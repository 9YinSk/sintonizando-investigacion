## Bitácora

### Bitácora de imagen

Partí de `partes/datos-imagen.md` (no repetí AniList, Danbooru genérico
por personaje, Safebooru genérico, Wallhaven, Sketchfab de personajes ni
Openverse) y de `biblias/33-frieren/partes/imagen.md` + su `biblia.md`
(secciones 3, 4, 5, 16, 17, 19, 23, leídas con `sed`/`cat`, no con
`seccion.py` porque es de otro encargo) para no repetir nada.

**Red directa** (sin gastar buscador):
- **Frieren Wiki (Fandom), API**: `list=categorymembers` sobre
  `Category:Locations` (30+ sitios); `action=parse&prop=wikitext` sobre
  **Official Guide Book**, **Ruins of the King's Tomb**, **Aureole**,
  **Frieren: Beyond Journey's End Season 1/Gallery** y **Season
  2/Gallery** (para las secciones «Concept Art» y «Exhibition
  Illustrations»); `action=query&prop=imageinfo` para tamaños y URL de
  6 imágenes.
- **Descargas directas** (con `curl -A "Mozilla/5.0" -e
  "https://www.fandom.com/"`, medidas con Pillow/`estilo.py`, **vistas
  con Read**): Ruins of the King's Tomb, Rufen Region abandoned fort
  draft, Bier Region ruins draft, Aureole EP4, Aureole concept art, el
  wallpaper del árbol dorado (Wallhaven).
- **`herramientas/investigar_serie.py --wiki frieren --paginas "Royal
  Capital" "Aureole" "Ruins of the King's Tomb" "Lake Korridor" "Heiß"
  "Warm"`**: 111 imágenes enlazadas, 91 grandes → `hoja_01.jpg` y
  `hoja_02.jpg` (copiadas a `hojas/paisajes_01.jpg` y `paisajes_02.jpg`),
  **vistas enteras con Read**.
- **Danbooru API** (`posts.json?tags=sousou_no_frieren+scenery`) y
  **Safebooru API** (mismo tag): 8 resultados cada una, cruzados por
  `md5`/tamaño.
- **Sketchfab API** (`/v3/search?type=models&q=…`): «frieren village»
  (sin resultados), «frieren ruins» (sin resultados), «frieren statue»
  (4 resultados, con Himmel), «medieval fantasy village low poly» (8
  resultados genéricos).
- **ambientcg API** (`/api/v2/full_json?type=Material&q=…`): Grass,
  Moss, Bark, Water, Rock — elegidas Grass001, Bark014, Rock064, Ice002.
- **Wayback Machine** (`archive.org/wayback/available`) para
  `frieren-anime.jp/special/map/`: encontró snapshot pero la descarga
  del snapshot dio «blocked by egress policy» (2 intentos, con y sin
  `http/https`).

**Buscador web** (4 búsquedas de mi cupo de ~50):
- Japonés: «フリーレン展 原画展 background art exhibition Frieren»;
  «フリーレン 聖地巡礼 風景 ロケハン 元ネタ ヨーロッパ».
- Inglés: «"Sousou no Frieren" background art book "美術ボード" OR
  "background art" exhibition 2025»; «Frieren background art real
  Europe inspiration Rothenburg Dinkelsbühl location scouting».

**Fallos y cómo los resolví**:
- `frieren-anime.jp/special/map/`: **Cloudflare** (verificación JS) — no
  hay `navegar.py` disponible en este contenedor (falta el navegador:
  «Executable doesn't exist»); probé la Wayback Machine como plan B y
  también falló (política de red del contenedor) — anotado en «No
  encontré», no insistí una tercera vez.

### Bitácora de video

- Fandom API (`frieren.fandom.com/api.php`) — wikitext de `Locations`,
  `Aureole`, `Qual`, `The Golden Land Arc`; búsqueda de texto para
  «Flamme grave», «Aureole», «Titan Fortress Ruins». En español no hace
  falta: la wiki es en inglés.
- Descarga directa de imágenes de `static.wikia.nocookie.net` con cabecera
  `Referer: https://www.fandom.com/` (AYUDANTE.md) — 3 imágenes, medidas
  con `estilo.py`.
- `fotogramas.py` sobre dos vídeos de Dailymotion (`x8mkolb` tráiler,
  `x8qbrgb` fragmento de episodio): 6 fotogramas nuevos, todos mirados con
  Read y medidos con `estilo.py --colores 5`.
- `api.dailymotion.com/videos?search=…` para localizar clips (varios
  intentos: «Sousou no Frieren Anytime Anywhere», «OP1 Yuusha» — sin vídeo
  de vídeo real del OP, sólo el tráiler y el fragmento de episodio
  sirvieron).
- `archive.org/advancedsearch.php` — sin vídeo útil de OP/ED (uno resultó
  ser audio).
- WebSearch (en inglés): «Evan Call Frieren interview music nostalgia
  memory theme», «Frieren background art director interview scenery
  melancholy», «Frieren TikTok trend backgrounds aesthetic edit
  landscapes», «Frieren video essay analysis background art direction»,
  «Frieren season 2 trailer official landscape scenery minute».
- `navegar.py` sobre `epicstream.com` y `gamerant.com` (artículos con JS;
  hacía falta para leer el texto real, no sólo CSS).
- `curl` directo sobre `anitrendz.com` y `blog.sakugabooru.com` (sí
  responden a curl con cabecera de user-agent).
- Arctic Shift (`arctic-shift.photon-reddit.com`) para r/Frieren, búsqueda
  por título «background» y «Denken» — `reddit.com` directo da bloqueo
  («blocked due to a network policy»).
- AnimeThemes (`api.animethemes.moe`) — error 522, igual que le pasó al
  recolector automático; no insistí (regla de dos intentos, AYUDANTE.md).

### Bitácora de voz

**Red directa** (sin gastar el buscador):
- `frieren.fandom.com/api.php` — `action=query&list=search` (14 búsquedas de
  imágenes por palabra de emoción en inglés: angry, embarrassed, scared,
  cries, glares, delighted…, para las 5 caras del punto 13) y
  `action=parse&prop=wikitext` para Frieren, Fern, Stark, Himmel (secciones
  Trivia, para el punto 20) y `action=query&prop=imageinfo&iiprop=url|size`
  para medir 6 fotogramas (todos 1920×1080).
- Descarga directa de 6 imágenes de `static.wikia.nocookie.net` con cabecera
  `Referer: https://www.fandom.com/`, **todas miradas con Read** antes de
  describirlas (AYUDANTE.md).
- `doblaje.fandom.com/es/api.php?action=parse&prop=wikitext` con el título
  correcto en español (`Frieren: Más allá del final del viaje`) — el
  recolector automático había fallado por usar el título en inglés.
- `youtube.com/oembed?url=…&format=json` para 2 clips nuevos de Crunchyroll
  en Español (sin necesitar sesión).
- `yt-dlp --write-auto-subs --sub-langs "es.*"` sobre los 2 clips nuevos:
  **bloqueado** («Sign in to confirm you're not a bot»), mismo bloqueo de
  YouTube que ya documentan las otras partes.
- `api.dailymotion.com/videos?search=` con 7 consultas (4 ya probadas por
  el recolector, repetidas para comprobar que seguían sin resultado nuevo,
  + 3 mías) — sólo un hallazgo nuevo (el AMV de IA).
- `arctic-shift.photon-reddit.com/api/posts/search` en r/Frieren, `title=`
  con «meteor», «Era meteor» (con pausas de 2 s) — encontré el post de 131
  votos sobre la próxima lluvia de meteoros y confirmé los dos fan arts del
  mismo motivo.
- `curl` directo (con user-agent) sobre `espinof.com` y `efrenrodher.com`
  — ambos respondieron sin bloqueo; filtré el HTML con una expresión
  regular sobre `<p>` para no imprimir la página entera.

**Buscador web** (6 de mi cupo de ~50):
- Inglés: «Frieren character popularity poll official Shonen Sunday 2024
  2025 ranking»; «Frieren Beyond Journey's End review backgrounds OR
  scenery OR landscapes melancholy why fans love».
- Español: «Frieren identifica personaje "por eso amo" OR "por qué me
  encanta" melancolía paisaje reseña español»; «"Frieren" fandub latino OR
  doblaje fans escena "campo de flores" OR "meteoros" reacción youtube»;
  «Frieren fandub español "paisaje" OR "melancolía" OR "escena" reacción
  youtube OR tiktok comunidad hispana».

**Fallos y cómo los resolví**:
- Recolector automático: falló en Doblaje Wiki por usar el título en
  inglés — lo resolví buscando el título latino real en el propio
  wikitext de la ficha de Crunchyroll.
- `yt-dlp` sobre los 2 clips nuevos de Crunchyroll: bloqueado por login;
  usé `oembed` (sin sesión) para al menos confirmar título y canal, y dejé
  la frase exacta en «No encontré» en vez de inventarla.
- Dailymotion: sin fandub de voz nuevo pese a repetir las 4 búsquedas del
  recolector + 3 propias — confirma que la hermana ya encontró lo poco que
  hay.

**Parte terminada**: los 7 puntos (7, 8, 12, 13, 20, 21 y 22) tienen lo
obligatorio del encargo cubierto, con fuente y, donde aplica, minuto o
tamaño. No dejo ninguna línea «Sigue:».

### Bitácora de texto

- WebSearch (ja): `葬送のフリーレン 背景美術 聖地巡礼 ロケハン 実在の場所` →
  [libert.co.jp](https://libert.co.jp/pilgrimage-guild/frieren-pilgrimage/),
  [yutorilog.com](https://yutorilog.com/frieren-stage/)
- WebSearch (en): `Frieren anime background art real world location inspiration pilgrimage`
  → [AniTabi](https://anitabi.jp/works/36?lang=en)
- WebFetch: frieren-anime.jp/special/map/ (403 con WebFetch normal) →
  reintentado con `navegar.py --selector body` (200, texto completo de los
  28 títulos); `--captura` dio pantalla en blanco (mapa dibujado con JS)
- WebFetch: anitabi.jp/works/36 (lista de 7 sitios de peregrinaje)
- WebSearch (ja): `葬送のフリーレン 聖地巡礼 ひたち海浜公園 ネモフィラ 蒼月草 モデル` →
  [nlab.itmedia.co.jp](https://nlab.itmedia.co.jp/cont/articles/3377207/),
  [anitabi.jp/spots/2841](https://www.anitabi.jp/spots/2841)
- WebSearch (ja): `葬送のフリーレン 美術ボード 画集 背景 光 インタビュー 高木佐和子` →
  [animageplus.jp](https://animageplus.jp/articles/detail/55395) (poco
  contenido descriptivo, descartado)
- WebSearch (en): `Frieren anime lighting nostalgia melancholy analysis mono no aware backgrounds article`
  → [Unwinnable](https://unwinnable.com/2026/03/16/the-aesthetics-of-impermanence-how-frieren-visualizes-untranslatable-japanese-philosophy/)
- WebFetch/navegar: unwinnable.com (artículo completo, 23.6k caracteres,
  leído en dos tandas)
- WebSearch (en): `Frieren anime compared Studio Ghibli Isao Takahata landscape nostalgia influence article`
  → [FandomWire](https://fandomwire.com/frieren-beyond-journeys-end-has-the-essence-of-a-studio-ghibli-film/)
- WebFetch: fandomwire.com (citas textuales sobre fondos/paleta)
- WebSearch (en): `"Frieren" anime "Yokohama Kaidashi Kikou" OR "Mushishi" landscape melancholy comparison essay`
  → [CBR](https://www.cbr.com/10-cozy-anime-that-are-surprisingly-deep/),
  MyAnimeList (recomendaciones cruzadas)
- WebFetch: cbr.com (lista de animes parecidos, con cita por título)
- WebSearch (ja): `葬送のフリーレン テロップ 字幕 "年後" 書体 フォント アニメ` →
  [Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14289239084)
- WebFetch: chiebukuro.yahoo.co.jp (fuente del avance de episodio)
- WebSearch (ja): `文游明朝体 勇壮かな フリーレン OR モリサワ 使用例` →
  [morisawa.co.jp/fonts/specimen/6593](https://www.morisawa.co.jp/fonts/specimen/6593)
  (ficha oficial del tipo, sin ejemplo de uso en Frieren)
- WebSearch (ja): `葬送のフリーレン 墓 墓標 文字 刻まれた ヒンメル` →
  [office-tokiwa.com/eiga24](https://office-tokiwa.com/eiga24/)
- WebFetch: office-tokiwa.com/eiga24 (estatua de Himmel, tumbas y memoria)
- WebSearch (ja): `フリーレン 2期 37話 ヒンメル 自伝 湖畔の街 修道院 書物` →
  [frieren-anime.jp/story/2nd/ep37](https://frieren-anime.jp/story/2nd/ep37/),
  [dogadaijobu2025.com](https://dogadaijobu2025.com/archives/8036),
  [note.com/sakuraigo](https://note.com/sakuraigo/n/n179c6ef7e84e)
- WebFetch: frieren-anime.jp/story/2nd/ep37 (sinopsis y créditos oficiales)
- WebFetch/navegar: dogadaijobu2025.com (reseña larga del episodio 37)
- WebFetch/navegar: note.com/sakuraigo (cita exacta de la página en blanco)
- WebSearch (ja): `MapleStory Frieren collaboration map area background screenshot September 2026`
  → [Noisy Pixel](https://noisypixel.net/maplestory-frieren-beyond-journeys-end-collaboration-september-2026/),
  [Nexon](https://www.nexon.com/maplestory/micro-site/frieren)
- WebFetch/navegar: noisypixel.net (detalle del evento, estatua de bronce)
- WebSearch (Herramientas propias): `curl api.php` y `navegar.py` sobre
  `tcrf.net` (bloqueado, verificación Cloudflare, 2 intentos); búsqueda
  `site:tcrf.net Frieren` (cero resultados, confirma que no hay juego)
- WebSearch (ko): `장송의 프리렌 배경 미술 풍경 분석 서정적` → namu.wiki (bloqueado al
  intentar leerlo, 2 intentos: curl y `navegar.py`), ko.wikipedia.org
- WebSearch (zh): `葬送的芙莉莲 背景美术 风景 光影 分析` → resultados de baja calidad
  (wallpapers, sitios de dudosa fiabilidad), zhihu bloqueado al intentar
  leer la pregunta de estilo de dibujo (2 intentos)
- Fontsource API: `api.fontsource.org/v1/fonts?subsets=latin-ext` (lista
  completa, filtrado por Python para familias «zen/shippori/antique/kaisei»)
- Descarga y verificación con fontTools: `kaisei-tokumin.ttf`,
  `shippori-antique.ttf`, `zen-antique.ttf` desde `fonts.gstatic.com`,
  comprobados los 15 caracteres (á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü) con
  `TTFont(f).getBestCmap()`
- Herramientas propias: `python3 herramientas/seccion.py 33-frieren --indice`
  y lectura de las secciones 6, 7, 13, Punto 18, Punto 24 y Punto 25 de
  `biblias/33-frieren/biblia.md` (para no repetir)
- Repositorio: `ls biblias/`, lectura de
  `biblias/100-la-princesa-mononoke/biblia.md` (canal `#📸・fotos` ya usado
  como candidato) y comprobación de que `101-your-name-cielos-y-ciudades`
  y `102-el-estilo-ghibli-en-general` tienen partes pero no biblia
- Lectura de `servidor/inventario.md` (canal `#📸・fotos`, etiqueta
  «Paisaje», línea 172) y de las partes ya escritas por mi equipo:
  `biblias/89-frieren-paisajes-y-memoria/partes/imagen.md` y `video.md`

Revisado contra ENCARGO.md: los puntos 5, 6, 11, 18, 24 y 25 quedan
cubiertos con fuentes propias (no repetidas de la hermana). Los ⚠️ de
«No encontré» son detalle extra o bloqueos de red ya documentados con sus
dos intentos, no puntos obligatorios sin cubrir.
