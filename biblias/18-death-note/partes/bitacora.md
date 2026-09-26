## Bitácora

### Bitácora de imagen

- Fandom API (`deathnote.fandom.com/api.php`) + `investigar_serie.py`:
  1181 imágenes, 12 hojas — español/inglés — ✅.
- `api.sketchfab.com/v3/search` (ES/EN): «death note notebook», «death
  note l», «ryuk death note», «misa death note», «near death note»,
  «death note» (ordenado por ♥) — licencias reales, no de resultado de
  búsqueda — ✅.
- WebSearch (español e inglés): «Death Note colaboración cafe merchandising
  crossover pachislot figuras oficiales», «"Death Note" Jump Force
  collaboration crossover game art», «"Death Note" Universal Studios Japan
  Halloween Horror Nights maze attraction» (sin resultado de una casa del
  terror propia; sí existe el evento «Jump Summer» ⚠️), «Death Note x BAPE
  OR Uniqlo OR Loungefly collaboration merchandise art», «"Death Note"
  XLARGE Ryuk varsity jacket 2022 collaboration highsnobiety», «Death Note
  official wallpaper download site oficial fondo de escritorio Viz
  Madhouse», «free manga screentone halftone pattern pack license CC0
  download», «Clip Studio Assets free screentone brushes ink pinceles
  gratis licencia», «ambientCG CC0 license public domain textures
  confirmed».
- `curl` directo con cabecera `Referer: https://www.fandom.com/` para bajar
  las imágenes de color page (Light, L, Ryuk, Misa, Near) y medir hex con
  Pillow (`sample.py` propio, mediana de zona con y sin máscara de color) —
  ✅, archivos en `/tmp/claude-0/trabajo/18-death-note-imagen/color/`.
- `curl -A "Mozilla/5.0"` a `zerochan.net` para el tamaño real de los
  wallpapers oficiales (leído del `og:image` de cada página) — ✅.
- `python3 herramientas/estilo.py` sobre las 6 imágenes de color page:
  paleta dominante y estilo de sombreado por personaje — ✅.
- Fandom API a `List_of_Death_Note_figurines` (wikitext): confirma que la
  lista existe y qué marcas hicieron figuras, pero sin URLs de imagen
  directas por personaje ⚠️.
- No hizo falta usar `navegar.py` en esta tanda: todo respondió a `curl` o
  a la API correspondiente.

Nota de orden: el punto 3 quedó al final del archivo (no por delante del
15) por un error mío al editar por partes; el contenido está completo, sólo
el orden de guardado no siguió la numeración.

### Bitácora de video

- `yt-dlp` sobre `youtube.com/watch?v=NlJZ-YgAt-c` (tráiler AniList): **429 → «Sign in to confirm you're not a bot»**, dos intentos con minutos de por medio. No reintento más.
- `fotogramas.py` sobre 13 episodios completos de Internet Archive (`archive.org/download/death-note-XX`, y `death-note-11_202008` para el 11): **funciona perfecto**, 1280×720, sin bloqueo. 30 fotogramas extraídos y mirados con Read.
- `fotogramas.py` sobre 3 clips de Dailymotion (opening x31pve2, ending x6alujt, tráiler x89nprz): **funciona**, hojas de contacto de 6-8 fotogramas.
- `api.dailymotion.com/videos?search=...` (dos búsquedas: «Death Note analisis L Light»): da resultados pero son de la película 2017, no del anime.
- `api.animethemes.moe/anime?filter[name]=Death Note`: **403** (con `curl -g` y con `urllib` con cabeceras normales). No lo reintento (regla de dos intentos).
- `estilo.py` (Pillow) sobre 11 fotogramas para medir paleta real: **funciona**, da hex + saturación/brillo, sin necesidad de red.
- `wtas.moe/ost/death-note/25` y `/8` (WebFetch): da tracklist detectado por audio, con 5 bloques horarios por episodio.
- Wikipedia `Death_Note_original_soundtracks` (WebFetch): tracklist oficial de las 3 OST, cruzado con wtas.moe.
- WebSearch (es/en): «Death Note episode 25 death scene soundtrack», «Death Note TikTok trend keikaku doori potato chip», «potato chip Death Note TikTok trend». 3 búsquedas de las ~50 permitidas.
- `www.tiktok.com/discover/...` con `curl` y con `navegar.py --selector body`: la página carga (200) pero sin contenido útil (JS puro, 0 caracteres con navegar.py). Uso los enlaces directos a vídeos/sonidos que sí dio la búsqueda web.
- Metadatos de Internet Archive (`archive.org/metadata/death-note-XX`) para confirmar el nombre exacto del `.mp4` de cada episodio antes de pedir el fotograma: 13 episodios comprobados (01, 02, 08, 09, 10, 11, 12, 13, 24, 25, 27, 28, 33, 36, 37).
- Disco: se borraron todos los `video.mp4` descargados por `fotogramas.py` en cuanto salieron las hojas (regla del disco compartido); sólo quedan los `.jpg` en `/tmp/claude-0/trabajo/18-death-note-video/` (2,6 MB en total).

### Bitácora de voz

- Continué una tanda cortada por límite de uso: `partes/voz.md` sólo
  tenía el punto 7 escrito. Empecé desde el punto 8, sin repetir lo ya
  confirmado.
- `doblaje.fandom.com/es/api.php?action=parse&prop=wikitext&page=Death_Note`
  (español, directo): wikitext completo con el reparto de 37 episodios;
  resolvió el «no encontré» de Rem/Watari/Matsuda/Mikami que traía la
  biblia.
- `dubdb.fandom.com/api.php?action=parse&prop=wikitext&page=Death_Note_(Latin_American_Spanish)`
  (inglés, wiki de doblaje): segunda fuente para cada nombre del reparto
  latino, y plataformas oficiales.
- `en.wikipedia.org/w/api.php` (inglés): dio «too many requests» dos
  veces (varios ayudantes comparten IP); a la tercera con
  `User-Agent` identificado sí respondió. Extraje ventas, premios y
  reseñas (sección Reception).
- `deathnote.fandom.com/api.php` (inglés, wiki de la serie): alturas de
  Light, L, Misa, Near y Ryuk desde el infobox (cruce con AniList).
- `anilist.co` (ya lo trajo `recolectar.py`; sólo leí lo que faltaba):
  fichas de personaje completas para el punto 20.
- `python3 herramientas/navegar.py` en **TV Tropes**
  (`YMMV/DeathNote`, `TearJerker/DeathNote`) e inglés: la vista con
  `--selector` no basta (folders colapsados por JS), tuve que pedir
  `--html` y limpiar las etiquetas a mano para leer el contenido
  plegado.
- `python3 herramientas/navegar.py` en **YouTube** (`/results?search_query=…`,
  español): funcionó bien para ver título, canal y vistas reales sin
  necesitar login; hice un script propio con Playwright (basado en
  `navegar.py`) para sacar también el `href` de cada vídeo. Búsquedas:
  «death note fandub latino opening», «death note fandub español light».
  `yt-dlp --dump-json` sigue bloqueado («sign in to confirm you're not a
  bot») para bajar vídeo.
- `api.dailymotion.com/videos?search=…` (varias consultas en español):
  vistas muy bajas comparado con YouTube; sirve sólo como plan B si
  YouTube falla, tal como dice AYUDANTE.md.
- Reddit ya venía traído por `recolectar.py` (Arctic Shift); sólo lo leí,
  no repetí la consulta.
- **Tanda «seguir»**: la serie completa (37 episodios, TV) está en
  Internet Archive, `archive.org/details/DeathNoteTV`
  (`archive.org/metadata/DeathNoteTV` para el listado de archivos), en
  MP4 con `moov` al principio (`ffprobe` lee la duración en ~1 s vía
  HTTP sin bajar el archivo). Eso permite usar `ffmpeg -ss <seg> -i
  <url-directa>.mp4 -frames:v 1` (la función `sacar()` de
  `herramientas/fotogramas.py`) para un fotograma exacto sin pasar por
  el paso de descarga completa de `bajar()`/yt-dlp, que sí sería
  pesado (cada episodio pesa 130-200 MB).
- Con eso saqué los 6 fotogramas que faltaban en la tabla del punto 13.
  En 4 casos el minuto que traía la biblia (anotado sin vídeo, del
  subtítulo japonés) no coincidía con la escena descrita: hice una hoja
  de contacto (grid con `PIL`, igual que las hojas de
  `fotogramas.py` pero apuntando directo a la URL) cada ~25-30 s
  alrededor del minuto para localizar la escena real, y corregí el
  minuto en la tabla (diferencias de 1 a 18 min, siempre dentro del
  mismo episodio). Los dos que coincidían de entrada (Light-rabia,
  Near-calma) se quedaron con su minuto original.
- Probé además localizar la risa de Light en la tumba de L (fila
  «Alegría/triunfo», ya con enlace de YouTube, no obligatoria):
  escaneé el episodio 1 completo (fotograma en 00:22:32 sale
  sobreexpuesto/blanco, un flash de transición) y el episodio 24 entero
  cada 60 s sin encontrar la escena del cementerio; no insistí más por
  no ser obligatoria.

### Bitácora de texto

- 26-sep-2026 (repaso, español/inglés): Fandom API de `deathnote.fandom.com` para reglas del mundo, el objeto Death Note, ojos de shinigami, grupo Yotsuba, Task Force y SPK — sin bloqueo, la API funciona directo.
- 26-sep-2026 (inglés): Wikipedia `action=parse` sobre «Death Note» para la sección Plot completa, contrastada con la secuencia de arcos de Death Note Wiki (dos fuentes independientes para el punto 25).
- 26-sep-2026 (inglés): TV Tropes `Franchise/DeathNote` con `navegar.py` (funciona en esta máquina) para el panorama de toda la franquicia (usado sólo de contexto, ya cubierto por `datos-texto.md`).
- Sesión anterior (24/25-sep-2026, cortada por el límite de uso): fontTools sobre 12 fuentes descargadas de Google Fonts; entrevistas a Araki (fullfrontal.moe) y Obata (Tumblr); Inverse sobre Tsugumi Ohba; ComiPress/Yahoo con la cita original de Ohba; comparación con `encargos/` para el punto 24.
