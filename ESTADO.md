# ESTADO — dónde va el trabajo y cómo seguir en otro contenedor

Actualizado: 25-09-2026, 02:43 UTC. Rama: **`claude/peaceful-maxwell-fklpkp`**
(`main` todavía no tiene este trabajo).

<!-- lotes -->
## Cómo va por lotes (25-09-2026, 02:43 UTC)

Lo copia la central de `lotes/*.md` con `herramientas/juntar.sh --marcar`. `revisar.py` da por **COMPLETAS 26** biblias: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 19, 20, 21, 22, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 77, 78.

### Lote A (la central): 02-05 y 31-36

*Estado (02:22 UTC del 25, tercera cuenta): LOTE A TERMINADO*

Sigue la sesión https://claude.ai/code/session_01RJL7rbu6HGiYoChtxomcbb · rama `claude/lote-a-series-inxhbf`.

- 02 Attack on Titan: **COMPLETA** y subida (20:52). ✅33 ⚠️6 ❌0, 218 referencias, 113 webs.
- 03 Solo Leveling: **COMPLETA** y subida (01:17). ✅32 ⚠️5 ❌0, 148 referencias, 111 webs, 1760 líneas.
- 04 Harry Potter: **COMPLETA** y subida (22:5x). ✅36 ⚠️3 ❌0, 100 referencias, 144 webs, 2943 líneas.
- 05 Oshi no Ko: **COMPLETA** y subida (23:1x). ✅31 ⚠️6 ❌0, 129 referencias, 108 webs, 3256 líneas.
- 31 Demon Slayer: **COMPLETA** y subida (23:2x). ✅30 ⚠️7 ❌0, 252 referencias, 84 webs, 2544 líneas.
- 32 Jujutsu Kaisen: **COMPLETA** y subida (01:1x). ✅31 ⚠️3 ❌0, 52 referencias, 97 webs, 2772 líneas.
- 33 Frieren: **COMPLETA** y subida (02:16). ✅30 ⚠️7 ❌0, 163 referencias, 89 webs, 2647 líneas.
- 34 Haikyuu: **COMPLETA** y subida (02:17). ✅32 ⚠️9 ❌0, 175 referencias, 83 webs, 2938 líneas.
- 35 One Punch Man: COMPLETA.
- 36 Hunter x Hunter (nueva): **COMPLETA** y subida (02:22). ✅20 ⚠️10 ❌0, 183 referencias, 51 webs, 1615 líneas.

Ojo: dos cuentas trabajaron el lote A a la vez (`cool-keller` relanzada a la 01:11 y
`optimistic-dirac` desde las 22:43) y rehicieron 03, 04, 05 y 31. Al juntar se quedó
03 de `cool-keller` (✅32 ⚠️5, una ⚠️ menos) y 04, 05 y 31 de `optimistic-dirac` (las
subidas como COMPLETAS; las de `cool-keller` eran guardados a medias).

### Lote B: 06-18 (repasos)

*Estado*

- 06-09: ya COMPLETAS (sesiones anteriores).
- 10 K-On: **COMPLETA** y subida (02:4x). ✅19 ⚠️11 ❌0, 134 referencias, 106 webs, 2443 líneas.
- 11 Chainsaw Man: partes listas; redactor (Opus, repaso) en marcha.
- 12 Kakegurui: 4 investigadores (Sonnet, repaso) en marcha.
- 12-18: pendientes (12 y 13 ya recolectadas; 14-18 recolectando).

### Lote C: repasos 19-30

*Estado (02:50 UTC del 25)*

Desde las 02:45 lo lleva la central: sesión https://claude.ai/code/session_01RJL7rbu6HGiYoChtxomcbb
· rama `claude/lote-a-series-inxhbf` (la cuenta anterior paró a las 22:59 del 24).

- 23 Lilo & Stitch: imagen, vídeo y texto listos; voz relanzada (tanda corta: caras de
  miedo, vergüenza y rabia del punto 13); luego su redactor.
- 24 Assassination Classroom: 4 investigadores (Sonnet) en marcha desde las 02:45.
- 25-30: datos recolectados; faltan sus equipos.

**Si esta cuenta se corta (iba al 90 % del límite a las 02:43):** la siguiente cuenta del
lote C sigue así: `herramientas/juntar.sh`, `echo C > .lote` y `siguiente.py 5 --lote C`.
- 23: si `partes/voz.md` aún acaba en «## Sigue:», no la relances otra vez (ya lleva 2
  tandas): lanza directamente su redactor en modo `repaso` y que marque ⚠️ lo que falte.
- 24: sus 4 investigadores empezaron a las 02:42; relanza sólo los roles cuya parte
  falte o acabe en «Sigue:» (desde donde quedó).
- **19 Doraemon: COMPLETA y subida.** 2434 líneas, ✅27 ⚠️12 ❌0, 243 referencias,
  124 webs, 134 minutos citados, 79 hex, 3 hojas.
- **20 Dr. Stone: COMPLETA y subida.** 2498 líneas, ✅27 ⚠️11 ❌0, 183 referencias,
  92 webs, 166 minutos citados, 87 hex, 3 hojas.
- **21 Spider-Verse: COMPLETA y subida.** 2584 líneas, ✅28 ⚠️11 ❌0,
  197 referencias, 137 webs, 134 minutos citados, 55 hex, 3 hojas.
- **22 Violet Evergarden: COMPLETA y subida.** 2396 líneas, ✅24 ⚠️8 ❌0,
  168 referencias, 116 webs, 270 minutos citados, 34 hex, 3 hojas.
- Datos recolectados (gratis) para 19-30 (lote C entero).

### Lote D: series nuevas 37-56

*Estado*

- 37 Fullmetal Alchemist: Brotherhood: **COMPLETA** (22:12). ✅16 ⚠️15 ❌0, 189 refs, 52 webs.
- 38 Sailor Moon: **COMPLETA** (22:47). ✅23 ⚠️9 ❌0, 191 refs, 54 webs.
- 39 Saint Seiya: **COMPLETA** (23:31). ✅24 ⚠️8 ❌0, 223 refs, 45 webs.
- 40 Digimon Adventure: **COMPLETA** (00:03). ✅22 ⚠️10 ❌0, 159 refs, 48 webs.
- 41 Dandadan: imagen, texto y video completos; voz en marcha.
- 42 Blue Lock: imagen y texto en marcha. 43-47: recolectados por adelantado.

### Lote E: series nuevas 57-76

*Estado*

- Arranque (24-sep-2026, 21:30 UTC): herramientas instaladas; guardar.sh cada 300 s; recolectando datos de 58-62.
- 57 Coco: 4 investigadores completos; redactor (Opus) en marcha desde 22:05 UTC.
- 58 Encanto: 4 investigadores (Sonnet) en marcha desde 22:05 UTC.

### Lote F: series nuevas 77-96

*Estado*

- Arranque (24-sep-2026, 21:45 UTC): herramientas instaladas; guardar.sh cada 300 s; comprobación cada hora.
- 77 Wistoria: **COMPLETA y subida** (22:27 UTC). ✅20 ⚠️18 ❌0, 134 referencias, 56 webs, 1655 líneas.
- 78 Vinland Saga: **COMPLETA y subida** (22:52 UTC). ✅23 ⚠️7 ❌0, 162 referencias, 65 webs, 2031 líneas.
- **Corte por límite de sesión** (23:06-23:50 UTC, `rate_limit`, «resets 11:20pm UTC»): 5 agentes vivos murieron a mitad de tanda (79 redactor, 80 video, 81 imagen/video/voz). Nada se perdió del todo: guardar.sh había subido lo hecho hasta el corte. Relanzo los 5 desde donde quedaron en cuanto pase el reinicio.
- 79 Demon Slayer: redactor cortado justo tras «Tres conceptos de lámina» — faltan tabla de cumplimiento, bitácora y referencias.json. Relanzado 23:50 UTC.
- 80 Solo Leveling: vídeo cortado con un `Sigue:` legítimo ya escrito (fotograma del Rey Hormiga). Relanzado como relanzamiento corto.
- 81 Mushoku Tensei: imagen cortado justo después de escribir imagen.md (dice «Parte terminada») pero SIN escribir imagen.json ni hojas/ — relanzado sólo para eso. Vídeo y voz no llegaron a escribir nada: relanzados desde cero.
<!-- /lotes -->

## Cuándo una biblia está completa

`python3 herramientas/revisar.py` lo dice para cada biblia. Está **COMPLETA**
cuando tiene:

- la tabla «Cumplimiento del encargo» (los 25 puntos, 3 conceptos, 40 fuentes,
  tipos de fuente, hojas y referencias) **sin ningún ❌**;
- 20 entradas o más en `referencias.json` y 3 hojas en `hojas/`;
- si es una de las 01-30, la sección «Segunda pasada · qué cambió».

Los ⚠️ no la dejan incompleta: marcan datos con una sola fuente o cosas que
hay que ver u oír en persona (frases del doblaje, vídeos que YouTube no deja
bajar desde el servidor). Siempre quedarán algunos.

## Cómo va (17:33 UTC)

- **Casi completas (9):** 01, 02, 03, 04, 05, 31, 32, 33, 34. Tienen tabla sin
  ❌, hojas y referencias, pero **les faltan los puntos 18-25** (se añadieron al
  encargo hoy a las 17:10). `revisar.py` ya los exige. (El ❌ de 31 era falso:
  el revisor contaba un ❌ escrito dentro del «por qué».)
- **Hechas con reglas viejas, necesitan repaso (24):**
  - 06-25: red cerrada. Sin hojas, sin tabla, muchos ⚠️.
  - 26-30: red abierta, pero antes de las reglas de mirar vídeos y de la tabla.
- **A medias:** 35 One Punch Man (≈670 líneas, sin referencias) y 36 Hunter x
  Hunter (esqueleto).
- **Nuevas pendientes:** de la 37 a la 131 (tandas S10-S33).
- **Temas (A1-P1):** 0 de 96.

## Parado (20:40 UTC): el dueño reparte el trabajo por cuentas (REPARTO.md)

- **Hechas y subidas con las reglas nuevas:** One Piece (01) y One Punch Man (35).
- **Attack on Titan (02, lote A):** investigadores terminados (imagen, voz, texto,
  sin `Sigue:`). El **redactor en Opus se paró a medias** (iba por el punto 18):
  relanzarlo con el mensaje del paso 5 de la skill en modo repaso-corto; sigue
  desde lo que ya haya en `biblia.md`.
- **Solo Leveling (03, lote A):** 3 investigadores del repaso corto parados a
  medias tras unos 10 minutos; sus partes están guardadas. Relanzarlos («si tu
  parte ya existe, sigue desde donde quedó») y luego su redactor.
- Datos ya recolectados: 04, 05, 31, 32 (y 13).

## Mejoras hechas (19:20 UTC), pedidas por el dueño: más rápido sin perder calidad

1. **En cadena** (skill): el redactor de una serie y los investigadores de la
   siguiente trabajan a la vez; `recolectar.py` corre por adelantado para las 5
   siguientes. Objetivo: una serie cada 35-40 minutos.
2. **Una tanda por investigador** (hasta ~100 acciones): antes de terminar
   repasa sus puntos; `Sigue:` sólo para lo obligatorio que falte. Los extras,
   ⚠️ en «No encontré».
3. **`herramientas/episodio.py`**: un capítulo entero en una ficha de texto
   (planos, lo que se dice y lo que se lee, minuto a minuto). 2-3 capítulos
   clave por serie.
4. **`revisar.py` mide lo que pidió el dueño**: 40 webs enlazadas, 15 minutos,
   10 hex, bitácora y conceptos, además de los 25 puntos. Ojo: 31, 32, 33 y 34
   enlazan sólo 31-38 webs; en su repaso corto hay que completarlas.
5. **`PETICIONES.md`**: todo lo que pidió el dueño, tal como lo pidió, y dónde
   se vigila. Lo lee el redactor.

## El sistema (18:45 UTC)

Tras el piloto caro (8 investigadores, 25 minutos, unos 65 dólares, ninguno
terminó), el trabajo va con el **método económico** de `EQUIPO.md` y la skill
`serie-en-equipo`, que funciona sola: `siguiente.py` elige la serie,
`recolectar.py` junta gratis los datos (13 fuentes), 4 investigadores en Sonnet
parten de esos datos y leen sólo su parte de la biblia (`seccion.py`), un
redactor en Opus escribe, `revisar.py` exige los 25 puntos y `subir.sh` sube.

Parados a medias (guardado, sin marcar): repaso 06-spy-x-family, 35-one-punch-man
(≈450 líneas) y 36-hunter-x-hunter (esqueleto). Rehacerlos con el equipo.

**Herramientas nuevas** (tabla «Herramientas por tarea» de `AYUDANTE.md`):
`voz.py` (transcripción Whisper con minuto y ficha de voz), `estilo.py`
(paleta medida, sombreado, línea y etiquetas de anime WD14),
`fotogramas.py --cortes` (un fotograma por plano) y `tesseract` para leer texto.
Instalar: `pip install -U "yt-dlp[default]" Pillow fontTools requests faster-whisper "scenedetect[opencv-headless]" praat-parselmouth onnxruntime`
y `apt-get install -y ffmpeg tesseract-ocr tesseract-ocr-jpn tesseract-ocr-spa`.

## Cómo seguir en un contenedor nuevo

Desde ahora cada serie la hace **un equipo** (ver `EQUIPO.md`): 4
investigadores en paralelo (imagen, vídeo, voz y personajes, texto y juegos),
cada uno en su archivo de `partes/`, y **un redactor** que es el único que
escribe la biblia. La sesión principal revisa con `revisar.py` y sube. Los
pasos exactos están en la skill `.claude/skills/serie-en-equipo/SKILL.md`.

Pega esto en una sesión nueva en la nube, con este repositorio:

> Trae la rama `claude/peaceful-maxwell-fklpkp` (`git fetch origin claude/peaceful-maxwell-fklpkp && git checkout -B <tu rama> FETCH_HEAD`), lee `ESTADO.md` y sigue con la skill serie-en-equipo.

Orden de trabajo (`python3 herramientas/siguiente.py` lo calcula):
1. One Piece hasta COMPLETA, con el método económico.
2. Puntos 18-25 de las casi completas (02, 03, 04, 05, 31, 32, 33, 34): repaso
   corto con el equipo de 4 (cada investigador sólo sus puntos 18-25).
3. 35 y 36 con el equipo; el redactor aprovecha lo que ya haya en `biblia.md`.
4. Repasos 06-30 y tandas S10 en adelante: con 4 investigadores, como mucho 2
   series a la vez; con 8, una sola.

`subir.sh` no sube una biblia que `revisar.py` no dé por COMPLETA (salvo
`FORZAR=1`).

## Avisos

- Decisiones del dueño, cosas que oír en persona y sugerencias: `DECISIONES.md`.

- YouTube pide «iniciar sesión» a ratos (IP de servidor). Plan B: el mismo
  clip en Dailymotion o Internet Archive. Plan C: miniaturas de vista previa
  (±2 s). Si el dueño añade la variable de entorno `YT_COOKIES` (cookies.txt de
  una cuenta de Google **secundaria**), `fotogramas.py` y `voz.py` ya la usan
  con `--cookies`.
- Crunchyroll no se puede usar (403 desde el servidor y DRM).
