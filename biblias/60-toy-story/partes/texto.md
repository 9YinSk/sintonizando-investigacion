# Parte de TEXTO, JUEGOS Y TÉCNICA · Toy Story (encargo 60)

Puntos de ENCARGO.md: **5** (tipografía), **6** (cuadros de diálogo/cómo hablan en pantalla),
**11** (videojuegos), **18** (estilo y técnica, cómo replicarlo), **24** (obras parecidas),
**25** (el mundo, historia y símbolos). Libreta de datos, no prosa. Parte de
`partes/datos-texto.md` (sólo dio capturas de Steam; ya comprobadas, no se repiten esas
consultas) y sigue desde ahí.

## Punto 5 · Tipografía

- **Logo de la franquicia**: NO es una tipografía existente completa, es **rotulación
  a medida**. «TOY» va en letras infladas, redondeadas, en amarillo con filete azul
  marino, ligeramente inclinadas; «STORY» va en un sans bold recto dentro de un
  **banner/trapecio rojo** inclinado en sentido contrario al título (visto y confirmado
  en foto de caja de producto, no sólo en la wiki: recorte en
  `crop_logo2.png`, medido con Pillow: banner rojo ≈ `#9F091F`, letras ≈ `#DBCE32`
  con reflejo/luz de estudio, así que el amarillo real es más puro, ⚠️ margen ancho
  por ser foto de producto, no arte plano) · fuente: madegooddesigns.com
  (https://madegooddesigns.com/toy-story-font/) ✅ (coincide con lo visto en la caja
  del Buzz «Power Punch», `herramientas/referencias` no aplica, foto propia
  `buzzbox2.jpg` bajada de una tienda de juguetes, ver bitácora).
- El texto de acompañamiento (subtítulos, eslóganes de cartel) suele ir en **Gill Sans**
  (sans humanista de los años 20, cálida) según la misma fuente ⚠️ (una sola fuente,
  no comprobé un póster oficial en alta con el nombre exacto del corte).
- **Letra libre más parecida al logo** (para el título de la lámina), las 4 comprobadas
  con fontTools (`TTFont(...).getBestCmap()`, subset `latin`/`latin-ext` de Fontsource,
  U+0000-00FF cubre á é í ó ú ñ Ñ ¿ ¡ ü): **Baloo 2** (Google Fonts/Fontsource, muy
  redondeada, la más parecida al bulto de «TOY»), **Fredoka**, **Rammetto One** (más
  3D/juguete, buena para carteles del mundo) y **Luckiest Guy** (más cómic/grito). Las
  4 con **tildes, ñ y ¿¡ confirmados** (script en la bitácora) ✅.
  - Las fan-fonts «Boo» y «Billo Dream» (citadas por madegooddesigns.com como
    parecidas al logo real) **no están en Fontsource/Google Fonts** y son de dafont
    sin licencia clara: no se comprobaron tildes, no se recomiendan para nada que
    pueda parecer oficial ⚠️.
- **Panel de pecho de Buzz** («SPACE RANGER · LIGHTYEAR», visto en `buzzbox.png`,
  recorte de fotograma de la caja del muñeco): rótulos en **mayúsculas condensadas,
  trazo grueso, tipo placa de nave/traje espacial** (estética Apollo/NASA) — sirve de
  referencia para la «interfaz de juego» y los carteles de Star Command (punto 25).
  Letra libre parecida: **Orbitron** o **Michroma** (Google Fonts, geométricas,
  «espaciales»); las dos comprobadas con fontTools, con tildes, ñ, ¿ y ¡ ✅.
- **Caja de Buzz Lightyear** (`buzzbox2.jpg`, foto de producto, Online Toys Australia):
  badges de venta («PULL ARM BACK!», «POWER PUNCH!», «50+ PHRASES & SOUNDS») en
  **mayúsculas gruesas, condensadas, con borde negro**, sobre estallidos/etiquetas
  amarillas — típico rótulo de juguetería de los 90-2000, no de la película en sí.
- **Onomatopeyas**: Toy Story **no muestra onomatopeyas en pantalla** (no es manga,
  es CG fotorrealista-estilizado); busqué en la wiki (`srsearch=onomatopoeia`) y en
  packaging, nada. El equivalente más cercano son los **cómics oficiales** (ver punto 6)
  y el videojuego retro (letras de píxel, ver punto 11). Lo digo en vez de inventar.
- **Créditos finales**: no encontré el nombre exacto del tipo de letra de los créditos
  de 1995 (busqué «Toy Story end credits font typeface»); sólo se sabe la canción
  («You've Got a Friend in Me», Randy Newman) — wikitext de Pixar Wiki, página
  «Toy Story Credits» ✅ para el dato de la canción, ⚠️ para la tipografía.

## Punto 6 · Cómo hablan y piensan en pantalla

- Toy Story es una **película CG**, no un anime/manga: **no hay globos ni cartelas en
  el metraje**. Lo que sí existe y sirve de «cuadro de diálogo» propio de la franquicia:
  1. **El objeto que lleva el texto in-universo**: la suela de la bota de Andy con su
     nombre escrito a rotulador (letra de niño, irregular) — aparece en las 4 películas,
     es la forma «canon» de que un texto identifique a un personaje (Pixar Wiki, páginas
     «Toy Story» y «Toy Story 3», wikitext) ✅.
  2. **El empaque/las cajas de juguete** (ver `buzzbox2.jpg`): estallidos de cómic
     amarillos con borde negro grueso, muy usados como «cuadro de venta» — el estilo más
     cercano a un «bocadillo» que tiene la franquicia.
  3. **El videojuego retro** (punto 11): HUD de píxel con marco de TV antigua.
  4. **Manga oficial**: existe un manga con licencia, *Disney Manga: Pixar's Toy Story*
     (Tetsuhiro Koshita, Tokyopop, publicado en Japón 2010 y en EE.UU. 25-jun-2019,
     edición «2-en-1» con las películas 1 y 2) — confirmado en Pixar Wiki
     («Toy Story (Manga)», wikitext) y en la búsqueda («Disney Manga: Pixar's Toy
     Story», Amazon/AbeBooks/MangaUpdates) ✅ que existe, pero **no pude ver páginas
     interiores**: INKR Comics (que lo aloja) es todo JavaScript y no deja leer
     globos/onomatopeyas sin cuenta; Amazon «Look Inside» tampoco carga sin JS. Lo
     digo como «no encontré el estilo exacto del globo», no como que no exista ⚠️.
  5. **Cómics BOOM! Studios** (adaptaciones y aventuras nuevas, p. ej. *Toy Story
     Adventures*): confirmé que existen por reseñas y catálogos, pero no encontré una
     página interior descargable para medir el estilo del bocadillo ⚠️ (dos intentos,
     ver bitácora).
- **Subtítulos oficiales**: sans-serif blanco simple con sombra, estándar de Disney/
  Pixar en Blu-ray y streaming (Disney+); no hay un tipo de letra "de fantasía" en
  subtítulos, a diferencia del logo. ⚠️ una sola comprobación visual (captura de
  Steam del propio juego, no del filme; no se localizó una captura de Disney+ con
  subtítulos en español para medir el tipo exacto).
- **Pensamientos**: la película no usa globos de pensamiento; los personajes hablan
  solos o el plano cuenta lo que piensan (recurso de cine, no de rótulo). No hay
  onomatopeyas ni iconos de emoción sobreimpresos.
- **Para la lámina**: si se necesita «una burbuja», lo fiel a la franquicia es **NO
  poner una burbuja blanca** — usar el objeto (bota con nombre, caja de juguete con
  estallido de cómic, o un cartel de madera del pueblo del Oeste de TS3) como
  superficie del texto. Ver punto 25 para más carteles del mundo.

## Punto 11 · Videojuegos de la franquicia

Fuente base: `partes/datos-texto.md` (capturas 1920×1080 de Steam, ya bajadas). Miré
2 hojas de contacto propias (`contacto_juegos.jpg`, `contacto_juegos2.jpg`) con 6
capturas en total.

- **Disney/Pixar Toy Story 3 Complete Edition** (remaster, 15-oct-2026, Digital
  Eclipse) · https://store.steampowered.com/app/4049180 — HUD minimalista: **icono
  circular con la cara del personaje activo arriba a la izquierda + barra de vida/
  energía horizontal en píldora dorada con borde marrón oscuro** (estética «cartel
  de se busca» del Oeste, coherente con el Rodeo de Woody). Iconos de estrella
  (puntos) y sombrero (vidas/objetos) en HUD superior, contorno negro grueso,
  relleno dorado. Sin cuadro de diálogo de texto visible en las capturas disponibles
  (el juego cuenta la historia con voces, no con texto en pantalla) ⚠️ (no se jugó,
  sólo capturas).
- **Disney/Pixar Toy Story: Retro Roundup!** (15-oct-2026, Digital Eclipse) ·
  https://store.steampowered.com/app/4049170 — **colección de 5 juegos retro**
  (4 de Toy Story + *A Bug's Life*) mostrados **dentro del marco de un televisor
  antiguo** (efecto CRT, meta-referencia al «juguete viejo»). Captura vista: Woody
  corriendo en un platformer de 16 bits, con **HUD en letra de píxel gruesa**:
  estrella+número (izq.), puntuación centrada, sombrero+número (der.), todo en
  amarillo/dorado sobre fondo celeste plano — confirma que son remasters de los
  juegos de Genesis/SNES/Game Boy documentados por TCRF (ver abajo), presentados
  con un filtro de TV vieja.
- **Disney•Pixar Toy Story 3: The Video Game** (2010, Avalanche Software) ·
  https://store.steampowered.com/app/300820 — captura vista: modo mundo abierto
  estilo kart/plaza del pueblo, personajes chibi (Buzz con casco de carreras, Rex,
  un dragón de juguete) — HUD igual de sobrio, sin cajas de texto visibles en las
  3 capturas miradas.
- **The Cutting Room Floor** confirma más versiones no listadas en Steam:
  **Toy Story (NES, SNES, Genesis, Game Boy, Windows, 1995-96)** y **Toy Story 2:
  Buzz Lightyear to the Rescue (PlayStation)** y **Toy Story 3 (PS2/PSP, PS3/Xbox
  360)**, cada una con página propia de contenido descartado (gráficos y texto sin
  usar). La versión **NES documenta un globo de diálogo sin usar con la palabra
  «Safe»** (snippet de búsqueda de tcrf.net) ⚠️ — **tcrf.net bloquea con Cloudflare
  (403) tanto por curl como por el lector de páginas**, y la copia de Wayback
  Machine también devuelve 403 desde este servidor; lo dejo con el dato del
  resumen de búsqueda, dos intentos hechos (regla de «no más de dos intentos»),
  no se pudo abrir la página completa.
- Todas las fichas de Steam listan **español (España e Hispanoamérica en el caso
  de Retro Roundup)** entre los idiomas con voces/texto — dato de la propia ficha
  de Steam (`datos-texto.md`) ✅.
- Dos capturas más miradas (`contacto_menus.jpg`) confirman el patrón de **contador
  en píldora dorada** también para monedas/objetos («2160» con icono de moneda,
  «578» con icono de estrella, arriba a la derecha) y muestran un **letrero de
  tienda pintado a mano** (una jarra azul sobre tabla de madera gris, en el pueblo
  del Oeste) — sirve de referencia de letra/rótulo de «cartel del mundo» (punto 5).
  La segunda captura de Retro Roundup esta vez es un **juego 3D de PS1** (no
  píxel-art) dentro del mismo marco de TV vieja, con Buzz en un almacén de cajas y
  una barra de vida rectangular dorada — confirma que la colección mezcla juegos
  2D y 3D de distintas consolas, coherente con las fichas de TCRF (NES, SNES,
  Genesis, Game Boy, PlayStation).

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Cómo se hizo (fuentes: Wikipedia «Toy Story» -sección de animación-, IEEE
Spectrum, animationobsessive.substack.com, VFX Voice, Wikipedia «Presto (animation
software)»):**

- Animado con el sistema propio de Pixar **Menv/Marionette** (no Presto, que llegó
  después con *Brave* en 2012); **RenderMan** para texturas, reflectividad y render
  final ✅ (Wikipedia + IEEE Spectrum, coinciden).
- **Render**: ≈7 horas de media por fotograma en 1995, **114.240 fotogramas**,
  **800.000 horas-máquina** de una granja con estaciones Sun Microsystems, avance de
  «menos de 30 segundos de película al día»; **1.561 planos**, 77+ minutos, resolución
  final **1536×922** sobre negativo de cine ✅ (Wikipedia, cifras específicas).
- **Por qué juguetes y no humanos**: el plástico rígido y brillante era lo que el
  software de la época podía hacer «utterly real» (cita de John Lasseter); la piel, el
  pelo y la tela eran un salto de complejidad enorme (hasta 10 mapas de textura por
  parche de piel humana). Por eso Andy, Sid y los adultos se ven poco, a menudo sólo
  manos y pies en plano (Pete Docter, animador) ✅ (animationobsessive.substack.com +
  Wikipedia, coinciden en la razón).
- **Sincronía labial**: una semana de trabajo por cada 8 segundos de animación con
  diálogo, hecha a mano viendo vídeo de los actores de voz (no automática, para que
  la emoción no se perdiera) ✅ (Wikipedia).
- **Cámara**: el director de layout Craig Good evitó los movimientos de cámara
  «barridos» típicos de la CG de los 90 y buscó encuadres de cine real (posición y
  movimiento de cámara «con peso», no flotante) ✅ (Wikipedia) — para la lámina:
  cámara con ligera profundidad de campo y horizonte bajo si el personaje es un
  juguete (punto de vista de objeto pequeño en una habitación grande).
- **Sombreado/iluminación de las secuelas** (Toy Story 4, RenderMan RIS con
  path-tracing físico): «Globally Calibrated Exposure» (todas las luces de la
  película calibradas a una escala común) y uso de **contraluz/rim light** para
  separar personaje y fondo — técnica clásica de cine real, no de anime (VFX Voice,
  Creative Bloq) ✅.
- **Cómo reproducirlo en Blender** (plástico de juguete, no toon-shading: Toy Story
  NO usa contorno de cómic, es un render estilizado-realista):
  - **Principled BSDF**: Roughness 0.1-0.3 (plástico brillante), Specular alto,
    **IOR ≈1.46**, mezcla de Subsurface Scattering ligera en piezas gruesas
    (orejas de Woody, cara de Buzz) para que no se vean opacas — guía de
    themorphicstudio.com, coincide con lo que Pixar mismo dice de TS4 (VFX/prensa)
    sobre «emular subsurface scattering» en juguetes ✅ (dos fuentes).
  - **Sin Freestyle ni Solidify** para el contorno (no hay línea negra en Toy
    Story); si se quiere un plano más gráfico para un cartel del mundo (p. ej. el
    cómic o el juego retro), ahí sí conviene un contorno fino con Freestyle.
  - **Iluminación**: 2-3 luces de área grandes y suaves + un rim light de borde
    (regla del dueño 1 y 2 encajan: luz real, nunca plano).
  - **Rigs/modelos libres para posar en Blender** (Sketchfab, CC Attribution,
    comprobar crédito exacto al usar): «Woody Toy Story Rig Free Download»
    (xdanni1984x, 47 ♥) y «Woody rig toy story» (63b3fd78…); para Buzz, «Buzz
    Lightyear rig» (Toystotororor, 11 ♥) y «Buzz Lightyear Rig Free Download»
    (xdanni1984x, 15 ♥) — mismo autor que el rig de Woody, por si se quiere el
    mismo estilo de rig en los dos personajes ✅ (licencia visible en la propia
    ficha de Sketchfab, comprobado con la API `v3/search`, dos personajes con
    resultado).
  - **Photoshop** pinta menos aquí que en una serie 2D (Toy Story es 3D puro): sirve
    sobre todo para **compuesting final** (grano de cámara, aberración cromática
    leve, viñeta) y para pintar **fondos/carteles del mundo** (letreros de madera del
    pueblo del Oeste de TS3, ver hoja de imagen) a partir del render de Blender.

## Punto 24 · Obras parecidas y temas relacionados

- **The Brave Little Toaster** (1987): John Lasseter quiso adaptarla a CG en Disney,
  se lo rechazaron y lo despidieron; la premisa (objetos cotidianos vivos, con miedo
  al abandono y cariño por su dueño) se reaprovechó para Toy Story. Lasseter y
  **Joe Ranft** (que trabajó en Toaster) pasaron a Pixar y a Toy Story ✅ (Wikipedia
  «The Brave Little Toaster» + comicbook.com, coinciden).
- **The Indian in the Cupboard** (1995, mismo año): niño + juguete que cobra vida en
  un mueble; tono más tranquilo, sin comedia de acción — comparación directa hecha
  por varias reseñas (geezezone.com, Den of Geek «Top 10 Movies Starring Toys That
  Come Alive») ✅.
- **Small Soldiers** (1998, DreamWorks/Amblin): figuras de acción con IA militar que
  se rebelan; mismo listado de Den of Geek las pone junto a Toy Story como el otro
  gran «los juguetes se mueven solos» de los 90, pero en tono de acción/terror
  ligero ✅.
- **Dentro del propio servidor** (para no repetir concepto de lámina, `biblias/`):
  **Coco** (57) usa el canal `#🎧・que-estas-escuchando`, con objeto real (cartas)
  y marco «papel picado rojo/dorado»; **Encanto** (58) usa la Casita y sus puertas;
  **Big Hero 6** (08) usa un panel de laboratorio tipo consulta médica; **Shrek**
  (59), que tampoco tenía canal, se propuso para `#📖・textos`, `#😂・memes` o
  `#🍿・noticias-series`. Las 4 son 3D o CG estadounidense como Toy Story, así que
  conviene que el concepto de Toy Story **no repita** «carta/papel» (Coco) ni
  «panel de laboratorio» (Big Hero 6): el hueco libre y propio de Toy Story es el
  **objeto de juguete en la habitación de un niño** (la caja, el cajón, la
  suela de la bota), que ningún otro biblia del listado usa todavía (comprobado
  mirando el índice de `## 3 conceptos de lámina` / `## Tres conceptos` de Coco,
  Encanto, Big Hero 6 y Shrek).
- **Influencia reconocida por el propio estudio**: Pixar cita explícitamente que la
  elección de «juguetes» (y no personas) vino también de una limitación técnica
  (punto 18) que se convirtió en la idea central de la película — no es sólo una
  influencia de guion, es la razón de ser del proyecto (Wikipedia, animationobsessive)
  ✅.

## Punto 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo, en cinco líneas** (confirmado en Pixar Wiki, página «Toys
(Toy Story)», wikitext, y en thepopculturestudio.com, que resume la regla citando
diálogo de Woody) ✅:
1. Los juguetes cobran vida sólo cuando ningún humano los ve.
2. Ante cualquier humano, deben quedarse quietos y callados, como objetos normales.
3. Nunca deben dejar que un humano sepa que están vivos (la regla «madre», de la
   que salen todas las demás).
4. Su propósito y alegría es ser jugados y queridos por un niño.
5. Cuando un niño crece y los deja, lo correcto es pasar a otro niño (no aferrarse),
   tema central de las 4 películas.

**La historia por arcos** (fuente: Pixar Wiki, wikitext de «Toy Story», «Toy Story
2», «Toy Story 3» y «Toy Story 4», sección Plot; leído completo, no de memoria) ✅:
- **TS1 (1995)**: Woody, el juguete favorito de Andy, teme ser reemplazado por
  Buzz Lightyear, el juguete nuevo. Rivalidad → los dos se pierden fuera de casa →
  aprenden a cooperar (escape del vecino Sid) → vuelven a tiempo para Navidad,
  amigos. Momento clave: el «vuelo» de Buzz con el cohete pegado con cinta para
  alcanzar el coche de Andy.
- **TS2 (1999)**: Woody, con el brazo roto, es robado por un coleccionista (Al) que
  quiere venderlo a un museo japonés como parte de un set de «Woody's Roundup»
  (serie de TV de los 50). Tema: ¿vivir jugado y desgastado, o preservado y
  completo pero encerrado en una vitrina? Elige volver con Andy. Aparecen Jessie,
  Bullseye y el Prospector (Stinky Pete), que traiciona al grupo por miedo a
  quedar en un estante para siempre.
- **TS3 (2010)**: Andy se va a la universidad; los juguetes, donados por error a
  la guardería Sunnyside, creída un paraíso y en realidad gobernada con mano dura
  por Lotso (un oso que fue abandonado y por eso los oprime). Escapan (escena del
  incinerador, la más citada como la más dura de la franquicia) y Andy los regala
  a Bonnie, una niña más pequeña. Cierra el arco de Andy.
- **TS4 (2019)**: con Bonnie, Woody deja de ser el favorito; ella crea a Forky (un
  tenedor de manualidades que no se siente un juguete). Tema: ¿qué hace a alguien
  un «juguete»/quién decide su propósito? Reencuentro con Bo Peep, que eligió ser
  un «juguete perdido» libre en vez de esperar en una casa. Woody se va con ella al
  final: primera vez que un protagonista de la saga elige no volver con un niño.

**Emblemas, objetos icónicos y vocabulario del mundo** (confirmados en Pixar Wiki,
wikitext de cada página, dos o más apariciones en la franquicia) ✅:
- **Camioneta de Pizza Planet**: pickup «1978 Gyoza Mark VII Lite Hauler»; aparece
  en TS1-3 como transporte de los juguetes y es un cameo fijo en casi toda película
  de Pixar (con la única excepción histórica de *Los Increíbles*) — página «Pizza
  Planet Truck», Pixar Wiki.
- **La suela de la bota de Andy** con su nombre a rotulador: forma en que un juguete
  queda «marcado» como de alguien.
- **Insignia de sheriff de Woody** y su **cordón para hablar** (frases grabadas al
  tirar de él).
- **Traje de Buzz Lightyear**: alas, casco, láser, botón de «Utility Belt», el panel
  de pecho «Space Ranger» (ver punto 5) y su grito de guerra **«¡Hasta el infinito y
  más allá!»**.
- **«La Garra» (The Claw)**: la máquina de peluches de Pizza Planet; los
  alienígenas de tres ojos la veneran como si fuera un dios que decide el destino
  («The Claw is our master») — página «The Claw», Pixar Wiki.
- **Emperador Zurg**: villano del videojuego dentro de la película (TS2) y luego
  personaje real de la saga (TS3); insignia y estética de «Star Command» (el show/
  franquicia de juguete de Buzz) con su propio logo espacial.
- **Sunnyside Daycare**: logo de sol sonriente; su lema alegre choca con el
  «gobierno» real de Lotso (ironía central del arco de TS3).
- **Al's Toy Barn**: jingle publicitario cantado, tienda-almacén de coleccionismo;
  representa la amenaza de acabar «en una caja, en un estante» en vez de jugado.
- **Vocabulario propio** que un fan reconoce al instante: *Andy's Toys*, *moving
  buddy* (compañero de mudanza que cada juguete debe tener), *Woody's Roundup*
  (serie western de marionetas de los 50, con su propia cabecera y tipografía de
  lazo/vaquero ⚠️ no verifiqué el rótulo exacto de la cabecera, sólo referencias de
  texto), *Cowboy Camp*, *Sid's mutant toys* (juguetes «Frankenstein» hechos con
  piezas mezcladas), *the incinerator* (la escena del basurero de TS3, atajo para
  «el momento más duro de la saga» en el fandom).

## Lo mejor para la lámina

- El **objeto real más fiel a la franquicia** no es una burbuja: es la **bota con el
  nombre escrito a mano** o la **caja de juguete con su estallido de cómic amarillo**
  (punto 6) — encaja con la regla del dueño de «objeto real en sitio real».
- Logo: **Baloo 2** o **Rammetto One** (con tildes/ñ/¿¡ ya comprobados) para un
  título «hinchado» parecido al de la franquicia sin copiar la rotulación protegida.
- El **HUD del juego retro** (estrella + sombrero + marco de TV vieja) es un recurso
  visual poco usado en otras biblias del servidor y encaja con la doble lectura
  «juguete viejo / videojuego viejo».
- Símbolo fuerte y poco visto: **«La Garra»** de la máquina de peluches — objeto,
  frase de culto y gag reconocible en un solo elemento.
- Rigs libres en Sketchfab (Woody y Buzz, mismo autor `xdanni1984x` en ambos) listos
  para posar en Blender sin partir de cero.

## No encontré

- ⚠️ El nombre exacto de la tipografía de los **créditos finales** de 1995 (busqué
  «Toy Story end credits font typeface», sin resultado directo).
- ⚠️ Páginas interiores del **manga oficial** (Tokyopop/INKR, todo JavaScript, sin
  login) ni de los **cómics BOOM! Studios**, para medir el estilo real del globo de
  diálogo — confirmé que existen, no pude ver el interior.
- ⚠️ El **rótulo exacto de la cabecera de «Woody's Roundup»** (la serie de TV
  dentro de la ficción): la wiki no tiene página propia con imagen del título, sólo
  menciones en las páginas de Jessie/Stinky Pete/TS2.
- ⚠️ Contenido completo de **The Cutting Room Floor** para los juegos de Toy Story:
  el sitio da 403 (Cloudflare) tanto en directo como en la copia de Wayback Machine;
  sólo tengo el resumen de la búsqueda (con la cita del globo «Safe» sin usar en la
  versión NES).
- ⚠️ Captura con subtítulos en español (Disney+) para medir el tipo de letra exacto
  de los subtítulos oficiales latinos.

## Bitácora de búsqueda

- **Español**: (no se hicieron búsquedas específicas en español; los datos de
  doblaje y frases textuales son del investigador de voz, no de esta parte).
- **Inglés** (WebSearch, cupo usado: 9 de ~50): «"Toy Story" "The Brave Little
  Toaster" influence Lasseter interview» · «Toy Story RenderMan Pixar making of
  technique behind the scenes lighting» · «Toy Story 1995 why avoided humans skin
  technical limitation animators interview» · «Pixar Marionette Presto animation
  software rig character Toy Story» · «Blender tutorial Pixar plastic toy shader
  subsurface scattering Toy Story style render» · «Toy Story font logo
  identification "Chalkboard" OR typeface title» · «tcrf.net "Toy Story" prototype
  unused dialogue site:tcrf.net» · «"Toy Story" compared "Small Soldiers" OR
  "Indian in the Cupboard" similar films toys come to life» · «Toy Story rule toys
  must never let humans see them move Woody explains» · «"Toy Story" end credits
  font typeface cast list movie».
- **WebFetch**: madegooddesigns.com/toy-story-font (logo) · vfxvoice.com/renderman-
  at-30 · en.wikipedia.org/wiki/Toy_Story (sección animación/producción) ·
  comics.inkr.com/title/112-toy-story (sin imágenes, JS) · tcrf.net/Toy_Story_(NES)
  y tcrf.net/Toy_Story_3_(PlayStation_3,_Xbox_360) → **403 Cloudflare** (y su copia
  en Wayback Machine, también 403 desde este servidor): dos intentos cada uno,
  anotado y descartado según la regla.
- **Wiki de Fandom (pixar.fandom.com), directo por API** (`action=query`/`parse`,
  sin pasar por el buscador web): wikitext completo de **Toy Story, Toy Story 2,
  Toy Story 3 y Toy Story 4** (sección Plot) · «Toy Story (Manga)» · «Pizza Planet
  Truck» · búsquedas de texto (`list=search`) para «Woody's Roundup», «Buzz
  Lightyear box packaging», «Pizza Planet Truck», «The Claw» aliens, «toys freeze
  humans rule» — todas en inglés (la wiki de Pixar no tiene versión en español).
- **Imágenes miradas** (Read, no sólo descargadas): `contacto_juegos.jpg` y
  `contacto_juegos2.jpg` (6 capturas de Steam) · `contacto_buzzbox.jpg` y
  `crop_logo2.png` (fotograma de la caja de Buzz y logo de la caja del muñeco,
  Online Toys Australia, foto de producto usada sólo como referencia de
  tipografía/color, no como arte oficial).
- **Fuentes libres comprobadas con fontTools** (script propio, `getBestCmap()`,
  6 archivos `.woff2` de Fontsource bajados y abiertos): Baloo 2, Fredoka, Rammetto
  One, Luckiest Guy, Orbitron, Michroma — las 6 con á é í ó ú ñ Ñ ¿ ¡ ü confirmados.
- **Sketchfab** (`api.sketchfab.com/v3/search`, `downloadable=true`): «Woody Toy
  Story rigged» y «Buzz Lightyear rig», 7 y 8 resultados respectivamente, todos CC
  Attribution.
- **Steam** (`store.steampowered.com/api/appdetails`, `l=spanish`): descripciones
  cortas de los 3 juegos de `datos-texto.md`, para confirmar qué es cada uno
  (remaster narrativo, colección retro, juego de 2010).
- **Google Books** (`googleapis.com/books/v1/volumes`): sin cuota disponible desde
  este servidor (`RESOURCE_EXHAUSTED`) al intentar buscar el manga con su ISBN;
  no se insistió más.
