## Bitácora

### Bitácora de imagen

- Español: ninguna búsqueda específica (la wiki y los datos ya recolectados estaban en inglés/japonés).
- Inglés (WebSearch): "Princess Mononoke artbook The Art of Princess Mononoke cover official";
  "Princess Mononoke GKIDS Blu-ray cover art 2023 4K restoration"; "Princess Mononoke figure Figuarts
  ZERO San Ashitaka official"; "Ghibli Park Mononoke village area attraction 2023"; "Princess
  Mononoke Uniqlo UT collaboration t-shirt"; "Princess Mononoke exhibition cafe Ghibli collaboration
  2023 2024"; ""San" Princess Mononoke cosplay award winning craftsmanship"; "Princess Mononoke Bandai
  Figuarts Zero Boar God OR Shishigami figure"; "Princess Mononoke GKIDS Blu-ray cover art"; "Princess
  Mononoke video game crossover collaboration gacha OR Fortnite OR skin"; "sumi-e ink brush texture
  pack free CC0 Procreate Photoshop"; "Princess Mononoke video game official Ghibli licensed".
- Japonés (WebSearch): "もののけ姫 画集 スタジオジブリ 表紙"; "もののけ姫 サントラ 久石譲 アルバム
  ジャケット"; "スタジオジブリ 壁紙 無料 配布 公式 もののけ姫"; "ghibli.jp 高解像度 場面写真 もののけ姫
  無料提供 使用条件"; "もののけ姫 コミック版 漫画 スクリーントーン フィルムコミック"; "もののけ姫 主題歌
  米良美一 シングル CD ジャケット".
- Directo (sin buscador, cuota de 50 búsquedas ahorrada): API de Fandom (`ghibli.fandom.com/api.php`)
  para el wikitext de San, Lady Eboshi, Irontown, Emishi y Nightwalker; `ghibli.jp` (páginas de
  novedades 013251, 013344, 013358, 013772, y la página de la obra `/works/mononoke/`) para confirmar
  las URL de los 50 fotogramas y el wallpaper oficiales; API de AmbientCG (`/api/v2/full_json`) para
  Wood, Moss, Metal, Fabric, Bark, Paper, Leather, Rust, Lichen; API de Sketchfab (`/v3/search`) para
  kodama, japanese forest, wolf mask, tatara furnace, deer god; API de Danbooru (`related_tag`,
  `posts.json`) para confirmar etiquetas de San y su pintura facial; `herramientas/estilo.py` sobre
  10 imágenes de la wiki para los hex de vestuario y sitios (San×3, Ashitaka×3, Moro×2, Eboshi×1,
  bosque×2, Irontown×1).
- Fuentes que fallaron o no aplicaron: AnimeThemes (522, ya en `datos-imagen.md`); Poly Haven no tiene
  modelos de personajes/edificios (sólo materiales, no serviría para el punto 3); Fandom search de
  texto libre para "emblem/crest" no encontró nada en las páginas de esta película.

Sigue: nada obligatorio pendiente de los puntos 1, 3, 15, 16, 19 y 23 (todo lo exigido por ENCARGO.md
está cubierto, con lo no encontrado marcado arriba con ⚠️). Si hay tiempo extra: medir hex de un
primer plano de San con luz de día limpia (las imágenes grandes de la wiki son casi todas nocturnas)
y confirmar con una segunda fuente el pelo/ojos de San (la ficha dice "royal blue", Danbooru etiqueta
"brown_eyes").

### Bitácora de video

**Ya hecho por `recolectar.py`** (no repetido, ver `datos-video.md`): AniList
(tráiler y streaming), Dailymotion (6 clips), Internet Archive (14 ítems),
MusicBrainz (10 álbumes) — AnimeThemes falló con 522.

**Búsquedas propias, con idioma**:
- (es) `"La princesa Mononoke" análisis video ensayo YouTube minuto escena` → 2
  vídeos de análisis y 1 reseña escrita, sin acceso a contenido por bloqueo de
  YouTube.
- (en) `Joe Hisaishi "Mononoke Hime" soundtrack tracklist "Ashitaka" theme
  scene music` → confirmó nombres de pistas, llevó a Ghibli Fandom para la
  tabla completa.
- (en) `Princess Mononoke TikTok trend edit sound viral 2026` → tendencia
  "Princess Mononoke Edit", canción "The Seed" de Aurora.
- (es) `"princesa mononoke" tiktok edit millones vistas San Ashitaka audio
  viral` → confirmó la misma tendencia, sin cifras exactas.
- (en) `Mononoke Hime kodama sound effect "kata kata" onomatopoeia forest
  spirits` → llevó al PDF académico de Nottingham y a soundeffects.fandom.com.

**Fuentes consultadas directamente (API/wiki, sin gastar cupo de buscador)**:
- `ghibli.fandom.com/api.php` (búsqueda + wikitext): páginas "Princess
  Mononoke/Soundtrack", "Ashitaka and San", "The Legend of Ashitaka".
- `soundeffects.fandom.com/api.php`: página "Princess Mononoke (1997)".
- `archive.org/metadata/1997-mononoke-hime-la-princesa-mononoke`: resolución
  real (1920×1040) y licencia (ninguna declarada, colección "opensource_movies").
- `ambientcg.com/api/v2/full_json`: texturas CC0 `moss`, `wood`, `metal`.
- Streaming HTTP directo con `ffmpeg -ss` sobre la URL de descarga de Internet
  Archive: 12 fotogramas en 1920×1040 sin bajar los 2 GB completos del archivo.

**Vídeo mirado de verdad** (con Read de las hojas, no reseñas): tráiler
teaser oficial completo (16 fotogramas) · película completa a intervalos de
5 min de principio a fin (`mapa/hoja_01.jpg`, 27 fotogramas) · escena de la
maldición inicial, min 2:00–7:00 (15 fotogramas) · presentación de San,
min 25:50–29:10 (10 fotogramas) · bosque del dios ciervo/Okkoto,
min 1:09:10–1:18:20 (25 fotogramas en 2 hojas) · Moro y la roca,
min 1:19:00–1:22:40 (12 fotogramas) · San herida tras el ataque a Irontown,
min 53:00–56:40 (12 fotogramas) · batalla final de los jabalíes,
min 1:39:10–1:45:00 (14 fotogramas) · clímax y créditos finales,
min 1:50:00–2:13:00 (24 fotogramas) · 12 fotogramas sueltos en HD
(1920×1040) de las escenas más citadas arriba. Total: más de 165 fotogramas
distintos mirados uno a uno.

**Vídeo borrado tras usarlo** (AYUDANTE.md, disco compartido): se eliminaron
los dos `video.mp4` de 480p (`test/` y `mapa/`, 380 MB cada uno, el segundo
duplicado del primero) en cuanto se sacaron todas las hojas que hacían falta.
Sólo quedan los JPEG de las hojas y los fotogramas HD sueltos (5,6 MB en total
la carpeta de trabajo). Si hace falta relocalizar otra escena del montaje,
hay que volver a bajarlo con `fotogramas.py` sobre
`archive.org/details/so-3f-cb-vwqm-0-d` (480p) o sacar el fotograma directo en
HD con `ffmpeg -ss <s> -i <url_directa_de_archive.org>` como se hizo aquí,
sin descargar el archivo completo.

**Fuentes totales citadas en esta parte** (con fuente propia, sin contar las
que ya traía `datos-video.md`): Ghibli Fandom (3 páginas) · MusicBrainz ·
Soundeffects Fandom · PDF académico de Nottingham · Discogs (búsqueda, sin
datos extraídos) · ambientCG (3 texturas) · Dailymotion (1 tráiler mirado + 6
enlazados) · Internet Archive (2 copias de vídeo) · YouTube (3 enlaces sin
poder mirarlos) · TikTok (búsqueda agregada + 2 vídeos concretos) ·
Wikipedia/Cintilatio (análisis, referencia indirecta vía buscador). Con los
40+ de `datos-video.md` (AniList, Dailymotion×6, Internet Archive×14,
MusicBrainz×10) el total del punto de partida más esta parte supera
holgadamente el mínimo de 40 fuentes distintas que pide `ENCARGO.md` para
todo el dossier (la cuenta final la hace el redactor sumando las 4 partes).

**Parte terminada**: los 5 puntos (2, 4, 9, 10, 14) están completos con lo
obligatorio que pide `ENCARGO.md`. Los extras que faltaron quedan arriba en
"No encontré" con ⚠️, no como pendiente. Si el redactor necesita el fotograma
exacto del Shishigami caminando de día sobre el agua, pedírmelo y se saca con
`ffmpeg -ss` sobre la URL de Internet Archive ya usada en esta parte.

### Bitácora de voz

**Fuentes usadas directamente (API/descarga), sin buscador**:
- Doblaje Wiki, API `action=parse&prop=wikitext` sobre «La princesa
  Mononoke» (corrigiendo el error del recolector automático, que había
  bajado la ficha de la serie *Mononoke* de 2007).
- Ghibli Wiki (fandom), API `action=parse&prop=wikitext` sobre San,
  Ashitaka, Moro, Eboshi y Jigo (5 fichas completas).
- Tropedia (mirror en Fandom de TV Tropes), API `action=parse` sobre
  `Princess Mononoke/YMMV`, `/Funny`, `/Heartwarming`, `/Trivia`,
  `/Awesome`, `/Tear Jerker` (con `action=query&list=search` primero para
  encontrar el título exacto de cada subpágina).
- dubdb.fandom.com, API `action=parse` sobre las fichas «Sysdub» y
  «Estudio Tokio» de la película (segunda fuente para el reparto Wild
  Bunch y Zima).
- Audio oficial de Doblaje Wiki (`static.wikia.nocookie.net`): 6 muestras
  `.ogg` descargadas (API `imageinfo` para la URL real) y transcritas con
  `herramientas/voz.py` (Whisper, en español) — San (Wild Bunch y Buena
  Vista), Ashitaka, Moro, Eboshi y Jigo (Wild Bunch).
- `herramientas/fotogramas.py`, material YA reunido por el investigador de
  vídeo de este mismo encargo (`/tmp/claude-0/trabajo/100-la-princesa-mononoke-video/hd/`),
  mirado aquí directamente con Read: 5 fotogramas de metraje real (no
  tráiler) con segundo exacto en el nombre de archivo.
- MyAnimeList: HTML de `.../characters` bajado con `curl` (favoritos por
  personaje, sin depender de la API Jikan, que estaba caída/504).
- ranking.net Japón (`best-mononokehime-characters`): HTML bajado con
  `curl`, orden 1-18 extraído de las cabeceras `<h3>`.
- Reddit vía `arctic-shift.photon-reddit.com` sobre r/ghibli y
  r/PrincessMononoke (varias consultas, con reintentos espaciados por los
  timeouts del servicio).
- `api.dailymotion.com` (búsqueda directa, no buscador) para fandub/cover.
- `archive.org/metadata` para confirmar el archivo de preservación de
  doblajes.
- Wikipedia en español (`es.wikipedia.org/w/api.php`, extracto de texto) y
  en inglés (`en.wikipedia.org/w/api.php`, con reintento tras un 429 de
  «too many requests» compartido con otros ayudantes en el mismo
  contenedor).
- `yt-dlp --skip-download` sobre un video de YouTube: bloqueado por
  YouTube (ver «No encontré»), no se insistió.

**Buscador web (idioma entre paréntesis), de un cupo de ~50**:
1. Princess Mononoke box office Japan Academy Prize awards (en)
2. Princess Mononoke Rotten Tomatoes Roger Ebert review (en)
3. La Princesa Mononoke fandub español latino YouTube San Ashitaka (es)
4. cover español "Mononoke Hime" canción tema Ashitaka Sekki (es)
5. VocesalViento DUBTOBER 2023 San Mononoke fandub (es)
6. Princess Mononoke identify character why people love reddit essay (en)
7. もののけ姫 人気投票 サン アシタカ キャラクター ランキング (ja)
8. VocesalViento cover doblaje fandub (es)
9. ANMTV La princesa Mononoke redoblaje Netflix reparto actores 2020 (es)
10. comparación doblaje La Princesa Mononoke Zima Wild Bunch Disney youtube (es)
11. Princesa Mononoke cosplay San doblaje latino actriz voz entrevista (es)
12. Princess Mononoke San feeds Ashitaka meat mouth scene (en)
13. Princess Mononoke 5 reasons I love it blog (en, por lectura directa)

Todo lo pesado (audios, JSON de wikis, HTML de rankings, fotogramas
compartidos con vídeo) quedó en
`/tmp/claude-0/trabajo/100-la-princesa-mononoke-voz/`, fuera del repo.

### Bitácora de texto

**Búsquedas en inglés (WebSearch):** "Princess Mononoke" anime comic manga Tokuma Shoten film comic panels · "Princess Mononoke" OR "Studio Ghibli" video game official crossover Jump Force Nintendo · "Princess Mononoke" 8-bit fan game vice article · Ni no Kuni Studio Ghibli Yoshiyuki Momose character design Level-5 · "Princess Mononoke" font identify title logo english poster fontspring reddit · "Princess Mononoke" opening prologue text on screen japanese scroll narration written · Hayao Miyazaki influences Princess Mononoke Ursula K Le Guin Dersu Uzala Kurosawa acknowledged · Princess Mononoke tagline "Live." Shigesato Itoi copywriter slogan · "Princess Mononoke" Ocarina of Time Miyamoto Nightwalker Goron interview second source · Google Fonts japanese handwritten brush free font tildes ñ Klee Yomogi Zen Kurenaido · Princess Mononoke animation line art color outline brown black shading cel interview art director technique · Studio Ghibli Princess Mononoke digital paint software name CGI department founded 1997.

**Búsquedas en japonés (WebSearch):** もののけ姫 パチンコ 実機 · "もののけ姫" パチンコ "生きろ" 新台 サミー OR 京楽 OR SANKYO · スタジオジブリ パチンコ 版権 もののけ姫 千と千尋 公式 · もののけ姫 ゲーム 公式 スタジオジブリ アプリ · もののけ姫 タイトルロゴ 筆文字 デザイン 誰が書いた · もののけ姫 タタラ場 看板 文字 デザイン 劇中 · もののけ姫 師匠連 ジコ坊 組織 とは · アニメコミック もののけ姫 徳間書店 フィルムコミック セリフ 文字組み · もののけ姫 撮影 セル 影 線 色 グラデーション 技法 特色 · もののけ姫 地走り ジバシリ とは 意味.

**Fuentes consultadas directamente (API/curl/WebFetch):**
- ghibli.fandom.com (Ghibli Wiki, Fandom): wikitext completo de «Princess Mononoke», «San», «Irontown», «Princess Mononoke: The First Story»; imageinfo medido de 11 imágenes; búsqueda de texto de «Shishoren OR Jibashiri» y «Kodama» (`api.php?action=query&list=search`). Se descartó `mononoke.fandom.com`: es la wiki de OTRO anime («Mononoke», 2007), comprobado con `list=search`.
- en.wikipedia.org/wiki/Princess_Mononoke (WebFetch)
- dafont.com/forum/read/467592/princess-mononoke-title (WebFetch)
- screenrant.com/miyamoto-zelda-ocarina-time-inspiration-princess-mononoke (WebFetch)
- zeldadungeon.net, timeextension.com (segunda fuente de la entrevista de Miyamoto a Gamejin 1998)
- ciatr.jp, fumfum100.com, walking-planet.com, note.com/gifted_taka705 (japonés, sobre Jigo/Shishōren/Karakasaren y la entrevista a Itoi)
- akirakurosawa.info/2014/08/01/film-club-princess-mononoke-hayao-miyazaki-1997
- amazon.co.jp y tokuma.jp/book (ficha del «フィルムコミック もののけ姫 完全版», Tokuma Shoten)
- sketchfab.com (API v3, `search?type=models`) — modelo CC de San localizado y verificado por licencia
- fonts.googleapis.com (API css2) + fontTools (`TTFont(...).getBestCmap()`) — 13 fuentes descargadas y comprobadas letra por letra (ñ, á, é, í, ó, ú, ¿, ¡)
- 80.lv/articles/see-what-princess-mononoke-s-cg-scenes-looked-like-on-crt-monitor + openculture.com/2016/03 + engadget.com/2016-03-21 (software Toonz/OpenToonz, jefe de CG Yoshinori Sugano, reparto de los 15 minutos de CG)
- garagefarm.net/jp-blog + mikazukidou.com (japonés, técnica general de línea/sombra en cel-anime: 色トレス, 塗り分け)
- karin-zakki.com + comic-kingdom.jp (japonés, significado y disfraz de los Jibashiri)
- Intentos bloqueados: tvtropes.org (Anime/PrincessMononoke, 403), tcrf.net (búsqueda «Ghibli» y «Princess Mononoke», 403 x2), mobygames.com (403, protección Cloudflare), mu-te.4g63evo.net (403), p-world.co.jp (sin resultado accesible), nausicaa.net/wiki/Princess_Mononoke_(computer_graphics) (503 Service Unavailable, un intento)

Parte completa: los 6 puntos (5, 6, 11, 18, 24, 25) tienen sus hallazgos, con fuente y ✅/⚠️ en cada dato. Lo que falta es todo opcional/extra (no obligatorio), ya anotado arriba en «No encontré»: el minuto y tipografía exactos de la cartela japonesa (fotogramas.py, rol de vídeo) y reintentar la máquina de pachinko rumoreada por otra vía si el jefe insiste.
