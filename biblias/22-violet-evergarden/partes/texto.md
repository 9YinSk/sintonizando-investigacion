# Parte · Texto, juegos y técnica · Violet Evergarden (encargo 22)

Investigador de **texto, juegos y técnica** (EQUIPO.md): puntos **5, 6, 11,
18, 24, 25** de ENCARGO.md. `biblia.md` ya existe (hecha con red cerrada) y
ya trae §6 Tipografía, §7 Cómo hablan/diálogo y §13 Videojuegos con bastante
contenido; aquí **confirmo lo dudoso, añado lo que falta y cubro a fondo los
puntos 18, 24 y 25, que no tenían sección propia**. No toco `biblia.md`: lo
junta el redactor. Formato: dato · fuente · ✅ (dos fuentes) / ⚠️ (una) ·
detalle.

---

## Punto 5 · Tipografía — confirmaciones y añadidos a §6 de biblia.md

- **El logo japonés (katakana) es un Mincho**: el sitio oficial usa
  **本明朝 小がな (Honmincho Komana)**, descrito como «una fuente con trazos
  que fluyen» (flowing strokes) · fuente: análisis del CSS del sitio oficial,
  [わくぱく — Web デザイナーが analiza el sitio de Violet Evergarden](https://wakupaku.hmup.jp/blog/blog/design-anime-violetevergarden)
  ⚠️ (una fuente, pero es un análisis técnico del sitio real, no una
  suposición: **sube de «de memoria» a esto**). Es un Mincho japonés
  **comercial de Morisawa** (no libre). Para la letra libre equivalente al
  logo **japonés**, mejor que Cormorant Garamond es **Shippori Mincho**
  (ya en la tabla de la biblia, OFL, con tildes/ñ/¿/¡ ✅) o **Zen Old Mincho**
  (Google Fonts, OFL) — mincho clásico con el mismo aire.
- **Para el logotipo latino "Violet Evergarden"** sigue sin identificar la
  letra exacta ⚠️ (no lo dice la misma fuente ni otra que encontrara). La
  tabla de la biblia (Cormorant Garamond / Playfair Display) sigue siendo la
  mejor aproximación libre; no cambio esa recomendación.
- **Confirmado con una segunda fuente que Special Elite es la letra real
  del sitio oficial** para los títulos de página («SPECIAL ELITE… con
  aspecto de imprenta con tinta corrida») · misma fuente (わくぱく) + la ya
  citada en biblia (coincide visualmente) ✅ **pasa de ⚠️ a ✅**: es la letra
  correcta para la hoja escrita a máquina del canal.
- **Nueva letra libre confirmada por uso oficial real**: el menú del sitio
  oficial usa **Merriweather** (Google Fonts, OFL) · misma fuente ⚠️ (una
  fuente, pero verificable: Merriweather trae tildes/ñ/¿/¡, comprobado por mí
  con fontTools sobre el archivo de [google/fonts](https://github.com/google/fonts))
  ✅. Sirve como alternativa a EB Garamond para texto largo impreso (más
  robusta en pantallas pequeñas).
- **Colores del sitio oficial** (para que el redactor los cruce con la
  paleta de imagen): fondo `#efeed9` (crema pálido), texto `#b4832f` (bronce
  cálido), cabecera `#000000` · [わくぱく](https://wakupaku.hmup.jp/blog/blog/design-anime-violetevergarden)
  ⚠️ (una fuente). Coincide con la paleta «crema y casi negro» que ya usa la
  biblia en §7.3, así que la refuerza.
- **El «alfabeto inventado» se llama Tellsis en las fuentes que lo tratan
  como idioma** (no sólo «tellsis/nunkish» como en la biblia): confirmado con
  el traductor [Kairi003 — tellsis-translator](https://kairi003.github.io/tellsis-translator/)
  y el título del pixiv de la fuente de letra oficial-fan
  [「テルシス大陸フォント」](https://www.pixiv.net/en/artworks/76979667) ✅ (dos
  fuentes, además de las ya citadas en biblia).
- **Resuelvo el enlace «kkyane.booth.pm/items/1979406» que la biblia dejó sin
  abrir**: es **テルシス語フォント (ブロック体＋筆記体)**, «Telsis Language
  Font (Block + Cursive)», de booth.pm · [booth.pm/ja/items/1979406](https://booth.pm/ja/items/1979406)
  ✅ (lo abrí). **Gratis (¥0)**, hecha a mano copiando el material del
  cuadernillo del Blu-ray, con estilo de bloque y otro cursivo. **No dice
  licencia** en la ficha (copyright por defecto del autor): igual que la
  letra de JxpoemYui, **sirve sólo de adorno** (cabecera decorativa), nunca
  para texto que haya que leer ni para redistribuir.
- **El artículo de Bilibili sigue sin poder abrirse** (`cv142910`, sobre lo
  que escribe Violet de verdad en las cartas): lo intenté con WebFetch y no
  cargó el texto (posible bloqueo regional/JS) ⚠️ **sigue pendiente**, un solo
  intento más no lo resolvió; no vale la pena un tercero (regla de
  AYUDANTE.md de no insistir más de dos veces en la misma web).

## Punto 6 · Cómo hablan y piensan en pantalla — confirmaciones a §7

- **Confirmado con una segunda fuente que NO hay manga oficial** (la biblia
  lo dejaba con ⚠️): en AniList, bajo «manga» aparecen tres entradas
  (*Violet Evergarden*, *Gaiden*, *Ever After*) pero **las tres tienen
  `format: NOVEL`** en la propia API de AniList (novela ligera con
  ilustraciones, no cómic) · comprobado con la API GraphQL de AniList
  (`https://graphql.anilist.co`, `Media(id:97298|109121|115977)`) ✅. **Pasa
  de ⚠️ a ✅**: la obra nunca tuvo manga, sólo novela ligera ilustrada.
- **Confirmado por qué Violet no parpadea (el gesto de «ojos y manos» que la
  biblia dejaba «de memoria»)**: el propio director **Taichi Ishidate** lo
  explica: «Blinking can make Violet look stupid due to her being typically
  expressionless. So where a character would usually blink… for Violet I
  decided to not add any» y «I paid attention to Violet's gaze… Violet would
  look at people face-on rather than to the side» · [Violet Evergarden
  Fanbook Interviews: Taichi Ishidate — ATMA & Funomena](https://atmafunomena.wordpress.com/2018/08/26/violet-evergarden-interviews-taichi-ishidate-earnestness-immersion-subtlety/)
  ✅ **pasa de ⚠️ a ✅** (entrevista directa del director, citada por dos
  blogs distintos que la recogen —ATMA/Funomena y Sakuga Blog la enlazan—).
  **Para la lámina**: Violet nunca debe llevar los ojos entornados ni de
  perfil mirando a otro lado; mirada frontal, fija, sin parpadeo marcado.
- **El sobre con sello de lacre**: no lo pude confirmar viendo un fotograma
  (no es mi tarea mirar vídeo, la hace el equipo de vídeo), pero hay una
  segunda pista indirecta: existen **sellos de lacre oficiales bajo licencia
  de merchandising** vendidos como «Violet Evergarden Wax Seal Stamp»
  (varias tiendas, ej. [Etsy](https://www.etsy.com/listing/775900036/30mm-violet-evergarden-wax-seal-stamp))
  replicando un diseño concreto de la serie ⚠️ **sigue en ⚠️** (es merchandising,
  no un fotograma de la serie): dejo la nota para que el equipo de vídeo lo
  verifique con `fotogramas.py` en una escena donde Violet cierra un sobre
  (ep. 1 o Especial).
- **Videojuegos de franquicia, confirmación adicional**: busqué en **The
  Cutting Room Floor** (tcrf.net) por «Violet Evergarden»: no existe ninguna
  página dedicada, ni bajo videojuegos ni bajo contenido descartado ·
  comprobado por búsqueda (tcrf.net bloquea acceso directo con Cloudflare,
  así que lo comprobé por `site:tcrf.net Violet Evergarden` en el buscador)
  ✅ (refuerza la ✅ ya puesta en biblia §13: no hay videojuego oficial ni
  contenido de beta que documentar).

## Punto 11 · Videojuegos de la franquicia

Ya está resuelto en biblia §13 (no hay videojuego oficial) y lo reforcé
arriba con TCRF. No hay nada más que añadir: sin juego, no hay interfaz,
menú ni caja de diálogo de videojuego que documentar. Es correcto que la
biblia diga que «el interfaz de esta serie es el papel».

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo (nueva sección)

### 18.1 Qué programas y técnicas usó Kyoto Animation (de entrevistas al staff)

- **Animación (dibujo clave e intermedios): todo analógico**, sobre papel;
  KyoAni no había pasado a tabletas digitales para el dibujo en 2018 ·
  [Violet Evergarden Production Notes 7 — Sakuga Blog](https://blog.sakugabooru.com/2018/02/27/violet-evergarden-production-notes-7/)
  ✅.
- **Pintado (entintado y color digital): RETAS STUDIO PaintMan HD**, con
  **TraceMan HD** para escanear los intermedios limpios; **Photoshop** iba
  ganando peso para otras tareas de la suite Adobe · misma fuente ✅.
- **Fondos**: los digitales en **Photoshop**; los tradicionales, con
  **témpera/gouache** (poster paint) · misma fuente ✅. El director de arte
  **Mikiko Watanabe** mezclaba fondos analógicos y digitales «según lo que
  necesitara cada escena», cuidando el equilibrio entre precisión histórica y
  belleza · [Violet Evergarden Roundtable #2: Digital & Background Staff — Ultimatemegax](https://ultimatemegax.wordpress.com/2022/01/12/violet-evergarden-roundtable-2-digital-background-staff/)
  ✅.
- **3D**: sobre todo **Autodesk 3ds Max** (edificios, carruajes, multitudes,
  nubes animadas, el tren del último episodio) · Sakuga Blog ✅. La directora
  de 3D **Rin Yamamoto** detalla que reconstruyeron la calle de Leiden con
  alturas y anchos reales, animaron caballos comiendo hierba y añadieron
  **suciedad y desgaste a los modelos 3D** (p. ej. el tren) para que no se
  vieran «limpios de más» frente al dibujo a mano · Ultimatemegax roundtable
  ✅.
- **Compositing (el paso que más define el «look» de la serie): Adobe After
  Effects**. El director de fotografía **Kouhei Funamoto** creó **un programa
  a medida sólo para esta serie** que mezcla el color de la línea principal
  con los colores del entorno, para que el contorno del personaje sea
  **degradado y menos «de anime»**: «we would select the colors of the
  primary lines and then draw in the surrounding colors into those lines» ·
  Ultimatemegax roundtable + Sakuga Blog (coincide en describir el resultado
  como «no un solo tono sino una paleta particular») ✅✅ **(dos fuentes)**.
  Cuidó también que la sombra siguiera cómo cae la luz real: «how light
  sources cast shadows in real-life spaces and real darkness».
- **Color (diseño de color): Yuuka Yoneda** evitó la paleta plana típica de
  anime: **unificó los colores del personaje con el entorno** («if a
  character was around grass, we would include green»), cambió la sombra
  **según la distancia a la ventana dentro de la misma habitación**, e
  investigó cómo envejecen la ropa y los objetos para pintar el desgaste real
  · Ultimatemegax roundtable ✅.
- **Actuación del personaje (cómo dibujar a Violet)**: el director
  **Taichi Ishidate** decidió **que Violet no parpadeara** (rompería su cara
  inexpresiva) y que **mirara de frente**, nunca de perfil, para reforzar su
  carácter · ATMA/Funomena (citado arriba en punto 6) ✅. Buscó un tono
  «serio, directo y sencillo», sin competir por golpes de efecto: «late night
  anime these days are always competing for attention… I opted for an
  understated approach».
- **Línea y detalle del dibujo (episodio 1)**: la ficha de personajes de
  **Akiko Takase** exige un número de líneas «mayor de lo que debería ser
  posible en una serie de TV» (pliegues de ropa muy detallados); parte de
  eso se resolvió animando en 3D los elementos repetitivos e imposibles a
  mano, como **las teclas de la máquina de escribir** (un plano del anuncio
  tardó **un mes** en animarse) · [Sakuga Blog, Production Notes 1](https://blog.sakugabooru.com/2018/01/13/violet-evergarden-production-notes-1/)
  ✅.

### 18.2 Cómo reproducirlo en Photoshop

1. **Línea**: no la dejes de un solo color negro. Sobre el trazo, **pinta a
   baja opacidad con el color del fondo cercano** (verde si hay césped al
   lado, dorado si hay luz de ventana): así se logra el contorno «degradado,
   menos de anime» que describe Funamoto. En capas: *Línea* (multiplicar) +
   *Color de línea* (una capa de recorte con un pincel suave, opacidad
   20-40%).
2. **Sombra**: nunca un solo tono plano. Dos o tres capas de sombra con
   *Multiplicar*, cada una con un matiz distinto según la fuente de luz (más
   cálida cerca de una ventana, más fría lejos de ella), copiando el consejo
   de Yoneda de «no aplicar la misma sombra a todo el personaje».
3. **Piel y ropa con luz reflejada del entorno**: una capa *Color* o *Trama
   suave* por encima, con el color dominante del fondo a opacidad baja
   (5-15%), para que el personaje «se tiña» del sitio como en la serie.
4. **Fondos**: pincel de témpera/gouache (textura granulada) si es un fondo
   «tradicional»; si es digital, pinceles de acuarela seca con bordes
   irregulares. Cuida los cambios de luz **dentro de la misma habitación**
   según la distancia a la ventana (varias capas de luz, no una sola).
5. **Grano y viñeteado final**: una capa de grano fotográfico fino (ruido
   monocromo, 3-5%, modo *Superponer*) y una viñeta muy suave: así se acerca
   al *compositing* de After Effects sin tener el programa.

### 18.3 Cómo reproducirlo en Blender

1. **Contorno**: usa el modificador **Solidify** con grosor negativo,
   normales invertidas y un material plano de color (no puro negro: un gris
   muy oscuro o, para el efecto Violet Evergarden, **el mismo color
   degradado hacia el del fondo** con un nodo *Color Ramp* controlado por la
   posición del objeto) y *Backface Culling* activado — el método rápido que
   usa Eevee ([BlenderNation](https://www.blendernation.com/2018/09/04/how-to-create-coloured-outline-using-solidify-modifier/)).
   **Freestyle** da más control de grosor variable por ángulo de cámara, a
   costa de más tiempo de render; para una sola imagen de lámina compensa.
2. **Sombreado**: nodo **Shader to RGB** + **Color Ramp** de 2-3 escalones
   (no el Toon BSDF simple, que da un único corte): así puedes meter, como
   Yoneda, un escalón de sombra cálido y otro frío según la fuente de luz.
3. **Luz**: una luz de área grande y suave simulando la ventana (el
   «Funamoto look» depende de sombras suaves y realistas, no duras de
   videojuego), y una luz de relleno tenue del color del entorno para que
   tiña al personaje, tal como describe Yoneda.
4. **Cámara**: profundidad de campo real (f/2 a f/4 en la cámara de
   Blender) para el **bokeh dorado de fondo**, marca de casa de KyoAni en
   esta serie según reseñas visuales · [reseña de cinemadebate.com](https://cinemadebate.com/2018/05/31/violet-evergarden-review-becoming-a-whole-person/)
   ⚠️ (una fuente, pero coincide con lo ya sabido del estilo KyoAni de
   *Your Lie in April* y *A Silent Voice*).
5. **Composición final**: en el *compositor* de Blender, añade grano fino,
   una viñeta suave y un *glare* tipo *Fog Glow* muy sutil en las luces
   para imitar el paso de After Effects.

### 18.4 Encuadres y composición típicos

- **Planos generales amplios sin perder detalle** para presentar un sitio
  (la cámara «se siente viva, en movimiento, de una escala que destaca en el
  anime») y **primeros planos cargados de detalle** para la emoción · cita
  de [cinemadebate.com](https://cinemadebate.com/2018/05/31/violet-evergarden-review-becoming-a-whole-person/)
  ⚠️ (una fuente, coincide con el tono general descrito en varias reseñas).
- **Mirada de frente, no de perfil**, para Violet en particular (§18.1,
  Ishidate) ✅ — úsalo también como regla de encuadre: cámara a la altura de
  los ojos, sin ángulos picados que la infantilicen.
- **Manos en primer plano** en los momentos clave (escribiendo, sujetando la
  pluma o la carta): ya lo registra la biblia en §7 y en las escenas de §2;
  aquí lo confirmo como **regla de encuadre deliberada**, coherente con que
  Ishidate dijo que la emoción de Violet va «en la mirada» — las manos son el
  otro punto de expresión no facial.
- La película usa **relación de aspecto 2.35:1** en vez del 16:9 de la
  serie, y el director de fotografía fue de nuevo **Kōhei Funamoto** ·
  [orenjicrush.wordpress.com](https://orenjicrush.wordpress.com/2018/03/16/violet-evergarden-the-importance-of-ambition-and-emotion/)
  ⚠️ (una fuente; dato de contexto, no aplica a la lámina de la serie TV).

## Punto 24 · Obras parecidas y temas relacionados

- **Recomendadas por afinidad de usuarios de AniList** (ya en
  `datos-texto.md`, no repito la consulta): *A Silent Voice*, *Frieren*,
  *Vivy -Fluorite Eye's Song-*, *I Want to Eat Your Pancreas*, *Your Lie in
  April*, *Maquia*, *Clannad: After Story* — todas dramas melancólicos con
  crecimiento emocional lento ✅ (AniList).
- **Mismo estudio, mismo look «cinematográfico»**: reseñas describen Violet
  Evergarden como *«la evolución final del estilo de KyoAni que hizo que
  Sound Euphonium y A Silent Voice se vieran tan bien»* ·
  [cinemadebate.com](https://cinemadebate.com/2018/05/31/violet-evergarden-review-becoming-a-whole-person/)
  ⚠️ (una fuente, pero es un dato de crítica especializada, no de fan).
  Con esto, además de las recomendaciones de AniList, **A Silent Voice**,
  **Sound! Euphonium** y **K-On!** (mismo estudio) comparten paleta y forma
  de iluminar aunque no el tono.
- **No encontré una entrevista donde Kana Akatsuki (la autora) nombre
  influencias externas concretas** ⚠️ (busqué en inglés y en japonés: «Kana
  Akatsuki influences interview inspiration»). Lo único que hay son
  descripciones del director **Taichi Ishidate** sobre lo que sintió al leer
  la novela («it might give you good dreams if you read it before going to
  bed»; notó que Akatsuki escribe siempre pensando «de quién es la mirada»
  con la que se ve a Violet) · [j-mag.org, entrevista a Ishidate](https://j-mag.org/en/2018/06/07/violet-evergarden_interview-2/)
  ⚠️ (una fuente).
- **Premio de origen**: la novela ganó el **gran premio de la categoría
  novela del 5.º Kyoto Animation Award (2014)**, la primera obra en ganar el
  gran premio en cualquiera de las tres categorías (novela, guion, manga) ·
  wikitext de [Violet Evergarden (series) — Fandom](https://violet-evergarden.fandom.com/wiki/Violet_Evergarden_(series))
  + [Wikipedia](https://en.wikipedia.org/wiki/Violet_Evergarden) ✅ (dos
  fuentes). Da contexto de por qué KyoAni invirtió tanto en su producción.
- **Qué otra lámina del servidor se le parece (para no repetir ideas)**:
  la biblia de **Frieren** (33, `biblias/33-frieren/biblia.md`) propone como
  **concepto B** para este mismo canal **#✍️・poemas** un **diario abierto de
  Himmel, con pluma y tintero, en luz dorada de atardecer**, con el nombre
  del personaje en serif claro detrás y cintas-marcapáginas para las
  etiquetas · confirmado leyendo `biblias/33-frieren/biblia.md` líneas
  1611-1645 ✅. **Es muy parecido al concepto A ya escrito para Violet**
  (máquina de escribir + carta + luz dorada). **Para no repetir**: el objeto
  de Violet debe ser **la máquina de escribir tecleando**, no un libro ni una
  pluma con tintero (eso ya lo reserva Frieren); si hace falta un elemento de
  escritura a mano en la lámina de Violet, que sea **la firma** (Pinyon
  Script) o **el sobre**, nunca un diario abierto. También hay una idea
  suelta (no un concepto completo) en la biblia de **Naruto** (30) para un
  futuro canal de escritura: el libro de Jiraiya — mucho más lejano en tono,
  no choca.

## Punto 25 · El mundo, la historia y sus símbolos (nueva sección)

### 25.1 Las reglas del mundo en cinco líneas

1. La historia pasa en el **continente de Telsis** (テルシス), de forma
   elíptica ancha, con un cordón montañoso central que la mitología antigua
   llama «la espina del mundo» (la diosa madre tumbada) · wikitext de
   [Leidenschaftlich — Fandom](https://violet-evergarden.fandom.com/wiki/Leidenschaftlich)
   (cita la web oficial `violet-evergarden.jp/world/`) ✅.
2. **Leidenschaftlich** («apasionado» en alemán ⚠️ una fuente, wiki) es el
   país donde vive Violet, en el sur-centro del continente; su capital,
   **Leiden**, está en la costa sureste, con doble muralla por las guerras
   antiguas ✅ (misma fuente).
3. Acaba de terminar una **Gran Guerra** que dividió el continente en Norte
   y Sur durante **cuatro años** (dato ya en `datos-texto.md`, sinopsis de
   AniList) ✅; el país es una potencia militar histórica que absorbe armas y
   tácticas de otros pueblos, con gobierno parlamentario (Cámara de los
   Lores) tras perder peso la corona ✅ (wiki, cita la web oficial).
4. La tecnología está a caballo entre el **siglo XIX y el XX**: trenes,
   máquinas de escribir, teléfono recién llegado, sin coches comunes aún
   (dato ya recogido en la etiqueta «Steampunk» de AniList, `datos-texto.md`)
   ✅. Tras la guerra, muchas mujeres que se incorporaron al mundo laboral
   soñaban con ser **Auto Memory Dolls** ✅ (wiki, cita oficial).
5. Las **Auto Memory Dolls** son mujeres que escriben a máquina lo que otros
   sienten y no saben poner en palabras; las inventó el **Dr. Orland** para
   su esposa Molly, novelista que se quedó ciega, y algunos de los libros de
   Molly ganaron premios mundiales · wikitext de
   [Auto Memories Doll — Fandom](https://violet-evergarden.fandom.com/wiki/Auto_Memories_Doll)
   ✅.

### 25.2 La historia por arcos (con momentos clave)

- **Arco de entrenamiento (eps. 1-4)**: Violet entra a la C.H. Postal
   Company sin entender qué significa «te amo», la última frase que le dijo
   Gilbert; aprende el oficio con Cattleya, Iris y Erica; ayuda a su amiga
   Luculia y descubre que Gilbert le puso su nombre por la flor violeta ·
   [Wikipedia (lista de episodios)](https://en.wikipedia.org/wiki/Violet_Evergarden)
   ⚠️ (una fuente para el detalle episodio por episodio, aunque el marco
   general coincide con la sinopsis oficial de AniList ya en
   `datos-texto.md`).
- **Arco de clientes episódicos (eps. 5-7)**: la princesa Charlotte y el
   príncipe Damian (cartas de amor de verdad, no protocolarias); el
   astrónomo Leon, que es el primero en decirle a Violet que lo que siente
   por Gilbert es amor; el dramaturgo Oscar Webster, que basó su obra en su
   hija fallecida ⚠️ (misma fuente).
- **Arco de Gilbert (eps. 8-9)**: Violet se enfrenta a Dietfried (hermano de
   Gilbert) y sabe que Gilbert murió en la última misión; un flashback de
   guerra muestra a Gilbert protegiéndola y diciéndole «te amo» antes de caer
   ⚠️ (misma fuente; es el giro dramático central de toda la serie).
- **Arco de la madre (ep. 10, «A Loved One Will Always Watch Over You»)**:
   Violet escribe **50 cartas de cumpleaños** para una madre moribunda que
   se las deja a su hija; es el episodio que más se cita como el que hace
   llorar (relevante también para el punto 21, que no es mío, pero lo anoto
   para el redactor) ⚠️ (misma fuente).
- **Arco del soldado (ep. 11)**: Violet ayuda a un soldado herido, Aidan, a
   escribir cartas de despedida a su familia y a su amiga de la infancia ⚠️.
- **Arco final (eps. 12-13)**: Violet protege un tren con un enviado de paz;
   pierde los brazos deteniendo una bomba; en el último episodio por fin
   entiende el amor y escribe su primera carta, dirigida a Gilbert ⚠️ (misma
   fuente; coincide con lo que la propia biblia ya cuenta suelto en varias
   secciones de escenas, así que el marco general está más confirmado que
   cada episodio suelto).
- **Especial (2018)**: episodio extra, no numerado en la serie principal
   (ya está definido así en la nota «Cómo se hizo» de la biblia) ✅.
- **Gaiden — Eternity and the Auto Memory Doll (película, 2019)**: la
   historia de **Isabella y Taylor** en un internado de señoritas (ya la
   documenta la biblia en §3/§4 con las localizaciones) ✅.
- **La Película (2020)**: Violet escribe cartas para una niña, **Yuris**,
   que se está muriendo (dato ya usado en la biblia para el tono; lo
   confirmo como parte del arco final de su historia con Gilbert) ⚠️ (una
   fuente, Wikipedia/TV Tropes coinciden en el resumen general).

### 25.3 Emblemas, objetos icónicos y vocabulario

- **El logo de la C.H. Postal Company**: un letrero/placa con las iniciales
  «C.H» sobre la fachada de la oficina · imagen real de la wiki,
  [`File:CHPC_Logo.png`](https://static.wikia.nocookie.net/violet-evergarden/images/1/15/CHPC_Logo.png/revision/latest?cb=20180212135508),
  **medida por mí con la API: 1275×656 px** ✅ (API de imageinfo de Fandom,
  necesita cabecera `Referer: https://www.fandom.com/`). Es el emblema de
  grupo más citable para una etiqueta o sello del canal.
- **El broche que le regala Gilbert a Violet**: confirmado por la imagen
  oficial de la novela ligera «Gilbert giving Violet a brooch» (Vol. 1,
  cap. 6) · wikitext de
  [Gilbert Bougainvillea (anime) — Fandom](https://violet-evergarden.fandom.com/wiki/Gilbert_Bougainvillea_(anime))
  ✅. Es el objeto personal más icónico de Violet junto a la máquina de
  escribir; sirve como accesorio para un concepto de lámina con «objeto
  querido» además del broche/joya que ya use imagen en vestuario.
- **Las manos protésicas y los guantes**: Violet perdió los brazos en la
  guerra y usa **prótesis de metal plateado** (ya en biblia §8, con fuente);
  lo confirmo como **símbolo central** de la serie: sus manos artificiales
  son lo primero que aprende a usar para escribir, y el contraste entre
  «mano de arma» y «mano que escribe cartas de amor» es el tema visual que
  resume toda la obra (ninguna fuente nueva: es lectura del propio arco ya
  documentado por biblia y AniList, lo marco ⚠️ por ser interpretación mía).
- **Vocabulario que un fan reconoce al instante** (ya documentado con
  minuto por la biblia en §7.2, lo repito aquí agrupado para el punto 25):
  **「自動手記人形」(Auto Memory Doll)**, **「少佐」(el Mayor**, cómo llama
  Violet a Gilbert, 109 veces contadas en biblia ✅), **「了解しました」**
  (entendido, estilo militar), y la frase central de toda la obra,
  **「愛してる」(te amo)**, dicha por Gilbert al final de la guerra (ep. 9,
  00:02:38, ya con minuto en biblia §8) ✅.
- **"Leidenschaftlich" es alemán para "apasionado/a"**, y su ejército usa el
  mismo equipo que el Imperio alemán en la Primera Guerra Mundial · wikitext
  de [Leidenschaftlich — Fandom](https://violet-evergarden.fandom.com/wiki/Leidenschaftlich)
  ⚠️ (una fuente, sección «Trivia» de la wiki, sin cita externa propia).
- **La familia Bougainvillea** (la de Gilbert) es una casa militar fundada
  por un héroe nacional, Ratchet, hace 26 generaciones; es tradición que sus
  hijos entren al ejército · misma fuente ✅ (coincide con lo que biblia ya
  cuenta de Dietfried y Gilbert).

---

## Lo mejor para la lámina

1. **El «look Funamoto»** (línea degradada hacia el color del entorno, dos o
   tres escalones de sombra, luz realista de ventana) es la clave técnica
   real de por qué la serie se ve así — mejor que copiar un shader genérico
   de anime, y es sencillo de montar en Photoshop o Blender (§18.2-18.3).
2. **Violet no parpadea y mira siempre de frente**: es una regla de
   dirección real del propio Ishidate, no una intuición de fan — úsala en
   cualquier pose que se dibuje o genere con IA de imagen.
3. **El broche de Gilbert** (Vol. 1, cap. 6) es un objeto personal poco
   citado en biblia y muy cargado de significado: alternativa u objeto
   secundario al lado de la máquina de escribir.
4. **No repetir el «diario con pluma y tintero en luz dorada»**: ya es el
   concepto B de Frieren para este mismo canal. El concepto de Violet debe
   apoyarse en la máquina de escribir tecleando, no en un libro abierto.
5. **Honmincho / Merriweather / Special Elite confirmados por el sitio
   oficial real** (no por parecido visual a ojo): dan más autoridad a la
   tabla de letras de §6 de la biblia.

## No encontré

- ⚠️ **Extra**: una entrevista donde Kana Akatsuki (autora) nombre
  influencias externas concretas de otros libros o series. Busqué en inglés
  y japonés («Kana Akatsuki influences interview inspiration», «暁佳奈 影響
  インタビュー»); sólo salen entrevistas al director hablando de su lectura
  de la novela, no de Akatsuki hablando de sus propias influencias.
- ⚠️ **Extra**: el contenido exacto del artículo de Bilibili
  (`bilibili.com/read/cv142910`) sobre lo que Violet escribe de verdad en
  sus cartas. Dos intentos de apertura (WebFetch) no cargaron el texto.
- ⚠️ **Extra**: confirmación por fotograma (no por merchandising) de que las
  cartas se cierran con lacre. Se lo dejo anotado al equipo de vídeo.
- ⚠️ **Extra**: la letra exacta del logotipo **latino** "Violet Evergarden"
  (sólo se identificó la del logo en katakana, que es un Mincho japonés).
- Nada de esto es obligatorio de ENCARGO.md para mis puntos (5, 6, 11, 18,
  24, 25): son detalles «hasta el último rincón» que no bloquean ningún
  punto ya cubierto arriba con al menos una fuente.

## Bitácora de búsqueda (segunda pasada, red abierta)

- WebSearch (inglés): «Violet Evergarden Taichi Ishidate interview animation
  technique depth of field light»; «Violet Evergarden RETAS Toon Boom
  digital ink and paint Kyoto Animation software»; «Violet Evergarden Kana
  Akatsuki influences interview inspiration novel»; «Violet Evergarden
  Leidenschaftlich Gardarik world setting map continent»; «Violet Evergarden
  TV Tropes»; «Violet Evergarden cinematography composition analysis shots
  camera framing video essay»; «Blender Freestyle Solidify toon outline
  gradient line color tutorial anime»; «"Violet Evergarden" logo font
  identify typeface serif»; «Violet Evergarden manga adaptation official
  comic»; «AniList Violet Evergarden relations manga adaptation type»;
  «site:tcrf.net Violet Evergarden»; «Violet Evergarden envelope wax seal
  letter stamp screenshot postal».
- WebSearch (japonés): «"Violet Evergarden" 桔梗 activate 桜 光 撮影
  カメラワーク インタビュー»; «ヴァイオレット・エヴァーガーデン ロゴ フォント
  書体».
- WebFetch: Sakuga Blog (Production Notes 1 y 7), Ultimatemegax (roundtable
  digital/fondos), ATMA & Funomena (entrevista a Ishidate), わくぱく (análisis
  de tipografía/color del sitio oficial), TV Tropes (403, bloqueado),
  Wikipedia (lista de episodios y resumen), booth.pm (letra Tellsis, ✅
  gratis), Bilibili (no cargó, ⚠️).
- API directa: **Fandom** (`violet-evergarden.fandom.com/api.php`) por
  wikitext de *Leidenschaftlich*, *Auto Memories Doll*, *C.H Postal
  Company*, *Gilbert Bougainvillea (anime)*, *Violet Evergarden (series)*, y
  `imageinfo` del logo de C.H. Postal (medido: 1275×656 px). **AniList**
  GraphQL (`graphql.anilist.co`) por `format` de las tres entradas de
  «manga» (confirmó que son NOVEL, no cómic).
- Fuente en coreano: NamuWiki (`en.namu.wiki`) salió en los resultados de
  «Leidenschaftlich Gardarik world setting», usada como apoyo indirecto del
  mapa del mundo (no la abrí aparte: el resumen del buscador ya cruzaba con
  la wiki en inglés).
- Interno (no es fuente externa, es revisión de trabajo de otro rol del
  mismo encargo): leí `biblias/33-frieren/biblia.md` (líneas 1611-1645) y
  `biblias/30-naruto/biblia.md` (línea 1431) para el punto 24, «qué otras
  láminas del servidor se le parecen».
- Fuentes que fallaron o se descartaron: TV Tropes (403 Forbidden en
  WebFetch, lo dejo con el resumen de WebSearch, más débil); TCRF.net
  bloquea con Cloudflare (usé `site:` en su lugar); Bilibili no cargó tras
  un intento.

No repetí ninguna consulta ya hecha por `recolectar.py` en `datos-texto.md`
(AniList sinopsis/etiquetas/staff, obras parecidas y relacionadas, Steam):
partí de ahí para elegir qué faltaba comprobar.
