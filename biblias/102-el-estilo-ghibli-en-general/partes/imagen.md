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

(pendiente)

### Punto 23 — Colaboraciones y cruces

(pendiente)

## Lo mejor para la lámina

(pendiente)

## No encontré

(pendiente)

## Bitácora

(pendiente)

Sigue: llenar todos los puntos (1, 3, 15, 16, 19, 23) desde cero.
