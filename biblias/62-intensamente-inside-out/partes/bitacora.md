## Bitácora

### Bitácora de imagen

- `investigar_serie.py --serie "Intensamente (Inside Out)" --wiki pixar --paginas "Joy" "Sadness" "Anger" "Disgust" "Fear" "Anxiety" "Embarrassment" "Envy" "Ennui" "Inside Out" "Inside Out 2"` (inglés) → 251 imágenes grandes, 6 hojas de contacto.
- `pixar.fandom.com/api.php` (`list=search`, `list=allimages`, `action=parse&prop=wikitext`) en inglés, para: nombres correctos de página, imágenes limpias de Envidia (`Envy_laughs.png`), sinopsis de Intensamente 2 (localizaciones y personajes nuevos).
- Sketchfab API (`search?type=models&downloadable=true`) en inglés: Joy, Sadness, Anger, Disgust, Fear, Anxiety, Envy, Ennui, Embarrassment, Riley, Bing Bong, Headquarters console — 12 búsquedas.
- ambientCG API (`full_json?type=Material`) en inglés: paper, fabric, cardboard — 3 búsquedas.
- Wallhaven API (`search`) en inglés: «inside out», «inside out pixar», con categorías 010/111 y purity 100 — 4 búsquedas, filtradas a mano por etiquetas para descartar falsos positivos.
- WebSearch en inglés: colaboraciones oficiales (Funko, LEGO, Crocs, Disney Emoji Blitz), guías de cosplay (Envy, Anxiety, Joy), crossover de videojuego (Disney Dreamlight Valley, Kingdom Hearts), eventos de parques Disney — 4 búsquedas.
- Medí color con Pillow (script propio: mediana de un parche de 9-11 px, con recorte y grid de calibración de 10×10 para ubicar cada prenda) sobre 9 imágenes descargadas de pixar.fandom.com: 5 pósters de personaje de Intensamente 2 (Sadness, Anxiety, Envy, Embarrassment, Ennui, Joy) y 4 renders sin fondo de Intensamente 2015 (Anger, Fear, Disgust, Joy).
- Wiki en español (Doblaje Wiki, Fandom ES) no hizo falta para este rol: los puntos de imagen no dependen del idioma del doblaje.

### Bitácora de video

- Dailymotion API (`api.dailymotion.com/videos?search=`) en español e inglés: «Intensamente Inside Out opening/ending/trailer/escena» (recolector), «Inside Out official trailer pixar», «Inside Out 2 official trailer», «Inside Out Bing Bong scene», «Inside Out memory dump Bing Bong sacrifice», «Inside Out 2 Anxiety panic attack clip», «Inside Out opening scene baby Riley», «Inside Out 2 opening scene puberty» → varios clips oficiales o con metraje real localizados y usados arriba
- `fotogramas.py` sobre 7 clips de Dailymotion: trailer1 (IO1), trailer_io2 (IO2), opening_io2, ending_io2, bingbong, hockey, dinner_anger — todas las hojas miradas con Read
- YouTube (`yt-dlp` directo): da 429 / «Sign in to confirm you're not a bot» desde este servidor, como avisa AYUDANTE.md; no insistí, usé Dailymotion
- MusicBrainz: `release-group` y `release?inc=recordings` de los 2 OST (Giacchino 2015, Datzman 2024) con cabecera `User-Agent` propia — listas de pistas confirmadas
- Internet Archive `advancedsearch.php?q=inside+out+pixar`: sin vídeo oficial útil, sólo reseñas de audio y contenido de fans
- AnimeThemes: recolector ya probó, da 522 (no aplica, no es anime)
- Inside Out Wiki (Fandom) por `api.php?action=parse&prop=wikitext` (sin bloqueo, a diferencia de la web normal): páginas «Tears of Joy», «We Can Still Stop Her», «Rainbow Flyer», búsqueda de texto «Bing Bong disappears music» — confirmó a qué escena corresponde cada pista de la BSO de 2015
- `herramientas/estilo.py` (Pillow) sobre 6 fotogramas propios (no de las hojas de contacto) para medir los hex reales de cada sitio; al hacerlo detecté que dos de mis primeras lecturas de minuto/escena estaban mal (confundí el número de fotograma con el segundo, y el clip «ending_io2» mete fan art 2D no oficial a partir del minuto 5:00): corregido en los puntos 2, 4 y 14 arriba, con la parte fan art descartada como fuente
- WebSearch (inglés): «Inside Out 2 Anxiety character TikTok trend viral 2024», «Inside Out Bing Bong scene which score track Michael Giacchino»
- Segunda tanda (relanzo por pocos dominios distintos, 26-sep-2026): probé la red directa (ya sin bloqueo de certificado) sobre dominios nuevos en vez de sólo Dailymotion/MusicBrainz/TikTok/AnimeThemes
- Inside Out Wiki (Fandom) por su API (`api.php?action=parse&prop=wikitext` y `action=query&prop=info&inprop=url` para sacar la URL real de cada página): «Bing Bong» (confirma la escena de la Memoria a Largo Plazo), «We Can Still Stop Her», «Tears of Joy», «Inside Out 2 (soundtrack)» (leitmotifs de Ansiedad y Alegría); «Anxious to Meet You» no existe como página propia (lo digo para no repetir la búsqueda)
- MovieMusicUK (`moviemusicuk.us/?s=inside+out`, en inglés) para localizar la reseña real de la BSO de 2015 y citar textualmente la descripción de «Tears of Joy»; probé también `?s=inside+out+2` para la reseña de Datzman en IO2, sin resultado (no reseñaron la secuela)
- Know Your Meme (`knowyourmeme.com/memes/subcultures/inside-out-2` y `.../first-look-at-inside-outs-new-emotion-character`, en inglés): cifras reales del teaser oficial y del meme *exploitable* de noviembre 2023, con fechas y autores de origen
- Wikipedia en inglés (`en.wikipedia.org/wiki/Anxiety_(Inside_Out)`): desarrollo del personaje con las psicólogas asesoras (Lisa Damour, Dacher Keltner) y la recepción crítica de las escenas de pánico
- Internet Archive (`archive.org/advancedsearch.php?q=title:(inside out) AND mediatype:(movies)`, 1527 resultados): revisé los primeros 10, ninguno es la película oficial o un tráiler oficial completo (son programas de TV con «inside out» en el título, un cover de fans y vídeos de terceros) — confirma lo que ya había visto en la primera tanda
- yt-dlp directo sobre un tráiler oficial de YouTube: sigue dando 429 «Sign in to confirm you're not a bot» incluso en esta tanda; no insistí más de un intento, como pide AYUDANTE.md
- IMDb (`imdb.com/title/tt22022452/trivia/`, con user-agent de navegador): responde 202 sin cuerpo, no usable con curl; no reintenté con `navegar.py` por presupuesto de acciones

### Bitácora de voz

- Español: «encuesta personaje favorito Intensa Mente México votación», «personaje más
  querido Intensa Mente 2 encuesta Twitter X», «fandub español Intensamente/Inside Out
  YouTube parodia doblaje fans latino canal», «TikTok intensamente 2 fandub doblaje fans
  viral parodia México vistas», «ANMTV Intensa mente doblaje latino elenco Cristina Hernández
  Kerygma Flores», «Intensa Mente 2 doblaje latino reparto Alegría Tristeza Ansiedad actores
  de voz», «María José Guerrero Ansiedad Intensa Mente 2 voz reemplazo Nayeli Mendoza».
- Inglés: «Inside Out character popularity ranking poll fans favorite Joy Sadness Bing Bong
  Ranker», «Pixar Inside Out official character descriptions Joy Sadness Anger Disgust Fear»,
  «Inside Out 2 official character descriptions Anxiety Envy Embarrassment Ennui Pixar»,
  «Inside Out Kids' Choice Award favorite animated movie nomination Joy Riley», «Fandango poll
  Inside Out 2 favorite emotion survey audience», «Bing Bong death scene minute Inside Out
  most emotional crying scene reaction», «Inside Out fandom memes core memory meme jokes what
  not to do fan gets annoyed», «tvtropes YMMV Inside Out tearjerker Bing Bong the reason
  you're crying», «Inside Out review why people love it therapists praise emotions accurate
  identify character», «Inside Out 2 reddit favorite emotion poll Anxiety most popular».
- Fuentes consultadas por API/directo (sin buscador): Pixar Wiki (pixar.fandom.com/api.php,
  wikitext de Joy, Sadness, Anger, Disgust, Fear, Anxiety, Riley), Doblaje Wiki
  (doblaje.fandom.com/es/api.php, wikitext de «Intensa mente» e «Intensa mente 2»),
  Dailymotion API (api.dailymotion.com/videos?search=…, tráilers oficiales doblados),
  `herramientas/voz.py` (2 muestras de audio oficiales transcritas y medidas),
  `herramientas/fotogramas.py` (2 tráilers/teaser mirados fotograma a fotograma, 8 fotogramas
  propios guardados en `/tmp/claude-0/trabajo/62-intensamente-inside-out-voz/`).
- Bloqueos anotados: stitchkingdom.com (503 en vivo, Wayback también bloqueado esta sesión),
  Arctic Shift sin resultados para r/insideout, YouTube sin acceso directo a video (sólo
  metadata por buscador). TV Tropes ya no está bloqueado (se arregló el certificado del proxy
  en `navegar.py`: se releyó `TearJerker/InsideOut` con `--selector body` y confirmó la frase
  original «Take her to the moon for me… okay?» de Bing Bong, la misma escena de la que salió
  la adaptación al doblaje «Llévala a la Luna de mi parte» — y que Pete Docter comentó que
  Richard Kind, su actor de voz original, casi llora al grabar esa línea).
- Segunda pasada (26-sep-2026, tras aviso de `revisar_partes.py` de que la parte tenía sólo 1
  dominio distinto enlazado): se convirtieron en enlaces reales todas las fuentes ya citadas
  por nombre (Doblaje Wiki, Pixar Wiki, Wikipedia, Looper, Animation Magazine, Cinemablend,
  Paul Ekman Group, Psychology Today, anniewright.com, NPR, Cedar Counseling, The Psychology
  Group, Know Your Meme, TV Tropes, Infobae, TVAzteca, unotv, La Razón de México, Tomatazos,
  El Universo, MTV News, TIME, TikTok) con `WebSearch` para confirmar la URL exacta de cada
  una; ahora hay 24 dominios distintos enlazados (antes 1).

### Bitácora de texto

- Se descartó `partes/datos-texto.md` de `recolectar.py`: el buscador automático
  de AniList cruzó mal el título y trajo un manga hentai sin relación («Sweet
  Spot»/«Inside-out», Comic Kairakuten). Se investigó todo de cero.
- Inglés: «Inside Out movie logo font identifont», «Inside Out Pixar headquarters
  console screen text font», «Inside Out Cinestory Comic Joe Books speech
  bubbles», «Inside Out: Thought Bubbles mobile game interface screenshots menu»,
  «Disney Infinity 3.0 Inside Out Play Set menu interface screenshots», «Pete
  Docter Ralph Eggleston Inside Out character design interview making of
  meatball», «Pete Docter Inside Out influence Everything You Always Wanted to
  Know About Sex control room brain», «Herman's Head TV series anthropomorphized
  emotions similar to Inside Out», «Inside Out 2 world Sar-Chasm Belief System
  Vault Sense of Self islands», «Ralph Eggleston Inside Out color script art
  direction interview lighting palette», «Inside Out Dream Productions scene
  aspect ratio widescreen film grain vintage look making of», «Inside Out
  cinematography camera framing per emotion analysis», «if you liked Inside Out
  recommendations similar movies personified emotions», «TV Tropes Inside Out
  Follow the Leader similar works influenced by», «Osmosis Jones compared Inside
  Out body personification», «Inside Out 2 Sadness Steam Kingdom Hearts crossover
  Fortnite Dreamlight Valley», «Inside Out 2 construction site sign Puberty
  Headquarters renovation Brain Changes scene», «Blender tutorial Pixar style
  shading subsurface scattering glow character stylized render toon Principled
  BSDF».
- Japonés: «インサイド・ヘッド 邦題 ロゴ フォント Pixar» (título y logo del estreno japonés).
- Fandom (API `api.php`, sin bloqueo): wikitext de Headquarters, Control Console,
  Mind Manuals, Islands of Personality, Long Term Memory, Train of Thought, Dream
  Productions, Belief System, Vault of Secrets, Sar-chasm, en
  `insideout.fandom.com`.
- Capturas oficiales bajadas y miradas con `Read`: 3 capturas de App Store de
  *Inside Out: Thought Bubbles* (API `itunes.apple.com/lookup?id=918780702`),
  guardadas en `/tmp/claude-0/.../scratchpad/juego/`.
- Letras: 11 fuentes libres bajadas de `fonts.gstatic.com`/GitHub de Google Fonts
  (Chewy, Baloo 2, Fredoka, Bangers, Bubblegum Sans, Sniglet, Comfortaa, Quicksand,
  Nunito, Work Sans) y comprobadas con `fontTools` (`getBestCmap()`) para á é í ó
  ú, mayúsculas, ñ, Ñ, ¿ y ¡: **todas completas**.
- Fallos de red anotados: `tcrf.net` (403), `web.archive.org` (dos intentos,
  `ws_closed_mid_exchange`), `herramientas/navegar.py` (`ERR_CERT_AUTHORITY_INVALID`
  en cualquier URL), `api.github.com` (sin acceso en esta sesión, se necesitaría
  `add_repo`).
