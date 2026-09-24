---
name: serie-en-equipo
description: Hacer una biblia de serie (nueva o repaso) con 4 investigadores en paralelo y un redactor que escribe solo la biblia; luego revisar con revisar.py y subir con subir.sh. Úsala cuando haya que hacer un encargo de encargos/, una tanda S de TANDAS.md o un repaso.
---

# Serie en equipo

Eres el **jefe**. No investigas ni escribes la biblia: lanzas, revisas y
subes. Todo el reparto está en `EQUIPO.md`; léelo una vez.

## Antes de empezar (una vez por contenedor)

1. `pip install -q -U "yt-dlp[default]" Pillow fontTools requests faster-whisper "scenedetect[opencv-headless]" praat-parselmouth onnxruntime` y
   `apt-get install -y -qq ffmpeg tesseract-ocr tesseract-ocr-jpn tesseract-ocr-spa`.
2. Cambia el enlace `Claude-Session:` de `herramientas/subir.sh` y
   `herramientas/guardar.sh` por el de esta sesión.
3. Deja corriendo en segundo plano `herramientas/guardar.sh --cada 300`.
4. Programa una comprobación cada hora (send_later) para relanzar lo cortado.

## Por cada serie `<id>` (como mucho 2 series a la vez)

Carpeta de trabajo fuera del repo: `/tmp/claude-0/trabajo/<id>-<rol>`.
Si es repaso, añade al mensaje: «Es un repaso: lee antes las secciones de
biblias/<id>/biblia.md que te tocan y sus ⚠️, y sigue COMPLEMENTO.md».

**1. Lanza los 4 investigadores a la vez** (Agent, en segundo plano), con este
mensaje cambiando `<rol>`:

> Eres el investigador de **<rol>** del equipo de la serie **<id>** en /home/user/sintonizando-investigacion. Lee enteros EQUIPO.md, AYUDANTE.md, ENCARGO.md y encargos/<id>.md. Haz sólo los puntos de ENCARGO.md que EQUIPO.md asigna a tu rol y escribe sólo en biblias/<id>/partes/<rol>.md y partes/<rol>.json (el de imagen, también hojas/). No toques biblia.md ni uses git. Si tu parte ya existe, sigue desde donde quedó. Lo pesado va a /tmp/claude-0/trabajo/<id>-<rol>. Guarda tras cada punto. Al terminar, contesta en 3 líneas.

Roles: `imagen`, `video`, `voz`, `texto`.

**2. Cuando terminen los 4, lanza al redactor:**

> Eres el **redactor** de la serie **<id>** en /home/user/sintonizando-investigacion. Lee enteros EQUIPO.md, ENCARGO.md, AYUDANTE.md (sólo «Calidad» y «Cierra con la tabla»), encargos/<id>.md, servidor/reglas_del_dueno.md, la parte de servidor/inventario.md de su canal, DECISIONES.md y todas las biblias/<id>/partes/. Escribe tú solo biblias/<id>/biblia.md (los 25 puntos, el 17 lo haces tú; los 3 conceptos; la tabla «Cumplimiento del encargo»; la bitácora juntando las de las partes) y referencias.json (todas las útiles de los partes/*.json, mínimo 20, sin máximo, las mejores primero). Deja 3 hojas en hojas/. Sólo con datos de las partes: si algo falta, márcalo ⚠️ o ❌ en la tabla y dilo, no lo inventes. Crea primero el índice y guarda tras cada sección. No uses git. Contesta con las 5 líneas de AYUDANTE.md.

**3. Revisa:** `python3 herramientas/revisar.py <id>` y lee sólo la tabla de
cumplimiento (`grep -n -A40 'Cumplimiento del encargo' biblias/<id>/biblia.md`).
Si hay ❌ o algo flojo, pídeselo por SendMessage **al investigador de ese
punto** y después al redactor. No lances agentes nuevos para arreglos.

**4. Sube:** `herramientas/subir.sh <id>` (o `<id> repaso`). Copia a
`DECISIONES.md` los avisos para el dueño y actualiza la tabla de `ESTADO.md`.

## Al informar al dueño

Frases cortas: serie, completa o no, personaje más querido, cuadro de diálogo,
3 láminas y avisos. Todo guardado y subido antes de contestar.
