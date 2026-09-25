# Voz y personajes · No Man's Sky (encargo 124)

Investigador de voz, puntos 7, 8, 12, 13, 20, 21 y 22 de ENCARGO.md. Parte de
`partes/datos-voz.md` (recolectado automáticamente) y de lo que ya dejaron
imagen.md/video.md sobre el Viajero, Nada, Polo, Gek/Korvax/Vy'keen (no se
repite esa parte, se enlaza).

**Aviso de género, importante para los otros puntos:** No Man's Sky NO es una
obra con un reparto de personajes con diálogo actuado como una serie: el
protagonista (el Viajero) es un traje-exotraje mudo y personalizable, sin cara
fija, y los alienígenas hablan un idioma alienígena sintetizado, no actuado.
«Personajes» aquí son las entidades con nombre propio y lore (Nada, Polo,
Artemis, Apollo, -null-, el Atlas, los Centinelas) y las tres especies
jugables (Gek, Korvax, Vy'keen) como arquetipos.

## Hallazgos

### Punto 8 · Doblaje latino (y por qué NO existe)

- **No existe ninguna versión de español latinoamericano del juego, ni en
  texto ni en voz** (a diferencia del portugués, que sí tiene Portugal Y
  Brasil por separado): la lista oficial de idiomas de Steam sólo trae
  «Español de España» marcado con asterisco de «idioma con localización de
  audio» · Steam Store API (oficial) · https://store.steampowered.com/api/appdetails?appids=275850 · ✅ (dato oficial de la tienda)
- Confirmado por jugadores: un hilo de Steam Community («¿Doblaje Español
  latino?», jul-2018) explica que, aunque el juego dice traer doblaje en
  español, al activarlo «sale en español de España», sin opción latina ·
  https://steamcommunity.com/app/275850/discussions/0/1762481957308442405/ ·
  ✅ (dos fuentes: tienda oficial + comunidad, coinciden)
- **Doblaje Wiki no tiene página de No Man's Sky**: probé `No_Man's_Sky`,
  `No_Man%27s_Sky_(videojuego)` y `No_Man's_Sky` por la API (`action=parse`,
  `prop=wikitext`) → los tres dan «missingtitle»; probé también
  `action=query&list=search&srsearch=No Man's Sky` → no aparece entre los
  resultados (que sí devuelve otras fichas, prueba de que la búsqueda
  funciona) · https://doblaje.fandom.com/es/api.php · ✅ (confirma la ausencia,
  ya lo había detectado `recolectar.py`)
- **Por qué no hay «doblaje» tradicional**: los alienígenas (Gek, Korvax,
  Vy'keen) no tienen diálogo actuado por humanos, sino una voz sintetizada
  proceduralmente por el diseñador de sonido **Paul Weir** con un software
  propio, «VocAlien» (un tracto vocal modelado físicamente, tocado como un
  instrumento con MIDI); por eso suena igual en todos los idiomas · ficha de
  reparto de Behind The Voice Actors («Aliens — voiced by Paul Weir», único
  actor listado en toda la ficha) · https://www.behindthevoiceactors.com/video-games/No-Mans-Sky/
  · y entrevista técnica en Audiokinetic/A Sound Effect sobre VocAlien ·
  https://www.audiokinetic.com/en/blog/behind-the-sound-of-no-mans-sky-a-qa-with-paul-weir-on-procedural-audio/
  · ✅ (dos fuentes independientes, mismo dato)
- La única «voz» de diálogo real (no alienígena) del juego es **Telamon**, la
  IA que habita el exotraje y da avisos («voz de alarma» del exotraje, HUD:
  peligros, salud, vida de soporte); es ese aviso el que sí está doblado, y
  sólo en español de España según la tabla de idiomas de Steam (arriba) ·
  wikitext de la página «Telamon» de la wiki de Fandom nomanssky ·
  https://nomanssky.fandom.com/wiki/Telamon · ✅ (wiki + coincide con lo que
  describe otro jugador en el hilo de Steam citado arriba: «sólo unas pocas
  frases con tono cibernético»)
- **Tráiler narrado por Rutger Hauer** («I've Seen Things», revelado en el
  escenario de PlayStation en la Paris Games Week, octubre de 2015; anunciaba
  la fecha de junio de 2016): Hauer recita una variación de su propio
  monólogo «lágrimas en la lluvia» de Blade Runner («I've seen things you
  people wouldn't believe…») adaptada al universo del juego · PCGamesN ·
  https://www.pcgamesn.com/no-mans-sky/no-mans-sky-trailer-reveals-june-release-date-also-rutger-hauers-voice
  y Nerdbot (posible última grabación de voz de Hauer, murió en jul-2019) ·
  https://nerdbot.com/2022/02/17/no-mans-sky-trailer-features-rutger-hauers-likely-last-voice-over/
  · ✅ (dos fuentes)
- Tráiler oído con `voz.py` (mirror en Dailymotion, YouTube pide login):
  registro grave (110 Hz), muy expresivo (33.3 semitonos), velocidad lenta
  (0.54 palabras/s); primera frase en 0:02, Whisper transcribe «I've seen
  things, a few things before, the sun and more galaxies... resources...
  pleasures unknown» (revisar nombres propios, Whisper se equivoca, pero el
  tono y el minuto son fiables) · propio, sobre
  https://www.dailymotion.com/video/x443lhp?t=2 · ✅ (vídeo oficial, mirror +
  coincide con la cita publicada por PCGamesN/Nerdbot) · 0:02
- No encontré ningún doblaje o subtitulado al español de este tráiler
  concreto de Hauer (ni oficial ni de fans): búsquedas «lágrimas en la lluvia
  No Man's Sky homenaje español», «No Man's Sky doblaje fan español he visto
  cosas tráiler» → nada.
- ANMTV (una de las fuentes que pide el encargo para doblaje) está bloqueado
  por política de la organización en este contenedor (`ERR_TUNNEL_CONNECTION_FAILED`,
  probado con curl y con `navegar.py`); no pude comprobar si cubrió el tema
  (poco probable, es un juego, no anime).

### Punto 22 · Fan dubs y comunidad hispana

- **No hay tradición de fandub de No Man's Sky** porque casi no hay diálogo
  que redoblar (ver punto 8: protagonista mudo, alienígenas con voz
  sintetizada igual en todos los idiomas, y el único aviso de voz real
  —Telamon— es muy corto y técnico, no narrativo) · razonamiento propio a
  partir de los datos de arriba · ✅
- Búsquedas específicas sin resultado: «No Man's Sky fandub español tráiler
  parodia YouTube», «No Man's Sky fandub latino» (Dailymotion, ya en
  `datos-voz.md`: los resultados son clips de gameplay comentado, no
  redoblajes) → no hay fandub dedicado.
- Lo que sí produce la comunidad hispana: series largas de gameplay
  comentado en español con temporadas numeradas, por ejemplo «NO MAN'S SKY
  2022 GAMEPLAY ESPAÑOL T2», que le dedica un episodio entero a la historia
  de Artemis («T2 #7 · COMUNICACIÓN CON ARTEMIS») · YouTube (resultado de
  búsqueda, canal de terceros) · https://www.youtube.com/watch?v=yvb-G382E2s
  · ⚠️ (una fuente, no pude abrir el vídeo por el bloqueo de login de
  YouTube en este servidor para comprobar vistas/fecha exacta)
- Vídeo-análisis reciente en español sobre la historia de redención del
  juego, «De ESTAFA a OBRA MAESTRA: No Man's Sky» (mayo-2026) · YouTube
  (resultado de búsqueda) · https://www.youtube.com/watch?v=EXLFqQKsRZw · ⚠️
  (una fuente, no verificado el contenido exacto por el mismo bloqueo)
- Dato relevante para el Discord de doblaje: como no hay versión
  latinoamericana ni en texto (punto 8), la comunidad hispanohablante que
  juega NMS lo hace en inglés o en español de España, nunca en un «latino»
  oficial · deducido de los datos oficiales de Steam ya citados · ✅

### Punto 7 · Encuestas de popularidad

- No existe una encuesta oficial de popularidad de «personajes» de Hello
  Games (el juego no tiene un reparto fijo que rankear); mejor proxy
  encontrado: hilo de Reddit «What's your favorite Alien race in the game
  and why?», 131 votos y 137 comentarios, r/NoMansSkyTheGame · Reddit vía
  Arctic Shift · https://redd.it/1msvwup · ✅ (hilo real, con comentarios
  propios leídos abajo)
- En los comentarios de ese hilo: a los Gek los llaman «adorable», «cute»
  («The Gek because they're adorable and super cute (And yes, I know...
  I know)», 1 voto) y también hay defensores de los Korvax «por el aspecto
  técnico» y de los Autophage (4ª especie, añadida en la actualización
  Echoes) con la broma recurrente «Autophage: Am I a joke to you?» · mismo
  hilo, comentarios · ✅ (leído directamente, no de memoria)
- El juego lleva nominado a «Labour of Love» en los Steam Awards varios años
  seguidos (al menos 2018, 2023, 2024 y 2025) sin ganar nunca, y cada
  diciembre la comunidad hace campaña para votarlo («Lets help NMS to win
  the Labour of Love award finally!», «This better win the Labor of Love
  award for 2025») · hilos de Steam Community (resultados de búsqueda) ·
  https://steamcommunity.com/app/275850/discussions/0/694248493352507893/
  y https://steamcommunity.com/app/275850/discussions/0/691994126364810870/
  · ✅ (dos hilos, mismo patrón repetido varios años)
- La valoración global en Steam pasó de «Mayormente positiva» a **«Muy
  positiva»** en 2024, tras tres años estancada en «mayormente positiva» ·
  TweakTown (resumen vía búsqueda, la web bloquea curl con 403) y Pocket
  Tactics, que la llama «the greatest comeback story in gaming» ·
  https://www.pockettactics.com/no-mans-sky/review · ⚠️ (confirmado por dos
  fuentes en el resumen de búsqueda, pero no pude leer el artículo de
  TweakTown entero por el bloqueo; el dato del cambio de categoría de Steam
  sí es verificable en la propia página de reseñas de Steam)

### Punto 12 · Lo que ama el fandom y qué NO hacer

- **El gran chiste/mito interno del fandom es su propio lanzamiento
  desastroso (ago-2016) y la «remontada»**: Sean Murray prometió funciones
  (multijugador, criaturas gigantes) que no estaban al lanzar, la comunidad
  se sintió engañada, hubo devoluciones incluso en PS4 (Sony rompió su
  política de no reembolsos) y la ASA británica investigó por publicidad
  engañosa en sep-2016 (falló a favor de Hello Games en 2017) · IBTimes ·
  https://www.ibtimes.com/no-mans-sky-devs-did-not-mislead-players-asa-says-ruling-hello-games-valve-case-2453084
  y TechRadar · https://www.techradar.com/news/no-mans-sky-didnt-mislead-consumers-rules-the-asa
  · ✅ (dos fuentes)
- Ocho años de actualizaciones gratis convirtieron el chiste en orgullo: «tal
  vez puede tirar un No Man's Sky» (*maybe it can pull a No Man's Sky*) es
  ahora jerga común en toda la industria de videojuegos para «lanzar roto y
  redimirse a base de parches gratis durante años» · resumen de búsqueda con
  cita textual del fenómeno (fuente primaria: cobertura de Eurogamer sobre
  Sean Murray, 10 años del juego) · https://x.com/eurogamer/status/2086817804225819003
  · ⚠️ (una fuente citada directamente, el resto son medios menores/agregador
  de memes)
- **Qué NO hacer, por eso mismo**: no presentar el juego base de 2016 como si
  ya tuviera todo lo prometido (sin multijugador, sin las criaturas
  gigantes); no burlarse de Sean Murray de forma cruda — el fandom actual lo
  trata con cariño, no con el mismo tono de 2016 · deducido de los datos de
  arriba + hilos de Steam Community sobre premios (el propio fandom vota
  para premiar al estudio cada año) · ✅
- No inventar diálogo hablado «entendible» para los alienígenas: su idioma es
  deliberadamente ininteligible/pictográfico (se traduce por palabras sueltas
  a medida que el jugador aprende, nunca frases completas dobladas) — un
  cuadro de diálogo de burbuja blanca genérica quedaría doblemente falso aquí,
  porque el juego real muestra terminales holográficas y texto de bitácora,
  no globos de cómic · wikitext de Gek (`Gek (language)`) y ficha de Telamon
  (arriba) · ✅
- No mostrar una única «cara» fija para el Viajero como si fuera canon: el
  protagonista es un exotraje sin rostro y totalmente personalizable (ya lo
  documentó el investigador de vídeo en el punto 14) · confirmado también en
  la wiki de Nada («comforts the player» independientemente de la apariencia)
  · ✅ (coincide con `video.md`)
- Lo que sí celebra el fandom en sus posts con más votos: capturas de
  tormentas y auroras de planetas («storms in this game look so damn good»,
  3064 votos), la sensación de asombro al aterrizar en un planeta nuevo, y
  discusiones apasionadas sobre naves/corbetas favoritas («my squadron will
  beat up your squadron», 794 votos) · Reddit, ya recolectado en
  `datos-voz.md` · ✅

### Punto 13 · Personajes con nombre propio y las tres especies

- **Nada** (Entidad Sacerdote, Korvax): vive en la Anomalía Espacial junto a
  Polo; es una Korvax «no conforme» que se resiste a la Convergencia (la
  mente colmena Korvax intenta «borrarla de la existencia» recuperando el
  control de su cuerpo); se vuelve más paranoica y pesimista según avanza la
  partida; viste una capa roja y azul con tres naves y el símbolo del Atlas
  bordados · wikitext de «Priest Entity Nada» · https://nomanssky.fandom.com/wiki/Priest_Entity_Nada
  · ✅ (wiki, cruzado con la imagen `Nada Cape.jpg` que ya midió el
  investigador de imagen)
- **Polo** (Especialista, Gek): traductor enviado a un puesto remoto como
  castigo por su comportamiento; curioso por naturaleza · wikitext de
  «Specialist Polo» · https://nomanssky.fandom.com/wiki/Specialist_Polo · ✅
- **La dinámica Nada-Polo** (para láminas de grupo): en otra dimensión, con
  los Centinelas habiendo aniquilado toda vida, Nada salvó a Polo de morir;
  viajaron juntos hacia el centro de la galaxia perseguidos por Centinelas;
  antes de morir, ese Polo le dijo a Nada «nos volveremos a encontrar en otro
  universo» — y ahora, sin saberlo del todo, están reunidos en la Anomalía
  · misma página wiki de Nada, sección «Lore» · ✅
- **Artemis** (Traveller, aparece en la ruta narrativa «Artemis Path»,
  añadida en la actualización Atlas Rises/NEXT): el jugador la conoce por
  radio (Holo-Terminus) y la ayuda a triangular su posición; al final de esa
  primera conversación se descubre que la ubicación de Artemis «no existe» —
  ya está muerta — y el jugador debe decidir si «sube» su alma/datos a una
  simulación o la deja descansar · wikitext de «Artemis» ·
  https://nomanssky.fandom.com/wiki/Artemis · ✅
- **Apollo** (Traveller, mismo arco): antes tenía cuerpo de carne y hueso,
  ahora reemplazado casi todo por robótica; frío y desinteresado al
  principio, sólo le importan las unidades (el dinero) — «ha llegado a la
  conclusión de que el dinero es lo único que importa en la vida» ·
  wikitext de «Apollo» · https://nomanssky.fandom.com/wiki/Apollo · ✅
- **-null-** (Null, personaje central de Atlas Rises): un Traveller de otro
  universo que desafió al Atlas y vivió una eternidad para explorar y
  catalogar cada mundo de su universo; el Atlas le reveló que, aun así, era
  «uno más entre infinitos viajeros», lo que -null- interpretó como que su
  vida entera no significó nada; desde entonces el Atlas dejó de hablarle;
  está amargado y celoso de que el jugador sea el «elegido» en su lugar. Cita
  textual: «I was born to travel, to see these worlds, to catalogue them, to
  give a name to every creature, every planet. The skies... they were mine.»
  · wikitext de «-null-» · https://nomanssky.fandom.com/wiki/-null- · ✅
- **Gek**: especie anfibia mercantil, ojos y pico de ave, dedos con garras;
  sus ancestros (los «First Spawn») fueron un imperio genocida sometido por
  los Centinelas; cultura corporativa/plutocrática, títulos ligados al
  comercio; se comunican con habla Y con señales olfativas (usan aditivos
  llamados GekNip para provocar emociones en otros con el olor) · wikitext de
  «Gek» · https://nomanssky.fandom.com/wiki/Gek · ✅
- **Korvax**: raza mecánica muy intelectual, quieren saberlo todo sobre la
  ciencia y su propia existencia; adoran al Atlas como dios; su casco varía
  según su rol en la «Convergencia» (Analista, Matemático, Físico, Geólogo,
  Erudito, Entidad Divina…) y siempre se les ve con una tablet táctil ·
  wikitext de «Korvax» · https://nomanssky.fandom.com/wiki/Korvax · ✅
- **Vy'keen**: reptiles humanoides guerreros, posición encorvada, mandíbula
  prominente; código de honor estricto del «Alto Mando»; antiguamente
  dominaban la galaxia hasta perder una guerra por la traición de los First
  Spawn Gek; siguen siendo la mayor potencia militar y ven al Atlas como un
  falso dios (según su profeta Hirk el Grande) · wikitext de «Vy'keen» ·
  https://nomanssky.fandom.com/wiki/Vy%27keen · ✅
- **El Atlas**: entidad cósmica omnipresente, «creador» alegado del universo,
  venerado por Korvax y Gek; en la trama se revela que el universo es una
  simulación y el Atlas es literalmente el ordenador que la controla; su
  forma de hablar es un monólogo entrecortado, en mayúsculas irregulares, con
  cadencia de terminal informática (relevante para el punto 17 de estilo de
  texto, lo dejo anotado para el redactor) · wikitext de «The Atlas» ·
  https://nomanssky.fandom.com/wiki/The_Atlas · ✅
- **Centinelas**: drones policía de origen y motivos poco claros; son el
  antagonista recurrente más común de todo el juego · wikitext de
  «Sentinel» · https://nomanssky.fandom.com/wiki/Sentinel · ✅
- **Telamon**: protocolo/IA que el Atlas incorpora al exotraje del jugador
  para «vigilar sus propias acciones»; se convierte en la voz de aviso del
  traje (peligros, salud); en sus registros habla de que «nos están
  cazando» (los Centinelas) y de un lugar «bajo la realidad, un mundo de
  cristal» — tono analítico y melancólico a la vez · wikitext de «Telamon» ·
  https://nomanssky.fandom.com/wiki/Telamon · ✅

### Punto 20 · Gustos y detalles de cada personaje

- Gek: lo que aman es literalmente el dinero — «Units» — y el comercio;
  gastronómicamente no tienen «comida» documentada pero sí un equivalente:
  el GekNip (aditivo hecho de la planta NipNip) que usan para provocar
  emociones por el olfato, la cosa más parecida a un «gusto» propio de la
  especie · wikitext de Gek · ✅
- Korvax: lo que aman es el conocimiento y la aprobación del Atlas; su
  «objeto que siempre llevan» es la tablet táctil con la que se les ve
  trabajar siempre · wikitext de Korvax · ✅
- Vy'keen: lo que aman es el combate y el honor; estatura media citada por la
  wiki en 6 pies 5 pulgadas (~1,96 m), pero la propia wiki marca la cifra con
  «cita necesaria» · wikitext de Vy'keen · ⚠️ (una fuente, y la propia wiki
  duda del dato — no dar la cifra como segura en la biblia)
- Apollo: odia la sentimentalidad, sólo le importan las unidades (dinero);
  es la definición de un personaje que «se ve a sí mismo» como una máquina de
  hacer negocios tras perder su cuerpo original · wikitext de Apollo · ✅
- -null-: su obsesión es catalogar y nombrar cada criatura y cada planeta que
  existe; se ve a sí mismo como alguien que hizo «lo correcto» al sobrevivir
  a la eternidad, pero el Atlas le hizo sentir que fue en vano · wikitext de
  -null- · ✅
- Nada: lo que la define es la paranoia creciente hacia su propia
  Convergencia (su «gente») y una capa roja/azul con el símbolo del Atlas
  como objeto distintivo (ya medida en hex por el investigador de imagen) ·
  wikitext de Nada · ✅
- El Viajero (jugador): el objeto que siempre lleva es el Multiherramienta
  (por defecto, la Waveform Focuser N56-P) y viste el Exotraje — ya
  documentado con hex y fuente por imagen.md, no lo repito aquí; lo confirmo
  como coherente con lo que vi en el wikitext de Multi-Tool y Exosuit · ✅

### Punto 21 · Por qué la gente ama No Man's Sky

- Hoy se la describe como **«la mayor remontada de la historia de los
  videojuegos»**: Pocket Tactics titula su reseña así, y TouchArcade dice que
  ocho años después es «uno de los mejores juegos que se pueden jugar en
  2024» tras años de actualizaciones gratuitas · Pocket Tactics ·
  https://www.pockettactics.com/no-mans-sky/review y TouchArcade ·
  https://toucharcade.com/2024/07/29/no-mans-sky-2024-review/ · ✅ (dos
  fuentes)
- La valoración de Steam subió de «Mayormente positiva» a **«Muy positiva»
  en 2024**, tras 3 años estancada en la categoría anterior — dato
  verificable en la propia página de reseñas de Steam · TweakTown (resumen)
  y la página de reseñas de Steam · https://steamcommunity.com/app/275850/reviews/
  · ⚠️ (el resumen de TweakTown no lo pude leer completo, 403; el cambio de
  categoría en sí es comprobable directamente en Steam)
- Lo que dice la gente que ama, con sus palabras: «Why I Love No Man's Sky.
  Thank you Hello Games for a lovely game» (107 votos) y el hilo genérico de
  «por qué lo amo» con varias respuestas centradas en la sensación de
  explorar («man I love exploring new planets», 333 votos) · Reddit, ya en
  `datos-voz.md` · ✅
- Con qué se identifica el público: con la mezcla de asombro y soledad de la
  exploración espacial («captures both the breathtaking beauty and the
  haunting loneliness of deep space», TouchArcade) más que con un personaje
  concreto — coherente con que no hay protagonista con rostro fijo · ✅
- **La escena/quest que más se cita como emotiva**: la ruta «Artemis Path»
  (ver punto 13) — conocer por radio a alguien que resulta que ya murió, y
  tener que decidir si «revivirla» digitalmente o dejarla descansar; el
  propio nombre de una de sus misiones es «A Leap in the Dark» · wikitext de
  Artemis · ⚠️ (la lectura emocional es interpretación propia sobre la
  lore confirmada en la wiki; no encontré un comentario de Reddit con muchos
  votos que diga explícitamente «lloré con esto» — lo busqué, ver Bitácora)
- Reconocimiento pese a nunca ganar: nominado a «Labour of Love» en los Steam
  Awards varios años (2018, 2023, 2024, 2025) sin ganar nunca — y aun así la
  comunidad organiza campañas de voto cada diciembre, señal de cariño
  sostenido en el tiempo · hilos de Steam Community ya citados en el punto 7
  · ✅
- El propio escándalo de 2016 (devoluciones, investigación de la ASA
  británica) es parte de por qué se ama tanto la versión actual: la sensación
  de «me quedé, y valió la pena» es un tema recurrente en las reseñas de
  usuarios de Steam · IBTimes/TechRadar (punto 12) + Steam reviews · ✅

## Lo mejor para la lámina

- El aviso del exotraje (Telamon) y las terminales del Atlas son el modelo
  real de «cuadro de diálogo» de esta obra: texto de consola/holograma, NUNCA
  una burbuja blanca de cómic.
- La cita de -null- («I was born to travel, to see these worlds, to catalogue
  them...») funciona como frase de cabecera para un canal contemplativo o de
  escritura.
- La capa roja/azul con el símbolo del Atlas de Nada es un accesorio muy
  reconocible y ya con hex medido por imagen.md.
- Las hojas de info oficiales de Gek/Korvax/Vy'keen (`NmsFaction_*.jpg`,
  imágenes 1700-2200 px, ya en `voz.json`) son fichas de personalidad
  listas para explicar cada especie en una lámina de grupo.
- El propio relato de «remontada» (2016 roto → hoy alabado) es un concepto de
  lámina en sí mismo: encaja con un canal sobre constancia/mejora continua.

## No encontré

- Encuesta oficial de popularidad de personajes de Hello Games (el juego no
  tiene un elenco fijo que rankear oficialmente); usé como proxy un hilo de
  Reddit con votos reales (ver punto 7).
- Doblaje latinoamericano: confirmado que NO EXISTE (ni texto ni voz), no es
  que no lo encontrara — está documentado arriba con fuente oficial de Steam.
- Fandub en español de ningún tráiler o material de No Man's Sky: busqué
  «No Man's Sky fandub español», «fandub latino» y el caso concreto del
  tráiler de Rutger Hauer; no apareció ninguno.
- ANMTV: la web está bloqueada por la política de red de este contenedor
  (`connect_rejected` tanto en curl como en `navegar.py`); no pude comprobar
  si cubrió alguna vez el juego (poco probable, es un site de anime/doblaje
  de animación, no de videojuegos en general).
- Comentarios de Reddit con muchos votos que mencionen explícitamente llorar
  con la ruta de Artemis: probé `body=Artemis` y varios términos sueltos
  («cry», «cried», «chills», «beautiful», «masterpiece») en el buscador de
  Arctic Shift; las búsquedas de una sola palabra devuelven 0 resultados de
  forma sistemática (parece una limitación del buscador de título con
  términos cortos, no ausencia real de esos hilos) — la lectura emotiva de la
  quest queda como ⚠️ interpretación propia sobre lore confirmada, marcada
  así arriba.
- Ficha completa de Behind The Voice Actors más allá de «Aliens — Paul
  Weir»: el sitio usa Cloudflare y aunque `navegar.py` sí cargó la página
  principal, no tiene más actores listados (la ficha en sí dice «Voice
  Actors on BTVA: 1»), así que no es que faltara mirar más, es que no hay más.

## Bitácora

- Doblaje Wiki API (`doblaje.fandom.com/es/api.php`): 3 variantes de título +
  1 búsqueda de texto libre → sin página de la obra (español).
- Fandom `nomanssky.fandom.com/api.php`: wikitext de Nada→Priest Entity Nada,
  Polo→Specialist Polo, Gek, Korvax, Vy'keen, The Atlas, Sentinel, Artemis,
  Apollo, -null-, Telamon; `imageinfo` de 8 imágenes para medir tamaño real
  (inglés).
- WebSearch (inglés y español): doblaje/voces NMS, voice actor narrator
  credits, Paul Weir alien language, Rutger Hauer trailer, meme Sean Murray
  redemption arc, Steam Awards Labour of Love, review 2024/2025 comeback,
  fandub español, lágrimas en la lluvia homenaje, gameplay comentado latino.
- `behindthevoiceactors.com` vía `navegar.py` (Cloudflare bloquea curl
  directo) → ficha de reparto.
- Steam Store API `appdetails` (oficial) → tabla de idiomas.
- `navegar.py` sobre Steam Community (discusión doblaje) y Steam Store
  (tabla de idiomas) → funcionó bien, sin bloqueo.
- `herramientas/voz.py` sobre el tráiler de Rutger Hauer (mirror Dailymotion
  x443lhp) → transcripción + análisis de voz.
- Arctic Shift (Reddit, inglés): `posts/search` con `title=` (nota: el
  parámetro `sort` sólo acepta `asc`/`desc`, no `sort_type`; búsquedas de una
  sola palabra como «cry», «chills», «beautiful», «masterpiece» devuelven 0
  resultados aunque el hilo exista — el buscador de título parece exigir
  coincidencias más largas o exactas — mientras que frases de 2-3 palabras sí
  funcionan) y `comments/search` con `body=Artemis`.
- ANMTV bloqueado por política de proxy del contenedor (`connect_rejected`),
  probado por curl y por `navegar.py`.
- Wikipedia API: `Development of No Man's Sky` (extracto, confirma a Paul
  Weir y 65daysofstatic) funcionó; una segunda consulta a `No Man's Sky` dio
  «too many requests» (límite de tasa) y no reintenté para no gastar cupo.
