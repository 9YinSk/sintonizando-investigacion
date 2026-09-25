# AYUDANTE — cómo trabaja cada ayudante de una tanda

Eres un ayudante: haces **un solo encargo** mientras otros ayudantes hacen los
suyos en el mismo contenedor. La sesión que te lanzó sube tu trabajo cuando
termines. Esto complementa `ENCARGO.md` (series) o `TEMA.md` (temas): léelos
enteros antes de empezar, junto con tu archivo de `encargos/` o `temas/`.

## Ahorra sin recortar (obligatorio)

Cada paso que das vuelve a enviar todo lo que llevas leído: lo caro no es
buscar, es cargar de más. El equipo de 8 gastó 65 dólares en 25 minutos sin
terminar. La calidad no se toca (los 25 puntos, 40 fuentes, todo con fuente y
minuto); se ahorra así:

1. **Empieza por `partes/datos-<tu rol>.md`**: lo dejó `herramientas/recolectar.py`
   (AniList, Doblaje Wiki con muestras de audio, Fandom, Danbooru, Safebooru,
   Wallhaven, Sketchfab, Openverse, Dailymotion, Internet Archive, MusicBrainz,
   Steam, Reddit). **No repitas esas consultas**: compruébalas, elige, mira y
   ve a por lo que falta.
2. **No leas la biblia entera** (~45 mil tokens): `python3 herramientas/seccion.py
   <id> --rol <tu rol>` te da tus secciones, `--avisos` sólo sus ⚠️ y
   `--indice` el mapa.
3. **Nunca imprimas una respuesta entera** de una API o una web: filtra con
   Python, `jq`, `grep` o `head` y quédate con lo que sirve (40 líneas como mucho
   por salida).
4. **Imágenes**: mira primero hojas de contacto (muchas imágenes en una) y abre
   en grande sólo la que vas a citar.
5. **Escribe añadiendo**, no reescribiendo: `Edit` o `cat >> archivo <<'EOF'`.
   Reescribir un archivo largo entero cuesta cada vez.
6. **Tandas cortas**: hasta unas **100 acciones** por tanda (50 si te
   relanzan). Al llegar, guarda, escribe al final de tu parte una línea
   `Sigue: <lo obligatorio que falta, en concreto>` y termina. El jefe te
   relanza limpio (sale mucho más barato que seguir con la memoria llena). Si
   no te falta nada obligatorio, **no dejes ninguna línea `Sigue:`**: sin ella
   se entiende que terminaste (un «Sigue: nada» hace que te relancen).

## Reglas del contenedor compartido

- **Sólo escribes en tu carpeta**: `biblias/<tu-encargo>/` (series) o
  `investigaciones/<tu-tema>/` (temas). Nada fuera de ella en el repositorio.
- **No uses git**: ni `add`, ni `commit`, ni `push`, ni `checkout`, ni `stash`.
  Lo sube la sesión principal con `herramientas/subir.sh`.
- Lo pesado (imágenes originales, subtítulos, vídeos, clones de GitHub) va a
  tu carpeta de trabajo **fuera del repositorio** (te la dice el mensaje de
  arranque) o a `herramientas/referencias/`, que git ignora.
- En el repositorio sólo quedan: `biblia.md` (o `informe.md`),
  `referencias.json` (o `recursos.json`) y, en series, `hojas/` con **como mucho
  3 JPEG de menos de 3 MB** cada uno.

## Escribe por partes (el límite de uso puede cortarte)

1. Lo primero, crea tu `biblia.md` con el índice de secciones vacías.
2. Rellena **una sección cada vez y guárdala** antes de pasar a la siguiente.
   Nada de dejar todo para el final: si te cortan, lo guardado se aprovecha.
3. Si al arrancar ya hay una `biblia.md` a medias en tu carpeta, **no empieces
   de cero**: léela, sigue desde la primera sección vacía o floja.

## La red está abierta: úsala antes que el buscador

El buscador web tiene un cupo de unas **50 búsquedas por ayudante**. Planifícalas
(en español, inglés, japonés y coreano o chino según la obra) y usa la red
directa para todo lo demás, con `curl` o Python:

- **Fandom (wikis de la serie)**: la API (`https://<wiki>.fandom.com/api.php`),
  con `prop=imageinfo&iiprop=url|size` para el tamaño real de cada imagen.
  Las imágenes de `static.wikia.nocookie.net` piden la cabecera
  `Referer: https://www.fandom.com/`.
- **Hojas de contacto**: `python3 herramientas/investigar_serie.py --serie "<Serie>"
  --wiki <subdominio> --paginas "<Personaje 1>" "<Personaje 2>" …` deja las
  hojas numeradas en `herramientas/referencias/<slug>/`. Elige las 3 mejores
  (o monta las tuyas con Pillow), guárdalas en `hojas/` con nombre claro
  (`personajes_01.jpg`, `objetos_01.jpg`, `fondos_01.jpg`) y **míralas**: en la
  biblia di qué número de cada hoja sirve y para qué.
- **Doblaje Wiki**: `https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=<Serie>`
  (la web normal da 402). Cada nombre de actor, **en dos fuentes**.
- **YouTube**: `yt-dlp --skip-download` para título, duración, capítulos y
  subtítulos (`--write-subs --write-auto-subs --sub-langs "es-419,es,ja,en"`).
  Así sacas el **minuto exacto**. Si da 429, espera un minuto y reintenta; no
  insistas en bucle.
- **Reddit**: `https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=<sub>&query=<texto>`.
- **Sketchfab**: `https://api.sketchfab.com/v3/search?type=models&q=<objeto>&downloadable=true`;
  la licencia y el autor salen en la respuesta.
- **Letras**: comprueba tildes, ñ, ¿ y ¡ abriendo el archivo con `fontTools`
  (ya instalado), no de memoria.
- **GitHub**: subtítulos japoneses (p. ej. el espejo de kitsunekko), fichas,
  letras, recursos.
- **Wayback Machine** (`https://web.archive.org/…`) para páginas borradas.

Si una web da 403, anótalo en la bitácora y busca otra vía; no gastes más de
dos intentos en la misma.

## Mira los vídeos de verdad (obligatorio en series)

Es la queja principal del dueño: «no miras vídeos, no te empapas». Leer reseñas
**no cuenta** como mirar. Tú puedes ver imágenes: úsalo.

1. Como mínimo mira **el opening, un ending, un tráiler y 3 escenas icónicas**
   (clips oficiales en YouTube):
   `python3 herramientas/fotogramas.py "<url>" --cada 3 --salida <tu-carpeta-de-trabajo>/<nombre>`.
   Saca hojas con el número y el minuto de cada fotograma. **Ábrelas con Read y
   míralas** (`--fotograma <segundo>` saca uno en grande).
   Si YouTube da 429 o pide «iniciar sesión» (es por ratos: somos varios
   ayudantes con la misma IP), espera 3-5 minutos y reintenta, de uno en uno.
   Plan B: el mismo clip oficial en Dailymotion o Internet Archive
   (fotogramas.py lee cualquier sitio que lea yt-dlp; así lo hizo el repaso
   de Harry Potter). Plan C: los *storyboards* de YouTube, marcando el minuto como ±2 s. Borra el
   `video.mp4` cuando ya tengas las hojas: el disco es compartido.
2. Lo que escribas de poses, gestos, ropa, luz, encuadres y tipografía en
   pantalla sale de lo que viste, con **minuto y enlace `&t=`**. Las poses del
   punto 14 salen de aquí y de las hojas de la wiki, no de la memoria.
3. **Colores medidos**: saca los hex con Pillow de un fotograma o de arte
   oficial (di de cuál). Las paletas de fans sólo como contraste.
4. **Frases del doblaje latino, textuales**: busca clips oficiales doblados
   (Crunchyroll en Español, Netflix Latinoamérica, Disney/Warner Latino, el
   canal de la distribuidora…) y baja sus subtítulos o subtítulos automáticos
   en español (`yt-dlp --skip-download --write-subs --write-auto-subs
   --sub-langs "es.*" <url>`). Cita cada frase con su vídeo y minuto. Si no hay
   clips doblados oficiales, dilo.

## Herramientas por tarea (úsalas: dan datos, no impresiones)

| Para… | Herramienta |
|---|---|
| **Datos de la serie ya juntados** (el jefe lo corre antes de lanzarte) | `python3 herramientas/recolectar.py <id>` → `partes/datos-*.md` y `partes/datos.json` |
| **Sólo tus secciones de la biblia** | `python3 herramientas/seccion.py <id> --rol <rol>` (`--avisos`, `--indice`) |
| **Openings y endings sin YouTube** | las URL `.webm` de AnimeThemes (en `datos-video.md` si respondió) valen para `fotogramas.py` |
| **Frases del doblaje latino** sin YouTube | las muestras `.mp3` de Doblaje Wiki (en `datos-voz.md`) con `voz.py` |
| **Ver un capítulo entero** barato: ficha minuto a minuto con planos, lo que se dice y lo que se lee | `python3 herramientas/episodio.py "<url o archivo>" --titulo … --idioma ja|es [--ocr] --salida … --id <id>` → `partes/episodios.md` |
| **Mirar un vídeo** sin perder escenas cortas | `python3 herramientas/fotogramas.py "<url>" --cortes --salida …` (un fotograma por plano) |
| **Oír una voz**: frase textual con minuto y cómo suena (registro, expresividad en semitonos, velocidad) | `python3 herramientas/voz.py "<url o audio>" [--desde s --hasta s] --salida …` (Whisper en local; revisa nombres propios, se equivoca) |
| **Colores medidos** (vestuario, fondos) y **cómo está pintado** (plano o degradado, cuánta línea y de qué color) | `python3 herramientas/estilo.py <imágenes o URLs> --salida …` |
| **Etiquetas de anime** (pelo, ropa, pose, expresión, personaje) con el vocabulario que entienden las IA de imagen | `python3 herramientas/estilo.py <imagen> --etiquetas --salida …` (modelo WD14 en local) |
| **Leer texto en una imagen** (cartelas, menús de juegos, carteles, globos) | `tesseract <imagen> - -l spa+jpn+eng` |
| **Letras**: si traen tildes, ñ, ¿ y ¡ | fontTools (`TTFont(f).getBestCmap()`); letras libres con `latin-ext` en `https://api.fontsource.org/v1/fonts?subsets=latin-ext` |
| **Texturas libres (CC0)** | `https://ambientcg.com/api/v2/full_json?type=Material&q=<paper|fabric|wood>` |

Pon en la biblia de dónde sale cada dato («paleta medida con estilo.py en el
fotograma 12 de …»). Las herramientas ayudan a describir; las imágenes se miran
igual (Read).

## El encargo manda: no lo «corrijas» sin pruebas

Si el encargo o el dueño nombran algo (un objeto, una escena, un gag) y tú no lo
encuentras, **lo más probable es que no buscaste bien**. Antes de escribir «no
existe» o «posible confusión»: búscalo en el texto de la wiki
(`api.php?action=query&list=search&srwhat=text&srsearch=…`), en inglés y en el
idioma original, y en el wikitext de las páginas de los personajes. Si aun así
no aparece, escribe «no lo encontré» con las búsquedas que hiciste, **nunca**
«no existe». (Caso real: la caja de mangos de Bocchi sale en el episodio 1 y en
su ficha de la wiki; el ejemplo antiguo dijo que era una confusión.)

## Los ejemplos de `biblias/_ya_hechas/` son antiguos

Se hicieron antes de este encargo y se quedan cortos (vídeos sin mirar, el de
Attack on Titan tiene 99 líneas). Sirven para ver el tono, no el nivel. El nivel
lo marca `ENCARGO.md`, punto por punto.

## Cierra con la tabla de cumplimiento (obligatoria)

Antes de la bitácora, añade **«Cumplimiento del encargo»**: una tabla con los
25 puntos de «Qué investigar», los 3 conceptos, las 40 fuentes, los tipos de
fuente de «Profundidad exigida», las hojas y `referencias.json`. Para cada uno:
✅ hecho, ⚠️ a medias o ❌ no hecho, y **por qué**. Nada se omite en silencio:
si no lo hiciste, se ve en la tabla.

## Calidad

- Mínimo **40 fuentes distintas**, de todos los tipos que pide `ENCARGO.md`.
- ✅ = confirmado en dos fuentes; ⚠️ = una sola fuente o de memoria. No
  inventes minutos, tamaños ni nombres: si no lo comprobaste, lleva ⚠️.
- `referencias.json`: **todas las útiles** (mínimo 20, sin máximo; las mejores primero), con `url`, `fuente`, `ancho`, `alto`
  (**medidos**), `que_es`, `para_que`, `licencia`. La `url` es **la imagen**
  (o el vídeo con `&t=`), no una página donde «hay imágenes».
- Frases cortas, para leer en el celular. Termina con los 3 conceptos de lámina
  y la «Bitácora de búsqueda».

## Al terminar

Contesta a la sesión principal sólo con **5 líneas**: qué serie (o tema),
cuántas referencias y fuentes, el personaje más querido (o la herramienta
clave), el cuadro de diálogo propio de la serie (o el hallazgo más útil) y las
3 ideas de lámina (o las 3 acciones para sus proyectos). Añade una sexta línea
sólo si hay un aviso para el dueño.
