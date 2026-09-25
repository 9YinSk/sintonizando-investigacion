# Investigador de VÍDEO · Chainsaw Man (puntos 2, 4, 9, 10, 14 de ENCARGO.md)

Parto de `partes/datos-video.md` (AniList, Dailymotion, Internet Archive,
MusicBrainz) y de lo que ya escribió la biblia en sus secciones 2, 5, 11, 12
y 15 (`python3 herramientas/seccion.py 11-chainsaw-man --rol video`). YouTube
pide iniciar sesión desde este servidor, así que **miré los vídeos de verdad
por Internet Archive y Dailymotion** (fotogramas.py), como pide AYUDANTE.md.
Aquí sólo dejo lo NUEVO o lo CORREGIDO: lo que ya estaba bien en la biblia no
lo repito.

Carpeta de trabajo (hojas de contacto e índices): `/tmp/claude-0/trabajo/11-chainsaw-man-video/`.

## Hallazgos

### Punto 2 · Escena icónica del cine — confirmada fotograma a fotograma

- La escena de la cita en el cine (película *Arco de Reze*) **existe también
  en un doblaje/subtitulado en inglés** en Internet Archive, item «Chainsaw
  Man - The Movie: Reze Arc (EN-Sub)»: <https://archive.org/details/rezearc>
  (100 min). Primero la exploré con `fotogramas.py` (hojas de contacto, que
  bajan el formato ≤720p del item, aquí 854×480) para no gastar banda de
  más; una vez elegidos los fotogramas que sirven, los **volví a sacar en
  1080p reales** apuntando `ffmpeg -ss <segundo> -i` directo a la URL del
  .mkv original (`archive.org/download/rezearc/csmrezearc.mkv`, 1920×1080,
  60 fps) con salto HTTP por rango: sale en segundos y no hace falta bajar
  el archivo entero (5.28 GB) para una sola imagen. Cumple el «1080p o más»
  del punto 2 para los fotogramas citados abajo. ✅ (dos fuentes: este
  vídeo + los subtítulos japoneses ya citados en la biblia; el orden y las
  líneas coinciden, con un desfase de **+15 a +20 s** entre este corte en
  inglés y el corte japonés que usó la biblia).
- **El cine se llama シネマ座 («Cinema-za»)**: se lee en el rótulo de la
  marquesina, letras plateadas en relieve sobre un panel verde azulado
  metálico, con 4 focos colgantes. Fotograma en 1080p real:
  `/tmp/claude-0/trabajo/11-chainsaw-man-video/marquee_1080.jpg`
  (minuto 9:12 de este corte, 1920×1080). ✅ — nombre nuevo, no estaba en
  la biblia.
- **La sala por dentro**: butacas en **tono mostaza/ámbar envejecido**, NO
  rojo vino como proponía la biblia (§5.3, marcado «propuesto»). Medido con
  `estilo.py` sobre el fotograma de la sala llena (7:44 de este corte,
  `cine_sueltos/fotograma_00464.jpg`): paleta dominante
  `#020202` (35%, negro de sala) · `#323124` (23%, penumbra oliva) ·
  `#544A36` (17%, butaca en sombra) · `#7C6D4A` (9%, butaca iluminada) ·
  `#C2B4A2` (1%, piel iluminada). ✅ corrige el hex `#6E1F24` propuesto.
- **El haz del proyector** es blanco cálido con un halo de aberración
  cromática verde-violeta alrededor (no azul frío `#CFE3F2` como se
  proponía): se ve clarísimo en el mismo fotograma de 7:44 (todo el público
  de espaldas, luz puntual arriba). ⚠️→ tono corregido, pero el halo de
  color exacto varía por plano (una sola escena medida).
- **La película que ven al final** (la que los hace llorar) tiene un
  **grado de color propio, verde-azulado desaturado**, distinto del resto
  de la cinta: campo, un soldado con gorra y tirantes, una mujer con pañuelo
  blanco en la cabeza, se abrazan al final. Parece un drama bélico/rural.
  Medido en el fotograma 9:50 de este corte
  (`filmdentro/fotograma_00590.jpg`): `#030403` 39% · `#151D1C` 27% ·
  `#415855` 14% · `#7A8E87` 12% · `#BAC2BC` 9% (verdes apagados y grises).
  ✅ visto directamente. No identifiqué qué película real homenajea esta
  «película dentro de la película» (ver «No encontré»).
- **Orden real de los minutos de la escena** (este corte EN-Sub, para
  contrastar con los de la biblia en japonés): 6:20 Denji y Makima en la
  biblioteca antes de la cita · 6:56 «¿vamos a una cita mañana?» · 7:08
  «llegaste una hora antes» · 7:24 «¿cuál es el plan?» · 7:36-7:40 «de sala
  en sala hasta medianoche» · 7:44 sala llena, música de acción · 8:00-8:16
  primeras críticas («no tuvo gracia», «qué caro se ve») · 8:28-9:08
  segunda y tercera película, popcorn, «la música estaba bien» · 9:12
  rótulo シネマ座, «dicen que es difícil» · 9:28 **«sólo encuentro una
  buena de cada diez, pero esa cambió mi vida»** (la frase del canal) ·
  9:43-10:22 la última película (el drama verde-azulado) · 10:25 Denji
  llora tapándose la boca («esta escena no importa nada», «que no me vea
  Makima») · 10:37 **Makima también llora**, se miran · 10:43 plano general
  de las dos siluetas en la sala, pantalla en blanco · 10:49-10:58 saliendo:
  «nunca voy a olvidar esa última escena» / «yo tampoco» / **«esa última
  película hizo que valiera la pena el precio de la entrada»**. ✅ (fuente:
  este vídeo, subtítulo en pantalla).
- Después de la cita (nuevo, no estaba en la biblia): caminando de noche,
  Denji pregunta «Makima, ¿tú crees que tengo corazón?» (11:00); al día
  siguiente Denji **saca una flor de una caja de donativos** para regalarle
  a Makima y piensa «eso también significa que tengo corazón» (11:52-12:40);
  más tarde, bajo la lluvia, decide pedirle ser su novia y se encuentra con
  Beam antes de la cabina de teléfono con Reze (13:00-14:08). ✅ (mismo
  vídeo). Sirve para un posible «concepto 2» con la flor de la caja de
  donativos, coherente con que Power le quite la flor al final (biblia §2.2).

### Punto 4 · Sitio, luz y paleta — colores medidos, no propuestos

- Reemplaza los hex «propuestos» de la biblia (§5.3) por estos, medidos con
  Pillow/`estilo.py` sobre fotogramas reales de `rezearc` (Internet Archive):
  - Butacas del cine: `#544A36` / `#7C6D4A` (mostaza-ámbar) — ✅, ver arriba.
  - Ambiente de sala a oscuras: `#020202` / `#151815` (casi negro con un
    verde apagado de fondo) — ✅.
  - Marquesina シネマ座 (panel exterior): `#282A2C` / `#464E4D` / `#758382`
    (gris azulado metálico), letras casi blancas `#9CADAD`-`#C2B4A2` — ✅,
    fotograma `cine_sueltos/fotograma_00552.jpg`.
- **Pelo de Makima en la película es rojo oscuro/granate, no rosa salmón**:
  medido en un fotograma de día, luz natural, sin tintes de escena
  (`makima_dia/fotograma_00412.jpg`, min. 6:52): `#481D1B` a `#552423`
  (varias muestras del cabello, promedio ≈ `#4C201F`). Los ojos siguen
  siendo ámbar/dorado, coherente con la guía de fans ya citada
  (`#E6C873`). ✅ — esto es una diferencia real entre el diseño de la
  **película** (2025, más roja) y el de la **serie de TV** (2022, más
  salmón/rosa, que sí coincide con `#D3978F` de anime-colors.com). Anotar
  en vestuario/personajes que Makima cambia de tono de pelo según el corte.
- Pelo de Denji, medido en fotograma real (`denji_poses/fotograma_00424.jpg`,
  min. 7:04): `#E1B760` (rubio dorado cálido), piel `#F2C89E`. ✅ coincide
  con lo ya dicho en la biblia, ahora con medición real en vez de memoria.
- **Texturas de ambientCG ya miradas** (la biblia §5.4 las dejó sin abrir,
  «no pude abrirlas»): bajé las miniaturas de las 9 candidatas y monté una
  hoja (`texturas/hoja_texturas.jpg`). Resultado: **Fabric022** (pana/terciopelo
  azul acanalado) y **Fabric026** (pana/terciopelo rojo acanalado) son las
  que tienen el **canalado de terciopelo de butaca de cine** correcto; hay
  que recolorearlas a mostaza/ámbar en el shader de Blender (el mapa de
  altura y rugosidad sirve igual, el color base no). Fabric004 (carbono),
  Fabric019 (nube blanca) y Fabric031 (tweed gris) no sirven para butaca.
  Para el **papel de la entrada**: **Paper005** y **Paper006** ya son de
  un crema/tostado muy parecido al `#EDE6D6` propuesto, con grano fino —
  mejor opción que Paper001/003 (blancos, sin ese tono cálido). ✅ (visual,
  miniaturas oficiales de ambientCG).
- Sitio nuevo (no estaba en la biblia): un **área de descanso de carretera**
  al atardecer (bancas de madera, montañas moradas de fondo, coches
  estacionados), donde Makima y Denji comen juntos en el episodio 2 —
  fotograma `power_poses/fotograma_00330.jpg` (min. 5:30 del episodio).
  Paleta de la puesta de sol: cielo `#696870` (malva apagado), siluetas de
  montaña `#23242F` (casi negro azulado). ⚠️ una sola fuente (mi propio
  fotograma); sirve como referencia de luz de atardecer para un fondo
  alternativo si la lámina necesita variedad.

### Punto 9 · Música — opening y ending vistos, no sólo leídos

- **Opening «KICK BACK» visto completo** desde Internet Archive (episodio 1,
  item `ep-03-cm/EP01CM.mp4`, min. 2:02-4:20 del archivo): empieza con un
  **prólogo/flashback de Denji sin música** (0:30-2:00: la choza, el bosque,
  los papeles con la deuda «-38,075,120», el encuentro con Pochita) y **el
  OP entra recién en el minuto 2:02** del episodio, no a los 34 s como decía
  un resultado de búsqueda (ese dato mezclaba episodio con versión musical
  suelta). ✅ visto directamente. Estructura del OP: planos de acción muy
  cortados (2:02-3:38, referencias de cine ya listadas en la biblia §11.1,
  incluida una sala de cine con público en 2:32-2:44 que refuerza el motivo
  «cine»), texto **«KICK BACK»** sobreimpreso (3:08-3:11), logo
  **チェンソーマン** en pantalla completa sobre fondo negro con efecto de
  distorsión digital (3:41-3:44), y cierre con Denji corriendo hacia cámara
  (4:05-4:20). Hoja: `/tmp/claude-0/trabajo/11-chainsaw-man-video/op2/hoja_01.jpg`.
- **El episodio 1 NO tiene ending animado**: de 24:00 a 24:16 sólo hay
  **texto blanco sobre fondo negro** (créditos de personal), sin ninguna
  imagen, mientras suena «Chainsaw Blood» (Vaundy). Lo vi directamente en el
  vídeo (`ed1/hoja_01.jpg`, fotogramas 24:00-24:16) y lo confirma un
  artículo dedicado: **CBR, «Every End Credit Sequence in Chainsaw Man
  Season 1, Explained»** (<https://www.cbr.com/every-end-credit-sequence-chainsaw-man-season-1-explained/>,
  búsqueda en inglés). ✅ (dos fuentes: vídeo + CBR). Es una referencia
  perfecta para la lámina del canal: **el propio anime usa «créditos de
  cine» en vez de animación** para su primer ending — refuerza el concepto
  de «butacas y entradas».
- **El episodio 2 sí tiene ending animado** («Time Left», ZUTOMAYO, según
  la lista ya citada en la biblia): lo vi en `ep-03-cm/EP02CM.mp4`, min.
  22:16-23:40. Estilo de **siluetas en paleta oliva/verde apagado con
  detalles dorados**, un electrocardiograma que se aplana (22:28-22:32,
  presagio visual), Tokio de noche, Denji tirado en el suelo mirando la
  tele solo. Hoja: `ed2/hoja_01.jpg`. ✅ visto directamente.
- **Sonido de cada película-dentro-de-la-película**: los subtítulos de
  sonido de este corte marcan un cue distinto para cada una de las 6
  películas que ven: **«[action music playing]»** (7:44, la de peleas que
  hace reír a todos menos a ellos), **«[viewers sniffling]»** (8:32, el
  drama que hace llorar a la sala a la fuerza) y **«[classical music
  playing]»** (8:52, la que Makima dice que «la música estaba bien»). Es
  diseño de sonido deliberado: cada género de «película falsa» tiene su
  propia música-ambiente. ✅ (mismo vídeo, subtítulo de sonido en pantalla).
- **Tráiler visto** (no sólo enlazado): Dailymotion, «'Chainsaw Man' -
  Trailer final del anime» (id `x8dsw0h`, ya estaba en `datos-video.md`),
  92 s completos con `fotogramas.py`. Confirma: crédito de Fujimoto Tatsuki
  y logo MAPPA en los primeros 16 s, plano de Power de perfil (0:20), ojos
  de Denji en primer plano (0:36), Chainsaw Man peleando contra un devil
  blanco con manchas rojas en el clímax (1:12-1:24), y pantalla de
  **staff/cast en japonés** al final (1:28). Hoja:
  `trailer_dm/hoja_01.jpg`. ✅.

### Punto 10 · Vídeos con minuto exacto — fuentes que sí cargan en este servidor

YouTube pide iniciar sesión en este contenedor (confirmado: los enlaces que
ya tenía la biblia §12 quedan «sin verificar» por eso). Lo que sí funcionó,
con **yt-dlp de verdad**, no sólo enlaces sueltos:

- Internet Archive, «Chainsaw Man - The Movie: Reze Arc (EN-Sub)»
  <https://archive.org/details/rezearc> — 100:08 min, 854×480 y 1920×1080
  (mkv 5.28 GB) disponibles. Usado para toda la escena del cine (2.1) y la
  escena posterior con la flor (arriba). ✅
- Internet Archive, «Chainsaw Man Season 1» (12 episodios sueltos,
  ~1435-1525 s cada uno) <https://archive.org/details/ep-03-cm> — lista
  completa: `EP01CM.mp4` … `EP12CM.mp4`. Usados: EP01 (opening + no-ending),
  EP02 (ending, Power), EP07 (Aki y Himeno). ✅
- Dailymotion, tráiler oficial `x8dsw0h` (92 s) — ✅, visto completo.
- **AnimeThemes sigue caído** (HTTP 522, tal como ya avisaba
  `datos-video.md`; lo reintenté en `api.animethemes.moe` y en la CDN
  `v.animethemes.moe`, ambos fallan con el mismo error de conexión). ⚠️ no
  se pudo usar como fuente alternativa de OP/ED sin comprimir vídeo — se
  resolvió igual bajando los episodios completos de Internet Archive.
- Los enlaces de YouTube que ya cita la biblia (§12: tráiler doblado,
  análisis del opening, clip «Ahuevooooo», etc.) siguen sin poderse abrir
  desde aquí; no los marco como caídos, sólo «sin verificar en este
  servidor», como ya decía la biblia.

### Punto 14 · Poses — de «memoria/contexto» a fotograma real

La biblia (§15) avisaba que las posturas estaban descritas «de memoria o por
el contexto de la frase». Confirmé estas seis con el fotograma real
(quedan como referencia directa, número de fotograma y ruta):

| Personaje | Fotograma | Qué se ve | Sirve para |
|---|---|---|---|
| Denji | `denji_poses/fotograma_00424.jpg` (min. 7:04, película, corte EN) | Ojos cerrados, sonrisa suave, **los dos puños a la altura del pecho**, ligeramente levantados — un «yay» tímido, no un puño triunfal grande | **celebrar** (versión contenida) ✅ |
| Denji | `pareja_llanto/fotograma_00636.jpg` (min. 10:36) | De perfil, boca tapada con la mano, ceño fruncido conteniendo el llanto, mira de reojo | **pensar/emoción contenida** ✅ |
| Makima | `cine3/hoja_01.jpg` fotograma 1 (min. 9:28) | Sentada, girada hacia Denji, mirada tranquila, dice la frase clave | **explicar/recomendar** ✅ |
| Makima | `llanto_1080.jpg` (min. 10:36, 1920×1080 real) | De perfil, una lágrima cayendo, boca entreabierta, pelo rojo oscuro le tapa parte de la cara | **pensar/emoción** ✅ (además corrige el color de pelo, ver punto 4) |
| Power | `power_1080.jpg` (ep. 2, min. 19:20, 1920×1080 real) | Primer plano, boca muy abierta con colmillos afilados, cejas bajas, **pupila con forma de aspa/engranaje rojo y amarillo** (no es un iris normal) | **presentar** (grito de entrada) ✅ — detalle nuevo del diseño del ojo, no estaba en la biblia |
| Aki | `aki_close/fotograma_00434.jpg` (ep. 7, min. 7:14) | De pie, comisura levantada en una sonrisa leve, mirada de lado, traje verde oliva con camisa blanca y corbata negra | **explicar/complicidad** (con Himeno) ✅ — la biblia sólo tenía portadas de manga para Aki, ahora hay un fotograma de anime real |
| Himeno | `aki7/hoja_01.jpg` fotogramas 15-17 (ep. 7, min. 7:06-7:10) | Primer plano de un solo ojo (el otro tapado por el parche), pelo corto verde menta, mirada de lado | referencia nueva de personaje secundario, no pedida por el encargo pero disponible si el redactor la quiere | ⚠️ (una sola fuente, un plano) |

Aki y Himeno comen en un restaurante japonés tradicional (mesas bajas,
tabique de madera, ventanales) — coincide con la escena que la biblia ya
databa en «Ep. 7, 6:22-6:48»; con este corte (audio japonés sin subtítulo
quemado) el rango real de la escena es **6:10-7:18** del episodio 7. ⚠️ no
pude confirmar la frase exacta «vamos al cine de vez en cuando» en este
corte (sin subtítulos); la cito de la biblia con su fuente ya existente.

## Lo mejor para la lámina

- El rótulo real シネマ座 (letras plateadas en relieve, panel verde
  azulado) es el nombre exacto para pintar en la marquesina de Blender.
- Butacas mostaza/ámbar + haz de proyector cálido con halo verde-violeta:
  paleta medida, lista para usar tal cual (no inventar rojo vino).
- El gag «ep. 1 sin animación de ending, sólo créditos de cine» es oro para
  el canal: la propia serie ya piensa en «créditos» y «entradas».
- Pose de Denji celebrando (puños tímidos, ojos cerrados, sonrisa) es más
  fiel que un puño en alto genérico.
- Pupila de Power con forma de aspa roja y amarilla: detalle a no perderse
  si se dibuja su cara de cerca.

## No encontré

- **Qué película real homenajea la «película dentro de la película»** (el
  drama verde-azulado que hace llorar a Denji y Makima). Busqué en inglés
  «Chainsaw Man Reze movie theater scene inspired film reference» y en la
  wiki (`chainsaw-man.fandom.com`, `srsearch=movie theater scene reference`)
  sin resultado directo; puede que Fujimoto no citara una película concreta
  para esa escena en particular (sí lo hizo para el opening, ya listado en
  la biblia). ⚠️ No digo que no exista la referencia, sólo que no la hallé.
- **Qué cine real inspiró シネマ座**: la biblia ya avisaba de esto (§5.1);
  con el nombre exacto ahora en mano (シネマ座) intenté `srsearch=シネマ座`
  en la wiki japonesa y una búsqueda en japonés sin resultados fuera de la
  propia ficción. Sigue sin confirmarse un local real.
- **AnimeThemes** para tener los .webm de OP/ED sin bajar el episodio
  completo: sigue caído (522) en `api.animethemes.moe` y en la CDN
  `v.animethemes.moe`. Se resolvió por Internet Archive, así que no bloqueó
  el trabajo.
- Los clips de **TikTok** que cita la biblia §12 («IRIS OUT», «bang bang»)
  siguen sin poder verse desde aquí (TikTok no es de los sitios que lee
  yt-dlp sin bloqueo en este contenedor); confirmo el mismo bloqueo que ya
  avisaba la biblia, no es un punto obligatorio nuevo.

## Bitácora de búsqueda (esta parte)

- `api.animethemes.moe` y `v.animethemes.moe`: HTTP 522 / túnel cerrado por
  el proxy — descartado, se avisa arriba y en `datos-video.md`.
- yt-dlp sobre `archive.org/details/rezearc`: extrae título y duración sin
  problema (100:08 min); formatos disponibles 854×480 (mp4) y 1920×1080
  (mkv, 5.28 GB).
- yt-dlp `--flat-playlist` sobre `archive.org/details/ep-03-cm`: lista los
  12 episodios sueltos (`EP01CM.mp4` … `EP12CM.mp4`).
- yt-dlp sobre `archive.org/details/ep-03-cm/EP07CM.mp4`: episodio 7 completo,
  1435 s.
- Dailymotion `x8dsw0h`: tráiler de 92 s, bajado y mirado completo.
- `fotogramas.py` usado 9 veces (cine 2 tramos + sueltos, op1/op2, ed1,
  ed2, aki7, trailer_dm, power_poses/makima_dia sueltos) sobre estas
  fuentes; `estilo.py` usado 5 veces para medir hex reales.
- Búsqueda web (2 de 50 usadas): «Chainsaw Man episode 1 Kick Back opening
  timestamp minute appears» (en inglés) y «Chainsaw Man episode 1 no ending
  animation just credits black screen Vaundy» (en inglés) — ambas para
  confirmar con una segunda fuente lo que ya había visto en el vídeo.
- Búsquedas en la wiki de Fandom (`action=query&list=search&srwhat=text`):
  `movie theater scene reference` y `シネマ座`, sin resultado (ver «No
  encontré»).
- Vídeos borrados tras sacar las hojas (regla del disco compartido):
  `cine/video.mp4` (480p, ~607 MB), `op1/video.mp4` (~229 MB),
  `ed2/video.mp4` (~207 MB), `aki7/video.mp4` (~137 MB),
  `trailer_dm/video.mp4`. Sólo quedan las hojas y los fotogramas sueltos en
  `/tmp/claude-0/trabajo/11-chainsaw-man-video/` (4.9 MB en total).
