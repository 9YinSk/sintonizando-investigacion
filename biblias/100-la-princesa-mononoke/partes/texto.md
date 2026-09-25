# Parte de TEXTO, JUEGOS Y TÉCNICA · La princesa Mononoke (encargo 100)

Investigador de texto: puntos 5, 6, 11, 18, 24 y 25 de `ENCARGO.md`. Libreta de datos (no prosa), un dato por línea, con fuente y ✅/⚠️. Parte de `partes/datos-texto.md` (AniList, staff, obras parecidas de AniList) y de `biblias/100-la-princesa-mononoke/partes/datos.json`; no repite esas consultas.

## Hallazgos

### Punto 5 — Tipografía

**Créditos oficiales del logo:** «Title Logo Design» acreditado a Kaoru Mano (真野薫) y Yukari Yoshida (吉田由香里) — de `datos-texto.md`/AniList (anilist.co/anime/164/staff) · ✅ (staff oficial de AniList, dato ya recogido por `recolectar.py`, no se repite la consulta). No se encontró qué caligrafía o tipografía concreta usaron ellos (búsqueda «もののけ姫 タイトルロゴ 筆文字 デザイン 誰が書いた», japonés): el logo japonés parece caligrafía a pincel hecha a mano, no una fuente comercial — ⚠️ sin confirmar con una fuente que lo diga explícitamente.
- El logo en inglés («PRINCESS MONONOKE») del cartel de EEUU/Miramax es un grabado tipo madera/sello, muy distinto de una fuente digital estándar; en el hilo de identificación de fuentes de dafont.com (`dafont.com/forum/read/467592/princess-mononoke-title`) la comunidad identifica **Eremaeus** como similar al título de la edición FRANCESA en DVD (con **Optimus Princeps** como alternativa menos exacta) — dato de fans, sólo para el póster francés, no el japonés ni el original de EEUU · dafont.com (foro) · ⚠️ (una fuente, identificación de aficionados, y es sobre la edición francesa)
- El eslogan «生きろ。» / «Live.» (ver punto 25) se presenta en los carteles en texto grande, centrado, como frase-sello — parte de la campaña de Shigesato Itoi · ghibli.fandom.com («Advertising Slogan») · ✅
- El prólogo de apertura en la versión japonesa original se muestra como TEXTO en pantalla (no narración hablada, a diferencia del doblaje inglés que sí lo narra en voz) — confirma que la película SÍ usa cartelas de texto al menos una vez · guion transcrito (scripts.com/script/princess_mononoke_13983) + comparación de doblajes citada en TV Tropes «Opening Monologue» · ⚠️ (no verificado con fotograma exacto; el investigador de vídeo puede confirmar minuto y tipografía con `fotogramas.py` sobre la versión japonesa)
- Existe una edición oficial en manga/cómic de la película («フィルムコミック もののけ姫 完全版», Tokuma Shoten, colección Animage Comics Special, 5 tomos) que usa fotogramas reales de la película con los diálogos tipografiados encima en japonés — el formato es de «cine-cómic» (fotograma + texto), no viñetas dibujadas a mano con globos clásicos de manga · amazon.co.jp + tokuma.jp/book/b503719.html · ✅ (dato relevante también para el punto 6)

**Letra libre recomendada por uso (las 8 que pide el encargo), comprobada con fontTools que trae ñ, tildes, ¿ y ¡:**
- **Logo o título:** Yuji Syuku (Google Fonts, pincel japonés fino y elegante) · glyphs ñ/á/é/í/ó/ú/¿/¡ = **todos presentes**, comprobado con `fontTools.ttLib.TTFont(...).getBestCmap()` sobre el .ttf descargado de fonts.googleapis.com · ✅
- **Globo normal (diálogo):** Shippori Antique (Google Fonts, gótica japonesa con aire de impreso antiguo, encaja con el Japón Muromachi) · glyphs completos ✅ (mismo método)
- **Grito:** Reggae One (Google Fonts, trazo grueso y redondeado, de alto impacto) · glyphs completos ✅
- **Pensamiento:** Caveat (Google Fonts, cursiva manuscrita ligera, para pensamientos internos) · glyphs completos ✅
- **Onomatopeya:** Yuji Boku (Google Fonts, pincel de tinta grueso y enérgico, tipo sumi-e) · glyphs completos ✅ — alternativa occidental más «marcador»: Permanent Marker (glyphs completos ✅)
- **Cartel del mundo** (letreros de Tatara-ba, aldea Emishi): Rye (Google Fonts, imita madera tallada/sello, look de cartel de pueblo antiguo) · glyphs completos ✅
- **Interfaz de juego:** Zen Maru Gothic (Google Fonts, redondeada, limpia, moderna — para menús/HUD si se necesita uno ficticio, ver punto 11) · glyphs completos ✅
- **Subtítulos:** Noto Sans JP (Google Fonts, neutra, máxima cobertura de glyphs, estándar de legibilidad) · glyphs completos ✅
- **Créditos:** EB Garamond (Google Fonts, serif elegante clásica, look de títulos de crédito de cine) · glyphs completos ✅
- Todas verificadas descargando el subconjunto de fonts.googleapis.com/css2 con `text=ñáéíóú¿¡` y comprobando el cmap con fontTools — método exigido por AYUDANTE.md, no de memoria.

### Punto 6 — Cómo hablan y piensan en pantalla

- **No hay globos de diálogo en la película** (es un largometraje, no manga original): todo el diálogo es voz en off/doblaje sincronizado a labios, sin texto en pantalla salvo la cartela de apertura · visto en la trama descrita en ghibli.fandom.com + confirmado por el guion transcrito (scripts.com) · ✅
- **Cartela de apertura**: sólo en la versión japonesa original, el texto del prólogo («古代、この地は深い森におおわれ、その森の中には太古から神々が住んでいた…») aparece escrito en pantalla; en el doblaje inglés se reemplaza por narración hablada de un narrador (no acreditado como personaje) · comparación de guion/doblaje citada en TV Tropes «Opening Monologue» + guion en scripts.com · ⚠️ (falta confirmar el tipo de letra exacto de esa cartela con un fotograma; pendiente para vídeo)
- **Subtítulos**: los DVD/Blu-ray oficiales en EEUU/Reino Unido incluyen DOS pistas de subtítulos en inglés distintas — una que sigue el guion del doblaje (de Neil Gaiman) y otra con traducción más literal del japonés — un caso raro de doble subtitulado que vale la pena mencionar como referencia de «cómo mostrar dos registros de texto a la vez» · ghibli.fandom.com/wiki/Princess_Mononoke («Localization») · ✅
- **Traducción de términos propios**: el doblaje/subtítulos en inglés cambia nombres mitológicos japoneses (Jibashiri, Shishigami) por términos genéricos (Mercenary, Forest Spirit) «porque el inglés no tiene palabras para esos términos»; críticos (Michael Atkinson, Mr. Showbiz) dijeron que esto debilitó la película — dato útil para la guía de doblaje/subtítulos en español: mejor conservar términos propios con una nota, no genéricos · ghibli.fandom.com («Localization») · ✅
- **Pensamientos**: la película NO usa monólogo interior ni cajas de pensamiento en pantalla — los personajes hablan en voz alta o hay silencio (recurso más usado por Miyazaki que el texto) · deducido de la ausencia de cualquier mención a monólogo interior en la trama/guion revisados · ⚠️ (ausencia de evidencia, no confirmado explícitamente por ninguna fuente que lo niegue directamente — es lo esperable en un largometraje de este tipo)
- **Formato manga/cómic oficial** (ver punto 5): el «フィルムコミック もののけ姫» (Tokuma Shoten) tipografía el diálogo en japonés DEBAJO o AL LADO del fotograma real de la película, en cajas de texto rectas (no globos redondeados clásicos de manga dibujado) — es el modelo más fiel si se quiere un «cuadro de diálogo» propio de esta franquicia en vez de una burbuja blanca genérica: fotograma real + caja de texto rectangular con borde fino · amazon.co.jp/tokuma.jp (ver punto 5) · ✅
- **Interfaces y cajas de videojuego**: no encontré ningún videojuego oficial de la franquicia pese a buscar a fondo (ver el detalle de búsquedas en el punto 11), así que este punto no tiene material propio que mostrar — se documenta como «no encontré» y no como «no existe», siguiendo la regla de AYUDANTE.md · ver punto 11

### Punto 11 — Videojuegos de la franquicia

**No encontré ningún videojuego oficial de La princesa Mononoke.** Búsquedas hechas (español, inglés y japonés) sin resultado de un juego licenciado:
- «Princess Mononoke video game official crossover Nintendo» (inglés, WebSearch) → sin resultado oficial, sólo un video-tributo de estilo 8-bit hecho por el canal de YouTube CineFix («8-Bit Cinema»), que NO es un juego jugable, es una animación imitando el estilo retro · vice.com/en/article/a-miyazaki-masterpiece-gets-remixed-into-an-8-bit-video-game + openculture.com/2015/09 · ✅ (confirmado que es un vídeo, no un juego)
- «もののけ姫 ゲーム 公式 スタジオジブリ アプリ» (japonés, WebSearch) → ghibli.jp no lista ningún juego ni app oficial de Mononoke; sólo aparecen juegos de terceros «inspirados» en el tono del bosque (no licenciados) y el juego móvil «二ノ国：Cross Worlds» (Ni no Kuni), que es otra franquicia · ✅
- «もののけ姫 パチンコ 実機» y «スタジオジブリ パチンコ 版権» (japonés) → la máquina «フィーバーもののけ» (SANKYO, 2001) usa el mismo juego de palabras («mononoke» = yōkai/espíritu) pero NO está licenciada por Ghibli, es un tema genérico de fantasmas japoneses; se encontraron menciones sueltas de una posible «Pもののけ姫～生きろ～» en foros de rumores de nuevas máquinas (sitio con acceso bloqueado, 403, dos intentos) sin confirmación en ninguna base de datos oficial de máquinas (P-WORLD) — no se pudo verificar si es real o un montaje de aficionado, así que NO se cuenta como confirmado · sankyo-fever.jp/history + p-world.co.jp/machine/database (búsqueda sin resultado directo) · ⚠️ sin confirmar, no se incluye como dato firme
- TCRF (The Cutting Room Floor, para contenido descartado de videojuegos) devolvió error 403 (protección Cloudflare) en dos intentos (`tcrf.net/index.php?title=Special:Search&search=Ghibli` y `...search=Princess+Mononoke`) tanto por `curl` como por WebFetch — no se pudo revisar directamente; no hay indicio en ningún otro buscador de que exista una entrada de TCRF para esta película · ⚠️ bloqueado, no confirmado

**Lo más cercano (para contexto, aclarando que NO es Mononoke):**
- *Ni no Kuni: Wrath of the White Witch* (Level-5, 2011) fue una colaboración oficial con Studio Ghibli (Joe Hisaishi compuso la música, animadores de Ghibli trabajaron en las escenas animadas); la secuela *Ni no Kuni II* (2018) ya NO tuvo participación de Ghibli, aunque conservó al diseñador de personajes Yoshiyuki Momose (ex-Ghibli, animador de *Porco Rosso* y *El viaje de Chihiro*, hoy con estudio propio) y a Hisaishi · animenewsnetwork.com/news/2018-01-26 + en.wikipedia.org/wiki/NiNoKuni · ✅ — útil sólo como referencia de qué aspecto tiene una interfaz/caja de diálogo de un RPG «con aire Ghibli», no de Mononoke en concreto
- *The Legend of Zelda: Ocarina of Time* (1998) no es un cruce oficial pero Miyamoto reconoció similitudes de diseño con Mononoke (ver punto 24) — no aporta interfaz ni caja de diálogo propia de la franquicia, es sólo una influencia cruzada

**Conclusión para la lámina:** este punto no aporta material de «interfaz de videojuego» propio de Mononoke porque no existe uno licenciado; si el canal necesita una caja de diálogo con estética de videojuego, lo más fiel es inventar una interfaz nueva basada en el punto 5 (letra Zen Maru Gothic para HUD) y el punto 18 (paleta y textura), no copiar una interfaz real de otra franquicia.

### Punto 18 — Estilo de dibujo y técnica, y cómo replicarlo

**Qué técnica usó el estudio (de entrevistas y making-of):**
- Fue la última película de Ghibli animada casi enteramente con celuloide tradicional; el uso de CG en Ghibli empezó antes, en el videoclip *On Your Mark* (1995) de Chage & Aska, hecho por un estudio externo (Ghibli no tenía departamento de CG propio todavía) · ghibli.fandom.com/wiki/Princess_Mononoke («Transition to Digital») + en.wikipedia.org/wiki/Princess_Mononoke · ✅
- Se hicieron más de 144.000 celuloides (lo normal en Ghibli eran 50.000-70.000); Miyazaki supervisó y retocó a mano unos 80.000 de ellos personalmente · ghibli.fandom.com («Production») + Wikipedia EN («approximately 144,000 cels, 80,000 key animation frames») · ✅
- Animación por computadora (simulación de fluidos y partículas) sólo en 5 minutos de metraje: sangre/efectos en las criaturas y en la cara de San · ghibli.fandom.com («Transition to Digital») + Wikipedia EN · ✅
- Otros 10 minutos usaron «pintura digital» (coloreado por computadora) por lo ajustado del calendario de producción; esas partes están diseñadas para mezclarse con el dibujo tradicional, nunca sustituirlo del todo · ghibli.fandom.com («Coloring») · ✅
- El efecto de los «gusanos» que brotan de los dioses poseídos (Nago, Okkoto) es una mezcla de técnica digital y tradicional: Miyazaki contó que el equipo joven no sabía cómo darle forma a un espíritu maligno sin forma propia, y terminó pareciendo «espagueti con tinta de calamar negro» · ghibli.fandom.com (cita de Miyazaki, «Turning Point 1997-2008», p.50) · ✅
- Coloreado digital: la colorista jefa Michiyo Yasuda (nunca había usado una computadora) aprendió el sistema de coloreado digital en una visita a Fox Animation Studios (con Gary Goldman), el único estudio que usaba el mismo programa que Ghibli en esa época; mantenía carpetas físicas con instrucciones exactas de qué color de pintura usar para cada personaje, como referencia · ghibli.fandom.com («Coloring») (cita de la autobiografía de Steve Alpert) · ✅
- Arte de fondos: el director de arte Kazuo Oga visitó Shirakami-Sanchi en 1995 para pintar el pueblo Emishi (recorrió Ajigasawa, el paso de Tsugaru, Tengu, Hitotsumori); la isla de Yakushima (bosques antiguos de cedro) inspiró el bosque del Shishigami · ghibli.fandom.com («Background Art») + Wikipedia EN · ✅ — Oga pintaba con gouache/acuarela sobre papel, la técnica clásica de fondos de Ghibli (heredada de Toshio Ito para *Mi vecino Totoro*)
- Cada celuloide se escaneó a mano uno por uno (no automatizado) · ghibli.fandom.com («Production», pie de foto) · ⚠️ (una fuente, pie de imagen)
- El prólogo japonés («En tiempos antiguos, la tierra estaba cubierta de bosques...») se muestra como TEXTO en pantalla en la versión original; el doblaje inglés lo reemplaza por narración hablada — dato útil para saber cómo se presenta texto narrativo dentro del propio filme · resumen de búsqueda con fuentes TV Tropes/IMDb citando el guion, más el guion transcrito en scripts.com/script/princess_mononoke_13983 · ⚠️ (no se verificó con captura directa del fotograma; queda para el investigador de vídeo si necesita confirmarlo con fotogramas.py)

**Cómo replicarlo en Photoshop:**
- Fondos «Kazuo Oga»: pintar con pinceles de textura de gouache/acuarela real (grano visible, pigmento irregular) sobre una capa base de color plano; varias capas de "Multiply" para sombra de la vegetación y una capa de luz ambiental cálida encima en "Overlay" o "Soft Light" para las escenas de atardecer del Shishigami · técnica descrita en ghibli.fandom.com («Background Art») + práctica estándar documentada en tutoriales de pintura de fondos estilo Ghibli (ver Bitácora) · ⚠️ (la técnica exacta de capas es reconstrucción a partir de la descripción de la técnica real, no un tutorial oficial de Ghibli)
- Personajes: línea de contorno fina, marrón oscuro o gris oscuro (nunca negro puro) en vez de negro, coloreada con relleno plano por zonas (sin degradados en el cel, el degradado lo da la luz de fondo); para la piel bajo la maldición de Ashitaka, textura de vetas oscuras superpuestas en "Multiply" sobre el tono de piel base.
- Efecto «gusanos»/maldición: pincel de textura orgánica repetida (líneas onduladas finas, no manchas), en negro con un halo rojo oscuro alrededor, animado como si reptara — replica el resultado descrito por Miyazaki (ver arriba) con un pincel de "dispersión" en Photoshop y "warp" o pintura cuadro a cuadro.

**Cómo replicarlo en Blender:**
- Contorno (line art): usar el modificador **Freestyle** o el nodo **Solidify invertido con material de fondo negro** para el contorno grueso de los dioses del bosque (Shishigami, Moro, Okkoto), y un contorno más fino con Freestyle normal para los humanos.
- Shading: **toon shader** (Shader to RGB + rampa de 2-3 tonos) en vez del PBR realista, para conseguir el sombreado plano de las células; los reflejos del Shishigami de noche (aspecto de estrellas) piden un shader emisivo con textura de ruido (Noise Texture) animada.
- Luz: luz ambiental verde-azulada en el bosque (referencia: Yakushima, niebla y musgo), luz cálida naranja/roja en Tatara-ba (hornos encendidos) — contraste de paleta entre «bosque de los dioses» y «pueblo humano» es el recurso central para leer en qué territorio está una escena.
- Modelo/rig libre de referencia: hay un modelo 3D de San con licencia CC Attribution en Sketchfab (`sketchfab.com/3d-models/none-9f8755e5444b40c2a2f35f2ce07a8fcc`, usuario amandadollar, ~559 000 caras) que sirve de referencia de proporciones y de la máscara; usar sólo como referencia de estudio, nunca para publicar tal cual (exige atribución) · api.sketchfab.com/v3/search (comprobado por API, campo license.label="CC Attribution") · ✅

**Encuadres y composición típicos:**
- Planos muy amplios (wide shots) para el bosque y el Shishigami, mostrando la escala pequeña de los personajes frente a la naturaleza — el encuadre transmite el tema central (humanos pequeños frente a fuerzas naturales inmensas) · deducido de las descripciones de trama y del análisis de producción del making-of citado arriba (Uratani, «How Princess Mononoke Was Born») · ⚠️ (interpretación a partir de fuentes de producción, no medición directa de fotogramas — el investigador de vídeo puede confirmar minutos exactos con fotogramas.py)
- Primeros planos muy cerrados en los momentos de posesión/maldición (Nago, Okkoto, el brazo de Ashitaka) para el horror corporal, contrastando con los planos amplios del resto de la película.

### Punto 24 — Obras parecidas y temas relacionados

**Obras recomendadas por comunidad (ya en `datos-texto.md`, no repetido aquí):** Nausicaä del valle del viento, El viaje de Chihiro, El castillo ambulante, Arrietty, El castillo en el cielo, Cuentos de Terramar, La tumba de las luciérnagas (Pom Poko), Mushi-shi, Colmillo blanco/InuYasha, Kimetsu no Yaiba — lista completa con votos en `datos-texto.md`.

- Influencia reconocida: *El viaje de Shuna* (もののけ姫 de Miyazaki, 1983), su propio relato corto inspirado en el cuento tibetano «El príncipe que se convirtió en perro»; Miyazaki cita la falta de motivación del héroe de Shuna como lección para darle a Ashitaka un motivo (curar su maldición) que el público sí puede entender · ghibli.fandom.com/wiki/Princess_Mononoke («Motivation of the Hero») · ✅
- *Princess Mononoke: The First Story* (もののけ姫, 1980/1993): el cuento ilustrado original de Miyazaki (acuarelas) del que nació el título y la idea-semilla (un samurái, un gato monstruoso, un pacto de matrimonio) — muy distinto de la película final; publicado en inglés por VIZ Media el 21-oct-2014 · ghibli.fandom.com/wiki/Princess_Mononoke:_The_First_Story · ✅
- Influencia de Akira Kurosawa: Miyazaki se reunió con Kurosawa en 1993 (charla documentada en el especial de TV «Miyazaki and Kurosawa Fireside Chat»); la crítica compara las escenas de batalla con el «jidai-geki» de Kurosawa aunque Miyazaki insiste en que NO es un jidai-geki convencional; comparaciones de puesta en escena con *Kagemusha* y *Ran* · ghibli.fandom.com («Early Draft») + akirakurosawa.info/2014/08/01/film-club-princess-mononoke · ✅
- Comparada temáticamente con *Dersu Uzala* (Kurosawa, 1975) por el tema humano-vs-naturaleza · akirakurosawa.info (Film Club) · ⚠️ (una fuente, comparación crítica)
- Influencia del *Kojiki* (古事記, la crónica más antigua de Japón) y la mitología sintoísta en los dioses-animales y el Shishigami · medium.com/@ytatamura (Exploring Princess Mononoke in Japanese) · ⚠️ (una fuente; recomendable pedir confirmación en japonés si el redactor la necesita ✅)
- Cruce sorprendente con videojuegos: Shigeru Miyamoto reconoció en una entrevista de 1998 a la revista japonesa *Gamejin* que *The Legend of Zelda: Ocarina of Time* (Nintendo, 1998) se desarrolló en paralelo y comparte diseños: Link disparando flechas a caballo sobre Epona le recordaba a Ashitaka sobre Yakul, y el Goron Gigante caminando tras la montaña le recordaba al Nightwalker (Daidarabotchi); Nintendo amplió el mundo de Hyrule a propósito para diferenciarse · zeldadungeon.net + timeextension.com (ambos citan/traducen la misma entrevista de Gamejin 1998) · ✅
- Elemento en común con *Pom Poko* (Isao Takahata, 1994): ambas nacen de la idea de Miyazaki de «negar sus obras anteriores» (Totoro, Laputa) que mostraban la naturaleza como benévola; Takahata ya había retratado a la naturaleza «devolviendo el golpe» contra el progreso humano y eso empujó a Miyazaki a hacer lo mismo con Mononoke · ghibli.fandom.com («Denial of Past Works») · ✅

**Qué otra lámina del servidor se le parece (no repetir ideas):**
- El encargo **102 — El estilo Ghibli en general** (`biblias/102-el-estilo-ghibli-en-general/`, todavía sin biblia escrita a fecha de esta investigación) cubre el estilo pictórico COMÚN a todo Ghibli: fondos pintados a mano, comida, luz, viento — justo lo que un fan reconoce en cualquier película del estudio. Esta biblia de Mononoke debe centrarse en lo específico de ESTA película (el bosque de los dioses, la maldición, Tatara-ba, San/Ashitaka/Moro) y remitir a la 102 para las técnicas genéricas de fondo/luz/viento de Ghibli, para no duplicar contenido entre ambas láminas · comprobado en el propio repositorio (`encargos/102-el-estilo-ghibli-en-general.md`, `biblias/102-el-estilo-ghibli-en-general/partes/`) · ✅
- No hay otro encargo de Ghibli específico más allá del 100 (Mononoke), el 101 (*Your Name*, no es Ghibli, es CoMix Wave, pero comparte estética de «cielos y paisajes pintados») y el 102 (genérico); no se encontró solape directo con otra biblia ya escrita (el resto de encargos en `biblias/` son series muy distintas: shonen, sitcoms, videojuegos) · revisado el listado de `biblias/` · ✅

### Punto 25 — El mundo, la historia y sus símbolos

**Reglas del mundo (5 líneas):**
- Japón, período Muromachi (1336-1573): transición del Japón medieval al moderno, con el poder de los shogunes en declive · ghibli.fandom.com/wiki/Princess_Mononoke («Historical Setting») + en.wikipedia.org/wiki/Princess_Mononoke · ✅
- El bosque es territorio de dioses (kami) con forma animal: el jabalí (Nago, Okkoto), la loba (Moro) y el Shishigami (Dios Ciervo), que da y quita la vida · ghibli.fandom.com (propuesta de director + trama) + Wikipedia EN · ✅
- Tatara-ba (Irontown) tala el bosque para sacar mineral de hierro y fabrica arcabuces (ishibiya) para defenderse de los dioses y de los samuráis del Emperador · ghibli.fandom.com («Director's Proposal», «Tatara People») + Wikipedia EN («Guns are the primary weapons») · ✅
- Herir a un dios lo convierte en tatarigami (dios maldito): su rabia se transmite como maldición letal a quien lo toca — así empieza la maldición de Ashitaka con Nago · ghibli.fandom.com (trama, sección «To the West») · ✅
- No hay final feliz en la guerra entre humanos y dioses, pero «incluso en medio del odio y la masacre, hay razones para vivir»: cita literal de la propuesta de Miyazaki para la película («The Battle Between Humans and Ferocious Gods», folleto de Toho, 12-jul-1997) · ghibli.fandom.com · ✅

**Historia por arcos (con momentos clave):**
- Arco 1, exilio: el jabalí-demonio Nago ataca la aldea Emishi; Ashitaka lo mata pero recibe la maldición en el brazo derecho; la anciana Hii-sama lo destierra; Kaya (su prometida, aunque se hacen pasar por «hermanos») le regala una daga de cristal de despedida · ghibli.fandom.com (trama «To the West») · ✅
- Arco 2, el camino: cruza tierras arrasadas por la guerra, conoce al monje Jigo, llega al bosque de los dioses y ve por primera vez al Shishigami y a San · ghibli.fandom.com («The Lost Mountains») · ✅
- Arco 3, la guerra de los jabalíes: Lord Okkoto lidera una carga suicida de jabalíes contra Tatara-ba; Jigo no les avisa de las minas colocadas; el ejército jabalí es aniquilado · ghibli.fandom.com («Furies», «Requiem») · ✅
- Arco 4, la cabeza del Dios Ciervo: instigada por Jigo (que la quiere para el Emperador a cambio de protección legal para Tatara-ba), Eboshi decapita al Shishigami mientras se transforma; el cuerpo se vuelve un «dios de la muerte» de líquido negro que licúa todo lo que toca y arranca el brazo de Eboshi (mordido por la cabeza de Moro) · ghibli.fandom.com («Requiem», ficha de Eboshi) · ✅
- Arco 5, resolución: Ashitaka y San devuelven la cabeza al cuerpo; el bosque reverdece; la maldición de Ashitaka se cura; Eboshi decide reconstruir Tatara-ba «no como centro industrial, sino como un asentamiento más modesto»; San y Ashitaka se separan pero prometen verse · ghibli.fandom.com («Requiem», ficha de San) · ✅

**Emblemas, objetos icónicos y organizaciones:**
- La máscara de San: arcilla roja oscura, dos orejas blancas, líneas blancas onduladas y tres agujeros amarillos (boca y ojos) — su rasgo icónico más reconocible · ghibli.fandom.com/wiki/San + en.wikipedia.org (menciona que se vendieron réplicas de la máscara como merchandising) · ✅
- La daga de cristal que Kaya regala a Ashitaka; él se la da luego a San (a través de un lobo) como gesto de afecto · ghibli.fandom.com (trama) · ✅
- Collar de colmillos (huesos blancos) y pendientes ovalados blancos de San, llevados durante toda la película · ghibli.fandom.com/wiki/San · ⚠️ (una fuente, descripción física detallada de la wiki)
- Ishibiya: arcabuces de hierro fabricados en Tatara-ba; una bala de hierro maldita queda dentro del cadáver de Nago y es la pista que Ashitaka sigue hacia el oeste · ghibli.fandom.com («Localization», «Tatara People») · ✅
- Kodama: espíritus del bosque de cuerpo blanco translúcido, cabeza que suena como un traqueteo al moverse; son el «termómetro» de la salud del bosque — muchos caen al morir el Shishigami, sólo uno sobrevive al final de la película · ghibli.fandom.com/wiki/Princess_Mononoke + Wikipedia EN (los kodama guían a Ashitaka) · ✅
- Shishōren (師匠連): sociedad secreta de monjes que actúa por orden imperial; Jigo es uno de sus miembros pero NO trabaja directo para el Emperador (es un malentendido común del fandom) · ghibli.fandom.com/wiki/Jigo + ciatr.jp/topics/318789 y fumfum100.com/princess-mononoke-shishoren (japonés) · ✅
- Karakasaren (唐傘連): el escuadrón de combate bajo el mando de Jigo — visten haori (chaqueta corta) rojo y capucha, y llevan enormes paraguas de papel aceitado (karakasa) mientras cazan la cabeza del Shishigami; es la unidad armada del Shishōren · fumfum100.com/princess-mononoke-shishoren + walking-planet.com/mononoke-jikobou (japonés) · ✅ — dato visual muy citable para vestuario/emblema de un grupo secundario, no está en la wiki en inglés
- Eslogan publicitario «生きろ。» / «Live.», acuñado por el copywriter Shigesato Itoi (autor también de eslóganes de otras películas Ghibli y diseñador del videojuego *Mother*); Itoi descartó cerca de 50 propuestas (ghibli.fandom cita casi 50; el libro «Ghibli Textbook 10: Princess Mononoke» habla de 23 ideas rechazadas antes de llegar a «Live.») · ghibli.fandom.com («Advertising Slogan») + note.com/gifted_taka705 (entrevista a Itoi, japonés) · ✅ (el eslogan y autor, en dos fuentes) ⚠️ (el número exacto de propuestas varía según la fuente)

**Vocabulario propio (para textos del canal y guía de IA):**
- Mononoke (もののけ): nombre genérico para un espíritu vengativo o poseído, no un nombre propio — por eso los humanos llaman a San «la princesa mononoke» (もののけ姫), no es su nombre real · ghibli.fandom.com/wiki/San · ✅
- Tatara-ba (たたら場): fundición donde se funde el hierro con fuelles que las mujeres pisan por turnos; el pueblo entero se llama así en japonés, «Irontown» es la traducción inglesa · ghibli.fandom.com («Localization») · ✅
- Jibashiri (じばしり): mercenarios/exploradores de tierra al servicio de Jigo; el doblaje inglés los simplifica como «Mercenary» · ghibli.fandom.com («Localization») · ✅
- Shishigami / Dios Ciervo / Daidarabotchi (でいだらぼっち, forma nocturna, «Nightwalker» en inglés): mismo ser, dos formas (ciervo de día, gigante translúcido de noche) · ghibli.fandom.com/wiki/Princess_Mononoke · ✅
- Ishibiya (石火矢): arcabuz/mosquete temprano de mecha, el arma que define a Tatara-ba frente al mundo natural · ghibli.fandom.com · ✅

## Lo mejor para la lámina

(pendiente)

## No encontré

(pendiente)

## Bitácora

(pendiente)

Sigue: rellenar todos los puntos (5, 6, 11, 18, 24, 25) desde cero.
