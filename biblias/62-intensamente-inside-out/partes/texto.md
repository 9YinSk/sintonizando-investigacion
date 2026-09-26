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
- Grito/susto en pantalla: la película no pone onomatopeyas ni texto de grito como
  el manga (es animación 3D con actuación, no viñetas); si se necesita una letra para
  una lámina «al estilo Inside Out» con una palabra gritada, la más cercana al humor
  visual de la serie es `Bangers` (Google Fonts, muy usada para cómics/rótulos
  enérgicos) — fontTools: completa en acentos/ñ/¿/¡ ✅. **Se marca como letra libre de
  apoyo, no una tipografía que aparezca en la obra** ⚠️
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
