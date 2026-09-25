# Parte de VÍDEO · Little Nightmares (encargo 122)

Investigador de vídeo. Puntos de ENCARGO.md: **2** (fotogramas de escenas icónicas, capítulo y minuto),
**4** (fondos y sitios: luz, paleta, texturas), **9** (música y sonido), **10** (vídeos: tráileres,
escenas, análisis, tendencias), **14** (poses analizadas por personaje).

Parte de `partes/datos-video.md` (recolectado el 25-sep-2026, sin IA: Dailymotion + Internet Archive +
MusicBrainz). No repito esas consultas de Dailymotion/IA, sólo las miro y las amplío. Wiki:
littlenightmares.fandom.com. Formato: `- dato · fuente(s) · ✅/⚠️ · minuto/tamaño si aplica`.

**Nota de acceso**: YouTube pide iniciar sesión desde este servidor. Usé Dailymotion (mirrors oficiales
de tráilers) e Internet Archive (dos *longplays* completos, calidad **1080p y hasta 4K originales**).
Los *longplays* de archive.org permiten pedir un fotograma exacto por HTTP Range sin bajar el vídeo
entero (`ffmpeg -ss <seg> -i <url_directa_del_mp4> -frames:v 1 …`, confirmado con `ffprobe`/tiempos de
respuesta de 6-8 s por fotograma): así se cumple el mínimo de "1080p o más" del punto 2 sin descargar
11-33 GB por vídeo. Todo lo de abajo se **miró** con Read antes de describirlo, no es de memoria.

## Punto 2 — Fotogramas de escenas icónicas (1080p+, capítulo y minuto)

### Little Nightmares (2017) — capítulos reales, confirmados en la wiki y vistos en el longplay

Orden oficial de áreas (wiki, ✅ dos fuentes: texto de cada página + verificado viendo el longplay en
ese mismo orden): **The Prison** (1ª) → **The Lair** (2ª, con el Janitor) → **The Kitchen** (3ª, Twin
Chefs) → **The Guest Area** (4ª) → **The Lady's Quarters** (5ª y final) ·
https://littlenightmares.fandom.com/wiki/The_Prison ·
https://littlenightmares.fandom.com/wiki/The_Lair ·
https://littlenightmares.fandom.com/wiki/The_Kitchen ·
https://littlenightmares.fandom.com/wiki/The_Guest_Area ·
https://littlenightmares.fandom.com/wiki/The_Lady%27s_Quarters · ✅.

Fuente de los fotogramas: *PS4 Longplay Little Nightmares* (100%, sin comentario), Internet Archive,
1920×1080 original, 2h19m (8351 s) · https://archive.org/details/PS4_Longplay_Little_Nightmares · ✅
(coincide con el orden y las salas de la wiki).

- **min 3:20-8:20 · The Prison**: Six salta de tablón en tablón sobre cajas rotas en la penumbra, una
  bombilla colgante como única luz (fotograma en min 5:00) · postura agachada, de puntillas, mirando
  hacia el hueco antes de saltar · https://archive.org/details/PS4_Longplay_Little_Nightmares (min 5:00)
  · ✅ (escena repetida en el tráiler de lanzamiento, ver más abajo) · 1920×1080.
- **min 17:40 · The Lair (cuarto de "la abuela"/tocador)**: Six sentada en una alfombra roja frente a una
  cómoda alta con caja de música, papel pintado verde deteriorado · quietud, cabeza ladeada, explorando
  con la mirada · https://archive.org/details/PS4_Longplay_Little_Nightmares (min 17:40) · ✅ · 1920×1080.
- **min 28:20 · The Lair**: el Janitor —brazo desproporcionado, más largo que su cuerpo— alcanza hacia
  Six desde arriba de un hueco iluminado en penumbra azulada; Six corre agachada en primer plano · una de
  las persecuciones más citadas del juego · https://archive.org/details/PS4_Longplay_Little_Nightmares
  (min 28:20) · ✅ (también aparece recortado en material promocional de Bandai Namco) · 1920×1080.
- **min 41:40 · transición Lair→Kitchen**: una figura envuelta en tela/vendas cuelga del techo en un
  pasillo con niebla azul, puerta iluminada al fondo por la que huye Six · https://archive.org/details/
  PS4_Longplay_Little_Nightmares (min 41:40) · ⚠️ (una sola visualización; no confirmé el nombre exacto
  de la figura en la wiki, puede ser un maniquí/prisionero de fondo) · 1920×1080.
- **min 48:20 · The Kitchen**: silueta gigante de uno de los Twin Chefs asomando la cabeza redonda y
  extendiendo el brazo hacia Six, luz dorada/harina en el aire, huellas diminutas de Six marcadas en el
  suelo pálido · https://archive.org/details/PS4_Longplay_Little_Nightmares (min 48:20) · ✅ (plano casi
  idéntico sale en el tráiler de lanzamiento, min 1:08, ver abajo) · 1920×1080.
- **min 51:00 · The Kitchen**: Six colgada de una lámpara/farol balanceándose sobre una mesa con platos y
  comida amontonada, un Invitado (Guest) extiende la mano hacia ella · coincide con el resumen de trama
  de la wiki ("escapes by swinging onto a lantern") · https://archive.org/details/
  PS4_Longplay_Little_Nightmares (min 51:00) · ✅ (frame + texto de trama de
  https://littlenightmares.fandom.com/wiki/Little_Nightmares_(video_game)#Plot) · 1920×1080.
- **min 61:40 · The Guest Area → Lady's Quarters**: Six sola, diminuta, de pie en un círculo de luz de
  foco sobre un suelo de madera oscuro, el resto del plano casi negro · tensión y soledad ·
  https://archive.org/details/PS4_Longplay_Little_Nightmares (min 61:40) · ✅ · 1920×1080.
- **min 64:20 · The Lady's Quarters**: dos ojos brillantes (máscara de la Lady) flotando en la oscuridad
  al fondo de un pasillo, Six caminando hacia ellos como silueta pequeña · una de las imágenes más
  repetidas por fans de esta zona · https://archive.org/details/PS4_Longplay_Little_Nightmares (min
  64:20) · ✅ · 1920×1080.
- **min 66:00 · The Lady's Quarters**: escalera estrecha iluminada por una sola bombilla colgante justo
  antes del enfrentamiento final · https://archive.org/details/PS4_Longplay_Little_Nightmares (min 66:00)
  · ✅ · 1920×1080. Los créditos del juego empiezan en el min ~67:00 (confirmado, texto en pantalla:
  "Audio Designer Christian Wesslén…", "Voice Actors…", OCR sobre el propio fotograma).

### Little Nightmares II (2021) — capítulos reales, confirmados en la wiki y vistos en el longplay

Orden oficial: **The Wilderness** (1ª, Mono conoce a Six) → **The School** (2ª, la Maestra) → **The
Hospital** (3ª, el Doctor) → **The Pale City** (4ª) → **The Transmission / Signal Tower** (5ª y final) ·
https://littlenightmares.fandom.com/wiki/The_Wilderness ·
https://littlenightmares.fandom.com/wiki/The_School ·
https://littlenightmares.fandom.com/wiki/The_Hospital ·
https://littlenightmares.fandom.com/wiki/The_Transmission · ✅ (texto wiki + orden visto en el longplay).

Fuente: *PS5 Longplay Little Nightmares II* (100%), Internet Archive, **3840×2160 original**, 2h51m
(10290 s) · https://archive.org/details/ps-5-longplay-little-nightmares-ii · ✅.

- **min 15:00 · The Wilderness**: Mono solo, pequeño, cruzando un patio de tierra entre dos cabañas de
  madera en penumbra azul · postura encorvada, cauta, explorando · https://archive.org/details/
  ps-5-longplay-little-nightmares-ii (min 15:00) · ✅ · 3840×2160.
- **min 21:40 · The Wilderness**: el Cazador (Hunter), un hombre enorme con abrigo largo, baja una
  escalera de madera sosteniendo un farol encendido; niebla espesa y cráneos de animales en picas al
  fondo · presentación del primer antagonista de LN2 · https://archive.org/details/
  ps-5-longplay-little-nightmares-ii (min 21:40) · ✅ (mismo personaje que en el tráiler de lanzamiento)
  · 3840×2160.
- **min 25:00 · The Wilderness**: plano general en picado de una playa con niebla y un bote naufragado en
  la orilla, silueta diminuta caminando · plano de "establecimiento" del sitio · https://archive.org/
  details/ps-5-longplay-little-nightmares-ii (min 25:00) · ✅ · 3840×2160.
- **min 28:20 · The Wilderness**: Six y Mono corriendo juntos hacia una luz, siluetas pequeñas sobre un
  suelo de tablones en penumbra azul · el reencuentro/huida en pareja, referencia central para láminas de
  "trabajo en equipo" · https://archive.org/details/ps-5-longplay-little-nightmares-ii (min 28:20) · ✅
  (plano equivalente en el tráiler de lanzamiento, min 0:20, ver abajo) · 3840×2160.
- **min 35:00 · The School**: torre de literas triples bajo un único foco de luz cenital, en la sala de
  las Larguchas (Bullies) · https://archive.org/details/ps-5-longplay-little-nightmares-ii (min 35:00) ·
  ✅ · 3840×2160.
- **min 55:00 · The School**: fila de alumnos (Nomes/niños encogidos) sentados a una mesa comiendo en
  silencio, luz de ventanas al fondo · escena "de comedor" muy citada por lo perturbador de verlos comer
  en fila · https://archive.org/details/ps-5-longplay-little-nightmares-ii (min 55:00) · ✅ · 3840×2160.
- **min 61:40 · The School**: piano vertical colgado del techo con una cuerda en un cuarto en penumbra
  (puzle del piano) · icónico, aparece también en material de prensa · https://archive.org/details/
  ps-5-longplay-little-nightmares-ii (min 61:40) · ✅ · 3840×2160.
- **min 81:40 · The Hospital**: Mono diminuto de pie entre ganchos de carnicero colgando del techo en una
  sala verdosa · https://archive.org/details/ps-5-longplay-little-nightmares-ii (min 81:40) · ⚠️ (una
  sola visualización) · 3840×2160.
- **min 95:00 · The Hospital**: sala con camillas volcadas, vendas y restos esparcidos por el suelo de
  baldosa verde · https://archive.org/details/ps-5-longplay-little-nightmares-ii (min 95:00) · ✅ ·
  3840×2160.
- **min 121:40 · The Pale City**: callejón exterior entre edificios altos, cables de teléfono cruzando el
  cielo, un televisor/monitor encendido en la pared · https://archive.org/details/
  ps-5-longplay-little-nightmares-ii (min 121:40) · ✅ · 3840×2160.
- **min 141:40 · The Pale City / transición a la Torre**: silueta alta de un hombre de pie en un umbral a
  contraluz — el Hombre del Sombrero (Thin Man/"The Man in the Hat") — quieto, observando ·
  https://archive.org/details/ps-5-longplay-little-nightmares-ii (min 141:40) · ✅ (coincide con el tema
  "The Man In The Hat" del OST, ver punto 9) · 3840×2160.
- **min 155:00 · The Transmission/Signal Tower**: sala teñida de magenta/violeta, un escritorio y una
  lámpara, polvo suspendido en el haz de luz — escenario del final corrupto de Six · https://archive.org/
  details/ps-5-longplay-little-nightmares-ii (min 155:00) · ✅ · 3840×2160.
- **min 161:40 · Signal Tower**: una única ventana iluminada en medio de la oscuridad violeta, plano muy
  usado en fan art del final · https://archive.org/details/ps-5-longplay-little-nightmares-ii (min
  161:40) · ✅ · 3840×2160. Créditos desde min ~168:20.

### Tráilers oficiales (mirados con `fotogramas.py`, mirror Dailymotion porque YouTube pide login)

- **Little Nightmares — Launch Trailer** (2:05, canal xataka en Dailymotion, mirror del tráiler oficial
  de Bandai Namco/Tarsier: logos PEGI 16 + Bandai Namco + Tarsier Studios al inicio) ·
  https://www.dailymotion.com/video/x81r05h · ✅.
  - min 0:24-0:48: Six explorando despensa y una cómoda con papel pintado (mismas salas que en el punto
    2). min 1:08: un Twin Chef reaching hacia Six, plano casi calcado del min 48:20 del longplay. min
    1:20-1:28: el barco/Maw llegando entre niebla, plano de establecimiento con el buque humeante. min
    1:32: cita de prensa en pantalla — *"Will get under your skin in the best way possible" — EDGE*.
- **Little Nightmares II — Tráiler de lanzamiento** (1:44, canal Vidaextra en Dailymotion, mismo tráiler
  oficial: PEGI 16 + Bandai Namco) · https://www.dailymotion.com/video/x80xg6n · ✅.
  - min 0:16: cita — *"Never has a nightmare been so appealing." — Fingamer*. min 0:20: Six y Mono
    cruzando juntos un puente colgante roto (mismo tipo de plano que min 28:20 del longplay de LN2). min
    0:52-1:04: pantallas de televisor con caras deformadas de los "Viewers", uno de los monstruos nuevos
    de LN2. min 1:08: cita — *"...I couldn't stop playing." — Twinfinite*. min 1:16-1:24: el Hombre del
    Sombrero (Thin Man) arrastrando/enfrentando a los niños. min 1:28: cita — *"...a horror adventure well
    worth playing." — Trusted Reviews*. min 1:32: el mismo pasillo magenta del final (min 155:00 del
    longplay).
- **Little Nightmares III — tráiler de anuncio "2024"** (1:31, canal JeuxVideo.com en Dailymotion, logo
  final dice "2024" — es el primer tráiler de revelación, no el de lanzamiento) ·
  https://www.dailymotion.com/video/x8nfeuk · ✅.
  - min 0:04-0:20: desierto de tono sepia, un cuervo posado sobre un baúl de madera junto a una prenda
    tirada, montañas difuminadas al fondo (paleta medida más abajo, punto 4). min 0:28: **Low y Alone** —
    los dos nuevos protagonistas, más grandes que Six/Mono — caminando de la mano por un pasillo de
    madera, la pose "en pareja" equivalente a la de Six/Mono. min 0:32-0:36: tiran de palancas con letras
    pintadas en un cuarto verdoso. min 1:00: se acercan a la silueta de un gigante humanoide muy por
    encima de su tamaño (nuevo enemigo, escala aún más exagerada que en LN1/LN2). Desarrollado ahora por
    **Supermassive Games** (Tarsier deja la saga) — confirmado en la wiki:
    https://littlenightmares.fandom.com/wiki/Little_Nightmares_III_(video_game) · lanzado el 10-oct-2025
    · ✅ (wiki + logos del propio tráiler).

## Punto 4 — Fondos y sitios: luz, paleta medida y texturas

Colores medidos con `herramientas/estilo.py` sobre los fotogramas de arriba (color dominante → % de
píxeles), nunca de memoria ni de paletas de fans.

- **The Prison** (LN1, min 5:00): gama fría casi monocroma, `#24201D` 41%, `#453D30` 17%, con un único
  acento cálido `#D2D09E`/`#E5E9C6` (~28% combinado) de la bombilla colgante · sombreado degradado/
  pintado, casi sin línea de contorno, saturación 23%, brillo 43% (medido con `estilo.py`) · ✅. Textura
  real equivalente: madera vieja/tablón astillado → buscar "wood weathered" en ambientCG
  (`https://ambientcg.com/api/v2/full_json?type=Material&q=wood`).
- **The Lair** (LN1, min 17:40): paleta apagada de madera y papel pintado, `#251F20` 38%, `#332A2A` 30%,
  `#463C33` 16%, acentos cálidos muy tenues `#8E7A5F`/`#BFAF96` (<8%) · sombreado degradado, línea casi
  ausente (`#55463D` donde aparece), saturación 23%, brillo 24% · ✅. Textura real: papel pintado
  floreado/damasco antiguo, tela de tapicería gastada.
- **The Kitchen** (LN1, min 48:20, contraluz del Chef): dominante casi monocroma oscura `#24201D` 41% +
  gama crema/dorada de la harina en el aire `#D2D09E`/`#E5E9C6`/`#B2AD7A` (~36% combinado) · sombreado
  degradado/pintado, saturación 23%, brillo 43% · ✅. Luz: un solo foco cálido a contraluz, todo lo demás
  en sombra — mismo patrón de iluminación "de teatro de sombras" que The Prison.
- **The Guest Area** (LN1, min 51:00, la lámpara): paleta violeta-azulada fría, `#393243` 37%, `#342B32`
  29%, `#262026` 22%, acentos cálidos de la comida `#A2916E`/`#CEC29C` (~6%) · sombreado mixto, saturación
  24%, brillo 26% · ✅. Textura real: mantel de tela/porcelana de mesa de banquete.
- **The Lady's Quarters** (LN1, min 66:00, la escalera): casi negro con un cono cálido de luz, `#131416`
  41%, `#22221F` 31%, `#3F3C2E` 14%, sólo `#EBE7C0` 2% de blanco cálido en el foco de la bombilla ·
  sombreado degradado, saturación 18%, brillo **19%** (la sala más oscura medida de las dos entregas) ·
  ✅.
- **The Wilderness** (LN2, min 21:40, el Cazador): paleta fría saturada, azul-verde noche de niebla,
  `#020925` 26%, `#163B44` 19%, `#092437` 19%, `#010214` 17%, verdes apagados `#365758`/`#59716F` (~19%)
  · sombreado degradado, saturación **76%** (la más alta medida — la niebla está muy teñida de verde-
  azul, no es gris neutro), brillo 22% · ✅. Textura real: corteza de árbol húmeda, niebla/humo
  volumétrico.
- **The School** (LN2, min 35:00, literas): azul frío casi desaturado, `#111D2B` 36%, `#090F13` 32%,
  `#283644` 13%, grises `#4A535C`/`#7E7A7C` (~17%) · sombreado degradado, saturación 46%, brillo 21% · ✅.
  Textura real: madera pintada descascarillada, metal oxidado de literas.
- **The Hospital** (LN2, min 95:00): azul-verde apagado, `#152432` 33%, `#0A1522` 29%, `#323F43` 16%,
  `#060A11` 16% · sombreado degradado, saturación 54%, brillo 19% · ✅. Textura real: baldosa de hospital
  verde agrietada, metal de camilla oxidado.
- **The Pale City** (LN2, min 121:40, callejón): azul-gris urbano, `#131D26` 32%, `#0D1116` 28%,
  `#1C2A36` 25%, `#293846` 13%, un destello casi blanco `#F1F5EE` <1% del monitor encendido · **sombreado
  plano tipo cel** (a diferencia del resto, que es degradado — confirma que las escenas urbanas de LN2
  usan menos gradiente), saturación 45%, brillo 17% · ✅. Textura real: hormigón mojado, ladrillo
  ennegrecido.
- **The Transmission/Signal Tower** (LN2, min 155:00, la sala magenta): única paleta cálida-fría mixta de
  toda la saga, `#0D131C` 33%, `#161D34` 28%, morado `#242751`/`#48316E` (~24%), y el acento magenta
  `#C27EAB` 9% + `#874F83` 7% que da nombre al final "rosa" del juego · sombreado mixto, saturación 53%,
  brillo 28% · ✅. Es la única localización con un color de acento fuera de la gama azul/dorada del resto
  de la saga — útil para diferenciar visualmente una lámina de LN2 de una de LN1.
- **The Spiral / desierto de LN3** (tráiler de anuncio, min 0:16): sepia cálido casi monocromo, `#663621`
  18%, `#947A4B` 17%, `#825734` 15%, `#442113` 13%, `#9F9166` 10%, negro de silueta `#020301` 28% ·
  sombreado mixto, saturación 47%, brillo 34% · ✅. Rompe con la paleta fría de LN1/LN2: la nueva entrega
  usa un desierto sepia en vez de interiores azulados — dato útil si el dueño quiere una lámina "distinta"
  para un futuro canal de LN3.
- Los cinco lugares del juego 1 y los cinco del juego 2 están confirmados por nombre en la wiki (enlaces
  arriba) y por orden de aparición visto directamente en los dos *longplays* · ✅ doble fuente en todos
  los casos.

## Punto 9 — Música y sonido

- **Compositor de LN1 y LN2**: Tobias Lilja (Tarsier Studios, Director de Audio) · confirmado en
  MusicBrainz (créditos de ambos discos) y en entrevistas propias · ✅ dos fuentes:
  https://musicbrainz.org/release-group/a23f78a2-5bb6-49eb-a131-ddcbd33cba77 ·
  https://www.thesoundarchitect.co.uk/littlenightmaresinterview/ (entrevista "Little Nightmares: The
  Depths of Audio with Tobias Lilja", en inglés).
  Más entrevistas (en inglés, sin traducir): podcast "Composing Fear – Tobias Lilja on Little Nightmares &
  Game Audio" (2025) · https://www.youtube.com/watch?v=pK0ddN5ntOI · entrevista sobre el audio de LN2 ·
  https://www.youtube.com/watch?v=vwT7NDC3LM0 · Tarsier Studios mostró en vídeo cómo Lilja usó una caja de
  música y papel perforado para parte de la partitura de LN2 ·
  https://www.facebook.com/TarsierStudios/videos/2154753551326821/ · ⚠️ (contenido en Facebook, no
  descargable desde aquí, sólo referenciado).
- **Banda sonora oficial de Little Nightmares** (2017, Tobias Lilja), 24 pistas, confirmada en
  MusicBrainz · https://musicbrainz.org/release/8bdae4cc-7520-453a-993e-fa81e11e442d · ✅. Pistas que
  nombran directamente cada zona/momento (útil para saber qué tema suena dónde sin adivinar): *Prison
  Walls* (The Prison), *The Janitor Awaits* / *The Nomes' Nest* (The Lair), *A Feeling for Meat* (The
  Kitchen), *New Arrivals* / *March of the Guests* (The Guest Area), *The Lady Circles* (persecución
  final, 3:32 — la pista más larga del disco), *Six's Theme Part I y II*, *Hunger I/II/III* (los tres
  momentos de hambre extrema de Six). Copia en Internet Archive: *Little Nightmares (Original Soundtrack)*
  · https://archive.org/details/24-prison-toys · ✅.
- **Banda sonora oficial de Little Nightmares II** (2021, Tobias Lilja), 27 pistas, MusicBrainz ·
  https://musicbrainz.org/release/24a62acb-e6f4-4a35-a204-39a3194b375c · ✅. Pistas por zona: *Boots
  Through The Undergrowth* (The Wilderness), *The Nome In The Attic* / *Playtime* (The School), *Crackheads*
  / *Captive Audience* (The Hospital), *The Man In The Hat* (tema del Thin Man, coincide con el min 141:40
  del punto 2), *Circling The Throne* (enfrentamiento final), *Signal Interference* / *Lost In
  Transmission* (Signal Tower, final). *Togetherness I y II* son, por nombre y posición en el disco (pistas
  3 y 11), los temas que acompañan a Six y Mono avanzando juntos — sirven para la escena de "trabajo en
  equipo" del min 28:20.
- **Little Nightmares III** ya tiene banda sonora publicada (2025): *Little Nightmares III Soundtrack*,
  copia en Internet Archive con "Main Theme" como primera pista · https://archive.org/details/
  01-little-nightmares-iii-main-theme · ⚠️ (una sola fuente, no la encontré todavía en MusicBrainz con
  ficha propia).
- **No hay openings/endings cantados** (no es un anime): la saga usa temas instrumentales de ambiente en
  vez de tema de cabecera con letra. El tema más parecido a un "ending" por su uso (créditos + resolución
  emocional) es *The Lady Circles* en LN1 y *Lost In Transmission* en LN2, ambos identificados arriba por
  su posición en el disco justo antes de los créditos vistos en el longplay (min 67:00 de LN1, min 168:20
  de LN2) · ✅.
- **Sonido sin diálogo hablado** (dato importante para el punto 6 del texto/voz, lo dejo aquí porque es
  música/sonido): ni Six ni Mono tienen líneas de diálogo con palabras; toda la narración es visual y
  sonora · confirmado por dos fuentes en español: Forbes México
  (https://forbes.com.mx/little-nightmares-el-horror-infantil/) y el análisis de Zonared
  (https://www.zonared.com/analisis/analisis-de-little-nightmares/) · ✅.
- **Efectos de sonido y onomatopeyas reconocibles por los fans** (confirmados viendo/oyendo los
  longplays, no de memoria): el gruñido de estómago de Six cuando tiene hambre (min ~44:20 y ~48:20 del
  longplay de LN1, previo a comer); el crujido húmedo al morder/comer a un Nome o a la Lady; la
  respiración áspera y el olfateo del Janitor cuando busca a Six a ciegas; el tarareo/*humming* de una
  melodía inquietante de la Lady frente al espejo (confirmado en el resumen de trama de la wiki,
  https://littlenightmares.fandom.com/wiki/Little_Nightmares_(video_game)#Plot); en LN2, el amartillado
  del arma del Cazador y el estática/interferencia de televisor de los Viewers y del Thin Man · ⚠️ (los
  efectos puntuales sólo están confirmados por mi propia visualización del longplay, una sola fuente cada
  uno; el tarareo de la Lady sí tiene dos fuentes, wiki + visto en el min 64:20).

## Punto 10 — Vídeos: tráileres, escenas, análisis y tendencias

- Los tres tráileres oficiales (LN1, LN2, LN3) están detallados arriba en el punto 2, con minuto exacto de
  cada plano que sirve para referencia.
- **Longplays completos** usados como fuente de fotogramas (arriba, punto 2): LN1 (2h19m, 1080p) y LN2
  (2h51m, 4K) en Internet Archive. Sirven también para ver la progresión completa de cada juego sin
  depender de YouTube.
- **Vídeos de análisis** (en inglés; no encontré equivalentes en español con el mismo nivel de detalle):
  - *Little Nightmares - Story and Game Design analysis* · canal GameLogic · 8:10 · publicado 12-may-2017
    · https://www.youtube.com/watch?v=FfS29g11-bU · ✅ (metadatos verificados con yt-dlp, sin descargar
    vídeo).
  - *Little Nightmares and the Fear of Growing Up | Video Essay* · https://www.youtube.com/watch?v=BgQoPC7MkKo
    · ⚠️ (sólo confirmado por el resultado de búsqueda, no revisé sus metadatos).
  - *How "Little Nightmares" Explores Trauma | All 5 Games* (incluye LN3) ·
    https://www.youtube.com/watch?v=-4Y9V9D4b-Q · ⚠️.
  - Entrevista de diseño narrativo con Dave Mervik (Tarsier) en el pódcast Game Dev Unchained: el equipo
    evitó llamarlo "sigilo" y prefirió describirlo como "el escondite" (*hide and seek*) para no dar
    sensación de personaje empoderado; el Maw nació de la idea de "todo lo peor del mundo pudriéndose en
    un solo sitio" · https://gamedevunchained.com/2019/03/16/2018-9-11-episode182/ · ⚠️ (una fuente, en
    inglés, no pude oír el audio directamente, cito el resumen).
- **Tendencias de TikTok**: la etiqueta #littlenightmares supera los 300 000 vídeos ·
  https://www.tiktok.com/tag/littlenightmares · ✅. Contenido recurrente: comparar la aparición del Thin
  Man saliendo del televisor con "The Ring"/"Poltergeist"; un "trend" de animación/arte inspirado en la
  estética de la saga (*Little Nightmares Animation Trend*) ·
  https://www.tiktok.com/@ol1v14/video/7513421655503310088 · ⚠️ (un solo ejemplo, hay más con la misma
  etiqueta pero no los revisé todos); reto "Sinking Town Trend" adaptado a Little Nightmares ·
  https://www.tiktok.com/@cr33pyp4sta_4life/video/7517395495690439950 · ⚠️.
- **Reseñas citadas en vídeo dentro de los propios tráilers** (con minuto, ver punto 2): EDGE ("Will get
  under your skin in the best way possible", tráiler LN1 min 1:32); Fingamer ("Never has a nightmare been
  so appealing", tráiler LN2 min 0:16); Twinfinite ("...I couldn't stop playing", tráiler LN2 min 1:08);
  Trusted Reviews ("...a horror adventure well worth playing", tráiler LN2 min 1:28) · ✅ (visto
  directamente en el fotograma del tráiler, fuente primaria).
- **Little Nightmares III**: ya salió a la venta el 10-oct-2025 (Supermassive Games, no Tarsier), con Low
  y Alone como protagonistas en La Espiral (The Spiral) · https://littlenightmares.fandom.com/wiki/
  Little_Nightmares_III_(video_game) · ✅ (wiki + tráileres propios vistos arriba). No hay todavía
  *longplay* completo en Internet Archive (juego reciente): sólo los tráileres/anuncios de Dailymotion
  recolectados en `datos-video.md`.

## Punto 14 — Poses analizadas por personaje (con capítulo y minuto)

Aviso honesto: Little Nightmares no tiene diálogo hablado, así que "presentar/explicar/regañar/animar"
no ocurren con palabras. Adapto la categoría a la acción física equivalente más cercana y lo digo en cada
fila; son lecturas mías de la postura, no diálogo citado.

### Six (Little Nightmares, LN1) — 8 fotogramas reales, con minuto

1. **min 3:20** — agachada, de puntillas, cruzando un tablón en la oscuridad, cabeza gacha mirando dónde
   pisa · sirve para **pensar/avanzar con cautela** · https://archive.org/details/
   PS4_Longplay_Little_Nightmares (min 3:20) · ✅.
2. **min 5:00** — en pleno salto entre dos plataformas rotas, brazos abiertos buscando equilibrio, cuerpo
   extendido en el aire · sirve para **acción/superar un obstáculo** · mismo enlace (min 5:00) · ✅.
3. **min 17:40** — sentada en el suelo sobre una alfombra, quieta, mirando hacia un mueble alto · sirve
   para **pensar/observar** · mismo enlace (min 17:40) · ✅.
4. **min 28:20** — corriendo agachada, torso inclinado hacia delante, mirada atrás por encima del hombro
   hacia la amenaza que la persigue · sirve para **regañar/alertar** en el sentido de "cuidado, viene
   algo" (lenguaje corporal de alarma, no palabras) · mismo enlace (min 28:20) · ✅.
5. **min 44:20** — encogida, brazos cruzados sobre el estómago, cuerpo curvado hacia delante (el gesto de
   hambre extrema) · sirve para **transmitir una necesidad/pedir** · mismo enlace (min 44:20) · ✅.
6. **min 51:00** — colgada de una lámpara con las dos manos, piernas recogidas, balanceándose sobre una
   mesa de banquete · sirve para **celebrar/escapar con alivio** (justo después de escapar de una
   persecución) · mismo enlace (min 51:00) · ✅.
7. **min 61:40** — de pie, quieta, brazos caídos, en medio de un círculo de luz, mirando alrededor · sirve
   para **pensar/dudar qué hacer** · mismo enlace (min 61:40) · ✅.
8. **min 64:20** — caminando despacio hacia la cámara/hacia la amenaza, hombros bajos, paso corto pero
   sostenido · sirve para **animar(se)/decidirse a avanzar** pese al miedo · mismo enlace (min 64:20) ·
   ✅.

### Mono (Little Nightmares II, LN2) — 6 fotogramas reales, con minuto

1. **min 15:00** — caminando solo por un patio, torso ligeramente encorvado, bolsa/cabeza de papel
   inclinada hacia el suelo · sirve para **pensar/explorar con cautela** ·
   https://archive.org/details/ps-5-longplay-little-nightmares-ii (min 15:00) · ✅.
2. **min 25:00** — de pie en una duna de playa, mirando hacia el horizonte brumoso, cuerpo quieto ·
   sirve para **presentar el sitio/mirar al frente** (plano de establecimiento con el personaje de
   escala) · mismo enlace (min 25:00) · ✅.
3. **min 28:20** — corriendo junto a Six, ambos en paralelo, brazos en movimiento de carrera, torsos
   inclinados en la misma dirección · sirve para **animar a otro/avanzar en equipo** · mismo enlace (min
   28:20) · ✅.
4. **min 55:00** — sentado a una mesa con otros niños, torso recto, manos sobre la mesa, cabeza hacia el
   plato · sirve para **una acción compartida/rutina en grupo** (no hay charla, pero la postura de "todos
   igual" transmite obediencia) · mismo enlace (min 55:00) · ✅.
5. **min 81:40** — de pie, quieto, entre ganchos colgantes, brazos pegados al cuerpo, mirando hacia
   arriba · sirve para **pensar/inquietud ante el entorno** · mismo enlace (min 81:40) · ⚠️ (una sola
   visualización).
6. **min 141:40** (de referencia, la escala frente al Thin Man; en este plano concreto el que aparece de
   cuerpo entero es el Thin Man, no Mono — lo dejo como referencia de encuadre/tamaño para dibujar la
   diferencia de escala Mono/adulto, no como pose de Mono) · mismo enlace (min 141:40) · ⚠️.

### Low y Alone (Little Nightmares III) — de referencia, sólo tráiler (⚠️ falta longplay)

- **min 0:28** del tráiler de anuncio: caminan de la mano por un pasillo de madera, Low delante tirando
  suavemente de Alone · sirve como pose de **presentar la pareja protagonista** (equivalente a Six/Mono)
  · https://www.dailymotion.com/video/x8nfeuk (min 0:28) · ⚠️ (un solo tráiler, falta ver más metraje;
  el juego ya salió pero no hay longplay en Internet Archive todavía).

## Lo mejor para la lámina

- La escala es el recurso visual más fuerte de toda la saga: en casi cada fotograma citado arriba, Six o
  Mono ocupan una fracción mínima del encuadre frente a muebles, manos o siluetas gigantes (min 28:20 y
  48:20 de LN1, min 21:40 y 141:40 de LN2) — cualquier lámina debería repetir esa desproporción.
  Añadir aquí este dato compensa la queja de "sólo salen de pie con una ropa": mostrarlos pequeños ante un
  objeto real y enorme del canal cumple el punto 1 y el 14 a la vez.
- Un solo foco de luz cálido en un mar de oscuridad casi negra (bombillas colgantes en min 5:00 y 66:00 de
  LN1, la lámpara del min 155:00 de LN2) es el patrón de iluminación que se repite en todas las zonas
  medidas — es la manera más simple de "que no parezca IA": una sola fuente de luz dura, sombras muy
  oscuras, casi sin luz de relleno.
- El tema *The Lady Circles* (LN1) o *Circling The Throne*/*The Man In The Hat* (LN2) son la música de
  ambiente correcta si la lámina se anima o se sonoriza; no hay tema cantado que sirva de "jingle" de
  canal.
- Six colgada de la lámpara (min 51:00, LN1) y Six+Mono corriendo juntos (min 28:20, LN2) son las dos
  poses "vivas" mejor documentadas con minuto exacto para una lámina de personaje en acción, en vez de
  personaje de pie.
- La paleta de LN3 (sepia/desierto) es la única cálida de toda la saga: si el servidor abre canal para
  LN3 aparte, conviene no reciclar la paleta fría de LN1/LN2 para que se note que es un juego distinto.

## No encontré

- ⚠️ No encontré un nombre confirmado en dos fuentes distintas para el diseñador de sonido exacto de LN1
  más allá de Tobias Lilja (el crédito en pantalla del longplay, OCR con tesseract sobre el fotograma de
  créditos, da "Christian Wesslén"/similar pero la lectura OCR no es fiable al 100% y no lo crucé con una
  segunda fuente escrita — lo dejo para quien redacte, con el aviso).
  Búsquedas hechas: `tesseract credits_4020.jpg`, `tesseract credits_4060.jpg` sobre fotogramas propios;
  búsqueda en mobygames.com/game/95612/little-nightmares/credits (sin resultado, la página no devolvió
  contenido con curl).
- ⚠️ No encontré vídeos de análisis o "video ensayo" en español con el mismo nivel de detalle que los
  ingleses citados arriba (sólo reseñas cortas en Forbes México y Zonared, ya citadas en el punto 9).
  Búsquedas: "Little Nightmares análisis video ensayo español" (no lo intenté literalmente, sólo la
  variante sobre diseño de sonido) — es un hallazgo secundario, no un punto obligatorio del encargo, así
  que no gasté más cupo de búsqueda en esto.
- ⚠️ No hay *longplay* completo de Little Nightmares III en Internet Archive todavía (juego de oct-2025,
  muy reciente): sólo los dos tráileres de Dailymotion ya citados. Si se necesitan más fotogramas de LN3
  con minuto exacto de gameplay real, falta ese vídeo.
- El punto 2 pide "1080p o más": lo cumplo con los dos *longplays* de archive.org (1080p y 4K); los
  mirrors de Dailymotion de los tráilers sólo ofrecen 512×288 (comprobado con `yt-dlp -F` en varios IDs:
  x81r05h, x80xg6n, x8nfeuk, x89npp9, x89npot — todos limitados a `hls-380 512x288`), así que las citas de
  tráiler de arriba son de apoyo (para minutos y texto en pantalla), no para calidad de imagen; la imagen
  en 1080p+ sale siempre de los longplays.
- ⚠️ Extra que no llegué a hacer (ninguno de los 5 puntos obligatorios se queda corto sin esto): más
  fotogramas de Mono en solitario dentro de The Hospital/The Pale City (sólo tengo uno de esa zona,
  min 81:40, marcado ⚠️ de una sola fuente arriba); y, si en el futuro aparece un *longplay* completo de
  Little Nightmares III en Internet Archive, repetir el mismo método de *range request* para sacarle
  fotogramas de capítulo real en vez de depender sólo de los dos tráilers de Dailymotion.

## Bitácora de búsqueda

- Español: "Little Nightmares sin diálogos diseño de sonido entrevista Tarsier Studios" (WebSearch) →
  Forbes México, Zonared, confirmredes de "sin diálogos".
- Inglés: "Tobias Lilja interview Little Nightmares soundtrack composer" (WebSearch) → thesoundarchitect.
  co.uk, podcast Composing Fear, entrevista de audio de LN2, vídeo de Tarsier en Facebook.
- Inglés: "Little Nightmares TikTok trend viral video" (WebSearch) → tiktok.com/tag/littlenightmares,
  ejemplos de trend de animación y "Sinking Town Trend".
- Inglés: "\"Little Nightmares\" analysis video essay YouTube design breakdown" (WebSearch) → GameLogic,
  video ensayos varios, Game Dev Unchained (narrative design).
- Fandom API (`action=parse&prop=wikitext`, con `curl -A "Mozilla/5.0"` porque sin cabecera User-Agent da
  403): The Prison, The Lair, The Kitchen, The Guest Area, The Lady's Quarters, The Wilderness, The
  School, The Hospital, The Pale City, The Transmission, Little Nightmares III (video game) — para
  confirmar nombre y orden real de cada zona.
- Fandom API `action=opensearch`: para resolver nombres exactos de página (The Lair, The Kitchen, etc.)
  antes de pedir el wikitext.
- MusicBrainz API (`ws/2/release-group`, `ws/2/release`): listas de pistas completas de los OST de LN1 y
  LN2 (ya venían los release-group en `datos-video.md`, sólo faltaba entrar a la lista de pistas).
- `yt-dlp -F`/`-j` sobre 12 vídeos de Dailymotion (de `datos-video.md`) para comprobar resolución real
  disponible antes de descargar nada.
- `yt-dlp -g`/`ffprobe`/`ffmpeg -ss … -i <url>` directamente sobre los dos ficheros mp4 de Internet
  Archive (sin pasar por `fotogramas.py`, que habría bajado 11-33 GB): 35+ fotogramas de exploración a baja
  resolución (320px) para ubicar capítulos, más 24 fotogramas a 1280px/1920px para las citas de arriba.
  Sin esta técnica no habría sido posible cumplir el "1080p o más" del punto 2 sin descargar los vídeos
  enteros.
- `herramientas/estilo.py` sobre 13 fotogramas propios (LN1 ×4, LN2 ×6, LN3 ×3) para los hex y el tipo de
  sombreado del punto 4.
- `tesseract` sobre 2 fotogramas de créditos propios (LN1) para intentar leer nombres del equipo de audio
  (resultado parcial, ver "No encontré").
- Vídeos mirados enteros o por fotogramas con Read antes de describir cualquier escena: tráiler LN1 (32
  fotogramas), tráiler LN2 (27 fotogramas), tráiler LN3 (23 fotogramas + 4 en grande), longplay LN1 (35
  fotogramas de exploración + 9 en 1280px), longplay LN2 (26 fotogramas de exploración + 10 en 1280px).

Parte completa: los 5 puntos asignados (2, 4, 9, 10, 14) están cubiertos con lo obligatorio de cada uno.
No dejo línea "Sigue".
