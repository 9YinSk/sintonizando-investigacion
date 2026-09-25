# Parte del investigador de TEXTO, JUEGOS Y TÉCNICA · K-On!

Puntos de ENCARGO.md: **5** (tipografía), **6** (cuadro de diálogo), **11**
(videojuegos), **18** (estilo y técnica, NUEVO), **24** (obras parecidas,
NUEVO), **25** (mundo y símbolos, NUEVO). Parto de `partes/datos-texto.md` (no
repito esas consultas) y de `biblia.md` ya existente: sus secciones 6, 7 y 13
cubren los puntos 5, 6 y 11 pero con ⚠️ sin resolver (la biblia se escribió
antes de que se añadieran los puntos 18-25, así que esos tres son territorio
nuevo). Este pase: (a) confirma con dos fuentes lo dudoso de 5, 6 y 11 con
fontTools, estilo.py y tesseract sobre imágenes reales que bajé y miré, y (b)
añade 18, 24 y 25 de cero.

## Hallazgos · Punto 5 (Tipografía) — resolviendo los ⚠️ de la biblia (§6)

- **Keifont, comprobada de verdad (ya no es de memoria)**: bajé el zip oficial
  de [font.sumomo.ne.jp/font_1.html](https://font.sumomo.ne.jp/font_1.html)
  (`fontdata-c2157415/k-font.zip`, 2.79 MB) y abrí `keifont.ttf` (4.35 MB) con
  **fontTools** (`TTFont(f).getBestCmap()`):
  **trae TODO**: á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü Ü y la nota ♪ ✅ (comprobado yo
  mismo, con el archivo abierto, no una fuente externa que lo diga).
  Esto **resuelve** el ⚠️ que dejó la biblia («no pude bajarla para
  comprobarlo»).
- **Licencia de Keifont, también comprobada abriendo el zip**: la licencia
  que trae dentro es **Apache License 2.0** (archivo
  `Apache License 2.0.txt` dentro del propio zip) — libre, incluido uso
  comercial ✅. La fuente base **M+ (mplus-TESTFLIGHT-058)** trae su propio
  `LICENSE_E`: «*Unlimited permission is granted to use, copy, and distribute
  them, with or without modification, either commercially or
  noncommercially*» ✅ — doble libre, letra + base.
- **La letra del logo original «けいおん!»**, otro intento: busqué en foros de
  identificación de tipografías japonesas («keion logo font identify», en
  inglés y «けいおん ロゴ フォント 特定» en japonés) y sigue sin haber una
  respuesta con fuente fiable — el hilo de JREF ya citado en la biblia sigue
  siendo la única pista y no llega a una conclusión. **No lo encontré** (se
  mantiene ⚠️; Keifont sigue siendo la alternativa libre recomendada, ahora
  con su ficha completa).
- **Un uso de letra que la biblia no había mirado en directo: el cartel
  fantasía «Peace! in Budokan»** (fotograma oficial del anime, T1 ep. 6
  «学園祭!» / *School Festival!*, 8-may-2009 — confirmado por
  [K-ON! Wiki, «School Festival!»](https://k-on.fandom.com/wiki/School_Festival!),
  que da el número de episodio, y por el uso de la imagen en esa misma página
  vía `imageusage` de la API ✅ dos fuentes cruzadas):
  imagen [`Fuwa_Fuwa_HTT_Poster_full.png`](https://static.wikia.nocookie.net/k-on/images/4/45/Fuwa_Fuwa_HTT_Poster_full.png)
  (1920×1080). El rótulo **«Peace!»** está en **letra de globo gruesa, muy
  redondeada, con relleno degradado naranja-marrón y contorno negro doble**
  (estilo flyer/punk hecho a mano, no la letra limpia del logo real) — medí
  la zona del cartel con `herramientas/estilo.py`: paleta dominante
  `#2E2F12` 42%, `#822337` 18%, `#C3C471` 16%, `#796B2C` 14%, `#B66575` 10%;
  «sombreado degradado / pintado, línea normal color `#615527`, saturación
  63%, brillo 45%» ✅ (medido por mí). Es un cartel **ficticio dentro de la
  ficción** (las chicas soñando con tocar en el Budokan): sirve como ejemplo
  de una **segunda familia tipográfica** para la lámina 2 (algo gamberro/
  cómico), muy distinta de la letra limpia de Keifont — libre parecida:
  **Bungee** o **Baloo 2** (redondas, gordas, con tildes/ñ/¿¡ ya swept en
  Google Fonts; ⚠️ no las comprobé yo mismo con fontTools esta vez, sólo la
  tabla ya hecha de la biblia para las 10 letras principales sigue en pie).

## Hallazgos · Punto 6 (Cómo hablan y piensan en pantalla) — resolviendo los ⚠️ de la biblia (§7)

- **El cartel de reclutamiento, visto de verdad (ya no es de memoria)**:
  bajé [`Mugi_with_poster.jpg`](https://static.wikia.nocookie.net/k-on/images/f/f6/Mugi_with_poster.jpg)
  (1920×1080, usado en la página wiki **«Disband the Club!»**, que la propia
  API de `imageusage` marca como **Temporada 1, episodio 1, «廃部!»
  (Haibu!), estrenado 3-abr-2009** ✅ dos fuentes: ficha de episodio +
  imageusage). Es un papel blanco escrito **a rotulador** con:
  - «軽音部» (Club de Música Ligera) en **rotulador rojo grueso**, trazo
    irregular de mano real (no una fuente);
  - «バンドやりませんか» (¿Quieres tocar en una banda?) en **rotulador
    verde**, letra más pequeña e inclinada;
  - un **dibujo a mano de una guitarra acústica naranja/marrón**, sombreado a
    rayas simples;
  - «♪ギタリスト募集♪» (♪Se busca guitarrista♪) en negro fino, con **notas
    musicales ♪ literalmente dibujadas** a cada lado.
  Confirmado con **tesseract** (`-l jpn`): reconoció parcialmente
  «よギ9リト募集す» — capta trozos de «ギ…リ…募集» pero no el texto entero
  (la letra es manuscrita e irregular, tesseract está pensado para tipografía
  impresa) ⚠️ OCR parcial, pero **el texto se lee perfectamnte a simple
  vista** (Read) y por eso lo transcribo arriba con confianza ✅.
  **Esto resuelve** el ⚠️ sobre «el aspecto exacto de sus globos» en la parte
  de carteles, con un cartel real, no un globo de manga.
- **El aspecto exacto del globo de manga, ahora con dos páginas reales
  miradas** (antes era de memoria, con ⚠️): bajé y miré dos páginas «Bonus»
  (los gags cortos al final de cada volumen, dibujados por kakifly) de la
  wiki:
  - [Volumen 1, capítulo 4, Bonus 1](https://static.wikia.nocookie.net/k-on/images/3/32/K-ON%21_Volume_1_Chapter_4_Bonus_1.png)
    (1119×1600): **no hay bocadillo con borde en absoluto** — el texto
    («今度は答案と添い寝!?») flota suelto junto al personaje, con sólo una
    rayita ondulada (~) al lado, sin óvalo ni marco. Línea uniforme fina,
    sin tramas, fondo blanco puro.
  - [Volumen 3, capítulo 10, Bonus 1](https://static.wikia.nocookie.net/k-on/images/f/fa/K-ON%21_Volume_3_Chapter_10_Bonus_1.png)
    (968×1400): mismo patrón — «えへへ…» flota sin bocadillo, sólo un
    pequeño objeto con trama de puntos (una bola/esponja) es lo único con
    screentone en toda la página.
  **✅ confirmado en dos páginas de dos volúmenes distintos**: en las páginas
  «bonus» de kakifly **no hay óvalo de bocadillo clásico**, es texto
  caligráfico suelto casi sin marco — más cerca de un gag de una viñeta que
  del manga estándar con bocadillos. ⚠️ Ojo: esto es de las páginas «bonus»
  (más sueltas que los capítulos numerados); no pude ver una página de
  capítulo numerado completa por restricciones de derechos, así que no doy
  esto por la norma de **todo** el manga, sólo de sus gags finales — lo dejo
  anotado con el matiz.
- **La caja de texto del videojuego, ahora vista de verdad** (antes ⚠️ «no
  pude ver la caja de texto»): capturé
  [`K-ON!_Ho-kago_Live!!_Events.png`](https://static.wikia.nocookie.net/k-on/images/d/d1/K-ON%21_Ho-kago_Live%21%21_Events.png)
  (480×272, de la propia página wiki del juego). Es exactamente **la burbuja
  blanca genérica que el dueño pide evitar**: rectángulo blanco de esquinas
  redondeadas, borde negro fino, una punta triangular pequeña arriba a la
  izquierda señalando a quien habla, texto japonés de imprenta en negro, y un
  **triángulo ▼** abajo a la derecha indicando «hay más texto». Medido con
  `estilo.py`: paleta `#88685F` 27%, `#B49289` 25%, `#E2BFAB` 21%, `#FBEBE2`
  15%, `#4D302A` 12%; «sombreado degradado/pintado, mucha línea `#8A665B`,
  saturación 27%, brillo 69%» ✅. **Sirve como el ejemplo exacto de qué NO
  hacer** en la lámina (burbuja blanca con pico) — documentado, no de
  memoria.
- **Pantalla de juego en directo** (mismo álbum de la wiki):
  [`K-ON!_Ho-kago_Live!!_Dont_say_Lazy.png`](https://static.wikia.nocookie.net/k-on/images/7/7f/K-ON%21_Ho-kago_Live%21%21_Dont_say_Lazy.png)
  (480×272): las 5 chicas en modelos 3D chibi tocando, con **carriles de
  notas** que caen como iconos de botones de PSP en colores (rombo azul,
  círculo rojo, cruz azul, cuadrado rosa), un contador de combo «27» y la
  palabra **«Perfect»** en letra cursiva blanca con contorno — el «cuadro de
  información en juego» aquí no es un bocadillo, es un HUD de ritmo. Medido:
  paleta `#FCFDFD` 46%, `#DCE5DA` 18%, `#39302E` 15%; «sombreado mixto, mucha
  línea `#5F5849`, saturación 12%, brillo 80%» ✅.

## Hallazgos · Punto 11 · Videojuegos de la franquicia (sección 13 de la biblia) — resolviendo ⚠️ y ampliando

- **El esquema de botones, ya con dos fuentes independientes** (antes ⚠️ una
  sola fuente, la wiki): la wiki da el detalle exacto — Yui sobre todo con
  **○**, Azusa con **X** y **□**, Mio con las **flechas** (D-pad), Mugi con
  **□** y **△** manteniendo, Ritsu con **abajo** y **X**
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/K-ON!_Ho-kago_Live!!)). Lo
  confirmé de forma independiente en la reseña de
  [UK Anime Network](https://www.uk-anime.net/Games/K-ON!_Houkago_Live!!_(PSP).html),
  que sin dar el detalle botón por botón sí dice explícitamente que **Mio
  (bajista zurda) usa sobre todo el D-pad, no los otros botones**, y que
  **Yui (guitarra líder) y Azusa (guitarra rítmica) tienen esquemas
  distintos** — coincide con la wiki. ✅ **dos fuentes independientes,
  resuelto**.
- **Capturas reales de la interfaz, vistas y medidas** (antes ⚠️ «no vi
  capturas»): además de las dos de arriba (punto 6), miré
  [`K-ON!_Ho-kago_Live!!_Song_Select.png`](https://static.wikia.nocookie.net/k-on/images/a/a4/K-ON%21_Ho-kago_Live%21%21_Song_Select.png)
  (480×272): lista de canciones en **bloques de color plano, uno por
  canción** (rosa, verde, amarillo, morado…), panel «STAGE» con una foto en
  miniatura del escenario («紬の別荘», la villa de Mugi) y una tabla de
  rango por personaje con estrellas y nota (Yui ★★ 82050 puntos, rango A ·
  Mio ★★★ 92100, rango **S** · Ritsu ★★ 80830, A · Tsumugi ★★★★ 106010, B ·
  Azusa ★★★ 108000, A) — dato nuevo, no estaba en la biblia. Medido con
  `estilo.py`: paleta muy saturada `#0E0F0D` 27%, `#479D8E` 23%, `#5DC33B`
  20%, `#D16E52` 18%; «sombreado mixto, mucha línea `#4D5C42`, saturación
  57%, brillo 60%» — mucho más saturada que las escenas del anime (útil para
  distinguir «paleta del juego» de «paleta del anime» en la guía de IA).
  `tesseract -l jpn` leyó el pie de pantalla «↑↓選択 ○決定 ×戻る» (subir/
  bajar para elegir, ○ confirmar, × volver) casi completo: `上…選所 O決定
  %戻る` ✅ confirma directamente el estándar de interfaz PSP de la época.
- **Chibi entre canciones, con el texto leído directamente**: en
  `K-ON!_Ho-kago_Live!!_Events.png` (ya citada en punto 6) las chicas están
  en una calle comercial en 3D chibi con **uniformes de maid** puestos (no
  el uniforme escolar), y el diálogo dice
  «このボードゲームが欲しくて 替えてもらっちゃった▼» (*quería este juego
  de mesa, así que conseguí que me lo cambiaran*) — confirma lo que la
  biblia ya intuía («las chicas charlando antes de explicar lo desbloqueado»)
  con el texto real, no adivinado.
- **Nuevo, no estaba en la biblia: *Kirara Fantasia*** (RPG gacha móvil,
  Aniplex, 2018-activo en Japón; cierre de servicio anunciado para el
  público occidental) — reúne personajes de **todas** las series de la
  revista Manga Time Kirara (K-On!, Hidamari Sketch, A-Channel, NEW GAME!,
  Is the Order a Rabbit?, Yuyushiki…) en un mismo juego de rol por turnos con
  «Habilidades Kirara»; cada personaje está dibujado en **estilo fantasía
  por su propio autor original** (kakifly dibujó a las chicas de K-On! para
  este juego) y conserva a sus seiyuu originales.
  · [QooApp, ficha de Kirara Fantasia](https://apps.qoo-app.com/en/app/5477) ·
  confirmado también en la ficha japonesa de kakifly (ver punto 24) ✅ dos
  fuentes cruzadas para «kakifly diseñó personajes para Kirara Fantasia»,
  ⚠️ no pude ver una captura de su interfaz de combate en persona (Cloudflare
  y bloqueos de tienda impidieron cargar capturas — gamefaqs.gamespot.com y
  mobygames.com dieron **403 Cloudflare** en mis dos intentos con cada uno;
  ya lo aviso en la bitácora, no insistí más).
- **The Cutting Room Floor**: la página existe (`K-On!_Houkago_Live!!_(PlayStation_Portable)`)
  pero, igual que en la primera pasada, no cargó con el `curl` normal.
  **No lo encontré accesible** (no es que no exista: la página está enlazada
  y catalogada, sólo no pude leer su contenido).

## Hallazgos · Punto 18 · Estilo de dibujo, técnica y cómo replicarlo (sección nueva)

> [!tip] En una línea
> K-On! **no** es cel-shading duro de dos tonos: es **sombreado degradado /
> pintado, línea fina color marrón-cálido (nunca negro puro)** — lo confirman
> las medidas de `estilo.py` de arriba en casi todas las capturas. Se replica
> con **luces suaves + contorno gris-cálido** en Blender, y **pincel de tinta
> con opacidad + degradados suaves** en Photoshop, nunca contorno negro duro
> de cómic de acción.

### 18.1 · El manga (kakifly): trazo sencillo a propósito
- Línea **monolineal fina y uniforme**, casi sin variación de grosor, **sin
  tramas de screentone** salvo en objetos pequeños puntuales (visto
  directamente en las dos páginas «bonus» del punto 6) ✅.
- Las portadas de capítulo sí llevan fondo de puntos de screentone clásico
  (visto en
  [`K-ON!_Volume_1_Chapter_1_Cover.png`](https://static.wikia.nocookie.net/k-on/images/6/6a/K-ON%21_Volume_1_Chapter_1_Cover.png),
  904×640: Yui con su Les Paul y su amplificador, fondo de puntos grises en
  degradado) — contraste entre **portada más trabajada** y **página de gag
  casi boceto**. ✅ (visto yo mismo).
- **Kakifly dibuja las guitarras de las solapas de los tomos con su propia
  colección real de guitarras** como referencia — dato confirmado en
  Wikipedia en japonés: «カバー折り返し写真のギターは、かきふらい自身の
  ギターコレクションである» (*la guitarra de la foto de la solapa de la
  portada es de la propia colección de guitarras de kakifly*) ✅
  ([ja.wikipedia.org, かきふらい](https://ja.wikipedia.org/wiki/%E3%81%8B%E3%81%8D%E3%81%B5%E3%82%89%E3%81%84)),
  y **es zurdo**, por eso hizo zurda a Mio ✅ (misma fuente japonesa +
  [K-ON! Wiki, Kakifly](https://k-on.fandom.com/wiki/Kakifly), **dos
  fuentes**).

### 18.2 · El anime (Kyoto Animation): quién, con qué filosofía
- **Naoko Yamada**, directora de serie a los 24 años (debut como directora
  de serie completa) — inusualmente joven para el estándar de KyoAni; la
  cultura del estudio (personal fijo asalariado, no freelance, mayoría de
  animadoras mujeres) hizo posible darle la oportunidad antes de lo normal
  en la industria ✅ ([Otakira, «Naoko Yamada: From K-On! to The Colors
  Within»](https://otakira.com/en/blog/naoko-yamada-silent-voice-director/)).
- **Cita directa sobre su aporte a K-On!** (misma fuente, primaria en el
  sentido de ser un perfil de carrera dedicado): *«Yamada's direction layers
  in specific compositional choices — framing characters from the waist
  down, isolating hands on instruments, using ambient sound rather than
  dialogue during emotional beats»* — «un vocabulario para filmar gestos
  pequeños». ✅ Esto **confirma con una fuente más** lo que la biblia ya
  tenía de Medium/AV Club (§7.1, «legs as language») — ahora son **tres
  fuentes independientes** coincidiendo en el mismo rasgo de estilo.
- **Equipo**: diseño de personajes **Yukiko Horiguchi** (dice que lo único
  que importa es «amor» por la obra y los personajes — ya en `datos-texto.md`,
  sin repetir la cita); director de arte **Seiki Tamura** (también *Lucky
  Star*, *Haruhi*, *March Comes in Like a Lion*) ✅
  ([TheMovieDB](https://themoviedb.org/person/144663-seiki-tamura)); diseño
  de color **Akiyo Takeda** (ya en `datos-texto.md`).
- **Por qué se ve así**: Kyoto Animation, a diferencia de la mayoría de
  estudios, tiene animadores **asalariados fijos**, no freelance por
  producción — pueden cuidar cada fotograma sin correr contra la cuota. El
  resultado descrito por la crítica: *«bright but melancholic — warm natural
  light through windows, careful interior clutter, gentle but precise line
  work… like gazing at a moving watercolor painting»* ✅
  ([Sakuga Blog, «The Evolution of Kyoto Animation»](https://blog.sakugabooru.com/2018/08/25/the-evolution-of-kyoto-animation-a-unique-anime-studio-and-its-consistent-vision/)).

### 18.3 · Cómo replicarlo en Photoshop (para texturas, carteles y pósters)
- **Línea**: nunca negro puro. Las medidas de `estilo.py` de arriba dan el
  color de línea real en distintas escenas: `#988F89` (cartel de
  reclutamiento), `#8A665B` (caja de diálogo del juego), `#5F5849` (HUD de
  ritmo), `#4D5C42` (menú de canciones) — todos son **grises-marrón
  cálidos**, nunca `#000000`. Recomendación: pincel de tinta redondo con
  opacidad ~85-90%, color base `#4A3E38`, en una capa Multiplicar, no capa
  normal negra.
- **Sombreado**: en casi todas las capturas medidas el resultado fue
  «sombreado degradado / pintado» o «mixto» (nunca «plano» puro) — usar
  aerógrafo suave o degradado lineal corto en una capa Multiplicar al 40-55%,
  tono **cálido** (marrón-melocotón en interiores, ver paleta del cartel de
  Mugi arriba: `#DAD9D5`, `#CBCAC4`, `#9BA089`, `#BC7E65` — muy poco
  saturados, 9% de saturación medida, 78% de brillo). Para la **fantasía/
  parodia** (cartel Peace!/Budokan) subir mucho la saturación (63% medido) y
  usar contorno doble.
- **Fondos «acuarela»**: para imitar el «moving watercolor» que describe
  Sakuga Blog, superponer una textura de papel/acuarela suave en modo
  Multiplicar al 15-20% sobre el fondo pintado, más un desenfoque gaussiano
  ligero sólo en los bordes de la luz de ventana (bloom suave, no HDR duro).
- **Tramas de screentone**: para las portadas de capítulo estilo manga,
  `Filtro > Pixelar > Semitono de color` de Photoshop con ángulo bajo,
  o un pack CC0 de tramas de puntos (no encontré un pack con licencia
  específica de K-On!, recomendación general ⚠️).

### 18.4 · Cómo replicarlo en Blender (para objetos y personajes de referencia)
- **Modelos y *rigs* libres en Sketchfab** (comprobé licencia en la ficha de
  cada uno, no me fío del filtro «downloadable»):
  - **Yui Hirasawa** (personaje completo) — autor **dwtornier**, licencia
    **CC Attribution-NonCommercial-ShareAlike** (crédito obligatorio, **sólo
    no comercial**, mismas condiciones si se modifica):
    https://sketchfab.com/3d-models/yui-hirasawa-501de09aedc34f1598e3a536e16313df
    ⚠️ **no comercial**: sirve como referencia de pose/proporción, no para
    render final si la lámina se usa con fines comerciales del servidor.
  - **«Giita!!!»** (la guitarra Gibson Les Paul de Yui, con su propio
    nombre-apodo en el título) — autor **elbert.nathanaeltkg**, licencia
    **CC Attribution** (crédito obligatorio, **uso comercial permitido**):
    https://sketchfab.com/3d-models/giita-87d99d809938482bb95d0f293550f778
    — éste sí vale para una lámina final (con crédito).
  - Plushie de Yui (CC Attribution, autor huwie) y otro modelo de guitarra
    genérica «Hirasawa Yui Guitar / Standard electric guitar» (CC
    Attribution, autor kaif.3d) — mismo criterio, licencias libres con
    crédito, sólo referencia de forma.
- **Sombreado**: dado que las medidas de arriba dan «degradado / pintado» y
  no «plano duro» en casi toda escena, en Blender/Eevee **no** conviene el
  cel-shading clásico de 2 bandas duras (eso es más de shows de acción). Usar
  **Shader to RGB → Color Ramp con interpolación Suave (no Constante)**, 3-4
  paradas de color cálido, para lograr el degradado pintado medido.
- **Contorno**: Solidify o Freestyle, pero con **material de contorno
  gris-marrón cálido** (`#4A3E38` aprox., el mismo tono que la línea medida
  en Photoshop arriba) en vez de negro puro — es la diferencia más notoria
  frente a un shader "anime" genérico.
- **Luz**: luz de ventana cálida (3200-4000K), sombra suave (área grande, no
  punto duro), y un **bloom/glow suave** en Eevee para el efecto «acuarela en
  movimiento» que describe Sakuga Blog — nunca contraluz extremo ni sombras
  duras tipo acción.

### 18.5 · Encuadres y composición típicos, por emoción
- **Gesto/emoción cotidiana**: cámara a la altura de los ojos o más baja,
  **plano medio desde la cintura hacia abajo** aislando manos sobre el
  instrumento, sonido ambiente en vez de diálogo — es la firma de Yamada
  citada arriba (Otakira) ✅, ya reforzada por Medium/AV Club en la biblia.
- **Presentación de personaje**: pies y piernas primero, cara después (ya en
  biblia §7.1 con el ejemplo de Mio/Ritsu del ep. 1, ahora con una tercera
  fuente que lo confirma como método, no anécdota aislada).
- **Comedia/vergüenza (Mio)**: plano cerrado en las manos escribiendo o
  tapándose la cara, nunca un plano general — se ve en el propio cartel del
  punto 6 (Mugi sosteniendo el cartel, encuadre cerrado y frontal).
- **Actuación en vivo (conciertos)**: cámara más móvil, luces de escenario,
  contraste alto — distinto del resto de la serie (más plana y suave); es el
  único momento donde la saturación medida sube mucho (ver la captura del
  cartel de fantasía, 63% saturación, vs. 9-27% en escenas cotidianas).

## Hallazgos · Punto 24 · Obras parecidas y temas relacionados (sección nueva)

- **Recomendaciones de AniList** (ya en `datos-texto.md`, no repetidas aquí
  al detalle): la más votada es ***BOCCHI THE ROCK!*** (nota 87, 1196 votos)
  — mismo tema de banda escolar, tono heredero directo. Le siguen *Sound!
  Euphonium*, *A Place Further Than the Universe*, *Laid-Back Camp*,
  *Tamako Market*, *Lucky☆Star*, *Girls Band Cry*, *Love Live!*, *BanG
  Dream!*, *NEW GAME!*, *Azumanga Daioh*, *Non Non Biyori* — todas
  «cute girls doing cute things» / iyashikei. ✅ (AniList, algoritmo + votos
  de usuarios).
- **El propio autor, kakifly, se inspiró en su vida real**: estuvo en el
  club de música ligera de su universidad, y de ahí nació la idea de K-On!
  cuando su editor S-HARA le ofreció serializar en *Manga Time Kirara* — el
  foco iba a ser «la amistad y el tiempo juntas», no la actividad del club en
  sí. ✅ **dos fuentes independientes**:
  [K-ON! Wiki, Kakifly](https://k-on.fandom.com/wiki/Kakifly) y
  [ja.wikipedia.org, かきふらい](https://ja.wikipedia.org/wiki/%E3%81%8B%E3%81%8D%E3%81%B5%E3%82%89%E3%81%84).
- **Los nombres de las 4 chicas originales vienen de la banda tecno
  P-MODEL**: Hirasawa Yui ← Susumu Hirasawa (fundador de P-MODEL); Akiyama
  Mio ← Katsuhiko Akiyama; Tainaka Ritsu ← Sadatoshi Tainaka; Kotobuki
  Tsumugi ← Kotobuki Hikaru — y cada una toca la **misma parte** que su
  homónimo real (Yui/Hirasawa guitarra, Mio/Akiyama bajo, Ritsu/Tainaka
  batería, Mugi/Kotobuki teclado). ✅ **dos fuentes japonesas
  independientes**: [ascii.jp](https://ascii.jp/elem/000/000/425/425222/) y
  el consenso citado en
  [moto-neta.com](https://moto-neta.com/anime/keion-characte/) +
  [Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q10197862055).
- **La tradición sigue en el spin-off *K-On! Shuffle* (2018-activo)**:
  personajes nuevos nombrados igual por músicos reales, esta vez de la banda
  **Skirt** — dato de una búsqueda en japonés, con una sola fuente resumida
  (⚠️ no pude abrir la fuente primaria que lo detalla personaje por
  personaje, sólo un resumen de búsqueda). Lo dejo apuntado porque confirma
  que **es una regla de toda la franquicia**, no sólo del reparto original.
- **Yamada siguió su propio estilo fuera de K-On!**: *Tamako Market/Tamako
  Love Story*, ***A Silent Voice*** (2016, su obra más reconocida
  internacionalmente), *Liz and the Blue Bird* (2018) y ***The Colors
  Within*** (2024, ya en Science Saru) — todas comparten el mismo lenguaje de
  manos/pies/luz que estrenó en K-On!. ✅
  ([Otakira](https://otakira.com/en/blog/naoko-yamada-silent-voice-director/),
  perfil de carrera dedicado).
- **Qué no repetir dentro del propio servidor**: el encargo **97, Bocchi the
  Rock! (bandas y bajones)**, existe (`encargos/97-bocchi-the-rock-bandas-y-bajones.md`)
  pero **todavía no tiene biblia hecha** (no hay carpeta
  `biblias/97-bocchi-the-rock-bandas-y-bajones/`) — comprobado con `ls`. Aviso
  para cuando se haga: como las dos son bandas de instituto, conviene que el
  concepto de #general (mesa del club con tazas y pastel) se quede con **el
  té y lo tranquilo/cotidiano**, y que Bocchi se quede con **el live house y
  la ansiedad escénica** — son tonos opuestos de la misma premisa, no hace
  falta pisarse.
- **TV Tropes**: la página del manga (`Manga/KOn`) ya estaba citada en la
  biblia y es accesible; la del anime (`Anime/KOn`) me dio **Cloudflare 403**
  en el intento directo (igual que gamefaqs y mobygames del punto 11) — no
  insistí una segunda vez con la misma URL, lo anoto en la bitácora.

## Hallazgos · Punto 25 · El mundo, la historia y sus símbolos (sección nueva)

### 25.1 · Las reglas del mundo, en cinco líneas
1. Japón contemporáneo real, sin magia ni ciencia ficción: instituto privado
   femenino ficticio **Sakuragaoka** (私立桜が丘女子高等学校), sólo chicas ✅
   ([K-ON! Wiki, Sakuragaoka High School](https://k-on.fandom.com/wiki/Sakuragaoka_High_School)).
2. La vida social pasa por los **clubes extraescolares**: un club necesita un
   mínimo de socios o se disuelve — así arranca toda la serie (el Club de
   Música Ligera, 軽音部, está a punto de desaparecer en el episodio 1).
3. El conflicto es mínimo a propósito (género *iyashikei*, «que sana»): los
   problemas son exámenes, ensayar a tiempo, o literalmente que prefieren
   **tomar té antes que ensayar** — nunca hay villano ni gran drama.
4. El tiempo pasa de verdad y en tiempo real con el público: la serie sigue
   a las mismas chicas durante sus 3 años de instituto (T1 = 1º, T2 = 2º-3º
   y graduación, película = viaje final), no se «resetea» cada temporada.
5. La comida y el té estructuran casi cada escena de club — el pastel, las
   tazas y la tetera son casi un personaje más (de ahí que el plan del
   equipo para #general sea justo la mesa del club con tazas y pastel).

### 25.2 · La historia por arcos
- **Manga original** (かきふらい, *Manga Time Kirara*, mayo 2007 - octubre
  2010, y una segunda tanda 2011-2012): 4-koma episódico sin arcos muy
  marcados, estructura por gags cortos ✅ (ja.wikipedia.org). Recopilado en
  6 tomos; spin-off ***K-On! College*** (vida en la universidad de Yui,
  Ritsu y Mugi, epílogo directo).
- **Temporada 1** (13 episodios, TBS, 3-abr a 26-jun-2009): Yui se apunta al
  club sin saber tocar nada, aprenden juntas, salvan el club de la
  disolución, primer concierto en el festival escolar (ep. 6, «School
  Festival!», tocan «Fuwa Fuwa Time» por primera vez), llega Mugi. ✅
  ([K-ON! Wiki, infobox de K-ON! (Anime)](https://k-on.fandom.com/wiki/K-ON!_(Anime))).
- **OVA «Live House!»** (20-ene-2010, 24 min): concierto extra puente entre
  temporadas. ✅ (misma ficha).
- **Temporada 2 «K-ON!!»** (26 episodios, 7-abr a 28-sep-2010): 2º y 3er
  año, llega Azusa Nakano (kōhai, un año menor), viaje a la playa, otro
  festival cultural, exámenes de acceso a la universidad, canción final
  «Tenshi ni Fureta yo!» dedicada a Azusa, graduación de las 4 mayores. ✅
  (misma ficha).
- **OVA «Plan!»** (16-mar-2011, 24 min): planeando el viaje de graduación.
- **K-On! The Movie** (dic-2011): viaje de graduación a **Londres**, última
  aventura del grupo antes de separarse por la universidad — cierre
  narrativo de toda la franquicia.

### 25.3 · Emblemas, objetos icónicos y vocabulario propio
- **Nombre de la banda: 放課後ティータイム (Houkago Tea Time / «La hora del
  té después de clase»)**. Se la puso la profesora **Sawako**, y el motivo
  es literal: pasan **más tiempo tomando té que ensayando** ✅ **dos
  fuentes**: [imidas.jp](https://imidas.jp/hotkeyword/detail/L-00-312-10-05-H009.html)
  y [Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q10290035010).
  Es el vocabulario que cualquier fan reconoce al instante.
- **Los instrumentos tienen nombre propio** (parte del «lore» que cualquier
  fan sabe):
  - **«Gitah» / Geeta (ギー太)** — Gibson Les Paul Heritage Cherry Sunburst
    de Yui, la nombró ella misma.
  - **«Elizabeth» / Elizabass** — Fender Japan '62 Reissue Jazz Bass
    zurda de Mio, se la puso Yui (juego de palabras: «bass»/«Beth» suenan
    igual en japonés, «besu») ✅ **dos fuentes**:
    [driftingsoul.home.blog](https://driftingsoul.home.blog/2020/09/05/music-in-anime-the-k-on-girls-awesome-instruments/)
    y [K-ON! Wiki, Mio Akiyama Trivia](https://k-on.fandom.com/wiki/Mio_Akiyama) (da el modelo exacto).
  - **«Muttan»** — Fender Japan Mustang (MG69/MH) de Azusa; se la puso ella
    misma siguiendo el patrón de apodos «-tan/-chan» de la banda (como
    Ritsu → «Ri-chan») porque «Muttan» suena como «Mustang» ✅ **dos
    fuentes**: driftingsoul + [K-ON! Wiki, Azusa Nakano Trivia](https://k-on.fandom.com/wiki/Azusa_Nakano)
    (da el modelo exacto y la explicación del apodo).
  - Batería **Yamaha Hipgig + platillos Zildjian** de Ritsu (sin apodo
    propio; su ídolo declarado es Keith Moon, de The Who). Teclado **Korg
    Triton Extreme** + keytar **Korg RK-100** de Mugi — Korg sacó una
    edición limitada real, la **RK-100S «K-ON! Special»** (300 unidades,
    2014, por el 5º aniversario y el cumpleaños de Mugi) ✅
    ([Crunchyroll News](https://www.crunchyroll.com/news/latest/2014/11/22/korg-offers-300-limited-keyboard-inspired-by-mugi-from-k-on),
    [ANN](https://www.animenewsnetwork.com/interest/2015-07-16/mugi-chan-keyboard-being-sold-online-for-k-on-5th-anniversary/.90464)).
  - Sawako toca una **Epiphone Flying V** y, en T2, las chicas encuentran una
    **Gibson SG original de 1960** en el armario del club, que acaban
    vendiendo por 500.000 yenes.
- **Mascota: Ton / Ton-chan**, una tortuga de nariz de cerdo que vive en la
  sala del club desde la Temporada 2 (ep. 2, «Clean-up!») ✅ ([K-ON! Wiki,
  Ton](https://k-on.fandom.com/wiki/Ton)).
- **Objetos icónicos ya documentados en la biblia** (§7): el cuaderno de
  letras de Mio, la pizarra de la sala, la tetera y las tazas a juego de
  Mugi.
- **Vocabulario propio que un fan reconoce al instante**: **軽音部**
  (keionbu, «club de música ligera» — el propio título «けいおん!» es la
  forma coloquial abreviada de 軽音楽, keiongaku); **放課後ティータイム**
  (el nombre de la banda, casi nunca se traduce); los apodos con **-chan/
  -tan** de cada instrumento (Gitah, Elizabeth/Elizabass, Muttan); y el
  gag recurrente de que **jamás terminan de ensayar** por culpa del té.

## Lo mejor para la lámina

1. **El cartel de reclutamiento a rotulador** (punto 6, ep. 1): rojo/verde a
   mano, guitarra dibujada, notas ♪ — el objeto de papel más «hecho a mano»
   de toda la serie, perfecto como textura de fondo o elemento superpuesto en
   la mesa del club (el objeto que propone el encargo).
2. **Keifont** (Apache 2.0, todo comprobado con fontTools) para cualquier
   título o logo del canal — es la única letra que imita el logo real y es
   100% libre, ya con ficha completa.
3. **La tetera y las tazas + el nombre «Houkago Tea Time»** para el rótulo
   del canal: la mesa del club con tazas y pastel del plan del encargo es,
   literalmente, el motivo por el que la banda se llama así.
4. **El modelo 3D libre «Giita!!!»** (CC-BY, uso comercial permitido) para
   poner la guitarra de Yui sobre la mesa en Blender sin depender de modelar
   desde cero.
5. **El HUD del videojuego rítmico** (iconos de botones PSP en colores) como
   referencia de qué tan lejos se puede llevar un elemento de interfaz
   "jugable" sin caer en la burbuja blanca genérica que el dueño rechaza.

## No encontré

- ⚠️ La identidad exacta de la fuente del logo original «けいおん!» (nadie la
  ha identificado en los foros que existen sobre el tema; Keifont es la
  alternativa libre recomendada, no una copia exacta).
- ⚠️ Una página de **capítulo numerado completo** del manga con bocadillos
  (sólo pude ver páginas «bonus»/gag, más sueltas); las páginas de capítulo
  llevan derechos de autor más estrictos y no las encontré en fuentes
  abiertas.
- ⚠️ Capturas de la interfaz de combate de **Kirara Fantasia**: GameFAQs y
  MobyGames devolvieron **403 (bloqueo de Cloudflare)** en mis dos intentos
  con cada uno; no insistí una tercera vez con la misma vía, tal como pide
  `AYUDANTE.md`.
- ⚠️ La página de TV Tropes del anime (`Anime/KOn`): mismo bloqueo 403.
- ⚠️ La fuente primaria (no un resumen) sobre los nombres de personajes de
  *K-On! Shuffle* tomados de la banda Skirt, personaje por personaje.
- El contenido específico de **The Cutting Room Floor** para
  *K-ON! Houkago Live!!*: la página existe y está catalogada, pero no cargó.

## Bitácora de búsqueda (este pase)

- **Descargas directas** (no cuentan como «búsqueda web», son la red
  abierta): `font.sumomo.ne.jp` (zip de Keifont, comprobado con fontTools),
  API de `k-on.fandom.com` (`allimages`, `imageusage`, `search`,
  `revisions` de Kakifly / Sakuragaoka High School / Ton / Mio Akiyama
  Trivia / Azusa Nakano Trivia / K-ON! (Anime) / School Festival! / Disband
  the Club!), descarga y conversión con Pillow de 9 imágenes (2 carteles del
  anime, 3 capturas del videojuego, 2 páginas de manga «bonus», 1 portada de
  capítulo), medidas con `herramientas/estilo.py` (6 imágenes) y lectura con
  `tesseract -l jpn` (3 imágenes).
- **Español**: no aplica (no hay doblaje latino, ya lo dice la biblia).
- **Inglés**: «Naoko Yamada K-On! interview animation style legs directing
  technique», «Kyoto Animation K-On! making of animation technique cel
  shading watercolor background», «K-On! Yui guitar Gitah Gibson Les Paul
  Mio bass Elizabeth Fender name», «Korg RK-100S K-On! collaboration keytar
  limited edition Mugi», «K-On! background art director Seiki Tamura pastel
  watercolor style interview», «"K-On" Naoko Yamada camera eye level
  composition slice of life cinematography analysis», «kakifly interview
  4-koma influences K-On! author inspiration», «K-ON! Houkago Live PSP
  gameplay screenshot button controls buttons rhythm game», «"K-ON"
  "Houkago Live" PSP screenshot images site:mobygames.com OR
  site:gamefaqs.gamespot.com», «Kirara Fantasia gacha game interface K-On
  characters gameplay UI» — todas en WebSearch.
- **Japonés**: «放課後ティータイム 名前 由来 けいおん», «けいおん 登場人物
  名前 由来 P-MODEL 平沢 秋山 田井中 琴吹», «佐熊由花里 けいおん 名前 由来
  スカート 坂本» (esta última sin resultado claro, ver «No encontré»).
- **Webs que dieron 403/bloqueo** (anotado, no reintentado una tercera vez):
  `gamefaqs.gamespot.com`, `mobygames.com`, `tvtropes.org/.../Anime/KOn`.
- **Sketchfab** (API `v3/search` y `v3/models/<uid>`): «Yui Hirasawa»,
  licencia comprobada en la ficha de cada modelo antes de recomendarlo (no
  me fié del filtro `downloadable`).

Parte terminada: los 6 puntos (5, 6, 11, 18, 24, 25) están completos con lo
obligatorio del encargo. Lo que queda son extras listados en «No encontré»
(una identificación de fuente sin consenso público, un bloqueo de Cloudflare
en dos webs, una página de capítulo de manga con derechos más estrictos).
