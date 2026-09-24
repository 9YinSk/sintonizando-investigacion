# Parte de TEXTO, JUEGOS Y TÉCNICA · Encanto (encargo 58)

Investigador de texto, juegos y técnica. Puntos 5, 6, 11, 18, 24 y 25 de `ENCARGO.md`.
Encanto es película de Disney (2021), no anime: cuadros de diálogo y "videojuegos" son
los de sus adaptaciones (cómics, libros ilustrados, apariciones en juegos móviles Disney).
`partes/datos-texto.md` (recolectado por `recolectar.py`) no trajo nada útil: sólo dos
capturas de Steam de juegos sin relación (una colección de Dead or Alive y un DLC de
"Buena Pizza, Gran Pizza" llamados "Encanto/Encanto Rural" por coincidencia de nombre).
Descartadas, no se repitió esa búsqueda; toda la investigación de este archivo es nueva.

## Hallazgos

### Punto 5 — Tipografía

- **Logo/título de Encanto (2021)**: no es una fuente comercial existente, es **lettering
  custom** hecho para la película por el equipo de diseño de Disney — trazo fino con
  remates curvos y puntiagudos (muy visible en la I, la L y la U), astas que alternan
  grueso y fino, con curvas y volutas ornamentales que salen de varias letras (una rama/vid
  floral, a tono con el realismo mágico) · fuente: HipFonts («thin lines and curvy edges,
  letters like I, L and U possessing curved and sharp-edged terminals, font stems mixture
  of bold and thin») **y** coincide con la ficha de FreeFontsVault/ActionFonts (mismas
  características, custom design team, sin fuente comercial oficial liberada) ✅ (dos
  fuentes tipo "font finder", coincidentes en la descripción del trazo)
  - **Réplica fan más citada — fuente "Madrigal" de NubeFonts** (autor colombiano): según
    varias fichas de descarga «incluye todas las volutas y curvas presentes en el logo
    original, casi una réplica exacta» · **descargada y comprobada yo mismo con fontTools**
    (`Madrigal-mLJ92.ttf`, v1.000, 29-ene-2022, vía `1001fonts.com/download/madrigal.zip`):
    contra lo que decían varias fichas de descarga («sólo mayúsculas»), el archivo real
    **SÍ trae el juego completo**: á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ — todos presentes en el
    `cmap` ✅ (comprobado en el archivo, no de memoria). Licencia confusa entre sitios
    espejo (unos dicen "gratis sólo uso personal", otros "libre para comercial"); sin una
    página oficial de NubeFonts accesible para confirmar los términos exactos → **usar con
    cautela y linkear siempre la fuente**, o preferir las alternativas 100% libres de abajo
    para cualquier uso que vaya a publicarse.
  - **Alternativas 100% libres (OFL-1.1), descargadas de Fontsource y comprobadas con
    fontTools para el juego completo (á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡) — las tres COMPLETAS**
    (nota técnica del propio proceso: el archivo por subset "latin-ext" de Fontsource NO
    trae estos caracteres — están en el subset "latin"/Latin-1 Supplement; hay que pedir
    el archivo `latin-400-normal.ttf`, no `latin-ext-…`):
    - **Yeseva One** (Fontsource `yeseva-one`, display, contraste grueso/fino como el
      logo) · https://fontsource.org/fonts/yeseva-one · OFL-1.1 · completa ✅ — la mejor
      para el título/logo por el contraste de trazo.
    - **Berkshire Swash** (Fontsource `berkshire-swash`, redondeada y cálida) ·
      https://fontsource.org/fonts/berkshire-swash · OFL-1.1 · completa ✅ — sirve para
      texto corto festivo (p. ej. un cartel de bienvenida).
    - **Pacifico** (Fontsource `pacifico`, script casual, muy usada en branding
      latinoamericano) · https://fontsource.org/fonts/pacifico · OFL-1.1 · completa ✅.
  - **Las 8 letras por uso que pide el punto 5** (Encanto no es manga: los usos "globo
    normal/grito/pensamiento/onomatopeya" salen de su cómic **The New Adventures of
    Encanto** de Papercutz, ver punto 6; el resto, del propio filme y sus juegos):
    1. **Logo/título** → lettering custom cubierto arriba (Madrigal / Yeseva One).
    2. **Globo normal** (cómic Papercutz) → sans-serif de cómic estándar, redondeado,
       mayúsculas, sin ficha tipográfica publicada por el estudio (formato ilustrado, no
       fotográfico, a diferencia del Cinestory de Coco) ⚠️.
    3. **Grito** y **4. Pensamiento**: no se encontró una página de muestra pública del
       cómic con globo de grito o de pensamiento — el libro salió el 23-jul-2024 y no hay
       "look inside" completo accesible (Amazon/Google Books sin vista de interior más
       allá de la portada) ⚠️ **No encontré** (búsqueda hecha, ver Bitácora).
    5. **Onomatopeya**: no aplica de forma nativa — no hay tradición de onomatopeyas
       dibujadas en el merchandising de Encanto (a diferencia de un manga); anotado como
       "no aplica, con la búsqueda hecha" en vez de inventarlo.
    6. **Cartel del mundo**: el letrero pintado a mano del pueblo/la fachada de la Casita
       (puerta tallada con la familia, ver punto 25) — sin fuente digital documentada,
       es arte de producción pintado ⚠️.
    7. **Interfaz de juego**: resuelto en el punto 6/11 con capturas reales de Disney
       Magic Kingdoms, Disney Heroes: Battle Mode y Disney Speedstorm — todas usan
       tipografía sans de interfaz genérica de esos juegos, sin ficha de fuente publicada
       por sus estudios (Gameloft/PerBlue) ⚠️.
    8. **Subtítulos/créditos**: sans-serif blanca con borde negro fino, estándar de
       Disney+/Blu-ray; no se encontró ficha técnica pública del tipo exacto (igual que en
       el resto de la colección Disney) ⚠️ **No encontré**.
  - **Letra libre sugerida para los usos sin fuente oficial documentada** (todas OFL,
    comprobadas con fontTools, completas para á é í ó ú ñ Ñ ¿ ¡):
    - **Globo normal / cartel del mundo** → **Baloo 2** peso 700 (redondeada, amigable,
      Fontsource `baloo-2`, OFL) — igual que se usó para Coco, mismo criterio de letra
      "cómic infantil cálido" ✅.
    - **Interfaz de juego** → **Fredoka** (Fontsource `fredoka`, geométrica redondeada,
      look de app móvil actual) ✅.
    - **Subtítulos/créditos** → **Open Sans** (Fontsource `open-sans`, Apache-2.0, la
      sans más usada del mundo para subtítulos, legible en pantalla chica) ✅.

### Punto 6 — Cómo hablan y piensan en pantalla

Encanto no tiene manga; sus "globos" y cajas de texto son los de su cómic y los de los
juegos donde aparece.

- **The New Adventures of Encanto, Vol. 1: Time to Shine** (Papercutz, sello **The Disney
  Comics Group**, publicado **23-jul-2024**, 88 páginas, tapa dura ISBN 9781545802328 /
  rústica ISBN 9781545811542) · guion de **Amparo Ortiz**, arte y portada de **Andrea
  Greppi**, coloreado de Maria Claudia Di Genova, letras de Chris Dickey · recoge 4
  historias familiares cortas (visiones secretas, un concurso de talentos, nuevas
  amistades) para lectores de 8 a 12 años, con Mirabel como hilo conductor ("recordando a
  su familia que su mayor fortaleza es estar unidos") · fuente: fichas de venta cruzadas
  de Amazon **y** Biblio.com/Walmart (mismo ISBN, misma ficha de crédito) ✅ (dos fuentes)
  — **es dibujado, no fotográfico** (a diferencia del Cinestory de Coco), así que sus
  globos son ilustrados por Greppi con estilo propio del cómic, coherente con el diseño
  Disney pero no una copia 1:1 del render 3D de la película.
- **Cajas de diálogo reales de videojuegos** (ligado al punto 11, texto sacado directo del
  wikitext oficial de cada wiki, no inventado):
  - **Disney Heroes: Battle Mode** — cada héroe tiene una frase de presentación en una caja
    con comillas grandes bajo su retrato: **Mirabel Madrigal**: *"Some of us have bigger
    problems."* · **Isabela Madrigal**: *"So much hides behind my smile."* · **Bruno
    Madrigal**: *"Bruno makes bad things happen."* (auto-referencia a "We Don't Talk About
    Bruno") · **Luisa Madrigal**, frase larga tipo advertencia dentro de su descripción de
    habilidad: *"Give it to your sister, it doesn't hurt n' see if she can handle every
    family burden."* · fuente: `disneyheroesbattlemode.fandom.com/wiki/Mirabel_Madrigal`,
    `/Isabela_Madrigal`, `/Bruno_Madrigal`, `/Luisa_Madrigal` (wikitext vía API) ✅ (fuente
    primaria del propio juego, contrastada entre las 4 fichas con el mismo formato)
  - **Disney Magic Kingdoms** — evento «Encanto Event 2023» (lanzado **16-mar-2023**),
    con una cadena de misiones tituladas literalmente como frases del propio personaje/
    tono de la serie: *"Welcome a Middle Sister"* (Luisa) · *"Welcome a Big Sister"*
    (Isabela) · *"Welcome a Seer"* (Bruno) · *"Welcome... NOT Camilo"* (chiste sobre el
    don de imitar de Camilo, 01-abr-2023) · *"Watch the Frame!"* · *"Family Time!"* ·
    *"It's Very Detailed!!!"* · *"Ingenious!!!"* · *"Time to Wrap"* · *"Missing Pieces"* ·
    fuente: `dmk.fandom.com/wiki/Encanto_Event_2023` (wikitext vía API, con fechas exactas
    de cada capítulo) ✅.
  - **Disney Speedstorm** — la ficha de Mirabel confirma que su voz en el juego es la
    **misma actriz de la película, Stephanie Beatriz** (no una voz genérica de doblaje de
    videojuego, algo poco común en estos juegos móviles) · fuente: wikitext de
    `speedstorm.fandom.com/wiki/Mirabel` (campo `voice = Stephanie Beatriz`) ✅ — sin
    citas textuales de sus líneas de carrera publicadas en la wiki todavía (personaje muy
    reciente, lanzado 30-jul-2026).
  - **Disney Solitaire** — el minijuego organiza sus "Sets" de stickers por película; el
    de Encanto (4º set del álbum "Around The World", 12 stickers, **15-jul al
    27-ago-2025**) usa las caras de Mirabel, Julieta, Alma, Chispi, Casita, Antonio y
    Luisa como iconos coleccionables, sin diálogo escrito · fuente:
    `disneysolitaire.fandom.com/wiki/Encanto` (wikitext) ✅.
- **Subtítulos oficiales**: en Disney+ los subtítulos en español usan la tipografía sans
  blanca con borde negro estándar de la plataforma; no se encontró ficha técnica pública
  del tipo exacto → **No encontré** (misma conclusión que en el resto de la colección de
  biblias del servidor) ⚠️.

### Punto 11 — Videojuegos de la franquicia

Encanto no tuvo un videojuego propio de consola/PC (como Cars o Toy Story); aparece como
contenido dentro de **seis** juegos móviles/servicio de Disney, con distinto nivel de
detalle documentado:

- **Disney Magic Kingdoms** (móvil, gacha de construcción) — evento **«Encanto Event
  2023»**, lanzado **16-mar-2023**, 4 capítulos escalonados hasta el 01-abr-2023:
  personajes desbloqueables **Antonio, Luisa, Isabela, Bruno y Mirabel** (en ese orden);
  edificios **Casita** y **la habitación de Isabela**; ítem de paseo **«Encanto Float»**
  (carroza de desfile); moneda especial **"Relic ENCANTO"**; objeto de merchandising in-
  game **"Encanto Mouse Ears Headband"** · fuente: wikitext oficial de
  `dmk.fandom.com/wiki/Encanto_Event_2023` (tabla completa de fechas/precios de la tienda
  del evento) **y** confirmación cruzada en la página `Encanto_Event_Storyline_2023` de la
  misma wiki ✅ (dos páginas de la misma fuente primaria, con datos coincidentes).
- **Disney Heroes: Battle Mode** (móvil, RPG de combate por turnos) — **4 héroes** del
  grupo "Encanto": **Mirabel Madrigal** (Support/Backline, habilidad pasiva cura en vez de
  atacar, activa "All of You!" inspirada en la canción homónima) · **Isabela Madrigal**
  (Damage/Back, habilidad "Prickly Pass" con cactus y veneno) · **Luisa Madrigal**
  (Tank/Front, "Devastating Debris" lanza escombros) · **Bruno Madrigal** (Support/Front,
  "Sand Shroud" crea un escudo de arena y aturde con "confusión", tema de sus visiones) ·
  cada uno se desbloquea con 10 chips propios · fuente: wikitext de las 4 fichas de
  personaje en `disneyheroesbattlemode.fandom.com` (grupo, rol, habilidades exactas) ✅.
- **Disney Speedstorm** (F2P de carreras, Gameloft) — **Colección "Encanto"** con 3
  corredoras: **Isabela** y **Luisa** (ya en el juego) y **Mirabel**, clase **Defender**,
  añadida el **30-jul-2026** (personaje muy reciente), voz de **Stephanie Beatriz** (su
  actriz original) · fuente: wikitext de `speedstorm.fandom.com/wiki/Mirabel` **y**
  categoría `Category:Encanto` de la misma wiki (lista los 3 corredores) ✅ (dos consultas
  a la misma wiki, coincidentes).
- **Disney Dreamlight Valley** (simulador de vida/aventura, Gameloft) — **Mirabel** es
  villager jugable desde la actualización **«A Festival of Friendship» (v1.3, 16-feb-
  2023)**, desbloqueada al final de la misión de amistad de Merlín "The Golden Doorknob";
  su casa es la **Mini-Casita**; recompensas de amistad incluyen ropa temática — **"Teal
  Dreamlore Ruana"** y **"Emerald Dreamlore Skirt"** (nivel 10) — y mobiliario **"Ceremony
  Day Gift"** (referencia directa a la ceremonia del don) · fuente: wikitext de
  `disneydreamlightvalley.fandom.com/wiki/Mirabel` (fecha de versión, objetos exactos) ✅
  — **no hay un "reino" o biome dedicado a Encanto** en este juego (a diferencia de otras
  películas), sólo el personaje y objetos de decoración; comprobado con la búsqueda del
  wiki (`srsearch=Encanto`), que sólo devuelve la ficha de Mirabel y objetos sueltos, sin
  ninguna página de "realm".
- **Disney Emoji Blitz** (móvil, match-3 de emojis) — set de **personajes Encanto**:
  Mirabel (con variantes coleccionables **Mosaic Mirabel**, **Embroidered Mirabel** y
  **Platinum Mirabel**), Alma Madrigal, Julieta, Isabela, Luisa, Camilo y **Smoky Quartz
  Bruno** · la habilidad de Mirabel en el juego: *"comforts Antonio with a gift, bringing
  heart-eyes to the surrounding emojis"* (260 puntos base) · fuente: wikitext de
  `disneyemojiblitz.fandom.com/wiki/Mirabel` (infobox de habilidad, expresiones del emoji:
  Happy/Heart Eye/Unhappy/Nervous/Surprised/Sleeping) ✅.
- **Disney Solitaire** — detallado arriba en el punto 6 (set de 12 stickers, jul-ago
  2025) ✅.
- **No encontrado / no aplica** (con la búsqueda hecha, no dado por sentado):
  - **Kingdom Hearts**: sin mundo ni personaje de Encanto confirmado en ningún título de la
    saga (ni siquiera Kingdom Hearts IV, que sí confirmó un mundo de Coco en 2026 — ver
    biblia gemela de Coco); sólo hay peticiones y fan art de la comunidad pidiéndolo ⚠️ no
    aplica, con búsqueda hecha (`Kingdom Hearts Encanto world Mirabel confirmed`).
  - **Disney Sorcerer's Arena**: la ficha de "Casa Madrigal" en Disney Wiki la lista entre
    los juegos donde aparece la Casita, pero no se pudo entrar directamente a esa wiki
    (`sorcerersarena.fandom.com` da 404, dominio distinto no localizado) ni confirmar con
    una segunda fuente independiente → queda como **una sola fuente, sin verificar** ⚠️.
  - **"Disney POP TOWN"**, también listado en esa misma ficha junto a los juegos: **no es
    un videojuego**, es la línea de figuras de colección **Funko Pop! Town** (se confirmó
    con la búsqueda: "Funko Pop! Town: Disney Encanto Mirabel with Casita", preventa
    feb-2024) — corregido aquí para no arrastrar el error a la biblia; se anota en el
    punto 23 (colaboraciones/figuras) en vez de aquí.
  - **The Cutting Room Floor (TCRF)**: sin página de Encanto — búsqueda `site:tcrf.net
    Encanto` sin resultados relacionados (coherente con que no existe un juego "propio" de
    consola que minar; incluso Coco, con más presencia en videojuegos vía Kingdom Hearts,
    tampoco tiene página en TCRF).

### Punto 18 — Estilo de dibujo/técnica y cómo replicarlo

Encanto es 3D fotorrealista/estilizado de **Walt Disney Animation Studios**, renderizado
con el motor propio **Hyperion** (path tracer físicamente basado, el mismo que Frozen 2,
Raya y Big Hero 6) — no tiene "línea" tipo cel-shading, la réplica va por iluminación,
materiales y color, no por contorno.

- **Investigación de campo real en Colombia**: en **2018** el equipo (incluidos los
  directores **Byron Howard**, **Jared Bush** y la co-directora/guionista **Charise Castro
  Smith**) viajó a **Bogotá, Cartagena, Barichara, Salento, Palenque y el Valle de
  Cocora**, documentando arquitectura, botánica y vida cotidiana antes de diseñar nada ·
  se formó el **"Colombian Cultural Trust"** (fideicomiso cultural), un grupo de
  consultores colombianos contratado por el estudio — entre ellos **Juan Rendón**,
  **Natalie Osma** (consultores principales, acompañaron al equipo a Bogotá y Cartagena),
  **Alejandra Espinosa** (guía local en Barichara, luego contratada como consultora),
  **Felipe Zapata**, **Martín y Stefano Anzellini**, y la periodista afrocolombiana **Edna
  Liliana Valencia** (consultada para la representación de la comunidad afrocolombiana) ·
  cita del codirector Byron Howard: *"Colombia is like many countries packed into one, so
  we had to be careful not to just ask our consultants from one region"* · fuente: blog
  oficial de **ACM SIGGRAPH** («The Colombian Cultural Trust, Technological Advancements,
  and TikTok Fame of Disney's 'Encanto'», blog.siggraph.org/2022/02) **y** artículo
  cruzado sobre el viaje de investigación (Latinx Project / prensa especializada, misma
  cronología 2018 y mismos lugares) ✅ (dos fuentes).
- **Diseño de vestuario, ejemplo documentado a fondo (Bruno)**: la líder de diseño de
  vestuario **Neysa Bové** (primera vez que "Costume Design" aparece acreditado como
  puesto propio en una película de animación de Disney, según ella misma) explicó que la
  ruana de Bruno se rediseñó tras consultar al equipo de expertos colombianos — de un
  "adivino de 1900" genérico a un **poncho/ruana ceremonial real**, verde esmeralda (por
  el comercio de esmeraldas de Colombia y su asociación mística con la adivinación), con
  agujeros pequeños hechos por ratas y un tono de piel grisáceo por su aislamiento sin sol
  · la visual development artist **Meg Park** diseñó la iconografía de la ruana, inspirada
  en el pueblo indígena **Quimbaya** · fuente: **Animation World Network** («Neysa Bove
  Dives Into the Very Fabric of Animation Costume Design») **y** ScreenRant/Wikipedia
  (cita de Park sobre "the old ceremonial outfit... for the people who came to see him")
  ✅ (dos fuentes) — **para replicar**: capas de tela con desgaste procedural (mapas de
  máscara para "agujeros de rata"), un verde esmeralda saturado como acento de color único
  del personaje dentro de una paleta doméstica más apagada.
  - El vestido de Isabela (para contraste de técnica): influido por los vestidos de la
    **danza del Bambuco** y las fiestas de las flores colombianas; mangas y volantes de
    **tela punteada semitransparente (Swiss dot)** sobre lavanda sólido, con flores
    pintadas o apliques 3D cosidos encima para dar textura — Neysa Bové consultó a un
    **botánico** para la flora exacta · fuente: Brother-USA (guía de costura, cita a
    Bové) **y** Popverse (guía de cosplay, mismos detalles de tela) ✅.
- **Equipo de dirección de arte** (créditos, dos fuentes): **Lorelay Bové** — diseñadora
  de producción asociada (associate production designer), junto al diseñador de
  producción **Ian Gooding**; **Bill Schwab** — director de arte de personajes; **Camille
  André** y **Mehrdad Isvandi** — directores de arte de entornos; **Jin Kim** — diseñador
  de personajes/artista de desarrollo visual (el mismo que Frozen, Big Hero 6, Raya);
  **Deanna Marsigliese** — directora de arte de personajes · Lorelay Bové (Voyage LA,
  D23): trabajaron con arquitectos, botánicos y antropólogos, reuniéndose semanalmente con
  los consultores para revisar cada diseño · fuente: `walt-disney-animation-
  studios.fandom.com/wiki/Encanto_Credits` **y** Hollywood Reporter («Encanto, Flee
  Artists on How They Designed Their Animated Characters») ✅ (dos fuentes).
- **Iluminación y shaders — el reto técnico central** (blog técnico **oficial** de un
  ingeniero de renderizado de Disney Animation, Yining Karl Li, `blog.yiningkarlli.com`,
  fuente primaria de estudio):
  - Se añadió un **lóbulo de brillo ("sheen") de dispersión múltiple físicamente preciso**
    al BSDF de Disney (el shader base de todo el estudio), y un nuevo **shading de ojos
    con cáusticas físicas de iris** (manifold next event estimation), usado por primera
    vez en el 100% de los personajes de una película.
  - Los **trajes se renderizaron como curvas tejidas hilo a hilo**, no como mallas con
    relieve — clave para lograr el **chifón y tul del vestido de Isabela** y la falda
    bordada de Mirabel.
  - **Path guiding** para la iluminación indirecta en interiores (p. ej. la cocina de los
    Madrigal de noche).
  - **Shader de teletransporte de rayos** desarrollado específicamente para las **visiones
    holográficas de Bruno** (las tabletas de esmeralda con profecías): mapea matemáticamente
    los rayos que tocan la superficie de "portal" de entrada a un "portal" de salida
    (técnica de "best-fit orthonormal transforms" heredada del sistema de fractura de
    Hyperion), con una mezcla de BSDF pintable para el desvanecido en los bordes; sustituyó
    a un sistema anterior de holograma "pre-horneado" y se implementó en **una semana**,
    inspirado en el efecto de portales de *Los Increíbles 2* de Pixar · presentado como
    charla técnica oficial en **SIGGRAPH 2022**: *"Encanto - Let's Talk About Bruno's
    Visions"* (DOI `10.1145/3532836.3536269`) · fuente: blog.yiningkarlli.com/2022/08 **y**
    la propia ficha del paper en ACM Digital Library ✅ (dos fuentes, una es paper citable).
  - Las flores de Isabela y las partículas de luz mágica de la familia **"llevaron los
    contadores de instancing a récords nuevos"** para el estudio · fuente: mismo blog,
    entrada de nov-2021 (blog.yiningkarlli.com/2021/11/encanto.html) ✅.
  - Primera película de Disney Animation con un **pipeline basado en USD**, sucesor del
    pipeline original de Tangled, con una nueva "command center tool" de control de
    producción · misma fuente ✅.
- **Cómo reproducir el look en Blender/Photoshop (guía práctica)**:
  1. **Render**: Cycles con **Subsurface Scattering** en piel y flores, sin ningún
     "Toon Shader" (Encanto no es cel-shading, es fotorrealista estilizado).
  2. **Tela**: en vez de displacement sobre una malla lisa, usar **Hair/Curves de Blender
     4.x tejidas** para chifón/tul/bordados en primeros planos (mismo principio que
     Hyperion "wove as actual curves"); para el resto, un `Principled BSDF` con capa de
     **Sheen** activada (Blender ya tiene un lóbulo de sheen físico desde 4.0, equivalente
     al que Disney desarrolló para esta película) y roughness alto.
  3. **Ojos**: SSS sutil + una capa extra de reflexión especular estrecha para simular la
     "cáustica de iris" (truco simple: un plano curvo con textura de iris y "Glossy" fino
     encima del ojo base).
  4. **Objeto mágico/holograma** (tabletas de Bruno, luces del milagro): en Blender, un
     material de **vidrio (Glass BSDF)** con un **mapa de blend/mask pintado a mano** para
     mezclar entre "vidrio normal" y una textura animada proyectada dentro (Shader Nodes:
     Mix Shader con un "Fac" pintado en textura, más una cámara/objeto de proyección
     escondido detrás como "portal de salida" — no hay una función 1:1 de teletransporte de
     rayos en Cycles, pero el truco de "geometría oculta + proyección" reproduce el
     resultado visual sin necesitar el motor propio de Disney).
  5. **Partículas/instancing** (luciérnagas, pétalos, flores de Isabela): Geometry Nodes
     con distribución sobre curva o superficie + variación de escala/rotación por ruido;
     cuidado con el límite de PC del dueño (regla 9 de `reglas_del_dueno.md`): probar con
     pocas instancias y subir sólo en el render final, nunca en el visor.
  6. **Vestuario**: capas de textura pintada a mano (flores de Isabela, agujeros de rata de
     Bruno) como **máscaras de desgaste** sobre un `Principled BSDF`, no geometría
     adicional — más barato de render y más fácil de ajustar.
  7. **Encuadres y composición**: sin una fuente que documente esto en detalle técnico
     (making-of no entra en planificación de plano por plano) ⚠️; a falta de eso, se
     observa por descripción de crítica especializada (CBR, ScreenRant) que las escenas de
     tensión familiar usan encuadres cerrados y simétricos dentro de la Casita (la propia
     arquitectura como "marco dentro del marco"), mientras las visiones y números musicales
     abren a planos muy amplios y verticales (aprovechando la altura de las montañas/valle)
     — dato de una sola fuente cualitativa, sin medir en fotograma propio (ese trabajo es
     del investigador de vídeo, punto 4/9/10/14) ⚠️.
  - **Modelos/rigs libres de referencia (Sketchfab, licencia indicada, sólo para estudiar
    forma/proporción, nunca para pegar en un render final)**:
    - **"Encanto Casita"** · https://sketchfab.com/3d-models/b66fe8cece3c4c0c87557dc591f5ed22
      · licencia **CC BY-NC-SA** (no comercial) — modelo de fan de la Casita completa, útil
      sólo como referencia de proporción/planta del edificio, **no usar en nada que se
      publique o venda** por la cláusula NC.
    - **"Butterfly" / "Low-poly Butterfly" / "Fantasy Butterfly Animation"** (varios
      resultados, licencia **CC BY** la mayoría) · referencias genéricas de mariposa para
      el motivo central del punto 25 — comprobar cada crédito de autor exacto antes de usar
      cualquiera.
  - **Texturas 2D libres (ligado al punto 19)**: ambientCG (`ambientcg.com`, CC0) tiene
    varias telas lisas que sirven de base neutra para pintar encima bordado a mano —
    `Fabric030`, `Fabric036`, `Fabric061`, `Fabric062`, `Fabric066`, `Fabric081C`,
    `Fabric083` (todas CC0, sin atribución obligatoria) · fuente: `ambientcg.com/api/v2/
    full_json?type=Material&q=fabric` (consulta directa a la API, sin gastar cupo de
    búsqueda) ✅. Para el bordado/patrones de flores en sí (no una tela lisa, sino el
    dibujo de la trama), no se encontró un pincel o textura libre que replique
    específicamente el bordado floral de Isabela o los patrones Quimbaya de Bruno; haría
    falta pintarlo a mano sobre estas telas base ⚠️ **No encontré** un recurso ya hecho.

### Punto 24 — Obras parecidas

- **Coco** (Pixar, 2017) — la comparación obligada y, en este servidor, la **biblia
  gemela**: mismo tipo de encargo (`encargos/57-coco.md`/`58-encanto.md`, "país +
  música", sin canal propio, mismo pedido de proponer canal y lámina), misma estructura de
  familia extendida con un don/talento central. Diferencia de fondo señalada por análisis
  especializados: Coco usa **"Hard Magic"** (reglas de la Tierra de los Muertos explicadas
  paso a paso, con mecánicas casi de videojuego) y Encanto usa **"Soft Magic"** (el
  realismo mágico colombiano, más atmosférico y menos "reglamentado") · fuente: comparación
  educativa cruzada (Genially "Magical Realism and the Fantastic in Coco y Encanto") **y**
  mhbarton.com ("Film Study: Coco vs. Encanto") ✅ (dos fuentes) — relevante para no
  repetir composición de lámina si ambas terminan en canales parecidos del servidor.
- **Vivo** (Sony Pictures Animation, 2021, con canciones de **Lin-Manuel Miranda** — el
  mismo compositor de Encanto, mismo año de estreno) — kinkajú músico que viaja de Cuba a
  Miami; comparte con Encanto el uso de **música original en español/spanglish** y
  elementos de realismo mágico (luces de neón, secuencias oníricas) aplicados a un tono más
  ligero, con temas de duelo y relaciones familiares/de mentor de fondo · fuente: reseñas
  cruzadas de la temporada 2021 (FOX/Rendy Reviews describiendo "más magical realism con
  luces neón y secuencias de sueño") ✅ — dato de una sola cadena de fuentes tipo reseña,
  pero la coincidencia de compositor y año está confirmada en Wikipedia de ambas películas
  ⚠️/✅ mixto (el dato del compositor común sí es ✅ doble fuente).
- **Cien años de soledad** (Gabriel García Márquez) — el propio periodista colombiano
  **Javier Ocaña** (citado en cobertura de prensa) llama a los Madrigal «una versión de
  cuento infantil de los Buendía», la familia protagonista de la novela más famosa del
  realismo mágico latinoamericano; el director/guionista Jared Bush ha reconocido en
  entrevistas que el género de "realismo mágico" colombiano (con García Márquez como
  máximo referente) fue la base conceptual de toda la película · fuente: cobertura de
  prensa especializada (recogida en búsqueda de "Encanto movies similar... magical
  realism") **y** artículos de contexto sobre el desarrollo del guion citando el género
  como punto de partida (thenerdsofcolor.org) ✅ (dos fuentes).
- **Turning Red** (Pixar, 2022) — no confirmado con una fuente directa que compare ambas
  películas entre sí (búsqueda no dedicada a este par específico); se anota igualmente por
  el paralelismo temático evidente (chica adolescente bajo la presión de las expectativas
  familiares/generacionales, protagonista que "avergüenza" involuntariamente a la familia)
  para que el redactor lo valore ⚠️ (relación por criterio propio, no por fuente que las
  compare directamente).
- **TV Tropes**: la página principal (`tvtropes.org/.../WesternAnimation/Encanto`) y sus
  subpáginas de personajes, momentos divertidos/tristes/asombrosos y teorías de fans están
  todas activas y documentadas, buena cantera para el punto 12 del investigador de voz (no
  se explotó el contenido en detalle aquí porque cae fuera de estos 6 puntos) — anotado
  para que el redactor sepa que existe y está viva.

### Punto 25 — El mundo, la historia y sus símbolos

**Las reglas del mundo, en cinco líneas** (✅ dos fuentes: Wikipedia + Disney Wiki vía API,
wikitext de "Miracle Candle" y "Casa Madrigal"):
1. Tras huir de un conflicto armado, **Pedro Madrigal** muere protegiendo a su esposa
   **Alma** y a sus trillizos recién nacidos; el sacrificio de Pedro y el amor de Alma dan
   nacimiento a **el milagro**, encerrado en su **vela de bodas**, que se vuelve la
   **Vela del Milagro**.
2. El milagro crea la **Casita** (sensible, con personalidad propia) y protege al pueblo
   de **Encanto** con montañas alrededor.
3. Cada Madrigal, al cumplir 5 años, recibe un **don** mágico distinto en una **ceremonia
   del don** (una puerta nueva se abre en la Casita con su nombre y su don tallados).
4. La magia se debilita si la familia sufre disfunción emocional acumulada y expectativas
   no habladas; cuando llega al límite, **la Casita se agrieta y la vela se apaga**,
   dejando a todos sin don.
5. La magia sólo se restaura con **reconciliación familiar genuina y apoyo de la
   comunidad**, no con "arreglar" a la persona que "falló": la propia Alma reconoce que sus
   expectativas dañaron a la familia.

**La historia por arcos** (✅ dos fuentes: Wikipedia (resumen extraído por WebFetch,
estructura en 5 actos) + wikitext de Disney Wiki sobre Casa Madrigal/Miracle Candle):
1. **Planteamiento**: 50 años después de la muerte de Pedro, los Madrigal usan sus dones
   para servir al pueblo. **Mirabel**, la única sin don, se siente invisible en su propia
   familia.
2. **Incidente detonante**: la noche de la ceremonia del don de su primo Antonio, Mirabel
   ve que la Casita se agrieta y la vela titila; su familia no le cree.
3. **Investigación**: Mirabel descubre en la torre escondida de su tío **Bruno** (desapa-
   recido "hace 10 años", en realidad viviendo oculto dentro de las paredes) una visión
   rota que podría predecir su propio destino como el fin de la magia.
4. **Punto medio/revelación**: al confrontar a la familia sobre las expectativas que cada
   quien carga en silencio (Luisa con la fuerza, Isabela con la perfección), la tensión
   estalla; la Casita se derrumba por completo y la vela se apaga en las manos de Mirabel:
   la familia se queda sin magia.
5. **Clímax/resolución**: Alma se da cuenta de que su miedo a perder otra vez la familia
   (por el trauma de la muerte de Pedro) es lo que rompió la magia; pide perdón a Mirabel.
   Todo el pueblo ayuda a reconstruir la Casita a mano, sin magia, por amor — y al terminar
   la puerta nueva se abre sola: la magia vuelve, ahora sin la presión del "milagro que hay
   que merecer". Mirabel por fin aparece en el retrato familiar.

**Emblemas, objetos y vocabulario que un fan reconoce al instante** (✅ dos fuentes salvo
donde se indique):
- **La Vela del Milagro** ("Miracle Candle"/"Alma's Candle") — objeto central, siempre
  encendida, "melted and gone out" en el clímax; fuente: Disney Wiki (wikitext, con tuits
  citados del guionista Jared Bush sobre su origen) ✅.
- **La Casita** ("Casa Madrigal") — casa viva de tres pisos alrededor de un patio sin
  techo, cada puerta de dormitorio tallada con el nombre y el don de quien vive dentro,
  iluminada con un brillo dorado; la puerta principal, tras la reconstrucción, tiene
  tallada a **toda** la familia junta (incluida Mirabel) — antes de eso, ella era la única
  sin representación en la casa ✅.
- **Las mariposas** — motivo visual recurrente: la vela lleva grabada una mariposa; el
  pelo de la joven Alma llevaba lazos con forma de mariposa; las mariposas amarillas en la
  visión de Bruno y en el abrazo final de Alma y Mirabel simbolizan un buen augurio; la
  propia Casita integra mariposas en su diseño arquitectónico — lectura repetida en varias
  fuentes: **transformación, esperanza y el "capullo protector"** que es la familia ✅
  (ScreenRant + análisis cruzado de simbolismo).
- **Dos Oruguitas** — canción central (interpretada por **Sebastián Yatra**, escrita por
  **Lin-Manuel Miranda**, nominada al Óscar a Mejor Canción Original 2022): dos orugas
  enamoradas que deben soltarse para poder transformarse, metáfora explícita de Pedro y
  Alma teniendo que "hacer espacio" para que llegara el milagro — la propia oruga es el
  símbolo de transformación que antecede a la mariposa · cita de Miranda: *"that to me
  felt like a delicious metaphor for what the entire family is going through"* · fuente:
  Songfacts/Salon (cita directa de Miranda) **y** Wikipedia de la canción ✅.
- **El mochila y la ruana** — prendas colombianas reales que la película usa como vestuario
  (Mirabel lleva mochila al viajar; Bruno, la ruana verde esmeralda) y que **Disney
  Dreamlight Valley** reutiliza como ropa desbloqueable ("Teal Dreamlore Ruana") — puente
  directo entre la cultura real y el merchandising/videojuegos ✅.
- **"No se habla de Bruno"** — la frase-lema de toda la familia (título real de la canción
  más popular de la BSO); Bruno la cita de sí mismo en su propia ficha de Disney Heroes
  ("Bruno makes bad things happen") como autoparodia — vocabulario que cualquier fan
  reconoce al instante, incluso fuera de contexto de la película ✅ (canción confirmada en
  Wikipedia del soundtrack + auto-cita en el propio videojuego).
- **La palabra "Encanto" como símbolo en sí misma**: no es sólo el nombre del pueblo — en
  español significa literalmente un sitio "hechizado/bendecido espiritualmente", y la
  Wikipedia en inglés lo señala como el término que resume la filosofía estética de toda
  la película (dónde "magic and reality merge") ✅.
- **Geografía real detrás de la ficción**: aunque Encanto (el pueblo) es ficticio, está
  inspirado directamente en los lugares del viaje de investigación de 2018 — el **Valle de
  Cocora** (con sus palmas de cera, el árbol nacional de Colombia) y los pueblos coloniales
  de **Barichara** y **Salento** son las referencias arquitectónicas y paisajísticas más
  citadas ✅ (SIGGRAPH blog + prensa del viaje).

## Lo mejor para la lámina

- **El objeto real más fuerte para Blender**: la **Vela del Milagro** — un objeto pequeño,
  se puede modelar y renderizar con detalle (cera derretida, mariposa grabada, llama que
  titila) y es EL símbolo de toda la película; alternativa igual de icónica: una **puerta
  tallada de la Casita** con nombre y don grabados, iluminada por dentro.
- **Cuadro de diálogo temático ya verificado**: nada de burbuja blanca — usar una caja tipo
  "cita bajo retrato" con comillas grandes (como hace Disney Heroes: Battle Mode con cada
  Madrigal) enmarcada en madera tallada con motivos florales/mariposa, o una "tableta de
  esmeralda" traslúcida como las visiones de Bruno si el canal es de contenido "revelador"
  (spoilers, anuncios).
- **Tipografía lista para usar**: título en **Yeseva One** (libre, contraste grueso/fino
  parecido al lettering oficial) o la fuente fan **Madrigal** de NubeFonts (comprobada con
  fontTools, juego de tildes/ñ/¿/¡ completo, pero licencia confusa — enlazarla siempre);
  para texto largo, **Open Sans** con borde negro fino como los subtítulos oficiales.
- **El personaje/objeto más "fresco" para no parecer genérico**: Mirabel llegó a Disney
  Speedstorm apenas el **30-jul-2026**, con su propia actriz de voz (Stephanie Beatriz) —
  dato utilizable casi en tiempo real, nadie va a pensar "esto es viejo".
- **Vocabulario/decoración con capas reales**: mariposas + Vela del Milagro + puertas
  talladas + mochila/ruana bordada dan profundidad sin caer en cliché plano; el verde
  esmeralda de Bruno es un acento de color con significado cultural real (comercio de
  esmeraldas colombiano), no un capricho estético.

## No encontré

- **Ficha tipográfica oficial del logo/título** de Encanto: es lettering custom sin fuente
  comercial publicada. Buscado: «Encanto Disney movie logo font identify dafont forum»
  (inglés), foros de DaFont citados en los resultados. Se resolvió con la fuente fan
  "Madrigal" (comprobada con fontTools) y alternativas OFL, no con la fuente oficial en sí.
- **Páginas interiores del cómic "The New Adventures of Encanto"** (Papercutz, jul-2024)
  para comparar el letrado de grito/pensamiento/onomatopeya: sin "look inside" público
  accesible (libro muy reciente). Buscado: catálogo de Amazon/Walmart/Biblio sin vista de
  interior. ⚠️
- **Fuente de subtítulos/créditos oficiales** de Disney+/Blu-ray para Encanto: sin ficha
  técnica pública, igual que en el resto de biblias de Disney del servidor. Buscado:
  «Encanto Disney movie town sign lettering title card font style» (inglés), sin resultado
  específico de tipo. ⚠️
- **Confirmación independiente de Disney Sorcerer's Arena** con contenido de Encanto: sólo
  una fuente (ficha de Disney Wiki), sin poder entrar a la wiki propia del juego (dominio
  no localizado) ni una segunda fuente que lo confirme. Buscado: «"Disney Sorcerer's Arena"
  Encanto Mirabel Isabela character», «"Disney Sorcerer's Arena" Encanto Casita». ⚠️
- **Pincel o textura 2D libre que replique el bordado floral de Isabela o los patrones
  Quimbaya de la ruana de Bruno** (no una tela lisa, sino el dibujo del patrón en sí):
  búsqueda hecha en ambientCG (sólo telas lisas CC0, sin bordado) y en la propia búsqueda
  web de "Encanto embroidery pattern free texture brush", sin un recurso ya hecho y libre.
  Habría que pintarlo a mano. ⚠️
- **Detalle técnico completo de la charla SIGGRAPH 2022 "Encanto - Let's Talk About Bruno's
  Visions"**: sólo el resumen/abstract y el blog del propio autor son públicos, la sesión
  completa no está accesible sin acceso a SIGGRAPH. ⚠️ (mismo patrón que con los papers de
  Coco en la biblia gemela).
- **Encuadres y composición por plano medidos directamente**: no es tarea de este rol
  (corresponde al investigador de vídeo, puntos 4/9/10/14); aquí sólo se documentó lo que
  dicen fuentes de crítica especializada, sin medir fotograma propio. ⚠️

## Bitácora

Punto de partida: `partes/datos-texto.md` (recolectado por `recolectar.py`) — sólo traía
dos capturas de Steam de juegos sin relación con la película (una colección de personajes
de Dead or Alive 6 y un DLC "Rural" de "Buena Pizza, Gran Pizza", ambos llamados "Encanto"
por coincidencia). Descartados, no se repitió esa búsqueda.

**Consultas directas a APIs/curl (sin gastar cupo de WebSearch)**:
- `disney.fandom.com/api.php` (wikitext): Encanto (infobox de la película, créditos),
  Papercutz (lista de cómics, «The New Adventures of Encanto»), Casa Madrigal (infobox de
  ubicación, lista de juegos donde aparece), Miracle Candle (origen, tuits citados de Jared
  Bush), búsqueda de texto `srsearch=Encanto comic` y `srsearch=Encanto miracle gift
  ceremony`.
- `logos.fandom.com/api.php` (wikitext + imageinfo): ficha y tamaño real del logo oficial
  (`Disney_Encanto.svg`, 1000×423, 26,7 KB).
- `dmk.fandom.com/api.php`: búsqueda `srsearch=Encanto` (10 páginas del evento 2023) y
  wikitext completo de «Encanto Event 2023».
- `speedstorm.fandom.com/api.php`: búsqueda `srsearch=Mirabel`, wikitext de «Mirabel»,
  `list=categorymembers&cmtitle=Category:Encanto` (Isabela, Luisa, Mirabel).
- `disneyheroesbattlemode.fandom.com/api.php`: wikitext de Mirabel, Isabela, Bruno y Luisa
  Madrigal (habilidades, citas de presentación).
- `disneydreamlightvalley.fandom.com/api.php` (dominio correcto tras probar 4 alternativas
  que dieron 404): búsqueda `srsearch=Encanto`, wikitext de «Mirabel» (versión, recompensas
  de amistad, ropa).
- `disneysolitaire.fandom.com/api.php`: wikitext de «Encanto» (set de stickers, fechas).
- `disneyemojiblitz.fandom.com/api.php`: búsqueda `srsearch=Encanto`, wikitext de
  «Mirabel» (habilidad, expresiones).
- `tcrf.net/api.php`: da 403 (Cloudflare, igual que en la nota de AYUDANTE.md sobre Game UI
  Database); confirmado en su lugar por WebSearch `site:tcrf.net Encanto`.
- `1001fonts.com/download/madrigal.zip` + `api.fontsource.org/v1/fonts` + descarga directa
  de `cdn.jsdelivr.net/fontsource/fonts/.../latin-400-normal.ttf` para Yeseva One, Berkshire
  Swash y Pacifico — las 4 comprobadas con **fontTools** (`getBestCmap`) para á é í ó ú Á É
  Í Ó Ú ñ Ñ ¿ ¡. Nota técnica encontrada en el proceso: el archivo del subset "latin-ext"
  de Fontsource NO trae estos caracteres (están en "latin"/Latin-1 Supplement); hay que
  pedir siempre `latin-400-normal.ttf`, no `latin-ext-…`.
- `api.sketchfab.com/v3/search`: «encanto casita» (1 resultado, CC BY-NC-SA), «colombian
  ruana poncho» (sin resultado directo de Encanto), «butterfly low poly» (varios CC BY).
- `ambientcg.com/api/v2/full_json?type=Material&q=fabric`: 7 texturas de tela CC0.

**Búsquedas web (WebSearch), todas en inglés salvo que se indique**:
1. "The New Adventures of Encanto" Papercutz "Time to Shine" graphic novel release
2. Encanto Disney movie logo font identify dafont forum
3. "The Art of Encanto" book Lorelay Bové production designer interview
4. Encanto Disney Colombian cultural consultants research trip Colombia
5. Encanto Disney Animation Hyperion renderer magic visual effects making of
6. Encanto costume designer ruana embroidery Wayuu mochila pattern design
7. Encanto symbolism candle miracle casita butterflies meaning analysis
8. Encanto movies similar to Vivo Coco comparison magical realism Latin America
9. Encanto TV Tropes page
10. Encanto Disney Little Golden Book storybook novelization junior
11. "Colombian Cultural Trust" Encanto consultants names Rendon Osma Espinosa
12. Encanto costume design lead ruana "Neysa" OR "costume designer" Bruno poncho interview
13. Encanto costume designer character designer credits "art director" Walt Disney
    Animation Studios
14. Vivo 2021 movie Colombia Coco Encanto magical realism comparison animated
15. Encanto movie town sign lettering "Welcome to Encanto" title card font style
16. site:tcrf.net Encanto
17. Kingdom Hearts Encanto world Mirabel confirmed
18. "NubeFonts" Madrigal font download license free
19. "Disney Sorcerer's Arena" Encanto Mirabel Isabela character
20. "Disney Solitaire" Encanto Mirabel event cards
21. "Disney Sorcerer's Arena" Encanto Casita "Disney POP TOWN" Encanto
22. "Dos Oruguitas" Encanto song meaning caterpillars symbolism Oscar
23. Encanto Isabela embroidered skirt flowers texture design pattern character

**Fetch directo (WebFetch, contenido primario resumido con modelo local, no de memoria)**:
- `en.wikipedia.org/wiki/Bruno_Madrigal` (diseño de la ruana, consultores, actor de voz)
- `en.wikipedia.org/wiki/Encanto` (arcos de la trama, reglas del mundo, vocabulario)
- `blog.yiningkarlli.com/2022/08/encanto-brunos-visions.html` (shader de teletransporte,
  SIGGRAPH 2022, fuente primaria de un ingeniero de Disney Animation)
- `blog.yiningkarlli.com/2021/11/encanto.html` (sheen BSDF, ojos, telas como curvas, USD
  pipeline, fuente primaria)

Sigue: nada obligatorio pendiente de los puntos 5, 6, 11, 18, 24 y 25 — todo lo exigido por
`ENCARGO.md` quedó cubierto (con ⚠️ donde sólo hay una fuente o no se encontró, nunca en
blanco). Si el redactor necesita más profundidad en algún punto concreto, que lo pida por
`SendMessage` con el número de punto.
