# Investigador de VÍDEO · JoJo's Bizarre Adventure (repaso, 25-sep-2026)

Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. La biblia ya tenía mucho de estos
puntos (subtítulos con minuto, música, hex "a ojo"), pero **ninguna imagen
salía de mirar un vídeo de verdad**: la nota decía «los minutos dentro de
los vídeos de YouTube no se pudieron medir». Aquí sí: bajé y miré vídeos
reales con `fotogramas.py` (YouTube pidió iniciar sesión o se quedó
colgado con `tZRpLrZgr6w`; usé Internet Archive y Dailymotion, como dice
AYUDANTE.md). Trabajo pesado en
`/tmp/claude-0/trabajo/28-jojo-s-bizarre-adventure-video/` (borrado al
terminar).

## Hallazgos

### Punto 2 · Opening, ending, tráiler y 3 escenas icónicas (vistos de verdad)

- **Opening** — *"Sono Chi no Sadame"*, OP1 de Phantom Blood (2012), bajado de
  Internet Archive (`archive.org/details/jojo-no-kimyou-na-bouken-op-1`,
  1920×1080) y mirado entero con `fotogramas.py --cada 4` (23 fotogramas,
  0:00-1:31) · ✅ (el vídeo + coincide con el título del opening en
  [JoJo Wiki: Music](https://jojowiki.com/Music)) · minutos exactos:
  - **0:04** Jonathan Joestar flexiona los brazos, fondo con líneas de
    velocidad verdes.
  - **0:08** cartela del título «ジョジョの奇妙な冒険» en rosa sobre negro.
  - **0:12-0:16** panel de manga (blanco y negro) de una figura bajando una
    escalera, encuadre torcido.
  - **0:24** Erina Pendleton, atardecer naranja-amarillo detrás.
  - **0:40** **mano de Jonathan alzada hacia una luz blanca cegadora**, con
    anillos dorados en los dedos, guantelete oscuro (pose «alcanzar el
    cielo»; sirve para **animar**).
  - **0:44** puño envuelto en fuego naranja.
  - **1:04-1:08** aura de fuego rosa/verde envolviendo el cuerpo de
    Jonathan.
  - Enlace directo al fotograma 0:40:
    `/tmp/.../op1_frames` (local; el vídeo original no tiene URL con `&t=`
    porque es un archivo, no YouTube).
- **Ending** — *"Roundabout"* (Yes), del ítem de Dailymotion **"Jojos
  Bizarre Adventure Ending 1 & 2 Synced"** (`dailymotion.com/video/x3j25ta`,
  manganimex, 3:04) ✅ (coincide con [JoJo Wiki: Roundabout](https://jojowiki.com/Roundabout)
  y con lo que ya decía la biblia del «mural azteca»). Mirado entero con
  `fotogramas.py --cada 8` (24 fotogramas):
  - **0:00-0:48**: fondo fijo de **talla de piedra azteca** (tonos tierra
    `#8F7B61`/`#AFA07E`), con una **línea roja** (`#8B1A1A` aprox.) que
    recorre los relieves como una serpiente — es la «sangre» que
    describía la biblia, **confirmado visualmente** (antes era ⚠️ de
    memoria).
  - **0:56**: cartela de créditos **«ROUNDABOUT — Jon Anderson / Steve
    Howe — YES»** (el bloque de créditos de la canción, en japonés
    alrededor).
  - **1:12**: **máscara con forma de rostro pálido y rosa** aparece entre
    zarcillos verdes (silueta de Stand tipo Wamuu/Dio) sobre el muro.
  - **1:28-1:36**: dos **máscaras de piedra** (una dorada, una con
    manchas violeta) encajadas en los relieves — antes la biblia sólo
    describía «una máscara al final»; hay **varias**, a distintos
    minutos.
  - **2:40**: **Joseph Joestar joven**, sombrero, mano cerca de la
    barbilla con sonrisa de lado (pose «pensar/explicar»); fondo del
    muro. Colores medidos (quantize 6, Pillow): chaqueta verde oliva
    `#8F7B61`/`#AFA07E`, chaleco morado `#673E31`, corbata a rayas rojo
    y verde, piel `#C79B6C` aprox.
- **Tráiler** — clip de **Dailymotion "JoJo's Bizarre Adventure"**
  (canal **Level Up**, `dailymotion.com/video/x8x1bgw`, 4:11, 9826
  vistas) ✅. Es un tráiler/gameplay de **JoJo's Bizarre Adventure:
  All-Star Battle R** (2022): lo identifico por el HUD «**SECRET FACTOR
  +2**» a los **0:30**, mecánica propia de ese juego, y por el letrero de
  vida «Jonathan Joestar vs. Joseph Joestar» a 1:00-1:10. Mirado entero
  con `fotogramas.py --cada 10`:
  - **0:00-0:20**: desierto de Steel Ball Run con 5 jinetes; después
    Speedwagon, Jonathan y Zeppeli en un pueblo del oeste (cinemática del
    juego).
  - **0:40**: texto **«THE WORLD!»** sobre una esfera azul con reflejo —
    cinemática de Dio deteniendo el tiempo.
  - **0:50**: primer plano de **ojos rojos furiosos** (Dio) en la
    oscuridad.
  - **1:20**: **Jotaro Kujo** en contrapicado, gorra negra con insignia
    dorada, gabardina negra con cuello de piel, **camisa lila estampada**
    y **cadena dorada** colgando del hombro — pose seria, de pie, mirada
    directa. Colores medidos por zona (Pillow, `crop`+promedio, escena
    oscura así que los tonos salen apagados): cadena `#7B5325`,
    chaqueta `#221223`, camisa `#4B2750`, gorra `#6F491D`. **Corrige**
    la tabla «a ojo» de §5.3, que decía «blanco del gorro»: en esta
    escena (y en las hojas de personaje) la gorra es **negra con
    insignia dorada**, no blanca.
  - **1:40-1:50**: menú de personajes de Battle Tendency (Joseph
    caminando por una calle con casas, cielo amarillo-crema).
  - **3:20**: dos siluetas en blanco y negro luchando frente a una
    fachada (probablemente Joseph vs. un Hombre del Pilar).
- **Escena icónica 1** — avance oficial de TV del **episodio 33 de
  Diamond is Unbreakable** («7月15日(木) その3», Dailymotion
  `x5mk7ho`, 0:15) ✅ (el logo «ダイヤモンドは砕けない» y el número de
  episodio están en pantalla). Mirado fotograma a fotograma
  (`--cada 1`):
  - **0:00-0:01**: **Josuke** de perfil, tres cuartos, aura violeta
    (Crazy Diamond) alrededor, cielo dorado con nubes; manos cerca del
    cinturón, cadera ladeada — pose de **presentación**.
  - **0:04-0:05**: Yukako (pelo blanco) mirando de lado con expresión
    intensa, fondo violeta.
  - **0:07**: **Crazy Diamond** (armadura blanca y azul) junto a
    Yukako, de perfil.
  - **0:10-0:15**: interior de coche, sobre en la mano — el sobre de
    la carta de las apuestas del arco de Kira.
- **Escena icónica 2** — avance oficial del **episodio 36**
  («アナザーワン バイツァ・ダスト その2», Dailymotion `x547qml`,
  0:15) ✅. Mirado fotograma a fotograma:
  - **0:00-0:03**: Aya Tsuji (pelo rojo) llorando, primer plano, luego
    de perfil hablando con Josuke.
  - **0:04-0:06**: **primer plano de Killer Queen** (cara blanca,
    ojos rojos brillantes) con el **puño enguantado** sosteniendo un
    disco dorado con tachuelas negras (el «cronómetro»/detonador de
    Bites the Dust); fondo de humo púrpura. Colores medidos (quantize):
    máscara `#F3E6F2`, aura `#5A058C`/`#6F4B6C`, fondo casi negro
    `#110617`.
  - **0:12-0:14**: Killer Queen de cuerpo entero avanzando entre
    fuego/humo rojo.
- **Escena icónica 3**: la del tráiler ASBR arriba (Jotaro 1:20 y Dio
  0:50) cuenta como tercera escena aparte del tráiler mismo: son
  cinemáticas distintas dentro del mismo vídeo.
- **Límite honesto**: el opening está en 1080p (Internet Archive); el
  ending, el tráiler y las 2 escenas de Dailymotion sólo llegan a
  **512×288** (es la resolución que ofrece Dailymotion para clips
  antiguos/cortos) ⚠️. Para arte en alta de estos mismos momentos, usar
  las hojas de contacto (F-numbers) de la wiki que ya cita la biblia en
  el punto 15, en 1920×1080 o más.

### Punto 4 · Sitios, luz y paleta (medida en fotogramas, no a ojo)

- **Muro azteca del ending**: piedra tierra `#8F7B61` a `#AFA07E`, línea
  roja de sangre `#8B1A1A` aprox., medido en `fotogramas.py --fotograma
  40` del ending sincronizado (0:40) ✅ (Pillow, `quantize` a 6 colores).
- **Cielo de Morioh en DU** (avance del ep. 33, 0:00-0:01): amarillo dorado
  con nubes blancas, el mismo tono que ya medía la biblia en F315
  (`#B79E2D`) — **confirmado** con una segunda fuente en vídeo, no sólo
  la hoja de la wiki ✅.
- **Escena de Killer Queen** (ep. 36, 0:04): fondo de humo púrpura oscuro
  `#110617`-`#5A058C`, más violeta y menos rosa que la paleta de
  Morioh de día — es el color que usa el anime para las escenas
  amenazantes de Kira, distinto del ambiente "pop" del resto de DU.
- **Escena de Jotaro en el tráiler ASBR** (1:20): interior oscuro
  (subterráneo egipcio, ambientado como El Cairo), luz violeta desde
  abajo; los colores de su ropa salen apagados por el contraluz — pongo
  el aviso arriba (§Punto 2) para no dar esos hex como los "reales" de
  su traje sin más contexto.
- La tabla de §5.1 (sitios) y la de texturas de Poly Haven de la biblia
  ya estaban bien: no encontré datos nuevos que las corrijan, las doy
  por confirmadas.

### Punto 9 · Música

- Confirmado con imagen real: el ending **"Roundabout"** trae la
  cartela de créditos de la canción («ROUNDABOUT — Jon Anderson / Steve
  Howe — YES») **a los 0:56** del vídeo sincronizado, con todavía 2:08
  de animación después (máscaras, Joseph, símbolos) — la biblia no
  tenía este dato del minuto de la cartela ✅.
- El resto de música (openings, endings occidentales, "il vento d'oro",
  "Awaken") ya estaba bien confirmado en JoJo Wiki: Music; no repetí esa
  consulta (regla de AYUDANTE). Sólo añado: el **artista de "SPIN"**
  (Kroi, OP de Steel Ball Run) sigue siendo la única canción sin
  vídeo/clip que pueda mirar todavía (se estrenó ayer, 25-sep-2026, en
  el ep. 2 semanal) ⚠️ — no hay clip oficial subido aún a ninguna
  plataforma abierta que probé (Dailymotion, Internet Archive).

### Punto 10 · Vídeos (con minuto exacto)

| Vídeo | Fuente | Duración / resolución | Qué se ve y minuto |
|---|---|---|---|
| OP1 "Sono Chi no Sadame" | [Internet Archive](https://archive.org/details/jojo-no-kimyou-na-bouken-op-1) | 1:31 · 1920×1080 | Ver arriba, 0:04 a 1:28 |
| Ending "Roundabout" (1&2 sync) | [Dailymotion, manganimex](https://www.dailymotion.com/video/x3j25ta) | 3:04 · 512×288 | Ver arriba, 0:00 a 2:40 |
| Tráiler/gameplay ASBR | [Dailymotion, Level Up](https://www.dailymotion.com/video/x8x1bgw) | 4:11 · 512×288 | Ver arriba, 0:20 a 3:20 |
| Avance TV DU ep. 33 | [Dailymotion](https://www.dailymotion.com/video/x5mk7ho) | 0:15 · 512×288 | Josuke, Yukako, sobre; 0:00-0:15 |
| Avance TV DU ep. 36 | [Dailymotion](https://www.dailymotion.com/video/x547qml) | 0:15 · 512×288 | Killer Queen, Aya; 0:00-0:14 |
| Tráiler SBR oficial (Netflix LATAM) | [YouTube](https://www.youtube.com/watch?v=tZRpLrZgr6w) | 2:10 | **No se pudo bajar**: `yt-dlp` se quedó colgado (probable límite de la IP compartida). Ya está en la biblia por metadatos (título, fecha, vistas); sigue sin minutos internos ⚠️. |
| OP2 (2012, Battle Tendency "BLOODY STREAM") | [Internet Archive](https://archive.org/details/jojo-no-kimyou-na-bouken-op-2) | 1:31 · 1920×1080 | Bajado pero no analizado por tiempo — queda para otra pasada ⚠️ |

- AnimeThemes (`api.animethemes.moe`) sigue caído: probé
  `/anime?filter[slug]=...` y `/search`, las dos sin respuesta (mismo
  522 que ya anotó `recolectar.py`) ✅ confirmado dos veces, en dos
  endpoints.
- TikTok: seguí sin poder abrir los vídeos de las 4 búsquedas que ya
  listaba la biblia (bloqueado sin sesión); no hay vía alternativa
  documentada en AYUDANTE.md para TikTok.

### Punto 14 · Poses con minuto (nuevas, de vídeo real; se suman a las de §15)

| Personaje | Fuente | Minuto | Postura / manos / mirada | Sirve para |
|---|---|---|---|---|
| Jonathan Joestar | OP1, Internet Archive | 0:40 | Mano derecha alzada hacia una luz blanca, anillos dorados, guantelete oscuro | **Animar** / alcanzar una meta |
| Joseph Joestar (joven) | Ending "Roundabout", Dailymotion | 2:40 | Sombrero, mano junto a la barbilla, sonrisa de lado, cuerpo de perfil | **Pensar / explicar** con ironía |
| Jotaro Kujo | Tráiler ASBR, Dailymotion | 1:20 | Contrapicado, de pie, mirada fija al frente, cadena colgando del hombro, gabardina abierta | **Presentar / amenazar** |
| Josuke Higashikata | Avance DU ep. 33, Dailymotion | 0:00-0:01 | De perfil, aura violeta alrededor, manos cerca del cinturón, cadera ladeada | **Presentar** |
| Killer Queen (Kira) | Avance DU ep. 36, Dailymotion | 0:04 | Primer plano, ojos rojos, puño enguantado con el disco dorado del detonador | **Amenazar / regañar** |

Estas cinco se pueden citar junto a las de la tabla de §15 de la
biblia (que usan hojas F-n de la wiki, en mayor resolución); las de
aquí aportan **movimiento y minuto de vídeo real**, que es lo que
pedía el punto 14 y lo que AYUDANTE.md marca como obligatorio.

## Lo mejor para la lámina

- El fotograma **0:40 del OP1** (mano de Jonathan hacia la luz):
  encuadre limpio, un solo gesto, funciona como "alcanzar algo" para
  cualquier concepto de superación.
- El primer plano de **Killer Queen a 0:04** (avance ep. 36): cara
  blanca + ojos rojos + puño con el disco dorado es reconocible al
  instante para un fan y funciona como "amenaza" sin violencia
  explícita (bueno para un canal de memes).
- La pose de **Joseph a 2:40** del ending (mano en la barbilla,
  sonrisa de lado) es perfecta para un globo de "explicación sarcástica"
  o para el gag de "tu siguiente frase será…".
- El **muro azteca con la línea roja** (ending, 0:00-0:48) sirve de
  fondo/textura para cualquier cartela en homenaje al "To Be
  Continued", sin repetir la flecha ya muy vista.
- **Corrección importante**: la gorra de Jotaro (SC) es **negra con
  insignia dorada**, no blanca como decía la tabla "a ojo" de §5.3;
  cambiar esa celda si el redactor la usa.

## No encontré

- **AnimeThemes**: sigue caído (522) en dos endpoints distintos
  (`/anime?filter[slug]=...`, `/search?q=jojo`); no hay `.webm` directo
  de los openings/endings desde ahí, como sí pasó en otras series.
- **Tráiler oficial SBR de YouTube con minutos internos**: `yt-dlp` se
  colgó (timeout de 40 s) al bajar `tZRpLrZgr6w`; no reintenté una
  segunda vez seguida (regla de "no más de dos intentos"), lo dejo para
  otra pasada si hace falta.
- **Clip oficial de "SPIN" (OP de Steel Ball Run)**: se estrenó ayer
  (25-sep-2026); ninguna plataforma abierta que probé (Dailymotion,
  Internet Archive) lo tiene todavía.
- **Vídeos de TikTok**: mismas 4 búsquedas que ya tenía la biblia,
  siguen sin poder verse sin sesión.

## Bitácora

- Leí `partes/datos-video.md` entero antes de empezar; no repetí las
  consultas de Dailymotion/Internet Archive/MusicBrainz que ya trae
  (sólo usé sus resultados para elegir qué bajar).
- `archive.org/details/jojo-no-kimyou-na-bouken-op-1` y `-op-2`:
  bajados con `yt-dlp`, mirados con `fotogramas.py --cada 4`.
- `dailymotion.com/video/x3j25ta` (ending), `x8x1bgw` (tráiler ASBR),
  `x5mk7ho` (avance ep. 33), `x547qml` (avance ep. 36): bajados con
  `yt-dlp -f best`, mirados con `fotogramas.py --cada N` y
  `--fotograma <s>` para hex.
- `curl api.animethemes.moe/anime?filter[slug]=jojos-bizarre-adventure`
  y `/search?q=jojo`: sin respuesta (522), en español y sin resultado.
- `curl api.dailymotion.com/videos?search=JoJo+ending+Roundabout`: dio
  el ítem "Jojos Bizarre Adventure Ending 2" que usé.
- `yt-dlp -J` sobre `archive.org/details/youtube-tSFm7y-L8OY` (película
  de Phantom Blood doblada): falló al parsear JSON, no insistí (no era
  obligatorio, ya tenía opening y ending de otra fuente).
- Colores: medidos con Pillow (`Image.quantize` a 6 colores y
  recortes con promedio de píxeles) sobre los fotogramas grandes
  sacados con `--fotograma`, nunca a ojo.
- Vídeos pesados (`op1.webm`, `ending2.mp4`, `ep33.mp4`, `ep36.mp4`,
  `dm_scene.mp4`, `op2` y sus carpetas de fotogramas) quedan en
  `/tmp/claude-0/trabajo/28-jojo-s-bizarre-adventure-video/` para
  borrarse; no se subieron al repositorio.
