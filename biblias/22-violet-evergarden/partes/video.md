# Parte del investigador de VÍDEO · Violet Evergarden (puntos 2, 4, 9, 10, 14)

Repaso sobre una biblia ya escrita (revisar.py: 0 de 15 minutos citados). YouTube pedía
inicio de sesión desde este servidor: usé **Dailymotion** (los mismos clips oficiales
reesubidos) e **Internet Archive**. AnimeThemes dio error 522 (caído) las dos veces que
lo probé, igual que ya avisaba `datos-video.md`. Todo lo de abajo sale de vídeos que
**miré de verdad** con `fotogramas.py` (hojas de contacto en
`/tmp/claude-0/trabajo/22-violet-video/`) y coloreé con `estilo.py`/Pillow sobre
fotogramas sueltos. Los minutos de episodio los crucé con los subtítulos japoneses
originales del espejo de kitsunekko (mismo método que ya usó la biblia en la sección 2),
clonado en `/tmp/claude-0/trabajo/22-violet-video/kmirror/`.

## Lo que miré (obligatorio de AYUDANTE.md)

| Vídeo | Fuente real | Duración | Resolución medida | Fotogramas | Hoja |
|---|---|---|---|---|---|
| **Opening «Sincerely»** (TRUE), completo | Dailymotion, canal Espinof · https://www.dailymotion.com/video/x8c9bet | 1:30 | 512×288 (reencode de Dailymotion; no hay copia en 1080p accesible sin YouTube) | cada 3 s, 31 fotogramas | `opening/hoja_01.jpg` |
| **Tráiler oficial** subtitulado en español | Dailymotion, canal FilmAffinity · https://www.dailymotion.com/video/x7t0he2 | 1:28 | 512×288 | cada 2 s, 45 fotogramas | `trailer_es/hoja_01.jpg` |
| **Ending «みちしるべ» (Michishirube)**: no encontré la secuencia animada del anime (ni en Dailymotion ni en Internet Archive); vi el **vídeo musical oficial** de Minori Chihara (acción real, con violín) | Internet Archive (espejo de YouTube) · https://archive.org/details/youtube-UKU4B05fPck (archivo `UKU4B05fPck.mp4`) | 4:49 | 854×480 | cada 8 s, 37 fotogramas | `ending/hoja_01.jpg` |
| **Escena icónica 1**: Violet salta en paracaídas desde el avión para rescatar al soldado Aidan | Dailymotion, canal «Wings of Silk», título «Violet Evergarden - parachute scene» · https://www.dailymotion.com/video/x8qbypz | 0:26 | 512×288 | cada 1 s, 26 fotogramas | `escena_paraguas/hoja_01.jpg` |
| **Escena icónica 2**: las cartas de cumpleaños de una madre a su hija Ann (ep. 10) | Dailymotion, canal lawrenceburgos69, título «Violet Evergarden Episode 10 Emotional Ending [Violet's Crying]», subtítulos en inglés | https://www.dailymotion.com/video/x80vbaj | 3:20 | 512×288 | cada 5 s, 41 fotogramas | `escena_ep10/hoja_01.jpg` |
| **Escena icónica 3**: Violet en el hospital, día 120, escribe su parte al Mayor Gilbert (ep. 1) | Dailymotion, canal «Chopper bom», título «Violet evergarden letter», subtítulos en español | https://www.dailymotion.com/video/x947zqa | 0:42 | 512×288 | cada 2 s, 21 fotogramas | `escena_letter/hoja_01.jpg` |

⚠️ Ninguno de estos vídeos llega a 1080p (el punto 2 del encargo lo pide): son
reesubidas antiguas de Dailymotion o el archivo mp4 de un espejo de YouTube en
Internet Archive. La única copia en 1080p que encontré es el ítem de Internet
Archive `violet-evergarden-720p-complete` (10,6 GB, sólo la película), demasiado
pesado para este contenedor compartido; queda anotado por si otra tanda con más
tiempo/disco quiere bajarlo. Lo que describo de postura y color lo vi en estas
resoluciones más bajas; los fotogramas de mayor detalle (cara, pliegues de tela)
pueden variar un poco al verlos en alta.

`video.mp4` de cada carpeta ya se borró tras sacar las hojas y los fotogramas
sueltos (quedan sólo las hojas JPEG y unos `fotograma_*.jpg` para medir color).

---

## Hallazgos

### Punto 2 · Fotogramas de escenas icónicas, con capítulo y minuto

- **Ep. 11, 00:10:04 a 00:10:15** — Violet salta en paracaídas desde un avión
  (sonido de motor: «（飛行機のエンジン音）（アルセニー）飛行機？» a las 00:10:04) para
  llegar hasta el soldado **Aidan**, que agoniza llamando a «Maria» (エイダン「マリア」
  00:01:27, 00:12:17, 00:16:04…). Los enemigos, al verla caer, dicen «子供？» («¿una
  niña?», 00:10:15): la confunden con una cría por su tamaño. Es el episodio **«I
  Don't Want Anybody Else to Die»** ✅ (subtítulo japonés del espejo kitsunekko,
  `[Retimed] Violet Evergarden - 11.srt`, líneas 92-140 y 580-583; resumen de la
  escena también en [búsqueda web con cita del argumento](https://www.imdb.com/title/tt8176408/plotsummary/)).
  El clip de Dailymotion (26 s) muestra: soldados junto a cruces/lápidas en la
  nieve al atardecer (00:00-00:02), el avión visto desde tierra (00:05-00:09), un
  bulto que cae y se abre el paracaídas naranja sobre bosque nevado (00:09-00:17),
  primeros planos de ojos azules con reflejo del atardecer (00:18-00:23) —
  probablemente Aidan mirando hacia arriba. **No hay diálogo en el clip que
  identifique a Violet en pantalla** (cae de espaldas a cámara): la identifico por
  el argumento y el sonido del avión, no porque se la vea con nitidez. ⚠️ marcar
  así si se usa como «Violet en acción».
  [Enlace con minuto](https://www.dailymotion.com/video/x8qbypz?t=9) (0:09, el
  paracaídas abriéndose).
- **Ep. 10, aprox. 00:20:26 a 00:22:38** (ya estaba en la biblia con ✅ por
  subtítulo japonés) — **confirmado visualmente**: la casa blanca de Ann de
  adulta; la madre, ya enferma, dicta cartas por adelantado para cada cumpleaños
  futuro («I'm sure you've grown up a lot…», «Have you graduated from riddles and
  bugs?», «Happy 18th birthday»); Ann niña llorando en un banco («Your mother
  loves you very much»); Ann adulta en una sala con vitrales recibe el paquete de
  50 cartas: «These letters are to be delivered to Ann Magnolia for the next
  fifty years»; cierre con la cita 「愛する人は　ずっと見守っている」 / «A loved one will
  always watch over you». Clip con subtítulo en inglés (no es el doblaje latino,
  es fansub/subtítulo del reescape) ✅ [Dailymotion, minuto 0:05 del clip](https://www.dailymotion.com/video/x80vbaj?t=5)
  (casa), [minuto 1:20](https://www.dailymotion.com/video/x80vbaj?t=80) (cartas
  por año), [minuto 3:15](https://www.dailymotion.com/video/x80vbaj?t=195) (cita
  final).
- **Ep. 1, 00:01:19 a 00:01:34** — Violet, en la cama del hospital, día 120 de
  internación, dicta/escribe su parte militar: *«Mayor Gilbert. Hoy es el día 120
  de mi hospitalización. Mis fuerzas están casi recuperadas. A pesar de ciertos
  desperfectos, mi estado me permite seguir con la misión. Solicito una pronta
  reintegración al servicio»* (subtítulo en español del clip; el japonés original
  dice «“ギルベルト少佐” “本日 入院120日目” “体力は ほぼ回復” “動作に多少 支障あるも―”
  “任務の遂行は可能” “速やかに 職務への復帰を…”») ✅✅ (confirmado en el clip doblado/subtitulado
  y en el `.srt` japonés original, líneas 8-13). Es el **primer texto que
  «escribe» Violet** en toda la serie, antes de saber lo que significa «te
  quiero»: encaja perfecto con #poemas. Postura: tumbada, mirando el techo, sólo
  el ojo en cámara (00:00-00:10 del clip); luego sentada en el borde de la cama,
  vendaje en la frente, escribiendo con las manos protésicas nuevas sobre un
  papel que tiembla al escribir la letra (00:18-00:22 del clip, primer plano de
  la pluma temblando); cierra con «Lo lamento» (00:40). [Enlace con minuto](https://www.dailymotion.com/video/x947zqa?t=18).
- **Opening, 0:39** — la máquina de escribir negra sobre mesa de madera clara, sin
  manos, en penumbra: el objeto solo, protagonista un segundo entero.
  [Enlace](https://www.dailymotion.com/video/x8c9bet?t=39).
- **Opening, 0:54 a 1:03** — el brazo mecánico de Violet, plano detalle: dedos de
  metal que se cierran despacio contra un fondo blanco liso, las juntas visibles.
  [Enlace](https://www.dailymotion.com/video/x8c9bet?t=54).

### Punto 4 · Fondos y sitios: luz, paleta (hex medidos) y texturas

Los sitios y su inspiración ya estaban bien sourceados en la biblia (§5.1); lo que
faltaba eran **colores medidos de verdad** (la biblia decía «todos los hex son
estimados ⚠️»). Medí con `estilo.py --colores` y, para zonas pequeñas (broche,
ojos), con Pillow píxel a píxel sobre los fotogramas sueltos que saqué del
opening y del tráiler (1280×720, reescalados de la fuente 512×288: sirven para el
tono, no para el detalle fino).

**Vestuario y personaje (Violet, fotograma del opening, 0:21 — [enlace](https://www.dailymotion.com/video/x8c9bet?t=21)):**
- Chaqueta militar: `#2F444F` (zona de sombra, hombro) y `#3B5363` (zona con más
  luz) → un azul grisáceo oscuro, más apagado que el «azul de Prusia de libro»
  `#003153` que proponía la biblia. ✅ medido, pero la escena está a contraluz de
  atardecer: en interior puede leerse más azul puro.
- Broche verde (los «ojos del Mayor»): `#4C8669` medido en el centro de la
  piedra — más verde-oliva que el `#1E8A5A` que estimaba la biblia. ✅ medido.
- Corbatín/lazo: `#ECE2C9` (crema, no blanco puro) ✅ medido, coincide con lo que
  ya decía la biblia sobre «blanco roto».
- Pelo: zona iluminada `#E6DAC0`, zona en sombra `#9E908C` (más grisáceo de lo
  esperado por el contraluz). ✅ medido.
- Ojos: en esta escena, a contraluz de atardecer, leen más teal que azul puro:
  `#426A6B` aprox. (promedio de 3 puntos del iris). ⚠️ un solo fotograma, con luz
  fuerte de fondo; conviene remedir en un plano de interior.
- Piel (mejilla): `#B5A491`.
- Tinta/cuerpo de la máquina de escribir (opening, 0:39): `#1E1D1B` (casi negro,
  nunca negro puro, confirma lo que ya decía la biblia) y madera del escritorio
  `#A27234`. ✅ medido.
- Papel de carta (fotograma de la escena de las 50 cartas, ep. 10,
  [enlace 1:15](https://www.dailymotion.com/video/x80vbaj?t=75)): `#F0EDE2` y
  `#DAD4C5` — coincide bien con el `#EFE6D2` que estimaba la biblia. ✅ medido.
- **Gilbert Bougainvillea** (no estaba en la paleta de la biblia): chaqueta
  oscura `#3E3932`, pelo castaño oscuro `#3B3734` (NO rubio: si algún punto de la
  biblia lo pinta rubio, corregir), piel con tono cálido de luz nocturna `#C6A670`
  (ojo: la escena es de noche con luces de calle ámbar, así que este último tono
  está corrido hacia el naranja). Fuente: tráiler,
  [minuto 0:56](https://www.dailymotion.com/video/x7t0he2?t=56), letrero en
  pantalla «ギルベルト・ブーケンビリア cv 浪川大輔» (Daisuke Namikawa, el mismo actor
  japonés que ya cita la biblia en música/voz). ✅ medido y con crédito en pantalla.

**Luz confirmada mirando los vídeos** (la biblia lo tenía todo ⚠️ «de memoria»):
- Opening: luz de tarde dorada muy marcada de 1:12 a 1:15 (cielo naranja sobre el
  mar) y contraluz azul en los primeros planos de Violet (0:18-0:24): confirma lo
  que decía la biblia sobre «sol bajo y dorado» y «contraluz con tristeza». ✅
- Interior de oficina (tráiler, 0:06-0:10): lámparas cálidas, madera oscura,
  ventanales — confirma «ventanal lateral, madera oscura» de la biblia §5.2. ✅
- Escena de Gilbert (tráiler, 0:56): calle nocturna con faroles ámbar y bokeh muy
  marcado al fondo (luces borrosas), gente en silueta: un recurso de luz que no
  estaba descrito en la biblia y sirve para escenas nocturnas/de ciudad. ✅
- Hospital (ep. 1, escena 3): luz fría de ventana lateral sobre sábanas blancas,
  contraste con el vendaje; nada del calor dorado de las escenas de campo. ✅

Ninguna textura nueva: las de `ambientCG`/`Poly Haven` que ya tenía la biblia
(papel, madera, cuero) encajan con lo que vi en los fotogramas (mesa de la
oficina de madera oscura con vetas visibles, papel con textura mate, no
satinado).

### Punto 9 · Música y sonido

- **Opening «Sincerely»** confirmado de oído y de vista completo (1:30, TRUE) ✅
  (ya lo tenía la biblia por IMDb/UtaTen; ahora además mirado fotograma a
  fotograma). Estructura visual: piano/paisaje (0:00-0:36) → clímax con fuego y
  brazo mecánico (0:39-1:03) → resolución en paisaje y carta (1:06-1:21): crece
  igual que describe la biblia («desde un piano hasta cuerdas enormes»).
- **Ending «Michishirube»**: el vídeo musical oficial (acción real) que miré
  confirma lo que ya tenía la biblia — letra y voz de **Minori Chihara**, música
  y arreglo de **Daisuke Kikuta (菊田大介)** — porque aparecen en los créditos del
  propio archivo (metadata de Internet Archive, descripción del ítem
  `youtube-UKU4B05fPck`: «作詞：茅原実里 作曲・編曲：菊田大介») ✅✅ (coincide con
  IMDb/ticketjam que ya citaba la biblia). El vídeo en sí: una actriz (no
  animación) recorre una casa de campo de época, un violinista toca al aire
  libre, cierre con una carta lacrada en rojo — **imaginería de carta/campo muy
  parecida al tono de la serie**, aunque no es la secuencia animada del anime.
  Sirve como referencia de ambiente para #poemas (carta + naturaleza + música),
  no como fotograma de la serie.
- **Efectos de sonido reconocidos por el fandom** (punto que la biblia no tenía):
  el **tecleo de la máquina de escribir de Violet** es EL sonido que el fandom
  más reconoce y hasta replica: dos guías de Reddit para configurar el sonido del
  teclado propio igual al de Violet ✅✅ — [«[GUIDE] How to make your keyboard
  sound just like Violet's
  typewriter!»](https://www.reddit.com/r/VioletEvergarden/comments/1suyki6/guide_how_to_make_your_keyboard_sound_just_like/)
  (22 puntos) y [«Violet Evergarden Typewriter Sounds for Mech
  Vibes»](https://www.reddit.com/r/VioletEvergarden/comments/1ltfql7/violet_evergarden_typewriter_sounds_for_mech/)
  (24 puntos), ambos vía Arctic Shift. Para la lámina: el «clac-clac» de las
  teclas es un sonido-marca de la serie, tan reconocible como la música.
- Análisis de sonido en español (ep. 3): un blog académico sobre animación
  japonesa describe la apertura del capítulo 3 con una **campana metálica grande
  en primer plano** que pasa a ambiente, **foley claro de botas sobre piso duro**
  cuando Violet camina por la ciudad, y música que «invade, con nivel alto,
  pregnante, con espectro de gotitas de agua» ⚠️ (una sola fuente, sin minuto
  exacto ni nombre del diseñador de sonido) —
  [tallerabiertodeanimacionjaponesa.blogspot.com](https://tallerabiertodeanimacionjaponesa.blogspot.com/2020/05/un-buen-augurio-lo-sonoro.html).
  No encontré el nombre del diseñador de sonido de la serie en ninguna fuente
  (busqué en español e inglés: «Violet Evergarden sound design interview», «音響
  ヴァイオレット・エヴァーガーデン»); si se necesita, buscar en japonés en el
  artbook o el Blu-ray commentary, que no pude abrir desde aquí.

### Punto 10 · Vídeos: tráilers, escenas, análisis y tendencias (con minuto)

- **Tráiler oficial subtitulado en español** (Netflix), reescape en Dailymotion
  (FilmAffinity), 1:28, mirado completo ✅. Contenido con minutos:
  - 0:00-0:10 escena de tren/estación (introducción)
  - 0:12-0:16 texto «Era un instrumento, sin corazón»
  - 0:18 logo «VIOLET EVERGARDEN» sobre vista aérea de Leiden (ciudad costera)
  - 0:20-0:34 presentación de personajes con su reparto **japonés** en pantalla:
    Claudia Hodgins (cv 子安武人, Takeshi Kusao), Benedict Blue (cv 内山昂輝, Kōki
    Uchiyama), Cattleya Baudelaire (cv 遠藤綾, Aya Endo) tecleando la máquina de
    escribir, Erica Brown (cv 茅原実里, Minori Chihara — la misma actriz que canta
    el ending)
  - 0:38-0:40 texto «UNA CHICA QUE ERA UNA SOLDADO»
  - 0:40-0:46 escena de guerra/batalla con humo
  - 0:48-1:00 Violet (cv 石川由依, Yui Ishikawa) frente al mar de Leiden
  - 0:56 **Gilbert Bougainvillea** (cv 浪川大輔, Daisuke Namikawa), de perfil en
    calle nocturna — ver ficha de color arriba
  - 1:00-1:04 texto «COMIENZA UNA NUEVA VIDA» / 「新たな人生を歩み始める」
  - 1:10-1:16 texto «AÚN NO CONOCE EL SIGNIFICADO DE "TE QUIERO"»; créditos en
    pantalla: dirección **石立太一** (Taichi Ishidate), guion/composición de serie
    **吉田玲子** (Reiko Yoshida), diseño de personajes **高瀬亜貴子** (Akiko
    Takase), animación **京都アニメーション** (Kyoto Animation)
  - 1:24-1:28 título final y logo de producción
  - Todo ✅ (visto directamente; los nombres del staff ya los tenía la biblia por
    otras fuentes, ahora confirmados también en pantalla del tráiler oficial).
  [Enlace con minuto](https://www.dailymotion.com/video/x7t0he2?t=56) (Gilbert).
- **Análisis y tendencias que ya traía `datos-video.md`** (búsquedas de
  recolectar.py): los enlaces de YouTube de análisis en español, coreano y chino,
  y los de TikTok, **no los pude abrir** (YouTube pide inicio de sesión; TikTok
  no cargó el reproductor sin JS desde este contenedor). Quedan tal cual estaban,
  sin minuto: ⚠️ pendientes de que alguien con YouTube disponible los mire.
- Nuevo hallazgo de tendencia: el propio fandom en Reddit trata el tecleo de la
  máquina como contenido de vídeo/audio para compartir (ver punto 9): esto es en
  sí una «tendencia» reconocible, más allá de TikTok.

### Punto 14 · Poses analizadas por personaje (6-10 fotogramas, capítulo y minuto)

La tabla de la biblia (§15) ya tenía a Violet, Hodgins, Cattleya, Benedict, Iris
y Erica con posturas «de memoria ⚠️». Confirmé algunas mirando los fotogramas y
**añado a Gilbert Bougainvillea**, que el encargo pide como personaje inicial y
no estaba en esa tabla.

**Gilbert Bougainvillea** (nuevo, no estaba en la biblia)

| # | Escena | Minuto | Qué pasa | Postura (vista, no de memoria) | Sirve para |
|---|---|---|---|---|---|
| 1 | Tráiler oficial | 0:56 ([enlace](https://www.dailymotion.com/video/x7t0he2?t=56)) | Presentación de personaje, cv 浪川大輔 en pantalla | De perfil, quieto, mirada al frente fija hacia algo fuera de cuadro, en una calle nocturna con faroles y gente borrosa al fondo; chaqueta oscura con un pin/insignia en la solapa | **Pensar / presentar** (mirada seria, distante) |

**Confirmaciones y correcciones sobre lo que ya había (viendo el fotograma, no de memoria)**

- **Violet, ep. 11 (paracaídas)** — postura nueva que la biblia no tenía: cae de
  espaldas a cámara con el paracaídas abierto sobre bosque nevado al atardecer
  (00:10:09-00:10:15 del episodio; [clip 0:09](https://www.dailymotion.com/video/x8qbypz?t=9)).
  Sirve para **animar/celebrar** (acción, rescate) más que para «explicar»: es la
  pose de Violet más física y menos administrativa de toda la tabla.
- **Violet, ep. 1 (hospital, día 120)** — pose nueva: tumbada mirando el techo,
  después sentada al borde de la cama escribiendo con la mano protésica sobre un
  papel que tiembla ([clip 0:18](https://www.dailymotion.com/video/x947zqa?t=18)).
  Sirve para **pensar** (antes de «presentar»): es el origen de todas las cartas
  que escribirá después.
- **Violet, opening 0:21** — bust cerrado, mirada neutra/seria de frente, pelo al
  viento, fondo de campo y cielo: coincide con la descripción que ya tenía la
  biblia en otras entradas («mirada firme»); confirmo que el broche se ve
  claramente sobre el lazo del cuello, no escondido. [Enlace](https://www.dailymotion.com/video/x8c9bet?t=21).
- Las poses de Hodgins, Cattleya, Benedict, Iris y Erica de la tabla ya existente
  (§15 de la biblia) **no las pude confirmar por fotograma**: ninguno de mis 6
  vídeos las contiene (son escenas de oficina de los ep. 1-3 y del especial, que
  no encontré sueltas en Dailymotion/Internet Archive). Siguen con el ⚠️ «de
  memoria» que ya tenían; alguien con acceso a YouTube o al episodio completo
  debería confirmarlas.

---

## Lo mejor para la lámina

1. La escena del **hospital, ep. 1 (00:01:19-00:01:34)**: Violet dicta su primer
   texto («solicito una pronta reintegración al servicio») sin saber aún lo que
   es escribir con el corazón. Es el origen de #poemas.
2. El **tecleo de la máquina de escribir** como sonido-marca: el fandom lo
   recrea en su propio teclado (dos guías en Reddit). Para la lámina, ese sonido
   vale más que cualquier música de fondo.
3. **Gilbert** de perfil en la calle nocturna (tráiler, 0:56): pose seria, de
   pensar, con luces cálidas de fondo — sirve si el canal necesita al personaje
   secundario más buscado sin repetir la pose de las ilustraciones oficiales.
4. El broche verde medido en `#4C8669`: más verde-oliva que el estimado de la
   biblia; usar este tono si se pinta el broche en detalle.
5. El paracaídas del ep. 11 como imagen de acción real de Violet (no sólo
   sentada escribiendo): equilibra la lámina si se quiere mostrarla «viva» y no
   sólo de oficina.

## No encontré

- ⚠️ La secuencia **animada** del ending «Michishirube» (sólo el vídeo musical de
  acción real): probé Dailymotion (búsquedas «Violet Evergarden ending»,
  «Violet Evergarden ED みちしるべ», «Chihara Minori») e Internet Archive
  (`violet evergarden ending`, `violet evergarden michishirube`); AnimeThemes dio
  522 dos veces.
- ⚠️ Los análisis en español/coreano/chino y los TikTok que ya listaba
  `datos-video.md`: no cargaron sin YouTube ni JavaScript de TikTok desde este
  contenedor.
- ⚠️ Fotogramas en 1080p+ de cualquier escena: las fuentes que sí pude usar
  (Dailymotion, el mp4 de Internet Archive) están todas por debajo de esa
  resolución (512×288 a 854×480). El único archivo en 1080p que localicé es la
  película completa en `archive.org/details/violet-evergarden-720p-complete`
  (10,6 GB): demasiado pesado para bajar en esta tanda.
- ⚠️ Nombre del diseñador de sonido / equipo de Foley de la serie: busqué en
  español e inglés, no lo encontré (habría que ir al artbook o al commentary del
  Blu-ray, en japonés).
- Poses de Hodgins, Cattleya, Benedict, Iris y Erica ya en la biblia: no había
  vídeo suyo entre mis 6 fuentes para confirmarlas por fotograma (ver punto 14).

---

## Bitácora de búsqueda (esta tanda)

- Español: «Violet Evergarden diseño de sonido máquina de escribir efectos
  sonido entrevista» (WebSearch) → un blog de análisis de sonido del ep. 3, sin
  nombre de diseñador.
- Inglés: «"Violet Evergarden" parachute scene episode flashback soldiers snow
  forest» (WebSearch) → identifiqué el episodio 11 y el nombre del soldado
  (Aidan) y de quien busca (Maria); confirmado después con el subtítulo japonés.
- API de Dailymotion (`api.dailymotion.com/videos?search=…`), directa con curl,
  varias veces: «Violet Evergarden ending michishirube», «Violet Evergarden ED
  みちしるべ», «"Violet Evergarden" ED», «Violet Evergarden ending theme», «Violet
  Evergarden Chihara Minori», «violet evergarden opening full» — sin encontrar
  la secuencia animada del ending.
- `archive.org/advancedsearch.php`: «violet evergarden ending», «violet
  evergarden michishirube», «violet evergarden episode» → encontré el vídeo
  musical del ending y descarté los demás resultados (no son la serie).
- `api.animethemes.moe`: dos intentos, error 522 las dos veces (confirma lo que
  ya decía `datos-video.md`).
- Arctic Shift (Reddit): `subreddit=VioletEvergarden&query=typewriter sound` →
  las dos guías de «sonido de teclado igual al de Violet».
- Clon parcial (`git sparse-checkout`) de
  `github.com/Ajatt-Tools/kitsunekko-mirror`, carpeta
  `subtitles/anime_tv/Violet Evergarden`, para cruzar minutos exactos de los
  episodios 1 y 11 (búsquedas de texto japonés: «パラシュート», «飛行機», «メナス»,
  «アイデン», «マリア», «120»).
- Herramientas: `fotogramas.py` ×6 vídeos (ver tabla arriba), `estilo.py
  --colores` sobre 7 fotogramas sueltos, Pillow directo para medir puntos
  concretos (broche, ojos, chaqueta) que `estilo.py` promediaba con el fondo.

Sigue: nada obligatorio pendiente de los puntos 2, 4, 9, 10 y 14. Lo que falta
(1080p, ending animado, TikTok/YouTube, poses de los secundarios de oficina,
nombre del diseñador de sonido) queda documentado arriba en «No encontré» por
ser extras que dependían de acceso bloqueado en este contenedor, no de puntos
obligatorios sin intentar.
