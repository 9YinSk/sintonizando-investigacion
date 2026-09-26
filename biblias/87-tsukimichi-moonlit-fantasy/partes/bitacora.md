## Bitácora

### Bitácora de imagen

| Búsqueda | Idioma | Fuente | Resultado |
|---|---|---|---|
| Tsukimichi wiki imágenes | — | tsukimichi.fandom.com/api.php | ✅ 116 imágenes en índice |
| Artwork personajes anime | — | Wiki generator allimages | ✅ Makoto/Tomoe/Mio artwork |
| Portadas Blu-ray | — | Wiki allimages | ✅ v01-v04 |
| Key visual AniList | — | anilist.co | ✅ portada + banner |
| Fan art Safebooru | — | safebooru.org | ✅ 12 resultados para personajes principales |
| Fondos pantalla | — | wallhaven.cc | ✅ 6 resultados |
| Modelos 3D | — | sketchfab.com/v3/search | ❌ 0 resultados |
| Colores hex | — | PIL/estilo.py | ✅ medidos de imágenes |
| CAGallery bocetos | — | wiki allimages | ✅ 37 páginas de bocetos |
| Cosplay | — | wiki | ⚠️ 1 imagen baja res |
| Colaboraciones gachas | EN | Google/wiki | ❌ no encontrado |
| Texturas libres | — | ambientcg.com | ⚠️ sin verificar washi |
| Fandom falló | — | herramientas/recolectar.py | Error wiki inicial (resuelto manualmente) |

### Bitácora de video

- Dailymotion (API directa `api.dailymotion.com/videos?search=`), español/inglés/japonés: «Tsukimichi opening full», «月が導く異世界道中 OP», «TSUKIMICHI Moonlit Fantasy OP1», «Tsuki ga Michibiku Isekai Douchuu ED1», «月が導く異世界道中 ED» — sin un OP/ED limpio propio; sí sirvieron los tráilers ya usados en `datos-video.md`.
- `api.animethemes.moe` (dos rutas, `/anime?filter...` y `/search?q=`): error 522 las dos veces.
- YouTube: tráiler de AniList (`U8T63kIny7E`) → «Video unavailable» con yt-dlp.
- Internet Archive: `archive.org/metadata/<id>` para ver los archivos de vídeo reales de dos ítems (`tsuki-ga-michibiku-isekai-douchuu`, `subs-please-...-s-2-01-...`); frames sacados con `ffmpeg -ss <seg> -i <URL directa>` (usa *range requests*, no hace falta bajar el episodio entero).
- `tsukigamichibikuisekaidouchuu.fandom.com/api.php` (búsqueda de texto y `action=query&prop=revisions` sobre wikitexto): episodios 1, 5 y S2E1 para confirmar título, fecha, OP/ED y personajes; páginas «Gambling (song)», «Utopia (song)», «Aa Jinsei ni Namida Ari (song)».
- MusicBrainz (`musicbrainz.org/ws/2/release` y `/work` y `/recording`, query «Tsuki ga Michibiku Isekai Douchuu», «Gambling Tsukimichi», «Utopia Tsukimichi»): resultados genéricos sin relación real, no se usó nada de aquí (mejor la wiki, que sí tenía las fichas exactas).
- WebSearch (inglés): «Tsukimichi Moonlit Fantasy TikTok viral clip edit», «Tsukimichi Moonlit Fantasy YouTube analysis video explained», «Tsukimichi Moonlit Fantasy season 3 release date 2026».
- `herramientas/estilo.py` sobre 3 fotogramas propios de 1280 px para las paletas del punto 4.
- Un clip de Dailymotion descartado por no ser contenido real de la serie (gameplay de shooter con vtuber mal etiquetado); anotado arriba para que nadie lo reuse.
- Aviso de corrección propia: en un primer repaso confundí a Tomoe con Mio en dos fotogramas del episodio 1 (ambas pueden llevar tonos claros en el pelo a primera vista). Se corrigió comparando el color de pelo de la ficha de cada personaje en la wiki (Tomoe «light blue», Mio «black») y la lista oficial de «Characters in Order of Appearance» de cada episodio (Mio no aparece en el episodio 1; debuta como «Black Spider» en el 2 y consigue forma humana y nombre en el 3). La tabla del punto 14 ya queda con la atribución correcta.

### Repaso 26-sep-2026 (arreglar dominios distintos)

- `en.wikipedia.org`: `action=parse` con `prop=sections`/`prop=wikitext` dio «too many requests» dos veces seguidas (límite de la API compartido); funcionó pidiendo la **página normal** (`/wiki/Tsukimichi:_Moonlit_Fantasy`) con `curl` normal, sin login. De ahí: temas de OP/ED oficiales por tramo, compositor Yasuharu Takanashi, estudios C2C/J.C.Staff, 37 episodios y el anuncio de la 3ª temporada.
- `tsukimichi.com` (sitio oficial japonés, de `datos-video.md`): páginas `/1st/music/`, `/1st/movie/` y `/1st/staffcast/` con `curl` directo (200 OK, sin bloqueo) — confirman OP/ED de la T1, 4 vídeos promocionales con su ID de YouTube, compositor y director de sonido.
- `python3 herramientas/navegar.py "https://www.tiktok.com/tag/tsukimichimoonlitfantasy" --espera 5000`: **funcionó** (antes no se había probado con TikTok en esta parte) — confirma en vivo el gag «Tomoe and Mio put arrogant adventurers in their place» y varios edits de Makoto.
- `navegar.py` sobre `https://www.youtube.com/watch?v=Wi5k6q5ZKPg`: sigue dando 429 «tráfico inusual» (captcha) aunque el certificado del proxy ya esté arreglado — el bloqueo de YouTube es del propio YouTube, no del proxy. No se reintentó una tercera vez.
- `animethemes.moe` y `crunchyroll.com` y `animenewsnetwork.com`: 403 con `curl` directo, un solo intento cada uno (no vale la pena un segundo con las mismas herramientas).
- `twitter.com/tsukimichi_pr` → redirige a `x.com/tsukimichi_pr` (200), pero el contenido de los tuits no se puede leer sin JavaScript/login; se cita sólo como canal oficial confirmado (AniList + enlace del propio sitio oficial), no como fuente de un tuit concreto.

### Bitácora de voz

- AniList (API/web, ya en `datos-voz.md`): favoritos por personaje, biografías, seiyū.
- Doblaje Wiki, `action=parse&prop=wikitext` sobre `Tsukimichi:_Moonlit_Fantasy` completo (la tabla
  de `datos-voz.md` sólo traía la mitad; pedí la wikitext entera y saqué el reparto principal a mano).
- `tsukimichi.fandom.com` (wiki de la obra en inglés), `api.php?action=parse&prop=wikitext` sobre
  Makoto Misumi, Tomoe, Mio y Shiki: personalidad, trivia, relaciones, altura, cumpleaños.
- Danbooru (ya en `datos-voz.md`): recuento de dibujos de fans por personaje.
- Buscador japonés «月が導く異世界道中 人気投票» (encuesta de popularidad) → encontré «ランこれ»
  (rancolle.com, 2º sondeo oficial de personajes) y «みんなのランキング» (ranking.net, sondeo de
  fans con 81 votantes); rancolle.com dio error de certificado tanto por curl+JS como por
  `navegar.py` (Playwright), y probé también con `https://example.com` para confirmar que
  `navegar.py` está fallando en general en este contenedor ahora mismo (TLS/CA), no sólo con ese
  sitio — lo anoto para quien revise el entorno. ranking.net sí cargó por curl normal.
- Internet Archive (`archive.org/advancedsearch.php`) buscando «tsukimichi latino»: encontré los
  episodios 1-6 completos con audio del doblaje latino oficial subidos por «Anime Online Ninja»
  (`anime-online-ninja-tsukimichi-bd-latino-01` a `-06`). Bajé fragmentos con
  `yt-dlp --download-sections` (no el episodio entero) de los episodios 1 y 2, transcribí con
  `herramientas/voz.py` (Whisper local, idioma es) y saqué fotogramas con `herramientas/fotogramas.py`
  en los mismos segundos para las caras de cada emoción.
- Dailymotion (API, ya usada en `datos-video.md`/`datos-voz.md`): sin clips doblados relevantes
  nuevos; sin fandubs de voz completos.
- TikTok (buscador web): cuenta @aoisamastudio con recortes en español latino del doblaje oficial.
- WebSearch (en español, inglés y japonés): «Tsukimichi Moonlit Fantasy encuesta popularidad
  personaje favorito Newtype ranking», «tsukimichi.fandom.com wiki Makoto Misumi cumpleaños altura»,
  «月が導く異世界道中 人気投票 キャラクター», «reddit tsukimichi moonlit fantasy why underrated love
  this anime», «Tsukimichi Moonlit Fantasy fandub español latino cover opening youtube», «Tsukimichi
  Moonlit Fantasy meme Goddess hate running joke fandom», «"Ferso Velázquez" Makoto Tsukimichi
  doblaje voz», «ANMTV Tsukimichi Moonlit Fantasy doblaje latino Crunchyroll reparto», «Tsukimichi
  Moonlit Fantasy tiktok español latino escena viral», «"Tsukimichi" fandub español meme parodia
  Makoto Diosa».
- Arctic Shift (Reddit archive): `subreddit=anime&query=tsukimichi`, `query=tsukimichi` global y
  `title=tsukimichi`/`moonlit fantasy`/`Tsuki ga Michibiku` sin resultados (0 posts) — coincide con
  lo que ya había anotado `recolectar.py` («no encontré el subreddit»); la comunidad de Reddit para
  esta serie es minúscula o el índice de Arctic Shift no la cubre bien.
- Crunchyroll: la web es una SPA (contenido no está en el HTML crudo) y `navegar.py` falló por el
  problema de certificado ya anotado; usé el resumen de WebSearch sobre la página oficial de anuncio
  de reparto como segunda fuente para el reparto principal.

### Bitácora de texto

| Búsqueda | Idioma | Fuente | Resultado |
|---|---|---|---|
| Logo tipografía anime Tsukimichi | ES/EN | WebSearch | Seeklogo tiene SVG del logo; no nombra fuente |
| Videojuego Tsukimichi interfaz | ES/EN | WebSearch | Peace Chronicles (G123, 2024) confirmado |
| Manga bubbles font Alphapolis | EN | WebSearch | Convención AntiGothi confirmada; no específico de Tsukimichi |
| Anime similar isekai Tsukimichi | EN | WebSearch | Lista completa de AniList, Anime-Planet, GameRant |
| Season 3 2025 2026 | EN | WebSearch | Confirmada S3 para 2026 |
| Manga ch001 title image | — | Fandom API + imagen | Vista directamente |
| Key visual S1 y S2 | — | Fandom wiki API + imágenes | Descargadas y analizadas |
| Kuzunoha Company logo | — | Fandom API + imágenes | Manga (blanco/negro) y anime (letrero madera) vistos |
| Mapa del mundo | — | Fandom API + imagen | world_map.png descargado y visto |
| Colores hex | — | estilo.py (Pillow) | Medidos en key_visual_s1.png y key_visual_s2.png |
| Noto Sans JP, Cinzel, M PLUS Rounded | — | Google Fonts + fontTools | ñ, ¿, ¡, tildes verificadas ✅ |
| Trailer VOSE Dailymotion | — | fotogramas.py | Descargado; 36 fotogramas analizados |
| Trailer S2 Dailymotion | — | fotogramas.py | Descargado; 21 fotogramas analizados |
| Fandom wiki: Magic, Hyuman, Goddess, Subspace, Sakai, Story Timeline, Species, Kuzunoha, Manga | EN | Fandom API | Consultadas |
| AnimeThemes | EN | API | HTTP 522 error, inaccesible |
| Reddit / Arctic Shift | EN | Arctic Shift API | Timeout o requiere subreddit específico |
| TV Tropes | EN | curl | Cloudflare bloqueó |
| Wikipedia ES/EN | ES/EN | API | Timeout en Wikipedia |
| G123 Peace Chronicles interfaz | EN | WebSearch + curl | Requiere sesión activa, no accesible directo |
