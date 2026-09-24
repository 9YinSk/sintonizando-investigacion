# Investigador de TEXTO, JUEGOS Y TÉCNICA · Demon Slayer: paisajes y auras

Puntos de `ENCARGO.md`: **5** (tipografía), **6** (cómo hablan y piensan en pantalla), **11** (videojuegos), **18** (estilo y cómo replicarlo, con foco en Ufotable), **24** (obras parecidas) y **25** (mundo, historia y símbolos — aquí con **peso especial en los símbolos visuales de cada respiración/aura**, tal y como pide `encargos/79-demon-slayer-paisajes-y-auras.md`).

**Aviso importante sobre `partes/datos-texto.md`**: el AniList que trajo `recolectar.py` (id 21612) es el de **«Onigiri» (Studio Signpost, 2016, TV_SHORT)**, un anime corto sobre un videojuego MMORPG que en inglés también se llama «Demon Slayer» — **no** es Kimetsu no Yaiba de Ufotable. Los «Videojuegos en Steam» de ese archivo (Onigiri Shop Simulator, Onigiri Support Pack…) tampoco son de esta franquicia. **No usé nada de `datos-texto.md`**: repetí la consulta a AniList a mano con el título exacto y el id correcto es **101922**. Los datos de imagen (`datos-imagen.md`) sí apuntan bien a `kimetsu-no-yaiba.fandom.com`, así que confirmo que esa es la wiki correcta.

Ya miré `biblias/31-demon-slayer-kimetsu-no-yaiba/biblia.md` (repaso general de la misma serie) para no repetir la investigación básica de tipografía y mundo — la cito donde reaproveché un dato, y añado verificación propia y hallazgos nuevos centrados en paisajes y auras. Trabajo pesado en `/tmp/claude-0/trabajo/79-demon-slayer-texto/`.

## Hallazgos

### 5 · Tipografía

- **Logo japonés** 鬼滅の刃: caligrafía a pincel propia (no es una fuente comercial), negra, dentro de un sello circular blanco con aro rojo, furigana きめつのやいば encima. **Logo occidental** «DEMON SLAYER»: **Blood Crow Condensed** (Iconian Fonts, gratis sólo no comercial). **Web oficial** (kimetsu.com, demonslayer-anime.com): **Zen Old Mincho** + **Noto Serif JP** con **YakuHanMP** para la puntuación, leído en su CSS. **Web del juego** *Hinokami*: **Cinzel** (títulos latinos) + **Noto Serif JP**, leído en su HTML. ✅ ya verificado con fontTools por `biblias/31-demon-slayer-kimetsu-no-yaiba/biblia.md` §6.1-6.2 (dafontonline, FontBolt, CSS/HTML propios).
- **Verificación propia, independiente** (bajé los .ttf de la CDN de Fontsource y corrí `fontTools.ttLib.TTFont(f).getBestCmap()` yo mismo, no copié el resultado ajeno): **Cinzel** (`cinzel@latest/latin-400-normal.ttf`, OFL) y **Zen Old Mincho** Black (`zen-old-mincho@latest/latin-900-normal.ttf`, OFL) → **á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü Ü: todos presentes** en ambas. ✅ (dos verificaciones independientes: la mía + la de la biblia hermana).
- **Letra para paisajes/carteles del mundo**: sigo la tabla ya hecha en la biblia hermana (§6.2): **Zen Antique** y **Kaisei Decol** para carteles de madera/época Taishō, **Yuji Syuku/Boku/Mai** para pincel vertical (cartelas de nombre), **Dela Gothic One** para onomatopeyas. Todas OFL, con kanji, ya comprobadas con fontTools por esa biblia. ✅ (cito, no repito la descarga).
- **Videojuego *Demon Slayer -Kimetsu no Yaiba- Sweep the Board!*** (Steam, hallazgo propio, ver punto 11): en las capturas oficiales, los carteles de las tiendas del tablero (八山商店, 十兵衛塾…) usan una **rotulación vertical gruesa de estilo Edo/Taishō** (parecida a Yuji Boku/Kaisei Decol) pintada a mano sobre fondo de tela colgante (noren); no identifiqué la fuente exacta del HUD del juego (números de turno, menús) porque las capturas de Steam no muestran menús, sólo el tablero y las celebraciones de personajes. ⚠️ una fuente (capturas oficiales de Steam), sin menú visible.
- **Interfaz de los juegos de pelea** (*Hinokami Chronicles* 1 y 2): la biblia hermana ya leyó el HTML de `game.kimetsu.com/hinokami` → **Cinzel + Noto Serif JP**. ✅ cito esa lectura directa de código, no la repetí.

### 6 · Cómo hablan y piensan en pantalla

- **Nunca un globo blanco genérico**: confirmado también por la biblia hermana (§7, «Demon Slayer no habla con globos blancos»). Lo que aparece en pantalla es siempre **caligrafía, madera, papel o un escenario real**. ✅.
- **El «Secreto de la era Taisho»** (大正コソコソ噂話) es el recurso de texto+paisaje más importante de toda la serie para esta biblia: cada versión usa un **fondo/paisaje distinto** como soporte del texto — la gran ola ukiyo-e azul (T1), una tablilla de madera «その1» sujeta a mano (Herreros/Pilares), o un escenario de teatro con telón rojo `#B91F2A` y luces (versión Pilares de Crunchyroll). Es decir: **el fondo cambia, pero el texto siempre se apoya en un objeto u paisaje físico**, nunca flota solo. ✅ ya visto y citado con minuto por la biblia hermana (§7.1); lo reaprovecho porque es la clave de estilo para las cartelas de ESTA biblia (paisajes).
- **La casa/refugio marcada con el emblema de glicina (wisteria) en la puerta**: en el capítulo/episodio 14, el trío de Tanjiro llega de noche a una casa con **un blasón familiar de flor de glicina en la verja** (「藤の花の家紋」), señal de que ahí los Cazademonios pueden quedarse gratis y a salvo. Es un **símbolo real pintado en un objeto físico de un paisaje** (una puerta) que funciona como «cartel» sin usar ni una palabra. ✅ [Episode 14, wikitext de la wiki](https://kimetsu-no-yaiba.fandom.com/wiki/Episode_14) (confirmado también en la ficha de [Wisteria](https://kimetsu-no-yaiba.fandom.com/wiki/Wisteria): «the family designed their family crest with a wisteria flower so Corps members would be able to identify the home»).
- **El cuervo mensajero** (鎹鴉) habla en pantalla como un telegrama («¡Orden! ¡Orden!», gramática cortada) — ya lo tiene la biblia hermana con minuto exacto (T1-21, 00:17:32) ✅, lo cito para no repetir el visionado.
- **En los videojuegos**: no encontré una caja de diálogo del modo historia de *Hinokami Chronicles* con interfaz visible (las capturas oficiales y las de Steam vienen sin HUD) — mismo resultado ⚠️ que ya reportó la biblia hermana. En ***Sweep the Board!*** tampoco hay captura con caja de texto/menú entre las 7 disponibles en Steam: sólo el tablero y animaciones de personajes. ⚠️ **sin verificar** en ningún juego de la franquicia.
- **Qué SÍ hacer para esta biblia (paisajes)**: cualquier texto de la lámina debería ir sobre un **objeto real dentro de un paisaje** (una tablilla de madera, una puerta con un blasón, un cartel de tienda), nunca flotando — es literalmente el patrón que usa la serie en el 100% de lo que miré.

### 11 · Videojuegos de la franquicia

Repetí la búsqueda en la **API de Steam directamente** (no en el buscador, para evitar el mismo error del id de AniList) con `storesearch` para «Kimetsu no Yaiba» y `appdetails` para cada juego encontrado. Encontré **un juego que la biblia hermana no tiene**: *Sweep the Board!*.

| Juego | Datos (Steam API, `appdetails`) | Qué sirve para paisajes/auras |
|---|---|---|
| ***The Hinokami Chronicles*** | CyberConnect2 / SEGA · 15-oct-2021 · appid 1490890 (id interno de datos 1996370) · 7 capturas 1920×1080 | modo historia hasta Mugen Train; ✅ (Steam API, comprobado hoy) |
| ***The Hinokami Chronicles 2*** | CyberConnect2 / SEGA · 5-ago-2025 · appid 2928600 (id interno 4010480) · 5 capturas 1920×1080 | vi una captura del templo de Gyomei con todos los Pilares en tatami; el rosario/estola de Gyomei lleva bordado 南無阿弥陀仏 (mantra budista «Namu Amida Butsu»), otro símbolo real del mundo ✅ (mirado directamente, `hinokami2_1.jpg`) |
| ***Sweep the Board!*** (**hallazgo propio**, no está en `datos-texto.md` ni en la biblia hermana) | CyberConnect2 / SEGA · 16-jul-2024 · appid 2424110 · 7 capturas 1920×1080 · géneros Action/Casual/Simulation | **juego de mesa virtual (sugoroku)**: el tablero ES un mapa en miniatura isométrico del mundo de la serie — un santuario de glicinias con pilares rojos y niebla en el bosque, un pueblo de época Taishō con río, puente de madera y tiendas con rótulos verticales, y una plaza europea con fuente y torre de reloj. Las celebraciones de personajes usan versiones **chibi/2D recortadas sobre el tablero 3D**: mezcla 2D+3D igual que el anime (ver punto 18). ✅ mirado directamente en dos capturas oficiales (1920×1080, medidas con Pillow) |
| *Sweep the Board!* — descripción oficial | «virtual board game... events and minigames with up to four players offline or online» | ✅ [Steam](https://store.steampowered.com/app/2424110) |

- **The Cutting Room Floor**: repetí la búsqueda de «Hinokami Chronicles» — **sin resultados**, mismo resultado ⚠️ que ya tiene la biblia hermana; no hay página del juego en TCRF.
- Otros juegos de móvil/colaboración (*Nichirin Battle Slash*, *Puzzle & Dragons*, *Shironeko Project*, *Kotodaman*) ya listados por la biblia hermana; no los repetí. ✅ cito.

### 18 · Estilo de dibujo y técnica, y cómo replicarlo (foco: paisajes, respiraciones y efectos de Ufotable)

Este es el punto que más pesa en esta biblia. Hice mi propia búsqueda (no repetí la de la hermana) y encontré **dos entrevistas técnicas nuevas** con nombres, software y cifras concretas.

- **Software confirmado**: ufotable usa **Autodesk 3ds Max** como herramienta principal de CG, con los plugins **V-Ray** (render), **PhoenixFD** (simulación de fluidos: agua y fuego), **tyFlow** (partículas: los efectos de «aura» de las respiraciones), **ForestPack** y **RailClone** (vegetación y arquitectura procedimentales — bosques y calles repetidas), **GrowFX** (plantas) y **Pencil+** (línea de estilo *toon* sobre geometría 3D, el puente entre 3D y el look 2D de la serie). Cita textual del director 3D: «la mayor parte de los cortes CG de Kimetsu fueron creados con 3ds Max y sus plugins». ✅ [Autodesk AREA Japan, parte 1](https://area.autodesk.jp/case/animation/kimetsu-01/) y [parte 2](https://area.autodesk.jp/case/animation/kimetsu-02/) (japonés, leídas con WebFetch).
- **Cómo se hacen los efectos de las respiraciones**: para la respiración del agua de Tanjiro, el director 3D **Kazuki Nishiwaki** hizo múltiples pruebas en 3ds Max investigando **obras tradicionales japonesas** (referencias ukiyo-e), y el equipo decidió caso por caso qué parte del efecto es **animación tradicional a mano** y qué parte es CGI, con iteración constante junto al director. ✅ misma fuente.
- **Investigación de paisajes reales**: el equipo **visitó bosques de verdad varias veces** para las escenas de naturaleza; cita de Nishiwaki: «no podíamos lograr bosques realistas sólo colocando árboles — detalles como la acumulación de nieve alrededor de los troncos y la disposición de la maleza necesitan fotografía de referencia real». ✅ misma fuente. Esto confirma que los fondos «pintados, casi fotográficos» que ya notó la biblia hermana (§18.1) vienen de **documentación de campo**, no sólo de imaginación.
- **Escala del renderizado 3D creció con los años** (cita de **Yūichi Terao**, director de fotografía de ufotable, entrevistado por Popverse en la San Diego Comic-Con): en el episodio 26 (*Unwavering Resolve*, 2019) «lo máximo que podíamos expresar en 3D era un espacio de unos 100×100 metros»; en el episodio 45 (*Swordsmith Village*, 2023) ya podían «pintar visualmente un fondo de unos dos kilómetros cuadrados»; para la película *Infinity Castle* (2025) «la velocidad de renderizado se multiplicó por diez» y los operadores de datos 3D trabajan «6,5 veces más rápido». Objetivo declarado: que el Castillo Infinito «casi parezca infinito» al verlo en pantalla. ✅ [Popverse: Yuichi Terao interview](https://www.thepopverse.com/movies-demon-slayer-kimetsu-no-yaiba-yuichi-terao-interview-making-the-infinity-castle-feel-infinite).
- **El Castillo Infinito como «paisaje imposible»**: gravedad deformada — los demonios pueden estar de pie en el suelo, boca abajo o perpendiculares en una pared a la vez; toda la estructura la controla a voluntad la demonio Nakime con su *biwa* (Arte Demoníaco de Sangre), y el castillo también se mueve por sí solo. Es el paisaje más extremo de toda la serie y el que más CG nuevo necesitó (ver cifra de los 2 km² arriba). ✅ [Infinity Castle, wikitext](https://kimetsu-no-yaiba.fandom.com/wiki/Infinity_Castle).
- **Equipo humano y cifras de la película** (ya citado por la biblia hermana desde la misma entrevista de los Oscars; lo confirmo sin repetir el vídeo): +2.200 planos a mano, 5 veces más animadores 2D que de CG, dirección de Haruo Sotozaki, dirección de animación jefe Akira Matsushima, *storyboard* de Toshiyuki Shirai, fotografía de Yuichi Terao. ✅ [ufotable en los Oscars, YouTube](https://www.youtube.com/watch?v=FLB_sLTgbPk).
- **Cómo reproducirlo en Photoshop y Blender** (propuesta mía a partir de lo anterior — marcar como propuesta, no cita textual):
  - **Agua y fuego de las respiraciones**: PhoenixFD ≈ el dominio de fluidos **Mantaflow** de Blender (agua) y su simulación de fuego/humo (llama); sobre la simulación base, **pintar a mano encima** (Grease Pencil o una capa 2D en Photoshop) los remolinos y espuma tipo ukiyo-e — así es como lo hace ufotable (3D base + dibujo clave encima), no un shader automático.
  - **Partículas de aura** (rayo, enjambre de insectos, viento, chispas): tyFlow ≈ el sistema de partículas o **Geometry Nodes** de Blender para dispersar sprites/mallas con movimiento.
  - **Línea y sombreado**: Pencil+ (3ds Max, línea *toon* con grosor variable y a veces de color) ≈ **Line Art (Grease Pencil)** o **Freestyle** en Blender, con grosor modulado por distancia a cámara; usar línea de **color** (rojo/azul/verde, como el lápiz de marcar sombras de ufotable en sus dibujos clave — visto en el vídeo de los Oscars, 0:29-0:44) en vez de negro puro para las zonas de sombra.
  - **Bosques y calles**: ForestPack/RailClone ≈ **Geometry Nodes** con dispersión sobre el terreno (para árboles) y **arrays/instancias** (para casas, faroles, cercas) — pero, como dice Nishiwaki, conviene partir de **fotos de referencia reales** del elemento (musgo en la base de un tronco, maleza) antes de dispersarlo.
  - **Fotografía/composición final** (el departamento 撮影 de Terao): profundidad de campo, niebla/neblina atmosférica en capas, *bloom* en las fuentes de luz, grano fino, y corrección de color cálida/fría según el ánimo de la escena — aplicable como *compositor* de Blender o ajustes por capas en Photoshop.
  - **Encuadre**: alternar **plano general de paisaje** (para mostrar la escala, como el bosque de 2 km² del pueblo de herreros) con **primer plano muy cerrado** de cara en el clímax emocional — mismo patrón que ya notó la biblia hermana con la altura de cámara del *engawa*. ✅ cito ese dato puntual (§18.5), el resto es hallazgo propio.

### 24 · Obras parecidas y temas relacionados

- **Recomendaciones del propio público de AniList** (id **101922**, la ficha correcta — repetí la consulta porque `datos-texto.md` traía el id equivocado): **Jujutsu Kaisen** (nota 84, 3.343 votos), **Hunter x Hunter (2011)** (89, 103 votos), **Hell's Paradise** (80, 148 votos), **Dororo** (81, 1.945 votos), **Bleach** (79, 385 votos), **Black Clover** (79, 151 votos), **My Hero Academia S4** (78, 335 votos), **Rurouni Kenshin (2023)** (74, 107 votos). ✅ [AniList: Media #101922](https://anilist.co/anime/101922) (consulta GraphQL propia, 24-sep-2026).
- **Influencias que el propio Koyoharu Gotouge reconoce**: en entrevistas, sus tres mangas de mayor influencia son **JoJo's Bizarre Adventure**, **Naruto** y **Bleach** (el *Gotei 13* de Bleach salió mucho en reuniones con su editor); **Yu Yu Hakusho** y **Rurouni Kenshin** marcaron su forma de narrar. La inspiración directa para Tanjiro es **Kenshin Himura** de *Rurouni Kenshin*: pelo rojo, cicatriz en la cara y el mismo principio de no matar salvo que sea imprescindible. ✅ [CBR: Fun facts about Koyoharu Gotouge](https://www.cbr.com/koyoharu-gotouge-demon-slayer-creator-trivia-fun-facts/) + [ScreenRant: Demon Slayer's creator confirms JoJo influence](https://screenrant.com/demon-slayer-jojos-bizarre-adventure-surprising-influence/).
- **Obras del propio Ufotable con el mismo lenguaje visual de efectos** (esto es lo que pide en concreto el encargo: «los efectos de Ufotable»): la saga **Fate** (*Fate/Zero*, *Fate/stay night: Unlimited Blade Works*, *Heaven's Feel*) es el otro gran catálogo de Ufotable con el mismo estilo de **efectos elementales cinematográficos** (fuego, agua, energía mágica) mezclando 2D y CG con el mismo departamento de fotografía. ⚠️ una fuente de resumen (Anime News Network, ficha de la compañía) — no encontré una entrevista que compare directamente ambas producciones palabra por palabra; lo marco como comparación razonable de catálogo, no cita textual.
- **Qué láminas del servidor ya existen y se parecen** (para que el redactor no repita ideas): ya hay una biblia de **Demon Slayer «repaso general»** (`biblias/31-demon-slayer-kimetsu-no-yaiba/`) que propuso el canal **🔊 Aula** con la clase de respiración de la Mansión Mariposa y usó como fondo **el «Secreto de la era Taisho»** y **el shamisen de Zenko** (`que-estas-escuchando`). También hay biblias ya completas de **Jujutsu Kaisen** (`biblias/32-jujutsu-kaisen/`, conceptos «Clase extra», «Baja el velo», «¡Salmón!») y **Attack on Titan** (`biblias/02-attack-on-titan/`, «Reglamento del cuartel», «La sentencia», «¡Consagren sus corazones!») con tono de poderes/efectos sobrenaturales parecido. **Para esta biblia (paisajes y auras) conviene un concepto distinto a esos tres**: no repetir el Aula ni el Secreto de la era Taisho tal cual, y explorar mejor un canal ligado a **fondos, naturaleza o algo visual/artístico** (`servidor/inventario.md` tiene `🎨・arte`, `📺・que-estas-viendo`, `🍿・noticias-series`) donde el paisaje (no la clase de respiración) sea el protagonista. Queda para el redactor, que es quien decide los 3 conceptos.

### 25 · El mundo, la historia y sus símbolos (énfasis en los símbolos visuales de cada respiración/aura)

**Reglas del mundo en 5 líneas** (wiki, en inglés, cruzado con las fichas citadas abajo):
1. Japón, era **Taishō** (1912-1926); los demonios existen en secreto y la mayoría de la gente no lo sabe. ✅.
2. El **Cuerpo de Cazadores de Demonios** (鬼殺隊, *Kisatsutai*) no está reconocido por el gobierno japonés y se financia sólo con la fortuna de la **familia Ubuyashiki**. ✅ [Demon Slayer Corps](https://kimetsu-no-yaiba.fandom.com/wiki/Demon_Slayer_Corps).
3. Sólo decapitar a un demonio con una **espada Nichirin** (forjada con mineral que absorbe la luz solar en el monte Yoko) lo mata de verdad; la luz del sol también los destruye. ✅ [Nichirin Sword](https://kimetsu-no-yaiba.fandom.com/wiki/Nichirin_Sword).
4. Los demonios nacen de la sangre de **Muzan Kibutsuji**, que se convirtió en el primer demonio al tomar una medicina experimental hecha con la **Glicina Azul** (青い彼岸花), una flor mítica que sólo florece 2-3 días al año, de día — por eso Muzan lleva siglos buscándola para curar su debilidad al sol. ✅ [Blue Spider Lily](https://kimetsu-no-yaiba.fandom.com/wiki/Blue_Spider_Lily).
5. La **glicina (wisteria, 藤)** repele y envenena a los demonios: se usa como incienso protector, para atraparlos en el monte Fujikasane durante la Selección Final, y su flor en el blasón de una casa marca un refugio seguro para los Cazadores. ✅ [Wisteria](https://kimetsu-no-yaiba.fandom.com/wiki/Wisteria).

**Las 13 respiraciones y su símbolo/color** — tabla completa, sacada del wikitext de la página general de respiraciones (una sola fuente wiki, pero cita capítulo/tomo del manga como respaldo primario, y coincide con lo medido por el investigador de imagen/vídeo en vestuario y efectos):

| Respiración (kanji) | Color asociado | N.º de formas | Quién la usa |
|---|---|---|---|
| **Sol (日)** — Hinokami Kagura, el origen de todas | Negro | 13 | Yoriichi Tsugikuni, la familia Kamado (Tanjiro) |
| **Agua (水)** | Azul | 11 | Giyu Tomioka, Tanjiro Kamado, Sakonji Urokodaki |
| **Llama (炎)** | Naranja-rojo | 9 | Kyojuro Rengoku, Shinjuro Rengoku |
| **Trueno (雷)** | Amarillo | 7 | Zenitsu Agatsuma, Jigoro Kuwajima |
| **Viento (風)** | Verde | 9 | Sanemi Shinazugawa |
| **Piedra (岩)** | Gris | 5 | Gyomei Himejima |
| **Bestia (獣)** | Gris índigo | 11 | Inosuke Hashibira |
| **Insecto (蟲)**, de Agua | Azul lavanda | 5 | Shinobu Kocho |
| **Serpiente (蛇)**, de Agua | Lavanda | 5 | Obanai Iguro |
| **Amor (恋)**, de Llama | Rosa oscuro | 6 | Mitsuri Kanroji |
| **Sonido (音)**, de Trueno | Ámbar | 5 | Tengen Uzui |
| **Niebla (霞)**, antigua | Blanco | 7 | Muichiro Tokito |
| **Flor (花)**, antigua | Rosa claro | 7 | Kanae y Kanao Kocho/Tsuyuri |
| **Luna (月)** | Púrpura claro | 16 | Kokushibo |

✅ [Breathing Style, wikitext completo](https://kimetsu-no-yaiba.fandom.com/wiki/Breathing_Style) (leído con `action=parse&prop=wikitext`, tabla íntegra). **Dato clave para el diseño del «aura»**: la propia wiki cita el tomo 17 (extra pages) — *«las respiraciones no liberan de verdad su ataque elemental; la gente que lo ve sólo cree verlo y sentirlo, es un efecto visual»* — **excepto** la Respiración del Trueno, cuyos usuarios sí vibran el aire y producen un sonido real de trueno con sus pasos. Es decir: el aura de agua/fuego/viento es **una metáfora visual hecha realidad en pantalla**, no un poder literal — justo la clave para diseñar el efecto de la lámina.
- **Origen y ramificación**: las 5 respiraciones fundamentales (Agua, Llama, Trueno, Viento, Piedra) derivan todas de la **Respiración del Sol** de Yoriichi Tsugikuni; Insecto y Serpiente salen de Agua, Amor sale de Llama, Sonido sale de Trueno, y Bestia sale (de forma «extraña», dice la propia wiki) de Viento. Niebla y Flor son antiguas y sobrevivieron hasta la era Taisho sin que se sepa bien su origen. ✅ misma fuente.

**Las Marcas de Cazador de Demonios (鬼殺痣, *aza*) — el aura hecha piel**: cuando un Cazador supera un límite físico extremo (pulso +200, temperatura +39°C) puede despertar una marca en la piel que **casi siempre repite visualmente el elemento de su respiración** — es el ejemplo más literal de «aura visible» de toda la serie:

| Usuario | Forma de la marca | Dónde |
|---|---|---|
| Tanjiro Kamado | Llamas | lado izquierdo de la frente (creció hasta pasar las cejas) |
| Giyu Tomioka | Corrientes de agua | mejilla izquierda |
| Muichiro Tokito | Nubes de niebla | ambas mejillas y frente izquierda |
| Mitsuri Kanroji | Dos corazones alados enfrentados | clavícula izquierda |
| Gyomei Himejima | Grietas de tierra | ambos antebrazos |
| Sanemi Shinazugawa | Molino de viento | mejilla derecha |
| Obanai Iguro | Serpientes reptando | hombro y pectoral izq. hasta el antebrazo |
| Yoriichi Tsugikuni / Kokushibo | Llamas | frente/sien izquierda (Kokushibo: hasta la mejilla derecha y el cuello) |

✅ [Demon Slayer Mark, wikitext completo](https://kimetsu-no-yaiba.fandom.com/wiki/Demon_Slayer_Mark) (tabla «Known Demon Slayer Marks», con capítulo/episodio de respaldo). Trivia útil: **Kyojuro Rengoku, Tengen Uzui y Shinobu Kocho nunca despertaron su marca** (Kyojuro y Tengen porque Tanjiro aún no había despertado la suya y no hubo «precursor» de contacto; Shinobu porque no participó en el Entrenamiento de los Pilares). ✅ misma fuente.

**Espadas Nichirin (日輪刀, «espada solar»)**: cambian de color según el usuario al desenvainarlas por primera vez («espadas que cambian de color»), forjadas con **Arena de Hierro Escarlata** hallada en montañas de sol perpetuo como el **monte Yoko**. El color no es libre: **el negro se considera un mal augurio raro** — cuando la espada de Tanjiro se vuelve negra, él mismo teme que sea mala señal, y Sakonji lo calma diciendo que «las espadas negras simplemente son poco comunes» (el herrero Haganezuka, en cambio, se enfada porque esperaba una espada roja). ✅ [Episode 5, wikitext](https://kimetsu-no-yaiba.fandom.com/wiki/Episode_5) + [Nichirin Sword](https://kimetsu-no-yaiba.fandom.com/wiki/Nichirin_Sword). Al llegar a Pilar, la espada se graba con **惡鬼滅殺** (*Akki Messatsu*, «Destructor de demonios»). ✅ misma ficha.

**El Castillo Infinito** (異空間無限城, ver punto 18): paisaje imposible con gravedad deformada, controlado por el Arte Demoníaco de Sangre de Nakime (su *biwa*). Es el símbolo/escenario opuesto a los paisajes naturales (bosque, mansión, aldea) del resto de la serie: el único sitio del mundo que **no obedece física real**. ✅ [Infinity Castle](https://kimetsu-no-yaiba.fandom.com/wiki/Infinity_Castle).

**Los Doce Kizuki (十二鬼月)**: la jerarquía demoníaca en espejo, con **Rangos Superiores (上弦, Jōgen) 1-6** y **Rangos Inferiores (下弦, Kagen) 1-6** — el número de rango va **grabado a fuego en un ojo** de cada demonio (los Superiores llevan además el kanji 上弦 en el otro ojo). Es el equivalente demoníaco de la Marca de Cazador: **cada bando lleva su poder escrito en el propio cuerpo**. ✅ [Twelve Kizuki](https://kimetsu-no-yaiba.fandom.com/wiki/Twelve_Kizuki).

**Vocabulario propio verificado**:
- **«Kamaboko Squad»** (el «Escuadrón Kamaboko»): apodo de fans para el trío Tanjiro-Zenitsu-Inosuke. Nace en el episodio/capítulo 14, cuando Inosuke destroza el nombre «Kamado Tanjiro» y dice «**Kamaboko Gonpachiro**» (かまぼこ, pastel de pescado con un estampado a cuadros parecido al *haori* de Tanjiro). ✅ [Episode 14, wikitext](https://kimetsu-no-yaiba.fandom.com/wiki/Episode_14).
- **Tsuguko** (継子, «sucesor»): aprendiz personal de un Pilar, por aplicación (Genya con Gyomei, rechazado) o por reclutamiento directo. ✅ [Tsuguko](https://kimetsu-no-yaiba.fandom.com/wiki/Tsuguko).
- **Kokyū** (呼吸): «respiración», la base técnica de toda la serie; **Kokyū Hō** (呼吸法) es el nombre formal de «Breathing Style». ✅ [Breathing Style](https://kimetsu-no-yaiba.fandom.com/wiki/Breathing_Style).
- «Hashira» se traduce «Pilar» en el doblaje latino — dato ya verificado por la biblia hermana (§6.3, §14); lo cito, no repito la búsqueda del clip doblado.

## Lo mejor para la lámina

1. La **tabla de las 13 respiraciones con su kanji y color** es material listo para una leyenda o clave visual de auras (agua=azul, llama=naranja-rojo, trueno=amarillo…).
2. La **Marca de Cazador de Demonios** (tabla de formas por Pilar) es el ejemplo más directo de «aura hecha símbolo permanente»: cada patrón puede inspirar un marco decorativo distinto según el canal/tema.
3. El tablero de ***Sweep the Board!*** (captura propia) es una referencia de **paisaje-mapa en miniatura** ya hecha oficialmente: santuario de glicinias + pueblo Taishō + plaza europea, en isométrico 3D con personajes 2D encima — exactamente la mezcla 2D/3D que ufotable usa en el anime.
4. La puerta con el **blasón de glicina** (casa refugio, ep. 14) es un objeto real+símbolo+paisaje en un solo elemento: encaja con la regla del dueño de «un objeto real en un sitio real».
5. La cita de Yuichi Terao sobre el Castillo Infinito («que casi parezca infinito») + la cifra de 2 km² del episodio 45 dan pie a un fondo de profundidad exagerada como concepto de lámina.

## No encontré

- ⚠️ La fuente exacta del HUD/menú de ningún videojuego de la franquicia (ni *Hinokami Chronicles* 1/2 ni *Sweep the Board!*): ninguna captura oficial de Steam muestra menús o cajas de diálogo, sólo juego/cinemáticas. Búsquedas hechas: capturas de las 3 fichas de Steam completas (appdetails), sin resultado.
- ⚠️ Una comparación directa, citada por el propio staff, entre el estilo de efectos de *Fate* y el de *Demon Slayer* (los uso como comparación razonada de catálogo del mismo estudio, no como cita textual).
- ⚠️ Nombre exacto del programa usado para el rotulado de tiendas en *Sweep the Board!* (sin menú de créditos visible en las capturas).
- No es una carencia, es un aviso: **`datos-texto.md` trae el AniList y los juegos de Steam de la serie equivocada** («Onigiri», id 21612) — lo dejo anotado arriba para que nadie más lo reutilice por error.

## Bitácora de búsqueda

- **Fandom** (`kimetsu-no-yaiba.fandom.com`, API `action=parse&prop=wikitext`, en inglés): `Breathing Style`, `Demon Slayer Corps`, `Nichirin Sword`, `Wisteria`, `Blue Spider Lily`, `Demon Slayer Mark`, `Twelve Kizuki`, `Hinokami Kagura`, `Infinity Castle`, `Tsuguko`, `Episode 5`, `Episode 14`. Búsquedas de texto (`list=search&srwhat=text`) para «Hanafuda» (no hay página propia; el dato sale dentro de Hinokami Kagura), «black blade unlucky» y «Kamaboko Squad».
- **AniList** (GraphQL, `graphql.anilist.co`, en inglés): consulta propia por título exacto «Kimetsu no Yaiba» → id correcto **101922** (el de `datos-texto.md`, 21612, es «Onigiri», otro anime); recomendaciones y relaciones.
- **Steam** (API pública, en inglés): `storesearch` para «Kimetsu no Yaiba» y `appdetails` para appid 2928600, 1490890, 2424110 — encontré *Sweep the Board!* que no estaba en `datos-texto.md` ni en la biblia hermana; bajé y miré 2 capturas oficiales con Pillow (1920×1080 exactas).
- **The Cutting Room Floor**: búsqueda `"Hinokami Chronicles" site:tcrf.net` (WebSearch) → sin página.
- **WebSearch** (inglés): «ufotable Demon Slayer photography department background lighting interview», «Koyoharu Gotouge Demon Slayer influences interview Rurouni Kenshin inspiration», «Demon Slayer anime technique name on-screen text kanji».
- **WebSearch** (japonés): «鬼滅の刃 ufotable 背景美術 エフェクト 制作 インタビュー».
- **WebFetch** (leídas completas): [Popverse, entrevista a Yuichi Terao](https://www.thepopverse.com/movies-demon-slayer-kimetsu-no-yaiba-yuichi-terao-interview-making-the-infinity-castle-feel-infinite) (inglés), [Autodesk AREA Japan parte 1](https://area.autodesk.jp/case/animation/kimetsu-01/) y [parte 2](https://area.autodesk.jp/case/animation/kimetsu-02/) (japonés).
- **Fontsource** (`api.fontsource.org` + CDN `cdn.jsdelivr.net/fontsource`): bajé Cinzel y Zen Old Mincho Black en `.ttf` y comprobé con `fontTools.ttLib.TTFont(f).getBestCmap()` (á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü Ü) yo mismo, sin repetir la descarga de la biblia hermana.
- Leída `biblias/31-demon-slayer-kimetsu-no-yaiba/biblia.md` (secciones 6, 7, 13, 18) para no repetir investigación básica de tipografía/mundo, citada donde se reaprovechó un dato.

## Cumplimiento de mis puntos

| Punto | Estado | Por qué |
|---|---|---|
| 5 · Tipografía | ✅ | Base ya comprobada por la biblia hermana + verificación propia con fontTools de 2 fuentes clave; sólo el HUD de *Sweep the Board!* queda ⚠️ por falta de captura de menú. |
| 6 · Cómo hablan en pantalla | ✅ | Confirmado con wikitext propio (Episode 14, el blasón de glicina) + lo ya visto por la biblia hermana; sólo las cajas de diálogo de videojuego quedan ⚠️. |
| 11 · Videojuegos | ✅ | 3 juegos con datos de Steam API verificados hoy, incluido uno nuevo (*Sweep the Board!*) no encontrado antes; TCRF confirmado sin página. |
| 18 · Estilo y cómo replicarlo | ✅ | Dos entrevistas técnicas nuevas con nombres, software (3ds Max + 7 plugins) y cifras concretas (2 km², ×10 renderizado); propuesta completa de Photoshop/Blender. |
| 24 · Obras parecidas | ✅ | AniList con el id correcto (101922) + influencias declaradas por el autor + comparación de catálogo Ufotable (Fate, ⚠️ una fuente) + aviso al redactor de qué conceptos no repetir. |
| 25 · Mundo y símbolos | ✅ | Tabla completa de las 13 respiraciones con kanji/color, tabla de las 9 Marcas de Cazador (el aura hecha piel), símbolos de la glicina, espadas Nichirin, Castillo Infinito y Doce Kizuki — con peso especial en los símbolos de aura, como pide el encargo. |
