# Parte del investigador de TEXTO, JUEGOS Y TÉCNICA · Mafalda (09-mafalda)

Puntos de `ENCARGO.md`: **5** (tipografía), **6** (cómo habla en pantalla), **11**
(videojuegos), **18** (estilo y técnica, cómo replicarlo), **24** (obras
parecidas) y **25** (el mundo, la historia y sus símbolos).

Repaso con la red abierta sobre la `biblia.md` ya escrita (se hizo con la red
cerrada). No repito lo que ya está ✅ en la biblia; sólo confirmo lo ⚠️ de mis
puntos y añado 18, 24 y 25, que no existían como secciones propias. Un dato por
línea, con fuente y ✅/⚠️.

---

## Punto 5 · Tipografía

### Confirmado: Quino rotulaba en MAYÚSCULAS
- Bajé dos tiras reales de la wiki de Fandom y las miré directamente
  (`Read`) más OCR con `tesseract -l spa`: **todo el rotulado está en
  mayúsculas**, sin excepción, en ambas · [Basilio.jpg](https://static.wikia.nocookie.net/mafalda/images/8/8d/Basilio.jpg) (800×228, wiki de Mafalda),
  [Muertemafalda.jpg](https://static.wikia.nocookie.net/mafalda/images/b/bc/Muertemafalda.jpg) (640×195, wiki de Mafalda) · ✅ (visto + OCR + ya
  apuntaba a esto [Cadena 3](https://www.cadena3.com/noticia/siempre-juntos/una-vineta-de-mafalda-de-1973-viral-por-describir-el-panorama-politico-actual_372684)
  en la biblia). **Cambia el ⚠️ de la biblia a ✅: usar MAYÚSCULAS siempre.**
- La tira de Basilio tiene **5 viñetas, no 4** (ver punto 6): confirma que el
  número de viñetas variaba día a día.

### La letra «Quino» (Esteban Garrido / Garrido-Nieto): sigue ⚠️, pero ahora con motivo claro
- Probé bajar el archivo real para pasarlo por `fontTools` (como pide la
  tarea): **bloqueado dos veces** · 1001fonts.com pide iniciar sesión para
  descargar; onlinewebfonts.com da una página HTML (captcha), no la fuente ·
  dafontfree.net y blogfonts.com dan 403 a `curl` (protección anti-bot) y no
  traen enlace directo. Dos intentos por sitio, como marca `AYUDANTE.md`;
  no sigo insistiendo.
- **Las licencias de los espejos se contradicen** (dato nuevo, útil): 1001
  Free Fonts dice «libre para uso personal y comercial»
  ([1001 Free Fonts](https://www.1001freefonts.com/es/quino.font)) ⚠️, pero
  DaFontFree.net dice **sólo uso personal**, «mirar el léame o la web del
  autor» ([DaFontFree](https://www.dafontfree.net/quino-regular-font/f250611.htm))
  ⚠️. Diseñador: **Esteban Garrido-Nieto**, 102 glifos, 90,2 KB. **Con dos
  fuentes que se contradicen: tratarla como sólo-personal y sin tildes
  comprobadas.** No usar para nada comercial del servidor.
- **Alternativa real:** con 47 letras de Google Fonts ya comprobadas con
  fontTools (dato de la biblia), quedarse con **Patrick Hand** o **Short
  Stack**, que sí llevan tildes, ñ, ¿ ¡ confirmadas.

### La fuente de Frank Wynne (traductor inglés): confirmado que es privada, con la cita exacta
- Cita textual de Wynne, ahora con la fuente abierta y leída entera (antes
  sólo se citaba, sin abrir): *«I literally scanned every single letter of
  the alphabet in Quino's handwriting, and then again in his bold version,
  and then I scanned a whole bunch of the punctuation marks... And I
  created a font that meant that I can actually do this using his hand
  lettering.»* ([Harte, Substack](https://harte.substack.com/p/soup-is-to-childhood-what-communism))
  ✅ (texto exacto, primera persona).
- Busqué en dos entrevistas más de la traducción al inglés (2025,
  Archipelago Books, edición «Mafalda: Book One», 5 tomos): **ninguna
  menciona que la fuente se haya publicado** ([Latin American Literature
  Today](https://latinamericanliteraturetoday.org/2025/09/the-anglophone-world-is-ready-for-mafalda-a-conversation-with-frank-wynne/),
  [The Dial](https://www.thedial.world/articles/news/issue-28/mafalda-english-translation)).
  **Confirmado con dos fuentes que no aparece pública en ningún sitio de
  letras**: sigue siendo una herramienta privada de Wynne. Mantener ⚠️ pero
  ya no «sin comprobar»: comprobado que no está disponible.

---

## Punto 6 · Cómo habla en pantalla (el «cuadro de diálogo» de la serie)

### Confirmado: cada personaje tiene su propio discurso (los globos no son intercambiables)
- Antes citado sin abrir. Abrí el artículo: **Juan Matías Loiseau, «Tute»**
  (dibujante al que Quino aconsejó) dice textualmente que *«cada personaje
  debe tener una psicología, una personalidad distintiva. Los globos no
  deberían ser intercambiables»* entre personajes
  ([La Nación, «Mafalda, la grande»](https://www.lanacion.com.ar/lifestyle/mafalda-la-grande-nid1677806/))
  ✅.
- Segunda fuente, la wiki de Mafalda citando una entrevista real de 1987:
  *«Mafalda recurre al diálogo; la mayoría de las otras caricaturas de Quino
  son sin diálogo, más visuales»* (Rodolfo Braceli, libro *10 años con
  Mafalda*, 1987, citado en [Mafalda Wiki: Quino](https://mafalda.fandom.com/es/wiki/Quino))
  ✅. **Sube de ⚠️ a ✅ las dos afirmaciones de la biblia** (línea 551 y 555).
- Ojo: **dentro de la propia Mafalda también hay remates sin una palabra**
  (no sólo en el resto de la obra de Quino): vi una ilustración de Felipe
  caminando en silueta repetida hacia Susanita en un banco, sin texto
  ([Felipemuriel.jpg](https://static.wikia.nocookie.net/mafalda/images/a/a9/Felipemuriel.jpg),
  wiki de Mafalda) — matiza el dato, no lo contradice.

### Confirmado: el número de viñetas varía (no siempre son 4)
- Prueba visual directa: la tira de Basilio tiene **5 viñetas**
  ([Basilio.jpg](https://static.wikia.nocookie.net/mafalda/images/8/8d/Basilio.jpg))
  ✅. El plan de la lámina puede seguir usando 4 (formato típico de tira
  diaria), pero ya no hace falta el ⚠️: está confirmado que varía.

### Colores y trazo medidos con `herramientas/estilo.py` (pedido por la tarea)
- Sobre `Basilio.jpg`: paleta **#FEFEFE 41% (papel) · #060606 11% (tinta) ·
  grises intermedios #383838-#CECECE (tramas)**; «sombreado mixto, mucha
  línea, saturación 0%, brillo 69%» ✅ (medido).
- Sobre `Muertemafalda.jpg`: paleta **#F9F9F9 51% (papel) · #0B0B0B 6%
  (tinta) · grises #4D4D4D-#C3C3C3 (tramas)**; «sombreado mixto, mucha línea,
  saturación 0%, brillo 80%» ✅ (medido). Confirma que **no hay degradados
  reales**: los grises intermedios salen de rayado/trama, no de un
  degradado digital. Esto ya estaba en la biblia como ⚠️ «de memoria»: ahora
  está **medido**, sube a ✅.
- Texto de la cartela leído con `tesseract -l spa` sobre `Basilio.jpg`:
  reconoce sobre todo mayúsculas con ruido normal de letra a mano
  (`BUEN DÍA,DON BASILIO`, `¿SUS ZAPATOS?`, `LA SEMANA PASADA`…) — confirma
  el punto anterior. La tira de `Muertemafalda.jpg` (el camión **«SOPA /
  FOOD COMPANY INC.»**) no tiene texto de globo, sólo el rótulo del camión en
  letra de imprenta gruesa: sirve de ejemplo real de «cartel del mundo»
  (punto 5) y del símbolo de la sopa (punto 25).

### Confirmado (con matices): por qué la animación quitó las voces
- Cita textual de Quino sobre la serie de 1993: *«[buscaban] situaciones
  que se pudieran hacer sin que hablaran los personajes, que dijeran cosas
  con estos idiomitas que no dicen nada»*, para que «el gag se concentrara
  en el dibujo y la animación, y no en el texto»
  ([NODAL, Guillermo Courau](https://www.nodal.am/2024/09/mafalda-en-el-cine-y-la-television-por-guillermo-courau/))
  ✅ (cita directa, antes sin abrir).
- Corrobora el motivo (voces criticadas) una fuente **distinta e
  independiente**: el crítico Raúl Manrupe, sobre los cortos de 1972,
  escribió que «faltó un ritmo... y las voces fueron particularmente
  criticadas»; el propio Quino los llamó «una versión edulcorada de
  Mafalda» ([Sonrisas Argentinas](http://sonrisasargentinas.blogspot.com/2011/08/en-1972-quino-cede-tanta-insistencia.html))
  ✅. **Sube de ⚠️ a ✅** (antes era «una sola fuente, repetida por el mismo
  autor»; ahora hay una segunda fuente, de otro autor, sobre el mismo
  motivo).
- Dato nuevo, corrige un «no encontré» de la biblia (punto 20: «compositor
  de la cortina... de la serie de 1993»): la serie de 1993 (Juan Padrón,
  **104 episodios**, estudio **ICAIC**, Cuba, 35 mm) tuvo música de **José
  María Vitier**, fotografía de Jorge Reyes, Dagmar Lorenzo y Alfredo
  Rodríguez, animación de Mario García-Montes
  ([ENDAC, ficha oficial cubana](https://endac.org/encyclopedia/mafalda/))
  ✅. (Dato para el investigador de voz/vídeo: pasa al apartado de música.)
- Los 1972: **72 cortos** de 90 segundos según [NODAL](https://www.nodal.am/2024/09/mafalda-en-el-cine-y-la-television-por-guillermo-courau/)
  vs **230 cortos** de 90 segundos según [Sonrisas Argentinas](http://sonrisasargentinas.blogspot.com/2011/08/en-1972-quino-cede-tanta-insistencia.html)
  ⚠️ (cifras distintas, no lo pude resolver con una tercera fuente).
  Coinciden en: director **Catú**, productor **Daniel Mallo**, estreno en
  TV **1973**, con voces de actores reales que a Quino no le convencieron.

### En los juegos (sin cambios: no aplica, ver punto 11)

---

## Punto 11 · Videojuegos

### App oficial: mucho mejor confirmada que antes
- La biblia sólo citaba `apptk.es` (⚠️). Encontré **el enlace oficial de
  Apple**: [App Store, «Mafalda»](https://apps.apple.com/ar/app/mafalda/id585754234)
  (id585754234) y la **página oficial del sitio de Quino**:
  [quino.com.ar/mafaldadigital](https://www.quino.com.ar/mafaldadigital)
  ✅ (dos fuentes, una de ellas del propio autor).
- Interfaz y contenido (de la propia web oficial): libros interactivos por
  tema («Mafalda y la sopa», «Mafalda y las fiestas», «Mafalda cuando sea
  grande»…), **~30 tiras y ~64 tomos en total**; minijuegos de **colorear,
  memoria y trivia**; un tomo gratis, el resto por compra dentro de la app;
  contacto `mafalda@panareadigital.com` (probable desarrolladora: Panarea
  Digital) ✅.
- **Conclusión sin cambios**: no hay cajas de diálogo ni menús propios de
  un videojuego narrativo; la app es un lector de tiras con minijuegos
  simples, no una interfaz a replicar como «juego».

### El juego de mesa: identificado con dos fuentes (antes sólo Facebook)
- «Jugando con Mafalda y sus amigos» es en realidad un **juego de memoria**
  (cartas para emparejar), no un juego de mesa de tablero: lo confirma un
  anuncio de coleccionismo, «ANTIGUO JUEGO, MEMORIA, JUGANDO CON MAFALDA,
  MUY RARO DE ENCONTRAR»
  ([todocoleccion.net](https://en.todocoleccion.net/educational-games/antiguo-juego-memoria-jugando-mafalda-muy-raro-encontrar~x197358146))
  ✅, además del grupo de Facebook ya citado en la biblia. Es una pieza
  vintage descontinuada, no algo que se pueda comprar hoy.
- Encontré también un juego de fans **«Las aventuras de Mafalda»**, un
  plataformero hecho por estudiantes: **una sola fuente, sin más datos**
  (nombre del canal o enlace), ⚠️. No lo confirmo del todo: dejar para
  quien quiera profundizar.

### The Cutting Room Floor: confirmado que no se pudo revisar (no que no exista)
- La biblia decía «no aplica, no hay videojuego». Intenté comprobarlo en la
  fuente misma: `tcrf.net` está detrás de Cloudflare y bloquea `curl`
  («Just a moment...», protección anti-bot) — **dos intentos, sin éxito**.
  No cambio la conclusión (sigue sin haber un videojuego grande de Mafalda
  con contenido cortado que documentar), pero el motivo correcto es «TCRF
  bloqueó el acceso», no que se comprobara vacío.

### Objeto 3D relacionado (para el punto 18, ver abajo)
- Hay un modelo de Mafalda en Sketchfab, con licencia libre: ver punto 18.

---

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo (NUEVO)

### La técnica real de Quino, con sus propias palabras
- Entrevista directa (cita textual, primera persona): *«Primero hago los
  bocetos con lápiz. Después dibujo con tinta china.»* Papel: **«Fabriano
  F4 o papel Schoeller»**. Plumas: **«plumillas francesas que se llaman
  'Blanzy', las que tienen el manguito naranja»** para personas y
  animales; **«Rotring núm. 1, 3 y 5»** para precisión (vehículos, objetos)
  ([La Nuez, entrevista a Quino](https://lanuez.blogspot.com/2008/04/quino-te-cuenta-como-dibuja.html))
  ✅.
- Sobre su propio trazo (otra entrevista, cita textual): *«¿Por qué oscila
  entre una línea limpia, casi a mano alzada, y el abigarramiento
  barroco?» — «Me molesta mucho cuando me pongo barroco, pero no lo puedo
  evitar.»* Sobre el detalle: *«¡No logro entender cómo es posible que a
  veces tengo que borrar 15 veces un puntito hasta que sale!»*
  ([Dreamers.es, entrevista a Quino](https://dreamers.es/mafalda/Entrevista/entrevista_a_quino.htm))
  ✅. **Para replicar el trazo**: personajes con línea limpia y mínima,
  fondos y objetos con más trama y detalle (el contraste es intencional,
  no un descuido).
- **Medido, no de memoria** (con `estilo.py`, ver punto 6): tinta casi
  negra (#060606–#0B0B0B), papel casi blanco (#FEFEFE/#F9F9F9),
  saturación 0%, sombreado por trama y rayado, **sin degradados**. Esto
  reemplaza el ⚠️ «de memoria» que tenía la biblia en la sección 18 vieja
  (línea 146).

### Cómo lo hicieron las adaptaciones (para el estudio o programa a imitar)
- **1993 (Juan Padrón, ICAIC, Cuba)**: animación tradicional en **35 mm**,
  dibujo a mano, coproducción con España (D.G. Producciones/TVE); música
  José María Vitier ([ENDAC](https://endac.org/encyclopedia/mafalda/)) ✅
  (ver cita completa en punto 6).
- **Netflix (2027, Mundoloco CGI)**: **no es 2D tradicional**. Dos fuentes
  de prensa especializada, independientes entre sí, describen la primera
  imagen oficial como animación **por computadora, estilizada, en 3D**, y
  la comparan directamente con *The Peanuts Movie* (2015, Blue Sky
  Studios): *«The character design and soft tactile textures recall The
  Peanuts Movie... a major step forward in stylized CG animation»*
  ([Cartoon Brew](https://www.cartoonbrew.com/series/mafalda-first-look-netflix-juan-jose-campanella-259859.html)),
  y *«el estilo recuerda a Snoopy y Charlie Brown: Peanuts (2015)... un
  hito en la animación computarizada»* ([ANSA Latina](https://www.ansalatina.com/americalatina/noticia/espectaculos/2026/04/12/llega-a-netflix-mafalda-rodada-por-un-premio-oscar_5486a721-80bd-4244-a9c3-5b80ef4e19c1.html))
  ✅. Ojo: en agosto de 2024, antes de ver imágenes, la prensa de animación
  todavía decía que 2D o 3D era «una de las dudas»
  ([Radix Animación](https://radixanimacion.com/noticias/mafalda-juan-jose-campanella-netflix/))
  — la duda se resolvió con la imagen de abril de 2026: es 3D estilizado.
  Estudio: **Mundoloco CGI** (de Campanella, el más premiado de la región,
  hace *Metegol* y *Mini Beat Power Rockers*).
  Luz de la primera imagen: «sombras suaves y una atmósfera cálida,
  ligeramente melancólica», luz lateral
  ([La Nación](https://www.lanacion.com.ar/espectaculos/netflix-argentina-mostro-la-primera-imagen-de-la-serie-animada-de-mafalda-y-emociono-a-todos-nid08042026/))
  ✅.
- **Por qué importa para Blender**: el propio Netflix ya está usando el
  camino de *The Peanuts Movie* — 3D con **toon shader** que imita el
  dibujo plano — así que es el mismo pipeline recomendado para una lámina
  en Blender.

### Filtros de imagen en las adaptaciones (grano, brillo): poco documentado, lo digo claro
- Busqué específicamente «grano», «filtro» o «aberración cromática» para las
  tres adaptaciones y **no encontré nada dicho por el estudio o la prensa
  especializada** sobre esto ⚠️. Lo único deducible por el formato: los
  cortos de 1972 y la serie de 1993 se filmaron en **35 mm** (dato
  confirmado en el punto de arriba, [ENDAC](https://endac.org/encyclopedia/mafalda/)),
  así que llevan el **grano fotoquímico propio del celuloide de la época**,
  no un filtro digital añadido — es una inferencia razonable, no una cita,
  la marco ⚠️. De Netflix (2027) sólo hay una imagen fija; nadie ha hablado
  todavía de grano, brillo o aberración cromática para la serie: no lo
  invento, queda en «No encontré».

### Cómo replicarlo en Blender
- **Contorno**: `Line Art` (modificador de Grease Pencil) o **Freestyle**
  sobre una malla 3D da el contorno negro grueso; alternativa clásica,
  **Solidify** con normales invertidas y material negro sin sombra. Tutorial
  gratuito que cubre justo esta combinación (línea + sombreado por trama,
  no degradado): [«How to make Line Art and Halftone Toon Shader in
  Blender»](https://cgian.com/blender-line-art/) ✅; nodo oficial **Toon
  BSDF** documentado en el [manual de Blender](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/toon.html)
  ✅ (fuente primaria del programa).
- **Sombreado**: Toon BSDF con 2 tonos (blanco/negro puro, saturación 0)
  en vez de degradado; para las tramas, una textura de puntos (halftone)
  proyectada sobre la sombra, no un degradado real — coincide con lo
  medido arriba.
- **Modelo base libre**: hay un modelo 3D de «Mafalda» en Sketchfab,
  licencia **CC Attribution** (crédito obligatorio, uso comercial
  permitido), autor **andresspa79**, malla estática (121.920 vértices, sin
  animación ni rig) — sirve como referencia de volumen o base, no trae
  rig para posar
  ([Sketchfab, ficha con licencia](https://sketchfab.com/3d-models/mafalda-9a5f14636a254068b71dddd58fcc3d46))
  ✅ (medido por la propia API de Sketchfab, `license.slug=by`).
- **Texturas encima**: coordinar con el investigador de imagen (puntos 4 y
  19) para el papel/grano; en Blender, mezclar esa textura con el shader
  Toon en modo Multiply, opacidad baja.

### Cómo replicarlo en Photoshop
- Boceto a lápiz en una capa, tinta en otra (imita el propio proceso de
  Quino: lápiz → tinta china), con un pincel de punta fina y **grosor algo
  irregular** (como una plumilla real, no una línea vectorial perfecta).
- **Tramas en vez de degradados**: pinceles de puntos (halftone) gratis y
  con licencia de uso comercial libre:
  [MyPhotoshopBrushes, halftone «Free for Commercial Use»](https://myphotoshopbrushes.com/resources/71/halftone-brushes),
  [PsFiles, halftone dots ABR](https://psfiles.com/halftone-dots-ps-brushes/),
  [Brusheezy, halftone/comic](https://www.brusheezy.com/free/comic-halftone)
  ✅ (packs con licencia libre confirmada en la propia página). Aplicar en
  modo Multiply sobre zonas de sombra, nunca degradado suave.
- Desaturar todo a 0% (blanco y negro puro, medido arriba); grano de papel
  por encima en opacidad baja (textura CC0 del punto 4/19 del investigador
  de imagen).

### Encuadres y composición (de una entrevista, con ejemplo real)
- Quino **investigaba sitios reales antes de dibujarlos** (visitaba
  carnicerías para copiar bien los mostradores) y ponía **chistes
  escondidos en el fondo** (objetos con nombres de amigos suyos); su
  montaje de viñetas guiaba al lector a propósito para reforzar el remate
  ([La Nación, entrevista a Tute](https://www.lanacion.com.ar/lifestyle/mafalda-la-grande-nid1677806/))
  ✅. **Para la lámina**: fondos simples salvo que el fondo SEA el chiste;
  basar objetos en fotos reales, no en formas genéricas; pensar el orden
  de viñetas como un guion de remate, no como ilustraciones sueltas.

---

## Punto 24 · Obras parecidas y temas relacionados (NUEVO)

### Influencias que Quino declaró él mismo (fuente primaria, cita directa)
- *«He tenido mucha influencia de dibujantes franceses que hacían humor
  mudo. El mejor del momento se llama Sempé.»* También nombra a **Chaval**
  (francés), **Palomo, Fontanarrosa, Rus, Mordillo** (contemporáneos que le
  gustan, no necesariamente influencias) ([Dreamers.es, entrevista a Quino](https://dreamers.es/mafalda/Entrevista/entrevista_a_quino.htm))
  ✅. Una segunda búsqueda confirma una lista más larga: **Jean-Jacques
  Sempé, Chaval, Hieronymus Bosch, Lino Palacio y Guillermo Divito** (su
  editor en la revista *Rico Tipo*, donde Divito le exigió que Mafalda no
  fuera humor mudo porque «la gente que pagaba por la revista quería
  material para leer») ✅ (dos fuentes independientes con la misma lista).
- **Esto es más fiable que la versión de Wikipedia** («mezcla de Peanuts y
  Blondie», sugerida por Miguel Brascó para una publicidad) — la wiki de
  Fandom, con la biografía de Quino, dice que la campaña publicitaria que
  dio pie a Mafalda fue para los **electrodomésticos Mansfield** (personajes
  con nombres en «M») ([Mafalda Wiki: Quino](https://mafalda.fandom.com/es/wiki/Quino))
  ✅, no para Peanuts/Blondie. **Dejo las dos versiones con su fuente**: es
  posible que se refieran a campañas distintas y una tercera fuente las
  esté mezclando. No elijo una sola como «la verdad» sin poder resolverlo.

### Comparación explícita con Peanuts (Charlie Brown), por Umberto Eco
- Umberto Eco escribió el prólogo de la primera edición italiana, *Mafalda,
  la contestataria* (1969). Cita textual: *«Charlie Brown pertenece a un
  país próspero, a una sociedad opulenta a la que busca desesperadamente
  integrarse mendigando bienestar y solidaridad. Mafalda pertenece a un
  país lleno de contrastes sociales.»* Y la más citada: *«Charlie Brown
  seguramente leyó a los 'revisionistas' de Freud y busca una armonía
  perdida; Mafalda probablemente leyó al Che [Guevara].»*
  ([reproducción del prólogo de Eco](http://mafaldaylarumia.blogspot.com/2009/03/mafalda-la-contestataria-por-umberto.html))
  ✅ (con segunda fuente que confirma autoría y año: búsqueda cruzada con
  Infobae y Las2Orillas coincide en el mismo prólogo de 1969).
- **Para la lámina/guía de estilo**: si se compara Mafalda con Peanuts, la
  diferencia central (según Eco, no invento propio) es que **Charlie
  Brown se quiere integrar; Mafalda se opone y critica**. Sirve para no
  igualar el tono de ambas series en un cruce o mención.

### Qué otras láminas del servidor se le parecen
- Repasé la lista de encargos ya confirmados (carpetas `biblias/01-…` a
  `36-…`): ninguna comparte el formato de Mafalda (**tira de prensa en
  blanco y negro, sátira política real de los años 60-70, sin fantasía**).
  Los más cercanos en tono adulto/satírico de la lista (p. ej. Rick and
  Morty) son animación para adultos, no prensa gráfica, y no se acercan al
  estilo visual. **No encontré riesgo de repetir concepto de lámina** con
  otro canal ya hecho.

---

## Punto 25 · El mundo, la historia y sus símbolos (NUEVO)

### Las reglas del mundo, en cinco líneas
1. Buenos Aires real de clase media, **1964 a 1973**, sin magia ni ficción:
   todo el humor sale de la vida diaria y las noticias reales.
2. La radio, la tele y el diario son la ventana constante al mundo: la
   Guerra Fría, la carrera espacial y la política argentina entran todo el
   tiempo en las conversaciones de una nena de 6 años.
3. Familia nuclear, casa con patio, colegio, almacén de barrio (Don
   Manolo); el auto familiar (un Citroën, ver abajo) es aspiracional, no
   de lujo.
4. Dibujo en blanco y negro puro: una viñeta = un día de diario, remate
   en la última viñeta.
5. El país vive bajo gobiernos militares buena parte de estos años: la
   censura y la política real entran en la tira, aunque el foco siga
   siendo Mafalda y sus amigos.

### La historia por etapas (con fuentes cruzadas: Wikipedia ES/EN + Fandom)
- **1963**: antología *Mundo Quino*; encargo publicitario para
  electrodomésticos **Mansfield** (personajes con nombres en «M») que no
  funcionó como anuncio pero fue la semilla de Mafalda
  ([Mafalda Wiki: Quino](https://mafalda.fandom.com/es/wiki/Quino)) ✅.
- **29-sep-1964**: debut en la revista *Primera Plana* (ya en la biblia).
- **1965-1966**: se suman **Felipe** (ene 1965), **Manolito** y
  **Susanita** (mar/jun 1965), **Miguelito** (1966) (Wikipedia ES y EN,
  coinciden) ✅.
- **15-mar-1966**: la tira pasa al diario *El Mundo*
  ([La Tercera / síntesis cruzada](https://www.latercera.com/culto/2020/09/30/una-nina-diferente-quino-y-la-historia-de-la-creacion-de-mafalda/))
  ✅.
- **29-jun-1966**: un día después del golpe de Onganía, una tira muestra a
  Mafalda preguntándose *«¿Entonces? ¿Eso que me enseñaron en la
  escuela?»* ([El Historiador, Felipe Pigna](https://elhistoriador.com.ar/mafalda-la-celebre-argentinita-que-inmortalizo-quino-por-felipe-pigna/))
  ✅.
- **dic-1967**: cierra el diario *El Mundo*; la tira pasa a la revista
  *Siete Días Ilustrados* (jun 1968) (Wikipedia EN, corrige una fecha
  confusa que traía la síntesis en español) ✅.
- **1968**: nace **Guille**, cuando a Quino «se le acababan las ideas»
  (Wikipedia EN) ✅.
- **feb-1970**: se suma **Libertad**, personaje favorito del propio Quino,
  «más auténtica que la mismísima Mafalda» ([Mafalda Wiki: Quino](https://mafalda.fandom.com/es/wiki/Quino))
  ✅.
- **25-jun-1973**: última tira, por decisión propia de Quino: cansancio,
  falta de ideas y que el personaje principal «le resultaba opresivo»
  (ya en la biblia + Mafalda Wiki) ✅.
- **1976 (dictadura)**: la viñeta de «el palito de abollar ideologías»
  (una porra policial) quedó asociada a la masacre de los curas y
  seminaristas palotinos de la parroquia San Patricio (jul-1976): apareció
  junto a los cuerpos, y los servicios de inteligencia empapelaron Buenos
  Aires con una versión alterada de la tira ([Caras y Caretas](https://carasycaretas.org.ar/2022/07/10/el-palito-de-abollar-ideologias/),
  [La Izquierda Diario](https://www.laizquierdadiario.com/Mafalda-y-el-palito-de-abollar-ideologias))
  ✅ (dos fuentes coinciden en el hecho). ⚠️ **La fecha del exilio de Quino
  en Italia varía según la fuente** (mediados de 1975 según Caras y
  Caretas, 1977 según otras notas de la misma búsqueda): no lo resolví con
  una tercera fuente firme. Dato sensible: lo dejo tal cual, sin elegir
  una fecha por mi cuenta.

### Símbolos icónicos (de la propia wiki de Mafalda, con wikitext citado)
- **«El Mundo» (el globo terráqueo)**: *«Es uno de los elementos más
  icónicos en toda la tira»*, cita textual del wikitext de la página
  propia ([Mafalda Wiki: El Mundo](https://mafalda.fandom.com/es/wiki/El_Mundo))
  ✅. Mafalda le mide la «cintura», le borra «países malos», lo acuesta
  enfermo en cama.
  ⚠️ **Aviso importante**: un artículo sobre este símbolo
  ([La Unión](https://launion.com.ar/nota/13823/2021/11/mafalda-y-el-globo-terraqueo))
  cita también *«¡¡¡Paren el mundo, que me quiero bajar!!!»* como frase de
  Mafalda — **es FALSA**, ya desmentida dentro de esta misma biblia (punto
  10, con Chequeado y la BBC: viene de un musical de Broadway, Quino lo
  desmintió en persona). Es un ejemplo real de que «más de la mitad de las
  frases de Mafalda en internet son falsas» (Divinsky, ya citado en la
  biblia): **no usar esa frase en la lámina bajo ningún concepto**, ni
  siquiera con el globo de por medio.
  La otra frase que sí aparece asociada al globo, *«¿Qué habrán hecho
  algunos sures para merecer ciertos nortes?»*, tiene menos repercusión de
  desmentido en las búsquedas, pero **sólo una fuente secundaria de
  verdad la sostiene** ⚠️: usarla con cautela, no como cita 100% segura.
- **Burocracia**: la tortuga, «primera y única mascota que se le conoce a
  Mafalda»; odia la sopa igual que ella, lo que la hace correr rápido
  «contrario a su naturaleza» ([Mafalda Wiki: Burocracia](https://mafalda.fandom.com/es/wiki/Burocracia))
  ✅.
- **Nervocalm**: marca ficticia de pastillas para los nervios que toma el
  papá de Mafalda (y una vez Felipe, por la ansiedad de los Reyes Magos);
  la wiki señala que está inspirada en un producto real argentino de
  **Garden House**, a base de valeriana, pasiflora y tilo
  ([Mafalda Wiki: Nervocalm](https://mafalda.fandom.com/es/wiki/Nervocalm))
  ✅. Sirve como objeto de utilería «del mundo» con marca propia, no
  inventada.
- **El Citroën 2CV / 3CV («la rana»)**: el auto del papá de Mafalda; en
  Argentina se lo conoció como **3CV** y de cariño **«la rana»**; empezó a
  fabricarse en el país en 1959, con 223.442 unidades hasta 1979; símbolo
  de la clase media emergente ([Perfil/Parabrisas](https://parabrisas.perfil.com/noticias/novedades/citroen-2cv-quino-mafalda-muerte-argentina-historieta-auto-padre-2-cv.phtml),
  [Fuel Car Magazine](https://fuelcarmagazine.com/noticias/recordando-a-quino-este-es-el-citroen-2cv-de-mafalda-y-su-familia/),
  [La Unión](https://launion.com.ar/nota/10790/2021/07/el-citron-del-papa-de-mafalda))
  ✅ (tres fuentes coinciden).
- **La sopa**: representa el militarismo y las imposiciones políticas,
  según explicó el propio Quino (Wikipedia EN, resumen de declaraciones
  del autor) ✅ — complementa el dato ya confirmado en la biblia (TV
  Tropes) de que la odia «como palabrota».
- **El palito de abollar ideologías**: viñeta de una porra policial,
  ligada para siempre a la masacre de San Patricio (ver historia arriba).

### Logos de grupos: no aplica
- Mafalda no tiene bandos, facciones ni organizaciones con emblema propio
  (no es una historia de aventuras): los únicos «logos» reales son de
  marcas que aparecen en la tira, como **Nervocalm** (arriba) o el diario
  **El Mundo**/la revista **Siete Días**. Lo digo aquí en una línea, como
  pide `ENCARGO.md`, en vez de inventar un logo que no existe.

### Vocabulario que un fan reconoce al instante
- **«La sopa»**, como sinónimo de algo impuesto y odiado.
- **«El Mundo»**, el globo terráqueo de Mafalda (no confundir con el
  diario homónimo del punto anterior).
- **«Burocracia»**, nombre de mascota como chiste sobre la lentitud del
  Estado.
- **Nervocalm**, remedio-broma para los nervios que le provoca Mafalda a
  los adultos.
- **El palito de abollar ideologías**, expresión que quedó en la memoria
  política argentina, más allá de la tira.

---

## Lo mejor para la lámina

1. **Mayúsculas confirmadas** (visto + OCR): rotular el globo de
   #sugerencias siempre en mayúsculas, nunca minúsculas.
2. **El globo terráqueo («El Mundo»)** es el objeto-símbolo más fuerte y
   más fácil de llevar a un objeto real en Blender (una esfera vieja,
   grande, con países dibujados a mano) — mucho más seguro que citar una
   frase de Mafalda (la mitad son falsas).
3. **Camión o cartela «SOPA» en letra de imprenta gruesa** (visto en
   Muertemafalda.jpg) como referencia real de «cartel del mundo» dentro de
   la tira, distinto del globo de diálogo.
4. **Técnica confirmada**: tinta negra pura + tramas de puntos, sin
   degradados — así de simple debe verse cualquier textura que se agregue
   en Blender o Photoshop para no romper el estilo.
5. **Netflix ya usa 3D con toon shader** (como *The Peanuts Movie*): valida
   hacer la lámina en 3D con Line Art/Freestyle sin traicionar el
   espíritu de la obra.

---

## No encontré

- El archivo real de la fuente «Quino» (Esteban Garrido-Nieto) para
  comprobar tildes/ñ/¿¡ con `fontTools`: los cuatro espejos que la
  ofrecen (1001fonts, onlinewebfonts, dafontfree, blogfonts) bloquean la
  descarga directa (login, captcha o 403) ⚠️. Búsquedas: «Quino font
  Esteban Garrido dafont licencia» (español/inglés).
- Una tercera fuente que resuelva si los cortos de 1972 fueron 72 o 230
  (NODAL dice 72, Sonrisas Argentinas dice 230) ⚠️.
- Una tercera fuente sobre el año exacto del exilio de Quino en Italia
  (1975 según una nota, 1977 según otra) ⚠️ — no pude cerrarlo, tema
  sensible y no crítico para la lámina.
- Confirmación de si «¿Qué habrán hecho algunos sures para merecer ciertos
  nortes?» es una cita real de una tira concreta (con número de tira o
  libro) o sólo una paráfrasis que circula en blogs ⚠️.
- The Cutting Room Floor sobre Mafalda: `tcrf.net` bloqueado por
  Cloudflare a `curl` (dos intentos). Es probable que no haya nada, pero
  no pude comprobarlo en la fuente misma.
- Detalles de interfaz (capturas) del App Store para Mafalda: la ficha de
  Apple para EE.UU. devolvió 404 al pedir la versión larga; me quedé con
  la descripción de la web oficial de Quino, que sí abrió.
- **Filtros de imagen (grano, brillo, aberración cromática)** de las
  adaptaciones (punto 18): ni el estudio ni la prensa especializada lo
  mencionan para ninguna de las tres versiones (1972, 1993, Netflix 2027)
  ⚠️. Búsqueda: «Mafalda Netflix imagen grano film look textura retro
  filtro visual» (español). Es un extra, no algo que exista todavía para
  documentar (la serie de Netflix ni se estrenó).

---

## Bitácora de búsqueda (esta pasada)

### Red abierta: lo que sí respondió
- `mafalda.fandom.com/es/api.php` — sí, sin problemas (páginas Quino, El
  Mundo, Burocracia, Nervocalm, `allimages`, categorías).
- `static.wikia.nocookie.net` — sí, con `Referer: https://www.fandom.com/`.
- `api.sketchfab.com` — sí (ficha completa con licencia de «Mafalda»).
- WebFetch sobre la mayoría de medios (La Nación, NODAL, Caras y Caretas,
  ENDAC, El Historiador, Cartoon Brew, ANSA Latina, Dreamers.es, La Nuez,
  Harte/Substack, blogs) — sí.
- `es.wikipedia.org` por `curl` — **límite de tasa** («too many requests»,
  varios ayudantes en la misma IP); funcionó por WebFetch en su lugar.
- `tvtropes.org` — **403** (protección anti-bot) tanto por WebFetch como
  por `curl` con user-agent de navegador. Dos intentos, no insistí más.
- `tcrf.net` — Cloudflare, «Just a moment...», no se pudo leer.
- `resistencia.org.uy` — error DNS (`EAI_AGAIN`), no se pudo cargar.
- Descarga directa de la fuente «Quino» — bloqueada en los 4 espejos
  probados (ver «No encontré»).
- `apps.apple.com/us/...` (versión larga) — 404; sí funcionó la versión
  `.../ar/app/mafalda/id585754234`.

### Búsquedas (`WebSearch`, todas en español salvo que se indique)
1. Quino técnica dibujo plumín tinta china entrevista
2. Mafalda serie 1993 animación estudio técnica Cardón Daniel Mallo
3. "Quino" font Esteban Garrido dafont licencia gratis
4. Quino Mafalda influencia Sempé "humor mudo" entrevista
5. Mafalda videojuego oficial juego de mesa "Jugando con Mafalda"
6. "Mafalda" app store iOS oficial tiras interactivas aplicación
7. halftone dot pattern brush free CC0 comic Photoshop (inglés)
8. Blender Freestyle line art comic newspaper toon shader tutorial gratis
   (inglés)
9. Mafalda Netflix Mundoloco CG animación 2D técnica Campanella
10. Mafalda Netflix imagen CGI 3D "Snoopy"/"Peanuts" comparación estilo
11. diario "El Mundo" Mafalda cierre 1967 dictadura Onganía Quino tira
12. Mafalda "palito de abollar ideologías" "In-The-pendiente" Quino tira
13. auto familia Mafalda Citroën 3CV Rastrojero tira Quino coche
14. Umberto Eco prólogo Mafalda Charlie Brown comparación "sociedad
    opulenta"
15. Mafalda frase real "sures" "nortes" globo terráqueo tira original
    Chequeado
16. Mafalda cortometrajes 1972 sonidos gibberish sin diálogos
    comprensibles Quino voces
17. Mafalda English translation Frank Wynne font typeface Quino lettering
    scanned (inglés)

### Herramientas usadas (no sólo buscador)
- `mafalda.fandom.com/es/api.php` (`action=parse&prop=wikitext`,
  `action=query&list=allimages`, `list=categorymembers`) — texto y
  tamaños reales de la propia wiki.
- `herramientas/estilo.py` sobre dos tiras reales bajadas de la wiki:
  paleta, línea y sombreado medidos (no de memoria).
- `tesseract -l spa` sobre las mismas dos tiras: confirma mayúsculas.
- `api.sketchfab.com/v3/models/...`: licencia y medidas exactas del
  modelo 3D.
- `Read` (mirar la imagen) sobre 4 imágenes reales de la wiki de Mafalda:
  Basilio.jpg, Muertemafalda.jpg, Guillesietedias.jpg, Felipemuriel.jpg.

### Coincide con lo que ya sabía la biblia (no repetido en detalle)
- Las 47 letras de Google Fonts comprobadas con fontTools, el resto de
  vestuario/hex, personajes y doblaje: no son mis puntos o ya estaban
  ✅/correctos; no los reabrí para no gastar de más.
