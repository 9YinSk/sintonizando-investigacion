# COMPLEMENTO — la segunda pasada de las biblias 01-25

Las biblias 01-25 se hicieron con la red cerrada: sólo buscador web y GitHub.
No tienen hojas de contacto, casi no usan Doblaje Wiki ni minutos de YouTube, y
muchos tamaños y datos llevan ⚠️. Ahora la red está abierta. Tu trabajo es
**corregirlas y completarlas, no rehacerlas**. Sigue `AYUDANTE.md` (reglas del
contenedor, herramientas de red, cómo guardar por partes) y `ENCARGO.md` (lo que
tiene que tener una biblia).

## Antes de tocar nada

1. Lee **entera** `biblias/<id>/biblia.md`, su `referencias.json` y su encargo
   en `encargos/<id>.md`.
2. Cuenta los ⚠️ que tiene (`grep -o '⚠️' biblia.md | wc -l`) y apunta el número.
3. Haz la lista de lo que falta o está flojo, sección por sección.

## Qué hacer, por orden

1. **Hojas de contacto** (lo que más falta): corre `herramientas/investigar_serie.py`
   con la wiki de Fandom de la serie y las páginas de los personajes de la
   biblia. Deja 3 hojas en `hojas/` (JPEG, menos de 3 MB) y **míralas**. Añade
   una sección «Las hojas de contacto» que diga qué números sirven, para qué
   pose o concepto, y enlaza el original de cada uno.
2. **Doblaje latino**: pasa cada nombre de actor, estudio y director por la API
   de Doblaje Wiki y una segunda fuente. Corrige lo que esté mal y pasa a ✅ lo
   confirmado. Añade las «frases propias del doblaje» que salgan.
3. **Minutos exactos**: con `yt-dlp` (capítulos y subtítulos) o subtítulos de
   GitHub, pon capítulo y minuto a las escenas y frases que no lo tengan, y
   comprueba que cada enlace de vídeo existe.
4. **Tamaños reales**: en `referencias.json`, mide `ancho` y `alto` con la API de
   la wiki (o bajando la imagen); cambia los enlaces muertos y sube las mejores
   imágenes nuevas de las hojas (quedan 20-40 entradas).
5. **Lo que el buscador no alcanzaba**: licencias de Sketchfab por su API,
   letras comprobadas con `fontTools`, Reddit por Arctic Shift, webs oficiales y
   entrevistas que antes daban 403.
6. **Los ⚠️**: resuelve todos los que puedas. Lo que siga dudoso, déjalo con ⚠️
   y di por qué.
7. **Los conceptos de lámina**: si las imágenes nuevas dan una pose u objeto
   mejor, cámbialo en los 3 conceptos (con el número de hoja o el enlace).

## Cómo dejarlo escrito

- **Edita en su sitio**, sección por sección, y guarda tras cada una. No
  reescribas lo que está bien ni cambies el orden de las secciones.
- Cambia el recuadro «Cómo se hizo» del principio: di que hubo segunda pasada
  con la red abierta (fecha) y qué se pudo usar.
- Justo debajo, añade **«Segunda pasada · qué cambió»**: lo corregido (antes →
  ahora), lo añadido, y los ⚠️ que había y los que quedan.
- Amplía la «Bitácora de búsqueda» con un apartado de la segunda pasada.

## Al terminar

Contesta sólo con **5 líneas**: la serie; hojas y referencias nuevas; ⚠️ antes →
después; la corrección más importante; si cambió algún concepto de lámina.
