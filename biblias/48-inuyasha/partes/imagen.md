# Parte de IMAGEN · Inuyasha (encargo 48)

Puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md. Libreta de datos: un dato por línea,
fuente con enlace, ✅ (dos fuentes) o ⚠️ (una), minuto o tamaño si aplica.
Partida de `partes/datos-imagen.md` (recolectar.py, 2026-09-25): esos datos no
se repiten aquí, sólo se comprueban y se amplían.

## 15 · Vestuario: colores hex medidos, accesorios y qué es «lo icónico»

Colores medidos con `herramientas/estilo.py` (Pillow, cuantización de la imagen ya
compuesta sobre blanco cuando traía transparencia) o con muestreo directo de
píxel sobre la imagen bajada; la ficha exacta de cada imagen va en la última
columna. Son aproximados a la iluminación de esa imagen concreta, no un
«color oficial» de licencia.

Personaje | Prenda | Hex medido | De qué imagen
---|---|---|---
Inuyasha | Haori/kosode rojo (piel de Rata de Fuego), la prenda «icónica» que todo fan reconoce | #BE2A28 (tela), #5C2B26 (sombra/pliegues) | `Inuyasha_and_shippo.png` (wiki, 1440×1080) ✅
Inuyasha | Piel | #DBC09A | misma imagen
Kagome Higurashi | Uniforme escolar «sailor fuku»: falda y cuello | #068D5A (verde) | `Kagome_Vector.png` (wiki, vector oficial 800×3254, compuesto sobre blanco) ✅
Kagome Higurashi | Pañuelo/neckerchief | ≈#AC4F49 (rojo apagado por el antialiasing del vector; a ojo es un rojo más vivo, ver imagen) | misma imagen ⚠️ (un solo original, sin comprobar en fotograma)
Kagome Higurashi | Piel | #E8B28B / #FDE6CB | misma imagen
Sesshōmaru | Kimono blanco-crema base | #DEE6DF / #DBD8CE | `Sesshomaru.png` (wiki, 1920×1080) ✅
Sesshōmaru | Marca de luna creciente (frente) | #6458A1 (violeta azulado) | muestreo directo de píxel, misma imagen ✅
Sesshōmaru | Marcas de mejilla (dos rayas) | #933855 (magenta oscuro) | promedio de 2100 píxeles de la raya, misma imagen ✅
Sesshōmaru | Patrón del cuello del kimono (flor/cruz roja) | #5A2D33 | misma imagen
Miroku | Túnica de monje budista (kesa morado) | #352A3C, #261D33, #3F3348, #4C3D5D (degradado de sombra) | `Miroku_and_his_Shakujo.jpg` (wiki, 1280×720) ✅
Sango | Traje de exterminadora (bodysuit) | #1B0F0D (negro-marrón muy oscuro) | `Sango_Vector.png` (wiki, vector oficial 593×719, compuesto sobre blanco) ✅
Sango | Franjas/obi rojo y guanteletes | #BE3E30 | misma imagen
Sango | Sombra del traje | #5B3B3A | misma imagen

- Accesorios que se repiten en el arte oficial: el rosario de cuentas de Inuyasha (control del *sit*), el báculo *shakujō* y el *kazaana* envuelto de Miroku, el *Hiraikotsu* de hueso gigante de Sango, el arco y las flechas purificadoras de Kagome, el *Tessaiga*/*Bakusaiga* y la armadura de hombro con piel (*boa*) de Sesshōmaru · visibles en `hojas/personajes_01.jpg` (#2, #10, #28-30, #36, #58) · ✅
- Peinados icónicos: coleta alta de Miroku, cabello suelto blanco-plateado de Inuyasha y Sesshōmaru (con las marcas moradas/magenta de Sesshōmaru como único punto de color en la cara), coleta alta de Sango, pelo suelto oscuro de Kagome con flequillo recto · confirmado visualmente en las imágenes de arriba y en `hojas/personajes_01.jpg` #23-24 (primeros planos) ✅
- «Lo icónico» que todo fan reconoce: el haori rojo de Inuyasha (temporada tras temporada, casi no cambia de color aunque sí de textura entre anime 2000 y Final Act) y el uniforme escolar verde de Kagome, aunque ella cambie a kimonos de sacerdotisa en arcos puntuales (ver `Inuyasha_and_Kagome_artbook.jpg`, hoja #40) ⚠️ (dato de memoria de fandom, sin databook que lo cite explícitamente todavía)

## 3 · Fan art y renders 3D (referencia; nunca para pegar) y modelos 3D con licencia

- Fan art mejor valorado en Safebooru por personaje (Inuyasha, Kagome, Miroku, Sango), con tamaño y enlace al origen en Pixiv/Twitter/Zerochan cuando lo hay: ver bloque «Fan art mejor valorado» de `datos-imagen.md` (30 imágenes) · ✅ (Safebooru + origen enlazado)
- Modelos 3D de todo el elenco principal, con licencia **CC Attribution**, autor **deankagura** (Sketchfab): Inuyasha, Kagome, Sesshōmaru, Kikyō, Sango — ver `datos-imagen.md` (bloque Sketchfab) · ✅
- Modelo 3D de **Naraku** (postura de combate) y **Naraku (Casual)**, mismo autor, CC Attribution · https://sketchfab.com/3d-models/none-3312dfe1d19342feb6b68a7405524bf4 (♥21) y https://sketchfab.com/3d-models/none-a6b498884a8347f6ab523327029cbda5 (♥6) · ✅ (licencia visible en la ficha del modelo)
- Modelo 3D de **Kirara** en forma de gatita (kitten), CC Attribution, deankagura · https://sketchfab.com/3d-models/none-dec388ee3ae947e3a5a116a0f3cf1264 (♥13) · ✅
- **Tessaiga** (espada de Inuyasha) en dos modelos CC Attribution: «Tessaiga» de lvdagmil (♥24, https://sketchfab.com/3d-models/none-5e849d275acc40149b1a01694da420c7) y «Tesaiga Inuyasha (low)» de Ericks.Raphael.Effio.Lujan (♥27, ya en `datos-imagen.md`) · ✅
- **HDRI CC0 de Poly Haven «Bamboo Tunnel»** (túnel de bambú, luz de mediodía, natural), sirve de referencia real de iluminación y textura para los bosques de bambú del Sengoku que recorren los personajes · https://polyhaven.com/a/bamboo_tunnel · resoluciones hasta 16K · licencia CC0 · ✅ (ficha de Poly Haven, autoría Dimitrios Savva)
- No encontré modelo 3D con licencia libre de **Hiraikotsu** (el bumerán-hueso de Sango) ni de sitios recreados (el Árbol Sagrado, el pozo devora-huesos) en Sketchfab con `downloadable=true`: búsqueda «Hiraikotsu», «feudal japan village», «InuYasha well» sin resultados descargables ⚠️



- Portada del videojuego «InuYasha: Feudal Combat» (PS2, 2005, lucha por equipos, célula-shading) · https://static.wikia.nocookie.net/inuyasha/images/e/ef/Feudal-Combat.jpg (707×1000) · fuente: https://inuyasha.fandom.com/wiki/Feudal_Combat y https://en.wikipedia.org/wiki/Inuyasha:_Feudal_Combat · ✅
- Portada de «InuYasha: The Secret of the Cursed Mask» (PS2, RPG) · https://static.wikia.nocookie.net/inuyasha/images/d/db/The-Secret-of-the-Cursed-Mask.jpg (704×1000) · fuente: https://inuyasha.fandom.com/wiki/The_Secret_of_the_Cursed_Mask · ⚠️ (una fuente, wiki)
- Portada de «InuYasha: Secret of the Divine Jewel» (PS1, RPG por turnos) · https://static.wikia.nocookie.net/inuyasha/images/c/c2/Secret-of-the-Divine-Jewel.jpg (1000×898) · fuente: https://inuyasha.fandom.com/wiki/Secret_of_the_Divine_Jewel · ⚠️
- Portada de «The Art of InuYasha» (artbook oficial, Rumiko Takahashi, VIZ 2005; ilustraciones + comparación manga/anime + entrevistas al staff y seiyuu) · https://static.wikia.nocookie.net/inuyasha/images/3/39/The_Art_of_InuYasha.jpg (816×1000) · fuente: https://inuyasha.fandom.com/wiki/The_Art_of_InuYasha y https://www.goodreads.com/book/show/22703.The_Art_of_Inuyasha · ✅
- «The Art of Rumiko Takahashi: Colors 1978–2024» (Viz, artbook con Inuyasha entre sus 6 series, formato derecha-a-izquierda, entrevista larga a la autora) · https://www.amazon.com/Art-Rumiko-Takahashi-Colors-1978-2024/dp/1974756165 · ⚠️ (ficha de venta, no imagen medida)
- Ilustración nueva de Rumiko Takahashi para el relanzamiento Blu-ray HD 2020 de VIZ (16:9 remasterizado; incluye la versión 4:3 original) · https://www.cbr.com/inuyasha-hd-remaster-bluray/ y https://www.comingsoon.net/tv/news/1193589-original-inuyasha-anime-getting-hd-remaster-blu-rays-in-japan · ✅ (dos medios)
- Portada oficial y banner de AniList (key visual del anime) · https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx249-jVBkyLnBvnRE.png · https://s4.anilist.co/file/anilistcdn/media/anime/banner/249-9ufXhmXxncry.jpg · fuente: datos-imagen.md (AniList) · ✅
- 69 imágenes grandes (≥640 px) de las páginas de personaje de la wiki (portadas de tomo, hojas de modelo, cartelones, arte de capítulo) montadas en 2 hojas de contacto (`hojas/personajes_01.jpg`, `personajes_02.jpg`; ver índice más abajo) · fuente: https://inuyasha.fandom.com/wiki/Inuyasha y las fichas de Kagome, Sesshōmaru, Miroku, Sango (`herramientas/investigar_serie.py`) · ✅

**Índice de las hojas de contacto** (`hojas/personajes_01.jpg` = nº1-48, `personajes_02.jpg` = nº49-69; ver `herramientas/referencias/inuyasha/indice.json` para la URL de cada número):
- Poses vivas con arma: #2 Miroku lanzando el Kazaana, #10 Inuyasha desenvainando Tessaiga contra Sesshōmaru, #28-30 filo de Tessaiga en acción, #45 Inuyasha en su forma yōkai con Kagome abrazándolo.
- En grupo: #7 Kagome/Sango/Miroku, #16 Kagome y Kikyō, #26 Shippō a caballito de Miroku e Inuyasha, #37-39 la familia (Higurashi + InuKag + Sesshōmaru/Rin), #63 el grupo completo caminando.
- Portadas de manga (blanco y negro, para tramas del punto 19): #61 Chapter178-Cover, #62 Chapter117-Cover, #69 Chapter101-Cover, #59 y #64 páginas interiores con screentone visible.
- Objetos icónicos: #12 la tumba/pozo, #36 Tessaiga en la piedra, #58 Sacred Sutra de Miroku.

