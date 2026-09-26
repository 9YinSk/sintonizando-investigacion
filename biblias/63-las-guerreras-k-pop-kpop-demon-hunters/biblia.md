---
tags: [biblia, serie, laminas, biblioteca]
serie: "Las Guerreras K-pop (KPop Demon Hunters), Sony Pictures Animation / Netflix, 2025"
canal: "sin canal: propuesta #🎼・demos-canto (alternativas 🎭・Escenario y #😂・memes, ver §0)"
fecha: 2026-09-25
---

# Biblia · Las Guerreras K-pop (KPop Demon Hunters) — para la biblioteca

> [!important] Cómo se hizo, y sus límites
> - La escribió el **redactor** sólo con las partes del equipo
>   (`partes/imagen.md`, `video.md`, `voz.md`, `texto.md` y, para
>   completar, los `datos-*.md` y los `.json`). Nada nuevo sin fuente.
> - **Es una película** (1:39:37), no una serie: no hay opening, ending ni
>   capítulos. Los minutos son **del clip citado** (tráiler oficial y los
>   *lyric videos* oficiales de Sony Animation, que llevan metraje real),
>   no de la película entera.
> - **YouTube pidió iniciar sesión**. Los vídeos se miraron en
>   **Dailymotion** e **Internet Archive**, a 720p. Hay capturas 4K de la
>   wiki (hasta 6464×3630), pero sin minuto.
> - **Doblaje latino** (Argentina): 6 muestras oficiales de Doblaje Wiki
>   pasadas por `voz.py` (Whisper). No hay clips oficiales doblados en
>   Dailymotion ni en Internet Archive.
> - El redactor **miró las 3 hojas de `hojas/` número a número** y
>   corrigió varias cosas de las partes (la más importante: el traje
>   «Free» de Rumi **no** es la cazadora amarilla). Está todo en §28.
> - ✅ = dos fuentes o visto por nosotros. ⚠️ = una sola fuente, o algo
>   que hay que comprobar. Lo que falta está en §28 y en la tabla final.
> - **Hubo una segunda sesión del redactor** (modo «seguir», 25-sep): la
>   primera se cortó tras §5. Ver el apartado de abajo.

## Segunda pasada · qué cambió

- **Antes**: la biblia llegaba hasta §5 (419 líneas, 16 ⚠️), sin
  `referencias.json`, sin conceptos, sin tabla y sin bitácora.
- **Ahora**: escritas §6 a §29, la tabla «Cumplimiento del encargo» y la
  bitácora. `referencias.json` armado con `juntar_referencias.py` (174) y
  12 más del redactor, sacadas de las hojas con su tamaño medido por la
  API de la wiki (186 en total).
- **Corregido**: en `referencias.json`, el traje «Free» de Rumi decía
  «cazadora amarilla»; es la **sudadera lila con vaqueros** (hoja
  `personajes_01`, nº 6). Las demás correcciones de las partes, en §28.
- **Mismas fuentes**: no se buscaron datos nuevos. Todo sale de las
  cuatro partes y de las tres hojas, que el redactor volvió a mirar. La
  API de la wiki sólo se usó para el enlace de esas 12 imágenes.

## Índice

- 0 · Sin canal: dónde encaja mejor
- 1 · Resumen para quien tenga prisa
- 2 · Las escenas que sirven, con minuto (punto 2)
- 3 · Arte oficial y hojas de contacto (punto 1)
- 4 · Fan art y 3D, sólo como referencia (punto 3)
- 5 · Sitios, luz, paleta y texturas reales (punto 4)
- 6 · Tipografía: una letra para cada uso (punto 5)
- 7 · Cómo hablan en pantalla: el cuadro de diálogo (punto 6)
- 8 · Los personajes a fondo: carácter, cara y dinámicas (punto 13)
- 9 · ¿Quién es el más querido? (punto 7)
- 10 · Doblaje latino y frases textuales (punto 8)
- 11 · Música y sonido (punto 9)
- 12 · Vídeos y tendencias (punto 10)
- 13 · Videojuegos de la franquicia (punto 11)
- 14 · Lo que ama el fandom, y qué NO hacer (punto 12)
- 15 · Poses analizadas por personaje (punto 14)
- 16 · Vestuario, con hex medidos (punto 15)
- 17 · Ciudades, paisajes y fondos de pantalla (punto 16)
- 18 · Guía para generar con IA: imagen y texto (punto 17)
- 19 · Estilo de dibujo, técnica, Photoshop y Blender (punto 18)
- 20 · Texturas 2D (punto 19)
- 21 · Gustos y detalles de cada personaje (punto 20)
- 22 · Por qué la gente la ama, y las escenas que hacen llorar (punto 21)
- 23 · Fan dubs y comunidad hispana (punto 22)
- 24 · Colaboraciones, figuras y cosplay (punto 23)
- 25 · Obras parecidas y láminas vecinas (punto 24)
- 26 · El mundo, la historia por arcos y sus símbolos (punto 25)
- 27 · Tres conceptos de lámina
- 28 · Lo que no pude verificar, y lo que corregí de las partes
- Cumplimiento del encargo
- 29 · Bitácora de búsqueda

## 0 · Sin canal: dónde encaja mejor

El encargo dice por qué está: **fenómeno musical reciente**. Las partes
lo concretan en cuatro datos que tocan de lleno a este servidor:

1. **Es un musical sobre la voz.** Tres cantantes protegen el mundo
   cantando: su voz sostiene el **Honmoon**, la barrera contra los
   demonios ([wiki, Honmoon](https://kpop-demon-hunters.fandom.com/wiki/Honmoon)).
   El conflicto de Rumi es que **su voz se rompe** y se cura
   ([wiki, Rumi](https://kpop-demon-hunters.fandom.com/wiki/Rumi)). ✅
2. **En el doblaje latino, las mismas actrices hablan y cantan.** En el
   original cada una tiene una voz para hablar y otra para cantar; en
   latino sólo Celine tiene dos
   ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Las_guerreras_k-pop)). ✅
   Es el dato más útil para un servidor de doblaje **y** canto.
3. **«Golden» fue nº1 del Billboard Hot 100** al menos 8 semanas
   ([Billboard](https://www.billboard.com/lists/huntr-x-golden-number-one-hot-100-eighth-week/)),
   y hubo **funciones para cantar en el cine** (*sing-along*)
   ([The Hollywood Reporter](https://www.hollywoodreporter.com/movies/movie-news/kpop-demon-hunters-sing-along-box-office-first-netflix-win-1236352043/)). ✅
4. **Es la película más vista de la historia de Netflix**
   ([Netflix Tudum](https://www.netflix.com/tudum/articles/kpop-demon-hunters-most-popular-netflix-film)). ✅

**Propuesta** (mirando `servidor/inventario.md`):

| Canal | Qué dice el inventario | Por qué encaja | Concepto |
|---|---|---|---|
| `#🎼・demos-canto` ⭐ | «Tu ficha de CANTO, aparte de la de doblaje: un hilo con tu registro y tus covers.» | Rumi es la vocalista; su arco es su voz. La cabina de grabación de la HUNTR/X Tower existe en la película | A (§27) |
| `🎭・Escenario` | «Charlas, entrevistas y directos. Sube quien invita el anfitrion.» | Los **Idol Awards** tienen anfitrión (en latino lo dobla Hernán Tracchia). Es el escenario del clímax | B (§27) |
| `#😂・memes` | «El meme, sin más. Si lo doblas, va a fandub-de-memes.» | El fandom vive de memes: los tres sabores de ramyeon y «No thoughts, only Derpy» | C (§27) |

- Alternativas en una línea: `#🪪・presentaciones` (una *photocard*
  firmada en un *fansign*, con Zoey) y `🎶・Karaoke` (el *sing-along*).
- **Nota de choque** (no bloquea nada, decisión del 25-sep):
  `#🎼・demos-canto` lo propuso Bocchi; `🎭・Escenario` y `🎶・Karaoke`,
  *Sing* (biblia 29) y Saint Seiya (39); `#🪪・presentaciones`, Encanto,
  Spy x Family, Kung Fu Panda y Steven Universe.

## 1 · Resumen para quien tenga prisa

- **Qué es.** Película de animación 3D de **Sony Pictures Animation**
  para **Netflix**, dirigida por **Maggie Kang** y **Chris Appelhans**,
  estrenada el **20-jun-2025**, 1:39:37
  ([wiki, ficha del film](https://kpop-demon-hunters.fandom.com/wiki/KPop_Demon_Hunters_(Film))). ✅
- **Título latino: «Las Guerreras K-Pop».** Sin «cazadoras» ni
  «demonios». Un fan lo nota al instante (§14). ✅
- **De qué va.** HUNTR/X (Rumi, Mira y Zoey) son ídolos del K-pop y, en
  secreto, cazadoras de demonios. Su voz mantiene el Honmoon. Llega un
  grupo rival, los **Saja Boys**, que son demonios disfrazados, con
  **Jinu** al frente. Rumi esconde que es medio demonio (§26).
- **Más querido.** **Rumi**: 1.ª en el ranking de Collider y la «más
  identificable» en Reddit, con **Mira** muy cerca. El secundario que
  sorprende es **Bobby**, el mánager, por delante de Jinu. El meme más
  querido: **Derpy**, el tigre azul (§9, §14).
- **Cuadro de diálogo propio.** No hay globos: es cine. La película
  «habla» con **grafismo de concierto** (letras grandes que laten con la
  música: «I'M GONNA SHOW YOU», «UP UP UP») y, en lo íntimo, con **letra
  a mano en el vaho de un espejo**. Más el subtítulo de Netflix (§7).
- **Letras libres comprobadas** (tildes, ñ, ¿ y ¡ con fontTools):
  **Hunters K-Pop** (título), **Anton** (grito de concierto), **Caveat**
  (pensamiento), **Roboto** (subtítulo), **Noto Sans KR** (hangul),
  **Permanent Marker** (Saja Boys) (§6).
- **Paleta.** Neón **verde** para el mundo demonio (`#A0B481`),
  **magenta** para los Saja Boys (`#FC02A5`), **dorado y rojo** para el
  triunfo (`#E0C66B`, `#793121`), **lavanda** para el final (`#ECD4FC`),
  **azul** para el Honmoon (`#1D579B`) (§5).
- **Lo mejor para la lámina.**
  - Rumi escribiendo en el espejo empañado del Han Clinic («Golden»
    1:48): texto íntimo real, no una burbuja.
  - Rumi sola en el escenario de los Idol Awards, brazos en «V», letrero
    «UP UP UP» («Golden» 2:12): triunfo.
  - El trío con sus tres armas de luz sobre niebla verde (tráiler 0:24).
  - El logo holográfico de HUNTR/X, para decorar un objeto en Blender.
  - La frase latina de Rumi: «…de alguna forma mi voz estuvo sanando».

## 2 · Las escenas que sirven, con minuto (punto 2)

Miradas fotograma a fotograma con `fotogramas.py` por el investigador de
vídeo. **Los minutos son del clip**, no de la película. Los clips:

- **Tráiler oficial de Netflix** (2:43), copia en Dailymotion:
  [x9k1104](https://www.dailymotion.com/video/x9k1104). ✅
- ***Lyric videos* oficiales de Sony Animation** en Internet Archive, con
  metraje real de la película:
  [«How It's Done»](https://archive.org/details/youtube-QGsevnbItdU),
  [«Soda Pop»](https://archive.org/details/youtube-983bBbJx0Mk),
  [«Golden»](https://archive.org/details/golden-official-lyric-video-kpop-demon-hunters-sony-animation_202511)
  y [«Takedown»](https://archive.org/details/youtube-l8Dr7vzMSVE). ✅

| Clip · minuto | Qué se ve | Para qué sirve | Estado |
|---|---|---|---|
| Tráiler [0:00](https://www.dailymotion.com/video/x9k1104?t=0) | Tres maniquíes con el vestuario de HUNTR/X en el armario | Objeto real: el armario de la torre | ✅ |
| Tráiler [0:08](https://www.dailymotion.com/video/x9k1104?t=8) | Rumi canta a cámara, plano muy cerrado, luz violeta y verde azulada | Cara cantando | ⚠️ |
| Tráiler [0:24](https://www.dailymotion.com/video/x9k1104?t=24) | **El trío en pose de batalla** con sus tres armas de luz (dagas de Zoey, espada de Rumi, gok-do de Mira), niebla verde neón | La imagen de acción más reconocible | ✅ |
| Tráiler [0:32](https://www.dailymotion.com/video/x9k1104?t=32) | Un demonio sale de un póster de «BOYS» y roba el alma a un peatón que mira el móvil (rayo cian por la boca) | Gag de robo de almas | ⚠️ |
| Tráiler [1:04](https://www.dailymotion.com/video/x9k1104?t=64) | Los Saja Boys en fila, sombreros negros, a contraluz azul | Presentación del grupo rival | ✅ |
| Tráiler [1:20](https://www.dailymotion.com/video/x9k1104?t=80) | **Jinu** en primer plano: media sonrisa a cámara, chaqueta blanca a cuadros, pendiente, marca de demonio morada en el cuello | Jinu seductor | ✅ |
| Tráiler [1:36](https://www.dailymotion.com/video/x9k1104?t=96) | HUNTR/X en negro y dorado, luz rosa fuerte, público desenfocado | Concierto | ⚠️ |
| Tráiler [1:40](https://www.dailymotion.com/video/x9k1104?t=100) | Criatura pequeña en short blanco frente a tres siluetas, niebla verde-amarilla cenital | Gag cómico | ⚠️ |
| Tráiler 2:24 | Cartela «ONLY ON NETFLIX JUNE 20» | Tipografía de marketing | ✅ |
| «How It's Done» 0:06 | Selfie de las tres en la furgoneta; texto «50,000 fans are waiting for you» | Las tres juntas, casual | ✅ |
| «How It's Done» 0:12 | Pelea con un demonio morado grande y secuaces verdes entre bambalinas | Acción | ⚠️ |
| «How It's Done» 0:54 | **Trío con los puños en alto**, negro y dorado, letrero «I'M GONNA SHOW YOU» | Presentar en grupo | ✅ |
| «How It's Done» 1:06 | Zoey en primer plano con sus dagas turquesa; «HUNTRIX DON'T QUIT!» | Zoey desafiante | ✅ |
| «How It's Done» 2:48-2:54 | Pelea final en un puente o estación, atardecer naranja, neón azul y rojo | Acción en ciudad | ⚠️ |
| «Soda Pop» 0:12-0:48 | Debut de los Saja Boys en una calle de Seúl: humo magenta, multitud, un demonio escupe palomitas | Saja Boys en la calle | ✅ |
| «Golden» 0:24-0:30 | **Gwi-Ma** en su trono rojo y dorado, niebla verde, neón verde «HAH» | El villano | ⚠️ |
| «Golden» 1:48 | **Rumi ante el espejo del Han Clinic**, bata clara, marcas visibles; escribe en el vaho «Put these patterns all in the past now» | Texto íntimo | ✅ |
| «Golden» 2:12 | **Rumi sola en el escenario de los Idol Awards**, brazos en «V», letrero «UP UP UP», decorado de templo coreano | Triunfo | ✅ |
| «Golden» 3:00 | Seúl al atardecer con la Namsan Tower y ondas turquesa y rosa del Honmoon sobre la ciudad | Fondo | ✅ |
| «Golden» 3:02 | Las tres caminan juntas, blanco y dorado, luz lavanda | Cierre, unidad | ✅ |
| «Takedown» 0:30-1:00 | Jeongyeon, Jihyo y Chaeyoung (TWICE) grabando en estudio, alternado con HUNTR/X en el escenario («ROTTEN», «WORLD OF PAIN») | Estudio de grabación real | ✅ |
| «Takedown» 2:48 | Criatura celeste translúcida sobre negro | Sin identificar | ⚠️ |

**Capturas 4K sin minuto** (wiki de Fandom; tamaño medido por el
recolector), para cuando haga falta más resolución que 720p:

- [Mira y Rumi hablando en casa](https://static.wikia.nocookie.net/kpop-demon-hunters/images/9/98/Mira_and_Rumi_Conversation_1.webp),
  6464×3630 (hoja `personajes_01`, nº 1).
- [Rumi mira a Jinu en su cita](https://static.wikia.nocookie.net/kpop-demon-hunters/images/1/10/Rumi_looking_at_Jinu_meetup_scene_1.webp),
  4096×2304 (nº 11).
- [Rumi con la Saingeom en batalla](https://static.wikia.nocookie.net/kpop-demon-hunters/images/2/2e/Rumi_using_the_Saingeom_Sword_in_battle.png),
  4096×1733 (nº 15).
- [Rumi pacta con Jinu](https://static.wikia.nocookie.net/kpop-demon-hunters/images/9/9d/Rumi_makes_a_deal_with_Jinu.png),
  4096×1705 (nº 20), y
  [Jinu le cuenta que fue humano](https://static.wikia.nocookie.net/kpop-demon-hunters/images/d/d4/Jinu_reveals_that_he_was_once_human_to_Rumi.png),
  4096×1685 (nº 21).

⚠️ **No hay fotogramas propios en 1080p**: `fotogramas.py` baja a 720p.
Si hace falta un plano grande, el *scenepack* 4K de fans en
[Dailymotion](https://www.dailymotion.com/video/x9ohwu0) (2:38) sirve de
cantera. No usar las copias piratas de la película entera que aparecen
en Internet Archive.

## 3 · Arte oficial y hojas de contacto (punto 1)

### Libros y key art

- **Artbook oficial: *The Art of KPop Demon Hunters*** (Tracey
  Miller-Zarneke; Random House Worlds con Gallery Nucleus), 142-144
  páginas, más de 500 piezas: bocetos, estudios de personaje, arte final.
  La **edición Platinum** salió el 8-sep-2026 con cortes holográficos
  «Honmoon»
  ([Penguin Random House](https://www.penguinrandomhouse.com/books/837553/the-art-of-kpop-demon-hunters-by-tracey-miller-zarneke-and-random-house-worlds/),
  [Gallery Nucleus](https://www.gallerynucleus.com/detail/43364/)). ✅
- **Libro oficial de pósters**: más de 35 pósters, portada con *foil*
  ([Netflix Shop](https://www.netflix.shop/products/kpop-demon-hunters-the-official-poster-book)). ⚠️
- **Key art y tráiler**: nota de prensa de Netflix
  ([AWN](https://www.awn.com/news/netflix-debuts-kpop-demon-hunters-official-trailer-key-art)). ✅
- **La wiki de Fandom** tiene 813 imágenes en las fichas de los cuatro
  protagonistas; 478 grandes: renders 4K, retratos, hojas de vestuario
  por traje y arte conceptual firmado. ✅

### Quién dibujó qué (nombres de archivo de la wiki)

| Artista | Qué hay suyo | Dónde |
|---|---|---|
| **Simonbaek** | *Storyboards* de escenas clave (Rumi con Celine, el Honmoon roto, la tumba de la madre), versión de instituto de las chicas, portadas de revista «Hibiscus» | hoja `concept_02`, nº 59, 68-73, 94; `personajes_01`, nº 9-10 |
| **nachomolina** | Diseño de set y de efectos del Honmoon (Seúl de noche desde una colina) | `personajes_01`, nº 29-30 |
| **Mingjuechen** | Arte del Honmoon | ficha de Rumi |
| **Wendell** | Retrato de Jinu | `concept_02`, nº 60 |
| **Amithompson** | Ilustración de Rumi | `concept_02`, nº 57 |
| **Eunicho** | Efectos e invocación de la espada | `personajes_01`, nº 42; `vestuario_10`, nº 473 |

✅ (nombres vistos en las hojas; fichas de
[Rumi](https://kpop-demon-hunters.fandom.com/wiki/Rumi),
[Mira](https://kpop-demon-hunters.fandom.com/wiki/Mira),
[Zoey](https://kpop-demon-hunters.fandom.com/wiki/Zoey) y
[Jinu](https://kpop-demon-hunters.fandom.com/wiki/Jinu)).

### Las 3 hojas de `hojas/`, número a número

Montadas con `investigar_serie.py` sobre la wiki. **Miradas por el
redactor** una a una (corrige números de la parte de imagen, §28).

**`personajes_01.jpg`** (nº 1-48): poses vivas y producto.

| Nº | Qué es | Para qué |
|---|---|---|
| 1, 25, 26 | Mira y Rumi hablando en casa, en sudadera; Mira con el jersey de oso polar | Las chicas fuera del escenario |
| 2 | La espada **Saingeom**, dos fases | Objeto |
| 3 | **Zoey** render 4K: salto con sus *shin-kal* | Acción |
| 4 | Rumi, traje «What It Sounds Like» | Traje de gala lila |
| 5 | Rumi, traje «Takedown», con la espada | Traje oscuro |
| 6 | Rumi, traje «**Free**»: **sudadera lila y vaqueros**, de la mano de alguien | Rumi casual (no es la cazadora amarilla) |
| 7 | **Rumi** render de cazadora: espada en diagonal, pierna adelantada | Pelear |
| 8, 23 | **Mira** render 4K y cuerpo entero con el gok-do | Pelear, presentar |
| 11, 19, 20, 21 | Fotogramas 4K: Rumi y Jinu, Rumi y Celine | Escenas de diálogo |
| 12 | Zoey, traje dorado | Gala |
| 13-14 | Cajas Youtooz «Monitor Buddiez» (Jinu y Rumi; Mira y Zoey) | Figura chibi oficial |
| 15 | Rumi con la Saingeom en batalla, neón magenta | Acción |
| 16 | Mira retrato: top negro, falda naranja, gok-do | Presentar |
| 17 | **Rumi retrato: cazadora amarilla**, top corto, trenza | La ropa más reconocible |
| 18 | **Zoey retrato**: *shin-kal* en alto, top halter turquesa | Presentar, regañar |
| 22, 24 | Jinu: traje de *Play Games With Us* y traje «Soda Pop» | Jinu de ídolo |
| 27 | Arma de Mira (gok-do), diseño | Objeto |
| 29-30 | Seúl de noche con silueta en una colina (nachomolina) | Fondo |
| 31-33 | Autógrafos de Mira, Zoey (guiño) y Rumi con el logo HUNTR/X | Objeto firmado |
| 34-36 | Youtooz «figure and pin» de Rumi, Zoey y Mira, en dorado | Figura |
| 38 | Rumi en forma demonio, angustiada | Miedo |
| 39-40 | Rumi y Zoey, renders de los Idol Awards | Gala |
| 41 | Los Saja Boys en la tele | Pantalla |
| 44-45 | Fotogramas de Sony Animation (neón; Rumi con el puño en alto) | Acción |
| 46-48 | Merch de los Saja Boys (chapas, camiseta) | Producto |

**`concept_02.jpg`** (nº 49-96): estilo, gestos y símbolos.

| Nº | Qué es | Para qué |
|---|---|---|
| 49-53, 80-82 | Merch oficial: camisetas, pijama, pegatinas, taza, toalla | Qué no copiar (§14) |
| 54-55 | «Climax outfits»: color explosivo, 2D pintado | Efectos del clímax |
| 56, 74 | Rumi render normal y cuerpo entero: cazadora amarilla | Pose de pie |
| 58, 75 | Concept de los Saja Boys: ropa de calle pastel y **hanbok negro con *gat*** | Saja Boys |
| 60 | Retrato de Jinu (Wendell) | Jinu sonriente |
| 61 | Traje de inspiración tradicional (MAMA) | Gala coreana |
| 62 | Efectos de la espada, pintado encima | Luz de las armas |
| 63-67 | Fotogramas de Rumi: con la espada de luz, tumbada con un vaso de ramyeon «RUMI» | Rumi en casa y en acción |
| 68-73 | *Storyboards* de Simonbaek | Encuadres del estudio |
| 76-78 | Hojas de **invocación de armas por el Honmoon** (tambor, anillo con *shin-kal*, «sprites») con notas | Cómo aparecen las armas |
| 79 | La montaña con las caras de HUNTR/X y Saja Boys | Promo |
| 84 | **Las tres comiendo ramyeon**, vasos con su nombre | Concepto C |
| 85, 87, 88 | Rumi comiendo, cantando al micro, con un vaso | Rumi feliz |
| 86, 95 | Rumi y Mira, trajes dorados | Gala |
| 89 | Jinu con *gat*, luz magenta | Jinu demonio |
| 93 | **Zoey con «ojos de mazorca»** (gag chibi) | Vocabulario de gestos (§18) |
| 94 | Portadas de la revista «Hibiscus» con Mira | Objeto impreso |
| 96 | Pintura de color: ciudad de neón de los Saja Boys | Paleta de calle |

**`vestuario_10.jpg`** (nº 433-478): ropa de todos los días y caras.

| Nº | Qué es | Para qué |
|---|---|---|
| 433 | Rumi, cazadora amarilla, media sonrisa segura | Presentar |
| 435, 437 | Mira de incógnito: gorra, gafas, cara de desconfianza | Mira escéptica |
| 436, 453-455, 460 | Zoey disfrazada: sombrero amarillo, camisa floral | Zoey graciosa |
| 438 | Jinu «Your Idol»: silueta de *gat* y túnica negra | Jinu amenaza |
| 439, 462 | Rumi en bata, con el móvil | Rumi en casa |
| 440 | Zoey rapeando al micro | Zoey en escena |
| 441, 443-446 | Trajes dorados; Mira con chaqueta blanca y dorada | Gala |
| 448 | **Mira furiosa**: dientes apretados, puños | Rabia |
| 449 | Mira con fastidio | Regañar |
| 450-452 | Mira en bata y toalla: susto, relax, dormida en la bañera | Humor |
| 456 | Zoey en pijama | Casa |
| 457-459 | Zoey pícara, suplicando con las manos juntas, triste | Emociones |
| 461 | Zoey cantando «What It Sounds Like» | Alegría |
| 465 | Zoey deslumbrada | Asombro |
| 466 | Zoey abrazando el disco de las **Sunlight Sisters** | Fan |
| 470 | Mira en batalla, luz verde | Pelear |
| 471 | Rumi demonio en la oscuridad | Miedo |
| 474-475 | Rumi en sudadera rosa: boca abierta; con una caja | Sorpresa |
| 476 | HUNTR/X doradas | Grupo |
| 477 | **Rumi escribiendo la letra de «Takedown»** en un cuaderno | Concepto A |
| 478 | **Rumi comiendo kimbap** (meme) | Concepto C |

## 4 · Fan art y 3D, sólo como referencia (punto 3)

**Fan art mejor valorado** (Safebooru, con el autor original). Mirar,
nunca pegar; si se cita, con el nombre del autor. ✅

| Personaje | Imagen | Tamaño | Autor |
|---|---|---|---|
| Rumi | [safebooru 274/b2cc…](https://safebooru.org/images/274/b2cc64d7041764874da567ee977956f15e99366a.jpg) | 2160×2700 | [@nikkotari](https://twitter.com/nikkotari/status/1937224201108152333) |
| Rumi, Mira y Zoey | [safebooru 1811/452b…](https://safebooru.org/images/1811/452be493d468c8f6751e52159ebda4e82c9fe18f.jpg) | 1868×1751 | [@Kiioki11](https://twitter.com/Kiioki11/status/1938591331196064123) |
| Las tres | [safebooru 4370/e57b…](https://safebooru.org/images/4370/e57b7ec257f9021b280777c3a6b9139139395e26.jpg) | 1160×1240 | [@eni_ate](https://twitter.com/eni_ate/status/1937872983777026238) |
| Mira | [safebooru 1558/21b7…](https://safebooru.org/images/1558/21b7ec8c05defb2b3d1a26b381c3a75ce31011c0.jpg) | 1500×1500 | [@tlsskdydrkfl](https://twitter.com/tlsskdydrkfl/status/1949369642419728531) |
| Zoey | [safebooru 23/1b60…](https://safebooru.org/images/23/1b60ea23cab96e3bcc334b7fd9c93ed8051ae715.jpg) | 1639×2048 | [@rina4rt](https://twitter.com/rina4rt/status/1946228901505626314) |
| Jinu | [safebooru 1046/e932…](https://safebooru.org/images/1046/e93298a19a1bedf5c3833d3afc5f87349435ec01.jpg) | 817×1300 | [@antenna2667](https://twitter.com/antenna2667/status/1943626817098690975) |
| Jinu | [safebooru 4403/1c8b…](https://safebooru.org/images/4403/1c8b2ad465d2ade302b50bae8a919bd7775e4b87.png) | 1461×2048 | [l00llaby en Tumblr](https://l00llaby.tumblr.com/post/802510181526339584) |

**Modelos 3D con licencia libre** (Sketchfab). Todos son **de fans,
basados en las skins de Fortnite**, no de Netflix. Licencia visible en
cada ficha. ✅

| Modelo | Autor | Licencia | ♥ |
|---|---|---|---|
| [Zoey (Fortnite)](https://sketchfab.com/3d-models/none-aa3d9d519b34425ea5dd1456c4c67eaf) | Centrixe the Dodo | CC BY | 783 |
| [Rumi (Fortnite)](https://sketchfab.com/3d-models/none-61401e8d527044b3bba43925669300e6) | Centrixe the Dodo | CC BY | 688 |
| [Mira (Fortnite)](https://sketchfab.com/3d-models/none-7e5f6ef4b77e40f680e4eff68edaa8e1) | Centrixe the Dodo | CC BY | 576 |
| [Rumi](https://sketchfab.com/3d-models/none-7d608f6e55174d79a6a1ff128396c4b4), [Zoey](https://sketchfab.com/3d-models/none-12f3da007bd4495999904a6fac70b19b), [Mira](https://sketchfab.com/3d-models/none-39a41da507cb4570b2128d63449b59f9) | Guilherme Navarro | CC BY | 196 / 155 / 150 |
| [Arma de Mira (gok-do)](https://sketchfab.com/3d-models/none-eaa70194d746438c817706749eec880c) | Pursuits-Avenue | CC BY | 69 |
| [Rumi dorada](https://sketchfab.com/3d-models/none-2cfb56bdf919444f896a27280bf8f384) | elsafrozenaninationfans2013 | CC BY | 45 |
| [Rumi con las palmas juntas](https://sketchfab.com/3d-models/none-874791cc3bf5460e991bba4129f1bfd9) | XxDeafYesxx | CC BY | 27 |
| [Rumi](https://sketchfab.com/3d-models/none-a1b07ddc7a114ef8ab699fec49016666) | azzman__ | CC BY-NC-SA (no comercial) | 38 |
| [«Patterns» (marcas de demonio)](https://sketchfab.com/3d-models/none-547051dd1fcd4fcb95d6ccd5d0261c98) | MIKESTEEZ | CC BY | 102 |

- **Crédito exacto** para CC BY: «Modelo "<nombre>" de <autor>
  (Sketchfab), CC BY 4.0». ✅
- **Poly Haven no tiene nada de la serie** (es un banco genérico). Sus
  texturas de asfalto y ciudad nocturna sí valen de base. ⚠️ (búsqueda
  negativa hecha)
- ⚠️ La malla de ninguno se abrió en Blender: comprobar escala y
  *rig* antes de usarlo.

## 5 · Sitios, luz, paleta y texturas reales (punto 4)

**Los sitios de la película** (ficha del film en la wiki, «Locations»):
aldea de la era Joseon, Estadio Olímpico de Seúl, Mundo Demonio,
HUNTR/X Tower, COEX K-Pop Square, Han Clinic, calle Myeongdong, baños
públicos de hombres y de mujeres, aldea Bukchon Hanok, palacio
Gyeongbokgung, parque Naksan, línea 7 del metro, puente Cheongdam,
estación Jayang, Namsan Tower e isla de Jeju. ✅

**Paletas medidas con `estilo.py`** (Pillow, k-means) en fotogramas
propios o en arte oficial. Una muestra cada una: ⚠️ salvo que se diga.

| Sitio | Hex medidos | Luz | Dónde se midió |
|---|---|---|---|
| Concierto nocturno, Rumi canta | `#010102` `#42375B` `#5D4168` `#232A59` `#3F5590` `#A1ACCA` | Violeta frío, brillo 32%, sombreado plano | Tráiler 0:08 |
| Pelea en niebla verde | `#000000` `#495745` `#313A31` `#A0B481` `#748661` `#D3DEAF` | Verde neón sucio, brillo 35% | Tráiler 0:24 |
| Niebla verde-amarilla cenital | `#000101` `#5F9A6A` `#35605F` `#19204D` `#675899` `#B2A5E5` | Verde y violeta, brillo 38% | Tráiler 1:40 |
| Bambalinas del concierto | `#040204` `#2E1E26` `#533B42` `#676676` `#899DAD` | Vino y malva, brillo 25% | «How It's Done» 0:12 |
| Trío a contraluz violeta | `#0A0827` `#000002` `#4F2A65` `#9C828F` `#E2E7F1` | Contraluz, brillo 24% | «How It's Done» 0:54 |
| Zoey y sus dagas | `#0C0B34` `#010106` `#5D4B7C` `#AB81AA` `#EBE9F7` | Azul violeta con acento lila | «How It's Done» 1:06 |
| Puente al atardecer | `#C85124` `#8E1815` `#040001` `#C52263` `#D384C9` | **El más cálido**: naranja y rojo, saturación 68% | «How It's Done» 2:48 |
| Calle de Seúl, debut Saja Boys | `#C75CB4` `#AF49A0` `#7B3B7A` `#392E47` · `#4C3F63` `#847AC0` `#B07E4A` `#CB93D3` | Magenta de neón con luz dorada de tienda | «Soda Pop» 0:24 y 2:30 |
| Trono de Gwi-Ma | `#040102` `#221B26` `#4F3741` `#92663D` `#E4CE74` | Negro con dorado verdoso, brillo 22% | «Golden» 0:30 |
| Escenario de los Idol Awards | `#0A0503` `#3B6369` `#E0C66B` `#AF8351` `#793121` | Rojo y oro de templo, foco cenital | «Golden» 2:12 |
| Seúl y la Namsan Tower | `#000000` `#BCB2E8` `#A095C6` `#DCD7F9` `#4B4D42` `#817D8A` | Lavanda pastel, brillo 57% | «Golden» 3:00 |
| Cierre, las tres juntas | `#010102` `#564BA2` `#ECD4FC` `#C5ADF5` `#8972D0` | **El más claro**: lila, brillo 63% | «Golden» 3:02 |
| HUNTR/X Tower, Seúl de noche | `#060E1D` `#121C32` `#102E50` `#464961` `#3E869C` `#D2D6CA` | Azul medianoche, brillo 23% ✅ | [HUNTRX_Tower_Full.png](https://static.wikia.nocookie.net/kpop-demon-hunters/images/d/d4/HUNTRX_Tower_Full.png), 1920×800 |
| Namsan Tower, anochecer | `#BDBAF0` `#AAA1D4` `#DED1F5` `#383833` `#8683A6` `#615F5F` | Cielo lavanda, brillo 76% ✅ | [Namsantowerkdh.jpg](https://static.wikia.nocookie.net/kpop-demon-hunters/images/a/ab/Namsantowerkdh.jpg), 964×600 |
| Set del Honmoon (nachomolina) | `#1D579B` `#244B7C` `#07201A` `#233855` `#577DA8` `#B3C6D8` | **Azul místico**, saturación 70% ✅ | [TheHonmoon1_setdesign](https://static.wikia.nocookie.net/kpop-demon-hunters/images/c/c2/TheHonmoon1_setdesign_nachomolina.jpg), 2500×1776 |
| Montaña con las caras | `#B2A6A1` `#D2D0D6` `#7F7D87` `#424C64` `#A3B9D8` `#649FD7` | Gris con azul frío, mucha línea | [Mountain.jpeg](https://static.wikia.nocookie.net/kpop-demon-hunters/images/1/1e/Huntrix_and_Saja_Boys_Mountain.jpeg), 2307×976 |

- **La regla de color de la película**, repetida en los cuatro números
  musicales mirados: **verde neón** = demonios y peleas; **magenta y
  rosa** = Saja Boys y la calle; **dorado y rojo cálido** = triunfo de
  HUNTR/X; **lavanda pastel** = el final feliz. ✅ (patrón visto en 4
  clips distintos)
- **Han Clinic** (espejo del baño, «Golden» 1:48): gris azulado
  apagado, luz plana de baño, marcas rosa y violeta sobre la bata. Sin
  hex medidos. ⚠️
- **Mundo Demonio**: reino bajo el nuestro, niebla, picos de roca,
  charcos, cielo siempre cubierto
  ([wiki, Demon world](https://kpop-demon-hunters.fandom.com/wiki/Demon_world)). ✅
- **HUNTR/X Tower**: rascacielos de Seúl con el logo del grupo en la
  fachada; dentro, ático (habitaciones, cocina, sala), **estudio de
  grabación** y vestidor
  ([wiki](https://kpop-demon-hunters.fandom.com/wiki/HUNTR/X_Tower)). ✅
- **Namsan Tower**: la N Seoul Tower real; allí tocan los Saja Boys al
  final y HUNTR/X crea el nuevo Honmoon
  ([wiki](https://kpop-demon-hunters.fandom.com/wiki/Namsan_Tower)). ✅

**Texturas reales equivalentes** (CC0, AmbientCG). Son equivalencias
genéricas, no copias del metraje. ⚠️

| Para | Textura |
|---|---|
| Tejas de palacio y hanok (Gyeongbokgung, Bukchon, Joseon) | [RoofingTiles013A](https://ambientcg.com/view?id=RoofingTiles013A), [RoofingTiles006](https://ambientcg.com/view?id=RoofingTiles006) |
| Madera oscura (Han Clinic, muebles) | [Wood051](https://ambientcg.com/view?id=Wood051), [WoodFloor051](https://ambientcg.com/view?id=WoodFloor051) |
| Papel *hanji* (farolillos, carteles de Joseon, cuaderno) | [Paper006](https://ambientcg.com/view?id=Paper006), [Paper001](https://ambientcg.com/view?id=Paper001) |
| Hormigón de Seúl (torre, puente Cheongdam) | [Concrete034](https://ambientcg.com/view?id=Concrete034), [Concrete047A](https://ambientcg.com/view?id=Concrete047A) |
| Tela de trajes y telón | [Fabric081C](https://ambientcg.com/view?id=Fabric081C), Fabric061 |
| Metal dorado (Honmoon, accesorios) | [Metal048A](https://ambientcg.com/view?id=Metal048A), Metal034 |
| Cuero (cazadora, correas) | [Leather037](https://ambientcg.com/view?id=Leather037), Leather038 |

## 6 · Tipografía: una letra para cada uso (punto 5)

**El logo de la película** lo hizo el estudio de títulos
**Picturemill**, que también hizo los títulos de inicio y los créditos
finales ([portfolio de Picturemill](https://picturemill.com/portfolio/kpop-demon-hunters/)). ✅

- Cómo es (medido en el
  [archivo oficial de la wiki](https://static.wikia.nocookie.net/kpop-demon-hunters/images/a/ad/KPop_Demon_Hunters_Logo.png),
  1000×266): sans geométrica **blanca**, en dos líneas («K-POP» /
  «DEMON·HUNTERS»), con **sombra gris en diagonal**. La K, la N, la R y
  la H tienen **cortes en diagonal**. Una **estrella de cuatro puntas**
  hace de punto del guion y separa «DEMON» de «HUNTERS». ✅
- El prototipo de 2021 era un degradado neón rosa y azul sobre azul
  oscuro, más chillón que el final
  ([1000logos](https://1000logos.net/k-pop-demon-hunters-logo/)). ⚠️
- El logo de **HUNTR/X** (el del grupo) sería una **Blanka
  modificada**, según los aficionados del
  [foro de dafont](https://www.dafont.com/forum/read/577458/kpop-demon-hunters-font).
  Blanka es de pago: no se comprobó. ⚠️
- El de los **Saja Boys** es otra cosa: firma a pincel, «SAJA» en
  blanco y «BOYS» en magenta `#FC02A5`
  ([logo en la wiki](https://static.wikia.nocookie.net/kpop-demon-hunters/images/e/ed/Saja_Boys_Logo.jpg)). ✅

**Una letra para cada uso.** Todas las libres se **descargaron y se
abrieron con `fontTools`**: la columna «¿Trae?» es comprobada, no de
memoria.

| Uso | Qué hay en la película | Letra libre | ¿Trae á é í ó ú, ñ, ¿, ¡? | Licencia |
|---|---|---|---|---|
| Logo o título | Sans geométrica de Picturemill, cortes en diagonal, estrella de 4 puntas | **Hunters K-Pop** (Chequered Ink, Allison J. James, 2025), la que propone el [hilo de dafont](https://www.dafont.com/forum/read/577458/kpop-demon-hunters-font); bajada de [FontSpace](https://www.fontspace.com/hunters-k-pop-font-f150441) | ✅ las 11 | Gratis uso personal; comercial de pago ([Chequered Ink](https://chequered.ink/font-license/)) |
| Logo de HUNTR/X | Blanka modificada (⚠️) | **Hunters K-Pop** | ✅ | Igual |
| Logo de Saja Boys | Firma a pincel | **Permanent Marker** ([archivo de Fontsource](https://cdn.jsdelivr.net/fontsource/fonts/permanent-marker@latest/latin-400-normal.ttf)) | ✅ | OFL |
| Grito (grafismo de concierto) | Frases enormes que laten con la música, hechas en After Effects | **Anton**, recorte «latin» | ✅ (el «latin-ext» **no** trae tildes) | OFL |
| Pensamiento (manuscrito) | Rumi escribe con el dedo en el vaho del espejo | **Caveat** | ✅ | OFL |
| Onomatopeya | No hay. Lo más parecido: el rótulo «SHINING» sobre el Honmoon («Golden» 0:48) y el neón verde «HAH» del trono (0:24-0:30) | **Anton** (el mismo grafismo) | ✅ | OFL · ⚠️ letra exacta no comprobada |
| Cartel del mundo (hangul) | Letrero **HAN의원** de la clínica, logo en la fachada de la torre | **Noto Sans KR**, recorte «latin» | ✅ y todo el hangul | OFL |
| Interfaz de juego (Roblox) | **Builder Sans** desde 2024; lo viejo en Gotham pasa a Montserrat, y Arial a Arimo ([foro oficial de Roblox](https://devforum.roblox.com/t/introducing-builder-font-deprecating-gotham-and-arial/2868222)) | **Montserrat** o **Arimo** | ✅ las dos | OFL |
| Subtítulos y créditos | Netflix Sans en la app; Arial en los archivos de subtítulos ([guía de Netflix](https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617-Timed-Text-Style-Guide-General-Requirements)) | **Roboto** | ✅ | OFL |

- **Truco de Fontsource**: en fuentes partidas en recortes, las tildes
  españolas suelen estar en «latin», no en «latin-ext». Pedir siempre
  el «latin». ✅ (comprobado en Anton)
- El grafismo de conciertos lo hizo el equipo de Sony Pictures
  Imageworks en **After Effects**, cada canción con su línea de tiempo
  (Nori Kaneko, en
  [No Film School](https://nofilmschool.com/kpop-demon-hunters-how-sony-pictures-imageworks-used-adobe-in-creating-the-global-phenomenon)). ✅

## 7 · Cómo hablan en pantalla: el cuadro de diálogo (punto 6)

**No hay globos.** Es una película con voces, no un manga. Una burbuja
blanca sería falsa. La película tiene **cinco maneras reales** de poner
texto en pantalla:

1. **Grafismo de concierto (el «cuadro» propio de la serie).** Frases
   enormes que aparecen detrás o alrededor de las chicas y laten con la
   música, como letreros de escenario. Ejemplos vistos con minuto:
   - «I'M GONNA SHOW YOU», detrás del trío con los puños en alto
     ([«How It's Done» 0:54](https://archive.org/details/youtube-QGsevnbItdU)). ✅
   - «HUNTRIX DON'T QUIT!», con Zoey y sus dagas («How It's Done»
     1:06). ✅
   - «UP UP UP», detrás de Rumi en los Idol Awards
     ([«Golden» 2:12](https://archive.org/details/golden-official-lyric-video-kpop-demon-hunters-sony-animation_202511)). ✅
   - «ROTTEN» y «WORLD OF PAIN» en el escenario
     ([«Takedown» 0:30-1:00](https://archive.org/details/youtube-l8Dr7vzMSVE)). ✅
   - Lo hizo Imageworks en After Effects, sincronizado a cada canción
     ([No Film School](https://nofilmschool.com/kpop-demon-hunters-how-sony-pictures-imageworks-used-adobe-in-creating-the-global-phenomenon)). ✅
2. **Letra a mano en el vaho del espejo.** El único «pensamiento»
   visible: Rumi, en el baño del Han Clinic, escribe con el dedo «Put
   these patterns all in the past now» («Golden» 1:48). Es su letra,
   no un rótulo. ✅
3. **Subtítulo de Netflix.** Centrado, abajo o arriba. El espectador
   elige entre 4 estilos: blanco, blanco con sombra, negro sobre
   blanco o amarillo sobre negro
   ([ayuda de Netflix](https://help.netflix.com/en/node/100267)). ✅
4. **Karaoke del *sing-along*.** En la reposición para cantar en el
   cine, la letra salía en pantalla sobre la película
   ([The Hollywood Reporter](https://www.hollywoodreporter.com/movies/movie-news/kpop-demon-hunters-sing-along-box-office-first-netflix-win-1236352043/)). ✅
5. **Carteles del mundo en hangul**: el letrero **HAN의원** de la
   clínica (juego con el apellido del doctor y «clínica de medicina
   tradicional»), el logo en la fachada de la torre, y el mensaje que
   Jinu le escribe a Rumi y ella lee en voz alta
   ([wiki, Korean Cultural References](https://kpop-demon-hunters.fandom.com/wiki/Korean_Cultural_References)). ✅

**Qué recurso para qué texto de una lámina**:

| Texto | Recurso | Letra |
|---|---|---|
| El título o la orden principal («¡Sube tu cover!») | Grafismo de concierto, grande, detrás del personaje | Anton |
| Un consejo íntimo o un ánimo | Letra a mano en vaho o en un cuaderno | Caveat |
| Una explicación neutra (cómo se usa) | Subtítulo de Netflix, blanco con sombra | Roboto |
| Nombre de un sitio o de una sala | Cartel del mundo, con hangul | Noto Sans KR |
| Etiquetas, rangos | *Photocard* o pegatina de merch (§24) | Hunters K-Pop |

- ⚠️ «50,000 fans are waiting for you» («How It's Done» 0:06) parecía
  una pantalla de móvil. Es letra del grafismo, no un chat. No usarla
  como «pantalla de teléfono» sin ver el fotograma.
- ⚠️ **No hay caja de diálogo de misión** en las 9 capturas oficiales
  del juego de Roblox: son de tienda y promoción (§13).

## 8 · Los personajes a fondo: carácter, cara y dinámicas (punto 13)

Fuentes: fichas de la wiki (Personality, Appearance, Trivia), las 6
muestras oficiales del doblaje latino oídas con `voz.py`, y los
fotogramas y hojas mirados. La voz medida (Hz, semitonos) es de esas
muestras.

### Rumi — la líder que esconde lo que es

- **Qué es.** Líder y voz principal de HUNTR/X, 23 o 24 años. Es
  **mitad demonio** (*cambion*) y lo oculta: tiene marcas moradas en la
  piel que brillan rosa cuando se estresa
  ([wiki, Rumi](https://kpop-demon-hunters.fandom.com/wiki/Rumi)). ✅
- **Carácter.** Segura en público, ambiciosa, responsable, «la mayor».
  Se exige más que nadie: sigue cantando con la voz rota aunque el grupo
  le pide parar. Terca, casi nunca pide ayuda. ✅
- **Miedo.** Que la descubran y perder al grupo y a los fans. ✅
- **Qué transmite.** Ternura y nudo en la garganta: la chica perfecta
  que por dentro se avergüenza de sí misma. Es con quien más se
  identifica el público (§22).
- **Arco.** Esconde las marcas → su voz se rompe → sana cantando con
  Jinu («Free») → la descubren → se acepta en «What It Sounds Like» y
  crea el Honmoon arcoíris (§26). ✅
- **Cómo se expresa.** Autoridad de líder hacia fuera; en privado,
  frases que dudan y se quiebran. En latino (Azul Bötticher) suena
  reflexiva y algo temblorosa: tono agudo (232 Hz), expresividad
  normal (4,2 semitonos). ✅
- **Su cara en cada emoción**:

| Emoción | Cómo es | Dónde |
|---|---|---|
| Alegría, triunfo | Sonrisa amplia, cabeza atrás, brazos en «V» | «Golden» [2:12](https://archive.org/details/golden-official-lyric-video-kpop-demon-hunters-sony-animation_202511) ✅ |
| Vergüenza, miedo | Ceja fruncida, boca entreabierta, mirada de lado, un brazo tapando las marcas del otro | «Golden» 1:48 ✅ |
| Miedo (demonio) | Piel azulada, cara angustiada, en la oscuridad | hoja `personajes_01` nº 38; `vestuario_10` nº 471 ✅ |
| Tristeza | Suplica a Celine, plano 4K | `personajes_01` nº 19 ✅ |
| Rabia, pelea | Ceño fruncido, cuerpo hacia delante, espada | Tráiler [0:24](https://www.dailymotion.com/video/x9k1104?t=24) ✅ |
| Sorpresa | Boca abierta, sudadera rosa | `vestuario_10` nº 474 ✅ |
| Segura, reta | Media sonrisa, cazadora amarilla | `vestuario_10` nº 433 ✅ |
| Glotona feliz | Mejillas llenas de kimbap | `vestuario_10` nº 478 ✅ |

### Mira — la dura que por fin encontró su sitio

- **Qué es.** Segunda al mando, bailarina y coreógrafa principal. Su
  familia la rechazó por ser como es; en HUNTR/X puede ser ella misma
  ([wiki, Mira](https://kpop-demon-hunters.fandom.com/wiki/Mira)). ✅
- **Carácter.** Directa, sarcástica, desconfiada al principio, «el
  músculo del trío». Genio corto. Se ablanda enseguida con sus amigas. ✅
- **Qué transmite.** Seguridad y risa seca. La amiga que te dice la
  verdad a la cara y luego te defiende.
- **Cómo se expresa.** Frases cortas e inexpresivas (*deadpan*). En
  latino (Karin Zavala) se define sola: «franca, temperamental,
  agresiva». Tono medio (184 Hz), muy expresiva (10,7 semitonos). ✅
- **Su cara**: rabia con dientes apretados y manos como garras
  (`vestuario_10` nº 448); fastidio (nº 449); desconfianza con gorra y
  gafas (nº 435, 437); susto en bata (nº 450); guiño con el puño en la
  sien y media sonrisa
  ([«Takedown» 1:06](https://archive.org/details/youtube-l8Dr7vzMSVE)). ✅
  ⚠️ No hay fotograma con minuto de su tristeza.

### Zoey — la pequeña que escribe las letras

- **Qué es.** Rapera y letrista, la más joven (*maknae*). Nació en
  Corea y se crió en Burbank, California
  ([wiki, Zoey](https://kpop-demon-hunters.fandom.com/wiki/Zoey)). ✅
- **Carácter.** Efusiva, cariñosa con fans y amigas, algo ingenua
  (cree que los tónicos del doctor Han curan la voz), muy distraída:
  dos veces no puede evitar bailar «Soda Pop» aunque la canten sus
  enemigos. ✅
- **Miedo.** Que sus letras sean «inútiles y raras». El grupo le da
  valor. ✅
- **Qué transmite.** Alegría pura y ternura. La que levanta el ánimo.
- **Cómo se expresa.** Habla rápido y encadena preguntas cuando se
  pone nerviosa. En latino (Tatul Bernodat): tono agudo (264 Hz), muy
  expresiva (9,6 semitonos). ✅
- **Su cara**: desafiante con las dagas en alto y ceja levantada
  («How It's Done» 1:06); pícara (`vestuario_10` nº 457); suplicando
  con las manos juntas (nº 458); triste (nº 459); deslumbrada (nº 465);
  fan abrazando el disco de las Sunlight Sisters (nº 466); **ojos de
  mazorca** (`concept_02` nº 93). ✅

### Jinu — el demonio que quería olvidar

- **Qué es.** Líder de los Saja Boys, demonio. Hace 400 años era un
  plebeyo de Joseon: pactó con Gwi-Ma para salir de la pobreza y
  abandonó a su madre y a su hermana pequeña
  ([wiki, Jinu](https://kpop-demon-hunters.fandom.com/wiki/Jinu)). ✅
- **Carácter.** Listo, carismático y manipulador. Pacta con Gwi-Ma que
  le borre los recuerdos a cambio de ayudar a romper el Honmoon. Odia a
  Gwi-Ma, pero le obedece. ✅
- **Qué transmite.** Encanto y pena. El público lo quiere pese a ser
  demonio: «no es un demonio malo» (§22).
- **Arco.** Seduce a Rumi para desestabilizarla → se le acerca de verdad
  («Free») → se sacrifica por ella en el clímax y recupera un momento el color
  humano de sus ojos. ✅
- **Cómo se expresa.** Se burla y coquetea con Rumi. Al hablar de su
  vergüenza baja la voz de golpe: en latino (Juan Balvín) es la más
  grave del reparto, 112 Hz. ✅
- **Su cara**: media sonrisa seductora a cámara
  ([tráiler 1:20](https://www.dailymotion.com/video/x9k1104?t=80));
  silueta con *gat* (`vestuario_10` nº 438); retrato sonriente
  (`concept_02` nº 60); demonio con *gat* y luz magenta (nº 89). ✅

### Los secundarios

- **Gwi-Ma**, el villano. Demonio que devora almas, atrapado; sólo
  actúa a través de sus siervos. En latino (Carlo Vázquez Díaz) tiene
  el rango de voz más amplio: 32,8 semitonos, de grave amenazante a
  gritos. ✅
- **Celine**, mentora de Rumi y su madre adoptiva, antigua cazadora.
  Protectora y urgente: habla rápido (3,06 palabras por segundo). ✅
- **Bobby**, el mánager. Rompe el cliché del mánager codicioso: sólo se
  lleva el 3%
  ([Collider](https://collider.com/kpop-demon-hunters-characters-likability-ranked/)). ✅
- **Derpy y Sussie**, las mascotas de Jinu: un tigre azul y una urraca
  de seis ojos con sombrero, sacados de la pintura popular *jak-ho-do*
  ([wiki](https://kpop-demon-hunters.fandom.com/wiki/Derpy_and_Sussie)). ✅
- **El doctor Han** (Healer Han): llama a Rumi «Rumi Nim». ✅

### Dinámicas (para láminas en grupo)

- **Mira y Rumi discuten** por lo cerrada que es Rumi. ✅
- **Zoey es la que más anima a Rumi** y la que hace bajar la guardia a
  Mira. ✅
- **Jinu pica y coquetea con Rumi** para desestabilizarla. ✅
- **Celine protege a Rumi** pidiéndole tapar sus marcas («Cubramos tus
  marcas», §10). ✅
- En grupo, Rumi va **en el centro**, Mira a un lado, siempre de
  perfil respecto a cámara («How It's Done» 0:54). ✅

## 9 · ¿Quién es el más querido? (punto 7)

**No hay encuesta oficial por personaje** (ni de Netflix ni de Sony).
Lo que sí hay:

- **YouGov (EE. UU.), sobre la película**: la conoce el 61%; le gusta
  al 31% de quienes la conocen; le disgusta al 12%
  ([YouGov](https://yougov.com/en-us/topics/movies/KPop_Demon_Hunters)). ✅
- **Ranking de Collider por lo querible** (ago-2025): 1.º **Rumi** («la
  más humana»), 2.º **Zoey** («la más divertida»), 3.º **Mira**, 4.º
  **Bobby**, 5.º Jinu, 6.º Derpy y Sussie, 7.º el doctor Han, 8.º los
  Saja Boys, 9.º Celine, 10.º Gwi-Ma
  ([Collider](https://collider.com/kpop-demon-hunters-characters-likability-ranked/)). ✅
- **Reddit, r/KpopDemonhunters**: el debate de siempre es **Mira contra
  Rumi** («Mira es la dura» / «Rumi es la más identificable»); Zoey
  tiene un grupo más pequeño. Hilo con más votos: 120 votos y 60
  comentarios
  ([hilo del aniversario](https://www.reddit.com/r/KpopDemonhunters/comments/1u24oq4/));
  otro de 95 votos y 70 comentarios
  ([«who is your favorite character?»](https://www.reddit.com/r/KpopDemonhunters/comments/1wdm1vs/hi_im_brand_new_herei_discovered_kpdh_not_long/)). ✅
- ⚠️ El recuento de fan art de Danbooru **no sirve**: el recolector
  mezcló personajes de otras obras.

**Conclusión para la lámina:**
- **Rumi** es a la vez la protagonista y la más querida. Aquí no hay un
  secundario que la supere.
- **Mira** va muy cerca: la favorita de quien quiere carácter.
- El secundario que sorprende: **Bobby**, el mánager, por delante de
  Jinu.
- El más querido «de meme»: **Derpy** (§14).
- Jinu es el que más hace llorar (§22).

## 10 · Doblaje latino y frases textuales (punto 8)

**Ficha** (Doblaje Wiki por su API; confirmada por
[ANMTV](https://www.anmtvla.com/2025/06/las-guerreras-k-pop-ya-esta-disponible.html)):
- Título: **«Las guerreras k-pop»**.
- Estudio: **Media Access Company Argentina**.
- Dirección de doblaje y dirección musical: **Irene Guiser**.
- Traducción: **Solana Malacco**. Adaptación musical: **Sandra
  Brizuela**.
- Grabado en **enero y febrero de 2025**. Con diálogos grabados en
  España (Azul Bötticher y Luciana Falcón Graña) y en México (Carlo
  Vázquez Díaz)
  ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Las_guerreras_k-pop)). ✅
- En latino **las mismas actrices hablan y cantan**; sólo Celine tiene
  dos voces (§0). ✅

**Reparto** (dos fuentes: Doblaje Wiki y ANMTV o
[Infobae](https://www.infobae.com/tecno/2025/11/25/las-guerreras-de-k-pop-como-se-llaman-y-quienes-son-las-voces-en-espanol/)):

| Personaje | Voz latina | Estado |
|---|---|---|
| Rumi | **Azul Bötticher** | ✅ Doblaje Wiki, ANMTV, Infobae |
| Rumi niña | Donna Ponce Carballo | ✅ Doblaje Wiki, Infobae |
| Mira | **Karin Zavala** | ✅ tres fuentes |
| Zoey | **Tatul Bernodat** | ✅ tres fuentes |
| Jinu | **Juan Balvín** | ✅ tres fuentes |
| Celine | Mara Campanelli (habla) / Paloma Odriozola (canta) | ✅ / ⚠️ sólo Doblaje Wiki |
| Bobby | Alejandro Bono | ✅ tres fuentes |
| Abby Saja | Nicolás Ginesin | ✅ (Infobae: «Guinessin») |
| Romance Saja | Thomas Lepera | ✅ (Infobae: «Tomás») |
| Gwi-Ma | Carlo Vázquez Díaz (México) | ⚠️ sólo Doblaje Wiki |
| Mystery Saja | Pablo Gandolfo | ⚠️ sólo Doblaje Wiki |
| Baby Saja | Mathias Rapisarda | ⚠️ sólo Doblaje Wiki |
| Doctor Han | Pedro Ruiz | ⚠️ sólo Doblaje Wiki |
| Anfitrión de los premios Idol | Hernán Tracchia | ⚠️ sólo Doblaje Wiki |
| Presentadores de «Jueguen con nosotros» | Marcelo Pintos y Alan Kanaan | ⚠️ sólo Doblaje Wiki |
| Demonio llorón | Luciana Falcón Graña | ⚠️ sólo Doblaje Wiki |

- **Dato para el servidor**: Carlo Vázquez Díaz ya dobló a **Lee
  Byung-hun** (actor original de Gwi-Ma) en *El juego del calamar*. Por
  eso el meme del «Front Man» (§14). En Brasil pasa igual con Guilherme
  Briggs. ✅

**Frases textuales del doblaje latino.** Transcritas con `voz.py`
(Whisper) de las **muestras oficiales de Doblaje Wiki**, y oídas. El
minuto es **de la muestra**, no de la película. ✅ salvo lo marcado.

| Quién | Frase | Muestra · minuto |
|---|---|---|
| **Rumi** | «Hasta que empezó a destruir lo único que me daba un propósito. Mi voz. Pero desde que te conocí y a medida que hablamos, no lo entiendo, pero de alguna forma mi voz estuvo sanando.» | [Rumi2 LGK.ogg](https://static.wikia.nocookie.net/doblaje/images/3/32/Rumi2_LGK.ogg/revision/latest?cb=20260629225230&path-prefix=es) · 0:08-0:18 |
| **Mira** | «Miren, soy una persona un poco difícil. Muy franca, temperamental, agresiva. Toda mi vida esos rasgos fueron algo malo. Pero de alguna forma, con ustedes, me siento bien.» | [Mira (Audio)](https://static.wikia.nocookie.net/doblaje/images/b/b5/Mira_%28Audio%29_-_LGK.ogg/revision/latest?cb=20260629225208&path-prefix=es) · 0:27-0:36 |
| **Zoey** | «¿Cómo lo resolvemos? ¿Qué sabrán los fans? [...] Antes de unirme a Huntrix sentía que mis pensamientos, mis letras y todas mis libretas eran inútiles y raras. Pero con ustedes dos significan algo. Yo tengo valor.» | [Zoey (Audio)](https://static.wikia.nocookie.net/doblaje/images/d/d3/Zoey_%28Audio%29_-_LGK.ogg/revision/latest?cb=20260629225233&path-prefix=es) · 0:00-0:20 |
| **Jinu** | «Me recuerdan mi vergüenza, una vergüenza de la que no puedo escapar [...] Puedes contármelo, voy a entender. Soy el único que puede.» | [Jinu (Audio)](https://static.wikia.nocookie.net/doblaje/images/e/eb/Jinu_%28Audio%29_-_LGK.ogg/revision/latest?cb=20260629225205&path-prefix=es) · 0:12-0:27 |
| **Gwi-Ma** | «¡Me pareció que creíste que podía ser libre! [...] Traicionaste a tu propia familia, las dejaste atrás, no olvides nuestro trato [...] No creas que puedes escapar de tu realidad.» ⚠️ una fuente | [Gwi-Ma (Audio)](https://static.wikia.nocookie.net/doblaje/images/a/a5/Gwi-Ma_%28Audio%29_-_LGK.ogg/revision/latest?cb=20260629225200&path-prefix=es) · 0:02-0:26 |
| **Celine** | «Cubramos tus marcas y resolvamos las cosas. Les diré a Mira y a Zoey que todo fue una mentira, una ilusión de Guima para separarnos.» ⚠️ una fuente | [Celine (Audio)](https://static.wikia.nocookie.net/doblaje/images/8/84/Celine_%28Audio%29_-_LGK.ogg/revision/latest?cb=20260629225114&path-prefix=es) · 0:21-0:30 |

- **Cómo se escriben al oído**: la transcripción revisada de las
  muestras da «**Guima**» y «**Huntrix**». Para un texto en la voz del
  doblaje, escribirlos así. ⚠️ (transcripción, no guion oficial)
- **Cambios de traducción** (Doblaje Wiki, con cita de Azul
  Bötticher): la burla de Jinu a Rumi, «¡Y tú eres de 1900!», quedó
  como **«¿Qué eres, del siglo pasado?»**. ✅
- **Canciones en latino**: «Golden» → **«Dorada»**, «Takedown» →
  **«Nocaut»**, «Soda Pop» se queda igual. ✅
- ⚠️ «¡Huntrix no se rinde!» (de «HUNTR/X don't quit!») es muy citada,
  pero en pantalla sale en inglés. No hay clip doblado que confirme la
  frase exacta.
- ⚠️ **No hay clips oficiales doblados** en Dailymotion ni Internet
  Archive. El tráiler latino subido por fans
  ([x9tkmqo](https://www.dailymotion.com/video/x9tkmqo), 0:39) no
  tiene diálogo. El clip `x9sl3s6` ya no existe.

## 11 · Música y sonido (punto 9)

**Es un musical.** No hay opening ni ending: hay 9 canciones propias,
la partitura de **Marcelo Zarvos** y 3 canciones de fuera (de TWICE,
MeloMance y Jokers, según la parte de vídeo)
([wiki, Soundtrack](https://kpop-demon-hunters.fandom.com/wiki/KPop_Demon_Hunters_(Film)/Soundtrack);
[Republic Records](https://shop.republicrecords.com/products/kpop-demon-hunters-soundtrack-from-the-netflix-film-digital-album)). ✅

| Canción | Quién | Qué pasa y qué ambiente da |
|---|---|---|
| «How It's Done» | HUNTR/X | La presentación: selfie en la furgoneta, pelea entre bambalinas, trío con los puños en alto. Energía de debut |
| «Soda Pop» | Saja Boys | Debut del grupo rival en la calle: humo magenta, dulce y pegadizo. Se vuelve viral |
| «Golden» («Dorada») | HUNTR/X | El himno: el Honmoon se vuelve dorado, triunfo en los Idol Awards, espejo del Han Clinic |
| «Strategy» | — | Tema de la banda sonora |
| «Takedown» («Nocaut») | HUNTR/X; versión de TWICE | *Diss track* contra los Saja Boys. Oscuro y agresivo |
| «Your Idol» | Saja Boys | La canción del villano, en la Namsan Tower: rompe el Honmoon |
| «Free» | Rumi y Jinu | Dúo. **Ella sana su voz al confiar en él** |
| «What It Sounds Like» | HUNTR/X | Clímax: Rumi rompe el trance de Gwi-Ma sobre Mira y Zoey |
| «Love, Maybe» (사랑인가 봐) | MeloMance (ya existía) | ⚠️ suena, según vídeo, en la escena de los ojos de corazón |
| «Path» (오솔길) | — | Tema de la banda sonora |
| «Score Suite» | Marcelo Zarvos | La partitura |
| «Prologue (Hunter's Mantra)», 1:36 | Celine narra | Edición *deluxe* |
| «Jinu's Lament», 0:46 | Jinu | Edición *deluxe* |

✅ (lista y escenas: wiki; ⚠️ lo marcado)

- **Quién canta de verdad**: **EJAE** (Rumi), **Audrey Nuna** (Mira),
  **Rei Ami** (Zoey)
  ([Billboard](https://www.billboard.com/lists/huntrx-golden-kpop-demon-hunters-number-1-hot-100/)).
  Los Saja Boys: **Andrew Choi** (Jinu), Danny Chung (Baby Saja), Kevin
  Woo y Alan Lee
  ([Wikipedia, Andrew Choi](https://en.wikipedia.org/wiki/Andrew_Choi)). ✅
- Productor musical ejecutivo: **Ian Eisendrath**. Canciones con 24,
  Teddy Park, Lindgren, Stephen Kirk, Jenna Andrews, IDO y otros. ✅
- **Récords**: «Golden» fue nº1 del Hot 100 **8 semanas** o más, y
  HUNTR/X el primer grupo femenino ligado al K-pop en lograrlo. El
  álbum llegó al **nº1 del Billboard 200** y tuvo **4 canciones a la vez
  en el top 10**, la primera banda sonora en hacerlo
  ([Billboard 200](https://www.billboard.com/music/chart-beat/kpop-demon-hunters-soundtrack-number-one-billboard-200-1236066167/)). ✅
- **Versiones**: *remix* de David Guetta (25-jul-2025); «Golden» de
  The Piano Guys; banda sonora en francés; la partitura de Zarvos salió
  aparte el 19-dic-2025
  ([MusicBrainz](https://musicbrainz.org/release-group/094f56bf-4715-4e33-bb28-058b1ab43036)). ✅
- **Las escenas más emotivas** suenan con «Free» y «What It Sounds
  Like». ✅

**Sonidos que todos reconocen**:
- El **Honmoon** suena como un tañido de campana coreana cuando se
  activa o se agrieta («Golden» 0:48, «SHINING»). ⚠️ (oído en el clip)
- **Gwi-Ma** ruge con eco grave y distorsionado en su trono verde
  («Golden» 0:24-0:30). ⚠️ (oído en el clip)
- El grito de HUNTR/X: **«gaja gaja gaja»** (가자, «¡vamos!»)
  ([wiki](https://kpop-demon-hunters.fandom.com/wiki/Korean_Cultural_References)). ✅
- El **«HEHEHE»** de Jinu, que se hizo meme (§14). ✅
- ⚠️ No hay entrevista del diseñador de sonido.

## 12 · Vídeos y tendencias (punto 10)

**YouTube pedía iniciar sesión.** Se usaron copias en Dailymotion e
Internet Archive, con metraje real.

| Vídeo | Minuto útil | Qué sirve | Estado |
|---|---|---|---|
| [Tráiler oficial](https://www.dailymotion.com/video/x9k1104), 2:43 | [0:24](https://www.dailymotion.com/video/x9k1104?t=24) trío con armas; [1:04](https://www.dailymotion.com/video/x9k1104?t=64) Saja Boys en fila; [1:20](https://www.dailymotion.com/video/x9k1104?t=80) Jinu; 2:24 «ONLY ON NETFLIX JUNE 20» | Poses y cartela | ✅ |
| [Tráiler, copia de JeuxVideo.com](https://www.dailymotion.com/video/x9khghu) | 64 370 vistas | La misma pieza | ✅ |
| Teaser de 2:30 en [Allociné](https://www.dailymotion.com/video/x9k0bd2) (237 004 vistas) y [FILMSTARTS](https://www.dailymotion.com/video/x9k0b34) (156 239) | — | El tráiler sin el logo final | ✅ |
| [*Lyric video* «How It's Done»](https://archive.org/details/youtube-QGsevnbItdU) | 0:06, 0:54, 1:06, 2:18, 2:48 | Presentación y pelea | ✅ |
| [*Lyric video* «Soda Pop»](https://archive.org/details/youtube-983bBbJx0Mk) | 0:12-0:48 | Debut de los Saja Boys | ✅ |
| [*Lyric video* «Golden»](https://archive.org/details/golden-official-lyric-video-kpop-demon-hunters-sony-animation_202511) | 0:24, 0:48, 1:48, 2:12, 3:00, 3:02 | El más útil de todos | ✅ |
| [*Lyric video* «Takedown»](https://archive.org/details/youtube-l8Dr7vzMSVE) | 0:30-1:00, 1:06, 1:48 | TWICE en el estudio; diss track | ✅ |
| [*Scenepack* 4K de Rumi](https://www.dailymotion.com/video/x9ohwu0), 2:38 | — | Cantera de planos grandes | ⚠️ de fans |

- **Panel de los directores** (Animation Is Film, Los Ángeles): la
  escena de los **ojos de corazón** (que cambian a *six-pack* y a
  mazorca) nació de una orden de la presidenta de Sony Animation,
  Kristine Belson: «Let's objectify the crap out of these guys»
  ([AOL](https://www.aol.com/articles/kpop-demon-hunters-directors-break-150000307.html)). ⚠️ (texto, no el vídeo)
- **El director de fotografía, Gary Lee**, explica el encuadre pegado
  a la cabeza, tipo TikTok, en un vídeo de Collider que no se pudo ver
  (§19). ⚠️
- **Sing-along en cines** (23-24 ago 2025): más de 1700 cines; 18 a 20
  millones de dólares; **la primera vez que Netflix gana un fin de
  semana de taquilla** en EE. UU.
  ([THR, entradas agotadas](https://www.hollywoodreporter.com/movies/movie-news/kpop-demon-hunters-singalong-box-office-sells-out-1236348539/)). ✅
- **Récord de Netflix**: la primera película en pasar de 300 millones de
  visualizaciones; nº1 13 semanas seguidas
  ([Netflix Tudum](https://www.netflix.com/tudum/articles/kpop-demon-hunters-most-popular-netflix-film)). ✅
- **TikTok**: el reto de baile de «Golden», con tutoriales en espejo
  ([@midnyt.team](https://www.tiktok.com/@midnyt.team/video/7535402512384298258));
  el **#takedownchallenge**, que lanzó el canal oficial con TWICE
  ([@icm_triplets](https://www.tiktok.com/@icm_triplets/video/7507677639918832927));
  y el **#SodaPopChallenge**. ⚠️ (sin vistas comprobadas)
- **Reddit**: «Your Idol» de los Saja Boys pasó los 300 millones de
  vistas; el hilo lo celebra con 459 votos
  ([r/KpopDemonhunters](https://www.reddit.com/r/KpopDemonhunters/comments/1p0cd9i/your_idol_by_saja_boys_hit_300_million_views_lets/)). ⚠️
- ⚠️ No se vio ningún vídeo de análisis largo (bloqueo de YouTube).

## 13 · Videojuegos de la franquicia (punto 11)

**No hay juego de pago** (nada en Steam): es una película. ✅
(búsqueda negativa)

**Sí hay un juego oficial gratis en Roblox**: «KPop Demon Hunters», de
**Twin Atlas** y **Makeshift** con Netflix, desde el **19-dic-2025**
([blog de Twin Atlas](https://twinatlas.com/blog/19dec2025_KPopDemonHuntersTA);
[ficha en Roblox](https://www.roblox.com/games/118806061296143/KPop-Demon-Hunters)). ✅

- **Qué se hace**: crear tu propio *trainee* de K-pop (ropa, peinado,
  maquillaje), recorrer un **Seúl de Roblox** con sitios de la película
  (la **HUNTR/X Tower** se puede visitar), pelear contra demonios con
  armas como las del film, bailar coreografías para «restaurar el
  Honmoon» y comprar ropa, mascotas y muebles. ✅
- **Ropa real y virtual a la vez**: el jersey de oso polar de Mira, el
  pantalón de pijama de Rumi y la camiseta «Faded» existen como prenda
  y como cosmético. ✅
- **Interfaz**: letra **Builder Sans** de Roblox (§6). El inventario es
  una **rejilla de iconos cuadrados**, esquinas redondeadas, gris oscuro
  translúcido: `#1C1D24` y `#4F4448`, con acentos de cada prenda
  (`#137AF3` azul, `#DD7D79` coral). El logo del juego es el de la
  película con «NETFLIX» en rojo debajo. ✅ (capturas oficiales,
  medidas con `estilo.py`)
- **Las 9 capturas oficiales**: inventario, selección de personaje,
  pelea con espada, estudio de grabación, fogata, puesto de *corndogs*,
  fila de 5 avatares. **Ninguna tiene caja de diálogo.** ⚠️
- **The Cutting Room Floor**: bloqueado por Cloudflare en los dos
  intentos. ⚠️
- **Juegos que NO son oficiales** (no usarlos de referencia): «Kpop
  Demon Hunters Battle», «KPop Demon Hunters Playground» y «Kpop Demon:
  Piano Game» en
  [Google Play](https://play.google.com/store/apps/details?id=com.pg.kpop.demon.hunters.game). ⚠️
- **Dentro de otros juegos**: Fortnite y CookieRun: Kingdom (§24). ✅

## 14 · Lo que ama el fandom, y qué NO hacer (punto 12)

**Memes y chistes internos** (página de memes de
[TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Memes/KPopDemonHunters),
leída entera):

- **«No thoughts, only Derpy»** (o «No thoughts, head empty, only
  Derpy»): el más repetido. Nació de un corto oficial de Netflix con las
  caras de **Derpy**, el tigre azul
  ([Netflix Tudum, ficha de Derpy](https://www.netflix.com/tudum/articles/kpop-demon-hunters-derpy-tiger-bio)).
  A Sussie la llaman «Hat Bird»; a Derpy, «Goofy Ass Tiger». ✅ (tres
  fuentes)
- **Los tres sabores de ramyeon**: «Rumi: Superstar Flavour. Mira:
  Spice Queen. Zoey: H A M B U R G E R.» ✅
- **«Rumi sniffing / eating kimbap»** y «Rumi smiling»: caras de Rumi
  usadas como reacción (hoja `vestuario_10` nº 478). ✅
- **«Jinu Running»** y el **«HEHEHE»** de Jinu. ✅
- Tras el final: **«Jinu is chilling in Rumi's sword»** y «Jinu is
  alive!». ✅
- **«The Cry Guys»**: los tres chicos que lloran citando a HUNTR/X. Al
  demonio que llora lo llaman **«Jelly»**. ✅
- **«Front Man»**: Gwi-Ma comparado con el villano de *El juego del
  calamar*; en habla hispana, porque los dobla el mismo actor (§10). ✅
- **#SodaPopChallenge** (§12). ✅

**Qué NO hacer** (lo que un fan notaría al instante):

1. **No escribir mal el título.** En latino es **«Las Guerreras
   K-Pop»**, sin «cazadoras» ni «demonios»
   ([Doblaje Wiki, datos de interés](https://doblaje.fandom.com/es/wiki/Las_guerreras_k-pop#Datos_de_inter%C3%A9s)). ✅
2. **No mezclar los nombres de las canciones**: «Dorada», «Nocaut» y
   «Soda Pop» (igual). ✅
3. **No hacer un dibujo animado genérico.** Fans surcoreanos (foro
   theqoo) llamaron al merch oficial de Netflix «tacky», «outdated» y
   «too Western»
   ([Koreaboo](https://www.koreaboo.com/news/kpop-demon-hunters-merch-criticism/)).
   Hay que imitar el lenguaje real del K-pop: carteles de *comeback*,
   *photocards*, *fancams*, rótulos de *variety show*. ✅
4. **No poner a los Saja Boys como malos planos.** Para muchos fans,
   Jinu «no es un demonio malo», y hubo enfado de verdad por su final
   ([Sportskeeda](https://www.sportskeeda.com/us/k-pop/news-why-protest-trucks-kpop-demon-hunters-fans-hilariously-react-unconventional-male-female-idols-interaction)). ✅
5. **No esconder las marcas de Rumi ni su vergüenza.** Es el corazón del
   personaje. Siempre «perfecta» vacía su arco. ✅
6. **No llamarla anime ni dibujarla en 2D.** La directora: «I don't
   [consider it anime]». Tampoco es Spider-Verse: es 3D con gestos de
   anime ([CBR](https://www.cbr.com/netflix-kpop-demon-hunters-not-anime/)). ✅
7. **No confundir el traje «Free»** (sudadera lila y vaqueros) con la
   **cazadora amarilla** (§16). ✅
8. **No usar una burbuja blanca** (§7). ✅
9. **No tomar de referencia los juegos falsos** de Google Play (§13) ni
   las copias piratas de la película en Internet Archive. ✅
10. **No dar por bueno el recuento de Danbooru** (§9). ✅

## 15 · Poses analizadas por personaje (punto 14)

Vistas fotograma a fotograma (vídeo) y en las hojas (redactor). Armas:
Rumi, espada de luz (**sa-in-geom**); Mira, alabarda curva
(**gok-do**); Zoey, dagas arrojadizas (**shin-kal**). ✅

### Rumi

| Dónde | Postura, manos, mirada | Sirve para |
|---|---|---|
| «How It's Done» [0:54](https://archive.org/details/youtube-QGsevnbItdU) | Puños en alto junto a Mira y Zoey, mirada al frente, negro y dorado, letrero detrás | **Presentar** |
| Tráiler [0:24](https://www.dailymotion.com/video/x9k1104?t=24) | Espada de luz en vertical, cuerpo hacia delante, ceño fruncido | Pelear, **animar** a la acción |
| «Golden» 1:48 | De pie ante el espejo, un brazo cruzado sobre el pecho, mirada baja, marcas visibles, bata | **Pensar** |
| «Golden» 2:12 | Sola en el centro, brazos en «V» hacia arriba, un pie adelantado, botas altas de cordones | **Celebrar** |
| «Golden» 3:02 | Camina del brazo de Mira y Zoey, una pierna en el aire (paso saltado), sonríe | Cierre, unidad |
| «Takedown» 1:48 | De perfil, micrófono junto a la boca, boca abierta, cabeza atrás, cazadora amarilla, foco azul cenital | **Explicar** cantando |
| Hoja `vestuario_10` nº 477 | Sentada, escribe en un cuaderno | **Explicar**, pensar |
| Hoja `vestuario_10` nº 433 | Media sonrisa segura, cazadora amarilla | Presentar, **regañar** con gracia |
| Hoja `personajes_01` nº 7 | Espada en diagonal, pierna adelantada | Pelear |
| Hoja `vestuario_10` nº 469 | Render cantando, cuerpo entero | Cantar |

### Mira

| Dónde | Postura, manos, mirada | Sirve para |
|---|---|---|
| Tráiler 0:24 | Gok-do en alto con los dos brazos, capa roja al vuelo, piernas abiertas | Pelear |
| «How It's Done» 0:54 | Gok-do en diagonal hacia arriba, de perfil, a un lado de Rumi | Presentar en grupo |
| «Takedown» 1:06 | Puño junto a la sien, ceja alzada, media sonrisa | **Regañar** con guiño, animar |
| Hoja `personajes_01` nº 23 | Cuerpo entero con el gok-do | Presentar |
| Hoja `personajes_01` nº 16 | Retrato: top negro, falda naranja, gok-do | Presentar |
| Hoja `vestuario_10` nº 448 | Dientes apretados, manos como garras | **Regañar** en serio |
| Hoja `vestuario_10` nº 449 | Cara de fastidio | Regañar |
| Hoja `vestuario_10` nº 435, 437 | Gorra, gafas, desconfía | **Pensar**, dudar |
| Hoja `vestuario_10` nº 470 | En batalla, luz verde | Pelear |

### Zoey

| Dónde | Postura, manos, mirada | Sirve para |
|---|---|---|
| «How It's Done» 1:06 | Primer plano, dagas turquesa en una mano en alto, ceja levantada, mirada a cámara | **Regañar**, advertir |
| Tráiler 0:24 | Dagas separadas en las dos manos, agachada hacia delante | Pelear |
| Hoja `personajes_01` nº 3 | Salto con los *shin-kal* | Acción |
| Hoja `personajes_01` nº 18 | Retrato: dagas en alto, top halter turquesa | Presentar |
| Hoja `vestuario_10` nº 440 | Rapea al micrófono, señala | **Explicar** |
| Hoja `vestuario_10` nº 457 | Pícara, puños junto a la barbilla | **Animar** |
| Hoja `vestuario_10` nº 458 | Manos juntas, suplica | Pedir algo |
| Hoja `vestuario_10` nº 466 | Abraza el disco de las Sunlight Sisters | **Celebrar** como fan |
| Hoja `vestuario_10` nº 453 | Disfrazada, brazos abiertos | Humor |

### Jinu y los Saja Boys

| Dónde | Postura, manos, mirada | Sirve para |
|---|---|---|
| Tráiler [1:20](https://www.dailymotion.com/video/x9k1104?t=80) | Primer plano tres cuartos, media sonrisa a cámara, chaqueta blanca a cuadros, pendiente, marca en el cuello | **Presentar** seduciendo |
| Hoja `vestuario_10` nº 438 | Silueta con *gat* y túnica negra, brazos abiertos | Amenazar |
| Hoja `concept_02` nº 60 | Retrato sonriente | Presentar |
| Hoja `concept_02` nº 89 | *Gat*, luz magenta, cara seria | Jinu demonio, momento serio |
| Hoja `personajes_01` nº 22, 24 | Traje del programa de juegos y traje «Soda Pop» | Ídolo |
| Tráiler [1:04](https://www.dailymotion.com/video/x9k1104?t=64) | Los cinco en fila, sombreros, contraluz azul | Presentar al grupo |
| «Soda Pop» 0:24-0:42 | En corro, brazos hacia una chica con capucha rosa | Celebrar en la calle ⚠️ |

### Las tres juntas

- **Presentar**: alineadas, armas en alto, cámara centrada, frase
  detrás («How It's Done» 0:54). ✅
- **Animar al público**: de espaldas, brazos en alto, contraluz blanco
  («How It's Done» 2:18). ⚠️
- **Celebrar**: trajes dorados (hoja `vestuario_10` nº 476). ✅
- **Humor**: comiendo ramyeon con los vasos de su nombre (hoja
  `concept_02` nº 84). ✅

**Qué pose para qué**: presentar → Rumi 0:54 o nº 433; explicar →
Rumi nº 477 o Zoey nº 440; celebrar → Rumi «Golden» 2:12; regañar →
Mira nº 448 o Zoey 1:06; pensar → Rumi «Golden» 1:48; animar → Zoey
nº 457 o Mira «Takedown» 1:06.

## 16 · Vestuario, con hex medidos (punto 15)

Hex medidos con `estilo.py` en las hojas de modelo oficiales de la wiki
(el % es del área; incluye el fondo del render). ✅ salvo lo marcado.

| Quién · traje | Hex | Qué es | Imagen |
|---|---|---|---|
| Rumi · «Takedown» | `#040419` `#5675A6` `#151636` `#AB7FBD` `#7A497A` `#40335F` | Traje táctico oscuro, chaleco azul acero, pelo lila | [Takedown Outfit](https://static.wikia.nocookie.net/kpop-demon-hunters/images/a/a5/Rumi_-_Takedown_Outfit.png), 3077×4096 |
| Rumi · «What It Sounds Like» | `#C0AFF5` `#6F65C1` `#C381B8` `#9F5398` `#E5D6F0` `#512264` | Gala lila y violeta, el del clímax | [WISL Outfit](https://static.wikia.nocookie.net/kpop-demon-hunters/images/a/a1/Rumi_-_What_It_Sounds_Like_Outfit.png), 3084×4096 |
| Rumi · «Free» | `#443E83` `#594EAA` `#8073D8` `#A790EE` `#875A8B` `#AF74A7` | **Sudadera lila y vaqueros** (no la cazadora) | [Free Outfit](https://static.wikia.nocookie.net/kpop-demon-hunters/images/5/59/Rumi_-_Free_Outfit.png), 3065×4096 |
| Mira · cuerpo entero | `#FCF9FC` `#100831` `#C9A5CE` `#2A1774` `#9A5BBA` `#9D335C` | Traje base, violetas y vino | [Full Body](https://static.wikia.nocookie.net/kpop-demon-hunters/images/3/3e/Mira_-_Full_Body.png), 2630×2356 |
| Zoey · «Golden» | `#CAA297` `#BF6D37` `#FDFDFD` `#D3BFCD` `#916F82` `#5C3230` | Dorado cobrizo | [Golden Outfit](https://static.wikia.nocookie.net/kpop-demon-hunters/images/8/8f/Zoey_-_Golden_Outfit.png), 2259×4096 |
| Jinu · «Soda Pop» | `#020202` `#C9C2BD` `#42678C` `#7F96AA` `#B17678` `#593958` | Camisa clara, vaquero azul, acento rosado | [Jinu sodapop](https://static.wikia.nocookie.net/kpop-demon-hunters/images/6/66/Jinu_sodapop.png), 1323×4467 |

**La ropa icónica: la cazadora amarilla de Rumi.** Amarilla, con
**hombrera de picos**, top corto, parches. Es la más repetida en
cosplay y en los renders (hojas `personajes_01` nº 17; `concept_02`
nº 56, 74; `vestuario_10` nº 433, 463, 469). Los parches y el patrón de
la manga se texturizaron por capas en Substance (§19). ✅
⚠️ **Sus hex no se midieron**: medir en
[Rumi Portrait](https://static.wikia.nocookie.net/kpop-demon-hunters/images/3/31/Rumi_Portrait.png/revision/latest?cb=20250725045033)
(2304×3072) antes de pintarla.

**Otros trajes, prenda a prenda** (wiki, Appearance):
- **Mira, «How It's Done»**: top corto negro con **ondas del Honmoon**
  azules, texto «WON'T MISS» rosa fuerte, minifalda vaquera azafrán,
  *norigae* (colgante coreano) carmesí. ✅
- **Zoey, «How It's Done»**: top halter turquesa con tiras de cuero
  negras y un loto rosa. ✅
- **Trajes dorados de gala**: Rumi (`concept_02` nº 86), Mira (nº 95;
  `vestuario_10` nº 443-446, chaqueta blanca con dorado), el trío
  (nº 441, 476). ⚠️ sin hex.
- **Fuera del escenario**: Mira con el jersey de oso polar
  (`personajes_01` nº 1, 25, 26), en bata y toalla (`vestuario_10`
  nº 450-452); Zoey disfrazada con sombrero amarillo y camisa floral
  (nº 436, 453-455, 460) y en pijama (nº 456); Rumi en bata (nº 439,
  462) y con sudadera rosa (nº 474-475). ✅
- **Mira en una gala** (archivo «Mirametgala»): abrigo acolchado
  negro hasta los pies (`vestuario_10` nº 447). ⚠️ la escena no se
  identificó
- **Jinu «Your Idol»** y los Saja Boys: **hanbok negro con *gat***
  (sombrero coreano de ala ancha), el disfraz de *jeoseung saja*
  (`concept_02` nº 75; `vestuario_10` nº 438). En su debut, ropa de
  calle pastel (`concept_02` nº 58). ✅

**Rasgos que nunca cambian** (wiki, Appearance):
- **Rumi**: **trenza *mohawk* morada** hasta las pantorrillas con
  *daenggi* (cinta) de seda dorada. Marcas moradas que brillan rosa.
  En modo demonio, el **iris izquierdo** pasa de castaño a dorado con
  pupila rasgada. En casa, a veces moño (nº 439). ✅
- **Mira**: pelo **rosa** hasta el muslo, con dos coletas y mechones a
  los lados; cejas negras (es teñida). La más alta (170 cm). ✅
- **Zoey**: pelo negro, **moños trenzados** y flequillo corto recto;
  **6 perforaciones en cada oreja**, pulsera dorada, aros de plata. La
  más baja (1,52 m). ✅
- **Jinu**: flequillo cortina negro, piel pálida y ojos marrones.
  Pendientes, collares y gafas de sol de ídolo. En forma demonio: piel
  morada con marcas, garras, dientes afilados, ojos dorados. ✅

**Colores de marca** (logos, §26): HUNTR/X `#677D9A` `#4F466A`
`#9A4893` sobre `#000000`; Saja Boys `#FC02A5` `#FD02BA`. ✅

## 17 · Ciudades, paisajes y fondos de pantalla (punto 16)

Paletas medidas de cada sitio en §5. Aquí, **la hora y la luz**:

| Sitio | Hora y luz | Dónde verlo |
|---|---|---|
| Seúl desde la **HUNTR/X Tower** | Noche, azul medianoche con luces turquesa, muy oscura (23%) | [HUNTRX_Tower_Full](https://static.wikia.nocookie.net/kpop-demon-hunters/images/d/d4/HUNTRX_Tower_Full.png), 1920×800 |
| **Namsan Tower** | Atardecer y anochecer, cielo lavanda (76%) | [Namsantowerkdh](https://static.wikia.nocookie.net/kpop-demon-hunters/images/a/ab/Namsantowerkdh.jpg), 964×600 |
| Seúl con el **Honmoon** encima | Atardecer, ondas turquesa y rosa sobre la ciudad | «Golden» 3:00 |
| Colina sobre Seúl (diseño del Honmoon, nachomolina) | Noche azul, silueta de espaldas | hoja `personajes_01` nº 29-30 |
| **Puente** o estación | Atardecer naranja y rojo, neón azul | «How It's Done» 2:48 |
| **Calle de Seúl** | Noche de neón magenta con luz dorada de tiendas | «Soda Pop» 0:24 |
| Escenario de los **Idol Awards** | Rojo y oro de templo, foco cenital | «Golden» 2:12 |
| **Han Clinic** | Luz plana de baño, gris azulado | «Golden» 1:48 |
| **Baños públicos** | Agua, niebla y reflejos; pelea con los *mul-gwishin* | §19 |
| **Bukchon Hanok** | Ladrillo diseñado a medida en Substance Designer | §19 |
| **Mundo Demonio** | Niebla, picos de roca, charcos, cielo cubierto | [wiki](https://kpop-demon-hunters.fandom.com/wiki/Demon_world) |

✅ (fotogramas, arte oficial y wiki)

**Fondos de pantalla en alta** (Wallhaven, sólo aptos; tamaño y ♥ de
la propia ficha; autor original enlazado). ✅ Son de fans: sólo
referencia.

| Tamaño | ♥ | Qué | Autor original |
|---|---|---|---|
| [10665×6000](https://w.wallhaven.cc/full/po/wallhaven-pojd1j.jpg) | 43 | «Wallpaper Huntrix» | [wickellia (DeviantArt)](https://www.deviantart.com/wickellia/art/Wallpaper-Huntrix-1281696651) |
| [8800×4950](https://w.wallhaven.cc/full/gw/wallhaven-gw7rdl.jpg) | 46 | Las tres, cazadora amarilla, nubes | [mietita (X)](https://x.com/mietita/status/1962709768302375195) |
| [6400×3600](https://w.wallhaven.cc/full/3q/wallhaven-3ql62d.jpg) | 49 | Pista de tenis | [lulusketches (Instagram)](https://www.instagram.com/lulusketches/p/DPcasjFAdWt/) |
| [5120×2880](https://w.wallhaven.cc/full/9o/wallhaven-9oz82w.jpg) | 65 | Versión mejorada del fondo final | [Reddit](https://www.reddit.com/r/KpopDemonhunters/comments/1mjwl2b/i_made_a_better_version_wallpaper_of_the_final/) |
| [3840×2160](https://w.wallhaven.cc/full/9o/wallhaven-9o678d.jpg) | 102 | El trío de pie | sin origen (subió Gone65478) |
| [3840×2160](https://w.wallhaven.cc/full/21/wallhaven-21od8m.jpg) | 77 | Rumi, Mira y Zoey | [lesly_oh (X)](https://x.com/lesly_oh/status/1938596689566199873) |
| [3840×2160](https://w.wallhaven.cc/full/je/wallhaven-jewyl5.jpg) | 69 | El trío | [ArtStation](https://www.artstation.com/artwork/98V4Vo) |
| [3840×2160](https://w.wallhaven.cc/full/w5/wallhaven-w5l86q.jpg) | 36 | Rumi, gatos, tigre, lluvia, paraguas | [DevinElleKurtz (X)](https://x.com/DevinElleKurtz/status/1958983294005268725) |
| [2700×1572](https://w.wallhaven.cc/full/gw/wallhaven-gw7qzl.jpg) | 74 | Ciudad pintada | [lulusketches (X)](https://x.com/lulusketches/status/1947345396310663274/photo/1) |
| [2560×1440](https://w.wallhaven.cc/full/vp/wallhaven-vpz5ql.jpg) | 75 | El trío (Jason Liang) | [Pixiv](https://www.pixiv.net/artworks/137893470) |
| [2400×3653](https://w.wallhaven.cc/full/3q/wallhaven-3q9wx6.jpg) | 115 | Chica, vertical (el más guardado) | [artelsia (X)](https://x.com/artelsia/status/1937126231201517817) |
| [3072×4096](https://w.wallhaven.cc/full/e8/wallhaven-e88q7k.jpg) | 58 | Cara de Rumi con lágrimas y grietas | [dannyisonfiree (X)](https://x.com/dannyisonfiree/status/1996042151168291077) |
| [1920×1255](https://w.wallhaven.cc/full/5y/wallhaven-5yy7g1.jpg) | 67 | El trío con armas, oscuro | [ArtStation](https://www.artstation.com/artwork/0lvelK) |

- ⚠️ No hay fondos de pantalla **oficiales** de Netflix en alta
  localizados; lo oficial más grande es el arte de la wiki (§3).
- La montaña con las caras de HUNTR/X y Saja Boys
  ([Mountain.jpeg](https://static.wikia.nocookie.net/kpop-demon-hunters/images/1/1e/Huntrix_and_Saja_Boys_Mountain.jpeg),
  2307×976) sirve de fondo panorámico. ✅

## 18 · Guía para generar con IA: imagen y texto (punto 17)

Hecha por el redactor con lo de §5-§17 y §19. Sirve para Firefly,
Canva o cualquier IA de imagen, y para una IA de texto. **La IA no
sustituye las referencias reales**: se usa para poses o fondos de
apoyo, y lo que salga se compara con las imágenes de abajo.

### Para la IA de imagen

**El estilo, en una frase.** Animación 3D estilizada de cine, con
expresiones de anime pero cuerpo y luz 3D; «alta costura» y
«K-drama»; colores suaves con neón de concierto; luz de foto de moda
editorial (§19).

**Rasgos que nunca cambian** (si falla uno, se rehace):
- **Rumi**: coreana de 23 años, **trenza *mohawk* morada muy larga**
  hasta las pantorrillas con cinta dorada, ojos castaños, marcas
  moradas en brazos y hombros (visibles u ocultas, según la escena).
- **Mira**: la más alta, **pelo rosa larguísimo** con dos coletas,
  cejas negras, gesto seco.
- **Zoey**: la más baja, pelo negro con **moños trenzados** y
  flequillo corto recto, muchas perforaciones en las orejas, sonrisa
  enorme.
- **Jinu**: chico coreano, flequillo cortina negro, piel pálida, media
  sonrisa, marca morada en el cuello; alto (180 cm).

**Paleta según el momento** (hex medidos en §5 y §16):

| Momento | Colores | Hex base |
|---|---|---|
| Pelea, demonios | Verde neón sucio sobre negro | `#A0B481` `#495745` `#000000` |
| Saja Boys, calle | Magenta y rosa de neón | `#C75CB4` `#FC02A5` |
| Triunfo de HUNTR/X | Rojo y oro de templo | `#E0C66B` `#AF8351` `#793121` |
| Final feliz | Lavanda pastel | `#ECD4FC` `#C5ADF5` `#8972D0` |
| Honmoon, magia | Azul místico | `#1D579B` `#244B7C` |
| Noche de Seúl | Azul medianoche con turquesa | `#060E1D` `#102E50` `#3E869C` |

**Línea y sombreado.** No hay línea negra de cómic. Sombra **por zonas,
suave**, con calidad de foto: ni *cel-shading* duro ni fotorrealismo.
Brillos de satén en la ropa, bordados con relieve.

**Luz.** Contraluz fuerte de concierto, focos cenitales, neón de color
según el momento. Brillo bajo (22-38%) en conciertos y peleas; los cielos lavanda
y el final suben (57-76%).

**Encuadre.** Plano cerrado a la cara, «pegado a la cabeza», como un
vídeo de TikTok o una *fancam*; en grupo, las tres en línea con Rumi en
el centro (§19).

**Palabras que ayudan** (en inglés suelen ir mejor): *stylized 3D
animated feature, Sony Pictures Animation look, K-pop idol, K-drama
lighting, high fashion editorial lighting, concert stage lights, neon
rim light, Korean girl group, soft color palette, expressive anime-like
eyes on 3D faces, satin fabric, embroidered stage outfit*.

**Palabras que lo estropean**: *anime, 2D, manga, cel shading,
Spider-Verse, comic book, speech bubble, chibi* (salvo para un gag),
*cartoon, Disney princess, photorealistic, Demon Slayer*. Tampoco
«demon hunter» a secas: puede salir un cazador genérico de fantasía.

**Vocabulario de gestos** (para pedirlos por su nombre):
- **Ojos de mazorca** (*corn eyes*) y **ojos de corazón rojo** que
  cambian de forma: el gag de cuando ven a los Saja Boys (hoja
  `concept_02` nº 93; §12). Cambio a estilo *chibi* sólo en ese golpe.
- **Marcas que brillan rosa** cuando Rumi se asusta o se estresa.
- **Iris izquierdo dorado** con pupila rasgada: Rumi en modo demonio.
- **Brazo cruzado tapando el otro brazo**: la vergüenza de Rumi
  («Golden» 1:48).
- **Brazos en «V»** hacia arriba: el triunfo («Golden» 2:12).
- **Armas de luz** que se invocan con el Honmoon: espada, alabarda
  curva, dagas (hojas `concept_02` nº 76-78).

**Imágenes de referencia de estilo y pose** (subirlas como referencia):
- Estilo general: hojas de modelo de §16 y
  [Rumi Portrait](https://static.wikia.nocookie.net/kpop-demon-hunters/images/3/31/Rumi_Portrait.png/revision/latest?cb=20250725045033).
- Pose de triunfo: «Golden» 2:12. Pose de pensar: «Golden» 1:48.
  Pose de grupo: «How It's Done» 0:54. Pelea: tráiler 0:24.
- Fondos: [HUNTRX_Tower_Full](https://static.wikia.nocookie.net/kpop-demon-hunters/images/d/d4/HUNTRX_Tower_Full.png)
  y [TheHonmoon1 setdesign](https://static.wikia.nocookie.net/kpop-demon-hunters/images/c/c2/TheHonmoon1_setdesign_nachomolina.jpg).

**Ejemplo de encargo a la IA** (Rumi para demos-canto): *Stylized 3D
animated feature film still, Korean K-pop idol girl, very long purple
mohawk braid with golden ribbon, yellow cropped jacket with spiked
shoulder pad, sitting in a recording booth writing lyrics in a
notebook, studio microphone with pop filter in foreground, soft
high-fashion lighting, violet and gold rim light, shallow depth of
field*.

### Para la IA de texto

**Cómo hablan** (del doblaje latino, §10):
- **Rumi**: frases de líder cuando hay público; a solas, frases que
  dudan, se corrigen y se quiebran («no lo entiendo, pero de alguna
  forma…»). Habla de su **voz** como de algo que se rompe o se cura.
- **Mira**: frases cortas y secas. Se define con adjetivos duros sobre
  sí misma. Poco adorno. Si se ablanda, lo dice sin rodeos: «me siento
  bien».
- **Zoey**: preguntas en cadena cuando está nerviosa (¿…? ¿…?).
  Entusiasta. Habla de sus **letras y libretas**.
- **Jinu**: burla ligera y coqueteo con Rumi; cuando habla de su culpa,
  baja el tono y se vuelve lento.
- **Celine**: rápida, urgente, protectora; propone planes («Cubramos…,
  resolvamos…»).
- **Gwi-Ma**: exclamaciones, amenazas, recuerda el «trato».
- **Honoríficos y jerga**: «Rumi Nim» (el doctor Han), *maknae*,
  *sunbae*, «¡gaja gaja gaja!» (§26). Escribir **Huntrix** y **Guima**
  como suenan en latino.

**Frases reales por emoción** (latino; ⚠️ las marcadas):

| Emoción | Frase | Quién |
|---|---|---|
| Alegre, orgullo | «Pero con ustedes dos significan algo. Yo tengo valor.» | Zoey |
| Alegre, grito de grupo | «¡Huntrix no se rinde!» ⚠️ (rótulo en inglés) | HUNTR/X |
| Enfadado, amenaza | «No creas que puedes escapar de tu realidad.» | Gwi-Ma |
| Enfadado, burla | «¿Qué eres, del siglo pasado?» | Jinu a Rumi |
| Explicando | «Cubramos tus marcas y resolvamos las cosas.» | Celine |
| Explicando, sincera | «Miren, soy una persona un poco difícil. Muy franca, temperamental, agresiva.» | Mira |
| Animando, consolando | «Puedes contármelo, voy a entender. Soy el único que puede.» | Jinu |
| Nerviosa | «¿Cómo lo resolvemos? ¿Qué sabrán los fans?» | Zoey |
| Triste | «Me recuerdan mi vergüenza, una vergüenza de la que no puedo escapar.» | Jinu |
| Triste que sana | «…de alguna forma mi voz estuvo sanando.» | Rumi |

- ⚠️ No hay una frase latina **de Rumi enfadada** ni **de Mira
  alegre** comprobadas: si hacen falta, escribirlas nuevas en su tono y
  decir que no son del guion.
- **Puntuación**: ¡! y ¿? siempre dobles. Mira casi sin exclamaciones.
  Zoey con muchas. Nada de «—» ni paréntesis en el texto de una lámina
  (regla del dueño).
- **Frases de canción**: en pantalla van en **inglés** tal cual
  («I'M GONNA SHOW YOU», «UP UP UP»), en mayúsculas, como grafismo.

## 19 · Estilo de dibujo, técnica, Photoshop y Blender (punto 18)

### Cómo quisieron que se viera

- **«Alta costura» y «K-drama»**: colores suaves, un estilo «entre
  caprichoso y contundente», luz de foto de moda (Nori Kaneko y Jody
  Tidsbury, Imageworks, en
  [No Film School](https://nofilmschool.com/kpop-demon-hunters-how-sony-pictures-imageworks-used-adobe-in-creating-the-global-phenomenon)). ✅
- **Bocas y ojos «muy coreanos»** al hablar, aunque el diálogo sea en
  inglés (Maggie Kang en
  [Cartoon Brew](https://www.cartoonbrew.com/feature-film/the-directors-of-kpop-demon-hunters-discuss-the-unexpected-challenges-of-making-an-animated-k-pop-film-247998.html)). ✅
- **3D, no 2D**: «wanted to translate that in a 3D way and not go 2D
  like Spider-Verse does» (Kang, en
  [CBR](https://www.cbr.com/netflix-kpop-demon-hunters-not-anime/)). ✅
  ⚠️ Alguna prensa habla de «menos fotogramas, como Spider-Verse»; se
  sigue a las directoras.
- **Gags *chibi***: en golpes de humor como los ojos de mazorca cambian
  a propósito a una estética *chibi*, por Los Simpson, Looney Tunes y
  Chaplin (Kang, en
  [Geeks OUT](https://www.geeksout.org/2025/07/16/interview-with-maggie-kang-creator-of-kpop-demon-hunters/)). ✅
  ⚠️ El sistema facial se llamaría «Chibi» (Josh Beveridge, director de
  animación): sale de un resumen, no del artículo.

### Programas y proceso (*making of*, con nombre y cargo)

| Paso | Programa | Quién lo cuenta |
|---|---|---|
| Animación de personajes | **Maya** | [Creative Bloq](https://www.creativebloq.com/art/animation/how-kpop-demon-hunters-animation-process-was-changed-by-unreal-engine-5) ✅ |
| Previsualización y *layout* | **Unreal Engine 5** con **OpenUSD**, por primera vez en Imageworks: exportar una secuencia pasó de 6-8 horas a 5 minutos | Jonghwan Hwang y Adam Holmes ([Unreal Engine](https://www.unrealengine.com/spotlights/reimagining-previs-and-layout-for-kpop-demon-hunters-with-unreal-engine)) ✅ |
| Multitudes | 7 cuerpos con ropa y pelo intercambiables; la herramienta **Foliage** (de vegetación) llena el estadio | Lillia Lai ✅ |
| Luces de concierto | Animadas en UE5 y pasadas a **Katana** con un *plugin* propio | Creative Bloq ✅ |
| Niebla y agua (pelea del baño) | Volumétricos en tiempo real en UE5 | Jason Baldwin ✅ |
| Texturas | **Substance 3D Painter** (ropa, *props*, Seúl), **Designer** (el ladrillo de Bukchon), **Sampler** con filtro de bordado (hanbok y trajes de HUNTR/X; la cazadora amarilla, por capas, con brillo **anisotrópico**) | Jody Tidsbury, que texturizó a Rumi ✅ |
| Variedad | Más de 1000 figurantes distintos; sólo la camiseta más común tenía 35 variantes | Tidsbury ✅ |
| Grafismo de conciertos | **After Effects** | Nori Kaneko ✅ |
| Referencia de actuación | El animador Daniel Ceballos se grabó actuando (planos «caóticos» de Zoey) | Creative Bloq ✅ |
| Títulos y créditos | Picturemill recortó los modelos (brazos, cuerpo, pelo, caras) y los animó como recortes 2,5D | [Picturemill](https://picturemill.com/portfolio/kpop-demon-hunters/) ✅ |

### Encuadres y composición

- **Pegado a la cabeza** (*head-locked*), como en TikTok, y cobertura
  de concierto en directo (Gary Lee, director de fotografía). ⚠️ (vídeo
  de Collider no visto)
- **Vergüenza**: plano cerrado, luz fría, silencio salvo su voz
  («Golden» 1:48). ✅
- **Triunfo**: plano general, la heroína sola en el centro, foco
  cenital, letrero gigante detrás («Golden» 2:12). ✅
- **Pelea**: las tres alineadas, cámara centrada, armas encendidas
  (tráiler 0:24). ✅
- **Seducción**: primer plano tres cuartos, mirada a cámara (tráiler
  1:20). ✅
- *Storyboards* de Simonbaek para ver cómo encuadra el estudio: hoja
  `concept_02` nº 68-73. ✅

### Cómo reproducirlo en Photoshop

1. **Sombra por zonas**: color plano por zonas, como un *cel*, y
   encima una capa en **Luz suave** con aerógrafo grande. Nada de
   bandas duras.
2. **Bordado de los trajes**: patrón limpio con *Superposición de
   motivo*, una capa de relieve (filtro **Relieve** / *Emboss*) para
   las puntadas y un brillo direccional en **Superponer** al 20-30%
   para el satén.
3. **Holográfico del logo HUNTR/X**: *Mapa de degradado* multicolor en
   **Sobreexponer color** sobre ruido difuminado en diagonal, con
   máscara sólo en los bordes del emblema (`#677D9A` `#4F466A`
   `#9A4893`).
4. **Neón de concierto**: contraluz de color del momento (§18) en
   **Trama** o **Sobreexponer color**, y el grafismo de letras con
   resplandor exterior.
5. Todo recorte pasa por `v3/integrar.py` (regla del dueño).

### Cómo reproducirlo en Blender

1. **Contorno**: **Freestyle** (por geometría), no *Solidify*, que
   aplana la luz de moda. Grosor fino.
2. **Sombreado**: *Shader to RGB* + *ColorRamp* de 2-3 escalones.
3. **Niebla del Mundo Demonio o del baño**: *Principled Volume* o
   *Volume Scatter* en un cubo, con la vista de Eevee.
4. **Luces de escenario**: *Light Linking* (Blender 4.x) para que los
   focos no ensucien los primeros planos.
5. **Caras exageradas**: *shape keys* con *drivers* para pasar de lo
   normal a los ojos de mazorca con un control.
6. **Multitudes**: nodos de geometría con instancias y material
   aleatorio por instancia.
7. **Modelos y *rigs* libres**: los de Sketchfab de §4 (CC BY, de fans,
   basados en Fortnite). ⚠️ Revisar escala y *rig*.
8. **Render**: ×2 para pruebas y ×3 la final; no pasar de ~4000 px
   (regla del dueño, no saturar su PC).

## 20 · Texturas 2D (punto 19)

**No hay tramas de manga**: es 3D. Las «texturas 2D» de esta película
son los patrones de la ropa, los símbolos y los efectos.

| Capa | Qué es en la película | Dónde verla | Equivalente libre |
|---|---|---|---|
| Bordado | Bordado coreano de hanbok y trajes de gala, hecho con Substance Sampler | Trajes dorados (hoja `vestuario_10` nº 443-446) | Relieve en Photoshop (§19) |
| Parches | Cazadora amarilla de Rumi, parches y manga por capas | `personajes_01` nº 17 | Cuero [Leather037](https://ambientcg.com/view?id=Leather037) (CC0) |
| Estampado floral | Camisa de Zoey disfrazada | `vestuario_10` nº 436, 453 | — |
| Ondas del Honmoon | Líneas onduladas azules en ropa y cielo | Top de Mira; «Golden» 3:00; efectos en `concept_02` nº 76-78 | Pintar a mano |
| Marcas de demonio | Patrones morados en la piel, con el «lenguaje de formas» del mapa Daedongnyeojido | [wiki, Demon](https://kpop-demon-hunters.fandom.com/wiki/Demon) | Modelo [«Patterns»](https://sketchfab.com/3d-models/none-547051dd1fcd4fcb95d6ccd5d0261c98) de MIKESTEEZ (CC BY) |
| Holográfico | Emblema de HUNTR/X, iridiscente | [Huntrix_Logo](https://static.wikia.nocookie.net/kpop-demon-hunters/images/2/25/Huntrix_Logo.jpg), 1194×1194 | Mapa de degradado (§19) |
| Purpurina y *foil* | Look de póster K-pop | Libro de pósters con *foil* (§3) | Pinceles de [BrushWarriors](https://brushwarriors.com/glitter-brushes-procreate/) ⚠️ |
| Trama de medios tonos | Para carteles y pegatinas | — | Pinceles de [Speckyboy](https://speckyboy.com/halftone-photoshop-brushes/) ⚠️ |
| Ladrillo de Bukchon | Diseñado en Substance Designer, no foto | §19 | ⚠️ las partes no dan uno |
| Metal dorado | Accesorios, Honmoon dorado | — | [Metal048A](https://ambientcg.com/view?id=Metal048A) (CC0) |

- **El Honmoon por colores**: azul normal, **dorado** completo,
  **arcoíris** al final
  ([glosario](https://kpopdemonhunterscoloringpages.com/glossary/honmoon)). ✅
- ⚠️ Los packs de pinceles de terceros declaran «gratis»: revisar la
  licencia al bajarlos.

## 21 · Gustos y detalles de cada personaje (punto 20)

De la ficha y la sección Trivia de la wiki; lo de Netflix Tudum y el
Instagram oficial, citado por la wiki. ✅ salvo lo marcado.

| | Rumi | Mira | Zoey | Jinu |
|---|---|---|---|---|
| Cumpleaños | 23 de octubre (Escorpio: «our Scorpio queen», Instagram oficial) | 22 de marzo | 21 de agosto | 17 de abril de 1623 |
| Edad | 23 o 24 (AMA de Maggie Kang en Reddit) | — | 22 o 23 | Más de 400; parece de 23 |
| Altura | ⚠️ no publicada | 170,4 cm (la más alta) | 1,52 m (la más baja) | 180 cm, 58 kg |
| Ramyeon | «Superstar» | **«Spice Queen»** (picante) | **Hamburguesa** (su lado de EE. UU.) | — |
| Objeto | Guitarra Fender Acoustasonic Telecaster decorada | Jersey de oso polar | Libretas de letras; colgante de tortuga | **Bipa** (laúd coreano), lo único que tenía de humano |
| Le encanta | Comer: kimbap y ramyeon (hojas `vestuario_10` nº 478, `concept_02` nº 65) | Su grupo, donde puede ser ella | **Las tortugas** (pijama, colgante, vídeos) y las Sunlight Sisters | Quiere olvidar su culpa |
| Apodos | «Popstar Royalty», «Rumi Nim» | «Oveja negra de la familia», «problem child» | «Cutest Maknae» | — |
| Cómo se ve | Con vergüenza de sus marcas | Como «difícil»: franca, temperamental | Sus letras le parecían «inútiles y raras» | Preso de su vergüenza |
| Curioso | Apellido probable: Kang (no «Ryu», que es de fans) | Look inspirado en la modelo Ahn So Yeon; pelo negro teñido | Nació en Corea, se crió en Burbank | Nombre por el dúo Jinusean; «murió» el 20-jun-2025, el día del estreno |

- Fuentes: [Rumi](https://kpop-demon-hunters.fandom.com/wiki/Rumi),
  [Mira](https://kpop-demon-hunters.fandom.com/wiki/Mira),
  [Zoey](https://kpop-demon-hunters.fandom.com/wiki/Zoey),
  [Jinu](https://kpop-demon-hunters.fandom.com/wiki/Jinu). La edad de
  Jinu, del guion citado por Deadline. ✅
- **La comida es parte del personaje**: los sabores de ramyeon salen en
  el merch oficial y son meme (§14). ✅
- ⚠️ «Superstar» para Rumi sale del meme de TV Tropes, no de su ficha.

## 22 · Por qué la gente la ama, y las escenas que hacen llorar (punto 21)

**Las cifras** ✅:
- **La película más vista de la historia de Netflix**: 325,1 millones
  de visionados (antes, *Red Notice*: 230,9) (The Hollywood Reporter,
  sep-2025).
- **481,6 millones** en la segunda mitad de 2025 y **52 semanas
  seguidas** en el top 10 mundial (Deadline, jul-2026).
- La película de *streaming* más vista de 2025 en EE. UU. según
  Nielsen: unos **20.500 millones de minutos**.
- Banda sonora: 4 canciones a la vez en el top 10 del Hot 100 y más de
  3.000 millones de reproducciones.
- **Ganó el Óscar**
  ([Wikipedia, premios](https://en.wikipedia.org/wiki/List_of_accolades_received_by_KPop_Demon_Hunters)).
  Hay fotos libres de la rueda de prensa del Óscar: los directores,
  4559×3039
  ([KOREA.NET en Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/1/1e/Chris_Appelhans_and_Maggie_Kang_-_KPop_Demon_Hunters_Academy_Award_Win_Commemoration_Press_Conference_-_55181088831.jpg),
  CC BY-SA 4.0). Hay más en `referencias.json`. ✅
- **Sing-along**: más de 1.300 funciones agotadas y nº1 de taquilla un
  fin de semana, meses después del estreno (Netflix Tudum).

**Por qué conecta**:
- **Aceptarse a una misma**: las marcas de Rumi son la metáfora de lo
  que escondes. Es el motivo más citado; Azul Bötticher cuenta que su
  *casting* fue con «Dorada», que habla de eso (Doblaje Wiki). ✅
- **Con quién se identifican**: con **Rumi**, «la más identificable»
  (Reddit) y «la más humana» (Collider). ✅ Mira es la favorita de
  quien prefiere a «la dura» (Reddit). ✅
- **Los villanos tienen matices**: niños entrevistados por CNN dicen
  que les gusta porque «Jinu no es un demonio malo»
  ([CNN](https://www.cnn.com/2025/08/23/entertainment/kpop-demon-hunters-kids-cec)). ⚠️
- **Es K-pop de verdad**: cantantes reales, TWICE en «Takedown», covers
  de ídolos (§24). ✅

**Las escenas que hacen llorar, reír o gritar**:

| Escena | Dónde | Qué pasa | Cómo está hecha | Reacción |
|---|---|---|---|---|
| 😢 **El sacrificio de Jinu** | Clímax. ⚠️ sin minuto (no hay clip) | Jinu se sacrifica por Rumi y recupera un instante el color humano de sus ojos | ⚠️ música y luz no comprobadas: no se vio la escena | **Jungkook (BTS)** contó que lloró ([Sportskeeda](https://www.sportskeeda.com/us/k-pop/news-he-s-real-fans-react-bts-jungkook-reveals-cried-kpop-demon-hunters-ending-calls-jinu-idiot-emotional-confession)) ⚠️; hilos de Reddit «heartbreaking finale» ✅ |
| 😢 **Rumi ante el espejo** | «Golden» 1:48 | Escribe en el vaho que quiere dejar atrás sus marcas | Plano cerrado, luz fría, silencio salvo su voz | La más citada para hablar de su vergüenza ✅ |
| 😢 **«Free»** | Dúo | Rumi sana su voz al confiar en Jinu | Canción a dos | — |
| 🙌 **Triunfo en los Idol Awards** | «Golden» 2:12 | Rumi sola, brazos en «V», «UP UP UP» | Rojo y oro, foco cenital | «Golden», nº1 del Hot 100 ✅ |
| 🙌 **Las tres con sus armas** | Tráiler 0:24 | Pose de batalla en niebla verde | Neón verde | La imagen de acción más reconocible ✅ |
| 😂 **Ojos de corazón** | Escena de los Saja Boys ⚠️ sin minuto | Los ojos de las chicas cambian a *six-pack* y a mazorca | Gag *chibi* | Lo explicaron los directores en un panel ([AOL](https://www.aol.com/articles/kpop-demon-hunters-directors-break-150000307.html)) ⚠️ |
| 😂 **Zoey no puede no bailar** | Dos veces con «Soda Pop» | Baila la canción de sus enemigos | — | ✅ (wiki) |
| 😂 **Derpy** | Varias | Las caras del tigre | — | El meme nº1 (§14) ✅ |

## 23 · Fan dubs y comunidad hispana (punto 22)

- **Cover de «Golden» en español latino**: «Las Guerreras KPOP |
  Huntrix - GOLDEN (Cover Español Latino)», de la cantante
  **HitomiFlor**
  ([YouTube](https://www.youtube.com/watch?v=nvtGsaMv9yc)). ⚠️ (YouTube
  pidió iniciar sesión: sin vistas ni duración)
- **TikTok**: «Las Guerreras Kpop: Doblaje y Música en Español», de
  [@melody._star](https://www.tiktok.com/@melody._star/video/7511256336668118278). ⚠️
  Y mucho contenido bajo búsquedas como «Golden audio en español
  completo», «Takedown en español latino» o «los actores de doblaje de
  las guerreras de k pop». Es tendencia en el TikTok hispano, sin cifras
  por vídeo. ⚠️
- **Fandub de casting**: un blog de usuario de Doblaje Wiki propone un
  reparto alternativo «localizado en México»
  ([FanDubbing22](https://doblaje.fandom.com/es/wiki/Usuario_Blog:FanDubbing22/LAS_GUERRERAS_K-POP_(Localizado_en_M%C3%A9xico))). ✅
- **Prensa hispana del doblaje**: ANMTV e Infobae publicaron quién dobla
  a quién (§10). ✅
- **Meme hispano**: el «Front Man» (Gwi-Ma y *El juego del calamar*,
  mismo actor latino). ✅
- **No se encontraron fandubs de escenas habladas** en Dailymotion ni en
  Internet Archive. Búsquedas: «Las Guerreras Kpop escena español
  latino», «KPop Demon Hunters clip doblaje latino», «fandub Jinu
  Rumi», «parodia». ⚠️
- **Para el servidor**: las muestras oficiales de §10 son el mejor
  material para un reto de doblaje: frase corta, emoción clara, voz
  medida.

## 24 · Colaboraciones, figuras y cosplay (punto 23)

**En otros juegos**:
- **Fortnite**, dos oleadas. 1.ª (2-oct a 1-nov-2025): Rumi, Mira y
  Zoey, pico y mochila de ramyeon para cada una y el gesto «Zoey's
  Thumbs Up»; lote completo, 3500 V-Bucks
  ([Forbes](https://www.forbes.com/sites/paultassi/2025/10/02/here-are-the-fortnite-kpop-demon-hunters-skins-and-cosmetics-prices/)).
  2.ª (6-feb-2026): HUNTR/X doradas y **Jinu** en dos trajes («Soda
  Pop» y el demoníaco de «Your Idol»); Rumi dorada trae un estilo con
  las marcas en brazos y piernas
  ([VICE](https://www.vice.com/en/article/kpop-demon-hunters-fortnite-wave-2-revealed-with-huntrix-golden-skins-jinu/),
  [Dexerto](https://www.dexerto.com/fortnite/fortnite-x-kpop-demon-hunters-release-date-skins-emotes-more-3260330/)). ✅
- **CookieRun: Kingdom** (versión 7.3): Rumi, Mira y Zoey Cookie (Rumi
  cuerpo a cuerpo rápida, Mira tanque, Zoey a distancia), trajes de
  HUNTR/X y Saja Boys, 4 edificios y el modo «Live! Survival on Stage»
  ([Pocket Gamer](https://www.pocketgamer.com/cookie-run-kingdom/kpop-demon-hunters-collab-now-live/),
  [esports.gg](https://esports.gg/news/cookie-run-kingdom/cookie-run-kingdom-kpop-demon-hunters-collab-new-idol-group-bites/)). ✅

**Marcas**:
- **McDonald's** (31-mar-2026): menú Saja Boys (Spicy Saja McMuffin
  con salsa de Gwi-Ma) y menú HUNTR/X (McNuggets, papas «Ramyeon
  McShaker», salsa Demon morada y salsa Hunter picante, 1 de 6 tarjetas
  holográficas); McFlurry «Derpy»
  ([Today](https://www.today.com/food/restaurants/kpop-demon-hunters-mcdonalds-rcna265117),
  [Game Rant](https://gamerant.com/kpop-demon-hunters-mcdonalds-collab/)). ✅
- **LEGO**: tema propio, primer set en preventa 2026-27
  ([LEGO](https://www.lego.com/en-us/themes/kpop-demon-hunters/about),
  [Brickset](https://brickset.com/article/129902/lego-kpop-demon-hunters-coming-soon!)). ✅
- **Guía oficial de productos**: cosmética Anua, muñecas Mattel,
  Hasbro, Furby, kits de ganchillo Woobles, ropa de Bershka
  ([Netflix Tudum](https://www.netflix.com/tudum/articles/kpop-demon-hunters-products-guide)). ✅
- **Tienda *pop-up***: Seúl (diciembre) y gira por Asia; en Hong Kong,
  New Town Plaza, del 18-dic al 11-ene: *photocards* lenticulares,
  *washi tape*, peluches, llaveros de mini-CD
  ([Time Out](https://www.timeout.com/hong-kong/news/theres-a-k-pop-demon-hunters-pop-up-opening-in-hong-kong-121725)). ⚠️
- ⚠️ No se encontró café temático oficial, ni Uniqlo, ni Crocs.

**Ídolos reales**: TWICE (Jeongyeon, Jihyo, Chaeyoung) cantan
«Takedown»; Cha Eunwoo bailó «Soda Pop» y cantó «Free» con Arden Cho;
An Yujin (IVE), Lily (NMIXX), Solar (MAMAMOO) y Urban Zakapa hicieron
covers de «Golden»
([Korea Herald](https://www.koreaherald.com/article/10541560),
[The Honey POP](https://thehoneypop.com/2025/08/04/k-pop-demon-hunter-covers/)). ✅

**Figuras oficiales** (su pose sirve de referencia 3D):
- **Youtooz**, con licencia de Netflix: vinilos de HUNTR/X y Saja Boys
  desde 29,99 $; cajas «figure and pin» (hoja `personajes_01`
  nº 34-36) y «Monitor Buddiez» (nº 13-14)
  ([Youtooz](https://youtooz.com/collections/kpop-demon-hunters),
  [Netflix Shop](https://www.netflix.shop/collections/kpop-demon-hunters-youtooz)). ✅

**Cosplay bien hecho** (fotos libres):
- Galaxy Con San José 2025, dos ángulos, 3000×2000
  ([Wikimedia Commons, John E. Manard](https://upload.wikimedia.org/wikipedia/commons/a/a2/Cosplay_of_KPop_Demon_Hunters_at_Galaxy_Con_San_Jose_2025.jpg),
  CC BY-SA 4.0). ✅
- Derpy y Sussie en la Japan Expo 2026, 2448×3264
  ([Wikimedia Commons, Eunostos](https://upload.wikimedia.org/wikipedia/commons/9/9d/Statue_du_tigre_bleu_et_de_la_pie_de_Kpop_Demon_Hunter_-_Japan_Expo_2026.jpg)). ✅
- **Materiales de la cazadora de Rumi** (tutorial casero): óvalo de
  fieltro negro con 4 picos cónicos pegados; camiseta de cuello alto con
  cinta de gargantilla; short negro con cinturón de fieltro rosa; trenza
  con tiza morada; menos de 10 $
  ([Life at Cloverhill](https://lifeatcloverhill.com/2025/10/diy-rumi-costume-kpop-demon-hunters-tutorial.html)). ⚠️

## 25 · Obras parecidas y láminas vecinas (punto 24)

**Lo que reconoce la directora, Maggie Kang**
([Geeks OUT](https://www.geeksout.org/2025/07/16/interview-with-maggie-kang-creator-of-kpop-demon-hunters/)):
- Cine que le ponía su padre: Kurosawa, Kieślowski, Chaplin, Wong
  Kar-wai, Kim Ki-duk, Kiarostami, Scorsese, Kubrick; y *Star Wars*,
  *Indiana Jones*, *Los Goonies*, Disney. ✅
- Humor: Los Simpson, Looney Tunes y Chaplin. ✅
- Su camino: DreamWorks, Blue Sky, DreamWorks otra vez, jefa de
  *storyboard* en *La Lego Ninjago Película*. ✅
- La idea nació de leer sobre demonología coreana y las *mudang*
  (chamanas); el K-pop llegó después
  ([Variety](https://variety.com/2025/tv/festivals/kpop-demon-hunters-creator-maggie-kang-favorite-character-1236525113/)). ✅
  Bong Joon-ho como inspiración para mezclar géneros. ⚠️ (Screendaily
  no se pudo abrir)

**K-pop real detrás**: HUNTR/X mezcla a **Itzy, Twice y Blackpink**;
los Saja Boys, a **TXT, BTS, Stray Kids, ATEEZ, BIGBANG y Monsta X**
(wiki, con Mashable y Forbes). ✅

**Obras parecidas** (Collider, 15 recomendaciones): *Demon Slayer*,
*Trollhunters*, *Star vs. the Forces of Evil* («la misma energía»),
*Totally Spies!* y *Martin Mystery*
([Collider](https://collider.com/shows-like-kpop-demon-hunters/)). ✅

**Láminas vecinas del servidor** (para no repetir ideas):
- `05-oshi-no-ko`: la doble vida de un ídolo y la industria por dentro.
- `38-sailor-moon`: grupo de chicas con armas mágicas.
- `97-bocchi-the-rock-bandas-y-bajones` y `10-k-on`: música en directo.
  **Bocchi ya propuso `#🎼・demos-canto`** (y hay una «demos-canto 2»
  con el teclado): el concepto A de aquí usa otro objeto (§27).
- `31-demon-slayer-kimetsu-no-yaiba` y
  `79-demon-slayer-paisajes-y-auras`: caza de demonios, mucho más seria.

## 26 · El mundo, la historia por arcos y sus símbolos (punto 25)

**Las reglas del mundo en cinco líneas**
([wiki, Honmoon](https://kpop-demon-hunters.fandom.com/wiki/Honmoon);
[Demon](https://kpop-demon-hunters.fandom.com/wiki/Demon)):
1. Los demonios comen almas humanas. Los gobierna **Gwi-Ma** desde el
   Mundo Demonio.
2. Sólo **la voz y la música** crean y sostienen el **Honmoon**, la
   barrera. Nació de rituales de *mudang* y hay que renovarla siempre.
3. Las cazadoras son linajes secretos de mujeres que en público son
   ídolos. Hay una generación nueva cada década o así; HUNTR/X es la
   primera desde las **Sunlight Sisters** de los 90.
4. Un humano se vuelve demonio por un pacto con Gwi-Ma nacido de la
   desesperación. La piel se llena de «patrones». Sólo aceptarse a uno
   mismo lo revierte.
5. El color del Honmoon cuenta la historia: **azul** normal, **dorado**
   completo (la meta de HUNTR/X), **arcoíris** al final: más fuerte,
   pero no perfecto.

✅

**La historia por arcos**
([wiki, Timeline](https://kpop-demon-hunters.fandom.com/wiki/Timeline)):
- **Hace siglos**: tres *mudang* crean el primer Honmoon con música.
- **Hace 400 años**: Jinu, plebeyo de Joseon, pacta con Gwi-Ma: voz
  preciosa y favor del rey a cambio de abandonar a su familia. Acaba
  demonio.
- **Siglo XX**: cazadoras en los años 20, 40, 60 y 80. En los 90, las
  Sunlight Sisters y el primer **International Idol Awards**.
- **Hace 5 años**: Celine elige a Rumi, Mira y Zoey. HUNTR/X gana los
  Idol Awards cinco años seguidos.
- **La película**:
  1. Los demonios asaltan su avión; después, **«How It's Done»**.
  2. **«Golden»**: el Honmoon empieza a volverse dorado.
  3. Llegan los **Saja Boys** con **«Soda Pop»** y se hacen virales en
     el programa *Play Games With Us* (en latino, «**Jueguen con
     nosotros**»).
  4. Guerra de canciones: el *diss track* **«Takedown»**.
  5. Rumi y Jinu se acercan: **«Free»**. ⚠️ la Timeline no dice en
     qué punto exacto
  6. Ruptura pública de HUNTR/X en los Idol Awards (la wiki la llama
     «fingida»). ⚠️ revisar con la película
  7. **«Your Idol»** en la Namsan Tower rompe el Honmoon; entra Gwi-Ma.
  8. **«What It Sounds Like»**: Rumi se acepta, Jinu se sacrifica, nace
     el Honmoon arcoíris.

✅ (wiki, cruzada con la ficha del film)

**Emblemas** (vistos y medidos):
- **HUNTR/X**: cuadrifolio holográfico (cuatro óvalos en cruz) con una
  **H** blanca; debajo «HUNTR/X» con la X como una diagonal ancha.
  `#677D9A` `#4F466A` `#9A4893` sobre negro. 1194×1194. ✅
- **Saja Boys**: «SAJA» a pincel en blanco y «BOYS» en magenta, con una
  cabeza de león o tigre en un escudo de cinco lados. `#FC02A5`. ✅
- **La película**: la estrella de cuatro puntas (§6). ✅

**Objetos icónicos** (objetos chamánicos coreanos reales,
[Korean Cultural References](https://kpop-demon-hunters.fandom.com/wiki/Korean_Cultural_References),
que cita a KoreaTlas y Korea Travel Post):
- **Sa-in-geom** (사인검), la espada de Rumi: «espada de los cuatro
  tigres», forjada en el año, mes, día y hora del tigre. ✅
- **Gok-do / wol-do** (곡도/월도), la alabarda curva de Mira. ✅
- **Shin-kal** (신칼), las «cuchillas divinas» de Zoey. ✅
- **Bipa** (비파), el laúd de Jinu. ✅
- **Gat** (sombrero negro de ala ancha) de los Saja Boys. ✅ (hojas)
- **Los vasos de ramyeon** con el nombre de cada una (`concept_02`
  nº 84). ✅

**Vocabulario que un fan reconoce al instante** ✅:
- **Honmoon** (혼문): «puerta del alma».
- **Mudang** (무당): chamana coreana.
- **Dokkaebi** (도깨비): duendes y demonios comunes.
- **Jeoseung saja** (저승사자): el mensajero del inframundo. De ahí el
  nombre y el disfraz de los Saja Boys, aunque en público dicen que
  *saja* es «león».
- **Mul-gwishin** (물귀신): fantasmas de ahogados, los demonios del baño.
- **Maknae** (막내): la más joven. **Sunbae / hoobae** (선배/후배):
  veterano y novato.
- **The Pride**: el club de fans de los Saja Boys (*saja* = león).
- **Fansign** (팬사인): firma de autógrafos.
- **Gaja gaja gaja** (가자): «¡vamos!».
- **Daedongnyeojido** (대동여지도): el mapa histórico de Corea cuyas
  formas inspiran las marcas de los demonios.
- **Derpy** (el tigre) y **Sussie** (la urraca): de la pintura popular
  *jak-ho-do*.

## 27 · Tres conceptos de lámina

Tres ideas distintas, una por canal de §0. Las tres usan un **objeto
real en un sitio real** de la película y el cuadro de diálogo propio de
la serie (§7), nunca una burbuja. Textos del canal copiados de
`servidor/inventario.md`.

### A · El cuaderno de letras en la cabina (`#🎼・demos-canto`) ⭐

- **Objeto y sitio**: un **cuaderno de letras abierto** sobre el atril
  del **estudio de grabación de la HUNTR/X Tower** (existe en la
  película, §5). En Blender: cuaderno de espiral con hojas curvas y
  arrugadas, **micrófono de estudio con filtro antipop**, auriculares
  colgados. La tinta sigue la curva del papel.
- **Personaje**: **Rumi**, la más querida y la que canta (§9). Detrás
  del cristal de la cabina, **de perfil, cantando al micro, cabeza
  atrás** («Takedown» 1:48). Referencia del gesto de escribir: hoja
  `vestuario_10` nº 477
  ([imagen](https://static.wikia.nocookie.net/kpop-demon-hunters/images/7/75/Rumi_writing_notes_for_Take_Down.jpg/revision/latest?cb=20260617125554)).
  Cazadora amarilla: `personajes_01` nº 17. El estudio real: «Takedown»
  0:30-1:00.
- **Cómo habla**: **con su letra a mano**, como en el espejo del Han
  Clinic («Golden» 1:48). Letra **Caveat**. El título, en la tapa, en
  **Hunters K-Pop**.
- **Dónde va cada texto**:
  - Tapa del cuaderno: **demos-canto**.
  - Página izquierda, a mano: «Tu ficha de canto, aparte de la de
    doblaje.» y «Un hilo con tu registro y tus covers.»
  - Margen, como nota de Rumi: «…de alguna forma mi voz estuvo
    sanando» (frase real del doblaje, §10).
  - Página derecha: las **etiquetas** como pestañas o pegatinas de
    colores: registros (Soprano, Mezzosoprano, Contralto, Tenor,
    Barítono, Bajo, Falsete, Growl), estilos (Balada, Rock, Pop, Anime
    OP/ED) y estado (Disponible, Ocupado). Si no caben, **lámina 2**.
  - Una esquina: «Lee el hilo fijado» con una flecha a mano.
- **Que no quede plano**: el micro y el antipop **delante**, un poco
  desenfocados; Rumi detrás del cristal con reflejo; contraluz violeta
  y dorado de concierto (`#533B42` `#E0C66B`); ondas tenues del Honmoon
  en el cristal.
- **Lámina 2** (etiquetas): un **álbum de *photocards***, una por
  etiqueta, como las *photocards* lenticulares del *pop-up* (§24). Cada
  registro con una cara del trío cantando (`vestuario_10` nº 440, 461,
  469).

### B · El escenario de los Idol Awards (`🎭・Escenario`)

- **Objeto y sitio**: el **escenario de los Idol Awards**, con su
  decorado de templo coreano rojo y oro y un **micrófono de pie** en el
  centro. En Blender: tarima, pilares, telón y la pantalla gigante del
  fondo, donde va el grafismo.
- **Personaje**: **Rumi sola, brazos en «V»**, un pie adelantado
  («Golden» 2:12). Variante en grupo: HUNTR/X doradas (`vestuario_10`
  nº 476) o el trío con los puños en alto («How It's Done» 0:54). Cuerpo
  entero para recortar: `personajes_01` nº 39
  ([Rumi IdolAwards Render](https://static.wikia.nocookie.net/kpop-demon-hunters/images/c/cd/Rumi_IdolAwards_Render.png/revision/latest?cb=20260626093239)).
- **Cómo habla**: con **grafismo de concierto**, como «UP UP UP»:
  mayúsculas enormes detrás de ella, en **Anton**, con resplandor dorado.
  Lo explicativo, como **subtítulo de Netflix** (blanco con sombra,
  **Roboto**).
- **Dónde va cada texto**:
  - Pantalla del fondo, gigante: **ESCENARIO**.
  - Subtítulo, línea 1: «Charlas, entrevistas y directos.»
  - Subtítulo, línea 2: «Sube quien invita el anfitrión.»
  - Un cartel pequeño en hangul y español en el atril, como el del Han
    Clinic (**Noto Sans KR**).
- **Que no quede plano**: el **público de espaldas en silueta** delante,
  con los brazos en alto («How It's Done» 2:18); **foco cenital** y humo;
  rojo y oro (`#E0C66B` `#AF8351` `#793121`).

### C · Los tres vasos de ramyeon (`#😂・memes`)

- **Objeto y sitio**: los **tres vasos de ramyeon** con el nombre de
  cada una (`concept_02` nº 84, 65) en la mesa de la **cocina de la
  HUNTR/X Tower**, de noche. En Blender: vasos de cartón con tapa medio
  abierta, palillos, vapor.
- **Personaje**: **Derpy**, el tigre azul, el más querido de meme
  (§14), asomado detrás de los vasos, con Sussie al lado. Referencias:
  su ficha en
  [Netflix Tudum](https://www.netflix.com/tudum/articles/kpop-demon-hunters-derpy-tiger-bio)
  y, para el volumen en 3D, la estatua de la Japan Expo 2026 (§24).
  ⚠️ No hay imagen de Derpy en las hojas. Y **Rumi
  comiendo kimbap** con las mejillas llenas (`vestuario_10` nº 478), la
  cara de meme.
- **Cómo habla**: la etiqueta impresa de cada vaso y el **subtítulo de
  Netflix amarillo sobre negro** (el estilo de alto contraste), que
  parece un meme.
- **Dónde va cada texto**:
  - Etiquetas de los vasos: «Superstar», «Spice Queen» y «H A M B U R G
    E R» (el meme de verdad).
  - Tapa del vaso del centro: **memes**.
  - Subtítulo amarillo: «El meme, sin más.»
  - Un *post-it* pegado en un vaso, a mano (Caveat): «Si lo doblas, va a
    fandub-de-memes.»
- **Que no quede plano**: **vapor y palillos delante**, en diagonal hacia
  cámara; luz cálida de cocina contra la ventana azul de Seúl de noche
  (`#060E1D` `#102E50`); poca profundidad de campo.

⚠️ Ninguno de los tres se ha probado a 1200×800: si el A se satura, las
etiquetas van a la lámina 2.

## 28 · Lo que no pude verificar, y lo que corregí de las partes

### Corregido al mirar las hojas (antes → ahora)

| Parte | Decía | Es |
|---|---|---|
| imagen | El traje «Free» de Rumi es la cazadora amarilla | «Free» es **sudadera lila y vaqueros** (`personajes_01` nº 6). La cazadora amarilla es su look habitual (nº 17) |
| imagen | Rumi con la espada, nº 8 y 23 | nº 8 y 23 son **Mira** con el gok-do. Rumi con espada: nº 7 y 15 |
| imagen | Seúl de noche «desde la torre», nº 29-30 | Es el diseño del Honmoon de nachomolina: silueta en una colina |
| imagen | Merch de Saja Boys, nº 46-49 | nº 46-48 (la hoja acaba en el 48) |
| imagen | Hoja de gestos de combate de Rumi, nº 77 | nº 76-78 son las hojas de **invocación de armas** del Honmoon |
| imagen | Honmoon *drum*, *ring* y *sprites*, nº 84-86 | Son nº 76-78. El 84 es **el trío comiendo ramyeon** |
| imagen | Disfraces de Zoey, nº 449-456 | nº 436, 453-455 y 460. El 449 es Mira; el 456, Zoey en pijama |
| imagen | Trajes dorados de Mira, nº 441-448 | nº 443-446. El 447 es Mira en una gala; el 448, Mira furiosa |
| imagen | Jinu con capucha negra, nº 438 | Jinu «Your Idol»: silueta con *gat* y túnica |
| imagen | Cazadora amarilla en «hoja 9, nº 63-64» | La hoja 9 no está en `hojas/`. Sí sale en `concept_02` nº 63-66 |
| vídeo | En «Takedown» 1:48 Rumi lleva coleta, «distinto al habitual moño» | Lo habitual es **la trenza larga** (wiki); el moño sale en casa (nº 439) |
| vídeo y voz | Zoey con dagas y «HUNTRIX DON'T QUIT!» | Vídeo lo pone en «How It's Done» 1:06; voz, en «Takedown» 1:06. Se sigue a vídeo, que sacó los fotogramas. ⚠️ |
| texto | «50,000 fans are waiting for you» como pantalla de móvil | Es letra del grafismo (lo corrigió la propia parte de texto) |
| voz | Recuento de Danbooru | Mezcla otras obras: descartado |

### Lo que falta o sigue dudoso

- **Hex de la cazadora amarilla**: sin medir. Medir en Rumi Portrait
  (§16).
- **Altura de Rumi**: no publicada.
- **Minuto del sacrificio de Jinu** y de los ojos de corazón: no hay
  clip. Sin música ni luz comprobadas.
- **Caras de Mira, Gwi-Ma y Celine** con minuto: sólo hojas sin minuto.
- **Fotogramas en 1080p**: `fotogramas.py` baja a 720p.
- **YouTube**: pidió iniciar sesión. Sin vídeos de análisis, sin vistas
  del cover de HitomiFlor, sin el vídeo de Gary Lee en Collider.
- **Frases del doblaje**: minutos de la muestra, no de la película; no
  hay clips oficiales doblados. Celine (canciones), Gwi-Ma y los
  secundarios, una sola fuente.
- **Letras sin comprobar**: Blanka (de pago); la letra exacta de
  «SHINING» y «HAH».
- **Caja de diálogo del juego de Roblox**: ninguna captura la muestra.
- **Bloqueados**: The Cutting Room Floor (Cloudflare), Wayback Machine
  (fallo de red), Screendaily (verificación), IMDb.
- **Sistema facial «Chibi»**: nombre sacado de un resumen.
- **Película entera con `episodio.py`**: no se hizo (presupuesto).
- **Café temático, Uniqlo, Crocs**: no encontrados.
- **GitHub**: no se buscó.

## Cumplimiento del encargo

✅ hecho y confirmado · ⚠️ a medias, una fuente o comprobado que no
existe · ❌ no se buscó.

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | Artbook, libro de pósters, key art, 478 imágenes grandes de la wiki; 3 hojas miradas número a número (§3) |
| 2 · Fotogramas con minuto | ⚠️ | 22 escenas con minuto del tráiler y 4 *lyric videos* oficiales (§2); a 720p, no 1080p; minutos del clip, no de la película; capturas 4K sin minuto |
| 3 · Fan art y 3D con licencia | ✅ | Safebooru con autor original; 11 modelos de Sketchfab con licencia (§4). ⚠️ mallas sin abrir |
| 4 · Fondos, paleta y texturas reales | ✅ | 16 paletas hex medidas, luz de cada sitio, texturas CC0 de AmbientCG (§5) |
| 5 · Tipografía por uso | ✅ | 9 usos, 8 letras libres comprobadas con fontTools (§6). ⚠️ Blanka y «SHINING» sin comprobar |
| 6 · Cómo hablan en pantalla | ✅ | Cinco recursos reales con minuto (§7). ⚠️ sin caja de diálogo en Roblox |
| 7 · Popularidad | ⚠️ | No hay encuesta oficial por personaje (buscada). Sí YouGov, ranking de Collider y hilos de Reddit con votos (§9) |
| 8 · Doblaje latino | ⚠️ | Reparto principal en dos o tres fuentes; 6 frases textuales de las muestras oficiales (§10). Minutos de la muestra, sin clip doblado; varios secundarios con una fuente |
| 9 · Música y sonido | ✅ | Lista completa, voces reales, récords, escenas emotivas (§11). ⚠️ efectos de sonido, oídos en un clip |
| 10 · Vídeos con minuto | ⚠️ | Tráiler, teaser, 4 *lyric videos*, *scenepack*, tendencias de TikTok (§12). YouTube bloqueado: sin análisis largos ni vistas de TikTok |
| 11 · Videojuegos | ⚠️ | Juego oficial de Roblox con interfaz medida; comprobado que no hay juego de pago (§13). Sin caja de diálogo; TCRF bloqueado |
| 12 · Lo que ama el fandom y qué no hacer | ✅ | Memes de TV Tropes y Netflix; 10 «no hacer» con fuente (§14) |
| 13 · Personajes a fondo | ⚠️ | Rumi, Mira, Zoey, Jinu y secundarios con carácter, arco, voz medida y dinámicas (§8). Caras con minuto sólo de Rumi, Zoey y Jinu; Mira, en hojas sin minuto; Gwi-Ma y Celine, sólo voz |
| 14 · Poses analizadas | ✅ | 10 de Rumi, 9 de Mira, 9 de Zoey, 7 de Jinu y los Saja Boys, con minuto u hoja, y qué pose para qué (§15) |
| 15 · Vestuario con hex | ⚠️ | 6 trajes con hex medidos, prendas y rasgos fijos (§16). La cazadora amarilla, la ropa icónica, sin hex |
| 16 · Ciudades y fondos de pantalla | ✅ | 11 sitios con hora y luz; 13 fondos de fans con tamaño, ♥ y autor (§17). ⚠️ sin fondos oficiales en alta |
| 17 · Guía para IA | ✅ | Hecha por el redactor: rasgos, paleta, luz, encuadre, palabras, referencias y frases reales por emoción (§18) |
| 18 · Estilo y técnica | ✅ | *Making of* con nombres y cargos, programas, encuadres, recetas de Photoshop y Blender (§19). ⚠️ nombre del sistema «Chibi» |
| 19 · Texturas 2D | ✅ | 10 capas con equivalente libre o cómo hacerlas (§20). ⚠️ licencias de pinceles de terceros |
| 20 · Gustos y detalles | ✅ | Tabla de los cuatro con cumpleaños, altura, comida, objeto y apodos (§21). ⚠️ altura de Rumi no publicada |
| 21 · Por qué la aman | ⚠️ | Cifras, razones y 8 escenas (§22). El sacrificio de Jinu, la que más hace llorar, sin minuto ni música comprobada |
| 22 · Fan dubs y comunidad hispana | ⚠️ | Cover de HitomiFlor, TikTok, blog de fandub de Doblaje Wiki (§23). Sin vistas; no hay fandubs de escenas habladas (buscados) |
| 23 · Colaboraciones, figuras y cosplay | ✅ | Fortnite, CookieRun, McDonald's, LEGO, *pop-up*, Youtooz, cosplay libre (§24) |
| 24 · Obras parecidas | ✅ | Influencias de la directora, K-pop real, 5 obras parecidas y 6 láminas vecinas (§25) |
| 25 · Mundo, historia y símbolos | ✅ | Reglas en 5 líneas, historia por arcos, emblemas medidos, objetos y vocabulario (§26) |
| Conceptos de lámina | ✅ | Tres distintos, con objeto en Blender, personaje, cuadro de diálogo, textos y profundidad (§27) |
| Fuentes distintas | ✅ | 75 webs distintas enlazadas en el cuerpo (revisar.py) |
| Fuentes oficiales | ✅ | Netflix Tudum, Picturemill, Unreal Engine, Twin Atlas, entrevistas a directores y staff con cargo |
| Otros idiomas | ⚠️ | Obra de EE. UU. en inglés: se buscó en inglés y español; el coreano llega por la wiki (hangul) y la prensa coreana. Sin búsquedas en coreano, japonés ni chino |
| Wikis, TV Tropes, TCRF, Wayback | ⚠️ | Fandom, Doblaje Wiki y TV Tropes sí; TCRF y Wayback bloqueados en dos intentos |
| Foros y comunidades | ✅ | Reddit (y Arctic Shift), theqoo vía Koreaboo, foro de dafont, foro de Roblox |
| Arte | ✅ | Safebooru, X, Tumblr, Pixiv, ArtStation, DeviantArt, Wallhaven |
| Vídeo | ⚠️ | Dailymotion e Internet Archive con minuto; YouTube pidió sesión |
| Código y recursos | ⚠️ | Sketchfab, AmbientCG, Fontsource y API de Roblox sí; GitHub no se buscó |
| Doblaje latino | ✅ | Doblaje Wiki por su API, ANMTV, Infobae |
| Hojas de contacto | ✅ | 3 JPEG de menos de 700 KB, miradas por el redactor (§3) |
| `referencias.json` | ✅ | 186 referencias: 174 de las partes y 12 del redactor, con tamaño medido |

## 29 · Bitácora de búsqueda

**Del redactor** (25 y 26-sep):
- Primera sesión: §0 a §5 y las 3 hojas miradas; se cortó ahí.
- Segunda sesión (modo «seguir»): §6 a §29 y la tabla, sólo con las
  cuatro partes, los `datos-*.md` (por `grep`) y las hojas, que volvió
  a mirar para las poses y las correcciones de §28.
- `juntar_referencias.py` (174) y `juntar_bitacora.py`. La API de la
  wiki (`action=query&prop=imageinfo`) sólo para el enlace y el tamaño
  de 12 imágenes ya vistas en las hojas.
- Confirmado a la vez en dos partes: reparto latino, armas, rasgos
  fijos, minutos de «Golden». Contradicción sin resolver: el minuto de
  Zoey con dagas (§28).

Lo que sigue son las bitácoras de las cuatro partes, tal cual.


### Bitácora de imagen

- Español: «Las Guerreras K-pop vestuario colores», «Las Guerreras K-pop fondos de pantalla» — sin resultados propios en español más allá de calcos de EN; se priorizó inglés/coreano transliterado por ser producción reciente sin mucha cobertura hispana.
- Inglés (WebSearch, ~10 búsquedas): artbook/concept art, key visual poster, Fortnite collab, McDonald's collab, LEGO/Uniqlo/cafe, Honmoon symbol/logo, real idol cameos, Cookie Run Kingdom collab, cosplay tutorial, Youtooz figures, character designer interview.
- Fandom API (`api.php`) directa, sin bloqueo: fichas de Rumi/Mira/Zoey/Jinu (`Appearance`), Honmoon, HUNTR/X Tower, Namsan Tower, Demon world, categoría `Locations`; imágenes bajadas con cabecera `Referer: https://www.fandom.com/` (sin esto da 403).
- `herramientas/investigar_serie.py` reejecutado (la carpeta de hojas del recolector ya no existía en el contenedor): 10 hojas nuevas en `herramientas/referencias/las-guerreras-k-pop-kpop-demon-hunters/`, todas miradas con Read antes de elegir.
- `herramientas/estilo.py` sobre 10 imágenes oficiales descargadas (6 trajes + 4 fondos) para los hex medidos de vestuario y paisajes.
- `ambientcg.com/api/v2` (leather, fabric, paper, metal/gold) para texturas reales/CC0 equivalentes; sin bloqueo.
- WebFetch: creativebloq.com (artbook, poco contenido extraíble), 1000logos.net (logo, sí funcionó).
- No usé `navegar.py`: ninguna web de las tocadas dio bloqueo de verificación.

### Bitácora de video

- 2026-09-25 · leídos AYUDANTE.md, EQUIPO.md, ENCARGO.md, encargos/63-…md,
  partes/datos-video.md. Sin serie hermana (`herramientas/hermanas.py`).
- 2026-09-25 (en) · Fandom `kpop-demon-hunters` API (`action=parse&prop=wikitext`):
  ficha del film (`KPop Demon Hunters (Film)`) y soundtrack (`…/Soundtrack`):
  runtime 1:39:37, dirección, fecha, sinopsis, argumento completo, localizaciones,
  tracklist estándar y deluxe. También fichas de Rumi, Mira, Zoey, Jinu (pelo,
  ojos, armas, especie).
- 2026-09-25 · `fotogramas.py` sobre 5 vídeos (bajados con yt-dlp, sin login):
  tráiler oficial (Dailymotion x9k1104, cada 8 s + 3 fotogramas sueltos),
  «How It's Done» lyric video (IA youtube-QGsevnbItdU, cada 6 s + 4 sueltos),
  «Soda Pop» lyric video (IA youtube-983bBbJx0Mk, cada 6 s + 3 sueltos), «Golden»
  lyric video (IA golden-official-lyric-video…, cada 6 s + 5 sueltos), «Takedown»
  lyric video (IA youtube-l8Dr7vzMSVE, cada 6 s). Vídeos borrados de
  `/tmp/claude-0/trabajo/…` tras sacar las hojas (quedan hojas + fotogramas
  sueltos + los `.json` de `estilo.py`).
- 2026-09-25 · `estilo.py` (Pillow k-means) sobre 12 fotogramas sueltos para
  paleta hex y tipo de sombreado (punto 4).
- 2026-09-25 (en) · búsquedas web (WebSearch, cupo usado: 6 de ~50): «"KPop
  Demon Hunters" "Golden" TikTok dance challenge viral trend»; «"Golden"
  HUNTR/X Billboard Hot 100 number one record»; «"KPop Demon Hunters" Netflix
  most watched film record weeks Billboard 200 soundtrack chart»; «Saja Boys
  singing voices Andrew Choi Danny Chung Kevin Woo real singers»; «"KPop Demon
  Hunters" trailer official Netflix release date teaser July 2025»; «"KPop
  Demon Hunters" sing-along theatrical event August 2025 box office»; «"KPop
  Demon Hunters" director Maggie Kang "breaks down" scene YouTube Vanity Fair
  Anatomy». Fuentes: Billboard, Netflix Tudum, The Hollywood Reporter, AOL,
  Wikipedia (Andrew Choi, Kevin Woo), TikTok (discover pages).
- No usé `navegar.py`: no hizo falta abrir ninguna web con bloqueo de curl para
  estos puntos (las que consulté — Fandom API, Billboard, Netflix Tudum,
  Hollywood Reporter, AOL — respondieron directo).

### Bitácora de voz

- Búsquedas web (inglés): «KPop Demon Hunters personaje favorito encuesta poll most popular
  character» → Koreaboo, CBR, BuzzFeed, foro de Fandom.
- Búsquedas web (español): «ANMTV Guerreras K-pop doblaje latino reparto voces» → confirma
  ANMTV + Infobae como segunda/tercera fuente del reparto.
- Fandom `kpop-demon-hunters.fandom.com/api.php`: wikitext completo de Rumi, Mira, Zoey,
  Jinu, Gwi-Ma, Celine, Saja Boys y Bobby (secciones Trivia, infobox, Personality).
- `herramientas/voz.py` sobre 6 muestras oficiales de audio de Doblaje Wiki (Rumi, Mira,
  Zoey, Jinu, Gwi-Ma, Celine): transcripción + tono medido.
- `yt-dlp` sobre los clips Dailymotion `x9tkmqo` (trailer latino, sin diálogo) y `x9sl3s6`
  (ya no existe, «Not found», dos intentos).
- Fotogramas reutilizados de `/tmp/claude-0/trabajo/63-las-guerreras-k-pop-kpop-demon-hunters-video/`
  (ya sacados por el investigador de vídeo con `fotogramas.py`), mirados con Read: `golden`
  fotogramas 108 y 132, `howitsdone` fotograma 66, `takedown` fotograma 66.
- Búsquedas web (WebSearch, inglés): «KPop Demon Hunters Netflix most watched film ever
  record Nielsen viewership», «KPop Demon Hunters crying scene made me cry reddit Jinu
  death», «KPop Demon Hunters fandom inside jokes memes Derpy tiger Sussie cat Gwi-Ma meme»,
  «KPop Demon Hunters fans annoyed misconception Saja Boys not villains», «KPop Demon Hunters
  fans criticized inaccurate merch fan art», «KPop Demon Hunters YouGov survey favorite
  character percent».
- Búsquedas web (español): «Guerreras K-pop fandub español latino youtube tiktok cover
  Golden», «Guerreras Kpop doblaje fandub tiktok cover español latino creador».
- Páginas leídas enteras con `curl` (tras limpiar HTML con Python): ANMTV (reparto de
  doblaje), Infobae (reparto de doblaje), Netflix Tudum «Golden Milestone», Koreaboo (crítica
  al merchandising), Wikipedia «List of accolades».
- Páginas leídas con `herramientas/navegar.py` (curl daba 403): TV Tropes `Memes/…` (sí,
  contenido completo) y `YMMV/…` (sólo encabezados, el contenido está en pestañas
  colapsadas por JavaScript que el selector no expandió — no insistí más de dos intentos),
  Collider (ranking de personajes por «likability», contenido completo), IMDb poll (pantalla
  de verificación «no soy un robot», no se pudo pasar).
- `arctic-shift.photon-reddit.com`: búsquedas por título en r/KpopDemonhunters («cry»,
  «hurts so much», «sobbing», «meme», «identify», «relate», «Derpy», «Sussie»,
  «underrated», «cursed», «brainrot»); varias devolvieron 0 resultados o error de límite de
  peticiones («Timeout. Maybe slow down a bit») — no insistí en bucle.
- Fandom Doblaje Wiki: confirmé de paso la existencia de un blog de fandub alternativo
  («FanDubbing22») con la propia API de búsqueda de Google indizada.

No queda nada obligatorio pendiente de mis puntos (7, 8, 12, 13, 20, 21, 22): lo que quedó
sin cerrar (vistas exactas de fan dubs, minuto de un clip doblado del sacrificio de Jinu,
altura de Rumi) es extra y ya está anotado en «No encontré» con las búsquedas hechas.

### Bitácora de texto

- 2026-09-25 · leídos AYUDANTE.md, EQUIPO.md, ENCARGO.md, `encargos/63-…md`, `partes/datos-texto.md` (casi vacío: la obra no es un juego de Steam), y `partes/imagen.md` + `partes/video.md` completos, ya escritos por el resto del equipo, para no repetir consultas.
- Fandom API (`kpop-demon-hunters.fandom.com/api.php`), sin bloqueo: listado completo de páginas (`allpages`), wikitext de `Korean Cultural References`, `Honmoon`, `Demon`, `Timeline`, `HUNTRIX`, `Saja Boys`, `International Idol Awards`, `Category:Logos`; imágenes descargadas con `Referer: https://www.fandom.com/` y convertidas de WebP a PNG con Pillow para poder medirlas y verlas.
- `herramientas/estilo.py` sobre 3 logos propios (`Huntrix_Logo.jpg`, `Saja_Boys_Logo.jpg`, `KPop_Demon_Hunters_Logo.png`) y sobre 1 captura del juego de Roblox, para los hex de marca/interfaz — ninguno medido antes por el resto del equipo.
- **API pública de Roblox** (sin necesidad de cuenta ni WebSearch): `apis.roblox.com/universes/v1/places/{placeId}/universe` para sacar el `universeId` del juego oficial a partir de su URL, `games.roblox.com/v2/games/{universeId}/media` para listar sus capturas aprobadas, y `thumbnails.roblox.com/v1/assets?assetIds=…` para resolver cada `imageId` a una URL de imagen descargable — así conseguí 4 capturas oficiales del juego sin depender de que la prensa las hubiera recogido.
- `fontTools` (`TTFont().getBestCmap()`) sobre 8 fuentes descargadas de verdad (no de memoria): **Hunters K-Pop** (FontSpace), **Permanent Marker**, **Anton**, **Caveat**, **Noto Sans KR**, **Montserrat**, **Arimo** y **Roboto** (las siete últimas de Fontsource/jsDelivr, recorte «latin» — el recorte «latin-ext» de Fontsource NO siempre trae las tildes españolas, hay que pedir el «latin») — las ocho con tildes, ñ/Ñ, ¿ y ¡ comprobados carácter a carácter, ninguna de memoria.
- Inglés (WebSearch, cupo compartido del contenedor entre los 4 investigadores — se agotó a mitad de esta tanda, ver nota abajo): animación/render/Imageworks, character designer/art director, logo font identification, mobile game oficial, credits font, Roblox interface, similar movies/anime influence, Roblox UI font, Netflix subtitle font, Korean title logo, Hunters K-Pop font license, fontsinuse.com, Picturemill titles — 15 búsquedas en total antes de que el cupo compartido (200 del contenedor) se agotara.
- **Aviso para el jefe**: el cupo de `WebSearch` es del contenedor entero (200 llamadas), no de 50 por investigador como dice AYUDANTE.md — se agotó por el uso combinado de los 4 investigadores en paralelo, no sólo el mío. A partir de ahí seguí sólo con `curl`/`navegar.py`/Fandom API, que no cuentan contra ese cupo.
- `navegar.py` (para sitios que bloquean `curl`): Collider (15 recomendaciones, cargó bien), CBR (cargó bien), Picturemill (cargó bien), TCRF (403, dos intentos), Screendaily (405/captcha, dos intentos), Wayback Machine (fallo de red, dos intentos).
- `curl` directo (sin bloqueo): No Film School (entrevista Adobe/Substance 3D), Creative Bloq (Unreal Engine 5), Cartoon Brew (parcial, luego completado con `navegar.py`... en realidad cargó bien con `curl`), dafont (hilo de identificación del logo), Geeks OUT (entrevista completa a Maggie Kang), Fandom API.
- No hice falta usar coreano/japonés/chino como idioma de búsqueda propio: toda la película es una producción occidental (Sony/Netflix, EE. UU.) en inglés, y las fuentes en coreano que sí importan (nombres de armas, términos de cultura) ya vienen traducidas y con su hangul original dentro de la propia wiki en inglés, citando prensa coreana (koreaherald.com, korea.net) que enlacé arriba.
