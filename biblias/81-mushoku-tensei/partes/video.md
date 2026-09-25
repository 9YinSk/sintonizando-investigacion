# Parte de VÍDEO · Mushoku Tensei: Jobless Reincarnation (encargo 81)

Investigador de vídeo: puntos 2, 4, 9, 10 y 14 de `ENCARGO.md`. Libreta de datos
(no prosa), un dato por línea. Parte de `partes/datos-video.md` (no se repiten
esas consultas). YouTube pedía iniciar sesión en este servidor (confirmado:
`yt-dlp` da «Sign in to confirm you're not a bot» en `JoS7Z8MCD6E`), así que se
usó Dailymotion e Internet Archive todo el rato, más `episodio.py` para ver
capítulos completos sin gastar.

## Fuentes de vídeo usadas (con qué se vio)

- Tráiler oficial japonés S1 (PV Crunchyroll, «2020年放送», con logo 無職転生,
  créditos de staff y branding Crunchyroll al final) · Dailymotion (subido por
  «Sensacine») · 1:59 · https://www.dailymotion.com/video/x8bc8ii · ✅ (mismo
  tráiler repetido también por JeuxVideo.com https://www.dailymotion.com/video/x9j3vu2)
  — visto entero con `fotogramas.py --cada 4` (30 fotogramas, hoja en
  `/tmp/claude-0/trabajo/81-mushoku-tensei-video/trailer1/hoja_01.jpg`).
- Opening Temporada 2 (creditless, UHD 60fps, 1:57) · Internet Archive ·
  https://archive.org/details/creditless-mushoku-tensei-season-2-op-opening-uhd-60-fps
  · ✅ — visto entero con `fotogramas.py --cada 3` (40 fotogramas, hoja en
  `/tmp/claude-0/trabajo/81-mushoku-tensei-video/op2/hoja_01.jpg`). Por el
  contenido (torres de Ranoa, Rudeus adolescente, grupo en mesa) coincide en
  escenario con el arco de la universidad (ep. 22-24 según Fandom) → probable
  Opening Theme 6 «Traveller's Song ~Homecoming~» (debut ep. 22); no hay forma
  de confirmar el número exacto sin oír la letra, así que queda ⚠️.
- Episodio 1 completo, «Jobless Reincarnation» (doblaje inglés, 1080p,
  23:47) · Internet Archive (colección con 10 episodios S1: E1-E5, E7-E11,
  falta E6) · https://archive.org/details/mushoku-tensei-jobless-reincarnation-e-2-1080p
  (archivo `Mushoku_Tensei_Jobless_Reincarnation-E1-1080p.mp4`) · ✅ — visto
  entero con `episodio.py --idioma en` (319 planos, ficha en
  `partes/episodios.md`) y con `fotogramas.py` en tramos concretos (nacimiento
  2:00-5:00, créditos/ending 21:50-23:47).
- Episodio 2, «Master» (introduce a Roxy como maestra) · mismo lote de
  Internet Archive, `Mushoku_Tensei_Jobless_Reincarnation-E2-1080p.mp4` · ✅ —
  visto con `fotogramas.py --cada 8` (hojas de contacto de todo el capítulo).

## Punto 9 · Música y sonido

### Openings de la temporada 1 (los 6 son la MISMA canción base «旅人の唄
/ Tabibito no Uta», reescrita por arco — dato curioso de producción)
- OP1 «Traveller's Song» (旅人の唄) · Yuiko Ōhara · TOHO animation RECORDS ·
  estreno 10-ene-2021, debut ep. 1 · https://mushokutensei.fandom.com/wiki/Opening_Theme_1 · ✅
  (confirmado además viendo el propio ep. 1: la ficha de créditos a las 23:06
  del episodio dice literalmente «旅人の唄 / 大原ゆい子 / 編曲 MANYO / TOHO
  animation RECORDS» — ver `ep01_ending/hoja_01.jpg` fotograma 20)
- OP2 «Awakening Song» (目覚めの唄) · Yuiko Ōhara · estreno 15-mar-2021 ·
  https://mushokutensei.fandom.com/wiki/Opening_Theme_2 · ✅
- OP3 «Inheritance song» (継承の唄) · Yuiko Ōhara · estreno 17-oct-2021 ·
  https://mushokutensei.fandom.com/wiki/Opening_Theme_3 · ✅
- OP4 «Prayer song» (Inori no uta) · Yuiko Ōhara · estreno 31-oct-2021, debut
  ep. 17 «Reunion» (reencuentro de Rudeus con su madre Zenith) ·
  https://mushokutensei.fandom.com/wiki/Opening_Theme_4 · ✅
- OP5 «Distant Lullaby song» (遠くの子守の唄) · Yuiko Ōhara ·
  https://mushokutensei.fandom.com/wiki/Opening_Theme_5 · ✅
- OP6 «Traveller's Song ~Homecoming~» (旅人の唄 ~帰郷~) · Yuiko Ōhara ·
  arreglo MANYO · debut ep. 22 «Reality (Dream)» ·
  https://mushokutensei.fandom.com/wiki/Opening_Theme_6 · ✅

### Openings de la temporada 2 (cambio de estilo: ya no es Yuiko Ōhara sola,
entran bandas)
- OP7 «spiral» · LONGMAN (letra y música Hiroya Hirai) · debut ep. 25
  «Brokenhearted Magician» · hay versión audio completa en Internet Archive
  (549 descargas) · https://archive.org/details/mushoku-tensei-season-2-opening-full-spiral-longman-lyrics-kan-rom-eng
  · https://mushokutensei.fandom.com/wiki/Opening_Theme_7 · ✅
- OP8 «on the front line» (オン・ザ・フロントライン) · HITORIE · letra
  Shinoda, música Yumao · Sony Music Associated Records · 3:29 · publicado
  15-abr-2024 · usado desde el ep. 18 «Turning Point 3» (Sisters Arc) ·
  https://mushokutensei.fandom.com/wiki/Opening_Theme_8 · ✅

### Endings de la temporada 1
- ED1 «Only» (オンリー) · Yuiko Ōhara · TOHO-animation RECORDS · 3:50/1:31 ·
  17-ene-2021 · debut ep. 2 «Master» · https://mushokutensei.fandom.com/wiki/Ending_Theme_1 · ✅
- ED2 «Kaze to Iku Michi» (風と行く道, «El camino que recorro con el
  viento») · Yuiko Ōhara · 3:50/1:30 · 3-oct-2021 · debut ep. 15 «The Woman
  with the Demon Eyes» · va con el OP4 en el ep. 17 «Reunion» (la escena de
  reencuentro con la madre) · https://mushokutensei.fandom.com/wiki/Ending_Theme_2 · ✅
- ED3 «Clover» · Yuiko Ōhara · arreglo MANYO · 4:51/1:30 · debut ep. 24
  «Guardian Fitz» · https://mushokutensei.fandom.com/wiki/Ending_Theme_3 · ✅
- ED4 «Musubime» (ムスビメ, «El nudo») · Yuiko Ōhara · debut ep. 26 «The
  Forest in the Dead of Night» (clímax del arco del Gran Bosque, Eris/Ruijerd) ·
  https://mushokutensei.fandom.com/wiki/Ending_Theme_4 · ✅

### Ending real del episodio 1 (visto en el propio capítulo, no en la wiki de
temas): usa la versión base «旅人の唄» sin subtítulo de arco — detalle que
NO sale en la ficha de Opening Theme 1 tal cual (la wiki la cataloga como
tema de apertura, pero en el ep. 1 suena también al cierre, antes de que
arranque el ED1 «Only» en el ep. 2) · ⚠️ (una fuente: el propio fotograma de
créditos; no lo confirma ninguna wiki en texto)

### Ambiente por escena (visto, no de memoria)
- Escena de nacimiento de Rudeus (ep. 1, 2:00-3:48): sin música de fondo,
  sólo ambiente de parto y llanto de bebé; luz cálida de velas · minuto
  https://archive.org/details/mushoku-tensei-jobless-reincarnation-e-2-1080p
  (archivo E1) t=2:36 · ✅ (visto)
- Cierre del ep. 1 (21:50-22:10): cena familiar iluminada con velas, tono
  íntimo, seguida del cartel de título «第一話 無職転生» sobre fondo rojo
  texturado (ver `ep01_ending/hoja_01.jpg`) · ✅ (visto)

### Efectos y onomatopeyas
- El tráiler oficial (Dailymotion x8bc8ii) no lleva SFX destacados propios
  (es corte de escenas con música); no se puede sacar onomatopeya de ahí.
- ⚠️ No encontré (todavía) una fuente textual (artbook, entrevista de sonido)
  que liste onomatopeyas oficiales del anime en pantalla; búsqueda pendiente
  en el propio manga (puede que sea mejor terreno para el investigador de
  texto, punto 6).

## Punto 2 · Fotogramas de escenas icónicas (capítulo y minuto)

- **Reincarnación / nacimiento de Rudeus** — ep. 1 «Jobless Reincarnation»,
  2:36-2:48: bebé recién nacido con ojos verdes (mirada de adulto en cuerpo de
  bebé, el gesto clave del pilot) sujetado en un paño, luego tres velas
  encendidas. Fuente: E1 Internet Archive (dub 1080p) ·
  `ep01_inicio/hoja_01.jpg` fotogramas 8-9 · ✅
- **Título de apertura «第一話 無職転生»** — ep. 1, 22:10, cartel rojo con
  textura de tela antes de los créditos · ✅ (visto)
- **Golden hour / niño Rudeus corriendo por el trigal** — tráiler oficial,
  0:04-0:20, plano recurrente de la promoción (portada del anime en varias
  webs de streaming) · Dailymotion x8bc8ii t=8 ·
  `trailer1/hoja_01.jpg` fotogramas 2-6 · ✅
- **Isla/templo flotando sobre el mar** — tráiler oficial, 0:24-0:28, plano
  de paisaje usado como transición · t=24 · ✅
- **Combate con criatura de colmillos grandes (bosque nevado/rocoso)** —
  tráiler oficial, 0:48-1:00, personaje con lanza contra una bestia blanca ·
  t=48-56 · ⚠️ (no identificado el personaje con certeza, posible escena del
  arco del Gran Bosque; sin confirmar en dos fuentes)
- **Manos entrelazadas en oración/ritual, luz dorada** — tráiler oficial,
  1:12-1:16 · t=72 · ✅
- **Combate final con relámpagos y criatura con ojo rojo (dragón/demonio)**
  — tráiler oficial, 1:42-1:59, la escena de cierre antes del logo · t=102 ·
  ✅ (aparece también recortada como preview en varias copias del mismo
  tráiler en Dailymotion)
- **Cena familiar con velas** — ep. 1, 21:54-22:02, Rudeus niño con sus
  padres Paul y Zenith y la sirvienta Lilia en la mesa · `ep01_ending/hoja_01.jpg`
  fotograma 2 · ✅

## Punto 4 · Luz y paleta medidas en fotogramas (con `estilo.py`)

- **Castillo de Ranoa de noche** (Opening S2, 0:39) — paleta: `#18243E`
  21% · `#2C3B5D` 20% · `#8C93BE` 17% · `#0C1120` 16% · `#7275A0` 15% ·
  `#465784` 11%. Sombreado degradado/pintado, saturación 48%, brillo 42% (azul
  noche, poco contraste, torres iluminadas por dentro). Fuente: fotograma
  propio · ✅
- **Interior cálido, grupo en mesa** (Opening S2, 0:51) — paleta: `#1E1412`
  29% · `#452E2E` 19% · `#847469` 16% · `#63524D` 13% · `#A9988F` 13% ·
  `#D5C8BE` 11%. Sombreado degradado, línea `#4E3F3B`, saturación 31%, brillo
  39% (marrones cálidos, luz de vela). Fuente: fotograma propio · ✅
- **Trigal al atardecer** (tráiler oficial, 0:08) — paleta: `#ECAD1F` 34% ·
  `#BE6617` 17% · `#F6EDC5` 9% · `#F2CE5B` 9% · `#76300D` 7%. Saturación 60%,
  brillo 65% (amarillo-naranja dominante, look «golden hour» muy marcado,
  poca línea). Fuente: fotograma propio · ✅
- **Mar/isla flotante de día** (tráiler oficial, 0:24) — paleta: `#DDF8F5`
  35% · `#48B0EA` 17% · `#5DC0F2` 13% · `#97D7F1` 12%. Sombreado plano (cel),
  saturación 27% (muy lavado), brillo 73%: cielo y mar casi del mismo celeste
  pálido. Fuente: fotograma propio · ✅
- **Caravana en desierto sobre montura tipo lagarto/tortuga** (tráiler
  oficial, 1:08) — paleta: `#D1A482` 21% · `#E8E2C5` 20% · `#817B5D` 12% ·
  `#563429` 11% · `#BB4F3A` 11%. Sombreado degradado, línea `#8C6848` normal,
  saturación 35%, brillo 54% (tierra y arena, tonos tostados). Fuente:
  fotograma propio · ✅

## Punto 10 · Vídeos, análisis y tendencias (con minuto)

- Tráiler oficial S1 (PV 2020, japonés, ramifica en Crunchyroll) · 1:59 ·
  https://www.dailymotion.com/video/x8bc8ii · ✅ (visto entero, ver punto 2)
- Tráiler doblado/VOSE de temporada 2 · 2:16 ·
  https://www.dailymotion.com/video/x8c9d35 (Sensacine) · ⚠️ (listado en
  `datos-video.md`, no se abrió fotograma a fotograma en esta tanda)
- Teaser de temporada 3 · Dailymotion, «Mushoku Tensei - Tráiler Oficial del
  nuevo arco» · 1:32 · https://www.dailymotion.com/video/x8yhi8e · ⚠️ (una
  fuente)
- «I'm Crashing Out Over this Teaser Trailer for Mushoku Tensei Season 3» ·
  vídeo de reacción, copia subida a Internet Archive ·
  https://archive.org/details/youtube-qpngswo2lc4 · ⚠️ (una fuente, título de
  reacción de fan, no oficial)
- Escena viral en TikTok: muerte de Geese Nukadia y reencuentro final con
  Ghislaine (personaje secundario, arco avanzado) — varios TikToks la citan
  como el momento que hizo llorar a la comunidad hispana y angloparlante ·
  ejemplos: https://www.tiktok.com/@el_luiisiitto/video/7367669814531263749
  («Escenas para el episodio 18 de Mushoku Tensei, no quiero llorar»,
  etiqueta rudeusgreyrat/sylphiette/roxygreyrat) y
  https://www.tiktok.com/@normanlance/video/7485145190907284791 («La Escena
  que Marcó la Temporada 2») · ✅ (dos publicaciones de TikTok distintas
  coinciden en el mismo momento)
- Vídeo de reacción a mitad de temporada 2 (episodio 2x17, antes del cierre
  del arco) marcado por fans como muy emotivo: «THIS SCENE HIT ME HARD...
  Mushoku Tensei 2x17 Reaction» · https://www.youtube.com/watch?v=XAnoAkTQN5o
  · ⚠️ (una fuente, no se pudo abrir el vídeo en sí por el bloqueo de
  YouTube; sólo título y buscador)
- Playlist de análisis dedicado: «Mushoku Tensei Analysis» (YouTube,
  colección) · https://www.youtube.com/playlist?list=PLAZDgAKa6ylrua9mTzvDstGQDDzQZy63A
  · ⚠️ (no abierto vídeo a vídeo, bloqueo de YouTube)
- Búsqueda web (es): «Mushoku Tensei escena viral TikTok momento icónico
  reacción» — resultados arriba.
- Búsqueda web (en): «Mushoku Tensei analysis video YouTube minute best scene
  reaction» — resultados arriba.

## Punto 14 · Poses analizadas (capítulo, minuto, qué hace)

### Rudeus Greyrat (bebé y niño, ep. 1 «Jobless Reincarnation»)
1. 2:36 — Recién nacido envuelto en un paño; ojos verdes muy abiertos mirando
   al techo (gesto de reconocimiento, no de bebé normal). Sirve para
   **presentar** (el «renacido» que despierta a su nueva vida). ✅
2. 2:48 — Manos diminutas agarrando el dedo de su madre Zenith. Sirve para
   **vínculo/ternura**, no para lámina de acción. ✅
3. 3:12 — Boca abajo en la cuna, sonriendo con las manitas levantadas.
   Sirve para **celebrar/alegría** simple de bebé. ✅
4. 3:18-3:24 — Ya gateando, mirando hacia arriba con curiosidad hacia una
   ventana con luz. Sirve para **animar/explorar**. ✅
5. 3:36 — De pie apoyado en una tina de agua, alcanzando un objeto en la
   repisa. Sirve para **pensar/investigar** (empieza a manipular objetos con
   intención de adulto). ✅
6. 4:24 — En brazos de su padre Paul, sonriendo con las manos hacia la
   cámara. Sirve para **celebrar** en familia. ✅
7. 4:36 — De pie solo junto a una ventana con parteluces circulares, mirando
   hacia afuera, postura erguida para su edad. Sirve para **pensar/mirar el
   horizonte** (foreshadowing de su curiosidad por la magia). ✅

Fuente de las 7: E1 Internet Archive (dub 1080p) · `ep01_inicio/hoja_01.jpg` ·
minutos exactos arriba.

### Escenas de personaje (tráiler oficial, sin identificar con certeza —
quedan como referencia de encuadre/pose, no de personaje concreto)
8. 0:16-0:20 — Niño de espaldas mirando el atardecer desde un promontorio,
   capa ondeando. Encuadre de **presentar** el mundo (silueta contra el
   trigal). Dailymotion x8bc8ii t=16 · ⚠️ (personaje no identificado con
   certeza, probablemente Rudeus niño por el peinado)
9. 0:56 — Personaje con lanza en pose de ataque bajo, cuerpo bajo y brazo
   extendido, contra una criatura blanca de colmillos grandes. Pose de
   **combate/atacar**. t=56 · ⚠️ (sin identificar el arma exacta ni el
   personaje)

## Lo mejor para la lámina

- El opening de temporada 2 da paletas ya medidas (azul noche del castillo de
  Ranoa `#18243E`/`#2C3B5D`, marrones cálidos de interior `#1E1412`) listas
  para un fondo nocturno de universidad mágica.
- El tráiler S1 da el «golden hour» icónico (`#ECAD1F`/`#BE6617`) que aparece
  en casi toda la promoción oficial: sirve de paleta de referencia para
  cualquier lámina ambientada al aire libre.
- La escena de nacimiento (ojos verdes de Rudeus bebé, ep. 1 min 2:36) es EL
  gesto de marca de la serie (alma adulta en cuerpo de niño): cualquier
  lámina de presentación de canal puede citarlo en texto sin necesidad de
  dibujar al bebé.
- El dato de que los 6 openings de temporada 1 son variaciones de la misma
  canción («旅人の唄») es un gancho de texto curioso para una ficha o post
  del canal de doblaje/canto.
- La escena viral de Geese/Ghislaine (TikTok, dos fuentes) es la prueba de
  qué momento mueve más al fandom hispano: útil para el redactor si el canal
  encaja con "voz.md"/emociones.

## No encontré

- ⚠️ Un ending oficial (creditless) por separado en Dailymotion o Internet
  Archive: no apareció ninguno con esos títulos exactos (busqué «Mushoku
  Tensei Only ending», «Kaze to Iku Michi», «Clover ending» en Dailymotion,
  sin resultados relevantes). Se compensó viendo el cierre real del episodio 1
  completo (créditos con el tema y el cartel de título).
- ⚠️ AnimeThemes (`api.animethemes.moe`) siguió caído en esta tanda (error
  522/timeout, igual que en `datos-video.md`): no se pudieron sacar los
  `.webm` de OP/ED que menciona `AYUDANTE.md` como atajo.
- ⚠️ SFX y onomatopeyas oficiales del anime (ficha aparte, entrevistas de
  sonido): no encontré una fuente dedicada; el tráiler no las muestra en
  texto. Pendiente si aparece en un artbook (mejor terreno para el
  investigador de texto/mundo, punto 6).
- ⚠️ Identificación segura de los personajes de las escenas de combate del
  tráiler (0:48-1:00, 1:42-1:59): sin un segundo fotograma claro de cara no
  pude confirmar si es Eris, Ruijerd u otro personaje; quedan marcadas ⚠️.

## Bitácora de búsqueda

- Comprobado `datos-video.md` (ya recolectado): tráiler AniList, clips
  Dailymotion, Internet Archive, MusicBrainz — no se repitieron esas
  consultas, se partió de ahí.
- `yt-dlp` directo sobre YouTube (`JoS7Z8MCD6E`): confirmado el bloqueo
  «Sign in to confirm you're not a bot» (HTTP 429 primero, luego el aviso de
  login) → se dejó YouTube y se trabajó con Dailymotion/Internet Archive.
- API de AnimeThemes (`api.animethemes.moe`): timeout/522 (igual que anotó
  `recolectar.py`) → descartada.
- Dailymotion API (`api.dailymotion.com/videos?search=`): búsquedas «Mushoku
  Tensei OP1», «opening 1 creditless», «ED1 creditless», «Only ending»,
  «Kaze to Iku Michi», «Clover ending», «Eris Goblin Slayer», «episode 17
  Reunion», «S1 E17» (en inglés) — encontró clips de fans/AMV pero no un
  OP/ED oficial suelto.
- Internet Archive (`archive.org/advancedsearch.php`, campo `title:`):
  búsquedas «Mushoku Tensei opening», «Mushoku Tensei OST», «Mushoku Tensei
  episode 1», «ending», «creditless», «trailer», «OP1», «ED1», «spiral»,
  «Confusion» (en inglés) → encontró el OP2 creditless UHD y el audio del OP7
  «spiral»; confirmó que los `turner_video_*` de `datos-video.md` son promos
  cortas (~2:20 min), no episodios completos.
- Wiki de Fandom (`mushokutensei.fandom.com/api.php`, `action=parse` y
  `action=query&list=search`/`list=categorymembers`): páginas «Reunion»,
  «Turning Point 3 (Anime)», «Opening Theme 1-8», «Ending Theme 1-4»,
  «Master (Episode)», «A Friend», «Route Selection», categoría «Episodes» (en
  inglés) → toda la ficha de temas musicales y episodios clave sale de aquí,
  con wikitext (no de memoria).
- Metadatos de Internet Archive (`archive.org/metadata/<id>`) para los
  `turner_video_*`, el lote `mushoku-tensei-jobless-reincarnation-e-2-1080p`
  (confirmó episodios 1-5, 7-11 en 1080p, falta el 6) y el OP2 creditless
  (nombre de archivo, duración, formato).
- `episodio.py` sobre el episodio 1 completo (dub inglés, 23:47): 319 planos
  detectados, ficha añadida a `partes/episodios.md`.
- `fotogramas.py` sobre: tráiler S1 completo, opening S2 completo, tramo de
  nacimiento del ep. 1 (2:00-5:00), tramo de créditos/ending del ep. 1
  (21:50-23:47), y episodio 2 completo (cada 8 s) para ver la llegada de
  Roxy.
- `estilo.py` sobre 5 fotogramas propios (castillo de Ranoa, interior cálido,
  trigal, mar/isla, caravana desierto) para paleta y tipo de sombreado.
- WebSearch (es): «Mushoku Tensei escena viral TikTok momento icónico
  reacción» → escena de Geese/Ghislaine confirmada en dos TikToks distintos.
- WebSearch (en): «Mushoku Tensei analysis video YouTube minute best scene
  reaction» → playlists de análisis y reacciones (YouTube bloqueado para
  abrir, sólo metadatos de búsqueda).

Sigue: revisar la hoja de contacto de `ep02` (llegada de Roxy, episodio 2) que
quedó generada pero sin mirar con Read; sacar 6-10 poses de Roxy y, si el
tiempo alcanza, de Sylphiette (episodio 3, aún sin descargar) y Eris (episodio
no identificado en el lote S1 disponible — buscar en qué episodio aparece);
completar el punto 14 para los 4 personajes del encargo (Rudeus ya tiene 7
poses, faltan Roxy, Eris y Sylphiette); rellenar `partes/video.json` con las
referencias de vídeo citadas arriba (`url`, `fuente`, `ancho`, `alto`,
`que_es`, `para_que`, `licencia`).
