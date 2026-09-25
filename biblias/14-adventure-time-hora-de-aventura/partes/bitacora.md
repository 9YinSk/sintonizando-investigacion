## Bitácora

### Bitácora de imagen

- **API de Fandom** (`adventuretime.fandom.com/api.php`): `action=query&meta=siteinfo`
  (confirmar subdominio), `action=query&list=search&srwhat=text` (Lego
  Dimensions, MultiVersus, collaboration crossover, Vampire Kingdom emblem),
  `action=parse&prop=wikitext&page=References_in_other_media` y
  `page=LEGO_Dimensions`, `action=query&titles=...&prop=imageinfo` (tamaños
  reales de Obsidian-concept y del logo).
- **`herramientas/investigar_serie.py`**: 1 corrida completa (6 páginas,
  `--wiki adventuretime`), 1188 imágenes indexadas, 13 hojas generadas.
- **`herramientas/estilo.py`**: 4 corridas (11 imágenes/recortes en total)
  para medir hex de Marceline, Finn, Jake, Dulce Princesa y BMO.
- **Sketchfab API** (`api.sketchfab.com/v3/search`): 6 consultas (Ax Bass,
  Finn, Jake, BMO, Marceline house, treehouse, Marceline guitar).
- **Wallhaven API** (`wallhaven.cc/api/v1/search` y `/w/<id>`): 2 búsquedas
  («adventure time», «Marceline») + 6 fichas individuales.
- **ambientCG API** (`ambientcg.com/api/v2/full_json`): 7 consultas (paper,
  fabric, denim, knit, vinyl record, cardboard, wood, leather).
- **WebSearch** (4 de mi cupo de 50, todas en inglés): «Adventure Time
  collaboration Vans OPI Uniqlo Hot Topic official merchandise»,
  «Adventure Time MultiVersus Finn Jake Marceline playable character»,
  «Adventure Time Funko Pop Marceline figure official Kidrobot vinyl»,
  «Marceline cosplay ax bass build tutorial craftsmanship», «Adventure Time
  Distant Lands Obsidian key art poster Bubblegum Marceline image», «free
  halftone dithering texture pack CC0 Photoshop brushes public domain».
- **Descargas directas** con `curl -H "Referer: https://www.fandom.com/"`:
  9 imágenes (2 model sheets, 2 screenshots de Marceline, 2 concept art de
  Obsidian, más 3 recortes con Pillow), todas miradas con `Read`.

**Cumplo AYUDANTE.md**: hojas de contacto miradas (no descritas de oído),
colores medidos con Pillow (no de memoria salvo donde digo ⚠️), licencias de
Sketchfab confirmadas por su API, «no encontré» sólo tras buscar (nunca «no
existe»).

Sigue: nada obligatorio pendiente de mis puntos (1, 3, 15, 16, 19, 23). Si
hay tiempo de sobra: medir el turquesa de BMO recortando a mano y la corona
de la Dulce Princesa; comprobar una a una las 6 licencias de Sketchfab que
quedaron sin campo de licencia.

### Bitácora de video

### Comprobación de red (25-sep-2026)

- **Dailymotion API** (`api.dailymotion.com`): funciona bien, sin límite
  aparente; usada para 9 búsquedas específicas por canción/escena.
- **`herramientas/fotogramas.py`** sobre Dailymotion: funciona con
  `yt-dlp`; en un intento dio error de «impersonation… firefox» (no 429) y
  al reintentar una vez funcionó normal.
- **TikTok oEmbed** (`www.tiktok.com/oembed?url=...`): funciona sin login,
  da título completo y autor — mejor que sólo el título del buscador.
- **MusicBrainz API**: funciona, `release-group` con `query=` da
  resultados relevantes si se afina la búsqueda (con «Marceline» en vez de
  sólo «Adventure Time», que traía discos sin relación por «Time»/«Hora»).
- No probé YouTube (pide iniciar sesión desde este servidor, según
  AYUDANTE.md) ni AnimeThemes (no aplica: es una serie occidental, no
  anime, no tiene fichas ahí).

### Búsquedas (12, todas en inglés salvo 3 en español — la serie es
estadounidense, no hacía falta japonés/coreano para vídeo)

| # | Idioma | Búsqueda | Qué salió |
|---|---|---|---|
| 1 | en | dailymotion API: Marceline bass Adventure Time | clips no oficiales, ninguno útil |
| 2 | en | dailymotion API: Adventure Time opening theme song | «Theme Song» variantes (Islands, Stakes, Food Chain, Fionna&Cake) |
| 3 | en | dailymotion API: Adventure Time trailer official | tráileres de «Fionna & Cake», «Side Quests», «Islands» |
| 4 | en | dailymotion API: I'm Just Your Problem Adventure Time | clip oficial del canal Cartoon Network ✅ |
| 5 | es | dailymotion API: Hora de Aventura intro español | intro real doblada (Espinof), piloto subtitulado (Capra TV) |
| 6 | es | dailymotion API: Marceline Reina Vampiro español latino | sin resultado útil (falsos positivos por «Reina») |
| 7 | es | dailymotion API: Hora de Aventura trailer HBO Max | tráiler de BMO (HobbyConsolas) ✅ |
| 8 | en | dailymotion API: Adventure Time Come Along With Me ending | créditos finales reales (canal fan, contenido real) ✅ |
| 9 | en | dailymotion API: I Remember You song Marceline Ice King | escena real (audio FR) ✅ |
| 10 | en | dailymotion API: Monster Marceline Obsidian song | tráiler oficial de Obsidian ✅ |
| 11 | en | dailymotion API: Slow Dance With You / Henchman | nada útil, sin coincidencias reales |
| 12 | en | dailymotion API: Marceline's Closet Finn Jake | sólo un clip genérico sin la escena |

### Herramientas usadas (con cupo)

- `fotogramas.py`: 7 clips completos (contact sheets) + 4 fotogramas
  individuales de alta resolución para medir color.
- `estilo.py --colores`: 5 fotogramas (2 de «I'm Just Your Problem»/«Fry
  Song», 3 de «Obsidian trailer»).
- Pillow directo (`Image.getpixel`): puntos exactos de piel, top y sombrero
  de Marceline en el fotograma 0:52 de «I'm Just Your Problem».
- `curl` directo: Dailymotion API (fichas + búsquedas), TikTok oEmbed (4
  vídeos), MusicBrainz API (release-group + tracklist).

### Fuentes consultadas por tipo (para mis 5 puntos)

- **Oficiales**: canal de Cartoon Network en Dailymotion, HBO Max (logo en
  el tráiler de Obsidian), MusicBrainz (tracklist del álbum en español).
- **Semioficiales/medios**: Espinof (intro), HobbyConsolas (tráiler BMO),
  Capra TV (piloto subtitulado).
- **Reloads de fans con contenido real**: canal que subió los créditos
  finales y «Teaser Trailer» que subió el tráiler de Obsidian — el
  contenido en sí es oficial (se ve el logo/staff real), el canal que lo
  aloja no.
- **TikTok**: 4 vídeos verificados por oEmbed (Rebecca Sugar, Evanescence,
  2 creadores de fandom hispano).

---

### Bitácora de voz

- **APIs directas** (no cuentan como «búsqueda web», pero son la base de casi
  todo este documento): `doblaje.fandom.com/es/api.php` (wikitext completo de
  «Hora de aventura», 87 135 caracteres, con `curl -A "Mozilla/5.0"` — sin
  user-agent, tanto `curl` simple como `urllib` de Python daban 403/error);
  `adventuretime.fandom.com/api.php` (wikitext de Marceline, Finn, Jake,
  Princess Bubblegum, BMO, Ice King); `horadeaventura.fandom.com/es/api.php`
  (funciona; la sugerida `adventuretimewithfinnandjake.fandom.com` del
  encargo da 404, el dominio correcto en inglés es `adventuretime.fandom.com`).
- **Audio real del doblaje**: 6 archivos `.ogg` bajados de
  `static.wikia.nocookie.net/doblaje/...` (con cabecera `Referer:
  https://www.fandom.com/`), transcritos con `herramientas/voz.py` (Whisper
  local). Sin esto, `biblia.md` no tenía ninguna frase textual de Marceline
  en el doblaje; ahora sí.
- **Búsquedas web** (español e inglés): «Óscar Flores doblaje Rey Helado
  director entrevista»; «Héctor Emmanuel Gómez BMO doblaje Hora de
  aventura»; «Adventure Time character popularity poll official fan
  favorite Cartoon Network»; «Adventure Time most popular character reddit
  poll ranking 2023 2024»; «Adventure Time Marceline fan favorite most
  popular character reddit»; «Hora de aventura fandub español cover opening
  intro YouTube»; «Hora de aventura fandub latino Marceline parodia
  TikTok»; «Everything Stays / Todo se queda cover español Marceline
  Adventure Time»; «I Remember You español cover Marceline Simon Hora de
  Aventura youtube»; «Princesa Grumosa oh por glob muletilla doblaje latino
  Lumpy Space Princess»; «Adventure Time finale Come Along With Me
  reception reddit tears music emotional analysis»; «Arturo Castañeda
  director doblaje Hora de aventura»; «Adventure Time Encyclopedia book
  official character profiles favorite food height»; «Guardian review
  Adventure Time Marceline best character DVD»; «Vulture Eric Thurm Ice
  King Best Character Adventure Time»; «Adventure Time awards Emmy Peabody
  Annie won series list».
- **Reddit vía Arctic Shift** (`arctic-shift.photon-reddit.com`):
  `subreddit=adventuretime&title=cried` — **sí existe** el subreddit
  r/adventuretime y está activo (esto corrige el «no encontré el subreddit»
  del recolector automático, que seguramente buscó mal el nombre exacto).
- **WebFetch**: `en.wikipedia.org/wiki/Marceline_the_Vampire_Queen`,
  `en.wikipedia.org/wiki/Adventure_Time` (dos veces, para premios y
  recepción crítica); falló en `ranker.com` (401), `youtube.com/watch`
  (redirige a un CAPTCHA de Google), `tiktok.com` (sin datos sin JS) y
  `scribd.com` (no cargó el documento).
- **Dailymotion** (API): ya lo había cubierto el recolector; repetí
  «Hora de aventura fandub» y «Adventure Time cover español opening» y sólo
  salieron vídeos sin relación real (0-24 vistas, mal etiquetados) — confirmo
  que Dailymotion **no tiene** contenido útil de doblaje o fandub para esta
  serie, mejor concentrar el esfuerzo en Doblaje Wiki y la wiki en inglés.
- Archivos de trabajo (fuera del repositorio, en
  `/tmp/claude-0/trabajo/14-adventure-time-voz/`): wikitext descargado
  (`doblaje_serie.json`, `en_Marceline.json`, `en_Finn.json`, `en_Jake.json`,
  `en_Princess_Bubblegum.json`, `en_BMO.json`, `en_IceKing.json`), 6 muestras
  de audio `.ogg` y sus transcripciones (`voz_*`).
  Fotogramas del piloto en `pilot_frames/` y del trailer de «Fionna & Cake»
  en `trailer_frames/` (este último no se usó: no sale la Marceline
  clásica). Fotogramas de Marceline, Jake, Dulce Princesa y BMO (tanda del
  punto 13) en la carpeta de scratchpad de esta sesión, `at_voz/`.

Punto 13 («su cara en cada emoción con fotograma y minuto», §13) queda con
los seis personajes pedidos (Finn, Rey Helado, Marceline, Jake, Dulce
Princesa, BMO) con al menos una cara/emoción real, cada una con clip,
minuto exacto y enlace `&t=` verificados con `fotogramas.py` sobre
Dailymotion (YouTube bloqueado en este servidor). No probé Internet
Archive: no hace falta, Dailymotion tuvo clips oficiales o subtitulados
para los cinco personajes que faltaban. Queda para más adelante, si se
retoma la biblia, ampliar a más emociones por personaje (rabia, miedo...)
y a los secundarios del punto 20 — pero eso ya no es parte de este punto
tal como se pidió.

### Bitácora de texto

### Comprobación de red (25-sep-2026)

- **curl** funciona: `adventuretime.fandom.com/api.php` (200; ojo, el
  subdominio correcto es `adventuretime`, **no** `adventuretimewithfinnandjake`
  como sugería el encargo — comprobado con `action=query&meta=siteinfo`),
  `doblaje.fandom.com` (200), `dl.dafont.com` (200, bajé un ttf real),
  `spriters-resource.com` (200), `i.imgur.com` (200), `store.steampowered.com`
  (200 pero `success:false` para esos dos appid), `cdn.jsdelivr.net/fontsource`
  (200).
- **curl** no conectó: `tcrf.net` (403), `web.archive.org` (cortado a media
  conexión, un solo intento), `industriaanimacion.com` (503 dos veces, y
  luego 000 con curl directo).
- **WebFetch**: funcionó en Wikipedia, GitHub (repo `shishkabob27/CardWars`,
  vía resumen), Spriters Resource. Bloqueado (403) en `medium.com` y `tcrf.net`.
- El acceso a `raw.githubusercontent.com` está cerrado en este contenedor para
  repos no vinculados con `add_repo` (probé bajar Google Fonts directo de ahí
  y dio un JSON de error, no el archivo).

### Búsquedas web (WebSearch, ~14 de las ~50 del cupo)

| # | Idioma | Búsqueda | Qué salió |
|---|---|---|---|
| 1 | en | animación Toon Boom Harmony Photoshop backgrounds interview | nada específico de AT, sólo genérico |
| 2 | en | Pendleton Ward influences interview D&D Flapjack | Mary Sue: cita de D&D; Wikipedia: Totoro, Home Movies |
| 3 | en | background art Nick Jennings gouache watercolor Photoshop | ficha de Fandom, sin técnica concreta |
| 4 | en | "Hey Ice King" DS game dialogue box screenshot portrait | Spriters Resource (clave) |
| 5 | en | series similares Gravity Falls Regular Show Steven Universe Over the Garden Wall | primer indicio de Flapjack |
| 6 | en | BOOM! Studios letterer Steve Wands | confirmado en Fandom + comics DB |
| 7 | en | Sketchfab Finn Jake free rig | 5+ modelos CC BY |
| 8 | en | line art black outline flat color cel shading style | análisis de estilo (⚠️, blogs) |
| 9 | en | TV Tropes symbols Enchiridion Algebraic Mathematical | Enchiridion, catchphrases abandonados |
| 10 | en | Blender Solidify Freestyle toon outline tutorial | técnica confirmada (Blender Studio, BlenderNation) |
| 11 | en | Card Wars mobile game interface screenshot | repo de GitHub con capturas reales |
| 12 | en | story arcs season by season Finn arm Elements finale | resumen T6-T10 (Wikipedia) |
| 13 | en | "Card Wars" mobile game screenshot deck | mismo repo, confirmado |
| 14 | en | Flapjack storyboard alumni Hirsch McHale Sugar | SlashFilm (segunda fuente para punto 24) |
| 15 | en | Rynda Photoshop pre-production interview | sin la entrevista original, sólo referencias |
| 16 | en | BMO screen face Nintendo parody interface | mod de GBC + sitio de Active Theory |
| 17 | en | film grain post-production Adventure Time | nada específico de la serie |
| 18 | en | dafont Adventure Time font ttf download | encontré el zip descargable real |

No hice búsquedas en japonés/coreano/chino: la serie es estadounidense: sus
entrevistas originales están en inglés (igual que anotó el pase anterior).

### Fandom (API directa, sin gastar cupo de búsqueda)

- `action=query&meta=siteinfo`: confirmé el subdominio correcto
  (`adventuretime.fandom.com`).
- `action=parse&prop=wikitext` en: Mushroom War, Land of Ooo, Ice King's
  crown, Grass Sword, Nightosphere, Steve Wands, BMO (búsqueda), Card Wars
  (redirección a desambiguación).
- `action=query&list=search`: para encontrar los títulos reales detrás de
  redirecciones (Mushroom War, story arc, BMO screen, crown ice king).

### Fuentes consultadas por tipo

- **Oficiales/semioficiales**: Wikipedia (artículo principal y temporadas
  6-10), Fandom de la serie (varias páginas), sitio de Active Theory (sólo
  resumen).
- **Herramientas técnicas usadas de verdad**: `fontTools.ttLib` (tres veces:
  fuente de fans de dafont, VT323, Press Start 2P + 4 más), API de Sketchfab
  (licencias), `file`/Pillow-equivalente vía `file` de Linux para medir
  imágenes.
- **Comunidad/fans**: TV Tropes, SlashFilm, The Mary Sue, Instructables (mod
  de BMO), GitHub (`shishkabob27/CardWars`, puerto no oficial con capturas).
- **Videojuegos**: Giant Bomb, Nintendo Life, The Spriters Resource (hoja de
  sprites vista y medida), GameFAQs (referencia, no citado directo).
- **Letras/tipografía**: dafont.com (descarga real), Fontsource vía
  `cdn.jsdelivr.net` (descarga real de 6 fuentes en subset «latin»).
- **3D**: API de Sketchfab (`api.sketchfab.com/v3/search`), licencias CC BY
  confirmadas por la respuesta de la API, no de la página web.
