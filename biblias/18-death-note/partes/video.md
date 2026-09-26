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

