"""Leer sólo un trozo de una biblia (ahorra dinero: una biblia entera son ~45 mil tokens).

    python3 herramientas/seccion.py 01-one-piece --indice            # títulos, líneas y ⚠️ de cada sección
    python3 herramientas/seccion.py 01-one-piece --rol voz           # las secciones de un rol (imagen, video, voz, texto)
    python3 herramientas/seccion.py 01-one-piece vestuario 14        # por palabra del título o por número
    python3 herramientas/seccion.py 01-one-piece --rol imagen --avisos   # sólo las líneas con ⚠️ o ❌ de esas secciones

Una sección es un título `## `. Con --avisos sale cada línea dudosa con su número
de línea, para ir directo a corregirla.
"""
import argparse
import re
import signal
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
RAIZ = Path(__file__).resolve().parent.parent
ROLES = {
    "imagen": "arte oficial|fan art|fanart|3d|render|vestuario|ropa|traje|fondos de pantalla|wallpaper|textura|colabora|cruce|hojas de contacto|referencias",
    "video": "fotograma|escena|sitio|lugar|ciudad|paisaje|luz|musica|opening|ending|banda sonora|video|tendencia|tiktok|pose",
    "voz": "popular|encuesta|doblaje|frase|fandom|meme|no hacer|caracter|personaje|forma de hablar|gusto|detalle|por que|aman|fan dub|fandub|comunidad",
    "texto": "tipograf|letra|cuadro|dialogo|globo|cartela|videojuego|juego|interfaz|estilo|tecnica|replicar|parecid|relacionad|mundo|simbolo|emblema",
}


def normal(t):
    return "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")


def secciones(lineas):
    idx = [i for i, l in enumerate(lineas) if l.startswith("## ")] + [len(lineas)]
    return [(a, b, lineas[a][3:].strip()) for a, b in zip(idx, idx[1:])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id")
    ap.add_argument("buscar", nargs="*", help="palabras o números de sección")
    ap.add_argument("--indice", action="store_true")
    ap.add_argument("--rol", choices=ROLES)
    ap.add_argument("--avisos", action="store_true", help="sólo líneas con ⚠️ o ❌")
    a = ap.parse_args()
    ruta = RAIZ / "biblias" / a.id / "biblia.md"
    lineas = ruta.read_text(encoding="utf-8").split("\n")
    secs = secciones(lineas)
    if a.indice or not (a.buscar or a.rol):
        print(f"{ruta} · {len(lineas)} líneas")
        for x, y, t in secs:
            bloque = "\n".join(lineas[x:y])
            print(f"  l.{x + 1:5}  {y - x:4} lín  ⚠️{bloque.count('⚠️'):3}  {t}")
        return
    patrones = [normal(p) for p in a.buscar]
    if a.rol:
        patrones.append(ROLES[a.rol] + "|no pude|no encontr|verificar|dudoso")
    elegidas = []
    for x, y, t in secs:
        tn = normal(t)
        for p in patrones:
            if p.isdigit():
                if re.match(rf"^{p}\b", tn):
                    elegidas.append((x, y, t))
                    break
            elif re.search(p, tn):
                elegidas.append((x, y, t))
                break
    if not elegidas:
        sys.exit("Ninguna sección coincide. Mira --indice.")
    for x, y, t in elegidas:
        if a.avisos:
            dudosas = [(i + 1, lineas[i]) for i in range(x, y) if "⚠️" in lineas[i] or "❌" in lineas[i]]
            if dudosas:
                print(f"\n## {t}")
                for n, l in dudosas:
                    print(f"l.{n}: {l.strip()[:300]}")
        else:
            print(f"\n<!-- {a.id} · líneas {x + 1}-{y} -->")
            print("\n".join(lineas[x:y]))


if __name__ == "__main__":
    main()
