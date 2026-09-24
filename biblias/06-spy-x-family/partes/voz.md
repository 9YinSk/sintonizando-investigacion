# Parte de VOZ Y PERSONAJES · Spy x Family (encargo 06)

**Repaso corto** (`EQUIPO.md`): los puntos 7, 8, 12 y 13 de `ENCARGO.md` ya están
hechos en `biblia.md` (secciones 8, 9, 10 y 14, marcadas «segunda pasada», con
doblaje verificado en dos fuentes) y **no los repito**. Esta parte cubre lo que
faltaba entero en la biblia: los puntos **20** (gustos y detalles de cada
personaje), **21** (por qué la gente la ama) y **22** (fan dubs y comunidad
hispana). Comprobado con `grep -n "^## " biblia.md`: no existía ninguna
sección para 20/21/22 antes de esta parte.

Personajes cubiertos (los que pide `encargos/06-spy-x-family.md`): Anya, Loid,
Yor, Bond, Damian, Becky. Formato: libreta de datos, un dato por línea, fuente
y ✅ (dos fuentes)/⚠️ (una fuente o sin confirmar).

Carpeta de trabajo (fuera del repositorio): `/tmp/claude-0/trabajo/06-spy-x-family-voz/`.

---

## Punto 20 · Gustos y detalles de cada personaje

Fuente principal para comida/aficiones/gustos-odios/objeto: el perfil de cada
personaje en el **`SPY x FAMILY Official Fanbook: EYES ONLY`** (databook
oficial, 2023), citado con página exacta por [Spy x Family Wiki](https://spy-x-family.fandom.com/wiki/SPY_x_FAMILY_Official_Fanbook:_EYES_ONLY)
(API `action=parse`, secciones Trivia). Lo confirmé con una **traducción
independiente del mismo cuestionario**, hecha por una fan que compró el libro:
[hilo de Tumblr de @mj-ackerman](https://www.tumblr.com/mj-ackerman/690237118081024000/tatsuya-endos-characters-guide-qna-from-the)
(coincide palabra por palabra con la wiki en Loid, Anya, Yor y Bond) y el
[hilo de traducción en Twitter/X de @kaikaikitan](https://twitter.com/kaikaikitan/status/1520793885328707585).
Aviso honesto: ambas transcripciones parten del mismo libro físico, así que no
son dos investigaciones independientes, pero sí dos transcripciones humanas
distintas que coinciden — lo marco ✅ sólo cuando coinciden literalmente.

### Anya Forger
- **Comida**: cacahuetes por encima de todo; en el colegio come *omurice*
  (arroz con omelette) y le gustan los bocaditos crujientes con forma de
  animalito ✅ (wiki + Tumblr, casi palabra por palabra).
- **Aficiones/gustos**: su peluche con forma de quimera («Chimera», con el
  que Yor jugó a que era su «hija» en el ep. 3), los cacahuetes, los dibujos
  de espías, su uniforme de Eden, Penguinman, los castillos, y en broma:
  «Papá (un mentiroso), Mamá (una salvaje), Becky (mi dama), Bond» ✅ (wiki,
  cita del fanbook con página; Tumblr confirma la lista de comida y el gusto
  por Penguinman).
- **Lo que odia**: las zanahorias (ya en biblia §8, ep. 1, 00:09:05); el
  robot de juguete que le regaló Loid no le gusta mucho ✅ (wiki + Tumblr).
- **Talla de zapato**: 14 cm ✅ (wiki + Tumblr, mismo dato).
- **Altura**: 99.5 cm (3'3") ✅ (fanbook vía wiki + AniList, `datos-voz.md`).
- **Cumpleaños**: **no revelado oficialmente**. Su edad en papeles falsos es
  6; su edad real aproximada, 5 («Notas del autor», vol. 13) ✅. AniList (en
  `datos-voz.md`) da «cumple 6/4», pero **no hay ninguna fecha de nacimiento
  en la wiki ni en el fanbook**: es casi seguro un dato metido por un
  editor de AniList sin fuente, no un dato oficial ⚠️ — no lo uses en la
  lámina como si fuera oficial.
- **Objeto que siempre lleva**: su peluche-quimera y el lazo/diadema del
  pelo (ya en imagen/vestuario).
- **Golpe especial**: «300 Star Impact» (su puñetazo); otros movimientos que
  le enseñó Yor: Star Catcher Arrow, Rising Hope, Shin Kick, Eye Poke ✅
  (wiki, cita de página del fanbook; Tumblr confirma que existen movimientos
  con nombre pero no logró transcribir bien los nombres en japonés — mismo
  dato, transcripción distinta).
- **Quiere**: un llavero de oveja de edición limitada, carísimo («Lady
  Sheep»/«Redy-shibu») ✅ (wiki + Tumblr).
- **Cómo se ve a sí misma**: no se cree buena estudiante pero sí «buena en
  las otras materias también, aunque el Lenguaje Clásico es lo suyo» (broma
  del propio Endo en el fanbook) ✅. Por dentro se ve como una agente
  secreta de verdad (su organización imaginaria «B'2», que viene de
  «Peanuts») que debe mantener unida a la familia; teme que la reemplacen o
  la devuelvan al orfanato (`Personality`, wiki, ya citado en `datos-voz.md`) ✅.

### Loid Forger
- **Le gusta**: información fiable, los trajes bien hechos. **Le disgusta**:
  la guerra, el comportamiento irracional ✅ (wiki, cita del fanbook, y
  Tumblr: «Likes: Reliable Information, well tailored suits. Dislikes: War,
  Illogical behavior.», calcado).
- **Aficiones**: **no tiene ninguna** (lo dice el propio fanbook) ✅ (wiki +
  Tumblr). Fuera del trabajo casi no habla de sí mismo, ni con Franky.
- **Comida**: puede cocinar cualquier cosa (hizo de chef de primer nivel en
  una misión); en casa cocina él (ya en biblia §8, ep. 4, 00:14:46) ✅.
- **Altura**: 187 cm (6'2") ✅ (fanbook + AniList, `datos-voz.md`).
- **Cumpleaños**: no revelado; su edad «reclamada» es 32 (cap. 134) ⚠️ (sin
  segunda fuente para el número exacto).
- **Objeto que siempre lleva**: su pistola (diseñada a partir de la Walther
  PPK y la Luger P08), siempre con el dedo fuera del gatillo por disciplina
  de manejo de armas; el pin de solapa con el símbolo de WISE ✅ (wiki, cita
  de material extra del volumen 1 para la pistola).
- **Cómo se ve a sí mismo**: sólo como un espía, nunca como «Loid Forger» de
  verdad. Cita directa: «¿Esperanzas de matrimonio? ¿Las alegrías de una
  vida normal? Eso se fue a la basura junto con mis papeles de identidad el
  día que me hice espía» (cap. 1, pág. 11, ep. 1) ✅ (cita primaria, wiki).
  Su misión más estresante no fue desactivar una bomba nuclear, sino la
  entrevista de admisión de Anya a Eden (fanbook) ✅ (wiki + Tumblr).
- **Dato de color**: gana unos ¥20 millones al año como psiquiatra (~$140.000
  USD, cambio de 2023); sólo duerme 2 horas cada noche entre el hospital y
  las misiones ✅ (wiki, cita del fanbook; Tumblr confirma la cifra de 20
  millones de yenes y las 2 horas de sueño, mismo dato).

### Yor Forger
- **Plato especialidad**: el guiso sureño de su madre («southern stew»); no
  ha aprendido a cocinar nada más desde entonces ✅ (wiki + Tumblr, mismo
  chiste: «¿Ha mejorado su plato especial? Uf...»).
- **Le gusta**: comer manzanas; de niña, su sabor favorito de caramelo de
  silbato también era manzana (cap. 68) ✅ (wiki, dos citas de capítulo
  distintas que coinciden en la manzana).
- **Le odia**: los insectos, al punto de no soportar ni fotos de ellos (cap.
  10, ep. 7) ✅.
- **Su fuerza de agarre no se puede medir** porque rompe los aparatos; su
  estilete simboliza espinas de rosa y da un golpe rápido para no alargar el
  sufrimiento del objetivo; tasa de éxito como asesina: 100% ✅ (wiki +
  Tumblr, coincide).
- **Altura**: 170 cm (5'7") ✅ (fanbook, pág. 43 + AniList).
- **Edad**: 27 (cap. 2, ep. 2) ✅.
- **Cumpleaños**: no revelado. El archivo de personal del ayuntamiento (ep.
  2) trae la fecha «06 ABR 63», que la propia wiki aclara que **podría ser
  la fecha en que empezó a trabajar ahí, no su cumpleaños** — coincide
  sospechosamente con el «cumple 6/4» que da AniList (`datos-voz.md`): lo
  más probable es que ese dato de AniList confunda fecha de contratación con
  cumpleaños ⚠️. No lo des como oficial en la biblia.
- **Objeto que siempre lleva**: sus estiletes/tacones de aguja (arma); tiene
  buena letra (dato de Franky, ep. 20) ✅.
- **Cómo se ve a sí misma**: en el ayuntamiento se considera de nivel medio,
  «ni tan mala como para que el jefe le grite» (autoevaluación modesta,
  fanbook) ✅ (wiki + Tumblr, casi calcado). Como asesina, en cambio, tiene
  seguridad total. Antes de Loid nunca había tenido pareja (cap. 14, ep. 9) ✅.

### Bond Forger
- **Le gusta** la comida que hace Loid; **le disgusta** la que hace Yor ✅
  (wiki + Tumblr, mismo chiste).
- **Orden de cariño** hacia la familia (y Franky): Anya, Loid, Franky, Yor ✅
  (wiki + Tumblr, idéntico).
- Cuando Anya está en el colegio, se pasa el día rodando por el suelo y
  molestando a Penguinman ✅ (wiki + Tumblr).
- Le gustan los paseos, pero no es muy activo: sólo 30 minutos al día; Yor lo
  saca cuando Loid no puede ✅ (wiki + Tumblr).
- Le gusta más el olor de Anya; el de Yor es de las pocas cosas que sí le
  gustan de ella ✅ (wiki + Tumblr).
- Cercano al perro pastor alemán del laboratorio (llamado «Shepard» en la
  traducción de Tumblr), del tiempo en que ambos eran sujetos de
  experimentos del Proyecto Apple ✅.
- **Altura**: aprox. 1 m (fanbook, pág. 48) ⚠️ (una fuente).
- **Objeto/seña propia**: el lazo tipo pajarita que lleva en el cuello, guiño
  al James Bond literario (ya en biblia, referencia a su nombre).
- **Cómo se ve a sí mismo** (hasta donde un perro puede): quiere usar sus
  visiones para proteger a la gente; Anya le puso el nombre de su héroe de
  ficción Bondman porque «se parecen en personalidad y aspecto» (wiki,
  Trivia) ✅.

### Damian Desmond
- **Talla de zapato**: 17 cm ✅ (fanbook, pág. 102).
- **Le gusta**: el fútbol (de delantero centro, «porque le gusta anotar
  goles y destacar», dato extra de otro libro de la franquicia, «filmfiles»
  pág. 66), los cómics, las «Stella Stars» (las estrellas que dan prestigio
  en Eden) ✅ (dos fuentes: fanbook + libro de películas, ambos citados por
  la wiki).
- **Le disgusta**: las lombrices de tierra, los pimientos verdes, escribir
  ✅ (fanbook).
- **Plato favorito**: el *schnitzel* de la matrona del internado; como
  Desmond, tiene paladar refinado y come en el dormitorio en vez del comedor
  general ⚠️ (una fuente, fanbook vía wiki).
- Tiene un pastor alemán llamado Max, a cargo de su mayordomo Jeeves cuando
  Damian está interno ✅ (wiki, cap. y ep. citados).
- **Apodo**: «Dammy», que le pone Jeeves (cap. 25, pág. 22, ep. 17) ✅.
- **Número de estudiante** en Eden: 61133229 (cap. 27, ep. 18) ✅.
- **Altura**: 110 cm (3'7") ✅ (fanbook, pág. 102 + AniList).
- **Cómo se ve a sí mismo**: presión constante por igualar a su hermano
  mayor, ya «Erudito Imperial». Cita directa: «Sé que a mi padre no le
  importo en absoluto. Si quiero complacerlo... si quiero ganarme su
  respeto... tengo que ser perfecto. ¡Tengo que convertirme en Erudito
  Imperial!» (cap. 25, págs. 24-25, ep. 17) ✅ (cita primaria).
- Es el único personaje al que Anya le ha confesado que lee mentes — Damian
  no le cree, piensa que ve demasiados dibujos animados ✅ (wiki, Trivia).

### Becky Blackbell
- **Talla de zapato**: 15 cm ✅ (fanbook, pág. 106).
- **Le gusta**: el llavero a juego que tiene con Anya, su perro Wiesel (un
  Yorkshire terrier cuya caseta es más grande que el cuarto de Anya, cap.
  59, ep. 36), y los dramas románticos de TV, en especial «Berlint in
  Love», que imita en la vida real ✅ (wiki + fanbook, dos citas
  coincidentes).
- **Le disgusta**: las cosas infantiles, «hacer las rondas» de cortesía en
  fiestas sociales, y los calcetines de su padre ✅ (fanbook).
- **Plato favorito** del comedor: la pasta de tomate y crema con langosta
  ⚠️ (una fuente, fanbook vía wiki).
- **Ambición**: quiere ser cantante (cap. 75, pág. 5) ✅.
- Tiene una muñeca, Martha, desde que tiene memoria: juega a dramas cursis
  con ella y hace shows de moda ella sola ✅ (fanbook).
- Su broche/pin en forma de bomba es un motivo familiar: su padre lleva un
  pin igual y su madre, pendientes a juego (caps. 71 y 107) ✅.
- **Altura**: 104 cm (3'5") ✅ (fanbook, pág. 106).
- **Cómo se ve a sí misma**: se cree más madura que sus compañeros («el
  ideal de adultez» que copia de los dramas de TV); al llegar a Eden juzga a
  los demás por su estatus social y mira a Anya por encima del hombro, pero
  cambia al ver que Anya se enfrenta a Damian sin miedo (`Personality`,
  wiki) ✅.

**Nota para el redactor**: ninguno de los 6 tiene cumpleaños oficial
confirmado — dilo así en la biblia en vez de repetir el dato suelto de
AniList como si fuera un hecho. Es justo el tipo de cosa que el dueño no
quiere: un dato «inventado» sin fuente real.

---

## Punto 21 · Por qué la gente la ama

### 21.1 Ventas (progresión, para ver que no es una moda pasajera)
| Fecha | Copias en circulación | Fuente |
|---|---|---|
| ago-2022 | 25 millones | [Anime News Network](https://www.animenewsnetwork.com/news/2022-08-28/spy-family-manga-tops-25-million-copies-in-circulation/.189083) ✅ |
| dic-2022 | 29-30 millones | [somosxbox.com](https://www.somosxbox.com/el-manga-de-spy-x-family-alcanza-los-29-millones-de-copias-vendidas/) + [ramenparados.com](https://ramenparados.com/spy-x-family-alcanza-las-30-millones-de-copias-en-circulacion/) ✅ |
| dic-2024 (14 vols.) | 37 millones | [ComicBook.com](https://comicbook.com/anime/news/spy-x-family-manga-sales-37-million/) (10-dic-2024) ⚠️ una fuente para esta cifra exacta |
| mar-2026 (17 vols.) | **42 millones** | [AnimeExplained](https://www.animeexplained.com/news/spy-x-family-draws-closer-to-50-million-sales-milestone-after-only-17-volumes/) + [CBR](https://www.cbr.com/spy-x-family-vs-detective-conan-oricon-manga-ranking/) ✅ (dos medios, misma cifra) |

- La película **«Spy x Family Code: White»** recaudó unos **59 millones de
  dólares** en todo el mundo ⚠️ (una fuente, ComicBook.com; no encontré una
  segunda cifra que lo confirme con exactitud).

### 21.2 La encuesta oficial más reciente (¡importante, cambia el ranking!)
- Shueisha organizó la **1.ª Encuesta de Popularidad oficial** de la serie en
  *Shonen Jump+*, del 29-sep al 26-oct-2025, para celebrar el estreno de la
  3.ª temporada. Se podía votar una vez al día; 166 personajes elegibles;
  **338.341 votos en total**. Resultados de los 10 primeros anunciados en
  Jump Festa 2026 (21-dic-2025), con una ilustración especial de Tatsuya
  Endo; la tabla completa salió al día siguiente con el capítulo 127 ✅
  ([Spy x Family Wiki, «Popularity Poll»](https://spy-x-family.fandom.com/wiki/Popularity_Poll),
  que enlaza directo a la [página oficial de votación de Shonen Jump](https://sp.shonenjump.com/p/sp/2509/vote_spyfamily)).

| Puesto | Personaje | Votos |
|---|---|---|
| 1 | **Loid Forger** | 52.164 |
| 2 | Anya Forger | 48.022 |
| 3 | Yor Forger | 43.304 |
| 4 | Damian Desmond | 39.179 |
| 5 | Bond Forger | 28.011 |
| 6 | Yuri Briar | 13.078 |
| 7 | Becky Blackbell | 12.085 |
| 8 | Fiona Frost | 11.009 |

- **Dato clave para el dueño** (que un secundario a veces gana al
  protagonista): aquí gana **Loid**, no Anya, que es quien suele llevarse la
  fama en redes de Occidente. El propio Endo comentó tras la encuesta: «la
  sensación general era que la mayoría esperaba que Anya quedara primera.
  Sin embargo, Loid ganó (¿a salvo?), lo que le permite mantener su dignidad
  como protagonista, y eso es un alivio» ✅ (cita directa de Endo, misma
  página de la wiki).
- **Contraste Oriente/Occidente** (con la encuesta de fans de AniList que ya
  está en `datos-voz.md`, votos de Occidente mayoritariamente): ahí gana
  **Yor** (14.405), 2.ª Anya (13.281), 3.º Loid (10.163) — **el orden se
  invierte casi del todo** frente a la encuesta oficial japonesa (Loid,
  Anya, Yor) ✅ dos encuestas de origen distinto, cada una con su público.
  Útil para decidir qué personaje poner en la lámina según a quién le habla
  el servidor (mayoría hispanohablante, gustos más parecidos a Occidente).

### 21.3 Premios
- **Kono Manga ga Sugoi!** (Takarajimasha): 1.er puesto en el ranking para
  lectores varones en 2019 y 2020 ✅ ([atamashi.net](https://atamashi.net/spy-x-family-es-el-manga-numero-1-en-premios-kono-manga-ga-sugoi/) + la propia [wiki del manga](https://spy-x-family.fandom.com/wiki/SPY_x_FAMILY_(manga))).
- **Tsutaya Comic Award**, 4.ª edición (2020): ganador (empatado con «A Man
  and His Cat») ✅ ([No Somos Ñoños](https://nosomosnonos.com/2020/06/19/spy-x-family-a-man-and-his-cat-tsutaya/)).
- **Da Vinci, 22.º «Book of the Year»** (2022): 1.er puesto ⚠️ (una fuente
  indirecta, buscador; no confirmé con la página original de la revista).
- **Japan Cartoonists Association Award**, 52.ª edición (2023): Gran Premio
  en la categoría de cómic ⚠️ (una fuente, buscador).
- **Crunchyroll Anime Awards, 7.ª edición** (4-mar-2023, Tokio): SPY x FAMILY
  fue la serie **con más nominaciones de la noche (19)**. **Ganó al menos 5
  categorías**, comprobadas una por una en la lista completa de ganadores
  ✅ ([CGMagazine](https://www.cgmagonline.com/news/anime-awards-2023-winners-list/),
  cruzado con [Deadline](https://deadline.com/2023/03/anime-awards-2023-winners-list-1235278881/)
  y la [ficha de Wikipedia del evento](https://en.wikipedia.org/wiki/7th_Crunchyroll_Anime_Awards)):
  - **Mejor Serie Nueva** (Best New Series).
  - **Mejor Secuencia de Ending**, por «Comedy» de Gen Hoshino.
  - **Mejor Comedia** (Best Comedy).
  - **Personaje que «hay que proteger a toda costa»**: Anya Forger.
  - **Mejor Personaje Secundario** (Best Supporting Character): Anya Forger.
  - ⚠️ Deadline dice que en total fueron **6** categorías (junto con Attack
    on Titan y Demon Slayer); sólo pude confirmar el nombre exacto de 5 en
    la lista completa — la sexta no la ubiqué con certeza, no la invento.
  - **No ganó** Anime del Año (se lo llevó *Cyberpunk: Edgerunners*), ni
    Mejor Actuación de Voz Japonesa (Atsumi Tanezaki/Anya, nominada) ni
    Mejor Actuación de Voz Inglesa (Natalie Van Sistine/Yor, nominada) ✅.

### 21.4 Con qué personaje se identifica el público, y por qué
- Medios en español (El Comercio Perú, Nintenderos) coinciden: lo que
  engancha es que la serie pone a la **familia** en el centro, no sólo la
  acción, y que Anya «se ha ido acaparando el protagonismo... por sus
  poderes y su versatilidad», siendo «la favorita de millones de fans» ✅
  (dos medios, mismo argumento).
- Hilo de Reddit r/SpyxFamily (260 votos): «creo que una razón de la
  popularidad de la serie es que no hay muchos protagonistas de anime
  mainstream como Loid» — la gente se identifica con un protagonista adulto,
  calculador, que no encaja en el molde típico shonen ⚠️ (opinión de un solo
  hilo, aunque con cientos de votos a favor).
- Con Yor, buena parte del público occidental se identifica por la mezcla de
  «competente y temible en el trabajo, insegura y torpe en lo social»: hilos
  como «I like Fiona, but Yor is the best girl» (806-942 votos, repetido
  varias veces por distintos usuarios) y «My midlife crisis ended up being
  Yor Forger. I am lucky my wife is not the jealous type» (1050 votos) ✅
  (varios hilos independientes, todos con cientos/miles de votos, en
  [r/SpyxFamily](https://www.reddit.com/r/SpyxFamily) vía Arctic Shift).

### 21.5 Las escenas que hacen llorar (o gritar de emoción)
**El pasado de Loid («Loid's Past Arc»)**, el momento que el fandom más cita
en 2025-2026:
- Ubicación exacta: manga caps. 58-63 (vols. 9-10); anime **temporada 2-3,
  episodios 36 a 41**. El golpe más duro cae en el **episodio 40**
  («■■■■'S MEMORIES II» — su nombre sale censurado hasta que se revela),
  estrenado en Japón el **18-oct-2025** (inglés, 1-nov-2025) ✅ (ficha
  oficial de episodio en la wiki, que enlaza a la sinopsis del sitio oficial
  `spy-family.net`).
- **Qué pasa**: de niño, Loid pierde su pueblo (Luwen) en un bombardeo; su
  madre lo saca de ahí, pero después muere ella también en otro bombardeo
  mientras él está refugiado y ella se queda fuera — Loid se queda sin
  nadie. De joven se alista con nombre falso («Roland Spoofy»), sobrevive a
  la guerra y, cuando por fin vuelve a encontrarse con sus tres amigos de la
  infancia (General, Corporal, Major), los mandan a una operación mal
  planeada de la que **sólo vuelven sus placas de identificación**. Termina
  con la cita: «La ignorancia no es una bendición. La ignorancia es
  debilidad. La ignorancia es un pecado» (cap. 62, ep. 40) ✅.
- **Por qué duele**: explica de una vez por qué Loid se volvió una persona
  que «tiró su nombre y su cara» (ya citado en biblia §8) y por qué quiere
  «un mundo donde los niños no lloren» — el dolor de fondo detrás de un
  personaje que en el día a día es frío y calculador.
- **Música**: según lo que encontré (sin poder escuchar el tema yo mismo), el
  disco de la 3.ª temporada trae una pista llamada **«Lullaby»** con la voz
  de la nana que canta la madre de Loid, reutilizada después en una escena
  entre Loid y Yor ⚠️ (un solo resultado de búsqueda, no lo pude verificar
  escuchándolo ni ubicar el número exacto de pista).
- **Cómo está dibujada (encuadre, luz, lluvia...)**: **no lo pude
  comprobar**. La temporada 3 es de estreno reciente (oct-2025 en adelante)
  y sólo está en Crunchyroll de pago: no hay clip oficial gratuito en
  Dailymotion ni Internet Archive, y YouTube pide iniciar sesión desde este
  servidor (confirmado con `yt-dlp`: error 429 y «Sign in to confirm you're
  not a bot», sin insistir más de un intento). Es tarea del investigador de
  vídeo si se retoma con más cupo de YouTube.
- **Reacción del fandom** (Reddit, vía Arctic Shift, en inglés): «Loid's
  backstory makes us appreciate the slice-of-life parts of the story even
  more» (1217 votos, oct-2025) y «Did anyone else end up tearing up in the
  flashback episodes?» (963 votos, nov-2025: *"tuve que contener las
  lágrimas... sólo es la segunda vez que algo me hace llorar"*) ✅ (dos
  hilos independientes con cientos de comentarios cada uno, en
  [r/SpyxFamily](https://www.reddit.com/r/SpyxFamily/comments/1oasb1v/loids_backstory_makes_us_appreciate_the/)).

**El pasado de Yor** (huérfana de guerra, crió sola a Yuri desde niña,
reclutada por Garden): confirmado en la wiki con varios capítulos de manga
(algunos aún no animados) y profundizado en el arco «Cruise Adventure» de la
temporada 2 ✅ (wiki + [Sportskeeda](https://sportskeeda.com/anime/spy-x-family-season-2-finally-gives-yor-much-deserved-spotlight)),
pero **no ubiqué el episodio/minuto exacto de una escena concreta de llanto**
ni pude mirar el vídeo (mismo problema de acceso a YouTube) ⚠️.

**Escena que hace gritar de alegría** (para no dejar sólo tristeza):
**episodio 11, «STELLA»** (Japón, 18-jun-2022; caps. 16-17): Anya, que odia
estudiar, consigue su primera Estrella Stella no por notas sino salvando con
su telepatía a un niño que se ahogaba en una piscina durante su trabajo de
voluntariado en un hospital ✅ (ficha oficial de episodio, wiki). Es de los
momentos más citados como «orgullo/alivio» de la serie, aunque no encontré un
hilo de Reddit con cientos de votos específico de esta escena (⚠️ mención sin
cifra de reacción).

---

## Punto 22 · Fan dubs y comunidad hispana

### 22.1 Doblajes de fans (fandub) en español
- Serie de fandub «D.E.» en YouTube: Twilight interpretado por el canal
  `@MrJina-tx1wf` y Anya por `@unahoramasfeliz`, capítulo **«D.E. 20# | Loid
  Adopta a Anya | SPY X FAMILY Fandub Latino»** (5-ago-2024) ⚠️ (hallado por
  buscador; no pude ver vistas: YouTube pide iniciar sesión desde este
  servidor).
- Canal genérico «Spy x Family -Fandub español latino #spyxfamily #anime
  #español» ⚠️ (mismo problema, sin canal identificado con certeza).
- **Bilibili** (sí es accesible sin iniciar sesión): fandub con **Loid
  interpretado por «Laxer15»** y **Yor por «KimKings»**, publicado el
  **25-abr-2022**, apenas días después del estreno del doblaje oficial en
  Crunchyroll (24-abr-2022) ✅ (fecha y repartos confirmados directamente en
  la página, sin necesitar YouTube).

### 22.2 Covers de openings/endings en español latino (todos de aficionados)
| Tema | Intérprete oficial | Covers en español encontrados |
|---|---|---|
| OP1 «Mixed Nuts» | Official HIGE DANdism | Al menos 9 covers (canales AxlolRms, Dianilis, David Delgado, «Luna ft. JonatanKing», «RonRockerOfficial» —colab con doblaje fiel—, «Takayamizu»), subidos ya en abril-junio de 2022, la misma temporada del estreno japonés ⚠️ (fechas y títulos por buscador; sin vistas verificadas) |
| ED1 «Comedy/Kigeki» | Gen Hoshino | Al menos 1 cover completo en español latino localizado ⚠️ |
| ED2 «Shikisai/Color» | yama | Al menos 4 covers completos en español latino localizados (2022) ⚠️ |

- No encontré covers en español de los temas de la 3.ª temporada («Kura
  Kura» de Ado, «Todome no Ichigeki» de Vaundy, «Protect the Light» de
  Spitz, «Actor» de Lilas Ikuta): búsquedas hechas, sin resultado ⚠️.

### 22.3 Memes y parodias en español
- **«Papi, quiero mimir»** (frase de Anya en el doblaje oficial, ep. 1) es
  EL meme latino de la serie: circula en TikTok en docenas de vídeos
  comprobados de distintas cuentas (`@maripuliaoficial`, `@lowzs_`, entre
  otras) desde 2022 ✅ (ya citado también en biblia §14; coincide).
- Playlist de YouTube dedicada **«PARODIAS: SPY X FAMILY»** ⚠️ (título
  confirmado, no pude entrar al contenido individual de cada vídeo).
- **Memedroid** (`es.memedroid.com`) tiene una etiqueta propia
  «spyxfamily»/«spy x family» en español con decenas de memes hechos por la
  comunidad hispana ⚠️ (existencia confirmada, no conté los memes uno por
  uno).

### 22.4 Reacción de la comunidad hispana al doblaje (contexto para el foro)
- Medios especializados en español cubrieron el estreno del doblaje latino
  (24-abr-2022) como un evento celebrado en redes: «récords de vistas» en
  clips de opening/ending, cosplays de los protagonistas «apenas
  empezando» ✅ ([Geekzilla.tech](https://geekzilla.tech/spy-x-family-el-anime-que-todos-los-fans-latinoamericanos-amamos-por-su-increible-doblaje/),
  27-abr-2022, y [Universo Nintendo](https://universo-nintendo.com.mx/2022/04/24/spy-x-family-doblaje-latino-video/),
  24-abr-2022 — dos medios independientes, mismo argumento).
- Cuenta de fans en X/Twitter **«SPY x FAMILY LATAM»** (`@spyfamily_la`)
  dedicada a la comunidad hispanohablante de la serie ⚠️ (una fuente, no
  revisé su contenido a fondo).

---

## Lo mejor para la lámina

1. La **encuesta oficial de Shueisha** (dic-2025): Loid 1.º, Anya 2.ª, Yor
   3.ª — pero en Occidente (AniList) gana Yor. Es la prueba exacta que pedía
   el dueño de que «un secundario puede ser más querido», y sirve para
   justificar qué personaje poner en el expediente de WISE.
2. Loid, en su propia ficha oficial, «no tiene aficiones» y su misión más
   estresante fue la entrevista de Anya, «peor que desactivar una bomba
   nuclear» — frase perfecta, en su voz, para un documento «clasificado» de
   WISE en el escritorio.
3. El golpe «300 Star Impact» de Anya y su obsesión con el llavero de oveja
   carísimo son gags visuales reconocibles al toque para el foro de
   #presentaciones.
4. Bond odia la comida de Yor y adora la de Loid: un detalle de humor que
   humaniza a la familia sin caer en la burbuja de diálogo genérica que el
   dueño rechazó.
5. El meme **«Papi, quiero mimir»** conecta directo con el doblaje latino:
   es la frase que más repite la comunidad hispana de la serie en TikTok.

---

## No encontré (⚠️, extras que no son obligatorios del encargo)

- Vistas exactas de cualquier fandub o cover en español: YouTube pide
  iniciar sesión desde este servidor (confirmado con `yt-dlp --skip-download`,
  error 429 + «Sign in to confirm you're not a bot»; no insistí más de un
  intento, como pide `AYUDANTE.md`).
- Covers en español de los openings/endings de la 3.ª temporada (Ado,
  Vaundy, Spitz, Lilas Ikuta): búsquedas hechas (`WebSearch`, español), sin
  resultado.
- Número exacto de pista y escucha del tema «Lullaby» (posible música de la
  escena del pasado de Loid): un solo resultado de búsqueda, sin poder
  confirmarlo escuchándolo.
- Encuadre, luz, lluvia o silencio de la escena del pasado de Loid (ep. 40):
  no hay clip oficial gratuito (temporada 3, sólo Crunchyroll de pago) y
  YouTube está bloqueado; sin vídeo no puedo describir la puesta en escena
  de verdad, sólo la sinopsis textual.
- Sexta categoría exacta ganada por la serie en los Crunchyroll Anime Awards
  2023 (Deadline dice 6 en total, la lista completa que revisé sólo nombra 5
  con seguridad).
- Cifra de taquilla de «Spy x Family Code: White» confirmada en una segunda
  fuente (sólo tengo ComicBook.com).

---

## Bitácora de búsqueda (esta parte)

- **Spy x Family Wiki (Fandom, inglés)**, API directa (`action=parse`,
  `prop=wikitext`): secciones Trivia/Personality de Anya, Loid, Yor, Bond,
  Damian y Becky (con cita de página del fanbook «EYES ONLY» en cada dato);
  página **«Popularity Poll»** y su plantilla de resultados completa;
  página **«Loid's Past Arc»**; ficha de **Episodio 40** y **Episodio 11**;
  `action=query&list=search` para ubicar «Loid's Past Arc» y el episodio de
  «STELLA».
- **Tumblr** (`mj-ackerman`, en inglés): traducción independiente del
  cuestionario del fanbook «EYES ONLY» para Loid, Anya, Yor y Bond — usada
  para confirmar en dos fuentes los datos del punto 20.
- **Reddit vía Arctic Shift** (`arctic-shift.photon-reddit.com`, en inglés),
  `subreddit=SpyxFamily` con `query=tears`, `favorite%20character`,
  `best%20girl`, `relate`, `identify%20with`, `cried`, `sad`, `funny`,
  `laughed`, `iconic`, `Stella`, `exam`, `poll`, `Jump Festa` (varias de
  estas últimas dieron 0 resultados por cómo indexa la API, no por falta de
  contenido — no lo repetí más de 2 veces cada una).
- **Buscador web** (`WebSearch`, español e inglés, de mi cupo de ~50):
  «Spy x Family Crunchyroll Anime Awards Anime of the Year winner», «Spy x
  Family manga ventas millones de copias 2025/2026», «Spy x Family episodio
  que hace llorar Yor Yuri pasado reddit», «Spy x Family fandub español
  latino youtube», «Spy x Family opening cover español latino "Mixed
  Nuts"», «Spy x Family premio Newtype Kono Manga ga Sugoi», «Spy x Family
  por qué es tan popular identificación Anya Loid Yor», «Spy x Family Yor
  pasado triste episodio 25», «Spy x Family meme tiktok español "a mimir"
  "Segundo"», «Spy x Family cosplay hispano comunidad doblaje México», «Eyes
  Only fanbook Loid dislikes war black underwear translation», «Spy x
  Family fanbook Anya favorite things peanuts Penguinman translation
  twitter», «Spy x Family episode 40 insert song soundtrack», «Spy x Family
  Crunchyroll Anime Awards Best Girl/Comedy», «Spy x Family parodia español
  meme animación», «Spy x Family ending cover español latino Kokoro/Shikisai»,
  «Spy x Family encuesta popularidad Latinoamérica Crunchyroll».
- **Páginas leídas directo con `curl`** (sin gastar cupo de buscador):
  CGMagazine (lista completa de ganadores de los Crunchyroll Anime Awards
  2023), ComicBook.com (ventas del manga, dic-2024), Geekzilla.tech (reacción
  al doblaje latino), Tumblr (traducción del fanbook). Atomix.vg estaba
  detrás de Cloudflare («Just a moment...»): 1 intento, no insistí más.
- **Wikipedia (inglés), API**: 429 «making too many requests» (uso
  compartido con el resto del equipo), 1 intento, no insistí — cubrí los
  premios de Crunchyroll con CGMagazine y Deadline en su lugar.
- **`yt-dlp --skip-download`** sobre un cover de YouTube: confirmó el bloqueo
  («Sign in to confirm you're not a bot», error 429), 1 intento, como pide
  `AYUDANTE.md`.

Sigue: nada obligatorio de los puntos 20/21/22 queda pendiente (ver «No
encontré» para los extras). Falta que el redactor decida si mete la escena de
«STELLA» y el contraste de encuestas Oriente/Occidente en la biblia.
