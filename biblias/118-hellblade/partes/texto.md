# Parte de TEXTO, JUEGOS Y TÉCNICA · Hellblade (Senua's Sacrifice + Senua's Saga: Hellblade II)

Investigador de texto, juegos y técnica. Puntos 5, 6, 11, 18, 24 y 25 de `ENCARGO.md`.
Parte de `datos-texto.md` (capturas de Steam de ambos juegos en 1920×1080, sin datos de Fandom porque
`recolectar.py` no encontró la wiki con ese nombre). La wiki real es **`thehellblade.fandom.com`**
(no `hellblade-nt.fandom.com`, que da 404/403 — ese es sólo el prefijo de las imágenes en
`static.wikia.nocookie.net/hellblade-nt/...`). Es una libreta de datos: un dato por línea, con
fuente, ✅ (dos fuentes) o ⚠️ (una).

## Índice
- [Punto 5 — Tipografía](#punto-5)
- [Punto 6 — Cuadros de diálogo, cartelas e interfaces](#punto-6)
- [Punto 11 — Videojuegos de la franquicia: interfaz, menús, cajas de diálogo](#punto-11)
- [Punto 18 — Estilo de dibujo y técnica, y cómo replicarlo](#punto-18)
- [Punto 24 — Obras parecidas](#punto-24)
- [Punto 25 — El mundo, la historia y sus símbolos](#punto-25)
- [Lo mejor para la lámina](#lamina)
- [No encontré](#no-encontre)
- [Bitácora de búsqueda](#bitacora)

---

<a name="punto-5"></a>
## Punto 5 — Tipografía

### 5.1 El logo/título — sin fuente pública confirmada, pero con tipografía oficial de marca verificada
- **Nadie ha identificado la fuente exacta del logo** de *Hellblade: Senua's Sacrifice* (2017): es previsiblemente lettering custom o muy retocado. La comunidad de identificación de fuentes (dafont, Typography.Guru) no lo ha resuelto; el sustituto más citado es **"Sell Your Soul"** (Christopher Hansen), como aproximación, no como fuente real. ⚠️ una fuente de calidad media — [Hyperpix: Hellblade Font Download](https://hyperpix.net/fonts/hellblade-senuas-sacrifice-font/).
- El logo de **Senua's Saga: Hellblade II** (2024) tampoco tiene fuente identificada; se describe como letras "como talladas en piedra", bordes afilados tipo cuchilla, con el subtítulo "Hellblade II" en gris metálico bajo el título "Senua's Saga" en rojo oscuro. ⚠️ una fuente (análisis de diseño, no del estudio) — [Logos-World: Hellblade 2 Logo](https://logos-world.net/hellblade-2-logo/).
- **Dato directo y verificado** (mejor que cualquier análisis de fans): revisé el CSS que sirve la propia web oficial **`hellblade.com`** (Adobe Fonts/Typekit, `use.typekit.net/tvg7fkw.css`) y encontré las **tres tipografías reales de marca** que usa el estudio para el primer juego: **`trajan-pro-3`** (serif clásica romana, con la elegancia "grabada en piedra" típica de logos épicos — la misma familia usada en carteles de películas y otros juegos de fantasía/historia), **`proxima-nova-extra-condensed`** (sans muy condensada, para titulares/menús), y **`lato`** (sans para cuerpo de texto). ✅ verificado directamente leyendo el CSS servido por `hellblade.com` (fuente primaria, no un análisis de terceros).
- **Dato directo y verificado para Hellblade II**: la web oficial **`senuassaga.com`** (gestionada por Xbox) sirve sus fuentes con Next.js; leyendo su CSS (`_next/static/css/*.css`) confirmé que usa **Cinzel** (`--font-cinzel`, variable de peso 400-900) para titulares/encabezados y **Outfit** (`--font-outfit`, geométrica) para el cuerpo, además de una referencia a `--font-arno-pro` (Adobe, serif clásica) para elementos puntuales. ✅ verificado directamente en el CSS oficial. **Las dos son gratis (Google Fonts, licencia OFL)** — es una suerte para la lámina: la tipografía oficial de la web de Hellblade II ya es libre.
- **Comprobación con fontTools** (obligatoria por AYUDANTE.md) de las dos fuentes libres que usa la propia Hellblade II: descargué `Cinzel[wght].ttf` y `Outfit[wght].ttf` de Google Fonts (vía `fonts.googleapis.com/css2`) y ambas traen el juego completo de español: **á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü Ü, sin faltar ninguna**. ✅ comprobado yo mismo con `fontTools.getBestCmap()`.
- **Recomendación para la lámina**: usar **Cinzel** para el título/logo (misma familia "grabada en piedra" que ya usa la propia Hellblade II en su web oficial) y **Outfit** o **Lato** (Google Fonts, con tildes) para cuerpo de texto — no hace falta inventar una aproximación: el estudio ya usa fuentes libres de verdad en su propia web.

### 5.2 El alfabeto rúnico de los puzles (uso: cartel del mundo / interfaz de juego)
- Los símbolos que hay que encontrar y enfocar (`Focus`) en las puertas selladas de *Senua's Sacrifice* **son runas reales del Futhark Antiguo (Elder Futhark)**, no glifos inventados para el juego — confirmado por dos fuentes independientes que identifican el alfabeto y por la wiki oficial del juego, que dice literalmente «the runes seal the gates to Hel». ✅ [SteamCommunity: Why Elder Futhark?](https://steamcommunity.com/app/414340/discussions/0/1815422173039264083/), cruzado con [thehellblade.fandom.com/wiki/Focus](https://thehellblade.fandom.com/wiki/Focus) (vía API).
- **Detalle curioso confirmado**: los anillos de runas alrededor de cada uno de los 44 [Lorestones](#punto-25) (ver 25.3) deletrean, en Futhark Antiguo, un mensaje real en inglés: **"SEEK HELA'S TRUTH IN MIRROR GODS BETRAY US UNMASK FEAR"** — un guiño para quien sepa leer runas. ✅ [SteamCommunity: Futhark Runes on Lorestones](https://steamcommunity.com/app/414340/discussions/0/1471967615867064757/), cruzado con la wiki de Lorestones.
- **Cómo funciona el puzle de puertas (glyph doors)**: la runa roja en la puerta se debe encontrar tallada en algún punto del paisaje (a veces como una silueta que sólo se forma alineando un objeto en primer plano con otro al fondo, un juego de luces y sombras); al mirar desde el ángulo correcto la runa cambia de rojo a blanco-azulado y, si Senua la enfoca (Focus), queda «capturada» y se transmite a la puerta. ✅ [Gameranx: How To Solve Every Puzzle](https://gameranx.com/features/id/115013/article/hellblade-senuas-sacrifice-how-to-solve-every-puzzle-solutions-guide/), cruzado con [PowerPyx: Puzzle Solutions & Symbol Locations](https://www.powerpyx.com/hellblade-senuas-sacrifice-puzzle-solutions-symbol-locations-walkthrough/).
- **Letra libre para el rúnico**: **Noto Sans Runic** (Google Fonts, licencia OFL) — **lo comprobé yo mismo con fontTools**: trae los 24 signos del Futhark Antiguo completos (bloque Unicode Runic, U+16A0-16B7) más 426 glifos rúnicos en total (incluye variantes anglosajonas y del Futhark Joven). ✅ comprobado directamente. [Google Fonts: Noto Sans Runic](https://fonts.google.com/noto/specimen/Noto+Sans+Runic).
- En *Hellblade II* el mismo lenguaje visual continúa pero con otro nombre: los **Rostos Escondidos (Hidden Faces)** son 17 caras talladas en piedra escondidas en el paisaje (no runas esta vez, sino rostros) que hay que enfocar para revelar un camino secreto hacia un árbol pequeño (`Landdísasteinar`); unas voces avisan cuando hay uno cerca. ✅ [thehellblade.fandom.com/wiki/Hidden_Faces](https://thehellblade.fandom.com/wiki/Hidden_Faces) (vía API).

### 5.3 Subtítulos e interfaz de accesibilidad (uso: subtítulos/HUD)
- *Senua's Sacrifice* cumple el estándar de accesibilidad de altura mínima de subtítulo: **al menos 1/20 de la altura de la pantalla (46 píxeles en 1080p)**, con alto contraste, y el color del texto del subtítulo se puede ajustar. ✅ [Family Gaming Database: Accessibility Report](https://www.familygamingdatabase.com/accessibility/Hellblade+Senuas+Sacrifice), cruzado con [Can I Play That? — Steam accessibility info](https://caniplaythat.com/2022/02/09/hellblade-senuas-sacrifice-now-lists-accessibility-information-on-steam/).
- *Hellblade II* amplía esto: soporta **26 idiomas** y añade un **indicador de dirección** junto al subtítulo — una marca que dice de qué lado viene la voz que habla (coherente con el audio binaural, ver [punto 18](#punto-18)), más opciones avanzadas de color, tamaño y visualización del texto. ✅ [TechRaptor: Hellblade 2 Accessibility Options](https://techraptor.net/gaming/news/senuas-saga-hellblade-2-accessibility), cruzado con [Can I Play That?: Hellblade II accessibility review](https://caniplaythat.com/2024/07/02/senuas-saga-hellblade-ii-accessibility-review/).
- **No hay letras de globo de manga** (normal, grito, pensamiento, onomatopeya): ninguno de los dos juegos usa globos de cómic en pantalla — ver [punto 6](#punto-6) para cómo se resuelve el diálogo interior sin ellos. El único material impreso real es el cómic promocional (ver 6.3), que tampoco usa globos clásicos.
- **En japonés/coreano/chino**: no aplica — Hellblade es una obra británica (Ninja Theory, Cambridge, Cambridgeshire), no viene de Asia oriental, así que no hace falta buscar en esos idiomas (lo dice el propio ENCARGO.md, «si la obra viene de ahí»).

---

<a name="punto-6"></a>
## Punto 6 — Cuadros de diálogo, cartelas e interfaces

**Hellblade no tiene globo de cómic ni caja de diálogo tradicional en ningún momento.** Es el ejemplo más extremo de «nada de burbuja blanca genérica» que puede pedir el dueño: literalmente no hay HUD, ni marco, ni panel. Confirmado por dos fuentes que analizan el diseño de interfaz del juego. ✅ [Gaming Conceptz: diegetic vs non-diegetic elements in Hellblade](http://gamingconceptz.blogspot.com/2025/10/the-clash-between-diegetic-and-non.html), cruzado con foros de Steam sobre «no hud» ([SteamCommunity](https://steamcommunity.com/app/414340/discussions/0/1471966894874945366/)).

### 6.1 Cómo se sustituye la caja de diálogo: subtítulo flotante + voz espacial
- Los subtítulos (opcionales, se pueden apagar) son **texto flotante sin caja ni panel de fondo**, igual que hace *God of War* (ver `biblias/117-god-of-war-todas-las-sagas/partes/texto.md`, punto 6.2) — es una convención que comparten los juegos "cinemáticos sin HUD" de esta generación. ✅ (ver 5.3 arriba, Family Gaming Database/Can I Play That).
- **El verdadero «cuadro de diálogo» de Hellblade es el sonido binaural**: las voces de **las Furias** (Furies) —los susurros constantes en la cabeza de Senua— se graban y mezclan para que suenen delante, detrás, a un lado, muy cerca del oído; el jugador necesita auriculares para captar toda la información. Esto funciona como interfaz: las voces avisan de amenazas, dan pistas de puzles y advierten del peligro, ocupando el rol que en otro juego llevaría un HUD. ✅ dos fuentes: [Gaming Conceptz](http://gamingconceptz.blogspot.com/2025/10/the-clash-between-diegetic-and-non.html) (análisis "meta-diegético"), [insidethemagic.net: nightmarish audio experience](https://insidethemagic.net/2017/08/video-hellblade-senuas-sacrifice-creates-stunningly-nightmarish-audio-experience-using-binaural-audio/). Ver la técnica de grabación en [punto 18.4](#punto-18).
- **El indicador de "salud"/fallo es el brazo de Senua, no una barra**: la `Dark Rot` (Corrupción Oscura) es una mancha negra que le sube por el brazo derecho cada vez que el jugador falla en combate; el propio juego avisa al empezar: *"The dark rot will grow each time you fail. If the rot reaches Senua's head, her quest is over and all progress will be lost"*. ✅ [thehellblade.fandom.com/wiki/Dark_Rot](https://thehellblade.fandom.com/wiki/Dark_Rot) (vía API), cruzado con [PCGamesN: Hellblade's permadeath bluff](https://www.pcgamesn.com/hellblade-senuas-sacrifice/hellblade-permadeath-fake).
- **Giro importante, confirmado por el propio director**: ese aviso de "todo se perderá" **es un farol** — el juego no borra la partida de verdad, la corrupción nunca llega a la cabeza. Tameem Antoniades (director creativo, Ninja Theory) lo explicó así: *"The wording for the permadeath message was chosen quite carefully because we didn't want to lie to the player... A large part of the game is about fear, and a large part of mental illness — psychosis in particular — is about fear"*. Es decir: el "cuadro de aviso" está diseñado para inducir el mismo miedo hipervigilante que siente alguien con psicosis, no para castigar de verdad. ✅ [PCGamesN: Hellblade's permadeath bluff is "not as simple as people think"](https://www.pcgamesn.com/hellblade-senuas-sacrifice/hellblade-permadeath-fake), cruzado con [ComicBook.com: Permadeath Warning Turns Out To Be A Cruel Bluff](https://comicbook.com/gaming/news/hellblade-senuas-sacrifice-is-a-lie/).
- **Qué NO hacer**: poner una barra de vida roja convencional o una burbuja blanca para las voces — la propia mecánica del juego es la prueba de que Ninja Theory evitó a propósito cualquier elemento de HUD reconocible como "videojuego": todo el feedback pasa por el cuerpo de Senua y por el sonido.

### 6.2 Hellblade II: mismo lenguaje, con indicador de dirección
- *Senua's Saga: Hellblade II* mantiene la ausencia de HUD (sin barra de vida visible, sin mapa, sin indicador de objetivos); un análisis técnico de terceros midió que Senua tiene una reserva de vida oculta muy pequeña por combate, pero nunca se muestra en pantalla. ✅ [caniplaythat.com: Hellblade II accessibility review](https://caniplaythat.com/2024/07/02/senuas-saga-hellblade-ii-accessibility-review/), cruzado con guías de Steam sobre el modo Dark Rot.
- El modo opcional **Dark Rot Mode** (nuevo, no estaba en el lanzamiento original de 2024) sí aplica un permadeath real y explícito: da **4 vidas** a lo largo de los 6 capítulos del juego; a la cuarta muerte se borra el progreso — está inspirado a propósito en el farol del juego original, pero aquí es una mecánica real y optativa, no una amenaza falsa. ✅ [Steam Community Guide: 100% Achievements & Collectibles | Hellblade II](https://steamcommunity.com/sharedfiles/filedetails/?id=3433636765), cruzado con la wiki (`Dark_Rot`, vía API).
- Sin mapa ni marcador de objetivo: la navegación depende de **pistas ambientales y sonoras** (la voz de las Furias sugiriendo un camino, la luz, la composición del encuadre) — el mismo lenguaje "sin muletas" del primer juego, llevado a un mundo más abierto. ⚠️ una fuente de calidad media — [XBOX Wire: The Wanderers, entorno de Hellblade II](https://news.xbox.com/en-us/2024/05/20/hellblade-2-environmental-design-inspired-by-iceland/).

### 6.3 El único material «de viñeta»: el cómic promocional de Valiant (no usa globos clásicos)
- *Hellblade: Senua's Song #1* (2017) es un cómic digital exclusivo de pre-compra hecho con **Valiant Entertainment**: guion de Tameem Antoniades, arte de **Ben Templesmith**. Se presenta como **un poema épico ilustrado, sin viñetas ni globos de diálogo tradicionales** — el texto corre como verso libre junto a las ilustraciones, no dentro de burbujas. ✅ [Valiant Entertainment: Hellblade: Senua's Song #1](https://valiantentertainment.com/2017/06/06/ninja-theory-and-valiant-partner-for-hellblade-senuas-song-1-a-pre-order-exclusive-comic-available-on-steam-and-gog-com/), cruzado con [ComicsBeat](https://www.comicsbeat.com/valiant-templesmith-and-ninja-theory-team-for-exclusive-hellblade-senuas-song-digital-comic/).
- Esto refuerza la regla de estilo de toda la franquicia: **evitar cualquier convención gráfica "de cómic clásico"** (globo ovalado, onomatopeya en letras grandes) incluso en su material impreso — todo se resuelve con tipografía suelta sobre la imagen, nunca encerrada en una forma.

---

<a name="punto-11"></a>
## Punto 11 — Videojuegos de la franquicia: interfaz, menús, cajas de diálogo

_(pendiente)_

---

<a name="punto-18"></a>
## Punto 18 — Estilo de dibujo y técnica, y cómo replicarlo

_(pendiente)_

---

<a name="punto-24"></a>
## Punto 24 — Obras parecidas

_(pendiente)_

---

<a name="punto-25"></a>
## Punto 25 — El mundo, la historia y sus símbolos

_(pendiente)_

---

<a name="lamina"></a>
## Lo mejor para la lámina

_(pendiente)_

---

<a name="no-encontre"></a>
## No encontré

_(pendiente)_

---

<a name="bitacora"></a>
## Bitácora de búsqueda

_(pendiente)_

Sigue: rellenar todos los puntos (5, 6, 11, 18, 24, 25) desde cero, empezando por buscar la
tipografía del logo, el alfabeto rúnico de los puzles, la charla GDC de captura de movimiento
en tiempo real, la fotogrametría islandesa, Paul Fletcher/Wellcome Trust, y la mitología picta.
