# ENCARGO DE TEMA — volverse experto en un tema, para sus proyectos

Eres una sesión de Claude Code en la nube. Tu trabajo es **investigar un tema a
fondo** y dejar un informe que otra sesión, en su PC, usará para trabajar como
experta. Lee `contexto/proyectos.md`: son los proyectos del dueño, y todo lo que
investigues tiene que servirle a alguno de ellos.

## Qué investigar (con detalle concreto, fechas y fuentes; nada genérico)

1. **El estado del arte en 2026**: qué se usa hoy de verdad, qué cambió en el
   último año, qué quedó viejo. Con fecha de cada dato.
2. **Herramientas**: programas, servicios, modelos, repositorios de GitHub,
   skills y servidores MCP de Claude. Para cada una: qué hace, precio o
   licencia, si corre en Windows con una RTX 4060 Ti de 8 GB, y si toca red o
   pide claves. Marca las gratuitas.
3. **Cómo se hace, paso a paso**: los flujos de trabajo que usan los
   profesionales, con los comandos o menús concretos.
4. **Trampas y errores comunes**: lo que falla y cómo se evita.
5. **Referentes**: profesionales, canales de YouTube, cursos, comunidades,
   sobre todo **hispanohablantes y latinoamericanos**, con enlace.
6. **Ejemplos buenos**: casos reales que funcionaron y por qué.
7. **Cómo se aplica a SUS proyectos**: qué haría un experto con lo que él tiene
   (ver `contexto/proyectos.md`); ideas concretas, ordenadas por impacto.
8. **Lo que no se puede o no conviene**: límites legales, de licencias o de
   plataforma, para no perder tiempo.

Verifica lo importante en dos fuentes. Si algo no lo pudiste confirmar, dilo.

## Profundidad exigida: hasta el último rincón

No te quedes en la primera página de resultados. **Mínimo 40 fuentes distintas**
por encargo, y de todos estos tipos (si alguno no existe, dilo):

- **Oficiales**: web y redes oficiales, entrevistas al staff (director, diseñador
  de personajes, director de arte, compositor), artbooks, *making of*, notas de
  producción, comentarios de los Blu-ray, blogs de desarrollo de los juegos.
- **En otros idiomas**: busca también **en japonés, inglés y coreano o chino**
  si la obra viene de ahí (las entrevistas originales suelen no estar traducidas).
- **Wikis de fans** (Fandom y las de cada idioma), **TV Tropes**, y para
  videojuegos **The Cutting Room Floor** (contenido descartado, textos y
  frases de betas y prototipos) y **Wayback Machine** para páginas borradas.
- **Foros y comunidades**: Reddit (si reddit.com no responde, usa el archivo
  público de Arctic Shift: `https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=<sub>`),
  foros especializados, Discords públicos con registros, 4chan/archivos si hace
  falta un dato, Tumblr y X/Twitter de artistas del staff.
- **Arte**: Pixiv, ArtStation, DeviantArt, Pinterest (para encontrar la fuente
  original, nunca como fuente final).
- **Vídeo**: análisis en YouTube, vídeos de staff, tendencias de TikTok, con el
  **minuto exacto**.
- **Código y recursos**: repositorios de GitHub (letras, herramientas, mods,
  shaders, extractores de recursos), Sketchfab, bancos de texturas.
- **Doblaje latino**: Doblaje Wiki (por su API), ANMTV, entrevistas a los
  actores latinos en YouTube, créditos de Crunchyroll y Netflix Latinoamérica.

Al final del dossier añade **«Bitácora de búsqueda»**: las búsquedas que hiciste
(con el idioma), las fuentes consultadas y lo que NO encontraste. Distingue
siempre lo **confirmado** (dos fuentes) de lo **dudoso**.

## Dónde dejarlo

En `investigaciones/<tu-tema>/`, sin tocar otras carpetas:
- `informe.md`: el informe completo, en español, **claro para leer en el
  celular**, con índice arriba y fuentes enlazadas.
- `recursos.json`: las herramientas y fuentes, cada una con `nombre`, `url`,
  `tipo`, `precio`, `licencia` y `para_que`.

Si eres parte de un equipo (EQUIPO.md), **no uses git**: lo sube el jefe. Sólo
una sesión que trabaje sola hace commit y push **de su rama**. No toques `main`
ni otras carpetas.
No instales nada fuera de la sesión ni publiques nada en ningún sitio.
