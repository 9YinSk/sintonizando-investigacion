# Parte IMAGEN · 89-frieren-paisajes-y-memoria (puntos 1, 3, 15, 16, 19, 23 de ENCARGO.md)

Serie hermana: **33-frieren** (biblia ya completa, con `partes/imagen.md` propio).
Ya tiene a fondo: portadas/banners AniList, hojas de personajes, vestuario con
hex medidos (§16 de su biblia), sitios con luz y paleta (§5), fondos de
pantalla generales (§17), texturas de tela/papel/tramas/emblema (§19),
colaboraciones de cafés/figuras/cosplay (§23). **No repito esos datos** (los
cito por número cuando hacen falta). Esta parte profundiza el **enfoque nuevo
del encargo 89: fondos, luz y melancolía** — el material de **arte de fondos
(background art), ruinas, el "más allá" y la memoria del viaje**, que la
biblia hermana apenas toca.

Parto de `partes/datos-imagen.md` (ya recolectado: AniList, Danbooru,
Safebooru, Wallhaven, Sketchfab, Openverse) y de
`herramientas/investigar_serie.py` centrado en **páginas de LUGARES**, no de
personajes (ya hecho en la hermana), para tener hojas propias.

## Hallazgos

### Punto 1 · Arte oficial, en cantidad y variado (foco: arte de fondos)

- **«Official Guide Book»** (Shōgakukan, 24-jul-2024, 144 pp., ISBN
  978-4-09-199034-1): guía oficial de los 28 episodios, con **galería de
  «art board» (planchas de fondo) por bloque de episodios** (1-6, 7-17,
  18-28) comentada por la **directora de arte Sawako Takagi**, una
  **galería de arte conceptual** con entrevistas a **Seiko Yoshioka**
  (fondos), **Harue Ono** (color), **Akane Fushihara** (fotografía),
  **Izumi Seguchi**, **Daiki Harashina**, **Toru Iwasawa**, **Shoji
  Hata**, **Yuichiro Fukushi**, **Shoichiro Taguchi**, **Mikito
  Bizenjima** (staff de fondos/acabado), y una sección propia llamada
  **«Character memories selection»** (recuerdos: el viaje con Himmel; la
  relación de Fern y Stark; los aspirantes al examen; la línea
  maestro-aprendiz) — **es la fuente oficial más directa sobre «memoria»
  como tema de producción** · [Frieren Wiki, «Official Guide
  Book»](https://frieren.fandom.com/wiki/Official_Guide_Book) (wikitext
  con el índice completo) ✅ (contrastado con la ficha de venta,
  ISBN 9784091990341).
- **Artbook «Frieren: Beyond Journey's End (Sousou no Frieren) Art Works
  Vol. 1»** (Shōgakukan, 18-dic-2023, 128 pp.), **distinto** del Guide
  Book (es sólo ilustración, sin entrevistas) · [ficha en
  jpbookstore.com](https://jpbookstore.com/products/frieren-beyond-journeys-end-sousou-no-frieren-art-works-vol1-original-art-collection-illustration-book)
  + [japanese-creative-books.com](https://japanese-creative-books.com/product/illustration/frieren-beyond-journeys-end-art-works-book-vol-1/)
  ✅ dos fuentes (no pude ver el interior, sólo la ficha de venta) ⚠️ contenido exacto.
- **Exposición oficial itinerante «アニメ 葬送のフリーレン展 〜冒険の終わりから
  始まる物語〜»** («La historia que empieza cuando termina la aventura»):
  empezó en **Ikebukuro Sunshine City** (abr-2024), pasó por **Sapporo**
  y terminó en el **Museo de Arte del Siglo XXI de Kanazawa, Galería B**
  (7-ago a 6-sep-2025) · cuenta oficial
  [@frieren_ten en X](https://x.com/frieren_ten) (anuncio de Kanazawa:
  [x.com/frieren_ten/status/1920765692581748944](https://x.com/frieren_ten/status/1920765692581748944))
  + [artículo de Tokyo
  Weekender](https://www.tokyoweekender.com/event/frieren-beyond-journeys-end-anime-exhibition/)
  ✅ dos fuentes. **Trae ilustraciones exclusivas de la exposición**
  («Exhibition Illustrations»), un set entero de piezas nuevas por
  distintos animadores/ilustradores del staff (Reiko Nagasawa, Ayaka
  Minoshima —de Frieren y de Himmel por separado—, Daiki Tanaka, Kanata
  Yanagisawa y más), listadas con nombre de archivo en la galería oficial
  de la wiki · [Season 1
  Gallery](https://frieren.fandom.com/wiki/Frieren:_Beyond_Journey%27s_End_Season_1/Gallery)
  (sección «Exhibition Illustrations», wikitext) ✅. **Es la fuente más
  clara de que la serie SÍ expone su arte de fondos como pieza de museo**
  — perfecto para justificar un canal de «arte» o «paisajes» con tono
  serio, no sólo merchandising.
- **Galería de arte conceptual de lugares** (Season 1 y Season 2, sección
  «Concept Art» de cada página de galería en la wiki): decenas de
  **drafts, modelos de terreno y «concept art» a color** de Seiko
  Yoshioka por región — mucho más grande de lo que cita la biblia
  hermana (que sólo listaba 3-4 ejemplos sueltos). Confirmé y **descargué
  3 piezas para verlas de verdad** (con Read + `estilo.py`, paleta
  medida):
  - [Ruins of the King's Tomb.png](https://static.wikia.nocookie.net/frieren/images/f/f5/Ruins_of_the_King%27s_Tomb.png)
    (1277×742, fondo real del anime, EP23): tumba tallada en un
    acantilado, columnas clásicas medio cubiertas de vegetación,
    escalinata larga. Paleta: `#A69D94` `#BEB5A9` `#3B4D49` `#576164`
    `#62845F` piedra beige + verde musgo, sombreado degradado/pintado,
    saturación 20%, brillo 59% ✅ (visto entero, medido).
  - [Rufen Region abandoned fort exterior draft by Seiko
    Yoshioka.png](https://static.wikia.nocookie.net/frieren/images/3/3d/Rufen_Region_abandoned_fort_exterior_draft_by_Seiko_Yoshioka.png)
    (1920×1080): **torre en ruinas** con el tejado roto, un puente de
    madera derrumbado, cuervos volando, silueteada contra un cielo claro
    tras un bosque de abetos — **draft en gris puro** (0% saturación,
    brillo 48%, sombreado plano/cel): confirma que el estudio primero
    bocetea el fondo **sólo en valores de gris** antes de colorear (dato
    útil para el punto 18 de texto/técnica, lo dejo anotado aquí porque
    lo vi en mi propia búsqueda) ✅ (visto entero, medido).
  - [Bier Region ruins draft by Seiko
    Yoshioka.png](https://static.wikia.nocookie.net/frieren/images/7/79/Bier_Region_ruins_draft_by_Seiko_Yoshioka.png)
    (1920×1080): portalón de piedra en penumbra, **un personaje marcado
    en rosa fosforito** (no coloreado, sólo para dar escala) frente a la
    puerta — **draft de valores, 0% saturación salvo el marcador de
    escala**, brillo 31% ✅ (visto entero, medido). Muestra el método de
    trabajo: gris para luz/sombra, un solo color plano para ubicar al
    personaje.
- **Aureole** («la Tierra donde descansan las almas» / «el Cielo»,
  lugar al que Frieren viaja para reencontrarse con Himmel — el motor de
  toda la serie): el fondo oficial **[Aureole
  EP4.png](https://static.wikia.nocookie.net/frieren/images/2/27/Aureole_EP4.png)**
  (1920×1080, EP4) es **la imagen más «memoria» de toda la serie**: un
  árbol dorado dentro de un templete circular, columnas y ruinas claras
  asomando entre niebla, un listón de luz dorada cruzando el cuadro.
  Paleta medida (`estilo.py`): `#F2F5EA` 42.6% `#C6F2F8` 24.9% `#CBDCD1`
  11.3% `#EBEFB7` 8.2% — **brillo 93%, saturación sólo 16%**: es casi
  sobreexpuesto, pastel, sin apenas línea (línea `#B9C488`) ✅ (visto
  entero, medido). Hay también **concept art** de Yoshioka del mismo
  sitio: [Aureole concept art by Seiko
  Yoshioka.png](https://static.wikia.nocookie.net/frieren/images/4/47/Aureole_concept_art_by_Seiko_Yoshioka.png)
  (1427×798, paleta casi igual: brillo 92%) ✅. Ficha del lugar: **Aureole
  = 魂の眠る地 (Oreōru), «la Tierra donde descansan las almas», también
  llamada «el Cielo»**, en el extremo norte del continente (Ende); ahí
  reside —se presume— la Diosa de la Creación · [Frieren Wiki,
  «Aureole»](https://frieren.fandom.com/wiki/Aureole) (wikitext) ✅.
- **Hojas de contacto propias** (`herramientas/investigar_serie.py --wiki
  frieren --paginas "Royal Capital" "Aureole" "Ruins of the King's Tomb"
  "Lake Korridor" "Heiß" "Warm"`, **91 imágenes** en 2 hojas, todas
  vistas con Read): `hojas/paisajes_01.jpg` y `hojas/paisajes_02.jpg`.
  Además de lo ya citado arriba, destaco (número de la hoja):
  - **paisajes_01 n.º 31** «Statue of Himmel in the fortress city»:
    estatua conmemorativa de Himmel en una plaza — objeto de homenaje/
    memoria hecho piedra, perfecto para una lámina de «legado».
  - **paisajes_01 n.º 42** «Royal Capital Era Meteors outlook EP1»: la
    Capital de noche con el lago reflejando estrellas — la escena donde
    el grupo mira la lluvia de meteoros (visible también en
    **paisajes_02 n.º 90**, «The Hero's Party watches the Era Meteor»,
    panel de manga con las siluetas mirando al cielo).
  - **paisajes_02 n.º 71** «Lake Korridor deserted monastery CH78»: panel
    de manga, un monasterio abandonado con cúpula, en grises — otro
    sitio en ruinas ligado a la trama de la memoria (el examen de
    primera clase transcurre ahí).
  - **paisajes_02 n.º 74** «Aureole concept art by Seiko Yoshioka» (ya
    descrita arriba) y **n.º 80** «Ruins of the King's Tomb» (color, ya
    descrita arriba), juntas en la misma hoja para comparar ruina
    «viva» (King's Tomb, verde y ocupada) contra ruina «celestial»
    (Aureole, pastel y vacía).
  - **paisajes_02 n.º 85-86** «Warm terrain model» y «Warm terrain model
    2 by Seiko Yoshioka»: **maquetas de terreno en 3D** (bloques de
    color plano, sin textura) que el estudio usa para calcular
    perspectiva y luz antes de pintar el fondo final — referencia directa
    de cómo bloquear un escenario en Blender antes de aplicar el estilo
    2D encima.

### Punto 3 · Fan art y 3D (como referencia; foco: paisajes y sitios)

- **Fan art de paisaje puro** (no de personaje), etiqueta `scenery` en
  Danbooru/Safebooru — más específico que la búsqueda genérica por
  personaje que ya trae `datos-imagen.md`:
  - [3277×4096, puntuación 20](https://cdn.donmai.us/original/14/cd/14cd567a57a384af93761bf06478c808.jpg)
    · autor/origen: [x.com/gmmarady](https://x.com/gmmarady/status/2092266418553454594)
    ✅ (medido, Danbooru API).
  - [2000×3500, puntuación 15](https://cdn.donmai.us/original/95/e4/95e43dd58529e9f0ffdc8bf65312c8e8.jpg)
    · autor: [x.com/Porukana_Art](https://x.com/Porukana_Art/status/2095829730612379750) ✅.
  - **@gmmarady (X/Twitter)** aparece **4 veces** entre los resultados de
    `scenery` (todas de 2026, puntuación 10-20): es un fan artist que se
    repite pintando fondos/paisaje de la serie, no sólo personajes ⚠️
    (no confirmé si tiene portafolio dedicado sólo a Frieren, una fuente).
  - [4500×3048, ♥581 en Wallhaven](https://w.wallhaven.cc/full/gp/wallhaven-gpl8d3.jpg)
    · autor: [Owl279 / Pixiv
    116555120](https://www.pixiv.net/en/artworks/116555120) — **visto
    entero** con Read: Frieren de espaldas bajo un **árbol gigante
    dorado-violeta** con mariposas, ruinas de piedra a los lados, luz de
    amanecer/atardecer. Paleta medida (`estilo.py`): `#716CBF` `#544C88`
    `#2D315A` `#CEB6D9` `#9B8ED9`, saturación 39%, brillo 54% ✅. **Es
    prácticamente un "árbol de Flamme" imaginado por un fan**: mismo
    lenguaje visual que el Aureole oficial (árbol + ruinas + niebla +
    contraluz), sin ser calco — sirve como referencia de estilo, nunca
    para pegar.
- **Modelos 3D con licencia** (Sketchfab, complementando `datos-imagen.md`
  que sólo trajo modelos de *personajes*):
  - **«Himmel The Hero»** · bmwylam · CC Attribution ·
    [sketchfab.com/3d-models/none-18793206124245eb8e20fafc95b868ab](https://sketchfab.com/3d-models/none-18793206124245eb8e20fafc95b868ab) ✅.
  - **«Himmel the Hero Pedastal»** (el pedestal/base de la estatua, por
    separado) · bmwylam · CC Attribution ·
    [sketchfab.com/3d-models/none-8f3f0a27429341149ccc442ef24ee0c0](https://sketchfab.com/3d-models/none-8f3f0a27429341149ccc442ef24ee0c0)
    ✅ — **referencia 3D real de la estatua de Himmel** (el mismo
    monumento que aparece en `paisajes_01` n.º 31): útil para modelar el
    objeto de homenaje/memoria en Blender.
  - No encontré en Sketchfab **modelos de un pueblo o ruina con licencia
    libre hechos específicamente sobre localizaciones de Frieren**
    (busqué «frieren village», «frieren ruins», «frieren royal capital»)
    ⚠️. Alternativa genérica libre para montar la escena: **«Medieval
    castle with village»** · isogl · CC Attribution ·
    [sketchfab.com/3d-models/none-5109b5e46e064790badecedf8f6d2ef6](https://sketchfab.com/3d-models/none-5109b5e46e064790badecedf8f6d2ef6)
    y **«Low Poly Medieval Environment Pack (35+ Props)»** ·
    anastasita.3d · CC Attribution ·
    [sketchfab.com/3d-models/none-a850530905a24d97bc4aa83353aba134](https://sketchfab.com/3d-models/none-a850530905a24d97bc4aa83353aba134)
    ✅ (mismo criterio que usó la biblia hermana con Poly Haven: piezas
    genéricas de la época, no de la serie).
  - Los **modelos 3D con licencia de personajes** (Frieren, Fern, la
    tetera, el hacha) ya están listados en `datos-imagen.md` y en la
    biblia hermana §4 — no los repito.

### Punto 15 · Vestuario

**Ya está medido a fondo en la biblia hermana** (33-frieren, §16: rayas de
la camisa de Frieren `#FFFFFF`/`#181818`-`#1E1E1E`, ribete dorado
`#DFC27A`/`#C0B064`, colores planos de Fern/Stark/Himmel) — no repito esas
medidas. Lo que aporto, con el foco de «paisajes»:

- **La ropa cambia con la región y el clima del viaje**, no sólo por
  temporada de la serie: en las hojas propias (`paisajes_01` n.º 10 «Exterior
  of the inn... [nieve]», n.º 18 «baños termales en Heiß», n.º 63 «ciudad
  portuaria nevada del Lago Korridor») los personajes llevan **capas y
  bufandas añadidas encima de la ropa base** en las regiones frías del
  norte (Kühl, Heiß), y ropa ligera en las zonas cálidas del sur (Warm,
  litoral) — visto en las 91 imágenes de mis hojas, comparando escenas
  del mismo personaje en distinto clima ✅ (confirmado por contraste
  directo entre imágenes de la misma hoja).
- **Se lee incluso a contraluz**: en [«Frieren and Fern watch the sunset
  in Warm EP3.png»](https://static.wikia.nocookie.net/frieren/images/f/f8/Frieren_and_Fern_watch_the_sunset_in_Warm_EP3.png)
  (Punto 16, visto entero) los dos personajes quedan en silueta casi
  total contra un atardecer, y aun así se distingue el **blanco de
  Frieren** del **morado oscuro de Fern**: el bloque de color de cada
  personaje funciona incluso sin luz directa ✅ (visto). No medí hex
  nuevos aquí a propósito (el contraluz falsea el color real de la tela):
  ver los hex ya medidos de verdad en la biblia hermana §16 y su Punto 19
  (rayas y ribete).

### Punto 16 · Ciudades, paisajes y fondos de pantalla (el corazón del encargo)

**Ya está el listado de luz por sitio y hora del día en la biblia hermana**
(§5.2 y §17.1) — no repito esa tabla. Lo nuevo:

- **La lista completa de regiones y lugares con nombre propio** es mucho
  más larga que los 12 sitios que mide la hermana: la categoría
  `Locations` de la wiki trae **más de 30 entradas** (Alt Woods, Appetit
  Region, Aufgabe Federation, Aureole, Bande Woods, Bier Region, Bohne
  Village, Bredt Region, Decke Region, Demon King's Castle, Drachen
  Region, Eiseberg, Empire, Ende, Graf Dach's Domain, Great Sanft Forest,
  Great Tor Canyon, Heiß, Norm Company Territory, Riegel Canyon, Royal
  Capital, Ruins of the King's Tomb, Rufen Region, Turk Region, Waal…) ·
  [Frieren Wiki, categoría
  Locations](https://frieren.fandom.com/api.php?action=query&list=categorymembers&cmtitle=Category:Locations)
  (API, 30+ resultados) ✅. Es la lista para elegir sitios que la hermana
  no llegó a cubrir.
- **Aureole, «la Tierra donde descansan las almas»** (ver Punto 1, ya
  descrita con paleta): es EL sitio de la memoria en la serie — el
  destino final del viaje de Frieren, dibujado deliberadamente
  sobreexpuesto y casi sin saturación, como contraste con el resto del
  mundo (verde y cian intensos en el día a día, según §5.3 de la
  hermana). **Es el concepto más fuerte que puedo aportar para un canal
  o lámina de "paisajes y memoria".**
- **Ruinas como motivo recurrente** (no sólo Aureole): Ruins of the
  King's Tomb (tumba en un acantilado, EP23), el fuerte abandonado de
  Rufen Region (draft, ver Punto 1), el monasterio abandonado del Lago
  Korridor (`paisajes_02` n.º 71) y las ruinas de Bier Region (mencionadas
  en el índice de la galería de Season 2, no las descargué: «Bier Region
  ruins draft» y «draft 2», mismas coordenadas que el resto del concept
  art de Yoshioka) — **el mundo de Frieren está lleno de restos de
  civilizaciones o batallas pasadas que los personajes cruzan sin
  detenerse mucho**, un motivo de fondo constante para «memoria» ✅
  (patrón confirmado en al menos 4 sitios distintos con nombre propio).
- **Mapa oficial del viaje**: la web oficial tiene una página **«旅の軌跡を
  辿る地図» (mapa que traza el rastro del viaje)** en
  `frieren-anime.jp/special/map/` — **no pude abrirla** (Cloudflare la
  protege con verificación JS; la Wayback Machine también la bloqueó,
  «blocked by egress policy» en los 2 intentos) ⚠️. Anoto su existencia
  y la URL para quien la reintente con `navegar.py` cuando el navegador
  esté disponible.
- **Analogía con sitios reales** (para fotos de referencia de textura, no
  como fuente de diseño): blogs de turismo japoneses señalan que el
  mundo mezcla **arquitectura alemana y checa de entramado de madera y
  piedra** (sin un único lugar real confirmado por el estudio) y que
  **Huis Ten Bosch** (parque temático holandés en Nagasaki) y **Yufuin**
  (pueblo balneario japonés con calles que recuerdan a Salzburgo) son los
  destinos de «peregrinaje» más citados por fans en Japón para fotografiar
  algo parecido · [libert.co.jp, guía de
  peregrinaje](https://libert.co.jp/pilgrimage-guild/frieren-pilgrimage/)
  + [AniTabi, mapa de sitios reales](https://anitabi.jp/works/36?lang=en)
  ⚠️ (ninguna fuente oficial del estudio confirma un lugar real
  concreto; tratarlo como "ambiente", no como localización exacta).
- **Fondo de fans destacado** (ver Punto 3): el wallpaper del árbol
  dorado con mariposas y ruinas (Wallhaven `gpl8d3`, ♥581) — mismo
  lenguaje visual que Aureole, sin ser el sitio oficial.
- **[Frieren and Fern watch the sunset in Warm
  EP3.png](https://static.wikia.nocookie.net/frieren/images/f/f8/Frieren_and_Fern_watch_the_sunset_in_Warm_EP3.png)**
  (1920×1080, dentro de `paisajes_01` n.º 65): Frieren y Fern comen en la
  terraza de una posada con vistas a una **ciudad fortificada costera con
  un acueducto/puente curvo** cruzando la bahía, sol poniéndose sobre el
  mar. **Vistas enteras con Read**: los personajes quedan a
  **contraluz, casi en silueta** — y aun así se distingue el blanco de
  Frieren del morado oscuro de Fern, prueba de que el diseño de color de
  cada uno **se lee incluso sin luz directa** (dato de lectura, no medí
  hex de la ropa aquí porque el contraluz falsea el color real; ver los
  hex ya medidos en la biblia hermana §16) ✅ (visto entero). Paleta del
  cielo/mar (`estilo.py`): `#F5C4A4` `#7F484D` `#DAB0B5` `#9D635C`,
  brillo 75%, saturación 36% — atardecer costero, otra variante de «hora
  dorada» que no estaba en la tabla de la hermana (§17.1, que no cubre
  Warm).

### Punto 19 · Texturas 2D (foco: paisaje, no vestuario — eso ya está en la hermana)

La hermana midió texturas de **tela, papel, tramas de manga y el
emblema** (su §19) — aquí sumo las texturas que faltan para **pintar el
paisaje mismo** (musgo, hierba, corteza, piedra de ruina, agua/hielo),
todas **CC0, sin crédito obligatorio**, medidas por su miniatura oficial
1024×1024 en la API de ambientcg:

- **Hierba**: `Grass001` · [ambientcg.com/a/Grass001](https://ambientcg.com/a/Grass001) ✅.
- **Corteza de árbol** (para el árbol de Aureole o los abetos del norte):
  `Bark014` · [ambientcg.com/a/Bark014](https://ambientcg.com/a/Bark014) ✅.
- **Piedra con musgo** (para las ruinas — Ruins of the King's Tomb,
  Rufen Region): `Rock064` · [ambientcg.com/a/Rock064](https://ambientcg.com/a/Rock064)
  ✅, alternativa `Ground037` (tierra con musgo) ✅.
- **Hielo/agua helada** (para las escenas de Heiß y el norte nevado):
  `Ice002` · [ambientcg.com/a/Ice002](https://ambientcg.com/a/Ice002) ✅.
- Confirmado por API (`ambientcg.com/api/v2/full_json`), las 4 con
  miniatura 1024×1024/2048×2048 disponible en PNG/JPG/WEBP.
- (Madera, piedra de plaza, bronce, terciopelo, cuero y las texturas de
  vestuario ya están en la biblia hermana §5.4 y su Punto 19 — no las
  repito.)

### Punto 23 · Colaboraciones y cruces (foco: exposición de arte, no merchandising)

La hermana ya documentó a fondo cafés, figuras, ropa de gala y cosplay
(su §23) — no repito esa tabla completa (>15 colaboraciones). Lo que
faltaba, y que encaja mejor con «paisajes y memoria»:

- **La exposición oficial «アニメ 葬送のフリーレン展»** (ver Punto 1: Ikebukuro
  2024 → Sapporo → Kanazawa 21st Century Museum of Art, ago-sep 2025) es
  en sí misma una **colaboración/evento**, distinta de una tienda o un
  café: el estudio **expone el arte de fondos como obra de museo**, con
  ilustraciones nuevas encargadas para la ocasión (ver lista de
  «Exhibition Illustrations» en Punto 1). Es la prueba más fuerte de que
  el fondo/paisaje de la serie se trata como arte por derecho propio, no
  sólo como decorado — dato central para justificar la premisa del
  encargo 89.
- No encontré (⚠️, dos búsquedas en japonés e inglés: «フリーレン 美術展
  背景» y «Frieren background art exhibition catalog») un **catálogo
  impreso** de la exposición aparte del propio Art Works Vol.1 y el
  Official Guide Book ya citados.

## Lo mejor para la lámina

- **Aureole** (Punto 1/16): árbol dorado, ruinas pastel, niebla y un haz
  de luz — la imagen oficial que mejor resume «paisajes y memoria»
  (`estilo.py`: brillo 93%, saturación 16%).
- El **fuerte en ruinas de Rufen Region** (draft en grises, Punto 1):
  torre rota, cuervos, bosque de abetos — encaje perfecto para una
  lámina melancólica sin colorear de más.
- La **estatua de Himmel** (`paisajes_01` n.º 31 + el modelo 3D con
  licencia «Himmel the Hero Pedastal» en Sketchfab): un objeto real,
  modelable en Blender, con historia de homenaje dentro de la serie.
- El **wallpaper del árbol dorado con mariposas** (Wallhaven `gpl8d3`,
  Punto 3): mismo lenguaje que Aureole hecho por un fan, sólo como
  referencia de estilo.
- Las **hojas propias `paisajes_01.jpg` y `paisajes_02.jpg`** (91
  imágenes, Punto 1): el catálogo más grande de lugares con nombre propio
  que tiene esta biblia; cualquier lámina de «sitios» debería mirarlas
  antes de elegir.

## No encontré

- ⚠️ El **mapa oficial del viaje** (`frieren-anime.jp/special/map/`):
  Cloudflare lo bloquea (verificación JS) y la Wayback Machine dio
  «blocked by egress policy» en los 2 intentos — pendiente para quien
  tenga navegador disponible (`navegar.py`).
- ⚠️ Un **catálogo impreso propio de la exposición** «葬送のフリーレン展»
  (aparte del Art Works Vol. 1 y el Official Guide Book, que sí están
  citados): busqué «フリーレン展 図録» sin resultado claro de venta o
  contenido.
- ⚠️ **Modelos 3D con licencia libre de un lugar o ruina concretos de la
  serie** (no de personajes): no existen en Sketchfab bajo los términos
  que probé («frieren village», «frieren ruins», «frieren royal
  capital», «frieren tomb»); dejo alternativas genéricas de la época en
  su lugar (Punto 3).
- Esto es **extra**, no obligatorio: no confirmé si **@gmmarady** (fan
  artist de paisajes recurrente) tiene un portafolio dedicado sólo a
  Frieren — sólo vi 4 piezas sueltas en Danbooru.

## Bitácora de búsqueda

Partí de `partes/datos-imagen.md` (no repetí AniList, Danbooru genérico
por personaje, Safebooru genérico, Wallhaven, Sketchfab de personajes ni
Openverse) y de `biblias/33-frieren/partes/imagen.md` + su `biblia.md`
(secciones 3, 4, 5, 16, 17, 19, 23, leídas con `sed`/`cat`, no con
`seccion.py` porque es de otro encargo) para no repetir nada.

**Red directa** (sin gastar buscador):
- **Frieren Wiki (Fandom), API**: `list=categorymembers` sobre
  `Category:Locations` (30+ sitios); `action=parse&prop=wikitext` sobre
  **Official Guide Book**, **Ruins of the King's Tomb**, **Aureole**,
  **Frieren: Beyond Journey's End Season 1/Gallery** y **Season
  2/Gallery** (para las secciones «Concept Art» y «Exhibition
  Illustrations»); `action=query&prop=imageinfo` para tamaños y URL de
  6 imágenes.
- **Descargas directas** (con `curl -A "Mozilla/5.0" -e
  "https://www.fandom.com/"`, medidas con Pillow/`estilo.py`, **vistas
  con Read**): Ruins of the King's Tomb, Rufen Region abandoned fort
  draft, Bier Region ruins draft, Aureole EP4, Aureole concept art, el
  wallpaper del árbol dorado (Wallhaven).
- **`herramientas/investigar_serie.py --wiki frieren --paginas "Royal
  Capital" "Aureole" "Ruins of the King's Tomb" "Lake Korridor" "Heiß"
  "Warm"`**: 111 imágenes enlazadas, 91 grandes → `hoja_01.jpg` y
  `hoja_02.jpg` (copiadas a `hojas/paisajes_01.jpg` y `paisajes_02.jpg`),
  **vistas enteras con Read**.
- **Danbooru API** (`posts.json?tags=sousou_no_frieren+scenery`) y
  **Safebooru API** (mismo tag): 8 resultados cada una, cruzados por
  `md5`/tamaño.
- **Sketchfab API** (`/v3/search?type=models&q=…`): «frieren village»
  (sin resultados), «frieren ruins» (sin resultados), «frieren statue»
  (4 resultados, con Himmel), «medieval fantasy village low poly» (8
  resultados genéricos).
- **ambientcg API** (`/api/v2/full_json?type=Material&q=…`): Grass,
  Moss, Bark, Water, Rock — elegidas Grass001, Bark014, Rock064, Ice002.
- **Wayback Machine** (`archive.org/wayback/available`) para
  `frieren-anime.jp/special/map/`: encontró snapshot pero la descarga
  del snapshot dio «blocked by egress policy» (2 intentos, con y sin
  `http/https`).

**Buscador web** (4 búsquedas de mi cupo de ~50):
- Japonés: «フリーレン展 原画展 background art exhibition Frieren»;
  «フリーレン 聖地巡礼 風景 ロケハン 元ネタ ヨーロッパ».
- Inglés: «"Sousou no Frieren" background art book "美術ボード" OR
  "background art" exhibition 2025»; «Frieren background art real
  Europe inspiration Rothenburg Dinkelsbühl location scouting».

**Fallos y cómo los resolví**:
- `frieren-anime.jp/special/map/`: **Cloudflare** (verificación JS) — no
  hay `navegar.py` disponible en este contenedor (falta el navegador:
  «Executable doesn't exist»); probé la Wayback Machine como plan B y
  también falló (política de red del contenedor) — anotado en «No
  encontré», no insistí una tercera vez.
