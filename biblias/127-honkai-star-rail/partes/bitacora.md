## Bitácora

### Bitácora de imagen

- 2026-09-26 · `herramientas/recolectar.py 127-honkai-star-rail --hojas` (previo, ya en datos-imagen.md): AniList no aplica (es videojuego), Doblaje Wiki no encontró la página, Fandom no encontró «el Trazacaminos» (el nombre correcto en la wiki en inglés es «Trailblazer»).
- 2026-09-26 · `investigar_serie.py --serie "Honkai: Star Rail" --wiki honkai-star-rail --paginas "March 7th" "Kafka" "Trailblazer" "Stelle" "Firefly"`: 232 imágenes enlazadas, 32 grandes, 1 hoja de contacto (`hojas/personajes_01.jpg`) → mirada con Read.
- 2026-09-26 · Fandom API (`action=query&list=search`, `prop=images`, `prop=revisions`, `list=categorymembers`) en inglés: aniversarios, banners, trajes alternativos, categorías de colaboraciones y de emblemas de Camino/mundo.
- 2026-09-26 · Pillow/`estilo.py` sobre recortes de torso de los retratos «Game» (sin fondo de UI) para el hex de la ropa, no del fondo; y sobre 5 imágenes de área (`Area *.png`) para el hex y la luz de los sitios.
- 2026-09-26 · Sketchfab API (`type=models&downloadable=true`): «Astral Express», «Honkai Star Rail train», «Honkai Star Rail Herta», «Honkai Star Rail Acheron», «Honkai Star Rail March 7th» → 11 modelos con licencia usables.
- 2026-09-26 · ambientCG API (`type=Material`): «fabric», «metal plate», «paper», «gold» → 4 texturas CC0 elegidas por parecido a los materiales vistos.
- 2026-09-26 · Búsqueda web (inglés): «Honkai Star Rail collaboration KFC brand crossover», «Honkai Star Rail official figure statue Kafka», «"Honkai Star Rail" collaboration list Alienware Razer OPPO», «Honkai Star Rail official wallpaper download» → colaboraciones, figura oficial, wallpapers de HoYoLAB.
- 2026-09-26 · Montaje propio con Pillow de una 2.ª hoja de contacto (`hojas/vestuario_fondos_01.jpg`, 10 recortes: vestuario + fondos + colaboraciones) para mirar todo junto.

### Bitácora de video

- `api.dailymotion.com/videos?search=...` (inglés): "Honkai Star Rail Kafka", "Honkai Star Rail March
  7th", "Honkai Star Rail Trailblazer character demo Stelle Caelus", "Honkai Star Rail Launch Trailer",
  "Honkai Star Rail animated short Astral Express", "Honkai Star Rail Penacony trailer", "Honkai Star
  Rail Xianzhou Luofu trailer", "Honkai Star Rail lore explained analysis" — todas devolvieron
  resultados, elegidos los oficiales/repostados por medios reconocibles (JeuxVideo.com, Gamekult,
  GRYOnline.pl, ActuGaming, 3djuegos, WatchMojo).
- `herramientas/fotogramas.py` sobre 8 vídeos de Dailymotion (opening_cutscene, opening_3_0,
  march7th_trailer, kafka_trailer, trailblazer_trailer descartado, reveal_trailer, penacony, xianzhou) +
  4 fotogramas sueltos con `--fotograma` para medir color.
- `herramientas/estilo.py --colores 5` sobre 5 fotogramas propios (Herta, Belobog, Penacony, Xianzhou,
  Amphoreus).
- `honkai-star-rail.fandom.com/api.php` (inglés): wikitext de `Pom-Pom` y de `Trailblazer`, búsqueda de
  categoría `Sound Effects`, búsqueda de texto "soundtrack" y "warp jump sound".
- `soundeffects.fandom.com/api.php`: página de Honkai: Star Rail sin contenido útil (plantilla vacía).
- `ambientcg.com/api/v2/full_json` (texturas CC0): "marble", "metal plate".
- WebSearch (inglés): "Honkai Star Rail most emotional scene players cried March 7th identity reveal 2.7
  song" (sin resultado concreto), "Honkai Star Rail iconic sound effects Pom-Pom bell warp jump gacha
  onomatopoeia" (parcial), "Honkai Star Rail TikTok trend viral 2025 2026 dance edit meme" (✅, dio el
  trend de Evernight).
- `herramientas/navegar.py` (TikTok bloquea curl): página de tendencia
  `tiktok.com/en/trending/detail/honkai-star-rail-animation-dancing-evernight` con `--espera 4000`.
- `arctic-shift.photon-reddit.com/api/posts/search` (Reddit r/HonkaiStarRail_, "OST"): sin datos
  utilizables, no insistí.

### Bitácora de voz

- Doblaje Wiki (api.php, español): `action=query&titles=Honkai:%20Star%20Rail` → `missing`; `action=query&list=search&srsearch=Honkai`/`Star Rail`/`intitle:Honkai` → sin página propia de la obra; ficha de Jeannie Hernández (traductora) sí la menciona.
- Honkai Star Rail Wiki (Fandom, inglés): wikitext de `March 7th`, `Kafka`, `Trailblazer`, `Firefly` y sus subpáginas `/Lore` y `/Voice-Overs`; `allpages?apprefix=` para mapear subpáginas de cada personaje.
- WebSearch (inglés): «Honkai Star Rail voice language Spanish text only official languages list» → confirma EN/JP/CN/KR de voz y ES sólo texto (Prima Games, DigiStatement).
- WebSearch (inglés): «Honkai Star Rail popularity poll fan favorite character HoYoLAB» y «personaje más popular encuesta 2025» → encuesta oficial china de mayo 2025 (HoYoLAB + X/StarRailVerse1).
- WebSearch (español): «Honkai Star Rail fandub español latino youtube personaje» y «Kafka Honkai Star Rail fandub español latino voz» → canales Honkai Spanish Dubs y ALANREQUIEM DUBS, vídeos de Ying Yuan y Caelus.
- Dailymotion API: búsquedas de tráiler de personaje («Kafka character trailer», «March 7th character trailer», «Trailblazer trailer») → tráilers oficiales «Ironía Dramática» (Kafka), «Bande-annonce de March 7th», «The Deliverer» (Trazacaminos).
- `fotogramas.py` sobre los 4 tráilers anteriores (cada 6-8 s) → hojas de contacto miradas con Read; fotogramas citados en el punto 13.
- Arctic Shift (Reddit r/HonkaiStarRail): `query=cried`, `made me cry`, `saddest scene`, `silent protagonist`, `Evernight reveal`, `cringe` → hilos usados en los puntos 12 y 21.
- `navegar.py` sobre HoYoLAB (`hoyolab.com/article/40440025`): la página no renderiza contenido sin sesión (queda en «Cargando…»); me apoyé en el resumen de X/StarRailVerse1 y en Sportskeeda (bloqueado por captcha) para la encuesta.
- (Tanda «seguir») Dailymotion API: `search=Honkai Star Rail Astral Express opening cutscene` → confirmó que x8bbisq es la cinemática de apertura oficial (69 s); `fotogramas.py --cortes` sobre x8n3btc, x90j8pu, x8a7le6 y x8bbisq (contactos de 25-85 planos cada uno, mirados con Read) para buscar rabia/tristeza/miedo/vergüenza del punto 13.
- No usé más de dos intentos por web bloqueada (regla de AYUDANTE.md): X/Twitter dio 403 directo con navegar.py, así que no insistí más ahí.

### Bitácora de texto

- Fandom `honkai-star-rail.fandom.com` vía API (`action=parse`, `action=query&list=search`): páginas Typeface, Universal Script, Aeon, Stellaron, Path, Data Bank, Chat Box, Trailblaze Mission, e íconos de facción con tamaño real (`imageinfo`). En inglés.
- `honkaiimpact3.fandom.com` vía API: página Alien Space (cómic oficial). En inglés.
- TV Tropes (`tvtropes.org`) con `herramientas/navegar.py` (bloqueaba a curl): páginas VideoGame/HonkaiStarRail y ShoutOut/HonkaiStarRail completas. En inglés.
- `tcrf.net` con `navegar.py`: 403 dos veces (verificación Cloudflare); no insistí más, según la regla de dos intentos.
- WebSearch (inglés): arte y cel-shading, motor gráfico, Trails/Persona 5/Disco Elysium, franquicia Honkai, Cutting Room Floor, fuente china/japonesa. ~10 búsquedas.
- `manga.honkaiimpact3.com` y ONE Esports (`oneesports.gg`) con `navegar.py --selector`: hubo que probar varios selectores (`article`, `main`, `.entry-content`) hasta dar con el que traía texto.
- GitHub (`raw.githubusercontent.com`, `api.github.com`): READMEs de `stalomeow/StarRailNPRShader` y `festivities/Blender-StellarToon` (shaders fan-made que replican el estilo, licencias MIT/GPL-3.0).
- Fontsource API (`api.fontsource.org`): descarga real de Titillium Web y Exo 2, comprobados con `fontTools.ttLib.TTFont.getBestCmap()` (ñ, Ñ, á, é, í, ó, ú, ü, ¿, ¡ presentes en ambos).
- Steam: `store.steampowered.com` no tiene ficha del juego (no está en Steam); confirmado con `storesearch` (0 resultados) y una búsqueda web.
