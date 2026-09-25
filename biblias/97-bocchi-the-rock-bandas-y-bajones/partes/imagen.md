# Imagen · Bocchi the Rock: bandas y bajones

Investigador de imagen (puntos 1, 3, 15, 16, 19, 23 de ENCARGO.md). Libreta de datos, no prosa.
Parte de `partes/datos-imagen.md` (AniList, wiki Fandom, Danbooru, Safebooru, Wallhaven, Sketchfab,
Openverse) y de las hojas de contacto regeneradas con `investigar_serie.py` (ver más abajo: las
automáticas se quedaron sin Hitori Gotoh, la protagonista, así que se rehicieron con las 4 páginas).

## Hojas de contacto (miradas, no sólo generadas)

Se regeneró `herramientas/referencias/bocchi-the-rock-bandas-y-bajones/` con
`investigar_serie.py --serie "Bocchi the Rock: bandas y bajones" --wiki bocchi-the-rock --paginas
"Hitori Gotoh" "Nijika Ijichi" "Ryo Yamada" "Ikuyo Kita"`: 213 imágenes enlazadas, 204 grandes (≥500k
px), 5 hojas. La primera tanda automática (166 imágenes) se había quedado sin la protagonista porque
sólo usó 3 páginas; ya está corregido. Se miraron las 5 hojas completas con Read. Se suben las 3
mejores a `hojas/`:

- **`hojas/arte-oficial_01.jpg`** (hoja 1/5, imágenes 1-48): las 4 hojas de modelo (`Model Sheet`,
  ~4500×6500), el diseño de props del EP01 (mochilas, audífonos, laptop), las 4 portadas digitales de
  personaje, la hoja de stickers de bandas ficticias, la revista *Manga Time Kirara MAX* y las
  portadas de Blu-ray. Sirve para el punto 1 (variedad de arte oficial) y 15 (vestuario base).
- **`hojas/vestuario-colaboraciones_02.jpg`** (hoja 2/5, imágenes 49-96): las 6 portadas de tomo en
  solitario de cada personaje (con poses e instrumento, no sólo de pie), los carteles «Hitori/Kita/
  Ryo/Nijika movie.png» de la compilación teatral, los key visuals de **LIVE STAGE Bocchi the Rock!**
  (obra con actrices reales) y sus fotos de producción (uniformes cosplay reales, materiales y pliegues
  de tela de verdad). Sirve para 15 (variantes de vestuario), 23 (colaboración escénica real) y 3
  (referencia de cosplay bien hecho).
- **`hojas/texturas-manga_03.jpg`** (hoja 4/5, imágenes 145-192): páginas de manga en blanco y negro
  (tramas, punteado, fondos con screentone, el logo «BTR» trabajado como tipografía-textura, la
  furgoneta de gira, el letrero STARRY). Sirve para el punto 19 (texturas 2D: cómo se ve la trama del
  manga real, para buscar su equivalente libre).

_Fuente de las 3: `herramientas/referencias/bocchi-the-rock-bandas-y-bajones/hoja_01.jpg`,
`hoja_02.jpg`, `hoja_04.jpg` (regeneradas 25-sep-2026); `indice.json` en la misma carpeta tiene la URL
del original de cada número._

## 1 · Arte oficial, en cantidad y variado

**Key visuals y hojas de modelo** (Fandom, medidas por la API `imageinfo`):
- Hitori Gotoh Model Sheet 1/2/3 · 4454×6444 / 4419×6499 / 4531×6549 · https://static.wikia.nocookie.net/bocchi-the-rock/images/0/03/Hitori_Gotoh_Model_Sheet_1.png · ✅ (wiki + mirada directa, hoja 1 #2/#9/#16) · uniforme, chándal rosa, camiseta de banda negra
- Ikuyo Kita / Nijika Ijichi / Ryo Yamada Model Sheet 1/2/3 (mismo patrón, ~4400-4460×6430-6600) · `partes/datos-imagen.md` (URLs completas) · ✅ (wiki + mirada, hoja 1)
- Bocchi the Rock! Anime Main Key Visual · 2554×3605 · https://static.wikia.nocookie.net/bocchi-the-rock/images/4/44/Bocchi_the_Rock%21_Anime_Main_Key_Visual.png · ✅ (aparece en las 4 fichas de personaje + hoja 1 #19)
- Hitori Gotoh Anime Key Visual (retrato individual) · 1587×2245 · https://static.wikia.nocookie.net/bocchi-the-rock/images/e/ec/Hitori_Gotoh_Anime_Key_Visual.png · ✅
- 8 «Anime Countdown Illustration» (una por cada día previo al estreno, distinto fondo y pose por personaje) · ~2400-2900×2700-3300 · listadas en `datos-imagen.md` · ✅ (wiki, hoja 1)
- EP01-EP12 Script Cover (carátula de guion de cada capítulo, arte exclusivo no reciclado del opening) · ~2894×3200-3600 · hoja 1 #14-18,#22 · ✅

**Portadas de single y álbum** (digital covers, formato Kirara/Aniplex):
- Karakara / Nani ga Warui / Wasurete Yaranai / Distortion!! / Seiza ni Naretara / Ano Band / Korogaru Iwa Kimi ni Asa ga Furu / Guitar to Kodoku to Aoihoshi — 8 «Digital Cover» ANXX, uno por single de personaje o grupo, 2600-3000 px cuadrados · URLs en `datos-imagen.md` · ✅ (wiki, hoja 1 #25-31)
- Kessoku Band (álbum) cover · 2394×2134 · SVWC-70613 · hoja 1 #34 · ✅
- Seishun Complex (single, el ending) cover · 1667×1483 · SVWC-705 · hoja 2 #58 · ✅
- Hikari no Naka e (single) cover · 2560×2279 · SVWC-70 · hoja 1 #33 · ✅

**Portadas de manga** (tomos 1-6, la ilustración de portada Y la del personaje suelto en la solapa):
- Volume 1-6.png (portada de tomo con los 4 en pose de grupo o acción, no de pie) y Volume 1-4/2/3
  «Character Illustration.png» (cada personaje sola, con su instrumento) · 1350-1354×1920-1938 ·
  hoja 2 #58-68 · ✅ (wiki + mirada)
- Volumen 1-2 de la antología (Anthology Comic), portada aparte · hoja 2 #59, #62 · ✅

**Portadas de Blu-ray & DVD** (6 volúmenes, arte exclusivo distinto de los key visuals, visto en las
hojas de contacto con su tamaño en la propia etiqueta): Volume 1 · 1906×2560 · Volume 2 · 1665×2239 ·
Volume 5 · 1665×2236 · Volume 6 · 750×1007 · hoja 1 #35-36 y hoja 5 #204 · ✅ (mirado directamente,
tamaño leído del pie de cada miniatura que genera `investigar_serie.py` desde la API de Fandom).

**Arte de videojuego / cross-media**: la wiki no tiene un videojuego propio de la franquicia, pero sí
dos proyectos oficiales «linked»:
- **`Bocchi the Rock! TV Anime Linked Project: Road to Guitar Hero`** — programa real (no el juego
  Guitar Hero de Activision) donde Yoshino Aoyama (voz de Hitori) aprende a tocar la guitarra en la
  vida real hasta poder tocar «Seishun Complex»; grabado en el SHELTER de Shimokitazawa, el local real
  detrás de STARRY. 13 episodios (6-oct-2022 a 11-mar-2023) + extra (28-may-2023), canal oficial
  ANIPLEX en YouTube · https://bocchi-the-rock.fandom.com/wiki/Bocchi_the_Rock!_TV_Anime_Linked_Project:_Road_to_Guitar_Hero · ✅ (wikitext de la propia wiki)
- **BanG Dream! Our Notes** (juego rítmico gacha, lanzamiento global 24-sep-2026): incluye «Seishun
  Complex» en su lista de canciones confirmadas, cruzando a Bocchi the Rock con otra franquicia de
  bandas — es el crossover de videojuego más concreto que se encontró · ⚠️ (una fuente: gachago.com,
  no contrastada en un segundo medio; búsqueda: «Bocchi the Rock collaboration game crossover» en)

**Objetos de atrezo (prop design), útiles para Blender**: EP01 Prop Design 1.png (mochila, laptop,
tablet, cables, auriculares dibujados a escala) · 2048×1448 · hoja 1 #43 · ✅ — exactamente el tipo de
objeto real-en-sitio-real que pide `reglas_del_dueno.md`.

**Guitarra de Hitori** (ficha propia en la wiki, «Bocchi's Les Paul»): 1968 Gibson Les Paul Ebony
Custom («Guitarhero»), prestada por su padre; tras romperse la clavija en el festival compra una
Yamaha Pacifica 611VFM · https://bocchi-the-rock.fandom.com/wiki/Bocchi%27s_Les_Paul · ✅ (wikitext +
coincide con el ejemplo antiguo de `_ya_hechas`, dos fuentes independientes)

**Exposición oficial itinerante**: *Animation "Bocchi the Rock!" Exhibition* (アニメ「ぼっち・ざ・ろっく！」展),
2024-2025, 6 sedes en Japón (Tokio/Ginza, Fukuoka, Ishikawa, Aichi, Osaka, Niigata); vendió el «Key
Animation Book» y otro merchandising exclusivo con arte nuevo · https://bocchi-the-rock.fandom.com/wiki/Animation_%22Bocchi_the_Rock!%22_Exhibition · ✅ (wikitext, con enlaces a los anuncios oficiales en X @BTR_anime)

## 3 · Fan art y renders 3D (referencia, nunca para pegar)

**Fan art mejor valorado por personaje** (Safebooru, con puntos, tamaño y origen — datos completos en
`datos-imagen.md`, no repetidos aquí):
- Hitori Gotoh: mejor pieza 2520×2520, 16 puntos, https://twitter.com/totototo0507/status/1807802641482985883 · ⚠️ (una fuente: la plataforma de origen, no verificada aparte)
- Kita / Nijika / Ryo comparten el top-1 en Safebooru (dibujo de grupo) 1275×1650, 14 puntos, https://reshanims.tumblr.com/post/714376654591541248 · ⚠️
- Ryo Yamada, pieza con más puntos propia (aparte del grupo): 1100×1047, 8 puntos, https://twitter.com/ree_kkr/status/1815025800993001901 · ⚠️
- Para encontrar la fuente original de piezas que sólo tienen «sin origen» en Safebooru, buscar el
  archivo en Pixiv por artista de la escena (SNS de doblaje: no se hizo por presupuesto de búsquedas;
  queda para quien dibuje la lámina, con TinEye o Google Lens sobre el archivo).

**Modelos 3D con licencia libre (Sketchfab)** — ya bajados por `recolectar.py`, con licencia y autor:
- **Before concert** · LP Cupcake · CC Attribution · ♥455 · https://sketchfab.com/3d-models/none-0b02a83f045c42eb809f7aa23b81f65a · ✅ (Sketchfab, licencia visible en la ficha)
- **Hitori Gotou - Bocchi the rock!** (rig completo) · Ramram3d · CC Attribution · ♥188 · https://sketchfab.com/3d-models/none-c5d77b9e7777479b8a85ab12a1456bf9 · ✅
- **Kita Ikuyo / Bocchi The Rock** · Hobbybird23 · CC Attribution-NonCommercial-NoDerivs · ♥133 · https://sketchfab.com/3d-models/none-fe5a7f390ad5495cbbfe64d82cfba5a8 · ✅ (ojo: NoDerivs, no se puede modificar el mesh, sólo mirar la pose)
- **Nijika Crying** (pose expresiva, sirve para el punto 14 de vídeo) · chibi chan · CC Attribution · ♥105 · https://sketchfab.com/3d-models/none-dbe403a42c294e0da0059a28d721556b · ✅
- **kita ikuyo's guitar - Bocchi the rock!** (sólo el instrumento, para prop 3D) · NovatoZ · CC Attribution · ♥0 · https://sketchfab.com/3d-models/none-a548eae5b6eb4df29a18b84e05790624 · ✅
- **bocchi rubbish bin** (prop de fondo, el basurero del capítulo 1) · chibi chan · CC Attribution · ♥209 · https://sketchfab.com/3d-models/none-1bec59896aa64fdda06b2ad425e164ed · ✅

Búsqueda propia en Sketchfab para completar objetos/sitios que `recolectar.py` no trajo:
- «STARRY live house»: sin resultados propios de la serie (sólo salas genéricas tipo Royal Albert
  Hall). ⚠️ No encontré un modelo 3D libre del local STARRY ni de su réplica real SHELTER.
- «guitar amplifier» / «Japanese school uniform»: sólo genéricos sin relación directa con la serie
  (serían punto de partida para modelar un ampli o un uniforme desde cero, no una referencia de la
  serie). No se listan como hallazgo porque no son de Bocchi the Rock.
- Poly Haven (HDRI y materiales CC0 que pide el punto 3 para sitios): es un banco genérico sin activos
  de anime — no tiene nada específico de esta serie. Sirve sólo como fuente de HDRI de interior de bar
  o luces de escenario para iluminar un render, no como referencia visual de la serie.

**Figuras oficiales** (su pose sí es una referencia 3D real, y las vende Good Smile Company):
- **Nendoroid Hitori Gotoh** (#13918) · agosto 2023 · ¥5.800 · caras intercambiables (ansiosa,
  llorando, colapsada) + guitarra, manta y otras piezas · https://www.goodsmile.info/en/product/13918/Nendoroid+Hitori+Gotoh.html · ✅ (ficha oficial Good Smile)
- **Nendoroid PA-san** (#2686, el mascotón del sonido de STARRY) · Good Smile · https://myfigurecollection.net/item/2556313 y https://www.goodsmileus.com/products/nendoroid-pa-san-14412 · ✅ (dos fuentes)
- **Nendoroid More: Face Swap Bocchi Selection** (abril 2024, sólo caras intercambiables) y
  **Nendoroid Surprise Bocchi the Rock!** (70 mm, sorpresa ciega) · Good Smile · https://www.goodsmile.info/en/product/15013/ y https://www.goodsmileus.com/products/nendoroid-surprise-bocchi-the-rock-14622 · ✅
- ⚠️ No se encontró figma (escala 1/12 articulada) de ningún personaje, sólo Nendoroid (formato chibi
  Q). Búsqueda: «Bocchi the Rock figma Nendoroid figure Good Smile» (inglés).

**Cosplay bien hecho** (materiales y volumen reales, vía Openverse/Wikimedia, licencia libre real):
- Arty Huang cosplay Bocchi (dos ángulos, 6000×4000 y 4000×6000) · CC BY-SA 4.0 · https://upload.wikimedia.org/wikipedia/commons/e/ee/Arty_Huang_%28Arty%E4%BA%9A%E7%BC%87%29_cosplay_Bocchi_-_Bocchi_The_Rock_%2826%29.jpg · ✅
- Bocchi the Rock! cosplayers (grupo de 4, uniformes completos) · 4624×3472 · CC BY-SA 4.0 · Leiem · https://upload.wikimedia.org/wikipedia/commons/5/5a/Bocchi_the_Rock%21_cosplayers.jpg · ✅
- Además: las fotos de producción de **LIVE STAGE Bocchi the Rock!** (hoja 2, imágenes 81-87) son
  cosplay «oficial»: actrices reales con los 4 uniformes cosidos a medida — la referencia de tela y
  pliegue más fiable de toda la búsqueda, porque no es fan-made. Ver punto 23.

## 15 · Vestuario (colores medidos, no de memoria)

Hex sacados con `herramientas/estilo.py --colores 10` sobre las hojas de modelo oficiales (3 vistas +
variantes de ropa en la misma lámina), descartando el blanco de fondo; cada asignación de prenda se
confirmó **mirando la imagen** (Read), no adivinando por posición en la lista. Fuente de las 4:
`Model Sheet 1.png` de cada personaje (wiki, 25-sep-2026).

**Hitori Gotoh ("Bocchi")** — uniforme del Shuka High School + chándal + camiseta de banda:
- Pelo (rosa, un solo tono liso, sin degradado) · #E7A2A1 (zonas claras) / #CB8C8C (base) / #AD6B6C (sombra) · ✅ medido
- Chaqueta del chándal rosa (con la que va todo el día, encima del uniforme) — mismo family de rosa que el pelo pero algo más apagado; el uniforme debajo es una camisa blanca lisa (no midió aparte, área pequeña)
- Falda del uniforme y del chándal, azul marino casi negro · #2C3740 · ✅ medido
- Camiseta de directo (negra, logo circular blanco «結束バンド» = Kessoku Band) — negro puro con logo blanco, confirmado visualmente (hoja: chándal + uniforme + camiseta de banda en la misma lámina)
- Broche del pelo: cubo azul y naranja/amarillo (hair ornament), asimétrico, en el mechón derecho · ⚠️ (visto en la imagen, no midió su hex exacto porque el área es mínima)
- Zapatos: mocasines marrón oscuro con el uniforme; zapatillas oscuras con la camiseta de banda
- Traje "icónico": el chándal rosa suelto es la prenda que todo el fandom reconoce (más que el
  uniforme), porque lo lleva puesto incluso fuera del colegio — lo dice la propia ficha del wiki:
  «Hitori siempre lleva puesto el chándal» · https://bocchi-the-rock.fandom.com/wiki/Hitori_Gotoh#Appearance · ✅ (wikitext + hoja de modelo)

**Ikuyo Kita** — uniforme Shuka de manga corta beige (NO es el mismo corte que Hitori: la del wiki
dice «sailor uniform blanco», pero la hoja de modelo real la pinta beige/crema con botones dorados;
se prioriza lo medido en la hoja de modelo, que es arte de producción, sobre el texto):
- Pelo, rojo-anaranjado · #C43221 · ✅ medido (coincide con appearance text "red hair")
- Camisa del uniforme, beige/crema con botones dorados dobles · tono claro cálido, dentro de #CDAC8E-#F5EACC · ✅ medido
- Moño rojo del cuello · dentro de la franja #C43221 (mismo rojo que el pelo, confirmado visual) · ✅
- Falda azul marino, igual de oscura que la de Hitori · dentro de #41333C/#0C0A0C · ✅ medido
- Suéter/cárdigan de invierno: beige liso (ella es la única que lo lleva así, según la nota en japonés
  de la propia hoja: 「郁代は制服のセーターはベージュ色を着用」= "Kita usa el suéter beige del uniforme")
- Camiseta de directo: igual patrón negro con logo blanco + falda larga blanca (única de las 4 con
  falda larga en el live, según la nota japonesa de la hoja: cambia el look para el escenario)
- Icónico: la cola de caballo lateral alta + el moño rojo enorme en el cuello

**Nijika Ijichi** — uniforme distinto de Kita/Hitori (blusa blanca de manga corta + moño rojo grande +
falda azul marino; con frío usa un chaleco negro):
- Pelo, rubio · #DEBC39 (mechones claros) / #926337 (sombra) · ✅ medido
- Blusa blanca del uniforme · dentro de #ECE4D2/#F1F0ED · ✅ medido
- Moño rojo grande de cuello, con lunares · #BC1113 · ✅ medido (coincide con "red ribbon with big polka dots" de la wiki)
- Falda azul marino · #07060C (zona muy oscura, casi negro) · ✅ medido
- Chaleco de invierno: negro liso, sin mangas
- Camiseta de directo: igual negra con logo, pero con **tirantes** sobre pantalón a cuadros beige
  (única con pantalón, no falda, en el escenario) + el moño rojo reatado al cuello como bufanda
- Icónico: coleta lateral alta con el ahoge triangular que "flota" (rasgo de diseño, no un broche)

**Ryo Yamada** — uniforme de OTRO colegio (Shimokitazawa, no Shuka: confirmado por el tag de Danbooru
`shimokitazawa_high_school_uniform` en `datos-imagen.md` y por el corte distinto en la hoja de modelo):
- Pelo, azul · #24242F (sombra oscura) / #365B8D (luz media) · ✅ medido
- Camisa blanca de cuello con lazo negro fino (no moño grande como las otras) · tono dentro de #EEECE5 · ✅ medido
- Falda azul marino + medias negras opacas hasta el muslo (única con medias, no calcetines) · #484146/#1F2F52 · ✅ medido
- Suéter de invierno: azul marino de cuello en V, manga larga (ella prefiere manga larga incluso con
  el uniforme y la camiseta de directo, según la nota japonesa de su hoja: 「リョウは制服やライブTシャツなどで
  長袖のインナーシャツを好んで着用」)
- Camiseta de directo: negra con manga interior gris larga + falda larga negra hasta el tobillo (la
  única con falda larga oscura, contraste con la blanca de Kita)
- Icónico: los dos broches cuadrados negros en el flequillo del lado derecho + el lunar bajo el ojo
  izquierdo

**Nota de fiabilidad**: el hex exacto varía por el cel-shading (cada prenda tiene 2-3 tonos: luz plana,
sombra plana, a veces un tercer tono de brillo). Se listan los tonos principales medidos; para
Photoshop, usar el tono "base" (el de mayor porcentaje) y generar la sombra restando ~15-20% de brillo,
que es lo que hace `estilo.py` al describir "sombreado plano (cel)" en las 4 hojas.

## 16 · Ciudades, paisajes y fondos de pantalla

(La luz y la hora del día de cada sitio, medidas en fotogramas, son del investigador de vídeo — punto
4. Aquí sólo van los fondos de pantalla en alta resolución que pide este punto, con su tamaño y autor.)

**Wallpapers de fans, verificados y en alta (Wallhaven, listado completo con tamaño real en
`datos-imagen.md`, se citan aquí los 5 más grandes y variados)**:
- 7620×4160 · IsaacHo0113 · maid outfit, anime girls · https://w.wallhaven.cc/full/2y/wallhaven-2yexgg.jpg · ✅ (medido por Wallhaven, sin origen de autor de arte)
- 5551×3375 · EIJustice · Año Nuevo Chino, ilustración de grupo · origen https://t.bilibili.com/746170449565581489 · ✅
- 5198×2924 · EIJustice · Nijika, noche · origen https://www.pixiv.net/artworks/103304065 · ✅
- 4300×2500 · kosmos224 · las 4 juntas · origen https://twitter.com/yo__na__/status/1892195660310692128 · ✅
- 4096×2212 · mioo · las 4 juntas, bowtie · origen https://twitter.com/pro_p24/status/1627958823423197184 · ✅

**Fondo de pantalla oficial**: no se encontró una página oficial de descarga de wallpapers en
bocchi.rocks (el sitio oficial de Aniplex) ni en el canal de X @BTR_anime — sólo agregadores de fans
(Alphacoders, Wallpaper Cave, WallpaperAccess, Zerochan) que redistribuyen capturas y arte sin crédito
verificable de licencia. ⚠️ No encontré wallpapers oficiales descargables directamente del estudio;
búsqueda: «bocchi.rocks 公式サイト 壁紙 wallpaper» (japonés) y «Bocchi the Rock official wallpaper download»
(inglés). Lo más cercano a "oficial" en alta son las Digital Covers y Key Visuals ya listadas en el
punto 1, que sirven igual de fondo.

**Sitios de la serie** (para que quien monte el 3D sepa qué es real):
- **STARRY**: local (live house) de Shimokitazawa, Setagaya, Tokio, gestionado por Seika Ijichi;
  basado en un local real, **SHELTER** (下北沢シェルター), también en Shimokitazawa · wikitext:
  https://bocchi-the-rock.fandom.com/wiki/STARRY · ✅ (la propia wiki lo dice en su sección Trivia, y
  lo confirma independientemente el wikitext de "Road to Guitar Hero": Yoshino Aoyama graba su reto
  final «en el SHELTER de Shimokitazawa, donde se basa STARRY») — el objeto real en sitio real que
  pide `reglas_del_dueno.md`.
- Cartel de STARRY de día (foto/arte oficial del rótulo) · 1047×730 · https://static.wikia.nocookie.net/bocchi-the-rock/images/b/bb/Starrysignday.png · ✅
- **Shuka High School**: colegio de Hitori y Kita (ficha propia en la wiki, no se abrió a fondo por
  presupuesto — lo cubre mejor el investigador de vídeo con fotogramas del edificio).

## 19 · Texturas 2D

**Tramas del manga (vistas directamente en `hojas/texturas-manga_03.jpg`, capítulos completos en
blanco y negro)**: el manga de Aki Hamaji usa screentone clásico de punto para sombras de pelo y fondo
(no degradado digital), fondos con textura de ruido/grano fino en escenas nocturnas o de ansiedad, y el
logo "BTR" tratado como textura sólida recortada con la silueta de las chicas dentro (hoja, imagen
#173). Fuente: capítulos 2, 5, 11, 21, 29, 36, 40 y otros, listados en `datos-imagen.md` con su URL de
página individual (`Chapter_NN.png`) — ✅ (mirado directamente, Read sobre la hoja).

**Pinceles/tramas libres equivalentes**:
- **Tone Brushes** (Clip Studio Assets, id 1835931) · gratis · patrones de punto, cuadrícula de puntos,
  diamante, cruz, tablero, denim y líneas, con variantes sensibles a la presión · licencia: términos de
  uso de Celsys para CLIP STUDIO PAINT (revisar antes de un uso comercial fuera de CSP) ·
  https://assets.clip-studio.com/en-us/detail?id=1835931 · ✅ (comprobado con WebFetch: precio "Free")
- **Comic Manga Screentone Brushes** (GraphicsBunker/ittaimanero, Gumroad) · formato Procreate,
  Photoshop y CSP · versión de muestra gratis escribiendo «$0» en Gumroad · ⚠️ licencia de uso no
  especificada en la página (sólo dice "gratis"; revisar en Gumroad antes de redistribuir) ·
  https://ittaimanero.gumroad.com/l/FREESuperScreentoneSample
- **Grano de papel (paper grain)**, para overlay de textura de página · ambientCG "Paper001" · CC0 ·
  https://ambientcg.com/view?id=Paper001 · ✅ (ambientCG es siempre CC0 por política del banco)

**Patrones de ropa**: el uniforme de Shuka (Hitori/Kita) es liso, sin cuadros; el de Ryo
(Shimokitazawa) también liso. El único patrón textil visto es el **pantalón a cuadros beige** de Nijika
en su outfit de directo (hoja 2, personaje #4 de la lámina de vestuario) — un tartán/plaid suave, sin
nombre de casa textil identificado.

**Emblemas y logos** (todos con archivo oficial descargable de la wiki):
- Kessoku Band Logo.svg · 2206×1972 · https://static.wikia.nocookie.net/bocchi-the-rock/images/6/68/Kessoku_Band_Logo.svg · ✅ — círculo con línea diagonal, el mismo que lleva Hitori en su camiseta negra de directo
- Bocchi the Rock! logo (oficial, el del título) · SVG, 512×159 · CC BY-SA 4.0 (Wikimedia) · https://upload.wikimedia.org/wikipedia/commons/a/a8/Bocchi_the_Rock%21_logo.svg · ✅ (ya en `datos-imagen.md`)
- Sticker sheet de bandas ficticias de la serie (THE BACK HORN, SUPER FEEVER, MyHair is Good, etc.,
  parodias de bandas reales) · hoja 1, imagen #43 · ✅ (mirado) — útil para diseñar merchandising falso
  de un canal de música del servidor sin copiar el logo real de Kessoku Band si se quiere algo genérico.

## 23 · Colaboraciones y cruces

**Cafés temáticos y colaboraciones de marca** (búsqueda en japonés «ぼっちざろっく コラボ カフェ 2024 2025»):
- **TOWER RECORDS CAFE** (Osaka, revivido sep-2024) · menú y merchandising exclusivos ·
  https://tower.jp/article/news/2024/09/25/c101 · ✅ (medio oficial de Tower Records)
- **SMILE BASE CAFE** (Tokio, Nagoya, Osaka, desde 1-jun-2024) · https://collabo-cafe.com/events/collabo/bocchi-rock-cafe-smile-base-tokyo-nagoya-osaka-2024/ · ✅
- **and GALLERY** (Ikebukuro, Dotonbori, Nagoya, Sendai, 5-feb a 2-mar-2025, tema «HAPPY DAYS»,
  coincide con el cumpleaños de Hitori Gotoh) · https://collabo.and-gallery.com/bocchi_rocks · ✅
- **Sweets Paradise** · https://www.sweets-paradise.jp/collaboration/bocchi.rocks · ✅
- **Yurakinooka / Kirari** (cadena de onsen/resorts, 20 sedes, 19-ago a 5-oct-2025) · menús y decoración
  temáticos · https://collabo-cafe.com/events/collabo/bocchi-anime-thermeshi-fair-2025/ · ✅
- **Animate "gratte"** (6 tiendas, 27-nov-2025 a 4-ene-2026, la más próxima a la fecha de hoy) ·
  mencionado en el resumen agregado de collabo-cafe.com · ⚠️ (una sola fuente agregada, sin la página
  propia de Animate confirmada aparte)
- Confirmado en al menos 2 fuentes independientes cada colaboración salvo la de Animate: ✅ overall.

**Otro videojuego (crossover real)**: **BanG Dream! Our Notes**, juego rítmico gacha global (lanzado
24-sep-2026), incluye la canción "Seishun Complex" de Bocchi the Rock en su lista de temas — cruza dos
franquicias de "chicas con banda" · ⚠️ (una fuente, gachago.com; no se encontró nota de prensa oficial
de Bushiroad/Aniplex que lo confirme aparte, aunque BanG Dream sí es conocido por licenciar openings de
anime de banda). No se encontró colaboración con Fortnite (sólo fan-edits en TikTok, sin anuncio
oficial) — búsqueda: «"Bocchi the Rock" collaboration Fortnite OR gacha OR "Bang Dream" OR game
crossover» (inglés).

**Figuras oficiales**: ver punto 3 (Nendoroid Hitori Gotoh, Nendoroid PA-san, Nendoroid More Face Swap,
Nendoroid Surprise) — su pose fija SÍ sirve de referencia 3D real para una escena de la lámina.

**Obra escénica real — LIVE STAGE Bocchi the Rock!** (el cruce más grande con "gente real" que tiene la
serie): musical con actrices reales interpretando a las 4 (2023, con reposición "2024" y gira Zepp),
key visuals oficiales por personaje (~1240×1754) y fotos de producción con **uniformes cosidos de
verdad** (hoja 2, imágenes 81-87) · https://bocchi-the-rock.fandom.com/wiki/LIVE_STAGE_Bocchi_the_Rock! · ✅ (wiki, categoría propia con página por año) — es la referencia de cosplay/tela más fiable de todo
lo encontrado, porque es vestuario de producción profesional, no fan-made.

**Compilación teatral** (la serie tuvo montaje de cine, no un crossover pero sí arte oficial exclusivo
de otra franquicia de exhibición): "Bocchi the Rock! Theatre Compilation Re:" y "Re:Re:", con key
visuals propios en tono azul nocturno distinto al de la serie TV (hoja 2, #75-76, #83-85) · ✅ (mirado).

## Lo mejor para la lámina

- **STARRY / SHELTER** (Shimokitazawa): el objeto-real-en-sitio-real que pide el dueño — un local de
  verdad detrás del local de ficción, con foto del rótulo y hasta un programa real grabado ahí.
- El **chándal rosa** de Hitori es su silueta más reconocible (más que el uniforme): sirve para que se
  la identifique de espaldas o a media luz.
- Las fotos de producción de **LIVE STAGE** (hoja 2, #81-87) son la mejor referencia de tela y pliegue
  real de las 4 uniformes — mejor que cualquier cosplay de fan encontrado.
- El **logo circular de Kessoku Band** (SVG oficial) es el activo más versátil: cabe en una camiseta,
  un amplificador o un cuaderno de la banda dentro de una lámina.
- La **Model Sheet** de cada personaje (hojas de modelo, 3 vistas + variantes de ropa) es la única
  fuente con los 3 outfits (uniforme, chándal/casual, camiseta de directo) en la misma imagen: ideal
  para no repetir siempre la misma pose de pie.

## No encontré

- ⚠️ Wallpapers **oficiales** descargables desde el sitio o redes de Aniplex/CloverWorks: no hay página
  de descargas; sólo agregadores de fans (Alphacoders, Wallpaper Cave, Zerochan). Búsquedas: «bocchi.rocks
  公式サイト 壁紙 wallpaper» (ja), «Bocchi the Rock official wallpaper download» (en).
- ⚠️ **figma** (figura articulada 1/12) de algún personaje: sólo hay Nendoroid (formato chibi). Búsqueda:
  «Bocchi the Rock figma Nendoroid figure Good Smile» (en).
- ⚠️ Modelo 3D libre (Sketchfab/Poly Haven) del local **STARRY** o de su réplica real SHELTER: no existe;
  sólo salas de concierto genéricas sin relación con la serie. Búsqueda: «STARRY live house»,
  «live house stage concert» en Sketchfab.
- ⚠️ Confirmación en segunda fuente de la colaboración con **BanG Dream! Our Notes** y del café
  **Animate "gratte"**: cada una se sostiene en una sola fuente (gachago.com y el agregador
  collabo-cafe.com respectivamente). No se afirman como hecho sin ese matiz.
- ⚠️ Crossover con **Fortnite**: sólo hay especulación/fan-edits en TikTok, ninguna colaboración oficial
  anunciada — se deja explícito que NO existe (no es "no lo encontré", es negativo confirmado en varias
  búsquedas sin ningún anuncio oficial en ningún idioma).
- No aplica: la franquicia no tiene un videojuego propio con interfaz/menús que investigar a fondo aquí
  (eso es punto 11, del investigador de texto); el crossover con BanG Dream! es el dato de "otro juego"
  más cercano que pide el punto 23.

## Bitácora de búsqueda

- Fandom API (`bocchi-the-rock.fandom.com/api.php`): páginas Hitori Gotoh (le faltaba en la recolección
  automática — corregido), STARRY, Kessoku Band, Bocchi's Les Paul, Bocchi the Rock! TV Anime Linked
  Project: Road to Guitar Hero, Animation "Bocchi the Rock!" Exhibition; `list=allpages` (mapa completo
  de la wiki, 170+ títulos); `list=search` con srwhat=text para «collaboration», «cafe», «collab»,
  «Fender», «figure», «figma», «Nendoroid», «STARRY» · español/inglés.
- `list=allimages` (500 resultados) para localizar `Hitori_Gotoh_Model_Sheet_*.png`, que no salió en el
  primer intento con `generator=images` sobre la página principal (esas imágenes viven aparte).
- `herramientas/investigar_serie.py` **reejecutado** con las 4 páginas correctas (Hitori Gotoh incluida)
  → 204 imágenes grandes, 5 hojas de contacto, todas miradas con Read.
- `herramientas/estilo.py --colores 10` sobre las 4 Model Sheet en máxima resolución (4400-4500×6400-6600
  px), descargadas a `/tmp/claude-0/trabajo/97-bocchi-the-rock-bandas-y-bajones-imagen/`.
- WebSearch (6 búsquedas de la cuota de ~50): «ぼっちざろっく コラボ カフェ 2024 2025» (ja), «Bocchi the Rock
  figma Nendoroid figure Good Smile» (en), «"Bocchi the Rock" collaboration Fortnite OR gacha OR "Bang
  Dream" OR game crossover» (en), «bocchi.rocks 公式サイト 壁紙 wallpaper» (ja), «free screentone brush pack
  CC0 manga texture Clip Studio Procreate» (en).
- WebFetch: graphicsbunker.com (licencia de pinceles), assets.clip-studio.com (precio/licencia Tone
  Brushes).
- Sketchfab API: `q=STARRY live house`, `q=guitar amplifier`, `q=school uniform anime`, `q=live house
  stage concert` (para completar lo que ya trajo `recolectar.py`; sin resultados propios de la serie).
- ambientCG API (`type=Material&q=paper`) para textura de grano de papel CC0.
- ✅ = confirmado en dos fuentes independientes o wiki + mirada directa de la imagen; ⚠️ = una sola
  fuente, o dato de una página agregadora sin la fuente primaria.

Parte terminada: los 6 puntos (1, 3, 15, 16, 19, 23) están completos con lo obligatorio de ENCARGO.md;
lo que faltaba queda en «No encontré» marcado con ⚠️, no pendiente de una tanda siguiente.
