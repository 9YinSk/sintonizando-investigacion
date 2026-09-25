"""Mide las partes de los investigadores ANTES de pagar el redactor: líneas,
webs distintas, minutos, hex, ✅/⚠️, «Sigue:» pendiente y hojas. Dice qué rol
está flojo para relanzarlo en modo seguir en vez de mandar al redactor partes
vacías.

    python3 herramientas/revisar_partes.py 43-kaguya-sama-love-is-war
    python3 herramientas/revisar_partes.py 43-kaguya-sama-love-is-war --json
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "herramientas"))
from siguiente import pendiente  # noqa: E402

ROLES = ["imagen", "video", "voz", "texto"]
# mínimos para no ser «floja» (una parte normal tiene 150-700 líneas y 20-40 webs)
MIN = {"lineas": 80, "webs": 8}
MIN_WEBS = {"imagen": 8, "texto": 8, "video": 5, "voz": 6}
MIN_MINUTOS = {"video": 6, "voz": 3}  # los roles que citan escenas
MIN_HEX = {"imagen": 5}


def medir(id, rol):
    p = RAIZ / "biblias" / id / "partes" / f"{rol}.md"
    if not p.exists():
        return {"rol": rol, "existe": False, "floja": True, "por_que": "no existe"}
    t = p.read_text(encoding="utf-8")
    m = {
        "rol": rol, "existe": True, "lineas": t.count("\n"),
        "webs": len({re.sub(r"^www\.", "", d.lower()) for d in re.findall(r"https?://([^/\s)\]>»]+)", t)}),
        "minutos": len(re.findall(r"(?<![\d:])(?:\d{1,2}:)?\d{1,2}:\d{2}(?![\d:])", t)),
        "hex": len(set(h.upper() for h in re.findall(r"#[0-9A-Fa-f]{6}\b", t))),
        "ok": t.count("✅"), "dudosos": t.count("⚠️"), "sigue": pendiente(t),
        "json": (p.with_suffix(".json")).exists(),
    }
    if rol == "imagen":
        h = RAIZ / "biblias" / id / "hojas"
        m["hojas"] = len([x for x in h.iterdir() if x.is_file()]) if h.exists() else 0
    faltas = []
    if m["lineas"] < MIN["lineas"]: faltas.append(f"{m['lineas']} líneas")
    if m["webs"] < MIN_WEBS.get(rol, MIN["webs"]): faltas.append(f"{m['webs']} webs")
    if rol in MIN_MINUTOS and m["minutos"] < MIN_MINUTOS[rol]: faltas.append(f"{m['minutos']} minutos citados")
    if rol in MIN_HEX and m["hex"] < MIN_HEX[rol]: faltas.append(f"{m['hex']} hex")
    if m["sigue"]: faltas.append("Sigue: con obligatorio pendiente")
    if not m["json"] and rol != "voz": faltas.append("sin .json de referencias")
    m["floja"] = bool(faltas)
    m["por_que"] = ", ".join(faltas)
    return m


def main():
    id = sys.argv[1]
    roles = [a for a in sys.argv[2:] if a in ROLES] or ROLES
    res = [medir(id, r) for r in roles]
    if "--json" in sys.argv:
        print(json.dumps({"id": id, "partes": res, "flojas": [r["rol"] for r in res if r["floja"]]}, ensure_ascii=False))
        return
    for r in res:
        if not r["existe"]:
            print(f"{r['rol']:7} NO EXISTE"); continue
        print(f"{r['rol']:7} {r['lineas']:4} lín {r['webs']:3} webs {r['minutos']:3} min {r['hex']:3} hex ✅{r['ok']:3} ⚠️{r['dudosos']:3}"
              f"{'  hojas ' + str(r['hojas']) if 'hojas' in r else ''}  {'FLOJA: ' + r['por_que'] if r['floja'] else 'bien'}")


if __name__ == "__main__":
    main()
