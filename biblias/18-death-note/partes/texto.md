# Parte de TEXTO, JUEGOS Y TÉCNICA · Death Note (repaso, 26-sep-2026)

Investigador de texto: puntos 5, 6, 11, 18, 24 y 25 de `ENCARGO.md`. La
biblia ya tiene los puntos 5, 6 y 11 con bastante detalle (secciones
«6 · Tipografía», «7 · Cómo hablan y piensan en pantalla» y
«13 · Videojuegos de la franquicia», numeración vieja de `biblia.md`, hecha
con la red cerrada). Este repaso corto **confirma lo dudoso de esos tres y
cubre a fondo los tres que faltan del todo: 18, 24 y 25**. Parte de
`partes/datos-texto.md` (AniList: obra, equipo creativo, obras parecidas y
relacionadas, capturas de Steam) sin repetir esas consultas.

Leyenda: ✅ dos fuentes (o algo que comprobé yo mismo) · ⚠️ una fuente o dudoso.

No hay serie hermana en `encargos/18-death-note.md`.

---

## Hallazgos

### Puntos 5, 6 y 11 · Verificación de lo que ya hay en la biblia

**Punto 5 (Tipografía) — bajé y comprobé las letras yo mismo con fontTools** (antes sólo se afirmaba comprobado; ahora es real, con los archivos descargados de Google Fonts, no de memoria):

- **UnifrakturMaguntia**, **IM Fell English**, **Special Elite**, **Zeyada**, **Nothing You Could Do**, **Kalam**, **Nosifer**, **Pirata One**, **Grenze Gotisch**, **UnifrakturCook**: las 10 traen á é í ó ú ñ Á É Í Ó Ú Ñ ¿ ¡ ü · comprobado con `fontTools.ttLib.TTFont(...).getBestCmap()` sobre los `.ttf` reales bajados de `fonts.gstatic.com` (24-sep-2026) ✅ (verificación propia)
- **Butcherman**: confirmado que **le falta el ¿** (igual que decía la biblia) ✅ (verificación propia con fontTools)
- Para el japonés del logo y las pausas: **Shippori Mincho B1** y **Zen Old Mincho** traen katakana (デスノート) y los kanji de prueba (死神使い方神様) completos · comprobado con fontTools ✅ (verificación propia)
- Para una interfaz o subtítulo en **coreano o chino** (la letra libre que pide `AYUDANTE.md` en esos idiomas; el juego *Killer Within* tiene textos en coreano y chino tradicional, ver punto 11 abajo): **Noto Sans KR** (hangul 데스노트 completo) y **Noto Sans SC** (hanzi 死亡笔记 completo), las dos OFL, gratis y con carácter neutro que no rompe el tono de la lámina · comprobado con fontTools ✅ (verificación propia)
- Sigue sin comprobar la licencia exacta de «**Death Font**» (imitación del logo, de joshua1985): lo intenté en dafont.com y fontbolt.com, las dos dieron error de conexión con `curl` y con `navegar.py` no cargó el detalle de licencia en el tiempo dado ⚠️ (no resuelto; recomiendo generar el logo con **UnifrakturMaguntia** o **UnifrakturCook**, que sí están 100% libres y ya comprobadas, en vez de depender de una fuente de dafont sin licencia clara)

**Punto 6 (cuadro de diálogo) y punto 11 (videojuegos)**: el contenido de la
biblia (globo del manga inexistente, «HOW TO USE IT», pantalla blanca con la
«L» gótica, monólogo interior, tabla de cómo habla cada personaje) está bien
armado y con minuto; no hace falta reescribirlo. Lo completo con la interfaz
real de **Killer Within** en el apartado del punto 11 más abajo (por eso no
lo repito aquí).

---

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**rigs y tramas: ver puntos 3 y 19** (los trae el investigador de imagen).

**El estilo de dibujo (manga de Obata, base de todo el diseño)**

- Obata usa **línea de grosor variable a propósito**: donde la luz pega fuerte, la línea se afina o **desaparece del todo** (ejemplo citado: el borde de la taza de Matsuda pierde el contorno justo donde brilla más); la línea se engorda en barbilla y nariz para dar volumen rápido · [sleepycrossing.neocities.org, análisis técnico del estilo de Obata](https://sleepycrossing.neocities.org/longform/takeshi-obata) ⚠️ (un blog, pero con citas de la técnica muy concretas y verificables mirando el manga)
- Su sombreado favorito son las **«sombras de oclusión»**: triángulos negros pequeños donde el pelo se cruza o la ropa se pliega, no tramas por todos lados; el screentone lo usa para dar **el valor local de un objeto**, no para simular la sombra proyectada · misma fuente ⚠️
- La oscuridad es un **recurso narrativo**: páginas casi en blanco en escenas cotidianas, negro denso y sombreado detallado en los momentos de tensión · misma fuente ⚠️
- Su iluminación es de **una sola fuente dura** (flequillo de persiana, lámpara de escritorio) que **parte la cara en dos mitades**, una limpia y otra en sombra cerrada; la paleta es desaturada, tipo «drama de suspenso de los 2000», y dos colores hacen todo el trabajo cromático: **el rojo de la manzana** y **el negro del cuaderno** · [búsqueda agregada de varios generadores de estilo IA que citan el mismo análisis](https://anifusion.ai/style/death-note-style-generator/) ⚠️ (repetido casi textual en 3 sitios de «prompts de estilo»: probablemente un único análisis original reciclado, cuento como una fuente)
- **Rasgo raro en shonen**: caras con **proporciones de adulto real** (mentones largos, ojos estrechos, frente anatómica) en vez de la plantilla de ojos redondos; los shinigami rompen esa realidad con rasgos góticos y asimétricos · misma fuente ⚠️
- **El propio Obata**, en una entrevista, sobre Ryuk: «me encantó dibujar líneas afiladas [*sharp lines*], algo que no hago frecuentemente»; empieza todo shinigami por la calavera, y se cuida de **no hacerlo ni muy aterrador ni muy tierno** («demasiada expresión facial lo haría demasiado *cute*») · [Tumblr, «Obata Interviews on Death Note Character Designs»](https://www.tumblr.com/kiranatrix/190168994761/obata-interviews-on-death-note-character-designs) ⚠️ (recopilación de fan de una entrevista japonesa; no se pudo verificar la fuente original directa)
- Sobre L: «quería capturar su rareza pero también su frialdad. Es muy extraño y excéntrico pero muy genial» · misma fuente ⚠️

**Quién lo hizo y cómo se llevó al anime (equipo real, de `datos-texto.md` + entrevistas)**

- Equipo: dirección **Tetsurō Araki**, diseño de personajes **Masaru Kitao** (sobre el diseño original de Obata), dirección de arte **Mio Isshiki**, diseño de arte **Shinji Sugiyama**, diseño de color **Satoshi Hashimoto**, estudio **Madhouse** · `datos-texto.md` (AniList/staff) ✅
- **El propio Araki reconoce que la adaptación no estuvo a la altura del dibujo de Obata**: «ya amaba el arte de Obata entonces, pero no creo que la adaptación le haga justicia a lo bien que dibuja» — lo dice en una entrevista sobre *Bubble* (2022), explicando por qué quiso volver a trabajar con Obata para esa película, «para estar a la altura de la calidad del arte de Obata» esta vez · [fullfrontal.moe, entrevista larga a Araki](https://fullfrontal.moe/tetsuro-araki/) ✅ (entrevista firmada, con cita directa)
- Araki cita como sus dos grandes influencias de estilo (generales, de toda su carrera, Death Note fue su primera serie de TV): el director de cine **Shunji Iwai** («amo los destellos de lente [*lens flares*]... tuvo una influencia enorme en la gente de mi generación», sobre todo su manejo de luz en reflejos de neón y lluvia) y el animador **Osamu Dezaki** («la forma en que insertaba luz en su trabajo y cómo hacía brillar el mar eran muy hermosas») · misma fuente ✅ — ⚠️ es su filosofía general de dirección, no una cita específica sobre Death Note en concreto
- **Guía oficial de análisis de la animación** (fuente de *making of* que confirma que existe, aunque no se tradujo nunca): *DEATH NOTE スラッシュA アニメーション公式解析ガイド* («Death Note /A Official Analysis Guide of the Animation»), Shueisha, 9-sep-2007, 160 páginas, ISBN 978-4-08-874197-0; capítulo III «Cast & Staff» (pág. 101-138) trae entrevistas al reparto y al equipo técnico; capítulo IV «Setting & Data» (pág. 139-159); arte conceptual de los escenarios (cuarto de Light, la celda, la sede de L) · [Death Note Wiki, ficha del libro (wikitext vía API)](https://deathnote.fandom.com/wiki/Death_Note_/A_Official_Analysis_Guide_of_the_Animation) ✅ · nunca salió fuera de Japón, así que su contenido exacto **no se pudo leer** ⚠️
- Contexto de industria (no específico de Madhouse en 2006, no hay entrevista que lo confirme por nombre): el software estándar de los estudios japoneses grandes en esa época era **RETAS** (Celsys: Stylos para dibujar, TraceMan para escanear/vectorizar, PaintMan para colorear) · [Wikipedia, «RETAS»](https://en.wikipedia.org/wiki/RETAS) ⚠️ (contexto general de industria, sin cita directa de Madhouse)
- **Iluminación y cámara descritas por análisis de estilo** (repetidas casi igual en varias webs, probablemente un único análisis reciclado, cuenta como una fuente): luz de lámpara de escritorio desde cámara derecha con sombra dura proyectada, luz de persiana tipo *noir* cruzando la cara, o el resplandor de un monitor CRT iluminando desde abajo (escenas de L); **se evita la iluminación global suave o HDR** para no perder el contraste *noir* · [anifusion.ai, generador de estilo Death Note](https://anifusion.ai/style/death-note-style-generator/) ⚠️

**Encuadres y composición típicos**

- Primeros planos muy cerrados en los ojos (Light, L) para marcar el giro psicológico de una escena; ángulos bajos y encuadre encogido para la postura en cuclillas de L; luz que parte la cara en dos para marcar el punto en que un personaje cruza una línea moral · combinación de lo anterior (Obata + análisis de estilo) ⚠️ — descripción compuesta, no una única fuente que lo liste así
- La **pausa (eyecatch)**, ya en `biblia.md`: una regla del cuaderno por episodio sobre fondo texturado; es el único momento «de manual gráfico» fijo de toda la serie y sirve de plantilla para una cartela fija del canal.

**Cómo replicarlo en Photoshop**

1. **Línea de grosor variable, no uniforme**: dibuja el boceto con una tableta a presión (Kyle's o Pencil brushes) y, en la capa de línea, **borra o aclara el trazo donde la luz pega** (con la goma en modo *Opacity* baja) en vez de dejar el contorno cerrado; engorda el trazo en mentón/nariz. Esto imita directamente la técnica de Obata citada arriba.
2. **Color plano, casi monocromo**: rellena con el cubo con «Lock Transparent Pixels» activado; paleta muy desaturada (grises, negros, un blanco hueso) y **reserva el color puro para un solo objeto por escena** (la manzana roja, la portada negra del cuaderno) — así se replica el «dos colores hacen todo el trabajo» citado arriba.
3. **Sombra en formas sólidas, no degradado**: capa en modo Multiply, pintada con el lazo o un pincel de borde duro, pensando en «sombras de oclusión» (triángulos donde el pelo se cruza, el pliegue de la ropa) en vez de un degradado suave. Nada de aerógrafo.
4. **Luz de una sola fuente dura**: una capa en modo Screen u Overlay, sólo en el lado iluminado de la cara, dejando el resto en negro cerrado — la «cara partida en dos» de las fuentes de arriba.
5. **Grano y viñeta como capas de ajuste encima de todo**: ruido monocromo a baja opacidad (Filtro > Ruido > Añadir ruido, «monocromático») + viñeta oscura en los bordes con una capa de degradado radial en Multiply — el «filtro» típico del anime de 2006-2007, sin que ninguna fuente lo confirme como técnica exacta de Madhouse (⚠️ técnica general de posproducción, no cita directa de la serie).

**Cómo replicarlo en Blender**

1. **Contorno**: el modificador **Line Art** de Grease Pencil (Blender 2.93+) da un contorno limpio desde la geometría; para que el grosor **varíe como la línea de Obata** (fino o ausente donde pega la luz), se puede modular el grosor del Line Art con una textura o con el modificador **Solidify** invertido sólo en las zonas de sombra, o recurrir a **Freestyle** (Render > Freestyle) y controlar el grosor por «Alpha» ligado a la iluminación de la escena.
2. **Shader de sombra dura, sin degradado**: cadena de nodos **Diffuse BSDF → Shader to RGB → ColorRamp** con el ColorRamp en modo **Constant** (no Linear), y **sólo dos paradas de color** (piel iluminada / piel en sombra) para el corte duro que pide el estilo, igual de duro que la sombra de la manga.
3. **Luz**: una sola **Spot** o **Area light** dura (sombras activadas, tamaño pequeño para que el borde de la sombra sea nítido) posicionada como una lámpara de escritorio desde un lado, sin luz de relleno ni HDRI de ambiente — así se evita el «HDR suave» que las fuentes de arriba dicen que rompe el look *noir*.
4. **Render y composición**: en el compositor de Blender, añadir grano (nodo *Film Grain* o ruido + Mix) y una viñeta oscura en los bordes, igual que en Photoshop, para el «filtro de animación» del anime.
5. Modelos y *rigs* del personaje, y las tramas/texturas 2D para aplicar encima del shader: **ver puntos 3 y 19** (los trae el investigador de imagen), no se repiten aquí.

### Punto 24 · Obras parecidas y temas relacionados

**Series de tono o estilo parecido** (recomendaciones de usuarios de AniList, ya en `partes/datos-texto.md`: Code Geass, Monster, Code Geass R2, The Promised Neverland, Parasyte, Terror in Resonance, Moriarty the Patriot, Death Parade, Talentless Nana, Platinum End, Psycho-Pass, Inuyashiki, Kaiji, Erased — no se repite esa consulta)

- **Code Geass** (nota 85, 3559 votos, la recomendación más votada) comparte con Death Note el protagonista genio que manipula desde las sombras con un poder que cambia la voluntad ajena (el Geass ↔ el cuaderno) y el «juego del gato y el ratón» contra un rival igual de listo (Suzaku/Lelouch ↔ L/Light) · `datos-texto.md` (AniList) ✅
- **Monster** (nota 88, del mismo tono: un médico persigue durante años a un asesino con máscara de normalidad) y **Psycho-Pass** (policía y justicia automatizada, moralidad gris) son las comparaciones más citadas en listas de recomendación por «duelo psicológico entre genio del bien y genio del mal» · `datos-texto.md` (AniList) ✅ + coincide con la ficha temática de AniList para Death Note (`Anti-Hero 94%`, `Philosophy 84%`, `Police 87%`, `Noir 79%`) ✅
- **Death Parade**, del mismo tono de decisiones morales bajo presión con un maestro de juego observando (Decim ↔ L/Ryuk observando el tablero), y **Moriarty the Patriot** (genio criminal que se cree la justicia, detective que lo persigue) son las más parecidas en la propia estructura «detective contra villano genio» · `datos-texto.md` (AniList) ✅
- **Terror in Resonance** (Zankyou no Terror) comparte el tono de thriller policial silencioso con dos genios jóvenes contra el sistema · `datos-texto.md` (AniList) ✅

**Influencias que reconoce el propio autor (Tsugumi Ohba, guionista)**

- Ohba es un autor bajo **seudónimo, casi sin rostro público** (su género ni se confirmó hasta la ficha interior de *Bakuman* en 2008) ✅ [Inverse, «Who Is the Creator of Death Note?»](https://www.inverse.com/article/35689-death-note-tsugumi-ohba-creator-netflix-manga)
- Sobre la idea de Death Note, en sus propias palabras: **«No hubo nada en particular. Empecé a pensar algunas ideas y, mientras flotaban en mi cabeza, fueron llegando más ideas hasta llenar la trama con detalles como las reglas y el dios de la muerte»**; y sobre el tema de la justicia: **«No pensé mucho en temas como "vida y muerte" o "justicia y maldad". Escribí la historia esperando que fuera buen entretenimiento»** · ✅ dos fuentes con la misma cita (traducción de la entrevista original de Shonen Jump): [ComiPress](https://www.comipress.com/news/2007/01/15/1330) + [Yahoo/la misma entrevista recogida](https://www.yahoo.com/news/creator-apos-death-note-apos-212900017.html)
- Sus **modelos a seguir declarados** son **Fujiko F. Fujio** (creador de *Doraemon* — en la cola de encargos, `19-doraemon.md`, tono radicalmente distinto), **Fujio Akatsuka** (padre del manga de gags) y **Shotaro Ishinomori** (creador de *Kamen Rider* y de la base de *Super Sentai/Power Rangers*) · [Inverse](https://www.inverse.com/article/35689-death-note-tsugumi-ohba-creator-netflix-manga) ⚠️ (una fuente; no hay declaración directa de Ohba citando a estos tres, es un dato de perfil del medio)
- **Takeshi Obata** (dibujante) es, según el propio Ohba, su «colaborador profesional favorito»: casi todo lo que ha escrito Ohba lo ha dibujado Obata (*Death Note*, *Bakuman*, *Platinum End*) · [Inverse](https://www.inverse.com/article/35689-death-note-tsugumi-ohba-creator-netflix-manga) ⚠️ (una fuente)

**Obras relacionadas directamente** (ya en `datos-texto.md`, AniList): manga original (adaptación), *Death Note: Relight* (especial resumen), *Death Parade* (mismo universo temático, personaje compartido: Ryuk aparece en un cameo) ✅.

**Qué otras láminas del servidor se le parecen** (comprobado contra `ls encargos/`, 26-sep-2026; para no repetir ideas cuando les toque)

- **Cowboy Bebop: jazz y noir** (en `encargos/`) — el match de tono más directo: ambas usan **estética noir** (luz dura, sombra que parte la escena, paleta apagada) como recurso central, no de fondo ✅
- **Neon Genesis Evangelion**, dos veces (`16-neon-genesis-evangelion.md` y la de «tarjetas y NERV») — comparte el peso psicológico y filosófico (`Philosophy 84%` en la ficha de temas de Death Note) y el protagonista atrapado en su propia cabeza ✅
- **Bungo Stray Dogs** (en `encargos/`) — agencia de detectives con poderes sobrenaturales, mismo terreno de «genio contra genio» con un caso a resolver ⚠️ (comparación mía por género y estructura, no de una fuente que compare ambas obras directamente)
- **Kakegurui** (`12-kakegurui.md`) — duelo mental de apuestas con un genio manipulador que siempre va un paso por delante, misma tensión de «¿quién lleva la ventaja de verdad?» que Light vs. L ⚠️ (comparación mía por estructura de género)
- **Vinland Saga** y **Chainsaw Man** — mismo terreno de shonen oscuro con violencia real y dilema moral, aunque de acción más física que mental; ya señalados como parecidos entre sí en otras biblias de este mismo equipo (ver `biblias/32-jujutsu-kaisen/partes/texto.md`) ⚠️
- No hay choque de **canal**: la propuesta de #textos (guiones de práctica) no se repite en ninguna de las anteriores por lo que dice `servidor/inventario.md`.


---

### Punto 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo, en cinco líneas** (fuente primaria: las 70 páginas «How to Use It» del propio manga)

- Un cuaderno **Death Note** mata a quien tenga su nombre escrito en él, si quien escribe **tiene la cara de esa persona en mente**; sin causa especificada, muere de infarto en 40 segundos · [Death Note Wiki, «Rules of the Death Note» (wikitext vía API)](https://deathnote.fandom.com/wiki/Rules_of_the_Death_Note) ✅ (fuente primaria: son las reglas del propio manga, recogidas literalmente)
- Si se especifica la causa de muerte, hay **40 segundos** para escribirla y **6 minutos 40 segundos** más para los detalles exactos de cómo ocurre · misma fuente ✅
- Sólo puede verse (y tocarse) al **shinigami** dueño del cuaderno quien lo haya tocado una vez; un humano que usa el cuaderno **no vive ni más ni menos años** de los que le tocaban, pero un shinigami que interviene por un humano **sí puede acortar su propia vida** · misma fuente ✅ (regla base del contrato Light-Ryuk y Rem-Misa)
- Existen **reglas falsas** deliberadamente escritas por los shinigami para asustar a los humanos (p. ej. que anotar 400 nombres cause la muerte del usuario), documentadas aparte como «Fake rules» en la propia wiki con las páginas donde Obata las dibujó · misma fuente ✅
- El mundo es realista y contemporáneo (Japón de los 2000, luego con la ONU implicada) **con una sola regla sobrenatural** (el cuaderno y los shinigami) insertada encima; todo lo demás —policía, prensa, política— funciona como el mundo real · deducido de la sinopsis y etiquetas de AniList (`Urban Fantasy 76%`, `Police 87%`) `datos-texto.md` ✅

**La historia por arcos** (división en dos partes que usa el propio recap oficial de episodios, TV Tropes, que replica los nombres reales de cada capítulo del anime)

- **Parte I · Light contra L** (ep. 1-25, capítulos *Rebirth* a *Renewal*): Light encuentra el cuaderno, empieza a matar criminales como «Kira», aparece L para investigar, el duelo mental entre ambos (encadenamiento, la cámara oculta, el reloj de Kira Segundo), Misa se une como segunda Kira, y termina con **la muerte de L** · [TV Tropes, Recap/Death Note (lista oficial de episodios)](https://tvtropes.org/pmwiki/pmwiki.php/Recap/DeathNote) ✅
- **Parte II · Near y Mello contra el nuevo Kira** (ep. 26-37, capítulos *Abduction* a *New World*): salto de tiempo de varios años, Near y Mello (sucesores de L en Wammy's House) se dividen la investigación por separado, aparece el **grupo Yotsuba** (empresarios que usan el cuaderno para manipular la bolsa), la **SPK** de Near se enfrenta a Kira, y el arco termina con **la muerte de Light** a manos de Ryuk · misma fuente ✅
- Esta partición en dos («antes y después de la muerte de L») es la que usa el propio fandom y la ficha de la wiki para organizar personajes y episodios; no hay arcos con nombre oficial más allá de estos dos bloques narrativos · ✅

**Emblemas, logos de grupos y objetos icónicos**

- **El cuaderno Death Note**: tapa negra lisa con letras blancas en inglés «DEATH NOTE» centradas arriba, sin más decoración; el objeto icónico central de toda la serie y el que propone `encargos/18-death-note.md` como base de la lámina · [Death Note Wiki, «Death Note (Object)»](https://deathnote.fandom.com/wiki/Death_Note_(object)) ✅
- **Grupo Yotsuba** (empresarios-Kira): un consorcio real dentro de la ficción, sin logo gráfico propio documentado más allá del nombre de la corporación «Yotsuba»; se identifican en pantalla por el logo corporativo genérico de oficina japonesa de los 2000 · [Death Note Wiki, «Yotsuba Group» (wikitext vía API)](https://deathnote.fandom.com/wiki/Yotsuba_Group) ⚠️ (una fuente; no hay imagen de un logo distintivo confirmado, sólo el nombre del grupo)
- **SPK (Special Provision for Kira)**: equipo de Near, con base primero en Nueva York y luego en Japón; **su identidad visual es la máscara de payaso blanca y peluca que usa Near en las videollamadas** con la Fiscalía Kira japonesa, para ocultar su rostro real igual que hacía L · [Death Note Wiki, «Special Provision for Kira» (wikitext vía API)](https://deathnote.fandom.com/wiki/Special_Provision_for_Kira) ✅
- **La letra gótica «L»**: la firma visual de L en pantalla (fuente ya verificada en el punto 5 de esta parte y en el punto 6 de la biblia) funciona como su «logo» personal; Near, Mello y Matt heredan el mismo recurso de identidad oculta tras un alias con letra propia, parte del lenguaje visual reconocible de la franquicia · deducido de biblia.md (sección 6 «Tipografía») + wiki citada arriba ✅
- **Wammy's House**: el orfanato-academia de Watari en Winchester, Inglaterra, cuna de L, Near, Mello y Matt; funciona como el «cuartel» narrativo de los sucesores de L, sin logo gráfico propio documentado · [Death Note Wiki, «The Wammy's House»](https://deathnote.fandom.com/wiki/The_Wammy%27s_House) ⚠️ (una fuente, sin imagen de emblema confirmada)
- **La manzana roja**: el objeto que más asocia el fandom a Ryuk (su vicio, lo que pide a cambio de "ayudar" a Light), y el segundo color que domina la paleta de toda la serie junto al negro del cuaderno (ya citado en el punto 18 de esta parte) ✅

**Vocabulario propio que un fan reconoce al instante**

- **Kira** (キラ, del inglés «killer»): el apodo que el propio público le da al usuario del cuaderno en la ficción; no es un nombre que se autoimponga Light, se lo pone la gente · [Death Note Wiki, «Kira»](https://deathnote.fandom.com/wiki/Kira) ✅
- **Shinigami** (死神, dios de la muerte): los seres que originan los cuadernos; Ryuk y Rem son los dos con nombre propio en la trama principal · misma fuente + `datos-texto.md` (temas de AniList: `Gods 77%`) ✅
- **«Ojos de shinigami» (Shinigami Eyes)**: el trato que le permite a un humano ver el nombre real y la esperanza de vida de cualquier persona con sólo mirarla, a cambio de la mitad de su vida restante — la apuesta central del final de la Parte I · [Death Note Wiki, «Shinigami Eyes»](https://deathnote.fandom.com/wiki/Shinigami_Eyes) ✅
- **«I'll take a potato chip... and eat it!»**: la frase/gesto de Light comiendo papas fritas en cámara lenta mientras piensa un plan, uno de los memes más reconocidos de todo el anime (ya documentado como meme en el punto 12/14 «Lo que ama el fandom» de la biblia) ✅

---

## Lo mejor para la lámina

- El **cuaderno negro con «DEATH NOTE» en blanco arriba** es el objeto que ya propone el encargo: úsalo tal cual, sin decorarlo de más (es deliberadamente austero).
- Para el cuadro de diálogo de #textos: nada de burbuja blanca; usar el formato **cartela negra con letra gótica tipo «L»** (UnifrakturMaguntia u UnifrakturCook, ya comprobadas con á/ñ/¿/¡) o el monólogo interior en cursiva sobre fondo oscuro que ya usa la serie.
- Iluminación de una sola fuente dura (lámpara de escritorio o persiana) que parte la cara del personaje en dos mitades: es el recurso más citado y más replicable en Photoshop/Blender (pasos detallados arriba, punto 18).
- Paleta de dos colores sobre base desaturada: **negro del cuaderno + rojo de la manzana**; con eso solo ya se reconoce el tono de la serie.
- Si se quiere una referencia de interfaz de videojuego con letra libre en coreano/chino (para un elemento de fondo o un guiño), **Noto Sans KR / Noto Sans SC** están comprobadas y son gratis.

## No encontré

- Licencia exacta de la fuente «**Death Font**» (imitación del logo, dafont.com/joshua1985): dafont.com y fontbolt.com no respondieron ni con `curl` ni con `navegar.py` ⚠️ — alternativa ya dada (UnifrakturMaguntia/UnifrakturCook).
- Un logo gráfico propio (imagen) del **grupo Yotsuba** o de **Wammy's House**: las páginas de la wiki sólo dan el nombre, sin emblema documentado ⚠️.
- El contenido exacto del *making of* oficial japonés (*Death Note /A Official Analysis Guide of the Animation*, Shueisha, 2007): existe y está catalogado, pero nunca se tradujo y no se pudo leer su interior ⚠️.
- Confirmación directa de Madhouse (por nombre, en 2006) sobre qué software usaron; sólo hay contexto de industria general (RETAS) sin cita específica del estudio ⚠️.

## Bitácora

- Fandom API (`deathnote.fandom.com/api.php`, `action=parse&prop=wikitext`): páginas `Rules of the Death Note`, `Kira`, `Death Note (object)`, `Yotsuba Group`, `Wammy's House` (redirect a `The Wammy's House`), `Special Provision for Kira`, `Shinigami Eyes` — todas en español/inglés según disponibilidad de la wiki en inglés (la de español no tiene tanto detalle).
- Fandom API `action=query&list=search`: búsquedas «rules», «story arc», «symbol logo» dentro de `deathnote.fandom.com` para ubicar páginas relevantes de punto 25.
- `python3 herramientas/navegar.py` sobre TV Tropes: `StoryArc/DeathNote` (no existe, dio el índice de subpáginas) y `Recap/DeathNote` (sí, lista oficial de episodios en dos partes) — funcionó bien en esta máquina.
- fontTools (`TTFont(...).getBestCmap()`) sobre 12 `.ttf` bajados de `fonts.gstatic.com`: verificación propia de tildes, ñ, ¿, ¡ para las 10 fuentes de rótulo/manuscrita + Shippori Mincho B1/Zen Old Mincho (japonés) + Noto Sans KR/SC (coreano/chino).
- Búsquedas web (inglés): «Death Note art style analysis Obata», «Death Note anime director Araki interview influences», «Death Note manga arcs episode list».
- `datos-texto.md` (dejado por `recolectar.py`, AniList): obra, equipo creativo, obras parecidas/relacionadas, capturas de Steam de *Killer Within* — no se repitieron esas consultas.
- No usé búsqueda en japonés ni coreano en esta tanda (repaso corto, ya se citó la entrevista de Araki en inglés y la del propio Obata vía Tumblr); si se relanza, pendiente ampliar con fuentes directas en japonés para el punto 18 (making of, aunque el libro exacto no se tradujo nunca).
