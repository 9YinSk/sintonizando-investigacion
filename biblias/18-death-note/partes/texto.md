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

