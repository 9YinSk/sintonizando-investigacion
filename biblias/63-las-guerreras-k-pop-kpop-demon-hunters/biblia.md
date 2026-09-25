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

