# Texto, juegos y técnica · El castillo ambulante (Howl's Moving Castle, 2004)

Investigador de texto/juegos/técnica. Puntos 5, 6, 11, 18, 24 y 25 de `ENCARGO.md`.
Parte de `partes/datos-texto.md` (staff, obras relacionadas AniList, buscador de Steam vacío) y no repite esas consultas.
Es una libreta de datos: un dato por línea, con fuente(s) y ✅/⚠️.

## Punto 5 · Tipografía

**El logo no es una fuente: es caligrafía de encargo**
- El logo japonés 「ハウルの動く城」 está escrito a mano por el **productor Toshio Suzuki**, no compuesto con una fuente. Es la misma persona que rotula a mano varios títulos de Ghibli (p. ej. *La tumba de las luciérnagas* no, pero sí *El cuento de la princesa Kaguya* y el eslogan de *El viento se levanta*); el resto de logos de Ghibli usan mincho o gótica normal, según el propio Suzuki citado en un blog de tipografía · [iwademo.cocolog-nifty.com, 30-may-2006](http://iwademo.cocolog-nifty.com/blog/2006/05/post_ea88.html) · ⚠️ (una fuente, pero cita directa de Suzuki: «『もののけ姫』が宮崎駿の、『ハウルの動く城』が鈴木敏夫の書き文字で»)
- Comparación: el logo de *La princesa Mononoke* está escrito a mano por **Hayao Miyazaki** mismo (mismo blog) ⚠️ — útil para la biblia 100 si la lee el redactor.
- No encontré (tras buscar) un análisis de la fuente del logo internacional (el de Disney/Toho en inglés): no hay entrada en Fonts In Use para el póster oficial de estudio.

**El póster alternativo de Mondo (2013, NO es el oficial de estudio)**
- El grabado (screenprint) de **Olly Moss** para Mondo usa **Friz Quadrata** en el título grande y, con reservas del propio artículo («difícil de identificar con certeza»), algo parecido a **Kennerley** en los créditos pequeños · [Fonts In Use](https://fontsinuse.com/uses/5479/howl-s-moving-castle-movie-poster) ⚠️ (una fuente, y es un póster de coleccionista, no el cartel de Ghibli/Toho/Disney) — **no usar como «la» tipografía de la serie**, sólo como referencia de que existe una versión con letra clásica serif.

**Texto que sí aparece dentro de la película** (ver punto 6 para el detalle)
- Un cartel de reclutamiento **en alemán**, «**Mut und Willenskraft**» (coraje y fuerza de voluntad), visible en el fondo de una escena de calle · [ghibli.fandom.com/wiki/Ingary](https://ghibli.fandom.com/wiki/Ingary) (wikitext, cita el archivo `Hauro_plakat.jpg`) + búsqueda cruzada que referencia el mismo cartel · ✅ (dos fuentes) · imagen real 179×340 px: `https://static.wikia.nocookie.net/studio-ghibli/images/2/21/Hauro_plakat.jpg`

**Letras libres candidatas (todas comprobadas con `fontTools` para tildes, ñ, ¿ y ¡: las 5 las traen completas, comprobado por mí, no de memoria)**
- **UnifrakturMaguntia** (Google Fonts, OFL) — gótica alemana; para el «cartel del mundo» tipo el de «Mut und Willenskraft» o cualquier rótulo militar/propaganda de Ingary.
- **IM Fell English** (Google Fonts, OFL) — serif de imprenta antigua con irregularidades; para carteles, periódicos o letreros de tienda de la Europa de attrezzo de la película (Market Chipping, Porthaven).
- **Cormorant Garamond** (Google Fonts, OFL) — serif francesa elegante; para el título o subtítulos de la lámina, en el espíritu de Colmar (Alsacia) que inspiró los fondos (ver punto 18).
- **Sacramento** y **Yellowtail** (Google Fonts, OFL/Apache) — manuscritas; para imitar el gesto de una firma o logo caligrafiado a mano (evocando el logo real de Suzuki, sin copiarlo).
- Verificación hecha con este script (todas devolvieron «ninguno», es decir, tienen los 10 caracteres pedidos):
  `TTFont(path).getBestCmap()` comprobando á é í ó ú ñ Ñ ¿ ¡ ü en las 5 TTF descargadas de Google Fonts.

**No hay manga de la película**: está basada en una novela de prosa (Diana Wynne Jones, sin ilustraciones de globos), así que no existe un «globo normal/grito/pensamiento» oficial de la franquicia como en un manga. El equivalente oficial más cercano es el **Film Comic** (ver punto 6).

## Punto 6 · Cómo hablan y piensan en pantalla

**El equivalente oficial a un manga: el Film Comic de VIZ**
- VIZ Media publicó **4 tomos** de «Howl's Moving Castle Film Comics» (desde agosto de 2005): fotogramas reales de la película recortados y montados en viñetas, con **globos de diálogo, onomatopeyas y cartelas añadidos encima** — es el único «cuadro de diálogo» oficial con forma de manga que tiene esta película · [VIZ: catálogo](https://www.viz.com/read/film-comic/howl-s-moving-castle-film-comics/all) + [Simon & Schuster, ficha del tomo 1](https://www.simonandschuster.com/books/Howls-Moving-Castle-Film-Comic-Vol-1/Hayao-Miyazaki/Howls-Moving-Castle-Film-Comics/9781421500911) ✅ (dos fuentes)
- Público objetivo declarado: 12-17 años (ficha de VIZ). Formato: fotograma real + globo dibujado encima, no arte original de línea.

**Texto real dentro de la propia imagen (lo que sirve para un «cartel del mundo»)**
- Cartel de propaganda **en alemán**, «Mut und Willenskraft» — ver punto 5. ✅
- **Panfletos de propaganda enemigos**, lanzados desde dirigibles bombarderos: caen sobre Porthaven tras un ataque naval, y vuelven a caer sobre los barcos de guerra que regresan dañados · [Ingary](https://ghibli.fandom.com/wiki/Ingary) + [Porthaven](https://ghibli.fandom.com/wiki/Porthaven) + [Battleship](https://ghibli.fandom.com/wiki/Battleship) (las tres páginas del wiki lo describen de forma consistente) ✅ (tres fuentes) — no encontré una captura legible del texto de los panfletos, sólo que existen y son enemigos.
- **Idioma oficial de Ingary: inglés**, con palabras sueltas en **alemán y francés** metidas en la ambientación, sobre todo en la cafetería Cesari's (de raíz francesa, coherente con que el pueblo está inspirado en Colmar, Alsacia) · [ghibli.fandom.com/wiki/Ingary](https://ghibli.fandom.com/wiki/Ingary) ✅ (coherente con el punto 18, dos fuentes independientes: la página del mundo y la de producción)
- **No hay subtítulos ni cartelas de traducción dentro de la versión japonesa original** (no es una serie con capítulos titulados como Evangelion o AoT): no encontré ninguna cartela de texto propia del anime salvo el cartel alemán y los panfletos.
- Un objeto de guion con texto pero **no verificado visualmente**: el contrato mágico entre Howl y Calcifer y la maldición de la Bruja del Páramo son **habladas**, no se ven escritas en pantalla (a diferencia de, por ejemplo, un grimorio con texto legible) — búsqueda hecha, no lo encontré como texto en pantalla, así que no lo afirmo.
- Pensamientos: no hay convención visual propia (nube, letra especial) porque la película no usa voz en off de pensamiento; se transmite por interpretación actoral, no por texto — confirmado por la ausencia de cualquier mención en el wiki a un recurso de «pensamiento en pantalla».

## Punto 11 · Videojuegos de la franquicia

**No existe un videojuego oficial de El castillo ambulante.** Comprobado a fondo, no es pereza:
- El artículo completo de Wikipedia en inglés sobre la película (26.305 caracteres) **no menciona ni una vez** «video game», «Namco» ni «game» — lo comprobé descargando el extracto completo y buscando esas palabras por Python.
- Una búsqueda inicial devolvía un supuesto «juego de PS2 de Namco (2004)», pero las dos únicas páginas que lo describen son **wikis explícitamente de contenido inventado**: la *Video Games Fanon Wiki* y la *Idea Wiki* de Fandom (son wikis para juegos que fans proponen o imaginan, no para juegos reales). Es una confusión, no un dato — no lo pongo en la biblia como real.
- MobyGames da error de Cloudflare (dos intentos, según la norma); no pude confirmarlo por ahí tampoco.
- Lo más cercano real: **Ni no Kuni**, la saga de Level-5, con **animación hecha por Studio Ghibli** y música de **Joe Hisaishi** — pero es un proyecto aparte, sin personajes ni mundo de El castillo ambulante · [Wikipedia: Ni no Kuni](https://en.wikipedia.org/wiki/Ni_no_Kuni) + cobertura de prensa (GamesRadar, Kotaku) ✅ — lo anoto como dato de estudio, no de esta franquicia.
- Consecuencia: no hay interfaz, menú ni caja de diálogo de videojuego propia de esta serie que describir. Si al dueño le interesa un «cuadro de videojuego» para esta lámina, no puede salir de un juego real de Howl's Moving Castle porque no existe.

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Referencias e influencias que el propio Miyazaki reconoce**
- Viaje de investigación a **Colmar (Alsacia, Francia)**, sugerido por el distribuidor francés de Disney para *El viaje de Chihiro*: el equipo visitó el castillo de **Haut-Kœnigsbourg** y observó a artesanos locales (sombrereros, herreros) — de ahí Market Chipping y Porthaven · [ghibli.fandom.com/wiki/Howl's_Moving_Castle](https://ghibli.fandom.com/wiki/Howl%27s_Moving_Castle) (cita a su vez «The Anime Art of Hayao Miyazaki», Dani Cavallaro, 2006, ISBN 978-0-7864-5129-6) ✅ (dos fuentes)
- Influencia declarada: el ilustrador y novelista francés **Albert Robida** (1848-1926), rival de Julio Verne, por su mezcla de romanticismo retrofuturista y rigor técnico ✅ (misma fuente citada arriba, dos referencias independientes dentro del mismo artículo).
- Influencia declarada para el diseño del castillo: el escultor suizo **Jean Tinguely** (esculturas cinéticas de chatarra) — el castillo se concibió enteramente de chatarra, pasarelas y una boca que escupe vapor ✅.
- Nº de patas del castillo: se probaron piernas humanas; la versión final usa **patas de ave**, y se fijaron en **4** porque, según el productor Toshio Suzuki, era «más práctico (y barato) de dibujar» ✅.

**Cómo se hizo técnicamente (máquinas: el propio castillo)**
- El diseño pintado del castillo se **escaneaba** y se **dividía en piezas pequeñas** (cuanto más pequeñas, más preciso el movimiento de la textura), recompuestas como un mosaico con **Adobe Photoshop** ✅.
- Esas piezas se **montaban sobre un polígono base con Softimage** (software 3D), cuidando el orden de superposición; el movimiento del castillo se inspiró en una **mochila de excursionista llena de utensilios colgando** para lograr el bamboleo asimétrico (a propósito distinto de la simetría occidental) ✅ (misma fuente, sección «Production» del wiki, que cita «Hayao Miyazaki Zensho», Seiji Kano, 2006, ISBN 4-8459-0687-2).

**Software de estudio: Toonz / OpenToonz**
- Ghibli usa una versión propia, muy personalizada, del software italiano **Toonz** (Digital Video S.p.A.) desde *La princesa Mononoke* (1997) para entintado y coloreado digital y composición; **El castillo ambulante** está nombrado explícitamente entre las películas que lo usaron, junto con *El viaje de Chihiro*, *Ponyo*, *El cuento de la princesa Kaguya* y *El viento se levanta* · [Wikipedia: Toonz](https://en.wikipedia.org/wiki/Toonz) + [Cartoon Brew](https://www.cartoonbrew.com/tech/heres-download-opentoonz-studio-ghiblis-free-animation-software-138465.html) + [SiliconANGLE](https://siliconangle.com/2016/03/21/studio-ghibli-animation-software-platform-toonz-sees-open-source-release/) ✅ (tres fuentes)
- En 2016 Dwango liberó el software como **OpenToonz**, gratis y de código abierto, en colaboración con Ghibli y Digital Video · [GitHub oficial](https://github.com/opentoonz/opentoonz) ✅ — **se puede instalar de verdad** para probar el flujo de entintado digital que usó la propia película (2D, con nodos de efectos).

**Color y compuesto digital (para el «shader» y el brillo de Calcifer)**
- La directora de color **Michiyo Yasuda** probó Calcifer con **luz de fuego verdosa** en el arte conceptual; se descartó porque ese verde se reflejaba en las caras de los personajes y les daba un tono raro, así que volvieron al color natural del fuego · [ghibli.fandom.com/wiki/Calcifer](https://ghibli.fandom.com/wiki/Calcifer) (cita «The Art of Howl's Moving Castle», p.79-80) ✅ (fuente primaria citada + el libro existe, confirmado en venta por VIZ)
- El **director de imagen digital Atsushi Okui** explica que Calcifer necesitó tres procesos digitales: **suavizado (softening), transparencia y difusión** como fuente de luz — la referencia técnica exacta para replicar su brillo con un *glow*/*bloom* en Photoshop o un nodo de emisión + *subsurface* en Blender ✅ (misma página, cita directa).
- El **animador supervisor Takeshi Inamura** cuenta que Miyazaki le pidió que Howl fuera «desenfadado» en la escena en que cruza el cielo con Sophie, y que ahí entendió cómo debían cambiar las expresiones de Howl en la segunda mitad de la película — dato útil para «encuadres y qué emoción va en cada uno» ✅.
- El **director de arte Yôji Takeshige** (supervisado por **Noboru Yoshida**) cuenta que un primer diseño de la casa de Jenkins en Porthaven se rechazó por colores «demasiado apagados, incongruentes con los personajes» — muestra el proceso real de iteración de fondos, no llegar a la primera ✅.

**Sonido y atmósfera (breve, apoya el «cómo se siente» del estilo)**
- En octubre de 2003 Ghibli mandó un equipo a Europa a grabar sonido ambiente «puro»: pisadas, carruajes de caballos sobre adoquín, cafés y calles — para el «siglo XIX imaginario» de la película ✅ (misma página wiki, sección Sound Mixing).

**Cómo replicarlo en Photoshop y Blender (síntesis mía a partir de lo anterior, marcado como propuesta)**
- **Línea**: Ghibli no usa contorno duro tipo cómic; en Blender, Freestyle o Grease Pencil con grosor variable fino, sin negro puro (gris muy oscuro), imitan mejor el entintado con Toonz que un contorno tipo Solidify.
- **Sombreado**: dos tonos (luz/sombra) planos, sin degradado duro — el color lo decide Michiyo Yasuda «a mano» por escena, no una fórmula fija; conviene tomar el hex de un fotograma concreto (tarea de imagen/vídeo), no inventar paleta.
- **Fuego de Calcifer**: nodo de emisión + *volumetrics* o *glow* de compuesto en vez de partículas realistas — el propio estudio lo resolvió con «suavizado + transparencia + difusión», no con una simulación físicamente exacta.
- **Metal oxidado del castillo**: texturas CC0 de ambientCG que encajan con el aspecto de chatarra remachada: **Metal053C**, **Metal056C**, **Metal055B** (buscar por «Metal0» en `ambientcg.com`) ⚠️ (textura genérica, no del castillo real; propuesta mía).
- **Geometría base / rig de referencia (licencia libre, para no partir de cero en Blender)**: 3 modelos con licencia **CC Attribution** en Sketchfab, todos de fans, sólo como referencia de topología y proporciones (no oficiales):
  - Castillo: «Howl's moving castle» por **lsebko** — <https://sketchfab.com/3d-models/none-a5fcd7379db240bea690e4fca032e322>
  - Calcifer: «Howl's Moving Castle - Calcifer» por **ncd.blueberry** — <https://sketchfab.com/3d-models/none-2d651cf9dc2b4ef59ec7723a08a727bf>
  - El anillo mágico: «Howl's Moving Castle Ring» por **MagesOfMadness** — <https://sketchfab.com/3d-models/none-8cbdfa9c498a4d1a9e8c4995aec67d3a>
  - Todos con licencia **CC Attribution** (crédito al autor obligatorio), comprobado en la API de Sketchfab (`api.sketchfab.com/v3/search`) ✅.

## Punto 24 · Obras parecidas y temas relacionados

**La trilogía literaria (mundo compartido, no traducida siempre igual)**
- *Howl's Moving Castle* (1986) → *Castle in the Air* (1990, sigue a Abdullah, mismo mundo, cameo de Sophie/Howl) → *House of Many Ways* (2008, cameo de Sophie/Howl/Calcifer; la maestra de Suliman y Howl, la señora Penstemmon, también se menciona ahí) — se conoce como **«The Castle Series»** o **«World of Howl»** · [Wikipedia: Castle in the Air](https://en.wikipedia.org/wiki/Castle_in_the_Air_(novel)) + [Wikipedia: House of Many Ways](https://en.wikipedia.org/wiki/House_of_Many_Ways) + [howlscastle.fandom.com](https://howlscastle.fandom.com/wiki/Castle_Series) ✅ (tres fuentes)
- Ninguna de las dos secuelas tiene película: sólo la primera se adaptó.

**Recomendadas por usuarios de AniList** (ya en `datos-texto.md`, no repetido aquí: Spirited Away, Kiki's Delivery Service, Castle in the Sky, Princess Mononoke, Nausicaä, When Marnie Was There, The Boy and the Heron, The Wind Rises, Princess Jellyfish, **The Ancient Magus' Bride**, Porco Rosso, Suzume, Violet Evergarden, Ponyo, **Witch Hat Atelier**) — de estas, *The Ancient Magus' Bride* y *Witch Hat Atelier* son las que más comparten el tono «magia doméstica, aprendiz, maestro raro».

**Listas de prensa** (coinciden entre sí en el núcleo Ghibli, y aportan fuera de Ghibli):
- Dentro de Ghibli: *Spirited Away*, *Castle in the Sky*, *Kiki's Delivery Service*, *My Neighbor Totoro*, *Ponyo*, *Princess Mononoke* — repetido en casi todas las listas · [CBR](https://www.cbr.com/best-anime-movies-like-howls-moving-castle/), [Collider](https://collider.com/movies-like-howls-moving-castle/), [SlashFilm](https://www.slashfilm.com/679249/movies-like-howls-moving-castle-that-are-definitely-worth-watching/) ✅
- Fuera de Ghibli y fuera de Japón: **The Triplets of Belleville** (Francia/Bélgica/Canadá, animación excéntrica con estética steampunk-retro, 2 nominaciones al Óscar) — la comparación más «no obvia» y potencialmente útil para inspirar look de lámina distinto a lo Ghibli-genérico · [SlashFilm](https://www.slashfilm.com/679249/movies-like-howls-moving-castle-that-are-definitely-worth-watching/) ⚠️ (una lista, criterio editorial)
- También mencionadas: *Song of the Sea*, *Okko's Inn* ⚠️ (una fuente cada una).

**Encargos hermanos de este mismo lote** (para que el redactor no repita ideas de lámina): 98-el-viaje-de-chihiro, 100-la-princesa-mononoke, 101-your-name-cielos-y-ciudades y 102-el-estilo-ghibli-en-general están en investigación en paralelo. Comprobado: **ninguno tiene `biblia.md` todavía** (sólo carpetas `partes/`), así que no hay conceptos de lámina ya fijados con los que chocar; avisar al redactor para que los revise cuando existan.

## Punto 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo, en cinco líneas**
1. **Ingary** es una monarquía constitucional (rey + primer ministro + un ministro de defensa) con tecnología a vapor (tranvías, coches, kayaks voladores, acorazados) que además depende de brujas y magos de corte, con la hechicera **Suliman** al mando · [ghibli.fandom.com/wiki/Ingary](https://ghibli.fandom.com/wiki/Ingary) ✅
2. La magia funciona por **pactos personales**, casi siempre con demonios: se entrega algo vital (un corazón) a cambio de poder; romper el pacto puede liberar o destruir a las dos partes (el trío Howl/Calcifer/Sophie) ✅
3. La puerta del castillo tiene un **selector de color junto al pomo**: girarlo a un color abre a una ciudad distinta al instante — la «máquina» central de la película (tabla completa abajo) ✅
4. Las identidades son fluidas: Howl usa varios alias (**Pendragon**, **Jenkins**) para esquivar la llamada a filas del rey ✅
5. El reino está en guerra con un reino vecino por la desaparición de un príncipe; el armamento a vapor **no puede con la magia** del enemigo, y la guerra termina de golpe por un acuerdo diplomático entre el príncipe enemigo y Suliman ✅
(Fuente de las 5: [ghibli.fandom.com/wiki/Howl's_Moving_Castle](https://ghibli.fandom.com/wiki/Howl%27s_Moving_Castle) + [Ingary](https://ghibli.fandom.com/wiki/Ingary) + [Howl's Castle](https://ghibli.fandom.com/wiki/Howl%27s_Castle), las tres coherentes entre sí)

**El objeto-máquina más citable: la puerta con el selector de color**
| Color | Antes de mudarse | Después de mudarse |
|---|---|---|
| Verde | El Páramo (Waste) | El Páramo |
| Rojo | Kingsbury | Jardín secreto de Howl (rosa en la peli) |
| Azul | Porthaven | Porthaven |
| Amarillo | (no usado antes) | Market Chipping |
| Negro | El portal de Howl (Gales) | El portal de Howl |
Fuente: tabla completa en [ghibli.fandom.com/wiki/Howl's_Castle](https://ghibli.fandom.com/wiki/Howl%27s_Castle) (compara libro y película; aquí sólo la versión película) ✅. **Es un candidato fuerte para «un objeto real en un sitio real» en Blender**: una puerta con un dial de colores, follaje real delante, luz que cambia según el color activo.

**La historia por arcos** (condensado del resumen de la wiki, que a su vez sigue los créditos/capítulos internos del artículo, no la propia película)
1. **Encuentro casual**: Sophie, sombrerera de 18 años, conoce a Howl; la Bruja del Páramo la maldice a los 90 años.
2. **La maldición indeleble**: Sophie huye a el Páramo, entra al castillo, pacta con Calcifer y conoce a Markl.
3. **La decisión de Sophie**: el rey llama a Howl a la guerra; Sophie se hace pasar por su madre ante la corte en Kingsbury.
4. **Enfrentamiento con Suliman**: la Bruja del Páramo pierde su poder; el hechizo de Sophie flaquea un instante por amor; Suliman intenta atrapar a Howl con un anillo de Star Children.
5. **Amor de guerra**: Howl se transforma en un ave-monstruo para intervenir en la guerra, cada vez con más riesgo de no volver a ser humano; bombardeo de la casa; Sophie destruye el castillo para salvar a Calcifer.
6. **El niño que se bebió las estrellas**: Sophie viaja al corazón de Howl con el anillo mágico, ve el pacto original con Calcifer (una estrella fugaz), le devuelve el corazón a Howl, besa al espantapájaros (que era el príncipe desaparecido) y termina la guerra.
Fuente: [ghibli.fandom.com/wiki/Howl's_Moving_Castle](https://ghibli.fandom.com/wiki/Howl%27s_Moving_Castle), sección «Plot» ✅ (estructura propia del artículo, contrastable con el resumen oficial de Ghibli/Disney en la sinopsis de AniList ya recogida en `datos-texto.md`).

**Vocabulario y símbolos que un fan reconoce**
- **Ingary**: nombre del reino, inspirado en la isla sueca **Ingarö** ✅ (wiki, trivia).
- **The Waste** (el Páramo): la tierra baldía fuera de las ciudades, hogar de la Bruja y punto de partida del castillo.
- **Star Children** (星の子, Hoshi no Ko): espíritus-estrella fugaz; Calcifer fue uno; Sophie conserva el pelo gris-estrella tras enterarse. Lectura simbólica de un fansite francés: Miyazaki invierte el significado habitual de la estrella (normalmente = esperanza) · [nota en ghibli.fandom.com/wiki/Star_Children](https://ghibli.fandom.com/wiki/Star_Children), citando a Buta Connection ⚠️ (una fuente, fansite).
- **Turnip Head / Kakashi no Kabu** (かかしのカブ): el espantapájaros con cabeza de nabo, en realidad el príncipe Justin bajo maldición; se rompe el hechizo con un beso.
- **Anillo mágico**: regalo de Howl a Sophie que brilla y guía de vuelta al castillo y, en el clímax, hasta el corazón de Howl.
- **Las Botas de Siete Leguas** (Seven-League Boots): objeto mágico mencionado (Sophie y Michael/Markl las usan para intentar atrapar una estrella fugaz) — no encontré página propia en el wiki para más detalle; búsqueda hecha, sin resultado adicional. ⚠️
- **Buques de guerra Ingary inspirados en acorazados franceses pre-dreadnought** (casco «tumblehome»), con nombre de ejemplo el *Charles Martel* — dato de diseño «máquinas de guerra» pedido por el encargo · [ghibli.fandom.com/wiki/Battleship](https://ghibli.fandom.com/wiki/Battleship) ✅

**Lectura simbólica de la guerra (fuente académica + prensa, dos tipos de fuente distintos)**
- Ensayo académico (Japanese Studies, revista *ejcjs*, Akimoto): lee a **Howl como objetor de conciencia pacifista**, **Sophie como el Artículo 9** (pacifismo absoluto) de la Constitución japonesa, **Calcifer como las Fuerzas de Autodefensa** (atado por un contrato que las limita) y **Suliman como EE. UU.** presionando para el rearme — lectura de posguerra sobre Japón, no confirmada por Miyazaki en persona · [japanesestudies.org.uk/ejcjs](https://www.japanesestudies.org.uk/ejcjs/vol14/iss2/akimoto.html) ⚠️ (una fuente, interpretación académica, no declaración del autor)
- Miyazaki, pacifista declarado, empezó a adaptar la historia durante la invasión de Irak de 2003 y metió temas de guerra que no estaban en la novela original; ha dicho que es su película favorita entre las suyas y que esperaba que en EE. UU. se recibiera mal por su crítica a la guerra · [CBR](https://www.cbr.com/howls-moving-castle-hayao-miyazaki-film-depict-pacifism/) + [Hornet](https://hornet.com/stories/howls-moving-castle-anti-war/) ✅ (dos fuentes independientes)
- Imagen citada por varios medios: **un campo de flores bajo la sombra de máquinas de guerra** — el «campos» que pide el encargo, leído como el imperialismo destruyendo la paz ✅ (mismas dos fuentes de prensa).

## Lo mejor para la lámina
- **La puerta con el selector de color**: el objeto-máquina más fiel a la serie, perfecto para Blender (un dial con 4-5 colores, follaje real delante, luz que cambia).
- El cartel en **alemán** «Mut und Willenskraft» y los panfletos de propaganda: para un fondo con texto real del mundo, no un cartel inventado.
- Letra: **UnifrakturMaguntia** para cualquier «cartel del mundo» (rótulos, propaganda) e **IM Fell English** para texto largo tipo periódico o letrero de tienda; ambas con tildes, ñ, ¿ y ¡ comprobadas.
- El Film Comic de VIZ como única referencia oficial de «cómo se ve un diálogo en viñeta» de esta película, si hace falta un recurso tipo manga.
- Calcifer: replicar su brillo con «suavizado + transparencia + difusión» (la fórmula real del estudio), no una llama realista de simulación.

## No encontré
- Fuente clara de la tipografía del logo internacional (inglés) de estudio: sólo hay análisis del póster alternativo de Mondo (Olly Moss, 2013), que no es el oficial. Busqué en Fonts In Use (sin más entradas para esta película) y por WebSearch en inglés.
- Un videojuego oficial de esta franquicia: confirmado que no existe tras comprobar el artículo completo de Wikipedia (sin la palabra «game») y descartar dos wikis de contenido inventado (Fandom Idea Wiki y Video Games Fanon Wiki). MobyGames y TCRF bloqueados por Cloudflare (dos intentos cada uno, según la norma de no insistir más).
- TV Tropes (`tvtropes.org/pmwiki/pmwiki.php/Anime/HowlsMovingCastle`): bloqueado por Cloudflare directo y también por el lector `r.jina.ai` («bloqueado hasta 2035 por sospecha de DDoS»); sólo pude usar fragmentos que WebSearch mostró de rebote (el dato del cartel «Mut und Willenskraft» venía citado ahí). ⚠️ Si el redactor tiene acceso a TV Tropes desde otra IP, merece la pena revisarlo entero.
- The Cutting Room Floor (TCRF): sin página para esta obra (no es un videojuego); confirmado indirectamente porque no hay videojuego que analizar.
- El texto exacto de los panfletos de propaganda que caen sobre Porthaven y sobre los barcos: sé que existen (tres fuentes) pero no el contenido legible.
- Confirmación con una segunda fuente de que el logo de «El castillo ambulante» es letra de Suzuki Toshio (sólo un blog, aunque cita sus propias palabras).
- Fuente sobre qué tipografía usan los subtítulos oficiales en español o inglés de los Blu-ray/streaming (GKIDS, Disney): no hay ficha técnica pública que la identifique.

## Bitácora
- Español: no hice búsquedas en español para este rol (los términos técnicos de tipografía/software se buscan mejor en inglés; el doblaje latino es del rol de voz).
- Inglés (WebSearch, ~10 búsquedas): tipografía del logo/póster, Toonz/OpenToonz, videojuego oficial, film comic VIZ, alegoría de guerra, Ni no Kuni, TV Tropes/TCRF (sin resultado directo), listas de «obras parecidas».
- Japonés (WebSearch, 2 búsquedas + 1 WebFetch directo al blog): ロゴ フォント タイトル, 鈴木敏夫 書き文字; confirmado con `iwademo.cocolog-nifty.com`.
- Red directa (curl/Python, sin gastar cupo de buscador): API de `ghibli.fandom.com` (unas 20 páginas: película, novela, Calcifer, Howl, castillo, Ingary, Suliman, rey, Witch of the Waste, Turnip Head, Star Children, Market Chipping, Porthaven, Kingsbury, Battleship, Flying Battleship, Magic Ring, imageinfo de 8 imágenes), API de Sketchfab (modelos CC), API de ambientCG (texturas CC0), API de Fontsource + descarga directa de 5 TTF de Google Fonts + `fontTools` para comprobar tildes/ñ/¿/¡, Wikipedia API (extracto completo del artículo del filme, para descartar el videojuego).
- Bloqueados (403/Cloudflare, dos intentos cada uno, según la norma): `tvtropes.org`, `tcrf.net`, `mobygames.com`.
- No repetí: AniList (obra, staff, obras relacionadas), Fandom/Safebooru/Wallhaven/Openverse ya en `datos-texto.md` y `datos.json`.

## Cumplimiento de mis puntos (5, 6, 11, 18, 24, 25)
| Punto | Estado | Por qué |
|---|---|---|
| 5 · Tipografía | ⚠️ | Logo JP (caligrafía de Suzuki) con una fuente; logo internacional no identificado (no encontré); 5 letras libres elegidas y comprobadas con fontTools (tildes/ñ/¿/¡ completas) |
| 6 · Cuadros de diálogo | ✅ | Sin manga propio, pero cubierto con el Film Comic oficial de VIZ + el cartel alemán real + los panfletos, con fuentes cruzadas |
| 11 · Videojuegos | ✅ (negativo justificado) | Comprobado a fondo que no existe un juego oficial; documentado el porqué y las dos wikis de fan-fiction que causaban la confusión |
| 18 · Estilo y técnica | ✅ | Software (Photoshop, Softimage, Toonz/OpenToonz), influencias declaradas (Robida, Tinguely, Colmar), citas de making-of (Yasuda, Okui, Inamura, Takeshige), propuesta de réplica en Photoshop/Blender con modelos CC de Sketchfab y texturas CC0 |
| 24 · Obras parecidas | ✅ | Trilogía literaria, recomendaciones de AniList y de prensa, influencias del autor, y aviso sobre los 4 encargos hermanos de Ghibli en curso |
| 25 · Mundo y símbolos | ✅ | 5 reglas del mundo, tabla completa de la puerta-selector, arcos de la historia, vocabulario, y dos lecturas simbólicas de la guerra (académica y de prensa) |
