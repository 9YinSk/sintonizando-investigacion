"""Mirar un vídeo de verdad: fotogramas cada N segundos en hojas numeradas con su minuto.

El dueño lo pidió así: «no miras vídeos ni descripciones, no te empapas del tema».
Este script baja el vídeo (YouTube u otro sitio que lea yt-dlp, o un archivo
local), saca un fotograma cada N segundos y monta hojas de contacto con el
número y el minuto de cada uno. Después se MIRAN las hojas (Read de la imagen)
y en la biblia se cita el minuto exacto con su enlace `&t=`.

    python3 herramientas/fotogramas.py "https://www.youtube.com/watch?v=XXXX" \
        --cada 4 --salida /ruta/de/trabajo/opening
    python3 herramientas/fotogramas.py video.mp4 --desde 60 --hasta 180 --cada 2 --salida …
    python3 herramientas/fotogramas.py "https://…" --salida … --fotograma 83.5   # uno en grande

Deja en --salida: `hoja_01.jpg`… (48 fotogramas por hoja), `indice.json`
(número, segundo, minuto y enlace) y, con --fotograma, `fotograma_<seg>.jpg`.
Necesita yt-dlp, ffmpeg (o imageio-ffmpeg) y Pillow.
"""
import argparse
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def ffmpeg():
    if shutil.which("ffmpeg"):
        return "ffmpeg"
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def minuto(s):
    s = int(s)
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60}:{s % 60:02d}"


def bajar(url, carpeta):
    """Vídeo sin audio hasta 720p (basta para mirar) en carpeta/video.mp4."""
    destino = carpeta / "video.mp4"
    if destino.exists():
        return destino
    formato = "bv*[height<=720][vcodec^=avc1]/bv*[height<=720]/b[height<=720]/b"
    orden = ["yt-dlp", "-q", "--no-warnings", "--js-runtimes", "node", "-f", formato,
             "-o", str(destino), url]
    r = subprocess.run(orden, capture_output=True, text=True)
    if r.returncode or not destino.exists():
        sys.exit(f"yt-dlp no pudo bajarlo (si dice 429, espera un minuto):\n{r.stderr[-800:]}")
    return destino


def duracion(video):
    r = subprocess.run([ffmpeg(), "-i", str(video)], capture_output=True, text=True)
    for linea in r.stderr.splitlines():
        if "Duration:" in linea:
            h, m, s = linea.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    return 0.0


def sacar(video, t, ruta, ancho):
    subprocess.run([ffmpeg(), "-loglevel", "error", "-y", "-ss", f"{t:.2f}", "-i", str(video),
                    "-frames:v", "1", "-vf", f"scale={ancho}:-2", "-q:v", "3", str(ruta)], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fuente", help="URL (YouTube…) o archivo de vídeo")
    ap.add_argument("--salida", required=True)
    ap.add_argument("--cada", type=float, default=5, help="segundos entre fotogramas")
    ap.add_argument("--desde", type=float, default=0)
    ap.add_argument("--hasta", type=float, default=0)
    ap.add_argument("--fotograma", type=float, nargs="*", help="sacar sólo estos segundos, a 1280 px")
    a = ap.parse_args()

    carpeta = Path(a.salida)
    carpeta.mkdir(parents=True, exist_ok=True)
    es_url = a.fuente.startswith("http")
    video = bajar(a.fuente, carpeta) if es_url else Path(a.fuente)
    enlace = (lambda t: f"{a.fuente}{'&' if '?' in a.fuente else '?'}t={int(t)}") if es_url else (lambda t: "")

    if a.fotograma:
        for t in a.fotograma:
            r = carpeta / f"fotograma_{int(t):05d}.jpg"
            sacar(video, t, r, 1280)
            print(f"{minuto(t)}  {r}  {enlace(t)}")
        return

    fin = a.hasta or duracion(video)
    tiempos = [a.desde + i * a.cada for i in range(int((fin - a.desde) / a.cada) + 1) if a.desde + i * a.cada < fin]
    tmp = carpeta / "cuadros"
    tmp.mkdir(exist_ok=True)
    try:
        letra = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
    except OSError:
        letra = ImageFont.load_default()

    indice, por_hoja, cols, celda = [], 48, 6, (320, 180)
    for h in range(math.ceil(len(tiempos) / por_hoja)):
        tanda = tiempos[h * por_hoja:(h + 1) * por_hoja]
        filas = math.ceil(len(tanda) / cols)
        hoja = Image.new("RGB", (cols * celda[0], filas * celda[1]), (20, 20, 24))
        d = ImageDraw.Draw(hoja)
        for k, t in enumerate(tanda):
            n = h * por_hoja + k + 1
            r = tmp / f"{n:04d}.jpg"
            try:
                sacar(video, t, r, celda[0])
                im = Image.open(r).convert("RGB")
                im.thumbnail(celda)
                x, y = (k % cols) * celda[0], (k // cols) * celda[1]
                hoja.paste(im, (x, y))
                etiqueta = f"{n} · {minuto(t)}"
                d.rectangle((x, y, x + 12 + 9 * len(etiqueta), y + 22), fill=(0, 0, 0))
                d.text((x + 5, y + 2), etiqueta, fill=(250, 210, 60), font=letra)
            except Exception:                                           # noqa: BLE001
                continue
            indice.append({"n": n, "segundo": round(t, 1), "minuto": minuto(t), "enlace": enlace(t)})
        ruta = carpeta / f"hoja_{h + 1:02d}.jpg"
        hoja.save(ruta, quality=85)
        print(ruta)
    (carpeta / "indice.json").write_text(json.dumps(indice, ensure_ascii=False, indent=1), encoding="utf-8")
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"{len(indice)} fotogramas de {minuto(a.desde)} a {minuto(fin)}, cada {a.cada} s → {carpeta}")


if __name__ == "__main__":
    main()
