## Bitácora

### Bitácora de imagen

- **Red directa (sin buscador), la mayoría de mis datos**: Fandom API
  `tombraider.fandom.com/api.php` — `action=parse&prop=wikitext` sobre
  `Lara's Outfits` (18 143 caracteres, completo), `Tomb Raider Crossovers`
  (20 936 caracteres, completo), `Tomb Raider (1996 Game)/Artwork`, `Croft
  Family Crest`, `Jeep Wrangler Rubicon and Tomb Raider Bundle`; `action=query
  &list=search&srwhat=text` para "Fortnite", "crossover", "statue figure",
  "cosplay", "Nike/Land Rover/MAC Cosmetics", "Croft family crest coat of
  arms", "Trinity symbol logo"; `action=query&prop=imageinfo&iiprop=url|size`
  para dimensiones exactas de 7 imágenes distintas · Steam API `appdetails`
  para las capturas de Rise (391220), Shadow (750920) y TR2013 (203160) — 24
  capturas descargadas, miradas en `hoja_fondos.jpg` de mi carpeta de trabajo
  y 6 elegidas para `hojas/fondos_03.jpg` · Poly Haven API (`/assets?t=hdris`,
  `/info/colosseum`, `/files/colosseum`) · ambientCG API v2 (`stone`, `moss`,
  `rock`) · tombraider.com directo (curl, sin buscador) para 4 "Cosplay
  Guide"/"Gear Up Guide" (Legend, Shadow, Shadowrunner, TR III Nevada) y la
  lista de la sección `/news/cosplay` y `/news/merch` · Internet Archive
  `advancedsearch.php` (sin resultado para el artbook) · `herramientas/estilo.py`
  sobre 5 renders de vestuario y 6 capturas de fondos + Pillow directo
  (`getpixel`) para hex puntuales de prendas y de los dos símbolos.
- **Buscador web** (inglés, 4 búsquedas de ~50 usadas): "Lara Croft official
  statue Gaming Heads OR PCS Collectibles OR Weta figure" ·
  ""Tomb Raider" official cosplay recognized Crystal Dynamics OR Square Enix
  Comic-Con"" · "Tomb Raider 1996 Japanese PlayStation box art cover
  different Lara Croft" · ""Art of Tomb Raider" OR "Art of Survival" artbook
  Dark Horse Crystal Dynamics concept art".
- **Confirmado con dos fuentes (✅)**: traje icónico TR I-III (wiki + medido),
  material del Legend (cita oficial), Brenoch Adams como director de arte
  (dos Gear Up Guides distintos), tank top+pantalón de Shadow (artículo web +
  imagen oficial con el mismo texto), Fortnite/Call of Duty/Magic (wiki +
  fuente primaria citada en ella), estatuas de Gaming Heads y Weta (tienda
  oficial + prensa del fandom), sección de cosplay oficial (página propia de
  tombraider.com).
- **Imágenes miradas de verdad con Read** (no sólo enlazadas): las 20
  imágenes de `hojas/arte_oficial_01.jpg` (ya hecha por
  `investigar_serie.py`), las 6 que monté en `hojas/vestuario_02.jpg`
  (incluye recortes a resolución completa de TR1 Classic y Shadow Tank Top
  para sacar hex de píxel exacto) y las 6 de `hojas/fondos_03.jpg`, más la
  hoja de 24 capturas de Steam sin recortar en mi carpeta de trabajo antes de
  elegir las 6 finales.

### Bitácora de video

- Español: ninguna búsqueda específica (el material de vídeo de Tomb Raider es
  mayormente en inglés/japonés de origen; no hay doblaje ni fandom hispano de
  vídeo relevante a mis puntos, eso es del rol de voz).
- Inglés — web (`WebSearch`, 4 usadas de ~50): `Nathan McCree Tomb Raider
  soundtrack interview music only in caves theme title`; `Tomb Raider TikTok
  trend viral 2023 2024 Lara Croft`; `"Tomb Raider" medipack pickup sound
  iconic ding sound effect`; `"Tomb Raider" "Turning Point" official trailer
  youtube square enix site:youtube.com`.
- Fandom (`tombraider.fandom.com/api.php`, `action=query&list=search` y
  `action=parse&prop=wikitext`): `soundtrack`, `sound effects`, `quotes`,
  `opening cinematic`, `Turning Point trailer`, `Tomb Raider 1996 Music`,
  páginas leídas: «Tomb Raider (2013 Game)/Music», «Tomb Raider (2013
  Game)/Videos», «Rise of the Tomb Raider/Music», «Shadow of the Tomb
  Raider/Music», «Tomb Raider (1996 Game)/Music», «Nathan McCree», «Shadow of
  the Tomb Raider/Videos» (sólo listado). Primero comprobé `laracroft.fandom.com`
  (404, no existe) antes de confirmar `tombraider.fandom.com` con
  `action=query&meta=siteinfo`.
- Internet Archive: `https://archive.org/metadata/TombRaider_23930` y
  `.../tomb_raider_legend_xbox360` (metadatos, sin gastar búsqueda web) para
  encontrar los archivos `.mp4` reales y sus duraciones por nivel.
- Dailymotion: reutilicé los enlaces de `datos-video.md`, sin repetir la
  consulta a su API.
- YouTube: 1 intento con `yt-dlp -F` sobre `RN7_8Yholm4` (tráiler oficial
  «Turning Point» en NA) → bloqueado por «Sign in to confirm your age»,
  coherente con el aviso del encargo; no reintenté.
- Cloudflare: `tombraiderforums.com/showthread.php?t=185866` devolvió el reto
  «Just a moment...» dos veces; no hay tercera fuente equivalente localizada
  para ese dato en concreto.
- Herramientas propias usadas: `fotogramas.py` (7 veces: menú/Caves, Lost
  Valley, Great Pyramid ×2, Turning Point, SOTTR Launch, Dailymotion Globtopus)
  y `estilo.py` (2 veces, 4 imágenes) para paleta y luz medidas.

Parte terminada: los 5 puntos (2, 4, 9, 10, 14) tienen lo obligatorio del
encargo con fuente, minuto y ✅/⚠️. Lo que falta son extras, ya listados en
«No encontré» (SFX con nombre oficial, tráiler de Legend sin mirar fotograma a
fotograma, TikTok con minuto propio, 4 de las 6 poses sociales del punto 14).

### Bitácora de voz

- Doblaje Wiki, API `action=query&list=search&srsearch=Tomb Raider` (30
  resultados) y `action=parse&prop=wikitext` sobre 10 páginas: `Lara_Croft`,
  `Lara_Croft:_Tomb_Raider`, `Lara_Croft:_Tomb_Raider_-_La_cuna_de_la_vida`,
  `Rise_of_the_Tomb_Raider`, `Shadow_of_the_Tomb_Raider`,
  `Tomb_Raider:_Las_aventuras_de_Lara_Croft`,
  `Tomb_Raider:_La_leyenda_de_Lara_Croft`, `Tomb_Raider:_Catalyst`,
  `Tomb_Raider:_Legacy_of_Atlantis`, `Tomb_Raider` (redirección) — español.
- Fandom `tombraider.fandom.com`, API `action=parse&prop=wikitext` sobre
  `Lara Croft (Survivor Timeline)` (infobox + secciones «Personality and
  Traits» y «Relationships» con Roth, Samantha Nishimura, Jonah Maiava y Alex
  Weiss) y `Winston (Original Timeline)`, `Natla (Original Timeline)` — inglés.
- `raidingtheglobe.com`: biografías oficiales completas de Lara Croft en las
  líneas Core Design (1996) y Crystal Dynamics (2006), extraídas con `curl` y
  limpieza del HTML — inglés.
- `tombraider.com` (blog oficial de la franquicia, Crystal Dynamics/Amazon
  Games): 3 artículos leídos completos con `curl` — «Lara's Most Iconic Lines
  from the Survivor Trilogy» (29-may-2024), «Survivor Trilogy Lore: Sam
  Nishimura» (4-sep-2024) y «Survivor Trilogy Lore: Conrad Roth»
  (20-sep-2024) — inglés. Un cuarto intento («5 Times Jonah & Lara Were
  Absolute Besties») dio 404 por URL mal adivinada; no se reintentó por
  presupuesto de acciones.
- WebSearch (13 búsquedas de las ~50 permitidas): Guinness World Records,
  BAFTA poll, psicología de Lara Croft (perfiles de fans), controversia E3
  2012, Sam Nishimura popularidad, cumpleaños/altura/databook, fandub español,
  memes del fandom, Winston mayordomo, Natla villana, ANMTV doblaje de la
  serie de Netflix, fandub latino en YouTube, memes hispanos en TikTok —
  inglés y español.
- Búsquedas fallidas o sin resultado útil: `gamerant.com` (conexión rechazada
  al hacer `curl` directo, sólo pude usar el resumen de WebSearch); clips
  doblados latinos descargables en YouTube (bloqueado, pide iniciar sesión) y
  en Dailymotion (los resultados de `datos-voz.md` son avances de noticias de
  TV francesa, no escenas del juego dobladas).

Mi parte está completa: los 7 puntos (7, 8, 12, 13, 20, 21, 22) tienen
hallazgos con fuente, la tabla de cumplimiento y la bitácora están al final.
Si hay otra tanda para reforzar (no obligatorio, son mejoras de ⚠️ a ✅):
repetir búsqueda de fan dubs/covers **latinoamericanos** (no de España) en
TikTok e Internet Archive (punto 22), cruzar 2-3 actores secundarios de
doblaje con ANMTV/IMDb (punto 8), y buscar un longplay narrativo (no tráiler)
de Tomb Raider 2013 en Dailymotion/Internet Archive para sacar el minuto
exacto de las muertes de Roth y Alex Weiss (punto 21).

### Bitácora de texto

- Fandom (tombraider.fandom.com, inglés, `action=parse&prop=wikitext`): Trinity (Survivor Timeline), Trinity Badge, Yamatai, Kitezh, Divine Source, Solarii Brotherhood, Endurance, Croft Manor, Croft Manor (Survivor Timeline), Croft Family Crest, Notebook, Tomb Raider (Dark Horse Comics), y `imageinfo` para Trinity seal.png, Solarii Symbol.png, Trinity Badge.png, Croft Family Crest.png.
- WebSearch (inglés, 8 búsquedas): fuente del logo clásico y de Shadow, fuente de interfaz de Rise/Shadow, TressFX/Crystal Engine/Foundation Engine, ZBrush/Substance Designer en Crystal Dynamics, Toby Gard e Indiana Jones, Uncharted vs Tomb Raider vs Indiana Jones, Survival Instinct diegetic UI, TCRF debug/prototipos.
- Páginas leídas directas (curl): trsearch.org/fonts (32 fuentes de la comunidad TRLE/TEN catalogadas por versión), dafont.com/tomb-raider2.font (con descarga real del .ttf y verificación de glifos con fontTools), interfaceingame.com/games/shadow-of-the-tomb-raider (20 categorías de captura real de la interfaz, miradas en hoja de contacto propia), 80.lv (entrevista a Dannie Carlone, Crystal Dynamics), elopezr.com (blog técnico de renderizado de Rise of the Tomb Raider).
- Sketchfab API (`api.sketchfab.com/v3/search`): modelos CC de Lara Croft (fan art) y de ruinas/templos mayas, con licencia y autor verificados.
- ambientCG API: texturas CC0 de roca (`Rock064`) y grava (`Gravel043`).
- Steam Store API (`appdetails`) y las capturas ya recolectadas en `datos-texto.md`: miradas en hojas de contacto propias (`hoja_capturas.jpg`, `hoja_shadow2.jpg`, `hoja_iig.jpg`, `hoja_iig2.jpg`).
- fotogramas.py sobre un gameplay demo de Rise of the Tomb Raider en Dailymotion (E3 2015, CC/Asher Grace) — 26 fotogramas cada 15 s, mirados; sin HUD visible (vídeo cinemático de feria).
- tcrf.net: bloqueado por Cloudflare al intentar leerlo directo y también en Wayback Machine (conexión cortada por el proxy); me quedé con las citas textuales que dio el buscador sobre el menú de depuración («Escape-Tab», `-debugkeys`, `-dev` en el Remastered).
- Bloqueos anotados: fontmeme.com (403 Cloudflare, 2 intentos), tcrf.net (403 Cloudflare + Wayback caído, 2 intentos), gameuidatabase.com (403), alexricher.com (verificación humana), interfaceingame.com/games/rise-of-the-tomb-raider (404, el slug no existe en ese sitio).

Cumplimiento de mis puntos (5, 6, 11, 18, 24, 25): todos con hallazgos ✅ verificados en dos fuentes o mirados directamente; lo que quedó en una sola fuente o sin comprobar está en «No encontré» de arriba, no oculto.
