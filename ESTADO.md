# ESTADO — dónde va el trabajo y cómo seguir en otro contenedor

Actualizado: 2026-09-24, 17:00 UTC. Rama: **`claude/optimistic-keller-but3rn`**
(`main` todavía no tiene este trabajo).

## Cuándo una biblia está completa

`python3 herramientas/revisar.py` lo dice para cada biblia. Está **COMPLETA**
cuando tiene:

- la tabla «Cumplimiento del encargo» (17 puntos, 3 conceptos, 40 fuentes,
  tipos de fuente, hojas y referencias) **sin ningún ❌**;
- 20-40 entradas en `referencias.json` y 3 hojas en `hojas/`;
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

## En marcha al cortar esta sesión (guardado a medias cada 5 min)

| Trabajo | Qué es |
|---|---|
| repaso 01-one-piece | casi cerrado |
| repaso 06-spy-x-family | a medias: ya tiene 3 hojas |
| 35-one-punch-man | recién empezado |
| 36-hunter-x-hunter | recién empezado |

## Cómo seguir en un contenedor nuevo

Pega esto en una sesión nueva en la nube, con este repositorio:

> Trae la rama `claude/optimistic-keller-but3rn` (`git fetch origin claude/optimistic-keller-but3rn && git checkout -B <tu rama> FETCH_HEAD`), lee `ESTADO.md` y sigue: relanza un ayudante por cada trabajo a medias, diciéndole que siga desde lo guardado, sin empezar de cero.

Lo que tiene que hacer esa sesión:

1. Traer la rama (arriba) y trabajar en la suya propia a partir de ella.
2. Instalar las herramientas:
   `pip install -U "yt-dlp[default]" Pillow fontTools requests` y
   `apt-get install -y ffmpeg`.
3. Cambiar el enlace `Claude-Session:` de `herramientas/subir.sh` y
   `herramientas/guardar.sh` por el de la sesión nueva.
4. Dejar corriendo en segundo plano `herramientas/guardar.sh --cada 300`.
5. Relanzar los trabajos de la tabla de arriba (4 ayudantes a la vez como
   mucho: con 7 el límite de uso se acaba enseguida). Cada ayudante lee
   `AYUDANTE.md`, `ENCARGO.md` (y `COMPLEMENTO.md` si es repaso) y **sigue la
   biblia que ya hay**.
6. Al terminar cada uno: `python3 herramientas/revisar.py <id>` y, si dice
   COMPLETA, `herramientas/subir.sh <id>` (o `<id> repaso`). Si le falta algo,
   se lo devuelve al ayudante.
7. Orden después: repaso 31 (el ❌), repasos 06-30, y tandas S10 en adelante.

## Avisos

- YouTube pide «iniciar sesión» a ratos (IP de servidor). Plan B: el mismo
  clip en Dailymotion o Internet Archive. Plan C: miniaturas de vista previa
  (±2 s). Si el dueño añade la variable de entorno `YT_COOKIES` (cookies.txt de
  una cuenta de Google **secundaria**), hay que hacer que `fotogramas.py` la
  use con `--cookies`.
- Crunchyroll no se puede usar (403 desde el servidor y DRM).
