## Bitácora

### Bitácora de imagen

- Español: «Kimi no Na wa coraboración góza tenrankai» (sin resultado útil, ver búsqueda en japonés
  abajo, mejor resultado).
- Japonés: `君の名は コラボ 2024 2025 グッズ 展覧会` (sin colaboración reciente encontrada).
- Inglés: «Your Name Kimi no Na wa official collaboration merchandise Suica JR East real locations
  tourism pilgrimage» (dio el hallazgo clave de Suga Shrine y el Anime Tourism Project) y «Kimi no Na wa
  Your Name collaboration JR East station stamp rally official art» (sin resultado, no hay stamp rally
  de esta película).
- Consultas directas a API (no buscador, no gastan cupo):
  - AniList GraphQL (`graphql.anilist.co`): `Media(id:97962)` para confirmar que es el especial de
    Suntory, `Media(search:"Kimi no Na wa", type:ANIME, format:MOVIE)` para hallar el ID real (21519),
    y `Media(id:21519){bannerImage coverImage characters studios}` para portada, banner y personajes.
  - Fandom API `kiminonawa.fandom.com/api.php`: `list=allimages` con varios prefijos (`Mitsuha`,
    `Shrine`, `Itomori`, `Uniform`, `Suit`, `Miyamizu`, `Kumihimo`) para hallar las hojas de modelo de
    vestuario que el recolector automático no trajo; `list=search&srwhat=text` para «collaboration»,
    «exhibition», «merchandise» (sin resultado).
  - Doblaje Wiki API: `list=allimages&aiprefix=Your` para hallar el póster latino oficial
    (`Your_Name.jpg`), y `prop=imageinfo` para medir su tamaño real (2000×3000).
  - Wallhaven API (`wallhaven.cc/api/v1/search`): `q=kimi no na wa` para fondos de pantalla, y
    `/api/v1/w/<id>` para confirmar licencia/tags de uno de ellos.
  - Sketchfab API (`api.sketchfab.com/v3/search`): `q=<término>&downloadable=true` con «your name kimi
    no na wa» (vacío), «comet», «torii gate», «japanese train station», «shinto shrine», «kumihimo
    braid cord» (vacío) para modelos 3D con licencia.
  - Openverse API (`api.openverse.org/v1/images`): `q=Kimi no Na wa cosplay` para fotos con licencia
    libre.
  - ambientCG API (`ambientcg.com/api/v2/full_json`): `type=Material&q=Wood|Paper|Fabric` para
    texturas CC0.
  - `herramientas/investigar_serie.py --serie "Your Name: cielos y ciudades" --wiki kiminonawa --paginas
    "Taki Tachibana" "Mitsuha Miyamizu"`: hoja de contacto de 39 imágenes (guardada en `hojas/`).
  - `herramientas/estilo.py` sobre 8 imágenes (key visual, banner, wallpaper, hojas de modelo de
    vestuario) para paletas y tipo de sombreado.
  - Pillow directo (Python) para medir hex de zonas específicas de vestuario, filtrando el color de
    fondo de las hojas de modelo, cuando `estilo.py` (que promedia toda la imagen) no aislaba bien la
    tela del fondo crema de la hoja.

### Bitácora de video

- Búsqueda web (inglés): "Your Name Kimi no Na wa official trailer
  Dailymotion" → varios tráilers doblados en Dailymotion, ninguno en japonés
  sin doblaje.
- Búsqueda web (inglés): "Kimi no Na wa Your Name 2016 opening scene
  archive.org" → encontrado `kimi-no-na-wa-op-1`, `sparkle_201703`,
  `YourNameKimiNoNaWaTrailer`, `kiminonawasoundtrack`.
- Búsqueda web (inglés): "Your Name Kimi no Na wa comet scene clip Dailymotion
  archive.org" → confirmó `kiminonawasoundtrack` y la ficha de Comet Tiamat en
  la wiki de Fandom.
- Búsqueda web (inglés): "Your Name Kimi no Na wa staircase final scene clip
  video" → confirmó identidad del lugar real (Suga Shrine, Yotsuya) en
  ticketsinjapan.com y TikTok, sin clip de vídeo adicional nuevo.
- `curl` directo a `archive.org/metadata/<id>` para los 4 ítems usados:
  confirmó formato, duración y tracklist sin gastar búsqueda web.
- `fotogramas.py` sobre los 3 vídeos (tráiler, apertura, Sparkle): 3 hojas de
  contacto completas miradas con Read, más 4 fotogramas individuales grandes
  para medir color con `estilo.py`.
- No se usó el buscador web más de 4 veces (queda margen amplio del cupo de
  ~50 para otro repaso si hace falta).

### Bitácora de voz

- Español: «Your Name doblaje latino reparto», «Your Name entrevista actor de doblaje», «君の名は
  encuesta popularidad personajes» (sin resultado directo).
- Consultas directas (no buscador, ahorra cupo): API de Doblaje Wiki (`action=parse&prop=wikitext`,
  página `Your_Name`, completa + por secciones), API de Doblaje Wiki `action=query&prop=imageinfo`
  para los 5 archivos de entrevista, API de kiminonawa.fandom.com (`action=parse&prop=wikitext`) para
  Taki, Mitsuha, Sayaka Natori, Katsuhiko Teshigawara, Tsukasa Fujii, Yotsuha Miyamizu, Miki Okudera,
  Hitoha Miyamizu; API de AniList (ya en `datos-voz.md`, no repetida); Danbooru (comprobación manual
  del tag `kimi_no_na_wa.`, dato del recolector descartado por mal filtrado).
- `herramientas/voz.py` sobre las 4 muestras `.ogg` principales del reparto (Taki, Mitsuha, Sayaka,
  Teshigawara) para frase textual + tono.
- **Vídeo real mirado** (Dailymotion, ya que YouTube pide login en este servidor): tráiler oficial en
  español (`x5wv0f8`, 92 s) con `fotogramas.py --cada 3` + `--fotograma` en segundos concretos; escena
  del reencuentro final "Ending Scene" (`x6vxp2a`, 22 s) con `fotogramas.py --fotograma`; resumen
  general de apoyo (`x63fy51`, 5:48 min, marcado ⚠️ como posible fan-edit). Los 6+6 fotogramas
  extraídos se midieron con `herramientas/estilo.py --etiquetas` (paleta, tipo de sombreado, etiquetas
  WD14 con detección de personaje).
- Búsquedas en Dailymotion (español e inglés): "your name kimi no na wa trailer", "escena atardecer
  musubi", "scene clip", "nandemonaiya cover español", "sparkle cover español latino", "parodia
  español", "meme latino", "fandub", "reaccion latino llorando".
- Búsqueda en Internet Archive (`advancedsearch.php`, inglés): "kimi no na wa your name" (92
  resultados, revisados los títulos relevantes).
- Intento con Reddit vía Arctic Shift (`arctic-shift.photon-reddit.com`, subreddit `anime`, varias
  consultas por `query` y `title`): no devolvió posts de la época del estreno (2016-2017) de forma
  fiable para este título — usé en su lugar el buscador web (`WebSearch`) para llegar a reseñas y
  páginas de "ending explained" en inglés, y Wikipedia en inglés para taquilla/premios verificables.
- API de kiminonawa.fandom.com (`action=parse&prop=wikitext`) para Taki y Mitsuha completos (fichas
  principales, secciones Trivia), además de los 9 secundarios ya listados arriba.
- API GraphQL de AniList (`characters` de Media id 97962): confirmé que sólo Mitsuha y Taki tienen
  ficha completa en AniList; los secundarios no están cargados ahí (por eso fui a la wiki de personajes
  para el punto 20 de los secundarios, no a AniList).

### Bitácora de texto

- Fandom (`kiminonawa.fandom.com/api.php`, `action=parse&prop=wikitext`): páginas `Your Name`,
  `Your Name (Manga)`, `Miyamizu Shrine`, `Nandemonaiya (Movie Version)`; `list=search` para
  `manga`, `game`, `logo`, `musubi`. Segunda fuente de "Great Fire of Mayugoro":
  `remixfavoriteshowandgame.fandom.com`.
- ES: `"Your Name" Kimi no Na wa videojuego "Reversible Destiny" OR VR OR mobile game` (WebSearch) — sin resultados relevantes.
- ES: `"Your Name" Kimi no Na wa juego móvil "puzzle" OR "otome" OR aplicación oficial` (WebSearch) — sin resultados relevantes, sólo Steam Workshop de fondo de escritorio y otome sin relación.
- EN: `Makoto Shinkai "Your Name" making of interview animation technique CoMix Wave photorealistic backgrounds Photoshop` (WebSearch) — buenas fuentes de estilo/técnica (BFI, ANN).
- EN: `CoMix Wave Films RETAS Photoshop After Effects software anime production pipeline` (WebSearch) — sólo genérico de la industria, no específico del estudio; no se usa como ✅.
- EN: `"Your Name" influences "5 Centimeters per Second" "Voices of a Distant Star" Shinkai filmography style comparison` (WebSearch) → Wikipedia como fuente principal de filmografía.
- EN: `Makoto Shinkai lens flare cloud painting technique signature style analysis` (WebSearch) → sólo blogs no verificados (animepapa.com), no se citan como confirmado.
- EN: `Makoto Shinkai New York Times interview "feeling of the world changing" sky obsession` (WebSearch) → cita no confirmable en fuente primaria, descartada.
- EN: `how to recreate Makoto Shinkai anime style Photoshop clouds light god rays tutorial` (WebSearch) → tutoriales de terceros, usados sólo como referencia de técnica genérica, no como dato del estudio.
- EN: `Your Name Kimi no Na wa "Great Fire of Mayugoro" OR "Musubi-no-Kami" shrine history` (WebSearch) → confirma el incendio en dos wikis de Fandom independientes.
- WebFetch directo: BFI (`bfi.org.uk`), ANN making-of (`animenewsnetwork.com/.217914`), ANN entrevista 2016 (`.110150`), fontlot.com, fontmeme.com (403).
- Herramientas: `fontTools` (`TTFont.getBestCmap()`) sobre subsets reales bajados de Google Fonts
  (API CSS2 con `text=` codificado en `urllib.parse.quote`) para Noto Serif JP (tildes minúsculas,
  mayúsculas, ñ/Ñ, ¿, ¡ — todos presentes, en dos peticiones distintas para cubrir mayúsculas y
  minúsculas).

Sigue: nada obligatorio pendiente de ENCARGO.md en los puntos 5, 6, 11, 18, 24 y 25. Lo que falta
son extras (marcados ⚠️ en «No encontré»): software exacto del estudio, tipografía de
créditos/subtítulos oficiales, rotulado del manga, y fotogramas en hex de las escenas de escritura
a mano (depende del investigador de vídeo).
