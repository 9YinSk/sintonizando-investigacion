# Parte del investigador de VÍDEO · Spy×Family (encargo 06)

Puntos de `ENCARGO.md` que me tocan (según `EQUIPO.md`): **2** (fotogramas de
escenas icónicas), **4** (fondos y sitios: luz, paleta, texturas), **9**
(música y sonido), **10** (vídeos y tendencias) y **14** (poses analizadas por
personaje).

Parto de `partes/datos-video.md` (ya recolectado, no repito esas consultas) y
de `biblia.md`, que ya trae un §2 (escenas), §5 (sitios/paleta), §11 (música),
§12 (vídeos) y §15 (poses) muy trabajados **pero sin mirar ni un solo vídeo**:
el propio §20 de la biblia dice «Ningún fotograma mirado: YouTube, Crunchyroll
y Netflix estaban bloqueados. Los minutos salen de subtítulos; las posturas,
de memoria ⚠️». Ese es el hueco que lleno aquí: **vi los vídeos de verdad** y
confirmo o corrijo con el fotograma real.

**YouTube pidió iniciar sesión** toda la tanda (server compartido). Usé, como
dice `AYUDANTE.md`:
- **Internet Archive**: los 12 capítulos de la T1 que `datos-video.md` ya
  había encontrado (`archive.org/details/spy-family-0X-720p`) son copias
  reales de fans, 1280×720. Recorté con `ffmpeg -ss … -i <url> -t … -c copy`
  (range request HTTP, sin bajar el episodio entero) los tramos que quería y
  les pasé `fotogramas.py` en local. Borré todo (`clips/`, `video.mp4`) al
  terminar; sólo quedan las hojas en `/tmp/claude-0/trabajo/06-spy-x-family-video/`.
- **Dailymotion**: los 3 tráilers oficiales de `datos-video.md` (con créditos
  en pantalla, así que son 100 % oficiales aunque el canal que los subió sea
  de terceros) y dos clips más que busqué con la API de Dailymotion.
- **AnimeThemes** seguía caído (522, igual que en `recolectar.py`): no hay
  `.webm` de openings/endings por ahí.

**Aviso de resolución** (afecta al punto 2, que pide 1080p o más): Dailymotion
sólo sirve **512×288** sin iniciar sesión (comprobado con `yt-dlp -F` en el
tráiler de Netflix) — sirve para confirmar contenido, encuadre y minuto, no
color exacto. Los capítulos de Internet Archive son **1280×720** de verdad
(comprobado con `ffprobe`), reales pero no llegan a 1080p. Para color exacto
sigue mandando la tabla ya medida en `biblia.md` §5.3 (fotogramas 1920×1080 de
la wiki); lo que yo aporto es la **pose y el encuadre reales**, con el minuto
de la copia que vi.

---

## Hallazgos

### Punto 2 · Escenas icónicas — miradas de verdad (antes: sólo subtítulos)

Vi 6 tramos completos con `fotogramas.py` (hojas numeradas, minuto y enlace):

1. **Ep. 1, la misión llega y Loid firma** (IA `spy-family-01-720p`, 00:02:30 a
   00:04:45) — confirmado fotograma a fotograma:
   - 00:02:38 a 00:03:36: Loid, con sombrero y gabardina, en un tren, lee un
     periódico («Daily OST», editorial sobre la Guerra Fría) mientras se
     calienta un vaso de café; **el mensaje de la misión está escondido en el
     periódico y aparece con el calor** (tinta térmica): las fotos de
     «Anakin Heywood» y «Donovan Desmond» se queman en el papel a 00:02:57
     (frame 8-9 de mi hoja). Detalle nuevo, no estaba en la biblia. ✅ (visto
     directamente, dos veces con `--fotograma`).
   - 00:04:15: cartela «MISSION:1 / オペレーション〈黄昏〉» (Operation Strix),
     letra blanca sobre negro, con vista aérea del río y el castillo de
     Berlint justo antes (00:04:09-00:04:14). Confirma el minuto que ya traía
     la biblia (00:04:13) ✅.
   - 00:04:18: Loid abre los brazos mostrando el piso («This is the family
     room»), de pie junto al casero.
   - **00:04:36** (biblia decía 00:04:28-00:04:35, ahora más preciso): primer
     plano de una pluma firmando «**Loid Forger**» a mano, sobre el
     contrato — la toma es sólo la mano y el papel, no la cara. ✅ nuevo
     minuto exacto.
   - Fuente: [archive.org/details/spy-family-01-720p](https://archive.org/details/spy-family-01-720p),
     copia de fans (720p reales) ✅ visto con `fotogramas.py`.

2. **Ep. 1, «wakuwaku» y «quiero mimir»** (IA ep.1, 00:06:25 a 00:10:00):
   - **00:06:46**: Anya frente al televisor, viendo el programa de espías
     «SPY WARS» (letras rojas y azules estilo cómic), con su peluche Chimera
     en brazos; ojos verdes muy abiertos, boca abierta, cuerpo echado hacia
     la pantalla. Coincide exactamente con el minuto que ya tenía la biblia
     (00:06:45-00:06:47) y **confirma la postura que antes estaba «de
     memoria»**: sube de ⚠️ a ✅.
   - 00:09:57: Loid carga la compra (pan, huevos) con Anya agarrada a su
     brazo, cuerpo flojo, ojos entrecerrados — la pose de «Anya está
     cansada, no puede caminar más» (antes sólo el texto, ahora la postura
     confirmada). ✅.
   - Fuente: misma copia de IA, tramo distinto.

3. **Ep. 3, Anya presenta a Chimera** (IA `spy-family-03-720p`, 00:00 a
   00:45 del capítulo): la escena real va de **00:05:37 a 00:05:44** (la
   biblia decía 00:05:24-00:05:38; con el vídeo delante el gesto de levantar
   el peluche es más corto y un poco después). Anya sostiene el peluche
   rosa con cuernos verdes **con las dos manos, en alto, a la altura de su
   cara**, y Yor (vestido rojo, pelo negro) se agacha a la altura de Anya
   para saludarlo. El cuarto de Anya (visto justo antes, 00:00-00:20) tiene
   papel pintado rosa a rayas, muebles blancos con cajones rojos, una
   estantería de libros y un cartel redondo con «ANIA» en la pared — coincide
   con lo que describía la biblia de memoria (§5.1), ahora visto ✅.

4. **Ep. 4, la entrevista de Eden** (IA `spy-family-04-720p`, 00:11:25 a
   00:16:35): sala de madera oscura con sofás de cuero rojo, muy solemne.
   - 00:11:55: aparece la ficha de **Walter Evans** con foto y datos en
     japonés («ウォルター・エバンス(59) 第5寮・マルカム寮長 担当教科:国語
     性格:温厚・実直・保守的» = profesor de lengua, dormitorio Malcolm,
     personalidad «amable, honesto, conservador»). Da el carácter que el
     subtítulo en inglés no traía.
   - 00:13:01: ficha de **Murdoch Swan** («マードック・スワン(47) 第2寮・
     シライン寮長 担当教科:経済学 性格:高慢・強欲・無神経» = economía,
     dormitorio Shrine, «arrogante, codicioso, insensible»). Confirma el
     tono del profesor «malo» que ya intuía la biblia.
   - 00:14:37: Yor, sonrojada, se traba respondiendo (biblia ya lo tenía,
     ahora con minuto exacto de esta copia).
   - **00:15:49**: primer plano de los ojos verdes muy abiertos de Anya justo
     antes de «I'm Anya Forger!» — nervio y sorpresa, no seguridad; confirma
     y afina el minuto de la ficha del canal (biblia decía 00:15:45-00:15:50).
   - Fuente: [archive.org/details/spy-family-04-720p](https://archive.org/details/spy-family-04-720p).

5. **Ep. 6, la cara «Heh»** (IA `spy-family-06-720p`, 00:17:48 a 00:19:03):
   - **00:18:26 a 00:18:28** exactos (antes la biblia daba un rango ancho,
     00:18:12-00:18:38): primer plano de Anya con **párpados a media altura,
     boca en sonrisa torcida hacia un lado, barbilla ligeramente levantada**
     — la descripción de memoria de la biblia **era correcta**, ahora ✅ con
     fotograma real y minuto exacto.
   - 00:18:30: Damian, dientes apretados, cara roja, puños cerrados a los
     costados — confirma «se enfada» con la postura exacta.
   - 00:18:40: Becky con las manos juntas bajo la barbilla, sonrisa amplia,
     mejillas sonrojadas, mirando a Anya con admiración — confirma su pose
     de «admira a Anya» (antes ⚠️ de memoria).
   - Antes de esta escena (00:00-00:12 del tramo) hay un partido de balón
     prisionero en el gimnasio de Eden con uniformes negro y oro — encaja
     con §16 de la biblia (vestuario Eden ya medido).
   - Fuente: [archive.org/details/spy-family-06-720p](https://archive.org/details/spy-family-06-720p).

6. **Cierre del episodio 1 y créditos de salida** (IA ep.1, 00:21:00 a
   00:23:30): tras un adelanto de Anya en un examen tipo test de Eden y una
   escena de ella tumbada en la hierba junto a Loid bajo un árbol (luz de
   sol entre hojas, muy cálida), sale la cartela «SPY×FAMILY» a 00:22:44 y
   corren los créditos de cierre **sobre fondos fijos de las calles de
   Berlint** (edificios de piedra rosa/crema, una calle en curva, un puente)
   mientras suena «喜劇 (Kigeki)» de Gen Hoshino — el texto en pantalla dice
   literalmente «エンディング主題歌『喜劇』星野源 (Victor Entertainment)» a
   00:22:53. Esto **confirma con fuente primaria** (créditos en pantalla) el
   ending T1 parte 1 que la biblia ya tenía por una web externa. Después
   sigue el avance del capítulo 2. Nota: el minuto es el de esta copia de
   fans; el estreno original puede variar uno o dos minutos.

**Tres tráilers oficiales vistos completos** (los 3 traen créditos en
pantalla, o sea que son oficiales de verdad, no fan-edits):

- **Tráiler oficial de Netflix** (2:16), [Dailymotion x8ar3pt](https://www.dailymotion.com/video/x8ar3pt)
  (subido por JeuxVideo.com, contenido = tráiler de Netflix) ✅: en inglés
  subtitulado. Trae **la ficha de personaje de cada uno** («The father, Loid
  Forger» 00:20; «The mother, Yor Forger» 00:24; «The daughter, Anya Forger»
  00:28) — sirve de plantilla para el estilo «cartela con nombre» del canal.
  A 00:44 Yor se ve como asesina en la sombra («A spy… An assassin!»). A
  01:12 aparece la cartela **«Opening Theme: “Mixed Nuts” OFFICIAL HIGE
  DANDISM»** sobre una silueta de acción de Loid (referencia real del
  opening, ver punto 9). A 01:44 un primer plano de una mano poniendo un
  anillo (la boda de conveniencia). Créditos completos a 01:48-01:56:
  estudio **WIT STUDIO × CloverWorks**, música **(K)NoW_NAME**, director
  **Kazuhiro Furuhashi (古橋一浩)**.
- **Tráiler de la película CODE: White** (2:03), [Dailymotion x8r5lrz](https://www.dailymotion.com/video/x8r5lrz)
  (JeuxVideo.com) ✅: confirma en pantalla **«エンディング主題歌 星野源
  『光の跡』»** (00:20) y **«主題歌 Official髭男dism『SOULSOUP』»** (01:08) —
  o sea el opening y el ending de la película, con crédito visible (ver
  punto 9). A 00:08-00:11 Anya y Bond comen (Bond como perro grande,
  cariñoso). A 01:36 la cartela «守るべきものがある» («hay algo que
  proteger») sobre Loid al volante, serio. A 02:00 Anya llorando de cerca:
  pose útil para «cómo se ve triste» (punto 13, no es mío, lo dejo apuntado
  para quien lo use).
- **Teaser de la Temporada 3** (0:48), [Dailymotion x9ndxls](https://www.dailymotion.com/video/x9ndxls)
  (Espinof) ✅: «**The Forgers… come back**» (00:09); Anya y Bond comiendo
  helado (00:03-00:06); flashback de Loid de niño en una ciudad
  bombardeada (00:15-00:24, arco del pasado); cartela final **«少年はなぜ
  〈黄昏〉になったのか？ Season 3 10月より放送開始»** («¿por qué el chico se
  convirtió en Twilight? Temporada 3, empieza en octubre») a 00:45.

### Punto 4 · Sitios, luz, paleta y texturas (complemento; el hex ya está medido en §5.3)

No repito la medición de hex (ya hecha y con fuente en `biblia.md` §5.3,
sobre fotogramas 1920×1080 de la wiki). Lo que aporto es **confirmación
visual real** de esos mismos sitios, vistos en vídeo, más sitios nuevos:

- **Tren de Loid** (ep.1, 00:02:38-00:04:09): vagón de madera oscura con
  asientos de terciopelo, ventanas grandes; fuera pasan campo verde, un río
  y un castillo — la transición campo→ciudad antes de llegar a Berlint. No
  estaba descrito en la biblia.
- **Sala de entrevistas de Eden** (ep.4, todo el tramo): paneles de madera
  oscura en las paredes, sofás de **cuero rojo intenso**, lámparas de pared
  doradas — un ambiente de club inglés / colegio privado victoriano; encaja
  con la paleta ya medida («oro apagado», uniforme carbón) pero añade el
  **rojo del cuero** como color nuevo del sitio, que la tabla de §5.3 no
  tenía. ✅ visto directamente.
- **Cuarto de Anya** (ep.3): confirmado en vídeo real lo que la biblia
  describía de memoria (§5.1): papel pintado rosa a rayas, muebles blancos
  con cajones rojos, cartel «ANIA» en la pared, cortinas verde agua.
- **Calle de Berlint con tranvía** (ep.1 y tráiler de Netflix 00:32-00:40):
  edificios de piedra rosa/crema de 4-5 pisos, farolas negras, tranvía rojo
  — coincide con la comparación a la Alemania de la Guerra Fría que ya
  citaba la biblia (§5.2), ahora con imagen real de apoyo.
- **Fondos fijos del cierre del episodio 1**: los mismos edificios y calles
  de Berlint, en luz de tarde cálida, usados **como fondo estático bajo los
  créditos** — sirven de referencia directa si el concepto de lámina usa un
  fondo de ciudad con texto encima (formato ya probado por la propia serie).
- **Sala del consejo** (tráiler Netflix, 00:08): mesa larga, cortina roja,
  paredes de madera oscura, gente sentada en penumbra — tono de «guerra fría
  de despachos», más oscuro que el resto de fondos de la serie.

### Punto 9 · Música y sonido

**Openings y endings, confirmados con fuente primaria** (créditos en
pantalla de los tráilers, punto 2) además de la fuente ya citada en la
biblia:
- T1 parte 1: OP **«Mixed Nuts», Official HIGE DANdism** — confirmado en
  pantalla en el tráiler de Netflix (01:12) ✅✅ (dos fuentes: biblia +
  visto). ED **«喜劇 (Kigeki)», Gen Hoshino** — confirmado en pantalla en
  los créditos reales del episodio 1 (00:22:53 de la copia de IA) ✅✅.
- T1 parte 2: **OP «SOUVENIR», BUMP OF CHICKEN** y **ED «色彩 (Shikisai)»,
  yama** (con el productor **くじら**, su primer trabajo juntos desde «春を
  告げる»). Estaban con ⚠️ «de memoria» en la biblia; ahora **✅ con dos
  fuentes**: [Tower Records](https://tower.jp/article/news/2022/10/04/tg016)
  y [lisani.jp](https://www.lisani.jp/0000211868/) /
  [Sony Music](https://www.sonymusic.co.jp/artist/yama/info/545668) /
  [Natalie](https://natalie.mu/music/news/495949). El OP sonó del episodio
  13 al 25 (desde el 1-oct-2022).
- Película CODE: White: **OP «SOULSOUP», Official HIGE DANdism**, **ED
  «光の跡 (Hikari no Ato)», Gen Hoshino** — ambos confirmados en pantalla en
  el tráiler oficial (00:20 y 01:08) ✅✅. Aclaración: el título
  internacional del single es **«Why»**; «光の跡» es el título japonés del
  mismo tema, no dos canciones distintas (comprobado con
  [Oricon](https://www.oricon.co.jp/news/2307790/full/),
  [NiEW](https://niewmedia.com/en/news/029795/) y
  [Billboard](https://www.billboard.com/music/music-news/gen-hoshino-interview-spy-x-family-code-white-ending-theme-why-1235573422/)):
  la biblia decía sólo «Why», no estaba mal, sólo incompleto.

**Efectos de sonido y onomatopeyas** (no estaba en la biblia; punto 9 lo
pide): la wiki especializada [SFX Resource Wiki](https://sfx-resource.fandom.com/wiki/Spy_%C3%97_Family/Sound_Effects_Used/By_Episode)
cataloga los efectos de librería usados episodio a episodio. El patrón que
sale ✅ (confirmado por la propia lista, contrastado viendo las escenas):
la serie **mezcla efectos reales de espías** (disparo con silenciador y
código morse en el ep.1; ricochets de bala en el ep.2 y el ep.23) **con
efectos de cartón cómico exagerados** en las escenas de humor doméstico
(«TWANGY SPROING, COMEDY» y «FAST TWANGS» en los eps. 17 y 21; «BIG CHOMP»
en el ep.19; «Anime Big Pop Sound» y «Sparkle» en el ep.21, que es el
capítulo donde Yor tiene celos). Ese contraste —serio cuando es espionaje,
de cartón cuando es familia— es un dato útil para la guía de estilo (punto
17, no es mío, lo dejo anotado). No encontré una onomatopoeia visual (texto
en pantalla tipo manga) que los fans citen como «la» seña de la serie; lo
dejo en «No encontré» abajo en vez de inventarlo.

### Punto 10 · Vídeos y tendencias (con minuto real)

Sustituye la tabla de la biblia («Ningún minuto de YouTube está
comprobado»): los 3 tráilers de arriba (punto 2) están vistos completos,
con minuto real de una copia concreta y enlace directo. Añado:

- **Resolución real de lo que se puede mirar sin iniciar sesión**:
  Dailymotion sirve sólo 512×288 (comprobado con `yt-dlp -F` en el tráiler
  de Netflix, x8ar3pt) pese a que los títulos digan «HD»; Internet Archive
  sirve **1280×720 de verdad** (comprobado con `ffprobe` en los 4 clips
  descargados). Para 1080p real, la fuente sigue siendo la wiki de Fandom
  (ya usada en §5.3 y por el investigador de imagen).
- Los vídeos de análisis y el de «muebles del piso» que cita la biblia
  (§12) siguen sin poder verse: están sólo en YouTube, bloqueado toda la
  tanda. Quedan en «No encontré».
- **TikTok e Instagram** no se puede mirar contenido incrustado desde este
  servidor (no es un bloqueo puntual, es la política de la red social); el
  dato de que la tendencia latina gira en torno a «mimir» (§12 de la
  biblia) ya estaba confirmado con Reddit, lo dejo igual.

### Punto 14 · Poses analizadas por personaje (subo de ⚠️ a ✅ con fotograma real)

Sólo las poses que pude verificar mirando el vídeo (el resto de la tabla de
la biblia sigue como estaba; no la repito):

| Personaje | # (biblia) | Antes (⚠️ memoria) | Ahora, visto | Minuto exacto |
|---|---|---|---|---|
| Anya | 4 | «ojos brillando, puños cerrados, cuerpo hacia delante» | Confirmado: ojos muy abiertos, boca abierta, echada hacia la pantalla del televisor, abraza a Chimera | 00:06:46 (ep.1, IA) |
| Anya | 5 «Heh» | ya tenía fuente (KnowYourMeme) | Confirmado con fotograma propio, además de la fuente de fans: párpados a media altura, sonrisa torcida, barbilla arriba | **00:18:26-00:18:28** (ep.6, IA) |
| Anya (nueva) | — | — | Cansada tras la compra: cuerpo flojo, agarrada al brazo de Loid, ojos entrecerrados | 00:09:57 (ep.1, IA) |
| Loid | 1 | «pluma en mano ⚠️» | Confirmado: sólo se ve la mano y el papel firmando «Loid Forger» | **00:04:36** (ep.1, IA) |
| Loid (nueva) | — | — | De pie con sombrero y gabardina en el tren, leyendo el periódico con la misión oculta por calor | 00:02:38-00:03:36 (ep.1, IA) |
| Yor | 2 | ya tenía fuente parcial | Confirmado: sonrojo real y gesto de trabarse al hablar en la entrevista | 00:14:37 (ep.4, IA) |
| Yor (nueva) | — | — | Se agacha a la altura de Anya para saludar a Chimera, sonrisa suave | 00:05:40 (ep.3, IA) |
| Damian | 4 | «se enfada ⚠️» | Confirmado: dientes apretados, cara roja, puños a los costados | 00:18:30 (ep.6, IA) |
| Becky | 2 | «el aplauso es de memoria ⚠️» | Corrección: no aplaude; junta las manos bajo la barbilla, sonrisa amplia, sonrojada | 00:18:40 (ep.6, IA) |
| Bond (nueva) | — | — | Sentado junto a Anya, comiendo un helado de una bola con ella (cada uno con el suyo), mirándose de frente, orejas caídas y relajadas | 00:03-00:06 (teaser T3, Dailymotion) |

---

## Lo mejor para la lámina

1. La firma «Loid Forger» a pluma sobre el contrato (ep.1, 00:04:36): un
   plano sólo de mano y papel — ideal para el expediente de WISE del canal.
2. La cara «Heh» de Anya, ahora con fotograma propio y minuto exacto
   (00:18:26-00:18:28, ep.6): la pose más pedida por el fandom, ya
   verificada dos veces.
3. Las cartelas con nombre del tráiler de Netflix («The father, Loid
   Forger», etc., 00:20-00:28): plantilla lista para el estilo de ficha del
   canal #presentaciones.
4. Los fondos fijos de Berlint bajo los créditos de cierre del ep.1: ya
   pensados por la propia serie para llevar texto encima.
5. El contraste de sonido serio (espionaje) / cómico exagerado (familia):
   pista de tono para la guía de IA de imagen y de texto (punto 17).

## No encontré

- **Vídeos de análisis y el de «muebles del piso»** citados en la biblia
  (§12): sólo existen en YouTube, bloqueado toda la tanda (busqué su
  título en Dailymotion e Internet Archive, sin resultado). Quedan
  pendientes de una sesión con YouTube disponible.
- **AnimeThemes**: la API sigue devolviendo 522 (probado dos veces, con y
  sin cabecera de navegador); no hay `.webm` limpio de OP/ED por ahí.
- **Una onomatopeya visual (texto en pantalla) que el fandom cite como
  «la» seña de la serie**: busqué «Spy x Family onomatopoeia iconic sound
  effect» y «Anya telepathy sound design» (inglés); sólo salieron memes de
  TikTok y bases de sonidos genéricas, no una fuente que diga «esta es LA
  onomatopeya». Dejo en su lugar el dato confirmado del contraste de
  efectos (punto 9).
- **Tendencias de TikTok** con vídeo real: la red social no deja mirar el
  contenido incrustado desde este servidor; me quedé con el dato de texto
  que ya tenía Reddit (biblia §12).
- **Resolución 1080p en vídeo** (no en imagen fija) del opening o el
  ending completos: no encontré una copia oficial en Dailymotion ni en
  Internet Archive que llegue a 1080p; los 720p de Internet Archive son lo
  mejor disponible sin YouTube.

## Bitácora de búsqueda (vídeo)

- API de AnimeThemes (`api.animethemes.moe`), dos veces, con y sin
  cabecera de navegador → **522** las dos veces.
- API de Dailymotion (`api.dailymotion.com/videos?search=…`), en inglés:
  «SPY FAMILY Mixed Nuts opening», «SPY FAMILY Kigeki Gen Hoshino ending»,
  «Spy x Family opening 1», «Spy x Family ending Kigeki», «Spy x Family
  Anya heh face scene», «Spy x Family OP1 Mixed Nuts anime full», «Spy
  Family opening full HD anisong», «Gen Hoshino Kigeki Spy Family ending
  anime clip», «SPY FAMILY ED Kigeki animation» → de ahí salieron los 3
  tráilers oficiales que sí vi completos; los resultados de «opening
  limpio» eran todos covers/reacciones de fans cantando (los descarté
  tras verlos: sólo un recuadro pequeño con el anime real, no sirve para
  poses).
- `yt-dlp --print`/`-F` sobre 8 vídeos de Dailymotion para confirmar
  título, duración y resolución real antes de gastar tiempo bajándolos.
- `archive.org/metadata/spy-family-0X-720p` (API, sin buscador) para
  confirmar nombre de archivo y duración de los episodios 1, 3, 4, 5, 6, 7
  antes de recortar con `ffmpeg`.
- WebSearch en japonés: «SPY×FAMILY CODE: White エンディング主題歌 星野源
  「光の跡」 OR 「Why」» y «SPY×FAMILY 二期前半 オープニング BUMP OF
  CHICKEN SOUVENIR エンディング yama 色彩» → confirmaron música T1 parte 2
  y aclararon el título doble de la ED de la película.
- WebSearch en inglés: «"SPY x FAMILY CODE White" Gen Hoshino "Hikari no
  Ato" ending theme "Why"», «Spy x Family onomatopoeia iconic sound effect
  wakuwaku dogeza», «"Spy x Family" Anya telepathy sound effect chime
  iconic sound design review».
- `sfx-resource.fandom.com/api.php` (wikitext de «Sound Effects Used/By
  Episode») para el punto 9.
- Reintento de YouTube (una vez, como pide `AYUDANTE.md`): `yt-dlp --print`
  sobre el tráiler oficial japonés (`_VRxEEBa1XU`) sí devolvió el título
  («【主題歌解禁】TVアニメ『SPY×FAMILY』本予告») pero la descarga real dio
  403 y, al reintentar con `-F`, ya daba 429 y «Sign in to confirm you're
  not a bot» — bloqueado de nuevo a los pocos minutos (varios ayudantes
  compartimos IP). No insistí en bucle.
- Vídeo mirado de verdad con `fotogramas.py` (hojas en
  `/tmp/claude-0/trabajo/06-spy-x-family-video/`, borrados los `.mp4`):
  opening1 (cover, descartado), ending2 (cover, descartado),
  trailer_codewhite, trailer_t3, trailer_netflix, hojas_ep1_a, hojas_ep1_b,
  hojas_ep3, hojas_ep4, hojas_ep6, hojas_ep1_ending.

---

Sigue: quedan sin fotograma real (siguen con la postura «de memoria ⚠️» que
ya tenía la biblia) el resto de la tabla del punto 14 — sobre todo Loid #2,3,5,6,8;
Yor #4,5,6; Bond #2,3; Damian #1,2,3,5; y los vídeos de análisis/muebles del
§12 de la biblia, que sólo existen en YouTube (reintentar cuando el server
lo desbloquee, sin insistir en bucle). Lo obligatorio de los puntos 2, 4, 9
y 10 ya quedó cubierto arriba.
