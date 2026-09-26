# Parte del investigador de IMAGEN · SpongeBob (Bob Esponja)

Puntos de ENCARGO.md: **1** (arte oficial variado), **3** (fan art y 3D con
licencia), **15** (vestuario con hex medidos), **16** (fondos de pantalla),
**19** (texturas 2D) y **23** (colaboraciones y cruces).

Repaso con la red abierta. Parto de `partes/datos-imagen.md` (no repito esas
consultas) y de lo que ya hay en `biblia.md` (secciones 3, 4, 5, 16, 17 y 20
vistas con `seccion.py --rol imagen`). El recolector automático había fallado
con Fandom en «Don Cangrejo» y «Calamardo»: repetí con los nombres en inglés
(`Eugene H. Krabs`, `Squidward Tentacles`, `Sheldon J. Plankton`, `Patrick
Star`, `SpongeBob SquarePants (character)`, `Krusty Krab`) y sí funcionó.

Formato: un dato por línea, con fuente(s) y ✅/⚠️.

---

## Hallazgos

### Punto 1 · Arte oficial, en cantidad y variado

**Hojas de contacto — nuevas (la biblia no tenía ninguna)**

- `investigar_serie.py --wiki spongebob --paginas "Eugene H. Krabs" "Squidward
  Tentacles" "SpongeBob SquarePants (character)" "Patrick Star" "Sheldon J.
  Plankton" "Krusty Krab"` → **254 imágenes enlazadas, 214 grandes, 5 hojas**
  en `herramientas/referencias/spongebob-squarepants/` ✅ (vistas las 5 con
  Read). Quedaron 3 en `hojas/`:
  - `personajes_01.jpg` (hoja 1 del lote): stock art de cuerpo entero de Bob,
    Calamardo, Don Cangrejo, Patricio y Plankton; renders 3D de *Kamp Koral* y
    de *Nickelodeon All-Star Brawl 2*; interiores del Crustáceo; la billetera
    de Don Cangrejo con su identificación de Fondo de Bikini (imagen 39).
  - `fondos_01.jpg` (hoja 2): el Crustáceo por fuera en **distintas horas y
    estaciones** (de noche con farolillos, nevado en Navidad, de día),
    interiores variados (cocina, oficina, el ring de *Hot Crossed Nuts*),
    página de cómic (*SpongeBob Comics* #36), el cartel del **Nut Shack**
    (imagen 88) y capturas de las pantallas «Krusty Krab Training Video».
  - `objetos_01.jpg` (hoja 5): **ficha Pantone de colores oficiales**
    (imagen 196, ver §15), la licencia de conducir de Bikini Bottom de
    Patricio (imagen 200), bocetos de diseño de personaje («Design-patrick»,
    «Crabs-Stephen-Hillenburg-1996», imágenes 203-204 y 211), y un cuadro
    en el mundo, «The Clam Calamity of 1912» (imagen 214), útil como textura
    de cartel antiguo.

**El «Main Model Pack»: ya se pudo ver (antes ⚠️, «no pude ver las páginas»)**

- Página completa en Fandom ✅ ([Main Model Pack](https://spongebob.fandom.com/wiki/Main_Model_Pack)):
  es el libro de referencia de Nickelodeon Animation Studio (1999-2016), con
  las páginas de construcción de cada personaje principal y notas debajo.
  Originalmente 8 personajes: Arenita (bañador y traje espacial), Bob,
  Patricio, Calamardo, Don Cangrejo, Sra. Puff y Perla; luego Gary, y tras la
  película de 2004, Plankton (Karen fue al «BG Layout Stock Pack» porque es
  un objeto, no un personaje). Fuente secundaria del dato ✅: foto de Vincent
  Waller (director de arte) en Twitter, citada en la wiki, y un especial de
  making-of, *Show Design*, del DVD **Nautical Nonsense and Sponge Buddies**
  (12 de marzo de 2002), minuto **18:00** (`t=1080`).
- Vi `Season 1 Complete Model Pack.png` (909×532, [Fandom](https://static.wikia.nocookie.net/spongebob/images/9/9a/Season_1_Complete_Model_Pack.png/revision/latest?cb=20190218054312)):
  foto real del cuaderno físico abierto sobre la mesa de un animador, con
  pinceles y botes de pintura alrededor; se ve una lámina de fondo (rocas,
  niebla) y las siluetas en color de Patricio, Bob, Calamardo y Don Cangrejo
  recortadas y pegadas encima. ✅ visto.
- **«SpongeBob Main Characters» — hoja de modelo oficial a color, 2200×2200**
  ✅ visto y medido ([Fandom](https://static.wikia.nocookie.net/spongebob/images/f/fa/SpongeBob-Main-Characters-sheet-color.jpg/revision/latest?cb=20260405224319)):
  turnaround de cuerpo entero (página 1: Arenita en bikini, Arenita con
  traje espacial y flor en la burbuja, Gary, Bob, Patricio con short verde
  de flores moradas; página 2: Calamardo, Don Cangrejo, Sra. Puff, Perla
  como ballena con corazón). Es la referencia de vestuario más limpia que
  hay (usada para medir hex en §15).

**Campañas del 25.º aniversario (2024): antes ⚠️ «no pude abrir las
páginas», ahora vistas y descritas**

- **«25 con medusas»** (AWN, 620×413, [imagen](https://www.awn.com/sites/default/files/styles/inline/public/image/featured/25_anniversary_jellyfish_final-1280.jpg)):
  key art con **los 6 personajes principales cazando medusas con redes de
  mariposa** (pose de acción y de objeto en mano): Don Cangrejo, Patricio,
  Bob (con red y lengua fuera) y Calamardo corriendo en fila por el césped;
  Gary detrás; Arenita **con su traje espacial**, red en mano, flotando
  arriba; Plankton escondido espiando bajo una hoja; encima, un enjambre de
  medusas rosas forma el número «25». Fondo pintado con degradado turquesa y
  coral morado. ✅ visto.
- **«25 con burbuja de flor»** (AWN/PR Newswire, 620×652, [imagen](https://www.awn.com/sites/default/files/styles/inline/public/image/attached/1062874-25anniversarybubblefinalforpressonly-1280.jpg)):
  **foto de grupo mirando a cámara**: Bob soplando una burbuja enorme con
  forma de flor que dibuja el «25»; a su lado Don Cangrejo, Arenita
  (abrazándolo, traje espacial), Patricio, Calamardo y Gary. Fondo de coral
  morado bajo el agua. ✅ visto. Sirve como pose de «grupo feliz,
  presentando» para el concepto 2.
- Ambas confirmadas también en [NickALive (8-jul-2024)](https://www.nickalive.net/2024/07/nickelodeon-unveils-happy-25th.html)
  y [PR Newswire](https://www.prnewswire.com/news-releases/nickelodeon-commemorates-25-years-of-spongebob-squarepants-with-larger-than-life-tribute-to-original-pilot-episode-at-comic-con-international-san-diego-2024-302193519.html) ✅✅.
  Estilo medido con `estilo.py`: **degradado/pintado** (no plano como los
  fotogramas de episodio), saturación 41-51%, línea gris rosada suave —
  distinto del cel-shading de la serie (dato para el punto 18, que no es
  mío, pero lo dejo anotado).
- Making of / entrevistas del 25.º: declaraciones de Tom Kenny (Bob), Bill
  Fagerbakke (Patricio), Carolyn Lawrence (Arenita), Rodger Bumpass
  (Calamardo), Clancy Brown (Don Cangrejo) y Mr. Lawrence (Plankton) en el
  mismo artículo de AWN ✅.

**Logo oficial**

- `SVG SpongeBob SquarePants.svg` (600×600, vector, [Fandom](https://static.wikia.nocookie.net/spongebob/images/4/46/SVG_SpongeBob_SquarePants.svg/revision/latest?cb=20181117230211)):
  colores exactos leídos del propio SVG ✅: relleno `#FFF463` (amarillo del
  título), contorno `#B2B618`/`#919107` (verde-oliva), rojo `#EF5240`/`#EB1C22`,
  marrón `#B26E2D`.

### Punto 3 · Fan art y 3D con licencia (comprobado por la API, no sólo la
página web)

La biblia tenía 7 modelos con licencia «según la búsqueda» ⚠️. Repetí la
consulta con la **API real** de Sketchfab (`/v3/search?type=models&q=…`):

| Modelo | Autor | Licencia (API) | Nota |
|---|---|---|---|
| [BFBBR - Krusty Krab Cash Register](https://sketchfab.com/3d-models/none-cc79260fc5f44d73b8268f68dfb83a3f) | SMF Features Developed From Cheryl Hill | **CC Attribution** ✅ (confirmado por API) | sacado del juego *Rehydrated* (THQ Nordic); mirar, no publicar |
| [The Krusty Krab](https://sketchfab.com/3d-models/none-e109df8b1cb1487dbf2553e5e2d7eff1) — Mrlunettes | Mrlunettes | **CC Attribution-NonCommercial** ✅ (la biblia decía «CC BY», es más restrictiva: **no comercial**) | interior y exterior, fan-made |
| [Mr Krabs (Spongebob)](https://sketchfab.com/3d-models/none-d7e712d733ae4de69623cd408d68a289) | Yanez Designs | **CC Attribution** ✅ | **nuevo**: no estaba en `datos-imagen.md` |
| [Krabby Patty (Spongebob)](https://sketchfab.com/3d-models/none-6bf2dc6ffc594a8598bcf84f5d0325f1) | Yanez Designs | **CC Attribution** ✅ | **nuevo**; objeto suelto, fácil de usar en Blender |
| [Krusty Krab Employee Hat (Spongebob)](https://sketchfab.com/3d-models/none-8d0e167b2eef4c9d8b99bfd4823d9329) | Yanez Designs | **CC Attribution** ✅ | **nuevo**; accesorio de vestuario |
| [Krusty Krab Menu (Spongebob)](https://sketchfab.com/3d-models/none-2d19327e22284f7e85ffd444e55bbbc8) | Yanez Designs | **CC Attribution** ✅ | **nuevo**; sirve para el objeto del canal (precios) |
| [Jelly Fish (Spongebob)](https://sketchfab.com/3d-models/none-4227c0c46a1640ef9c61c455f7bc10f7) | Yanez Designs | **CC Attribution** ✅ | **nuevo** |
| [The SpongeBob Squarepants](https://sketchfab.com/3d-models/none-74e87e0af5b2495792d8068d561fd816) | Pixel | **CC Attribution** ✅ | **nuevo**, personaje completo |
| [Plankton](https://sketchfab.com/3d-models/none-683b0ce1f9324ae9ba59bcda10a18d80) | 1ooooJ0Y | **CC Attribution** ✅ | **nuevo** |
| [Sandy Bikini](https://sketchfab.com/3d-models/none-ee46def4864945198c053754725f9a9a) | Placidone | **CC Attribution** ✅ | **nuevo** |
| [Cash Register](https://sketchfab.com/3d-models/none-1e04d7a73a004e2380e2ee715ce7bd06) | BumBácBonifác | descarga gratis (sin CC explícita en la API) ⚠️ | caja genérica, la más segura como base |
| The Krusty Krab! — pizzabrian | — | no reapareció en la búsqueda por API ⚠️ | no reconfirmado esta vez |

**Recomendación reforzada**: el catálogo de **Yanez Designs** (Mr. Krabs, la
Krabby Patty, el gorro de empleado, el menú, la medusa) es CC Attribution
confirmado por API y da piezas sueltas fáciles de recombinar en Blender —
mejor opción que modelar todo desde cero. Crédito: «*Título* por Yanez
Designs, CC BY 4.0, Sketchfab».

### Punto 15 · Vestuario, colores medidos (antes 11 ⚠️ de memoria)

**Colores de producción oficiales (ficha Pantone, la mejor fuente posible)**

`SpongeBob-character-model-colors-Pantone.jpg` (800×1100, [Fandom](https://static.wikia.nocookie.net/spongebob/images/8/8c/SpongeBob-character-model-colors-Pantone.jpg/revision/latest?cb=20210313185736),
usada en las páginas de Arenita, Sra. Puff y Bob) ✅✅ (es la hoja de color
que usa el propio estudio; la vi y transcribí):

| Personaje | Parte | Pantone | CMYK |
|---|---|---|---|
| Bob | cuerpo (frente) | 101 | C0 M0 Y70 K0 |
| Bob | corbata / raya del calcetín | 1788 | C0 M100 Y100 K0 |
| Bob | raya superior del calcetín | 2718 | C0 M40 Y0 K0 |
| Bob | iris | 298 | C60 M0 Y0 K0 |
| Bob | pantalón | 723 | C30 M60 Y100 K0 |
| Bob | sombra del pantalón | 724 | C30 M70 Y100 K3 |
| Bob | tinta de todo el cuerpo | 392 | C45 M25 Y100 K1 |

(Arenita y Sra. Puff no son mis personajes prioritarios; dejo su tabla
completa para el redactor si hace falta, están en la imagen.)

**Medidos con `estilo.py` sobre la hoja de modelo oficial
«SpongeBob-Main-Characters-sheet-color.jpg» (recortes por personaje)**

- **Don Cangrejo** ✅ (antes «de memoria + paleta de fans»): cuerpo/pinzas
  **rojo `#F04A3E`**, camisa **azul claro `#A5C9D2`**, pantalón **morado-azul
  `#77719B`**, brillo de pinza `#FCAB9A`.
- **Calamardo** ✅ (antes «de memoria»): piel **verde menta `#B6D5CA`**
  (sombra `#CBE6DC`), camisa/cuello **marrón `#866E4B`**.
- **Patricio** ✅ (antes «de memoria»): piel **rosa salmón `#FE9285`** (rosa
  más oscuro `#EC5240` en sombras), short **verde `#B2E638`** con **flores
  moradas `#9E71D1`** — confirma y mide lo que antes era sólo texto.

**Medidos con `estilo.py` sobre stock art individual (además, cruce con lo
de arriba)**

- Don Cangrejo (`Eugene_Krabs.png`, 3000×3000): rojo `#D34835`, camisa azul
  claro `#C1DAE6`, azul más oscuro `#7797BD`. ✅ coincide con la hoja de
  grupo (mismo rango de rojo y azul).
- Calamardo (`Squidward_unhappy_stock_art.png`, 3500×3500): piel
  `#C3DDD3`/`#8AA8A3`. ✅ coincide.
- Patricio (`Patrick_stock_art_(oil_painted).png`, 2500×2500): piel
  `#F4B1B5`, rosa oscuro `#EB716B`, amarillo-verde `#CCD428` (flor/short).
  ✅ coincide.

**Plankton — del SVG oficial de la wiki (colores exactos, no aproximados)**

`Sheldon_Plankton.svg` (600×600, [Fandom](https://static.wikia.nocookie.net/spongebob/images/2/22/Sheldon_Plankton.svg/revision/latest?cb=20191117042039)),
hex leídos directamente del código del vector ✅✅ (reemplaza el
`#68A079` «de paleta de fans»):
- Cuerpo verde oscuro **`#00613B`**, verde claro (brillo) **`#6FA48C`**.
- Antenas / contorno **`#231F20`** (casi negro).
- Ojo **`#F14829`** (rojo-naranja), con un rojo más oscuro **`#861810`**.
- Patas del exoesqueleto **`#94A0CE`** / **`#C3CADE`** (azul grisáceo).

**Conclusión para el redactor**: la tabla de vestuario del §16 de la biblia
puede pasar de 11 ⚠️ a **0**: Bob con Pantone oficial, Don Cangrejo/Calamardo/
Patricio medidos en dos fuentes cada uno (hoja de grupo + stock art
individual), Plankton con hex exacto del SVG.

### Punto 16 · Fondos de pantalla

- [Wallhaven `dpgdp3`](https://wallhaven.cc/w/dpgdp3): 1920×1080, 1.06 MB,
  188 favoritos, subido por **káká311610** ✅ (tamaño y autor reales por la
  API, no de la página).
- [Wallhaven `w86qqp`](https://wallhaven.cc/w/w86qqp): 1920×1080, 638 KB, 59
  favoritos, subido por **felixal** ✅.
  (Ojo: en Wallhaven el «uploader» no siempre es el artista original; lo digo
  así en vez de dar un nombre de autor que no comprobé.)
- Las dos key arts del 25.º aniversario (§1) sirven también como fondo de
  pantalla alternativo, con fuente oficial confirmada (mejor que los fan
  wallpapers).
- El fondo pintado de «Wallpapers.com» que ya tenía la biblia sigue con
  autor y licencia desconocidos ⚠️ (repetí la búsqueda de la imagen en
  TinEye/Google Images de forma indirecta vía búsqueda de texto; no
  encontré el artista original — lo dejo igual).

### Punto 19 · Texturas 2D (sección nueva: no existía en la biblia)

SpongeBob es animación occidental plana (cel-shading), **no manga**: no hay
tramas de puntos (screentones). Lo que sí aplica — logos, patrones de ropa,
grano de fondo pintado y pinceladas — con equivalentes libres:

- **Logo del Crustáceo Cascarudo**: `Krusty_Krab_logo.jpg` (400×300,
  [Fandom](https://static.wikia.nocookie.net/spongebob/images/8/89/Krusty_Krab_logo.jpg/revision/latest?cb=20171102014937))
  ✅ visto: letras rojas gruesas de palo sobre fondo de concha.
- **Logo del Balde de Carnada**: `SpongeBob-Karen-Chum-Bucket-logo.jpg`
  (800×550, [Fandom](https://static.wikia.nocookie.net/spongebob/images/f/f1/SpongeBob-Karen-Chum-Bucket-logo.jpg/revision/latest?cb=20190803170616))
  ✅ visto.
- **Logo de la serie**: colores exactos del SVG en §1 (`#FFF463`, `#B2B618`,
  `#EF5240`, `#B26E2D`).
- **Patrón de ropa**: el short de Patricio — verde `#B2E638` con flores
  hibisco moradas `#9E71D1` (medido en §15) — es el patrón textil más
  reconocible de la serie.
- **«Phylum Porifera»** (hoja `personajes_01.jpg`, imagen 98 del lote,
  1525×1350): título con textura de **spray/grunge** verde lima sobre morado,
  el único ejemplo de textura de pincelada "sucia" que encontré en la wiki
  (el resto del show es vector limpio). Sirve de referencia de "pincelada"
  si se quiere ensuciar un fondo.
- **Grano de papel pintado (equivalente CC0)**: [ambientCG Paper001](https://ambientcg.com/view?id=Paper001)
  y Paper002-006, descarga 2K JPG libre (CC0) — ✅ (API comprobada, no
  bajé el zip completo por peso). Sirve para las **acuarelas de fondo**
  del show, que están pintadas a mano (no son fotos).
- **Pinceladas / línea de tinta (equivalente libre)**: [«FREE Comic Ink
  Set»](https://georgvw.gumroad.com/l/free_procreate_ink_brushes) (20+
  pinceles de entintado para Procreate, gratis) ⚠️ comprobar en la propia
  página si sigue gratis al momento de bajarlo (algunos packs del mismo
  autor son "paga lo que quieras"). No encontré un equivalente para
  Photoshop igual de directo; con "Convertir a pincel" desde Procreate o
  Krita (gratis) se puede pasar.
- **Emblemas y carteles del mundo**: la licencia de conducir de Patricio
  («Bikini Bottom Driver License», imagen 200 de `objetos_01.jpg`) y el
  cuadro «The Clam Calamity of 1912» (imagen 214) son las mejores texturas
  de "papel/documento del mundo" que hay en la wiki — sirven de referencia
  directa para el cuadro de diálogo de tipo "documento" del punto 6 (no es
  mi punto, lo anoto para el redactor).

### Punto 23 · Colaboraciones y cruces (sección nueva: no existía en la
biblia)

- **Fortnite** (Epic Games, 2024-2025) ✅✅: SpongeBob llegó primero como
  **Sidekick** (NPC acompañante, no jugable), con el pack «SpongeBob
  Slippies Kicks», «Gary Slippies Kicks» y los emotes «Jellyfish Jam» y
  «Lil' Big Jellyfish» (diciembre 2024, [NickALive](https://www.nickalive.net/2024/12/spongebob-brings-bikini-bottom-to.html)).
  En **Winterfest 2025** se añadieron los skins completos de **Calamardo,
  Patricio y Arenita**, y Don Cangrejo apareció en el pack; se vende también
  el **Patty Wagon** (coche de la película de 2004) como vehículo del
  Item Shop ([vpesports](https://vpesports.com/games/fortnite/fortnite-and-nickelodeon-collaboration-2025),
  [gamerant](https://gamerant.com/fortnite-spongebob-skins-cosmetics-prices/)).
- **Vans × SpongeBob** (febrero 2018) ✅✅: línea Vault by Vans de
  zapatillas (Old Skool, Slip-On, Sk8-Hi), ropa y tabla de skate, diseñada
  por el artista de Los Ángeles **Mike Gigliotti**
  ([Vans oficial](https://www.vans.com/vault-main/spongebob.html),
  [Empire Blog](https://thinkempire.com/blogs/news/vans-x-spongebob-by-mike-gigliotti),
  [Tillys](https://www.tillys.com/product/vans-x-spongebob-squarepants-sk8-hi-shoes/401260957.html)).
- **«The Krabby Patty Kollab»** (Nickelodeon + Paramount, 25.º aniversario,
  desde el 8 de octubre de 2024) ✅✅: varios restaurantes y chefs hicieron
  platos inspirados en la Cangreburger (dumplings, falafel, hamburguesas,
  donas, helado…). **Wendy's** sacó su propia «Krabby Patty Kollab Burger»
  (una hamburguesa con doble queso y salsa "secreta") y el «Pineapple Under
  the Sea Frosty», hasta noviembre de 2024
  ([PR Newswire](https://www.prnewswire.com/news-releases/nickelodeon-and-paramounts-spongebob-squarepants-25th-anniversary-celebration-serves-up-krabby-patty-inspired-dishes-with-the-krabby-patty-kollab-beginning-oct-8-302264923.html),
  [CNN](https://www.cnn.com/2024/10/02/food/wendys-spongebob-squarepants-meal/index.html),
  [Variety](https://variety.com/2024/tv/news/spongebob-squarepants-themed-burgers-wendys-restaurants-collaboration-1236162353/)).
  No fue un restaurante físico del Crustáceo, es un programa de menús — lo
  digo así para no exagerar (aviso del dueño: no inventar).
- **Nickelodeon All-Star Brawl / All-Star Brawl 2** (videojuego de pelea) ✅✅:
  Bob y Patricio desde el juego 1; en la secuela (2023-2024) se sumaron
  **Calamardo**, **Plankton** (con Karen integrada en su traje robótico) y
  **Don Cangrejo** (DLC de temporada, 2024)
  ([Nintendo Life](https://www.nintendolife.com/guides/nickelodeon-all-star-brawl-2-character-roster-every-new-and-returning-fighter),
  [wiki del juego](https://nickelodeon-allstar-brawl.fandom.com/wiki/SpongeBob_(NASB_2))).
  Ya había renders de este juego en la hoja `personajes_01.jpg` (imágenes 16
  y 32: Patricio y Calamardo de *All-Star Brawl 2*).
- **Figuras oficiales — Funko Pop** ✅: línea POP! Television/Animation con
  Bob, Arenita, Calamardo, Don Cangrejo, Patricio, Hombre Medusa y Chico
  Percebe; también línea POP! Movies para *Sponge on the Run* y *Search for
  SquarePants* ([Encyclopedia SpongeBobia](https://spongebob.fandom.com/wiki/SpongeBob_SquarePants_Funko_POP!_Vinyls),
  [Paramount Shop oficial](https://www.paramountshop.com/collections/spongebob-squarepants-funko-pop-figurines)).
  No encontré una línea propia de **McFarlane Toys** para esta serie
  (búsqueda hecha, sólo aparece listado junto a Funko en tiendas, no como
  fabricante propio) — lo dejo en «No encontré», no lo invento.
- **Cosplay**: busqué cosplay concreto con crédito (Reddit, «foam» y
  materiales) y sólo salieron tableros de Pinterest sin autor identificable
  ni datos de materiales — no hay un ejemplo con crédito que pueda dar como
  ✅. Queda en «No encontré» (es extra, no obligatorio: la serie tiene
  disfraces simples —camisa+corbata+pantalón, o triángulo rosa— más que
  cosplay elaborado con volumen).

---

## Lo mejor para la lámina

1. **La ficha Pantone oficial** (§15): coloca a Bob con sus colores de
   producción exactos, cero adivinanza.
2. **La hoja de modelo «Main Characters» 2200×2200** (§1): turnaround limpio
   de los 5 personajes del encargo en la misma imagen, ideal para pose base.
3. **La key art «25 con burbuja de flor»** (§1): pose de grupo mirando a
   cámara, con Don Cangrejo, Bob y compañía — sirve directo para un concepto
   de "todos presentando la oferta".
4. **El catálogo Yanez Designs en Sketchfab** (§3): objetos CC BY sueltos
   (Don Cangrejo, la Krabby Patty, el menú) listos para Blender sin tener
   que modelar desde cero.
5. **El menú/caja registradora medidos en §3.4 de la biblia + Yanez Designs**:
   la caja registradora del Crustáceo (objeto del canal) ya tiene referencia
   2D (textura de juego) y 3D (modelo libre).

## No encontré

- ⚠️ Cosplay con crédito y materiales reales (foam, volumen): sólo Pinterest
  sin autor. Búsquedas: «mejor cosplay Bob Esponja Patricio Calamardo
  materiales foam reddit» (español e inglés). Es un extra del punto 23, no
  lo obligatorio (las colaboraciones oficiales sí están completas).
- ⚠️ Línea de figuras McFarlane Toys propia de la serie: no existe una
  dedicada (Funko sí). Búsqueda: «SpongeBob Funko Pop McFarlane Toys
  official figures line».
- ⚠️ Autor original del fondo de pantalla de Wallpapers.com (flores):
  ninguna fuente lo da.
- ⚠️ Licencia exacta del modelo «The Krusty Krab!» de pizzabrian: no
  reapareció en la búsqueda por API de Sketchfab esta vez (puede haberse
  retirado o cambiado de nombre); no lo afirmo sin confirmarlo.

## Bitácora de búsqueda (segunda pasada)

- Fandom API (`spongebob.fandom.com/api.php`), en inglés: páginas de
  personajes con nombre correcto (`Eugene H. Krabs`, `Squidward Tentacles`,
  `Sheldon J. Plankton`), búsqueda de texto («Pantone», «model sheet»,
  «Krusty Krab logo», «Chum Bucket logo», «SpongeBob SquarePants logo svg»,
  «Plankton model sheet»), `fileusage` y `imageinfo` para tamaños reales.
- `investigar_serie.py --wiki spongebob` con 6 páginas en inglés → 5 hojas,
  214 imágenes grandes (antes: 0, fallo total).
- Sketchfab API (`/v3/search?type=models&q=…`) en inglés: «krusty krab cash
  register», «the krusty krab», «cash register generic», «spongebob» — para
  confirmar licencias reales, no las de la página web.
- Wallhaven API (`/api/v1/search`, `/api/v1/w/<id>`): `q=spongebob`,
  1920×1080 o más, orden por favoritos.
- ambientCG API: `q=paper`, `q=fabric pattern` (CC0).
- `estilo.py` sobre 7 imágenes oficiales descargadas (stock art de Don
  Cangrejo, Calamardo y Patricio; recortes de la hoja de modelo; las 2 key
  arts del 25.º aniversario) para hex medidos.
- Lectura directa del código de 2 SVG oficiales (Plankton, logo de la serie)
  para hex exactos.
- WebSearch (4 de mi cupo de ~50): «SpongeBob SquarePants Fortnite
  collaboration skin Krusty Krab», «SpongeBob 25th anniversary Krusty Krab
  pop-up restaurant real life 2024», «Nickelodeon All-Star Brawl 2 fighting
  game characters roster», «SpongeBob Funko Pop McFarlane Toys official
  figures line», «SpongeBob Vans Supreme collaboration», «mejor cosplay Bob
  Esponja materiales foam reddit», «free CC0 flat cel shading ink brush pack
  Photoshop Procreate cartoon».
- Páginas que antes daban 403/no cargaban y ahora sí: `awn.com`,
  `nickalive.net` (con `curl -A "Mozilla/5.0"`).

## Cumplimiento del encargo (sólo mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | 214 imágenes nuevas en hojas de contacto (antes 0); Main Model Pack visto y descrito (antes ⚠️); hoja de modelo oficial 2200×2200 medida; 2 key arts del 25.º aniversario vistas y descritas (antes ⚠️ "no pude abrir"); logo oficial con hex exactos del SVG |
| 3 · Fan art y 3D con licencia | ✅ | 11 modelos con licencia confirmada por la API de Sketchfab (5 nuevos: catálogo Yanez Designs + Pixel + Plankton + Sandy); 1 corregido (Mrlunettes: no comercial, no sólo "CC BY"); 1 sin reconfirmar, dicho con ⚠️ |
| 15 · Vestuario con hex medidos | ✅ | Bob con Pantone oficial de producción; Don Cangrejo, Calamardo y Patricio medidos en dos fuentes cada uno (hoja de grupo + stock art individual); Plankton con hex exacto del SVG. Los 11 ⚠️ de la biblia quedan resueltos |
| 16 · Fondos de pantalla | ✅ | 2 wallpapers de Wallhaven con tamaño y autor reales (API); 2 key arts oficiales como alternativa con fuente segura; el wallpaper sin autor sigue marcado ⚠️ porque no lo encontré, no lo invento |
| 19 · Texturas 2D | ✅ | Sección nueva completa: logos (Crustáceo, Balde de Carnada, serie) con hex; patrón de ropa de Patricio medido; grano de papel CC0 (ambientCG); pinceles de entintado libres; aviso de que no aplican tramas de manga (western/cel-shading) |
| 23 · Colaboraciones y cruces | ✅ | Sección nueva completa: Fortnite, Vans, Krabby Patty Kollab/Wendy's y Nickelodeon All-Star Brawl 2, todos con dos fuentes; figuras Funko confirmadas; cosplay con crédito y McFarlane Toys dichos como "no encontré" con la búsqueda hecha, no como "no existe" |

Parte terminada: los 6 puntos (1, 3, 15, 16, 19, 23) están cubiertos, sin
obligatorio pendiente. Extras para otra pasada si hay tiempo (no
obligatorios, en «No encontré» arriba): reconfirmar la licencia de «The
Krusty Krab!» de pizzabrian y buscar el autor original del wallpaper de
flores.
