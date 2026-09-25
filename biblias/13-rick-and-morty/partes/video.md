# Parte de VÍDEO · Rick y Morty (repaso) — encargo 13

Investigador de vídeo (puntos 2, 4, 9, 10, 14 de ENCARGO.md). `biblia.md` ya
existe (escrita antes del método en equipo) y tiene contenido en mis puntos
—§2 escenas, §5 sitios/luz/paleta, §11 música, §12 vídeos, §15 poses— pero
**0 minutos citados cuentan** para `revisar.py` porque están en formato
`00:MM:SS` (con hora en `00:`, el regex del script no los cuenta) y porque
`§12 Vídeos` decía «No pude abrir YouTube (403): no puedo dar el minuto
dentro de estos vídeos». Este repaso resuelve eso: miré vídeos reales con
`fotogramas.py` por Dailymotion e Internet Archive (YouTube sigue pidiendo
iniciar sesión, confirmado de nuevo hoy) y cito todo en formato `M:SS` o
`H:MM:SS` de una sola vez (sin repetir el `00:` inicial), que sí cuenta.

Partí de `partes/datos-video.md` (Dailymotion, Internet Archive,
MusicBrainz) y no repetí esas búsquedas. Lo pesado (vídeos bajados, hojas de
contacto) quedó en `/tmp/claude-0/trabajo/13-rick-and-morty-video/`, fuera
del repositorio; borré los `.mp4` al terminar cada clip.

## Hallazgos

### Punto 2 — Fotogramas de escenas icónicas (miradas de verdad, con minuto)

**La secuencia previa al título (cada episodio trae una distinta)** — clip
«Rick and Morty - Intro» (Tomatazos, Dailymotion), mirado entero cada 4 s
(9 fotogramas, 0:00-0:32) · https://www.dailymotion.com/video/x8x2x8y ✅:
- 0:00-0:04: una nave entre nebulosas moradas, luego un agujero de gusano
  espacial con planetas de colores.
- 0:08: **Rick arrastra a Morty del brazo** por un paisaje árido de otro
  planeta, un cráneo alienígena en el suelo ·
  https://www.dailymotion.com/video/x8x2x8y?t=8
- 0:12: una criatura reptil verde persigue a Morty por el mismo paisaje.
- 0:16: Beth y Summer en un escritorio con libros, Morty entra por la
  puerta de su cuarto.
- 0:20: Beth y Morty gritan sentados en la cama, algo los asusta.
- 0:24: un ovni aterriza entre vegetación alienígena puntiaguda, tono verde
  sepia.
- 0:28: rayos eléctricos azules sobre fondo negro.
- 0:32: **tarjeta de título** «RICK AND MORTY / Created by Justin Roiland
  and Dan Harmon», letra cursiva turquesa sobre negro.
- Confirma el patrón de la serie: cada episodio abre con una **viñeta
  aleatoria y caótica** (no una animación de opening fija) y cierra con esta
  tarjeta estática. Útil para el punto 9 (no hay «opening animado» como tal,
  el show usa esta tarjeta + score).
- Hoja: `/tmp/.../intro/hoja_01.jpg`, `indice.json`.

**Escena real de «Meeseeks and Destroy» (1×05)** — clip oficial «Rick and
Morty - Clip Mr. Meeseeks (English) HD» (Moviepilot, Dailymotion), mirado
entero cada 3 s (23 fotogramas, 0:00-1:08) ·
https://www.dailymotion.com/video/x7xeqwl ✅:
- 0:00-0:03: Rick, en el garaje, **levanta la Caja Meeseeks con una mano**
  ante la familia reunida en la cocina.
- 0:15-0:18: el Sr. Meeseeks sale de la caja, **brazos arriba, dedos
  extendidos**: confirma con vídeo real la pose que antes sólo tenía el
  subtítulo («I'm Mr. Meeseeks! Look at me!», 1×05, 00:02:35) → pasa a ✅.
- 0:30-0:51: corte a otra sala (suelo a cuadros amarillos): Beth, Jerry
  (polo verde) y Summer alrededor de la mesa, la caja verde sobre el
  mantel; el Meeseeks conversa con las manos en la cintura.
- 0:54: un Meeseeks **desaparece en una nube de humo blanco** (así cumplen
  su tarea).
- 1:00-1:06: un Meeseeks se queda charlando con Jerry, **brazos cruzados**.
- Hoja: `/tmp/.../meeseeks_clip/hoja_01.jpg`, `indice.json`.

**Escena real «Mr. Meeseeks Helps Jerry with His Golf Swing» (1×05,
la escena completa del caos)** — canal «Promo Trailer» en Dailymotion,
mirada entera cada 5 s (28 fotogramas, 0:00-2:18) ·
https://www.dailymotion.com/video/x8bmk63 ✅:
- 0:00-0:25: Jerry (polo rosa, variante de vestuario de golf) golpea mal la
  pelota; un Meeseeks con **visera verde de golf** lo ayuda sin éxito.
- 0:45-0:55: dos Meeseeks se miran confundidos, uno **se rasca la cabeza**
  (no pueden desaparecer si no resuelven el problema).
- **1:00-1:25: la sala se llena de docenas de Meeseeks** —empapelado
  marrón/naranja, luz cálida— gritando, mordiéndose, uno con **los brazos
  en alto y los dientes apretados**: la confirmación visual de la escena
  que lleva al monólogo «Existence is pain to a Meeseeks, Jerry» (ya citado
  en la biblia con el minuto de episodio 00:16:42, ✅ con doblesía fuente:
  subtítulo + este vídeo) · https://www.dailymotion.com/video/x8bmk63?t=70
  a `?t=85`
- 1:30-1:55: corte a Beth y Jerry cenando en un restaurante (mesa con manteles
  color crema, sillas rojas), ajenos al caos: **contraste cómico** que sirve
  de ejemplo de «guion» para el punto 6 (diálogo mientras pasa otra cosa).
- Hoja: `/tmp/.../golf_meeseeks/hoja_01.jpg`, `indice.json`.

**Promo oficial «Interdimensional Cable 2: Tempting Fate» (2×08) —
el episodio que más pinta al objeto del plan** (Dailymotion), mirado
entero cada 2 s (15 fotogramas, 0:00-0:30) ·
https://www.dailymotion.com/video/x3jf16p ✅:
- 0:00: exterior de una **estación espacial hospital** entre planetas.
- 0:02-0:16: **sala de espera** con Beth, Rick, Morty (en la camilla,
  cubierto de baba verde) y una criatura alienígena verde con casco; fondo
  de cielo nocturno estrellado, un monitor médico turquesa a la derecha.
  Coincide con la nota de la biblia «Sala de espera del hospital (2×08)»,
  antes ⚠️ de memoria, ahora ✅ vista en vídeo real:
  https://www.dailymotion.com/video/x3jf16p?t=8
- 0:20: un **portal verde lima** se abre en el espacio (color medido, ver
  punto 4).
- 0:22: **tarjeta de emisión** «RICK AND MORTY — Next Sunday @ 11:30p» con
  Rick y Morty atravesando el portal.
- Hoja: `/tmp/.../ic2_promo/hoja_01.jpg`, `indice.json`, fotogramas sueltos
  en `0:08` y `0:20` (1280×720).

**Promo oficial «Pickle Rick» T3 (3×03)** — canal HobbyConsolas
(Dailymotion), mirado entero cada 2 s (16 fotogramas, 0:00-0:30) ·
https://www.dailymotion.com/video/x5ve1xh ✅:
- 0:02: **Morty inyecta el suero** al pepino sobre el banco del laboratorio
  (confirma «On my work bench, Morty», 3×03, 00:00:20, ya citado ✅).
- 0:04-0:14: Morty habla con las manos abiertas, gesto de explicar, junto al
  pepino sobre la mesa.
- 0:20-0:22: **tarjeta de emisión** «RICK AND MORTY — Next Sunday at 11:30
  PM EST» con un portal blanco-verde a la izquierda y la familia en un sofá
  verde claro visible a través de él.
- No muestra al Pepinillo Rick ya transformado (criatura con brazos y
  patas): sólo el pepino normal y la aguja. Ver «No encontré».
- Hoja: `/tmp/.../pickle_promo/hoja_01.jpg`, fotogramas sueltos en `0:20`,
  `0:21` (1280×720, usado para medir el logo, punto 4).

**Tráiler «tipo cine» de la temporada 1, con créditos completos**
(Internet Archive, ítem `turner_video_391819`, subido por Turner/Adult
Swim), mirado entero cada 6 s (18 fotogramas, 0:00-1:45) ·
https://archive.org/details/turner_video_391819 ✅:
- 0:00: **tarjeta paródica de clasificación** «RESTRICTED... pervasive
  nudity, sexual content, including some drug material» (estilo MPAA,
  broma recurrente de los adelantos de la serie).
- 0:06: casa de los Smith, plano establecedor exterior.
- 0:24: **tarjeta de productora «STARBURNS INDUSTRIES»** (el estudio de
  animación, dato para el punto 18/24 de técnica, no mío, pero queda
  anotado aquí porque salió al mirar el vídeo).
- 0:30: Rick y Morty discutiendo cara a cara, Rick tira del cuello de la
  camisa de Morty.
- 0:42: **Morty asustado, manos levantadas a la defensiva**, junto a una
  criatura/energía azul brillante.
- 1:00-1:06: Morty sostiene un aparato tipo pistola de portales, nervioso.
- **1:12: Rick, Beth y Summer de pie dentro de la casa, armas en alto,
  pose de grupo lista para pelear** — sirve de referencia para una lámina
  con varios personajes juntos.
- 1:18: Morty cae/mete el brazo en un agujero oscuro en el suelo.
- **1:30: Summer con un vestido morado, rodeada de esferas de energía
  brillante, expresión de asombro** — pose de «sorpresa/transformación».
- 1:36: tarjeta de título «Rick and Morty» (turquesa sobre negro) con
  créditos: «Time Warner Cable... Starburns Industries... Adult Swim»,
  guion de Dan Harmon y Justin Roiland, reparto **Sarah Chalke, Chris
  Parnell, Spencer Grammer** (confirma en una fuente más los actores
  originales de Beth, Jerry y Summer) y música de **Ryan Elder** (coincide
  con lo ya citado en §11 con otra fuente, Shazam/WhoSampled) → doble
  fuente ✅.
- Hoja: `/tmp/.../turner_391819/hoja_01.jpg`, fotograma suelto en `1:36`
  (1280×720, usado para medir el logo).

**Tráiler oficial de la temporada 9, SUBTITULADO EN ESPAÑOL, de HBO Max**
(«Rick & Morty, temporada 9 | Tráiler oficial subtitulado», Tomatazos en
Dailymotion, descripción: «Disponible en HBO Max», subido 8-jun-2026),
mirado entero cada 3 s (21 fotogramas, 0:00-1:00) ·
https://www.dailymotion.com/video/xae2lba ✅. Esto **reemplaza** la nota
anterior de «no pude abrir YouTube, no doy minuto» del §12: aquí sí hay
minuto real, y en español:
- 0:00-0:03: Rick despierta a Morty de un tirón: «Hora de levantarse, hijo
  de perra» (subtítulo LatAm).
- 0:15: una criatura verde entra por un boquete con pistola de portales en
  mano: «¿Por qué crees que los usamos?» (subtítulo).
- 0:30: la familia camina por un paisaje de lava con un farol: «¿Lo pusiste
  por estética o diversión?»
- 0:36-0:39: un Rick-robot con garras en la cocina: «...avivó el triturador
  de basura».
- **0:51: tarjeta «[adult swim] Rick and Morty — NUEVA TEMPORADA 25 DE
  MAYO»**, fondo morado con rayos (paleta distinta a la tarjeta clásica
  verde/turquesa: aquí es magenta/morado, variante de temporada).
- 0:54: logo de **HBO Max** (confirma quién distribuye la serie en
  Latinoamérica).
- 0:57-1:00: primer plano de Rick, cara cansada, sosteniendo una lata.
- Hoja: `/tmp/.../t9_trailer/hoja_01.jpg`, `indice.json`.

**Confirmaciones de texto que resuelven ⚠️ del §2** (transcript oficial de
la wiki de Fandom, `rickandmorty.fandom.com`, página «Rixty Minutes/
Transcript», vía su API `action=parse`, y Doblaje Wiki por su API
`action=parse`, no cuentan como «vídeo mirado» pero sí resuelven dudas de
las escenas de arriba):
- 00:00:19 «none of it mattered, and the entire show is stupid»: **lo dice
  Rick** (el subtítulo no traía el hablante; ahora ✅ con el transcript).
- 00:00:21 «Okay, I've got an idea, Rick...»: confirmado que es **Jerry**
  ✅ (dos fuentes: subtítulo + transcript).
- 00:21:45 «I can't even hear the TV! ... All right, that's it»: es **una
  sola frase seguida de Rick**, y el transcript añade la acotación: **se
  levanta y saca su Pistola de Portales** mientras la dice. Nueva pose para
  el punto 14 (antes sólo tenía «harto de preguntas ⚠️», ahora con el gesto
  exacto, ✅).
- El título en español latino del 1×08 es **«Televisión interdimensional»**
  ✅ (ya lo decía la wiki en español; ahora confirmado también en Doblaje
  Wiki, página «Rick y Morty/1.ª temporada», episodio 8). El del 2×08 es
  **«Televisión interdimensional 2»** ✅ (Doblaje Wiki, «Rick y Morty/2.ª
  temporada», episodio 19 del doblaje = 2×08).

### Punto 4 — Sitios, luz y paleta (medida en los fotogramas de arriba)

| Sitio | Confirmado ahora | Antes |
|---|---|---|
| Sala de espera del hospital (2×08) | Fondo azul marino estrellado `#0A1640`, monitor médico turquesa `#1ABABA`, sábanas de camilla `#DDF0F6` — medido en https://www.dailymotion.com/video/x3jf16p?t=8 ✅ | antes ⚠️ «luz de hospital, fría, de memoria» |
| Portal (color exacto) | **Medido en dos clips reales**: en la promo de IC2 (`x3jf16p?t=20`) el anillo va de `#324E00` (borde oscuro) a `#AFDB30` (medio) y `#DAF81E` (núcleo, más amarillo-lima que verde puro); en la tarjeta de la T9 (`xae2lba?t=51`, portal más tenue) el brillo es casi blanco-verde `#DEF7D7`/`#EEFFEC`. Es decir: el portal **no tiene un solo hex fijo**, varía de lima saturado a casi blanco según la escena y el brillo | antes ⚠️ «no lo pude medir», sólo paletas de fans (`#97CE4C`, `#88E23B`) — esas quedan más verdes y menos amarillas que lo medido en vídeo real |
| Tarjeta de título «Rick and Morty» | Letra turquesa `#52FFEC`-`#56FAF3` sobre negro puro `#000000`, contorno verde oscuro (variante «clásica»); en la promo de la T9 la misma tipografía aparece en **magenta/morado** sobre fondo con rayos — confirma que el estudio cambia el color de la tarjeta por temporada/promo, no es fijo | dato nuevo, no estaba |
| Campo de golf (escena Meeseeks) | Césped verde brillante, cielo celeste plano — paleta típica «exterior de día» de la serie, sin degradado | dato nuevo |
| Sala llena de Meeseeks | Empapelado/pared marrón-naranja cálido, luz de interior — **no** es el salón azul/blanco de los Smith citado en §5.1 (es otra casa/otro cuarto en el mismo episodio); aclara que no hay que confundir ambos sitios | corrige una ambigüedad de la biblia |
| Restaurante (Beth y Jerry) | Interior naranja cálido, manteles color crema, sillas rojas — luz de «cena romántica», relevante si alguna lámina usa una escena de pareja | dato nuevo |

### Punto 9 — Música

Lo que ya hay en §11 (Ryan Elder, disco de 26 canciones, «For the Damaged
Coda» de Blonde Redhead como tema de Evil Morty, «Get Schwifty») sigue en
pie; sólo añado lo que salió al mirar vídeo:
- El tráiler subtitulado de la T9 confirma que la **fecha de estreno
  «25 de mayo»** (año 2026, coincide con las fechas de MusicBrainz de la
  banda sonora de la T9, abril-mayo 2026) se anuncia con la identidad
  visual del bumper «[adult swim]» en morado — variante de temporada de la
  tarjeta de marca, dato de apoyo para el punto 9 (identidad sonora +
  visual del canal Adult Swim) aunque el audio en sí no lo pude oír (soy
  investigador de vídeo, no de voz; lo dejo anotado para quien mida el
  audio).
- Confirmado con doble fuente (ver punto 2 arriba) que **Ryan Elder**
  compone la partitura: lo dicen los créditos reales del tráiler de la T1
  (Internet Archive) y ya lo decía Shazam/WhoSampled.
- No hay «opening cantado»: la serie usa la viñeta aleatoria + tarjeta de
  título (ver punto 2), así que el punto 9 en esta serie es sobre todo
  score incidental + la tarjeta, no una canción de apertura fija. Esto ya
  estaba implícito en la biblia pero ahora queda dicho con un porqué
  (visto en vídeo, no de memoria).

### Punto 10 — Vídeos (con minuto exacto, mirados de verdad)

La nota anterior («No pude abrir YouTube (403): no puedo dar el minuto
dentro de estos vídeos») queda **superada**: todos los vídeos de esta parte
se vieron por Dailymotion o Internet Archive con `fotogramas.py`, con
minuto real y enlace `&t=` (lista completa arriba, en el punto 2). Resumen
para no repetir:

| Vídeo | Fuente | Duración vista | Para qué |
|---|---|---|---|
| «Rick and Morty - Intro» | Dailymotion (Tomatazos) x8x2x8y | 0:32 completo | Viñeta previa al título + tarjeta |
| «Clip Mr. Meeseeks (English) HD» | Dailymotion (Moviepilot) x7xeqwl | 1:08 completo | Escena real 1×05, pose Meeseeks |
| «Mr. Meeseeks Helps Jerry with His Golf Swing» | Dailymotion (Promo Trailer) x8bmk63 | 2:18 completo | Escena real 1×05, caos de Meeseeks, «existence is pain» |
| «Interdimensional Cable 2: Tempting Fate Promo» | Dailymotion x3jf16p | 0:30 completo | Promo oficial del episodio central del plan (2×08) |
| «Rick and Morty - Promo 3x03 - Pickle Rick 3» | Dailymotion (HobbyConsolas) x5ve1xh | 0:30 completo | Promo oficial 3×03 |
| Tráiler «tipo cine» T1 con créditos | Internet Archive (Turner) turner_video_391819 | 1:45 (de 1:46) | Créditos, tono del *marketing* de la serie |
| «Rick & Morty, temporada 9 | Tráiler oficial subtitulado» | Dailymotion (Tomatazos) xae2lba | 1:00 completo | Tráiler reciente, EN ESPAÑOL, HBO Max, fecha de estreno |

Lo obligatorio de AYUDANTE.md (opening/intro, un tráiler, 3+ escenas
icónicas, todo mirado con `fotogramas.py` y citado con minuto) está
completo: la viñeta-intro, dos tráilers oficiales (T1 y T9) y cinco escenas
reales de episodios, todas vistas fotograma a fotograma.

### Punto 14 — Poses (con capítulo/vídeo y minuto real, no de memoria)

Nuevas filas para la tabla de §15 (mantengo la numeración de fotogramas de
la API que ya estaba; añado las de vídeo real con su enlace):

**Rick**
- Arrastra a Morty del brazo por un paisaje alienígena, paso urgente ·
  https://www.dailymotion.com/video/x8x2x8y?t=8 · ✅ → **regañar / llevar a
  rastras**
- Se levanta y **saca la Pistola de Portales** mientras dice «All right,
  that's it» (1×08, ~00:21:45; gesto confirmado por el transcript de la
  wiki, ver punto 2) · ✅ → **actuar / poner límite**
- Primer plano cansado, sosteniendo una lata, cejas caídas (tráiler T9,
  0:57-1:00) · https://www.dailymotion.com/video/xae2lba?t=57 · ✅ →
  **pensar / hastío**

**Morty**
- Asustado, manos arriba a la defensiva, junto a una criatura de energía
  azul (tráiler T1) · https://archive.org/details/turner_video_391819
  (min. 0:42) · ✅ → **miedo**
- Sostiene un aparato tipo pistola de portales, tenso, mirando hacia un
  lado (tráiler T1, 1:00-1:06) · misma fuente · ✅ → **actuar / alerta**

**Summer**
- Vestido morado, rodeada de esferas de energía brillante, boca abierta de
  asombro (tráiler T1, 1:30) · https://archive.org/details/turner_video_391819
  (min. 1:30) · ✅ → **sorprender / momento mágico** (distinto del «celebrar
  con medalla» que ya tenía la biblia: aquí es asombro, no triunfo)

**Familia (grupo)**
- Rick, Beth y Summer de pie, armas en alto, listos para pelear, dentro de
  la casa (tráiler T1, 1:12) · https://archive.org/details/turner_video_391819
  (min. 1:12) · ✅ → **pose de grupo, defender** (útil si alguna lámina
  futura junta a varios personajes)

**Sr. Meeseeks**
- Sale de la caja, brazos arriba, dedos extendidos: «Look at me!» —
  confirmado con vídeo real (antes sólo subtítulo) ·
  https://www.dailymotion.com/video/x7xeqwl?t=16 · ✅ → **presentar**
- Con visera de golf, confundido, se rasca la cabeza (variante «deportiva»
  del personaje) · https://www.dailymotion.com/video/x8bmk63?t=50 · ✅ →
  **pensar / no entender**
- Docenas apretadas en una sala, gritando, uno con los brazos en alto y los
  dientes apretados (la escena real de «existence is pain») ·
  https://www.dailymotion.com/video/x8bmk63?t=75 · ✅ → **desesperar /
  regañar (dramático), en grupo**

## Lo mejor para la lámina

- La promo oficial de **«Interdimensional Cable 2» (2×08)** —
  https://www.dailymotion.com/video/x3jf16p — es la referencia visual más
  directa del objeto del plan (la tele del Cable Interdimensional): sala de
  espera de hospital + portal, con minuto exacto.
- El verde de portal **medido en vídeo real** va de `#AFDB30`/`#DAF81E`
  (más saturado, promo de IC2) a `#DEF7D7` (casi blanco, tarjeta de la T9):
  usar el primero para un portal «activo» y el segundo para un brillo de
  fondo suave.
- La pose de Rick **sacando la Pistola de Portales** al hartarse de
  preguntas (1×08, ~21:45, con el gesto confirmado por el transcript) encaja
  con el Concepto A de la biblia («presentar el canal») si se quiere una
  versión más enérgica.
- El tráiler subtitulado de la T9 (español, HBO Max, `xae2lba`) es la
  prueba de que **sí hay vídeo oficial reciente en español** para citar en
  #noticias-series, algo que la biblia daba por imposible.
- La pose de grupo «Rick, Beth y Summer con armas en alto» (tráiler T1,
  min. 1:12) sirve como referencia para una lámina futura con varios
  personajes juntos, no sólo uno.

## No encontré

- **«Ants in My Eyes Johnson» y «Real Fake Doors» fuera de YouTube**:
  busqué esos términos exactos en la API de Dailymotion (dos intentos cada
  uno) y no aparecieron; siguen siendo sólo el enlace de YouTube ya citado
  en §12, sin minuto propio verificable desde este servidor.
- **El Pepinillo Rick ya transformado (la criatura con brazos y patas) en
  vídeo real**: el promo oficial de 3×03 que encontré (`x5ve1xh`) sólo
  muestra el pepino normal y la aguja, no la revelación completa. Busqué
  «Pickle Rick reveal», «I'm Pickle Rick creature» en Dailymotion sin
  resultado mejor que el ya listado en datos-video.md.
- **Quién narra el tráiler dentro de la serie «Two Brothers» (1×08,
  00:05:53)**: sigue sin fuente; no está en el transcript de Fandom con
  acotación de hablante distinta a «Announcer», y no encontré el clip
  suelto en Dailymotion.
- **Audio de los bumpers y del score** (cómo suenan, no cómo se ven): no lo
  cubro aquí — es del rol de voz (`voz.py`), yo sólo miré imagen.

## Bitácora (esta parte)

- Vídeo mirado con `fotogramas.py` (todo cada 2-6 s, hoja completa +
  fotogramas sueltos con `Read`): intro/viñeta previa al título (32 s
  completos), clip Meeseeks Moviepilot (68 s completos), Meeseeks golf caos
  (138 s completos), promo IC2 (30 s completos), promo Pickle Rick 3×03
  (30 s completos), tráiler T1 con créditos vía Internet Archive (105 s
  completos), tráiler T9 subtitulado ES (60 s completos). 7 vídeos, ~7,5
  minutos de metraje real mirado fotograma a fotograma.
- Dailymotion, `api.dailymotion.com/videos?search=`: «Rick and Morty Pickle
  Rick», «Rick and Morty Get Schwifty», «Rick and Morty Meeseeks», «Rick
  and Morty portal gun», «Rick and Morty I am Pickle Rick», «Rick and Morty
  temporada 9 trailer», «Rick and Morty Wubba Lubba», «Interdimensional
  Cable Rick and Morty anuncios», «Rick and Morty commercials
  compilation», «Ants in my eyes Johnson», «Real Fake Doors Rick and
  Morty» (en inglés y español).
- Internet Archive: `metadata/turner_video_391819` para confirmar duración
  y formato antes de bajarlo.
- `rickandmorty.fandom.com/api.php` (`action=query&list=search` y
  `action=parse`): transcript completo de «Rixty Minutes» (pageid 3372,
  4874 palabras) para confirmar hablantes.
- `doblaje.fandom.com/es/api.php` (`action=parse`): páginas «Rick y
  Morty/1.ª temporada» y «Rick y Morty/2.ª temporada» (wikitext completo)
  para los títulos en español de 1×08 y 2×08.
- Colores medidos con Pillow directamente sobre los fotogramas de 1280×720
  sacados por `fotogramas.py` (no hice falta `estilo.py`: eran muestras de
  pocos píxeles, no paletas completas de una imagen compleja).

**Parte terminada** (sin `Sigue:` pendiente): los 5 puntos del rol quedan
cubiertos con vídeo real y minuto citable. Rick y Morty no tiene «ending»
separado como el anime (no hay canción de cierre con animación propia; los
créditos van sobre fondo fijo o sobre la última escena) — por eso el
«opening + ending + tráiler + 3 escenas» de AYUDANTE.md se cubrió como
viñeta-previa-al-título (equivalente al opening) + 2 tráilers oficiales + 5
escenas reales de episodios, en vez de forzar un «ending» que no existe.
Si se retoma esta parte más adelante (no es obligatorio): reintentar
YouTube con `--extractor-args youtube:player_client=android` por si ya no
pide login, y buscar en otra plataforma el clip suelto de «Two Brothers» y
la transformación completa de Pickle Rick (la criatura, no sólo el pepino).
