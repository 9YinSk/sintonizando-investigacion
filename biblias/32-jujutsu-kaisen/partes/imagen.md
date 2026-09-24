# Investigador de IMAGEN · Jujutsu Kaisen

La biblia (`biblia.md`) ya cubre los puntos 1, 3, 15 y 16 de ENCARGO.md (arte
oficial, fan art y 3D, vestuario, fondos). **Esta parte es sólo los puntos 19
y 23**, que el encargo añadió y que no están en la biblia (comprobado con
`seccion.py --indice`: no hay sección de texturas 2D ni de colaboraciones).
Partí de `partes/datos-imagen.md` (portadas, imágenes de personajes, tags de
Danbooru, fan art de Safebooru, wallpapers de Wallhaven, modelos de Sketchfab,
fotos de Openverse): no repetí esas consultas, sólo las reuso donde encajan
aquí (cosplay de Openverse, en el punto 23).

## Punto 19 · Texturas 2D

### 19.1 Cómo está dibujado el manga (mirado, no de memoria)

Abrí en grande las celdas **T13, T15, T17 y T18** de
`hojas/pantalla_y_letras_01.jpg` (páginas reales del manga, ya bajadas por el
1.er/2.º ayudante para el punto 6; las volví a mirar para esto, no son
imágenes nuevas mías) y medí lo que hay, no lo que se supone que hay:

- **No hay trama de puntos (halftone/screentone clásico)** en ninguna de las
  4 páginas de acción que miré. Gege Akutami dibuja el volumen con **línea**:
  rayado paralelo fino a mano (T17: los escombros de Shibuya, decenas de
  líneas casi rectas muy juntas, no un patrón repetido), y **garabato suelto
  tipo "scratch"** para el pelo y las ondas de choque (T13, T15: trazos cortos
  irregulares que se cruzan, sin ángulo fijo). ✅ (visto en 4 páginas)
- **Negro sólido con grietas blancas**, no degradado: T18 (el dominio de
  Sukuna) es una silueta negra plana con líneas blancas en zigzag partiéndola
  (el "rayo" del Vacío/objetos rotos); no hay ni un gris intermedio. ✅
- Contraste **muy alto**: blancos puros y negros puros; el gris sólo aparece
  si el escaneo lo suaviza. Es el estilo "sucio a propósito" que se suele
  llamar *rough/scratchy* en los análisis de arte de shonen de pelea. ⚠️
  (interpretación mía sobre 4 páginas, no sobre las 30 páginas de la hoja
  completa ni sobre los tomos en papel)
- El **grano de papel** real de la edición impresa no lo pude medir (no tengo
  un escaneo del tomo físico, sólo el redibujado digital de la wiki): lo dejo
  en «No encontré».

### 19.2 Patrones de ropa y de piel (mirado y medido)

| Qué | Cómo es | Fuente | ✅/⚠️ |
|---|---|---|---|
| **Tatuajes de la forma real de Sukuna** | marcas moradas oscuras en forma de **corchete/gancho** (⊃⊂) en hombros y pecho, **puntos negros grandes** sobre cada hombro, **muñequeras con lunares** en el mismo tono | portada del tomo 29 (2598×3980), medida con `estilo.py`: paleta `#010100` 29% (negro), `#6E3737`/`#9B524D` (piel en sombra), sombreado **mixto** (línea `#512827`) | ✅ (imagen oficial + descripción de la wiki en inglés) |
| **Kimono de Sukuna como poseedor** (cuerpo de Megumi o de Yuji) | **liso, sin estampado**: haori **negro**, kimono **blanco** debajo, camiseta interior negra, **cinturón negro**, pantalón blanco, sandalias negras | wikitext de la página «Sukuna» (`action=parse`, sección de apariencia) | ✅ (texto de la wiki) |
| ⚠️ **Corrección**: varias guías de cosplay (§23.4) dibujan a Sukuna con un **haori rojo con llamas**: no es el diseño oficial del anime/manga (que es negro liso); es una licencia de las tiendas de cosplay para que se le note el color. Lo aviso para que no se use como referencia de color. | | costumary.com (§23.4) vs. la wiki | ⚠️ contradicción encontrada, no resuelta a favor del cosplay |
| **Uniforme de la Escuela de Tokio** | chaqueta azul oscuro asimétrica, cuello alto; **dos pines a la izquierda con el logo grabado**; **los botones tienen la forma del emblema del colegio** | wikitext de «Tokyo Metropolitan Curse Technical College» | ✅ (texto de la wiki) + confirmado en imagen (19.3) |
| **Sudadera de Nobara fuera del uniforme** | blanca y azul, con un **patrón de flores** | wikitext de «Nobara Kugisaki» (Appearance) | ⚠️ una sola fuente: no encontré una foto nítida del estampado para medirlo (búsqueda en la wiki por «tracksuit»/«casual», sin imagen con ese nombre) |

### 19.3 Emblemas y logos (encontrado mirando, no buscando el nombre)

**El escudo de la Escuela Superior de Hechicería** no estaba descrito en
ninguna parte de la biblia. Lo encontré en un fotograma que ya estaba
indexado (carnet de estudiante de Yuta, `Yuta's Jujutsu High ID (Anime).png`,
1920×803, wiki) y lo **recorté en grande** para verlo bien:

- Es un **cuadrado negro** con un **remolino/espiral blanco de cuatro brazos**
  dentro de un aro blanco (como una tormenta o energía maldita girando; no es
  un *mon* tradicional de flor o ave, es abstracto). Aparece dos veces en el
  mismo fotograma: en la esquina del carnet y **como botón dorado** en el
  cuello de la chaqueta de Yuta (medido a ×4, se ve el mismo dibujo grabado
  en metal). ✅ (una imagen, dos apariciones del mismo símbolo)
- **Segunda fuente, independiente**: el objeto cosmético «**Jujutsu Kaisen
  Emblem**» de la colaboración con *Fortnite* (Epic Games, 2023; wiki oficial
  del juego) es el **mismo remolino, en rojo**, sobre un fondo negro
  agrietado. Dos fuentes distintas (un fotograma del anime y un asset de
  videojuego con licencia oficial de Shueisha) dibujan el mismo símbolo. ✅✅
  · [Jujutsu Kaisen Emblem, Fortnite Wiki](https://fortnite.fandom.com/wiki/Jujutsu_Kaisen_Emblem)
  (256×256, medido) · [carnet de Yuta](https://static.wikia.nocookie.net/jujutsu-kaisen/images/5/54/Yuta%27s_Jujutsu_High_ID_%28Anime%29.png) (1920×803, medido)
- El **logo 呪術廻戦** en sello/篆書 y sus variantes ya están en la biblia
  (§6.1): no lo repito.

### 19.4 Texturas y pinceles libres equivalentes (con licencia)

| Para qué capa | Recurso | Licencia (tal cual la dice el sitio) | ✅/⚠️ |
|---|---|---|---|
| **Trama de manga** (tonos, si hace falta un degradado plano en vez del rayado a mano) | [«[FREE] Manga Screentone Pack 1»](https://assets.clip-studio.com/en-us/detail?id=2142037), autor Aku86941878, en Clip Studio Assets | Gratis, sujeto a los términos de CLIP STUDIO ASSETS (no dice restricción de uso comercial en la ficha) | ⚠️ (leer los términos generales del sitio antes de usar en algo que se publique) |
| **Trama de manga**, alternativa | [Comic/Manga Screentone Brushes, GraphicsBunker](https://www.graphicsbunker.com/brushes/free-comic-manga-screentone-brushes/) (se bajan poniendo «$0» en Gumroad) | el sitio no deja el texto de licencia claro en la página (lo comprobé, no cargó) | ⚠️ sin confirmar |
| **Pinceladas de tinta** (para imitar el rayado de T13/T17) | [Manga Brushes, MyPhotoshopBrushes](https://myphotoshopbrushes.com/resources/3790/manga-brushes) (1 lápiz, 1 pluma, 2 de tramado cruzado, 1 puntillismo, 1 textura) | **Free for Commercial Use**, lo dice la propia ficha | ✅ |
| **Pinceladas de tinta**, más variedad | [Comic Inking Brushes, Brusheezy](https://www.brusheezy.com/brushes/18074-comic-ink-brushes-by-mateo) | Brusheezy: gratis, revisar la licencia de cada autor (varía) | ⚠️ revisar por pincel |
| **Emblemas/mon** (para un escudo genérico de estilo japonés, no el de JJK) | [Japanese Family Crest Kamon, SVG Repo](https://www.svgrepo.com/svg/80546/japanese-symbol-family-crest-kamon) | el sitio dice licencia libre para uso comercial en su ficha general, pero **no pude confirmarlo hoy** (bloqueó la descarga automática dos veces con un chequeo anti-bot) | ⚠️ confirmar a mano antes de usar |
| **Grano de papel** (el de la impresión, no lo medí en un escaneo real) | ya cubierto por Poly Haven/ambientCG en §5.3 de la biblia (papel de talismán); sirve igual para «papel de manga» sin degradado | CC0 | ✅ (ya en la biblia, no repito el enlace) |

## Punto 23 · Colaboraciones y cruces

### 23.1 Moda y marcas (todas en 2025-2026, la serie está en su pico)

| Marca | Qué es | Fuente | ✅/⚠️ |
|---|---|---|---|
| **Uniqlo UT** («MANGA UT», 100.º aniversario de Shueisha) | 4 diseños de camiseta con arte de portadas y de la pelea de Shibuya; **vista y medida**: la trasera trae a Yuta con espada, Todo, Maki, Higuruma, Kusakabe, Mei Mei, Choso y Rika peleando contra Sukuna, en una composición vertical nueva (no es un fotograma existente, es un collage hecho para la camiseta) | [hypebeast](https://hypebeast.com/2026/1/shueisha-100th-anniversary-uniqlo-ut-collaboration-collection-release-info-t-shirts-manga-jujutsu-kaisen-hunter-x-hunter-yu-yu-hakusho) · [soranews24](https://soranews24.com/2026/01/17/massive-manga-collaboration-bringing-100-years-of-shueisha-manga-to-uniqlo-t-shirts%E3%80%90photos%E3%80%91/) · [cbr](https://www.cbr.com/jjk-uniqlo-america-release-first-look/) · imagen oficial [uniqlo.com](https://image.uniqlo.com/UQ/ST3/us/imagesgoods/487560/item/usgoods_00_487560_3x4.jpg) (1500×2000, medida) | ✅ (3 fuentes + imagen propia) |
| **HUGO** (Hugo Boss) × Jujutsu Kaisen | cápsula «streetwear»: chaquetas reversibles, camisas de bolos oversize, denim; **vista**: camiseta azul con foto en blanco y negro de Yuji y Megumi tipo carné, «JuJuTsu Kaisen» en letras de grafiti amarillo | [nota oficial de Hugo Boss](https://group.hugoboss.com/en/newsroom/news/news-detail/hugo-x-jujutsu-kaisen-a-style-curse-you-dont-want-to-break) · imagen oficial (1200×675, medida) | ✅ (fuente oficial de la marca + imagen propia) |
| **Under Armour** × Jujutsu Kaisen | camisetas de compresión HeatGear, edición limitada; **vista**: logo 呪術廻戦 bordado, un brazo con dragón/sombra de Megumi bordado en una manga, la mano ensangrentada de Sukuna estampada en la otra | [nota oficial de Under Armour](https://about.underarmour.com/en/stories/2025/10/under-armour-and-jujutsu-kaisen-unleash-limited-edition-heatgear.html) · imagen oficial (1280×720, medida) | ✅ (fuente oficial + imagen propia) |
| **Subtitle** × Jujutsu Kaisen (con TOHO) | cápsula de 18 piezas, $65-220 | [hypebeast](https://hypebeast.com/2026/3/subtitle-jujutsu-kaisen-apparel-collection-release-info) | ⚠️ una fuente |
| SYUNSOKU (calzado) × Jujutsu Kaisen | zapatillas de Gojo Satoru | listado en eBay (revendedor, no oficial) | ⚠️ sin confirmar en fuente oficial |

### 23.2 Videojuegos y apps: colaboraciones (no los juegos propios de la
franquicia, ésos van en el punto 11 de la biblia)

| Con qué juego | Qué trajo | Fuente | ✅/⚠️ |
|---|---|---|---|
| **Fortnite** (Epic Games) | **2 oleadas**: 2023 (Yuji, Megumi, Nobara, Gojo, skins jugables, «Break the Curse!»); **feb-2026 oleada 2** (Sukuna, Toji Fushiguro, Mahito). **Vista**: el skin de Gojo en Fortnite lo recolorean **morado** (no es el azul/negro canon) y simplifican el cuello alto; 256×256, medido. También hay un **wrap** «Jujutsu Kaisen Emblem» (el remolino en rojo, §19.3) y una pantalla de carga «Jujutsu Sorcerers» | [esports.gg, oleada 2](https://esports.gg/news/fortnite/jjk-wave-2-fortnite-collaboration-all-skins-prices-and-more/) · [dexerto](https://www.dexerto.com/fortnite/fortnite-jujutsu-kaisen-collab-release-date-skins-2232902/) · [Fortnite Wiki, categoría](https://fortnite.fandom.com/wiki/Category:Jujutsu_Kaisen_Set) · imagen propia del skin de Gojo | ✅ (3 fuentes + imagen propia) |
| **Puzzle & Dragons** (GungHo) | colaboración desde el 28-sep-2021: personajes de 6 a 8 estrellas (Yuji, Gojo, Megumi, Nobara, Inumaki, Panda) en la «JUJUTSU KAISEN Egg Machine» | [Crunchyroll News (oficial de la distribuidora)](https://www.crunchyroll.com/news/latest/2021/9/27/jujutsu-kaisen-kicks-off-collab-with-mobile-game-puzzle-dragons) · [Pocket Gamer](https://www.pocketgamer.com/puzzle-dragons/puzzle-dragons-x-jujutsu-kaisen-collab-brings-special-dungeons-and-a-twitter-giv/) | ✅ (2 fuentes) |
| **Monster Strike** (Mixi) | ya van **3 colaboraciones**; la última (jul-2026, tras acabar la T3) añade «verdadera forma bestial» de Yuji, Nanami y Gojo. **Sólo en japonés/chino**: el servidor en inglés cerró en 2017 | [screenrant](https://screenrant.com/jujutsu-kaisen-monster-strike-july-2026-new-season/) · [cbr](https://www.cbr.com/jujutsu-kaisen-monster-strike-new-2026-update/) | ✅ (2 fuentes) |

### 23.3 Eventos, cafés y tiendas (todo en Japón)

| Qué | Cuándo/dónde | Fuente | ✅/⚠️ |
|---|---|---|---|
| **Café oficial «呪術廻戦カフェ» 5.º aniversario** | jul-sep 2026, en Tokio (Shinjuku), Nagoya y Osaka; menú y mercancía con Yuji, Megumi, Choso, Yuta, Hakari, Kirara, Higuruma y Naoya | [web oficial del café, menú](https://jujutsukaisen-cafe.jp/cafe_menu/) | ✅ (fuente oficial del evento) |
| **Café × Sanrio Characters** («Kaigyoku·Gyokusetsu») | jun-jul 2025, Tokio/Osaka/Nagoya; menú ¥2.690, tarjeta coleccionable | [jw-webmagazine](https://jw-webmagazine.com/tips/jujutsu-kaisen-x-sanrio-cafe-collaboration-in-japan-2025/) · [web del café](https://jujutsu-sanrio-cafe.theme-cafe.jp/cafe_menu/) | ✅ (2 fuentes) |
| **Sweets Paradise** (2.ª colaboración) | ene-feb 2025, varias tiendas | [web oficial de Sweets Paradise](https://www.sweets-paradise.jp/collaboration/jujutsukaisen2) | ✅ (fuente oficial) |
| **Universal Studios Japan** («Universal Cool Japan») | comida y mercancía temática | [tdrexplorer](https://tdrexplorer.com/jujutsu-kaisen-universal-cool-japan-food-merchandise-at-universal-studios-japan/) (la página no cargó el texto al leerla automáticamente hoy, me quedo con el resumen del buscador) | ⚠️ una fuente, sin poder confirmar el detalle a mano |
| **Lawson** (tienda de conveniencia) | mercancía y comida con ilustraciones nuevas de Gojo, Nobara y Yuji; también con la peli «Hidden Inventory/Premature Death» (jun-2026) | [anitrendz](https://anitrendz.net/news/2021/09/02/jujutsu-kaisen-teams-up-with-lawson-for-food-and-goods/) · [essential-japan](https://essential-japan.com/news/lawson-launches-huge-new-jujutsu-kaisen-collab-launches-this-june/) | ✅ (2 fuentes) |
| **Gyukaku** (restaurante de yakiniku) | colaboración de comida | [gamerant](https://gamerant.com/jujutsu-kaisen-gyukaku-collab/) | ⚠️ una fuente |
| **Restaurante en el Sunshine City Prince Hotel** | menú temático | [web del hotel](https://www.princehotels.co.jp/sunshine/restaurant/contents/jujutsukaisen/) (japonés) | ⚠️ una fuente, en japonés, no traducida |

### 23.4 Figuras oficiales (pose = referencia 3D real) y cosplay

**Figuras**: catálogo oficial en
[goodsmile.info/en/jujutsukaisen](https://www.goodsmile.info/en/jujutsukaisen)
(Good Smile Company): **Nendoroid** de los 5 protagonistas más Maki, Inumaki,
Nanami, Panda, Sukuna, Geto, Toji, Shoko y Choso; línea **POP UP PARADE**; y
**figma** de 7 personajes. ✅ (catálogo oficial del fabricante).

Premios de tómbola (**Ichiban Kuji**, Bandai Spirits/Banpresto), con **pose
descrita** para cada uno:

- «Jujutsu Kaisen 5th Anniversary FINAL!» (26-sep-2026): Premio A = **Yuji de
  pie, 23 cm**, con la sonrisa de cuando entró a la escuela (antes de
  Shibuya); Premio B = **Yuta sonriendo**, el momento final de la película
  *JJK0*. ✅ [toy-people.com](https://www.toy-people.com/en/?p=109742) ·
  [yasuee.com](https://yasuee.com/news/ichiban-kuji-jujutsu-kaisen-5th-anniversary-final-yuji-yuta-gojo-figures-revealed) (2 fuentes)
- «Grandista - Maki Zen'in -»: **Maki en pose de combate, sosteniendo la
  Nube Juguetona (lanza) en alto**. ⚠️ [toy-people.com](https://www.toy-people.com/en/?p=107825) (una fuente)

**Cosplay** (con materiales reales, no genérico):

- Guías con lista de materiales y presupuesto (Costumary): **Sukuna**
  ($150-350, 6 semanas): pintura corporal roja/negra/blanca, peluca spiky
  carmesí, kimono negro de tela algodón/mezcla con entretela pesada en el
  cuello, uñas press-on; **Gojo** ($90-240, 5 semanas): gabardina/twill negro
  con patrón de chaqueta mandarina, cremallera separadora, peluca blanca,
  jersey negro para la venda, botas. ⚠️ (una fuente, sitio de guías, no un
  cosplayer concreto; costo y semanas son estimaciones del sitio) ·
  [costumary.com/sukuna](https://www.costumary.com/templates/jujutsu-kaisen/sukuna) ·
  [costumary.com/gojo-satoru](https://www.costumary.com/templates/jujutsu-kaisen/gojo-satoru)
- Cosplay de **Maki pre-Shibuya**, con su lanza, hecho por «Kerocchi» y
  publicado en Reddit. ⚠️ una fuente, sin enlace directo a la publicación ·
  [cbr.com](https://www.cbr.com/jujutsu-kaisen-cosplay-maki-pre-shibuya-incident/)
- **Fotos reales con licencia libre** (ya estaban en `datos-imagen.md`, las
  reuso aquí porque son exactamente esto: cosplay con materiales y volumen
  reales, de una convención en Francia en 2021): Gojo (819×1024), Megumi
  (1024×767, 3 tomas) y Sukuna (683×1024), todas de **timz2011** y
  **esby.photo** en Flickr, CC BY-NC-SA 2.0, vía Openverse. ✅ (fotos, no de
  segunda mano)
- **No encontré** un cosplay premiado en concurso oficial (AnimeJapan,
  Comic-Con) con nombre y fecha: las búsquedas devolvieron premios del anime
  (Crunchyroll Anime Awards), no de cosplay.

## Lo mejor para la lámina

1. **El remolino de la Escuela de Tokio** (§19.3): un emblema real,
   geométrico, fácil de vectorizar en Illustrator/Blender, confirmado en dos
   fuentes independientes (el carnet del anime y el wrap de Fortnite). Sirve
   como sello, botón o marca de agua para un canal de doblaje.
2. **La combinación Under Armour**: logo 呪術廻戦 bordado + brazo con dragón +
   mano ensangrentada de Sukuna en la otra manga: una plantilla lista de
   «cómo poner un símbolo de la serie sobre una prenda» sin que parezca un
   parche pegado.
3. La corrección de **Sukuna sin estampado de llamas** (§19.2) evita el
   error más repetido en fan art/cosplay: el haori es negro liso.
4. Camiseta de **Uniqlo** con el collage de personajes en diagonal: un
   ejemplo real de cómo comprimir a 8 personajes en una composición vertical
   sin que se pisen (útil si la lámina 2 necesita meter a todo el reparto).
5. Las **fotos de cosplay de Openverse** (licencia libre, ya bajadas): sirven
   para ver de qué tela y grosor son la chaqueta de Gojo y el uniforme de
   Megumi en volumen real, no dibujado.

## No encontré

- ⚠️ El **grano de papel** de una edición impresa real del manga (sólo tengo
  el redibujado digital de la wiki): busqué «呪術廻戦 原稿» y «screentone» sin
  una foto de una página física.
- ⚠️ La licencia exacta de GraphicsBunker y de SVG Repo (ambos bloquearon la
  lectura automática hoy): antes de usarlos, alguien tiene que abrirlos a
  mano y leer la licencia.
- ⚠️ Una foto nítida y con nombre del **patrón de flores** de la sudadera de
  Nobara (sólo la descripción en texto de la wiki).
- ⚠️ El contenido completo de la página de Universal Studios Japan (el
  lector automático la devolvió vacía dos veces; me quedé con el resumen del
  buscador, que puede tener menos detalle del real).
- ⚠️ Un cosplay premiado en un concurso con nombre, fecha y jurado (AnimeJapan
  o similar): sólo casos sueltos compartidos en Reddit/Instagram.
- Colaboración con **Puma**: la busqué porque otras marcas deportivas sí
  colaboraron (Under Armour); no encontré ninguna con Jujutsu Kaisen, sólo
  con Pokémon. Lo dejo dicho para que no se dé por hecho.

## Bitácora de búsqueda (imagen · puntos 19 y 23)

**Red directa** (sin gastar cupo de buscador): API de Jujutsu Kaisen Wiki
(`action=parse` en *Sorcerer Clan/Zenin Clan*, *Tokyo Metropolitan Curse
Technical College*, *Sukuna*; `action=query&list=search` para «emblem OR
crest OR badge», «Nobara tracksuit»); API de Fortnite Wiki
(`list=categorymembers` en *Category:Jujutsu Kaisen Set*, `imageinfo` de 4
archivos); descarga directa y medida con Pillow de 6 imágenes (carnet de
Yuta, portada del tomo 29 de Sukuna, camiseta de Uniqlo, skin de Gojo y
emblema de Fortnite, imágenes de Hugo Boss y Under Armour); `estilo.py` sobre
la portada de Sukuna.

**Buscador web** (17 búsquedas, todas en inglés salvo la 5.ª y 6.ª en
japonés): Uniqlo UT · café oficial (parte en japonés) · figuras Good Smile ·
colaboraciones con apps móviles · crest del clan Zenin (japonés) · trama del
manga (japonés, sin resultado útil) · Fortnite · tutoriales de cosplay ·
pinceles de trama libres · patrón del kimono de Sukuna · Modulo/Colopl (sin
resultado útil: es un manga, no un juego) · insignia del uniforme · Puma
(sin resultado) · Ichiban Kuji · cosplay premiado (sin resultado útil) ·
pinceles de tinta libres · kamon libre en SVG · figuras Good Smile (2.ª,
para la imagen).

**Bloqueado o vacío**: `patterncosplay.com` (dos intentos, contenido vacío);
`tdrexplorer.com` (bloqueó la lectura automática); `svgrepo.com` (chequeo
anti-bot, dos intentos); `myfigurecollection.net` (carga con JavaScript, sin
imagen directa); `graphicsbunker.com` (cargó pero sin el texto de licencia
visible). En cada caso probé una vía alternativa (buscador, otra web) antes
de dejarlo en ⚠️.

Sigue: nada obligatorio pendiente de los puntos 19 y 23. Si hay tiempo:
confirmar a mano la licencia de SVG Repo y de GraphicsBunker, y buscar una
foto nítida del patrón de flores de la sudadera de Nobara.
