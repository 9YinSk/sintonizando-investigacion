# LOCAL — trabajar un lote desde la compu del dueño (con MWAPI)

Para seguir sin el límite de uso de la nube: Claude Code corre en la compu del
dueño, con la llave de MWAPI, y sube a GitHub igual que siempre. Todo lo demás
(REPARTO.md, la skill serie-en-equipo, `lotes/<letra>.md`) sigue igual.

## Lo que hace el dueño (una sola vez, en Windows)

1. **Ubuntu dentro de Windows.** PowerShell como administrador:
   `wsl --install` → reinicia → al abrir «Ubuntu», elige usuario y contraseña.
2. **Herramientas.** En la ventana de Ubuntu, pega esto (pide tu contraseña):
   ```
   sudo apt-get update && sudo apt-get install -y git gh python3-pip ffmpeg tesseract-ocr tesseract-ocr-jpn tesseract-ocr-spa
   pip3 install --user --break-system-packages -U "yt-dlp[default]" Pillow fontTools requests faster-whisper "scenedetect[opencv-headless]" praat-parselmouth onnxruntime
   curl -fsSL https://claude.ai/install.sh | bash
   ```
   Luego cierra y vuelve a abrir Ubuntu.
3. **GitHub.** `gh auth login` (GitHub.com → HTTPS → Login with a web browser;
   copia el código en el navegador) y después `gh auth setup-git`.
4. **El repo.** `gh repo clone 9YinSk/sintonizando-investigacion && cd sintonizando-investigacion`
5. **La llave.** `mkdir -p ~/.claude && nano ~/.claude/settings.json`, pega esto
   con tu llave en lugar de `TU_LLAVE` y guarda (Ctrl+O, Enter, Ctrl+X):
   ```json
   {
     "env": {
       "ANTHROPIC_AUTH_TOKEN": "TU_LLAVE",
       "ANTHROPIC_BASE_URL": "https://api.mwapi.dev",
       "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-sonnet-5",
       "ANTHROPIC_DEFAULT_SONNET_MODEL": "claude-sonnet-5",
       "ANTHROPIC_DEFAULT_OPUS_MODEL": "claude-sonnet-5",
       "CLAUDE_CODE_ENABLE_TELEMETRY": "0"
     },
     "permissions": {
       "defaultMode": "bypassPermissions",
       "skipDangerousModePermissionPrompt": true
     },
     "model": "sonnet"
   }
   ```
   La llave vive sólo en ese archivo: **nunca** en el repo ni en un chat.
6. **Arrancar.** Dentro de la carpeta del repo: `claude`. Escribe `/status`: tiene
   que salir `api.mwapi.dev`. Después pega el mensaje de «Qué pegar».

Deja la compu encendida y sin suspender. Si se cierra la ventana: vuelve a la
carpeta del repo, `claude --continue` y escribe «sigue».

## Qué pegar (lote G)

> Eres el jefe del **lote G** en la compu del dueño, con MWAPI. Lee LOCAL.md y REPARTO.md. Crea tu rama: `git fetch origin && git checkout -B claude/lote-g-local origin/claude/optimistic-turing-0es5zg`. Corre `herramientas/juntar.sh` y `echo G > .lote`. Haz la comprobación de modelos de LOCAL.md y apunta el resultado en `lotes/G.md`. Luego sigue con la skill serie-en-equipo sólo con tu lote (`python3 herramientas/siguiente.py 5 --lote G`), en cadena, desde lo que dice `lotes/G.md`. No toques ESTADO.md, DECISIONES.md, COSTOS.md ni TANDAS.md.

(Para otro lote, cambia la letra y la rama de origen por la última de ese lote.)

## Lo que cambia para el jefe en local

- **Herramientas**: ya las instaló el dueño (paso 2). No uses `sudo`: pide la
  contraseña y te quedarías parado; si falta algo, avisa en `lotes/<letra>.md`.
- **Enlace de sesión** en `subir.sh` y `guardar.sh`: no hay; déjalo como está.
- **Comprobación de cada hora** (`send_later`): no existe en local. No hace
  falta: la sesión sigue mientras la ventana esté abierta.
- **Sí** lanza `herramientas/guardar.sh --cada 300` en segundo plano.
- **Rama**: `claude/lote-g-local` (empieza por `claude/` para que `juntar.sh`
  de la central la encuentre).

## Comprobación de modelos (al empezar)

La llave ya está en el entorno (`ANTHROPIC_AUTH_TOKEN`); no la imprimas.

1. `curl -s https://api.mwapi.dev/v1/models -H "x-api-key: $ANTHROPIC_AUTH_TOKEN" -H "anthropic-version: 2023-06-01" | python3 -m json.tool | head -40`
2. Para cada modelo con «opus» en el nombre, una petición mínima
   (`POST /v1/messages`, `max_tokens: 20`) y mira el campo `model` de la respuesta.
3. Si alguno responde, dile al dueño que cambie `ANTHROPIC_DEFAULT_OPUS_MODEL`
   en `~/.claude/settings.json` por ese nombre y reabra `claude --continue`: así
   el redactor va en Opus, como pide la skill. Si no, todo va en `claude-sonnet-5`
   y lo anotas en `lotes/<letra>.md`.

Ojo: un revendedor puede poner lo que quiera en esos campos. Es una
comprobación de nombres, no una garantía. La prueba real es la calidad:
`revisar.py` tiene que seguir dando COMPLETA, como en 97-99.

## Costos

Apunta en `lotes/<letra>.md` los tokens de cada agente, como siempre. En la
nube cada serie gastó 1,2-1,3 millones de tokens (4 investigadores y un
redactor). Mira en el panel de MWAPI cuánto cobra la primera serie y avisa al
dueño cuántas alcanzan con el saldo.
