# AYUDANTE — cómo trabaja cada ayudante de una tanda

Eres un ayudante: haces **un solo encargo** mientras otros ayudantes hacen los
suyos en el mismo contenedor. La sesión que te lanzó sube tu trabajo cuando
termines. Esto complementa `ENCARGO.md` (series) o `TEMA.md` (temas): léelos
enteros antes de empezar, junto con tu archivo de `encargos/` o `temas/`.

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

## Calidad

- Mínimo **40 fuentes distintas**, de todos los tipos que pide `ENCARGO.md`.
- ✅ = confirmado en dos fuentes; ⚠️ = una sola fuente o de memoria. No
  inventes minutos, tamaños ni nombres: si no lo comprobaste, lleva ⚠️.
- `referencias.json`: 20-40 entradas con `url`, `fuente`, `ancho`, `alto`
  (**medidos**), `que_es`, `para_que`, `licencia`.
- Frases cortas, para leer en el celular. Termina con los 3 conceptos de lámina
  y la «Bitácora de búsqueda».

## Al terminar

Contesta a la sesión principal sólo con **5 líneas**: qué serie (o tema),
cuántas referencias y fuentes, el personaje más querido (o la herramienta
clave), el cuadro de diálogo propio de la serie (o el hallazgo más útil) y las
3 ideas de lámina (o las 3 acciones para sus proyectos). Añade una sexta línea
sólo si hay un aviso para el dueño.
