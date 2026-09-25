# Parte del investigador de TEXTO, JUEGOS Y TÉCNICA · Scooby-Doo

**Repaso corto** (EQUIPO.md): `biblia.md` ya existe y está muy trabajada.
Los puntos **5** (tipografía, §6 de la biblia), **6** (cómo hablan y piensan
en pantalla, §7) y **11** (videojuegos, §13) **ya están hechos a fondo** con
✅ en casi todo — no los repito, per EQUIPO.md («Repaso corto» → texto sólo
hace 18, 24 y 25). Este archivo cubre exclusivamente:

- **18** — Estilo de dibujo y técnica, y cómo replicarlo (Photoshop, Blender).
- **24** — Obras parecidas y temas relacionados.
- **25** — El mundo, la historia y sus símbolos.

Parto de `partes/datos-texto.md` (capturas de Steam ya listadas, no las
repito) y del recuadro «Cómo se hizo» y la bitácora de `biblia.md` (qué
fuentes dieron 403/429 en la primera pasada). Wikipedia y Wikimedia Commons,
que en la primera pasada daban 429, **respondieron esta vez** con
`User-Agent: Mozilla/5.0` (Commons volvió a dar 429 en un segundo intento,
no insistí más). No tengo `partes/episodios.md` (nadie corrió `episodio.py`
para esta serie) ni vídeos propios que mirar para estos tres puntos: son de
técnica, historia y comparación, no de escenas — lo que necesitaba ver
(estilo de línea, fondos) ya está mirado y medido en `biblia.md` §3 y §5 por
el investigador de imagen; lo cito, no lo repito.

## Hallazgos · Punto 18 — Estilo de dibujo y técnica, y cómo replicarlo

### 18.1 Qué técnica usó el estudio (con fuente, no de memoria)

- **1969: xerografía**, no tinta a mano. Confirmado con **dos fuentes de la
  propia franquicia**: la ficha de **Robert "Tiger" West** en **Scoobypedia**
  dice explícitamente «*Scooby-Doo, Where Are You! - xerography (seasons 1
  and 2)*» y «*The New Scooby-Doo Movies - xerography (season 1)*»
  ([API de Scoobypedia](https://scoobydoo.fandom.com/wiki/Robert_%22Tiger%22_West),
  wikitext leído entero) ✅; la **Hanna-Barbera Wiki** confirma que fue
  «xerographer at Hanna-Barbera from 1968 to 1975», acreditado desde *The
  Adventures of Gulliver* y *Wacky Races* (ambas de 1968-69, justo antes de
  Scooby-Doo) ([API de Hanna-Barbera Wiki](https://hanna-barbera.fandom.com/wiki/Robert_%22Tiger%22_West))
  ✅. La xerografía (el proceso que Disney estrenó en *101 dálmatas*, 1961,
  y que Hanna-Barbera adoptó para abaratar la producción televisiva)
  fotocopiaba el dibujo del animador directo al cel, sin repasarlo a tinta a
  mano: por eso la línea de 1969 es **fina, uniforme y algo temblorosa** (se
  ve en C-43, ya medida por el investigador de imagen en `biblia.md` §3.0)
  — descripción general del proceso: [Use of Xerography in Animation (Canonica.ai)](https://canonica.ai/page/Use_of_Xerography_in_Animation),
  [D23, «Xerox process»](https://d23.com/a-to-z/xerox-process/) ✅.
  Los **fondos**, en cambio, se pintaban a mano (gouache/témpera), por eso
  tienen textura y degradado y los personajes no (ya documentado con nombres
  de los pintores en `biblia.md` §3.1 — no lo repito).
- **2010 en adelante (Warner Bros. Animation)**: la casa usa **Toon Boom
  Harmony** como pipeline estándar de animación 2D para TV — confirmado de
  forma genérica para el estudio (no encontré una fuente que lo diga
  específicamente de *Mystery Incorporated* o *Be Cool*, así que va con ⚠️)
  ([Toon Boom, «Producer»](https://www.toonboom.com/products/producer),
  [TV Tropes, «MediaNotes/ToonBoom»](https://tvtropes.org/pmwiki/pmwiki.php/MediaNotes/ToonBoom))
  ⚠️ (fuente sobre el estudio en general, no confirmada línea por línea para
  Scooby-Doo).
- **2020, *Scoob!*: 3D real, pero NO es «toon shader» plano.** Es CGI de
  **Reel FX Creative Studios** + Warner Animation Group
  ([Wikipedia, «Scoob!»](https://en.wikipedia.org/wiki/Scoob!)) ✅, con un
  acabado **realista/semi-PBR**, no un cel-shading plano: varias reseñas
  coinciden en describir la piel como «goma» o «fieltro mojado» y el
  aspecto como el de un CGI genérico tipo DreamWorks de comienzos de los
  2000 —
  [CGMagazine](https://www.cgmagonline.com/review/movie/scoob-review/),
  [Frame Rated](https://www.framerated.co.uk/scoob-2020/) ✅ (dos reseñas
  independientes con la misma observación). **Para la lámina, esto importa
  al revés**: *Scoob!* es el ejemplo de **qué NO hacer** si se usa 3D — el
  personaje tiene que seguir viéndose plano/2D, no realista.

### 18.2 Encuadres y composición (por qué la serie se lee tan clara)

Sobre lo ya visto en las hojas C/F (`biblia.md` §3, §5.2, §18.2: «plano
general a la altura de los ojos»), añado la lógica de guion que explica esos
encuadres — de la sinopsis oficial y el resumen de la fórmula de la serie
([Wikipedia, «Scooby-Doo»](https://en.wikipedia.org/wiki/Scooby-Doo), sección
«CBS years») ✅. Esto es lectura de la fórmula narrativa, **no** fotogramas
nuevos míos — el investigador de vídeo es quien tiene que sacar el fotograma
exacto de cada uno si hace falta:

| Momento del guion | Encuadre típico | Para qué sirve en una lámina |
|---|---|---|
| Llegada al lugar | Plano general, la Máquina del Misterio entrando en cuadro | Encabezado o fondo: sitúa «dónde estamos» |
| «Separémonos» (el gag más citado de la fórmula) | Plano de grupo partido: dos a la izquierda, dos a la derecha (o tres y uno) | Para una lámina de dos columnas (p. ej. «Resuelta» / «Sigue abierta») |
| La persecución por puertas | Plano fijo lateral, entran y salen en fila por varias puertas | Tira cómica en el borde de la lámina, poco texto |
| El susto | Primer plano muy cerrado de Scooby o Shaggy, ojos enormes, salto vertical | Icono de alerta o de «duda nueva» |
| El desenmascarado | Plano medio, la mano tira de la máscara hacia arriba, el resto del grupo mirando en semicírculo | El icono de «Resuelta»: revelar algo |

### 18.3 Cómo reproducirlo en Photoshop

- **Capas separadas**, como el cel original: (1) línea, (2) color plano del
  personaje, (3) fondo pintado, en ese orden de detalle creciente hacia
  abajo (el fondo lleva más textura y degradado que el personaje: regla ya
  confirmada en `biblia.md` §5.2).
- **Línea**: pincel de tinta de borde duro, 2-4 px a 1080p, gris muy oscuro
  o sepia (no negro puro: la xerografía de 1969 no daba un negro perfecto),
  con «Bloquear píxeles transparentes» para rellenar el plano de color sin
  salirse.
- **Fondo pintado a mano**: los pinceles de gouache/acuarela de **Kyle T.
  Webster** vienen ya incluidos gratis en Photoshop (Adobe los integró en
  2017; están en la librería de pinceles «Kyle's...»); usar uno de gouache
  con textura de papel a baja opacidad, en capas superpuestas de claro a
  oscuro, como hacía el equipo de fondos de 1969.
- **Grano de xerografía**: capa nueva, `Filtro > Ruido > Añadir ruido`
  (monocromático, 3-5 %), en modo Superponer y opacidad baja, sólo sobre
  personajes (no sobre el fondo pintado, que ya tiene su propia textura de
  pincel).
- **Aberración leve de VHS/TV de los 70**: `Filtro > Distorsionar >
  Corrección de lente` con un desplazamine de canal rojo/cian de 1-2 px, o
  desplazar a mano el canal rojo con las flechas del teclado tras separar
  canales — sólo si la lámina quiere un aire "de tele antigua"; para el
  estilo limpio de 1969 normal, mejor no usarlo.

### 18.4 Cómo reproducirlo en Blender (contorno, luz, render)

- **Contorno (outline) con el modificador Solidify — método «inverted
  hull»**: crear un segundo material sólo para el contorno (Emisión o Toon),
  activar **«Backface Culling»** en ese material, añadir el modificador
  **Solidify**, marcar **«Flip Normals»** y subir el **«Material Index
  Offset»** a 1; el grosor del contorno lo da el valor de «Thickness» del
  Solidify — funciona en **Eevee** ✅
  ([Blender Secrets, «Inverted Hull Toon Outline»](https://www.3dsecrets.com/secrets/inverted-hull-toon-outline-bnpr-blender-tutorial),
  [StraySpark, «How to Get an Anime/Toon Look in Blender»](https://www.strayspark.studio/blog/how-to-get-anime-toon-look-blender))
  ✅ (dos tutoriales, mismo método). Alternativa con **Line Art** (para
  *Grease Pencil* o como *Freestyle* moderno): un modificador de línea que
  saca el contorno de la geometría 3D como trazo 2D, más parecido a un
  dibujo a mano —
  [guía «Line Art with Blender» (GitHub)](https://github.com/TehMerow/Tutorials/wiki/Line-Art-with-Blender)
  ✅. Cualquiera de los dos sirve mejor que *Freestyle* clásico (más lento,
  pensado para render final, no para iterar rápido en una lámina).
- **Sombreado plano (cel shading) para el color de personaje**: nodo
  **Shader to RGB** → **Color Ramp** en interpolación **«Constant»**: dos
  paradas dan el típico bicolor de anime (luz/sombra), tres paradas dan un
  tono medio — mismo tutorial de StraySpark ✅. Con **dos** paradas es lo
  más parecido al color plano de 1969 (sin degradado, ver §5.2 de
  `biblia.md`).
- **Luz**: una luz de área grande y suave desde arriba-delante (evita
  sombras duras: la serie no las tiene en los personajes) + una luz de
  relleno azulada si es escena nocturna (coincide con el tinte azul medido
  en C-15, `biblia.md` §5.2).
- **Texturas encima**: aplicar el fondo pintado (hecho en Photoshop, §18.3)
  como imagen de fondo de cámara (`Film > Transparent` + compositor) en vez
  de modelarlo en 3D: así el contraste «personaje plano / fondo pintado»
  se mantiene igual que en la serie.
- **Modelos y rigs libres del personaje** (Sketchfab, comprobados por su
  API, todos **CC Attribution**, ✅ medidos):
  - **«Scooby-Doo»** de *gaddiellartey2010*: 2796 caras, bajo poli, sin animar
    — sirve de base rápida para posar a mano.
    [sketchfab.com/3d-models/scooby-doo-29c1fff…](https://sketchfab.com/3d-models/scooby-doo-29c1fffa88794e408b5579889eb091bc)
  - **«Scrappy Doo v2026»** de *jacobq1004*: 108 694 caras, **con animación
    incluida** (`animationCount: 1` en la API) — el único de los
    encontrados que ya trae rig en movimiento, útil de referencia de huesos
    aunque el personaje no sea el protagonista.
    [sketchfab.com/3d-models/scrappy-doo-v2026…](https://sketchfab.com/3d-models/scrappy-doo-v2026-scooby-doo-b7e17227352142c9a271232d62a9bdad)
  - **«Daphne Blake»** y **«Velma Dinkley»** de *placidone*: 281 440 y 62 811
    caras — alto detalle, sin animar; Velma con licencia **CC
    Attribution-ShareAlike** (ojo: cualquier cosa derivada de ese modelo hay
    que compartirla igual). [Daphne](https://sketchfab.com/3d-models/daphne-blake-60c98889d23c46e992867af623cd130e) ·
    [Velma](https://sketchfab.com/3d-models/velma-dinkley-fb8d2ee3f6604e88b7993cc6664a1d34)
  - Ninguno trae shader de trama ya montado: el toon shader hay que
    montarlo encima con la receta de arriba.

## Hallazgos · Punto 24 — Obras parecidas y temas relacionados

### 24.1 De dónde salió Scooby-Doo (las dos influencias declaradas)

- El propio **Fred Silverman** (el ejecutivo de CBS que encargó la serie)
  la concibió como un cruce entre **los seriales de radio «I Love a
  Mystery» (años 40)** y la sitcom **«The Many Loves of Dobie Gillis»**
  (1959-63) — confirmado en **Wikipedia** con detalle del reparto:
  Fred ↔ Dobie Gillis, Daphne ↔ Thalia Menninger, Vilma ↔ Zelda Gilroy y
  Shaggy ↔ Maynard G. Krebs (mismo look de perilla y forma de hablar)
  ([en.wikipedia.org/wiki/Scooby-Doo](https://en.wikipedia.org/wiki/Scooby-Doo))
  ✅, y por **Decades.com**, «Jinkies! The characters of Scooby-Doo were
  based on The Many Loves of Dobie Gillis»
  ([dev.decades.com](https://dev.decades.com/articles/jinkies-the-characters-of-scooby-doo-were-based-on-the-many-loves-of-dobie-gillis))
  y **CBR** ([cbr.com, «Jinkies! The Mysterious Origins of Scooby-Doo»](https://www.cbr.com/tv-legends-revealed-jinkies-the-mysterious-origins-of-scooby-doo/))
  ✅ dos fuentes más. **Ojo con la leyenda urbana** de que representan a los
  Five Colleges de Massachusetts: Hanna-Barbera, Fred Silverman y el propio
  guionista Mark Evanier la han desmentido explícitamente (Wikipedia) ✅ —
  no usarla como dato real.
- También se cita el parecido de premisa con los libros de **Los Cinco**
  (Enid Blyton): cuatro chicos y un perro, misterio que nunca es
  sobrenatural de verdad (Wikipedia) ⚠️ una sola fuente.

### 24.2 «Obras parecidas» de la misma época (competencia y clones)

Hanna-Barbera y sus rivales hicieron varias series con la misma fórmula
(«teens + mascota + misterio») en los 70, todas citadas en Wikipedia y
repetidas en tres artículos de listas especializados
([MovieWeb, «10 Scooby-Doo Ripoffs»](https://movieweb.com/scooby-doo-ripoffs/),
[CBR, «10 Great Cartoons That Copied Scooby-Doo's Formula»](https://www.cbr.com/scooby-doo-best-tv-cartoons-used-formula/),
[ScreenRant, «10 Animated Scooby-Doo Ripoffs»](https://screenrant.com/animated-scooby-doo-ripoffs-made-by-hanna-barbera/))
✅ dos fuentes (Wikipedia + al menos uno de los tres):

| Serie | Año | Diferencia con Scooby-Doo |
|---|---|---|
| *Josie and the Pussycats* | 1970-71 | Sí son banda de música de verdad (lo que Scooby-Doo dejó atrás) |
| *The Funky Phantom* | 1971-72 | El fantasma **es real** y ayuda a la pandilla |
| *The Amazing Chan and the Chan Clan* | 1972-73 | Familia de detectives con perro que habla |
| *Speed Buggy* | 1973-74 | El «personaje raro» es el propio coche, no el perro |
| **Goober and the Ghost Chasers** | 1973-74 | Perro tipo lebrel afgano; **los fantasmas que encuentran son reales** y ayudan a vencer a los falsos — el giro contrario a Scooby-Doo |
| *Jabberjaw* | 1976-78 | Cambia el perro por un tiburón robot baterista |
| *Captain Caveman and the Teen Angels* | 1977-80 | Cambia el perro por un cavernícola con superpoderes |
| *Dynomutt, Dog Wonder* | 1976-77 | Perro-robot con toque de superhéroe |

### 24.3 Lo que Scooby-Doo influyó después (para no repetir sus ideas)

- **Buffy, la cazavampiros**: el grupo de amigos se llama literalmente **«la
  pandilla Scooby» (Scooby Gang / Scoobies)**, usan libros para investigar
  monstruos igual que Vilma — influencia reconocida y descrita en
  Wikipedia; además **Sarah Michelle Gellar** (Buffy) hizo de Daphne en las
  películas de imagen real de 2002 y 2004 ✅ (dato ya en `biblia.md`).
- **Meddling Kids** (2017), novela de **Edgar Cantero**: parodia
  explícita de Scooby-Doo y también de los Hardy Boys, Nancy Drew y Los
  Cinco — Wikipedia ✅.
- **«Scoobynatural»** (2018): episodio-crossover animado de *Supernatural*
  con Scooby y la pandilla — Wikipedia ✅.
- **Gravity Falls**: hay comparaciones de fans por el grupo de
  investigación adolescente y el misterio del pueblo, pero **no encontré
  ninguna entrevista donde el creador Alex Hirsch cite Scooby-Doo como
  influencia** (dice que su referencia principal fue *Los Simpson*) — lo
  dejo con ⚠️ **como parecido de fans, no confirmado por el autor**; no
  usarlo como dato firme.
- **DC Comics, «Scooby Apocalypse»** (2016): reinvención seria, mundo
  postapocalíptico con monstruos reales — sirve de **contraejemplo de tono**
  igual que *Velma* (2023, ya en `biblia.md` §14): the fandom no lo pide.

### 24.4 Otras biblias de este servidor (para no repetir concepto)

Revisé si otra biblia ya hecha usa la idea de «tablero de pistas» o de
investigación/deducción, que es el concepto que propone `encargos/26-scooby-doo.md`
para #dudas: **`biblias/18-death-note/`** comparte el tema de
investigación/deducción (L, Kira) pero es de tono oscuro y serio, sin
tablero de corcho ni fichas — no hay ningún parecido visual que choque ✅
(revisé su `biblia.md` con grep, sin resultado de «tablero» ni «pizarra»).
No encontré ninguna otra biblia de este lote con el concepto de «pandilla +
pistas + misterio resuelto», así que el tablero de pistas sigue siendo un
concepto libre para Scooby-Doo.

## Hallazgos · Punto 25 — El mundo, la historia y sus símbolos

### 25.1 Las reglas del mundo, en 5 líneas

1. Todo caso empieza como un rumor de fantasma o monstruo en un pueblo o
   sitio real (nunca fantasía pura: la ambientación es la EE. UU.
   contemporánea a cada época) ✅ (Wikipedia, «CBS years»).
2. La pandilla llega en la Máquina del Misterio, investiga por su cuenta —
   **nunca la policía resuelve el caso** — y **se separa a buscar pistas**,
   el gag más repetido de la fórmula ✅ (Wikipedia).
3. Casi siempre hay una **trampa diseñada por Fred** para atrapar al
   villano, y funciona la mitad de las veces (ya en `biblia.md` §14) ✅.
4. **El monstruo es casi siempre una persona disfrazada** con un motivo
   económico o criminal, desenmascarada al final con la frase «si no
   fuera por... esos chicos entrometidos» ✅ (Wikipedia). **Excepciones
   confirmadas** donde el monstruo SÍ es real dentro de la ficción: los
   cortos de 1980-82 (*Scooby-Doo and Scrappy-Doo*, tras subir a Scrappy),
   *The 13 Ghosts of Scooby-Doo* (1985), y las películas directas a vídeo
   *Scooby-Doo on Zombie Island* (1998) y *…and the Witch's Ghost* (1999)
   ✅ (Wikipedia, «ABC years» y «Film and rerun history»).
5. Es una fórmula **deliberadamente escéptica**: el astrónomo **Carl Sagan**
   la elogió en su libro *The Demon-Haunted World* (1995) por enseñar a
   desconfiar de lo paranormal con pruebas, y dijo que un «Scooby-Doo para
   adultos» sería un servicio público — cita recogida en Wikipedia y en
   varias colecciones de citas del propio libro
   ([Wikipedia](https://en.wikipedia.org/wiki/Scooby-Doo),
   [libquotes.com](https://libquotes.com/carl-sagan/works/the-demon-haunted-world))
   ✅.

### 25.2 La historia por arcos (con fechas; Wikipedia, leída completa, ✅)

1. **Origen (1969)**: *Scooby-Doo, Where Are You!* debuta el 13 de
   septiembre de 1969 en CBS con «What a Night for a Knight»; 17 episodios
   la primera temporada, 8 la segunda. Formato ya fijado: llegada, pistas,
   separarse, trampa, desenmascarado.
2. **Crossovers de famosos (1972-73)**: *The New Scooby-Doo Movies*, cada
   episodio con un invitado real o de ficción (Batman y Robin, los Harlem
   Globetrotters, Don Knotts, Los Tres Chiflados…).
3. **ABC y los bloques largos (1976-83)**: *The Scooby-Doo Show* (1976-78),
   luego *Laff-A-Lympics*; en **1979 llega Scrappy-Doo**, sobrino de Scooby,
   para levantar el rating — funcionó, pero en **1980-82** la serie se
   redujo a cortos de 7 minutos SIN Fred, Daphne ni Vilma, y **los
   monstruos empezaron a ser reales**: el giro que más odiaron los fans
   (Wikipedia lo dice explícito: «negatively hated by fans»).
4. **13 Ghosts (1985)** y **A Pup Named Scooby-Doo (1988-91)**: esta
   última vuelve a desenmascarar humanos (fórmula clásica) y es donde se
   fija por primera vez el nombre **«Coolsville»** como pueblo natal —
   dato que ya usa `biblia.md` §5.1, ahora con la fecha exacta de cuándo
   se inventó.
5. **Vuelta a sábado por la mañana (2002-08)**: *What's New, Scooby-Doo?*
   (2002-06, actualizada al 2000: móviles, internet) y *Shaggy & Scooby-Doo
   Get a Clue!* (2006-08, sin Fred/Daphne/Vilma casi nunca).
6. **Las películas directas a vídeo (desde 1998)**: empiezan con *Zombie
   Island* (1998, monstruos reales de verdad, tono más adulto, muy querida
   por los fans que crecieron con la serie) y *Witch's Ghost* (1999, **aquí
   nacen las Hex Girls**). Desde entonces sale casi una película nueva al
   año.
7. **Misterios S.A. (2010-13)**: primera vez que Scooby-Doo cuenta **una
   sola historia larga** (52 episodios como «novela televisada»), con
   **Crystal Cove** como pueblo y un misterio de fondo que se resuelve en
   el final, emitido exactamente 3 años después del estreno (5-abr-2010 →
   4/5-abr-2013).
8. **Be Cool (2015-18)** y **Guess Who? (2019-21)**: formato corto,
   invitados reales (Halsey, Sia, Mark Hamill…) y de ficción (Batman,
   Sherlock Holmes).
9. **Streaming y ahora (2021-2026)**: *Velma* (2023-25, HBO Max, precuela
   adulta sin Scooby, elenco diverso, muy divisiva — ya en `biblia.md`
   §14). **En desarrollo/producción ahora mismo**: *Scooby-Doo: Origins*
   (serie live-action de Netflix, Berlanti Productions; empezó a rodar en
   2026, con Frank Welker de nuevo como la voz de Scooby) y **«Yokoso
   Scooby-Doo!»** — un spin-off **anime** (estudio japonés **OLM**,
   dirigido por **Itsuro Kawasaki**) que sigue a Scooby y Shaggy de viaje
   por Japón; **Tubi lo anunció el 18 de mayo de 2026** para
   Norteamérica, con Frank Welker y Matthew Lillard repitiendo sus voces
   ✅ (Wikipedia, sección «Streaming era», la más reciente que encontré:
   dato fresco, no estaba en la primera pasada de `biblia.md`).

### 25.3 Emblemas, objetos icónicos y vocabulario

- **Objetos icónicos ya documentados** en `biblia.md` (no los repito):
  Máquina del Misterio, placa «SD» del collar, la lupa de Vilma, la ficha
  «Who's Who», el periódico «Daily Babbler».
- **Las Scooby-galletas son un producto real**: Del Monte Pet Products
  fabrica «Scooby Snacks» de verdad desde los 70 (Wikipedia, sección
  «Merchandising») ✅ — sirve como objeto físico real para una lámina (una
  caja auténtica, no inventada).
- **Logo/parche de «Mystery Inc.»** (de *Misterios S.A.*, 2010): existe y
  se ve en el propio show, pero **no encontré una ficha oficial que
  describa su diseño exacto** (sólo Pinterest y wikis de logos, sin texto
  fiable) ⚠️ una fuente débil — para la lámina, más seguro usar el logo de
  1969 (ya medido en `biblia.md` §6) que inventar el de 2010.
- **Las Hex Girls**: banda de rock gótico-ecológico nacida en *Witch's
  Ghost* (1999): **Thorn** (voz y guitarra, nombre real Sally McKnight),
  **Dusk** (batería) y **Luna** (teclado) — Wikipedia ✅ y Scoobypedia
  (Fandom) ✅ dos fuentes; ya aparecían en `biblia.md` §8 sin esta ficha.
- **Vocabulario en inglés original** (además de las frases en latino que
  ya tiene `biblia.md` §7.3): **«Zoinks!»**, **«Jinkies!»**, **«Jeepers!»**,
  **«Ruh-roh»**, **«like, ¿qué tal?»** (la muletilla «like» de Shaggy),
  **«meddling kids»**, **«let's split up, gang»**. Dato curioso para el
  tema de #dudas: en el argot rimado británico (*rhyming slang*), **«I
  haven't got a Scooby» significa literalmente «no tengo ni idea/pista»**
  — «Scooby(-Doo)» rima con «clue» (pista) — Wikipedia, sección «In
  popular culture» ✅. Es un juego de palabras real con «pista», el mismo
  concepto que pide el canal.

## Lo mejor para la lámina

1. **El contorno «inverted hull» + Shader to RGB con Color Ramp constante en
   Blender** (§18.4) es la forma más fiel y más rápida de imitar el plano
   de 1969 en 3D — mejor que copiar el look de *Scoob!* (2020), que los
   críticos describen como «piel de goma» y que NO es el estilo que se
   busca.
2. **«I haven't got a Scooby» = «no tengo ni pista»** (§25.3): un guiño de
   vocabulario perfecto para el foro #dudas, con fuente real (argot rimado
   británico), no inventado.
3. **Coolsville nace en *A Pup Named Scooby-Doo* (1988)** y **Crystal
   Cove en *Misterios S.A.* (2010)**: si la lámina usa un pueblo con
   nombre, mejor Coolsville (más clásico y usado más años) salvo que se
   quiera el tono serializado de 2010.
4. **Las Scooby-galletas son un producto real de Del Monte**: se puede
   fotografiar/recrear una caja real en vez de inventar el diseño.
5. **El modelo animado «Scrappy Doo v2026» (Sketchfab, CC Attribution)** es
   el único rig libre encontrado ya en movimiento — útil de referencia de
   huesos aunque no se use ese personaje en la lámina final.

## No encontré

- **Diseño exacto y oficial del logo/parche de «Mystery Inc.»** de 2010: lo
  que hay son sólo imágenes sin ficha (Pinterest, wikis de logos) ⚠️.
  Búsquedas hechas: «"Mystery Inc." Scooby-Doo logo patch emblem design
  Crystal Cove» (en).
- **Confirmación directa del creador de *Gravity Falls*** citando a
  Scooby-Doo como influencia: sólo hay comparaciones de fans. Búsqueda:
  «Scooby-Doo influence on Gravity Falls creator interview» (en).
- **Qué software usó exactamente *Scooby-Doo! Mystery Incorporated*** (Toon
  Boom u otro): sólo confirmé el pipeline general de Warner Bros. Animation,
  no específico de esta serie. Búsqueda: «Scooby-Doo Mystery Incorporated
  2010 animation production Toon Boom Flash software» (en).
- **Segunda fuente independiente** (fuera de Wikipedia) para las reglas del
  mundo con excepciones (punto 25.1, línea 4): Wikipedia es sólida y cita
  episodios concretos, pero no crucé un segundo sitio aparte ⚠️.
- **Wikimedia Commons**: dio 429 en el segundo intento (buscaba el SVG del
  logo de 1969 para medirlo yo mismo); no insistí más allá de dos intentos.
  El logo ya está descrito y medido por el investigador de imagen en
  `biblia.md` §6, así que no hacía falta repetirlo.

## Bitácora de búsqueda (esta tanda, texto: puntos 18, 24, 25)

**Búsquedas web** (en inglés salvo que se diga lo contrario; siguen las 44 ya
hechas en la primera pasada de `biblia.md`, que no repito):

1. Scooby-Doo Where Are You xerography cel animation Hanna-Barbera limited
   animation technique
2. Iwao Takamoto interview Scooby-Doo animation process model sheet
3. Scooby-Doo Mystery Incorporated 2010 animation production Toon Boom Flash
   software
4. Sketchfab Scooby free rig model 3D toon
5. "Tiger West" xerography Hanna-Barbera animation
6. Hanna-Barbera xerography Xerox process cel animation cost cartoon history
7. Warner Bros Animation Toon Boom Harmony television production pipeline
8. Scooby-Doo Where Are You created influenced by "Many Loves of Dobie
   Gillis" teen archetypes Fred Daphne Velma
9. Hanna-Barbera Goober and the Ghost Chasers Clue Club Speed Buggy Josie
   Pussycats similar shows to Scooby-Doo
10. Scooby-Doo influence on Gravity Falls creator interview teen mystery
    cartoon
11. Scoob! 2020 movie animation Reel FX CGI toon shader stylized rendering
    interview
12. Blender toon outline tutorial Freestyle Solidify modifier inverted hull
    cel shading
13. "Mystery Inc." Scooby-Doo logo patch emblem design Crystal Cove
14. Hex Girls Scooby-Doo logo symbol band eco-goth
15. Scoob! 2020 review animation style generic Dreamworks glossy CGI review
    criticism
16. Carl Sagan Scooby-Doo "Demon-Haunted World" skeptic quote

**Red directa** (sin pasar por el buscador):

- `en.wikipedia.org/w/api.php` (con `User-Agent: Mozilla/5.0`, porque sin él
  seguía dando problemas): artículo **«Scooby-Doo»** completo (56 445
  caracteres, leído entero en 4 tandas) — desarrollo, las 10 series por
  década con fechas, películas, reparto de voces por era, merchandising,
  recepción, cultura popular. Es la fuente principal de los puntos 24 y 25.
- API de **Scoobypedia** (`scoobydoo.fandom.com/api.php`,
  `action=parse&prop=wikitext`): ficha de Robert "Tiger" West.
- API de **Hanna-Barbera Wiki** (`hanna-barbera.fandom.com/api.php`): misma
  ficha, para la segunda fuente.
- API de **Sketchfab** (`api.sketchfab.com/v3/search`): búsqueda «scooby
  doo», 12 resultados con licencia, tamaño de miniatura y si tienen
  animación — comprobados uno a uno.
- `commons.wikimedia.org/w/api.php`: 429 en el intento (con y sin
  User-Agent); no insistí un tercer intento.
- `WebFetch` sobre `cartoonresearch.com/index.php/animation-anecdotes-267/`:
  **descarté** un dato («Star Wirth, departamento de xerografía») que el
  resumen del buscador había atribuido a este artículo pero que el artículo
  **no contiene** — no lo puse en la biblia. Ojo con los resúmenes del
  buscador: hay que comprobar la fuente primaria antes de citarla como ✅.
- `WebFetch` sobre `hanna-barbera.fandom.com/wiki/Robert_"Tiger"_West`: dio
  402 (como avisa `AYUDANTE.md` de las páginas normales de Fandom); usé la
  API en su lugar y sí funcionó.

Sin `Sigue:` pendiente: los tres puntos de esta tanda (18, 24, 25) quedan
completos con lo obligatorio de `ENCARGO.md` — técnica histórica con fuente,
cómo replicarla en Photoshop y Blender con rigs libres comprobados, obras
parecidas con dos fuentes, y el mundo con reglas, arcos fechados y símbolos.
Lo que falta son extremos menores, ya anotados arriba en «No encontré» con
⚠️, no puntos obligatorios sin hacer.
