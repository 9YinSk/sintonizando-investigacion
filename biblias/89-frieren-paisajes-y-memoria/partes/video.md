# Vídeo — Frieren: paisajes y memoria (89-frieren-paisajes-y-memoria)

Investigador de vídeo. Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Enfoque del
encargo: **fondos, luz y melancolía**.

**Serie hermana**: `33-frieren` ya tiene una biblia completa y muy profunda
(su `biblia.md`, roles fusionados). Leí sus secciones de vídeo (escenas §2,
sitios §5, música §11, vídeos §12, poses §15) con
`seccion.py 33-frieren --rol video` antes de empezar: **no repito** su tabla
de 12 sitios, sus 6 vídeos OP/ED con storyboard, ni sus 48 poses. Esta parte
añade sólo lo NUEVO: sitios y escenas que ella no tocó (sobre todo los
ligados a la memoria — Aureole, el Golden Land), fotogramas con **color
medido de verdad** con `estilo.py` (ella sólo tuvo storyboards, sin bajar
vídeo), y las citas de las entrevistas sobre cómo se diseñan luz y paisaje.

## Hallazgos

### Punto 2 · Escenas (con fotogramas.py, capítulo y minuto)

**Vistas esta sesión** (AYUDANTE.md: opening/ending ya los vio a fondo la
biblia hermana con storyboard; yo doy el tráiler y 5 escenas con fotograma
real y color medido, que ella no tenía):

- **Aureole**, el páramo de almas — T1-04 (mencionado; ficha de la escena
  en manga cap. 7) · [Frieren Wiki, «Aureole»](https://frieren.fandom.com/wiki/Aureole)
  ✅ (ficha + imagen oficial) · niebla dorada altísima en brillo (93%),
  columnas en ruinas, un árbol-templo dorado en lo alto de una colina.
  Es **el destino real del viaje de Frieren**: quiere reencontrarse ahí con
  el alma de Himmel. El paisaje-meta de toda la serie.
- **Flamme visita a sus compañeros muertos en Aureole** — manga cap. 7 /
  mencionado en anime ep. 4 · misma fuente ✅ · Flamme de espaldas ante
  **cuatro siluetas translúcidas verde-doradas** (sólo contorno + sombra
  plana, sin piel ni ropa a color): así pinta la serie a los muertos/el
  recuerdo. Es la referencia visual más clara de «paisaje de memoria» que
  hay en toda la obra.
- **Combate con Qual** — T1-03 (confirmado: ficha de Qual, `anime = Episode 3`)
  · [Dailymotion x8qbrgb](https://www.dailymotion.com/video/x8qbrgb?t=10) ⚠️
  (clip de fans, no oficial, pero contenido real del episodio) · Frieren y
  Fern diminutas al pie de una colina de hierba bajo **cielo totalmente
  cubierto**, con la figura de Qual sentada en la cima. La escena más gris
  y desaturada (saturación 15-23%) que medí en toda esta parte: encaja con
  la «melancolía» que pide el encargo 89, y es un sitio que NO está en la
  tabla de sitios de la biblia hermana (ella cubrió del ep. 3 sólo la sala
  de estudio con Zoltraak, no este exterior).
- **PV2 de la T1 (tráiler), 4 paisajes nuevos** — puente de piedra en bosque
  (0:31), campo de flores rosa-magenta con montañas (0:41), cueva
  subterránea de agua azul con Frieren remando y el bastón brillando (0:47,
  **sitio no listado antes**), campo de flores azules gigantes al atardecer
  dorado (1:27) · [Dailymotion x8mkolb](https://www.dailymotion.com/video/x8mkolb)
  ✅ (mismo tráiler que YouTube itKPyGXrCVA, ya citado por la biblia
  hermana, pero yo bajé el vídeo y medí el color real; ella sólo describió
  por storyboard) · detalle y hex en video.json.
- **El Golden Land** (黄金郷, la ciudad transformada en oro) — arco que
  empieza en el **episodio 37** de la T2 según la ficha del arco
  ([Frieren Wiki, «The Golden Land Arc»](https://frieren.fandom.com/wiki/The_Golden_Land_Arc))
  ⚠️ (una fuente wiki; no encontré fotograma del anime todavía, el arco
  recién empieza donde acaba la T2) · es el mismo «arco de la Tierra
  Dorada» que la biblia hermana apuntó como la T3 (PV corto, oct-2027):
  confirmo que en realidad **ya arrancó dentro de la T2** (cap. 77 del
  manga = ep. 37 del anime), así que su primera imagen puede existir antes
  de la T3 completa. Lo dejo anotado para que el redactor no lo dé por
  «sólo futuro».

**Por qué no repito el opening/ending**: la biblia hermana ya los miró
fotograma a fotograma vía storyboard oficial de TOHO (minuto ±1 s) y los
describió con detalle en su §11.1. Volver a bajarlos habría gastado cupo en
lo mismo; en su lugar usé ese cupo en sitios y escenas que ella no tocó.

### Punto 4 · Sitios, luz y paleta (medida en fotogramas)

Además de los sitios de la escena (arriba, con hex), el **proceso de
diseño** detrás de la luz y el paisaje, de una entrevista que la biblia
hermana no cita:

- **Seiko Yoshioka** (concept artist y directora de color de fondos,
  entrevista de abril-2026,
  [Anitrendz](https://www.anitrendz.com/news/2026/04/12/seiko-yoshioka-frieren-interview))
  ✅ (entrevista directa + confirmado por
  [Sakuga Blog](https://blog.sakugabooru.com/2023/10/05/crafting-a-tangible-aging-world-frieren-beyond-journeys-end-production-notes-01-04/),
  que nombra el mismo reparto de tareas): para el **color-script del OP de
  la T2** usó como referencia «los tonos y la transparencia de la acuarela
  de Abe-san en la portada del tomo 1», buscando «una atmósfera bonita con
  tonos medios que recuerdan a los impresionistas»; del tema del OP sacó
  las palabras clave **«nostalgia, sensación de pérdida, luminosidad y
  calidez»** y las volcó en el color.
- Para **Heiß** (T2), Yoshioka diseñó primero **la colina desde donde Fern
  y Stark miran el pueblo**, calculando la altura para que el atardecer
  iluminara el pueblo con el vapor de las termas y el humo de las
  chimeneas «brillando suavemente»; sólo después construyó el resto del
  pueblo (misma entrevista) ✅.
- Para **Äußerst** (T1) diseñó el equilibrio entre el casco antiguo (con
  sus murallas) y los barrios nuevos de la Asociación de Magia, pensando
  la isla como si hubiera crecido de verdad con el tiempo (misma
  entrevista) ✅.
- El **equipo de pintura de fondos** está liderado por **Sawako Takagi**
  en el estudio **Wyeth** (confirmado en dos fuentes independientes:
  [Sakuga Blog](https://blog.sakugabooru.com/2023/10/05/crafting-a-tangible-aging-world-frieren-beyond-journeys-end-production-notes-01-04/)
  y la ficha de la wiki que ya citó la biblia hermana) ✅.
- **Boceto de producción real** (no lo tenía la biblia hermana): el
  embarcadero nevado de Lake Korridor, dibujado por Yoshioka en grises con
  los personajes marcados en rosa para el encaje de cámara —
  [`Lake Korridor port city draft 2 by Seiko Yoshioka.png`](https://frieren.fandom.com/wiki/File:Lake_Korridor_port_city_draft_2_by_Seiko_Yoshioka.png)
  ✅ (archivo oficial de producción subido a la wiki, abr-2026). Prueba que
  el sitio se compone primero en valores (luz/sombra) y el color llega
  después — útil para el punto 18 del redactor (cómo replicarlo).
- **Técnica del OP de la T2**: la artista de fondos **Manae Yamatogi**
  resolvió el plano donde «Frieren y los demás caminan en el mismo sitio
  mientras el entorno cambia alrededor» (mismo truco de fondo-cinta que un
  paso de comedia clásico, pero aplicado a mostrar el paso del tiempo) —
  citado por Yoshioka en la misma entrevista ✅.
- **Truco de montaje para el tiempo/memoria**: el director Keiichiro Saito
  usa **montajes rápidos** (paisajes que pasan en segundos) para marcar
  que, para una elfa, diez años «no son nada» — el primero es justo tras
  la despedida de Himmel en el ep. 1-2 (Sakuga Blog, con detalle de plano)
  ✅. Es el recurso visual concreto que une paisaje + paso del tiempo +
  memoria, el eje del encargo 89.

### Punto 9 · Música (ligada a paisaje y memoria)

Entrevistas directas al compositor **Evan Call**, no citadas por la biblia
hermana (ella sólo tuvo los títulos de la wiki, sin oír ni leer entrevista,
porque YouTube le bloqueó el audio):

- Sobre el tono general: **«traté de mantener el mismo sentimiento en todo
  el mundo [de la serie]. Una sensación de nostalgia, una sensación de
  melancolía, pero no siempre melancólica. También era alegre, feliz, sólo
  una sensación agradable en general»** —
  [Anitrendz, jul-2025](https://www.anitrendz.com/news/2025/07/10/frieren-interview)
  ✅ (cita directa, entrevista de Anime Expo).
- Sobre los instrumentos: usó **tin whistle/penny whistle** (contratando a
  un intérprete profesional) y **flauta dulce** para diferenciar «una
  sensación antigua» de «una sensación emotiva, alegre, folk»; **shvi** y
  **tagelharpa** como instrumentos de fondo «para dar un color, una
  sensación de mundo antiguo»; y **vielle** (viola medieval) y violín
  solista. «Usé esos instrumentos distintos para dar forma a una paleta de
  color única para la serie» —
  [Epicstream](https://epicstream.com/article/frieren-evan-call-interview-soundtrack)
  ✅ (cita directa; verificada leyendo el artículo entero, no el resumen).
- **«One Last Adventure»** suena quando Himmel y el grupo salen a ver la
  lluvia de meteoros por última vez (misma entrevista, Epicstream) ✅: es
  la pieza exacta de la escena que la biblia hermana marcó como «el
  corazón de la serie» (T1-01, 06:19-06:46 y 11:47-12:59), confirmada por
  el propio compositor como una de sus favoritas.
- Para el opening de la T2 arrancó con **«un instrumento a tempo de arrastrar
  el pincel del hammered dulcimer»** en Zoltraak para dar sensación
  «mágica» — mismo mecanismo (instrumento poco común = textura de mundo)
  que usa para el resto del score ✅.
- Palabra del sonido: Call compone por «menú» (una pieza por sentimiento,
  sin saber en qué escena exacta se usará) salvo los 4 primeros episodios
  y contadas escenas, que llevan **partitura hecha a medida** («film
  score») — dato útil para entender por qué el mismo tema (p. ej. el de
  Himmel) reaparece en escenas de memoria muy distintas: no se escribió
  para una escena, se escribió para un sentimiento que se repite ✅.

### Punto 10 · Vídeos (tráileres, análisis, tendencias)

- **Tráiler de la T2**: empieza con la partitura de Evan Call sobre un
  plano del cielo visto **a través de la pulsera que Stark le regaló a
  Fern** (objeto ya fichado por la biblia hermana en su escena 13); los
  paisajes son «más amplios y detallados, sobre todo los del norte», señal
  de que el mundo se abre según avanza el viaje —
  [Anitrendz](https://www.anitrendz.com/news/2025/11/20/watch-the-trailer-for-frieren-beyond-journeys-end-season-2)
  y [CBR](https://www.cbr.com/frieren-beyond-journeys-end-season-2-trailer-explained/)
  ✅ (dos fuentes).
- **Producción, en profundidad**: «Crafting a Tangible, Aging World» —
  [Sakuga Blog](https://blog.sakugabooru.com/2023/10/05/crafting-a-tangible-aging-world-frieren-beyond-journeys-end-production-notes-01-04/)
  ✅, el análisis de producción más detallado que encontré (equipo, montajes
  de paso del tiempo, reparto de tareas Yoshioka/Takagi). No lo tenía
  ninguna de las dos biblias.
- **Vídeo-ensayos de YouTube** sobre el estilo visual (no vistos entero por
  cupo, pero confirmados como existentes y con tema afín):
  - [«Color Design in Anime: Frieren's Eyes»](https://www.youtube.com/watch?v=4GRMlHGB-AM)
    — jerarquía de color aplicada a un personaje, mismo lenguaje que uso
    para la paleta de los sitios ⚠️ (no lo vi entero).
  - [«The Art Of Frieren»](https://wherecreativityworks.com/the-art-of-frieren/)
    — artículo (no vídeo) que analiza la fogata del ep. 1: «los colores
    brillantes de las flores contrastan con el fondo oscuro del bosque de
    noche, visto desde abajo con las flores en primer plano» — la MISMA
    composición (primer plano vegetal + fondo oscuro) que ya vi en mis dos
    fotogramas del campo de flores del PV2 ✅ (patrón repetido, dos
    fuentes distintas de imagen).
- **Tendencia de TikTok** (búsqueda de hashtags, no cuenta oficial): ediciones
  de **«Frieren aesthetic»** con paletas apagadas (pasteles, azules suaves,
  tonos desaturados), grano de película y viñeteado; recortes en primer
  plano de la cara; «edits de profundidad» de escenas icónicas, sobre todo
  **el momento de Himmel** (su funeral/recuerdo). Un fondo de pantalla
  viral concreto: **«Himmel, 30 años después de su muerte»**, con las
  etiquetas `#frierenbeyondjourneysend` `#animeedit` ⚠️ (una fuente, no
  pude entrar a TikTok directo desde el contenedor — dato de agregador de
  búsqueda, sin enlace a un vídeo concreto que pueda dar por bueno).
- **Reddit r/Frieren**, hilos sobre fondos (vía Arctic Shift, `reddit.com`
  bloqueado directo): «New background» (2401 votos), «Background practice
  ft the gang» (25 votos) — la comunidad hispanohablante y angloparlante
  **comparte activamente fondos/paisajes hechos por fans**, señal de que
  un canal de «fondos de pantalla» encajaría con esta serie ⚠️ (visto por
  título únicamente, no leí el contenido completo por cupo).

### Punto 14 · Poses (con capítulo y minuto, ligadas al paisaje)

La biblia hermana ya analizó 48 poses «funcionales» (presentar, explicar,
celebrar, regañar, pensar, animar) de cerca. Aquí añado el recurso que
**no** cubrió: personajes **integrados en el paisaje**, casi siempre de
cuerpo entero o diminutos en el plano — el lenguaje visual propio de
«paisajes y memoria»:

| Quién | Dónde (minuto) | Pose | Sirve para |
|---|---|---|---|
| Frieren | PV2 T1, [0:47](https://www.dailymotion.com/video/x8mkolb?t=47) | De pie en una barca dentro de una cueva de agua azul, sujeta el bastón cuya piedra brilla; mira al frente, cuerpo entero, plano cenital | **pensar / viajar sola**: la figura pequeña ante un espacio enorme y silencioso |
| Frieren | PV2 T1, [1:27](https://www.dailymotion.com/video/x8mkolb?t=87) | De pie sobre un montículo, bastón en la mano derecha apoyado en el suelo, entre flores azules gigantes desenfocadas en primer plano, cielo dorado | **presentar** a lo grande, con el paisaje como marco — misma familia que la pose de la roca sobre el mar de nubes que ya tiene la biblia hermana, pero con flores en vez de nubes |
| Frieren (niña/joven, de espaldas) | PV2 T1, [0:41](https://www.dailymotion.com/video/x8mkolb?t=41) | Camina sola de espaldas por un campo de flores rosa hacia el horizonte, montañas al fondo, muy pequeña en el encuadre | **pensar / el paso del tiempo**: no se ve la cara, sólo la escala; es la pose que mejor resume «memoria» sin mostrar ninguna emoción facial |
| El grupo de Himmel (4) | PV2 T1, [0:31](https://www.dailymotion.com/video/x8mkolb?t=31) | Caminan en fila por un puente de piedra visto entre dos árboles, de espaldas, luz filtrada entre hojas | **grupo / viaje**: sirve para una lámina de bienvenida en equipo, sin mostrar caras (evita elegir una expresión) |
| Frieren y Fern | Ep. 3 (Qual), [0:10](https://www.dailymotion.com/video/x8qbrgb?t=10) | Dos siluetas muy pequeñas de pie al fondo de una colina de hierba, bajo un cielo gris cerrado, frente a una figura gigante sentada | **escala dramática / lo que asusta o sobrecoge**: útil si una lámina quiere transmitir pequeñez ante algo enorme (un reto, un aviso) sin usar caras de miedo |
| Flamme | Manga cap. 7 / mencionado ep. 4 | De espaldas, quieta, ante cuatro siluetas translúcidas de sus compañeros muertos, brazo de uno de ellos extendido hacia ella | **recordar / despedirse**: la pose «de memoria» por excelencia de la serie — nadie mira a cámara, todo pasa en la espalda y en la distancia entre las figuras |

**Regla que sale de mirar estas seis**: cuando la serie habla de memoria o
del paso del tiempo, **casi nunca enseña la cara** — usa la espalda del
personaje, la escala frente al paisaje, o (en el caso de los muertos) la
transparencia. Es útil para el redactor: una lámina «melancólica» de
Frieren no necesita una expresión triste dibujada, con ponerla pequeña y de
espaldas en un paisaje grande ya se lee igual.

## Lo mejor para la lámina

- **Aureole**: el páramo dorado y brumoso donde se reencuentran las almas —
  el paisaje-símbolo de «memoria» de toda la serie, con su propia ficha en
  la wiki y dos fotogramas con hex medido.
- El recurso de **siluetas translúcidas verde-doradas** para pintar a los
  muertos (Flamme y sus compañeros): un vocabulario visual concreto y
  citable para «recordar a alguien» sin inventarlo.
- La cita de Evan Call: la música busca **«nostalgia, melancolía, pero no
  siempre melancólica»**, con instrumentos poco comunes (tin whistle,
  shvi, tagelharpa, vielle) para dar «una sensación de mundo antiguo» — la
  paleta sonora que acompaña a la paleta visual.
- La cueva subterránea con la barca y el bastón brillando (PV2, 0:47): un
  sitio de luz mágica puntual en la oscuridad que no estaba fichado antes.
- La regla de pose: **personaje pequeño y de espaldas ante el paisaje** =
  memoria/paso del tiempo, sin necesidad de dibujar una cara triste.

## No encontré

- **Fotograma del anime del Golden Land** (la ciudad de oro): el arco
  arranca en el ep. 37 según la ficha del arco, pero no encontré una
  imagen del anime ya emitida que lo muestre (puede que sólo se insinúe al
  final de la T2 o que aún sea manga-only) ⚠️. Busqué: `site:frieren.fandom.com
  golden city episode 37/38`, `Frieren season 2 finale golden city reddit`
  (en inglés) — sin resultado con imagen.
- **Vídeo real (no sólo audio) de un opening o ending** para medir su color
  con estilo.py: probé Dailymotion (`x8zsv38`, borrado: «Not found») y un
  ítem de Internet Archive que resultó ser sólo audio (mp3 con ID3, sin
  pista de vídeo). Ya lo hizo bien la biblia hermana por storyboard, así
  que no insistí más (ahorro de cupo, AYUDANTE.md punto 1).
- **El vídeo de TikTok concreto** del «Himmel, 30 años después» (sólo lo vi
  citado por un agregador de búsqueda, sin poder entrar directo a TikTok
  desde el contenedor) ⚠️.
- **Instrumentación exacta del tema que suena en Aureole**: no encontré una
  entrevista que hable de esa escena en concreto (sólo mencionado, no
  mostrado en el anime todavía) ⚠️.
- Búsquedas hechas (además de las citadas arriba): «Frieren Aureole scene
  anime episode» (en), «葬送のフリーレン 黄金郷 アニメ» (ja, sin resultado
  claro de imagen), «Frieren soundtrack Himmel theme reprise» (en).

## Bitácora

- Fandom API (`frieren.fandom.com/api.php`) — wikitext de `Locations`,
  `Aureole`, `Qual`, `The Golden Land Arc`; búsqueda de texto para
  «Flamme grave», «Aureole», «Titan Fortress Ruins». En español no hace
  falta: la wiki es en inglés.
- Descarga directa de imágenes de `static.wikia.nocookie.net` con cabecera
  `Referer: https://www.fandom.com/` (AYUDANTE.md) — 3 imágenes, medidas
  con `estilo.py`.
- `fotogramas.py` sobre dos vídeos de Dailymotion (`x8mkolb` tráiler,
  `x8qbrgb` fragmento de episodio): 6 fotogramas nuevos, todos mirados con
  Read y medidos con `estilo.py --colores 5`.
- `api.dailymotion.com/videos?search=…` para localizar clips (varios
  intentos: «Sousou no Frieren Anytime Anywhere», «OP1 Yuusha» — sin vídeo
  de vídeo real del OP, sólo el tráiler y el fragmento de episodio
  sirvieron).
- `archive.org/advancedsearch.php` — sin vídeo útil de OP/ED (uno resultó
  ser audio).
- WebSearch (en inglés): «Evan Call Frieren interview music nostalgia
  memory theme», «Frieren background art director interview scenery
  melancholy», «Frieren TikTok trend backgrounds aesthetic edit
  landscapes», «Frieren video essay analysis background art direction»,
  «Frieren season 2 trailer official landscape scenery minute».
- `navegar.py` sobre `epicstream.com` y `gamerant.com` (artículos con JS;
  hacía falta para leer el texto real, no sólo CSS).
- `curl` directo sobre `anitrendz.com` y `blog.sakugabooru.com` (sí
  responden a curl con cabecera de user-agent).
- Arctic Shift (`arctic-shift.photon-reddit.com`) para r/Frieren, búsqueda
  por título «background» y «Denken» — `reddit.com` directo da bloqueo
  («blocked due to a network policy»).
- AnimeThemes (`api.animethemes.moe`) — error 522, igual que le pasó al
  recolector automático; no insistí (regla de dos intentos, AYUDANTE.md).
