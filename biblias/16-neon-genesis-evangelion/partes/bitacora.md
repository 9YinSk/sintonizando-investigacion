## Bitácora

### Bitácora de imagen

- `herramientas/investigar_serie.py --serie "Neon Genesis Evangelion" --wiki
  evangelion --paginas "Shinji Ikari" "Rei Ayanami" "Asuka Langley Soryu"
  "Misato Katsuragi" "Gendo Ikari" "Kaworu Nagisa"` → 455 imágenes, 208
  grandes, 5 hojas (las 5 miradas con Read antes de elegir 3).
- API de Sketchfab (`api.sketchfab.com/v3/search`) con los términos:
  `evangelion`, `clipboard`, `cello`, `sony walkman`, `entry plug`, `eva unit
  01 rigged`, `evangelion rigged` — todas devolvieron resultados con licencia
  exacta.
- API de ambientCG (`ambientcg.com/api/v2/full_json?type=Material&q=paper`) →
  6 materiales de papel CC0.
- API de Wallhaven (`wallhaven.cc/api/v1/search` y `/w/<id>`) → top 5 fondos
  por favoritos, tamaño y autor reales.
- `curl -I` (código de estado) a los 4 enlaces de Wallpaper Abyss de la biblia
  vieja: los 4 siguen vivos (200).
- Descargué y medí con Pillow (mediana de un parche de 6-12 px) 6 imágenes:
  Shinji en plugsuit, Asuka con uniforme escolar, Rei con plugsuit dañado, la
  figura S-FIRE de Asuka, Misato de cuerpo entero y un fotograma de Gendo/EoE.
  Herramienta: script propio (no `estilo.py`, que da colores dominantes de
  toda la imagen, no por prenda) en `/tmp/claude-0/trabajo/16-neon-genesis-evangelion-imagen/`.
- Búsquedas web (WebSearch, en español e inglés): «free CC0 manga screentone
  halftone brush pack», «Evangelion NERV logo emblem free vector download
  license», «gumroad free screentone pack $0», «Evangelion Fortnite
  collaboration skin OR pachinko OR cafe collaboration 2025 2026», «"The First
  Descendant" Evangelion collaboration release date official skins»,
  «Evangelion Uniqlo UT OR Sanrio OR Ichiban Kuji 30th anniversary
  collaboration 2025», «EVANGELION:30+ McDonald's Japan GU collaboration
  merchandise details».
- No repetí ninguna consulta de `datos-imagen.md` (portada AniList, texto de
  «Appearance» de la wiki, Danbooru, Safebooru, Openverse): las usé tal cual
  llegaron, sólo verificando lo que hacía falta para mis puntos.

### Bitácora de video

- `curl` a `api.animethemes.moe` (dos veces) → HTTP 522, sin datos.
- `archive.org/advancedsearch.php` (inglés): «Neon Genesis Evangelion»,
  «Evangelion ending», «Evangelion trailer», «Neon Genesis Evangelion
  Platinum Perfect Collection», «Evangelion 24 / Kaworu / 26» → encontré el
  opening completo, el ending suelto, el tráiler oficial de GKIDS y 19
  episodios sueltos con audio japonés y hardsubs en inglés.
- `curl -I` a los `.mp4` de Internet Archive para comprobar tamaño real antes
  de bajarlos (`content-length`).
- `fotogramas.py` sobre 6 vídeos reales: opening (17 fotogramas + 4 sueltos),
  ending (14 + 1), tráiler (15 + 3 sueltos), episodio 1 (6 fotogramas
  sueltos), episodio 8 (3), episodio 6 (3).
- `estilo.py` sobre 9 fotogramas para paleta real (k-means con Pillow).
- `evangelion.fandom.com/api.php` (inglés): búsqueda de texto «synchronization
  ratio warning sound» e intento de página «Pattern_Blue» (no existe).
- `soundeffects.fandom.com/api.php` (inglés): wikitext completo de la página
  «Neon Genesis Evangelion» → catálogo de efectos de sonido.
- Búsqueda web (español): «Evangelion sonido reconocible alarma pattern
  sincronización efecto de sonido icónico».
- Búsqueda web (inglés): «Evangelion sound effects iconic "synchronization
  ratio" alarm klaxon recognizable» → confirmó la librería Hollywood Edge (2.ª
  fuente en `forum.evageeks.org`).
- `curl -sSI` a los enlaces de TikTok de §12 de la biblia para comprobar que
  siguen respondiendo.
- **Segunda pasada (relanzo)**: bajé el episodio 5 completo (Rei I, 140 MB) y
  el episodio 6 completo (Rei II, 140 MB) uno por uno del ítem de los 19
  episodios sueltos, y el archivo combinado `.ia.mp4` de los episodios 22-24
  (435 MB, Kaworu). Miré los tres con `fotogramas.py` en pasadas de 10-15 s
  (contactos completos) y luego saqué fotogramas sueltos con `ffmpeg -ss` en
  los segundos exactos para confirmar cada pose. `estilo.py` no hizo falta
  esta vez (ya había paleta medida de los sitios principales).
- `python3 herramientas/navegar.py "https://tvtropes.org/pmwiki/pmwiki.php/Awesome/NeonGenesisEvangelion" --selector 'div#main-article'`
  (inglés) → sí funcionó esta vez (200, sin bloqueo); confirmé que «Ode to
  Joy» suena en toda la escena final de Kaworu (punto 9).

Corrección importante de esta pasada: la pose de §15 «silueta de pie, ep. 6,
15:32» que se atribuía a Rei es en realidad **Shinji** (visto en el fotograma
vecino); se retira de la lista de Rei arriba.

- Episodios completos disponibles para mirar de verdad en Internet Archive
  (ítem `neon-genesis-evangelion-episode-21-...`, 19 episodios sueltos +
  tema de cierre) y episodios 22-26 combinados en otros dos ítems
  (`neon-genesis-evangelion-22-al-24`, `evangelion-final-25-y-26_202609`):
  dejo la ruta anotada para que cualquiera pueda seguir mirando capítulos
  concretos sin depender de YouTube · ✅ (comprobé que los archivos existen y
  pesan lo que dicen, con `curl -I`)

### Bitácora de voz

- Doblaje Wiki, API `action=parse&prop=wikitext`, página
  `Neon_Genesis_Evangelion` (doblaje original) — wikitext completo leído con
  Python, no con el navegador (evita el 402 de la web normal). Confirmó
  Humberto Solórzano (Gendo) y Maru Guerrero (Ritsuko), datos que la biblia
  tenía como huecos.
- Doblaje Wiki, misma API, página `Renewal_of_Evangelion` — dio el estudio
  (Grabaciones y Doblajes Internacionales), director (Gerardo García) y año
  (2007 grabación / 2008 emisión) del 2.º doblaje, que la biblia no tenía.
- `herramientas/voz.py` sobre 6 muestras `.ogg` de Doblaje Wiki (Gendo,
  Ritsuko, Shinji, Asuka, Rei, Misato, todas del doblaje original) — Whisper
  en local, `--idioma es`. Confirmé que transcribe mal los nombres propios
  (aviso ya en AYUDANTE.md).
- Know Your Meme, búsqueda directa de «Get in the Robot Shinji» y «Gendo
  Pose» — confirmó los dos memes que la biblia tenía con ⚠️ en el nombre.
- Intenté `fotogramas.py` sobre los clips de Dailymotion de `datos-video.md`
  (`x89nqnd`, `x8czp5s`) buscando primeros planos de cara para el punto 13.2:
  son montajes de acción, no sirven para la tabla de emociones.
- Internet Archive, búsqueda `title:(Neon Genesis Evangelion) AND
  mediatype:(movies)` — encontré `neon-genesis-evangelion-toonami-rip` (47
  min, emisión real de Toonami con anuncios, doblaje inglés) y lo miré entero
  con `fotogramas.py --cada 15` (192 fotogramas, 4 hojas de contacto) más
  `--fotograma` en 6 segundos concretos para sacar caras en alta. Es el
  episodio 8. También busqué `identifier:erai-raws-neon-genesis-evangelion*`:
  sólo hay ep. 3 y 4 (japonés, sin los personajes que me faltaban).
- Arctic Shift (Reddit): repetí la consulta del subreddit de Evangelion, con
  el mismo resultado que `recolectar.py` (no lo encuentra) — no insistí más
  de dos veces, según la regla de AYUDANTE.md.
- Búsquedas de fan dub en Dailymotion (español y latino) — ya hechas por
  `recolectar.py` en `datos-voz.md`: sólo devuelven tráilers oficiales y un
  AMV, no fandubs de voz. Repetí con la API de Dailymotion con términos más
  específicos («Cruel Angel Thesis cover español», «Evangelion fandub voz
  español») y esta vez sí salió un cover cantado real del opening y un vídeo
  etiquetado «fandub» de Asuka — confirmé el cover oyéndolo con `voz.py`.
- No hay `biblias/131-evangelion-tarjetas-y-nerv/` con `voz.md` propio: el
  encargo 131 comparte carpeta con esta serie (misma obra), pero no tiene
  biblia escrita aún, así que no había nada que leer de una «serie hermana».
  Sigue así en esta tanda (relanzo): comprobé de nuevo y la carpeta
  `biblias/131-evangelion-tarjetas-y-nerv/` no existe todavía.
- **Relanzo — resuelto el `Sigue:` de la tanda anterior**: busqué en Internet
  Archive (`archive.org/advancedsearch.php?q=title:(neon genesis evangelion)
  AND mediatype:(movies)`, más de 50 ítems) hasta encontrar
  `evangelion-the-full-series` («Neon Genesis Evangelion - The Definitive
  Release»), los **26 episodios completos** en 1080p, SUB (japonés+subtítulo
  inglés, duración = corte japonés original) y DUB (inglés). Extraje
  fotogramas de los episodios 2, 8 y 24 directamente por URL con `ffmpeg -ss
  <segundo> -i "<url .mp4>" -frames:v 1 …` (range request HTTP: ~10-15 s por
  fotograma, sin bajar los ~600 MB de cada episodio) para no gastar disco
  compartido. Revisé varios segundos alrededor de cada minuto citado en
  biblia §8 montando hojas de contacto propias (Pillow) antes de elegir el
  fotograma final de cada personaje — así confirmé que los minutos que la
  biblia ya tenía de oído (audio/subtítulo japonés) coinciden con la imagen
  real. También descarté frames vecinos: el tramo 240-243 s del ep. 8 es un
  gag cómico de un marinero levantando la falda de otra tripulante, y sólo al
  segundo 244 aparece Asuka debajo, gritando de rabia — por eso el fotograma
  final es 244 y no 246 (el que ya citaba biblia §8 de oído).

### Bitácora de texto

- WebSearch (inglés): «Cutting Room Floor Evangelion Girlfriend of Steel
  prerelease»; «"Cutting Room Floor" Evangelion Shinji Ikari Raising
  Project»; «Hideaki Anno interview Kabbalah Sephirot Evangelion symbolism
  "no particular meaning"»; «Hideaki Anno influences Yoshiyuki Tomino Ideon
  Kunihiko Ikuhara interview Evangelion»; «Evangelion production Gainax
  limited budget still frames cel animation analog making of interview»;
  «Blender Freestyle Line Art modifier anime outline toon shader tutorial
  settings»; «Photoshop anime cel shading tutorial layers multiply screen
  grain halation brushes»; «Evangelion manga Sadamoto speech bubbles panel
  layout style analysis»; «"Anno shot" OR "Anno-shot" Hideaki Anno signature
  framing composition style analysis»; «ChiKareGo2 font free download ttf».
- WebSearch (japonés): «庵野秀明 エヴァンゲリオン 影響を受けた作品 イデオン
  ウルトラマン»; «新世紀エヴァンゲリオン 使徒 名前 天使 由来 セフィロト».
- Bajado y comprobado con **fontTools** (`TTFont.getBestCmap()`):
  `ChiKareGo2.woff` (GitHub, helloedit/resources/fonts).
- Leído directo con `curl` (sí responde, a diferencia de Fandom/TV Tropes):
  `wiki.evageeks.org` — páginas Human_Instrumentality_Project, MAGI,
  Second_Impact, AT_Field, Lance_of_Longinus, Children, Kabbalah (vacía),
  Sephirot (no existe), Statements_by_Evangelion_Staff.
- Intentado y **bloqueado**: `tcrf.net` (Cloudflare, 403 en WebFetch,
  `ERR_CERT_AUTHORITY_INVALID` en navegar.py); `tvtropes.org` (mismo error
  de certificado); `web.archive.org` (túnel del proxy se cerró 3 veces,
  `ws_closed_mid_exchange` según `/__agentproxy/status`; `archive.org` sin
  «web.» sí funcionó).
- Repositorio propio: `grep -rl "demos" biblias/*/biblia.md` para el punto
  24.3 (ningún canal #demos repetido).
- Ya estaba en `datos-texto.md` y no repetí la consulta: AniList (obra,
  equipo creativo, obras parecidas y relacionadas).
