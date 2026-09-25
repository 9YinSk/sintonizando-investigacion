# CONTINUAR — cómo seguir desde otra cuenta o sesión

Escrito el 25-sep-2026 a las 22:40 UTC por la sesión central
(https://claude.ai/code/session_0178LSBU8mFn49LiPaSVU6fN). Si esa sesión se
acaba, **todo lo necesario está aquí y en la rama**.

## 1. Dónde está todo

- **Rama `claude/amazing-johnson-mxlnjs`**: lo tiene todo junto: las biblias de
  los ocho lotes (A-H), las herramientas al día, la skill `serie-en-equipo`, los
  subagentes (`.claude/agents/`), el flujo guardado (`.claude/workflows/`), el
  motor de GitHub y este archivo. **`main` está viejo**: cuando el dueño diga
  «pásalo a main», se hace `git push origin claude/amazing-johnson-mxlnjs:main`
  (o se abre un PR y se junta).
- Estado por lote: `python3 herramientas/siguiente.py 9 --lote <L>` (lo que toca
  y en qué modo) y `python3 herramientas/revisar.py` (qué biblias están
  COMPLETAS). `lotes/<L>.md` es orientativo; el disco manda.
- Series hermanas (misma obra, dos encargos): `python3 herramientas/hermanas.py`.

## 2. Qué corría al escribir esto (para no duplicar)

Sesión central (esta rama, guardado automático cada 5 min): flujos por lote con
las series **D** 45, 46, 47 · **E** 63, 65, 66 · **F** 89, 90, 91 · **G** 104,
108, 105 · **H** 124, 125, 126 · **B** 14-18 (repasos) · sólo redactor: 64, 86,
100, 101, 121, 122 · roles que faltaban: 42, 43, 87, 102.
Sesión aparte del **lote C** (misma rama): https://claude.ai/code/session_01Tyk6GzpvzkPnU36EVJt7eZ.

Cómo saber si siguen vivas: `git log --oneline -10 origin/claude/amazing-johnson-mxlnjs`
(el guardado dice qué series se tocaron y cuándo) y las fechas de
`biblias/<id>/partes/*.md`. Si una serie no cambia en más de una hora, está
libre.

## 3. Seguir desde una sesión nueva en la nube (cuenta Max)

1. Trae la rama: `git fetch origin claude/amazing-johnson-mxlnjs && git checkout -B <tu rama> FETCH_HEAD`
   (tu rama debe empezar por `claude/` para que `juntar.sh` la recoja). Si la
   sesión ya está en la rama `claude/amazing-johnson-mxlnjs`, trabaja ahí mismo:
   el guardado junta los pushes de varias sesiones sin choques.
2. Herramientas (una vez por máquina):
   `apt-get install -y ffmpeg tesseract-ocr tesseract-ocr-jpn tesseract-ocr-spa`
   y `pip install -U "yt-dlp[default]" Pillow fontTools requests faster-whisper scenedetect opencv-python-headless praat-parselmouth onnxruntime playwright && python3 -m playwright install chromium`.
3. `export CLAUDE_SESSION_URL=<enlace de la sesión>; herramientas/guardar.sh --cada 300 &`
4. Elige un lote libre (punto 2) y lánzalo:
   - Con la herramienta `Workflow`: `Workflow({name: "serie-en-equipo", args: {lote: "G", max: 6, esfuerzo: {inv: "medium", red: "high", aux: "low"}}})`
     (o `ids: [...]` para series concretas). Cada flujo lleva 2 agentes a la vez
     en una máquina de 4 procesadores: lanza uno por lote para ir en paralelo.
   - Sin `Workflow`: la skill `serie-en-equipo` con los subagentes (`Agent` con
     `subagent_type` `recolector`, `investigador-imagen/video/voz/texto`,
     `redactor`, `cierre` y un mensaje corto «Serie <id>, modo <x>»).
5. Reglas: una sola sesión por lote y por serie; no tocar `main`; no pulsar el
   botón de parar mientras corren agentes (los corta); todo lo del lote va a
   `lotes/<L>.md`; la exigencia de ENCARGO.md no se baja.

## 4. Seguir en GitHub Actions con la Max (sin sesión abierta)

Cuando `main` esté al día: el dueño crea el pase con «MAX EN GITHUB» en su PC
(secreto `CLAUDE_CODE_OAUTH_TOKEN`), pone las letras en `.github/lotes-activos`
(tres con Max 5x, cinco con 20x) y los lotes corren solos, 5 h por vuelta.
Detalles en README, «Los lotes en GitHub». Mientras haya sesiones trabajando un
lote, **su letra no debe estar** en `lotes-activos`.

## 5. Lo que le toca al dueño

- Crear el pase de la Max en la PC (una vez) si quiere los lotes en GitHub.
- Decir «pásalo a main».
- Decir qué Max compró (5x: tres lotes a la vez; 20x: cinco).
- Repositorio privado o público: en privado GitHub cobra los minutos de las
  máquinas; en público no. Las sesiones en la nube no dependen de eso.
- Los avisos ⚠️ de cada lote (`lotes/<L>.md`, «Avisos para el dueño»): cosas que
  hay que oír o ver en persona.

## 6. Mejoras hechas el 25-sep (para no repetirlas)

Motor de GitHub a prueba de la Max; auditoría de scripts (siguiente.py con modo
`redactar` y «Sigue: nada» ignorado, guardar.sh guarda `lotes/` y sobrevive a
pushes en paralelo, recolectar.py no confunde obras, revisar.py cuenta bien);
skill y documentos sin contradicciones ni MWAPI; ramas de los lotes juntadas;
subagentes por rol con modelo fijo; flujo guardado; `navegar.py` (navegador sin
ventana para TV Tropes y Reddit); `hermanas.py`. Pendiente de aplicar: lo que
diga el análisis de mejoras en curso (se anotará aquí abajo).

## 7. Notas del análisis de mejoras

(pendiente: se añade cuando termine)
