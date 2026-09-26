# CONTINUAR — cómo seguir desde otra cuenta o sesión

## 0. Lo último (26-sep-2026, 03:40 UTC) — empieza por aquí

La rama con todo al día es ahora **`claude/focused-ritchie-qolnvi`** (sesión
https://claude.ai/code/session_0138RwvbWSrVhmaUChfe2D2s). Lleva dentro
`claude/awesome-hypatia-ofqvy7` (la sesión que se quedó sin cuota a las 03:20
UTC) y, por tanto, `quirky-brahmagupta`, `trusting-thompson` y `amazing-johnson`.

- Estado al arrancar: 87 biblias COMPLETAS (revisar.py); con biblia pero con
  faltas: 17 (tabla de cumplimiento) y 105 (1 ❌); sin biblia y con partes: 47,
  48, 67, 68, 91, 127; con datos recolectados: 106, 128.
- En marcha desde las 03:35 UTC, un flujo por lote (B, D, E, F, G, H) con
  `Workflow({scriptPath: ".claude/workflows/serie-en-equipo-roles.js", args:
  {lote: "D", max: 4, esfuerzo: {inv: "medium", red: "high", aux: "low"}}})`.
  `serie-en-equipo-roles.js` es el flujo para una sesión que arrancó sin los
  `.claude/agents/` registrados: cada agente lee su ficha de rol y **lleva el
  modelo fijo del rol** (Haiku recolector/revisor/cierre, Sonnet
  investigadores, Opus redactor), y **mide las partes con revisor-partes antes
  de cada redactor también en modo redactar/seguir** (67 tenía texto.md con 7
  líneas y siguiente.py decía «redactar»). Lo flojo o inexistente se relanza
  una vez.
- Dos flujos de revisión (Sonnet, sólo lectura) sobre las 47 biblias cerradas
  desde el 25-sep 12:00 UTC: obra correcta, puntos flojos, restos, tabla
  honesta. Sus hallazgos se apuntan aquí abajo cuando acaben.
- Herramientas en esta máquina: apt (`apt-get update` primero: sin él da 404)
  y pip del punto 3.2 instalados; `navegar.py` necesita **los dos**
  certificados del proxy en NSS: `certutil -d sql:$HOME/.pki/nssdb -A -t "C,,"
  -n a -i /root/.ccr/ca-bundle.crt` y lo mismo con
  `/root/.ccr/agent-proxy-ca.crt` (con sólo el bundle sigue dando
  ERR_CERT_AUTHORITY_INVALID). No hace falta `playwright install`: usa
  /opt/pw-browsers/chromium.
- Red de esta máquina: archive.org, Wikipedia, YouTube, AniList, MAL,
  Dailymotion, MusicBrainz y Google responden 200 a curl; fandom.com, Reddit y
  TV Tropes dan 403 a curl (fandom por api.php; los otros con navegar.py).

## 0 (anterior). 26-sep-2026, 01:50 UTC

La rama con todo al día es ahora **`claude/quirky-brahmagupta-vrgrir`**. Lleva
dentro `claude/amazing-johnson-mxlnjs` y `claude/trusting-thompson-8pej3z` (la
sesión que se quedó sin cuota a las 01:22 UTC con los lotes B, D-H en marcha).

- Cerradas en la sesión https://claude.ai/code/session_01R4yquRAnGecNhSQcEfBmQJ:
  103 Hazbin Hotel, 123 Reanimal, 102 Ghibli en general; 125 Elden Ring, con
  el redactor en marcha.
- **Esa sesión no pudo investigar**: su entorno («Default», red «de confianza»)
  da 403 a archive.org, Wikipedia, Fandom, AniList, YouTube, Dailymotion,
  Google… y también a WebFetch. Hace falta un entorno con **acceso de red
  completo**; si no, sólo se puede redactar lo ya investigado.
- Cola cuando haya red (lo cortado primero):
  - 18: voz y texto de repaso, y luego el redactor (faltan también las 3 hojas).
  - 125: vídeo flojo (3 webs), sólo si su redactor no la cierra.
  - 17: voz y vídeo (Sigue:).
  - 44: vídeo (Sigue:).
  - 88: voz (Sigue:) y vídeo flojo.
  - 90: texto, más imagen, vídeo y voz flojas.
  - 46: texto, vídeo y voz, más imagen floja.
  - Después, las nuevas de `siguiente.py 9 --lote L`: 66, 47, 105, 126, 91…
    Ya tienen datos.json recolectado.
- Repasos cortos por herramientas que faltaron en su día (sin rastro de
  `voz.py`: 02, 03, 18, 23, 24, 28, 31, 32, 33, 89; sin fotogramas: 15, 31, 33).
- Si la sesión arranca desde `main`, los subagentes de `.claude/agents/` no
  aparecen hasta traer la rama: se lanzan con `general-purpose` y «Eres el
  subagente definido en .claude/agents/<rol>.md…», con el `model` del rol.
- **Una sola sesión por lote**: si la sesión de `trusting-thompson` tenía
  «continuar automáticamente» (06:10 UTC), hay que apagarla.

Mensaje para pegar en la sesión nueva (entorno con red completa):

> Lee CONTINUAR.md, punto 0. Trae la rama `claude/quirky-brahmagupta-vrgrir` (`git fetch origin claude/quirky-brahmagupta-vrgrir && git checkout -B <tu rama> FETCH_HEAD`), instala las herramientas (punto 3.2), deja `herramientas/guardar.sh --cada 300` en segundo plano y sigue la cola del punto 0 con la skill `serie-en-equipo` (o `Workflow` si lo tienes), lote por lote (B, D, E, F, G, H). El lote C está terminado. No toques `main`.

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
**lote C** (https://claude.ai/code/session_01Tyk6GzpvzkPnU36EVJt7eZ) terminó su
lote: las 12 biblias de 19-30 dan COMPLETA.

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
- C: terminado (12 de 12 COMPLETAS; lo cerró la sesión aparte)
- D: 43 (seguir) · 45 (redactar) · 44 (nueva) · 46 (nueva) · 47 (nueva) · 48 (nueva)
- E: 63 (redactar) · 62 (nueva) · 65 (nueva) · 66 (nueva) · 67 (nueva) · 68 (nueva)
- F: 87 (seguir) · 89 (redactar) · 88 (nueva) · 90 (nueva) · 91 (nueva) · 92 (nueva)
- G: 102 (seguir) · 104 (redactar) · 100 (redactar) · 101 (redactar) · 103 (nueva) · 105 (nueva)
- H: 121 (redactar) · 122 (redactar) · 124 (redactar) · 123 (nueva) · 125 (nueva) · 126 (nueva)

**Mensaje para pegar en la sesión nueva** (cuenta Max, entorno con red abierta):

> Lee CONTINUAR.md y sigue el punto 3. Trae la rama `claude/amazing-johnson-mxlnjs`, instala las herramientas, deja `herramientas/guardar.sh --cada 300` en segundo plano y lanza un flujo por lote con la herramienta Workflow, en este orden: `Workflow({name: "serie-en-equipo", args: {lote: "G", ids: ["102-el-estilo-ghibli-en-general", "104-steven-universe", "100-la-princesa-mononoke", "101-your-name-cielos-y-ciudades"], esfuerzo: {inv: "medium", red: "high", aux: "low"}}})`, y lo mismo para H con ["121-tomb-raider", "122-little-nightmares", "124-no-man-s-sky", "123-reanimal"], D con ["43-kaguya-sama-love-is-war", "45-mob-psycho-100", "44-your-lie-in-april-shigatsu", "46-sakamoto-days"], E con ["63-las-guerreras-k-pop-kpop-demon-hunters", "62-intensamente-inside-out", "65-the-legend-of-zelda", "66-persona-5"], F con ["87-tsukimichi-moonlit-fantasy", "89-frieren-paisajes-y-memoria", "88-konosuba", "90-kaguya-sama-love-is-war"] y B con ["14-adventure-time-hora-de-aventura", "16-neon-genesis-evangelion", "17-arcane", "18-death-note"]. El lote C ya está terminado: no lo toques. Cuando un flujo acabe sus series, relánzalo con las siguientes de `siguiente.py 9 --lote L`. No toques `main`; no pulses el botón de parar mientras corran agentes.

## 3. Seguir desde una sesión nueva en la nube (cuenta Max)

1. Trae la rama: `git fetch origin claude/amazing-johnson-mxlnjs && git checkout -B <tu rama> FETCH_HEAD`
   (tu rama debe empezar por `claude/` para que `juntar.sh` la recoja). Si la
   sesión ya está en la rama `claude/amazing-johnson-mxlnjs`, trabaja ahí mismo:
   el guardado junta los pushes de varias sesiones sin choques.
2. Herramientas (una vez por máquina):
   `apt-get install -y ffmpeg tesseract-ocr tesseract-ocr-jpn tesseract-ocr-spa`
   y `pip install -U "yt-dlp[default]" Pillow fontTools requests faster-whisper scenedetect opencv-python-headless praat-parselmouth onnxruntime playwright && python3 -m playwright install chromium`.
   En la nube, para que `navegar.py` no dé `ERR_CERT_AUTHORITY_INVALID`, Chromium
   tiene que fiarse del certificado del proxy:
   `apt-get install -y libnss3-tools && mkdir -p ~/.pki/nssdb && certutil -d sql:$HOME/.pki/nssdb -N --empty-password </dev/null; certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n ccr-agent-proxy -i /root/.ccr/agent-proxy-ca.crt </dev/null`.
   En la nube, para que `navegar.py` pase el proxy (si no, `ERR_CERT_AUTHORITY_INVALID`):
   `apt-get install -y libnss3-tools && mkdir -p ~/.pki/nssdb && certutil -d sql:$HOME/.pki/nssdb -N --empty-password && certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n ccr-agent-proxy -i /root/.ccr/agent-proxy-ca.crt`
   Sin la herramienta `Workflow` ni los subagentes registrados (sesión que arrancó en otra rama), el jefe lanza
   `Agent` general-purpose con `model` del rol y el mensaje «Lee .claude/agents/<rol>.md y síguelo. Serie <id>, modo <x>».
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
