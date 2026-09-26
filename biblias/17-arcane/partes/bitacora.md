## Bitácora

### Bitácora de imagen

- Corrí `herramientas/investigar_serie.py --serie "Arcane" --wiki arcane
  --paginas "Jinx" "Vi" "Jayce Talis" "Viktor" "Caitlyn Kiramman" "Ekko"
  "Silco"` (antes daba error de red): 268 imágenes, 6 hojas. Miré las 6.
- API de Sketchfab (`api.sketchfab.com/v3/search?type=models&q=…`): 6
  búsquedas para confirmar licencias de los modelos ya listados + 2 nuevas
  búsquedas (Vi gauntlet, chibi).
- API de Poly Haven (`api.polyhaven.com/info/<slug>`): 2 consultas (autor +
  licencia de Spray Paint Bottles y Painted Brick).
- API de ambientCG (`ambientcg.com/api/v2/full_json`): 9 búsquedas (ladrillo
  pintado, metal oxidado, hormigón, chapa, cuero, tela a cuadros, papel,
  metal genérico) para las texturas del punto 19.
- Medí colores por pixel con Pillow (Python) en `Piltover_Crest.png` y
  `Zaun_Crest.png` bajados directo de Fandom (con `Referer`).
- `navegar.py` (en inglés, 2 páginas): la galería de carteles de Netflix
  Tudum (sólo dio el título, sin alt-text de las imágenes) y el artículo de
  The Mary Sue sobre esos carteles (sí sirvió, con descripción).
- Buscador web, 8 búsquedas en inglés: pinceles/grunge libres, screentone
  gratis, colaboración Fortnite, cosplay oficial, café pop-up, gacha/PUBG
  Mobile, Magic the Gathering, tokidoki, Nendoroid/Youtooz/Funko.
- No usé japonés/coreano/chino en esta parte: todo el material oficial de
  colaboraciones y merchandising que encontré está en inglés (Riot Games es
  la fuente primaria en todos los casos).

### Bitácora de video

- IA `arcane-season-1-60fps`, item con los 9 episodios de la T1 en 1080p,
  bajado sin login: https://archive.org/details/arcane-season-1-60fps
- Descargué 1×03 (`[60FPS].Arcane.S01E03...mp4`, 257 MB) con
  `fotogramas.py ... --cada 40` (visión general, 67 fotogramas) y luego
  `--desde 1150 --hasta 1350 --cada 5` (fino) para ubicar la escena de Silco;
  las hojas quedan en `/tmp/claude-0/trabajo/17-arcane-video/e03_overview/` y
  `e03_fine/`.
- Busqué primero la prueba Hextech de Jayce y Viktor (`todo flota, funciona`)
  en 1×03 entre los minutos 0 y 32: **no está ahí** — lo que hay en ese tramo
  es Silco/Vander (arriba) y escenas de Heimerdinger/Powder.
- Descargué también 1×04 (`e04_overview/`, `--cada 45`, visión general de
  los 40:43) y afiné dos tramos: `--desde 650 --hasta 800 --cada 8` (la gema
  con Heimerdinger, `e04_gema/`) y `--desde 1420 --hasta 1620 --cada 10` (el
  discurso, `e04_speech/`). Confirmé ahí las dos escenas del punto 2.
- YouTube: `yt-dlp -j` sobre `F5tSoaJ93ac` (Enemy) dio metadatos bien, pero
  la descarga real con `fotogramas.py` para ese mismo vídeo y para el clip
  de fan `v91giP0wo5Y` dieron **"Sign in to confirm you're not a bot"** las
  dos veces (probé una vez cada uno, sin insistir, según la regla de
  AYUDANTE.md de no gastar más de dos intentos). `navegar.py` no aplica aquí
  (es para páginas, no para bajar vídeo).
- Dailymotion sí funcionó sin problema: bajé
  `https://www.dailymotion.com/video/x89n6ax` (1:53) con `fotogramas.py
  --cada 15` y lo miré completo (8 fotogramas, una sola hoja).
- Medí color con Pillow (`ImageStat.Stat(...).mean`, promedio real del
  fotograma, no un pixel suelto ni una paleta de fans) sobre 4 fotogramas
  propios de 1280 px sacados con `--fotograma <segundo>` (ver punto 4).
  Antes probé recortar celdas de las hojas de contacto por coordenadas: dio
  valores erróneos (el color de fondo del lienzo, no el de la imagen) — lo
  descarté y usé fotogramas sueltos en su lugar.
- Wiki de Arcane (`arcane.fandom.com/api.php`): `action=parse&prop=wikitext`
  sobre «Jayce Talis» (confirma que el flashback del padre de Jayce es del
  episodio 2, no del 3 — por eso descarté esa hipótesis) y `action=query&
  list=search` con «Jayce father explosion flashback» y «Jayce hextech night
  demonstration Mel» (en inglés).
- Espacio en disco: borré los `video.mp4` de 1×03 y 1×04 (≈500 MB juntos) al
  terminar de sacar las hojas; sólo quedan las hojas JPEG en
  `/tmp/claude-0/trabajo/17-arcane-video/` (fuera del repositorio, como pide
  AYUDANTE.md).

### Relanzo (26-sep-2026)

- YouTube volvió a bloquear `F5tSoaJ93ac` hoy (mismo error). Lo busqué en
  Internet Archive (`advancedsearch.php?q=title:(Enemy) AND Arcane`) y
  aparecieron **varias copias subidas por fans**, incluida una de 213 s
  (igual a la duración oficial) en 1080p: la bajé con `fotogramas.py --cada
  15` (`enemy_overview/hoja_01.jpg`, 15 cuadros) y la miré entera — confirma
  el opening con fotograma propio, ya no sólo metadatos.
  https://archive.org/details/9convert.com-imagine-dragons-x-jid-enemy-from-the-series-arcane-league-of-legends-1080p
- Mismo ítem de siempre (`arcane-season-1-60fps`) para 1×05 y 1×06: bajé
  ambos completos con `--cada 60` (visión general) y luego afiné 1×05 en
  `--desde 480 --hasta 960 --cada 15` (`e05_fine/`) y `--desde 520 --hasta
  640 --cada 5` (`e05_demo/`, la escena de Jayce/Marcus con la crisis de
  enforcers) y `--desde 640 --hasta 760 --cada 10` (`e05_hexcore/`, la
  escena de Jinx que sí sirvió); y 1×06 en `--desde 745 --hasta 870 --cada
  15` (`e06_gift/`, Marcus/Ren/Silco) y `--desde 1580 --hasta 1720 --cada 15`
  (`e06_vi/`).
- Color con Pillow (mismo método del punto 4) sobre 4 fotogramas nuevos de
  1280 px con `--fotograma <segundo>`: `color/fotograma_00660.jpg` (1×05
  11:00), `color/fotograma_01080.jpg` (1×05 18:00), `color/fotograma_01310.jpg`
  (1×06 21:50) y `color/fotograma_01620.jpg` (1×06 27:00).
- Wiki de Arcane (`arcane.fandom.com/api.php?action=parse&prop=wikitext`)
  sobre «Everybody Wants to Be My Enemy» y «When These Walls Come Tumbling
  Down» (las páginas de episodio) para confirmar personajes y orden de
  escenas antes de citarlas — así identifiqué bien a Jinx, Marcus, Ren,
  Silco y el hex core sin adivinar por la imagen sola.
- **Dominios nuevos para las fuentes** (antes sólo tenía 6): probé Wikipedia
  (bloqueada con 429 «too many requests» las dos veces que la llamé, parece
  un límite compartido del contenedor — no insistí más), IMDb (403/202,
  verificación de humano tanto por `curl` como por `navegar.py`), Genius
  (403) y varias URLs adivinadas de recaps (ComicBook, Den of Geek,
  ScreenRant, IGN, Riot Games) que dieron 404 por no acertar la ruta exacta
  — las dejo anotadas para no repetir el intento. Lo que sí funcionó:
  **MusicBrainz** (ficha de «Enemy», ya la traía `datos-video.md`) y **la
  API de Reddit** (`arctic-shift.photon-reddit.com`, subreddit `arcane`) para
  el post viral de «Enemy start playing in the background» — dos dominios
  nuevos (`musicbrainz.org`, `reddit.com`) que se suman a los 6 de antes:
  ahora la parte cita 8 dominios distintos.
- Espacio: borré `enemy_overview/video.mp4`, `e05_overview/video.mp4`,
  `e05_fine`, `e05_demo`, `e06_overview/video.mp4` y los `.mp4` intermedios
  de `color/` al terminar cada descarga; sólo quedan las hojas JPEG y los
  4 fotogramas sueltos de `color/` en `/tmp/claude-0/trabajo/17-arcane-video/`.

### Bitácora de voz

**Repaso, sesión 2026-09-26.** Empecé por `partes/datos-voz.md` (ya lo
había juntado `recolectar.py`: ficha de Doblaje Wiki completa, reparto
latino, «datos de interés», textos de personalidad de Arcane Wiki,
ranking de Danbooru, hilos de Reddit, clips de Dailymotion) y por
`herramientas/seccion.py 17-arcane --rol voz` / `--avisos` para ver qué
ya estaba en `biblia.md` (puntos 7, 8, 12 y 13 ya trabajados por el
equipo «nueva»; **20, 21 y 22 no existían**).

- **Español**: «ANMTV Arcane doblaje latino reparto Netflix», «Miguel de
  León Jayce Arcane doblaje voz», «Arcane parodia meme español latino
  tiktok bombón/pastelito», «fandub Arcane español latino Jinx Vi escena»,
  «Arcane 인기 캐릭터 설문» (intento en coreano, sin resultado de encuesta).
- **Inglés**: «Art and Making of Arcane character height chart», «Jinx
  Arcane favorite food likes hobbies», «IMDb poll Arcane best character
  results», «Arcane Emmy Awards won 2022 2025», «Arcane Vander death
  scene episode reaction», «Arcane Isha death season 2 episode», «Arcane
  season 1 Rotten Tomatoes Metacritic Netflix hours», «Reddit Arcane I
  relate to Jinx Viktor», «Enemy Arcane cover español latino canal
  YouTube opening», «Jinx Arcane quote There is no Jinx / loose cannon».
- **Red directa** (no buscador): API de Doblaje Wiki
  (`doblaje.fandom.com/es/api.php`, ficha completa de Arcane) y de Arcane
  Wiki (`arcane.fandom.com/api.php`, ficha de Vander por
  `action=parse&prop=wikitext` para confirmar el apuñalamiento de Silco);
  `curl` directo a `comingsoon.net` y `desdelacuna.net` (reparto de
  doblaje por capítulo, independiente de Doblaje Wiki) — este último
  **cerró 4 ⚠️** del punto 8 (Jayce, Heimerdinger, Vander, Mel, Marcus).
  `elvortex.com` da 404 ahora (lo tiene Wayback, no llegué a usarlo).
- **`herramientas/fotogramas.py`**: tráiler oficial T1 en Dailymotion
  (`x85f7g5`, cada 6 s, 28 fotogramas, y 5 al detalle) y el episodio
  **1×03 completo** que ya tenía bajado el investigador de vídeo en
  `/tmp/claude-0/trabajo/17-arcane-video/` (Internet Archive,
  `arcane-season-1-60fps`, 1080p): saqué 3 fotogramas propios con emoción
  clara (Vi rabia 23:30, Powder tristeza 24:45, Powder miedo 27:15). No
  tuve que volver a bajar el vídeo: ya estaba en el disco compartido.
- **`herramientas/navegar.py`**: funcionó (200) en `tiktok.com`, pero dio
  **429** dos veces seguidas en `youtube.com/watch` — lo dejé, según pide
  `AYUDANTE.md` (no más de un reintento).
- **Doblaje Wiki, muestras de audio** (`herramientas/voz.py`): quedaron
  identificadas en `datos-voz.md` (Mel ×3, Viktor ×4, Silco ×1) pero **no
  llegué a correrlas**: es lo primero que dejo para quien siga.

**Relanzo, sesión 2026-09-26 (segunda vez, sólo la línea Sigue anterior).**
Bajé con `curl` (directo, no `yt-dlp`: la misma velocidad y sin depender de
que reconozca el formato) los episodios 1×01, 1×02, 1×03 (otra vez, ya no
estaba de la tanda pasada), 1×04, 1×07, 1×08 y 1×09 de
`archive.org/details/arcane-season-1-60fps` (720p, ~250 MB cada uno, unos
15-30 s por descarga) a `/tmp/claude-0/trabajo/17-arcane-voz/`. Con
`herramientas/fotogramas.py` saqué primero una hoja de contacto cada 45-60 s
de cada episodio completo (para ubicar la escena a ojo) y luego afiné con
`--desde/--hasta --cada 6-10` sobre el tramo bueno; miré (Read) cada hoja
antes de decidir. Encontré el **juicio de Jayce ante el Consejo** (1×02,
confirmado con la wikitext de `arcane.fandom.com/api.php?action=parse` de
«Jayce Talis», que cita 1×02 como el episodio del juicio) y comprobé que la
escena de Vander/Silco con Shimmer (que ya usé para Vi/Jinx en la tanda
pasada) es también donde está el primer encuentro de **Viktor** con Jayce
(cita en la wikitext de «Viktor») y donde **Silco** consuela a Powder y le
pone el nombre «Jinx» (cita en la wikitext de «Silco») — los tres estaban
en el mismo episodio 1×03, no hizo falta bajar más para ellos.
- **ffmpeg con `-ss` directo sobre la URL remota de archive.org** dio
  **403 Forbidden** (el proxy o el CDN de archive.org bloquea el acceso
  por rango sin las cabeceras de un navegador/curl completo): descarté esa
  vía y bajé el `.mp4` entero con `curl -L` en su lugar, que sí funcionó
  siempre a buena velocidad (curl sí manda las cabeceras que hacen falta).
- **Caitlyn** (1×08, min 22:18) y **Ekko** adulto (1×07, min 12:18) los
  encontré en escenas que no esperaba por el título del episodio: no busqué
  «la escena de Caitlyn» a ciegas, sino que miré la hoja de contacto entera
  y elegí el fotograma con cara clara y emoción legible.
- Intenté **Jinx adulta alegría** en 1×09 (min 19:00-23:00, pelea con
  guantelete morado): era **Sevika**, no Jinx — las confundí por el pelo
  oscuro en la hoja pequeña; lo anoto para no repetir el error. No bajé
  más tramos de 1×09 por tiempo.
- Intenté **Vi alegría/vergüenza** en 1×01 (rooftop del heist, min 5:40-9:30)
  y en 1×07 (mural de los Firelights, min 11:00-13:30): la primera es tensión
  de atraco, no alegría; la segunda es nostalgia con lágrimas, no alegría
  limpia. No encontré vergüenza de Vi en lo que miré.
- Los `.mp4` (7 episodios, ~1.7 GB en total) quedan en
  `/tmp/claude-0/trabajo/17-arcane-voz/e01.mp4` … `e09.mp4` — fuera del
  repositorio, listos para quien los necesite sin volver a bajarlos.

Sigue: punto 13, alegría y vergüenza de Vi, y alegría de Jinx (adulta) —ver fila «Vi» y «Jinx (adulta)» de la tabla de emociones—; probar en 1×09 (Jinx con las armas nuevas, «Get Jinxed») para la alegría de Jinx, y en 1×01 (tras el heist fallido, Vander regañando) o 1×08 (con Caitlyn) para Vi.

### Bitácora de texto

- (repaso) `dafont.com/arcane-nine.font` + descarga y comprobación con fontTools del `.otf` real → confirma licencia y tildes.
- (repaso) `deviantart.com/arcanafoundry/...Piltover-x-Zaun-Regular...` → descubre que es de pago (Shoptly), corrige la biblia.
- (repaso, inglés) "Beaufort" "Spiegel" Riot Games League of Legends official font brand → fontsinuse.com confirma autores y que son de pago.
- (repaso, inglés) free font alternative to Beaufort League of Legends UI google fonts → Cinzel confirmado como alternativa libre.
- Google Fonts API (`fonts.googleapis.com/css2?family=Barlow&text=...`) + fontTools sobre el `.ttf` real → Barlow con tildes/ñ/¿¡ completos.
- steampowered.com, fichas de los 6 juegos de `datos-texto.md` → descartados como falsos positivos (no son de la franquicia Riot).
- `wiki.play2xko.com` (2XKO Wiki, Jinx/Audio) → confirma formato de líneas de diálogo del juego de lucha.
- (inglés) "Legends of Runeterra Path of Champions Arcane story" → destructoid.com confirma el formato de «cómic animado» con caja de subtítulo.
- `web.archive.org` (Wayback Machine) de `riotxarcane.riotgames.com` → la API `archive.org/wayback/available` confirma que existe un snapshot (8-dic-2021), pero `web.archive.org` da «Blocked by egress policy» por `curl`, `navegar.py` y WebFetch: no pude leer el contenido archivado en este contenedor.
- `herramientas/fotogramas.py` sobre el tráiler de Path of Champions (YouTube) → pide inicio de sesión (bloqueo del servidor ya avisado en AYUDANTE.md); no encontré el mismo tráiler en Dailymotion ni Internet Archive.
- `wiki.play2xko.com/en-us/Jinx/Audio` leída completa → sólo transcripción de audio, sin captura del formato visual del subtítulo; corrijo mi primera afirmación para no darla por vista.
- `tcrf.net`, buscador interno "Arcane" y "RiotX Arcane" → sin resultados; League of Legends sí tiene página pero no cubre Arcane.
- (inglés) "Fortiche Arcane art style breakdown 3D painted textures interview making of" → syncsketch.com, 80.lv (dos artículos), redsharknews.com.
- (inglés) "Arcane Fortiche Blender Maya pipeline shader interview" → confirma Maya + Photoshop + Nuke + After Effects (redsharknews.com), no Blender en el pipeline real del estudio (por eso el punto 18 distingue «lo que usó el estudio» de «cómo reproducirlo con herramientas libres/Photoshop y Blender»).
- (inglés) "Arcane 12fps hand-drawn effects vs 24fps character animation staccato frame rate" → confirma la mezcla de fps.
- (inglés) "Arcane cinematography camera framing composition analysis emotion" → formeinfullbloom.wordpress.com ("The Anicamera in Arcane").
- (inglés) "Fortiche Production Gorillaz Saturnz Barz" y "...Tranz" → **descubro que mi primer dato estaba mal** (esos vídeos son de Passion Pictures y Blinkink, no de Fortiche); corrijo buscando la web oficial del estudio.
- `forticheprod.com/fortichize/` (leída completa con WebFetch) → lista real de trabajos previos de Fortiche: Get Jinxed, Warriors, Rise, KDA-POP/STARS, Enemy, Blood Sweat & Tears, Welcome to Noxus, un vídeo de Gorillaz (sin nombre).
- (inglés) "Christian Linke Alex Yee influences animation interview" → sin resultado directo, descarto la hipótesis de Genndy Tartakovsky.
- (coreano) 아케인 제작 기법 인터뷰 · (japonés) アーケイン 制作 技法 インタビュー → sin entrevistas técnicas, sólo doblaje.
- `arcane.fandom.com` (wikitext, vocabulario: Shimmer, Chem-Barons, Hexcore, Firelights, Undercity, Gray, Enforcers) vía API `action=parse&prop=wikitext` en las páginas Piltover y Zaun; confirma los campos `symbol` y `crest` exactos de cada ciudad y corrige mi primera suposición sobre los emblemas.
- `arcane.fandom.com/api.php?action=query&list=search` para "Chembaron" y "Firelights emblem": confirma el término y que no hay campo de emblema documentado para los Firelights ni ficha de la casa Kiramman.
- (inglés) "Arcane episode ACT I title card screenshot font" → madegooddesigns.com (leída completa): tipo de letra de cartelas sin nombre exacto; descubro y descarto una afirmación falsa de «Sharp Sans ExtraBold» que salió en el resumen automático del buscador pero no está en la página real.
- Google Fonts API + fontTools sobre `Cardo`, `Almendra Display`, `EB Garamond`, `Cinzel Decorative` (.ttf reales) → los cuatro con tildes/ñ/¿¡ completos.
- `arcane.fandom.com/api.php?action=parse&prop=wikitext` en Piltover y Zaun (campos `symbol`, `crest`) + tamaños de `Piltover Crest.png` (4042×4167) y `Zaun Crest.png` (3487×4167) por `action=query&prop=imageinfo`.
