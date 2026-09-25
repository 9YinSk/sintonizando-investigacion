"""Abre una página con un navegador sin ventana (Playwright + Chromium) y
devuelve su texto: sirve para webs que bloquean a curl/requests (TV Tropes,
Reddit, algunas fichas). Las wikis de Fandom siguen bloqueadas: usa su API
(api.php). YouTube abre la página (título, descripción), no el vídeo.

    python3 herramientas/navegar.py <url>                 # texto de la página
    python3 herramientas/navegar.py <url> --html          # HTML entero
    python3 herramientas/navegar.py <url> --selector '#main-article' --espera 4000
    python3 herramientas/navegar.py <url> --captura /tmp/pagina.png

Requiere `pip install playwright` y `python3 -m playwright install chromium`
(en GitHub lo instala lote.yml). Si PLAYWRIGHT_CHROMIUM apunta a un ejecutable,
se usa ese.
"""
import argparse
import asyncio
import os
import sys

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"


async def navegar(url, selector, espera, html, captura):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        exe = os.environ.get("PLAYWRIGHT_CHROMIUM")
        b = await p.chromium.launch(headless=True, executable_path=exe) if exe else await p.chromium.launch(headless=True)
        ctx = await b.new_context(user_agent=UA, locale="es-MX", viewport={"width": 1366, "height": 900})
        pg = await ctx.new_page()
        r = await pg.goto(url, wait_until="domcontentloaded", timeout=45000)
        await pg.wait_for_timeout(espera)
        if captura:
            await pg.screenshot(path=captura, full_page=False)
        if html:
            out = await pg.content()
        elif selector:
            out = "\n\n".join(await pg.locator(selector).all_inner_texts())
        else:
            out = await pg.inner_text("body")
        estado = r.status if r else "?"
        await b.close()
        return estado, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--selector", help="CSS de la parte que interesa")
    ap.add_argument("--espera", type=int, default=2500, help="ms tras cargar (páginas que pintan con JS)")
    ap.add_argument("--html", action="store_true")
    ap.add_argument("--captura", help="guardar una captura PNG")
    ap.add_argument("--max", type=int, default=20000, help="caracteres como mucho (0 = todo)")
    a = ap.parse_args()
    try:
        estado, out = asyncio.run(navegar(a.url, a.selector, a.espera, a.html, a.captura))
    except ImportError:
        sys.exit("falta playwright: pip install playwright && python3 -m playwright install chromium")
    except Exception as e:  # noqa: BLE001
        sys.exit(f"no pude abrir {a.url}: {str(e)[:200]}")
    sys.stderr.write(f"[{estado}] {len(out)} caracteres\n")
    print(out[: a.max] if a.max else out)


if __name__ == "__main__":
    main()
