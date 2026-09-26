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
