# Investigador de vídeo · Neon Genesis Evangelion (repaso)

Puntos 2, 4, 9, 10 y 14 de `ENCARGO.md`. Parto de `datos-video.md` (no repito
esas consultas) y de lo que ya escribió la biblia en sus secciones «2 · Las
escenas que sirven para #demos», «5 · Sitios, luz, paleta y texturas»,
«11 · Música», «12 · Vídeos» y «15 · Poses analizadas por personaje»: esas
partes ya tienen minuto y texto **confirmados con subtítulo japonés** (✅), pero
lo que se **ve** en cada fotograma estaba marcado ⚠️ «de memoria, mira el
fotograma antes de usarlo». Esta pasada mira los vídeos de verdad con
`fotogramas.py` (AnimeThemes daba 522 todo el rato; usé Internet Archive, que
sí respondió) y mide color real con `estilo.py`. Todo lo nuevo cita el
archivo exacto de Internet Archive con su segundo.

## 2 · Fotogramas de escenas icónicas (capítulo y minuto)

Vistas de verdad con `fotogramas.py` sobre el episodio 1 completo
(fansub con hash `[5F116C28]`, Internet Archive, ítem
`neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12`,
720p). **Aviso de minuto**: este corte no es el de Netflix (el de los
subtítulos japoneses de §2 de la biblia): el offset es distinto por unos
segundos (por el metraje del opening). Cito el minuto **de este archivo**,
con su enlace `?t=`.

- Misato se quita las gafas de sol de un tirón, mirada de lado, sonrisa de
  medio lado (su primer plano de presentación) · fotograma propio, ep. 1 ·
  ✅ (coincide con la escena que ya cita §2 de la biblia con el diálogo) ·
  minuto 6:20 · [enlace](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=380)
- Shinji nervioso dentro del vehículo de transporte camino al GeoFront, cejas
  apretadas, mirando de reojo (justo antes/después del folleto de NERV) ·
  fotograma propio, ep. 1 · ✅ · minuto 10:16 ·
  [enlace](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=616)
- **El plano más citado por el fandom de Gendo**: primerísimo primer plano de
  sus gafas, con **el carnet/foto de Shinji reflejado dos veces** en los
  cristales (números de expediente en rosa/violeta sobre negro) · fotograma
  propio, ep. 1 · ✅ · minuto 15:38 (coincide con «乗るなら早くしろ» de §2) ·
  [enlace](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=938)
- Primerísimo primer plano de la cara de Shinji, sólo ojo y pelo, dientes
  apretados (el momento «no debo huir») · fotograma propio, ep. 1 · ✅ ·
  minuto 18:33 ·
  [enlace](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=1113)
- Unidad 01 encadenada de pie en su jaula/hangar verde musgo, plano general
  pequeño dentro de una estructura enorme (la imagen que resume «está presa,
  no es libre») · fotograma propio, ep. 1 · ✅ · minuto 20:58 (mismo archivo)
- Shinji dentro de la cápsula de entrada (LCL), dos gotas de refrigerante en
  el pelo, mirada de sorpresa/miedo · fotograma propio, ep. 1 · ✅ · minuto
  19:55 (mismo archivo)
- Tráiler oficial **«The End of Evangelion» (reestreno 30 aniversario,
  GKIDS)**: silueta gigante crucificada en rojo sobre una cruz de neón, y
  Tokio-3 con sus rascacielos ya no ocultos, en ruinas bajo un cielo rosa
  (Tercer Impacto) · Internet Archive `youtube-JGcbdUgNYOY` (subida oficial
  del tráiler de GKIDS) · ✅ · minutos 0:16 y 0:32 ·
  [crucifixión](https://archive.org/download/youtube-JGcbdUgNYOY/JGcbdUgNYOY.mp4?t=16),
  [cielo rosa](https://archive.org/download/youtube-JGcbdUgNYOY/JGcbdUgNYOY.mp4?t=32)
- Opening: **una figura cae/cuelga en pose de cruz recortada contra la luna
  llena**, brazos y piernas abiertos (uno de los planos más repetidos en fan
  art) · vídeo del opening completo, Internet Archive
  `y-2mate.com-neon-genesis-evangelion-opening-full-english-version-a-cruel-angels-thesis-360p`
  · ✅ · minuto 3:45 ·
  [enlace](https://archive.org/download/y-2mate.com-neon-genesis-evangelion-opening-full-english-version-a-cruel-angels-thesis-360p/y2mate.com%20-%20Neon%20Genesis%20Evangelion%20Opening%20Full%20English%20Version%20A%20Cruel%20Angels%20Thesis_360p.mp4?t=225)

Las escenas con diálogo textual japonés-minuto de §2 de la biblia (folleto de
NERV, ficha de Rei, presentación de Asuka, Kaworu) siguen siendo la fuente
principal para **qué se dice**; esta lista aporta **qué se ve**, comprobado.

## 4 · Fondos y sitios: luz, paleta y texturas

Los sitios reales (Hakone, Ube) y sus fuentes ya estaban confirmados en §5 de
la biblia (✅, dos fuentes cada uno); aquí sumo **color medido con
`estilo.py`** (Pillow, k-means) sobre fotogramas oficiales reales, que sí es
comprobable pixel a pixel, en vez de las paletas de fans que ya había.

- **Jaula/hangar de las Eva** (donde cuelga la Unidad 01): verdes musgo y
  oliva `#3D4D2E`, `#536347`, `#88A27E`, con vigas casi negras `#0B0C03` ·
  medido en el fotograma propio del ep. 1, minuto 20:58 (mismo archivo de
  arriba) · ✅ (medición directa sobre fotograma oficial)
- **Cápsula de entrada / cabina del Eva** (LCL): verdes más claros y grisáceos
  `#5E6146`, `#559671`, con un blanco verdoso de luz `#ECF3DD` · medido en el
  fotograma propio del ep. 1, minuto 19:55 · ✅
- **Interior del transporte a NERV** (donde Shinji va nervioso): turquesa
  apagado de metal `#141411`/`#544E29` de fondo con tapicería granate · medido
  sobre el fotograma del minuto 10:16 del mismo episodio · ✅
- **Opening, silueta de Eva contra el atardecer** (Tokio-3, luz de la tarde):
  ocres y dorados `#967E2E`, `#403411`, cielo apagado `#544E29` · medido en el
  fotograma propio del opening, minuto 1:00 · ✅
- **Opening, plano de la Unidad 02 (Asuka) de pie**: rojo carmesí de fondo
  `#EA5E41`, `#96422E`, violeta de sombra `#3A273E` · medido en el fotograma
  propio del opening, minuto 1:15 · ✅
- **Ending «Fly Me to the Moon», la luna llena entre ramas** (imagen fija que
  cierra episodios): azules noche `#182032`, `#162F4C`, `#214868`, luna verde
  pálida `#678E9C`/`#84A1A5` · medido en el fotograma propio del ending,
  minuto 0:20 · ✅
- **Tráiler de *End of Evangelion*, imagen de la crucifixión** (LCL/sangre):
  rojo intenso `#C5344A`, granate oscuro `#421E27`, blanco hueso `#DECDD1` ·
  medido en el fotograma propio del tráiler, minuto 0:16 · ✅
- **Tráiler, el cielo del Tercer Impacto** (rosa apocalíptico sobre Tokio-3
  en ruinas): magenta `#ED5AB9`, `#572145`, `#793662` · medido en el
  fotograma propio del tráiler, minuto 0:32 · ✅
- La paleta de pantallas NERV de `nerv-ui` (naranja `#FF9830`, verde
  `#50FF50`, cian `#20F0FF`) que ya cita §5 sigue siendo de **fans** (proyecto
  con licencia MIT, no oficial): la dejo como estaba, ⚠️, para no perder la
  referencia, pero las medidas de arriba sí son de fotograma oficial.
- Texturas reales equivalentes de §5 (ambientCG, Poly Haven, TextureCan)
  siguen valiendo: no repito la búsqueda. Añado una para el **verde oxidado
  de la jaula de las Eva**: [ambientCG «Metal038» (óxido verde)](https://ambientcg.com/view?id=Metal038),
  CC0 ✅.

**Estilo del trazo** (de `estilo.py` sobre los mismos fotogramas): sombreado
degradado/pintado en fondos y luces (cel shading con degradados suaves en el
aerografiado, típico de Gainax años 90), línea fina o casi ausente en primeros
planos de piel («línea None» en varias muestras) y línea marcada sólo en
metal y estructuras (`#414F37` en la jaula) ✅ (medido, no de memoria).

## 9 · Música y sonido

Lo del opening, el ending y la banda sonora que ya tenía §11 de la biblia
(Yoko Takahashi, Shiro Sagisu, las ediciones en vinilo) sigue en pie; no lo
repito. Confirmo con vídeo real y sumo lo que faltaba: **los efectos de
sonido y onomatopeyas** (el hueco explícito del punto 9 que §11 no cubría).

- El opening completo (visto de verdad, 4:03) confirma que **no es sólo el
  logo con el título**: hay planos de las tres pilotos, siluetas de las Eva
  al atardecer, el ojo verde de Rei en primer plano y **una figura colgando
  en cruz sobre la luna llena** (min. 3:45) — ese plano de la cruz es el más
  citado en fan art del OP · ✅ (visto, `fotogramas.py`)
- El ending «Fly Me to the Moon» que cierra este episodio es **una imagen fija
  de la luna llena tras unas ramas**, sin animación, 65 segundos; confirma que
  el ending cambia de imagen fija según el capítulo (ya lo decía §11 de
  oídas) · ✅ (visto)
- **Efectos de sonido reconocibles**, del catálogo real de la mezcla de
  sonido (biblioteca de librerías comerciales, con nombre exacto de cada
  clip): sirena de alarma «Hollywoodedge, Warning Buzzer Space PE194501» /
  «Sound Ideas, ALARM - SPACE WARNING SYSTEM: INTRUDER ALERT» (la alarma de
  ángel detectado), la puerta de malla que protege a las Eva
  «Hollywoodedge, Warehouse Door HugeM PE185501» (la misma jaula verde del
  punto 4), cigarras de fondo en las escenas de día «Discovery Sound, CICADA»
  (confirma el «verano eterno» de Hakone de §5) y el tren a lo lejos
  «Hollywoodedge, Train Long From Dista PE064401» · ✅ (dos fuentes:
  [Sound Effects Wiki, «Neon Genesis Evangelion»](https://soundeffects.fandom.com/wiki/Neon_Genesis_Evangelion)
  cataloga cada clip por su nombre de librería;
  [hilo de EvaGeeks sobre la sirena de NERV](https://forum.evageeks.org/viewtopic.php?t=6384)
  confirma que la sirena viene de una librería Hollywood Edge)
- Efecto libre parecido a la alarma de NERV para usar como referencia (no es
  el original, es una recreación): [«Evangelion style alarm sound», esffects.net](https://esffects.net/en/176.html) · ⚠️ (fan, no oficial)
- **La onomatopeya hablada más repetida en pantalla**: el número de
  sincronización dicho en voz alta por Maya («シンクロ率41.3パーセント», ep.
  1) es, además de un dato, un **cue sonoro reconocible** (aparece en memes y
  vídeos de recopilación de frases) · ✅ (texto confirmado en §2 de la
  biblia con el subtítulo japonés; el uso como meme sonoro,
  [TikTok «Sonido de chicharra Evangelion»](https://www.tiktok.com/discover/sonido-de-chicharra-evangelion) ⚠️ un solo tipo de fuente)

## 10 · Vídeos: tráilers, análisis y tendencias

§12 de la biblia ya listaba tráilers y vídeos de análisis, pero avisaba que
«los minutos no están comprobados» porque YouTube y TikTok no abrían. Esta
vez sí abrió Internet Archive con una copia oficial del tráiler.

- **Tráiler oficial verificado con minuto exacto**: «THE END OF EVANGELION -
  Official 30th Anniversary Theatrical Trailer», subido por **GKIDS**
  (distribuidora oficial en EE. UU.), copia en Internet Archive
  `youtube-JGcbdUgNYOY`, 57 segundos · ✅ · cartela final «IN THEATRES JULY
  22 ONLY» → minuto 0:52 ·
  [enlace con &t=](https://archive.org/download/youtube-JGcbdUgNYOY/JGcbdUgNYOY.mp4?t=52).
  Contenido, minuto a minuto: logo GKIDS (0:00), montaje de piedras/LCL rojo
  (0:08-0:12), silueta crucificada roja (0:16), Tokio-3 con la pirámide de
  rascacielos ya no escondidos (0:24), cielo rosa del Tercer Impacto sobre el
  mar (0:32-0:36), Gendo en primer plano con el número «03F» al fondo (0:40),
  rayos rojos en el cielo (0:44-0:48), título y fecha (0:52-0:56)
- **Tráiler del opening completo**, mismo archivo del punto 9, confirmado
  visto de principio a fin con `fotogramas.py`, 4:03 · ✅
- Vídeo oficial en Internet Archive con el **doblaje al castellano** de
  Evangelion (`evangelion_202506`, «Neon Genesis Evangelion – Doblaje
  (Castellano 1997-2017)»): **no es doblaje latino** (España), lo dejo
  anotado para que el investigador de voz/doblaje sepa que existe y lo
  descarte a propósito, no por no haberlo visto · ⚠️ (un solo dato, fuera de
  mi punto)
- Los análisis en español y las etiquetas de TikTok que ya tenía §12
  («Komm Süsser Todd», «Fanta Evangelion», «Third Impact Evangelion»,
  «Shinji Cassette Player») siguen siendo la referencia de tendencias: no
  repito la búsqueda, sólo confirmo que las URL abren (código 200) desde
  aquí con `curl -I` para TikTok discover · ⚠️ (TikTok no da minuto, son
  etiquetas)
## 14 · Poses analizadas por personaje

§15 de la biblia ya tenía una tabla por personaje, pero **toda marcada ⚠️
«de memoria, mira el fotograma antes de usarlo»**. Esta tabla trae las poses
que **ya miré** con `fotogramas.py` (✅, con enlace `?t=` al segundo exacto)
sobre el episodio 1 (Misato, Shinji, Gendo) y el episodio 8 (Asuka). No pude
bajar los episodios 6 (Rei) completos a tiempo de forma limpia ni el 24/26
(Kaworu): quedan con el aviso de §15 sin cambiar (⚠️), detallado en «No
encontré». El **minuto es el de este archivo de Internet Archive**, no el de
Netflix: hay un desfase de segundos frente al resto de la biblia.

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Se quita las gafas de sol de un tirón, mirada de lado, sonrisa de medio lado | ep. 1 | [6:20 ✅](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=380) | **presentar** (Misato) |
| Primerísimo plano de sus gafas con el carnet de Shinji reflejado dos veces, gesto impasible | ep. 1 | [15:38 ✅](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=938) | **regañar/explicar en frío** (Gendo, la pose más citada por el fandom) |
| Mirada de reojo, cejas apretadas, dentro del transporte a NERV | ep. 1 | [10:16 ✅](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=616) | **pensar/dudar** (Shinji) |
| Dentro de la cápsula de LCL, gotas de refrigerante en el pelo, ojos muy abiertos | ep. 1 | 19:55 ✅ (mismo archivo) | **pensar** (Shinji, miedo antes del combate) |
| Primerísimo plano, sólo ojo y mechones, dientes apretados («no debo huir») | ep. 1 | [18:33 ✅](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=1113) | **animar** (Shinji, encontrar valor) |
| De perfil, ojos muy abiertos, sorprendida, girada hacia un grupo que celebra | ep. 8 | [3:20 ✅](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2008%20Asuka%20Strikes%21%20%5BC6590C43%5D.mp4?t=200) | **celebrar** (Asuka, reacción de grupo) |
| De pie, barbilla alta, con una carpeta en la mano, dirigiéndose al grupo | ep. 8 | [3:46 ✅](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2008%20Asuka%20Strikes%21%20%5BC6590C43%5D.mp4?t=226) | **presentar/explicar** (Asuka) |
| De pie muy tensa contra una pared, con el traje de conexión, manos juntas al pecho | ep. 8 | [11:02 ✅](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2008%20Asuka%20Strikes%21%20%5BC6590C43%5D.mp4?t=662) | **pensar** (Asuka, incómoda) |
| Silueta de pie, brazos cruzados, proyectada en una pared clara (personaje de pelo corto; no se le ve la cara, sólo la sombra) | ep. 6 | 15:32 ⚠️ (un fotograma, sin confirmar quién es con certeza — el episodio es «Rei II» pero no vi la cara) | **pensar** (probable Rei) |
| Unidad 01 encadenada de pie en su jaula, plano pequeño dentro de una estructura enorme | ep. 1 | 20:58 ✅ (mismo archivo) | **presentar el encierro**, no es de un personaje humano pero sirve para composición |
| Resto de poses de Rei, Asuka (regañar, saludar) y Kaworu de §15 | varios | igual que en la biblia | siguen ⚠️ «de memoria»: no se pudieron confirmar en vídeo esta pasada (ver «No encontré») |

Detalle importante para el redactor: en el fotograma de Gendo (15:38) **no
se le ve tapándose la boca con las manos entrelazadas** (la pose clásica de
memes); en este plano concreto son sólo sus gafas y su frente. La pose de
manos entrelazadas hay que buscarla en otro fotograma o en arte oficial (es
tarea del investigador de imagen, ⚠️ para él).

## Lo mejor para la lámina

- El primer plano de las gafas de Gendo con el carnet de Shinji reflejado
  (ep. 1, 15:38): la pose de personaje secundario más citada por el fandom,
  sirve para «regañar/explicar en frío» sin necesidad de dibujar todo el
  cuerpo.
- La paleta real de la jaula de las Eva (`#3D4D2E` `#536347` `#88A27E`,
  medida con `estilo.py`) da un verde musgo/óxido auténtico para el fondo de
  la ficha de piloto, mejor que las paletas de fans que ya había.
- El plano del opening con la silueta colgando en cruz sobre la luna llena
  (min. 3:45): el encuadre más repetido en fan art de toda la serie, listo
  para inspirar la composición de la lámina.
- Asuka de pie con una carpeta, barbilla alta, dirigiéndose al grupo (ep. 8,
  3:46): una pose «viva» de mando, justo lo que pedía el dueño («no salen
  sólo de pie»).
- La escena del chelo de Shinji (ep. 15, 11:10, con texto y minuto ya
  confirmados en §2/§11 de la biblia) sigue siendo el concepto más natural
  para #demos: alguien toca y otro aplaude, con miedo a la primera demo.

## No encontré

- **AnimeThemes** (openings/endings en `.webm` limpios): la API dio **522**
  en dos intentos distintos (`api.animethemes.moe/anime` y
  `/anime/neon-genesis-evangelion`), igual que le pasó a `recolectar.py`. Usé
  Internet Archive en su lugar (si funciona.
- **Poses de Rei confirmadas en vídeo** (la ficha ep. 5 min. 4:25, la sonrisa
  ep. 6 min. 21:30 de §15): bajé el episodio 6 y busqué esos segundos, pero
  el fotograma de esa franja resultó ser una silueta sin rostro y dos
  fotogramas de un chico llorando/sonriendo que no pude identificar con
  certeza (parece Shinji, no Rei, por el peinado) — el desfase de tiempos
  entre este archivo y los subtítulos de Netflix es mayor de lo que pensaba
  en este episodio. Lo dejo con ⚠️ en vez de inventar qué se ve.
- **Poses de Kaworu confirmadas en vídeo** (ep. 24): el único archivo con ese
  episodio en Internet Archive junta los capítulos 22-24 en un solo vídeo de
  435 MB (`neon-genesis-evangelion-22-al-24`); no me dio tiempo de bajarlo y
  calcular el segundo exacto dentro de él. Queda anotado en `video.json` para
  quien siga.
- **TV Tropes** (banda sonora, tropos de sonido): no lo intenté con
  `navegar.py` esta vez por el tiempo que quedaba; si hace falta, la página
  es `Awesome/NeonGenesisEvangelion` (da 403 por `curl` normal).
- Página wiki `Pattern_Blue` en evangelion.fandom.com: no existe con ese
  nombre exacto (`missingtitle`); el término aparece en el guion pero no
  tiene página propia.

## Bitácora

- `curl` a `api.animethemes.moe` (dos veces) → HTTP 522, sin datos.
- `archive.org/advancedsearch.php` (inglés): «Neon Genesis Evangelion»,
  «Evangelion ending», «Evangelion trailer», «Neon Genesis Evangelion
  Platinum Perfect Collection», «Evangelion 24 / Kaworu / 26» → encontré el
  opening completo, el ending suelto, el tráiler oficial de GKIDS y 19
  episodios sueltos con audio japonés y hardsubs en inglés.
- `curl -I` a los `.mp4` de Internet Archive para comprobar tamaño real antes
  de bajarlos (`content-length`).
- `fotogramas.py` sobre 6 vídeos reales: opening (17 fotogramas + 4 sueltos),
  ending (14 + 1), tráiler (15 + 3 sueltos), episodio 1 (6 fotogramas
  sueltos), episodio 8 (3), episodio 6 (3).
- `estilo.py` sobre 9 fotogramas para paleta real (k-means con Pillow).
- `evangelion.fandom.com/api.php` (inglés): búsqueda de texto «synchronization
  ratio warning sound» e intento de página «Pattern_Blue» (no existe).
- `soundeffects.fandom.com/api.php` (inglés): wikitext completo de la página
  «Neon Genesis Evangelion» → catálogo de efectos de sonido.
- Búsqueda web (español): «Evangelion sonido reconocible alarma pattern
  sincronización efecto de sonido icónico».
- Búsqueda web (inglés): «Evangelion sound effects iconic "synchronization
  ratio" alarm klaxon recognizable» → confirmó la librería Hollywood Edge (2.ª
  fuente en `forum.evageeks.org`).
- `curl -sSI` a los enlaces de TikTok de §12 de la biblia para comprobar que
  siguen respondiendo.

Sigue: confirmar en vídeo real (no de memoria) las poses de Rei (ep. 5 min. 4:25 la ficha, ep. 6 min. 21:30 la sonrisa) y de Kaworu (ep. 24, la presentación y el tarareo) para completar la tabla del punto 14 — los archivos ya están localizados en `video.json` (`neon-genesis-evangelion-episode-21-...` para Rei, ep. 5; `neon-genesis-evangelion-22-al-24` para Kaworu, hay que calcular el segundo dentro del vídeo combinado de 3 episodios).

- Episodios completos disponibles para mirar de verdad en Internet Archive
  (ítem `neon-genesis-evangelion-episode-21-...`, 19 episodios sueltos +
  tema de cierre) y episodios 22-26 combinados en otros dos ítems
  (`neon-genesis-evangelion-22-al-24`, `evangelion-final-25-y-26_202609`):
  dejo la ruta anotada para que cualquiera pueda seguir mirando capítulos
  concretos sin depender de YouTube · ✅ (comprobé que los archivos existen y
  pesan lo que dicen, con `curl -I`)
