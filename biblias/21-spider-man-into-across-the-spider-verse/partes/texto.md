# Parte de TEXTO, JUEGOS Y TÉCNICA · puntos 5, 6, 11, 18, 24, 25 · Spider-Man: Into/Across the Spider-Verse

Repaso corto (EQUIPO.md): la `biblia.md` ya tiene bien cubiertos los puntos 5
(§6 Tipografía), 6 (§7 Cómo hablan y piensan en pantalla) y 11 (§13
Videojuegos), hechos con la red **cerrada**. Los puntos **18, 24 y 25 no
existen** en la biblia: son el foco de esta parte. Abajo van confirmaciones y
ampliaciones para 5/6/11, y el material nuevo completo para 18/24/25, para que
el redactor los añada como secciones nuevas.

UNU = *Un nuevo universo* (2018). ATSV = *A través del Spider-Verso* (2023).

---

## Punto 5 · Tipografía — confirmaciones y ampliación

- **Letra de los cómics *Marvel 2099*** (biblia §6.1 lo dejó en ⚠️, «no lo
  pude abrir»): confirmado. La familia **Zephyr / Chariot** se usa para el
  número «2099» en los logos (el diseñador «quitó la línea que sube del
  contador del cero y lo puso en cursiva»); el cuerpo de texto usa
  **Eurostile** ✅ ([Fonts In Use](https://fontsinuse.com/uses/41204/marvel-2099-comic-books)).
  Los nombres de personaje van rotulados a mano, no tipografiados.
  **Letra libre parecida a Eurostile** (geométrica, cuadrada): **Michroma**
  (Cyreal, OFL, Google Fonts) — con tildes, ñ, ¿ y ¡ (comprobar con
  fontTools antes de usarla; no la bajé yo).
- Sigue sin resolverse cuál letra comercial exacta usa el **logo** de
  *Spider-Verse* (rotulación a medida, sin fuente comercial única) ⚠️: no
  encontré nada nuevo que lo desmienta ni lo confirme más que lo que ya
  tiene la biblia (dafont, Font In Logo).

## Punto 6 · Cómo hablan y piensan en pantalla — una confirmación importante

- **«With great power comes great responsibility»** (Tío Ben, UNU 00:01:33):
  la biblia lo tenía en ⚠️ («es el audio de las películas de Raimi»).
  **Confirmado con dos fuentes**: es el audio original de **Cliff
  Robertson** reciclado de *Spider-Man* (2002, Sam Raimi); el productor
  **Phil Lord** lo confirmó en entrevista ✅
  ([Gizmodo](https://gizmodo.com/into-the-spider-verse-lifted-a-key-line-of-dialogue-fro-1831360476),
  [CBR](https://www.cbr.com/into-spider-verse-raimi-spider-man-line/)).
  **Sube de ⚠️ a ✅** en biblia.md l.845.

## Punto 11 · Videojuegos de la franquicia — ampliación

- La biblia dice «no hay un juego de estas películas»: es cierto para un
  juego propio, pero **sí hay contenido jugable con Miles Morales/UNU** en
  juegos ya existentes, con **menús e interfaz propios** (no cajas de la
  película):
  - ***LEGO Marvel Super Heroes 2*** (TT Games, 2017): **Miles Morales**
    es personaje jugable (se desbloquea completando el nivel bonus «Poole
    Party» de Gwenpool) y trae **trajes de UNU** ✅
    ([LEGO Marvel Superheroes Wiki](https://lego-marvelsuperheroes.fandom.com/wiki/Spider-Man_(Miles_Morales)),
    [LEGO Games Wiki](https://legogames.fandom.com/wiki/Spider-Man_(Miles_Morales)/LM2)).
    Interfaz: los **menús y diálogos de LEGO Marvel** son las cajas de
    texto blancas típicas de LEGO, **no sirven de referencia** para la
    lámina. Imagen de tienda medida: `header.jpg` de Steam, **460×215 px**
    ([Steam](https://store.steampowered.com/app/460970/LEGO_Marvel_Super_Heroes_2/)).
  - ***Marvel Snap*** (temporada «Spider-Versus»): cartas con arte propio
    de personajes del Spider-Verse (Ghost-Spider/Gwen) y **cartas de
    localización con recuadro tipo viñeta de cómic** ✅
    ([Marvel.com](https://www.marvel.com/articles/games/marvel-snap-swings-into-new-season-spider-versus)).
    Su interfaz de carta (marco negro grueso, esquina con coste, texto en
    caja inferior) es un buen modelo de «ficha de personaje tipo cómic»
    para el foro, distinto de la caja amarilla de pensamiento.
  - ***Marvel Contest of Champions***: Spider-Gwen, Spider-Ham y Miles
    Morales como luchadores jugables, con sinergias de equipo «Spider-Verse»
    ✅ ([auntm.ai](https://auntm.ai/champions/spiderman)).
  - **The Cutting Room Floor**: no tiene página de Spider-Verse (no hay
    juego propio que desempaquetar) ⚠️ búsqueda hecha, sin resultado.
- **Nada de esto trae una caja de diálogo «de la película»**: confirma lo
  que ya decía la biblia — para el foro, la caja amarilla de pensamiento
  (§7) sigue siendo la referencia, no un HUD de videojuego.

---

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo (NUEVO)

### 18.1 Qué programas usó el estudio (Sony Pictures Imageworks)

- **Maya**: herramienta principal de animación, confirmado por animadores
  japoneses del equipo (「メインツールはMayaなのですが」) ✅
  ([CGWORLD, en japonés](https://cgworld.jp/interview/201904-spiderverse-01.html)).
- **Houdini**: gestiona con procedimientos (y una interfaz propia hecha con
  Python) que el dibujo a mano se ajuste encima de la animación en CG en
  vez de usar un mapa de textura fijo ✅
  ([CGSpectrum](https://www.cgspectrum.com/blog/spider-man-into-the-spider-verse-how-they-got-that-mind-blowing-look)).
  Elementos como humo, chispas y explosiones se dibujaron a mano encima
  ✅ (misma fuente).
- **Katana** (iluminación/look-dev) y **Mari** (texturizado): confirmados
  para ambas películas ✅ ([Foundry, Into](https://www.foundry.com/insights/film-tv/into-spiderverse),
  [Foundry, Across](https://www.foundry.com/insights/film-tv/across-the-spider-verse-nuke-mari-katana)).
- **Nuke**: compositing final, con **más de 25 herramientas propias**
  hechas por el equipo, entre ellas ✅ ([Foundry](https://www.foundry.com/insights/film-tv/graphic-look-in-comp-spiderman),
  [Foundry Across](https://www.foundry.com/insights/film-tv/across-the-spider-verse-nuke-mari-katana)):
  - **Hatcher** y **Thresher**: crean los puntos de trama (halftone) y las
    líneas de rayado (hatching) del «look impreso»; el tamaño, el ángulo y
    el espacio entre puntos se ajustan **a mano por plano** (Lead
    Compositor Geeta Basantani).
  - **ChromaShifter**: pensado primero para simular profundidad de campo
    por desfase de color; reutilizado para las estelas de movimiento.
  - **Brush Bomber** (nodo OSL en Katana, pasado a BlinkScript de Nuke y
    luego a C++): pinta 45 capas de pincel por fotograma.
  - **Kismet** (ATSV): sistema de tinta a mano que deja que las líneas de
    contorno **salgan del borde del objeto**, para que no se vean
    perfectas.
  - **PigmentMerge**: mezcla de color pensada para imitar el **desfase de
    impresión CMYK** (aditivo vs. sustractivo).
  - **MaskToInk**: convierte máscaras en «tinta mojada» que se puede
    esparcir según la humedad de la superficie.
  (Head of Compositing **Marco Recuay**, citado en ambos artículos de
  Foundry.)
- **Toon Boom Harmony**: el equipo de **FX 2D** (Sony Pictures Imageworks,
  responsable **Nikolaos Finizio**, con Slava Spiriannin, Quentin
  Cordonnier, Brice Maleo, Alex Alvarado Chavez y Brandon Louie) lo usó en
  ATSV para dibujar a mano: los tentáculos de tinta de **Spot**, el
  «sistema nervioso» de Miles cuando se electrifica, humo y explosiones
  (con línea distinta según el universo) y simulaciones de acuarela para
  Spot. Cambiaban entre **flujo de trabajo bitmap y vectorial** según el
  universo ✅ ([Toon Boom](https://www.toonboom.com/behind-the-amazing-2dfx-in-spider-man-across-the-spider-verse)).
- **Herramientas propias para «dibujar» sobre Maya** (equipo japonés,
  Atsuo Fujiwara, Hiroya Sonoda, Tatsuyuki Shimada y Earl Brawley): la
  **Incline tool** (líneas y arrugas a mano) y la **Pose Stamp tool**
  (estampa varios miembros/estelas), que convierten el trazo del lápiz en
  un objeto de Maya ✅ ([CGWORLD, japonés](https://cgworld.jp/interview/201904-spiderverse-01.html)).
  ATSV fue la primera película animada por ordenador con **equipo propio
  de entintado**, según befores & afters (ya citado en biblia §6.2).
- **Patente**: Sony pidió una patente en EE. UU. en diciembre de 2018 sobre
  el proceso de animación desarrollado para UNU ✅
  ([Deadline](https://deadline.com/2018/12/sony-gets-inventive-seeks-patents-for-spider-man-into-the-spider-verse-animation-tech-1202518373/),
  confirmado también en japonés por [CGWORLD](https://cgworld.jp/interview/202006-spi-danny.html)).
- **No usan Clip Studio Paint ni Blender** en la producción oficial (esos
  son para el fan-art y la réplica, ver 18.3).

### 18.2 Línea, sombreado, filtros y encuadre (para describirlo)

- **Línea**: contorno negro variable, con herramientas de tinta a mano
  (Kismet, Incline) que dejan que la línea **se salga del borde** y no sea
  perfecta ✅ (fuentes de 18.1).
- **Sombreado**: **plano por bandas** (varias franjas de color, no
  degradado suave) + **halftone** (puntos Ben-Day) en brillos/medios tonos
  + **rayado** (hatching) en sombras, con densidad ajustable por plano
  (Hatcher/Thresher) ✅. Confirma y amplía lo que la biblia ya medía en los
  repositorios de GitHub (§4.4).
- **Filtro de «desfase de impresión»** en vez de desenfoque de cámara: el
  equipo evitó el **blur de profundidad de campo tradicional** para no
  perder el aspecto ilustrado; en su lugar usan el desfase CMYK
  (PigmentMerge/ChromaShifter) ✅ ([Foundry](https://www.foundry.com/insights/film-tv/graphic-look-in-comp-spiderman)).
- **Encuadre y composición** (para las 3 láminas y para IA de imagen):
  - **Plano bajo** (contrapicado): empodera a Miles, marca su crecimiento.
  - **Plano alto** (picado): marca su vulnerabilidad y miedo (p. ej. al
    caer).
  - **Ángulo holandés** (dutch angle): su confianza creciente en escenas de
    acción.
  - **Pantalla partida** (split screen): dos personajes hablando a la vez,
    cada uno en su viñeta.
  - **Congelados** (freeze frames) y **profundidad de campo exagerada tipo
    viñeta**, para que el plano se sienta una página de cómic.
  ⚠️ (una sola fuente de análisis de cine, no es entrevista oficial del
  estudio): [lensviewing.com](https://lensviewing.com/camera-angle-shots-in-into-the-spiderverse/);
  lo mismo describen dos vídeo-ensayos de YouTube, **"Spider-Verse:
  Cinematography of an Animated Masterpiece"**
  (https://www.youtube.com/watch?v=2zjp7-S8mX0) y **"The Cinematography of
  Spider-Man: Into The Spider-verse"**
  (https://www.youtube.com/watch?v=dwcf-HftAnw).
  El propio estudio sí confirma la parte de la cámara: probaron un **array
  de cámaras** que proyecta 7 ángulos a la vez, cada uno renderizado con un
  estilo distinto, y jugaron con **destellos de lente (lens flare)**
  distintos según el mundo (2099 vs. India) ✅ ([Foundry](https://www.foundry.com/insights/film-tv/graphic-look-in-comp-spiderman)).

### 18.3 Cómo reproducirlo — Blender (fan, no oficial)

No hay complemento (*add-on*) libre ya hecho: se monta el árbol de nodos a
mano. Receta más completa que encontré, paso a paso ✅ (coincide en varias
fuentes independientes):

1. **Sombreado por bandas**: nodo `Shader to RGB` → `ColorRamp` (controla
   cuántas bandas de luz/sombra tiene el material).
2. **Halftone en brillos**: `Voronoi Texture` en modo **Smooth F1**,
   `Randomness` en 0 (da los puntos regulares); `Texture Coordinate` →
   `Mapping` para el tamaño de los puntos; se multiplica con la máscara de
   brillo del paso 1.
3. **Rayado (hatching) en sombras**: `Wave Texture` rotado, con su propia
   máscara (la de sombra, invertida); se suma con el halftone del paso 2.
4. Agrupar todo con `Ctrl+G` (Node Group) para reusarlo en varios
   materiales.
5. **Contorno**: activar **Freestyle** (Render Properties → Freestyle;
   View Layer Properties → Freestyle → Line Set) y ajustar grosor; es la
   alternativa que pide el encargo a Solidify con normales invertidas.
6. **Aberración cromática / desfase de impresión** (en el compositor):
   `Separate RGBA` → `Combine RGBA`, con nodos `Translate` que desplazan
   los canales rojo y verde en el eje X uno o dos píxeles.
   Fuente completa, paso a paso: **Amiel**, en
   [GarageFarm](https://garagefarm.net/blog/recreating-the-spider-verse-look-in-the-blender-node-editor)
   y [CGTrader](https://www.cgtrader.com/tutorials/7012-recreating-the-spider-verse-look-in-the-blender-node-editor)
   ✅. Coincide con [BlenderNation, «7 steps»](https://www.blendernation.com/2024/01/15/7-steps-to-make-a-spiderverse-shader-in-blender/)
   y el vídeo [«Spider-verse Style / Comic Shader in Blender»](https://www.youtube.com/watch?v=xzz52hX5rzk).
   Curso pagado con el mismo enfoque: [Digital Creator School](https://courses.digitalcreatorschool.com/courses/create-a-spider-verse-halftone-shader).
- Modelos/rigs libres: no encontré un rig con licencia libre de Miles,
  Gwen o Hobie (ni en Sketchfab ni en GitHub) ⚠️; sí hay los objetos y
  efectos ya listados en biblia §4.1-4.4 (Sketchfab CC, shaders MIT/sin
  licencia para sólo mirar).

### 18.4 Cómo reproducirlo — Photoshop

- **Semitono de color** (*Color Halftone*, Filtro → Pixelar): funciona
  mejor en **modo CMYK**; cada canal (C, M, Y, K) tiene su propio **ángulo
  de pantalla** (*screen angle*), que es lo que da la trama real de
  imprenta, no un patrón de puntos genérico ✅
  ([Photoshop Essentials](https://www.photoshopessentials.com/photo-effects/get-better-color-halftone-effects-in-photoshop/),
  [Academy Class](https://www.academyclass.com/blog/colour-halftones-in-photoshop/)).
- **Desfase de impresión** (misregistration): aplicar el halftone a los
  canales C, M, Y por separado y mover cada uno 1-3 px con la herramienta
  Mover; para no perder legibilidad, se hace sobre una copia y se
  enmascara sólo en los bordes y detalles clave, no en toda la imagen ✅
  (mismas fuentes).
- **Capas**: base CG o dibujo plano abajo; encima, una capa de **grano de
  papel** en modo Superponer/Multiplicar con opacidad baja; el rayado de
  sombras con un set de pinceles de trama (hay sets gratis en
  [Brusheezy](https://www.brusheezy.com/free/spiderman) y
  [Pixelbuddha](https://pixelbuddha.net/effects/halftone-effects-photoshop),
  licencia de cada set a comprobar antes de usar) ⚠️ (sets de fans, sin
  licencia clara caso por caso).
- Esto complementa (no repite) la paleta y las texturas reales que ya
  midió el investigador de imagen en biblia §4-5.

---

## Punto 24 · Obras parecidas y temas relacionados (NUEVO)

### 24.1 Influencias de cómic que citan los propios directores

Lista con la influencia de cada autor, confirmada en una nota técnica ✅
([CBR](https://www.cbr.com/across-the-spider-verse-comics-artists-influence/)):

| Autor | Qué influencia |
|---|---|
| **Steve Ditko** (co-creador de Spider-Man) | el traje rojo/azul original, desde 1962 |
| **John Romita Sr.** | la máscara icónica, «la cara de Marvel» en merchandising |
| **Gil Kane** | trazo fino en primeros planos («La noche que murió Gwen Stacy») |
| **Jim Steranko** (*Nick Fury*) | collage y tipografías experimentales — muy cerca del estilo de **Hobie** |
| **Bill Sienkiewicz** | expresionismo y color casi abstracto |
| **Paul Pope** (*THB*) | estética cyberpunk — cerca de **Miguel/2099** |
| **Moebius** (Jean Giraud) | arquitectura futurista detallada — Tierra-928 |
| **Alex Ross** (*Marvels*) | fondos pintados en acuarela — cerca del mundo de **Gwen** |
| **J. Scott Campbell** | diseño facial redondeado, ojos grandes |
| **Sara Pichelli** | co-creadora de Miles Morales; detalle externo para mostrar lo que siente el personaje |

- **Universo «Kirbyverse» descartado**: el diseñador de producción
  **Aymeric Kevin** enseñó en Twitter bocetos de un universo con estética
  de **Jack Kirby** (nave espacial, ambientes) que no llegó a salir en la
  película; «no están ligados a ningún momento de la historia, es un
  estudio visual de cómo se vería el mundo» ✅
  ([ComicBook.com](https://comicbook.com/movies/news/spider-man-across-the-spider-verse-jack-kirby-universe/)).

### 24.2 Influencias del anime — sólo en fuente japonesa (no traducida)

Entrevista a los directores y el productor, en japonés, sin traducción
encontrada en otro idioma ✅ ([Fan's Voice](https://fansvoice.jp/2019/05/14/spiderman-spiderverse-interview/)):

- **Hayao Miyazaki**: el director **Bob Persichetti** dice que todo el
  equipo es fan suyo y que marcó «el tono general de la película y su
  aspecto visual».
- ***AKIRA* (Katsuhiro Otomo)**: el director **Peter Ramsey** dice que
  tuvo «mucha influencia», «hay elementos de *AKIRA*, seguro».
- **Satoshi Kon** (*Tokyo Godfathers*, *Paprika*): citado como influencia.
- ***Sailor Moon***: usado como referencia al diseñar a **Peni Parker**.
- El equipo japonés de animadores (8 personas en Imageworks, ver 18.1)
  metió técnicas de anime en la producción ✅ ([CGWORLD](https://cgworld.jp/interview/201904-spiderverse-01.html)).

### 24.3 Obras que citan a Spider-Verse como influencia después (2021-2023)

- ***The Mitchells vs. the Machines*** (Sony, 2021): reutilizó la
  tecnología de Spider-Verse para su estilo «acuarela pintada a mano» ✅
  ([Collider](https://collider.com/movies-similar-animation-spider-man-across-the-spider-verse/)).
- ***Puss in Boots: The Last Wish*** (DreamWorks, 2022): mezcla 2D/3D con
  aspecto de libro de cuentos ilustrado, inspirado en Spider-Verse ✅
  (misma fuente).
- ***Teenage Mutant Ninja Turtles: Mutant Mayhem*** (2023): estilo
  «boceto» híbrido 2D/3D, siguiendo la tendencia que abrió Spider-Verse ✅
  (misma fuente). Hay una segunda lista larga (25 títulos) en
  [Collider](https://collider.com/best-animated-movies-like-spider-man-across-the-spider-verse/),
  de valor desigual ⚠️ (listado editorial, sin cita de los estudios).

### 24.4 Tema parecido en el propio Spider-Man

- El argumento de UNU se parece al de los **dos últimos episodios de
  *Spider-Man: The Animated Series*** (1990s): Kingpin construye una
  máquina para acceder a otras realidades, y varios Spider-Man de
  universos alternos se unen para pararlo ⚠️ (una sola fuente, wiki de
  fans: [TV Tropes, Mythology Gag](https://tvtropes.org/pmwiki/pmwiki.php/MythologyGag/SpiderManIntoTheSpiderVerse)).
- Páginas de **TV Tropes** de la propia película (para el redactor, si
  hace falta un tropo concreto):
  [WesternAnimation/SpiderManIntoTheSpiderVerse](https://tvtropes.org/pmwiki/pmwiki.php/WesternAnimation/SpiderManIntoTheSpiderVerse),
  [TearJerker](https://tvtropes.org/pmwiki/pmwiki.php/TearJerker/SpiderManIntoTheSpiderVerse) (cruza con punto 21, de voz).

### 24.5 Qué otra lámina del servidor se le parece (para no repetir ideas)

- **Arcane** (encargo 17, `biblias/17-arcane/biblia.md`): también pinta a
  mano encima de un render 3D («pintura digital con aspecto de óleo sobre
  3D», §2.2 y §12 de esa biblia) y usa el **grafiti/pintura en pared** como
  cuadro de diálogo de Jinx. **Es la más parecida técnicamente** de las
  biblias hechas hasta ahora. Para no repetir: si Arcane ya usa «grafiti en
  la pared» como cuadro de texto, la lámina de Spider-Verse debería situar
  el grafiti de Miles en un **objeto distinto** (una pegatina, una libreta,
  una página de cómic), no una pared pintada — ver conceptos de lámina en
  biblia §19, ya lo evitan sin saberlo (proponen el túnel del grafiti con
  **pegatinas**, no un muro liso).
- No encontré ninguna otra biblia ya hecha (01-20) con un cuadro de diálogo
  tipo cómic o manga superpuesto en pintura; el resto usa diseño de
  interfaz de juego, pergamino o letrero, distintos de la caja amarilla de
  Spider-Verse.

---

## Punto 25 · El mundo, la historia y sus símbolos (NUEVO)

### 25.1 Las reglas del mundo, en 5 líneas

1. El multiverso está hecho de **Tierras numeradas** (Earth-1610 Miles,
   Earth-65 Gwen, Earth-928 Miguel/2099, Earth-138 Hobie, Earth-90214 Peter
   B. Noir, Earth-616 el «canon» de los cómics…) ✅ (ya usado en biblia
   §4).
2. Cualquiera que reciba el poder de una araña (radiactiva o mística) se
   vuelve un **«Spider-Totem»** (o «arácno-humanoide»); casi siempre es un
   chico llamado Peter Parker, pero no siempre ✅
   ([Fandom, Spider-Totems](https://intothespiderverse.fandom.com/wiki/Spider-Totems)).
3. Cada Spider-Person tiene **«eventos canónicos»** (*canon events*): nodos
   fijos de la llamada **«Red de la Vida y el Destino»** (*Web of Life and
   Destiny*) que tienen que pasar en (casi) todos los universos —incluida
   la muerte de alguien cercano al empezar a ser héroe— o el universo se
   desestabiliza y puede colapsar el multiverso entero ✅
   ([Fandom, Canon Events](https://intothespiderverse.fandom.com/wiki/Canon_Events),
   [ScreenRant](https://screenrant.com/spider-man-spider-verse-canon-events-explained/)).
4. Pasar demasiado tiempo fuera de tu universo hace que **«glitchees»**
   (te descompones en fragmentos, y duele); el reloj de viaje evita el
   glitch mientras lo llevas puesto (ya en biblia §7).
5. La **Spider-Society**, fundada por **Miguel O'Hara** con su IA **Lyla**,
   vigila que nadie rompa un evento canónico; su sede está en Nueva
   York-928 (año 2099) (ya en biblia §4/§7-8).

### 25.2 La historia por arcos, con sus momentos clave

- **UNU (2018)**: Wilson Fisk (Kingpin) hace que **Alchemax** construya un
  **supercolisionador** en Brooklyn para traer de otra dimensión a su
  esposa e hijo muertos. El experimento arrastra a **Peter B. Parker** (y
  otras arañas) al universo de **Miles Morales**; el Peter original de
  Miles muere a manos de Kingpin. Miles aprende a ser Spider-Man con la
  ayuda de los visitantes, cierra el colisionador y derrota a Kingpin.
  Termina presentándose como el Spider-Man de su universo ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Spider-Man:_Into_the_Spider-Verse)).
- **ATSV (2023) — acto 1**: Gwen (Earth-65) vive aislada, perseguida por su
  padre policía; Miles hace equilibrio entre su vida y ser Spider-Man;
  aparece **el Spot** (Jonathan Ohnn, ex-científico de Alchemax con
  agujeros interdimensionales), buscando venganza.
  **Acto 2**: Miles y Gwen reclutan a **Spider-Man India** (Pavitr) y
  **Spider-Punk** (Hobie); llegan a Nueva York-928, sede de la
  Spider-Society; Miguel explica los eventos canónicos, incluida la muerte
  del padre policía de Miles.
  **Acto 3**: Miles se niega a aceptar esa muerte como «necesaria»; Miguel
  lo encierra; escapa con ayuda de Hobie y Spider-Byte; Miguel revela que
  la araña que picó a Miles venía del **Earth-42**, y que Miles «no debía»
  ser Spider-Man. Miles cae al Earth-42: su tío Aaron sigue vivo ahí y es
  el Prowler de ese mundo, junto a un Miles Morales alterno **vuelto
  villano**. Gwen es expulsada de la Sociedad. Termina en cliffhanger ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Spider-Man:_Across_the_Spider-Verse)).
- **Beyond the Spider-Verse**: tercera película, «parte 3 de una historia
  en 3 actos». Estreno confirmado para el **25 de junio de 2027**
  (aplazada varias veces desde 2024, primero por la huelga de guionistas y
  actores de 2023) ✅ ([Hollywood Reporter](https://www.hollywoodreporter.com/movies/movie-news/spider-man-beyond-the-spider-verse-release-1236320001/),
  [Variety AU](https://au.variety.com/2025/film/news/spider-man-beyond-the-spider-verse-release-date-june-2027-25333/)).

### 25.3 Emblemas, logos y objetos icónicos

- **Alchemax**: la corporación-villano institucional de la saga; aparece
  en varios universos (Earth-1610 dirigida por Fisk; también Earth-616 y
  Earth-50101) ✅ ([Fandom, Alchemax](https://intothespiderverse.fandom.com/wiki/Alchemax_(Earth-1610))).
  Buen candidato a **logo corporativo** de fondo (carteles, pantallas) en
  escenas de Brooklyn o de 2099.
- **El reloj/gadget multiversal** («Multiversal Gizmo» / «Web-Watch»),
  creado por la IA Lyla: lo llevan todos los miembros de la Spider-Society
  en el brazo izquierdo; evita el glitch y sirve de vigilancia ✅
  ([Fandom, Multiversal Gizmo](https://intothespiderverse.fandom.com/wiki/Multiversal_Gizmo),
  [Fandom, Web-Watch](https://intothespiderverse.fandom.com/wiki/Web-Watch)).
- **El Prowler (Earth-42)**: rediseño de ATSV para el Earth-42, «estilo
  casero, con ayuda de ingeniería del tío Aaron». Hubo varios diseños
  descartados —colores rosa, morado, rojo y verde; símbolos pintados con
  espray; garras de formas distintas— revelados por el diseñador de
  personajes **Kris Anka** (uno de ellos de **Evan Monteiro**) ✅
  ([The Direct](https://thedirect.com/article/spider-verse-2-miles-morales-prowler-designs-rejected-photos)).
  Cruza con biblia §4 (Kris Anka ya está citado ahí como diseñador de
  personajes de ATSV).
- **El «Kirbyverse» descartado** (ver 24.1): bocetos de un universo entero
  con estética Kirby que no llegó a la película final.

### 25.4 Vocabulario propio que un fan reconoce al instante

- **«Canon event»** (evento canónico) — ya en biblia como meme de 2023.
- **«Web of Life and Destiny»** (Red de la Vida y el Destino) — el nombre
  oficial de la estructura que conecta todos los universos ✅ (Fandom,
  ScreenRant, ver 25.1).
- **«Spider-Totem»** / «arácno-humanoide» ✅ (Fandom).
- **«Glitching»** (glitchear) — ya en biblia.
- **«Spider-Society»**, **«Multiversal Gizmo» / «Web-Watch»**, **«Alchemax»**
  — nuevos en esta parte, ver arriba.
- **«Anyone can wear the mask»** — ya está en biblia (§8/§14); no repetir,
  sólo enlazar con la idea de «Web of Life and Destiny»: el mensaje del
  multiverso es que la máscara **puede ser de cualquiera**, pero el
  universo **exige** que alguien la lleve (tensión entre los dos temas,
  útil para el redactor si conecta puntos 6 y 25).
- **«With great power comes great responsibility»** — confirmado en el
  punto 6 de esta parte que el audio es el reciclado de Raimi (2002).

---

## Lo mejor para la lámina

1. **Punto 18 (Blender)**: la receta de nodos de Amiel (Shader to RGB +
   Voronoi Smooth F1 + Wave Texture + Freestyle + Translate en compositor)
   es la más concreta que hay para que quien monte la lámina en Blender
   reproduzca el halftone y el rayado sin inventar.
2. **Punto 18 (Photoshop)**: Semitono de color en modo CMYK, con
   desplazamiento de canal a canal, es el método real de imprenta que
   describe el propio encargo («desfase de impresión»): más fiel que un
   filtro de aberración cromática genérico.
3. **Punto 24**: Jim Steranko como influencia confirmada por el estudio
   encaja perfecto con el **collage de Hobie** (letras recortadas,
   fanzine punk) que ya propone el concepto de lámina 3 de la biblia.
4. **Punto 25**: la **Red de la Vida y el Destino** y los **eventos
   canónicos** son el concepto de mundo más citado por el fandom después
   de «anyone can wear the mask»; sirve de texto corto para una cartela de
   «reglas del multiverso» en cualquiera de los 3 conceptos.
5. **Punto 25**: el reloj/Web-Watch (objeto pequeño, en la muñeca) es un
   buen «objeto real» adicional para una lámina 2 sobre normas del canal,
   si hace falta.

## No encontré ⚠️

- **Nombre comercial exacto del logo de Spider-Verse** (punto 5): sigue sin
  resolverse; busqué «Spider-Verse font identified», «Spider-Verse logo
  typeface -dafont» en inglés, nada nuevo sobre lo que ya tenía la biblia.
- **Rig o modelo 3D libre** de Miles, Gwen o Hobie con licencia CC
  (Sketchfab, búsqueda «Miles Morales rig free download», «Spider-Gwen
  model CC0»): no hay ninguno con licencia clara, sólo modelos de pago o
  sin licencia — esto es un **extra** del punto 18 (el encargo pide
  «modelos y rigs libres» como parte de la receta de Blender, ya lo cubre
  §18.3 diciendo que no encontré ninguno).
- **The Cutting Room Floor**: no tiene ficha de Spider-Verse (no hay un
  juego propio que desempaquetar); comprobado con su buscador (dio 403 por
  Cloudflare al segundo intento, no insistí más).
- **Interfaz de un juego oficial de las películas** (punto 11): no existe;
  ya lo decía la biblia y lo confirmo con más juegos mirados (LEGO Marvel
  2, Marvel Snap, Contest of Champions): ninguno tiene una caja «de la
  película».

## Bitácora de búsqueda (esta parte)

- **Inglés** (WebSearch + WebFetch): «Spider-Verse animators hand-paint
  texture CG frames», «Spider-Verse custom line render tool interview»,
  «recreate Spider-Verse shader Blender tutorial halftone Freestyle»,
  «Spider-Verse camera lens flare hand-drawn compositing Nuke», «Spider-Verse
  Hobie frame rate TVPaint interview», «Spider-Verse cinematography
  composition analysis», «Photoshop brush texture paint Spider-Verse comic
  style», «movies influenced by Spider-Verse visual style», «Spider-Verse
  directors influences Ditko Kirby», «Beyond the Spider-Verse release date
  2027», «Spider-Verse canon event rules explained», «Spider-Society badge
  emblem watch device», «LEGO Marvel Super Heroes 2 Spider-Verse DLC»,
  «Prowler emblem symbol design Aaron Davis», «TV Tropes Spider-Man Into
  the Spider-Verse», «Photoshop Color Halftone CMYK misregistration
  tutorial», «Marvel Contest of Champions Marvel Snap Spider-Verse cards».
  Fuentes: Foundry (×2), CGSpectrum, Toon Boom, CBR (×2), ComicBook.com,
  Deadline, Gizmodo, Collider (×2), Hollywood Reporter, Variety AU,
  thedirect.com, Fandom (Spider-Totems, Canon Events, Alchemax,
  Multiversal Gizmo, Web-Watch), Wikipedia (ambas películas), TV Tropes,
  Steam, LEGO wikis, Marvel.com, auntm.ai, Photoshop Essentials, Academy
  Class, GarageFarm/CGTrader, BlenderNation.
- **Japonés**: 「スパイダーバース 作画 技法 アニメーション インタビュー」
  (CGWORLD, dos entrevistas) y 「日本アニメからの影響」ya venía en el
  resultado de Fan's Voice. Da datos **no traducidos** a otro idioma:
  herramientas Incline/Pose Stamp, Maya como programa principal, y las
  influencias directas de Miyazaki, *AKIRA*/Otomo, Satoshi Kon y *Sailor
  Moon* que dieron los propios directores.
- **Coreano**: 「스파이더맨 스파이더버스 세계관 정경 원칙 나무위키」 — sólo
  confirma en general el concepto de Spider-Totem como «cosmovisión
  mitológica»; no aportó datos nuevos que no tuviera ya la wiki en inglés,
  no lo cito como fuente aparte.
- **Wiki de Fandom directa** (`intothespiderverse.fandom.com/api.php`):
  búsqueda de texto «spider emblem symbol design» y «Alchemax»; página
  completa de Spider-Totems y Alchemax (Earth-1610) por wikitext.
- **Bloqueado**: The Cutting Room Floor (403 Cloudflare al buscar
  «Spider-Verse», un solo intento más de comprobación, no insistí).
- Medí con Pillow el `header.jpg` de la tienda de Steam de *LEGO Marvel
  Super Heroes 2*: 460×215 px.
