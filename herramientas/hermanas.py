"""Series «hermanas»: la misma obra con dos encargos (otro enfoque), para que la
segunda parta de las partes de la primera y no repita la investigación.

    python3 herramientas/hermanas.py            # todas las parejas
    python3 herramientas/hermanas.py 90-kaguya-sama-love-is-war   # la hermana de una

Salida por línea: <id> <hermana> <qué tiene la hermana: biblia | partes | nada>
"""
import difflib
import os
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
# Parejas fijadas a mano (el título no basta: «Ghibli en general» no se parece a «Chihiro»)
FIJAS = {"90": "43", "104": "64", "101": "52", "103": "55", "107": "53", "102": "98", "98": "51", "89": "33", "79": "31", "80": "03"}


def norm(s):
    s = re.sub(r"^\d+-", "", s)
    s = re.sub(r"-(paisajes|el-sistema|cielos|comedia|y-|la-|el-|de-|en-general).*$", "", s)
    return re.sub(r"[^a-z0-9]", "", s.lower())


def estado(id):
    d = RAIZ / "biblias" / id
    if (d / "biblia.md").exists():
        return "biblia"
    if (d / "partes").exists() and any(p.suffix == ".md" and not p.name.startswith("datos-") for p in (d / "partes").iterdir()):
        return "partes"
    return "nada"


def main():
    ids = sorted(p.stem for p in (RAIZ / "encargos").glob("*.md") if p.stem[:1].isdigit())
    por_num = {i.split("-")[0]: i for i in ids}
    parejas = {}
    for i in ids:
        n = i.split("-")[0]
        if n in FIJAS and FIJAS[n] in por_num:
            parejas[i] = por_num[FIJAS[n]]
            continue
        for j in ids:
            if j != i and int(j.split("-")[0]) < int(n) and difflib.SequenceMatcher(None, norm(i), norm(j)).ratio() >= 0.9:
                parejas[i] = j
                break
    pedidos = sys.argv[1:] or sorted(parejas)
    for i in pedidos:
        h = parejas.get(i)
        if h:
            print(f"{i} {h} {estado(h)}")
        elif sys.argv[1:]:
            print(f"{i} - sin hermana")


if __name__ == "__main__":
    main()
