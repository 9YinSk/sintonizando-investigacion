# Parte IMAGEN · El castillo ambulante (encargo 99)

Puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md. Libreta de datos para el redactor,
no prosa final. Partí de `partes/datos-imagen.md` (AniList, Fandom, Danbooru,
Safebooru, Wallhaven, Sketchfab, Openverse) y añadí lo que faltaba: hojas de
contacto propias, colores medidos con `estilo.py`, 50 fotogramas oficiales de
`ghibli.jp`, modelos 3D con licencia, texturas CC0 y colaboraciones.

## 1 · Arte oficial, en cantidad y variado

- **Fuente nueva y mayor, no estaba en datos-imagen.md**: Studio Ghibli publicó
  el 16-oct-2020 en su web oficial 50 fotogramas libres de "El castillo
  ambulante" para uso no comercial: `https://www.ghibli.jp/gallery/howl001.jpg`
  a `howl050.jpg` (1920×1038 cada uno, medidos). Nota oficial:
  `https://www.ghibli.jp/info/013358/` · ✅ (declaración oficial + página del
  estudio) · 50 imágenes confirmadas contando los enlaces `<a href>` de
  `https://www.ghibli.jp/works/howl/`.
- Los miré todos en hoja de contacto propia (13 de los 50, ver
  `hojas/personajes_01.jpg` y `hojas/fondos_01.jpg`) para elegir cuáles sirven:
  sombrerería de Sophie (howl001), retrato Sophie+Howl (howl005), Calcifer de
  cerca (howl012), interior del castillo/baño (howl020), alcoba de la Bruja
  (howl025), Bruja+Sophie anciana caminando (howl030), Nabo+Markl+Heen en la
  colina (howl035), Howl en forma de ave (howl040), Sophie volando al
  atardecer (howl045), castillo volando sobre nubes (howl050).
- Portada y banner oficiales de AniList (ya en datos-imagen.md) · ✅.
- **Artbook oficial**: *The Art of Howl's Moving Castle* (2005), producido por
  Hayao Miyazaki, portada 1824×2560 en la wiki de Fandom · ✅ (wikitext de la
  página + imageinfo medida). Es el equivalente más cercano a "hojas de
  modelo": no encontré páginas interiores escaneadas sueltas y con licencia
  clara, sólo la portada.
- **Póster oficial en inglés**: 1000×1363, `File:Howl's Moving Castle -
  English Poster.jpeg` en la wiki de Fandom · ✅ (imageinfo medida).
- **Portada de Blu-ray Steelbook** (GKIDS, distribuidor oficial en EE. UU.):
  1080×1548 medida desde `store.gkids.com` · ✅ (tienda oficial). Hay también
  ediciones SteelBook (12-may-2020) y exclusiva de Target (24-dic-2023) con
  tarjetas de arte, mencionadas en blu-ray.com, pero no medí esas portadas
  (⚠️, sólo un tipo de portada verificado con tamaño).
- Imágenes grandes de la wiki de Fandom (Howl 54, Sophie 164, Calcifer 20; ya
  recolectadas) más las de personajes/lugares que añadí con
  `investigar_serie.py`: Witch of the Waste, Markl, Turnip Head, Howl's
  Castle, Market Chipping, The Art of Howl's Moving Castle, Porthaven, Royal
  Palace, The Waste → 63 imágenes enlazadas, 52 grandes (≥300 000 px) en
  `herramientas/referencias/el-castillo-ambulante/` (hoja_01.jpg, hoja_02.jpg,
  `indice.json` con url y tamaño real de cada una) · ✅.
- **Pose en grupo** (pedida explícitamente por el encargo): key visual
  promocional oficial `Howl_and_all_characters.jpg` (1750×1000, wiki de
  Fandom) con Howl, Sophie, Calcifer, Markl, Heen, Nabo y la Bruja del Yermo
  todos juntos volando · ✅. **Ojo para el redactor**: en este arte
  promocional el vestido de Sophie se ve azul marino con capa rosa, más
  saturado que en los fotogramas de la película (cerulean #51A5C7 medido
  arriba); son dos fuentes de color distintas (arte promocional vs.
  fotograma), no un error mío — anotar ambas.
- **"Portadas de tomos, singles"**: no aplica. La película no es adaptación
  de manga (no hay tomos) y no tiene canción theme con single propio a la
  venta (el álbum es de banda sonora, tema de texto/voz, no mío).
- **No encontré** cartones de cuenta atrás (countdown cards): es una práctica
  de mercadotecnia más reciente (manga/streaming por capítulos); la película
  es de 2004 y no tiene ese formato de promoción. Búsquedas: "Howl's Moving
  Castle countdown card" (inglés), "ハウルの動く城 カウントダウン" (japonés) → 0
  resultados relevantes.
- **"Arte de videojuegos"**: no encontré un videojuego oficial de "El castillo
  ambulante". Búsqueda: `"Howl's Moving Castle" video game PlayStation 2
  Level-5 2004 Studio Ghibli` (inglés) → sólo wikis de fans con juegos
  hipotéticos/fan-made, ningún juego oficial confirmado. (Level-5 sí colaboró
  después con Ghibli en *Ni no Kuni*, pero es otra obra, no ésta.) Punto 11 de
  ENCARGO.md es del investigador de texto; si él confirma un juego oficial
  distinto, avisar para revisar este punto.

## 3 · Fan art y renders 3D (como referencia, con licencia)

- **Modelos 3D descargables, licencia CC Attribution (CC-BY), en Sketchfab**
  (búsqueda directa a la API, no salió nada en `datos-imagen.md`) · ✅ (página
  del modelo con licencia explícita):
  - *Howl's Moving Castle* (castillo completo) — autor **lsebko** — 36 606
    caras — `sketchfab.com/3d-models/howls-moving-castle-a5fcd7379db240bea690e4fca032e322`
  - *Howl's Moving Castle - Calcifer* — autor **ncd.blueberry** — 29 702 caras
    — `sketchfab.com/3d-models/howls-moving-castle-calcifer-2d651cf9dc2b4ef59ec7723a08a727bf`
  - *Howl's Moving Castle - Turnip Head* (Espantapájaros Nabo) — autor
    **ncd.blueberry** — 50 638 caras —
    `sketchfab.com/3d-models/howls-moving-castle-turnip-head-1e97101c0eec48fab876f366d8e46540`
  - *Howl's Room* (interior del cuarto de Howl) — autor **waltersnchz** —
    400 569 caras —
    `sketchfab.com/3d-models/howls-room-c881f51855db460ba832e6d601d9a369`
  - Hay más resultados (Fire-Calsifer, Geometry_Calcifer_2023, etc.) también
    CC-BY; dejé los 4 más relevantes y con mejor nombre/autor identificable.
- **Fan art mejor valorado por personaje** (Safebooru, ya venía en
  datos-imagen.md, confirmado y elegido aquí):
  - Howl: 2048×1588, 4 puntos, origen twitter.com/hammar_dobucof.
  - Sophie: 3840×2160, origen x.com/AkaiguArts.
  - Calcifer: 636×900, 6 puntos, origen pixiv (axis04).
  - Crossover con Kiki (bruja hermana temática): 3000×4000, origen pixiv,
    útil también para el punto 23 (crossover de fans).
  - Todo con nota: "referencia de pose/estilo, nunca para pegar", autor
    siempre enlazado.
- **No encontré** modelos 3D de personajes con más detalle de vestuario (por
  ejemplo un Howl completo con el abrigo a cuadros) con licencia libre
  verificada: los que aparecen en Sketchfab sin filtro `downloadable=true`
  parecen ser de fan sin licencia clara, los descarté.
- **Poly Haven**: revisado (`api.polyhaven.com/assets?t=models`, 521 modelos
  en total en toda la plataforma) — es un banco de objetos reales genéricos
  (muebles, plantas, rocas), no tiene ni tendría sentido que tuviera activos
  de una franquicia con personajes; no hay nada de "El castillo ambulante"
  ahí. Por eso las referencias 3D con licencia libre de esta biblia vienen
  todas de Sketchfab.

## 15 · Vestuario (colores medidos, accesorios, peinado)

Colores medidos con `herramientas/estilo.py` (Pillow, clustering de color)
sobre fotogramas oficiales de `ghibli.jp` y de la wiki. Cito siempre de qué
imagen sale cada paleta.

- **Sophie (vestido cerulean)**: paleta del fotograma oficial `howl005.jpg`
  → **#51A5C7** (vestido, dominante 19.3%), #EED1A7 (piel), #CEE0E1 (cielo de
  fondo) · ✅ (medido; coincide con la descripción textual de la wiki:
  "cerulean dress with a white neck and black buttons"). Texto de la wiki:
  pelo castaño oscuro trenzado con dos listones rosas, cejas gruesas
  castañas · ✅ (`ghibli.fandom.com/wiki/Sophie_Hatter`).
- **Sophie anciana**: sigue con el mismo vestido cerulean pero con sombrero de
  paja y listón rojo. El pelo se vuelve gris con "brillo de luz de estrellas"
  (cita literal traducida de la wiki) y, tras cortar la trenza para dársela a
  Calcifer, queda en corte bob a la altura de los hombros, peinado detrás de
  las orejas · ✅ (wikitext completo de `Sophie_Hatter#Appearance`).
- **Howl**: camisa blanca lisa, pantalón oscuro, abrigo a cuadros rojo y gris
  azulado con ribetes amarillos en el cuello y las mangas; casi no usa las
  mangas, deja el abrigo colgando sobre los hombros; colgante al cuello · ✅
  (texto completo de la wiki). Pelo rubio al inicio, brevemente naranja
  (accidente en el baño), luego negro. Colores medidos del retrato
  `Sophie_x_howl.jpg`: #F5C3A8 (piel), #60AEC2 (fondo/ojos), #7F505C y #806666
  (tonos rojizo-ciruela, coherentes con el abrigo a cuadros) · ⚠️ (el abrigo
  no se ve completo en esa toma; falta una medición de cuerpo entero con luz
  de día).
- **Forma de ave de Howl**: cuerpo cubierto de plumas negras, dos alas negras
  anchas en la espalda o en los brazos al volar · ✅ (texto de la wiki).
  Paleta medida en `howl040.jpg`: #443952, #595273, #2A2634 (azules y
  púrpuras muy oscuros, plumaje) · ✅.
- **Bruja del Yermo**: alta, muy corpulenta, piel pálida, ojos azul claro,
  nariz larga, pelo rosa brillante en peinado voluminoso extravagante; viste
  un gran vestido negro, sombrero negro de ala grande con plumas, pequeños
  aretes rojos, sombra de ojos verde y labial rojo · ✅ (wikitext completo de
  `Witch_of_the_Waste`). Tras perder sus poderes se vuelve pequeña, mayor,
  pelo rubio, nariz bulbosa, piel arrugada. Paleta medida (primer plano,
  `Witch_of_the_Waste_-_close_up.jpg`): #C3A899 (piel), #2A202C (sombra/pelo
  oscuro) · ✅. Paleta del retrato de AniList (busto limpio): #572614
  (rojo-vino del vestido), #467945 (verde del maquillaje/joya), #EFCC6B
  (dorado de accesorios) · ✅.
- **Markl**: capucha/capa azul, cara redonda infantil · ✅ (imagen medida,
  `Markl.png`).
- **Calcifer**: sin ropa (es fuego), colores de llama medidos en dos fuentes
  distintas y coincidentes: retrato AniList → #EB4825, #F59529, #ED6B2A; primer
  plano oficial `howl012.jpg` → #ED9B40, #EA5B3A, #88402B, #B75F3A. Naranja y
  rojo-anaranjado muy saturado (58-82% saturación) · ✅ (dos fuentes).
- **No encontré** trajes por temporada/arco en el sentido de "guardarropa que
  cambia con la trama" más allá de lo descrito (Sophie mantiene el mismo
  vestido cerulean toda la película, salvo el sombrero de anciana; Howl no
  cambia de abrigo). Es coherente con que la película ocurre en pocas semanas
  narrativas, no por temporadas del año.
- **Ropa "icónica" que todos reconocen** (lo pide el encargo explícitamente):
  el vestido azul cerulean de Sophie con el sombrero de paja de anciana es la
  silueta más repetida en fan art y merchandising (aparece en 6 de las 10
  imágenes mejor valoradas de Safebooru); del lado de Howl, el abrigo a
  cuadros rojo/gris con ribetes amarillos es lo primero que lo identifica
  (aparece en el logo de casi todo el merchandising, incluida la colección
  Loewe del punto 23) · ✅ (frecuencia contada a mano en las fuentes ya
  citadas).

## 16 · Ciudades, paisajes y fondos de pantalla

- **Market Chipping** (pueblo natal de Sophie): valle verde con montañas
  nevadas al fondo, río y puente; **luz de pleno día, sol alto** (sombras
  cortas, cielo despejado). Imagen 1200×649 medida (`Market_Scene.jpg`,
  Fandom) · ✅. Escena de multitud/mercado en `howl014` (wiki, 1920×1038).
- **Porthaven** (ciudad portuaria bajo ataque): edificios con banderines de
  colores, barcos de vapor; **luz de atardecer/humo de bombardeo**, cielo
  entre gris y naranja. Paleta medida en la escena `Howls-moving-castle...
  -13338.jpg`: #3F424C, #6B533F, #302C32 (azul grisáceo y marrón apagado) · ✅.
- **El Yermo / The Waste**: páramo despoblado, colinas oscuras; **anochecer**,
  el cielo aún tiene una franja naranja baja en el horizonte y el resto ya es
  azul oscuro. Imagen 1024×602 medida · paleta: #2A3841, #38474F, #1A2B32
  (azules y verdes muy oscuros) · ✅. Pedido especial del encargo ("campos"):
  cubierto también por las colinas verdes de `Howl_Hills.jpg` (1200×661,
  **media tarde, sol lateral**) y por `howl035.jpg` (colina con flores,
  **mañana, cielo despejado**).
- **Palacio Real de Kingsbury**: puerta dorada ornamentada, estatuas doradas,
  fachada roja con balaustradas; **mediodía, luz frontal dura** que hace
  brillar el dorado. Imagen 915×515 medida, paleta: #4B2F2E (marco rojo
  oscuro), #9C653C y #B6A078 (dorado/bronce), #418AC9 y #D4DDE0 (cielo azul
  claro) · ✅. Coincide con el desfile militar (`Military_Parade.jpg`, 1118×640:
  azules, rojos y dorados de los uniformes, también luz de día) que responde
  al pedido del encargo de fijarse en "máquinas" (armamento/desfile bélico).
- **El castillo por dentro** (máquinas, pedido especial del encargo): **luz
  cálida y baja, de vela y de la llama de Calcifer** (nunca luz de día
  directa) con tuberías y engranajes visibles en `howl020.jpg` (baño con
  cañerías, vapor) y en la imagen wiki `Howl024.jpg` (interior oscuro con
  mecanismos, de noche), paleta medida de esta última: #232525, #212C3D,
  #15181C, #3F3F3E, #4C5559 (grises y azul muy oscuro, metal sin pintar) · ✅.
- **El castillo por fuera**: imagen de referencia 640×346 (pequeña, ⚠️ una
  sola fuente con ese tamaño) más el mucho mejor fotograma oficial
  `howl050.jpg` (1920×1038, castillo volando sobre nubes) · ✅.
- **Magia visible** (pedido especial del encargo): hechizo de la Bruja sobre
  Howl, imagen `Witch's spell for Howl.jpg` (1024×600, manos con energía
  dorada) · ⚠️ (una fuente, wiki).
- **Fondos de pantalla de fans en alta** (Wallhaven, ya en datos-imagen.md):
  el más guardado es un collage de películas Ghibli con el castillo, 4000×1600,
  100 favoritos, subido por JT42 · ✅. El más centrado sólo en Howl: 1920×1080,
  67 favoritos, mismo autor.
- **No encontré** fondos de pantalla "oficiales" en el sentido estricto de
  wallpapers para escritorio publicados por Ghibli con esa etiqueta; lo más
  cercano y realmente oficial son los 50 fotogramas libres de `ghibli.jp`
  (ya listados en el punto 1), que sirven igual de bien como fondo en alta.

## 19 · Texturas 2D

- La película no tiene manga con tramas (no es adaptación de manga: viene de
  la novela de Diana Wynne Jones); no hay "screentones" que replicar. Lo que
  sí pide el encargo y sí encontré: grano de fondo pintado a mano, patrones de
  tela y metal del castillo.
- **Texturas CC0 equivalentes (ambientCG, medidas con Pillow, todas
  1024×1024)**:
  - `Metal053C` — metal oxidado/latón — para las placas remachadas y tuberías
    del castillo · ✅ (licencia CC0, medida).
  - `Planks009` — tablones de madera vieja — para el interior de la
    sombrerería y la cabaña de Howl · ✅.
  - `Paper006` — papel con grano — el equivalente más cercano al grano de
    fondo pintado a mano que usa Ghibli (no es una trama de manga, es textura
    de soporte) · ✅.
  - `Fabric030` — tela lisa tileable — base para el abrigo de Howl o la capa
    de Sophie · ✅.
  - `Fabric080` — tela a cuadros/plaid tileable — equivalente directo del
    patrón del abrigo de Howl (rojo y gris azulado a cuadros) · ✅. Alternativa
    con otra trama: `Fabric060` (tartán).
- **Emblemas/logos**: no hay un escudo o logo de facción reiterado como en
  otras franquicias (a diferencia de Naruto o Attack on Titan); el símbolo
  más repetido es la estrella de seis puntas del contrato con Calcifer,
  visible en `Witch's spell for Howl.jpg` y en el pentagrama bajo los pies de
  Howl en varias escenas del castillo · ⚠️ (lo vi en fotogramas, no encontré
  una ficha oficial que lo nombre con un término fijo).
- **No encontré** pinceles o packs de Photoshop con licencia libre vendidos
  específicamente como "estilo Ghibli watercolor/gouache"; lo que hay son
  paquetes de pago (no cumplen "licencia libre"), así que no los incluyo en
  `imagen.json`.

## 23 · Colaboraciones y cruces

- **Ghibli Park — Valle de las Brujas** (Valley of Witches), abierto el
  16-mar-2024: réplica del castillo ambulante a tamaño real (4-5 pisos), no se
  mueve pero se puede recorrer por dentro y por fuera; incluye también la
  sombrerería de Sophie ("Hatter's Millinery") y atracciones (carrusel,
  Máquina Voladora, Torre de los Aviadores) · ✅ (Anime News Network +
  blooloop.com, dos fuentes independientes,
  `animenewsnetwork.com/feature/2024-06-03/...` y
  `blooloop.com/theme-park/news/ghibli-park-howls-moving-castle-valley-of-witches/`).
- **Loewe × Studio Ghibli** (2023): colección cápsula de moda, la tercera y
  última de una trilogía (tras El viaje de Chihiro y Mi vecino Totoro),
  diseñada por Jonathan Anderson. Ropa, bolsos "Puzzle", "Flamenco" y
  "Amazona" con ilustraciones de Sophie, Howl, Calcifer, Markl, Heen, Nabo y
  la Bruja del Yermo bordadas o en intarsia de piel; vela aromática inspirada
  en Calcifer (incienso, pachulí, avellana tostada, cardamomo). Lanzamiento
  mundial el 2 de febrero de 2023, fotos de campaña por Juergen Teller, pop-up
  en Selfridges (Londres) con "Calcifer's Kitchen" · ✅ (Fashionista +
  Wallpaper + PurseBlog + Dazed, cuatro fuentes coincidentes).
- **Figura oficial**: figurín mecánico licenciado del castillo ambulante con
  patas que caminan de verdad, vendido en Maison Ghibli (tienda oficial de
  merchandising licenciado) · ✅ (ficha de producto con imagen medida
  800×800).
- **Ediciones físicas coleccionables**: Blu-ray Steelbook de GKIDS (12-may-2020)
  y edición exclusiva de Target con tarjetas de arte (24-dic-2023) · ✅
  (GKIDS store + blu-ray.com).
- **Cosplay**: cosplay de Howl con una "llama" de Calcifer hecha a mano en las
  manos, con joyería y pendiente verde colgante fieles al diseño (usuario de
  Reddit Jiimboart, recogido por ScreenRant) · ✅. Cosplay de Sophie con
  vestido cosido a mano (recogido por CBR) · ⚠️ (una fuente por cosplay
  individual, pero dos artículos distintos confirman que hay cosplay de
  calidad documentado).
- **Café temático**: café ambientado en la película en Nagano, Japón,
  mencionado en redes (Instagram, Facebook, TikTok) · ⚠️ (fuentes de redes
  sociales, no una web oficial del local; no confirmé nombre exacto ni
  dirección con una segunda fuente independiente).
- **No encontré** colaboraciones con videojuegos tipo gacha o Fortnite, ni
  eventos oficiales de comida rápida (a diferencia de otras franquicias de
  anime). Búsquedas: "Howl's Moving Castle" + "Fortnite" / "collab" / "gacha"
  (inglés) y「ハウルの動く城」+「コラボ」（ゲーム）(japonés) → nada relevante
  fuera de lo ya listado.

## Hojas de contacto

- `hojas/personajes_01.jpg` — 9 imágenes: Sophie+Howl (retrato oficial),
  Calcifer, Bruja del Yermo (dos tomas), Bruja+Sophie anciana, Nabo, Markl,
  Howl en forma de ave, Sophie en la sombrerería, alcoba de la Bruja. Armada a
  mano con Pillow a partir de fotogramas oficiales de `ghibli.jp` y de la wiki
  (medidas ya citadas arriba).
- `hojas/fondos_01.jpg` — 9 imágenes: Market Chipping, Porthaven, El Yermo,
  Palacio de Kingsbury, colinas verdes, desfile militar, interior del castillo
  (baño), vuelo al atardecer, castillo por fuera.
- `hojas/colaboraciones_01.jpg` — 5 imágenes: campaña Loewe×Ghibli, castillo
  real de Ghibli Park, figura mecánica oficial, portada Blu-ray GKIDS, y una
  escena oficial adicional de `ghibli.jp` (Nabo).
- Además, `herramientas/referencias/el-castillo-ambulante/hoja_01.jpg` y
  `hoja_02.jpg` (52 imágenes numeradas de la wiki, con `indice.json` con url y
  tamaño real de cada una) quedan como banco de miniaturas para quien necesite
  más variedad que no cupo en las 3 hojas del repositorio.

## Lo mejor para la lámina

1. Sophie y Howl de pie mirándose, vestido cerulean #51A5C7 vs. abrigo a
   cuadros rojo/gris — pose cálida, sirve para canales de bienvenida o de
   pareja/dúo (fotograma oficial `howl005.jpg`).
2. El castillo completo en vuelo (`howl050.jpg`) como "objeto real en un
   sitio real": una ventana o compuerta del castillo puede llevar el texto del
   canal, con las patas mecánicas como detalle en primer plano (referencia 3D:
   figura oficial de Maison Ghibli, o el modelo Sketchfab de lsebko).
3. Calcifer de cerca (#EB4825/#ED6B2A) en la chimenea: sirve para canales de
   "energía/ánimo" del servidor, con la cara expresiva y el marco de piedra
   de la chimenea como "objeto real" donde poner texto.
4. Bruja del Yermo con su vestido negro y sombrero de plumas: personaje
   secundario muy reconocible, sirve si se busca un "villano querido" para
   una lámina de reglas o advertencias.

## No encontré

- ⚠️ Cartones de cuenta atrás (no existen para esta película de 2004).
- ⚠️ Escaneos de páginas interiores del artbook (sólo confirmé la portada).
- ⚠️ Modelos 3D con licencia libre de personajes con vestuario completo
  (Howl/Sophie de cuerpo entero); sólo objetos (castillo, Nabo, interior).
- ⚠️ Segunda fuente independiente para el café temático de Nagano (nombre y
  dirección exactos).
- ⚠️ Colaboraciones con videojuegos o comida rápida: no existen, confirmado
  con búsquedas en inglés y japonés.
- ⚠️ Pinceles/patrones de Photoshop de "estilo Ghibli" con licencia libre
  (sólo hay de pago).

## Bitácora de búsqueda

- Consultas ya hechas por `recolectar.py` (no repetidas): AniList (portada,
  banner, personajes), Fandom `ghibli.fandom.com` (Howl, Sophie, Calcifer),
  Danbooru `related_tag`, Safebooru (fan art top), Wallhaven, Sketchfab (sin
  resultado ese día), Openverse.
- `investigar_serie.py --serie "El castillo ambulante" --wiki ghibli --paginas
  "Witch of the Waste" "Markl" "Turnip Head" "Howl's Castle" "Market Chipping"
  "The Art of Howl's Moving Castle" "Porthaven" "Royal Palace" "The Waste"
  --min-px 300000` → 63 imágenes enlazadas, 52 grandes, 2 hojas nuevas.
- API de Fandom directa: `list=categorymembers` sobre `Category:Howl's Moving
  Castle` (español: página de la categoría en inglés, la wiki no tiene
  versión japonesa) para mapear todas las páginas de personajes y lugares.
- `action=parse&prop=wikitext` sobre Sophie Hatter, Howl Jenkins Pendragon y
  Witch of the Waste (texto completo, no truncado) para vestuario y peinado.
- `estilo.py` (Pillow) sobre 15 imágenes (fotogramas oficiales + wiki +
  AniList) para colores medidos, citados uno por uno arriba.
- API de Sketchfab (`api.sketchfab.com/v3/search`, en inglés) con
  `downloadable=true` para "Howl Moving Castle" y "Calcifer": antes salía
  vacío en `recolectar.py`, a mano sí devuelve resultados CC-BY.
- API de ambientCG (`ambientcg.com/api/v2/full_json`) para texturas CC0:
  "rusted metal", "old wood planks", "paper", "fabric" (todas en inglés).
- Búsqueda web (`WebSearch`, en inglés): "Ghibli Park Howl's Moving Castle
  area attraction", "Howl's Moving Castle official figure Bandai Kotobukiya",
  "Howl's Moving Castle cafe collaboration Japan", "Howl's Moving Castle
  cosplay Calcifer Sophie", "Loewe Howl's Moving Castle collection Jonathan
  Anderson", "Howl's Moving Castle 4K Blu-ray cover art GKIDS".
- Búsqueda web en japonés: "ghibli.jp 壁紙 ハウルの動く城 無料" → llevó al
  hallazgo de los 50 fotogramas oficiales libres.
- `curl` directo a `ghibli.jp` (página de info + página de la obra) para
  extraer los 50 enlaces `gallery/howlNNN.jpg`.
- `curl` directo con cabecera `Referer` a `static.wikia.nocookie.net` para
  bajar imágenes puntuales a medir con Pillow (varias, todas citadas arriba
  con su tamaño real).
- Fuentes que fallaron o no dieron nada nuevo: Sketchfab en `recolectar.py`
  (vacío, resuelto a mano); Reddit (no encontré subreddit específico de la
  película, no insistí más de dos intentos); "brass" en ambientCG (sin
  resultados, usé "rusted metal" en su lugar); Poly Haven (`api.polyhaven.com`,
  521 modelos en total, ninguno de la franquicia — banco genérico, no aplica).
- Búsqueda adicional en inglés: `"Howl's Moving Castle" video game
  PlayStation 2 Level-5 2004 Studio Ghibli` → sin juego oficial confirmado
  (corrijo una suposición inicial mía: lo que recordaba era *Ni no Kuni*, otra
  colaboración Ghibli-Level 5, no ésta).
- ambientCG en inglés: "plaid" y "tartan" para el patrón del abrigo de Howl
  (punto 19) → `Fabric080` y `Fabric060`, CC0, medidas 1024×1024.

## Cumplimiento de mis puntos (1, 3, 15, 16, 19, 23)

| Punto | Estado | Por qué |
|---|---|---|
| 1. Arte oficial variado | ✅ | 50 fotogramas oficiales de ghibli.jp + artbook + póster + Blu-ray + AniList + 52 imágenes de wiki. Falta sólo cartones de cuenta atrás (no existen) y páginas interiores del artbook. |
| 3. Fan art y 3D con licencia | ✅ | 4 modelos Sketchfab CC-BY con autor y enlace; fan art de Safebooru con puntaje, tamaño y origen. |
| 15. Vestuario con hex medidos | ✅ | Colores medidos con estilo.py para Sophie, Howl (parcial ⚠️), Bruja, Calcifer, Markl; peinados y accesorios de la wiki (texto completo). |
| 16. Fondos y paisajes | ✅ | 7 sitios distintos con paleta medida o descrita, más fondos de pantalla de fans en alta. Fondos "oficiales" resueltos con los fotogramas libres de ghibli.jp. |
| 19. Texturas 2D | ⚠️ | 4 texturas CC0 medidas (metal, madera, papel, tela); no hay tramas de manga que replicar (la obra no viene de manga) y no encontré pinceles libres de "estilo Ghibli". |
| 23. Colaboraciones y cruces | ✅ | Ghibli Park (dos fuentes), Loewe (cuatro fuentes), figura oficial, ediciones coleccionables, cosplay (dos fuentes); café temático sólo con una fuente débil. |
