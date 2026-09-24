# ESTADO — dónde va el trabajo y cómo seguir en otro contenedor

Actualizado: 2026-09-24, 15:35 UTC.

## Dónde está guardado

Todo el trabajo está en la rama **`claude/optimistic-edison-gyhtgr`**.
`main` todavía **no** lo tiene. Una sesión nueva empieza desde `main`, así que
lo primero que tiene que hacer es traer esta rama.

## Qué está hecho

- **Series:** 31 de 227 (01 a 31), marcadas en `TANDAS.md`.
- **Repasos (segunda pasada):** 2 de 25 (03 Solo Leveling y 05 Oshi no Ko).

## Qué está a medias (guardado, sin marcar en `TANDAS.md`)

| Trabajo | Líneas | ⚠️ | Hojas | Referencias | Lo que falta |
|---|---|---|---|---|---|
| repaso 01-one-piece | 1181 | 49 (antes 47) | 3 | 40 | casi todo el repaso: vídeos, ⚠️, «Segunda pasada · qué cambió», cumplimiento |
| repaso 02-attack-on-titan | 1441 | 4 (antes 14) | 3 | 39 | revisar que esté completo y cerrar |
| repaso 04-harry-potter | 1725 | 45 (antes 55) | 3 | 40 | resolver ⚠️, vídeos, cumplimiento |
| repaso 06-spy-x-family | 1138 | 77 (antes 77) | 0 | 33 | recién empezado: el repaso entero |
| 32-jujutsu-kaisen | 1586 | 39 | 3 | 37 | secciones 20, cumplimiento y 21 (bitácora) |
| 33-frieren | 1112 | 35 | 3 | 0 | secciones 0, 1, 4, 15, 17-21, cumplimiento y `referencias.json` |
| 34-haikyuu | 1437 | 27 | 3 | 0 | secciones 1, 18-21, cumplimiento y `referencias.json` |

«Antes» es el número de ⚠️ que tenía la biblia antes de empezar su repaso
(commit `6d6407f`).

## Cómo seguir en un contenedor nuevo

Pega esto en una sesión nueva en la nube, con este repositorio:

> Trae la rama `claude/optimistic-edison-gyhtgr` (`git fetch origin claude/optimistic-edison-gyhtgr && git checkout -B <tu rama> FETCH_HEAD`), lee `ESTADO.md` y sigue: relanza un ayudante por cada trabajo a medias, diciéndole que siga desde lo guardado, sin empezar de cero.

Lo que tiene que hacer esa sesión:

1. Traer la rama (arriba) y trabajar en la suya propia a partir de ella.
2. Instalar las herramientas (el contenedor nuevo no las trae):
   `pip install -U "yt-dlp[default]" Pillow fontTools requests` y
   `apt-get install -y ffmpeg`.
3. Cambiar el enlace `Claude-Session:` de `herramientas/subir.sh` y
   `herramientas/guardar.sh` por el de la sesión nueva.
4. Dejar corriendo en segundo plano `herramientas/guardar.sh --cada 600`
   (sube lo que va a medias cada 10 minutos).
5. Relanzar los ayudantes de la tabla: cada uno lee `AYUDANTE.md`,
   `ENCARGO.md` (y `COMPLEMENTO.md` si es repaso) y **sigue la biblia que ya
   hay**, desde lo que falta.
6. Al terminar cada uno: `herramientas/subir.sh <id>` o
   `herramientas/subir.sh <id> repaso`.
7. Después: siguientes repasos (07 en adelante) y tanda S9 (35, 36) en
   `TANDAS.md`.

## Avisos

- Con 7 ayudantes a la vez, el límite de uso se acabó dos veces el 24 de septiembre.
  Con menos ayudantes el uso dura más.
- YouTube corta a ratos la descarga de vídeos (varios ayudantes con la misma
  IP). Esperar 3-5 minutos y reintentar; si no, miniaturas de vista previa
  (*storyboards*) con el minuto a ±2 s.
