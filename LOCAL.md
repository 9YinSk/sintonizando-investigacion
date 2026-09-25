# LOCAL — un lote a mano, sin el motor de GitHub

Los lotes corren solos en GitHub con la suscripción Max (README, «Los lotes en
GitHub»). Esto es sólo para seguir un lote desde una sesión de Claude Code a
mano: la PC del dueño (WSL con `claude`) o una sesión en la nube.

**Antes de nada, quita la letra de `.github/lotes-activos`** (y cancela su run
en Actions si está en marcha): dos jefes en el mismo lote hacen el trabajo dos
veces.

1. Rama fija del lote, para que el motor la reconozca después:
   `git fetch origin && git checkout -B claude/lote-<l>-local origin/claude/lote-<l>-local`
   (en la nube, si tu rama es otra, no pasa nada: `juntar.sh` la recoge).
2. Herramientas: las del paso «Herramientas» de `.github/workflows/lote.yml`
   (apt: ffmpeg, tesseract con jpn y spa, tmux; pip: yt-dlp, Pillow, fontTools,
   requests, faster-whisper, scenedetect, opencv-python-headless,
   praat-parselmouth, onnxruntime; y Claude Code).
3. `herramientas/juntar.sh && echo <L> > .lote`, y en segundo plano
   `herramientas/guardar.sh --cada 300`.
4. Pega en la sesión (con `/model sonnet`):

> Eres el jefe del lote <L>. Lee REPARTO.md y lotes/<L>.md y sigue con la skill serie-en-equipo sólo con tu lote (`python3 herramientas/siguiente.py 5 --lote <L>`), en cadena. Fíate de `siguiente.py`. Todo lo tuyo (estado, avisos, tokens) va en lotes/<L>.md. No toques ESTADO.md, DECISIONES.md, COSTOS.md ni TANDAS.md.

Deja la máquina encendida y sin suspender. Si se cierra la ventana:
`claude --continue` y escribe «sigue». Al terminar, vuelve a poner la letra en
`.github/lotes-activos` para que GitHub siga desde tu rama.

*(Histórico: hasta el 25-sep-2026 esto era para MWAPI, un revendedor que se
dejó de usar; la comprobación de modelos de entonces queda en `lotes/G.md`.)*
