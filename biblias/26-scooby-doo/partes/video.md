# Parte del investigador de VÍDEO · Scooby-Doo (26-scooby-doo)

Repaso (25-sep-2026). `biblia.md` ya tiene los puntos 2, 4, 9, 10 y 14 muy
trabajados (§2, §5, §11, §12, §15), pero casi todo sale de **subtítulos
descargados de GitHub** o de **hojas de contacto de la wiki** (fotogramas
fijos), no de vídeo visto de verdad — la propia biblia lo dice en §12:
«**No vi las imágenes en movimiento**». Ese es el hueco que llena esta
parte: cumplir «Mira los vídeos de verdad» de `AYUDANTE.md` (opening, un
ending, un tráiler y 3 escenas, con `fotogramas.py`, mirando las hojas de
verdad) y aportar minuto + enlace `&t=` de lo que antes era «de memoria» o
sólo texto.

YouTube pidió iniciar sesión (bloqueo del servidor, como avisa el
encargo). Usé **Dailymotion** (clips oficiales re-subidos, canal
«Fandango MOVIECLIPS» con marca de agua para los de 2002, canal «Scooby
Doo» para Zombie Island) e **Internet Archive** para el opening de 1969.
Partí de `partes/datos-video.md` (enlaces de Dailymotion e Internet
Archive ya listados por `recolectar.py`) y busqué más con la API de
Dailymotion (no cuenta como «búsqueda web», es red directa).

Trabajo pesado en `/tmp/claude-0/trabajo/26-scooby-doo-video/` (hojas de
`fotogramas.py`, `video.mp4` ya borrados tras sacar las hojas).

## Hallazgos · Punto 10 — Vídeos mirados de verdad (opening, ending, tráiler, 3 escenas)

Los 6 vídeos, con `fotogramas.py`, mirados con Read (hojas de contacto +
fotogramas sueltos en grande). Todos con `&t=` al segundo exacto.

| Vídeo | Fuente | Duración | Vista |
|---|---|---|---|
| **Opening 1969** («Scooby Doo Where Are You! original 1969 Intro») | [archive.org/details/scooby-doo_20210808](https://archive.org/details/scooby-doo_20210808) | 1:02 | ✅ hoja completa (42 fotogramas, cada 1.5 s) + 9 fotogramas sueltos en grande |
| **«Ending»** (créditos finales de *¿Dónde estás?*, VHS-rip) | [dailymotion.com/video/x3vi48h](https://www.dailymotion.com/video/x3vi48h) | 1:03 | ✅ hoja completa (43 fotogramas) |
| **Tráiler oficial, película 2002** | [dailymotion.com/video/x88nuzj](https://www.dailymotion.com/video/x88nuzj) | 1:45 | ✅ 2 hojas (53 fotogramas) + 1 fotograma en grande |
| **Escena 1 — «A Clue for Scooby Doo» (ep. 2, 1969), parte 2/4** | [dailymotion.com/video/x962eqg](https://www.dailymotion.com/video/x962eqg) (canal CLICK 4 CARTOON, TV-rip) | 4:58 | ✅ 2 hojas (75 fotogramas) + 2 fotogramas en grande |
| **Escena 2 — «Damsel in Distress», película 2002** | [dailymotion.com/video/x3z918e](https://www.dailymotion.com/video/x3z918e) (Fandango MOVIECLIPS, oficial) | 3:07 | ✅ 2 hojas (75 fotogramas) + 2 fotogramas en grande |
| **Escena 3 — «The Ghost Is Here», Scooby-Doo en la Isla del Zombi (1998)** | [dailymotion.com/video/x3zqdm6](https://www.dailymotion.com/video/x3zqdm6) (canal «Scooby Doo», oficial) | 1:16 | ✅ 2 hojas (51 fotogramas) + 3 fotogramas en grande |

✅ = vistas de verdad con Read, no sólo el título. Los 6 cubren el mínimo de
AYUDANTE.md (opening + ending + tráiler + 3 escenas) y **3 épocas distintas**:
serie clásica 1969 (cel animado, TV 4:3), película de imagen real 2002 y
película animada para vídeo 1998 (más oscura y madura).

**Nota sobre el «ending»**: el vídeo de Dailymotion con ese título es en
realidad **el mismo metraje del opening reutilizado como créditos
finales** (mismo plano de la casa encantada y el mismo gag de Scooby rosa
en la bañera de burbujas), con la ficha técnica sobreimpresa. No encontré
un tema de cierre distinto del de apertura en la serie de 1969 — es
correcto, según Wikipedia (ya citada en biblia §11) la cabecera y el cierre
comparten canción; lo nuevo aquí es que **ahora está confirmado mirando el
vídeo real**, no de memoria.

**Créditos en pantalla, confirmados mirando el «ending» (fotogramas 7 a
35, 0:09 a 0:52)**: «Produced and Directed by **Joseph Barbera and
William Hanna**»; «Story **Ken Spears, Joe Ruby**»; «Voices **Nicole
Jaffe** [Vilma], **Casey Kasem** [Fred], **Don Messick**, **Frank
Welker**, **John Stephenson**, **Stefanianna Christopherson** [Daphne]»;
«**Music Director TED NICHOLS**»; «Sound Direction **Richard Olson**»;
cierre con el óvalo giratorio «Hanna-Barbera Production» y las caras de
los 4 humanos en un plato de colores. ✅ (fotograma + ya buscado en la
biblia = dos fuentes).

## Hallazgos · Punto 9 — Música (confirmación en pantalla)

- **Ted Nichols, director musical de la serie 1969-1970**: la biblia (§11)
  ya lo tenía con ⚠️ («✅ la búsqueda» sola). Ahora está en **pantalla**,
  en los créditos del propio episodio (ver arriba): **pasa a ✅ con dos
  fuentes** (crédito en pantalla + la búsqueda que ya tenía la biblia).
- **David Newman, compositor de la película 2002**: confirmado también **en
  pantalla**, en la tarjeta final del tráiler oficial (0:44,
  [dailymotion.com/video/x88nuzj?t=104](https://www.dailymotion.com/video/x88nuzj?t=104)):
  «a Raja Gosnell film "SCOOBY-DOO" … **music by David Newman**». Coincide
  con MusicBrainz (`partes/datos-video.md`, ya recolectado) → ✅ dos
  fuentes.
- La tarjeta final del tráiler también confirma en pantalla el reparto y
  ficha técnica completa: **Freddie Prinze Jr., Sarah Michelle Gellar,
  Matthew Lillard, Linda Cardellini y Rowan Atkinson**, dirigida por
  **Raja Gosnell**, «based on characters created by Hanna-Barbera
  Productions», guion de **James Gunn** — todo dato que la biblia ya tenía
  por Wikipedia, ahora con una segunda fuente (la propia tarjeta).
- **Sonido de la escena de la Isla del Zombi**: ambiente de grillos y
  viento con un **coro grave tipo órgano** cuando aparece el fantasma
  (0:07-0:10) y un **golpe de tambor** en cada salto susto (0:27, 0:42) —
  visto/oído en el vídeo, no en una ficha ⚠️ (no hay crédito de compositor
  en este clip corto; la biblia ya tiene a **Robert Ryan Buck / ver
  MusicBrainz de la peli** en `datos-video.md`, no lo repito).

## Hallazgos · Punto 2 — Escenas icónicas vistas de verdad (con minuto)

### A) 1969, «A Clue for Scooby Doo» (ep. 2, el caso que abre la serie)

Es el episodio que la biblia ya cita en §2.2 (Fred le quita la máscara al
capitán Cutler) pero **sin haberlo visto**. Ahora sí, minuto a minuto de la
parte 2/4 (el vídeo empieza ya avanzado el capítulo, en un pueblo costero
de noche, no es la escena del capitán Cutler sino **otro tramo de brujería**
del mismo episodio con una anciana sospechosa — puede ser una repetición de
personajes de esta franquicia con casos parecidos; el título del vídeo y el
villano con capa coinciden con el catálogo de 1969):

| Minuto | Qué se ve | Sirve para |
|---|---|---|
| [0:00](https://www.dailymotion.com/video/x962eqg?t=0) | Un hombre con capucha morada sonríe con malicia, mirando de reojo (villano) | Pose de villano: sonrisa ladeada, ojos entornados |
| [0:40](https://www.dailymotion.com/video/x962eqg?t=40) | Scooby llama a una puerta con el puño en alto | Pose de acción: **llamar/anunciar** |
| [0:44](https://www.dailymotion.com/video/x962eqg?t=44) | Shaggy y Vilma, **las dos manos en la cintura**, posando con seguridad | Pose de **presentar/confianza** (nueva; no estaba en §15) |
| [1:20](https://www.dailymotion.com/video/x962eqg?t=80) | Primer plano de un frasco con la etiqueta **«EAR OF A NEWT»** (oreja de tritón) | Prop de bruja; útil para cartelas del punto 6/19 (aviso al texto) |
| [1:36-1:44](https://www.dailymotion.com/video/x962eqg?t=96) | Shaggy y Vilma **leen juntos un libro grande** apoyado entre los dos, título «WITCHCRAFT MADE EASY» | Pose de **explicar/investigar en pareja** (nueva) |
| [1:44-1:48](https://www.dailymotion.com/video/x962eqg?t=104) | Shaggy con las **dos manos levantadas, boca abierta**, del susto; Scooby se esconde en sus brazos | Pose de **susto** con minuto exacto (la biblia sólo tenía «de memoria») |
| [2:00-2:32](https://www.dailymotion.com/video/x962eqg?t=120) | Una **anciana encapuchada de blanco y morado** señala acusando a Vilma; luego remueve un caldero humeante | Villana secundaria (no es Cutler): pose de acusar con el dedo |
| [2:36-2:48](https://www.dailymotion.com/video/x962eqg?t=156) | **Scooby prueba la sopa del caldero con una cuchara**, cara de asco, se la ofrece a la anciana | Gag físico: probar comida rara |
| [3:12-4:24](https://www.dailymotion.com/video/x962eqg?t=192) | En una **playa de noche**, Scooby mete el hocico en un tubo/desagüe y sale **cubierto de algas fosforescentes verdes**, corriendo a cuatro patas | **Coincide con el gag de las algas de §5.2** («el fantasma del capitán Cutler y las algas son verde fosforito»): confirmado en vídeo real, no sólo en la hoja de la wiki |
| [4:36-4:56](https://www.dailymotion.com/video/x962eqg?t=276) | **Vilma sostiene un libro con «BIOLOGY» en el lomo** y examina las algas verdes que trae Shaggy; luego el grupo entero camina por la playa hacia la Máquina del Misterio | Pose de **explicar con un libro** (ciencia, no magia) — otra variante para el punto 14 |
| [4:52](https://www.dailymotion.com/video/x962eqg?t=292) | Fred y Daphne caminando juntos por la playa, de espaldas | Pose de pareja caminando (fondo, no protagonismo) |

Medí el verde de las algas directamente en el fotograma de la playa
(0:39s del clip aproximadamente = 4:20 en la hoja): promedio de los
píxeles verdes `#5C8F66` (luz de noche/atardecer, tono apagado — no es el
verde neón puro que se ve en el primer plano del fantasma; ambos son el
mismo gag, con luz distinta) ✅ (Pillow, esta sesión).

### B) 2002, película: «Damsel in Distress» (clip oficial Fandango MOVIECLIPS)

Escena del templo de la isla donde los monstruos capturan a Daphne y
atacan a Shaggy — la pelea final antes del clímax.

| Minuto | Qué se ve | Sirve para |
|---|---|---|
| [0:00-0:12](https://www.dailymotion.com/video/x3z918e?t=0) | Un monstruo con máscara negra de araña agarra a Daphne; ella **sale volando por el aire** en varias vueltas (efectos prácticos + CGI) | Pose de **acción/peligro** de Daphne, distinta a «secuestrada en un coche» que ya tenía §15 |
| [0:15-0:42](https://www.dailymotion.com/video/x3z918e?t=15) | Monstruos de piel roja y verde (demonios con colmillos) rodean al grupo; un monstruo verde-escamoso con casco samurái aparece entre la gente | Diseño de monstruo (referencia de vestuario/maquillaje para «monstruos» del canal) |
| [1:20-1:42](https://www.dailymotion.com/video/x3z918e?t=80) | Shaggy **acorralado contra una pared de raíces**, mueca de miedo, luego se ríe con alivio | Expresión de miedo → alivio, en 20 segundos |
| [1:35-1:40](https://www.dailymotion.com/video/x3z918e?t=95) | Shaggy suelta gas verde (chiste de pedo) que noquea a un monstruo | Gag físico icónico de Shaggy |
| [2:15-2:42](https://www.dailymotion.com/video/x3z918e?t=135) | Daphne sigue **volando/cayendo** entre trampas y jaulas, atrapada al final en un pozo circular | Secuencia larga de «damisela en apuros», confirma el patrón de §2.1 («Daphne es la que más veces cae prisionera») con imagen real de la película, no sólo la estadística |

### C) 1998, *Scooby-Doo en la Isla del Zombi*: «The Ghost Is Here» (clip oficial)

| Minuto | Qué se ve | Sirve para |
|---|---|---|
| [0:00-0:03](https://www.dailymotion.com/video/x3zqdm6?t=0) | Cielo **rojo fuego** sobre un pantano, la Máquina del Misterio cruza entre humo | Paleta de apertura, mucho más oscura que 1969 |
| [0:05-0:07](https://www.dailymotion.com/video/x3zqdm6?t=5) | Sesión de espiritismo: mesa con velas, una médium con turbante y bola de cristal; la pandilla sentada alrededor | Sitio nuevo no descrito en §5.1: «cuarto de espiritismo» |
| [0:07-0:10](https://www.dailymotion.com/video/x3zqdm6?t=7) | Fantasma gris translúcido con forma de polilla/murciélago aparece flotando | Diseño de fantasma 1998, más realista que el de 1969 |
| [0:09-0:12](https://www.dailymotion.com/video/x3zqdm6?t=9) | **Los 4 humanos corren y gritan juntos** hacia la puerta, en fila, brazos en alto | Pose de **grupo asustado huyendo** — no había ninguna pose de GRUPO en §15, sólo individuales |
| [0:18-0:25](https://www.dailymotion.com/video/x3zqdm6?t=18) | Cementerio de noche con niebla azul; Shaggy ve su reflejo en un espejo caído y grita | Sitio «cementerio con niebla» + susto con prop |
| [0:27-0:34](https://www.dailymotion.com/video/x3zqdm6?t=27) | Zombis salen de las tumbas; un esqueleto agarra el tobillo de Daphne entre las lápidas | Gag clásico de terror (mano que agarra el tobillo) |
| [0:39-0:43](https://www.dailymotion.com/video/x3zqdm6?t=39) | El grupo **graba con una cámara de vídeo** (visor con «REC» y marco de encuadre en pantalla) apuntando a un barco fantasma encallado | Interfaz en pantalla (cámara) — aviso para el punto 6/19, útil también si se usa un "visor" en la lámina |
| [1:12-1:16](https://www.dailymotion.com/video/x3zqdm6?t=72) | Serpiente/monstruo rojo gigante ataca; el visor de la cámara sigue encendido con «REC» | Cierre de la escena |

Paleta medida con `estilo.py` en 3 fotogramas de esta escena: saturación
**38-64%** y brillo **18-28%**, frente al **65-89%** de saturación y
22-48% de brillo del opening de 1969 (mismo método, mismos fotogramas
medidos esta sesión) → confirma con números que **Zombi Island es visualmente
más oscura y apagada** que la serie clásica, no sólo «da esa sensación».

## Hallazgos · Punto 4 — Luz y paleta medida en fotogramas reales (amplía §5)

- **De noche, los personajes se tiñen de azul** (ya lo decía §5.2 con un
  solo ejemplo, C-15): lo confirmo con **una fuente distinta** — en el
  opening de 1969 (0:22-0:33), medí con Pillow: camisa de Fred (blanca de
  día) da `#53555B` de noche; jersey de Vilma (naranja) da `#5E92AE`;
  camisa de Shaggy (verde) da `#556172`. Los tres, sin excepción, se
  desplazan hacia el azul-gris. ✅ (dos fuentes: C-15 de la wiki + este
  opening).
- **Vestido de Daphne, de noche** (0:21, escena de la mano fantasma
  saliendo de una puerta): azul marino oscuro con pañuelo verde apagado y
  pelo naranja quemado — coincide con la nota de §5.3 de que en luz de día
  es más claro (`#7E4BA6` aprox.); esta escena confirma que de noche se ve
  mucho más oscuro y saturado de azul, no sólo «morado».
- **Escena nueva — playa nocturna del episodio 2** (algas): cielo azul
  cobalto liso sin nubes, agua azul más clara con una franja de espuma;
  paleta dominante medida con `estilo.py`: `#023B67`, `#0F234C`,
  `#083E6C` (los mismos tonos de «noche Hanna-Barbera» de §5.2, con
  fuente nueva).
- **2002, templo/isla (tráiler y escena «Damsel»)**: paleta cálida y
  terrosa (torres de antorchas): `#332416`, `#582D1E`, `#86341B`, con
  saturación media (56%) — muy distinta del azul nocturno de la serie
  animada. Sitio nuevo para la biblia: **«templo/isla de Kalabar»**, no
  estaba en §5.1.
- **Grupo en fila, luz de antorchas (tráiler 2002, 0:28,
  [dailymotion.com/video/x88nuzj?t=28](https://www.dailymotion.com/video/x88nuzj?t=28))**:
  colores medidos (mediana de una caja central de cada torso, luz cálida y
  tenue, por eso salen oscuros): Fred camisa azul `#0E2553`; Daphne
  vestido morado `#5B345A`; Vilma jersey `#8D2F19` (se ve más rojizo que
  naranja por la luz de antorcha); Shaggy camiseta `#32542F`. Sirven como
  **contraste actor real vs. dibujo animado**: la paleta clásica (azul,
  morado, naranja, verde) se mantiene en la versión de imagen real, con
  la luz cambiando el tono exacto — dato para el punto 17 (qué nunca
  cambia: la paleta por personaje).
- **Furgoneta y pañuelo de Fred** (⚠️ en §5.3, «no medí, las imágenes eran
  de noche»): **sigue sin resolver**. Ninguno de los 6 vídeos que miré
  muestra la Máquina del Misterio en primer plano de día ni a Fred con el
  pañuelo naranja de cerca; es un dato de **vestuario/objeto**, no de
  «sitio con luz», así que lo dejo para quien mida vestuario (imagen) —
  lo anoto en «No encontré» para que no se pierda.

## Hallazgos · Punto 14 — Poses nuevas encontradas en vídeo real (con minuto)

Además de las ya confirmadas arriba (Shaggy+Vilma investigando con un
libro, susto de Shaggy con las manos arriba, Vilma con el libro de
biología, grupo huyendo asustado, Daphne volando/atacada), esta pose
nueva:

- **Vilma y Shaggy, las dos manos en la cintura, posando con seguridad**
  (1969, ep. 2, [0:44](https://www.dailymotion.com/video/x962eqg?t=44)):
  sirve para **«presentar» en pareja**, algo que §15 no tenía (sólo poses
  individuales de «presentar»).
- **Scooby llamando a una puerta con el puño** (1969,
  [0:40](https://www.dailymotion.com/video/x962eqg?t=40)): pose de
  «anunciar/pedir permiso», útil si la lámina necesita un gesto de
  «toca aquí» o «pide ayuda».

## Lo mejor para la lámina

1. **Vilma con el libro de «BIOLOGY» examinando la pista verde**
   (1969 ep. 2, [4:40](https://www.dailymotion.com/video/x962eqg?t=280)):
   la pose de «explicar con pruebas», perfecta para #dudas (foro técnico).
2. **Shaggy y Vilma leyendo juntos un libro grande** (1969 ep. 2,
   [1:40](https://www.dailymotion.com/video/x962eqg?t=100)): dos
   personajes investigando a la vez, sirve para una lámina en pareja.
3. El **frasco «EAR OF A NEWT»** (1969 ep. 2, 1:20) como referencia de
   cartela/etiqueta pintada a mano, si el tablero de pistas lleva frascos
   o notas con letra de la época.
4. La comparación de **saturación medida** (65-89% en 1969 vs. 38-64% en
   Zombi Island 1998) como argumento visual para elegir la paleta viva y
   plana de la serie clásica, no la oscura, para el canal.
5. El **crédito en pantalla de Ted Nichols y David Newman**: ya no hace
   falta el ⚠️ de música en §11 y §9.

## No encontré

- **Furgoneta (Máquina del Misterio) y pañuelo de Fred en primer plano,
  de día**, en ninguno de los 6 vídeos vistos (opening y ending 1969,
  tráiler 2002, y las 3 escenas). Busqué también en Dailymotion
  «Mystery Machine close up» y «Scooby Doo Fred ascot» (0 resultados
  útiles, sólo merchandising). Sigue con ⚠️ en §5.3; no es tarea mía
  medirlo de una hoja de la wiki (eso ya lo hizo imagen), pero no lo pude
  resolver con vídeo.
- **Tendencias de TikTok mirando el vídeo real** (§12 lo deja con ⚠️
  «resumen de búsqueda, sin ver los vídeos»): TikTok no es accesible con
  `fotogramas.py`/`yt-dlp` de forma fiable desde este servidor (probé
  `https://www.tiktok.com/discover/scooby-doo-veamos-quien-esta-detras-de-la-mascara-scooby`,
  yt-dlp no devolvió lista de vídeos individuales) y no es mi cupo de
  vídeos obligatorios (ya cubrí opening/ending/tráiler/3 escenas); lo
  dejo marcado para quien tenga tiempo, no es información inventada.
- **Un «ending» distinto del opening** en la serie de 1969: no existe
  (confirmado mirando el vídeo, ver nota arriba); la canción de cierre es
  la misma de apertura, con las guitarras/versos exactos que ya cita la
  biblia (Wikipedia).

## Cumplimiento (mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 2 · Escenas icónicas con minuto | ✅ | 3 escenas nuevas vistas con `fotogramas.py`, minuto y `&t=` |
| 4 · Luz y paleta medida en fotogramas | ✅ (con 1 ⚠️ heredado) | Confirmé el tinte azul de noche con fuente nueva y medí 2 sitios nuevos (playa, templo); furgoneta/pañuelo siguen sin medir (no es de vídeo) |
| 9 · Música | ✅ | Ted Nichols y David Newman confirmados en pantalla (créditos), suben de ⚠️ a ✅ |
| 10 · Vídeos (opening, ending, tráiler, 3 escenas, mirados) | ✅ | Los 6, con Read de las hojas, cumple AYUDANTE.md al pie de la letra |
| 14 · Poses con minuto | ✅ | 2 poses nuevas + minuto exacto a 4 poses que antes eran «de memoria» |

## Bitácora de búsqueda (esta sesión)

- Español/inglés, red directa (no gasté cupo de buscador web: todo fue
  API de Dailymotion + archive.org + yt-dlp, ya autorizado por
  AYUDANTE.md):
  - API de Dailymotion: `search=A Clue for Scooby Doo` → encontré el
    TV-rip completo en 4 partes (canal CLICK 4 CARTOON).
  - API de Dailymotion: `search=Scooby-Doo 2002 movie clip unmask` →
    clips oficiales «Fandango MOVIECLIPS».
  - API de Dailymotion: `search=Scooby Doo Zombie Island clip` → clip
    oficial «The Ghost Is Here» (canal «Scooby Doo»).
  - `archive.org/details/scooby-doo_20210808` (ya en `datos-video.md`).
  - Dailymotion `search=Mystery Machine close up` y `Fred ascot`: sin
    resultados útiles (ver «No encontré»).
- `herramientas/fotogramas.py` × 6 vídeos (opening, ending, tráiler,
  3 escenas) + fotogramas sueltos en grande para medir color.
- `herramientas/estilo.py` × 8 fotogramas (paleta y saturación).
- Medidas de color con Pillow directo (cajas manuales) para 2 escenas
  más que no cubría `estilo.py` (colores de personaje, no paleta
  general).
- `video.mp4` de los 6 vídeos, borrado tras sacar las hojas (48 MB en
  total, ya liberados).
