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

