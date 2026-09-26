# Parte del investigador de TEXTO, JUEGOS Y TÉCNICA · SpongeBob (Bob Esponja)

Puntos de `ENCARGO.md`: **5** (tipografía), **6** (cuadros de diálogo en pantalla),
**11** (videojuegos), **18** (estilo de dibujo y técnica, cómo replicarlo),
**24** (obras parecidas) y **25** (el mundo, la historia y sus símbolos).

Es una **segunda pasada**: `biblia.md` ya tiene mucho de los puntos 5, 6 y 11
(hecha el 24-sep-2026 con la red cerrada, sección «Tipografía» l.387,
«Cómo hablan y piensan en pantalla» l.423, «Videojuegos de la franquicia»
l.755). Aquí **confirmo con la red abierta** lo que ya había y añado lo que
falta, y dejo **enteros** los puntos 18, 24 y 25, que la biblia no tenía.
Parto de `partes/datos-texto.md` (sólo capturas de Steam de un juego; el resto
lo busqué yo) y no repito lo que ya está ✅ en `biblia.md` salvo para sumar
una segunda fuente o corregirlo.

Formato: un dato por línea, con fuente(s) y ✅ (dos fuentes o comprobado por
mí) / ⚠️ (una fuente o dudoso).

---

## Hallazgos

### Punto 5 · Tipografía — confirmado con la red abierta

- **Ya no dan 403**: `1001fonts.com`, `dafont.com` y `fontmeme.com` (antes
  bloqueados, según la bitácora de `biblia.md` §21). No cambian los datos que
  ya había, pero ahora se pueden enlazar y comprobar de verdad, no de memoria.
- **Comprobé yo mismo con fontTools** la letra **Some Time Later** (la de las
  tarjetas del Narrador Francés, ya en la biblia como ✅): descargué el
  archivo real de [Jordy3D/Jordy3D.github.io](https://github.com/Jordy3D/Jordy3D.github.io/raw/master/projects/sometimelater/Some%20Time%20Later.otf)
  y con `TTFont(f).getBestCmap()` confirmé **los 14 caracteres** (á é í ó ú Á
  É Í Ó Ú ñ Ñ ¿ ¡) presentes, de **1177 glifos** en total. También leí los
  campos `name` del propio archivo: dice **«This Font Software is licensed
  under the SIL Open Font License, Version 1.1»** (copyright 2016-2020,
  Fredrick R. Brennan) ✅✅ doble confirmación (dato antiguo + comprobación
  mía directa, no de memoria).
- **Letra de los cómics de la franquicia (SpongeBob Comics, Papercutz/United
  Plankton Pictures)**: no encontré qué letra usa el rotulado real. Sólo hay
  generadores de efecto de texto (textstudio.com, fontspace.com) que imitan
  el logo, no el rotulado de los globos de los cómics ⚠️. Lo más parecido a
  una convención real de rotulado de cómics estadounidense son familias tipo
  Blambot/Actor, pero no until confirmado para esta franquicia: **no lo
  encontré**, lo digo así en vez de inventarlo.

### Punto 6 · Cómo hablan y piensan en pantalla — un cuadro nuevo: la interfaz de los juegos

- La biblia ya cubre bien las tarjetas de tiempo, el menú, los carteles y el
  botón de Calamardo (§7 de `biblia.md`). Lo que faltaba es **cómo se rotula
  el texto en los videojuegos**, que es del punto 6 tanto como del 11 (ver
  abajo, «Punto 11»): en *Battle for Bikini Bottom Rehydrated* los avisos en
  pantalla mezclan **iconos de botón dentro del texto**, con una etiqueta de
  formato enriquecido: `<GameCmd>Press</GameCmd> <img id="R1_Button"/>
  <GameCmd>to travel to the Spongeball Arena</GameCmd>` ✅ (visto en el texto
  descartado del juego, [The Cutting Room Floor](https://tcrf.net/SpongeBob_SquarePants:_Battle_for_Bikini_Bottom_Rehydrated),
  archivo `Game.locres`, vía [Wayback Machine](https://web.archive.org/web/20260911094445/https://tcrf.net/SpongeBob_SquarePants:_Battle_for_Bikini_Bottom_Rehydrated)
  porque tcrf.net da 403 en directo). Es un **patrón replicable**: icono del
  botón incrustado en la frase, no una instrucción aparte.

### Punto 11 · Videojuegos de la franquicia — profundizado

- ***Battle for Bikini Bottom – Rehydrated* corre sobre Unreal Engine** ✅:
  lo confirman dos huellas técnicas en sus archivos descartados ([TCRF](https://web.archive.org/web/20260911094445/https://tcrf.net/SpongeBob_SquarePants:_Battle_for_Bikini_Bottom_Rehydrated)):
  la ruta `Engine/Content/SlateDebug/Fonts/LastResort.tps` (Slate es el
  sistema de interfaz de Unreal) y los archivos `Game.locres` (formato de
  localización propio de Unreal). El **nombre interno del proyecto era
  «Pineapple»** (se ve en las rutas `Pineapple/Binaries/Win64/…`) ⚠️ una sola
  fuente (TCRF), pero es un dato técnico verificable en los propios archivos.
- **Vi las capturas 1920×1080 de *Bob Esponja: El juego de Patricio Estrella***
  (2024, PHL Collective, ya en `datos-texto.md`, [Steam](https://store.steampowered.com/app/2322380))
  ✅ visto por mí:
  - La casa piña y la roca de Patricio en 3D **mantienen el contorno negro
    grueso** típico del 2D, aunque el render es en tiempo real: es un
    *toon shading* con línea, no un 3D realista con textura de dibujo
    encima.
  - Las **nubes-flor** (§18 abajo) se repiten como formas de línea sueltas
    flotando en el cielo, sin relleno: un motivo gráfico 2D metido dentro
    de una escena 3D.
  - Ventanas redondas tipo **portillo de barco** (con remaches) en las
    casas: coherente con «mantener todo náutico» (§18).
  - En *Glove World!* los colores son **muy saturados** (magenta, amarillo
    canario, cian), con más contorno negro en cada objeto del parque.
- ***SpongeBob: Krusty Cook-Off* (Tilting Point, móvil)**: no encontré
  capturas directas de su interfaz que pudiera abrir (Dribbble y el estudio
  [PUNCHev Group](https://punchev.com/cases/spongebob-krusty-cook-off-contributing-to-the-magic-of-deep-sea-cooking)
  dicen haber hecho su UI, y un consultor de UX, [Christopher Furniss](https://cargocollective.com/chrisfurniss/filter/ui/Spongebob-Squarepants-Krusty-Cookoff),
  dice haber evaluado su navegación y su tienda de compras dentro de la app)
  ⚠️ confirma que el juego SÍ tiene un estudio de interfaz detrás, pero no
  pude ver ni describir sus pantallas.
- **Modelos y *rigs* 3D libres del personaje, con licencia comprobada por la
  API de Sketchfab** (`api.sketchfab.com/v3/search?type=models&q=spongebob+rig&downloadable=true`),
  no sólo por la búsqueda como en la biblia:
  - [«Spongebob Rig»](https://sketchfab.com/3d-models/spongebob-rig-5009dc11dd1f45d3ac8dda79b06e09db)
    de **FreeModeler12345** — licencia **CC Attribution**, descargable ✅
    (campo `license.label` de la propia API, no de la búsqueda). Aviso del
    propio autor: los dedos y casi toda la cara **no están riggeados**.
  - [«Battle for bikini bottom SpongeBob Rig»](https://sketchfab.com/3d-models/none-e0848f57d5074f9daf90d9b7817ce098) —
    también CC Attribution por la API, pero **sacado directamente del juego**
    *Rehydrated* (como el de la caja registradora que ya está en la biblia):
    mirar, no usar como si fuera libre de origen.
- **Game UI Database (ficha de *Rehydrated*, id 1490)**: sigue **sin poderse
  ver**. Ni en directo (403) ni por Wayback Machine: la copia archivada es
  sólo el **armazón vacío de la app** (los filtros de búsqueda del sitio,
  sin los datos concretos del juego, porque es una aplicación de una sola
  página que carga los datos por JavaScript después) ⚠️ **no lo encontré**,
  con dos intentos (directo y Wayback).

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo (punto entero, nuevo)

#### 18.1 Cómo se anima, por etapas ✅ (Wikipedia, con las fuentes primarias detrás)

| Etapa | Técnica | Fuente primaria |
|---|---|---|
| Temporada 1 (1999-2000) | **Animación en cel tradicional**, tinta a mano. El Smithsonian conserva cels originales de la serie. | [Smithsonian: cel de producción de SpongeBob SquarePants](https://www.si.edu/object/animation-cel-used-production-spongebob-squarepants:nmah_1888673) |
| Temporada 2 en adelante (2000) | Cambio a **«digital ink and paint»**: se sigue dibujando a mano en papel, pero el entintado y coloreado se hace en ordenador. | Entrevista a Paul Tibbitt, [Digital Spy, 3-abr-2011](https://web.archive.org/web/20131031235346/http://www.digitalspy.co.uk/tv/interviews/a312387/paul-tibbitt-spongebob-squarepants.html) |
| *The SpongeBob SquarePants Movie* (2004) | El entintado y coloreado digital lo hizo el estudio **USAnimation** ⚠️ confirmado sólo para la película, no para la serie de televisión. | búsqueda propia, ficha de USAnimation |
| Temporada 5, ep. «Pest of the West» (2008) en adelante | El equipo empieza a usar **tabletas de dibujo** (para corregir al momento sin rehacer el papel). La diseñadora de fondos **Kenny Pittenger** cuenta que a varios compañeros no les gustaban, preferían el papel. | [Tom Heintjes, «The Oral History of SpongeBob SquarePants», Hogan's Alley, 21-sep-2012](https://web.archive.org/web/20150831044034/http://cartoonician.com/the-oral-history-of-spongebob-squarepants/) |
| Desde 2004, episodios especiales | Colaboración con el estudio **Screen Novelties** para secuencias en **stop-motion / claymation** (clímax de la película de 2004, cabecera del especial del 10.º aniversario en 2009, un especial entero «It's a SpongeBob Christmas!» en 2011 con muñecos inspirados en Rankin/Bass, y un especial de Halloween en la temporada 11). Usaron materiales «no convencionales»: bicarbonato, purpurina, virutas de madera y cereal de desayuno para los decorados. | [Animation Magazine, 21-nov-2012](http://www.animationmagazine.net/tv/stop-motion-casts-a-spell-on-spongebob/); [Cartoon Brew, 6-nov-2012](http://www.cartoonbrew.com/stop-motion/its-a-spongebob-stop-mo-christmas-72872.html); [Animation World Network, 5-dic-2012](http://www.awn.com/animationworld/stop-motion-spongebob-special-means-christmas-comes-early-year) |

> ✅✅ Todo lo anterior sale del **wikitexto con notas al pie** de la ficha
> en inglés de Wikipedia (no del resumen del artículo): cada dato tiene su
> fuente primaria de prensa especializada de animación, comprobada por mí
> siguiendo el enlace.

#### 18.2 Cómo se pintan los fondos ✅✅ (dos fuentes independientes de la misma artista)

- **Gouache sobre papel**, escaneado, y **la línea y el retoque se dibujan
  encima en digital**. Dirección de arte de **Peter Bennett** y **Shane
  Richardson** ✅✅: lo dice la propia fondista [Amy Lewis en su
  portafolio](https://www.amylewisart.com/spongebob) («Traditionally
  painted backgrounds for SpongeBob Squarepants. Gouache on paper. Line and
  editing drawn digitally on top») y también en su
  [publicación en X/Twitter](https://x.com/AmyLewis_Art/status/1728845656956309884),
  con ejemplos de fondos reales.
- Otro fondista, **April Borchelt**, tiene fondos pintados de la serie en su
  portafolio de ArtStation: [«BG for Spongebob Squarepants»](https://www.artstation.com/artwork/aRYBz8)
  ⚠️ una fuente, pero confirma que **varios artistas** pintaban fondos con la
  misma técnica (gouache + línea digital encima), no fue un caso aislado.

#### 18.3 Elementos de diseño que no cambian ✅

- **Todo tiene que verse «náutico»**: cuerdas, tablones, timones de barco,
  redes, anclas, remaches (según el diseñador de fondos Kenny Pittenger).
- **Nubes-flor** en el cielo, con la misma función que las nubes normales,
  pensadas para parecer una **camisa hawaiana floreada**.
- **Arena con motas de pintura** y **rocas de coral moradas**: texturas
  reconocibles a simple vista, ya vistas también en las capturas de
  videojuegos (§11).
- Las formas de los personajes son **geometría simple**: el cuerpo cuadrado
  de Bob Esponja «une su personalidad nerd con el atractivo visual» (fuente:
  análisis de diseño de personajes, [exresearch.co](https://www.exresearch.co/behind-the-art-of-spongebob/)
  ⚠️ una fuente, pero coincide con lo que se ve en cualquier fotograma).
- Fuente de todo el bloque: [Wikipedia (en), sección «Animation»/«Setting»](https://en.wikipedia.org/wiki/SpongeBob_SquarePants),
  con la nota al pie que remite a la misma entrevista de Hogan's Alley
  (§18.1) ✅✅.

#### 18.4 Cómo reproducirlo en Photoshop

- **Fondos**: pintar (o usar pinceles con textura de gouache/papel) en capa
  «pintura», con formas simples y algo de veta de pincel visible; encima,
  una capa de **línea limpia digital** con un pincel redondo duro de grosor
  poco variable (así se ve el «fondo pintado + línea encima» real de la
  serie, no un dibujo digital liso de principio a fin).
- **Personajes**: color **plano**, sin degradado (salvo alguna sombra dura de
  un solo tono, sin difuminar), contorno negro grueso y uniforme.
- **Motivo flor**: una forma de línea suelta (sin relleno) se puede pegar
  encima de cualquier fondo como «nube» o adorno, tal como se ve en los
  videojuegos (§11).

#### 18.5 Cómo reproducirlo en Blender (para el objeto 3D de la lámina, la caja registradora)

- El contorno negro grueso que se ve incluso en los juegos 3D (§11) se logra
  con la técnica clásica de **«inverted hull»**: un modificador **Solidify**
  con las normales invertidas y un material negro sin sombreado, por encima
  del modelo (o **Freestyle**, activando sólo el borde de silueta con grosor
  alto). Ambas están en `AYUDANTE.md`/`ENCARGO.md` punto 18 como opciones
  válidas; las dos dan el mismo look que se ve en las capturas del juego de
  Patricio Estrella.
- **Sombreado**: nodo **Toon BSDF** (o un *Color Ramp* de 2 pasos sobre un
  difuso normal) para que la luz caiga en bloques planos, no en degradado.
- ***Rigs* libres**: ver §11 (Sketchfab, licencia CC Attribution confirmada
  por API).

### Punto 24 · Obras parecidas y temas relacionados (punto entero, nuevo)

#### 24.1 La influencia confirmada por el propio autor y su equipo ✅✅

- **Stephen Hillenburg trabajó en *Rocko's Modern Life* (1993-1996)** antes
  de crear Bob Esponja, y **fue ahí donde le animaron a hacer su propia
  serie**; se llevó consigo a varios compañeros de *Rocko's* al montar el
  equipo de Bob Esponja ✅✅ ([Wikipedia (en)](https://en.wikipedia.org/wiki/SpongeBob_SquarePants),
  con nota al pie que remite a Hogan's Alley; confirmado también por
  [Rocko's Modern Life en Wikipedia](https://en.wikipedia.org/wiki/Rocko%27s_Modern_Life)).
- **Sin *Ren y Stimpy* (John Kricfalusi/Spumco), no existirían ni *CatDog* ni
  Bob Esponja**: Hillenburg «heredó rasgos de su estética y su lenguaje
  expresivo» ✅ ([Serielizados.com, «Nickelodeon: sitcoms demenciales, locura
  slapstick y el monopolio Esponja»](https://serielizados.com/nickelodeon-sitcoms-demenciales-locura-slapstick-y-el-monopolio-esponja/),
  en español). Varias personas del equipo de Bob Esponja (Vincent Waller,
  Fred Osmond, Kelly Armstrong, Bob Jacques, Bob Camp, Sherm Cohen) habían
  trabajado antes en *Ren y Stimpy*, lo que crea una **línea de estilo
  directa** entre ambas series ⚠️ una fuente de detalle ([exresearch.co](https://www.exresearch.co/behind-the-art-of-spongebob/)),
  pero coincide con el dato ✅ de Serielizados.
- El creador de *Rocko's Modern Life*, **Joe Murray**, cita como referencias
  gráficas propias a **Tex Avery, los hermanos Fleischer, Jay Ward (Rocky y
  Bullwinkle) y los Looney Tunes** ⚠️ una fuente ([Lambiek Comiclopedia](https://www.lambiek.net/artists/m/murray_joe.htm)):
  son las influencias «de segunda mano» que llegan a Bob Esponja a través del
  ambiente de *Rocko's*.

#### 24.2 Series con el mismo tono, según sitios de recomendación ⚠️ (curación de fans, no del autor)

*CatDog*, *Mr. Pickles*, *Agallas, el perro cobarde*, *Vaca y Pollo*,
*Duckman*, *Sanjay y Craig*, *La casa de los dibujos* (*Foster's Home for
Imaginary Friends*) — todas emparentadas con Bob Esponja y con *Ren y Stimpy*
en el mismo árbol de «humor absurdo de Nickelodeon/Cartoon Network de los 90
y 2000» ✅ el árbol en sí ([parecidas.com: Ren y Stimpy](https://parecidas.com/peliculas/14428-el-show-de-ren-y-stimpy),
[parecidas.com: Bob Esponja](https://parecidas.com/peliculas/15875-bob-esponja)),
⚠️ cada emparejamiento suelto es curación de un sitio de fans, no una
declaración del propio Hillenburg.

#### 24.3 Qué otras láminas del servidor se le parecen

Revisé los 131 encargos de `encargos/` y **ninguna otra serie pide el canal
`#ofertas-y-gratis`**: no hay choque de canal. En tono, la serie más cercana
de las ya encargadas es *Rick and Morty* (13, para `#noticias-series`), pero
es de humor adulto y cínico, no de humor absurdo «inocente» como Bob
Esponja; *Scooby-Doo* (26, para `#dudas`) comparte comedia con misterio, pero
no el mundo submarino ni el "todo puede pasar sin explicación" de Bikini
Bottom. Ninguna repite el concepto de «objeto real del mundo de la serie que
enseña precios» que se propone aquí para la caja registradora (§19 de la
biblia).

### Punto 25 · El mundo, la historia y sus símbolos (punto entero, nuevo)

#### 25.1 Las reglas del mundo, en cinco líneas ✅✅

1. Todo pasa bajo el agua, en la ciudad-estado de **Fondo de Bikini** (Bikini
   Bottom), en el océano Pacífico, justo debajo del **atolón Bikini** de
   verdad ✅✅ (Nickelodeon, [ficha de prensa vía Wayback](https://web.archive.org/web/20170315035655/http://www.vimn.com/press/nicktoons/series/spongebob-squarepants-0);
   [Encyclopedia SpongeBobia, «Bikini Bottom»](https://spongebob.fandom.com/wiki/Bikini_Bottom)).
2. La lógica es la del **chiste, no la física**: un fuego de leña puede
   arder bajo el agua «mientras nadie lo señale» — es el propio *Rule of
   Funny* de la serie, citado tal cual en [TV Tropes](https://web.archive.org/web/20260815110156/https://tvtropes.org/pmwiki/pmwiki.php/WesternAnimation/SpongebobSquarepants)
   ✅.
3. Sus habitantes son peces y otros bichos marinos que viven **como
   personas**: casas, coches (barquitos), trabajos, colegio — «no son
   animales viviendo en un mundo humano, es un mundo submarino nuevo vivido
   por criaturas marinas» (cita del análisis de diseño, [exresearch.co](https://www.exresearch.co/behind-the-art-of-spongebob/)) ⚠️.
4. Hay **teoría de fans confirmada a medias**: Bikini Bottom recuerda a las
   pruebas nucleares reales en el atolón Bikini. **Tom Kenny (voz de Bob) lo
   negó en 2015**; **Mr. Lawrence (voz de Plankton) dijo en 2024 que la
   teoría de los mutantes es verdad** y que las pruebas nucleares
   influyeron en más cosas de la serie ✅✅ dos fuentes con fechas distintas:
   [HuffPost, 7-feb-2015](https://www.huffingtonpost.com/2015/02/07/spongebob-squarepants-theory_n_6627556.html)
   y el vídeo de reunión del reparto, [YouTube/Esquire, 27-nov-2024](https://www.youtube.com/watch?v=5hlE75E4Yz8).
5. Todo se diseña para que se vea **«náutico»**, no genérico: cuerdas,
   remaches, anclas, portillos redondos, timones (§18.3).

> ⚠️ Dato de contexto, no para la lámina: en 2019 una profesora de la
> Universidad de Washington, Holly M. Barker, escribió que la serie
> «promueve un colonialismo violento y racista» por ponerle nombre de humor
> al atolón donde de verdad se desplazó a población indígena para hacer
> pruebas nucleares ✅ tres fuentes ([The Independent](https://www.independent.co.uk/arts-entertainment/tv/news/spongebob-squarepants-violent-racist-colonialism-professor-holly-m-barker-a9153976.html),
> [Spiked](https://www.spiked-online.com/2019/10/30/no-spongebob-squarepants-is-not-a-violent-colonialist/),
> [KEYE/CBS Austin](https://cbsaustin.com/news/offbeat/college-professor-says-spongebob-squarepants-is-violent-and-racist)).
> No es un dato para dibujar, pero es bueno que el dueño lo sepa si alguien
> lo menciona.

#### 25.2 La historia, por etapas (la serie es episódica; esto es el «detrás de cámara», no una trama única) ✅✅

- **1999-2004 · era Hillenburg**: creador y showrunner. Antes de la serie,
  hizo un cómic educativo, *The Intertidal Zone*, mientras enseñaba en el
  Ocean Institute; muchas ideas de la serie salen de ahí ✅ ([Michael Cavna,
  «The Interview: 'SpongeBob' Creator Stephen Hillenburg», The Washington
  Post, 14-jul-2009](http://voices.washingtonpost.com/comic-riffs/2009/07/_tom_kenny_who_voices.html)).
- **2004 · la película que iba a ser el final**: Hillenburg quería que *The
  SpongeBob SquarePants Movie* cerrara la serie. El éxito en taquilla hizo
  que Nickelodeon pidiera más, sin él como showrunner del día a día ✅
  (Oral History, §18.1).
- **2005-2015 · era Paul Tibbitt**: showrunner de las temporadas 4 a 9.
  Hillenburg seguía como productor ejecutivo, revisando cada episodio y con
  poder de veto (por ejemplo, frenó un capítulo de flashback sobre el origen
  de Perla) ✅ ([Digital Spy, entrevista a Tibbitt](https://web.archive.org/web/20131031235346/http://www.digitalspy.co.uk/tv/interviews/a312387/paul-tibbitt-spongebob-squarepants.html)).
- **2015 · Hillenburg vuelve, y muere en 2018**: regresó a la producción en
  enero de 2015 (durante la novena temporada); murió el 26 de noviembre de
  2018, de ELA. La temporada 13 fue la primera hecha enteramente sin él ✅✅
  ([Variety, 27-nov-2018](https://variety.com/2018/tv/news/spongebob-squarepants-creator-dead-dies-stephen-hillenburg-1203037362/);
  [Variety, 13-mar-2017, diagnóstico](https://variety.com/2017/tv/news/spongebob-squarepants-creator-stephen-hillenburg-reveals-als-diagnosis-1202007865/)).
- **Octubre de 2015 en adelante · era Waller/Ceccarelli**: **Vincent Waller**
  y **Marc Ceccarelli**, antes guionistas y directores de storyboard,
  **siguen siendo los showrunners hoy** (2026) ✅✅ ([Animation World
  Network, 17-jul-2024, entrevista por el 25.º aniversario](https://www.awn.com/animationworld/vincent-waller-and-marc-ceccarelli-talk-25-years-spongebob-squarepants)).
- **Expansión de la franquicia**: *Kamp Koral: SpongeBob's Under Years*
  (2021-2024, spin-off sobre el campamento de verano de Bob Esponja de niño)
  y *The Patrick Star Show* (2021-, con Patricio de presentador de late
  night) ✅. Películas, en orden: *The SpongeBob SquarePants Movie* (2004),
  *Sponge Out of Water* (2015), *Sponge on the Run* (2021, estrenada
  directamente en streaming por la pandemia), *Saving Bikini Bottom: The
  Sandy Cheeks Movie* (Netflix, ago-2024, por el 25.º aniversario),
  *Plankton: The Movie* (Netflix, mar-2025) y *Search for SquarePants*
  (cines, dic-2025) ✅✅.
- **Hoy**: la serie estrenó su **temporada 17 el 12 de junio de 2026** y es
  «la serie animada infantil más longeva hecha en Norteamérica» ✅
  ([Wikipedia (en), sección de introducción](https://en.wikipedia.org/wiki/SpongeBob_SquarePants),
  con nota al pie de 2026).

#### 25.3 Emblemas, objetos icónicos y vocabulario propio ✅✅

- **El Crustáceo Cascarudo (Krusty Krab)**: el letrero cuelga con forma de
  concha/áncora y dice «THE KRUSTY KRAB» (ya en la biblia, §3 imagen).
- **El Balde de Cebo (Chum Bucket)**: rival al otro lado de la calle, de
  Plankton y Karen; casi no tiene clientes porque vende «chum» (cebo de
  pescar), no comida de verdad ✅ ([Wikipedia (en)](https://en.wikipedia.org/wiki/SpongeBob_SquarePants)).
- **La Espátula Dorada (Golden Spatula)**: aparece primero en el episodio
  «¡Plankton!»; en los videojuegos es el coleccionable principal para abrir
  zonas nuevas, y los «Shiny Objects» (objetos brillantes) son la moneda del
  juego para pagar peajes o comprarle espátulas a Don Cangrejo ✅ ([Logopedia
  y Encyclopedia SpongeBobia, «Golden spatula»](https://spongebob.fandom.com/wiki/Golden_spatula)).
- **La Fórmula Secreta**: el objeto que todo el mundo persigue (Plankton la
  quiere robar en casi cada episodio); es el motor de la rivalidad entre los
  dos restaurantes.
- **Goofy Goober**: la mascota-cacahuate de la heladería-barco del mismo
  nombre, con sombrero sureño, pajarita roja de lunares y guantes tipo
  Mickey Mouse; aparece primero en el libro de la película de 2004 ✅
  ([Encyclopedia SpongeBobia, «Goofy Goober»](https://spongebob.fandom.com/wiki/Goofy_Goober)).
- **Nombre en latino de Fondo de Bikini confirmado**: la propia ficha
  multilingüe de la wiki en inglés da el nombre en español como **«Fondo de
  Bikini»** ✅ ([Encyclopedia SpongeBobia, «Bikini Bottom», enlaces
  interwiki](https://spongebob.fandom.com/wiki/Bikini_Bottom)).
- **Lugares del mundo (vocabulario para carteles o menciones)**: Jellyfish
  Fields (Campo de Medusas), Goo Lagoon (Laguna Goo), Sand Mountain (Montaña
  de Arena), Kelp Forest (Bosque de Algas), Rock Bottom, Shell City,
  Industrial Park, el Mermalair (guarida secreta de Mermaid Man y Barnacle
  Boy), Conch Street (Calle Conchita en varias traducciones), Glove World!
  (el parque de diversiones) — todos ✅ de la misma ficha de «Bikini Bottom»
  de Encyclopedia SpongeBobia (wikitexto propio, no un resumen de IA).

## Lo mejor para la lámina

- El **contorno negro grueso con sombreado plano** que se ve hasta en los
  juegos 3D (§11, §18.5) es la clave técnica para que la caja registradora
  en Blender encaje: Solidify invertido o Freestyle, más un Toon BSDF, no un
  render realista.
- El patrón de la interfaz de *Rehydrated* — **icono de botón metido dentro
  de la frase** («Presiona 🅡 para…», §6) — es un modelo real y propio de la
  franquicia para un aviso corto tipo «Reclama ya» en la lámina, mejor que
  un botón genérico de Discord.
- La **Espátula Dorada** y los **«Shiny Objects»** (§25.3) son el icono
  propio de la serie para «premio»/«coleccionable gratis»: mejor que
  inventar una moneda genérica para marcar lo que es gratis.
- Fondos: **gouache + línea digital encima** (§18.2) es la textura a imitar
  si se pinta algo a mano para el fondo de la lámina, no un dibujo vectorial
  liso.
- El vínculo con *Ren y Stimpy* / *Rocko's Modern Life* (§24.1) explica por
  qué las expresiones son tan exageradas: sirve para justificar caras muy
  grandes y gestos exagerados en los personajes de la lámina sin que se vea
  «hecho por IA».

## No encontré

- La **letra exacta del rotulado de los cómics** de la franquicia (Papercutz
  / United Plankton Pictures): sólo generadores de efecto de texto de fans,
  ninguno confirma el tipo real. Busqué «SpongeBob comics lettering font» y
  «Papercutz SpongeBob lettering» en inglés.
- **Capturas abiertas de la interfaz de *Krusty Cook-Off***: sólo casos de
  estudio de las agencias que la diseñaron (PUNCHev, Christopher Furniss),
  sin imágenes que pudiera abrir directamente.
- **Game UI Database** para *Rehydrated* (id 1490): ni en directo ni en
  Wayback Machine se puede leer (aplicación de una sola página, la copia
  archivada sólo trae el armazón vacío del sitio).
- **Qué software usó exactamente Nickelodeon Animation Studio** para el
  «digital ink and paint» de la propia serie de televisión (sólo se
  confirmó USAnimation para la película de 2004, no para los episodios).
- **Una entrevista directa de Purple Lamp Studios** (el estudio de los
  juegos nuevos) sobre cómo lograron el *look* con contorno en 3D: lo que
  hay es lo que yo mismo vi y deduje de las capturas (§11, §18.5), no una
  cita del estudio.

## Bitácora de búsqueda

### Comprobación de red (26-sep-2026)

- **Ya funcionan** (antes daban 403 en la primera pasada): `1001fonts.com`,
  `dafont.com`, la **API de Fandom** con cabecera de navegador
  (`spongebob.fandom.com/api.php`), **Wikipedia** en `action=raw` (wikitexto
  con notas al pie completas), **Sketchfab** por su API.
- **Siguen dando 403 en directo**, pero se pudieron leer por **Wayback
  Machine** (con el sufijo `id_` en la URL para el HTML sin la cabecera del
  archivo, y a veces con `Accept-Encoding: identity` para evitar una
  compresión zstd que `curl --compressed` no sabía descomprimir; para
  `tcrf.net` hizo falta instalar el módulo `zstandard` de Python y
  descomprimir a mano con `stream_reader`): `tvtropes.org`, `tcrf.net`,
  `gameuidatabase.com` (esta última, vacía incluso archivada: es una
  aplicación de una sola página).
- **`spongebob.fandom.com` en directo** (sin pasar por la API) sigue dando
  403; por eso todo lo de Fandom de esta parte pasa por `api.php`.

### Búsquedas web (12; es = español, en = inglés)

1. (en) SpongeBob SquarePants animation technique interview Toon Boom
   traditional cel
2. (en) Stephen Hillenburg influences Ren and Stimpy Tex Avery Rocko's
   Modern Life interview
3. (en) SpongeBob background art style watercolor gouache art director
   interview
4. (en) SpongeBob SquarePants symbols Krusty Krab logo Chum Bucket logo
   Golden Spatula
5. (es) series parecidas a Bob Esponja Nickelodeon estilo absurdo Ren and
   Stimpy Rocko
6. (en) SpongeBob comics Papercutz lettering font speech bubble style comic
   book → no encontrado
7. (en) "toon shader" Blender Freestyle tutorial cartoon flat cel outline
8. (en) SpongeBob Krusty Cook-Off interface UI menu screenshot
9. (es) SpongeBob SquarePants historia por temporadas resumen arcos
   personajes cambios showrunner
10. (en) Sketchfab SpongeBob rig free download rigged 3D model Blender
11. (en) SpongeBob "digital ink and paint" software USAnimation Nickelodeon
    2000
12. Búsquedas directas sin buscador (Fandom API, Wikipedia raw, Sketchfab
    API, Wayback): no gastan cupo.

**Otros idiomas**: la serie es de Estados Unidos (creador estadounidense,
producción en California y Corea del Sur para el dibujo, no para el guion ni
la dirección de arte); no busqué en japonés, coreano ni chino porque
`ENCARGO.md` lo pide sólo «si la obra viene de ahí», y no es el caso. Sí
comprobé si la wiki tenía nombre en español («Fondo de Bikini», §25.3).

### Fuentes nuevas de esta parte, por tipo

- **Oficiales / de producción**: Nickelodeon (ficha de prensa vía Wayback),
  Smithsonian Institution (cel de producción conservado).
- **Entrevistas al staff**: Paul Tibbitt (Digital Spy), Stephen Hillenburg
  (The Washington Post), Luke Brookshier (4Mations), Vincent Waller y Marc
  Ceccarelli (Animation World Network), la fondista Amy Lewis (su propio
  portafolio y su X/Twitter), «The Oral History of SpongeBob SquarePants»
  (Hogan's Alley, vía Wayback).
- **Prensa de animación**: Animation Magazine (dos artículos), Cartoon Brew,
  Animation World Network (tres artículos), Variety (dos artículos).
- **Wikis**: Encyclopedia SpongeBobia (por su API, tres páginas), TV Tropes
  (por Wayback), Logopedia.
- **Código y datos técnicos**: The Cutting Room Floor (por Wayback,
  descomprimido con `zstandard`), GitHub (Jordy3D, la letra Some Time
  Later).
- **Arte**: ArtStation (April Borchelt), X/Twitter (Amy Lewis).
- **3D**: Sketchfab, por su API (licencias comprobadas, no de la búsqueda).
- **Academia / crítica**: The Independent, Spiked, KEYE/CBS Austin (la
  crítica de Holly M. Barker, §25.1).
- **Estudios de diseño de interfaz**: PUNCHev Group, portafolio de
  Christopher Furniss (Krusty Cook-Off, sin poder ver las capturas).
- **Vídeo**: YouTube/Esquire (reunión del reparto, nov-2024, confirmación de
  Mr. Lawrence sobre la teoría nuclear).

Repasado contra `ENCARGO.md`: los puntos 5, 6, 11, 18, 24 y 25 están
completos con lo obligatorio de cada uno. Lo que falta (rotulado exacto de
los cómics, capturas de Krusty Cook-Off, Game UI Database) es detalle extra,
ya listado en «No encontré», no bloquea el punto.
