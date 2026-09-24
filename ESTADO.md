# ESTADO — dónde va el trabajo y cómo seguir en otro contenedor

Actualizado: 2026-09-24, 17:00 UTC. Rama: **`claude/optimistic-keller-but3rn`**
(`main` todavía no tiene este trabajo).

## Cuándo una biblia está completa

`python3 herramientas/revisar.py` lo dice para cada biblia. Está **COMPLETA**
cuando tiene:

- la tabla «Cumplimiento del encargo» (17 puntos, 3 conceptos, 40 fuentes,
  tipos de fuente, hojas y referencias) **sin ningún ❌**;
- 20 entradas o más en `referencias.json` y 3 hojas en `hojas/`;
- si es una de las 01-30, la sección «Segunda pasada · qué cambió».

Los ⚠️ no la dejan incompleta: marcan datos con una sola fuente o cosas que
hay que ver u oír en persona (frases del doblaje, vídeos que YouTube no deja
bajar desde el servidor). Siempre quedarán algunos.

## Cómo va (17:00 UTC)

- **Completas (8):** 01*, 02, 03, 04, 05, 32, 33, 34.
  (*01 ya cumple, pero su ayudante aún lo está puliendo).
- **Hechas con reglas viejas, necesitan repaso (24):**
  - 06-25: red cerrada. Sin hojas, sin tabla, muchos ⚠️.
  - 26-30: red abierta, pero antes de las reglas de mirar vídeos y de la tabla.
  - 31 Demon Slayer: tiene tabla, pero con 1 ❌. Arreglo pequeño.
- **Nuevas pendientes:** 35 y 36 (en marcha) y de la 37 a la 131 (tandas S10-S33).
- **Temas (A1-P1):** 0 de 96.

## En marcha al cortar esta sesión (17:25 UTC)

**Piloto del equipo de 8 con One Piece (01)**, lanzado a las 17:15 UTC. Cada
investigador escribe en `biblias/01-one-piece/partes/<rol>.md` y `.json`
(roles en `EQUIPO.md`, «Equipo de 8»): arte, fanart-3d, escenas,
musica-videos, doblaje, personajes, dialogos, tecnica-mundo. Si se cortó:
relanzar cada rol con el mensaje de la skill `serie-en-equipo` («si tu parte ya
existe, sigue desde donde quedó») y, cuando estén los 8, el redactor, que
**edita la biblia que ya hay** y añade los puntos 18-25.
Medir: hora de inicio y fin de cada uno, para saber cuánto tarda el equipo.

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

> Trae la rama `claude/optimistic-keller-but3rn` (`git fetch origin claude/optimistic-keller-but3rn && git checkout -B <tu rama> FETCH_HEAD`), lee `ESTADO.md` y sigue con la skill serie-en-equipo: primero los trabajos a medias, luego el orden de ESTADO.md.

Trabajos a medias de la tabla de arriba:
- **Casi hechos** (repaso 01, repaso 06): un solo ayudante que siga la biblia
  que ya hay (método viejo, `AYUDANTE.md` + `COMPLEMENTO.md`), revisar y subir.
- **Recién empezados** (35, 36): con el equipo. El redactor aprovecha lo que
  ya haya en `biblia.md`.

Orden después: repaso 31 (el ❌), repasos 07-30 y tandas S10 en adelante,
como mucho 2 series a la vez. `subir.sh` ya no sube una biblia que
`revisar.py` no dé por COMPLETA (salvo `FORZAR=1`).

## Avisos

- Decisiones del dueño, cosas que oír en persona y sugerencias: `DECISIONES.md`.

- YouTube pide «iniciar sesión» a ratos (IP de servidor). Plan B: el mismo
  clip en Dailymotion o Internet Archive. Plan C: miniaturas de vista previa
  (±2 s). Si el dueño añade la variable de entorno `YT_COOKIES` (cookies.txt de
  una cuenta de Google **secundaria**), hay que hacer que `fotogramas.py` la
  use con `--cookies`.
- Crunchyroll no se puede usar (403 desde el servidor y DRM).
