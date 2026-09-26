## Bitácora

### Bitácora de imagen

- Fandom API (`shigatsu-wa-kimi-no-uso.fandom.com/api.php`) — pageimages de los 4 personajes, imageinfo de las 4 páginas + galerías (idioma: inglés/wiki).
- `investigar_serie.py --serie "Your Lie in April (Shigatsu)" --wiki shigatsu-wa-kimi-no-uso --paginas "Kousei Arima" "Kaori Miyazono" "Tsubaki Sawabe" "Ryota Watari"` — regenerado porque `herramientas/referencias/` estaba vacío al arrancar (otro proceso lo había limpiado); 112 imágenes, 74 grandes, 2 hojas miradas enteras con Read.
- `herramientas/estilo.py` sobre 6 imágenes locales (paleta dominante de imagen completa) — poco útil por la iluminación cálida; sustituido por recortes propios con Pillow por prenda.
- Wallhaven (ya recolectado, revisado y ordenado).
- Openverse (ya recolectado: fan art expuesto + cosplay).
- Sketchfab: sin `--con-gemini`, probé `https://api.sketchfab.com/v3/search?type=models&q=your+lie+in+april&downloadable=true` y variantes en inglés y japonés romanizado — sin resultados relevantes.
- ambientCG API (`type=Material&q=paper|wood|fabric|metal|leather`) — 5 texturas CC0 elegidas y citadas en el punto 19.
- OpenGameArt (`screentone`, `halftone`) e itch.io (`tag-screentone`, `tag-manga` en la sección `/free/`) — sin resultado libre; sólo un pack de pago.
- Wikimedia Commons API — 429 (límite de tasa) en dos intentos, sin insistir más.
- Fandom API `srsearch=merchandise|collaboration|cafe` — sin resultados en la wiki de imagen para el punto 23.
- `goodsmileshop.com` (búsqueda de figuras) y `myfigurecollection.net` — sin resultado / bloqueado; `navegar.py` no disponible en este contenedor (Chromium headless no instalado).
- Recortes propios con Pillow (no `estilo.py` completo) sobre 9 imágenes locales para el punto 15, apuntando coordenadas por prenda tras mirar cada imagen con Read.

Pendiente sin ser obligatorio (queda en «No encontré»): figuras oficiales, café temático, cuero medido con hex propio, más fan art de Pixiv listado uno por uno.

### Bitácora de video

- `datos-video.md` (recolectado antes de empezar): tráiler AniList, clips Dailymotion (sólo AMV de fans), MusicBrainz. Partí de ahí y descarté los AMV de fans como fuente de «escena icónica» (no son metraje oficial en la mayoría de los casos).
- Dailymotion API (`api.dailymotion.com/videos?search=…`), en inglés y japonés: «Shigatsu wa Kimi no Uso official trailer», «Your Lie in April official trailer Aniplex», «四月は君の嘘 PV», «Hikaru Nara Goose house», «Kirameki Ai Kayano», «Orange 7 nanauchi», «Your Lie in April analysis video essay», «Your Lie in April AMV edit», «Shigatsu wa Kimi no Uso reseña» → encontré el PV2 oficial (x2682f1), un vídeo de tendencia tipo «POV» (xa3w48g) y varios «Twixtor edit».
- `api.animethemes.moe`: error 522 en todos los intentos (caído, igual que en `recolectar.py`).
- Internet Archive: `archive.org/advancedsearch.php` con «Shigatsu wa Kimi no Uso» → ítem `EVYourLieinApril`, los 22 episodios + OVA en 1080p. Localicé OP/ED/escenas con `ffmpeg -ss <segundo> -i "archive.org/download/…"` (range requests, sin bajar el archivo completo) y contact sheets propias con Pillow, igual que hace `fotogramas.py`.
- Wiki de Fandom (`shigatsu-wa-kimi-no-uso.fandom.com/api.php`), en inglés: páginas «Music», «Hikaru Nara», «Nanairo Symphony», «Kirameki», «Orange», «Episode 03: Inside Spring» (`action=parse&prop=wikitext`) y búsqueda de texto («Ballade», «Kreutzer») para confirmar temas e insertos musicales.
- `herramientas/estilo.py` sobre 6 fotogramas propios en 1080p para los hex de sitios (punto 4).
- WebSearch (2 búsquedas): «"Your Lie in April" tiktok trend edit viral sound», «"Your Lie in April" ending scene reaction youtube analysis video minute» → confirmaron el formato de tendencia y que el final es lo más reaccionado.
- `herramientas/navegar.py` sobre `tiktok.com/discover/…`: falló (navegador de Playwright no instalado, ver «No encontré»).
- Retratos de AniList (ya en `datos.json`) para verificar de qué personaje es cada fotograma (pelo y gafas), antes de rellenar la tabla de poses.

### Segunda pasada (relanzo por pocas webs distintas: sólo 3 enlazadas)

- `graphql.anilist.co` (POST directo, sin buscador): pedí `idMal` y `externalLinks` del media 20665 para tener el id real de MyAnimeList (23273) y el enlace oficial `kimiuso.jp` con URL exacta.
- `myanimelist.net/anime/23273` con `navegar.py` (sí carga, sin login): ficha completa, sinopsis, puesto de popularidad y **reparto de voces japonés** → descubrí que había leído mal dos nombres del PV (Kaori no es «Oda Risa» sino Risa Taneda; Watari no es «Aisaka Ryouta» sino Ryouta Oosaka), corregido en el punto 2.
- `en.wikipedia.org/wiki/Your_Lie_in_April` con `navegar.py --selector '#mw-content-text' --max 0` (la API `action=query` de Wikipedia dio «too many requests» varias veces, cambié a navegar.py): sección «Production» con la razón del director para elegir cada banda de OP/ED, y sección de emisión con fechas exactas. También `--html` para sacar los `href` reales de las dos noticias de Anime News Network citadas.
- `animenewsnetwork.com` (las dos URLs de la nota anterior, directas y vía `web.archive.org`): 403 «security check» (captcha) en todos los intentos, incluso con `navegar.py`; me quedé con el título de cada noticia (visible en el propio enlace de Wikipedia) como confirmación parcial.
- `www.kimiuso.jp` con `navegar.py`: sitio oficial japonés, sigue actualizado (anuncio de figura de Kaori, feb-2025).
- `www.tiktok.com/tag/yourlieinapril` con `navegar.py --espera 6000` (funcionó, a diferencia del intento anterior): listado real de vídeos con autor y descripción, sin buscador.
- `musicbrainz.org`: reutilicé los 3 discos ya recolectados en `datos-video.md` y los enlacé directamente en el punto 9 (antes sólo se mencionaban, no estaban citados como enlace).
- YouTube (los 2 vídeos de reacción del punto 10) con `navegar.py`: 429 «tráfico inusual» en los dos, igual que antes.

### Tercera pasada (relanzo puntual: completar poses de Watari y Tsubaki)

- Wiki de Fandom, wikitext de «Episode 09: Resonance», «Episode 11: Light of Life», «Episode 13: Love's Sorrow», «Episode 14: Footsteps», «Episode 15: Liar», «Episode 16: Two of a Kind», «Episode 17: Twilight», «Episode 18: Hearts Come Together» y «Episode 19: Goodbye, Hero» (`action=parse&prop=wikitext`, filtrando líneas con «Watari»/«Tsubaki») para saber en qué episodios tienen escena propia antes de sacar fotogramas a ciegas.
- `ffmpeg -ss <segundo> -i "https://archive.org/download/EVYourLieinApril/<ep>.mp4"` (mismo método que tandas anteriores). Esta vez archive.org devolvía **403** al pedir el `.mp4` directo con ffmpeg sin más: hacía falta pasarle el proxy de este contenedor explícito (`-http_proxy "http://127.0.0.1:33635"`, tomado de la variable de entorno `HTTPS_PROXY`) además de `-user_agent`; con eso funcionó igual que antes. Lo anoto por si otro investigador de esta serie se topa con el mismo 403.
- Para explorar tramos largos sin gastar una llamada por minuto usé `ffmpeg -vf "fps=1/90"` sobre 600-1300 s seguidos de una sola vez (contact sheet con Pillow), y sólo pedí en grande el fotograma que servía.
- Encontradas y confirmadas: Watari en Ep. 17 «Twilight» (min 8:55-9:10, confesión sobre Kaori, diálogo coincide palabra por palabra con la cita de la wiki) y en Ep. 11 «Light of Life» (min 9:00, tablón de resultados, identificado por pelo castaño-naranja y ropa ya usadas en otras poses); Tsubaki en Ep. 14 «Footsteps» (min 20:00, escena de la playa que cita la propia wiki del episodio) y en Ep. 19 «Goodbye, Hero» (min ~19:30, pasillo del hospital con Takeshi y Kousei).
- Episodios revisados sin pose nueva aprovechable de ninguno de los dos: 9, 12, 13, 15, 16 (ver «No encontré»).

### Bitácora de voz

- AniList (`anilist.co/anime/20665`): favoritos por personaje y fichas — ya venía en `datos-voz.md`, verificado y ampliado.
- Doblaje Wiki (`doblaje.fandom.com/es/api.php?action=parse`): wikitext completo de la ficha de la serie — descargado directamente con curl, sacó el reparto que `datos-voz.md` no había parseado bien (tabla vacía → reparto completo con personaje-actor).
- Shigatsu wa Kimi no Uso Wiki (Fandom, `api.php?action=parse`): wikitext de Kousei Arima, Kaori Miyazono, Tsubaki Sawabe y Ryota Watari (infobox, personalidad, apariencia, relaciones, trivia, episodio 22).
- Wikipedia ES (`es.wikipedia.org/wiki/Shigatsu_wa_Kimi_no_Uso`): sección de reparto de doblaje por personaje e idioma — segunda fuente independiente para los 4 actores latinos.
- Wikipedia EN (`en.wikipedia.org/wiki/Your_Lie_in_April`, `en.wikipedia.org/wiki/Naoshi_Arakawa`): premios y ventas.
- kimiuso.jp/character/: sitio oficial revisado con curl; sin texto de fichas (usa imágenes), sin encuesta.
- eldoblaje.com: ficha de España (no Latinoamérica) con id capturado por recolectar.py da 404; descartado.
- MyAnimeList / Jikan API (`api.jikan.moe/v4/anime/23273/characters`): 504 repetido, sin datos.
- Internet Archive (`archive.org/advancedsearch.php`, `archive.org/metadata/...`): busqué «your lie in april» / «shigatsu wa kimi no uso»; encontré y usé el episodio 1 completo BDRip (`lns-tsundere-shigatsu-wa-kimi-no-uso-01-...`) con `fotogramas.py` (hojas de contacto cada 20 s + 5 fotogramas individuales en detalle), y también la colección `EVYourLieinApril` (serie completa, 22 episodios + OVA): vi el episodio 22 completo entre el min. 15:30 y 21:22 (la escena de la carta) con fotogramas cada 8 s. Borré los `video.mp4` bajados al terminar de mirarlos (disco compartido).
- Dailymotion (API, `datos-voz.md`): probé un AMV (`x479c6d`) con `fotogramas.py` como plan B; sirvió para confirmar estilo visual pero no lo usé para las citas finales (el episodio 1 de Internet Archive da capítulo y minuto reales, el AMV no).
- yt-dlp (metadatos, `--skip-download --print`): usado para sacar título, canal, vistas y fecha de 8 vídeos de YouTube (fandubs y covers en español) sin descargar nada; funciona aunque la descarga de vídeo esté bloqueada por «inicia sesión».
- navegar.py: falló con «BrowserType.launch: Executable doesn't exist» — el navegador headless no está instalado en este contenedor. Anotado como fallo de entorno, no de la web.
- Arctic Shift (Reddit, `arctic-shift.photon-reddit.com/api/posts/search`): 3 intentos, todos con timeout. Descartado, usé búsqueda web para contenido de Reddit/foros en su lugar.
- Búsquedas web (WebSearch), en español, inglés y japonés: «Your Lie in April doblaje latino», «ANMTV Your Lie in April Crunchyroll», «Your Lie in April reparto voces latino», «anmtvla.com Your Lie in April reparto doblaje 2026», «Your Lie in April Newtype character popularity poll», «Your Lie in April personaje más querido encuesta MyAnimeList», «四月は君の嘘 キャラクター人気投票» (japonés), «Your Lie in April fandom memes running gag», «Your Lie in April reddit best crying scene», «Your Lie in April qué NO hacer fans odian adaptación», «Your Lie in April running joke comedic violence», «Your Lie in April awards sales Kodansha Manga Award», «Your Lie in April episode 22 letter scene reaction», «Your Lie in April episode 22 letter scene song Watashi no Uso», «Your Lie in April Tsubaki confession episode number», «Your Lie in April fandub español latino YouTube», «Hikaru Nara cover español latino».

### Bitácora de texto

- Fandom `shigatsu-wa-kimi-no-uso.fandom.com`, API `api.php` (allpages,
  allcategories, categorymembers, parse&prop=wikitext): páginas de
  competencias, localizaciones, objetos, piezas musicales, temas de
  apertura/cierre. Sin bloqueo.
- AniList (`datos-texto.md`, ya recolectado): ficha, equipo creativo, obras
  recomendadas — no repetido.
- WebSearch (idioma inglés): "Your Lie in April" A-1 Pictures 3DCG piano
  hands animation interview · Kyohei Ishiguro director interview visual
  style flowers light · Your Lie in April flower petals visual metaphor
  performance scenes analysis · site:tvtropes.org Your Lie in April YMMV ·
  site:tcrf.net Your Lie in April · "Your Lie in April" OR "Shigatsu wa Kimi
  no Uso" game app mobile · "Your Lie in April" logo font identify title ·
  Your Lie in April Kaori letter handwritten scene final episode · A-1
  Pictures animation software RETAS Toon Boom Photoshop compositing pipeline
  2014 · Graphinica "Your Lie in April" piano 3DCG.
- WebSearch (idioma japonés): 四月は君の嘘 ゲーム アプリ · 四月は君の嘘
  アニメ 制作 CG 手 ピアノ インタビュー · 四月は君の嘘 石黒恭平 演出
  インタビュー 色.
- Sitio oficial `kimiuso.jp/special/`: reportes de producción semanales
  (`04.html`) y entrevistas al staff (`05_01.html` director Ishiguro,
  `05_05.html` autor Arakawa) — leídos completos con `curl`, en japonés, no
  traducidos antes al español en ninguna fuente encontrada.
- `animeherald.com`: transcripción de charla en Anime Boston 2016 con
  Ishiguro y Aikei — leída completa con `curl`.
- TV Tropes (`tvtropes.org`) bloquea `curl`/`WebFetch` con 403. Arreglado
  `herramientas/navegar.py` para esta sesión: el Chromium instalado está en
  `/opt/pw-browsers/chromium_headless_shell-1194/...` (no
  `-1243`, que es lo que el script trae por defecto) y hacía falta
  `ignore_https_errors=True` en el contexto de Playwright porque el proxy
  reemplaza el certificado TLS. Con `PLAYWRIGHT_CHROMIUM` apuntando a la
  build correcta sí funcionó, dos páginas leídas completas (Manga y Trivia).
- Internet Archive: el volumen 1 del manga está indexado pero es préstamo
  con DRM, no legible sin pedirlo prestado — no se insistió.
- `fontTools` (`TTFont(f).getBestCmap()`) sobre 8 fuentes bajadas de
  `raw.githubusercontent.com/google/fonts`: Zen Maru Gothic, Shippori
  Mincho, M PLUS 1p, M PLUS Rounded 1c, Bungee, Comfortaa, Caveat, Noto
  Sans, Anton, Yomogi — las 10 con á, ñ, ¿, ¡. (Permanent Marker no se pudo
  bajar del repo, no crítico: no se usó como recomendación final.)
- Fuentes que fallaron sin insistir más de dos intentos: `tcrf.net` directo
  (Cloudflare); Wikipedia `pageimages` API (sin respuesta útil, se resolvió
  extrayendo el `<img>` del HTML de la página en su lugar); Wayback Machine
  (`web.archive.org/cdx/search/cdx`) — el túnel del proxy se cerró a medio
  intercambio en dos intentos (`ws_closed_mid_exchange`, ver
  `__agentproxy/status`), parece un fallo transitorio del lado de Internet
  Archive en este momento, no del proxy. No hizo falta insistir más: ninguno
  de mis puntos tenía una página borrada específica que recuperar (no hay
  videojuego ni sitio de franquicia desaparecido que rastrear).
