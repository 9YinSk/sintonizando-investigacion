## Bitácora

### Bitácora de imagen

- Español: no se buscó en español aparte (la wiki y casi toda la prensa de Little Nightmares es en inglés;
  se comprobó que no hay wiki de Fandom en español para esta serie).
- Inglés (WebSearch, ~10 consultas): `Little Nightmares collaboration crossover official event` ·
  `"Little Nightmares" Identity V crossover` · `Little Nightmares Six Gecco statue figure official` ·
  `Little Nightmares First4Figures OR Numskull OR Funko figure official` · `Little Nightmares cosplay Six
  best costume` · `Little Nightmares cosplay Six worldcosplay OR deviantart handmade raincoat` ·
  `Little Nightmares official wallpapers press kit site:bandainamcoent.com OR presskit` · `Little Nightmares
  artbook "The Art of Little Nightmares" concept art book` · `Little Nightmares II Mono trench coat color
  khaki concept art hex` · `"Little Nightmares" Fortnite OR Brawl Stars OR Dead by Daylight collaboration` ·
  `"Little Nightmares" Brawl Stars official collaboration Supercell skin` · `"Little Nightmares" Fortnite
  official skin Epic Games item shop` · `"Little Nightmares" vinyl soundtrack iam8bit "Music Box Collection"`
  · `Little Nightmares Gecco Mono figure OR "The Guests" mini figure collection` · `"Very Little Nightmares"
  Six white shirt shorts mobile spin-off screenshot`.
- Directo (sin buscador, con curl/Python): API de Fandom (`littlenightmares.fandom.com/api.php`) para
  `imageinfo` y `srsearch=collaboration` / `srsearch=merchandise` (encontró la novela *The Lonely Ones*, que
  no estaba en `datos-imagen.md`); wikitext de "The Lonely Ones"; API de ambientCG (`type=Material&q=…`)
  para rubber/wood/metal/paper/fabric/leather; `herramientas/estilo.py` sobre 9 imágenes oficiales para los
  hex del punto 15; ZBrushCentral (WebFetch) para comprobar que el sculpt de Mono de "Lucas_Andrade1" es fan
  art, no oficial.
- Fuentes consultadas (ver URLs en cada punto de arriba): littlenightmares.fandom.com (wiki + API), Danbooru,
  Safebooru, Wallhaven, Sketchfab, Openverse/Flickr, Wikimedia Commons, Sideshow Collectibles, gecco.co.jp,
  Tokyo Otaku Mode, VGMdb, store.bandainamcoent.eu/.com, Siliconera, Bleeding Cool, X/Twitter (@LittleNights),
  DeviantArt, ambientcg.com, YouTube (vídeo del artbook), ZBrushCentral.
- Hojas de contacto usadas (11, ya hechas por `recolectar.py`/`investigar_serie.py`, en
  `herramientas/referencias/little-nightmares/`): se miraron las 11 completas con Read antes de escribir esta
  parte.

### Bitácora de video

- Español: "Little Nightmares sin diálogos diseño de sonido entrevista Tarsier Studios" (WebSearch) →
  Forbes México, Zonared, confirmredes de "sin diálogos".
- Inglés: "Tobias Lilja interview Little Nightmares soundtrack composer" (WebSearch) → thesoundarchitect.
  co.uk, podcast Composing Fear, entrevista de audio de LN2, vídeo de Tarsier en Facebook.
- Inglés: "Little Nightmares TikTok trend viral video" (WebSearch) → tiktok.com/tag/littlenightmares,
  ejemplos de trend de animación y "Sinking Town Trend".
- Inglés: "\"Little Nightmares\" analysis video essay YouTube design breakdown" (WebSearch) → GameLogic,
  video ensayos varios, Game Dev Unchained (narrative design).
- Fandom API (`action=parse&prop=wikitext`, con `curl -A "Mozilla/5.0"` porque sin cabecera User-Agent da
  403): The Prison, The Lair, The Kitchen, The Guest Area, The Lady's Quarters, The Wilderness, The
  School, The Hospital, The Pale City, The Transmission, Little Nightmares III (video game) — para
  confirmar nombre y orden real de cada zona.
- Fandom API `action=opensearch`: para resolver nombres exactos de página (The Lair, The Kitchen, etc.)
  antes de pedir el wikitext.
- MusicBrainz API (`ws/2/release-group`, `ws/2/release`): listas de pistas completas de los OST de LN1 y
  LN2 (ya venían los release-group en `datos-video.md`, sólo faltaba entrar a la lista de pistas).
- `yt-dlp -F`/`-j` sobre 12 vídeos de Dailymotion (de `datos-video.md`) para comprobar resolución real
  disponible antes de descargar nada.
- `yt-dlp -g`/`ffprobe`/`ffmpeg -ss … -i <url>` directamente sobre los dos ficheros mp4 de Internet
  Archive (sin pasar por `fotogramas.py`, que habría bajado 11-33 GB): 35+ fotogramas de exploración a baja
  resolución (320px) para ubicar capítulos, más 24 fotogramas a 1280px/1920px para las citas de arriba.
  Sin esta técnica no habría sido posible cumplir el "1080p o más" del punto 2 sin descargar los vídeos
  enteros.
- `herramientas/estilo.py` sobre 13 fotogramas propios (LN1 ×4, LN2 ×6, LN3 ×3) para los hex y el tipo de
  sombreado del punto 4.
- `tesseract` sobre 2 fotogramas de créditos propios (LN1) para intentar leer nombres del equipo de audio
  (resultado parcial, ver "No encontré").
- Vídeos mirados enteros o por fotogramas con Read antes de describir cualquier escena: tráiler LN1 (32
  fotogramas), tráiler LN2 (27 fotogramas), tráiler LN3 (23 fotogramas + 4 en grande), longplay LN1 (35
  fotogramas de exploración + 9 en 1280px), longplay LN2 (26 fotogramas de exploración + 10 en 1280px).

Parte completa: los 5 puntos asignados (2, 4, 9, 10, 14) están cubiertos con lo obligatorio de cada uno.
No dejo línea "Sigue".

### Bitácora de voz

- Fandom `littlenightmares.fandom.com`: categoría completa de personajes (`Category:Characters`, ~150 páginas listadas) vía API `list=categorymembers` · wikitext completo (`action=parse&prop=wikitext`) de Six, Mono, The Runaway Kid, Low, Alone, The Lady, The Janitor, The Twin Chefs, The Hunter, The Thin Man, Nomes, The Teacher, The Doctor, Dime, The Sounds of Nightmares (audio-ficción oficial) — inglés.
- Fandom, búsqueda de texto (`list=search&srwhat=text`): `voice actor`, `"voiced by"`, `Credits` — inglés, para localizar créditos de voz/vocalización de cada personaje.
- Doblaje Wiki (`doblaje.fandom.com/es`): comprobación directa de título con `action=query&titles=` en seis variantes de "Little Nightmares" — todas `missing` (confirma que no hay doblaje latino, ya visto en `datos-voz.md`) — español.
- Danbooru: conteo real de posts por personaje (`counts/posts.json?tags=`) para Six, Mono, la Lady, el Cazador, el Runaway Kid, Low, Alone, Nomes, el Conserje — medido, no de memoria.
- Arctic Shift (Reddit r/LittleNightmares): búsquedas de texto `favorite character`, `BEST FEMALE CHARACTER`, `Dime favorite`, `top 5 favorite residents`, `made me cry`, `identify relate` — inglés.
- `herramientas/voz.py` sobre un tráiler oficial de Dailymotion (Vidaextra, `x81lc28`) — confirma 0 palabras transcritas pese a 22.3 s de voz detectada (tono medio 152 Hz, muy expresivo, 33.2 semitonos): evidencia técnica adicional de que la saga no tiene diálogo hablado, sólo vocalización/música.
- `yt-dlp --skip-download --print` para metadatos de vídeos de YouTube sin necesidad de iniciar sesión (título, canal, vistas, duración): funcionó para 2 de 5 intentos; los otros 3 dieron "Sign in to confirm you're not a bot" (no se insistió más de dos veces por vídeo, según la regla del equipo).
- WebSearch (inglés y español, ~14 búsquedas de las ~50 disponibles para este rol): popularidad oficial/de fans, premios (BAFTA/D.I.C.E./NAVGTR/Golden Joystick), ventas de la saga (12 millones), reseñas sobre atmósfera y sonido, final de LN2 y reacción de jugadores, Reanimal y la reacción del fandom al cambio de estudio, memes de Six comiéndose al Nome, fandubs en español, cosplay hispano, gameplays en español (Fernanfloo).
- No se repitieron las consultas ya hechas por `recolectar.py` en `datos-voz.md` (personalidad de Six/Mono/Janitor/Lady, Danbooru genérico, Dailymotion, Reddit "favorite character"/"best scene"/"iconic").

### Bitácora de texto

_pendiente_
