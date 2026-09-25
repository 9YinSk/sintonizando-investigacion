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
