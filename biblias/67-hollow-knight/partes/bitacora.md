## Bitácora

### Bitácora de imagen

- Fandom API (`hollowknight.fandom.com/api.php`), en español e inglés no aplica (wiki sólo en inglés): páginas de Hornet, Quirrel, The_Knight, categorías `X_HK_Promo_Art` y `X_SS_Promo_Art` — sin bloqueos.
- `herramientas/investigar_serie.py --serie "Hollow Knight" --wiki hollowknight --paginas "The Knight" "Hornet" "Quirrel" "Hollow Knight"` → 180 imágenes, 3 hojas de contacto (miradas con Read, no sólo listadas).
- `herramientas/estilo.py` sobre 5 imágenes (3 artes oficiales de personaje + 3 fondos de zona) para hex medidos, no de memoria.
- `ambientcg.com/api/v2/full_json` (fabric, rust metal, paper) y `api.polyhaven.com/assets` (hdris cueva, texturas musgo) — sin bloqueos, CC0 confirmado por catálogo.
- Safebooru y Danbooru `related_tag` (ya recolectados por recolectar.py): comprobados y citados, no repetida la consulta.
- WebSearch (inglés): «Hollow Knight artbook official art Fangamer poster box art», «Hollow Knight Silksong key art official promotional image Team Cherry», «Hollow Knight crossover collaboration figure Youtooz First 4 Figures statue», «Hollow Knight cosplay Hornet materials armor tutorial», «Hollow Knight brush pack free texture ink halftone Photoshop CC0».
- WebSearch (español): «"Hollow Knight" evento colaboración marca crossover oficial merchandising café temático» — sin resultados de colaboraciones reales, sólo tiendas de merchandising propio.
- No busqué en japonés/coreano: Hollow Knight es una obra australiana (Team Cherry), sin origen japonés/coreano; sí tiene doblaje/traducciones pero el arte oficial sale directo del estudio en inglés.

### Bitácora de video

- `herramientas/fotogramas.py` sobre 6 vídeos (Dailymotion x2, Internet Archive x4), unos 100 fotogramas mirados en hojas de contacto + 10 fotogramas sueltos en grande — sin bloqueos; YouTube dio «Sign in to confirm you're not a bot» en yt-dlp directo, como avisa AYUDANTE.md.
- `herramientas/estilo.py` sobre 4 fotogramas de vídeo (Moss Grotto, 3 rincones de Bellhart) para hex y estilo de sombreado medidos, no de memoria.
- Wiki de Fandom (`hollowknight.fandom.com/api.php`): `imageinfo` sobre 16 archivos «Screenshot HK …» para confirmar 1920×1080 real antes de citarlos, y `list=search&srwhat=text&srsearch=onomatopoeia` (cero resultados, comprobado antes de decir que no hay onomatopeyas en pantalla) y wikitext completo de `Soundtrack_(Hollow_Knight)` y `Dream_Nail`.
- MusicBrainz y Archive.org (ya recolectados por recolectar.py): tracklists completos de Hollow Knight OST y Silksong OST, comprobados y citados sin repetir la consulta.
- WebSearch (inglés): «Hollow Knight ending credits song theme Sealed Vessel OR Dream», «Hollow Knight iconic sound effects geo chime bench save dream nail whisper recognizable», «Hollow Knight Silksong TikTok trend viral 2025».
- WebFetch: `en.wikipedia.org/wiki/Music_of_Hollow_Knight` (tono de la banda sonora, temas de créditos y de la pelea final).
- No busqué en japonés/coreano: Hollow Knight es una obra australiana (Team Cherry) sin origen ni doblaje japonés/coreano relevante para vídeo o música; el doblaje y las voces son punto de otro investigador.

### Bitácora de voz

- WebSearch (inglés, 12): «Hollow Knight does it have voice acting or is dialogue text only», «Hollow Knight "Hollow Speak" who voiced characters», «Hollow Knight most popular character official poll survey results», «Hollow Knight Steam reviews overwhelmingly positive percentage copies sold million», «Hollow Knight BAFTA award Silksong Game of the Year nomination 2025», «Hollow Knight 2017 original game awards BAFTA DICE Awards», «"Hollow Knight" reddit "Quirrel" favorite character beloved fan poll death saddest», «"Tyler Bartley" Quirrel Hollow Knight voice», «"Makoto Koji" Hollow Knight voice Hornet Mantis Lords Seer», «Hornet "GIT GUD" scream Hollow Knight meme "GEK TUU" word of god reddit AMA», «Hollow Knight Metacritic score IGN review "masterpiece"», «Hollow Knight Myla "hi ho cherry-o" infected transformation sad reddit», «Hollow Knight character height size comparison chart official Team Cherry canon», «Hollow Knight Hornet favorite food hobbies likes dislikes hunter's journal», «Hollow Knight fans identify with the Knight silent protagonist reddit», «Hollow Knight Quirrel Blue Lake theme music track name Christopher Larkin».
- WebSearch (español/portugués, 3): «Hollow Knight fandub español latino voces mod doblaje YouTube», «Hornet "guaraná" meme hollow knight reddit brasil», «Hollow Knight canción parodia español rap tema cover OST YouTube latino».
- Fandom wiki EN (`hollowknight.fandom.com/api.php`) y ES (`hollowknight.fandom.com/es/api.php`), `action=parse&prop=wikitext`: páginas Hornet (EN/ES), Quirrel (EN/ES), Caballero (ES) — sin bloqueos, con `curl` directo; también `list=search` para ubicar el nombre correcto de la página en español.
- TV Tropes (bloquea `curl` e `inner_text` de `navegar.py` porque el contenido vive en «folders» plegados con JS): se bajó el HTML completo (`--html --max 0`) y se limpió a mano con un script propio (quitar `<script>`/`<style>`, pasar `<li>`/`<h2>` a texto) para las páginas YMMV/HollowKnight, Characters/HollowKnightProtagonists, Memes/HollowKnight; TearJerker/HollowKnight se descargó pero no hizo falta explotarla a fondo: las escenas que hacen llorar del punto 21 ya salieron confirmadas por YMMV, la wiki y Steam Community.
- Arctic Shift (`arctic-shift.photon-reddit.com/api/comments/tree?link_id=…`) sobre 4 hilos de r/HollowKnight ya listados en datos-voz.md (773+718+104+104 votos): conteo propio de personajes mencionados en las respuestas con un script en Python.
- `yt-dlp --skip-download --print` sobre 4 vídeos de YouTube (2 de fandub, 1 de reacción, 1 de rap tributo): 3 dieron metadatos (vistas, canal, duración); 1 (el tráiler de «Voces del Reino») dio 429/pedir sesión y no se reintentó.
- Imágenes ya recolectadas por el investigador de imagen: miradas con Read `partes/hojas/personajes_01.jpg` (rostro fijo del Caballero, imágenes 100 y 102) y `personajes_02.jpg` (Hornet y Quirrel en contexto, imágenes 69-92) para el punto 13 — no se volvió a pedir la hoja, ya estaba en el repositorio.
- Segunda pasada (relanzo, `revisar_partes.py` marcó «2 minutos citados»): reintenté `yt-dlp` sobre el tráiler de «Voces del Reino» (`dBcBAtDvJRQ`) y sigue en 429/«sign in» (mismo bloqueo de siempre); en vez de insistir en YouTube, usé el tráiler oficial de Silksong ya confirmado en Dailymotion (`x7zx623`) con dos herramientas nuevas: `voz.py` (mide tono/expresividad, sin transcripción porque no hay palabras) y `fotogramas.py --cortes` (74 planos con minuto exacto), y miré las hojas resultantes con Read. Eso confirmó por tercera vía la falta de diálogo hablado (puntos 8/12), sacó el apodo «Wanderer» de Hornet en Silksong (punto 13) y subió los minutos citados de 2 a 8 sin inventar diálogo que el juego no tiene.

### Bitácora de texto

- Fandom `hollowknight.fandom.com` vía `api.php` (parse/wikitext): Hallownest, Geo, Dream Nail, Void, Hunter's Journal, Hallownest Seal, Charm Notch (redirect) — en español no hace falta, la wiki está en inglés y es la fuente primaria.
- WebSearch (inglés): «Hollow Knight font used logo Perpetua typeface», «Hollow Knight TCRF unused content», «Hollow Knight dialogue box font in-game text typeface», «Team Cherry Ari Gibson Hollow Knight art process interview», «Hollow Knight lore world Hallownest kingdom Pale King Void Radiance summary symbols», «games similar to Hollow Knight hand-drawn metroidvania», «Hollow Knight kingdom seal emblem wyrm symbol Team Cherry logo meaning».
- `tcrf.net/index.php?title=Hollow_Knight`: 403 Cloudflare con curl y con `herramientas/navegar.py`; sin snapshot en Wayback.
- Fuentes descargadas y comprobadas con fontTools (`getBestCmap`, códigos 0xf1 ñ, 0xd1 Ñ, 0xe1 á, 0xbf ¿, 0xa1 ¡): Cinzel, Cinzel Decorative, Cormorant Garamond, EB Garamond, Uncial Antiqua — las 5 con soporte completo de español.
- Fichas de Steam ya traídas por `recolectar.py` en `datos-texto.md` (capturas 1920×1080 de Hollow Knight, Silksong, dos bandas sonoras y Gods & Nightmares): usadas para el punto 11 sin repetir la consulta.
