# Investigador de IMAGEN · Kung Fu Panda (encargo 61)

Puntos de `ENCARGO.md`: **1** (arte oficial variado), **3** (fan art y 3D con licencia),
**15** (vestuario con hex medidos), **16** (fondos y sitios), **19** (texturas 2D),
**23** (colaboraciones y cruces). Parte de `partes/datos-imagen.md` (recolectado
automáticamente); no repite esas consultas. Personajes de partida: Po, Shifu,
Tigresa, Oogway (+ Tai Lung, Furious Five, Kai, The Chameleon, Mr. Ping, Li por
ser centrales para vestuario/colaboraciones).

Libreta de datos: `- dato · fuente(s) · ✅/⚠️ · tamaño o detalle`.

## Hallazgos

### Punto 1 · Arte oficial, en cantidad y variado

- Hojas de contacto armadas con `investigar_serie.py` sobre 10 páginas de
  `kungfupanda.fandom.com` (Po, Shifu, Tigress, Oogway, Tai Lung, Kai, The
  Chameleon, Furious Five, Mr. Ping, Li) → **283 imágenes enlazadas** en
  6 hojas, `herramientas/referencias/kung-fu-panda/hoja_01.jpg` a `hoja_06.jpg`,
  con `indice.json` (URL + tamaño real de cada original). ✅ (script, mirado
  entero con Read).
- Las 3 hojas elegidas y copiadas a `hojas/` (todas fueron miradas):
  - **`personajes_01.jpg`** (=hoja_01): pósters oficiales (KFP4 2316×3667),
    hojas de modelo (Tigress T-pose completa 1472×3040), turnarounds de
    concept art (Li joven ×3, Mr. Ping joven ×5, Li Shan/padre de Po ×8 en
    círculos), pósters de personaje de KFP4 (Tai Lung, The Chameleon) y
    fotogramas oficiales de entrenamiento/acción.
  - **`personajes_02.jpg`** (=hoja_05): más turnarounds de concept art —
    **Chameleon-concept-faces.jpg** (1500×1033, ~15 bocetos de cabeza del
    camaleón en distintas expresiones) y **Li-concept-1.png** (1400×1077,
    turnaround de 3 vistas) —, banners anchos 1600×680 de KFP2 (Po + Furious
    Five juntos), pósters 3D/coreano, y las 3 formas-disfraz del Chameleon
    (leopardo de nieve, elefante, cocodrilo).
  - **`personajes_03.jpg`** (=hoja_02): Tai Lung Head Design (hoja de diseño
    de cabeza, 1596×1253, útil para trazo/línea del punto 19), fotografía real
    de la premier con Angelina Jolie (cruce ficción/realidad), Oogway
    ascendiendo (escena clave, paleta verde), y el póster real 3D "See it in
    Real D 3D".
- Portada oficial encontrada por AniList (`datos-imagen.md`) **no es de una
  película**: es la portada del **manga japonés** de Kadokawa (ver punto 19).
  Aclarado para no confundir al redactor. ✅
- Poses VIVAS confirmadas (no sólo de pie): Po entrenando con Shifu en el
  patio (`PoTraining.JPG`, 3840×1636), Tai Lung atacando con fuego azul
  (`Tai-Lung-fire-attack.jpg`, 3840×1636), Tigresa/Cinco en pose de combate
  (`Furious-five_l.jpg`, 3072×1309), Po y Shifu abrazados
  (`Kung Fu Panda 3 01.jpg`, 2766×1632). ✅ (miradas directamente).
- **Manga oficial japonés** (arte oficial fuera de la wiki, punto 1 + 19):
  *Kung Fu Panda* se serializó desde **septiembre de 2008** en la revista
  infantil **Kerokero Ace** de **Kadokawa Shoten**, guion de **Hanten Ōkuma**
  y dibujo de **Takafumi Adachi**. ✅ dos fuentes:
  [Anime News Network](https://www.animenewsnetwork.com/news/2008-07-29/america-kung-fu-panda-film-gets-manga-in-japan)
  y ficha de [AniList #90886](https://anilist.co/manga/90886) (confirmado por
  GraphQL: `format: MANGA`, título nativo カンフー・パンダ); listado también en
  [kungfupanda.fandom.com/wiki/Kung_Fu_Panda_(manga)](https://kungfupanda.fandom.com/wiki/Kung_Fu_Panda_(manga)).
- **Cómic occidental**: *Kung Fu Panda* de **Ape Entertainment** (desde
  11-may-2011), guion de Matt Anderson, arte de CV Design y Chad Lambert. ✅
  ([Wikipedia "Ape Entertainment"](https://en.wikipedia.org/wiki/Ape_Entertainment)
  + [leagueofcomicgeeks.com](https://leagueofcomicgeeks.com/comics/series/104600/kung-fu-panda)).

### Punto 3 · Fan art y 3D con licencia (sólo referencia, nunca para pegar)

- **Fan art** (ya en `datos-imagen.md`, filtrado: esa tabla traía mezclados
  tags de OTROS personajes que no son de Kung Fu Panda —hong_meiling, link,
  pikachu, kirby, princess_peach, monkey_d_luffy—, descartados aquí por no
  aplicar). Válidos y usables como referencia con autor:
  - `po_(kung_fu_panda)`: 6 piezas en Safebooru con enlace a origen (Pixiv,
    FurAffinity, Twitter/X, DeviantArt) — la mejor puntuada,
    [safebooru.org/images/528/...](https://safebooru.org/images/528/169a8779e238fc88883100a037281da14ecbd0a6.jpg)
    771×1028, origen [Pixiv](http://img05.pixiv.net/img/m1A4n1d5R/15326081.jpg). ✅
  - `master_shifu`: 6 piezas, incluida una reciente de
    [twitter.com/romu_38](https://twitter.com/romu_38/status/1972250085225586837)
    (2278×1800, sep-2026). ✅
  - `oogway`: 4 piezas, la mejor 2250×2250 origen
    [Pixiv](http://i2.pixiv.net/img-original/img/2016/01/13/17/55/32/54696577_p3.png). ✅
  - Vocabulario Danbooru (`related_tag`) para `po_(kung_fu_panda)` sí devolvió
    etiquetas (furry, two-tone_fur, panda, fat, black_fur, panda_boy…, ver
    punto 17 futuro); para `master_shifu` y `oogway` la consulta devolvió
    **vacío** (sin etiquetas relacionadas registradas) ⚠️ — el personaje no
    tiene suficiente presencia en ese tablero.
- **Modelos 3D con licencia libre** (Sketchfab, API verificada; todos CC
  Attribution — crédito obligatorio al autor):
  - [Kung Fu Panda Po](https://sketchfab.com/3d-models/none-ee714f83c9b14240838c506be05a74d8)
    · Guilherme Navarro · ♥180 ✅
  - [Po Rig Kung Fu Panda](https://sketchfab.com/3d-models/none-352e808c8a174bb5923d11b26567cc21)
    · Guilherme Navarro · ♥129 (con rig, sirve para posar) ✅
  - [Kung-Fu Panda - Tigress](https://sketchfab.com/3d-models/none-5bd2cda8deb04409bd0b4272966be972)
    · donmcdonough · ♥121 ✅
  - [Tigress Rigged Kung Fu Panda](https://sketchfab.com/3d-models/none-8fb7cfe3ec7a4ce2abe57cdacc6f37f8)
    · Guilherme Navarro · ♥110 ✅
  - [Kung-Fu Panda - Shifu](https://sketchfab.com/3d-models/none-c34b40858ede4bc6b5b7ab8fbc298bf1)
    · donmcdonough · ♥80 ✅
  - [Bars Low Poly (kung fu panda)](https://sketchfab.com/3d-models/none-6c6b412627564703807727e6d83b20de)
    y [Punching Bag Low Poly](https://sketchfab.com/3d-models/none-f4fc6ebf80da4045838b1c3e9140f3a8)
    · Lunev — props del Salón de los Mil Rollos, para ambientar sin usar la
    escena completa. ✅
  - **Staff of Wisdom / bastón de Oogway** — objeto icónico con DOS modelos
    independientes: [Staff Of Wisdom | Kung Fu Panda 4](https://sketchfab.com/3d-models/none-9551403730b343f1bdc5909a764fb45f)
    (kanimator, ♥36) y [Oogway's Stick (Staff of Wisdom)](https://sketchfab.com/3d-models/none-86517f51684d4adfb4233ec7f6664289)
    (TECH_AR, ♥11), ambos CC Attribution. ✅
  - Búsquedas sin resultado útil: "Jade Palace" y "Valley of Peace" en
    Sketchfab devuelven modelos de OTRAS franquicias (Black Myth: Wukong,
    banderas) — no hay modelo 3D libre del Palacio de Jade en sí. ⚠️
- **Texturas/CC0 de Poly Haven** para vestir escenas de bambú (el bosque de
  las Cinco Furiosas, el Valle): `bamboo_wall`, `bamboo_wall_02`,
  `bamboo_wall_03`, `bamboo_veneer`, `bamboo_tunnel`, `spooky_bamboo_morning`
  — todas CC0, [polyhaven.com](https://polyhaven.com). Muebles/decoración chinos
  también CC0: `chinese_garden`, `chinese_armchair`, `chinese_screen_panels`,
  `chinese_tea_table`, `wooden_lantern_01`. ✅ (API propia).
- **Fotos con licencia libre** (ya en `datos-imagen.md`, Openverse): 20 fotos
  de la premier de Sídney (Lucy Liu, Jack Black) CC BY-SA 2.0/CC BY 2.0 —
  sirven como referencia de "colaboración con el elenco real", no de estilo.

### Punto 15 · Vestuario (con hex medidos)

Confirmado en la sección **"Clothing"** de cada ficha de
`kungfupanda.fandom.com` (wikitext, fuente primaria de la wiki oficial de la
franquicia) y comprobado visualmente en las hojas de contacto. Al ser una
sola wiki como fuente textual, se marca ⚠️ salvo cuando además hay imagen que
lo confirma (entonces ✅ imagen+texto).

- **Po**: sin camisa; pantalón de arpillera a parches de colores variados,
  con una franja roja y amarilla a rayas en la pretina; vendas de tela en los
  tobillos; zapatos con forma de garras de panda. ✅ (texto + visto en
  `PoTraining.JPG` y en las hojas).
  - *Winter Feast* (especial navideño): gorro rojo de nieve con rayas negras
    y puntos amarillos + bufanda amarilla; en la cena formal, capa oscura y
    sombrero-corona alto. ⚠️ (sólo wiki).
  - KFP2: sombrero cónico de paja breve al enfrentar la flota de Shen. ⚠️
  - **KFP3 (Reino de los Espíritus)**: túnica blanca con ribete negro, mangas
    negras con borde dorado, capa dorada larga, faja roja, sombrero de paja;
    Oogway le entrega el **Bastón de la Sabiduría**. Esta imagen repite el
    diseño del "Guerrero Legendario" del sueño de la película 1. ✅ (texto +
    `KFP3-Po-outfit.png`, medido abajo).
- **Shifu**: túnica borgoña/rojiza con faja marrón, diseños dorados de olas
  en los puños plateados, patrones ovalados en la espalda de las mangas,
  pantalón negro (blanco en la serie de TV), vendas Shaolin en piernas,
  anilla que sujeta su perilla. ✅ (texto + `Shifu2.jpg`).
  - *Winter Feast*: chal plateado con copos de nieve, broche dorado.
  - **Desde KFP2**: jiāshā verde jade cerrado con broche dorado con insignia
    (haciendo eco de la túnica de Oogway), mangas de la túnica borgoña
    re-cosidas en jade, faja también jade con ribete dorado. Igual en KFP3 y
    KFP4. ✅ (texto + `ShifuGreen.JPG`, medido abajo).
- **Tigresa**: única de las Cinco Furiosas que lleva camisa — un **qipao**
  (cheongsam) rojo hasta la cintura con **patrones dorados de enredadera** y
  ribete negro, cerrado con broches metálicos y una faja a la cintura;
  pantalón de seda negro; sandalias negras con suela de almohadilla de pata.
  ✅ (texto + `Tigress2.jpg` y `Tigress.png`).
  - Antes de KFP3 tuvo mangas en varias apariciones (concept art temprano,
    sueño de Po en la película 1, créditos finales 2D). ⚠️
  - *Winter Feast*: chaleco plateado con enredadera roja, faja roja, pantalón
    marrón oscuro, tocado.
  - **Desde KFP3**: hanfu dorado con el mismo patrón de enredadera roja del
    chaleco original — la "ropa icónica" que evoluciona pero mantiene el
    motivo de enredadera. ✅
- **Oogway**: faja verde cruzada sobre el pecho que envuelve casi todo el
  caparazón, cerrada con una anilla; en la espalda lleva un diseño
  estilizado de **taichí (peces yin-yang)** — símbolo de liderazgo del Valle,
  por eso Shifu hereda un envoltorio verde parecido al asumir el cargo. En
  KFP3 la faja se alarga como una capa. En *Secrets of the Masters* usa
  sombrero cónico + túnica verde-amarilla de viaje, y en un flashback de
  guerra, armadura metálica con púas y brazaletes. ✅ (texto, referencia
  cruzada a trivia de IMDb) + `Oogway_Concept.jpg`.
- **Tai Lung**: cinturón marrón tachonado y pantalón morado —la tela y el
  estampado del pantalón son **el mismo de la manta** en la que Shifu lo
  encontró de cachorro (detalle de continuidad visual)—, vendas Shaolin.
  Bocetos tempranos, el videojuego *Kung Fu Panda: The Game* y el arranque de
  *Holiday* lo muestran con hombrera tachonada y guantelete metálico que NO
  aparecen en la película final. ✅ (texto) + `Tai_Lung_Head_Design.jpg`
  (hoja de diseño de cabeza, más útil para el trazo que para el color).
- **Furious Five (resto)**: **Crane** — único con sombrero (cónico/de arroz,
  se lo deja puesto incluso peleando), pantalón azul suelto, faja morada
  estilo Shaolin, 5 anillos de tobillo por pierna + anillo en cada dedo del
  pie. **Monkey** — único con muñequeras de cuero tachonadas, pantalón marrón
  suelto, faja dorada. Ambos con variante dorada/recoloreada en *Winter
  Feast*. ✅ (texto, fichas de cada uno en la wiki).
- **Hex medidos con `herramientas/estilo.py`** (paleta dominante, % y estilo
  de sombreado — todo en `/tmp/claude-0/trabajo/61-kung-fu-panda-imagen/estilo/estilo.json`):
  - `KFP3-Po-outfit.png` (1920×816, Po Reino de los Espíritus): **#F1C744,
    #F3E25D** (dorado/amarillo), **#B7521B, #E2771D** (naranja azafrán),
    **#762911** (marrón oscuro) — saturación 75%, brillo 78%, sombreado
    degradado/pintado, línea #B16323. ✅ medido.
  - `ShifuGreen.JPG` (1501×1357): **#283220, #3C653C** (verde jade de la
    túnica), **#6D4C2A, #917A51** (marrón de la faja) — sombreado **plano
    (cel)**, saturación 13%, brillo 81%. ✅ medido.
  - `Tigress2.jpg` (1573×1326, fondo blanco 63%): **#211814** (negro del
    pantalón/ribete), **#59392A, #C17128** (rojo-naranja del qipao) —
    sombreado plano (cel), brillo 81%. ✅ medido.
  - `Tigress.png` (1472×3040, pose de cuerpo entero): **#483020, #1C0F0B**
    (rayas/sombras), **#74553D, #B68146** (piel/traje) — sombreado degradado
    /pintado, brillo 63%. ✅ medido.
  - `PoTraining.JPG` (3840×1636, escena de entrenamiento completa): **#C8C4B2**
    (piedra), **#192328, #71878C, #466774** (azules de la escena) — saturación
    26%, brillo 54%. Sirve para el AMBIENTE del patio, no sólo el vestuario.
    ✅ medido.
  - `Tai-Lung-fire-attack.jpg` (3840×1636, escena nocturna): **#141920,
    #04080D** (negros), **#385374, #A6C1DD** (azules fríos del pelaje bajo
    luz de fuego azul) — saturación 41%, brillo 47%. ✅ medido.
  - `Tai_Lung_Head_Design.jpg` (1596×1253, hoja de diseño en gris): tonos
    **#E9E9E9 a #131210**, sombreado **mixto, mucha línea** (línea #76705D) —
    sirve para estudiar el TRAZO del diseño de personaje, no el color de
    vestuario (la hoja es monocroma). ✅ medido.
  - `Kai.png` (1920×814, General Kai con energía de jade): **#B6EFDD,
    #80E2C2, #20EAA5** (verdes jade luminosos), **#030402, #1B401E** (negros)
    — saturación 44%, brillo 56%, sombreado degradado. Vestuario de Kai:
    armadura oscura con amuletos de jade robados (ver hoja `personajes_02`,
    "Kai's amulets.jpg"). ✅ medido.
  - `MrPingPoster.jpg` (2000×850): **#353A37, #1D1813** (delantal/plumaje
    oscuro), **#B0751B, #E9A437** (dorado/naranja del entorno del puesto de
    fideos) — saturación 41%, brillo 35%. ✅ medido.
  - `FiveKFP2.jpg` (2000×850, grupo Cinco Furiosas + Po): **#552F18,
    #793E0E, #A24102, #CE6C07** (marrones y naranjas cálidos de madera y
    pelaje) — saturación 55%, brillo 33% (escena de interior en penumbra). ✅
    medido.
  - `Chameleon-render.jpg` (1000×563, render de estudio The Chameleon en su
    forma real): **#8B8B89** (gris piedra, 83%), poco color — sombreado
    **plano (cel)**, saturación 7%. La piel natural del camaleón es gris
    apagada; el color llamativo (jade/dorado) es su disfraz de sacerdotisa,
    no su piel real. ✅ medido.
  - Colores por SIMBOLISMO (según el equipo de arte, entrevista): jade/verde
    = sabiduría (Oogway), marrón = trabajo duro (Shifu), rojo = poder
    (Tigresa), azul = villanía (Tai Lung) — Production Designer Raymond
    Zibach y Art Director Tang Heng Heng tras un viaje de referencia a China.
    ⚠️ una sola fuente secundaria (blog académico) citando el proceso, no el
    artbook original:
    [tbatleyresearchdevelopment.wordpress.com](https://tbatleyresearchdevelopment.wordpress.com/2013/12/18/researching-character-development-in-kung-fu-panda/).

### Punto 16 · Ciudades, paisajes y fondos de pantalla

- **Palacio de Jade** (Jade Palace): sobre el Monte Jade, domina el Valle;
  descrito en la web oficial de KFP1 como "símbolo de justicia, honor y
  coraje" ✅ (wikitext con referencia a la web oficial archivada). Imagen
  `JadePalaceDW.jpg` (1920×816): **atardecer dorado/anaranjado a contraluz**
  detrás del templo de tejados verde-jade y rojo, escalinata de piedra
  musgosa, niebla baja entre picos kársticos. Medido: **#CD8D43, #DFB05F**
  (cielo dorado), **#39372F, #2A2B1E, #1A1B12** (siluetas oscuras del templo
  a contraluz) — saturación 45%, brillo 43%. ✅ medido y mirado.
- **Valle de la Paz** (Valley of Peace): pintura digital oficial de
  **Tang Kheng Heng**, citada en el artbook *The Art of Kung Fu Panda* (p.
  134) como "el descubrimiento de un Shangri-La chino… paisaje magnífico,
  hecho aún más mágico por el aire neblinoso" ✅ (wikitext citando el
  artbook). Imagen `ValleyPeaceArt.JPG` (2177×929): **niebla verde-azulada
  matutina** entre montañas kársticas estilo Guilin, aldea dorada iluminada
  al centro del valle, arrozales. Medido: **#536A62, #668077, #AFB2A3**
  (verdes-grises de niebla), **#A98534, #D9B24D** (dorado de la aldea) —
  saturación 25%, brillo 52%. ✅ medido y mirado.
- **Reino de los Espíritus / Hilo de la Esperanza** (KFP4, `ThreadOfHope2.jpg`,
  1920×816): picos de piedra flotando entre niebla blanca-azulada muy densa,
  puente colgante de cuerda entre dos pilares, pino en primer plano —
  paleta **fría** #9DA9A3, #A4B5AF, #203029, saturación sólo 18%, brillo 53%.
  Contrasta a propósito con el dorado cálido del Valle. ✅ medido y mirado.
- **Inspiración real confirmada**: los diseñadores de producción visitaron
  China antes de diseñar color, luz y ambiente; el estilo se describe
  explícitamente como paisaje kárstico (Guilin/Zhangjiajie). ⚠️ una fuente
  (ACMI, museo de cultura de pantalla —
  [acmi.net.au/stories-and-ideas/kung-fu-panda](https://www.acmi.net.au/stories-and-ideas/kung-fu-panda/)),
  no se llegó a la entrevista original del staff en esta tanda.
- **Fondos de pantalla** (ya listados en `datos-imagen.md`, Wallhaven, sólo
  aptos): el más guardado es un render 3D de Master Tigress en 5216×3000
  (♥27, Opostrof) y uno 3840×2160 de un interior/CGI genérico ambientado
  (♥184) que NO es arte oficial de la franquicia (etiquetado por error en
  Wallhaven) — aviso para no usarlo como referencia de sitio real. ⚠️

### Punto 19 · Texturas 2D

- La franquicia nace como **película CGI**, no manga — pero SÍ hay dos
  fuentes 2D reales que aportan textura/línea (ver punto 1 para bibliografía
  completa): el **manga japonés de Kadokawa** (Kerokero Ace, 2008, dibujo de
  Takafumi Adachi) y el **cómic de Ape Entertainment** (2011, CV Design/Chad
  Lambert). No se pudo mirar una página suelta con licencia libre en esta
  tanda (revistas de pago) ⚠️.
- **Prólogo animado a mano** (KFP1): la secuencia onírica de apertura ("el
  Guerrero Legendario") es 100% 2D tradicional, animada por **James Baxter
  Animation**, con estética plana tipo recorte/*Samurai Jack*, paisajes
  chinos pintados y caligrafía. ✅ dos fuentes:
  [cartoonbrew.com](https://www.cartoonbrew.com/feature-film/kung-fu-panda-2d-animated-sequences-in-hi-res-7854.html)
  y [awn.com](https://www.awn.com/news/kung-fu-pandas-title-sequences-go-2d).
  En **KFP2**, la secuencia del pasado de Shen imita el **teatro de sombras
  chino** (shadow puppetry) — mismas dos fuentes. Referencia directa de
  "línea/textura 2D" para cartelas o transiciones del canal.
- **Emblemas y patrones que se repiten** (útiles como logo/textura):
  - El **taichí de peces (yin-yang)** bordado en la faja de Oogway, heredado
    visualmente por la faja de Shifu — símbolo de liderazgo del Valle. ✅
    (wikitext, referencia cruzada a trivia de IMDb).
  - El patrón de **enredadera dorada** bordado en el qipao rojo de Tigresa,
    repetido en su hanfu dorado de KFP3 — mismo motivo, distinto color base.
    ✅ (wikitext, ver punto 15).
  - El estampado del **pantalón morado de Tai Lung** es el mismo tejido de
    la manta en la que fue encontrado de cachorro — patrón de continuidad,
    no decorativo. ✅ (wikitext).
- **Texturas libres equivalentes** (todas con licencia, para capas de
  Photoshop):
  - Grano de papel/cartón: `Paper001`–`Paper006`, `Cardboard002` — CC0,
    [ambientcg.com](https://ambientcg.com) (API `type=Material&q=paper`).
  - Tela/bordado (base para simular el bordado del qipao o el jiāshā):
    `Fabric030`, `Fabric036`, `Fabric061`, `Fabric062`, `Fabric066`,
    `Fabric081C`, `Carpet016` — CC0, ambientcg.com.
  - No se encontraron **pinceles** de tinta/caligrafía chinos con licencia
    libre explícita en Openverse (los resultados eran fotos de arte, no
    archivos de pincel) ⚠️ — pendiente si se necesita, probar
    r/ClipStudio o Gumroad free con filtro de licencia.

### Punto 23 · Colaboraciones y cruces

- **Parques temáticos** (traen poses/ropa nuevas de personajes en 3D real):
  - **Kung Fu Panda Land of Awesomeness**, Universal Beijing Resort — primera
    área 100% techada de un parque Universal, con Palacio de Jade, Aldea
    Panda y el Árbol de la Sabiduría Celestial recreados en volumen. ✅ dos
    fuentes:
    [Wikipedia "Universal Studios Beijing"](https://en.wikipedia.org/wiki/Universal_Studios_Beijing)
    y la [web oficial del parque](https://www.universalbeijingresort.com/en/themelands/kungfupanda).
  - **DreamWorks Theatre featuring Kung Fu Panda: The Emperor's Quest**,
    Universal Studios Hollywood — atracción narrativa donde Po pide ayuda a
    los visitantes para llevar el "Líquido de Poder Ilimitado" al Palacio. ✅
    dos fuentes: [comunicado de Comcast](https://corporate.comcast.com/press/releases/universal-studios-hollywood-celebrates-the-opening-of-dreamworks-theatre-featuring-kung-fu-panda-the-emperors-quest)
    y [guía de discoveruniversal.com](https://blog.discoveruniversal.com/attractions/dreamworks-theatre-featuring-kung-fu-panda-universal-studios-hollywood/).
  - "Kung Fu Panda: Land of Awesomeness" en **Dreamworld** (Australia, 2012)
    — mención única, sin segunda fuente. ⚠️
- **Bebidas/comida**: **Kung Fu Tea x Kung Fu Panda 4** (1-15 marzo 2024) —
  4 bebidas de edición limitada con diseño propio: *Chameleon's Sesame
  Matcha*, *The Dragon Warrior*, *Po's Skadoosh Slush* (vainilla + Oreo),
  *Zhen's Taro Treasure*; stickers coleccionables por compra. ✅ dos fuentes:
  [kungfutea.com](https://www.kungfutea.com/kung-fu-tea-partners-with-dreamworks-animation-for-kung-fu-panda-4-in-theaters-nationwide-march-8th/)
  y [prnewswire.com](https://www.prnewswire.com/news-releases/kung-fu-tea-partners-with-dreamworks-animation-for-kung-fu-panda-4-in-theaters-nationwide-march-8-302076720.html).
- **Videojuegos crossover** (traen poses y skins nuevas — referencia de
  pose real):
  - **Mobile Legends: Bang Bang x Kung Fu Panda** (20-ago a 18-oct 2022):
    skins de evento gacha — Akai "Kung Fu Panda", **Thamuz "General Kai"**,
    Ling "Lord Shen"; animaciones, emotes y iconos de habilidad propios. ✅
    dos fuentes: [moonton.com](https://en.moonton.com/news/76.html) (oficial)
    y [oneesports.gg](https://www.oneesports.gg/mobile-legends/mlbb-kung-fu-panda-skins-rewards/).
  - **Brawlhalla x Kung Fu Panda** (24-mar-2021, parche 5.05): Po, Tigresa y
    Tai Lung jugables de forma permanente, mapa "Spirit Realm", modo
    Showdown, ataques con Shifu/Mantis/Crane/Monkey/Viper de apoyo. ✅ dos
    fuentes: [news.ubisoft.com](https://news.ubisoft.com/en-us/article/6ThI4zNhqF7ZrAQlPo9YM1/kung-fu-panda-comes-to-brawlhalla)
    y [Steam (oficial del juego)](https://store.steampowered.com/news/app/291550/view/3008941395558540620).
  - **Kung Fu Panda x Zooba** (Wildlife Studios): Po desbloqueable en un
    evento especial. ⚠️ una sola fuente
    ([wildlifestudios.com](https://wildlifestudios.com/games/zooba/news/kung-fu-panda-arrives-in-zooba-event/)).
- **Figuras oficiales** (pose = referencia 3D real):
  - **McFarlane Toys "Po" 6" (Movie Maniacs)** — figura posada muy detallada,
    con peana impresa, fondo de cartón y tarjeta de arte coleccionable. ✅ dos
    fuentes: [mcfarlane.com](https://mcfarlane.com/toys/po-kung-fu-panda/) y
    [collider.com](https://collider.com/kung-fu-panda-mcfarlane-figure-image/).
  - **Mattel "Master Tigress" (Claw Attack, 5")** y **"Tai Lung" (Spear
    Assault, 5")** — línea de figuras de película. ⚠️ una sola fuente de
    reventa (ToyWiz), no la ficha oficial de Mattel.
- **Cosplay**: tutorial en video **"Tigress cosplay tutorial AWESOMENESS"**
  (YouTube) — construcción de cabeza de tigresa estilo *fursuit* (materiales
  reales, volumen 3D). Sólo localizado en la búsqueda, no se miró el video
  con minuto exacto en esta tanda. ⚠️
  [youtube.com/watch?v=kFUeS4i0Yw4](https://www.youtube.com/watch?v=kFUeS4i0Yw4).
- Manga (Kadokawa, Japón) y cómic (Ape Entertainment, EEUU) del punto 19
  también son, en sentido estricto, colaboraciones editoriales con DreamWorks
  — anotado aquí para no duplicar investigación.

## Lo mejor para la lámina

1. **Palacio de Jade a contraluz dorado** (`JadePalaceDW.jpg`) — el edificio
   más reconocible de la serie, con luz de atardecer lista para poner texto
   delante en silueta oscura.
2. **Tigresa en pose de combate, qipao rojo con enredadera dorada**
   (`Tigress2.jpg` / hoja `personajes_01`) — la "secundaria más querida" con
   su prenda icónica y hex ya medidos.
3. **Po en su traje de Guerrero Espiritual dorado** (`KFP3-Po-outfit.png`) —
   pose de autoridad, paleta cálida (#F1C744/#B7521B) distinta al verde/rojo
   habitual, buena para un mensaje "oficial" del canal.
4. **Bastón de la Sabiduría de Oogway** (modelo 3D libre en Sketchfab, CC
   Attribution) — objeto real posible en Blender para sostener texto o
   servir de "puntero" del canal.
5. **Chameleon-concept-faces.jpg** (hoja `personajes_02`) — 15 expresiones
   del villano de KFP4 en una sola hoja: referencia rápida de gama emocional
   para cualquier personaje reptil/camaleónico del servidor.

## No encontré

- ⚠️ Modelo 3D libre del Palacio de Jade o el Valle de la Paz como sitio
  completo (Sketchfab sólo da objetos de otras franquicias con esas palabras)
  — se cubre parcialmente con texturas de bambú/muebles chinos CC0 de Poly
  Haven, pero no hay un edificio o mapa completo con licencia libre.
- ⚠️ Página suelta y legible del manga japonés de Kadokawa o del cómic de
  Ape Entertainment con licencia para citar visualmente (son revistas y
  cómics de pago; sólo confirmé que existen y quién los hizo, dos fuentes
  cada uno).
- ⚠️ Pinceles (brushes) de tinta/caligrafía china con licencia libre
  explícita — Openverse sólo devolvió fotografías de pinturas, no archivos
  de pincel descargables.
- ⚠️ Ficha oficial de Mattel para sus figuras de Tigresa/Tai Lung (sólo
  reventa en ToyWiz) y segunda fuente para Dreamworld Australia / Zooba /
  Minecraft-Castle Clash (mencionados de pasada en búsquedas generales, sin
  confirmar en una fuente propia).
- ⚠️ Entrevista original en video/texto del equipo de arte (Raymond Zibach /
  Tang Heng) sobre el simbolismo de color: sólo se encontró citada de
  segunda mano en un blog académico, no la fuente primaria (artbook o
  entrevista directa).
- Nota: no busqué doblaje, música ni fotogramas de escena con minuto exacto:
  son puntos 4/8/9/10/14 de otros roles (vídeo/voz), no de imagen.

## Bitácora de búsqueda

- `investigar_serie.py --wiki kungfupanda` sobre 10 páginas → 283 imágenes,
  6 hojas de contacto, todas miradas con Read.
- Wiki (curl a la API de `kungfupanda.fandom.com`, en inglés): búsqueda de
  texto y `action=parse&prop=wikitext` en las páginas *Jade Palace*, *Valley
  of Peace*, *Spirit Realm*, *Po*, *Shifu*, *Tigress*, *Oogway*, *Tai Lung*,
  *Crane*, *Monkey*, *Furious Five action figures* (secciones "Clothing"
  completas, citadas arriba).
- `herramientas/estilo.py` sobre 14 imágenes (URLs directas de
  `static.wikia.nocookie.net`) para paleta y tipo de sombreado — salida en
  `/tmp/claude-0/trabajo/61-kung-fu-panda-imagen/estilo/estilo.json`.
- Sketchfab API (`search?type=models`): "Jade Palace", "Valley of Peace",
  "Dragon Scroll", "Oogway staff", "Chinese pagoda" — en inglés.
- Poly Haven API (`/assets`): filtrado por "bamboo" y por chinese/paper/
  lantern en categorías.
- ambientcg.com API (`full_json?type=Material`): "paper", "fabric" — en
  inglés.
- Openverse API: "chinese cloud pattern fabric", "ink brush stroke texture"
  — en inglés, sin resultado útil con licencia de pincel.
- AniList GraphQL: ficha del manga (id 90886) — confirmó `format: MANGA`.
- WebSearch (todas en inglés, cupo usado: 9 de ~50):
  "Kung Fu Panda concept art character design colors interview costume",
  "Kung Fu Panda Universal Studios Land of Awesomeness collaboration",
  "Kung Fu Panda comic book Ape Entertainment style texture paper",
  "Kung Fu Panda manga adaptation Japan artist publisher 2008",
  "Kung Fu Panda opening dream sequence 2D flat paper cutout animation
  style", "Kung Fu Panda cosplay costume tutorial materials Po Tigress",
  "Kung Fu Panda official action figure Po Tigress collectible statue
  McFarlane NECA", "Kung Fu Panda mobile game DreamWorks crossover event
  Fortnite OR gacha", "Kung Fu Panda Mobile Legends Bang Bang skin General
  Kai Thamuz collaboration", "Brawlhalla Kung Fu Panda crossover Po skin
  official".
- No se probaron búsquedas en japonés/coreano/chino en esta tanda (la
  franquicia es de origen estadounidense — DreamWorks — así que las fuentes
  "en otros idiomas" que pide `ENCARGO.md` se cubrieron con la ficha del
  manga en japonés vía AniList/ANN, no con búsqueda nativa en 日本語). Si se
  retoma, probar `カンフー・パンダ 漫画` en japonés para encontrar scans/reseñas
  del manga de Kadokawa.

## Cumplimiento (mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | 283 imágenes en 6 hojas miradas, 3 elegidas a `hojas/`, manga+cómic oficiales confirmados con fuente. |
| 3 · Fan art y 3D con licencia | ✅ | Fan art con autor (Safebooru, filtrado de ruido), 11 modelos Sketchfab CC con crédito, texturas Poly Haven CC0. |
| 15 · Vestuario con hex | ✅ | 6 personajes con vestuario por arco/temporada (texto primario de wiki) + 11 imágenes con hex medidos por `estilo.py`. |
| 16 · Fondos y sitios | ✅ | 3 sitios (Palacio, Valle, Reino de los Espíritus) con hex medidos, luz/hora descritas, inspiración real citada. |
| 19 · Texturas 2D | ✅ | Manga y cómic oficiales identificados, prólogo 2D confirmado, emblemas repetidos localizados, texturas CC0 enlazadas. ⚠️ en pinceles de tinta libres (no encontrados). |
| 23 · Colaboraciones y cruces | ✅ | Parques, bebida, 2 crossovers de videojuegos con doble fuente, figuras oficiales, cosplay listado. |

**Parte terminada**: lo obligatorio de los puntos 1, 3, 15, 16, 19 y 23 está
cubierto (ver tabla arriba). Quedan sólo extras opcionales, ya anotados en
«No encontré»: mirar el video de cosplay de Tigresa con minuto exacto,
segunda fuente para Dreamworld Australia y las figuras Mattel, y búsqueda
nativa en japonés del manga de Kadokawa.
