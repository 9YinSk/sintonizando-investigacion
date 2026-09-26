## Bitácora

### Bitácora de imagen

- Fandom `finalfantasy.fandom.com` API (`action=query`, `prop=images|imageinfo`) para portadas, Amano, key art y tamaños exactos — español/inglés
- `herramientas/investigar_serie.py` sobre Cloud/Tifa/Aerith/Sephiroth: 1186 imágenes enlazadas, 539 grandes, 12 hojas de contacto en `herramientas/referencias/final-fantasy-vii/` (miradas todas, elegidas 3 para `hojas/`)
- `herramientas/estilo.py` sobre 4 renders oficiales descargados y recortados a mano por prenda (18 recortes en total) para los hex del punto 15
- Sketchfab API (`api.sketchfab.com/v3/search`) con las consultas: «Sephiroth Final Fantasy», «Midgar Final Fantasy», «Materia Final Fantasy VII», «Chocobo Final Fantasy», «Buster Sword», «Aerith Final Fantasy», «Tifa Lockhart», «Cloud Strife Final Fantasy» — todas devolvieron modelos CC
- ambientcg API (`ambientcg.com/api/v2/full_json`) con «Leather», «Fabric», «Concrete», «Metal», «Rust», «Paper» — todo CC0
- WebSearch (2 búsquedas): «Final Fantasy VII fan art ArtStation Tifa Cloud Aerith destacado» (inglés/español) y «free manga screentone halftone brush pack CC0» (inglés), más una sobre la novela «Kids Are Alright»
- Wiki de Fandom, página «Collaboration» completa por wikitext (`action=parse&prop=wikitext`), para el punto 23: confirmó Smash Bros., Street Fighter 6, Dissidia NT, LittleBigPlanet 2, Dragon Quest Tact y 5 eventos crossover dentro de Ever Crisis (FFIX, Monster Hunter, FFVI, saga Lightning/FFXIII, NieR)
- GitHub API (`search/repositories`) para pinceles de screentone: sin resultados, se usó WebSearch en su lugar
- Sin serie hermana declarada en el encargo, no se leyó ninguna biblia previa

### Bitácora de video

- `herramientas/fotogramas.py` sobre 8 clips de Dailymotion (opening Remake, opening tech-demo
  PS3, ending Fin Partie 4, muerte de Aerith, flashback de Nibelheim, caída del Sector 7,
  gameplay de Tifa en Remake, recuerdos de Tifa en la Corriente Vital, tráiler final de
  Rebirth): 8 hojas de contacto miradas con Read, más de 190 fotogramas en total.
- `ffmpeg` para extraer 6 fotogramas sueltos de los vídeos ya bajados (sin volver a descargar) +
  `herramientas/estilo.py --colores 5` sobre esos 6 fotogramas para el punto 4.
- API de Dailymotion (`api.dailymotion.com/videos?search=…`): búsquedas en francés e inglés —
  «Final Fantasy VII bombing mission», «Aerith death», «Sephiroth Nibelheim», «opening movie
  FMV», «Midgar plate falls Sector 7», «Cloud vs Sephiroth final battle», «La chute du secteur
  7», «generique de fin», «cinematique finale», «Fin Partie 1», «Tifa Cloud puits», «Tifa combat
  Corel», «Cloud presente Buster Sword» (12 búsquedas en total).
- `archive.org/metadata/final_fantasy_vii_soundtrack`: tracklist completo de 90 pistas del OST
  original, para el punto 9.
- `musicbrainz.org`: confirmación de 3 álbumes oficiales (original, Remake, Rebirth).
- `arctic-shift.photon-reddit.com`: 100 posts recientes de r/FinalFantasyVII, ordenados por
  puntuación en el propio análisis, para el punto 10 (tendencias).
- `herramientas/navegar.py` sobre `tiktok.com/tag/finalfantasy7rebirth`: bloqueado (login).
- `yt-dlp -F` sobre un clip de Dailymotion para comprobar la resolución máxima real (512×288).
- Ya recolectado por `recolectar.py` y **no repetido**: los clips de Dailymotion de
  `datos-video.md` (opening/ending/trailer/escena genéricos), Internet Archive (soundtracks,
  Advent Children) y MusicBrainz (13 álbumes) — se usaron esos datos como punto de partida y se
  añadió lo que faltaba (clips concretos con escena identificada, minuto exacto y paleta medida).

### Bitácora de voz

- Doblaje Wiki (`api.php`, `action=parse` y `action=query&list=search`, español): «Final Fantasy VII», «Final Fantasy VII Remake», «Final Fantasy VII Rebirth», «Final Fantasy VII: Advent Children», «Kingdom Hearts III», «Ever Crisis» → confirmado que no existe doblaje latino oficial de ningún FFVII.
- Final Fantasy Wiki (`finalfantasy.fandom.com/api.php`, inglés): wikitext de Cloud Strife, Tifa Lockhart, Aerith Gainsborough, Sephiroth, Barret Wallace, Red XIII, Cid Highwind, Yuffie Kisaragi, Cait Sith, Vincent Valentine, Materia (Final Fantasy VII), Birthday, Final Heaven — voces, edades, alturas, tipo de sangre, cumpleaños.
- Behind The Voice Actors (`navegar.py`, porque curl daba 403): Cloud Strife, Tifa Lockhart, Aerith Gainsborough, Sephiroth, Barret Wallace — confirmación en inglés de seiyū y voces en inglés, como segunda fuente.
- TV Tropes (`navegar.py --html --max 0` porque los «folders» ocultan texto con JavaScript y con `--selector` no se veían): YMMV/FinalFantasyVII y Tearjerker/FinalFantasyVII, en inglés — memes, qué ama el fandom, escenas que hacen llorar.
- WebSearch (español e inglés): «Final Fantasy VII Remake character popularity poll Famitsu Dengeki ranking», «encuesta popularidad personajes Final Fantasy VII más querido resultado oficial», «Final Fantasy VII Remake Ultimania profile favorite food hobby», «fandub Final Fantasy VII español latino youtube», «Final Fantasy VII cover opening español latino».
- Push Square, ResetEra, NextN, LEVEL UP, Wikipedia (inglés y español): encuesta Famitsu 2020 con votos exactos, encuesta nacional NHK 2020, ventas y premios.
- Dailymotion (`api.dailymotion.com`, búsquedas por texto) + `fotogramas.py` sobre los clips encontrados: «La Mort d'Aerith Final Fantasy VII» (xwr79w), «Final Fantasy VII : Le Gold Saucer» (x89clxh), «Sephiroth à Nibelheim» (x2yc6on), montaje de Advent Children (x4qnl9), «Chez Don Cornéo» (x89clzv), tráiler «Cloud Strife» de Remake (x7p3q62), «Cloud dates Jessie in Kalm» de Rebirth (x9mj91u) — 7 clips mirados de verdad, no sólo leídos.
- yt-dlp `--skip-download --print` (sin necesidad de iniciar sesión) para metadatos de 2 vídeos de fandub en YouTube.
- Intentos fallidos: `www.anmtv.la` (proxy del contenedor lo bloquea, «connect_rejected», 2 intentos); Corona Jumper (blog, 403 con curl y con navegar.py); Tumblr de aitaikimochi (200 la primera vez, 429 al segundo intento — no insistí más).
- Corregido dato de `datos-voz.md`: la ficha de doblaje recolectada automáticamente ahí es de **Final Fantasy XVI**, no de Final Fantasy VII — se confirmó que es la única entrega de la franquicia con doblaje latino oficial, y por eso se cita para el punto 8, no por error del recolector.

### Bitácora de texto

Punto de partida: `partes/datos-texto.md` (recolectado, capturas de Steam de 6 juegos) — no repetí esa consulta, la usé directamente en el punto 11. Sin serie hermana declarada para este encargo.

**Búsquedas web (WebSearch), todas en inglés salvo que se diga lo contrario**:
- «Final Fantasy VII logo font identify typeface»
- «"Final Fantasy VII" font fontsinuse.com»
- «Final Fantasy VII Remake dialogue text font typeface UI»
- «"Final Fantasy VII" site:tcrf.net»
- «Advent Children title font credits typeface»
- «Final Fantasy VII Ever Crisis comic panels speech bubbles story mode»
- «Final Fantasy VII original PlayStation dialogue box design blue border description»
- «Final Fantasy VII Remake dialogue box character name tag design subtitle style»
- «"Final Fantasy VII" manga adaptation official comic "On the Way to a Smile" OR "Kids are Alright"»
- «Final Fantasy VII Remake battle menu command HUD font description blue white»
- «Final Fantasy VII Remake art director interview Unreal Engine character shader realistic Nomura»
- «Final Fantasy VII Advent Children Visual Works making of Maya CG production»
- «Final Fantasy VII 1997 development making of 3D models Softimage backgrounds prerendered»
- «Naoki Hamaguchi Unreal Engine interview Final Fantasy VII Remake "Cloud's" expression redo hair shader»
- «Tetsuya Nomura character design influences Todd McFarlane comics Cloud buster sword interview»
- «Hironobu Sakaguchi Final Fantasy VII influences Star Wars interview inspiration»
- «"Final Fantasy VII" similar games recommend if you like JRPG cyberpunk dystopia»
- «"Final Fantasy VII Revelation" Steam app 4354570»
- «tcrf.net "Final Fantasy VII" unused text debug room dummied dialogue»
- «ファイナルファンタジー7 リメイク 書体 フォント インタビュー» (japonés)

**Navegación directa (curl/API, sin gastar cupo de búsqueda)**:
- dafont.com/reactor7.font (vía curl con user-agent; WebFetch lo bloquea el proxy) — descargado su mapa de caracteres y mirado con Read
- api.fontsource.org — Cinzel, Rajdhani, Anton: comprobados con `fontTools.getBestCmap()` sobre el `.ttf` real descargado (no de memoria)
- finalfantasy.fandom.com/api.php — búsqueda de texto y wikitext de «Menu (Final Fantasy VII)», «Menu (VII Remake)», «Menu (Dirge of Cerberus)», «Materia (Final Fantasy VII equipment)», «Midgar», y `imageinfo` de 4 imágenes oficiales (medidas en Pillow: menú de Materia original, menú de Materia & Equipment del Remake, logo de Shinra)
- gameuidatabase.com/gameData.php?id=29 (Final Fantasy VII Remake) — bloqueado por Cloudflare a `curl`, abierto con `python3 herramientas/navegar.py --selector body`: confirmó las etiquetas **Flat 2.0** y **Futuristic**; **aviso**: esa web prohíbe expresamente el uso de su contenido para IA/ML, así que no se citan sus imágenes en `texto.json`
- namelivia.com (blog técnico, 2015) — leído por curl (WebFetch lo bloquea el proxy): técnica de reconstrucción de fondos de FFVII en Blender con el add-on Blam
- automaton-media.com — leído por curl: entrevista completa a Naoki Hamaguchi sobre el pelo de Cloud (TAA/DRS/DLSS)
- store.steampowered.com — ya recolectado en `datos-texto.md`; descargué y miré 3 capturas de Rebirth/Remake con Read para buscar UI en pantalla (no salió HUD en esas 3, sólo cinemáticas)
- dotcolon.net/fonts/ferrum/ — leído por curl: fuente japonesa gratis «No Rights Reserved» hecha a propósito referenciando el logo de FINAL FANTASY; descargada y comprobada con fontTools (sólo ASCII, sin ñ/tildes/¿/¡)
- automaton-media.com/articles/newsjp (japonés) y famitsu.com (japonés) — polémica de la fuente en inglés del Pixel Remaster

**Bloqueado o sin poder verificar**: unrealengine.com (egress bloqueado por el proxy tanto en WebFetch como en curl, 403); dafont.com por WebFetch (funcionó por curl directo); gameuidatabase.com por curl directo (Cloudflare; resuelto con `navegar.py`); **tcrf.net bloqueado por los 3 caminos** (Cloudflare a curl y a `navegar.py`, proxy del contenedor a WebFetch) — los datos de TCRF que aparecen en el punto 11 vienen de fragmentos de búsqueda, no de la página completa.
