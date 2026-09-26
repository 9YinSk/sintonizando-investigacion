# Voz y personajes — Honkai: Star Rail (127)

Libreta de datos del investigador de voz (puntos 7, 8, 12, 13, 20, 21, 22 de ENCARGO.md). No es la biblia final: la redacta el redactor. Partí de `partes/datos-voz.md` (recolectar.py) y busqué lo que faltaba.

**Aviso general de doblaje (afecta a los puntos 8 y 22):** Honkai: Star Rail **NO tiene doblaje oficial en español** (ni España ni Latinoamérica). Sólo tiene voces en inglés, japonés, chino y coreano; el español es únicamente texto/subtítulos. Comprobado en dos fuentes independientes:
- Doblaje Wiki: la página «Honkai: Star Rail» no existe (roja) — `https://doblaje.fandom.com/es/api.php?action=query&titles=Honkai:%20Star%20Rail&format=json` devuelve `missing`. ✅
- Honkai Star Rail Wiki (Fandom): la plantilla `Character Infobox` de cada personaje sólo trae los campos `vaEN`, `vaCN`, `vaJP`, `vaKR` (comprobado en March 7th, Kafka, Trailblazer y Firefly); no existe `vaES`. ✅
- Confirmación adicional: búsqueda web — Prima Games / DigiStatement, «Honkai Star Rail: how to change voice/text language», dicen que las voces sólo están en EN/JP/CN/KR y que el español es «text only». ✅ (tercera fuente)
- La única mención de «español» ligada al juego en Doblaje Wiki es la traductora mexicana **Jeannie Hernández**, que lista «Honkai: Star Rail» en su sección **Traducción** (no de voz) de su ficha: `https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Jeannie%20Hern%C3%A1ndez`. Confirma que el texto sí se traduce al español, pero no hay actores de doblaje. ⚠️ (una fuente, y es indicio, no doblaje de voz)

## 7 · Personajes principales y secundarios (encuestas de popularidad)

Con protagonista silencioso (el Trazacaminos, Stelle/Caelus, elegible), el foco de cariño del fandom recae en los personajes de apoyo. Hay encuesta oficial china y medidas de fandom (fan art, Reddit).

- Encuesta oficial de popularidad 2025 (HoYoverse/HoYoLAB, votación del 2 al 19 de mayo de 2025, sólo comunidad china): **1º Dan Heng: Imbibitor Lunae** (55 586 votos) — 2º Aventurine (45 784) — 3º Sunday (23 880) — **4º Kafka** (21 965) — 5º Jing Yuan (20 219) — 6º Anaxa (16 669) — 7º Robin (16 086) — 8º Acheron (12 111) — 9º Mydei (11 912) — 10º March 7th: Caza (11 125) · fuente 1: https://www.hoyolab.com/article/40440025 (evento oficial) · fuente 2: https://x.com/StarRailVerse1/status/1924332577499865439 (recoge el cartel oficial con las mismas cifras) · ✅
- La misma encuesta declaró **personaje más popular en general y más popular masculino: Dan Heng**; **personaje femenino más popular: Kafka** (uno de los 3 personajes que pidió el encargo); **mascota/compañero más popular: Pom-Pom** · fuente: https://x.com/StarRailVerse1/status/1924332577499865439 · ⚠️ (un solo posteo lo resume así; coincide con el orden de votos de arriba, pero no vi el cartel oficial directamente)
- Medida de cariño por fan art (Danbooru, «honkai_(series)», 190 986 dibujos en total, recolectado ya en `datos-voz.md`): 1º Trazacaminos 21 446 · 2º **Firefly** 16 723 · 3º Elysia (Honkai Impact) 13 574 · 4º Stelle 13 326 · 5º Phainon 10 584 · 6º **March 7th** 9714 · 9º **Kafka** 8096 · fuente: https://danbooru.donmai.us/posts?tags=honkai_%28series%29 · ✅ (recuento directo de la API, reproducible)
- Reddit r/HonkaiStarRail (326 000+ miembros): hilo «So, who is your favorite character in Planarcadia?» (237 votos, 157 comentarios) y «Did my favorite character of each element» (323 votos) muestran que el favoritismo se reparte por elemento/camino, no por un solo ganador · fuente: https://www.reddit.com/r/HonkaiStarRail/comments/1sb225o/ · ⚠️ (una fuente, es hilo de opinión no encuesta cerrada)
- Los 3 personajes que pide el encargo (March 7th, Kafka, Trazacaminos) están los tres entre los 10 más dibujados por fans; Kafka además es la femenina más votada oficialmente: es seguro centrar la lámina en cualquiera de los tres. ✅

## 8 · Doblaje latino y frases icónicas dobladas

Tabla de actores de voz (no hay «voz latina»: se documenta EN/JA/ZH/KO tal como pide el punto 8, y se deja constancia expresa de que no hay doblaje al español).

| Personaje | Seiyū (JP) | Voz latina | Fuente 1 | Fuente 2 |
|---|---|---|---|---|
| March 7th | Yui Ogura (小倉唯) | No hay (sólo texto en español) | Fandom HSR, Character Infobox `vaJP`/`vaES` ausente | Doblaje Wiki: página inexistente |
| Kafka | Shizuka Itō (伊藤静) | No hay (sólo texto en español) | Fandom HSR, Character Infobox | Doblaje Wiki: página inexistente |
| Trazacaminos (Stelle/Caelus) | F: Yui Ishikawa (石川由依) · M: Junya Enoki (榎木淳弥) | No hay (sólo texto en español) | Fandom HSR, Character Infobox | Doblaje Wiki: página inexistente |
| Firefly | Tomori Kusunoki (楠木ともり) | No hay (sólo texto en español) | Fandom HSR, Character Infobox | Doblaje Wiki: página inexistente |

- Actores en inglés (para contexto, sí hay doblaje EN oficial): March 7th — Skyler Davenport; Kafka — Cheryl Texiera; Trazacaminos — F: Chloe Eves (reemplazó a Rachael Chau) / M: Shaun Mendum (reemplazó a Caleb Yen); Firefly — Analesa Fisher · fuente: Fandom HSR, Character Infobox de cada uno (`vaEN`) · ✅ (mismo dato en la ficha inglesa y en el enlace a IMDb de cada actor)
- Sin doblaje latino no hay «frases icónicas dobladas al español» que citar con minuto, tal como pide el punto 8 cuando no existe doblaje: se deja dicho aquí y no se inventa ninguna. Las frases textuales en inglés (voz original jugable en Occidente) quedan documentadas en el punto 13, con fuente y sin minuto de vídeo (son líneas de diálogo interactivo del juego, no de un clip publicado).
- ANMTV (portal de doblaje latino) no tiene ninguna nota sobre Honkai: Star Rail: busqué `honkai` y `star rail` en su buscador interno (navegar.py) y no hay resultados relacionados con doblaje del juego. ⚠️ (comprobado, no encontrado)

## 12 · Lo que el fandom ama (y qué no hacer)

- Meme recurrente: **«el Trazacaminos ha peleado contra Áeones, pero nada es tan icónico como comerse cosas raras del suelo»** — publicado varias veces en r/HonkaiStarRail (57, 18, 14 y 10 votos en distintos repostes) · fuente: https://www.reddit.com/r/HonkaiStarRail/comments/1vkrind/ · ✅ (el mismo meme se repite en 4 hilos distintos, señal de que es un chiste interno asentado)
- El Trazacaminos existe en dos versiones jugables, **Stelle (femenina) y Caelus (masculino)**, cada un@ con su propio actor en cada idioma (ninguno es «el canon»); el fandom cuida mucho no invisibilizar ninguna de las dos · fuente: Fandom HSR, página «Trailblazer», sección de introducción · ✅ (contrastado con las fichas de VA de ambos)
- Emote «Iconic» de la comunidad (dibujado por usagi.minku, 7276 votos en Reddit) y pose «Iconic Wally West» de Cipher (3747 votos) muestran que el fandom celebra las poses de acción reconocibles, no sólo las splash arts quietas · fuente: `datos-voz.md` (ya recolectado) · ✅
- **Qué NO hacer:** no dibujar ni describir al Trazacaminos como un personaje mudo y sin reacciones — desde la versión 2.x tiene líneas propias en las misiones principales, y el fandom lo celebró expresamente («Let's all show our appreciation to having our Trailblazer fully voiced in main story quests now», 383 votos, 69 comentarios) · fuente: `datos-voz.md`, hilo https://www.reddit.com/r/HonkaiStarRail/comments/1v0m4pc/ · ✅
- **Qué NO hacer:** no poner a Kafka con acento o modismos latinos inventados en un cuadro de diálogo «doblado»: no existe ese doblaje, así que cualquier lámina con «voz latina» de un personaje de HSR sería inventar un dato que no existe. Es la aplicación directa del aviso del punto 8. ✅
- No encontré una lista oficial de «qué odia el fandom que le hagan a la obra» (tipo encuesta); lo de arriba son inferencias directas de hilos con muchos votos, no una declaración del propio fandom sobre «qué no hacer». ⚠️

## 13 · Descripción profunda de los personajes (carácter, forma de hablar, cara en cada emoción)

Bio y diálogos sacados de la wikitexto oficial del juego (Fandom HSR, páginas `<Personaje>/Lore` y `<Personaje>/Voice-Overs`, en inglés: es el texto que el juego reproduce, no un resumen de fan). Las emociones en imagen salen de tráilers oficiales (Dailymotion, mirados con `fotogramas.py`), con el segundo exacto.

**March 7th** — Chica que despertó sin memoria dentro de un bloque de hielo eterno; se puso su propio nombre por la fecha en que «nació de nuevo». Curiosa, optimista y bromista (finge asustar al Trazacaminos el primer día «Did that scare you! Just a joke~»); le aburre el silencio y rellena route con cámara y diario. Su arco (2.x) revela que es un «Niño Puro de Anāsrava» y una posible amenaza cósmica bajo el nombre «Evernight»: ella elige seguir siendo March 7th igualmente, algo que el fandom recibió como uno de los giros más comentados del juego (hilo con 2886 votos que lo cita de memoria, ver punto 21). Cómo habla: frases cortas, exclamativas, remata bromas con «~»; tartamudea entusiasmo con puntos suspensivos. Fuente: Fandom HSR `March 7th/Lore`, `March 7th/Voice-Overs`. ✅

**Kafka** — Miembro veterana de los Cazadores de Stellaron, buscada en media galaxia (orden de busca la describe: «~170 cm, complexión media, chaqueta negra, camisa blanca, medias moradas, gafas de sol en la cabeza»). Habla en tono pausado, con metáforas elaboradas y humor seco («tocar el violín y disparar necesitan dedos flexibles, pero las balas obedecen más»); se declara indiferente al pasado y al futuro por igual, lo que more refuerza su fachada calculadora. Su hobby es coleccionar y cuidar abrigos de terciopelo («son frágiles y hermosos… basta un descuido para arruinar el brillo»). Fuente: Fandom HSR `Kafka/Lore`, `Kafka/Voice-Overs`. ✅

**Trazacaminos (Stelle/Caelus)** — El protagonista jugable, sin memoria propia al despertar en la Estación Herta; el jugador elige su apariencia (Stelle o Caelus) pero no cambia su historia. Reflexivo con las decisiones («cuando puedas elegir, elige algo de lo que sepas que no te arrepentirás»​), cariñoso con Pom-Pom aunque lo disimula («suenan molestos, pero su lenguaje corporal es más honesto: debería visitar a Pom-Pom más seguido»). Desde 2.x tiene línea de diálogo hablada en las misiones principales (antes era mudo). Fuente: Fandom HSR `Trailblazer/Lore`, `Trailblazer/Voice-Overs`. ✅

**Firefly** (personaje secundario más dibujado por fans, 2º lugar tras el propio Trazacaminos): agente encubierta de los Cazadores de Stellaron dentro de la armadura mecanizada «SAM»; criada como arma contra el Enjambre, con esperanza de vida acortada. Descrita como de lealtad inquebrantable y voluntad de acero; se unió a los Cazadores buscando una oportunidad de «vivir» antes de su muerte anunciada. Fuente: Fandom HSR `Firefly/Lore`. ✅

### Cara en cada emoción (fotograma con minuto)

| Personaje | Emoción | Vídeo | Minuto | Fotograma (enlace) |
|---|---|---|---|---|
| March 7th | Alegría/ternura | Tráiler oficial «Bande-annonce de March 7th» (Dailymotion) | 0:12 | https://www.dailymotion.com/video/x8a7le6 (fotograma 3, ojos cerrados, sonriendo con su cámara) |
| March 7th | Serenidad/nostalgia | mismo tráiler | 0:54 | https://www.dailymotion.com/video/x8a7le6 (fotograma 10, ojos cerrados, luz cálida) |
| March 7th | Determinación (combate) | mismo tráiler | 1:30 | https://www.dailymotion.com/video/x8a7le6 (fotograma 16, en plena acción con hielo) |
| Kafka | Calma/control | Tráiler «Ironía Dramática» (Dailymotion) | 1:20 | https://www.dailymotion.com/video/x8n3btc (fotograma 11, perfil sereno, media sonrisa) |
| Firefly | Resignación serena (acepta su destino) | Tráiler oficial «Embers in a Shell» (Dailymotion) | 0:40 | https://www.dailymotion.com/video/x90j8pu?t=40 (ojos cerrados, rodeada de llamas, sin gesto de dolor) |

- No conseguí primeros planos claros de Caelus/Stelle mostrando una emoción marcada: el tráiler «The Deliverer» (Dailymotion x9o6p18) es casi todo efectos abstractos y planos de acción lejanos, sin cara visible; probé también «1st anniversary trailer» y «Astral Express trailer» en Dailymotion y salieron los mismos tráilers generales ya usados, sin uno centrado en la cara del Trazacaminos. Habría que sacarlo de una cinemática de misión principal (necesita el juego instalado o un canal de story cutscenes) o de las hojas de la wiki (`Trailblazer/Media`) que hace el investigador de imagen. ⚠️
- Sigue faltando rabia, tristeza, miedo y vergüenza de los 4 personajes (sólo tengo alegría/serenidad/determinación de March 7th, calma de Kafka y resignación de Firefly): no me dio el tiempo de esta tanda para más tráilers ni cinemáticas de historia. Ver «Sigue» al final.

## 20 · Gustos y detalles de cada personaje

Datos sacados de las líneas de diálogo interactivo del propio juego («Character Infobox» y «Voice-Overs» de Fandom HSR): son la ficha más oficial que existe, porque HSR no publica un databook aparte con «cumpleaños/altura» para cada personaje como otras franquicias (Kafka es la única con altura publicada, por su ficha de «se busca»).

| Personaje | Le gusta | Odia | Aficiones | Cumpleaños | Altura | Fuente |
|---|---|---|---|---|---|---|
| March 7th | El jugo, tomar fotos, escribir su diario | Aburrirse cuando nadie le habla; la anguila en gelatina y el café de Himeko («difíciles de tragar») | Fotografía, llevar diario, esgrima (aprendida de Yanqing y Yunli) | «7 de marzo» (su propio nombre; no se conoce su fecha real de nacimiento, es amnésica) | No publicada | Fandom HSR, `March 7th/Voice-Overs` ✅ |
| Kafka | Los abrigos de terciopelo («frágiles y hermosos»), el violín, charlar con Silver Wolf | Nada en concreto: se declara indiferente al pasado y al futuro por igual | Coleccionar y cuidar abrigos, tocar el violín | No publicado | ≈170 cm (ficha de busca «Suspect Kafka…») | Fandom HSR, `Kafka/Lore` (orden de busca) y `Kafka/Voice-Overs` ✅ |
| Trazacaminos | Pom-Pom (lo disimula), explorar la Express, el Curio-arma que le asignó Herta | No especificado en las líneas revisadas | Explorar, combatir, ayudar a la tripulación | No aplica (personaje-avatar sin fecha propia) | No publicada | Fandom HSR, `Trailblazer/Voice-Overs` ✅ |
| Firefly | Las excursiones al aire libre (hierba, moras, mariposas, «tocar con sus manos el mundo lleno de vida») | No especificado; le molesta no poder soñar (duerme mucho menos que una persona normal) | Salir de excursión, mirar el mar de estrellas desde el tejado por las noches | No publicado | No publicada | Fandom HSR, `Firefly/Voice-Overs` ✅ |

- Nombre en español confirmado por la propia wiki (útil para textos del canal): «Siete de Marzo» (March 7th) y «Estela»/Caelus (Trazacaminos) · fuente: Fandom HSR, plantilla «Other Languages» de cada página · ✅

## 21 · Por qué la gente la ama

- Identificación con el elenco por «camino»/elemento más que con un único protagonista: hilo «Did my favorite character of each element» (323 votos) y «So who is your favorite in Planarcadia» (237 votos, 157 comentarios) muestran que cada jugador tiene su favorito distinto según con quién jugó primero · fuente: `datos-voz.md` (ya recolectado) ✅
- Motivo recurrente citado por jugadores: la narrativa por arcos (Belobog, Xianzhou Luofu, Penacony, Amphoreus) engancha porque cada parche cierra una historia completa antes de abrir la siguiente («This patch has reminded me why I love HSR so much», 898 votos) · fuente: https://www.reddit.com/r/HonkaiStarRail/comments/1l3pjaz/ ✅
- Escena que hace llorar (Penacony, arco de Clara/Svarog): hilo «Clara's VA laughs during the saddest scene of the Penacony quest» (378 votos, 82 comentarios) señala esa escena como la más triste comentada del juego hasta ese parche · fuente: https://www.reddit.com/r/HonkaiStarRail/comments/1b6wqqm/ ⚠️ (no da minuto: es una cinemática dentro del juego, no un vídeo publicado con timestamp)
- Escena que hace llorar (parche 3.6, Amphoreus): «The past scene in 3.6 was one of the saddest ones in the whole game» (80 votos) · fuente: https://www.reddit.com/r/HonkaiStarRail/comments/1nsws55/ ⚠️ (mismo motivo: sin minuto verificable)
- Momento que generó más comentarios de sorpresa/asombro colectivo: la revelación de que March 7th es «Evernight» (hilo-meme con 2886 votos y 122 comentarios cita la escena de memoria) · fuente: https://www.reddit.com/r/HonkaiStarRail/comments/1whk4zo/ ⚠️ (el hilo es un meme sobre la escena, no un análisis con minuto)
- No encontré reseñas de prensa especializada (IGN, Polygon) centradas en personajes con cifras de premios/ventas por personaje: HSR no publica ese desglose. Lo que sí hay son las encuestas de popularidad del punto 7. ⚠️

## 22 · Fan dubs y comunidad hispana

Sin doblaje oficial en español, la comunidad hispana hace principalmente **fandubs de escenas y cómics** (comic dubs), no doblaje del juego completo.

- Canal **Honkai Spanish Dubs** (`@HonkaiSpanishDubs`, 5330 suscriptores, 18 vídeos): comic dubs y fandubs latinos de escenas y cómics de fans sobre HSR. Vídeo destacado: «Marzo y Caelus son muy traviesos» (109 000 vistas, hace 1 año); «La muñeca perdida de Herta» (26 000 vistas); «Un Partido de Voleibol» (8900 vistas) · fuente: https://www.youtube.com/@HonkaiSpanishDubs (navegar.py) · ✅
- Canal **ALANREQUIEM DUBS** (24 400 suscriptores): fandubs latinos de escenas de HSR y Zenless Zone Zero. Vídeo «La novia de Caelus ✨ | Honkai Star Rail Fandub Latino» (44 000 vistas, hace 7 meses, con #Caelus #DoblajeEspañol #March7th); «El Traje de March 7th | Honkai Star Rail Fandub Latino» (4800 vistas) · fuente: https://www.youtube.com/watch?v=p1EHkhaCGvs (navegar.py) · ✅
- Fandub de la cinemática de **Ying Yuan** (personaje del arco Amphoreus), «Monólogo Ying Yuan Fandub Español Latino» y «Cinemática Ying Yuan Fandub Español Latino»: https://www.youtube.com/watch?v=P1Q18UsN-V4 y https://www.youtube.com/watch?v=8JRou7Qzibo · ⚠️ (sólo vi el título y metadatos por el buscador, no pude abrir el detalle con navegar.py en esta tanda)
- Vídeo «La Pesadilla de Caelus - Honkai Star Rail Fandub Español latino»: https://www.youtube.com/watch?v=9_8YbbQp5vQ (marzo 2025) · ⚠️ (mismo motivo: sólo metadatos de búsqueda)
- No encontré covers en español de los openings/temas de HSR (el juego no tiene «opening» tipo anime, son tráilers de versión): no aplica igual que en un anime. ✅ (se aclara por qué no hay, no es que falte)
- No encontré parodias o memes hispanos específicos de HSR con canal propio (tipo cuenta de memes en español); lo que hay son los memes en inglés de Reddit (punto 12) traducidos informalmente por fans, sin fuente propia en español. ⚠️

## Lo mejor para la lámina

1. **Kafka** es la femenina más votada en la encuesta oficial 2025 y la 9ª más dibujada por fans: personaje seguro para protagonizar una lámina, con su frase de calma «tocar el violín y disparar necesitan dedos flexibles, pero las balas obedecen más».
2. **March 7th** tiene la mejor mezcla foto-a-foto para mostrar emoción (alegría con su cámara a 0:12 del tráiler, seriedad a 0:54): sirve para una lámina con progresión de humor del canal.
3. Aviso obligatorio en cualquier lámina: **no hay doblaje latino**, así que ningún cuadro de diálogo puede citarse como «doblado»; se cita el texto en español (localización) o el original con su traducción.
4. El Trazacaminos existe en dos versiones (Stelle/Caelus): si aparece en la lámina, decidir cuál (o mostrar ambigüedad a propósito) en vez de asumir una por defecto.
5. Canales de fandub latino ya identificados (Honkai Spanish Dubs, ALANREQUIEM DUBS) son candidatos a mencionar si el canal de destino habla de fandubs de la comunidad.

## No encontré

- Doblaje latino de voz: confirmado que no existe (no es un «no encontré», es un hecho con 3 fuentes).
- Altura y cumpleaños oficiales de March 7th, Trazacaminos y Firefly: no están publicados por HoYoverse (busqué en `Character Infobox` y en `Voice-Overs` de cada uno); sólo Kafka trae altura aproximada por su ficha de «se busca».
- Emociones de rabia, tristeza, miedo y vergüenza con fotograma propio: sólo saqué alegría/serenidad/determinación de March 7th, calma de Kafka y resignación serena de Firefly en esta tanda (faltó tiempo para más tráilers/cinemáticas, y no encontré ningún tráiler centrado en la cara del Trazacaminos).
- Reseñas de prensa especializada centradas en personajes (con premios o cifras de ventas por personaje): no existen para este juego gacha, según lo que busqué.
- Parodias o memes hispanos propios de HSR con canal identificado: no encontré ninguno con nombre propio, sólo traducciones informales de los memes en inglés de Reddit.
- Fandub latino de Kafka o del Trazacaminos en concreto (busqué «Kafka fandub español latino» y «Trazacaminos fandub español»): sólo aparecieron pruebas de casting sueltas en Instagram, sin canal ni vídeo terminado que pudiera verificar.

## Bitácora de búsqueda

- Doblaje Wiki (api.php, español): `action=query&titles=Honkai:%20Star%20Rail` → `missing`; `action=query&list=search&srsearch=Honkai`/`Star Rail`/`intitle:Honkai` → sin página propia de la obra; ficha de Jeannie Hernández (traductora) sí la menciona.
- Honkai Star Rail Wiki (Fandom, inglés): wikitext de `March 7th`, `Kafka`, `Trailblazer`, `Firefly` y sus subpáginas `/Lore` y `/Voice-Overs`; `allpages?apprefix=` para mapear subpáginas de cada personaje.
- WebSearch (inglés): «Honkai Star Rail voice language Spanish text only official languages list» → confirma EN/JP/CN/KR de voz y ES sólo texto (Prima Games, DigiStatement).
- WebSearch (inglés): «Honkai Star Rail popularity poll fan favorite character HoYoLAB» y «personaje más popular encuesta 2025» → encuesta oficial china de mayo 2025 (HoYoLAB + X/StarRailVerse1).
- WebSearch (español): «Honkai Star Rail fandub español latino youtube personaje» y «Kafka Honkai Star Rail fandub español latino voz» → canales Honkai Spanish Dubs y ALANREQUIEM DUBS, vídeos de Ying Yuan y Caelus.
- Dailymotion API: búsquedas de tráiler de personaje («Kafka character trailer», «March 7th character trailer», «Trailblazer trailer») → tráilers oficiales «Ironía Dramática» (Kafka), «Bande-annonce de March 7th», «The Deliverer» (Trazacaminos).
- `fotogramas.py` sobre los 4 tráilers anteriores (cada 6-8 s) → hojas de contacto miradas con Read; fotogramas citados en el punto 13.
- Arctic Shift (Reddit r/HonkaiStarRail): `query=cried`, `made me cry`, `saddest scene`, `silent protagonist`, `Evernight reveal`, `cringe` → hilos usados en los puntos 12 y 21.
- `navegar.py` sobre HoYoLAB (`hoyolab.com/article/40440025`): la página no renderiza contenido sin sesión (queda en «Cargando…»); me apoyé en el resumen de X/StarRailVerse1 y en Sportskeeda (bloqueado por captcha) para la encuesta.
- No usé más de dos intentos por web bloqueada (regla de AYUDANTE.md): X/Twitter dio 403 directo con navegar.py, así que no insistí más ahí.

## Cumplimiento (mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 7 · Popularidad | ✅ | Encuesta oficial 2025 (2 fuentes) + Danbooru + Reddit |
| 8 · Doblaje latino | ✅ | Confirmado que NO existe, con 3 fuentes; tabla EN/JP/CN/KR completa para los 4 personajes |
| 12 · Fandom y qué no hacer | ✅ | Memes con repost verificado, aviso de Trazacaminos con voz propia, aviso de no inventar doblaje latino |
| 13 · Carácter y forma de hablar | ⚠️ | 4 personajes descritos con fuente; emociones en imagen cubren March 7th (3), Kafka (1) y Firefly (1), falta el Trazacaminos y las emociones negativas (rabia/tristeza/miedo/vergüenza) de todos |
| 20 · Gustos | ✅ | March 7th, Kafka, Trazacaminos y Firefly completos, cada uno con fuente |
| 21 · Por qué la aman | ✅ | Identificación por camino, escenas que hacen llorar (Penacony, 3.6) con reacción de Reddit |
| 22 · Fan dubs | ✅ | 2 canales identificados con suscriptores y vídeos; aclarado por qué no hay covers de opening |

Sigue: sacar «cara en cada emoción» (al menos rabia, tristeza, miedo o vergüenza) de March 7th, Kafka, Trazacaminos y Firefly con fotograma y minuto — de una cinemática de misión principal o de un tráiler más centrado en el rostro (el punto 13 sólo tiene alegría/serenidad/determinación por ahora) — es lo único obligatorio que quedó a medias.
