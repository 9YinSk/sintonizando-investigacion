# Texto, juegos y técnica · Intensamente (Inside Out) · puntos 5, 6, 11, 18, 24, 25

Investigador de texto. Datos comprobados a mano: los `datos-texto.md` de `recolectar.py`
buscaron mal (encontraron un manga hentai llamado «Sweet Spot» por una etiqueta
cruzada en AniList, nada que ver con la película Pixar). Se descarta esa parte y se
investiga todo de cero, en inglés, japonés y con las herramientas de la wiki y de
fuentes primarias (capturas reales de apps, wikitext de la wiki oficial, artículos
técnicos).

## 5 · Tipografía

El logo real de «Inside Out» es blanco con degradado azul, cursiva ligera y letras
gruesas y redondeadas, con «Disney·Pixar» arriba en una script fina. Se comprobó
mirando la carátula oficial del juego «Thought Bubbles» (bajada del App Store).

- Logo/título: letras gruesas, itálicas, muy redondeadas, degradado blanco→azul, con
  contorno oscuro fino · vista en la carátula oficial de `Inside Out: Thought Bubbles`
  (https://apps.apple.com/us/app/inside-out-thought-bubbles/id918780702, captura
  guardada en `/tmp/claude-0/.../scratchpad/juego/captura_1.png`, 900×1600) · ⚠️ (una
  fuente visual; nadie confirma el nombre exacto de la fuente porque Pixar la dibuja
  a mano para cada título, no es tipografía de catálogo)
- El hilo de identificación de fuentes de dafont no llega a un acuerdo: proponen
  «Cartonsix NC», «Good Girl», «Your Shirt's Inside Out!» (538 Fonts) y «Psychatronic»
  como parecidas, ninguna oficial · fuente: https://www.dafont.com/forum/read/187595/inside-out-font · ⚠️
- **Letra libre recomendada para el logo/título**: `Chewy` (Google Fonts, gratis, la
  más parecida por su trazo grueso, infantil y ondulado) o `Baloo 2` ExtraBold (más
  sobria). Comprobado con fontTools (`getBestCmap()` sobre el .ttf bajado de
  `fonts.gstatic.com`): **las dos traen á é í ó ú, Á…Ú, ñ, Ñ, ¿ y ¡ completos** ✅
- El subtítulo «THOUGHT BUBBLES» del juego va dentro de una nube de cómic blanca de
  verdad (forma de globo de pensamiento), con letras azules gruesas y contorno blanco
  · misma captura oficial de arriba ✅ (se ve igual en la miniatura de Google Play:
  https://play.google.com/store/apps/details?id=com.disney.thoughtbubbles_goo)
- Interfaz del juego «Thought Bubbles»: HUD con números y textos en un sans redondo,
  grueso, con contorno oscuro morado — muy parecido a `Baloo 2` ExtraBold o `Fredoka`
  Bold (fuentes libres) · visto en capturas oficiales de la app (App Store, capturas
  2 y 3 guardadas en el scratchpad) ✅ (dos capturas oficiales distintas del mismo
  estudio) · fontTools: `Baloo2.ttf` y `Fredoka[wdth,wght].ttf` completos en
  acentos/ñ/¿/¡ ✅
- Cartel del mundo confirmado por el guion de Inside Out 2: en la obra de
  Headquarters aparece un cartel de advertencia amarillo que dice **"Pardon our
  dust, puberty is messy"** (tipografía de cartel de obra, mayúsculas, condensada,
  como una señal de tránsito) · fuente: reseña de Popsci
  (https://www.popsci.com/health/inside-out-2-puberty/) y resumen de guion en
  themoviespoiler.com (https://themoviespoiler.com/movies/inside-out-2/) ✅ (dos
  fuentes que describen la misma escena)
  - Letra libre parecida para carteles del mundo (avisos, letreros de isla): `Oswald`
    (condensada, mayúsculas, gratis) — fontTools: completa en acentos/ñ/¿/¡ ✅
- Subtítulos/créditos: Pixar usa en los créditos finales un grotesco humanista fino
  (no hay ficha oficial pública del nombre); como letra libre parecida sirve `Work
  Sans` (limpia, muy legible en pantallas pequeñas) — fontTools: completa ✅ ⚠️ (el
  parecido es una aproximación visual, no una confirmación de Pixar)
- Globo normal (si se quiere imitar el único cómic real de la franquicia, el
  Cinestory de Joe Books): no se identificó el nombre comercial de su letra exacta
  (el libro no da créditos de tipografía, búsqueda en inglés sin resultado) ⚠️; como
  letra libre parecida a la letra de cómic clásica que usa ese tipo de adaptación
  (mayúscula limpia, algo redondeada) sirve `Comic Neue` Bold (Google Fonts) —
  fontTools: completa en acentos/ñ/¿/¡ ✅
- Grito y onomatopeya en pantalla: la película no pone onomatopeyas ni texto de
  grito como el manga (es animación 3D con actuación, no viñetas) — se anota como
  «no aplica en la obra», no «no existe». Si se necesita una letra para una lámina
  «al estilo Inside Out» con una palabra gritada o un efecto de sonido, la más
  cercana al humor visual de la serie es `Bangers` (Google Fonts, muy usada para
  cómics/rótulos enérgicos) — fontTools: completa en acentos/ñ/¿/¡ ✅. **Se marca
  como letra libre de apoyo para ambos usos, no una tipografía que aparezca en la
  obra** ⚠️
- Pensamiento (si se necesita una letra para un globo de pensamiento en la lámina):
  `Comfortaa` (redonda, ligera, look "burbuja") — fontTools: completa ✅. Igual que la
  anterior, es una sugerencia de letra libre, no algo que salga en pantalla.
- Sin fuentes en japonés/coreano/chino propias del universo de la obra: es una
  película estadounidense; en su estreno japonés el título se retituló como
  «インサイド・ヘッド» (Inside Head, no es traducción literal de Inside Out) con el logo
  latino sin adaptar a tipografía japonesa especial · fuente: ficha oficial Disney
  Japón (https://www.disney.co.jp/movie/head) y Wikipedia japonesa
  (https://ja.wikipedia.org/wiki/インサイド・ヘッド) ✅

## 6 · Cómo hablan y piensan en pantalla

Intensamente no usa globos de manga: es animación 3D con voces actuadas. Los
«pensamientos» y la información se muestran de tres formas confirmadas por la wiki
oficial y por el propio juego derivado.

- **No hay globos de diálogo en la película** (ni normales ni de pensamiento): las
  emociones hablan en voz alta todo el tiempo, incluso «pensando» · confirmado
  viendo el patrón del guion completo en la wiki
  (`https://insideout.fandom.com/wiki/Inside_Out/Transcript`, 118 548 caracteres,
  sin ninguna acotación de "burbuja" o texto en pantalla para diálogo) ✅
- El único lugar donde SÍ hay un globo real, de cómic, es la adaptación en papel
  **Inside Out Cinestory Comic** (Joe Books, 2015): toma fotogramas reales de la
  película y les pega globos de diálogo clásicos encima, escrito por Michael Arndt
  y Pete Docter · fuente: ficha en Amazon
  (https://www.amazon.com/Disneys-Inside-Cinestory-Michael-Arndt/dp/1926516877) y
  copia digitalizada en Internet Archive
  (https://archive.org/details/insideoutcinesto0000unse) ✅ (dos fuentes,
  editorial + copia del libro)
- Recuerdos = esferas de cristal de color (el color es la emoción dominante del
  recuerdo); los Recuerdos Centrales son doradas y más grandes; se guardan y
  reproducen como una proyección, no como texto · wikitext de la wiki oficial,
  página «Long Term Memory» (https://insideout.fandom.com/wiki/Long_Term_Memory) ✅
- Información del mundo interior = libros ilustrados: los **«Mind Manuals»**, una
  serie de libros en un estante detrás de la consola de Cuartel General, con un
  mapa de la Memoria a Largo Plazo dibujado dentro · wikitext
  (https://insideout.fandom.com/wiki/Mind_Manuals) ✅ (página propia + se cita en
  la página de Cuartel General)
- El juego oficial «Thought Bubbles» convierte el propio concepto de «pensamiento»
  en el objeto jugable: burbujas/globos redondos de colores que hay que reventar,
  literalmente llamadas «bubbles»; el logo del juego mete el título dentro de una
  nube-globo de pensamiento de cómic (ver punto 5) · captura oficial guardada,
  ficha en Fandom (https://insideout.fandom.com/wiki/Inside_Out:_Thought_Bubbles) ✅
- El cartel de obra «Pardon our dust, puberty is messy» (punto 5) es la cartela más
  citada del mundo de la saga fuera de la consola: funciona como un aviso real
  dentro de la cabeza de Riley, con humor de obra en construcción · mismas dos
  fuentes del punto 5 ✅
- **Para la lámina**: como la serie no tiene un cuadro de diálogo propio de cómic,
  la recomendación es imitar el lenguaje visual de sus **carteles y consola**: texto
  redondo, grueso, sobre una placa con bordes de plástico de colores (como los
  botones de Cuartel General) en vez de una burbuja blanca — así se evita el
  «globo blanco genérico» que rechazó el dueño.

## 11 · Videojuegos de la franquicia

Franquicia con pocos juegos propios y varios cameos en juegos ajenos de Disney.
Interfaz comprobada con capturas oficiales, no de memoria.

- **Inside Out: Thought Bubbles** (2015, Kongregate/Disney, iOS/Android, bubble
  shooter con más de 1000/400+ niveles): HUD con corazones = vidas, diamante = gemas
  de pago, círculos numerados = niveles del mapa con estrellas de puntuación,
  botón de pausa cuadrado celeste con icono blanco · comprobado con **tres capturas
  oficiales bajadas de la ficha de Apple** (iTunes API,
  `https://itunes.apple.com/lookup?id=918780702`), miradas con Read: mapa de niveles
  estilo tren en la Estación de los Trenes del Pensamiento, y una pantalla de juego
  con Tristeza y las burbujas cayendo ✅
- Personajes jugables del bubble shooter y su poder: Alegría (ráfaga de sol, iguala
  todas las memorias), Tristeza (nube que tiñe de azul), Furia (bola de fuego que
  abre camino), Desagrado (ola que quita un color), Temor (memoria que rebota y
  limpia todos los colores que toca) · ficha de la app en MWM
  (https://mwm.ai/apps/inside-out-thought-bubbles/918780702) y Google Play
  (https://play.google.com/store/apps/details?id=com.disney.thoughtbubbles_goo) ✅
- Escenarios del juego con nombre propio: Family Island y Dream Productions (los
  mismos lugares del mundo de la película) · mismas fuentes de arriba ✅
- **Disney Infinity 3.0 — Inside Out Play Set** (2015, consola/PC, toys-to-life):
  plataformas cooperativas a 2 jugadores, 25 niveles, tres mecánicas: nubes que se
  desvanecen, plataformas musicales a ritmo y «barreras de gravedad» que voltean el
  nivel; personajes jugables Alegría, Temor, Furia, Desagrado y Tristeza, cada uno
  con esferas de memoria de su color como power-up · fuente: reseña oficial Pixar
  Post (https://pixarpost.com/2015/05/disney-infinity-30-inside-out-play-set.html)
  y ficha de Disney Infinity Wiki
  (https://disneyinfinity.fandom.com/wiki/Inside_Out_Play_Set) ✅
- **The Cutting Room Floor** SÍ tiene ficha de «Inside Out: Thought Bubbles»
  (https://tcrf.net/Inside_Out:_Thought_Bubbles), pero el sitio devolvió 403 a
  curl/navegador sin cabecera y también falló la copia de Wayback Machine (error de
  red del contenedor, dos intentos). **No se pudo leer su contenido esta vez** ⚠️
  (queda para un repaso)
- Cameos posteriores fuera de un juego propio: **Disney Speedstorm** metió a
  Ansiedad y Hastío (Inside Out 2) como corredoras jugables en un evento de
  temporada, con Tristeza ya jugable antes lanzando una «esfera de recuerdo triste»
  que frena a los rivales · nota oficial del juego
  (https://disneyspeedstorm.com/news/disney-speedstorm-inside-out-inspired-season-8-available-now)
  ✅; **Disney Emoji Blitz** tiene emojis coleccionables de Tristeza y otras
  emociones (match-3 con iconos, no interfaz propia de la saga) · confirmado en la
  búsqueda de Google Play, sin ficha detallada propia ⚠️
- No se encontró ninguna caja de diálogo ni interfaz propia de Inside Out en
  Kingdom Hearts, Fortnite ni Dreamlight Valley: búsqueda hecha en inglés, sin
  resultado oficial (sólo mods de fans en Steam Workshop, que no cuentan como
  franquicia oficial) — se anota como «no lo encontré», no como «no existe».

## 18 · Estilo de dibujo y técnica, y cómo replicarlo

Rigs y tramas: ver puntos 3 y 19 (los trae el investigador de imagen). Aquí sólo la
técnica de render/iluminación real (con entrevistas) y cómo acercarse a ella en
Photoshop y Blender.

**Cómo lo hizo Pixar (con fuente):**
- Render de la película 1 (2015): **RenderMan PRMan/REYES** con «geometry lights»
  (tecnología nueva entonces): las emociones son fuentes de luz reales de la escena,
  no un truco de post · fuente: fxguide (https://www.fxguide.com/fxfeatured/inside-out-rendering/) ✅
- Las emociones están «hechas de energía, de miles de partículas»: un efecto de
  «hervido» (*boiling*) procedural que se genera en el momento del render, no en el
  modelado; cada una tiene un nivel de solidez distinto (Furia más sólida, Alegría y
  Temor más «emanantes») · misma fuente + blog oficial de SIGGRAPH
  (https://blog.siggraph.org/2016/02/inside-the-minds-behind-inside-out.html/) ✅
- Técnica «**glow darkening**»: como los personajes son ellos mismos la fuente de
  luz, el equipo de iluminación (Sudeep Rangaswamy) oscurece su halo según de dónde
  venga la luz clave de la escena, para que no floten como un punto blanco fijo ·
  blog SIGGRAPH ✅, y se repite mejorada en Inside Out 2 (fxguide,
  https://www.fxguide.com/fxfeatured/inside-out-2-redefining-the-magic-with-new-technology/) ✅
- Piel con **subsurface scattering con ray tracing** (para que la piel humana de
  Riley y su familia se vea real) y pelo iridiscente anisótropo reescrito con
  iluminación global · fxguide ✅
- Efectos con **Houdini** (Side Effects): Gary Bruins simuló con FEM procedural los
  zarcillos de las Islas de la Personalidad para que se movieran como plantas de
  hielo · blog SIGGRAPH ✅
- **Lenguaje de formas** del director de arte Albert Lozano: Alegría = estrella,
  Furia = cuadrado, Temor = forma nerviosa/angulosa, Desagrado = triangular y
  puntiagudo, Tristeza = gota de lágrima azul · blog SIGGRAPH ✅
- El diseñador de producción **Ralph Eggleston** pintó 500-600 gouaches/pasteles
  para el guion de color, reducidos a 200, organizados como un storyboard para
  poder rastrear cambios de color, luz y contraste de golpe. Su problema central:
  «si las emociones son luz, ¿de dónde vienen las sombras?» — John Lasseter le
  sugirió que Cuartel General funcionara como una fuente de luz dramática, como en
  el Disney clásico. Su regla de diseño: «primero el personaje, todo lo demás sale
  de ahí» · entrevista en AWN
  (https://www.awn.com/animationworld/ralph-eggleston-talks-inside-out) ✅ y en
  Cartoon Brew (https://www.cartoonbrew.com/rip/ralph-eggleston-a-cornerstone-of-pixars-visual-style-dies-at-56-220781.html) ✅
- El **mundo real** y el **mundo mental** se trataron casi como dos películas
  distintas: distinta traslucidez, sombreado y saturación para que el público note
  siempre en cuál está · misma entrevista AWN ✅
- **Encuadre y composición** (director de fotografía Patrick Lin): líneas
  horizontales = espacios abiertos (Minnesota); líneas verticales = a Riley se le
  «aprieta en compartimentos cada vez más ajustados» al mudarse a San Francisco;
  cámara fija a trípode (sólo *pans* y *tilts*) cuando Riley se apaga
  emocionalmente; cámara en mano cuando huye de casa; el plano final mezcla
  *steadicam* y grúa para unir los dos mundos · Pluralsight
  (https://www.pluralsight.com/resources/blog/software-development/camera-structure-language-within-inside) ✅
- **Inside Out 2** (2024) cambió de RenderMan REYES a **RenderMan RIS** (path
  tracing): «con REYES el 80% del trabajo era lograr que se viera bien; con RIS el
  80% ya lo hace el renderizador» (Jacob Kuenzel, shading lead). Pelo con doble
  lóbulo Chiang, sistema de partículas de piel «Hexport» simulado en Houdini,
  brillos volumétricos por capas con *field volumes* · fxguide (enlace arriba) ✅

**Cómo acercarse en Blender** (guía práctica, no un tutorial de Pixar, construida
sobre la técnica real de arriba):
- Nada de contorno tipo manga: el look de Inside Out es 3D suave, no *cel shading*
  plano. Usa `Principled BSDF` con *Subsurface* activado (radio y peso según el
  color del personaje) para la piel translúcida, y *roughness* bajo-medio para el
  acabado liso de plástico — documentado en el manual oficial de Blender
  (https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/sss.html)
  y discutido para «luz al estilo Pixar» en Blender Artists
  (https://blenderartists.org/t/lighting-like-pixar-movies/1459950).
- Para el «hervido» de energía de Alegría o Temor: anima una textura de ruido
  (Noise/Voronoi) en el input de un shader de `Emission` sobre una copia ligeramente
  más grande de la malla, y activa *Bloom* (Eevee) o el nodo *Glare* (Cycles) para
  el halo — traduce el efecto de partículas procedurales que describe fxguide.
- Para el «glow darkening»: mezcla dos versiones del shader de emisión (una más
  intensa, otra apagada) con un nodo *Layer Weight*/Fresnel según la dirección de
  la luz clave, así el personaje-luz no se ve siempre igual de brillante.
- Dos mundos, dos iluminaciones: real = luz más neutra y algo desaturada;
  mental = luces de punto saturadas del color de la emoción activa y niebla
  volumétrica, tal como separaba Eggleston sus dos guiones de color.
- Encuadre: usa elementos verticales del set (marcos, columnas) cerca de la
  cámara para «encerrar» una escena triste o ansiosa, y planos horizontales
  abiertos para una escena de Alegría; simula la cámara en mano con un modificador
  de ruido (*Noise* F-curve) en la posición/rotación de la cámara sólo en los
  momentos de caos emocional.

**Cómo acercarse en Photoshop** (para la lámina final o arte de apoyo):
- Bloquea primero la lámina en manchas de color planas a baja opacidad (un
  «guion de color» rápido, como los pasteles de Eggleston) antes de entrar en
  detalle, para fijar el contraste general.
- Glow de personaje-luz: degradado radial en modo Screen detrás del personaje
  (tintado a su color) + `Outer Glow` suave del mismo tono.
- Piel/SSS: una pasada de `Color Overlay` u `Overlay` cálido y suave en los bordes
  donde pega la luz, sin textura pintada gruesa (el acabado es liso, no pictórico).
- Carteles del mundo (ver punto 5): letras redondas y gruesas (`Baloo 2`,
  `Fredoka`) o condensadas en mayúscula (`Oswald`) sobre una placa de plástico de
  color con `Bevel & Emboss` suave — no una burbuja blanca plana.
- Grano/aberración: la película no lleva grano de cámara (es CG limpio); resérvalo
  sólo si se hace un panel «recuerdo/sueño dentro de la mente» tipo Dream
  Productions, con una leve aberración cromática y viñeta, nunca en las escenas
  normales de Cuartel General.

## 24 · Obras parecidas y temas relacionados

- **Antes de Inside Out**: *Osmosis Jones* (Warner Bros., 2001) personifica el
  interior del cuerpo (glóbulos blancos policías) en vez de las emociones; se
  compara mucho con Intensamente pero Pixar dice que no fue una referencia directa
  · comparación en The Numbers
  (https://www.the-numbers.com/movies/custom-comparisons/Osmosis-Jones/Inside-Out-(2015))
  y Wikipedia (https://en.wikipedia.org/wiki/Osmosis_Jones) ✅
- **Herman's Head** (Fox, 1991-1994): sitcom con cuatro personajes (Ángel, Animal,
  Genio, Cobarde) que viven en la cabeza de un hombre normal y discuten para
  decidir sus actos — mismo concepto que Intensamente para adultos, pero Pete
  Docter dijo que no la conocía / no fue influencia · SlashFilm
  (https://www.slashfilm.com/1989921/simpsons-stars-hank-azaria-yeardley-smith-sitcom-hermans-head-inside-out-adults/)
  y Wikipedia (https://en.wikipedia.org/wiki/Herman%27s_Head) ✅
- **Influencia confirmada por el propio Pete Docter**: la comedia de Woody Allen
  *Everything You Always Wanted to Know About Sex* (1972, el sketch del cuarto de
  control del cerebro) — la estudiaron para NO caer en lo mismo, para que las
  emociones no se sintieran «mecánicas» como esos personajes · NPR
  (https://www.npr.org/2015/06/10/413273007/its-all-in-your-head-director-pete-docter-gets-emotional-in-inside-out) ✅
- **Origen de la idea**: nació durante la producción de *Up* (Pixar), cuando
  Docter notó los cambios de humor de su propia hija preadolescente · SlashFilm
  (https://www.slashfilm.com/919442/the-idea-for-inside-out-came-from-the-production-of-pixars-up/) ✅
- **Del mismo estudio y tono** (mundos internos/abstractos con una regla de fantasía
  y un mensaje emocional para toda la familia): *Soul* (2020, el Más Allá y las
  almas), *Onward* (2020, duelo), *Elemental* (2023, elementos personificados),
  *Coco* (2017, memoria y muerte) · lista de recomendaciones de Thecinemaholic
  (https://thecinemaholic.com/movies-like-inside-out/) y Scary Mommy
  (https://www.scarymommy.com/entertainment/movies-like-inside-out) ✅
- **TV Tropes** de la obra: no se pudo leer con `navegar.py` (el navegador sin
  ventana del contenedor da «ERR_CERT_AUTHORITY_INVALID» en cualquier web ahora
  mismo, se probó también con una página neutral) ni con `curl` (403 normal en TV
  Tropes) — **no encontrado esta tanda**, no «no existe» ⚠️
- **Qué lámina del servidor se le parece**: no se leyó `servidor/inventario.md` a
  fondo (no es tarea de este rol); se avisa al redactor para que cruce el canal que
  se proponga con lo que ya hay, porque el estilo «mundo interior con reglas
  propias» puede chocar con series de fantasía ya cubiertas en el servidor.

## 25 · El mundo, la historia y sus símbolos

- **Reglas del mundo en cinco líneas**: cada persona tiene un Cuartel General en su
  mente con las emociones básicas al mando de una consola; los recuerdos son
  esferas de color que van a la Memoria a Largo Plazo por un tubo de succión; los
  recuerdos más importantes («Recuerdos Centrales», dorados) alimentan Islas de la
  Personalidad flotantes; si esas islas se apagan, la persona pierde ese pedazo de
  personalidad; en Intensamente 2 aparece además un Sistema de Creencias bajo
  Cuartel General que construye el Sentido del Yo · wikitext de
  `insideout.fandom.com` (Headquarters, Long Term Memory, Islands of Personality,
  Belief System) ✅
- **Historia por arcos**:
  1. *Inside Out* (2015): Riley (11) se muda a San Francisco; Alegría y Tristeza
     caen fuera de Cuartel General junto a los Recuerdos Centrales; cruzan la
     Memoria a Largo Plazo, la Abstracción, Producciones de Sueños y sacrifican a
     Bing Bong (amigo imaginario) en el Vertedero de la Memoria para volver;
     Tristeza toca por primera vez un Recuerdo Central y nace el recuerdo «mixto»
     (agridulce) · wikitext de la wiki (Inside Out/Transcript) ✅
  2. *Inside Out 2* (2024): Riley (13) entra en la pubertad; llegan cuatro
     emociones nuevas (Ansiedad, Envidia, Vergüenza, Hastío) durante una obra de
     renovación de Cuartel General («Pardon our dust, puberty is messy»);
     Ansiedad destierra a las emociones viejas a **La Bóveda** (donde viven otros
     personajes imaginarios de Riley, como Bloofy y Lance Slashblade) y fabrica un
     Sentido del Yo falso cruzando el **Sar-Chasm**; el clímax es un ataque de
     pánico que se resuelve aceptando que el Sentido del Yo tiene espacio para
     todas las emociones a la vez · Disney Wiki
     (https://disney.fandom.com/wiki/Inside_Out_2) y wikitext de Sar-chasm/Belief
     System en insideout.fandom.com ✅
- **Símbolos/objetos icónicos**: la consola de botones y palancas de Cuartel
  General; las esferas de recuerdo (doradas = centrales); el Tren del Pensamiento;
  los «Mind Manuals»; Bing Bong y su carrito-cohete de caramelo (símbolo de la
  imaginación infantil que se deja atrás); el cartel de obra «Pardon our dust,
  puberty is messy» de la secuela · fuentes ya citadas en los puntos 5, 6 y 18 ✅
- **Vocabulario propio que un fan reconoce**: Cuartel General (Headquarters),
  Recuerdo Central (Core Memory), Islas de la Personalidad, Memoria a Largo Plazo,
  Tren del Pensamiento, Producciones de Sueños, el Vertedero de la Memoria, Sistema
  de Creencias, Sar-Chasm, la Bóveda · mismas fuentes de wiki ✅

## Lo mejor para la lámina

- El cartel de obra «Pardon our dust, puberty is messy» es la plantilla perfecta de
  cartela del mundo: letra condensada en mayúscula sobre una placa de aviso, no una
  burbuja blanca.
- El propio logo del juego mete el título dentro de una nube-globo de pensamiento
  real: sirve de plantilla directa para un «cuadro de diálogo propio» de la serie.
- El HUD del juego (corazón=vidas, diamante=gemas, botón de pausa redondo, letras
  gruesas tipo `Baloo 2`/`Fredoka`) da un lenguaje de interfaz coherente para los
  textos del canal.
- El truco de «glow darkening» (un personaje que es su propia fuente de luz) es la
  clave para que Alegría no se vea plana en Blender o Photoshop: hay que oscurecer
  su halo según de dónde venga la luz de la escena.
- Separar «mundo real» (neutro, algo desaturado) de «mundo mental» (saturado, con
  niebla de color) al estilo del guion de color de Eggleston da automáticamente la
  profundidad que pide el dueño para que la lámina no quede plana.

## No encontré

- TCRF de *Inside Out: Thought Bubbles* (https://tcrf.net/Inside_Out:_Thought_Bubbles):
  403 con `curl` y con `WebFetch`; la copia de Wayback Machine
  (`web.archive.org/web/20251119003754/...`) falló dos veces por un error de red
  del contenedor (`ws_closed_mid_exchange`); `herramientas/navegar.py` devolvió
  `ERR_CERT_AUTHORITY_INVALID` en **cualquier** web probada, incluida
  `example.com` — no es un bloqueo de TCRF, es el navegador sin ventana del
  contenedor el que está roto hoy. Aviso para quien relance o repase.
- Nombre comercial exacto de la fuente del logo de Inside Out: Pixar no lo publica
  (se dibuja a mano para cada título); el hilo de dafont no llega a un acuerdo
  (búsqueda en inglés). ⚠️
- Capturas propias de la interfaz de Disney Infinity 3.0 — Inside Out Play Set:
  sólo se confirmó por reseña de texto (Pixar Post); no se abrieron las fotos de
  disneyinfinitycodes.com por presupuesto de tiempo. ⚠️
- Integración oficial de Inside Out en Kingdom Hearts, Fortnite o Disney Dreamlight
  Valley (búsqueda en inglés): no hay nada oficial, sólo mods de fans en Steam
  Workshop.
- Entrevistas de *making of* en japonés o coreano sobre el estilo de dibujo
  (búsqueda en japonés hecha para el título de estreno, no para el estilo): la obra
  es estadounidense y no se encontró cobertura técnica propia en esos idiomas. ⚠️
- Qué lámina ya publicada en el servidor se parece a esta propuesta: no se leyó
  `servidor/inventario.md` a fondo (lo hace el redactor); se avisa aquí para que lo
  cruce.

## Bitácora

- Se descartó `partes/datos-texto.md` de `recolectar.py`: el buscador automático
  de AniList cruzó mal el título y trajo un manga hentai sin relación («Sweet
  Spot»/«Inside-out», Comic Kairakuten). Se investigó todo de cero.
- Inglés: «Inside Out movie logo font identifont», «Inside Out Pixar headquarters
  console screen text font», «Inside Out Cinestory Comic Joe Books speech
  bubbles», «Inside Out: Thought Bubbles mobile game interface screenshots menu»,
  «Disney Infinity 3.0 Inside Out Play Set menu interface screenshots», «Pete
  Docter Ralph Eggleston Inside Out character design interview making of
  meatball», «Pete Docter Inside Out influence Everything You Always Wanted to
  Know About Sex control room brain», «Herman's Head TV series anthropomorphized
  emotions similar to Inside Out», «Inside Out 2 world Sar-Chasm Belief System
  Vault Sense of Self islands», «Ralph Eggleston Inside Out color script art
  direction interview lighting palette», «Inside Out Dream Productions scene
  aspect ratio widescreen film grain vintage look making of», «Inside Out
  cinematography camera framing per emotion analysis», «if you liked Inside Out
  recommendations similar movies personified emotions», «TV Tropes Inside Out
  Follow the Leader similar works influenced by», «Osmosis Jones compared Inside
  Out body personification», «Inside Out 2 Sadness Steam Kingdom Hearts crossover
  Fortnite Dreamlight Valley», «Inside Out 2 construction site sign Puberty
  Headquarters renovation Brain Changes scene», «Blender tutorial Pixar style
  shading subsurface scattering glow character stylized render toon Principled
  BSDF».
- Japonés: «インサイド・ヘッド 邦題 ロゴ フォント Pixar» (título y logo del estreno japonés).
- Fandom (API `api.php`, sin bloqueo): wikitext de Headquarters, Control Console,
  Mind Manuals, Islands of Personality, Long Term Memory, Train of Thought, Dream
  Productions, Belief System, Vault of Secrets, Sar-chasm, en
  `insideout.fandom.com`.
- Capturas oficiales bajadas y miradas con `Read`: 3 capturas de App Store de
  *Inside Out: Thought Bubbles* (API `itunes.apple.com/lookup?id=918780702`),
  guardadas en `/tmp/claude-0/.../scratchpad/juego/`.
- Letras: 11 fuentes libres bajadas de `fonts.gstatic.com`/GitHub de Google Fonts
  (Chewy, Baloo 2, Fredoka, Bangers, Bubblegum Sans, Sniglet, Comfortaa, Quicksand,
  Nunito, Work Sans) y comprobadas con `fontTools` (`getBestCmap()`) para á é í ó
  ú, mayúsculas, ñ, Ñ, ¿ y ¡: **todas completas**.
- Fallos de red anotados: `tcrf.net` (403), `web.archive.org` (dos intentos,
  `ws_closed_mid_exchange`), `herramientas/navegar.py` (`ERR_CERT_AUTHORITY_INVALID`
  en cualquier URL), `api.github.com` (sin acceso en esta sesión, se necesitaría
  `add_repo`).
