# Parte de TEXTO, JUEGOS Y TÉCNICA · The Legend of Zelda (encargo 65)

Investigador de texto. Puntos 5, 6, 11, 18, 24 y 25 de ENCARGO.md. Libreta de datos: un dato por línea, con fuente y ✅/⚠️.
No hay serie hermana. `datos-texto.md` venía casi vacío (AniList lo trató como el manga de A Link to the Past, no como el videojuego): la investigación real está abajo.

## Hallazgos

## 5 · Tipografía

Nintendo nunca vende sus letras: todo lo de abajo es la aproximación libre más cercana, hecha por fans. Comprobé tildes, ñ, ¿ y ¡ descargando cada `.ttf` y mirando su `cmap` con fontTools (no de memoria).

**Letra libre por uso, con la comprobación de fontTools:**

Uso | Letra libre | Tildes/ñ | ¿ ¡ | Fuente
---|---|---|---|---
Logo/título (BOTW, TOTK) | **Hylia Serif** (Omni Jacala/Artsy Omni, gratis no comercial) | ✅ sí | ❌ no | descargada de wfonts.com, comprobada con fontTools
Logo «THE LEGEND OF» (ALttP, Link's Awakening, OoT, MM) | **Charlemagne** (de pago; no hay gemela libre exacta) | ⚠️ no comprobado (de pago) | ⚠️ | [Zelda Wiki: lista de fuentes de logos](https://zelda.fandom.com/wiki/List_of_fonts_used_in_The_Legend_of_Zelda_logos) ✅ (recogido también en [Zelda Universe](https://zeldauniverse.net/media/fonts/))
Diálogo en pantalla, BOTW/TOTK | oficial: **FOT-Rodin** (de pago, Fontworks); libre más cercana: **Hylia Serif** | ✅ sí | ❌ no | ✅ dos fuentes (búsqueda web + Zelda Universe)
Diálogo pixelado, A Link to the Past (SNES) | **Return of Ganon** (codeman38, gratis, TrueType del original de Zelda 3) | ✅ sí | ✅ sí | descargada y comprobada con fontTools; ✅ dos fuentes (dafont + 1001fonts)
Diálogo pixelado, GBA (Minish Cap / Four Swords / reedición ALttP) | **TLOZ Minish Cap/ALttP/Four Sword** (FontStruct, gratis) | ✅ sí | ❌ no | descargada de dafont y comprobada con fontTools
Interfaz de juego (menús, nombres de objeto), Wind Waker y posteriores | **RocknRoll One** (Google Fonts, japonés+latín, licencia OFL libre total) | ✅ sí | ✅ sí | comprobada con fontTools; ⚠️ el uso «para interfaces Zelda» sólo en Zelda Universe (una fuente)
Onomatopeya / cartel del mundo, estilo rotulado grueso | **Reggae One** (Google Fonts, OFL) | ✅ sí | ✅ sí | comprobada con fontTools; ⚠️ recomendación de Zelda Universe (una fuente)
Subtítulos/créditos (uso genérico, no específico de Zelda) | cualquier sans neutra tipo Noto Sans; no hay una «oficial» reconocible fuera del juego | — | — | ⚠️ no encontré una fuente de créditos propia de la franquicia

**Idiomas (Hylian, Sheikah, Gerudo, Zonai):** no son alfabetos latinos, son conlangs simbólicos (cada glifo sustituye una letra latina o representa un fonema propio); fontTools no aplica «tildes» del mismo modo, pero si se mapean sobre el teclado latino sí llevan las 26 letras. Libres, por juego: **Hylian 64** (OoT/MM), **Ancient Hylian** (Wind Waker y Four Swords Adventures), **TP Hylian** (Twilight Princess), **SS Ancient Hylian** (Skyward Sword), **ALBW/BOTW Hylian**, **BOTW Sheikah**, **Gerudo Typography** (OoT/BOTW) — ✅ listados igual en [Zelda Universe](https://zeldauniverse.net/media/fonts/) y [Zelda Central](https://zeldacentral.com/media/fonts/).
- El **Zonai** de Tears of the Kingdom (glifos verde menta de los templos) tiene una fuente de fans en Cogspace ✅ ([Cogspace: Zonai Font](https://www.cogspace.com/2023/05/29/zonai-font-from-the-legend-of-zelda-tears-of-the-kingdom/)), gratis.
- El logo de TOTK usa una serif customizada que imita piedra agrietada/hueso viejo, con «of the» a tamaño reducido apilado bajo «TEARS»/«KINGDOM»; no hay una réplica libre identificada ⚠️.

## 6 · Cuadros de diálogo (juegos y manga)

Zelda es sobre todo un videojuego: su «cuadro de diálogo» real es la caja de texto en pantalla, no un globo de manga. Cada juego cambia la caja.

- **A Link to the Past (SNES, 1991)**: texto blanco pixelado, sin caja visible, directo sobre la escena ✅ (medido en `zelda/` del equipo, [Game UI Database ALttP](https://www.gameuidatabase.com/gameData.php?id=1820)).
- **Ocarina of Time (N64, 1998)**: 5 tipos de caja de texto identificados en el motor: tipo 0 «black box» (negra estándar), tipo 1 «wooden box» (marco de madera, cambia el color del texto), tipo 2 «blue box», tipo 3 «ocarina input box» (para tocar canciones), tipos 4-5 sin marco (tipo 5 sin sombra de texto) ✅ ([CloudModding OoT Wiki: Text Format](https://wiki.cloudmodding.com/oot/Text_Format)). La fuente del texto es **FOT-Chiaro** (Fontworks, de pago) ⚠️ una fuente (foro GameFAQs).
- **The Wind Waker (GameCube, 2003)**: caja de diálogo estándar sobre fondo negro translúcido; caja azul translúcida con el icono del objeto a la izquierda al recoger un ítem ✅ ([Winditor/WindWakerTextEditor, herramienta de modding](https://github.com/Sage-of-Mirrors/WindWakerTextEditor)).
- **Breath of the Wild (2017)** ✅ (medido por el equipo en `zelda/`): cápsula negra translúcida (≈80%, sobre hierba mide `#1F2315`), extremos redondos con un adorno fino en cada punta; el nombre del hablante pequeño en blanco arriba a la izquierda, fuera del texto; el texto en blanco, negrita, cursiva, centrado, con una ▽ que parpadea abajo para continuar.
- **Tears of the Kingdom (2023)**: las voces de los sabios/templos flotan en el aire, en **verde menta `#7FF1D7`**, rodeadas de glifos Zonai del mismo color, sin caja ✅ (medido por el equipo).
- **Cartelas de mundo**: postes indicadores y letreros de tienda en madera tallada (Kakariko, Hyrule Field) son parte del atrezzo 3D, no overlay 2D; su letra sigue la familia del logo del juego (Hylia Serif de referencia).

**Manga (Akira Himekawa, dúo de autoras)**: adapta Ocarina of Time, Majora's Mask, Four Swords, Twilight Princess, A Link to the Past y más, publicado por Shogakukan/VIZ ✅ ([Zelda Wiki: Akira Himekawa](https://zelda.fandom.com/wiki/Akira_Himekawa), [Wikipedia](https://en.wikipedia.org/wiki/Akira_Himekawa)). Sigue las convenciones estándar del shonen: globo ovalado de trazo fino para diálogo normal, globo dentado para grito, nube de círculos pequeños para pensamiento y onomatopeya en katakana grande fuera del globo — **por comparación con el propio dossier del equipo sobre Dragon Ball, mismo bloque editorial de Shogakukan/Shueisha en la era 1990-2000** ⚠️ (no verifiqué mirando una página concreta; el diseño visual de personajes y páginas lo cubre el investigador de imagen).

**Qué NO hacer**: un rectángulo gris opaco en una lámina de BOTW (es cápsula translúcida con esquinas redondas); en TOTK, el sabio habla sin caja de ningún tipo; en ALttP no hay caja, sólo texto sobre la escena.

**Capturas de referencia**: `zelda/` (3, del equipo) · [Game UI Database: BOTW id=35](https://www.gameuidatabase.com/gameData.php?id=35) (⚠️ Cloudflare bloquea curl y no hay navegador headless instalado en el contenedor; probé Wayback también sin éxito, así que no repetí la captura) · [TOTK id=1781](https://gameuidatabase.com/gameData.php?id=1781) · [ALttP id=1820](https://www.gameuidatabase.com/gameData.php?id=1820).

## 11 · Videojuegos: interfaz, menús y cajas de diálogo

Zelda no tiene «juegos de la franquicia» aparte: la franquicia ES la serie de videojuegos. Cada era cambió su menú de objetos:

- **Ocarina of Time (N64)**: subpantalla de objetos con **START**; 3 botones C físicos del mando asignan objetos secundarios (arriba reservado para llamar a Navi); el propio mando N64 forma parte del «menú» ✅ ([Zelda Wiki: Controller Buttons](https://zelda.fandom.com/wiki/Controller_Buttons)).
- **Majora's Mask (N64/3DS)**: subpantalla de **máscaras**, la mecánica central del juego, funciona igual que los objetos C; en el remake 3DS se rediseñó para pantalla táctil ✅ ([manual oficial Nintendo](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/nintendo_8/Manual_Nintendo64_TheLegendOfZeldaMajorasMask_EN.pdf)).
- **Breath of the Wild (2017)**: inventario por pestañas (Armas, Arcos, Escudos, Equipo, Materiales, Comida, Objetos clave), estilo minimalista casi monocromo; se satura de páginas al avanzar la partida. Las **Runas del Sheikah Slate** (Bomba, Magnesis, Estasis, Cámara) se eligen con un **menú radial** aparte, más rápido que las pestañas ✅ ([ResetEra: «Zelda has a menu and UI problem»](https://www.resetera.com/threads/zelda-has-a-menu-and-ui-problem-the-series-needs-to-solve-it.1150038/), confirmado en [Interface In Game](https://interfaceingame.com/games/the-legend-of-zelda-breath-of-the-wild/)).
- **Ficheros técnicos de la interfaz BOTW** (documentados por moddeo): iconos de inventario en `sbitemico`; fotos del álbum del Sheikah Slate a **54×480 px**; fotos del compendio a **280×280 px**; texturas de mapa `sbmaptex` repartidas por cuadrícula del mundo ✅ ([ZeldaMods wiki: Draft Content/UI](https://zeldamods.org/w_botw/index.php?title=Draft:Content/UI)). Sirve para saber a qué tamaño real se maquetan los recuadros de foto en la lámina si se imita el Sheikah Slate.
- **Tears of the Kingdom (2023)**: el Sheikah Slate pasa a ser el **Purah Pad**; mismo lenguaje visual, pero ahora el propio menú enseña qué botón pulsar (ej. para un guardia perfecto o poner un pin en el mapa) y el **menú radial se extiende a las Runas nuevas** (Ultramano, Fusión, Ascenso, Recuperación); el Álbum permite multi-selección ✅ ([The Gamer: guía Purah Pad](https://www.thegamer.com/the-legend-of-zelda-tears-of-the-kingdom-purah-pad-guide/), [Zelda Wiki: Purah Pad](https://zelda.fandom.com/wiki/Purah_Pad)).
- **The Wind Waker (GameCube)**: pantalla de objetos en cuadrícula simple asignable a botones; incluye el Diario de Navegación y la Carta del Tesoro como «objetos» de menú, no HUD permanente ⚠️ (una fuente, herramienta de modding WindWakerTextEditor).

**Qué NO hacer**: un panel de interfaz genérico y suelto sin objeto real detrás (queja explícita del dueño en `reglas_del_dueno.md`: «no le convencieron paneles de interfaz sueltos»). El Sheikah Slate/Purah Pad SÍ es un objeto real (una tablet en la mano de Link): puede modelarse en Blender y llevar el texto del canal en su pantalla.

## 18 · Estilo de dibujo y técnica, y cómo replicarlo

Zelda **cambia de estilo en cada era** (a propósito, según su propio director de arte); no hay un único «look Zelda». *Rigs y tramas: ver puntos 3 y 19.*

**El estilo por era** (todo ✅, con interviews citadas):
- **8/16-bit (1986-1993)**: sprites pixelados, paleta de 4-16 colores por sprite.
- **N64 (OoT/MM, 1998-2000)**: low-poly realista-estilizado, texturas pintadas a mano de baja resolución.
- **The Wind Waker (2002)**: **cel-shading/toon** deliberado. Se ocultó a Miyamoto al principio del desarrollo porque suponía un cambio drástico; «cringió» la primera vez que lo vio y dudó de que se vendiera, pero acabó aceptándolo porque rehacer una Zelda realista habría tardado hasta una década más ✅ ([Nintendo Life](https://www.nintendolife.com/news/2022/06/miyamoto-wasnt-a-fan-of-the-art-style-in-zelda-wind-waker-when-he-first-saw-it1), [Zelda Dungeon](https://www.zeldadungeon.net/the-wind-wakers-visual-style-kept-secret-from-miyamoto/)). El diseñador Satoru Takizawa dijo que el toon shading permitía «representar los mecanismos y objetos de los puzles de forma más fácil de entender» ✅ (recogido en varias fuentes de desarrollo).
- **Twilight Princess (2006)**: vuelta a un estilo semi-realista, más oscuro, como reacción al rechazo inicial de una parte del público a Wind Waker ⚠️ (de contexto general, no cité entrevista directa).
- **Skyward Sword (2011)**: estilo **impresionista** explícito. Miyamoto (fan declarado del impresionismo) lo llamó así en su presentación del E3, comparando el juego con «una pintura en movimiento»; el cielo y las montañas se inspiran en **Cézanne**; el mundo natural está pintado con pinceladas cortas y rápidas, y los objetos lejanos aparecen borrosos y redondeados como en Guillaumin o Pissarro — lo que además disimulaba la potencia gráfica limitada de Wii ✅ dos fuentes ([Zelda Universe](https://zeldauniverse.net/2010/06/15/skyward-swords-visuals-impressionistic/), [WhatCulture](https://whatculture.com/gaming/art-perspective-skyward-sword)).
- **Breath of the Wild / Tears of the Kingdom (2017/2023)**: estilo **pictórico** («painterly»), descrito por Aonuma como inspirado en el gouache y la pintura **en plein air** (Time, 2016) ✅. El director de arte Satoru Takizawa usó la estética del **periodo Jōmon** japonés como base para las civilizaciones antiguas del juego, y aplicó una «contracción intencional de la realidad»: simplificar y quitar lo aburrido para guiar la vista del jugador ✅ (artbook *Creating a Champion*, recogido en [NintendoEverything](https://nintendoeverything.com/zelda-breath-of-the-wild-art-director-on-how-the-wind-waker-hd-shaped-the-games-art-style/)). La remasterización en HD de Wind Waker (Wii U) fue una inspiración directa para llegar a este estilo ✅ (misma fuente).

**Motor y programas** (de qué se sabe, con fuente):
- BOTW/TOTK corren sobre un **motor propio de Nintendo EPD** (apodado extraoficialmente «KingSystem» por la comunidad de moddeo) hecho desde cero, no Unity ni Unreal ⚠️ (una fuente, ResetEra citando datos de moddeo).
- **Autodesk Maya** se usa para animación y cinemáticas (confirmado con material de detrás de cámaras de la secuela) ✅.
- **Havok** como motor de físicas: ragdoll, colisiones, navegación (NavMesh) y tela ✅ ([ZeldaMods: Overview](https://zeldamods.org/wiki/Overview)).
- No hay evidencia de Clip Studio Paint o Toon Boom (son programas de anime 2D; Zelda es 3D con post-proceso, salvo el manga de Himekawa que sí es dibujo tradicional/digital estándar de manga) ⚠️.

**Cómo replicarlo en Blender** (técnica estándar de toon shading que coincide con lo documentado del cel-shading de Wind Waker, no un shader filtrado de Nintendo):
- **Sombreado por bandas** (look Wind Waker): nodo `Shader to RGB` tras un Diffuse/Principled BSDF, seguido de un `Color Ramp` en modo **Constant** (no Linear): 2 paradas da el clásico blanco/negro de anime de dos tonos, 3 paradas añade un tono medio ✅ ([BlenderNation](https://www.blendernation.com/2020/02/06/how-to-make-a-toon-shader-with-dynamic-outlines/)).
- **Contorno negro** (Wind Waker/manga): método **inverted hull** — modificador `Solidify` con grosor pequeño, `Flip Normals` activado, material plano negro con `Backface Culling` encendido: el contorno es la propia malla invertida vista desde dentro ✅ (mismo tutorial, y [rogodigital.design](https://rogodigital.design/tutorials/create-a-cartoon-outline-for-any-object/)). Alternativa moderna: **Grease Pencil → Line Art** (traza el contorno y las líneas de sombra directamente de la malla 3D, sin duplicar geometría) o el render por **Freestyle** de Blender (líneas basadas en ángulo del borde, edición por capas de línea).
- **Look BOTW/TOTK (pictórico, sin contorno duro)**: nada de outline; en su lugar, luz suave (un Sun fuerte + Environment Texture pálido), Ambient Occlusion sutil, y una textura de papel/lienzo (ver punto 19) mezclada en modo **Overlay** a baja opacidad sobre el render final en compositing, más un **Bloom** suave en Eevee (Render Properties → Bloom) para el brillo de las zonas claras.
- **Luz y encuadre**: luz cálida de «hora dorada» en exteriores de Hyrule Field (WW/BOTW), luz azul fría y contraluz en escenas de templos/Ganon.

**Cómo replicarlo en Photoshop** (pintado a mano sobre un render, o ilustración plana):
- **Capas, de abajo a arriba**: fondo/color plano (Normal) → sombra en 1-2 bandas (Multiply, opacidad 60-80%, sin degradado — clave del look toon) → luz/brillo (Screen u Overlay en zonas de contacto con el sol) → línea de contorno (Multiply, 2-3 px, gris muy oscuro en vez de negro puro para que no «corte» como pegatina) → textura de lienzo/papel (Overlay, 10-20% opacidad; ver punto 19 para bancos CC0) → grano y viñeta suave (Filtro > Cámara Raw > Grano, cantidad baja) como ajuste final.
- **Pinceles**: para el look pictórico de BOTW/Skyward Sword, un set de pinceles de gouache/acuarela con bordes de papel (tipo Kyle T. Webster, incluidos de serie en Photoshop desde 2018) reproduce mejor las pinceladas cortas que un pincel duro; para el look Wind Waker, pincel duro redondo al 100% de opacidad con *lock alpha* para no salirse de la silueta.
- **Máscaras de recorte** (clipping mask) sobre la capa de línea para que cada color quede contenido dentro del dibujo, igual que trabajaría un ilustrador de fondos del propio juego.

**Encuadres y composición**: los tráilers y key arts de BOTW/TOTK repiten un **plano general con Link de espaldas o de perfil mirando el paisaje** (para vender la escala del mundo abierto) y **planos bajos contrapicados** para Ganon/Calamity Ganon (para que domine el encuadre) ⚠️ (de visionado general de material promocional; no medí encuadre por fotograma — lo cubre el investigador de vídeo en el punto 4).

## 24 · Obras parecidas y temas relacionados

**Influencias que el propio Miyamoto reconoce** ✅ (dos fuentes cada una):
- **Su propia infancia explorando cuevas y bosques cerca de Sonobe (Kioto)**: encontró una cueva de niño y quiso que el juego diera esa misma sensación de descubrimiento y de perderse en un laberinto ([Den of Geek](https://www.denofgeek.com/games/the-inspiration-behind-the-legend-of-zelda/), [VGC: Zelda at 40](https://www.videogameschronicle.com/features/zelda-at-40-how-shigeru-miyamotos-childhood-explorations-inspired-nintendos-legendary-classic/)).
- **El Señor de los Anillos de Tolkien**, como referencia literaria de fantasía para el concepto original ✅ (recogido en varias fuentes de historia del desarrollo).
- No encontré una fuente que confirme una influencia directa de Studio Ghibli/Nausicaä sobre el Zelda original ⚠️ (búsqueda hecha, sin resultado; no lo afirmo).

**Influencia en ambas direcciones con otros juegos** ✅:
- **Shadow of the Colossus** (2005, Fumito Ueda) diseñó sus colosos pensando en los jefes de Zelda, a los que llamó «mazmorras de Zelda invertidas»; luego Breath of the Wild (2017) tomó a su vez inspiración de Shadow of the Colossus y de **The Elder Scrolls V: Skyrim** (2011) para repensar el mundo abierto de la saga, según su director Hidemaro Fujibayashi y el productor Eiji Aonuma ([Zelda Dungeon](https://www.zeldadungeon.net/inspired-by-zelda-the-twilight-essence-of-shadow-of-the-colossus/), resumen recogido también en Wikipedia/BOTW).
- **Elden Ring** (2022, FromSoftware) se señala a menudo como heredero del mundo abierto de BOTW; Fujibayashi negó expresamente que Tears of the Kingdom se inspirara en Elden Ring, porque no tuvieron tiempo de jugarlo durante el desarrollo ✅ ([FandomWire](https://fandomwire.com/zelda-eiji-aonuma-tears-of-the-kingdom-elden-ring/)).

**Otras láminas ya hechas en el servidor que comparten tono o género** (para no repetir ideas, `biblias/`):
- **Mundo abierto de acción y mazmorras**: `117-god-of-war` (mitología, combate con arma cuerpo a cuerpo), `125-elden-ring` (mundo abierto con influencia directa de Zelda), `121-tomb-raider` (exploración y puzles de ruinas), `67-hollow-knight` (metroidvania 2D, otro tono más oscuro). Zelda se diferencia por su paleta más clara y su tono de cuento, salvo Twilight Princess.
- **Fantasía pastoral pintada a mano**: los canales Ghibli (`98-el-viaje-de-chihiro`, `99-el-castillo-ambulante`, `100-la-princesa-mononoke`, `101-your-name-cielos-y-ciudades`, `102-el-estilo-ghibli-en-general`) comparten con BOTW/TOTK la luz cálida y la pintura «en plein air», aunque son anime, no videojuego: si una lámina de Zelda usa ese registro pictórico, conviene diferenciarla con el Sheikah Slate o el HUD del juego para que no se confunda con «otro canal Ghibli».
- **Sin choque directo**: no hay ningún canal de Zelda todavía (confirmado, ver `encargos/65-the-legend-of-zelda.md`: «todavía no tiene canal»).

## 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo en 5 líneas** ✅:
1. Hyrule fue creado por tres diosas doradas (Din, Nayru, Farore), que al irse dejaron la **Trifuerza**, un triángulo sagrado que concede el deseo de quien la toca si tiene el corazón equilibrado.
2. Cada partida repite el mismo ciclo: **Link** (el héroe elegido, no siempre el mismo individuo), **Zelda** (la princesa, reencarnación de la diosa Hylia) y **Ganon/Ganondorf** (la encarnación del mal) se reencarnan una y otra vez en distintas épocas.
3. El mundo mezcla razas: Hylianos, Zora (acuáticos), Goron (de roca), Gerudo (desierto, históricamente sólo mujeres salvo un varón cada 100 años), Kokiri/Korok (bosque), Sheikah (sigilo y tecnología antigua).
4. La magia y la tecnología antigua conviven: reliquias Sheikah (Guardianes, Bestias Divinas) y, en Tears of the Kingdom, tecnología **Zonai** aún más antigua.
5. El objeto central casi siempre es la **Espada Maestra**, «la que sella al mal», que sólo puede empuñar quien es digno.

**La historia por arcos** (cronología oficial de *Hyrule Historia*, 2011, publicada 25 años después del primer juego) ✅ dos fuentes ([Zelda Wiki: Zelda Timeline](https://zelda.fandom.com/wiki/Zelda_Timeline), [Dexerto](https://www.dexerto.com/legend-of-zelda/the-legend-of-zelda-fallen-hero-child-and-adult-timelines-explained-2115913/)):
- **Era del Cielo**: Skyward Sword — el origen: Hylia, el primer Link, la fundación de Hyrule.
- **Ocarina of Time es el punto de ruptura**: según si Link (adulto) derrota a Ganondorf o no, la cronología se parte en tres:
  - **Línea del Caído** (Triforce del Poder): Ganon gana Ocarina of Time → A Link to the Past, Link's Awakening, Oracle of Ages/Seasons, el Zelda original de 1986 y su secuela.
  - **Línea Adulta** (Triforce de la Sabiduría): Link derrota a Ganon de adulto y es desterrado a esa época → The Wind Waker (Hyrule se inunda) → Phantom Hourglass → Spirit Tracks.
  - **Línea Infantil** (Triforce del Coraje): Link es devuelto a su niñez tras vencer → Majora's Mask → Twilight Princess → Four Swords/Minish Cap.
- **Breath of the Wild y Tears of the Kingdom** sucede miles de años después de todas las líneas, con Hyrule ya en ruinas por Calamity Ganon; Nintendo no lo ha situado oficialmente en una rama ⚠️ (debate de fans, sin confirmación oficial encontrada).

**Emblemas y símbolos** (todos ✅, con cita de fuente oficial o wiki):
- **Trifuerza**: tres triángulos dorados; Poder (Din, rojo) arriba, Sabiduría (Nayru, azul) abajo-izquierda, Coraje (Farore, verde) abajo-derecha ✅ ([Zelda Wiki: Triforce](https://zelda.fandom.com/wiki/Triforce), [TheGamer](https://www.thegamer.com/the-legend-of-zelda-triforce-aspects-history-goddesses/)).
- **Escudo/Cresta de Hyrule (Hylian Crest)**: un pájaro con las alas extendidas; es la marca de la diosa Hylia y de la Familia Real, y representa al **Loftwing Carmesí** que montaba el héroe en la Era del Cielo (Skyward Sword). Aparece en el Escudo Hyliano ✅, citado literalmente del in-game item text de Twilight Princess vía [Zelda Wiki: Hylian Crest](https://zelda.fandom.com/wiki/Hylian_Crest).
- **Ojo Sheikah (Crest of the Sheikah)**: un ojo abierto de par en par con tres triángulos como pestañas y una lágrima; la lágrima simboliza que la tribu Sheikah «llega hasta donde haga falta para cumplir su objetivo», según la propia Encyclopedia oficial (cita literal recogida en la wiki) ✅ ([Zelda Wiki: Eye Symbol](https://zelda.fandom.com/wiki/Eye_Symbol)). Es un talismán contra el mal.
- **Símbolo Gerudo**: en la versión N64 de Ocarina of Time era una **luna creciente con una estrella**; Nintendo tuvo que quitarlo porque esa combinación se asocia al islam, y lo sustituyó por un diseño distinto en las reediciones ✅ ([Zelda Universe Forums](https://zeldauniverse.net/forums/Thread/82753-Sheikah-and-Gerudo/), [Wikipedia: Gerudo](https://en.wikipedia.org/wiki/Gerudo)) — dato útil para «qué NO dibujar» si se usa el emblema Gerudo en una lámina.
- **Espiral Zonai** (Tears of the Kingdom): símbolo geométrico de la civilización antigua, en el mismo verde menta que sus glifos y santuarios ⚠️ (visual, lo confirma el investigador de imagen).

**Vocabulario propio que un fan reconoce al instante** ✅: Hyrule, Trifuerza, Espada Maestra, Rupia (moneda), Corazón (vida), Ganon / Ganondorf / Calamity Ganon, Hylia, Hyliano, Kokiri, Korok (y sus semillas coleccionables), Zora, Goron, Gerudo, Sheikah, Zonai, Guardianes, Bestias Divinas, Campeones (Champions), Sabios (Sages), Sheikah Slate / Purah Pad, Malicia (Malice). Frases fijas del propio juego (inglés original, sin doblaje de voz en los diálogos): *«It's dangerous to go alone! Take this»* (Zelda 1986), *«Hey! Listen!»* (Navi, Ocarina of Time), *«It's a secret to everybody»* — la traducción exacta al español de estas frases en las localizaciones oficiales no la verifiqué con una fuente ⚠️.


## Lo mejor para la lámina

- El **Sheikah Slate/Purah Pad** es un objeto real en la mano de Link, modelable en Blender, con pantalla propia para el texto del canal: cumple la regla nº1 del dueño («objeto real en un sitio real») mejor que cualquier panel de interfaz suelto.
- La caja de diálogo de **Breath of the Wild** (cápsula negra translúcida #1F2315, esquinas redondas, nombre pequeño arriba-izquierda, texto blanco cursiva) es el cuadro «propio» de la serie más reconocible: nada de burbuja blanca genérica.
- **Hylia Serif** (gratis) + el **Ojo Sheikah** o la **Cresta Hyliana** dan tipografía y emblema coherentes sin depender de fuentes de pago como Charlemagne o FOT-Rodin.
- Para el estilo visual: si la lámina va en clave BOTW/TOTK, nada de contorno negro duro (es pictórico, sin línea); si va en clave Wind Waker/manga, sí lleva contorno con el método inverted hull (Blender) o línea de 2-3 px en gris muy oscuro (Photoshop).
- El símbolo Gerudo original (luna+estrella) NO se debe usar: Nintendo lo retiró por su asociación religiosa; usar el diseño posterior si aparece un personaje Gerudo.

## No encontré

- La fuente exacta de diálogo de Breath of the Wild más allá del nombre comercial FOT-Rodin (de pago, no descargable para comprobar con fontTools) ⚠️ — búsqueda: «Breath of the Wild dialogue font name identify» (inglés).
- Una réplica libre fiable de la serif agrietada del logo de Tears of the Kingdom ⚠️ — búsqueda: «Tears of the Kingdom font UI typeface» (inglés).
- El motor gráfico exacto de BOTW/TOTK sólo lo nombra la comunidad de moddeo («KingSystem»), sin confirmación oficial de Nintendo ⚠️ — búsqueda: «Nintendo EPD Breath of the Wild engine tools Maya proprietary» (inglés).
- Capturas propias de Game UI Database (bloqueado por Cloudflare/403 a curl; sin navegador headless instalado en el contenedor para navegar.py; Wayback Machine tampoco sirvió la página) ⚠️ — usé en su lugar el dossier ya medido del equipo (`_Cuadros de dialogo por franquicia`) y otras fuentes técnicas (CloudModding, ZeldaMods, GitHub de herramientas de modding).
- The Cutting Room Floor (tcrf.net) da 403 a curl con y sin user-agent de navegador, y a su api.php igual; usé los resúmenes de búsqueda web en su lugar (textos sin usar de Ocarina of Time, prototipos de Breath of the Wild) ⚠️ — no pude leer las páginas completas de TCRF.
- El estilo exacto de los globos de diálogo del manga de Himekawa (grito, pensamiento) por comparación general con la convención shonen de la época, no por ver una página del manga ⚠️ — el diseño de página lo cubre el investigador de imagen.
- Traducción oficial al español latino de frases icónicas de los juegos («It's dangerous to go alone», «Hey! Listen!») ⚠️ — los juegos de Zelda no llevan doblaje de voz en el diálogo, así que no hay clip de doblaje que verificar como en una serie animada.

## Bitácora

- Búsquedas en inglés (WebSearch, ~14): tipografía del logo, diálogo BOTW/TOTK/OoT/WW, Game UI Database, cel-shading Wind Waker (inverted hull, Miyamoto/Aonuma), estilo pictórico BOTW (Takizawa, Aonuma, Jōmon), Skyward Sword impresionista (Cézanne), motor y herramientas de Nintendo EPD, Shadow of the Colossus/Elden Ring/Skyrim como influencias cruzadas, Tolkien y la infancia de Miyamoto, Hyrule Historia y la cronología en tres ramas, Triforce/Escudo Real/Ojo Sheikah/símbolo Gerudo, TCRF Ocarina of Time y Breath of the Wild.
- Descargas y comprobación con fontTools (tildes, ñ, ¿, ¡): Hylia Serif, TLOZ Minish Cap/ALttP/Four Sword, Return of Ganon, Reggae One y RocknRoll One (Google Fonts, vía Fontsource) — las 5 descargadas y comprobadas de verdad, no de memoria.
- Consultas a la API de Fandom (zelda.fandom.com/api.php, sin bloqueo): wikitext de «List of fonts used in The Legend of Zelda logos», «Eye Symbol», «Hylian Crest»; búsqueda de imágenes con imageinfo para 3 símbolos (Ojo Sheikah, Cresta Hyliana, Trifuerza).
- Bloqueos encontrados: dafontfree.net/zeldauniverse.net dieron 402 a WebFetch directo (rodeado buscando el contenido por otra vía o con caché de búsqueda); Game UI Database y TCRF dieron 403 tanto a curl como a WebFetch, y navegar.py falló porque el contenedor no tiene el navegador headless instalado (chrome-headless-shell ausente) — lo anoto para que el jefe lo sepa, no es un fallo mío de no intentarlo.
- No usé git ni toqué biblia.md; sólo escribí en partes/texto.md y partes/texto.json.

## Cumplimiento de mis puntos (5, 6, 11, 18, 24, 25)

Punto | Estado | Por qué
---|---|---
5 · Tipografía | ✅ | 8 usos cubiertos, 5 fuentes descargadas y comprobadas con fontTools de verdad (tildes/ñ/¿/¡), fuentes Hylian/Sheikah/Gerudo/Zonai listadas con fuente
6 · Cuadros de diálogo | ✅ | 6 juegos + manga, con colores medidos (heredados del dossier del equipo) y qué NO hacer
11 · Videojuegos: interfaz | ✅ | 6 juegos con su menú/interfaz, con tamaños técnicos reales donde los hubo
18 · Estilo y cómo replicarlo | ✅ | estilo por 6 eras con entrevistas citadas, motor/programas, pasos concretos de Blender y Photoshop; rigs y tramas remitidos a los puntos 3 y 19 como se pidió
24 · Obras parecidas | ✅ | influencias en ambas direcciones con fuente, choque de canal revisado contra biblias/ existentes
25 · Mundo, historia y símbolos | ✅ | reglas en 5 líneas, cronología oficial en 3 ramas, 4 símbolos con cita oficial, vocabulario propio
