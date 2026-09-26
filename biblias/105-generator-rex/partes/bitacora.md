## Bitácora

### Bitácora de imagen

- Wiki de Fandom: `generatorrex.fandom.com` (imágenes en `static.wikia.nocookie.net/generatorrexpedia/`),
  confirmada por búsqueda en `api.php?action=query&list=search`. `datos-imagen.md` no traía wiki (el encargo no
  la fijó); se buscó a mano.
- `investigar_serie.py --wiki generatorrex --min-px 90000 --paginas "Rex Salazar" "Agent Six" "Bobo Haha"
  "Providence" "Van Kleiss" "Breach" "White Knight" "Rex Salazar's machines" "Nanites" "Circe" "Noah Nixon"
  "Rebecca Holiday"` → 121 imágenes enlazadas, 113 grandes, 3 hojas de contacto (en español: se subieron a
  `hojas/` como `personajes_01.jpg`, `personajes_02.jpg`, `maquinas_01.jpg`).
- Colores: recorte con Pillow de zonas de tela limpias (sin borde de línea) sobre el retrato oficial de cada
  personaje en la wiki; verificado visualmente con recortes ampliados antes de medir (ver método en el punto 15).
- Danbooru `related_tag` y Safebooru API (`tags=generator_rex`) en inglés, para fan art y vocabulario de tags.
- Sketchfab API (`api.sketchfab.com/v3/search?type=models&q=...&downloadable=true`) en inglés, varias consultas:
  «generator rex», «generator rex nanite», «generator rex jetpack», «rex salazar», «biowulf generator rex»,
  «Meta-Nanites». Se comprobó licencia y nº de caras de cada modelo elegido con `api.sketchfab.com/v3/models/<id>`.
- ambientcg API (`ambientcg.com/api/v2/full_json`) para texturas CC0: Metal, Fabric, Paper.
- Búsquedas web (WebSearch, en inglés): «Generator Rex wallpaper 1920x1080», «Generator Rex Sketchfab 3D model
  download», «Generator Rex action figure Mattel 2010», «Generator Rex cosplay Rex Salazar costume», «Generator
  Rex DVD cover complete series poster key art», «circuit board pattern seamless texture CC0», «free halftone
  dot pattern brushes Photoshop CC0 comic screentone». 7 búsquedas usadas del cupo de ~50.
- `datos-imagen.md` (recolectar.py) revisado primero: casi todo su contenido (Danbooru/Safebooru de Raven,
  Robin, Starfire, Marceline, Bonnibel, Buttercup; Sketchfab de terrenos/SciFi genérico; Openverse de dinosaurios
  y NASA OSIRIS-REx) es ruido de una búsqueda genérica por la palabra «rex» sin wiki fijada; se descartó y se
  investigó todo de nuevo con la wiki correcta. Sólo se aprovechó el bloque de `rex_salazar` en Danbooru y
  Safebooru, que sí es de esta serie.

### Bitácora de video

- Dailymotion API (`api.dailymotion.com/videos?search=...`): «Generator Rex
  opening theme», «Generator Rex full episode», «Generator Rex ending
  credits», «Generator Rex clip scene» — en inglés. De ahí salieron los clips
  usados (opening HD, intro+ending, tráiler del juego, Operation Wingman,
  SixxRex).
- `fotogramas.py` sobre 6 clips de Dailymotion y 1 de Internet Archive: hojas
  de contacto miradas con Read en /tmp/claude-0/trabajo/105-generator-rex-video/.
- Wiki `generatorrex.fandom.com` (api.php): `action=query&list=search` para
  «Episode 1», «Operation Wingman», «theme song Orange», «damned wretch»; y
  `action=parse&prop=wikitext` sobre «List of Generator Rex episodes»,
  «Kevin Manthei», «Orange» y «Soundtrack of Generator Rex».
- `estilo.py` sobre 4 fotogramas propios (Providence, patio colonial, ciudad
  de noche, interior de ruinas) para los hex de paleta y luz del punto 4.
- Internet Archive `advancedsearch.php` para episodios completos: no hay
  episodios completos subidos, sólo compilaciones de fans y clips de juego;
  usé la compilación de poderes (canal con más descargas, 571) como escena 3.
- `kmmproductions.com` (sitio del compositor) está fuera de la lista de
  hosts permitida desde este servidor: no pude leerlo directo; la wiki cita
  esa misma fuente para el dato de Kevin Manthei, así que lo dejé con la
  wiki + los créditos del propio show como las dos fuentes.
- WebSearch (2 de ~50): «"Generator Rex" TikTok edit OR trend 2024 2025»
  (nada relevante) y «"Generator Rex" opening theme song "Revolution" Orange
  band» (confirmó la autoría en Wikipedia, Bandcamp y Apple Music/Spotify).

### Bitácora de voz

- Doblaje Wiki, wikitext completo de «Generador Rex» vía `action=parse&prop=wikitext` (api.php, funciona en este servidor) · español.
- Behind The Voice Actors (`behindthevoiceactors.com`): páginas de personaje de Rex, Van
  Kleiss, Agente Seis, Bobo Haha, Dra. Holiday, Caballero Blanco, Circe, Brecha, Caballero
  Negro, Skalamandra, Hunter Caín, Noah, César — leídas con `navegar.py --html --max 0`
  para ver el HTML completo (los actores no ingleses están ocultos tras un botón «Show
  Non-English Actors», pero el HTML los trae igual) — inglés/español mezclado en los
  nombres de actor.
- WebSearch: «Juan Amador Pulido» (para identificar el país del actor que dio BTVA para
  Bobo), ANMTV + Generador Rex (varias veces, sin ficha de reparto útil, sólo noticias de
  estreno/emisión), TV Tropes Ensemble Darkhorse, fandub español latino, memes/TikTok
  hispano — español e inglés.
- `herramientas/navegar.py` sobre `tvtropes.org/pmwiki/pmwiki.php/YMMV/GeneratorRex`
  completo (--max 0) — inglés.
- `generatorrex.fandom.com` (wiki en inglés activa), API `action=parse&prop=wikitext`,
  páginas: Rex Salazar, Agent Six, Bobo Haha, Rebecca Holiday, Noah Nixon, Caesar Salazar,
  Van Kleiss, White Knight, Circe, Biowulf, Breach, Black Knight, Hunter Cain — inglés.
- `herramientas/voz.py` sobre el tráiler oficial doblado de Dailymotion
  (`x84bg5o`, repost de 3djuegos.com) para transcripción con minuto y ficha de voz —
  español.
- `herramientas/fotogramas.py --cortes` sobre dos clips de Dailymotion (compilado
  «Generator Rex Episode 1», x31x2vw; promo oficial CN «Heroes United», x2z8as2) para
  fotogramas del punto 13.
- Archive.org (`advancedsearch.php` y `metadata`) buscando «generator rex» y «generator
  rex latino»: sin episodios doblados aprovechables — inglés.
- API de Dailymotion (`api.dailymotion.com/videos?search=...`) varias veces: «Generator
  Rex fandub», «Generador Rex cover», «Generator Rex Revolution cover», «Generador Rex
  capitulo español latino» — sin fandubs reales, sólo contenido no relacionado o
  reposts oficiales.
- YouTube, API oEmbed, para confirmar el canal real del opening reposteado
  (`youtube.com/oembed?url=...&format=json`) — español.

### Bitácora de texto

- generatorrex.fandom.com vía api.php (`action=query`, `list=search`, `list=allpages`, `list=allimages`, `prop=revisions`): páginas de Generator Rex, M. Rex, Man of Action, Cartoon Network Action Pack, Nanite Event, Providence, EVO, Consortium, Jose Lopez, juegos (Agent of Providence, Nanite Master, Nanite Runner, Heroes United online, Titanic Kungfubot Offensive) — español no aplica, wiki en inglés.
- en.wikipedia.org/wiki/Generator_Rex vía curl directo (funcionó; WebFetch a Wikipedia salió bloqueado por el proxy de red) — inglés.
- tcrf.net vía curl y `navegar.py` (`/api.php?action=query&list=search`, `/index.php?title=Special:Search`) — bloqueado por Cloudflare en los tres intentos (403 / challenge JS), no se insistió más.
- tvtropes.org/pmwiki/pmwiki.php/WesternAnimation/GeneratorRex y /Trivia/GeneratorRex vía `navegar.py` (funciona en esta máquina; por curl directo da Cloudflare) — leídas completas en esta tanda (premisa, epígrafe del opening, trivia de voces y episodios); las carpetas largas de tropos (#-E a U-Z) siguen sin cargar por ser JS de scroll — inglés.
- twitter.com/rouleau1/status/1788393357955514857 vía `navegar.py` — leído directamente, confirma «Everything in the game falls under canon» (dato del punto 25, antes sólo citado de segunda mano) — inglés.
- archive.org/wayback/available (`http://`, la versión `https://` cortó la conexión del proxy) para 4 variantes de la URL oficial de Cartoon Network y para `generatorrex.com` — inglés.
- api.fontsource.org/v1/fonts/black-ops-one — confirmación directa de la licencia OFL-1.1 en la respuesta de la API, no sólo en la web de Google Fonts.
- api.github.com/search/repositories y github.com/search (repos o código con «Generator Rex» font/subtitles): la API de búsqueda de código no está disponible en este contenedor («sessions are bound to their configured repositories») y la búsqueda web de github.com dio 403; no se insistió más.
- store.steampowered.com/api/storesearch (`term=generator rex`): sin resultados, no hay ningún juego de Generator Rex en Steam (coherente con que el único juego de consola fue de 2011, pre-Steam para ese tipo de licencia) — confirma lo ya sabido, no añade dato nuevo.
- ign.com/games/generator-rex-agent-of-providence vía curl directo: 403 (bloqueo del sitio, no del proxy); la reseña de IGN sigue citada de segunda mano por la propia wiki, no se pudo leer directamente.
- dafont.com/generator-rex.font vía `navegar.py` (bloqueado por WebFetch, funcionó por `navegar.py`); descarga del .ttf vía `dl.dafont.com` y comprobación de glifos con `fontTools` — inglés.
- api.fontsource.org (`/v1/fonts`, `/v1/fonts/<id>`) + descarga de .ttf desde `cdn.jsdelivr.net/fontsource` + `fontTools.getBestCmap()` para comprobar á é í ó ú ñ ¿ ¡: Black Ops One, Bangers, Comic Neue, Luckiest Guy, Special Elite, Audiowide, Oswald — todas completas.
- archive.org: `/metadata/generator-rex-website-tour` y `/metadata/PS3_Longplay_141_Generator_Rex_Agent_of_Providence`; miniaturas del recorrido del sitio bajadas y miradas directamente (contact sheet propio, `web_sheet.jpg`).
- Búsquedas web (`WebSearch`, en inglés y coreano): `"Generator Rex" logo font typeface`; `"Generator Rex" animation studio Flash Toon Boom production`; `"Generator Rex" thecuttingroomfloor.com`; `"Generator Rex" animation "Rough Draft" OR "Moi Animation" OR "Digital eMation" OR overseas animation studio`; `"Generator Rex" character design interview Duncan Rouleau art style influences`; `"Generator Rex" 제너레이터 렉스 한국 카툰네트워크`.
- `servidor/inventario.md`: revisado por «rex», no hay canal ni lámina existente que choque; `biblias/` revisado por series de género parecido (nanotecnología/cyborg adolescente): ninguna biblia terminada todavía comparte ese género exacto (106-glitch-techs existe como carpeta pero sin `biblia.md`).
- Aviso del jefe sobre datos-texto.md mezclado con otras obras: comprobado, el archivo estaba casi vacío (un único bloque de Steam sin resultados) y no se usó nada de él.
