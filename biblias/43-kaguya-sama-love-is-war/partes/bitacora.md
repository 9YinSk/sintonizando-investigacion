## Bitácora

### Bitácora de imagen

- AniList (`https://anilist.co/anime/101921`): portada, banner y 15 retratos de personajes — ya
  recolectado por `recolectar.py`, sólo comprobado.
- Fandom `kaguyasama-wa-kokurasetai.fandom.com` vía API (`action=query&prop=pageimages&piprop=original`):
  hojas de modelo de cuerpo entero de Kaguya, Miyuki, Chika, Ishigami, Hayasaka e Iino — usadas para
  medir hex del punto 15. También `action=parse&prop=wikitext&page=Crossovers` para el punto 23 (es/en).
- `investigar_serie.py` (ya corrido antes de esta tanda): 157 imágenes de la wiki → 3 hojas de
  contacto en `hojas/`, revisadas en detalle imagen por imagen para los puntos 1 y 15.
- Openverse (`api.openverse.org`): `kaguya-sama cosplay` → 6 resultados, 5 de Flickr (CC BY-NC-SA) y 1
  de Wikimedia Commons (CC BY-SA), en inglés.
- Sketchfab (`api.sketchfab.com/v3/search`): `kaguya-sama`, `kaguya shinomiya`, `school uniform anime
  girl` (en) → 5 modelos de personajes/escena con licencia CC-BY confirmada modelo por modelo.
- Wallhaven (`wallhaven.cc/api/v1/search`): `kaguya-sama`, `atleast=1920x1080`, `purity=100` (sfw) →
  12 resultados, se verificaron 4 con la API de detalle (`/api/v1/w/<id>`) para confirmar purity y tamaño.
- ambientCG (`ambientcg.com/api/v2`): `marble floor`, `wood floor dark`, `wool fabric`, `paper`, `red
  carpet` (en) → 4 texturas CC0 elegidas para los puntos 16 y 19.
- Poly Haven (`api.polyhaven.com/assets?t=hdris`): filtro por «class/school/library/hall» (en) → HDRI
  «Entrance Hall» elegido para el punto 16.
- WebSearch (en y es): colaboraciones (café/tienda, Bilibili/juegos, Oshi no Ko), screentones libres,
  artbook/Blu-ray, figuras oficiales — 6 búsquedas, resultados usados en los puntos 1 y 23.
- Danbooru (`donmai.us/posts.json`): bloqueado por reto de Cloudflare (403) — descartado, no reintenté
  una tercera vez.
- Colores hex del punto 15: medidos con Pillow (`Image.getcolors` sobre recortes RGBA, descartando
  fondo transparente) directamente sobre las 6 hojas de modelo oficiales del anime descargadas de la
  wiki — no son una estimación visual, son el promedio del color de relleno más repetido en cada zona.

### Bitácora de video

- Recolector (`datos-video.md`): AniList (tráiler, enlaces oficiales), Dailymotion (búsqueda opening/ending/tráiler/escena — opening y ending no dieron resultado directo), Internet Archive (vacío), MusicBrainz (vacío), AnimeThemes (522, caído). Punto de partida, no repetido.
- Internet Archive, búsqueda avanzada (`advancedsearch.php`): `kaguya-sama opening` (6 resultados), `kaguya-sama love is war` (106 resultados, filtrado a mediatype movies) — en español e inglés.
- Descarga y visión completa (fotogramas.py + Read) de `SEASON 1/01.mkv` y `SEASON 1/03.mkv` del ítem `kaguya-sama_202403` (Internet Archive), borrados de `/tmp/claude-0/trabajo/43-kaguya-sama-love-is-war-video/` al terminar de sacar fotogramas (pendiente de limpieza final, ver nota).
- YouTube (`yt-dlp`): funcionó para metadatos (`--print`) pero dio 403 al intentar bajar el tráiler oficial (`IwpJJiQkZzI`) para fotogramas — se resolvió con Dailymotion/Internet Archive (plan B del AYUDANTE.md).
- WebSearch (inglés): «Kaguya-sama Love is War season 1 opening ending song title artist composer», «Kaguya-sama Love is War TikTok trend viral scene meme», «Ishigami first appearance episode», «season 2 opening ending Kaze ni Fukarete», «Ultra Romantic season 3 Giri Giri theme song artist», «Chikatto Chika Chika Chika dance meme origin».
- Wikipedia API (`en.wikipedia.org/w/api.php`, extracts): páginas «Kaguya-sama: Love Is War (TV series)» y «…season 1» — confirmación cruzada de OP/ED T1 y compositor.
- Fandom (API, no la web): `kaguyasama-wa-kokurasetai.fandom.com/api.php` para la imagen oficial de Ishigami (imageinfo con `Referer: https://www.fandom.com/`).
- Dailymotion API: búsquedas `Kaguya-sama opening full`, `Kaguya-sama ending`, `Ishigami Kaguya-sama`, `Kaguya-sama Tsubame Ishigami` (en inglés).
- `herramientas/estilo.py`: paleta medida en 3 fotogramas propios (sala del consejo, calle de Tokio, atardecer).
- **Relanzo (este pase):** Internet Archive `advancedsearch.php` (dos consultas, inglés) buscando más episodios o vídeo real de Ishigami; prueba de streaming por rango HTTP con `ffmpeg -ss` directo sobre un `.ia.mp4` de Archive.org sin descarga completa (funcionó técnicamente, pero el ítem resultó ser la película de imagen real, no el anime); Dailymotion API (japonés: `石上優`, `かぐや様 石上`; inglés: `Ishigami Kaguya sama episode 6`); Fandom API `list=allimages&aiprefix=Ishigami` (13 archivos, japonés/inglés) y `imageusage`/`imageinfo` para confirmar tamaños y contexto de cada uno; se revisaron también los fotogramas ya extraídos y no usados de tandas previas (`ep1-climax`, `ep3-seg2`) para sacar 2 poses más de Shirogane sin nueva descarga.

### Bitácora de voz

**Ya hechas por el recolector** (no repetidas): AniList (favoritos, fichas de
personaje), Doblaje Wiki (ficha + reparto + datos de interés, aunque con la
tabla de reparto incompleta — la rehice yo con wikitext completo), Fandom en
inglés (Kaguya-Ice, Kei, Chika, Ishigami), Dailymotion (tráilers).

**Hechas por mí, con idioma:**
- Español: «ANMTV Kaguya-sama Love is War doblaje latino elenco»; «Kaguya-sama
  Weekly Young Jump encuesta popularidad personajes oficial resultados»;
  «Kaguya-sama Love is War fandub español latino YouTube»; «Kaguya-sama Love
  is War openings cover español latino TikTok»; «Kaguya-sama Love is War
  reseña español por qué gusta tan querida»; «"My Dubber Heroes" fandub
  Kaguya-sama canal español»; «Kaguya-sama Love is War recupera elenco
  doblaje original ANMTV Jessica Ángeles Enzo Fortuny»; «Kaguya-sama Love is
  War manga ventas millones copias Aka Akasaka» (mixto es/en); «reddit
  r/Kaguya_sama OR r/KaguyaSamaLoveIsWar subreddit».
- Inglés: «Kaguya-sama Love is War why fans love it reddit favorite
  character»; «Kaguya-sama Love is War most emotional crying scene episode
  confession»; «Kaguya-sama Love is War Crunchyroll Anime Awards nomination»;
  «"kaguyasama-wa-kokurasetai.fandom.com" popularity poll ranking»;
  «Kaguya-sama Love is War memes fandom inside jokes "10 count" OR "Chika
  Dance" OR "hayasaka route"»; «Kaguya-sama Chika Dance episode 3 viral meme
  origin know your meme»; «Kaguya-sama Love is War school festival president
  speech scene emotional episode»; «Kaguya-sama character profile birthday
  height likes dislikes official databook fanbook»; «Kaguya-sama Love is War
  "Kono Manga ga Sugoi" OR "Tsutaya Comic Award" ranking premio manga»;
  «Kaguya-sama Love is War MyAnimeList score ranking top rated comedy anime»;
  «Yu Ishigami popular character fans relate social anxiety introvert why
  loved»; «Kaguya-sama Love is War fandom complaints out of character fanart
  criticism»; «Kaguya-sama Love is War TV Tropes Funny moments what not to do
  fandom»; «Kaguya-sama Ishigami spin-off popularity "more popular than"
  Shirogane secondary character beloved»; «Kaguya-sama Love is War "Ensemble
  Dark Horse" TV Tropes Ishigami Hayasaka Miko»; «Kaguya-sama Love is War
  episode 12 fireworks scene soundtrack music cue "Kei Haneoka"»; «Kaguya-sama
  confession episode reaction video views comments most upvoted».
- Japonés: «かぐや様は告らせたい 人気投票 結果».
- APIs/directo (sin buscador): `doblaje.fandom.com/es/api.php action=parse`
  (wikitext completo de la ficha de la serie); `kaguyasama-wa-kokurasetai.fandom.com/api.php`
  (`prop=sections` y `prop=wikitext&section=N`) para Kaguya Shinomiya, Miyuki
  Shirogane, Ai Hayasaka y Miko Iino (Personality + Trivia + infobox);
  `nlab.itmedia.co.jp/research/articles/229268/` (texto completo, curl);
  `ranking.net/rankings/best-kaguya-characters` (texto completo, curl);
  `manga-comic-netabare.com/archives/28932/...` (texto completo, curl);
  `arctic-shift.photon-reddit.com/api/posts/search` (3 intentos distintos de
  parámetros, todos 0 resultados) — `tvtropes.org` bloqueado por Cloudflare
  desde este servidor (probado 1 vez, no insistí más, usé los resúmenes del
  buscador en su lugar).
- Herramientas propias: `voz.py` sobre 7 muestras oficiales de Doblaje Wiki
  (Kaguya, Shirogane, Chika, Ishigami, Ai Hayasaka, Miko Iino, Narrador) —
  frase textual + tono/velocidad medidos, no de oído. `fotogramas.py --cortes`
  sobre el tráiler oficial de la 3ª temporada (Dailymotion x8bc80m, 68
  fotogramas, 0:00-1:54), el tráiler de la película (Dailymotion x8f2tz7, 23
  fotogramas, 0:00-0:35), un tráiler largo de 9:51 (x9lifrs, 141 fotogramas) y
  un clip corto (x84di3i, 33 fotogramas) — miradas con Read; de los dos
  últimos no salió ninguna cara identificable de Hayasaka/Miko con confianza
  (los descarté tras mirarlos, tenían otros personajes). Para esas dos,
  imágenes de `kaguyasama-wa-kokurasetai.fandom.com` vía API
  (`action=query&titles=<Personaje>/Image Gallery&prop=images`, listado
  completo, y `prop=imageinfo&iiprop=url|size` con cabecera
  `Referer: https://www.fandom.com/` para bajarlas) — 6 imágenes miradas con
  Read y contrastadas contra AniList antes de citarlas (evité confundir a
  Hayasaka, rubia, con Miko, castaña, algo que casi hago con un fotograma
  ambiguo de x84di3i). `archive.org/advancedsearch.php` para episodios
  completos (nada útil, ver «No encontré»). `api.animethemes.moe` (timeout,
  no usable desde aquí).

### Bitácora de texto

**Punto de partida** (no repetido): `partes/datos-texto.md` (AniList ficha, staff, obras parecidas/relacionadas; sección Steam vacía — `recolectar.py` no encontró juego en Steam, confirmado más abajo por qué).

**Wiki de Fandom** `kaguyasama-wa-kokurasetai.fandom.com` (confirmada, la sugerida en el encargo):
- `action=query&list=allpages` (dos tandas) → mapa completo de ~500+ páginas, sin página dedicada a videojuego.
- `action=parse&prop=wikitext` leído directo en: Shuchi'in Academy, Shuchi'in Academy Student Council, List of Organizations, Timeline, Crossovers, Cubari Facaccimo, We Want to Talk About Kaguya (redirect).
- Hojas de contacto ya bajadas por `investigar_serie.py` (`herramientas/referencias/kaguya-sama-love-is-war/hoja_01.jpg`, `hoja_02.jpg`, 75 imágenes, `indice.json`) miradas enteras con Read.
- 11 imágenes bajadas en grande y miradas una por una (Read) para tipografía/cuadros de diálogo/portadas: `I_probably_already_have_this_save.png`, `Season_2_Announcement_Banner.jpg`, `Anime_Yu_Ishigami.jpg`, `177_Preview.png`, `180_Preview.png`, `Werewolf.jpg`, `Chapter59-01.png`, `Screen_Shot_2019-06-30...png`, `Chapter84-01.png`, `Chapter21-01.png`, `Chapter27-01.png` (guardadas en `/tmp/claude-0/trabajo/43-kaguya-sama-love-is-war-texto/full/`).

**Otras wikis**:
- `tropedia.fandom.com` (mirror de TVTropes en Fandom, porque `tvtropes.org` da reto de Cloudflare bloqueado — anotado, no se insistió más de dos veces): wikitext completo de la página "Kaguya-sama: Love Is War" leído en 3 tandas.
- `tvtropes.org` directo: **403/Cloudflare challenge**, descartado tras un intento.

**Búsquedas web** (WebSearch, en inglés y japonés):
1. "Kaguya-sama Love is War video game app official" (inglés)
2. "かぐや様は告らせたい ゲーム 公式 アプリ" (japonés)
3. "Kaguya-sama: Love is War" Steam visual novel Shueisha Games release date screenshots (inglés) → reveló que el "juego" de Steam es una estafa
4. "パチスロ かぐや様は告らせたい 液晶 演出 実機 台" (japonés) → detalle de interfaz de la máquina
5. Aka Akasaka interview influences inspiration manga artists favorite (inglés)
6. 赤坂アカ かぐや様 インタビュー 影響 きっかけ 頭脳戦 (japonés)
7. "First Kiss wa Owaranai" OR "First Kiss That Never Ends" Kaguya-sama studio animation 2022 (inglés)
8. Kaguya-sama Love is War director Shinichi Omata interview animation style A-1 Pictures (inglés)
9. かぐや様は告らせたい アニメ 作画 インタビュー 演出 特徴 (japonés)
10. Kaguya-sama Love is War narrator captions "mental warfare" screen text style analysis (inglés)
11. "Mamoru Hatakeyama" "Shinichi Omata" real name Kaguya-sama director (inglés) → confirmado en dos fuentes que es la misma persona
12. guya.moe "Wielding emotions to create a story" Akasaka interview (inglés) → localizó la entrevista traducida real

**WebFetch**: Sakuga Blog (notas de producción ep. 1-5, técnica de animación ✅), animatetimes.com (petición del autor al anime ✅), guya.cubari.moe (entrevista completa del autor ✅ — dos intentos de URL fallaron por 302/404 antes de encontrar la correcta vía búsqueda). Fallaron por 403: ddnavi.com, natalie.mu (anotado, no se insistió).

**Sketchfab**: `api.sketchfab.com/v3/search?type=models&q=kaguya-sama&downloadable=true` → 6 resultados, 5 de personajes/grupo de la serie con licencia CC Attribution confirmada por la API (punto 18, modelos y rigs libres).

**Fontsource/fontTools** (obligatorio del punto 5): 10 fuentes candidatas descargadas en `.ttf` desde `api.fontsource.org` y comprobadas con `fontTools.ttLib.TTFont(f).getBestCmap()` para á/é/í/ó/ú/ñ/¿/¡ — el subset `latin-ext` de Fontsource NO trae estos caracteres (son sólo extras centroeuropeos), hay que pedir el subset `latin`; las 10 los tienen. 8 elegidas para los 8 usos que pide el encargo (logo, globo, grito, pensamiento, onomatopeya, cartel, interfaz, subtítulos).

No quedan puntos pendientes de este rol (5, 6, 11, 18, 24, 25 completos). Parte terminada.
