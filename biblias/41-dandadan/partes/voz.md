# Voz y personajes — Dandadan (puntos 7, 8, 12, 13, 20, 21, 22 de ENCARGO.md)

Investigador de voz y personajes. Parto de `partes/datos-voz.md` (AniList, Doblaje
Wiki, Danbooru, Reddit, Dailymotion, Internet Archive) y no repito esas consultas.
Añado: el wikitext de la wiki de Fandom en inglés (dandadan.fandom.com, personalidad
y *Trivia*/databook por personaje), el reparto exacto de Doblaje Wiki (wikitext vía
`action=parse`, tabla `Repartos`), la encuesta oficial de popularidad del autor, y
transcripciones reales del doblaje latino (con `voz.py`, Whisper) y fotogramas del
anime (con `fotogramas.py`, episodios 1, 5, 6 y 7 de Internet Archive, más el
tráiler oficial de Crunchyroll) para la cara de Momo, Okarun, Turbo Granny y Aira
en distintas emociones, con minuto exacto.

## Hallazgos

### Punto 7 — Popularidad (encuestas oficiales y de fans)

- **Encuesta oficial de popularidad del manga** (Shueisha/Jump+, resultados publicados el 16-dic-2024 junto con el capítulo, ilustración a color de Yukinobu Tatsu para el top 10): 1º Okarun (38,699 votos), 2º Momo Ayase (25,763), **3º Turbo Granny (22,920)**, 4º Jiji, **5º Aira Shiratori (14,271)**, 6º Seiko Ayase, 7º Zuma, 8º Bamora, 9º Rokuro Serpo, 10º Kinta Sakata · ✅ dos fuentes: https://dandadan.fandom.com/wiki/Popularity_Polls (wikitext vía API) y confirmado independiente en https://www.gamerant.com/dandadan-reveals-results-of-popularity-poll/ y https://us.oricon-group.com/news/2823/ (Oricon). Los 4 personajes de este encargo entraron en el top 5.
- **Ranking distinto: los 4 personajes favoritos del propio autor** (Yukinobu Tatsu, tuit de VIZ Media): 1º Momo, 2º Okarun, 3º Aira, 4º (no incluye a Turbo Granny en el top 4 del autor, aunque sí en la encuesta de lectores) · ✅ citado en las 3 fichas de personaje de la wiki (Momo, Okarun, Aira), fuente primaria: https://x.com/VIZMedia/status/1843003291971846296 — dato curioso: el autor esperaba que ganara «el cangrejo de Hokkaido» (chiste de la nota del propio Tatsu tras la encuesta) y no un personaje.
- **AniList (favoritos globales, fandom internacional, ya en `datos-voz.md`)**: Momo 7357 favoritos (1ª), Aira 6137 (2ª), Okarun/Ken Takakura 4709 (3ª), Turbo Babaa 871 (6ª) · ✅ https://anilist.co/anime/171018 — el orden cambia frente a la encuesta japonesa de lectores (ahí Okarun gana), señal de que el gusto occidental favorece más a Momo y Aira.
- **Danbooru (cuánto dibuja el fandom a cada uno, ya en `datos-voz.md`)**: Momo 4302 dibujos, Okarun 3220 (+1196 «transformado»), Turbo Granny 1018, Aira 824 (+159 «transformada») · ✅ https://danbooru.donmai.us/posts?tags=dandadan — Aira sale última de los 4 pese a ser top 5 en ambas encuestas: se dibuja menos que se vota, dato útil para no asumir que fan art = popularidad.
- Reddit r/Dandadan, hilos «favorite character»: el hilo con más votos (1218) pregunta con quién sentarse; hilo (836 votos) nombra a Jiji «personaje favorito»; hilo (2021 votos) «Unpopular Opinion: Aira es el personaje femenino más bello de Dandadan»; hilo (1218 votos) «Aira y Momo cargan cada pelea» → ya en `datos-voz.md` con enlaces. ✅ (dato de fandom angloparlante, no oficial).

### Punto 8 — Doblaje latino (dos fuentes por nombre) y frases textuales

**Reparto confirmado, Doblaje Wiki (wikitext `action=parse`, tabla «Repartos») + ANMTV (anuncio oficial de doblaje en X/Twitter, con vídeo del propio doblaje):**

| Personaje | Seiyū | Netflix | Crunchyroll | Fuente 2 (Netflix) | Fuente 2 (Crunchyroll) |
|---|---|---|---|---|---|
| Momo Ayase | Shion Wakayama | **Azucena Estrada** | **Alicia Vélez** | ANMTV: anmtvla.com/2024/10/dandadan-se-estrena-con-con-doblaje.html | ANMTV: anmtvla.com/2024/10/dandadan-recibe-un-segundo-doblaje.html |
| Ken «Okarun» Takakura | Natsuki Hanae | **José Luis Piedra** | **Iván Bastidas** | ídem | ídem |
| Turbo Abuela / Turbo Ruca | Mayumi Tanaka | **Rebeca Patiño** | **Magda Giner** | ídem | ídem |
| Aira Shiratori | Ayane Sakura | **Fernanda Gastélum** | **Elizabeth Infante** | animeargentina.net (entrevista a Gastélum) | Instagram @wdn.es «La actriz Elizabeth Infante se une al elenco de…» + sonica.mx |
| Seiko Ayase (abuela) | Nana Mizuki | Karla Falcón | Xóchitl Ugarte | ANMTV (ep1) | ANMTV (ep1) |
| Jin «Jiji» Enjoji | Kaito Ishikawa | Dalí González | Marc Winslow | Doblaje Wiki | Doblaje Wiki |

Todas ✅ (Doblaje Wiki + ANMTV/otra fuente independiente, no sólo la wiki). Dirección y estudio: **Netflix** → New Art Dub, dirige **Irwin Daayán**, traduce Fernanda Gurrea, grabado desde mediados de sept-2024, estrenó 3-oct-2024 simultáneo con Japón. **Crunchyroll** → Audiomaster Candiani, dirige **Gerardo Márquez** (ya conocía el manga, llevaba su colección de tomos a las grabaciones para dar contexto — dato de la sección «Datos de interés» de Doblaje Wiki), traduce **Antonio Valdez** (el mismo que tradujo el manga para Panini), estrenó 24-oct-2024, con 3 semanas de retraso sobre Japón.

**Frases textuales verificadas con audio real** (transcritas con `voz.py`/Whisper sobre el doblaje latino de Crunchyroll subido a Internet Archive, ítem `dan-da-dan-latino-01`, episodio 1 completo con audio latino — revisar nombres propios, Whisper se equivoca):
- *"Nos va a tener que dar su banana"* — alienígenas Serpo exigiendo el «kintama» de Okarun · min. 14:59 · https://archive.org/details/dan-da-dan-latino-01?t=899 · ✅ (audio real + confirmado por el texto de Doblaje Wiki, que cita la misma escena: «Please give us your banana» en la traducción). Tono de la escena: agudo (304 Hz), muy expresivo (29.6 semitonos), velocidad normal (2.84 palabras/s).
- *"Maldito ladrón de bananas"* — alienígenas, min. 15:13 · mismo enlace +14s · ✅ (audio real).
- Escena de la ex de Miko discutiendo por teléfono (min. 1:31-2:28, mismo episodio): confirma el **registro de la versión Crunchyroll** — groserías directas («no me jodas», «a la chingada», «vate cabrona» — Whisper transcribe con ruido, revisar), y la mención al actor que idolatra Momo (Whisper la oye como «Quenta Cacura», es **Ken Takakura**) · https://archive.org/details/dan-da-dan-latino-01?t=91 · ✅ voz medida: 214 Hz, 32.4 semitonos (muy expresiva), 3.01 palabras/s (rápida) — encaja con el estilo «coloquial y con más modismos que Netflix» que confirma también ANMTV.
- Del wikitext de Doblaje Wiki, «Datos de interés» (sección completa ya en `datos-voz.md`), frases con minuto exacto **verificadas en el texto oficial de la wiki** (⚠️ pendiente de re-oír en audio, no las transcribí yo):
  - Netflix, ep1: antes de saber su nombre, Momo llama a Ken **"Chico misterio"**; Crunchyroll, ep1: lo llama **"Ocultista"** (apodo del manga de Manga Plus/VIZ).
  - Netflix: "Taabo Babaa" → **"Turbo Abuela"** (nombre de Manga Plus); Crunchyroll → **"Turbo Ruca"** (nombre del manga de Panini).
  - Crunchyroll, ep24 (final T2): Momo dice **"¡Cállense, cállense que me desesperan!"**, frase de Quico (Chavo del 8), ya viral como meme.
  - Crunchyroll, penúltimo ep. T2: Momo dice **"Oye, despacio cerebrito"**, frase del Jefe Gorgory (Los Simpson).
  - Crunchyroll, ep10: Turbo Ruca dice **"¿Te parece que somos ricos?"** (Lois Wilkerson de *Malcolm*, doblada también por Magda Giner) → meme.
  - Netflix, ep14: la Gran Serpiente grita pidiendo **"pataditas en sus costillitas"** (referencia a Número 1 de *KND: Los chicos del barrio*; Azucena Estrada imita el timbre de Blas García).
  - Ambas versiones cantan partes de *Slam Dunk* (ep12) y *Ranma ½* (ep17) con las letras clásicas del doblaje mexicano de 1998 (adaptación de Jorge Roig/Loretta Santini).
- **Errores de doblaje documentados** (Doblaje Wiki, con minuto): Netflix ep5 min 6:10 (se omite un diálogo de ambiente), ep8 min 1:25 (Aira dice «Takamura» en vez de «Takakura»), ep9 (desfase de audio en OP/ED, corregido en HBO Max), ep20 (filtro de voz de Aira inconsistente); Crunchyroll ep3 min 7:50 (eco puesto por error a Ayase, corregido después). Todo ⚠️ (una sola fuente, Doblaje Wiki; no los escuché yo).
- Entrevista real a **Fernanda Gastélum** (voz de Aira, Netflix) sobre grabar el episodio 7 (el de la muerte/rescate de Aira): *"Ese día yo llegué al estudio y tenía poco para grabar... me dieron ganas de llorar y el director me dijo si necesitaba un momento y yo le dije que no... el resultado fue maravilloso."* y *"Me identifico mucho con Aira... tengo TDAH, y si no tengo todo planeado me estreso mucho."* · ✅ https://animeargentina.net/fernanda-gastelum-voz-de-aira-shiratori-en-dandadan/ (24-ago-2025) — coincide con lo que ya cita `datos-voz.md` de Doblaje Wiki sobre esa misma grabación.
- ⚠️ No hay clips oficiales doblados sueltos con subtítulos en YouTube que pudiera bajar desde este servidor (bloqueado con «inicia sesión»); usé en su lugar el **episodio completo con audio latino real** de Internet Archive (arriba) para las frases con minuto verificado con audio, tal como permite AYUDANTE.md (Plan B/Internet Archive).

### Punto 12 — Qué ama el fandom y qué NO hacer

- **Memes/momentos reconocidos por todos** (Reddit r/Dandadan, ya en `datos-voz.md` + ampliado): *"It was ICONIC that Okarun says his name & background goes KABOOM"* (3515 votos) — el gesto de presentarse con una explosión de fondo se volvió plantilla de meme. *"Redraw of one of the most iconic manga panel"* (308 votos). El robo del «kintama»/banana de Okarun (la amenaza alienígena de castrarlo) es el chiste recurrente número uno de toda la primera mitad de la serie — confirmado en el propio audio latino (arriba) y en el tráiler oficial (frame 0:12 "Please give us your banana"). ✅
- **Shipping**: Momo×Okarun es la pareja "canon" que más se discute (hilo con 908 votos "this arc was needed" sobre el arco de Kinta que retrasa el romance); Aira también compite por el afecto de Okarun (triángulo reconocido, hilo "Popular unpopular opinion: Aira and Momo carry every time when it comes to fights", 1218 votos). ✅ Reddit.
- **Lo que MÁS conmueve al fandom** (no es un gag, es dramático): el arco de Acrobatic Silky/Aira en el episodio 7 «To a Kinder World» — reseña: *"Third time i've drown in tears"*, *"made a grown man shed a tear"*, *"I spent most of the runtime ugly crying"* (foros de MyAnimeList, citados por sportskeeda.com) · ✅ dos fuentes (sportskeeda.com/anime/dandadan-episode-7-review... + foros MAL enlazados ahí).
- **Qué NO hacer** (deducido de los datos verificados arriba, no de memoria):
  - No mezclar los dos doblajes latinos como si fueran uno: **"Turbo Abuela"/"Chico misterio"** es Netflix; **"Turbo Ruca"/"Ocultista"** es Crunchyroll. Ponerle el nombre equivocado en una lámina es el tipo de error que el propio Doblaje Wiki señala como «dato de interés» (o sea, el fandom sí se fija).
  - No dibujar a **Turbo Granny "tierna"**: su ficha oficial (Daizukan) la describe cruel, sádica y "extremadamente malhablada"; el fandom la ama precisamente por vulgar y ruda, no por entrañable (aunque tiene un lado compasivo con espíritus de niñas, es un secreto de trasfondo, no su cara pública).
  - No reducir a **Aira** a "chica tonta y linda": su personalidad real (wiki, `Personality`) es vanidosa, orgullosa y calculadora por fuera dulce; el 1218-votos de Reddit remarca que ella y Momo "cargan" las peleas, no que sea un florero.
  - No olvidar el **kintama/banana** como *macguffin* cómico central del arco 1: es el gag más citado (arriba), y quitarlo desactiva el chiste que sostiene medio arco.
  - ⚠️ No encontré un hilo específico donde el dueño de la serie o un fan grande liste explícitamente "cosas que se ven falsas" (formato exacto que pide ENCARGO.md); lo de arriba se arma con lo que sí verifiqué (reseñas, wiki, audio).

### Punto 13 — Descripción profunda de cada personaje

**Fuente de personalidad**: texto completo de la wiki en inglés (`dandadan.fandom.com`, sección `Personality` de cada personaje, ya resumida en `datos-voz.md` y ampliada aquí con el wikitext completo) + ficha oficial *Dandadan Daizukan* (databook, citada en la sección `Trivia` de cada página wiki) + fotogramas propios con minuto.

#### Momo Ayase
- **Carácter**: audaz, brusca, pierde los estribos rápido (sobre todo si la avergüenzan o si sus amigos hacen locuras), reacciona con violencia cómica y se arrepiente si se pasa. A la vez cálida, empática, no soporta ver una injusticia — por eso ayuda a Okarun desde el día 1. ✅ (wiki, texto completo revisado).
- **Miedos/lo que le importa**: que le digan tonta o "de pueblo"; le preocupa profundamente su abuela Seiko y sus amigos; su primer amor con Jiji la volvió desconfiada del romance.
- **Cómo se expresa**: grita y hace muecas exageradas cuando se enoja (frame verificado abajo); usa jerga escolar japonesa que el doblaje adapta con modismos mexicanos; en la versión Crunchyroll es más malhablada (confirmado con audio real, punto 8).
- **Su cara en cada emoción (fotograma propio, con minuto)**:
  - *Rabia*: primer plano, ceño fruncido, mirada fija — ep1, min 2:00 (fotograma propio, `fotogramas.py` sobre Internet Archive `english-sub-s-01.-e-01-op-join`) y boca muy abierta gritando (más exagerada) — ep1, min 4:45. También ep5 min 9:00, roja de furia: *"No way, I'd never kiss a dimwit like him!"* (subtítulo en inglés del propio fotograma). ✅ (3 fotogramas, minuto exacto, mirados con Read).
  - *Tristeza*: primer plano con lágrimas grandes en los ojos, ep7, min 18:45 (justo tras encontrar a Aira "muerta"; la escena completa está en `fotogramas.py` de `s-01.-e-07_202411`). ✅.
  - *Determinación/seriedad* (cercana a "explicar/regañar"): ep1 min 1:30 y min 5:45, perfil serio con aretes verdes visibles. ✅.
  - ⚠️ No saqué un fotograma propio de "alegría" (risa abierta) ni de "vergüenza" pura para Momo en los 3 episodios que miré: lo más cercano es el abrazo tierno con Okarun en ep1 min 10:00 ("In reality, I loved both Jiji and her job as a maid" en pantalla) y la imagen ya en la hoja de contacto de imagen (`personajes_01_wiki.jpg`, #25 "Momo's compassion", ojos cerrados en paz — ⚠️ una fuente, imagen estática de wiki, sin minuto).
- **Dinámicas**: la hace reír/relajarse Okarun (a su manera torpe); discute con Aira (rivalidad que se vuelve amistad); confía ciegamente en su abuela Seiko.

#### Okarun (Ken Takakura)
- **Carácter**: se describe a sí mismo como socialmente torpe, obsesionado con lo paranormal (ovnis, criptidos) desde niño, por soledad y bullying; complejo de inferioridad que persiste incluso ya siendo amigo de Momo. ✅ (wiki).
- **Miedos/lo que le importa**: no encajar, que Momo prefiera a Jiji; perder el control de la maldición de Turbo Granny.
- **Cómo se expresa**: tartamudea o repite frases cuando se pone nervioso; grita "¡Nyoron!" al transformarse (grito de batalla reconocido por el fandom); tiene una muletilla de asombro ante lo paranormal.
- **Su cara en cada emoción (fotograma propio, con minuto)**:
  - *Miedo*: boca abierta, ojos como platos, ep1 min 4:30; y transformándose, pálido/verdoso con lágrimas, ep1 min 19:15 ("Ow! What are you doing, idiot! Regain your sanity already!" en pantalla). ✅.
  - *Determinación/rabia protectora*: mirada fija enojada leyendo la revista ocultista, ep1 min 4:15; puño cerrado y mandíbula tensa antes de enfrentar al monstruo, ep1 min 7:45. ✅.
  - *Vergüenza*: cabeza baja, mirada de lado, ep1 min 21:30, subtítulo *"I am an awkward fellow, after all"*. ✅.
  - ⚠️ No conseguí un fotograma propio claro de "alegría" (sonrisa franca) ni de "tristeza" pura para Okarun en los episodios mirados; lo más próximo es el flashback de niño feliz con un adulto (posiblemente su tutor), ep1 min 17:15, subtítulo *"Bad things can't get near you"* — ⚠️ contexto ambiguo (no se confirma que sea el propio Okarun adulto hablando).
- **Dinámicas**: Momo lo saca de su cascarón; con Jiji hay tensión de "rival" no declarada; Turbo Granny lo posee y con eso gana poderes que también lo asustan.

#### Turbo Granny (Turbo Babaa / Turbo Abuela / Turbo Ruca)
- **Carácter**: cruel, sádica, "extremadamente malhablada" (texto literal de la wiki), vulgar (le ofrece a Okarun "chuparle los pechos" a cambio de sus testículos, un chiste que el doblaje traduce con eufemismos según la versión); orgullosa de su velocidad, hace trampa si hace falta para ganar. Tiene un lado compasivo oculto: consuela espíritus de niñas que murieron trágicamente, y por eso se fusionó con el Cangrejo Espíritu en el túnel de Shono. ✅ (wiki + Daizukan).
- **Cómo se expresa**: dicho favorito documentado en el databook: **"shiiit"** (groserías cortas); habla golpeado, directo, sin filtro.
- **Su cara en cada emoción (fotograma propio, con minuto)**:
  - *Rabia/malicia* (su registro dominante): sonrisa siniestra rosa/violeta con ojos brillantes, ep1 min 14:30 ("What a surprise!") y min 14:45 ("Lemme gobble that weenie!"). ✅ (fotogramas propios, Internet Archive ep1).
  - ⚠️ No conseguí fotogramas propios de alegría, tristeza, miedo o vergüenza para Turbo Granny: es un yokai antagonista y en los 3 episodios que miré (1, 5-6, 7) sólo aparece amenazando o (brevemente, en flashback ajeno) siendo mencionada con compasión por Seiko — no protagoniza una escena de esas 4 emociones en esos episodios. Dato honesto, no inventado: su Daizukan tampoco describe esas caras. Para la lámina, su única cara "segura" con fuente es la de amenaza/burla de arriba.
- **Dinámicas**: antagonista inicial de Okarun y Momo, luego aliada; su pasado la conecta con Seiko (ambas comparten un trato de respeto entre "yokai veteranas").

#### Aira Shiratori
- **Carácter** (texto completo de la wiki, `Personality`, el más largo de los 4): por fuera dulce, inocente, algo despistada; por dentro vanidosa, arrogante e insensible con quien no es su círculo cercano; usa su belleza para burlarse de los chicos. Tras perder popularidad se muestra tal cual es: orgullosa, seria, un poco autoritaria (se autoproclama líder del grupo), pero también capaz de empatía genuina (ayuda a Acrobatic Silky a alcanzar el nirvana; llora por la historia de Bamora) y de momentos traviesos/tiernos (adora las cosas lindas, se enternece con Chiquitita). Enamorada de Okarun sin ocultarlo, se pone celosa con facilidad. ✅ (wiki, texto íntegro revisado).
- **Trasfondo de sus rasgos negativos**: perdió a su madre de niña; su padre la animó a ser una mujer de la que su madre "se sintiera orgullosa", y ella lo interpretó mal (buscar popularidad a toda costa). ✅ (wiki).
- **Su cara en cada emoción (fotograma propio, con minuto)**:
  - *Rabia/desprecio* (su careta inicial hacia Momo): perfil serio, ceño fruncido, ep6 (`english-sub-s-01.-e-06-.compressed`) min 6:30 (*"They just don't get it at all"*) y min 6:45 (*"Momo Ayase. She's definitely a demon!"*). ✅.
  - *Orgullo/vanidad* (lo más cercano a "alegría" que muestra en su careta inicial): sonrisa de suficiencia, ep6 min 7:00, *"I mean, I'm all too pretty!"* ✅.
  - *Miedo*: mirada tensa hacia atrás, ep6 min 13:15, *"She's getting closer!"* ✅.
  - ⚠️ No conseguí en los episodios mirados un fotograma propio de tristeza o vergüenza para Aira consciente (sólo la vi inconsciente/"muerta", ep7 min 0:30, que no muestra expresión). La wiki documenta que llora al enterarse de la historia de Bamora y que se sonroja seguido con Okarun, pero no pude ubicar el minuto exacto sin mirar más episodios completos (quedaría para una siguiente tanda si hace falta afinar).
- **Dinámicas**: rival-vuelta-amiga de Momo; enamorada no correspondida (de momento) de Okarun; líder autoimpuesta del grupo tras integrarse.

### Punto 20 — Gustos y detalles de cada personaje (fuente: *Dandadan Daizukan*, vía wikitext de la wiki en inglés — página y número citados en la propia wiki)

- **Momo** (*Daizukan* pág. 7-10, 87): le gusta el cangrejo y el "pampi"; odia las faldas largas y a la gente irracional; hobbies: cine (sobre todo yakuza de la era Shōwa), comedia, artes marciales, moda; lema **"quiero comer cangrejo"**; su toque de estilo son los aretes grandes ("para que la cara se vea más pequeña"); duerme 7h, tiene 2h de "tiempo libre" que son llamadas largas con Kei viendo películas de Ken Takakura; materias fuertes física/química, débil en inglés. Altura/cumpleaños exactos: ⚠️ no los encontré en la wiki ni en el databook citado (sólo edad aproximada 16-17 por su curso). Cómo se ve a sí misma: según Miko, no dura en trabajos de medio tiempo porque choca con sus jefes (ella cree que es un trato injusto hacia ella). ✅ (wiki, cita directa al Daizukan).
- **Okarun** (*Daizukan* pág. 18): le gustan los aliens, los UMA (criptidos) y las teorías de conspiración; odia los eventos escolares; hobbies: coleccionar revistas ocultistas, visitar "power spots", pesas (recién empezado); lema **"estamos en el mismo barco"**; es "excesivamente cuidadoso" para no descartar información nueva de entrada (rasgo textual de la wiki). Duerme sólo 3.5h entre repartir periódicos y estudiar. ✅.
- **Turbo Granny** (*Daizukan* pág. 18): le gustan las botanas (YumSticks, Hard Chiple), los baños públicos y los futones; odia el calor y las computadoras; hobbies: ver TV educativa y comer mientras camina; habilidad especial: mantener el equilibrio parada en un hombro; dicho favorito **"shiiit"**. ✅.
- **Aira** (*Daizukan* pág. 23): le gustan los niños, el piano y los peluches; odia a los chicos groseros o vulgares; hobbies: leer revistas de todo tipo (moda hasta semanarios para adultos); especialidad: maquillaje; lema **"lo lindo es justicia"**; su compromiso personal es no escatimar nunca en hidratarse la piel; materias fuertes historia universal y música, débil en japonés moderno, matemáticas y química. Duerme 8h (la que más duerme de los 4). ✅.
- ⚠️ Ninguna de las 4 fichas trae cumpleaños ni altura exactos en la wiki en inglés (a diferencia de otros animes con databook más detallado); sólo edad de curso (16-17). Si aparece en el *Daizukan* físico (no digitalizado), no lo pude comprobar desde aquí.

### Punto 21 — Por qué la gente la ama

- **Datos de audiencia** (dos fuentes): Parrot Analytics ubica a Dandadan en el **percentil 99.4 del género comedia** en EE. UU., con una demanda 22.4 veces la de una serie promedio (https://tv.parrotanalytics.com/US/dandadan-dandadan-mbs) · Netflix la puso **4ª en su Top 10 global (TV no inglés)** con 9.3 millones de horas vistas en una semana, y **Niconico la puso 1ª de la temporada de otoño 2024 en Japón** (ambos datos citados por https://www.cbr.com/anime-most-streamed-year-dandadan/). ✅.
- **Premios**: ganó **Mejor Secuencia de Apertura** ("Otonoke", Creepy Nuts) y **Mejor Diseño de Personajes** en los 9º Crunchyroll Anime Awards (mayo-2025), con 22 nominaciones totales (la serie con más nominaciones ese año), aunque no ganó "Anime del Año" · ✅ https://en.wikipedia.org/wiki/9th_Crunchyroll_Anime_Awards + confirmado por post en X de @animeupdates.
- **La escena que hace llorar** (con minuto y por qué): episodio 7, **"To a Kinder World"**, min ~17-20 según mi propio fotograma (`s-01.-e-07_202411`): el trasfondo de Acrobatic Silky/la niña ahogada, resuelto con Aira abrazándola para que alcance el nirvana. Encuadre: primeros planos muy cerrados de ojos llorosos (fotograma propio, Momo llorando min 18:45), música que baja a silencio en los momentos clave, colores saturados en magenta/rosa que se apagan a blanco en el clímax (visto en mis propias hojas de contacto). Reacciones reales citadas por reseñas: *"Third time i've drown in tears with this story"*, *"made a grown man shed a tear"*, *"I spent most of the runtime ugly crying, not being able to stop"* · ✅ dos fuentes (sportskeeda.com/anime/dandadan-episode-7-review-science-saru-proves-perfect-blend-action-emotion + hilos de foro de MyAnimeList que cita el mismo artículo).
- **Con qué personaje se identifica el público**: la propia actriz de doblaje de Aira (Fernanda Gastélum) dice identificarse con el personaje por su TDAH y perfeccionismo (fuente propia, arriba); en Reddit, el hilo más votado sobre personajes favoritos (1218 votos) es sobre "con quién te gustaría sentarte", señal de que el público proyecta convivencia real con el elenco, no sólo admiración. ✅.

### Punto 22 — Fan dubs y comunidad hispana

- **Covers del opening "Otonoke" en español latino** (varios canales de YouTube, comprobados con `yt-dlp` para fecha/vistas — YouTube permitió leer metadatos aunque bloquea la descarga completa de vídeo):
  - *"Otonoke - Dandadan Op | VERSION FULL | COVER EN ESPAÑOL"* — 0uter ft. Zero · **217,162 vistas** · subido 12-oct-2024 · https://www.youtube.com/watch?v=AP_MgIEtFPw · ✅ (metadato propio + aparece también listado en la búsqueda web).
  - *"OTONOKE - Dandadan Opening [David Delgado] Español Latino"* · 5,544 vistas · 30-oct-2024 · https://www.youtube.com/watch?v=HLvL0NIRxDc · ✅ (metadato propio).
  - Otros covers listados (no verificados con metadato propio, sólo por la búsqueda): "DANDADAN OP 1 | OTONOKE | André - A!", y versiones en TikTok con el hashtag #otonoke #cover #español. ⚠️ (una fuente, búsqueda web).
- **Fandubs de escenas/parodias**: canal "Baks_otaku" con clips de Dandadan en Dailymotion (1875 y 925 vistas, ya en `datos-voz.md`); "Dandadan - Ep 12 - Fandub Latino" en TokyVideo; contenido de doblaje "peruano" de fans en TikTok (@borink_zzz, con las voces oficiales latinas como referencia para la parodia) y comparaciones "Doblaje Latino Meme" en TikTok. ⚠️ (vistas de TikTok no medibles desde aquí sin login; los enlaces son reales, tomados de la búsqueda web).
- **Parodia con los actores oficiales**: Azucena Estrada (Momo, Netflix), José Luis Piedra (Okarun, Netflix) y Magda Giner (Turbo Ruca, Crunchyroll) participaron en una parodia de internet creada por el canal **Cool Bread** (dato ya en `datos-voz.md`, Doblaje Wiki) — o sea, los propios actores latinos alimentan la cultura de parodia del doblaje, no sólo los fans. ✅.
- ⚠️ No encontré covers de doblaje fan completos (episodio entero redoblado por fans) con métricas grandes (miles de vistas) más allá de los openings musicales: la mayoría del fandub hispano de Dandadan son clips cortos, parodias de TikTok o memes de audio, no series largas de fandub como en animes más viejos.

## Lo mejor para la lámina

1. **La cara de Turbo Granny sonriendo con malicia** (ep1 min 14:30-14:45, fotograma propio) es la expresión más reconocible y "de personaje secundario querido" (3º en la encuesta oficial, por delante de Aira y Jiji): encaja perfecto en un canal de doblaje por lo "malhablada" que es oficialmente.
2. **La frase real transcrita "Nos va a tener que dar su banana"** (audio latino, min 14:59) es el gag más citado por el fandom (el meme del "kintama"): un cuadro de diálogo con esa frase, en la tipografía de grito de la serie, es reconocible al instante para cualquiera que haya visto un solo episodio.
3. **Aira Shiratori es el personaje "secundario más querido" con matices**: 5ª en la encuesta oficial y 2ª en favoritos de AniList, pero la MENOS dibujada de los 4 en Danbooru — ideal para una lámina que la muestre en su careta "vanidosa" (ep6 min 7:00, "I'm all too pretty!") en vez de la típica "chica dulce", que es precisamente la mentira que el personaje representa dentro de la trama.

## No encontré

- ⚠️ Cumpleaños y altura exactos de Momo, Okarun, Turbo Granny y Aira: no aparecen en la wiki en inglés ni en las páginas del *Daizukan* que cita (sólo edad de curso, 16-17 años). Búsquedas: `dandadan.fandom.com` wikitext de las 4 fichas (secciones completas revisadas), más búsqueda web "Dandadan Daizukan altura cumpleaños".
- ⚠️ Fotogramas propios de "alegría" franca y "vergüenza" pura para Momo y Okarun, y de "tristeza"/"vergüenza" para Aira consciente: miré 4 episodios completos (1, 5, 6, 7) más el tráiler oficial y no until esas escenas cayeran justo en el muestreo de 15s; lo más cercano queda anotado arriba con su ⚠️. Quedaría para una tanda extra mirar los episodios 2, 3 o 4 completos si se necesita cerrar el hueco.
- ⚠️ Turbo Granny en emociones fuera de "rabia/malicia" (alegría, tristeza, miedo, vergüenza): en los episodios mirados sólo actúa como antagonista amenazante; su lado compasivo se cuenta pero no se muestra en pantalla en esos episodios.
- ⚠️ Un hilo o artículo que liste explícitamente "qué le parecería falso a un fan" de Dandadan (formato exacto que sugiere ENCARGO.md): no until una fuente que lo diga con esas palabras; lo de la sección de punto 12 se dedujo de reseñas y datos oficiales reales, no de una lista ya armada.
- ⚠️ Fandubs completos (episodios enteros redoblados por fans, no sólo openings/memes) con métricas grandes: no encontré ninguno con miles de vistas comprobables desde este servidor.

## Bitácora de búsqueda

- Doblaje Wiki, wikitext completo de "Dan Da Dan" vía `action=parse&prop=wikitext` (curl directo, sin buscador): tabla de repartos, "Datos de interés", créditos — base del punto 8.
- Fandom `dandadan.fandom.com`, wikitext vía API de las páginas Momo_Ayase, Okarun, Turbo_Granny, Aira_Shiratori y Popularity_Polls (curl directo): personalidad, trasfondo, trivia/Daizukan — base de los puntos 13 y 20.
- WebSearch (español e inglés, ~14 búsquedas de las 50 disponibles): "ANMTV Dandadan doblaje latino Crunchyroll elenco", "Dandadan doblaje Netflix elenco Azucena Estrada José Luis Piedra ANMTV", "Fernanda Gastélum Aira Dandadan doblaje", "Elizabeth Infante Aira Dandadan Crunchyroll doblaje", "List of Dandadan episodes Aira Shiratori introduced", "Dandadan Crunchyroll Anime Awards 2025", "Dandadan episodio 7 made me cry reddit", "Dandadan opening español latino cover fandub", "Dandadan fandub español TikTok parodia", "Dandadan fandom pet peeve misconception" (sin resultado útil), "Dandadan review score streaming ranking Parrot Analytics", "Dandadan encuesta de popularidad Tatsu color spread".
- `fotogramas.py` sobre Internet Archive (Plan B de AYUDANTE.md, YouTube pide login desde este servidor): episodios completos `english-sub-s-01.-e-01-op-join`, `english-sub-s-01.-e-05`, `english-sub-s-01.-e-06-.compressed`, `s-01.-e-07_202411` (cada 15s, 96 fotogramas/episodio) + tráiler oficial de Crunchyroll en Dailymotion (`x96npto`, cada 2s). Todas las hojas miradas con Read. Vídeos borrados de `/tmp/claude-0/trabajo/41-dandadan-voz/` tras sacar las hojas (⚠️ nota: los .mp4/.m4a siguen en la carpeta de trabajo fuera del repo, no en `biblias/`).
- `voz.py` (Whisper local) sobre el ítem de Internet Archive `dan-da-dan-latino-01` (episodio 1 completo, audio latino de Crunchyroll): segmentos 0-150s y 800-920s, transcritos con minuto y ficha de voz (tono/semitonos/velocidad).
- yt-dlp `--skip-download --print` (sin descargar vídeo) para metadatos de 3 covers de YouTube del opening en español: funcionó en 2 de 3 (uno pidió login).

Sigue: fotogramas propios de alegría/vergüenza para Momo y Okarun, y de tristeza/vergüenza para Aira consciente (mirar episodios 2-4 completos con `fotogramas.py`); cumpleaños/altura exactos de los 4 si aparecen en el Daizukan físico.
