# Parte del investigador de VÍDEO · SpongeBob (Bob Esponja)

Puntos de ENCARGO.md: **2** (fotogramas de escenas icónicas, capítulo y
minuto), **4** (sitios, luz y paleta medida, texturas), **9** (música), **10**
(vídeos: tráilers, escenas, análisis, tendencias, con minuto) y **14** (poses
analizadas por personaje, con minuto real).

**YouTube dio 429 / pide iniciar sesión** al primer intento (`yt-dlp` sobre
`YhtaF9O7JRg`, 2026-09-26). Según `AYUDANTE.md` no insistí en bucle: usé
**Dailymotion** para los 6 vídeos de abajo (opening, dos cierres, tráiler y 3
escenas), todos bajados y **mirados de verdad** con `fotogramas.py --cortes`
(un fotograma por plano) y revisados con Read. Son reproducciones de
aficionados, **resolución baja** (320×240 a 512×312, medida con `ffprobe`):
lo digo con ⚠️ donde afecta. Es lo mejor disponible bajo la regla de «no
insistir con YouTube»; si una sesión futura recupera acceso a YouTube, estas
mismas escenas están descritas en `datos-video.md`/`biblia.md` §2 con más
detalle textual (subtítulos) que se puede cruzar con 1080p real.

Carpeta de trabajo con los vídeos y las hojas de contacto:
`/tmp/claude-0/trabajo/15-spongebob-video/` (opening, ending, ending2,
trailer, krusty_training, help_wanted, born_again_krabs — cada una con
`hoja_NN.jpg` e `indice.json` con el segundo exacto y el enlace `&t=`).

---

## Hallazgos

### Punto 2 · Escenas icónicas, miradas fotograma a fotograma

**1 · «Krusty Krab Training Video»** (corto independiente, no el episodio
03x10 completo — mismo contenido, minutos propios) ✅ visto entero,
119 fotogramas, 5:37 min, [Dailymotion](https://www.dailymotion.com/video/x3uvarj):
- 0:03-0:03 — storyboard: **Aaron Springer y C.H. Greenblatt**, storyboard
  artist **Caleb Meurer** (créditos en pantalla) ✅ visto.
- 0:29 — El Crustáceo Cascarudo de día, letrero de concha «THE KRUSTY KRAB»,
  banderas de señales, flores de fondo (turquesa) — [ver](https://www.dailymotion.com/video/x3uvarj?t=29).
- 0:38 — mismo plano de noche, luna llena — [ver](https://www.dailymotion.com/video/x3uvarj?t=38).
- 0:42 — **Don Cangrejo duerme dentro del Crustáceo**, en una cama con forma
  de barquito — dato nuevo: su casa/cuarto está DENTRO del restaurante en
  este corto (contrasta con «Se busca ayuda», ver abajo, donde su casa es un
  cofre aparte) — [ver](https://www.dailymotion.com/video/x3uvarj?t=42) ✅.
- 1:20 — tablero **«YOUR WORK STATION»** con los ingredientes rotulados:
  Ketchup, Mustard, Mayo, Patties, Pickles, Misc., Onions, Tomatoes, Lettuce,
  Buns — [ver](https://www.dailymotion.com/video/x3uvarj?t=80) ✅ (para el
  investigador de texto: interfaz/cartel del restaurante).
- 1:40 — Calamardo con el botón **«I REALLY WISH I WEREN'T HERE RIGHT
  NOW»**, leyendo un libro, apoyado — confirma con minuto real la pose que la
  biblia (§2.2/§15) sólo tenía deducida del subtítulo — [ver `&t=100`](https://www.dailymotion.com/video/x3uvarj?t=100) ✅ visto.
- 3:52-3:54 — **primer plano de la caja registradora**: caja gris oscura/
  antracita, cajón abierto y vacío, pantalla pequeña arriba, botones
  circulares; Don Cangrejo a un lado, Patricio y Arenita (o similar) comiendo
  al fondo — [ver `&t=232`](https://www.dailymotion.com/video/x3uvarj?t=232) ✅ visto (paleta medida abajo, §4).
- 3:55 — **«THE MONEY IS ALWAYS RIGHT!»**: Don Cangrejo irrumpe por la
  puerta, pinzas rojas bien abiertas, ojos como platos, boca abierta
  gritando — la frase perfecta para el canal — [ver `&t=235`](https://www.dailymotion.com/video/x3uvarj?t=235) ✅ visto.

**2 · «Se busca ayuda» / Help Wanted (01x01), doblada al latino** ✅ visto
entero (recorte de 7:40 min, calidad baja — grabación dentro de un marco de
TV falso, resolución real 512×288 ⚠️), [Dailymotion](https://www.dailymotion.com/video/x51sid2)
(descripción del propio vídeo: «Bob esponja en español latino Episodio 1»):
- 1:13 — Bob Esponja hace ejercicio bajo un cartel **«PAIN»** en el gimnasio
  — [ver `&t=73`](https://www.dailymotion.com/video/x51sid2?t=73).
- 4:30 — **la casa de Don Cangrejo es un cofre del tesoro** (no el
  Crustáceo): se le ve dentro, con Bob llamando a la puerta — dato para el
  punto 4/16 (sitios) — [ver `&t=270`](https://www.dailymotion.com/video/x51sid2?t=270) ✅.
- 6:57 — Don Cangrejo señala el letrero **«THE KRUSTY KRAB»** y se lo
  presenta a Bob Esponja — pose de **presentar** el negocio — [ver `&t=417`](https://www.dailymotion.com/video/x51sid2?t=417) ✅.
- 7:30 — plano final del letrero y la fachada, ya con Bob dentro — [ver `&t=450`](https://www.dailymotion.com/video/x51sid2?t=450).

**3 · «Born Again Krabs» (03x16, "el corazón de la sección 2.1")** ✅ visto
entero (corto independiente de 5:49 min), [Dailymotion](https://www.dailymotion.com/video/x3uhkek)
(«Born Again Krabs (Peedy)»):
- 0:05 — créditos: **animation director Tom Yasumi, creative director Derek
  Drymon** — [ver `&t=5`](https://www.dailymotion.com/video/x3uhkek?t=5) ✅ visto (dato para el investigador de texto/técnica).
- 1:16-2:38 — Don Cangrejo en cama de hospital tras casi ahogarse; un
  **fantasma verde de su propia tacañería** lo persigue y discute con él
  (secuencia larga, 1:32 a 2:31) — el «demonio interior del avaro», muy
  visual — [ver `&t=92`](https://www.dailymotion.com/video/x3uhkek?t=92) ✅.
- 3:12 — cuelga un cartel **«LIVE FOR TODAY»** y regala comida: **«COMPANY
  POLICY»** escrito en una hamburguesa (3:21) — pose de **celebrar/generosidad**
  — [ver `&t=192`](https://www.dailymotion.com/video/x3uhkek?t=192) ✅.
- 3:47 — llega la **factura: «BILL — TOTAL DUE $10,000»**, primer plano en
  sus pinzas — pose de **miedo/pánico por dinero**, contraste perfecto con la
  generosidad — [ver `&t=227`](https://www.dailymotion.com/video/x3uhkek?t=227) ✅.
- 3:52 — Don Cangrejo y Calamardo en la caja registradora, cobrando — mismo
  mueble que en el corto 1, otro ángulo — [ver `&t=232`](https://www.dailymotion.com/video/x3uhkek?t=232) ✅.
- 4:53 — **«GRAND RE-OPENING»**, letrero nuevo en la fachada — [ver `&t=293`](https://www.dailymotion.com/video/x3uhkek?t=293) (n.º 88 del índice).

> Las tres escenas están en 512×288-312 px (Dailymotion), no 1080p: es lo que
> dio la red disponible esta sesión (⚠️ resolución). El contenido y los
> minutos están verificados mirando el vídeo entero, no deducidos.

### Punto 4 · Sitios, luz y paleta (medida en fotogramas, no de memoria)

Resuelve el ⚠️ «Luz (de memoria; comprobar en fotogramas)» de la biblia
actual (§5.4):

- **Exterior del Crustáceo, de día** (fotograma 0:24 de «Krusty Krab
  Training Video», 1280×720 al extraerlo): cielo turquesa liso, sin
  degradado fuerte; sombra plana bajo el edificio; flores de fondo en 3
  colores (amarillo, celeste, violeta) — confirma que las «flores» no son
  sólo nubes (§5.3 de la biblia): son un motivo que se repite también en el
  fondo del exterior, pintado a mano. Paleta medida con `estilo.py`:
  **cielo `#289FBF`** (27 %), verde agua `#4BC2AB` (24 %), madera/sombra
  oscura `#1F1F15` y `#465247` (15 %+13 %), arena `#D0CFBA` (14 %), flor
  verde `#97A680` (7 %) ✅ medido, [Dailymotion `&t=24`](https://www.dailymotion.com/video/x3uvarj?t=24)
  (frame en `frames/fotograma_00024.jpg`).
- Confirma **luz plana de mediodía, sin sombras duras**, tal como decía la
  biblia con ⚠️: ahora es ✅ (visto).
- **Caja registradora, de cerca** (fotograma 3:52 de «Born Again Krabs»,
  1280×780): cuerpo **gris antracita** `#282927` (28 %), no azul como
  sugería el nombre «Cashy»; ventana del local en azul `#3C95B7` (10 %),
  camisa/pinzas de Don Cangrejo `#B93F23` (5 %), fondo casi negro por el
  encuadre `#040505` (37 %, incluye barras del vídeo) ✅ medido, [Dailymotion `&t=232`](https://www.dailymotion.com/video/x3uhkek?t=232).
  Corrige/matiza §5.5 de la biblia («`#427193` `#89BED7`», medido de otra
  fuente/§3.4): con la caja real en pantalla el cuerpo es más **gris oscuro
  que azul**; puede ser una diferencia de modelo entre temporadas —
  dejar ambas medidas con su fuente.
- **Casa de Don Cangrejo**: dos versiones distintas confirmadas mirando
  vídeo — un **cofre del tesoro** aparte (Help Wanted, 4:30) y, en el corto
  de entrenamiento, **una cama-barquito dentro del propio Crustáceo**
  (0:42). Las dos son reales, de episodios distintos; no es un error, es
  continuidad floja de la serie (dato para §5/§25) ✅ visto en ambas.
- **Cierre de la serie (crédito de producción)**: cartela amarilla con
  flores (fondo de «BACKGROUND PAINTERS», dailymotion `x3v1puo` `&t=16`),
  y el logo de **United Plankton Pictures Inc.** dibujado a mano —
  personajes-plancton en trazo de rotulador sobre fondo cian (`&t=34`) — el
  mismo estilo «garabato» que el logo de Nickelodeon en scribble naranja
  sobre negro (`&t=39`) ✅ visto, [Dailymotion](https://www.dailymotion.com/video/x3v1puo).
  Útil para el punto 18 (estilo): el estudio cierra CADA episodio con un
  logo dibujado a mano, no vectorial.
- **Texturas**: nada nuevo que añadir a §5.6 de la biblia (madera de Poly
  Haven ya cubierto); no encontré textura de papel térmico libre — sigue ⚠️.

### Punto 9 · Música (confirmado visualmente, plano a plano, sobre el opening real)

Vi el opening completo (no un mash-up de fans): 42 s, 19 planos,
[Dailymotion, «Bob Esponja Intro»](https://www.dailymotion.com/video/x8hj84s),
451 vistas del corte más visto de todos los que devolvió la búsqueda (18 334
en el canal `espinof`) ✅:
- 0:01–0:06 — cortina negra y luego el **retrato enmarcado del capitán
  pirata** (voz narradora pregunta «Are you ready, kids?») — [ver `&t=6`](https://www.dailymotion.com/video/x8hj84s?t=6).
- 0:11 — agua con burbujas (el «Aye, aye, Captain!»).
- 0:14 — Bob Esponja sale de su piña («¿Quién vive en una piña…?»).
- 0:15-0:16 — salpicón en la bañera y primer plano sonriendo (letra:
  «SpongeBob SquarePants!» cantado) — [ver `&t=16`](https://www.dailymotion.com/video/x8hj84s?t=16).
- 0:19-0:22 — **título «SpongeBob SquarePants»** en letras de colores estilo
  alga/esponja sobre fondo violeta — coincide justo con el coro cantado del
  tema — [ver `&t=22`](https://www.dailymotion.com/video/x8hj84s?t=22).
- 0:24-0:33 — pez nadando, algas, Bob bailando/dando karatazos entre las
  plantas (los golpes de música rápidos del ukelele) — [ver `&t=29`](https://www.dailymotion.com/video/x8hj84s?t=29).
- 0:38 — bumper de **Nickelodeon** — [ver `&t=38`](https://www.dailymotion.com/video/x8hj84s?t=38).
- 0:41 — tarjeta **«created by Stephen Hillenburg»** — [ver `&t=41`](https://www.dailymotion.com/video/x8hj84s?t=41).

Esto confirma plano a plano lo que la biblia (§11) ya tenía por letra escrita
(sin ver vídeo): la sincronía real entre la letra y el dibujo, con enlace y
segundo exacto para cada corte, en vez de sólo la letra.

**Cierre/creditos**: la cortina final NO lleva canción propia (es instrumental
corto); lo que sí es reconocible es el **logo garabateado de United Plankton
Pictures y de Nickelodeon** (arriba, §4) como remate visual, con el listado
de «Background Painters» en letras rosa sobre fondo de flores amarillo — dato
nuevo para la biblia, no estaba.

Además, clip promocional oficial de **Nickelodeon Latinoamérica** («La
Mascota de Plankton», con bumper final «Encuentra Bob Esponja más en Nick»,
0:48-0:49) ✅ visto entero, 17 planos, [Dailymotion](https://www.dailymotion.com/video/x6i3rnb):
confirma que sí hay clips oficiales en español disponibles vía Dailymotion,
no sólo fan-made (usado también en el punto 14, Plankton).

### Punto 10 · Vídeos (tráiler oficial con minuto, mirado plano a plano)

**Tráiler oficial doblado de «Bob Esponja: En busca de los pantalones
cuadrados»** (película 2025, la misma que cita la biblia en §12) ✅ visto
entero, 63 s, 31 planos, [Dailymotion, canal `sensacinemx`, 19 960 vistas](https://www.dailymotion.com/video/x9mmh7y)
(«Tráiler Oficial Doblado»):
- 0:00-0:06 — tarjetas de texto «ESTE AÑO / ALGO GRANDE / LLEGA A LOS
  CINES» intercaladas con **grito de Bob Esponja a pantalla completa**
  (boca enorme, ojos muy abiertos) — [ver `&t=4`](https://www.dailymotion.com/video/x9mmh7y?t=4) — pose de **urgencia**.
- 0:10 — **Patricio con la boca abierta de golpe**, mismo recurso de grito
  — [ver `&t=10`](https://www.dailymotion.com/video/x9mmh7y?t=10).
- 0:13 — plano de grupo: todo el elenco corriendo/reunido dentro de un
  interior de madera (posible Crustáceo) — sirve para una idea de «todos
  corren por la oferta» — [ver `&t=13`](https://www.dailymotion.com/video/x9mmh7y?t=13).
- 0:31 — Don Cangrejo y Calamardo asustados frente a un monstruo verde —
  [ver `&t=31`](https://www.dailymotion.com/video/x9mmh7y?t=31).
- 0:33 — Bob Esponja sentado, cabizbajo, con un ladrillo al lado — pose de
  **pensar/desánimo**, útil para contraste — [ver `&t=33`](https://www.dailymotion.com/video/x9mmh7y?t=33).
- 0:39 — **Don Cangrejo con guantes de boxeo, furioso** — pose de
  **regañar/pelear** — [ver `&t=39`](https://www.dailymotion.com/video/x9mmh7y?t=39).
- 0:49 — logotipo de la película **«BOB ESPONJA — En busca de los
  pantalones cuadrados»**.
- 0:57 — **Bob Esponja y Patricio codo a codo, de pie, listos para la
  aventura** — pose de **animar/celebrar en pareja** — [ver `&t=57`](https://www.dailymotion.com/video/x9mmh7y?t=57).
- 0:59 — tarjeta final **«AGÁRRATE LOS PANTALONES»**, con los logos de
  Nickelodeon y Paramount Pictures — [ver `&t=59`](https://www.dailymotion.com/video/x9mmh7y?t=59).

Es CGI 3D (no el dibujo 2D clásico): color más saturado y luz de estudio,
buen contraste para mostrar en la biblia que la franquicia tiene dos
estilos visuales activos a la vez (2D de serie y 3D de película) — dato para
§18 (estilo).

No encontré tráilers de temporada (sólo de película) en Dailymotion; YouTube
(que sí los tendría, canal oficial) dio 429 esta sesión — ver «No encontré».

### Punto 14 · Poses analizadas por personaje (minuto real, verificado mirando el vídeo)

Sustituye/confirma las poses de la §15 de la biblia que estaban **deducidas
del subtítulo, sin ver el fotograma** (la propia sección lo avisaba). Formato:
personaje · qué hace · para qué sirve · fuente y minuto real.

**Don Cangrejo**
- Duerme en su cama-barquito dentro del Crustáceo, 0:42, *Krusty Krab
  Training Video* — **descansar/dueño de casa** — [`&t=42`](https://www.dailymotion.com/video/x3uvarj?t=42) ✅.
- Irrumpe por la puerta gritando «THE MONEY IS ALWAYS RIGHT!», pinzas muy
  abiertas, ojos como platos, 3:55, *Krusty Krab Training Video* —
  **regañar/proclamar** — [`&t=235`](https://www.dailymotion.com/video/x3uvarj?t=235) ✅.
- De pie junto a la caja con el cajón abierto y vacío, mirando alarmado,
  3:52, *Krusty Krab Training Video* — **explicar/mostrar la caja** —
  [`&t=232`](https://www.dailymotion.com/video/x3uvarj?t=232) ✅.
- Señala el letrero «THE KRUSTY KRAB» explicándole el negocio a Bob
  Esponja, 6:57, *Help Wanted* — **presentar** — [`&t=417`](https://www.dailymotion.com/video/x51sid2?t=417) ✅.
- Cuelga el cartel «LIVE FOR TODAY» con los brazos extendidos, sonriente,
  3:12, *Born Again Krabs* — **celebrar/generosidad** — [`&t=192`](https://www.dailymotion.com/video/x3uhkek?t=192) ✅.
- Sostiene la factura de $10 000 con las pinzas temblando, ojos muy
  abiertos, 3:47, *Born Again Krabs* — **miedo/pánico por dinero** —
  [`&t=227`](https://www.dailymotion.com/video/x3uhkek?t=227) ✅.
- Con guantes de boxeo, furioso, cargando contra algo fuera de plano, 0:39,
  tráiler 2025 — **pelear/regañar** — [`&t=39`](https://www.dailymotion.com/video/x9mmh7y?t=39) ✅.

**Calamardo**
- Apoyado en la caja, leyendo un libro, con el botón «I REALLY WISH I
  WEREN'T HERE RIGHT NOW» bien visible en la camisa, 1:40, *Krusty Krab
  Training Video* — **queja/desgana en el trabajo** — [`&t=100`](https://www.dailymotion.com/video/x3uvarj?t=100) ✅
  (confirma con minuto real la pose que en §15 de la biblia estaba
  «deducida, sin ver»).
- Cobrando junto a Don Cangrejo en la caja, cara seria, 3:52, *Born Again
  Krabs* — **atender de mala gana** — [`&t=232`](https://www.dailymotion.com/video/x3uhkek?t=232) ✅.

**Bob Esponja**
- Hace ejercicio bajo un cartel «PAIN», gesto de esfuerzo, 1:13, *Help
  Wanted* — **animar(se)** — [`&t=73`](https://www.dailymotion.com/video/x51sid2?t=73) ✅.
- Grito a pantalla completa, boca enorme, 0:04, tráiler 2025 —
  **urgencia** — [`&t=4`](https://www.dailymotion.com/video/x9mmh7y?t=4) ✅.
- Sentado, cabizbajo, junto a un ladrillo, 0:33, tráiler 2025 —
  **pensar/desánimo** — [`&t=33`](https://www.dailymotion.com/video/x9mmh7y?t=33) ✅.
- De pie junto a Patricio, listo para la aventura, 0:57, tráiler 2025 —
  **animar/celebrar en pareja** — [`&t=57`](https://www.dailymotion.com/video/x9mmh7y?t=57) ✅.
- Sale de su piña por la puerta, sonriendo, 0:14, opening — **presentar** —
  [`&t=14`](https://www.dailymotion.com/video/x8hj84s?t=14) ✅.

**Patricio**
- Boca abierta de golpe, ojos muy abiertos, grito de sorpresa, 0:10,
  tráiler 2025 — **sorpresa/alarma** — [`&t=10`](https://www.dailymotion.com/video/x9mmh7y?t=10) ✅.
- Codo a codo con Bob Esponja, pose heroica de pie, 0:57, tráiler 2025 —
  **animar/celebrar** — [`&t=57`](https://www.dailymotion.com/video/x9mmh7y?t=57) ✅.

**Plankton** (clip promocional oficial en español, *«La Mascota de
Plankton»*, [Dailymotion, con bumper final «Encuentra Bob Esponja más en
Nick»](https://www.dailymotion.com/video/x6i3rnb) → confirma fuente
Nickelodeon LA, no fan-made):
- Camina junto a su mascota gigante (un gusano rosa con dientes) que se le
  descontrola, antena hacia arriba, ojo único preocupado, 0:22-0:25 —
  **explicar un problema / preocupación** — [`&t=22`](https://www.dailymotion.com/video/x6i3rnb?t=22) ✅.
- De pie, diminuto junto a los barrotes de una jaula de refugio de
  animales, mirando hacia arriba, 0:31 — **pensar/plan** — [`&t=31`](https://www.dailymotion.com/video/x6i3rnb?t=31) ✅.

> Todas estas poses están vistas fotograma a fotograma con `fotogramas.py
> --cortes` (contact sheets en la carpeta de trabajo) y confirmadas con Read;
> ninguna es deducción del subtítulo.

---

## Lo mejor para la lámina

- **«THE MONEY IS ALWAYS RIGHT!»** (Don Cangrejo, 3:55 de *Krusty Krab
  Training Video*, [enlace](https://www.dailymotion.com/video/x3uvarj?t=235)):
  la frase y la pose (pinzas muy abiertas, grito) resumen el canal
  #ofertas-y-gratis mejor que cualquier otra encontrada.
- La **caja registradora real** (3:52, [enlace](https://www.dailymotion.com/video/x3uhkek?t=232)):
  gris antracita `#282927`, cajón abierto — referencia exacta para modelar
  el objeto del plan (la caja del Crustáceo) en vez de inventarla.
- El **logo garabateado de United Plankton Pictures** al cierre de cada
  episodio ([enlace](https://www.dailymotion.com/video/x3v1puo?t=34)): útil
  para un remate de lámina «hecho a mano», no genérico.
- Calamardo con el botón **«I REALLY WISH I WEREN'T HERE RIGHT NOW»** (1:40,
  [enlace](https://www.dailymotion.com/video/x3uvarj?t=100)): el propio botón
  ya es un cuadro de diálogo/prop con texto — se puede recrear como sticker.
- El **contraste generosidad/pánico** de Don Cangrejo en *Born Again Krabs*
  (3:12 «LIVE FOR TODAY» → 3:47 factura de $10 000): dos poses del mismo
  personaje a 35 s de distancia, perfectas para antes/después de una oferta.

## No encontré

- **Tráileres de temporada / anuncios de estreno en Dailymotion**: sólo
  aparecieron tráilers de las películas (2015, 2020, 2025). Búsquedas:
  «SpongeBob trailer official», «bob esponja temporada estreno». YouTube
  (que sí los tendría, en el canal oficial) dio **429 / pide iniciar
  sesión** en el único intento (no insistí, según regla de AYUDANTE.md).
- **Storyboards de YouTube (Plan C)**: no los probé porque dependen del
  mismo `player response` de YouTube que dio 403/429; no gasté un segundo
  intento porque Dailymotion ya dio las 6 fuentes necesarias.
- **AnimeThemes**: no aplica — SpongeBob no es anime, la base no tiene
  entradas de la serie (comprobado: `datos-video.md` no trae ninguna).
- **Muestras de audio de Doblaje Wiki para complementar el opening en
  español**: no las busqué yo (le toca al investigador de voz, que ya
  trabaja el doblaje en `partes/voz.md`); el opening que vi es la versión
  original en inglés.
- **Ending real cantado** (con música, no sólo la cortina de crédito): los 2
  clips de «ending credits» que encontré (x3uqwjd, x3v1puo) son la cortina
  de logos, no un tema cantado — no existe un «ending» musical propio en
  SpongeBob (los créditos van sobre un fragmento instrumental corto); lo
  marco como **no aplica**, no como «no encontré».

## Bitácora de búsqueda (segunda pasada · investigador de vídeo)

- Español — Dailymotion API (`api.dailymotion.com/videos?search=`): «Bob
  Esponja Don Cangrejo dinero», «Bob Esponja capitulo completo latino»,
  «cha ching bob esponja», «Don Cangrejo dinero cancion», «krusty krab
  training video», «bob esponja crustaceo cascarudo escena», «Selling Out
  cha ching bob esponja español», «Born Again Krabs free toys», «bob
  esponja capitulo final creditos», «bob esponja pelicula 2025 trailer
  español», «En busca de los pantalones cuadrados trailer 2025»,
  «Plankton formula secreta bob esponja», «Plankton Karen escena bob
  esponja» → varias decenas de resultados filtrados, 7 vídeos usados.
- Inglés — Dailymotion: «SpongeBob opening intro official», «SpongeBob
  credits ending», «Krusty Krab Training Video clip» → 2 vídeos usados
  (opening x8hj84s, créditos x3v1puo).
- Dailymotion `api.dailymotion.com/users?search=` para identificar canales
  reales: «Nickelodeon Latinoamerica», «Paramount SpongeBob», «SpongeBob
  SquarePants» → ningún canal oficial verificado con certeza (todo son
  resubidas de usuarios); lo digo en cada cita.
- YouTube — 1 intento (`yt-dlp --dump-json` sobre `YhtaF9O7JRg`): HTTP 429 y
  403. No reintenté (regla de AYUDANTE.md: esperar 3-5 min y no insistir en
  bucle; el resto de la tanda se hizo con Dailymotion).
- Archive.org (`advancedsearch.php`): «spongebob squarepants episode»,
  «spongebob squarepants opening», «bob esponja capitulo» → nada
  directamente usable (DVD ISOs completos, remakes de fans, no clips
  cortos); no bajé nada de ahí.
- Vídeos bajados y mirados enteros con `herramientas/fotogramas.py --cortes`
  (fotograma por plano) + Read de las hojas de contacto: opening (19
  planos), 2 cierres (5+4 planos), tráiler (31 planos), Krusty Krab
  Training Video (119 planos, 2 hojas), Se busca ayuda (11 planos), Born
  Again Krabs (93 planos, 2 hojas), La Mascota de Plankton (17 planos) —
  **299 fotogramas mirados en total**, 7 vídeos.
- Paleta medida con `herramientas/estilo.py --colores` sobre 2 fotogramas a
  1280 px extraídos con `--fotograma`: exterior del Crustáceo (día) y caja
  registradora en primer plano.
- Resoluciones de los 7 vídeos medidas con `ffprobe` (320×240 a 512×312):
  todas por debajo de 1080p — límite de las fuentes en Dailymotion
  disponibles, no de la búsqueda.

Sigue: nada obligatorio pendiente de los puntos 2, 4, 9, 10 y 14. Si hay más
tanda: probar de nuevo YouTube (pueden haber pasado los 3-5 min) para un
tráiler de temporada y el ending cantado si existiera; y medir paleta de 1-2
fotogramas más (interior del Crustáceo de noche) con estilo.py.
