## Bitácora

### Bitácora de imagen

- `herramientas/investigar_serie.py --paginas "Taro Sakamoto" "Shin Asakura" "Lu Wutang" "Yoichi Nagumo" "Osaragi"` (wiki sakamoto-days.fandom.com, inglés): 162 imágenes enlazadas, 149 grandes, 4 hojas de contacto generadas; se eligieron las hojas 1-3 (personajes, portadas WSJ, tomos, arte de acción) para `hojas/`, se descartó la 4 (5 portadas repetidas y pequeñas)
- `herramientas/estilo.py --colores 10` sobre 7 imágenes oficiales de hoja de modelo (Sakamoto ×2, Shin ×2, Lu, Osaragi, Nagumo), descargadas con `curl` (cabecera `Referer: https://www.fandom.com/`) y miradas con Read para asignar cada hex a su prenda a mano
- API de Sketchfab v3 (`search?type=models&q=...&downloadable=true`) con 5 consultas distintas: sólo 3 modelos 3D de la serie existen, con su licencia y autor confirmados
- API de Fandom (`api.php`, `list=categorymembers` y `list=search&srwhat=text`) para la lista de localizaciones y para comprobar que «The Order» no tiene emblema
- API de ambientCG v2 (`full_json`) para texturas CC0: Paper001/004 (papel) y Fabric030/036 (tela lisa)
- WebSearch (inglés) ×6: fondos de pantalla 4K, pinceles de screentone libres, repositorios GitHub de halftone con licencia, patrones CC0 (freesvg.org), colaboraciones/cafés (collabo-cafe.com, essential-japan.com, sweets-paradise.jp), figuras Ichiban Kuji, ropa Uniqlo UT, crossovers con juegos
- `curl` directo a `collabo-cafe.com/events/category/sakamoto-days/` y a `freesvg.org`, `4kwallpapers.com`/`wall.alphacoders.com` para confirmar tamaños de imagen reales
- Datos ya reunidos por `recolectar.py` (AniList, Fandom, Danbooru, Safebooru, Wallhaven, Sketchfab, Openverse) comprobados y ampliados, no repetidos: ver `datos-imagen.md`

### Bitácora de video

- AnimeThemes API (`api.animethemes.moe`): 522, dos veces (recolectar.py y yo)
  → descartada.
- Internet Archive: `advancedsearch.php` para OP1, Part2-OP1, «sakamoto days
  ED», «sakamoto days ending» (inglés) → 2 vídeos de OP útiles, 0 de ED.
- Dailymotion API (`api.dailymotion.com/videos?search=`): 14 búsquedas en
  inglés/francés («Sakamoto Days opening/ending/trailer/fight scene/best
  scenes/Lu Wutang/Shin ability/Futsu Conton Candy/普通 SAKAMOTO DAYS»…) →
  encontrados 1 opening completo, 2 tráileres oficiales y 1 escena real de
  ep.1; el resto eran repeticiones del mismo tráiler o vídeos ajenos a la
  serie (descartados tras comprobar el contenido con `fotogramas.py`, p. ej.
  «Sakamoto day best fight scene» de Gauravnews no es esta obra).
- Fandom `sakamoto-days.fandom.com/api.php`: búsqueda de texto «opening theme»
  y «ending theme» (inglés) → páginas Hashire Sakamoto, Futsū, Somebody help
  us, Method; wikitext de las 4 con `action=parse`; página «Episode 1» para
  confirmar la escena.
- AniList GraphQL (`graphql.anilist.co`): formato, episodios, duración.
- Wikipedia (`en.wikipedia.org/w/api.php`): extracto de «Sakamoto Days» para
  compositor, estudio, dirección y fechas de emisión (segunda fuente de la
  música y la ficha técnica).
- MusicBrainz (de `datos-video.md`): filtrado a mano; sólo 4 de 14 resultados
  eran de esta serie (el resto, ruido por el título genérico «Days»).
- `navegar.py` sobre `tiktok.com/discover/shin-sonic-sway-sakamoto-days` →
  200 pero 0 caracteres (JS), no reintentado (regla de 2 intentos).
- Buscador web (2 búsquedas, inglés): «Sakamoto Days TikTok trend viral clip
  2025», «Sakamoto Days anime analysis video YouTube minute».
- `fotogramas.py`: opening (archive.org), tráiler y tráiler parte 2 y escena
  de ep.1 (Dailymotion), cada uno con hoja de contacto mirada con `Read`.
- `ffmpeg` + Pillow (`quantize`) sobre los mismos `video.mp4` ya descargados,
  para los hex de 6 sitios/escenas.
- `yt-dlp -F` sobre el ítem de archive.org del OP1, para confirmar que 720p es
  el techo real (no hay pista de 1080p).
- `navegar.py` sobre TV Tropes (`Anime/SakamotoDays`, inglés): confirma «golden
  rule of not taking a single life» y la «Hitman Association»; no encontré ahí
  ninguna entrada sobre onomatopeyas o efectos de sonido reconocidos (puede
  seguir más abajo de lo que cargó la herramienta; no insistí más de una vez).

### Bitácora de voz

- Doblaje Wiki, API `action=parse&prop=wikitext`, páginas: «Sakamoto Days», «Óscar López»,
  «Geezuz González», «Irene Ponce», «Angélica Villa», «Bruno Coronel», «Stephanie Filigrana»,
  «Emmanuel Alejandro», «Armando Guerrero», «Héctor Estrada (México)», búsqueda `list=search`
  para resolver nombres con tilde. Español.
- `sakamoto-days.fandom.com` (wiki oficial en inglés), API `action=parse&prop=wikitext`,
  páginas: «Popularity Polls», «Taro Sakamoto», «Shin Asakura», «Lu Shaotang», «Yoichi
  Nagumo». Inglés.
- `navegar.py` sobre TV Tropes: YMMV, Funny y Heartwarming de «SakamotoDays» (TearJerker no
  existe como página propia, da 404 con lista de alternativas). Inglés.
- `navegar.py` sobre Behind The Voice Actors (reparto en inglés, no latino — no usado en la
  tabla del punto 8) e intento sobre okamisamatv.com (sin datos de Nagumo). Inglés/español.
- WebSearch (13 búsquedas): doblaje ANMTV, encuestas de popularidad en Japón, reparto de
  secundarios, sales/streaming de Netflix, fandubs y memes hispanos, entrevista de Óscar López.
  Español e inglés.
- Dailymotion API `api.dailymotion.com/videos?search=`: tráilers oficiales en español latino y
  portugués (para fotogramas). `voz.py` transcribió el tráiler oficial en español (x9a858e,
  108 s) y uno que resultó ser en portugués (x9c2low, descartado para citas de texto pero
  usado para fotogramas visuales). `fotogramas.py --cortes` sobre ambos, 68 + 84 fotogramas
  vistos con Read.
- YouTube: sólo `oembed` (título/canal, sin necesitar sesión) para confirmar canales de
  reacción al doblaje y entrevistas; no se abrieron los vídeos en sí (bloqueado en esta
  máquina, según el aviso de arranque).
- ComicBook.com y AnimeCorner/GameRant/ScreenRant/CBR (vía WebSearch) para cifras de ventas y
  streaming; Anime News Network bloqueó con captcha incluso con `navegar.py`.

### Bitácora de texto

- Wiki de Fandom `sakamoto-days.fandom.com` por su `api.php` (búsqueda de texto y wikitext completo):
  Order, Japanese Association of Assassins, X's Organization, Japan Clear Creation, Story Arcs, Sakamoto's
  Store, logo del sitio · sin bloqueo
- `WebSearch` en inglés: «Sakamoto Days logo font», «Sakamoto Days font dafont», «Yuto Suzuki interview
  drawing process Clip Studio Paint», «Sakamoto Days anime animation style interview director», «Sakamoto
  Days video game mobile app Goodroid», «Yuto Suzuki interview influences Domu Otomo»
- `WebSearch` en japonés: «サカモトデイズ 鈴木祐斗 インタビュー 作画 画材», «サカモトデイズ 実写映画 目黒蓮
  福田雄一 2026年4月29日»
- `navegar.py` (funciona en esta máquina): TV Tropes (`Manga/SakamotoDays`, 200 OK), Animation Magazine
  (403/error de navegación, descartado), AWN (200 OK), `tcrf.net` (403, Cloudflare, dos intentos),
  Google Play (200 OK, con `--captura` para ver capturas del juego)
- `curl` directo: `mangaplus.shueisha.co.jp` (entrevista completa), `mediadogs.jp` (perfil en japonés),
  `animationmagazine.net` (403 CloudFront, no se insistió), `tcrf.net` (403 Cloudflare)
- fontTools (`getBestCmap()`) sobre 8 fuentes de Google Fonts/Fontsource bajadas con `curl` (subset
  `latin`, que es el que trae á/é/í/ó/ú/ñ/¿/¡, no `latin-ext`): Anton, Bangers, Archivo Black, Caveat,
  Press Start 2P, IBM Plex Mono, Titan One, Patrick Hand — las 8 con todos los caracteres
- Pillow: medidos los hex de la caja de diálogo y la pantalla de equipo del videojuego móvil
  (`playshots/*.jpg`, capturas propias de Google Play)
- Imágenes miradas con Read: `ch1_small.jpg`, `ch2_small.jpg`, `ch43_small.jpg`, `vol9_small.jpg`,
  `sitelogo_conv.png`, `playstore.png`, `playshots/sheet1.jpg` (todas en mi carpeta de trabajo temporal)
