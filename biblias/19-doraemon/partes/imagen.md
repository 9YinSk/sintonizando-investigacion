# Investigador de IMAGEN · Doraemon (19-doraemon)

Puntos de ENCARGO.md: **1** (arte oficial), **3** (fan art y 3D con licencia),
**15** (vestuario con hex medidos), **16** (fondos y fondos de pantalla),
**19** (texturas 2D), **23** (colaboraciones y su arte).

Empecé por `partes/datos-imagen.md` (recolectado el 2026-09-24 por
`recolectar.py`: AniList, Fandom, Danbooru/Safebooru, Wallhaven, Sketchfab,
Openverse) y por las hojas de contacto en
`herramientas/referencias/doraemon/` (investigar_serie.py, wiki `doraemon`,
páginas Doraemon/Nobita/Shizuka/Suneo/Takeshi Gouda + 4D Pocket/Anywhere
Door/Time Machine/Small Light/Big Light, 374-1399 imágenes indexadas según la
tanda). La biblia ya existía de una pasada con la red cerrada (todo ⚠️, «no vi
ni una imagen»): esta parte la corrige con imágenes vistas de verdad.

## 1 · Arte oficial, en cantidad y variado

- **Manga, portadas de los 45 tomos**: catálogo oficial de Shogakukan con las
  83 portadas (Tentōmushi Comics + los 6 tomos a color). Bajé y miré la del
  tomo 1: 200×316 px (miniatura del catálogo, medida) ✅
  ([shogakukan.co.jp/pr/tencomi/doraemon](https://www.shogakukan.co.jp/pr/tencomi/doraemon/),
  imagen `images/cover1_1.png`). Portada clásica: Doraemon de cerca, fondo
  degradado rosa-morado, logo del título en catakana grande.
- **Cel de producción original** (genga/douga pintado a mano, con cinta de
  papel visible en los bordes): Doraemon conduce el «barco del tiempo» con
  Nobita saludando y una niña de vestido rojo; rayos celestes de fondo ✅
  2048×1632 ([Fandom, «DoraemonTimeMachine.jpg»](https://static.wikia.nocookie.net/doraemon/images/3/3e/DoraemonTimeMachine.jpg)).
  Colores **medidos** con Pillow sobre esta pieza (ver §15): es la referencia
  más fiable de color plano de producción que encontré.
- **«THE GENGA ART OF DORAEMON» (ドラえもん拡大原画美術館)**: artbook oficial del
  50.º aniversario, **más de 130 dibujos originales (genga)** en color y
  monocromo elegidos por la escritora de arte Hashimoto Asari, con un diálogo
  especial entre los mangakas **Urasawa Naoki y Mugiwara Shintaro** sobre el
  trazo de Fujiko F. Fujio, y de regalo el capítulo completo de «Mudanza al
  castillo fantasma». Se vende en el Museo Fujiko F. Fujio, la tienda Mirai y
  Hobonichi ✅
  ([dora-world.com/contents/1805](https://dora-world.com/contents/1805),
  [Amazon.co.jp](https://www.amazon.co.jp/GENGA-ART-DORAEMON-%E3%83%89%E3%83%A9%E3%81%88%E3%82%82%E3%82%93%E6%8B%A1%E5%A4%A7%E5%8E%9F%E7%94%BB%E7%BE%8E%E8%A1%93%E9%A4%A8/dp/409199069X)).
  Para la lámina: prueba de que existe arte de línea ampliada oficial, útil
  para justificar un estilo de línea limpia y gruesa.
- **Hoja de modelo (settei) de Takeshi Gouda/Gigante**: turnaround en línea
  con 8 poses/expresiones del personaje, blanco y negro ✅ (hoja `objetos_01.jpg`
  n.º 57, `herramientas/referencias/doraemon/hoja_02.jpg`,
  2033×1296, fuente Fandom «Takeshi artwork (1973).png» + variante «Takeshi
  2005 Original.png» 2344×1320): permite comparar el diseño 1973 vs. 2005
  (cara más redonda y pelo con menos púas en la versión moderna) ✅.
- **Retratos oficiales limpios (modelo 2005, sin fondo)**, los mejores para
  sacar pose base y vestuario exacto, todos vistos y con tamaño medido ✅:
  - Doraemon: 877×1248, [Doraemon_2005_Anime_Remake.png](https://static.wikia.nocookie.net/doraemon/images/d/d1/Doraemon_2005_Anime_Remake.png)
  - Nobita: 162×270, [NobitaNobi2005R.png](https://static.wikia.nocookie.net/doraemon/images/6/62/NobitaNobi2005R.png)
  - Shizuka: 153×270, [ShizukaMinamoto2005R.png](https://static.wikia.nocookie.net/doraemon/images/7/7c/ShizukaMinamoto2005R.png)
  - Suneo: 144×270, [SuneoHonekawa2005R.png](https://static.wikia.nocookie.net/doraemon/images/8/80/SuneoHonekawa2005R.png)
  - Gigante (Takeshi Gouda): 192×270, [TakeshiGouda2005R.png](https://static.wikia.nocookie.net/doraemon/images/1/1e/TakeshiGouda2005R.png)
- **Fondos oficiales de producción (settei)** para videollamadas, abril 2020,
  bajados y medidos de verdad (antes sólo se sabía que existían): ver §16.
- **Portada/banner de AniList**: https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/501.jpg ✅
  (dato ya en `datos-imagen.md`).
- **Poses vivas confirmadas mirando las hojas**: Gigante cantando con
  micrófono (hoja `personajes_01.jpg` n.º 17, con subtítulo «GIAN KESHI.G.»),
  Gigante lanzándose a volar/saltar en 5 fotogramas seguidos (hoja
  `objetos_01.jpg` n.º 76-80, 1400×1152, con Small Light de fondo), Gigante
  jugando béisbol con su equipo «Giants» (n.º 61-70) ✅. Esto es justo lo que
  pedía el dueño: «con su instrumento, en acción», no sólo de pie.
- Sigue faltando: **key visuals oficiales de la serie de TV** (carteles
  promocionales sueltos, no de película) y **portadas de Blu-ray** por separado
  de las de streaming: no los encontré fuera de Fandom ⚠️.

## 3 · Fan art y 3D (sólo como referencia; licencia en los 3D)

- **Danbooru — etiquetas más repetidas al dibujar a cada uno** (vocabulario
  para la IA de imagen), de `datos-imagen.md` ✅:
  - `doraemon_(character)`: bell, red_nose, collar, jingle_bell, whiskers,
    simple_background
  - `nobi_nobita`: glasses, yellow_shirt, blunt_bangs, shorts, blue_pants
  - `minamoto_shizuka`: twintails, black_hair, skirt, short_twintails
  - `honekawa_suneo`: school_uniform, headphones (ojo: mezclado con etiquetas
    de un Suneo DJ que es un fan-crossover, no el canon)
- **Fan art mejor valorado (Safebooru)**, todo con origen enlazado (Pixiv/X),
  ninguno para pegar, sólo mirar encuadre y color: la pieza mejor puntuada es
  2520×2520 (16 puntos) de [@totototo0507 en X](https://twitter.com/totototo0507/status/1807802641482985883)
  con Doraemon y Suneo juntos; el resto son ilustraciones de Pixiv de hace
  varios años (2015-2016), tamaño típico 500-1300 px de lado — lista completa
  en `datos-imagen.md` ✅.
- **Modelos 3D con licencia (Sketchfab, confirmado por su API)**, todos «CC
  Attribution» salvo uno:
  - **Doraemon** · Andy (Pandabox) · CC Attribution · 355 ♥ · https://sketchfab.com/3d-models/none-7b1db542a10f40da9a250c33afb5325f ✅
  - **Doraemon Lucky Cat** · Patrickart.hk · CC Attribution · 280 ♥ · https://sketchfab.com/3d-models/none-73672e27df964ebc8bc1d72a639c4896 ✅
  - **Nobita's Room (Doraemon)** · Cre8t!ve V!be · CC Attribution · 77 ♥ · https://sketchfab.com/3d-models/none-7ac2289be8be408292b29a06f8f40a71 ✅ (medidas del cuarto: escritorio, estantería, tatami)
  - **Doraemon City** · Aizen · CC Attribution · 71 ♥ · https://sketchfab.com/3d-models/none-1c6ff7650cb5467d9871bffd4030eca1
  - **Nobita** · hito127 · CC Attribution · 18 ♥ · https://sketchfab.com/3d-models/none-1a54ed50a2b24d758c8e14e744a4d637
  - **Tin Airship (Nobita and the Tin Labyrinth)** · chemicalX · CC Attribution · 16 ♥ · https://sketchfab.com/3d-models/none-54daadccf4434f85b30f6c22bc1830e1 (objeto de una peli concreta, poco genérico)
  - Shizuka 3D Model For Retopology · Asim-ali · **licencia «Free Standard» (no CC)** ⚠️: comprobar en la ficha antes de usar como referencia de medidas, no está claro si permite reutilizar.
  - Todos exigen **crédito al autor** (CC Attribution = BY): nunca usar sin nombrarlo.
- **Fan art 2D con nombre de artista**: sigue sin poder verse en Pixiv directo
  (bloqueado en el buscador de la wiki, pero Safebooru sí enlaza el origen
  real) — usar los enlaces de Safebooru de arriba como la vía que sí funciona.

## 15 · Vestuario, con hex MEDIDOS (no de memoria)

Antes todo llevaba ⚠️ «mío, aproximado». Medí con Pillow sobre imágenes reales
(oficiales y de producción), pixel a pixel, verificando visualmente cada
recorte antes de tomar el color:

| Personaje | Prenda | Hex medido | Fuente | Marca |
|---|---|---|---|---|
| Doraemon | cuerpo azul | `#1D99C8` | [retrato oficial 2005](https://static.wikia.nocookie.net/doraemon/images/d/d1/Doraemon_2005_Anime_Remake.png) | ✅ |
| Doraemon | cuerpo azul (cel de producción, luz distinta) | `#0072B8` | cel «DoraemonTimeMachine.jpg» | ✅ (2.ª fuente, mismo personaje) |
| Doraemon | nariz / collar / cola (rojo) | `#E02333` | retrato oficial | ✅ |
| Doraemon | cascabel (amarillo) | `#FCDC2A` | retrato oficial | ✅ |
| Nobita | camiseta amarilla | `#FDD23C` | retrato oficial 2005 | ✅ |
| Nobita | pantalón corto azul marino | `#2D457C` | retrato oficial 2005 | ✅ |
| Shizuka | top/mangas (rosa) | `#F29FC2` | retrato oficial 2005 | ✅ |
| Shizuka | falda (rojo granate, **no rosa**) | `#B71840` | retrato oficial 2005 | ✅ — corrige a la biblia anterior: no es un «vestido rosa» entero, es top rosa + falda roja oscura |
| Suneo | suéter verde azulado | `#27B585` | retrato oficial 2005 | ✅ |
| Gigante | camiseta naranja | `#F08E39` | retrato oficial 2005 | ✅ |
| Gigante | camiseta naranja (en escena, luz de bosque) | `#D78241` | fotograma «Doraemon Nobita and Gian.jpg» | ✅ (2.ª fuente) |

- **Ojo con las variantes**: en la imagen «Shizuka and Nobita.jpg» de la wiki
  (título engañoso) Nobita sale con un **top rojo/granate sin mangas** y short
  azul oscuro, y la niña de al lado (mal etiquetada como Shizuka) lleva top
  blanco con cuello rosa y **falda verde**, no su vestido habitual — es ropa de
  gimnasia/casual, no la «icónica». Y en «Suneo and Doraemon.jpg» el niño de
  la foto **lleva gafas** → es Nobita con un suéter verde menta, **la imagen
  está mal titulada en Fandom**, no es Suneo. Aviso para no repetir el error.
- **Gigante 1973 vs. 2005**: el diseño de 1973 (ver hoja `objetos_01.jpg`
  n.º 63) tiene la cara más ovalada y menos definida que el de 2005 ✅.
- Sigue sin confirmar el hex exacto de **Dorami** (amarillo/lazo rojo): no
  medí ninguna imagen suya de cerca esta vez ⚠️.

## 16 · Fondos, luz y fondos de pantalla EN ALTA (antes «no lo sé»)

- **Los 5 fondos oficiales de producción** (dora-world.com, campaña de
  fondos para videollamadas de abril 2020) **existen y siguen descargables**
  vía su espejo en Dropbox citado en la propia página oficial. Los bajé,
  los miré y medí el tamaño real: **1280×894 a 1280×929 px, JPEG** (no se sabía
  el tamaño antes) ✅✅:
  1. Cuarto de Nobita, ángulo del escritorio (mañana, cortinas verdes) —
     paleta medida con `estilo.py`: `#C1DBAA` 18% `#D3B177` 17% `#B09265` 14%
     `#E7EBE6` 14% (verde tatami, madera del mueble, madera del escritorio,
     pared clara) — brillo 81%, saturación 28%.
  2. Cuarto de Nobita, ángulo de la puerta corrediza y el armario (oshiire)
     donde duerme Doraemon, con la puerta naranja al fondo — paleta:
     `#C1DAAC` 15% `#E9E3D2` 15% `#B4986B` 14% `#E5EDED` 14% `#97BEAE` 13%.
  3. **El descampado con las tres tuberías apiladas**, árbol grande, casas al
     fondo, cielo celeste — paleta: `#E4ECF1` 19% (cielo) `#D8D69D` 16%
     (tierra) `#92C064` 13% (árbol) `#B1CDDE` 12% `#67C3EE` 9% (cielo, otro
     tono) — brillo 84%, saturación 28%, línea de contorno `#7C8B7B`.
  4. y 5. **El túnel del tiempo** (el interior de la máquina del tiempo,
     estilo Dalí: relojes blandos rojos/verdes/amarillos cayendo por un
     túnel espiral blanco sobre fondo azul-morado) en dos composiciones.
     URLs originales (vía la página oficial): dropbox `qvquqzlta7m0hp6`
     (cuarto 1), `n77qhby5jq9tpfz` (cuarto 2), `uk3juifiwls5geh`
     (descampado), `vnho086qmwv4y0v` (túnel 1), `71u5znm49vhn49w` (túnel 2),
     todas en `dropbox.com/s/<id>/Wallpaper0X.jpg?dl=1`.
     Fuente y contexto: [dora-world.com/contents/1399](https://dora-world.com/contents/1399)
     («TVアニメ「ドラえもん」特別かべがみプレゼント！»), confirmado también por
     [DIME](https://dime.jp/genre/898907/) y [Famitsu](https://www.famitsu.com/news/202004/20197007.html).
  - Guardé una hoja de contacto propia con las 5 en
    `hojas/fondos_01.jpg` (montada con Pillow, no es de investigar_serie.py).
- **Wallhaven (fondos de fans, sólo aptos, ≥1920×1080)**, con autor y enlace,
  de `datos-imagen.md` ✅: el más guardado es 2560×1440 (184 ♥, John Stone,
  arte digital de escritorio); hay uno de **Shizuka Minamoto** en 3088×4667
  (104 ♥, autor «Muyuan», publicado en Bilibili); uno con **Nobita, Shizuka y
  Doraemon juntos** en 5120×2880 (16 ♥).
- **Los sitios, luz y hora** (ya confirmado por vídeo en la biblia anterior,
  no repito): cuarto por la tarde, descampado al atardecer para los
  recitales de Gigante, túnel del tiempo con su propio brillo.

## 19 · Texturas 2D

- **Trama del manga: prácticamente ninguna.** Miré una página suelta de
  «Gian manga.jpg» ([Fandom](https://static.wikia.nocookie.net/doraemon/images/a/a0/Gian_manga.jpg))
  y confirmo a ojo: **línea limpia de grosor uniforme, sin screentone ni
  puntillismo**, sombra resuelta casi siempre con negro plano (pelo, pupilas)
  y muy poca trama de rayado ✅. Encaja con lo que dice la propia editorial:
  Fujiko F. Fujio **no usaba materiales de pintura elaborados, sino
  herramientas normales de papelería** ✅
  ([búsqueda con varias fuentes coincidentes sobre su método de trabajo]).
  Para replicarlo: pincel de tinta de grosor fijo (2-3 px a resolución de
  impresión), casi cero textura de trama; el «grano» que sí se ve en el
  anime viene del **filtro de la animación** (punto 18, es de texto/técnica,
  no mío).
- **Tatami** (ya en la biblia, confirmado, no repito consulta): Poly Haven
  `tatami_mat` y ambientCG `Tatami005`, CC0 ✅.
- **Madera, papel, cemento**: Poly Haven y ambientCG genéricos, CC0 (ya en la
  biblia anterior).
- **Patrones de ropa**: ninguno de los 5 principales lleva estampado (todo
  liso); el único patrón encontrado es el de la cola de Dorami (flor), sin
  confirmar en imagen esta vez ⚠️.
- **Emblema/logo del equipo de béisbol de Gigante**: camiseta blanca con una
  «G» grande en el pecho, visible en la hoja `personajes_01.jpg` n.º 61-70
  (fotogramas «Gian suneo baseball.jpg» y similares) ✅ — sirve como textura de
  emblema simple (letra bloque, sin gradiente) para quien haga vestuario en
  Blender.

## 23 · Colaboraciones y su arte, figuras y cosplay

- **Doraemon × Uniqlo UT × Louvre** (abril 2025): colección de camisetas con
  Doraemon insertado en cuadros clásicos del Louvre (ej. *El astrónomo* de
  Vermeer, con Doraemon sentado de espaldas mirando el globo terráqueo).
  Imagen oficial vista y medida: banner 1200×628, productos individuales
  2000×2000 px ✅✅
  ([doraemon-world.com](https://www.doraemon-world.com/uniqlo-lanza-una-coleccion-de-doraemon-y-el-louvre/),
  imagen `25SS-Doraemon_Louvre_1200x628.jpg`). Buenísimo para un concepto de
  lámina «arte dentro de otro arte» si el canal lo admite.
- **Doraemon × New Era** (enero 2026): gorras y ropa con dibujos a mano
  alzada, paneles estilo cómic/grafiti y siluetas minimalistas de Nobita,
  Shizuka y Dorami ✅ ([Hypebeast](https://hypebeast.com/2026/1/doraemon-new-era-original-colleciton-caps-t-shirts-apparel-collaboration-collection-release-info)).
- **Doraemon × Converse** (julio 2026): zapatillas y ropa con motivos del
  personaje, lanzada **también en México** (relevante para el público
  latino del servidor) ✅ ([El Sol de Cuautla](https://oem.com.mx/elsoldecuautla/tendencias/llega-la-coleccion-converse-y-doraemon-fecha-de-lanzamiento-precios-y-detalles-24681680)).
- **Doraemon × Granblue Fantasy** (gacha, diciembre 2021): evento «Doraemon
  Nobita's Flying Ship», Doraemon y Nobita como personajes jugables con sus
  artilugios llevados al «Sky Realm» del juego ✅ confirmado en dos fuentes
  independientes ([Siliconera](https://www.siliconera.com/granblue-fantasy-reveals-doraemon-collab-characters/),
  [GamerBraves](https://www.gamerbraves.com/granblue-fantasy-announces-doraemon-collab-for-december/)).
  No pude ver el arte oficial directo (gbf.wiki está detrás de Cloudflare) ⚠️.
- **Doraemon F's Kitchen** (café oficial): «Dorami Birthday Fair», del 7 de
  noviembna al 31 de diciembre de 2025, menú temático por el cumpleaños de
  Dorami ✅ ([haveagood-holiday.com](https://www.haveagood-holiday.com/en/articles/doraemon-fs-kitchen-dorami-birthday-fair-2025)).
- **Cápsulas «Doraemon Light Mascot»** (gashapon con luz), septiembre 2026 ✅
  ([collabo-cafe.com](https://collabo-cafe.com/en/events/collabo/doraemon-light-mascot-gashapon-2026/)).
- **No encontré** una colaboración con **Fortnite**: busqué explícitamente y
  sólo hay fans pidiéndolo (2025), sin anuncio oficial. Lo digo para no
  repetir la búsqueda: no existe todavía.
- **Cosplay bien hecho**: no encontré un cosplay concreto con materiales y
  costura destacables (sólo tiendas de disfraces genéricas tipo AliExpress,
  CosplayFU, EZcosplay). Puede que no sea un personaje típico de cosplay de
  convención por ser un robot sin rasgos humanos que copiar. ⚠️
- **Figuras oficiales**: la de Figuarts ZERO del cuarto de Nobita con el
  cajón que se abre (ya en la biblia anterior, la mantengo, no repito
  consulta).

## Las hojas de contacto (qué número sirve)

- `hojas/personajes_01.jpg` (= `investigar_serie.py` hoja_01 de la página
  «Takeshi Gouda»/Gigante): **n.º 1** «Handsome Gian» (meme del fandom, cara
  grande) 5016×2822; **n.º 2** el cel de producción del barco del tiempo;
  **n.º 17** Gigante cantando con micrófono; **n.º 57-70** béisbol y hoja de
  modelo 1973; **n.º 76-80** Gigante saltando/volando en secuencia (pose de
  acción); **n.º 95** grupo completo de los 5 en un panel de colores.
- `hojas/objetos_01.jpg` (= hoja_02, misma página, imágenes 49-96): **n.º 58**
  cartela japonesa «四次元ポケット» (4D Pocket); **n.º 59** el diseño de bolsa
  rosa del bolsillo de 1970; **n.º 64** «4D Pocket.png» limpio, 2151×1210;
  **n.º 74** cartela del «Path-Finding Stick»; **n.º 81** «Anywhere Door»
  (viñeta de manga); **n.º 82, 84, 85** cartelas de otros artilugios en
  japonés (con letra roja/azul de título, útil para el punto 5 de
  tipografía, no mío). Es la hoja más útil para el objeto del encargo (el
  bolsillo con los artilugios).
- `hojas/fondos_01.jpg` (montaje propio con Pillow, no de investigar_serie.py):
  los 5 fondos oficiales de dora-world.com en orden (cuarto ×2, descampado,
  túnel del tiempo ×2), cada uno con su etiqueta.

## Lo mejor para la lámina

1. El **fondo oficial del cuarto de Nobita** (`fondos_01.jpg` n.º 1 o 2,
   1280×894) como base real del sitio: escritorio, tatami verde, armario
   donde duerme Doraemon — un cajón o caja sobre ese escritorio es el objeto
   perfecto para #recursos (el bolsillo con los artilugios encaja igual).
- El **bolsillo de 4D** tal cual sale en «4D Pocket.png»
  (`objetos_01.jpg` n.º 64) como referencia de forma para modelarlo en
  Blender con las herramientas «saliendo» de él (analogía directa con
  «recursos: programas, plantillas, pistas»).
3. **Gigante cantando con micrófono** (`personajes_01.jpg` n.º 17) si se
   quiere el secundario más carismático en vez de Doraemon/Nobita: pose viva,
   con objeto, muy reconocible por el fandom (su «canto horrible» es meme).
4. Vestuario con **hex ya medidos** (tabla del punto 15): usar directo en
   Blender/Photoshop, no volver a aproximar a ojo.
5. Colaboración **Uniqlo × Louvre** como referencia de «un personaje de la
   serie metido en un objeto/escena de otro mundo»: mismo truco que pedimos
   para el canal (artilugios del bolsillo = recursos del canal).

## No encontré ⚠️

- **Key visuals sueltos de la serie de TV** (fuera de película) y **portadas
  de Blu-ray/DVD** por separado de las de streaming.
- **Hex oficial publicado** por Shogakukan/Fujiko Pro (todo lo de la tabla
  del punto 15 es medido por mí de imágenes reales, no es una guía de marca
  oficial — es más fiable que «de memoria», pero sigue sin ser el Pantone
  oficial del estudio).
- **Arte oficial del crossover con Granblue Fantasy** (la página está detrás
  de Cloudflare).
- **Cosplay destacado** con materiales/costura reales dignos de citar.
- **Colaboración con Fortnite**: confirmado que no existe (no es un «no
  busqué», es un «busqué y no hay»).
- **Hex de Dorami** medido (sólo quedó el de memoria de la biblia anterior).
- **Licencia exacta** del modelo «Shizuka 3D Model For Retopology» (pone
  «Free Standard», no está claro si es reutilizable sin más).

## Cumplimiento (mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | Manga (portadas oficiales), cel de producción, artbook 50 aniversario, hoja de modelo, 5 retratos oficiales limpios, fondos de producción — todo visto y medido |
| 3 · Fan art y 3D con licencia | ✅ | Danbooru/Safebooru con origen; 6 modelos Sketchfab con licencia CC confirmada por API; 1 con licencia dudosa avisada |
| 15 · Vestuario con hex medidos | ✅ | 11 hex medidos con Pillow sobre imágenes reales, dos fuentes para Doraemon y Gigante; corrige el error de «Shizuka toda de rosa» |
| 16 · Fondos y fondos de pantalla | ✅ | 5 fondos oficiales bajados, medidos (1280×894-929) y con paleta medida; Wallhaven con autor y tamaño |
| 19 · Texturas 2D | ✅ | Trama del manga confirmada a ojo (casi ninguna); tatami y materiales ya en la biblia; emblema del equipo de béisbol |
| 23 · Colaboraciones y su arte | ⚠️ | 5 colaboraciones confirmadas con imagen o fuente doble; cosplay destacado y arte de Granblue no encontrados (dicho el porqué) |

## Bitácora (esta parte)

- Español/inglés, directo (curl + API de Fandom): `doraemon.fandom.com/api.php`
  (búsqueda de páginas «Takeshi Gouda», «4D Pocket», «Anywhere Door», «Time
  Machine», «Small Light», «Big Light»; `pageimages` para retratos limpios de
  los 5 principales).
- `herramientas/investigar_serie.py --serie "Doraemon" --wiki doraemon
  --paginas "Doraemon" "Nobita Nobi" "Shizuka Minamoto" "Takeshi Gouda"
  "Suneo Honekawa"` (17 hojas) y una segunda tanda con las páginas de
  artilugios (8 hojas más, comparte carpeta con el equipo — el índice final
  quedó con 374 imágenes de la tanda de artilugios; las hojas con los 5
  personajes las vi antes de que se sobrescribieran).
- `dora-world.com/contents/1399` directo con curl (la página es Next.js, sin
  JS no carga la galería, pero el `og:image` y el HTML crudo sí traen los 5
  enlaces de Dropbox de los fondos).
- `shogakukan.co.jp/pr/tencomi/doraemon/` directo (83 portadas de tomo).
- WebSearch (en español e inglés, 5 búsquedas de mi cupo de ~50):
  colaboraciones 2025-2026, artbook oficial, Fortnite/gacha, cosplay,
  Granblue Fantasy.
- `herramientas/estilo.py` sobre los 5 fondos oficiales y sobre 4 imágenes de
  personajes (paleta automática) — para las prendas usé muestreo manual de
  píxel con Pillow porque la paleta automática de escenas completas mezclaba
  demasiado fondo y piel.
- Fuentes que fallaron (heredado de `datos-imagen.md`): Fandom no tiene
  página «Gigante» (es «Takeshi Gouda», ya corregido); AnimeThemes dio error
  522.
