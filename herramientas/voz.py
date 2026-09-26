"""Escuchar una voz de verdad: transcripción con minuto y ficha de la voz.

Para el doblaje: saca la frase TEXTUAL con su minuto (Whisper, en local) y mide
cómo suena la voz (tono, rango, velocidad, pausas) para describir al personaje
con datos y no «de memoria».

    python3 herramientas/voz.py "https://…clip doblado…" --salida /trabajo/voz_luffy
    python3 herramientas/voz.py audio.mp3 --desde 30 --hasta 75 --idioma es --salida …

Deja en --salida: `transcripcion.txt` (una línea por frase con [minuto] y
enlace &t=), `transcripcion.srt`, `ficha_voz.json` y un resumen en pantalla.
Con música o efectos de fondo el tono sale menos fiable: mejor clips donde el
personaje habla solo. Whisper se equivoca en nombres propios: la frase que se
cite en la biblia se revisa escuchando o con una segunda transcripción.
Necesita faster-whisper, praat-parselmouth, ffmpeg y yt-dlp.
"""
import argparse
import json
import math
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from fotogramas import galletas, minuto  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def bajar_audio(url, carpeta):
    destino = carpeta / "audio.m4a"
    if not destino.exists():
        orden = ["yt-dlp", "-q", "--no-warnings", "--js-runtimes", "node", *galletas(),
                 "-f", "ba/b", "-x", "--audio-format", "m4a", "-o", str(carpeta / "audio.%(ext)s"), url]
        r = subprocess.run(orden, capture_output=True, text=True)
        if r.returncode or not destino.exists():
            sys.exit(f"yt-dlp no pudo bajar el audio:\n{r.stderr[-800:]}")
    return destino


def a_wav(fuente, carpeta, desde, hasta):
    wav = carpeta / "voz.wav"
    orden = ["ffmpeg", "-loglevel", "error", "-y"]
    if desde:
        orden += ["-ss", str(desde)]
    if hasta:
        orden += ["-to", str(hasta)]
    orden += ["-i", str(fuente), "-ac", "1", "-ar", "16000", str(wav)]
    subprocess.run(orden, check=True)
    return wav


def tono(wav):
    import parselmouth
    snd = parselmouth.Sound(str(wav))
    f0 = snd.to_pitch(time_step=0.01, pitch_floor=70, pitch_ceiling=600).selected_array["frequency"]
    f0 = sorted(x for x in f0 if x > 0)
    if len(f0) < 20:
        return None
    q = lambda p: f0[int(p * (len(f0) - 1))]
    med, p10, p90 = q(0.5), q(0.1), q(0.9)
    semitonos = 12 * math.log2(p90 / p10)
    return {
        "tono_medio_hz": round(med), "p10_hz": round(p10), "p90_hz": round(p90),
        "rango_semitonos": round(semitonos, 1),
        "registro": "grave" if med < 140 else "medio" if med < 220 else "agudo" if med < 320 else "muy agudo",
        "expresividad": "monótona" if semitonos < 4 else "normal" if semitonos < 8 else "muy expresiva",
        "segundos_con_voz": round(len(f0) * 0.01, 1),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fuente", help="URL (YouTube, Dailymotion, Doblaje Wiki…) o archivo de audio/vídeo")
    ap.add_argument("--salida", required=True)
    ap.add_argument("--desde", type=float, default=0)
    ap.add_argument("--hasta", type=float, default=0)
    ap.add_argument("--idioma", default="es", help="es, ja, en… (vacío = detectar)")
    ap.add_argument("--modelo", default="small", help="tiny, base, small, medium (más grande = mejor y más lento)")
    a = ap.parse_args()

    carpeta = Path(a.salida)
    carpeta.mkdir(parents=True, exist_ok=True)
    es_url = a.fuente.startswith("http")
    fuente = bajar_audio(a.fuente, carpeta) if es_url else Path(a.fuente)
    wav = a_wav(fuente, carpeta, a.desde, a.hasta)
    enlace = (lambda t: f"{a.fuente}{'&' if '?' in a.fuente else '?'}t={int(t)}") if es_url else (lambda t: "")

    from faster_whisper import WhisperModel
    modelo = WhisperModel(a.modelo, device="cpu", compute_type="int8")
    trozos, info = modelo.transcribe(str(wav), language=a.idioma or None, word_timestamps=True,
                                     vad_filter=True)
    lineas, srt, palabras, habla = [], [], 0, 0.0
    for i, s in enumerate(trozos, 1):
        t0, t1 = s.start + a.desde, s.end + a.desde
        texto = s.text.strip()
        palabras += len(texto.split())
        habla += s.end - s.start
        lineas.append(f"[{minuto(t0)}] {texto}  {enlace(t0)}".rstrip())
        f = lambda t: f"{int(t // 3600):02d}:{int(t % 3600 // 60):02d}:{int(t % 60):02d},{int(t % 1 * 1000):03d}"
        srt.append(f"{i}\n{f(t0)} --> {f(t1)}\n{texto}\n")
    (carpeta / "transcripcion.txt").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    (carpeta / "transcripcion.srt").write_text("\n".join(srt), encoding="utf-8")

    ficha = {"fuente": a.fuente, "desde": a.desde, "hasta": a.hasta, "idioma": info.language,
             "palabras": palabras,
             "palabras_por_segundo": round(palabras / habla, 2) if habla else None,
             "tono": tono(wav)}
    if ficha["palabras_por_segundo"]:
        v = ficha["palabras_por_segundo"]
        ficha["velocidad"] = "lenta" if v < 2 else "normal" if v < 3 else "rápida" if v < 4 else "muy rápida"
    (carpeta / "ficha_voz.json").write_text(json.dumps(ficha, ensure_ascii=False, indent=1), encoding="utf-8")

    print("\n".join(lineas))
    t = ficha["tono"] or {}
    print(f"\nVoz: registro {t.get('registro', '?')} ({t.get('tono_medio_hz', '?')} Hz), "
          f"{t.get('expresividad', '?')} ({t.get('rango_semitonos', '?')} semitonos), "
          f"velocidad {ficha.get('velocidad', '?')} ({ficha['palabras_por_segundo']} palabras/s) → {carpeta}")


if __name__ == "__main__":
    main()
