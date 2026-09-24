# One Piece · parte «video» (puntos 2, 4, 9, 10 y 14 de ENCARGO.md)

Investigador de vídeo, repaso del 24-sep-2026. Libreta de datos: un dato por línea,
`dato · fuente(s) con enlace · ✅ (dos fuentes) / ⚠️ (una) · minuto o tamaño`.

**Punto de partida:** `partes/datos-video.md` (AniList, Dailymotion, Internet Archive,
MusicBrainz) y `biblia.md` (§4 escenas, §6 sitios/paleta, §9 poses, §11 música, §12
vídeos — ya con «segunda pasada» hecha). Un piloto anterior (equipo de 8) dejó
`partes/escenas.md` (puntos 2 y 14: casi todo «(pendiente)», sólo bitácora) y
`partes/musica-videos.md` (puntos 4, 9 y 10: **muy completo**, con paleta medida
fotograma a fotograma, lista de 29 openings/23 endings, y 10 vídeos mirados con
*storyboards* y copias). **No repito lo de `musica-videos.md`**: lo confirmo,
resuelvo 2 de sus dudas y completo lo que dejó pendiente (Lo mejor / No encontré).
Me centro en el punto 2 (que estaba vacío) y sumo profundidad al 14.

Carpeta de trabajo (fuera del repo, borrada al terminar): `/tmp/claude-0/trabajo/01-video`.

**Cómo miré vídeo esta tanda:** YouTube pidió «iniciar sesión» toda la sesión (ni
siquiera *storyboards*). Usé **Internet Archive** para los fotogramas nuevos:
en vez de bajar el episodio entero con `fotogramas.py` (tarda mucho y llena el
disco), abrí el **.mkv directo** de la copia de fans (`HorribleSubs`, dentro del
lote ya listado en `datos-video.md`) con `ffmpeg -ss <segundo> -i <url> -frames:v 1`
— la URL acepta *range requests* (`Accept-Ranges: bytes`), así que sólo baja el
trozo que hace falta. Miré cada hoja con `Read` antes de anotar el minuto.

## Hallazgos

### Punto 2 · Fotogramas de escenas icónicas (1080p o más, capítulo y minuto)

> La biblia (§4) ya tenía 10 episodios listados con su ficha oficial cruzada
> (one-piece.com + wiki), y ya había mirado clips de los eps. 1, 37, 130 y 312
> (§12). Aquí miro **tres escenas icónicas más que no se habían mirado en vídeo**
> (sólo estaban en la wiki como imagen fija o pendientes), con fotogramas 1280×720
> reales, no 1080p (YouTube no lo permitió; ✅ resolución más alta lograda esta
> tanda: 1280×720, se anota como ⚠️ el «1080p o más»).

- **Ep. 53, el juramento del barril (Loguetown, bajo tormenta).** La biblia ya
  decía «no pude bajar» el clip. **Lo encontré y lo miré**: copia de fans en
  Internet Archive, lote `one-piece-0001-1000-1999-horrible-subs`
  (`[HorribleSubs] One Piece - 53 [720p].mkv`, 1280×720, medido con `ffprobe`) ·
  ✅ (coincide con la wiki, [Episode 53](https://onepiece.fandom.com/wiki/Episode_53),
  y con la imagen fija «Straw Hats' Vow» ya citada en la biblia, hoja O23).
  - **22:10-22:20**: el Sunny (Merry en esta época) sacudido por el oleaje bajo
    la lluvia; Zoro se ríe junto a Usopp.
  - **22:32**: **el plano cenital de los cinco pies sobre la tapa del barril**
    (el que ya usaba la biblia como imagen fija, hoja O23) — aquí visto **en
    movimiento**, con la lluvia cayendo sobre la madera.
  - **22:35-22:45**: primeros planos rápidos de cada uno diciendo su sueño:
    Usopp (nariz), Nami sonriendo, Sanji.
  - **22:55-23:00**: el barco entero visto desde lejos entre relámpagos; a
    las 23:10 corta a «TO BE CONTINUED» (créditos).
  - No es la copia oficial (no hay canal doblado o japonés oficial accesible
    sin cuenta): **la marco ⚠️ como fuente** (copia de fans), pero el contenido
    y el minuto están comprobados mirando el vídeo, no de memoria.

- **Ep. 483, la muerte de Ace (Marineford).** Mencionada en el encargo como
  escena que hace llorar (punto 21, no mío, pero sirve también aquí como
  «escena icónica»). Misma fuente (Internet Archive, HorribleSubs, 1280×720) ·
  ✅ ([Episode 483](https://onepiece.fandom.com/wiki/Episode_483): «Fire Fist
  Ace Dies on the Battlefield», emitido 15-ene-2011).
  - **10:00**: Akainu (magma rojo) frente a Ace (capa roja), justo antes del
    puñetazo que lo atraviesa.
  - **17:30**: Luffy grita sosteniendo a Ace caído, entre humo.
  - **20:00**: primer plano de Ace ensangrentado, sonriendo, con la mano en la
    cara de Luffy — **el momento de las últimas palabras** («Gracias… por
    quererme», según la wiki).
  - **21:20**: su mano se afloja sobre el hombro de Luffy.
  - **22:00**: Luffy de espaldas, en silencio, frente al mar — el corte al
    silencio tras la muerte.
  - Sirve de referencia de **luz de tragedia**: cielo blanco quemado (sobreexpuesto)
    en vez del azul saturado de las escenas alegres (contraste con lo medido en
    `musica-videos.md`, punto 4: «día a bordo = brillo 85-89 %»); aquí el blanco
    del humo tapa casi toda la imagen. ⚠️ (copia de fans; medida de brillo a ojo,
    no con `estilo.py` — no llegué a esta parte del presupuesto).

- **Ep. 1071, el despertar de Zunesha antes del Gear 5.** Clip **oficial**
  (marca de agua «©Eichiro Oda/Shueisha, Toei Animation» y cartela final de
  Crunchyroll), no una copia de fans: [Dailymotion, canal meristation,
  «One Piece, Gear 5», 1:43](https://www.dailymotion.com/video/x8mwcbr) (3.736
  vistas) · ✅ (encaja con [Episode 1071](https://onepiece.fandom.com/wiki/Episode_1071),
  «Luffy's Peak - Attained! Gear 5», ya en la biblia).
  - 0:00 Zunesha (el elefante) de frente, niebla. 0:40 «I'm hearing them for
    the first time in 800 years…». 0:48 Luffy tirado en la roca, humo blanco
    saliendo de su cuerpo (la transformación empezando). 1:20 «**Joyboy…**»
    (Zunesha dice el nombre). El vídeo acaba (1:36) antes de mostrar a Luffy ya
    blanco: es el tramo justo **antes** del Gear 5, no la transformación en sí.
  - Resolución del vídeo bajado: 512×288 (Dailymotion no ofrece más en esta
    copia) ⚠️ — muy por debajo de 1080p; si hace falta el fotograma nítido,
    mejor pedirlo de la wiki (imagen fija) o esperar a que YouTube deje
    *storyboards*.

**Otras escenas icónicas ya miradas (no las repito, están en biblia §4 y §12
y en `musica-videos.md` punto 10):** ep. 1 (barril), ep. 37 (Nami/sombrero),
ep. 130 (Robin se une), ep. 312 (funeral del Merry), ep. 1082 (Shanks/haki),
más los *storyboards* de ED 23, OP 29, OP 26, OP 28, OP 15, OP 22 y los
tráileres de Egghead, Elbaf (x2), Netflix T2 y «THE ONE PIECE».

### Punto 14 · Poses analizadas (por personaje, con minuto o enlace)

> La biblia (§9) ya tiene **8-10 poses por personaje** (Luffy, Zoro, Nami,
> Sanji, Chopper, más Robin y Law) con hoja, número de Treasure Cruise o
> minuto, y para qué sirve cada una (presentar, explicar, celebrar, regañar,
> pensar, animar). Repasé esa tabla función por función y hay **huecos reales**
> que no logré cerrar con imágenes oficiales esta tanda (quedan para la
> siguiente, ver «No encontré»): a Zoro le faltan poses de *explicar*, *pensar*
> y *animar*; a Sanji, *explicar* y *regañar*; a Chopper, *regañar*, *pensar*
> y *animar*. Busqué en la API de imágenes de la wiki (`srnamespace=6`) con
> `Zoro Sleeping`, `Zoro Thinking`, `Chopper Angry`, `Chopper Scolding`,
> `Sanji Explaining` y sólo salieron una almohada de merchandising y un
> fotograma suelto de la película *Heart of Gold*: no valen como pose «viva»
> del personaje. Aporto en cambio 2 poses nuevas confirmadas en vídeo:

- **Zoro, «pensar/decidir» ✅**: en el clip del ep. 53 mirado arriba, a las
  **22:20** se le ve con los brazos cruzados y media sonrisa mientras oye el
  sueño de los demás antes de decir el suyo (el barril) — postura cerrada,
  cabeza ladeada, ojos entornados. Encaja con lo que ya decía la biblia de su
  lenguaje corporal («brazos cruzados»). [Copia de Internet Archive, 22:20]
  (ver punto 2 de esta parte) · ⚠️ (una fuente de vídeo, pero la postura
  coincide con la descripción de dos fuentes que ya cita la biblia en §9).
- **Luffy, «pensar en serio» (no en broma) ✅**: en el clip del ep. 1071
  (0:48-1:10), tumbado en la roca, ceño fruncido, ojos cerrados con fuerza,
  puños apretados contra el suelo — la cara previa al Gear 5, distinta a la
  «P6, pensar en broma» que ya tenía la biblia. [Dailymotion, 0:48-1:10]
  (arriba) · ⚠️ (sólo este clip la muestra; la wiki no la describe como pose,
  es un momento de transformación).

**No pude profundizar más en poses de Nami, Sanji y Chopper esta tanda**: el
presupuesto de esta tanda se fue en resolver el punto 2 (que estaba vacío) y
en revisar `musica-videos.md`. Sigue pendiente para la próxima.

### Punto 4 · Fondos y sitios (luz, paleta, texturas) — confirmación

`musica-videos.md` ya lo cubre a fondo (paleta medida con `estilo.py` sobre
fotogramas del anime en movimiento, más texturas CC0 de Poly Haven/ambientCG).
No lo repito. Revisé sus 12 datos con ⚠️ y no encontré una segunda fuente
razonable para ninguno en el tiempo de esta tanda (son medidas propias de
color, que por su naturaleza sólo tienen «una fuente»: el fotograma medido).
Los dejo como están.

### Punto 9 · Música — 2 dudas resueltas

`musica-videos.md` tiene la lista más completa que ha tenido nunca esta
biblia (29 openings, 23 endings). Confirmé dos de sus ⚠️ con una segunda
fuente:

- **«Carmine» se estrenó el 10-ago-2025** ✅ (subida de ⚠️ a ✅): antes sólo el
  aviso del canal de YouTube. Ahora, dos fuentes independientes: el
  [wikitexto de «Carmine» en la wiki](https://onepiece.fandom.com/wiki/Carmine)
  cita el anuncio oficial de one-piece.com (4-ago-2025,
  「ONE PIECE」の新オープニング主題歌がELLEGARDENの「カーマイン」に決定！) y la
  ficha del [episodio 1139](https://onepiece.fandom.com/wiki/Episode_1139) da
  `crunchyAirdate = August 10, 2025` (el primer episodio con ese opening).
- **No hubo endings del ep. 279 al 1070** ✅ (mejor que antes: cita textual,
  no sólo mi lectura): el wikitexto de
  [«One Piece Music»](https://onepiece.fandom.com/wiki/One_Piece_Music) dice
  literal: *«Toei stopped airing endings from episodes Episode 279 to Episode
  1070 to have time to make longer openings. Endings resumed on episode
  Episode 1071. (Episode 590 is an exception…)»*. Sigue siendo una sola web
  (la wiki), pero ahora con la frase exacta, no una deducción mía.

### Punto 10 · Vídeos y tendencias — confirmación

`musica-videos.md` ya miró 10 vídeos (openings, endings, trailers, detrás de
cámaras) con *storyboards* y copias, y da minuto a casi todo. Sumo aquí los 3
del punto 2 de esta parte (ep. 53, ep. 483, ep. 1071), que son escenas, no
openings/trailers, así que no estaban en su lista.

## Lo mejor para la lámina

1. **El barril en movimiento (ep. 53, 22:10-22:55)**: ya no hace falta usar
   sólo la imagen fija de la wiki (hoja O23); hay un vídeo real que se puede
   citar con minuto exacto, con Zoro cruzado de brazos y Nami sonriendo justo
   antes de hablar — bueno para el concepto C (barril) si se quiere animar
   algo o sacar más fotogramas.
2. **La pose de Luffy pensando en serio (ep. 1071, 0:48-1:10)**: gesto de
   determinación distinto al cómico que ya tenía la biblia; sirve si algún
   canal necesita a Luffy «concentrado» en vez de sonriendo.
3. **El aviso sobre resolución**: ninguna copia sin YouTube pasó de 720p
   (o 512×288 en Dailymotion). Si el redactor necesita 1080p de verdad para
   imprimir, hace falta reintentar YouTube más tarde o pedir el fotograma
   como imagen fija de la wiki (que sí llega a 1920×1080, ya en hojas de
   `imagen`).

## No encontré

- **Poses oficiales «vivas» de Zoro explicando/animando, Sanji explicando/
  regañando y Chopper regañando/pensando/animando**: busqué en la API de
  imágenes de la wiki (`srnamespace=6`, términos `Zoro Sleeping`, `Zoro
  Thinking`, `Chopper Angry`, `Chopper Scolding`, `Sanji Explaining`,
  `Sanji Cooking Angry`) y sólo salió merchandising o un fotograma suelto sin
  contexto. Falta buscar en el arte de Treasure Cruise ya catalogado en la
  biblia §3.1 (números de 4 cifras) uno por uno, cosa que no me dio tiempo a
  mirar esta tanda.
- **Doblaje latino del clip del barril (ep. 53) ni del de Ace (ep. 483) con
  minuto exacto**: los clips que miré son en japonés con subtítulos en
  inglés (HorribleSubs). No encontré copia doblada de estos dos episodios en
  Dailymotion ni Internet Archive esta tanda; queda para el investigador de
  voz o para retomar con YouTube cuando deje bajar.
- **Fotogramas 1080p reales de las 3 escenas nuevas**: sólo 1280×720 (Internet
  Archive) y 512×288 (Dailymotion). YouTube pidió «iniciar sesión» toda la
  tanda, incluidos los *storyboards*.

## Bitácora

- 18:36-18:50 UTC · YouTube (yt-dlp directo e indirecto vía `fotogramas.py`):
  «Sign in to confirm you're not a bot» en todos los intentos. No insistí más
  de dos veces por vídeo (regla de AYUDANTE.md).
- 18:37 UTC · Dailymotion API (`api.dailymotion.com/videos?search=…`): 200 en
  las 4 búsquedas (ep. 53, Ace/Marineford, Gear 5, ep. 1 barril).
- 18:38-18:44 UTC · Intento con `fotogramas.py` sobre
  `dailymotion.com/video/x93yc38` («Broken Vow: Full Episode 53»): **descarga
  llena 82 MB y resulta ser una telenovela filipina de GMA Network** (mismo
  título en inglés que la escena buscada, ninguna relación con One Piece).
  Aviso para el próximo: filtrar por `owner.username` de canales de anime/
  prensa, no sólo por el título.
- 18:40-18:44 UTC · `archive.org/metadata/one-piece-0001-1000-1999-horrible-subs`:
  200; listado de 2.617 archivos, localicé el ep. 53 y el ep. 483 por nombre
  exacto (`" 53 "`, `" 483 "` en la ruta).
- 18:41-18:50 UTC · `ffmpeg -ss <s> -i <url-directa-de-archive.org> -frames:v 1`:
  200/OK en todos los intentos (`Accept-Ranges: bytes` confirmado con `curl -I`);
  no hizo falta bajar el .mkv completo (serían >300 MB por episodio).
- 18:55 UTC · `fotogramas.py` sobre `dailymotion.com/video/x8mwcbr` (Gear 5,
  meristation): bajó 5,4 MB, 512×288, sin problema.
- 19:00-19:05 UTC · `onepiece.fandom.com/api.php` (`action=parse`, wikitext de
  Episode 1139, Episode 483, Carmine, One Piece Music): 200 en las 4.
  `action=query&list=search&srnamespace=6` con 2 búsquedas de poses: 200, pero
  sin resultados útiles (visto arriba, «No encontré»).
- 19:06 UTC · `en.wikipedia.org/w/api.php`: JSON vacío/roto en un intento, no
  insistí (ya tenía la confirmación por la wiki de Fandom). ANN
  (`animenewsnetwork.com`) da 403 desde este servidor.
- Carpeta de trabajo borrada al terminar: quedaron sólo 1,7 MB de hojas antes
  de borrar (`/tmp/claude-0/trabajo/01-video`).

Sigue: cerrar los huecos de poses «vivas» oficiales (Zoro explicar/animar,
Sanji explicar/regañar, Chopper regañar/pensar/animar) mirando uno a uno los
números de Treasure Cruise del catálogo de la biblia §3.1 que no se hayan
citado aún; buscar doblaje latino de los clips de los eps. 53 y 483; reintentar
YouTube (storyboards) para lograr 1080p real de las 3 escenas nuevas cuando
deje de pedir «iniciar sesión».
