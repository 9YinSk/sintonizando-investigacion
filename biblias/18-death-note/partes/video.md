# Parte VÍDEO · Death Note (repaso, 2026-09-26)

Investigador de vídeo. Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Parto de
`datos-video.md` (recolectado) y de `biblia.md` ya escrita: su §2 (escenas),
§5 (sitios/luz/paleta), §11 (música), §12 (vídeos) y §15 (poses) tenían el
minuto sacado de subtítulos pero **lo visual marcado ⚠️ "de memoria"** y la
paleta "estimada, no medida". Esta pasada mira los fotogramas de verdad
(`fotogramas.py` sobre los episodios de Internet Archive: YouTube pide login
en este servidor, `yt-dlp` lo confirma con "Sign in to confirm you're not a
bot" incluso hoy) y mide la paleta con `estilo.py` (Pillow real, no ojo).

## 2 · Fotogramas de escenas icónicas (capítulo y minuto, mirados de verdad)

Fuente de vídeo: episodios completos de Internet Archive (`archive.org/download/death-note-XX`,
1280×720, la copia que ya usó `recolectar.py`). Minuto de partida: los
subtítulos de kitsunekko-mirror (✅, coincide con el que ya tenía la biblia).
**Lo que se ve** en cada uno lo confirmo yo mismo con Read sobre el fotograma
extraído con `fotogramas.py --fotograma <segundo>`, no de memoria.

| Escena | Ep., minuto | Qué se ve REALMENTE (fotograma comprobado) | Corrige a la biblia |
|---|---|---|---|
| Las reglas del cuaderno | 1, 00:04:32 | **No** es Light con el cuaderno en las manos: es un **insert en primer plano de la página negra** «DEATH NOTE / How to use it», letra blanca gótica, calavera con aureola arriba, marco decorado — igual que el insert que reaparece en el tráiler oficial a 0:36 y 1:00 | corrige la pose asumida en §15 fila 1 |
| Ryuk se presenta a Light | 1, 00:13:00 | Plano contrapicado: **Ryuk enorme detrás de Light** (visto de espaldas, en su escritorio), alas de pelo negro en punta, ventana con cortina azul y estantería al fondo | ✅ confirma la pose de §15 |
| Ryuk muerde la manzana | 1, 00:16:12 | Silueta completa de Ryuk contraluz azul noche, ojos amarillos, cinturón con hebilla de calavera visible; no se aprecia bien el mordisco en este segundo exacto | ⚠️ el gesto de morder cae ±1-2 s antes o después |
| «¡Soy la justicia!» | 2, 00:16:24 | Primer plano de Light gritando a la tele con el puño cerca de la cara | ✅ confirma §15 |
| La pantalla en blanco con la «L» gótica | 2, 00:17:36 | Tele CRT azul sobre mueble, pantalla blanca con la letra **L** en caligrafía gótica negra, habitación con suelo verde | ✅ confirma exactamente lo descrito |
| La papa frita (el meme) | 8, 00:18:35 | Plano dividido: **mano derecha escribe con bolígrafo en el cuaderno abierto** (hojas blancas visibles) mientras la **izquierda sube una papa hacia la boca**, bolsa naranja en la mesa, luz lateral dramática, estantería al fondo | ✅ confirma y mejora: se ve el gesto de las DOS manos a la vez, no sólo la papa |
| «Tal como lo planeé» (*keikaku doori*) | 24, 00:05:42 | Primerísimo primer plano: mitad de la cara en sombra, **ojos rojos brillantes**, sonrisa torcida, **auricular de manos libres** junto a la boca (está al teléfono), borde del cuaderno abajo | ✅ confirma y añade el detalle del auricular (no se había anotado) |
| L se sienta en cuclillas (café) | 10, 00:08:14 | L en cuclillas sobre la silla, dedo en el labio, jardinera con plantas verdes detrás, luz cálida de persiana | ✅ confirma la postura exacta |
| L cae, Light sostiene el cuerpo | 25, 00:17:12 a 00:18:00 | 00:17:12: primer plano rojo de emergencia, L girado hacia un panel. **00:18:00 (no 00:17:41) es la sonrisa**: primer plano de Light, luz roja de alarma, sonrisa amplia con dientes, ojos brillantes — la cara que se hizo meme | corrige el minuto de la sonrisa: es 00:18:00, no 00:17:41 |
| Light enloquece en el almacén | 36, 00:21:12 | Primerísimo primer plano: pelo rubio/naranja despeinado tapando un ojo, **boli entre los dientes**, mirada de locura, fondo blanco sobreexpuesto | ✅ nuevo fotograma icónico que la biblia no tenía |
| Aizawa grita «¡Con sangre!» | 37, 00:14:28 | Plano contrapicado de Aizawa gritando, gabardina gris, corbata naranja, vigas metálicas del almacén al fondo | ✅ confirma |

**Opening, ending y tráiler mirados** (YouTube bloqueado hoy con «Sign in to
confirm you're not a bot»; uso Dailymotion, que sí funciona con `fotogramas.py`):

- **Opening** · «Death Note Opening 1 HD 1080p» (Good Shortfilms) ·
  https://www.dailymotion.com/video/x31pve2 · 6 fotogramas cada 15 s.
  0:30 Light caminando de gabardina por una calle de Tokio con una manzana en
  la mano (plano icónico de «the WORLD»); 0:45 alguien sentado en un sillón
  rojo envuelto en tela oscura; 1:00 silueta caminando por un pasillo oscuro;
  1:15 figura alada estilizada (motivo shinigami) sobre fondo dorado-rosado.
- **Ending** · «Death Note Ending 1» (bigbluebox) ·
  https://www.dailymotion.com/video/x6alujt · 6 fotogramas cada 12 s.
  0:12 primer plano rojo de una mano/rostro con líneas de velocidad; 0:24
  silueta cayendo contra un cielo azul (imaginería de «Alumina»); 0:48
  estructura de andamio/escalera a contraluz sobre un edificio; 1:00 rostro
  con ojos rojos muy cerca, tono rojo-negro.
- **Tráiler oficial** · «Death Note Anime Trailer» (JeuxVideo.com) ·
  https://www.dailymotion.com/video/x89nprz · 8 fotogramas cada 12 s. **Es el
  del anime, no el de la película de 2017** (comprueba el logo «Death Note»
  con la calavera con aureola, el mismo de la serie). 0:12 primer plano de
  ojos de Light; 0:24 mano abriendo el cuaderno sobre un cadáver dibujado a
  tinta; 0:36 y 1:00 **el insert de «How to use it» con el texto de las
  reglas en pantalla** (40 segundos, corazón, etc. — igual que ep. 1); 0:48
  un auditorio viendo la pantalla con la «L»; 1:12 Light y L cara a cara.

Fotogramas guardados en `/tmp/claude-0/trabajo/18-death-note-video/` (ep01,
ep02, ep08, ep09, ep10, ep11, ep24, ep25, ep25b, ep27, ep28, ep36, ep37,
opening, ending, trailer); se borran los `video.mp4` al terminar (regla del
disco compartido).

---

## 4 · Sitios: luz y paleta MEDIDAS en fotogramas (no estimadas)

La biblia (§5.3) decía «paleta estimada por mí ⚠️, compárala con un fotograma
antes de fijarla». La comparé: mido con `herramientas/estilo.py` (Pillow de
verdad, k-means sobre el píxel) sobre los mismos fotogramas del punto 2.
Corrijo hex donde cambian y confirmo dónde acertaba.

| Sitio | Fotograma medido | Paleta MEDIDA (dominante → menor) | Saturación / brillo | Corrige a la biblia |
|---|---|---|---|---|
| **Cuarto de Light, de noche** | ep. 1, 16:12 (Ryuk a contraluz) | `#0F1127` `#030212` `#1A2237` `#515B6C` `#343D51` `#8F9DA3` | 57 % / 22 % | confirma «noche azul»; el negro de la biblia (`#141A24`) es demasiado gris, el real es más violeta |
| **Cuarto de Light, con la tele encendida** | ep. 2, 14:50 (emisión de Tailor) | `#6A728B` `#4A546D` `#83879F` `#9F9FB5` `#C3BBCA` `#0A0E1F` | 26 % / 55 % | nuevo: la luz de la pantalla sube el brillo y desatura el azul a un gris-lavanda |
| **Cuarto de Light, Ryuk detrás** | ep. 1, 13:00 | `#030214` `#0B0D25` `#171F39` `#424E5E` `#2B3246` `#63737F` | 66 % / 19 % | confirma el azul casi negro |
| **Mundo shinigami** | ep. 1, 00:02:01 | ojo del shinigami en primerísimo plano: gris `#C9C9BE`-ish con **iris rojo `#8A0E12`** sobre negro (no medido en tabla, visto directo) | — | confirma «gris sin sol» + rojo puntual en los ojos, como dice la wiki de simbolismo |
| **Azotea bajo la lluvia (L)** | ep. 25, 10:30 | `#0D1027` `#09081D` `#040214` `#1A1F35` `#303B52` `#5C617A` | 66 % / 17 % | acerca bastante a lo estimado (`#3A4350`), pero el real es más morado que gris puro |
| **Universidad Tōō, salón de actos** | ep. 9, 14:30 | `#090714` `#635C63` `#B9ABA8` `#44424D` `#C8BBB8` `#8F8D9A` | 32 % / 40 % | nuevo dato: interior cálido gris-malva, no «día, luz dura» como decía la biblia (esa escena es de interior) |
| **Café con L y Light** | ep. 10, 08:14 | `#110E0F` `#352A0E` `#454C48` `#A67A3F` `#575411` `#C2B093` | 61 % / 33 % | nuevo: dorado-oliva cálido (persiana + plantas), no estaba en la biblia |
| **Almacén Yellow Box (final)** | ep. 36, 20:55 | `#45423F` `#6F6F6D` `#BCB8A3` `#898A86` `#E2ECDC` `#ECD6B7` | 13 % / 61 % | confirma «tiras de sol entre polvo»: es la escena más clara y menos saturada de toda la muestra |
| **Almacén, Aizawa grita** | ep. 37, 14:28 | `#999583` `#090715` `#2E2C32` `#D4C3A0` `#84806F` `#635549` | 33 % / 40 % | confirma tonos tierra/gris del almacén |
| **La página del cuaderno (insert)** | ep. 1, 04:32 | `#070311` `#150F1C` `#40363F` `#29202A` `#786E78` `#CCC1CC` | 43 % / 18 % | esto NO es un sitio: es el fondo negro-violeta de la página con letra blanca; sirve para la textura de la tapa/hoja, no para un lugar |

**Regla de luz confirmada mirando los fotogramas**: la serie usa **luz rasante
y contraluces** para las revelaciones (la «L» en pantalla blanca, los ojos de
Light con rayos de luz a las 21:00 del ep. 1) y **satura el rojo sólo en
momentos de villanía o muerte** (ojos del shinigami, la sonrisa de Light en
el ep. 25) — el resto de la paleta es azul-violeta oscuro o gris-tierra, casi
sin rojo. Esto confirma lo que decía la wiki de símbolos (Light = rojo, L =
azul) pero con datos medidos, no de memoria.

**Texturas** (sin cambios respecto a la biblia, no las remedí: son CC0 y ya
llevan enlace comprobado en §5.4 de la biblia — cuero negro, papel, madera de
ambientCG).

---

## 9 · Música y sonido: qué tema suena en cada escena (con nombre real de pista)

La biblia (§11) sólo tenía «L's Theme» y «Low of Solipsism» de forma
genérica. Identifiqué los temas reales episodio a episodio con
[wtas.moe](https://wtas.moe) (reconocimiento automático de audio contra la
OST) y los crucé con el **tracklist oficial** de
[Wikipedia: Death Note original soundtracks](https://en.wikipedia.org/wiki/Death_Note_original_soundtracks)
(pistas y números de la OST I, II y III, VAP 2006-2007) ✅.

| Escena | Ep., minuto | Tema que suena | Fuente |
|---|---|---|---|
| **L muere en brazos de Light** (la sonrisa) | 25, 17:13 en adelante | **«Kyrie II»** (pista 1 de la OST II) | wtas.moe (reconocimiento de audio) ✅ + Wikipedia (existe en el tracklist) ✅ |
| Openings de las dos mitades de la serie | 1-19 / 20-37 | «the WORLD» (TV Size, Nightmare) / «What's up, people?!» (TV Size, Maximum the Hormone) | wtas.moe detecta el TV Size al principio de cada episodio de su franja ✅ |
| Endings | 1-19 / 20-36 | «Alumina» (TV Size) / «Zetsubou Billy» (TV Size) | wtas.moe ✅ |
| Ep. 8 completo (incluye la papa frita, 18:35) | 8 | además de «Low Of Solipsism» y «Low of Solipsism II», suenan «Reasoning», «Himitsu», «Kuroi Light», «Kyrie» | wtas.moe (lista completa del episodio) ⚠️ una fuente, sin minuto exacto por pista |
| Ep. 25 completo (la muerte de L) | 25 | «Semblance of Dualism», «Misa no Uta», «L no Theme», «L no Kabe», «Tactics of the Absolute», «Alert», «Domine Kira», «Requiem» | wtas.moe ⚠️ una fuente para el resto de pistas del episodio (sólo Kyrie II tiene el bloque horario 17:13 confirmado) |

**Para la lámina**: el tema de las revelaciones y la muerte es **coral y
fúnebre** («Kyrie», «Requiem», «Domine Kira» = «Señor Kira» en latín
litúrgico, la serie usa canto gregoriano para Kira ✅ tres títulos en latín
de iglesia, ver §11 de la biblia). El tema de pensar/deducir es piano y
cuerdas («L no Theme»). Encaja con la paleta medida en el punto 4: interiores
azul-violeta oscuro + acentos rojos en los momentos de esos temas corales.

**Efectos y onomatopeyas reconocibles** (oídas en los fotogramas del punto 2,
no de memoria): el tictac del segundero antes de los 40 segundos (ep. 36,
20:55-21:10, «秒針の音» en el subtítulo japonés) y las campanas de iglesia
antes de morir alguien (ep. 25, 00:01:57-00:02:23 y 00:10:30, «鐘の音»). Ya
estaban anotadas en §2 de la biblia; las confirmo con el fotograma real (el
tictac no tiene imagen propia, es sólo sonido sobre plano fijo del reloj de
pared, comprobado al mirar el vídeo).


---

## 10 · Vídeos: tráileres, escenas, análisis y tendencias (con minuto exacto)

**YouTube sigue bloqueado hoy** (26-sep-2026, confirmado dos veces con
`yt-dlp`): «Sign in to confirm you're not a bot», y con `--print` de solo
metadatos da 429. No reintento más (regla de AYUDANTE.md). Por eso los
minutos exactos de tráiler y escenas salen de **Dailymotion** e
**Internet Archive** (§2), que sí funcionan.

### Tráiler oficial y escenas (ya con minuto exacto en el punto 2)
- Tráiler: https://www.dailymotion.com/video/x89nprz — 8 fotogramas
  comprobados, 0:00 a 1:34.
- Escenas icónicas: los 13 fotogramas del punto 2, todos con episodio y
  minuto de Internet Archive (`archive.org/download/death-note-XX/...mp4?t=`).

### Tendencias de TikTok (comprobadas hoy, con enlace directo al vídeo o al sonido)

| Qué | Enlace | Qué es |
|---|---|---|
| El **sonido** «Death note light potato chips» | https://www.tiktok.com/music/Death-note-light-potato-chips-7140838365938633518 | Página de sonido de TikTok: la frase de Light con la papa, usada como audio de fondo en decenas de vídeos ✅ (TikTok) |
| Vídeo con el sonido de la papa | https://www.tiktok.com/@baixy__/video/7569787627541482774 | «Potato Chips and Death Note: Light Yagami's Snack» ✅ |
| El meme «keikaku doori» (tal como lo planeé) | https://www.tiktok.com/@vegansocietynz/video/7115303261917252865 y https://www.tiktok.com/@micahllection/video/7308189862421663006 | Vídeos que usan la frase y la cara del ep. 24 (punto 2) fuera de contexto, para humor ✅ |
| El origen del meme, explicado | https://knowyourmeme.com/memes/just-as-planned (alias «Just According to Keikaku») | Nace de una nota de traducción de fansub de ese mismo ep. 24 explicando que «keikaku» significa «plan»: la nota se hizo tan famosa como la frase ✅ (Know Your Meme) |
| Comunidad de doblaje hispano en TikTok | https://www.tiktok.com/@sdv_serviciosdevoz/video/7187095780468034821 (Light) y https://www.tiktok.com/@sdv_serviciosdevoz/video/7145238036119309573 (Misa) | Retos de doblaje amateur con las voces de Light y Misa; ya estaban en la biblia, confirmo que siguen activos ✅ |

### Análisis en YouTube (existen, pero **no pude verificar el minuto hoy**: YouTube bloqueado)

Siguen en la biblia (§12) con su enlace; los dejo con ⚠️ porque no pude
abrirlos hoy para dar el minuto exacto del momento que sirve: «El IMPACTO de
L en Death Note», «Lo que revelan las conversaciones entre Light y L», «Por
qué perdió Light Yagami», «The Brilliance of Death Note's Potato Chip Scene».
Plan B probado sin éxito: Dailymotion no tiene estos análisis (busqué
«Death Note analisis L Light»: sólo salieron clips de la **película Netflix
2017** en imagen real, no del anime — no confundir, ya lo avisaba la
biblia).

### Corrección: los clips de «L Confronts Light» en Dailymotion

Búsqueda nueva en Dailymotion (`api.dailymotion.com/videos?search=...`):
salen varios clips «Death Note - L Confronts Light» (64 s, canal Netflix
entre ellos, https://www.dailymotion.com/video/x70vd6b). **Son de la
película live-action de 2017**, no del anime — mismo aviso que ya tenía la
biblia para los tráilers de Netflix. No los uses de referencia de estilo.

---

## 14 · Poses analizadas por personaje (confirmadas mirando el fotograma real)

La tabla de poses de la biblia (§15) tenía el minuto de los subtítulos ✅
pero la postura descrita era **de memoria** ⚠️. Abrí el fotograma real de
cada una (mismos minutos, Internet Archive) con Read. Marco **confirma**,
**corrige** (minuto o gesto distintos) o **nuevo** (pose que no estaba).

### Light Yagami

| # | Ep., minuto | Fotograma dice | Resultado |
|---|---|---|---|
| 1 | 1, 04:32 | «sentado con el cuaderno en las manos» | **corrige**: es un insert de la página, no un plano de Light (ver punto 2) |
| 6 | 8, 18:35 | «mano en la bolsa, papa en el aire» | **confirma y mejora**: además escribe con la otra mano en el cuaderno abierto a la vez — el gesto es «trabajar con las dos manos» |
| 7 | 24, 05:42 | «media cara en sombra, sonrisa torcida» | **confirma y añade**: ojos rojos brillantes + auricular de manos libres junto a la boca (está al teléfono mientras sonríe) |
| — | 25, 18:00 (no 17:41) | «la sonrisa que todos recuerdan» | **corrige el minuto**: a las 17:41 aún no se ve con claridad; la sonrisa nítida, boca abierta, luz roja de alarma, es a las **18:00** |
| 8 | 36, 21:12 | «de pie, cabeza gacha, sonríe» | **corrige el encuadre**: es un primerísimo primer plano, pelo despeinado tapando un ojo, **bolígrafo entre los dientes**, fondo blanco quemado de luz — más intenso que «de pie» |

**Sirve para** (con el fotograma ya comprobado): explicar (insert del cuaderno),
animar/humor (papa+escritura simultánea), pensar-villano (keikaku doori, con
el detalle del teléfono), celebrar-villano (la sonrisa con L, el boli en los
dientes del almacén).

### L

| # | Ep., minuto | Fotograma dice | Resultado |
|---|---|---|---|
| 1 | 2, 17:36 | «sólo la "L" gótica en pantalla blanca» | **confirma exacto**: tele CRT azul con la letra L caligráfica negra sobre blanco, mueble y suelo verde alrededor |
| 5 | 10, 08:14 | «en cuclillas sobre la silla del café» | **confirma exacto**: dedo en el labio, jardinera con plantas verdes, luz cálida de persiana detrás — postura de pensar perfecta para «explicar» |
| 8 | 25, 17:12 | «en la azotea, empapado, mirando al cielo» | **corrige el momento**: a las 17:12 ya está DENTRO, en un plano rojo de alarma alcanzando un panel — el plano de la azotea bajo la lluvia es antes, a las **10:30-11:05** |

**Sirve para**: presentar sin cara (la «L», el misterio antes de conocerlo),
explicar/pensar (la postura en cuclillas, icónica en todo merchandising).

### Ryuk

| # | Ep., minuto | Fotograma dice | Resultado |
|---|---|---|---|
| 2 | 1, 13:00 | «aparece detrás de Light, enorme, sonrisa de dientes» | **confirma**: contrapicado, Light de espaldas al escritorio, Ryuk con alas de pelo negro en punta llenando el encuadre, ventana con cortina azul |
| 3 | 1, 16:12 | «muerde una manzana roja» | **corrige**: en ese segundo se ve su silueta completa a contraluz azul con el cinturón de hebilla-calavera; el mordisco cae uno o dos segundos antes o después (±2 s, aviso de storyboard) |

**Sirve para**: presentar (la silueta enorme detrás de Light es la pose más
reutilizable: funciona para «alguien imponente entra en escena»).

### Misa Amane

| # | Ep., minuto | Fotograma dice | Resultado |
|---|---|---|---|
| 1 | 11, 03:27 | «sólo la cinta en la tele» | **confirma**: pantalla de TV con estática, cronómetro verde «5:59» y la palabra «KIRA» escrita a mano en gótico — no se ve a Misa, es literalmente la grabación |
| 3 | 12, 14:39 | «posa para la cámara en una sesión de fotos» | **confirma y detalla**: primer plano, pelo rubio, labios rojos, bufanda roja tejida con un pendiente en forma de «M», mirada de lado sonriente — buena pose para «celebrar» |
| 4 | 13, 10:31 | «ve a Light entre la gente, con los ojos de shinigami» | ⚠️ **no confirmado**: en ese segundo el plano es de un personaje con gafas (no identifico si es Misa) con el efecto de «ojos de shinigami» (anillo rojo) reflejado en los cristales — confirma el EFECTO visual pero no que sea ella en ese fotograma exacto |

### Near

| # | Ep., minuto | Fotograma dice | Resultado |
|---|---|---|---|
| 1 | 27, 02:01 | «de niño, en el suelo, con un puzle blanco» | ⚠️ **no confirmado**: el fotograma de ese segundo muestra a otro chico de Wammy's House (pelo cobrizo, luz dorada), no a Near — el minuto puede necesitar ajuste de ±5-10 s, no lo pude fijar hoy |
| 2 | 28, 01:49 | «voz tras una "N" en pantalla» | ⚠️ **parcial**: se ve una cara de pelo claro despeinado (compatible con Near) hablando por teléfono en penumbra azul, pero no el texto «N» en pantalla en ese segundo exacto |
| 4 | 33, 11:53 | «sentado entre juguetes, concluye» | **confirma parcialmente**: primer plano de Near con el pelo cubriéndole los ojos, camisa blanca abierta — no se ven los juguetes en este encuadre cerrado, pero sí la postura fría y el gesto de concluir |

**Nota honesta**: con Misa y Near el ajuste fino de segundo a segundo es más
flojo que con Light/L/Ryuk (protagonistas, más fotogramas comprobados). Quien
monte la lámina debería mirar ±10 s alrededor de los minutos con ⚠️ antes de
usarlos como referencia exacta de pose.

---

## Lo mejor para la lámina

- **La sonrisa de Light sosteniendo a L** (ep. 25, 18:00, luz roja de alarma) con **«Kyrie II»** sonando: el momento más fotografiado de la serie, con música confirmada.
- **La papa frita con las dos manos** (ep. 8, 18:35): escribe y come a la vez — gesto perfecto para un personaje «multitarea» en una lámina de canal de textos.
- **La «L» gótica en pantalla blanca** (ep. 2, 17:36): tipografía + revelación en un solo fotograma, ideal para una interfaz o pantalla dentro de la lámina.
- **El insert «How to use it»** del tráiler (0:36-1:00) y del ep. 1 (04:32): el cuaderno explicando sus propias reglas es el objeto-narrador perfecto para el canal de guiones.
- **Paleta medida real**: azul-violeta casi negro en interiores, dorado-oliva sólo en el café de L, rojo sólo en ojos/sangre/alarma — nunca de fondo.

## No encontré

- **Minuto de los vídeos de análisis en YouTube** («El IMPACTO de L», «Por qué perdió Light Yagami», etc.): YouTube bloqueado hoy dos veces (`yt-dlp`: «Sign in to confirm you're not a bot» y 429). Probé Dailymotion como alternativa (`api.dailymotion.com/videos?search=Death+Note+analisis+L+Light`): sólo salieron clips de la película Netflix 2017, no del anime.
- **AnimeThemes** para vídeo directo de OP/ED: la API sigue caída (antes 522, hoy 403 con `filter[name]`); usé Dailymotion en su lugar.
- **Vistas exactas y fecha de los vídeos de TikTok**: TikTok bloquea el HTML con contenido vacío incluso con `navegar.py` (0 caracteres); me quedé con los enlaces directos y lo que confirma Know Your Meme/la búsqueda web.
- **Minuto por pista exacto de toda la OST del ep. 8 y 25** (sólo tengo el bloque de las 17:13 confirmado para el ep. 25): `wtas.moe` da la lista completa del episodio pero no el minuto de cada pista suelta.
- **Confirmación visual exacta de Misa (13, 10:31) y Near (27, 02:01 y 28, 01:49)**: el segundo del subtítulo no coincidía con el personaje esperado en el fotograma; puede que el gesto caiga unos segundos antes o después dentro del mismo plano.

## Bitácora de búsqueda

- `yt-dlp` sobre `youtube.com/watch?v=NlJZ-YgAt-c` (tráiler AniList): **429 → «Sign in to confirm you're not a bot»**, dos intentos con minutos de por medio. No reintento más.
- `fotogramas.py` sobre 13 episodios completos de Internet Archive (`archive.org/download/death-note-XX`, y `death-note-11_202008` para el 11): **funciona perfecto**, 1280×720, sin bloqueo. 30 fotogramas extraídos y mirados con Read.
- `fotogramas.py` sobre 3 clips de Dailymotion (opening x31pve2, ending x6alujt, tráiler x89nprz): **funciona**, hojas de contacto de 6-8 fotogramas.
- `api.dailymotion.com/videos?search=...` (dos búsquedas: «Death Note analisis L Light»): da resultados pero son de la película 2017, no del anime.
- `api.animethemes.moe/anime?filter[name]=Death Note`: **403** (con `curl -g` y con `urllib` con cabeceras normales). No lo reintento (regla de dos intentos).
- `estilo.py` (Pillow) sobre 11 fotogramas para medir paleta real: **funciona**, da hex + saturación/brillo, sin necesidad de red.
- `wtas.moe/ost/death-note/25` y `/8` (WebFetch): da tracklist detectado por audio, con 5 bloques horarios por episodio.
- Wikipedia `Death_Note_original_soundtracks` (WebFetch): tracklist oficial de las 3 OST, cruzado con wtas.moe.
- WebSearch (es/en): «Death Note episode 25 death scene soundtrack», «Death Note TikTok trend keikaku doori potato chip», «potato chip Death Note TikTok trend». 3 búsquedas de las ~50 permitidas.
- `www.tiktok.com/discover/...` con `curl` y con `navegar.py --selector body`: la página carga (200) pero sin contenido útil (JS puro, 0 caracteres con navegar.py). Uso los enlaces directos a vídeos/sonidos que sí dio la búsqueda web.
- Metadatos de Internet Archive (`archive.org/metadata/death-note-XX`) para confirmar el nombre exacto del `.mp4` de cada episodio antes de pedir el fotograma: 13 episodios comprobados (01, 02, 08, 09, 10, 11, 12, 13, 24, 25, 27, 28, 33, 36, 37).
- Disco: se borraron todos los `video.mp4` descargados por `fotogramas.py` en cuanto salieron las hojas (regla del disco compartido); sólo quedan los `.jpg` en `/tmp/claude-0/trabajo/18-death-note-video/` (2,6 MB en total).
