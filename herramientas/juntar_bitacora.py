"""Junta las bitácoras de las cuatro partes en partes/bitacora.md, con un
apartado por rol, para que el redactor la pegue en la biblia en vez de
reescribirla (revisar.py exige una sección «Bitácora» en biblia.md).

    python3 herramientas/juntar_bitacora.py 41-dandadan
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ROLES = ["imagen", "video", "voz", "texto"]


def seccion_bitacora(texto):
    m = re.search(r"^(#{1,4})\s*.*bit[áa]cora.*$", texto, re.M | re.I)
    if not m:
        return ""
    nivel = len(m.group(1))
    resto = texto[m.end():]
    fin = re.search(rf"^#{{1,{nivel}}}\s", resto, re.M)
    return (resto[:fin.start()] if fin else resto).strip()


def main():
    id = sys.argv[1]
    partes = RAIZ / "biblias" / id / "partes"
    trozos = []
    for rol in ROLES:
        p = partes / f"{rol}.md"
        if not p.exists():
            continue
        b = seccion_bitacora(p.read_text(encoding="utf-8"))
        if b:
            trozos.append(f"### Bitácora de {rol}\n\n{b}\n")
    if not trozos:
        sys.exit("ninguna parte tiene sección Bitácora")
    salida = partes / "bitacora.md"
    salida.write_text("## Bitácora\n\n" + "\n".join(trozos), encoding="utf-8")
    print(f"partes/bitacora.md: {sum(t.count(chr(10)) for t in trozos)} líneas de {len(trozos)} roles")


if __name__ == "__main__":
    main()
