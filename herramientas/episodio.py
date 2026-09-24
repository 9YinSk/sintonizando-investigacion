"""Ver un capítulo entero sin gastar: una ficha de texto con todo lo que pasa, minuto a minuto.

Mirar un capítulo imagen por imagen llena la memoria del investigador y cuesta
mucho. Este programa lo hace gratis en el servidor: baja el capítulo (o el
trozo), saca un fotograma por plano en hojas numeradas, transcribe lo que se
dice con su minuto (Whisper) y, con --ocr, lee el texto que sale en pantalla
(tesseract). Junta todo en `ficha.md`: una línea por minuto con los planos
(número de hoja), lo que se dice y lo que se lee. El investigador lee la ficha
y abre SÓLO las hojas de los momentos que va a citar.

    python3 herramientas/episodio.py "https://archive.org/details/…" --titulo "One Piece ep. 53" \
        --idioma ja --salida /tmp/claude-0/trabajo/01-episodios/ep053 --id 01-one-piece
    python3 herramientas/episodio.py capitulo.mp4 --desde 1200 --hasta 1500 --idioma es --ocr --salida …

Con --id añade la ficha a biblias/<id>/partes/episodios.md. Borra el vídeo al
terminar (quedan hojas, transcripción y ficha). Necesita yt-dlp, ffmpeg,
PySceneDetect, faster-whisper y, con --ocr, tesseract.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from fotogramas import galletas, minuto  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def bajar(url, carpeta):
    destino = carpeta / "capitulo.mp4"
    if not destino.exists():
        orden = ["yt-dlp", "-q", "--no-warnings", "--js-runtimes", "node", *galletas(),
                 "-f", "b[height<=720]/bv*[height<=720]+ba/b", "--merge-output-format", "mp4",
                 "-o", str(destino), url]
        r = subprocess.run(orden, capture_output=True, text=True)
        if r.returncode or not destino.exists():
            sys.exit(f"yt-dlp no pudo bajarlo:\n{r.stderr[-800:]}")
    return destino


def recortar(video, carpeta, desde, hasta):
    """Trabaja sólo con el trozo pedido (más rápido); los minutos se corrigen después."""
    if not (desde or hasta):
        return video
    trozo = carpeta / "trozo.mp4"
    orden = ["ffmpeg", "-loglevel", "error", "-y", "-ss", str(desde)]
    if hasta:
        orden += ["-to", str(hasta)]
    subprocess.run(orden + ["-i", str(video), "-c", "copy", str(trozo)], check=True)
    return trozo


def ocr(video, tiempos, carpeta):
    """Texto en pantalla en el fotograma del medio de cada plano (sólo líneas con letras de verdad)."""
    dir_ocr = carpeta / "ocr"
    dir_ocr.mkdir(exist_ok=True)
    visto, salida = set(), {}
    for t in tiempos:
        img = dir_ocr / f"{int(t * 10):06d}.png"
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{t:.2f}", "-i", str(video), "-frames:v", "1",
                        "-vf", "scale=1280:-2", str(img)], check=False)
        if not img.exists():
            continue
        r = subprocess.run(["tesseract", str(img), "-", "-l", "spa+jpn+eng", "--psm", "11"],
                           capture_output=True, text=True)
        lineas = [l.strip() for l in r.stdout.splitlines()
                  if len(re.sub(r"[^\w]", "", l)) >= 4 and sum(c.isalpha() for c in l) / max(len(l), 1) > 0.6]
        nuevas = [l for l in lineas if l not in visto]
        visto.update(nuevas)
        if nuevas:
            salida[t] = nuevas[:4]
    shutil.rmtree(dir_ocr, ignore_errors=True)
    return salida


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fuente", help="URL (Internet Archive, Dailymotion, AnimeThemes…) o archivo de vídeo")
    ap.add_argument("--salida", required=True)
    ap.add_argument("--titulo", default="")
    ap.add_argument("--idioma", default="ja", help="idioma del audio: ja, es, en…")
    ap.add_argument("--desde", type=float, default=0)
    ap.add_argument("--hasta", type=float, default=0)
    ap.add_argument("--modelo", default="small", help="Whisper: tiny, base, small, medium")
    ap.add_argument("--ocr", action="store_true", help="leer también el texto en pantalla (más lento)")
    ap.add_argument("--id", help="añadir la ficha a biblias/<id>/partes/episodios.md")
    ap.add_argument("--guardar-video", action="store_true")
    a = ap.parse_args()

    carpeta = Path(a.salida)
    carpeta.mkdir(parents=True, exist_ok=True)
    es_url = a.fuente.startswith("http")
    video = bajar(a.fuente, carpeta) if es_url else Path(a.fuente)
    trozo = recortar(video, carpeta, a.desde, a.hasta)

    # 1 · un fotograma por plano, en hojas numeradas
    r = subprocess.run([sys.executable, str(AQUI / "fotogramas.py"), str(trozo), "--cortes", "--salida",
                        str(carpeta / "hojas")], capture_output=True, text=True)
    print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-400:])
    planos = json.loads((carpeta / "hojas" / "indice.json").read_text(encoding="utf-8"))
    for p in planos:
        p["hoja"] = (p["n"] - 1) // 48 + 1
        p["segundo"] += a.desde

    # 2 · lo que se dice, con minuto
    subprocess.run([sys.executable, str(AQUI / "voz.py"), str(trozo), "--idioma", a.idioma, "--modelo", a.modelo,
                    "--salida", str(carpeta / "voz")], capture_output=True, text=True)
    dichos = []
    ruta_srt = carpeta / "voz" / "transcripcion.srt"
    if ruta_srt.exists():
        for bloque in ruta_srt.read_text(encoding="utf-8").split("\n\n"):
            m = re.search(r"(\d+):(\d+):(\d+),\d+ -->.*\n(.+)", bloque)
            if m:
                s = int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3])
                dichos.append((s + a.desde, m[4].strip()))

    # 3 · texto en pantalla
    textos = ocr(trozo, [p["segundo"] - a.desde for p in planos], carpeta) if a.ocr else {}
    textos = {t + a.desde: v for t, v in textos.items()}

    # 4 · la ficha, minuto a minuto
    enlace = (lambda s: f"{a.fuente}{'&' if '?' in a.fuente else '?'}t={int(s)}") if es_url else (lambda s: "")
    fin = max([p["segundo"] for p in planos] + [d[0] for d in dichos] + [a.desde])
    ficha = [f"## {a.titulo or a.fuente}", "",
             f"_Fuente: {a.fuente} · {len(planos)} planos · audio en «{a.idioma}» transcrito con Whisper "
             f"({a.modelo}; revisar nombres propios) · hojas en {carpeta / 'hojas'}_", "",
             "| Minuto | Planos (hoja · n.º) | Se dice | Se lee en pantalla |", "|---|---|---|---|"]
    for m0 in range(int(a.desde // 60), int(fin // 60) + 1):
        en = lambda s: m0 * 60 <= s < (m0 + 1) * 60
        ps = [p for p in planos if en(p["segundo"])]
        ds = [d for s, d in dichos if en(s)]
        ts = [x for s, v in sorted(textos.items()) if en(s) for x in v]
        if not (ps or ds or ts):
            continue
        hojas = ", ".join(f"h{h} · {min(p['n'] for p in ps if p['hoja'] == h)}-{max(p['n'] for p in ps if p['hoja'] == h)}"
                          for h in sorted({p["hoja"] for p in ps}))
        celda = lambda xs: " / ".join(x.replace("|", "¦") for x in xs)[:600]
        ficha.append(f"| [{minuto(m0 * 60)}]({enlace(m0 * 60)}) | {hojas} ({len(ps)}) | {celda(ds)} | {celda(ts)} |"
                     if es_url else f"| {minuto(m0 * 60)} | {hojas} ({len(ps)}) | {celda(ds)} | {celda(ts)} |")
    texto = "\n".join(ficha) + "\n"
    (carpeta / "ficha.md").write_text(texto, encoding="utf-8")
    if a.id:
        destino = AQUI.parent / "biblias" / a.id / "partes" / "episodios.md"
        destino.parent.mkdir(parents=True, exist_ok=True)
        previo = destino.read_text(encoding="utf-8") if destino.exists() else (
            "# Capítulos vistos con herramientas/episodio.py\n\nUna ficha por capítulo: planos, lo que se dice y lo "
            "que se lee, minuto a minuto. Abre sólo las hojas de los momentos que cites.\n")
        destino.write_text(previo.rstrip("\n") + "\n\n" + texto, encoding="utf-8")
    if not a.guardar_video:
        for v in (carpeta / "capitulo.mp4", carpeta / "trozo.mp4", carpeta / "voz" / "voz.wav"):
            v.unlink(missing_ok=True)
    print(f"→ {carpeta / 'ficha.md'} ({len(ficha) - 6} minutos con algo, {len(planos)} planos, {len(dichos)} frases, "
          f"{sum(len(v) for v in textos.values())} textos en pantalla)")


if __name__ == "__main__":
    main()
