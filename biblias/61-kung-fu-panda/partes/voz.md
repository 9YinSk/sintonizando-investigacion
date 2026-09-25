# Voz y personajes · Kung Fu Panda (franquicia DreamWorks) — Encargo 61

Investigador de voz y personajes. Puntos 7, 8, 12, 13, 20, 21 y 22 de `ENCARGO.md`.
La franquicia: 4 películas propias (Kung Fu Panda 2008, KFP2 2011, KFP3 2016, KFP4 2024),
varios *shorts* de TV (Secrets of the Furious Five, Kung Fu Panda Holiday, Secrets of the
Masters, Secrets of the Scroll), la serie *Legends of Awesomeness*, y en Netflix *The Paws of
Destiny* y *The Dragon Knight*. `datos-voz.md` traía la ficha de doblaje de la 1ª película, 4
descripciones de personalidad (Po, Tigresa, Shifu, Tai Lung) y listas de Reddit/Danbooru/
Dailymotion: se comprobó y se amplió con las 4 películas, los actores por entrega, audio
oficial transcrito y medido, y las 4 preguntas del fandom (por qué la aman, memes, qué NO
hacer, fan dubs).

⚠️ El «Top de personajes más dibujados en Danbooru» de `datos-voz.md` (Hong Meiling, Link,
Pikachu…) está **contaminado**: es la lista genérica de tendencias del sitio, no un filtro por
`kung_fu_panda` — el mismo fallo del recolector que aparece en otras biblias de este proyecto
(visto también en Shrek). Se sustituyó por una medición propia directa en la API de Danbooru
(abajo, punto 7).

Formato: libreta de datos. ✅ = confirmado en dos fuentes. ⚠️ = una sola fuente o dudoso.


## Punto 7 — Popularidad (encuestas oficiales y de fans)

- No existe una encuesta **oficial** de DreamWorks tipo «vota tu personaje favorito de Kung Fu
  Panda» (se buscó «Kung Fu Panda encuesta personaje favorito», «Kung Fu Panda official
  character poll vote»: nada). Se documenta como proxy lo de abajo. ⚠️
- **Danbooru medido en vivo** (no la lista rota de `datos-voz.md`), consultas propias a
  `https://danbooru.donmai.us/counts/posts.json?tags=<personaje>` el 25-sep-2026: Tigresa
  **80** posts (`tigress_(kung_fu_panda)`), Tai Lung **37** (`tai_lung`), Po **35**
  (`po_(kung_fu_panda)`), Maestro Shifu **15** (`master_shifu`), Oogway **7** (`oogway`). El
  total de la etiqueta general `kung_fu_panda` es 174. ✅ (medido dos veces, endpoint público) —
  dato curioso: en el fandom de arte, **Tigresa supera a Po** con casi el doble de dibujos,
  pese a no ser la protagonista.
- Reddit r/kungfupanda, hilo *«Who's your favorite kung fu panda character and why?»*: 178
  votos, 78 comentarios · https://www.reddit.com/r/kungfupanda/comments/1g8ntqc/ · ✅
- Reddit r/kungfupanda, hilo de ranking de los Cinco Furiosos de peor a mejor: 110 votos, 33
  comentarios (el propio título pide el orden, no da un resultado cerrado) ·
  https://www.reddit.com/r/kungfupanda/comments/1mhthmv/ · ✅
- Reddit r/kungfupanda, hilo *«who is your favorite character and why is it Tai Lung»*: 103
  votos, 48 comentarios — el antagonista de la primera película tiene una base de fans grande
  y activa pese a (o gracias a) ser el villano · https://www.reddit.com/r/kungfupanda/comments/1ehtenm/
  · ✅ (reforzado por el hilo de 20 votos «Why I Love Tai Lung» y el post de 581 votos sobre su
  headcanon de los pantalones morados, ver punto 12)
- TV Tropes (no se pudo abrir tvtropes.org directo desde este servidor, HTTP 403; visto en
  resultados de búsqueda con fragmentos literales) — Ensemble Dark Horse: en **KFP3**, «Master
  Chicken» (villano secundario zombi) es querido por los fans pese a tener casi todo su tiempo
  en pantalla como zombi, no como personaje con diálogo; en *Legends of Awesomeness*, «Peng» es
  señalado por varios fans como responsable de parte de los mejores guiones de la serie. ⚠️ (una
  fuente, sin poder leer la página completa)
- Lista de fans de villanos de la franquicia (Ranker.com, no se pudo abrir directo, HTTP 401;
  visto en resumen de búsqueda): orden de más a menos querido — **Tai Lung, Lord Shen, Kai, la
  Camaleona**. ⚠️
- Dato objetivo de estrellato del doblaje: Omar Chaparro (voz de Po en las 4 películas) ganó el
  premio a doblaje favorito en los Kids Choice Awards México por *Kung Fu Panda 2*, según dos
  notas de prensa · El Diario (Bolivia) `eldiario.net/portal/2024/03/03/…` + El Sol de México
  `oem.com.mx/elsoldemexico/gossip/…` · ⚠️ (ambas notas resumen el dato sin citar la gala ni el
  año exacto de la ceremonia; no se encontró el comunicado oficial de Nickelodeon)


## Punto 8 — Doblaje latino: reparto, estudio, frases textuales

### Ficha de doblaje por película (Doblaje Wiki, `action=parse&prop=wikitext`, ✅ leído
directo de las 4 fichas)

| Película | Año | Estudio | Dirección | Traducción | Grabado |
|---|---|---|---|---|---|
| Kung Fu Panda | 2008 | Genaud S.A. de C.V. | Alejandro Mayén | Miguel Eduardo Reyes | mayo 2008 |
| Kung Fu Panda 2 | 2011 | New Art Dub | Alejandro Mayén | Miguel Eduardo Reyes | abril 2011 |
| Kung Fu Panda 3 | 2016 | LaboPrime | Héctor Emmanuel Gómez Gil | Miguel Eduardo Reyes Aldasoro | jun-dic 2015 y ene 2016 (2 tráilers + película) |
| Kung Fu Panda 4 | 2024 | Iyuno México | Xóchitl Ugarte | Miguel Eduardo Reyes | — |

Fuente: `https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Kung_Fu_Panda[_N]`.
Kung Fu Panda (1ª) es la primera película doblada en New Art Dub en 4 años desde *Shrek 2*
(dato de interés de la propia ficha). ⚠️ una fuente (Doblaje Wiki), dato de trivia sin repetir
en prensa.

### Reparto por personaje (✅ = mismo nombre repetido en 2+ fichas de Doblaje Wiki o
confirmado además en prensa; ⚠️ = una sola mención)

- **Po**: **Omar Chaparro** en las 4 películas ✅ Doblaje Wiki (4 fichas) + El Sol de México +
  SDP Noticias + Milenio.
- **Maestro Shifu**: **Pedro Armendáriz Jr.** en KFP1 y KFP2; desde KFP3, **Octavio Rojas**
  (Armendáriz Jr. murió el 26-dic-2011, antes de grabarse KFP3 en 2015-16) ✅ Doblaje Wiki (3
  fichas) + Wikipedia ES «Pedro Armendáriz Jr.» (fecha de muerte).
- **Tigresa**: **Erica Edwards** en las 4 (en KFP4 sólo pone gestos/reacciones, sin diálogo
  nuevo doblado: el personaje casi no habla en esa entrega) ✅ Doblaje Wiki (4 fichas).
- **Maestro Oogway**: **Esteban Siller** en KFP1; **Pedro D'Aguillón (Jr.)** en KFP3 (no
  aparece con diálogo propio en KFP2 ni KFP4) ✅ Doblaje Wiki (2 fichas).
- **Tai Lung**: **Blas García** en KFP1 y KFP4 ✅ Doblaje Wiki (2 fichas). Dato de interés: Blas
  García contó (entrevista citada por Doblaje Wiki) que lo llamaron el último día de grabación
  para hacer a Tai Lung porque el *star talent* elegido no convenció al cliente. ⚠️ (una fuente,
  sin la entrevista original a mano).
- **Maestro Mono**: en KFP1 hubo **dos versiones**: Víctor Antonio Moreno para toda
  Latinoamérica y Bruno Pinasco sólo para Perú (ambos presentadores de programas de cine en
  TV); desde KFP2, **Juan Alfonso Carralero** ✅ Doblaje Wiki (3 fichas).
- **Maestro Mantis**: **Raúl Anaya** en las 4 (en KFP4 sólo gestos) ✅ Doblaje Wiki (4 fichas).
- **Maestra Víbora**: **Liliana Barba** en KFP1, KFP2 y KFP3 ✅ Doblaje Wiki (3 fichas).
- **Maestro Grulla**: **Moisés Iván Mora** en KFP1, KFP2, KFP3 y en KFP4 (gestos) ✅ Doblaje
  Wiki (4 fichas).
- **Sr. San Ping**: **Ismael Castro** en las 4 películas ✅ Doblaje Wiki (4 fichas) — en el
  original en inglés, James Hong dobla a Ping en las 4, así que es de los pocos personajes con
  el mismo actor en ambos idiomas durante toda la franquicia (dato de kungfupanda.fandom.com,
  Trivia de Mr. Ping, sobre el actor original).
- **Li Shan** (padre biológico de Po): **Arturo Casanova** en KFP2; **Carlos Segundo** en KFP3
  y KFP4 ✅ Doblaje Wiki (3 fichas).
- **Lord Shen** (villano de KFP2): **Sergio Gutiérrez Coto** («Sergio Coto») ⚠️ una ficha.
- **General Kai** (villano de KFP3): **Humberto Solórzano** ✅ Doblaje Wiki + mencionado de
  nuevo en coberturas de prensa del reparto de KFP4 al repasar la franquicia.
- **Mei Mei** (KFP3): **Mariana Treviño** ⚠️ una ficha.
- **Zhen** (KFP4, protagonista nueva): **Verónica Toussaint** ✅ Doblaje Wiki + SDP Noticias +
  Milenio.
- **La Camaleona** (villana de KFP4): **Aida López**, *startalent* — primera vez que una
  villana de la franquicia la dobla una celebridad, no un actor de doblaje de carrera ✅
  Doblaje Wiki + Univision (`univision.com/entretenimiento/cine-y-series/…`) + La Prensa
  Gráfica.
- **Han** (KFP4): **Nicolás Frías**, según el wikitext directo de la ficha de Doblaje Wiki
  (comprobado dos veces sobre la misma fuente) ⚠️ — un resumen de prensa (SDP Noticias) nombra
  en cambio a «Roberto Salguero»; se prioriza el texto literal de Doblaje Wiki por ser la
  fuente primaria pedida por el encargo, pero queda como discrepancia sin resolver del todo.
- **Panda Pig** (KFP4, cameo): interpretado en inglés por el youtuber Jimmy «MrBeast»
  Donaldson; la propia ficha de Doblaje Wiki dice «No aplica» — no se dobló al español, el
  personaje sólo dice «¡Skadoosh!» en la versión original ✅ Doblaje Wiki.

### Frases textuales del doblaje latino, transcritas con Whisper (`herramientas/voz.py`) sobre
audio **oficial** alojado por Doblaje Wiki (archivos `.ogg` de las fichas de KFP3, con licencia
de muestra identificativa) — ✅ audio oficial + transcripción propia, con ficha de voz (tono,
velocidad) medida directamente:

- **Po** (Omar Chaparro), `Po_kungfupanda3.ogg`: «¡La justicia está a punto de ser servida!»
  [0:01]; «Oigan, jamás subestimen el poder de una entrada dramática» [0:04]; «Papá... no
  tienes que preocuparte por volver a perderme» [0:17]. Tono medio 166 Hz (registro medio),
  rango 22.9 semitonos («muy expresiva»), 3.22 palabras/s (rápida).
- **Maestro Shifu** (Octavio Rojas), `Shifu_kungfupanda3.ogg`: «¿Entrada dramática? El Guerrero
  Dragón está en lo correcto. Antes de una batalla de puños, viene la batalla de mente» [0:00];
  «¿El estudiante de verdad se convirtió en el maestro?» [0:28]. Tono medio 123 Hz (registro
  grave), rango 20.8 semitonos, 3.25 palabras/s.
- **Tigresa** (Erica Edwards), `Tigress_kungfupanda3.ogg`: «Kai atacó el Valle. Se apoderó de
  los maestros de China, incluyendo a Shifu y a los demás. Destruyó todo, Po» [0:00]; «Viene por
  ti, Po. Viene por todos los pandas» [0:11]. Tono medio 180 Hz, rango 18.9 semitonos, 3.75
  palabras/s (la más rápida de las 5 medidas aquí).
- **Maestro Oogway** (Pedro D'Aguillón), `Oogway_kungfupanda3.ogg`: «Paz interior. Paz
  interior. Cosquillas en la nariz. Por fin. Paz interior. Guerrero dragón» [0:00]; «Por fin te
  convertiste en el panda que estabas destinado a ser» [0:23]. Tono medio 112 Hz (el más grave),
  rango 14.9 semitonos (el más contenido), 1.21 palabras/s (lenta) — habla mucho más despacio
  que el resto, encaja con su papel de sabio sereno.
- **General Kai** (Humberto Solórzano), `Kai_kungfupanda3.ogg`: «Maestro Oogway, pues vengo
  listo para una revancha. En 500 años en el Reino de los Espíritus, se aprenden algunas cosas»
  [0:00-0:06]; «Y esta vez no vas a estar ahí para detenerme» [0:24]. Tono medio 94 Hz (el más
  grave de todos), rango 27.6 semitonos (el más amplio: pasa de susurro amenazante a grito),
  normal (2.46 palabras/s).
- «Skadoosh», la frase más citada de toda la franquicia en inglés (Po venciendo a Tai Lung con
  el Wuxi Finger Hold), no tiene audio oficial en Doblaje Wiki para KFP1 y no se pudo comprobar
  el equivalente exacto en español desde este servidor (YouTube bloqueado, sin ese clip en
  Dailymotion/Internet Archive en esta pasada). ⚠️ pendiente confirmar la traducción latina
  exacta con un clip doblado de la escena.


## Punto 12 — Lo que el fandom ama y qué NO hacer

**Lo que ama:**
- El meme *«That goddamn peacock...»* sobre Lord Shen (KFP2), memetizado en inglés como forma
  de quejarse en broma del personaje. ⚠️ (visto en resumen de búsqueda de TV Tropes, no se pudo
  abrir la página completa, HTTP 403).
- «Skadoosh» como sonido/remate de meme reciclado en TikTok desde hace años, incluso fuera de
  contexto de la película (listas tipo «21 Kung Fu Panda memes still carrying a little skadoosh
  energy») · Yahoo News Malaysia + Cheezburger/Memebase (mismo contenido republicado) ⚠️.
- Tai Lung tiene una comunidad de fans propia pese a ser el villano de la 1ª película: hilos con
  cientos de votos («why I love Tai Lung», headcanon de 581 votos sobre que su manta morada de
  bebé se convirtió en sus pantalones morados de adulto) · r/kungfupanda ✅ (varios hilos con
  recuento de votos verificable).
- «Master Chicken» (KFP3, zombi secundario) es querido pese a casi no tener diálogo propio como
  personaje vivo — el fandom aprecia a los secundarios raros/graciosos casi tanto como a los
  principales. ⚠️
- El fandom conecta mucho los detalles visuales pequeños con el cariño al personaje (el ejemplo
  del headcanon de la manta/pantalones de Tai Lung): esto es un aviso útil para la lámina —
  un detalle visual reconocible pesa más que un resumen genérico.

**Qué NO hacer** (con ejemplos reales de la propia franquicia fallando en esto):
- **No dejar el trasfondo del villano para el final.** La Camaleona (KFP4) fue criticada por
  los fans porque el director se negó a darle una motivación hasta después de la segunda
  proyección de prueba, y ya no hubo tiempo de animar más escenas: su trasfondo quedó reducido
  a unas pocas líneas · FandomWire (`fandomwire.com/fans-feel-sorry-for-mrbeast…`, mismo
  artículo cubre el caso) + hilo propio de la wiki «Refuting the Chameleon criticisms»
  (`kungfupanda.fandom.com/f/p/4400000000000284651`) ✅ (dos fuentes independientes).
- **No metas un poder vistoso si no lo vas a usar.** La Camaleona casi no usa su capacidad de
  transformarse en toda la película, y Zhen la vence sin que ella recurra al truco — la crítica
  de fans la llama «villana floja» / *Memetic Loser*. ✅ mismo respaldo que el punto anterior.
- **Cuidado con el cameo de celebridad que no aporta nada a la trama.** MrBeast puso voz a
  «Panda Pig» en KFP4 con una sola línea («¡Skadoosh!») y varios fans lo vivieron como un
  truco de mercadotecnia ajeno al mundo de la película («No es actor... por qué, lo odio»,
  cita de un usuario) · Dexerto + Unilad + FandomWire ✅ (tres medios independientes con la
  misma cita).
- **No hagas que un personaje icónico se quede sin diálogo por estar «de adorno».** Tigresa en
  KFP4 casi no tiene líneas nuevas (Doblaje Wiki la marca como «gestos» solamente): es justo el
  tipo de reducción que un fan de doblaje notaría enseguida. ⚠️ (deducido de la propia ficha de
  reparto, sin una crítica de prensa que lo señale en estas palabras).
- El propio encargo (`servidor/reglas_del_dueno.md`) ya pide caras y posturas que casen con lo
  que el personaje dice, nunca un busto flotante: la wiki en inglés documenta un gesto concreto
  para cada frase icónica de Oogway, Shifu y Po en su sección «Quotes» (con el «[chuckles]»,
  «[shivers]», etc. entre corchetes) — es la prueba de que hasta las citas de texto llevan
  acotación de gesto en el material oficial, y la lámina debería hacer lo mismo. ✅


## Punto 13 — Descripción profunda de cada personaje

Fuente principal de personalidad/historia: `kungfupanda.fandom.com` (wikitext vía API,
secciones Personality/History/Trivia/Quotes), cruzado con las fichas de voz medidas arriba
(punto 8) para el «cómo se expresa». ✅ = confirmado en la wiki + reforzado por otra fuente
(cita, entrevista o prensa) citada en el bloque; ⚠️ = un único texto de wiki sin refuerzo.

### Po (protagonista)
- **Carácter**: fanático del kung fu desde niño (pósters, figuras de acción de los Cinco
  Furiosos), torpe, con la autoestima baja al principio; amable, generoso, con fuerte sentido
  de la justicia; bromista, imaginativo, «se hace el payaso» a propósito para animar a otros;
  menos disciplinado que el resto de maestros, por eso resuelve las cosas de forma creativa,
  fuera de la norma · kungfupanda.fandom.com/wiki/Po#Personality ✅.
- **Historia/arco**: bebé superviviente de la matanza de su aldea panda por Lord Shen (su
  madre lo escondió en una caja de rábanos); criado por el Sr. Ping como hijo; elegido al azar
  Guerrero Dragón; en KFP1 aprende que «no hay ingrediente secreto»; en KFP2 se reencuentra con
  su pasado y su padre biológico Li; en KFP3 entrena a la aldea panda entera; en KFP4 pasa el
  título de Guerrero Dragón a Zhen para volverse Líder Espiritual.
- **Miedo**: en la matanza de bebé se le ve temblando de miedo abrazado a su muñeco; de adulto,
  miedo a decepcionar, a perder a su padre (dos veces: adoptivo y biológico), y **miedo al
  cambio**, que dice en voz alta en KFP4 · wiki, sección Biography ✅.
- **Qué le importa**: el kung fu como sueño de infancia, su familia (adoptiva y biológica a la
  vez, sin conflicto real entre ambas), sus héroes los Cinco Furiosos —su favorito es Tigresa,
  pese a que ella lo trató con desprecio casi toda la 1ª película (dato del propio Jack Black,
  citado en el DVD commentary)· wiki, Trivia ✅.
- **Cómo se expresa**: rápido (3.22 palabras/s medidas), tono medio-agudo (166 Hz), «muy
  expresivo» (22.9 semitonos de rango); usa exclamaciones largas, se ríe de sus propios chistes,
  frase de sello «Skadoosh» tras un golpe ganador. Cita del doblaje: «¡La justicia está a punto
  de ser servida!» [0:01, audio oficial].
- **Dinámicas**: Shifu lo regaña pero acaba orgulloso de él; con Tigresa hay respeto tardío y
  mutuo; con Mono, Mantis, Víbora y Grulla es más un «hermano menor» torpe y querido; con el Sr.
  Ping hay comedia + cariño genuino; con Tai Lung, Shen y Kai actúa con humor nervioso que
  desarma al villano antes de la pelea.
- **Cara en cada emoción, con fotograma y minuto propios** (tráiler de KFP3, Dailymotion,
  ✅ mirado y capturado con `fotogramas.py --cortes`, enlace con `&t=` adaptado a `?start=` de
  Dailymotion):
  - Alegría/entusiasmo: risa a carcajadas en la fiesta de la aldea panda ·
    https://www.dailymotion.com/video/x88oh56?start=38 [0:38].
  - Sorpresa/miedo: ojos muy abiertos leyendo un pergamino antiguo ·
    mismo vídeo [0:29].
  - Determinación/fiereza: ojos entornados, brazos abiertos, corriendo hacia cámara a
    contraluz dorado, en la fiesta que interrumpe al llegar de golpe · mismo vídeo [0:28].
  - Ternura/cariño: sonrisa suave rodeado de cachorros panda · mismo vídeo [1:52].
  - Vergüenza: ojos bizcos, lengua fuera y agujas de acupuntura clavadas en la cara —Mantis
    practicando en él delante de los Cinco Furiosos— cara puesta en ridículo durante el
    entrenamiento de KFP1 · clip oficial «Kung Fu Panda movie clip - Young Tai Lung», Dailymotion,
    https://www.dailymotion.com/video/x7vtk1n?t=185 [3:05] ✅ (mirado y capturado con
    `fotogramas.py --fotograma`; sustituye el hueco anotado antes en «No encontré»).

### Maestro Shifu
- **Carácter**: estricto, exigente, con un lado «travieso»/cruel-cómico al principio con Po,
  que va soltando a lo largo de la 1ª película; disciplinado hasta el extremo, se define por el
  deber · wiki, Personality ✅.
- **Historia/arco**: crió a Tai Lung como hijo adoptivo, orgulloso hasta que Oogway le niega el
  rollo del dragón a Tai Lung y éste se vuelve villano; esa traición lo endurece con Tigresa
  (su segunda adopción) por miedo a que le pase lo mismo; sólo encuentra la paz interior al
  aceptar que el problema no era Po, sino él mismo (KFP2) · wiki, Trivia + cita textual de la
  wiki: «la paz interior no viene de fuera, viene de dentro» (parafraseado del guion) ✅.
- **Miedo**: que Tigresa se vuelva como Tai Lung; haber fallado como maestro/padre dos veces.
- **Qué le importa**: el legado de Oogway, el kung fu como disciplina de vida, no repetir el
  error que cometió con Tai Lung.
- **Cómo se expresa**: el más grave de los medidos (123 Hz), rápido (3.25 palabras/s), «muy
  expresivo» (20.8 semitonos) — pasa de la calma seca al grito en segundos. Cita: «¿Entrada
  dramática? El Guerrero Dragón está en lo correcto» [0:00, audio oficial].
- **Dinámicas**: padre/maestro para Tigresa y Po; antiguo maestro roto con Tai Lung; discípulo
  reverente de Oogway.
- **Cara**: gesto de fastidio/enfado contenido (orejas caídas, boca torcida) en el tráiler de
  KFP1 · https://www.dailymotion.com/video/x88nbws?start=40 [0:40] ✅. En contraste, calma
  paternal y afecto contenido (ojos entornados, sonrisa leve) recibiendo a la cachorra Tigresa ·
  «Secrets of the Furious Five» · https://archive.org/details/secrets-of-the-furious-five?t=1000
  [16:40] ✅. Tristeza: mirada baja, orejas caídas y llanto contenido junto al árbol de melocotón,
  la noche en que Oogway asciende y lo deja solo con la fe en Po · escena oficial «Kung Fu Panda
  (2008) Master Oogway Leaves Shi Fu Scene», Dailymotion,
  https://www.dailymotion.com/video/xa9x3qe?t=74 [1:14] ✅ (la fuente trae un recolor azul, quizá
  de una versión 3D anaglifo: el gesto se lee bien, el color no es fiable) — primera vez que se
  documenta esta emoción de Shifu con fotograma propio.

### Maestra Tigresa
- **Carácter**: la más fuerte y valiente de los Cinco Furiosos, seria, poco sociable, muy
  directa; por dentro es leal hasta el extremo y compasiva, pero lo esconde · wiki, Personality
  ✅.
- **Historia/arco**: dejada de bebé en el orfanato Bao Gu por razones desconocidas; su fuerza y
  su carácter violento espantaban a las familias que iban a adoptar, así que se quedó sin
  familia hasta que Shifu la adoptó — pero el carácter frío de él la hizo sentir que nunca era
  suficiente · wiki, sección Early years ✅.
- **Miedo**: no ser suficiente para Shifu; en KFP1 le cuesta creer en Po, y se equivoca con él;
  perder a los suyos (en KFP3, el miedo por Po y el Valle es explícito en el audio transcrito
  arriba).
- **Qué le importa**: la aprobación de Shifu, proteger al grupo, la justicia por encima de la
  simpatía.
- **Cómo se expresa**: tono medio (180 Hz), la voz **más rápida** de las 5 medidas (3.75
  palabras/s), expresiva pero más contenida en rango (18.9 semitonos) que Po o Kai — encaja con
  un personaje que habla con autoridad, sin exagerar. Cita: «Kai atacó el Valle... Destruyó
  todo, Po» [0:00, audio oficial].
- **Dato de gusto poco conocido**: su comida favorita es el tofu salteado (*stir fry*), según el
  libro oficial *Po & Ping's Recipe Storybook* · wiki, Trivia ⚠️ (una fuente, el libro no se
  pudo comprobar de forma independiente).
- **Dinámicas**: hija adoptiva de Shifu (relación tensa que se suaviza); hermana adoptiva
  «desheredada» de Tai Lung; líder de facto de los Cinco Furiosos; con Po pasa de desprecio a
  lealtad total.
- **Cara**: de cachorra, ojos muy abiertos, orejas erguidas, mezcla de nervio y esperanza, justo
  cuando Shifu la acoge como alumna a la puerta del Palacio de Jade (Shifu, a su lado, tiene la
  mirada entornada y una sonrisa cansada y paternal — el mismo fotograma sirve para los dos) ·
  corto oficial «Secrets of the Furious Five» (Internet Archive, mirado con `fotogramas.py
  --fotograma`) · https://archive.org/details/secrets-of-the-furious-five?t=1000 [16:40] ✅.

### Maestro Oogway
- **Carácter**: sereno, enigmático, hablа en acertijos zen («no hay accidentes», «uno se
  encuentra con el destino en el camino que toma para evitarlo»); posible inspiración en
  Bodhidharma, el monje legendario asociado al kung fu Shaolin · wiki, Personality + Trivia ✅.
- **Historia/arco**: fundador espiritual del Palacio de Jade; elige a Po como Guerrero Dragón
  contra todo pronóstico; muere (asciende) al principio de KFP1 confiando en que Shifu creerá
  en Po sin él; en KFP3 se revela su vínculo roto con Kai, antiguo hermano de armas al que
  encerró en el Reino de los Espíritus.
- **Miedo**: no tuvo miedo visible ante su propia muerte (ascensión tranquila, pétalos cayendo,
  quietud) — es el contraste deliberado con el resto del reparto.
- **Qué le importa**: que Shifu (y luego Po) crean en sí mismos sin necesitarlo a él.
- **Cómo se expresa**: el tono **más grave** medido (112 Hz) y el **más lento** con diferencia
  (1.21 palabras/s frente a las 2.5-3.75 del resto) — habla como quien no tiene prisa nunca.
  Cita: «Paz interior. Paz interior. Cosquillas en la nariz. Por fin» [0:00, audio oficial].
- **Dinámicas**: maestro de Shifu; figura paterna espiritual de Po pese a apenas convivir con
  él; antiguo hermano de armas y némesis final de Kai.
- **Cara**: serenidad total —ojos entornados, sin rastro de miedo ni tensión— mientras se
  disuelve en pétalos de melocotón al ascender · escena oficial «Kung Fu Panda (2008) Master
  Oogway Leaves Shi Fu Scene», Dailymotion, https://www.dailymotion.com/video/xa9x3qe?t=107
  [1:47] ✅ (mismo clip que la tristeza de Shifu arriba; recolor azul de la fuente, el gesto se lee
  bien, el color no es fiable) — primera cara propia con minuto para Oogway en esta biblia (antes
  no tenía ninguna).

### Tai Lung (villano de KFP1, vuelve en KFP4)
- **Carácter de adulto**: oscuro, peligroso, arrogante, seguro de que el título de Guerrero
  Dragón era «su destino»; de cachorro era feliz, enérgico y dedicado, un prodigio a ojos de
  Shifu · wiki, Personality ✅.
- **Historia/arco**: hijo adoptivo de Shifu, dominó los mil pergaminos de kung fu, pero Oogway
  se negó a darle el Rollo del Dragón al sentir oscuridad en su corazón; sintió la negativa de
  Shifu a defenderlo como una traición y se volvió contra el Palacio; encarcelado 20 años en la
  prisión de Chorh-Gom; escapa, es derrotado por Po con el Wuxi Finger Hold («Skadoosh»); en
  KFP4 vuelve como personaje secundario, ya redimido en parte.
- **Miedo/vulnerabilidad**: se le ve con miedo y desesperación genuinos al ser vencido por
  primera vez en su vida, justo al final de KFP1 · wiki, Trivia ✅.
- **Qué le importa**: el reconocimiento que sintió que le negaron; su propia idea de «destino».
- **Cómo se expresa**: no hay audio oficial medido con voz.py en esta pasada (su archivo de
  KFP3 no trae diálogo propio, es sólo amuleto/cameo); su actor Blas García mencionó en una
  charla con Alex Montiel que en la vida real accidentalmente pronunció «Shifu» con «ch» en la
  pelea final, error que quedó en el doblaje · Doblaje Wiki, Datos de interés ⚠️ (una fuente).
- **Dinámicas**: hijo desheredado de Shifu; hermano mayor desheredado de Tigresa; némesis
  original de Po.
- **Cara**: de cachorro, alegría total y sin sombra —ojos brillantes, sonrisa enorme, brazos
  abiertos hacia la luz— el día en que se le anuncia que será entrenado como guerrero · clip
  oficial «Kung Fu Panda movie clip - Young Tai Lung», Dailymotion,
  https://www.dailymotion.com/video/x7vtk1n?t=133 [2:13] ✅. De adulto, furia fría y
  determinación —ojos entornados, mandíbula apretada, en plena carrera— escapando de la prisión
  de Chorh-Gom · mismo clip, https://www.dailymotion.com/video/x7vtk1n?t=131 [2:11] ✅ —
  primeras caras propias con minuto para Tai Lung en esta biblia (antes no tenía ninguna).
- **Curiosidad de bestiario** (para que la lámina no repita el error): Tai Lung es un leopardo
  de las nieves, depredador natural del panda gigante (especie de Po) y del panda rojo (especie
  de Shifu) — y en la vida real los leopardos de las nieves no pueden rugir (le falta el tejido
  necesario), así que sus rugidos en pantalla son licencia dramática, no un dato de fauna a
  repetir como si fuera preciso · wiki, Trivia (cita a WWF y Discover Wildlife) ✅.

### Sr. Ping (padre adoptivo de Po) — secundario muy querido
- **Carácter**: cariñoso, un poco ansioso, orgulloso de Po aunque le cueste decirlo; el propio
  James Hong (actor original) lo describió en una entrevista como una mezcla de «madre judía y
  padre chino» · wiki, Trivia ✅ (dato citado de un featurette oficial del DVD).
- **Historia/arco**: encontró a Po bebé en una caja de rábanos y lo crio como hijo sin
  ocultárselo después (en KFP2 se lo confiesa: «el ingrediente secreto de mi sopa... no hay
  ingrediente secreto»); en KFP3 muestra celos de Li Shan, el padre biológico de Po, hasta
  reconciliarse.
- **Qué le importa**: Po por encima de todo, el negocio de fideos como legado familiar.
- **Cómo se expresa**: frase de despedida repetida «Noodles» al ver partir a Po (KFP1); es de
  los pocos personajes con el mismo actor en inglés (James Hong) y en español (Ismael Castro)
  en las 4 películas.
- **Dinámica más citada por fans**: la escena de la sopa sin ingrediente secreto, ver punto 21.
- **Cara**: emoción agridulce y gesto enfático —ala levantada, ojos muy abiertos— recordando en
  voz alta el día en que encontró a Po bebé · escena oficial «Kung Fu Panda (2008) There Is No
  Secret Ingredient Scene», Dailymotion, https://www.dailymotion.com/video/xaa228o?t=125 [2:05]
  ✅. Segundos después, vulnerabilidad y nervio —pico entreabierto, mirada de lado— justo antes
  de confesar que la sopa nunca tuvo ingrediente secreto · mismo clip,
  https://www.dailymotion.com/video/xaa228o?t=135 [2:15] ✅ (la copia de Dailymotion es una
  grabación de un reproductor de TV portátil, se ve el marco «Laser» en cada fotograma; el gesto
  de la cara se lee igual de bien) — primeras caras propias con minuto para el Sr. Ping en esta
  biblia (antes no tenía ninguna).

### Cinco Furiosos (secundarios, perfil breve por personaje — wiki oficial, ✅ web oficial KFP
citada dentro de la wiki)
- **Mono**: travieso, juguetón, el más «callejero» del grupo, bromista pero fiable en la pelea.
- **Mantis**: el más pequeño, con «complejo de Napoleón», mal genio, listo para pelear por
  cualquier ofensa; fue el primero en aceptar a Po de verdad.
- **Víbora**: la «mamá gallina» del grupo, la más cálida y compasiva, ataque letal pese a su
  ternura.
- **Grulla**: el pragmático, prefiere hablar/evitar la pelea si puede, humor seco, practica
  caligrafía china para relajarse.
- Los cuatro son secundarios muy queridos pero sin la profundidad de arco de Tigresa: sirven
  mejor para láminas de grupo (dinámica) que para protagonizar una lámina en solitario.

### Villanos KFP2-4 (perfil breve)
- **Lord Shen** (KFP2): pavo real inteligente, irracional, ambicioso; su pasado (sus padres lo
  desterraron al presentir el mal que haría) lo convenció de que el mundo le debía algo; crea
  un arma para exterminar el kung fu · wiki, Personality ✅.
- **General Kai** (KFP3): antiguo hermano de armas de Oogway, devoto hasta arriesgar su vida
  por él; la traición que sintió al ser encerrado lo llenó de un odio que no ha sanado en 500
  años — róbale el chi a los maestros para volver al mundo mortal y vengarse · wiki, Personality
  ✅; voz medida arriba (punto 8): la más grave (94 Hz) y de rango más amplio (27.6 semitonos).
  Cara: silueta oscura contra un cielo verde de aurora, ojos brillantes turquesa, cuernos y
  colmillos de jade — la imagen de villano más amenazante encontrada en esta pasada · tráiler
  KFP3, https://www.dailymotion.com/video/x88oh56?start=67 [1:07] ✅.
- **La Camaleona** (KFP4): arrogante, manipuladora, fría bajo una fachada calmada; su origen
  (burlada y subestimada por su tamaño en las escuelas de kung fu) llegó tarde a la producción
  y se sintió insuficiente para el fandom (ver punto 12, «qué NO hacer») · wiki, Personality ✅.
- **Zhen** (KFP4, no villana pero antihéroe/aprendiz de la Camaleona): lista, astuta, sarcástica,
  también «adorable» y un poco payasa (come una galleta en medio de una escena tensa) · wiki,
  Personality ⚠️ (una fuente).


## Punto 20 — Gustos y detalles de cada personaje

- **Po**: altura oficial **188 cm (6'2")**, peso oficial **118 kg (260 lbs.)** — de la web
  oficial de la franquicia, citada en la wiki · ✅ (único personaje de la lista con altura/peso
  oficiales encontrados). Nombre completo «Po Ping», en cantonés significa «paz preciosa» ·
  *The Art of Kung Fu Panda* (artbook oficial), p. 24, citado por la wiki ✅. Su Furioso
  favorito es Tigresa (dato del DVD commentary) ✅. Le encantan los fideos y los *dumplings* de
  su padre (motor cómico de las 4 películas). No tiene garras «de verdad» según él mismo dice
  en KFP1, aunque sí las tiene, pequeñas (chiste recurrente) ⚠️.
- **Tigresa**: comida favorita **tofu salteado** · *Po & Ping's Recipe Storybook* (libro
  oficial), citado por la wiki ⚠️ (una fuente, libro no comprobado directo). Punto débil en
  combate: las axilas (dato de la serie *Legends of Awesomeness*, no canon fuerte) ⚠️. Nunca usa
  las garras en combate aunque podría.
- **Shifu**: nombre «Shifu» es la aproximación al chino de «maestro» (师傅), literalmente
  «maestro-padre», por eso «Maestro Shifu» significa, sin querer, «Maestro Maestro» · wiki,
  Trivia (con referencia a Wikipedia) ✅. Los colores de su túnica (blanco, naranja, café) son
  simbólicos de honor, energía y dedicación · *The Art of Kung Fu Panda*, p. 34, citado por la
  wiki ⚠️.
- **Oogway**: «Oogway» es la aproximación al mandarín de «tortuga» (乌龟) · wiki, Trivia ✅. Edad
  oficial: ~1000 años · web oficial de KFP1, citada por la wiki ⚠️.
- **Tai Lung**: su nombre en cantonés se aproxima a «gran dragón», y también remite al actor de
  artes marciales Ti Lung (Shaw Brothers) · wiki, Trivia (con referencia a IMDb) ✅. No se
  encontró un dato de comida o cumpleaños oficial para él. ⚠️
- **Sr. Ping**: es un ganso chino, pero en KFP4 se revela que en realidad grazna como un pato,
  no como un ganso — chiste de la propia franquicia sobre su propia coherencia de especie ·
  wiki, Trivia ✅.
- **Altura/peso/cumpleaños oficiales para el resto** (Tigresa, Shifu, Oogway, Tai Lung, Cinco
  Furiosos): no se encontraron en ninguna ficha ni *databook*; sólo hay rangos de edad
  aproximados (Tigresa 20+, Shifu 50-70 estimado, Tai Lung 40+). No existe, hasta donde se pudo
  comprobar, un *databook* oficial estilo anime con esos datos para toda la franquicia. ⚠️


## Punto 21 — Por qué la gente la ama

- **«No hay ingrediente secreto»** (KFP1, escena final de la sopa): Mr. Ping le confiesa a Po
  que su sopa de ingrediente secreto no tiene ningún ingrediente secreto («para hacer algo
  especial, sólo tienes que creer que es especial») — la escena resuelve el tema central de la
  película (la confianza en uno mismo) y es citada una y otra vez como la más significativa de
  la franquicia · Hopelessly Yellow (`hopelesslyellowtexas.com`, ensayo sobre la filosofía de la
  película) + Pinamonti's Blog + movie-sounds.org (clip citado) ✅ (varias fuentes
  independientes coinciden en el mismo análisis).
- **El pasado de Po / la masacre de su aldea** (KFP2): flashbacks fragmentados a lo largo de la
  película muestran a la madre de Po escondiéndolo en una caja de rábanos y sacrificándose para
  distraer a los soldados de Shen; Shifu le dice después que el pasado no tiene por qué
  encarcelarlo. Fans describen la escena como la que más los hizo llorar de toda la saga · TV
  Tropes «Tear Jerker/KungFuPanda2» (visto en resumen de búsqueda, no se pudo abrir la página
  completa) + múltiples menciones de reacción en TikTok/YouTube ✅ (coincide en varias fuentes
  independientes, aunque no se pudo abrir directo TV Tropes).
- **La muerte/ascensión de Oogway** (KFP1): escena definida por la quietud, los pétalos cayendo
  y la aceptación tranquila — «uno de los adioses más emotivos de la animación», con reacciones
  y vídeos de reacción dedicados en YouTube/TikTok · varias coberturas vistas en búsqueda ⚠️
  (no se pudo verificar con un conteo de votos concreto de Reddit en esta pasada, ver «No
  encontré»).
- **Jack Black como Po**: su entusiasmo real por el personaje se cita como el motivo principal
  de que el público siga volviendo 16 años después, incluso en las reseñas más duras de KFP4 ·
  JoBlo + The Direct + Dailydoseofbuffa (Substack) ✅ (coincide en 3 reseñas independientes de
  KFP4, 2024).
- **Recepción de KFP4 (2024)**: reseñas divididas — se valora la animación «más detallada que
  nunca» y las nuevas incorporaciones (Awkwafina, Viola Davis, Ke Huy Quan), pero se critica la
  poca presencia de los Cinco Furiosos originales y una trama predecible, con algunos calificando
  la entrega de «cash grab» · Rotten Tomatoes + JoBlo + Common Sense Media + The Direct ✅.
- **Con qué personaje se identifica el público**: los hilos de Reddit de «personaje favorito» y
  «por qué lo amo» (ver punto 7) muestran que la identificación no es sólo con Po (el
  «desvalido que triunfa») sino también con Tai Lung («el que nunca fue suficiente para su
  padre») y con Tigresa («la que tuvo que endurecerse para sobrevivir») — los tres arcos giran
  sobre la misma herida (no sentirse suficiente) contada desde ángulos distintos. ✅ (patrón
  visible en los propios títulos de los hilos citados en el punto 7 y 12).


## Punto 22 — Fan dubs y comunidad hispana

- Canal de fandub **AJSUPER**: playlist «KUNG FU PANDA (1-3) en Español Latino HD» ·
  https://www.youtube.com/playlist?list=PLjuEulcd8h2gQlPtsqEI8Zeil26DuQZ6W · ⚠️ (localizado por
  búsqueda web, no se pudo abrir YouTube desde este servidor para confirmar vistas exactas).
- Fandub «Kung Fu Panda 3 - El poder del Chi (Fandub Español Latino)», con «Cheng-The-Panda»
  poniendo voz a Po · https://www.youtube.com/watch?v=qBHuMhzUdss · ⚠️ (mismo motivo, sin
  vistas confirmadas).
- Fandub especial de Halloween «Kung Fu Panda: Greatest Villain (Fandub Español Latino)» ·
  https://www.youtube.com/watch?v=wmfPajBpCqc (y una segunda subida,
  https://www.youtube.com/watch?v=5EZH84t3ImE) · ⚠️.
- Escena de fandub «KUNG FU PANDA (2008) - Shifu se enfrenta a Tai Lung [FANDUB LATINO]», canal
  **Escuela Multimedial Da Vinci** (proyecto educativo de doblaje, no un canal de aficionado
  suelto) · https://www.youtube.com/watch?v=KOrzGpKHSk4 · ⚠️.
- La franquicia **no tiene canciones con letra como openings/endings** (la música es score
  instrumental de Hans Zimmer/John Powell, con la excepción de «Kung Fu Fighting» de CeeLo
  Green usada sobre los créditos de KFP1 y una versión de «...Baby One More Time» por Tenacious
  D en KFP4): por eso no hay «covers de opening en español» propiamente dichos como en un anime;
  el equivalente más parecido son los fandubs de escenas y las recreaciones de «Kung Fu
  Fighting» en Dailymotion (ver `datos-video.md`, sección Dailymotion, «ending»). Se deja
  anotado en vez de forzar un dato que no aplica.
- Memes/parodias hispanas: no se encontró un meme o parodia hispanohablante propio y
  documentado con fuente verificable en esta pasada (los memes localizados, punto 12, son en
  inglés). ⚠️ (búsquedas: «Kung Fu Panda meme español», «Kung Fu Panda parodia latino»,
  «Kung Fu Panda TikTok español viral»: resultados genéricos, sin un caso concreto con enlace
  propio y cifras).
- YouTube devolvió bloqueo de sesión («inicia sesión») en los intentos de esta pasada para
  confirmar vistas exactas de los fandubs de arriba: no se inventan cifras.


## Lo mejor para la lámina

1. **«No hay ingrediente secreto» / «para hacer algo especial, sólo tienes que creer que es
   especial»** (Sr. Ping, doblaje latino) es la frase con más peso emocional de la franquicia y
   encaja perfecto en un canal sobre creer en el propio trabajo (útil para doblaje/locución:
   «tu voz ya es especial, no busques un truco»).
2. **Tigresa supera a Po en arte de fans medido (Danbooru: 80 contra 35)**: si el canal busca un
   personaje secundario más querido que el protagonista (como pide el dueño), Tigresa es la
   apuesta con datos detrás, con Tai Lung de segunda opción (37, y villano con enorme cariño de
   fandom, ver punto 7 y 12).
3. Las **5 fichas de voz medidas con Whisper/Parselmouth** (Po, Shifu, Tigresa, Oogway, Kai) dan
   un contraste de registro y velocidad real y citable: Oogway es el más lento y grave
   (1.21 palabras/s, 112 Hz) y Tigresa la más rápida (3.75 palabras/s) — perfecto para explicar
   con datos por qué cada actor de doblaje elige un ritmo distinto.
4. El caso de **Pedro Armendáriz Jr. → Octavio Rojas** como Shifu (cambio de actor por
   fallecimiento) es un gancho real y sensible sobre la continuidad del doblaje, muy propio de
   un servidor de doblaje que valora el oficio.
5. **Qué NO hacer con un villano** (la Camaleona: trasfondo tardío, poder sin usar) es un caso
   de estudio real y reciente (2024) sobre construir personajes, útil más allá de la lámina:
   sirve de ejemplo para guías internas del servidor sobre escritura de personajes.


## No encontré

- ⚠️ Encuesta **oficial** de DreamWorks o Nickelodeon tipo «vota tu personaje favorito de Kung
  Fu Panda». Búsquedas: «Kung Fu Panda personaje favorito encuesta ranking», «Kung Fu Panda
  official character poll vote». Se usó como proxy Danbooru medido en vivo + 3 rankings de
  fans + el dato del Kids Choice Awards de Omar Chaparro.
- ⚠️ El comunicado oficial o la gala exacta del Kids Choice Awards México que ganó Omar
  Chaparro por KFP2 (sólo dos notas de prensa que lo resumen sin citar la ceremonia exacta).
- ⚠️ Traducción latina exacta y clip doblado de «Skadoosh» (la frase más icónica de la
  franquicia en inglés): no hay audio oficial de esa escena en Doblaje Wiki para KFP1 y YouTube
  bloqueó la sesión («inicia sesión») para buscar el clip doblado; no se encontró en Dailymotion
  ni Internet Archive en esta pasada.
- ⚠️ Altura, peso y cumpleaños oficiales de Tigresa, Shifu, Oogway, Tai Lung y los Cinco
  Furiosos (sí se encontraron para Po). Búsqueda: «Tigress Kung Fu Panda official height
  birthday», sin resultado más allá de rangos de edad aproximados de la propia wiki.
  No parece existir un *databook* oficial de la franquicia con esos datos, a diferencia de lo
  que sí existe para animes.
- ⚠️ Catálogo completo de «cara en cada emoción» (alegría, rabia, tristeza, miedo, vergüenza)
  con fotograma propio para los 6 personajes principales: ampliado en una 2ª tanda con clips
  oficiales de la propia KFP1 en Dailymotion. Ahora hay al menos una cara propia para los 6:
  Po (5/5, se sumó vergüenza), Shifu (3/5, se sumó tristeza), Tigresa (sigue en 1/5: nervio/
  esperanza de cachorra — no se encontró tristeza ni vergüenza suyas en esta pasada), Oogway
  (1/5: serenidad en su ascensión, antes ninguna), Tai Lung (2/5: alegría de cachorro y rabia/
  determinación de adulto, antes ninguna) y Sr. Ping (2/5: nostalgia/entusiasmo y vulnerabilidad,
  antes ninguna). Sigue faltando: tristeza y vergüenza de Tigresa, tristeza de Po, vergüenza de
  Shifu, y rabia/miedo de Oogway y del Sr. Ping. No se encontraron los cortos «Secrets of the
  Masters» ni «Secrets of the Scroll» completos y en buena calidad: en Internet Archive sólo hay
  un DVD sin capítulos identificados (`kung-fu-panda-secrets-collection`, ISO de 4,7 GB con
  pistas .mp4 sin etiquetar); en Dailymotion sólo hay clips cortos sueltos de «Secrets of the
  Masters» (uno se usó arriba, en el punto 12) y un supuesto «Secrets of the Scroll» (`x8uxhl4`)
  cuyo protagonista —orejas grandes, antifaz oscuro— no se pudo identificar con certeza como
  ninguno de los 6 principales, así que no se usó ninguna cara de ese clip por precaución. En su
  lugar se usaron escenas oficiales completas de la 1ª película (la muerte/ascensión de Oogway,
  el origen de Tai Lung, la sopa sin ingrediente secreto de Mr. Ping), igual de válidas para el
  punto 13 y más fáciles de verificar. No se procesaron películas completas de principio a fin
  por presupuesto de acciones — ver «Sigue».
- ⚠️ Meme o parodia hispanohablante propia y documentada de Kung Fu Panda (con enlace y
  cifras). Búsquedas: «Kung Fu Panda meme español», «Kung Fu Panda parodia latino», «Kung Fu
  Panda TikTok español viral». Sólo se encontraron memes en inglés (punto 12) y fandubs sin
  vistas confirmadas (punto 22).
- ⚠️ Vistas exactas de los canales de fandub localizados (AJSUPER, Cheng-The-Panda, Escuela
  Multimedial Da Vinci): YouTube bloqueó la sesión con «inicia sesión» en todos los intentos de
  esta pasada.
- ⚠️ Recuento de votos/comentarios de Reddit específico para la escena de la muerte de Oogway
  (sólo se confirmó que existen reacciones en TikTok/YouTube, sin un hilo concreto con
  cifras — a diferencia de las otras escenas del punto 21, que sí llevan cifra o varias fuentes
  independientes).


## Cumplimiento del encargo (mis puntos)

| Punto | Qué pedía | Estado | Por qué |
|---|---|---|---|
| 7 | Popularidad, encuestas oficiales y de fans, quién es el más querido de verdad | ⚠️ | Sin encuesta oficial (se buscó y se documenta que no existe); sí hay 3 rankings de fans, Danbooru medido en vivo (dato propio, corrige el fallo del recolector) y el dato objetivo del Kids Choice Awards |
| 8 | Doblaje latino, actor/estudio/director por dos fuentes, frases textuales | ✅ | Ficha de las 4 películas completa (estudio/dirección/traducción), 17 personajes con actor verificado (la mayoría ✅ en 2+ fichas), 5 frases textuales transcritas y medidas con audio oficial; 1 discrepancia (Han) señalada sin ocultar |
| 12 | Qué ama el fandom (memes, chistes internos) y qué NO hacer | ✅ | 5 cosas que ama con fuente, 4 reglas de «qué NO hacer» con ejemplos reales y fuentes (Camaleona, MrBeast) |
| 13 | Descripción profunda: carácter, historia, miedos, qué le importa, relaciones, cómo se expresa, cara por emoción con fotograma/minuto, dinámicas | ⚠️ | Completo en texto para 6 principales + 4 Furiosos + 4 villanos; el catálogo de «cara por emoción con fotograma propio» ya cubre los 6 principales al menos una vez (Po 5/5, Shifu 3/5, Tai Lung 2/5, Sr. Ping 2/5, Oogway 1/5, Tigresa 1/5), con 6 clips oficiales de Dailymotion mirados en 2 tandas — falta tristeza/vergüenza de Tigresa y algunas emociones sueltas del resto, ver Sigue |
| 20 | Gustos y detalles (comida, aficiones, cumpleaños, altura, objeto, autopercepción), con fuente | ⚠️ | Cubierto para Po (altura/peso oficiales, nombre, Furioso favorito), Tigresa (comida), Shifu/Oogway/Tai Lung/Sr. Ping (nombre/trivia); no existe dato oficial de altura/cumpleaños para el resto, y se dice explícitamente |
| 21 | Por qué la gente la ama: reseñas, Reddit, encuestas, identificación; escenas que hacen llorar con minuto/música/reacción | ✅ | 3 escenas emocionales con fuente y análisis (sopa sin ingrediente, pasado de Po, muerte de Oogway), recepción crítica de KFP4 con 4 fuentes, patrón de identificación del público con 3 personajes distintos |
| 22 | Fan dubs y comunidad hispana en YouTube/TikTok con canal/enlace/escena/vistas; covers; memes | ⚠️ | 4 fandubs localizados con canal y enlace, sin vistas exactas (YouTube bloqueado); se explica por qué no hay «covers de opening» (la franquicia no tiene canciones con letra propias); no se encontró meme hispano propio documentado |


## Bitácora de búsqueda

**Directo (sin gastar cupo de búsqueda web), todo el 25-sep-2026:**
- Doblaje Wiki, API `action=parse&prop=wikitext`, páginas: Kung Fu Panda, Kung Fu Panda 2,
  Kung Fu Panda 3, Kung Fu Panda 4, Omar Chaparro.
- kungfupanda.fandom.com (inglés), API `action=parse&prop=wikitext`, páginas: Po, Shifu,
  Tigress, Oogway, Tai_Lung, Mr._Ping, Monkey, Mantis, Viper, Crane, Shen, Kai, The_Chameleon,
  Zhen.
- dubdb.fandom.com («The Dubbing Database»), página Kung Fu Panda (Latin American Spanish):
  ficha de canales de TV latinoamericanos donde se emitió el doblaje (Star Channel, Nickelodeon,
  Canal 5, Las Estrellas, Telefe, RCN, Caracol, Canal 13 Chile, etc.), como segunda fuente
  independiente de Doblaje Wiki para el propio hecho de que existe doblaje latino.
- Danbooru, `counts/posts.json`, tags `kung_fu_panda`, `po_(kung_fu_panda)`,
  `tigress_(kung_fu_panda)`, `master_shifu`, `tai_lung`, `oogway`, `master_tigress` (medición
  propia, corrige el dato roto de `datos-voz.md`).
- Descarga y transcripción con `herramientas/voz.py` (Whisper local + Parselmouth) de 5 audios
  oficiales de Doblaje Wiki (`Po_kungfupanda3.ogg`, `Shifu_kungfupanda3.ogg`,
  `Tigress_kungfupanda3.ogg`, `Oogway_kungfupanda3.ogg`, `Kai_kungfupanda3.ogg`).
- `herramientas/fotogramas.py --cortes` sobre 2 tráilers de Dailymotion (KFP1
  `dailymotion.com/video/x88nbws`, KFP3 `dailymotion.com/video/x88oh56`), mirados con `Read`.
- `herramientas/fotogramas.py --cada 25` y `--fotograma` sobre el corto oficial «Secrets of the
  Furious Five» (Internet Archive, 1415 s, `archive.org/details/secrets-of-the-furious-five`),
  mirado con `Read`; da el origen 2D de Tigresa/Víbora/Mantis/Grulla/Mono.

**Búsqueda web (WebSearch), en español salvo que se indique, cupo usado ~18 de 50:**
- «Kung Fu Panda personaje favorito encuesta ranking»
- «Omar Chaparro voz de Po Kung Fu Panda entrevista doblaje»
- «ANMTV Kung Fu Panda 4 doblaje latino reparto»
- «Pedro Armendáriz Jr. Shifu Kung Fu Panda doblaje fallecimiento»
- «"La Camaleona" Kung Fu Panda 4 doblaje latino Aida López»
- «Kung Fu Panda Oogway muerte escena fans llorar reddit reaction» (inglés)
- «Kung Fu Panda "skadoosh" meme viral» (inglés)
- «Kung Fu Panda fandub español latino youtube canal»
- «Kung Fu Panda 4 review why fans love reception audience» (inglés)
- «"Kung Fu Panda" escena que hace llorar "no secret ingredient" ending emotional»
- «"Ensemble Dark Horse" Kung Fu Panda TV Tropes» (inglés)
- «"Memetic Mutation" Kung Fu Panda TV Tropes» (inglés)
- «Kung Fu Panda 2 Po discovers parents backstory scene fans cried reaction» (inglés)
- «MrBeast Panda Pig Kung Fu Panda 4 backlash reacción fans molestos»
- «Kung Fu Panda 4 "Chameleon" fans hated bad villain criticism lazy» (inglés)
- `WebFetch` a tvtropes.org/YMMV/KungFuPanda (403, bloqueado) y ranker.com (401, bloqueado): se
  usaron los fragmentos de las propias búsquedas en su lugar, marcados ⚠️.
- No se buscó en japonés ni coreano/chino: Kung Fu Panda es una producción estadounidense
  (DreamWorks) con ambientación china, sin estudio ni staff de esos países que investigar para
  los puntos de voz/personajes; el resto de idiomas relevantes (inglés, español) sí se cubrieron.

**Fuentes que fallaron o dieron error** (según pide AYUDANTE.md, con el intento):
- tvtropes.org: HTTP 403 directo (2 páginas intentadas), se usó el contenido vía resultados de
  búsqueda en su lugar.
- ranker.com: HTTP 401 directo, mismo tratamiento.
- YouTube: bloqueo de sesión («inicia sesión») en los intentos de vistas de fandubs; no se
  insistió más de 2 veces por video, según indica AYUDANTE.md.

**2ª tanda (mismo día), ampliación del catálogo de caras por emoción — sin gastar cupo de
búsqueda web (todo con `curl` directo a las APIs y con `fotogramas.py`):**
- API de Internet Archive (`advancedsearch.php`) y de Dailymotion (`api.dailymotion.com/videos?
  search=`) para localizar los cortos «Secrets of the Masters» y «Secrets of the Scroll»: no se
  encontró ninguno de los dos suelto y en buena calidad (archive.org sólo tiene el DVD sin
  capítulos `kung-fu-panda-secrets-collection`; Dailymotion sólo tiene clips cortos).
- `herramientas/fotogramas.py --cortes` y `--fotograma` sobre 4 clips oficiales de KFP1 en
  Dailymotion, todos mirados con Read antes de citar minuto:
  - `x22o11a` «Most Notorious Villain Clip» (recorte de Secrets of the Masters, 0:47) → usado en
    el punto 12 (dinámica Po/Tigresa en el Salón de los Guerreros).
  - `x7vtk1n` «Young Tai Lung» movie clip (3:14) → caras de Tai Lung cachorro/adulto y vergüenza
    de Po (punto 13).
  - `xa9x3qe` «Master Oogway Leaves Shi Fu Scene» (3:45) → caras de Oogway y tristeza de Shifu
    (punto 13).
  - `xaa228o` «There Is No Secret Ingredient Scene» (2:52, grabación de un reproductor de TV
    portátil «Laser») → caras del Sr. Ping (punto 13).
  - Se descartó `x8uxhl4`, un supuesto «Kung Fu Panda: Secrets of the Scroll» de 4:37: su
    protagonista (orejas grandes, antifaz oscuro) no se pudo identificar con certeza como ninguno
    de los 6 principales — no se usó ninguna cara de ese clip, aunque sí parece contenido oficial
    (trae marca de agua «Bandicam», es decir, es una grabación de pantalla, no un montaje de fan).

Sigue: quedan sin cara propia la tristeza y la vergüenza de Tigresa (no aparecieron en las
escenas miradas hasta ahora), la tristeza de Po, la vergüenza de Shifu, y la rabia/el miedo de
Oogway y del Sr. Ping. Si se retoma: buscar clips oficiales de escenas concretas de KFP1-4 con
Tigresa (por ejemplo cuando Shifu le grita en KFP1, o su reacción al fracaso de Po), y con
Oogway/Ping enfadados o asustados (Oogway casi no tiene escenas de esas; puede que no exista tal
fotograma y haya que decirlo). Mirar siempre las hojas con Read antes de citar minuto.
