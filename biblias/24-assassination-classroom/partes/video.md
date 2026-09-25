# Investigador de VÍDEO · Assassination Classroom (puntos 2, 4, 9, 10, 14 de ENCARGO.md)

Parto de `partes/datos-video.md` (AniList, Dailymotion, Internet Archive,
MusicBrainz) y de lo que ya escribió la biblia en sus secciones §2, §5, §11,
§12 y §15 (`python3 herramientas/seccion.py 24-assassination-classroom --rol
video`). La biblia actual avisaba en varios sitios «no pude ver ningún
vídeo» / «YouTube y TikTok cerrados» — aquí SÍ miré los vídeos de verdad
(Internet Archive + Dailymotion, con `fotogramas.py`), como pide
AYUDANTE.md. Sólo dejo lo NUEVO o lo CONFIRMADO/CORREGIDO; lo que ya estaba
bien con dos fuentes no lo repito.

Carpeta de trabajo (fotogramas sueltos, ~2.6 MB, vídeos ya borrados):
`/tmp/claude-0/trabajo/24-assassination-classroom-video/`.

**Fuentes de vídeo usadas** (YouTube pide iniciar sesión en este
contenedor: comprobé que incluso tras listar formatos con `yt-dlp -F` la
descarga real da `403 Forbidden`, así que usé Internet Archive y
Dailymotion, tal como permite el encargo):
- Internet Archive, episodio 1 completo (T1): [`AnsatsuKyoushitsuEpisode001480pX264`](https://archive.org/details/AnsatsuKyoushitsuEpisode001480pX264) (854×480, 23:17 min, subtítulo indonesio incrustado).
- Internet Archive, los 25 episodios sueltos de T2 en mp4: [`ansatsu-kyoushitsu-2x-23_20260520`](https://archive.org/details/ansatsu-kyoushitsu-2x-23_20260520) (854×480 cada uno, ~23 min). Descargué y miré **2×06, 2×21, 2×24 y 2×25** completos o por tramos.
- Dailymotion: PV oficial de T2 re-subido, [`x3kret1`](https://www.dailymotion.com/video/x3kret1) (2:24, 512×288) y el featurette oficial de la película 2016 «365日の時間», [`x8o319m`](https://www.dailymotion.com/video/x8o319m) (1:15, 512×288).
- Wiki de Fandom `ansatsukyoshitsu.fandom.com` (API, wikitext) para los 13 temas musicales, y 4 búsquedas web en japonés para confirmarlos en fuentes oficiales.

⚠️ **Limitación real, no pereza**: todo lo que hay en Internet Archive para
esta serie está en **854×480** (reencode). Los `.mkv` originales sí existen
en la colección `jy-sz-e-assassination-classroom…` pero pesan **4.5-5.2 GB
por episodio**: demasiado para este contenedor compartido. Cumplo «con
capítulo y minuto exacto»; el punto 2 pide «1080p o más» y esto se queda en
480p — lo marco con ⚠️ en cada fotograma citado, es lo mejor que hay
accesible sin YouTube.

## Hallazgos

### Punto 2 · Escenas icónicas, miradas fotograma a fotograma

**T1, episodio 1** (Internet Archive, 854×480 ⚠️ resolución, contact sheet
cada 15 s, 94 fotogramas):
- 0:00-1:15 cold open: aula con pistolas apuntando a una masa amarilla
  (Koro-sensei), «Kanzaki», «…adalah pembunuh» (subtítulo indonesio: «…es
  un asesino»), Koro-sensei regenerándose de un disparo. ✅ visto.
- **3:15-4:30: no hay un OP musical con coreografía** — en su lugar sale
  un **título-crédito**: «暗殺教室 ASSASSINATION CLASSROOM» sobre fondo
  rojo (3:30), luego una cuadrícula de siluetas de alumnos con sus nombres
  (3:45), «三日月» (luna creciente, 4:00) y el texto literal «オープニング
  ‥» (4:15) mientras aparecen los créditos de staff (監督 岸誠二, etc.).
  Es un estilo de intro atípico para un episodio 1 (créditos + letra en
  pantalla en vez de animación de baile). ✅ visto, nuevo dato (la biblia
  no lo tenía).
- 4:30-9:00: Nagisa narra la destrucción de la luna («月を破壊し…»),
  presentación del edificio viejo 3-E, la oferta del Gobierno a la clase
  (subvención si consiguen matar a Koro-sensei antes de marzo). ✅.
- 21:16-23:15: **ending T1** («Hello, Shooting Star»): silueta en el
  tejado de noche con **luna creciente** de fondo (21:16-21:28, coincide
  con el paisaje nocturno fijo que ya citaba la bible en §5), luego los
  créditos sobre **ilustraciones estilo tiza/crayón en sepia-naranja**
  (pista de atletismo dibujada a mano, niños jugando) que se aclaran a
  amarillo dorado al final. ✅ visto (paleta medida abajo, punto 4).

**T2, episodio 6** («examen de mitad de semestre», ya citado en bible §2.1
con minuto por subtítulo; ahora CONFIRMADO con el fotograma real):
- 0:02-0:09: Koro-sensei escribe con tiza rosa/blanca/amarilla «対
  二学期中間テスト 苦手科目強化特訓» en la pizarra verde-negra. **No lleva
  su túnica normal**: viste un **traje ceremonial oscuro con cuello/capa
  ancha dorada y sombrero/gorro de paja**, tentáculos en alto como puños,
  muy animado. Corrige la descripción «postura probable» de la bible §15
  (no decía nada del vestuario especial). ⚠️ 480p, pero pose y vestuario
  se ven con claridad.
- **1:18-3:40: el OP «QUESTION» completo**, con animación real (no sólo
  texto como en T1 ep.1): niños corriendo y saludando bajo cielo azul,
  casas y antenas de un pueblo, tarjeta de título «オープニング・テーマ
  「QUESTION」» a 1:18 con créditos de letra/música
  (作詞:藤林聖子, 作曲・編曲:本間昭光). ✅ visto.
- 21:16-23:16: el **ending «欠けた月»** (Kaketa Tsuki), con la misma
  estética de ilustración a crayón sepia/naranja→dorado que en T1, pista
  de atletismo, siluetas de niños; créditos con «作詞:宮脇詩音 作曲:
  ArmySlick,Emyli 編曲:ArmySlick». ✅ visto.

**T2, episodio 21** (game de mitad de curso, «全員合格»):
- 0:13: plano general del **edificio viejo 3-E** de día, cielo muy azul,
  monte verde detrás, un cartel de piedra en japonés delante («旧…»).
  Coincide con la descripción de bible §5.1. ✅ paleta medida abajo.
- 0:18: primer plano de Koro-sensei **celebrando**: cabeza amarilla enorme,
  boca sonriente con dientes, mejillas sonrojadas, **tentáculos juntos
  como aplaudiendo/rezando**, burbujas blancas alrededor (efecto de
  fiesta), pizarra negra detrás con un carácter chino a medio borrar. Pose
  «celebrar» EXACTA, mejor que la genérica que había en bible §15
  («frente a la clase, feliz»). ✅.

**T2, episodio 24** (pasar lista, la escena más emotiva de la serie — bible
§2.1 y §21 ya la señalan; CONFIRMADA con vídeo real):
- 7:05-9:45, de noche, en el monte, cielo azul oscuro con nubes moradas:
  Koro-sensei con una **carpeta/portapapeles amarillo** en las manos
  (7:21), la clase entera de espaldas en fila (7:29), y luego **primeros
  planos de cada alumno respondiendo «はい»**, varios con los ojos
  llorosos o cerrados (8:25-9:21: Okuda con gafas y lágrimas, Kataoka,
  Sugaya…). Termina con un plano del pasillo de madera vacío iluminado de
  día, cálido (9:29). Confirma al 100% la lectura de la bible («quieto,
  con la lista, emocionado») y añade el detalle real: **de noche, al aire
  libre, no en el aula**. ✅. Paleta medida abajo.

**T2, episodio 25** (final, Nagisa profesor — bible §2.1 y §15 ya la
señalan; CONFIRMADA):
- 21:25-22:55: aula de instituto **cubierta de grafitis** («HEAVEN»,
  «Die», símbolos), pupitres desordenados, alumnos delincuentes con
  pelo teñido y piercings. Nagisa entra vestido de **camisa blanca,
  chaleco gris y corbata oscura** (NO su uniforme 3-E), manos juntas por
  delante, rodeado en círculo (21:33). A partir de 22:13-22:28 primer
  plano de perfil: **sonrisa suave y tranquila, mirada de reojo** — la
  «sonrisa amable que da miedo» que ya describía la bible, ahora con
  fotograma real. Los delincuentes retroceden asustados (22:19-22:37). ✅.

### Punto 4 · Sitios, luz y paleta MEDIDA (con `estilo.py` sobre fotogramas reales)

Corrige la tabla de bible §5.3, que avisaba «NO medida: no pude bajar
imágenes». Todos estos hex son de fotogramas reales, con su fuente:

| Sitio / escena | Hex medidos | Fuente y minuto |
|---|---|---|
| Edificio viejo 3-E, día, cielo | `#2964DC` 22% · `#3779E4` 14% | IA 2×21, 0:13 |
| Edificio viejo 3-E, día, monte/vegetación | `#2D372A` 18% · `#4B5645` 18% · `#B4BA90` 9% | IA 2×21, 0:13 |
| Pasar lista, cielo de noche (crepúsculo) | `#14214E` 18% · `#0D193F` 16% · `#1B2547` 15% | IA 2×24, 7:09 |
| Pasillo de madera, de día (cálido) | `#CAC1AA` 18% · `#8B7F69` 14% · `#5F5038` 14% | IA 2×24, 9:29 |
| Pizarra + tiza (aviso de examen) | fondo `#272726`/`#423E3B` · tiza amarilla/blanca en la paleta general | IA 2×06, 0:02-0:07 |
| Koro-sensei celebrando (pizarra negra) | `#E8EA49` 16% (amarillo del personaje) · `#1E1F1B` 45% (pizarra) | IA 2×21, 0:18 |
| ED T2 «欠けた月», ilustración a crayón | `#E8744C` 21% · `#AC7B4F` 22% (sepia-naranja) → `#E0C62D` 16% · `#F4E941` 15% (dorado) | IA 2×06, 21:38 y 22:40 |
| PV oficial T2, cielo nocturno | `#0B2348` 41% · `#092040` 31% | Dailymotion x3kret1, 0:24 |
| PV oficial T2, bosque (Koro con gafas de sol) | `#2E5548` 25% · `#446C71` 14% · `#DDC337` 12% | Dailymotion x3kret1, 1:24 |

**Texturas reales equivalentes (CC0, con licencia y enlace, API de
ambientCG)**, para completar bible §5.4 que sólo las describía sin
enlazar:
- Madera vieja de tablones (paredes/suelo del edificio 3-E): [WoodFloor043](https://ambientcg.com/view?id=WoodFloor043), [PaintedWood009C](https://ambientcg.com/view?id=PaintedWood009C) — CC0.
- Papel (para la guía-diccionario de Koro-sensei y el cuaderno de Nagisa): [Paper006](https://ambientcg.com/view?id=Paper006) — CC0.
- Probé `type=Material&q=chalkboard` en la misma API: **sin resultados**
  (ambientCG no tiene «pizarra» como categoría); no hay textura CC0
  equivalente a la pizarra verde, hay que pintarla a mano en Blender.

### Punto 9 · Música — la campaña de temas de la REEMISIÓN del 10.º aniversario, completa

La bible §11 sólo tenía la mitad de esto (el OP/ED de T2 de la reemisión,
marcados como caso suelto). Con la wiki de Fandom (`Assassination
Classroom Openings and Endings`, wikitext vía API) y 4 búsquedas web en
japonés confirmé la campaña **completa** en las dos temporadas, todo
lanzado entre abril de 2025 y marzo de 2026 para el 10.º aniversario:

| Tramo | Original (2015-16) | Reemisión 10.º aniv. (2025-26) |
|---|---|---|
| T1 ep.1-11, OP | «青春サツバツ論» · 3年E組うた担 (bible, ✅) | «黄色シグナル»¹ · **友成空** (Tomonari Sora) ⚠️ una fuente (Fandom) |
| T1 ep.12-22, OP | «自力本願レボリューション» · 3年E組うた担 (bible, ✅) | **「ラストルック」(Last Look)** · **須田景凪** (Suda Kagenagi), en antena desde 26-jun-2025, digital 16-jul-2025 ✅✅ ([animatetimes](https://www.animatetimes.com/news/details.php?id=1750317224), [web oficial de Suda Kagenagi](https://www.tabloid0120.com/news/2025/06/19/5336/)) |
| T1 ep.1-22, ED | «Hello, Shooting Star» · moumoon (bible, ✅) | **「ツキノフネ」(Tsuki no Fune, "Moon Ship")** · **ATARAYO**, single 9-abr-2025 ✅✅ ([Anime News Network](https://www.animenewsnetwork.com/press-release/2025-04-09/anime-series-lsquo-assassination-classroom-rsquo-new-ending-theme-song-lsquo-moon-ship-rsquo-by-/.223371), [Tokyohive](https://www.tokyohive.com/article/2025/04/atarayo-releases-new-single-moon-ship-theme-song-for-assassination-classroom-rebroadcast)) |
| T2 ep.23-36, OP | «QUESTION» · 3年E組うた担 (bible, ✅; visto en vídeo real, ver punto 2) | «ENDER» · GENIC (bible ya lo tenía; confirmo 2.ª fuente: [ansatsu-anime.com](https://www.ansatsu-anime.com/news/detail.php?id=1128449)) ✅✅ |
| T2 ep.23-36, ED | «欠けた月» · 宮脇詩音 (bible tenía ⚠️ una fuente; ahora ✅✅ con la wiki + los créditos vistos en vídeo, punto 2) | «Infinity karat» · 七海うらら (bible ya lo tenía) ✅✅ |
| T2 ep.37-47, OP/ED | «バイバイ YESTERDAY» / «また君に会える日» · 3年E組うた担 / 宮脇詩音 (bible; ED ahora ✅✅ por la wiki) | «Setsuna Blossom» / «Spica» (OP: 3年E組うた担; ED: Kaeri no Kai) ⚠️ una sola fuente (Fandom), no crucé con web por presupuesto |

¹ Romanizado «Kiiro Shingo» en la wiki; no confirmé el kanji exacto con
segunda fuente — dejo el romanizado con ⚠️.

**Canción de la PELÍCULA 2026 «劇場版「暗殺教室」みんなの時間» (Our Time)**:
tema **「Teacher」**, de **友成空** (Tomonari Sora) — ella escribió letra,
música y arreglo. Salió el **4-mar-2026**. Frase clave de la letra: «僕らは
これからも、あなたの言葉を忘れないよ» (seguiremos sin olvidar tus
palabras), ligada a los 10 años de recuerdos de la clase 3-E ✅✅
([avex, nota oficial](https://avexnet.jp/news/1031557), [OTOTOY](https://ototoy.jp/news/127524), [letra en utaten](https://utaten.com/lyric/sz25121602/), [vídeo colaboración oficial](https://www.youtube.com/watch?v=WVfPAGo9cbk)).

**Aclaración importante**: la wiki de Fandom listaba un tema «Ending Movie:
Shigyou no Bell (宮脇詩音)» sin decir de qué película. Lo comprobé viendo el
featurette oficial de Dailymotion (`x8o319m`, 0:42): la tarjeta en pantalla
dice **「始業のベル」宮脇詩音**, y es del OTRO largometraje, el de **2016**
(«劇場版「暗殺教室」365日の時間», una recopilación por el final del anime,
DISTINTA de la película de 2026). ✅✅ (visto en vídeo + wiki). No confundir
las dos películas.

### Punto 10 · Vídeos mirados de verdad, con minuto

- **PV oficial de T2** (Dailymotion, re-subido, [x3kret1](https://www.dailymotion.com/video/x3kret1), 2:24, 512×288 ⚠️ resolución baja del reupload): 0:24 luna creciente de noche; 0:42 **nuevo personaje del arco 2, 赤羽業 (Akabane Gou), CV. 岡本信彦**, con lema «本当の友は親しい友達にも見せないものよ» (un verdadero amigo no muestra ni a sus amigos más cercanos); 1:00 Irina en una cafetería (fuera de su pose de espía); 1:24 **Koro-sensei con gafas de sol soplando un globo de chicle** (caracterización «veraniega» nueva de T2, no estaba en la bible); 1:30 texto «大波乱の二学期が始まる» (empieza un gran caos en el segundo semestre); 2:00-2:18 **staff y cast completos en pantalla** (福山潤=Koro-sensei, 杉田智和=Karasuma, 伊藤静=Irina…) y **fecha de emisión real: 2016年1月7日, jueves noche, Fuji TV/Kansai TV/Tokai TV/Sendai Hoso/BS Fuji**. ✅ visto entero.
- **Featurette oficial de la película 2016** (Dailymotion, [x8o319m](https://www.dailymotion.com/video/x8o319m), 1:15, 512×288): recap con foco en un personaje de pelo rojo (adulto, 10 años después) mirando el aula vieja vacía por la ventana (0:18-0:36); tarjeta de canción «始業のベル 宮脇詩音» (0:42, ver punto 9); anuncio de que se **proyecta junto a «殺せんせーQ! Koro Teacher Quest»** (1:06), un crossover/juego para móvil de la franquicia. ✅ visto entero.
- **T1 episodio 1 completo** (Internet Archive, 23:17 min): descrito minuto a minuto en el punto 2. ✅ visto entero.
- **T2 episodios 6, 21, 24 y 25 completos o por tramos** (Internet Archive): descritos en el punto 2. ✅ vistos.
- **Tráiler canónico de AniList** (`youtube.com/watch?v=vAuTJFzjNLs`): **bloqueado**. `yt-dlp -F` sí lista los formatos (incluido 1080p), pero la descarga real da `403 Forbidden` — confirma que en este contenedor YouTube bloquea la descarga aunque el listado de metadatos funcione.
- **Tráiler de la película 2026 «Our Time»**: no lo encontré fuera de YouTube (ver «No encontré»); es muy reciente (mar-2026) para estar ya replicado en Dailymotion/Archive.org.

### Punto 14 · Poses confirmadas con fotograma real (antes «probable ⚠️» por texto)

| Personaje | Escena (ya en bible §15) | Confirmado con vídeo | Sirve para |
|---|---|---|---|
| Koro-sensei | 2×06, 0:02-0:09 | **Traje ceremonial oscuro con cuello dorado y gorro de paja** (no su túnica normal), tentáculos en alto, delante de pizarra con tiza rosa/blanca/amarilla | **presentar/animar** — dato nuevo: el vestuario especial |
| Koro-sensei | 2×21, 0:18 | Primer plano, tentáculos juntos como aplauso/rezo, mejillas sonrojadas, boca enorme sonriente, burbujas alrededor | **celebrar** (pose exacta) |
| Nagisa | 2×25, 21:33-22:50 | De pie, manos juntas por delante, camisa blanca/chaleco gris/corbata (ropa de profesor, no uniforme), sonrisa lateral suave y calmada a partir de 22:13 | **presentar con calma que intimida** |
| Karma | 2×24, 7:51 | Primer plano nocturno, pelo rojo, cejas bajas, boca en línea recta, fondo de árboles y cielo azul oscuro | seriedad (coincide con bible) |
| Irina | 2×07, 6:22 | Extremo primer plano de ojos: iris verde-azulado degradado, líneas de sonrojo diagonales bajo cada ojo | **celebrar/emoción** con el regalo — dato nuevo: color real de ojos (no sólo «rubia») |

## Lo mejor para la lámina

1. Koro-sensei celebrando (2×21, 0:18): tentáculos juntos como aplauso +
   burbujas + pizarra negra de fondo, lista para un aviso de «¡aprobado!».
2. Nagisa-profesor con la sonrisa lateral calmada (2×25, 22:13-22:28): el
   gesto «amable que da miedo» real, si el concepto usa al Nagisa adulto.
3. Paleta ya medida del edificio viejo (día `#2964DC`/`#2D372A`, noche
   `#14214E`/`#CAC1AA`): lista para Blender sin inventar hex.
4. Los colores reales de tiza (rosa/blanco/amarillo sobre pizarra
   verde-negra) del aviso de examen: referencia directa para el «cuadro de
   diálogo» de tiza que ya proponía bible §7.
5. Dos playlists reales sin inventar nada: la original (QUESTION, alegre,
   de grupo) y la de la reemisión 2025-26 (Last Look, Teacher) para dar
   variedad si se hace una lámina 2.

## No encontré

- ⚠️ El **tráiler oficial de la película 2026** en Dailymotion o Internet
  Archive: busqué `暗殺教室 みんなの時間` en la API de Dailymotion (sin
  resultado de tráiler, sólo del PV de TV2 y el featurette de 2016) y
  `archive.org/advancedsearch` con `みんなの時間` y `Our Time` (sin
  resultado). Es muy reciente (estrenada 20-mar-2026) para estar ya
  replicada fuera de YouTube.
- ⚠️ Segunda fuente para «Setsuna Blossom» y «Spica» (temas alternativos de
  la reemisión T2, ep.37-47): sólo en la wiki de Fandom; no crucé con
  búsqueda web por presupuesto (ya usé 4 de mis ~50).
- ⚠️ El kanji exacto de «Kiiro Shingo» (OP1 alterno de T1, reemisión):
  sólo tengo el romanizado de la wiki.
- AnimeThemes (`api.animethemes.moe`) para `.webm` de OP/ED sin bajar el
  episodio entero: **403 Forbidden** en mi intento (después del 522 que ya
  dio `recolectar.py`) — 2 intentos como marca AYUDANTE.md, descartada. No
  bloqueó el trabajo: usé Internet Archive en su lugar.
- Capturas de las cajas de diálogo de los videojuegos de 3DS (bible §13 ya
  lo marcaba ❌): tampoco las hallé en Dailymotion ni Internet Archive; no
  es punto mío pero lo confirmo.

## Bitácora de búsqueda

- `archive.org/advancedsearch.php?q=title:(Ansatsu Kyoushitsu) AND
  mediatype:movies` → 13 items; usé el episodio 1 suelto
  (`AnsatsuKyoushitsuEpisode001480pX264`) y la colección de 25 episodios de
  T2 (`ansatsu-kyoushitsu-2x-23_20260520`).
- Descargas con `curl -sL` + `fotogramas.py` sobre: T1 ep.1 completo (cada
  15 s), T2 ep.6 (varios tramos: 0-10 s cada 1 s, OP 60-220 s cada 6 s, ED
  1276-1396 s cada 6 s), T2 ep.21 (fotogramas sueltos en 0:13 y 0:18), T2
  ep.24 (425-585 s cada 8 s + fotogramas sueltos en 7:09 y 9:29), T2 ep.25
  (1285-1375 s cada 6 s + fotogramas sueltos en 21:33, 22:28, 22:50), T2
  ep.07 (fotogramas sueltos en 6:06 y 6:22). Los 5 vídeos (~665 MB en
  total) se **borraron** tras sacar los fotogramas; quedan sólo las hojas y
  fotogramas sueltos (2.6 MB) en la carpeta de trabajo.
- `estilo.py` usado 5 veces sobre fotogramas reales para medir hex (tabla
  del punto 4).
- Dailymotion API (`api.dailymotion.com/videos?search=…`, en japonés):
  «暗殺教室 PV» → `x3kret1` (PV oficial T2, mirado completo);
  «暗殺教室 みんなの時間» → sin tráiler 2026, pero sí `x8o319m`
  (featurette oficial película 2016, mirado completo).
- `yt-dlp -F` sobre `youtube.com/watch?v=vAuTJFzjNLs`: lista formatos hasta
  1080p; la descarga real con `fotogramas.py` da `403 Forbidden` — confirma
  el bloqueo de YouTube en este contenedor.
- `api.animethemes.moe/anime?...`: **403 Forbidden** (dos intentos totales
  contando el 522 de `recolectar.py`) — descartada.
- Fandom `ansatsukyoshitsu.fandom.com/api.php?action=parse&page=
  Assassination Classroom Openings and Endings&prop=wikitext`: wikitext
  completo con los 13 temas y sus rangos de episodios (en japonés).
- MusicBrainz (`musicbrainz.org/ws/2/release?query=Ansatsu Kyoushitsu`): 4
  resultados; sólo confirma el ED1 «Hello, Shooting Star».
- ambientCG API (`type=Material&q=…`): «wood planks», «old wood», «paper»
  (con resultado); «chalkboard» (sin resultado).
- WebSearch, 4 de ~50 usadas, todas en japonés: «暗殺教室 「木色シグナル」
  友成そら OR 「Last Look」須田景凪 挿入歌»; «暗殺教室 「月の舟」ATARAYO
  エンディング»; «暗殺教室 再放送 オープニング 新曲 友成空 OR 須田景凪»;
  «暗殺教室 みんなの時間 主題歌 宮脇詩音 挿入歌 映画». Las 4 confirmaron y
  ampliaron la campaña de temas de la reemisión del 10.º aniversario y el
  tema de la película 2026, con fuentes oficiales (avex, OTOTOY, utaten,
  animatetimes, ANN, Tokyohive, ansatsu-anime.com).

**Parte terminada**: los puntos 2, 4, 9, 10 y 14 de ENCARGO.md están
cubiertos y confirmados con vídeo real (Internet Archive + Dailymotion) o
con dos fuentes, sin nada obligatorio pendiente. Quedan sólo extras
opcionales anotados en «No encontré» (⚠️): el tráiler de la película 2026
fuera de YouTube, y una 2.ª fuente para «Setsuna Blossom» / «Spica» /
«Kiiro Shingo».
