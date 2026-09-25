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

## 2. Estado al entregar (25-09-2026 23:09 UTC) y qué toma la cuenta siguiente

**Nada corre ya desde la sesión central**: todos sus flujos se pararon a las
23:10 UTC y todo quedó guardado y subido en la rama. La sesión aparte del
**lote C** (https://claude.ai/code/session_01Tyk6GzpvzkPnU36EVJt7eZ) iba en la
misma cuenta y puede haberse parado también: antes de tomar el C, mira si sus
series (24-30) cambiaron en la última hora (`git log --oneline -5 -- biblias/24* biblias/25* biblias/27*`).

| Lote | Series | Completas | A medias | Sólo datos | Sin empezar | Avance |
|---|---|---|---|---|---|---|
| A | 10 | 10 | 0 | 0 | 0 | 100 % |
| B | 13 | 9 | 4 | 0 | 0 | 69 % |
| C | 12 | 12 | 0 | 0 | 0 | 100 % |
| D | 20 | 6 | 2 | 4 | 8 | 30 % |
| E | 20 | 6 | 1 | 4 | 9 | 30 % |
| F | 20 | 10 | 2 | 7 | 1 | 50 % |
| G | 20 | 3 | 4 | 3 | 10 | 15 % |
| H | 15 | 4 | 3 | 4 | 4 | 26 % |
| Todo | 130 | 60 | 16 | 22 | 32 | 46 % |

Cerradas en la sesión central el 25-sep: 64 Steven Universe, 86 Saga of Tanya
the Evil, 42 Blue Lock y 15 Bob Esponja. Con trabajo a medias guardado (se
retoma solo con `siguiente.py`): 100, 101, 104, 124, 45, 63, 89, 43, 16 y las
del lote C.

**Qué toca en cada lote** (`siguiente.py 9 --lote L`, en orden; el modo dice
qué lanza el flujo):
- B: 14 (redactar) · 16 (repaso) · 17 (repaso) · 18 (repaso) · 4 (pendientes)
- C: 0 (pendientes)
- D: 43 (seguir) · 45 (redactar) · 44 (nueva) · 46 (nueva) · 47 (nueva) · 48 (nueva)
- E: 63 (redactar) · 62 (nueva) · 65 (nueva) · 66 (nueva) · 67 (nueva) · 68 (nueva)
- F: 87 (seguir) · 89 (redactar) · 88 (nueva) · 90 (nueva) · 91 (nueva) · 92 (nueva)
- G: 102 (seguir) · 104 (redactar) · 100 (redactar) · 101 (redactar) · 103 (nueva) · 105 (nueva)
- H: 121 (redactar) · 122 (redactar) · 124 (redactar) · 123 (nueva) · 125 (nueva) · 126 (nueva)

**Mensaje para pegar en la sesión nueva** (cuenta Max, entorno con red abierta):

> Lee CONTINUAR.md y sigue el punto 3. Trae la rama `claude/amazing-johnson-mxlnjs`, instala las herramientas, deja `herramientas/guardar.sh --cada 300` en segundo plano y lanza un flujo por lote con la herramienta Workflow, en este orden: `Workflow({name: "serie-en-equipo", args: {lote: "G", ids: ["102-el-estilo-ghibli-en-general", "104-steven-universe", "100-la-princesa-mononoke", "101-your-name-cielos-y-ciudades"], esfuerzo: {inv: "medium", red: "high", aux: "low"}}})`, y lo mismo para H con ["121-tomb-raider", "122-little-nightmares", "124-no-man-s-sky", "123-reanimal"], D con ["43-kaguya-sama-love-is-war", "45-mob-psycho-100", "44-your-lie-in-april-shigatsu", "46-sakamoto-days"], E con ["63-las-guerreras-k-pop-kpop-demon-hunters", "62-intensamente-inside-out", "65-the-legend-of-zelda", "66-persona-5"], F con ["87-tsukimichi-moonlit-fantasy", "89-frieren-paisajes-y-memoria", "88-konosuba", "90-kaguya-sama-love-is-war"] y B con ["14-adventure-time-hora-de-aventura", "16-neon-genesis-evangelion", "17-arcane", "18-death-note"]. El lote C sólo si sus series no cambiaron en la última hora: ["0"]. Cuando un flujo acabe sus series, relánzalo con las siguientes de `siguiente.py 9 --lote L`. No toques `main`; no pulses el botón de parar mientras corran agentes.

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

## 7. Análisis de mejoras (25-sep, tres lentes y un juez; 25 propuestas confirmadas)

**Hechas ya** (en la rama):
- `juntar_referencias.py` y `juntar_bitacora.py`: referencias.json y la bitácora
  las arma un script; el redactor (Opus) ya no las teclea (≈ 10 % de su gasto).
- El redactor lee sólo lo que necesita (fuera DECISIONES.md, inventario.md y
  datos-*.md enteros: ~130 k caracteres menos de contexto).
- `revisar_partes.py` + subagente `revisor-partes` (Haiku): mide las partes antes
  de pagar el redactor y el flujo relanza una vez los roles flojos.
- Investigadores: tablas fijas por punto (8, 13, 14, 15, 20) listas para pegar,
  primer punto escrito antes de la acción 20, frontera imagen/texto en modelos
  3D y tramas (puntos 3, 19 y 18).
- AnimeThemes: un intento y nota «no reintentar» (lleva semanas caído).
- `.github/lotes-activos` vacío mientras la nube trabaje esos lotes.

**Pendientes, por valor** (para una sesión con tiempo; no bajan la exigencia):
1. `armar_biblia.py`: montar biblia.md pegando las secciones de un solo rol
   (5, 6, 11, 15, 16, 19, 20, 23) y que Opus escriba sólo lo suyo (§0, §1, §17,
   conceptos, correcciones, tabla) y funda las mixtas (8, 10, 13, 14, 21).
   Pilotar en 2 series y comparar tokens y ✅ antes de generalizar (≈ −15 %).
2. Recolector más rico y gratis: subtítulos de kitsunekko para minutos de
   escena; episodios con pista latina de Internet Archive transcritos en segundo
   plano (`episodio.py`); muestras de Doblaje Wiki transcritas y medidas con
   `voz.py` (sólo personajes del encargo + top 12); `letras.json` con las
   letras más citadas comprobadas con fontTools; Safebooru por emoción como
   referencia de expresión (no cuenta como fotograma).
3. Series hermanas en «segunda mirada» con 2 roles + redactor (≈ 0,75 M en vez
   de 1,3 M) cuando la primera ya tiene biblia; ojo con los 40 webs de revisar.py.
4. `datos-voz.md` recortado (40 filas de reparto, resto en datos.json).
5. TV Tropes, TCRF, ArtStation: sólo por `navegar.py` o Wayback, una vez, desde
   el recolector.
6. Que `cierre` reciba y apunte los tokens de cada agente.

**Le toca al dueño** (dos secretos opcionales con gran ganancia): `YT_API_KEY`
(YouTube Data API v3, gratis: vistas, búsquedas de fandubs y comentarios → los
puntos 10, 21 y 22 dejan de quedar ⚠️) y `YT_COOKIES` (cookies.txt de una
cuenta secundaria: vídeos a 1080p en `fotogramas.py`). Se ponen como secretos
en GitHub y como variables de entorno en la nube o la PC.

**Cifras del juez**: quedan 69 series en D-H (59 nuevas); a 1,3 M por nueva y
0,33 M por «sólo redactor», unos 80 M de tokens (72 % Sonnet, 28 % Opus). Lo
más barato por biblia es cerrar primero las que sólo necesitan redactor.
