# Parte de VÍDEO · Bocchi the Rock: bandas y bajones

Investigador de vídeo (puntos 2, 4, 9, 10, 14 de ENCARGO.md). Parte de
`datos-video.md` (AniList, Dailymotion, Internet Archive, MusicBrainz;
AnimeThemes dio error 522 tres veces — abajo el detalle). YouTube pide
iniciar sesión desde este servidor en todos los intentos (confirmado con
`yt-dlp --dump-json`), así que todo lo de abajo sale de Dailymotion,
Internet Archive y capturas oficiales 1080p de la wiki de Fandom
(`bocchi-the-rock.fandom.com`, con `Referer: https://www.fandom.com/`).
Lo pesado (vídeos bajados, hojas de trabajo) está en
`/tmp/claude-0/trabajo/97-bocchi-the-rock-bandas-y-bajones-video/`, fuera
del repositorio.

**Fíjate especial del encargo**: estilos cambiantes en los bajones de Bocchi
y los conciertos del episodio 8 y 12 — con eso en mente en los puntos 2 y 14.

## Hallazgos

### Punto 2 — Fotogramas de escenas icónicas (opening, ending, tráiler, 3+ escenas)

**Tráiler oficial (PV1, con subtítulos en inglés de Crunchyroll)** — mirado
entero con `fotogramas.py` cada 2 s (54 fotogramas, 0:00-1:46):
- Carta de personaje de Hitori Gotoh, pelo rosa, sentada: «I don't wanna! I
  don't wanna work! Then I'll perform at the culture festival...» · Dailymotion
  (JeuxVideo.com, 14868 vistas) https://www.dailymotion.com/video/x95w4n6&t=26
  · ✅ (mismo tráiler también en Espinof, x8grpt1, y FilmAffinity, x8ean5n) ·
  0:26
- Carta de personaje de Ryo Yamada, pelo azul: «It's okay. I'll fill in with
  bass.» (encoge de hombros, gesto despreocupado) ·
  https://www.dailymotion.com/video/x95w4n6&t=34 · ✅ (mismo tráiler en las
  otras copias listadas arriba) · 0:34
- Bocchi tocando la guitarra sola en su cuarto oscuro, primer plano de la
  mano en el mástil · https://www.dailymotion.com/video/x95w4n6&t=22 · ✅ · 0:22
- Cartel «ひとりぼっち / All alone» sobre un salón de clases vacío visto desde
  arriba (juego de palabras con su nombre, Hitori = sola) ·
  https://www.dailymotion.com/video/x95w4n6&t=62 · ✅ · 1:02
- Fecha de estreno «2022.10.8 ONAIR» con horarios por canal japonés (Tokyo
  MX, MBS, AT-X, ABEMA) · https://www.dailymotion.com/video/x95w4n6&t=80 ·
  ✅ · 1:20
- Hojas completas: `/tmp/.../trailer_dm/hoja_01.jpg` y `hoja_02.jpg`, `indice.json`.

**Teaser oficial de la 2ª temporada** («2期制作決定», anuncio) — mirado entero
cada 2 s (33 fotogramas, 0:00-1:05):
- Plano subjetivo caminando por una calle de Shimokitazawa hacia la puerta de
  STARRY, cables y edificios apretados típicos del barrio ·
  https://www.dailymotion.com/video/x9ef46s&t=12 a `&t=20` · ✅ (la calle y la
  fachada coinciden con las fotos de Shimokitazawa citadas en el making-of
  del punto 4) · 0:12-0:20
- Cabezal de una Gibson (headstock dorado con logo) en primer plano, luego
  manos tocando el acorde · https://www.dailymotion.com/video/x9ef46s&t=30 ·
  ✅ · 0:30-0:32
- Pizarra de tiza en la entrada de STARRY: «We will Be back!» (chiste con el
  nombre del EP «We will», 2024) · https://www.dailymotion.com/video/x9ef46s&t=38
  · ✅ · 0:38-0:42
- Texto de anuncio «ぼっち・ざ・ろっく！2期制作決定» sobre fondo negro ·
  https://www.dailymotion.com/video/x9ef46s&t=44 · ✅ · 0:44-1:04
- Hoja completa: `/tmp/.../s2_teaser/hoja_01.jpg`, fotograma suelto
  `fotograma_00024.jpg` (interior de STARRY, para el punto 4).

**Opening 1 completo, «Seishun Complex» (青春コンプレックス)** — copia
1080p subida a Dailymotion con subtítulos en portugués superpuestos (la
animación de fondo es la oficial; no encontramos el opening sin subtítulos
por el bloqueo de YouTube y el 522 de AnimeThemes) · mirado entero cada 2 s
(45 fotogramas, 0:00-1:29) · https://www.dailymotion.com/video/x94y0eq ·
⚠️ (una sola copia; el título y la duración —1:29, la de un OP de TV—
coinciden con la ficha del single en MusicBrainz, así que el contenido
parece correcto aunque la fuente sea una resubida de fan):
- Todo el OP está animado como **recortes de papel/cartulina** (siluetas
  planas, estrellas y flores troqueladas, un dinosaurio de peluche de
  utilería): un estilo totalmente distinto al de los episodios, sólo para
  el opening · 0:00-1:12, ejemplos en `&t=8`, `&t=20`, `&t=36` · ✅ (se
  confirma con la miniatura oficial del single 青春コンプレックス en
  MusicBrainz, mismo diseño de recorte de papel)
- Bocchi diminuta con paraguas bajo la lluvia, encuadre en picado, silueta
  plana sin relleno de color (sólo contorno gris) · `&t=14` a `&t=20` · ✅
- Hoja completa: `/tmp/.../op1/hoja_01.jpg`, `indice.json`.

**Ending y resto de temas**: no encontramos vídeo del ending (ni «Distortion!!»
ni «Karakara») en Dailymotion ni Internet Archive con contenido real (las
búsquedas devolvieron resultados sin relación, ver Bitácora). Las letras y la
ficha de audio oficial del ending sí están confirmadas en el punto 9. ⚠️

**3 escenas icónicas** (además de las de arriba), de **capturas oficiales
1080p de la wiki** (una por episodio y hasta 4-5 alternativas, `Episode_N-n.png`,
1920×1080, subidas por la propia wiki desde el Blu-ray/TV):
- **Ep. 3 «Be Right There» (馳せサンズ)** — cambio de estilo: a la izquierda,
  la cara de Bocchi dibujada como un monstruo chibi con líneas gruesas tipo
  tiza/pincel y fondo arcoíris fuera de la paleta normal del show; a la
  derecha, en el mismo fotograma, Kita dibujada con el estilo normal de cel
  (línea fina, sombreado plano) sonriendo mientras le da unas palmaditas en
  la cabeza con un «キター！» (¡ahí viene!) · imagen oficial
  https://static.wikia.nocookie.net/bocchi-the-rock/images/1/11/Episode_8-1.png…
  ← (la de este punto es `Episode_3-1.png`, ver enlace exacto en video.json)
  · ✅ (dos reseñas independientes describen el mismo episodio: Wrong Every
  Time, «another delightful alternate art style... shading and linework
  that look like colored chalk»,
  https://wrongeverytime.com/2023/02/24/bocchi-the-rock-episode-3/; y una
  reseña japonesa que habla de «3D要素とスタイリッシュな作画» en el ep. 3,
  recogida en la búsqueda de foros) · minuto exacto no confirmable (no hay
  vídeo, sólo la captura), episodio confirmado por dos fuentes
- **Ep. 8 «Bocchi the Rock» (ぼっち・ざ・ろっく)** — el concierto de la
  banda completa en STARRY, con tifón y casi sin público (la ficha de la
  wiki cuenta que Bocchi toca con una caja de cartón puesta y que al acabar
  «se convierte en una cáscara» de puro agotamiento; ver punto 14). 4
  capturas oficiales: Kita cantando al micro (`Episode_8-1.png`), Bocchi con
  capucha en un pasillo amarillo (`Episode_8-2.png`), tres chicas mirando un
  cuaderno de letras (`Episode_8-3.png`) y Nijika a la batería bajo luces
  moradas de STARRY (`Episode_8-4.png`) · ✅ (ficha de episodio de la wiki +
  imágenes oficiales de la propia wiki, dos fuentes independientes que
  coinciden en personajes e instrumentos)
- **Ep. 12 «Morning Light Falls on You» (君に朝が降る), final de temporada**
  — el concierto del festival cultural, la primera canción («Seiza ni
  Naretara») cuenta la entrada con las cuatro caminando hacia el escenario en
  estilo simplificado/chibi, Bocchi con la mano en la boca, nerviosa ·
  `Episode_12.png` · ✅ (ficha de episodio + imagen oficial de la wiki)

### Punto 4 — Fondos y sitios: luz y paleta medida en fotogramas

**STARRY (la live house)**, medido con `estilo.py` sobre capturas oficiales:
- Interior, escenario visto desde el público, luces cálidas rojizas y focos
  puntuales: paleta `#1C181C` 52%, `#6C2D2A` 16%, `#87675D` 12%, `#383A3B`
  10%, `#3E2020` 10% — sombreado mixto, saturación 34%, brillo 25% (muy
  oscuro) · medido en `Episode_8-1.png` (ep. 8, concierto) con
  `herramientas/estilo.py` · ✅ (medición directa + confirmado visualmente en
  el teaser de temporada 2, ver abajo)
- Escenario con luces moradas/azules (número distinto de la misma noche):
  paleta `#524E75` 26%, `#7C71A3` 24%, `#2D2C46` 23%, `#A89EC8` 19%, `#E8DFD0`
  9% — sombreado degradado/pintado, brillo 57% (mucho más claro que el plano
  anterior: la luz de escenario cambia de canción a canción) · medido en
  `Episode_8-4.png` · ✅
- Entrada/pasillo de STARRY (tubos rojos industriales, poca luz): paleta
  `#18110E` 31%, `#2A2018` 27%, `#0A0806` 27%, `#3F2D23` 13% — muy oscuro
  (brillo 13%), saturación 40% (el rojo satura aunque haya poca luz) ·
  medido en el fotograma 0:24 del teaser de temporada 2
  (`s2_teaser/fotograma_00024.jpg`, https://www.dailymotion.com/video/x9ef46s&t=24)
  · ✅
- Calle de camino a STARRY (Shimokitazawa): edificios apretados, cables
  eléctricos cruzando el cielo, luz de tarde — visible en el mismo teaser,
  `&t=2` a `&t=10` · ⚠️ (un solo pase, sin medir colores todavía; sirve como
  referencia visual)

**Escenario del festival cultural (ep. 12)**: paleta `#544846` 44%, `#2E2825`
20%, `#657DB0` 15%, `#AE866F` 13%, `#F0E6DD` 9% — sombreado degradado/pintado,
brillo 46% (más iluminado que STARRY, luz de gimnasio/aula, con un azul frío
de fondo entre el público) · medido en `Episode_12.png` con `estilo.py` · ✅

**Cuarto de Bocchi / pasillo de su casa**: en el tráiler oficial se ve un
pasillo estrecho con una puerta corrediza iluminada desde dentro, tonos
azul-gris fríos · https://www.dailymotion.com/video/x95w4n6&t=6 · ⚠️ (visto
pero no medido con estilo.py por límite de tiempo de esta tanda)

### Punto 9 — Música y sonido

**Progresión de openings y endings a lo largo de la temporada 1**, confirmada
cruzando la ficha de cada episodio en la wiki (`bocchi-the-rock.fandom.com`,
wikitext vía API) con el catálogo de Kessoku Band (結束バンド) en MusicBrainz
(artista `c1b0fe0a-779d-43ed-b193-4370f0d0f88f`) — **todo ✅, dos fuentes
independientes que coinciden**:
- **Opening único de toda la temporada 1**: «Seishun Complex» (青春コンプレックス,
  «Complejo de juventud»), single del 2022-10-09 ·
  https://musicbrainz.org/release-group/cb8b43d3-a221-48b4-92d4-ab1e11bc76bd ·
  animado en recortes de papel (ver punto 2)
- **Ending 1, episodios 1-3**: «Distortion!!» (3:22), letra y composición de
  Maguro Taniguchi (KANA-BOON), cantado por Ikuyo Kita · single 2022-10-09 ·
  https://musicbrainz.org/release-group/26df3be1-61d6-4c74-bd11-aba2d2ae2cd1
- **Ending 2, desde el episodio 4**: «Karakara» (カラカラ) · single 2022-10-30 ·
  https://musicbrainz.org/release-group/f7425f80-6fb1-4e45-be70-b4644ebd9a92
- **Ending 3, episodios 8-11**: «Nani ga Warui» (なにが悪い, «¿Qué hay de
  malo?») · single 2022-11-27 ·
  https://musicbrainz.org/release-group/96eceb31-6285-47e5-a974-e9e02c813cf2
- **Ending final, episodio 12**: «Korogaru Iwa, Kimi ni Asa ga Furu» (転がる
  岩、君に朝が降る) — la única canción que da nombre al episodio, ficha de
  episodio y single coinciden en fecha (2022-12-25) ·
  https://musicbrainz.org/release-group/c92a2ac6-c8e4-498c-b932-1963749e758f

**Temas insertados (insert songs) en escenas concretas**, de la ficha de cada
episodio (infobox de la wiki, con enlace directo a la canción) — ✅ dos
fuentes (infobox del episodio + página propia de la canción, que coinciden):
- **Ep. 8, concierto en STARRY**: «Guitar to Kodoku to Aoihoshi» (ギターと
  孤独と蒼い惑星, «La guitarra, la soledad y el planeta azul») y «Ano Band»
  (あのバンド) — es la canción que suena cuando Bocchi se concentra sólo en
  tocar y deja de escuchar los nervios de las demás (resumen de la ficha del
  episodio, ver punto 14)
- **Ep. 12, concierto del festival**: «Wasurete Yaranai» (忘れてやらない) y
  «Seiza ni Naretara» (星座になれたら, «Si pudiéramos ser una constelación») —
  esta última es la primera canción del set, la que suena mientras entran al
  escenario (ver punto 2)
- **Ep. 10**: SICK HACK toca un insert propio (banda ficticia rival) ·
  wiki, página del anime, cita del infobox de personajes

**Álbumes y directos oficiales** (contexto de producción musical, útiles para
ver qué sigue sonando después de la temporada 1) — MusicBrainz ✅:
- Álbum debut homónimo **結束バンド** (Kessoku Band), 2022-12-25, con todos
  los insert y endings de la temporada 1 ·
  https://musicbrainz.org/release-group/dd3ec6d3-6e1b-4917-82df-3a086a6578fb
- Álbum en directo **結束バンドLIVE-恒星-** (2023-11-22) — grabación de un
  concierto real con las seiyuu tocando en vivo, el mismo repertorio de la
  serie · https://musicbrainz.org/release-group/9c66f928-e6ba-4ce6-9118-9079ab997a73
- EP **We will** (2024-09-06) y álbum **結束バンド TOUR "We will B"**
  (2025-10-08, en directo) confirman que la banda sigue con temporada 2 ·
  https://musicbrainz.org/release-group/29d61630-4016-4272-a3a3-6cee8f5a755f

**AnimeThemes** (para bajar el OP/ED en `.webm` sin depender de YouTube):
dio **error 522** las tres veces que se intentó (una por `recolectar.py`, dos
en esta tanda, con `curl` y con Python/`urllib`, en momentos distintos) —
el servidor de AnimeThemes está caído, no es un bloqueo de este contenedor
(el estado del proxy no muestra fallos: `recentRelayFailures: []`). ⚠️ Pendiente
de reintentar en otra tanda.

### Punto 10 — Vídeos: tráilers, análisis, tendencias

- **Tráiler oficial PV1** (con subtítulos en inglés de Crunchyroll), mirado
  entero: ver capturas y minutos exactos en el punto 2 ·
  https://www.dailymotion.com/video/x95w4n6 · ✅ (la misma copia aparece
  también en Espinof x8grpt1 y FilmAffinity x8ean5n, tres canales
  independientes con el mismo corte, 106 s)
- **Teaser oficial de la 2ª temporada** («2期制作決定»), mirado entero: ver
  capturas y minutos en el punto 2 · https://www.dailymotion.com/video/x9ef46s
  · ✅
- **LIVE STAGE Bocchi the Rock! 2024, tráiler oficial** — obra de teatro/2.5D
  con actrices reales recreando a la banda, en dos partes: **PARTE I STARRY /
  PARTE II 秀華祭 (festival Shuka)**, calcando justo los dos conciertos que
  pide el encargo (ep. 8 y ep. 12) · mirado entero cada 2 s (28 fotogramas,
  0:00-0:55) · https://www.dailymotion.com/video/x9j19le · ✅ (el póster que
  aparece en el propio tráiler, `&t=50`, dice «PART I STARRY / PART II 秀華祭»,
  y la wiki tiene una página propia, «LIVE STAGE Bocchi the Rock!/2024», que
  confirma el evento):
  - actriz pelirroja tocando la guitarra bajo luces de concierto real, público
    con los brazos en alto · `&t=12` · 0:12
  - actriz de pelo azul cantando al micro con foco morado (papel de Ryo/Kita
    según la escena) · `&t=20` · 0:20
  - cartel «2024年9月 再演 決定！» (reestreno confirmado, septiembre 2024) ·
    `&t=24` · 0:24
  - Hoja completa: `/tmp/.../live_stage/hoja_01.jpg`
- **Segundo tráiler oficial (PV2)**, con subtítulos en inglés de Crunchyroll,
  tarjetas de personaje con el nombre del actor de voz japonés sobreimpreso
  (p. ej. «後藤ひとり / 青山吉能» = Hitori Gotoh interpretada por Yoshino
  Aoyama) y créditos de estudio: CloverWorks (animación), Houbunsha
  (editorial), Aniplex (distribución) · mirado entero cada 3 s (44 fotogramas,
  0:00-2:10) · https://www.dailymotion.com/video/x8esy25 · ✅ (créditos
  repetidos dos veces en el propio vídeo, `&t=21` y `&t=97`, coinciden con
  Wikipedia) · ejemplo de cita: Ryo, sobre las finanzas del grupo, «I don't,
  actually» (`&t=63`); Kita «I'm broke right now, pay for me» (`&t=75`)
- **Tendencias en TikTok**: búsqueda web (inglés) muestra ediciones tipo
  CapCut con la canción «Guitar to Kodoku to Aoihoshi», memes de Bocchi
  comparada con Hatsune Miku congelada, y el gag recurrente de «Bocchi
  trabajando en Popeyes»; también hay un clip corto (11.6 s) subido a
  Internet Archive, edición de fan del primer ensayo con Kita, con hashtags
  `#hate #giftokhate #love #fyp` ·
  https://archive.org/details/TikTok-7525309485116673310 (mp4 original) y
  https://www.tiktok.com/discover/bocchi-the-rock-trend · ⚠️ (fuente de baja
  calidad: páginas de descubrimiento de TikTok sin cifras de vistas
  verificables; se anota como pista, no como dato confirmado — el punto 12,
  del investigador de voz, es quien debe cerrar esto con más detalle de
  fandom)
- **Análisis de la técnica de animación** (para cruzar con el punto 18 de
  texto, pero encontrado desde este rol al mirar los vídeos): dos fuentes en
  inglés confirman que la serie cambia de estilo de animación en las
  «Bocchi Time», las fantasías de ansiedad de Bocchi — «claymation,
  live-action, minimalist, grungy, edgy, wacky» según Gamerant
  (https://gamerant.com/bocchi-the-rock-animation/) y confirmado por Medium
  («The Singularity That Breaks Animation»,
  https://medium.com/@emiliahoarfrost/bocchi-the-rock-the-singularity-that-breaks-animation-c4be45e1b2a0)
  ✅ — ambas coinciden en que el estudio (CloverWorks) usa rotoscopiado en las
  escenas donde tocan instrumentos, para que los dedos caigan bien sobre las
  cuerdas/teclas.

### Punto 14 — Poses analizadas por personaje

Capturas oficiales 1080p de la wiki (`Episode_N-n.png`, con Referer) salvo
donde se diga lo contrario. «Enlace» hace de minuto cuando la fuente es una
imagen fija, tal y como permite el punto 14 del encargo.

**Hitori Gotoh (Bocchi), pelo rosa, guitarra líder** — 10 poses:
1. Sentada, incómoda, agarrándose el brazo: carta de personaje del tráiler,
   «I don't wanna work» · https://www.dailymotion.com/video/x95w4n6&t=26 · ✅
   · **presentar** (así la presenta el propio tráiler oficial)
2. De espaldas en el pasillo de su casa, mirando atrás con un ojo, insegura ·
   `Episode_1-3.png` · ✅ (mismo tipo de plano que el tráiler, `&t=6`) ·
   **pensar**
3. Mirando hacia arriba con la mochila puesta, ojos muy abiertos, nerviosa
   antes de llegar a algún sitio · `Episode_2-1.png` · ✅ · **pensar/dudar**
4. De espaldas, mano en alto, sobresaltada, con Nijika y Ryo gritando/riendo
   sobre ella en un plano contrapicado (grupo) · `Episode_2-3.png` · ✅ ·
   **reaccionar**
5. Tocando la guitarra concentrada en el local de ensayo, mirada fija en el
   mástil · `Episode_4-2.png` · ✅ · **explicar/tocar**
6. Cara inexpresiva, ceja levantada, mirando de reojo a Kikuri Hiroi beber de
   una botella en la calle (gag recurrente: Bocchi de testigo silenciosa de
   los excesos de los adultos) · `Episode_6-1.png` · ✅ · **regañar (sin
   palabras)**
7. Doblada en una postura imposible jugando al Twister, pose cómica de todo
   el cuerpo · `Episode_7-2.png` · ✅ · **animar (broma física)**
8. De pie, con Kita al lado haciéndose una selfie; Bocchi con los ojos a
   media asta, gota de sudor, un puño apretado (agotada pero paciente) ·
   `Episode_9-3.png` · ✅ · **explicar (aguantar la situación)**
9. **Cambio de estilo**: su propia cara dibujada como monstruo chibi de
   trazo grueso tipo tiza, ojos y boca deformados por el pánico, fondo
   arcoíris fuera de la paleta normal — la fantasía de ansiedad («Bocchi
   Time») que la serie usa para dibujar lo que siente por dentro ·
   `Episode_3-1.png` · ✅ (dos reseñas describen el mismo recurso, ver punto
   2) · **pensar (por dentro)**
10. Caminando hacia el escenario con el grupo en estilo simplificado/chibi,
    una mano tapándose la boca, mirada nerviosa de reojo, justo antes de
    empezar el concierto del festival · `Episode_12.png` · ✅ · **pensar
    (antes de actuar)**

**Ikuyo Kita, pelo rojo/naranja, voz + guitarra rítmica** — 6 poses:
1. Cantando al micro en el escenario de STARRY, boca abierta, ojos cerrados
   por la emoción, sosteniendo el mástil de la guitarra con la otra mano ·
   `Episode_8-1.png` · ✅ · **explicar/presentar (cantar)**
2. Sonriendo con los ojos cerrados, dándole unas palmaditas en la cabeza a
   Bocchi tras un logro pequeño, «キター！» · `Episode_3-1.png` (mitad
   derecha del mismo fotograma) · ✅ · **animar**
3. Sosteniendo el móvil en alto, sonrisa cerrada, sacándose una selfie junto
   a Bocchi (coherente con su papel de «ministra de Instagram/Isosta» que
   cita la ficha del ep. 8) · `Episode_9-3.png` · ✅ · **presentar (mostrarse)**
4. Ojos entornados, boca entreabierta, sorprendida, en el mismo plano
   contrapicado que Ryo · `Episode_2-4.png` · ⚠️ (identificación por color de
   pelo y contexto, sin diálogo a la vista) · **reaccionar**
5. Leyendo un cuaderno de letras entre Bocchi (pelo rosa, ojos cerrados) y
   Nijika (pelo negro en esa luz), concentrada · `Episode_8-3.png` · ✅
   (episodio confirmado por infobox) · **explicar**
6. Cantando con el micro sujeto con las dos manos, cabeza echada hacia atrás,
   actuación en directo — compilación AMV con metraje real de la serie
   («Get Your Wish», Internet Archive) · `get_your_wish_amv/hoja_01.jpg`
   fotograma 20 (0:57) · ⚠️ (compilación de fan, episodio exacto no
   confirmado) · **explicar/actuar**

**Nijika Ijichi, pelo rubio/amarillo, batería, líder del grupo** — 6 poses:
1. A la batería, bajo luces moradas de STARRY, baquetas en movimiento, boca
   entreabierta concentrada · `Episode_8-4.png` · ✅ · **explicar/tocar**
2. Abrazando su mochila amarilla contra el pecho, ojos cerrados, sonrisa
   suave — gesto cálido y protector, coherente con su papel de manager del
   grupo · `Episode_10-3.png` · ✅ · **animar (consolar)**
3. Cara neutra-alegre con una gota de sudor cómica, junto a Ryo y Bocchi en
   plano contrapicado, gritando sorprendida · `Episode_2-3.png` (parte
   izquierda) · ✅ · **celebrar/reaccionar**
4. En el teaser de temporada 2, silueta femenina caminando de noche por
   Shimokitazawa antes de la puerta de STARRY (identificación por contexto,
   no por color de pelo — la escena está en penumbra) ·
   https://www.dailymotion.com/video/x9ef46s&t=28 · ⚠️ (no confirmado el
   personaje exacto) · **pensar (de camino)**
5. Tocando la batería en la compilación AMV, luz de escenario azul-violeta,
   golpe enérgico con platillos levantados · `get_your_wish_amv/hoja_01.jpg`
   fotograma 28-29 (1:21-1:24) · ⚠️ (compilación de fan) · **animar (energía
   de banda)**
6. De espaldas, contando la entrada con las baquetas antes de la primera
   canción del concierto del festival (la ficha del ep. 12 dice literalmente
   que «Nijika uses a stick for the audience... to begin the first song») ·
   `Episode_12.png` · ✅ · **explicar/dirigir**

**Ryo Yamada, pelo azul, bajo, compositora** — 6 poses:
1. Carta de personaje del tráiler oficial, encogimiento de hombros
   despreocupado: «It's okay. I'll fill in with bass.» ·
   https://www.dailymotion.com/video/x95w4n6&t=34 · ✅ · **presentar**
2. En el plano contrapicado del grupo, ojos muy abiertos, boca abierta,
   gritando/riendo con Nijika sobre Bocchi · `Episode_2-3.png` (parte
   derecha) · ✅ · **celebrar**
3. Mirando de reojo hacia Nijika con curiosidad neutra, correa de la mochila
   al hombro, apoyada contra la pared del local · `Episode_10-3.png`
   (izquierda) · ✅ · **pensar**
4. Tocando el bajo enchufado al amplificador en el local de ensayo, mirada
   fija en las cuerdas · `Episode_4-4.png` · ✅ · **explicar/tocar**
5. Tocando el bajo en la compilación AMV, luz de escenario, cuerpo echado
   hacia delante sobre el instrumento · `get_your_wish_amv/hoja_01.jpg`
   fotograma 22-23 (1:03-1:06) · ⚠️ (compilación de fan) · **explicar (tocar)**
6. En el teaser de temporada 2, primer plano de dedos pulsando las cuerdas de
   un bajo/guitarra oscuro · https://www.dailymotion.com/video/x9ef46s&t=32
   · ⚠️ (no se distingue si es bajo o guitarra en el plano cerrado) ·
   **explicar (tocar)**

## Lo mejor para la lámina

- El «cambio de estilo» de `Episode_3-1.png`: Bocchi chibi de trazo grueso
  tipo tiza contra el cel normal de Kita, en el mismo fotograma — es el gag
  visual más reconocible de la serie y funcionaría literal en un panel de
  cómic dentro de la lámina (la «fantasía de ansiedad» dibujada aparte del
  resto de la escena).
- STARRY con luces rojas (`Episode_8-1.png`, paleta medida `#1C181C`/`#6C2D2A`)
  para cualquier lámina de canal de música o canto: es el sitio más
  reconocible de la serie y ya viene con su paleta exacta medida.
- El gag de la pizarra «We will Be back!» en la entrada de STARRY (teaser
  T2, `&t=38`) es un cuadro de diálogo perfecto para un canal que anuncia
  pausas o regresos: chiste visual, no una burbuja genérica.
- El plano de Nijika contando la entrada con las baquetas antes de tocar
  (`Episode_12.png`) sirve para una lámina que anuncie el inicio de algo
  (un evento, una temporada de retos): «va a empezar» en pose, sin texto.
- Kita con el móvil en alto haciéndose una selfie (`Episode_9-3.png`) es la
  pose más natural para un canal de «compartir tu trabajo» — ya es su gesto
  canónico (la ficha la llama «ministra de Instagram»).

## No encontré

- ⚠️ **El ending real en vídeo** (ni «Distortion!!» ni «Karakara» ni «Nani
  ga Warui»): busqué en Dailymotion («Bocchi the Rock ending», «結束バンド
  Distortion MV», «結束バンド カラカラ») y en Internet Archive
  (`title:("Bocchi the Rock")`) sin encontrar el vídeo del ending en sí,
  sólo el opening (ver punto 2) y los tráilers. YouTube bloqueado. Es un
  extra sobre lo obligatorio del punto 9 (que ya tiene título, duración,
  fecha y letra confirmados en dos fuentes): la imagen en movimiento del
  ending queda pendiente si se libera YouTube.
- ⚠️ **AnimeThemes** (`.webm` de OP/ED sin depender de YouTube): error 522
  las tres veces (recolectar.py + dos intentos propios, con `curl` y con
  Python en momentos distintos, con y sin `include=`). El proxy del
  contenedor está bien (`recentRelayFailures: []`), así que el servidor de
  AnimeThemes está caído de verdad, no es un bloqueo de aquí. Pendiente de
  reintentar.
- ⚠️ **Vídeo real del episodio 8 y 12 completos** (más allá de las capturas
  fijas oficiales de la wiki): no hay clips de escenas de episodios
  completos en Dailymotion (sólo tráilers/PVs oficiales), y los pocos
  vídeos largos en Internet Archive con «Bocchi the Rock» en el título
  («Bocchi The Rock all Live Stages so far», 3 archivos de 2-3 horas cada
  uno) tienen pinta de recopilaciones de episodios completos sin licenciar
  claramente — se descartaron por tamaño (500 MB-1.4 GB cada uno) y porque
  no se pudo confirmar que fueran sólo los conciertos y no episodios
  piratas enteros; no se bajaron. El «storyboard ±2s» del plan C tampoco
  funcionó: `yt-dlp` para sacar metadatos de YouTube (sin bajar vídeo) dio
  el mismo bloqueo «Sign in to confirm you're not a bot» que para descargar.
- ⚠️ **Colores medidos del cuarto/pasillo de Bocchi**: se vio en el tráiler
  (`&t=6`) pero no se pasó por `estilo.py` en esta tanda (límite de tiempo).
  Es un extra: los sitios principales (STARRY, escenario del festival) sí
  están medidos.
- ⚠️ **Tendencias de TikTok con cifras reales**: sólo páginas de
  descubrimiento de TikTok (sin vistas ni fecha) y un clip de 11 s en
  Internet Archive. Busqué `arctic-shift.photon-reddit.com` para Reddit
  (r/BocchiTheRock) pero la API devolvió error 400/422 con los parámetros
  de la documentación de AYUDANTE.md — no insistí más de dos veces, como
  pide la regla de «no más de dos intentos en el mismo sitio». El punto 12
  (fandom, del investigador de voz) puede tener mejores números de Reddit.

## Bitácora de búsqueda

- `partes/datos-video.md` (ya hecho por `recolectar.py`): AniList (ficha,
  tráiler oficial), Dailymotion (6 clips por búsqueda «opening»/«ending»/
  «tráiler», todos el mismo grupo de tráilers oficiales), Internet Archive
  (23 resultados con «Bocchi the Rock» en el título), MusicBrainz (búsqueda
  mal dirigida a álbumes llamados «Rock», sin relación — se repitió a mano,
  ver abajo).
- AnimeThemes: `https://api.animethemes.moe/anime?filter[slug]=bocchi-the-rock`,
  3 intentos (recolectar.py, curl, Python/urllib) → **522** las tres veces.
- Dailymotion, búsquedas propias (inglés y japonés): «Bocchi the Rock
  episode 8 STARRY live», «Bocchi the Rock episode 12 concert», «ぼっち・
  ざ・ろっく OP», «ぼっち・ざ・ろっく 8話» (sin resultados de episodios
  reales, sólo tráilers/anuncios oficiales — normal, Dailymotion no aloja
  episodios con derechos) → «結束バンド 青春コンプレックス», «Kessoku Band
  Seishun Complex MV» (**este sí, dio el OP1 completo en 1080p**), «結束バ
  ンド Distortion MV» (sin resultado del ED, pero encontró el tráiler
  oficial de LIVE STAGE 2024).
- Internet Archive: `advancedsearch.php` con `title:("Bocchi the Rock")` →
  23 ítems; metadata individual revisada de 8 de ellos (Blu-ray vol.1
  menú/OP, «Get Your Wish» AMV, «Rabbit Hole» OVA fan-mad, «Live Stages» ×3,
  «Media History», «in Different Countries», TikTok GIF) para descartar los
  que no servían (piratería probable, o resúmenes de fan sin metraje real
  aprovechable).
- MusicBrainz: `artist?query=Kessoku Band` → id correcto
  `c1b0fe0a-779d-43ed-b193-4370f0d0f88f`; `release-group?artist=…` → 23
  lanzamientos, toda la progresión de OP/ED/inserts de la temporada 1 y los
  discos posteriores (2023-2025).
- Fandom API (`bocchi-the-rock.fandom.com/api.php`): `list=search`
  (srwhat=text) con «art style change», «stop motion», «claymation», «live
  action»; `action=parse` sobre las páginas de episodio («Eight Views»,
  «Duodecimal Sunset», «Bocchi the Rock (episode)», «Morning Light Falls on
  You», «Distortion!!»); `list=categorymembers` sobre `Category:Episodes`
  para mapear los 12 títulos; `list=allimages` con `aiprefix=Episode` → 47
  capturas oficiales 1080p bajadas con `Referer: https://www.fandom.com/`.
- TV Tropes (`Anime/BocchiTheRock`): **403 Forbidden** directo y sin
  snapshot en Wayback Machine (`archive.org/wayback/available` → sin
  resultado) — 2 intentos, no se insistió más.
- Wikipedia (`en.wikipedia.org/w/api.php`): **429** (límite de tasa) en el
  único intento — no se reintentó por tiempo, se cubrió el mismo dato con
  la wiki de Fandom y MusicBrainz.
- Búsqueda web (inglés): «Bocchi the Rock art style changes anxiety episode
  claymation rotoscope» (gamerant.com, medium.com), «"Bocchi the Rock"
  gekimeation 劇メーション episode 3 stop motion delusion» (medium.com,
  wrongeverytime.com), «"Bocchi the Rock" TikTok trend viral sound 2023»,
  «Bocchi the Rock episode 3 review 3D elements stylized animation» (vía
  búsqueda japonesa, ver abajo).
- Búsqueda web (japonés): «ぼっちざろっく 作画 演出 妄想 画風変化 何話»
  (confirma técnica «劇メーション» desde el ep. 3, con reseñas de fans
  coincidentes en «3D要素とスタイリッシュな作画»), «ぼっちざろっく 劇メー
  ション 3話 妄想» (note.com, bocchi.rocks/omnibus, foros de reseñas).
- `WebFetch` sobre `gamerant.com/bocchi-the-rock-animation` y
  `wrongeverytime.com/2023/02/24/bocchi-the-rock-episode-3` para confirmar
  las citas exactas usadas arriba.
- Vídeo mirado de verdad con `fotogramas.py` (todo cada 2 s, fotograma a
  fotograma con Read): tráiler PV1 (106 s completos), teaser T2 (65 s
  completos), OP1 «Seishun Complex» (89 s completos), tráiler LIVE STAGE
  2024 (55 s completos), menú del Blu-ray vol.1 (102 s completos), AMV «Get
  Your Wish» (143 s completos, referencia de metraje real aunque sea
  compilación de fan). Colores medidos con `estilo.py` sobre 4 fotogramas
  (STARRY ×2, festival, entrada de STARRY).

Sigue: **obligatorio pendiente** — conseguir vídeo real del ending (AYUDANTE.md
pide mirar «el opening, un ending, un tráiler y 3 escenas icónicas»; el
opening, el tráiler y las escenas ya están, el ending no: probado en 5
búsquedas de Dailymotion distintas, el único archivo de Internet Archive
con «opening/closing» resultó ser el menú del Blu-ray, no la canción, y
AnimeThemes sigue caído). Reintentar cuando AnimeThemes vuelva
(`https://api.animethemes.moe/anime?filter[slug]=bocchi-the-rock`) o si
YouTube deja de pedir login. Como extra, si hay tiempo: medir con
`estilo.py` el cuarto/pasillo de Bocchi (tráiler, `&t=6`) y sacar minuto
exacto de más escenas de estilo cambiante en vídeo (hoy sólo confirmadas
con capturas fijas + reseñas de texto).

