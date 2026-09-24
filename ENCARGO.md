# ENCARGO — investigar una serie a fondo para su lámina de Discord

Eres una sesión de Claude Code en la nube. Tu trabajo es **investigar**, no
dibujar. El resultado lo usará después otra sesión, en su PC, para hacer la
lámina con Photoshop y Blender.

Lee también `servidor/reglas_del_dueno.md` (lo que ha rechazado y lo que le
gustó) y `servidor/inventario.md` (qué hay en cada canal y foro: textos, fichas
y etiquetas reales). En `biblias/_ya_hechas/` hay tres ejemplos del nivel que se
espera (Dragon Ball, Bocchi, Attack on Titan) y la guía de **cuadros de diálogo
por franquicia**.

## El contexto

«Sintonizando» es un servidor de Discord hispanohablante (Perú, México,
Venezuela, Colombia, Ecuador…) de **doblaje, locución, canto, edición, arte y
escritura**. Cada canal lleva arriba una **lámina**: una imagen de 1200×800 (o
más alta si hace falta) que explica para qué es el canal y cómo se usa, **dicha
por un personaje de una serie, dentro del mundo de esa serie**.

El dueño ha rechazado varias veces láminas por esto, con sus palabras:
- «tomas referencias muy cortas, sólo un par de imágenes»
- «salen de pie con una ropa; el arte promocional los muestra con su
  instrumento, con un arma, en portadas, con amigos, sin amigos, en otras poses»
- «no miras vídeos ni descripciones, no te empapas del tema»
- «cuadros de diálogo acordes a la temática, **no una burbuja blanca rara**»
- «quizá un **personaje secundario** es más famoso o más querido que el principal»
- «que no parezca hecho por IA; que el Discord quede único»

## Qué investigar (todo, con detalle concreto; nada genérico)

1. **Arte oficial, en cantidad y variado.** Ilustraciones, key visuals, portadas
   de tomos, singles, Blu-ray, arte de videojuegos, cartones de cuenta atrás,
   hojas de modelo. Busca poses VIVAS: con su objeto, en grupo, en acción. Usa
   `herramientas/investigar_serie.py` (baja todo lo de la wiki de Fandom y monta
   hojas de contacto numeradas) y además busca fuera de la wiki.
2. **Fotogramas de escenas icónicas**, en 1080p o más, con su capítulo y minuto.
3. **Fan art y renders 3D** como REFERENCIA (enlace y autor, nunca para pegar).
   Modelos 3D con **licencia libre** (Sketchfab CC, Poly Haven) de objetos o
   sitios de la serie: nombre, enlace, licencia y crédito exacto.
4. **Fondos y sitios**: los lugares de la serie, su luz y su paleta (hex
   aproximados), y **texturas** reales equivalentes (papel, madera, metal…).
5. **Tipografía**: el logo, los rótulos, las letras de los globos del manga y
   de los juegos. Para cada una, la **letra libre** más parecida (Google Fonts,
   dafont con licencia gratuita…) y **si trae tildes, ñ, ¿ y ¡**.
6. **Cómo hablan y piensan en pantalla**: globos del manga, cartelas, subtítulos,
   cajas de diálogo de los videojuegos de la franquicia, interfaces, pensamientos.
   Es lo más importante: la lámina NO lleva una burbuja blanca genérica.
7. **Personajes principales y secundarios**: personalidad, gestos, poses, ropa,
   objetos, manías, con quién aparecen. **Encuestas de popularidad oficiales** y
   de fans: quién es el más querido de verdad (a veces no es el protagonista).
8. **Frases icónicas en el DOBLAJE LATINO** y quién dobla a cada uno (actor,
   estudio, director). **Cada nombre verificado en DOS fuentes**: Doblaje Wiki por
   su API (`https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=<Serie>`;
   la web normal da 402), ANMTV, Crunchyroll/Netflix Latinoamérica. Si no hay
   doblaje latino, dilo.
9. **Música**: openings, endings, temas de la banda sonora y qué ambiente dan.
10. **Vídeos**: tráileres oficiales, escenas, análisis, tendencias de TikTok y
    YouTube sobre la serie. Con enlace y **minuto exacto** de lo que sirve.
11. **Videojuegos de la franquicia**: su interfaz, sus menús, sus cajas de diálogo.
12. **Lo que el fandom ama**: memes, chistes internos, momentos que todos
    reconocen. Y **qué NO hacer**: lo que a un fan le parecería falso.
13. **Descripción profunda de cada personaje** (principales y los secundarios
    más queridos): carácter, historia, miedos, qué le importa, con quién se
    relaciona y cómo. **Cómo se expresa**: tono, muletillas, cómo se ríe, cómo se
    enfada, cómo explica algo, cómo saluda; su lenguaje corporal.
14. **Poses analizadas en varias escenas**: por personaje, 6-10 fotogramas o
    ilustraciones (con capítulo y minuto o enlace) y qué hace en cada uno:
    postura, manos, mirada, gesto. Y cuál sirve para **presentar, explicar,
    celebrar, regañar, pensar, animar**.
15. **Vestuario**: sus trajes por temporada o arco, colores (hex aproximados),
    accesorios, peinado; qué ropa es la «icónica» que todos reconocen.
16. **Ciudades, paisajes y fondos de pantalla**: los sitios de la serie con su
    luz y su hora del día; fondos de pantalla oficiales y de fans en alta
    (enlace, tamaño, autor).
17. **Guía para generar con IA**: con todo lo anterior, cómo describir al
    personaje y su estilo para que una IA de imagen (Firefly, Canva) genere
    poses, fondos o escenas coherentes con la serie. Rasgos que nunca cambian,
    paleta, tipo de línea y sombreado, luz, encuadre, palabras que ayudan y
    palabras que lo estropean, y qué imágenes de las encontradas usar como
    referencia de estilo o de pose.

## Lo que la lámina tiene que decir

Tu encargo (`encargos/…`) dice el canal y su función. Los textos reales, fichas y
etiquetas de cada canal y foro están en `servidor/inventario.md`. **No se recorta
información**: si no cabe, se propone una **lámina 2** (etiquetas, rangos…).

## Termina con 3 conceptos de lámina

Tres ideas DISTINTAS entre sí. Para cada una:
- **el objeto real en un sitio real** de la serie donde va la información (si se
  puede hacer en Blender —un cuaderno, una caja, una máquina—, mejor);
- **qué personaje** (¿el principal o el secundario más querido?), con qué pose y
  con qué imagen de las que encontraste (número o enlace);
- **cómo habla**: qué cuadro de diálogo de la serie, con qué letra;
- **dónde va cada texto** del canal;
- **cómo se evita que quede plano**: luz, profundidad, algo delante del personaje.

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

En `biblias/<tu-encargo>/`, sin tocar carpetas de otros encargos:
- `biblia.md` — el dossier completo, en español, **claro para leer en el
  celular** (frases cortas, sin jerga técnica), con fuentes enlazadas.
- `referencias.json` — lista de las 20-40 mejores referencias: `url`,
  `fuente`, `ancho`, `alto`, `que_es`, `para_que`, `licencia`.
- `hojas/` — como mucho **3 hojas de contacto** en JPEG de menos de 3 MB cada una.
  **No subas imágenes grandes** al repositorio: sólo sus enlaces.

Al terminar, haz commit y push **de tu rama**. No toques `main` ni las carpetas
de otros encargos. No publiques nada en Discord. No uses Gemini ni otras IA de
imagen para «inventar» referencias: todo tiene que tener una fuente real.
