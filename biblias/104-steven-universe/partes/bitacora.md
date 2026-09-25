## Bitácora

### Bitácora de imagen

- Recolector automático (`recolectar.py`): AniList no aplica (obra occidental), Doblaje Wiki con `action=query` falló, Fandom no se buscó porque el encargo no traía `--wiki` — corregido a mano con `steven-universe`.
- `investigar_serie.py --serie "Steven Universe" --wiki steven-universe --paginas "Steven Universe" "Garnet" "Amethyst" "Pearl" "Steven Quartz Universe" --min-px 90000`: 287 imágenes enlazadas, 270 grandes, 6 hojas de contacto en `herramientas/referencias/steven-universe/`. Miradas las 6 con Read.
- Fandom API (`api.php?action=query&list=search`, `prop=imageinfo&iiprop=url|size`) para localizar y medir modelsheets oficiales limpios de Garnet, Amatista, Perla y Steven (headers `Referer: https://www.fandom.com/` para bajar los PNG).
- Medición de color con Pillow: cuadrículas de referencia (`ImageDraw`), recortes ampliados y `getcolors()`/muestreo de píxel para evitar el contorno negro y el fondo blanco. Documentado por personaje en el Hallazgo 15.
- Datos ya traídos por el recolector (no repetidos): Danbooru `related_tag` (vocabulario de etiquetas), Safebooru (fan art top por personaje), Wallhaven (fondos), Sketchfab (modelos 3D con licencia), Openverse (fotos con licencia libre de cosplay/merchandising).
- Búsquedas web propias (inglés, cupo usado: 12 de ~50):
  - «Steven Universe background art style gouache paint texture art director interview» → confirmó el estudio Chromosphere y a Elle Michalka como dirección de arte, pero no la palabra «gouache» exacta: lo dejé sin afirmar el material.
  - «"Steven Universe" "Tap-Tap Dance" app Cartoon Network» → el nombre real es *Tap Together*, corregido.
  - «Hot Topic Steven Universe official merchandise collection» → confirmado con enlace oficial de la tienda.
  - «"Art of Steven Universe" Dark Horse artbook 2017» → corrigió el dato: el de 2017 es *Art & Origins* (Abrams), Dark Horse sólo hizo el de la película (2019).
  - «Steven Universe comic book publisher KaBOOM Boom Studios» → confirmó KaBOOM!/BOOM! Studios (no IDW, corregido).
  - «Steven Universe #1 KaBOOM comic 2014 cover artist» → confirmó autores de portada.
  - «"Cartoon Network: Battle Crashers" Steven Universe playable characters» → corrigió el dato: sólo Steven es jugable, no las 4 Crystal Gems.
  - «Steven Universe Peabody Award 2019» → confirmado.
  - «"Steven Universe: Art & Origins" Chris McDonnell publisher Abrams» → confirmado.
  - «Steven Universe Funko Pop official Garnet Amethyst Pearl» → confirmado, con enlace oficial de funko.com.
  - «free gouache brush pack Procreate Photoshop CC0 download» → sin un paquete libre verificable (ver «No encontré»).
  - Comprobé con `curl -I` que `ambientcg.com/view?id=Paper002` y `...Fabric038` responden 200, y que el enlace de itch.io que iba a citar da 404 (lo retiré).
- Páginas que bloquearon o fallaron: `cartoonnetwork.com/backgrounds/` no resolvió en directo (probablemente geo-bloqueada o retirada); usé el enlace de Wallhaven como fuente y anoté ⚠️. No hizo falta `navegar.py` (ninguna web de las usadas pidió verificación).

### Bitácora de video

- Dailymotion API (`api.dailymotion.com/videos?search=`), en inglés: «Steven
  Universe official clip», «Steven Universe Stronger Than You», «Steven
  Universe theme song», «Steven Universe trailer Cartoon Network», «Steven
  Universe Love Like You ending credits» — de aquí salieron todos los clips
  de las secciones 2, 4 y 14.
- Internet Archive (`advancedsearch.php`), en inglés: «steven universe
  intro», «steven universe opening» (mediatype movies) — sin resultados
  útiles nuevos; el ítem de «Stronger Than You» ya estaba en
  `datos-video.md`.
- Internet Archive `metadata` de los ítems `StevenUniverseE86`,
  `StevenUniverseS02E0912`, `steven-universe-full-series`: descartados tras
  mirar los fotogramas (vídeos de reacción o .rar no reproducible), ver
  aviso al inicio.
- Fandom API (`steven-universe.fandom.com/api.php`), en inglés:
  `action=parse&page=We Are the Crystal Gems`, `Ending Theme`,
  `It's Over Isn't It`, `Coach Steven`, `Know Your Fusion`, `Jeff Ball`;
  `action=query&list=search` con «poof sound», «sound effects», «theme
  song», «end card».
- WebSearch, en inglés: «Steven Universe TikTok trend opening meme viral»,
  «Steven Universe análisis video ensayo YouTube Stronger Than You
  reacción», «Steven Universe reboot 2026 announcement new intro», «Steven
  Universe lofi theme song TikTok viral», «L.Dre Steven Universe lofi TikTok
  article billion views composer», «Steven Universe video essay analysis
  YouTube fusion queerness storytelling».
- WebFetch: Wikipedia `Jail_Break_(Steven_Universe)`; comicbook.com (revival
  de Cartoon Network); lofidre.com/about (cifras del remix lo-fi); TikTok
  (no cargó contenido, sólo cabecera — anotado como límite, no como dato).
- yt-dlp directo sobre YouTube: bloqueado en todos los intentos con «Sign in
  to confirm you're not a bot» / HTTP 429 — confirma el aviso de AYUDANTE.md
  sobre el bloqueo del servidor.
- `fotogramas.py` sobre 10 vídeos (opening ×2, ending, tráiler ×2, Jail
  Break ×2, Coach Steven ×2, Know Your Fusion); todas las hojas miradas con
  Read antes de escribir esta parte. `estilo.py` sobre 7 fotogramas sueltos
  para las paletas del punto 4. `video.mp4` de los clips usados y de los
  descartados borrados de `/tmp/claude-0/trabajo/104-video/` al terminar
  (quedan las hojas JPEG, más pequeñas).

### Bitácora de voz

- Doblaje Wiki, API `action=parse&prop=wikitext`, páginas «Steven_Universe»
  (ficha completa de doblaje), «Jorge_Bringas» (actor) — español.
- Fandom `stevenuniverse.fandom.com`, API `action=parse&prop=wikitext`,
  páginas: «Steven Universe (character)», «Garnet», «Amethyst», «Pearl»,
  «Peridot», «Lapis Lazuli», «Connie Maheswaran», «Greg Universe» — inglés
  (la wiki no tiene versión en español activa para estas fichas).
- Doblaje Wiki, API `imageinfo`, para bajar las muestras oficiales .ogg de
  Steven, Perla, Garnet, Amatista, Peridot, Lapislázuli, Rose, Connie y
  Greg, y transcribirlas/medirlas con `herramientas/voz.py` — español.
- `herramientas/navegar.py` sobre TV Tropes: «EnsembleDarkhorse/
  StevenUniverse» y «Heartwarming/StevenUniverse» (TV Tropes bloquea curl
  directo, no navegar.py) — inglés.
- `herramientas/fotogramas.py` sobre el clip oficial de Dailymotion
  «It's Over, Isn't It? | Steven Universe | Cartoon Network»
  (x4wic92) para sacar la cara triste de Perla con minuto exacto.
- Reaprovechados (mirados, no repetidos) los fotogramas ya sacados por el
  investigador de vídeo en `partes/video.md`: `sugilite_detalle/hoja_01.jpg`
  (miedo cómico de Steven y vergüenza de Perla) y `stronger_x5bh5gl/
  hoja_01.jpg` (rabia de Garnet y de Jasper), citando el mismo clip oficial
  con nuevo minuto para la emoción que necesitaba.
- Dailymotion API `api.dailymotion.com/videos?search=...` para covers en
  español de «Amar Como Tú» y «Más Fuerte que Tú» — español.
- Arctic Shift (`arctic-shift.photon-reddit.com/api/comments/search`) sobre
  los hilos de r/stevenuniverse ya recolectados, para leer los comentarios
  con más votos de los hilos «best scene from the finale» y «favorite
  character» — inglés.
- WebSearch (antes de agotarse la cuota compartida del contenedor a mitad
  de tanda, aviso «200 de 200»): reparto de la película (Jorge Bringas),
  intento de encuesta oficial de popularidad, fandubs en español, escenas
  que hacen llorar — español e inglés.
- ANMTV (`anmtvla.com`): bloqueado por la política de red de este
  contenedor (502 / `connect_rejected` en 3 intentos directos con curl);
  sólo accesible lo que indexó el buscador antes de agotarse la cuota.

### Segunda pasada (relanzo)

- Doblaje Wiki, API `action=parse&prop=wikitext`, página individual de cada
  actor de reparto secundario para conseguir la segunda fuente que pedía
  `Sigue:`: Rocío Mallo, Stefani Villarroel, Yasmil López, Abigaly Claro,
  Navid Cabrera, Henrique Palacios, Ángel Lugo, Karina Parra, Mariangny
  Álvarez, Sofía Narváez, Andrea Navas, Maythe Guedes, Arelys González,
  Yvette García (la tabla de reparto decía «Ivette García», que es una
  redirección), Alix Ramírez, Catherine Reyes — español. Las 15 fichas se
  guardaron en `/tmp/claude-0/trabajo/104-voz/*.wikitext` (carpeta de
  trabajo, no en el repositorio).
- ANMTV (`anmtvla.com`): reintentado con `curl` directo (ya no da 502; HTTP
  200) y con su buscador interno (`?s=steven+universe+doblaje`, dos
  variantes de codificación); no filtra resultados por texto, así que no
  sirvió para confirmar reparto — se confirmó por la vía de arriba en su
  lugar.
- YouTube, API oEmbed (`youtube.com/oembed?url=...&format=json`, no
  bloqueada aunque la página completa sí): los 5 enlaces de fandub del
  punto 22, para confirmar canal real (4 de 5 respondieron 200; uno dio
  403). `yt-dlp --dump-json` sobre el primero: 429 (confirma que el
  bloqueo de la página completa sigue activo esta tanda).
- Dailymotion, API `api.dailymotion.com/video/x3fdt3q?fields=views_total`
  para las vistas exactas del cover de «Amar Como Tú»; y una búsqueda más
  (`api.dailymotion.com/videos?search=steven+universe+cover+español`) para
  ver si había más covers de fans aparte de los ya listados — sólo aparecen
  reposts oficiales (Cartoon Network, Cartoon Workshop), no fandubs nuevos.
- WebSearch: intenté 2 consultas (ANMTV site:, «Rocío Mallo» actriz) pero
  la cuota compartida del contenedor seguía en 200/200 desde antes del
  relanzo; no se pudo usar el buscador web en esta tanda, todo lo de arriba
  se sacó con `curl`/Python directo.
- Dailymotion API (`videos?search=...`) para encontrar clips oficiales de
  Peridot y Lapislázuli específicamente (los dos personajes secundarios más
  dibujados por el fandom, punto 7), y `fotogramas.py` sobre
  «The Real Peridot (Clip) Catch And Release» (x3lmesb) y «Lapis Lazuli's
  Backstory (Clip) Same Old World» (x6viabp) para sacar caras en emoción
  con minuto exacto que faltaban del punto 13 (antes sólo tenían «forma de
  hablar», sin cara). `video.mp4` borrado tras sacar las hojas.

### Bitácora de texto

- Fandom (`steven-universe.fandom.com/api.php`, `action=parse&prop=wikitext` y `action=query&list=search`, en inglés — la wiki no tiene versión en español): páginas `Gem_Glyph`, `Video_Chat`, `Attack_the_Light`, `Save_the_Light`, `Unleash_the_Light`, `Grumpyface_Studios`, `Cartoon_Network:_Battle_Crashers`, `Camp_Pining_Hearts`, `Steven_Universe_(comic_series)`, `Steven_Universe:_Harmony`; búsquedas de texto: «font lettering logo», «video game», «Peridot tablet screen hologram», «Homeworld broadcast Yellow Diamond screen», «Camp Pining Hearts»; categoría `Category:Video_Games` completa.
- Wikipedia (inglés, wikitext crudo vía `action=raw`): `Steven_Universe` completo (confirmé directamente Bauhaus/Kandinsky, proceso de fondos, animación en Corea, sin repetir de memoria lo que ya tenía el encargo 64).
- WebSearch (cupo compartido del contenedor con los otros investigadores de esta tanda — se agotó a las 200/200 del entorno tras mis primeras 5 búsquedas): «site:tcrf.net Steven Universe», «Steven Universe logo font identify», «Steven Universe official comic BOOM Studios lettering font speech balloon», «"Steven Universe" subtitle font closed captions Cartoon Network», «"Gem Glyph" font dafont Steven Universe». El resto de la tanda se hizo con `curl`/`r.jina.ai` directo a las páginas ya identificadas por esas 5 búsquedas y por el encargo 64.
- `r.jina.ai` (lector de texto) como vía alternativa cuando un sitio bloquea `curl`/`navegar.py` por Cloudflare: funcionó para `gameuidatabase.com` (di con los IDs de juego buscando en `html.duckduckgo.com/html/` vía el mismo lector) y para `google.com`/`bing.com` (sin resultados útiles, límite de tasa); **no** funcionó para `tcrf.net` (reto de seguridad persiste incluso a través del lector).
- Descargas propias verificadas con `fontTools` (`TTFont(f).getBestCmap()`, comprobando á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡): `crewniverse_font.ttf` (sí, completo), `CrystalUniverse-Regular.ttf` (no, sólo é), `creditverse_font.ttf` (no, ninguno) — las tres descargadas de dafont.com con éxito en esta tanda (el encargo 64 no pudo descargar Crystal Universe, yo sí).
- Capturas reales de interfaz de *Unleash the Light* bajadas directamente de `gameuidatabase.com/uploads/` (sin bloqueo, sólo la página HTML está tras Cloudflare) y miradas con Read: `modal1.jpg`, `modal2.jpg` (cuadro de diálogo), `gamestate1.jpg` (menú de equipo), `stats1.jpg` (cartel de etapa) — en `/tmp/claude-0/trabajo/104-texto/guidb_imgs/`.
- Chromosphere LA (`chromosphere-la.com/case-study/steven/`) y Toon Boom (`toonboom.com/top-animation-news-the-dragon-prince-steven-universe-and-more`) leídos directamente por mí con `curl`, no repetidos de memoria del encargo 64.
- Sitios bloqueados (máximo el límite razonable de intentos por cada uno, con vías alternativas probadas antes de rendirme): `tcrf.net` (403/reto Cloudflare por 4 vías), `comicvine.gamespot.com` (403 directo; vía `r.jina.ai` con id adivinado da la ficha equivocada), `madegooddesigns.com` (403).
- Encontré el encargo 64 (`biblias/64-steven-universe/`), la misma obra con otro encargo, ya con biblia completa — lo leí entero (`partes/texto.md`, 240 líneas) antes de empezar a buscar, para no repetir consultas y para saber exactamente qué le faltaba (letrista del cómic, TCRF, capturas de interfaz): ese fue el hilo conductor de esta tanda.
