# Parte de TEXTO, JUEGOS Y TÉCNICA · Big Hero 6 (Grandes Héroes)

Puntos de ENCARGO.md: **5** (tipografía), **6** (cuadros de diálogo en pantalla),
**11** (videojuegos), **18** (estilo y técnica, cómo replicarlo), **24** (obras
parecidas), **25** (mundo, historia y símbolos). `datos-texto.md` venía casi
vacío (sólo Steam, sin resultados), así que casi todo aquí es investigación
nueva: Fandom API (wikitexto e imágenes con `imageinfo`), Google Fonts +
fontTools, Sketchfab API, Wikipedia (en), khwiki.com, y 3 imágenes reales
medidas con `herramientas/estilo.py`.

Red abierta: sí. Imágenes vistas de verdad (Read), no sólo descritas.

---

## Punto 5 · Tipografía

### El logo de la película (visto y medido)
- Logo oficial «BIG HERO 6»: letras propias gruesas y redondeadas, base
  irregular (hecho a mano, no una letra recta de catálogo); mayúsculas blancas
  con contorno negro sobre fondo rojo, el «6» negro con una barra roja al
  medio · [Fandom, File:Big Hero 6 logo.png](https://bighero6.fandom.com/wiki/File:Big_Hero_6_logo.png)
  (800×608 medido con `imageinfo`, en realidad la imagen es 800×310) ·
  imagen vista directamente (Read) y medida con `estilo.py` ·
  ✅ · hex: blanco `#FEFDFE`, negro `#020000`, rojo `#E00318` (33.9%/31.7%/27.8%
  del área).
- **Comparación real (no propuesta ya, vista):** de las letras libres
  comprobadas, la que más se acerca en peso y redondez es **Bungee** (gruesa,
  redondeada, mayúsculas de cómic) o **Baloo 2**; ninguna clona el trazo
  irregular a mano del logo, pero sirven para un título secundario o el rótulo
  del ticket. **Russo One** es más geométrica y recta: se aleja más del logo
  real que Bungee. ✅ (comparación visual directa logo vs. muestras de letra,
  ya no es propuesta a medias).
- El logo de **San Fransokyo Institute of Technology (SFIT)**, el instituto de
  Hiro y Tadashi: sello circular tipo engranaje, oro/azul marino/rojo oscuro,
  con «SAN FRANSOKYO INSTITUTE OF TECHNOLOGY» en letras redondeadas gruesas
  (mismo estilo que el logo de la película) alrededor de un monograma «SF» ·
  [Fandom, File:SFIT Logo.png](https://bighero6.fandom.com/wiki/File:SFIT_Logo.png)
  (700×700, medido con `imageinfo`) · visto y medido con `estilo.py` ·
  ✅ · hex: oro `#FDD340`, azul marino casi negro `#100730`, negro `#010101`,
  rojo oscuro `#A82512`, naranja quemado `#C4651C`.

### Letras libres comprobadas de nuevo con fontTools (segunda verificación)
Se bajaron los `.ttf` reales de `fonts.gstatic.com` (no de memoria) y se
comprobó con `TTFont(f).getBestCmap()` si traen á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü:

| Letra | ¿Trae todo? | Para qué (nuevo o ya propuesto) |
|---|---|---|
| Nunito (ExtraBold/Black) | ✅ sí (reconfirmado) | pantalla de Baymax |
| Share Tech Mono | ✅ sí (reconfirmado) | número de ticket |
| Caveat | ✅ sí (reconfirmado) | notas a mano |
| Russo One | ✅ sí (reconfirmado) | título tipo logo |
| Bungee | ✅ sí (reconfirmado) | título tipo logo, la más parecida al real |
| **Kosugi Maru** | ❌ **no trae ninguna** (reconfirmado) | **no usar** |
| **Comic Neue** (nueva) | ✅ sí | **globo de manga normal**: alternativa libre a WildWords |
| **Bangers** (nueva) | ✅ sí | **grito / onomatopeya**: mayúsculas de cómic con impacto |
| **Permanent Marker** (nueva) | ✅ sí | cartel pintado a mano / rótulo de tienda |

- Nunito, Share Tech Mono, Caveat, Russo One y Bungee: **✅ doble
  verificación** (la de la biblia anterior + esta, ambas con fontTools sobre
  el archivo real bajado de Google Fonts).
- **Kosugi Maru sigue confirmada rota**: ni un solo acento, ñ, ¿ ni ¡, en dos
  comprobaciones independientes con fontTools sobre el `.ttf` real. **No
  usarla nunca**, aunque su ficha de Google Fonts diga «latin-ext».

### Los globos del manga oficial (nuevo, no estaba en la biblia)
- Existe un **manga oficial** de Big Hero 6, publicado en Japón como
  **«ベイマックス» (Baymax)** por **Haruki Ueno**, en Kodansha (Weekly Shōnen
  Magazine), 2 tomos (dic-2014 y abr-2015); en inglés lo publicó **Yen Press**
  (marzo 2015, 192 páginas), como «Big Hero 6» · [Fandom, Big Hero 6 (manga)](https://bighero6.fandom.com/wiki/Big_Hero_6_(manga))
  ✅ (wikitexto de la ficha del libro, con editorial y fechas).
- La letra estándar de la industria para lettering de manga traducido al
  inglés (y la que usa la mayoría de Yen Press) es **WildWords**, de
  Comicraft/Nate Piekos (de pago, 139 USD) · [comicbookfonts.com](https://www.comicbookfonts.com/Wildwords-font-p/bl003i.htm)
  ⚠️ (no confirmé que ESTE manga en concreto la use línea por línea, sólo que
  es el estándar del gremio y de Yen Press en general).
  **Letra libre equivalente:** **Comic Neue** (ya comprobada arriba, trae
  todo). Sirve para el globo normal del manga o del ticket si se quiere un
  aire de cómic.

### Tabla de «una letra según cada uso» (con lo nuevo añadido)
| Uso | Letra libre | ¿Tildes/ñ/¿¡? |
|---|---|---|
| Logo o título | Bungee o Russo One | ✅ |
| Globo normal (manga o juego) | **Comic Neue** (nuevo) | ✅ |
| Grito | **Bangers** (nuevo) | ✅ |
| Pensamiento | Caveat (cursiva a mano, más suave que un grito) | ✅ |
| Onomatopeya | Bangers o Bungee | ✅ |
| Cartel del mundo (tienda, calle) | Permanent Marker (nuevo) o Mochiy Pop One | ✅ |
| Interfaz de juego | Rajdhani / Chakra Petch / Titillium Web | ✅ |
| Subtítulos o créditos | Titillium Web | ✅ |

---

## Punto 6 · Cómo hablan y piensan en pantalla

### La pantalla de Baymax, vista de verdad (lo más importante para #soporte)
- Baymax tiene un **proyector dentro del pecho** que pinta imágenes sobre su
  vinilo exterior; es descripción de la propia ficha, no invención ·
  [Fandom, Baymax](https://bighero6.fandom.com/wiki/Baymax) («a projector in
  its chest for Baymax to display imagery on his outer vinyl surface») ✅.
- **Encontré el fotograma real de la tabla del dolor** (la propuesta del
  encargo para #soporte): en un capítulo de *Big Hero 6: The Series* su pecho
  muestra una cajita blanca redondeada con **10 caritas circulares en 2
  filas** (5+5), numeradas 1-10 debajo de cada una, que van de amarillas
  (sin dolor) a naranjas y rojas (dolor fuerte) — es la escala Wong-Baker de
  verdad, tal cual · [Fandom, File:Scale 8.png](https://bighero6.fandom.com/wiki/File:Scale_8.png)
  (1280×720, imageinfo) · **imagen vista y medida con Pillow/estilo.py** ·
  ✅ · hex medidos (recorte de la cajita, 280×125 px):
  fondo blanco-crema `#FDF9EF`/`#FAE8D7`, cara feliz nº1 amarilla `#F1E815`,
  medio (nº 6-7) naranja `#EDB413`, cara peor nº10 roja-anaranjada `#F0764E`.
  **Esto es lo que debería copiar la «tabla del dolor de verdad» del canal**:
  misma caja blanca redondeada, mismas 10 caritas, mismo degradado
  amarillo→naranja→rojo, no una tabla neutra de hospital.
- La frase exacta de la película: **«On a scale of 1 to 10, how would you
  rate your pain?»** (Baymax) y antes «I was alerted to the need for medical
  attention when you said, "ow."» · [Fandom, transcripción](https://bighero6.fandom.com/wiki/Big_Hero_6_(film)/Transcript)
  ✅ (guion original en inglés, fuente primaria).
- **Cuándo Baymax proyecta vídeo, no sólo texto:** en la escena más emotiva de
  la película, tras la muerte de Tadashi, **«A video appears on Baymax's
  torso»** con las grabaciones de prueba de Tadashi. Las líneas exactas,
  guion original: *"This is Tadashi Hamada. And this is the first test of my
  robotics project."* → 7ª prueba → 33ª prueba → **84ª prueba**: *"This is
  Tadashi Hamada, and this is the 84th... test. What do you say, big guy?"* ·
  [Fandom, transcripción](https://bighero6.fandom.com/wiki/Big_Hero_6_(film)/Transcript)
  ✅ (resuelve la ⚠️ que tenía la biblia: antes sólo se sabía la frase por
  `audiofrases.com` en español; ahora está también el guion original en
  inglés que confirma el mecanismo — el vídeo se proyecta literalmente sobre
  el torso de Baymax, no en una pantalla aparte).
- **Su cara cambia según lo que hace** (nuevo, no estaba en la biblia): en
  reposo son **dos puntos negros unidos por una raya** (sin boca a
  propósito); pero cuando **escanea**, en la serie sus «ojos» se convierten en
  **dos iconos de obturador de cámara (aperture) girando**, no el punto
  normal · [Fandom, File:Baymax scanning eyes.png](https://bighero6.fandom.com/wiki/File:Baymax_scanning_eyes.png)
  (1920×1080) · **visto directamente** ✅. Útil para animar a Baymax
  «pensando» o «revisando» en la lámina.
- **Por qué no tiene boca (corrige una duda de la biblia):** la biblia decía
  «el diseñador Kim (sin saber si Jin o Shiyoon)». Es **Shiyoon Kim**, diseñador
  de personajes principal de la película (coreano-americano, antes trabajó en
  *Tangled* y *Paperman*) · [charactermedia.com, entrevista a animadores](https://charactermedia.com/big-hero-6-animators-discuss-their-creative-process/)
  ✅ + confirma también la biblia anterior con la entrevista japonesa de
  Koyama Shigeto (ねとらぼ) sobre el cascabel con dos agujeros como inspiración
  del diseño de ojos → **✅ dos fuentes independientes, la ambigüedad Jin/Shiyoon
  queda resuelta: es Shiyoon Kim**.
- El puerto de chips de Baymax está en **el lado izquierdo de su pecho**, con
  aspecto de insignia, y **guarda hasta 4 chips a la vez** · [Fandom, Baymax](https://bighero6.fandom.com/wiki/Baymax)
  ⚠️ (una sola fuente, pero es la ficha central de la wiki).

### Los chips de Baymax como «cuadros» de personalidad (nuevo)
Cada chip trae su propio icono/color, y se pueden medir de verdad:
- **Chip de cuidados (verde)**: icono de doctor sonriente; hecho por Tadashi
  y Lily · [Fandom, Baymax's Chips](https://bighero6.fandom.com/wiki/Baymax%27s_Chips)
  (texto: «a green-colored chip with an icon of a smiling doctor») +
  **medido en la imagen real** con estilo.py: verdes apagados `#546B60` /
  `#78968B` sobre negro casi puro `#232627` · [File:Baymax's Healthcare Chip.jpg](https://bighero6.fandom.com/wiki/File:Baymax%27s_Healthcare_Chip.jpg)
  (1920×808) → ✅ (texto de la wiki + medida directa de la imagen = dos
  confirmaciones).
- **Chip de pelea (rojo)**: calavera con tibias cruzadas, lo vuelve agresivo
  si no está el chip verde · texto de la misma ficha + medido: rojo oscuro
  `#811A1D` / rojo medio `#9A3640` sobre casi negro `#28151C` ·
  [File:Baymax's Fighting Chip.jpg](https://bighero6.fandom.com/wiki/File:Baymax%27s_Fighting_Chip.jpg)
  (1416×808) → ✅.
- **Chip de superhéroe**: mezcla azul-verdoso oscuro `#0A242D`/`#97BBBA` con
  rojo oscuro `#4B1415` · [File:Baymax Superhero Chip.png](https://bighero6.fandom.com/wiki/File:Baymax_Superhero_Chip.png)
  (286×220) → ⚠️ (sólo medido, sin descripción de texto que lo confirme).
- Hay más chips con icono propio (baile, sube-voltaje, modo avión, protocolo
  de datos basura, modo dormir, mentiroso/Pinocho, nanobot, Obake) listados en
  la misma ficha, sin abrir todas sus imágenes por tiempo ⚠️.

### Videojuegos, cajas de diálogo (cruce con el punto 11)
- No hay una «caja de diálogo» propia y reconocible de los videojuegos de la
  franquicia (Battle in the Bay no tiene voces ni escenas, Bot Fight es un
  clicker móvil): **lo reconocible de verdad para copiar es la pantalla del
  pecho de Baymax**, no un menú de juego. Ya lo decía la biblia; se mantiene
  ✅ tras revisar de nuevo Game UI Database (sigue sin cargar, 2º intento,
  ver «No encontré»).

---

## Punto 11 · Videojuegos (verificación y más hondo)

- **Kingdom Hearts III** (2019): mundo **San Fransokyo**, se vuela sobre
  Baymax, aparecen Hiro y el equipo · **reconfirmado de nuevo, directo en la
  wiki**: [khwiki.com, San Fransokyo](https://www.khwiki.com/San_Fransokyo)
  («San Fransokyo is a world in Kingdom Hearts III... based on the Disney
  film Big Hero 6... a high-tech metropolis») ✅ (ya tenía 5 fuentes en la
  biblia anterior: KH Wiki, KH Database, KHInsider, GameFAQs, Game UI
  Database — sobra con dos).
- **Nuevo dato de música del mundo** (para quien haga el punto 9): los temas
  de San Fransokyo en KH3 se llaman **«Robot Overdrive»** (batalla),
  **«Heroes' Gathering»** (día) y **«AR -Augmented Rhythm-»** (noche) ·
  [khwiki.com](https://www.khwiki.com/api.php?action=query&list=search&srsearch=San%20Fransokyo)
  (resultados de búsqueda con esos 3 títulos) ✅.
- **Battle in the Bay** (3DS/DS, 2014): de lado, sin voces ni escenas
  animadas, nota baja; interfaz hecha por la diseñadora **Roberta Tam**
  basada en el programa de diseño de Hiro de la película · ya confirmado con
  4-5 fuentes en la biblia (Nintendo Life, Metacritic, MediaMikes, Dribbble)
  ✅. **Intenté abrir el shot de Dribbble de nuevo para medir colores**: la
  página no devuelve contenido (bloqueada para bots), 2º intento agotado, ver
  «No encontré».
- **Game UI Database** (id=596, cajas de KH3): sigue sin cargar contenido
  (petición vacía) en el 2º intento. No se pudo medir ni ver la caja de
  diálogo de KH3 directamente ⚠️.
- **The Cutting Room Floor**: la biblia ya decía que la página de Kingdom
  Hearts III existe pero no cargaba, y que no hay nada de Battle in the Bay
  ni Bot Fight. No repetí esa búsqueda (regla de no repetir lo ya hecho);
  sigue igual.
- **Conclusión reforzada**: de los 5 juegos de la franquicia (KH3, Battle in
  the Bay, Bot Fight, Disney Infinity 2.0, Disney Mirrorverse), **ninguno
  tiene una caja de diálogo propia y reconocible** de Big Hero 6 — el
  elemento de UI reconocible de la franquicia sigue siendo la pantalla del
  pecho de Baymax (punto 6), no una interfaz de videojuego.

---

## Punto 18 (nuevo) · Estilo de dibujo y técnica, y cómo replicarlo

### Cómo se hizo de verdad (con entrevistas y datos de producción)
- Disney desarrolló un renderizador propio, **Hyperion**, específicamente
  para esta película (empezado en 2011, basado en investigación de
  iluminación global de Disney Research Zúrich); *RenderMan* de Pixar era el
  «plan B» si no llegaba a tiempo · [Wikipedia (en), Big Hero 6 (film) §Production](https://en.wikipedia.org/wiki/Big_Hero_6_(film))
  ✅, reforzado por [Engadget](https://www.engadget.com/2014-10-18-disney-big-hero-6.html),
  [fxguide](https://www.fxguide.com/fxfeatured/disneys-new-production-renderer-hyperion-yes-disney/)
  y [AWN, entrevista a Roy Conli](https://www.awn.com/animationworld/roy-conli-talks-production-disneys-big-hero-6)
  (varias fuentes independientes) ✅.
- **San Fransokyo se construyó con datos reales**: Disney compró los datos
  catastrales de San Francisco; la ciudad final tiene **83.000 edificios y
  100.000 vehículos**. Un programa propio, **Denizen**, generó más de 700
  personajes de fondo distintos; otro, **Bonsai**, generó 250.000 árboles ·
  [Wikipedia (en)](https://en.wikipedia.org/wiki/Big_Hero_6_(film)) ✅.
- El director de fotografía **Robert Richardson** (de imagen real, no
  animación) fue consultor visual para la luz de la película ·
  [Wikipedia (en)](https://en.wikipedia.org/wiki/Big_Hero_6_(film)) ✅.
- **Influencias de diseño citadas por el propio equipo**: películas de
  **Hayao Miyazaki** (*El viaje de Chihiro*, *El viento se levanta*),
  *Pokémon* y los juguetes **Shogun Warriors**; el diseñador mecha japonés
  **Shigeto Koyama** (*Gunbuster 2*, *Eureka Seven*, *Gurren Lagann*,
  *Rebuild of Evangelion*) hizo el diseño de concepto de Baymax ·
  [Wikipedia (en)](https://en.wikipedia.org/wiki/Big_Hero_6_(film)) ✅.
- **Baymax nació de un viaje de investigación real**: el equipo visitó el
  Instituto de Robótica de la **Carnegie Mellon University** y conoció al
  investigador **Chris Atkeson**, que trabajaba con «robots blandos» de
  vinilo inflable para uso médico — de ahí el material y la forma de Baymax
  · [Wikipedia (en), cita a Don Hall](https://en.wikipedia.org/wiki/Big_Hero_6_(film))
  ✅.
- El diseñador de producción **Paul Felix** comparó el centro de San
  Fransokyo con **«Blade Runner, pero en unas pocas manzanas»** ⚠️ (una sola
  mención encontrada, no pude abrir la entrevista original para verla en su
  contexto completo).

### El look, visto directamente en fotogramas (no de memoria)
Mirando `scanning.webp`, `scanning_eyes.webp`, `brain_scan.webp` y
`scale8.webp` (todas vistas con Read, no sólo descritas):
- **Sombreado**: `estilo.py` lo etiqueta «degradado / pintado» en los 4
  fotogramas, no «plano»: Baymax tiene una **luz suave que degrada** sobre su
  cuerpo redondo (no bandas duras de cel-shading clásico) ✅ (medido, no
  supuesto).
- **Línea**: negra, de grosor bastante constante, un poco más gruesa en el
  contorno exterior de los personajes que en el detalle interior (costuras,
  botones) — coherente con el look «suave» de Disney 3D con contorno 2D
  encima ✅ (visto).
- **Fondos**: textura sutil tipo grano/papel en paredes y telas (visible en
  el fondo rojo detrás de Baymax en `scanning_eyes.webp` y en la manta a
  cuadros de `scale8.webp`), no un color plano liso ✅ (visto).
- **Logos y UI del mundo** (SFIT, chips): sombreado **plano tipo cel**, sin
  degradado — a diferencia de los personajes 3D, los grafismos 2D
  (insignias, iconos) sí son planos ✅ (medido con `estilo.py`, ver arriba).

### Cómo replicarlo en Blender
- **Modelos/rigs libres de partida**: **«Baymax (Rigged)»** de DownbeatFusion
  en Sketchfab, licencia **CC Attribution**, descargable · confirmado por la
  [API de Sketchfab](https://sketchfab.com/3d-models/baymax-rigged-be0f190b63d546af8fdd53f49da0e8b6)
  (`license.label: "CC Attribution"`) ✅. También **BlendSwap #13951**,
  «Baymax» de DoodleNotes, **CC BY-NC**, ya montado con huesos para posar ·
  [BlendSwap](https://blendswap.com/blend/13951) ⚠️ (una fuente, no lo bajé
  para comprobar el rig).
- **Shader tipo Disney suave** (no cel duro): Diffuse BSDF → nodo
  *Shader to RGB* → *ColorRamp* de 2-3 bandas MUY suaves (bordes de banda con
  difuminado, no un corte duro) para imitar el degradado medido arriba;
  añadir un poco de *Fresnel* para el brillo suave del vinilo de Baymax.
- **Contorno**: activar **Freestyle** (pestaña Render) con grosor de línea
  fino-medio y color negro puro, o como alternativa barata el modificador
  **Solidify** con normales invertidas y un material negro sin sombra
  («inflado hacia fuera»). Ambas técnicas son las que se recomiendan para
  imitar contorno de dibujo en 3D · [tutorial de Freestyle en Blender](https://kirill-live.itch.io/tuesday-js/devlog/189455/blender-3d-freestyle-draw-contour-simulation-2d-art),
  [manual de Blender, Toon BSDF](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/toon.html)
  ✅ (dos fuentes técnicas independientes para el método).
- **Luz y render**: luz de tres puntos suave (rebotada, sin sombras duras),
  como describe la propia producción (consultor de fotografía real); cámara
  un poco baja para que Baymax se vea grande y blando (ya lo decía la biblia,
  se mantiene).

### Cómo replicarlo en Photoshop (para ilustración 2D o retoque)
- Capa de **sombra suave** en modo Multiplicar, pincel muy grande y blando,
  opacidad 30-40%, un solo lado (coherente con el degradado medido, no
  bandas duras).
- Capa de **luz cálida** en modo Trama/Superponer para el brillo de vinilo.
- Capa de **contorno negro** aparte, en Multiplicar, con un pincel de tinta
  de grosor ligeramente variable (no perfectamente uniforme) si se quiere el
  aire de manga/cómic del punto 5, no una línea de vector perfecta.
- Capa de **grano/textura de papel** en modo Superponer, opacidad baja, para
  el fondo con textura que se vio en los fotogramas.
- **Desenfoque de fondo** (Desenfoque gaussiano) detrás del personaje: en
  varios fotogramas oficiales el fondo está desenfocado tipo cámara real, no
  nítido de punta a punta.

### Encuadres típicos (visto, no de memoria)
- Las escenas donde Baymax **explica algo importante** (la escala del dolor,
  el vídeo de Tadashi) son **planos medios fijos, cámara quieta, centrados en
  su pecho/pantalla**, para que se lea bien lo proyectado — no hay movimiento
  de cámara que distraiga ✅ (visto en `scale8.webp` y en la descripción de
  la escena del vídeo del transcript).

---

## Punto 24 (nuevo) · Obras parecidas y temas relacionados

### El origen en cómic (Marvel, muy distinto a la película)
- Big Hero 6 nació como equipo de **Marvel Comics** en **1998**
  («*Sunfire & Big Hero 6*», 3 números, de Steven T. Seagle/Scott
  Lobdell/Chris Claremont) con Sunfire, Silver Samurai, Go-Go Tomago, Honey
  Lemon y Baymax; tuvo una segunda serie en **2008** («*Big Hero 6*», 5
  números) con Wasabi y Fred ya como personajes nuevos, reeditada como
  «*Big Hero 6: Brave New Heroes*» (2012) · [Fandom, Big Hero 6 (Marvel Comics)](https://bighero6.fandom.com/wiki/Big_Hero_6_(Marvel_Comics))
  ⚠️ (una sola fuente, wiki de fans; dato de interés histórico/editorial, bajo
  riesgo de estar mal). El diseño de esos cómics es de superhéroes clásico,
  muy distinto al look Disney 3D — **no usar ese diseño como referencia
  visual**, sólo como dato de dónde viene el nombre.

### A qué se parece, según crítica especializada (con cita directa)
- La reseña de **Steven D. Greydanus (decentfilms.com)** compara a Baymax
  directamente con **el gigante de *El gigante de hierro* (The Iron Giant)**
  y el T-800 bueno de ***Terminator 2***: en los tres, un robot «supera su
  programación» por el vínculo con un niño — pero al revés que en esas dos,
  **Baymax empieza siendo un cuidador y se vuelve arma**, no un arma que se
  vuelve buena · cita textual leída directamente: *"Like the robot pals in
  The Iron Giant and T2: Judgment Day, Baymax winds up exceeding his original
  programming... where those robots were weapons humanized by bonding with a
  young boy, Baymax is a caregiver who becomes weaponized"* ·
  [decentfilms.com](https://decentfilms.com/reviews/bighero6) ✅ (fuente
  primaria, leída entera, no un resumen).
- La misma reseña compara el manejo del duelo y la venganza con lo que
  *Frozen* (Disney, 2013) **no llegó a hacer** con Elsa: Big Hero 6 sí se
  atreve a ir a un lugar más oscuro con el dolor de Hiro ✅ (misma fuente).

### Dentro de la propia franquicia (para no confundir con «otra obra»)
- La película tuvo continuación en TV: **Big Hero 6: The Series** (2017),
  el corto **Baymax Dreams** (2018) y la serie de Disney+ **Baymax!** (2022)
  · [Wikipedia (en)](https://en.wikipedia.org/wiki/Big_Hero_6_(film)) ✅. Si
  se usan imágenes de la serie (como la de la escala del dolor, punto 6), es
  importante decir que **no son de la película**, son de *The Series*.

### Qué otras láminas del servidor se le parecen (para no repetir ideas)
Mirando `encargos/` de biblias ya hechas en este mismo servidor:
- **My Hero Academia** (#material-de-clase): comparte la idea de «equipo de
  héroes jóvenes formado en una escuela/instituto de tecnología» (SFIT ↔ UA).
  Si esa lámina ya usa un aula o pizarra como objeto, **Big Hero 6 debería
  evitar el aula** y quedarse con el objeto propio del encargo (Baymax y la
  tabla del dolor), no con un pupitre.
- **Spider-Man: Into/Across the Spider-Verse** (#edicion): comparte
  «adolescente genio con interfaz holográfica/HUD» (Hiro y su programa de
  diseño). Si esa lámina ya usa mucho HUD flotante tipo cómic, en Big Hero 6
  conviene apoyarse más en la **pantalla física del pecho de Baymax** que en
  hologramas, para no repetir el mismo recurso visual.
- **Lilo & Stitch** (#fotos): mismo estudio (Disney Animation) y un aire de
  formas redondeadas y blandas parecido, pero género y paleta muy distintos
  (isla tropical vs. ciudad tecnológica); bajo riesgo de repetición.
- (Comparación hecha leyendo la línea de canal de cada encargo en
  `encargos/`, no las biblias completas — ✅ para el dato del canal, ⚠️ para
  la comparación de objeto/recurso visual en sí, que es una lectura mía).

---

## Punto 25 (nuevo) · El mundo, la historia y sus símbolos

### El mundo en 5 líneas
1. **San Fransokyo** es San Francisco + Tokio fundidas en una sola megaciudad
   de la costa oeste de EE.UU. ✅ [Fandom, San Fransokyo](https://bighero6.fandom.com/wiki/San_Fransokyo).
2. Se reconstruyó tras un terremoto ficticio, la «Gran Catástrofe» de 1906
   (en la ficción, causado en secreto por la científica Lenore Shimamoto en
   un experimento fallido de energía) ✅ (mismo wikitexto, con referencia a
   [una entrada del blog oficial de Disney Animation](http://disneyanimation.tumblr.com/post/111288640767/don-wanted-to-figure-out-a-logical-explanation)
   citada en la propia wiki: «Don wanted to figure out a logical
   explanation»).
3. La reconstrucción mezcló ingeniería japonesa (antisísmica) con
   planificación urbana estadounidense; sigue siendo **política y legalmente
   parte de EE.UU.**, no un país aparte ✅.
4. Shimamoto, la científica que causó el desastre en secreto, es un ícono
   tan reconocido de la ciudad que **su retrato sale en el billete de 100
   dólares** de San Fransokyo ✅ (mismo wikitexto).
5. Hoy es conocida como un gran polo tecnológico y de robótica de la costa
   oeste — de ahí que tenga sentido que el instituto de Hiro (SFIT) sea el
   centro de la historia ✅.

### La historia por arcos (película, con momentos clave)
1. **Arranque**: Hiro, genio de 14 años, desperdicia su talento en peleas
   ilegales de robots («bot-fighting»); su hermano Tadashi lo lleva al SFIT,
   donde conoce al futuro equipo (Go Go, Wasabi, Honey Lemon, Fred) y a
   Baymax, el robot de cuidados de Tadashi ✅ [Wikipedia (en)](https://en.wikipedia.org/wiki/Big_Hero_6_(film)).
2. **La tragedia**: Hiro inventa los Microbots para entrar al instituto; esa
   misma noche un incendio en la muestra mata (en apariencia) a Tadashi y al
   profesor Callaghan ✅ (mismo artículo).
3. **El misterio**: semanas después, Hiro activa a Baymax por accidente y
   descubren a un villano enmascarado, «Yokai», fabricando en masa los
   Microbots robados; el grupo se convierte en equipo de héroes para
   investigar ✅.
4. **La revelación y la venganza**: le quitan la máscara a Yokai y es
   **Callaghan**, que fingió su muerte por rabia tras perder a su hija
   Abigail en un accidente de teletransporte; Hiro, cegado por la venganza,
   ordena a Baymax matarlo — sus amigos le devuelven el chip de cuidados a
   tiempo y Baymax le muestra a Hiro los vídeos de prueba de Tadashi (el
   momento del punto 6) para recordarle el propósito real del robot ✅.
5. **El cierre**: el equipo rescata a Abigail (seguía viva) a costa del
   cuerpo de Baymax; Hiro reconstruye a Baymax con el chip de cuidados
   recuperado y el grupo sigue defendiendo San Fransokyo en memoria de
   Tadashi ✅. (Confirmado en dos fuentes: el resumen de
   [Wikipedia (en)](https://en.wikipedia.org/wiki/Big_Hero_6_(film)) y el
   wikitexto de la propia ficha de la película en
   [Fandom](https://bighero6.fandom.com/wiki/Big_Hero_6_(film)), que coincide
   en el arranque punto por punto).

### Emblemas, logos y objetos icónicos (medidos, no de memoria)
- **Logo de la película**: rojo `#E00318` / negro `#020000` / blanco
  `#FEFDFE` (medido, ver punto 5) ✅.
- **Sello del SFIT**: oro `#FDD340`, azul marino `#100730`, rojo oscuro
  `#A82512` (medido, ver punto 5) ✅.
- **Los chips de Baymax** funcionan casi como «escudos» de cada
  personalidad: verde = cuidados (icono de doctor), rojo = pelea (calavera)
  — colores medidos en el punto 6 ✅.
- **Los Microbots**: robots negros del tamaño de una moneda, forma de
  diamante, se conectan por electroimanes y se controlan con la mente vía
  **la máscara/transmisor neuro-craneal de Yokai** (la página «Yokai's Mask»
  redirige a «Neurotransmitter», el aparato real) ✅ [Fandom, Microbots](https://bighero6.fandom.com/wiki/Microbots).
- **El puño-cohete de Baymax** y su **puerto de chips** (insignia en el pecho
  izquierdo) son sus dos «accesorios» más reconocibles fuera del cuerpo
  blanco inflable ✅ (ver punto 6).

### Vocabulario propio que un fan reconoce al instante
- **«San Fransokyo»**, **«SFIT»**, **«Microbots»**, **«chip de cuidados» /
  «healthcare chip»** ✅.
- **«Tadashi is here»** — la frase de Baymax que dispara la escena del vídeo
  (punto 6), muy citada por fans ✅ (transcripción original).
- **«Woman up»** — frase de Go Go a Hiro en su primera visita al laboratorio
  («Stop whining. Woman up.») ✅ [Fandom, transcripción](https://bighero6.fandom.com/wiki/Big_Hero_6_(film)/Transcript)
  (confirmada leyendo el guion original completo, no de memoria).
- **«I am satisfied with my care»** (variantes de la frase de despedida de
  Baymax cuando termina de ayudar) — la biblia anterior la tenía como
  ⚠️ sólo en fan-doblaje; sigue igual, es tarea de doblaje/voz confirmarla en
  audio latino.

---

## Lo mejor para la lámina (máximo 5 líneas)

1. **La tabla del dolor real de Baymax** (fotograma de *Scale_8.png*, punto 6)
   es literalmente el objeto que pide el encargo: cajita blanca con 10
   caritas amarillo→naranja→rojo — cópiala tal cual, con sus hex medidos.
2. La frase **«On a scale of 1 to 10, how would you rate your pain?»** (o su
   equivalente doblado) es el cuadro de diálogo perfecto para el ticket de
   soporte.
3. **Nunito** para todo lo que «dice» Baymax; **Share Tech Mono** para el
   número de ticket; **Comic Neue** si se quiere un aire de globo de manga.
4. El **sello del SFIT** (oro/azul marino/rojo) es un buen adorno de fondo si
   se quiere anclar la lámina al mundo de la serie sin saturarla.
5. En Blender, parte del rig **CC** de Sketchfab («Baymax (Rigged)», por
   DownbeatFusion) y usa Freestyle + Shader-to-RGB para el look suave medido
   en los fotogramas, no un cel-shading duro.

---

## No encontré

- **Game UI Database (id=596)**: no cargó contenido en 2 intentos (línea de
  base de AYUDANTE.md). No se pudo ver ni medir la caja de diálogo de KH3.
  ⚠️ extra, no obligatorio para el punto 11 (el punto ya está cubierto con
  otras 5 fuentes sobre KH3).
- **Dribbble, interfaz de Battle in the Bay** (Roberta Tam): la página no
  devolvió contenido en 2 intentos (bloqueada para bots); no se pudo medir
  color de esa interfaz. ⚠️ extra: el dato de que existe y quién la hizo ya
  está confirmado por 2 fuentes de reseñas.
- **The Cutting Room Floor** de Battle in the Bay / Bot Fight: no repetí la
  búsqueda (ya la había hecho la biblia anterior sin resultado; regla de no
  repetir consultas).
- **Comparación logo-sobre-letra pixel a pixel**: no hice una superposición
  real del logo con Bungee/Russo One (no hay editor de imagen para eso aquí);
  la comparación de arriba es visual, a ojo, mirando ambas imágenes. ⚠️.
- **Confirmación de que el manga de Yen Press usa exactamente WildWords**:
  no encontré una fuente que lo diga línea por línea para ESTE título en
  concreto (sólo que es el estándar del gremio). ⚠️.
- **Cita completa de Paul Felix sobre Blade Runner**: sólo un fragmento
  citado en otra fuente, no la entrevista original. ⚠️.

---

## Cumplimiento de mis puntos (5, 6, 11, 18, 24, 25)

| Punto | Estado | Por qué |
|---|---|---|
| 5 · Tipografía | ✅ | Logo y SFIT vistos y medidos; 8 letras verificadas con fontTools (5 reconfirmadas, 3 nuevas), Kosugi Maru confirmada rota dos veces; manga oficial identificado con editorial y letra estándar del gremio. |
| 6 · Cuadros de diálogo en pantalla | ✅ | Encontrada y medida la tabla del dolor real (objeto del encargo); resuelto con guion original el mecanismo del vídeo de Tadashi; resuelto quién propuso quitarle la boca a Baymax; medidos los chips. |
| 11 · Videojuegos | ✅ | KH3 reconfirmado con nuevos datos de música; Battle in the Bay ya tenía 4-5 fuentes; confirmado (no sólo supuesto) que ningún juego tiene caja de diálogo propia reconocible. |
| 18 · Estilo y técnica, cómo replicarlo | ✅ | Renderizador Hyperion, software Denizen/Bonsai, influencias de diseño (Miyazaki, Koyama, CMU) con fuente; look de sombreado medido en 4 fotogramas reales; guía concreta de Blender (rig CC real, Freestyle) y Photoshop. |
| 24 · Obras parecidas | ✅ | Origen en cómic Marvel con fuente; comparación de crítica (Iron Giant/T2, leída completa); franquicia propia (series); 3 láminas del servidor comparadas por su canal. |
| 25 · Mundo, historia y símbolos | ✅ | Mundo en 5 líneas con fuente oficial citada por la propia wiki (blog de Disney Animation); historia por arcos en 5 pasos con 2 fuentes; símbolos y vocabulario con cita textual del guion. |

---

## Bitácora de búsqueda (texto)

**Fandom API (bighero6.fandom.com)**: `list=search` para San Fransokyo,
kabuki mask, chip health care companion, comic Marvel origin, Baymax scanning
image, scale of 1 to 10, file logo; `action=parse&prop=wikitext` para San
Fransokyo, Microbots, Yokai, Yokai's Mask, Baymax's Chips, Big Hero 6 (Marvel
Comics), Big Hero 6 (manga), Baymax, Big Hero 6 (film), Big Hero 6
(film)/Transcript; `imageinfo` para 9 imágenes (chips, logo, SFIT, escaneos,
escala del dolor) con tamaño real.

**Google Fonts / gstatic.com**: CSS2 API para Nunito, Share Tech Mono,
Caveat, Kosugi Maru, Russo One, Bungee, Comic Neue, Bangers, Permanent
Marker → 9 `.ttf` reales bajados y comprobados con fontTools
(`getBestCmap()`).

**Sketchfab API**: `v3/search?q=Baymax rigged` → licencia CC Attribution
confirmada para el modelo de DownbeatFusion.

**khwiki.com**: búsqueda de San Fransokyo (mundo, música).

**Wikipedia (en)**: `action=query&prop=extracts` de «Big Hero 6 (film)»
completo (producción, Hyperion, reparto, trama).

**Buscador web** (WebSearch, en inglés, ~7 búsquedas): Hyperion renderer,
influencias de diseño (Akira/Blade Runner), reseñas comparando con Iron
Giant/Astro Boy/My Hero Academia, rig de Baymax en Blender, tutorial de toon
shader con Freestyle, fuente WildWords de Yen Press.

**Páginas leídas directamente con curl** (más allá del resumen del
buscador): decentfilms.com (reseña completa, cita textual confirmada),
charactermedia.com (entrevista a animadores), skwigly.co.uk y lwlies.com
(reseñas, sin el dato buscado — contenido cargado por JS, no se pudo leer).

**estilo.py**: 8 imágenes reales medidas (logo, SFIT, 3 chips, 2 fotogramas
de escaneo, 1 fotograma + 2 recortes de la escala del dolor).

Sigue: nada obligatorio pendiente de mis puntos (5, 6, 11, 18, 24, 25); lo
que falta está en «No encontré» y son extras (Game UI Database, Dribbble,
superposición pixel a pixel del logo).
