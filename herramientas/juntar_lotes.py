#!/usr/bin/env python3
"""Copia a ESTADO.md, DECISIONES.md y COSTOS.md lo que traen los lotes/*.md.

Lo corre la central desde `herramientas/juntar.sh --marcar`. Cada archivo lleva
un bloque entre `<!-- lotes -->` y `<!-- /lotes -->` que se rehace entero cada
vez (lo de fuera del bloque no se toca):

- ESTADO.md: cuántas biblias están COMPLETAS y la sección «Estado» de cada lote.
- DECISIONES.md: la sección «Avisos para el dueño» de cada lote.
- COSTOS.md: la tabla de «Costos» de cada lote.

    python3 herramientas/juntar_lotes.py
"""
import datetime, os, re, sys

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, "herramientas")
from revisar import revisar

INI, FIN = "<!-- lotes -->", "<!-- /lotes -->"


def secciones(t):
    """{título de cada «## …»: su texto, sin el título}"""
    partes = re.split(r"^## (.*)$", t, flags=re.M)
    return {partes[i].strip(): partes[i + 1].strip("\n") for i in range(1, len(partes), 2)}


def buscar(secs, prefijo):
    for k, v in secs.items():
        if k.lower().startswith(prefijo):
            return k, v
    return None, ""


def bajar(texto):
    """Baja un nivel los títulos para que quepan dentro de «### Lote X»."""
    return re.sub(r"^(#{2,5}) ", r"#\1 ", texto, flags=re.M)


def poner(archivo, bloque, despues_de=None):
    t = open(archivo, encoding="utf-8").read()
    nuevo = f"{INI}\n{bloque.rstrip()}\n{FIN}"
    if INI in t and FIN in t:
        t = t[:t.index(INI)] + nuevo + t[t.index(FIN) + len(FIN):]
    elif despues_de and re.search(despues_de, t, re.M):
        m = re.search(despues_de, t, re.M)
        t = t[:m.start()] + nuevo + "\n\n" + t[m.start():]
    else:
        t = t.rstrip("\n") + "\n\n" + nuevo + "\n"
    open(archivo, "w", encoding="utf-8").write(t)


lotes = sorted(f[:-3] for f in os.listdir("lotes") if f.endswith(".md"))
hora = datetime.datetime.now(datetime.timezone.utc).strftime("%d-%m-%Y, %H:%M UTC")

ids = sorted(i for i in os.listdir("biblias") if os.path.exists(f"biblias/{i}/biblia.md"))
completas = [i for i in ids if not revisar(i, solo_falta=True)]
series = [i for i in completas if i[:2].isdigit()]

estado = [f"## Cómo va por lotes ({hora})", "",
          f"Lo copia la central de `lotes/*.md` con `herramientas/juntar.sh --marcar`. "
          f"`revisar.py` da por **COMPLETAS {len(completas)}** biblias: "
          + ", ".join(i.split("-")[0] for i in series) + ".", ""]
avisos = [f"## 6. Avisos de los lotes ({hora})", "",
          "Copiados tal cual de `lotes/*.md` por la central (`juntar.sh --marcar`). "
          "Cuando el dueño decida algo, que lo anote arriba, en su apartado.", ""]
costos = [f"## Costos de los lotes ({hora})", "",
          "Copiados tal cual de `lotes/*.md` por la central (`juntar.sh --marcar`).", ""]

for l in lotes:
    t = open(f"lotes/{l}.md", encoding="utf-8").read()
    titulo = t.split("\n", 1)[0].lstrip("# ").strip()
    secs = secciones(t)
    k, v = buscar(secs, "estado")
    estado += [f"### {titulo}", ""] + ([f"*{k}*", "", bajar(v), ""] if v else ["(sin estado)", ""])
    _, v = buscar(secs, "avisos")
    if v.strip() and not v.strip().startswith("(ninguno"):
        avisos += [f"### {titulo}", "", bajar(v), ""]
    _, v = buscar(secs, "costos")
    filas = [f for f in v.split("\n") if f.startswith("|")]
    if len(filas) > 2:
        costos += [f"### {titulo}", ""] + filas + [""]

poner("ESTADO.md", "\n".join(estado), r"^## Cuándo una biblia está completa")
poner("DECISIONES.md", "\n".join(avisos))
poner("COSTOS.md", "\n".join(costos), r"^## Estimación en dólares")

e = open("ESTADO.md", encoding="utf-8").read()
e = re.sub(r"^Actualizado: [^.]*\.", f"Actualizado: {hora}.", e, count=1, flags=re.M)
open("ESTADO.md", "w", encoding="utf-8").write(e)
print(f"lotes copiados: {', '.join(lotes)} · completas: {len(completas)}")
