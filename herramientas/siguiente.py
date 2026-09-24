"""¿Qué toca ahora? Lista el trabajo pendiente en el orden de ESTADO.md.

    python3 herramientas/siguiente.py        # las 10 siguientes
    python3 herramientas/siguiente.py 3      # las 3 siguientes

Orden: 1) series con partes/ a medias (se sigue lo empezado), 2) casi completas
a las que sólo faltan los puntos 18-25 (repaso corto), 3) nuevas empezadas,
4) repasos 06-30, 5) series nuevas por número. Dice el modo para la skill
serie-autonoma: «seguir», «repaso-corto», «nueva» o «repaso».
"""
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "herramientas"))
from revisar import revisar  # noqa: E402


def num(i):
    return int(i.split("-")[0])


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    encargos = sorted((p.stem for p in (RAIZ / "encargos").glob("*.md") if p.stem[:1].isdigit()), key=num)
    cola = []
    for id in encargos:
        d = RAIZ / "biblias" / id
        if not (d / "biblia.md").exists():
            cola.append((5, num(id), id, "nueva", "sin biblia"))
            continue
        falta = revisar(id, solo_falta=True)
        if not falta:
            continue
        partes = list((d / "partes").glob("*.md")) if (d / "partes").exists() else []
        a_medias = [p.stem for p in partes if not p.stem.startswith("datos-")
                    and re.search(r"_\((pendiente|en curso)\)_|^Sigue:", p.read_text(encoding="utf-8"), re.M)]
        texto = ", ".join(falta)
        if a_medias:
            cola.append((1, num(id), id, "seguir", f"partes a medias: {', '.join(a_medias)} · {texto}"))
        elif falta == ["puntos 18-25"]:
            cola.append((2, num(id), id, "repaso-corto", "sólo faltan los puntos 18-25"))
        elif num(id) > 30:
            cola.append((3, num(id), id, "nueva", texto))
        else:
            cola.append((4, num(id), id, "repaso", texto))
    cola.sort()
    total = len(cola)
    for _, _, id, modo, por in cola[:n]:
        print(f"{id:40} {modo:13} {por[:110]}")
    print(f"\n{total} pendientes de {len(encargos)} series.")


if __name__ == "__main__":
    main()
