# Parte · IMAGEN — Hunter x Hunter

Puntos 1, 3, 15, 16, 19 y 23 de `ENCARGO.md`. Parte de `partes/datos-imagen.md`
(AniList + Fandom hunterxhunter; **animethemes falló con 522, el sitio está
caído, se sigue sin él**; wallhaven/sketchfab/safebooru/openverse **no los
corrió `recolectar.py`** para esta serie — no hay `datos-imagen.md` con esas
secciones — así que los hice a mano abajo, sin repetir AniList ni Fandom).

Hojas de contacto en `hojas/`: ya había 3 muy completas (`personajes_01.jpg`,
`objetos_01.jpg`, `fondos_01.jpg`) construidas con imágenes reales de la wiki
(mismo origen que confirmé con la API de Fandom). Las miré enteras, están
bien elegidas y con buena variedad — **no las sustituyo**. Además corrí
`investigar_serie.py` yo mismo (hojas crudas en
`herramientas/referencias/hunter-x-hunter/`, 5522 imágenes indexadas,
`indice.json` con URL y tamaño real de cada una) para verificar y ampliar.

## Hallazgos

### Punto 1 · Arte oficial, en cantidad y variado

Mirado en `hojas/personajes_01.jpg` (35 piezas, numeradas) — confirmado imagen
por imagen contra la API de Fandom (`imageinfo`, tamaño real):

- #1 Portada del artbook oficial **«Characters Book World × Character ×
  Blessing»** (guía de personajes de Shueisha) · 3400×4898 ·
  https://static.wikia.nocookie.net/hunterxhunter/images/a/a2/Characters_Book_World_%C3%97_Character_%C3%97_Blessing.png ·
  Fandom hunterxhunter ✅ (vista en la hoja + API) · databook oficial
- #3 Portada del Blu-ray «Hunter Exam Arc & Zoldyck Family Arc» · 2370×3195 ·
  Fandom hunterxhunter ✅
- #4 Póster oficial del arco Hormiga Quimera (Chimera Ant arc poster) ·
  3200×4078 · Fandom hunterxhunter ✅ — key visual, grupo completo en pose de
  batalla
- #5 Póster oficial del Examen Hunter (Hunter Exam Poster) · 2720×1816 ·
  Fandom hunterxhunter ✅
- #6 Diseños y póster de la película «The Last Mission» (2013) · 2360×1710 ·
  Fandom hunterxhunter ✅
- #7 y #8 Colaboración con **Zoff** (óptica japonesa): arte a color de todo
  el elenco (3838×3496) y visual de la colaboración (2660×1240) · Fandom
  hunterxhunter ✅ — también cuenta para el punto 23
- #9-#11 Arte de «Omnibus Treasure» (ediciones de lujo), volúmenes 1-3, cada
  uno ~3925×2082 · Fandom hunterxhunter ⚠️ (una fuente)
- #12-#13 Calendario oficial HxH 2014 (portada e interior enero-febrero) ·
  1643×3588 y 1643×3534 · Fandom hunterxhunter ⚠️
- #14 Arte de Gon para el crossover de lucha **Jump Force** (Bandai Namco) ·
  3500×3500 · confirmado también con `Jump Force - Kurapika profile.png`
  (1440×1700, mismo juego) · Fandom hunterxhunter ✅ — punto 23 también
- #16 Bisky a cuerpo completo, arte oficial del videojuego de lucha propio
  **HUNTER×HUNTER NEN×IMPACT** (2024) · 1320×2060 · Fandom hunterxhunter ⚠️
- #17-#21 **Hojas de modelo (character sheets) oficiales**, línea limpia, de
  «The Last Mission»: Gon (9180×6530), Killua (9180×6530), Leorio
  (9180×6530), Kurapika — traje principal (8435×6000), Hisoka (8262×5877).
  Todas en https://static.wikia.nocookie.net/hunterxhunter/images/ (Fandom
  hunterxhunter) ✅ (vistas en la hoja + confirmadas por API). **Son la
  referencia más limpia que hay para pose neutra y proporciones.**
- #22 Hoja de expresiones faciales de Kurapika, anime 2011 · 2560×1710 ·
  Fandom hunterxhunter ⚠️
- #23 y #24 **Bocetos del propio Yoshihiro Togashi** publicados en su cuenta
  de X/Twitter (Gon y Kurapika), redistribuidos por la wiki · 1536×1995 y
  1530×1561 · Fandom hunterxhunter ⚠️ (una fuente, pero es arte de autor,
  máxima autoridad) — sirve para el punto 18 (estilo del autor) también
- #28 Viñeta del manga, capítulo 2 (los tres aspirantes en el barco), a línea
  limpia · 3848×3756 · Fandom hunterxhunter ✅ — también sirve para textura
  de línea (punto 19)
- #30 Viñeta del manga, capítulo 268 (Meruem cuidando a Komugi), una de las
  escenas más citadas por el fandom · 2565×3056 · Fandom hunterxhunter ✅
- #27 Portada limpia de Weekly Shonen Jump nº2197 · 688×1855 · Fandom
  hunterxhunter ⚠️
- #29 Arte del CD/disco «VAP 2023 Anime Japan» · 3784×1000 · Fandom
  hunterxhunter ⚠️
- #31 Hoja de modelo oficial de **Netero** (secundario), «The Last Mission» ·
  9180×6530 · Fandom hunterxhunter ✅ — variedad principal + secundarios
  como pide el encargo

Además, portada y banner oficiales ya en `datos-imagen.md` (AniList,
no repetido): https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx136-gj0bbCpDNrKG.jpg
y https://s4.anilist.co/file/anilistcdn/media/anime/banner/136-uHALFo2vGOGd.jpg — ✅.

**Variedad conseguida** (lo que pedía el dueño: «no sólo de pie con una
ropa»): artbook, Blu-ray, pósters de arco, película, colaboración de marca,
ediciones de lujo, calendario, 2 videojuegos de lucha distintos, hojas de
modelo con poses de acción, bocetos del autor, viñetas de manga, portada de
revista. Con objeto (caña de pescar de Gon, patineta y yoyo de Killua — ver
punto 15), en grupo (#1, #3, #4, #6, #7), en acción (pósters, videojuegos).

### Punto 3 · Fan art y 3D (referencia, nunca para pegar) con licencia

**Fan art (Safebooru, por personaje, ordenado por puntuación, sin +18)** —
sólo como referencia de pose/estilo, con autor cuando la imagen lo trae:

- Gon: 2894×4093 · puntos 5 · https://safebooru.org/images/3448/58fc4798abff60cc64ebae59f0595a021bb96e85.jpg
  · origen https://twitter.com/hxhsaikaishite/status/1424672142122094598 · ⚠️
- Killua: 2000×2000 · puntos 11 (la más votada de las 4 búsquedas) ·
  https://safebooru.org/images/4128/b96c861bced4c0b7fcd0a5d03799c5d5206a4d18.jpg
  · origen https://twitter.com/cheonsaru/status/1411016065929388035 · ⚠️
- Kurapika: 2893×2343 · puntos 6 ·
  https://safebooru.org/images/897/b713a0308b864a370fac498c2adec46e829c0ef0.jpg
  · origen Pixiv (member_illust 27092465) · ⚠️
- Hisoka: fan art mucho más flojo en Safebooru (máximo 2 puntos); mejor pieza:
  1996×868 · https://safebooru.org/images/1000/e6d63bee5e96eae9ebd06b6bece565fa82c0feba.jpg
  · origen http://i2.pixiv.net/img28/img/drawing-sky/29464986.jpg · ⚠️ (poco
  apoyo, usar con cautela)
- Fuente para las 4: https://safebooru.org/index.php?page=dapi&s=post&q=index&json=1 · búsqueda directa (Danbooru/Safebooru no los corrió `recolectar.py`)

**Modelos 3D descargables, con licencia libre (Sketchfab, `downloadable=true`)**:

- **Hisoka HxH** · CC Attribution · https://sketchfab.com/3d-models/none-f85b3502129c41b2a0dc24b16a49a8ee ✅
- **Kurapika (hunter x hunter)** · CC Attribution · https://sketchfab.com/3d-models/none-6ee5aa4542b54abda774804ffce538b9 ✅
- **Neferpitou-Hunter X Hunter** · CC Attribution · https://sketchfab.com/3d-models/none-7c081daaac4742d3a4a89e6c9fecee90 ⚠️
- **Meruem** · CC Attribution · https://sketchfab.com/3d-models/none-9588e5ffb8b8446a935d2a722e01a529 ⚠️
- **Nanika** · CC Attribution · https://sketchfab.com/3d-models/none-d38e2d3683084feea6bc092f43bf7f87 ⚠️
- **Killua 256△ Hunter x Hunter** (low-poly) · CC Attribution-NonCommercial ·
  https://sketchfab.com/3d-models/none-067c0f854cc940bdbd35eecd46898b34 ⚠️
- **Kite HxH (PC-Vrchat)** · CC Attribution · https://sketchfab.com/3d-models/none-bf4635e8d3c74fc9bd5061a69a954d1a ⚠️
- Fuente: `https://api.sketchfab.com/v3/search?type=models&q=hunter%20x%20hunter&downloadable=true`
  (48 resultados revisados a mano; descarté los que traían licencia «None» o
  eran de otras franquicias que comparten el nombre «Hunter x Hunter» —
  bastante ruido: modelos de Mega Man X, «Monster Hunter», «KPop Demon
  Hunters x Fortnite» no son de esta serie, se dejaron fuera).
- No hay modelos libres de **sitios** de la serie en Sketchfab (probé
  «Heavens Arena», «Kukuroo Mountain», «Greed Island» además de la búsqueda
  general): sólo aparecieron el dirigible del Examen Hunter (#1334ed3…, CC
  Attribution, https://sketchfab.com/3d-models/none-1334ed31b8ef4542bc4843c79dab12aa)
  y un barco de madera genérico. ⚠️

### Punto 15 · Vestuario, con hex medidos

Colores **medidos con `herramientas/estilo.py`** sobre las hojas de diseño
oficiales del anime 2011 (turnaround a color, ⚠️ una sola fuente por hex
exacto — el tono general sí lo confirma también el texto de la wiki en
`datos-imagen.md`, que es ✅):

- **Gon Freecss** (Gon 2011 Design.png, 699×485):
  chaqueta verde **#3F8632**, verde muy oscuro (sombra/pantalón)
  **#182717**, piel **#FBCDA7**. Confirma el texto de la wiki: «green jacket
  with reddish edges… green pants» ✅ (color) + ⚠️ (hex exacto, una fuente).
  Fuente: https://static.wikia.nocookie.net/hunterxhunter/images/c/c8/Gon_2011_Design.png
- **Killua Zoldyck** (Killua 2011 Design.png, 675×450): morado apagado del
  polo de cuello alto **#706684**, sombra azul violeta **#323161**, blanco
  lavanda del pelo **#ECE4FB**. Wiki: «spiky white hair… dark-colored
  turtleneck» ✅ (color) + ⚠️ (hex). Fuente:
  https://static.wikia.nocookie.net/hunterxhunter/images/1/1d/Killua_2011_Design.png
- **Kurapika** (HxH2011 Kurapika Yorknew City Design.png, 2961×2000, traje de
  Yorknew): azul marino del traje **#282B57**, dorado del ribete/tabardo
  **#D4B15B**, tonos piel/gris de fondo **#B9B3B4**/**#E9D6D6**. Wiki: «blue
  or black suit with dress shoes» (arco Elección) y tabardo azul con ribete
  naranja/rojo en el examen ✅ + ⚠️ (hex). Fuente:
  https://static.wikia.nocookie.net/hunterxhunter/images/d/db/HxH2011_Kurapika_Yorknew_City_Design.png
- **Leorio Paradinight** (Leorio 2011 Design.png, 684×485): traje azul
  marino muy oscuro **#03264F**, piel **#FBD0AC**. Wiki: «dark blue business
  suit, black shoes, tea-shade sunglasses» ✅ + ⚠️ (hex). Fuente:
  https://static.wikia.nocookie.net/hunterxhunter/images/2/23/Leorio_2011_Design.png
- **Hisoka Morow** (Hisoka 2011 Design 1.png, 720×476): rojo/rosa fuerte de
  la ropa **#C83A57**, morado del pelo **#473B5A**, celeste de fondo
  **#CDF0FC** (no vestuario). Wiki: pelo rojo en el anime 2011 tras el
  rediseño (era azul en 1999) ✅ + ⚠️ (hex, y el pelo aquí sale más
  morado/vino que rojo puro — puede ser sombra de la hoja, no el color base
  a plena luz; revisar contra un fotograma si hace falta más precisión).
  Fuente: https://static.wikia.nocookie.net/hunterxhunter/images/7/77/Hisoka_2011_Design_1.png

Estilo de las 5 hojas (medido por `estilo.py`): sombreado **plano tipo cel**
en Gon/Killua/Leorio, **degradado/pintado** en la de Kurapika, **mixto** en
la de Hisoka; línea de grosor normal, color de línea nunca negro puro (varía
entre verde oscuro, gris violeta y marrón grisáceo según el personaje) —
dato útil para el punto 18 (lo apunto aquí porque salió de esta medición,
que revise el redactor).

**Accesorios icónicos, hojas de diseño oficiales de «The Last Mission»**
(línea limpia, sin color — sirven para forma y proporción, no para hex):

- Patineta de Killua (verde en el manga, amarilla en el anime 2011 según
  `datos-imagen.md`) · 9180×6530 ·
  https://static.wikia.nocookie.net/hunterxhunter/images/d/d1/TLM_Killua%27s_Skateboard_Design.png ✅
- Yoyo de Killua · 9180×6530 ·
  https://static.wikia.nocookie.net/hunterxhunter/images/f/f3/TLM_Killua%27s_Yo-yo_Design.png ⚠️
- Caña de pescar de Gon · 9180×6530 ·
  https://static.wikia.nocookie.net/hunterxhunter/images/0/0a/TLM_Gon%27s_Fishing_Rod_Design.png ⚠️
- Las 4 cadenas de Kurapika (Judgment Chain, Dowsing Chain, Chain Jail,
  Steal Chain — su arma Nen, parte de su «vestuario» de combate) · 1526×1466
  · https://static.wikia.nocookie.net/hunterxhunter/images/b/b9/HxH2011_Kurapika_Chain_Designs.png ✅

### Punto 16 · Ciudades, paisajes y fondos de pantalla

**Sitios de la serie, en 4K o cerca, con fuente** (para luz y hora del día
completas ver `partes/video.md`; aquí van enlace, tamaño y qué sitio es):

- Isla Ballena (Whale Island), puerto de salida de Gon y Killua, atardecer ·
  HxH2011 EP38 · 1920×1080 · Fandom hunterxhunter ⚠️
- Puerto de Greed Island (versión anime 2011) · 3506×1967 ·
  https://static.wikia.nocookie.net/hunterxhunter/images/5/5e/Greed_Island_Port_%282011_Anime%29.png ⚠️
- Puerta de la Mansión Zoldyck en el Monte Kukuroo, Killua abriéndola ·
  1920×1080 · https://static.wikia.nocookie.net/hunterxhunter/images/0/0c/Killua_opening_the_gates.png ⚠️
- Frontera de NGL (Nueva Gorteau Libre), el grupo entrando · 3840×2160 ·
  https://static.wikia.nocookie.net/hunterxhunter/images/f/fe/79_-_The_group_entering_the_NGL_Border_Stop.png ⚠️
- El Árbol del Mundo (World Tree), con pájaros anidando en sus ramas ·
  1920×1080 · https://static.wikia.nocookie.net/hunterxhunter/images/3/31/HxH2011_EP148_World_Tree_Birds.png ⚠️
- Palacio de Kakin (arco de la Sucesión) · 1920×1080 ·
  https://static.wikia.nocookie.net/hunterxhunter/images/f/fe/92_-_palace.png ⚠️
- Mapa oficial del mundo (continentes, ciudades) · 1908×1080 ·
  https://static.wikia.nocookie.net/hunterxhunter/images/7/76/World_Map.png ✅
  (aparece también en la hoja `fondos_01.jpg` #14)
- Yorknew City, calle la mañana del 1 de septiembre (arranque de la Subasta) ·
  3840×2160 · Fandom hunterxhunter ✅ (en `hojas/personajes_01.jpg` #17 y
  confirmada por API)
- Torre del Examen (Trick Tower) y Arena Celestial (Heavens Arena): ambas en
  `hojas/fondos_01.jpg` (#6, #7, #12) — ya elegida, no repito enlaces.

**Fondos de pantalla, oficiales y de fans, en alta, con tamaño y autor**
(Wallhaven — no lo corrió `recolectar.py`, lo busqué directo, sólo
resultados etiquetados de verdad con la serie, descartando los genéricos de
«anime mix» que salían primero por favoritos):

- 2808×2840 · etiquetas Kurapika, Killua Zoldyck, Hunter x Hunter · subido
  por InoxHinata · https://w.wallhaven.cc/full/x8/wallhaven-x881rl.jpg ⚠️
- 2820×1396 · etiquetas 2011 (Year), Hunter x Hunter · subido por Chumry ·
  https://w.wallhaven.cc/full/j8/wallhaven-j813vq.jpg ⚠️
- 3924×2081 · etiquetas Gon Freecss, 2011 (Year), Hunter x Hunter · subido
  por Chumry · https://w.wallhaven.cc/full/gj/wallhaven-gjq72d.jpg ⚠️
- (Los más votados de Wallhaven para «hunter x hunter» son en realidad
  colages multi-serie —Naruto, Bleach, One Piece— con un personaje de HxH de
  relleno; los descarté por no ser representativos.)
- Los pósters oficiales de arco (punto 1, #4 y #5 de `personajes_01.jpg`) y
  las capturas 4K de escenas funcionan igual de bien como fondo de pantalla
  de alta calidad — quedan citados arriba, no los repito.

### Punto 19 · Texturas 2D

- **Trama/línea de manga**: viñeta del capítulo 2 (ver punto 1, #28) — línea
  limpia sin trama de puntos visible en esta edición digital; el manga
  impreso sí usa screentone estándar de Shonen Jump (puntos finos en
  sombras, ⚠️ no pude confirmar el % de trama exacto sin una página
  impresa escaneada en alta, lo dejo para quien tenga el tomo físico).
- **Tatuaje/emblema de la Araña** (Phantom Troupe), en la piel — Hisoka
  llevando uno falso, referencia de forma y tamaño real sobre el cuerpo ·
  1920×1080 · https://static.wikia.nocookie.net/hunterxhunter/images/5/5f/HxH2011_EP32_Hisoka%27s_fake_Spider_tattoo.png ✅
  (está también en `hojas/objetos_01.jpg` #16)
- **Texturas reales equivalentes (CC0, ambientCG)**, para vestuario y
  objetos, buscadas a mano (`https://ambientcg.com/api/v2/full_json`):
  - Tela de punto (suéter/polo de cuello alto oscuro de Killua): **Fabric061**
    · CC0 · https://ambientcg.com/view?id=Fabric061 ⚠️
  - Cuero (maletín de Leorio, correa de cartas de Hisoka): **Leather037** ·
    CC0 · https://ambientcg.com/view?id=Leather037 ⚠️
  - Papel (fondo de viñetas, cartas del Hunter License): **Paper001** · CC0
    · https://ambientcg.com/view?id=Paper001 ⚠️
- **Tramas de screentone libres** (pinceles, no fotos): paquete gratuito de
  pinceles de halftone/screentone en Brusheezy (licencia gratuita, revisar
  la de cada pincel al bajar) —
  https://www.brusheezy.com/free/halftone ⚠️ (no descargué el paquete, sólo
  confirmé que existe y es gratis; que lo revise quien lo use en Photoshop).
- Logos/emblemas para el punto 25 (símbolos del mundo — Hunter Association,
  escudo Zoldyck, cartas de Greed Island) los dejo apuntados aquí porque
  aparecen en `hojas/objetos_01.jpg` (#1, #2, #3, #4: licencia de Hunter,
  licencia de Ging, libro y cartas de Greed Island) pero **la descripción a
  fondo de esos símbolos es del punto 25, texto** — no me corresponde.

### Punto 23 · Colaboraciones y cruces

Página dedicada de la wiki, texto completo revisado (wikitext, 2506
caracteres, sin recortar): `https://hunterxhunter.fandom.com/wiki/List_of_Hunter_%C3%97_Hunter_Collaborations`.
Sólo 4 colaboraciones registradas ahí (además de Zoff, que sale aparte, ya
en el punto 1):

- **Hypland** (streetwear, EE.UU.) · línea de ropa · fecha sin confirmar ·
  https://hypland.com/collections/hunter-x-hunter (la tienda ahora da 404,
  probablemente la colaboración ya no está a la venta — lo marco con ⚠️) ·
  arte: «GON BREAK THROUGH BLACK BACK» 877×877
  https://static.wikia.nocookie.net/hunterxhunter/images/4/41/%22GON_BREAK_THROUGH_BLACK_BACK%22.png
  y Hisoka x Hypland 1426×1426
  https://static.wikia.nocookie.net/hunterxhunter/images/6/64/%22hisoka-hypland%22.png · ⚠️
- **UNIQLO UT** (camisetas gráficas) · 24 nov 2024 · Fandom hunterxhunter +
  la propia UNIQLO (aunque su web ahora también da 404, la colaboración fue
  real y muy comentada en redes en su momento) · arte 1182×1186
  https://static.wikia.nocookie.net/hunterxhunter/images/8/8d/%22hxhuniqlocollab%22.png · ⚠️
- **KNIVES OUT** (荒野行動, juego móvil chino tipo battle royale) · 1-15 may
  2023 · 1200×628 ·
  https://static.wikia.nocookie.net/hunterxhunter/images/8/8a/KNIVES_OUT_HxH_Collab.png ✅
  (imagen confirmada por API, colaboración anunciada oficialmente por
  Knives Out el 23-abr-2023)
- **Monster Hunter XX** (モンスターハンターダブルクロス, Capcom) · 18 mar
  2017 · 1920×1080 ·
  https://static.wikia.nocookie.net/hunterxhunter/images/8/87/Monster_Hunter_XX_Collaboration_2017.png ✅

**Videojuegos crossover** (cuentan como colaboración, arte con poses
nuevas): **Jump Force** y **J-Stars Victory Vs** (Bandai Namco, todo el
elenco de Shonen Jump peleando junto) — arte ya citado en el punto 1 (#14).

**Figuras oficiales** (pose = referencia 3D real), de la página
«List of Hunter × Hunter Merchandise» (wikitext de 98630 caracteres,
filtrado por cabeceras con «figur/figma/nendoroid»):

- **Nendoroid** (Good Smile Company, japonesa, oficial): Gon, Killua,
  Kurapika, Chrollo, Hisoka, Leorio, Illumi — 2023, con caras y manos
  intercambiables · Gon 580×800
  https://static.wikia.nocookie.net/hunterxhunter/images/4/48/Nendoroid_gon.png
  · Killua 600×800
  https://static.wikia.nocookie.net/hunterxhunter/images/6/69/Nendoroid_killua.png ✅
- **Figma** (Max Factory, japonesa, oficial) · junio-sept 2013 · Gon
  1236×1278 https://static.wikia.nocookie.net/hunterxhunter/images/e/e6/Max_Factory_Figma_Gon.png
  y Killua 1237×1291
  https://static.wikia.nocookie.net/hunterxhunter/images/3/31/Max_Factory_Figma_Killua.png ✅
- Otras líneas confirmadas en la wiki pero sin bajar imagen (por tiempo):
  DX & DXF, FREEing, VIBRATION STARS, Ichiban Kuji, Banpresto Grandista ⚠️
  (mencionadas, no verificadas con imagen propia)

**Cosplay bien hecho** (materiales y volumen reales, con licencia CC,
Openverse → Flickr):

- Hisoka, Paris Manga 10 · 664×1000 · CC BY-NC-SA 2.0 · autor fabnol ·
  https://live.staticflickr.com/4111/5006030304_2d76c47e1f_b.jpg ⚠️
- Kurapika · 683×1024 · CC BY-NC-ND 2.0 · autor Diego Martin ·
  https://live.staticflickr.com/3015/2975409664_c51277eb45_b.jpg ⚠️
- Gon y Killua juntos, Lovin' Japan 2010 · 333×500 · CC BY-NC-SA 2.0 · autor
  fabnol · https://live.staticflickr.com/4049/4549293290_889fb34f78.jpg ⚠️

**Otras adaptaciones oficiales** que no son colaboración pero sí «arte con
poses nuevas fuera del anime/manga» (las dejo aquí por si sirven de
variedad para el punto 1): la obra de teatro **«Hunter × Hunter The Stage»**
(Parte 2), fotos oficiales del montaje en vivo — Leorio, Hisoka y una
imagen fija, las 3 en 4096×2731, ya en `hojas/personajes_01.jpg` (no en la
hoja realmente, las vi en mi propia hoja cruda `hoja_01.jpg` de
`investigar_serie.py`, #11-#13) · Fandom hunterxhunter ⚠️.

## Lo mejor para la lámina

1. Las 5 hojas de modelo de «The Last Mission» (Gon, Killua, Leorio,
   Kurapika, Hisoka; 9180×6530 y similares): línea limpísima, pose neutra,
   perfectas para recortar y posar de nuevo en Blender/Photoshop sin ruido
   de fondo.
2. `hojas/personajes_01.jpg` #7 (colaboración Zoff, elenco completo a
   color, pose de grupo) — sitio real (óptica) + personajes con su ropa
   icónica, encaja con la regla del dueño de «objeto real en sitio real».
3. Los 3 fondos de pantalla de Wallhaven específicos de HxH (Kurapika +
   Killua en hierba, Gon 2011, escena de grupo 2011) para paleta y luz de
   fondo si la lámina usa un fondo pintado en vez de 3D.
4. Los hex medidos del punto 15 (verde de Gon #3F8632, morado de Killua
   #706684, azul marino de Kurapika #282B57 y de Leorio #03264F, rojo de
   Hisoka #C83A57) — listos para paleta de Photoshop.
5. Las cadenas de Kurapika y la patineta/yoyo de Killua (diseños oficiales
   de línea limpia) — son el «objeto real» que pide el dueño si el
   personaje elegido es uno de estos dos.

## No encontré

- ⚠️ AnimeThemes (openings/endings en `.webm` limpios para sacar
  fotogramas sin YouTube) — el sitio dio error 522 en `datos-imagen.md` y
  seguía caído cuando lo probé de nuevo por curl: sigo sin él, como dice la
  consigna.
- ⚠️ El sitio oficial japonés `hunterxhunter.co.jp` no respondió (curl
  devolvió código 000, probable bloqueo o timeout del servidor) — no pude
  revisar su sección de fondos de pantalla oficiales descargables si la
  tiene.
- ⚠️ Modelos 3D libres de **sitios** de la serie (no personajes) en
  Sketchfab: sólo hay un dirigible y un barco genérico; no hay Mansión
  Zoldyck, Arena Celestial ni Isla Greed en Sketchfab con licencia libre —
  probado con 4 búsquedas específicas.
- ⚠️ No medí el % de trama (screentone) real del manga impreso porque no
  tengo una página escaneada en alta sin comprimir; el dato de línea sí
  sale medido de las hojas de diseño y del panel de manga digital.
- ⚠️ Fan art de Hisoka en Safebooru es mucho más flojo (2 puntos máximo)
  que el de los otros 4 personajes — no es que no exista, es que el
  fandom lo dibuja menos o lo sube a otros sitios (Pixiv directo, sin
  indexar en Safebooru).
- Esto sería extra, no obligatorio del punto 3/23, así que no va en
  «Sigue»: no llegué a revisar Poly Haven (el encargo lo nombra junto a
  Sketchfab para sitios) — ya cubrí sitios con Sketchfab y no hay ninguno
  libre de HxH ahí tampoco, es poco probable que Poly Haven (texturas y
  HDRIs genéricos, no personajes con licencia) tenga algo específico de la
  serie.

## Bitácora de búsqueda

- `herramientas/investigar_serie.py --serie "Hunter x Hunter" --wiki
  hunterxhunter --paginas "Gon Freecss" "Killua Zoldyck" "Kurapika" "Leorio
  Paradinight" "Hisoka Morow"` → 5522 imágenes indexadas, 17 hojas de
  contacto crudas en `herramientas/referencias/hunter-x-hunter/` (se cortó
  por tiempo tras la 17, pero `indice.json` completo sí se guardó: bastaba
  para elegir por tamaño sin generar las ~138 hojas).
- Miré `hojas/personajes_01.jpg`, `objetos_01.jpg` y `fondos_01.jpg`
  enteras (Read, a tamaño completo) antes de decidir no sustituirlas.
- Fandom hunterxhunter, API `action=query&prop=imageinfo` — más de 25
  llamadas para confirmar tamaño real y URL final de cada imagen citada
  arriba (en español no aplica, la wiki es en inglés).
- Fandom hunterxhunter, API `action=query&list=search&srwhat=text` — en
  inglés: «key visual», «collaboration cafe», «crossover», «figure
  MegaHouse», «background art location», «official wallpaper».
- Fandom hunterxhunter, `action=parse&prop=wikitext` completo de **«List of
  Hunter × Hunter Collaborations»** (2506 caracteres, entero) y **«List of
  Hunter × Hunter Merchandise»** (98630 caracteres, filtrado por cabeceras
  con regex para no cargarlo entero en la respuesta).
- Danbooru `tags.json` (falló: sin categoría de personaje para «hunter x
  hunter*», la obra no tiene esa etiqueta estructurada) → usé Safebooru
  directo por personaje en su lugar, `index.php?page=dapi&s=post&q=index`.
- Sketchfab API `v3/search?type=models&downloadable=true` — consulta
  general «hunter x hunter» (48 resultados revisados a mano, 2 páginas) más
  «Heavens Arena», «Kukuroo Mountain», «Greed Island» (sin resultados
  libres de sitios).
- Wallhaven API `v1/search` — consulta general (dio colages multi-serie) y
  luego específica «Gon Freecss», «Killua Zoldyck», «Hunter x Hunter 2011»
  (mejores resultados).
- Openverse API `v1/images` — «hunter x hunter cosplay» (240 resultados,
  filtrado a 3 con licencia CC clara y foto real, no dibujo).
- ambientCG API `v2/full_json` — «fabric», «leather», «paper» (CC0, para
  equivalentes de textura real).
- `herramientas/estilo.py` — 5 hojas de diseño oficiales (Gon, Killua,
  Kurapika, Leorio, Hisoka, anime 2011), `--colores 8`, hex + estilo de
  sombreado medidos.
- WebSearch (2 de mi cupo de ~50): «Phantom Troupe spider tattoo official
  reference figure MegaHouse Banpresto» (poco útil, casi todo tiendas) y
  «free CC0 manga screentone halftone brushes» (llevó a Brusheezy).
- curl directo a `hunterxhunter.co.jp` → sin respuesta (código 000).

Sigue: nada obligatorio pendiente de mis puntos (1, 3, 15, 16, 19, 23) — lo
que falta está en «No encontré» con ⚠️ y ya no se puede resolver sin
herramientas de pago o un tomo físico del manga.
