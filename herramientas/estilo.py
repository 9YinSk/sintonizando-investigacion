"""Entender una imagen con datos: paleta medida, cómo está pintada y etiquetas.

Para vestuario, fondos, estilo de dibujo y la guía para IA. De cada imagen
(archivo o URL) saca:
- **paleta**: los colores dominantes en hex con su % (y una tira de muestras);
- **estilo**: saturación y brillo medios, si el sombreado es plano (cel) o en
  degradado, cuánta línea hay y de qué color es la línea;
- con --etiquetas, **etiquetas de anime** (pelo, ropa, pose, expresión,
  personaje) con el modelo WD14 en local: el vocabulario que entienden las IA
  de imagen, útil para el punto 17.

    python3 herramientas/estilo.py fotograma.jpg arte.png --salida /trabajo/estilo
    python3 herramientas/estilo.py "https://static.wikia.nocookie.net/…" --etiquetas --salida …

Deja en --salida: `paleta_<n>.png` (tira de colores) y `estilo.json`.
Los datos ayudan a describir; la imagen se MIRA igual (Read).
Necesita Pillow, numpy, opencv; con --etiquetas, onnxruntime y huggingface_hub.
"""
import argparse
import csv
import io
import json
import sys
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def abrir(fuente):
    if fuente.startswith("http"):
        pet = urllib.request.Request(fuente, headers={"User-Agent": "Mozilla/5.0",
                                                      "Referer": "https://www.fandom.com/"})
        return Image.open(io.BytesIO(urllib.request.urlopen(pet, timeout=60).read())).convert("RGB")
    return Image.open(fuente).convert("RGB")


def paleta(im, n=8):
    peq = im.copy()
    peq.thumbnail((400, 400))
    q = peq.quantize(colors=n, method=Image.Quantize.MEDIANCUT, kmeans=2)
    pal = q.getpalette()[: n * 3]
    cuenta = sorted(q.getcolors(), reverse=True)
    total = sum(c for c, _ in cuenta)
    return [{"hex": "#{:02X}{:02X}{:02X}".format(*pal[i * 3:i * 3 + 3]), "pct": round(100 * c / total, 1)}
            for c, i in cuenta]


def tira(colores, ruta):
    alto, ancho = 90, 110
    img = Image.new("RGB", (ancho * len(colores), alto), "white")
    d = ImageDraw.Draw(img)
    try:
        letra = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
    except OSError:
        letra = ImageFont.load_default()
    for k, c in enumerate(colores):
        d.rectangle((k * ancho, 0, (k + 1) * ancho, alto - 26), fill=c["hex"])
        d.text((k * ancho + 6, alto - 22), f"{c['hex']} {c['pct']}%", fill="black", font=letra)
    img.save(ruta)


def medir_estilo(im):
    import cv2
    a = np.asarray(im.resize((min(im.width, 1024), int(im.height * min(im.width, 1024) / im.width))))
    hsv = cv2.cvtColor(a, cv2.COLOR_RGB2HSV)
    gris = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY)
    bordes = cv2.Canny(gris, 80, 160)
    dens = float((bordes > 0).mean())
    # color de la línea: píxeles de borde que además son oscuros respecto a su entorno
    borde_osc = (bordes > 0) & (gris < cv2.GaussianBlur(gris, (9, 9), 0) - 10)
    linea = a[borde_osc]
    color_linea = "#{:02X}{:02X}{:02X}".format(*np.median(linea, axis=0).astype(int)) if len(linea) > 50 else None
    # plano o degradado: cuánto del área (sin bordes) cambia suave pero no es plano
    gx = cv2.Sobel(gris, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(gris, cv2.CV_32F, 0, 1)
    mag = np.hypot(gx, gy)[bordes == 0]
    plano = float((mag < 4).mean())
    suave = float(((mag >= 4) & (mag < 40)).mean())
    return {
        "saturacion_media": round(float(hsv[..., 1].mean()) / 2.55),
        "brillo_medio": round(float(hsv[..., 2].mean()) / 2.55),
        "zonas_planas_pct": round(100 * plano), "degradado_pct": round(100 * suave),
        "sombreado": "plano (cel)" if plano > 0.6 else "degradado / pintado" if suave > 0.45 else "mixto",
        "densidad_linea_pct": round(100 * dens, 1),
        "linea": "mucha línea" if dens > 0.12 else "línea normal" if dens > 0.05 else "poca línea",
        "color_linea": color_linea,
    }


_tagger = None


def etiquetas(im, umbral=0.35):
    global _tagger
    import onnxruntime as ort
    from huggingface_hub import hf_hub_download
    if _tagger is None:
        repo = "SmilingWolf/wd-vit-tagger-v3"
        sesion = ort.InferenceSession(hf_hub_download(repo, "model.onnx"), providers=["CPUExecutionProvider"])
        with open(hf_hub_download(repo, "selected_tags.csv"), encoding="utf-8") as f:
            tags = [(r["name"], int(r["category"])) for r in csv.DictReader(f)]
        _tagger = (sesion, tags)
    sesion, tags = _tagger
    lado = sesion.get_inputs()[0].shape[1]
    lienzo = Image.new("RGB", (max(im.size),) * 2, "white")
    lienzo.paste(im, ((lienzo.width - im.width) // 2, (lienzo.height - im.height) // 2))
    x = np.asarray(lienzo.resize((lado, lado), Image.BICUBIC), dtype=np.float32)[:, :, ::-1][None]
    prob = sesion.run(None, {sesion.get_inputs()[0].name: np.ascontiguousarray(x)})[0][0]
    general = sorted(((p, n) for p, (n, c) in zip(prob, tags) if c == 0 and p >= umbral), reverse=True)
    persona = sorted(((p, n) for p, (n, c) in zip(prob, tags) if c == 4 and p >= 0.6), reverse=True)
    return {"generales": [f"{n} ({p:.2f})" for p, n in general],
            "personaje": [f"{n} ({p:.2f})" for p, n in persona]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("imagenes", nargs="+", help="archivos o URLs")
    ap.add_argument("--salida", required=True)
    ap.add_argument("--colores", type=int, default=8)
    ap.add_argument("--etiquetas", action="store_true", help="etiquetas de anime con WD14 (baja ~400 MB la 1.ª vez)")
    a = ap.parse_args()
    carpeta = Path(a.salida)
    carpeta.mkdir(parents=True, exist_ok=True)
    datos = []
    for k, fuente in enumerate(a.imagenes, 1):
        try:
            im = abrir(fuente)
        except Exception as e:                                          # noqa: BLE001
            print(f"{fuente}: no se pudo abrir ({e})")
            continue
        d = {"fuente": fuente, "ancho": im.width, "alto": im.height,
             "paleta": paleta(im, a.colores), "estilo": medir_estilo(im)}
        if a.etiquetas:
            d["etiquetas"] = etiquetas(im)
        tira(d["paleta"], carpeta / f"paleta_{k:02d}.png")
        datos.append(d)
        e = d["estilo"]
        print(f"\n[{k}] {fuente}  ({im.width}×{im.height})")
        print("  paleta: " + "  ".join(f"{c['hex']} {c['pct']}%" for c in d["paleta"]))
        print(f"  estilo: sombreado {e['sombreado']}, {e['linea']} (línea {e['color_linea']}), "
              f"saturación {e['saturacion_media']}%, brillo {e['brillo_medio']}%")
        if a.etiquetas:
            print("  etiquetas: " + ", ".join(d["etiquetas"]["generales"][:30]))
            if d["etiquetas"]["personaje"]:
                print("  personaje: " + ", ".join(d["etiquetas"]["personaje"]))
    (carpeta / "estilo.json").write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n→ {carpeta}")


if __name__ == "__main__":
    main()
