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

## 18 · Estilo de dibujo y técnica, y cómo replicarlo (Photoshop y Blender)

Rigs y tramas: ver puntos 3 y 19 (los trae el investigador de imagen). Aquí: línea, sombreado, filtros de la
animación, programas reales usados y cómo imitarlos con Photoshop y Blender, y encuadre/composición.

**Del manga (Yuto Suzuki), por entrevista de su editor Sousuke Ishikawa en MangaPlus** ✅
([mangaplus.shueisha.co.jp/web_pages/1293](https://mangaplus.shueisha.co.jp/web_pages/1293/)):
- Suzuki estudió **Nihonga** (pintura tradicional japonesa) antes de dedicarse al manga; de ahí su ojo para
  que cada plano tenga «una silueta que funciona» dentro de su encuadre, incluso en los cortes de acción
  detenida a media acción.
- Dibuja con **Clip Studio Paint** ✅ (confirmado también por él mismo en una entrevista especial de Jump
  GIGA 2023, resumida por Shonen Jump News: [x.com/WSJ_manga](https://x.com/WSJ_manga/status/1607079895108050944)).
- Su acción es «fácil de leer» a propósito: evita el encuadre de cámara complicado y busca **el instante en
  que arranca el movimiento** (el pico de la acción), no coreografías largas; por eso lo lee bien tanto
  público joven como adulto.
- Colecciona vídeos de referencia en Pinterest y ve cine y series constantemente para mantener el ojo
  actualizado.
- Influencias directas del propio autor: el manga **«Domu» de Katsuhiro Otomo** (lo que le hizo querer ser
  mangaka) y el cine de acción de sicarios de Hollywood, sobre todo **John Wick** y **The Equalizer** (de
  ahí el tono «asesino profesional, frío y elegante») ✅ (MangaPlus + resumen del tuit de Shonen Jump News).

**Del anime (TMS Entertainment), por entrevista al director Masaki Watanabe** ✅
([AWN](https://www.awn.com/animationworld/masaki-watanabe-talks-sakamoto-days),
[ScreenRant](https://screenrant.com/sakamoto-days-anime-problem-biggest-challenge-character-designs/)):
- Programas: **Clip Studio Paint** para el dibujo/animación y programas de **Adobe** (composición, tipo
  After Effects) para el acabado final · ✅
- **Filtro de «papel»**: la textura de papel/grano se extrae de las **zonas de sombra** del material de
  color original y se aplica sólo ahí, en la fase de **composición** (no en cada dibujo). La textura queda
  **fija** (no se mueve con el personaje ni la cámara) para no multiplicar el trabajo. Fue idea del director
  de fotografía, para dar más información visual reduciendo el número de líneas necesarias en la animación
  · ✅ (cita directa del director)
- Se nota más en las sombras bajo la barbilla y en los pliegues oscuros de la ropa; da un aire cálido y
  casero en escenas familiares y un aire denso en las de pelea · ✅
- **Precisión del diseño**: los personajes son «engañosamente simples» (sin marca vistosa tipo cicatriz o
  pelo de color), así que el reconocimiento depende de detalles finísimos —forma de la cara, tamaño de los
  ojos, **grosor exacto de la línea**—; un pequeño desvío rompe el parecido, así que el estudio revisaba
  constantemente para mantener el modelo · ✅ (ScreenRant, cita directa)
- **3D + rotoscopia**: la escena de la montaña rusa (episodio 3) se modeló primero en 3D, se animó, y
  luego se **rotoscopió** a mano; tardó el triple que una escena normal · ✅ (AWN, cita directa)
- El director quiere usar más **animación 3D como base** en futuros proyectos, sin sustituir a los
  animadores expertos, para sostener un nivel de dibujo constante · ✅ (AWN)
- Las armas se dibujan con intención **realista** (brillo del metal, filo visible) aunque el estudio se
  toma licencias de diseño por espectacularidad (ej. el rifle de Heisuke dispara a ráfagas, algo que un
  Mosin-Nagant real no hace) · ✅ (AWN, cita directa)

**Cómo replicarlo en Photoshop** (para un objeto o cartel de la lámina):
1. Línea limpia y de grosor **muy constante** (2-3 px a tamaño final), sin la variación gruesa/fina típica
   de otros shonen: usa el Lápiz o el Pincel con *Pen pressure* casi plano, o vectoriza con la herramienta
   Pluma; corrige cada curva a mano, porque aquí el parecido depende del contorno, no de un gesto suelto.
2. Sombra plana a **un solo tono** (cel-shading de 2 niveles: luz base + una sombra, sin degradado) en una
   capa `Multiply` recortada (clipping mask) sobre el color base.
3. **Filtro de papel**: crea una capa de textura de papel/grano (ver `ambientcg.com` tipo Paper001), ponla
   en modo `Multiply` o `Soft Light` al 15-25 % de opacidad, y recórtala (clipping mask) **sólo** sobre la
   capa de sombra, no sobre toda la ilustración. No la animes ni la distorsiones con el dibujo: en la serie
   se queda fija encima, como un cristal esmerilado.
4. Añade un leve grano/aberración cromática muy sutil en la capa de ajuste final (Filtro > Ruido, cantidad
   baja) para el aire de composición de vídeo, sin pasarse (la serie es limpia, no granulada al estilo
   found-footage).

**Cómo replicarlo en Blender** (para el objeto real en 3D que pide el punto 17/concepto de lámina):
1. Modela el objeto (pistola, caja registradora, letrero de la tienda) con geometría simple y **el
   modificador Line Art** de Grease Pencil (o Freestyle) para sacar un contorno limpio tipo manga
   directamente del render — es el mismo camino que usó el propio estudio (3D primero, luego se afina a
   mano).
2. Shader de 2 tonos: nodo `Shader to RGB` → `ColorRamp` con un corte duro (sin degradado) para imitar el
   cel-shading plano de la serie; nada de PBR realista salvo en las armas, donde sí conviene un metal con
   brillo especular marcado (según la propia serie, «un arma sin brillo pierde tensión»).
3. Si la pieza necesita movimiento o una pose difícil (algo articulado, no sólo un objeto quieto), anímala
   en Blender y luego **repasa el contorno a mano en Photoshop** (rotoscopia), igual que hizo el equipo con
   la montaña rusa: ahorra tiempo de modelado fino sin perder el look dibujado.
4. Renderiza el objeto solo (sin fondo), pásalo a Photoshop y aplícale ahí el filtro de papel del paso 3 de
   arriba, recortado sólo a sus sombras, para que combine con el resto de la lámina dibujada a mano.

**Encuadre y composición** (de la entrevista a Ishikawa) ✅:
- Prioriza **una silueta clara** por plano: el personaje o el objeto se reconoce por su contorno general,
  no por el detalle interno — pensado para lectores de todas las edades.
- Congela la acción en su **punto más alto** (el instante en que golpea, dispara o revela algo), no a
  mitad de un movimiento confuso.
- Cámara sencilla: evita ángulos imposibles o múltiples cortes; un plano, una idea clara.

## 24 · Obras parecidas y temas relacionados

Tono: comedia + acción con toques de crimen organizado, familia encontrada y un protagonista que oculta
un pasado violento bajo una vida doméstica tranquila.

- **The Way of the Househusband** (Gokushufudou): la propia página de TV Tropes de Sakamoto Days lo pone
  como «Compare» directo — ex-yakuza legendario que ahora es amo de casa, mismo choque de «leyenda
  criminal + vida cotidiana absurda» · ✅ ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Manga/SakamotoDays))
- **SPY×FAMILY**: la recomendación con más votos de los usuarios de AniList para esta serie (162 votos) ·
  ✅ (`datos-texto.md`, AniList). Ya tiene su propia biblia en el servidor: `biblias/06-spy-x-family/` — no
  repetir sus ideas de lámina (agente secreto + familia falsa que se vuelve real); Sakamoto Days es la
  familia real de un asesino retirado, el contraste está en que aquí la familia **ya existe** y él es quien
  vive la doble vida.
- **One-Punch Man**: protagonista aplastantemente fuerte que vive con calma casi aburrida su poder,
  comedia por contraste · votos en AniList: 37 · ✅. Ya tiene biblia (`biblias/35-one-punch-man/`).
- **Assassination Classroom**: escuela de asesinos, tono que mezcla comedia escolar y acción letal, mismo
  espíritu que la JCC (Japan Clear Creation) de Sakamoto Days · votos AniList: 14 · ✅. Ya tiene biblia
  (`biblias/24-assassination-classroom/`) — si la lámina de Sakamoto Days usa la JCC, no repetir el
  «examen de ingreso mortal» si ya está en esa biblia.
- Otras recomendaciones de AniList con menos votos: Gintama (73), Buddy Daddies (56), Rurouni Kenshin 2023
  (41), Mission: Yozakura Family (22), The Fable (18), Lycoris Recoil (18), The Yakuza's Guide to
  Babysitting (29), Kill Blue (46), Marriagetoxin (66) · ⚠️ (una sola fuente, AniList, sin comprobar en
  reseñas)
- **Influencias reconocidas por el propio autor** (ver punto 18): el manga **Domu** de Katsuhiro Otomo, y
  el cine de sicarios de Hollywood **John Wick** y **The Equalizer** · ✅ (MangaPlus + Shonen Jump News)
- Con qué NO comparar: Sakamoto Days no tiene el tono sentimental de Spy×Family (la ternura ahí viene de
  la familia falsa aprendiendo a quererse; aquí la familia ya se quiere, la comedia sale de que él ya no
  puede matar) ni el gore constante de Chainsaw Man (aquí la violencia se dibuja «cool», no traumática,
  según el propio editor: «evito la brutalidad gratuita») · ✅ (MangaPlus, cita directa del editor)
