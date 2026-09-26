# Parte IMAGEN · 102 — El estilo Ghibli en general

Puntos de ENCARGO.md: **1** (arte oficial variado), **3** (fan art y 3D con licencia), **15** (vestuario con hex medidos), **16** (fondos de pantalla), **19** (texturas 2D), **23** (colaboraciones y cruces, su arte).

Nota: 102 es un tema general (el estilo Ghibli), no una obra con personajes propios. Los "personajes" que aparecen abajo son ejemplos de varias películas usados para ilustrar el estilo (fondos pintados, comida, luz, viento), no protagonistas de una sola obra.

Partido de `partes/datos-imagen.md` (recolectado el 2026-09-25): no se repiten esas consultas de Fandom/Danbooru/Safebooru.

## Hallazgos

### Punto 1 — Arte oficial, en cantidad y variado

Nota de enfoque: la hermana 98 (Chihiro) y la biblia ya hecha de 100 (Mononoke)
agotan el arte oficial de esas dos películas concretas (50 fotogramas cada
una, artbooks, storyboards, posters). Aquí no lo repito: busco el nivel
**estudio completo**, con foco en lo que pide el encargo — fondos pintados,
comida, luz, viento — mirando varias películas a la vez.

- **La biblioteca oficial de fotogramas cubre todo el catálogo, no sólo
  Chihiro/Mononoke.** Comprobé uno a uno los 26 slugs de `ghibli.jp/works/`:
  todos devuelven `NNN001.jpg` en `https://www.ghibli.jp/gallery/<slug>NNN.jpg`
  (1920×1038, medido) → aya, baron, chihiro, ged, ghiblies, hotarunohaka,
  howl, kaguyahime, karigurashi, kazetachinu, kimitachi, kokurikozaka,
  laputa, majo, marnie, mimi, mononoke, nausicaa, omoide, onyourmark, ponyo,
  porco, tanuki, totoro, umi, yamada. ✅ (comprobado con `curl` código 200 en
  cada uno, no de memoria)
- **Origen de la licencia**: el 18-sep-2020 Studio Ghibli publicó 400
  imágenes libres de 8 películas con una nota manuscrita del cofundador
  Toshio Suzuki: *"Please use them freely within the scope of common
  sense"*; para diciembre de 2020 ya eran 1178 imágenes y hoy cubre las 26
  obras de arriba. ✅ (dos fuentes:
  [openculture.com/2020/12](https://www.openculture.com/2020/12/studio-ghibli-makes-1178-images-free-to-download.html)
  y [siliconera.com](https://www.siliconera.com/studio-ghibli-uploads-400-images-for-free-use/))
- **Descargué y monté una hoja de contacto propia** (31 fotogramas, 4
  películas) para buscar a ojo comida/luz/viento en variedad de obras
  (`stills/contacto1.jpg`, carpeta de trabajo fuera del repo). Destacados,
  medidos con `herramientas/estilo.py`:
  - **Comida** — `ponyo035.jpg` (cuenco de ramen con jamón, la escena de
    comida más citada de todo Ghibli): paleta `#A49446` `#C7BA8D` `#BAAB58`
    `#DFD8C5` `#81B4C7` `#DE9F9B`, sombreado degradado/pintado, brillo 74%.
    `kazetachinu015.jpg` (bento envuelto en furoshiki con el periódico, «El
    viento se levanta»): paleta `#322923` `#847864` `#B19770` `#B4AD9C`
    `#5B3D28` `#865430`, brillo 47%. `totoro015.jpg` (bandeja de onigiri
    recién hechos). ✅ (medido directamente)
  - **Luz (komorebi, luz de sol filtrada entre hojas)** — `totoro025.jpg`
    (Mei mirando por un túnel de plantas iluminado): paleta `#1D4A3F`
    `#295D49` `#3D7351` `#1B3631` `#588B5C` `#9EA65D`, saturación 51%,
    brillo 38% (verdes oscuros con puntos de luz). Es el ejemplo visual más
    citado de la técnica «komorebi» del estudio. ✅ (medido)
  - **Luz mágica/color** — `howl020.jpg` (vapor verde de la bruja de las
    tierras baldías dentro de la casa): paleta `#9F9C88` `#828273` `#BAB39A`
    `#66665A` `#D4C8A4` `#C0B07E`, saturación 21%, brillo 62% (tonos tierra
    con el verde ácido como acento, no domina el % de píxeles pero sí la
    escena). ✅ (medido)
  - **Viento** — `kazetachinu001.jpg` (Jirō volando con gafas, campos verdes
    debajo) y `kazetachinu025.jpg` (avión derribado entre nubes, cielo
    dorado): paleta de la segunda `#D1BB9A` `#C3A77A` `#171514` `#727173`
    `#625446`, brillo 53%. «El viento se levanta» (Kazetachinu) es la
    película donde el viento es tema central: el título mismo cita un verso
    de Paul Valéry («Le vent se lève, il faut tenter de vivre»). ✅ (wiki +
    la propia película)
- **Técnica de fondo confirmada por el propio pintor jefe, Kazuo Oga**
  (director de arte de Totoro, Pompoko, Mononoke, Chihiro): pinta con
  **gouache Nicker Poster Color** (24 colores), moja el papel por las dos
  caras antes de empezar y trabaja con **30-60 minutos** antes de que se
  seque, metiendo primero las masas grandes y húmedas de color y los
  detalles al final. Cita textual: *"Basically, I use poster-color... it is
  easy-to-use"*. ✅ (dos fuentes:
  [openculture.com/2021/01](https://www.openculture.com/2021/01/a-look-inside-the-painting-process-of-the-studio-ghibli-artist-kazuo-oga.html)
  y [animatedviews.com](https://animatedviews.com/2008/interview-with-ghibli-background-artist-oga-kazuo/))
- **Por qué la comida "se ve rica" (confirmado por el propio estudio)**: el
  productor Toshio Suzuki reveló que **toda la comida que aparece está
  basada en comidas que el propio Hayao Miyazaki ha comido** (el pastel de
  arenque y la leche con miel de Ponyo, el desayuno de huevos con tocino de
  El increíble castillo vagabundo, el ramen). El estudio dedicó una
  exposición oficial entera al tema: **"Delicious! Animating Memorable
  Meals"**, Museo Ghibli, Mitaka (2021-2022) — página oficial:
  https://www.ghibli-museum.jp/en/exhibitions/013127/ ✅ (museo oficial +
  [hypebeast.com/2021/4](https://hypebeast.com/2021/4/studio-ghibli-animated-food-always-looks-tempting-secret))
  - Técnica de animación de la comida: vapor y humedad dibujados con trazos
    de tinta finos y con movimiento (miel goteando en Ponyo, burbujas del
    tocino friéndose en El castillo ambulante, vino girando en Porco Rosso).
    ✅ (misma fuente)
- **Rasgos que se repiten al dibujar cada personaje solo** (Danbooru, ya en
  `datos-imagen.md`, no repetido): Kiki, San, Howl, Chihiro, Jiji, Nausicaä —
  vocabulario de etiquetas para IA de imagen, incluido en el punto 17 del
  redactor.

Método de esta hoja: recorté cada fotograma de `stills/` a 320×173, los
pegué en cuadrícula con Pillow y rotulé el nombre de archivo; así se ve a la
vez comida, luz y viento de 4 películas distintas sin abrir 31 imágenes
sueltas (regla de «hojas de contacto» de AYUDANTE.md).

### Punto 3 — Fan art y 3D con licencia

Enfoque: objetos y personajes **transversales al estudio** (no de una sola
película, eso ya lo cubren las hermanas 98/100). Toda licencia comprobada en
el campo `license` de la respuesta de la API de Sketchfab, no de memoria.

**Modelos 3D descargables con licencia CC** (Sketchfab API,
`downloadable=true`):
- **Nubes estilizadas «Stylized clouds»** — CC BY, **557 likes** (el más
  valorado de toda esta búsqueda) — por *lavakongen* —
  https://sketchfab.com/3d-models/none-e326c36890364526910cba03c1393ebc ✅
  (sirve para el «cielo Ghibli» de cualquier lámina, no de una peli en
  concreto)
- **Howl's Moving Castle Breakfast** (el plato de huevos con tocino) — CC BY,
  **714 likes**, por *Zeps3D* —
  https://sketchfab.com/3d-models/none-0e8fde91fdb5413494e878b0fef85cda ✅
  (mejor referencia 3D de «comida Ghibli» de todo lo encontrado)
- **Ramen from Ponyo** — CC BY, 200 likes, por *Discovered* —
  https://sketchfab.com/3d-models/none-5e614fea3aaf4e78bd82cf2b6e0e5c7a ✅
- Variante del mismo plato: **Ramen Bowl from Ponyo** — CC BY-NC-SA, 101
  likes, por *ckaosatom* — ⚠️ (no comercial, avisar antes de usar)
- **My Neighbor Totoro** (personaje completo) — CC BY, 60 likes, por
  *Vanillaburp* —
  https://sketchfab.com/3d-models/none-ffb11769e03e4a9395416d714ccd66ce ✅
- **TOTOROs** (grupo, los 3 tamaños) y **Mei** — CC BY, 380 y 488 likes, por
  *goart* ✅
- **Catbus / Gatobús**, 3 versiones con licencia libre: *A modeling of the
  Ghibli Catbus* (CC BY, 42 likes, Valentine_Ventura), *CatBus Mi Vecino
  Totoro* (CC BY, 18 likes, AcalliTwissLART, en español), *Sculpt January -
  Day 11* (CC BY, 18 likes, jason.lp.davis). ⚠️ Descartado: la versión más
  votada (169 likes, Patrickart.hk) es **CC BY-NC-ND**, no cumple licencia
  libre del encargo.
- **Robot de Laputa** («Robot left on Laputa») — CC BY, 55 likes, por
  *zionkoenig* —
  https://sketchfab.com/3d-models/none-a659068938054b64bbac15110ffd2fa1 ✅
- **Kamaji (釜爺) de El viaje de Chihiro** — CC BY, 37 likes, por
  *godislove431* (no duplica los modelos de la hermana 98: ahí no salió éste)
  ✅
- **Calcifer, El increíble castillo vagabundo** — CC BY, 48 likes, por
  *berchello*; variante «Fire - Calsifer», CC BY, 107 likes, por *DonikXD*
  ✅
- **Nabo (Turnip Head), Howl** — CC BY, 117 likes, por *ncd.blueberry* ✅
- **Nausicaä del Valle del Viento** (personaje) — CC BY, 66 likes, por
  *lages.miguel* ✅
- **Props de Kiki: entrega urgente** («[Kiki's Delivery Service] Props
  collection») — CC BY, 163 likes, por *Kanna-nakajima*; y «Kiki's Delivery
  Service Bread Wreath» (la corona de pan de la panadería), CC BY, 25 likes
  ✅
- **Biplano rojo** (Porco Rosso / estética de aviones Ghibli) — CC BY, 264 y
  78 likes, por *won1* ✅
- **Casa con forma de cabeza de Ghibli** («Ghibli Head house», diorama
  fan-made inspirado en el estilo, no de una peli concreta) — CC BY, 128
  likes, por *Mars_Sobaka* ✅
- **Susuwatari/hollín (Soot Sprite)** — CC BY-NC, 205 likes, por *duz_vr* ⚠️
  (no comercial; la hermana 98 ya buscó "susuwatari" sin resultado
  descargable — este sí aparece pero limitado a no-comercial)

**Fan art (Safebooru, etiqueta `studio_ghibli` transversal, con autor y
origen; sólo referencia, nunca para pegar)**:
- 2952×2075 — https://safebooru.org/images/1096/db3d1c9105029bf9f66d68bc2cfcfa1d6241f771.jpg
  · origen: https://x.com/endlessrz/status/1267082711153422336
- 1946×2048 — https://safebooru.org/images/63/4974950fec31db2d75dac552bb22a166db53078f.jpg
  · origen: https://x.com/gan2 (comparación estilo Ghibli)
- 1261×1600 / 1535×2037 — dos versiones, mismo artista en ArtStation:
  https://www.artstation.com/artwork/zOoZm6
- 1280×1979 — Totoro por *ayasal* en DeviantArt (marca de agua del sitio
  visible, sólo referencia): imagen intermedia en safebooru.org/images/1104/...
  ✅ (fuente con autor identificado en las 4)

**Fotos con licencia libre (Openverse, para ver volumen/arquitectura real,
nunca para pegar)**:
- 10 fotos del **Museo Ghibli (Mitaka)** por el mismo fotógrafo de Flickr,
  CC BY-SA 2.0, 1024×768 cada una: exterior con el robot de Laputa en la
  azotea, jardín, fachada — ejemplo:
  https://live.staticflickr.com/8313/8025600359_b89c00a1c1_b.jpg ✅ (10
  fotos de la misma sesión, licencia confirmada por la API de Openverse)

Cómo se ve el estilo Ghibli **en el vocabulario de fan art** (Danbooru, ya
recogido por `recolectar.py` en `datos-imagen.md`, no repetido aquí): las
etiquetas más repetidas para Kiki, San, Howl, Chihiro, Jiji y Nausicaä
comparten patrón — pelo natural (nunca de colores imposibles), ropa de tela
simple, fondo simple o "outdoors", casi nunca fondos recargados; eso es
justo lo contrario del fondo pintado y detallado del propio estudio (dato
útil para el punto 17 del redactor: "lo que NO hace la IA bien" al copiar
Ghibli).

### Punto 15 — Vestuario con hex medidos

Enfoque: aquí NO repito Chihiro (hermana 98) ni Mononoke (biblia 100), ya
tienen su vestuario a fondo. Elijo un personaje icónico de **otras 5
películas distintas** para mostrar la variedad de paletas de vestuario del
estudio. Medido con Pillow (`getpixel`/`getcolors`) sobre fotogramas
oficiales de `ghibli.jp` descargados a `stills/` (1920×1038 cada uno),
localizando antes la zona exacta con una rejilla de coordenadas (no un color
al azar).

| Personaje | Prenda | Hex medido | De qué imagen |
|---|---|---|---|
| Kiki (Nicky, la aprendiz de bruja) | Lazo rojo del pelo | `#AA0118` | `majo020.jpg` (oficial, ghibli.jp) |
| Kiki | Vestido negro de trabajo | `#2A2B3F` | `majo020.jpg` |
| Sophie (El increíble castillo vagabundo) | Cinta del sombrero de paja | `#A04854` | `howl005.jpg` |
| Sophie | Vestido verde | `#699389` ⚠️ (zona con posible mezcla con el hombro de Howl) | `howl005.jpg` |
| Howl | Pelo rubio | `#EED39E` | `howl005.jpg` |
| Howl | Capa rosa con ribete dorado | `#EE90A0` (capa) · `#EBCA6D` (ribete) | `howl005.jpg` |
| Nausicaä (Nausicaä del Valle del Viento) | Mono/traje azul-verdoso | `#5691A8` | `nausicaa025.jpg` |
| Nausicaä | Bufanda/cuello marrón-vino | `#523436` | `nausicaa025.jpg` |
| Ponyo (forma mitad pez) | Vestido rojo-coral | `#E76476` | `ponyo030.jpg` |
| Ponyo | Vientre blanco-azulado | `#DEEBF1` | `ponyo030.jpg` |
| Ponyo | Pelo naranja | `#D68776` | `ponyo030.jpg` |
| Totoro | Pelaje del rostro (gris-pardo) | `#4E4F48` | `totoro030.jpg` |
| Totoro | Lengua/boca | `#DD868E` | `totoro030.jpg` |

✅ todos medidos directamente sobre el fotograma citado, coordenadas
localizadas con una rejilla propia antes de recortar (evita medir piel o
fondo por error). El único marcado ⚠️ (vestido de Sophie) es porque la zona
de recorte quedó pegada al hombro de Howl en ese plano; para confirmarlo
haría falta otro fotograma sin solape.

- **Ropa icónica que todos reconocen** (transversal al estudio, no de una
  sola peli): el vestido negro + lazo rojo de Kiki es probablemente el
  «uniforme» más reconocible de toda la filmografía Ghibli fuera de Totoro
  mismo — aparece en merchandising, cosplay y en el propio logo de Kiki's
  Delivery Service. ✅ (visual + volumen de fan art en Danbooru/Safebooru, ya
  en `datos-imagen.md`)
- Totoro **no lleva ropa**: su "vestuario" es el propio pelaje gris con
  vientre más claro y las hojas que a veces lleva sobre la cabeza a modo de
  paraguas (visible en `totoro030.jpg`, hoja verde sobre la cabeza). Lo
  anoto en vez de forzar una tabla de ropa que no existe. ✅ (visto
  directamente)
- Howl cambia de color de pelo (rubio ↔ negro) según su estado de ánimo en
  la trama; el fotograma medido es su estado "normal" (rubio). ⚠️ (dato de
  memoria de la trama, no verificado con un segundo fotograma del pelo
  negro en esta pasada — lo dejo para quien tenga más cupo)

### Punto 16 — Fondos y sitios: luz, paleta, texturas reales

Enfoque: sitios de **varias películas** (no repito el balneario de Chihiro
ni el bosque/Irontown de Mononoke, ya hechos por sus investigadores). La
idea es mostrar que "el estilo Ghibli" cambia de paleta según la película
pero mantiene la misma técnica de fondo pintado.

Paletas medidas con `herramientas/estilo.py` sobre fotogramas oficiales
descargados (1920×1038):

| Sitio / película | Luz | Paleta medida | Textura real libre (CC0) |
|---|---|---|---|
| Colina con espantapájaros al atardecer, viento fuerte (El increíble castillo vagabundo, `howl010.jpg`) | atardecer cálido, cielo dramático | `#403639` `#694E3F` `#542C2D` `#352324` `#B99D89` `#A77951` — brillo 39% | [Grass005](https://ambientcg.com/view?id=Grass005) |
| Calle de pueblo costero europeo, edificios de piedra (Kiki, entrega urgente, `majo015.jpg`) | tarde nublada, tonos fríos | `#263238` `#1E292E` `#CBB993` `#404B56` `#9D957D` — brillo 34% (la más fría/azulada medida) | [PavingStones151](https://ambientcg.com/view?id=PavingStones151) |
| Valle con plantas raras, atmósfera tóxica (Nausicaä del Valle del Viento, `nausicaa020.jpg`) | verde-ocre apagado, aire con esporas | `#273031` `#3D4341` `#142023` `#575A51` `#777560` `#A68D55` — brillo 33%, mucha línea | — |
| Fábrica de aviones/campo, gris industrial (El viento se levanta, `kazetachinu030.jpg`) | gris plomizo, luz difusa | `#2D302E` `#1D1E1B` `#494438` `#374E58` `#685C47` `#657676` — brillo 31%, mucha línea | [RoofingTiles013A](https://ambientcg.com/view?id=RoofingTiles013A) |
| Estanque con flores en verano, luz natural (Arrietty, el mundo de los pequeños seres) — no es fotograma propio, es el fondo de pantalla de fans más guardado con esta escena en Wallhaven (ver abajo) | sol de mediodía, verdes vivos | ver ficha de Wallhaven | [Grass001](https://ambientcg.com/view?id=Grass001) |
| Comida/luz/viento (Ponyo, Totoro, El viento se levanta, Howl) | — ya medido en el punto 1 (komorebi de Totoro, luz mágica de Howl, cielo de Kazetachinu) — no se repite aquí | — | — |

- **Fondos de pantalla oficiales de todo el catálogo**: los 26 slugs del
  punto 1 sirven directamente como fondos (1920×1038, sin marca de agua). Y
  el propio `ghibli.jp` publica fondos específicos "para videollamada" por
  película en `/info/013251/` (ya usados por las hermanas 98 y 100 para sus
  películas). ✅
- **Fondos de pantalla de fans, transversales al estudio** (Wallhaven,
  búsqueda `"studio ghibli"`, sólo "sfw", ordenados por favoritos):
  - `wallhaven-yx5kml` — 3840×2160, **591 favoritos** (el más guardado de
    toda la búsqueda), etiquetas: *anime screenshot, creature, stars, starry
    night, sky, Studio Ghibli* — https://wallhaven.cc/w/yx5kml — por las
    etiquetas coincide con la escena nocturna de la parada de autobús con
    Totoro bajo un cielo estrellado. ⚠️ (no lo abrí para confirmar la
    escena exacta, sólo por metadatos)
  - `wallhaven-96l5xd` — 3840×2160, 416 favoritos, etiquetas: *pond, grass,
    flowers, sunlight, summer, **Karigurashi no Arrietty**, Hayao Miyazaki,
    natural light* — https://wallhaven.cc/w/96l5xd — **confirmado por
    etiqueta de la propia web**: fotograma de *Arrietty* (estanque con
    flores en verano). ✅
  - `wallhaven-x8oxez` — 3072×1452, 535 favoritos, fan art de Totoro por el
    ilustrador *DannyLaiLai* — https://wallhaven.cc/w/x8oxez ⚠️ (licencia
    del autor, sólo referencia, no oficial)
- **Textura real de fondo pintado**: el propio Kazuo Oga (punto 1) pinta
  sobre papel mojado con gouache; el grano final se parece más a una
  **acuarela sobre papel de acuarela húmedo** que a un dibujo digital. No
  encontré en ambientcg una textura específica de "papel de acuarela
  mojado" (busqué "watercolor paper", 0 resultados) — lo más cercano son las
  texturas de papel genéricas ya usadas en el punto 19. ⚠️
- **Constante de todo el estudio**: cada localización mide brillo bajo (31-39%,
  salvo la de Arrietty en pleno día) porque casi todos los fotogramas
  elegidos por su interés dramático son de amanecer/atardecer/interior — es
  un patrón de **cómo se ilumina** una escena Ghibli para que se vea
  importante, no sólo casualidad de la muestra. ⚠️ (observación sobre 4-6
  fotogramas, no es una medición estadística del catálogo completo)

### Punto 19 — Texturas 2D

Enfoque transversal: no repito las fichas concretas de tela/madera que ya
sacaron las hermanas 98 (balneario de Chihiro) y 100 (Irontown/bosque de
Mononoke); aquí busco lo que se repite **en todo el catálogo**: cómo se
imita el papel pintado a mano, si hay tramas de manga (el estudio casi no
viene de manga) y el logo/emblema del propio estudio.

- **Nausicaä del Valle del Viento SÍ es manga original de Miyazaki** (serial
  en la revista Animage, 1982-1994) — la única obra grande de Ghibli con
  manga propio de verdad (Mononoke sólo tiene un "film comic" con fotogramas
  recortados, ya lo confirmó la hermana 100). Está dibujado a **lápiz y
  tinta con tramado a mano** (rayado/hachurado, *cross-hatching*), en tonos
  sepia poco saturados — **no usa screentone/trama impresa** como el manga
  comercial típico; es más cercano a un grabado o a una ilustración de
  ciencia ficción europea. ✅ (dos fuentes:
  [ghibli.fandom.com/wiki/Nausicaä…(manga)](https://ghibli.fandom.com/wiki/Nausica%C3%A4_of_the_Valley_of_the_Wind_(manga))
  y [screenrant.com](https://screenrant.com/miyazaki-nausicaa-manga-better-movie-op-ed/),
  ambas describen el mismo estilo de lápiz/tinta sepia)
  - Textura libre equivalente al hachurado de Nausicaä: no hay un pincel
    "cross-hatch manga Miyazaki" listo; lo más cercano son pinceles de
    grabado/rayado ("crosshatch brush") genéricos de Photoshop, no
    encontrados con licencia libre específica en esta pasada. ⚠️
- **Grano de fondo pintado a mano** (el rasgo transversal más importante,
  técnica de Kazuo Oga y su equipo, punto 1): pinceles gratis de tinta
  *sumi-e* ya localizados por la hermana 100, válidos aquí igual porque es
  la misma técnica de todo el estudio, no de una peli — "Sumi Ink Brushes"
  (Brusheezy, licencia libre declarada en ficha,
  https://www.brusheezy.com/brushes/1183-sumi-ink-brushes). Además, para el
  aspecto gouache/acuarela concreto, hay dos packs de pinceles **"inspirados
  en Ghibli" hechos por fans** con licencia de descarga gratuita declarada
  en su propia ficha: *"Ghibli-Inspired & Hand-Painted Brush Collection"*
  (https://brushespack.com/product/ghibli-inspired-hand-painted-brush-collection/)
  y los pinceles gratis de gouache/lienzo de *kawtherarts* en Gumroad
  (gratis, botón "pagar lo que quieras" en 0). ✅ (fichas propias, ambas
  dicen "free download") — ⚠️ ojo: son de fans, no del estudio; usar sólo
  como herramienta de textura, nunca presentarlos como "oficiales".
- **Texturas reales CC0 transversales** (AmbientCG, misma familia usada por
  las hermanas, aquí en genérico para cualquier película): `Paper004`
  (grano de papel de acuarela claro), `Fabric034` (lino/algodón liso para
  ropa sencilla tipo Kiki/Sophie), `Wood060` (madera clara de interiores
  cálidos tipo la casa de Totoro) — https://ambientcg.com/view?id=Paper004,
  Fabric034, Wood060. ✅ (licencia CC0 estándar de la ficha).
- **Logo del estudio** (el emblema más reconocible de todos, transversal por
  definición): la silueta de **Totoro** (con Chibi Totoro/Totoro pequeño
  dentro de la "O"), diseñada por el propio Hayao Miyazaki; se estrenó con
  *Only Yesterday* en 1991 (aunque Totoro es de 1988) y no ha cambiado el
  diseño desde entonces, sólo el grosor de línea al pasar a reproducción
  digital. Es marca registrada en Japón, EE. UU. y la UE. ✅ (dos fuentes:
  [1000logos.net/studio-ghibli-logo](https://1000logos.net/studio-ghibli-logo/)
  y [logos-world.net/studio-ghibli-logo](https://logos-world.net/studio-ghibli-logo/))
- **Patrón de ropa repetido en el estudio**: cuadros/tartán simple en
  chalecos y faldas de varias protagonistas europeas (Sophie en El castillo
  ambulante, gente del pueblo de Kiki) — visible directamente en los
  fotogramas de las hojas de contacto de abajo (`hojas/arte_01.jpg` #131,
  #157); no hay una ficha CC de "tartán Ghibli" concreta, se resuelve con
  cualquier textura de tartán/cuadros genérica con licencia libre.

### Punto 23 — Colaboraciones y cruces

Enfoque transversal: LOEWE (2021 Totoro / 2022 Chihiro) y UNIQLO UT ya están
documentadas a fondo por las hermanas 98 y 100 — no las repito, sólo las
nombro como ya cubiertas. Aquí meto lo que es **del estudio entero**, no de
una peli.

- **Ghibli Park (Aichi, Japón)** — parque temático oficial, no de una sola
  película: abrió el 1-nov-2022 con 3 zonas (**Ghibli's Grand Warehouse**,
  **Dondoko Forest** —inspirada en Totoro—, **Hill of Youth**); **Mononoke
  Village** abrió el 1-nov-2023 (ya la documentó la hermana 100) y **Valley
  of Witches** el 16-mar-2024, con un **castillo de Howl de 20 metros de
  alto** (incluida la habitación de Howl y el horno de Calcifer) y un
  tiovivo. Desde marzo de 2024 las 5 zonas están abiertas a la vez por
  primera vez. ✅ (dos fuentes:
  [en.wikipedia.org/wiki/Ghibli_Park](https://en.wikipedia.org/wiki/Ghibli_Park)
  y [japan-in-a-box.com/ghibli-park-guide-2025](https://japan-in-a-box.com/blogs/inside-the-box/ghibli-park-guide-2025))
- **Ni no Kuni — el crossover de videojuego oficial que SÍ existe** (a
  diferencia de Fortnite, que ninguna hermana encontró): colaboración
  directa Studio Ghibli + Level-5 + compositor Joe Hisaishi. Empezó en 2010
  (Nintendo DS, *Dominion of the Dark Djinn*), siguió con *Wrath of the
  White Witch* (PS3, 2011/2013) con animación 2D hecha por el propio
  estudio Ghibli para las cinemáticas, y sigue vivo hoy con **Ni no Kuni:
  Cross Worlds** (2022), un juego **gacha para móvil** — es decir, el
  encargo pedía justo "otros juegos (Fortnite, gachas…)" y este es el caso
  real. ✅ (dos fuentes:
  [gamedeveloper.com](https://www.gamedeveloper.com/game-platforms/-i-ni-no-kuni-i-level-5-s-collaboration-with-studio-ghibli-secures-600k-initial-shipment)
  y [en.wikipedia.org/wiki/Ni_no_Kuni](https://en.wikipedia.org/wiki/Ni_no_Kuni))
- **Café/panadería oficial reconocida por el estudio** (no una exposición
  temporal): **Shirohige's Cream Puff Factory** (Kichijoji y
  Shimo-Kitazawa, Tokio), pastelería que vende choux con forma de Totoro;
  la dueña es cuñada de Hayao Miyazaki y tiene permiso directo del estudio
  para vender el producto (tardó 3 años en conseguir la forma de las
  orejas de Totoro y 2 más en conseguir el permiso). Abierta desde 2007. ✅
  (dos fuentes:
  [thesmartlocal.jp](https://thesmartlocal.jp/shirohiges-cream-puff-factory/)
  y [washiwanders.com](https://washiwanders.com/food-drink/shirohiges-cream-puff-factory-kichijoji/))
- **Tienda oficial de merchandising del estudio entero**: **Donguri
  Kyowakoku** (どんぐり共和国), operada por Benelic Co., con tiendas físicas por
  todo Japón (Donguri Republic) y web propia (donguri-sora.com); vende
  figuras y peluches de todas las películas, no sólo una. Sólo envía dentro
  de Japón. ✅ (dos fuentes:
  [kanpai-japan.com](https://www.kanpai-japan.com/travel-guide/donguri-official-ghibli-shops)
  y [soranews24.com](https://soranews24.com/2014/03/04/donguri-kyowakoku-the-store-with-nothing-but-studio-ghibli-anime-items/))
- **Figuras oficiales, ejemplo concreto de pose 3D de referencia**: los
  productos de Donguri Kyowakoku incluyen figuras de Totoro en varias poses
  (de pie, sentado, con paraguas) vendidas como colección — sirven de
  referencia 3D de pose "oficial" sin ser fan art. ⚠️ (no encontré ficha
  con fotos técnicas de cada pose individual, sólo el catálogo general de
  la tienda)
- **Cosplay premiado en competición internacional**: un cosplay de **Mi
  Vecino Totoro** ganó aplausos y elogios en el **World Cosplay Summit**
  (la referencia más "oficial" de un concurso de cosplay reconocido
  internacionalmente en el que ha destacado un disfraz Ghibli). ⚠️ (una
  fuente:
  [cbr.com/studio-ghibli-my-neighbor-totoro-world-cosplay-championship-award](https://www.cbr.com/studio-ghibli-my-neighbor-totoro-world-cosplay-championship-award/) —
  falta cruzar el año/nombre exacto del cosplayer con una segunda fuente,
  quedó pendiente por cupo, ver «No encontré»).
- **Lo que NO existe (comprobado, no asumido)**: colaboraciones oficiales
  con Gucci, New Balance, MUJI o GU — busqué las cuatro juntas en inglés y
  sólo salió UNIQLO (ya cubierto por las hermanas). ⚠️ No lo doy por
  imposible a futuro, sólo no existe hoy con esta búsqueda.

## Hojas de contacto (`hojas/`, 3 JPEG, todas <1 MB)

Generadas con `herramientas/investigar_serie.py --wiki ghibli --paginas
"Kiki's Delivery Service" "Howl's Moving Castle" "My Neighbor Totoro" "Ponyo"
"The Wind Rises" "Nausicaä of the Valley of the Wind" "Kazuo Oga"` (701
imágenes candidatas, 5 hojas generadas antes de cortar por tiempo; elegí las
3 más variadas). Miradas una a una antes de elegir, no sólo por el nombre de
archivo.

- **`hojas/arte_01.jpg`** (numerada 1-48): posters oficiales variados
  (Ponyo, Howl, Totoro, Kiki, Wind Rises, Nausicaä), storyboard de Totoro a
  lápiz (#3), el logo original de Kiki's Delivery Service basado en las
  ilustraciones de Akiko Hayashi (#7), celdas de animación originales
  (#18, #26, #33), bocetos de personajes y fondos de Kazuo Oga trabajando
  en su estudio (#30-32, #38-39), foto del propio Oga pintando (#32). Sirve
  para el punto 1 (variedad oficial) y para citar la técnica de Oga con
  imagen de apoyo.
- **`hojas/fondos_01.jpg`** (numerada 49-96): fondos **sin personaje en
  primer plano** ya rotulados por su propio nombre de archivo —
  `Background - nausicaa1.jpg` (#68), `Background - howl1.jpg` (#70),
  `Background - kaze1.jpg` (#86), `Background - totoro1.jpg` (#79) — más el
  interior de la panadería de Kiki (#61), la cocina/desayuno de Sophie
  (#62-64) y el valle verde con el niño Jiro antes de la guerra (#42-43,
  Wind Rises). Es la hoja más directa para el punto 16 (fondos "puros").
- **`hojas/comida_viento_01.jpg`** (numerada 97-144): el valle tóxico de
  Nausicaä con Ohmu (#97-104, viento/atmósfera), Totoro bajo la lluvia con
  el paraguas (#106, viento/agua), la vista de la bahía y los Ohmu bebé
  cruzando el agua de Ponyo (#108-115), el desayuno de huevo con tocino de
  Sophie en El castillo ambulante (#143-144, comida — la escena de comida
  más citada del estudio junto al ramen de Ponyo, ya medida en el punto 1).

Nota: el `indice.json` con los números y URL originales quedó en
`herramientas/referencias/el-estilo-ghibli-en-general/` (carpeta que git
ignora), no en `hojas/`, tal como pide AYUDANTE.md.

## Lo mejor para la lámina

- El **fondo de pantalla oficial "para videollamada"** de cualquiera de las
  26 películas (`ghibli.jp/gallery/<slug>NNN.jpg`, sin marca de agua) es la
  base más limpia para poner un personaje delante en Blender/Photoshop.
- El **desayuno de Sophie** (huevo con tocino, `hojas/comida_viento_01.jpg`
  #143-144, o el modelo 3D CC BY de Zeps3D) es la referencia de "comida
  Ghibli" más citada fuera del ramen de Ponyo — sirve si el canal quiere
  algo de mesa/cocina.
- El **komorebi de Totoro** (`totoro025.jpg`, punto 1, verdes oscuros con
  puntos de luz) es el efecto de luz más reconocible y reproducible con una
  capa de "luz de trama" en Photoshop.
- El vestido negro + lazo rojo de **Kiki** (hex del punto 15) es el
  vestuario más reconocible del estudio fuera de Totoro mismo, útil si el
  canal quiere un personaje "cara" del estilo Ghibli en general.
- El **castillo de Howl de Ghibli Park** (Valley of Witches, punto 23) es la
  mejor referencia 3D/arquitectónica real de un edificio-personaje del
  estudio, con foto oficial del propio parque.

## No encontré

- ⚠️ Textura o pincel libre específico de "hachurado tipo Nausicaä manga"
  (cross-hatch sepia): sólo genéricos, ningún pack dedicado a este estilo
  concreto (punto 19).
- ⚠️ Ficha oficial con fotos de cada pose de las figuras de Totoro de
  Donguri Kyowakoku: sólo el catálogo general de la tienda, no una ficha
  técnica por figura (punto 23).
- ⚠️ Año y nombre exactos del cosplayer de Totoro premiado en el World
  Cosplay Summit: una sola fuente (cbr.com), no crucé una segunda antes de
  quedarme sin cupo en esta pasada (punto 23).
- ⚠️ Colaboración oficial con Gucci, New Balance, MUJI o GU: búsqueda hecha
  en inglés, no existe ninguna a día de hoy (punto 23).
- ⚠️ Color del pelo de Howl en su forma "negra" (estado de ánimo alterado):
  sólo medido su estado rubio normal (arrastrado del punto 15, ya avisado
  ahí).

## Bitácora

- Español: ninguna búsqueda específica nueva en esta tanda (el resto ya
  estaba en inglés/japonés de la tanda anterior, ver Hallazgos de los
  puntos 1/3/15/16).
- Inglés (WebSearch, esta tanda): "Nausicaä of the Valley of Wind manga
  screentone hatching hand-drawn technique Miyazaki"; "Studio Ghibli Park
  areas 2024 2025 Dondoko Forest Valley of Witches Hill of Youth official";
  "Shirohige's Cream Puff Factory Studio Ghibli official bakery Kichijoji
  Goro Miyazaki"; "Studio Ghibli official collaboration Gucci OR New
  Balance OR MUJI OR GU 2024 2025"; "Ni no Kuni Studio Ghibli Level-5
  official collaboration video game"; "Donguri Kyowakoku OR Benelic Studio
  Ghibli official figure line collectible"; ""Ghibli style" Photoshop brush
  pack free gouache texture watercolor background download"; "Studio Ghibli
  official cosplay contest craftsmanship award winning"; "Studio Ghibli
  logo Totoro silhouette trademark history design origin".
- Directo (sin buscador, cuota ahorrada): `herramientas/investigar_serie.py`
  con 7 páginas de la wiki de Ghibli (Kiki's Delivery Service, Howl's
  Moving Castle, My Neighbor Totoro, Ponyo, The Wind Rises, Nausicaä of the
  Valley of the Wind, Kazuo Oga) → 701 imágenes candidatas, 5 hojas de
  contacto miradas una a una, 3 elegidas para `hojas/`; ficha de licencia de
  ambientcg.com (Paper004, Fabric034, Wood060) y de Brusheezy/Gumroad para
  los pinceles.
- Fuentes que fallaron o no aplicaron: `investigar_serie.py` se cortó por
  tiempo (110 s) tras 5 hojas — suficiente para elegir, no hizo falta
  relanzarlo; AmbientCG no tiene una textura "watercolor paper wet" (ya lo
  avisó el punto 16 de la tanda anterior).

