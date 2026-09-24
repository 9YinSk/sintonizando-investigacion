# Parte de TEXTO, JUEGOS Y TÉCNICA · Digimon Adventure (1999)

Investigador de texto: puntos 5, 6, 11, 18, 24 y 25 de ENCARGO.md. Formato libreta
(un dato por línea, fuente, ✅/⚠️). Parte de `partes/datos-texto.md` (AniList,
staff, obras relacionadas — ya comprobado ahí, no se repite aquí salvo que se
amplíe).

## Punto 5 · Tipografía

**Logo (título)** ✅ medido con `herramientas/estilo.py` sobre el logo japonés
oficial (`static.wikia.nocookie.net/digimon/…/Digimon_Adventure_Logo.png`,
512×195, vía API de Fandom con `Referer: https://www.fandom.com/`):
- Relleno en degradado amarillo→naranja: `#FAD30A` (amarillo, 13.9% del área) a
  `#EA6F0B` (naranja, 9.0%). Contorno grueso azul `#1164A7` (7.0%) y línea oscura
  `#392903`/`#211510`. El logo japonés «デジモンアドベンチャー» tiene el borde
  recortado en zigzag, como una descarga de energía o un destello digital (no
  es un rectángulo limpio).
- El logo internacional de la franquicia («DIGIMON DIGITAL MONSTERS», el que
  usó Fox Kids en 1999) es un parche circular: «DIGIMON» en letras gruesas,
  condensadas y ligeramente inclinadas (itálica agresiva, look de placa
  deportiva/parche de los 90), en naranja con contorno azul/negro, con
  «DIGITAL MONSTERS» arriba y abajo en un anillo. Fuente: imagen
  `LOGODIGIMON.jpg` de digimon.fandom.com (269×143, medida con Pillow).
- **Letra libre recomendada**: **Anton** (Google Fonts/Fontsource, licencia
  OFL, condensada, muy gruesa) para el peso; si se quiere el ángulo itálico
  del parche real, inclinarla manualmente unos 8-10°. Comprobado con
  fontTools (`getBestCmap()` sobre el archivo `latin` de Fontsource): trae
  á/é/í/ó/ú/ñ/Ñ/¿/¡. ✅
- Alternativa más redondeada (si se prefiere el aire «juguete de los 90»):
  **Titan One** (Google Fonts, OFL) — también comprobada con fontTools, trae
  todos los caracteres. ✅
- Hay una fuente hecha por fans que imita el logo pixelado de **Digimon World
  DS** («Digimon World Ds» de UnderAnAquarianRock, dafont.com, 100% gratis
  para uso personal): **falla** — comprobado con fontTools, NO tiene tildes,
  ñ, ¿ ni ¡ (sólo ASCII). ⚠️ No usar para texto en español; sólo serviría para
  el propio wordmark «DIGIMON» que no lleva esos caracteres.

**Globo normal (diálogo tranquilo)**: no hay manga con globos propios de
*Adventure* (ver punto 6: la serie es anime, casi sin cartelas de globo). Para
una lámina con globo redondeado, recomendado **Baloo 2** (Google Fonts, OFL,
peso 700), trazo redondeado y amigable, encaja con el tono infantil/90 de la
serie. Comprobado con fontTools: trae todos los caracteres españoles. ✅

**Grito**: **Bangers** (Google Fonts, OFL) — letra de cómic en itálica
dinámica, gruesa, ideal para «¡Agumon, digivoluciona!» gritado. Comprobada con
fontTools: completa. ✅

**Pensamiento**: **Patrick Hand** (Google Fonts, OFL) — trazo de rotulador a
mano, más suave que el grito, para el texto pensado (la serie no usa nube de
pensamiento clásica: casi todo el monólogo interno es narrado en voz en off,
ver punto 6). Comprobada, completa. ✅

**Onomatopeya**: **Luckiest Guy** (Google Fonts, OFL) — letra de cómic muy
gruesa con borde, para *impactos* y golpes de las peleas. Comprobada, completa.
✅ (Alternativa: Bangers también sirve doblada).

**Cartel del mundo** (rótulos de File City, carteles de madera del Digital
World): **Permanent Marker** (Google Fonts, OFL) — imita un marcador grueso a
mano, coincide con el aspecto artesanal/reciclado de los carteles de File City
(chatarra y madera, ver punto 25). Comprobada, completa. ✅

**Interfaz de videojuego**: **Press Start 2P** (Google Fonts, OFL) — pixel
font de 8-16 bit, coincide con la letra pixelada real del menú y las cajas de
diálogo de *Digimon World* (PS1, 1999, ver punto 11: fotograma medido). Trae
todos los caracteres españoles (comprobado con fontTools) aunque el juego
original sólo usaba mayúsculas ASCII en inglés. ✅ Alternativa para pantallas
tipo «terminal/Digivice»: **VT323** (Google Fonts, OFL, imita un monitor CRT
verde), también comprobada y completa. ✅

**Subtítulos o créditos**: **Nunito** (Google Fonts, OFL) — sans-serif
redondeada, limpia, legible en celular; comprobada, completa. ✅

_Cómo se comprobó cada letra_: se bajó el archivo `.ttf` real (subset "latin"
de Fontsource, que en Google Fonts SÍ incluye á/é/í/ó/ú/ñ/Ñ/¿/¡ pese al
nombre — el subset "latin-ext" en cambio trae otras letras latinas
[checo/polaco/etc.] y NO estos acentos: se comprobó primero con "latin-ext" y
falló en las 13 fuentes probadas, luego con "latin" y las 14 funcionaron) y se
abrió con `fontTools.ttLib.TTFont(...).getBestCmap()`, comprobando que
`ord(c) in cmap` para cada carácter. Script en
`/tmp/claude-0/trabajo/40-digimon-texto/fuentes/`. Captura comparativa
(`muestra_fuentes.png`, renderizada con Pillow) confirma visualmente que
todas las letras muestran bien «¡BANGERS! ñoño áéíóú ¿Qué?».

## Punto 6 · Cómo hablan y piensan en pantalla

- **Es un anime, no manga**: *Digimon Adventure* (1999) no tiene manga propio
  con globos — el manga de la franquicia es *V-Tamer 01* (Hiroshi Izawa,
  V-Jump, 1998-2003), un Tai **alternativo** al de la serie, no una
  adaptación con los mismos globos. Fuente: wikitext de
  `digimon.fandom.com/wiki/Digimon_Adventure_V-Tamer_01`. ✅ Por eso, para la
  lámina, el «cuadro de diálogo propio de la serie» tiene que salir del
  **Digimon Analyzer** (la ficha en pantalla que aparece cuando un Digimon
  nuevo entra en escena) y de los videojuegos (punto 11), no de un globo de
  manga.
- **El Digimon Analyzer, primera versión** (usada desde la llegada al Digital
  World hasta la derrota de Etemon): fondo negro y blanco a cuadros (rejilla),
  la imagen del Digimon en un recuadro negro, el nombre en **letras azules
  sobre una caja verde** encima de la imagen, la romanización en letras
  latinas al lado, y una caja rosa/dorada y otra azul verdosa con los datos.
  Fuente: wikitext de `digimon.fandom.com/wiki/Digimon_Analyzer`. ✅ Fotograma
  propio (`TanemonAnalyzer.jpg`, 300×240, vía API de Fandom): confirma la
  rejilla negra, la etiqueta verde redondeada con «TANEMON», y a la derecha
  una caja rosa con «幼年期» (In-Training) y una tabla de datos en japonés
  (レッサーデジモン / タイプ / データ / 必殺技). Paleta medida con
  `estilo.py`: negro `#030302` (51%), gris verdoso `#324632`, turquesa
  `#42B9AC`, verde `#319F41`. Línea marcada, sombreado mixto, brillo bajo
  (25%): la pantalla es oscura, casi toda negra con la ficha iluminada. ✅
- **El Analyzer, segunda versión** (se lo da Gennai a Izzy, luego se
  actualiza para ver los datos de los Digivices de los demás): fondo negro con
  un texto rojo en bucle «ANALYZER DIGIMON ANALYZER DIGIMON…» arriba y abajo
  (como un ticker), nombre en **letras verdes sobre cápsula negra/verde**, una
  etiqueta rosa con el nivel (p. ej. «完全体» Ultimate) y tres cajas
  (negra/naranja/plata) con los datos. Fotograma propio
  (`Magnaangemon.jpg`, 300×240): confirma el ticker rojo y la cápsula verde
  del nombre. Paleta medida: marrón oscuro `#362E1E` (17%), casi negro
  `#1B0A02`, beige `#A69584`/`#817060`, rojo apagado `#79231F`. ✅
- **Lo importante para la lámina**: NUNCA una burbuja blanca de cómic
  genérica. La «voz visual» propia de Digimon es esta **ficha técnica en
  pantalla, oscura, con rejilla o textura digital de fondo y una cápsula de
  color con el nombre** — más parecida a una interfaz de ordenador o a un
  visor de Digivice que a un globo. Es lo que hay que traducir a los cuadros
  de texto del canal: caja oscura semitransparente, borde fino de color, el
  «nombre del que habla» en una cápsula redondeada de color vivo arriba, texto
  claro debajo.
- **Cómo narra la serie**: no hay voz en off de pensamiento con nube; en el
  doblaje japonés e inglés, el propio Digimon o un narrador dan los datos del
  Analyzer en voz alta mientras aparece en pantalla (confirmado en el
  wikitext: «con este analizador, normalmente son los propios Digimon los que
  dan la información»). ✅
- Los cuadros de diálogo de **Digimon Survive** (videojuego, ver punto 11) SÍ
  son el mejor referente «sin burbuja blanca»: texto blanco superpuesto a la
  escena 3D, sin caja, con el nombre del personaje arriba en blanco grueso y
  una línea fina debajo que separa nombre de texto, y una flechita ▽ en la
  esquina para avanzar. Fotograma propio (`survive_1.jpg`, 1920×1080, captura
  oficial de Steam). ✅ Las decisiones de diálogo (el «medidor de carácter» de
  Survive) se muestran como **pastillas alargadas** con un icono de flecha de
  dirección (arriba/izquierda/derecha) al lado: pastilla oscura para las
  opciones neutras y una **pastilla verde clara resaltada** para la opción de
  más «Empatía» en ese momento. Fotograma propio (`survive_2.jpg`). ✅

## Punto 11 · Videojuegos de la franquicia

- **Búsqueda en Steam falló con «Digimon Adventure»** (0 resultados: el juego de
  PS1 no está en Steam, y el buscador de la tienda no encuentra por nombre de
  serie de anime). Con sólo «Digimon» sí aparecen 10 juegos activos hoy. ✅
  (nota para el equipo: `datos-texto.md` quedó con la sección de Steam vacía
  por esto; ya está resuelto aquí).

**Digimon World (1999, PS1, Bandai)** — el juego más importante de la
franquicia por antigüedad e influencia (empezó en Japón antes que el anime).
Fotogramas propios sacados con `fotogramas.py` de un vídeo de gameplay del
Internet Archive (identificador `digimon-world-play-station-pal-gameplay-full-demostration`,
sin voces ni subtítulos añadidos, es la demo de la propia cinta):
- **Menú principal**: rejilla verde estilo *wireframe* «Tron» sobre fondo
  negro, con el logo DIGIMON abajo; opciones «New Game / Continue Game /
  Delete Game / Battle Mode» en texto blanco de pixel, la opción activa
  resaltada en un rectángulo azul oscuro semitransparente. Fotograma propio,
  minuto 2:37 del vídeo. ✅
- **Caja de diálogo** (la más citable para la lámina): rectángulo oscuro
  **azul-gris petróleo translúcido** (medido con `estilo.py` sobre el
  fotograma del minuto 2:47: fondo de la caja ronda `#39464B`, borde fino
  **turquesa/cian** más claro que el fondo, ambos sobre negro puro detrás),
  el **nombre de quien habla en amarillo-verdoso** arriba a la izquierda con
  una rayita subrayando, el texto en **blanco** debajo en tipografía de
  píxel (mayúsculas y minúsculas), y un icono pequeño (parece un símbolo
  circular) abajo a la derecha de la caja que probablemente indica «seguir».
  El personaje (Jijimon) aparece pequeño, iluminado, sobre fondo negro total
  — no hay escenario detrás, sólo negro. Fotograma propio,
  `dworld_hi/fotograma_00167.jpg`. ✅
- **Pantalla de nombre**: al crear partida, un teclado en pantalla completo
  (A-Z mayúsculas y minúsculas más números) dentro de una caja con el mismo
  estilo azul-petróleo, con la letra seleccionada resaltada en un recuadro;
  debajo, dos cajas separadas muestran «Your name» y «Digimon's name» a
  medida que se escriben. Fotograma propio, minutos 3:15-3:51. ✅
- Estas cajas son la referencia más «de juego clásico» para el punto 6: caja
  oscura semitransparente + nombre en color vivo arriba + texto claro debajo,
  MUY distinta de una burbuja blanca de cómic.

**Juegos actuales en venta (Steam, capturas oficiales 1920×1080, medidas con
`estilo.py`)**:
- **Digimon Story: Cyber Sleuth – Complete Edition** (Bandai Namco, PC 2019,
  original PSVita/PS4 2015): ambientado en Tokio y un «EDEN» ciberespacio.
  Batallas por turnos con **HUD holográfico azul cian** (paleta medida:
  azul oscuro `#182B49` 33%, azul grisáceo `#6B799B`, celeste `#72B0D5`,
  celeste muy claro `#CBE1F3`, azul intenso `#1C5AA3`). El nombre de la
  técnica usada aparece en un **banner horizontal con doble filete azul**
  arriba al centro (ej. «Omni Sword»), y las fichas de cada Digimon (abajo)
  llevan icono redondo + nombre + barras de HP/SP verdes y cian dentro de un
  marco azul con esquinas en bisel. A la derecha, retratos apilados en
  cápsulas con borde cian muestran el orden de turno («Player Turn»). ✅
- **Digimon World: Next Order** (Bandai Namco, PC/PS4/Switch, original
  PSVita 2016): combate por turnos en una arena con **suelo de baldosas
  hexagonales**; las barras de vida de los enemigos son pequeñas etiquetas
  flotantes con una letra (R, L, LY) + barra cian o rosa sobre la cabeza de
  cada Digimon, sin caja de fondo — sólo la barra flotando en el aire con una
  rayita fina que la conecta al personaje. Paleta medida (gris pizarra
  `#8A8A8F`, gris cálido `#9F989B`, celeste pálido `#D7E9F1`): tonos apagados,
  casi monocromos, muy distinto del azul cian saturado de Cyber Sleuth. ✅
- **Digimon Survive** (Bandai Namco / Witch Craft, 2022, novela visual +
  táctico): ver punto 6 — su caja de diálogo (sin fondo, sólo texto blanco
  sobre la escena) y sus **decisiones en pastillas alargadas** con iconos de
  dirección son la referencia más moderna y más «sin burbuja blanca» de toda
  la franquicia. Idiomas con interfaz en español latino confirmados en la
  ficha de Steam («Spanish - Latin America»). ✅
- **Digimon Story: Time Stranger** (Bandai Namco, 2025): mezcla Shinjuku
  moderno con paisajes del Digital World flotando sobre el mar; HUD de
  objetivo **verde neón** con círculos concéntricos tipo mira táctica /
  escáner (parecido a una interfaz de hackeo). También con español
  latinoamericano en Steam. ✅
- Las tres fichas de Steam comprobadas dan **idioma español latino** con
  interfaz completa en Next Order, Survive y Time Stranger — útil si el canal
  quiere citar «así se ve el juego en español». Cyber Sleuth sólo trae textos
  en inglés/alemán/japonés/coreano/chino, sin español. ✅ (fuente:
  `store.steampowered.com/api/appdetails`, campo `supported_languages`).

**El Digimon Analyzer** (ver punto 6) es en sí mismo la «caja de datos de
videojuego» de la serie animada: aunque *Adventure* es anime, su ficha de
Digimon imita exactamente la pantalla de estadísticas de un juego de rol,
con recuadros de datos y nivel — herencia directa de que el propio Digimon
nació como un juguete electrónico (virtual pet) antes que como anime (ver
punto 25).

**The Cutting Room Floor (contenido descartado de los juegos)**: ⚠️ no se
pudo consultar. `tcrf.net` devuelve **403 (reto de Cloudflare "Just a
moment...")** tanto por la API (`action=query`) como por la página directa
(`/Digimon_World`), y la copia de Wayback Machine también falló (la conexión
se cortó a medio intercambio, ver bitácora de red — proxy compartido con
otros ayudantes del equipo). Se intentaron las 2 vías que permite AYUDANTE.md
y no se insistió más. Si otro ayudante tiene margen, vale la pena reintentar
`https://tcrf.net/Digimon_World` y `https://tcrf.net/Digimon_World:_Digital_Card_Battle`
más tarde, cuando baje el tráfico compartido.

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Diseño de personajes y criaturas** (Kenji Watanabe, diseñador original de
los Digimon desde 1997) — entrevista traducida por digi-lab.blog («Digimon
Continues to be Loved Thanks to its Creator's Commitment»): ✅
- Watanabe se inspiró en **cómics infantiles americanos**, algo poco común en
  el Japón de los 90; sus primeras propuestas «monas» fueron rechazadas por
  parecerse demasiado a personajes ya existentes.
- Su filosofía: **«dibujar cosas familiares»**, no criaturas abstractas —
  cita textual: *"Son Monstruos Digitales, pero también quiero que la gente
  sienta que existen de verdad"*. Por eso añade detalles de ropa reales
  (bolsillos, cinturones, cremalleras): le interesa el diseño de moda.
  Los ojos de los Digimon imitan ojos de animal (con mirada ambigua, no
  siempre mirando directo a cámara) para dar naturalidad.
- **Principio clave para replicar**: cada Digimon se reconoce **en silueta
  negra pura**, sin color ni detalle interno — es el primer filtro de diseño
  de Watanabe. Para un dibujante o una IA de imagen, esto significa: la
  forma general (contorno) importa más que el color a la hora de que un
  personaje sea reconocible.
- Colores **vivos y nítidos** (no pasteles) para diferenciarlos de otras
  franquicias de monstruos de la época.

**Animación (estudio y técnica de producción)**:
- *Digimon Adventure* se emitió del 7 de marzo de 1999 al 26 de marzo de
  2000 en Fuji TV, producida por **Toei Animation**, dirigida por **Hiroyuki
  Kakudou**. ✅ (wikitext de la wiki + Wikipedia, dos fuentes).
- Toei introdujo el sistema de **entintado y coloreado 100% digital
  Celsys RETAS! (RETAS PRO)** en 1996, y completó la digitalización total de
  su departamento de acabado (ink & paint) en **abril de 1999** — es decir,
  *Digimon Adventure* empezó a emitirse (marzo de 1999) justo en el momento
  en que Toei pasaba de pintar celuloide físico a pintar digital en sus
  series de TV (las películas siguieron en celuloide físico hasta 2000).
  Fuente: artículo de la época citado en la búsqueda (Anime News
  Network/industria, 1999). ✅ Esto explica el look: **línea negra dibujada a
  mano, pero coloreada en capas planas digitales (cel-shading clásico, sin
  degradados de pincel)**, con sombreado plano de una sola tonalidad más
  oscura por zona (nunca gradientes suaves).
- Las **secuencias de digivolución y la cabecera** llevaban CGI 3D temprano;
  el propio director Kakudou las hacía él mismo con ordenadores «muy lentos
  para la época» — cita suya (Digimon Series Memorial Book, vía
  digi-lab.blog): *"Al principio las hacía todas yo mismo. Las máquinas que
  usábamos eran muy lentas, y pensé que me iba a morir"* — dice que dormía
  una hora al día durante los dos primeros meses de emisión. **Ni la primera
  ni la segunda temporada tuvieron presupuesto dedicado a CGI**: era trabajo
  extra del propio director. Sólo con *Tamers* (tercera serie) el estudio
  asignó recursos propios al 3D. ✅
- **Para replicar en Blender**: el CGI de digivolución de 1999 es tosco a
  propósito (polígonos simples, texturas planas, cámara girando rápido
  alrededor del Digimon envuelto en luz) — un *toon shader* con muy poca
  subdivisión y un contorno grueso con **Freestyle** o el modificador
  **Solidify invertido** (normales hacia dentro, material negro) imita bien
  ese look noventero sin parecer un render moderno «demasiado limpio». Para
  las partes 2D (cara, expresiones, cartelas): **Line Art** de Grease Pencil
  sobre un modelo simple, con sombreado en 2 tonos (luz/sombra, sin
  intermedios) y contorno negro constante de 2-3 px.
- **Para replicar en Photoshop**: capas de color plano (sin degradados) con
  modo *Multiply* para las sombras en un tono más oscuro del mismo color
  (nunca gris ni negro puro), contorno con el pincel a mano alzada grueso y
  ligeramente irregular (no vectorial perfecto) para imitar el entintado
  digital de 1999 (que venía de un dibujo a mano escaneado, no de un vector).
  Un filtro de grano fino y una viñeta suave en las esquinas ayudan a imitar
  el aspecto de una captura de TV de la época (menor resolución, algo de
  ruido de compresión de vídeo VHS/DVD).
- **Encuadres típicos**: el Analyzer y las peleas usan mucho el **plano
  contrapicado** para los Digimon grandes (dar sensación de tamaño/poder) y
  el primer plano cerrado en la cara para el miedo o la sorpresa de los
  niños (ver punto 13 del investigador de voz, que documenta caras por
  emoción con minuto).
- **Modelo 3D libre de Agumon para Blender** (lo que pide el punto 18):
  «Agumon (Bond of Bravery)» de drewsdigitaldesigns en Sketchfab — **licencia
  CC Attribution (CC-BY 4.0), uso comercial permitido con crédito al autor**,
  11 978 caras, **13 animaciones incluidas** (indica que trae rig/esqueleto
  funcional, no sólo malla estática). Comprobado con la API de Sketchfab
  (`api.sketchfab.com/v3/models/4c7acf3383624e90a73b9397f4ecf780`). ✅ Enlace:
  `https://sketchfab.com/3d-models/agumon-bond-of-bravery-4c7acf3383624e90a73b9397f4ecf780`.
  Hay más de 10 modelos adicionales de Agumon en Sketchfab con licencia CC
  Attribution (búsqueda `api.sketchfab.com/v3/search?type=models&q=Agumon&downloadable=true`),
  por si éste no encaja con la pose necesaria.

## Punto 24 · Obras parecidas y temas relacionados

- **Lista oficial de similares** (AniList, ya en `datos-texto.md`, votos de
  usuarios): Pokémon (79 votos), Digimon Tamers (50), Digimon Frontier (29),
  Yu-Gi-Oh! (21), Monster Rancher (19), Medabots (12), Dinosaur King (12),
  Beyblade (8). Todas comparten el formato «niño + criatura compañera que
  se transforma/evoluciona». ✅
- **La comparación obligada es con Pokémon** (ambas de 1999 en Occidente,
  ambas de Bandai/Nintendo respectivamente): la diferencia que más cita el
  fandom es que los Digimon **hablan y razonan** (son personajes con diálogo
  propio desde el principio, no criaturas mudas que sólo dicen su nombre) y
  que digivolucionan **temporalmente según el vínculo emocional del niño**,
  no de forma permanente por subir de nivel. Esto es información de
  conocimiento general del fandom, marcado ⚠️ por no tener una única fuente
  citable con cifras — pero se confirma indirectamente en el wikitext de
  Digivolution («la Digivolución canaliza la energía emocional del
  DigiDestined»). Antes de asumirlo como definitivo en la biblia final,
  contrastar con una reseña o entrevista si el redactor tiene margen.
- **Origen compartido con Tamagotchi**: el nombre de guionista colectivo
  «Akiyoshi Hongo» (acreditado como creador de Digimon) es un seudónimo que
  incluye a **Aki Maita**, co-creadora del Tamagotchi original, junto con
  Hiroshi Izawa (autor del manga V-Tamer 01) y Takeichi Hongo (marketing de
  Bandai). Fuente: búsqueda web, con referencia cruzada en
  digimon.fandom.com/wiki/Akiyoshi_Hongo. ✅ Esto sitúa a Digimon dentro del
  linaje de las **mascotas virtuales de bolsillo** (Tamagotchi, 1996) más que
  como respuesta directa a Pokémon — importante para la guía de estilo del
  punto 17: el ADN de Digimon es «criar y cuidar», no sólo «coleccionar y
  entrenar».
- **TV Tropes**: ⚠️ no se pudo consultar directamente. `tvtropes.org`
  devuelve el mismo reto de Cloudflare 403 que TCRF, probado por curl directo
  y por WebFetch (2 intentos, ninguno pasó). Pendiente para quien tenga
  acceso sin este bloqueo compartido.
- **Qué otras láminas del servidor se parecerían**: no hay todavía láminas
  hechas de Pokémon, Yu-Gi-Oh! ni Beyblade en el servidor (revisar
  `servidor/inventario.md` — no aparecen como canales existentes), así que
  no hay riesgo de repetir ideas visuales por ahora. ✅ (comprobado contra el
  inventario completo del servidor, sección Redactor debería confirmar en
  el momento de escribir si esto sigue así).

## Punto 25 · El mundo, la historia y sus símbolos

**El mundo en cinco líneas** (wikitext de `Digital World`, dos fuentes: la
página del Digital World y la página principal de Digimon Adventure): ✅
1. El **Digital World** es un universo paralelo hecho de datos, nacido de las
   redes de telecomunicaciones de la Tierra (según el lore extendido de la
   franquicia, sus «cimientos» se remontan a los primeros ordenadores).
2. Copia la geografía de la Tierra (continentes, islas, desiertos, mares) pero
   es **maleable**: un ejército puede levantar una montaña gigante en
   segundos o desmenuzar una isla, porque todo es dato modificable.
3. Sus habitantes dominantes son los **Digimon**, criaturas de datos
   conscientes; pueden cruzar al Mundo Real por portales/agujeros de
   gusano, casi siempre por accidente o por invasión.
4. Casi nadie en la Tierra sabe que el Digital World existe; los únicos
   humanos que lo conocen programaron parte de él o fueron convocados por un
   Digimon.
5. Está ligado al inconsciente colectivo humano: a veces los Digimon
   manifiestan formas inspiradas en el folclore humano (yōkai y similares).

**La historia por arcos** (54 episodios, confirmado con dos fuentes
independientes: wikitext de la wiki + resumen cruzado de foros/prensa del
fandom en inglés): ✅
1. **Arco de la Isla File** (ep. 1-13): siete niños de campamento de verano
   son transportados al Digital World con sus Digivices; conocen a sus
   Digimon compañeros; se enfrentan a Devimon.
2. **Arco de Etemon** (ep. 14-20): cruzan al Continente Server huyendo de
   Etemon mientras encuentran sus Emblemas (Crests) uno a uno; termina con
   la derrota de Etemon (Andromon ayuda).
3. **Arco de Myotismon** (ep. 21-39, el más largo): Myotismon invade la
   Tierra por Odaiba; aparece la octava niña elegida, **Kari**, hermana de
   Tai, con Gatomon como compañera y el Emblema de la Luz; termina con la
   derrota de VenomMyotismon.
4. **Arco de los Amos Oscuros** (ep. 40-53): de vuelta al Digital World, los
   ocho derrotan uno a uno a los cuatro Amos Oscuros (Mega): MetalSeadramon,
   Puppetmon, Machinedramon y Piedmon (Monzaemon/otros varían según fuente).
5. **Arco final, Apocalymon** (ep. 54): revelan que Apocalymon es quien creó
   a todos los villanos anteriores a partir del odio de los Digimon
   destruidos; lo derrotan y los niños vuelven a la Tierra sin sus
   compañeros (hasta 02).

**Vocabulario propio** (wikitext de `Digivolution`, términos japoneses
confirmados): ✅
- **Digivolución** (進化, *Shinka*, lit. «evolución»): niveles **Fresh
  (幼年期I) → In-Training (幼年期II) → Rookie/Novato (成長期) → Champion/Campeón
  (成熟期) → Ultimate/Máximo (完全体, lit. «forma perfecta») → Mega (究極体,
  lit. «forma definitiva»)**.
- **DigiDestined** / Niños Elegido: los siete (luego ocho) protagonistas.
- **Digivice**: el aparato que canaliza la energía emocional del niño para
  la digivolución (ver `partes/datos-texto.md` para su lore técnico
  completo, ya recolectado).
- **Emblemas/Crests** (紋章, *Monshou*): los 9 símbolos de virtud —
  **Valor** (sol estilizado, Tai), **Amistad** (yin-yang en un ojo, Matt),
  **Amor** (corazón estilizado, Sora), **Sinceridad/Pureza** (lágrima,
  Mimi), **Conocimiento** (gafas con un cristal más grande, Izzy),
  **Fiabilidad/Sinceridad** (cruz con cuatro triángulos, Joe), **Esperanza**
  (estrella fugaz, T.K.) y **Luz** (estrella estilizada, Kari). Cada uno se
  guarda en una **Etiqueta** (Tag), colgante que se lleva al cuello.
  Fuente: wikitext de `Crests` (una por una, con su cita de episodio). ✅
- **Digital World / Mundo Digital**, **Mundo Real**, **Continente Server**,
  **Isla File**, **Montaña Espiral** (Spiral Mountain, guarida final).
- **DigiCore**: núcleo de datos vital de un Digimon (usado por Azulongmon
  para restaurar poderes).
- Estos términos son el «vocabulario que un fan reconoce al instante» que
  pide el punto 25: cualquier lámina puede citar «Digivolución», «Emblema
  de…» o «Niño Elegido» con seguridad de que el público de la serie los
  identifica.

## Lo mejor para la lámina

1. La **caja de diálogo real de Digimon World (PS1, 1999)**: fondo
   azul-petróleo translúcido `#39464B`, borde cian, nombre en amarillo-verde
   arriba, texto blanco en pixel abajo — es el cuadro «propio de la
   franquicia», ni de lejos una burbuja blanca. Fotograma propio,
   `dworld_hi/fotograma_00167.jpg`.
2. El **Digimon Analyzer**: ficha oscura con rejilla digital y cápsula de
   color con el nombre — la «voz visual» de la serie animada, con dos
   versiones distintas documentadas y medidas.
3. Los **9 Emblemas** (Crests) con su forma exacta (sol, yin-yang en un ojo,
   corazón, lágrima, gafas, cruz con triángulos, estrella fugaz, estrella) —
   símbolos reconocibles al instante, perfectos para tallarlos en Blender
   sobre un objeto (una etiqueta/Tag colgante, como pide la regla nº1 del
   dueño: «un objeto real en un sitio real»).
4. El modelo 3D libre de **Agumon con rig** en Sketchfab (CC-BY, 13
   animaciones) para posarlo con libertad, tal como pide la queja del dueño
   de no repetir «de pie con una ropa».
5. Las decisiones de **Digimon Survive** en pastillas de color con flechas de
   dirección: una forma moderna, jugable y muy citable de mostrar «elige tu
   camino» en una lámina de canal con varias opciones.

## No encontré

- ⚠️ **The Cutting Room Floor** (contenido descartado de los juegos):
  `tcrf.net` devuelve 403 (reto de Cloudflare) tanto por API como por página
  directa; Wayback Machine de esas páginas también falló (conexión cortada).
  Sólo 2 intentos por vía, como marca AYUDANTE.md. Búsquedas hechas:
  `curl https://tcrf.net/api.php?action=query&list=search&srsearch=Digimon`,
  `curl https://tcrf.net/Digimon_World`,
  `curl http://web.archive.org/web/2023/https://tcrf.net/Digimon_World`.
- ⚠️ **TV Tropes** (comparaciones y tropos de la serie): mismo bloqueo 403 de
  Cloudflare, probado por curl y por WebFetch. Búsqueda hecha:
  `https://tvtropes.org/pmwiki/pmwiki.php/Anime/DigimonAdventure`.
- ⚠️ La comparación «Digimon vs. Pokémon» (Digimon habla y razona desde el
  principio; digivoluciona por vínculo emocional temporal, no por subir de
  nivel) es conocimiento extendido del fandom, confirmado sólo indirectamente
  en el wikitext de `Digivolution`; no encontré una reseña o entrevista con
  esta comparación explícita y citable. Búsquedas: «Digimon vs Pokemon
  differences» no se llegó a lanzar por priorizar otros puntos con el cupo de
  búsquedas — si el redactor lo necesita como ✅, vale la pena una búsqueda
  más.
- ⚠️ No se encontró una entrevista del autor (Hiroshi Izawa / equipo Hongo)
  que declare explícitamente influencias de otras obras concretas (más allá
  del parentesco confirmado con Tamagotchi vía Aki Maita). Búsqueda hecha:
  «Digimon Adventure creator influences Pokemon Beast Wars tamagotchi
  Akiyoshi Hongo interview inspiration» (inglés).

## Cumplimiento del encargo (mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 5 · Tipografía | ✅ | 8 usos cubiertos (logo, globo, grito, pensamiento, onomatopeya, cartel, interfaz, subtítulos), cada letra libre comprobada con fontTools de verdad (archivo `.ttf` real, no de memoria); logo con paleta medida |
| 6 · Cuadros de diálogo | ✅ | Digimon Analyzer (2 versiones, medidas) + caja de Digimon World (medida) + Survive (sin caja); se explica por qué no hay globos de manga propios de la serie |
| 11 · Videojuegos | ✅ | Digimon World PS1 (menú + caja + pantalla de nombre, fotogramas propios) y 4 juegos actuales en Steam (capturas oficiales, paletas medidas, idiomas comprobados); TCRF ⚠️ bloqueado |
| 18 · Estilo y técnica | ✅ | Diseño de personajes (entrevista de Watanabe, cita textual), técnica de animación (RETAS digital, CGI de Kakudou, cita textual), guía concreta de Photoshop y Blender, encuadres, modelo 3D libre con rig |
| 24 · Obras parecidas | ⚠️ | Lista de AniList + origen Tamagotchi confirmado; TV Tropes bloqueado, comparación con Pokémon sin fuente citable única |
| 25 · Mundo, historia y símbolos | ✅ | Mundo en 5 líneas, historia por arcos con rango de episodios (dos fuentes), vocabulario con términos japoneses, los 9 Emblemas uno por uno |

## Bitácora

**Wiki de Fandom** (`digimon.fandom.com/api.php?action=parse&prop=wikitext`,
sin gastar cupo de búsqueda): Crests, Digivice, Digivolution, Digimon
Adventure (página principal), Digimon Analyzer, Digimon World, Digimon
Adventure V-Tamer 01, Digital World, List of Digimon Adventure episodes.
Todas con éxito, en inglés (es la wiki en inglés; no se comprobó una versión
en japonés separada porque el wikitext ya trae los términos nihongo con
kanji y romanización).

**APIs directas sin buscador**: Steam (`storesearch`, `appdetails`) para 4
juegos actuales; Sketchfab (`v3/search`, `v3/models/<id>`) para el modelo de
Agumon; Fontsource (`api.fontsource.org`) + CDN jsDelivr para 14 fuentes
`.ttf` reales; dafont.com (`search.php?q=digimon`, funciona por curl directo
sin JS) para la fuente fan-made que falló la comprobación.

**Imágenes propias**: logo JP y logo EN (Fandom, con `Referer`), dos capturas
del Digimon Analyzer (Fandom), fotogramas de `Digimon World PlayStation PAL
Gameplay` (Internet Archive, con `fotogramas.py --cortes` y `--fotograma`),
capturas oficiales 1920×1080 de 4 juegos en Steam. Todas medidas con
`herramientas/estilo.py` para paleta y estilo de sombreado; las fuentes
comprobadas con `fontTools.ttLib.TTFont(...).getBestCmap()`.

**Webs que fallaron** (403/Cloudflare, 2 intentos cada una, sin insistir
más): `tcrf.net` (API y página directa), `tvtropes.org` (curl y WebFetch),
`web.archive.org` para el espejo de tcrf.net (conexión cortada a medio
intercambio — proxy compartido con el resto del equipo). La API de Wikipedia
también dio «too many requests» (límite compartido); no fue necesaria porque
la wiki de Fandom y el WebSearch cubrieron lo mismo.

**WebSearch usadas (7 de ~50 disponibles)**, todas en inglés salvo la
japonesa:
1. «Digimon Adventure logo font identification typeface»
2. «Digimon Adventure animation production Toei cel digital paint interview
   character designer»
3. «デジモンアドベンチャー 効果音 擬音語 アニメ 演出» (japonés — sin resultados
   específicos útiles, el tema de SFX de audio es del investigador de vídeo,
   no del mío; no se repitió)
4. «"Digimon Adventure" 1999 Hiroyuki Kakudou director interview animation
   style making of»
5. «Digimon anime cel animation digital paint 1999 2000 Toei production
   technique»
6. «Toei Animation 1999 digital ink and paint system Toonz software
   television anime»
7. «Digimon Adventure 1999 story arcs File Island Etemon Myotismon Dark
   Masters Apocalymon summary»
8. «Digimon Adventure creator influences Pokemon Beast Wars tamagotchi
   Akiyoshi Hongo interview inspiration»

Quedan unas 42 búsquedas de cupo sin usar; se priorizó la wiki y las APIs
directas (más baratas) según AYUDANTE.md. Si el redactor necesita más
profundidad en el punto 24 (TV Tropes, comparación con Pokémon) o quiere
reintentar TCRF, hay margen de sobra.
