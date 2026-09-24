"""Investigar una serie ANTES de dibujar su lámina — y sin gastar límite de Claude.

Él lo pidió así (23-sep-2026): «estás tomando referencias muy cortas, sólo un par
de imágenes… no estás mirando vídeos ni descripciones, no te estás empapando».
Este script hace el trabajo pesado fuera de Claude:

1. **Todas las imágenes de la wiki** de la serie (la página del personaje, su
   galería, la de la serie y las que se le pasen), no seis: se listan con su
   tamaño y se montan en **hojas de contacto numeradas** (`referencias/<slug>/
   hoja_01.jpg`…) para mirarlas de un vistazo. `indice.json` guarda, por número,
   el archivo, su tamaño y la URL del original, para bajar luego el que se elija:
       python investigar_serie.py --bajar <slug> 17 42
2. (Sólo con `--con-gemini`) un **borrador** de biblia de **Gemini con búsqueda en Google** (gratis, con
   la GEMINI_API_KEY del entorno): lenguaje visual, paleta, objetos y sitios
   icónicos, cómo hablan y piensan los personajes en pantalla, frases del
   **doblaje latino** y quién lo dobla, poses típicas, qué ama el fandom, qué
   no hacer, y una propuesta para la lámina del canal. Se guarda en la bóveda:
   `YinX/00-Bandeja/Biblias de series/<Serie>.md`, con las fuentes que citó.

    python investigar_serie.py --serie "Bocchi the Rock!" --wiki bocchi-the-rock \
        --paginas "Hitori Gotoh" "Ikuyo Kita" "Kessoku Band" \
        --canal "#demos-canto: foro donde cada uno sube su ficha de canto y sus covers"

🔴 Él no quiere que Gemini haga nada sin supervisión (23-sep): por defecto el
script sólo reúne imágenes, y la biblia la escribe Claude. Lo que diga Gemini **se comprueba** antes de dibujarlo (nombres de actores de
voz, sobre todo): la biblia marca las fuentes para eso.
"""
import argparse
import io
import json
import math
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
AQUI = Path(__file__).resolve().parent
BOVEDA = AQUI.parents[2] / "YinX" / "00-Bandeja" / "Biblias de series"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"}
GEM = "https://generativelanguage.googleapis.com/v1beta/models"


def pedir(u, crudo=False, timeout=40):
    cab = dict(UA)
    if "nocookie.net" in u:  # sin Referer, el servidor de imágenes de Fandom da 403
        cab.update({"Referer": "https://www.fandom.com/"})
    r = urllib.request.urlopen(urllib.request.Request(u, headers=cab), timeout=timeout).read()
    return r if crudo else json.loads(r)


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


# ── 1 · las imágenes ─────────────────────────────────────────────────────────

def titulos_de_imagenes(wiki, paginas):
    """Todas las imágenes enlazadas desde esas páginas y sus galerías."""
    todas = []
    candidatas = []
    for p in paginas:
        candidatas += [p, f"{p}/Gallery", f"{p}/Image Gallery", f"{p}/Images"]
    for i in range(0, len(candidatas), 20):
        grupo = "|".join(candidatas[i:i + 20])
        cont = {}
        while True:
            u = (f"https://{wiki}.fandom.com/api.php?action=query&format=json&redirects=1"
                 f"&prop=images&imlimit=500&titles={urllib.parse.quote(grupo)}"
                 + "".join(f"&{k}={urllib.parse.quote(v)}" for k, v in cont.items()))
            d = pedir(u)
            for pg in d.get("query", {}).get("pages", {}).values():
                todas += [x["title"] for x in pg.get("images", [])]
            if "continue" not in d:
                break
            cont = d["continue"]
    vistas, orden = set(), []
    for t in todas:
        if t not in vistas and t.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            vistas.add(t)
            orden.append(t)
    return orden


def info_imagenes(wiki, titulos, ancho_miniatura=300):
    """Tamaño real, URL del original y una miniatura de cada imagen."""
    out = []
    for i in range(0, len(titulos), 40):
        t = "|".join(titulos[i:i + 40])
        u = (f"https://{wiki}.fandom.com/api.php?action=query&format=json&prop=imageinfo"
             f"&iiprop=url|size&iiurlwidth={ancho_miniatura}&titles={urllib.parse.quote(t)}")
        for pg in pedir(u)["query"]["pages"].values():
            ii = (pg.get("imageinfo") or [{}])[0]
            if ii.get("width"):
                out.append(dict(titulo=pg["title"], ancho=ii["width"], alto=ii["height"],
                                url=ii.get("url"), mini=ii.get("thumburl") or ii.get("url")))
    return out


def hojas_de_contacto(imgs, carpeta, por_hoja=48, columnas=8, celda=(300, 250)):
    carpeta.mkdir(parents=True, exist_ok=True)
    try:
        letra = ImageFont.truetype("arialbd.ttf", 18)
        chica = ImageFont.truetype("arial.ttf", 13)
    except OSError:
        letra = chica = ImageFont.load_default()
    rutas = []
    for h in range(math.ceil(len(imgs) / por_hoja)):
        tanda = imgs[h * por_hoja:(h + 1) * por_hoja]
        filas = math.ceil(len(tanda) / columnas)
        hoja = Image.new("RGB", (columnas * celda[0], filas * (celda[1] + 34)), (24, 24, 28))
        d = ImageDraw.Draw(hoja)
        for k, im in enumerate(tanda):
            n = h * por_hoja + k + 1
            x, y = (k % columnas) * celda[0], (k // columnas) * (celda[1] + 34)
            try:
                mini = Image.open(io.BytesIO(pedir(im["mini"], crudo=True))).convert("RGBA")
                mini.thumbnail((celda[0] - 10, celda[1] - 10))
                fondo = Image.new("RGBA", mini.size, (70, 110, 70, 255))  # verde: se ve si es recortable
                fondo.alpha_composite(mini)
                hoja.paste(fondo.convert("RGB"), (x + (celda[0] - mini.width) // 2, y + 5))
            except Exception:                                          # noqa: BLE001
                d.text((x + 10, y + 100), "(no bajó)", fill=(200, 80, 80), font=chica)
            d.rectangle((x + 4, y + 4, x + 44, y + 28), fill=(250, 210, 60))
            d.text((x + 8, y + 6), str(n), fill=(0, 0, 0), font=letra)
            nombre = im["titulo"].replace("File:", "")[:38]
            d.text((x + 6, y + celda[1] + 2), f"{im['ancho']}×{im['alto']}", fill=(150, 220, 150), font=chica)
            d.text((x + 6, y + celda[1] + 17), nombre, fill=(200, 200, 210), font=chica)
        r = carpeta / f"hoja_{h + 1:02d}.jpg"
        hoja.save(r, quality=86)
        rutas.append(r)
    return rutas


# ── 2 · la biblia con Gemini ─────────────────────────────────────────────────

PREGUNTA = """Eres documentalista de arte y de doblaje para un servidor de Discord
hispanohablante de doblaje, locución, canto, edición y arte (Perú, México,
Venezuela, Colombia, Ecuador). Vamos a dibujar la imagen de cabecera de un canal
con el mundo de la serie «{serie}». El canal: {canal}.

Investiga en Google y escribe en español, en Markdown, una BIBLIA de trabajo con
estas secciones (con detalle concreto, nada genérico):

## Lenguaje visual
Estudio y dirección de arte; tipo de línea, sombreado y luz; paleta con códigos
hex aproximados; texturas y efectos típicos (tramas, destellos, glitch…).
## Tipografía
El logo y los rótulos de la serie; qué letras gratuitas (Google Fonts u otras
libres) se le parecen, y para qué usar cada una.
## Cómo hablan y piensan en pantalla
Globos, cartelas, subtítulos, interfaces, pensamientos: la forma concreta en que
esta serie muestra lo que alguien dice o piensa. Esto es lo más importante.
## Sitios y objetos icónicos
Lugares, objetos, props, logotipos del mundo: con qué objeto de la serie se
podría escribir información (una pantalla, un cuaderno, un cartel…).
## Personajes: poses, gestos y frases
Para los personajes principales: poses y gestos típicos, con qué objeto suelen
salir (instrumento, arma…), manías y 3-5 frases icónicas. Da las frases COMO
SUENAN EN EL DOBLAJE LATINO si lo hay (y di quién dobla a cada uno en
Latinoamérica, con el estudio). Si no hay doblaje latino, dilo.
## Lo que el fandom ama
Memes, momentos, chistes internos, escenas que todos reconocen.
## Qué NO hacer
Lo que quedaría falso o genérico para un fan.
## Propuesta para la lámina
Tres ideas distintas para la lámina de ESTE canal usando todo lo anterior: el
objeto del mundo donde va la información, el personaje y qué hace, cómo habla.
"""


def gemini_con_google(texto, clave):
    """Una llamada con búsqueda en Google. Prueba el alias vivo y cae a otros si
    está saturado (503) — la trampa medida en traspaso.py y discord_ia.py."""
    # La cuota gratis es POR MODELO (medido el 23-sep-2026): con el alias
    # agotado (429) los demás siguen respondiendo. Y gemini-2.5-* ya da 404
    # («no longer available to new users»). Por eso la lista es larga.
    modelos = ["gemini-3-flash-preview", "gemini-3.5-flash", "gemini-3.8-flash",
               "gemini-3.7-flash", "gemini-3.6-flash", "gemini-flash-latest",
               "gemini-3.5-flash-lite", "gemini-flash-lite-latest"]
    cuerpo = json.dumps({
        "contents": [{"parts": [{"text": texto}]}],
        "tools": [{"google_search": {}}],
        "generationConfig": {"temperature": 0.4, "maxOutputTokens": 8192},
    }).encode("utf-8")
    import time
    for ronda in range(3):
        for m in modelos:
            try:
                req = urllib.request.Request(f"{GEM}/{m}:generateContent?key={clave}", data=cuerpo,
                                             headers={"Content-Type": "application/json"})
                d = json.loads(urllib.request.urlopen(req, timeout=180).read())
                c = d["candidates"][0]
                texto_out = "".join(p.get("text", "") for p in c["content"]["parts"])
                fuentes = []
                for ch in (c.get("groundingMetadata") or {}).get("groundingChunks", []):
                    w = ch.get("web") or {}
                    if w.get("uri"):
                        fuentes.append((w.get("title") or w["uri"], w["uri"]))
                return texto_out, fuentes, m
            except urllib.error.HTTPError as e:
                print(f"   {m}: HTTP {e.code}", file=sys.stderr)
            except Exception as e:                                     # noqa: BLE001
                print(f"   {m}: {type(e).__name__}", file=sys.stderr)
        time.sleep(8 * (ronda + 1))
    return None, [], None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--serie")
    ap.add_argument("--wiki", help="subdominio de Fandom, p. ej. bocchi-the-rock")
    ap.add_argument("--paginas", nargs="*", default=[])
    ap.add_argument("--canal", default="")
    ap.add_argument("--min-px", type=int, default=500_000, help="descarta imágenes más chicas (px totales)")
    ap.add_argument("--con-gemini", action="store_true",
                    help="también un borrador de biblia con Gemini (él no lo quiere sin revisión: 23-sep)")
    ap.add_argument("--solo-gemini", action="store_true",
                    help="no vuelve a bajar imágenes: usa el indice.json que ya hay y sólo pide la biblia")
    ap.add_argument("--bajar", nargs="+", metavar=("SLUG", "N"), help="bajar originales por número")
    a = ap.parse_args()

    if a.bajar:
        s, nums = a.bajar[0], [int(n) for n in a.bajar[1:]]
        idx = json.loads((AQUI / "referencias" / s / "indice.json").read_text(encoding="utf-8"))
        for n in nums:
            im = idx[n - 1]
            ext = Path(urllib.parse.urlparse(im["url"]).path).suffix or ".png"
            ruta = AQUI / "referencias" / s / f"{n:03d}{ext}"
            ruta.write_bytes(pedir(im["url"], crudo=True))
            print(f"{n}: {im['ancho']}×{im['alto']}  {ruta}")
        return

    s = slug(a.serie)
    carpeta = AQUI / "referencias" / s
    paginas = a.paginas or [a.serie]
    if a.solo_gemini:
        imgs = json.loads((carpeta / "indice.json").read_text(encoding="utf-8"))
        a.con_gemini = True
    else:
        print(f"· imágenes de {a.wiki}.fandom.com ({len(paginas)} páginas y sus galerías)…")
        titulos = titulos_de_imagenes(a.wiki, paginas)
        imgs = [i for i in info_imagenes(a.wiki, titulos) if i["ancho"] * i["alto"] >= a.min_px]
        imgs.sort(key=lambda i: -(i["ancho"] * i["alto"]))
        carpeta.mkdir(parents=True, exist_ok=True)
        (carpeta / "indice.json").write_text(json.dumps(imgs, ensure_ascii=False, indent=1), encoding="utf-8")
        hojas = hojas_de_contacto(imgs, carpeta)
        print(f"  {len(titulos)} imágenes enlazadas, {len(imgs)} grandes → {len(hojas)} hojas en {carpeta}")

    if not a.con_gemini:
        return
    clave = os.environ.get("GEMINI_API_KEY", "").strip()
    if not clave:
        print("  (sin GEMINI_API_KEY: no hay biblia)")
        return
    print("· biblia con Gemini + Google…")
    texto, fuentes, modelo = gemini_con_google(PREGUNTA.format(serie=a.serie, canal=a.canal or "(sin canal)"), clave)
    if not texto:
        print("  Gemini no contestó; las hojas de contacto sí están.")
        return
    BOVEDA.mkdir(parents=True, exist_ok=True)
    nota = BOVEDA / f"{a.serie.replace(':', ' -').replace('/', '-').replace('?', '').replace('!', '')}.md"
    rel = os.path.relpath(carpeta, AQUI.parents[2]).replace("\\", "/")
    cuerpo = [
        "---", f"tags: [biblia, serie, laminas]", f"serie: \"{a.serie}\"", f"wiki: {a.wiki}", "---", "",
        f"# Biblia · {a.serie}", "",
        "> [!info] Cómo se hizo",
        f"> Redactada por **{modelo}** con búsqueda en Google (no gasta límite de Claude), para la lámina de **{a.canal or '—'}**.",
        f"> Referencias visuales: **{len(imgs)} imágenes** de la wiki en `{rel}/hoja_*.jpg` (numeradas; `indice.json` tiene la URL de cada original).",
        "> ⚠️ Los nombres de actores de voz y las frases **se comprueban** antes de dibujarlos.", "",
        texto.strip(), "", "## Fuentes que citó", "",
    ] + [f"- [{t}]({u})" for t, u in fuentes[:40]]
    nota.write_text("\n".join(cuerpo) + "\n", encoding="utf-8")
    print(f"  biblia → {nota}")


if __name__ == "__main__":
    main()
