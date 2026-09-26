# Parte de VIDEO · Saint Seiya (Los Caballeros del Zodiaco)

Puntos de ENCARGO.md: 2 (fotogramas de escenas icónicas), 4 (fondos y sitios,
paleta medida), 9 (música y sonido), 10 (vídeos: tráiler, escenas, análisis,
tendencias) y 14 (poses analizadas por personaje). Parte de
`partes/datos-video.md` (AniList, Dailymotion, Internet Archive, MusicBrainz)
— esas consultas no se repiten aquí.

YouTube pidió iniciar sesión desde este servidor (bloqueo compartido):
todo lo de abajo se miró en **Dailymotion**, **Internet Archive** (con
`fotogramas.py` y `episodio.py`) e imágenes de **Doblaje Wiki/Fandom**, tal
como permite AYUDANTE.md. Los vídeos se borraron tras sacar las hojas (disco
compartido); quedan las hojas en `/tmp/claude-0/trabajo/39-saint-seiya-video/`.

## Hallazgos

### Punto 2 — Fotogramas de escenas icónicas (capítulo y minuto)

- Serie clásica (1986, Toei): sólo se consiguió resolución baja en clips de
  fans (Dailymotion, 480×360–512×384): no llega a 1080p. ⚠️ (ver «No
  encontré»).
- **Saint Seiya: Knights of the Zodiac (Netflix, 2019, CG)**, episodios 1 y 6,
  bajados de Internet Archive en **1920×1080 confirmado** (metadato del
  archivo: `width:1920, height:1080`, https://archive.org/metadata/knights-of-the-zodiac-saint-seiya-episode-12)
  · ✅ (metadato + calidad visual de las hojas) · procesados con
  `episodio.py` → hojas y ficha en `partes/episodios.md`.
- Ep.1, min 0:53–1:02: Seiya niño en las ruinas de un templo griego, luz
  dorada de fondo (despertar del Cosmo) · fuente: hoja 1, planos 13-19,
  https://archive.org/download/knights-of-the-zodiac-saint-seiya-episode-12/Knights%20of%20the%20Zodiac%20Saint%20Seiya%20Episode%201.mp4?t=53
  · ✅ (visto en hoja + ficha).
- Ep.6, min 2:12–2:33: pelea Ikki/Shun hermanos en cueva de lava (Isla de la
  Reina Muerte) — Ikki con la Esmeralda (recuerdo), Shun protegiéndolo · min
  2:22 «Phoenix Rising» (texto en pantalla) · fuente: hoja 2, planos 54-90,
  https://archive.org/download/knights-of-the-zodiac-saint-seiya-episode-12/Knights%20of%20the%20Zodiac%20Saint%20Seiya%20Episode%206.mp4?t=212
  · ✅.
- Escena «El Final de las Doce Casas» (fandub Dailymotion, **doblaje
  latino**, subtítulos incrustados): Seiya llega a la cámara del Patriarca,
  atrapa al vuelo el escudo dorado y lo alza; se lee en pantalla «¡Me las vas
  a pagar!» (0:18), «¿Dónde está Athena?» (1:30), «¡El Sol! ¡Se está
  ocultando!» (1:36), «¡Ya es demasiado tarde!» (3:24) · 512×384 (no 1080p)
  · fuente: https://www.dailymotion.com/video/x3iigt0 (canal
  Eltemplodeatena) · ✅ (texto en pantalla, doblaje latino confirmado con
  `voz.py`: «¡Egasos! ¡Atena!» a 0:07, calidad de audio baja).
- Escena «Muerte de Athena» (flashback de Saga bebé-Atena, 12 Casas de
  noche): pétalos de cerezo cayendo, puñal dorado, Atena bebé en brazos ·
  512×384 · https://www.dailymotion.com/video/x8x3282 (canal Tomatazos) · ✅.
- Escena «Dohko rejuvenece» (Libra se quita 200 años de encima con su Cosmo):
  de anciano a joven, cielo estrellado de fondo · 512×384 ·
  https://www.dailymotion.com/video/x8x2zig (canal Tomatazos) · ✅.

### Punto 4 — Fondos y sitios (paleta medida con `estilo.py`)

- **Las Doce Casas (interior, alfombra roja)**: negro azulado #080713 40%,
  rojo sangre #8E0D24 17%, granate #4F101F 14%, azul oscuro #0C1F37 13%, teal
  #22727E 9%, gris azulado #98ADC5 7% · medido en fotograma 0:18 de la escena
  «Final de las Doce Casas» · ✅ (medido con Pillow vía `estilo.py`).
- **Patio de las Doce Casas de noche** (escena de Saga/Atena bebé): azul
  acero #618497 26%, pizarra #2E343C 24%, verde grisáceo #4F5754 20%, casi
  negro #171B22 14%, oliva #7D834F 11% · fotograma 0:30 · ✅.
- **Volcán / lava** (opening 1986, min 0:36, paisaje tipo Isla de la Reina
  Muerte de Ikki): marrón casi negro #1E110E 37%, rojo oscuro #3F1819 22%,
  ladrillo #70201A 16%, naranja rojizo #AF381F 15%, naranja #D77926 6% · ✅.
- **Cielo estrellado nocturno** (escena de Dohko): lavanda grisáceo #898AA7
  25%, violeta pizarra #5E5D73 22%, lavanda claro #B8BCD5 19%, azul marino
  #33313E 15%, dorado #836315 13% · ✅.
- Texturas reales equivalentes: mármol de las Doce Casas → **Marble012**
  (CC0, ambientCG) https://ambientcg.com/view?id=Marble012 · ✅. Hielo/nieve
  de Siberia (entrenamiento de Hyoga) → **Snow014** (CC0, ambientCG)
  https://ambientcg.com/view?id=Snow014 · ✅ (no se vio Siberia en vídeo
  directamente; textura elegida por descripción de la wiki de Hyoga, ⚠️
  aproximada).
- Lugares confirmados por la wiki/episodios pero sin fotograma propio en
  esta tanda: Santuario (Grecia), mansión Kido (Japón), Siberia (Hyoga),
  Rozan/Lushan (Shiryu, China), Isla de la Reina Muerte (Ikki) — quedan para
  quien complete «No encontré».

### Punto 9 — Música y sonido

- **Opening clásico 1986: «ペガサス幻想» (Pegasus Fantasy)** — música: Seiji
  Yokoyama (横山菁児); letra: Machiko Ryū (竜真知子); composición: Hiroaki
  Matsuzawa (松澤浩明), Nobuo Yamada (山田信夫); arreglo y voz: **MAKE UP**
  (Columbia Records) · fuente: cartela leída en el propio opening (Dailymotion
  https://www.dailymotion.com/video/x8ckt3d, min 0:39) + confirmado en
  MusicBrainz (existen versiones/covers registradas, p. ej. ANIMETAL, 石原慎一)
  https://musicbrainz.org/ws/2/recording?query=title:ペガサス幻想 · ✅ (dos
  fuentes).
- **Opening Netflix «Knights of the Zodiac» (2019, inglés): «Pegasus Seiya»**
  — letra: Machiko Ryu (JASRAC); letra inglesa: Tim Jensen; música: Hiroaki
  Matsuzawa, Nobuo Yamada (JASRAC); interpretada por **THE STRUTS**
  (Universal Music) · fuente: cartela en el ep.1 y ep.6 (Internet Archive,
  min 1:35 de cada episodio, idéntica en ambos) · ✅ (dos apariciones
  independientes, mismo dato).
- **Ending «Soul of Gold» (2015): «約束の明日へ» (Yakusoku no Ashita e /
  Hacia el mañana prometido)** — letra: Mio Aoyama; música y arreglo:
  **√5 (ROOT FIVE)** · fuente: cartela del ending (Dailymotion
  https://www.dailymotion.com/video/x33qu48, min 1:03) + MusicBrainz (recording
  «約束の明日へ» de √5) https://musicbrainz.org/ws/2/recording?query=title:約束の明日へ
  · ✅ (dos fuentes). Paleta del ending: dorado sobre azul noche, formas de
  ave fénix/paloma doradas silueteadas, los 12 Santos Dorados al final en
  procesión — tono solemne, de despedida.
- Bandas sonoras del compositor Seiji Yokoyama (横山菁児): 15+ álbumes de
  「聖闘士星矢 音楽集」catalogados en MusicBrainz (ver `datos-video.md`) — el
  ambiente dominante es orquesta sinfónica con coros y sintetizador, muy
  dramático (compases lentos y solemnes en escenas de sacrificio, como la de
  Dohko) ✅ (visto y oído en las escenas mismas).
- **Efecto/onomatopeya reconocible**: los personajes gritan el nombre de su
  ataque o de Atena antes de golpear (rasgo distintivo del género «shonen de
  los 80»); se oyó en la escena de las Doce Casas dobladas, aunque el audio
  es de baja calidad para transcribir con exactitud (`voz.py`: «¡Egasos!
  ¡Atena!», min 0:07) ⚠️ (transcripción aproximada, Whisper con audio ruidoso).
  El otro sonido-firma es el «crujido» de energía + grito prolongado cuando
  el personaje enciende su Cosmo (aura + grietas en el suelo), visto en
  fotogramas del opening (0:15, 0:33) y de la escena de Dohko (0:24-0:48)
  · ✅ (visual, confirmado en dos escenas distintas).
- Tema en la escena más emotiva mirada (Dohko rejuvenece): cuerdas lentas en
  crescendo mientras el anciano se transforma; no se pudo identificar el
  título exacto de esa pista (no hay cartela de música en mitad de episodio)
  ⚠️.

### Punto 10 — Vídeos (tráiler, escenas, análisis, tendencias)

- **Tráiler oficial doblado** de la película live-action *Saint Seiya: Los
  Caballeros del Zodiaco – El Inicio* (Sony Pictures, 2023): tono frío,
  playa/casa junto al mar, luz de amanecer grisácea; arriba «MUY PRONTO» y
  hashtags oficiales #SonyPictures #LosCaballerosDelZodiaco #SaintSeiya (min
  1:40-1:44) · 512×288 · https://www.dailymotion.com/video/x8k6gzh (canal
  3DJuegos México) · ✅.
- Tráiler VO (sin doblar) de la misma película, canal Sensacine:
  https://www.dailymotion.com/video/x88pdxw (56 291 vistas) · ✅.
- **Análisis y resúmenes en YouTube** (fandom hispano, comprobado con
  WebSearch): canal **«Universo Saint Seiya»** (https://www.youtube.com/c/UniversoSaintSeiya),
  activo también en podcast (mismo nombre en Internet Archive:
  «Universo Saint Seiya 3x02», «2x29 Universo Saint Seiya», ver
  `datos-video.md`) · ✅ (dos fuentes, YouTube + Internet Archive, mismo
  nombre de programa). Vídeo resumen «La HISTORIA de SAINT SEIYA (CABALLEROS
  DEL ZODIACO) | RESUMEN | ¿CÓMO TERMINÓ?»
  https://www.youtube.com/watch?v=kAzm9FeWd6Y · ⚠️ (no se pudo abrir para
  sacar minuto exacto: YouTube pide iniciar sesión desde este servidor).
- **TikTok**: existe edición activa de fans bajo la etiqueta «Saint Seiya
  edit» / «Saint Seiya Ikki edit» (montajes con música, sin narración) — no
  se detectó una tendencia única y masiva en 2024-2025, sino producción
  constante de *edits* por personaje (comprobado con WebSearch) ⚠️ (no hay
  cifras de vistas verificables desde aquí).
- Podcasts/radio de fans en español sobre la serie, en Internet Archive:
  «Otacast #12a/#12b — Saint Seiya (CDZ)», «MexidÃ£o Cast #5 — Especial Saint
  Seiya», «Afrikitown 1x27 Zodiaqueando» (ver enlaces en `datos-video.md`) ·
  ✅ (accesibles, con miles de descargas cada uno, dato de popularidad real
  del fandom hispano en audio).

### Punto 14 — Poses analizadas por personaje (6-10 cada uno)

Formato: pose · qué hace · fuente (capítulo/minuto o enlace) · para qué sirve
en lámina.

**Seiya (Pegasus)**
1. De pie, armadura blanca/roja, puños cerrados, piernas separadas (pose de
   combate neutra) · «Pegasus Seiya Basic Pic.jpg», wiki ·
   https://static.wikia.nocookie.net/saintseiya/images/f/f3/Pegasus_Seiya_Basic_Pic.jpg
   · ✅ · sirve para **presentar**.
2. Mirando atrás con tristeza, de espaldas, en un muelle con veleros (se
   despide) · «Seiya's farewell.PNG», wiki · ✅ · sirve para **pensar**.
3. Golpeando a los secuaces de Shaina, cuerpo inclinado en el impacto ·
   «Seiya defeating Shaina's henchmen.PNG», wiki · ✅ · sirve para
   **regañar/atacar**.
4. Brazos abiertos hacia arriba, luz dorada envolviéndolo (acaba de obtener
   la Armadura de Pegaso) · «Seiya's joy of obtaining the Pegasus Cloth.PNG»,
   wiki · ✅ · sirve para **celebrar**.
5. Silueta envuelta en aura de fuego blanco, puño al frente (con la
   Armadura de Pegaso puesta) · «Seiya with the Pegasus Cloth.PNG», wiki ·
   ✅ · sirve para **animar/atacar**.
6. De pie sobre un rival caído, otros Santos de Bronce alrededor ·
   «Seiya defeated Cassios.PNG», wiki · ✅ · sirve para **explicar/mostrar**.
7. Corriendo con el brazo extendido, boca abierta gritando, fondo galáctico
   · opening 1986, min 1:00, https://www.dailymotion.com/video/x8ckt3d?t=60
   · ✅ · sirve para **animar**.
8. Primer plano sonriendo, feliz · opening 1986, min 1:09 (mismo enlace,
   `&t=69`) · ✅ · sirve para **celebrar**.
9. Primer plano con dientes apretados, mirada decidida, mano alzada ·
   escena «Final de las Doce Casas» (doblaje latino), min 1:30,
   https://www.dailymotion.com/video/x3iigt0?t=90 · ✅ · sirve para
   **pensar/decidir**.
10. De pie con el escudo dorado en alto sobre la cabeza, luz dramática
    detrás · misma escena, min 2:24-2:30, `?t=144` · ✅ · sirve para
    **presentar/celebrar**.

**Shiryu (Dragon)**
1. De pie, armadura verde completa, pose neutra de presentación · «Bronze -
   Dragon Shiryu V1.jpg», wiki ·
   https://static.wikia.nocookie.net/saintseiya/images/0/01/Bronze_-_Dragon_Shiryu_V1.jpg
   · ✅ · sirve para **presentar**.
2. Un puño alzado sobre la cabeza mientras un dragón espiritual azul se
   forma detrás (técnica Cólera del Dragón) · «Tech-Shiryu-RozansRisingDragon.jpg»,
   wiki · ✅ · sirve para **animar/atacar**.
3. Ráfaga de puños envuelta en hielo azul y rojo, forma abstracta (técnica
   Rozan 100 Dragones Ascendentes) · «Tech-Shiryu-Rozans100RisingDragons.jpg»,
   wiki · ✅ · sirve para **atacar (furia)**.
4. Viñeta de manga, brazo en movimiento con líneas de velocidad (técnica
   Excalibur/Rozan Sho Ryu Ha) · «Dragon Excalibur.jpg», wiki · ✅ · sirve
   para **explicar una técnica**.
5. Torso desnudo, brazo estirado bajo una cascada, entrenando (asociado a su
   monte Rozan) · opening ep.6 Netflix (Internet Archive), min 1:06,
   https://archive.org/download/knights-of-the-zodiac-saint-seiya-episode-12/Knights%20of%20the%20Zodiac%20Saint%20Seiya%20Episode%206.mp4?t=66
   · ⚠️ (identidad no 100% segura, encaja con su entorno de entrenamiento) ·
   sirve para **pensar/entrenar**.
6. Cayendo/flotando de espaldas en el agua, capa hecha jirones, vulnerable
   (derrotado, antes de enfrentar a Shura) · «Shura-shiryu.jpg», wiki · ✅ ·
   sirve para **pensar** (momento de derrota, no de acción).
- Nota aparte (no es pose): tatuaje de dragón rojo en la espalda/hombro,
  primer plano · «Shiryu Tattoo.png», wiki · ✅ · útil para vestuario/marcas
  corporales, no para postura.

**Hyoga (Cygnus)**
1. De pie, puños al frente, piernas muy separadas, armadura blanca/azul ·
   «Cygnus Hyoga Basic Pic.jpg», wiki ·
   https://static.wikia.nocookie.net/saintseiya/images/b/b0/Cygnus_Hyoga_Basic_Pic.jpg
   · ✅ · sirve para **presentar/atacar**.
2. De pie, ropa casual (top azul sin mangas, pantalón negro, botas naranjas),
   mano en la cintura, sonrisa de lado · «Hyoga 2.jpg», wiki · ✅ · sirve
   para **explicar/celebrar** (relajado, seguro de sí).
3. Flotando en el espacio, brazos totalmente abiertos en cruz, aura azul ·
   «Screenshot 9.png», wiki · ✅ · sirve para **celebrar**.
4. Primer plano serio con el casco/armadura inicial puesto, mirada fija ·
   «Hyoga Early Bronze Cloth in Sanctuary Arc.png», wiki · ✅ · sirve para
   **pensar/explicar**.
5. De niño, puño cerrado junto a la cara, gesto desafiante, fondo de hielo
   (Siberia) · «Hyoga Child.png», wiki · ✅ · sirve para **animar** (aunque
   es su versión infantil).
6. Volando con alas de cisne extendidas, brazos en alto, constelación de
   Cygnus detrás (versión Netflix) · «KotZ Netflix Hyoga with his Guardian
   Constellation, Cygnus.jpg», wiki · ✅ · sirve para **celebrar/presentar**.

**Shun (Andromeda)**
1. De pie con las cadenas de Andrómeda desplegadas alrededor, fondo
   galáctico · «Andromeda Shun wallpaper.jpeg», wiki · ✅ · sirve para
   **presentar**.
2. Poseído por Hades, alzando un báculo, expresión oscura (alter ego, no su
   yo normal) · «Saint Seiya Hades Arc-Hades Shun lifts a staff.png», wiki ·
   ✅ · sirve para **amenazar** (marcar bien que es su versión poseída).
3. Retrato de pie, expresión serena · «Andromeda Shun - ND.jpg», wiki · ✅ ·
   sirve para **explicar**.
4. De pie al aire libre, cielo despejado, postura relajada (película CG
   *Legend of Sanctuary*) · «Shun in Saint Seiya Legend of Sanctuary.jpg»,
   wiki · ✅ · sirve para **pensar**.
5. Postura defensiva, capa rosa/blanca ondeando, en el desierto · ep.6
   Netflix (Internet Archive), min 2:15,
   https://archive.org/download/knights-of-the-zodiac-saint-seiya-episode-12/Knights%20of%20the%20Zodiac%20Saint%20Seiya%20Episode%206.mp4?t=135
   · ✅ · sirve para **regañar/defender**.
6. Brazos completamente abiertos de par en par, cuerpo interpuesto (se
   interpone para proteger a alguien) · mismo episodio, min 4:50, `?t=290` ·
   ✅ · sirve para **proteger/animar**.

**Ikki (Phoenix)**
1. Cuerpo completo en pose dinámica, alas de fuego del Fénix detrás ·
   «Netflix KotZ Phoenix Nero full body.png», wiki · ✅ · sirve para
   **presentar**.
2. De pie, armadura roja, fondo de wallpaper oficial · «Phoenix Ikki
   wallpaper.jpeg», wiki · ✅ · sirve para **presentar**.
3. Caminando en línea recta a través de las llamas, sin inmutarse ·
   «KotZ Netflix Phoenix Ikki walk through the fire.jpg», wiki · ✅ · sirve
   para **animar** (determinación).
4. Lanzando un puñetazo directo a cámara, gesto de furia · «KotZ Netflix
   Phoenix Ikki throw a punch.jpg», wiki · ✅ · sirve para **regañar/atacar**.
5. De pie con la armadura final de bronce, brazos cruzados · «Phoenix ikki
   final bronze cloth.jpg», wiki · ✅ · sirve para **explicar**.
6. Sosteniendo un objeto pequeño y dorado en la palma (recuerdo de
   Esmeralda), torso desnudo, mirada baja · ep.6 Netflix (Internet Archive),
   min 3:53, https://archive.org/download/knights-of-the-zodiac-saint-seiya-episode-12/Knights%20of%20the%20Zodiac%20Saint%20Seiya%20Episode%206.mp4?t=233
   · ✅ · sirve para **pensar**.
7. Puño en alto envuelto en aura de fuego con forma de alas, dientes
   apretados · mismo episodio, min 4:54-4:57, `?t=294` · ✅ · sirve para
   **atacar/regañar**.

**Saori (Athena)**
1. Cuerpo completo, vestido blanco, báculo dorado en la mano ·
   «Netflix KotZ Sienna Kido or Athena full bdy.png», wiki · ✅ · sirve para
   **presentar**.
2. De pie, wallpaper oficial, expresión serena · «Saori Kido wallpaper.jpeg»,
   wiki · ✅ · sirve para **explicar**.
3. Rodeada de un aura de luz (su Cosmo de diosa se manifiesta), fondo
   galáctico · «KotZ Netflix Soari Athena's Cosmo aura.jpg», wiki · ✅ ·
   sirve para **animar/celebrar**.
4. Con la Armadura Divina puesta, alas doradas desplegadas · «Athena God
   Cloth.png», wiki · ✅ · sirve para **presentar** (versión guerrera).
5. De pie en el desierto, manto y báculo, expresión decidida · «KotZ Netflix
   Saori Kido as Athena.jpg», wiki · ✅ · sirve para **explicar**.
6. Sentada en un trono, báculo en la mano derecha, mirada firme hacia abajo
   · ep.6 Netflix (Internet Archive), min 1:21,
   https://archive.org/download/knights-of-the-zodiac-saint-seiya-episode-12/Knights%20of%20the%20Zodiac%20Saint%20Seiya%20Episode%206.mp4?t=81
   · ✅ · sirve para **presentar/explicar** (autoridad).

## Lo mejor para la lámina

- El escudo dorado en alto de Seiya (min 2:24 del clip de las Doce Casas,
  doblaje latino) con el cuadro de diálogo «¡Ya es demasiado tarde!» encima:
  acción + urgencia + doblaje real, muy de la serie.
- La paleta medida de las Doce Casas (#080713/#8E0D24/#0C1F37) es más rica
  y oscura que el genérico «templo griego blanco»: da profundidad real.
- Shun con los brazos abiertos protegiendo a alguien (min 4:50, ep.6) es una
  pose de personaje secundario muy expresiva para una lámina de «ayuda» o
  «protección» en el servidor.
- El opening 1986 «Pegasus Fantasy» (interpretado por MAKE UP) es la pieza
  de audio más reconocible de toda la franquicia: cualquier cuadro con
  partitura o disco debería nombrarlo.
- Ikki sosteniendo el recuerdo dorado de Esmeralda es la pose más «humana»
  encontrada: sirve para un canal de escritura/emociones, no sólo acción.

## No encontré

- **Fotogramas 1080p+ de la serie clásica de 1986** con capítulo y minuto
  exacto: YouTube (donde sí hay remasters HD) pide iniciar sesión desde este
  servidor; probé Dailymotion (todo ≤512×384) e Internet Archive (el único
  ítem de la serie clásica en Archive.org es «Knights Of The Zodiac Saint
  Seiya (Blu-Ray/DVDRip Quality)», que en realidad resultó ser la serie CG de
  Netflix 2019, no la de 1986 — comprobado viendo las hojas). Búsquedas
  hechas: Dailymotion API (`search=Saint Seiya opening/ending/trailer/escena`,
  ver `datos-video.md`), AnimeThemes (HTTP 522, caído ambas veces que se
  probó), archive.org (`Saint Seiya 1986 1080p`, sin resultado en vídeo
  legal). ⚠️.
- **Ending original de la serie de 1986** (título japonés exacto): se
  confirmó el ending de *Soul of Gold* (2015) con dos fuentes, pero no el de
  la serie clásica. Búsquedas hechas: saintseiya.fandom.com (`action=query&list=search&srsearch=Ending Theme 1`,
  sin página dedicada), ja.wikipedia.org (bloqueado por límite de peticiones
  compartido: «You are making too many requests to the API», dos intentos),
  Anime News Network API (bloqueada por verificación anti-bot), Jikan/MAL
  (HTTP 504, caído). ⚠️.
- **Minuto exacto de vídeos de análisis largos en YouTube** (p. ej. «La
  HISTORIA de SAINT SEIYA», canal con resumen completo): no se pudo abrir el
  vídeo desde este servidor (pide iniciar sesión). Se dejó el enlace sin
  minuto. ⚠️.
- **Cifras de vistas de un trend concreto de TikTok**: se confirmó actividad
  de *edits* de fans (WebSearch), pero no una tendencia única, viral y
  medible desde aquí. ⚠️.
- **Fondos de Siberia, Rozan (China) y la mansión Kido** con fotograma propio
  y paleta medida: no aparecieron en los clips de Dailymotion ni en los
  minutos mirados de los episodios 1 y 6. Quedan para quien mire más
  capítulos. ⚠️.
- Un tema de banda sonora identificado nota a nota en la escena de Dohko (sin
  cartela a mitad de episodio que lo nombre): no se pudo poner título exacto
  sin arriesgar un dato inventado. ⚠️.

## Bitácora de búsqueda

- Español: «Saint Seiya opening/ending/trailer/escena» (Dailymotion API, ya
  en `datos-video.md`), «Los Caballeros del Zodiaco doce casas» (Dailymotion
  API, directo), «Saint Seiya Shiryu Excalibur» (Dailymotion API, directo).
- Español (WebSearch): «Saint Seiya» OR «Caballeros del Zodiaco» video
  ensayo análisis YouTube reseña.
- Inglés (WebSearch): «Saint Seiya TikTok trend viral edit 2024 2025».
- Japonés: `ja.wikipedia.org` búsqueda «聖闘士星矢 主題歌» (rate-limited, sin
  resultado); `saintseiya.fandom.com` `action=query&list=search&srsearch=Ending Theme`.
- APIs directas (sin gastar el cupo de búsqueda): AniList GraphQL
  (`Media(id:1254)`), MusicBrainz `ws/2/recording?query=title:...` (Pegasus
  Fantasy y Yakusoku no Ashita e, dos búsquedas), archive.org `/metadata/`
  (dos veces: ítem completo y archivo suelto para confirmar 1920×1080),
  ambientCG `api/v2/full_json` (marble, ice), Anime News Network API
  (bloqueada por anti-bot), Jikan/MAL (504, caído).
- Herramientas: `fotogramas.py` ×6 (opening, ending, trailer, 3 escenas,
  todas por Dailymotion), `episodio.py` ×2 (ep.1 y ep.6, Internet Archive,
  8 min cada uno, idioma «en», modelo Whisper «small»), `voz.py` ×1 (escena
  de las Doce Casas, confirmar doblaje latino), `estilo.py` ×1 (4 fondos,
  paleta y estilo de pintado), imágenes de la wiki bajadas directo con
  `curl` + cabecera `Referer` (11 imágenes de personajes, todas miradas con
  Read antes de describirlas).
- Fuentes consultadas en total (vídeo): Dailymotion (7 clips), Internet
  Archive (2 episodios + metadatos), AniList GraphQL, MusicBrainz (2
  búsquedas), saintseiya.fandom.com (imágenes + búsqueda de texto),
  ambientCG (2 texturas), YouTube (bloqueado, sólo enlaces sin abrir),
  WebSearch (2 búsquedas), ja.wikipedia.org (bloqueado), ANN API (bloqueada),
  Jikan (caída).
