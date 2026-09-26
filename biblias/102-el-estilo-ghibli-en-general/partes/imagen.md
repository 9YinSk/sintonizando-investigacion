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

(pendiente)

### Punto 15 — Vestuario con hex medidos

(pendiente)

### Punto 16 — Fondos y sitios: luz, paleta, texturas reales

(pendiente)

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
