"""Arma referencias.json de una serie sin IA: une partes/*.json (lo que eligieron
los investigadores) y datos.json (lo que trajo el recolector), quita repetidas
por URL y ordena: primero las de los investigadores, luego por tamaño.
El redactor NO tiene que teclearla; sólo quita con Edit las que no sirvan.

    python3 herramientas/juntar_referencias.py 41-dandadan
    python3 herramientas/juntar_referencias.py 41-dandadan --medir 40   # mide ancho/alto de hasta 40 imágenes sin tamaño
"""
import io
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

RAIZ = Path(__file__).resolve().parent.parent
CAMPOS = ["url", "fuente", "ancho", "alto", "que_es", "para_que", "licencia"]


def norm(url):
    u = urlsplit(url.strip())
    q = "&".join(p for p in u.query.split("&") if p and not p.lower().startswith(("utm_", "fbclid", "ref=")))
    return urlunsplit(("https", u.netloc.lower().replace("www.", ""), u.path.rstrip("/"), q, "")).lower()


def cargar(p):
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
        return [x for x in d if isinstance(x, dict) and x.get("url")] if isinstance(d, list) else []
    except Exception:  # noqa: BLE001
        return []


def medir(refs, n):
    import urllib.request
    from PIL import Image
    hechas = 0
    for r in refs:
        if hechas >= n:
            break
        if r.get("ancho") or not re.search(r"\.(jpe?g|png|webp|gif)(\?|$)", r["url"], re.I):
            continue
        try:
            datos = urllib.request.urlopen(urllib.request.Request(r["url"], headers={"User-Agent": "Mozilla/5.0"}), timeout=15).read(3_000_000)
            im = Image.open(io.BytesIO(datos))
            r["ancho"], r["alto"] = im.size
            hechas += 1
        except Exception:  # noqa: BLE001
            pass
    return hechas


def main():
    id = sys.argv[1]
    n_medir = int(sys.argv[sys.argv.index("--medir") + 1]) if "--medir" in sys.argv else 0
    d = RAIZ / "biblias" / id
    partes = d / "partes"
    vistas, out = {}, []
    fuentes = [p for p in sorted(partes.glob("*.json")) if p.name != "datos.json"] + [partes / "datos.json"]
    for prioridad, p in enumerate(fuentes):
        for r in cargar(p):
            k = norm(r["url"])
            fila = {c: r.get(c) for c in CAMPOS}
            fila["_p"] = 0 if p.name != "datos.json" else 1
            if k in vistas:
                viejo = out[vistas[k]]
                for c in CAMPOS:  # completa huecos con lo que traiga la repetida
                    if not viejo.get(c) and fila.get(c):
                        viejo[c] = fila[c]
                continue
            vistas[k] = len(out)
            out.append(fila)
    if n_medir:
        print(f"medidas {medir(out, n_medir)} imágenes")
    out.sort(key=lambda r: (r["_p"], -((r.get("ancho") or 0) * (r.get("alto") or 0))))
    for r in out:
        r.pop("_p", None)
    destino = d / "referencias.json"
    previas = cargar(destino) if destino.exists() else []
    propias = [r for r in previas if norm(r["url"]) not in vistas]  # las que añadió el redactor a mano se conservan
    final = out + propias
    destino.write_text(json.dumps(final, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"referencias.json: {len(final)} ({len(out)} de las partes y datos, {len(propias)} propias del redactor conservadas)")


if __name__ == "__main__":
    main()
