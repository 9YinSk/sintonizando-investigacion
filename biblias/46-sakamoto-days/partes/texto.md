# Texto, juegos y técnica · Sakamoto Days

Investigador de texto, juegos y técnica (puntos 5, 6, 11, 18, 24, 25 de ENCARGO.md). Parte de
`partes/datos-texto.md` (recolectar.py, 25-sep-2026); no repite esas consultas, las comprueba y
profundiza. Sin serie hermana en este encargo (modo `nueva`). Punto 18: rigs y tramas → ver puntos 3 y 19
(los trae el investigador de imagen); aquí sólo cómo replicar el estilo en Photoshop y Blender.

## 5 · Tipografía: logo, globos, cartelas y letra libre

El logo oficial es un bloque muy grueso, mayúsculas condensadas casi sin curvas, con **una cara redonda
de gafas circulares sustituyendo la "O"** de SAKAMOTO y de DAYS (es la marca/mascota de la serie, se repite
en el logo de la wiki y en las portadas). Comprobado con fontTools: las 8 letras libres de abajo sí traen
tildes, ñ y ¿¡.

- Logo «SAKAMOTO DAYS»: mayúsculas negras muy gruesas, casi sin diferencia grosor/fino (display grotesca),
  con la «O» sustituida por una carita de gafas redondas · portada Weekly Shōnen Jump (`ch1_small.jpg`,
  mirada) y portada de tomo 9 (`vol9_small.jpg`, mirada) · ✅ (dos portadas oficiales distintas) · 900×656 y
  900×1410 px las capturas
- Bajo el logo inglés va siempre el título en katakana pequeño: サカモトデイズ, en una tipografía japonesa
  gótica (sans) simple, sin adornos · mismas dos portadas · ✅
- Letra libre para el logo (título, cartelas grandes): **Anton** (Google Fonts, OFL, con tildes/ñ/¿¡
  comprobado con fontTools) — misma familia de grosor extremo condensado; no lleva la carita, eso se dibuja
  aparte
- Letra libre alternativa más redondeada: **Titan One** (Google Fonts, OFL, con tildes/ñ/¿¡ comprobado)
- Onomatopeyas y gritos (見た así en las páginas: trazo de pincel negro grueso, ej. «触即発!!» en el
  capítulo 43) van directamente pintadas a mano, no con una fuente; la letra libre más parecida en trazo
  grueso de cómic occidental: **Bangers** (Google Fonts, OFL, con tildes/ñ/¿¡ comprobado) — sirve para un
  grito latino tipo «¡CUIDADO!»
- Globo normal / diálogo de manga: sin fuente oficial identificada (rotulado japonés estándar de Jump);
  letra libre equivalente usada en otras biblias del equipo para manga shonen: **Patrick Hand** (Google
  Fonts, OFL, con tildes/ñ/¿¡ comprobado) para un rotulado manuscrito limpio, o **Archivo Black** (Google
  Fonts, OFL, con tildes/ñ/¿¡ comprobado) para texto de cartel/letrero dentro de viñeta (ej. el rótulo
  «坂本» de la tienda en la portada del tomo 1)
- Pensamiento (Shin lee mentes: sus «voces» internas se dibujan como nubes/burbujas de pensamiento en el
  anime — confirmado en la ficha de personaje, «his mind-reading ability is depicted through thought
  bubbles», sin captura propia porque el fotograma lo cubre el investigador de vídeo) → letra libre:
  **Caveat** (Google Fonts, OFL, cursiva manuscrita, con tildes/ñ/¿¡ comprobado)
- Interfaz de videojuego (única obra jugable oficial: el puzle móvil japonés «SAKAMOTO DAYS デンジャラス
  パズル», sólo en Japón, no se pudo instalar ni capturar la UI real; ver punto 11) → letra libre genérica
  de videojuego retro/pixel para cualquier lámina que simule una pantalla: **Press Start 2P** (Google
  Fonts, OFL, con tildes/ñ/¿¡ comprobado)
- Subtítulos / créditos (letra de máquina, para una cartela tipo «informe de la JAA» o ficha de expediente
  de asesino): **IBM Plex Mono** en negrita (Google Fonts, OFL, con tildes/ñ/¿¡ comprobado)
- El japonés real del logo y las cartelas usa fuentes gót icas gruesas tipo Gothic (comprobado visualmente,
  no identificado el nombre exacto) → para textos japoneses libres en la lámina, la familia gratuita más
  usada en el equipo es **Noto Sans JP** (Google Fonts, OFL; cubre kanji, hiragana y katakana)

## 6 · Cómo hablan y piensan en pantalla (manga, cartelas, videojuego)

Sakamoto Days **no usa la burbuja blanca genérica** casi nunca fuera de las viñetas normales: los títulos
de capítulo son cartelas negras con letras amarillas, y el videojuego tiene su propio cuadro de diálogo
estilo *visual novel*, ninguno de los dos parecido a un globo de cómic occidental.

- **Cartela de título de capítulo** (portada de la revista, capítulo 2, «殺し屋商店始めました»): caja
  **negra de esquinas redondeadas**, letras **amarillas** gruesas verticales, con furigana pequeño en gris
  encima de cada kanji; una palabra clave suelta en **rojo** fuera de la caja para dar énfasis (ej. «尻」
  ・殺し屋» en rojo junto al título) · mirado en `ch2_small.jpg` (portada Weekly Shōnen Jump nº2) · ✅
- **Globo de diálogo normal**: óvalo de contorno fino negro (~2 px), sin relleno de color, cola corta y
  recta hacia quien habla; en la página de ejemplo mirada (capítulo 43) los globos aparecen en blanco
  porque es la versión sin letrar que usa la wiki para las miniaturas de capítulo, pero la **forma** del
  globo (óvalo apaisado, trazo fino) se ve igual de clara · `ch43_small.jpg` · ✅ (forma), ⚠️ (el texto
  real de esa página no se pudo leer, está vacío en la fuente)
- **Onomatopeya/efecto**: pincelada de tinta negra gruesa y angulosa, directamente sobre el dibujo, sin
  caja ni contorno (ej. «触即発!!», «on the verge of conflict», capítulo 43, escrita a mano encima de la
  acción) · `ch43_small.jpg` · ✅
- **Videojuego «Sakamoto Days: Dangerous Puzzle» (Sakapazu, sólo Japón)**, cuadro de diálogo de las
  escenas de historia (estilo *visual novel*), medido con Pillow en una captura oficial de Google Play:
  - Fondo de la caja de texto: **negro casi opaco `#1e1e1e`**, rectángulo redondeado en la parte baja de
    la pantalla, con esquinas verde neón marcando el marco (detalle de HUD, no de la caja en sí).
  - Placa del nombre: rectángulo redondeado **naranja-amarillo `#fecb00`**, arriba a la izquierda de la
    caja, con el nombre del personaje en negro y negrita (ej. «南雲», Nagumo).
  - El texto va en **blanco**, dos líneas, alineado a la izquierda, letra de trazo uniforme sin serifa.
  - Botón «スキップ» (saltar) arriba a la derecha, en una píldora oscura translúcida.
  - Fuente: captura propia (`playshots/c.jpg`, 288×512) de la ficha de Google Play · ✅ (medido con
    Pillow, un solo pantallazo — sin verificar en más de una escena)
- **Pantalla de equipo** (チーム編成, formación de equipo) del mismo juego: tarjetas de personaje con
  insignia de color por elemento (rosa corazón, azul gota, amarillo estrella) arriba a la izquierda,
  etiqueta «Lv.» y botón «詳細» (detalles) en rosa pastel `#f6d6ba`; fondo de pantalla degradado lila
  `#b88abd` · `playshots/b.jpg` · ✅ (medido)
- **Escena de historia con villano**: fondo con cinta de peligro amarilla y negra en diagonal (motivo de
  «escena de acero/atraco»), texto de impacto blanco con contorno, todo en mayúsculas gruesas tipo cartel
  de cine de acción · `playshots/a.jpg` · ✅
- **Qué NO hacer**: un globo blanco redondo con cola puntiaguda tipo cómic americano clásico; la serie usa
  óvalos finos sin relleno y cartelas negras con letra amarilla, nunca globos de colores vivos.

## 11 · Videojuegos de la franquicia: interfaz y cajas de diálogo

Una sola obra jugable oficial confirmada, japonesa y sólo para móvil; no hay juego de PC/consola (Steam
vacío en `datos-texto.md`, comprobado).

- **SAKAMOTO DAYS デンジャラスパズル (サカパズ)** — «Sakamoto Days Dangerous Puzzle», de GOODROID Inc.
  (subsidiaria de CyberAgent), estrenado el 2-abr-2025 en Japón, gratis con compras · ✅
  ([Google Play](https://play.google.com/store/apps/details?id=jp.co.goodroid.sakapuzz&hl=en_US),
  [CyberAgent, nota de prensa](https://www.cyberagent.co.jp/en/news/detail/id=31588))
- Mecánica: **puzle de combinar 3** (match-3) por colores para dañar enemigos, con combos y movimientos
  especiales; se arma un equipo con Sakamoto, Shin, Lu y otros personajes; la app sólo está en japonés
  (sin selector de idioma) · ✅ (Google Play + CyberAgent)
- Reparto de voces del juego **igual que el anime**: Tomokazu Sugita (Sakamoto), Nobunaga Shimazaki
  (Shin), Ayane Sakura (Lu), Nao Toyama (Aoi), Hina Kino (Hana), Ryota Suzuki (Heisuke), más Natsuki Hanae
  (Nagumo), Taku Yashiro (Kamihate/«Kamigami») y Saori Hayami (Osaragi) · ✅ (ficha de Google Play)
- El juego incluye **ilustraciones exclusivas** («ゲームオリジナルのイラスト», arte que no sale en el manga
  ni el anime, con historias cortas propias) — interesa como referencia de poses nuevas · ✅ (ficha), ⚠️
  no se pudo entrar al juego para ver el catálogo completo de ilustraciones
- Interfaz medida: ver punto 6 (caja de diálogo, pantalla de equipo). No se encontró interfaz de combate
  (el tablero de puzle en sí) en las capturas conseguidas · ⚠️
- **The Cutting Room Floor**: sin página del juego (`tcrf.net` da con Cloudflare un reto de verificación
  que no se pudo pasar, con `curl` y con `navegar.py`, dos intentos cada uno) · ❌ probé, no hay o no se
  pudo comprobar
- No hay más videojuegos de la franquicia (ni en Steam, ni anunciados para consola) a fecha de esta
  investigación (26-sep-2026) · ✅ (búsqueda en inglés y japonés, sin resultados)
