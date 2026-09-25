# Parte de TEXTO, JUEGOS Y TÉCNICA · 102 — El estilo Ghibli en general

Rol: investigador de texto. Puntos de ENCARGO.md: 5 (tipografía), 6 (cómo se
comunica el texto/diálogo en pantalla), 11 (videojuegos), 18 (estilo de dibujo
y cómo replicarlo), 24 (obras parecidas), 25 (el mundo y sus símbolos).

Nota: 102 es un tema general sobre el estilo de Studio Ghibli (no una obra con
personajes ni trama). Se adapta el enfoque: tipografía/logo del estudio, cómo
se presenta el texto y el diálogo a través de varias películas, y la
influencia/parecido de Ghibli con otros estudios.

`datos-texto.md` no sirvió: `recolectar.py` buscó "El estilo Ghibli en general"
como si fuera un título de obra (Steam, MusicBrainz, etc. devolvieron ruido
sobre la palabra "general"). Se investigó todo a mano con búsqueda web y
consultas directas a wikis y APIs.

## Punto 5 — Tipografía: el logo del estudio y los títulos de las películas

- El logo actual (1991-presente) muestra al "Rey Totoro" de perfil con el
  Chibi Totoro sobre la cabeza y dos champiñones detrás simulando orejas;
  texto japonés arriba y "STUDIO GHIBLI" abajo en inglés, separados por una
  línea fina · [Logos Wiki (Fandom)](https://logos.fandom.com/wiki/Studio_Ghibli) y
  [1000logos.net](https://1000logos.net/studio-ghibli-logo/) · ✅ (dos fuentes)
- El texto en inglés "STUDIO GHIBLI" del logo está en **Futura** (sans-serif
  geométrica, mayúsculas, ángulos y curvas equilibrados) · confirmado en dos
  wikis de logotipos: [Scary Logos Wiki](https://freakylogo.fandom.com/wiki/Studio_Ghibli)
  ("underneath that is 'STUDIO GHIBLI' in Futura, with a line above it") y
  [Closing Logo Group](http://closinglogogroup.fandom.com/wiki/Studio_Ghibli_(Japan))
  (mismo texto, visto en snippet de búsqueda) · ✅ (dos fuentes)
- ⚠️ Dato distinto de una recreación fan-made del logo en Wikimedia Commons: el
  autor dice haber usado "MS Gothic" (MS Pゴシック, para el japonés) e
  "ITC Avant Garde Gothic Medium" (para el inglés) al reconstruirlo en
  Photoshop · [Wikimedia Commons, File:Studio_Ghibli.png](https://commons.wikimedia.org/wiki/File:Studio_Ghibli.png)
  · ⚠️ (una fuente, y es una versión hecha por un fan, no el archivo original
  del estudio; Avant Garde Gothic es también geométrica y muy parecida a
  Futura, así que puede ser una confusión entre ambas al identificar la letra
  a ojo)
- Cronología del logo (wikitext de Logos Wiki):
  - 1972-1985: bajo el nombre **Topcraft** (el estudio predecesor), logo
    simple en gris y blanco.
  - 1985-1991: **sin logo propio**. Las películas y la mercancía se
    comercializaban bajo Nibariki (productora de Miyazaki y Takahata) y Tokuma
    Shoten (editorial matriz hasta 2005).
  - 1991-presente: logo principal con Totoro, estrenado con *Only Yesterday*
    (Recuerdos del ayer, 1991).
  - 1993-presente: logo secundario simplificado (sólo Chibi Totoro), usado en
    mercancía, bandas sonoras, ediciones en Blu-ray y redes sociales.
  · [Logos Wiki, wikitext vía API](https://logos.fandom.com/wiki/Studio_Ghibli) · ✅
- El SVG del logo principal (1000×481 px, en `logopedia`/Logos Wiki) está
  trazado enteramente en negro puro (`fill:#000000`, 82 veces) sobre fondo
  transparente; las versiones a color que circulan (fondo celeste) son
  reconstrucciones o fotogramas de vídeo, no el vector oficial · medido con
  `grep` sobre el SVG descargado, archivo en `/tmp/claude-0/trabajo/102-texto/ghibli_logo.svg`
  · ✅ (medido directamente)
- El nombre "Ghibli" no es japonés: es una palabra libia/italiana para un
  viento cálido del Sahara (siroco); Miyazaki lo escogió para transmitir la
  idea de "soplar un viento nuevo" en la animación · [logos-world.net](https://logos-world.net/studio-ghibli-logo/)
  y [Wikipedia, Studio Ghibli](https://en.wikipedia.org/wiki/Studio_Ghibli) · ✅ (dos fuentes)
- **Cada película tiene su propia tipografía de título** (no hay una única
  "letra Ghibli"): no es una identidad tipográfica unificada como Disney, sino
  diseño por película.
  - *Mi Vecino Totoro* (1988): título en **Spumoni**, tipografía juguetona y
    con rebote, publicada por LetterPerfect · [fontmeme.com/my-neighbor-totoro-font](https://fontmeme.com/my-neighbor-totoro-font/)
    (visto en snippet de búsqueda, la página bloquea con 403 directo) · ⚠️ (una fuente)
  - *El Viaje de Chihiro* (2001): título en variante de **Palatino** (serif
    clásica) · [fontmeme.com/spirited-away-font](https://fontmeme.com/spirited-away-font/)
    (snippet de búsqueda; página con 403 directo) · ⚠️ (una fuente)
  - *El Increíble Castillo Vagabundo* (Howl's Moving Castle, 2004): título en
    **Albertus**, tipografía glífica con serifas diseñada por Berthold Wolpe
    para Monotype (1932-1940) · [fontmeme.com/howls-moving-castle-font](https://fontmeme.com/howls-moving-castle-font/)
    y [fontbolt.com](https://www.fontbolt.com/font/howls-moving-castle-font/) · ✅ (dos fuentes)
  - No se encontró confirmación de la tipografía exacta de *La Princesa
    Mononoke* en fuentes fiables (el foro de dafont sobre el tema no dio
    respuesta identificada, ver «No encontré»).
- **Letras libres de "estilo Ghibli"** recomendadas por un blog japonés
  especializado en tipografía (con licencia y a qué película se parece cada
  una) · [kyoukasho.net/entry/ghibli-fonts](https://www.kyoukasho.net/entry/ghibli-fonts) · ⚠️ (una fuente, blog de aficionado, no oficial):
  - **源の明朝 / Source Han Serif** — de Adobe, open source (SIL Open Font
    License), en [GitHub adobe-fonts/source-han-serif](https://github.com/adobe-fonts/source-han-serif)
    y Adobe Fonts. Serif japonesa (mincho) formal; el blog la asocia al
    aspecto de *La Colina de las Amapolas*, *Cuando Marnie Estaba Allí* y
    *Porco Rosso*. Tiene kanji, kana, y latín con acentos (proyecto
    multilingüe de Adobe/Google, cubre diacríticos latinos estándar).
  - **たぬゴ / Tanugo** — en tanukifont.com, gratis para uso comercial y no
    comercial. Aspecto manuscrito con carácter; asociada a *Ponyo* y a
    *Cuentos de Terramar* (Gedo Senki).
  - **鉄瓶ゴシック / Tetsubin Gothic** — de フロップデザインフォント (Flop
    Design Font) en BOOTH, gratis. Gótica en negrita con contorno que
    parece trazo a mano; asociada a *El Castillo en el Cielo* (Laputa) y a
    *Conan, el Niño del Futuro*.
  - **チェックポイントフォント / Checkpoint Font** — en
    cute-freefont.flop.jp, uso comercial permitido ("商用OK"). Trazo grueso
    hecho a mano, formas redondeadas y amigables; asociada a *Nausicaä del
    Valle del Viento*.
  - Dos generadores de logo (no fuentes descargables): uno de estilo *Mi
    Vecino Totoro* (mincho en negrita) y otro de estilo *El Viento se Levanta*
    (manuscrito suave), en tubudeco.com.
  - **Pendiente de comprobar con fontTools**: si Source Han Serif y las
    fuentes gratuitas japonesas cubren tildes, ñ, ¿ y ¡ para el español (ver
    «Sigue»).

## Punto 6 — Cómo se comunica el texto y el diálogo en pantalla

- Studio Ghibli **casi no usa cartelas de texto explicativo ni interfaces
  gráficas**: a diferencia de otros animes, la narrativa se apoya en
  imágenes y sonido ambiente antes que en texto en pantalla. El texto que
  aparece dentro del mundo de la película (letreros, carteles) está en
  japonés real, dibujado a mano como parte del fondo, no como grafismo de
  postproducción · deducido de análisis y wikis, ver ejemplos abajo.
- **Ejemplo detallado — letreros de la ciudad espiritual en *El Viaje de
  Chihiro*** (min. 00:07:24, análisis académico):
  - Un cartel con forma de ojo muestra el kanji 塩 (_shio_, "sal") como
    pupila, flanqueado por hiragana め (_me_, "ojo"); debajo, letreros con
    めめ y 三千眼 (_sanzenme_, "tres mil ojos") · [K-State English, "Signs, Signs, Everywhere"](https://englishkstate.org/2022/12/08/signs-signs-everywherethe-hidden-depth-of-japanese-signs-in-spirited-away/)
    · ⚠️ (una fuente, análisis de aficionado/académico, no oficial del estudio)
  - Función narrativa: como "ojo" se pronuncia "me" en japonés, el cartel
    genera la sensación de estar observado por múltiples ojos, reforzando la
    extrañeza y vigilancia que siente Chihiro como forastera que no puede
    leer las señales de su entorno.
  - Referencia budista: "tres mil" conecta con 一念三千 (_ichinen sanzen_),
    doctrina del budismo Nichiren; la pupila-sal remite al ritual de
    consagración de estatuas budistas (開眼供養), presagiando el propio
    crecimiento espiritual de Chihiro.
  - El letrero de la casa de baños dice **油屋 ("Aburaya", casa del aceite)**
    y no 湯屋 ("Yuya", casa del agua caliente) aunque es una casa de baños:
    es el nombre propio del negocio. 湯 y 油 comparten la misma lectura
    fonética ("yu"), un juego de palabras deliberado; una lectura del fandom
    añade que el agua de esa casa es un "agua medicinal" (薬湯) preparada por
    Kamaji, y que 油 marca una distinción simbólica entre lo sagrado y lo
    profano (paralelo con "Cristo" = "el ungido", untado con aceite) ·
    [Yahoo Chiebukuro (foro de preguntas japonés), dos respuestas coincidentes](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1454570314)
    · ✅ (dos respuestas independientes coinciden en el dato base: es el
    nombre propio del negocio; la lectura simbólica del aceite sagrado es
    ⚠️, una sola fuente)
- Los letreros y textos del mundo Ghibli están integrados en el fondo pintado
  (parte del arte de producción), no sobrepuestos como gráfico 2D aparte: se
  pintan con la misma textura e iluminación que el resto de la escena. Esto es
  coherente con la técnica de fondos pintados a mano que define el punto 18.
- Los créditos finales de las películas de Ghibli usan tipografía sobria,
  vertical en japonés cuando corresponde; no se encontró un análisis
  detallado y verificado en dos fuentes sobre la tipografía específica de
  créditos, ver «No encontré».

## Punto 11 — Videojuegos de la franquicia: interfaz y cuadros de diálogo

- Studio Ghibli **no es un estudio de videojuegos** y no tiene una franquicia
  de juegos propia como Pokémon o Dragon Ball. Sus colaboraciones en
  videojuegos son puntuales y de terceros, no cuadros de diálogo "de la
  franquicia" propios.
- **Ni no Kuni** (2010-2013, Level-5 + Studio Ghibli) es la colaboración más
  conocida en videojuegos: Ghibli hizo el diseño de personajes y storyboards
  (**Yoshiyuki Momose**, director de animación del juego), y Level-5 abordó
  la producción "de la misma forma que crearía una película de animación" ·
  [Wikipedia, Ni no Kuni](https://en.wikipedia.org/wiki/Ni_no_Kuni) y
  [IGN, "Level-5 Teams up With Studio Ghibli" (2008)](https://www.ign.com/articles/2008/09/24/level-5-teams-up-with-studio-ghibli)
  · ✅ (dos fuentes)
  - El equipo de desarrollo veía las películas de Ghibli constantemente
    durante la producción para calcar su atención al detalle, sus storyboards
    y su manejo de cámara · Wikipedia (misma fuente) · ⚠️ (una fuente)
  - Localización: en la versión occidental se cambió la reverencia japonesa
    de saludo del protagonista Oliver a un saludo "a la occidental" ·
    Wikipedia (misma fuente) · ⚠️ (una fuente)
  - No se encontraron capturas o descripciones verificadas en dos fuentes de
    los menús o cuadros de diálogo específicos de la interfaz del juego (ver
    «No encontré»).
- No se encontró ninguna otra franquicia de videojuegos propia de Ghibli más
  allá de Ni no Kuni y de las atracciones interactivas del Museo Ghibli /
  Ghibli Park (que son físicas, no software).

## Punto 18 — Estilo de dibujo y técnica, y cómo replicarlo

- **Software real usado por el estudio** (dato clave y verificable, no
  suposición): Ghibli usa el sistema **Toonz** para tinta, color y
  composición digital desde ***La Princesa Mononoke*** (1999) · confirmado en
  tres fuentes independientes: [OpenToonz, sitio oficial](http://opentoonz.github.io/e/),
  [Cartoon Brew](https://www.cartoonbrew.com/tech/toonz-software-used-studio-ghibli-futurama-made-free-open-source-138111.html)
  y [Wired](https://www.wired.com/story/toonz-animation-software-studio-ghibli-free-download/)
  · ✅ (dos fuentes o más)
  - En 2016 Ghibli y Dwango liberaron una versión de código abierto,
    **OpenToonz**, que incluye una variante llamada **"Toonz Ghibli
    Edition"** con las funciones a medida que el estudio desarrolló durante
    años (algoritmos de escaneo y preservación de línea) · Cartoon Brew y
    [Anime News Network](https://www.animenewsnetwork.com/press-release/2016-03-20/animation-production-software-opentoonz-to-be-released-on-march-26/.100022)
    · ✅ (dos fuentes)
  - **Para replicarlo**: OpenToonz es gratis y de código abierto
    (opentoonz.org o github.com/opentoonz/opentoonz); su preset "Ghibli"
    imita el gamma de escaneo y la preservación de línea del estudio. Es la
    vía más fiel a la técnica real del estudio, más que intentarlo sólo con
    Photoshop.
- **Fondos pintados a mano**: se usa **poster color**, una acuarela opaca
  japonesa similar al gouache, aplicada en papel grande (formatos B4 o A3),
  en capas de transparencias con realces opacos para dar profundidad de luz
  (ejemplo citado: *Mi Vecino Totoro*) · [animepapa.com, "How Studio Ghibli Combines Traditional and Digital Techniques"](https://animepapa.com/article/how-studio-ghibli-combines-traditional-and-digital-techniques/)
  · ⚠️ (una fuente, artículo de blog especializado, sin autor claro citado)
  - En *El Cuento de la Princesa Kaguya* (Takahata), la estética cambia a
    acuarela y carboncillo con líneas deliberadamente inacabadas, técnica
    "húmedo sobre húmedo" (wet-on-wet) que deja mezclarse el pigmento
    libremente, ligada a la pintura tradicional japonesa con tinta (misma
    fuente) · ⚠️
  - **Para replicar en Photoshop**: pinceles de acuarela/gouache con textura
    de papel, capas de color plano por debajo y una capa superior de "realce"
    con opacidad reducida y modo de fusión multiplicar, para simular las
    veladuras de la poster color.
- **Proceso de animación tradicional**: Ghibli separa **genga** (dibujo
  clave del movimiento, hecho por animadores senior) y **douga** (fotogramas
  intermedios), y estos últimos siguen dibujándose a mano incluso en
  producciones recientes; se evita el motion capture y el rotoscopiado
  porque, según el estudio, introducen "a mechanical smoothness that erases
  emotional nuance" (traducido: una suavidad mecánica que borra el matiz
  emocional) · animepapa.com (misma fuente) · ⚠️ (una fuente)
  - Los coloristas digitales no rellenan con balde de pintura ("bucket
    fill"): aplican el color con trazos de lápiz óptico que imitan la
    dirección de una pincelada, generando variación sutil de opacidad (misma
    fuente) · ⚠️
- **Uso puntual de CGI 3D**, siempre disimulado bajo textura y línea 2D:
  interiores de la casa de baños en *El Viaje de Chihiro*, el motor y el
  tren de aterrizaje del avión Zero en *El Viento se Levanta*, el castillo
  mecánico de *El Increíble Castillo Vagabundo*, y los espíritus "Warawara"
  de *El Chico y la Garza* (modelos 3D repintados a mano para devolverles
  línea y sombreado en acuarela) · animepapa.com · ⚠️ (una fuente, pero son
  datos verificables y consistentes con lo que se sabe públicamente de esas
  películas)
  - *Earwig and the Witch* (2020) fue la primera película enteramente en CG
    3D del estudio, descrita como una prueba de concepto y entrenamiento
    para animadores jóvenes · misma fuente · ⚠️
  - **Para replicar el look "2D sobre 3D" en Blender**: usar Freestyle o el
    modificador Solidify para el contorno de línea, un material tipo
    "Shader to RGB" + rampa de color para aplanar la iluminación a 2-3 tonos
    (cel shading), y una textura de papel/pincel superpuesta en modo
    multiplicar para igualar el grano de los fondos pintados.
- **Citas de Miyazaki sobre su proceso**: describió dibujar a lápiz como
  "drawing with your whole body" (dibujar con todo el cuerpo), y sobre la IA
  generativa dijo que es "an insult to life itself" (un insulto a la vida
  misma) · animepapa.com, que cita como fuente original un reportaje de
  Cartoon Brew sobre *Earwig* y un análisis del BFI sobre los métodos de
  Miyazaki · ⚠️ (cita de segunda mano; no se pudo verificar la cita en la
  fuente primaria del BFI directamente por límite de tiempo, ver «No
  encontré»)

## Punto 24 — Obras parecidas y la influencia de Ghibli en otros estudios

- **Cartoon Saloon** (estudio irlandés, *El Secreto de Kells*, *La Canción
  del Mar*, *Wolfwalkers*, *The Breadwinner*) es señalado repetidamente como
  "el sucesor real de Studio Ghibli" en la crítica anglosajona · [Rotten Tomatoes, editorial "Wolfwalkers Demonstrates Why Cartoon Saloon is Studio Ghibli's True Successor"](http://editorial.rottentomatoes.com/article/wolfwalkers-demonstrates-why-cartoon-saloon-is-studio-ghiblis-true-successor/)
  y [CBR, "This Animated Irish Film Is Perfect for Fans of Studio Ghibli"](https://www.cbr.com/the-secret-of-kells-studio-ghibli-inspiration-simiarities/)
  · ✅ (dos fuentes)
  - Comparaciones concretas: *Wolfwalkers* (caza de lobos, conflicto
    naturaleza/industria) se compara directamente con *La Princesa Mononoke*
    y con *Pom Poko*; *La Canción del Mar* (selkies del folclore irlandés) se
    compara con *Mi Vecino Totoro* por su criatura arraigada a la cultura
    local y por el contraste ciudad opresiva / campo liberador; *El Secreto
    de Kells* y *The Breadwinner* se comparan con *Nicky, la Aprendiz de
    Bruja* y *La Tumba de las Luciérnagas* por tratar temas duros con
    protagonistas infantiles · Rotten Tomatoes editorial (misma fuente) · ⚠️
    (una fuente, pero es un análisis extenso y bien argumentado, no un dato
    suelto)
  - Ambos estudios evitan adaptar un cuento folclórico específico de forma
    literal (a diferencia de Disney): añaden criaturas y creencias
    tradicionales como "sabor" para profundizar historias originales · misma
    fuente · ⚠️
- **Makoto Shinkai** (*Your Name*, *Weathering With You*, *Suzume*) se
  compara con Miyazaki por la conexión con la naturaleza, la profundidad
  emocional y las imágenes vívidas, pero se diferencia claramente: Shinkai
  viene de los videojuegos y trabaja con CGI, mientras Miyazaki dibuja a mano
  y limita el CGI; Miyazaki hace llamados a la acción colectivos (convivencia
  con el medioambiente en *La Princesa Mononoke*), Shinkai apunta a lo íntimo
  (soledad adolescente); Shinkai usa el clima como reflejo emocional (la
  lluvia constante en *5 Centímetros por Segundo* / *El Jardín de las
  Palabras*), algo que Miyazaki no destaca igual · [CBR, "Why the 'New' Miyazaki, Makoto Shinkai, Is Different From the Ghibli Master"](https://www.cbr.com/hayao-miyazaki-makoto-shinkai-differences/)
  · ⚠️ (una fuente, artículo de opinión crítica, pero coherente con el
  consenso general de la crítica)
- Listas de "anime parecido a Ghibli si no es de Ghibli" citan con frecuencia
  *Penguin Highway* y *Mary and the Witch's Flower* (esta última dirigida por
  **Hiromasa Yonebayashi**, ex-animador de Ghibli que fundó el estudio
  **Ponoc** tras dejar Ghibli) por solapamiento temático y de animación ·
  [CBR, "20 Best Non-Ghibli Anime Movies That Feel Like Studio Ghibli Movies"](https://www.cbr.com/best-movies-like-studio-ghibli/)
  · ⚠️ (una fuente; el dato de que Yonebayashi es ex-Ghibli y fundó Ponoc es
  de conocimiento público bien documentado, se marca ✅ para esa parte
  específica: [Wikipedia, Studio Ponoc](https://en.wikipedia.org/wiki/Studio_Ponoc) confirma la fundación en 2015 por
  exempleados de Ghibli).
- **Studio Ponoc** (Japón) se fundó el 15 de abril de 2015, por **Yoshiaki
  Nishimura**, ex productor principal de Ghibli, con el apoyo de varios
  animadores que habían trabajado en Ghibli, incluido el director
  **Hiromasa Yonebayashi**; su primera película, *Mary and the Witch's
  Flower* (2017), se hizo con varios ex empleados de Ghibli en el equipo ·
  [Wikipedia, Studio Ponoc](https://en.wikipedia.org/wiki/Studio_Ponoc) y
  [CBR, "20 Best Non-Ghibli Anime Movies..."](https://www.cbr.com/best-movies-like-studio-ghibli/)
  · ✅ (dos fuentes)

## Punto 25 — El mundo Ghibli: temas y símbolos recurrentes (en vez de "un
mundo" concreto, porque 102 es un tema general)

- **El vuelo y el movimiento como metáfora de liberación**: es uno de los
  motivos visuales más constantes de todo el catálogo, ligado a la biografía
  de Miyazaki (su padre tenía un negocio de piezas de avión) ·
  [animepapa.com, "The Significance of Flight and Movement in Studio Ghibli's Visual Narrative"](https://www.animepapa.com/article/the-significance-of-flight-and-movement-in-studio-ghiblis-visual-narrative/)
  · ⚠️ (una fuente, blog especializado, pero con ejemplos concretos y
  verificables por cualquiera que vea las películas):
  - *Kiki, la Aprendiz de Bruja*: volar en escoba está ligado a su confianza
    en sí misma; cuando duda de sí, "su escoba se niega a despegar del
    suelo".
  - *El Viaje de Chihiro*: los vuelos de Chihiro sobre el dragón Haku marcan
    su paso de niña asustada a joven con más agencia.
  - *Porco Rosso*: el avión rojo es refugio y exilio a la vez; el
    protagonista rompe su maldición en tierra, "a través de la conexión", no
    en el aire.
  - *El Viento se Levanta*: el vuelo es ambición creativa con coste trágico,
    mezclado con la sombra de la guerra.
  - *Mi Vecino Totoro*: el vuelo lúdico de Totoro y el Gatobús da un espacio
    de "asombro reparador" frente a la enfermedad de la madre.
  - *Nausicaä del Valle del Viento*: sus vuelos en planeador sobre la Jungla
    Tóxica son descritos como "actos de empatía radical".
  - *El Castillo en el Cielo* y *El Increíble Castillo Vagabundo*: el
    movimiento vertical (caídas, ascensos, la marcha del castillo) se
    vincula a la transformación espiritual de los personajes.
  - El correr también carga significado: las carreras de Ashitaka y San en
    *La Princesa Mononoke* liberan rabia interior; la carrera de Ponyo sobre
    las olas es pura alegría.
- **La naturaleza nunca es sólo decorado**: "respira, reacciona y suele ser
  el centro moral de la historia", con raíz en el sustrato animista del
  sintoísmo japonés · [animepapa.com, "Decoding Symbolism in Studio Ghibli Films"](https://www.animepapa.com/decoding-symbolism-in-studio-ghibli-films-nature-identity-and-the-human-experience/)
  · ⚠️ (una fuente)
- **Temas recurrentes** confirmados en dos fuentes de análisis crítico:
  ambientalismo y el choque entre innovación e industrialización codiciosa
  (ejemplo típico: *La Princesa Mononoke*, *Nausicaä*); pacifismo; pérdida de
  la inocencia; la espiritualidad sintoísta chocando con la modernidad ·
  [CBR, "Recurring Themes in Studio Ghibli Anime Films, Explained"](https://www.cbr.com/studio-ghibli-recurring-themes-anime-films-explained/)
  y [shapes.inc, "Studio Ghibli Themes"](https://shapes.inc/fandom/studio-ghibli/themes)
  · ✅ (dos fuentes)
- **Protagonistas jóvenes, casi siempre niñas o adolescentes con agencia
  propia** (Nausicaä, San, Chihiro, Kiki, Ponyo, Sophie): tropo constante en
  la filmografía de Miyazaki, señalado junto con otros recursos de fantasía
  recurrentes (transformación, profecías cumplidas de forma no literal,
  criaturas híbridas) · [CBR, "Fantasy Tropes in Studio Ghibli Films, Explained"](https://www.cbr.com/studio-ghibli-fantasy-tropes/)
  · ⚠️ (una fuente)
- **Obsesión con los viajes y los vehículos** (el Gatobús, el tren sobre el
  mar de *El Viaje de Chihiro*, el planeador de *Nausicaä*, el castillo
  andante) como constante visual del estudio, ligada también al negocio
  familiar aeronáutico de Miyazaki · [Polygon, "Totoro Cat Bus, Spirited train, and Ghibli's travel obsession, explained"](https://www.polygon.com/animation-cartoons/2020/5/30/21275192/studio-ghibli-movies-catbus-planes-spirited-away-my-neighbor-totoro-themes/)
  · ⚠️ (una fuente, pero coincide con el tema del vuelo ya confirmado arriba,
  así que se considera reforzado)
- Fuente académica encontrada pero no accesible por límite de tiempo/tokens
  de esta tanda: PDF de Carnegie Mellon University sobre temas recurrentes en
  el arte y la literatura japonesa aplicados a Ghibli (`andrew.cmu.edu`,
  RoslynMcDonald_Ghibli.pdf) — pendiente de leer, ver «Sigue».
