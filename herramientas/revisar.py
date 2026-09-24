#!/usr/bin/env python3
"""Dice qué biblias están completas según las reglas actuales.

Una biblia está COMPLETA cuando tiene la tabla «Cumplimiento del encargo» sin
ningún ❌, 20 referencias o más en referencias.json, 3 hojas en hojas/ y, si es
una de las 01-30, la sección «Segunda pasada · qué cambió».
Los ⚠️ no impiden que esté completa: son datos con una sola fuente o que hay
que oír/ver en persona (se listan para que el dueño sepa qué falta confirmar).

    python3 herramientas/revisar.py            # todas
    python3 herramientas/revisar.py 33-frieren # una
"""
import json, os, re, sys

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def revisar(id):
    d = f"biblias/{id}"
    t = open(f"{d}/biblia.md", encoding="utf-8").read()
    m = re.search(r"^#+ .*Cumplimiento del encargo.*$", t, re.M)
    ok = wa = no = 0
    if m:
        seg = t[m.end():]
        fin = re.search(r"^#{1,2} ", seg, re.M)
        for l in (seg[:fin.start()] if fin else seg).split("\n"):
            if l.startswith("|"):
                if "❌" in l: no += 1
                elif "⚠️" in l: wa += 1
                elif "✅" in l: ok += 1
    try:
        refs = len(json.load(open(f"{d}/referencias.json", encoding="utf-8")))
    except Exception:
        refs = 0
    hojas = len(os.listdir(f"{d}/hojas")) if os.path.isdir(f"{d}/hojas") else 0
    num = int(id.split("-")[0]) if id[:2].isdigit() else 999
    repaso = "Segunda pasada · qué cambió" in t
    falta = []
    if not m: falta.append("tabla de cumplimiento")
    if no: falta.append(f"{no} puntos ❌")
    if refs < 20: falta.append(f"referencias ({refs})")
    if hojas != 3: falta.append(f"hojas ({hojas})")
    if num <= 30 and not repaso: falta.append("segunda pasada")
    estado = "COMPLETA" if not falta else "falta: " + ", ".join(falta)
    return f"{id[:30]:30} {len(t.splitlines()):5} lín  ⚠️{t.count('⚠️'):4}  tabla ✅{ok} ⚠️{wa} ❌{no}  {estado}"


ids = sys.argv[1:] or sorted(i for i in os.listdir("biblias") if os.path.exists(f"biblias/{i}/biblia.md"))
for i in ids:
    print(revisar(i))
