## Bitácora

### Bitácora de imagen

- `herramientas/investigar_serie.py --serie "Elden Ring" --wiki eldenring --paginas Melina "Malenia, Blade of Miquella" "Ranni the Witch" "Starscourge Radahn"`: ya lo había corrido `recolectar.py` (indice.json con 247 imágenes); yo sólo regeneré las 6 hojas de contacto que faltaban (el intento anterior se cortó tras la nº1) reusando el mismo índice, sin repetir las consultas a la wiki.
- Miré las 6 hojas de contacto completas con Read antes de citar nada (247 imágenes en total).
- API de Sketchfab (`api.sketchfab.com/v3/search`): `q=elden ring castle` (0 resultados útiles), `q=erdtree` (Marika's hammer, Rellana, Bayle, Tree Sentinel, Blue Blossom), `q=elden ring ruins` (Old Church Ruins). En inglés.
- API de Poly Haven (`api.polyhaven.com/assets?t=models&c=nature`): filtrado por nombre para ruinas/raíces/piedra → `dead_tree_trunk`, `root_cluster_01`, `stone_01`. En inglés.
- API de ambientCG (`ambientcg.com/api/v2/full_json`): `q=stone`, `q=bark`, `q=fabric`, `q=paper`, `q=gold` (con resultados); `q=weathered stone`, `q=rusty metal`, `q=gold ornate` (sin resultados, probablemente por espacios en la query). En inglés.
- API de la wiki (`eldenring.fandom.com/api.php?action=query&prop=pageimages`) para panorámicas de Limgrave, Liurnia, Caelid, Leyndell y Haligtree, bajadas después con `curl` + cabecera Referer y medidas con `estilo.py`.
- Descargas directas de `static.wikia.nocookie.net` con `curl -A "Mozilla/5.0" -e "https://www.fandom.com/"` (sin el Referer da 403, como avisa AYUDANTE.md).
- `herramientas/estilo.py` sobre 11 imágenes propias (Melina, Malenia armadura/key art, Radahn armadura, 5 panorámicas de región, estatua de Haligtree, arte del asedio de Aeonia): paletas y tipo de sombreado para los puntos 15, 16 y 19.
- WebSearch (cupo compartido, en inglés): `free screentone halftone brush pack CC0 license download manga`, `Elden Ring official collaboration merchandise crossover cafe figure 2025 2026`, `"Elden Ring" x collaboration crossover brand event official announcement`, `Malenia Elden Ring cosplay armor build reddit instagram`. 4 búsquedas de las ~50 del cupo.
- `herramientas/navegar.py https://tamashiiweb.com/item_character/eldenring/?wovn=en --selector body`: confirmó las 3 figuras oficiales S.H.Figuarts/Figuarts mini (Bandai/TAMASHII).
- GitHub API de búsqueda: bloqueada en este contenedor («sessions are bound to their configured repositories»); no pude buscar shaders/rigs por ahí, sólo por Sketchfab y Poly Haven.
- Arctic Shift (Reddit) a r/cosplay con «Malenia»: dio timeout una vez; no insistí más (regla de máximo 2 intentos).
- Openverse (`api.openverse.org`) con `q=halftone texture`: sólo trajo fotos con licencia CC de fotógrafos, no packs de pinceles; usé Brusheezy en su lugar (licencia de plataforma, marcado ⚠️).

### Bitácora de video

- `herramientas/fotogramas.py` sobre 8 clips (7 de Dailymotion: tráiler narrativo, Malenia, Radahn, Rennala, final del juego en francés, exploración de Limgrave, «The Melina Accord»; 1 de Internet Archive: compilado de los 4 finales a 720p): 8 hojas de contacto miradas con Read.
- `herramientas/estilo.py --colores 5` sobre 12 fotogramas sueltos (Limgrave, Caelid, Raya Lucaria, Leyndell dorado, Leyndell ceniza, cielo de Ranni, muro de fuego, Elphael, ruinas, Erdtree) para el punto 4.
- `herramientas/navegar.py` sobre `tiktok.com/tag/eldenring` y `tiktok.com/search?q=elden+ring`: página vacía las dos veces (bloqueo sin sesión).
- `yt-dlp -F` sobre un clip de Dailymotion para comprobar la resolución máxima real (512×288).
- API de Dailymotion (`api.dailymotion.com/videos?search=…`): «Elden Ring Melina» (fr/en), «Elden Ring opening cinematic» (en), «Elden Ring cinématique d'ouverture» (fr), «Elden Ring Tarnished grace cinematic» (en) — 4 búsquedas.
- Archive.org: metadata de la banda sonora oficial (tracklist completo, 2 discos) y de «PS5 Longplay Elden Ring» (comprobado pero descartado por peso).
- MusicBrainz: confirmación de los 3 álbumes oficiales de banda sonora (base + Shadow of the Erdtree + Nightreign).
- Tanda anterior no usó WebSearch/WebFetch: todo salía de `datos-video.md` más red directa (Dailymotion, Archive.org, MusicBrainz), sólo 3 dominios. Esta tanda (`seguir`, tras aviso de `revisar_partes.py`: «FLOJA: 3 webs») se añadieron 5 dominios más: `eldenring.fandom.com` (vía `api.php`, dos páginas: Malenia y Melina), `eldenring.wiki.fextralife.com`, `es.wikipedia.org`, `en.wikipedia.org` y `3djuegos.com`.
- IGN (`ign.com`), Vandal (`vandal.elespanol.com`), PCGamer (`pcgamer.com`) y GameSpot (`gamespot.com`) probados con `WebFetch`: 403/404 en todas las URLs intentadas (bloqueo o artículo movido); no insistido más de 1-2 intentos por sitio.
- VGMdb probado con `WebFetch` y con `herramientas/navegar.py`: verificación de seguridad Cloudflare (403) las dos veces.

### Bitácora de voz

Punto de partida: `partes/datos-voz.md` (Danbooru, Dailymotion, Reddit r/Eldenring ya recolectados automáticamente) — no repetí esas consultas, sólo las usé y las amplié.

**Búsquedas (WebSearch), con idioma:**
- «Famitsu エルデンリング 人気投票 キャラクター ランキング» (japonés) → artículo oficial con los dos rankings (NPC y enemigo/jefe).
- «Elden Ring character popularity poll official ranking» (inglés) → confirmación en GameSpot, PCGamesN, Kakuchopurei.
- «"Ranni" popular NPC Famitsu survey "Alexander" "Blaidd" ranking Elden Ring» (inglés) → cifras exactas de votos.
- «Elden Ring idiomas de voz audio español latino doblaje» (español) → confirma que sólo hay fandubs, no oficial.
- «Elden Ring Steam supported languages "full audio" list English Japanese French German» (inglés) → lista oficial de idiomas.
- «site:anmtv.es Elden Ring doblaje» (español) → sin resultados directos, pero confirma título de vídeo «no tendrá doblaje».
- «Elden Ring 日本語音声 吹き替え 収録 声優» (japonés) → confirma que tampoco hay doblaje japonés, sólo inglés.
- «"Martha Mackintosh" Melina Elden Ring voice actress» / «"Pippa Bennett-Warner" Malenia Elden Ring voice actress» (inglés) → segunda fuente (IMDb) para el reparto.
- «Elden Ring artbook Melina Malenia height stats official profile» (inglés) → confirma que NO hay databook oficial (dato negativo verificado).
- «Elden Ring Game Awards 2022 Game of the Year sales million copies» (inglés) → premios y ventas.
- «Elden Ring saddest scene reddit "made me cry" ending» (inglés) → hilos de Steam/Reddit con reacciones.
- «Gurranq Bestial Clergyman howls direction Erdtree sad detail Elden Ring» (inglés) → detalle de fandom confirmado en dos wikis.
- «"Elden Ring" Fia embrace scene emotional most touching moment players» (inglés) → Kotaku + ScreenRant.
- «Malenia scarlet rot chronic illness disability representation fans relate reddit» (inglés) → identificación del público con el personaje.
- «Elden Ring fandub español latino canal youtube capitulos serie animada» (español) → canales Offline Player, ZaroDubs.
- «Elden Ring meme hispano parodia tiktok español "el juego que"» (español) → TikTok @manu_partida, @zequiodzilla, Memedroid.
- «Elden Ring canción tributo rap español "Tarnished" OR "Sin Luz" videojuego cover» (español) → raps tributo (Tirow, Keyblade).

**Red directa (sin buscador), con resultado:**
- `curl` a `https://www.famitsu.com/news/202205/07260652.html` (200 OK) → texto completo de la encuesta, números exactos extraídos con Python, no de memoria.
- `curl` a Doblaje Wiki API (`action=query&list=search&srsearch=ELDEN`) → confirma que no existe página de Elden Ring en el catálogo de doblaje latino.
- `curl` a `win.gg` y `gamepur.com` → confirmación de idiomas oficiales (sólo inglés con audio completo).
- `navegar.py` sobre `behindthevoiceactors.com/video-games/Elden-Ring/` (bloqueaba a curl con 403) → reparto completo en inglés, créditos oficiales, verificado también en IMDb.
- `api.dailymotion.com` (varias búsquedas: trailer oficial, Melina ending, Malenia intro, Fia embrace/champions) → clips usados con `fotogramas.py`.
- `fotogramas.py --cortes` sobre el tráiler de historia oficial (Dailymotion x8837gv, 6:29, 211 planos, mirado entero) → fotogramas de Melina con minuto exacto.
- `fotogramas.py --cada 15` sobre el combate oficial contra Malenia (Dailymotion x89wlj1, 4:16) → fotogramas de la transformación Flor Escarlata.
- `fotogramas.py --cada 6/12` sobre dos clips de Fia (uno resultó ser animación de fans, se descartó; el otro es gameplay real).
- `eldenring.fandom.com/api.php` (action=parse, prop=wikitext) → fichas completas de Melina, Malenia y Ranni, con citas literales de diálogos.
- `navegar.py` sobre el hilo de Reddit de `datos-voz.md` con más votos (5319, título «Why does fandom love her so much?») → leí el cuerpo real del post (reddit.com bloquea curl con 403, y la API de Arctic Shift dio timeout): resultó ser sobre **Sellen**, no sobre Malenia como parecía por el título; corregido en el punto 21 en vez de asumir de memoria.

**Fuentes consultadas (resumen, con enlace ya citado arriba en Hallazgos):** Famitsu, GameSpot, PCGamesN, Kakuchopurei, itmedia nlab, Danbooru, win.gg, Gamepur, Steambase, Doblaje Wiki (API), Behind The Voice Actors, IMDb, Wikipedia (Elden Ring, Malenia, Pippa Bennett-Warner, Martha Mackintosh), Eldenring Fandom wiki (Melina, Malenia, Ranni, Gurranq), Kotaku, ScreenRant, Video Games Chronicle, Anime News Network, The Game Awards (Wikipedia), Reddit r/Eldenring (vía datos-voz.md), Dailymotion (tráiler oficial + combate Malenia + Fia), YouTube (títulos vía WebSearch, no reproducidos), TikTok, Spotify, Memedroid.

### Bitácora de texto

- Búsquedas en inglés (WebSearch): "Elden Ring font identify UI text typeface", "Elden Ring logo font name", "Elden Ring dialogue box NPC font reddit", "site:tcrf.net Elden Ring", ""Elden Ring" fontsinuse.com", "Elden Ring UI design breakdown item pickup banner boss name", "Elden Ring "The Road to the Erdtree" manga Daisuke Izuka" (nombre de autor equivocado en mi hipótesis inicial; corregido a Nikiichi Tobita), "Elden Ring Miyazaki Berserk Kentaro Miura influence interview", "Elden Ring Kimihiko Fujisaka character design interview" (hipótesis descartada: Fujisaka no trabajó en Elden Ring), "Elden Ring art director Masanori OR concept art book official artbook", "Elden Ring game engine proprietary FromSoftware not Unreal", "Elden Ring Shadow of the Erdtree Scadutree fragment UI Rune Arc", "Elden Ring similar games soulslike Lies of P Lords of the Fallen Wo Long", "Elden Ring Great Runes list demigods symbols...", "Elden Ring story arcs Shattering timeline lore summary Marika Erdtree".
- Búsquedas en japonés: "エルデンリング フォント 書体 タイトルロゴ" (tipografía del logo).
- Búsquedas en coreano: "엘든링 폰트 한글 서체" (fuente coreana del juego).
- Webs abiertas con `navegar.py` (headless, sitios que bloquean curl): `dafont.com/forum` (✅ funcionó), `tcrf.net` (❌ 403 Cloudflare, sin pasar la verificación), `frontlinejp.net` (❌ 202/cookies, sin pasar la verificación), `gameuidatabase.com` (✅ funcionó, dos páginas: Elden Ring y Nightreign).
- Fandom API (`eldenring.fandom.com/api.php`): búsqueda de páginas de Grandes Rúnicas, `prop=images` + `prop=imageinfo&iiprop=url|size` para sacar tamaño real de los iconos de Godrick y Malenia, y la portada del manga tomo 1.
- `fontTools` (`TTFont(...).getBestCmap()`): comprobación real de á/é/í/ó/ú/ñ/Ñ/¿/¡/ü en 5 fuentes libres descargadas de Fontsource/Google Fonts (Cinzel, Cormorant Garamond, EB Garamond, Spectral, IM Fell English) — el primer intento (subset "latin-ext") dio falso negativo en las 4 primeras; repetido con el subset correcto "latin" y las 5 pasaron completas.
- `herramientas/estilo.py`: paleta y tipo de sombreado medidos sobre una de las 6 capturas oficiales de Steam de `datos-texto.md`.
- Hoja de contacto propia (`contacto_steam.jpg`, 960×810, Pillow) con las 6 capturas de Steam del juego base, mirada con `Read` para describir encuadres y composición — guardada en `/tmp/claude-0/trabajo/125-elden-ring-texto/`, no se subió al repositorio (no es una de las 3 hojas oficiales, esas las hace el investigador de imagen).
- Fuentes que dieron 403/bloqueo y no se reintentaron más de dos veces: `tcrf.net`, `frontlinejp.net`, `web.archive.org` (fallo de conexión del proxy, no de la web).
