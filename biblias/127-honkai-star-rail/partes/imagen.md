# Imagen · Honkai: Star Rail (encargo 127)

Investigador de imagen. Puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md. Libreta de
datos: un dato por línea, con fuente, ✅ (dos fuentes) o ⚠️ (una), y minuto o
tamaño si aplica.

## 1 · Arte oficial, en cantidad y variado

- Splash art de personaje (fondo verde/campo de estrellas, pose de acción, sin
  UI): March 7th (Preservation) 2048×2048, Kafka 2048×2048, Trailblazer (F) y
  (M) Destruction 2048×2048, Firefly 2048×2048 · fuente: wiki de Fandom,
  galería del personaje · ✅ (imagen vista y medida con Pillow) · 2048×2048 px.
- Retrato «Game» de cuerpo entero sobre fondo degradado azul (el que se ve al
  invocar/subir de nivel): March 7th, Kafka, Trailblazer (F) y (M) · mismo
  origen · ✅ · 1000×1778 px.
- Arte de banner de invocación («splash» de anuncio de personaje nuevo), con
  el personaje en pose de portada y su ícono de Camino/elemento en la esquina:
  Nessun Dorma (Kafka, varias fechas 2023-2026), Indelible Coterie (March 7th
  y otros), A Lost Soul, Words of Yore, Ripples Rejoined, Swirl of Heavenly
  Spear (Jing Yuan), To Evermore Burn as the Sun (Phainon), Firefull Flyshine
  (Firefly) · fuente: wiki, categoría de banners · ✅ · 1200×675 px cada una.
- Key visual de aniversario (arte grupal, todo el elenco principal en pose de
  celebración, fondo del Astral Express o del logo): «Honkai Star Rail 1st
  Anniversary.png» (abr-2024), «2nd Anniversary.png» (abr-2025), «3rd
  Anniversary.png» (abr-2026) · fuente: https://honkai-star-rail.fandom.com/wiki/File:Honkai_Star_Rail_3rd_Anniversary.png
  · ✅ (las tres en la wiki, con fecha por el nombre de archivo) · 1024×1024 px
  cada una.
- Arte de portada de tienda (Steam/PS5/App Store), banners de lanzamiento
  («Honkai: Star Rail Launches Today — Next Stop, the Universe!», «Departing
  on Schedule on April 26th») y logo oficial en varios idiomas (inglés,
  japonés, coreano, chino simplificado y tradicional) · fuente: wiki, sección
  de logos e imágenes de la web oficial · ✅ (archivo + descripción coinciden).
- Hoja de contacto propia (32 imágenes grandes de la wiki: splash arts, retratos
  de juego y banners de evento) hecha con `investigar_serie.py` · guardada en
  `hojas/personajes_01.jpg` (ver «Lo mejor para la lámina»).
- Fan art más votado por personaje (Safebooru, con enlace y autor de origen:
  Twitter/X o Pixiv) ya está en `datos-imagen.md` (punto 3, no se repite aquí).
- ⚠️ No confirmé si hay un artbook físico oficial en español o si sólo circula
  el «Honkai: Star Rail Collector's Edition Art Book» en inglés (Reddit y
  tiendas lo mencionan, no encontré ficha oficial de HoYoverse con el índice).

## 3 · Fan art y renders 3D con licencia

_(pendiente)_

## 15 · Vestuario

_(pendiente)_

## 16 · Ciudades, paisajes y fondos de pantalla

_(pendiente)_

## 19 · Texturas 2D

_(pendiente)_

## 23 · Colaboraciones y cruces

_(pendiente)_

## Lo mejor para la lámina

_(pendiente)_

## No encontré

_(pendiente)_

## Bitácora

- 2026-09-26 · `herramientas/recolectar.py 127-honkai-star-rail --hojas` (previo, ya en datos-imagen.md): AniList no aplica (es videojuego), Doblaje Wiki no encontró la página, Fandom no encontró «el Trazacaminos» (el nombre correcto en la wiki en inglés es «Trailblazer»).
- 2026-09-26 · `investigar_serie.py --serie "Honkai: Star Rail" --wiki honkai-star-rail --paginas "March 7th" "Kafka" "Trailblazer" "Stelle" "Firefly"`: 232 imágenes enlazadas, 32 grandes, 1 hoja de contacto → mirada con Read.
- 2026-09-26 · Fandom API (`action=query&list=search`, `prop=images`, `prop=revisions`) en inglés: aniversarios, banners, categoría de trajes alternativos.
- 2026-09-26 · Pillow/`estilo.py` sobre recortes de torso de los retratos «Game» (sin fondo de UI) para el hex de la ropa, no del fondo.

Sigue: puntos 3, 15, 16, 19, 23 completos; Lo mejor para la lámina; No encontré; hojas/ (elegir 2 más); referencias.json.
