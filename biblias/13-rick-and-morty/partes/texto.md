# Parte · Investigador de texto, juegos y técnica · Rick and Morty (13-rick-and-morty)

Puntos de ENCARGO.md: **5 (tipografía), 6 (cuadros de diálogo), 11 (videojuegos),
18 (estilo y técnica, cómo replicarlo), 24 (obras parecidas), 25 (mundo y símbolos)**.

Contexto: la `biblia.md` de este encargo **ya existe** (se escribió con la red
cerrada, ver su recuadro «Cómo se hizo») y ya cubre bastante bien los puntos 5,
6 y 11 (sus secciones 6, 7 y 13). Los puntos **18, 24 y 25 no existen todavía**
en la biblia: son el hueco principal de esta parte. Esta libreta trae
confirmaciones nuevas para 5/6/11 (sobre todo donde había ⚠️ o «no encontré») y
todo lo necesario para escribir 18, 24 y 25 desde cero.

`datos-texto.md` (recolector automático) sólo traía las 7 capturas de Steam de
*Virtual Rick-ality*: las miré (ver punto 11) y no repetí esa consulta.

---

## Hallazgos

### 5 · Tipografía (complementa la sección 6 de la biblia)

- **Crank!** (nombre real **Christopher Crank**), rotulista profesional de
  Cincinnati (Ohio); ha rotulado para Image, Dark Horse, Oni Press y Dynamite,
  y es el rotulista de los cómics de *Rick and Morty* de Oni Press (incluido
  *Pocket Like You Stole It*) · fuentes: [Blue Juice Comics — bio de Crank!](https://bluejuicecomics.com/about/crank/),
  [crankletters.blogspot.com](http://crankletters.blogspot.com/p/lettering.html)
  ✅ (dos fuentes, en inglés). Su letra personal de rotulación **no está
  publicada como fuente descargable** (no es una «font» que se pueda bajar,
  es su mano/estilo de rotulista): sigue sin identificarse un archivo exacto,
  pero ahora sí sabemos quién es y qué otros cómics rotula.
- **Letra libre equivalente a rotulación de cómic** (mejor que Sniglet o
  Grandstander para el globo de cómic, que son más «redonda amable» que
  «rotulado a mano»): **Comic Relief** (Google Fonts / Fontsource, licencia
  **OFL-1.1**) ✅ ([ficha de Fontsource](https://fontsource.org/fonts/comic-relief)).
  Comprobada con **fontTools** en el archivo `latin-400-normal.ttf` bajado de
  Fontsource: trae **á é í ó ú ñ Ñ ¿ ¡ Á É** — todo `True` en el cmap ✅
  (comprobación propia, no de memoria).

### 6 · Cómo hablan y piensan en pantalla (complementa la sección 7 de la biblia)

- **Pocket Mortys**, interfaz de crafteo: una barra **rosa pálida** abajo de
  la pantalla, texto centrado en negro **negrita, sans-serif**, tipo aviso de
  tutorial («*Add an item to the table to start crafting.*») — no es un globo
  de cómic, es una barra de ayuda de videojuego móvil · fuente: captura oficial
  de la wiki, `Crafting_Station_interface.png`, **1920×1080** (medida) ✅.
  Vista directamente (ver punto 11).
- **Virtual Rick-ality**: el texto en pantalla es **diegético** (dentro del
  mundo, nunca flotando): un cartel de tienda rotulado a mano
  («SALESMAN RICK'S», letra redonda gruesa con contorno negro, estilo cómic),
  una nota de papel pinchada en un corcho («VOUCHER — REPLACEMENT MORTY») y un
  **diagrama tipo plano técnico** (fondo azul, líneas blancas, textos en
  mayúsculas con círculos rojos de aviso: «DETACH FROM BODY», «TRAP IN BALL»,
  «VOICEBOX») · fuente: capturas oficiales de Steam, **1920×1080** (medidas)
  ✅. Esto es justo lo que pide el dueño: nada de burbuja blanca, el texto
  vive en un objeto del mundo (cartel, nota, plano).

### 11 · Videojuegos de la franquicia (reemplaza/amplía la sección 13 de la biblia)

- **Pocket Mortys** (13 ene 2016, **Big Pixel Studios**, publicado por *Adult
  Swim Games*, iOS/Android, gratis con compras) ✅ ([Wikipedia, vía resumen de
  búsqueda](https://en.wikipedia.org/wiki/Pocket_Mortys)) — **corrige** a la
  biblia actual, que no daba el estudio (sólo decía «parodia de Pokémon»).
  - Estructura confirmada: **mundo abierto en vista cenital** (pixel art),
    pantalla de **combate por turnos** lateral con HP, cambio de Morty, ítems
    y huída, y menús de equipo ✅ (Wikipedia).
  - **Vistas directamente** dos capturas oficiales de la wiki de Fandom:
    - *Overworld* (`Salesmanrick_in_game.png`, **1280×720**, medida): d-pad
      táctil abajo a la izquierda, botón «A» abajo a la derecha (controles de
      consola retro), personajes con **contorno negro grueso y colores
      planos**, cartel de tienda en letra rotulada gruesa con contorno negro,
      etiquetas rojas «SALE» ✅.
    - *Crafteo* (`Crafting_Station_interface.png`, **1920×1080**, medida):
      máquina de ciencia ficción (esfera azul brillante, cables de colores),
      3 botones verdes «ADD», pestañas «Craft / Share / Recipes», barra de
      aviso rosa abajo (ver punto 6) ✅.
  - No vi captura de la **pantalla de combate**: queda como ⚠️ (la estructura
    la confirma Wikipedia, pero no el diseño exacto de esa pantalla).
- **Virtual Rick-ality** (20 abr 2017, Owlchemy Labs, VR; ya estaba en la
  biblia). **Vistas directamente** las 6 capturas oficiales de Steam
  (`datos-texto.md`, todas 1920×1080):
  1. Garaje de Rick, vista en primera persona con manos VR, cartel amarillo
     «CAUTION WATCH FOR PORTALS», trampilla de portal en el suelo.
  2. Baño con un **portal verde en espiral** abierto sobre el lavabo.
  3. Mesa de trabajo del garaje con **cinta de precaución amarilla y negra**
     y una pantalla azul pequeña con texto de interfaz.
  4. Combate: manos como cañones robóticos disparando contra criaturas
     alienígenas voladoras y un ovni, sobre un paisaje rosado con «salchichas»
     gigantes de fondo.
  5. Auto volador con Morty y Summer atrás; botella de cerveza en la mano del
     jugador; salpicadero con botones físicos.
  6. Mesa con nota «VOUCHER — REPLACEMENT MORTY» y el plano técnico ya descrito
     en el punto 6.
  - Confirma: **sin barra de vida ni texto flotante** en pantalla; el juego se
    juega con las manos y por voz, y el único texto es el que hay dentro del
    mundo (carteles, notas, planos) ✅. Esto **resuelve** el «no encontré
    capturas verificadas de sus cajas de diálogo» que dejó la biblia: ahora sí
    hay capturas, y lo que muestran es justo que **no hay cajas de diálogo
    clásicas**, hay objetos con texto.
- **Clone Rumble** (móvil, cerrado) y apariciones en **MultiVersus** y
  **Fortnite**: sin cambios sobre lo que ya tiene la biblia (Game Rant).

---

### 18 · Estilo de dibujo y técnica, y cómo replicarlo (sección nueva, no existe en la biblia)

**Herramientas de producción** (✅ dos fuentes cada una):
- Guion gráfico y animación: **Toon Boom Storyboard Pro** y **Toon Boom
  Harmony** ✅ ([toonboom.com, blog propio de la empresa](https://www.toonboom.com/top-animation-news-mifa-rick-and-morty-the-dragon-prince-and-more),
  confirmado también por Wikipedia).
- Postproducción: **Adobe After Effects**; arte de fondos: **Adobe
  Photoshop** ✅ (Wikipedia, artículo «Rick and Morty»).
- **Diseño de personajes: Adobe Photoshop**, comprobado por mí viendo el
  vídeo oficial (ver abajo) — no es sólo Wikipedia, lo vi en pantalla.
- Estudios de animación por temporada: **Bardel Entertainment** (Vancouver),
  temporadas 1-8; desde la temporada 9, **Mercury Filmworks** (Ottawa);
  **Lighthouse Studios** (Kilkenny, Irlanda) se suma desde la temporada 7 ✅
  (Wikipedia).
- Pipeline (cita de Justin Roiland, vía resumen de búsqueda con fuente
  animationmagazine.net — ⚠️ una fuente, la web original dio 403): guion
  gráfico, diseños, *color keys* y fondos se hacen en Burbank (oficina de Los
  Ángeles) y se ensamblan en Vancouver, con ayuda de producción en Filipinas.

**Vi el vídeo oficial «Rick and Morty Style Guide» (Adult Swim, 2:42 min)**
— YouTube pedía iniciar sesión, así que lo vi en su copia de **Internet
Archive**: [archive.org/details/rick-and-morty-style-guide](https://archive.org/details/rick-and-morty-style-guide)
(mp4 original, 640×360, 162.7 s). Saqué 66 fotogramas por plano con
`fotogramas.py --cortes` y los miré con Read. Esto **resuelve** el «El vídeo
«Style Guide»: existe, pero no pude verlo» que dejó la biblia. Lo que
confirmé viéndolo yo mismo:

- **Software: Adobe Photoshop CC 2016.3** — leí el nombre en la barra de
  título de la pantalla, minuto 0:14 (hice zoom al fotograma) ✅ (visto
  directamente, dos veces, en dos fotogramas distintos).
- **Construcción por capas**: el panel derecho muestra 8-11 capas (guías +
  línea final) mientras dibuja.
- **Cómo dibuja a Morty** (min 0:26-1:22): cabeza ovalada con una línea guía
  curva cruzada (la proporción clásica de animación, como una esfera con
  ecuador marcado), **dos círculos de ojos de tamaño ligeramente distinto**
  con un punto de pupila centrado (asimetría a propósito, no error), boca en
  una sola curva simple, orejas pegadas a la cabeza, y luego el cuerpo como
  una **figura de palitos** (maniquí) antes de vestirlo con ropa simple.
- **Cómo dibuja a Rick** (min 1:16-2:42): primero el **pelo puntiagudo en
  zigzag** (antes que la cara), luego cejas muy marcadas y fruncidas, arrugas
  de la frente, un ojo más entrecerrado que el otro, boca abierta con dientes
  visibles y líneas de mueca.
- Entre medias (0:24-0:30) mete **fotogramas reales de episodios** como
  referencia de lo que se está enseñando a dibujar.
- Capturas propias (mías, en mi carpeta de trabajo, no subidas al repo):
  `styleguide_frames/hoja_01.jpg` y `hoja_02.jpg` (contactos de los 66
  cortes) y `styleguide_zoom/fotograma_00014.jpg` y `_00060.jpg` (detalle).

**Confirma con dos fuentes** (mi visionado del vídeo + entrevistas) que los
personajes se dibujan con **rasgos asimétricos a propósito**: *«the
characters are often drawn with odd or asymmetrical features, in order to
avoid looking too normal to live in the Rick and Morty universe»* — cita del
director de arte de la temporada 3 **Jeffrey Thompson** ✅ (resumen de
búsqueda citando Wikipedia/LinkedIn; confirmado visualmente por mí en el
vídeo: los dos ojos de Morty y de Rick NO son iguales de tamaño ni de forma).

**Dirección de arte, dos personas con nombre y entrevista**:
- **James McDermott** (director de arte temporadas 1-2): inspiración
  declarada en la ciencia ficción de los 70 (cita *Zardoz*, Roger Corman);
  su filosofía de diseño es el **«shape language»** (lenguaje de formas):
  *«A successful character drawing... often comes down to the language
  between its shapes»*; los alienígenas buscan ser **«squishy and gross but
  also familiar»**; las escenas domésticas se dibujan a propósito «cutres»
  para que contrasten con lo alienígena elaborado; cada mundo tiene un
  tratamiento visual coherente (en un «mundo perro», hasta los coches y las
  armas tendrían rasgos caninos) ✅ ([It's Nice That, entrevista](https://www.itsnicethat.com/features/inside-rick-and-morty-art-director-james-mcdermotts-sketchbooks-250717),
  en inglés).
- **Jeffrey Thompson** (director de arte temporada 3, venía de *Gravity
  Falls*): trabaja con **«color keys»** (fotogramas clave de color) para fijar
  el ánimo y la atmósfera de cada episodio antes de animarlo ✅
  ([Toronto Guardian, entrevista](https://torontoguardian.com/2017/01/rick-and-morty-artist-jeffrey-thompson/),
  en inglés). Hizo además el vídeo «Style Guide» ya descrito arriba.
- Influencias declaradas por **Justin Roiland**: *The Simpsons* (bocas y
  dientes parecidos «por generación compartida»); *Ren & Stimpy* le dio la
  **«boca en W»** de los personajes ✅ (Wikipedia, con cita).

**Línea y color** (de análisis visuales de terceros, no de entrevista directa
— marco todo ⚠️ salvo lo que comprobé yo mismo en el punto 3 de arte/colores
del equipo de imagen):
- Línea negra gruesa e irregular («wandering outlines»); pupilas
  desalineadas a propósito (coincide con la cita de Jeffrey Thompson) ⚠️.
- Paleta con verdes lima y morados intensos para portales y luz alienígena,
  tonos de piel planos, «rim light» (luz de borde) para vender el brillo del
  portal ⚠️.
- El «slime»/baba se dibuja en formas gráficas planas (gotas, burbujas,
  anillos), sin detalle realista de fluido ⚠️.

**Cómo replicarlo en Photoshop**:
- Capas separadas para **línea** y **relleno**; bloqueo de la capa de línea
  en modo Alfa para colorear dentro sin salirse (técnica descrita por el
  ilustrador **Jason Piperberg** en su tutorial de coloreado al estilo Rick
  and Morty) ✅ ([jasonpiperberg.com](https://jasonpiperberg.com/4140/4140/)).
  Brillo extra con aerógrafo suave en una capa en modo Pantalla / Luz suave /
  Superposición.
- Sombreado tipo *cel shading*: un tono más oscuro que el color base, pincel
  duro (sin difuminar), formas simples — es la técnica estándar de *cel
  shading* que coincide con lo que se ve en pantalla ⚠️ (guías genéricas de
  cel shading, no una entrevista del estudio).

**Cómo replicarlo en Blender — modelos y rigs libres, licencias comprobadas
por mí con la API de Sketchfab** (`api.sketchfab.com/v3/models/<id>`):
- **«Morty Rig Blender»** (mfxmotions) — licencia **CC Attribution (CC BY
  4.0)**, uso comercial permitido con crédito al autor ✅ (comprobado con la
  API, no de memoria) · [sketchfab.com/3d-models/morty-rig-blender-c99a7fbd39b84428ab99ec1af4b15800](https://sketchfab.com/3d-models/morty-rig-blender-c99a7fbd39b84428ab99ec1af4b15800).
- **«Portal gun (Rick and Morty)»** (kreems) — licencia **CC Attribution (CC
  BY 4.0)** ✅ comprobada con la API — **esto corrige** la entrada que ya
  tiene `referencias.json` de la biblia, que decía «comprobar si es CC BY»:
  ya está comprobado, sí lo es.
- **«Rick and Morty Meeseeks Box»** (MagunDongle) — la API de Sketchfab
  **ya no devuelve licencia** para este modelo (antes daba 403, ahora
  responde pero sin campo `license`): probablemente el modelo está
  restringido o el autor le quitó la licencia libre. **No usar** para nada
  comercial hasta comprobarlo a mano en la página ⚠️.
- **BlendSwap**: existen 8 modelos etiquetados «rick and morty» y 30
  etiquetados «toon shader», con licencia comunitaria tipo CC ⚠️ (confirmé
  que existen por búsqueda, no comprobé la licencia exacta de cada archivo
  uno por uno — quedaría para quien vaya a usar uno en concreto).
- Para el contorno tipo cómic en Blender: los tutoriales de fans usan
  **Freestyle** o un **Solidify** invertido (normales hacia dentro) más un
  material negro plano, con un **Toon BSDF** o un shader de nodos por
  rampa de color para el sombreado en bloques — es la técnica estándar para
  *toon shading* en Blender, no una confirmación oficial del estudio (ya
  usan Toon Boom 2D, no Blender) ⚠️.

**Encuadres y composición**: no encontré una entrevista o *making of*
específico sobre planos/ángulos por emoción del equipo de animación; lo que
hay son las escenas ya analizadas por los investigadores de vídeo y voz en el
resto de la biblia. **No encontré** nada nuevo que añadir aquí más allá de
eso (búsquedas: «Rick and Morty cinematography shot composition interview»,
sin resultados útiles, sólo genéricos).

---

### 24 · Obras parecidas y temas relacionados (sección nueva)

- Lista curada con razón para cada una ✅ ([TVLine, «15 TV Shows To Watch If
  You Like Rick And Morty»](https://www.tvline.com/2121225/tv-shows-like-rick-and-morty/),
  en inglés): *Doctor Who*, *Back to the Future: The Animated Series*,
  *Space Ghost Coast to Coast*, *The Venture Bros.*, *Bill & Ted's Excellent
  Adventures*, *Loki*, *South Park*, *American Dad!*, *BoJack Horseman*,
  *The Sandman*, **Solar Opposites**, *Star Trek: Lower Decks*, *Futurama*,
  *Voyagers!*, *Aeon Flux*.
- La más cercana por ADN: **Solar Opposites** (Hulu), creada por **Justin
  Roiland y Mike McMahan** (ambos de *Rick and Morty*): mismo estilo de
  animación y el mismo espíritu «que no se toma en serio», pero **sin** el
  método de guion de «*story circle*» de **Dan Harmon** que sí estructura
  Rick and Morty ✅ ([Bubbleblabber](https://www.bubbleblabber.com/2020/06/exploring-the-similarities-and-differences-between-rick-and-morty-and-solar-opposites/),
  [Inverse](https://www.inverse.com/entertainment/solar-opposites-review-justin-roiland-hulu),
  en inglés, dos fuentes).
- **Dan Harmon** describe la propia serie como un cruce entre ***The
  Simpsons*** y ***Futurama*** de Matt Groening, con «vida familiar
  balanceada con ciencia ficción dura» ✅ (Wikipedia, con cita directa).
- Influencias británicas declaradas: **The Hitchhiker's Guide to the
  Galaxy** y **Doctor Who** ✅ (Wikipedia).
- **Origen directo de la serie**: nació de un corto amateur no autorizado de
  2006, **«The Real Animated Adventures of Doc and Mharti»**, una parodia
  vulgar de *Back to the Future* que Justin Roiland hizo para el festival
  **Channel 101** (cofundado por Dan Harmon) — Doc Smith y Mharti McDonhalds
  (parodias de Doc Brown y Marty McFly) se convirtieron en Rick y Morty; el
  viaje en el tiempo pasó a ser viaje interdimensional para evitar líos
  legales con los estudios de *Volver al futuro* ✅ ([Rick and Morty Wiki, «The
  Real Animated Adventures of Doc and Mharti»](https://rickandmorty.fandom.com/wiki/The_Real_Animated_Adventures_of_Doc_and_Mharti),
  [Inverse](https://www.inverse.com/article/30812-rick-and-morty-troll-back-to-the-future-justin-roiland-origin-original-short),
  [ScreenRant](https://screenrant.com/rick-and-morty-back-to-the-future-origins-explained/),
  en inglés, tres fuentes).
- **Dentro del propio servidor**: comprobé los 90 encargos de `encargos/` y
  **ningún otro usa el canal #noticias-series** (`grep -l noticias-series
  encargos/*.md` sólo da este encargo): no hay choque de canal. Por tono y
  estilo, las biblias ya terminadas más parecidas son **27-cyberpunk-edgerunners**
  (animación adulta, ciencia ficción oscura, aunque en estilo anime, no
  cartoon estadounidense) y **14-adventure-time-hora-de-aventura** (viajes a
  mundos absurdos, tono mucho más amable). Ninguna comparte el humor
  cínico-adulto de Rick and Morty: no hay riesgo real de repetir ideas de
  lámina con otra ya hecha del servidor.

---

### 25 · El mundo, la historia y sus símbolos (sección nueva)

**Las reglas del mundo, en cinco líneas** (cada una con fuente):
1. Existen infinitos universos paralelos (el multiverso); Rick viaja entre
   ellos con la **pistola de portales** ✅ (wiki, *Portal Gun*).
2. Todos los Ricks y Mortys de la serie viven dentro de una porción acotada
   del multiverso, la **Central Finite Curve** («la Curva»): un muro
   construido a propósito alrededor de los universos donde Rick es el más
   listo; fuera de la Curva, Rick ya no sería especial ✅ (wiki, *Central
   Finite Curve*, con la cita de Evil Morty en «Rickmurai Jack»).
3. Los Ricks de miles de dimensiones se organizan en **la Ciudadela** (The
   Citadel, antes «Citadel of Ricks»), ciudad-estado en una dimensión de
   bolsillo, gobernada primero por el **Consejo de Ricks** (6 Ricks, portavoz
   Riq IV) y más tarde por un Morty presidente elegido (Evil Morty) ✅ (wiki,
   *The Citadel* / *Council of Ricks*).
4. La pistola de portales la inventó **Rick Prime**, que mató a la esposa e
   hija de Rick C-137 (Diane y Beth) cuando éste rechazó unirse a él: de ahí
   nace la venganza que mueve gran parte de la trama de las últimas
   temporadas ✅ (wiki, *Portal Gun* / *Rick Prime*).
5. Pese a toda la ciencia ficción, el motor de cada capítulo sigue siendo la
   familia Smith en su casa suburbana; el contraste entre lo doméstico
   «cutre» y lo alienígena elaborado es la regla visual base de la serie ✅
   (It's Nice That, entrevista a James McDermott).

**La historia por arcos** (fuente principal: [Den of Geek, «Rick and Morty:
Just the Lore Episodes»](https://www.denofgeek.com/tv/rick-and-morty-just-the-lore-episodes/),
en inglés, cruzada con la wiki de Fandom) ✅:
- **Arco 1 · El multiverso y la Ciudadela** (T1): «Rick Potion #9» (1×06)
  rompe el universo original de Rick y Morty y los obliga a huir a uno nuevo
  donde sus «yo» murieron — primer contacto real con el multiverso.
  «Close Rick-counters of the Rick Kind» (1×10) presenta la Ciudadela, el
  Consejo de Ricks y a **Evil Morty** por primera vez.
- **Arco 2 · La Federación Galáctica** (T2-T3): «The Wedding Squanchers»
  (2×10) — la boda de Ave Persona es una encerrona de la **Federación
  Galáctica**, que acaba ocupando la Tierra; «The Rickshank Rickdemption»
  (3×01) cierra ese cliffhanger y libera la Tierra. «The Ricklantis Mixup»
  (3×07) desarrolla la política de la Ciudadela y el ascenso de Evil Morty.
- **Arco 3 · El origen de Rick y Rick Prime** (T5-T6): «Rickternal
  Friendship of the Spotless Mort» (5×08) — flashback a la vida temprana de
  Rick y a la muerte de Diane; en la temporada 6 se revela que fue **Rick
  Prime** quien mató a Diane y Beth. «Rickmurai Jack» (5×10) explica la
  Central Finite Curve y vuelve a sacar a Evil Morty.
- **Arco 4 · La caza de Rick Prime** (T7): «Unmortricken» (7×05) — Rick y
  Evil Morty se alían, encuentran y casi derrotan a Rick Prime; Evil Morty
  roba los planos del «Omega Device» antes de dejar que Rick lo mate.
  «Fear No Mort» (7×10) explora la vida que Rick pudo tener con Diane.
- **Arco 5 · Después de Rick Prime** (T8-T9, actual): en T8, Summer y Morty
  escapan de una simulación tipo Matrix como castigo. La T9 arranca con
  «There's Something About Morty», donde se revela que Rick C-137 y Evil
  Morty llevaban tiempo trabajando juntos en secreto, y se enfrentan a una
  nueva amenaza para la Central Finite Curve llamada **el Colectivo (the
  Collective)** — la temporada 9 se estrenó el 25 de mayo de 2026 (ya
  registrado por el investigador de voz en la biblia).

**Símbolos, objetos icónicos y vocabulario propio** (todos ✅, wiki de
Fandom, wikitexto leído directamente, con la página exacta):
- **La pistola de portales**: portal verde en espiral; necesita «Quantum
  Transport Solution» (líquido verde brillante) para disparar; sin eso, no
  funciona · [Portal Gun](https://rickandmorty.fandom.com/wiki/Portal_Gun).
- **El Consejo de Ricks / la Ciudadela**: gobierno de Ricks, «Portal Fluid»
  restringido (de ahí el mercado negro de «Bootleg Portal Fluid») ·
  [The Citadel](https://rickandmorty.fandom.com/wiki/The_Citadel),
  [Council of Ricks](https://rickandmorty.fandom.com/wiki/Council_of_Ricks).
- **Central Finite Curve**: «el muro alrededor del infinito» — explica por
  qué Rick es siempre el más listo · [Central Finite Curve](https://rickandmorty.fandom.com/wiki/Central_Finite_Curve).
- **Mr. Poopybutthole**: personaje «Sausage Fella» recurrente en los cold
  opens; su frase de cabecera es «Ooh-wee!»; sus resúmenes de temporada son
  un ritual reconocido por el fandom · [Mr. Poopybutthole](https://rickandmorty.fandom.com/wiki/Mr._Poopybutthole).
- **Los Vindicadores (The Vindicators)**: equipo de superhéroes parodiado
  (tipo Vengadores/Guardianes de la Galaxia), con dos episodios especiales
  · [The Vindicators](https://rickandmorty.fandom.com/wiki/The_Vindicators).
- **Jerryboree**: guardería interdimensional de Jerrys, en un asteroide no
  registrado · [Jerryboree](https://rickandmorty.fandom.com/wiki/Jerryboree).
- **Blips and Chitz**: arcade intergaláctico con el videojuego dentro del
  videojuego «Roy: A Life Well Lived» · [Blips and Chitz](https://rickandmorty.fandom.com/wiki/Blips_and_Chitz).
- **Death Crystals**: cristales de Forbodulon Prime que muestran las formas
  en que morirás · [Death Crystal](https://rickandmorty.fandom.com/wiki/Death_Crystal).
- **Cronenberg World**: dimensión donde casi toda la humanidad se convirtió
  en monstruos mutantes («Cronenbergs») por un antídoto fallido de Rick — de
  ahí el verbo de fandom «cronenbergear» · [Cronenberg World](https://rickandmorty.fandom.com/wiki/Cronenberg_World).
- **«Wubba Lubba Dub Dub»**: la frase de cabecera de Rick; su significado
  real («estoy sufriendo mucho, ayúdenme», en el idioma nativo de Ave
  Persona) se revela en el especial «Ricksy Business», explicado por Ave
  Persona a Morty · [Birdperson (wikitexto)](https://rickandmorty.fandom.com/wiki/Birdperson)
  (leí el wikitexto completo, la cita está literal en la página). En el
  doblaje latino **no se traduce** (ya registrado en la biblia, sección 7.5).
- **«Get Schwifty»**: canción/episodio que se volvió meme y le dio nombre a
  una fuente tipográfica de fans (ver sección 6 de la biblia, ya
  registrado).

---

## Lo mejor para la lámina

1. **El vídeo «Style Guide» (Internet Archive)** es la mejor referencia de
   técnica: muestra en Photoshop, en vivo, cómo se construyen las cabezas de
   Rick y Morty con guías y asimetría a propósito — perfecto para «cómo
   replicarlo» y para que el redactor cite un minuto exacto y una imagen real
   del proceso (min 0:14 y 1:59-2:42).
2. Para el objeto del concepto de lámina (la caja del cable), el diagrama
   tipo plano técnico de *Virtual Rick-ality* («DETACH FROM BODY / TRAP IN
   BALL / VOICEBOX») es un ejemplo real y verificado de cómo la franquicia
   pone texto en pantalla sin burbujas: un plano pinchado en una pared, con
   círculos rojos de aviso.
3. El rig de Morty y la pistola de portales en Sketchfab (ambos **CC BY 4.0**,
   comprobados con la API) son los únicos modelos 3D de la franquicia con
   licencia libre confirmada al 100 % para Blender.
4. **Comic Relief** (OFL, tildes/ñ/¿¡ comprobadas con fontTools) es la letra
   libre más fiel a un cómic real si el concepto de lámina usa una viñeta.
5. El origen en «Doc and Mharti» (parodia de Volver al futuro) es un dato de
   trivia perfecto para el pie de la lámina o para un texto del bot: conecta
   con el canal de noticias de series.

## No encontré

- **Fuente/tipografía exacta de Crank!** para los cómics: sé quién es y qué
  más rotula, pero no hay un archivo de letra descargable con su nombre
  (búsquedas: «Crank! letterer font Oni Press credits», en inglés). Doy una
  alternativa libre comprobada (Comic Relief) en su lugar. ⚠️ No es un «no
  existe»: es que un rotulista dibuja a mano, no reparte su fuente.
- **Pantalla de combate de Pocket Mortys**: la estructura está confirmada por
  Wikipedia, pero no encontré (ni bajé) una captura oficial de esa pantalla
  concreta para mirarla (busqué en la categoría de la wiki de Fandom, sólo
  había overworld y crafteo).
- **Entrevista específica sobre encuadres y composición** (planos, ángulos
  por emoción) del equipo de animación: no apareció en las búsquedas
  («Rick and Morty cinematography shot composition interview», en inglés).
  Lo que hay de eso en la biblia lo cubren los investigadores de vídeo/voz
  con las escenas ya analizadas.
- **Licencia exacta de cada modelo de BlendSwap** (8 «rick and morty», 30
  «toon shader»): confirmé que existen, no comprobé licencia archivo por
  archivo (BlendSwap no tiene una API tan simple como Sketchfab).

## Bitácora de búsqueda (parte de texto)

**Buscador web** (WebSearch, todo en inglés salvo donde se dice; unas 15
búsquedas de las ~50 del cupo):
- «Rick and Morty animation style guide Toon Boom Photoshop line art
  interview» → software de animación y postproducción.
- «Rick and Morty character designer Justin Roiland style toon shader
  Blender fan» → primeras pistas de James McDermott y modelos 3D de fans.
- «"Rick and Morty" Bardel Entertainment "Toon Boom Harmony" animation
  process interview» → confirma estudios y pipeline (cita de Roiland).
- «Rick and Morty line weight color palette flat shading "The Art of Rick
  and Morty" artbook excerpt» → línea y paleta (fuentes de análisis, ⚠️).
- «"Rick and Morty" style Photoshop tutorial line art brush cel shading how
  to draw» → tutorial de Jason Piperberg.
- «Rick and Morty toon shader Blender tutorial rig free download character»
  → rigs de Sketchfab/BlendSwap.
- «Rick and Morty similar shows tone Solar Opposites Community Dan Harmon
  influences comparison» → punto 24.
- «Rick and Morty world rules Citadel of Ricks Council portal gun symbols
  vocabulary fandom» → punto 25.
- «shows like Rick and Morty Futurama Family Guy South Park tone comparison
  "if you like"» → punto 24.
- «Rick and Morty story arcs seasons Evil Morty Rick Prime finale overview
  TV Tropes» → punto 25.
- «Rick and Morty season by season summary arcs season 1 2 3 4 5 6 7 8 plot
  overview» → punto 25, encontró Den of Geek.
- «"Doc and Mharti" Justin Roiland Back to the Future parody short origin
  Rick and Morty» → origen de la serie, punto 24/25.
- «Jeffrey Thompson art director "Rick and Morty" interview asymmetrical odd
  features drawing» (dos veces) → cita sobre asimetría.
- «"Crank!" letterer comics font Oni Press "Rick and Morty" credits» y
  «Christopher Crank letterer ccrank.com bio comics lettering» → punto 5.
- «Rick and Morty grain filter chromatic aberration VHS look episode intro
  visual effect» → sin resultado útil específico de la serie.
- «Pocket Mortys screenshot battle dialogue box interface gameplay» → punto
  11, estructura de combate (Wikipedia).

**Red directa** (curl/Python, sin pasar por el buscador):
- API de **Fandom** (`rickandmorty.fandom.com/api.php`, `action=parse` y
  `action=query&list=search`): wikitexto completo de *Portal Gun*, *The
  Citadel*, *Council of Ricks*, *Central Finite Curve*, *Mr. Poopybutthole*,
  *The Vindicators*, *Jerryboree*, *Blips and Chitz*, *Death Crystal*,
  *Cronenberg World*, *Birdperson* (para «Wubba Lubba Dub Dub»); imágenes de
  `Category:Pocket_Mortys_screenshots` con `prop=imageinfo` para tamaño real.
- **Internet Archive**: `advancedsearch.php` para encontrar el mirror del
  «Rick and Morty Style Guide»; `metadata` para confirmar el archivo mp4
  (640×360, 162.73 s); descarga directa con curl (yt-dlp daba 500 en ese
  mirror, así que usé curl al mp4 directo).
- **Dailymotion** (`api.dailymotion.com`): probado, sin el clip que buscaba,
  no hizo falta al final (Internet Archive sí lo tenía).
- **`herramientas/fotogramas.py --cortes`** sobre el mp4 local del Style
  Guide → 66 fotogramas por plano, dos hojas de contacto, miradas con Read.
  Luego dos fotogramas sueltos en grande (min 0:14 y 1:00) con
  `--fotograma`, y un recorte con Pillow de la barra de título para
  confirmar «Adobe Photoshop CC 2016.3».
- **API de Sketchfab** (`api.sketchfab.com/v3/models/<id>`): licencias de
  «Morty Rig Blender», «Portal gun (Rick and Morty)» y «Rick and Morty
  Meeseeks Box» — las dos primeras CC BY 4.0, la tercera sin licencia ahora.
- **API de Fontsource** (`api.fontsource.org/v1/fonts`): filtro por
  `subsets=latin-ext` para encontrar «Comic Relief»; descarga del `.ttf` y
  comprobación con **fontTools** (`getBestCmap()`).
- **Capturas de Steam** de `datos-texto.md`: bajadas y miradas en hoja de
  contacto propia (Pillow) — cumple «no repitas la consulta, mira lo que ya
  hay».
- `grep -l noticias-series encargos/*.md`: comprobé que ningún otro encargo
  usa el mismo canal (punto 24).

**Lo que falló o no hizo falta usar**: `curl api.github.com` sin
autenticación para `google/fonts` (pide `add_repo`, no hizo falta: usé
Fontsource, que ya sirve el `.ttf`). `yt-dlp` contra YouTube directo:
bloqueado con «Sign in to confirm you're not a bot» (como avisa el mensaje de
arranque); no insistí, usé el mirror de Internet Archive.

## Sigue: nada obligatorio pendiente de mis 6 puntos (5, 6, 11, 18, 24, 25); si se relanza esta parte, sólo quedaría profundizar en el «No encontré» (pantalla de combate de Pocket Mortys, licencias BlendSwap una por una) si el redactor lo pide.
