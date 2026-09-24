"""Pequeña ayuda para las wikis de Fandom (y Wikipedia): listar imágenes de una
página y bajar un archivo a tamaño original. Ver sondear_wikis.py."""
import json, os, sys, urllib.request, urllib.parse
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"}
AQUI = os.path.dirname(os.path.abspath(__file__))

def pedir(u, crudo=False):
    cab = dict(UA)
    if "nocookie.net" in u:
        # El servidor de imágenes pide que se venga «desde» la wiki: sin Referer
        # da 403 aunque el user-agent sea de navegador.
        cab.update({"Referer": "https://www.fandom.com/", "Accept": "image/png,image/*;q=0.8"})
    r = urllib.request.urlopen(urllib.request.Request(u, headers=cab), timeout=40).read()
    return r if crudo else json.loads(r)

def imagenes(wiki, pagina, filtro=""):
    u = (f"https://{wiki}.fandom.com/api.php?action=query&format=json&redirects=1"
         f"&prop=images&imlimit=500&titles={urllib.parse.quote(pagina)}")
    p = next(iter(pedir(u)["query"]["pages"].values()))
    return [i["title"] for i in p.get("images", []) if filtro.lower() in i["title"].lower()]

def info(wiki, archivos):
    t = "|".join(archivos)
    u = (f"https://{wiki}.fandom.com/api.php?action=query&format=json&prop=imageinfo"
         f"&iiprop=url|size&titles={urllib.parse.quote(t)}")
    out = {}
    for p in pedir(u)["query"]["pages"].values():
        ii = (p.get("imageinfo") or [{}])[0]
        out[p["title"]] = (ii.get("width"), ii.get("height"), ii.get("url"))
    return out

def bajar(url, destino):
    datos = pedir(url, crudo=True)
    ruta = os.path.join(AQUI, "cuerpos", destino)
    open(ruta, "wb").write(datos)
    im = Image.open(ruta)
    alfa = 0
    if im.mode in ("RGBA", "LA", "P"):
        a = im.convert("RGBA").getchannel("A").histogram(); alfa = round(a[0] / sum(a), 2)
    return im.size, alfa

if __name__ == "__main__":
    wiki, pagina = sys.argv[1], sys.argv[2]
    filtro = sys.argv[3] if len(sys.argv) > 3 else ""
    lista = [x for x in imagenes(wiki, pagina, filtro) if x.lower().endswith((".png", ".webp"))]
    for i in range(0, len(lista), 40):
        for k, (w, h, u) in info(wiki, lista[i:i+40]).items():
            if w and w * h > 500_000:
                print(f"{w}x{h}  {k}")
