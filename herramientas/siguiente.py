"""¿Qué toca ahora? Lista el trabajo pendiente en el orden de ESTADO.md.

    python3 herramientas/siguiente.py        # las 10 siguientes
    python3 herramientas/siguiente.py 3      # las 3 siguientes
    python3 herramientas/siguiente.py 5 --lote D   # sólo las del lote D (REPARTO.md)

Orden: 1) series con partes/ a medias o con las partes listas y sin biblia
(se sigue lo empezado), 2) casi completas a las que sólo faltan los puntos
18-25 (repaso corto), 3) nuevas empezadas, 4) repasos 06-30, 5) series nuevas
por número. Dice el modo para la skill serie-en-equipo: «seguir» (relanzar
sólo los roles a medias o que faltan), «redactar» (las 4 partes listas: sólo
el redactor), «repaso-corto», «nueva» o «repaso».
Si hay un archivo .lote en la raíz y no se pasa --lote, se usa esa letra.
Una línea «Sigue:» sólo cuenta como pendiente si dice algo obligatorio
(«Sigue: nada pendiente» no cuenta).
"""
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "herramientas"))
from revisar import revisar  # noqa: E402


LOTES = {"A": [(2, 5), (31, 36)], "B": [(6, 18)], "C": [(19, 30)], "D": [(37, 56)], "E": [(57, 76)],
         "F": [(77, 96)], "G": [(97, 116)], "H": [(117, 131)]}
ROLES = {"imagen", "video", "voz", "texto"}
SIGUE = re.compile(r"^(?:#+\s*)?Sigue:\s*(.*)$", re.M)
NADA = re.compile(r"^(nada|ningun|ninguna|no queda|no hay|sin pendientes|sin nada|listo|completo|—|-\s*$|$)", re.I)


def num(i):
    return int(i.split("-")[0])


def pendiente(texto):
    """¿La parte está a medias? Marcas _(pendiente)_/_(en curso)_ o una línea
    «Sigue:» que pida algo de verdad («Sigue: nada obligatorio pendiente» no)."""
    if re.search(r"_\((pendiente|en curso)\)_", texto):
        return True
    return any(not NADA.match(m.group(1).strip()) for m in SIGUE.finditer(texto))


def main():
    args = sys.argv[1:]
    lote = ""
    if "--lote" in args:
        i = args.index("--lote")
        lote = args[i + 1].strip().upper() if i + 1 < len(args) else ""
        del args[i:i + 2]
    if not lote and (RAIZ / ".lote").exists():
        lote = (RAIZ / ".lote").read_text(encoding="utf-8").strip().upper()[:1]
    nums = [a for a in args if a.isdigit()]
    n = int(nums[0]) if nums else 10
    encargos = sorted((p.stem for p in (RAIZ / "encargos").glob("*.md") if p.stem[:1].isdigit()), key=num)
    if lote:
        rangos = LOTES.get(lote)
        if not rangos:
            sys.exit(f"lote desconocido: «{lote}» (valen {', '.join(LOTES)})")
        encargos = [e for e in encargos if any(a <= num(e) <= b for a, b in rangos)]
    cola = []
    for id in encargos:
        d = RAIZ / "biblias" / id
        partes = sorted(p for p in (d / "partes").glob("*.md") if not p.stem.startswith("datos-")) if (d / "partes").exists() else []
        a_medias = [p.stem for p in partes if pendiente(p.read_text(encoding="utf-8"))]
        listas = {p.stem for p in partes} - set(a_medias)
        if not (d / "biblia.md").exists():
            if partes and not a_medias and ROLES <= listas:
                cola.append((1, num(id), id, "redactar", f"partes listas ({', '.join(sorted(listas))}): sólo el redactor"))
            elif partes:
                faltan = sorted(ROLES - listas - set(a_medias))
                cola.append((1, num(id), id, "seguir", "sin biblia · " + " · ".join(
                    x for x in (f"partes a medias: {', '.join(a_medias)}" if a_medias else "",
                                f"faltan roles: {', '.join(faltan)}" if faltan else "") if x)))
            else:
                cola.append((5, num(id), id, "nueva", "sin biblia"))
            continue
        falta = revisar(id, solo_falta=True)
        if not falta:
            continue
        texto = ", ".join(falta)
        if a_medias:
            cola.append((1, num(id), id, "seguir", f"partes a medias: {', '.join(a_medias)} · {texto}"))
        elif all(f == "puntos 18-25" or f.startswith(("fuentes distintas", "minutos citados", "colores hex")) for f in falta):
            cola.append((2, num(id), id, "repaso-corto", texto))
        elif ROLES <= listas:
            cola.append((3, num(id), id, "redactar", f"biblia con faltas ({texto}); partes listas: sólo el redactor, editando en su sitio"))
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
