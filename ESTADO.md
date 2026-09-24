# ESTADO — dónde va el trabajo y cómo seguir en otro contenedor

Actualizado: 2026-09-24, 17:33 UTC. Rama: **`claude/peaceful-maxwell-fklpkp`**
(`main` todavía no tiene este trabajo).

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

## En marcha (17:33 UTC, cuenta nueva)

**Piloto del equipo de 8 con One Piece (01)**, lanzado a las 17:15 UTC. Cada
investigador escribe en `biblias/01-one-piece/partes/<rol>.md` y `.json`
(roles en `EQUIPO.md`, «Equipo de 8»): arte, fanart-3d, escenas,
musica-videos, doblaje, personajes, dialogos, tecnica-mundo. Si se cortó:
relanzar cada rol con el mensaje de la skill `serie-en-equipo` («si tu parte ya
existe, sigue desde donde quedó») y, cuando estén los 8, el redactor, que
**edita la biblia que ya hay** y añade los puntos 18-25.
Medir: hora de inicio y fin de cada uno, para saber cuánto tarda el equipo.
Se paró a las 17:30 UTC (límite de la cuenta) con las partes casi vacías (sólo el
índice). **Relanzado entero a las 17:33 UTC** en la cuenta nueva; la medición
(inicio, fin y tokens de cada investigador) se anota en `/tmp/claude-0/medicion_01.txt`
y, al terminar, en esta sección.

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

> Trae la rama `claude/peaceful-maxwell-fklpkp` (`git fetch origin claude/peaceful-maxwell-fklpkp && git checkout -B <tu rama> FETCH_HEAD`), lee `ESTADO.md` y sigue con la skill serie-en-equipo: primero los trabajos a medias, luego el orden de ESTADO.md.

Orden de trabajo:
1. Piloto de One Piece (equipo de 8) hasta COMPLETA; anotar la medición.
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
