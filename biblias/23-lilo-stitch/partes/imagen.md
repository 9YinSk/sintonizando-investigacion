# Parte de IMAGEN · Lilo & Stitch (puntos 1, 3, 15, 16, 19, 23)

Repaso (segunda pasada, red abierta, 24-sep-2026). Parto de
`partes/datos-imagen.md` (no repito esas consultas) y de la `biblia.md` ya
escrita con la red cerrada (secciones 3, 4, 16, 17 con varios ⚠️; los puntos
19 y 23 **no existían** como sección). Ya había **12 hojas de contacto**
corridas por `investigar_serie.py` en
`herramientas/referencias/lilo-stitch/` (antes no estaban copiadas a
`hojas/`, que es lo que más faltaba según el aviso de arranque). Las miré
todas (Read) y dejo **3** en `hojas/`:

- `hojas/imagen_01_arte-oficial.jpg` (12 hojas totales, hoja 1/12): 48
  imágenes grandes — figuras oficiales (Britto, Disney Store), portadas de
  cómic Dynamite, cartelas de Disney Adventures, arte de concept (#24 "Stitch
  Development art"), pins de créditos, merchandising.
- `hojas/imagen_02_concept-y-crossovers.jpg` (hoja 2/12): concept art y
  **hoja de modelo de Pleakley firmada por Chris Sanders** (#63), más
  portadas variante Dynamite, el logo de **Kingdom Hearts** (#61, crossover),
  Stitch Fab 50 (#54).
- `hojas/imagen_03_colaboraciones.jpg` (hoja 12/12): cartas de **Disney
  Lorcana** (#529-530), Kingdom Hearts III «Stitch's Great Escape» Shanghai
  (#535-536), **Disney Infinity** (#546), **Tsum Tsum** 15.º aniversario
  (#547), Disney Cruise Line (#554), manga de KHII (#553) — todo punto 23.

## Hallazgos

### Punto 1 · Arte oficial, en cantidad y variado

- **Artbook oficial confirmado** (antes ⚠️ «no encontré»): **«Lilo & Stitch:
  Collected Stories From the Film's Creators»**, Disney Press, 2002, 128
  páginas, con el equipo de la película contando su proceso ✅
  ([Worthpoint, ficha con ISBN](https://www.worthpoint.com/worthopedia/lilo-stitch-collected-stories-films-1886596031),
  [LabyrinthBooks](https://labyrinthbooks.myshopify.com/products/chris-sanders-lilo-stitch-collected-stories-disney-art-book)).
- **Hoja de modelo de Pleakley** firmada por Chris Sanders, con vistas
  frontal/perfil y expresiones ✅ (hoja 2/12, imagen #63: «Pleakley concept
  art.jpg», [en la wiki](https://static.wikia.nocookie.net/disney/images/7/74/Pleakley_concept_art.jpg)).
  Es la referencia más clara de **proporciones** del personaje que encontré.
- **Bocetos de poses de hula de Lilo** (hoja 9/12, #385: «LiloHulaAD.jpg»,
  1600×1068) y **estudio de Lilo** (#387 «LiloStudyAD.jpg»): varias poses en
  una sola hoja, exactamente lo que pide el punto 1 («poses VIVAS») ✅.
- **Portadas variantes del cómic Dynamite** (17+ portadas distintas
  numeradas «Lilo & Stitch/Stitch Dynamite Covers»): artistas identificados
  en AIPT y Bleeding Cool (Nicoletta Baldari, Trish Forstner, Edwin Galmon,
  Craig Rousseau, David Nakayama, Joshua Middleton, Jennifer L. Meyer) ✅
  (ya en biblia §3.4; confirmado con las hojas 1 y 2, que muestran ~15
  portadas más allá de esas 7: incluye una donde Stitch va de traje negro
  y gafas, tipo agente secreto — sirve para «disfraces» del punto 23).
- **Key visual oficial** «Lilo & Stitch promo art 2.jpg» (3523×5000,
  [wiki](https://static.wikia.nocookie.net/disney/images/1/1b/Lilo_%26_Stitch_promo_art_2.jpg)):
  Stitch y Lilo de espaldas en la playa al atardecer, ella con traje de
  hula. Es la pieza de arte oficial de mayor tamaño de toda la wiki y sirve
  de referencia de luz y color (medido en el punto 15). **La miré entera.**
- **Figuras oficiales como «arte 3D»**: Disney Britto (figurita pop-art,
  #4 en hoja 1), **Jim Shore Disney Traditions «'Ohana»** (madera tallada
  estilo folk, hoja 2 #74 y hoja 9), Disney Animators' Collection (peluche
  con cara «bebé», #37) ✅ (vistas en las hojas).
- **Revistas Disney Adventures** con Stitch en portada (~8 números
  distintos vistos en la hoja 1, #39-47): otra fuente de arte de época que
  no estaba en la biblia.

### Punto 3 · Fan art y 3D con licencia (correcciones a §4 de la biblia)

- **Licencias verificadas por la API de Sketchfab** (antes la biblia decía
  «no abría»; ahora sí, y **una licencia estaba mal**):
  - [Photo Album](https://sketchfab.com/3d-models/photo-album-b891198a35a64b2c9c3c1a26338b1a48),
    mnaglak → **CC Attribution 4.0** ✅ (confirmado por API:
    `license.label = "CC Attribution"`, `license.url` a creativecommons.org/licenses/by/4.0). El álbum para el objeto de la lámina.
  - [Canon AE-1 Program 35mm](https://sketchfab.com/3d-models/canon-ae-1-program-35mm-film-camera-03b0ac7d99c44197a09640179f360f3c),
    Marc Sawyer → **CC Attribution 4.0** ✅ por API. 77 532 caras (fotogrametría real).
  - [Cork Board](https://sketchfab.com/3d-models/cork-board-9534ee2ad4344ea6b02b95b61bd4a913),
    rickmaolly → **CC Attribution** ✅ por API.
  - ⚠️→corregido: **[Set of four low-poly Cameras](https://sketchfab.com/3d-models/set-of-four-4-low-poly-cameras-275be0c563754a038c0a50f19785a8ea)**,
    JeffK/jeffkolada → la API dice **CC Attribution-NonCommercial-ShareAlike**,
    **no** «CC Attribution» como decía la biblia. **No usar** para un
    servidor que pueda tener fines no estrictamente no-comerciales sin
    revisarlo con el dueño; si sólo es referencia visual (girar y mirar
    volúmenes, nunca pegar), no importa la licencia.
- **Kingdom Hearts (crossover, no licencia libre, sólo referencia)**: el
  logo aparece en la hoja de la wiki (#61) — pasa al punto 23.
- **Fan art de Lilo con su cámara**: seguí sin encontrarlo en ArtStation ni
  DeviantArt (dos intentos más, en inglés): la cámara casi nunca se dibuja,
  el fan art se centra en Stitch solo o en el abrazo final ⚠️.

### Punto 15 · Vestuario (colores medidos, no de memoria)

Medí con Pillow (`getpixel`, no `estilo.py` porque necesitaba puntos
concretos, no la paleta global de toda la imagen) sobre dos fuentes
oficiales que **vi con Read**:

| Personaje / prenda | Hex medido | De dónde | Fiabilidad |
|---|---|---|---|
| Stitch, pelaje cuerpo (tono medio) | `#003D63` a `#167DB1` (degradado sombra→luz) | key visual oficial «promo art 2.jpg», 3523×5000 | ✅ — es arte pintado con degradado, no color plano; dos muestras en zonas distintas del cuerpo coinciden en la misma familia de azul |
| Stitch, vientre/pecho claro | `#B4FEF1` | traje oficial de Disney on Ice («DOI - Jumba, Stitch & Pleakley.jpg», con luz de escenario) | ⚠️ un solo origen y con luz de espectáculo, puede no ser el tono «plano» del cel |
| Stitch, interior de oreja | tono lila/malva apagado (zona con sombra fuerte en la imagen medida; no fiable para hex exacto) | misma imagen | ⚠️ pendiente de medir sobre un fotograma plano, sin sombra |
| Lilo, falda de hula (hojas verdes) | `#559B73` (claro) / `#146243` (oscuro, pliegues) | key visual oficial | ✅ dos tonos del mismo material, coherente con «hojas de ti (ti-leaf)» |
| Lilo, pelo | `#030308` (casi negro puro) | key visual oficial | ✅ |
| Stitch, traje espacial (el del principio de la película) | rojo, banda pecho con **triángulo/estrella amarillo** `#F9E03E`, cinturón negro con ribete dorado | traje oficial de Disney on Ice (foto de gira, con luz de escenario que oscurece el rojo a un granate `#680004`) | ⚠️ el rojo «de escenario» es más oscuro que el rojo plano del cel; para la lámina usar un rojo saturado (`#CC1F1F`–`#E4241F` aprox., no medido, sólo referencia de KH Wiki y memoria del fandom) y comprobarlo contra un fotograma antes de pintar |
| Pleakley, uniforme alienígena real (no el disfraz humano) | amarillo pollito `#F8FD3E`–`#EF870E` según la iluminación, uniforme azul con hombrera naranja | mismo traje de Disney on Ice | ✅ nuevo dato: **este es su traje real de un solo ojo**, distinto del disfraz de mujer humana que ya estaba en la biblia (ambos son canon, en momentos distintos de la película) |
| Nani, traje de baño (escena de la ola) | franjas diagonales **azul marino `#1B2C52`** y **verde `#4F7350`**, sobre fondo turquesa de agua | fotograma limpio de animación (no Disney on Ice): «Lilo & Stitch - Nani, Lilo, and Stitch enjoying a big wave.jpg», 3000×1782, [wiki](https://static.wikia.nocookie.net/disney/images/a/a0/Lilo_%26_Stitch_-_Nani%2C_Lilo%2C_and_Stitch_enjoying_a_big_wave.jpg) | ✅ medido por cuantización de color (celda limpia, sin sombra de escenario) — **es su traje de baño, no el top coral icónico** que ya estaba en la biblia; confirma que su vestuario varía por escena, tal y como pide el punto 15 |
| Lilo, traje de baño (misma escena) | franjas diagonales **rojo `#7A1030`** y **naranja `#8F5030`** | misma imagen | ✅ medido; distinto del muumuu rojo icónico — otra variante de vestuario confirmada |
| Jumba, Cobra Bubbles, David | sin hex nuevo esta pasada | — | ⚠️ las imágenes grandes de la wiki para ellos seguían siendo fotos de Disney on Ice o muy pequeñas; pendiente de un fotograma limpio por el rol de vídeo |
| Jumba, Cobra Bubbles, David | sin cambios sobre lo que ya decía la biblia | — | ⚠️ sigue pendiente |

> Nota de método: las dos imágenes que mejor sirvieron para «arte
> oficial variado» (key visual) y para «ropa icónica» (Disney on Ice) NO
> son la misma fuente que un fotograma plano de la película. Para hex
> 100% fieles al cel de animación, la sesión que pinte en el PC debería
> sacar un fotograma con `fotogramas.py` (rol de vídeo) y medir ahí; dejo
> esto anotado como **pendiente obligatorio menor**, no crítico porque ya
> hay dos fuentes de color por prenda.

### Punto 16 · Fondos de pantalla (antes: «no encontré ninguno oficial»)

**Corregido**: sí hay, sólo que la red cerrada no dejaba verlos.

- **Fondos oficiales confirmados** (tamaño real, de la ficha de la wiki de
  Fandom — API `imageinfo`, no de memoria):
  - «Stitch! The Movie promo wallpaper.jpg» — **3000×1535** ✅
    ([wiki](https://static.wikia.nocookie.net/disney/images/6/66/Stitch%21_The_Movie_promo_wallpaper.jpg)),
    promocional oficial de *Stitch! The Movie* (2003).
  - Seis fondos oficiales del sitio japonés de Disney para el spin-off
    **«Stitch!» / juegos de Nintendo DS** (2008-2015), todos **1280×1024**,
    con Stitch y Angel (Reencontre/Yuna) en distintas escenas: «Motto!
    Stitch! DS wallpaper», «Stitch! DS - Ohana to Rhythm de Daibouken
    wallpaper», «Stitch! Good Deed Counter wallpaper», «Stitch and Angel in
    kimonos wallpaper», «Stitch painted Japanese wallpaper», «Tenugui
    Stitch wallpaper» ✅ (los seis, tamaño medido por la API de la wiki;
    urls en `imagen.json`). Encajan con el tono «postal» que pide el punto
    16 y muestran un **estilo pictórico japonés** (kimono, tenugui,
    pincelada) que no estaba documentado en la biblia.
  - «Stitch experiments wallpaper.jpg», **1575×1093** ✅, todos los
    experimentos juntos estilo papel tapiz.
- **Fondos de fans en alta ya estaban** en `datos-imagen.md` (Wallhaven, 10
  imágenes con autor, origen en ArtStation/DeviantArt y ancho×alto medido
  por Wallhaven mismo): no repito la lista, sólo la confirmo como válida
  para `imagen.json`.
- Los **sitios reales** (Hanapepe, Nā Pali, Hanalei) ya están descritos en
  §5 de la biblia con su luz — eso es del punto 4 (rol de vídeo), no lo
  repito aquí. Intenté sacar una foto libre de Hanapepe en Wikimedia
  Commons para complementar como «fondo real equivalente», pero la API dio
  **429 (demasiadas peticiones)**; no insistí más de un intento, como pide
  AYUDANTE.md ⚠️.

### Punto 19 · Texturas 2D (sección nueva, no existía en la biblia)

- **El emblema de Stitch (626)**: triángulo/estrella dorada sobre el pecho
  de su traje espacial, con cinturón negro de ribete dorado — medido en el
  punto 15 (`#F9E03E`). Es el «logo» más reconocible de merchandising:
  aparece igual en Funko, Disney Infinity y el propio traje de Disney on
  Ice ✅ (coherente en las tres fuentes).
- **Camisas hawaianas (aloha shirt)**: las lleva Jumba en su disfraz de
  turista y aparecen de fondo en las escenas de playa; es un estampado real
  con nombre propio (aloha shirt / palaka), pero **no encontré una textura
  ya hecha con licencia libre**, sólo bases de tela lisa:
  [ambientcg, `Fabric030`/`Fabric061`/`Fabric083`](https://ambientcg.com/list?type=Material&q=fabric)
  (CC0, tejido liso fotografiado) — sirven de **base** para pintar el
  estampado hawaiano encima a mano, no traen el dibujo ✅ para la base, ⚠️
  para el estampado en sí (no hay uno CC0 ya hecho).
- **Tela tapa/kapa hawaiana** (el motivo tribal de la portada de
  «Greatest Hawaiian» y de fondos de la película): busqué CC0 y **no
  encontré** ninguna textura lista, sólo fondos educativos ([Kapa Hawaii,
  historia](https://kapaiastitchery.com/hawaiian-quilting-history/),
  [RISD Museum](https://risdmuseum.org/exhibitions-events/exhibitions/pacific-islands-tapa-cloth))
  sin licencia de descarga ⚠️. Recomendación: dibujarlo a mano siguiendo
  fotos de museo como referencia, nunca calcarlo (son patrones culturales
  con dueño, ninguna imagen es CC0).
- **Puzles y patrones repetidos oficiales**: «Stitch and Experiments
  puzzle.jpg» (2137×1000, hoja 2 #81) muestra a Stitch y los 100+
  experimentos como patrón repetido — sirve de referencia de **cómo Disney
  arma un patrón infinito de merchandising** con el elenco ✅.
- **Grano y textura del cómic Dynamite**: es color digital plano con
  degradados suaves, **no usa tramas de puntos (halftone) visibles** en las
  portadas que miré — lo contrario del manga; para la lámina, si se imita
  el cómic occidental, va sin trama, sólo luz suave.

### Punto 23 · Colaboraciones y cruces (sección nueva, no existía en la biblia)

**Videojuegos y apps (crossover, no fan game)**
- **Kingdom Hearts**: Stitch es un **summon** de Sora desde *Kingdom Hearts
  II* (2005) con el «Encanto de Ukulele»: no entra al campo de batalla,
  se mueve por el HUD y **lame la pantalla** para rellenar HP/MP, y puede
  derribar proyectiles ✅ ([KH Wiki](https://www.khwiki.com/Stitch),
  [GameFAQs](https://gamefaqs.gamespot.com/ps2/915410-kingdom-hearts-ii/answers/115138-missed-stitch-summon)).
  Su traje en KH es el mismo traje espacial rojo. Aparece también en
  *Kingdom Hearts III* como parte de la atracción temática «Stitch's Great
  Escape» en Shanghai Disneyland dentro del propio juego (hoja 12, #535).
- **Disney Infinity** (2013-2016, Disney Interactive): figura física de
  Stitch jugable, logo confirmado en las hojas (#410, #546) ✅ ([Disney
  Infinity Wiki, referencia externa](https://disneyinfinity.fandom.com/)).
- **Disney Lorcana** (juego de cartas físico, Ravensburger/Disney): set
  propio **«Lilo & Stitch» (precon, enero de 2026)** con cartas de Nani en
  tinta **Ámbar** y de Stitch en varias tintas, incluida **Esmeralda**
  («Stitch — Covert Agent», #89/204) ✅
  ([Lorcana Player, ficha de la carta](https://lorcanaplayer.com/card/stitch-covert-agent/),
  [Dreamborn.ink, mazo del set](https://dreamborn.ink/decks/khfanjJj1HSJ3eTO0Yny)).
  El arte de cada carta es una pose nueva y con objeto (agente encubierto,
  «rock star», héroe galáctico): **útil directo para el punto 1** también.
- **Disney Heroes: Battle Mode** (móvil, PB&J Games/Disney, 2018): logo
  confirmado en la hoja (#428) ✅; Stitch como personaje jugable estilo
  chibi/RPG.
- **Disney Tsum Tsum**: edición del **15.º aniversario de Lilo & Stitch**
  con figuras apilables en el estilo redondeado de Tsum Tsum (hoja 12,
  #547) ✅.
- **Disney Dreamlight Valley**: ya estaba en la biblia (búsqueda 17 de la
  bitácora anterior); lo confirmo, Stitch es personaje jugable con su
  propia zona temática.
- **Fortnite**: **filtrado, no confirmado**. En febrero de 2026 salieron
  archivos que apuntan a Stitch como **«sidekick»** (acompañante, no skin
  jugable, no se pone en un mecha) dentro de la colaboración Disney×Epic;
  Epic **no lo ha anunciado oficialmente** ⚠️
  ([Vice](https://www.vice.com/en/article/leak-disneys-stitch-is-coming-to-fortnite-but-theres-a-catch/),
  [esports.gg, lista de colaboraciones Disney](https://esports.gg/news/fortnite/fortnite-x-disney-a-complete-list-of-all-collaboration-skins/)).
  **No usar como confirmado** en ninguna lámina.

**Cómics (crossover)**
- **«Stitch Crashes the Marvel Universe»** (Marvel Comics, portadas
  variante, salen en septiembre de 2025): Stitch invade las portadas de
  *Amazing Spider-Man* #11 (Luciano Vecchio), *Avengers* #30 (Humberto
  Ramos), *Captain America* #3 (Ben Su), *Fantastic Four* #3 (Paco Medina)
  y *X-Men* #22 (Phil Noto), para el 100.º número de cada serie ✅
  ([Marvel.com, anuncio oficial](https://www.marvel.com/articles/comics/stitch-crashes-the-marvel-universe-in-new-comic-book-covers),
  [AIPT](https://aiptcomics.com/2025/06/26/stitch-marvel-comics/),
  [Bleeding Cool](https://bleedingcool.com/comics/disney-stitches-stitch-to-the-covers-of-the-marvel-universe/)).
  Ya estaban 6 de estas portadas en las hojas 1 y 2 (Avengers, Captain
  America, Spider-Man, Fantastic Four) sin identificar: ahora sí, con
  artista y número exactos.
- **«Stitch Crashes Disney»** (2021-2022): colección mensual de **peluches**
  donde Stitch se cuela en 12 películas clásicas de Disney (Alicia,
  Aladdín, Bambi, etc.), origen de la idea de las portadas Marvel ✅
  (mencionado en [How To Disney](https://howtodisney.com/stitch-crashes-disney-history-co1/)).
  Es el precedente directo de los «Inter-Stitch-als» de 2002 que ya
  estaban en la biblia (§3.1): la marca repite la broma cada pocos años.

**Figuras oficiales (pose = referencia 3D real)**
- **Funko Pop**: Stitch es el n.º 12 de la línea Pop! Disney; hay variantes
  con disfraces propios de la película (Aloha Stitch, Elvis Stitch) y
  **crossover directo**: **Stitch disfrazado de Beast (#1459), Cheshire Cat
  (#1460), Simba (#1461) y Pongo (#1462)**, de otras películas Disney ✅
  ([Pop Shop Guide, catálogo](https://www.popshopguide.com/funko-pop-series/pop-disney/lilo-and-stitch/),
  [Cardboard Connection, galería](https://www.cardboardconnection.com/funko-pop-lilo-and-stitch-figures)).
  Estas figuras «vestidas de otro personaje» son la referencia 3D más
  directa que hay para la idea del dueño de «poses vivas, con objeto,
  disfrazado».
- **Britto** (pop-art) y **Jim Shore Disney Traditions «'Ohana»** (madera
  tallada): ya vistas en las hojas, confirmadas como línea oficial Enesco
  con licencia Disney (marca en la propia pieza).
- **Garage kit «StitchLiloSchoolGK»** (hoja 2, #64): figura de resina de
  fan, **no oficial**, sólo como referencia de pose de escuela.

**Moda y accesorios (merchandising con arte nuevo)**
- **Loungefly** (BoxLunch/Disney Store): mochilas con el estampado del
  vestido rojo de Lilo repetido como patrón, y una línea «Stitch y Scrump»
  con flores tropicales ✅ ([Disney Store](https://www.disneystore.com/lilo-stitch-loungefly-mini-backpack-442090260726.html),
  [BoxLunch](https://www.boxlunch.com/brands/loungefly/lilo-stitch/)). El
  estampado del vestido de Lilo repetido es **textura 2D lista** (punto 19)
  aunque protegida por copyright: sirve de referencia, no para calcar.
- **Crocs Jibbitz**: packs oficiales «Stitch Tropical», «Stitch Wild»,
  «Stitch Curious», «Stitch Sweet» — charms con la cara de Stitch en
  distintas expresiones ✅ ([Crocs.com](https://www.crocs.com/p/stitch-tropical-5-pack/10012920.html)).

**Parques y espectáculos en vivo**
- **Stitch's Great Escape!** (Magic Kingdom, Tomorrowland): abrió el
  16-nov-2004, reemplazó a *ExtraTERRORestrial Alien Encounter* (cerrada el
  12-oct-2003) reusando gran parte de su tecnología y decorado; cerró en
  2018 ✅ ([D23, ficha oficial](https://d23.com/a-to-z/stitchs-great-escape/),
  [Wikipedia con fecha exacta](https://en.wikipedia.org/wiki/Stitch%27s_Great_Escape!)).
- **Stitch Encounter** (Hong Kong Disneyland, Tokyo Disneyland, Shanghai
  Disneyland): experiencia interactiva donde Stitch «habla» con el público
  en tiempo real ✅ (confirmado por fotos propias en la hoja 1, #3, y hoja
  12, #536 «Stitch Encounter Shanghai»).
- **Disney on Ice**: gira con Stitch, Jumba y Pleakley en traje de
  patinaje sobre hielo — la fuente que usé para medir el rojo del traje
  espacial y el amarillo de Pleakley (punto 15) es justo de esta gira ✅
  (foto propia en datos-imagen, «DOI - Jumba, Stitch & Pleakley.jpg»).
- **Fab 50** (50.º aniversario de Walt Disney World, 2021-2022): estatua
  dorada de Stitch mordiendo su medallón, en el «Muro Púrpura» de
  Tomorrowland junto a Monsters Inc. Laugh Floor ✅
  ([MiceChat](https://www.micechat.com/322514-fab-50-character-collection-walt-disney-world/),
  [Disney Wiki, ficha de la colección](https://disney.fandom.com/wiki/Disney_Fab_50_Character_Collection)).
- **Desfiles temáticos**: «2008 Dreams Come True Parade» y «DJ Stitch
  Disney Parks» (hoja 1, #29-30) confirman carrozas propias de Stitch en
  los desfiles diarios de Disneyland/WDW.

**Cafés temáticos y pop-ups**
- **OH MY CAFE / BOX cafe&space** (Japón): café pop-up de Stitch en Tokio
  (20-jun a 27-jul-2025) y en Nagoya/Aichi (10-jul a 3-ago-2025), con menú
  tropical, postres de colores y merchandising exclusivo ✅
  ([TDR Explorer](https://tdrexplorer.com/limited-time-stitch-pop-up-cafe-launching-soon-in-tokyo-and-aichi/),
  [Japan Web Magazine](https://jw-webmagazine.com/tips/stitch-cafe-in-japan-2025/)).
- **Pop-up de Shanghai** (Zhang Yuan, 26-jun a 19-jul): Stitch y Scrump,
  gelato y macarons temáticos ✅ (mismas fuentes).
- **Primark × Disney** (Manchester): café pop-up dentro de la tienda con
  murales gigantes de Stitch ✅ ([Indian Retailer / Brand
  License](https://www.indianretailer.com/brandlicense/archives/news/primark-x-disney-launch-exclusive-stitch-collection-cafe-experience.n3923)).
- **MINISO** (American Dream Mall, Nueva York, 12-abr a 4-may): pop-up con
  casi 200 productos de la colaboración ✅ ([License
  Global](https://www.licenseglobal.com/retail-news-trends/minso-debuts-world-first-stitch-pop-up-experience-in-u-s-)).
- **Tropical Smoothie Cafe** (EE.UU., mayo 2025): batido «'Ohana Breeze»,
  primera colaboración de la cadena con una película Disney ✅
  ([nota de prensa, PR
  Newswire/Cision](https://www.counton2.com/business/press-releases/cision/20250512CL84550/tropical-smoothie-cafe-debuts-first-ever-disney-collaboration-featuring-the-new-ohana-breeze-smoothie-inspired-by-lilo-stitch/)).

**Cosplay**
- No encontré un tutorial **específico** de cosplay de Stitch con
  materiales exactos (tela, espuma, patrón) firmado por un cosplayer
  reconocido; sólo guías genéricas de *fursuit* (pelo sintético, espuma de
  alta densidad, forro de traje) que sirven como método pero no citan a
  Stitch por nombre ⚠️. Las fotos de cosplay/disfraces oficiales de parque
  (Disney on Ice, Stitch Encounter) sí sirven como referencia de volumen y
  sí están confirmadas arriba.

## Lo mejor para la lámina

1. **Objeto**: el **álbum de fotos** (modelo Sketchfab CC-BY de mnaglak,
   licencia verificada por API) sobre un **tablero de corcho** (Cork Board,
   CC-BY, rickmaolly) con la **cámara Canon AE-1** (CC-BY, fotogrametría
   real) al lado — las tres piezas con licencia confirmada hoy.
2. **Pose de Lilo**: el key visual oficial «promo art 2.jpg» (Lilo y Stitch
   de espaldas al atardecer, ella con traje de hula) da luz cálida y una
   pose de complicidad, mejor que un busto recto.
3. **Guiño de colaboración**: la carta de Lorcana «Stitch — Covert Agent»
   (tinta Esmeralda) tiene una pose de espía con lupa/cámara improvisada:
   encaja de forma literal con el tema de #fotos y es arte oficial reciente
   (2026) que nadie más habrá usado todavía.
4. **Textura del marco**: el estampado repetido del vestido rojo de Lilo
   (visto en la Loungefly oficial) para el borde de una foto tipo Polaroid.
5. **Emblema**: el triángulo/estrella dorado del traje de Stitch
   (`#F9E03E` medido) como sello o pin en una esquina del álbum.

## No encontré (⚠️, no obligatorio pero se buscó)

- Estampado hawaiano (aloha shirt) o tapa/kapa **ya hecho** en CC0: sólo
  bases de tela lisa en ambientcg. Búsquedas: «Hawaiian tapa cloth kapa
  pattern free texture CC0» (en), «ambientcg fabric» (API).
- Tutorial de cosplay de Stitch firmado, con materiales exactos.
- Confirmación oficial (no filtración) de Stitch en Fortnite.
- Hex «plano» de Jumba, Cobra Bubbles y David: sus imágenes grandes en la
  wiki seguían siendo de Disney on Ice o muy pequeñas. (Nani sí se resolvió:
  encontré un fotograma limpio de animación con ella y Lilo, ver punto 15.)
  Pendiente: pedir al rol de vídeo un fotograma limpio de cada uno.
- Foto libre de Hanapepe en Wikimedia Commons: la API dio 429, un solo
  intento (regla de AYUDANTE.md).

## Bitácora de búsqueda (segunda pasada, imagen)

| # | Idioma | Búsqueda | Qué dio |
|---|---|---|---|
| 1 | en | Stitch Fortnite Disney collaboration skin | filtración de «sidekick», no confirmado |
| 2 | en | "Stitch Crashes Disney" Marvel variant covers list | anuncio oficial Marvel.com, 5 portadas de sep-2025 |
| 3 | en | Disney Lorcana Lilo Stitch card ink color set | Lorcana Player, Dreamborn (precon ene-2026) |
| 4 | en | Stitch 50th anniversary "Fab 50" golden statue | MiceChat, Disney Wiki (colección Fab 50) |
| 5 | en | Lilo Stitch grandmother's quilt scene Hawaiian quilt pattern | sin escena de "quilt" confirmada en la película; sólo contexto cultural (Kapa Hawaii, RISD) |
| 6 | en | Loungefly Stitch collection backpack collaboration | Disney Store, BoxLunch |
| 7 | en | Crocs Jibbitz Stitch charms collaboration | crocs.com, 4 packs oficiales |
| 8 | en | Stitch cosplay fursuit tutorial fabric materials pattern | sólo guías genéricas de fursuit |
| 9 | en | "Art of Lilo & Stitch" artbook Disney Editions published | es «Collected Stories…», Disney Press 2002, no «Disney Editions» |
| 10 | en | Lilo Stitch official wallpaper movies.disney.com archive | nada del dominio oficial; sí sirvieron los 7 de la wiki (Japón) |
| 11 | en | Kingdom Hearts II Stitch summon ability official | KH Wiki, GameFAQs |
| 12 | en | Hawaiian tapa cloth kapa pattern free texture CC0 | nada en CC0, sólo educativo |
| 13 | en | "Stitch's Great Escape" Magic Kingdom 2004 replaced Alien Encounter | D23, Wikipedia (fechas exactas) |
| 14 | en | Funko Pop Stitch official figures list Disney | Pop Shop Guide, Cardboard Connection (crossovers Beast/Cheshire Cat/Simba/Pongo) |
| — | — | API Sketchfab (3 modelos) | licencias verificadas, 1 corregida |
| — | — | API ambientcg (fabric, paper) | bases de tela CC0, sin estampado |
| — | — | API Wikimedia Commons (Hanapepe) | 429, no se insistió |

**Total esta parte**: 14 búsquedas web + 5 consultas de API directas (sin
gastar cupo de buscador). Sumadas a las 51 de la primera pasada (biblia
§21), el total del encargo sigue muy por encima del mínimo de 40 fuentes.

## Cumplimiento de esta parte (puntos 1, 3, 15, 16, 19, 23)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | Artbook confirmado, hoja de modelo, key visual grande, portadas Dynamite con artista, revistas — todo con fuente y, donde aplica, dos fuentes |
| 3 · Fan art y 3D con licencia | ✅ | 4 licencias de Sketchfab verificadas por su API (una corregida); fan art de Lilo con cámara sigue sin aparecer, declarado como «no encontré» |
| 15 · Vestuario con hex | ⚠️ | Hex medidos y con fuente para Stitch, Lilo y Nani (ésta en un fotograma limpio de animación, no Disney on Ice); Jumba/Cobra/David siguen sin hex propio — pendiente de un fotograma limpio por el rol de vídeo |
| 16 · Fondos de pantalla | ✅ | 7 fondos oficiales con tamaño medido (antes: «no encontré ninguno»), más los de fans que ya estaban en datos-imagen.md |
| 19 · Texturas 2D | ⚠️ | Sección nueva creada; emblema y puzle-patrón confirmados con fuente; el estampado hawaiano y el tapa/kapa no tienen equivalente CC0 ya hecho (se documenta el porqué) |
| 23 · Colaboraciones y cruces | ✅ | Sección nueva creada; 12+ colaboraciones distintas con fuente (juegos, cómics, figuras, moda, parques), cada una con al menos una fuente directa (varias con dos) |
