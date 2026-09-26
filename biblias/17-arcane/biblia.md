---
tags: [biblia, serie, laminas]
serie: "Arcane"
canal: "#proyectos y #arte"
fecha: 2026-09-24
---

# Biblia · Arcane — para #proyectos y #arte

> [!important] Cómo se hizo, y sus límites
> - La red de esta sesión estaba cerrada. Por curl y por WebFetch daban
>   error: Fandom (Arcane Wiki y **Doblaje Wiki**), la wiki de League of
>   Legends, arcane.com, leagueoflegends.com, Sketchfab, ArtStation,
>   Game UI Database, Bolavip, El Vortex, Bubbleblabber. Por eso **no se
>   pudo correr** `herramientas/investigar_serie.py`: **no hay hojas de
>   contacto** ni carpeta `hojas/`.
> - Mi fuente principal fue la búsqueda web: **50 búsquedas** en
>   español, inglés, francés, chino y coreano (lista en §21).
> - GitHub sí respondía por `git` y por `raw`. De ahí saqué lo mejor:
>   **arte oficial de Riot** (splash arts «Arcane», retratos, fondos y el
>   **mapa-plano de Piltóver**), que miré, medí y describo en §3. No lo
>   subo al repositorio: cada imagen tiene su enlace directo.
> - Arcane **no es anime**: no está en el espejo de subtítulos de
>   kitsunekko, y los sitios de subtítulos no abrían. **No hay minutos
>   de subtítulo**: doy episodio y escena, con su fuente.
> - **Cómo leo los episodios**: «1×04» es temporada 1, episodio 4.
>   Arcane tiene 2 temporadas de 9 episodios, en 3 actos cada una.
> - ✅ **confirmado**: dos fuentes. ⚠️ **dudoso**: una sola fuente, o lo
>   describo de memoria. Lo de memoria siempre va marcado.
> - **Segunda pasada (26-sep-2026), con la red abierta**: lo de arriba
>   era la primera. Ahora sí corrió `investigar_serie.py` (hay 3 hojas en
>   `hojas/`, §3.7), se miró la T1 en 1080p con `fotogramas.py` (minutos
>   reales en §2, §8, §12 y §15), se cruzó el doblaje con Doblaje Wiki y
>   otra fuente (§10) y se añadieron los puntos 18-25 (§18b). Lo que
>   cambió está en «Segunda pasada · qué cambió», antes de la bitácora.

---

## 0 · Los canales y lo que tienen que decir

Del inventario (`servidor/inventario.md`):

> **ıı・📂・proyectos** (foro, sección EL ESTUDIO) · 3 hilos · etiquetas:
> Buscando gente, En traducción, En grabación, En edición, En revisión,
> Estrenado, En pausa, Cancelado, Oficial del servidor, De la comunidad —
> _Un hilo por proyecto: equipo, avance, entregas._
> - 📌 De qué va esto · adj: proyectos.png
> - YinX (1 msj)
> - EJEMPLO · Proyecto en marcha, para ver el formato

> **ıı・🎨・arte** (foro, sección EL TALLER) · 2 hilos · etiquetas: Dibujo,
> Digital, Fanart, Miniatura, Diseno, Edit o AMV, Boceto, Proceso,
> Terminado, Acepto encargos — _Dibujo, ilustración, diseño y fanart. Un
> hilo por pieza o por serie. Etiqueta si aceptas encargos._
> - 📌 Cómo se cuelga tu trabajo aquí · adj: arte.png
> - EJEMPLO · Miniatura para un fandub — dos versiones

Función según el encargo: **#proyectos** es el foro de proyectos con
estados; **#arte** es el foro de piezas (proceso, terminado, acepto
encargos).

> [!note] Ojo con la etiqueta «Diseno»
> En el inventario está escrita **sin ñ** («Diseno»). En la lámina hay que
> escribirla igual que la etiqueta real de Discord, o pedir al dueño que
> la corrija a «Diseño» antes de rotular.

### Los textos de la lámina #proyectos (lámina 1: qué es el canal)

| Qué | Texto (sale del inventario) |
|---|---|
| Título | **Proyectos** |
| Qué es | **Un hilo por proyecto** |
| Qué va dentro | **Equipo, avance y entregas** |
| Origen | **Oficial del servidor** o **De la comunidad** |

### Los textos de la lámina #proyectos (lámina 2: los estados)

Las 8 etiquetas de estado, en el orden de un proyecto:

1. **Buscando gente**
2. **En traducción**
3. **En grabación**
4. **En edición**
5. **En revisión**
6. **Estrenado**
7. **En pausa**
8. **Cancelado**

Más las dos de origen: **Oficial del servidor** y **De la comunidad**.
Son 10 etiquetas: si no caben con el texto de la lámina 1, van en la
lámina 2 (regla 5 del dueño).

### Los textos de la lámina #arte (lámina 1: qué es el canal)

| Qué | Texto (sale del inventario) |
|---|---|
| Título | **Arte** |
| Qué es | **Dibujo, ilustración, diseño y fanart** |
| Cómo se usa | **Un hilo por pieza o por serie** |
| El aviso | **Etiqueta si aceptas encargos** |

### Los textos de la lámina #arte (lámina 2: las etiquetas)

- **Qué es**: Dibujo · Digital · Fanart · Miniatura · Diseno · Edit o AMV
- **En qué punto va**: Boceto · Proceso · Terminado
- **Y la que importa**: **Acepto encargos**

(En la lámina no se usan «·»: cada etiqueta va en su propio sitio.)

---

## 1 · Resumen para quien tenga prisa

- **Qué es**: serie de animación de **Riot Games** (el estudio de *League
  of Legends*), animada por el estudio francés **Fortiche**, en Netflix.
  Temporada 1 en noviembre de 2021; temporada 2, la última, en tres
  actos: 9, 16 y 23 de noviembre de 2024 ✅
  ([ComicBook](https://comicbook.com/anime/news/arcane-season-2-character-posters/),
  [Wikipedia S2](https://en.wikipedia.org/wiki/Arcane_League_of_Legends:_Season_2)).
- **De qué va**: dos ciudades pegadas. Arriba, **Piltóver**, rica, dorada,
  de inventores. Abajo, **Zaun** (la «ciudad subterránea»), verde, sucia,
  de mafias. Dos hermanas, **Vi** y **Powder**, quedan en lados opuestos:
  Powder se convierte en **Jinx**.
- **Por qué sirve para #proyectos**: la mitad de la serie es **un
  proyecto de dos inventores**, Jayce y Viktor, que crean la **Hextech**
  a base de planos, pruebas, fracasos y una presentación pública (el
  **Día del Progreso**, 1×04). Tiene «equipo, avance y entregas».
- **Por qué sirve para #arte**: el mundo de Arcane **está pintado a mano**
  (texturas pintadas, efectos 2D encima del 3D) y **Jinx firma con
  grafiti**. Los Firelights de Ekko pintan un **mural** a sus muertos
  (1×07). En 2×04 Zaun entero pinta en azul por Jinx.
- **El personaje**: **Jinx** es la más querida sin discusión (§9). Para
  #proyectos, **Jayce y Viktor** son los dueños del objeto.
- **El «cuadro de diálogo»**: Arcane no tiene globos. Habla con **pintura
  sobre la pared** (Jinx), **garabatos de tiza neón encima de la imagen**
  (la cabeza de Jinx), **notas a lápiz sobre planos sepia con runas**
  (Hextech) y **murales** (Firelights). Ver §7.
- **Doblaje latino**: sí existe ✅. Jinx **Karla Falcón**, Vi **Romina
  Marroquín**, Viktor **Igor Cruz**, Silco **Nicolás Frías**, Caitlyn
  **Karina Altamirano**, Ekko **José Antonio Toledano**, Jayce **Miguel de
  León**. T1: **Sysdub**, director **Eduardo Garza**. T2: **Iyuno
  México**, directora **Angie Villa**. Ver §10.
- **Hallazgo clave**: en GitHub hay un espejo de **Data Dragon** (los
  archivos oficiales del juego) con **el mapa-plano oficial de RiotX
  Arcane** (3000×2280, papel sepia con runas y notas a lápiz) y **4 fondos
  de móvil** oficiales. Es el mejor modelo para los «planos Hextech».

---

## 2 · Las escenas que sirven para estos canales

> **Segunda pasada (26-sep)**: ahora sí hay minutos. Los investigadores
> bajaron la T1 entera en 1080p de Internet Archive
> ([arcane-season-1-60fps](https://archive.org/details/arcane-season-1-60fps))
> y **miraron los fotogramas** con `fotogramas.py`. Los minutos de abajo
> son de ese archivo (el de Netflix puede variar unos segundos). La T2
> sigue sin minutos: ese archivo sólo trae la T1.

### 2.1 Para #proyectos: el proyecto Hextech, de principio a fin

| Etapa del proyecto | Escena | Estado |
|---|---|---|
| **Buscando gente** | **1×02, min 14:48**: juicio de Jayce ante el Consejo; está solo y diminuto en un círculo de luz, todos lo miran desde arriba, y lo expulsan de la Academia. En 1×03 Viktor, ayudante de Heimerdinger, va a buscarlo porque cree en su teoría | ✅ minuto visto en fotograma ([archivo 1×02, `?t=888`](https://archive.org/download/arcane-season-1-60fps/%5B60FPS%5D.Arcane.S01E02.Some.Mysteries.Are.Better.Left.Unsolved.1080p.NF.WEB-DL.DDP5.1.x265.Homelander.mp4?t=888)) + [Jayce Talis · Arcane Wiki](https://arcane.fandom.com/wiki/Jayce_Talis); que se asocian en 1×03 es ✅ ([Arcane Wiki](https://arcane.fandom.com/wiki/The_Base_Violence_Necessary_for_Change), [The Review Geek](https://www.thereviewgeek.com/arcane-s1e3review/)); la frase exacta del encuentro ⚠️ |
| **Equipo formado** | 1×03: Viktor le habla del «sueño Hextech» y Jayce le corrige: «**nuestro** sueño Hextech». **Min 17:30**: los dos en el taller, Viktor con el cuaderno en la mano, sonriendo ante el primer arco eléctrico azul | ✅ ([The Review Geek](https://www.thereviewgeek.com/arcane-s1e3review/), [LoL Wiki S1E3](https://leagueoflegends.fandom.com/wiki/Arcane_(TV_Series)/Season_1/Episode_3)); minuto ✅ visto ([archivo 1×03, `?t=1050`](https://archive.org/download/arcane-season-1-60fps/%5B60FPS%5D.Arcane.S01E03.the.Base.Violence.Necessary.for.Change.1080p.NF.WEB-DL.DDP5.1.x265.Homelander.mp4?t=1050)) |
| **En grabación** (la prueba) | 1×03: de noche, en el laboratorio de Heimerdinger, Mel les da una noche. Todo flota: funciona. Jayce: no es la era de la magia, «es la era de la **Hextech**» | ✅ el hecho (mismas fuentes). ⚠️ **minuto sin encontrar**: no está entre 0:00 y 32:00 de 1×03, ni en 1×05 ni en 1×06, mirados enteros. Falta mirar 1×03 desde el 32:00 |
| **Estrenado** | 1×04, **Día del Progreso** (200 años de Piltóver): Jayce da el discurso; sus **hexportales** ya mueven los dirigibles. **Min 23:40-26:50**: entra con foco cenital, sube al atril de latón con bocinas de gramófono (24:20), habla con el puño en el pecho (25:40) y cierra con fuegos artificiales rojos y cian (26:20) | ✅ ([The Review Geek 1×04](https://www.thereviewgeek.com/arcane-s1e4review/), [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Recap/ArcaneS1E4HappyProgressDay)); minutos ✅ vistos en fotograma |
| **En pausa** | 1×04: Heimerdinger le quita la idea de presentar la **gema estabilizada** (**min 11:14-13:14**: Jayce solo con la gema flotando entre chispas azules; entra Heimerdinger; detrás, en la mesa, los guanteletes Atlas). Esa noche Jinx roba las gemas **y deja grafiti**. Al día siguiente, Jayce propone **suspender** toda la Hextech | ✅ ([The Review Geek 1×04](https://www.thereviewgeek.com/arcane-s1e4review/), [Arcane Wiki](https://arcane.fandom.com/wiki/Happy_Progress_Day!)); minuto ✅ visto, y lo confirma [PC Gamer, recap 1×04](https://www.pcgamer.com/arcane-episode-4-recap-ghosts-of-the-past/). **Corrección**: la escena de la gema es de 1×04, no de 1×03 |
| **En revisión** | 1×04: el Consejo vota; Mel propone a Jayce como concejal | ✅ (mismas fuentes) |
| **Cancelado** | 1×06: Jayce y Viktor chocan por el **Núcleo Hex**; Jayce lo cierra. **Min 27:00**: el núcleo hex (esfera azul violeta con runas) flota al fondo del laboratorio; Jayce, de perfil y preocupado, en primer plano | ✅ el núcleo en 1×06, visto en fotograma y en la sinopsis ([When These Walls Come Tumbling Down · Arcane Wiki](https://arcane.fandom.com/wiki/When_These_Walls_Come_Tumbling_Down)); ⚠️ que Jayce lo cierre sigue de memoria |

> [!tip] La escena de 1×04 es oro para las dos láminas
> **Jinx entra en el laboratorio de Jayce y Viktor y deja su grafiti.**
> Es el único sitio donde los **planos Hextech** (#proyectos) y **la
> pintura de Jinx** (#arte) están en la misma habitación. Qué dice y
> dónde está el grafiti exactamente: ⚠️ sigue sin fotograma. En la
> segunda pasada se miró 1×04 hasta el 26:50 al detalle y el resto cada
> 45 s, y no apareció.

### 2.2 Para #arte: pintura, murales y grafiti

| Escena | Qué pasa | Estado |
|---|---|---|
| **1×07 «The Boy Savior»**: el árbol de los Firelights | Ekko enseña a Vi un **mural pintado a sus muertos**: Vander, Benzo, Claggor, Mylo, Powder, Vi. **Uno está a medio pintar** (la chica Firelight que murió en 1×04). **Min 12:18**: Ekko, serio y con los párpados caídos, junto a Vi ante el mural; hacia el 12:30 Vi lo mira llorosa | ✅ ([Screenspy](https://www.screenspy.com/arcane-season-1-episode-7/), [Arcane Wiki](https://arcane.fandom.com/wiki/The_Boy_Savior)); minuto ✅ visto ([archivo 1×07, `?t=738`](https://archive.org/download/arcane-season-1-60fps/%5B60FPS%5D.Arcane.S01E07.The.Boy.Savior.1080p.NF.WEB-DL.DDP5.1.HEVC.Homelander.mp4?t=738)) |
| **2×04 «Paint the Town Blue»**, al empezar | Suena la canción de **Ashnikko**. Montaje de los «**Jinxers**»: Zaun se tiñe el pelo de azul y se rebela. **Jinx pinta caras** «tontas» y rompe la cuarta pared; ella e **Isha** pintan sus bichos como el Correcaminos del Rift y Vilemaw | ✅ ([IMDb](https://www.imdb.com/title/tt34383695/), [LoL Wiki S2E4](https://wiki.leagueoflegends.com/en-us/Universe:Arcane_(TV_Series)/Season_2/Episode_4), [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Recap/ArcaneS2E4PaintTheTownBlue)) |
| **La cabeza de Jinx** (1×03, 1×07, 1×09…) | **Garabatos 2D dibujados encima de la imagen**, a 12 fotogramas por segundo, sobre las caras de sus muertos (ojos y orejas exagerados) | ✅ ([SyncSketch](https://blog.syncsketch.com/creator-stories/arcane-fortiche/), [Fantasy/Animation](https://www.fantasy-animation.org/current-posts/visions-of-vulnerability-the-artistic-depiction-of-psychological-decline-in-arcane)) |
| **El escondite de Jinx** | Muñecos de **Mylo y Claggor** le hacen compañía | ✅ ([AOL](https://www.aol.com/news/league-of-legends-arcane-easter-eggs-act-1-netflix-040800601.html), [WatchMojo](https://www.watchmojo.com/articles/top-10-things-you-missed-in-arcane)); los dibujos de las paredes ⚠️ |

### 2.3 Más escenas miradas de verdad (T1, con minuto)

| Episodio y minuto | Qué se ve | Sirve para | Estado |
|---|---|---|---|
| **1×03, 16:55** | Vi, con el brazo vendado, sobre el hombro de Powder; las dos miran abajo | Lámina de equipo, ternura | ✅ visto ([`?t=1015`](https://archive.org/download/arcane-season-1-60fps/%5B60FPS%5D.Arcane.S01E03.the.Base.Violence.Necessary.for.Change.1080p.NF.WEB-DL.DDP5.1.x265.Homelander.mp4?t=1015)) |
| **1×03, 19:15-19:55** | Un artefacto con núcleo azul estalla entre relámpagos y corta a un primer plano de una cara pálida con marcas oscuras bajo los ojos | Retrato de origen | ✅ visto; ⚠️ el investigador lo leyó como la explosión que marcó a Silco, pero por el orden del episodio (al 23:30 Mylo y Claggor ya han muerto) puede ser **la bomba de Powder**. Comprobar antes de usarlo |
| **1×03, 20:10-22:25** | Flashback de una banda armada en los túneles de Zaun: reuniones tensas, un cuchillo, primeros planos de ojos | Trasfondo de la violencia de Zaun | ✅ visto; ⚠️ el investigador lo leyó como «Vander joven con cresta magenta», pero la cresta magenta es el peinado de Vi: identificación dudosa |
| **1×03, 23:30-24:45** | Vi, con sangre en la mejilla, le grita a Powder «jinx» y la deja sola | La escena que crea a Jinx (§8, §18b.4) | ✅ visto ([`?t=1410`](https://archive.org/download/arcane-season-1-60fps/%5B60FPS%5D.Arcane.S01E03.the.Base.Violence.Necessary.for.Change.1080p.NF.WEB-DL.DDP5.1.x265.Homelander.mp4?t=1410)) |
| **1×03, 37:44-38:00** | Silco llega al edificio en llamas con un relámpago azul detrás; encuentra a Powder llorando y la consuela | Silco y Jinx, el origen | ✅ visto ([`?t=2264`](https://archive.org/download/arcane-season-1-60fps/%5B60FPS%5D.Arcane.S01E03.the.Base.Violence.Necessary.for.Change.1080p.NF.WEB-DL.DDP5.1.x265.Homelander.mp4?t=2264)) + [Silco · Arcane Wiki](https://arcane.fandom.com/wiki/Silco) |
| **1×05, 10:40-11:20** | Jinx activa un aparato hextech hecho con los apuntes de Jayce y Viktor; el pulso de luz azul (11:00) le recuerda la explosión y se derrumba llorando junto a la baranda | Los planos robados en manos de Jinx: une los dos canales | ✅ visto + [sinopsis · Arcane Wiki](https://arcane.fandom.com/wiki/Everybody_Wants_to_Be_My_Enemy) |
| **1×05, 18:00** | Puerta de caja fuerte con dial de símbolos rúnicos; una silueta da una patada alta a contraluz | Acción, pelea | ✅ visto; ⚠️ quién da la patada no se ve |
| **1×06, 12:25-14:25** | Marcus entra al cuarto de su hija Ren, que juega con naipes; Silco está sentado con ella, deja caer una carta y se va («los accidentes pasan») | Silco amenazando sin alzar la voz | ✅ visto + [sinopsis · Arcane Wiki](https://arcane.fandom.com/wiki/When_These_Walls_Come_Tumbling_Down) |
| **1×06, 21:50** | Una figura de pelo magenta camina de espaldas, decidida, por un pasillo oscuro con cortinas | Pose de espaldas | ✅ visto; ⚠️ probablemente Vi (no se ve la cara) |

---

## 3 · Arte oficial y referencias visuales

> [!warning] Dos estilos que NO se mezclan
> - **Estilo Arcane** (Fortiche): pintado, texturas a mano, luz de cine,
>   caras con pinceladas. Es el que va en la lámina.
> - **Estilo League of Legends** (el juego): ilustración digital brillante
>   y más «de juguete». Los fondos de RiotX de §3.2 son de este estilo:
>   sirven de pose, **no** de estilo.
> Las **splash arts de las skins «Arcane»** (§3.1) están a medio camino:
> las pinta Riot imitando la serie. Son lo más cercano con buena resolución.

### 3.1 Splash arts oficiales de las skins «Arcane» (1215×717)

Todas bajan por `raw.githubusercontent.com` del espejo de Data Dragon
[InFinity54/LoL_DDragon](https://github.com/InFinity54/LoL_DDragon)
(carpeta `img/champion/splash/`). Dirección directa, comprobada (200):
`https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/img/champion/splash/<archivo>`.
Nombres oficiales en español latino,
sacados de `latest/data/es_MX/champion/*.json` del mismo repositorio ✅.
Las describo yo, mirándolas.

| # | Archivo | Nombre oficial (LATAM) | Qué se ve | Sirve para |
|---|---|---|---|---|
| S1 | `Jinx_37.jpg` | Arcane: Jinx Enemiga | Jinx de pie en una calle de farolas, niebla oscura; trenzas largas, top negro, una mano con una bomba rosa. Muy oscura: el gris `#202026` es el 19 % | Presentar con amenaza |
| S2 | `Jinx_60.jpg` | Arcane: Jinx Quebrantada | Jinx con capucha morada, rostro pintado, con el minigun Pow-Pow. A la izquierda, **un vitral de ella misma pintado con garabatos neón**: estrella verde, corazón rosa, zigzags | **El estilo del grafiti de Jinx** (#arte) |
| S3 | `Vi_29.jpg` | Arcane: Vi Suburbana | Vi de chaqueta roja, de pie, un guantelete Hextech enorme a la altura del pecho, otro abajo. Rojos `#9C3C3C`–`#CC3C54` | Vi seria, explicando |
| S4 | `Vi_48.jpg` | Arcane: Vi Peleadora | Vi de ring, agachada tras un golpe, guantelete azul Hextech | Acción |
| S5 | `Jayce_24.jpg` | Arcane: Jayce Inventor | **Jayce en un atril de latón con bocinas de gramófono (un discurso), camisa blanca; levanta en el puño una gema Hextech azul y sonríe hablando; la otra mano, abierta. Detrás, el martillo en una vitrina y cortinas moradas**. Dorados `#B4843C`–`#E4B46C` | **Presentar** (#proyectos) |
| S6 | `Jayce_35.jpg` | Arcane: Jayce Sobreviviente | Jayce barbudo y roto, abrazado al martillo, con la mano en la cabeza, entre grietas moradas | Pensar, dudar |
| S7 | `Viktor_24.jpg` | Arcane: Viktor Redentor | Viktor de la T2, pelo blanco, túnica lila, bastón; **tiende la mano abierta** hacia el que mira. Fondo blanco perla `#E3DBDE` | Invitar, explicar |
| S8 | `Caitlyn_28.jpg` | Arcane: Caitlyn Vigilante | Caitlyn con el rifle en diagonal, en una nave verde de Zaun; **cristales rotos pintados por Jinx** (garabatos cian, estrella morada, letras rosas) y **el mono de juguete** con el ojo rojo encendido en primer plano | Caitlyn investigando |
| S9 | `Caitlyn_50.jpg` | Arcane: Caitlyn Comandante | Caitlyn de la T2: boina blanca, uniforme azul `#3C6CB4`, rifle en horizontal, soldados detrás | Mandar, ordenar |
| S10 | `Ekko_36.jpg` | Arcane: Ekko Firelight | Ekko adulto, pelo blanco, con su bate-reloj en el aire, en pleno salto | Acción |
| S11 | `Ekko_57.jpg` | Arcane: Ekko Batalla Decisiva | Ekko esquivando, con el dispositivo del tiempo azul | Acción |
| S12 | `Heimerdinger_33.jpg` | Arcane: Profesor Heimerdinger | Heimerdinger **tocando un banjo** en un sitio verde lleno de pompas, con niños mirando | Celebrar |
| S13 | `Mel_1.jpg` | Arcane: Concejal Mel | Mel arrodillada en el Consejo, con una gema en la mano; luz dorada de ventanal | Luz de Piltóver |
| S14 | `Warwick_56.jpg` | Arcane: Warwick Vander | Vander convertido en bestia, garras moradas | No para estos canales |

### 3.2 Material oficial de RiotX Arcane (2021)

Mismo repositorio, carpeta `extras/arcane/` ✅ (descargado y medido). Dirección:
`https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/arcane/<archivo>`.

| # | Archivo | Tamaño | Qué es |
|---|---|---|---|
| R1 | `riotxarcane_onlinegamemap.jpg` | **3000×2280** | **Mapa-plano de Piltóver** en papel sepia: calles en círculos, edificios dibujados a lápiz, **círculos de runas Hextech**, notas en escritura inventada, un cristal Hextech dibujado en un recuadro, un diamante-glifo con firma. **Es exactamente el estilo «plano Hextech»** |
| R2 | `wallpapers/riotxarcane_jinx.png` | 1440×2960 | Fondo de móvil: Jinx riendo, cohete rosa. Estilo LoL, no Arcane |
| R3 | `wallpapers/riotxarcane_vi.png` | 1440×2960 | Vi con guanteletes dorados. Estilo LoL |
| R4 | `wallpapers/riotxarcane_jayce.png` | 1440×2960 | Jayce con el martillo en diagonal. Estilo LoL |
| R5 | `wallpapers/riotxarcane_caitlyn.png` | 1440×2960 | Caitlyn con sombrero de copa y rifle. Estilo LoL |
| R6 | `avatars/*.jpg` | 736×736 | 11 avatares: Ambessa, Caitlyn, Ekko, Heimerdinger, Jayce, Jinx, Mel, Sevika, Vi, Viktor, Warwick |

**Medido en R1**: papel `#B39A84` (mediana), tonos del papel de
`#978370` a `#B8A18C`, tinta de lápiz `#5B4D42` (percentil 2) ✅.

### 3.3 Carteles y key visuals

| Qué | Dónde | Estado |
|---|---|---|
| **Carteles de personaje de la T2** (Vi y Jinx enfrentadas, Ekko «From Little Man to The Boy Savior», Ambessa) | [Netflix Tudum, galería](https://www.netflix.com/tudum/galleries/arcane-season-2-character-posters), [The Mary Sue](https://www.themarysue.com/netflix-drops-arcane-season-2-character-posters/), [ComicBook: Ekko](https://comicbook.com/gaming/news/arcane-season-2-netflix-ekko-poster/), [Bleeding Cool: Ambessa](https://bleedingcool.com/tv/arcane-season-2-character-key-art-poster-spotlights-ambessa-medarda/) | ✅ que existen. **Segunda pasada**: descritos. El de **Vi** lleva **una diana de grafiti pintada en la espalda** (la marca de Jinx); el de **Jinx**, apuntando. Están compuestos para leerse juntos: hermana contra hermana ✅ ([The Mary Sue](https://www.themarysue.com/netflix-drops-arcane-season-2-character-posters/) + [CGMagazine](https://www.cgmagonline.com/news/new-arcane-season-2-poster-dropped/)). La galería de Tudum sólo dio el título, sin descripción ⚠️ |
| **Cartel de Silco, T1** (`Silco_Season_1_Poster_1.jpg`, 2025×3000) | De perfil, media cara humana y media con textura de madera y metal verde (la cicatriz química). Sostiene una jeringa de **Shimmer** morada que le tiñe la mano de rosa. Detrás, en transparencia, su despacho de **The Last Drop** con una lámpara Tiffany naranja | ✅ mirado directamente ([Arcane Wiki, imagen](https://static.wikia.nocookie.net/arcane/images/5/54/Silco_Season_1_Poster_1.jpg/revision/latest?cb=20241129111151)). Pose útil: «sostener algo pequeño y peligroso mirando de lado», para quien explica un secreto |
| **Escudos de Piltóver y Zaun** (`Piltover_Crest.png` 4042×4167 y `Zaun_Crest.png` 3487×4167, PNG con **fondo transparente de verdad**) | Piltóver: un Hexgate rodeado en parte por un engranaje. Zaun: un **vial químico alado**. Los dos en el mismo oro, **`#C7A965`**, medido por píxel (el oro «de catálogo», sin luz de escena; la splash de Jayce da `#B4843C`, más oscuro por la luz) | ✅ medido ([Piltover Crest](https://static.wikia.nocookie.net/arcane/images/c/c6/Piltover_Crest.png/revision/latest?cb=20241118070136), [Zaun Crest](https://static.wikia.nocookie.net/arcane/images/b/bc/Zaun_Crest.png/revision/latest?cb=20241123234130)); los símbolos, del campo `symbol` de las fichas de [Piltover](https://arcane.fandom.com/wiki/Piltover) y Zaun |
| Cartel principal de la T2 (Jinx, Vi, Caitlyn, Ambessa) | [CGMagazine](https://www.cgmagonline.com/news/new-arcane-season-2-poster-dropped/), [Yahoo](https://www.yahoo.com/entertainment/arcane-season-2-poster-previews-192014449.html), [Game Rant: qué esconden](https://gamerant.com/arcane-season-2-posters-hints-clues/) | ✅ |
| Guía del *making of* de la T2 | [Netflix Tudum](https://www.netflix.com/tudum/features/arcane-season-two-behind-the-scenes) | ✅ |

### 3.4 El libro de arte oficial

**The Art and Making of Arcane**, de Elisabeth Vincentelli (Titan Books,
2024) ✅ ([SFFWorld](https://www.sffworld.com/2024/12/the-art-and-making-of-arcane-by-elisabeth-vincentelli/),
[Google Books](https://books.google.com/books/about/The_Art_of_Arcane.html?id=_iDT0AEACAAJ),
[GeekNative](https://www.geeknative.com/167615/titan-confirm-limited-portfolio-edition-of-the-art-of-the-arcane/)):
- Arte conceptual inédito, *storyboards*, fondos pintados y
  **desplegables de hasta 120 cm**.
- Entrevistas a más de 20 personas del equipo.
- **Trae de regalo un «plano» dentro del mundo (in-world blueprint), un
  mapa de Piltóver que se saca, una carta de Vander y un póster de Jinx.**
  El plano confirma que los planos Hextech son un objeto «real» de la
  serie. ⚠️ No vi su contenido.

### 3.5 Arte conceptual de Fortiche (ArtStation, X, Tumblr)

| Autor | Qué | Enlace | Estado |
|---|---|---|---|
| **Julien Georgel**, director de arte | Conceptos y fondos pintados (hizo Piltóver «más usada», con Art Déco) | [ArtStation](https://www.artstation.com/juliengeorgel), [80.lv](https://80.lv/articles/riot-games-on-designing-arcane-s-piltover-zaun) | ✅ |
| **Alexia Ferry** | **«Arcane – Hextech Lab»**: el laboratorio en 3D, sobre conceptos de **Arnaud-Loris Baudry** | [ArtStation](https://www.artstation.com/artwork/3qagn2) | ✅ existe; ⚠️ no lo vi |
| **Mariana Galiano** | Viktor tras la explosión (T2): la escena en que Jayce lo encuentra | [X de Fortiche](https://x.com/ForticheProd/status/1868702708904910894?lang=en), [Tumblr art-of-arcane](https://www.tumblr.com/art-of-arcane/770045202608111616/mariana-galiano) | ✅ |
| Varios | **«ARCANE S2: JINX»**, diseño final de Jinx | [ArtStation](https://www.artstation.com/artwork/lG4RrJ) | ⚠️ autor sin comprobar |
| Blog **art-of-arcane** (Tumblr) | Recopila arte conceptual con su autor | [Tumblr](https://www.tumblr.com/art-of-arcane/770045202608111616/mariana-galiano) | ✅ |
| Conceptos de Viktor y Jayce T2 | Recopilación | [Tumblr aurelion-solar](https://aurelion-solar.tumblr.com/post/772964799003885568/viktor-jayce-arcane-season-2-concept-art) | ⚠️ |

### 3.6 Cómo está hecho (para imitarlo, no para copiarlo)

- **«Cada fotograma tiene que parecer un cuadro»**; «el 3D es sólo una
  herramienta» (Pascal Charrue, codirector) ✅
  ([AWN](https://www.awn.com/animationworld/unveiling-arcane-conversation-pascal-charrue-and-alexis-wanneroy),
  [Cineuropa](https://cineuropa.org/en/newsdetail/424453/)).
- **Texturas pintadas a mano** sobre modelos 3D ✅
  ([80.lv: texturas](https://80.lv/articles/a-closer-look-at-texturing-in-arcane),
  [8forty](https://8forty.ca/2022/01/19/arcane-3d-animation-with-hand-drawn-backgrounds/)).
- **Humo, explosiones y los garabatos de Jinx son 2D**, dibujados encima
  del 3D ya animado, **a 12 fotogramas por segundo** (lo demás va a 24).
  Por eso chisporrotean ✅ ([SyncSketch, Alexis Wanneroy](https://blog.syncsketch.com/creator-stories/arcane-fortiche/),
  [RedShark](https://www.redsharknews.com/why-netflixs-arcane-looks-so-good-how-fortiche-ramped-up-the-animation-pipeline)).
- Sobre los garabatos, el equipo: «es como si Jinx montara la película de
  su vida con rabia, **rayando directamente sobre la película**» ⚠️ (cita
  recogida por el buscador, sin la fuente original a la vista).
- **Cada magia tiene su color**: runas, Hextech, quimtech y Shimmer tienen
  paletas distintas ✅ ([Netflix Tudum](https://www.netflix.com/tudum/features/arcane-season-two-behind-the-scenes)).
- **Más, con la técnica paso a paso para Photoshop y Blender**: §18b.1.

### 3.7 Las hojas de contacto (segunda pasada)

`investigar_serie.py --serie "Arcane" --wiki arcane --paginas "Jinx" "Vi"
"Jayce Talis" "Viktor" "Caitlyn Kiramman" "Ekko" "Silco"` corrió esta vez:
**268 imágenes grandes** de la wiki en 6 hojas. El investigador de imagen
las miró las 6. Quedan 3 en `hojas/` (JPEG, menos de 3 MB):

| Hoja | Números que sirven | Para qué |
|---|---|---|
| `hojas/arte_modelos_01.jpg` (nº 49-96) | **70** Jayce, boceto de color con la paleta al lado · **75** el Heraldo, escultura gris en *turnaround* · **77-79** el pelo de Caitlyn en 5 ángulos · **86** *turnaround* con 5 poses de baile y el rótulo «ARCANE» · **93** bustos del personal del Consejo | Hojas de modelo reales del estudio: proporciones para Blender (punto 1) |
| `hojas/colaboraciones_figuras_01.jpg` (nº 145-192) | **150** portada del cómic promocional de Jayce · **157-159** tres vistas de concepto del Heraldo · **163** render T2 de Jayce · **182** Nendoroid Jinx · **183** sudadera con la cita de Viktor · **186** Youtooz Vi y Jinx · **187** sudadera «Jayvik» · **188-189** figuras de Jinx | Figuras oficiales y colaboraciones (§18b.6) |
| `hojas/colaboraciones_merch_01.jpg` (nº 241-268) | **245** mochila tokidoki × Arcane · **252** Funko Viktor · **260-261** *turnaround* oficial de Ekko, de frente y de perfil · **262** Funko Jinx · **263** Youtooz Jinx suelta | Merch y el modelo de Ekko |

Las otras 3 hojas (`hoja_01`, `hoja_03`, `hoja_05`) son sobre todo
fotogramas y las splash de §3.1, que ya tienen enlace directo. Se
regeneran con el mismo comando. Los originales de cada número están en
`referencias.json` (fuente «Fandom arcane»).

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D para la mesa o la pared (Sketchfab y Poly Haven)

> Los modelos de Sketchfab son **fan art de algo que es de Riot**. La
> licencia CC BY cubre el trabajo del modelador, no la marca. Para una
> lámina sin fines comerciales vale, **con crédito**. **Segunda pasada**:
> las licencias ya no son del buscador, están **comprobadas una a una por
> la API de Sketchfab** y la de Poly Haven.

| Objeto | Modelo | Autor | Licencia | Enlace |
|---|---|---|---|---|
| Guantelete Hextech (los «Atlas» de 1×04) | Orivers - Hextech Gauntlet - Arcane | Frayseur | **CC BY** ✅ (API) | [Sketchfab](https://sketchfab.com/3d-models/orivers-hextech-gauntlet-arcane-71ff4266065e475d817ca882922137f0) |
| Martillo de Jayce | Orivers - Hextech hammer - Arcane | Frayseur | **CC BY** ✅ (API) | [Sketchfab](https://sketchfab.com/3d-models/orivers-hextech-hammer-arcane-f04d59aed16347a6b7b074a0b044ea7a) |
| Martillo de Jayce | Arcane Jayce Hammer | KarmaDiya | **CC BY** ✅ (API) | [Sketchfab](https://sketchfab.com/3d-models/arcane-jayce-hammer-98746826bfdd47bbbf517b8fd6ccf60c) |
| Martillo de Jayce | Jayce Hammer | GageCriscione | descarga libre ⚠️ (no se volvió a comprobar) | [Sketchfab](https://sketchfab.com/3d-models/jayce-hammer-143c80c529424bfc8a00c75c2f0412fa) |
| Granada «mascafuegos» de Jinx | Game Ready - Arcane - Jinx's Grenade | **AllanJayBranscombe** (así, es el usuario) | **CC BY** ✅ (API) | [Sketchfab](https://sketchfab.com/3d-models/arcane-jinxs-grenade-82b0959b18524af2a6311586183bd8f7) |
| Granada de Jinx (otra) | Jin'x Grenade GAME READY | pipaboba530 | **CC BY** ✅ (API) | [Sketchfab](https://sketchfab.com/3d-models/none-3db9ceaa9516460f9e53d59c7ced90f2) |
| Guantelete de Vi | Arcane Vi Gauntlet Fanart | potias | **CC BY-NC-ND** ✅ (API): sólo mirar, no modificar | [Sketchfab](https://sketchfab.com/3d-models/arcane-vi-gauntlet-fanart-7dc0ebd2584741f3a2eabc1929bdca8d) |
| Guantelete de Vi | Vi Arcane Gauntlet | karmadiya | **CC BY** ✅ (API) | [Sketchfab](https://sketchfab.com/3d-models/none-16863169437d4050b307b9be759fe08a) |
| Guantelete de Vi (del juego) | Vi Gauntlet - League of Legends | Gustavo_Ribeiro | **CC BY** ✅ (API) | [Sketchfab](https://sketchfab.com/3d-models/none-46092034259442ec91346f202fb2393e) |
| Vi en chibi (proporciones) | Chibi Vi – Arcane 3D Print Ready | sergei_8888 | **CC BY** ✅ (API) | [Sketchfab](https://sketchfab.com/3d-models/none-936a0976aab94e9ca9a7148aa1f11cf5) |
| Colección con cajas de cristales Hextech | «arcane» | shipyarn | varias ⚠️ | [Sketchfab](https://sketchfab.com/shipyarn/collections/arcane-3c0d007fa9364aa0a52dbd4778f3b300) |
| Todo lo etiquetado «hextech» | — | — | varias | [Sketchfab](https://sketchfab.com/tags/hextech) |
| **Botes de espray** (con gotas y etiquetas) | Spray Paint Bottles | **James Ray Cock** (Poly Haven) | **CC0** ✅ (API) | [Poly Haven](https://polyhaven.com/a/spray_paint_bottles) |
| **Ladrillo pintado y desconchado** (azul) | Painted Brick | **Amal Kumar** (Poly Haven) | **CC0** ✅ (API) | [Poly Haven](https://polyhaven.com/a/painted_brick) |

Personajes en 3D (sólo para **mirar poses**, nunca pegar):
[Arcane - Jinx, Craft Tama](https://sketchfab.com/3d-models/arcane-jinx-b74f25a5ee6e43efbe9766b9fbebc705) ·
[Jinx – Arcane Fan Art, Stan](https://sketchfab.com/3d-models/jinx-arcane-fan-art-4451649bf5c04fe6a5bbc3617af1678a) ·
[Jinx (Fortnite), TheBuffalo](https://sketchfab.com/3d-models/jinx-arcane-fortnite-52d63cbc920d46c090b803f8448c054e).

### 4.2 Fan art 2D del grafiti de Jinx (mirar, nunca pegar)

| Qué | Autor | Enlace |
|---|---|---|
| Jinx Arcane Neon Graffiti | meynirr | [DeviantArt](https://www.deviantart.com/meynirr/art/Jinx-Arcane-Neon-Graffiti-Digital-Art-1076440241) |
| Arcane Jinx Graffiti Neon Street Art | Yazooor | [DeviantArt](https://www.deviantart.com/yazooor/art/Arcane-Jinx-Graffiti-Neon-Street-Art-1320844834) |
| Graffiti artwork Jinx | Mani Ranganaath | [ArtStation Prints](https://www.artstation.com/prints/art_print/ADXWO/graffiti-artwork-jinx-from-arcane-league-of-legends) |
| Jinx, Powder (time-lapse 4K) | ⚠️ sin ver | [ArtStation](https://www.artstation.com/artwork/WmKByQ) |
| Symbol of Zaun (Jinx) | chebreadd | [DeviantArt](https://www.deviantart.com/chebreadd/art/Symbol-of-Zaun-Arcane-s-Jinx-1141480688) |
| Tutorial del grafiti de «Paint the Town Blue» | joaotiagovarao | [TikTok](https://www.tiktok.com/@joaotiagovarao/video/7451046601671331077) |

### 4.3 Murales de verdad, en nuestras ciudades

- **Riot pintó murales de Arcane en 2021 en Ciudad de México, Bogotá,
  Lima, Santiago y Buenos Aires**, con cinco artistas urbanos. Se conocen
  **Alucina** (Bogotá) y **Montserrat Ventura** (México) ✅
  ([LoL LATAM: Murales Arcane](https://www.leagueoflegends.com/es-mx/news/community/murales-arcane/),
  [La República, Perú](https://larepublica.pe/tendencias/2021/11/15/facebook-viral-impresionantes-murales-inspirados-en-la-serie-arcane-se-ven-alrededor-de-latinoamerica)).
  Los de Lima, Santiago y Buenos Aires: autor ⚠️.
- Otro mural de encargo: [STROY Studio](https://stroystudio.com/en/project/arcane-league-of-legends) ✅ existe; dónde está ⚠️.
- **Para el servidor esto importa**: es gente de Perú, México, Colombia…
  pintando Arcane en sus paredes. Es la mejor excusa para #arte.

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios

| Sitio | Cómo es | Luz | Estado |
|---|---|---|---|
| **Piltóver** | «Ciudad del progreso». **Art Déco** con toques *steampunk*: dorados, brillo de metal, simetría = orden y obsesión por el progreso. Julien Georgel la hizo «más usada», con historia | Cálida, dorada, de día o de atardecer | ✅ ([80.lv](https://80.lv/articles/riot-games-on-designing-arcane-s-piltover-zaun), [Game Game Over](https://gamegameover.com/exploring-the-world-of-arcane-visual-and-scenic-analysis/)) |
| **Laboratorio de Jayce** | Barandillas de latón, cristaleras, bancos de trabajo, el martillo | Dorada con sombras moradas (splash `Jayce_24`) | ✅ la splash; ⚠️ el plano completo |
| **Sala del Consejo** | Semicírculo de asientos, ventanal enorme | Contraluz dorado de ventana (splash `Mel_1`) | ✅ la splash |
| **Zaun** | **Art Nouveau**: líneas curvas, formas orgánicas; tuberías, máquinas, **grafiti**, carteles | Verde químico, neblina, farolas | ✅ ([Fizzy Mag](https://fizzymag.com/articles/how-art-nouveau-and-art-deco-styles-shaped-the-costumes-in-arcane), [Meanvexa](https://meanvexa.com/arcane-symbols/)) |
| **El árbol de los Firelights** | Un asentamiento escondido alrededor de un **árbol enorme** (algo rarísimo en Zaun), con el **mural** de los muertos | ⚠️ luz verde-azulada de memoria | ✅ el sitio ([Screenspy](https://www.screenspy.com/arcane-season-1-episode-7/)) |
| **El escondite de Jinx** | Oscuro, lleno de chatarra y de sus inventos; muñecos de Mylo y Claggor | Penumbra con puntos de neón ⚠️ | ✅ los muñecos |
| **The Last Drop** | El bar de Vander, luego de Silco | ⚠️ | ⚠️ de memoria |

**Paletas oficiales de las dos ciudades**: la cuenta oficial publicó
«The colors of Piltover vs Zaun» ✅
([X @arcaneshow](https://x.com/arcaneshow/status/1585300226247647232),
[Pinterest con la misma imagen](https://in.pinterest.com/pin/413627547048197210/)).
No pude abrir la imagen ⚠️: los hex de abajo son míos.

La paleta **cambia con la emoción**: fría en la tensión, cálida en el
cariño ⚠️ (una fuente: [Game Game Over](https://gamegameover.com/exploring-the-world-of-arcane-visual-and-scenic-analysis/)).

### 5.2 Paleta (medida por mí en las imágenes oficiales de §3)

Muestreo de JPG, margen ±10 por canal.

| Color | Hex | Dónde lo medí | Para qué |
|---|---|---|---|
| Papel de plano Hextech | `#B39A84` (de `#978370` a `#B8A18C`) | R1, mapa de RiotX | Fondo de los planos |
| Lápiz del plano | `#5B4D42` | R1 | Líneas y notas |
| Oro de Piltóver | `#B4843C` · `#E4B46C` · `#FCE484` (brillo) | `Jayce_24` | Latón, marcos, títulos |
| Azul Hextech | `#3C6CB4` · `#549CCC` | `Caitlyn_50`, `Vi_29` | Gemas, runas encendidas |
| Cian de Jinx | `#249CCC` · `#6CCCFC` | `Jinx_60` | Pelo, espray azul |
| **Rosa neón de Jinx** | `#FC6CFC` · `#FC54FC` | `Jinx_60` | Grafiti, nubes tatuadas |
| Verde de Zaun (niebla) | `#344F45` · `#98B9A2` | `Caitlyn_28` | Ambiente de Zaun |
| Verde químico | `#3CB46C` | `Ekko_36` | Quimtech, Firelights ⚠️ |
| Rojo de Vi | `#9C3C3C` · `#CC3C54` | `Vi_29` | Chaqueta de Vi |
| Lila de Viktor (T2) | `#CC84FC` · `#E484FC` | `Viktor_24` | Viktor final ⚠️ |
| Negro de Zaun | `#202026` · `#141416` | `Jinx_37`, `Vi_48` | Sombras (nunca `#000`) |
| **Oro de los escudos** (sin luz de escena) | `#C7A965` | `Piltover_Crest.png` y `Zaun_Crest.png` (§3.3) | Sello grabado, emblema ✅ |

### 5.2b La luz de verdad, medida en fotogramas (segunda pasada)

Color **medio** de fotogramas propios del episodio (Pillow,
`ImageStat.mean`), no un píxel suelto. Da el tono ambiente real, que es
más sucio y más oscuro que el de las splash arts.

| Escena | Color medio | Qué dice | Estado |
|---|---|---|---|
| Discurso del Día del Progreso, **1×04 24:30** | `#6B5B67` | Luz de escenario, magenta apagado: **no es oro puro** | ✅ medido |
| La gema en la mano de Jayce, **1×04 12:12** | `#D7F0F8` | El foco Hextech es **casi blanco**; el azul `#3C6CB4` es el halo ya atenuado | ✅ medido |
| Calle de Zaun, **1×04 6:45** | `#58615E` | La niebla verde de Zaun es **más gris** que en la splash | ✅ medido |
| Explosión y cara pálida, **1×03 19:55** | `#19314D` | Azul eléctrico: luz fría dentro de Zaun | ✅ medido |
| Jinx ante su aparato, **1×05 11:00** | `#213369` | Azul violeta: el color del trauma de Jinx | ✅ medido |
| Caja fuerte de los túneles, **1×05 18:00** | `#9C6751` | Cobre cálido de antorcha: el único acento cálido de Zaun | ✅ medido |
| Pasillo con cortinas, **1×06 21:50** | `#191117` | Casi negro con tinte granate: Zaun también es oscuridad | ✅ medido |
| Núcleo hex en el laboratorio, **1×06 27:00** | `#1D2632` | Azul pizarra: el núcleo brilla pero no quema el plano, al revés que la gema | ✅ medido |

**Para la lámina**: la mesa de Hextech va con la luz de 1×04 12:12 (centro
casi blanco, el resto en sombra). La pared de Jinx, con el verde sucio
`#58615E`, no con un verde saturado. Fuente de los fotogramas: T1 en 1080p
de [Internet Archive](https://archive.org/details/arcane-season-1-60fps).

### 5.3 Texturas reales equivalentes

Licencias comprobadas por la API de Poly Haven y la de
[ambientCG](https://ambientcg.com/) (segunda pasada).

| Para | Textura | Licencia |
|---|---|---|
| Pared de Zaun | [Painted Brick](https://polyhaven.com/a/painted_brick), Poly Haven (Amal Kumar): ladrillo con pintura azul desconchada | CC0 ✅ |
| Botes de espray en el suelo | [Spray Paint Bottles](https://polyhaven.com/a/spray_paint_bottles), Poly Haven (James Ray Cock) | CC0 ✅ |
| Papel de los planos | [Paper006](https://ambientcg.com/a/Paper006), ambientCG: papel beige-marrón con normal y rugosidad; su color base se acerca al `#B39A84` de R1 | CC0 ✅ |
| Tuberías y máquinas de Zaun | [Metal063](https://ambientcg.com/a/Metal063) (metal oscuro envejecido) | CC0 ✅ |
| Óxido de Zaun | [Metal041B](https://ambientcg.com/a/Metal041B) · pasarela [MetalWalkway014](https://ambientcg.com/a/MetalWalkway014) | CC0 ✅ |
| Suelo o mesa del laboratorio | [DiamondPlate009](https://ambientcg.com/a/DiamondPlate009), chapa estriada | CC0 ✅ |
| Latón de Piltóver | [Metal049A](https://ambientcg.com/a/Metal049A): metal plateado limpio. ambientCG no tiene latón: teñirlo hacia `#C7A965` | CC0 ✅; que sirva de latón ⚠️ |
| Guantes de Jayce, chaqueta de Caitlyn T1 | [Leather037](https://ambientcg.com/a/Leather037), cuero marrón | CC0 ✅ |
| Chaleco a cuadros de Piltóver | [Fabric060](https://ambientcg.com/a/Fabric060) · [Fabric054](https://ambientcg.com/a/Fabric054) | CC0 ✅ |

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

| Dónde | Qué es | Estado |
|---|---|---|
| **Logo «ARCANE»** | Rotulado **hecho a mano, a medida**: no existe como fuente | ✅ ([Made Good Designs](https://madegooddesigns.com/arcane-font/), [Font In Logo](https://www.fontinlogo.com/famous-fonts/arcane-font)) |
| Imitación de fans del logo | **Arcane Nine**, de Chequered Ink | ✅ **«100% Free»** en [dafont](https://www.dafont.com/arcane-nine.font); el `.otf` real, comprobado con fontTools, trae **á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü Ü** (segunda pasada) |
| Imitación de fans de los rótulos de la serie | **Piltover x Zaun Regular**, de arcanafoundry | ✅ existe, pero **es de pago** (la ficha manda a Shoptly): **no usar como letra libre** ([DeviantArt](https://www.deviantart.com/arcanafoundry/art/Piltover-x-Zaun-Regular-Arcane-font-1129768780)) |
| Letras de *League of Legends* (el juego) | **Beaufort for LoL** (títulos; variante de la Beaufort de Nick Shinn, adaptada por Monotype) y **Spiegel Sans** (texto; de Lucas de Groot). De pago y exclusivas de Riot | ✅ ([Fonts In Use](https://fontsinuse.com/uses/26935/league-of-legends-game-and-website)) |
| Cartelas de episodio y créditos | Serif refinada o display elegante, **rotulada a medida**, sin nombre publicado | ⚠️ una fuente ([Made Good Designs](https://madegooddesigns.com/arcane-font/)). Se descartó un «Sharp Sans ExtraBold» que sólo salía en un resumen automático del buscador, no en la página |
| Subtítulos de Netflix | Letra de la plataforma (Netflix Sans), no de Arcane | ⚠️ visto en créditos; no comprobado con fontTools |
| Runas Hextech | Glifos inventados, sin fuente oficial ni de fans (ver el mapa R1) | ✅ se ven en R1; buscada en inglés y coreano, **no hay fuente** ⚠️ |

### 6.2 Letras libres comprobadas por mí

Bajadas de [google/fonts](https://github.com/google/fonts) y comprobadas
con fontTools: todas traen **á é í ó ú ñ Ñ ¿ ¡ ü** ✅.

| Para qué | Letra | Licencia | Nota |
|---|---|---|---|
| **Grafiti de Jinx** (etiquetas, títulos) | **Sedgwick Ave Display** | OFL | Letra de *handstyle* de grafiti. La mejor para Jinx |
| Grafiti de Jinx (texto corrido) | **Permanent Marker** | Apache | Rotulador grueso, se lee bien a tamaño pequeño |
| Grafiti con goteo | Rubik Wet Paint | OFL | Sólo una palabra: satura |
| Espray a manchas | Rubik Spray Paint | OFL | Sólo títulos |
| Garabato nervioso | Rock Salt | Apache | Para la «voz» de la cabeza de Jinx |
| **Notas a lápiz en los planos** | **Architects Daughter** | OFL | Letra de arquitecto: justo la de un plano |
| Notas rápidas de Viktor | Caveat | OFL | Más apretada, inclinada |
| Firma o anotación elegante de Jayce | Homemade Apple | Apache | Cursiva; sólo firmas |
| Garabato diminuto en márgenes | Reenie Beanie | OFL | Para «ruido» de fondo |
| **Títulos de Piltóver** (placas, carteles) | **Cinzel** / Cinzel Decorative | OFL | Romana, solemne; la que más recuerda al logo |
| Rótulos Art Déco | Marcellus · Federo | OFL | Federo es muy Art Déco |
| Documentos del Consejo | IM Fell English | OFL | Imprenta antigua |
| Expediente de Caitlyn | Special Elite | Apache | Máquina de escribir |
| ⚠️ Evitar | Limelight | OFL | Su **¿** se parece a **¡** en mi prueba |
| ⚠️ Evitar | Poiret One | OFL | El **¿** queda descolgado |
| **Interfaz de juego** (sustituto de Spiegel) | **Barlow** | OFL | Sans humanista; tildes, ñ, ¿ y ¡ comprobados con fontTools (segunda pasada) ✅ |
| Cartelas de acto, créditos largos | **Cardo** | OFL | Serif de libro antiguo; tildes comprobadas ✅ |
| Subtítulo elegante | **Almendra Display** | OFL | Display fino con floritas; tildes comprobadas ✅ |
| Texto corrido, créditos | **EB Garamond** | OFL | Serif clásica; tildes comprobadas ✅ |
| Logo imitado (sólo el título) | **Arcane Nine** | «100% Free» (dafont) | Tildes, ñ, ¿ y ¡ comprobados ✅; es imitación de fans |

**Una letra por uso** (lo que pide el encargo): logo o título **Arcane
Nine** o Cinzel · «globo» normal (la frase de un personaje) **Permanent
Marker** si la dice Jinx, **Architects Daughter** si va en un plano ·
grito **Sedgwick Ave Display** · pensamiento **Rock Salt** · onomatopeya
**Rubik Wet Paint** · cartel del mundo **Cinzel** (Piltóver) o **Sedgwick
Ave Display** (Zaun) · interfaz de juego **Cinzel** (títulos, como
Beaufort) y **Barlow** (texto, como Spiegel) · subtítulos o créditos
**Cardo** o **EB Garamond**. Cinzel como sustituto libre de Beaufort lo
recomienda también [DesignYourWay](https://www.designyourway.net/blog/league-of-legends-font/) ✅.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que la serie pone en pantalla

Arcane **no tiene globos**. Es una serie: la gente habla y ya. Pero el
texto **sí aparece sobre objetos del mundo**:

| Soporte | Dónde se ve | Estado |
|---|---|---|
| **El espray de Jinx como firma** | 1×04: su pintura «está por todas partes» en el robo del muelle y en el ataque del Día del Progreso. **Caitlyn la usa como prueba** | ✅ ([PC Gamer 1×04](https://www.pcgamer.com/arcane-episode-4-recap-ghosts-of-the-past/), [Arcane Wiki](https://arcane.fandom.com/wiki/Happy_Progress_Day!)) |
| **Garabatos sobre la imagen** (la mente de Jinx) | Tiza neón que chisporrotea a 12 fps encima de la escena | ✅ ([SyncSketch](https://blog.syncsketch.com/creator-stories/arcane-fortiche/), [Fantasy/Animation](https://www.fantasy-animation.org/current-posts/visions-of-vulnerability-the-artistic-depiction-of-psychological-decline-in-arcane)) |
| **Garabatos de Jinx en el mundo** | Estrellas rosas y rayas neón en primer plano de `Caitlyn_28`; estrella verde, corazón rosa y zigzags sobre el vitral de `Jinx_60` | ✅ visto por mí en las splash |
| **Planos Hextech** | Papel sepia, lápiz, **círculos de runas**, escritura inventada (R1). El libro de arte trae «un plano del mundo» | ✅ |
| **Mural de los Firelights** | 1×07, retratos pintados de los muertos, uno a medio pintar | ✅ |
| **Pintura azul de los Jinxers** | 2×04: pelo azul, caras pintadas en las paredes | ✅ |
| **Cartelas de acto** | Cada temporada va en 3 actos; la cartela es texto sobrio en mayúsculas sobre el arte | ✅ que existen; la letra ⚠️ (§6.1) |
| **Interfaz Hextech** (el núcleo hex, el laboratorio) | Proyecciones azules de líneas finas y texto pequeño tipo HUD; **1×06 27:00** el núcleo flota al fondo del laboratorio ([archivo 1×06](https://archive.org/details/arcane-season-1-60fps)) | ✅ el núcleo visto; el hex del HUD sin medir ⚠️ |
| **Créditos finales** | **1×03 42:40-44:00** y **1×06 40:10-41:40**: rótulo de Riot Games y Fortiche, reparto en letra limpia | ✅ vistos en fotograma |

### 7.2 Cómo habla cada uno

| Quién | Cómo habla | Ejemplo con fuente |
|---|---|---|
| **Jinx** | Cantarina, burlona, cambia de golpe a rabia o a miedo. Alarga palabras | En 2XKO, a Ekko: «That's because everyone else you know is **BOOORIIING!**» (traducción mía: «¡Porque todos los demás que conoces son **ABUUURRIIIDOS**!») ⚠️ ([YouTube, interacciones de 2XKO](https://www.youtube.com/watch?v=vhN1FXwwoEY), [2XKO Wiki](https://wiki.play2xko.com/en-us/Jinx/Audio)); en latino, a Vi en 1×09: «**Mira, traje a tu novia**» ⚠️ (sólo Doblaje Wiki, vía buscador) |
| **Vi** | Seca, sarcástica, de calle. Llama a Caitlyn «cupcake» | En latino: «**Bombón**» en la T1 y «**Pastelito**» en la T2; en 1×08 «It's been real, cupcake» → «**Fue un placer, cariño**» ✅ (Doblaje Wiki, vía buscador y vía la guía de cuadros, `biblias/_ya_hechas/`, §22) |
| **Jayce** | De discurso, idealista, entusiasta | 1×03: no es la era de la magia, «**es la era de la Hextech**» ✅ ([The Review Geek](https://www.thereviewgeek.com/arcane-s1e3review/)) |
| **Viktor** | Tranquilo, preciso, práctico; acento de Europa del Este en inglés | 1×03: le habla a Jayce del «sueño Hextech»; Jayce le corrige: «**nuestro** sueño» ✅ |
| **Silco** | Suave, lento, amenazante; cada palabra pesa | 1×09, a Jinx, herido: «I never would have given you to them» y sus últimas palabras, «**You're perfect**». La primera la cita el buscador; la segunda es de memoria ⚠️. **Cómo lo dice el doblaje latino: no lo encontré** ( [Looper](https://www.looper.com/761753/the-most-heartbreaking-jinx-moment-from-arcane/), [Game Rant](https://gamerant.com/arcane-silco-perfect-villain/)) |
| **Ekko** | Líder joven, decidido, con humor | En latino, 2×07: «**A veces, para dar un paso hacia adelante, hay que dejar algo atrás**» ⚠️ (una fuente: la guía, que cita Doblaje Wiki) |

### 7.3 Cómo se traduce a una lámina fija

1. **Jinx habla en pintura**: su frase va **pintada con espray** sobre la
   pared o sobre el objeto, en rosa `#FC6CFC` y cian `#6CCCFC`, con
   Sedgwick Ave Display o Permanent Marker. Alrededor, sus garabatos:
   estrellas, corazones, flechas, una carita.
2. **Jayce y Viktor hablan en el plano**: la frase va **escrita a lápiz**
   (`#5B4D42`) en el margen del plano sepia, con Architects Daughter, y
   una flecha que señala la pieza. El nombre, **en una plaquita de
   latón** atornillada o en un sello.
3. **Ekko habla en el mural**: la frase pintada a brocha en la pared de
   los Firelights, junto a un retrato.
4. **Caitlyn habla en el expediente**: ficha a máquina (Special Elite)
   con una chincheta y un hilo rojo.
5. **El pensamiento** no es una nube: son **los garabatos de tiza neón
   encima de la imagen**, como en la cabeza de Jinx.

### 7.4 En los videojuegos de la franquicia

Ver §13. Segunda pasada:
- **Legends of Runeterra: Path of Champions** cuenta la historia de Jinx y
  Vi con «**cómics animados con voces**» ✅
  ([Destructoid](https://www.destructoid.com/legends-of-runeterra-path-of-champions-single-player-story-jinx-vi-jayce/)).
  La caja de texto en sí **sigue sin captura**: su tráiler está en YouTube,
  que pidió sesión, y no está en Dailymotion ni en Internet Archive ⚠️.
- **2XKO** (lucha, con Jinx, Vi, Ekko y Caitlyn): su wiki transcribe las
  frases por momento (selección, intro, burlas, combate, *supers*,
  *outro*), sin captura del subtítulo ⚠️
  ([2XKO Wiki: Jinx/Audio](https://wiki.play2xko.com/en-us/Jinx/Audio)).
- Los **cómics de Runeterra** de Riot sí usan **globo clásico de contorno
  negro**, pero no hay uno centrado en los personajes de Arcane ⚠️
  ([LoL Wiki: Universe:Arcane](https://wiki.leagueoflegends.com/en-us/Universe:Arcane)).

### 7.5 Qué NO hacer con el texto

- Un **globo blanco redondo**. En Arcane nadie habla en globo.
- Un **bocadillo limpio para Jinx**: lo suyo es pintura sobre pared.
- Grafiti **de colores alegres de arcoíris**: Jinx es rosa y cian sobre
  **negro sucio**, nunca sobre blanco.
- Los **planos en azul de «blueprint» moderno** (fondo azul, líneas
  blancas). Los de Arcane son **sepia con lápiz** (R1).
- **Letra de cómic americano** (Bangers, Comic Neue). Arcane no es cómic.

---

## 8 · Los personajes

> Lo de carácter sale de las fuentes que enlazo. Lo que va **«de
> memoria»** es de haber visto la serie: **compruébalo en el episodio**
> antes de dibujar. Los **títulos oficiales en español latino** salen de
> los archivos del juego (`es_MX`, Data Dragon) ✅.
> Retratos oficiales de todos, estilo Arcane, 736×736: `extras/arcane/avatars/` (R6).

### Jinx (Powder) — «la Bala Perdida» · la más querida

- **Quién es**: la hermana pequeña de Vi. De niña (Powder) quiere ayudar
  y sus inventos fallan. En 1×03 una bomba suya mata a Mylo y Claggor;
  Vi le grita que es **«una jinx»** (gafe) y se separan. **Silco la
  adopta** y la cría como su hija ✅ trama
  ([Wikipedia: Jinx](https://en.wikipedia.org/wiki/Jinx_(League_of_Legends)),
  [Looper](https://www.looper.com/761753/the-most-heartbreaking-jinx-moment-from-arcane/));
  la frase exacta de Vi ⚠️ de memoria.
- **Qué le importa**: que Vi no la abandone otra vez; que Silco la
  quiera como es. **Miedo**: ser la que lo rompe todo.
- **Su cabeza**: oye y ve a sus muertos. En pantalla son **garabatos 2D
  sobre la imagen**, con ojos y orejas exagerados ✅
  ([Fantasy/Animation](https://www.fantasy-animation.org/current-posts/visions-of-vulnerability-the-artistic-depiction-of-psychological-decline-in-arcane)).
- **En la T2** se vuelve **símbolo de Zaun**: los «Jinxers» se tiñen de
  azul ✅ ([TV Tropes 2×04](https://tvtropes.org/pmwiki/pmwiki.php/Recap/ArcaneS2E4PaintTheTownBlue)).
  Cuida a **Isha**, una niña que no habla, y pinta con ella ✅ (mismas fuentes).
- **Cómo se expresa** ⚠️ de memoria: voz cantarina, se ríe con una
  carcajada aguda que se corta en seco; ladea la cabeza; se agacha en
  cuclillas sobre sitios altos; juega con las trenzas; habla sola.
  Explica las cosas como un juego («¿quieres ver algo genial?»).
- **Armas** (nombres del juego, en latino ✅): el cohete tiburón
  **Fishbones**, la minigun **Pow-Pow**, las granadas **«¡Mascafuegos!»**,
  el **«¡¡Supermegacohete Requetemortal!!»**.
- **Con quién aparece**: Vi, Silco, Ekko, Isha, Sevika; de niña con
  Mylo, Claggor, Vander y Ekko.
- **Voz**: Ella Purnell (inglés); **Karla Falcón** (latino) ✅.

### Vi — «la Vigilante de Piltóver»

- **Quién es**: la hermana mayor. Luchadora, protectora, años en la
  prisión de Aguasquietas (Stillwater). Sale para buscar a Powder y
  acaba de compañera de Caitlyn ✅ (lore oficial `es_MX`,
  [Wikipedia: Vi](https://en.wikipedia.org/wiki/Vi_(League_of_Legends))).
- **Qué le importa**: su hermana. **Miedo**: haberla perdido por su
  culpa.
- **T2**: se pone **uniforme de agente** y vuelve a llevar sus
  **gafas** del diseño original ✅ ([Screen Rant](https://screenrant.com/arcane-season-2-teaser-trailer-vi-new-costume-caitlyn-team/)).
- **Cómo se expresa** ⚠️ de memoria: seca, sarcástica, pocas palabras;
  puños en guardia; brazos cruzados apoyada en la pared; a Caitlyn la
  pica con **«bombón» / «pastelito»** (así en latino, ver §10).
- **Voz**: Hailee Steinfeld (inglés); **Romina Marroquín Payró** (latino) ✅.

### Jayce Talis — «el Defensor del Mañana»

- **Quién es**: inventor de Piltóver que, con Viktor, hace la
  **Hextech** (magia con runas). Admirado como «el hombre del progreso»,
  luego **concejal** ✅ (lore `es_MX`; [The Review Geek 1×04](https://www.thereviewgeek.com/arcane-s1e4review/)).
- **Qué le importa**: que el invento ayude a todos. **Miedo**: que su
  invento se use para matar, y perder a Viktor.
- **Cómo se expresa**: de discurso, idealista («es la era de la
  Hextech») ✅. ⚠️ de memoria: gesticula con las manos abiertas, se
  inclina sobre la mesa de trabajo, levanta las piezas para enseñarlas.
- **Objetos**: el **martillo de Mercurio**, las gemas, sus planos.
- **Voz**: Kevin Alejandro (inglés) ✅ ([Infobae](https://www.infobae.com/latinpower/gaming/2021/11/14/kevin-alejandro-actor-de-voz-de-arcane-cuando-le-dije-a-mi-hijo-que-iba-a-participar-me-dijo-emocionado-papa-sabes-lo-que-estas-haciendo/)); latino, ver §10 ⚠️.

### Viktor — de ayudante a «Heraldo»

- **Quién es**: chico de Zaun, ayudante de Heimerdinger, genio y
  enfermo. Anda con **bastón y un aparato en la pierna** ⚠️ de memoria.
  Es el socio de Jayce: «**nuestro** sueño Hextech» ✅. Crea el **Núcleo
  Hex** (Hexcore). En la T2 cambia de cuerpo y de color (pelo blanco,
  túnica lila, splash `Viktor_24`) ✅ visto; su lore oficial `es_MX` lo
  llama «el Heraldo de lo Arcano» y habla de «la Gloriosa Evolución» ✅.
- **Qué le importa**: que nadie sufra lo que sufre él; ayudar a Zaun.
  **Miedo**: morir antes de terminar.
- **Cómo se expresa** ⚠️ de memoria: voz baja, frases exactas, humor
  seco; se apoya en el bastón; examina las cosas de cerca, con la mano
  abierta bajo la pieza.
- **La pareja Jayce-Viktor («Jayvik»)** fue el **n.º 15 de AO3 en 2024**,
  la primera vez en el top 100 ✅ ([esports.gg](https://esports.gg/news/league-of-legends/two-arcane-pairings-breach-top-20-ships-on-ao3-for-2024/)).
- **Voz**: Harry Lloyd (inglés); **Igor Cruz** (latino) ✅.

### Caitlyn Kiramman — «la Sheriff de Piltóver»

- **Quién es**: hija de una familia rica de Piltóver, agente idealista.
  Lleva tiempo **investigando por su cuenta** lo que Jayce llama «la
  Gran Conspiración»; sigue la pista del espray de Jinx ✅
  ([PC Gamer 1×04](https://www.pcgamer.com/arcane-episode-4-recap-ghosts-of-the-past/),
  [TV Tropes: Caitlyn](https://tvtropes.org/pmwiki/pmwiki.php/Characters/ArcaneCaitlynKiramman)).
  En la T2 manda tropas: **boina blanca** ✅ (splash `Caitlyn_50`,
  [Screen Rant](https://screenrant.com/arcane-season-2-teaser-trailer-vi-new-costume-caitlyn-team/)).
- **Cómo se expresa** ⚠️ de memoria: correcta, directa, curiosa; pose
  recta con el rifle; piensa con la mano en la barbilla.
- **Caitlyn y Vi («Caitvi»)**: n.º 17 de AO3 en 2024 ✅ (esports.gg).
- **Voz**: Katie Leung (inglés) ⚠️ de memoria; **Karina Altamirano** (latino) ✅.

### Ekko — «el Joven que Fragmentó el Tiempo»

- **Quién es**: amigo de infancia de Powder. De mayor, **líder de los
  Firelights**, que luchan contra Silco desde un **árbol escondido**; allí
  pintan el **mural de sus muertos** ✅ ([Screenspy 1×07](https://www.screenspy.com/arcane-season-1-episode-7/)).
  El cartel de la T2 lo resume: «**From Little Man to The Boy Savior**» ✅
  ([ComicBook](https://comicbook.com/gaming/news/arcane-season-2-netflix-ekko-poster/)).
- **Qué le importa**: su gente; y Powder, aunque sea Jinx.
- **Diseño del final (2×09)**: mezcla su paleta con la de Jinx a
  propósito ✅ ([Netflix Tudum](https://www.netflix.com/tudum/features/arcane-season-two-behind-the-scenes)).
- **Cómo se expresa** ⚠️ de memoria: seguro, callado, líder; aerotabla;
  bate con engranajes. Bufanda naranja (avatar R6 ✅).
- **Voz**: Reed Shannon (inglés) ⚠️ de memoria; **José Antonio Toledano** (latino) ✅.

### Silco — el villano que el fandom adora

- **Quién es**: el capo de Zaun; antiguo compañero de Vander; adopta a
  Jinx. Personaje **creado desde cero** para la serie ✅
  ([Game Rant](https://gamerant.com/arcane-silco-perfect-villain/)).
  Su actor: «**es el héroe de otra historia**» ✅
  ([Upcomer](https://upcomer.com/jason-spisak-on-arcanes-silco-hes-the-hero-of-a-different-story/)).
- **Cómo se expresa**: voz suave y amenazante, palabras medidas ✅
  (Game Rant). ⚠️ de memoria: cicatriz y ojo dañado en el lado
  izquierdo; siempre en su despacho.
- **No sirve para estos canales**: es oscuro y su final es de muerte.
  Úsalo sólo como guiño.
- **Voz**: Jason Spisak (inglés); **Nicolás Frías** (latino) ✅.

### Secundarios a mano

| Quién | Para qué sirve | Estado |
|---|---|---|
| **Heimerdinger** («el Venerable Inventor») | El profesor que frena a Jayce. En la splash `Heimerdinger_33` **toca el banjo** rodeado de niños | ✅ splash |
| **Mel Medarda** («el Reflejo del Alma») | Concejal; propone a Jayce para el Consejo en 1×04 | ✅ |
| **Isha** | La niña de la T2 que pinta con Jinx | ✅ (TV Tropes 2×04) |
| **Sevika**, **Vander/Warwick**, **Ambessa** | Oscuros; no para estos canales | — |

---

## 9 · ¿Quién es el más querido?

| Encuesta | Resultado | Fuente |
|---|---|---|
| Encuesta de Reddit recogida por Screen Rant | **Jinx**, la única con más de 200 votos | ✅ [Screen Rant](https://screenrant.com/arcane-best-characters-reddit/) |
| Ranking mundial de VainKeurz (más de 157.400 duelos) | 1.º **Powder/Jinx**, 2.º **Vi**, 3.º **Silco** | ⚠️ una fuente ([VainKeurz](https://vainkeurz.com/tv-shows/league-of-legends-arcane/toplist-worldwide/best-arcane-characters/7_R9IscZ)) |
| China (Douban, Xiaomi, Huxiu) | «La popularidad de Jinx en solitario es la más alta»; «Jinx le dio prestigio a Tencent» | ✅ ([Douban](https://www.douban.com/group/topic/313961123/), [Xiaomi](https://game.xiaomi.com/viewpoint/1375999065_1638465807743_16), [Huxiu](https://m.huxiu.com/article/474375.html)) |
| China, reacción al acto 2 de la T2 | **Viktor** recibe «montones de notas perfectas» | ⚠️ ([GamerSky](https://www.gamersky.com/news/202411/1846266.shtml)) |
| AO3 2024 (parejas) | **Jayvik** n.º 15, **Caitvi** n.º 17 | ✅ [esports.gg](https://esports.gg/news/league-of-legends/two-arcane-pairings-breach-top-20-ships-on-ao3-for-2024/) |
| Encuesta de IMDb | existe; resultado sin ver | ⚠️ [IMDb](https://www.imdb.com/poll/ef72fiSOfgA/) |
| Corea | no encontré encuesta | — |

**Conclusión**: **Jinx** es la cara de la serie y la más querida. Detrás,
**Vi** y **Silco**. **Viktor** subió mucho en la T2, y **Jayce+Viktor**
juntos son una de las parejas más escritas de 2024.
Para #arte, Jinx sin duda. Para #proyectos, **Jayce y Viktor juntos**
(el equipo es el mensaje del canal).

---

## 10 · Doblaje latino

> Doblaje Wiki no abría (403). Todo sale de otras fuentes y de lo que el
> buscador leyó de Doblaje Wiki. **Hay otro doblaje, el de España**
> ([Doblaje España Wiki](https://doblaje-espana.fandom.com/es/wiki/Arcane),
> [Vandal](https://vandal.elespanol.com/noticia/1350748054/lol-este-es-el-reparto-de-actores-de-doblaje-para-la-serie-arcane-de-netflix/)):
> no confundirlos.

### 10.1 Reparto

| Personaje | Actor latino | Estado y fuentes |
|---|---|---|
| **Jinx** | **Karla Falcón** (también Jinx en el juego; Dulce Princesa en *Hora de Aventura*) | ✅ [Rock&Pop](https://www.rockandpop.cl/2024/10/festigame-itau-2024-las-voces-de-arcane-estaran-presentes-en-el-esperado-evento-de-videojuegos/), [Alerta Geek](https://www.alertageekchile.cl/2024/10/21/festigame-2024-confirma-a-voces-de-latinas-de-arcane-como-invitados/), [FestiGame](https://cl.festigame.com/las-voces-de-arcane-se-toman-festigame-itau-2024/) |
| **Vi** | **Romina Marroquín Payró** | ✅ mismas fuentes + [Bolavip](https://bolavip.com/gamer/Arcane-la-serie-de-League-of-Legends-confirma-su-elenco-de-voces-en-latino-20210921-0044.html) |
| **Viktor** | **Igor Cruz** | ✅ mismas fuentes |
| **Silco** | **Nicolás Frías** (el profesor Frink de *Los Simpson*) | ✅ [Bolavip](https://bolavip.com/gamer/Arcane-la-serie-de-League-of-Legends-confirma-su-elenco-de-voces-en-latino-20210921-0044.html), [TikTok SDV](https://www.tiktok.com/@sdv_serviciosdevoz/video/7414674465876937989) |
| **Caitlyn** | **Karina Altamirano** (Lois en *Padre de familia*) | ✅ [TikTok SDV](https://www.tiktok.com/@sdv_serviciosdevoz/video/7442462275287452983), [AniList](https://anilist.co/staff/108265/Karina-Altamirano) |
| **Ekko** | **José Antonio Toledano** (también en el juego) | ✅ [TikTok SDV](https://www.tiktok.com/@sdv_serviciosdevoz/video/7416131651387854086?lang=es), [Starcon](https://www.facebook.com/starconmx/posts/jos%C3%A9-antonio-toledano-actor-de-doblaje-que-dio-voz-a-ekko-en-el-universo-league-/1446435646854462/) |
| **Jayce** | **Miguel de León** (Bugs Bunny en *Looney Tunes Cartoons*) | ⚠️ una búsqueda dice que hace a Jayce **joven**, otra que en la T2; en el juego dobla a «Arcane: Jayce Sobreviviente» ([TikTok](https://www.tiktok.com/@.ru_ma/video/7440738759320096055)). Otra búsqueda nombró a **Michel Tejerina**, que parece del doblaje **de España**. **Comprobar** |
| **Heimerdinger** | José Luis Orozco (repite del juego) | ⚠️ una fuente |
| **Vander** | Dafnis Fernández | ⚠️ una fuente (Bolavip, vía buscador) |
| **Mel** | Adriana Núñez | ⚠️ una fuente |
| **Marcus** | Eduardo Garza | ⚠️ una fuente |

**Estudio y dirección**:
- **T1**: **Sysdub**, dirección de **Eduardo Garza** (director del juego
  *League of Legends* de 2014 a 2017) ⚠️ (dos búsquedas, pero parece la
  misma fuente de fondo, Doblaje Wiki).
- **T2**: **Iyuno México**, dirección de **Angie Villa**, traducción de
  **Briana González** ✅ ([Bubbleblabber LATAM](https://latam.bubbleblabber.com/2024/11/netflix-estrena-el-doblaje-de-la-segunda-temporada-de-arcane-en-espanol-latino/)
  y Doblaje Wiki, vía buscador).
- En noviembre de 2024 **Karla Falcón, Romina Marroquín e Igor Cruz**
  fueron invitados a FestiGame (Santiago de Chile) ✅ (fuentes de arriba).

### 10.2 Frases y decisiones del doblaje latino

| Quién | Frase | Estado |
|---|---|---|
| Vi a Caitlyn (1×08) | «It's been real, cupcake» → «**Fue un placer, cariño**» | ✅ Doblaje Wiki (vía buscador) y la guía de cuadros |
| Vi a Caitlyn (T1) | «cupcake» → «**Bombón**» | ⚠️ Doblaje Wiki (vía buscador) |
| Vi a Caitlyn (T2) | «cupcake» → «**Pastelito**», más fiel | ⚠️ Doblaje Wiki (vía buscador) |
| Jinx a Vi (1×09, con un pastelito) | «**Mira, traje a tu novia**» (el chiste de «cupcake» se pierde porque en la T1 era «bombón») | ⚠️ Doblaje Wiki (vía buscador) |
| Ekko (2×07) | «**A veces, para dar un paso hacia adelante, hay que dejar algo atrás**» | ⚠️ la guía de cuadros, que cita Doblaje Wiki |
| Silco (1×09) | «You're perfect» → ❌ no encontré cómo se dijo | — |

### 10.3 Nombres oficiales en latino (del juego)

Del archivo `es_MX` de Data Dragon ✅: **Piltóver** (con tilde),
**Concejo de Piltóver**, **Distrito Suburbano** (así llama el juego a la
ciudad subterránea), **Prisión de Aguasquietas**. Si la lámina escribe
«Piltóver», que lleve tilde, como en el juego latino. Cómo lo pronuncia
el doblaje de la serie ⚠️.

---

## 11 · Música

| Tema | Quién | Dónde | Ambiente | Estado |
|---|---|---|---|---|
| **Enemy** (opening) | Imagine Dragons y JID | Opening. Salió el 28-oct-2021 | Épico, rabioso. El coro «**Oh, the misery**» es meme | ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Enemy_(Imagine_Dragons_and_JID_song)), [PC Gamer](https://www.pcgamer.com/league-of-legends-gets-a-new-music-video-featuring-imagine-dragons-for-its-upcoming-tv-series/), [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Memes/Arcane)) |
| Playground | Bea Miller | T1 | Infancia rota, susurro | ✅ tema ([NME](https://www.nme.com/news/tv/arcane-soundtrack-every-song-season-2-3811242)); escena ⚠️ |
| Goodbye | Ramsey | T1 | Despedida de las hermanas ⚠️ | ✅ tema (NME) |
| Guns for Hire | Woodkid | T1 | Épico, tambores | ✅ tema (NME) |
| Dynasties and Dystopia | Denzel Curry, Gizzle, Bren Joy | T1 | Hip-hop de Zaun | ✅ tema (NME) |
| Snakes | PVRIS y MIYAVI | T1 | Oscuro, seductor | ✅ tema (NME) |
| What Could Have Been | Sting y Ray Chen | T1 | Nostalgia, violín | ✅ tema (NME) |
| **Paint the Town Blue** | **Ashnikko** | **Inicio de 2×04**, montaje de los Jinxers | **Juguetón, gamberro, de pintar paredes. La canción de #arte** | ✅ ([Arcane Wiki](https://arcane.fandom.com/wiki/Paint_the_Town_Blue_(song)), [Wikipedia S2](https://en.wikipedia.org/wiki/Arcane_League_of_Legends:_Season_2)) |
| Come Play | — | Single T2 (16-oct-2024) | ⚠️ intérpretes de memoria | ✅ fecha |
| Blood Sweat & Tears | — | Single T2 (26-oct-2024) | ⚠️ | ✅ fecha |
| Remember Me | — | Single T2 (15-nov-2024) | ⚠️ | ✅ fecha |
| The Line | Twenty One Pilots | Single T2 (22-nov-2024) | ⚠️ | ✅ |
| Ma meilleure ennemie | — | Single T2 (6-dic-2024) | Francés, dúo de enemigos que se quieren | ✅ fecha; intérpretes ⚠️ |
| (varias) | Freya Ridings | T2 | ⚠️ | ✅ nombre |

- La banda sonora de la T1 salió **en tres partes**, una por acto
  (6, 13 y 20 de noviembre de 2021); la de la T2 tiene **22 temas**
  (23-nov-2024) ✅ ([LoL Wiki: Soundtrack](https://wiki.leagueoflegends.com/en-us/Arcane_(Soundtrack)), [Wikipedia S2](https://en.wikipedia.org/wiki/Arcane_League_of_Legends:_Season_2)).
- Por escena: [Tunefind T2](https://www.tunefind.com/show/arcane/season-2).
- **Para #proyectos**: el ambiente es el del laboratorio (cuerdas,
  esperanza). **Para #arte**: «Paint the Town Blue».

---

## 12 · Vídeos

> YouTube no abría desde aquí: **no tengo minutos exactos**. Los enlaces
> salen de los resultados de búsqueda.

| Vídeo | Para qué sirve | Enlace |
|---|---|---|
| **Enemy**, vídeo oficial (animado por Fortiche, la banda como personajes de Arcane; **409 millones de vistas**) | Estilo, poses de la banda en Zaun | [YouTube](https://www.youtube.com/watch?v=F5tSoaJ93ac) ✅ |
| Tráiler oficial T2 (5-sep-2024) | Poses de la T2 | [LoL](https://leagueoflegends.com/en-us/news/media/arcane-season-2-official-trailer) ✅ |
| Teaser oficial T2 | Vi de agente | [LoL](https://www.leagueoflegends.com/en-us/news/media/arcane-season-2--official-teaser-trailer-/) ✅ |
| Making of T2: dirección de arte (Fortiche) | Cómo pintan | [YouTube Shorts](https://www.youtube.com/shorts/pA5aa8zbyIg) ✅ |
| Entrevista a los creadores de Fortiche (francés) | Los secretos de la creación | [YouTube](https://www.youtube.com/watch?v=pYY0HpyAPa4) ✅ |
| Charrue y Delord en MIFA | Estilo del estudio | [YouTube](https://www.youtube.com/watch?v=YWDPC2cgr3c) ✅ |
| Jayce y Viktor, el experimento del acto 1 | La escena de la Hextech (1×03) | [YouTube](https://www.youtube.com/watch?v=v91giP0wo5Y) ⚠️ subida de fan |
| Las voces latinas de Arcane | Oír el doblaje | [YouTube 1](https://www.youtube.com/watch?v=2ReoiBnYdkc), [YouTube 2](https://www.youtube.com/watch?v=eDalIyzRMbM), [YouTube 3](https://www.youtube.com/watch?v=TQ5GBqCJUiU) ⚠️ |
| Retos de doblaje de SDV con las voces oficiales | Frases en latino, voz por voz | [Silco](https://www.tiktok.com/@sdv_serviciosdevoz/video/7414674465876937989), [Caitlyn](https://www.tiktok.com/@sdv_serviciosdevoz/video/7442462275287452983), [Ekko](https://www.tiktok.com/@sdv_serviciosdevoz/video/7416131651387854086?lang=es), [Jinx](https://www.tiktok.com/@sdv_serviciosdevoz/video/7413937045812382981), [Vi](https://www.tiktok.com/@sdv_serviciosdevoz/video/7441395739810401591) |
| Entrevista a Karla Falcón en FestiGame 2024 | Cómo vive a Jinx | [TikTok](https://www.tiktok.com/@eldiariodelalquimista/video/7440244073505623352?lang=es) |
| Tutorial del grafiti de «Paint the Town Blue» | Tendencia TikTok; cómo se hace el grafiti de Jinx | [TikTok](https://www.tiktok.com/@joaotiagovarao/video/7451046601671331077) |
| Todas las cinemáticas de Arcane en Path of Champions | Arte de juego | [YouTube](https://www.youtube.com/watch?v=kK5uchh1-0Y) |

---

## 13 · Videojuegos de la franquicia

| Juego | Qué tiene de Arcane | Cómo «hablan» | Estado |
|---|---|---|---|
| **League of Legends** | Skins «Arcane» de Jinx, Vi, Jayce, Viktor, Caitlyn, Ekko, Heimerdinger, Mel y Warwick (lista y nombres latinos en §3.1) | Frases sueltas de cada campeón; sin cajas de diálogo | ✅ (Data Dragon) |
| **RiotX Arcane** (evento web, 2021) | El mapa-plano de Piltóver (R1), fondos y avatares | ⚠️ no vi el evento | ✅ los archivos (los tengo); la dirección `riotxarcane.riotgames.com` sale en un tuit de LoL LATAM copiado en [cocotbodol](https://www.cocotbodol.com/author/lollatam) ⚠️ |
| **Legends of Runeterra: Path of Champions** (evento Arcane) | Historia en Piltóver y Zaun; historias de Jinx y Vi | **«Cómics animados» con voces** y decisiones que cambian el final. Ej.: Vi: «If I hear fat-hands one more time!» / Jinx: «Jeeez. Least one of us got a sense of humor» | ✅ ([Destructoid](https://www.destructoid.com/legends-of-runeterra-path-of-champions-single-player-story-jinx-vi-jayce/), [YouTube: Jinx](https://www.youtube.com/watch?v=L4-suaLzH7Y), [YouTube: Vi](https://www.youtube.com/watch?v=OZzo7hmPonA)); cómo es la caja ⚠️ |
| **2XKO** (lucha, Riot) | Jinx, Ekko, Vi… | **Diálogos de entrada** entre parejas de campeones | ✅ ([Game8](https://game8.co/articles/latest/2xko-gameplay-and-story), [2XKO Wiki: Jinx](https://wiki.play2xko.com/en-us/Jinx/Audio), [YouTube](https://www.youtube.com/watch?v=JwGyVB_etaA)) |

**Lo útil para la lámina**: el **«cómic animado» de Path of Champions**
confirma que Riot cuenta Arcane en viñetas pintadas. Si hace falta una
caja de texto, **una viñeta pintada con su texto en la parte de abajo**
es más de Arcane que un globo. Cómo es exactamente: ⚠️ no vi capturas.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todos reconocen

- **«Oh, the misery»**, el coro de *Enemy*, para cualquier momento de
  sufrimiento ✅ ([TV Tropes: Memes](https://tvtropes.org/pmwiki/pmwiki.php/Memes/Arcane)).
- **«Jinx necesita terapia»** ✅ (TV Tropes).
- **Silco, padre entregado** frente a Vander, «padre torpe» ✅ (TV Tropes).
- **«[X] FROM ARCANE»**: llamar así a los campeones en los directos de LoL ✅ (TV Tropes).
- Jayce en la T2 «haciendo un *speedrun* de toda la saga Dark Souls» ⚠️ (una fuente, TV Tropes).
- **«Cupcake»** de Vi a Caitlyn (en latino «bombón»/«pastelito») ✅.
- **«Paint the Town Blue»** y el pelo azul de los Jinxers ✅.
- El **mural de los Firelights** y **el retrato de Powder** (suena el
  tema de Jinx cuando la cámara llega a él) ✅ ([Screenspy](https://www.screenspy.com/arcane-season-1-episode-7/)).
- Las parejas **Jayvik** y **Caitvi** ✅ (§9).

### 14.2 Qué NO hacer (lo que un fan notaría)

- **Mezclar la ropa del juego con la de la serie.** Los fondos de RiotX
  (R2-R5) llevan la ropa **del juego**: Caitlyn con **sombrero de copa**,
  Vi con armadura dorada, Jinx con **medias a rombos rosas**. En Arcane
  no visten así. Usa los avatares (R6) o las splash «Arcane».
- **Jinx alegre de colores pastel.** Es rosa neón y cian **sobre negro
  sucio**; su alegría da miedo.
- **Hextech de otro color.** La Hextech es **azul**. El morado-rosa es
  otra cosa (el Shimmer, Viktor de la T2); el verde, el quimtech de Zaun.
  Cada magia tiene su paleta ✅ ([Netflix Tudum](https://www.netflix.com/tudum/features/arcane-season-two-behind-the-scenes)).
- **Piltóver verde o Zaun dorada.** Piltóver es oro y Art Déco; Zaun,
  verde y Art Nouveau ✅ (§5).
- **Viktor de la T1 sin bastón** ⚠️ de memoria.
- **Planos azules modernos** (*blueprint* de fondo azul): los de Arcane
  son sepia a lápiz (R1).
- **Momentos de muerte para un canal alegre**: la muerte de Silco, de
  Vander o de Isha. Son lo más querido, pero son un funeral.
- **Mezclar los dos doblajes**: una frase del doblaje de España puesta
  como latina.

---

## 15 · Poses analizadas por personaje

> Las imágenes con código (S1…S14, R1…R6) están en §3. Las escenas sin
> fotograma van con ⚠️: son de memoria o de una sinopsis.

### Jinx

| # | Imagen o escena | Postura | Manos | Mirada y gesto | Sirve para |
|---|---|---|---|---|---|
| 1 | S2 `Jinx_60` | Inclinada hacia delante, cargando el Pow-Pow | Las dos en el arma | Ceño fruncido, directa a cámara | **Regañar**, avisar |
| 2 | S2, el vitral de la izquierda | Jinx pintada, de lado, brazo arriba | Una mano en el pelo | Boca abierta, grito | **Celebrar** a lo loco |
| 3 | S1 `Jinx_37` | De pie, peso en una pierna, en la niebla | Una mano baja con una bomba | Media sonrisa desde la sombra | **Presentar** con misterio |
| 4 | R2 (estilo juego) | Salto, brazo extendido | Mano abierta hacia fuera | Risa a carcajadas | **Animar** (sólo pose) |
| 5 | R6 avatar | Busto frontal | — | Ojos entornados, desconfiada | Retrato |
| 6 | 2×04, montaje de «Paint the Town Blue» | Pintando la pared, con Isha | Brocha o espray | Juguetona, rompe la cuarta pared | **Explicar #arte** ✅ la escena; pose ⚠️ |
| 7 | 1×04, el laboratorio | Entra de noche, deja su pintura | Espray | — | Guiño #proyectos ⚠️ |
| 8 | `Caitlyn_28` (primer plano) | El **mono de juguete** de Jinx con ojo rojo encendido y cristales pintados | — | — | Firma de Jinx sin Jinx |

### Jayce

| # | Imagen o escena | Postura | Manos | Mirada y gesto | Sirve para |
|---|---|---|---|---|---|
| 1 | S5 `Jayce_24` | **En un atril de latón con bocinas de gramófono** (un discurso); el martillo en una vitrina detrás | **Derecha levantada, puño con la gema azul**; izquierda abierta, invitando | Sonríe hablando, mira la gema | **Presentar** ✅ (visto) |
| 2 | S6 `Jayce_35` | Encorvado, abrazado al martillo | Una mano en la cabeza | Agotado, roto | **Pensar**, dudar, «En pausa» |
| 3 | R4 (estilo juego) | Martillo en diagonal, cargando | Las dos en el mango | Sonrisa segura | Acción |
| 4 | R6 avatar | Busto, abrigo blanco, pañuelo rojo | — | Serio, frontal | Retrato |
| 5 | 1×03, la prueba nocturna | Todo flota a su alrededor | Brazos abiertos ⚠️ | Asombro | **Celebrar** «¡funciona!» ✅ escena |
| 6 | 1×04, discurso del Día del Progreso | Ante el público | ⚠️ | ⚠️ | **Anunciar** ✅ escena |
| 7 | 1×04, enseña inventos a Heimerdinger (gema fortificada, guanteletes Atlas) | Junto a la mesa | Señala la pieza ⚠️ | Orgullo | **Explicar** un proyecto ✅ escena ([PC Gamer](https://www.pcgamer.com/arcane-episode-4-recap-ghosts-of-the-past/)) |

### Viktor

| # | Imagen o escena | Postura | Manos | Mirada y gesto | Sirve para |
|---|---|---|---|---|---|
| 1 | S7 `Viktor_24` (T2) | De pie, túnica lila, bastón alto | **Mano abierta tendida hacia quien mira** | Sereno, triste | **Invitar**, «únete» |
| 2 | R6 avatar (T1) | Busto, chaleco de punto gris, pañuelo granate | — | Ojos ámbar `#C88729`, cansado | Retrato |
| 3 | Concepto de Mariana Galiano (Jayce lo encuentra) | Caído | — | — | No para estos canales |
| 4 | 1×03, la prueba con Jayce | ⚠️ | ⚠️ | ⚠️ | **Equipo** ✅ escena |
| 5 | 1×06, el Núcleo Hex | Inclinado sobre el núcleo ⚠️ | ⚠️ | Fascinado ⚠️ | **Pensar** ⚠️ |

### Vi, Caitlyn y Ekko

| # | Imagen o escena | Qué hace | Sirve para |
|---|---|---|---|
| Vi 1 | S3 `Vi_29` | De pie, guantelete enorme a la altura del pecho, mirada dura | **Regañar**, poner orden |
| Vi 2 | S4 `Vi_48` | Rodilla en tierra tras el golpe | Acción |
| Vi 3 | R6 avatar | Uniforme azul de agente, gafas en la frente | Retrato T2 |
| Cait 1 | S8 `Caitlyn_28` | Rifle cruzado, avanza entre cristales pintados por Jinx | **Investigar** |
| Cait 2 | S9 `Caitlyn_50` | Boina blanca, rifle horizontal, tropas detrás | **Mandar**, anunciar |
| Ekko 1 | S10 `Ekko_36` | Salto con el bate en alto | **Animar**, acción |
| Ekko 2 | 1×07, delante del mural | Enseña el mural a Vi | **Explicar #arte** ✅ escena |
| Ekko 3 | R6 avatar | Bufanda naranja `#773019`, ceño serio | Retrato |

**Resumen de uso**:
- **Presentar**: Jayce S5 (el atril) · Jinx S1.
- **Explicar**: Jayce ante Heimerdinger (1×04) · Ekko ante el mural (1×07).
- **Celebrar**: la Hextech que flota (1×03) · Heimerdinger con el banjo (S12).
- **Regañar**: Jinx S2 · Vi S3.
- **Pensar**: Jayce S6.
- **Animar / invitar**: Viktor S7 (mano tendida).

---

## 16 · Vestuario

| Quién | Ropa icónica | Colores (hex medidos, ±10) | Estado |
|---|---|---|---|
| **Jinx T1** | Trenzas azules larguísimas, flequillo; top negro de tirantes con lazada en X (avatar); cinturones de balas; **nubes rosas tatuadas** ⚠️ | Pelo `#2C4F74` en sombra, `#6CCCFC` con luz; rosa `#FC6CFC` | ✅ avatar y splash; tatuajes ⚠️ |
| **Jinx T2 (final)** | Diseño final hecho entre Riot y Fortiche; la splash S2 la muestra con **capucha morada** | Morados, cian | ✅ existe ([ArtStation](https://www.artstation.com/artwork/lG4RrJ)); detalle ⚠️ |
| **Vi T1** | Chaqueta roja, vendas en las manos, pelo rojo-rosa con un lado rapado; tatuaje «VI» en la cara ⚠️ | Pelo `#7D2637`; chaqueta `#9C3C3C` | ✅ splash S3 |
| **Vi T2** | **Uniforme de agente** azul y **gafas** | Azul `#1E3159` | ✅ ([Screen Rant](https://screenrant.com/arcane-season-2-teaser-trailer-vi-new-costume-caitlyn-team/), avatar) |
| **Caitlyn T1** | Chaqueta marrón de cuero, blusa blanca, pantalón morado; rifle | Pelo azul marino `#121324` | ✅ splash S8 |
| **Caitlyn T2** | **Boina blanca** y uniforme azul | `#3C6CB4` | ✅ S9 |
| **Jayce T1** | Camisa blanca cruzada de botones redondos, pantalón granate, guantes marrones | Blanco roto, granate, oro | ✅ S5 |
| **Jayce (concejal)** | Abrigo blanco con ribetes dorados, pañuelo rojo oscuro `#551A1D` | | ✅ avatar |
| **Viktor T1** | Chaleco de punto gris, camisa oscura, pañuelo granate `#4D1A26`; bastón | Gris `#544A50` | ✅ avatar |
| **Viktor T2** | Pelo blanco, túnica lila | `#CC84FC` | ✅ S7 |
| **Ekko** | Bufanda naranja, pelo blanco en rastas cortas | Naranja `#773019` | ✅ avatar |

**Lo «icónico» que todos reconocen**: las **trenzas azules** de Jinx, la
**chaqueta roja** y los **guanteletes** de Vi, el **martillo** de Jayce,
el **bastón** de Viktor, el **rifle** de Caitlyn.

---

## 17 · Paisajes y fondos de pantalla

### 17.1 Los sitios, con su luz

- **Piltóver de día**: oro, cristal y cielo limpio; ventanales enormes
  con contraluz (splash `Mel_1`) ✅.
- **El laboratorio**: cortinas moradas, latón brillante, motas de polvo
  en la luz (splash `Jayce_24`) ✅.
- **Zaun**: neblina verde, farolas, tuberías, grafiti (splash `Jinx_37`,
  `Caitlyn_28`) ✅.
- **El árbol de los Firelights**: el único árbol grande de Zaun ✅; su luz ⚠️.

### 17.2 Fondos de pantalla oficiales y de fans

| Qué | Tamaño | Autor | Enlace |
|---|---|---|---|
| RiotX Arcane: Jinx, Vi, Jayce, Caitlyn (móvil) | 1440×2960 | Riot Games | [GitHub, carpeta extras/arcane/wallpapers](https://github.com/InFinity54/LoL_DDragon) ✅ |
| Mapa-plano de Piltóver | 3000×2280 | Riot Games | mismo repositorio, `extras/arcane/` ✅ |
| Splash arts «Arcane» | 1215×717 | Riot Games | mismo repositorio, `img/champion/splash/` ✅ |
| Fondos de los murales LATAM (la web de los murales tenía fondos descargables) | ⚠️ | los muralistas | [LoL LATAM](https://www.leagueoflegends.com/es-mx/news/community/murales-arcane/) ⚠️ no abrí |
| Fondos 4K de móvil (fan) | ⚠️ | yonecraft | [Gumroad](https://yonecraft.gumroad.com/l/Arcane4KWallpapersForMobile) ⚠️ |

---

## 18 · Guía para generar con IA (Firefly, Canva)

> El dueño pidió **«que no parezca hecho por IA»**. La IA sirve para
> **fondos, bocetos de pose y texturas**, no para el personaje final.
> El personaje sale de una imagen oficial, recortado por `v3/integrar.py`.

### 18.1 El estilo en palabras

- **Técnica**: «pintura digital con aspecto de óleo sobre 3D», «texturas
  pintadas a mano con pincelada visible», «iluminación de cine»,
  «efectos de humo y chispas dibujados a mano».
- **Piltóver**: «arquitectura Art Déco con latón y cristal», «luz dorada
  de atardecer entrando por ventanales», «motas de polvo en el aire».
- **Zaun**: «callejón industrial Art Nouveau con tuberías curvas»,
  «neblina verde química», «farolas de gas», «paredes de ladrillo con
  grafiti rosa neón y cian».
- **Planos Hextech**: «plano técnico a lápiz sobre papel sepia
  envejecido», «círculos de runas geométricas», «anotaciones a mano en
  una escritura inventada», «cristal hexagonal dibujado».

### 18.2 Rasgos que nunca cambian

| Quién | Nunca cambia |
|---|---|
| Jinx | Dos **trenzas azules larguísimas**, flequillo, muy delgada, piel pálida, **nubes rosas tatuadas**, cinturones de munición. Sonrisa torcida |
| Jayce | Pelo castaño oscuro peinado hacia atrás, mandíbula cuadrada, **camisa blanca**, martillo de latón con gema azul |
| Viktor (T1) | Delgado, ojeras, **ojos ámbar**, pelo castaño revuelto, **bastón**, chaleco gris, pañuelo granate |
| Vi | Pelo **rojo-rosa** con un lado rapado, nariz rota, **guanteletes** enormes |
| Caitlyn | Pelo **azul marino** muy largo, rifle largo, porte recto |
| Ekko | Piel oscura, **pelo blanco**, bufanda naranja |

### 18.3 Paleta, línea, sombra y luz

- Paleta de §5.2. **Sombras en violeta-gris** (`#202026`), nunca negras.
- **Sin contorno negro**: la forma sale del color y la luz, como en un
  cuadro. Sombreado suave con pincelada.
- **Luz**: una fuente fuerte y cálida más un contraluz de color (azul
  Hextech, verde Zaun o rosa Jinx).
- **Encuadre**: de cine, cámara un poco baja (como `Jayce_24` y
  `Caitlyn_28`), algo desenfocado en primer plano.

### 18.4 Palabras que ayudan y palabras que lo estropean

- ✅ Ayudan: *painterly*, *hand-painted textures*, *oil painting look*,
  *cinematic lighting*, *Art Deco*, *Art Nouveau*, *steampunk brass*,
  *volumetric haze*, *sepia blueprint*, *graffiti*, *spray paint drips*.
- ❌ Estropean: *anime*, *chibi*, *cel shading*, *Pixar*, *cute*,
  *pastel*, *cyberpunk neon city* (Arcane no es *cyberpunk*),
  *League of Legends splash art* (saca el estilo del juego),
  *blueprint* a secas (sale azul moderno).

### 18.5 Qué imágenes usar de referencia

- **Estilo de plano**: R1 (el mapa de RiotX).
- **Estilo de grafiti**: S2 `Jinx_60` (el vitral pintado) y S8 `Caitlyn_28`.
- **Luz de Piltóver**: S5 `Jayce_24` y S13 `Mel_1`.
- **Luz de Zaun**: S1 `Jinx_37` y S8.
- **Caras**: los avatares R6.
- **Poses**: §15.

---

## 19 · Tres conceptos de lámina

Los textos salen de §0. Las frases «en la voz de la serie» son **mías**,
no del doblaje latino (no las encontré). Recortes siempre por
`v3/integrar.py` y comprobados a 1:1.

### Concepto A — «La mesa de dibujo del laboratorio» (#proyectos)

- **Objeto y sitio**: una **mesa de dibujo inclinada** en el
  **laboratorio de Jayce y Viktor**, en Piltóver. Encima, **varios planos
  sepia** sujetos con pinzas de latón, uno encima de otro: cada plano es
  un proyecto. Sobre el de arriba, **una gema Hextech azul** hace de
  pisapapeles. Al lado: compás, regla, lápices, una lupa. En Blender:
  tablero de madera, hojas con curvatura y esquinas levantadas (la tinta
  sigue la curva), gema con emisión azul, martillo apoyado detrás
  ([Orivers Hextech hammer](https://sketchfab.com/3d-models/orivers-hextech-hammer-arcane-f04d59aed16347a6b7b074a0b044ea7a) ⚠️ licencia).
  El papel imita R1 (`#B39A84`, lápiz `#5B4D42`).
- **Personaje**: **Jayce y Viktor juntos** (el equipo es el mensaje).
  Jayce con la pose de S5 (`Jayce_24`): **puño en alto con la gema** y
  la otra mano abierta hacia la mesa. Viktor, a su lado, apoyado en el
  bastón, mirando el plano (cara del avatar R6; pose ⚠️ a buscar en 1×03).
  Si sólo cabe uno: Jayce.
- **Cómo habla**: sin globo. **Nota a lápiz** en el margen del plano,
  con flecha, en **Architects Daughter**: «**Un hilo por proyecto**».
  Debajo, con otra letra (**Caveat**) y como corrección de Viktor:
  «**nuestro** proyecto», como en 1×03. Los nombres, en **plaquitas de
  latón** con Cinzel.
- **Dónde va cada texto**:
  - **Proyectos**: en el **cajetín del plano** (el recuadro del título,
    abajo a la derecha, como en un plano de verdad), en Cinzel.
  - **Equipo, avance y entregas**: el plano dibuja un invento con **tres
    piezas numeradas**; cada número lleva su rótulo a lápiz: 1 Equipo,
    2 Avance, 3 Entregas.
  - **Oficial del servidor**: **sello dorado** de la Academia de
    Piltóver en la esquina. **De la comunidad**: **marca pintada con
    espray**, como de Zaun, en la otra esquina.
  - Guiño para fans: un **garabato rosa de Jinx** en una esquina del
    plano (en 1×04 entró en este laboratorio y dejó su pintura).
- **Para que no quede plano**: la gema **ilumina el papel desde abajo**
  en azul; **luz dorada de ventanal** por detrás; sombras moradas de
  cortina (como S5); **compás y cabeza del martillo desenfocados** en
  primer plano; motas de polvo en el haz de luz.
- **Lámina 2 (los estados)**: una **regleta de latón en la pared** con
  **8 fichas colgadas de ganchos**, en el orden de un proyecto:
  Buscando gente · En traducción · En grabación · En edición · En
  revisión · **Estrenado** (ficha con la gema encendida) · **En pausa**
  (gema apagada, gris) · **Cancelado** (plano tachado con una X a lápiz).
  Debajo, los dos sellos de origen.

### Concepto B — «La pared de Jinx» (#arte)

- **Objeto y sitio**: una **pared de ladrillo de Zaun** bajo una farola,
  con **botes de espray** por el suelo. En Blender: pared con relieve
  ([Painted Brick, CC0](https://polyhaven.com/a/painted_brick)), el
  grafiti como calcomanía que **se mete en las juntas del ladrillo**,
  botes ([Spray Paint Bottles, CC0](https://polyhaven.com/a/spray_paint_bottles)).
- **Personaje**: **Jinx**, la más querida. En cuclillas sobre una
  tubería o una caja, **bote de espray en la mano**, girada hacia quien
  mira. Cara y actitud de S2 (`Jinx_60`); movimiento del cuerpo de R2
  (sólo la pose: la ropa del juego no). Opcional: **Isha** pintando
  abajo, pequeña (2×04).
- **Cómo habla**: **lo que dice es el grafiti**. **Sedgwick Ave Display**
  en rosa `#FC6CFC` y cian `#6CCCFC`, con sus garabatos: estrellas,
  corazones, flechas, una carita con ojos en X. Nada de globo.
- **Dónde va cada texto**:
  - **Arte**: el *tag* gigante, en el centro de la pared.
  - **Dibujo, ilustración, diseño y fanart**: cuatro palabras sueltas
    pintadas alrededor, cada una con su garabato.
  - **Un hilo por pieza o por serie**: frase más pequeña, con flecha
    hacia el tag, en Permanent Marker.
  - **Etiqueta si aceptas encargos**: **lo más visible después del
    título**: rodeado con un círculo rosa y estrellas, o en un **cartel
    de cartón colgado** de un clavo.
- **Para que no quede plano**: la pintura **brilla** un poco (rosa y
  cian); cono de luz cálida de la farola; neblina verde al fondo; **un
  bote desenfocado y goterones** en primer plano; **una trenza de Jinx
  cruza por delante** del texto; el **mono de juguete** de Jinx en una
  esquina (S8).
- **Lámina 2 (las etiquetas)**: la misma pared más a lo ancho.
  - **Boceto · Proceso · Terminado**: **el mismo dibujo tres veces**: a
    tiza (contorno), a medio rellenar y terminado a todo color.
  - **Dibujo · Digital · Fanart · Miniatura · Diseno · Edit o AMV**:
    pegatinas y plantillas (*stencils*) sobre el ladrillo.
  - **Acepto encargos**: el cartel de cartón, otra vez.

### Concepto C — «El mural de los Firelights» (#arte, alternativa)

- **Objeto y sitio**: el **mural de los Firelights** en su escondite del
  **árbol** (1×07). En la escena hay **un retrato a medio pintar** ✅: es
  justo lo que hace la gente en #arte. En Blender: pared de madera o
  piedra con el mural como textura, **botes y brochas** en una tabla,
  una escalera, **raíces del árbol** entrando por un lado.
- **Personaje**: **Ekko**, el secundario más querido de Zaun, con una
  **brocha en la mano** delante del mural, girándose a explicar
  (escena de 1×07 en que se lo enseña a Vi ✅; la pose exacta ⚠️).
  Bufanda naranja (R6).
- **Cómo habla**: **letras pintadas a brocha** en tablas de madera
  clavadas junto al mural, en blanco sucio y verde Firelight ⚠️ (el
  color de su pintura no lo comprobé). Letra: Permanent Marker o Caveat
  Brush.
- **Dónde va cada texto**:
  - **Arte**: en la tabla de arriba, como el nombre del escondite.
  - **Dibujo, ilustración, diseño y fanart** y **un hilo por pieza o por
    serie**: en tablas más pequeñas.
  - **Boceto · Proceso · Terminado**: **tres retratos del mural**: uno a
    carboncillo, uno a medio pintar y uno terminado.
  - **Etiqueta si aceptas encargos**: una tabla aparte, con la máscara
    de los Firelights dibujada.
- **Cuidado**: el mural real es **un memorial a sus muertos**. En la
  lámina, los retratos **no pueden ser los muertos** (Vander, Powder…):
  que sean «retratos nuevos», o queda de funeral.
- **Para que no quede plano**: luz verde-azulada filtrada por las hojas
  ⚠️; **polen o luciérnagas** en el aire; **brocha y bote desenfocados**
  en primer plano; Ekko en contraluz.

### De reserva para #proyectos — «El tablero de Caitlyn»

Si A no convence: el **tablero de corcho** de la investigación de
Caitlyn («la Gran Conspiración», 1×04-1×05 ✅), con **fichas a máquina**
(Special Elite), **chinchetas e hilo rojo**. Cada ficha es un proyecto y
lleva **un sello de estado**. Caitlyn con la mano en la barbilla. ⚠️ No
comprobé cómo es su tablero en la serie.

### ¿Cuál primero?

1. **A para #proyectos**: es el objeto que propone el plan, mejorado
   (mesa en vez de «planos sueltos»), y tiene lámina 2 natural.
2. **B para #arte**: Jinx es la más querida y su pared es su voz.
3. **C** si el dueño prefiere algo menos oscuro que Jinx, o quiere un
   secundario querido en vez de la protagonista.

---

## 20 · Lo que no pude verificar

- **Minutos exactos** de todas las escenas: no hay subtítulos de Arcane
  en GitHub y los sitios de subtítulos y transcripciones daban error.
- **Fotogramas** de la serie: ninguno (Fandom, YouTube y Netflix
  cerrados). Todas las imágenes de §3 son de promoción y del juego.
- **Qué pinta Jinx exactamente** en el laboratorio (1×04) y en 2×04.
- **El tablero de Caitlyn** y **el escondite de Jinx** (sus paredes).
- **Colores y letras del mural** de los Firelights.
- **Jayce en latino**: Miguel de León es lo más probable, pero no está
  confirmado con dos fuentes limpias. También Heimerdinger, Vander, Mel
  y Marcus (una fuente cada uno).
- **Frases del doblaje latino** de Jinx, Silco, Jayce y Viktor.
- **Licencias exactas** de los modelos de Sketchfab (las dio el buscador).
- **Arcane Nine** y **Piltover x Zaun**: licencia y tildes.
- **La imagen oficial «The colors of Piltover vs Zaun»** (no abrió).
- **Cajas de diálogo** de Path of Champions y 2XKO: sin capturas.
- **Encuesta oficial** de popularidad: no encontré ninguna de Riot o
  Netflix; sólo de fans.
- Títulos de los episodios en español latino: la búsqueda dio una lista
  desordenada (de España) ⚠️. Mejor usar los títulos en inglés.

---

## 21 · Bitácora de búsqueda

### 21.1 Comprobación de red (24-sep-2026)

| Qué | Resultado |
|---|---|
| WebFetch a Doblaje Wiki (`api.php`), El Vortex, Bubbleblabber LATAM, 8flix | **Bloqueado** por el proxy |
| curl a wiki.leagueoflegends.com, arcane.fandom.com, arcane.com, leagueoflegends.com, Bolavip, Sketchfab, Game UI Database, ddragon.leagueoflegends.com, ArtStation, universe.leagueoflegends.com, tvsubtitles, subdl, srtfiles, Hugging Face, jsDelivr, Codeberg | **Sin respuesta (000)** |
| raw.githubusercontent.com, `git clone` de GitHub, PyPI | **Funcionan** |
| `herramientas/investigar_serie.py` | No se corrió (Fandom cerrado). **Sin hojas de contacto** y sin carpeta `hojas/` |

### 21.2 GitHub (sin cupo de búsquedas)

- **[InFinity54/LoL_DDragon](https://github.com/InFinity54/LoL_DDragon)**
  (clon parcial): `extras/arcane/` (mapa-plano, 4 fondos, 11 avatares),
  14 splash arts «Arcane» de `img/champion/splash/`, y los datos
  `latest/data/es_MX/champion/*.json` (nombres, títulos y habilidades en
  latino). Medí tamaños y colores con Pillow y numpy.
- **[google/fonts](https://github.com/google/fonts)** (clon parcial): 41
  familias probadas con fontTools para á é í ó ú ñ Ñ ¿ ¡ ü (40 bien;
  Nanum Pen Script sin tildes) y una hoja de prueba con texto en español.

### 21.3 Búsquedas web (50)

| # | Idioma | Búsqueda (resumida) | Qué salió |
|---|---|---|---|
| 1 | es | reparto latino Jinx, Vi, Jayce, Silco, Viktor | Vandal, Millenium (España), El Vortex, desdelacuna |
| 2 | en | Latin American dub cast, studio, director | Iyuno México, Angie Villa, Eduardo Garza |
| 3 | es | «Karla Falcón» «Romina Marroquín» «Igor Cruz» | FestiGame 2024 (tres fuentes) |
| 4 | es | Silco, Vander, «Eduardo Garza», Sysdub | Nicolás Frías, Dafnis Fernández, Karina Altamirano |
| 5 | es | Bolavip, elenco latino | Lista de Bolavip (vía buscador) |
| 6 | es | «Nicolás Frías» Silco | TikTok SDV |
| 7 | es | voz de Jayce en latino | Confusión Miguel de León / Michel Tejerina |
| 8 | es | «Karina Altamirano» Caitlyn | TikTok SDV, AniList |
| 9 | es | «Miguel de León» Jayce | «Jayce joven» / T2; sin cerrar |
| 10 | es | «Toledano» Ekko | TikTok SDV, Starcon |
| 11 | en | The Art of Arcane (Titan) | El libro y sus regalos (plano, mapa, carta) |
| 12 | en | Julien Georgel, texturas | 80.lv, Netflix Tudum, VFX Voice, AWN |
| 13 | en | garabatos 2D de Jinx | SyncSketch (12 fps), RedShark |
| 14 | en | laboratorio, planos Hextech, concept art | ArtStation Alexia Ferry, Mariana Galiano |
| 15 | en | 2×04 «Paint the Town Blue» | IMDb, LoL Wiki, TV Tropes |
| 16 | en | 1×04 «Happy Progress Day» | Review Geek, TV Tropes, transcripciones (cerradas) |
| 17 | en | subtítulos .srt de Arcane | Sólo webs de subtítulos (cerradas) |
| 18 | en | `site:github.com` subtítulos | **Nada** |
| 19 | en | encuesta de popularidad | Screen Rant (Reddit), VainKeurz, IMDb |
| 20 | zh | 双城之战 人气 投票 | Douban, Xiaomi, GamerSky: Jinx la más popular |
| 21 | en | carteles de personaje T2 | Netflix Tudum, Mary Sue, ComicBook |
| 22 | en | fuente del logo | Rotulado a medida; Arcane Nine (fan) |
| 23 | en | banda sonora T1 y T2 | NME, LoL Wiki, Wikipedia |
| 24 | es | frases icónicas del doblaje latino | **Nada** concreto |
| 25 | en | Sketchfab Hextech CC | Guantelete, granada, Jinx |
| 26 | fr | Fortiche, dirección artística | Cineuropa, AWN, ESMA, YouTube (francés) |
| 27 | ko | 아케인 인기 캐릭터 순위 | Namuwiki; **sin encuesta** |
| 28 | en | escondite de Jinx, dibujos | Muñecos de Mylo y Claggor; dibujos **no** |
| 29 | es | murales Arcane en Latinoamérica | LoL LATAM, La República |
| 30 | en | tráilers y vídeo de *Enemy* | YouTube, LoL |
| 31 | es | artistas de los murales | Alucina, Montserrat Ventura; los otros **no** |
| 32 | en | investigación de Caitlyn | «La Gran Conspiración»; tablero **no** |
| 33 | en | mural de los Firelights | Screenspy, Arcane Wiki |
| 34 | en | 1×03, la prueba Hextech | «nuestro sueño», «era de la Hextech» |
| 35 | en | 2XKO y Runeterra, diálogos | Game8, 2XKO Wiki, YouTube |
| 36 | en | memes del fandom | TV Tropes Memes |
| 37 | es | «pastelito» / «cupcake» en latino | Bombón (T1), Pastelito (T2), «Fue un placer, cariño» |
| 38 | en | vestuario T2 | Tudum (Ekko con la paleta de Jinx), Screen Rant |
| 39 | en | fuente de runas Hextech | Piltover x Zaun (DeviantArt) |
| 40 | en | Poly Haven espray y ladrillo | Dos recursos CC0 |
| 41 | es | entrevista a Karla Falcón | Sólo TikToks |
| 42 | en | paletas Piltóver y Zaun | 80.lv, Fizzy Mag, X oficial |
| 43 | en | fan art del grafiti de Jinx | DeviantArt, ArtStation |
| 44 | en | Sketchfab martillo de Jayce | Varios modelos |
| 45 | en | parejas y popularidad 2024 | AO3: Jayvik 15.º, Caitvi 17.º |
| 46 | en | símbolos del grafiti de Jinx | Nada oficial |
| 47 | en | Silco, «You're perfect» | Game Rant, Upcomer, Looper |
| 48 | es | títulos en español latino | Lista confusa (España) |
| 49 | en | 1×04, pintura de Jinx en el laboratorio | PC Gamer: el espray como prueba; guanteletes Atlas |
| 50 | en | Path of Champions, caja de diálogo | Destructoid: «cómics animados»; caja **no** |

### 21.4 Fuentes consultadas por tipo

- **Oficiales**: Data Dragon (Riot, vía GitHub), Netflix Tudum, LoL
  LATAM (murales), leagueoflegends.com (tráilers), X de @arcaneshow, X de
  Fortiche, 2XKO (Riot).
- **Staff y making of**: 80.lv (Arnaud-Loris Baudry, Julien Georgel),
  SyncSketch (Alexis Wanneroy), AWN, Cineuropa, VFX Voice, RedShark,
  Upcomer (Jason Spisak), libro de arte (Titan).
- **Otros idiomas**: chino (Douban, Xiaomi, GamerSky, Huxiu), coreano
  (Namuwiki), francés (Fortiche, YouTube).
- **Wikis**: Arcane Wiki, LoL Wiki, 2XKO Wiki, TV Tropes (sólo por el
  buscador).
- **Arte**: ArtStation, DeviantArt, Tumblr (art-of-arcane), Sketchfab,
  Poly Haven.
- **Doblaje**: Bolavip, FestiGame, Rock&Pop, Alerta Geek, TikTok de SDV,
  AniList, Starcon, Doblaje Wiki (sólo vía buscador).
- **Prensa**: PC Gamer, Screen Rant, Game Rant, Looper, ComicBook, The
  Mary Sue, Bleeding Cool, CGMagazine, NME, Destructoid, esports.gg.

### 21.5 Lo que NO encontré

- Subtítulos con tiempos, transcripciones abiertas y fotogramas.
- El reparto latino completo en Doblaje Wiki (403).
- Frases del doblaje latino de Silco, Jinx (salvo una), Jayce y Viktor.
- Encuesta oficial de popularidad (Riot, Netflix) ni coreana.
- Cómo son las cajas de diálogo de los juegos.
- Autores de los murales de Lima, Santiago y Buenos Aires.
- Las paredes del escondite de Jinx y el tablero de Caitlyn.
