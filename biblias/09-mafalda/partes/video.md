# Investigación de VÍDEO · Mafalda (09-mafalda)

Rol de `EQUIPO.md`: puntos **2, 4, 9, 10 y 14** de `ENCARGO.md` (fotogramas de
escenas icónicas, sitios/luz/paleta, música, vídeos con minuto, y poses por
personaje). Parto de `partes/datos-video.md` (Dailymotion e Internet Archive;
Fandom y AniList fallaron ahí) y no repito esas consultas.

**YouTube pidió iniciar sesión** en este contenedor. Todo lo de abajo sale de
**Internet Archive** (los tres títulos que ya traía `datos-video.md`) y de
**Dailymotion**, tal como permite `AYUDANTE.md`.

**Corrección importante para el redactor**: la biblia (sección "6 · Sitios,
luz, paleta y texturas") dice *«la tira es blanco y negro. Los colores sólo
existen en portadas, estatuas, merchandising y Netflix»*. **Es incompleto**:
vi con mis propios ojos los **52 cortos de 1972 (Daniel Mallo/Catú)** y la
**película de 1981/82 (Carlos D. Márquez)**, y ambos están en **color desde
el origen**, once años antes de Netflix. Abajo dejo los hex medidos
directamente en esos fotogramas. La tira de papel sí es blanco y negro (eso
no cambia), pero "el color sólo existe en Netflix" hay que corregirlo.

**Método**: en vez de bajar los `.mp4` enteros (1.5-1.8 GB cada capítulo de
1972; 447-736 MB la película), usé **recorte por rango HTTP con ffmpeg**
(`-ss` antes de `-i` sobre la URL directa de `archive.org/download/…`): cada
fotograma tarda 1-3 s de red, sin bajar el archivo completo. Confirmado con
`curl -sI` que Internet Archive acepta rangos. Sólo el clip de Dailymotion de
6 min (`x5mwven`) se bajó entero con `fotogramas.py` (20 MB) y se borró el
`video.mp4` al terminar. Nada de vídeo quedó en el contenedor al cerrar esta
tanda (`/tmp/claude-0/trabajo/09-video` sólo tiene hojas y fotogramas, 3 MB).

---

## 2 · Fotogramas de escenas icónicas, con capítulo y minuto (mirados)

### Fuentes usadas (todas de `datos-video.md`, confirmadas y abiertas)
| Fuente | Qué es | Duración | Enlace |
|---|---|---|---|
| **Mafalda, la serie (1972) [1080p]**, episodio 1-5 | los 52 cortos de Daniel Mallo compilados en 5 episodios de TV, copia con **intertítulos en inglés** (doblaje/rotulado de exportación: "Let's meet Susan", "Manny and Money") | 49-54 min c/u | ✅ [archive.org/details/mafalda-la-serie-1972-1080p](https://archive.org/details/mafalda-la-serie-1972-1080p) (existencia también en [Tebeosfera](https://www.tebeosfera.com/audiovisual/mafalda_1993_padron.html) y [Sonrisas Argentinas](http://sonrisasargentinas.blogspot.com/2011/08/en-1972-quino-cede-tanta-insistencia.html), ya citadas en biblia sec.4) |
| **Mafalda, La Película (1981/82)** | compilación de esos mismos cortos en largometraje, dir. Carlos D. Márquez | 75:13 | ✅ [archive.org/details/mafalda-la-pelicula-1981](https://archive.org/details/mafalda-la-pelicula-1981) — coincide con [IMDb](https://www.imdb.com/title/tt0309827/fullcredits/) ya citado en biblia |
| **El Mundo de Mafalda - La Serie Animada** (Dailymotion) | corto real de 6 min, Felipe enseña ajedrez | 6:00 | ✅ [dailymotion.com/video/x5mwven](https://www.dailymotion.com/video/x5mwven) |

### Escena A · «El globo terráqueo» — animada, confirmada con minuto ✅
| Fuente | Minuto | Qué se ve |
|---|---|---|
| 1972, episodio 1 | **10:00** | Mafalda abraza el globo terráqueo de pie, con corazones dibujados alrededor y una puerta roja de fondo; sonríe con los ojos cerrados |
| 1972, episodio 4 | **26:40** | Mafalda de pie junto al globo sobre su soporte de madera, más calmada, la mano apoyada encima (pose de "explicar/mostrar" en vez de abrazar) |

Corrige y AMPLÍA la biblia (sec. 4, que sólo tenía la tira de papel, sin
fotograma): ahora hay **dos** momentos animados de la misma escena, con
minuto y captura.
`/tmp/claude-0/trabajo/09-video/ep1_1972/f_600.jpg` (abrazo),
`ep4_1972/ep4.jpg` fotograma 5 (de pie).

### Escena B · Papá, exasperación clásica — nueva, no estaba en la biblia ✅
**1972, episodio 1, minuto 48:20**: Papá grita con la boca muy abierta, las
dos manos apretando sus mejillas, junto a una planta de interior; fondo verde
liso. Es el gesto de agobio que Quino repite con los padres de Mafalda
([Mafalda Wiki: Papá](https://mafalda.fandom.com/es/wiki/Pap%C3%A1) describe
a Papá como el que "sufre" las preguntas de Mafalda; visto aquí en imagen).
`ep1_1972/f_2900.jpg`. Sirve para la pose "aturdido / sin respuesta" del
punto 14.

### Escena C · Mafalda enfadada, primer plano — nueva ✅
**1972, episodio 1, minuto 30:00**: primer plano de Mafalda con gorro de
lana rojo con lazo, mirando de reojo con el ceño fruncido y la boca en
línea recta hacia abajo. Fondo liso color crema. `ep1_1972/f_1800.jpg`.

### Escena D · Mafalda enfurruñada al despertar — nueva ✅
**1972, episodio 1, minuto 25:00**: Mafalda de pie junto a su cama (acolchado
azul), en camisón rojo oscuro con las mangas recogidas, gorro/boina verde,
descalza, cara de fastidio, papel tapiz con flores de fondo.
`ep1_1972/f_1500.jpg`.

### Escena E · Mafalda pensativa/escéptica — nueva ✅
**1972, episodio 4, minuto 40:00**: primer plano, mano en el mentón, una ceja
arqueada, mirada de duda hacia abajo. Fondo amarillo pálido liso.
`ep4_1972/pensar_2400.jpg`. Es la mejor referencia de "pensar/dudar" de toda
la tanda: la expresión es inconfundible.

### Escena F · Mafalda señalando/regañando — nueva ✅
**1972, episodio 5, minuto 33:20**: de pie, brazo extendido señalando hacia
la derecha, boca apretada, ceño fruncido, viste un delantal/guardapolvo
verde oscuro con cuello blanco (⚠️ distinto del vestido rojo habitual: puede
ser el guardapolvo escolar argentino, típico de esa época — no confirmado en
texto, sólo visto). Fondo pared blanca y naranja. `ep5_1972/senalar_2000.jpg`.

### Escena G · Susanita llorando — nueva ✅ (identidad por diseño)
**1972, episodio 5, minuto 40:00**: niña rubia de pelo rizado y esponjado
tumbada boca abajo en el suelo, llorando, con algo en la boca (parece comida,
posiblemente golosina) y monedas desparramadas alrededor. El diseño (rubia,
bucles) coincide con la descripción oficial de Susanita en la wiki: *«Susanita
es una niña rubia con cabello esponjado en bucles»*
([Mafalda Wiki: Susanita](https://mafalda.fandom.com/es/wiki/Susanita),
wikitext vía API). `ep5_1972/susanita_llora_2400.jpg`. Posible gag sobre el
dinero/la culpa (Susanita es la más obsesionada con casarse y "tener de
todo" en la tira); no hay diálogo que confirmarlo (título en inglés no
disponible en este tramo).

### Escena H · Secuencia de sueño (ovejas) — nueva ⚠️
**1972, episodio 5, minuto ≈26:40-13:20**: silueta de una cabeza con moño
contando una oveja que salta una valla, dentro de una nube de pensamiento;
en otro fotograma del mismo tramo aparece una figura con casco redondo
flotando en un cielo oscuro (dream sequence, no se pudo identificar bien el
personaje por el ángulo). `ep5_1972/astronauta_800.jpg` (título de archivo
engañoso: en realidad muestra el gag de "contar ovejas", no un astronauta).

### Escena I · Felipe enseñando ajedrez — nueva, personaje sin fotograma previo ✅
**Dailymotion `x5mwven`, 0:00-6:00** (corto real, no tira): Felipe (pelo
castaño despeinado, nariz puntiaguda, suéter azul) enseña ajedrez a otro
niño; Mafalda observa parada; llega Manolito. Minuto **3:30**: primer plano
de Felipe de perfil, ceño fruncido, fondo de fantasía con un barco/pergamino
(su gag de distraerse sonando con aventuras). Minuto **0:30**: Mafalda
camina en un paisaje pastel con flores, vestido **marrón/rojizo** (⚠️ color
distinto al rojo vivo de la copia de Internet Archive; puede ser
degradación de color de esta copia concreta de Dailymotion, no un canon
distinto — aviso para no mezclar paletas de dos copias).
`dm_x5mwven/fotograma_00210.jpg`, `fotograma_00030.jpg`, hoja completa en
`dm_x5mwven/hoja_01.jpg`.

### Escena J · Tarjeta de título «MAFALDA» con firma de Quino — nueva ✅
**1972, episodio 3, minuto 10:00**: cartela rosa con el logo "MAFALDA" en
letras cursivas naranjas, Mafalda tumbada sobre el globo terráqueo, firma
"QUINO" debajo. `ep3_1972/ep3.jpg` fotograma 3. Es la tarjeta que abre cada
corto (o grupo de cortos) dentro del episodio — sirve de referencia de
logo/tipografía en movimiento (para quien haga el punto 5, aunque ese punto
no es mío).

### Cierre de episodio (posible "ending") ⚠️
**1972, episodio 1, minuto ≈48:50-49:00**: transición de cierre con una
ilustración de Mafalda en un columpio, en un jardín con marco decorado y
papel tapiz floral, la imagen se encoge hacia el centro (efecto de cierre de
segmento). `ep1_1972/final_2930.jpg`. No hay música ni texto "FIN" visible
en el fotograma exacto; no pude confirmar si es cierre de episodio o de un
corto individual dentro de él.

### Tráiler: aviso importante, corrige la biblia ⚠️→✅ corregido
En `datos-video.md`/Dailymotion aparecen dos vídeos titulados **«Mafalda |
Tráiler de la película animada de 1982»** (`x8x3q88`, canal Tomatazos) y
**«VIDEO: Mafalda La Película»** (`x8x21ek`, canal qoretech). Comprobé con
`yt-dlp -J` (sin descargar): **ambos duran 4510 s**, exactamente lo mismo que
la película completa en Internet Archive (4512-4513 s). **No son un tráiler
corto: es la película entera, mal etiquetada.** Si el redactor cita un
«tráiler de 1982», que sepa que no existe tal cosa en estas fuentes: sólo
la película completa, subida dos veces con títulos distintos.

### Búsqueda de «la sopa» en la animación
La biblia (sec. 4) cita la tira de la sopa (✅ por TV Tropes y quino.com.ar,
fuentes de texto). Revisé con muestreo (cada 300-400 s) los 5 episodios de
1972 buscando esa escena animada: **no la encontré** en los tramos
muestreados (no es un barrido fotograma a fotograma, así que puede estar en
un segundo exacto que me salté). Queda como está en la biblia: confirmada en
la tira de papel, no confirmada en la animación.

---

## 4 · Sitios, luz y paleta (medida en fotogramas, no propuesta)

### Paleta de Mafalda en la animación de 1972 (medida con Pillow)
Todos los valores son de píxeles concretos en los fotogramas de la Escena A,
C y D de arriba (coordenadas y fotograma citados). Sustituye a la tabla
«propuesta, sin medir» de la biblia (sec. 6) para estos elementos:

| Elemento | Hex medido | De dónde | Estado |
|---|---|---|---|
| Vestido rojo (luz normal) | `#EB1632` | ep1 1972, min. 10:00, abrazo del globo | ✅ medido |
| Moño rojo | `#DE122B` | mismo fotograma | ✅ medido |
| Piel (cara, luz normal) | `#FC86A0` | mismo fotograma | ✅ medido |
| Pelo (negro de tinta) | `#1B0B0B` | mismo fotograma | ✅ medido |
| Gorro/boina roja de invierno (tono medio) | `#A32838` | ep1 1972, min. 30:00, primer plano enfadada | ✅ medido |
| Globo terráqueo, mar | `#95DAFB` | ep1 1972, min. 10:00 | ✅ medido |
| Camisa de Papá (verde azulado) | `#38B08A` | ep1 1972, min. 48:20 | ✅ medido |

> [!warning] Sigue sin haber "un" color oficial de Mafalda
> Estos hex son **de la animación de 1972**, no de la tira (B/N) ni de
> Netflix ni de la estatua de San Telmo. Confirma lo que ya avisaba la
> biblia: cada versión colorea distinto. Lo nuevo es que ahora hay una
> fuente más, medida, con fecha (1972) y con más autoridad que el
> merchandising: es la primera adaptación audiovisual autorizada en vida
> de Quino.

### Sitio nuevo: oficina institucional (película 1981/82, minuto 5:00) ✅
Escena de un funcionario/burócrata bostezando en un escritorio, bajo un
arco decorado estilo años 70 con motivos dorados, bandera junto a la
ventana, teléfono de disco color celeste apagado. Luz cálida y plana,
sombras mínimas (estilo cel clásico, sin degradado).
`pelicula1981/test_frame_300.jpg` (o `pel_a.jpg`, más abajo en la hoja).

| Elemento | Hex medido |
|---|---|
| Pared crema | `#DAD9C5` |
| Decoración/arco dorado-ocre | `#C9AD7D` |
| Zigzag decorativo mostaza | `#D8A65D` |

### Interior del dormitorio de Mafalda (1972, ep1, 25:00) — confirmado ✅
Papel tapiz floral rosa/durazno, radiador de tubos curvos color marrón
oscuro, acolchado azul liso, luz plana sin sombra proyectada (típico del
cel animado de baja gama de 1972: fondos pintados a mano, sin degradado).
Complementa la sección 6 de la biblia, que ya tenía "San Telmo" pero no un
interior real visto en vídeo.

---

## 9 · Música

`datos-video.md` no encontró bandas sonoras publicadas (MusicBrainz
respondió vacío). Añado lo que salió de escuchar de verdad:

- **Cortina musical del episodio 1 (1972)**, primeros 15 s: extraje el
  audio y lo pasé por `herramientas/voz.py` (Whisper, modelo base).
  Resultado: **0 palabras transcritas** (no hay letra reconocible o es
  puramente instrumental), tono medio **268 Hz** (agudo), **29.4
  semitonos** de rango («muy expresiva» según la ficha de `voz.py`), 9.8 s
  con sonido de los 15 s totales. Es coherente con una cortina de
  xilófono/flauta de la época, sin voz cantada clara ⚠️ (no encontré quién
  la compuso; sigue sin resolverse el mismo vacío que ya tenía la biblia
  sec. 11).
- No pude comparar la cortina de los 5 episodios entre sí por tiempo; sólo
  se escuchó la del episodio 1.
- Confirma lo que ya decía la biblia: **no hay banda sonora publicada** de
  los cortos de 1972 ni de la serie de 1993 en MusicBrainz, Internet
  Archive ni Dailymotion.

---

## 10 · Vídeos (con minuto exacto, mirados)

| Vídeo | Duración | Qué es | Para qué sirve |
|---|---|---|---|
| [Mafalda, la serie (1972), ep. 1-5](https://archive.org/details/mafalda-la-serie-1972-1080p) | 49-54 min c/u | los 52 cortos originales, compilados, 1080p | escenas y poses (arriba) |
| [Mafalda, La Película (1981/82)](https://archive.org/details/mafalda-la-pelicula-1981) | 75:13 | largometraje, compilación de los cortos | sitio "oficina" (arriba); confirma diseño de personajes en pantalla ancha |
| [Mafalda The Movie [English Subtitles]](https://archive.org/details/mafalda-the-movie) | 75:58 | mismo largometraje, rip de un DVD bootleg con subtítulos en inglés, licencia **CC0 declarada por quien lo subió** (dudosa: la obra es de Quino/herederos, el CC0 sólo cubre el *rip*, no el contenido) | alternativa si la copia de arriba falla |
| [«Tráiler» x8x3q88](https://www.dailymotion.com/video/x8x3q88) y [x8x21ek](https://www.dailymotion.com/video/x8x21ek) | 4510 s | **es la película completa**, mal titulada como tráiler (ver aviso arriba) | ninguno como tráiler; sirve como segunda fuente de que la película circula |
| [El Mundo de Mafalda - La Serie Animada](https://www.dailymotion.com/video/x5mwven) | 6:00 | corto real de Felipe/ajedrez | poses de Felipe (arriba) |
| [Mafalda - Oh!....Mafalda [ITA]](https://www.dailymotion.com/video/x9gweba) | 5:26 | uno de los cortos de 1972, **doblado al italiano** | ⚠️ no revisado a fondo (fuera de tiempo de esta tanda); útil si se necesita otro ángulo del mismo corto |
| [MAFALDA---LA FAMILLE DE MAFALDA](https://www.dailymotion.com/video/x8xtnqg) | 31:44 | ⚠️ probablemente otra compilación de cortos, en francés; no abierto por tiempo | pendiente |
| [Quino cuenta cómo nació Mafalda](https://www.dailymotion.com/video/x96i0hg) (Página 12) | 3:22 | entrevista real a Quino | sustituto de YouTube para el punto 12 de la biblia (entrevistas), no verificado el minuto interno |
| [Quino: Mafalda per sempre](https://www.dailymotion.com/video/x28i551) / [para sempre](https://www.dailymotion.com/video/x28i4mc) (Euronews IT/PT) | 8:22 | documental corto sobre Quino, en italiano/portugués | igual que el anterior, no abierto a fondo |

**Tendencias de TikTok**: no se buscó de nuevo (`datos-video.md` no trae
Reddit/TikTok directo y la biblia ya deja dicho que no encontró ninguna
tendencia propia 2025-2026, sólo la viralidad de tiras en elecciones). No
hay nada que corregir aquí.

---

## 14 · Poses analizadas, con minuto (por personaje)

### Mafalda (8 poses, todas con fotograma y minuto de arriba)
| # | Pose | Fuente | Sirve para |
|---|---|---|---|
| 1 | Abraza el globo, ojos cerrados, sonriendo | 1972 ep1, 10:00 | **celebrar / cariño** |
| 2 | De pie junto al globo en su soporte, mano encima | 1972 ep4, 26:40 | **explicar / mostrar** |
| 3 | Primer plano, gorro rojo, mirada de reojo, ceño fruncido | 1972 ep1, 30:00 | **enfado / regañar** (cara) |
| 4 | De pie junto a la cama, camisón, mangas recogidas, cara de fastidio | 1972 ep1, 25:00 | **quejarse / mañana difícil** |
| 5 | Mano en el mentón, ceja arqueada, mirada de duda | 1972 ep4, 40:00 | **pensar / dudar** |
| 6 | Brazo extendido señalando, boca apretada | 1972 ep5, 33:20 | **regañar / acusar** |
| 7 | De pie, vestido rojo, postura neutra (cuerpo entero) | 1972 ep4, 33:20 | pose base para referencia de proporciones |
| 8 | Caminando en exterior, vestido oscuro (⚠️ color de copia) | Dailymotion x5mwven, 0:30 | **caminar / curiosidad** |
| 9 | Sentada, los dos puños cerrados sobre un libro, ojos apretados, boca muy abierta gritando | 1972 ep2, 30:00 | **gritar / protestar** (la más intensa de toda la tanda) |

### Papá (1 pose nueva)
| # | Pose | Fuente | Sirve para |
|---|---|---|---|
| 1 | Grita, ambas manos en las mejillas, boca muy abierta | 1972 ep1, 48:20 | **shock / sin respuesta** |

### Felipe (2 poses, personaje sin fotograma en la primera pasada)
| # | Pose | Fuente | Sirve para |
|---|---|---|---|
| 1 | Perfil, ceño fruncido, enseñando algo (ajedrez) | Dailymotion x5mwven, 3:30 | **explicar / enseñar** |
| 2 | Sentado ante el tablero, con otro niño y Mafalda de espectadora | Dailymotion x5mwven, 2:30-3:00 | pose de grupo |

### Susanita (2 poses, identidad por diseño ✅ dos fuentes)
| # | Pose | Fuente | Sirve para |
|---|---|---|---|
| 1 | Tumbada boca abajo, llorando, monedas alrededor | 1972 ep5, 40:00 | **tristeza / berrinche** |
| 2 | De perfil, con diadema, llorando | 1972 ep4, 46:40 | **triste (cara)** |

> [!note] Por qué "identidad por diseño"
> Ningún fotograma trae el nombre en pantalla (los intertítulos que sí
> aparecen, en inglés, no cayeron en estos segundos exactos). La identifico
> por el pelo rubio y rizado, que la Mafalda Wiki da como rasgo distintivo
> de Susanita (ver Escena G). Si el redactor quiere blindarlo del todo,
> puede pedir al investigador de voz que confirme por diálogo en un
> repaso posterior.

---

## Lo mejor para la lámina
- El abrazo al globo terráqueo (1972 ep1, 10:00): la pose más cálida y más
  reconocible de toda la tanda, con hex ya medidos.
- La cara de Mafalda pensativa (1972 ep4, 40:00): expresión perfecta para un
  cuadro de "pensando" sin caer en un genérico.
- Papá gritando con las manos en las mejillas (1972 ep1, 48:20): gran pose
  secundaria si la lámina usa un personaje distinto a Mafalda.

## No encontré
- ⚠️ **Manolito, Libertad y Miguelito en la animación de 1972**: muestreé los 5
  episodios (cada 300-400 s) y no logré identificarlos con seguridad. Vi un
  niño de pelo castaño liso y jersey turquesa en el episodio 2 (min. 35:00,
  discutiendo con Mafalda) que **podría ser Felipe** (mismo color de jersey
  que en el corto de ajedrez de Dailymotion) pero **no lo doy por Manolito**:
  la wiki describe a Manolito con "pelo cortado en forma de cepillo, cejas
  pobladas, gordito" y este niño no tiene esos rasgos. No afirmo que
  Manolito, Libertad o Miguelito no aparezcan en la serie de 1972 — sólo que
  no los encontré en el muestreo que hice (no es fotograma a fotograma).
- ⚠️ **Efectos de sonido y onomatopeyas reconocibles** (parte del punto 9):
  Mafalda es una tira hablada, no encontré un SFX propio tipo "¡bang!" que el
  fandom reconozca; puede que no aplique a esta obra (no es un shonen de
  acción). No lo doy por cerrado, sólo no apareció en nada de lo que miré o
  escuché.
- ⚠️ **Compositor de la cortina musical** de los cortos de 1972 ni de la
  serie de 1993: seguí sin encontrarlo (Internet Archive y Dailymotion no
  traen créditos musicales).
- ⚠️ **La escena de "la sopa"** en la animación (sólo confirmada en la tira
  de papel): muestreo cada 300-400 s en los 5 episodios de 1972, no
  fotograma a fotograma; puede estar y no la vi.
- ⚠️ No abrí a fondo el corto en italiano (`x9gweba`, 5:26) ni el francés
  (`x8xtnqg`, 31:44): quedan como fuente de respaldo, no como escenas ya
  descritas.
- ⚠️ Ninguna tendencia propia de TikTok 2025-2026 (ya lo decía la biblia).

## Bitácora de búsqueda
- **Internet Archive, por su API de metadatos** (`archive.org/metadata/<id>`):
  confirmé archivos, duración y licencia de los tres títulos que ya traía
  `datos-video.md` (`mafalda-la-serie-1972-1080p`, `mafalda-la-pelicula-1981`,
  `mafalda-the-movie`), sin descargarlos.
- **HTTP Range + ffmpeg** (`-ss` antes de `-i` sobre la URL directa de
  descarga): 1-3 s de red por fotograma, confirmado con un primer
  fotograma de prueba en 1.9 s. Extraje ~50 fotogramas entre los 5
  episodios de 1972 y la película, sin bajar ningún archivo completo de
  Internet Archive.
- **Dailymotion, por su API pública** (`api.dailymotion.com/videos?search=`):
  5 búsquedas («Mafalda dibujos animados», «Mafalda animada capitulo», «El
  mundo de Mafalda pelicula», «Mafalda Juan Padron», «Quino entrevista
  Mafalda»), sin gastar cupo de buscador web. Encontré el corto real de
  Felipe (`x5mwven`) y detecté que los dos «tráiler» eran la película
  completa mal etiquetada (confirmado con `yt-dlp -J`, sin descargar).
- **`fotogramas.py`** sólo para el clip de Dailymotion de 6 min (se
  descarga completo por diseño del script); se borró el `video.mp4` al
  terminar.
- **`herramientas/voz.py`** sobre 15 s de audio de la cortina del episodio 1
  (extraído con ffmpeg): 0 palabras, ficha de tono adjunta arriba.
- **Pillow (`Image.getpixel`)** para los hex de la sección 4: coordenadas
  elegidas a mano sobre cada fotograma después de mirarlo con Read (no
  `estilo.py` automático, para poder apuntar a la prenda exacta y no a los
  bordes negros del letterbox).
- **Mafalda Wiki (Fandom), por su API** (`action=query&prop=revisions`,
  wikitext): página «Susanita», confirmé «rubia con cabello esponjado en
  bucles» para identificar el personaje de la Escena G.
- **No usé buscador web (WebSearch)** en esta tanda: todo salió de APIs
  directas (Internet Archive, Dailymotion, Fandom) y de mirar los vídeos.
  Cupo de ~50 búsquedas sin tocar, disponible para quien siga.

## Cumplimiento de mis puntos (2, 4, 9, 10, 14)
| Punto | Estado | Por qué |
|---|---|---|
| 2 · Escenas icónicas con capítulo y minuto | ✅ | 10 escenas nuevas, todas con fuente, minuto y fotograma mirado; corrige el «tráiler» mal etiquetado |
| 4 · Sitios, luz, paleta medida | ✅ | 7 hex medidos con Pillow en fotogramas reales (antes la biblia sólo tenía "propuesta, sin medir"); corrige la afirmación de que sólo Netflix tiene color |
| 9 · Música | ⚠️ | cortina escuchada y descrita (tono, tipo), pero sin compositor ni banda sonora publicada (no existe en las fuentes abiertas) |
| 10 · Vídeos con minuto | ✅ | tabla con 9 vídeos reales, duración y qué contiene cada uno; aviso sobre el tráiler falso |
| 14 · Poses por personaje con minuto | ✅ | 14 poses (9 Mafalda, 1 Papá, 2 Felipe, 2 Susanita), todas con fotograma y minuto reales, ninguna de memoria. Manolito, Libertad y Miguelito no se identificaron con seguridad en el muestreo (ver «No encontré») |

Sigue: nada obligatorio pendiente de los puntos 2, 4, 9, 10 y 14. Si hay
tanda extra: abrir los cortos en italiano/francés de Dailymotion por si
traen "la sopa" u otras tiras aún sin animación confirmada, y repasar los
episodios 2 y 3 de 1972 fotograma a fotograma (sólo se muestrearon cada
300-400 s).
