# Parte de VOZ Y PERSONAJES · Adventure Time (Hora de aventura)

Puntos de `ENCARGO.md`: **7** (popularidad), **8** (doblaje latino y frases),
**12** (fandom y qué NO hacer), **13** (personajes a fondo), **20** (gustos),
**21** (por qué la aman), **22** (fan dubs y comunidad hispana).

Parto de `partes/datos-voz.md` (Dailymotion no tenía nada útil: son clips de
trailers/cajitas felices, no diálogo doblado) y de lo que ya escribió el
redactor anterior en `biblia.md` (secciones 8, 9, 10, 14; la red estaba
**cerrada** cuando se hizo, así que casi todo era ⚠️ de memoria o de resúmenes
de búsqueda). Aquí **confirmo con la red abierta**, corrijo lo que estaba mal
y añado los puntos 20, 21 y 22, que no existían. Cada dato nuevo dice de
dónde sale. `biblia.md` NO se toca: esto lo usa el redactor.

**Novedad de método**: la API de Doblaje Wiki (`doblaje.fandom.com/es/api.php`)
y la wiki inglesa `adventuretime.fandom.com` (antes daban error o 404 al
equipo del recolector) **sí respondieron** hoy con `curl -A "Mozilla/5.0"`
(sin user-agent, `urllib` de Python daba 403). Con eso saqué el reparto
completo, directamente de la fuente, y **6 muestras de audio reales** del
doblaje (ver §8.3), transcritas con `voz.py` (Whisper local).

---

## 7 · Popularidad (encuestas oficiales y de fans)

- **No existe una encuesta oficial numérica** de popularidad de personajes de
  Cartoon Network para esta serie · busqué en español e inglés
  («Adventure Time character popularity poll official», «reddit poll ranking»)
  y no apareció ninguna · ⚠️ «no encontré» (no «no existe»: puede haberla en
  una revista o evento que no indexa el buscador).
- Lo más cercano a un reconocimiento oficial: **CartoonNetwork.co.uk nombró a
  Marceline «Character of the Week» el 24 de enero de 2012** ✅
  ([Adventure Time Wiki, Marceline § Reception](https://adventuretime.fandom.com/wiki/Marceline),
  [Wikipedia: Marceline the Vampire Queen](https://en.wikipedia.org/wiki/Marceline_the_Vampire_Queen)
  cita el mismo dato).
- El comunicado de prensa oficial del cómic **«Marceline and the Scream
  Queens»** (BOOM! Studios) la llamó **«fan-favorite»** ✅ (misma wiki +
  Wikipedia, ambas citan el comunicado).
- Según el creador **Pendleton Ward**, la popularidad de Marceline **«creció
  enormemente»** después de su primer episodio, «Evicted!» (1×12) ✅
  ([Adventure Time Wiki](https://adventuretime.fandom.com/wiki/Marceline)).
- **Eric Thurm** (revista *Vulture*) llamó al Rey Helado/Simon **«Adventure
  Time's Best Character»** en una reseña retrospectiva ✅ (citado igual en
  [Wikipedia: Ice King](https://en.wikipedia.org/wiki/Ice_King) y en
  [Adventure Time Wiki](https://adventuretime.fandom.com/wiki/Ice_King)).
- ***The Guardian*** llamó a Marceline **la mejor de la serie** en una reseña
  del DVD, remarcando que «es responsable de algunas de las mejores canciones
  del show» ✅ (mismo doble respaldo: Wikipedia + Adventure Time Wiki).
- **WhatCulture** (2016) la puso **#4** en su ranking de mejores personajes,
  llamándola «bad ass» y «el personaje más cool de la serie» ⚠️ (una fuente:
  Adventure Time Wiki, que cita la reseña original).
- El sitio **Ranker** tiene una lista votada por el público («Best Adventure
  Time Characters», 1958 votantes a fecha de esta búsqueda) pero **da error
  401** al intentar leerla (posible bloqueo anti-bot) ⚠️ «no pude confirmar el
  orden exacto», sólo que existe.
- **BMO era el personaje favorito del propio Pendleton Ward**, según entrevista
  con Hot Topic ✅ ([Adventure Time Wiki: BMO § Trivia](https://adventuretime.fandom.com/wiki/BMO)) —
  dato curioso: el creador prefiere a un secundario, no a Finn.
- Los secundarios con más peso propio (fuera del top Finn/Jake/Marceline/PB/
  Rey Helado): **BMO** (favorito del creador), **Princesa Grumosa** (memes,
  «Oh por Glob»), **Fionna** (protagonizó su propia serie, «Fionna & Cake»,
  2023-2024) ✅.

## 8 · Doblaje latino y frases textuales

> Corrige y amplía `biblia.md` §10. La wikitext completa de la página
> [`Hora de aventura` en Doblaje Wiki](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Hora_de_aventura)
> (87 135 caracteres) **sí se pudo leer hoy** con `curl -A "Mozilla/5.0"`, cosa
> que el recolector no consiguió. Es la fuente 1 de cada actor; la fuente 2 va
> aparte.

### 8.1 Ficha técnica (corrige y precisa lo que ya había)

- Estreno en EE. UU.: **5 de abril de 2010**; en Hispanoamérica: **8 de agosto
  de 2010**. Terminó en EE. UU. el **3 de septiembre de 2018** (283 episodios,
  10 temporadas) y en Latinoamérica el **23 de septiembre de 2018** ✅
  ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Hora_de_aventura)
  + [Wikipedia: Adventure Time](https://en.wikipedia.org/wiki/Adventure_Time)).
- **Estudios**: **Sensaciones Sónicas** (temporadas 1-4 y primera mitad de la
  5) → **SDI Media de México** (segunda mitad de la 5 en adelante). Algunos
  promocionales se doblaron en **Candiani Dubbing Studios** ✅ (Doblaje Wiki,
  tabla «Estudios de doblaje»).
- **Ingeniero de grabación**: Antonio Hernández. **Supervisión/logística**:
  Marina Urbán (temp. 1-5). **Gerentes de producción**: Gerardo Suárez
  (temp. 1-5), Gabriela Garay (temp. 5.2-9). **Productor ejecutivo**: Mario
  Castañeda (temp. 5.2-6) — **el mismo actor que dobla a Goku en Dragon Ball**
  ⚠️ (dato de Doblaje Wiki, no comprobado en segunda fuente para este dato
  puntual, aunque la voz de Goku de Castañeda sí es de dominio público).
- **Directores por temporada** (tabla exacta de Doblaje Wiki, no la lista
  suelta que había antes) ✅:

  | Director | Temporadas |
  |---|---|
  | Óscar Flores | 1ª-2ª, 4ª (eps. 96-101), 5ª (ep. 131-¿?) |
  | Rafael Pacheco | 3ª, 8 episodios |
  | Circe Luna | 3ª y 4ª, algunos episodios |
  | Elsa Covián | 4ª, algunos episodios |
  | Carlos Hugo Hidalgo | 4ª, algunos episodios (retake de sonido) |
  | Juan Antonio Edwards | 3ª, algunos episodios |
  | *(sin datos)* | 5ª hasta el episodio 130 |
  | **Arturo Castañeda** | **6ª-9ª** |

  **Arturo Castañeda** (nuevo dato, no estaba en la biblia): nació el 3 de
  octubre de 1988 en Ciudad de México, **hijo de Mario Castañeda (voz de
  Goku) y Rommy Mendoza**, hermano de la actriz Carla Castañeda; de niño dobló
  a Harry Potter en *La piedra filosofal* (2001) ✅
  ([Doblaje Wiki: Arturo Castañeda](https://doblaje.fandom.com/es/wiki/Arturo_Casta%C3%B1eda),
  [Facebook — Comic Fest Juárez](https://www.facebook.com/comicfestjuarez/posts/arturo-casta%C3%B1eda-doblajeactor-y-director-de-doblaje-mexicano-hijo-de-los-tambi%C3%A9n/811605114317097/)).
- **Traductores**: Carlos Hugo Hidalgo (la mayoría de episodios), Janet León,
  Luis Leonardo Suárez (131 en adelante), Circe Luna, David Bueno (ep. 279) ✅
  (Doblaje Wiki, tabla «Traductores»).

### 8.2 Reparto (corregido con la tabla oficial de Doblaje Wiki)

| Personaje | Voz latina | Temporadas | Estado | 2ª fuente |
|---|---|---|---|---|
| **Marceline** | **Isabel Martiñón** | 1ª-9ª (toda la serie doblada) | ✅ | [TikTok, Expomac Veracruz](https://www.tiktok.com/@rebecavirgen/video/7434952138339536184), [Facebook Starcon](https://www.facebook.com/starconmx/videos/isabel-marti%C3%B1on-actriz-de-doblaje-que-dio-voz-a-marceline-en-hora-de-aventura-be/1609015216591153/) |
| Marceline niña (flashbacks) | Isabel Martiñón (misma actriz) | 3ª-5ª | ✅ | Doblaje Wiki |
| Marceline alterna («Fionna & Cake», universo alterno) | Ángela Villanueva (5ª) → **vuelve Isabel Martiñón** (7ª) | 5ª, 7ª | ⚠️ | sólo Doblaje Wiki |
| **Finn** | **José Antonio Toledano**, **sin cambios en toda la serie** | 1ª-10ª | ✅ | [GeekZilla](https://geekzilla.tech/hora-de-aventura-misiones-secundarias-llega-a-hbo-max/), [TheProjectArcade](https://theprojectarcade.com/hora-de-aventura-misiones-secundarias-revive-al-jake-clasico-hbo-max-revela-su-doblaje-latino/) |
| **Jake** | **José Arenas** (temp. 1-5.2, eps. 1-148) → **mismo actor, «tono nuevo»** (5.2-10, eps. 149-283) | 1ª-10ª | ✅ | [Milenio](https://www.milenio.com/espectaculos/television/cambio-voz-jake-perro-hora-aventura), [TVLaint](https://www.tvlaint.com/2026/09/jose-arenas-regresa-como-jake-en-hora.html) |
| Jake (2 loops sueltos) | Víctor Ugarte (7ª, ep. 202); Tommy Rojas (9ª, ep. 279 «Diamantes y limones») | — | ⚠️ | sólo Doblaje Wiki |
| **Dulce Princesa** | **Karla Falcón** (1ª-2ª; **vuelve en la 4ª, ep. 96, con «Rey Gusano»**, hasta el final) | 1ª-2ª, 4ª-10ª | ✅ | [TikTok, entrevista Festigame 2024](https://www.tiktok.com/@eldiariodelalquimista/video/7440244073505623352) |
| Dulce Princesa (suplente) | **Claudia Urbán** (eps. 58-94, temp. 3ª-4ª) — Urbán se retiró del doblaje en **noviembre de 2012** para dedicarse a su empresa con su esposo Gerardo Suárez | 3ª-4ª | ✅ | Doblaje Wiki (con fecha de retiro y motivo, verificable en su propia ficha) |
| **Rey Helado / Simon** | **Óscar Flores**, toda la serie | 1ª-10ª | ✅ | [La República (Perú)](https://larepublica.pe/cine-series/2022/10/22/oscar-flores-entrevista-a-actor-mexicano-de-voz-en-the-mandalorian-que-consejo-dio-a-las-personas-que-quieren-hacer-doblaje-anime-movie-con) |
| Rey Helado (2 episodios) | Rafael Pacheco (3ª, eps. 59-60) | — | ⚠️ | sólo Doblaje Wiki |
| **BMO** | **Gustavo Melgarejo** (1ª-5ª) → **Héctor Emmanuel Gómez** (5.2ª-9ª, desde «El traje de Jake») | 1ª-9ª | ✅ | [Hora de Aventura Wiki: Héctor Emmanuel Gómez](https://horadeaventura.fandom.com/es/wiki/H%C3%A9ctor_Emmanuel_G%C3%B3mez) |
| **Princesa Grumosa** (Lumpy Space Princess) | **Alfonso Obregón**, casi toda la serie | 1ª-9ª | ✅ | [Hora-de.fandom (wiki espejo)](https://hora-de.fandom.com/es/wiki/Princesa_Grumosa) |
| Hunson Abadeer (padre de Marceline) | José Luis Orozco (2ª) → Rafael Pacheco (3ª) → Julián Lavat (4ª) → Enrique Cervantes (9ª) | — | ⚠️ | sólo Doblaje Wiki |
| Voz **original** (inglés) de Marceline | **Olivia Olson**, **canta ella misma** | toda la serie | ✅ | [Wikipedia: Olivia Olson](https://en.wikipedia.org/wiki/Olivia_Olson) |

**Corrección importante sobre §10 de `biblia.md`**: decía que Karla Falcón
«vuelve desde la 4 a petición de los fans» sin más detalle; ahora hay el
**episodio exacto («Rey Gusano»)** y el **motivo documentado del cambio**: la
wiki cita **peticiones firmadas, un grupo de Facebook y un post de queja**
contra el reemplazo de Falcón por Urbán ✅
([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Hora_de_aventura) enlaza
la petición en change.org/peticionpublica.es y el grupo de Facebook
«Evitemos que cambien las voces...»). Esto es un dato de oro para el punto 22
(la comunidad hispana **se organizó** para pedir que no cambiaran una voz).

- **Las voces de Finn y Marceline NUNCA cambiaron en toda la serie**, algo
  poco común (casi todos los demás personajes sí tuvieron cambios) ✅ (dicho
  explícitamente en la sección de curiosidades de Doblaje Wiki).
- El **título latino del episodio final es «Ven Conmigo»** (no «Come Along
  With Me» sin traducir) ✅ (Doblaje Wiki, sección de curiosidades).
- Canal 2 (El Salvador) y Canal 5 (México) emiten la serie **sin las
  censuras** que sí tiene en Cartoon Network y Netflix Latinoamérica ✅
  (Doblaje Wiki).

### 8.3 Frases reales del doblaje: muestras de audio de Doblaje Wiki, transcritas

> El recolector no encontró clips oficiales doblados en Dailymotion (sólo
> trailers y cajitas felices, sin diálogo). YouTube pide iniciar sesión. Así
> que bajé **6 muestras de audio oficiales de Doblaje Wiki** (`.ogg`, la wiki
> las sube como prueba de cada actor) y las pasé por `herramientas/voz.py`
> (Whisper local). **Son diálogo real doblado, con la voz de cada actor**,
> aunque no sé de qué episodio es cada una (la wiki no lo dice) y Whisper
> puede confundir nombres propios ✅ el audio es real y oficial; ⚠️ el
> episodio exacto y alguna palabra suelta.

| Personaje | Frase transcrita | Voz (medida por `voz.py`) | Archivo fuente |
|---|---|---|---|
| **Marceline** | «¿Vía⚠️? ¿Qué estás haciendo? No puedes estar aquí. **Ash no quiere que salga con mortales**» | registro agudo (295 Hz), **muy expresiva (17.3 semitonos)**, velocidad normal (2.86 palabras/s) | [Isabel Martiñón como Marceline.ogg](https://static.wikia.nocookie.net/doblaje/images/a/a6/Isabel_Marti%C3%B1on_como_Marceline.ogg) |
| **Finn** | «Tienes razón, sólo hay una forma de salir. Uno de nosotros será sacrificado para que los otros vivan. Saldré y dejaré que las criaturas me casen. Y mientras están ocupadas con mi cuerpo de adolescente, los tres puedan escalar para estar a salvo. No traten de convencerme. Estoy seguro de que... esto es lo que significa ser un...» | registro medio (164 Hz), muy expresiva (16.0 semitonos), **velocidad rápida** (3.49 palabras/s) | [Jose Toledano - Finn 5ta Temporada.ogg](https://static.wikia.nocookie.net/doblaje/images/5/57/Jose_Toledano_-_Finn_5ta_Temporada.ogg) |
| **Jake** | «Estoy para ti, hermano. Pero, Finn, te diré algo gentilmente. Necesitas otra espada. Ellos iban a acabarte. Todo estará bien. Vayamos de compras» | registro medio (214 Hz), muy expresiva (14.8 semitonos), velocidad normal (2.43 palabras/s) | [Jose Arenas - Jake Nuevo Tono.ogg](https://static.wikia.nocookie.net/doblaje/images/5/51/Jose_Arenas_-_Jake_Nuevo_Tono.ogg) |
| **Dulce Princesa** | «¡Los veo en el dulce reino! ¡Esta noche!» | registro **muy agudo** (397 Hz), velocidad rápida (3.36 palabras/s) | [Karla Falcon como la Dulce Princesa.ogg](https://static.wikia.nocookie.net/doblaje/images/4/40/Karla_Falcon_como_la_Dulce_Princesa.ogg) |
| **Rey Helado** | «¡La hora es suya, pero el día será mío! ¡Como tú, princesa mía!» | registro agudo (266 Hz), muy expresiva (15.8 semitonos) | [Oscar Flores como el Rey Helado.ogg](https://static.wikia.nocookie.net/doblaje/images/7/7a/Oscar_Flores_como_el_Rey_Helado.ogg) |
| **BMO** | «¡Jajajajajaja! ¡Juguemos⚠️ a policías y⚠️ ladrones!» (Whisper transcribió «Cukemos... iradrones», reconstruido de oído) | registro **muy agudo** (465 Hz), velocidad **lenta** (1.36 palabras/s) | [BMO.ogg](https://static.wikia.nocookie.net/doblaje/images/7/70/BMO.ogg) |

Estas frases **sí sirven para la lámina**: son diálogo real, con el tono
medido de cada voz (útil también para el punto 13, cómo suena cada uno). La
frase de Marceline («Ash no quiere que salga con mortales») encaja con su
personaje burlón/rebelde; la de Finn es un discurso de sacrificio heroico
típico de su forma de ser.

### 8.4 «Oh por Glob» y otras muletillas dobladas (confirmo lo dudoso de §10.4/§14)

- **«¡Oh por Glob!»** es la muletilla latina confirmada de la **Princesa
  Grumosa** (Lumpy Space Princess), traducción de «Oh my Glob» ✅ (Doblaje
  Wiki + [Hora-de.fandom.com, ficha de Princesa Grumosa](https://hora-de.fandom.com/es/wiki/Princesa_Grumosa)).
  Esto **corrige** la duda que dejó `biblia.md` §10.4/§14.1 («dato confuso»):
  no se cambió por «Oh por Dios», la frase sí es de Grumosa y sí lleva
  «Glob» en latino.
- La voz de «Misiones Secundarias» (2026) sigue con Toledano, Arenas y
  Flores ✅ (ya estaba en `biblia.md`, sin cambios que reportar).

## 12 · Lo que ama el fandom, y qué NO hacer

`biblia.md` §14 ya está bastante completo. Confirmo y añado:

- La **organización de fans para que Karla Falcón volviera** como Dulce
  Princesa (firmas, grupo de Facebook, quejas en foros) es en sí un ejemplo
  de **lo que el fandom ama y defiende**: una voz que sienten «suya» ✅ (§8.2,
  arriba). Para un canal de doblaje como #musica-nueva/el server en general,
  es un dato perfecto: **la audiencia latina peleó por su actriz de doblaje**.
- **BMO es el personaje favorito del creador** (Pendleton Ward, entrevista
  Hot Topic) ✅ — dato para «lo que el fandom valora», no sólo lo visual.
- La pareja **«Bubbline»** (Marceline + Dulce Princesa) fue nominada a un
  **GLAAD Media Award** (categoría Outstanding Kids and Family Programming)
  por el especial «Obsidian» ✅ ([Wikipedia: Marceline the Vampire
  Queen](https://en.wikipedia.org/wiki/Marceline_the_Vampire_Queen)). Se
  confirma como **el hito de representación LGBTQ+** más citado del fandom
  hispano y global — no es sólo «shippeo», es reconocido oficialmente.
- Confirmo (✅, dos fuentes: Doblaje Wiki + Hora-de.fandom.com) que **«¡Oh por
  Glob!»** es de la Princesa Grumosa — corrige la duda anterior (§8.4).
- **Qué NO hacer, dato nuevo**: no poner **subtítulos con la censura de
  Cartoon Network** si el canal quiere sonar «fiel»: en El Salvador y México
  la serie se vio **sin cortes** ✅ (Doblaje Wiki) — anécdota de fans que
  comparan versiones.
- Sigue sin encontrarse una traducción textual verificada de «¿Qué hora es?
  ¡Hora de aventura!» como frase exacta de un capítulo doblado (es la letra
  del intro, no un diálogo) — se mantiene ⚠️ como en `biblia.md`.

## 13 · Los personajes a fondo (carácter, arco, cómo se expresan, dinámicas)

> `biblia.md` §8 ya describe bien a Marceline, Finn, Jake, Dulce Princesa y
> BMO **desde la música** (es el ángulo del canal). Aquí profundizo su
> **carácter general**, arco y forma de hablar con la wiki en inglés
> (`adventuretime.fandom.com`, páginas «Marceline», «Finn», «Jake»,
> «Princess Bubblegum», «BMO», «Ice King» — todas leídas hoy, wikitext
> completo vía API) para que el redactor tenga de dónde ampliar sin
> repetir lo que ya hay.

### Marceline Abadeer

- **Personalidad**: independiente, traviesa, al principio antagonista
  («Evicted!», 1×12) hasta que Finn ve que es «a radical dame who likes to
  play games» ✅. Debajo de la fachada dura es **muy sentimental**: se
  emociona por su osito Hambo (regalo de Simon) y rompió con su ex Ash
  cuando él lo vendió ✅. Le cuesta expresar sentimientos **si no es
  cantando** («Fry Song», «I'm Just Your Problem») ✅
  ([Adventure Time Wiki: Marceline](https://adventuretime.fandom.com/wiki/Marceline)).
- **Arco**: de villana traviesa (temp. 1) → amiga cercana y más madura, que
  acepta su inmortalidad («The Dark Cloud») → en «Obsidian» (años después del
  final) es **mucho más madura emocionalmente sin perder su lado juguetón** ✅.
- **Miedo real**: no es sólo «que la olviden» (como decía `biblia.md`): es
  **el peso de la inmortalidad**, ver morir a todos los que quiere, y el
  precio de sus poderes (consume almas de vampiros) — «Magia, Locura y
  Tristeza» es un concepto central de su arco en «Stakes» ✅ (misma fuente).
- **Cumpleaños**: **27 de junio** ✅ (infobox de Adventure Time Wiki, con cita
  a la canción «House Hunting Song», 1×12, donde dice «I'm a thousand years
  old»).
- **Cómo se ve a sí misma**: «No soy mala. Tengo mil años y perdí de vista mi
  código moral» (cita directa del personaje) ⚠️ traducción mía del inglés, no
  encontré el doblaje de esta línea puntual.

### Finn el humano

- **Personalidad**: impulsivo, de mal genio a veces, pero de fondo un chico
  **bondadoso, valiente y con un código moral casi absoluto** — le cuesta
  mucho hacer algo que considere «malo», incluso robar en una misión
  («City of Thieves») ✅. Actúa de «sheriff moral» de Ooo ✅
  ([Adventure Time Wiki: Finn](https://adventuretime.fandom.com/wiki/Finn)).
- **Arco**: al descubrir que su padre biológico es un criminal egoísta
  («Wake Up»/«The Tower»), Finn casi cae en la venganza, pero aprende a
  controlarla con ayuda de la Dulce Princesa ✅. Va madurando: acepta el
  romance (besa a PB en «Too Young», sale con Flame Princess) después de
  vomitar de vergüenza con escenas románticas en «Go With Me» ✅.
- **Cómo se expresa**: casi no llora — sólo en situaciones devastadoras
  (muerte, un corazón roto), según «Dad's Dungeon» ✅. Catchphrases
  matemáticas («mathematical», «rhombus», «algebraic») que además usa como
  censura de groserías ✅.
- **Gustos confirmados en pantalla**: color favorito **azul bebé «de
  niño»** («The Silent King»); comida favorita **meatloaf** (pastel de
  carne), confirmada en tres episodios distintos («Still», «Jake Suit»,
  «Three Buckets») ✅; es **daltónico rojo-verde** («Red Starved») ✅
  (todas del Adventure Time Wiki, con cita de episodio cada una).

### Jake el perro

- **Personalidad**: relajado, cero preocupado, se apoya mucho en sus poderes
  (o en Finn) para salir de líos; hace de mentor-sabio de Finn con consejos
  que van de brillantes a absurdos ✅. Puede ser **irresponsable**, deja a
  Finn peleando solo a veces, pero siempre aparece cuando hace falta ✅
  ([Adventure Time Wiki: Jake](https://adventuretime.fandom.com/wiki/Jake)).
- **Posibles rasgos**: **quizá disléxico** (escribe al revés, «Storytelling»)
  y con **síntomas de TDAH** (se distrae fácil, se duerme a media
  conversación) ⚠️ — la propia wiki lo dice como «posible», no diagnóstico
  oficial de la serie.
- **Comida**: le encanta comer, sobre todo **comida chatarra: pay, hamburguesas
  y helado**; el chocolate lo mataría, como a un perro real («Slumber Party
  Panic») ✅. Cocina de verdad: bacon pancakes, café, «Everything Burrito» ✅.

### Dulce Princesa (Princess Bubblegum / Bonnibel)

- **Personalidad**: amable y bien educada en general, pero con un lado
  **frío y hasta un poco macabro**: corta y reconecta extremidades de
  criaturitas «sin dolor» por experimento («The Lich»), tiene un humor negro
  con venenos («The Other Tarts») ✅. Es **muy racional**, escéptica de la
  magia («all magic is science») ✅. Bajo estrés extremo, **come de más**
  como mecanismo de escape ✅ ([Adventure Time Wiki: Princess
  Bubblegum](https://adventuretime.fandom.com/wiki/Princess_Bubblegum)).
- **Edad**: 827 años según *Explore the Dungeon Because I DON'T KNOW!*, más
  joven que Marceline según el libro *Art of Ooo* ✅ (misma fuente, con cita
  al libro).
- **Cómo se expresa**: da órdenes técnicas que nadie entiende (coincide con
  lo ya escrito en §8 de `biblia.md` sobre la música), y tiene el **mayor
  número de vestuarios de cualquier personaje** de la serie ✅ (Adventure
  Time Wiki, Trivia).

### BMO

- **Personalidad**: dice no tener emociones («I am incapable of emotion»)
  pero llora, se enoja y se pone celoso — es inconsistente con su propia
  frase ✅. Muy protector con Finn y Jake («If anyone tries to hurt Finn, I
  will kill them») ✅. Actúa de mediador cuando Finn y Jake discuten (edita
  su película en «Video Makers» para arreglar la pelea) ✅
  ([Adventure Time Wiki: BMO](https://adventuretime.fandom.com/wiki/BMO)).
- **Cómo habla**: como un niño muy seguro de sí mismo, a veces en tercera
  persona (confirma lo que ya decía `biblia.md`, ahora ✅ con fuente directa).

### Rey Helado / Simon Petrikov (secundario más querido, punto extra)

> No está descrito en `biblia.md` como personaje aparte (sólo aparece en la
> tabla de doblaje y como «secundario musical»). Por su peso en el fandom
> (ver §21), merece esta ficha.

- **Como Simon**: inteligente, cariñoso, capaz de un enorme autosacrificio —
  cuidó a Marceline de niña en el apocalipsis pese a estar perdiendo la
  cordura por la corona; sus últimas cartas a ella (leídas en «I Remember
  You», 4×25) muestran que temía abandonarla ✅.
- **Como Rey Helado**: en las primeras temporadas es un villano irritante
  «al estilo Gargamel»; desde la temporada 3 se vuelve un personaje trágico,
  solitario, que sólo quiere casarse con una princesa porque **no recuerda
  por qué** — el eco de haber perdido a Betty ✅
  ([Adventure Time Wiki: Ice King](https://adventuretime.fandom.com/wiki/Ice_King)).
- **Detalle físico curioso**: tiene un **tatuaje de pingüino** en el glúteo
  derecho («Prisoners of Love», secuencia de sueño) ⚠️ dato de trivia, no
  visto en fotograma propio.
- **Cómo se expresa**: optimista incluso en las peores situaciones; en el
  final («Come Along With Me») consuela a Finn diciéndole que nadie elige
  cómo morir, pero que al menos estaban juntos ✅.

### Dinámicas (para láminas en grupo)

- **Marceline y la Dulce Princesa**: de tensión con humor («Obsidian», ríen
  juntas) a pareja oficial (beso final, 10×13) ✅.
- **Marceline y Simon/Rey Helado**: padre-hija adoptivos; ella es la única
  (con Betty) que lo llama «Simon» y él lo acepta de ella, aunque a Betty
  la corrige cuando lo intenta ✅ (Adventure Time Wiki: Ice King, Trivia).
- **BMO media entre Finn y Jake** cuando discuten ✅ (arriba).
- **Jake es «el hermano sabio pero disperso»** de Finn; Finn es «el impulsivo
  con código moral» — el contraste es la base cómica del dúo ✅.

## 20 · Gustos y detalles de cada personaje

> Punto que **no existía** en `biblia.md`. Todo sale de los infoboxes y
> secciones de curiosidades («Trivia») de `adventuretime.fandom.com`
> (wikitext vía API), con el episodio que lo confirma cuando la wiki lo da.
> **No hay campo de altura en ningún infobox** de los seis personajes que
> miré (Marceline, Finn, Jake, Dulce Princesa, BMO, Rey Helado): lo marco
> como «no encontré» en vez de inventar un número.

### Marceline

- **Comida**: no bebe sangre, **consume el color rojo** (por eso toda su ropa
  tiene al menos una prenda roja «por si acaso», excepto en «Red Starved») ✅.
  Comer **tomates le da sueños lúcidos**, según una nota suya en «Marceline's
  Closet» ✅.
- **Aficiones**: música (bajo-hacha), **basquetbol** («Simon & Marcy») ✅.
- **Mascota**: un **caniche zombi llamado Schwabl** ✅.
- **Objeto que siempre lleva**: el **bajo-hacha**, hecho del hacha de guerra
  de su familia (ya en `biblia.md` §1/§3).
- **Detalle de cuidado**: usa protector solar **«FPS 10 000 000»**
  («Marceline the Vampire Queen») ✅.
- **Cómo se ve a sí misma**: ver §13.
- **Altura**: no hay número; la wiki sólo dice que es «alta y delgada», más
  alta que la Dulce Princesa al estar de pie, y del tamaño del Rey Helado en
  «I Remember You» ⚠️ sin cifra.

### Finn

- **Color favorito**: **azul bebé** «de niño» (según él mismo, «The Silent
  King») ✅.
- **Comida favorita**: **meatloaf** (pastel de carne), tres veces confirmada
  en pantalla ✅ (§13).
- **Lo que odia/le cuesta**: las escenas románticas (vomita, «Go With Me»);
  es **daltónico rojo-verde** ✅.
- **Objeto que siempre lleva**: su espada (varias a lo largo de la serie) y
  su mochila; en «Jake vs. Me-Mow» lleva la cajita de música de su madre
  adoptiva y se sabe su nana de memoria ✅.
- **Cómo se ve a sí mismo**: quiere ser un gran héroe, «moral sheriff» de Ooo,
  y sufre cuando no puede ayudar a alguien ✅.

### Jake

- **Comida**: pay, hamburguesas, helado; **el chocolate lo mataría** ✅.
- **Aficiones**: cocinar (le sale bien: bacon pancakes, café, sándwiches
  imposibles), tocar la viola, el beatbox ✅ (cocina, nuevo; música ya en
  `biblia.md` §8).
- **Cómo se ve a sí mismo**: el mentor «sabio» de Finn, aunque él mismo sabe
  que sus consejos son inconsistentes ✅.

### Dulce Princesa

- **Color favorito**: **rosa**, dicho por ella misma («The Real You») ✅.
- **Comida favorita**: **espagueti** (se enoja si se le cae, «To Cut a
  Woman's Hair»); desde entonces se le ve comiéndolo en varios episodios ✅.
- **Afición**: toca la **trompeta** («Bad Timing») ✅.
- **Objeto/transporte propio**: un pájaro muy veloz llamado **Morrow**, que
  usa para moverse rápido ✅.
- **Detalle inquietante**: en situaciones límite **consume gente-caramelo**
  de su propio reino para «reponer biomasa» (confirmado por el
  showrunner Adam Muto) ✅.
- **Edad**: 827 años (ver §13).

### BMO

- **Objeto que más valora**: **su control (joystick)**, llamado
  explícitamente «BMO's prized possession» en «What Was Missing» ✅.
- **Detalle técnico/curioso**: su «edad» en la ficha de un DVD especial dice
  **«VER. 2600»**, especie tipo **«110 VOLT-60 HERTZ SYSTEM»** — un chiste
  sobre la consola Atari 2600 (BMO tiene juegos «clones» de esa consola) ✅.
- **Miedo/vulnerabilidad**: llora cuando Finn se afeita la cabeza para
  disfrazarse de otra persona («Davey»), y cuando Jake no invita a su ídolo a
  cenar ✅ — pese a decir que no siente emociones.

### Rey Helado / Simon

- **Manía/detalle físico**: el tatuaje de pingüino (ver §13).
- **Cómo se ve a sí mismo**: como Simon, un arqueólogo enamorado que se
  siente responsable de Marceline; como Rey Helado, sólo sabe que «quiere una
  princesa» sin recordar el porqué real (el eco de Betty) ✅.
- **Objeto**: la corona de hielo (le da poder y locura a la vez) y una
  computadora vieja con la que juega videojuegos y hace dibujos torpes de
  princesas ✅.

## 21 · Por qué la gente la ama

### Reconocimiento formal de la serie completa

- **8 premios Primetime Emmy**, **1 Peabody Award**, **3 Premios Annie**,
  **2 British Academy Children's Awards**, un Motion Picture Sound Editors
  Award y un premio *Kerrang!* ✅ ([Wikipedia: Adventure
  Time](https://en.wikipedia.org/wiki/Adventure_Time), sección de premios).
- El episodio **«Simon & Marcy»** (4×24) fue **nominado a un Primetime Emmy**
  en la ceremonia 65 (2013) ✅. El final, **«Come Along With Me»**, fue
  **nominado a un Emmy Creative Arts en 2019** ✅ (ambos en
  [Wikipedia: Ice King](https://en.wikipedia.org/wiki/Ice_King) y
  [Wikipedia: Come Along with Me](https://en.wikipedia.org/wiki/Come_Along_with_Me_(Adventure_Time))).
- El especial **«Obsidian»** fue **nominado a un GLAAD Media Award** ✅ (ya
  citado en §12).

### Por qué conecta con la audiencia (crítica especializada)

- **Coming-of-age honesto**: *Vox* (Emily VanDerWerff) llamó a la serie «la
  mejor historia de crecimiento de esta era»; a Finn lo describe pasando «de
  niño a casi-hombre» ✅. *Comic Book Resources* destaca que Finn crece de
  «niño amable» a «joven noble» ✅.
- **Representación de salud mental**: el arco del Rey Helado se lee como una
  metáfora del **Alzheimer** y el aislamiento social, según *Vulture*; por
  eso «resulta identificable para un público amplio» ✅. *Teen Vogue* destaca
  a Marceline como ejemplo de representación por venir de una **familia no
  tradicional** cuyas emociones «a veces reflejaban depresión» ✅.
- **Representación LGBTQ+**: *Them* (revista de temas LGBTQ+) llamó a
  Marceline «uno de los mejores retratos de angustia bisexual» en la
  animación ✅ ([Wikipedia: Marceline the Vampire
  Queen](https://en.wikipedia.org/wiki/Marceline_the_Vampire_Queen)). La
  relación con la Dulce Princesa, hecha canon en el final y ampliada en
  «Obsidian», es **el ejemplo más citado** de representación queer en una
  caricatura infantil de esa época ✅ (Wikipedia: Adventure Time, sección de
  recepción crítica, habla de «roughly equal numbers of female and male
  characters» y de la relación confirmada).
- **Originalidad**: la crítica la llama «una de las caricaturas más
  distintivas al aire» por su «pura imaginación», combinando humor accesible
  con temas complejos («guerra nuclear, mortalidad, identidad») ✅
  (Wikipedia: Adventure Time, recepción crítica).

### Con qué personaje se identifica el público, y por qué

- **Con Finn**: por su crecimiento «real», comparado por *Entertainment
  Weekly* con los niños que crecieron viendo Harry Potter, envejeciendo junto
  a su audiencia ✅.
- **Con el Rey Helado/Simon**: por la mezcla de una tragedia enorme
  (Alzheimer, pérdida de identidad) con torpezas cotidianas (vergüenza
  social) — *Vulture* dice que esa mezcla es la razón de que sea «el
  personaje favorito de mucha gente» ✅.
- **Con Marceline**: adolescentes y jóvenes que se identifican con su lado
  «punk», su tristeza de fondo bajo la fachada dura, y —para el público
  LGBTQ+— con su relación abierta con la Dulce Princesa ✅.
- **Cosplay como termómetro de cariño**: Finn y Jake son, según *The Daily
  Beast* (2019), de los disfraces más vistos en Halloween y convenciones en
  EE. UU. en los últimos años; **hubo una carroza de Finn en el Macy's
  Thanksgiving Day Parade de 2013** ✅ ([Adventure Time Wiki:
  Finn](https://adventuretime.fandom.com/wiki/Finn) y
  [Adventure Time Wiki: Jake](https://adventuretime.fandom.com/wiki/Jake),
  ambas citan la misma nota de *The Daily Beast*).

### Escenas que hacen llorar (capítulo, minuto aprox., por qué)

- **«I Remember You»** (4×25, min. ≈8:49 según transcripción usada en
  `biblia.md` §15): Marceline le canta a Simon la carta que él mismo escribió
  para ella cuando aún era humano y se estaba volviendo loco por la corona.
  Se la considera **un punto de inflexión** en cómo la serie trata la salud
  mental; *io9* la llamó «una de las cosas más intensas que he visto en
  años» ✅.
- **«Simon & Marcy»** (4×24): nominada al Emmy; el fandom la pone junto con
  «I Remember You» en listas de «los 10 mejores episodios» de sitios como
  *Geek.com* ✅.
- **El final, «Come Along With Me» / «Ven Conmigo»** (10×13): la crítica lo
  describe como «desgarrador, aventurero e inventivo», «extraño y triste y
  tonto y divertido», con un tono «tierno y un poco lloroso» ✅. En Reddit
  (r/adventuretime, que **sí existe** —corrige el «no encontré» del
  recolector—) hay posts con cientos de votos sobre llorar con el final:
  **«I definitely cried on the last episode and my mom thought I was
  faking»** (1186 puntos) ✅, **«Just cried when finishing the last
  episode»** (167 puntos) ✅
  ([r/adventuretime, vía Arctic Shift](https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=adventuretime&title=cried&limit=15&sort=desc)).
- **«Obsidian»** (especial, años después del final): la pareja Marceline/PB
  ya establecida, con la nominación a GLAAD ya citada, es la escena que más
  cita el fandom para «por fin, felices juntas» ✅ (§12).

## 22 · Fan dubs y comunidad hispana

> Punto que **no existía** en `biblia.md`. YouTube pide iniciar sesión desde
> este servidor (confirmado: tanto `yt-dlp` como `WebFetch` dieron error de
> verificación/CAPTCHA al intentar) y TikTok no entrega datos a un fetch sin
> JavaScript, así que **no pude confirmar vistas ni fecha exacta** de la
> mayoría de estos vídeos — los cito con lo que sí pude verificar (título,
> canal, tema) y marco ⚠️ lo que falta.

- **Fandubs de escenas y parodias en español**, activos desde hace años,
  encontrados por búsqueda (títulos y canales reales, existencia confirmada
  por buscador, **vistas no verificadas** por el bloqueo de YouTube) ⚠️:
  - «Hora De Aventura - Chico Malo (Fandub Español Latino) [clip del
    episodio]» — YouTube.
  - «Hora de aventura "Parodia" (Fandub español latino)» — YouTube.
  - «Hora De Aventura Demasiado Joven (Fandub Español Latino) Clip» —
    YouTube.
  - Serie de **«Cómics de Hora de aventura (Fandub español)»**, varios
    capítulos numerados (mínimo del #2 al #7), el más reciente subido en
    **septiembre de 2024** — parece un proyecto sostenido en el tiempo, no
    un vídeo suelto.
  - «Muchachito malo | Hora de Aventura | Español latino - Fandub».
- **Fandub en TikTok, ejemplo concreto con datos**: cuenta
  **@angelon_2002_fandubs**, vídeo del especial **«Estacas» (Stakes)**, con
  la voz del **Hierofante Vampiro** hecha por un fandubber que firma como
  «Artista Galáctico»; usa las etiquetas **#fandubcomunidad #fandoblaje
  #horadeaventura** ⚠️ (visto por buscador, no pude abrir el vídeo para
  contar reproducciones — TikTok bloquea el fetch sin sesión).
- **Comparación de doblajes por TikTok**: cuenta **@whiderlin_hot** publicó
  una comparación de la canción **«Soy tu problema»** (I'm Just Your
  Problem) entre el doblaje latino y el castellano, con hashtags de ambos
  públicos (#horadeaventuralatino #horadeaventurascastellano) — muestra que
  la comunidad hispana **compara activamente** las dos versiones del
  doblaje ⚠️ (mismo problema de acceso).
- **Comunidad de traducción de canciones**: sitios de letras hechas por fans
  (no oficiales) para las canciones de Marceline en español: LyricsTranslate,
  Letras.com y Cifra Club tienen traducciones fan de **«I Remember You»** y
  **«Everything Stays»** ✅ (páginas accesibles y con texto real).
- **El precedente de organización de fans** ya citado en §12: firmas, un
  grupo de Facebook y quejas en foros (McAnime, Taringa) **para que Karla
  Falcón volviera a doblar a la Dulce Princesa** — es el ejemplo más fuerte
  y mejor documentado de la comunidad hispana defendiendo «su» doblaje ✅
  (Doblaje Wiki enlaza las fuentes originales: una petición en
  peticionpublica.es, un post de queja en la wiki de Hora de Aventura en
  español, un hilo de McAnime y un evento/grupo de Facebook).
- **Álbum oficial en español** (no es fandub, pero es la puerta de entrada a
  covers): **«Marceline Canta: Timeless Songs (Versión en Español)»**
  (2019), disponible en Spotify con «Todo se Queda» («Everything Stays») y
  otras canciones dobladas ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Hora_de_aventura)
  menciona el álbum «Marceline Canta»; existencia y catálogo confirmados en
  Spotify). Esto **facilita** que haya covers de fans, porque ya existe una
  versión oficial cantada en español sobre la que comparar.
- **No encontré** un canal de fandub en español con métricas grandes y
  verificables (suscriptores, vistas) por el bloqueo de YouTube/TikTok en
  este servidor. Recomiendo a quien repase esto con acceso sin restricciones
  buscar directamente «Hora de aventura fandub capítulo completo» en YouTube
  para encontrar el canal con más alcance.

---

## Lo mejor para la lámina

1. **La frase real de Marceline** doblada por Isabel Martiñón («Ash no
   quiere que salga con mortales»), con su tono medido (295 Hz, muy
   expresiva) — es diálogo real, no una frase inventada, y encaja con su
   actitud despreocupada.
2. **BMO fue el personaje favorito de Pendleton Ward**: un buen gancho de
   trivia para textos cortos del canal, ya que BMO tiene su propio disco
   (`biblia.md` §3.4/§8).
3. **La comunidad pidió (y logró) que Karla Falcón volviera** a la Dulce
   Princesa: muestra al servidor de doblaje que las voces latinas
   **importan al fandom**, algo muy en línea con «Sintonizando».
4. **«Oh por Glob»** (Princesa Grumosa) queda confirmado como frase 100 %
   latina — sirve de gag reconocible sin tocar a los 4 personajes
   principales del canal.
5. El **Rey Helado/Simon** es, según crítica especializada (*Vulture*), «el
   mejor personaje» de la serie por su tragedia + torpeza — vale la pena
   como personaje secundario para una lámina 2 si el dueño quiere variar del
   objeto de Marceline.

## No encontré

- ⚠️ **Encuesta oficial numérica de popularidad** de Cartoon Network (busqué
  en español e inglés). Sólo hay «Character of the Week» (2012, sólo
  Marceline) y rankings de medios (WhatCulture, Ranker) que no son de la
  cadena.
- ⚠️ **Acceso a Ranker.com** (da 401 — posible bloqueo anti-bot del proxy de
  este servidor), así que no pude confirmar el orden exacto de su ranking
  votado por el público, sólo que existe (1958 votantes a la fecha).
- ⚠️ **Vistas y fechas exactas de los fandubs de YouTube y TikTok** (§22):
  YouTube pide iniciar sesión (confirmado con `yt-dlp` y `WebFetch`, ambos
  fallaron con CAPTCHA/verificación) y TikTok no entrega datos a un fetch sin
  JavaScript. Cité título, canal y tema, no métricas.
- ⚠️ **Episodio exacto** de cada una de las 6 muestras de audio del doblaje
  (§8.3): Doblaje Wiki no indica de qué capítulo salió cada archivo, sólo
  el actor. El contenido y el tono sí son reales y verificables.
- ⚠️ **The Adventure Time Encyclopædia** (Martin Olson / Hunson Abadeer,
  Abrams/Titan Books, 2013): confirmé que existe y que trae fichas de cada
  personaje (comida, gustos, etc. en «voz» del propio personaje), pero **no
  pude leer su contenido** (la copia en Scribd no cargó). Si alguien tiene
  el libro físico o un PDF accesible, ahí hay más datos concretos de gustos
  para el punto 20.
- ⚠️ **Altura exacta** (cm) de Marceline, Finn, Jake, Dulce Princesa, BMO o
  Simon: ningún infobox de la wiki en inglés trae ese dato. No lo inventé.
- Directores de doblaje de los episodios «sin datos disponibles» (temporada
  5, hasta el ep. 130): la propia Doblaje Wiki lo deja así, no es que yo no
  buscara.

## Bitácora de búsqueda (segunda pasada, investigador de voz)

- **APIs directas** (no cuentan como «búsqueda web», pero son la base de casi
  todo este documento): `doblaje.fandom.com/es/api.php` (wikitext completo de
  «Hora de aventura», 87 135 caracteres, con `curl -A "Mozilla/5.0"` — sin
  user-agent, tanto `curl` simple como `urllib` de Python daban 403/error);
  `adventuretime.fandom.com/api.php` (wikitext de Marceline, Finn, Jake,
  Princess Bubblegum, BMO, Ice King); `horadeaventura.fandom.com/es/api.php`
  (funciona; la sugerida `adventuretimewithfinnandjake.fandom.com` del
  encargo da 404, el dominio correcto en inglés es `adventuretime.fandom.com`).
- **Audio real del doblaje**: 6 archivos `.ogg` bajados de
  `static.wikia.nocookie.net/doblaje/...` (con cabecera `Referer:
  https://www.fandom.com/`), transcritos con `herramientas/voz.py` (Whisper
  local). Sin esto, `biblia.md` no tenía ninguna frase textual de Marceline
  en el doblaje; ahora sí.
- **Búsquedas web** (español e inglés): «Óscar Flores doblaje Rey Helado
  director entrevista»; «Héctor Emmanuel Gómez BMO doblaje Hora de
  aventura»; «Adventure Time character popularity poll official fan
  favorite Cartoon Network»; «Adventure Time most popular character reddit
  poll ranking 2023 2024»; «Adventure Time Marceline fan favorite most
  popular character reddit»; «Hora de aventura fandub español cover opening
  intro YouTube»; «Hora de aventura fandub latino Marceline parodia
  TikTok»; «Everything Stays / Todo se queda cover español Marceline
  Adventure Time»; «I Remember You español cover Marceline Simon Hora de
  Aventura youtube»; «Princesa Grumosa oh por glob muletilla doblaje latino
  Lumpy Space Princess»; «Adventure Time finale Come Along With Me
  reception reddit tears music emotional analysis»; «Arturo Castañeda
  director doblaje Hora de aventura»; «Adventure Time Encyclopedia book
  official character profiles favorite food height»; «Guardian review
  Adventure Time Marceline best character DVD»; «Vulture Eric Thurm Ice
  King Best Character Adventure Time»; «Adventure Time awards Emmy Peabody
  Annie won series list».
- **Reddit vía Arctic Shift** (`arctic-shift.photon-reddit.com`):
  `subreddit=adventuretime&title=cried` — **sí existe** el subreddit
  r/adventuretime y está activo (esto corrige el «no encontré el subreddit»
  del recolector automático, que seguramente buscó mal el nombre exacto).
- **WebFetch**: `en.wikipedia.org/wiki/Marceline_the_Vampire_Queen`,
  `en.wikipedia.org/wiki/Adventure_Time` (dos veces, para premios y
  recepción crítica); falló en `ranker.com` (401), `youtube.com/watch`
  (redirige a un CAPTCHA de Google), `tiktok.com` (sin datos sin JS) y
  `scribd.com` (no cargó el documento).
- **Dailymotion** (API): ya lo había cubierto el recolector; repetí
  «Hora de aventura fandub» y «Adventure Time cover español opening» y sólo
  salieron vídeos sin relación real (0-24 vistas, mal etiquetados) — confirmo
  que Dailymotion **no tiene** contenido útil de doblaje o fandub para esta
  serie, mejor concentrar el esfuerzo en Doblaje Wiki y la wiki en inglés.
- Archivos de trabajo (fuera del repositorio, en
  `/tmp/claude-0/trabajo/14-adventure-time-voz/`): wikitext descargado
  (`doblaje_serie.json`, `en_Marceline.json`, `en_Finn.json`, `en_Jake.json`,
  `en_Princess_Bubblegum.json`, `en_BMO.json`, `en_IceKing.json`), 6 muestras
  de audio `.ogg` y sus transcripciones (`voz_*`).
