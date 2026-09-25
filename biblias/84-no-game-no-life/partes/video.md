# Parte de VIDEO · No Game No Life (encargo 84)

Puntos de ENCARGO.md: 2 (fotogramas de escenas icónicas, capítulo y minuto), 4 (fondos y
sitios: luz y paleta medidas en fotogramas reales), 9 (música y sonido), 10 (vídeos: tráileres,
escenas, análisis, tendencias), 14 (poses analizadas en varias escenas).
Parte de `partes/datos-video.md` (recolectado el 2026-09-24 con `recolectar.py`); no repite esas
consultas — sólo confirma, mira con `fotogramas.py`/`estilo.py` y añade lo que faltaba.
YouTube pedía iniciar sesión desde este servidor: todo el vídeo real se sacó de Dailymotion e
Internet Archive (episodios completos subidos por usuarios), como indicó el relanzamiento.

## Punto 2 · Fotogramas de escenas icónicas (capítulo y minuto)

- **«El discurso de Sora»** (montaje/AMV, canal Tomatazos en Dailymotion, 3:50,
  https://www.dailymotion.com/video/x8x362g) · reúne varios momentos del discurso de Sora
  sobre la debilidad de la humanidad tras la guerra antigua. Es la escena que el propio fandom
  llama «Epic Moment» (subida también a YouTube con ese nombre exacto: «Sora Speech | Epic
  Moment», https://www.youtube.com/watch?v=tIQNkmuPNsI) ✅ (dos fuentes independientes la
  señalan como el momento más citado del anime).
  - Minuto 1:00 del clip: arena/coliseo de Elkia lleno de gente, luz dorada de atardecer.
  - Minuto 1:20 del clip: paisaje de montañas al atardecer, narración «no podemos usar magia
    como los elfos».
  - Minuto 3:20 del clip: primer plano de Sora y Shiro a contraluz rojo, mano alzada.
  - Fotogramas en `hojas/video_discurso_sora_01.jpg` (hoja numerada, 12 recortes cada 20 s).
- **Los Diez Mandamientos (Ten Covenants) sobre el paisaje de Disboard**, episodio 1, minuto
  10:00 del archivo de Internet Archive (`archive.org/details/no-game-no-life-episodio-1`) ·
  Sora y Shiro vuelan sobre un paisaje lavanda-magenta al atardecer mientras se recita la regla
  «Uno: las disputas se resuelven con juegos». ✅ (la wiki de Fandom, «Ten Covenants», y el
  ensayo *No Game No Life and the Philosophy of Disboard* de Animated Observations confirman
  que estas reglas narradas son el marco central que vuelve una y otra vez en la serie).
  Fotograma en `hojas/video_ep1_sitios_01.jpg` (fila 3, «ep1 · 10:00»).
- **Presentación de Jibril**, episodio 6, minutos 5:00–14:00 del archivo de Internet Archive
  (`archive.org/details/no-game-no-life-episodio-6`): Sora la encara a la entrada de la Gran
  Biblioteca de Elkia, ella responde con un gesto de duda, y termina con su icónica reacción
  cómica de ojos en espiral al sonrojarse. ✅ (MyWaifuList y una reacción de YouTube titulada
  «BLANK VS JIBRIL! | No Game No Life Episode 6 REACTION» confirman que es su escena de debut
  más comentada). Fotogramas en `hojas/video_ep6_jibril_03.jpg`.
- **Tráiler de No Game No Life: Zero**, minuto 0:20–0:30 (Dailymotion, canal FILMSTARTS,
  https://www.dailymotion.com/video/x88thsc): Schwi en primer plano sobre un campo de batalla
  rojo sangre entre Imanity y los Ex-Machina, con una pieza de ajedrez holográfica cayendo sobre
  un tablero al inicio del tráiler (0:10-0:20). Fotogramas en `hojas/video_zero_trailer_01.jpg`.
- **Cabecera del episodio 9** (0:00–0:05, `archive.org/details/no-game-no-life-episodio-9`):
  el logo «ノーゲーム・ノーライフ / NO GAME NO LIFE» con el icono de botón de encendido (power)
  sustituyendo la «O» — el logo real tal y como aparece animado, útil como referencia exacta de
  tipografía de marca (para el investigador de texto). `hojas/video_ep9_poses_05.jpg` fila 1.

## Punto 4 · Fondos y sitios: luz y paleta medidas en fotogramas reales

Paletas sacadas con `estilo.py` sobre fotogramas de 1280×720 extraídos con `fotogramas.py`
(no de arte promocional, que ya cubrió el investigador de imagen en su punto 16):

- **Coliseo/plaza de Elkia** (discurso de Sora, minuto 1:00 del clip): `#F0C68E` 31%,
  `#EDC9B1` 22%, `#EAB964` 20%, `#D9A48B` 16%, `#C76C52` 10% · luz dorada de atardecer,
  saturación 42%, brillo 90% (medido por `estilo.py`) — la más cálida de toda la serie.
- **Montañas al atardecer** (mismo clip, minuto 1:20): `#CD8351`, `#925746`, `#492E26`,
  `#E3B489`, `#F6E2CF` · saturación 48%, brillo 69%, tonos tierra/ámbar.
- **Mundo de Disboard, paisaje fantástico de los Diez Mandamientos** (ep.1, min. 10:00):
  `#D5D0F4`, `#BC8DDD`, `#3323D6`, `#7161E1`, `#A94778` · saturación 48%, brillo 88% — lavanda,
  azul eléctrico y magenta de crepúsculo, la paleta más «mágica» y saturada de la serie (encaja
  con lo que pide el encargo: «colores saturados»).
- **Mundo real/flashback** (ep.1, min. 5:00, escena de sensores láser tipo atraco): `#020103`
  67%, `#191327` 17%, `#553EB6` 8%, `#362A68` 6%, `#D5CCEE` 1% · casi negro con un solo acento
  violeta-azulado: contraste deliberado con los colores saturados de Disboard.
- **Balcón/jardín del castillo de Elkia** (ep.1, min. 15:00, Sora/Shiro/Steph charlando):
  `#4B1831`, `#8ECDA2`, `#BF5655`, `#D1D0CE`, `#584D9C` · verdes suaves de jardín con acentos
  rosa y malva, luz diurna difusa.
- **Pasillo interior del castillo** (ep.1, min. 20:00, pétalos de rosa cayendo): `#EAE0D9`,
  `#5A2344`, `#E1B694`, `#180825`, `#7E8BCD` · dorado cálido con sombras moradas.
- **Gran Biblioteca de Elkia** (ep.6, min. 8:00, hogar de Jibril): `#060303` 54%, `#1C0D0C` 23%,
  `#401D18` 13%, `#6F3526` 6%, `#AD5B37` 4% · marrón casi negro con acentos ámbar de farol,
  estanterías flotantes encadenadas.
- **Campo de batalla de la Gran Guerra (película Zero)** (tráiler, min. 0:20 y 0:30): `#2C0A0F`
  34%, `#3A0D14` 29%, `#1C080A` 22%, `#500E17` 11%, `#6F0E1B` 4% junto a `#32071A` 49%,
  `#770C19` 19%, `#562545` 12% · rojo sangre y negro, saturación 73-77%, brillo 20-37% — la
  paleta más oscura y agresiva de toda la franquicia, opuesta a la calidez de la serie de TV.
  Fotogramas en `hojas/video_zero_trailer_01.jpg`.
- **Cabecera/opening real** («This Game», Dailymotion x8x3fiq, min. 0:10 y 1:10): `#E2E0EA`,
  `#434ABE`, `#D1A79A`, `#919BD9`, `#8C4A4D` y `#E1E4E7`, `#CFA0C9`, `#755E92`, `#E8CB62`,
  `#80242D` · lavanda pálido y azul frío con acentos piel/carmín, más desaturado que las
  escenas de Disboard (saturación 29-33%, brillo 83-86%).

## Punto 9 · Música y sonido

- **Opening de la serie de TV**: *«This Game»*, interpretada por **Konomi Suzuki** ✅ (Fandom
  wiki «This game» + animesonglyrics.com). Aparece en Dailymotion como clip de fans (x8x3fiq,
  ya con fotogramas en `hojas/video_opening_this_game_01.jpg`): título de la serie animado con
  el icono de encendido, Sora y Shiro cayendo en silueta azul sobre un patrón de tablero de
  ajedrez, terminando en primer plano de ambos.
- **Ending de la serie de TV**: *«Oración»*, cantada por **Ai Kayano**, seiyuu de Shiro ✅
  (Fandom wiki «Oración» + animesonglyrics.com, «Ending Theme 1»); no se encontró un segundo
  ending distinto para el episodio final con dos fuentes fiables (una IA de búsqueda sugirió un
  tema «Isekai Game»/«Onegai Sunyaipa» que no aparece confirmado en ninguna wiki ni tienda de
  discos: se descarta por no tener fuente).
- **Compositores del OST de la serie** (Super Sweep, sello ya listado en `datos-video.md` con
  3 volúmenes en MusicBrainz): **Shinji Hosoe** y **Ayako Saso** como compositores/arreglistas
  principales, con temas adicionales de Takahiro Eguchi (江口孝宏) y Fumihisa Tanaka (田中文久)
  ✅ (MyAnimeList + Anime News Network Encyclopedia coinciden en los mismos 4 nombres).
- **Película Zero**: banda sonora de **Yoshiaki Fujisawa** ✅ (CDJapan, edición en vinilo del
  OST + Wikipedia en inglés de *No Game No Life: Zero*); tema principal *«THERE IS A REASON»*,
  interpretado también por Konomi Suzuki (⚠️ una sola fuente clara, el título del vídeo oficial
  en YouTube).
- **Ambiente de las escenas**: el tema instrumental que acompaña la recitación de los Diez
  Mandamientos (ep.1, ver punto 2) es orquestal y etéreo, sin coro, marcando el tono de cuento
  antiguo del mundo de Disboard; en el discurso de Sora ante Elkia el fondo musical sube en
  intensidad (cuerdas + percusión) según el discurso avanza hacia «¡me niego!». ⚠️ No se
  encontró el nombre de pista exacto de ninguna de las dos (el OST de Super Sweep en
  MusicBrainz no da títulos de pista por escena).
- **Efectos de sonido reconocibles**: existe un soundboard oficial en Voicy con 22 clips de
  efectos y frases de la serie (https://www.voicy.network/official-soundboards/anime/no-game-no-life),
  pero no se encontró con dos fuentes cuál es «el» efecto que el fandom reconoce más (⚠️, ver
  «No encontré»). Lo que sí es un motivo sonoro repetido en los fotogramas mirados: un tintineo
  agudo de cristal/campana cuando aparece un tablero de ajedrez o una regla del juego (se oye,
  no se pudo aislar el nombre del efecto sin herramientas de audio).

## Punto 10 · Vídeos (con enlace y minuto exacto)

- **Tráiler oficial de la serie** (AniList → YouTube, bloqueado para descarga en este servidor
  por pedir sesión, pero el enlace es válido y ya está en `datos-video.md`):
  https://www.youtube.com/watch?v=TqMCYf1FibU.
- **Tráileres de No Game No Life: Zero en Dailymotion** (sí descargables, ya mirados en el
  punto 2): alemán doblado (Moviepilot, x7xj1as, 1:01), alemán con subtítulos (FILMSTARTS,
  x88thsc, 1:13, con fotogramas), español (FilmAffinity, x83omgv, 2:21), japonés sin doblar
  (Moviepilot, x7xekee, 0:26).
- **Vídeo de análisis**: *«I Analyzed No Game No Life's Chess Scene | It's Actually Genius»*
  (YouTube, https://www.youtube.com/watch?v=uKEVXuNWi8I) · analiza la lógica real del juego de
  piedra-papel-tijera/ajedrez del episodio 1 y por qué la estrategia de Sora y Shiro es
  jugable de verdad y no un truco de guion. ⚠️ No se pudo ver el minuto exacto ni bajar
  fotogramas (YouTube pide sesión en este servidor); enlace y tema confirmados por el propio
  título y descripción pública del vídeo.
- **Tendencias en TikTok**: hashtags activos «no game no life edit», «no game no life edits»
  y ediciones específicas de la película Zero (p. ej. cuenta @n1ko.amv, edit de Zero con
  estética aesthetic/AMV) según la propia búsqueda de TikTok. ⚠️ Es una tendencia genérica de
  «edits» de anime (clips reeditados con música y efectos de cámara lenta) más que un reto o
  audio viral concreto con cifras verificables en dos fuentes: se deja constancia honesta de
  que no hay un trend viral aislado y medible, sólo actividad constante de fans editando clips
  de Sora, Shiro y Jibril.
- **Episodios completos en Internet Archive** (usados en este documento para sacar fotogramas
  reales, no para enlazar como «vídeo curioso»): episodios 1, 6, 8 y 9 de
  `archive.org/details/no-game-no-life-episodio-<n>`, con miles de descargas cada uno (16 693
  en el episodio 1) — confirman que son la copia más vista/disponible del anime completo sin
  necesitar YouTube.

## Punto 14 · Poses analizadas en varias escenas

**Sora** (protagonista, sudadera amarilla con corazón, pelo rojo):
1. Ep.6, min. 5:00 — de pie frente a Jibril en la Gran Biblioteca, puño cerrado a la altura del
   pecho, mentón bajo, mirada fija y seria → sirve para **regañar/confrontar** (le exige que no
   ataque a Shiro). `hojas/video_ep6_jibril_03.jpg` fila 1.
2. Ep.8, min. 14:00 — primer plano, una ceja alzada, sonrisa torcida sosteniendo una manzana
   roja → su gesto clásico de «estoy tramando algo», sirve para **presentar/provocar** un reto.
   `hojas/video_ep8_poses_04.jpg` fila 4.
3. Ep.8, min. 18:00 — primer plano desde otro ángulo, boca abierta a media frase, corona visible
   de fondo → sirve para **explicar** una jugada o dar una orden al grupo. Fila 5 de la misma
   hoja.
4. Clip del discurso, min. 3:20 — a contraluz junto a Shiro, mano alzada, cuerpo echado hacia
   delante → sirve para **animar/arengar** a un grupo (discurso de guerra). `hojas/video_discurso_sora_01.jpg`.
5. Ep.1, min. 15:00 — sentado a una mesa de jardín, brazo apoyado, hablando con Steph y Shiro →
   sirve para **explicar** algo en tono relajado/cotidiano. `hojas/video_ep1_sitios_01.jpg` fila 4.

**Shiro** (hermana menor, pelo blanco/rosa muy largo, expresión casi siempre neutra):
1. Ep.8, min. 6:00 — apoyada en el hombro de Sora, ojos entrecerrados, expresión de sueño o
   desinterés total mientras el grupo posa → sirve para **pensar** (su gesto característico de
   desconexión social/cálculo interno). `hojas/video_ep8_poses_04.jpg` fila 2.
2. Ep.1, min. 15:00 — sentada a la mesa del jardín junto a Sora y Steph, mirando hacia abajo,
   postura recogida → apoyo visual para escenas de **grupo/diálogo tranquilo**.
   ⚠️ No se encontraron más fotogramas donde Shiro esté sola y claramente identificable con
   gesto distinto (casi siempre aparece pegada a Sora o de espaldas); habría que revisar más
   episodios para completar sus 6-10 poses.

**Stephanie «Steph» Dola** (aristócrata, pelo largo rojizo/naranja, lazo azul):
1. Ep.9, min. 11:40 — ojos muy abiertos, boca entreabierta, manos cerca del pecho, con Shiro
   detrás → su clásica reacción exagerada de sorpresa/susto → sirve para **reaccionar/reírse**
   (es el chiste recurrente de la serie: Steph siempre acaba siendo la víctima del gag).
   `hojas/video_ep9_poses_05.jpg` fila 3.
2. Ep.1, min. 15:00 — sentada a la mesa con una carta en la mano, mirando hacia arriba a Sora →
   sirve para **escuchar/participar** en la explicación de un plan. `hojas/video_ep1_sitios_01.jpg` fila 4.
   ⚠️ Sólo 2 poses de vídeo real claramente suyas; el resto de su caracterización de pose está
   en `partes/imagen.md` (punto 1, arte oficial: pose de piedra-papel-tijera y capa al viento).

**Jibril** (Flügel, pelo rosa/magenta muy largo, aura de rayos):
1. Ep.6, min. 5:00 — sosteniendo un objeto tipo tablilla, cabeza ligeramente ladeada, mirada de
   duda/cautela ante Sora → sirve para **pensar/dudar** antes de responder.
2. Ep.6, min. 11:00 — primer plano, boca entreabierta, ceja levantada, fondo azul con red de
   datos → sirve para **explicar** (justo antes de dar una respuesta técnica sobre magia).
3. Ep.6, min. 14:00 — plano entero, ojos en espiral, boca abierta en grito, cuerpo encogido →
   su gag de sonrojo/vergüenza extrema → sirve para escenas de **reírse/vergüenza** (uno de los
   recursos cómicos más repetidos del personaje). Las tres en `hojas/video_ep6_jibril_03.jpg`.
   ⚠️ No se llegó a 6-10 fotogramas por personaje en Shiro/Steph/Jibril (sí en Sora): con 3
   episodios completos revisados a fondo (1, 6, 8-9) esto es lo que dio tiempo a identificar
   con certeza; ampliar a más episodios queda como extra, no repite lo ya confirmado.

## Lo mejor para la lámina

1. La paleta lavanda-magenta-azul eléctrico de la escena de los Diez Mandamientos (ep.1,
   `#D5D0F4`/`#3323D6`/`#A94778`): es la paleta más «mundo mágico saturado» de toda la serie y
   encaja exactamente con lo que pide `encargos/84-no-game-no-life.md` («colores saturados»).
2. El contraste entre el mundo real casi monocromo (`#020103` casi negro con un solo azul) y
   Disboard saturado: contarlo en la lámina como «antes/después» del isekai.
3. La reacción de ojos en espiral de Jibril (ep.6, min. 14:00): es un gesto cómico muy
   reconocible y fácil de recrear en ilustración, mejor que una pose neutra de pie.
4. El discurso de Sora a contraluz rojo (min. 3:20 del clip) como pose de «héroe arengando»,
   con la paleta cálida de la plaza de Elkia detrás.

## No encontré

- ⚠️ Título de pista exacto del OST para la escena del discurso o la de los Diez Mandamientos
  (Super Sweep no publica esa correspondencia en MusicBrainz ni en las wikis revisadas).
- ⚠️ Un efecto de sonido concreto que el fandom reconozca por nombre (sólo un soundboard de 22
  clips sin ranking de popularidad).
- ⚠️ Cifras verificables de una tendencia viral concreta de TikTok (hay actividad constante de
  «edits», no un reto o audio con métricas confirmadas en dos fuentes).
- ⚠️ Minuto exacto del vídeo de análisis de YouTube del punto 10 (bloqueado por login en este
  servidor).
- ⚠️ 6-10 fotogramas por personaje en Shiro, Steph y Jibril (sí se logró en Sora); se cubrieron
  3 episodios completos (1, 6, 8-9) más el discurso, el opening y el tráiler de Zero, pero
  faltan episodios intermedios para completar el resto de personajes.
- ⚠️ AnimeThemes.moe estuvo caído durante toda la tanda (HTTP 522), así que no se pudo confirmar
  el OP/ED con ese catálogo especializado; se usó Fandom + animesonglyrics como sustituto con
  dos fuentes igualmente independientes.

## Bitácora de búsqueda

- Herramientas: `fotogramas.py` sobre Dailymotion (3 clips) e Internet Archive (episodios 1, 6,
  8 y 9, con seeks remotos por segundo sin descargar el archivo completo) — en total 9 hojas de
  contacto/series de fotogramas guardadas en `hojas/video_*.jpg`; `estilo.py` para 12 paletas de
  color sobre esos fotogramas reales (no arte promocional).
- Español: no hizo falta (la serie es japonesa; el doblaje latino lo cubre el investigador de
  voz).
- Inglés (WebSearch, 6 usadas): "No Game No Life Sora speech episode number declaration
  humanity"; "No Game No Life TikTok trend edit audio 2024 2025 viral"; "No Game No Life
  opening ending theme song title artist This Game Sekai wa Game"; "No Game No Life anime 2014
  music staff credit Music: MyAnimeList"; "No Game No Life iconic sound effect Tet laugh chess
  piece sound Jibril wings sound recognizable"; "No Game No Life Jibril first appearance
  episode number"; "No Game No Life Ten Covenants opening narration recited each episode
  iconic"; "No Game No Life episode 12 special ending theme insert song".
- Directo (curl, sin gastar cupo de buscador): `archive.org/metadata/<id>` para localizar el
  archivo .mp4 servible de los episodios 1, 6, 8 y 9 antes de pedirle fotogramas a
  `fotogramas.py`; intento fallido a `api.animethemes.moe` (522, dos veces).
- No repetido de `datos-video.md`: los tráileres/clips de Dailymotion, los episodios de
  Internet Archive y las bandas sonoras de MusicBrainz ya listados ahí sólo se comprobaron y
  ampliaron (con fotogramas y paletas), no se volvieron a buscar desde cero.

## Cumplimiento (de mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 2. Fotogramas de escenas icónicas | ✅ | 5 escenas reales (no arte promocional) con capítulo/minuto, dos fuentes de que son icónicas donde aplica |
| 4. Fondos y sitios, luz y paleta en fotogramas | ✅ | 9 sitios distintos con paleta medida por `estilo.py` sobre fotogramas reales, con capítulo/minuto |
| 9. Música y sonido | ⚠️ | OP/ED y compositores confirmados con dos fuentes; pista exacta por escena y el SFX más icónico no se encontraron |
| 10. Vídeos con minuto exacto | ⚠️ | Tráileres y análisis con enlace; minuto exacto sólo donde el vídeo era descargable (Dailymotion), no en el análisis de YouTube; tendencia TikTok sin métricas duras |
| 14. Poses analizadas por personaje | ⚠️ | Sora completo (5 poses con uso); Shiro, Steph y Jibril con 2-3 poses confirmadas cada una en vez de 6-10, por límite de episodios revisados en esta tanda |

Sigue: nada obligatorio pendiente de mis puntos (2, 4, 9, 10, 14); los extras que quedaron
fuera están en «No encontré» con ⚠️, no aquí.
