# Parte · Investigador de IMAGEN · Spider-Man: Into/Across the Spider-Verse

Puntos de ENCARGO.md: **1** (arte oficial), **3** (fan art y 3D con licencia), **15**
(vestuario con hex), **16** (fondos de pantalla), **19** (texturas 2D), **23**
(colaboraciones y cruces). Parte del repaso: `biblia.md` ya existía (red cerrada,
0 hojas, muchos ⚠️). Este archivo **añade y corrige**, no repite lo que
`partes/datos-imagen.md` ya trae confirmado (pósters de personaje, libros de
arte, modelos Sketchfab base, fan art 2D, texturas CC0).

Nombro las películas como la biblia: **UNU** = *Un nuevo universo* (2018),
**ATSV** = *A través del Spider-Verso* (2023).

---

## Corrección previa: la página de Fandom de «Peter B»

El recolector no la encontró porque **no existe con ese nombre**. En la wiki
`spiderverse.fandom.com`, «Peter B. Parker» es una **redirección** a
**`Peter Parker (Earth-616)`** (comprobado con
`action=query&titles=Peter%20B.%20Parker&redirects` → `"to": "Peter Parker (Earth-616)"`,
y con el wikitext de esa página, que empieza `{{DISPLAYTITLE:Peter B. Parker}}`
y cita *Spider-Man: Into the Spider-Verse* en el alias). ✅ (la API + el
wikitext de la propia página). Con el nombre correcto corrí
`investigar_serie.py --paginas "Peter Parker (Earth-616)"`: **63 imágenes
enlazadas, 53 grandes → 2 hojas** en
`herramientas/referencias/spider-man-into-across-the-spider-verse-peter-b/`.

---

## 1 · Arte oficial, en cantidad y variado

- **Hojas de contacto: ya existen y las miré** (antes 0). 7 hojas de Miles,
  Gwen, Miguel y Hobie (360 imágenes enlazadas, 323 grandes,
  `herramientas/referencias/spider-man-into-across-the-spider-verse/`) + 2
  hojas propias de Peter B (63 imágenes, 53 grandes, ver arriba). ✅ (herramienta
  + inspección visual con Read, hoja por hoja).
- **Arte de producción real encontrado dentro de las hojas** (hospedado en la
  wiki, con nombre de autor y fecha, no fan art):
  - **Kris Anka**, turnaround de traje de Gwen, «WAM / CHARACTER DESIGN / GWEN
    / v101 / KRIS ANKA / 09/15/2020», 3 variantes de máscara y logo (a, b, c) ·
    [imagen](https://static.wikia.nocookie.net/intothespiderverse/images/5/57/SpiderGwen_ATSV_Concept_Art_by_Kristafer_Anka_2.jpg)
    2048×1326 ✅ (wiki + coincide con el crédito ya confirmado por la biblia en
    `krisanka.com/work/atvs`, dos fuentes).
  - **Jesús Alonso Iglesias**, arte de desarrollo de la **ropa de calle** de
    Gwen: 8 variantes (E-P) con looks muy distintos (top rojo con «PUNK»,
    impermeable turquesa con «ROCK'N'ROLL» en la espalda, blusa rosa, top
    mostaza con espiral verde) · [imagen](https://static.wikia.nocookie.net/intothespiderverse/images/2/2c/GwenOutfitsJes%C3%BAsAlonsoIglesias.jpg)
    2048×1018 ✅ (wiki, un solo crédito de autor).
  - **Evening Monteiro**, moodboard de referencia real **«Black Punks»**
    (fotos de la escena punk negra de Londres/NY: peinados, chaquetas de
    cuero, tachuelas) usado por el equipo de arte para Hobie ·
    [imagen](https://static.wikia.nocookie.net/intothespiderverse/images/c/ca/Spider_Punk_ATSV_moodboard_by_Evening_Monteiro.jpg)
    4096×1935 ✅ (wiki; confirma y da fuente visual a lo que la biblia ya
    decía en 5.1 sobre carteles y punk real, antes sin imagen).
  - **Jake Panian**, 11 estudios de la **chaqueta, parches y guitarra/bajo**
    de Hobie, incluida la vista de espalda con el diseño completo de parches ·
    [imagen](https://static.wikia.nocookie.net/intothespiderverse/images/8/8a/Spider_Punk_ATSV_by_Jake_Panian_3.jpg)
    1440×1440 ✅.
  - **Lena Sayaphoum**, turnaround de personaje de Hobie (3 imágenes) ·
    [ejemplo](https://static.wikia.nocookie.net/intothespiderverse/images/7/75/Gwen_Stacy_%28Earth-65%29_AtSV_character_design_7_by_Lena_Sayaphoum.jpg)
    1600×1135 ⚠️ (un crédito).
- **Peter B. Parker, arte y escenas oficiales** (antes 0 en la biblia): hoja
  con 53 imágenes grandes, incluida su ficha `Peterbparkeratsv.jpg`
  (3840×1600), el póster «Spider-Man Prime» y varias escenas familiares clave
  (el anillo, el beso con MJ, «Peter B meets May Parker», «Peter returns
  home», «Olivia Octavius vs Peter B. Parker», «Dead of Ben Parker») que
  sirven de referencia de **pose y vestuario casual** (bata, ropa de calle
  desaliñada) además del traje. ✅ (hoja propia, mirada con Read).

## 3 · Fan art y 3D (sólo como referencia)

- **Corrijo 2 licencias que la biblia dejó en ⚠️** (comprobadas ahora con la
  API de Sketchfab, `GET /v3/search?type=models&q=…`):
  - «Graffiti on a wall — Low Poly», **leoskateman** → **CC Attribution** ✅
    (antes ⚠️ «licencia no vista»).
  - «Street Graffiti», **Yanez-Designs** → **CC Attribution** ✅ (antes ⚠️).
  - «3D, low poly, Graffiti Spray Paint Can Prop», **ScottPritchard**: la API
    devuelve el campo `license` **vacío** (no es CC) → sigue ⚠️, **no usar**
    para nada salvo mirar la pose/forma.
- El resto de licencias de la tabla de `datos-imagen.md` (modelos de Miles,
  Gwen, Spider-Punk, Miguel por CVRxEarth, Kabiidev, etc.) ya venían con
  **CC Attribution** confirmado por el propio buscador de Sketchfab: ✅.

## 15 · Vestuario, con hex **medidos** (no de memoria)

La biblia tenía esta sección marcada con ⚠️ («no pude muestrear fotogramas»,
hex de memoria o de paletas de fans). Medí con `herramientas/estilo.py` y con
Pillow directo sobre **arte oficial plano** (no fotogramas con luz dramática,
que dan colores falseados):

- **Traje de Gwen** (sobre el turnaround de Kris Anka, WAM/v101, fondo
  blanco): negro del body **#2D2926** (no es negro puro, tira a marrón muy
  oscuro), rosa magenta de la capucha y la telaraña de los brazos **#E6145A**
  (clúster de muestreo `#DC145A`-`#E6145A`), cian de las zapatillas
  **#00FAFA**. ✅ medido, fuente oficial con fecha y autor.
- **Traje de Miguel O'Hara / Spider-Man 2099**: azul marino del cuerpo
  **#304080**, rojo de máscara y guantes **#E80038** — medidos sobre el
  fotograma-homenaje al Spider-Man de 1967 («Spider-Men (E-67) 001.png»,
  1920×804,
  [wiki](https://static.wikia.nocookie.net/intothespiderverse/images/e/ed/Spider-Men_%28E-67%29_001.png)),
  una escena con colores planos tipo cel clásico, no iluminación de neón. ✅.
  Sustituye los `#1B2A5C` / `#FF2B2B` «de memoria» que traía la biblia.
- **Símbolo de araña rojo clásico** (Peter B / Spider-Man estándar): **#BF0001**
  medido con `estilo.py` sobre el asset oficial
  [`Spider-Man symbol red.webp`](https://static.wikia.nocookie.net/intothespiderverse/images/5/52/Spider-Man_symbol_red.webp)
  (1000×962, 69.9% del área). ✅. Sustituye el `#D7262E` «de memoria».
- **Ropa de calle de Gwen** (Jesús Alonso Iglesias, 8 variantes): confirma que
  **no hay un solo «look icónico» de civil**, cambia de arco a arco — dato
  útil para el punto 15 de ENCARGO.md («sus trajes por temporada»). ✅ (una
  fuente, arte de producción).
- **Chaqueta de Hobie**: negra con tachuelas metálicas, **parches pintados a
  mano** con letras recortadas estilo fanzine (no parches comprados), visible
  en el estudio de espalda de Jake Panian. Pelo: mohawk con **imperdibles**
  visibles en el mismo estudio y en el moodboard de Evening Monteiro. ✅ (dos
  fuentes de arte de producción, más el moodboard real que las inspira).
- **Sigue en ⚠️** (no medí, no encontré arte oficial plano sin iluminación
  dramática): el rojo/azul exacto del traje de Hobie y de Miles (los
  fotogramas disponibles están todos de noche o con luz de color encima); la
  biblia puede mantener sus valores «de memoria» marcados como tal hasta que
  alguien mida un fotograma de día.

## 16 · Ciudades, paisajes y fondos de pantalla

`datos-imagen.md` ya trae 3 fondos de Wallhaven con tamaño real medido por su
propia API. Añado más, uno por mundo, con la misma API
(`api.sketchfab.com` no, `wallhaven.cc/api/v1/search`, tamaño y favoritos
reales, sin descargar nada pesado):

- **Tierra-928 (Miguel, 2099)**: 3840×2160, ♥207,
  https://w.wallhaven.cc/full/2y/wallhaven-2yod8m.jpg ✅ · también 7680×4800,
  ♥82, https://w.wallhaven.cc/full/vp/wallhaven-vpyd75.jpg ✅ (tamaños medidos
  por la API de Wallhaven).
- **Tierra-138 (Hobie, Spider-Punk)**: 7200×4050, ♥234,
  https://w.wallhaven.cc/full/2y/wallhaven-2y9vlm.jpg ✅.
- **Tierra-65 (Gwen)**: 5000×2250, ♥464,
  https://w.wallhaven.cc/full/96/wallhaven-96z8vd.jpg ✅ · también 7680×4320,
  ♥436, https://w.wallhaven.cc/full/x6/wallhaven-x6jo5o.jpg ✅.
- Todos «sólo aptos» (`purity=100`), verificado en la misma consulta que
  `datos-imagen.md` usó.

## 19 · Texturas 2D (tramas, grano, pinceladas, patrones, emblemas)

Esta sección **no existía** como tal en la biblia (sólo tenía, en 4.4, los
shaders de GitHub para el punteado Ben-Day/aberración, que es lo más cercano
a «trama impresa» y ya sirve). Lo que añado:

- **Pincel de halftone/Ben-Day con licencia clara**: RetroSupply, «Free
  Halftone Brush Kit», licencia explícita **«Free for Commercial Use»**
  ([RetroSupply](https://www.retrosupply.co/), listado en
  [Speckyboy](https://speckyboy.com/halftone-photoshop-brushes/)) ✅. Aviso:
  los packs sueltos de Brusheezy que aparecen en la misma búsqueda traen
  licencias **mezcladas por archivo** (no asumir CC0 sin comprobar cada uno)
  ⚠️.
- **Patrón de telaraña de Gwen**: rejilla diagonal rosa/cian sobre los brazos
  y la capucha, visible en el turnaround de Kris Anka (arriba) — no es una
  telaraña estándar de Spider-Man, es un **patrón geométrico propio**, con
  dos variantes de logo (araña redondeada clásica / araña angulosa
  «Spider-Woman») dibujadas en el mismo documento. ✅.
- **Parches de la chaqueta de Hobie**: no son texturas de tela compradas,
  son **ilustraciones pintadas a mano** con letras recortadas (estética de
  fanzine punk, collage y fotocopia), coherente con el «fanzine, fotocopia,
  collage» que la biblia ya describía en 5.1 para Tierra-138, ahora con
  imagen de referencia real (Jake Panian) en vez de sólo texto. ✅.
- **Emblemas**: el símbolo de araña **cambia de silueta por personaje** (no
  es el mismo logo reescalado): redondeado clásico en Peter B (#BF0001
  medido arriba), anguloso en las dos variantes de Gwen (turnaround Kris
  Anka), y el propio moodboard de Hobie usa **parches y flyers reales** como
  «logo» en vez de un símbolo de araña fijo. ✅.

## 23 · Colaboraciones y cruces

**No existía** esta sección en la biblia. Todo nuevo, con fuente oficial:

- **Fortnite** (mayo 2023, para promocionar ATSV): trajes de **Miles Morales**
  y **Spider-Man 2099** en la tienda de objetos (por separado o en lote, con
  la mochila «Spider-Verse Portal»); **Spider-Gwen** ya jugable; lanzadores de
  telaraña especiales «Spider-Verse Web-Shooters»; pista de lobby «Silk &
  Cologne (EI8HT version)». ✅ (dos fuentes:
  [CGMagazine](https://www.cgmagonline.com/news/fortnite-across-the-spider-verse-skins/),
  [GameSpot](https://www.gamespot.com/articles/fortnite-miles-morales-and-spider-man-2099-skins-debut-alongside-spider-verse-quests/1100-6514447/)).
  La skin de Gwen (`GwenStacyFortnite.png`, 1024×1024) está en la hoja
  `colaboraciones_01.jpg`, casilla 49 ✅ (wiki, coincide con las fuentes
  anteriores).
- **LEGO** (2023): set **71050** de minifiguras sorpresa (12 personajes:
  Miles, Miguel, Gwen, Hobie, Pavitr…) y set **76311** «Miles Morales vs. The
  Spot» (Miles, The Spot, Gwen, el oficial Jefferson, accesorios de
  telaraña). ✅ ([LEGO oficial](https://www.lego.com/en-us/product/spider-verse-miles-morales-vs-the-spot-76311),
  [Brickset](https://brickset.com/sets/subtheme-Spider-Man-Across-the-Spider-Verse-Series)).
- **Hot Toys / Sideshow**: figura a escala 1/6 **«Miles G. Morales»**
  (MMS725, ≈285 USD), cabeza con ojos intercambiables, accesorios de diorama
  (cómic, efectos de telaraña, fondo del multiverso). ✅ ([Sideshow](https://www.sideshow.com/collectibles/marvel-miles-g-morales-hot-toys-912767),
  [Collider](https://collider.com/spider-man-across-the-spider-verse-hot-toys-figures/)).
  **Su pose es referencia 3D directa** para el punto 23 de ENCARGO.md.
- **Funko Pop**: Gwen Stacy oficial, imagen en la propia wiki
  (`GwenFunkoPop.png` 1300×1300 y `GwenFunko.png` 800×800, casillas 313/297 de
  la hoja `colaboraciones_01.jpg`). ✅.
- **Bandai S.H.Figuarts (Japón)**: figuras oficiales de la línea, incluida
  **Scarlet Spider** (Ben Reilly); merchandising con licencia en Disney
  Store Japón (sudadera, stickers metálicos, llaveros) y TOHO Theater Store
  (huchas con mascota de Miles y Gwen). ✅, dos fuentes en japonés
  ([tamashiiweb.com](https://tamashiiweb.com/item_character/spiderman_across-the-spiderverse/),
  [toho.co.jp](https://www.toho.co.jp/goods/cspider-verse)).
- **Burger King Brasil** (campaña con Sony, estreno de ATSV): 2 locales de
  São Paulo con fachada, «portales» de escaleras y combo «BK Aranhaverso»
  (Spider Burger + Spider Verse Fries + Multiverse Sundae). ✅
  ([LatinSpots](https://www.latinspots.com/noticia/spiderman-va-a-comer-con-bk-dm9-y-sony/66129)).
- **POP MART**: figuras blind-box oficiales de la serie ATSV (línea de
  colección, mercado asiático/global). ⚠️ (una fuente,
  [popmart.com](https://www.popmart.com/us/products/1936/marvel-spider-man-across-the-spider-verse-series-figures)).
- **Cosplay bien hecho, con materiales reales** (lo que pide ENCARGO.md, no
  para pegar sino como referencia de construcción):
  - Traje de Gwen: tutorial detallado (spandex, paneles termosellados,
    máscara con inserto rígido para mantener la forma de la capucha) en
    [RandomTuesday](https://randomtuesday.com/spidergwen-cosplay-tutorial/) ⚠️
    (una fuente, blog de cosplayer).
  - Chaqueta de Hobie: reportaje de «closet cosplay» con chaqueta de cuero,
    tachuelas y parches pintados a mano en
    [Bell of Lost Souls](https://www.belloflostsouls.net/2023/06/take-a-crap-in-the-establishment-the-spiderman-across-the-spider-verse-spider-punk-closet-cosplay.html)
    ⚠️ (una fuente).

---

## Las hojas de contacto (`hojas/`, 3 JPEG)

1. **`vestuario_01.jpg`** (hoja 4 del set principal, 2400×1704, 732 KB).
   Casillas 133-136: turnaround completo de Gwen con capucha puesta/quitada
   (Kristafer Anka). Casillas 147-160: 12+ variantes de ropa de calle de Gwen
   (Jesús Alonso Iglesias). Casillas 163-170: estudios de la chaqueta, parches
   y guitarra/bajo de Hobie (Jake Panian). Casilla 186: Funko Pop de Gwen.
   **Sirve para**: punto 15 (vestuario) y 19 (texturas/patrones).
2. **`colaboraciones_01.jpg`** (hoja 7 del set principal, 2400×1420, 452 KB).
   Casilla 49: skin de Gwen en **Fortnite**. Casillas 297/313: **Funko Pop**.
   Casillas 292-296: arte y concept de Gwen adicional. **Sirve para**: punto
   23 (colaboraciones y cruces), confirma visualmente lo que las fuentes de
   texto ya decían.
3. **`peterb_01.jpg`** (hoja propia de Peter B, 2400×1704, 572 KB, generada
   tras encontrar la página correcta de la wiki). Casillas 1-9: traje y pose
   de Spider-Man clásico. Casillas 10, 17-48: escenas familiares clave (el
   anillo, el beso, la despedida de Miles, la pelea con Olivia Octavius).
   **Sirve para**: punto 1 (arte oficial), el único personaje de los 5 que la
   biblia tenía en blanco.

## Lo mejor para la lámina

1. El turnaround de Gwen de Kris Anka (hoja `vestuario_01.jpg`, casilla 133)
   da la silueta y el hex exacto de su traje: sirve para cualquier lámina que
   la use de cuerpo entero.
2. El moodboard **«Black Punks»** de Evening Monteiro es la mejor prueba de
   que Hobie no es «punk genérico»: es un homenaje directo a la escena punk
   negra real, útil para justificar texturas de fotocopia/collage en vez de
   cuero liso.
3. El símbolo de araña rojo medido (`#BF0001`) es el hex más seguro de toda
   la biblia para el punto de logo/emblema del canal #edicion.
4. La skin de Gwen en Fortnite (hoja `colaboraciones_01.jpg`, casilla 49) es
   el gancho más reconocible para un chiste de «crossover» en el canal.
5. La chaqueta de Hobie con parches pintados a mano (Jake Panian) es la mejor
   referencia si la lámina 2 usa un objeto con «pegatinas»/washi tape en vez
   de un traje.

## No encontré ⚠️ (no es obligatorio, se anota igual)

- El **libro de arte** *The Art of the Movie* (ATSV): confirmé que existe
  (ISBN, editorial, páginas) pero no pude hojear su interior; sigue igual que
  antes.
- **Licencia exacta** del modelo de ScottPritchard en Sketchfab (campo vacío
  en la API): no se puede dar por CC, sólo mirar.
- Un **fotograma de día, sin luz de color encima**, del traje de Hobie o de
  Miles para medir su hex con la misma precisión que Gwen y Miguel: todos los
  que hay en las hojas están de noche o con neón encima.
- Colaboración **oficial** de moda (tipo Nike/Jordan × Spider-Verse): lo que
  aparece en `datos-imagen.md` (Openverse, «Air Jordan I High OG «Next
  Chapter»») es **un tenis inspirado**, no confirmé que sea colaboración con
  licencia de Sony; lo dejo fuera de la lista de colaboraciones por esa duda.
- Cifras de ventas o unidades de ninguno de los productos de merchandising
  (no las publican las tiendas).

## Bitácora de búsqueda (segunda pasada, imagen)

- **API de Fandom** (`spiderverse.fandom.com/api.php`), en inglés: 6
  llamadas (`list=search`, `list=allpages`, `action=query&redirects`,
  `action=parse&prop=wikitext`, 2× `generator=images`) para resolver la
  página de Peter B y sacar sus imágenes e hipervínculos.
- `herramientas/investigar_serie.py --wiki spiderverse --paginas "Peter Parker (Earth-616)"`
  → 2 hojas nuevas.
- **Sketchfab API** (`api.sketchfab.com/v3/search`, `/v3/models/<uid>`), en
  inglés: 4 llamadas para confirmar licencias de 3 modelos de grafiti.
- **Wallhaven API** (`wallhaven.cc/api/v1/search`), 3 consultas
  (`spider-man+2099`, `hobie+brown+spider+punk`, `spider-gwen`) para fondos
  de pantalla con tamaño real.
- **Pillow / `estilo.py`**, local: 9 imágenes procesadas para medir hex
  (Gwen, Miguel, símbolo rojo, más las que no sirvieron por tener luz de
  color encima).
- **Búsqueda web** (`WebSearch`), 8 consultas: en inglés «Fortnite Spider-Man
  Across the Spider-Verse skin…», «LEGO set official 2023», «Hot Toys Miles
  Morales…», «cosplay tutorial Gwen Stacy suit materials WonderCon», «cafe
  temático colaboración restaurante» (en español), «Hobie Brown Spider-Punk
  cosplay build», «halftone brush pack CC0», «McFarlane Toys» (sin resultado
  relevante, descartado); **en japonés**: «スパイダーマン アクロス・ザ・スパイダーバース
  コラボ 日本 グッズ» (Bandai S.H.Figuarts, Disney Store Japón, TOHO Theater
  Store).
- Total de fuentes nuevas de esta parte (no contando las que ya traía
  `datos-imagen.md`): **≈22** (wiki de producción ×7, Sketchfab API ×3,
  Wallhaven ×3, Fortnite ×2, LEGO ×2, Hot Toys ×2, Funko ×1 wiki, Bandai/Japón
  ×2, Burger King ×1, POP MART ×1, cosplay ×2).
