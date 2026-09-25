# Parte de VÍDEO · Tomb Raider (encargo 121)

Investigador de vídeo (puntos 2, 4, 9, 10, 14 de `ENCARGO.md`). Libreta de datos,
no prosa. Parte de `partes/datos-video.md` (no se repiten esas consultas) y de
`partes/episodios.md` (dos tráilers de Steam ya vistos con `episodio.py`).
Wiki usada: **tombraider.fandom.com** (nombre real del sitio: «Lara Croft Wiki»;
`laracroft.fandom.com` no existe, da 404 — comprobado).

YouTube pidió inicio de sesión en este servidor (comprobado con `yt-dlp -F` sobre
`https://www.youtube.com/watch?v=RN7_8Yholm4`, tráiler oficial «Turning Point»:
*"Sign in to confirm your age"*). Se usó el plan B: los mismos tráilers oficiales
alojados en el CDN de Steam (Akamai, ya listados en `episodios.md`), Internet
Archive y Dailymotion, tal como pide `AYUDANTE.md`.

Vídeo pesado y fotogramas en `/tmp/claude-0/trabajo/121-tomb-raider-video/`
(se borran los `.mp4` al terminar; las hojas se mencionan por ruta y también
quedan ahí, no en el repositorio).

## Hallazgos

### Punto 2 — Fotogramas de escenas icónicas (capítulo/nivel y minuto)

Es un videojuego: uso «nivel/misión» donde el encargo dice «capítulo». Mirado de
verdad con `fotogramas.py` (no leído de reseñas), fotograma a fotograma:

- **Tomb Raider (1996, PS1) — Nivel 1 «Caves» (la apertura del juego)**: menú de
  selección → pantalla «LOADING» → Lara corre y salta entre nieve y roca con las
  dos pistolas listas, se aprieta contra una pared apuntando a una amenaza fuera
  de plano (1:12), atraviesa una cámara con enredaderas y se sumerge en agua
  entre lianas (1:54-2:00), termina en pantalla de resultados «Caves · KILLS 1 ·
  PICKUPS 0 · SECRETS 0 of 3 · TIME TAKEN 3:12» (3:30) · fuente: longplay de
  Stacy Corron, parte 1, `https://archive.org/download/TombRaider_23930/TombRaider_23930_part01_512kb.mp4`
  (320×240, medido con `ffprobe`) · ✅ (nivel confirmado por la propia pantalla
  de resultados + orden de niveles del propio Internet Archive) · minutos exactos
  arriba.
- **Tomb Raider (1996) — Nivel 3 «Lost Valley»** (el nivel del T-Rex): jungla con
  ruinas cubiertas de vegetación, Lara corre, trepa y dispara; pantalla de
  resultados a los 6:58 confirma «Lost Valley · KILLS 5 · PICKUPS 5 · SECRETS 0
  of 5 · TIME TAKEN 6:58» (`/tmp/…/tr1-trex/fotograma_00443.jpg`) · fuente:
  misma longplay, parte 3, `…part03_512kb.mp4` (320×240) · ✅ (nivel confirmado
  igual). El T-Rex no salió en los fotogramas muestreados cada 8 s (el
  speedrunner esquiva o mata rápido a los 5 enemigos del nivel); no lo marco
  como visto, sólo el nivel y su fauna. ⚠️ (T-Rex en sí, no confirmado en imagen
  propia; sí documentado por la propia wiki en la ficha del nivel).
- **Tomb Raider (2013) — tráiler de revelación «Turning Point»** (la isla de
  Yamatai, naufragio inicial): silueta bajo el agua (0:08), escritorio con
  diario/celular de Lara (0:24), primeros planos de su cara (0:32-0:40), Lara
  atrapada en el interior rojo de un barco hundido (0:48), cara ensangrentada
  bocarriba tras un cristal (1:04), mano bajo el agua alcanzando la luz
  (1:12-1:28), caída agarrándose a rocas de una cueva (1:36-1:44), grito con la
  cara ensangrentada (2:24), agachada con arco improvisado, herida (2:32),
  costa con el barco naufragado al atardecer (2:40-2:48) · fuente:
  `https://video.akamai.steamstatic.com/store_trailers/203160/10727/bc433a91a02e76d1ea82a1bfaa6b9bf118a27429/1750498724/hls_264_master.m3u8?t=1447357498`
  (1280×720, medido) · minutos con `&t=` ya en `partes/episodios.md` · ✅ (tráiler
  oficial confirmado también por `tombraider.fandom.com` página
  «Tomb Raider (2013 Game)/Videos», que lo lista como *"Tomb Raider 'Turning
  Point' Debut Trailer"*).
- **Shadow of the Tomb Raider — tráiler de lanzamiento**: Lara camina hacia
  ruinas a contraluz (0:06), asesinato furtivo saltando sobre un enemigo desde
  arriba (0:12), río de selva visto desde el aire (0:24), Lara y el grupo
  (Jonah, Dr. Dominguez) frente a un mural iluminado con antorchas (0:42),
  persona con túnica indígena de espaldas (0:48), Lara con una pulsera de
  jade/piedra en la muñeca (0:54), explosión de luz (1:06), disparo agachada
  (1:12), salto/patada en el aire (1:24), plataforma industrial (1:30),
  explosión de fuego (1:36), primer plano pensativo mirando hacia abajo (1:48) ·
  fuente: `https://video.akamai.steamstatic.com/store_trailers/750920/183833/87b5a80178719395a8eacf41be455afc790e40a2/1750578719/hls_264_master.m3u8?t=1536601620`
  (1280×720) · ✅ (tráiler oficial de lanzamiento, PEGI/ESRB visible al inicio).
- **Tomb Raider (1996) — Nivel 15 «The Great Pyramid» (el final)**: corredores
  de piedra arenisca muy oscuros, cámara siguiendo a Lara de espaldas, en el
  minuto 5:00 un tramo minero oscuro con vetas brillantes en la roca
  (`/tmp/…/tr1-ending/fotograma_00300.jpg`); a los 11:54 un pasillo con paredes
  rojizas y talladas que lleva a la cámara final (antes del enfrentamiento con
  Natla) · fuente: misma longplay, parte 15, `…part15_512kb.mp4` (320×240) · ✅
  (nivel = último de los 15, confirmado por el orden de partes del propio ítem
  de archive.org, que coincide exactamente con los 15 niveles de la lista de
  tiempos del autor en la descripción del ítem).
- ⚠️ **Resolución**: todo lo anterior está en 720p (tráilers de Steam) o 320×240
  (capturas de PS1 de 2005 en Internet Archive), no en «1080p o más» como pide
  el punto 2. La fuente en 1080p+ sería el canal oficial de YouTube, bloqueado
  en este servidor (comprobado arriba). No hay atajo dentro de las reglas del
  encargo (no instalar programas de terceros para saltar el bloqueo).

### Punto 4 — Fondos y sitios: luz, paleta (hex) y textura equivalente

Paleta medida con `herramientas/estilo.py` sobre fotogramas propios (no de
memoria ni de paletas de fans):

- **Lost Valley (TR1, jungla con ruinas), fotograma 1:36 del nivel 3**: paleta
  dominante `#010202` 28% (sombra) · `#3A604E` 16.5% · `#2C4F3C` 14% ·
  `#1D3B28` 12.3% (verdes musgo/selva) · `#66947F`/`#7DB5A6` (verdes claros de
  vegetación iluminada) · luz de mediodía filtrada por hojas, sombreado
  degradado (no plano) · medido en `/tmp/…/paleta/fotograma_00096.jpg` (1280×960
  tras el procesado del fotograma, vídeo original 320×240) · textura real
  equivalente: musgo/piedra caliza cubierta de vegetación (buscar en
  ambientCG «moss» o «limestone»).
- **Isla de Yamatai, playa del naufragio (TR 2013), tráiler «Turning Point»
  2:48**: paleta `#101208` 21.5% · `#262617` 21.2% (arena oscurecida) ·
  `#4A412A`/`#7D6848`/`#A88C63`/`#D3B07E` (tonos arena-madera) · `#FFFEDD`/
  `#F5DDA4` (brillo del atardecer, 10.7% y 7.6%) · luz de atardecer/dorada baja,
  sombreado degradado, saturación 43%, brillo medio 45% · medido en
  `/tmp/…/paleta/fotograma_00168.jpg` (1280×720) · textura real: madera de
  barco oxidada/podrida, metal oxidado.
- **Templo de Paititi, entrada en penumbra (Shadow of the Tomb Raider),
  tráiler de lanzamiento 0:06**: paleta `#201A0C` 24.2% · `#2F2810` 19.7% ·
  `#141108` 17.7% (negros cálidos) · `#423B1B`/`#585639` (verdes oliva oscuros)
  · un verde vivo `#9DD34E` sólo 0.6% (vegetación puntual a contraluz) · luz a
  contraluz (silueta), saturación 55%, brillo muy bajo (18%) · medido en
  `/tmp/…/paleta/fotograma_00006.jpg` (1280×720) · textura real: piedra maya
  tallada, musgo.
- **The Great Pyramid, tramo final (TR1), minuto 5:00 del nivel 15**: paleta
  casi monocroma `#101211` 27.3% · `#161917` 16.4% · `#202320` 15.7% ·
  `#2C2F2B`/`#3A3D3A` (grises verdosos) · saturación muy baja (13%), brillo 14%:
  un corredor minero oscurísimo con una sola fuente de luz frontal (la linterna
  de cámara del juego de 1996, no un foco propio de Lara) · medido en
  `/tmp/…/paleta/fotograma_00300.jpg` (1280×960 tras el procesado, vídeo
  320×240) · textura real: roca volcánica/mineral con vetas.
- Las cuatro medidas muestran el contraste que pide el encargo: selva a
  mediodía (verdes), costa al atardecer (ámbar/dorado), templo a contraluz
  (oliva oscuro) y tumba interior casi sin luz (gris-verde). ✅ (paleta medida
  por herramienta propia sobre fotograma propio, no de memoria).

### Punto 9 — Música y sonido

- **Tomb Raider (1996-1998)**: compuesta por **Nathan McCree** con
  sintetizador (no orquesta real) · fuente: `datos-video.md`
  (MusicBrainz) + página wiki «Nathan McCree» (`tombraider.fandom.com`,
  wikitext comprobado) · ✅. El tema de las cuevas de los 4 primeros niveles se
  conoce como **«Cave»**; McCree valoraba el silencio y el espacio por encima
  del ruido constante (la música casi no suena durante la exploración, sólo en
  momentos concretos, para dar tensión) · fuente: interview.
- **Cita textual de Nathan McCree** sobre la falta de un tema propio en el
  reboot de 2013: *"...it is a complete disaster for the franchise. It is like
  releasing a James Bond movie without Monty Norman's classic theme. To this
  day, I don't know why Eidos decided to weaken their prize possesion!"* ·
  fuente: entrevista de Daryl Baxter, recogida en
  `http://www.musicoftombraider.com/2013/11/interview-with-tomb-raider-legacy.html`
  (27-nov-2013) · ✅ (entrevista publicada, con nombre de autor y fecha) — sirve
  para el punto 21 (por qué el fandom más veterano no ama del todo el reboot en
  lo sonoro) y el 24 (comparación con el «tema de James Bond» que el propio
  compositor usa).
- **Tomb Raider (2013)**: compositor **Jason Graves**. Se construyó un
  **instrumento a medida** (madera, vidrio y metales, hecho por el escultor
  Matt McConnell, vecino de Graves) que se toca con arco o percutido; el arco
  está modelado sobre el arco improvisado de Lara. Ese instrumento se usó en
  exclusiva para la misión inicial «Scavenger's Den» y da los sonidos de
  tensión al correr/escapar · fuente: `tombraider.fandom.com`, página
  «Tomb Raider (2013 Game)/Music» (wikitext) · ✅. Lista de pistas incluye
  **«Adventure Found Me»** como primer tema — la misma frase («Adventure found
  me») es la que narra Lara al segundo 0:00-0:24 del tráiler «Turning Point»
  (ver `episodios.md`), es decir el tema y el tráiler comparten título/frase ·
  ✅ (dos fuentes: página de música de la wiki + transcripción propia del
  tráiler).
- **Rise of the Tomb Raider**: compositor **Bobby Tahouri**, que reutiliza
  **«Lara's Theme»** de Jason Graves dentro de la partitura · además, la
  canción **«I Shall Rise»**, cantada por **Karen O** (de Yeah Yeah Yeahs), se
  encargó como tema promocional — colaboración con una artista indie conocida,
  no sólo compositor de videojuegos · fuente: `tombraider.fandom.com`, página
  «Rise of the Tomb Raider/Music» · ✅.
- **Shadow of the Tomb Raider**: compositor **Brian D'Oliveira**. Lista de
  pistas con nombres que marcan los momentos emotivos de la historia:
  «Innocent Death», «Sacrifice», «Baptism of Fire» (la escena bautismal/de
  inundación del templo, coherente con la escena homónima que da nombre al
  juego), «Hope», «Death of the Sun», «Goodbye Paititi» · fuente:
  `tombraider.fandom.com`, página «Shadow of the Tomb Raider/Music» · ✅
  (existencia y nombres de las pistas, oficiales) / ⚠️ (no pude verificar viendo
  la escena exacta que acompaña cada pista, sólo el título oficial: lo marco
  como pendiente para quien monte la lámina con el juego delante).
- **Efectos de sonido reconocibles**: ⚠️ no encontré una fuente sólida con
  nombres oficiales de los efectos más famosos (el «tintineo» de recoger un
  objeto, el sonido del cristal de guardado). Hay un banco de audio extraído
  del juego en `https://sounds.spriters-resource.com/pc_computer/tombraider/asset/428378/`
  (confirma que existen y están catalogados, pero la página es una lámina de
  ondas de sonido sin texto descriptivo aprovechable) y un hilo dedicado en
  Tomb Raider Forums (`tombraiderforums.com/showthread.php?t=185866`,
  «Complete Tomb Raider 1 sound effects») que no pude abrir: Cloudflare devolvió
  «Just a moment...» (challenge) las dos veces que lo intenté. Queda en
  «No encontré» más abajo.

### Punto 10 — Vídeos: tráilers, análisis, tendencias, con minuto exacto

- **2 tráilers oficiales mirados fotograma a fotograma** (con minuto exacto):
  «Turning Point» (revelación de Tomb Raider 2013) y el tráiler de lanzamiento
  de Shadow of the Tomb Raider — detalle completo en el punto 2 de esta parte,
  y transcripción palabra por palabra en `partes/episodios.md`. ✅.
- **Vídeo de análisis/retrospectiva** (mirado con `fotogramas.py`, no leído de
  resumen): programa francés **«Le Fond De L'affaire»** del canal **Globtopus**
  sobre la historia de Tomb Raider, mezclando metraje de varios juegos con
  humor (dirección: Maxime Robinet; guion: Nicolas Trouillé, Rodolphe Riton,
  Kevin Poncin — créditos leídos en pantalla a los 8:00). Contenido con minuto:
  0:30 corredor con palanca de TR1, 1:00 inserto de una película/actor ajeno a
  modo de broma, 4:00-4:30 tumbas egipcias con columnas (referencia a TR4 «The
  Last Revelation»), 5:00 pasillos dorados con Lara pequeña en plano general,
  7:00-7:30 selva y una cueva con antorchas · fuente:
  `https://www.dailymotion.com/video/x89cmfn` (512×288, medido con `ffprobe`) ·
  ✅ (mismo vídeo listado 4 veces en `datos-video.md` para consultas distintas,
  y créditos propios en pantalla al final).
- **Tendencia en TikTok** (comprobada por búsqueda, no vista en la app: TikTok
  no es accesible por `yt-dlp` para clips sueltos con minuto): los hashtags
  `#laracroft` y `#tombraider` acumulan decenas de millones de publicaciones;
  los formatos que más se repiten son *edits* con música de fondo y efecto de
  «glow up» comparando los distintos diseños de Lara Croft a través de los
  juegos, y clips de errores/caídas de físicas (*ragdoll*) de los juegos más
  recientes · fuente: `https://www.tiktok.com/en/trending/detail/tomb-raider-lara-croft-goes-viral`,
  `https://www.tiktok.com/tag/tombraider`, `https://www.tiktok.com/tag/laracroft`
  · ⚠️ (descripción de tendencia general, no un clip con minuto propio: TikTok
  no ofrece un vídeo único y estable para citar con `&t=`).
- **Tráiler adicional documentado pero no descargado** (por ahorrar tiempo,
  ⚠️ sólo con ficha, no mirado fotograma a fotograma): «Tomb Raider: Legend —
  Xbox 360 Trailer Video», `https://archive.org/details/tomb_raider_legend_xbox360`
  (Eidos, canal oficial de la época) · fuente: `datos-video.md` (Internet
  Archive).

### Punto 14 — Poses de Lara Croft analizadas (con nivel/tráiler y minuto)

10 fotogramas, todos mirados y con fuente propia (nada de memoria):

1. **De pie, apuntando con las dos pistolas hacia una abertura oscura**,
   torso echado atrás contra la pared, mirada al frente · TR1, nivel «Caves»,
   1:12 · `…part01_512kb.mp4`.
2. **Clavado/inmersión**: cuerpo semi-agachado, brazos abiertos, a punto de
   saltar al agua entre lianas colgantes · TR1, «Caves», 1:54-2:00.
3. **Corriendo entre ruinas cubiertas de vegetación**, torso inclinado hacia
   delante, un brazo flexionado al pecho, mirada al frente · TR1, «Lost
   Valley», 1:12 · `…part03_512kb.mp4`.
4. **Caminando de espaldas por un pasillo minero oscuro**, hombros algo
   caídos, ritmo cansado, una sola luz frontal — sirve para **pensar/tensión
   antes del clímax** · TR1, «The Great Pyramid», 5:00 · `…part15_512kb.mp4`.
5. **Mano extendida hacia arriba bajo el agua**, dedos abiertos, pidiendo
   ayuda/alcanzando la luz · tráiler «Turning Point» (TR2013), 1:12-1:28.
6. **Cayendo y agarrándose a la roca dentro de una cueva**, brazos hacia
   arriba, boca abierta (grito) — pose de pánico/supervivencia · tráiler
   «Turning Point», 1:36-1:44.
7. **Primer plano gritando, cara ensangrentada**, cejas contraídas, boca
   abierta — referencia de expresión de dolor/rabia · tráiler «Turning
   Point», 2:24.
8. **Agachada, sosteniendo un arco improvisado con ambas manos**, cuerpo
   encogido y alerta, mirada fija al frente — pose de alerta antes de pelear ·
   tráiler «Turning Point», 2:32.
9. **De pie junto a Jonah y el Dr. Dominguez frente a un mural iluminado con
   antorchas, señalando/mirando la pared** — sirve para **explicar/mostrar un
   hallazgo al grupo** · tráiler de lanzamiento de Shadow of the Tomb Raider,
   0:42.
10. **Primer plano mirando hacia abajo, gesto serio y quieto** — sirve para
    **pensar** · tráiler de lanzamiento de Shadow of the Tomb Raider, 1:48.

⚠️ **No encontré, en el metraje revisado, poses claras de «presentar»,
«celebrar», «regañar» ni «animar»**: los tráilers y el longplay muestran sobre
todo exploración, combate y huida (es el tono de la franquicia: aventura y
supervivencia, no comedia de grupo). Búsquedas hechas antes de darlo por
pendiente: repasé los 24-56 fotogramas de cada tráiler/nivel descargado sin
encontrar un saludo, una celebración de victoria o un regaño a otro personaje.
Es probable que sí existan en cinemáticas internas del juego (no en tráilers
ni en el longplay de acción de un speedrunner, que evita las escenas de
diálogo) — para cubrir esas cuatro haría falta grabación propia del juego o
clips de «cutscenes» concretos, que no estaban en `datos-video.md` ni los
encontré sueltos en Dailymotion/Internet Archive con esos nombres.

## Lo mejor para la lámina

- El tráiler «Turning Point» (TR2013) resume solo, en 3 minutos, el arco de
  huida-supervivencia-determinación de Lara: sirve para un concepto de lámina
  centrado en su cara ensangrentada y decidida (2:24-2:32).
- Paleta de Yamatai al atardecer (`#F5DDA4`/`#D3B07E`/`#101208`) para un canal
  con tono cálido; paleta de Paititi a contraluz (`#201A0C`/`#9DD34E`) para uno
  con tono de misterio/selva.
- La pose 9 (explicando un mural a su grupo) es la más «social» encontrada:
  útil si el canal necesita a Lara señalando o explicando algo a la cámara.
- El dato del instrumento a medida de Jason Graves (madera+vidrio+metal, arco
  modelado sobre el de Lara) es un detalle de *making of* muy visual para un
  texto corto del canal de música/producción.
- La cita de Nathan McCree sobre el reboot es un buen gancho de «datos
  curiosos» si el servidor tiene un canal de trivia.

## No encontré

- ⚠️ Nombres oficiales de los efectos de sonido icónicos (recogida de objeto,
  cristal de guardado): busqué `sounds.spriters-resource.com` (sólo lámina de
  ondas, sin texto) y el hilo de Tomb Raider Forums
  (`showthread.php?t=185866`), que devolvió el reto de Cloudflare las dos veces
  (no reintenté una tercera, según la regla de no insistir). Es un extra, no
  bloquea los puntos obligatorios.
- ⚠️ Tráiler de «Tomb Raider: Legend» (Xbox 360, Internet Archive) documentado
  pero no descargado/mirado fotograma a fotograma, por ahorrar tiempo: ya había
  2 tráilers completos mirados y transcritos.
- ⚠️ El T-Rex de «Lost Valley» no apareció en los fotogramas muestreados cada
  8 segundos (56 fotogramas cubren los 7:26 del nivel); la pantalla de
  resultados confirma 5 bajas en el nivel, coherente con que sí aparece en la
  partida, pero no until en un fotograma propio.
- ⚠️ Poses de «presentar», «celebrar», «regañar» y «animar» (ver punto 14):
  no aparecieron en el metraje de acción/tráiler revisado; harían falta
  cinemáticas de diálogo concretas que no localicé en las fuentes permitidas.
- ⚠️ Vídeo de un TikTok concreto con minuto propio: la red social no deja
  citar un clip con `&t=`; sólo pude documentar la tendencia general (enlaces
  arriba).
- 1080p+ real en los fotogramas (ver aviso en el punto 2): la única fuente en
  esa calidad es YouTube, bloqueado en este servidor.

## Bitácora de búsqueda

- Español: ninguna búsqueda específica (el material de vídeo de Tomb Raider es
  mayormente en inglés/japonés de origen; no hay doblaje ni fandom hispano de
  vídeo relevante a mis puntos, eso es del rol de voz).
- Inglés — web (`WebSearch`, 4 usadas de ~50): `Nathan McCree Tomb Raider
  soundtrack interview music only in caves theme title`; `Tomb Raider TikTok
  trend viral 2023 2024 Lara Croft`; `"Tomb Raider" medipack pickup sound
  iconic ding sound effect`; `"Tomb Raider" "Turning Point" official trailer
  youtube square enix site:youtube.com`.
- Fandom (`tombraider.fandom.com/api.php`, `action=query&list=search` y
  `action=parse&prop=wikitext`): `soundtrack`, `sound effects`, `quotes`,
  `opening cinematic`, `Turning Point trailer`, `Tomb Raider 1996 Music`,
  páginas leídas: «Tomb Raider (2013 Game)/Music», «Tomb Raider (2013
  Game)/Videos», «Rise of the Tomb Raider/Music», «Shadow of the Tomb
  Raider/Music», «Tomb Raider (1996 Game)/Music», «Nathan McCree», «Shadow of
  the Tomb Raider/Videos» (sólo listado). Primero comprobé `laracroft.fandom.com`
  (404, no existe) antes de confirmar `tombraider.fandom.com` con
  `action=query&meta=siteinfo`.
- Internet Archive: `https://archive.org/metadata/TombRaider_23930` y
  `.../tomb_raider_legend_xbox360` (metadatos, sin gastar búsqueda web) para
  encontrar los archivos `.mp4` reales y sus duraciones por nivel.
- Dailymotion: reutilicé los enlaces de `datos-video.md`, sin repetir la
  consulta a su API.
- YouTube: 1 intento con `yt-dlp -F` sobre `RN7_8Yholm4` (tráiler oficial
  «Turning Point» en NA) → bloqueado por «Sign in to confirm your age»,
  coherente con el aviso del encargo; no reintenté.
- Cloudflare: `tombraiderforums.com/showthread.php?t=185866` devolvió el reto
  «Just a moment...» dos veces; no hay tercera fuente equivalente localizada
  para ese dato en concreto.
- Herramientas propias usadas: `fotogramas.py` (7 veces: menú/Caves, Lost
  Valley, Great Pyramid ×2, Turning Point, SOTTR Launch, Dailymotion Globtopus)
  y `estilo.py` (2 veces, 4 imágenes) para paleta y luz medidas.

Parte terminada: los 5 puntos (2, 4, 9, 10, 14) tienen lo obligatorio del
encargo con fuente, minuto y ✅/⚠️. Lo que falta son extras, ya listados en
«No encontré» (SFX con nombre oficial, tráiler de Legend sin mirar fotograma a
fotograma, TikTok con minuto propio, 4 de las 6 poses sociales del punto 14).
