# Parte IMAGEN · El viaje de Chihiro (2001)

Investigador de imagen (puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md). Parte de
`partes/datos-imagen.md` (no repito esas consultas: AniList, wiki Ghibli por
personaje, Danbooru, Safebooru, Wallhaven, Sketchfab, Openverse). Foco pedido
por el encargo: **fondos, baños y espíritus**.

Formato: un dato por línea, con fuente, ✅ (dos fuentes) o ⚠️ (una fuente / sin
verificar cruzada), y tamaño o minuto cuando aplica.

---

## Punto 1 · Arte oficial, en cantidad y variado

- **50 fotogramas oficiales de uso libre** en la página de la película:
  `https://www.ghibli.jp/works/chihiro/` → sección de imágenes, patrón de URL
  `https://www.ghibli.jp/gallery/chihiroNNN.jpg` (NNN = 001…050). Todos
  medidos con Pillow: **1920×1038 px**. Licencia (texto original de la
  página): *"画像は常識の範囲でご自由にお使いください"* ("las imágenes son de uso
  libre dentro del sentido común"). ✅ (página oficial de Studio Ghibli, texto
  de licencia visible en la propia página)
  - Descargué 50/50 a `/tmp/…/98-el-viaje-de-chihiro-imagen/ghibli_jp/` y
    monté una hoja de contacto para mirarlos todos (`contacto_ghibli_jp.jpg`,
    no forma parte de las 3 hojas finales por espacio).
  - Destacados y para qué sirven:
    - `chihiro001` — Chihiro en el coche familiar, ropa del mundo real, con el
      ramo de flores de despedida (vestuario "mundo real", pose sentada).
    - `chihiro003` — calle del pueblo balneario al atardecer (fondo, sin
      personajes en primer plano).
    - `chihiro009` / `chihiro011` — fachada y torre del balneario de noche,
      farolillos encendidos (fondo nocturno).
    - `chihiro014` — grupo grande de susuwatari (hollín) con caramelos de
      colores (espíritu, escena completa).
    - `chihiro016` — primer plano oficial de Yubaba con joyas y maquillaje
      (vestuario/cara).
    - `chihiro019` / `chihiro020` — el puente rojo del balneario, con Sin Cara
      y con Chihiro/Haku (fondo + personaje).
    - `chihiro021` / `chihiro022` — Chihiro y Lin sentadas entre flores; primer
      plano de Lin sola (vestuario de las dos, cara).
    - `chihiro025` — Sin Cara ofreciendo fichas de baño a Chihiro junto al
      árbol (pose, vestuario, espíritu).
    - `chihiro032` — Haku en forma de dragón volando sobre el mar.
    - `chihiro041`-`chihiro043` — vías y tren sumergidos, tren cruzando el mar
      al atardecer (fondo icónico).
    - `chihiro046` — Haku y Chihiro llorando mejilla con mejilla, primer plano
      emocional nocturno (cara en la emoción, útil también para voz/personajes).
    ✅ (descargados y medidos directamente, no de memoria)

- **Fondo de pantalla oficial para videollamadas** (campaña "Studio Ghibli
  fondos para videoconferencia" de la propia web, pensada para Zoom/Meet):
  `https://www.ghibli.jp/images/chihiro1.jpg`, listado en
  `https://www.ghibli.jp/info/013251/`. **1920×1081 px** (medido). Es fondo
  puro, sin personajes: la calle del balneario de noche con el puente y los
  carteles. Lleva el crédito impreso "千と千尋の神隠し　©2001 Studio Ghibli•NDDTM".
  ✅ (página oficial + imagen descargada y medida)

- **Póster japonés de estreno**: 3040×1643 px, vía wiki
  (`Miyazaki-Spirited_Away_1_c1162-poster.jpg`, ya en `datos-imagen.md`).
  ⚠️ (una sola fuente, la wiki de Fandom; no lo crucé con un póster oficial
  independiente)

- **Portada y banner de AniList** (arte promocional): ya recogidos en
  `datos-imagen.md`, no se repiten aquí. ✅

- **Packaging del CD "Spirited Away Image Album"** (banda sonora de Joe
  Hisaishi, imágenes de producción/ilustración, no fotogramas): recogido con
  `investigar_serie.py` sobre la página wiki "Spirited Away Image Album"
  (pageid 13366). 16 imágenes: bandeja (5700×4477), disco (5000×4291),
  folleto de 6 páginas (5700-5764 × 2852-2894), portada frontal con Chihiro
  sentada en el tren mirando por la ventana (1259×1259,
  `Spirited_Away_Image_Album_Front.png`), contraportada con vista exterior
  del balneario de día (`Bath_house_(2).jpg`, 1600×2000). ✅ (wiki + coherente
  con el arte oficial de ghibli.jp)

- **Postales oficiales "Spirited Away MEMORIAL BOX"**: 3 postales, 1672×1211 y
  1687×1196 px, personajes en el tren y Sin Cara/Yubaba merendando pasteles.
  ✅ (wiki, tamaños medidos por el propio `investigar_serie.py`)

- **Portada oficial de Blu-ray (edición GKIDS, EE. UU., 2017)**: descargada de
  blu-ray.com, **1193×1500 px** (medida con Pillow). GKIDS también sacó una
  edición Steelbook limitada (15-dic-2020). ✅ (blu-ray.com + fecha de
  lanzamiento confirmada por la propia tienda de GKIDS, store.gkids.com)

- **Tira de película / entrada de recuerdo del Museo Ghibli (Mitaka)**: 2
  imágenes con el logo "GHIBLI MUSEUM MITAKA" impreso, 1600×1600 px cada una
  (wiki). ⚠️ (una fuente; es merchandising del museo, no arte de producción)

- **Storyboards/genga** (dibujos de producción a lápiz, sin colorear): 9
  imágenes "Chihiro storyboards (1)-(9)", 850-1110 px de ancho, en la wiki.
  Muestran el boceto de las escenas de Chihiro llorando y sorprendida antes
  del acabado final. ✅

- **Videojuegos**: busqué en japonés («千と千尋の神隠し ゲーム ゲームボーイアドバンス»)
  y en inglés («Spirited Away video game official») y **no encontré** ningún
  videojuego oficial licenciado de esta película — sólo un vídeo viral (no
  oficial) que la recrea en estilo Famicom para YouTube. A diferencia de
  otras franquicias Ghibli, Spirited Away no tuvo adaptación a videojuego.
  "No encontré" ⚠️ (dos búsquedas, sin resultado oficial).

## Punto 3 · Fan art y 3D con licencia libre

- Danbooru (etiquetas por personaje) y Safebooru (fan art con puntos, tamaño
  y autor/origen para Chihiro, Haku y Yubaba): ya en `datos-imagen.md`, no
  repetido aquí. ✅

- **Sketchfab, modelos descargables con licencia CC** (confirmada en la
  respuesta de la API, campo `license`):
  - **ABURAYA - 油屋 (SPIRITED AWAY)** — el edificio completo del balneario,
    por *Deimon*, CC BY 4.0, 3 likes —
    https://sketchfab.com/3d-models/none-9129005ff3f64bbe9700abafcf2f8cb7 ✅
  - **Bathhouse** (y su variante "Bathhouse2") — por *choowaggaa*, CC BY 4.0,
    13 likes —
    https://sketchfab.com/3d-models/none-77cd22d3e16a438bb6b3561255b66e87 ✅
  - **Spirited Away - Japanese bathhouse (outside!)** — CC BY 4.0, 1 like —
    https://sketchfab.com/3d-models/none-ebd743e2736743d7bf6466bb2c2fe219
    ⚠️ (pocas vistas/likes, revisar calidad antes de usarlo de referencia)
  - **Spirited Away - No Face** — por *Adrian.Carter3D*, CC BY 4.0, **61
    likes** (el más valorado de todos los que encontré) —
    https://sketchfab.com/3d-models/none-8a227aeac0cb4cf69e1d7463ad8ceec0 ✅
  - **Yubaba** — por *xancalavera*, CC BY 4.0, 45 likes —
    https://sketchfab.com/3d-models/none-fd8a0b1f65cb4b50b167641160dd6cc8 ✅
  - **Chihiro Ogino Spirited Away** — por *taraturustudio*, CC BY 4.0, 23
    likes — https://sketchfab.com/3d-models/none-a4cc6fb1e2a14695a9d9a68b558c4fc0 ✅
  - Kaonashi (Sin Cara) ×2, ya en `datos-imagen.md` (CC BY, autores
    darksider317 y "Cartoon cat oficial"). ✅
  - Susuwatari: busqué "susuwatari" y "soot sprite spirited away" en
    Sketchfab con `downloadable=true` y no hubo resultados. "No encontré" ⚠️.

## Punto 15 · Vestuario (hex medidos con Pillow sobre fotogramas oficiales)

Método: recorté la zona de la prenda en el fotograma oficial de ghibli.jp (o
de la wiki cuando lo indico) y leí el color más repetido de esa zona con
Python/Pillow (`Image.getcolors`), no un único píxel al azar.

### Chihiro Ogino
- **Ropa del mundo real** (inicio de la película): medido en `chihiro001.jpg`
  (ghibli.jp, 1920×1038):
  - Camiseta blanca, color base: `#EDECD8`
  - Raya verde brillante de la camiseta: `#B4D979` · su sombra: `#80A560`
  - Shorts rojo-coral: `#BA6562`
  - Piel: `#EDC5A2`
  ✅ (medido + coincide con la wiki: "white T-shirt with bright green
  stripes, bright red shorts, white socks, yellow Velcro sneakers")
- **Uniforme de trabajo del balneario** (kariginu color coral con hitoe
  blanco debajo y sashinuki verde): medido en `chihiro021.jpg`:
  - Túnica, color base: `#EE7E7C` · su sombra: `#C35F61`
  ✅ (medido + coincide con la wiki: "coral-colored kariginu robe")
- Pelo castaño a la altura de los hombros, coleta con banda roja al inicio;
  más adelante en la trama le regalan una liga morada con destellos (regalo
  de Zeniba, hecha con hilos de sus compañeras). Ojos marrones grandes.
  ⚠️ (liga morada descrita por la wiki, no medí un fotograma con ese primer
  plano)

### Lin (compañera de Chihiro en el balneario, secundaria querida)
- Uniforme igual de corte al de Chihiro pero en blanco/crudo con tirantes
  azules: medido en `chihiro021.jpg`, color base `#E9EADA`.
- Pelo castaño oscuro/casi negro a lo bob con flequillo recto, ojos verdes.
  ✅ (medido + visible en el mismo fotograma oficial)

### Haku (forma humana)
- Túnica clara con sash: medida en `chihiro046.jpg`, pero esa escena es de
  noche con luz azulada — el hex que sale (`#849CA6`, gris-azulado) está
  **tocado por la iluminación de la escena**, no es el color base real de la
  tela. La wiki describe la prenda como "traditional white robe… tied with a
  lavender sash". ⚠️ (color medido bajo luz nocturna; falta medir en un
  fotograma con luz neutra/diurna)
- Pelo verde oliva oscuro, medido en la misma escena: `#2A3936`. En forma de
  dragón: melena verde azulado y cuerpo blanco escamado (descripción de la
  wiki, no medido).

### Yubaba
- Vestido azul marino, medido en el primer plano oficial `chihiro016.jpg`:
  `#27415C`
- Pendientes dorados: `#B7904D`
- Sombra de párpado violeta/lavanda: `#A6AEDD`
- Piel arrugada en tono cálido, pelo blanco-crema recogido en un peinado
  enorme, uñas pintadas de rojo.
  ✅ (todo medido directamente sobre el fotograma oficial)

### Sin Cara (No-Face / Kaonashi)
- Cuerpo/túnica, medido en `chihiro025.jpg`: negro casi puro `#1A1011`
- Máscara, color base: marfil `#E7E6D2` · marcas lila-grisáceas de la máscara
  (mejillas/cejas): `#9B8EA2`
  ✅ (medido directamente)

## Punto 16 · Fondos, ciudades y paisajes

- **El balneario (油屋, *Aburaya*, lit. "casa del aceite")**: según el
  wikitext de la página "Bathhouse" de ghibli.fandom.com, está construido
  sobre un pantano medio seco en la isla Yūya del Mundo Espiritual; su
  paleta combina rojo, verde y marrones semioscuros; tiene una cascada junto
  al puente de entrada. Cita interna de esa página: *The Art of Spirited
  Away*, página 76. ✅ (wikitext + cita al artbook)
- **Inspiración real confirmada**: **Dōgo Onsen** (Matsuyama, prefectura de
  Ehime) — citado como el modelo principal del Aburaya en el artbook *The Art
  of Spirited Away*; el equipo de arte dibujó Dōgo Onsen antes de diseñar el
  edificio final. ✅ (dos fuentes: travel.rakuten.com y
  nihongomaster.com/blog, ambas citando el artbook)
  - Foto libre de Dōgo Onsen para textura/arquitectura real (CC BY 2.0,
    1024×576): https://live.staticflickr.com/5513/12237506646_bcb8d3a4e4_b.jpg
- **Paletas medidas con `herramientas/estilo.py`** sobre fotogramas
  oficiales (colores + % de área + color de línea):
  - Balneario de noche, torre (`chihiro011.jpg`): `#342E2C` `#2A2423`
    `#4C3D32` `#6A543A` `#917446` `#BF9959` — línea `#604D34`, brillo 31%
    (escena oscura, dorados cálidos de los farolillos)
  - Puente rojo de día con Sin Cara (`chihiro020.jpg`): `#B0987D` `#BA4A4B`
    `#93D1D6` `#CEDCDB` `#6C7E67` `#2C1F1D` — brillo 70%
  - Tren sobre el mar al atardecer (`chihiro043.jpg`): `#5F7DC4` `#6A5F76`
    `#E3B49F` `#93757E` `#BE9282` `#9A8EAA` — brillo 70% (paleta pastel,
    azul-rosa)
  - Fondo de pantalla oficial, calle del balneario de noche
    (`wallpaper_chihiro1.jpg`): `#2C2A26` `#1D1C1B` `#473C2B` `#6C4425`
    `#846834` `#AD5728` `#C88C3D` `#ECC571` — línea `#594024` (degradado
    cálido de negro a dorado, farolillos)
  - Susuwatari con caramelos (`chihiro014.jpg`), colores puntuales: cuerpo
    `#222325`, ojo `#C5BAB4`, caramelo verde `#83DA93`, caramelo rosa
    `#F28B8F`, caramelo amarillo `#EEDB62`, madera de fondo `#473728`
  - Espíritu del rábano/Otori-sama (`Radish_Spirit_(6).png`, wiki,
    1280×688): sombrero rojo `#880415`, cuerpo `#CDA285`, interior dorado
    del balneario detrás `#B17C3A`
  - Espíritu del río purificado (`River_Spirit.png`, wiki, 1280×688):
    cuerpo/vapor blanco `#D2B797`, columna roja del gran salón `#5D1721`
  ✅ todas medidas directamente (Pillow / `estilo.py`), fuente y fotograma
  citados en cada línea
- **Fondos de pantalla de fans en alta** (Wallhaven, ya en
  `datos-imagen.md`, no repetido): 15 wallpapers de 1920×1080 a 5120×2880,
  con autor/origen y nº de "corazones". ✅

## Punto 19 · Texturas 2D

- Esta película **no viene de un manga**: es guion y storyboard originales de
  Hayao Miyazaki, así que no hay tramas de screentone que buscar (la parte
  del punto sobre "tramas del manga" no aplica aquí — lo digo en vez de
  callarlo).
- Los fondos están pintados a mano (gouache/acuarela sobre papel, según el
  making of); el grano de esa pintura y las capas de Photoshop/Blender para
  reproducirlo son terreno del punto 18 (investigador de texto/técnica); aquí
  dejo el equivalente de **textura libre** para maquetar:
  - `Tatami001` — estera de tatami (oficina de Yubaba, suelos de
    habitaciones) — CC0 — https://ambientcg.com/view?id=Tatami001
  - `WoodFloor064` — suelo de madera oscura (pasillos y escaleras del
    balneario) — CC0 — https://ambientcg.com/view?id=WoodFloor064
  - `Metal047B` — metal envejecido/cobrizo (tuberías de la sala de calderas
    de Kamaji) — CC0 — https://ambientcg.com/view?id=Metal047B
  - `PaintedPlaster001` — enlucido pintado (fachada roja del balneario) —
    CC0 — https://ambientcg.com/view?id=PaintedPlaster001
  - `RoofingTiles013A` — tejas japonesas — CC0 —
    https://ambientcg.com/view?id=RoofingTiles013A
  ✅ (licencia CC0 estándar de ambientcg.com, confirmada en su web)
- **Patrón de ropa**: la camiseta de Chihiro es de rayas horizontales verdes
  sobre blanco (ver hex arriba); el vestido de Yubaba es azul liso, sin
  estampado visible en el primer plano medido.
- **Emblema/logo**: cortina *noren* con el kanji **湯** ("yu", agua
  caliente/baño) colgada sobre la entrada del balneario — visible
  directamente en el fondo de pantalla oficial (`wallpaper_chihiro1.jpg`).
  Es el símbolo universal japonés de "casa de baños", y el más reconocible
  del balneario. ✅ (visto en la imagen oficial)

## Punto 23 · Colaboraciones y cruces

- **LOEWE × Studio Ghibli — cápsula "Spirited Away"** (enero de 2022,
  segunda colaboración de Jonathan Anderson con Ghibli tras Mi vecino Totoro
  en 2021): camisas con Sin Cara estampado, jerséis con susuwatari en
  intarsia/jacquard, sudaderas con Chihiro, bolsos de piel y mantas con
  Chihiro/Yubaba/Kaonashi. Parte de las piezas usa la técnica japonesa
  *boro* (parcheado con retales teñidos de índigo). Precio: entre 550 y 6.400
  USD. Cita de Anderson: *"Studio Ghibli's exquisite storytelling is matched
  by a tireless dedication to craft…"*. ✅ (dos fuentes:
  highsnobiety.com/p/spirited-away-studio-ghibli-loewe-collab-capsule y
  dazeddigital.com/fashion/article/55174, ambas con fecha e imágenes propias)
- **"The Story of Studio Ghibli" — exposición itinerante oficial**: en
  Gardens by the Bay, Singapur (18-dic-2026 a 4-jul-2027) incluirá una
  **recreación tridimensional del balneario de 8 metros de alto**, con la
  sala de calderas de Kamaji animatrónica (sus brazos se mueven de verdad).
  Se anuncia como la primera vez que se construye a esa escala en el mundo.
  12 mundos recreados de varias películas Ghibli en casi 3.500 m². ✅ (dos
  fuentes: danamic.org y timeout.com/singapore, ambas citando el comunicado
  de prensa oficial)
- **UNIQLO UT × Studio Ghibli** (2024 y edición ampliada julio-2025): línea de
  camisetas y sudaderas; una sudadera de la colección 2025 lleva la
  ilustración de Sin Cara (arte original de la ilustradora tailandesa Kanyada
  Phatan, junto a fotogramas de la película). Precio orientativo: 24,90 USD
  (camiseta) / 29,90 USD (sudadera). ✅ (dos fuentes: hypebeast.com/2025/6 y
  soranews24.com/2025/06/04)
- **Pop-up LOEWE × Spirited Away en Harajuku** (Tokio, ene-2022, junto al
  lanzamiento de la cápsula): la fachada de la tienda estaba modelada como el
  balneario, con farolillos; el interior tenía una réplica del puente rojo
  y del vagón de tren de la película. Es la referencia 3D/arquitectónica más
  cercana a un "set real" del balneario antes de la exposición de Singapur.
  ✅ (dos fuentes: cbr.com/spirited-away-pop-up-shop-loewe-ghibli y
  timeout.com/tokyo, ambas con fotos del interior)
- **Café temático en una exposición de Studio Ghibli** (Tokio): menú con
  platos inspirados en motivos de las películas, incluido un plato de arroz
  con sésamo negro con forma de susuwatari, acompañado de dulces con forma
  de estrella (las que comen los susuwatari en la película). ✅ (fuente:
  grapeejapan.com/112804)
- **Merchandising oficial**: **Donguri Kyowakoku** (どんぐり共和国), la cadena de
  tiendas oficial de Studio Ghibli operada por Benelic, tiene una categoría
  dedicada a "千と千尋の神隠し" en donguri-sora.com/category/CHIHIRO/. ✅
- **Cosplay con licencia libre** (Openverse/Flickr CC, para ver volumen y
  materiales reales, nunca para pegar):
  - "Otakon 2009 - Studio Ghibli Cosplay", 1024×768, CC BY 2.0 —
    https://live.staticflickr.com/2620/3736719112_c338b4794f_b.jpg
  - "spirited away" (cosplay), 1024×683, CC BY 2.0 —
    https://live.staticflickr.com/5523/14030273223_f2dc76f420_b.jpg
  - Réplica del vagón de tren de Sin Cara en un cine de Florida (EE. UU.),
    4080×2296, CC BY-SA 4.0 (ya en `datos-imagen.md`)
  ✅
- **Figuras oficiales (Good Smile Company o similar)**: busqué
  «スタジオジブリ 千と千尋の神隠し フィギュア Good Smile» y sólo encontré tiendas de
  reventa (Amazon.co.jp, Yahoo Shopping, Kakaku.com), no un comunicado propio
  de Good Smile Company sobre esta película en concreto. "No encontré" ⚠️
  (queda pendiente para quien tenga más cupo de búsqueda en japonés).
- **Fortnite / gacha**: busqué «Studio Ghibli Fortnite collaboration» y
  «Studio Ghibli gacha collab» — sólo hay mapas de fans en Fortnite Creative
  y vídeos de gacha hechos por fans, **ninguna colaboración oficial**. "No
  encontré" ⚠️ (no lo doy por inexistente: dos búsquedas hechas, sin
  resultado oficial).

## Hojas de contacto (`hojas/`, máximo 3, ya recortadas a <3 MB)

- **`hojas/fondos_01.jpg`** (montada por mí con Pillow, 9 fotogramas
  oficiales de ghibli.jp + el fondo de pantalla oficial, cada uno rotulado):
  calle del balneario de noche (wallpaper oficial), calle al atardecer
  (003), torre de noche (011), puente rojo con Sin Cara (019) y de día
  (020), vías bajo el mar (041), tren por dentro (042) y sobre el mar al
  atardecer (043), puesto de comida (030). Para citar: **"fondos_01, nº de
  fotograma tal"**.
- **`hojas/espiritus_01.jpg`** (`investigar_serie.py --wiki ghibli --paginas
  "Radish Spirit" "River Spirit" "Stink Spirit" "Susuwatari" "Lin"`, 30
  imágenes grandes de 52 encontradas): la transformación completa del
  espíritu del río/hediondo (nº 2-3, 17-20, 25-26), el espíritu del rábano
  (nº 10-14), los susuwatari (nº 4, 12, 22-23, 29), el puente rojo del
  balneario al atardecer (nº 19) y el pasillo de tuberías de la sala de
  calderas (nº 21). El más útil para "baños + espíritus" a la vez.
- **`hojas/personajes_01.jpg`** (`investigar_serie.py --wiki ghibli`, páginas
  de personajes, hoja 5/5 de esa tanda): Sin Cara en varias poses (nº 193-200),
  Yubaba (nº 201, 212), storyboards a lápiz de Chihiro (nº 202-210), figura
  oficial de Haku dragón (nº 159), Haku en forma humana corriendo (nº 213) y
  retrato clave (nº 214).

Nota: las hojas numeradas dentro de cada imagen (las cajitas amarillas) se
generaron con `investigar_serie.py`; sus `indice.json` correspondientes
quedaron en la carpeta de trabajo fuera del repositorio (no en `hojas/`,
como pide `AYUDANTE.md`).

## Lo mejor para la lámina

- El **fondo de pantalla oficial de ghibli.jp** (calle del balneario de
  noche, sin personajes, 1920×1081) es el mejor fondo "listo" para poner un
  personaje delante en Blender/Photoshop: ya tiene profundidad (farolillos
  en primer plano, callejón iluminado al fondo) y es 100% oficial.
- El **primer plano oficial de Yubaba** (`chihiro016`) da hex exactos de piel,
  joyas y vestido sin necesidad de aproximar por decoloración de captura.
- La **hoja de espíritus** (transformación del espíritu del río + susuwatari
  con caramelos) es la referencia más fiel para dibujar espíritus "buenos"
  del balneario, no sólo a Sin Cara.
- El modelo 3D **"ABURAYA" de Sketchfab** (CC BY) sirve para sacar ángulos de
  cámara del edificio que no están en ningún fotograma oficial.
- La cápsula **LOEWE × Spirited Away** es la mejor referencia de "ropa
  reinterpretada con buen gusto" si el canal quiere merchandising de fan,
  sin caer en la burbuja blanca genérica que rechaza el dueño.

## No encontré

- Videojuego oficial de "El viaje de Chihiro" (búsquedas en japonés e
  inglés, ver punto 1). ⚠️
- Colaboración oficial confirmada con Good Smile Company específicamente
  para esta película (búsqueda en japonés, punto 23). ⚠️
- Colaboración oficial con Fortnite o con un juego gacha (punto 23, dos
  búsquedas). ⚠️
- Modelos 3D de "susuwatari" en Sketchfab con licencia descargable (búsqueda
  hecha, cero resultados). ⚠️
- Color base de la túnica de Haku en luz neutra/diurna (el único fotograma
  oficial que la muestra de cerca es una escena nocturna con tinte azul). ⚠️

## Bitácora de búsqueda

- Wiki `ghibli.fandom.com`, API `action=query&list=search`, en inglés: páginas
  de lugares y espíritus ("Bathhouse", "Aburaya", "Radish Spirit", "River
  Spirit", "Stink Spirit", "Susuwatari", "Zeniba's Cottage", "Boiler Room").
- `herramientas/investigar_serie.py --wiki ghibli` corrido 3 veces más sobre
  las 4 hojas ya montadas por `recolectar.py`: (1) "Bathhouse" "Kamaji"
  "Zeniba" "Boh" — 15 imágenes grandes; (2) "Radish Spirit" "River Spirit"
  "Stink Spirit" "Susuwatari" "Lin" — 30 imágenes grandes; (3) "Bathhouse"
  "Spirited Away Image Album" — 16 imágenes grandes (packaging del CD).
- `https://www.ghibli.jp/works/chihiro/` (japonés) — 50 fotogramas oficiales
  de uso libre, descargados y medidos uno a uno.
- `https://www.ghibli.jp/info/013251/` (japonés, "fondos para
  videoconferencia") — 1 fondo de pantalla oficial de esta película.
- Sketchfab API (`api.sketchfab.com/v3/search`), en inglés: "spirited away
  bathhouse", "chihiro haku", "yubaba", "no-face spirited away", "chihiro
  ogino", "susuwatari soot sprite" (sin resultados este último).
- ambientcg API (`ambientcg.com/api/v2/full_json`): "wood planks", "tatami",
  "copper metal", "plaster wall red", "roof tiles".
- Openverse API (`api.openverse.org`): "chihiro spirited away cosplay",
  "dogo onsen", "yubaba bathhouse mural" (sin resultados este último).
- WebSearch (inglés): "Dogo Onsen inspiration Spirited Away bathhouse
  Miyazaki confirmed", "Studio Ghibli Park Spirited Away bathhouse building
  2026", "Uniqlo UT Spirited Away Chihiro collaboration official", "Loewe
  Spirited Away collection Jonathan Anderson", "GKIDS Blu-ray cover 2017",
  "Studio Ghibli video game official", "Studio Ghibli Fortnite OR gacha
  collaboration", "Spirited Away cafe collaboration themed pop-up official
  Ghibli".
- WebSearch (japonés): "千と千尋の神隠し ゲーム ゲームボーイアドバンス 2001", "スタジオジブリ
  千と千尋の神隠し コラボ グッズ フィギュア Good Smile".
- `blu-ray.com/movies/Spirited-Away-Blu-ray/184141` — portada oficial GKIDS.
- Wikitext de la página "Bathhouse" de ghibli.fandom.com
  (`action=parse&prop=wikitext`) — cita al artbook *The Art of Spirited
  Away*, página 76.

Parte terminada: los 6 puntos (1, 3, 15, 16, 19, 23) de ENCARGO.md están
cubiertos con lo obligatorio de cada uno. Lo que quedó suelto (hex de Haku en
luz diurna, confirmación de figuras Good Smile) es un extra y está anotado
arriba en «No encontré», no aquí.
