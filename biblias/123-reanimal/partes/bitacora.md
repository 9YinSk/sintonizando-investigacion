## Bitácora

### Bitácora de imagen

- Comprobación pedida por el investigador de vídeo (Niño = saco/capucha de arpillera, Niña = máscara de conejo): repasé las 6 apariciones de «arpillera»/«conejo»/«máscara»/«saco» en esta parte (puntos 1, 3, 15, 23) y todas asignan bien cada prenda; lo confirmé además mirando el render `TheGirl.png` en la hoja de contacto (máscara + vestido claro, cuchillo, linterna) y `Boy.png` (capucha oscura de arpillera). No había confusión que corregir.
- Corregí dos datos con la API de Fandom (`reanimal.fandom.com/api.php`, con cabecera de navegador porque sin ella Cloudflare responde con un reto): la URL de `ArtofReanimal_Cover.png` (hash `a/aa` inventado → `a/a8` real) y la medida de `Boy.png` (313×550 de una pasada anterior → 401×822, la que da hoy la wiki; probablemente el archivo se revisó tras esa medición, `cb=20260214032843`).
- Español: sin búsquedas nuevas en esta tanda (ya cubiertas en pasadas anteriores).
- Inglés (directo, sin buscador): API de Fandom `list=allimages` (2 páginas, 667 imágenes) para confirmar tamaño real y URL exacta de `ArtofReanimal_Cover.png`, `Collectorsedition.png`, `Boy.png`, `TheGirl.png`, `Feature-graphic-1/2/3.png`, `Reanimal-Officialart-1/2`, `DLCKeyArt.jpg`, `Mother_Spider_Kids_trading_card.png` y dos páginas del artbook (Hood pág. 11, Mother pág. 27); API de Poly Haven (`/info/hessian_230`, `/info/hessian_380`) para la resolución máxima real de las dos texturas de arpillera; API de ambientCG (`/api/v2/full_json`) para intentar sacar resolución de Metal041B (no la da; se usó el estándar de 2048×2048 con el que se listan sus previews).
- Verifiqué de nuevo (visualmente, con la herramienta de lectura de imagen) las 3 hojas de contacto completas (`arte_oficial_01.jpg`, `personajes_mascaras_01.jpg`, `personajes_render_01.jpg`) para el aviso de arriba y para confirmar los números de imagen citados en el resto de la parte.
- Cree `imagen.json` con 43 referencias candidatas (campos `url`, `fuente`, `ancho`, `alto`, `que_es`, `para_que`, `licencia`), cubriendo los 6 puntos de este rol: arte oficial (11), fan art (4), 3D con licencia (9), fondos de pantalla (6), renders para hex (2), texturas libres (7) y colaboraciones/figuras/cosplay (3).

### Bitácora de video

- Dailymotion API (`api.dailymotion.com/videos?search=…`): «Reanimal opening/ending/trailer/escena» (ya en `datos-video.md`), «Reanimal Sniffer tricycle» (sin resultado directo), «Reanimal gameplay» (encontré el id correcto `x9xxbbm`, que luego dio 404 al bajarlo con `yt-dlp`; usé `x9o072c` y `x9ve578` en su lugar, que sí funcionaron).
- `fotogramas.py` sobre 3 tráilers de Dailymotion (`xa1mxgm`, `x9o072c`, `x9ve578`): hojas de contacto cada 3-4 s + fotogramas grandes en segundos concretos. `x9xxb36` y `x9xxbbm` fallaron con «Not found» pese a aparecer en la API (geobloqueo o vídeo caído).
- `reanimal.fandom.com/api.php`: `allpages`, `categorymembers` de Characters/Chapters/Locations, y `action=parse&prop=wikitext` de The Boy, The Girl, The Island, The Mother, Sniffer, REANIMAL, REANIMAL (soundtrack), Dead in the Water, The Cleaning House, No Shelter, Down in a Hole, Nobody Left Behind, The Spoils, The Watcher (todo en inglés, es una wiki en inglés).
- `navegar.py` en TV Tropes `NightmareFuel/Reanimal` (bloquea a curl): confirmó el orden completo de capítulos, incluidos los del DLC «The Prisoner».
- YouTube `oembed` (sin sesión) para comprobar 4 pistas de la BSO citadas por la wiki: las 4 devolvieron el canal oficial «Reanimal - Topic».
- Un intento directo de `yt-dlp` sobre YouTube (id `ledRJ2CQuGU`): 429 y «sign in to confirm you're not a bot»; no insistí, según lo avisado en AYUDANTE.md.
- WebSearch (inglés/español): «Reanimal TikTok viral moment reaction», «Reanimal review análisis Little Nightmares comparación horror 2026», «"Reanimal" tricycle scene chapter wiki jumpscare».
- Steam (`store.steampowered.com/app/2129530`): descargué 4 capturas oficiales 1920×1080 directamente para medir hex y confirmar escenas de los tráilers.
- `ambientcg.com/api/v2/full_json` (texturas): 2 intentos sin resultado; no insistí más.
- **Segunda pasada (modo seguir)**: Dailymotion API `Reanimal gameplay walkthrough` → encontré «REANIMAL Full Gameplay Demo 45 Minutes» (`x9tibzi`, 45:46). `fotogramas.py --cada 30/15` sobre los primeros 35 min (3 tandas) para localizar la celda del cap. 1 y buscar el triciclo del cap. 2. `reanimal.fandom.com/api.php`: wikitext de The Prisoner (Chapter), The Prisoner (Character), Bandage, Bucket, Hood, No Shelter, The Spoils, Masked Children — para identificar con certeza quién es quién en cada fotograma (la primera pasada tenía al Niño y la Niña cruzados en dos escenas, ya corregido en los puntos 2 y 14). `yt-dlp` contra TikTok (`@.reanimal_ln`): bloqueado, sin vía alterna.

### Bitácora de voz

- Doblaje Wiki, API `action=parse&prop=wikitext`, página REANIMAL completa (no solo la tabla parseada por el recolector) → reparto, estudio, traductores, créditos.
- reanimal.fandom.com, API `action=query&prop=revisions` sobre: The Boy, The Girl, The Brother, The Sister, Hood, Bandage, Bucket, Masks, Masked Children, The Mother, The Prisoner (Character), The Second Prisoner, The Soldier, The Watcher, Pigs, The Spiral Whale, Unused and Cut Content, Art of REANIMAL, Critters, Skins, REANIMAL (soundtrack).
- Imagen de créditos del doblaje descargada (`Créditos REANIMAL ESLAT.png`, formato WebP real) y leída con `tesseract -l spa`, contrastada mirando la imagen directamente.
- Renders oficiales descargados y mirados: TheGirl.png, The_Boy.png (para comprobar los agujeros de la máscara).
- `voz.py` sobre las 8 muestras oficiales de audio del doblaje latino (Boy, Girl, Hood, Bandage, Bucket, Pig, Whale, Kid) — todas oídas, no solo listadas.
- `fotogramas.py` sobre el teaser oficial (dailymotion/xa1mxgm, cada 3 s, 31 fotogramas) y el tráiler de anuncio (dailymotion/x94c4ui, cada 3 s, 26 fotogramas + 3 fotogramas sueltos en 0:30, 0:45 y 0:51), todos mirados con Read.
- Reddit r/ReanimalGame vía Arctic Shift (`/api/posts/search`, 100 posts; `/api/comments/search` sobre 3 hilos) — búsqueda por tema (favorite character, why I love, best scene) sin resultado por `title=`, así que ordené por puntuación a mano.
- Danbooru: `/counts/posts.json` para los tags `girl_(reanimal)`, `boy_(reanimal)`, `hood_(reanimal)`, `reanimal` (contraste del dato ya recolectado).
- WebSearch (en español e inglés): «Reanimal doblaje latino elenco», «Reanimal review Tarsier Studios metacritic score», «Reanimal ending explained cry sad scene reddit», «Reanimal fandub español latino youtube», «"Reanimal" personaje favorito encuesta poll», «"Made in Spanish" estudio doblaje Reanimal México», «Reanimal opening ending song vocal theme soundtrack», «Reanimal Tarsier Studios interview director character design Boy Girl».
- `navegar.py` sobre news.xbox.com/en-us/2026/02/13/reanimal-interview (entrevista completa leída), tvtropes.org/pmwiki/pmwiki.php/Characters/Reanimal (solo el índice, las carpetas están cerradas por JS) y reanimalgame.com/tier-list (guía de fans, sin relación oficial).
- `anmtv.la` inalcanzable (curl: timeout; navegar.py: `ERR_TUNNEL_CONNECTION_FAILED`) — no pude usarlo como segunda fuente de doblaje pese a intentarlo dos veces.

### Bitácora de texto

- Español: «Reanimal wiki fandom», «Reanimal tipografía logo» → sin resultados
  útiles en español; se pasó a inglés.
- Inglés (web): «Reanimal Tarsier Studios interview Unreal Engine art style»,
  «Reanimal Tarsier Studios "toon shader" OR "stop-motion" art director
  interview», «Reanimal review "no dialogue" OR "don't speak" OR subtitles
  gibberish language children», «"Reanimal" "Unreal Engine 5" Tarsier»,
  «Reanimal Tarsier Studios ArtStation concept artist "Konstantin Kostadinov"
  OR "Petrus Johansson" postmortem».
- Fandom API (`reanimal.fandom.com/api.php`): `list=allpages` (lista completa
  de páginas), `action=parse&prop=wikitext` sobre Masks, Controls, Unused and
  Cut Content, REANIMAL, The Boy, The Spiral Whale, Posters, Paintings
  Portraits and Photos, Art of REANIMAL, REANIMAL: The Expanded World,
  Coffins, The Island; `list=search` para «spiral» y «dialogue».
- `reanimal.thqnordic.com`: HTML completo descargado y filtrado con `grep`
  para fuentes (`font-family`, `.woff`) — reveló la letra «Fabrikat».
- Steam: ficha de la app 2129530 (`store.steampowered.com` + API
  `appdetails`) para descripción, 14 capturas, tabla de idiomas (interfaz,
  audio, subtítulos) y categorías.
- `en.wikipedia.org/wiki/Reanimal`: artículo completo (desarrollo, argumento,
  recepción con notas de Metacritic/OpenCritic y reseñas).
- `gamecritics.com/jason-ricci/reanimal-review`,
  `cubed3.com/features/interviews/tarsier-interview`: entrevistas y reseñas
  completas descargadas y filtradas con `python3 -re` (nunca impresas enteras).
- `tcrf.net`: dos intentos (curl y `navegar.py`), 403 verificación Cloudflare
  las dos veces; Wayback Machine CDX sin snapshots.
- fontTools: `TTFont(...).getBestCmap()` sobre Anton, Barlow Condensed, Big
  Shoulders Display, Permanent Marker, Yanone Kaffeesatz y Noto Sans JP
  (descargados de `fonts.googleapis.com`/`fonts.gstatic.com`), comprobando
  á é í ó ú ñ Ñ ü ¿ ¡ y (en Noto Sans JP) hiragana/katakana/kanji.
- Hojas de contacto propias armadas con Pillow a partir de las capturas de
  Steam (`/tmp/claude-0/trabajo/123-reanimal-texto/hoja_capturas*.jpg`),
  miradas con Read antes de describir el estilo.
