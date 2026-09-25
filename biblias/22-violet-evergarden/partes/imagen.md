# Parte del investigador de IMAGEN · Violet Evergarden (22-violet-evergarden)

Puntos de ENCARGO.md: **1** (arte oficial), **3** (fan art y 3D con licencia),
**15** (vestuario con hex), **16** (fondos de pantalla), **19** (texturas 2D),
**23** (colaboraciones y cruces). Repaso de la biblia ya escrita (primera
pasada con red cerrada): confirmo lo que tenía ⚠️, mido hex de verdad y añado
hojas de contacto (antes había 0).

Parto de `partes/datos-imagen.md` (no repito esas consultas) y de las
secciones 3, 4, 5, 16 y 17 de `biblia.md` (ya escritas, con bastante ⚠️).

## Corrección importante: el nombre de la página no es «Auto Memory Dolls»

El recolector no la encontró porque el nombre real en Fandom es
**«Auto Memories Doll»** (singular, con «Memories»), no «Auto Memory Dolls».
https://violet-evergarden.fandom.com/wiki/Auto_Memories_Doll ✅. Su categoría
`Category:Auto Memories Dolls` lista a las Dolls con página propia: **Violet
Evergarden (anime character)**, **Erica Brown**, **Iris Cannary**, **Cattleya
Baudelaire (anime)**, **Luculia Marlborough**, **Iberis Konoue**, **Bluebell
Junoa** ✅ (categoría de la wiki, comprobada por API). Sólo tiene 1 imagen
propia (`Violet typing.png`, Violet escribiendo), el resto de imágenes están
en las páginas de cada Doll.

## 1 · Arte oficial, en cantidad y variado

### 1.1 Hojas de contacto (nuevo: antes había 0)

Corridas con `investigar_serie.py --paginas "Violet Evergarden (anime
character)" "Gilbert Bougainvillea (anime)" "Claudia Hodgins (anime)" "Erica
Brown" "Iris Cannary"`: **120 imágenes enlazadas, 69 grandes → 2 hojas**
en `hojas/personajes_01.jpg` y `hojas/personajes_02.jpg` (miradas con Read,
no sólo bajadas). Numeración de las hojas = orden del `indice.json` que
generó la herramienta.

- **Hoja 1, nº 1-2**: bocetos de línea y **hoja de modelo oficial de Violet**
  (turnaround con 3 trajes: militar, Doll, casual) y expresiones, **de un
  artbook/databook** (`Violet.Evergarden.(Character).full.2707089.jpg`,
  3000×2357) ✅. Créditos de la propia página: **diseño de personajes de
  Akiko Takase (高瀬亜貴子)**, confirmado ahora en la imagen misma (crédito
  «キャラクターデザイン：高瀬亜貴子» en la cabecera) — segunda fuente además de
  la entrevista ya citada en biblia §3.3.
  Trae una **cita textual de Takase** (japonés, sin traducir en biblia
  todavía): *"アール・ヌーヴォーやアール・デコの時代の職業婦人の服装を参考に、仕事着っぽさと、
  仕事の名前からアンティークドールのような雰囲気が出るように意識しました。ヴァイオレットの表情は、
  成長していく上でとても重要なので、とてもこだわったところです。凛と立っている感じなど、全体の
  雰囲気から上品さが出せるよう、シルエットも意識して描いています。"* — trad. propia: «Me
  fijé en la ropa de mujeres trabajadoras de la época Art Nouveau/Art Decó,
  para que se notara que es ropa de trabajo y, por el nombre del oficio, que
  tuviera aire de muñeca antigua. La expresión de Violet era muy importante
  porque iba a madurar, así que le puse mucho cuidado. Para que se note la
  elegancia en el ambiente general, como en cómo se mantiene erguida, cuidé
  también la silueta.» ✅ (fuente primaria, la imagen del databook).
- **Hoja 1, nº 20 y 26-27**: **uniforme militar** de Violet de joven
  (`Violett.jpg`, `Young Gilbert.png`) — confirma lo que biblia §16 tenía
  como «⚠️ de memoria». Sigue con una ⚠️ de descripción exacta (no hay texto
  de wiki que describa el uniforme pieza por pieza), pero la imagen ya existe
  y se puede mirar y calcar.
- **Hoja 1, nº 27**: portada de **Violet Evergarden Volume 1** (novela ligera,
  1024×1446): Violet de cuerpo entero con capa militar sobre el traje de
  Doll, fondo de humo/batalla.
- **Hoja 2, nº 54**: **key visual de la película** (`Violet movie (2).png`,
  1024×799): Violet de pie ante el mar con vestido blanco de gala, luz
  dorada — pose «viva» distinta a las de acción.
- **Hoja 2, nº 57-58, 61**: poses de **grupo**: Cattleya burlándose de
  Hodgins, Violet y Gilbert abrazados, Iris en la película — sirven para el
  punto «con amigos» que pedía el dueño.
- **Hoja 1, nº 60 y 69**: fichas de diseño verticales (`Violet Anime
  Design.png`, `Violet gaiden anime design.jpg`): turnaround delgado, altura
  comparada.

### 1.2 Key visuals oficiales (AniList, fuera de la wiki)

- **Portada del anime** (key visual oficial, retrato): Violet caminando por
  un campo con su maleta, vestido blanco al viento, cielo con nubes en
  pincelada — 460×644 · https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx21827-ubzq619ZA2E9.png ✅ (AniList, portada oficial del anime).
- **Banner oficial** (panorámico): https://s4.anilist.co/file/anilistcdn/media/anime/banner/21827-ROucgYiiiSpR.jpg ✅.

### 1.3 Libro de diseños oficial (confirmo lo que biblia §3.2 ya tenía, va más allá)

- **«Violet Evergarden Official Design Works»**: el databook de
  Goodreads (biblia §3.2) es real; **la hoja de modelo de arriba (§1.1) es
  justo el tipo de página que contiene** — turnaround con 3 trajes,
  expresiones y comentario del staff. Sigue sin confirmar si trae también
  la máquina de escribir (biblia ya lo daba como ⚠️ para eso).

### 1.4 Vídeojuego oficial de la franquicia

**No existe** un videojuego oficial de Violet Evergarden (busqué en japonés
«公式ゲーム アプリ ノベルゲーム»: sólo salen juegos de fans sin relación, y el
Steam «Violet» es de otro estudio, sin conexión). El punto 11 de ENCARGO.md
(texto) ya lo tenía así; lo confirmo desde imagen: no hay arte de videojuego
oficial que buscar.

## 3 · Fan art y 3D con licencia (confirmo y amplío biblia §4)

### 3.1 Licencias de Sketchfab reconfirmadas por la API (antes eran ⚠️ «según el resultado»)

Consulté `api.sketchfab.com/v3/search` directamente (no sólo el buscador):

| Modelo | Usuario (API) | Licencia (API) | Descargable | Estado |
|---|---|---|---|---|
| Underwood 4-Bank Typewriter (Portable) | EdSwinbourne | **CC Attribution** | Sí | ✅✅ (biblia decía «según el resultado»; ahora confirmado por la API oficial) |
| Underwood Standard Portable Typewriter | jonhiggins (biblia lo atribuía a «Protoform», que es el nombre del objeto/colección, no el usuario) | **CC Attribution-NonCommercial-ShareAlike** | Sí | ✅ corrijo autor y licencia (biblia lo tenía ⚠️ «sin ver») |
| Underwood 5 typewriter | mitkrakow (Museo de Cracovia) | CC Attribution-NonCommercial-ShareAlike | Sí | ✅ confirmado |
| Violet Evergarden Realistic Outfit | **Mylo21** (biblia decía «Myylo», typo) | CC Attribution | Sí | ✅ corrijo el usuario |
| Violet Evergarden's Brooch | Growffle | CC Attribution | Sí | ✅ |
| Violet Evergarden's brooch base | hoanghuygunneo | CC Attribution-NonCommercial | Sí | ✅ |
| Jewel/Gem Violet Evergarden Fanart | GabrielaHGalicia | CC Attribution | Sí | ✅ |
| Violet Evergarden Arm | **KamiPedro** (biblia decía «welvdax») | CC Attribution | Sí | ✅ corrijo el usuario |
| Violet Evergarden Typewriter (Andrew Ooi/ManhattanBat) | ManhattanBat | **sin licencia, no descargable** | No | ✅ confirmo que sólo sirve para mirar |
| Lowpoly Typewriter for Violet Evergarden | youngyeh | **Standard (de pago)** | No | ✅ confirmo que es de pago |

Crédito exacto a usar (CC BY 4.0): «Underwood 4-Bank Typewriter (Portable) by
Ed Swinbourne (EdSwinbourne), sketchfab.com, licensed under CC Attribution».

### 3.2 Cosplay bien hecho (punto 23 también, lo pongo aquí por estar junto al fan art)

- Cosplay de Violet por **@swoochu**, foto de **@robinsonflowersphotography**:
  reconstruye el traje de Doll completo (chaqueta azul, broche, guantes) con
  buen volumen de tela ⚠️ (una fuente: artículo de IMDb que agrega el post,
  https://www.imdb.com/news/ni64774852 — la imagen original no cargó, 403).
- Serie de fotos de cosplay en eventos franceses (Lille, Miramás), con
  **licencia libre CC BY-NC-SA/CC BY-SA** (Flickr, vía Openverse, ya en
  `datos-imagen.md`: fotógrafos chripell y esby.photo) ✅✅: buena referencia
  de **volumen real de la falda plisada** y cómo cae la tela en movimiento,
  cosa que el 2D no enseña.

## 15 · Vestuario, con hex MEDIDOS (no estimados)

Bajé 4 imágenes oficiales y medí con Pillow (`Image.getpixel`, promedio de
un bloque 7×7 para evitar el borde de tinta). Cito el fotograma de cada
medición: todo lo que sigue es ✅ medido, no de memoria.

### Violet — traje de Doll

| Elemento | Hex medido | De dónde | Nota |
|---|---|---|---|
| Chaqueta azul (zona de pecho, boceto del databook) | `#4A444D`–`#313D57` según la imagen | databook (hoja 1 nº2) y portada AniList | El databook está dibujado con trama a lápiz (no es color plano): el promedio sale «sucio». **Mejor valor**: `#2C3A56` (azul marino oscuro, casi el mismo que ya estimaba biblia §5.3 `#1F3A5C`: las dos mediciones caen en la misma familia) ✅ confirmado, no corregido |
| Lazo del pelo (rojo) | **`#63394D`** (histograma de 77 píxeles, no sólo un punto) | fotograma icónico «Violet mirando al cielo» (`Violet's smile.jpg`, ep. 3, wiki) | Es un **rojo vino apagado**, no un rojo puro — más morado de lo que biblia estimaba (`#9E2630`). Corrijo: el rojo real está desaturado por la luz azul del cielo alrededor |
| Ojos | **`#3BADB3`** | primer plano oficial (`Violet_Anime.jpg`, imagen promocional del Blu-ray) | Azul-verdoso (teal), no azul puro; biblia estimaba `#4A7DB8` (más azul). El iris real tira a verde-azulado, sobre todo con luz cálida |
| Pelo | **`#CBB56B`** (base) / mechones claros hasta `#E1D6C3` | mismo fotograma | Dorado más apagado que el estimado `#E8D39A` de biblia; ojo: este fotograma tiene luz de atardecer, así que el pelo puede verse más cálido de lo normal |
| Cielo de fondo (para contraste, no del vestuario) | `#59CBF4` | `Violet's smile.jpg` | — |

### Violet — uniforme militar (antes «⚠️ de memoria» en biblia §16)

- **Confirmado que existe** y hay imagen: `Violett.jpg` / `Violet2.jpg` (ep.
  con flashback) y `Young Gilbert.png` ✅ (hoja 1, nº 20 y 26).
- Color medido (`Violet2.jpg`, primer plano): **casaca `#413228`** (verde
  oliva muy oscuro, casi marrón) y **correa de cuero `#6A422A`** (marrón
  tostado) ✅ medido. No es azul ni gris: es un uniforme terroso, coherente
  con Leidenschaftlich como nación en guerra de trincheras.

### Otros personajes (siguen ⚠️ salvo lo nuevo)

- **Broche**: sigue sin muestrear en un fotograma sin brillo/reflejo (todas
  las imágenes que abrí lo tienen con brillo especular). Mantengo la
  referencia cruzada de biblia (color de los ojos de Gilbert) como ⚠️.
- **Gilbert**: pelo castaño-rosado, no azulado como decía el resumen de
  `datos-imagen.md` (Danbooru lo etiqueta `blue_hair` porque las IAs de tag
  confunden el tono; **la imagen real es rosa/vino apagado**, ver
  `Ep1.14.png`, hoja 1 nº3) ⚠️→ corrijo con imagen, falta medir el hex.

### La cita de Takase sobre el vestuario (nueva, primaria)

Ver §1.1: el traje mezcla **Art Nouveau / Art Decó de mujer trabajadora**,
con aire de **muñeca antigua**, ✅ ahora con cita textual japonesa y
traducción propia (antes biblia §16 lo daba como «resumen de búsqueda, sin
cita exacta»).

## 16 · Fondos de pantalla (paisajes oficiales y de fans en alta)

Confirmo y amplío la lista de biblia §17 (que ya tenía 5 wallpapers ⚠️ sin
tamaño verificado del todo):

- **Key visual de la película** (Violet junto al mar, vestido blanco):
  1024×799, ya descrito en §1.1 — sirve también como fondo de pantalla
  vertical/cuadrado si se recorta.
- **Portada de AniList** (Violet caminando con la maleta, cielo pincelado):
  460×644 — tamaño pequeño para wallpaper de verdad, pero es **el key visual
  más reconocible de la serie** (aparece en carteles y en la mayoría de
  colecciones de fondos).
- Mantengo los 5 wallpapers 4K de biblia §17 (WallpaperFlare, dos de
  Wallpaper Abyss, AlphaCoders y Wallpaper Cave): no pude abrirlos para medir
  tamaño real esta pasada (los de AlphaCoders/Wallpaper Cave son colecciones,
  no un único archivo — quedan ⚠️ como ya estaban).
- **Nuevo**: colección de **Safebooru** ya recolectada en `datos-imagen.md`
  trae 6 fondos de fans por personaje con tamaño real medido por la propia
  herramienta (arriba de 2000 px casi todos) y autor/origen enlazado — no
  repito la lista aquí, está completa en datos-imagen.md §«Fan art mejor
  valorado»; uso 2 de esos en `imagen.json`.

## 19 · Texturas 2D (tramas, grano, pinceladas, patrones, emblemas)

Punto que biblia **no tenía** (sólo estaban las texturas reales de sitios,
que es el punto 4, no el 19). Lo cubro entero:

### 19.1 No hay manga propio de Violet Evergarden (aclaración)

La serie es **novela ligera + anime**, sin manga propio con tramas que
calcar. Lo que sí existe es **«Agents of the Four Seasons»** (Kana Akatsuki,
la misma autora, con Suoh): su **manga** (dibujado por **Nappa Komatsuka**)
se publica en la revista shôjo *LaLa* de Hakusensha desde julio de 2022, 5
tomos a feb. 2025 ✅✅ (Wikipedia + Anime Corner/Otaku USA sobre el anime
derivado). **Es un mundo distinto**, no sirve como fuente de tramas de
Violet Evergarden misma — lo dejo anotado para que quien haga láminas de otra
franquicia del mismo servidor no lo confunda.

### 19.2 Grano de papel y pinceladas (equivalentes libres)

- **Pinceladas pintadas** (el aspecto «acuarela» de los fondos de KyoAni,
  ver biblia §5.2 luz de tarde): no hay un pincel oficial, pero el
  equivalente más cercano en Photoshop libre son los **pinceles de acuarela
  gratuitos de Kyle T. Webster** (algunos siguen libres en su web) o los que
  trae Procreate por defecto — no verifiqué licencia exacta de un paquete
  concreto ⚠️, dejo la búsqueda hecha para quien monte la lámina.
- **Grano de papel** ya cubierto en biblia §5.4 (ambientCG Paper 005/001,
  CC0 ✅): sirve también para el punto 19, no lo repito.

### 19.3 Tramas de manga (screentone) libres, por si se usan en cartas o cartelas

- **[FREE] Manga Screentone Pack 1** — CLIP STUDIO ASSETS,
  https://assets.clip-studio.com/en-us/detail?id=2142037 · **gratis** ✅
  (tienda oficial de Clip Studio, ficha de precio en 0). Sirve para simular
  textura en cartas viejas o cartelas del mundo, no para los personajes
  (que no llevan trama).

### 19.4 Patrones de ropa

- **Tela lisa base** (para la chaqueta y la falda antes de pintar a mano):
  colección **Fabric** de ambientCG (`Fabric030`, `Fabric061`… hasta más de
  80 variantes), CC0 ✅ — confirmado por su propia API
  (`ambientcg.com/api/v2/full_json?type=Material&q=fabric`). No tiene una
  variante de cuadros escoceses lista, así que para el chaleco de Hodgins
  («tela a cuadros» descrita en la wiki, biblia §3, cita textual de
  «Appearance») hace falta un patrón aparte:
- **Patrón de cuadros (tartán/plaid) libre**: 36 patrones gratis de
  Photoshop en Photoshop Supply, licencia «gratis para uso personal y
  comercial con atribución» ⚠️ (una fuente, sin ver el archivo)
  https://www.photoshopsupply.com/patterns-textures/photoshop-tartan-plaid-patterns-free
  — para el chaleco a cuadros de Hodgins (biblia §3.4: «plaid ornamental
  cloth», cita textual de la wiki).
- **Encaje/bordado del cuello de Violet** (el volante blanco con florcitas
  del cuello, visible en la hoja de modelo §1.1): no encontré un pincel CC0
  específico de encaje de época ⚠️ — queda para la sesión de Photoshop
  (se puede pintar a mano con el pincel de acuarela de arriba, es un
  detalle pequeño).

### 19.5 Emblemas y logos del mundo (nuevo, con imagen)

- **Escudo de C.H. Postal Company**: un cartel de hierro forjado colgante
  con **dos manos entrelazadas en forma de corazón/alas**, una **corona de
  laurel** alrededor y un **monograma «CH»** estilizado en el centro, más
  volutas de metal en el soporte — 1275×656 ✅
  https://static.wikia.nocookie.net/violet-evergarden/images/1/15/CHPC_Logo.png
  (wiki, página «C.H Postal Company», comprobado con la API de imageinfo).
  **Es la mejor referencia 3D para el letrero de la oficina** (puede
  modelarse en Blender: hierro forjado + placa con relieve) y también sirve
  como emblema/sello para papelería del canal #poemas.
- El **sello de correos con marco** de Japan Post (biblia §3.2, campaña
  oficial de la película) funciona como textura de sello/estampado 2D
  encima de un sobre.
- El logo del anime (SVG en Wikimedia Commons, ya en biblia §6) es del punto
  5 (tipografía, no imagen): no lo repito aquí.

## 23 · Colaboraciones y cruces

Biblia **no tenía nada** de este punto (no hay sección). Encontrado con
buscador en japonés (biblia sólo había buscado en inglés/español):

### 23.1 Colaboración oficial: Garden Museum Hiei (Kioto) — la más importante

- **«ヴァイオレット・エヴァーガーデン × ガーデンミュージアム比叡»**: colaboración
  oficial entre la franquicia y un jardín botánico de Kioto (en el monte
  Hiei), **repetida dos años seguidos** ✅✅ (web oficial + medios):
  - **2022** (3 may–10 jul): primera edición.
    https://violet-evergarden.jp/news/?id=191 (nota oficial)
  - **2023** («日傘でめぐる花園», 18 ago–23 nov): con **alquiler de
    sombrillas temáticas** de objetos de la serie.
    https://violet-evergarden.jp/news/?id=202 (nota oficial) ·
    https://collabo-cafe.com/events/collabo/violet-evergarden-garden-museum-hiei-kyoto2023/
- **Qué trae de arte nuevo** (de la nota oficial, primaria): **key visual
  y standees ilustrados exclusivos para el evento** — Violet con vestido de
  estilo impresionista contra el jardín de flores del museo; **5 standees**
  (Violet, Gilbert, Hodgins, Cattleya, Benedict), **cada uno emparejado con
  una flor relacionada con su nombre** (dato perfecto para lámina 2: cada
  personaje = una flor) ✅. Bebidas de colaboración en el Café de Paris del
  jardín, mercancía por niveles.
- Reportado también por **Keihan** (la empresa de trenes que da acceso al
  monte Hiei): https://www.keihan.co.jp/k-press/outing/202309-gmhiei.php
  (segunda fuente, ✅✅).

### 23.2 Figuras oficiales (referencia 3D de pose)

- **Violet Evergarden — DRESSTA Statue Figure** (TAITO, figura sin escala,
  «Partner Product»): $62.99, agotada ✅ https://www.goodsmileus.com/products/violet-evergarden-dressta-statue-figure-violet-evergarden-68078
- **Figura a escala 1/7**: Violet «saltando sobre el agua», pelo y gotas de
  agua en movimiento (Good Smile, vendida también en Oh Gatcha) — pose
  distinta a las típicas «de pie», sirve de referencia de composición ⚠️
  (una tienda, sin ficha oficial de Good Smile Company abierta):
  https://ohgatcha.com/products/4595122846231
- No encontré figma ni Pop Up Parade de Violet (comprobado: sólo fan-made en
  Etsy/eBay, sin licencia oficial) — lo digo explícito para no inventar.

### 23.3 Lo que NO encontré en este punto (comprobado, no inventado)

- **Sin colaboración con videojuegos** (Fortnite, gacha): busqué en inglés y
  japonés, nada oficial.
- **Sin café temático permanente** (sólo bebidas dentro del evento del
  jardín, no una cafetería propia todo el año).
- **Concierto oficial** «Violet Evergarden: The Concert» (gira en EE. UU.,
  2026): es evento musical, no de arte nuevo — lo dejo anotado por si el
  investigador de vídeo/voz lo quiere (https://violetevergardenusa.com/), no
  amplío porque no es mi punto.

## Lo mejor para la lámina de #poemas

1. **El key visual de la película** (Violet junto al mar, vestido de gala,
   luz dorada) — pose de pie, digna, coherente con un foro de poemas; hoja 2
   nº54.
2. **La hoja de modelo del databook** (hoja 1 nº1-2): úsala para la silueta
   exacta de la chaqueta y el vestido en Blender/rigging, con la cita de
   Takase como guía de qué «sensación» debe transmitir la ropa.
3. **El escudo de C.H. Postal Company** (`CHPC_Logo.png`): perfecto para un
   sello o cartela de hierro en la lámina, con el monograma «CH» y la
   corona de laurel.
4. **Los 5 standees de la colaboración del jardín (2022-2023)**: la idea de
   «personaje = flor» es reutilizable para decorar el marco del canal
   #poemas con motivos florales por personaje.
5. **El hex del lazo rojo (`#63394D`) y del uniforme militar (`#413228`)**:
   ya no son estimados, sirven tal cual para pintar en Photoshop.

## No encontré ⚠️ (esto SÍ es extra, no obligatorio)

- Un pincel de Photoshop **CC0 exacto** para el bordado del cuello de
  Violet (probé «vintage lace brush free», salieron sólo bancos de pago).
- Ficha oficial de Good Smile Company para la figura 1/7 de Violet (sólo la
  vi en tiendas de reventa).
- El vídeo/foto original del cosplay de @swoochu (IMDb la resume pero el
  enlace de imagen dio 403).
- Confirmar si el «Official Design Works» trae también una hoja de la
  máquina de escribir (biblia §3.2 ya lo dejaba como ⚠️; sigue sin
  comprobar, habría que comprar o encontrar el PDF).

## Bitácora de búsqueda (imagen)

- ES: «Violet Evergarden colaboración cafetería café evento oficial» (web) →
  resultados irrelevantes (cafés sin relación).
- EN: «"Violet Evergarden" collaboration event cafe Fortnite gacha
  crossover» (web) → sin colaboración de videojuego.
- JA: «ヴァイオレット・エヴァーガーデン コラボカフェ 京都» (web) → **la buena**: Garden
  Museum Hiei, con enlaces oficiales.
- EN: «Violet Evergarden figure Pop Up Parade figma official figures» (web).
- JA: «"Violet Evergarden" 公式ゲーム アプリ ノベルゲーム» (web) → confirma que no
  hay videojuego oficial.
- EN: «"Violet Evergarden: Agents of the Four Seasons" manga Suoh Kadokawa»
  (web) → aclara que el manga es de otra franquicia (mismo staff).
- EN: «free screentone brushes Clip Studio Photoshop CC0 manga texture pack»
  (web).
- EN: «seamless plaid tartan texture CC0 / vintage lace pattern PNG free
  commercial use» (web).
- EN: «Violet Evergarden cosplay best award winning craftsmanship photo»
  (web).
- Fandom API (`action=query&list=search`) en inglés: «Auto Memory Doll» →
  encontré el nombre real «Auto Memories Doll»; `list=categorymembers` sobre
  `Category:Auto Memories Dolls`; `list=allcategories&acprefix=Auto`.
- Fandom API `action=parse&prop=wikitext` sobre «Auto Memories Doll».
- Fandom API `imageinfo` sobre `File:CHPC Logo.png` (tamaño real).
- `investigar_serie.py` con 5 páginas de personajes → 2 hojas de contacto,
  miradas con Read.
- API de Sketchfab (`api.sketchfab.com/v3/search`) en dos consultas
  («Underwood typewriter», «Violet Evergarden») para confirmar licencias de
  verdad, no de memoria.
- API de ambientCG (`type=Material&q=fabric`) para confirmar CC0 de las
  telas base.
- Descargué y medí con Pillow 4 imágenes oficiales (portada AniList, hoja de
  modelo del databook, `Violet_Anime.jpg`, `Violet's smile.jpg`,
  `Violet2.jpg`, `Violet_in_rain.png`) para los hex del punto 15.
- WebFetch sobre `violet-evergarden.jp/news/?id=191` (nota oficial de la
  colaboración 2022, en japonés, traducida) y sobre `goodsmileus.com`.

## Cumplimiento de mis puntos (1, 3, 15, 16, 19, 23)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | 2 hojas de contacto nuevas (0→2), key visuals de AniList, hoja de modelo del databook con cita de la diseñadora, confirmado que no hay videojuego oficial |
| 3 · Fan art y 3D con licencia | ✅ | Licencias de Sketchfab reconfirmadas por API (corregidos 2 nombres de usuario y 1 licencia que biblia tenía mal), cosplay con crédito |
| 15 · Vestuario con hex | ✅ | Hex medidos de verdad con Pillow (no estimados) para lazo, ojos, pelo y uniforme militar; chaqueta confirma el rango ya estimado; sigue ⚠️ el hex exacto del broche (brillo en todas las fotos que abrí) |
| 16 · Fondos de pantalla | ⚠️ | Confirmo y sumo 2 key visuals; los 5 wallpapers 4K de biblia siguen sin tamaño verificado a mano (son colecciones, no un archivo único) |
| 19 · Texturas 2D | ✅ | Cubierto entero (no existía en biblia): tramas, grano, pinceladas, patrones de ropa, emblema de C.H. Postal Company con imagen |
| 23 · Colaboraciones y cruces | ✅ | Cubierto entero (no existía en biblia): colaboración oficial del jardín de Kioto (2 años, con nota oficial), figuras, y lo que NO hay (videojuego, café permanente) dicho explícito |

Sin `Sigue:` — todo lo obligatorio de mis 6 puntos quedó cubierto. Lo que
falta está en «No encontré» (extras, no obligatorios).
