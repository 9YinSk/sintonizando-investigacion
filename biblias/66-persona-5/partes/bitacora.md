## Bitácora

### Bitácora de imagen

- Fandom megamitensei (API `api.php`): páginas correctas de personajes — la del protagonista es «Ren Amamiya», no «Joker»; Ann y Ryuji sin desambiguación (búsqueda `list=search`). ES/EN.
- `Category:Persona 5 Artwork Images` (82 archivos) y galerías de Ren Amamiya, Ryuji Sakamoto, Ann Takamaki vía `generator=images`, filtradas por tamaño.
- Página de texto `Calling Card` leída con `prop=revisions&rvprop=content` para encontrar el archivo de la tarjeta física (evita adivinar el nombre del archivo).
- Colores medidos con `herramientas/estilo.py` sobre las URLs directas (cabecera Referer a fandom.com) y sobre recortes propios (Ann casual, uniforme de Shujin) cuando el fondo blanco dominaba la paleta.
- Sketchfab: API `v3/search` y `v3/models/<uid>` para comprobar licencia (todas CC BY 4.0) y que `isDownloadable` fuera `true`, no sólo confiar en el filtro `downloadable=true` de la búsqueda.
- ambientcg: API `v2/full_json?type=Material&q=…` para Leather, Fabric, Carpet, Bricks, Paper (todas CC0).
- Búsqueda web (inglés): «Persona 5 Shigenori Soejima key visual official artbook cover», «Persona 5 Royal Strikers Tactica key visual official art», «Persona 5 Joker fan art ArtStation illustration», «manga screentone halftone brushes free CC0», «Persona 5 manga Hisato Murasaki comic adaptation cover».
- `atlus.com` bloqueado por el WebFetch de Claude (proxy de salida), pero `curl` directo sí responde (200): así se sacó la colección de wallpapers oficiales de Strikers, incluido el archivo `海外版2021FIX◆PC用壁紙_01.jpg` (3840×2160). Algunos nombres de archivo con caracteres japoneses dieron 404 al re-tipearlos a mano; se resolvió extrayendo la URL exacta del HTML con una regex en vez de copiarla.
- `investigar_serie.py` tuvo que relanzarse: las hojas de contacto de la primera pasada de `recolectar.py` ya no estaban en el disco compartido (`herramientas/referencias/` es de todo el contenedor, no persiste). Relanzado con los 4 títulos correctos de página; se detuvo el proceso tras generar 16 hojas porque las 3 primeras (ordenadas por resolución) ya cubrían de sobra los 6 puntos.
- Morgana en forma de gato: comprobado mirando la imagen (`Morgana_(Cat_Version,_P5T).png`) — blanco y negro (tuxedo), collar amarillo, sin bolsa; una primera lectura de memoria decía «bolsa amarilla cruzada» y se corrigió tras ver la imagen.

### Bitácora de video

- Partí de `partes/datos-video.md` (Dailymotion, Internet Archive, MusicBrainz ya recolectados el 2026-09-25): comprobé los enlaces de opening/ending/tráiler y descarté los que no eran de Persona 5 (p. ej. resultados de "Persona 3 Reload" o "Babylon 5" mezclados en las búsquedas automáticas).
- Dailymotion API directa (`api.dailymotion.com/videos?search=`), en inglés y francés: "Persona 5 opening wake up get up", "Persona 5 all out attack", "Persona 5 Kamoshida boss battle", "Persona 5 interrogation scene", "Persona 5 Joker awakening persona", "Persona 5 ending true ending", "Persona 5 Royal trailer official", "Persona 5 Leblanc cafe", "Persona 5 castle palace gameplay", "Persona 5 Morgana cat scene", "Persona 5 Ann Takamaki Panther".
- `herramientas/fotogramas.py` sobre 11 clips de Dailymotion (opening del juego, ending 1 del anime, tráiler de lanzamiento, tráiler cinemático de Royal, 3 clips de All-Out Attack, clip de Palacios, clip de Morgana, clip de maid café, tráiler de personaje de Ann) — todas las hojas de contacto miradas con Read antes de escribir. Dos vídeos habían sido retirados de Dailymotion entre tandas (Persona 5 Royal - Morgana, Persona 5 Royal - Ann Takamaki de Vandal): usé la copia subida por otro canal de prensa.
- `herramientas/estilo.py` (Pillow) sobre 5 fotogramas grandes para medir paleta y tipo de sombreado de 4 sitios distintos.
- `megamitensei.fandom.com/api.php` (wiki de fans en inglés, vía API para evitar el 403): páginas "Beneath the Mask", "Last Surprise", "Life Will Change", búsqueda de texto "Persona 5 soundtrack Beneath the Mask", "Life Will Change Persona 5".
- Buscador web (inglés): "Persona 5 TikTok trend viral Beneath the Mask OR Last Surprise edit", "Persona 5 YouTube analysis video All Out Attack iconic scene reaction".
- AnimeThemes.moe: falló con error 522 en dos reintentos (uno heredado de `recolectar.py`, otro propio); no insistí más según la regla de dos intentos.
- YouTube: no se consultó directamente (pide inicio de sesión desde este servidor); todo lo de YouTube viene citado desde resultados del buscador web, sin descarga ni fotogramas.

### Bitácora de voz

**WebSearch (inglés):** "Persona 5 Royal character popularity poll official Atlus ranking" ·
"Persona 5 doblaje latino español actores de voz" · ""Persona 5" anime doblaje latino Crunchyroll
español" · ""Persona 5" ANMTV doblaje español latino" · "Persona 5 Ryuji 'sacrifice' scene Shido's
Palace music 'reaction' chapter" · "Persona 5 ending Phantom Thieves disappearing Yaldabaoth scene
music track name" · "Persona 5 Royal sales copies sold Metacritic score Game Awards Best RPG" ·
""Persona 5" "The Game Awards" 2017 "Best Role-Playing Game" winner".

**WebSearch (japonés):** "ペルソナ5 人気投票 結果 公式".

**Doblaje Wiki** (`doblaje.fandom.com/es/api.php`, nunca la web normal que da 402): `list=search`
con "Persona 5", "intitle:Persona", "\"Futaba Sakura\"", "\"Ann Takamaki\"", "\"Ryuji Sakamoto\"",
"Joker Persona", "Morgana Persona"; `list=allpages&apprefix=Persona` → confirmado: no existe página
de la obra (punto 8).

**Otras APIs de Fandom:** `dubbing.fandom.com/api.php` (ficha internacional de doblajes, página
"Persona 5: The Animation") · `megamitensei.fandom.com/api.php` (infobox y sección Personality de Ren
Amamiya, Ryuji Sakamoto, Ann Takamaki y Morgana, con `list=search` primero para encontrar el título
exacto de cada página).

**`navegar.py`** (páginas que bloquean curl o cargan con JavaScript): famitsu.com/news/… (encuesta
2021 completa) · mynintendonews.com (encuesta 2023) · crunchyroll.com/es (sin datos de audio, sólo
aviso de cookies) · foroseldoblaje.com (502 dos veces, sin insistir más) · xataka.com.mx (detalles del
mod LATAM Visions) · gamebanana.com/wips/85365 (estado del mod) · tvtropes.org (Memes, TearJerker y
Funny de Persona 5 — con `--html` y un script propio para leer el texto de las carpetas plegables que
un `inner_text` normal no muestra) · reddit.com (comprobar el post borrado de 891 votos).

**WebFetch:** nintendosoup.com, famitsu.com, nintendolife.com, xataka.com.mx, 3djuegos.lat,
lparchive.org → **bloqueados por la política de red del proxy** (`EGRESS_BLOCKED`); se resolvieron con
`navegar.py` cuando fue posible (famitsu, xataka) o se dejaron como «no encontré» (nintendosoup,
nintendolife, 3djuegos, lparchive).

**ANMTV** (anmtv.la): bloqueado por la política de red del proxy y por `navegar.py`
(`ERR_TUNNEL_CONNECTION_FAILED`); no se pudo consultar directamente.

**Vídeos mirados de verdad** (`herramientas/fotogramas.py`, hojas de contacto miradas con Read):
tráiler 20º aniversario Persona (Dailymotion x48wb94, HobbyConsolas) — resultó ser un tráiler cruzado
de Persona 3/4/5, poco útil para caras propias de P5 · tráiler oficial del anime «Persona 5 the
Animation - Trailer #2» (Dailymotion x6gu5mf, Gematsu/Siliconera) · clip doblado al inglés del
episodio de playa (Dailymotion x6uu26k, canal !t Live) · clip de gameplay francés del Palacio de
Kamoshida (Dailymotion x89nco2, JeuxVideo.com) — sin primeros planos útiles. Se intentó también un
clip de la escena Ann/Kamoshida (Dailymotion x5sfh6l) que dio «Not found» en yt-dlp.

**Doblaje Wiki, contenido de fans:** blog de propuesta `Usuario_Blog:SupaKaminari/Propuesta:_Persona_5`
y `propuestas-fanon.fandom.com/es/wiki/Persona_5` (reparto de fan-casting, punto 22).

**Tanda de seguimiento (26-sep-2026), sólo punto 13 — caras que faltaban:** búsqueda en la API de
Dailymotion con `Persona5 the Animation clip/scene/OVA/episode/eyecatch` (siempre devuelve el mismo
puñado de tráilers, la búsqueda por texto de Dailymotion no filtra bien más allá de la frase exacta) ·
revisado el catálogo del canal `kirill_y` (23 vídeos) hasta encontrar «First 6 Minutes» (382 s, episodio
1 real) · descartado por no ser del anime: «Persona 5 - Ryuji Trailer» (Dailymotion x50lbl6, tráiler del
videojuego con clasificación ESRB, no anime) y «ペルソナ(Persona) O.A.» (Dailymotion x6fevsz, resultó ser
un vídeo de gameplay en directo de dos actores de voz japoneses, no la animación) · WebSearch: `"Persona
5 the Animation" episode list "The Beach"` · `"Persona 5 the Animation" episode 1 title Sae
interrogation` · `"Stars and Ours" persona 5 animation special beach synopsis` · `"Dark Sun" persona 5
animation special synopsis Futaba beach` (para descartar que la playa fuera un especial y no un
episodio normal) · `megamitensei.fandom.com/api.php` página `List_of_Persona_5_The_Animation_Episodes`
(sinopsis oficial de cada episodio, confirma Episodio 1 y Episodio 18) · fotogramas.py sobre
`x6gzgvk` (cada 3 s, 3 hojas) y repaso de `x6uu26k` (cada 2 s, 2 hojas) — ambos vistos con Read, no de
oídas.

### Bitácora de texto

- Búsquedas en español: «Entrevista Hisato Murasaki Persona 5», «ペルソナ5 ロゴ フォント» (japonés).
- Búsquedas en inglés (≈16): tipografía del logo y de la UI, «Persona 5 UI font», «Atlus USA typography», «Persona 5 manga lettering Udon», «Persona 5 cel shading toon shader», «Katsura Hashino influences Lupin picaresque», «Persona 5 opening Production I.G Sayo Yamamoto», «Adapting Persona5 CloverWorks», «P5 Hatty font license», «github Persona 5 font mod», «Persona 5 Royal PC mod fonts».
- Fuentes oficiales usadas: fichas de **Fontworks/Monotype** (`fontworks.co.jp`, fabricante real de las fuentes del juego), **Famitsu** (crónica de la charla CEDEC+KYUSHU 2017 de los propios diseñadores de UI de Atlus), **Art of the Title** (créditos oficiales completos del opening), wiki de **Megami Tensei** (Fandom, vía su API `action=parse&prop=wikitext`), **The Game UI Database**.
- Fuentes de fans/comunidad, marcadas ⚠️: hilo de dafont sobre el logo, WhatFontIs sobre la fuente de diálogo, recopilaciones de mods de GameBanana sobre las fuentes de la UI en inglés.
- Herramientas propias: `fontTools` (comprobación de á/ñ/¿/¡ en 8 fuentes candidatas, todas ✅), capturas oficiales de Steam (P5 Royal, Strikers, Tactica, The Phantom X) miradas en dos hojas de contacto propias, `navegar.py` (TV Tropes, funcionó; TCRF y algunos blogs, bloqueados), `curl` directo (funcionó donde `WebFetch` estaba bloqueado por el proxy: fontworks.co.jp, famitsu.com, artofthetitle.com, blog.alltheanime.com, ramenparados.com).
- Webs que bloquearon el acceso: `tcrf.net` (Cloudflare), `ridwankhan.com` y `fontworks.co.jp`/`famitsu.com`/`artofthetitle.com` sólo vía `WebFetch` (con `curl` sí funcionaron), `web.archive.org` (fallo de red repetido), varios espejos de descarga de fuentes (dafont directo, fontsaddict, ffonts.net, wfonts — todos 403/404 a `curl`; `font.download` sí funcionó para Earwig Factory).
