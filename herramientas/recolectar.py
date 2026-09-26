"""Recolector: junta de golpe, SIN gastar IA, los datos de una serie.

Antes, cada investigador gastaba cientos de pasos (y de dinero) haciendo a mano
las mismas consultas. Este programa las hace todas en unos minutos y deja un
resumen por rol, para que los investigadores empiecen con los datos delante y
sólo tengan que mirar, comprobar, elegir y buscar lo que falta.

    python3 herramientas/recolectar.py 01-one-piece
    python3 herramientas/recolectar.py 100-la-princesa-mononoke --nombres "Princess Mononoke" "Mononoke Hime"
    python3 herramientas/recolectar.py 34-haikyuu --hojas          # también hojas de contacto de la wiki

Lee encargos/<id>.md (serie, wiki, personajes, objeto) y consulta:
  AniList (popularidad por personaje, descripciones, seiyū, staff, etiquetas,
  obras parecidas, tráiler, enlaces oficiales) · Doblaje Wiki (reparto latino
  con temporadas, estudio, director, «datos de interés» y MUESTRAS DE AUDIO del
  doblaje) · Fandom (imágenes grandes con tamaño; apariencia y personalidad) ·
  Danbooru (personajes más dibujados por los fans y sus rasgos en etiquetas) ·
  Safebooru (fan art mejor valorado, con tamaño y autor) · Wallhaven (fondos de
  pantalla con resolución y autor) · Sketchfab (3D con licencia) · Openverse
  (fotos con licencia libre) · AnimeThemes (openings y endings con vídeo
  descargable) · Dailymotion e Internet Archive (clips, doblaje, fandubs) ·
  MusicBrainz (bandas sonoras) · Steam (juegos con capturas 1920×1080).

Deja en biblias/<id>/partes/:
  datos-imagen.md · datos-video.md · datos-voz.md · datos-texto.md  (resumen por rol)
  datos.json  (referencias candidatas con url, fuente, ancho, alto, licencia)
y lo crudo en herramientas/referencias/<id>/recoleccion/ (git lo ignora).
Todo sale con su fuente. Es un punto de partida: lo que se cite en la biblia se
comprueba (✅ con dos fuentes). Si una fuente falla, lo dice y sigue.
"""
import argparse
import difflib
import html
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = Path(__file__).resolve().parent.parent
UA = "sintonizando-investigacion/1.0 (+https://github.com/9YinSk/sintonizando-investigacion)"
UA_WEB = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
# etiquetas que no queremos ni ver en un proyecto para todo público
NO_SFW = re.compile(r"breast|nude|nipple|sex|pussy|penis|cum\b|panties|underwear|\bass\b|butt|cleavage|lingerie"
                    r"|bikini|topless|bottomless|groin|crotch|thigh|navel|erect|bdsm|bondage|blood|gore|guro", re.I)

# ── utilidades ────────────────────────────────────────────────────────────────


def pedir(url, datos=None, web=False, crudo=False, intentos=3, cabeceras=None):
    cab = {"User-Agent": UA_WEB if web else UA, "Accept": "application/json"}
    if "nocookie.net" in url:
        cab["Referer"] = "https://www.fandom.com/"
    if datos is not None:
        cab["Content-Type"] = "application/json"
        datos = json.dumps(datos).encode()
    cab.update(cabeceras or {})
    for k in range(intentos):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, data=datos, headers=cab), timeout=45).read()
            return r if crudo else json.loads(r)
        except Exception as e:                                          # noqa: BLE001
            if k == intentos - 1:
                raise
            time.sleep(3 * (k + 1) if "429" not in str(e) else 20)


def q(t):
    return urllib.parse.quote(t)


def limpio(t, n=0):
    """Quita marcado de wiki/HTML y deja texto corto en una línea."""
    t = re.sub(r"\[\[(?:Archivo|File|Imagen|Image):[^\]]*\]\]", "", t or "")
    t = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", t)
    t = re.sub(r"\[https?://\S+ ([^\]]*)\]", r"\1", t)
    t = re.sub(r"\{\{[^{}]*\}\}", "", t)
    t = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", t, flags=re.S)
    t = re.sub(r"~!.*?!~", "[spoiler]", t, flags=re.S)
    t = re.sub(r"<br\s*/?>", " · ", t)
    t = re.sub(r"<[^>]+>|'''?|__", "", t)
    t = html.unescape(re.sub(r"\s+", " ", t)).strip(" ·")
    return (t[:n].rsplit(" ", 1)[0] + "…") if n and len(t) > n else t


def parecido(a, b):
    n = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
    return difflib.SequenceMatcher(None, n(a), n(b)).ratio()


# Obras de los canales (01-36) que no son anime; las demás salen del grupo de catalogo.py
NO_ANIME = {"04": "pelicula", "08": "pelicula", "09": "occidental", "13": "occidental", "14": "occidental",
            "15": "occidental", "17": "occidental", "21": "pelicula", "23": "pelicula", "26": "occidental"}


def tipo_de(id, serie):
    """anime, occidental, pelicula o juego (decide qué fuentes tienen sentido)."""
    if id.split("-")[0] in NO_ANIME:
        return NO_ANIME[id.split("-")[0]]
    try:
        sys.path.insert(0, str(RAIZ))
        from catalogo import SERIES
        for grupo, obras in SERIES.items():
            if any(parecido(o[0], serie) > 0.9 for o in obras):
                g = grupo.lower()
                return ("juego" if "videojuego" in g else "occidental" if "occidental" in g
                        else "pelicula" if "sagas" in g else "anime")
    except Exception:                                                   # noqa: BLE001
        pass
    return "anime"


def leer_encargo(id):
    t = (RAIZ / "encargos" / f"{id}.md").read_text(encoding="utf-8")
    campo = lambda k: (re.search(rf"\*\*{k}[^*]*:\*\*\s*(.+)", t) or [None, ""])[1].strip()
    wiki = re.search(r"Wiki de Fandom[^`]*`([^`]+)`", t)
    pers = re.split(r"[;¿]", campo("Personajes para empezar"))[0]
    return {"serie": campo("Serie") or re.sub(r"^# Encargo \d+ — ", "", t.splitlines()[0]).split(" (")[0],
            "wiki": wiki[1] if wiki else "",
            "personajes": [p.strip(" .") for p in re.split(r",| y ", pers) if p.strip(" .")],
            "objeto": campo("Objeto que propone el plan")}


class Salida:
    """Acumula, por fuente, líneas por rol, referencias candidatas y fallos.
    Cada fuente se guarda aparte (crudo/<fuente>.frag.json): repetir una sola
    fuente con --solo no borra lo que dieron las demás."""

    def __init__(self):
        self.frag = {}
        self.actual = ""

    def empezar(self, fuente):
        self.actual = fuente
        self.frag[fuente] = {"md": {r: [] for r in ("imagen", "video", "voz", "texto")}, "refs": [], "fallos": []}

    @property
    def fallos(self):
        return self.frag[self.actual]["fallos"]

    def sec(self, rol, titulo, fuente):
        self.frag[self.actual]["md"][rol] += ["", f"## {titulo}", f"_Fuente: {fuente}_", ""]

    def l(self, rol, linea):
        self.frag[self.actual]["md"][rol].append(linea)

    def ref(self, url, fuente, ancho, alto, que_es, para_que, licencia):
        refs = self.frag[self.actual]["refs"]
        if url and not any(r["url"] == url for r in refs):
            refs.append({"url": url, "fuente": fuente, "ancho": ancho, "alto": alto, "que_es": que_es,
                         "para_que": para_que, "licencia": licencia, "origen": "recolectar.py"})


def paso(nombre):
    """Decorador: cada fuente falla sola, sin tumbar las demás."""
    def envolver(f):
        def hacer(ctx, s):
            t0 = time.time()
            s.empezar(nombre)
            try:
                crudo = f(ctx, s)
                if crudo is not None:
                    (ctx["crudo"] / f"{nombre}.json").write_text(json.dumps(crudo, ensure_ascii=False, indent=1),
                                                                 encoding="utf-8")
                print(f"  ✓ {nombre} ({time.time() - t0:.0f} s)")
            except Exception as e:                                      # noqa: BLE001
                s.fallos.append(f"{nombre}: {str(e)[:160]}")
                print(f"  ✗ {nombre}: {str(e)[:160]}")
            (ctx["crudo"] / f"{nombre}.frag.json").write_text(json.dumps(s.frag[nombre], ensure_ascii=False),
                                                              encoding="utf-8")
        hacer.nombre = nombre
        return hacer
    return envolver


# ── AniList ───────────────────────────────────────────────────────────────────

AL_Q = """query($s:String,$t:MediaType){Page(perPage:6){media(search:$s,type:$t,sort:SEARCH_MATCH){
 id siteUrl format episodes chapters seasonYear status averageScore popularity favourites
 title{romaji english native} synonyms genres tags{name rank isGeneralSpoiler isMediaSpoiler category}
 description(asHtml:false) coverImage{extraLarge} bannerImage trailer{id site}
 studios(isMain:true){nodes{name}} externalLinks{site url language type}
 staff(perPage:30,sort:RELEVANCE){edges{role node{name{full native}}}}
 relations{edges{relationType node{type format title{romaji english}}}}
 recommendations(sort:RATING_DESC,perPage:15){nodes{rating mediaRecommendation{format averageScore title{romaji english}}}}
 characters(sort:FAVOURITES_DESC,perPage:25){edges{role
   node{id name{full native alternative} favourites gender age bloodType dateOfBirth{month day} description(asHtml:false) image{large} siteUrl}
   ja:voiceActors(language:JAPANESE){name{full}}}}}}}"""


@paso("anilist")
def anilist(ctx, s):
    if ctx["tipo"] != "anime":
        s.fallos.append(f"anilist: no aplica ({ctx['tipo']}; usa --tipo anime si lo es)")
        return None
    m = None
    for tipo in ("ANIME", "MANGA"):
        for nombre in ctx["nombres"]:
            try:
                d = pedir("https://graphql.anilist.co", {"query": AL_Q, "variables": {"s": nombre, "t": tipo}})
            except Exception:                                           # noqa: BLE001
                continue
            medias = (((d.get("data") or {}).get("Page") or {}).get("media")) or []
            # Varias obras pueden llamarse igual (un corto «Onigiri» tiene el sinónimo
            # «Demon Slayer»): entre las que cuadran, la más popular.
            buenos, peor = [], None
            for cand in medias:
                titulos = [cand["title"].get(k) or "" for k in ("romaji", "english", "native")] + (cand.get("synonyms") or [])
                sim = max((parecido(nombre, x) for x in titulos if x), default=0)
                prefijo = any(x and x.lower().startswith(nombre.lower()) for x in titulos[:2])
                if sim >= 0.85 or prefijo:
                    buenos.append((cand.get("popularity") or 0, sim, cand))
                elif peor is None or sim > peor[0]:
                    peor = (sim, cand)
            if buenos:
                m = max(buenos, key=lambda x: x[:2])[2]
                break
            if peor:
                cand = peor[1]
                s.fallos.append(f"anilist: descarté «{cand['title'].get('english') or cand['title']['romaji']}» "
                                f"({cand['format']}, parecido {peor[0]:.2f} con «{nombre}»); si es la obra, usa --nombres")
            time.sleep(1)
        if m:
            break
    if not m:
        s.fallos.append("anilist: no encontré la obra (¿no es anime/manga? usa --nombres con el título en inglés)")
        return None
    s.frag[s.actual]["fallos"] = []  # hubo un descarte antes del acierto: no es un fallo
    ctx["anilist"] = m
    # AniList junta los alias con el mismo campo: las voces en español van en otra consulta
    es = pedir("https://graphql.anilist.co", {"query": "query($i:Int){Media(id:$i){characters(sort:FAVOURITES_DESC,perPage:25)"
                                                       "{edges{node{id} voiceActors(language:SPANISH){name{full}}}}}}",
                                              "variables": {"i": m["id"]}})
    voces = {e["node"]["id"]: e["voiceActors"] for e in es["data"]["Media"]["characters"]["edges"]}
    for e in m["characters"]["edges"]:
        e["es"] = voces.get(e["node"]["id"], [])
    t = m["title"]
    s.sec("voz", "Personajes más queridos (AniList, favoritos de usuarios)", m["siteUrl"])
    s.l("voz", "| # | Personaje | Favoritos | Rol | Seiyū | Voz «Spanish» en AniList ⚠️ |")
    s.l("voz", "|---|---|---|---|---|---|")
    for i, e in enumerate(m["characters"]["edges"], 1):
        n = e["node"]
        s.l("voz", f"| {i} | {n['name']['full']} ({n['name']['native'] or ''}) | {n['favourites']} | {e['role']} | "
                   f"{', '.join(v['name']['full'] for v in e['ja']) or '—'} | {', '.join(v['name']['full'] for v in e['es']) or '—'} |")
    s.l("voz", "")
    s.l("voz", "_«Spanish» en AniList mezcla España y Latinoamérica: el reparto latino, en Doblaje Wiki (abajo)._")
    s.sec("voz", "Fichas de personaje (AniList): edad, cumpleaños, gustos y carácter", m["siteUrl"])
    for e in m["characters"]["edges"][:15]:
        n = e["node"]
        cumple = n["dateOfBirth"] or {}
        datos = [f"género {n['gender']}" if n["gender"] else "", f"edad {n['age']}" if n["age"] else "",
                 f"cumple {cumple.get('day')}/{cumple.get('month')}" if cumple.get("month") else "",
                 f"sangre {n['bloodType']}" if n["bloodType"] else ""]
        s.l("voz", f"- **{n['name']['full']}** ({', '.join(x for x in datos if x) or 'sin datos'}) · {n['siteUrl']}")
        if n["description"]:
            s.l("voz", f"  {limpio(n['description'], 700)}")
        if n["image"]["large"]:
            s.ref(n["image"]["large"], "AniList", None, None, f"Retrato de {n['name']['full']}",
                  "cara y colores base del personaje", "© titulares; sólo referencia")
    s.sec("texto", "La obra en datos (AniList)", m["siteUrl"])
    s.l("texto", f"- Títulos: {t['romaji']} · {t.get('english') or '—'} · {t['native']} · también: {', '.join(m['synonyms'][:6])}")
    s.l("texto", f"- Formato {m['format']}, año {m['seasonYear']}, episodios {m['episodes']}, capítulos {m['chapters']}, "
                 f"estado {m['status']}, nota media {m['averageScore']}, popularidad {m['popularity']}, favoritos {m['favourites']}")
    s.l("texto", f"- Estudio: {', '.join(x['name'] for x in m['studios']['nodes']) or '—'} · géneros: {', '.join(m['genres'])}")
    s.l("texto", f"- Sinopsis: {limpio(m['description'], 600)}")
    s.l("texto", "- Temas y rasgos (etiquetas, % de acuerdo): " + ", ".join(
        f"{x['name']} {x['rank']}%" for x in m["tags"] if not x["isGeneralSpoiler"] and not x["isMediaSpoiler"])[:1200])
    s.sec("texto", "Equipo creativo (para «estilo y cómo replicarlo»)", m["siteUrl"] + "/staff")
    for e in m["staff"]["edges"]:
        s.l("texto", f"- {e['role']}: {e['node']['name']['full']} ({e['node']['name']['native'] or ''})")
    s.sec("texto", "Obras parecidas (recomendaciones de usuarios de AniList)", m["siteUrl"])
    for n in m["recommendations"]["nodes"]:
        r = n["mediaRecommendation"]
        if r:
            s.l("texto", f"- {r['title'].get('english') or r['title']['romaji']} ({r['format']}, nota {r['averageScore']}) · votos {n['rating']}")
    s.sec("texto", "Obras relacionadas (películas, juegos, spin-offs)", m["siteUrl"])
    for e in m["relations"]["edges"]:
        n = e["node"]
        s.l("texto", f"- {e['relationType']}: {n['title'].get('english') or n['title']['romaji']} ({n['type']} {n['format']})")
    s.sec("video", "Tráiler y enlaces oficiales (AniList)", m["siteUrl"])
    tr = m.get("trailer") or {}
    if tr.get("site") == "youtube":
        s.l("video", f"- Tráiler: https://www.youtube.com/watch?v={tr['id']}")
    elif tr:
        s.l("video", f"- Tráiler: {tr.get('site')} {tr.get('id')}")
    for x in m["externalLinks"]:
        s.l("video", f"- {x['type']} · {x['site']}{' (' + x['language'] + ')' if x.get('language') else ''}: {x['url']}")
    s.sec("imagen", "Portada y banner oficiales (AniList)", m["siteUrl"])
    for u, que in ((m["coverImage"]["extraLarge"], "Portada oficial"), (m["bannerImage"], "Banner oficial")):
        if u:
            s.l("imagen", f"- {que}: {u}")
            s.ref(u, "AniList", None, None, que, "arte oficial / key visual", "© titulares; sólo referencia")
    return m


# ── Doblaje Wiki ──────────────────────────────────────────────────────────────

def celdas_wiki(linea):
    """Parte una línea de tabla de wiki en (atributos, contenido, es_cabecera)."""
    cab = linea.startswith("!")
    trozos = re.split(r"!!" if cab else r"\|\|", linea[1:])
    out = []
    for t in trozos:
        prof, corte = 0, -1
        for i, c in enumerate(t):
            if t[i:i + 2] in ("[[", "{{"):
                prof += 1
            elif t[i:i + 2] in ("]]", "}}"):
                prof -= 1
            elif c == "|" and prof == 0:
                corte = i
                break
        attr, cont = (t[:corte], t[corte + 1:]) if corte >= 0 and "=" in t[:corte] and "[[" not in t[:corte] else ("", t)
        out.append((attr, cont.strip(), cab))
    return out


def tabla_wiki(txt):
    filas, fila = [], None
    for linea in txt.split("\n"):
        l = linea.strip()
        if l.startswith("|-") or l.startswith("{|") or l.startswith("|}"):
            if fila:
                filas.append(fila)
            fila = [] if not l.startswith("|}") else None
            if l.startswith("|}"):
                filas.append("FIN")
            continue
        if fila is not None and l[:1] in ("|", "!") and not l.startswith("|+"):
            fila += celdas_wiki(l)
    rejilla, pend = [], {}
    for fila in filas:
        if fila == "FIN":
            pend = {}
            rejilla.append("FIN")
            continue
        fila_out, c, i = [], 0, 0
        while i < len(fila) or pend.get(c, (0,))[0] > 0:
            if pend.get(c, (0,))[0] > 0:
                n, v = pend[c]
                fila_out.append(v)
                pend[c] = (n - 1, v)
                c += 1
                continue
            attr, v, cab = fila[i]
            i += 1
            rs = int((re.search(r'rowspan="?(\d+)', attr) or [0, 1])[1])
            cs = int((re.search(r'colspan="?(\d+)', attr) or [0, 1])[1])
            for _ in range(cs):
                fila_out.append(("H:" if cab else "") + v)
                if rs > 1:
                    pend[c] = (rs - 1, v)
                c += 1
        rejilla.append(fila_out)
    return rejilla


@paso("doblaje_wiki")
def doblaje(ctx, s):
    api = "https://doblaje.fandom.com/es/api.php"
    # La MEJOR página entre todos los nombres, no la primera que se parezca un poco
    # («El Castillo Ambulante» daba «El castillo maldito»; «Mononoke» la serie de 2007).
    norm = lambda x: re.sub(r"[^a-z0-9]", "", x.lower())
    mejor = (0.0, None)
    for nombre in ctx["nombres"]:
        r = pedir(f"{api}?action=query&list=search&format=json&srlimit=5&srsearch={q(nombre)}", web=True)
        for x in r["query"]["search"]:
            sim = parecido(nombre, x["title"])
            a, b = norm(nombre), norm(x["title"])
            if len(a) >= 6 and (a in b or b in a):
                sim = max(sim, 0.9)
            if sim > mejor[0]:
                mejor = (sim, x["title"])
    titulo = mejor[1] if mejor[0] >= 0.8 else None
    if mejor[1] and not titulo:
        s.fallos.append(f"doblaje_wiki: descarté «{mejor[1]}» (parecido {mejor[0]:.2f}); si es la obra, usa --nombres con el título latino exacto")
    if not titulo:
        s.fallos.append("doblaje_wiki: no encontré la página de la obra (prueba --nombres con el título latino)")
        return None
    wt = pedir(f"{api}?action=parse&format=json&prop=wikitext&page={q(titulo)}", web=True)["parse"]["wikitext"]["*"]
    url = f"https://doblaje.fandom.com/es/wiki/{q(titulo.replace(' ', '_'))}"
    s.sec("voz", f"Doblaje latino: ficha de «{titulo}» (Doblaje Wiki)", url)
    caja = re.search(r"\{\{[^\n]*\n((?:\s*\|.*\n)+)", wt)
    if caja:
        for campo in re.findall(r"^\s*\|\s*([^=\n]+?)\s*=\s*(.+)$", caja[1], re.M):
            if campo[1].strip() and not campo[0].lower().startswith(("imagen", "image", "tamaño")):
                s.l("voz", f"- {campo[0]}: {limpio(campo[1], 200)}")
    reparto = wt[wt.find("Reparto"):] if "Reparto" in wt else wt
    grupo, filas, audios, visto = "", [], set(), set()
    cols = None
    for fila in tabla_wiki(reparto.split("\n==", 1)[0] if "\n== " in reparto else reparto):
        if fila == "FIN":
            cols = None
            continue
        textos = [limpio(v.removeprefix("H:")) for v in fila]
        if any("Personaje" in t for t in textos) and all(v.startswith("H:") for v in fila if v):
            cols = {k: j for j, t in enumerate(textos) for k in ("Personaje", "Seiyū", "Actor de doblaje", "Temp", "Ep", "Audio", "Actor original", "Doblaje")
                    if t.startswith(k)}
            continue
        if fila and all(v.startswith("H:") for v in fila):
            grupo = textos[0]
            continue
        if not cols or "Personaje" not in cols:
            continue
        g = lambda k: textos[cols[k]] if k in cols and cols[k] < len(textos) else ""
        actor = g("Actor de doblaje") or g("Doblaje")
        audio = re.findall(r"<sm2>(.*?)</sm2>", " ".join(fila))
        clave = (g("Personaje"), actor, g("Temp"))
        if not g("Personaje") or clave in visto:
            continue
        visto.add(clave)
        audios.update(audio)
        filas.append(f"| {grupo} | {g('Personaje')} | {g('Seiyū') or g('Actor original')} | {actor} | {g('Temp')} | {g('Ep')} | {', '.join(audio)} |")
    s.sec("voz", "Reparto latino por personaje (Doblaje Wiki; confirmar cada nombre con otra fuente)", url)
    s.l("voz", "| Grupo | Personaje | Voz original | Voz latina | Temp. | Eps. | Muestra de audio |")
    s.l("voz", "|---|---|---|---|---|---|---|")
    for f in filas[:120]:
        s.l("voz", f)
    if len(filas) > 120:
        s.l("voz", f"| … | {len(filas) - 120} filas más en el crudo | | | | | |")
    urls = {}
    lista = sorted(audios)
    for i in range(0, len(lista), 40):
        r = pedir(f"{api}?action=query&format=json&prop=imageinfo&iiprop=url&titles="
                  + q("|".join("Archivo:" + a for a in lista[i:i + 40])), web=True)
        for p in r["query"]["pages"].values():
            if p.get("imageinfo"):
                urls[p["title"].split(":", 1)[1]] = p["imageinfo"][0]["url"]
    if urls:
        s.sec("voz", "Muestras de audio del doblaje latino (para herramientas/voz.py: frase textual y cómo suena)", url)
        for a, u in urls.items():
            s.l("voz", f"- {a}: {u}")
    for sec in ("Datos de interés", "Curiosidades", "Trivia"):
        m = re.search(rf"==\s*{sec}\s*==(.*?)(?:\n==[^=]|\Z)", wt, re.S)
        if m:
            s.sec("voz", f"«{sec}» del doblaje (Doblaje Wiki: frases, cambios, adaptación)", url + "#" + q(sec))
            for linea in m[1].split("\n"):
                if linea.strip().startswith("*") and limpio(linea.strip("*: ")):
                    s.l("voz", f"- {limpio(linea.strip('*: '), 400)}")
            break
    return {"titulo": titulo, "filas": filas, "audios": urls, "wikitext": wt[:200000]}


# ── Fandom ────────────────────────────────────────────────────────────────────

def pagina_personaje(api, nombre):
    """La página del personaje, no una subpágina ni una novela: redirección exacta y, si no, búsqueda por título."""
    p = next(iter(pedir(f"{api}?action=query&format=json&redirects=1&titles={q(nombre)}", web=True)["query"]["pages"].values()))
    if "missing" not in p:
        return p["title"]
    cand = pedir(f"{api}?action=opensearch&format=json&limit=15&namespace=0&search={q(nombre)}", web=True)[1]
    cand += [x["title"] for x in pedir(f"{api}?action=query&list=search&format=json&srlimit=15&srnamespace=0"
                                       f"&srsearch={q(nombre)}", web=True)["query"]["search"]]
    buenos = [c for c in cand if "/" not in c and "'s" not in c and re.search(rf"\b{re.escape(nombre)}\b", c, re.I)]
    return min(buenos, key=len) if buenos else None


@paso("fandom")
def fandom(ctx, s):
    wiki = ctx["wiki"]
    if not wiki:
        s.fallos.append("fandom: el encargo no trae wiki (usa --wiki)")
        return None
    api = f"https://{wiki}.fandom.com/api.php"
    crudo = {}
    for nombre in ctx["personajes"]:
        titulo = pagina_personaje(api, nombre)
        if not titulo:
            s.fallos.append(f"fandom: no encontré la página de «{nombre}»")
            continue
        purl = f"https://{wiki}.fandom.com/wiki/{q(titulo.replace(' ', '_'))}"
        imgs = []
        for pag in (titulo, f"{titulo}/Gallery", f"{titulo}/Galería"):
            try:
                p = next(iter(pedir(f"{api}?action=query&format=json&redirects=1&prop=images&imlimit=500&titles={q(pag)}",
                                    web=True)["query"]["pages"].values()))
                imgs += [i["title"] for i in p.get("images", []) if i["title"] not in imgs]
            except Exception:                                           # noqa: BLE001
                pass
        tam = []
        for i in range(0, len(imgs), 50):
            r = pedir(f"{api}?action=query&format=json&prop=imageinfo&iiprop=url|size&titles={q('|'.join(imgs[i:i + 50]))}", web=True)
            for p in r["query"]["pages"].values():
                ii = (p.get("imageinfo") or [{}])[0]
                if ii.get("width") and re.search(r"\.(png|jpe?g|webp)$", p["title"], re.I):
                    tam.append((ii["width"] * ii["height"], ii["width"], ii["height"], p["title"], ii["url"]))
        tam.sort(reverse=True)
        s.sec("imagen", f"{titulo}: las imágenes más grandes de la wiki ({len(tam)} en total)", purl)
        for _, w, h, t, u in tam[:10]:
            s.l("imagen", f"- {w}×{h} · {t.split(':', 1)[1]} · {u.split('/revision')[0]}")
            s.ref(u.split("/revision")[0], f"Fandom {wiki}", w, h, f"{titulo}: {t.split(':', 1)[1]}",
                  "pose, ropa y colores del personaje", "© titulares; sólo referencia")
        textos = {}
        try:
            secs = pedir(f"{api}?action=parse&format=json&prop=sections&page={q(titulo)}", web=True)["parse"]["sections"]
            for sec in secs:
                if re.match(r"(Appearance|Apariencia|Aspecto|Personality|Personalidad|Abilities|Habilidades)$", sec["line"], re.I):
                    wt = pedir(f"{api}?action=parse&format=json&prop=wikitext&page={q(titulo)}&section={sec['index']}",
                               web=True)["parse"]["wikitext"]["*"]
                    textos[sec["line"]] = limpio(wt.split("\n", 1)[-1], 900)
        except Exception:                                               # noqa: BLE001
            pass
        for k, v in textos.items():
            rol = "imagen" if re.match(r"Appear|Aparien|Aspecto", k) else "voz"
            s.sec(rol, f"{titulo} · {k} (texto de la wiki)", f"{purl}#{k}")
            s.l(rol, v)
        crudo[titulo] = {"imagenes": tam, "textos": textos}
        time.sleep(0.5)
    if ctx.get("hojas") and ctx["personajes"]:
        orden = [sys.executable, str(RAIZ / "herramientas" / "investigar_serie.py"), "--serie", ctx["serie"],
                 "--wiki", wiki, "--paginas", *list(crudo.keys())]
        r = subprocess.run(orden, capture_output=True, text=True, timeout=1800)
        s.sec("imagen", "Hojas de contacto (investigar_serie.py)", "herramientas/referencias/")
        s.l("imagen", "```\n" + (r.stdout[-1500:] or r.stderr[-800:]) + "\n```")
    return crudo


# ── Danbooru + Safebooru (lo que dibujan los fans) ────────────────────────────

@paso("fans_booru")
def booru(ctx, s):
    db = "https://danbooru.donmai.us"
    cop = None
    for nombre in ctx["nombres"]:
        base = re.sub(r"[^a-z0-9]+", "_", nombre.lower()).strip("_")
        r = pedir(f"{db}/tags.json?search[category]=3&search[order]=count&limit=5&search[name_or_alias_matches]={q(base + '*')}")
        if r:
            cop = r[0]
            break
    if not cop:
        s.fallos.append("fans_booru: la obra no tiene etiqueta en Danbooru (poco fan art o nombre distinto)")
        return None
    rel = pedir(f"{db}/related_tag.json?query={q(cop['name'])}&category=character&limit=40")
    pers = [t["tag"] for t in rel.get("related_tags", [])]
    crudo = {"obra": cop, "personajes": pers, "rasgos": {}, "fanart": {}}
    s.sec("voz", f"Los personajes más dibujados por los fans (Danbooru, {cop['post_count']} dibujos de «{cop['name']}»)",
          f"{db}/posts?tags={q(cop['name'])}")
    s.l("voz", "Medida de cariño del fandom distinta de las encuestas: cuántos dibujos de fans tiene cada uno.")
    for i, t in enumerate(sorted(pers, key=lambda x: -x["post_count"])[:20], 1):
        s.l("voz", f"{i}. {t['name']} · {t['post_count']} dibujos")
    elegidos = []
    for nombre in ctx["personajes"]:
        clave = re.sub(r"[^a-z0-9]+", "_", nombre.lower()).strip("_")
        cand = [t for t in pers if clave in t["name"]]
        if cand:
            elegidos.append(max(cand, key=lambda x: x["post_count"]))
    for t in sorted(pers, key=lambda x: -x["post_count"])[:6]:
        if t not in elegidos:
            elegidos.append(t)
    s.sec("imagen", "Rasgos que más se repiten al dibujar a cada personaje solo (Danbooru; vocabulario de las IA de imagen)",
          f"{db}/related_tag?query=<personaje>")
    for t in elegidos[:10]:
        r = pedir(f"{db}/related_tag.json?query={q(t['name'] + ' solo')}&category=general&limit=40")
        rasgos = [x["tag"]["name"] for x in r.get("related_tags", [])
                  if not NO_SFW.search(x["tag"]["name"]) and not re.match(r"\d(girl|boy)s?|multiple_|solo", x["tag"]["name"])]
        crudo["rasgos"][t["name"]] = rasgos
        s.l("imagen", f"- **{t['name']}**: {', '.join(rasgos[:28])}")
        time.sleep(0.4)
    sb = "https://safebooru.org/index.php?page=dapi&s=post&q=index&json=1&limit=40&tags="
    s.sec("imagen", "Fan art mejor valorado por personaje (Safebooru; enlace, tamaño y autor/origen)", "https://safebooru.org")
    for t in elegidos[:8]:
        try:
            r = pedir(sb + q(f"{t['name']} sort:score:desc -rating:questionable -rating:explicit")) or []
        except Exception:                                               # noqa: BLE001
            r = []
        r = [x for x in r if not NO_SFW.search(x.get("tags", ""))][:6]
        crudo["fanart"][t["name"]] = r
        if r:
            s.l("imagen", f"**{t['name']}**")
        for x in r:
            img = f"https://safebooru.org/images/{x['directory']}/{x['image']}"
            origen = x.get("source") or "sin origen"
            s.l("imagen", f"- {x['width']}×{x['height']} · puntos {x['score']} · {img} · autor/origen: {origen}")
            s.ref(img, "Safebooru (fan art)", x["width"], x["height"], f"Fan art de {t['name']} ({origen})",
                  "referencia de pose y estilo de fans; nunca para pegar", "© su autor; sólo referencia")
        time.sleep(0.4)
    return crudo


# ── Wallhaven, Sketchfab, Openverse ───────────────────────────────────────────

@paso("wallhaven")
def wallhaven(ctx, s):
    r = pedir(f"https://wallhaven.cc/api/v1/search?q={q(ctx['nombres'][0])}&purity=100&sorting=favorites&order=desc&atleast=1920x1080")
    datos = r.get("data", [])[:15]
    s.sec("imagen", "Fondos de pantalla más guardados (Wallhaven, sólo aptos, 1920×1080 o más)", "https://wallhaven.cc")
    for x in datos:
        try:
            det = pedir(f"https://wallhaven.cc/api/v1/w/{x['id']}")["data"]
            autor = (det.get("uploader") or {}).get("username", "?")
            etiquetas = ", ".join(t["name"] for t in det.get("tags", [])[:6])
        except Exception:                                               # noqa: BLE001
            autor, etiquetas = "?", ""
        s.l("imagen", f"- {x['resolution']} · ♥ {x['favorites']} · {x['path']} · subido por {autor} · origen: "
                      f"{x.get('source') or '—'} · {etiquetas}")
        s.ref(x["path"], "Wallhaven", x["dimension_x"], x["dimension_y"], f"Fondo de pantalla ({etiquetas})",
              "fondo o paleta de sitio", f"subido por {autor}; © su autor")
        time.sleep(1.4)
    return datos


@paso("sketchfab")
def sketchfab(ctx, s):
    crudo = {}
    consultas = [ctx["nombres"][0]] + [f"{ctx['nombres'][0]} {p}" for p in ctx["personajes"][:3]]
    if ctx["objeto"]:
        consultas.append(re.split(r"[,(;]", ctx["objeto"])[0])
    s.sec("imagen", "Modelos 3D descargables con licencia (Sketchfab)", "https://sketchfab.com")
    for c in consultas:
        r = pedir(f"https://api.sketchfab.com/v3/search?type=models&downloadable=true&count=8&sort_by=-likeCount&q={q(c)}")
        crudo[c] = r.get("results", [])
        if crudo[c]:
            s.l("imagen", f"**«{c}»**")
        for m in crudo[c][:6]:
            lic = (m.get("license") or {}).get("label", "?")
            s.l("imagen", f"- {m['name']} · {m['user']['displayName']} · {lic} · ♥ {m['likeCount']} · {m['viewerUrl']}")
            s.ref(m["viewerUrl"], "Sketchfab", None, None, f"Modelo 3D: {m['name']} de {m['user']['displayName']}",
                  "objeto o personaje 3D para Blender", lic)
    return crudo


@paso("openverse")
def openverse(ctx, s):
    r = pedir(f"https://api.openverse.org/v1/images/?q={q(ctx['nombres'][0])}&page_size=20&mature=false")
    s.sec("imagen", "Fotos con licencia libre (Openverse: cosplay, exposiciones, merchandising, murales)", "https://openverse.org")
    for x in r.get("results", []):
        lic = f"CC {x['license'].upper()} {x.get('license_version') or ''}".strip()
        s.l("imagen", f"- {x.get('width')}×{x.get('height')} · {limpio(x['title'], 80)} · {x.get('creator') or '?'} · {lic} · {x['url']}")
        s.ref(x["url"], f"Openverse ({x.get('source')})", x.get("width"), x.get("height"), limpio(x["title"], 80),
              "foto real (cosplay, objeto, evento)", f"{lic}, autor {x.get('creator') or '?'}")
    return r


# ── vídeo y música ────────────────────────────────────────────────────────────

@paso("animethemes")
def animethemes(ctx, s):
    if ctx["tipo"] != "anime":
        return None
    nombre = (ctx.get("anilist") or {}).get("title", {}).get("romaji") or ctx["nombres"][0]
    try:  # su CDN lleva semanas dando 522: un intento y, si no, se anota para que nadie lo reintente a mano
        r = pedir("https://api.animethemes.moe/anime?page[size]=3&include=animethemes.song.artists,"
                  f"animethemes.animethemeentries.videos&filter[name]={q(nombre)}", intentos=1)
    except Exception:                                                   # noqa: BLE001
        s.sec("video", "Openings y endings (AnimeThemes)", "https://animethemes.moe")
        s.l("video", "- AnimeThemes no responde hoy (522): no lo reintentes; OP/ED en Dailymotion, Internet Archive o la wiki")
        return None
    s.sec("video", "Openings y endings con su vídeo descargable (AnimeThemes; fotogramas.py acepta estas URL)", "https://animethemes.moe")
    for a in r.get("anime", [])[:1]:
        for th in a.get("animethemes", []):
            canc = th.get("song") or {}
            art = ", ".join(x["name"] for x in canc.get("artists", []))
            for en in th.get("animethemeentries", [])[:1]:
                vid = (en.get("videos") or [{}])[0]
                s.l("video", f"- {th['slug']} · «{canc.get('title')}» de {art or '?'} · eps {en.get('episodes') or '?'} · "
                             f"{vid.get('resolution', '?')}p · {vid.get('link', '—')}")
    return r


@paso("dailymotion")
def dailymotion(ctx, s):
    n, es = ctx["nombres"][0], ctx["serie"]
    grupos = {"video": [(n, "opening"), (n, "ending"), (n, "trailer"), (es, "escena")],
              "voz": [(es, "latino"), (es, "doblaje latino"), (es, "fandub español"), (es, "fandub latino")]}
    crudo = {}
    for rol, consultas in grupos.items():
        s.sec(rol, "Clips en Dailymotion (se bajan con yt-dlp aunque YouTube bloquee; mirar con fotogramas.py / oír con voz.py)",
              "https://api.dailymotion.com")
        for base, extra in consultas:
            c = f"{base} {extra}"
            r = pedir(f"https://api.dailymotion.com/videos?search={q(c)}&fields=id,title,duration,owner.screenname,views_total,url"
                      "&limit=40&sort=relevance")
            # sólo los que nombran la obra en el título, los más vistos primero
            palabras = [w for w in re.findall(r"\w+", base.lower()) if len(w) > 2] or [base.lower()]
            crudo[c] = sorted([v for v in r.get("list", []) if all(w in v["title"].lower() for w in palabras)],
                              key=lambda v: -(v.get("views_total") or 0))[:6]
            s.l(rol, f"**«{c}»**")
            for v in crudo[c]:
                s.l(rol, f"- {limpio(v['title'], 90)} · {v['duration'] // 60}:{v['duration'] % 60:02d} · "
                         f"{v.get('owner.screenname', '?')} · {v.get('views_total', '?')} vistas · {v['url']}")
    return crudo


@paso("internet_archive")
def archive(ctx, s):
    n = ctx["nombres"][0]
    r = pedir("https://archive.org/advancedsearch.php?q=" + q(f'title:("{n}") AND mediatype:(movies OR audio)')
              + "&fl[]=identifier&fl[]=title&fl[]=mediatype&fl[]=downloads&sort[]=downloads+desc&rows=20&output=json")
    s.sec("video", "Internet Archive (vídeo y audio subidos por usuarios; comprobar qué es)", "https://archive.org")
    for d in r["response"]["docs"]:
        s.l("video", f"- {limpio(str(d.get('title')), 90)} · {d.get('mediatype')} · {d.get('downloads')} descargas · "
                     f"https://archive.org/details/{d['identifier']}")
    return r


@paso("musicbrainz")
def musicbrainz(ctx, s):
    n = ctx["nombres"][0]
    r = pedir(f"https://musicbrainz.org/ws/2/release-group/?query={q(f'releasegroup:{n} AND secondarytype:soundtrack')}&fmt=json&limit=15")
    s.sec("video", "Bandas sonoras publicadas (MusicBrainz)", "https://musicbrainz.org")
    for g in r.get("release-groups", []):
        art = ", ".join(a["name"] for a in g.get("artist-credit", []))
        s.l("video", f"- {g['title']} · {art} · {g.get('first-release-date', '?')} · https://musicbrainz.org/release-group/{g['id']}")
    return r


# ── juegos ────────────────────────────────────────────────────────────────────

@paso("steam")
def steam(ctx, s):
    n = ctx["nombres"][0]
    r = pedir(f"https://store.steampowered.com/api/storesearch/?term={q(n)}&cc=mx&l=spanish", web=True)
    apps = [a for a in r.get("items", []) if parecido(n, a["name"][:len(n) + 4]) > 0.5 or n.lower() in a["name"].lower()][:6]
    crudo = []
    s.sec("texto", "Videojuegos en Steam: interfaz y cuadros de diálogo en capturas 1920×1080", "https://store.steampowered.com")
    for a in apps:
        d = pedir(f"https://store.steampowered.com/api/appdetails?appids={a['id']}&l=spanish", web=True) or {}
        d = d.get(str(a["id"])) or next(iter(d.values()), {}) if isinstance(d, dict) else {}
        if not d.get("success"):
            continue
        d = d["data"]
        crudo.append(d)
        caps = [x["path_full"].split("?")[0] for x in d.get("screenshots", [])]
        s.l("texto", f"- **{d['name']}** ({d.get('release_date', {}).get('date', '?')}, {', '.join(d.get('developers', []))}) · "
                     f"https://store.steampowered.com/app/{a['id']} · {len(caps)} capturas · idiomas: {limpio(d.get('supported_languages', ''), 160)}")
        for c in caps[:6]:
            s.l("texto", f"  - {c}")
            s.ref(c, "Steam", 1920, 1080, f"Captura de {d['name']}", "interfaz, menús y cuadro de diálogo del juego",
                  "© titulares; sólo referencia")
        time.sleep(0.6)
    return crudo


# ── Reddit (Arctic Shift) ─────────────────────────────────────────────────────

@paso("reddit")
def reddit(ctx, s):
    base = "https://arctic-shift.photon-reddit.com/api"
    n = ctx["nombres"][0]
    sub = None
    for c in {re.sub(r"[^A-Za-z0-9]", "", n), re.sub(r"[^A-Za-z0-9]", "", n.split(":")[0])}:
        try:
            r = pedir(f"{base}/subreddits/search?subreddit_prefix={q(c)}&limit=5", intentos=2)
            if r.get("data"):
                sub = max(r["data"], key=lambda x: x.get("subscribers") or 0)["display_name"]
                break
        except Exception:                                               # noqa: BLE001
            pass
    if not sub:
        s.fallos.append("reddit: no encontré el subreddit")
        return None
    crudo = {}
    s.sec("voz", f"Reddit r/{sub}: lo que ama y discute el fandom (títulos de hilos)", f"https://www.reddit.com/r/{sub}")
    for c in ("favorite character", "why I love", "best scene", "unpopular opinion", "iconic"):
        try:
            r = pedir(f"{base}/posts/search?subreddit={sub}&title={q(c)}&limit=25&sort=desc", intentos=2)
        except Exception:                                               # noqa: BLE001
            continue
        hilos = sorted(r.get("data") or [], key=lambda x: -(x.get("score") or 0))[:6]
        crudo[c] = hilos
        s.l("voz", f"**«{c}»**")
        for h in hilos:
            s.l("voz", f"- ({h.get('score')} votos, {h.get('num_comments')} comentarios) {limpio(h['title'], 120)} · "
                       f"https://www.reddit.com{h.get('permalink', '')}")
        time.sleep(1.5)
    return crudo


FUENTES = [anilist, doblaje, fandom, booru, wallhaven, sketchfab, openverse, animethemes, dailymotion, archive,
           musicbrainz, steam, reddit]
TITULOS = {"imagen": "Datos para el investigador de IMAGEN (puntos 1, 3, 15, 16, 19, 23)",
           "video": "Datos para el investigador de VÍDEO (puntos 2, 4, 9, 10, 14)",
           "voz": "Datos para el investigador de VOZ Y PERSONAJES (puntos 7, 8, 12, 13, 20, 21, 22)",
           "texto": "Datos para el investigador de TEXTO, JUEGOS Y TÉCNICA (puntos 5, 6, 11, 18, 24, 25)"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id")
    ap.add_argument("--nombres", nargs="*", default=[], help="títulos alternativos (inglés, romaji, latino)")
    ap.add_argument("--wiki", default="", help="subdominio de Fandom si el encargo no lo trae")
    ap.add_argument("--personajes", nargs="*", default=[])
    ap.add_argument("--solo", nargs="*", default=[], help="sólo estas fuentes (" + ", ".join(f.nombre for f in FUENTES) + ")")
    ap.add_argument("--hojas", action="store_true", help="también hojas de contacto con investigar_serie.py")
    ap.add_argument("--tipo", choices=["anime", "occidental", "pelicula", "juego"], help="si la detección falla")
    a = ap.parse_args()

    enc = leer_encargo(a.id)
    serie = enc["serie"]
    nombres = a.nombres + [serie] + [re.sub(r"^(La|El|Los|Las)\s+", "", serie), serie.split(":")[0].strip()]
    ctx = {"id": a.id, "serie": serie, "nombres": list(dict.fromkeys(x for x in nombres if x)),
           "wiki": a.wiki or enc["wiki"], "personajes": a.personajes or enc["personajes"], "objeto": enc["objeto"],
           "hojas": a.hojas, "tipo": a.tipo or tipo_de(a.id, serie), "crudo": RAIZ / "herramientas" / "referencias" / a.id / "recoleccion"}
    ctx["crudo"].mkdir(parents=True, exist_ok=True)
    print(f"Recolectando «{serie}» ({ctx['tipo']}) · nombres {ctx['nombres']} · wiki {ctx['wiki'] or '—'} · personajes {ctx['personajes']}")
    s = Salida()
    for f in FUENTES:
        if not a.solo or f.nombre in a.solo or f.nombre == "anilist":
            f(ctx, s)
        # AniList da el título internacional: las fuentes en inglés buscan con él
        al = ctx.get("anilist")
        if f.nombre == "anilist" and al:
            for t in (al["title"].get("english"), al["title"].get("romaji")):
                if t and t not in ctx["nombres"]:
                    ctx["nombres"].insert(0, t)

    # juntar los trozos de todas las fuentes (las de esta vez y las de antes)
    md = {r: [] for r in TITULOS}
    refs, fallos, vistas = [], [], set()
    for f in FUENTES:
        ruta = ctx["crudo"] / f"{f.nombre}.frag.json"
        if not ruta.exists():
            continue
        fr = json.loads(ruta.read_text(encoding="utf-8"))
        for rol in md:
            md[rol] += fr["md"][rol]
        fallos += fr["fallos"]
        for r in fr["refs"]:
            if r["url"] not in vistas:
                vistas.add(r["url"])
                refs.append(r)
    dest = RAIZ / "biblias" / a.id / "partes"
    dest.mkdir(parents=True, exist_ok=True)
    hoy = date.today().isoformat()
    for rol, lineas in md.items():
        cab = [f"# {TITULOS[rol]} · {serie}", "",
               f"Recolectado automáticamente con `herramientas/recolectar.py` el {hoy}, sin IA. Cada bloque dice su fuente.",
               "Es el punto de partida, no la verdad: lo que pase a la biblia se comprueba (✅ con dos fuentes) y se mira.",
               "No repitas estas consultas: sigue desde aquí y busca lo que falta."]
        if fallos:
            cab += ["", "**Fuentes que fallaron** (hazlas a mano si hacen falta): " + " · ".join(fallos)]
        (dest / f"datos-{rol}.md").write_text("\n".join(cab + lineas) + "\n", encoding="utf-8")
    (dest / "datos.json").write_text(json.dumps(refs, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"→ {dest}: " + ", ".join(f"datos-{r}.md ({len(l)} líneas)" for r, l in md.items())
          + f", datos.json ({len(refs)} referencias)")
    if fallos:
        print("Fallaron: " + " · ".join(fallos))


if __name__ == "__main__":
    main()
