## Bitácora

### Bitácora de imagen

- `recolectar.py` (previo, no repetido): Fandom (8 páginas), Wallhaven, Sketchfab, Openverse → `datos-imagen.md`.
- `investigar_serie.py --serie "No Man's Sky" --wiki nomanssky --paginas Traveller "Priest Entity Nada" "Specialist Polo" Artemis "The Atlas" Multi-Tool Starship Exosuit`: falló primero con `--wiki nomanssky_gamepedia` (subdominio equivocado, error SSL); funcionó con `--wiki nomanssky` → 171 imágenes enlazadas, 70 grandes, 2 hojas de contacto en `herramientas/referencias/no-man-s-sky/` (miradas con Read, copiadas a `hojas/`).
- `herramientas/estilo.py` (paleta + estilo, con Pillow/numpy/opencv en local, no busca en la red): 9 imágenes — Exosuit/nave por defecto, Multiherramienta estándar, capa de Nada, traje de Artemis, 4 paisajes de planeta de la wiki, 1 fondo de pantalla oficial de Wallhaven.
- Web search (inglés): «No Man's Sky key art cover retro sci-fi pulp inspiration artist», «No Man's Sky box art 70s science fiction book cover style», «No Man's Sky cover art artist Malcolm Smith Innerspace retro poster design» (pista falsa), «No Man's Sky official merchandise collaboration figure Numskull Fangamer Youtooz», «No Man's Sky crossover collaboration PlayStation exclusive content event», «No Man's Sky Palworld collaboration 2025 official confirmed launched», «No Man's Sky alien language font Korvax Gek Vy'keen glyphs symbol alphabet», «No Man's Sky official wallpapers download nomanssky.com media», «Grant Duncan No Man's Sky art director Chris Foss interview influence», «No Man's Sky fan art ArtStation traveler exosuit illustration», «No Man's Sky logo meaning starburst symbol design», «Art of No Man's Sky official artbook book print», «No Man's Sky cosplay exosuit official recognition photo».
- Web search (japonés): «No Man's Sky pixiv イラスト ファンアート» → presencia escasa en Pixiv, confirmado.
- Páginas leídas directamente (curl, filtrando con Python/regex, nunca la respuesta entera): nomanssky.com (blog del arte, crossover con Mass Effect, aniversario, tienda), Wikipedia API (`Development of No Man's Sky`, extracto), GamesBeat (entrevista a Grant Duncan), Push Square (portadas retro de fans), Gematsu (crossover Mass Effect), Insert Coin Clothing, thevideogamelibrary.org (ficha del artbook), archive.org (metadata del escaneo del artbook), Youtooz (tienda oficial).
- Fandom API (`api.php`, sin bloqueo): `Traveller`, `Exosuit`, `Multi-Tool`, `Space Anomaly`, `Language`, `Alphabet` (extractos de texto) + `imageinfo` de `Alphabet.png` y `Freighter writing.jpg`.
- Sketchfab API (`v3/search`, `q=No Man's Sky`, `downloadable=true`): 8 modelos con licencia, autor y miniatura confirmados.
- ambientCG API (`full_json`, ojo: sólo acepta una palabra en `q`, no frases): `metal`, `rust`, `panel`, `paper`, `fabric` → 3 texturas CC0 elegidas (Corrugated Steel 009, Metal 063, Solar Panel 003).
- Bloqueados: time.com (403 a curl), highdefdigest.com (403, Cloudflare), tweaktown.com (403); `navegar.py` no pudo abrir ninguno (falta el ejecutable de Chromium en este contenedor: «BrowserType.launch: Executable doesn't exist»). No insistí más de dos intentos en cada uno, según la regla.

### Bitácora de video

- Miré con `fotogramas.py`: tráiler de anuncio (archive.org, mirror de YouTube aCgWabJssVI), tráiler E3 2015 (Dailymotion x89lilx), tráiler «Echoes» (Dailymotion x8nggcs), tráiler «Prisms» (Dailymotion x89nujz) y tráiler del 10.º aniversario (archive.org, mirror de YouTube -sK7EGiJSDk). Todos los clips venían ya localizados en `datos-video.md` salvo el del 10.º aniversario, que busqué porque es el más reciente (ago-2026) y encaja con «planetas de colores» del encargo.
- Probé `fotogramas.py` directo contra YouTube dos veces (aCgWabJssVI y -sK7EGiJSDk): ambas dieron «Sign in to confirm you're not a bot» (bloqueo de este servidor). Plan B que funcionó: el mismo vídeo mirrorado en `archive.org/details/youtube-<id>`, tal y como indica AYUDANTE.md.
- Intenté `yt-dlp` para sacar metadatos (duración/vistas) de dos vídeos de análisis en YouTube: uno dio 429 en el primer intento y funcionó al repetir («The Redemption Of No Man's Sky», GameSpot); el otro («The Engoodening», Internet Historian) siguió bloqueado, así que usé IMDb + Lemmy.World para la duración.
- Medí color y estilo con `herramientas/estilo.py` sobre 10 fotogramas propios (no descargué arte de terceros para esto).
- Búsquedas web (inglés, ~10 de mi cupo de 50): «65daysofstatic No Man's Sky soundtrack interview», «Paul Weir procedural audio No Man's Sky interview», «No Man's Sky TikTok viral trend meme», «No Man's Sky redemption documentary Noclip», «The Engoodening video essay», «No Man's Sky TikTok millions views», «No Man's Sky 10th anniversary trailer 2026 update», «No Man's Sky launch controversy meme lying Sean Murray». No hice búsquedas en japonés/coreano: el estudio (Hello Games) es británico y la obra no viene de Asia, así que no aplica ese requisito de ENCARGO.md.
- Wiki de Fandom (`nomanssky.fandom.com`) por su API: wikitext de «Music for an Infinite Universe» (lista de pistas verificada) e imágenes ya recolectadas del Viajero (descargadas con cabecera `Referer` para poder mirarlas).
- ambientCG (`api/v2/full_json`): texturas de arena/tierra («Ground054») y roca («Rock061»), ambas CC0, para las «texturas reales equivalentes» del punto 4.
- No until usé `navegar.py`: no hizo falta, ninguna web relevante bloqueó curl directamente (TikTok y Dailymotion respondieron bien por API).

### Bitácora de voz

- Doblaje Wiki API (`doblaje.fandom.com/es/api.php`): 3 variantes de título +
  1 búsqueda de texto libre → sin página de la obra (español).
- Fandom `nomanssky.fandom.com/api.php`: wikitext de Nada→Priest Entity Nada,
  Polo→Specialist Polo, Gek, Korvax, Vy'keen, The Atlas, Sentinel, Artemis,
  Apollo, -null-, Telamon; `imageinfo` de 8 imágenes para medir tamaño real
  (inglés).
- WebSearch (inglés y español): doblaje/voces NMS, voice actor narrator
  credits, Paul Weir alien language, Rutger Hauer trailer, meme Sean Murray
  redemption arc, Steam Awards Labour of Love, review 2024/2025 comeback,
  fandub español, lágrimas en la lluvia homenaje, gameplay comentado latino.
- `behindthevoiceactors.com` vía `navegar.py` (Cloudflare bloquea curl
  directo) → ficha de reparto.
- Steam Store API `appdetails` (oficial) → tabla de idiomas.
- `navegar.py` sobre Steam Community (discusión doblaje) y Steam Store
  (tabla de idiomas) → funcionó bien, sin bloqueo.
- `herramientas/voz.py` sobre el tráiler de Rutger Hauer (mirror Dailymotion
  x443lhp) → transcripción + análisis de voz.
- Arctic Shift (Reddit, inglés): `posts/search` con `title=` (nota: el
  parámetro `sort` sólo acepta `asc`/`desc`, no `sort_type`; búsquedas de una
  sola palabra como «cry», «chills», «beautiful», «masterpiece» devuelven 0
  resultados aunque el hilo exista — el buscador de título parece exigir
  coincidencias más largas o exactas — mientras que frases de 2-3 palabras sí
  funcionan) y `comments/search` con `body=Artemis`.
- ANMTV bloqueado por política de proxy del contenedor (`connect_rejected`),
  probado por curl y por `navegar.py`.
- Wikipedia API: `Development of No Man's Sky` (extracto, confirma a Paul
  Weir y 65daysofstatic) funcionó; una segunda consulta a `No Man's Sky` dio
  «too many requests» (límite de tasa) y no reintenté para no gastar cupo.

### Bitácora de texto

- `datos-texto.md` (recolectado antes): sólo 6 capturas de Steam de interfaz 1920×1080 — miradas en contacto propio (`contacto_steam.jpg`), sin diálogo visible en ninguna (son capturas de marketing sin HUD).
- Leído primero `imagen.md` y `video.md` (ya escritos por los otros investigadores) para no repetir: el alfabeto alien, el logo, las 4 paletas de planeta y los modelos Sketchfab ya estaban ahí — aquí sólo se referencian, no se repiten.
- GitHub: `add_repo` + clon superficial de `NMSCD/No-Mans-Sky-Universal-Font` (con `GIT_LFS_SKIP_SMUDGE=1`) para bajar los 4 `.ttf` reales y comprobarlos con fontTools (`TTFont(f).getBestCmap()`, chequeo de á é í ó ú ñ Ñ ¿ ¡ ü) — los cuatro dieron `True` en todo.
- Google Fonts / Fontsource: `api.fontsource.org/v1/fonts?family=Jost` (licencia OFL, subsets latin+latin-ext) y descarga directa de `fonts.gstatic.com` para Jost y Roboto, comprobadas igual con fontTools.
- Fandom API (`nomanssky.fandom.com/api.php`, sin bloqueo): páginas `Language`, `Alphabet`, `NPC conversation` (obsoleta), `Automatic translation device`, `Adventures in No Man's Sky`, `Artemis`, `The Atlas`, `Sentinel`, `Expedition Patches`, `Inventory`, `Quick Menu`, `Overseer (NPC)`, `Discoveries` — texto (`prop=wikitext`) e imágenes (`prop=pageimages` / `allimages`).
- Imágenes propias miradas con Read (no sólo citadas): `dialogue.jpg` (cuadro de diálogo real, 2522×1138), `contacto_ui.jpg` (inventario 2016 + menú rápido), `overseer.jpg` (hologramas), `patches.jpg` (2 parches de expedición), `contacto_steam.jpg` (6 capturas oficiales de Steam) — todas medidas en hex con `herramientas/estilo.py`.
- Steam: `store.steampowered.com/api/appdetails?appids=275850` (lista completa de 189 capturas, sólo usadas las ya citadas).
- `python3 herramientas/navegar.py` (sin ventana, con Chromium): funcionó para `gameuidatabase.com` (pasó el reto de Cloudflare) pero **no** para `tcrf.net` (403 duro, no es el mismo tipo de verificación).
- `WebSearch` (11 búsquedas antes de agotarse la cuota compartida de la sesión, en inglés): fuente UI/HUD, fuente del logo, mecánica de diálogo alienígena, cómic "Adventures in No Man's Sky", lista de expediciones, cita "playable painting" (sin resultado), filtros de post-proceso, juegos parecidos, tutorial de Blender estilo NMS, fuente CJK, inspiración de Sean Murray en "Elite".
- Bloqueados: `tcrf.net` (403 Cloudflare, con y sin navegar.py) y `web.archive.org` (confirmado esta tanda como **bloqueo de política de egress del contenedor**, no de la fuente ni de Cloudflare: `curl` por `http://` devolvió el texto literal "Blocked by egress policy") — repetido en esta tanda de relanzo por las tres vías posibles, sin éxito; no se insiste más, es un límite de infraestructura, no de investigación.
- Verificación propia del repositorio: `ls biblias/` para comparar con otras láminas del servidor (punto 24), sin necesidad de fuente externa.
- **Segunda pasada (relanzo, 25-sep-2026)**: se cerraron los 4 huecos ⚠️ que quedaban como extra — (1) fuente real del alfabeto alien descargada del bundle JS de `alphabet.nmscd.com` (`raw.githubusercontent.com/NMSCD/Expedition-Alphabet/.../nms-alphabet.ttf`) y comprobada con fontTools (NO trae tildes/ñ/¿¡, dato ahora confirmado en vez de dudoso); (2) captura propia del Galactic Map (`nomanssky.fandom.com`, imagen oficial 1920×1080) mirada y medida con `estilo.py`; (3) segunda imagen oficial de una Atlas Interface (`NMSAtlasInterface.jpg`) mirada directamente para confirmar la forma del símbolo del Atlas, antes sólo descrita en texto; (4) TCRF/Wayback reintentado por 3 vías, confirmado bloqueo de política de red del contenedor (no de la fuente, no hace falta reintentar). `texto.json` pasó de 12 a 15 referencias.
