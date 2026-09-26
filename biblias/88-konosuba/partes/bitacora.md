## Bitácora

### Bitácora de imagen

- `herramientas/investigar_serie.py --serie "Konosuba" --wiki konosuba --paginas "Kazuma Satou" "Aqua" "Megumin" "Darkness" "Axel" "Crimson Demon Village" "Devil King's Castle" "Wiz's Shop" "Royal Castle"`: 878 imágenes grandes indexadas, 7 hojas de contacto generadas (proceso cortado por el sistema tras la 7ª hoja; las 3 mejores copiadas a `hojas/`).
- API de `konosuba.fandom.com` (`action=query&list=search`) en inglés: confirmado el subdominio correcto y los títulos exactos de página de Kazuma Satou, Aqua, Megumin, Darkness, Axel, Crimson Demon Village, Devil King's Castle, Wiz's Shop, Kingdom of Belzerg, Royal Castle.
- Sketchfab API (`type=models&downloadable=true`), 4 búsquedas: `konosuba`, `megumin`, `kazuma konosuba`, `darkness konosuba` — 24+25+2+3 resultados, todos con licencia comprobada en el campo `license.label`.
- ambientcg API (`full_json?type=Material`), 6 búsquedas en inglés: `paper`, `fabric`, `leather`, `wood planks`, `metal gold`, `fabric diamond pattern` — todo CC0.
- WebSearch (3 usadas de las ~50 del cupo, en inglés y español): colaboraciones/café/figuras de Konosuba, wallpapers oficiales, KonoSuba Fantastic Days.
- Pillow + `herramientas/estilo.py`: 4 hojas de modelo T3 aplanadas sobre blanco (el canal alfa original las hacía dar colores falsos si no se aplanaban primero — aviso para quien reuse el script con PNG con transparencia), 2 trajes alternativos de Darkness (mucama, novia) y 4 capturas de sitios (Axel, Aldea Carmesí, tienda de Wiz, Castillo Real), con muestreo de parches 9×9 px para evitar el contorno de línea.
- No usé `navegar.py`: ninguna web con bloqueo (TV Tropes, Reddit) hizo falta para estos 6 puntos.
- Imágenes descargadas para medir (fuera del repositorio): `/tmp/claude-0/trabajo/88-konosuba-imagen/img/` (8 hojas de modelo/trajes + 4 sitios); se puede borrar tras subir la biblia.

### Bitácora de video

| # | Búsqueda | Idioma | Fuente | Resultado |
|---|---|---|---|---|
| 1 | `KonoSuba anime opening ending theme songs season 1 2 3 titles artists` | EN | WebSearch | OP/ED de las 3 temporadas confirmados ✅ |
| 2 | `api.animethemes.moe/anime?filter[slug]=...` | — | AnimeThemes API | HTTP 522 (caído desde este servidor, igual que en datos-video.md) ❌ |
| 3 | Fandom `action=query&list=search&srsearch=opening theme` | EN | konosuba.fandom.com API | Lista de 6 temas de apertura (anime + juegos) ✅ |
| 4 | Fandom `action=parse&page=Fantastic_dreamer/TOMORROW/Growing_Up/STAND_UP!/BLAST/Happy_Magic/It's_so_fine!` | EN | konosuba.fandom.com API | Fichas `{{Music}}` con fecha, duración, cantante ✅ |
| 5 | Fandom `action=query&list=categorymembers&cmtitle=Category:Endings` | EN | konosuba.fandom.com API | 9 endings listadas (anime + juegos) ✅ |
| 6 | Fandom `action=parse&page=Chiisana_Boukensha/Ouchi_ni_Kaeritai/Ano_Hi_no_mama_no_Bokura` | EN | konosuba.fandom.com API | Fichas de las 3 endings del anime, con seiyū como cantantes ✅ |
| 7 | Dailymotion API `search=Konosuba opening full` / `Konosuba ending` | — | api.dailymotion.com | Clips varios, mayoría cortos o mal etiquetados |
| 8 | Dailymotion API `search=Megumin explosion` / `Darkness Konosuba` / `Aqua Konosuba scene` / `Kazuma Konosuba` | EN | api.dailymotion.com | 3 escenas icónicas + recopilación de Aqua encontradas ✅ |
| 9 | Dailymotion API `search=Konosuba season 3 trailer` | EN | api.dailymotion.com | Tráiler oficial S3 (Official Trailer 2) ✅ |
| 10 | Dailymotion API `search=Fantastic Dreamer Konosuba full` / `Konosuba opening 1 full HD` | EN | api.dailymotion.com | OP1 real con cover fandub latino encima (KENBO) ✅ |
| 11 | Dailymotion API `search=Chiisana Boukensha full` / `ちいさな冒険者` / `おうちに帰りたい` / `Konosuba ED1 animation` | JA/EN | api.dailymotion.com | Sin resultado fiel al ED real ❌ |
| 12 | `archive.org/advancedsearch.php?q=konosuba+opening` | EN | Internet Archive | Sólo el OP del spin-off «Bakuen» (Megumin) en audio, no el OP principal |
| 13 | `fotogramas.py` sobre minuto 21:20-23:20 del episodio 1 «BD 1080p» de FFF en Internet Archive (para pescar el ED real) | — | Internet Archive | El archivo no es Konosuba (vídeo 3D mal etiquetado) ❌ — descartado |
| 14 | Dailymotion API `この素晴らしい世界に祝福を ED` / `Konosuba ED full screen` / `koi wo shite` (verso de letra) | JA/EN | api.dailymotion.com | Sin ED real ❌ |
| 15 | Dailymotion API `Lalatina Konosuba` / `Darkness Konosuba battle fight` / `Darkness Dustiness Konosuba` | EN | api.dailymotion.com | Sin poses nuevas de Darkness ❌ |
| 16 | `KonoSuba anime soundtrack composer "Masato Kōda"` | EN | WebSearch | Compositor confirmado (+ cruce con MusicBrainz de datos-video.md) ✅ |
| 17 | Fandom `action=parse&page=Give_Blessings_to_us_on_the_Road!` | EN | konosuba.fandom.com API | Confirma fecha del OST1 y cruza con MusicBrainz ✅ |
| — | `fotogramas.py` sobre 6 clips de Dailymotion (trailer, OP1, ED1-descartado, megumin_explosion, last_fight, aqua_recap, darkness_golem) | — | Dailymotion | 7 hojas de contacto vistas con Read ✅ |
| — | `estilo.py` sobre 4 fotogramas (castillo, campo+explosión, mansión, puerta de Axel) | — | Herramienta local | Hex + saturación/brillo medidos ✅ |
| — | `yt-dlp` directo sobre YouTube (tráiler de AniList) | — | YouTube | Bloqueado: «Sign in to confirm you're not a bot» ❌ (confirma la nota de AYUDANTE.md) |
| 18 | Dailymotion API `Chiisana Boukensha` / `konosuba ending` / `konosuba ED` / `この素晴らしい世界に祝福を ED` (relanzo) | JA/EN | api.dailymotion.com | Sin ED real, mismos resultados irrelevantes de siempre ❌ |
| 19 | `archive.org/metadata/` sobre 3 ítems candidatos (serie rusa completa T1 y T2, S2E2 suelto) | — | Internet Archive | Serie rusa T1 con 10 episodios .mp4 completos (imagen/audio original bajo doblaje) ✅ |
| 20 | `fotogramas.py` sobre episodio 1 (min 5:00, control) y episodio 2 (min 21:40-24:10, búsqueda del ED) del ítem `archive_etot_zamechatelnyy_mir_kono_subarashii_sekai_ni_shukufuku_wo` | — | Internet Archive | Episodio 1 confirmado como Konosuba real (Aqua); episodio 2 min 22:35-23:48 = ending real «Chiisana Boukensha» ✅✅ |
| 21 | `en.wikipedia.org/w/api.php?action=query&prop=extracts&titles=KonoSuba season 3` (relanzo, para sumar dominios distintos) | EN | Wikipedia API | Confirma OP3/ED3, fechas de emisión (10-abr a 19-jun-2024), canal (Tokyo MX) y streaming (Crunchyroll) ✅✅ |
| 22 | `WebSearch: Konosuba season 3 trailer tiktok viral trend` (relanzo) | EN | WebSearch | 9 enlaces de TikTok reales (vídeos y páginas de hashtag) — primera vez que se confirma que existen enlaces concretos, no sólo el bloqueo ✅ |
| 23 | `WebSearch: Konosuba season 3 trailer official announcement date Crunchyroll` (relanzo) | EN | WebSearch | Enlaces a Anime Corner, Dexerto, ComicBook, ScreenRant, Wikipedia — se eligió Anime Corner por ser el único legible con `navegar.py` (Dexerto es SPA sin contenido en el HTML servido) ✅ |
| 24 | `navegar.py` sobre `https://www.tiktok.com/tag/konosuba` y sobre dos vídeos sueltos de TikTok (relanzo, 2 intentos como marca AYUDANTE.md) | — | TikTok | Bloqueado: pide iniciar sesión / «Tenemos problemas para reproducir este vídeo» en ambos intentos ❌ — confirma el límite ya anotado |
| 25 | `navegar.py --selector article` sobre `animecorner.me/konosuba-season-3-anime-gets-first-main-trailer-april-premiere/amp/` (relanzo) | EN | Anime Corner | Artículo completo legible: fecha del tráiler, estudio, staff, reparto, compositor ✅ |
| 26 | `curl` directo sobre `animenewsnetwork.com/encyclopedia` (relanzo) | EN | Anime News Network | Bloqueado por verificación de seguridad (Cloudflare) ❌ — no se insistió (regla de dos intentos), se usó Anime Corner en su lugar |
| 27 | Dailymotion API `Darkness Konosuba armor` / `Konosuba Darkness masochist scene` / `ダクネス コノスバ` (JA) / `Konosuba Darkness confession scene` (relanzo, buscando 6ª pose) | JA/EN | api.dailymotion.com | Encontrado el clip `x5w5tow` (mismo gag del gólem ya usado) y `x7yuuzw` (nueva pose: Darkness regaña a Aqua, min 0:55) ✅ |

**Confirmado (✅):** OP/ED de las 3 temporadas (título, cantante, fecha) ahora con enlace directo en Fandom, Wikipedia y MusicBrainz (antes sólo texto); compositor de la BSO (Masato Kōda) con tres fuentes independientes (IMDb/Wikipedia, MusicBrainz, Anime Corner); opening y ending 1 vistos en vídeo real fotograma a fotograma; tráiler oficial T3 visto fotograma a fotograma y su ficha técnica confirmada por Anime Corner; 3 escenas icónicas vistas y citadas con minuto; 4 sitios con paleta medida; 23 poses de los 4 personajes con capítulo/clip y minuto; existencia de tendencia TikTok confirmada con 3 enlaces reales.
**A medias (⚠️):** contenido exacto de los vídeos de TikTok (bloqueados por login, sólo se confirmó que existen), 1 pose de Darkness por debajo del mínimo recomendado (5 de 6).

**Dominios distintos citados con enlace real en esta parte (relanzo, antes sólo 2):** dailymotion.com, archive.org, konosuba.fandom.com, musicbrainz.org, en.wikipedia.org, animecorner.me, tiktok.com.

### Bitácora de voz

- Doblaje Wiki, API `action=parse` (es): ficha de franquicia (ya en
  `datos-voz.md`) y ficha de la serie completa (nueva, con «Datos de
  interés», créditos y «Muestras multimedia»); `imageinfo|metadata` de 9
  `Archivo:` de vídeo para sacar sus videoId de YouTube sin pasar por
  YouTube.
- `konosuba.fandom.com`, API `action=parse` (en): fichas completas de
  Kazuma, Aqua, Megumin, Darkness y Yunyun.
- `voz.py` sobre 2 clips de Dailymotion (`x8qwfj9`, `xa0oox0`), modelos
  `tiny` y `small`; 2 intentos de bajar clips oficiales de YouTube con
  `voz.py` (fallaron por geobloqueo, no por sesión).
- `fotogramas.py --cortes` sobre 2 vídeos de Dailymotion (`x9avkfi`,
  `x8qwfj9`) y `--cada 15` sobre uno más (`xasu3fq`); 6 fotogramas sueltos
  en grande con `--fotograma`.
- Búsquedas web (todas en español o inglés, sin encontrar fuentes propias en
  japonés o coreano/chino más allá de lo ya citado de Wikipedia): «Konosuba
  encuesta popularidad personajes oficial Crunchyroll Anime Awards premio»,
  «ANMTV Konosuba doblaje latino reparto», «Konosuba fandom memes Megumin
  Day explosion», «Konosuba Know Your Meme Explosion Kazuma meme»,
  «Konosuba most emotional scene reddit», «reddit r/Konosuba identify with
  character», «Konosuba opening cover español latino fandub youtube»,
  «Konosuba fandub tiktok español parodia».
- `arctic-shift.photon-reddit.com`: `subreddit=Konosuba` (100 posts, sin
  filtro de fecha) y con `query=favorite character` / `query=cry` (sin
  resultados en estos dos últimos).
- Wikipedia (en), wikitext crudo vía `action=raw`: artículos «KonoSuba» y
  «Megumin», para sacar las citas originales (Crunchyroll News, Anime News
  Network, Newtype) en vez de quedarme con el resumen.
- `yt-dlp --skip-download --print` para metadatos (vistas, canal, fecha) de
  5 vídeos de YouTube sin necesitar sesión — funciona aunque bajar el audio
  o vídeo de clips geobloqueados falle.
- `navegar.py` sobre TV Tropes: falló por falta de navegador Chromium en el
  contenedor (ver «No encontré»).
- Relanzo (punto 13, cara de tristeza/vergüenza): `fotogramas.py --cortes`
  sobre dos episodios completos. (1) El spin-off *Kono Subarashii Sekai ni
  Bakuen wo!* ep. 1, doblado al español, en Dailymotion (`xa0oox0`, ya
  bajado por el investigador anterior) — 314 fotogramas, 0:00-22:43; sirvió
  para confirmar la tristeza de Megumin de niña (sentada sola, abrazando
  las rodillas, 18:15) pero no tiene a Kazuma/Aqua/Darkness (es sólo su
  pasado). (2) *Konosuba* temporada 2, episodio 2, en Internet Archive
  (`kono-subarashii-sekai-ni-shukufuku-wo-s-2-ep-2-tm`, MP4 directo de
  160 MB bajado con yt-dlp/ffmpeg) — 430 fotogramas, 0:00-23:39, con los 4
  principales; de ahí salen la tristeza de Aqua (4:45) y la vergüenza de
  Megumin (21:58) que quedan en la tabla del punto 13.

### Bitácora de texto

- Fandom `konosuba.fandom.com/api.php`: búsquedas de texto (`srsearch`) en inglés para «logo», «Axis Church symbol», «Crimson Demon Clan», «Adventurer Guild», «alphabet writing language», «manga page», «in the life», «Fantastic Days», «Eris Order» — todas con resultado, sin usar navegador (la API funciona directo, sin 403).
- Steam: `store.steampowered.com/search` y `api/appdetails` para localizar el juego con interfaz visible y sus 13 capturas oficiales 1920×1080; 4 bajadas y miradas con Read (contact sheet propio).
- WebSearch (en inglés): «Konosuba logo font title typography identification» → llevó a 2 hilos de dafont.com y a la página de HarJIT sobre el alfabeto del mundo. «Natsume Akatsuki interview influences Konosuba inspired by RPG games» → sin transcripción disponible.
- WebSearch (en japonés): «金崎貴臣 このすば インタビュー 制作 アニメーション» → llevó a la entrevista de ddnavi.com (leída completa); «このすば 爆発 エフェクト 作画 撮影 インタビュー Studio DEEN» → sin resultado específico de Konosuba, pero sí un tutorial profesional general de efectos de explosión usado igualmente.
- fontTools (`TTFont(f).getBestCmap()`) sobre Grobold.ttf y las 3 variantes de Tiki Tropic, descargadas de dafont.com (licencia «100% Free» comprobada en la ficha de cada fuente).
- Dailymotion + `fotogramas.py --cada 3`: tráiler oficial de la OVA (canal «Espinof», 48.679 vistas) completo, 11 fotogramas de 0:00 a 0:30; además 4 fotogramas propios con ffmpeg en 23.2/23.5/24.3/24.6 s para medir el color del logo de temporada 3 en el estallido. Vídeo borrado tras sacar las hojas.
- TCRF (`tcrf.net/api.php`) bloqueado por Cloudflare (challenge JS) tanto por curl como por `navegar.py` (falta el binario del navegador headless en el contenedor, versión 1243 vs 1194 instalada) — no se pudo entrar. TV Tropes da 403 directo por WebFetch y por curl; su copia en Wayback Machine también está bloqueada por política de red del contenedor («Blocked by egress policy» / reset de conexión), confirmado en dos intentos.
- Arctic Shift (Reddit) probado con el parámetro correcto (`query=`, no `q=`) sobre r/Konosuba, sin dato nuevo aprovechable para mis puntos.
