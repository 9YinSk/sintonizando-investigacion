## Bitácora

### Bitácora de imagen

- Español: ninguna búsqueda específica nueva en esta tanda (el resto ya
  estaba en inglés/japonés de la tanda anterior, ver Hallazgos de los
  puntos 1/3/15/16).
- Inglés (WebSearch, esta tanda): "Nausicaä of the Valley of Wind manga
  screentone hatching hand-drawn technique Miyazaki"; "Studio Ghibli Park
  areas 2024 2025 Dondoko Forest Valley of Witches Hill of Youth official";
  "Shirohige's Cream Puff Factory Studio Ghibli official bakery Kichijoji
  Goro Miyazaki"; "Studio Ghibli official collaboration Gucci OR New
  Balance OR MUJI OR GU 2024 2025"; "Ni no Kuni Studio Ghibli Level-5
  official collaboration video game"; "Donguri Kyowakoku OR Benelic Studio
  Ghibli official figure line collectible"; ""Ghibli style" Photoshop brush
  pack free gouache texture watercolor background download"; "Studio Ghibli
  official cosplay contest craftsmanship award winning"; "Studio Ghibli
  logo Totoro silhouette trademark history design origin".
- Directo (sin buscador, cuota ahorrada): `herramientas/investigar_serie.py`
  con 7 páginas de la wiki de Ghibli (Kiki's Delivery Service, Howl's
  Moving Castle, My Neighbor Totoro, Ponyo, The Wind Rises, Nausicaä of the
  Valley of the Wind, Kazuo Oga) → 701 imágenes candidatas, 5 hojas de
  contacto miradas una a una, 3 elegidas para `hojas/`; ficha de licencia de
  ambientcg.com (Paper004, Fabric034, Wood060) y de Brusheezy/Gumroad para
  los pinceles.
- Fuentes que fallaron o no aplicaron: `investigar_serie.py` se cortó por
  tiempo (110 s) tras 5 hojas — suficiente para elegir, no hizo falta
  relanzarlo; AmbientCG no tiene una textura "watercolor paper wet" (ya lo
  avisó el punto 16 de la tanda anterior).

### Bitácora de video

- `ghibli.jp` (japonés/inglés): galería oficial y ficha de créditos
  (música, tema, dirección de arte) de Totoro, Kiki, Mononoke, Howl, Ponyo y
  Se levanta el viento.
- Dailymotion, enlaces directos de tráilers oficiales (doblados y
  subtitulados) de las 5 películas con tráiler disponible, procesados con
  `fotogramas.py --cortes`.
- Búsqueda web (idioma inglés): «Studio Ghibli background painting
  technique interview Kazuo Oga», «Ghibli AI trend 2025», «Miyazaki AI art
  insult to life itself», «why Ghibli food looks so delicious».
- Búsqueda web (idioma español): «cómo pintan los fondos de Ghibli»,
  «tendencia estilo Ghibli IA 2025», «tráiler Se levanta el viento español».
- Fuentes de texto usadas para el punto 4 y 10: Anime News Network (2008),
  Open Culture (2021), CNN (27-mar-2025), Jerusalem Post, The Bridge
  Chronicle.
- `ambientcg.com/api/v2/full_json` (API directa) para texturas CC0
  equivalentes (césped, madera).
- `herramientas/estilo.py --colores 6` sobre 6 fotogramas oficiales
  (uno por película) para paleta y grosor/color de línea.
- Comprobación de tamaño real de las 38 imágenes oficiales y los 5 clips de
  Dailymotion citados en `video.json` (códigos HTTP 200, dimensiones
  medidas con Pillow y con la API de Dailymotion) al montar esta parte.

### Bitácora de voz

- WebSearch (es): "Joe Hisaishi Studio Ghibli firma musical estilo
  composición Miyazaki entrevista" → Qobuz, Classic FM, Wikipedia ES/EN.
- WebSearch (es): "Studio Ghibli doblaje latino historia Ventura
  Distribution Cinépolis actores de doblaje recurrentes" → sin resultados
  útiles directos, redirigió a Doblaje Wiki.
- WebSearch (en): "Studio Ghibli casting policy famous actors not voice
  actors Toshio Suzuki reasoning" → Anime News Network 2011, CBR, renote.net.
- WebSearch (es): "encuesta popularidad personajes Studio Ghibli favorito
  Oricon NHK ranking" → Nippon.com (LINE Research), TierMaker (no oficial).
- WebSearch (es/en): "Studio Ghibli 'ma' 間 silencio filosofía animación
  Miyazaki entrevista pausa" → Sensacine México, Tumblr @isavstheworld.
- WebSearch (es): "Studio Ghibli fandub español latino comunidad hispana
  doblaje de fans YouTube TikTok" → TikToks de otras franquicias (no útiles),
  Doblaje Wiki.
- WebSearch (en): "'Studio Ghibli' sound design diseñador de sonido Kazuhiko
  Takahashi onomatopeyas efectos Totoro viento" → llevó a Kazuhiro
  Wakabayashi (Ghibli Fandom) y Sound Effects Wiki de Totoro.
- WebSearch (es): "escenas que hacen llorar Studio Ghibli más tristes música
  Joe Hisaishi minuto" → Qobuz, artículo académico Panambí (Antillanca 2017).
- WebSearch (es): "Cristina Hernández Enzo Fortuny actor doblaje Studio
  Ghibli entrevista experiencia grabación" → Wikipedia Enzo Fortuny,
  BehindTheVoiceActors.
- WebSearch (es): "seiyuu actores voz japonesa que han trabajado en varias
  películas Ghibli Chishu Ryu Keiko Takeshita Yuriko Ishida" → From Up on
  Poppy Hill (Wikipedia EN), confirmó a Keiko Takeshita.
- WebSearch (en): "Studio Ghibli celebridades famosas doblaje japonés Ken
  Watanabe Takuya Kimura Youtube actrices no profesionales" → Ghibli Fandom
  (Takuya Kimura), Wikipedia EN/FR.
- API directa Doblaje Wiki (`action=parse&prop=wikitext`) para 9 páginas:
  El viaje de Chihiro, Mi vecino Totoro, La princesa Mononoke, Kiki: entregas
  a domicilio, Ponyo, El increíble castillo vagabundo, Se levanta el viento,
  Un castillo en el cielo, Nausicaä: Guerreros del viento.
- API directa Fandom (`ghibli.fandom.com`, `soundeffects.fandom.com`) para
  Kazuhiro Wakabayashi y My Neighbor Totoro (1988) — WebFetch dio 402, la API
  cruda funcionó.
- API Arctic Shift (Reddit) para r/ghibli y r/Studioghibli1: búsqueda por
  `title=` (no `q=`) y `sort=asc|desc` (no `score`) — parámetros correctos
  encontrados por prueba y error, anotados aquí para no repetir el fallo.
- Dailymotion API (`api.dailymotion.com/videos?search=`) para fandub "Nada
  se Olvida" — no aisló el video exacto, sólo confirmó que aparece listado
  en resultados de búsqueda web de Dailymotion.

**Tanda 2 (continuación en modo `seguir`, 25/26-sep-2026):**
- API directa Doblaje Wiki (`action=parse&prop=wikitext`) para **Nausicaä:
  Guerreros del viento** (reparto completo del doblaje Zima 2010) y para
  **Guerreros del viento** (la ficha de la versión editada estadounidense de
  1985, con la tabla de reparto que rebautiza a Nausicaä «Princesa Zandra»).
- API `action=query&prop=imageinfo` de Doblaje Wiki para sacar la URL directa
  de 4 muestras de audio (`Howlhowl1.ogg`, `HowlWBhowl1.ogg`,
  `MononokeDisneySan.ogg`, `MononokeZimaSan.ogg`), bajadas con curl y el
  header `Referer: https://www.fandom.com/`, y transcritas con
  `herramientas/voz.py` (Whisper + ficha de voz) — resuelve el pendiente de
  «frases textuales completas» sin necesitar YouTube.
- WebSearch (en): `Miyazaki "no cuts" clause "Warriors of the Wind" Nausicaa
  edited dub contract` → SlashFilm, ScreenRant, cinema.wisc.edu, Wikipedia EN
  — confirma la cláusula de «no cortes» y la anécdota de la katana a
  Weinstein.
- WebSearch (ja): `スタジオジブリ キャラクター 人気投票 ランキング 公式` →
  ranking.net (voto de fans, ~83 personajes), varias encuestas de ねとらぼ
  (Nlab/ITmedia) por categoría (chicos, heroínas, «novio ideal»).
- WebSearch (en): `Studio Ghibli recurring character archetypes strong girl
  heroines crone witch essay` → Fandom, CBR, Japan Nakama (arquetipos de
  heroínas y de mujeres mayores).
- WebSearch (ja): `Kazuhiro Wakabayashi 若林和弘 音響 スタジオジブリ 千と千尋
  インタビュー` → Wikipedia JA, eiga.com, jfdb.jp (confirman su filmografía
  real en Ghibli, segunda fuente para el dato biográfico, no para las citas).
- WebSearch (ja): `LINE Research 2022 ジブリ 好きな映画 ランキング 5254人` →
  encontró el **comunicado de prensa oficial de LINE Corporation** en
  PR Times (fuente primaria de la encuesta) y dos encuestas más de Nlab por
  franja de edad (20s, 40s) que confirman el mismo patrón generacional.
- Lectura directa de `ranking.net/rankings/best-ghibli-characters` (HTML con
  curl, extraído con regex en Python) y de un artículo de Nlab (curl +
  regex) — no se imprimió el HTML completo, sólo los fragmentos con datos.

**Tanda 3 (`seguir`, aviso de `revisar_partes.py`: «0 minutos citados»,
26-sep-2026):**
- Búsqueda directa en la API de Dailymotion (`api.dailymotion.com/videos?search=`)
  de tráilers oficiales doblados al latino de 5 películas (Chihiro, Castillo
  vagabundo, Mononoke, Totoro, Kiki); un id salió muerto (`x9ysqao`, "Not
  found") y se sustituyó por `x4bncvf` de la misma búsqueda.
- `herramientas/voz.py` sobre 5 tráilers de Dailymotion (Chihiro, Mononoke,
  Totoro, Castillo vagabundo, Kiki) con `--idioma es --modelo small`: da
  transcripción con minuto automático (`[m:ss]` + enlace `&t=`). El de Kiki
  salió inservible (ruido/hallucination de Whisper) y se descartó.
- `herramientas/fotogramas.py` sobre 3 tráilers (Mononoke, Totoro, Castillo
  vagabundo) cada 3 s, hojas de contacto miradas fotograma a fotograma (Read
  de la imagen) para identificar la cara de cada personaje en 5 emociones
  distintas con su minuto exacto — resuelve el punto 13 (tabla de emociones)
  que antes no existía en esta parte.
- Todo lo pesado (audio, vídeo, hojas de contacto) quedó en
  `/tmp/claude-0/trabajo/102-voz/` (fuera del repositorio).

Sin `Sigue:` — no queda pendiente ninguna tarea obligatoria de mis 7 puntos.
Extras que no se hicieron (quedan en «No encontré» con ⚠️, no aquí): más
canales de TikTok de fandub hispano específico de Ghibli con métricas, la
entrevista original de Roger Ebert, un ranking oficial (no de fans/prensa) de
personaje favorito, y datos tipo databook (altura/cumpleaños) por personaje —
este último punto (20) se resuelve mejor en cada biblia de película.

### Bitácora de texto

- (es) Fandom API `logos.fandom.com/api.php` → dimensiones exactas del SVG
  del logo (1000×481) confirmadas sin descargar el archivo entero.
- (en) WebSearch "Jost font free alternative to Futura Google Fonts" →
  confirmado, varias fuentes coinciden.
- (en) WebSearch "free font alternative to Albertus typeface" → sin
  alternativa clara disponible en Google Fonts/Fontsource.
- `fontTools.ttLib` sobre `noto-serif-jp-latin-400-normal.woff2` y
  `jost-latin-400-normal.woff2` (descargados de Fontsource vía
  cdn.jsdelivr.net) → comprobación real de glifos, no de memoria.
- `ghibli.jp/gallery/{totoro,mononoke,laputa,nausicaa}001.jpg` → fotogramas
  oficiales de cuatro películas distintas a las que ya cubre la serie hermana
  98 (Chihiro), para variar los ejemplos del estilo general.
- Openverse API (`api.openverse.org`) → consultas "OpenToonz", "Wolfwalkers",
  "Studio Ponoc", "Ni no Kuni": resultados de baja utilidad (merchandising,
  fotos de eventos, LEGO fan-made), descartados tras revisar las imágenes.
- Wikimedia Commons API (`commons.wikimedia.org/w/api.php`) → "too many
  requests" en tres intentos seguidos (con y sin User-Agent); abandonado.
- `opentoonz.github.io` → página raíz sin logo accesible en el HTML
  consultado; no se insistió más.
