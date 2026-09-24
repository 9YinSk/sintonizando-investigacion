# Parte del investigador de TEXTO, JUEGOS Y TÉCNICA · One Punch Man

Puntos de ENCARGO.md: **5** (tipografía), **6** (cuadro de diálogo), **11**
(videojuegos), **18** (estilo y técnica), **24** (obras parecidas), **25**
(mundo y símbolos). Parto de `partes/datos-texto.md` (no repito esas consultas)
y de lo que ya hay en `biblia.md` (secciones 6 y 7 ya están hechas de otra
pasada; 13, 19, 25 y 26 estaban vacías: «(pendiente)»). Esta parte añade lo
que falta para que el redactor lo meta.

## Hallazgos · Punto 5 (Tipografía) — sólo lo que faltaba

La biblia ya tiene una tabla completa de letras libres para logo, globo,
grito, katakana, onomatopeya y carta a mano (§6.2). Faltaban dos usos que pide
el encargo explícitamente: **interfaz de juego** y **subtítulos o créditos**.

- **Interfaz de juego**: en las capturas oficiales de Steam de *A Hero Nobody
  Knows* que miré (abajo, punto 11), el rótulo «**HERO Creation**» es una
  palo seco **muy condensada, negra y algo inclinada**, del mismo aire que
  **Teko** o **Saira Condensed Black** (ya comprobadas con fontTools en §6.2:
  ✅ tildes, ñ, ¿, ¡). No hace falta una letra nueva: sirven las mismas del
  logo. · fuente: capturas Steam app/991560 (Pillow, 1920×1080) ✅
- **Subtítulos o créditos**: el doblaje latino se ve en Crunchyroll y Netflix,
  cada uno con su propia tipografía de plataforma (no de la serie). Para un
  cartel del canal que cite un subtítulo, la letra libre más neutra y con
  todo comprobado por fontTools ya está en la tabla: **Oswald** (la usa la
  propia [web oficial](https://onepunchman-anime.net/) por Google Fonts) ✅
  todas las tildes, ñ, ¿, ¡. · ✅ (dos fuentes: fontTools + código fuente de
  la web oficial)
- **Ediciones en español (Ivrea)**: busqué scans del interior («One Punch Man
  Ivrea tomo interior scan globo letra», en español) y sólo aparecen fichas de
  venta (editorialivrea.com, whakoom.com, onianimestore.com) con tamaño y
  número de páginas, ninguna con página interior visible. **No lo encontré**
  (sigue igual que en §28 de la biblia).

## Hallazgos · Punto 6 (Cómo hablan y piensan en pantalla) — sólo lo que faltaba

- **PUBG Mobile × One Punch Man (colaboración del 20 sep. al 20 oct. 2026)**:
  vi el **arte promocional** (no el menú del juego en sí): Saitama sentado
  entre escombros bebiendo una lata, con Genos, Tatsumaki y Fubuki a la
  izquierda y Watchdog Man y un personaje de PUBG a la derecha. El titular
  «**ONE PUNCH TO WIN**» va en **blanco, palo seco muy condensada e
  inclinada**, el mismo aire que el logo de la serie.
  Imagen: [gamingonphone.com, `EN-scaled.jpg`](https://i0.wp.com/gamingonphone.com/wp-content/uploads/2026/09/EN-scaled.jpg)
  (1500×844, vista con Read) + confirmado en
  [ANN](https://www.animenewsnetwork.com/press-release/2026-09-21/pubg-mobile-collaborates-with-one-punch-man-to-bring-world-strongest-heroes-to-game/.242058)
  y [Inven Global](https://www.invenglobal.com/articles/26315/pubg-mobile-announces-collaboration-with-one-punch-man). ✅
  Personajes con set propio: Saitama («Ordinary Hero Set»), Genos, Terrible
  Tornado (Tatsumaki), Hellish Blizzard (Fubuki), Watchdog Man, Garou; armas
  «One-Punch Kar98K» y «Grocery Bag Machete» (el machete-bolsa-de-supermercado
  es un guiño directo al objeto cotidiano de Saitama). ⚠️ sigue sin verse el
  **menú/interfaz** real del juego con estos objetos puestos (sólo el cartel).

## Hallazgos · Punto 11 · Videojuegos de la franquicia (sección 13 de la biblia, vacía)

> [!tip] En una línea
> Cada juego de OPM tiene **su propia piel de interfaz**: la consola (*A Hero
> Nobody Knows*) usa el **rojo y negro serio de la Asociación de Héroes**; los
> móviles gacha usan **paneles azules «tech»** con números de daño enormes; el
> juego de mundo abierto usa **paneles rojos con esquinas redondeadas**. Las
> tres sirven de referencia distinta para una interfaz de canal.

### A · *One Punch Man: A Hero Nobody Knows* (PS4/Xbox One/PC, Spike Chunsoft, 27-feb-2020) ✅
- Capturas oficiales de Steam (app 991560, 1920×1080) miradas y medidas con
  `estilo.py` y Pillow:
  - **Pantalla «Hero Creation»**: cinta roja diagonal arriba a la izquierda
    con «**HERO Creation**» en blanco sobre rojo, pestañas *Base / Face /
    Height-Physique / Costume / Accessories / **Colors*** en gris muy oscuro
    (`#1C1D22` medido antes en §6.1), un **sello circular de la Asociación de
    Héroes** de marca de agua detrás, muy tenue, e indicador «**R1**» en rojo
    arriba a la derecha. Paleta de color en cuadrícula de 90 tonos abajo.
    [Captura vista](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/991560/ss_bedeee9ab3a00853f8e36fff0fefd4d6b9d7ae60.1920x1080.jpg)
  - **Saitama usando su especial**: kanji gigantes **「正義執行」** («ejecución
    de la justicia») en pincel negro grueso, sobre un fondo de hierba con luz
    dura de mediodía; guante rojo estirado hacia cámara.
    [Captura](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/991560/ss_4bcbd2c7b89cf384c5555074589f4d7cd62675d6.1920x1080.jpg) ·
    paleta medida: `#93BB7F` (hierba) `#F2F2EC` (capa) `#282A25` (traje oscuro).
  - **Genos vs. Speed-o-Sound Sonic**: composición diagonal, motion-blur en
    los proyectiles metálicos, efecto de disparo amarillo con resplandor
    (*bloom*) y humo; cielo azul despejado detrás de un puente.
    [Captura](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/991560/ss_cf3ebae34168af88903eb16bc254cdfdb1007dc7.1920x1080.jpg) ·
    paleta: `#191C20` `#ECD647` `#2D689E`.
  - Estilo medido (`estilo.py`): «sombreado degradado/pintado, línea normal»
    en las tres, saturación 26-44%, brillo 50-67%: **no es cel-shading plano
    puro**, lleva degradados suaves sobre el contorno negro (motor Unreal con
    *toon shader* + iluminación realista).
- DLC con su propia interfaz de tienda: Garou, Suiryu, Watchdog Man, Character
  Pass (todos con capturas 1920×1080 en `datos-texto.md`, sin repetir aquí).

### B · *One Punch Man: The Strongest* (móvil, gacha por turnos, activo en Asia; caídas en Occidente desde ene-2025) ✅
- Capturas oficiales de Google Play miradas (`w1052-h592`):
  - **Pantalla de combate**: marco de **panel azul «tech»** con esquinas
    redondeadas y filete claro, HUD dentro con «Active Attack», efecto de
    corte azul en arco y números de daño **enormes, blancos con borde rojo y
    contorno negro** («−12727», «Total DMG 33842»), tipografía palo seco
    condensada en cursiva.
    [Captura](https://play-lh.googleusercontent.com/H1f1CeF1ocNXmW8KKAl9iw0lJZsKlnrS74ecnR5Txptl_rmvKV5e43S4IpEdpsm3l0k3YzGjA9aJr1vMWIwjqQ=w1052-h592)
  - **Pantalla de alineación («Line up»)**: retratos circulares de los héroes
    (Flashy Flash, Mosquito Girl, Zombieman, Terrible Tornado, Gale Wind,
    Child Emperor…) con su nombre en inglés y «SP+número», anillos de color
    debajo de cada uno (rojo/azul/morado = tipo o rol), fila de miniaturas con
    estrellas de rareza abajo.
    [Captura](https://play-lh.googleusercontent.com/XXZ6Z1lnP14caZDrmBAr5sR4RcmJSK3VYvwI1v8wx7L48S5cDaTWqrLpysnQkOrM4TSne7Gu93XR-foUIWpE=w1052-h592)
  - Crédito fijo en toda captura promocional: «**©ONE, Yusuke Murata/SHUEISHA,
    Hero Association HQ**», en blanco pequeño.
  - Reseñas (Metacritic, ldplayer.net) señalan la interfaz como **«recargada,
    poco legible»**: dato útil para «qué NO hacer» si el canal usa esta
    referencia. ✅ (Metacritic + LDPlayer, dos fuentes)

### C · *One-Punch Man: World* (mundo abierto, Perfect World Games / Crunchyroll Games; lanzó 1-feb-2024, **cerró el 27-feb-2026**) ✅
- Cubre sólo la Temporada 1 (hasta el **Sea Monster Arc**), con Z-City y
  A-City explorables y misiones/redadas de 4 jugadores en tiempo real.
  · [ficha de la wiki](https://onepunchman.fandom.com/wiki/One_Punch_Man:_World) ✅
- Capturas oficiales miradas (mobi.gg):
  - **Combate de jefe**: marco de **panel rojo con esquinas redondeadas**
    alrededor de la escena de juego; arriba, nombre del enemigo («**Beast
    King**»), barra de vida en degradado rojo y un contador de golpes
    («**x15**»); arriba a la izquierda, temporizador «00/13» y un icono de
    pausa; abajo a la derecha, botón de habilidad **redondo con la cara chibi
    de Saitama** dentro.
    [Captura](https://images.mobi.gg/uploads/2024/02/1746/one-punch-man-screenshot-2.webp)
  - El cartel de lanzamiento usa el mismo **rojo diagonal con textura de
    grieta** que el logo del 10.º aniversario (§6.1 de la biblia), y el eslogan
    «**IT'S YOUR TURN TO BECOME A HERO FOR FUN**» en palo seco blanca muy
    gruesa con sombra roja.
    [Captura](https://images.mobi.gg/uploads/2024/02/1747/one-punch-man-screenshot-1.webp)

### D · Otros juegos (sin interfaz vista, para que conste) ⚠️
- ***Road to Hero* / *Road to Hero 2.0*** (móvil, OASGames/licenciado): juego
  de cartas ambientado antes de la serie. No encontré capturas de su
  interfaz real (sólo su ficha en AniList como `PREQUEL`). ⚠️
- **No hay página en The Cutting Room Floor** para ningún juego de One Punch
  Man: comprobado con la búsqueda del propio sitio
  (`tcrf.net/index.php?search=One+Punch+Man&fulltext=1` y con «A Hero Nobody
  Knows» también), 0 resultados en ambas. **No lo encontré** (no digo «no
  existe»: es sólo lo que dio la búsqueda directa en el sitio).

## Hallazgos · Punto 18 · Estilo de dibujo, técnica y cómo replicarlo (sección 19 de la biblia, vacía)

> [!tip] En una línea
> El chiste visual **es** la técnica: un **Saitama simplísimo** dibujado con
> un cuidado enorme (aunque no lo parezca) contra un **mundo hiperdetallado**
> a su alrededor. Se replica con **cel-shading de 2-3 bandas + contorno negro
> variable** en Blender, y **tinta dura + sombra plana** en Photoshop.

### 18.1 · Las dos capas de dibujo (manga) ✅
- **ONE** (guionista y dibujante original del webcómic): estilo **tosco y
  sencillo a propósito**, trazo rápido, casi sin sombreado, «muy alejado de
  los estilos típicos» de la época — así lo describe la prensa
  especializada. · [CBR](https://www.cbr.com/one-punch-man-webcomic-manga-artist-storyteller-success/) ·
  [ComicBook.com](https://comicbook.com/anime/news/one-punch-man-yusuke-murata-art-realistic/) ✅ (dos fuentes)
- **Yusuke Murata** (dibuja el manga oficial desde 2012, autor de *Eyeshield
  21*): redibuja la misma historia con **anatomía semirrealista, tinta muy
  contrastada y detalle obsesivo** (practica pintar bolas de cristal y
  canicas para dominar los reflejos). · [ComicBook.com](https://comicbook.com/anime/news/one-punch-man-yusuke-murata-art-realistic/) ✅
- **Programa de Murata**: dibuja en digital con **Clip Studio Paint** (el
  mismo programa que Boichi, de *Dr. Stone*). ⚠️ una sola fuente agregadora
  ([FandomWire](https://fandomwire.com/one-punch-man-quality-of-drawing-in-yusuke-muratas-manga-was-so-good-that-the-studio-thought-the-animation-can-never-match-it/));
  intenté la página oficial «CLIP STUDIO ASK» pero es una SPA en JS que no
  pude leer sin ejecutar el sitio.
- El contraste **Saitama-cara-simple / mundo-hiperdetallado en la misma
  viñeta** ya está anotado en §6.3 de la biblia como «el chiste visual base».

### 18.2 · El anime: quién lo hizo y con qué técnica (con citas directas) ✅
- **Temporada 1 (2015, 12 episodios)**: estudio **Madhouse**; director
  **Shingo Natsume**; diseño de personajes **Chikashi Kubota**. Los dos
  habían trabajado juntos antes en ***Space Dandy*** (BONES, 2014) y Kubota
  aceptó el encargo de OPM **por lo bien que le había ido en esa serie**.
  Natsume dice que *Space Dandy* le sirvió de referencia para **el color y el
  diseño de imagen** de OPM.
  · Entrevista completa leída: [Yatta-Tachi, «Industry Interview: One-Punch
  Man's Shingo Natsume & Chikashi Kubota» (2016)](https://yattatachi.com/one-punch-man-interview) ✅
- **Cita textual de Kubota** (tuit suyo del 26-oct-2015, citado en la misma
  entrevista): mucha gente cree que la calidad de la animación depende del
  presupuesto, pero **en Japón casi todos los animes de TV tienen presupuestos
  parecidos**; lo que cambia es **el esfuerzo del equipo**. Natsume añade que
  tuvieron un staff «muy apasionado, no motivado por el dinero», que
  sacrificó vida personal por la serie. ✅
- **Cita textual de Natsume** sobre dibujar a Saitama: «*As simplistic as
  Saitama is, he is a lot more difficult to draw than what we would think.
  His facial expressions are a difficult part... if you make a mistake, it is
  so obvious.*» Y sobre el detalle: querían que se vieran **las arrugas del
  guante cuando flexiona el brazo** y **el dibujo de la suela de sus botas**,
  desafiando la idea de que «meter mucho detalle es perder el tiempo». ✅
  (misma entrevista, primaria)
- Para las peleas, Natsume llamó a **especialistas en animación de acción**
  (animadores *sakuga* freelance, no fijos de un solo estudio) y llenaron el
  estudio de **libros de referencia y figuras de músculos flexionados** para
  acertar la anatomía en movimiento. ✅ (misma entrevista)
- **Animador destacado**: Yutaka Nakamura, conocido por sus **fotogramas de
  impacto** (*impact frames*), manchurrones tipo *sumi-e*, poses extremas y
  cámaras «locas»; trabajó en las escenas de acción de OPM.
  · [Wikipedia, Yutaka Nakamura](https://en.wikipedia.org/wiki/Yutaka_Nakamura) ·
  corroborado por los hilos de Reddit ya guardados en `datos-voz.md`
  («Boros vs Saitama», 269 votos; «Season 2 Best Detailed Drawing Scene»,
  1851 votos). ✅
- **Temporada 2 (2019)**: cambio de estudio a **J.C. Staff** (Madhouse tenía
  la agenda llena); fans y prensa notaron **menos fluidez** y criticaron el
  **CGI mal integrado** —fondos en CGI y partes cibernéticas de Genos que no
  encajaban con el 2D—. J.C. Staff sacó 8 animes ese año 2019 (posible causa).
  · [ScreenRant](https://screenrant.com/one-punch-man-anime-season-3-studio-failure/) ·
  [CBR](https://www.cbr.com/one-punch-man-season-3-worst-animation-ever/) ✅ (dos fuentes)
- **Temporada 3 (2025-26)**: mismo estudio, **J.C. Staff**; la crítica la
  llamó «la peor animación de la industria» en su estreno; el director sufrió
  acoso y **cerró sus redes sociales**; varios artículos apuntan a un problema
  más amplio del sector (estudios sobrecargados), no sólo a J.C. Staff.
  · [Yahoo/IMDb](https://www.yahoo.com/entertainment/one-punch-man-announces-season-115744930.html) ·
  [Gulf News](https://gulfnews.com/entertainment/one-punch-man-director-deletes-social-media-amid-brutal-season-3-backlash-i-will-not-forgive-1.500318231) ✅

### 18.3 · Cómo replicarlo en Photoshop (2D, para texturas y pósters) ✅ / propuesta razonada
- **Línea**: pincel redondo duro con ancho por presión (fino en curvas,
  grueso al cerrar contornos), en capa «Línea» aparte en modo Multiplicar —
  así se comporta la tinta de Murata (trazo muy contrastado, negro puro).
- **Sombreado**: **plano, de bordes duros** (no aerógrafo) en una capa
  «Sombra» en Multiplicar al 60-70%, tono violeta-grisáceo frío — así es el
  cel-shading de las capturas del juego de PS4/PC que medí arriba (líneas de
  sombra rectas, no degradados suaves). El degradado suave sólo va en pelo y
  efectos de energía (visto en el resplandor amarillo del disparo de Genos).
- **Tramas del manga**: para el punteado/trama de Murata (double-page
  spreads muy detallados), usar `Filtro > Pixelar > Semitono de color` de
  Photoshop, o un pack de pinceles de trama de manga gratuito (búsqueda
  recomendada, no encontré uno con licencia específica de OPM: sirve
  cualquier pack CC0 de tramas de puntos). ⚠️ recomendación general, no
  verificada contra un pincel concreto.

### 18.4 · Cómo replicarlo en Blender (3D, para objetos y personajes de la lámina) ✅
- **Modelos y *rigs* libres** (Sketchfab, CC):
  - **Saitama** — modelado, *rigged*, texturizado y posado en Blender por
    **Godfrey (SteamySenpai)**: https://sketchfab.com/3d-models/saitama-1c6ca849e4f04878959cbaa81401b403
  - **Genos (Demon Cyborg)** — mismo autor, mismo flujo en Blender:
    https://sketchfab.com/3d-models/genos-058940cf9b3d4c80bd29713805988c18
  - **Saitama (revisado)** por MMKH, esqueleto con Human IK de Maya (sirve de
    referencia de huesos si se reimporta):
    https://sketchfab.com/3d-models/saitama-one-punch-man-revised-5933d345ad9441d499c93eb655a9b214
  - Licencia de cada uno: **comprobar en su página** antes de usar (Sketchfab
    marca «Downloadable» pero la licencia exacta —CC BY, CC0, «sólo
    referencia»— varía por modelo; no la doy por hecha sin abrir la ficha).
    ⚠️ licencia por confirmar en el redactor/imagen antes de usarlos para
    render final, no sólo de referencia.
  - Garou (forma cósmica) y Boros (forma final) ya estaban en
    `partes/datos-imagen.md` (Sketchfab, CC Attribution): sirven para las
    escenas de villano.
- **Sombreado tipo cel** (Eevee, Blender 3.6+): nodo **Shader to RGB** →
  **Color Ramp** en interpolación **Constante**; dos paradas = blanco/negro
  clásico de dos tonos; tres paradas = una banda media (para la piel y el
  traje amarillo de Saitama, que en el manga lleva sombra a dos niveles).
- **Contorno** (tres formas, de más simple a más fiel):
  1. **Solidify**: material de contorno con *Backface Culling*, modificador
     Solidify con grosor ~0.01, normales invertidas, asignado por
     *Material Offset* — la más rápida, vale para props (el volante de héroe,
     la caja de fideos).
  2. **Freestyle** (pestaña Render): contorno de grosor variable, más
     parecido al trazo de tinta de Murata (más grueso en los pliegues del
     traje, más fino en la cara).
  3. **Line Art** (modificador *grease pencil*, Blender 2.93+): el más
     cercano a un entintado a mano; recomendable para un plano cercano de la
     cara de un personaje.
- **Luz y render**: una luz clave dura + un relleno ambiental mínimo, sombras
  duras y contraste alto (así se ve el traje de Saitama en el arte oficial:
  sombra plana bajo el cuello, sin degradado); usar Eevee (tiempo real) en
  vez de Cycles para mantener el look plano de cel-shading.
- **Texturas encima**: el logo/emblema de la Asociación de Héroes y el
  «正義執行» del traje (§6.1 de la biblia) sirven como *decal* pintado sobre
  el material, no como textura difusa base.

### 18.5 · Encuadres y composición típicos, por emoción ✅
- **Momento cómico/decepción (Saitama)**: plano medio o general, **estático**,
  personaje centrado sobre **fondo vacío o muy simple** (espacio negativo) —
  refleja su cara sin expresión. Ya está documentado en la biblia §7 con el
  papel del examen de héroe («C-rank, 71/100», Saitama con cara de fastidio):
  mismo patrón de encuadre plano y sin dramatismo.
- **Revelación de amenaza / villano poderoso**: **contrapicado extremo**
  («ojo de gusano») + luz de contraluz que lo convierte en silueta, para que
  parezca gigantesco — se ve directamente en la captura del jefe «Beast King»
  de *One-Punch Man: World* (arriba, punto 11-C): la cámara está a ras de
  suelo mirando hacia arriba.
- **El puñetazo en sí**: un **fotograma de impacto** —una sola imagen plana,
  de altísimo contraste (casi sólo blanco/negro/rojo), con líneas de
  velocidad radiales— que rompe el estilo normal de sombreado por un
  instante. Es la firma de la serie según los propios fans: el hilo de
  Reddit «Boros vs Saitama» (269 votos, guardado en `datos-voz.md`) lo señala
  como de los mejores momentos de animación de la serie. ✅
- **Peleas secundarias (Genos, etc.)**: composición **diagonal**, estelas de
  motion-blur, cámara siguiendo el proyectil — visto directamente en la
  captura de Genos contra Speed-o-Sound Sonic (punto 11-A).

## Hallazgos · Punto 24 · Obras parecidas y temas relacionados (sección 25 de la biblia, vacía)

- **Recomendaciones de AniList** (algoritmo + votos de usuarios, ya en
  `datos-texto.md`, no repetido): la más votada con diferencia es
  ***Mob Psycho 100*** (I, II y III) — **escrita por el mismo ONE**, incluso
  más cercana en tono que Dragon Ball. Le siguen *My Hero Academia*,
  *The Disastrous Life of Saiki K.*, *Tiger & Bunny*, *JUJUTSU KAISEN*,
  *Dragon Ball Z*, *Gintama*, *Kaiju No. 8*. · [AniList](https://anilist.co/anime/21087) ✅
- **A quién parodia Saitama, según el propio ONE**: creó a Saitama para
  **parodiar a los guerreros todopoderosos tipo Goku**, haciéndolo «más
  fuerte que todos ellos, hasta dar risa». · reportado por
  [Anime Explained](https://www.animeexplained.com/news/interview-with-one-punch-man-author-one-on-his-new-series-versus/)
  citando una entrevista de *Tokyo Reimei Note*. ⚠️ una sola fuente (no pude
  abrir la entrevista original: itechpost.com y cbr.com bloquearon la carga).
- **La inspiración de Murata como dibujante**: cita a **Akira Toriyama**
  (Dragon Ball) como una de sus mayores influencias; sus viñetas favoritas
  son las peleas de **Goku contra Piccolo y Freezer**. · reportado por
  [ComicBook.com](https://comicbook.com/anime/news/one-punch-man-saitama-versus-goku-fight/). ⚠️ una sola fuente (mismo bloqueo al intentar
  la fuente primaria).
- **La inspiración del director de la T1**: Shingo Natsume dice que
  ***Space Dandy*** influyó directamente en el color y diseño de imagen del
  anime (dato ya citado arriba en 18.2, con la entrevista primaria completa
  leída). ✅
- **Qué láminas vecinas del servidor no repetir**: ***My Hero Academia***
  (encargo 25) ya tiene su biblia terminada y va al canal
  `#material-de-clase`, con el recurso visual de «el cuaderno de héroe» y la
  letra de Deku a mano (`biblias/25-my-hero-academia/biblia.md`, secc. 0 y 7).
  Si a One Punch Man le toca un canal de temática parecida (acción/cómic),
  **conviene no repetir el cuaderno**: mejor un objeto propio de OPM (el
  volante de héroe C-class, la bolsa de la compra, el cupón de descuento).
  · comprobado leyendo esa biblia directamente. ✅
- **TV Tropes**: existe página (`Manga/OnePunchMan`) pero **Cloudflare la
  bloqueó** en los dos intentos (fetch directo y con user-agent de
  navegador): no es que no exista, es que no pude leerla. ⚠️

## Hallazgos · Punto 25 · El mundo, la historia y sus símbolos (sección 26 de la biblia, vacía)

### 25.1 · Las reglas del mundo, en cinco líneas ✅
1. La Tierra sufre la aparición cada vez más frecuente de **«Seres
   Misteriosos»** (monstruos): cualquier humano puede convertirse en uno por
   un deseo obsesivo, un complejo o el hastío de sí mismo (según la teoría
   del Dr. Genus, dentro de la propia historia). · [wiki, «Mysterious
   Beings»](https://onepunchman.fandom.com/wiki/Mysterious_Beings) ✅
2. La **Asociación de Héroes** (ヒーロー協会) es **privada**, no del
   gobierno: la fundó el multimillonario Agoni después de que un
   transeúnte salvara a su nieto de un monstruo. Clasifica a los héroes en
   cuatro clases con rango numerado dentro de cada una: **C, B, A, S**. ·
   [wiki, «Heroes/Hero Association»](https://onepunchman.fandom.com/wiki/Heroes/Hero_Association) ✅
3. Las amenazas se miden en **Nivel de Desastre**: **Lobo < Tigre < Demonio
   < Dragón < Dios** («Dragón o superior» es una categoría especial para
   amenazas cósmicas como Boros). Un aviso anuncia el nivel y decide qué
   héroes deben responder. · [wiki, «Disaster Level»](https://onepunchman.fandom.com/wiki/Disaster_Level) ✅
4. Las ciudades llevan **una letra** (Z-City, A-City…). **Z-City** tiene un
   «pueblo fantasma» en ruinas donde viven Saitama y Genos, lleno de
   monstruos pero libre de alquiler; **A-City** es la sede de la Asociación.
   · [wiki, «Z-City»](https://onepunchman.fandom.com/wiki/Z-City) ✅
5. Dentro de la Asociación hay **facciones**: el **Grupo Fubuki** (Blizzard
   Group), ~35 miembros de clase B con traje de oficina; más tarde aparecen
   los **Neo Héroes**, un grupo rival que dice «mostrar al mundo el
   verdadero heroísmo» porque la Asociación es «corrupta», pero resulta ser
   siniestro. · [wiki, «Blizzard Group»](https://onepunchman.fandom.com/wiki/Blizzard_Group) y
   [«Heroes/Neo Heroes»](https://onepunchman.fandom.com/wiki/Heroes/Neo_Heroes) ✅

### 25.2 · La historia por arcos ✅ (con el aviso de la propia wiki: nombres no oficiales, hechos por fans para ordenar la serie)

**Saga de introducción**
- *Saitama Introduction* (ep. 1): Saitama derrota al Cangrejo Mutante y
  conoce a Genos.
- *House of Evolution* (ep. 2-3): Genos se hace su discípulo; pelean contra
  el Dr. Genus y sus monstruos creados en laboratorio.
- *Paradise Group* (ep. 4): banda criminal potenciada por drogas.

**Saga de la Asociación de Héroes**
- *National Superhero Registry* (ep. 5-6): examen de héroe (Saitama saca
  71/100 y entra en clase C; Genos, pleno, entra en clase S).
- *Rumored Monster* (ep. 6) → *Giant Meteor* (ep. 7) → *Sea Monster*
  (ep. 8-9, el Rey del Mar Profundo) → ***Alien Conquerors*** (ep. 10-12,
  **Boros y los Ladrones de Materia Oscura invaden la Tierra**: el clímax de
  la T1) → *King* (ep. 13, episodio de puro alivio cómico con «King»).

**Saga del monstruo humano** (T2 + manga)
- *Garou Introduction* → *The Blizzard Group* → *Hero Hunt* → *Monster Raid*
  → *Super Fight* → ***Monster Association*** (Garou se vuelve el «Cazador de
  Héroes»; la Asociación de Monstruos secuestra niños con poderes: la
  columna vertebral de la T2).

**Saga de los Neo Héroes** (sólo en manga, todavía sin animar)
- *Psychic Sisters* → *Neo Heroes Introduction* → *Cruel Dragon* → *Ninjas*
  → *Supreme Hero* → *Neo Heroes Uprising* → *Robot Invasion* (la más
  reciente).
- Fuente de toda la lista: [wiki, «Story Arcs»](https://onepunchman.fandom.com/wiki/Story_Arcs) ✅
  (contrastada con la propia numeración de capítulos/episodios que trae la
  página, capítulo a capítulo).

### 25.3 · Emblemas, objetos icónicos y vocabulario propio ✅
- **Emblema de la Asociación de Héroes**: insignia circular con **alas** y la
  palabra «**HERO**» (`Herobadge.png` en la wiki); aparece de marca de agua
  en los avisos oficiales y en la interfaz del juego de PS4/PC (punto 11-A).
- **Emblema de los Neo Héroes**: tiene **dos versiones distintas** (una para
  el webcómic, otra para el manga) — dato útil para no mezclar cuál usar
  según qué versión de la historia cite el canal. · [wiki, «Heroes/Neo
  Heroes»](https://onepunchman.fandom.com/wiki/Heroes/Neo_Heroes) ✅
- **Uniforme del Grupo Fubuki**: traje de oficina negro con camisa blanca
  (también las chicas), en vez del típico traje de spandex de superhéroe —
  un contraste visual fuerte y fácil de dibujar.
- **Objetos icónicos de Saitama**: el traje amarillo con capa blanca y
  guantes/botas rojos **comprado en una tienda de descuento** (chiste
  recurrente: no es un traje de superhéroe de verdad); su **calvicie**
  (el precio literal de su entrenamiento); los **cupones y volantes de
  ofertas** que persigue por toda la ciudad; su alias no querido, **«Caped
  Baldy»** (ハゲマント). El **machete de bolsa de la compra** de la
  colaboración con PUBG Mobile (punto 6) confirma que ese objeto cotidiano
  ya se reconoce como icónico fuera de la serie.
- **Objetos de Genos**: sus brazos intercambiables (cada set tiene su propia
  habilidad); el de **Mumen Rider**: su bicicleta corriente, símbolo de
  «héroe sin poderes».
- **Vocabulario que un fan reconoce al instante**: «**Class S**», «**Disaster
  Level**» (Lobo/Tigre/Demonio/Dragón/Dios), «**One Punch**», «**Caped
  Baldy**», «**Hero Association**» — se usan como abreviaturas y memes fuera
  de la serie (se repiten en los títulos de los hilos de Reddit guardados en
  `datos-voz.md`, p. ej. «S-Class», «Disaster Level»).

## Lo mejor para la lámina

1. La **ficha de héroe con banda negra inclinada y filetes plateados** (ya en
   la biblia, §7) sigue siendo el mejor «cuadro de diálogo»; combínala con el
   **emblema circular alado** de la Asociación como marca de agua de fondo.
2. Para un canal de videojuegos o retos: el panel **rojo con esquinas
   redondeadas** de *One-Punch Man: World* (HP + contador de golpes) es un
   marco de texto ya hecho y reconocible sin ser genérico.
3. El **contraste de encuadre** (plano fijo y vacío para el chiste / contrapicado
   extremo para la amenaza / fotograma de impacto plano para el golpe) es la
   guía de composición más útil: elegir uno según la emoción del texto del
   canal.
4. En Blender: los *rigs* de Saitama y Genos de Godfrey (SteamySenpai) en
   Sketchfab, con contorno por **Freestyle** (más fiel al trazo de Murata que
   el Solidify simple).
5. El **machete-bolsa-de-la-compra** y el **volante del examen de héroe** son
   objetos cotidianos-icónicos perfectos para un prop de Blender (encargo:
   «el objeto real en un sitio real»).

## No encontré

- Interior escaneado de los tomos de **Ivrea** (letra de los globos en la
  edición española) — sólo fichas de venta. Búsquedas: «One Punch Man Ivrea
  tomo interior scan globo letra español manga» (español).
- **Menú/interfaz real** del evento PUBG Mobile × OPM (sólo vi el cartel
  promocional). Búsqueda: «PUBG Mobile One Punch Man collaboration 2026
  interface screenshot skin menu» (inglés).
- Interfaz de ***Road to Hero* / *Road to Hero 2.0***. Búsqueda ya hecha en la
  pasada anterior (registrada en `datos-texto.md`).
- Página de **The Cutting Room Floor** para cualquier juego de OPM: comprobado
  con la búsqueda del propio sitio, 0 resultados.
- Confirmación **primaria** (no de agregador) de que Murata usa Clip Studio
  Paint, y de las citas de ONE/Murata sobre Dragon Ball: los artículos
  originales (itechpost.com, cbr.com, CLIP STUDIO ASK) bloquearon la carga
  del contenido (verificación en JS o control anti-bot). Marcado con ⚠️.
- Página de **TV Tropes** para One Punch Man: existe pero Cloudflare bloqueó
  los dos intentos de lectura.

## Bitácora de búsqueda (este pase)

- **Wiki de Fandom (`onepunchman.fandom.com`), inglés**, por API
  (`action=parse&prop=wikitext`): «Disaster Level», «Heroes/Hero
  Association», «Story Arcs» (pageid 6341, saga por saga), «Mysterious
  Beings» (orígenes + niveles de desastre), «Z-City», «Heroes/Neo Heroes»,
  «Blizzard Group», búsqueda de texto «Threat Level», «Story Arcs», «Z-City».
- **AniList**: datos ya traídos por `recolectar.py` (`datos-texto.md`), sólo
  releídos y organizados, sin repetir la consulta.
- **WebSearch (inglés)**: «Yusuke Murata art style interview Clip Studio Paint
  One Punch Man drawing process», «One Punch Man season 3 2025 studio
  animation which studio», «One Punch Man season 2 JC Staff CGI 3D animation
  criticism digital compositing», «"One Punch Man" Sketchfab Saitama OR Genos
  free rig download», «"One Punch Man" tcrf.net cutting room floor», «"One
  Punch Man World" Netmarble game 2025 interface screenshots», «Blender toon
  shader Freestyle Solidify anime outline tutorial 2D style rendering»,
  «"One Punch Man: The Strongest" mobile game gacha interface UI screenshots
  2026», «ONE mangaka artist simple art style Paint interview One Punch Man
  original webcomic», «sakuga blog "One Punch Man" animation analysis Yutaka
  Nakamura episode 3», «Yusuke Murata Wacom Cintiq Clip Studio Paint interview
  digital tools», «"Murata" mangaka interview draws manga digitally tablet
  program name», «ONE creator interview Dragon Ball inspiration parody
  One-Punch Man influences», «Shingo Natsume director One Punch Man interview
  animation approach comedy contrast static wide shot», «PUBG Mobile One
  Punch Man collaboration 2026 interface screenshot skin menu».
- **Español**: «One Punch Man Ivrea tomo interior scan globo letra español
  manga».
- **Sitios leídos directamente** (curl, con user-agent de navegador cuando
  hizo falta): `ask.clip-studio.com` (bloqueado, SPA en JS), `tvtropes.org`
  (bloqueado, Cloudflare), `animenewsnetwork.com` (bloqueado en el intento de
  leer el artículo de 2015, «Security check»), `screenrant.com`/`cbr.com`
  (falló la carga con curl), `yattatachi.com` (✅ leído completo, entrevista
  primaria de 2016), `itechpost.com` (cargó pero sólo JS, sin texto),
  `tcrf.net` (búsqueda directa del sitio, 0 resultados para «One Punch Man»).
- **Steam** (`store.steampowered.com`, capturas ya traídas por
  `recolectar.py`): 3 capturas de *A Hero Nobody Knows* descargadas, miradas
  con Read y medidas con `herramientas/estilo.py`.
- **Google Play** (`play.google.com/store/apps/details?id=com.onepunchman.ggplay.sea`):
  HTML leído para sacar URLs de capturas reales (`=w1052-h592`), 2 miradas
  con Read.
- **mobi.gg**: página de capturas de *One-Punch Man: World*, 2 imágenes
  bajadas y miradas.
- **gamingonphone.com**: artículo de la colaboración PUBG Mobile, 1 imagen
  promocional bajada y mirada.
