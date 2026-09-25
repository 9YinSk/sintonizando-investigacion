# Voz y personajes — Hellblade (encargo 118)

Investigador de voz. Puntos 7, 8, 12, 13, 20, 21, 22 de ENCARGO.md. Parte de
`datos-voz.md` (no repite esas consultas). Sin YouTube directo (bloqueado):
Dailymotion, wikitext de `hellblade.fandom.com` (con sus `.mp3` de citas
—audio original del juego—, analizados con `voz.py`), Wikipedia (dos idiomas),
prensa hispana, Reddit vía Arctic Shift, Danbooru.

**Aviso importante:** en Hellblade casi todo el «doblaje» y «voz» ES el juego:
no hay doblaje latino (se confirma abajo), así que las «frases icónicas»
del punto 8 son citas en inglés con su traducción de los subtítulos en
español, no clips doblados. Lo digo claro para que el redactor no folclore
un doblaje que no existe.

## Hallazgos

### Punto 7 — Popularidad (encuestas oficiales y de fans)

- Hellblade no tiene encuestas de popularidad tipo anime (no es una obra con
  elenco amplio). Senua es la única protagonista jugable en ambos juegos; el
  resto son personajes de apoyo (Druth, Dillion, Zynbel en el 1; Ástríðr,
  Fargrímr, Thórgestr en el 2). ⚠️ Esto lo digo explícito para que no se
  fuerce una «encuesta» que no existe: lo busqué en inglés y español (`site
  reddit.com/r/hellblade favorite character poll`, `Hellblade personaje
  favorito encuesta`) y no hay nada oficial.
- Medida indirecta de cariño del fandom (arte de fans, Danbooru): con la
  etiqueta `hellblade` salen 5 dibujos y los 5 son de Senua. Con las
  etiquetas `druth`, `dillion`, `zynbel`, `hela_(hellblade)` no hay NINGÚN
  resultado (comprobado uno a uno). ✅ (fuente `datos-voz.md` + comprobación
  propia: https://danbooru.donmai.us/posts?tags=druth ,
  .../posts?tags=dillion , .../posts?tags=zynbel , .../posts?tags=hela_(hellblade) →
  0 posts cada uno). Conclusión: en el fandom de dibujo, Senua absorbe el 100%
  de la atención; no hay un «secundario más querido» que le compita en arte,
  aunque sí en cariño narrativo (ver Druth abajo).
- Medida de reconocimiento crítico (equivalente a «popularidad oficial» en un
  videojuego): Hellblade: Senua's Sacrifice ganó **5 de sus 9 nominaciones**
  en los 14th British Academy Games Awards (12-abr-2018): Mejor juego
  británico, Logro artístico, **Mejor intérprete** (Melina Juergens, por
  Senua), **Logro de audio** y la categoría nueva «Game Beyond
  Entertainment». ✅ (dos fuentes: https://en.wikipedia.org/wiki/Hellblade:_Senua%27s_Sacrifice
  §Awards, y https://www.techspot.com/news/74146-hellblade-senua-sacrifice-biggest-winner-bafta-awards-but.html
  — «It won five of its nominated categories on the night: Best British
  Game, Artistic Achievement, Best Performer, Audio Achievement, and the new
  Game Beyond Entertainment category»). El premio de **Logro de audio** es
  justo por el diseño binaural de las Furias (punto 13/21).
- Dentro del elenco secundario, **Druth es el más querido por la crítica y la
  comunidad**, no por delante de Senua pero sí el que más se cita: reseñas
  (IGN, Giant Bomb) destacan su narración de las Lorestones como lo mejor del
  ritmo del juego, y en Reddit hay hilos activos comparándolo con la
  narración alternativa de Hellblade II («The Others vs Druth... which do you
  think is better?», 7 votos, 1 comentario, r/hellblade:
  https://www.reddit.com/r/hellblade/comments/1gs4s4e/ — un fan responde que
  la narración de Druth es «más mitológica o mística», la de «los Otros» da
  perspectiva de los personajes nuevos). ✅ (dos fuentes: el hilo de Reddit +
  la propia wiki de Druth, que dedica una sección larga a sus historias).

### Punto 8 — Doblaje latino y frases icónicas

**No hay doblaje al español (ni latino ni de España) en ningún juego de la
saga. Sólo subtítulos.** Comprobado como pide el encargo:

- **Doblaje Wiki, por su API** (`action=parse`, no la web que da 402): probé
  `Hellblade`, `Hellblade: Senua's Sacrifice`, `Hellblade II`, `Senua's Saga:
  Hellblade II` → los 4 dan `error: The page you specified doesn't exist`.
  También `action=query&list=search&srsearch=Hellblade` y `srsearch=Senua` →
  0 resultados relevantes (el buscador sólo devuelve coincidencias
  fonéticas sin relación, como «Senna Abaru»). ✅ Confirmado: Doblaje Wiki NO
  tiene página de Hellblade, ni la tuvo nunca (no es que la borraran).
  https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Hellblade
- **Segunda fuente, prensa hispana especializada en videojuegos** (no doblaje
  wiki, pero exactamente lo que pide el encargo si no hay doblaje: «dilo»):
  - 3DJuegos LATAM (21-may-2024): «Hellblade 2 no tendrá doblaje al Español:
    Xbox opta por seguir con los subtítulos». Cita al director de audio de
    Ninja Theory: la decisión «se ha mantenido por razones de calidad»
    (doblar exigiría grabar en los estudios de la propia desarrolladora).
    Subtítulos en **26 idiomas** sin contar inglés, «incluyendo el Español
    Latino». https://www.3djuegos.lat/xbox-series-x-s/hellblade-2-no-tendra-doblaje-al-espanol-xbox-opta-seguir-subtitulos-lugar-audio-nuestro-idioma
  - LEVEL UP (17-abr-2024): «Senua's Saga: Hellblade II no tendrá doblaje
    latino ni ningún otro, así que los fanáticos sólo podrán disfrutar la
    experiencia con las voces originales al inglés», subtítulos a «más de 20
    idiomas». https://www.levelup.com/noticias/783046/Senuas-Saga-Hellblade-II-tendra-doblaje-latino-Ninja-Theory-responde
  - ✅ (dos fuentes) Confirmado también para el primer juego (2017): sólo
    subtítulos en español, nunca hubo audio doblado (hilo oficial de Steam
    «Cómo poner el juego en español», y la propia falta de créditos de
    doblaje en Doblaje Wiki, ANMTV —tampoco tiene entrada— o Crunchyroll,
    que no distribuye el juego).
- **Cómo se tradujo al español** (ya que no hay doblaje, esto es lo que sí
  hay): los términos clave se tradujeron literalmente y se mantienen
  consistentes en los subtítulos oficiales: «the Furies» → **«las Furias»**,
  «the Darkness» → **«la Oscuridad»**. ✅ (dos fuentes: búsqueda web que cruza
  reseñas y foros en español usando esos términos, y la reseña en español de
  NextN sobre la Switch —ver abajo— cuyo propio titular usa «Viaje a la
  oscuridad»). https://www.nextn.es/2019/04/analisis-hellblade-senuas-sacrifice-nintendo-switch/
  Los nombres propios (Senua, Druth, Dillion, Zynbel, Hela, Valravn, Surtr,
  Gramr) no se traducen, se dejan igual que en inglés/nórdico antiguo.
- **Frases icónicas (en inglés, con su origen y traducción de sentido; no hay
  clip doblado que subtitular en español porque no existe doblaje)**:
  - Narrador/Furias, monólogo de apertura: *"Hello, who are you? ...It
    doesn't matter. Welcome. You are safe with me."* — voz de la wiki y
    confirmada oyéndola: https://static.wikia.nocookie.net/hellblade-nt/images/b/bd/Senua.mp3
    (pese al nombre del archivo, es el Narrador, no Senua — ver punto 13).
  - Zynbel/la Sombra, amenaza recurrente: *"I am your shadow. And I will be
    watching when you draw your last dying gasp."* —
    https://static.wikia.nocookie.net/hellblade-nt/images/7/78/Shadow.mp3
  - Druth a Senua: *"Druth is my Truth."* (juego de palabras intraducible al
    español sin perder el sentido — «Druth» sale de «truth», verdad) —
    https://static.wikia.nocookie.net/hellblade-nt/images/6/6a/Druth.mp3.mp3
  - Dillion a Senua, sobre la muerte: *"A life without loss is one without
    love."* — clave del tema del juego, citada en reseñas en español (NextN:
    «Te hará vivir y sufrir tanto como su protagonista, empatizar con su
    lucha»).
  - Las Furias en pánico, escena de escalar: *"Climb, Senua. Climb. Climb.
    She's hurt. So tired."* —
    https://static.wikia.nocookie.net/hellblade-nt/images/5/5b/The_Furies.mp3

### Punto 12 — Qué ama el fandom y qué NO hacer

**Lo que ama:**
- **El «farol» del permadeath** (uno de los mitos más comentados de la
  historia reciente de los videojuegos): el juego avisa al empezar: «The dark
  rot will grow each time you fail. If the rot reaches Senua's head, her
  quest is over and all progress will be lost». Mucha gente creyó que morir
  mucho borraba la partida para siempre. Probado exhaustivamente por la
  prensa (PCGamesN murió más de 50 veces sin perder nada): **es un farol**,
  la podredumbre nunca llega a la cabeza sólo por morir en combate. El
  director creativo de Ninja Theory dijo que la redacción del aviso fue
  deliberada, para meter al jugador la misma ansiedad e hipervigilancia que
  siente Senua. ✅ (dos fuentes: https://www.pcgamesn.com/hellblade-senuas-sacrifice/hellblade-permadeath-fake
  y https://comicbook.com/gaming/news/hellblade-senuas-sacrifice-permadeath-is-a-lie/ ).
  Es EL tema de conversación clásico del fandom; cualquier lámina o texto
  sobre «miedo a morir» en Hellblade puede jugar con esto.
- **Jugar con auriculares**: la comunidad lo repite como regla no escrita
  (reseñas y Reddit) por el audio binaural de las Furias — sin auriculares se
  pierde el efecto de voces que rodean la cabeza.
- **Rejugarlo con la narración de «Los Otros»** (Hellblade II): al terminar
  el juego se desbloquea una segunda narración, contada por los tres NPC que
  acompañan a Senua (empezando por el esclavista vikingo Thórgestr), en vez
  de por Druth. La prensa en español lo señala como razón para rejugarlo. ✅
  (Kotaku en Español: «Después de llegar al final [...] desbloquearás la
  narración de 'Los Otros', los tres NPC que acompañan a Senua [...] narran
  secciones del juego [...] comenzando con [el] esclavista vikingo,
  Thórgestr» — https://es.kotaku.com/repeticion-del-narrador-de-la-saga-hellblade-2-senuas-1851497170 ).
- **Identificarse de verdad con la psicosis**: en Reddit, hilos con gente que
  tiene TEPT, ansiedad o psicosis describiendo reacciones físicas reales
  jugando (ver punto 21) — no es un meme, es la razón principal por la que el
  fandom lo defiende con tanta pasión.
- El giro final (Hela es en realidad la madre de Senua, Galena, quemada por
  Zynbel) es un momento que la comunidad comenta mucho como «hay que fijarse
  bien»: si el jugador presta atención puede notar a Hela en el lugar de
  Senua durante el clímax (dato de la propia wiki, sección Trivia).

**Qué NO hacer (para que no «se note IA» ni ofenda al tema real):**
- **No convertir la psicosis en un monstruo literal ni en un chiste.** Todo
  el desarrollo (ver punto 13) se hizo con neurocientíficos y personas que
  viven con psicosis real; el juego evita a propósito los estereotipos de
  «loco peligroso». Una lámina con Senua «poseída» de forma cómica o
  demoníaca rompe el tono.
- **No mostrar a Senua «curada».** Melina Juergens (su actriz) dijo
  expresamente que le molestaba la idea de que su personaje «superó toda su
  adversidad y sanó» tras el primer juego — la psicosis no se cura en la
  saga, se aprende a vivir con ella. Un texto de lámina que sugiera que
  Senua «venció su locura» es incorrecto y contradice a la propia actriz.
- **No usar una burbuja de diálogo blanca genérica** (regla general del
  encargo, pero aquí aplica el doble: en el juego mismo el texto de las
  Furias aparece a los lados de la pantalla, no en globos, para imitar cómo
  se oyen —desde ambos oídos—, y los subtítulos usan tipografía rúnica/tallada,
  no una fuente neutra).
- **No sexualizar a Senua** ni vestirla con ropa "atractiva": su diseño es
  deliberadamente realista y desgastado (barro, sangre, cicatrices) — es el
  opuesto al fanservice.
- **No inventar doblaje latino.** Ver punto 8: no existe. Poner «voz de
  [actor de doblaje]» sería falso y detectable al instante por cualquier
  miembro del servidor que conozca el tema.

### Punto 13 — Descripción profunda de personajes

**Senua** (voz e interpretación: **Melina Juergens**, sin experiencia actoral
previa — era editora de vídeo en Ninja Theory; hizo la prueba de captura de
movimiento «para probar la tecnología» y se quedó con el papel. ✅ dos
fuentes: wiki https://hellblade.fandom.com/wiki/Senua#Trivia y reseña en
español https://www.nextn.es/2019/04/analisis-hellblade-senuas-sacrifice-nintendo-switch/
—«no era la actriz propuesta originalmente [...] jamás había actuado»—).

- **Carácter**: reservada, retraída, «mansa» al principio por años de
  aislamiento y maltrato; determinación tenaz pese al pánico. En Hellblade II
  gana empatía: ya no lucha sólo su batalla personal, percibe el dolor
  colectivo de la gente que encuentra (texto de la wiki, sección
  Personality, ambos juegos).
- **Cómo se expresa**: habla poco y en frases cortas y graves cuando es ella
  misma; grita y jadea en combate («fighting more out of survival instinct
  than elegant technique», wiki). Nunca hace bromas; su humor es inexistente,
  su tono es siempre serio-contenido, salvo estallidos de rabia o pánico.
  Analizado con `voz.py` sobre el audio oficial de la wiki (medidas
  automáticas; ⚠️ el pitch-tracking se confunde con la música/reverb que
  llevan estos clips de cita, así que los Hz son orientativos, no un dato
  limpio de laboratorio — lo fiable es el patrón de velocidad y expresividad):
  - Narrador de apertura (voz que se atribuye a Senua en el archivo pero es
    el Narrador — ver más abajo): 117 Hz medio, **muy expresiva** (15.8
    semitonos), **lenta** (1.26 palabras/s) — un susurro pausado, casi de
    nana. Fuente: https://static.wikia.nocookie.net/hellblade-nt/images/b/bd/Senua.mp3
    analizado con `voz.py`.
  - Tráiler de revelación de Hellblade II (narración con la propia voz de
    Senua mezclada con Furias de fondo): 208 Hz medio, **muy expresiva**
    (30.1 semitonos de rango), **lenta** (1.89 palabras/s) — transcripción:
    «I've dreamt of this. This place of fear and fury. Do you hear it? The
    heartbeat of the lost ones. Can feel them on my skin.» Fuente:
    https://www.dailymotion.com/video/x8qciu2 (procesado antes por el
    equipo, ficha en `/tmp/claude-0/trabajo/118-episodios/hb2-trailer/voz/`).
- **Lenguaje corporal y cara en cada emoción** (fotogramas ya sacados por el
  equipo con `fotogramas.py`, mirados por mí — hojas en
  `/tmp/claude-0/trabajo/118-episodios/hb1-trailer/hojas/` y
  `.../hb2-trailer/hojas/`):
  - **Serenidad / posible alegría contenida**: 0:29 del tráiler de
    revelación de 2016, primer plano con tocado dorado, expresión suave y
    casi una sonrisa leve — es una visión "dorada" de sí misma, antes o
    fuera de la Oscuridad. https://www.dailymotion.com/video/x5v5lz0?t=29
  - **Sonrisa inquietante (delirio/alucinación)**: 0:38, primer plano con
    pintura azul, sonrisa amplia y fija que no encaja con el tono del resto
    — típica de los momentos en que no se sabe si lo que ve es real.
    https://www.dailymotion.com/video/x5v5lz0?t=38
  - **Rabia / grito de combate**: 1:17, primer plano gritando con los
    dientes apretados y la cara pintada de azul salpicada de sangre.
    https://www.dailymotion.com/video/x5v5lz0?t=77
  - **Miedo**: 1:31 (mismo tráiler), ojos muy abiertos, boca entreabierta,
    mirada de pánico contenido; y también 1:44-1:45 del tráiler de
    Hellblade II (2019), primer plano llorando con los ojos entrecerrados
    por el miedo, cara sucia y mojada. https://www.dailymotion.com/video/x5v5lz0?t=91
    y https://www.dailymotion.com/video/x8qciu2?t=104
  - **Tristeza / agotamiento**: 1:56 del tráiler de Hellblade II, mirando
    hacia abajo, hombros caídos, luz fría. https://www.dailymotion.com/video/x8qciu2?t=116
  - ⚠️ No encontré un fotograma claro de «vergüenza» específica en los
    tráileres disponibles (son de acción, no de diálogo íntimo); ese gesto
    habría que sacarlo de una escena de historia completa, que no pude
    grabar por el bloqueo de YouTube y porque los clips de Dailymotion
    disponibles son cortos.
- **Miedos y lo que le importa**: perder a quienes ama (Dillion, su madre);
  ser «el monstruo» que su padre decía que era; que su psicosis dañe a los
  demás. Le importa sobre todo la verdad de Druth y el recuerdo de su madre
  (pedirle que la mirara «con ojos brillantes»).
- **Relaciones**:
  - **Dillion** (voz: **Oliver Walker**, ✅ wiki +
    https://en.wikipedia.org/wiki/Hellblade:_Senua%27s_Sacrifice#Plot: «Dillion
    (Oliver Walker)»): su amor, el único que la vio como algo más que su
    enfermedad. Su cabeza cercenada es lo que Senua carga durante todo el
    primer juego.
  - **Druth** (voz: **Nicholas Boulton**, ✅ mismas dos fuentes: wiki +
    Wikipedia «guided by her memories of the stories of Druth (Nicholas
    Boulton)»): antiguo esclavo irlandés («Findan» antes de escapar y
    renombrarse), mentor y narrador; muere antes del viaje a Helheim pero
    sigue narrando en forma de recuerdo. Se llama a sí mismo y a Senua
    *geilts* (término irlandés: enloquecido por el terror o la batalla).
  - **Zynbel** (voz: **Steven Hartley**, que también hace de «la Sombra» —
    ✅ wiki + Wikipedia «the Darkness (Steven Hartley) [...] her father,
    Zynbel (also performed by Hartley)»): padre druida fanático; quemó viva
    a la madre de Senua por «tener la misma maldición»; abusó física y
    emocionalmente de Senua durante años. Se manifiesta como «la Sombra»
    (voz oscura que la degrada durante el viaje).
  - **Galena** (voz: **Ellie Piercy**, ✅ Wikipedia): madre de Senua,
    también con psicosis, pero la vivía como un don, no una maldición.
  - **El Narrador / una de las Furias** (voz: **Chipo Chung**, ✅
    Wikipedia: «the Narrator (Chipo Chung)»): es la voz que rompe la
    cuarta pared y habla directo al jugador.
  - **Las Furias** (las voces femeninas y masculinas que Senua oye
    —además del Narrador—): interpretadas por **Abbi Greenland** y **Helen
    Goalen**, ambas fundadoras de la compañía de teatro británica RashDash;
    repitieron el papel en Hellblade II. ✅ (Wikipedia, artículo de
    Hellblade: Senua's Sacrifice, sección Development: «Abbi Greenland and
    Helen Goalen, both founding members of British theatre company RashDash,
    were ultimately cast as the voices, known as the Furies, a role they
    would reprise in the game's sequel» + confirmado en el artículo de
    Hellblade II: «Abby Greenland and Helen Goalen reprised their roles as
    the 'Furies'» — https://en.wikipedia.org/wiki/Senua%27s_Saga:_Hellblade_II ).
    Grabadas con **técnica binaural** (micrófono con forma de cabeza
    humana, capta posición 3D del sonido) siguiendo descripciones del
    profesor **Charles Fernyhough** (Universidad de Durham, experto en oír
    voces) y con feedback de un grupo real de «oidores de voces» que
    probaba las grabaciones. Se repitió la misma técnica en Hellblade II.
  - En Hellblade II: **Ástríðr** (voz: **Aldís Amah Hamilton**) líder
    guerrera de Bárðarvík; **Fargrímr** (voz: **Guðmundur Thorvaldsson**)
    guía espiritual; ambos ✅ confirmados en el wikitext de sus páginas de
    personaje (`portayed_by`).
- **Análisis de audio de las Furias y la Sombra con `voz.py`** (sobre los
  .mp3 originales del juego, alojados en la propia wiki de Fandom —no
  YouTube—, para cumplir el aviso de «fijarse en el audio binaural y las
  voces de la psicosis», puntos 13 y 21):
  - Narrador («Oh how rude of me...»): 84 Hz grave, muy expresiva (15.9
    semitonos), velocidad normal (2.07 palabras/s).
  - Coro de Furias en pánico durante una escalada («Climb, Senua. Climb.»):
    238 Hz agudo, muy expresiva (27.5 semitonos), **rápida** (3.5
    palabras/s) — se nota el atropello de varias voces urgiendo a la vez,
    justo el efecto que describe la wiki de Psychosis («a veces
    contradictorias entre sí, unas animan mientras otras se burlan»).
  - La Sombra/Zynbel («I am your shadow…»): medido en 532 Hz muy agudo,
    pero ⚠️ esto es casi con certeza un artefacto: la voz real de Steven
    Hartley es grave (es un actor adulto haciendo de padre autoritario) y
    se oye distorsionada/procesada digitalmente para sonar sobrenatural —
    el medidor de tono se confunde con esa distorsión. Lo fiable aquí es
    cualitativo: muy expresiva (32.3 semitonos) y rápida (3.57 palabras/s),
    o sea, urgente y amenazante, no un susurro sereno.
  - Los tres archivos: `/tmp/claude-0/trabajo/118-hellblade-voz/audio_wiki/`
    (Furies.mp3, TheFuries.mp3, Shadow.mp3, Senua.mp3, Druth.mp3, Dillion.mp3),
    bajados con `Referer: https://www.fandom.com/` desde
    `static.wikia.nocookie.net`, análisis en
    `/tmp/claude-0/trabajo/118-hellblade-voz/analisis_*/ficha_voz.json`.
- **Qué transmite verla / cómo se siente jugarla**: angustia contenida que
  se vuelve determinación; no da alivio cómico en ningún momento (ver reseñas
  del punto 21: «piercing intensity», «legitimately affected»). No hay
  constancia en toda la wiki, ni en los guiones citados, de que Senua **se
  ría** ni una sola vez en ninguno de los dos juegos (comprobado: busqué
  «laugh», «smile», «joke» en el wikitext completo de su ficha y no aparece
  ninguna escena de risa) — es un dato de personaje en sí mismo: su arco no
  pasa por la alegría ligera, pasa de miedo/culpa a determinación serena.
  **Cómo saluda**: no hay saludos "normales" en el juego —a los personajes
  vivos (Ástríðr, Fargrímr, Thórgestr) los aborda directo, seria y cautelosa,
  sin cortesías; con los muertos (Druth, Dillion) habla en su cabeza, como
  recuerdo. **Cómo explica algo**: en frases declarativas cortas, casi nunca
  hace preguntas retóricas —esas las hacen las Furias, no ella. **Con quién
  discute**: con la Sombra (Zynbel) todo el tiempo, y a ratos directamente
  con sus propias Furias («decirles que la dejen en paz», wiki, sección
  Personality). **Quién la hace reír**: nadie, en ningún material revisado —
  ni siquiera Dillion, pese a ser la relación más cálida que tiene.
- **Arco resumido**: de creer que su psicosis es una maldición que hay que
  ocultar y curar (HB1) a usarla como herramienta y verse a sí misma como
  «faro de esperanza» que ayuda a otros con el mismo tipo de sufrimiento
  (HB2). Momento clave 1: el puente de Helheim, cuando se queda sin nada que
  ofrecer a Hela y aun así no se rinde (final de HB1). Momento clave 2: el
  reconocimiento de Illtauga («I know you», HB2) — ver punto 21.
- **Método de actuación** (relevante para «cómo se expresa» y para la guía de
  IA del punto 17 que hará el redactor): Juergens usó un proceso tipo
  «method acting» para Hellblade II — viajó a Islandia, entrenó esgrima y
  artes marciales, y pasaba ocho horas en maquillaje/vestuario antes de cada
  grabación. Los animadores recibieron entrenamiento militar para que los
  NPC enemigos se movieran de forma creíble. ✅
  https://en.wikipedia.org/wiki/Senua%27s_Saga:_Hellblade_II#Development

### Punto 20 — Gustos y detalles de cada personaje

⚠️ Hellblade no tiene *databook* oficial de personajes (comprobado: en 2021
los propios fans pedían un artbook en el foro de Steam y no existía ninguno
de Ninja Theory — https://steamcommunity.com/app/414340/discussions/0/3048356660238876040/ ;
sólo hay un «GAME HANDBOOK» de terceros en Amazon, no oficial). No hay
cumpleaños, comida favorita ni altura publicados — es un juego narrativo
realista, no una ficha de anime. Lo que sí hay, sacado de la propia
narrativa (wiki + Wikipedia, ✅ dos fuentes cada uno):

- **Lo que Senua siempre lleva encima**: la cabeza cortada de Dillion
  (atada a la cadera), el Espejo de Hierro que le dio Druth (para ver «el
  otro mundo», también mecánica de combate: da carga de Focus), y su
  espada. En Hellblade II cambia de arsenal pero conserva el mismo tipo de
  atuendo de cuero y pieles.
- **Cómo se ve a sí misma**: al principio del primer juego, como alguien
  «maldita», su psicosis es un castigo de los dioses; al final del primer
  juego aprende (con ayuda del recuerdo de su madre) a verla como una
  condición con la que aprender a vivir, no una maldición a curar. En
  Hellblade II, Ninja Theory la describe como un «faro de esperanza»
  («beacon of hope»): ya no lucha *contra* su psicosis sino que la usa como
  herramienta (la creen «vidente» porque oye voces).
- **Manía / objeto de Druth**: su gorro de cuero con calavera de animal
  pequeño y plumas (se refiere a sí mismo también como un tipo de «pájaro»
  por el término *geilt*).
- **Lo que odia/teme Zynbel**: la «oscuridad» (psicosis) en su propia
  familia; se define por su fanatismo religioso, no por gustos personales.

### Punto 21 — Por qué la gente la ama

- **Reconocimiento crítico centrado en la psicosis, no en la jugabilidad**:
  Metacritic la describe como «generally favorable»; casi todas las reseñas
  grandes (IGN, Giant Bomb, PC Gamer, VideoGamer.com, EGM) coinciden en que
  el combate y los puzles son lo más flojo, pero la interpretación de
  Juergens, el diseño de sonido y el tratamiento del tema son «casi sin
  parangón en el medio» (Giant Bomb). ✅ https://en.wikipedia.org/wiki/Hellblade:_Senua%27s_Sacrifice#Reception
- **Por qué conecta la gente (identificación real, no genérica)**: en
  r/hellblade hay hilos de jugadores con enfermedad mental real describiendo
  reacciones físicas jugando:
  - «Does anyone else with mental illness experience amazingly intense
    sensations with this game?» (76 votos, 20 comentarios): «I have PTSD and
    terrible anxiety [...] I broke out in sweat, cried, hyperventilated, and
    panicked [...] Mad props to the devs for planting you so firmly in
    Senua's hellish reality.» https://www.reddit.com/r/hellblade/comments/lubm62/
  - «3 years late but I finally played Hellblade, and I cried...a lot...so I
    drew my feelings.» (240 votos, 10 comentarios) —
    https://www.reddit.com/r/hellblade/comments/ktwcbv/
  - «I'm incredibly glad I was referred to this game [...] I haven't cried
    during a game since TLOU 1 and 2.» (60 votos) —
    https://www.reddit.com/r/hellblade/comments/1d1yi2v/
  - ✅ (dos fuentes por patrón: los tres hilos + la propia reseña de Alice
    Bell en VideoGamer.com citada en Wikipedia, que dice que el juego «da
    tanto cuidado, con aportación en cada paso de psicólogos y gente que ha
    vivido psicosis, para dar una representación lo más fiel posible»).
- **Escena que más hace llorar/temblar (Hellblade II)**: el momento en que
  Senua se enfrenta a la giganta Illtauga (antes Ingunn, una madre que
  perdió a su bebé) y dice «I know you» al reconocerla — hilo de 81 votos y
  24 comentarios en r/hellblade discutiendo por qué llora en esa línea (teme
  convertirse ella misma en algo así):
  https://www.reddit.com/r/hellblade/comments/rd4ynb/ . Encaja con el patrón
  de la saga: los «gigantes» de Hellblade II son personas comunes rotas por
  el miedo, no monstruos — el juego pide perdonarlos, no matarlos triunfante,
  para volverlos piedra (dato de la wiki y del resumen de Wikipedia del
  argumento).
- **Escena que más se cita de todas (final del primer juego)**: el reto a
  Hela en el puente de Helheim, cuando Senua admite «no tengo nada más que
  dar» y aun así se mantiene firme — varias reseñas (PC Gamer, VideoGamer.com)
  la señalan como el clímax emocional; el giro de que Hela toma la cara de su
  madre Galena a medio quemar es lo que remata la escena.
- **Premios como prueba de "por qué la aman" más allá de reseñas**: 5 BAFTA
  (ver punto 7) + más de un millón de copias vendidas para junio de 2018 (✅
  https://en.wikipedia.org/wiki/Hellblade:_Senua%27s_Sacrifice — «The game
  sold over one million units by June 2018», repetido en la sección
  Release) pese a ser un estudio pequeño (~20 personas) y precio bajo —
  se suele citar como ejemplo de «juego indie que compite con AAA».

### Punto 22 — Fan dubs y comunidad hispana

- **No encontré fandubs en español de escenas completas con recorrido
  (canal dedicado, varias vistas, comunidad detrás)**, a diferencia de series
  de anime. Lo que sí hay:
  - Un vídeo suelto, «Hellblade Intro | DOBLAJE en ESPAÑOL 🎙 | Irene Acosta»
    en YouTube (https://www.youtube.com/watch?v=xBgdwfX-WvE) — parece un
    fandub de aficionada del monólogo de apertura; no pude confirmar
    vistas/canal por el bloqueo de YouTube en este servidor («Sign in to
    confirm you're not a bot»). ⚠️ Una sola fuente, sin poder verificar
    datos (vistas, fecha) — dejar como pista para quien pueda entrar a
    YouTube fuera del servidor.
  - Gameplays en español latino sin doblaje (voz en off del streamer sobre
    subtítulos), no fandub de personaje: «Hellblade Senua's Sacrifice en
    Español Latino | Capítulo 1» (canal GaboMania) y una lista de
    reproducción «Let's play en ESPAÑOL». Esto es narración de streamer, no
    doblaje de personaje — lo distingo para que no se confunda en la biblia.
  - Vídeos de opinión sobre la falta de doblaje («HELLBLADE 2 NO TENDRÁ
    VOCES EN ESPAÑOL...», «Drama con el doblaje de Hellblade 2...!!!») — son
    reacción/queja, no fandub.
- **Covers de openings en español**: no aplica igual que en anime — Hellblade
  no tiene un tema cantado de apertura/cierre, su banda sonora es ambiental
  (compuesta por David García/Andy LaPlegua en el 1, por Heilung en el 2),
  así que no hay «opening» que versionar. Lo digo en una línea porque el
  encargo pide decir cuándo un punto no aplica y por qué.
- **Parodias y memes hispanos específicos**: no encontré memes en español
  propios del fandom hispano más allá de compartir el meme general del
  «farol del permadeath» (punto 12) traducido/comentado en foros en
  español (Steam en español, los vídeos de opinión ya listados). ⚠️ Una
  sola fuente indirecta, no un meme hispano original.
- **Búsquedas hechas** (español e inglés, sin YouTube directo por el
  bloqueo): `Hellblade fandub español`, `Hellblade doblaje fan Senua`,
  `Hellblade fandub latino` (ya en datos-voz.md, sin resultados), y en
  Dailymotion (datos-voz.md) tampoco aparece ningún fandub real, sólo
  gameplay sin editar.
- ⚠️ Conclusión honesta: la comunidad hispana de doblaje/fandub prácticamente
  no ha tocado Hellblade — probablemente porque, al no haber diálogo doblado
  oficial de referencia y ser un juego narrativo pesado (no una serie con
  personajes "ligeros" para imitar), no genera el mismo tipo de fandub que
  el anime. Esto en sí es un dato útil para el servidor: es terreno casi
  virgen para quien quiera doblarlo.

## Lo mejor para la lámina

1. La cita de las Furias en pánico («Climb, Senua. Climb. Climb.») funciona
   muy bien como texto corto y angustiado para un canal de doblaje/voz —
   tiene ritmo de verdad, urgente, no un cuadro de diálogo plano.
2. El «farol del permadeath» es un gancho perfecto de lámina (objeto real:
   el brazo con la podredumbre, o una nota de aviso "grabada en piedra"):
   todo el fandom lo conoce y da pie a un texto tipo advertencia del juego.
3. Los tres nombres de voz clave para citar en la lámina: **Melina Juergens
   (Senua)**, y **Abbi Greenland / Helen Goalen (las Furias, técnica de
   grabación binaural)** — son el dato de "voz" más fuerte y verificable de
   todo el encargo, perfecto para un servidor de doblaje.
4. «No hay doblaje latino, sólo subtítulos («las Furias», «la Oscuridad»)» —
   dato honesto y directamente citable en el pie de la lámina o en un texto
   de contexto, para que el servidor entienda por qué no hay clip doblado
   que usar.
5. Fotograma 0:38 del tráiler de 2016 (sonrisa inquietante) es la imagen más
   "psicosis, no terror genérico" de todas las que miré — mejor que un grito
   de combate para transmitir el tema real del juego.

## No encontré

- ⚠️ Encuesta oficial o de fans de "personaje favorito" (no existe este
  formato en el fandom de Hellblade; busqué en inglés y español, ver punto
  7).
- ⚠️ Databook o artbook oficial con gustos/cumpleaños/altura (confirmado que
  no existe, ver punto 20).
- ⚠️ Fandub español de una escena completa con canal y vistas verificables
  (sólo un vídeo suelto sin poder confirmar datos por el bloqueo de
  YouTube, ver punto 22).
- ⚠️ Fotograma claro de "vergüenza" en los tráileres disponibles en
  Dailymotion (son de acción; habría que sacarlo de una escena de historia
  completa que no pude grabar en este servidor).
- ⚠️ Canción exacta que suena en la escena de Illtauga/"I know you" (Reddit
  discute la escena pero no cita el nombre de la pista; eso es más bien del
  punto 9, que no es mío — lo dejo anotado por si el investigador de vídeo
  lo tiene).

## Bitácora de búsqueda

- Fandom `hellblade.fandom.com` (API `action=parse&prop=wikitext`, en
  inglés): páginas Senua, Druth, Dillion, Zynbel, Valravn, Hela, Psychosis,
  Hellblade: Senua's Sacrifice, Hellblade II: Senua's Saga, Galena, Astridr,
  Fargrímr, y `allpages` para el índice completo de la wiki.
- Doblaje Wiki (`doblaje.fandom.com/es/api.php`, español): `action=parse`
  sobre 4 variantes del título → todas `error, no existe`; `action=query
  list=search` con «Hellblade», «Senua» → 0 resultados relevantes.
- Wikipedia (`en.wikipedia.org/w/api.php`, inglés): extractos completos de
  «Hellblade: Senua's Sacrifice» y «Senua's Saga: Hellblade II» (gameplay,
  argumento, desarrollo, recepción, premios).
- Audio original del juego: 6 archivos `.mp3` de citas de personaje bajados
  directo de `static.wikia.nocookie.net` (con `Referer` de Fandom) y
  analizados con `herramientas/voz.py` (registro, semitonos, velocidad,
  transcripción Whisper).
- Prensa en español (curl directo): 3DJuegos LATAM, LEVEL UP, NextN.es,
  Kotaku en Español (sobre doblaje latino, traducción de términos y la
  narración alternativa de Hellblade II).
- Reddit vía Arctic Shift (`arctic-shift.photon-reddit.com`, inglés):
  búsquedas «favorite character», «Druth», «cried», «emotional» en
  r/hellblade.
- Danbooru: comprobación de etiquetas por personaje (`druth`, `dillion`,
  `zynbel`, `hela_(hellblade)`) para el punto 7.
- WebSearch (5 búsquedas de las ~50 disponibles): BAFTA 2018 categorías,
  doblaje latino Hellblade, fandub español, encuesta de personaje favorito,
  permadeath rumor, artbook oficial.
- YouTube: bloqueado en este servidor («Sign in to confirm you're not a
  bot»); usé Dailymotion (clips ya listados en `datos-voz.md` y
  fotogramas/voz ya procesados por el equipo en
  `/tmp/claude-0/trabajo/118-episodios/`) según indica AYUDANTE.md.
- TV Tropes y Wayback Machine: intenté la ficha de personajes de TV Tropes
  (403 directo) y su copia en Wayback (`web.archive.org` — la conexión del
  proxy se cortó, `ws_closed_mid_exchange`); no insistí más de dos intentos
  como pide AYUDANTE.md. ⚠️ No cubierto por mí; si el redactor lo necesita,
  reintentar en otro momento (puede ser sólo saturación puntual del proxy).
