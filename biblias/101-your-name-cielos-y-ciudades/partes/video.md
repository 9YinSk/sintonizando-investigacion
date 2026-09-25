# Parte de VÍDEO — Your Name: cielos y ciudades (Kimi no Na wa., 2016)

Puntos de ENCARGO.md: **2** (fotogramas de escenas icónicas), **4** (luz y paleta de
sitios, medida en fotogramas), **9** (música y sonido), **10** (vídeos y tendencias
con minuto), **14** (poses analizadas con capítulo/minuto).

Nota de contexto: es una **película** (no serie de TV), dirigida por Makoto Shinkai,
CoMix Wave Films, 2016. No hay opening/ending de TV: se cubre con el tráiler oficial,
la secuencia de apertura del filme y el vídeo musical del tema clave.
`datos-video.md` venía casi vacío y con datos de otra obra (AniList emparejó mal el
id 97962, que es otra película china); no se repite esa consulta, se buscó todo de
nuevo a mano.

Vídeos mirados de verdad con `fotogramas.py` (fuente = Internet Archive, porque
YouTube pide iniciar sesión desde este servidor):
- Tráiler oficial: https://archive.org/details/YourNameKimiNoNaWaTrailer (1:25)
- Secuencia de apertura "Yume Tourou": https://archive.org/details/kimi-no-na-wa-op-1 (1:46)
- Sparkle (前前前世, MV con escenas del filme): https://archive.org/details/sparkle_201703 (6:46)

## Hallazgos

### Punto 9 · Música y sonido

- Banda sonora completa (álbum oficial), 20 pistas listadas y verificadas en
  Internet Archive · https://archive.org/details/kiminonawasoundtrack · ✅ (dos
  fuentes: listado de pistas del propio ítem + confirmado contra el tracklist de
  [Wikipedia](https://en.wikipedia.org/wiki/Your_Name)) · compositor RADWIMPS
  (Yojiro Noda y banda).
- **夢灯籠 (Yume Tourou, "Linterna de sueños")** — tema de apertura del filme,
  suena en el primer minuto y medio con la narración de Taki sobre olvidar un
  sueño · escuchada y vista en https://archive.org/details/kimi-no-na-wa-op-1 ·
  ✅ (audio del clip + título de pista nº1 del álbum) · minuto 0:00-1:46.
- **前前前世 (Zenzenzense, "Sparkle" en la versión inglesa)** — tema más
  reconocible de la película, sonando sobre el montaje de vida de Taki y
  Mitsuha y el cruce en las escaleras de Tokio · pista nº8 del álbum (4:37 de
  duración en el álbum) y MV con escenas del filme en
  https://archive.org/details/sparkle_201703 · ✅ (dos fuentes: álbum +
  descripción del ítem, que dice explícitamente "the song in Kimi no Na Wa.").
- Pistas instrumentales clave por escena (nombres en japonés, del tracklist del
  álbum, ✅ por estar en el ítem de archive.org y en Wikipedia):
  - `04 はじめての、東京` ("Primera vez en Tokio") — tema de la llegada/vida en
    la ciudad.
  - `08 前前前世` = Zenzenzense/Sparkle (ver arriba).
  - `09 御神体` ("El santuario/deidad") — tema del cráter y la escalinata del
    santuario de Itomori, escena central del giro de trama.
  - `14 消えた町` ("El pueblo que desapareció") — tema de la escena más triste,
    cuando se revela la caída del cometa sobre Itomori tres años atrás.
- Efecto de sonido reconocible: la **campanilla de viento (furin)** y el
  crujido de las tablillas de madera (ema) en las escenas del santuario;
  descrito en la ficha de la wiki del Cometa Tiamat, no medido en clip propio ·
  https://kiminonawa.fandom.com/wiki/Comet_Tiamat · ⚠️ (una fuente, no se oyó
  un clip con ese SFX aislado).
- No hay doblaje latino cantado de los openings/insert songs (son en japonés
  en todas las versiones); las frases del doblaje latino las cubre el
  investigador de voz en `partes/voz.md`.

### Punto 10 · Vídeos y tendencias, con minuto

- **Tráiler oficial** (japonés, subtítulos ingleses quemados en la copia
  archivada) · https://archive.org/details/YourNameKimiNoNaWaTrailer · 1:25 ·
  visto entero con `fotogramas.py --cada 4` (22 fotogramas) · ✅.
  - 0:00-0:20 — montaje rápido de cielo, nubes, Tokio de noche y el pueblo de
    montaña Itomori, estableciendo el contraste ciudad/campo.
  - 0:56-1:04 (`&t=60`) — interior cálido (cafetería/casa), tonos tierra y
    dorados, ritmo más lento: presentación de personajes.
  - 1:04-1:12 (`&t=68`) — plano de naturaleza verde de montaña (lago cráter de
    Itomori) bajo cielo despejado.
  - 1:16-1:24 (`&t=80`) — Taki y Mitsuha frente a frente en una escalinata al
    atardecer, luz dorada-rosada (el momento "kataware doki", el crepúsculo
    donde el mundo se difumina); es el instante más citado del filme.
- **Secuencia de apertura "Yume Tourou"** · https://archive.org/details/kimi-no-na-wa-op-1
  · 1:46 · vista entera con `fotogramas.py --cada 5` (22 fotogramas) · ✅.
  - 0:00-0:30 — narración en off de Taki ("a veces, al despertar, llorosé sin
    motivo…" - tema de olvidar un sueño), fragmentos de cielo estrellado,
    ciudad de noche y el cordón trenzado (kumihimo) rojo.
  - 0:25-0:35 (`&t=30`) — el **cometa Tiamat** cruzando un cielo nocturno
    violeta/lavanda entre estrellas, uno de los planos más repetidos en
    marketing del filme.
  - 0:35-1:46 — montaje intercalado de Tokio (trenes, cruces peatonales,
    escaleras) y Itomori (santuario, escalinata, lago), estableciendo el
    "cambio de cuerpos" antes de la trama.
- **Sparkle (MV, versión larga con escenas del filme, incluye tomas cortadas
  del montaje final)** · https://archive.org/details/sparkle_201703 · 6:46 ·
  visto entero con `fotogramas.py --cada 8` (51 fotogramas, 2 hojas) · ✅.
  - Tramo ~0:00-2:00 — vida cotidiana de Mitsuha en Itomori: casa tradicional
    de madera, el santuario en la montaña, el bus escolar, el lago cráter.
  - Tramo ~2:00-4:00 — vida cotidiana de Taki en Tokio: la ciudad vista desde
    las alturas, trenes, la cafetería donde trabaja, azoteas al atardecer.
  - Tramo ~5:00-6:00 — el cruce en las escaleras de un santuario urbano con luz
    dorada de atardecer y hojas cayendo (la escena hermana de la del tráiler en
    1:16-1:24, filmada desde otro ángulo): candidata fuerte para pose de
    "reencuentro/anhelo".
- **Trailers doblados al español (Latinoamérica/España, Selecta Visión)** en
  Dailymotion, útiles para frases y para ver el marketing hispano · ⚠️ (vistos
  los metadatos, no se procesaron con fotogramas.py: son el mismo tráiler
  internacional con voz superpuesta, no aportan planos nuevos):
  - https://www.dailymotion.com/video/x588f0a
  - https://www.dailymotion.com/video/x5br0bw
  - https://www.dailymotion.com/video/x5bl31w
- **Tendencias / redes**: la escena de la escalinata de Suga Shrine (Yotsuya,
  Shinjuku) es la más replicada en TikTok como "peregrinación" real de fans que
  visitan la ubicación · https://www.tiktok.com/discover/kimi-no-nawa-stairs-scene
  y https://www.ticketsinjapan.com/media/suga-shrine-stairs/ · ✅ (dos fuentes,
  coinciden en identificar el lugar real) · sirve como dato de "sitio real que
  inspiró el escenario" para el punto 16 (imagen).
- No encontré tráilers oficiales completos accesibles en Dailymotion sin voz
  superpuesta ni en formato distinto al de archive.org; no fue necesario
  porque el de Internet Archive es el tráiler internacional oficial completo.

### Punto 4 · Luz y paleta de los sitios (medida en fotogramas)

Medida con `herramientas/estilo.py` sobre fotogramas propios (no de memoria):

- **Cielo nocturno con el cometa** (apertura, `&t=30`) · paleta dominante
  `#F9F0F8` 21% (nube/estela), `#7A7497` 16%, `#59597E` 14%, `#4A486C` 12%,
  `#383755` 11% · sombreado mixto (cel + degradado en el cielo), saturación
  22%, brillo 67% · violeta-lavanda con toques casi blancos en la estela del
  cometa · ✅ (medido).
- **Montaña/lago de Itomori** (tráiler, `&t=68`) · paleta `#40594D` 20%,
  `#4E6757` 19%, `#334C47` 16%, `#9FAA98` 12%, `#294140` 12% · sombreado
  degradado/pintado, saturación 25%, brillo 42% · verdes apagados y algo fríos,
  propios del campo antes del atardecer · ✅ (medido).
- **Interior cálido (cafetería/casa), atardecer** (tráiler, `&t=60`) · paleta
  `#8B6648` 19%, `#40433F` 17%, `#53595C` 16%, `#887B73` 14%, `#F2E9DD` 11%,
  `#B78F6E` 9% · sombreado degradado/pintado, saturación 25%, brillo 53% ·
  tonos tierra y madera, luz interior dorada · ✅ (medido).
- **Escalinata al atardecer, "kataware doki"** (tráiler, `&t=80`) · paleta
  `#F7F7EC` 22%, `#474447` 19%, `#9B7570` 18%, `#231E21` 16%, `#EBCFB7` 10%,
  `#DEB382` 5%, `#912323` 2% · sombreado mixto, saturación 18%, brillo 61% ·
  crema casi blanco (cielo/luz), siluetas oscuras en contraluz y un acento rojo
  (`#912323`, probablemente el cordón kumihimo o una prenda): es la firma de
  color más reconocible de Shinkai para esta película · ✅ (medido).
- **Patrón general observado** (⚠️ interpretación propia sobre lo medido, no
  una cifra citable): Shinkai alterna cielos fríos violeta/azul en las escenas
  nocturnas o de suspenso con contraluces cálidos naranja-crema en los momentos
  emocionales (atardeceres, crepúsculo), y verdes apagados para el campo de
  día. Coincide con lo que describe la crítica especializada sobre su "estilo
  de luz hiperrealista" (ver `partes/texto.md` o `partes/imagen.md` para cita
  formal si la tienen).

### Punto 2 · Fotogramas de escenas icónicas (con capítulo/minuto)

(No hay "capítulos": es película única. Se da el vídeo fuente + minuto.)

1. **Cielo con el cometa Tiamat cruzando entre estrellas** · secuencia de
   apertura · https://archive.org/details/kimi-no-na-wa-op-1 · minuto 0:25-0:35
   (fotograma propio en `&t=30`) · resolución del clip: 720p (h.264) · ✅.
2. **Montaje "primera vez en Tokio" / vida en la ciudad** · tráiler · `&t=56`
   a `&t=64` · ✅.
3. **Cruce en la escalinata al atardecer (Taki y Mitsuha frente a frente)** ·
   tráiler · `&t=76` a `&t=84`, y su equivalente en Sparkle MV (tramo final,
   ~5:00-6:00) · ✅ (visto en dos vídeos distintos, mismo tipo de escena).
- Las 3 hojas de contacto completas (22, 22 y 51 fotogramas) quedan en
  `/tmp/claude-0/trabajo/101-your-name-cielos-y-ciudades-video/{trailer,apertura,sparkle}/hoja_*.jpg`
  fuera del repositorio (son pesadas); los `video.mp4` ya se borraron tras
  procesarlos.

### Punto 14 · Poses analizadas (postura, manos, mirada, gesto), por personaje

Del tráiler y del MV de Sparkle, con minuto. Los planos generales sin
personaje identificable en primer plano no se cuentan aquí (van en el punto 2).

**Mitsuha Miyamizu**
- **Sparkle, `&t=20`**: caminando por un camino rural con montañas al fondo,
  pelo negro recogido en la trenza tradicional (kumihimo), torso inclinado
  levemente hacia adelante por el paso, mirada al frente, brazos en movimiento
  natural de caminata; mochila escolar a la espalda. Sirve para **presentar el
  contexto/lugar de un personaje**. ✅ (visto).
- **Escalinata al atardecer, `&t=80` (tráiler)**: de pie frente a Taki, a dos
  escalones de distancia, mirada fija en él, postura ligeramente tensa
  (anhelo/expectativa), brazos sueltos a los lados. Sirve para **el momento de
  reencuentro/clímax emocional**. ✅ (visto).
- Compañero de esta pose: en las hojas de contacto completas se ve que
  Mitsuha suele aparecer con el torso más erguido que Taki en los planos de
  acción (ej. corriendo hacia la escalinata en el tramo final del tráiler,
  `&t=76`-`&t=84`), coherente con la descripción de "decidida" de la wiki.

**Taki Tachibana**
- **Sparkle, `&t=180` (3:00)**: de pie en una azotea o mirador urbano de
  Tokio, uniforme escolar, manos relajadas cerca del barandal, mirada hacia el
  horizonte de la ciudad; postura contemplativa, torso erguido. Sirve para
  **pensar/observar** (bueno para un canal que invite a reflexionar antes de
  publicar). ✅ (visto).
- **Interior cálido, `&t=60` (tráiler)**: sentado, torso relajado, cabeza
  ligeramente inclinada, luz cálida de atardecer entrando por una ventana;
  postura de calma/rutina (probable escena de la cafetería donde trabaja).
  Sirve para **explicar/pensar**. ✅ (visto).
- **Escalinata al atardecer, `&t=80` (tráiler)**: ver descripción conjunta con
  Mitsuha arriba; Taki aparece con el peso del cuerpo ligeramente atrás,
  postura de duda antes del reencuentro. ✅ (visto).

- No se lograron más poses de personaje en primer plano con gestos de manos
  muy detallados: los 3 clips de archive.org son material de marketing (planos
  generales de 2-4 segundos), no escenas completas del filme con
  close-ups largos. Para expresiones faciales específicas (alegría, rabia,
  miedo, vergüenza) del punto 13, y para llegar a las 6-10 poses por
  personaje que pide el punto 14, falta cruzar con las imágenes fijas de la
  wiki que ya tiene el investigador de imagen en `datos-imagen.md` (30
  imágenes grandes por personaje, ya con nombre de archivo) — no es mi punto,
  lo dejo anotado para que el redactor lo junte con lo de arriba y complete
  el rango de 6-10 fotogramas/ilustraciones por personaje.

## Lo mejor para la lámina

- El cruce en la escalinata al atardecer (`&t=80` del tráiler, tonos crema y
  contraluz con acento rojo `#912323`) es la imagen-firma de la película: luz
  dorada, dos siluetas, profundidad de escalones.
- Paleta de cielo nocturno violeta-lavanda (`#7A7497`, `#59597E`) con el
  cometa: fondo fuerte para un canal sobre "cielos y ciudades".
- El tema **Sparkle (前前前世)** y su MV son el recurso más reconocible del
  fandom hispano para relacionar sonido + imagen en la lámina.
- Verdes apagados de Itomori (`#40594D`, `#334C47`) como paleta secundaria para
  contraste campo/ciudad.
- Título de apertura "Yume Tourou" (夢灯籠) como posible motivo tipográfico o
  frase temática ("olvidar un sueño") ligada al tema de canal.

## No encontré

⚠️ No encontré tráilers oficiales sin voz superpuesta en Dailymotion (sólo
versiones dobladas); no hizo falta porque el de Internet Archive cubre lo
mismo en japonés con subtítulos.
⚠️ No encontré un clip aislado con el SFX de la campanilla/tablillas del
santuario para confirmarlo con oído propio (sólo la mención en la wiki).
⚠️ No encontré primeros planos largos de cara/manos en los 3 vídeos
procesados para completar expresiones faciales del punto 13 (no es mi punto,
pero lo anoto para el redactor/investigador de voz-personajes).
⚠️ AnimeThemes no tiene entrada para esta película (dio error 522 en
`datos-video.md` y al comprobar a mano tampoco aparece: es una web de series de
TV con OP/ED, no de películas), así que no hay `.webm` de openings ahí.
Búsquedas hechas: web (español e inglés) "Your Name trailer Dailymotion",
"Kimi no Na wa opening scene archive.org", "Your Name comet scene clip",
"staircase final scene clip"; comprobación directa de metadata de
archive.org para 3 ítems.

## Bitácora

- Búsqueda web (inglés): "Your Name Kimi no Na wa official trailer
  Dailymotion" → varios tráilers doblados en Dailymotion, ninguno en japonés
  sin doblaje.
- Búsqueda web (inglés): "Kimi no Na wa Your Name 2016 opening scene
  archive.org" → encontrado `kimi-no-na-wa-op-1`, `sparkle_201703`,
  `YourNameKimiNoNaWaTrailer`, `kiminonawasoundtrack`.
- Búsqueda web (inglés): "Your Name Kimi no Na wa comet scene clip Dailymotion
  archive.org" → confirmó `kiminonawasoundtrack` y la ficha de Comet Tiamat en
  la wiki de Fandom.
- Búsqueda web (inglés): "Your Name Kimi no Na wa staircase final scene clip
  video" → confirmó identidad del lugar real (Suga Shrine, Yotsuya) en
  ticketsinjapan.com y TikTok, sin clip de vídeo adicional nuevo.
- `curl` directo a `archive.org/metadata/<id>` para los 4 ítems usados:
  confirmó formato, duración y tracklist sin gastar búsqueda web.
- `fotogramas.py` sobre los 3 vídeos (tráiler, apertura, Sparkle): 3 hojas de
  contacto completas miradas con Read, más 4 fotogramas individuales grandes
  para medir color con `estilo.py`.
- No se usó el buscador web más de 4 veces (queda margen amplio del cupo de
  ~50 para otro repaso si hace falta).

## Cumplimiento de mis puntos (2, 4, 9, 10, 14)

| Punto | Estado | Por qué |
|---|---|---|
| 2 · Fotogramas de escenas icónicas | ✅ | 3 escenas (cometa, ciudad/campo, escalinata) con vídeo fuente, minuto y `&t=`; hojas completas guardadas fuera del repo |
| 4 · Luz y paleta medida | ✅ | 4 paletas hex medidas con `estilo.py` sobre fotogramas propios, con fuente exacta de cada una |
| 9 · Música y sonido | ✅ | BSO completa (20 pistas) verificada en dos fuentes, tema clave (Sparkle/Zenzenzense) identificado y visto en su MV; SFX del santuario sólo con una fuente (⚠️) |
| 10 · Vídeos y tendencias, con minuto | ✅ | Tráiler, apertura y MV vistos enteros con minuto exacto; tendencia de peregrinación a la escalinata real con dos fuentes |
| 14 · Poses analizadas | ⚠️ | 5 poses (2 Mitsuha, 3 Taki) con minuto y gesto descrito desde lo visto en vídeo; el punto pide 6-10 por personaje y los 3 clips de marketing disponibles no dan más primeros planos — para completar el rango hace falta cruzar con las imágenes fijas de `datos-imagen.md`, ya anotado para el redactor |
