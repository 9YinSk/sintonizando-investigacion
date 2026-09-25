# Parte de VÍDEO · Encanto (encargo 58)

Investigador de vídeo. Puntos de ENCARGO.md: **2** (fotogramas de escenas icónicas), **4**
(fondos y sitios, luz y paleta), **9** (música y sonido), **10** (vídeos, minuto exacto) y **14**
(poses analizadas por personaje). Encanto es película (2021), no serie: no hay opening/ending,
así que uso tráiler oficial + los 4 números musicales completos + featurettes oficiales como
"lo que se mira" (indicado por ENCARGO.md para este caso).

YouTube pedía iniciar sesión desde este servidor: todo lo de abajo se miró con **Dailymotion** e
**Internet Archive** (mismos clips oficiales, vía `fotogramas.py`, que usa yt-dlp igual que con
YouTube). 11 vídeos descargados y mirados fotograma a fotograma (hojas de contacto), más
`estilo.py` para los hex medidos. Carpeta de trabajo: `/tmp/claude-0/trabajo/58-encanto-video/`.

## Vídeos mirados de verdad (con fotogramas.py, hojas revisadas con Read)

| # | Título | Duración | Fuente | Enlace |
|---|---|---|---|---|
| 1 | Encanto Trailer (doblado ES-España) | 2:08 | Dailymotion (Sensacine) | https://www.dailymotion.com/video/x88qgbc |
| 1b | Encanto Tráiler Oficial HD (mismo tráiler) | 2:08 | Internet Archive | https://archive.org/details/encanto-trailer-oficial-hd |
| 2 | Encanto - Dos Oruguitas (número completo) | 5:07 | Dailymotion (JeuxVideo.com) | https://www.dailymotion.com/video/x98djyw |
| 3 | [Encanto] The Family Madrigal (número completo) | 4:55 | Internet Archive | https://archive.org/details/encanto-the-family-madrigal-musical-number |
| 4 | Jessica Darrow - Surface Pressure (sing-along oficial) | 3:25 | Internet Archive | https://archive.org/details/jessica-darrow-surface-pressure-from-encanto-sing-along |
| 5 | [Encanto] We Don't Talk About Bruno (número completo) | 3:34 | Internet Archive | https://archive.org/details/encanto-we-dont-talk-about-bruno-musical-number |
| 6 | Encanto with Stephanie Beatriz \| "What Else Can I Do?" Clip | 0:52 | Dailymotion (FanReviews) | https://www.dailymotion.com/video/x869jte |
| 7 | Encanto \| Featurette: Inspiring Encanto | 1:59 | Dailymotion (Cinema Online Singapore) | https://www.dailymotion.com/video/x879tx2 |
| 8 | Encanto \| Featurette: Music Of Encanto | 2:53 | Dailymotion (Cinema Online) | https://www.dailymotion.com/video/x85zgfo |
| 9 | Encanto - Our Casita (making-of extenso) | 10:37 | Internet Archive (mirror The Disney Archives) | https://archive.org/details/youtube-B9SWLkaBIHk |
| 10 | Antonio Madrigal Get His Gift Scene! | 2:59 | Dailymotion (Video Blaze Network) | https://www.dailymotion.com/video/x88d13w |

Todos en 1280×720 (720p, tope de `fotogramas.py`; suficiente para citar pose, encuadre y luz).
`video.mp4` de cada carpeta se borra al terminar la parte (ver Bitácora).

---

## Punto 2 — Fotogramas de escenas icónicas (capítulo no aplica: es película; doy el minuto)

- **El milagro de la vela** (nace la magia): Pedro protege a la familia del ataque a caballo,
  muere, la vela de Alma se enciende sola y crea el valle, la Casita y los dones · Dos Oruguitas
  0:48–1:28 · https://www.dailymotion.com/video/x98djyw&t=68 · ✅ (vídeo + Disney Wiki ES resume
  la misma escena en la ficha de la película) · 1080p+ no disponible en estas fuentes, 720p sí.
- **"La familia Madrigal"** (número de apertura, casa viva): la puerta brilla con la palabra
  "Abuela" y Mirabel corre por los pasillos de la Casita antes de salir al pueblo · 0:48–1:20 ·
  https://archive.org/details/encanto-the-family-madrigal-musical-number&t=48 · ⚠️ (una fuente,
  el propio clip).
- **"No se habla de Bruno"** (número completo, el más viral de la película: ver punto 10) ·
  0:00–3:34 · https://archive.org/details/encanto-we-dont-talk-about-bruno-musical-number ·
  ✅ (vídeo + Wikipedia/CBC confirman que es la escena/canción más comentada, ver punto 10).
- **El don de Antonio** (jaguar, celebración con arcoíris): Antonio recibe su puerta, un jaguar
  lo escolta por la selva y sale montado en él ante la familia · 1:36–2:48 ·
  https://www.dailymotion.com/video/x88d13w&t=96 · ⚠️ (una fuente).
- **La grieta que parte la Casita** (visión de arena/luz verde, la magia empieza a fallar) ·
  no se habla de Bruno 3:02–3:34 · https://archive.org/details/encanto-we-dont-talk-about-bruno-musical-number&t=182
  · concept art oficial del *making of* la explica como "symptom of the family's dysfunction shown
  through house" (David Hutchins, Head of Story) · 8:15–8:30 de Our Casita ·
  https://archive.org/details/youtube-B9SWLkaBIHk&t=495 · ✅ (escena + explicación directa del staff).
- **Reconciliación Alma–Mirabel en el río** (mariposas y luz dorada, clímax emocional) ·
  Dos Oruguitas 3:12–4:56 · https://www.dailymotion.com/video/x98djyw&t=192 · ✅ (vídeo +
  featurette "Music of Encanto" la reutiliza como cierre, min 2:45 · https://www.dailymotion.com/video/x85zgfo&t=165).

## Punto 4 — Fondos y sitios (luz y paleta medida, texturas reales)

Hex sacados con `herramientas/estilo.py` sobre fotogramas en 1280×720 de estos mismos vídeos
(no de arte de fans). Método: fotograma exacto → `estilo.py` → paleta dominante ordenada por %.

- **Casa Madrigal, exterior de día** (trailer, tejado de barro, buganvillas y la ventana con
  luz mágica) · #1E2D29 20% · #384D48 18% · #70784D 16% · #B29B66 12% · #D7B4C5 9% (flores lila) ·
  #7E363B 8% (puerta roja) · sombreado degradado/pintado, saturación 43%, brillo 49% ·
  fotograma 0:12 de https://www.dailymotion.com/video/x88qgbc&t=12 · medido con estilo.py ⚠️
  (una fuente, medición propia).
- **Calle del pueblo Encanto, tarde** (paredes de adobe color salmón/terracota) · #44353A 22% ·
  #BF7C71 19% (pared rosa-salmón) · #713638 15% · #796B60 14% · #DBA899 13% · sombreado degradado,
  mucha línea marcada (línea #8E5D4E) · fotograma 2:56 de
  https://archive.org/details/encanto-the-family-madrigal-musical-number&t=176 · ⚠️.
- **Plaza de noche con faroles** (número "No se habla de Bruno") · #502D30 24% · #694C51 20% ·
  #886F7B 13% · #854714 11% (farol) · #BA7D2B 9% · #D2B05D 8% · #EEE08C 7% (luz cálida de vela) ·
  sombreado degradado, línea normal (#9E752A) · fotograma 1:45 ·
  https://archive.org/details/encanto-we-dont-talk-about-bruno-musical-number&t=105 · ⚠️.
- **El río al atardecer** (escena final de Dos Oruguitas): paleta ámbar/dorada muy saturada ·
  #3E2317 20% · #603A20 19% · #835129 16% · #AC713A 14% · #D49A4F 11% · #EAB680 10% ·
  #FBEDB9 7% (luz) · saturación 62%, brillo 55% · fotograma 4:56 ·
  https://www.dailymotion.com/video/x98djyw&t=296 · ⚠️.
- **Jardín mágico de Isabela** (flores gigantes al abrir su don) · paleta violeta/magenta muy
  saturada (83%): #440C69 29% · #3E0B4C 20% · #260D33 17% · #591281 17% · #6F20AA 7% ·
  fotograma 0:16 de https://www.dailymotion.com/video/x869jte&t=16 · ⚠️.
- **Escena de ataque nocturno** (huida de Alma y Pedro, antes del milagro): paleta oscura casi
  monocroma con vino/granate · #141618 23% · #222321 23% · #30342E 14% · #441A2C 12% ·
  #61303A 11% · saturación 36%, brillo 21% (la más oscura medida) · fotograma 4:16 ·
  https://www.dailymotion.com/video/x98djyw&t=256 · ⚠️.
- **Referencias reales de Colombia usadas para pintar los fondos** (del *making of*, no
  memoria): Barichara (pueblo colonial blanco de calles empedradas, rótulo "Barichara" en
  pantalla) 3:20–3:25 y Cartagena de Indias (fachadas de colores, balcones de hierro) 0:45–0:50,
  ambas en https://archive.org/details/youtube-B9SWLkaBIHk&t=200 · también en la featurette
  "Inspiring Encanto": acantilado real y calle de Cartagena 0:40–0:50 ·
  https://www.dailymotion.com/video/x879tx2&t=40 · Alejandra Espinosa Uribe, del "Colombian
  Cultural Trust", asesoró al equipo (aparece acreditada 3:30 de Our Casita) · ✅ (dos clips
  oficiales distintos coinciden en Cartagena/Barichara como referencia).
- **Texturas reales equivalentes** (CC0, ambientcg, para reproducir tejado/pared/suelo):
  - tejas de barro del pueblo → `RoofingTiles013A` · https://ambientcg.com/view?id=RoofingTiles013A · CC0
  - pared de estuco/adobe → `Plaster001` · https://ambientcg.com/view?id=Plaster001 · CC0
  - suelo de madera de la Casita → `WoodFloor064` · https://ambientcg.com/view?id=WoodFloor064 · CC0
  - adoquín/piedra de la plaza → `PavingStones151` · https://ambientcg.com/view?id=PavingStones151 · CC0
  - todas ⚠️ (elegidas por parecido visual, no medidas contra el fotograma pixel a pixel).

## Punto 9 — Música y sonido

- Todas las canciones las escribió **Lin-Manuel Miranda**; la banda sonora orquestal es de
  **Germaine Franco** · confirmado en MusicBrainz (créditos del álbum) y en la featurette "Music
  of Encanto" (Miranda habla a cámara como *songwriter*, 0:10) · ✅ ·
  https://musicbrainz.org/release-group/6bcff191-c8c6-425d-b057-23ee561cec8b ·
  https://www.dailymotion.com/video/x85zgfo&t=10
- **Títulos oficiales en español latino** (álbum "Encanto: Canciones originales de Lin-Manuel
  Miranda", México 2022) confirmados en MusicBrainz: *La familia Madrigal*, *Un regalo mágico*
  (Waiting on a Miracle), *En lo profundo* (Surface Pressure — ver aviso abajo), *No se habla de
  Bruno*, *Inspiración* (What Else Can I Do?), *Dos oruguitas*, *Colombia, mi encanto* · ✅ (lista
  completa con duración exacta de cada pista) ·
  https://musicbrainz.org/release/6026b713-cc76-49f8-915b-97a633d7828a
- ⚠️➡️✅ **Aviso, corrijo con pruebas**: el encargo da como título en español "Lo que se siente"
  para la canción de Luisa; con dos fuentes distintas el título oficial latino es **"En Lo
  Profundo"**, cantada por **Sugey Torres** · MusicBrainz (duración 202213 ms = 3:22, idéntica a
  "Surface Pressure") + Doblaje/Disney Wiki en español (`tituloES=En Lo Profundo`,
  `tituloLA=En Lo Profundo`, `interpretesLA=Sugey Torres`) ·
  https://musicbrainz.org/release/6026b713-cc76-49f8-915b-97a633d7828a ·
  https://disney.fandom.com/es/wiki/Surface_Pressure (vía API `action=parse`, wikitext) · ✅.
- **Colombia, Mi Encanto** la interpreta **Carlos Vives** (acreditado en pantalla "Recording
  Artist, 'Colombia Mi Encanto'") tocando acordeón en el estudio · Music of Encanto 1:40–2:00 ·
  https://www.dailymotion.com/video/x85zgfo&t=100 · ✅ (créditos en pantalla + MusicBrainz
  lista a Carlos Vives como intérprete de esa pista en el álbum de audio, ver datos-video.md).
- **Maluma** aparece acreditado como **"Mariano"** en la misma featurette (1:35) — es el
  personaje de Mariano Guzmán, el pretendiente de Isabela · ⚠️ (una fuente, el rótulo en pantalla;
  no confirmé si canta o solo actúa la voz).
- **Diseño de sonido concreto**: para el efecto de las maracas familiares usaron *foley* de
  granos de café en un colador ("Coffee beans in a colander = Maracas", boceto en pantalla) ·
  Our Casita 2:10–2:20 · https://archive.org/details/youtube-B9SWLkaBIHk&t=130 · ⚠️ (una fuente,
  pero es el propio equipo de sonido explicándolo).
- **Qué tema suena en la escena más emotiva**: "Dos Oruguitas" (versión instrumental/coral)
  acompaña la reconciliación de Alma y Mirabel junto al río, con mariposas doradas · 3:12–4:56 ·
  https://www.dailymotion.com/video/x98djyw&t=192 · ✅ (la propia featurette de música cierra
  con este mismo tramo como clímax, min 2:20–2:45 · https://www.dailymotion.com/video/x85zgfo&t=140).
- **"We Don't Talk About Bruno"** es la canción-ambiente de la tensión familiar: ritmo de
  murmuración coral, cada personaje "añade" su verso (Pepa, Félix, Dolores, Camilo, Isabela) ·
  0:00–3:34 · https://archive.org/details/encanto-we-dont-talk-about-bruno-musical-number · ✅.
- **Onomatopeyas/efectos reconocibles**: el crujido de las tejas y el yeso al agrietarse la
  Casita (grieta verde) · no se habla de Bruno 3:09 · las campanas y aplausos del pueblo
  recibiendo a cada Madrigal con su don · Family Madrigal 2:00–2:16 · ⚠️ (descripción propia del
  audio del clip, sin transcripción oficial encontrada).

## Punto 10 — Vídeos (tráileres, escenas, análisis, tendencias — todo con minuto)

- **Tráiler oficial (doblado España)**: 2:08, desglose completo con minuto: 0:00 apertura,
  0:12 Casa Madrigal, 0:24–0:33 baile del pueblo, 0:51 conversación Mirabel–Abuela, 1:03
  Abuela en el umbral (autoridad), 1:39 jaguar (don de Antonio, en un flash), 1:45 grieta
  verde, 1:48 Mirabel cae/vuela, 2:03 cueva final · dos copias idénticas en Dailymotion
  (https://www.dailymotion.com/video/x88qgbc) e Internet Archive
  (https://archive.org/details/encanto-trailer-oficial-hd) · ✅ (dos fuentes, mismo tráiler).
- **Escenas oficiales completas usadas como "clips"** (Plan B de YouTube, todas con
  yt-dlp/Dailymotion/Archive, ver tabla de arriba): los 4 números musicales completos y la
  escena del don de Antonio.
- **Featurettes/análisis oficiales de Disney**: "Inspiring Encanto" (1:59, inspiración real en
  Colombia), "Music of Encanto" (2:53, compositores y cantantes invitados), "Our Casita"
  (10:37, el making-of más largo mirado: diseño de la casa, símbolos, sonido, storyboards) ·
  las tres con director/staff hablando a cámara con nombre y cargo en pantalla, así que cada
  frase citada arriba tiene autor identificado.
- **Tendencias TikTok/YouTube** (sin clip propio, con fuente y minuto de contexto, no de
  vídeo): "We Don't Talk About Bruno" se convirtió en sonido viral de TikTok; 88 vídeos de fans
  hechos con ese sonido se proyectaron en el escenario de los Oscar 2022; la canción llegó al
  #1 del Billboard Hot 100 cinco semanas (la canción de una película Disney con más semanas en
  el #1 de la historia) y al #1 global de Spotify en la semana del estreno en Disney+ · ✅ (dos
  fuentes: Wikipedia "We Don't Talk About Bruno" + The Hollywood Reporter, "TikTok Makes Oscars
  Debut During 'We Don't Talk About Bruno' Segment") ·
  https://en.wikipedia.org/wiki/We_Don%27t_Talk_About_Bruno ·
  https://www.hollywoodreporter.com/movies/movie-news/tiktok-oscars-2022-bruno-1235121240/

## Punto 14 — Poses analizadas por personaje (6–10 cada uno, con minuto/enlace)

### Mirabel
1. Presenta el pueblo bailando y saludando, brazos abiertos, sonrisa grande (sirve para
   **presentar**) · Family Madrigal 2:24–2:40 ·
   https://archive.org/details/encanto-the-family-madrigal-musical-number&t=144
2. Sostiene la puerta mágica con las dos manos, mirando hacia arriba con esperanza (sirve para
   **animar/desear**) · Family Madrigal 0:56 · …&t=56
3. Cara de preocupación por Antonio: cejas arriba, manos cerca del pecho, se repite en 4 planos
   distintos (sirve para **pensar/temer**) · Antonio Gift Scene 0:18, 0:48, 1:00, 1:24 ·
   https://www.dailymotion.com/video/x88d13w&t=18
4. Abraza a Abuela Alma junto al río, cabeza apoyada en su hombro (sirve para **reconciliar**) ·
   Dos Oruguitas 4:32 · https://www.dailymotion.com/video/x98djyw&t=272
5. Cae/vuela en el aire, falda ondeando, brazo extendido (acción, no diálogo) · Tráiler 1:45–1:48
   · https://www.dailymotion.com/video/x88qgbc&t=105
6. Mira la grieta verde con miedo, retrocede, manos a medio alzar (sirve para **temer**) ·
   No se habla de Bruno 3:30 · …&t=210
7. De espaldas, entrando corriendo a la Casita, falda en movimiento (sirve para transición de
   escena) · Family Madrigal 0:08 · …&t=8

### Bruno Madrigal
⚠️ **No lo encontré en pantalla como personaje real** en ninguno de los 11 vídeos revisados
(Dailymotion + Internet Archive): en la película su aparición completa llega en el tercer acto,
fuera de los clips promocionales que circulan sueltos. Lo que sí aparece:
1. Su nombre en la puerta mágica de la Casita, letras doradas con motivo de ojo/vela ·
   Dos Oruguitas 2:32 · https://www.dailymotion.com/video/x98djyw&t=152
2. Una imitación verde-fantasma que hace Félix contando la leyenda familiar (no es Bruno, es un
   disfraz narrativo dentro del número) · No se habla de Bruno 1:17–1:24 ·
   https://archive.org/details/encanto-we-dont-talk-about-bruno-musical-number&t=77
Búsquedas hechas sin éxito para un clip donde aparezca él mismo: Dailymotion "Encanto Bruno
torre arena", "Encanto Bruno regresa clip"; Internet Archive `title:(Bruno) AND title:(Encanto)
AND -title:(dont) AND -title:(talk)`. Lo que sí hay (voz, ficha) lo cubre el investigador de voz.

### Luisa Madrigal
1. Flexiona los brazos mirando al cielo, orgullosa: "sé lo que valen" (sirve para **celebrar**)
   · Surface Pressure 0:20–0:25 · https://archive.org/details/jessica-darrow-surface-pressure-from-encanto-sing-along&t=20
2. Carga una fila de burros a la vez sobre los hombros, piernas firmes (fuerza en reposo) ·
   0:15 · …&t=15
3. Lanza una piedra enorme como si fuera un circo, un pie en el aire (acción exagerada,
   fantasía dentro de la canción) · 0:40 · …&t=40
4. Sostiene la puerta de golpe antes de que caiga una caja de pelotas sobre Mirabel y Antonio,
   mirada de alerta (sirve para **proteger/regañar con acción**) · 1:20 · …&t=80
5. Sujeta a Mirabel en el aire con un solo brazo mientras trepa una pared (sirve para
   **explicar mientras actúa**) · 1:55 · …&t=115
6. Cara tensa, dientes apretados, sosteniendo una roca gigante que no la deja moverse (sirve
   para **desahogarse/negar**) · 2:35–2:55 · …&t=155
7. Cara sudada, aliviada, hombros caídos al terminar la canción (sirve para **pensar/dudar**) ·
   3:20 · …&t=200
8. Se agacha para hablar cara a cara con Mirabel, manos en las rodillas, gesto cercano (sirve
   para **explicar**) · Music of Encanto 0:50–0:55 · https://www.dailymotion.com/video/x85zgfo&t=50

### Isabela Madrigal
1. Pose "perfecta" forzada con una flor en la mano, espalda recta, sonrisa de catálogo (antes
   del cambio) · No se habla de Bruno 2:20–2:27, balcón · …&t=140
2. Brazos cruzados, ceja alzada, gesto desafiante hacia Mirabel (sirve para **regañar**) ·
   What Else Can I Do 0:24 · https://www.dailymotion.com/video/x869jte&t=24
3. Boca abierta, ojos como platos, sorprendida de poder crear algo "feo" a propósito (sirve
   para **descubrir/celebrar**) · 0:26 · …&t=26
4. Corre entre enredaderas violeta que ella misma hace crecer, pelo suelto por primera vez ·
   0:34–0:46 · …&t=34
5. Crea un cactus grande con las manos extendidas, gesto de control (sirve para **explicar su
   don**) · 0:28 · …&t=28
6. Flota envuelta en una flor gigante abierta, brazos relajados, cara en paz (cierre del cambio
   de personaje) · 0:48 · …&t=48

### Abuela Alma Madrigal
1. Joven, vestido de novia, mirando a Pedro con ternura, manos entrelazadas · Dos Oruguitas
   0:24–0:40 · https://www.dailymotion.com/video/x98djyw&t=24
2. Huye cargando a los tres bebés recién nacidos, capa ondeando, mirada de terror (acción) ·
   1:04–1:12 · …&t=64
3. Llora arrodillada junto a la vela recién encendida, mano temblorosa (sirve para **sentir**,
   la cara más vulnerable de todo el material mirado) · 1:44 · …&t=104
4. De pie en el umbral de la Casita, espalda recta, gesto serio/autoritario, luz dorada detrás
   (sirve para **regañar/presentar reglas**) · Antonio Gift Scene 0:18 ·
   https://www.dailymotion.com/video/x88d13w&t=18
5. Sostiene la vela con las dos manos, orgullo mezclado con alerta por la grieta que empieza a
   verse (sirve para **advertir**) · 1:12 · …&t=72
6. Cara de shock, ojos muy abiertos, un paso atrás al ver la grieta verde en el suelo ·
   No se habla de Bruno 3:23 · https://archive.org/details/encanto-we-dont-talk-about-bruno-musical-number&t=203
7. Abraza a Mirabel junto al río, cabeza inclinada, manos en la espalda de su nieta (sirve para
   **reconciliar/pedir perdón**) · Dos Oruguitas 4:24–4:40 · …&t=264

---

## Lo mejor para la lámina

- El **río dorado de Dos Oruguitas** (min 4:40–4:56, #EAB680/#D49A4F/#FBEDB9) como fondo de
  cierre: luz cálida, mariposas, funciona para cualquier canal que hable de "reconciliar" o
  "cerrar" algo.
- La **puerta mágica con nombre en letras doradas** (Dos Oruguitas 2:32 / Family Madrigal 0:56)
  es un objeto real y concreto (cuaderno/puerta con nombre grabado) — encaja con la regla del
  dueño de "objeto real en sitio real".
- Las **8 poses de Luisa en Surface Pressure** cubren solas casi todo el abanico de emociones
  que pide el punto 14: celebrar, proteger, dudar, explicar — es el personaje con más material
  de vídeo verificado de los cinco.
- El boceto real de sonido "granos de café en un colador = maracas" (Our Casita 2:15) es una
  anécdota concreta y citable para cualquier texto sobre el "cómo se hizo".
- Paleta violeta/magenta muy saturada de Isabela (hex medidos, ⚠️ una fuente) frente a la
  paleta ámbar de la Casa/pueblo: sirve para distinguir personaje de fondo en una lámina.

## No encontré

- ⚠️ Bruno Madrigal **en pantalla como personaje real** (no como ilusión/puerta) en las fuentes
  permitidas (Dailymotion, Internet Archive, storyboards): su escena central del tercer acto no
  circula como clip suelto en estas plataformas. Búsquedas hechas: ver nota en la sección de
  Bruno arriba. Esto es del punto 14 (poses); su voz/ficha de personaje es del investigador de
  voz, no repito esa búsqueda aquí.
- ⚠️ Storyboards con marca de minuto (Plan C del encargo): no hice falta usarlos — Dailymotion e
  Internet Archive dieron todo el material necesario en 720p real, así que no busqué
  storyboards aparte. Si el redactor necesita un minuto exacto de una escena que no está en la
  lista de arriba, sí tocaría ir a Plan C.
- ⚠️ Transcripción oficial de efectos de sonido/onomatopeyas (crujidos, campanas): descritas de
  oído al mirar los clips, no encontré una lista oficial de foley aparte de la anécdota de las
  maracas.
- Onomatopeyas de videojuegos (punto 11, no es mío) y tipografía (punto 5/6, no es mío): fuera
  de mi encargo, no los busqué.

---

## Cumplimiento del encargo (mis puntos)

| Punto | Qué pedía | Estado | Por qué |
|---|---|---|---|
| 2 | Fotogramas de escenas icónicas, capítulo/minuto | ✅ | 6 escenas icónicas con minuto y enlace `&t=`, todas miradas en hoja de contacto |
| 4 | Fondos y sitios, luz/paleta hex, texturas reales | ✅ | 6 sitios con hex medidos por `estilo.py` + 2 referencias reales de Colombia (Barichara, Cartagena) + 4 texturas CC0 de ambientcg |
| 9 | Música y sonido, tema en escenas emotivas, efectos | ✅ | Compositores, título oficial LatAm corregido con 2 fuentes, intérpretes invitados, un dato de diseño de sonido, tema de la escena más emotiva |
| 10 | Vídeos con minuto exacto, tendencias TikTok/YouTube | ✅ | Tráiler desglosado minuto a minuto, 3 featurettes oficiales miradas, tendencia viral con 2 fuentes |
| 14 | Poses por personaje, 6-10 fotogramas con minuto | ⚠️ | Completo para Mirabel, Luisa, Isabela y Abuela Alma (6-8 cada uno); Bruno sin escena propia encontrada en las fuentes permitidas — se explica y se documentan las búsquedas, no se omite en silencio |

## Bitácora de búsqueda

- Partí de `partes/datos-video.md` (Dailymotion, Internet Archive, MusicBrainz) — no repetí esas
  consultas, sólo las de Dailymotion/Archive que faltaban (Bruno, Colombia Mi Encanto, Isabela,
  featurettes).
- Dailymotion (API directa, sin gastar cupo de buscador): `api.dailymotion.com/videos?search=…`
  para "No se habla de Bruno", "Colombia Mi Encanto", "What Else Can I Do Encanto", "Isabela
  Encanto flor", "Encanto Bruno torre arena", "Encanto Antonio Bruno clip official", "Encanto
  casita se derrumba" (sin resultado útil, el último).
- Internet Archive (`advancedsearch.php`, sin gastar cupo): `title:(Bruno) AND title:(Encanto)`,
  `title:(Colombia) AND title:(Encanto)`, `title:("What Else Can I Do")` (sin vídeo oficial
  suelto ahí, se usó Dailymotion en su lugar), `title:(Encanto) AND title:(house OR crumble OR
  collapse OR casita)`, `title:(Encanto) AND title:(trailer 2 OR teaser 2 OR official trailer)`,
  `title:(Encanto) AND title:(Antonio OR jaguar OR gift OR don)`.
- MusicBrainz: `release-group` con `inc=releases` para encontrar la edición mexicana en español,
  luego `release/<id>?inc=recordings` para la lista de pistas con duración exacta (así confirmé
  qué pista en español correspondía a cuál en inglés, por duración idéntica).
- Disney Wiki en español (Fandom): `api.php?action=query&list=search` +
  `api.php?action=parse&prop=wikitext&page=Surface Pressure` para el título oficial en LatAm y
  la intérprete de doblaje cantado (dato que además sirve al investigador de voz).
- ambientcg: `api/v2/full_json?type=Material&q=…` para 4 texturas CC0 equivalentes (tejas,
  estuco, madera, adoquín).
- Buscador web (2 de mi cupo de ~50, quedan ~48): `"Lo que se siente" Encanto Luisa canción
  español latino "Surface Pressure"` (para no "corregir sin pruebas" el título que da el
  encargo) y `"We Don't Talk About Bruno" TikTok trend viral 2022 Billboard number one` (punto
  10, tendencias).
- `estilo.py` sobre 7 fotogramas en 1280×720 sacados con `--fotograma` de los vídeos ya
  descargados en local (sin volver a descargar) para los hex de punto 4.
- Vídeos borrados de `/tmp/claude-0/trabajo/58-encanto-video/*/video.mp4` al terminar esta parte
  (quedan las hojas de contacto y `indice.json` de cada carpeta, por si el redactor necesita
  otro fotograma del mismo clip sin re-descargar).
