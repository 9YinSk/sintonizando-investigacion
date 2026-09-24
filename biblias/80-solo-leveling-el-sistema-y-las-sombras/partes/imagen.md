# Investigador de imagen · Solo Leveling: el Sistema y las sombras (puntos 1, 3, 15, 16, 19, 23)

Ángulo propio del encargo 80: **el Sistema** (ventanas, mensajes, interfaz de
juego) y **las sombras** (el ejército de Jinwoo), no un repaso general de la
serie. Ya existe `biblias/03-solo-leveling/` (repaso general, con su propio
`partes/imagen.md`): la miré para no repetir lo básico de vestuario humano de
Jinwoo/Cha Hae-in ni los emblemas de gremios, pero **todo lo de aquí es
investigación propia**, con sus propias fuentes y medidas. Parto de
`partes/datos-imagen.md` (ya recolectado, no repito esas consultas: AniList,
galerías grandes de Jinwoo/Igris/Beru de la wiki, Danbooru/Safebooru,
`herramientas/referencias/solo-leveling-el-sistema-y-las-sombras/` con 10
hojas de contacto de 476 imágenes de la wiki).

## Hallazgos · Punto 1 — Arte oficial variado (el Sistema y el ejército)

**El Sistema: las dos interfaces oficiales (webtoon vs. anime), miradas de verdad**
- El webtoon (Chugong/DUBU) dibuja las ventanas del Sistema como **paneles
  traslúcidos ámbar-dorado sobre fondo azul noche**, con texto en mayúsculas:
  `STATUS`, `[ITEM]`, notificaciones de misión. Vistas en el capítulo con
  lluvia donde Jinwoo llega a nivel 61 · 717×1028 · `File:System1.jpg` ·
  https://static.wikia.nocookie.net/solo-leveling/images/9/95/System1.jpg/revision/latest?cb=20210625162338
  · medida con Pillow (API `imageinfo`) · **la miré**: el marco de la ventana
  «STATUS» tiene texto ámbar apagado por la lluvia, medido con Pillow en
  `#93825A` (más un ámbar puro en escenas sin lluvia, ver Punto 19) · ✅ vista
  directa + página `System/Gallery` de la wiki (21 imágenes) · fuente:
  [System/Gallery](https://solo-leveling.fandom.com/wiki/System/Gallery).
- El **inventario** del webtoon es una **rejilla** con líneas finas ámbar
  (`#A29B39` medido) sobre panel gris-azulado (`#2B3136`), pestañas `ALL /
  EQUIPMENT / CONSUMABLES / MATERIALS / QUESTS`, iconos de objetos en
  siluetas blancas (hueso, poción, daga) · 718×716 · `File:SystemInventory1.jpg`
  · https://static.wikia.nocookie.net/solo-leveling/images/0/01/SystemInventory1.jpg/revision/latest?cb=20210625162158
  · medida con Pillow · **la miré**: hoja `hojas/sistema_01.jpg` #3.
- En la misma viñeta (`File:Shop.jpg`, 718×630,
  https://static.wikia.nocookie.net/solo-leveling/images/3/3b/Shop.jpg/revision/latest?cb=20240402141811)
  se ve el contraste clave para el redactor: el diálogo normal de Jinwoo
  («SHOP.») va en una **burbuja blanca ovalada normal** con texto negro; la
  ventana del Sistema detrás es el panel azul con líneas cian. Es decir: **la
  burbuja blanca es del habla humana, no del Sistema** — el Sistema nunca usa
  la burbuja blanca genérica que el dueño rechaza. Onomatopeya «DING» en azul
  con borde blanco · hoja `hojas/sistema_01.jpg` #4 · ✅ vista directa,
  confirma lo mismo en `SystemInventory1.jpg` (onomatopeya «SHWWP» en blanco
  con borde negro).
- El **anime** (A-1 Pictures, temporada 2) **rediseñó** la interfaz: ya no es
  ámbar/webtoon, es un **holograma neón violeta** con líneas de circuito,
  fondo casi negro-violeta (`#0E1732` medido), marco `#8C1BF8` (violeta
  saturado, el color que más se repite), texto blanco-azulado y números en
  verde para las estadísticas (STR, AGI, VIT, INT, PER) · 815×483 ·
  `File:Anime System.png` ·
  https://static.wikia.nocookie.net/solo-leveling/images/c/ce/Anime_System.png/revision/latest?cb=20250401121047
  · medida con Pillow · **la miré**: hoja `hojas/sistema_01.jpg` #2. Esta
  ventana concreta es la de Jinwoo ya convertido en «Shadow Monarch», nivel
  100 · fuente: página [System](https://solo-leveling.fandom.com/wiki/System)
  (infobox, pestaña «Anime») · ✅ dos fuentes (imagen + wikitext de la
  página).
- Ventana de misión con lluvia y toda la pantalla cubierta de paneles (7
  ventanas flotando alrededor de Jinwoo de espaldas) · 1080×1920 aprox (es la
  misma `System1.jpg` en su versión completa, ya medida arriba) · ✅.
- Momento en que Jinwoo **recibe su primera misión** del Sistema (Ep. 3) ·
  1196×649 · `File:Anime Episode 3 Jinwoo receives a quest from the System.png`
  ·
  https://static.wikia.nocookie.net/solo-leveling/images/b/b3/Anime_Episode_3_Jinwoo_receives_a_quest_from_the_System.png/revision/latest?cb=20240113194819
  · medida con Pillow · hoja de contacto genérica
  `herramientas/referencias/solo-leveling-el-sistema-y-las-sombras/hoja_09.jpg`
  #424 · ✅.
- Notificaciones de «caja bendita»/«caja maldita» (recompensas aleatorias del
  Sistema), formato horizontal de banner: 858×286 y 852×286 ·
  `File:Blessed random box.png` y `File:Cursed random box.png` ·
  https://static.wikia.nocookie.net/solo-leveling/images/a/a9/Blessed_random_box.png/revision/latest?cb=20250607144036
  y
  https://static.wikia.nocookie.net/solo-leveling/images/d/d8/Cursed_random_box.png/revision/latest?cb=20250607144020
  · medidas con Pillow · fuente: `System/Gallery` · ✅.

**El ejército de sombras: arte oficial de grupo, no sólo Igris/Beru sueltos**
- **Render oficial del ejército** (usado por la propia wiki como imagen
  «Anime» de la página `Shadows`): Igris al frente con su capa roja, docenas
  de soldados sombra detrás en azul-cian sobre humo negro, fondo blanco ·
  905×520 · `File:Shadow Army Render.png` ·
  https://static.wikia.nocookie.net/solo-leveling/images/c/c6/Shadow_Army_Render.png/revision/latest?cb=20250121154640
  · medida con Pillow · **la miré**: hoja `hojas/sombras_02.jpg` #1 · fuente:
  [Shadows (wiki, pestaña Anime)](https://solo-leveling.fandom.com/wiki/Shadows)
  · ✅.
- **Formación completa del ejército, versión webtoon**, panorámica muy ancha
  (línea de soldados en fila, útil de referencia para una composición
  horizontal) · 4438×889 · `File:Shadows1.jpg` ·
  https://static.wikia.nocookie.net/solo-leveling/images/b/bb/Shadows1.jpg/revision/latest?cb=20211015041406
  · medida con Pillow · fuente: página
  [Shadows](https://solo-leveling.fandom.com/wiki/Shadows) · ⚠️ una sola
  fuente (no la abrí en grande, la wiki es la única que la aloja).
- **Key visual oficial de Beru** para la temporada 2 («BERU · SOLO LEVELING
  SS2 -ARISE FROM THE SHADOW-»): silueta de armadura negra con grietas
  cian brillantes, fondo violeta-morado, tipografía elegante del título ·
  906×1280 · `File:Beru CV.jpg` ·
  https://static.wikia.nocookie.net/solo-leveling/images/8/86/Beru_CV.jpg/revision/latest?cb=20211201000000
  · medida con Pillow · **la miré a fondo**: hoja `hojas/sombras_02.jpg` #2 ·
  colores medidos: armadura `#020206`, grieta cian `#2CC6F2` · ✅ (imagen +
  la propia rotulación «SS2» del cartel la fecha como material promocional
  oficial de temporada).
- **Igris, arte oficial de cuerpo entero**, el más grande de toda la colecta:
  2880×5184 y 2880×5124 · `File:Igris 2.jpg` / `File:Igris 1.jpg` ·
  https://static.wikia.nocookie.net/solo-leveling/images/a/a9/Igris_2.jpg/revision/latest?cb=20260602102136
  y
  https://static.wikia.nocookie.net/solo-leveling/images/6/6d/Igris_1.jpg/revision/latest?cb=20260602101853
  · medidas con Pillow · **la miré a fondo** (recorte del filo de la espada y
  el casco): hoja `hojas/sombras_02.jpg` #3 · colores: armadura `#1D1B34`,
  grieta lila `#9E7EFF`, cinta de la capa `#901A32` · ✅ (imagen + página
  [Igris](https://solo-leveling.fandom.com/wiki/Igris), 25 imágenes propias).
- **Beru, anime**, forma de ángel/insecto con alas de energía blanco-cian,
  cueva azul de fondo · 1920×1080 · `File:Beru Anime1.png` ·
  https://static.wikia.nocookie.net/solo-leveling/images/f/fe/Beru_Anime1.png/revision/latest?cb=20250330071152
  · medida con Pillow · **la miré**: hoja `hojas/sombras_02.jpg` #4 ·
  colores: cuerpo `#1B3477`, brillo del ala `#E6FCFE` · ✅.
- **Arte oficial de Jinwoo con un soldado sombra en escena cotidiana** (no de
  batalla): ilustración firmada, Jinwoo sentado con «Tank» (el oso sombra) ·
  2000×2246 · fuente: publicada por la cuenta oficial coreana de noticias del
  webtoon
  [@SoloLevelingDNC](https://twitter.com/SoloLevelingDNC/status/1874289453054705806),
  indexada en Safebooru con la etiqueta `official_art` ·
  https://safebooru.org/images/4366/ee80f9382a9bc1c02c6558436508e0309201b168.jpg
  · medida con Pillow · ⚠️ una sola fuente directa (la cuenta que la publicó
  no es 100% oficial de la editorial, aunque el tag `official_art` y el
  estilo coinciden con el arte de DUBU); lo marco como probable arte
  promocional, no confirmado al 100%.
- **Origen de las sombras**: Ashborn, el Monarca de las Sombras original
  (antecesor de Jinwoo en el poder), en una imagen de la wiki de silueta azul
  con cuernos · 720×1084 · `File:Ashborn5.jpg` · fuente: hoja de contacto
  genérica `hoja_09.jpg` #423 (`herramientas/referencias/...`) · ⚠️ vista en
  miniatura dentro de la hoja de contacto, no la abrí a tamaño completo (no
  es tan central a mis 3 personajes de partida).
- **Portada y banner oficiales de AniList** (ya en `datos-imagen.md`, los
  cito porque son la referencia de marca más neutra):
  https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx151807-it355ZgzquUd.png
  y
  https://s4.anilist.co/file/anilistcdn/media/anime/banner/151807-37yfQA3ym8PA.jpg
  · fuente: [AniList #151807](https://anilist.co/anime/151807) · ✅.
- **Cartel oficial de difusión, temporada 1 cour 1** (japonés): Jinwoo cruza
  dos dagas, sudadera gris, fondo azul noche con el logo brillante · 1440×2460
  · `File:Sung Jinwoo Anime Season 1 Cour 1 Design.webp` ·
  https://static.wikia.nocookie.net/solo-leveling/images/6/6a/Sung_Jinwoo_Anime_Season_1_Cour_1_Design.webp/revision/latest?cb=20240310191123
  · medida con Pillow · **la miré a fondo**: hoja `hojas/vestuario_03.jpg` #1
  · ✅ (imagen + texto japonés de emisión «TOKYO MX» visible en la propia
  imagen, verificable).

## Hallazgos · Punto 3 — Fan art y 3D con licencia (referencia, no para calcar)

**Fan art del ejército de sombras en grupo (más allá de Igris/Beru sueltos,
que ya trae `datos-imagen.md`)**
- Ilustración de fans con Jinwoo y **6+ soldados sombra distintos** a la vez
  (oso/Tank, dragón, armadura con cuernos) · 1200×1600 · autor/origen:
  [twitter.com/itsk_istk](https://twitter.com/itsk_istk/status/1906008217639162183)
  · https://safebooru.org/images/29/d57d052c5c9091d82bb8e10f36ae66c7ff25dd29.jpg
  · medida con Pillow (vía API de Safebooru) · ✅ (imagen + tags
  `beru_(solo_leveling)`, `tank_(solo_leveling)`, `iron_(solo_leveling)` que
  coinciden en Safebooru).
- **Animación pixel-art** del ejército marchando (hacha, oso, armadura
  completa, fuego azul), formato GIF · 1565×674 · autor: **SteelJoe**
  (DeviantArt) · fuente:
  https://safebooru.org/images/568/dcb5dad7693805af9437349b070cbab78397d5e2.gif
  (alojada originalmente en DeviantArt/Wixmp) · medida con Pillow · ⚠️ una
  fuente (no abrí la página de DeviantArt del autor directamente, sólo el
  espejo de Safebooru) — interesa como referencia de **técnica alternativa**
  (pixel art), no como estilo a copiar.
- Danbooru/Safebooru confirma que sí hay tags propios para soldados sombra
  «menores» además de Igris/Beru: `kaisel_(solo_leveling)` (dragón volador),
  `tank_(solo_leveling)` (oso), `iron_(solo_leveling)` (armadura con hacha) ·
  comprobado con `index.php?page=dapi&s=post&q=index&tags=<tag>&json=1` · ✅.

**Modelos 3D con licencia libre (Sketchfab)**
- **«SOLO LEVELING HOLOGRAM»**: modelo 3D del **panel del Sistema como
  holograma**, descripción del propio autor «jinwoo system. works on cycle, a
  hologram v1» — es decir, un fan reconstruyó la ventana del Sistema en 3D,
  exactamente el objeto de mi ángulo · licencia **CC Attribution** (uso
  comercial permitido, crédito obligatorio) · autor: HERO_MEGA_4 · 4038 caras
  · https://sketchfab.com/3d-models/solo-leveling-hologram-9d15f77f6e2941d08bc9dd7a1ecf3e73
  · ✅ (ficha de la API de Sketchfab, licencia y descripción verificadas).
- **«Shadow Knight Solo Leveling»**: soldado sombra genérico tipo caballero,
  licencia **CC Attribution**, autor nea22906 ·
  https://sketchfab.com/3d-models/shadow-knight-solo-leveling-4f09d63a0ffd455b893b875bc8106620
  · ✅ licencia verificada por API.
- **Igris, varios modelos** en Sketchfab, todos **CC Attribution**: por
  ejemplo `Igris - Solo Leveling` (autor shrithik) y `Igris Solo Leveling`
  (autor missafe) ·
  https://sketchfab.com/3d-models/igris-solo-leveling-98c049a047da440b80a45f29f574dc09
  y
  https://sketchfab.com/3d-models/igris-solo-leveling-0eeb4795c56d4a5cbca69ba2bd340c6a
  · ⚠️ el primero dice explícitamente en su descripción «Ai Gen» (generado
  con IA): sirve como referencia de silueta/pose, **no** como referencia
  fiel de diseño — se lo marco así al redactor para que no lo use como
  fuente de forma.
- **«Sung Jinwoo»** (Meshy, generado con IA), CC Attribution, autor
  pgmugo1998 · ⚠️ mismo aviso: es IA, sólo como pose de referencia, no como
  diseño fiel · https://sketchfab.com/3d-models/sung-jinwoo-4391ce6201aa440c8da94e552f7b58c4.
- No encontré modelos de **Beru**, **Tank**, **Kaisel** ni **Iron** en
  Sketchfab con esos nombres exactos (búsquedas «Beru Solo Leveling», «Tank
  Solo Leveling», «Kaisel Solo Leveling»): sólo salieron resultados no
  relacionados. Ver «No encontré».

## Hallazgos · Punto 15 — Vestuario con hex medidos

**Sung Jinwoo — dos looks civiles oficiales (turnarounds, colores planos)**
- **Traje «Player» oficial** (turnaround de cuerpo entero, fondo
  transparente, el más fiable para medir color plano): cazadora azul-gris
  claro `#86A3C5` (sombra `#7697BC`), camiseta oscura debajo `#302A43`,
  pantalón azul grisáceo `#4E5476`, piel `#F4D1AD`, zapatillas verde oscuro
  `#2C413C` · 443×1594 · `File:Sung Jinwoo (Player) Anime.png` ·
  https://static.wikia.nocookie.net/solo-leveling/images/b/b9/Sung_Jinwoo_%28Player%29_Anime.png/revision/latest?cb=20250316023421
  · medida con Pillow (muestreo de píxeles en zonas planas) · ✅.
- **Look «Cour 1»** (cartel de difusión, con sudadera con capucha gris, no
  azul): sudadera gris-azulada clara `#9AADBB` (sombra media `#565F70`),
  pantalón/prenda oscura casi negra-azulada `#26273B`, piel `#F3D7B3`, pelo
  casi negro `#161621` · 1440×2460 · misma imagen citada en el punto 1
  (`Sung_Jinwoo_Anime_Season_1_Cour_1_Design.webp`) · medida con Pillow
  (colores dominantes de un recorte del personaje, sin fondo) · ✅. **Nota
  para vestuario**: el traje «Player» (azul) y el traje «Cour 1» (gris) NO
  son la misma prenda exacta — la wiki (`datos-imagen.md`, sección
  Appearance) describe que antes de ser elegido por el Sistema Jinwoo era
  «más delgado, pelo largo y desordenado»; estos dos looks corresponden a su
  etapa temprana como cazador de rango E, con ropa de calle, **no** al traje
  negro/gabardina larga que usa después de subir de nivel (ese lo cubre en
  detalle `03-solo-leveling/partes/imagen.md`, no lo repito aquí).

**Soldados sombra — armadura y brillo característico (mi aporte propio: la
otra biblia no midió esto)**
- **Igris**: armadura negra base `#1D1B34` (casi negro con tinte azul),
  grietas/luces de energía en **lila brillante** `#9E7EFF`, adorno/cinta de
  la capa en **rojo sangre** `#901A32` · medido en `Igris_2.jpg` (2880×5184,
  citada arriba) con muestreo de píxeles filtrado por tono (HSV) para no caer
  en el humo gris de fondo · ✅.
- **Beru**: armadura casi negro puro `#020206`, grietas de energía en
  **cian eléctrico** `#2CC6F2` · medido en `Beru_CV.jpg` (906×1280, key
  visual oficial SS2 citada arriba) · ✅. En la versión anime «insecto/ángel»
  (`Beru_Anime1.png`) el cuerpo es más azul medio `#1B3477` con brillo casi
  blanco `#E6FCFE` en las alas — son dos representaciones distintas del
  mismo personaje (silueta de armadura vs. forma de combate con alas), lo
  anoto para que el redactor no las mezcle como si fueran el mismo diseño.
- **Patrón que se repite en todos los soldados sombra**: armadura de base casi
  negra + un solo color de acento brillante por «grieta» de energía (varía
  por personaje: lila en Igris, cian en Beru) — es el dato de vestuario más
  útil para una guía de IA de imagen coherente con **cualquier** soldado
  sombra nuevo que se quiera dibujar.

## Hallazgos · Punto 16 — Fondos de pantalla oficiales y de fans en alta

- **Wallpaper de fans de Igris**, 3840×2160, **105 favoritos** (el más
  guardado de toda la búsqueda «igris» en Wallhaven), tags `Solo Leveling,
  Igris, webtoon, anime`, subido por **csutka** · purity SFW ·
  https://wallhaven.cc/w/1kdglv · comprobado tamaño y autor por la API de
  Wallhaven · ✅.
- **Wallpaper de fans de Igris** (de cuerpo entero, con espada), 2048×1177,
  98 favoritos, tags `Solo Leveling, Igris, knight, swordsman, shadow, scars,
  longsword, armor`, subido por **DaikoOfc** ·
  https://wallhaven.cc/w/x6qqmv · ✅ (API de Wallhaven).
- **Wallpaper general más guardado de la serie**, 1920×1080, **175
  favoritos** (el número más alto de toda la búsqueda «solo leveling» en
  Wallhaven), tags `glowing eyes, anime boys, looking at viewer, Solo
  Leveling, hunter`, subido por **MaiSakurajima** ·
  https://wallhaven.cc/w/96pzzd · ✅.
- Busqué específicamente wallpapers de **sitios/dungeons** («solo leveling
  gate», «solo leveling dungeon», «solo leveling scenery») y no aparecieron
  resultados en Wallhaven con esas palabras exactas: lo que hay son
  wallpapers de personajes, no de escenarios vacíos. La luz y paleta de los
  sitios (Cartenon Temple, Jeju Island) la mide el equipo de vídeo con
  fotogramas propios (punto 4, no es mío); aquí sólo dejo constancia de que
  busqué y no encontré wallpapers de fans centrados en el escenario en sí.
- Nota: las ventanas del Sistema (punto 1) casi siempre aparecen sobre un
  **fondo de lluvia nocturna** (la escena de nivel 61) o sobre **negro puro**
  (el rediseño del anime): ese contraste (cielo tormentoso vs. vacío total)
  es el dato de «fondo» más específico de mi ángulo, más que un paisaje
  turístico de la serie.
- Busqué un **wallpaper oficial descargable** (de la web oficial del anime o
  de A-1 Pictures/Crunchyroll) con `WebSearch` («Solo Leveling anime official
  wallpaper download») y no encontré una página oficial de descargas de
  fondos de pantalla: sólo aparecen agregadores de terceros (WallpaperBat,
  Wallpapers.com, 4kwallpapers.com, WallpaperCave, WallpaperAccess), que no
  son la fuente original. En su lugar, uso como «oficiales en alta» los key
  visuals y carteles ya citados en el Punto 1 (`Beru_CV.jpg` 906×1280,
  `System1.jpg`/`Anime System.png`, el cartel Cour 1 1440×2460): son arte
  promocional real de la editorial/estudio, con la resolución suficiente
  para funcionar como fondo de pantalla, aunque no estén etiquetados
  «wallpaper» en su origen.

## Hallazgos · Punto 19 — Texturas 2D (el Sistema y las sombras)

**Cómo está hecha la interfaz, para buscarle equivalente**
- Webtoon: líneas finas **ámbar/dorado** (`#A29B39` medido) formando una
  rejilla o un marco con esquinas cortadas en diagonal, sobre panel
  semitransparente gris-azulado (`#2B3136`) — no es una trama de manga, es
  vectorial y limpio, pensado para pantalla (coincide con lo que ya describió
  `03-solo-leveling/partes/imagen.md` sobre el estilo general del webtoon:
  degradados digitales, no tramas).
- Anime (rediseño SS2): líneas de **circuito/PCB** en violeta neón (`#8C1BF8`)
  con ramificaciones finas tipo rayo o raíz, sobre negro casi puro, más
  parecido a una interfaz de ciencia ficción que a un pergamino de videojuego
  retro — cambio de estilo entre el webtoon y el anime que vale la pena
  anotar para el redactor (punto 17, guía de IA).
- Los soldados sombra comparten una textura propia: **grietas de energía**
  (líneas finas e irregulares, no rectas) que se iluminan sobre armadura
  negra mate — es distinto de las líneas de circuito del Sistema (esas sí son
  rectas/geométricas). Dos texturas de brillo distintas para dos elementos
  distintos del ángulo (interfaz vs. ejército).

**Equivalentes libres con licencia (comprobados)**
- **«Free UI Hologram Interface»**, OpenGameArt, autor **Wenrexa**, licencia
  **CC0** (dominio público, sin atribución obligatoria), tags `hologram, ui,
  interface, png, sprites` — encaja directamente con el rediseño violeta neón
  del anime · https://opengameart.org/content/free-ui-hologram-interface ·
  ✅ licencia CC0 comprobada en la página (icono + enlace a
  creativecommons.org/publicdomain/zero/1.0).
- **«Magic Circle»**, CLIP STUDIO ASSETS, **gratis** (precio comprobado:
  «free» en la página) — sirve para los círculos mágicos de invocación de
  sombras (`Shadow Extraction`) y los portales de mazmorra ·
  https://assets.clip-studio.com/en-us/detail?id=2006760 · ✅ precio
  comprobado con curl.
- **«Free Smoke PS Brushes»**, MyPhotoshopBrushes, licencia **Free for
  Commercial Use** (uso comercial permitido) — para el humo negro/blanco que
  desprenden los soldados sombra en casi todo el arte oficial (`Igris_2.jpg`,
  `Beru_CV.jpg`, el render del ejército) ·
  https://myphotoshopbrushes.com/resources/3843/free-smoke-ps-brushes ·
  formato .ABR · ✅ licencia comprobada en el JSON-LD de la propia página.
- Para el grabado en metal de las armaduras y las líneas de velocidad del
  webtoon en general, `03-solo-leveling/partes/imagen.md` ya encontró y
  verificó dos fuentes CC0/gratis (3dtextures.me «Metal Armor Pattern 001» y
  el pack de «Manga Speedlines»): no las repito, sólo las señalo para que el
  redactor las junte con las de aquí en una sola guía de texturas.

## Hallazgos · Punto 23 — Colaboraciones y cruces (ángulo sombras)

**Videojuegos: la colaboración que trae exactamente un soldado sombra**
- **Fortnite × Solo Leveling: ARISE**: el pack «Blood-Red Commander Igris»
  incluye el traje de Igris con **estilos seleccionables**, un objeto de
  espalda propio («**Igris' Cloak**», con sus propios estilos) y una
  emote llamada **«Shadow Shift»** — o sea, la colaboración no sólo vistió a
  Igris, le dio una animación propia ligada al gesto de invocar/transformar
  sombras. Disponible desde el 18-feb-2026 (parche v39.50, Capítulo 7
  Temporada 1) · fuentes:
  [Sportskeeda](https://www.sportskeeda.com/fortnite/how-get-solo-leveling-arise-skins-fortnite-sung-jinwoo-blood-red-commander-igris-cha-hae-in)
  y
  [GosuGamers](https://www.gosugamers.net/entertainment/news/78010-fortnite-teases-solo-leveling-arise-crossover-with-jinwoo-and-igris)
  · ✅ dos fuentes (verificación propia, independiente de la que ya usó
  `03-solo-leveling` para el mismo evento).

**Figura oficial de un soldado sombra (referencia 3D)**
- **Igris, figura de vinilo Youtooz** (licencia oficial): estilo «chibi»
  (proporciones grandes de cabeza, no realista), casco con cuernos y la
  cinta/cabello rojo característico, armadura azul-negra con líneas cian,
  espada sostenida en vertical frente al cuerpo — USD 29,99 · imagen oficial
  del producto 676×1000 ·
  https://youtooz.com/cdn/shop/files/316t2d401i.png?v=1762268922 · medida
  con Pillow · **la miré**: pose de «presentación» (de pie, arma al frente,
  mirada al frente) útil de referencia 3D de volumen, aunque el estilo
  «chibi» no sirve para copiar proporciones realistas · fuente:
  [Youtooz — Igris](https://youtooz.com/products/igris) (precio y altura
  comprobados en el JSON de la página) · ✅.

**Cosplay bien hecho, con volumen real (props del Sistema/armas de Jinwoo)**
- **Sung Jinwoo (cosplayer «osskycos»)**, Japan Expo Sud 2025 (22-feb-2026),
  fotografiado por **esby.photo**: gabardina/abrigo negro largo, camiseta
  blanca, **dos dagas curvas rojo-negro-doradas con relieve real** (resina o
  espuma pintada, no plástico plano) cruzadas en pose de combate — son las
  dagas «Kasaka's Venom Fang», el arma personal de Jinwoo, con volumen y
  desgaste de pintura visibles · 1024×769 · licencia **CC BY-NC-SA 2.0** ·
  https://live.staticflickr.com/65535/54356837159_1b963d73b8_b.jpg · fuente:
  [Flickr, vía Openverse](https://www.flickr.com/photos/22789397@N05/54355753072)
  · medida con Pillow · **la miré**: hoja `hojas/vestuario_03.jpg` #3 · ✅
  (imagen vista completa + metadatos de evento/fecha en el propio título del
  archivo).
- Hay más fotos de la misma sesión (mismo cosplayer, mismo evento, ángulos
  distintos): otras 6 imágenes en la misma licencia CC BY-NC-SA 2.0,
  búsqueda `q=Solo Leveling cosplay` en la API de Openverse — las dejo
  anotadas por si el redactor quiere variar el ángulo de la pose.
- **Esil Radiru (mismo fotógrafo, Dokomi 2025)**: cosplay distinto, no es un
  personaje de mi ángulo (ni Sistema ni ejército de sombras) — lo anoto sólo
  como referencia por si el investigador de voz/personajes lo necesita, no
  lo desarrollo aquí.

**Aviso de datos cruzados (comprobado, no usar)**
- El archivo de la wiki `File:Anime awakened Sung Jinwoo Character
  design.webp` (800×643) **NO es una ficha de Jinwoo**: al abrirlo muestra a
  «**Shun Mizushino**, CV Yasuto Saka», un personaje y actor de voz que no
  corresponden a Sung Jinwoo ni a su reparto japonés real (el seiyuu
  confirmado de Jinwoo en el anime es otro). Es un caso exacto del aviso del
  encargo sobre datos cruzados de otra obra por nombre de archivo ambiguo:
  **no lo uso** para vestuario ni arte oficial, y lo marco aquí para que
  nadie más en el equipo lo cite por error · comprobado abriendo la imagen
  con Read (no de memoria) · fuente:
  https://static.wikia.nocookie.net/solo-leveling/images/d/dc/Anime_awakened_Sung_Jinwoo_Character_design.webp/revision/latest?cb=20240208161648

## Lo mejor para la lámina

1. El **panel del Sistema en holograma violeta** del anime (`Anime
   System.png`, hoja `sistema_01.jpg` #2) es la referencia más directa para
   un cuadro de diálogo/ventana de canal: ya tiene el marco, el título en
   mayúsculas y el contraste violeta-sobre-negro que pide un Discord de
   doblaje sin parecer una burbuja genérica.
2. El modelo 3D **«SOLO LEVELING HOLOGRAM»** de Sketchfab (CC Attribution) es
   la única referencia 3D real (no IA) de alguien recreando el panel del
   Sistema: sirve de base de volumen/perspectiva si la lámina se monta en
   Blender con el panel «flotando» sobre un objeto real.
3. El **render oficial del ejército** (`Shadow Army Render.png`, hoja
   `sombras_02.jpg` #1) con Igris al frente es la mejor imagen de grupo con
   licencia de wiki para un canal que necesite mostrar «el equipo» o «los
   miembros» de algo.
4. Las **dagas de Jinwoo en cosplay real** (hoja `vestuario_03.jpg` #3)
   muestran cómo dar volumen físico a un arma/objeto pequeño del personaje —
   útil si la lámina pone el arma sobre una mesa o mostrador real en vez de
   sólo dibujada.
5. El contraste medido **ámbar-webtoon vs. violeta-anime** para la misma
   ventana «STATUS» es el dato más aprovechable para decidir de una vez la
   paleta del canal: agrupa con el arco de temporada (S1 ámbar/webtoon, S2
   violeta neón) según qué anime estén doblando ese arco en el servidor.

## No encontré

- ⚠️ Modelos 3D con licencia libre de **Beru**, **Tank**, **Kaisel** o
  **Iron** en Sketchfab: busqué «Beru Solo Leveling», «Tank Solo Leveling»,
  «Kaisel Solo Leveling», «shadow soldier Solo Leveling» y sólo salió un
  modelo genérico («Shadow Knight Solo Leveling», sin nombre propio). Puede
  que estos personajes, al ser menos centrales que Igris, no tengan aún
  version modelada por fans.
- ⚠️ Wallpapers de fans centrados en **sitios/mazmorras vacíos** (sin
  personaje): busqué «solo leveling gate», «solo leveling dungeon», «solo
  leveling scenery» en Wallhaven y no hubo resultados; todo lo que sube la
  comunidad son retratos de personajes, no paisajes solos.
- ⚠️ Una **tercera fuente independiente** para el arte de Jinwoo+Tank
  (`ee80f9382a9bc1c02c6558436508e0309201b168.jpg`) que confirme al 100% que
  es arte oficial de la editorial y no un fan muy fiel al estilo: sólo tengo
  la cuenta que lo publicó + el tag `official_art` de Safebooru.
- No encontré (ni busqué a fondo, no es mi punto) sitios/dungeons con luz y
  hora del día medida: eso es expresamente del punto 4, del equipo de vídeo.

## Bitácora de búsqueda

- Wiki de Fandom (API, inglés): `action=query&list=search&srsearch=System
  window`, `action=query&list=allpages&apprefix=System` (encontró `System` y
  `System/Gallery`), `action=parse&page=System&prop=wikitext`,
  `action=query&titles=System/Gallery&prop=images` (21 imágenes),
  `action=query&list=search&srsearch=Army of Shadows`, `srsearch=Shadow
  Soldiers` (encontró la página `Shadows`), `action=parse&page=Shadows&prop=wikitext`,
  `action=query&titles=Shadows&prop=images`. `imageinfo&iiprop=url|size` para
  medir cada imagen citada (System1, System2, SystemInventory1, Anime
  System, Shop, Blessed/Cursed random box, Shadow Army Render, Shadows1,
  Tank4, Iron 3, Kaisel1, Greed2, Bellion1, Kamish3, Ant Queen Shadow1,
  Jima1).
- Descarga y medición con Pillow (en
  `/tmp/claude-0/trabajo/80-solo-leveling-imagen/`, borrado al terminar):
  `system1.jpg`, `anime_system.png`, `shadow_army_render.png`, `igris2.jpg`,
  `beru_anime1.png`, `beru_cv.jpg`, `shop.jpg`, `system_inv.jpg`,
  `jinwoo_design.webp`, `jinwoo_player.png`, `cosplay_jinwoo.jpg` — todas
  **miradas con Read**, no sólo descargadas. Hex medidos con muestreo directo
  de píxeles y con un filtro de saturación/tono (HSV) para separar el color
  de acento del fondo.
- Sketchfab (API v3, `type=models&downloadable=true`): «Solo Leveling
  Igris», «Solo Leveling Beru» (sin resultados), «Sung Jinwoo», «Solo
  Leveling System», «Beru Solo Leveling» (sin resultados), «shadow soldier
  Solo Leveling», «Kaisel Solo Leveling» (sin resultados), «Tank Solo
  Leveling» (sin resultados relevantes), «hunter status window» (sin
  resultados). Ficha completa (licencia, autor, descripción) por
  `api.sketchfab.com/v3/models/<uid>` de cada resultado usado.
- Wallhaven (API v1, `purity=100`): `q=solo leveling shadow`, `q=solo
  leveling system` (sin resultados), `q=igris`, `q="solo leveling"
  dungeon` (sin resultados), `q="solo leveling"` ordenado por favoritos,
  `q="solo leveling" gate` (sin resultados), `q="solo leveling" scenery`
  (sin resultados). Ficha de cada wallpaper citado por
  `api/v1/w/<id>` (tags, autor, purity).
- Safebooru (API `dapi`, JSON): `tags=kaisel_(solo_leveling)`,
  `tags=tank_(solo_leveling)`, `tags=iron_(solo_leveling)` (confirmó que
  existen como tags propios) — usé también los resultados ya traídos por
  `datos-imagen.md` para `igris_(solo_leveling)` y `beru_(solo_leveling)`
  sin repetir la consulta.
- Openverse (API v1): `q=Solo Leveling cosplay` (13 resultados, todos de la
  misma fotógrafa de eventos, esby.photo, en Flickr, CC BY-NC-SA 2.0).
- OpenGameArt, CLIP STUDIO ASSETS, MyPhotoshopBrushes: verificados con curl
  (licencia CC0 de OpenGameArt confirmada en el HTML de la página; precio
  «free» del Magic Circle de Clip Studio; licencia «Free for Commercial Use»
  del pack de humo en el JSON-LD de MyPhotoshopBrushes).
- WebSearch (inglés, 5 búsquedas): «free sci-fi hologram UI overlay texture
  PNG CC0 license», «magic circle brush free commercial use license Clip
  Studio OR Photoshop», «free smoke brush pack CC0 OR "free for commercial
  use" Photoshop Procreate», «Fortnite Igris skin Solo Leveling Arise
  shadow soldier» para verificar la colaboración con una fuente propia
  (Sportskeeda + GosuGamers) distinta a la que ya citó `03-solo-leveling`,
  «Solo Leveling anime official wallpaper download» (sin resultado oficial,
  sólo agregadores de terceros) y «Igris figure Solo Leveling Good Smile OR
  Banpresto OR Bandai official» (encontró la figura de vinilo de Youtooz,
  verificada aparte con curl al JSON de la página del producto).
- No usé YouTube (no hizo falta para estos 6 puntos; las capturas del
  Sistema y el ejército ya estaban en la wiki y en Sketchfab/Wallhaven/
  Openverse con fuente y tamaño verificables).
- Hojas de contacto propias creadas con Pillow (no genéricas): `hojas/
  sistema_01.jpg` (4 capturas del Sistema, webtoon y anime), `hojas/
  sombras_02.jpg` (4 artes oficiales del ejército/Igris/Beru), `hojas/
  vestuario_03.jpg` (cartel Cour 1, turnaround oficial, cosplay real) — cada
  una bajo 3 MB, construidas a partir de las imágenes ya descargadas y
  medidas arriba. También miré las hojas de contacto genéricas de
  `investigar_serie.py` (`herramientas/referencias/solo-leveling-el-sistema-y-las-sombras/hoja_01.jpg`,
  `hoja_09.jpg`, `hoja_10.jpg`) para localizar filas concretas (System quest,
  turnarounds, Ashborn) sin tener que abrir las 476 imágenes sueltas.

**Parte terminada.** Los 6 puntos (1, 3, 15, 16, 19, 23) están cubiertos con
lo obligatorio del encargo, con el ángulo propio del Sistema y las sombras:
arte oficial variado de ambos (interfaz + ejército), fan art y 3D con
licencia, hex medidos de Jinwoo y de la armadura de Igris/Beru, wallpapers
con autor y tamaño, texturas 2D con equivalentes libres comprobados, y
colaboraciones/cosplay centrados en objetos y personajes de mi ángulo. Lo que
falta son sólo los extras listados en «No encontré», con sus búsquedas.
