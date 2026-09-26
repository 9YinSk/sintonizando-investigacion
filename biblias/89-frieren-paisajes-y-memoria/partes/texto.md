# Parte TEXTO · 89-frieren-paisajes-y-memoria (puntos 5, 6, 11, 18, 24, 25 de ENCARGO.md)

Serie hermana: **33-frieren** (misma obra, otro encargo, ya con biblia
terminada). Leí primero `biblias/33-frieren/partes/texto.md` y las secciones
6, 7, 13, Punto 18, Punto 24 y Punto 25 de `biblias/33-frieren/biblia.md`
(con `seccion.py --indice`): esa biblia **ya cubre a fondo** la tipografía
general (logo, globos de manga, letra libre por uso), el cuadro de diálogo
«normal» de la serie, las colaboraciones en videojuegos completas, el
proceso de dibujo (Clip Studio, Photoshop, Blender), las obras parecidas por
tono y el sistema del mundo (maná, rangos, arcos). **No repito nada de eso.**

Este encargo (89) pide un **ángulo nuevo**: fondos, luz y melancolía —
«paisajes y memoria». Cada hallazgo de abajo es o bien un dato que la
hermana no tenía, o el mismo tema mirado con esa lupa. También leí
`biblias/89-frieren-paisajes-y-memoria/partes/imagen.md` y `video.md` (ya
escritos por mis compañeros de equipo) para no pisar sus datos: cito lo
suyo sólo como referencia cruzada, sin repetir sus hex ni sus minutos.

## Hallazgos

### Punto 5 · Tipografía (foco: letra de monumento, diario y mapa del viaje)

- **Tres letras libres nuevas, comprobadas con fontTools por mí** (no las
  llevaba la hermana), pensadas para el registro de «objeto de memoria»
  (lápida, monumento, libro viejo) en vez del logo o el globo normal:

| Letra | Licencia | Por qué sirve para «memoria» | á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü |
|---|---|---|---|
| **Kaisei Tokumin** (700/800) | OFL 1.1, Google Fonts/Fontsource | Serif japonesa **pesada, para títulos fuertes** («Tokudai Mincho» = mincho extra grueso); funciona para el título grabado de una estatua o una lápida | **todos presentes** ✅ (comprobado yo, `fontTools.TTFont(f).getBestCmap()`, descargada de `fonts.gstatic.com`) |
| **Zen Antique** | OFL 1.1, Google Fonts | Diseñada como «japonés antiguo»: el kanji/katakana pesa más que el latín/hiragana, look de letra vieja de antes de la guerra | **todos presentes** ✅ (comprobado yo) |
| **Shippori Antique** | OFL 1.1, Google Fonts | Versión más suave y gastada del mincho, para texto de diario o carta envejecida | **todos presentes** ✅ (comprobado yo) |

  Fuentes de la ficha de cada letra: [Fontsource, kaisei-tokumin](https://fontsource.org/fonts/kaisei-tokumin),
  [Google Fonts, Kaisei Tokumin](https://fonts.google.com/specimen/Kaisei+Tokumin)
  (créditos: Font-Kai, 金井和夫) y [Google Fonts, Zen Antique](https://fonts.google.com/specimen/Zen+Antique)
  ✅. Archivos verificados en mi carpeta de trabajo
  (`/tmp/claude-0/trabajo/89-texto/fonts/*.ttf`), no se suben al repo.
  **Ojo**: no encontré ninguna fuente que diga que Kaisei imita letra
  grabada en piedra —lo dije de memoria en una búsqueda y no salió nada
  que lo confirme⁠— así que **no lo afirmo**: la recomiendo sólo por su
  peso y estilo «antiguo», visto por mí en la muestra oficial.

- **La letra del avance de episodio («次回予告»), posible pero sin
  confirmar**: un usuario de Yahoo!知恵袋 identifica **「文游明朝体 勇壮かな」**
  (Bungyu Mincho, kana «Yūsō» = «valeroso»), fuente **de pago** de Morisawa,
  como la más parecida («おおそらく», «probablemente») · fuente:
  [Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14289239084)
  ⚠️ (una sola respuesta, con duda explícita del propio autor). La ficha
  oficial de Morisawa describe esta kana como pensada para **«no ficción e
  historia»**, con «un estilo óseo y tenso» — encaja con el tono de
  «testimonio/memoria» de la serie · fuente:
  [Morisawa, ficha 文游明朝体 勇壮かな](https://www.morisawa.co.jp/fonts/specimen/6593)
  ✅ (la ficha del tipo es oficial; su USO en Frieren sigue sin segunda
  fuente). Sin equivalente libre específico: para ese registro, la
  hermana ya recomienda Zen Old Mincho (mismo peso e intención).

- **El mapa oficial del viaje usa números en círculo como marcador**: la
  web oficial tiene la página **«旅の軌跡を辿る地図»** («el mapa que traza las
  huellas del viaje») en `frieren-anime.jp/special/map/`, que numera los
  **28 episodios de la T1** con números en círculo japoneses (①-㉘) junto a
  su título, como si fueran paradas en un mapa. Lo leí con
  `herramientas/navegar.py` (texto sí, el mapa visual con JS no: pantalla
  en blanco tras `--captura`, igual que le pasó a mi compañera de imagen,
  que además probó Wayback Machine y también le bloqueó el acceso) ⚠️ visto
  el texto, no el mapa dibujado. Lista completa de títulos en la Bitácora.
  Es un dato de tipografía y de mundo a la vez: la propia serie **usa el
  número de episodio como si fuera un pin de recuerdo en un mapa** — muy
  aprovechable para un concepto de lámina de «paisajes y memoria» (ver
  Punto 25) · fuente: [frieren-anime.jp/special/map/](https://frieren-anime.jp/special/map/)
  ✅ (accedido y leído por mí; su existencia también la vio mi compañera de
  imagen, que no pudo leer ni el texto: dos intentos independientes,
  mismo resultado de bloqueo visual).

### Punto 6 · Cómo hablan y piensan en pantalla (foco: la memoria sin globo)

- **El objeto de memoria más fuerte de toda la serie: «la autobiografía de
  Himmel»** (「ヒンメルの自伝」), T2 ep. 37, emitido el **20-mar-2026**. En el
  Lago Korridor, Frieren y su grupo se quedan sin dinero para el barquero;
  el precio del pasaje es encontrar «la autobiografía de Himmel», escondida
  en un monasterio de una isla del lago. La encuentran junto a una estatua
  de Himmel: está escrita **con su propia letra**, contando el viaje del
  grupo desde SU punto de vista, con los días normales del camino · fuente
  oficial: [frieren-anime.jp, sinopsis ep. 37](https://frieren-anime.jp/story/2nd/ep37/)
  (guion: Tomohiro Suzuki; storyboard/dirección: Youhei Tsuchiya; dirección
  de animación: Runa Harano) ✅.
- **Las últimas páginas están en blanco, y Frieren las pasa igual, buscando
  que siga**: «ヒンメルの自伝は最後の方が空白ページになっていて、フリーレンは続きを求めるように
  白いページをめくる» («las últimas páginas de la autobiografía de Himmel están
  en blanco, y Frieren las pasa como si buscara que continuara») — el
  bloguero lo resume así: «quizá la tristeza, para nosotros, es como pasar
  páginas en blanco: termina de golpe, pero no lo aceptamos y seguimos
  buscando la continuación» · fuente:
  [note.com/sakuraigo](https://note.com/sakuraigo/n/n179c6ef7e84e), 21-mar-2026
  ✅ (coincide con el resumen recogido también en
  [dogadaijobu2025.com](https://dogadaijobu2025.com/archives/8036), blog
  independiente sobre el mismo episodio, mismo dato de fondo aunque sin la
  frase exacta de la página en blanco).
- **Por qué esto importa para la lámina**: es el «cuadro de diálogo»
  perfecto para el encargo — no es un globo ni una cartela, es **un libro
  real, en un sitio real (el monasterio del lago), con una letra hecha a
  mano que se corta en una página en blanco**. Cumple a la vez la regla 1
  del dueño (objeto real en sitio real) y el tema del encargo (memoria).
- **La memoria sin palabras, como norma de la serie**: un análisis en
  inglés (ver Punto 18) describe cómo Frieren evita el monólogo para
  expresar el duelo — por ejemplo, cuando **no logra recordar la cara de
  Himmel, simplemente se queda quieta, sin explicarlo con palabras**: el
  vacío (**«yohaku»**, espacio en blanco deliberado) hace el trabajo del
  texto. **El cuadro de diálogo propio de Frieren, para una escena de
  memoria, puede directamente no llevar texto** — el silencio o la página
  en blanco son el mensaje, no una carencia · fuente:
  [Unwinnable, Beatrix Kondo](https://unwinnable.com/2026/03/16/the-aesthetics-of-impermanence-how-frieren-visualizes-untranslatable-japanese-philosophy/),
  16-mar-2026 ⚠️ (un solo artículo crítico, sin minuto exacto de esa escena
  de «no recordar la cara»; pero coincide en espíritu con la página en
  blanco de la autobiografía, arriba, y con la filosofía de Saitou ya
  citada por la hermana: «lo importante es qué se quiere transmitir»).
- **No confundir con la cartela normal de la serie** (§7.1 de la biblia
  hermana, ya con la cartela de tráiler y el título de episodio en negro):
  eso sigue siendo válido para textos cortos; lo de aquí es específico
  para **una escena de memoria/duelo dentro de la historia**, donde lo
  mejor es un objeto físico o directamente nada de texto.

### Punto 11 · Videojuegos (foco: el monumento que viaja a otros mundos)

La hermana ya tiene la lista completa de colaboraciones (13.1) y confirma
que **no existe un juego propio de Frieren**; lo comprobé otra vez yo mismo
buscando en TCRF (`site:tcrf.net Frieren` → cero páginas; el buscador
directo de tcrf.net da 403/verificación anti-bot con curl y con
`navegar.py`, dos intentos, ninguno pasó) ⚠️ **confirma que no hay
contenido descartado que documentar, porque no hay juego** — no es un
hueco de mi búsqueda.

- **MapleStory × Frieren (nuevo, 9-sep a 7-oct-2026, no estaba en la
  hermana con este detalle)**: el evento **empieza con una estatua de
  bronce que aparece en «Mushroom Hill»**, una zona clásica de MapleStory,
  antes de que Frieren y su grupo «lleguen» al Mundo Maple. Actividades:
  «Frieren's Spell Collection Event» (misiones semanales y jefes para
  coleccionar **grimorios**) y «Adventure with Frieren's Companions»
  (Frieren y Fern ayudan en combate con sus hechizos); hay mascotas «Petite
  Luna» temáticas y trajes de personaje · fuentes:
  [Noisy Pixel](https://noisypixel.net/maplestory-frieren-beyond-journeys-end-collaboration-september-2026/)
  y [Nexon, micro-site oficial](https://www.nexon.com/maplestory/micro-site/frieren)
  ✅ (dos fuentes, una de prensa del sector y el sitio oficial de Nexon).
- **Por qué importa para «paisajes y memoria»**: **el motivo del monumento
  conmemorativo de Himmel** (ya descrito por la hermana en su Punto 25.3:
  «las estatuas de Himmel están en todas partes») **se repite hasta en un
  crossover**: la propia mecánica de entrada al evento de MapleStory es
  «aparece una estatua de bronce» — el objeto-símbolo de la serie viaja
  intacto a un paisaje que no es el suyo. Es un argumento visual más para
  usar una estatua o un pedestal como objeto central de una lámina.
- No vi capturas de la caja de diálogo dentro de MapleStory (el evento
  empezó el mismo día del cierre de esta tanda) ⚠️ dato de fecha y mecánica
  confirmado, pantallas de texto sin confirmar.

### Punto 18 · Estilo de dibujo y técnica — foco fondos, luz y melancolía

Esto es el núcleo del encargo 89. La hermana ya documentó el flujo de
color/sombreado del personaje (Clip Studio) y el shader de Blender; aquí
me centro en **los fondos, la luz y cómo se construye la melancolía**, con
fuentes que la hermana no cita.

**A) De dónde sale el paisaje (referencias reales, no inventadas)**

- El mundo de Frieren **no copia un lugar real único**: mezcla
  arquitectura de piedra alemana, casas de entramado de madera checas
  (estilo Praga) y el paisaje de la Suiza Sajona, según blogs japoneses de
  turismo de peregrinaje · fuentes:
  [libert.co.jp](https://libert.co.jp/pilgrimage-guild/frieren-pilgrimage/)
  y [yutorilog.com](https://yutorilog.com/frieren-stage/) ⚠️ (ningún
  estudio lo confirma como lugar único; tratarlo como «atmósfera», no como
  localización exacta — mismo aviso que ya dejó mi compañera de imagen en
  su Punto 16, coincido con ella).
- **7 sitios reales de peregrinaje de fans en Japón**, catalogados por
  AniTabi (mapa de peregrinaje de anime), cada uno con qué elemento del
  mundo de Frieren recuerda: **Yufuin** (pueblo balneario con casco de
  aire europeo, al pie del monte Yufu), **Huis Ten Bosch** (parque temático
  de pueblo holandés, Nagasaki), **Warmth Forest** (parque temático de
  aire medieval, Shizuoka), **Lockheart Castle** (castillo escocés real,
  trasladado piedra a piedra a Japón), las **ruinas del ferrocarril Kumaen**
  (refugios de piedra octogonales, Kumamoto — con tour oficial de
  colaboración «Welcome to Kumamoto Journey»), **Laguna Ten Bosch**
  (Aichi, con evento de colaboración oficial) y el **Parque Marino de
  Hitachi, colina Miharashi** (Ibaraki) · fuente:
  [AniTabi, Frieren (en inglés)](https://anitabi.jp/works/36?lang=en) ✅
  (mapa colaborativo de fans con coordenadas, cruzado con las guías
  japonesas de arriba).
- **El campo de nemófilas de Hitachi = el modelo real de la «hierba luna
  azul» (蒼月草)** que Frieren hace crecer en la tumba de Himmel (ya descrita
  por la hermana en su Punto 25.3, sin este dato): el color azul y la
  forma de crecer «cubriendo el suelo» de la nemófila coinciden con el
  蒼月草 dibujado en la serie; cada abril-mayo el parque se llena de fans
  haciendo cosplay ahí mismo · fuentes cruzadas:
  [nlab.itmedia.co.jp](https://nlab.itmedia.co.jp/cont/articles/3377207/)
  (cosplay viral, 230 mil «me gusta») y
  [AniTabi, ficha del sitio](https://www.anitabi.jp/spots/2841) ✅ (dos
  fuentes japonesas independientes). **Es la referencia real más citable
  para pintar el campo de flores de la memoria de Himmel.**

**B) Cómo se hace el fondo, según quién lo hace (fuente nueva: Sakuga
Blog, análisis técnico en inglés, oct-2023)**

- **Seiko Yoshioka no es sólo «concept artist»**: está acreditada también
  como **«layout designer» de cada episodio** y, desde el episodio 3, como
  **«worldview illustrator»** (ilustradora de la cosmovisión). El equipo
  llama a parte de su trabajo **«color script»**. El propio director
  Saitou reconoce que, al costarle explicar todo verbalmente al equipo,
  **dejó que las pinturas de Yoshioka hicieran ese trabajo**: no sólo pintó
  el mundo, sino que imaginó cómo vive la gente en él y qué fabrican, con
  referencias reales de plantas y utensilios de cada región · fuente:
  [Sakuga Blog, «Crafting a Tangible, Aging World»](https://blog.sakugabooru.com/2023/10/05/crafting-a-tangible-aging-world-frieren-beyond-journeys-end-production-notes-01-04/)
  ✅ (coincide y amplía la entrevista de mdn.co.jp que ya cita la hermana:
  ambas fuentes independientes describen el mismo reparto de tareas
  Yoshioka/Takagi).
- **Yoshioka pinta variantes estacionales de casi todos los sitios del
  mundo** — el paso de las estaciones está resuelto desde el concept art,
  no sólo con un filtro de color encima; es la base técnica de por qué el
  «mismo sitio» se ve distinto cuando Frieren vuelve años después (mismo
  fuente, Sakuga Blog) ⚠️ (un solo artículo lo dice así de explícito, pero
  encaja con el patrón de «paisaje revisitado» que documenta también el
  análisis de Unwinnable, abajo).
- **Textura de decadencia animada a propósito**: en el ep. 4, la animadora
  **Yoshiko Matsumura** (la misma acreditada como «Design Works» en el
  staff, ya en `datos-texto.md`) insistió mucho en dar «textura de
  decadencia» al dibujo de un sello mágico que se degrada con el tiempo,
  según cuenta el propio director — la decadencia física **se anima como
  textura**, no sólo se pinta como color plano · misma fuente, Sakuga Blog
  ✅ (relato directo del staff, citado por un analista técnico
  especializado en producción de anime).
- **El boceto de producción real que ya encontró mi compañera de imagen**
  (Punto 16 de `imagen.md`, no repito el enlace): el embarcadero nevado de
  Lake Korridor, en grises con los personajes marcados en rosa. Confirma
  el **orden de trabajo**: primero valores de luz/sombra en gris, encaje
  de cámara con los personajes en un color de encaje (no el color final),
  y el color de verdad llega después. **Es el paso 1 que hay que copiar en
  Photoshop antes que nada** (ver «Cómo reproducirlo» abajo).

**C) El vocabulario estético de la melancolía (fuente nueva: análisis en
inglés sobre estética japonesa aplicada a Frieren)**

- Un ensayo dedicado entero a analizar Frieren con conceptos de estética
  japonesa que el inglés no traduce bien, útil como **vocabulario de
  guía de estilo** (punto 17, lo redacta el redactor, pero aquí dejo la
  cantera) · fuente:
  [Unwinnable, «The Aesthetics of Impermanence»](https://unwinnable.com/2026/03/16/the-aesthetics-of-impermanence-how-frieren-visualizes-untranslatable-japanese-philosophy/),
  Beatrix Kondo, 16-mar-2026 ⚠️ (un solo artículo crítico, no una fuente
  del estudio; lo marco ✅ sólo en los puntos donde coincide con Real Sound
  /Saitou, ya citado por la hermana):
  - **mono no aware** (la belleza de lo que se acaba): «los mismos campos,
    los mismos caminos, los mismos paisajes visitados otra vez a través de
    décadas o siglos» — Frieren de pie donde antes estuvieron sus amigos.
  - **ma** (el silencio con peso): la cámara **se queda quieta en un
    paisaje** —montañas al amanecer, bosques en otoño, pueblos nevados—
    como «espacio para respirar» antes y después de una escena importante.
  - **shizukesa** (quietud): **paleta de pasteles apagados** —verdes
    suaves, azules tenues, tonos tierra cálidos— «que recuerda a la
    animación clásica dibujada a mano o a la sobriedad estética de Studio
    Ghibli»; la cámara casi no hace movimientos bruscos.
  - **wabi-sabi** (belleza en lo imperfecto): la serie **no evita pintar
    ruinas** cuando Frieren vuelve a una ciudad que conoció hace siglos —
    muros de piedra desmoronados, vigas podridas, estatuas cubiertas de
    musgo, jardines invadidos por la maleza — «decadencia digna,
    envejecida con gracia», nunca trágica.
  - **yohaku** (espacio en blanco intencional): ya citado en el Punto 6
    (la autobiografía de Himmel es el ejemplo perfecto y **confirmado con
    dos fuentes**, a diferencia del resto de este bloque).
- **Comparación directa con Studio Ghibli** (fuente distinta, más
  concreta): «los fondos de Frieren se parecen más a las escenas dibujadas
  a mano y fluidas de Ghibli que a otras series modernas»; «la paleta
  suave recuerda a la animación vintage», sin los colores muy saturados
  del anime moderno · fuente:
  [FandomWire, Aaheli Pradhan](https://fandomwire.com/frieren-beyond-journeys-end-has-the-essence-of-a-studio-ghibli-film/),
  28-jun-2025 ⚠️ (una fuente de crítica, sin cita directa del estudio; pero
  coincide en el diagnóstico de paleta con el ensayo de Unwinnable arriba
  → ✅ combinado en el punto concreto de «paleta pastel, poco saturada»).

**D) Cómo reproducirlo (complemento a la receta ya escrita por la
hermana en Photoshop/Blender — aquí sólo lo nuevo, específico de fondos)**

1. **Boceto de valores primero, color después** (confirmado con el
   boceto real de producción, arriba): dibuja el fondo entero en escala
   de grises marcando sólo luz/sombra y la posición de los personajes con
   una mancha de un solo color (rosa o el que sea, sin detalle). No pintes
   color hasta tener resuelta la composición de luz.
2. **Variante estacional del mismo sitio**: si la lámina necesita
   «memoria», pinta (o describe a la IA) el mismo fondo en dos estaciones
   —por ejemplo, el mismo camino en primavera con flores y en invierno
   nevado— y usa una versión pequeña de la otra estación como «recuerdo»
   superpuesto con opacidad baja (25-35 %) y un halo dorado, como el
   truco de «campo de flores» ya citado por la hermana.
3. **Ruinas con «decadencia digna»**: en vez de grietas caóticas, usa
   **musgo verde apagado, piedra desgastada por agua (más clara en las
   partes que reciben lluvia) y vegetación que crece ordenada dentro de
   la estructura** (enredaderas siguiendo las líneas de un arco, no al
   azar). Textura libre CC0 recomendada:
   [ambientcg.com, buscar «stone wall weathered»](https://ambientcg.com/api/v2/full_json?type=Material&q=stone)
   ✅ (API ya listada en AYUDANTE.md).
4. **Paleta de referencia real, no inventada**: usar como referencia de
   color el campo de nemófilas de Hitachi (azul-violeta que cubre el
   suelo, arriba) para el campo de flores de la memoria, en vez de un
   azul de fantasía sin referencia.
5. **Letra grabada** para una lápida o placa de piedra en la escena:
   Kaisei Tokumin o Zen Antique (punto 5), nunca una letra de palo seco.

**Encuadres para la melancolía** (de los mismos análisis en inglés,
Unwinnable + Sakuga Blog): plano fijo largo sobre un paisaje vacío
(«ma»), sin nadie en cuadro o con el personaje muy pequeño dentro del
encuadre (para dar sensación de tiempo/vastedad); montajes muy rápidos de
varios paisajes seguidos para decir «pasaron años» (recurso que mi
compañera de vídeo ya documentó con minuto exacto en su Punto 4, no lo
repito aquí, sólo lo enlazo como el mismo tema).

### Punto 24 · Obras parecidas y temas relacionados — foco paisaje/nostalgia

La hermana ya tiene la lista de recomendaciones de AniList (Violet
Evergarden, Delicious in Dungeon, Mushishi, Kino's Journey, Girls' Last
Tour, Maquia, Spice and Wolf…) y la influencia citada por el propio autor
(*Nemu the Corpse Carrier*). **No repito esa lista.** Lo nuevo, con la
lupa de «paisaje + melancolía»:

- **Yokohama Kaidashi Kikou (よこはま買い出し紀行)**, recomendada junto a Frieren en
  varias listas especializadas por compartir el mismo tono: un mundo
  post-apocalíptico que se apaga muy despacio, con «campo exuberante» y el
  mar subiendo poco a poco; la dueña de una cafetería (una androide) vive
  tardes que pasan lentas; el tema es **mortalidad, legado e
  impermanencia**, con un mundo que «acepta su final con elegancia» — el
  paralelismo más directo con el tono de Frieren de todos los que
  encontré · fuentes:
  [CBR, «10 Cozy Anime as Surprisingly Deep as Frieren»](https://www.cbr.com/10-cozy-anime-that-are-surprisingly-deep/)
  y recomendaciones cruzadas en
  [MyAnimeList](https://myanimelist.net/recommendations/anime/975-52991)
  ✅ (dos fuentes independientes recomendando el mismo cruce).
- **Kino's Journey**, con el mismo enfoque de «paisaje bonito usado para
  hablar de otra cosa» (moral, crueldad de la tradición, la sociedad):
  ya estaba en la lista de la hermana como recomendación de AniList, pero
  aquí lo confirmo con un análisis textual que lo compara con Frieren
  específicamente por ese uso del paisaje · misma fuente CBR arriba ✅.
- **Studio Ghibli, como referencia de paleta y fondo (no como una película
  concreta)**: ver el detalle completo en el Punto 18 (FandomWire); lo
  anoto aquí también porque es la comparación de «obra parecida» más
  repetida en la prensa en inglés sobre Frieren.
- **Qué otras láminas del servidor se le parecen (hallazgo nuevo,
  importante para el canal)**: revisé `biblias/` buscando series ya
  terminadas con temática de paisaje/naturaleza real:
  - **`100-la-princesa-mononoke`** (biblia terminada, 620 líneas) **ya
    propone el canal `#📸・fotos` (etiqueta «Naturaleza») como candidato**
    para su lámina (concepto secundario, no el ⭐ recomendado, que usa
    `#🎨・arte`) — el mismo canal de fotografía que yo había identificado
    como el más lógico para «paisajes y memoria» de Frieren (el foro trae
    justo la etiqueta «Paisaje», ver `servidor/inventario.md` l. 172) ✅
    visto directamente en `biblias/100-la-princesa-mononoke/biblia.md`
    (líneas 525-553). **Si el redactor de esta biblia (89) también apunta
    a `#📸・fotos`, hay que diferenciar el ángulo**: Mononoke usa el bosque,
    los espíritus y el renacimiento de la naturaleza; Frieren debería
    usar el viaje, la luz de una hora del día concreta y el paso del
    tiempo — no repetir «bosque que revive», mejor «paisaje que la
    memoria revisita».
  - **`101-your-name-cielos-y-ciudades`** y **`102-el-estilo-ghibli-en-general`**:
    existen como carpetas con las 4 partes de investigador **ya escritas**
    (incluida su propia `texto.md`) pero **sin `biblia.md` ni canal
    decidido todavía** — comparten territorio de «cielos, ciudades, estilo
    Ghibli» con esta biblia; no hay lámina publicada con la que chocar
    todavía, pero **quien redacte después debería mirarlas antes de fijar
    canal**, para no repetir concepto cuando esas dos se completen ⚠️
    (dato de estado, no de contenido: no leí sus 4 partes enteras, sólo
    comprobé que existen y no tienen biblia).

### Punto 25 · El mundo, la historia y sus símbolos — foco memoria

La hermana ya documentó las reglas del mundo (maná, rangos de mago,
supresión de maná, esperanzas de vida), los arcos del manga con capítulo y
el vocabulario (Zoltraak, Aureole, Mimic, «Himmel lo habría hecho»). **No
repito nada de eso.** Lo nuevo, centrado en memoria:

- **El mapa oficial es, literalmente, un mapa de recuerdos**: la página
  «旅の軌跡を辿る地図» (Punto 5, arriba) numera **los 28 episodios de la T1**
  como si fueran paradas de un viaje. Lista completa de títulos
  (numerados con el círculo japonés tal cual aparecen en la web oficial),
  útil como guion de una lámina tipo «mapa»:
  ①冒険の終わり ②別に魔法じゃなくたって… ③人を殺す魔法 ④魂の眠る地 ⑤死者の幻影 ⑥村の英雄
  ⑦おとぎ話のようなもの ⑧葬送のフリーレン ⑨断頭台のアウラ ⑩強い魔法使い ⑪北側諸国の冬 ⑫本物の勇者
  ⑬同族嫌悪 ⑭若者の特権 ⑮厄介事の匂い … ㉒次からは敵同士 ㉓迷宮攻略 ㉔完璧な複製体 ㉕致命的な隙
  ㉖魔法の高み ㉗人間の時代 **㉘また会ったときに恥ずかしいからね** (título del último
  episodio de la T1: «porque sería vergonzoso [no haber cambiado] para
  cuando nos volvamos a ver» — la frase-cierre más «memoria» de toda la
  temporada) · fuente: [frieren-anime.jp/special/map/](https://frieren-anime.jp/special/map/)
  ✅ (leído directamente por mí, texto oficial completo; los títulos
  16-21 no se capturaron bien en la lectura de texto —posible fallo de
  orden del HTML— y quedan pendientes de revisar si hace falta la lista
  entera).
- **La estatua de Himmel, analizada como un objeto legal/funerario real**:
  un blog especializado en herencias y tumbas (una notaria pública)
  analiza la estatua de Himmel con el mismo lenguaje que usaría para una
  sepultura real: «el monumento cumple la misma función que una tumba»,
  «lugar de apoyo espiritual» (心の拠り所) para que los vivos sigan
  conectados con el muerto; y describe cómo la creencia de Himmel «sigue
  viva en Frieren, y luego se hereda a Fern y Stark» (継承, la misma
  palabra que usaría un notario para «sucesión») · fuente:
  [office-tokiwa.com, «アニメ『葬送のフリーレン』ヒンメルの銅像に学ぶ「継承」の形»](https://office-tokiwa.com/eiga24/),
  30-ago-2024 ✅ (coincide y amplía el dato que ya tenía la hermana en su
  Punto 25.3 —«las estatuas de Himmel están en todas partes»— con una
  lectura simbólica nueva y con fuente propia).
- **El monasterio del Lago Korridor**, donde se guarda la autobiografía de
  Himmel (Punto 6), es también un **sitio con nombre propio dentro de la
  lista de +30 lugares** que ya encontró mi compañera de imagen en la
  categoría `Locations` de la wiki (Punto 16 de `imagen.md`) — lo señalo
  aquí como el lugar concreto que uniría «paisaje» (el lago) y «memoria»
  (el libro) en un único sitio, si se quiere un concepto de lámina con
  edificio real.
- **El motivo de la estatua conmemorativa cruza hasta los crossover**:
  ver Punto 11 (MapleStory) — la estatua de bronce en «Mushroom Hill» abre
  el evento oficial, repitiendo el símbolo fuera de la historia original.

## Lo mejor para la lámina

- **La autobiografía de Himmel, con sus páginas en blanco al final** (ep.
  37, T2): el objeto de memoria más fuerte y mejor documentado (dos
  fuentes) de toda esta parte — libro real, sitio real (el monasterio del
  lago), letra a mano, sin necesidad de un globo de diálogo.
- **El campo de nemófilas del Parque Marino de Hitachi**: referencia real
  y fotografiable (no inventada) para pintar el campo de flores de la
  memoria de Himmel — azul-violeta cubriendo el suelo, confirmado por dos
  fuentes japonesas.
- **Ojo con el canal**: `100-la-princesa-mononoke` ya propone `#📸・fotos`
  (etiqueta «Naturaleza») como candidato secundario — si el redactor de
  esta biblia apunta al mismo canal, diferenciar el ángulo (viaje/luz de
  una hora concreta/tiempo que pasa, no bosque que revive).
- **Kaisei Tokumin, Zen Antique y Shippori Antique**: tres letras OFL
  verificadas por mí con fontTools (con ñ, tildes, ¿ y ¡), listas para
  texto grabado en piedra o de diario, sin depender de la letra de pago
  del logo.
- **El mapa oficial «旅の軌跡を辿る地図»** (números en círculo sobre los 28
  títulos de episodio) es un concepto ya hecho por el propio estudio de
  «viaje = mapa de recuerdos»: se puede citar como inspiración directa
  para una lámina en forma de mapa.

## No encontré

- ⚠️ **El mapa visual de `frieren-anime.jp/special/map/`** (el dibujo del
  recorrido, no sólo los títulos): protegido con verificación JS de
  Cloudflare; `--captura` con `navegar.py` dio pantalla en blanco. Mi
  compañera de imagen también lo intentó y además probó la Wayback
  Machine, bloqueada igual («blocked by egress policy»). Dos personas, dos
  vías, mismo bloqueo: lo dejo documentado por si alguien con otro acceso
  puede reintentarlo.
- ⚠️ Confirmación de una **segunda fuente** para que **「文游明朝体 勇壮かな」**
  sea de verdad la letra del avance de episodio de Frieren (sólo una
  respuesta de Yahoo!知恵袋, con duda del propio autor). Búsquedas hechas:
  `文游明朝体 勇壮かな フリーレン`, `モリサワ 使用例`.
- ⚠️ Un **lugar real único** confirmado por el propio estudio como
  inspiración del mundo (sólo hay guías de turismo de fans que hablan de
  «mezcla» de Alemania y Chequia). Búsquedas hechas (ja):
  `葬送のフリーレン 背景美術 聖地巡礼 ロケハン 実在の場所`; (en):
  `Frieren anime background art real world location inspiration pilgrimage`.
- No hay **videojuego propio de Frieren** que documentar en TCRF (The
  Cutting Room Floor): confirmado con `site:tcrf.net Frieren` (cero
  resultados) y dos intentos de abrir `tcrf.net` directamente (curl y
  `navegar.py`), los dos bloqueados por verificación anti-bot de
  Cloudflare. No es un hueco de búsqueda: no hay nada que cortar, porque
  no hay juego (coincide con la hermana).
- ⚠️ **Wiki coreana (namu.wiki) y china (zhihu)**: intenté
  `장송의 프리렌/설정/국가 및 지역` (namu.wiki, la página de países y regiones del
  mundo) y una pregunta de análisis de estilo en zhihu; las dos me
  bloquearon con verificación anti-bot (curl y `navegar.py`, dos intentos
  cada una). Sí conseguí resultados útiles del buscador en coreano y en
  chino simplificado (ver Bitácora), aunque de menor calidad que las
  fuentes japonesas e inglesas ya citadas arriba.
- No fue necesario usar YouTube directamente para esta parte: los
  hallazgos salieron de sitios oficiales (`frieren-anime.jp`), prensa
  especializada (Sakuga Blog, Unwinnable, FandomWire, CBR, Noisy Pixel,
  Nexon) y blogs japoneses verificados en dos fuentes cuando hacía falta.

## Bitácora

- WebSearch (ja): `葬送のフリーレン 背景美術 聖地巡礼 ロケハン 実在の場所` →
  [libert.co.jp](https://libert.co.jp/pilgrimage-guild/frieren-pilgrimage/),
  [yutorilog.com](https://yutorilog.com/frieren-stage/)
- WebSearch (en): `Frieren anime background art real world location inspiration pilgrimage`
  → [AniTabi](https://anitabi.jp/works/36?lang=en)
- WebFetch: frieren-anime.jp/special/map/ (403 con WebFetch normal) →
  reintentado con `navegar.py --selector body` (200, texto completo de los
  28 títulos); `--captura` dio pantalla en blanco (mapa dibujado con JS)
- WebFetch: anitabi.jp/works/36 (lista de 7 sitios de peregrinaje)
- WebSearch (ja): `葬送のフリーレン 聖地巡礼 ひたち海浜公園 ネモフィラ 蒼月草 モデル` →
  [nlab.itmedia.co.jp](https://nlab.itmedia.co.jp/cont/articles/3377207/),
  [anitabi.jp/spots/2841](https://www.anitabi.jp/spots/2841)
- WebSearch (ja): `葬送のフリーレン 美術ボード 画集 背景 光 インタビュー 高木佐和子` →
  [animageplus.jp](https://animageplus.jp/articles/detail/55395) (poco
  contenido descriptivo, descartado)
- WebSearch (en): `Frieren anime lighting nostalgia melancholy analysis mono no aware backgrounds article`
  → [Unwinnable](https://unwinnable.com/2026/03/16/the-aesthetics-of-impermanence-how-frieren-visualizes-untranslatable-japanese-philosophy/)
- WebFetch/navegar: unwinnable.com (artículo completo, 23.6k caracteres,
  leído en dos tandas)
- WebSearch (en): `Frieren anime compared Studio Ghibli Isao Takahata landscape nostalgia influence article`
  → [FandomWire](https://fandomwire.com/frieren-beyond-journeys-end-has-the-essence-of-a-studio-ghibli-film/)
- WebFetch: fandomwire.com (citas textuales sobre fondos/paleta)
- WebSearch (en): `"Frieren" anime "Yokohama Kaidashi Kikou" OR "Mushishi" landscape melancholy comparison essay`
  → [CBR](https://www.cbr.com/10-cozy-anime-that-are-surprisingly-deep/),
  MyAnimeList (recomendaciones cruzadas)
- WebFetch: cbr.com (lista de animes parecidos, con cita por título)
- WebSearch (ja): `葬送のフリーレン テロップ 字幕 "年後" 書体 フォント アニメ` →
  [Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14289239084)
- WebFetch: chiebukuro.yahoo.co.jp (fuente del avance de episodio)
- WebSearch (ja): `文游明朝体 勇壮かな フリーレン OR モリサワ 使用例` →
  [morisawa.co.jp/fonts/specimen/6593](https://www.morisawa.co.jp/fonts/specimen/6593)
  (ficha oficial del tipo, sin ejemplo de uso en Frieren)
- WebSearch (ja): `葬送のフリーレン 墓 墓標 文字 刻まれた ヒンメル` →
  [office-tokiwa.com/eiga24](https://office-tokiwa.com/eiga24/)
- WebFetch: office-tokiwa.com/eiga24 (estatua de Himmel, tumbas y memoria)
- WebSearch (ja): `フリーレン 2期 37話 ヒンメル 自伝 湖畔の街 修道院 書物` →
  [frieren-anime.jp/story/2nd/ep37](https://frieren-anime.jp/story/2nd/ep37/),
  [dogadaijobu2025.com](https://dogadaijobu2025.com/archives/8036),
  [note.com/sakuraigo](https://note.com/sakuraigo/n/n179c6ef7e84e)
- WebFetch: frieren-anime.jp/story/2nd/ep37 (sinopsis y créditos oficiales)
- WebFetch/navegar: dogadaijobu2025.com (reseña larga del episodio 37)
- WebFetch/navegar: note.com/sakuraigo (cita exacta de la página en blanco)
- WebSearch (ja): `MapleStory Frieren collaboration map area background screenshot September 2026`
  → [Noisy Pixel](https://noisypixel.net/maplestory-frieren-beyond-journeys-end-collaboration-september-2026/),
  [Nexon](https://www.nexon.com/maplestory/micro-site/frieren)
- WebFetch/navegar: noisypixel.net (detalle del evento, estatua de bronce)
- WebSearch (Herramientas propias): `curl api.php` y `navegar.py` sobre
  `tcrf.net` (bloqueado, verificación Cloudflare, 2 intentos); búsqueda
  `site:tcrf.net Frieren` (cero resultados, confirma que no hay juego)
- WebSearch (ko): `장송의 프리렌 배경 미술 풍경 분석 서정적` → namu.wiki (bloqueado al
  intentar leerlo, 2 intentos: curl y `navegar.py`), ko.wikipedia.org
- WebSearch (zh): `葬送的芙莉莲 背景美术 风景 光影 分析` → resultados de baja calidad
  (wallpapers, sitios de dudosa fiabilidad), zhihu bloqueado al intentar
  leer la pregunta de estilo de dibujo (2 intentos)
- Fontsource API: `api.fontsource.org/v1/fonts?subsets=latin-ext` (lista
  completa, filtrado por Python para familias «zen/shippori/antique/kaisei»)
- Descarga y verificación con fontTools: `kaisei-tokumin.ttf`,
  `shippori-antique.ttf`, `zen-antique.ttf` desde `fonts.gstatic.com`,
  comprobados los 15 caracteres (á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü) con
  `TTFont(f).getBestCmap()`
- Herramientas propias: `python3 herramientas/seccion.py 33-frieren --indice`
  y lectura de las secciones 6, 7, 13, Punto 18, Punto 24 y Punto 25 de
  `biblias/33-frieren/biblia.md` (para no repetir)
- Repositorio: `ls biblias/`, lectura de
  `biblias/100-la-princesa-mononoke/biblia.md` (canal `#📸・fotos` ya usado
  como candidato) y comprobación de que `101-your-name-cielos-y-ciudades`
  y `102-el-estilo-ghibli-en-general` tienen partes pero no biblia
- Lectura de `servidor/inventario.md` (canal `#📸・fotos`, etiqueta
  «Paisaje», línea 172) y de las partes ya escritas por mi equipo:
  `biblias/89-frieren-paisajes-y-memoria/partes/imagen.md` y `video.md`

Revisado contra ENCARGO.md: los puntos 5, 6, 11, 18, 24 y 25 quedan
cubiertos con fuentes propias (no repetidas de la hermana). Los ⚠️ de
«No encontré» son detalle extra o bloqueos de red ya documentados con sus
dos intentos, no puntos obligatorios sin cubrir.
