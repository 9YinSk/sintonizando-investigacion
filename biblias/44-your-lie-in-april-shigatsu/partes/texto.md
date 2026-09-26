# Investigación de TEXTO, JUEGOS Y TÉCNICA · Your Lie in April (Shigatsu wa Kimi no Uso) — encargo 44

Puntos 5, 6, 11, 18, 24 y 25 de ENCARGO.md. Libreta de datos, no prosa.
No hay serie hermana (encargo 44 no la menciona). Parto de `datos-texto.md`
(AniList: ficha, equipo creativo, obras parecidas recomendadas) y sigo desde ahí.

## 5 · Tipografía

El logo cambia de estilo entre el manga y el anime: dos letras muy distintas
para el mismo título. Todas las libres candidatas se comprobaron con
`fontTools` (á, ñ, ¿, ¡).

- **Logo del manga** (portada del tomo 1, Kodansha): «四月は君の嘘» en una
  **gótica redondeada muy gruesa, color magenta/rosa**, trazos parejos sin
  serifa, terminaciones romas ✅ (imagen medida:
  `static.wikia.nocookie.net/.../Manga_Volume_1.png`, 669×1000 · el nombre del
  autor 新川直司 va debajo en gótica fina normal, negro). Letra libre parecida:
  **Zen Maru Gothic** (peso Black, Google Fonts, japonés+latín) — comprobada
  con fontTools: trae á, ñ, ¿, ¡.
- **Logo del anime** (usado en Blu-ray/web oficial): el mismo título pero en
  **mincho fino tipo pincel**, trazos que se adelgazan como caligrafía,
  **negro**, con pétalos de sakura rosa y celeste flotando alrededor de los
  kanjis y un asterisco/flor negro entre el título y el eslogan ✅ (imagen:
  `upload.wikimedia.org/wikipedia/commons/5/5e/Shigatsu_wa_Kimi_no_Uso_logo.png`,
  466×126, usada en la Wikipedia en inglés con alt «The anime's logo»). Letra
  libre parecida: **Shippori Mincho** (Google Fonts, japonés+latín, hecha para
  imitar pincel fino) — comprobada, trae á, ñ, ¿, ¡.
- **Eslogan en inglés** bajo el logo del anime («I met the girl under
  full-bloomed cherry blossoms, and my fate has begun to change.»): itálica
  fina y muy pequeña, casi caligráfica ⚠️ (una fuente, no identificada por
  nombre: hay un hilo sin responder en el foro de dafont.com preguntando por
  ella,
  [dafont.com/forum](https://www.dafont.com/forum/read/365007/what-font-shigatsu-wa-kimi-uso-your-lie-in-april)).
  Letra libre parecida: **Cormorant Garamond** itálica o **EB Garamond**
  itálica (Google Fonts) — comprobadas, traen á, ñ, ¿, ¡.
- **Globo normal de manga**: no hay tipografía propia documentada (el manga
  japonés usa rotulación estándar del gremio, vertical) ⚠️. Para una lámina en
  español, letra clara sin adornos: **M PLUS 1p** (Google Fonts, gótica
  japonesa+latina, muy usada en ediciones digitales de manga) — comprobada.
- **Onomatopeyas**: la serie no es de acción (nota de AniList: 0% tags de
  pelea), pero sí tiene SFX musicales dibujados a mano (tecla, cuerda, respiración)
  ⚠️ (no se pudo confirmar viendo páginas del manga: el volumen 1 está en
  préstamo con DRM en Internet Archive, no accesible sin pedirlo prestado;
  descripción de memoria de reseñas). Letra libre parecida para SFX
  caligráficos: **Yomogi** (Google Fonts, manuscrita japonesa) — comprobada.
- **Cartel del mundo** (letreros de Towa Hall, programas de concurso,
  uniformes): gótica limpia institucional. Letra libre: **Zen Maru Gothic**
  (peso normal) o **M PLUS Rounded 1c** (Bold) — comprobadas.
- **Interfaz de videojuego**: no aplica — no existe videojuego oficial de la
  franquicia (ver punto 11, con las búsquedas hechas).
- **Subtítulos y créditos** (doblaje inglés de Bang Zoom!/Aniplex USA,
  Crunchyroll): sans-serif limpia estándar de streaming, sin personalidad
  propia de la serie ⚠️ (no se vieron subtítulos latinos: no hay doblaje
  latino, ver `partes/voz.md` del investigador de voz). Letra libre: **Noto
  Sans** — comprobada.

## 6 · Cómo hablan y piensan en pantalla

Es una serie dramática, no de acción: casi no hay gritos ni globos rotos. Lo
importante son tres cosas que si se copian mal delatan que no se investigó:
la carta de Kaori, cómo NO se muestra el pensamiento de Kousei, y el
silencio.

- **La carta de Kaori (el cuadro más icónico de la serie)**: en el capítulo
  final, sus padres le entregan a Kousei un sobre cerrado para abrir «cuando
  llegue la primavera». Es una **carta manuscrita**, leída en narración sobre
  planos de la letra en el papel; revela que ella mintió sólo una vez en
  abril (que amaba a Watari) y que en realidad amaba a Kousei desde niña ✅
  ([Fandom, Episodio 22](https://shigatsu-wa-kimi-no-uso.fandom.com/wiki/Episode_22:_Spring_Wind),
  [primetimeanime.com](https://primetimeanime.com/blog/your-lie-in-april-ending-explained-complete-analysis)).
  Para una lámina: letra cursiva fina sobre textura de papel de carta, nunca
  una tipografía de máquina.
- **El pensamiento NO va en burbuja de nube**: cuando Kousei no puede oír su
  propio piano, la serie no pone texto de pensamiento — corta a una
  metáfora visual completa (se hunde en un océano oscuro) ✅ (TV Tropes,
  trope *Rule of Symbolism*:
  [tvtropes.org/.../Manga/YourLieInApril](https://tvtropes.org/pmwiki/pmwiki.php/Manga/YourLieInApril);
  confirmado también por el propio director: «el monólogo interno de Kaori
  se redujo al mínimo a propósito, para dejar espacio a la imaginación del
  espectador», entrevista oficial, ver punto 18). Para una lámina fija (que no
  puede cortar de escena), la traducción correcta NO es una burbuja de
  pensamiento con nube: es un fondo que cambia de textura/color detrás del
  personaje (agua oscura, o color vívido si es un pensamiento feliz).
- **Silencio como puntuación**: TV Tropes documenta *Stunned Silence* — la
  reacción típica del público dentro de la ficción tras una actuación es
  quedarse callado, sin texto, varios segundos ✅ (mismo TV Tropes de arriba).
  Para diálogo en pantalla: dejar cuadros vacíos/pausas es fiel al tono.
- **Nombre con doble grafía, dato para subtítulos**: el nombre de Kaori en
  japonés no es かおり sino **かをり**, que se romaniza «Kawori»; en el
  episodio 11 un letrero en su puerta dice literalmente «Kawori's room» ✅
  (TV Tropes, *Spell My Name With An S*, mismo enlace de arriba). Si una
  lámina usa texto en japonés cerca de Kaori, esta es la grafía correcta.
- **Cartelas del mundo real**: la serie usa fondos reales fotografiados de
  Nerima-ku (Tokio) para casi toda la localización, según un blog citado por
  TV Tropes ⚠️ (una fuente, *Real-Place Background*, mismo TV Tropes). No hay
  HUD de interfaz digital en la serie (no es sci-fi): los «textos en
  pantalla» del mundo son analógicos — partituras con anotaciones a mano,
  programas de concurso impresos, el cartel de resultados de Towa Hall.
- **Videojuegos de la franquicia**: no existe ninguno (ver punto 11) — así
  que no hay caja de diálogo de videojuego propia que describir aquí.
- **Cómica/slapstick** (etiqueta AniList: Slapstick 56%): en los pocos
  momentos de comedia (Tsubaki golpeando a Watari o a Kousei) sí aparecen
  globos de grito puntiagudos, estándar de shonen — no hay estilo propio
  documentado más allá del convencional del género ⚠️.

## 11 · Videojuegos de la franquicia

- **No existe ningún videojuego oficial** de Your Lie in April/Shigatsu wa
  Kimi no Uso: ni en Steam, ni app móvil de juego (sólo apps de fondos de
  pantalla), ni juego para consola ✅ (búsqueda en Steam sin resultados de
  juego —sólo un grupo y guías de fans—, búsqueda web «Your Lie in April
  game app mobile» y en japonés «四月は君の嘘 ゲーム アプリ»: sólo apps de
  lectura de manga —Palcy, Magapoke, Piccoma— y de fondos de pantalla).
- **The Cutting Room Floor** no tiene página de la obra (buscado con
  `site:tcrf.net`, y por categorías de «juegos publicados en abril»: nada
  relacionado) ✅. Coherente con que no hay juego que analizar.
- El motor de búsqueda `tcrf.net` bloquea `curl` con un reto de Cloudflare, y
  `herramientas/navegar.py` fallaba porque `PLAYWRIGHT_CHROMIUM` apuntaba a
  una build inexistente (`chromium_headless_shell-1243`); la que sí está
  instalada es `chromium_headless_shell-1194`. Con
  `PLAYWRIGHT_CHROMIUM=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell`
  y `ignore_https_errors=True` en el contexto de Playwright si sirve para
  abrir TV Tropes (usado en el punto 24); para TCRF no hizo falta, ya que
  WebSearch fue suficiente para confirmar que no existe la página.
- Apps de lectura oficiales del manga (Palcy, Magapoke, Piccoma) tienen su
  propia interfaz de lector, pero son apps de la editorial (Kodansha/Palcy),
  no un juego de la franquicia: no aplican al punto 11.

## 18 · Estilo de dibujo y técnica, y cómo replicarlo

*Rigs y tramas: ver puntos 3 y 19.* Aquí sólo línea, sombreado, filtros,
programas usados según entrevistas oficiales, y cómo reproducirlo en
Photoshop y Blender.

**Cómo se hizo (entrevistas oficiales, en japonés, sitio oficial `kimiuso.jp`,
sección «スペシャル» — no traducidas antes a español):**

- El **piano en 3D** de las escenas de interpretación lo hizo el estudio de
  CG **Graphinica**; el reporte de producción oficial dice que «gracias al
  magnífico 3D de Graphinica, las escenas de interpretación del primer cour
  quedaron muy bien resueltas» ⚠️ (fuente única pero primaria y oficial:
  [kimiuso.jp/special/04.html](https://www.kimiuso.jp/special/04.html), entrada
  «#14 ピアノの3D設定», 21-ene-2015).
- **Dos intérpretes reales sirvieron de referencia de movimiento** (no
  motion-capture con marcadores, sino grabación en vídeo con varias cámaras
  para que los animadores dibujaran encima): el pianista **Tomoki Sakata**
  (阪田知樹) tocó para las manos de Kousei, Takeshi Aiza y Emi Igawa; la
  violinista **Yuna Shinohara** (篠原悠那) tocó para Kaori. El director les
  daba indicaciones actorales antes de grabar cada escena («aquí se te
  rompe el corazón», «toca pensando en alguien») ✅ (entrevista oficial al
  director Kyohei Ishiguro,
  [kimiuso.jp/special/05_01.html](https://www.kimiuso.jp/special/05_01.html);
  confirmado también por TV Tropes, trope *2D Visuals, 3D Effects*: «las
  escenas de piano usan CG, sobre todo para mostrar las teclas y los dedos
  en detalle, porque dibujarlo a mano no sería viable»,
  [tvtropes.org](https://tvtropes.org/pmwiki/pmwiki.php/Manga/YourLieInApril)).
- **Texturas 2D pegadas sobre objetos** («貼り込み素材», *harikomi sozai*):
  el equipo de diseño de Graphinica hacía etiquetas y páginas (la marca de
  leche que bebe Kousei, páginas de revista/periódico) y las «pegaba»
  ajustadas a la forma del objeto en 3D o el fondo ✅ (mismo
  `kimiuso.jp/special/04.html`, entrada «#13 2Dワークス»). Es exactamente la
  técnica de «proyectar una textura plana sobre una forma» que se replica en
  Photoshop (deformar con Transformación de perspectiva/Puppet Warp) o en
  Blender (UV-mapear una imagen sobre el objeto).
- **Paleta deliberadamente bipolar**: el director explica que el manga es en
  blanco y negro pero el anime es a todo color, así que decidió una
  «coordinación total del color»: en una frase, **«brillante y pop»**
  (明るくポップに) tomando los colores de las páginas a color y las portadas
  de los tomos, con mucha luz y saturación alta, y bordes nítidos (sin
  desenfocar) para dar sensación de transparencia (**透明感**, *tōmeikan*).
  Las escenas serias, en cambio, se llevan a un **monótono duro** a
  propósito, para que el contraste (明暗差) golpee ✅ (misma entrevista,
  `kimiuso.jp/special/05_01.html`).
- **Diseño de personaje**: la diseñadora de personajes y directora de
  animación **Yukiko Aikei** fue elegida porque su trazo «femenino» encajaba
  con el de Naoshi Arakawa; ella misma dice que le costaba dibujar a los
  personajes «guapos» (Watari, Aiza) y que le resultaba más fácil el estilo
  femenino y los niños ✅ (misma entrevista oficial). En una charla en
  convención (EE.UU.) contó que su prioridad fue «capturar el toque del
  lápiz de Arakawa» y simplificar el detalle del manga sin perder la esencia,
  con muchas iteraciones del diseño de Kaori hasta dar con su sonrisa y su
  movimiento desenfadado ✅
  ([animeherald.com](https://www.animeherald.com/2016/04/04/anime-boston-2016-conversation-lie-aprils-kyohei-ishiguro-yukiko-aikei/),
  charla en Anime Boston 2016).
- **El autor sobre su propio trazo** (Naoshi Arakawa, entrevista oficial):
  dibuja las manos «con sensualidad» a propósito («los grandes intérpretes
  tienen algo de erotismo en alguna parte», dice como teoría propia) y para
  las escenas de interpretación cuida el **ritmo de lectura de la página**:
  tamaño de las viñetas y los márgenes, intensidad de las líneas de efecto
  (*speed lines*), y **dónde coloca los globos de diálogo** — todo pensado
  como una partitura visual, no decorativo ✅
  ([kimiuso.jp/special/05_05.html](https://www.kimiuso.jp/special/05_05.html)).
  Esto conecta directo con el punto 6: los globos no son un añadido, son
  composición.
- **Metáfora visual recurrente**: pétalos de flor/luz que se elevan y
  dispersan durante las actuaciones (representa la desconexión de Kousei con
  su propio sonido, y en el final, a Kaori disolviéndose en partículas de
  luz como pétalos de sakura) ✅ (análisis coincidente en
  [Tumblr @fandomsandfeminism](https://www.tumblr.com/fandomsandfeminism/156397287024/your-lie-in-april-uses-visual-metaphors-and) y
  TV Tropes *Cherry Blossoms*/*Snow Means Death*, mismo enlace de arriba).
- **Preproducción larga y guion grabado antes de animar**: la serie tuvo 5
  veces más tiempo de preproducción que lo habitual del estudio, integrando
  la música en el storyboard; el doblaje japonés se grabó ANTES de terminar
  el arte final, y los animadores veían/escuchaban la actuación de voz
  mientras dibujaban ✅ (charla Anime Boston 2016, mismo enlace de arriba).
- **Pipeline general de la industria** (no confirmado específico de este
  título, pero es el estándar de A-1 Pictures/estudios TV de la época) ⚠️:
  línea vectorial en RETAS! PRO Stylos, color con PaintMan, composición en
  CoreRETAS + Adobe After Effects para efectos especiales (destellos, grano,
  desenfoques) — fuente:
  [Anime News Network, «What Software Is Used In Anime Production?»](https://www.animenewsnetwork.com/answerman/2018-03-30/.129615).

**Cómo reproducirlo en Photoshop:**

- **Línea**: fina, de grosor casi uniforme, color no-negro-puro (gris muy
  oscuro o marrón oscuro en escenas cálidas) — pincel de 2-3 px con poca
  variación de presión; para el «trazo femenino» de Aikei, evitar líneas
  duras en mandíbula/nariz, preferir curvas suaves.
  Añade guías: encaja aquí `estilo.py` (herramienta del equipo) sobre un
  fotograma para medir el grosor real de línea antes de dibujar — así lo pide
  AYUDANTE.md; el investigador de imagen ya mide colores, este dato de línea
  lo puede repetir el redactor si hace falta.
- **Sombreado**: cel-shading a **dos tonos** (base + una sombra plana, sin
  degradado duro) en las escenas «pop»; para las escenas serias, capas de
  **Multiplicar** en azul-gris frío por encima de toda la ilustración para
  bajar la saturación (imita el «monótono» que describe el director) y una
  capa de **Trama de puntos** (screentone, textura de manga) al 20-30% de
  opacidad sobre las sombras da el acabado de línea impresa.
- **Brillo y transparencia (透明感)**: capa nueva en modo **Aclarar/Lighten**
  o **Sobreexponer color (Color Dodge)** con un pincel suave blanco/dorado
  detrás del contorno de los personajes en escenas de actuación; un
  **destello de lente** (Filtro > Renderizar > Destello) muy sutil sobre la
  fuente de luz principal. Para el «pétalo de luz» de las actuaciones:
  pincel de partícula tipo confeti + Desenfoque de movimiento radial saliendo
  del instrumento.
- **Filtros de animación**: grano de película fino (Filtro > Ruido > Añadir
  ruido, 2-3%, monocromático) sólo en escenas nostálgicas/flashback; nada de
  aberración cromática fuerte (la serie no la usa, es un look limpio, no
  «glitch»).

**Cómo reproducirlo en Blender:**

- **Contorno**: usar **Freestyle** (Render Properties > Freestyle) en vez de
  Solidify, porque Freestyle permite variar el grosor de línea según ángulo
  de cámara — más parecido al trazo que se afina de la serie que un contorno
  de grosor constante (Solidify).
- **Shader tipo cel**: nodo *Shader to RGB* + **ColorRamp** de 2-3 escalones
  sobre un Diffuse BSDF (no usar Principled BSDF directo, pierde el corte
  duro entre luz y sombra); esto imita el cel-shading de 2 tonos descrito
  arriba.
- **Luz**: una luz de área grande y suave como key light dorada/cálida (imita
  la iluminación de sala de concierto de las escenas de actuación —
  candelabros, luces de escenario) + una luz de relleno azulada fría para
  las sombras, nunca sombras 100% negras.
- **Render de las manos/piano**: si se anima un piano en 3D como referencia
  (igual que hizo Graphinica), exportar sólo silueta/manos y componer encima
  del fondo 2D en Photoshop o After Effects — así lo hizo el estudio
  (mezcla 2D+3D, no todo en 3D).
- Modelos y rigs 3D libres del personaje/piano: **ver puntos 3 y 19** (los
  busca el investigador de imagen), no se buscaron aquí por instrucción del
  encargo.

**Encuadres y composición típicos** (de las entrevistas + TV Tropes):

- Plano extremo de cara/mirada a cámara para el key visual (ejemplo: la
  primera key visual oficial usó «ojos que se cruzan con los del espectador,
  para que dé un vuelco el corazón», concepto discutido entre el director y
  el productor) ✅ (`kimiuso.jp/special/04.html`, entrada «#04»).
- Composición de manga con viñetas grandes/pequeñas alternadas para marcar el
  ritmo de una interpretación (ver cita de Arakawa arriba).
- Planos silueta de los 4 protagonistas para fijar identidad de personaje
  antes de animar (el diseño de personaje se pensó primero en silueta) ✅
  (charla Anime Boston 2016, mismo enlace de arriba).

## 24 · Obras parecidas y temas relacionados

- **Recomendadas por afinidad en AniList** (ya en `datos-texto.md`, no se
  repite la consulta): *I Want to Eat Your Pancreas*, *A Silent Voice*,
  *Violet Evergarden*, *Clannad: After Story*, *Anohana*, *March Comes in
  Like a Lion*, *Golden Time*, *Kids on the Slope* (música + coming-of-age,
  la más cercana en tema), *Blue Period*, *Your Name.* ✅.
- **Del mismo autor, Naoshi Arakawa**: *Sayonara Football* (su obra anterior,
  sobre fútbol femenino — el propio autor dice que no quiso repetir tema
  deportivo y por eso cambió a música) y *Farewell, My Dear Cramer* (otro
  manga de fútbol) ✅ (TV Tropes, ficha de la obra,
  [tvtropes.org](https://tvtropes.org/pmwiki/pmwiki.php/Manga/YourLieInApril);
  confirmado por el propio Arakawa en su entrevista oficial,
  `kimiuso.jp/special/05_05.html`: «como ya hice fútbol antes, no quería
  repetir deporte»).
- **Homenajes reconocibles dentro de la obra** (*shout-outs*, TV Tropes):
  la melodía que toca Kaori con la melódica en el episodio 1 es **«A Morning
  of the Slag Ravine»**, de *El castillo en el cielo* (Studio Ghibli) — un
  guiño directo confirmado en el propio diálogo del capítulo (los niños le
  dicen que no atrae pájaros, y ella responde «a Pazu sí le funcionó») ✅.
  Varias frases de Kaori citan **Peanuts/Snoopy** (Charlie Brown, Snoopy,
  Marcie) en los episodios 6, 7, 11 y 21 ✅ (mismo TV Tropes).
- **Comparación explícita del propio equipo con otra obra**: el compositor
  Masaru Yokoyama dijo en su entrevista que él mismo estudió música clásica
  de niño igual que Kousei, y que sintió afinidad personal con la historia
  ✅ (`kimiuso.jp/special/05_01.html`).
- **Recepción que la vincula con otras obras**: Eiichiro Oda (autor de
  *One Piece*) declaró en una entrevista que envidiaba la manera en que la
  obra logra «mostrar la música en el dibujo»; tras esa entrevista el manga
  agotó existencias y hubo que reimprimir ✅ (TV Tropes, trope *Colbert
  Bump*, [tvtropes.org/.../Trivia/YourLieInApril](https://tvtropes.org/pmwiki/pmwiki.php/Trivia/YourLieInApril)).
- **Adaptaciones relacionadas** (mismo universo, no «obras parecidas» sino
  expansión): precuela *Your Lie in April: Moments* (OVA), spin-off
  *Coda* (manga bonus con el DVD/BD, aún sin traducir al inglés), película
  live-action (2016, con Kento Yamazaki y Suzu Hirose), musical de Broadway
  con canciones de Frank Wildhorn (estrenado 2020 en Japón, con producciones
  en Londres y Corea) ✅ (TV Tropes, ficha de la obra, mismo enlace de
  arriba; AniList, ya en `datos-texto.md`).
- **No se buscaron canales del servidor** que se parezcan en tono (eso es
  parte del trabajo del redactor con `servidor/inventario.md`, fuera de mis
  puntos).

## 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo en cinco líneas:**
1. Japón contemporáneo real, mayormente ambientado en Nerima-ku (Tokio) con
   fondos tomados de lugares reales ⚠️ (una fuente, blog citado por TV
   Tropes).
2. No hay magia ni tecnología especial: el «superpoder» de la serie es tocar
   un instrumento y hacer sentir algo a quien escucha.
3. El mundo se divide en dos capas visuales: **monótono** (cuando Kousei no
   puede sentir/oír su música) y **a todo color** (cuando sí puede) — es la
   regla visual central, confirmada por el propio director (ver punto 18).
4. El calendario manda: la historia empieza y termina en **abril**, con los
   cerezos en flor como marco de tiempo — de ahí el título.
5. Los concursos de piano (locales, regionales, el campeonato de Japón) son
   la estructura que ordena la trama, como torneos.

**La historia por arcos (con sus momentos clave):**
- **Arco 1 — El reencuentro con la música** (ep. 1-6 aprox.): Kousei vive en
  un mundo sin sonido propio desde que murió su madre; Kaori lo arrastra a
  tocar de nuevo como su acompañante de piano en un concurso.
- **Arco 2 — Las competencias** (ep. 7-14 aprox.): Maihou Competition y el
  Eastern Japan Piano Competition, ambas en **Towa Hall** — Kousei reaparece
  como pianista, compite contra sus viejos rivales Takeshi Aiza y Emi Igawa
  ✅ (categoría «Competitions» de la wiki de Fandom:
  [Maihou Competition](https://shigatsu-wa-kimi-no-uso.fandom.com/wiki/Maihou_Competition),
  [Eastern Japan Piano Competition](https://shigatsu-wa-kimi-no-uso.fandom.com/wiki/Eastern_Japan_Piano_Competition)).
- **Arco 3 — La enfermedad de Kaori** (ep. 15-20 aprox.): se revela que
  Kaori está gravemente enferma; decide operarse para poder volver a tocar
  con Kousei una última vez, aunque es arriesgado.
- **Arco 4 — El final** (ep. 21-22): Kaori muere; su carta final revela la
  «mentira de abril» (ver punto 6). Kousei vuelve a tocar, ahora en color.

**Emblemas, objetos icónicos y vocabulario que un fan reconoce:**
- **Piano-senpai**: apodo cariñoso que le da el fandom al piano de Kousei,
  «como si fuera un personaje más» — la propia wiki tiene una página
  (informal, con tono de broma) dedicada a él ✅
  ([Piano-senpai, Fandom](https://shigatsu-wa-kimi-no-uso.fandom.com/wiki/Piano-senpai)).
  Vocabulario de fans para usar en textos del canal.
- **Maihou Competition** (名宝コンペ): el concurso más grande de Japón en la
  ficción, premio = plaza para competir en Europa ✅ (Fandom, enlace arriba).
- **Towa Hall**: la sala de conciertos donde ocurren ambos concursos
  principales — el «coliseo» de la serie ✅ (categoría Locations, Fandom).
- **El manzana acaramelada (candy apple/ringo ame)**: aparece en el capítulo
  21 del manga / episodio 12 del anime durante un ensayo para el concierto de
  gala; comida típica de festival japonés, la wiki le dedica ficha propia
  (símbolo de un momento dulce/cotidiano entre Kaori y Kousei) ✅ ([Fandom,
  Candy Apple](https://shigatsu-wa-kimi-no-uso.fandom.com/wiki/Candy_Apple)).
- **Los gatos**: hay tres gatos distintos en la serie con significado
  simbólico propio, según un análisis detallado de fans: uno de **ojos
  amarillos** (encarna la autoduda de Kousei, ligado a su gata de la infancia
  Chelsea, que su madre le hizo regalar), uno de **ojos azules** (posible
  proyección del alma de Kaori) y un **gato negro** que Kaori suele acariciar
  y que muere atropellado justo antes de la muerte de Kaori, anticipándola
  ✅ el atropello está confirmado en dos fuentes (TV Tropes, trope *Rule of
  Symbolism*, y el análisis de
  [raianimeblog.wordpress.com](https://raianimeblog.wordpress.com/2016/08/18/analysis-the-use-of-symbolism-and-metaphor-in-your-lie-in-april/));
  ⚠️ la distinción ojos-amarillos/ojos-azules es de una sola fuente
  (raianimeblog), es interpretación de fan, no dato oficial.
- **El «océano oscuro»**: metáfora visual recurrente para cuando Kousei no
  puede oír su propio piano — se ve a sí mismo hundiéndose en un mar oscuro;
  en el episodio 12 hay una escena literal en una piscina que resuelve esta
  metáfora (ve luz llegando desde la superficie) ✅ (TV Tropes + análisis de
  raianimeblog, mismos enlaces de arriba).
- **Rojo/azul como código de personalidad** (*Red Oni, Blue Oni*): Kousei
  («el metrónomo humano», mecánico) es azul, Kaori (apasionada, errática) es
  roja; el mismo código se repite con los rivales Emi Igawa (roja, toca
  distinto según el ánimo) y Takeshi Aiza (azul, constante) — el propio
  episodio 9 los codifica por color antes del recital de Kousei ✅ (TV
  Tropes, mismo enlace).
- **かをり / Kawori**: la grafía correcta del nombre de Kaori en kana no es
  la típica かおり; ver punto 6 para la fuente y el uso en pantalla.
- **Los fuegos artificiales que se apagan antes de tiempo** (ep. 12): Kaori
  sostiene bengalas que se apagan justo cuando duda sobre su futuro —
  anticipa su muerte ✅ (TV Tropes, trope *Dying Candle*, mismo enlace).
- **Piezas musicales que un fan reconoce**: el *Etude Opus 25 No. 5* de
  Chopin tiene ficha propia en la wiki por su peso narrativo ✅
  ([Fandom](https://shigatsu-wa-kimi-no-uso.fandom.com/wiki/Chopin%27s_Etude_Opus_25_No._5));
  el repertorio se relaciona con música y sonido, que es punto de otro
  investigador (voz/video) — aquí sólo se deja como vocabulario de mundo.

## Lo mejor para la lámina

- La **carta de Kaori** (manuscrita, sobre papel, leída en voz baja) es el
  cuadro de diálogo más fiel a la serie — mucho mejor que cualquier burbuja.
- Logo del anime (mincho fino + pétalos + asterisco) da la paleta y el tono
  exacto: negro sobre blanco, con un toque rosa/celeste, nunca gritón.
- El contraste **monótono / a todo color** es la regla de oro: cualquier
  lámina que quiera sentirse «de la serie» debe decidir en cuál de las dos
  capas vive el personaje.
- Piano-senpai (el apodo del piano) y la manzana acaramelada son vocabulario
  de fans listo para usar en textos del canal, sin inventar nada.
- Para Blender/Photoshop: contorno con Freestyle (no Solidify), shader de
  2-3 escalones con ColorRamp, capas de Aclarar/Color Dodge para el brillo
  dorado de las escenas de actuación.

## No encontré

- **Nombre exacto de la fuente** del eslogan en inglés del logo del anime
  (⚠️, un solo hilo sin responder en dafont.com, búsqueda «Your Lie in April
  logo font identify» y «what font shigatsu wa kimi uso»).
- **Página de manga real** para confirmar el estilo exacto de los globos
  (normal/grito/pensamiento) con mis propios ojos: el volumen 1 en Internet
  Archive está en préstamo digital con DRM (`yourlieinaprilvo0000arak`), no
  se puede leer sin pedirlo prestado. Se documentó con TV Tropes y
  entrevistas oficiales en su lugar.
- **Coreano/chino**: no se encontró cobertura técnica de estilo/arte en
  coreano o chino más allá de la nota (ya en TV Tropes) de que el musical
  tuvo estreno coreano en 2024; no hay web china/coreana dedicada al making
  of (búsquedas: sitio oficial sólo en japonés e inglés).
- **Segunda fuente para Graphinica** (el estudio de CG del piano): sólo
  aparece en el reporte de producción oficial (`kimiuso.jp/special/04.html`);
  no se encontró una nota de prensa o entrevista externa que lo repita
  (búsqueda «Graphinica "Your Lie in April" piano 3DCG»).

## Bitácora

- Fandom `shigatsu-wa-kimi-no-uso.fandom.com`, API `api.php` (allpages,
  allcategories, categorymembers, parse&prop=wikitext): páginas de
  competencias, localizaciones, objetos, piezas musicales, temas de
  apertura/cierre. Sin bloqueo.
- AniList (`datos-texto.md`, ya recolectado): ficha, equipo creativo, obras
  recomendadas — no repetido.
- WebSearch (idioma inglés): "Your Lie in April" A-1 Pictures 3DCG piano
  hands animation interview · Kyohei Ishiguro director interview visual
  style flowers light · Your Lie in April flower petals visual metaphor
  performance scenes analysis · site:tvtropes.org Your Lie in April YMMV ·
  site:tcrf.net Your Lie in April · "Your Lie in April" OR "Shigatsu wa Kimi
  no Uso" game app mobile · "Your Lie in April" logo font identify title ·
  Your Lie in April Kaori letter handwritten scene final episode · A-1
  Pictures animation software RETAS Toon Boom Photoshop compositing pipeline
  2014 · Graphinica "Your Lie in April" piano 3DCG.
- WebSearch (idioma japonés): 四月は君の嘘 ゲーム アプリ · 四月は君の嘘
  アニメ 制作 CG 手 ピアノ インタビュー · 四月は君の嘘 石黒恭平 演出
  インタビュー 色.
- Sitio oficial `kimiuso.jp/special/`: reportes de producción semanales
  (`04.html`) y entrevistas al staff (`05_01.html` director Ishiguro,
  `05_05.html` autor Arakawa) — leídos completos con `curl`, en japonés, no
  traducidos antes al español en ninguna fuente encontrada.
- `animeherald.com`: transcripción de charla en Anime Boston 2016 con
  Ishiguro y Aikei — leída completa con `curl`.
- TV Tropes (`tvtropes.org`) bloquea `curl`/`WebFetch` con 403. Arreglado
  `herramientas/navegar.py` para esta sesión: el Chromium instalado está en
  `/opt/pw-browsers/chromium_headless_shell-1194/...` (no
  `-1243`, que es lo que el script trae por defecto) y hacía falta
  `ignore_https_errors=True` en el contexto de Playwright porque el proxy
  reemplaza el certificado TLS. Con `PLAYWRIGHT_CHROMIUM` apuntando a la
  build correcta sí funcionó, dos páginas leídas completas (Manga y Trivia).
- Internet Archive: el volumen 1 del manga está indexado pero es préstamo
  con DRM, no legible sin pedirlo prestado — no se insistió.
- `fontTools` (`TTFont(f).getBestCmap()`) sobre 8 fuentes bajadas de
  `raw.githubusercontent.com/google/fonts`: Zen Maru Gothic, Shippori
  Mincho, M PLUS 1p, M PLUS Rounded 1c, Bungee, Comfortaa, Caveat, Noto
  Sans, Anton, Yomogi — las 10 con á, ñ, ¿, ¡. (Permanent Marker no se pudo
  bajar del repo, no crítico: no se usó como recomendación final.)
- Fuentes que fallaron sin insistir más de dos intentos: `tcrf.net` directo
  (Cloudflare); Wikipedia `pageimages` API (sin respuesta útil, se resolvió
  extrayendo el `<img>` del HTML de la página en su lugar).
