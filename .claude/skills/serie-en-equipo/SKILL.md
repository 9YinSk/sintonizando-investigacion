---
name: serie-en-equipo
description: Hacer las biblias de series de forma autónoma y económica, una tras otra, sin bajar la exigencia de ENCARGO.md. El recolector gratuito junta los datos, 4 investigadores en Sonnet investigan y un redactor en Opus escribe; después se revisa con revisar.py, se sube con subir.sh y se sigue con la siguiente serie. Úsala para cualquier encargo de encargos/, tanda S de TANDAS.md, repaso o cuando digan «sigue».
---

# Serie en equipo (autónoma y económica)

Eres el **jefe**. No investigas ni escribes la biblia: preparas, lanzas,
revisas, subes y pasas a la siguiente, sin esperar al dueño. El reparto está
en `EQUIPO.md` («El método económico»); las reglas de ahorro de los
investigadores, en `AYUDANTE.md` («Ahorra sin recortar»).

**La exigencia no baja**: los 25 puntos de `ENCARGO.md`, 40 fuentes, todo con
fuente, minuto y tamaño. Al final, otra sesión de Claude hará las láminas
guiándose sólo por las biblias: lo que no esté escrito, no existe.

## Si eres un lote (varias cuentas a la vez)

Lee `REPARTO.md`. Al empezar: `herramientas/juntar.sh` y `echo <letra> > .lote`.
Usa `siguiente.py 5 --lote <letra>` y toca sólo tus series y `lotes/<letra>.md`
(ahí van tu estado, tus avisos para el dueño y tus costos; ESTADO.md,
DECISIONES.md, COSTOS.md y TANDAS.md los lleva la central).

## Una vez por contenedor

1. `pip install -q -U "yt-dlp[default]" Pillow fontTools requests faster-whisper "scenedetect[opencv-headless]" praat-parselmouth onnxruntime`
   y `apt-get install -y -qq ffmpeg tesseract-ocr tesseract-ocr-jpn tesseract-ocr-spa`
   (si apt da 404, antes `apt-get update`).
2. Cambia el enlace `Claude-Session:` de `herramientas/subir.sh` y
   `herramientas/guardar.sh` por el de esta sesión.
3. En segundo plano: `herramientas/guardar.sh --cada 300`.
4. Programa una comprobación dentro de una hora (send_later) que diga: «Sigue
   con la skill serie-en-equipo: relanza lo cortado y continúa». Vuelve a
   programarla en cada comprobación.

## En cadena (para ir rápido sin gastar más por serie)

Nunca esperes con las manos vacías. En cuanto los investigadores de una serie
terminan, lanza **a la vez** su redactor y los investigadores de la siguiente;
cuando un redactor termina, revisa, sube y su hueco lo ocupa el redactor de la
serie que ya esté lista. Como mucho 5 agentes vivos (4 investigadores + 1
redactor). Cada serie lleva su redactor nuevo: uno que siguiera con otra serie
arrastraría la memoria de la anterior y costaría más.

Al empezar, y cada vez que queden menos de 3 listas, recolecta por adelantado
en segundo plano las 5 siguientes (gratis):
`for id in $(python3 herramientas/siguiente.py 6 | awk '$1 ~ /^[0-9]+-/{print $1}'); do python3 herramientas/recolectar.py $id --hojas; done`

Esta sesión (el jefe) puede ir en Sonnet (`/model sonnet`): sólo lanza, revisa
y sube. El modelo de cada agente lo fija el `model` al lanzarlo.

## El bucle (repítelo hasta que no quede nada o el dueño diga basta)

**1. ¿Qué toca?** `python3 herramientas/siguiente.py 5`. Coge la primera que
no esté en marcha (modo `seguir`, `repaso-corto`, `nueva` o `repaso`).

**2. Recolecta (gratis)**, si no se hizo por adelantado:
`python3 herramientas/recolectar.py <id> --hojas`, y los capítulos clave con
`herramientas/episodio.py` (2 o 3 por serie: el 1, el de la escena más icónica y
uno reciente; ver su ayuda). Deja sus fichas en `partes/episodios.md`.
Mira la línea «Fallaron». Si AniList o Doblaje Wiki no encontraron la obra,
repite con `--solo anilist doblaje_wiki --nombres "<título en inglés>" "<título latino>"`.
En `repaso-corto` basta sin `--hojas`.

**3. Lanza los investigadores** (Agent, en segundo plano, **`model: "sonnet"`**),
uno por rol. Roles: `imagen`, `video`, `voz`, `texto`; en `repaso-corto` sólo
`imagen` (19, 23), `voz` (20, 21, 22) y `texto` (18, 24, 25). Mensaje:

> Eres el investigador de **<rol>** del equipo de **<id>** en /home/user/sintonizando-investigacion. Lee AYUDANTE.md (sobre todo «Ahorra sin recortar»), EQUIPO.md, ENCARGO.md y encargos/<id>.md. Haz sólo los puntos que EQUIPO.md da a tu rol, a fondo, y escribe sólo en biblias/<id>/partes/<rol>.md y partes/<rol>.json (el de imagen, también hojas/). Empieza por biblias/<id>/partes/datos-<rol>.md: no repitas esas consultas. No toques biblia.md ni uses git. Si tu parte ya existe, sigue desde su línea «Sigue:» o desde lo pendiente. Lo pesado va a /tmp/claude-0/trabajo/<id>-<rol>. Tandas de unas 70 acciones: al llegar, deja «Sigue: …» al final de tu parte y termina. YouTube pide iniciar sesión desde este servidor: usa Dailymotion, Internet Archive, AnimeThemes, las muestras de Doblaje Wiki o los storyboards (±2 s). No instales programas de terceros para saltarte bloqueos. Al terminar, contesta en 3 líneas.

Añade siempre: «Una sola tanda: hasta unas 100 acciones. Antes de terminar, repasa tus puntos contra ENCARGO.md: lo **obligatorio** (lo que pide cada punto) no se deja; si no te da, deja `Sigue:` sólo con lo obligatorio que falte. Lo que sería un extra va en «No encontré» con ⚠️, no en `Sigue:`. Lee también partes/episodios.md si existe.»

Añade según el modo:
- `repaso` / `seguir`: «Es un repaso: `python3 herramientas/seccion.py <id> --rol <rol>` y `--avisos` te dan lo que ya hay; aporta lo que falta, confirma lo dudoso y ve más hondo (COMPLEMENTO.md).»
- `repaso-corto`: «Sólo tus puntos <lista>, nuevos en el encargo: no están en la biblia. Mira `seccion.py <id> --indice` para no repetir nada.»

**4. Relanza sólo lo obligatorio.** Si una parte acaba con `Sigue:` (sólo
lleva lo obligatorio que faltó), relanza ese rol con un mensaje corto que diga
exactamente eso, hasta 50 acciones. Como mucho 2 tandas por rol; si aún queda
algo, que el redactor lo marque ⚠️ en la tabla y lo diga.

**5. Redactor** (Agent, **`model: "opus"`**) cuando no quede ningún `Sigue:`:

> Eres el **redactor** de la serie **<id>** en /home/user/sintonizando-investigacion. Lee PETICIONES.md, EQUIPO.md, ENCARGO.md, AYUDANTE.md («Ahorra sin recortar», «Calidad» y «Cierra con la tabla»), encargos/<id>.md, servidor/reglas_del_dueno.md, la parte de servidor/inventario.md de su canal, DECISIONES.md y todas las biblias/<id>/partes/ (primero las de los investigadores; los datos-*.md sólo para completar). Escribe tú solo biblias/<id>/biblia.md: los 25 puntos (el 17, guía para IA de imagen y de texto, lo haces tú), los 3 conceptos, la tabla «Cumplimiento del encargo» con los 25 puntos y la bitácora juntando las de las partes. referencias.json: todas las útiles de partes/*.json y datos.json, mínimo 20, sin máximo, las mejores primero. Deja 3 hojas en hojas/. Sólo con datos de las partes: si algo falta, márcalo ⚠️ o ❌ en la tabla y dilo, no lo inventes. Crea primero el índice y guarda tras cada sección, añadiendo, sin reescribir el archivo entero. No uses git. Contesta con las 5 líneas de AYUDANTE.md.

Añade según el modo:
- `repaso` / `seguir`: «Es un repaso: **edita en su sitio** la biblia que ya hay (COMPLEMENTO.md); no la leas entera, usa `seccion.py <id> --indice` y lee sólo la sección que vas a tocar. Mete lo nuevo, añade lo que falte y actualiza «Segunda pasada · qué cambió» y la tabla con los 25 puntos.»
- `repaso-corto`: «Sólo añade las secciones de los puntos 18-25 con lo de las partes, en su sitio (mira `seccion.py <id> --indice`), y actualiza la tabla de cumplimiento con los 25 puntos, «Segunda pasada · qué cambió», los conceptos si mejoran y la bitácora. No reescribas lo demás.»

**6. Revisa:** `python3 herramientas/revisar.py <id>` (exige los 25 puntos, 40
webs distintas enlazadas, 15 minutos, 10 hex, bitácora y conceptos) y
`grep -n -A45 'Cumplimiento del encargo' biblias/<id>/biblia.md`. Si falta
algo, SendMessage al investigador de ese punto (o relánzalo con el encargo
concreto) y luego al redactor. No lances equipos nuevos para arreglos.

**7. Sube:** `herramientas/subir.sh <id>` (en repasos, `<id> repaso`). Copia a
`DECISIONES.md` los avisos para el dueño, pon la serie al día en `ESTADO.md`
y anota en `COSTOS.md` una línea por agente (serie, rol, modelo, minutos y
tokens del aviso de fin). Vuelve al paso 1.

## Al informar al dueño

Frases cortas, sólo al terminar cada serie o si algo se atasca: serie,
completa o no, personaje más querido, cuadro de diálogo, 3 láminas, costo
medido y avisos. Todo guardado y subido antes de contestar.
