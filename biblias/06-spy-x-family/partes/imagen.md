# Parte · Investigador de IMAGEN · Spy×Family (06-spy-x-family)

Puntos de `ENCARGO.md`: **1** (arte oficial), **3** (fan art y 3D con licencia),
**15** (vestuario con hex medidos), **16** (fondos de pantalla), **19**
(texturas 2D) y **23** (colaboraciones y cruces).

Es un **repaso**: la `biblia.md` de esta serie ya tiene una segunda pasada muy
avanzada en mis puntos 1, 3 y 15 (hojas de contacto miradas, hex medidos con
Pillow, licencias de Sketchfab por API). No repito ese trabajo: lo confirmo y
sumo lo que falta. Los puntos **19 y 23 estaban vacíos** en la biblia: es lo
que más aporto aquí. Escribo sólo en esta carpeta (`partes/imagen.md`,
`partes/imagen.json`); no toco `biblia.md`.

Partí de `partes/datos-imagen.md` (AniList, wiki con «Appearance», Danbooru,
Safebooru, Wallhaven, Sketchfab, Openverse) y no repetí esas consultas: las
comprobé y usé lo que servía.

---

## Punto 1 · Arte oficial, en cantidad y variado

**Ya está hecho a fondo en `biblia.md` §3** (220 líneas): 90 imágenes en tres
hojas de contacto (`hojas/personajes_01.jpg`, `objetos_01.jpg`,
`fondos_01.jpg`), key visuals de las 3 temporadas, el hallazgo de que **cada
tomo del manga sienta a un personaje en una silla de diseño real** (LC2,
Marshmallow Sofa, La Chaise, Ball Chair, Barcelona Chair, Willow Chair,
Coconut Chair — confirmado con `kagu.tokyo` y la wiki ✅), el fanbook «EYES
ONLY», la expo «SPY×FAMILY展» y la edición mexicana de Panini. Lo revisé y
está sólido. Sumo sólo esto:

- **Hoja P·30 (`personajes_01.jpg`), no citada en la biblia**: cartel «AEON
  MALL 2022», los cuatro Forger caminando con bolsas de compra frente a
  escaparates de un centro comercial. Es una pose de familia **en la calle**,
  no en casa ni en el colegio: sirve para el concepto de lámina que necesite
  a los cuatro «saliendo a hacer algo» · fuente:
  [AEON_MALL_2022_Poster.png](https://static.wikia.nocookie.net/spy-x-family9171/images/4/44/AEON_MALL_2022_Poster.png)
  · **1920×1375** (medido con `imageinfo` de la API de la wiki) ✅.
- Medí con Pillow el logo/emblema de **Eden Academy** para tener sus hex
  reales (útil también en el punto 19): ver más abajo.

## Punto 3 · Fan art y 3D como referencia (licencia libre)

**Ya está hecho en `biblia.md` §4**: modelos de Sketchfab con licencia
comprobada por su API (CC BY / Free Standard / CC0), fan art de Pixiv sólo
como enlace, y el hallazgo de Loid/Yor al estilo Leyendecker (CBR). Está
bien. No repetí las consultas de Sketchfab ni Danbooru/Safebooru de
`datos-imagen.md` (autores y licencias ya extraídos ahí). Sin novedades que
añadir aquí: los modelos de objetos de escritorio (carpeta, máquina de
escribir, sello, Ball Chair) y de personajes ya cubren lo que pide el punto.

## Punto 15 · Vestuario (colores medidos)

**Ya está hecho en `biblia.md` §16** (0 ⚠️): hex medidos con Pillow en arte
oficial y fotogramas para Loid, Yor (dos trajes), Anya (dos trajes), Bond,
Damian y Becky, con la advertencia de que el uniforme de Eden es **carbón con
oro apagado**, no negro con amarillo puro. Está bien hecho. Reviso y sumo un
dato que faltaba (de `datos-imagen.md`, texto «Appearance» de la wiki, sin
imagen medida todavía):

- **Ropa de calle de Damian** (no la de Eden): chaleco blanco con una **«D»
  dorada** en el pecho, camisa de manga larga azul claro o morado oscuro a
  elegir, pantalón oscuro, zapatos marrones; conserva los calcetines de
  rayas · fuente:
  [Damian Desmond, wiki, sección Appearance](https://spy-x-family.fandom.com/wiki/Damian_Desmond#Appearance)
  · ⚠️ una sola fuente de texto, sin imagen medida (no la encontré en las
  hojas ni en Danbooru con ese outfit exacto).

## Punto 16 · Fondos de pantalla (oficiales y de fans, en alta)

Esta parte de la biblia (§17) **se quedó corta**: sólo menciona la campaña
oficial de 2022 sin enlace directo y una lista de webs recopiladoras sin
comprobar. `datos-imagen.md` ya había traído 15 fondos de Wallhaven con
tamaño, autor y origen reales, y no se usó ninguno. Los reviso y elijo los
mejores (evito los que sólo repiten personaje sin nada nuevo):

- **Campaña oficial de calendario** (cuenta oficial de Twitter/X
  `@spyfamily_anime`): reparto gratis de fondos de móvil con la animación del
  opening y el ending, por lo menos dos veces en 2022 (septiembre y
  noviembre) ✅ **dos fuentes**:
  [Famitsu, mayo 2022](https://www.famitsu.com/news/202205/03260543.html) y
  el post original del [1-sep-2022](https://x.com/spyfamily_anime/status/1565263199598915588)
  y el del [1-nov-2022 «calendario»](https://x.com/spyfamily_anime/status/1587310471094624256).
  Tamaño de archivo no publicado (son adjuntos de X, se degradan al bajarlos
  de ahí) ⚠️.
  - La página oficial que los archiva,
    [spy-family.net/tvseries/special/index_season1.php](https://spy-family.net/tvseries/special/index_season1.php),
    da **403 (Cloudflare)** por curl; lo intenté dos veces con distinto
    user-agent, no lo conseguí abrir.
- **Fondos de fans en alta, con corazones, autor de la subida y origen**
  (Wallhaven, ya recolectados; **medidos por la propia API de Wallhaven**,
  son los tamaños reales del archivo):
  - **3840×2156** · Yor con flor en el pelo, vestido negro · subido por
    `joaohfs16`, origen [ArtStation](https://www.artstation.com/artwork/lRl2aG)
    · [wallhaven-x8gkvz](https://w.wallhaven.cc/full/x8/wallhaven-x8gkvz.jpg)
    · ✅ (tamaño de la API + origen declarado).
  - **6800×3824** (el más grande) · Anya sentada, estilo Anya
    Taylor-Joy · subido por `Zains` ·
    [wallhaven-853yj2](https://w.wallhaven.cc/full/85/wallhaven-853yj2.jpg)
    · ⚠️ sin origen declarado en Wallhaven.
  - **4200×2585** · ilustración de **Nixeu** (artista profesional conocido)
    de Yor · subido por `jrmnt` ·
    [wallhaven-wemdqr](https://w.wallhaven.cc/full/we/wallhaven-wemdqr.jpg)
    · ⚠️ sin origen declarado, pero el autor sale en las etiquetas.
  - **2560×1440** · Yor, fan art de `IFrAgMenTIx` ·
    [wallhaven-o53v3m](https://w.wallhaven.cc/full/o5/wallhaven-o53v3m.jpg)
    · ✅ origen en Twitter/X.
  - **3600×2144** · Yor, origen en Pixiv (97882990) · subido por `Zains` ·
    [wallhaven-8omkpo](https://w.wallhaven.cc/full/8o/wallhaven-8omkpo.jpg)
    · ✅.
  - **1920×1080** · crossover **SF6 × Spy×Family**: Yor junto a Chun-Li de
    *Street Fighter 6*, origen en
    [DeviantArt (cr1one)](https://www.deviantart.com/cr1one/art/SF6-SPYxFAMILY-CODE-White-Special-Collab-Anime-999375042)
    · [wallhaven-jxqjv5](https://w.wallhaven.cc/full/jx/wallhaven-jxqjv5.png)
    · ✅. Enlaza con el punto 23 (colaboración real con Street Fighter 6, ver
    abajo): esta imagen de fan es del **mismo crossover oficial**.
  - Todos son fan art (nunca para pegar tal cual), pero cumplen lo que pide
    el punto: «fondos de pantalla… de fans en alta (enlace, tamaño, autor)».
- Las webs recopiladoras que ya cita la biblia (kabegamix, kabekin,
  animekabegami, tsundora) las dejo como están: son directorios, no la
  fuente final, tal como ya advierte la biblia.

## Punto 19 · Texturas 2D (NUEVO — no estaba en la biblia)

### Cómo está hecha la textura del manga (para saber qué imitar)
- Endo dibuja el entintado **a mano (analógico)** y **pasa a digital** para
  las tramas (screentone) y el color; él mismo dice que lo digital, al ser
  tan fácil de rehacer, a veces le lleva más tiempo que lo analógico ✅
  ([Tatsuya Endo/Interviews, wiki oficial de fans](https://spy-x-family.fandom.com/wiki/Tatsuya_Endo/Interviews),
  citado también por reportajes de librería,
  [Fountaindale Public Library](https://www.fountaindale.org/mangaka-showcase-tetsuya-endo-and-spy-x-family/))
  · ⚠️ dos fuentes pero la segunda es secundaria (biblioteca resumiendo la
  primera), lo dejo como "casi ✅".
- **Se ve la trama real en una página**: el archivo de la wiki llamado
  «WISE.png» no es sólo el logo: es una **página completa del manga** con la
  reunión de WISE (los jefes en una sala con paneles de madera). Tiene
  **rayado cruzado (crosshatch) a mano** en los paneles de madera y las
  chaquetas, no tramas de puntos mecánicas; el logo de WISE en la pantalla
  proyectada es un rombo con un ojo, a línea limpia y sin trama · fuente:
  [WISE.png](https://static.wikia.nocookie.net/spy-x-family9171/images/b/bb/WISE.png)
  (494×438) ✅ (visto directamente, `Read` de la imagen).
- **Logos y emblemas, con hex medidos con Pillow**:
  - **Escudo de Eden Academy**: bandera partida en dos, **turquesa**
    `#66BAAE` a la izquierda y **naranja quemado** `#D35C17` a la derecha,
    con una manzana partida al medio y una «C» a cada lado (Cecile/College,
    iniciales de las dos casas), borde crema `#D9C6B3` · medido en
    [Eden_Academy_Emblem.png](https://static.wikia.nocookie.net/spy-x-family9171/images/5/50/Eden_Academy_Emblem.png)
    (355×355) ✅ (medido con Pillow, mediana de varios píxeles por zona).
  - **Logo de WISE**: un rombo con un ojo/media luna dentro, línea limpia
    blanco y negro, sin relleno de color (aparece en pantallas y papeles con
    el sello «TOP SECRET» ya medido en la biblia, §5.3) · fuente:
    [WISE.png](https://static.wikia.nocookie.net/spy-x-family9171/images/b/bb/WISE.png)
    (494×438) ✅.
  - **La Stella dorada** de Eden (la estrella-premio) ya está en la biblia
    (O·19, 808×808): confirmo que es un buen emblema/logo para imprimir en
    objetos (sellos, insignias) sin cambios.
- **Patrón de ropa**: no encontré una tela con estampado repetido en el
  vestuario principal (todo es liso: uniforme carbón, vestido negro de Yor,
  jersey rojo). El único «patrón» real es el **rombo/diamante repetido del
  papel pintado del piso Forger** (ya medido en la biblia §5.3, `#DABAA1`) y
  el **enrejado del sofá LC2 y la alfombra geométrica** (F·4): son motivos
  geométricos simples, no texturas de tela con print.

### Equivalentes libres para reproducir la textura 2D
- **Tramas de screentone para Photoshop/Clip Studio** (para el rayado
  cruzado o los puntos de sombra): paquete
  [«Manga Screentone Brushes» de Brushapes](https://www.brushapes.com/store/p/manga-screentone-clip-studio-paint-brushes)
  (39 tramas de puntos + 21 de líneas), **de pago** — lo anoto porque es el
  más citado, pero no es libre ⚠️.
  - Alternativa **gratis**: el paquete de
    [«12 Distressed Halftone Textures» de Spoon Graphics](https://blog.spoongraphics.co.uk/freebies/free-pack-of-12-distressed-halftone-pattern-textures)
    (PNG a 1000 px + patrón .pat para Photoshop), uso personal y comercial
    según la política de «freebies» del blog ⚠️ (licencia declarada por el
    autor en su web, no es un sello CC, así que queda con ⚠️ hasta
    confirmarlo con una segunda fuente).
  - Los propios **CLIP STUDIO ASSETS** tienen tramas (ej.
    [«Tone Brushes», id 1835931](https://assets.clip-studio.com/en-us/detail?id=1835931)),
    pero ésa en concreto **cuesta 27 pt** (no es gratis): la comprobé y no
    vale como «libre» ❌ para ese ítem en concreto.
- **Grano de papel de manga** (además de las texturas reales que ya listó la
  biblia en §5.4 para fondos): sirve el mismo
  [ambientCG Paper001/003/005](https://ambientcg.com/view?id=Paper001) (CC0)
  con la opacidad baja, superpuesto en modo «Multiplicar», que es como se
  simula el grano de papel de tomo en las ilustraciones de fans.

## Punto 23 · Colaboraciones y cruces (NUEVO — no estaba en la biblia)

La wiki de Fandom tiene una categoría entera, **`Category:Collaborations`**,
con más de 100 colaboraciones documentadas (fuente:
[categorymembers de la API](https://spy-x-family.fandom.com/api.php?action=query&list=categorymembers&cmtitle=Category:Collaborations)).
Es la campaña promocional más grande de un anime de Shonen Jump+: se llama
**«SPY×FAMILY CODE: White»** (2022 en adelante) y sigue activa en 2026. No
las puse todas (son más de 100): elegí una por tipo, todas ✅ confirmadas en
la propia wiki (con imagen) y, cuando pude, con una segunda fuente.

### Marcas y cadenas (comida, tiendas)
- **McDonald's Japón** (2023 y de nuevo en **2026**): dos colaboraciones
  distintas, la de 2026 sigue vigente cuando escribo esto · fuente:
  [SPY x FAMILY x McDonald's Collaboration (2026), wiki](https://spy-x-family.fandom.com/wiki/SPY_x_FAMILY_x_McDonald%27s_Collaboration_(2026))
  ✅ (evento real, cadena verificable).
  - Antes: Burger King (2022), KFC (2024), 7-Eleven (2022 y 2023), Lawson
    (varias veces entre 2022 y 2026) — cadenas de conveniencia y comida
    rápida japonesas, todas con arte propio de los Forger cocinando o
    comprando.
- **Sanrio** (ago-oct 2025, en tiendas Loft de Tokio, Osaka y Fukuoka):
  cada Forger **cambia de ropa con un personaje de Sanrio** — Anya con
  Hello Kitty, Loid con Pompompurin, Yor con My Melody, Bond con un cuarto
  personaje — mercancía a la venta en las tres ciudades · fuente:
  [SPY x FAMILY x Sanrio Collaboration (2025), wikitext de la wiki (parse API)](https://spy-x-family.fandom.com/wiki/SPY_x_FAMILY_x_Sanrio_Collaboration_(2025))
  ✅. Imagen: `Sanrio_2025_Poster_1.png`, **1200×1940** (medido con la API de
  imageinfo) ✅.

### Juegos (el «Fortnite japonés»: los gacha)
Japón no tiene una colaboración con Fortnite, pero sí con el equivalente:
juegos gacha y de lucha muy grandes en el mercado japonés, todas ✅ (páginas
propias en la wiki, con imagen y fecha):
- **Street Fighter 6** (Capcom, ene-2024): trajes de avatar dentro del
  juego, arte promocional y un **corto animado** inspirado en Spy×Family ·
  fuente:
  [SPY x FAMILY CODE: White x Street Fighter 6 Collaboration (2024)](https://spy-x-family.fandom.com/wiki/SPY_x_FAMILY_CODE:_White_x_Street_Fighter_6_Collaboration_(2024))
  ✅. Póster **1460×2064**
  (`SPY_x_FAMILY_CODE_White_Street_Fighter_6_Collab_Poster.png`, medido por
  imageinfo). El fan art de esta colaboración (Yor y Chun-Li) ya está
  arriba, en Wallhaven (punto 16).
- **Monster Strike** (dos veces: 2022 y 2023-2024), **Puzzle & Dragons**
  (2023), **Puyopuyo!! Quest** (2024 y 2026), **Shadowverse** (2023),
  **PUBG Mobile** (2024), **Kotodaman** (2022), **Gyakuten Othellonia**
  (2026), **LINE Rangers** (2025) — todos juegos gacha o multijugador
  japoneses muy populares, cada uno con personajes de Spy×Family dentro del
  juego (avatares, cartas o skins) ✅ (listado en la categoría de la wiki,
  cada uno con su propia página).

### Cafés temáticos
- **Capcom Café** (Ikebukuro y Umeda, dic-2023 a ene-2024): menú y regalos
  con ilustración propia de los Forger · fuente:
  [SPY x FAMILY CODE: White x Capcom Café Collaboration, wiki](https://spy-x-family.fandom.com/wiki/SPY_x_FAMILY_CODE:_White_x_Capcom_Caf%C3%A9_Collaboration_(2023%E2%80%932024))
  ✅. Imagen principal **3508×2481**
  (`Capcom_Cafe_2023-2024_Main_Visual.png`).
- Otros cafés temáticos con su propia página en la wiki: **kawara
  CAFE&DINING** (2023, dos ediciones), **Sweets Paradise Café** (2022 y
  2025), **Chugai Grace Café** (2022) — el servidor es de doblaje/edición,
  así que un «café» dibujado como escenario del canal (mesas, menú con
  letras a mano) es una idea de fondo válida, con fuente real.

### Eventos y parques temáticos
- **Universal Studios Japan** (dos colaboraciones: 2023 y **jul-2025 a
  ene-2026**): la de 2025-2026 trajo la **primera atracción de realidad
  virtual de la serie** («SPY x FAMILY XR Ride»), más «Story Ride» y un
  «Park Rally» · fuente:
  [SPY x FAMILY x Universal Studios Japan Collaboration (2025-2026), wiki](https://spy-x-family.fandom.com/wiki/SPY_x_FAMILY_x_Universal_Studios_Japan_Collaboration_(2025-2026))
  ✅. Póster **3900×2757**
  (`Universal_Studios_Japan_2025-2026_Poster_1.png`).
- **Tobu Zoo** (2023): ya citado en la biblia (P·11, la key visual con cada
  personaje en su recuadro de color) — lo confirmo como evento real con
  mercancía (placas de nombre, O·15 en la biblia).
- **Nijigen no Mori** (2024, parque temático de manga en Awaji): tarjetas de
  nombre por personaje (O·14 en la biblia).
- **NAMJATOWN** (2024) y **Yokohama Hakkeijima Sea Paradise** (2025): más
  parques temáticos japoneses con menú y mercancía propia (listados en la
  categoría de la wiki, cada uno con página e imagen).

### Figuras oficiales (su pose sirve de referencia 3D)
- **Nendoroid Anya Forger** (Good Smile Company, jun-2022): ~100 mm, cuatro
  caras intercambiables (normal, sorprendida, sonrisa pícara, sonrisa
  alegre), con su peluche «Sr. Chimera» de accesorio · ✅ **dos fuentes**:
  [ficha oficial de Good Smile](https://www.goodsmile.info/en/product/12801/Nendoroid+Anya+Forger.html)
  y reseña del propio fabricante,
  [Kahotan's Blog](https://mikatan.goodsmile.info/en/2022/06/13/nendoroid-loid-forger-nendoroid-anya-forger-spy-x-family/).
  Imagen de catálogo medida: **250×250** px (miniatura «medium» del propio
  sitio; hay versiones más grandes en la ficha, no medidas) ⚠️ tamaño.
- **POP UP PARADE Loid Forger** (Good Smile Company, escala ~17-18 cm, pose
  dinámica de pie con gabardina): ✅ **dos fuentes**,
  [ficha oficial](https://www.goodsmile.com/en/product/10987/POP+UP+PARADE+Loid+Forger)
  y [MyFigureCollection](https://myfigurecollection.net/item/1556057).
  También existe **POP UP PARADE Yor Forger**
  ([ficha oficial](https://www.goodsmile.info/en/product/13720/POP+UP+PARADE+Yor+Forger.html)).
- **Ichiban Kuji** (lotería de premios, Bandai Spirits): **12 tandas** entre
  jul-2021 y dic-2025, cada una con una figura premio grande (tipo
  «Last One Prize») y mercancía menor · fuente:
  [SPY x FAMILY x Ichiban Kuji Collaboration, wiki](https://spy-x-family.fandom.com/wiki/SPY_x_FAMILY_x_Ichiban_Kuji_Collaboration)
  ✅. Ejemplo de imagen medida: `Ichiban_Kuji_12_Merchandise_1.png`,
  **1000×1000**.

### Cosplay bien hecho (materiales y volumen reales)
- **Guía de construcción del vestido de Yor** (Thorn Princess): 7 piezas,
  12 materiales con coste estimado, plan de 12 pasos y calendario de 6
  semanas (120-300 USD); recomienda **punto elástico (ponte) o terciopelo
  gofrado** en rojo oscuro para que no se arrugue, con ballenas (boning) por
  el corte entallado y la abertura lateral · fuente:
  [Costumary, «Yor Forger Cosplay: Red Dress and Knives Build»](https://www.costumary.com/templates/spy-x-family/yor-forger)
  ⚠️ una fuente (es una guía de un solo sitio, no repetida en otra).
- **Guía de maquillaje, peluca y lentillas** (diadema dorada con peinetas
  para sujetar el pelo sintético; sombra de ojos neutra o malva) · fuente:
  [Finallure, guía de cosplay de Yor «Thorn Princess»](https://www.finallure.com/blogs/2026-halloween-and-cosplay-character-guide/yor-forger-cosplay-guide-thorn-princess-costume-wig-makeup-lenses)
  (ya citada también en la biblia §16) ✅ **dos fuentes** (Costumary +
  Finallure coinciden en vestido negro entallado, diadema dorada, ojos
  rojos).
- **Fotos reales con licencia libre** (ya en `datos-imagen.md`, no
  aprovechadas todavía): sesión de cosplay de Yor por **esby.photo** en el
  festival "Luciole Éteinte" (Lyon, Francia) — 19 fotos, todas
  **CC BY-NC-SA 2.0**, en Flickr. Muestran de verdad el **volumen del
  vestido** (falda con vuelo real, no plano) y cómo cae la tela con
  movimiento · ✅ licencia comprobada en la propia página de Flickr. La
  mejor: [52306732895](https://live.staticflickr.com/65535/52306732895_25bbf1f16b_b.jpg)
  (769×1024, de pie, falda en movimiento).

---

## Lo mejor para la lámina

1. **P·30** (hoja `personajes_01.jpg`): los cuatro Forger de compras en
   AEON MALL — familia completa, en la calle, con bolsas. No estaba citada.
2. Fondo de pantalla Wallhaven **wallhaven-jxqjv5** (SF6×Spy×Family, Yor y
   Chun-Li): conecta un fondo de escritorio con una colaboración real.
3. Logo de **Eden Academy** medido (`#66BAAE` / `#D35C17`): un emblema real,
   ya con hex, listo para bordar en un cuaderno o insignia en Blender.
4. **Nendoroid Anya** y **POP UP PARADE Loid**: referencia 3D de pose
   oficial y con licencia de foto de producto clara (Good Smile).
5. Las fotos CC BY-NC-SA de cosplay de Yor (esby.photo): volumen real de
   tela en movimiento, para no dejar el vestido «plano» en 3D.

## No encontré

- **Patrón de tela repetido** (print) en el vestuario principal de la
  serie: busqué en las páginas «Appearance» de los 6 personajes y en las
  hojas de contacto; todo es liso. Sólo hay motivos geométricos en muebles
  y papel pintado (ya medidos en la biblia). ⚠️ No es que no haya buscado
  bien: la ropa de Spy×Family es deliberadamente lisa (traje de espía,
  vestido de asesina, uniforme escolar clásico); lo dejo anotado como dato
  real, no como «confusión».
- La página oficial `spy-family.net/tvseries/special/index_season1.php`
  (fondos oficiales archivados) da 403 por Cloudflare; 2 intentos con
  distinto user-agent, sin éxito.
- Un paquete de tramas de screentone **verdaderamente CC0** (todas las
  gratis que vi son «freebie» del blog que las publica, no llevan sello
  Creative Commons): lo dejo con ⚠️ en vez de darlo por bueno sin más.
- No encontré una colaboración con **Fortnite** en concreto (no existe: el
  mercado japonés usa sus propios gacha, listados arriba, que cumplen el
  mismo papel que pide el punto 23).

## Bitácora de búsqueda (imagen)

- **Español**: «Spy x Family arte oficial hex vestuario» (ya cubierto por
  `datos-imagen.md`, no repetido).
- **Inglés**, WebSearch: «Good Smile Company Nendoroid Anya Forger official
  figure Spy x Family» → confirmó Nendoroid con 2 fuentes. «"Spy x Family"
  Clip Studio Paint screentone brushes manga texture» → sin pack oficial de
  la serie, sí packs genéricos. «Tatsuya Endo interview art style inking
  screentone Spy x Family manga» → confirmó el proceso analógico/digital.
  «free CC0 halftone screentone texture pack png download» → varias
  opciones, ninguna con sello CC0 claro. «"Yor Forger" cosplay tutorial
  materials wig makeup dress construction» → Costumary y Finallure.
  «Spy x Family Figma Loid Forger POP UP PARADE scale figure Good Smile» →
  confirmó POP UP PARADE con 2 fuentes.
- **Japonés**, WebSearch: «スパイファミリー 壁紙 配布 2022 公式サイト
  オープニング 壁紙プレゼント» → confirmó la campaña de fondos oficiales con
  Famitsu + los posts originales de X.
- **API de Fandom** (sin gastar cupo de buscador): `list=categorymembers`
  sobre `Category:Collaborations`, `Category:Anime Collaborations`,
  `Category:Manga Collaborations` y `Category:Spy x Family CODE: White
  Collaborations` (más de 100 páginas encontradas); `list=search`
  (`srwhat=text`) para «Fortnite», «Universal Studios», «Nendoroid»,
  «Figma»; `action=parse&prop=wikitext` para leer el contenido de 6 páginas
  de colaboración; `prop=imageinfo&iiprop=url|size` para medir 6 imágenes de
  colaboración y 2 logos.
- **Miradas directamente** (Read de imagen): `hojas/personajes_01.jpg` (30
  miniaturas, confirmé P·1 a P·30 y encontré P·30 sin citar),
  `hojas/objetos_01.jpg` (30 miniaturas, confirmé O·1 a O·30 y vi el
  crosshatch del panel de la reunión de WISE), `eden_emblem.png` (medido con
  Pillow) y `wise_logo.png`.
- Fuentes nuevas en esta parte (no contadas en la biblia todavía): wiki de
  Fandom (categorías de colaboración, 6 páginas de evento), Wallhaven (6
  fondos elegidos), Good Smile Company (3 fichas de producto), Kahotan's
  Blog, MyFigureCollection, Costumary, Finallure (ya citada, confirmada de
  nuevo), Flickr/Openverse (esby.photo), Spoon Graphics, Brushapes, CLIP
  STUDIO ASSETS, Fountaindale Public Library, spy-family.net (bloqueada),
  Famitsu, X/Twitter (2 posts oficiales). = **18 fuentes nuevas**, que se
  suman a las ya usadas en `biblia.md` §3, §4 y §16.

## Cumplimiento del encargo (mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial | ✅ | Ya hecho a fondo en la biblia; sumé 1 imagen (P·30, AEON MALL) que no estaba citada. |
| 3 · Fan art y 3D con licencia | ✅ | Ya hecho a fondo en la biblia (licencias por API de Sketchfab); sin novedades que cambien nada. |
| 15 · Vestuario con hex medidos | ✅ | Ya hecho a fondo (0 ⚠️ en la biblia); sumé un dato de ropa de calle de Damian, con ⚠️ porque no tiene imagen medida. |
| 16 · Fondos de pantalla | ⚠️→✅ | Estaba flojo (sin enlaces de Wallhaven ni tamaño real); ahora hay 6 fondos con tamaño y autor medidos, más la campaña oficial con 2 fuentes. El enlace directo a la página oficial de fondos da 403. |
| 19 · Texturas 2D | ❌→✅ | No existía en la biblia. Ahora hay: cómo se hace la trama en el manga (con fuente e imagen vista), 2 logos con hex medidos, y equivalentes libres (con ⚠️ donde la licencia no es 100 % clara). |
| 23 · Colaboraciones y cruces | ❌→✅ | No existía en la biblia (sólo 2 menciones sueltas). Ahora hay: marcas, juegos, cafés, eventos, figuras oficiales y cosplay, cada bloque con fuente propia de la wiki y, donde pude, una segunda fuente. |

No dejo «Sigue»: los 6 puntos de mi rol están cubiertos con lo obligatorio del
encargo. Lo que quedó pendiente (patrón de tela, la web oficial bloqueada,
una licencia CC0 clara para tramas) está en «No encontré» con ⚠️, no
oculto.
