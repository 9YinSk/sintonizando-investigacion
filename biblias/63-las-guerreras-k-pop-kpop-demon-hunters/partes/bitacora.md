## Bitácora

### Bitácora de imagen

- Español: «Las Guerreras K-pop vestuario colores», «Las Guerreras K-pop fondos de pantalla» — sin resultados propios en español más allá de calcos de EN; se priorizó inglés/coreano transliterado por ser producción reciente sin mucha cobertura hispana.
- Inglés (WebSearch, ~10 búsquedas): artbook/concept art, key visual poster, Fortnite collab, McDonald's collab, LEGO/Uniqlo/cafe, Honmoon symbol/logo, real idol cameos, Cookie Run Kingdom collab, cosplay tutorial, Youtooz figures, character designer interview.
- Fandom API (`api.php`) directa, sin bloqueo: fichas de Rumi/Mira/Zoey/Jinu (`Appearance`), Honmoon, HUNTR/X Tower, Namsan Tower, Demon world, categoría `Locations`; imágenes bajadas con cabecera `Referer: https://www.fandom.com/` (sin esto da 403).
- `herramientas/investigar_serie.py` reejecutado (la carpeta de hojas del recolector ya no existía en el contenedor): 10 hojas nuevas en `herramientas/referencias/las-guerreras-k-pop-kpop-demon-hunters/`, todas miradas con Read antes de elegir.
- `herramientas/estilo.py` sobre 10 imágenes oficiales descargadas (6 trajes + 4 fondos) para los hex medidos de vestuario y paisajes.
- `ambientcg.com/api/v2` (leather, fabric, paper, metal/gold) para texturas reales/CC0 equivalentes; sin bloqueo.
- WebFetch: creativebloq.com (artbook, poco contenido extraíble), 1000logos.net (logo, sí funcionó).
- No usé `navegar.py`: ninguna web de las tocadas dio bloqueo de verificación.

### Bitácora de video

- 2026-09-25 · leídos AYUDANTE.md, EQUIPO.md, ENCARGO.md, encargos/63-…md,
  partes/datos-video.md. Sin serie hermana (`herramientas/hermanas.py`).
- 2026-09-25 (en) · Fandom `kpop-demon-hunters` API (`action=parse&prop=wikitext`):
  ficha del film (`KPop Demon Hunters (Film)`) y soundtrack (`…/Soundtrack`):
  runtime 1:39:37, dirección, fecha, sinopsis, argumento completo, localizaciones,
  tracklist estándar y deluxe. También fichas de Rumi, Mira, Zoey, Jinu (pelo,
  ojos, armas, especie).
- 2026-09-25 · `fotogramas.py` sobre 5 vídeos (bajados con yt-dlp, sin login):
  tráiler oficial (Dailymotion x9k1104, cada 8 s + 3 fotogramas sueltos),
  «How It's Done» lyric video (IA youtube-QGsevnbItdU, cada 6 s + 4 sueltos),
  «Soda Pop» lyric video (IA youtube-983bBbJx0Mk, cada 6 s + 3 sueltos), «Golden»
  lyric video (IA golden-official-lyric-video…, cada 6 s + 5 sueltos), «Takedown»
  lyric video (IA youtube-l8Dr7vzMSVE, cada 6 s). Vídeos borrados de
  `/tmp/claude-0/trabajo/…` tras sacar las hojas (quedan hojas + fotogramas
  sueltos + los `.json` de `estilo.py`).
- 2026-09-25 · `estilo.py` (Pillow k-means) sobre 12 fotogramas sueltos para
  paleta hex y tipo de sombreado (punto 4).
- 2026-09-25 (en) · búsquedas web (WebSearch, cupo usado: 6 de ~50): «"KPop
  Demon Hunters" "Golden" TikTok dance challenge viral trend»; «"Golden"
  HUNTR/X Billboard Hot 100 number one record»; «"KPop Demon Hunters" Netflix
  most watched film record weeks Billboard 200 soundtrack chart»; «Saja Boys
  singing voices Andrew Choi Danny Chung Kevin Woo real singers»; «"KPop Demon
  Hunters" trailer official Netflix release date teaser July 2025»; «"KPop
  Demon Hunters" sing-along theatrical event August 2025 box office»; «"KPop
  Demon Hunters" director Maggie Kang "breaks down" scene YouTube Vanity Fair
  Anatomy». Fuentes: Billboard, Netflix Tudum, The Hollywood Reporter, AOL,
  Wikipedia (Andrew Choi, Kevin Woo), TikTok (discover pages).
- No usé `navegar.py`: no hizo falta abrir ninguna web con bloqueo de curl para
  estos puntos (las que consulté — Fandom API, Billboard, Netflix Tudum,
  Hollywood Reporter, AOL — respondieron directo).

### Bitácora de voz

- Búsquedas web (inglés): «KPop Demon Hunters personaje favorito encuesta poll most popular
  character» → Koreaboo, CBR, BuzzFeed, foro de Fandom.
- Búsquedas web (español): «ANMTV Guerreras K-pop doblaje latino reparto voces» → confirma
  ANMTV + Infobae como segunda/tercera fuente del reparto.
- Fandom `kpop-demon-hunters.fandom.com/api.php`: wikitext completo de Rumi, Mira, Zoey,
  Jinu, Gwi-Ma, Celine, Saja Boys y Bobby (secciones Trivia, infobox, Personality).
- `herramientas/voz.py` sobre 6 muestras oficiales de audio de Doblaje Wiki (Rumi, Mira,
  Zoey, Jinu, Gwi-Ma, Celine): transcripción + tono medido.
- `yt-dlp` sobre los clips Dailymotion `x9tkmqo` (trailer latino, sin diálogo) y `x9sl3s6`
  (ya no existe, «Not found», dos intentos).
- Fotogramas reutilizados de `/tmp/claude-0/trabajo/63-las-guerreras-k-pop-kpop-demon-hunters-video/`
  (ya sacados por el investigador de vídeo con `fotogramas.py`), mirados con Read: `golden`
  fotogramas 108 y 132, `howitsdone` fotograma 66, `takedown` fotograma 66.
- Búsquedas web (WebSearch, inglés): «KPop Demon Hunters Netflix most watched film ever
  record Nielsen viewership», «KPop Demon Hunters crying scene made me cry reddit Jinu
  death», «KPop Demon Hunters fandom inside jokes memes Derpy tiger Sussie cat Gwi-Ma meme»,
  «KPop Demon Hunters fans annoyed misconception Saja Boys not villains», «KPop Demon Hunters
  fans criticized inaccurate merch fan art», «KPop Demon Hunters YouGov survey favorite
  character percent».
- Búsquedas web (español): «Guerreras K-pop fandub español latino youtube tiktok cover
  Golden», «Guerreras Kpop doblaje fandub tiktok cover español latino creador».
- Páginas leídas enteras con `curl` (tras limpiar HTML con Python): ANMTV (reparto de
  doblaje), Infobae (reparto de doblaje), Netflix Tudum «Golden Milestone», Koreaboo (crítica
  al merchandising), Wikipedia «List of accolades».
- Páginas leídas con `herramientas/navegar.py` (curl daba 403): TV Tropes `Memes/…` (sí,
  contenido completo) y `YMMV/…` (sólo encabezados, el contenido está en pestañas
  colapsadas por JavaScript que el selector no expandió — no insistí más de dos intentos),
  Collider (ranking de personajes por «likability», contenido completo), IMDb poll (pantalla
  de verificación «no soy un robot», no se pudo pasar).
- `arctic-shift.photon-reddit.com`: búsquedas por título en r/KpopDemonhunters («cry»,
  «hurts so much», «sobbing», «meme», «identify», «relate», «Derpy», «Sussie»,
  «underrated», «cursed», «brainrot»); varias devolvieron 0 resultados o error de límite de
  peticiones («Timeout. Maybe slow down a bit») — no insistí en bucle.
- Fandom Doblaje Wiki: confirmé de paso la existencia de un blog de fandub alternativo
  («FanDubbing22») con la propia API de búsqueda de Google indizada.

No queda nada obligatorio pendiente de mis puntos (7, 8, 12, 13, 20, 21, 22): lo que quedó
sin cerrar (vistas exactas de fan dubs, minuto de un clip doblado del sacrificio de Jinu,
altura de Rumi) es extra y ya está anotado en «No encontré» con las búsquedas hechas.

### Bitácora de texto

- 2026-09-25 · leídos AYUDANTE.md, EQUIPO.md, ENCARGO.md, `encargos/63-…md`, `partes/datos-texto.md` (casi vacío: la obra no es un juego de Steam), y `partes/imagen.md` + `partes/video.md` completos, ya escritos por el resto del equipo, para no repetir consultas.
- Fandom API (`kpop-demon-hunters.fandom.com/api.php`), sin bloqueo: listado completo de páginas (`allpages`), wikitext de `Korean Cultural References`, `Honmoon`, `Demon`, `Timeline`, `HUNTRIX`, `Saja Boys`, `International Idol Awards`, `Category:Logos`; imágenes descargadas con `Referer: https://www.fandom.com/` y convertidas de WebP a PNG con Pillow para poder medirlas y verlas.
- `herramientas/estilo.py` sobre 3 logos propios (`Huntrix_Logo.jpg`, `Saja_Boys_Logo.jpg`, `KPop_Demon_Hunters_Logo.png`) y sobre 1 captura del juego de Roblox, para los hex de marca/interfaz — ninguno medido antes por el resto del equipo.
- **API pública de Roblox** (sin necesidad de cuenta ni WebSearch): `apis.roblox.com/universes/v1/places/{placeId}/universe` para sacar el `universeId` del juego oficial a partir de su URL, `games.roblox.com/v2/games/{universeId}/media` para listar sus capturas aprobadas, y `thumbnails.roblox.com/v1/assets?assetIds=…` para resolver cada `imageId` a una URL de imagen descargable — así conseguí 4 capturas oficiales del juego sin depender de que la prensa las hubiera recogido.
- `fontTools` (`TTFont().getBestCmap()`) sobre 8 fuentes descargadas de verdad (no de memoria): **Hunters K-Pop** (FontSpace), **Permanent Marker**, **Anton**, **Caveat**, **Noto Sans KR**, **Montserrat**, **Arimo** y **Roboto** (las siete últimas de Fontsource/jsDelivr, recorte «latin» — el recorte «latin-ext» de Fontsource NO siempre trae las tildes españolas, hay que pedir el «latin») — las ocho con tildes, ñ/Ñ, ¿ y ¡ comprobados carácter a carácter, ninguna de memoria.
- Inglés (WebSearch, cupo compartido del contenedor entre los 4 investigadores — se agotó a mitad de esta tanda, ver nota abajo): animación/render/Imageworks, character designer/art director, logo font identification, mobile game oficial, credits font, Roblox interface, similar movies/anime influence, Roblox UI font, Netflix subtitle font, Korean title logo, Hunters K-Pop font license, fontsinuse.com, Picturemill titles — 15 búsquedas en total antes de que el cupo compartido (200 del contenedor) se agotara.
- **Aviso para el jefe**: el cupo de `WebSearch` es del contenedor entero (200 llamadas), no de 50 por investigador como dice AYUDANTE.md — se agotó por el uso combinado de los 4 investigadores en paralelo, no sólo el mío. A partir de ahí seguí sólo con `curl`/`navegar.py`/Fandom API, que no cuentan contra ese cupo.
- `navegar.py` (para sitios que bloquean `curl`): Collider (15 recomendaciones, cargó bien), CBR (cargó bien), Picturemill (cargó bien), TCRF (403, dos intentos), Screendaily (405/captcha, dos intentos), Wayback Machine (fallo de red, dos intentos).
- `curl` directo (sin bloqueo): No Film School (entrevista Adobe/Substance 3D), Creative Bloq (Unreal Engine 5), Cartoon Brew (parcial, luego completado con `navegar.py`... en realidad cargó bien con `curl`), dafont (hilo de identificación del logo), Geeks OUT (entrevista completa a Maggie Kang), Fandom API.
- No hice falta usar coreano/japonés/chino como idioma de búsqueda propio: toda la película es una producción occidental (Sony/Netflix, EE. UU.) en inglés, y las fuentes en coreano que sí importan (nombres de armas, términos de cultura) ya vienen traducidas y con su hangul original dentro de la propia wiki en inglés, citando prensa coreana (koreaherald.com, korea.net) que enlacé arriba.
