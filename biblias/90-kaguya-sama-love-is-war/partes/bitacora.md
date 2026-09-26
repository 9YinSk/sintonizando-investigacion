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

### Bitácora de voz

- doblaje.fandom.com/es/api.php — reparto latino y «Datos de interés»
  (español) — ya leído por `recolectar.py`, filtrado aquí para comedia.
- kaguyasama-wa-kokurasetai.fandom.com/api.php — secciones *Personality* de
  Nagisa, Tsubasa, Kobachi, Adolphe, Moeha, Toyomi (inglés) — 6 llamadas.
- kaguyasama-wa-kokurasetai.fandom.com/api.php — imágenes e imageinfo de 5
  secundarios (inglés) — 2 llamadas.
- `herramientas/voz.py` sobre 6 muestras `.ogg` de Doblaje Wiki que 43 no
  había transcrito (español) — hecho en el punto 8.
- `herramientas/navegar.py` en tvtropes.org/.../Funny/KaguyaSamaLoveIsWar
  (inglés, con selector `.folder` para saltar el colapso de JS) — 2
  intentos, el segundo funcionó.
- WebSearch: `"Kaguya-sama" fandub latino parodia comedia español tiktok`
  y `"Kaguya sama" fandub cómico "escena" latino youtube español` (español) —
  2 búsquedas, encontraron 2 fandubs cómicos nuevos.
- en.wikipedia.org/wiki/Chika_Fujiwara (inglés) — ya usado en punto 7-8.
- arctic-shift.photon-reddit.com — confirmado r/Kaguya_sama en cuarentena,
  0 resultados (repetido de 43, mismo resultado).

### Bitácora de texto

**Punto de partida** (no repetido): `partes/datos-texto.md` (AniList) y `biblias/43-kaguya-sama-love-is-war/partes/texto.md` completo (misma obra, otro encargo — leído entero antes de empezar para no duplicar).

**Wiki de Fandom** `kaguyasama-wa-kokurasetai.fandom.com`:
- `action=opensearch&search=Election` → localizó la página «Chaotic Election Arc».
- `action=parse&prop=wikitext&page=Chaotic Election Arc` → lista de capítulos del arco (59-69), sin detalle de rótulo de cartel (stub).
- `indice.json` de `herramientas/referencias/kaguya-sama-love-is-war/` (75 imágenes ya listadas por `investigar_serie.py` en el encargo hermano, reutilizado sin volver a descargar la wiki entera) filtrado por palabras clave de rótulo/comedia ("Election", "Poster", "Banner", "Festival", "Sign", "Screen_Shot", "Preview", "Chapter", "Campaign", "Culture").
- 4 imágenes oficiales bajadas en tamaño completo y miradas una por una (Read): `Chapter100-01.png`, `176 Preview.png`, `173 Preview.png`, `Chapter36-01.png` (guardadas en `/tmp/claude-0/trabajo/90-kaguya-sama-love-is-war-texto/full/`).

**Tropedia** (mirror de TV Tropes en Fandom, reutilizando el wikitext ya bajado por el encargo hermano, filtrado por líneas con `[[...]]` para tropos de comedia: Off-Model, Super-Deformed, Gratuitous English, Faceless Masses, Breaking the Fourth Wall, etc. — no se repitió la llamada a la API, se reprocesó el mismo `tropedia.json` guardado en la carpeta de trabajo).

**Fontsource/fontTools** (obligatorio del punto 5, tanda nueva de 6 letras para esta parte, más el aviso de Kosugi Maru descartada): `permanent-marker`, `mochiy-pop-one`, `yomogi`, `reggae-one`, `kosugi-maru`, `dela-gothic-one` — `.ttf` bajados de `api.fontsource.org` (subset `latin`) y comprobados con `fontTools.ttLib.TTFont(f).getBestCmap()` para á/é/í/ó/ú/ñ/¿/¡/Á/Ñ. 5 de 6 con todos los caracteres; Kosugi Maru sin ninguno (anotado como aviso para el redactor).

No quedan puntos obligatorios pendientes de este rol (5, 6, 11, 18, 24, 25 completos, profundizando el ángulo de comedia y rótulos sin repetir la biblia hermana).
