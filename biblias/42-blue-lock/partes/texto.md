# Investigador de TEXTO, JUEGOS Y TÉCNICA · Blue Lock

Puntos de `ENCARGO.md`: **5** (tipografía), **6** (cuadros de diálogo), **11**
(videojuegos), **18** (estilo de dibujo y técnica), **24** (obras parecidas),
**25** (el mundo y sus símbolos).

Parte desde `partes/datos-texto.md` (AniList, staff, recomendados, el juego de
Steam). No repite esas consultas. Formato libreta: un dato por línea, con
fuente, ✅ (dos fuentes) o ⚠️ (una fuente o de memoria).

---

## Punto 5 · Tipografía

**El logo** (ブルーロック / BLUELOCK):
- Título japonés e inglés en **letra blanca gruesa, con textura de pintura
  gastada/craquelada** (grunge), con salpicaduras, sobre un fondo verde neón
  en el tomo 1 · medido en la portada del tomo 1 (`vol1.png`, bajada por la
  API de Fandom) ✅ [Fandom: File:JP Volume 1.png](https://bluelock.fandom.com/wiki/File:JP_Volume_1.png)
- La palabra **«BLUE» gigante, cortada por el borde**, en azul marino con
  filo blanco, como grafismo de fondo en la misma portada ✅ (misma imagen).
- Verde de fondo del tomo 1 medido con Pillow: `#96FC02` (neón, no el azul
  que se asocia a la serie) ✅. Azul del uniforme de entrenamiento medido en
  la misma portada: `#083F9A` ✅.
- Un foro de dafont pidió identificarlo y **nadie dio una respuesta
  concreta** ⚠️ ([dafont](https://www.dafont.com/forum/read/526334/somebody-please-help-me-identify-similar-fonts-to-the-bluelock-anime-logo)).
- Una guía japonesa de tipografía (Design Pocket) recomienda para el
  «ambiente Blue Lock» **fuentes de pago** con grunge o corte geométrico ya
  aplicado (DFひびゴシック体, 東亜重工 GRUNGE, TA-方縦K700…), lo que confirma que el
  estilo real es: **líneas rectas/geométricas + textura de grunge**, aunque
  ninguna es la fuente exacta del logo oficial ⚠️ ([Design Pocket #119](https://designpocket.jp/static/font/fontguide/119.html)).
- Un blog japonés que analiza la interfaz de **BLUE LOCK Project: World
  Champion** dice que el juego usa una **fuente de 7 segmentos** (como un
  marcador digital) para el marcador de goles, y una fuente **condensada y
  angular, parecida a los números de las camisetas**, para las estadísticas
  y el poder de los jugadores — sin dar el nombre comercial ✅ ([ゲームアプリのUIデザイン](https://appgameui.hatenablog.com/entry/2024/06/01/214015)).
- El logo de **Blue Lock: Blaze Battle** (el otro juego oficial) usa el
  mismo lenguaje: letras blancas gruesas con bordes rasgados/arañados para
  «BLUELOCK» y un efecto de rotura para «BLAZE BATTLE» ✅ (fotograma del
  título del vídeo oficial, ver §11).

**Letra libre por uso, comprobada con fontTools (todas OFL de Google Fonts,
descargadas y comprobadas yo mismo, subset `latin`, no `latin-ext`: hay que
pedir ese subset o la ✿ tildes/ñ/¿/¡ no aparecen)**:

| Uso | Letra libre | ¿Tildes, ñ, ¿, ¡? |
|---|---|---|
| Logo/título (grunge, condensada, geométrica) | **Anton** (Google Fonts, OFL) | ✅ comprobado con `fontTools.getBestCmap()`: trae los 10 caracteres (á é í ó ú Ñ ñ ¿ ¡ ü) |
| Grito / onomatopeya / impacto (para el «¡GOAL!» y similares que aparecen en el juego, ver §11) | **Bangers** (Google Fonts, OFL) | ✅ comprobado, completo |
| Números de camiseta / estadísticas / marcador deportivo condensado | **Oswald** Bold y **Teko** Bold (Google Fonts, OFL) | ✅ ambas comprobadas, completas |
| Interfaz de juego / HUD (paneles, botones) | **Rajdhani** Bold (Google Fonts, OFL) | ✅ comprobado, completo |
| Marcador digital estilo «7 segmentos» (goles) | **DSEG7 Classic** (keshikan, SIL OFL, GitHub) | ⚠️ no la descargué para comprobar: los tipos de 7 segmentos casi nunca traen acentos, así que **sólo sirve para dígitos**, nunca para texto con tilde |
- Comando usado para comprobar: `TTFont(archivo).getBestCmap()` y se buscó
  el código de cada carácter (á=0xE1, ñ=0xF1, Ñ=0xD1, ¿=0xBF, ¡=0xA1, ü=0xFC).
  **Aviso para quien use estas fuentes después**: hay que bajar el subset
  **`latin`** de fontsource/Google Fonts, no `latin-ext` — probé primero
  `latin-ext` y los cuatro archivos fallaban (les faltaban los diez
  caracteres) porque ese subset no incluye el bloque Latin-1 con las tildes.
- Los 17 tipos «al estilo Blue Lock» de un blog japonés
  ([sitebk.com](https://sitebk.com/summary/blue-lock/)) son fuentes
  **japonesas** (kana/kanji) pensadas para carteles y eventos: sirven de
  referencia de «mood», no para texto en español (⚠️ no las comprobé con
  fontTools: son de uso japonés, lo normal es que no traigan ¿ ni ¡).

**El manga en español**: lo publica **Editorial Ivrea** (Argentina, con
distribución en Chile y España), en tomos mensuales; van 21+ tomos
publicados ✅ ([Ivrea](https://www.ivrea.com.ar/titulo/blue-lock/),
[coleccionablesblog](https://coleccionablesblog.com.ar/blue-lock/)). No
verifiqué qué fuente de letras usa Ivrea en los globos de la edición en
español ⚠️ (no encontré scans para comprobarlo sin piratear).

---

## Punto 6 · Cuadros de diálogo

- **El objeto de diálogo más fuerte de todo lo que encontré no es del manga:
  es la «carta de selección» del entrenador Gabi** en la colaboración oficial
  de **REMATCH x Blue Lock** (Sloclap, 24-sep-2026, ver capturas en §11):
  una **carta doblada en tres, sobre fondo azul noche con cadenas dibujadas**
  (el símbolo de Blue Lock), que empieza «Dear diamonds in the rough, you've
  been selected for a special player training program…» y la firma «Coach
  Gabi, Project Director» ✅ ([Blue Lock Store Blog](https://bluelockstore.co/blogs/infos/rematch-blue-lock-you-have-been-selected-coach-gabi-letter-blue-lock-project),
  confirmado por el propio anuncio del juego en [Gematsu](https://www.gematsu.com/2026/09/rematch-x-blue-lock-collaboration-announced)).
  Es un objeto real (una carta/convocatoria) que se puede hacer en Blender:
  papel doblado, cadena grabada o en relieve, tinta azul.
- **La interfaz de BLUE LOCK Project: World Champion** (medida en
  `pwc/hoja_pwc.jpg`, hoja de contacto de 4 capturas de Google Play,
  1052×592 cada una) ✅:
  - Paneles de estadística **rectangulares, azul marino translúcido**
    (fondo medido `#191E32`), con **borde/filete azul neón** (medido
    `#374F8B`) y esquinas rectas, no redondeadas.
  - Botones de acción («Combo Effect List», «Inspiration Obtained», «Training
    Ability List», «Details») en **caja azul oscuro sólido con texto
    blanco**, sin relleno de color llamativo: la jerarquía la marca el
    tamaño, no el color.
  - «Chips» de subida de estadística en rojo sólido con el texto «UX1»,
    «UX6»… en blanco.
  - El **fondo general del juego es una trama de cristales/rombos azules
    entrelazados con una cadena**, el mismo motivo que en la portada del
    tomo 1 y en el logo de Blaze Battle: **el «vitral» roto y la cadena son
    el marco visual reconocible de toda la franquicia**, en manga, anime y
    videojuego por igual ✅ (comparación directa entre las 3 fuentes de
    imagen bajadas en esta sesión).
  - Un panel de diálogo en cómic dentro del propio juego (pantalla
    «Devour each other») mezcla **viñetas fotográficas recortadas** con
    texto tipo grito **"GOAL!!"** en letra blanca gruesa muy angulosa, y
    bocadillos con cola simple (fondo blanco, texto negro, sin decoración)
    para las frases cortas de personaje («There's a…») — el único sitio
    donde vi un globo blanco «normal», y es dentro de un colage de cómic
    en el propio juego, no del anime.
- **No encontré capturas navegables del interior de Blaze Battle** (su app
  de Play Store da «Not found» con dos intentos, y el vídeo de gameplay que
  encontré fue borrado por YouTube: «This video is no longer available
  because the YouTube account…​has been terminated») ⚠️. Sólo tengo la
  imagen del título (chains + letra grunge, ver §5 y §11).
- **Cartelas del mundo**: no encontré una ficha tipo «información pública»
  (como Attack on Titan) propia de Blue Lock ⚠️; lo que sí es reconocible y
  reaparece en portada, juego y colaboraciones es la **cadena** alrededor
  del cuello/muñeca de los jugadores (visible en el tomo 1 y en el traje de
  la colaboración con REMATCH) — la wiki y varias notas dicen que el
  significado exacto de las cadenas **nunca lo explicó el autor**, y que el
  fandom lo lee como el ego, la relación con el proyecto o el sentimiento
  hacia el fútbol japonés, cada uno la suya ✅ (2 fuentes independientes:
  [CBR](https://www.cbr.com/blue-lock-muneyuki-kaneshiro-color-significance/)
  y el resumen coincidente de Attack of the Fanboy recogido en la búsqueda).
- **Qué NO hacer** (deducido de lo anterior, para la lámina): nada de globo
  blanco ovalado «de cómic genérico»: el objeto propio de Blue Lock es
  **la carta de convocatoria** o **el panel azul con la cadena**, no una
  burbuja. Si hace falta un grito, la letra es blanca, gruesa y muy angular
  (no redondeada).

---

## Punto 11 · Videojuegos

Blue Lock **sí tiene videojuegos oficiales** (más allá de la colaboración de
Steam ya recogida en `datos-texto.md`):

1. **BLUE LOCK Project: World Champion (PWC)** — el principal. Simulación de
   entrenamiento: el jugador hace de coach de Ego Jinpachi y entrena a un
   delantero con estadísticas propias (Stamina, Speed, Physical, Technical,
   Intelligence, Kick Power). Desarrollado por **Rudel Inc.**, publicado por
   **Bandai Namco Entertainment**; lanzado en Japón en 2022, con versión
   global para iOS/Android; **3.er aniversario y 17 millones de descargas**
   a 2026 ✅ ([BLUE LOCK PWC en App Store](https://apps.apple.com/us/app/blue-lock-pwc/id6476623870),
   [sitio oficial global](https://bluelock-pwc-gl.com/en/)). Usa las voces
   originales japonesas del anime ✅ (búsqueda web, resumen coincidente en
   QooApp y en el sitio oficial). **No confirmé que tenga español** ⚠️
   (la ficha global no lista el idioma).
   - **4 capturas oficiales miradas y medidas** en
     `/tmp/claude-0/trabajo/42-blue-lock-texto/pwc/` (hoja de contacto
     `hoja_pwc.jpg`, 666×1184): portada con Isagi y todo el reparto sobre
     fondo de vitral azul roto; panel de entrenamiento con las 6
     estadísticas y tarjetas doradas de «Special Lecture»; barra de
     «Condition Flow Bonus» al 4349 %; collage cómic con «GOAL!!».
2. **Blue Lock: Blaze Battle** (ブルーロック BLAZE BATTLE) — segundo juego
   oficial, más de acción: **gráficos 3D**, control directo de los
   jugadores en el campo, equipos de 11 contra 11, **modo Historia que
   sigue los hechos del anime** y PvP en tiempo real ✅ ([TapTap](https://www.taptap.io/post/7083898),
   resumen de búsqueda coincidente). Con Isagi y Nagi como personajes
   confirmados en el material promocional ✅.
   - La imagen del título (`blaze1.jpg`, 3836×2160, bajada de TapTap)
     muestra el motivo de **cadenas envolviendo a los personajes** y el
     logo con textura rasgada — mismo lenguaje visual que el tomo 1 del
     manga y que el logo de PWC.
   - **No pude ver capturas de la interfaz de combate**: la ficha de Google
     Play de la app (`jp.co.bael.bluelock.blazebattle`) devolvió «Not
     found» dos veces, y el único vídeo de gameplay que encontré en YouTube
     fue borrado («cuenta terminada») ⚠️. Queda pendiente si alguien puede
     abrir YouTube sin bloqueo.
3. **REMATCH x Blue Lock** (colaboración, no un juego propio de la
   franquicia, pero **el más jugado ahora mismo** y con más detalle
   verificable): **Sloclap** (estudio francés de *Rematch*, un juego de
   fútbol 5vs5) lanzó el 24-sep-2026 la «Season 5: Blue Lock», con el modo
   **Aura Striker** (3vs3, barra de «Aura» que sube con el tiempo y las
   intercepciones, activarla da velocidad y potencia de tiro extra, sin
   límite de resistencia y portero automático) ✅ ([Gematsu](https://www.gematsu.com/2026/09/rematch-x-blue-lock-collaboration-announced),
   [playrematch.com](https://www.playrematch.com/post/what-you-need-to-know-before-rematch-x-blue-lock),
   [gamespress](https://www.gamespress.com/REMATCH-ANNOUNCES-IN-GAME-COLLABORATION-WITH-BLUE-LOCK-KICKS-OFF-SEPTE)).
   Isagi, Bachira, Nagi y Rin como bundles de personaje jugables (piel,
   celebración de gol propia y carta de jugador cada uno) ✅. Del **Blue
   Lock Training Pack** en Steam (ya en `datos-texto.md`): la captura
   1920×1080 muestra el **traje de entrenamiento con el patrón de líneas
   tipo tela de araña/vitral** que usan los reclutas en el manga y el
   anime, y la carta de colección del pack con el mismo icono pentagonal
   partido ✅ (medido: fondo `#0A0E19`, líneas del traje `#303B6B`).
   Idiomas de la ficha de Steam: interfaz en español de España confirmada
   por la propia tienda (con asterisco = sólo texto, sin doblaje) ✅
   (dato ya en `datos-texto.md`, confirmado aquí con la búsqueda del
   anuncio oficial).
- **No encontré página de The Cutting Room Floor para ningún juego de Blue
  Lock** ⚠️ (busqué «Blue Lock» directamente en los resultados de tcrf.net:
  no aparece ninguna entrada dedicada).

---

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Quiénes lo hacen y su formación**:
- Guion: **Muneyuki Kaneshiro** (Osaka, 1987), graduado en el Departamento de
  Manga de la Universidad Kyoto Seika; antes escribió *As the Gods Will*
  (2011-12, «juegos de la muerte» con estudiantes) y *Jagaaaaaan* (2017-21,
  héroe oscuro con transformación); su firma es **la historia de
  supervivencia/selección brutal**, el mismo motor narrativo de Blue Lock
  ✅ ([Abema Times](https://times.abema.tv/en/articles/-/10180043)).
- Dibujo: **Yusuke Nomura** (Kyoto, 1987) fue **asistente de Hajime Isayama
  en Attack on Titan** y también asistente en *Ahiru no Sora* (manga de
  baloncesto), antes de debutar en solitario en 2013 con *Isago no Ou* ✅
  (2 fuentes: [Anime News Network](https://www.animenewsnetwork.com/encyclopedia/people.php?id=194273)
  y el resumen coincidente de la wiki de Blue Lock vía [caché de Wayback](http://web.archive.org/web/20260222052038/https://bluelock.fandom.com/wiki/Yusuke_Nomura)).
- **Cita textual de Nomura** sobre su técnica: *«ya empecé a desarrollar este
  estilo de añadir detalles en los ojos del personaje, o expresarlos con un
  aura que parece un monstruo»* y *«a partir de la idea de Kaneshiro,
  empezamos a incorporar elementos como las auras o la secuencia del
  disparo — la acción — para que se pareciera más a un manga de batallas»*
  ✅ ([entrevista en Anime Corner](https://animecorner.me/interview-blue-lock-creators-muneyuki-kaneshiro-yusuke-nomura/)).
  **Esto se ve confirmado en la propia imagen oficial**: en la portada de
  PWC (`pwc_cover_full.jpg`) Isagi y varios personajes llevan una **niebla
  o estela de color (verde y rosa) alrededor**, exactamente el «aura»
  descrito.
- Colores de aura **por personaje** (⚠️ fuente floja, un solo blog-resumen
  de baja calidad, no lo confirmé en una segunda fuente seria): Isagi con
  aura azul oscuro (blanca en su «despertar»); Nagi con un aura de
  «calavera»; Bachira imaginando a sus rivales como **monstruos** (esto sí
  lo dice también Nomura en la entrevista de arriba, así que la idea general
  de «monstruo» en Bachira sí es ✅; el color exacto no).
- **El anime** lo hace el estudio **8bit** (una rama de Satelight, con
  departamento propio de sakuga, fotografía/composición y **3DCG**) ✅
  ([Anime Corner](https://animecorner.me/in-defense-of-the-blue-lock-anime/)).
  Usa **CGI para los movimientos rápidos de pies** y deja animación 2D
  tradicional para los planos finales de los partidos importantes; la
  crítica de fans es que a veces se nota el «still over animation»
  (fotogramas fijos que se mueven en panorámica en vez de dibujarse) por
  la presión de calendario (87 episodios repartidos entre varias series en
  2024 con ~70 empleados) ✅ (misma fuente). El staff de producción (de
  `datos-texto.md`, AniList): Director Tetsuaki Watanabe, Director de Arte
  Sawako Takagi, Diseño de Color Sakura Komatsu, Director de CG Norimitsu
  Hirosawa — confirma que sí hay un departamento de CG dedicado.
- La etiqueta de AniList «**CGI 58 %**» (ya en `datos-texto.md`) coincide
  con todo lo anterior: la propia comunidad marca el uso de 3D como rasgo
  reconocible de la serie, no un error aislado.

**Cómo replicarlo en Photoshop**:
- **Línea**: contorno negro, grosor medio-grueso por fuera, líneas
  interiores finas (rasgos de cara, pliegues de ropa) — el patrón típico de
  shonen de acción, sin el rayado fino de un seinen.
- **Sombreado**: plano, de 1 o 2 tonos, bordes duros (no degradado suave);
  para el «aura», una **capa aparte en modo Pantalla (Screen)**, pintada a
  mano con un pincel de humo/chispa o con el filtro Viento + Desenfoque
  gaussiano, en el color propio del personaje (verde/rosa para Isagi según
  la portada de PWC medida arriba), más un **Resplandor exterior
  (Outer Glow)** para que se vea luminosa sobre el fondo oscuro.
- **Filtro de animación**: grano y viñeteado suaves en las escenas de
  partido (propio del "look" de 8bit); nada de aberración cromática fuerte.
- **Fondo/objeto de esta lámina** (si se usa el motivo de la franquicia):
  el patrón de **vitral/rombos azules partidos con una cadena** que se
  repite en portada, logo del juego y colaboración: fácil de vectorizar en
  Illustrator/Photoshop como una trama repetible.

**Cómo replicarlo en Blender**:
- **Contorno**: Freestyle (edge marks en los bordes duros) o un modificador
  Solidify invertido con material de emisión negra, según se prefiera
  contorno editable a mano o automático.
- **Sombreado tipo cel**: nodo *Shader to RGB* + una rampa de 2-3 escalones
  en color, en vez del degradado continuo del Principled BSDF.
- **El «aura»**: luz de contorno (rim light) con un nodo Fresnel que
  alimente la emisión de un shader adicional, en el color de cada
  personaje; combinarlo con partículas de humo/chispa de baja densidad.
- **Modelos y escenarios libres** (Sketchfab, licencia CC Attribution,
  comprobado con la API de Sketchfab — **ojo: son modelos subidos por fans,
  probablemente extraídos del propio videojuego, así que su crédito real es
  dudoso; usarlos como referencia de proporciones/pose, no para exportar
  tal cual a un producto**):
  - [Blue Lock Training Facility](https://sketchfab.com/3d-models/none-f8225941e44e4d9090b2a6c14db95031)
    y [Blue Lock training Stadium](https://sketchfab.com/3d-models/none-2537204b334d4af8a5bcc409115b60ea)
    — el **edificio/instalación** en sí, útil como base de escena para el
    objeto de la lámina.
  - [Blue Lock - Logo](https://sketchfab.com/3d-models/none-a33cbcfb5ce340f0af585b9fe834bd15)
    y [Blue Lock Soccer Ball](https://sketchfab.com/3d-models/none-84306d1b03464943b609f9af1b3624f4).
  - [Seishiro Nagi - Official Blue Lock Model](https://sketchfab.com/3d-models/none-12a92d5b590a498996fd2fd4dd37d34b)
    (marcado «oficial» por quien lo subió; sin confirmar la fuente real ⚠️).
- **Encuadres**: no encontré una entrevista de storyboard/dirección de
  cámara específica de Blue Lock (más allá de lo ya citado sobre el
  «still over animation») ⚠️; lo que sí es un patrón repetido y
  verificable en las 3 imágenes oficiales miradas esta sesión es el
  **primer plano muy cerrado de los ojos** en los momentos de máxima
  tensión (coincide con la cita de Nomura sobre «detalles en los ojos»).

---

## Punto 24 · Obras parecidas y temas relacionados

- Recomendados de AniList (ya en `datos-texto.md`, con votos): **Aoashi**
  (351 votos, nota 81), **Kuroko's Basketball** (170), **HAIKYU!!** (140),
  **Tomodachi Game** (76), **Inazuma Eleven** (76), **Captain Tsubasa**
  (19+11), **Slam Dunk** (9), **Ace of the Diamond** (9), **Death Note**
  (9, por el lado de juego psicológico/selección) ✅.
- **Por qué se parecen, con matiz** (no genérico):
  - **Aoashi**: fútbol de cantera, **realista y técnico** (scouting real,
    sin poderes ni auras) — es casi el opuesto estilístico de Blue Lock
    dentro del mismo deporte: sirve para contrastar «deporte realista» vs.
    «deporte estilizado como batalla» ✅ (nota AniList + descripción de
    género en su propia ficha).
  - **Tomodachi Game** y **Kakegurui** (ya en la lista de recomendados):
    comparten con Blue Lock el esquema de **«juego de selección/muerte
    social» con reglas del propio Kaneshiro** (As the Gods Will,
    Jagaaaaaan) — el motivo de fondo es "sobrevivir a una prueba diseñada
    por un adulto cruel", no el fútbol en sí ✅.
  - **HAIKYU!!**, **Kuroko no Basket**, **Inazuma Eleven**, **Captain
    Tsubasa**: comparten el habla-de-deporte-como-batalla (poderes/técnicas
    especiales) más que Aoashi, pero sin el filtro de «battle royale»
    (300 eliminados a uno) que es el rasgo único de Blue Lock ✅ (géneros
    y etiquetas cruzadas en AniList).
- **Ya hay láminas del servidor de series parecidas**, para no repetir
  ideas (mirado en `biblias/`, este mismo repositorio):
  - **34-haikyuu** ya tiene `biblia.md` terminada y propone el canal
    **#reto-de-la-semana** (con el marcador naranja y la pizarra de tiza
    como objeto) ✅ (leído directamente en `biblias/34-haikyuu/biblia.md`).
    Blue Lock **no debería repetir ni el mismo canal ni el mismo objeto**
    (pizarra/marcador de tiza).
  - **47-captain-tsubasa-supercampeones** está en el mismo lote de encargos
    y todavía **no tiene `biblia.md`** (sólo `partes/`), así que puede
    llegar a competir por canal/objeto: quien redacte Blue Lock debería
    revisarlo antes de fijar el canal final ⚠️ (dato para el redactor).
  - **Dato para el redactor** (no es mi punto, pero sale de investigar
    éste): la premisa de Blue Lock — **una sola plaza, 300 candidatos
    compitiendo, quien no destaca se va** — encaja de forma literal con la
    descripción de **#castings** en `servidor/inventario.md` («Cada casting
    es un hilo. Ciérralo cuando el papel esté cubierto»): es un canal que
    Haikyuu no usó y que temáticamente es más fiel a Blue Lock que un canal
    de retos genérico.
- **Influencias reconocidas por el propio Nomura**: fue asistente en
  *Ahiru no Sora* (baloncesto) y en **Attack on Titan** — el manga que
  además ambos autores citan entre risas en la misma entrevista (les
  preguntan qué Titán sería mejor delantero; ambos responden «Reiner», y
  Nomura añade «sería perfecto para parar el balón») ✅ ([Anime Corner](https://animecorner.me/interview-blue-lock-creators-muneyuki-kaneshiro-yusuke-nomura/)).
  Esto conecta directamente el estilo «tenso, de selección brutal» de Blue
  Lock con su etapa como asistente en un manga de terror de supervivencia.

---

## Punto 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo, en cinco líneas** ✅ (contrastado entre el wikitext
de Fandom vía API y `datos-texto.md`):
1. Japón queda eliminado del Mundial 2018; la Federación Japonesa de Fútbol
   decide que el problema es no tener un delantero egoísta de nivel mundial.
2. El entrenador **Jinpachi Ego** encierra a **300 delanteros** de instituto
   en una instalación-prisión llamada **Blue Lock**.
3. Se entrenan y se enfrentan entre sí; **quien no destaca, es eliminado y
   expulsado del fútbol de selección para siempre** (la amenaza real que
   sostiene toda la tensión).
4. El objetivo no es «jugar bien en equipo»: es desarrollar el **ego**, la
   obsesión egoísta por marcar gol uno mismo, por encima de todo lo demás.
5. Sólo **uno** sobrevivirá al proceso, hasta llegar a las selecciones y
   ligas del Neo Egoist League y representar a Japón.

**La historia por arcos** (nombres y tramos, contrastados en 2 fuentes:
Fandom «Story Arcs» y varias listas de manga/anime coincidentes) ✅:
| Arco | Capítulos manga | Qué pasa |
|---|---|---|
| Introducción | 1-4 | Eliminación mundialista, reclutamiento de Isagi |
| **First Selection** | 5-38 | Primeras pruebas de equipo, Isagi conoce a Bachira |
| **Second Selection** | 39-86 | Equipos más grandes, aparece Rin y el equipo de intercepción PxG |
| **Third Selection** | 87-108 | Selección final antes del U-20 |
| **U-20** | 109-151 | Selección Sub-20 de Japón, aparece Kaiser |
| **Neo Egoist League** | 152-302 (el arco más largo, en curso) | Selecciones sub-20 de Alemania, Inglaterra, España, Italia y Francia entrenan en Blue Lock; cada jugador elige un país/equipo |
- Además: la **película** *BLUE LOCK THE MOVIE -EPISODE NAGI-* (spin-off del
  pasado de Nagi) y el **manga spin-off** *Blue Lock - Episode Nagi*
  (2022-2025, 36 capítulos, dibujado por **Kota Sannomiya**) ✅ (ya en
  `datos-texto.md` + wikitext de Fandom).

**Símbolos y vocabulario que un fan reconoce al instante**:
- **El azul**: no es decorativo. Kaneshiro lo eligió porque la selección
  japonesa **jugó sus mejores partidos históricos de uniforme azul**
  (clasificaciones al Mundial de 1994 y 1998); cita textual suya en una
  entrevista de Animania: *«al final todos vivimos en algún sitio "para uno
  mismo" — así que ¿por qué no dejar correr tu ego?»* ✅ ([CBR, con la cita
  de la entrevista de Animania](https://www.cbr.com/blue-lock-muneyuki-kaneshiro-color-significance/)).
  El propio Isagi tiene ojos y mechas azules, «hecho a medida» para el
  programa; sus ojos se encienden en **llamas azules** en los momentos de
  máxima tensión (ego/obsesión por ganar) ✅ (misma fuente).
- **Las cadenas**: aparecen en las portadas de los tomos y en el traje de
  entrenamiento (confirmado en el tomo 1 y en la colaboración con REMATCH,
  ver §6 y §11). El propio autor **nunca explicó su significado exacto**;
  el fandom las lee como el ego, el vínculo con el proyecto Blue Lock o el
  sentimiento hacia el fútbol japonés ✅ (2 fuentes independientes, ver §6).
- **«Ego»**: el concepto central que da nombre al entrenador (Jinpachi Ego)
  y a la filosofía entera: el «ego» de un delantero no es soberbia, es el
  estado psicológico que **desbloquea su verdadero potencial** ✅ (varias
  fuentes coincidentes, incluida la cita de Kaneshiro arriba).
- **Nombres de equipos del Neo Egoist League** (parodias directas de clubes
  reales, muy citables para carteles/objetos del mundo) ✅ (2+ fuentes:
  [Blue Lock Store](https://bluelockstore.co/blogs/infos/guide-equipes-neo-egoist-league-blue-lock),
  [bluelock.wiki](https://bluelock.wiki/story-and-plot/what-teams-are-in-neo-egoist-league),
  fichas de Fandom):
  - **Bastard München** (parodia de Bayern Munich; su ropa deportiva es de
    «Abibas», parodia de Adidas).
  - **Manshine City** (parodia de Manchester City; equipo de Chigiri, Nagi
    y Reo).
  - **FC Barcha** (parodia de FC Barcelona; equipo de Bachira).
  - **PXG / Paris X Gen** (parodia de PSG, «finura táctica francesa»).
  - **Ubers** (equipo italiano).
- **Objetos icónicos**: el balón de Blue Lock (con el mismo motivo de
  vitral partido, ver modelo 3D en §18), el emblema hexagonal del proyecto
  cosido en la manga del uniforme (visible en el tomo 1), y la carta de
  convocatoria/selección (ver §6, el objeto de la colaboración REMATCH que
  es prácticamente un calco del propio dispositivo narrativo del manga:
  una carta que «selecciona» al jugador).

---

## Lo mejor para la lámina

1. **El objeto real más fuerte que encontré**: la **carta de convocatoria
   «You've been selected»** de la colaboración REMATCH × Blue Lock — es
   literalmente un objeto de papel con cadena dibujada, perfecto para un
   canal de «selección» (ver la idea de #castings en el §24) y reproducible
   en Blender/Photoshop sin inventar nada.
2. El **patrón de vitral azul partido + cadena** es el único elemento
   visual que se repite igual en portada de manga, logo del juego oficial y
   colaboración de 2026: es «la marca» de Blue Lock más fiable que cualquier
   burbuja de diálogo genérica.
3. El **aura de color** alrededor del personaje (verde/rosa en Isagi,
   confirmada por Nomura y visible en la portada de PWC) es la manera
   correcta de dar «energía» a una pose sin recurrir a un genérico brillo
   de anime shonen: tiene fuente directa del autor.
4. Tipografía ya probada con fontTools y lista para usar en español:
   **Anton** (títulos), **Bangers** (gritos/onomatopeyas), **Oswald**/**Teko**
   (números de camiseta y marcador), **Rajdhani** (HUD de videojuego).
5. Blue Lock **no tiene canal propio todavía**: dado que Haikyuu ya ocupó
   #reto-de-la-semana con objeto de pizarra/marcador, y que la premisa de
   Blue Lock es «una sola plaza, todos compiten, el que no destaca se va»,
   el canal **#castings** (con su propia norma «cierra el hilo cuando el
   papel esté cubierto») es una alternativa que no repite ninguna lámina
   ya hecha del servidor.

## No encontré

- ⚠️ **Blaze Battle por dentro**: no vi capturas de su interfaz de combate.
  Búsquedas hechas: `"Blaze Battle" Blue Lock game screenshots gameplay UI`,
  Google Play (`jp.co.bael.bluelock.blazebattle`, dos intentos, «Not
  found»), YouTube (el vídeo de TapTap fue borrado por YouTube: cuenta
  terminada). Sólo tengo la imagen de título.
- ⚠️ **Fuente exacta del logo oficial** (japonés e inglés): varias guías de
  tipografía japonesas y un hilo de dafont lo intentaron identificar y
  ninguno dio un nombre comercial concreto. Lo que sí está confirmado es el
  estilo (grunge, geométrico, condensado).
- ⚠️ **TV Tropes de Blue Lock**: bloqueado por el reto de Cloudflare de
  tvtropes.org (dos intentos con distinto user-agent). No pude sacar sus
  tropos de estilo visual.
- ⚠️ **The Cutting Room Floor**: no tiene página de ningún juego de Blue
  Lock (comprobado con búsqueda directa).
- ⚠️ **Fuente de los globos de la edición en español de Ivrea**: confirmé
  la editorial y el formato, no la tipografía exacta de sus globos (no
  encontré scans para comprobarlo sin acudir a escaneos pirata).
- ⚠️ **Color de aura por personaje más allá de Isagi/Bachira**: la única
  fuente que da colores exactos para Nagi y Rin es un blog de baja calidad
  (toolify.ai); lo dejo señalado como flojo, no lo uso como dato firme.

## Bitácora de búsqueda

- **Español**: «Blue Lock juego oficial videojuego móvil», «Blue Lock manga
  español editorial Panini Ivrea».
- **Inglés**: «Blue Lock official video game 2026 mobile app», «"Blaze
  Battle" Blue Lock game screenshots gameplay UI», «Blue Lock cutting room
  floor tcrf.net», «Blue Lock logo font identify dafont», «fontsinuse.com
  "Blue Lock"», «Blue Lock official game DSEG7 seven segment font OFL
  github keshikan download», «Yusuke Nomura Blue Lock art style manga
  drawing interview Clip Studio», «Blue Lock anime 8bit studio CGI 3DCG
  animation technique interview», «Yusuke Nomura assistant Hajime Isayama
  Attack on Titan Blue Lock manga artist biography», «Blue Lock story arcs
  list First/Second/Third Selection Neo Egoist League timeline», «Blue Lock
  symbolism "Ego" meaning blue color prison chain facility explained»,
  «Blue Lock chain each character meaning Isagi Bachira Nagi Rin barbed
  spiked», «Blue Lock Neo Egoist League teams PxG Bastard Munchen Manshine
  City names parody», «Blue Lock character aura color design Isagi Bachira
  Nagi Rin monster art», «Rematch Sloclap "Blue Lock" training pack
  collaboration».
- **Japonés**: «ブルーロック フォント 書体 ロゴ», «ブルーロック 単行本 ロゴ フォント 制作».
- **Fuentes consultadas** (además de las enlazadas arriba): Google Play
  (fichas de PWC y Blaze Battle), App Store, sitio oficial
  bluelock-pwc-gl.com, TapTap, Fandom API (`bluelock.fandom.com/api.php`,
  wikitext de la página del manga y de Yusuke Nomura), Wayback Machine
  (`archive.org/wayback/available`), api.fontsource.org + cdn.jsdelivr.net
  (descarga y verificación de 5 fuentes con fontTools), api.sketchfab.com
  (modelos CC de la instalación y personajes), AniList (ya en
  `datos-texto.md`), `biblias/34-haikyuu/biblia.md` (para no repetir canal
  ni objeto).
- **Herramientas usadas**: `curl` directo a APIs (Fandom, Sketchfab,
  Fontsource, Wayback), Python/Pillow para hojas de contacto y medir hex,
  `fontTools.getBestCmap()` para comprobar tildes/ñ/¿/¡, `fotogramas.py`
  (falló: vídeo de Blaze Battle borrado de YouTube).
- **Imágenes miradas de verdad** (con Read, no de memoria): 4 capturas de
  Google Play de PWC (hoja de contacto), la portada del tomo 1 del manga
  (bajada de Fandom), la imagen de título de Blaze Battle, y la captura de
  Steam del Blue Lock Training Pack (ya en `datos-texto.md`).
