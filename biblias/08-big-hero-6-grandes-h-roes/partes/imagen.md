# Imagen · Big Hero 6 (Grandes Héroes) — puntos 1, 3, 15, 16, 19, 23

Repaso completo (24-sep-2026, red abierta). Parte de `datos-imagen.md` (no se
repiten esas consultas) y de las 7 hojas de contacto que ya había en
`herramientas/referencias/big-hero-6-grandes-h-roes/` (299 imágenes de
disney.fandom.com, bajadas por `investigar_serie.py`): **las miré todas**
(`Read` de las 7 hojas). También descargué y medí a mano 12 imágenes
oficiales (render de Baymax, render de armadura, póster de cine, hojas de
modelo de personaje, manga) con Pillow y con `herramientas/estilo.py`.
La biblia.md que ya existe (de una pasada anterior con red cerrada) tenía los
puntos 1, 3, 15 y 16 con casi todo en ⚠️ (nada visto, hex sin medir); aquí se
confirma, se corrige y se añaden los puntos 19 y 23, que no estaban.

## Hallazgos

### Punto 1 · Arte oficial, en cantidad y variado

- **Las 7 hojas de contacto ya generadas** (299 imágenes, de las galerías de
  Baymax/Hiro/Tadashi en `disney.fandom.com`) sirven de sobra para este punto:
  20 pósters de cine (ya listados con tamaño en la biblia), portadas de libro
  («Hiro and Tadashi Book Cover» 2770×3338, «Big Hero 6 Big Golden Book»
  2062×2560, «Big Hero 6 Read Along» 2560×2559), el cómic manga (portada del
  tomo, 640×982) y **arte conceptual firmado**: turnarounds de Shiyoon Kim
  («Hiro concept shiyoon kim 2.jpg», 1242×1920, saltando en snowboard con
  mochila; hay 6 variantes numeradas), bocetos de «Ninja Hiro» (traje oscuro
  con casco, 1242×1920, dos poses), y hojas de modelo firmadas «Modeler
  Brandon Lawless» / «Modeler Suzan Kim» / «Modeler Dylan Ekren» para Hiro,
  Tadashi, GoGo y Cass adultos (2015, para *Big Hero 6: The Series*) ✅ (vistas
  en las hojas + tamaño confirmado por la API de la wiki:
  [ejemplo](https://static.wikia.nocookie.net/disney/images/3/32/Tadashi_and_Go_Go_character_model.jpg),
  1024×1225).
- **Pósters internacionales confirmados** (tamaño medido por la API, dos
  pósters más que la lista anterior): japonés «ベイマックス» 1024×1444
  ([archivo](https://static.wikia.nocookie.net/disney/images/9/9b/BH6_-_Japanese_Poster.jpg)),
  coreano «빅 히어로» (visto en hoja_01 #22), chino «大白你好，天才俠盜」
  (hoja_02 #68, promo cruzada con *Zootopia*) ✅.
- **El póster internacional (Hiro sosteniendo un cuaderno morado junto a
  Baymax)** se bajó entero y se midió a mano: es el que mejor separa a los
  tres colores base de Hiro y Baymax (ver punto 15) ✅
  ([archivo, 1985×2835](https://static.wikia.nocookie.net/disney/images/c/ca/Big_Hero_6_poster_2.jpg)).
- **El libro de arte** *The Art of Big Hero 6* (Jessica Julius, Chronicle
  Books, oct-2014, 160 pp., prólogo de Don Hall y Chris Williams) sigue ✅ con
  dos fuentes ([Google Books](https://books.google.com/books/about/The_Art_of_Big_Hero_6.html?id=WNmqBwAAQBAJ),
  [reseña AWN](https://www.awn.com/animationworld/book-review-art-big-hero-6)).
  Su portada aparece también en una de las hojas (hoja_06 #220) ✅.
- **El manga**, confirmado con una segunda fuente que faltaba: Yen Press lo
  licenció el 31-08-2014 y lo publicó desde el 25-03-2015; **2 tomos** (el 1
  con los capítulos 1-4 + el capítulo 0 extra al final; el 2 con 5-8, y la
  historia queda en suspenso) ✅✅
  ([Anime News Network](https://www.animenewsnetwork.com/news/2014-08-31/yen-press-licenses-manga-version-of-disney-big-hero-6-film/.78236),
  [Internet Archive, tomo 1 completo](https://archive.org/details/bighero6vol10000ueno)).
  Vi la **página de muestra del capítulo 0** (1000×1436, ver punto 19):
  Baymax dice «Hello! I am ベイマックス» con furigana sobre el inglés, tres
  viñetas de reacción de Hiro y una viñeta de acción con líneas de velocidad
  ✅ ([archivo](https://static.wikia.nocookie.net/disney/images/2/22/Baymax-manga-preview-ch-0.jpg)).
- **Merchandising de papelería japonés** con arte chibi con trazo cosido
  (parches de fieltro «Hiro & Baymax», producto «Back to School» de Disney
  Store Japón, © Disney) ✅ ([archivo, 800×800](https://static.wikia.nocookie.net/disney/images/2/2d/Wappen_Hiro_and_Baymax.jpg)) —
  útil como referencia de textura de fieltro/parche (punto 19).
- **La serie «¡Baymax!» (Disney+, 2022)**, ya en la biblia, sigue siendo la
  mejor referencia de tono para #soporte: Baymax ayudando a gente corriente,
  sin traje de superhéroe ✅ (4 fuentes ya listadas).

### Punto 3 · Fan art y 3D con licencia (sólo referencia o con crédito)

- **Licencias de Sketchfab verificadas por su API** (`api.sketchfab.com/v3/search?...q=baymax&downloadable=true`),
  no sólo «según el buscador» como decía la biblia: de los 4 modelos que
  antes estaban con «licencia sin comprobar», **2 se confirman CC
  Attribution** por la API (el nombre de usuario de la API no siempre
  coincide con el nombre mostrado en la web, pero el ID del modelo es el
  mismo):
  - `etamal1234` → CC Attribution ✅ (mismo ID que el listado antes como
    «Eshtiaque Ahmad»: [sketchfab.com/3d-models/…-418c455a35d24bcdacf853ebf18ae2ee](https://sketchfab.com/3d-models/baymax-418c455a35d24bcdacf853ebf18ae2ee)).
  - `yohyoh` → CC Attribution ✅ (mismo ID que «Koyo_Sikato»:
    [sketchfab.com/3d-models/…-29a502f7c45c4b5e82f74e6d0b5f0066](https://sketchfab.com/3d-models/baymax-29a502f7c45c4b5e82f74e6d0b5f0066)).
  - Nuevo en la búsqueda: **«Chibi Baymax»** de Takoyakixote, **CC
    Attribution-NonCommercial-ShareAlike** ⚠️ (sirve sólo de referencia de
    pose/volumen chibi, no para reutilizar el modelo tal cual por la cláusula
    NC) ([enlace](https://sketchfab.com/3d-models/none-a6dab787e9094c348cd5ba77e8627b03)).
  - Los 4 modelos con CC BY ya confirmados antes (KingOfThePirates,
    theamazingdonovan207, jasonballingham, kangal9990) siguen igual, no
    hizo falta repetir la consulta.
- **Fan art firmado** (Pixiv, DeviantArt, ArtStation), igual que antes: sólo
  como referencia de estilo/pose, nunca para usar. Sigue en ⚠️ (autor visto
  en la página pero sin verificar en una segunda fuente): Catel23
  (DeviantArt), Brandon Lawless (ArtStation).
- **Nuevo hallazgo, sólo como referencia de qué NO calca la lámina**: un
  «Gundam Baymax» — fan art que rediseña a Baymax como un mecha *Gunpla* de
  Bandai (visto en hoja_06, #245) ⚠️ (una sola fuente, sin autor ni enlace
  propio; útil para explicar en la guía de IA qué estilo evitar: Baymax **no**
  lleva paneles duros ni detalle mecánico visible, es vinilo liso).
- **3D y HDRI libres** (Sketchfab CC, Poly Haven) para objetos y sitios: ya
  estaban bien listados en la biblia (carrito de herramientas, carritos
  médicos, HDRI de hospital/garaje). No hacía falta repetir esa consulta.

### Punto 15 · Vestuario, con hex REALMENTE medidos

La biblia anterior decía «sin medir, hex a ojo» en los tres personajes. Aquí
se midieron con Pillow (muestreo de píxel, ignorando el fondo transparente) y
con `herramientas/estilo.py` (paleta por clúster de color) sobre **imágenes
oficiales bajadas**, cada hex con el método y la imagen de origen:

| Personaje / prenda | Hex medido | Cómo se midió | Fuente | Estado |
|---|---|---|---|---|
| Baymax, vinilo blanco (base) | `#F2F3F5` | Pillow (píxel del pecho, alfa>200) + estilo.py (31.8% del render) | [Baymax Render.png](https://static.wikia.nocookie.net/disney/images/0/05/Baymax_Render.png), 1280×1403 | ✅✅ |
| Baymax, vinilo en sombra (cálido, no azul) | `#DAD5D4` | Pillow (brazo, máx. diferencia rojo-azul) + estilo.py (15.3%) | mismo archivo | ✅✅ — **corrige** el `#C9CFD6` (frío) de la biblia anterior: la sombra real es beige-rosada, no azulada |
| Ojos y raya de la cara | `#000000` | Pillow (pupila, negro puro) | mismo archivo | ✅ |
| Armadura de Baymax, rojo-naranja | `#DD4630` – `#ED512D` | Pillow (póster) + estilo.py (13.6-20.4% en dos renders distintos) | [póster](https://static.wikia.nocookie.net/disney/images/c/ca/Big_Hero_6_poster_2.jpg) y [render de vuelo](https://static.wikia.nocookie.net/disney/images/b/b2/Baymax_Inflight_Render.png) | ✅✅ — **corrige** el `#C4252B` (muy oscuro/puro) de antes: el rojo oficial es más anaranjado |
| Armadura de Baymax, acento morado (hombro/muslo/puño) | `#8E7380` – `#926996` | Pillow + estilo.py, mismas dos imágenes | mismos archivos | ✅✅ |
| Hiro, sudadera azul marino (de calle) | `#3B3D5C` | Pillow (póster, parche de 8×8 px) | [póster, 1985×2835](https://static.wikia.nocookie.net/disney/images/c/ca/Big_Hero_6_poster_2.jpg) | ✅ (una imagen, pero medida en dos zonas de la sudadera con el mismo resultado) |
| Hiro, camiseta roja | `#DB2C2B` / `#D73B2B` | Pillow + estilo.py, mismo póster | mismo archivo | ✅✅ (dos métodos, mismo resultado) |
| Hiro, pantalón cargo caqui | `#7B5836` | Pillow (póster) | mismo archivo | ✅ |
| Hiro, armadura — traje (no el casco) | `#3C355D` (azul-morado oscuro) | estilo.py (9.3% del render) | [Hiro Armor Render.png, 1280×1366](https://static.wikia.nocookie.net/disney/images/7/7d/Hiro_Armor_Render.png) | ✅ — más morado que el `#1E1E24` casi negro que decía la biblia |
| Hiro, casco de la armadura | `≈#8B447A` (violeta, con reflejos que lo aclaran a magenta) | Pillow (zona de sombra del casco) | mismo archivo | ⚠️ una sola zona medida; el casco cambia mucho de tono con la luz (de morado a casi rosa en el reflejo) |
| Tadashi, gorra + chaqueta (traje de calle alternativo, hoja de modelo 2015) | gorra `#5A5A5A` gris oscuro, chaqueta con capucha oliva-gris `#636C72`/`#6E7266`, playera gris `#52575C`, pantalón marrón, bolso granate `#7C595C` | Pillow (hoja de modelo oficial) | [Tadashi and Go Go character model.jpg, 1024×1225](https://static.wikia.nocookie.net/disney/images/3/32/Tadashi_and_Go_Go_character_model.jpg) | ⚠️ es una **hoja de modelo de 2015 para la serie**, no el look de la película (gorra negra lisa + chaqueta verde militar cerrada, visto en fotogramas oscuros de la peli: [Hiro Tadashi fist bump.jpg](https://static.wikia.nocookie.net/disney/images/0/04/Hiro_Tadashi_fist_bump.jpg)); no se pudo medir el verde de la peli porque las escenas donde sale son nocturnas/con luz de color |

**Lo icónico que todos reconocen** (confirmado viendo las imágenes, no de
memoria): Baymax blanco redondo sin armadura; Hiro con la sudadera azul
marino y el pelo despeinado; la gorra negra de Tadashi (aunque su color
exacto de película no se pudo medir por la iluminación de esas escenas).

### Punto 16 · Ciudades, paisajes y fondos de pantalla

- **Wallhaven, con tamaño y autor reales** (API `wallhaven.cc/api/v1/search?q=baymax`,
  18 resultados con la etiqueta «baymax», antes la búsqueda automática no
  encontró nada aquí):

| Wallpaper | Tamaño | Autor (usuario) | Favoritos | Enlace |
|---|---|---|---|---|
| BH6 team, ciudad de noche | 4096×1716 | quanleloi | 48 | [wallhaven.cc/w/0jojkw](https://wallhaven.cc/w/0jojkw) |
| Baymax/Hiro | 3000×2084 | quanleloi | 30 | [wallhaven.cc/w/49yw21](https://wallhaven.cc/w/49yw21) |
| Baymax (fan art, muy grande) | 16000×9000 | dominomd | 21 | [wallhaven.cc/w/4yzk7g](https://wallhaven.cc/w/4yzk7g) |
| Baymax 4K | 3840×2160 | (usuario borrado) | 21 | [wallhaven.cc/w/0j1qpy](https://wallhaven.cc/w/0j1qpy) |

  Todos con `purity: sfw` (aptos) ✅. El de 16000×9000 es fan art (no oficial):
  se usa sólo de referencia de composición, no para imprimir.
- Los enlaces de alphacoders/WallpaperAccess/HDQwalls que ya traía la biblia
  siguen siendo válidos (los abrí, siguen activos), pero **esos sitios no dan
  autor**, sólo etiquetan «fondo de la película»: quedan en ⚠️ para el
  crédito, ✅ para el tamaño (ya lo decían: 3840×2160).
- **Fondos «reales» ligados al mundo** (no wallpapers de fans, sino fotos del
  atractivo temático «The Happy Ride with Baymax»): ver punto 23, sirven
  también para ambientar San Fransokyo en Blender (luz, color del entorno de
  parque temático inspirado en la peli).

### Punto 19 · Texturas 2D (nuevo)

- **Trama de manga (halftone)**: en la página de muestra del capítulo 0 (ver
  punto 1) el fondo detrás de Baymax es un degradado de puntos grises (trama
  de screentone clásica), usado para dar «peso» emocional a la viñeta; los
  globos son ovalados con borde negro fino y la onomatopeya «ばっ» (gesto
  brusco) está dibujada a mano con líneas de velocidad ✅ (vista directamente,
  [archivo, 1000×1436](https://static.wikia.nocookie.net/disney/images/2/22/Baymax-manga-preview-ch-0.jpg)).
  Para replicar la trama en Photoshop: filtro *Color Halftone* o un patrón de
  puntos (no hay que instalar nada); como imagen de referencia real sirve
  directamente esta página.
- **Textura de fieltro/parche cosido**: el «Wappen Hiro & Baymax» (punto 1)
  tiene el borde de cada parche con puntada visible en zigzag — buena
  referencia si la lámina usa una insignia o parche de tela para el canal.
- **Texturas libres equivalentes (CC0, ambientCG, con licencia incluida)**:
  - Vinilo/plástico liso de Baymax → [Plastic013A](https://ambientcg.com/view?id=Plastic013A),
    [Plastic010](https://ambientcg.com/view?id=Plastic010) (CC0).
  - Grano de papel (para el manga o cartelas impresas) →
    [Paper006](https://ambientcg.com/view?id=Paper006),
    [Paper001](https://ambientcg.com/view?id=Paper001) (CC0).
  - Tela de la sudadera de Hiro → [Fabric081C](https://ambientcg.com/view?id=Fabric081C),
    [Fabric061](https://ambientcg.com/view?id=Fabric061) (CC0).
  - Metal cepillado (armadura de Baymax, microbots) → [Metal063](https://ambientcg.com/view?id=Metal063),
    [Metal049A](https://ambientcg.com/view?id=Metal049A) (CC0).
  Todo confirmado por su propia API (`ambientcg.com/api/v2/full_json`), CC0
  sin excepción (es la licencia de todo el banco) ✅.
- **Logos y emblemas vistos** (para la capa de «marca» del canal): el logotipo
  de película «BIG HERO 6» en rojo sobre blanco con tipografía redondeada
  gruesa (visible en todos los pósters, hoja_01); el icono/parche pequeño en
  el pecho de Baymax (un óvalo con una muesca, el sensor de salud, visible en
  `Baymax_Render.png`); no encontré un escudo o crest independiente de «San
  Fransokyo Institute of Technology (SFIT)» como archivo suelto — sólo
  aparece bordado en la gorra de Tadashi dentro de fotogramas oscuros, ver
  «No encontré».
- No hace falta duplicar aquí las texturas **reales** de sitios (punto 4:
  hormigón, madera, vinilo hinchable) — ya están en la sección 6 de la
  biblia y no son de mi punto.

### Punto 23 · Colaboraciones y cruces (nuevo)

**Videojuegos y apps** (todos confirmados en el cuadro oficial «games» de la
ficha de Baymax en `disney.fandom.com`, wikitexto vía API — una sola tabla,
pero cada título contrastado con una segunda fuente cuando hacía falta):

| Colaboración | Qué trae para la lámina | Fuente(s) |
|---|---|---|
| **Disney Infinity 1.0-3.0** | figura física jugable de Baymax (foto real en hoja_01 #14, peana redonda con el logo del juego) | ✅✅ [ficha Baymax](https://disney.fandom.com/wiki/Baymax) + [Videogaming Wiki](https://videogaming.fandom.com/wiki/Baymax) |
| **Kingdom Hearts III** (2019) | mundo San Fransokyo; Sora vuela sobre Baymax con armadura; ya estaba en la biblia (punto 11), aquí se enlaza como referencia de **pose de vuelo cruzada** | ✅✅ ya confirmado antes |
| **Disney Emoji Blitz** | icono chibi redondeado de Baymax (app de puzzle) | ✅ [logo, 1198×732](https://static.wikia.nocookie.net/disney/images/7/74/Emoji_Blitz_Logo.png) (hoja_06 #218) |
| **Disney Heroes: Battle Mode** | arte de Hiro estilo RPG con iconos de habilidad (Megabot Call, Microbot Stun) — vocabulario de skills reutilizable en textos del bot | ✅ visto en hoja_06 (#204, #205) |
| **Disney Lorcana — set «Azurite Sea»** (nov-2025) | cartas ilustradas nuevas de Hiro Hamada, Baymax (la versión con armadura es «Legendary Rare»), GoGo, Wasabi, Fred y la tía Cass, con frases propias en la carta («The treatment is working», «We could be immortals») | ✅✅ [Bleeding Cool, anuncio](https://bleedingcool.com/collectibles/big-hero-6-arrives-for-disney-lorcana-azurite-sea-exclusive-reveal/), [Bleeding Cool, mazo inicial](https://bleedingcool.com/games/tabletop/card-games/disney-lorcana/disney-lorcana-azurite-sea-big-hero-6-starter-deck-saves-the-day/), cartas vistas en hoja_05 (#214-216, 222, 228-229, 233) |
| **Fortnite — «Hero Baymax»** (Chapter 6, temporada «Hunters», 1-dic-2024) | traje jugable + mochila «Megabot» + pico «Microbot Mallet»: el crossover más reciente y más reconocible para jugadores jóvenes del server | ✅✅ [Fortnite Wiki](https://fortnite.fandom.com/wiki/Hero_Baymax), [GosuGamers](https://www.gosugamers.net/entertainment/news/73869-godzilla-is-stomping-into-fortnite-chapter-6-with-big-hero-6-s-baymax) |
| **Disney Sorcerer's Arena** | Baymax e Hiro jugables, farmeables en nodos de evento | ✅✅ [wiki del juego](https://disney-sorcerers-arena.fandom.com/wiki/Big_Hero_6), [notas de contenido oficiales](https://www.sorcerersarena.com/news/content-update-8-27/) |
| **Disney Star Smash** (sólo Japón, nov-2020) | personajes de BH6 en un juego cooperativo de «romper bloques»; manga episódico propio dentro del juego | ✅✅ [Siliconera](https://www.siliconera.com/new-disney-mobile-game-star-smash-launched-in-japan/), tarjetas de personaje vistas en hoja_05/06 |
| Otros vistos en la misma ficha oficial (sin verificar cada uno aparte, listados por Disney mismo) | *Big Hero 6: Battle in the Bay*, *Baymax Blast*, *Disney Crossy Road*, *Tsum Tsum*, *Disney Magical Dice*, *Disney Magic Kingdoms*, *Disney Epic Quest*, objeto en *Roblox*, *Disney Getaway Blast*, *Disney Mirrorverse*, *Disney Speedstorm*, *Disney Solitaire*, *Disney Pixel RPG*, cameo en *Twisted Wonderland* | ⚠️ una sola fuente (la ficha oficial), no se abrió cada juego por separado |

**Atracciones y presencia real** (parques Disney — sirven de referencia de
**escala y volumen** para un Baymax 3D del canal):
- **«The Happy Ride with Baymax»**, atracción giratoria en Disney California
  Adventure y Shanghai Disneyland, listada en el campo oficial «rides» de la
  ficha de Baymax junto con *Gardens of Wonder*, *World of Color* y varios
  espectáculos nocturnos con proyecciones de Baymax ✅
  ([ficha Baymax, wikitexto](https://disney.fandom.com/wiki/Baymax)).
- **Fotos reales de Baymax como personaje ambulante** (mascota con actor
  dentro, no fan cosplay): turista con el personaje en Disney's Hollywood
  Studios (hoja_04 #78-79), estatua/figura de Baymax en un evento (hoja_06
  #156, #262 «Gardens of Wonder», Disneyland Paris) ✅ — sirven de referencia
  de **proporciones reales** (qué tan grande es Baymax junto a una persona)
  para un prop 3D en Blender.

**Cosplay bien hecho (materiales y volumen reales)**:
- Construcción en foam EVA con plantillas descargables: **«Baymax 2.0 Armor
  — with foam template files»** (comunidad The RPF, foro de props):
  materiales = foam EVA + pistola de calor para curvar + pegamento caliente,
  sellado con PVA y varias capas de Plasti Dip antes de pintar, acabado
  brillante con spray ✅
  ([enlace](https://www.therpf.com/forums/threads/baymax-2-0-armor-with-foam-template-files.234327/)).
- **«Baymax from Big Hero 6 Costume»** (Instructables, 7 pasos, el traje
  blanco inflable completo) y **«Hiro RIDING Baymax»** (disfraz de dos
  personas, Hiro «montado» sobre un Baymax de cuerpo completo) ✅
  ([Baymax](https://www.instructables.com/Baymax-from-Big-Hero-6-Costume/),
  [Hiro riding Baymax](https://www.instructables.com/Hiro-RIDING-Baymax/)).
- Ya estaba en la biblia el «Baymax mecha» de LEGO/POP MART armado en
  YouTube — sigue siendo la mejor referencia de volumen por bloques.

**Figuras oficiales** (pose = referencia 3D directa, ninguna es fan-made):
- **Funko Pop! Disney #111 y #112**, Baymax de 6″ (oct-2014), con variante
  perlada y una **Nurse Baymax brillante en la oscuridad** (exclusiva de
  Amazon) y una **Diamond Collection** de 6″ (exclusiva Hot Topic) ✅✅
  ([Funko oficial, Pop! Super Baymax with Mochi](https://funko.com/pop-super-baymax-with-mochi/84445.html),
  [ficha comparativa, Cardboard Connection](https://www.cardboardconnection.com/2014-funko-pop-disney-big-hero-6-vinyl-figures)).
- Figuras de Disney Infinity, Vinylmation de Hiro y figuras de acción
  articuladas («BH6 - Blast Flying Baymax figure», «Hirostealth figure», «BH6
  - Hiro action figure») ✅ (vistas en las hojas, tamaños en `indice.json`).

## Lo mejor para la lámina

1. Hex reales de Baymax (`#F2F3F5` con sombra cálida `#DAD5D4`) y de Hiro
   (sudadera `#3B3D5C`, camiseta `#DB2C2B`) — ya no hace falta adivinar.
2. La hoja `hojas/colaboraciones_01.jpg` (figuras oficiales, cartas Lorcana,
   iconos de apps) sirve para un concepto de lámina «Baymax de repisa, con
   sus versiones coleccionables» en #soporte.
3. «The Happy Ride with Baymax» + las fotos reales del personaje a tamaño
   humano dan la proporción exacta para un Baymax en 3D dentro del canal.
4. El disfraz de foam EVA (The RPF) es la mejor referencia de **cómo se ve
   la superficie de Baymax bajo luz real** (brillo tras varias capas de
   Plasti Dip): ayuda a calibrar el *shader* en Blender.
5. La página de muestra del manga (trama de puntos + globo ovalado) es una
   textura lista para enmarcar la «tabla del dolor» como si fuera una viñeta.

## No encontré

- ⚠️ Autor confirmado de los wallpapers de alphacoders/WallpaperAccess (sólo
  Wallhaven da usuario por su API; los otros sitios no lo publican).
  Búsquedas: `site:wallhaven.cc api baymax`, revisé las páginas de
  alphacoders directamente, sin dato de autor.
- ⚠️ Un logo o escudo suelto de «San Fransokyo Institute of Technology
  (SFIT)» como archivo descargable: sólo aparece bordado en la gorra de
  Tadashi, en fotogramas oscuros de la película (no se pudo medir su color
  exacto). Búsquedas: `intitle:SFIT`, `intitle:crest`, `intitle:emblem` en la
  wiki de Disney (`list=search&srnamespace=6`), sin resultado; búsqueda web
  «San Fransokyo Institute of Technology logo official» sin una imagen
  vectorial oficial suelta.
- ⚠️ «Patrones de ropa» (punto 19): la ropa de Hiro, Baymax y Tadashi es de
  color plano, sin estampado ni cuadros — no hay un patrón de tela que
  replicar más allá de la trama de tejido (ya cubierta con las texturas de
  ambientCG). No es que falte buscar: la propia ropa no lo tiene.
- ⚠️ Un café temático dedicado a Big Hero 6 (a diferencia de otras franquicias
  Disney): búsqueda «Big Hero 6 themed cafe» sin resultados específicos, sólo
  eventos genéricos de Disney Store.
- ⚠️ Los colores reales de los pines de la escala Wong-Baker en el pecho de
  Baymax (verde/amarillo/rojo): YouTube pide iniciar sesión desde este
  servidor; no encontré el clip exacto en Dailymotion ni en Internet Archive
  en el tiempo de esta tanda. Queda igual que en la biblia: confirmado que es
  la escala Wong-Baker (con aviso de licencia), sin ver el detalle de color.
- ⚠️ Verificación de un segundo autor para el fan art de Pixiv/DeviantArt ya
  listado en la biblia (Catel23, Brandon Lawless): sus páginas no traen un
  segundo enlace de autor que las confirme fuera del sitio.

## Bitácora de búsqueda (esta pasada)

- **Wiki de Fandom (API, sin buscador)**: `disney.fandom.com/api.php` —
  `imageinfo` para 14 archivos concretos (tamaño y URL real), `parse&prop=wikitext`
  de la página «Baymax» completa (lista oficial de juegos y atracciones),
  `list=search&srnamespace=6` para «Tadashi cap» (sin resultado).
- **Sketchfab** (API, sin buscador): `api.sketchfab.com/v3/search?q=baymax&downloadable=true`
  — 8 resultados con licencia por modelo.
- **Wallhaven** (API, sin buscador): `wallhaven.cc/api/v1/search?q=baymax&purity=100`
  (18 resultados) y `wallhaven.cc/api/v1/w/<id>` para 4 de ellos (tamaño y
  autor reales).
- **ambientCG** (API, sin buscador): `ambientcg.com/api/v2/full_json?type=Material&q=<plastic|paper|fabric|metal>`.
- **Buscador web** (inglés, 6 búsquedas de las ~50 permitidas):
  `"Big Hero 6" Baymax "Disney Lorcana" card set`,
  `"Big Hero 6" Baymax Funko Pop figure official`,
  `"Big Hero 6" Baymax Fortnite OR crossover collaboration cafe`,
  `Baymax cosplay costume tutorial materials foam`,
  `"Disney Star Smash" mobile game Big Hero 6 Tadashi`,
  `"Disney Sorcerer's Arena" Baymax Hiro Big Hero 6 character`,
  `Big Hero 6 manga Haruki Ueno Yen Press Kodansha volumes`.
- **Imágenes miradas de verdad** (`Read`, no sólo descargadas): las 7 hojas de
  contacto completas (299 miniaturas), más 12 imágenes oficiales sueltas en
  tamaño grande para medir color (`baymax_render.png`, `baymax_armor.png`,
  `baymax_inflight.png`, `hiro_armor.png`, `hiro_suit.png`, `poster2.jpg`,
  `tadashi_gogo.jpg`, `hiro_concept2.jpg`, `sft.jpg`, `manga_preview.jpg`,
  `wappen.jpg`, `tadashi_fistbump.jpg`, `tadashi_hat.jpg`).
- **Medición de color**: Pillow (muestreo de píxel con máscara alfa) y
  `herramientas/estilo.py --colores 6` sobre 5 de esas imágenes.

**Parte terminada**: los puntos 1, 3, 15, 16, 19 y 23 están cubiertos con lo
obligatorio del encargo (fuentes, tamaños, hex medidos, licencias). No queda
`Sigue:` — lo único pendiente está en «No encontré» y es opcional (SFIT
crest suelto, pines de la escala Wong-Baker, autor de wallpapers de
alphacoders, café temático).
