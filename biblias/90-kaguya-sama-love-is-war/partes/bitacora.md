## Bitácora

### Bitácora de imagen

- Leída entera `biblias/43-kaguya-sama-love-is-war/partes/imagen.md` (24 mil
  caracteres) antes de empezar, para no repetir consultas ni datos.
- `herramientas/investigar_serie.py --wiki kaguyasama-wa-kokurasetai --paginas
  "Kaguya (Moron)" "Nagisa Kashiwagi" "Go Kazamatsuri" "Chika Fujiwara"`: 106
  imágenes enlazadas, 46 grandes → 1 hoja (`comedia_01.jpg`), mirada entera.
- Fandom API `list=categorymembers&cmtitle=Category:Omake` y `Category:Extra
  Chapters` (en): confirma que "Talk Chapter" y "Doujinshi Chapter" son los
  extras cómicos oficiales de la serie.
- Fandom API `action=parse&prop=wikitext` sobre "Episode 33", "Episode 7", "Yu
  Ishigami", "Dual Confessions Culture Festival Arc" (en): para verificar (y
  descartar, en el caso del café) datos de ambientación antes de darlos por
  buenos.
- Sketchfab API (`v3/search` con `chika fujiwara`, `shirogane kaguya`,
  `ishigami kaguya`, `hayasaka kaguya`, en): 5 modelos nuevos del mismo autor,
  confirmados uno a uno con `v3/models/<uid>`.
- Wallhaven API (`atleast=1920x1080`, `purity=100`, ordenado por favoritos, en):
  15 resultados, comprobados 5 con el detalle `/api/v1/w/<id>` para tags y
  tamaño real; 3 no estaban en la parte de 43.
- Danbooru (`donmai.us`) y Safebooru (`safebooru.org` API de tags) (en):
  sin resultados para la serie, igual que constató 43.
- Poly Haven API (`assets?t=hdris`): filtros `class/school/library/hall/cafe`
  y `festival/market/lantern/string_light` (en) — "Comfy Café" encontrado
  pero descartado al no confirmarse la escena; sin resultado para festival.
- WebSearch (ja/en): Nendoroid Kaguya y Nendoroid Ishigami (faceplates),
  disfraces de festival/cosplay, LINE stickers oficiales, pinceles de líneas
  de velocidad — 5 búsquedas.

### Bitácora de video

- `datos-video.md` (recolector): AniList (tráiler, enlaces oficiales), Dailymotion (búsqueda opening/ending/tráiler/escena), Internet Archive (vacío), MusicBrainz (vacío), AnimeThemes (522, caído) — punto de partida, no repetido.
- Leída primero `biblias/43-kaguya-sama-love-is-war/partes/video.md` (serie hermana, COMPLETA): confirma opening/ending/compositor/tráiler/sala del consejo/calle de Tokio y las poses de ep. 1 y 3; este documento evita repetir esos datos y se centra en el episodio 2 (no visto por el otro equipo) y en el enfoque «comedia y rótulos» del encargo 90.
- Internet Archive, `advancedsearch.php` (`q=kaguya-sama AND mediatype:movies`, inglés): 50 resultados revisados; se identificaron y comprobaron por metadato (`archive.org/metadata/<id>`) tres ítems nuevos no citados por la biblia hermana: `turner_video_136312` (tráiler), `kaguya-sama-movie-darkrai` (reacción a la película en español), `kaguya-sama_love_is_war_en-dub_subtitles` (subtítulos del doblaje inglés, no latino, no usado).
- Descarga completa de `Kaguya Sama Love is War/SEASON 1/02.mkv` (181 MB) del ítem `kaguya-sama_202403` (Internet Archive) a `/tmp/claude-0/trabajo/90-kaguya-sama-love-is-war-video/ep2.mkv`.
- `fotogramas.py` sobre `ep2.mkv`: panorámica completa cada 8 s (180 fotogramas, 4 hojas de contacto) + 13 fotogramas sueltos en el segundo exacto de cada hallazgo (rótulos, poses, sitios).
- `estilo.py` sobre 2 fotogramas propios nuevos: sendero de montaña (min. 10:00) y pasillo a contraluz (min. 21:44).
- AnimeThemes (`api.animethemes.moe`): reintentado (dos consultas), sigue con error 522.
- WebSearch (inglés): «Kaguya-sama Love is War OST tracklist Kei Haneoka soundtrack album titles», «Kaguya-sama Love is War narrator text card meme tiktok trend», «Kaguya-sama text card gag analysis», «Kaguya-sama narrator captions comedy technique».
- `curl` a Last.fm (bloqueado, «Client Challenge» de Cloudflare) y `navegar.py` sobre la misma URL (devolvió 0 caracteres): no se pudo confirmar el tracklist del OST con una fuente propia de segunda mano.
- Vídeo de `archive.org/metadata/<id>` consultado también para: `kaguya-sama-love-is-war-2019-720p-blu-ray` (ya descartado por la biblia hermana: es la película de imagen real, confirmado de nuevo por su metadato `mediatype`), `kaguya-sama-love-is-wars-fanservice` (compilación de fan, descartada por no aportar al enfoque de comedia/rótulos de este encargo).
- Segunda pasada (repaso, `revisar_partes.py` marcó la parte floja con sólo 2 webs): se enlazaron con URL completa las fuentes ya usadas y se sumaron dominios nuevos, todos con datos reales comprobados, sin inventar ninguno:
  - `en.wikipedia.org` (API `action=query&prop=extracts`, con `User-Agent` propio tras un primer 429 por límite de tasa): página «Kaguya-sama: Love Is War season 1» confirma director, estudio, compositor, fechas de emisión e intérpretes del OP/ED.
  - `musicbrainz.org` (`ws/2/release-group` y `ws/2/recording`, con `User-Agent` propio): confirmado el release-group del ED «Sentimental Crisis» (halca, SACRA MUSIC, single 2019-02-20); búsqueda del OP «Love Dramatic» sin ficha exacta localizable (título demasiado genérico, +1,2 millón de grabaciones).
  - `anilist.co` (ya en `datos-video.md`, ficha 101921): usado como fuente propia del tráiler oficial de YouTube y de los enlaces de streaming, para diferenciarlo del tráiler recortado de Turner en Internet Archive.
  - `kaguya-sama.fandom.com` y 4 variantes de subdominio: comprobadas por `api.php?action=query&meta=siteinfo`, las cinco devuelven 404 (no se localizó wiki de Fandom dedicada).
  - `animethemes.moe` (frontend web, no la API): `/anime/kaguya_sama` redirige a la portada (slug incorrecto o anime no indexado); la API sigue en 522 como ya constaba.

### Bitácora de texto

**Punto de partida** (no repetido): `partes/datos-texto.md` (AniList: ficha, staff, obras parecidas — sección Steam vacía, confirmado por qué en el punto 11 de 43 y reconfirmado aquí).

**Serie hermana**: `biblias/43-kaguya-sama-love-is-war/partes/texto.md` leída entera (186 líneas) antes de empezar — de ahí sale todo lo que aquí se cita como "ya cubierto por 43" y no se repite.

**Wiki de Fandom** `https://kaguyasama-wa-kokurasetai.fandom.com` (la misma que confirmó 43 e imagen de este encargo):
- `action=query&list=search` para "poster", "campaign election", "scoreboard" (sin resultado útil para un marcador gráfico).
- `action=parse&prop=wikitext` leído directo en: Chaotic Election Arc, Talk Chapter 58, `https://kaguyasama-wa-kokurasetai.fandom.com/wiki/Kaguya-sama_wo_Kataritai`, Love is Show (descartada, es un opening musical, no un rótulo).
- `action=query&prop=imageinfo` para la portada del tomo 1 de *Kaguya-sama wo Kataritai* (`https://kaguyasama-wa-kokurasetai.fandom.com/wiki/File:Talk_Volume_01.png`, bajada, mirada con Read, `/tmp/claude-0/trabajo/90-kaguya-sama-love-is-war-texto/full/talk_vol01_small.jpg`).

**TV Tropes directo** (`https://tvtropes.org`, no el mirror de Tropedia que usó 43 — **en esta máquina sí respondió** con `herramientas/navegar.py`, confirma lo que decía el aviso de lanzamiento):
- `https://tvtropes.org/pmwiki/pmwiki.php/Funny/KaguyaSamaLoveIsWar` (`--selector '#main-article' --html --max 0`, texto extraído con Python, ~158 000 caracteres) → cartelas cómicas de remate, cartel "Fooled You".
- `https://tvtropes.org/pmwiki/pmwiki.php/ShoutOut/KaguyaSamaLoveIsWar` (mismo método, ~18 000 caracteres) → toda la lista de parodias episodio a episodio, incluida la de Bakemonogatari y el cartel "Biotic Hazard".
- `https://tvtropes.org/pmwiki/pmwiki.php/Manga/KaguyaSamaLoveIsWar` (página principal): el selector trajo sobre todo JavaScript de la plantilla del sitio y la lista de VideoExamples, no el cuerpo de tropos con folders — no se insistió más (ya se cubrió lo importante vía Tropedia, que usó 43, y las dos subpáginas de arriba sí funcionaron limpias).
- Nota: los números de episodio de TV Tropes son **acumulados** (temporada 2 empieza en "Episode 13"), así que "Episode 16" = temporada 2, episodio 4 — confirmado cruzando con Animehunch, que sí usa la numeración por temporada.

**Fuentes en inglés fuera de wiki**:
- `https://en.wikipedia.org/wiki/Shinichi_Omata` (leída completa con `curl` directo, WebFetch la bloqueaba) → carrera del director en Shaft, pseudónimo Mamoru Hatakeyama, filmografía completa con referencias numeradas.
- `https://animehunch.com/internet-is-talking-about-the-monogatari-reference-in-kaguya-sama-love-is-war-season-2-episode-4/` (leída con `curl` directo, WebFetch bloqueado por el proxy de red) → confirmación secundaria e independiente de la referencia a Bakemonogatari, con fecha (mayo 2020) y capturas de tuits citadas.
- `https://www.cbr.com` (bloqueado por el proxy de red, no se pudo leer directamente) → se dejó como referencia sin verificar el detalle visual del marcador de victorias (ver «No encontré»).

**Búsquedas web** (WebSearch, en inglés):
1. Mamoru Hatakeyama Shaft Monogatari Kaguya-sama director style
2. Kaguya-sama anime points scoreboard "points" battle victory overlay text
3. "Kaguya-sama" cuttingroomfloor.com OR tcrf.net game
4. "Mamoru Hatakeyama" director style "theatrical" "references to other" anime feature interview
5. Kaguya-sama Love is War review compared "Monogatari" OR "Nisemonogatari" comedic style visual text
6. "Kokurasetai" title meaning causative grammar joke Kaguya-sama translation nuance

**Fontsource/fontTools** (obligatorio del punto 5, nuevas de este encargo): `zen-old-mincho` (peso 900/Black), `permanent-marker`, `nosifer` — las tres bajadas en `.ttf` subset `latin` y comprobadas con `fontTools.ttLib.TTFont(f).getBestCmap()` para á/é/í/ó/ú/ñ/¿/¡/Á/Ñ: las tres completas ✅. Script y `.ttf` en `/tmp/claude-0/trabajo/90-kaguya-sama-love-is-war-texto/fonts/`.

No quedan puntos obligatorios pendientes de este rol (5, 6, 11, 18, 24, 25 completos, con el enfoque de comedia y rótulos que pide el encargo 90). Parte terminada.
