---
tags: [biblia, serie, laminas]
serie: "Spider-Man: Un nuevo universo / A través del Spider-Verso"
canal: "#edicion"
fecha: 2026-09-24
---

# Biblia · Spider-Verse — para #edicion

> [!important] Cómo se hizo, y sus límites
> - **Segunda pasada (24-sep-2026), con la red abierta.** Un equipo de 4
>   investigadores (imagen, vídeo, voz, texto) y un redactor. Ya se pudo
>   usar: la API de Fandom (`spiderverse` e `intothespiderverse`) y la de
>   **Doblaje Wiki**, `investigar_serie.py` (**9 hojas de contacto**, 3 en
>   `hojas/`), **Dailymotion** e **Internet Archive** con `fotogramas.py`
>   (11 clips y un archivo de *storyboards* mirados de verdad), `estilo.py` (hex **medidos**), `voz.py`
>   (5 muestras del doblaje latino oídas y transcritas), las API de
>   Sketchfab y Wallhaven, y fuentes en japonés (CGWORLD, Fan's Voice,
>   Bandai, TOHO). **YouTube siguió pidiendo iniciar sesión** y TV Tropes
>   y The Cutting Room Floor dieron 403. Lo que cambió va justo debajo,
>   en «Segunda pasada · qué cambió».
> - **Primera pasada** (lo que sigue en este recuadro): la red de esta
>   sesión estaba cerrada. Fandom (la wiki `spiderverse` y
>   Doblaje Wiki), Wikipedia, YouTube, Reddit, la web de Sony, Sketchfab,
>   Poly Haven, ambientCG, dafont, Fonts In Use, Cartoon Brew, AWN,
>   befores & afters, Infobae, Disney Latino y Deadline daban **bloqueo**
>   por curl o por WebFetch. Por eso **no se pudo correr**
>   `herramientas/investigar_serie.py`: **no hay hojas de contacto** ni
>   carpeta `hojas/`. Todas las imágenes van **como enlace**.
> - Hice **50 búsquedas web** en español, inglés, japonés, chino y
>   coreano (la lista está al final, en la bitácora).
> - GitHub sí respondía. De ahí saqué lo más útil de todo el trabajo:
>   **los subtítulos en inglés de las dos películas, con sus tiempos**:
>   - *Un nuevo universo* (2018):
>     [Bisbilge/subtitles](https://github.com/Bisbilge/subtitles), archivo
>     `Spider-Man: Into the Spider-Verse.en.srt` (de *explosiveskull*).
>   - *A través del Spider-Verso* (2023):
>     [sydney-machine-learning/sentimentanalysis-Hollywood](https://github.com/sydney-machine-learning/sentimentanalysis-Hollywood),
>     archivo `data/2023/Spider-Man Across the Spider-Verse.srt`.
>
>   Con ellos doy el **minuto de cada escena**. Es el minuto de ese
>   archivo: en Netflix, Max o el Blu-ray puede moverse un minuto o dos.
>   Los dos archivos empiezan a hablar en el minuto 1:18, después de los
>   logos, así que cuadran con la película completa.
> - También bajé de [google/fonts](https://github.com/google/fonts) las
>   letras propuestas y comprobé una a una, con fontTools, si traen
>   á é í ó ú ñ ¿ ¡ ü.
> - **Cómo nombro las películas**: **UNU** = *Spider-Man: Un nuevo
>   universo* (*Into the Spider-Verse*, 2018). **ATSV** = *Spider-Man: A
>   través del Spider-Verso* (*Across the Spider-Verse*, 2023). El minuto
>   va así: UNU 00:11:59.
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su minuto.
>   ⚠️ **dudoso**: una sola fuente, o lo describo de memoria. Lo de
>   memoria siempre va marcado.
> - Las frases que cito del subtítulo están **en inglés original**. La
>   versión en español que pongo al lado es **traducción mía**, salvo que
>   diga «doblaje latino ✅».

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección **EL TALLER**):

> **ıı・🎞️・edicion** (foro) · 2 hilos · etiquetas: Duda, Resuelto,
> Montaje, Subtítulos, Miniatura, Portada, Efectos, Diseño, Proceso,
> Truco que funciona — _Vídeo y arte, en modo galería: un hilo por cosa.
> Montaje, subtítulos, miniaturas, portadas y diseño. Lo terminado se
> enseña en galería; aquí_
>
> - 📌 De qué va esto (0 msj) · adj: `edicion.png` ← **esta lámina**
> - EJEMPLO · Los subtítulos me tapan la cara del personaje (0 msj)

Función según el encargo: **foro de edición** (duda, montaje, subtítulos,
miniatura…).

> [!warning] La descripción del canal está cortada
> El inventario termina en «Lo terminado se enseña en galería; **aquí**_».
> Falta el final. Tampoco hay en el inventario un canal que se llame
> «galería» (lo busqué con grep: la palabra sólo sale aquí). Puede ser
> que «galería» sea el **modo galería del foro** de Discord, o un canal
> que todavía no existe. **No invento el final.** Abajo propongo una
> frase y la marco para que el dueño la confirme.

### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Edición** | nombre del canal |
| 2 | **Vídeo y arte** | para qué es |
| 3 | **Un hilo por cosa** | la regla |
| 4 | **Montaje** | bloque 1 |
| 5 | **Subtítulos** | bloque 2 |
| 6 | **Miniaturas** | bloque 3 |
| 7 | **Portadas** | bloque 4 |
| 8 | **Diseño** | bloque 5 |
| 9 | **Lo terminado se enseña en galería** | a dónde va lo acabado |
| 10 | **Aquí, el proceso y las dudas** ⚠️ | propuesta para el final cortado |
| 11 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

### Los textos de la lámina 2 (las 10 etiquetas)

Diez etiquetas **no caben** bien en la lámina 1 junto a los cinco
bloques. Propongo **lámina 2**, y cada etiqueta con **un recurso real de
las películas** (así la lámina 2 también enseña la serie):

| Etiqueta | Qué pongo al lado | Recurso de la película que la representa |
|---|---|---|
| **Duda** | Pregunta lo que sea | la **caja amarilla** de los pensamientos de Miles: «Why is the voice in my head so loud?» (UNU 00:14:22) |
| **Resuelto** | Márcalo cuando esté | una **pegatina** «HELLO my name is» de Miles pegada encima (UNU 00:04:18 y 01:44:20) |
| **Montaje** | Cortes, ritmo, orden | el **resumen «hagámoslo una última vez»** que cada araña repite (UNU 00:01:18, 00:35:39, 00:55:04, 01:43:51) |
| **Subtítulos** | Tiempos, estilo, que no tapen | la **cartela de Tierra** que dice dónde estamos («Earth-50101», ATSV 01:02:30) ⚠️ |
| **Miniatura** | La imagen del vídeo | una **portada de cómic en pequeño**, como las viñetas de origen de cada araña (UNU 01:02:25) |
| **Portada** | Discos, libros, carteles | la **portada** con su sello y su número, como un cómic de verdad |
| **Efectos** | Glitch, color, transiciones | el **glitch** de las arañas fuera de su mundo (ATSV 00:09:29: «You're glitching, huh?») |
| **Diseño** | Logos, carteles, tipografía | el **collage punk** de Hobie (letras recortadas, fotocopia) |
| **Proceso** | Enseña cómo lo hiciste | el **grafiti con el tío Aaron**: «Makin' mistakes is part of it» (UNU 00:11:59) |
| **Truco que funciona** | Comparte lo que te sirvió | la **lección de Peter B.**: «Thwip and release» (UNU 00:53:43) |

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué el Spider-Verse encaja con #edicion | Son **las películas más «editadas» de la animación**. Cada mundo tiene su técnica: **puntos Ben-Day**, **desfase de impresión** en vez de desenfoque, **animación a doses**, **acuarela** en el mundo de Gwen, **collage de fanzine** en el de Hobie (con **distintos fotogramas por segundo en cada parte de su cuerpo**) ✅. Y la historia premia al que crea: **Miles pinta grafiti** y hace **pegatinas**, y un **chico de 14 años que rehízo el tráiler en LEGO con Blender** acabó animando una escena de ATSV ✅. |
| Cuadro de diálogo propio | Las **cajas de texto amarillas** con los pensamientos de Miles ✅. Regla del equipo: **ni una caja ni recurso de cómic hasta que la araña muerde a Miles** ✅ (ver §7). Además: onomatopeyas («THWIP»), **cartelas** que dicen en qué Tierra estamos, y el **glitch** cuando alguien está fuera de su mundo. |
| Objeto para la lámina | **Tres propuestas** (§19): la **pared de grafiti del túnel** con las pegatinas de Miles; el **cuarto de Miles** con sus dibujos y una página de cómic impresa con desfase; y el **fanzine punk de Hobie**. Todo se puede hacer en Blender. |
| El más querido | **No hay encuesta oficial** (Sony no las hace). En la de IMDb de pósters de personaje ganó **Gwen**, Miles 2.º, Hobie 6.º ✅. En la de Looper sobre la mejor historia ganó **Miles (51 %)**, Gwen 22 %, Miguel 5 % ✅. **Hobie** es el favorito de las redes: la cuenta oficial le dedicó un TikTok ✅. **Miguel** es el rey de los memes («evento canónico») ✅. |
| Letras | **Bangers** (cómic, onomatopeyas), **Anton** o **Saira Extra Condensed** (títulos altos como el logo), **Comic Neue** (cajas), **Rubik Spray Paint** / **Sedgwick Ave Display** (grafiti de Miles), **Special Elite** + letras recortadas (Hobie), **Rubik Glitch** (glitch), **Orbitron** (2099). **Todas** traen tildes, ñ, ¿ y ¡: comprobado en el archivo. |
| Voz latina | Miles **Emilio Treviño** ✅, Gwen **Alondra Hidalgo** ✅, Peter B. **Miguel Ángel Ruiz** ✅, Miguel O'Hara **José Luis Rivera** ✅ (el mismo en las dos películas), Hobie **Óscar Garibay** ✅, Spider-Ham **Óscar Flores** ✅, la Mancha **Javier Ibarreche** ✅. **Director de las dos: Gerardo García** ✅; estudio **New Art Dub** (UNU) y **VSI Mexico City** (ATSV) ✅ (§10, segunda pasada). |
| Tono | Juvenil, urbano, **con mucho color y mucho ruido gráfico**, pero con **sombras duras** y noches (Brooklyn, túneles). Nada de dibujo «limpio» de Disney ni de 3D brillante de plástico. |
| Juegos de la franquicia | No hay juego propio de las películas. Sí **trajes**: el traje «Un nuevo universo» en *Marvel's Spider-Man: Miles Morales* se mueve **a doses** ✅; hay trajes de ATSV en *Marvel's Spider-Man 2* ✅ y **aspectos en Fortnite** (Miles y Miguel, 23-may-2023; Spider-Gwen, 2022) ✅. Miles jugable en *LEGO Marvel Super Heroes 2*; cartas en *Marvel Snap* y luchadores en *Contest of Champions* ✅ (§13). |
| Lo que viene | *Spider-Man: Beyond the Spider-Verse*, **25 de junio de 2027** ✅ (Hollywood Reporter y Variety AU; antes «4 o 18 de junio», ya corregido; §Punto 25). |

---

## 2 · Las escenas que sirven para #edicion (con minuto)

Todas salen de los subtítulos (ver arriba). Son las que hablan **de crear,
de editar, de equivocarse y de tener tu propio estilo**.

### 2.1 El túnel del grafiti con el tío Aaron (UNU 00:10:42 a 00:13:07) ✅

La escena más útil para el canal. Aaron lleva a Miles a una **estación de
metro abandonada** llena de grafitis viejos. Miles pinta su pieza.

| Minuto | Quién | Línea (original) | En español (mía) |
|---|---|---|---|
| 00:10:42 | Aaron | «You throw these up yet?» (le ve las pegatinas) | «¿Ya las pegaste?» |
| 00:10:56 | Aaron | «Tell him your art teacher made you.» | «Dile a tu papá que te lo mandó tu profe de arte.» |
| 00:11:32 | Aaron | «There's a lot of history on these walls.» | «Estas paredes tienen mucha historia.» |
| 00:11:37 | Miles | «This is so fresh.» | «Esto está buenísimo.» |
| 00:11:50 | Aaron | «Whoa, slow down a little. That's better.» | «Más despacio. Así.» |
| **00:11:59** | Aaron | **«See what you got now? Makin' mistakes is part of it.»** | **«¿Ves? Equivocarse es parte de esto.»** |
| 00:12:08 | Aaron | «The real Miles comin' outta hidin'.» | «Ahí sale el Miles de verdad.» |
| 00:12:13 | Aaron | «Now you can cut that line with another color.» | «Ahora corta esa línea con otro color.» |
| 00:12:29 | Aaron | «Did you want drips? … you gotta keep it moving.» | «¿Querías chorreones? Si no, no te pares.» |
| 00:12:33 | Miles | **«That's intentional.»** | **«Es a propósito.»** |
| 00:12:41 | Miles | «Is it too crazy?» | «¿Está muy loco?» |

**Para qué sirve**: es, palabra por palabra, **un consejo de edición**:
equivócate, corta con otro color, no te pares, y si algo «falla», di que
es a propósito. La etiqueta **Proceso** sale de aquí.

### 2.2 Las cajas amarillas: los pensamientos de Miles (UNU 00:14:07 a 00:16:40) ✅

- 00:14:22 — primera caja: **«Wait. Why is the voice in my head so
  loud?»** («Un momento. ¿Por qué la voz de mi cabeza suena tan fuerte?»).
  Es justo después de la picadura: la regla del equipo es que **antes de
  eso no hay cajas** (§7).
- 00:15:10 — «Why is this so scary?» / 00:15:13 «Am I doing this in slow
  motion or does it just feel that way?» (con Gwen, «Wanda»).
- **00:16:14 a 00:16:40** — el pasillo del colegio: las cajas **se
  multiplican** y le tapan la vista: «Everyone knows», «He knows. She
  knows. They know», «Can they hear my thoughts?!», **«Why are all my
  thoughts so loud?!»**. Es el mejor ejemplo de **muchas cajas a la vez**,
  útil si la lámina tiene que decir mucho.
- 00:18:11 — en su cuarto, Miles **lee en voz alta** sus pensamientos
  entre comillas («"Why is this happening?" "Please stop sticking."»):
  el texto de la caja se vuelve voz.

**Para qué sirve**: la etiqueta **Duda** y el hilo de ejemplo «Los
subtítulos me tapan la cara del personaje» — en el pasillo, **las cajas
tapan literalmente a Miles**. Chiste que un fan pilla.

### 2.3 El resumen que todos repiten: «hagámoslo una última vez» ✅

Es la **plantilla de montaje** de la saga. Cada araña se presenta igual:
nombre, picadura, «ya sabes el resto», y un **resumen rapidísimo** de su
vida con viñetas. Es literalmente un **montaje**.

| Minuto | Quién | Arranque |
|---|---|---|
| UNU 00:01:18 | Peter Parker (rubio) | «All right, let's do this one last time. My name is Peter Parker.» |
| UNU 00:35:39 | Peter B. Parker | «All right, people, let's do this one last time. My name is Peter B. Parker.» |
| UNU 00:55:04 | Gwen | «All right, people. Let's start at the beginning one last time. My name is Gwen Stacy.» |
| UNU 01:02:25 | Noir, Peni, Spider-Ham | tres a la vez: «My name is Peter Parker. / Peni Parker. / Peter Porker.» |
| UNU 01:43:51 | Miles | «Okay, let's do this one last time, yeah? For real this time.» |
| UNU 01:56:04 | Miguel O'Hara | «Let's start at the beginning one last time. Earth-67.» (escena poscréditos) |
| ATSV 00:01:19 | Gwen | «Let's do things differently this time. Like, so differently.» (rompe la plantilla) |
| ATSV 00:11:13 | Miguel | «My name is Miguel O'Hara.» (se corta: «Actually, forget it.») |
| ATSV 00:23:23 | Miles | «Okay, let's do this one last time. My name is Miles Morales… for the last year and four months, I've been Brooklyn's one and only Spider-Man.» Dentro, a las 00:23:54: «**I designed my new suit** with some fly ambience down the side.» |
| ATSV 01:10:28 | Hobie | «A'ight, my name's Hobie, Hobie Brown. I was bitten by a— Wouldn't you like to know?» (se niega a hacerla) |
| ATSV 01:21:49 | Miguel | «My name is Miguel O'Hara. I'm this dimension's one and only Spider-Man.» |

**Para qué sirve**: la etiqueta **Montaje**. Y un texto de lámina con la
voz de la saga: «Hagámoslo una última vez» ⚠️ (frase original; su forma
exacta en el doblaje latino no la pude comprobar).

### 2.4 El arte y el «esto no es arte» (ATSV) ✅

- **00:09:31 a 00:10:09** — Gwen contra el Buitre del Renacimiento, en
  el **Guggenheim**:
  - Buitre: «I am an artist, an engineer.» Gwen: «Oh, great. A
    Renaissance man.»
  - Gwen: «Maybe you could stop making a mess of the art museum?»
  - Buitre: «**You call this art?**» Gwen: «**We're talking about it,
    aren't we?** … It's more of a meta commentary on what we call art,
    **but it's also art.**»
  - Chiste perfecto para un canal de edición y arte.
- **00:27:11 a 00:27:23** — la profesora de arte de Miles: «**Every
  person is a universe.** And my job is to capture your person's universe
  on this piece of paper.» Miles: «That's blank.» — «Exactly.»
- **00:28:00** — en la reunión del colegio: Miles saca **A en «AP Studio
  Art»** (arte), y su papá: «He takes after his uncle.»
- **00:46:38** — Gwen en el cuarto de Miles: «**Are these your drawings?
  They're good.**» Miles: «Hey. What? No.» — «Wow, there's so many.» El
  cuarto está **empapelado de dibujos suyos** (base del concepto B).
- **01:10:38** — Hobie: «…staging **unpermitted political actions slash
  performance-art pieces**».

### 2.5 Lyla y la red de eventos canónicos: una línea de tiempo (ATSV 01:26:34 a 01:28:51) ✅

Miguel: «LYLA, do the thing.» Lyla: «What thing?» Miguel: «**The
information-explainy thing.**» Y sale un holograma con **todas las vidas
de las arañas como hilos**, y **nodos** donde coinciden: «They are the
canon. **Chapters** that are a part of every Spider's story every time.»

**Para qué sirve**: se parece mucho a **una línea de tiempo de un
programa de edición** (hilos = pistas, nodos = cortes). Lo dejo como
**idea secundaria**, porque al dueño **no le convencen los paneles de
interfaz sueltos** (regla 1). Si se usa, que sea **proyectado sobre algo
real** (la sala de la Spider-Society, con Miguel delante).

### 2.6 Hacer tu propio traje, y tu propia banda ✅

- **UNU 01:21:35 a 01:23:55** — tras la charla de su papá por la puerta
  («I see this spark in you… But it's yours.», 01:21:09), casi un minuto
  y medio **sin diálogo**: Miles se va a casa de la tía May y **pinta con
  espray su propio traje** ⚠️ (el minuto exacto del espray lo deduzco del
  hueco del subtítulo; el traje negro con la araña roja pintada es de
  memoria). Suena «What's Up Danger» (01:22:56). «Made 'em myself. They
  fit perfectly.» (01:23:53).
- **UNU 01:23:23** — «When do I know I'm Spider-Man?» «You won't.» «**A
  leap of faith.**» Y el **salto de fe**: Miles cae **boca abajo** hacia
  la ciudad ✅. **Visto en vídeo** (segunda pasada): el plano está
  invertido de verdad; cae con las **piernas juntas, en silueta roja plana
  sobre negro**, y abre los brazos después ✅
  ([clip «Leap of Faith», 0:10](https://www.dailymotion.com/video/x6yq9yg?t=10); ver §2.8).
- **ATSV 01:44:31** — Miles: «**Everyone keeps telling me how my story is
  supposed to go. Nah. I'm gonna do my own thing.**» («Todos me dicen cómo
  tiene que ir mi historia. No. Voy a hacer lo mío.»).
- **ATSV 02:12:44** — Gwen: «**I never found the right band to join. So I
  started my own.**» («Nunca encontré la banda correcta. Así que armé la
  mía.»). Es el final: junta a Peter B., Hobie, Pavitr, Peni, Noir, Ham…
  para ir a por Miles.

### 2.7 Un fan que editó su camino hasta la película ✅

**Preston Mutanga**, de Toronto, **14 años**, rehízo el tráiler de ATSV
plano a plano **en estilo LEGO con Blender**, aprendido en tutoriales de
YouTube. Phil Lord y Chris Miller lo llamaron y **animó la escena LEGO
de la película** (cuando la Mancha salta entre universos). Trabajó unos
tres meses, desde febrero de 2023, por las tardes y los fines de semana.
Chris Miller: «This looks incredibly sophisticated for a nonadult,
nonprofessional to have made». Fuentes:
[TheWrap](https://www.thewrap.com/across-the-spider-verse-lego/),
[CBC](https://www.cbc.ca/news/entertainment/preston-mutanga-spiderverse-interview-1.6884005),
[Variety](https://variety.com/2023/film/news/spider-man-across-the-spider-verse-hired-14-year-old-animator-preston-mutanga-toronto-1235637160/).

**Para qué sirve**: es la historia perfecta para un canal de edición de
un servidor de aficionados. Puede ir en el mensaje fijado, no en la
lámina.

### 2.8 Mirado en vídeo de verdad (segunda pasada) ✅

YouTube pedía iniciar sesión. Se miraron **clips oficiales en
Dailymotion** y un archivo de **Internet Archive** con `fotogramas.py`, y
se midió el color con `estilo.py`. El minuto es **del clip**, no de la
película.

| Escena | Clip y minuto | Lo que se ve de verdad |
|---|---|---|
| **Salto de fe** (UNU) | [«Leap of Faith», 0:05-0:35](https://www.dailymotion.com/video/x6yq9yg?t=10) | Miles en el borde con capucha (0:05); cae boca abajo, **piernas en rojo plano** sobre casi negro (0:10: `#3E0005` 52 %, `#5A0008` 23 %, `#E30014` 7 %); luego picado nocturno en azul muy oscuro ([0:35](https://www.dailymotion.com/video/x6yq9yg?t=35): `#020210`, `#0B143A`) |
| **Torre del reloj** (ATSV, película 00:49:31) | [«Hanging With Gwen», 0:09-0:48](https://www.dailymotion.com/video/x8l73q0?t=9) | Gwen **de pie boca abajo contra la pared** del reloj, capucha colgando; Miles **sentado normal** a su lado. Cierra con **los dos sentados de espaldas** ante la ciudad ([0:48](https://www.dailymotion.com/video/x8l73q0?t=48)), casi el póster. Cielo **violeta y azul lavanda**, no naranja (§5.3) |
| **Pelea final con Kingpin** (UNU), nueva | [«Get Up, Spider-Man», 2:36](https://www.dailymotion.com/video/x87pqho) | Miles solo en un **pasillo rojo** (primeros 30 s); golpes marcados con **manchas de tinta azul cian sobre blanco**, como acuarela ([0:55-1:50](https://www.dailymotion.com/video/x87pqho?t=55)); explosión naranja y dorada (2:00). La paleta cambia con la emoción: rojo → azul → fuego |
| **Persecución en la Spider-Society** (ATSV), nueva | [«Stop Spider-Man!», 0:50](https://www.dailymotion.com/video/x8le5bg?t=8) | Decenas de variantes en la **sala amarilla triangular**, vista por dentro y en movimiento; acaba con Miles **estrellándose en el salón de Peter B.** (0:44) |
| **Boceto → plano final** (ATSV), nueva | [storyboards, Internet Archive](https://archive.org/details/fz-kuox-0a-yaa-7-hm-7_202405) | Lado a lado, el **storyboard a lápiz** y el fotograma terminado: Miles asustado entre **líneas triangulares de neón** naranja, verde, turquesa y magenta ([imagen 2550×2564](https://archive.org/download/fz-kuox-0a-yaa-7-hm-7_202405/FzKUOX0aYAA7Hm7.jfif)). El crédito en pantalla es «Entertainment Access» (repost de prensa) ⚠️ |
| **Título de UNU con glitch** | [tráiler UNU, 2:12](https://www.dailymotion.com/video/x942l02?t=132) | Letras negras con **halo cian y magenta desplazado**: el desfase de impresión que propone el encargo ya existe en la saga (`#8E0126`, `#B00137`, `#644581`) |
| **Glitch de Gwen** (ATSV) | [tráiler ATSV, 2:06](https://www.dailymotion.com/video/x8gaz41?t=126) | Primer plano deformado en **amarillo, magenta y cian** casi puros (`#D3AE17`, `#BC1B22`, `#3BC7DB`): la paleta CMYK de imprenta sin el negro |

**Para #edicion**: el boceto → plano final es el «de la idea al resultado»
del canal; el título con desfase es el efecto exacto del objeto propuesto.

**Sigue sin verse en vídeo**: el Guggenheim (los dos clips de Dailymotion,
`x8l68ns` y `x8l7ilg`, daban 404) y el túnel del grafiti. Su minuto sigue
siendo el del subtítulo ✅.

---

## 3 · Arte oficial y referencias visuales

> [!note] Segunda pasada: ya hay imágenes medidas
> En la primera pasada no se pudo bajar nada. Ahora hay **9 hojas de
> contacto** (383 imágenes de la wiki, con tamaño por la API) y **3 en
> `hojas/`** (ver §3.6). Guardar las que sirvan en
> `herramientas/laminas_v2/v3/referencias/spider-verse/`.

### 3.1 Pósters de personaje de ATSV (mayo de 2023) ✅

Sony sacó **un póster por araña**: Miles, Gwen, Peter B., Miguel, Jessica
Drew, Pavitr (Spider-Man India), **Hobie**, Ben Reilly (Scarlet Spider),
Spider-Cat y la Mancha. Cada uno lleva **el arte del mundo de ese
personaje** (Hobie en collage, Gwen en acuarela…), así que son la mejor
referencia de **estilo por personaje**. Fuentes que los recogen:
[AWN](https://www.awn.com/news/character-posters-released-spider-man-across-spider-verse),
[MovieWeb](https://movieweb.com/spider-man-across-the-spider-verse-character-posters/),
[SuperHeroHype](https://www.superherohype.com/movies/534944-spider-man-across-the-spider-verse-character-posters-show-lots-of-spider-people),
[GeekTyrant](https://geektyrant.com/news/character-posters-for-spider-man-across-the-spider-verse-introduces-the-spider-society),
[ComingSoon](https://www.comingsoon.net/movies/news/1290555-spider-man-across-the-spider-verse-character-posters-give-a-closer-look-at-the-movies-villain).
En alta suelen estar en IMP Awards (bloqueado desde aquí).

### 3.2 Arte de producción (del equipo, no de fans)

| Qué | Dónde | Para qué |
|---|---|---|
| Archivo de arte conceptual (Tumblr de fans que recopila arte oficial) | [spiderverseconceptart · Nueva York](https://www.tumblr.com/spiderverseconceptart/tagged/nueva%20york), [arte de objetos de Nueva York](https://spiderverseconceptart.tumblr.com/post/728917913484017664/nuevo-york-concept-artprop-design-for-spider-man), [desarrollo de Nueva York](https://spiderverseconceptart.tumblr.com/post/721678755905536000/nueva-york-development-art-for-spider-man-across) | mundo de Miguel ✅ |
| **Kris Anka**, diseñador de personajes de ATSV (supervisó a Hobie) | [krisanka.com/work/atvs](https://www.krisanka.com/work/atvs) | trajes y hojas de personaje ✅ |
| **Mack Sztaba**, horizonte de Nueva York | [ArtStation](https://www.artstation.com/artwork/8bR9kR) | fondo 2099 ✅ |
| **Jessica Rossier**, arte conceptual de UNU (con Bastien Grivet, bajo el director de arte Alberto Mielgo) | [ArtStation](https://jessica-rossier.artstation.com/projects/XBJX03) | Nueva York de Miles, luz ✅ (una fuente) |
| **@chuwenjie**, *color keys* de la escena de Gwen y su papá | [Tumblr](https://www.tumblr.com/chuwenjie/720485703016923136/i-painted-these-color-keys-for-this-scene-in) | paleta de Tierra-65 ✅ (una fuente) |
| Reseña del libro de *visdev* de ATSV | [Halcyon Realms](https://halcyonrealms.com/animation/the-visdev-art-of-spider-man-across-the-spider-verse/) | ver páginas del libro ⚠️ |
| Hilo oficial **#CreatingTheSpiderVerse** sobre Tierra-65 | [X @SpiderVerse](https://x.com/SpiderVerse/status/1727044559665004549) y [TikTok @sonypicturesanimation](https://www.tiktok.com/@sonypicturesanimation/video/7304356340539968811) | acuarela y «anillo del humor» ✅ |

### 3.3 Libros de arte (existen, no los pude hojear) ✅

- *Spider-Man: Into the Spider-Verse — The Art of the Movie*, Ramin
  Zahed ([Penguin Random House](https://www.penguinrandomhouse.com/books/605851/spider-man-into-the-spider-verse--the-art-of-the-movie-by-ramin-zahed/)).
- *Spider-Man: Across the Spider-Verse — The Art of the Movie*, Ramin
  Zahed, Abrams, **224 páginas**, 3 de julio de 2023, ISBN
  9781419763991 ([Bookshop](https://bookshop.org/p/books/spider-man-across-the-spider-verse-the-art-of-the-movie-ramin-zahed/19794761),
  [Goodreads](https://www.goodreads.com/book/show/110740538-spider-man)).
  Trae arte conceptual, bocetos, diseños y *storyboards*, y entrevistas
  a Lord y Miller.

### 3.4 La secuencia de logos del principio (UNU) ✅

El logo de Columbia **se rompe en glitch** y pasa por versiones viejas de
la «dama de Columbia» (1924, 1928, 1936, 1976…), con **fragmentos de
neón, líneas de movimiento, chispas y puntos Ben-Day**. La hizo
**Devastudios**: [su página](https://devastudios.com/work/titles/spider-man-into-the-spider-verse/),
[Cartoon Research](https://cartoonresearch.com/index.php/the-trippy-columbia-logo-art-in-spider-man-into-the-spiderverse/),
[Art of the Title](https://www.artofthetitle.com/title/spider-man-into-the-spider-verse/).
Vídeo: [logos en 4K](https://www.youtube.com/watch?v=MV2Xutd3BM8).
**Para qué sirve**: es la referencia exacta del **glitch** para la
etiqueta **Efectos**.

### 3.5 Lo que falta ⚠️

- ~~No pude ver ni una imagen en grande. No hay hojas de contacto.~~ →
  **Resuelto** en la segunda pasada: 9 hojas miradas (§3.6).
- Hojas de modelo: ya hay **turnarounds** oficiales de Gwen y de Hobie
  (§3.6). Siguen sin aparecer las de **Miles** y **Miguel** ⚠️.
- No encontré **portadas de Blu-ray** con tamaño ⚠️.
- El libro *The Art of the Movie* (ATSV) existe, pero **no se pudo hojear
  por dentro** ⚠️.

### 3.6 Arte de producción en la wiki y las hojas de contacto (segunda pasada) ✅

**Arte del equipo** (con autor y fecha en la propia imagen, no fan art):

| Qué | Autor | Tamaño | Para qué |
|---|---|---|---|
| [Turnaround del traje de Gwen](https://static.wikia.nocookie.net/intothespiderverse/images/5/57/SpiderGwen_ATSV_Concept_Art_by_Kristafer_Anka_2.jpg), «WAM / CHARACTER DESIGN / GWEN / v101», 15-09-2020, 3 variantes de máscara y logo | **Kris Anka** | 2048×1326 | silueta y hex del traje ✅ |
| [Ropa de calle de Gwen, 8 variantes](https://static.wikia.nocookie.net/intothespiderverse/images/2/2c/GwenOutfitsJes%C3%BAsAlonsoIglesias.jpg) (top rojo «PUNK», impermeable turquesa «ROCK'N'ROLL», blusa rosa, top mostaza con espiral) | **Jesús Alonso Iglesias** | 2048×1018 | Gwen de civil ✅ |
| [Moodboard «BLACK PUNKS»](https://static.wikia.nocookie.net/intothespiderverse/images/c/ca/Spider_Punk_ATSV_moodboard_by_Evening_Monteiro.jpg): fotos reales de la escena punk negra de Londres y Nueva York | **Evening Monteiro** | 4096×1935 | Hobie no es «punk genérico» ✅ |
| [Estudios de la chaqueta de Hobie](https://static.wikia.nocookie.net/intothespiderverse/images/8/8a/Spider_Punk_ATSV_by_Jake_Panian_3.jpg), parches y bajo; vista de espalda | **Jake Panian** | 1440×1440 | textura de la chaqueta ✅ |
| [Turnaround de personaje](https://static.wikia.nocookie.net/intothespiderverse/images/7/75/Gwen_Stacy_%28Earth-65%29_AtSV_character_design_7_by_Lena_Sayaphoum.jpg) (serie de 3) | **Lena Sayaphoum** | 1600×1135 | pose ⚠️ (un solo crédito) |
| [Ficha de Peter B.](https://static.wikia.nocookie.net/intothespiderverse/images/4/41/Peterbparkeratsv.jpg) `Peterbparkeratsv.jpg` y 53 imágenes grandes más | wiki | 3840×1600 | Peter B., antes en blanco ✅ |

**Peter B. en la wiki**: la página se llama **`Peter Parker (Earth-616)`**
(«Peter B. Parker» es una redirección) ✅. Por eso el recolector no la
encontraba.

**Las 3 hojas de `hojas/`** (miradas; el número es la casilla amarilla):

1. **`personajes_01.jpg`** (hoja 1 del juego principal, 2400×1704,
   0,6 MB). Sustituye a `colaboraciones_01.jpg`, que tenía menos uso
   para la lámina.
   - **1**: póster de Hobie en collage, «SAVE YOUR DAD» ([4096×2864](https://static.wikia.nocookie.net/intothespiderverse/images/d/d9/HobieBTSV.jpg)). Concepto C.
   - **2-3**: Gwen de civil (5 looks) y estudios de peinado ([4096×2650](https://static.wikia.nocookie.net/intothespiderverse/images/9/97/FyCY0QkaYAEcgXs.jpg)).
   - **4-10**: caras y cuerpo de Hobie a lápiz, de **Evening Monteiro** ([ej. 4096×2048](https://static.wikia.nocookie.net/intothespiderverse/images/5/50/Hobie_Brown_ATSV_by_Evening_Monteiro_1.jpg)). 11: el moodboard.
   - **12**: [selfie de Gwen y Miles](https://static.wikia.nocookie.net/intothespiderverse/images/1/15/Gwenmilesselfie.jpg) (2748×2748). Presentar en pareja.
   - **13, 25**: el Spider-Gang de UNU en grupo ([4200×1760](https://static.wikia.nocookie.net/intothespiderverse/images/3/3f/Spider-Gang.jpg)).
   - **14, 17, 18**: caras de Gwen: ojos y boca muy abiertos ([GwenAwkward](https://static.wikia.nocookie.net/intothespiderverse/images/5/57/GwenAwkward.jpg)), susto en primer plano ([17](https://static.wikia.nocookie.net/intothespiderverse/images/a/a2/GLedZflWQAA_D6F.jpg)) y **agarrándose el pelo** ([GwenHairGrab](https://static.wikia.nocookie.net/intothespiderverse/images/a/ae/GwenHairGrab.jpg)). Todas 3840×1608, **sin minuto** ⚠️.
   - **19**: Gwen en su cuarto, con tablón de fotos ([3840×1608](https://static.wikia.nocookie.net/intothespiderverse/images/9/98/GwenNoFilter.jpg)).
   - **23**: **Miles pintando grafiti** ([Miles tagging, 3840×1608](https://static.wikia.nocookie.net/intothespiderverse/images/a/a4/Miles_tagging_001.png)). **La pose del concepto A.**
   - **40**: Miles y Gwen sentados en el cuarto de Miles ([3840×1606](https://static.wikia.nocookie.net/intothespiderverse/images/2/27/GLerIMiWMAA2XoJ.jpg)). Concepto B.
   - **45**: [Gwen, Miles y Hobie](https://static.wikia.nocookie.net/intothespiderverse/images/5/5c/GwenMilesHobie.jpg) juntos (3840×1606).
2. **`vestuario_01.jpg`** (hoja 4, 2400×1704, 0,7 MB). Casillas
   **133-136**: turnaround de Gwen con capucha puesta y quitada (Kris
   Anka). **147-160**: más de 12 looks de calle de Gwen (Jesús Alonso
   Iglesias). **163-170**: chaqueta, parches y bajo de Hobie (Jake
   Panian). **186**: Funko Pop de Gwen. Para vestuario (§16) y texturas
   (Punto 19).
3. **`peterb_01.jpg`** (hoja propia de Peter B., 2400×1704, 0,6 MB).
   Casillas **1-9**: traje y pose de Spider-Man clásico. **10, 17-48**:
   escenas de familia (el anillo, el beso con MJ, la despedida de Miles,
   la pelea con Olivia Octavius). Pose y ropa de casa (bata, ropa de
   calle desaliñada).

La hoja 7 (la antigua `colaboraciones_01.jpg`) sigue en
`herramientas/referencias/spider-man-into-across-the-spider-verse/hoja_07.jpg`:
casilla **49** skin de Gwen en Fortnite, **297 y 313** Funko Pop (Punto 23).

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Objetos 3D para Blender (Sketchfab)

| Modelo | Autor | Licencia (según el buscador) | Enlace |
|---|---|---|---|
| Spray can graffiti [Low-poly] | smakologg | **CC BY** ✅ | [Sketchfab](https://sketchfab.com/3d-models/spray-can-graffiti-low-poly-by-smakologg-bd4f3e7d509f4fd691d9ee6def794f19) |
| Spray Paint Can | Shara Ritchey (@SharaSchool) | **CC BY** ✅ | [Sketchfab](https://sketchfab.com/3d-models/spray-paint-can-360f6ce433894dc3baaa7e035b617aac) |
| Free Spray Paint Can | navebackwards | **CC BY** ✅ | [Sketchfab](https://sketchfab.com/3d-models/free-spray-paint-can-7b44a71676d841c9a8eb777b2ee55096) |
| 3D, low poly, Graffiti Spray Paint Can Prop | ScottPritchard | ⚠️ la API la da **vacía** (no es CC): sólo mirar | [Sketchfab](https://sketchfab.com/3d-models/3d-low-poly-graffiti-spray-paint-can-prop-efffc9856955496187383760210fefe4) |
| Graffiti on a wall — Low Poly | Léonard_Doye (@leoskateman) | **CC BY** ✅ (API de Sketchfab, segunda pasada) | [Sketchfab](https://sketchfab.com/3d-models/graffiti-on-a-wall-low-poly-fb3d849c6de346079d338251533a84e6) |
| Street Graffiti | Yanez Designs | **CC BY** ✅ (API de Sketchfab, segunda pasada) | [Sketchfab](https://sketchfab.com/3d-models/street-graffiti-d366fa89405640428dff57961efc7886) |

**Crédito exacto para CC BY** (ejemplo): «"Spray can graffiti [Low-poly]"
by smakologg, licensed under CC BY 4.0, sketchfab.com». Comprobar la
versión de la licencia al bajarlo.

### 4.2 Modelos 3D de personajes (sólo para mirar poses) ⚠️

Son de fans. Aunque el que los sube ponga CC BY, **el personaje es de
Marvel y Sony**: sirven para girar la cámara y estudiar una pose, **no
para pegarlos en la lámina**.
[Miles ATSV, CVRxEarth](https://sketchfab.com/3d-models/miles-from-spider-man-across-the-spider-verse-6585b5cd701d4b11a66618e20b7c8df7) ·
[Miles ATSV, CVRxEarth (otro)](https://sketchfab.com/3d-models/miles-morales-across-the-spider-verse-e07f49a8eb2e45adb0946d8c243a17ad) ·
[Miles UNU, GekWyd](https://sketchfab.com/3d-models/miles-morales-spider-man-into-the-spider-verse-3360b9eca35c49dbb7722d17b257b745) ·
[Miles UNU, elvinguhl](https://sketchfab.com/3d-models/miles-morales-into-the-spider-verse-88d2b738503d4af981f4f6b9fc9ddbab).
En ArtStation, **Jose David Cruz** hizo un Hobie en 3D:
[enlace](https://www.artstation.com/artwork/8Bm9JE).

**Segunda pasada** (API de Sketchfab, licencia **CC Attribution** en la
respuesta ✅; mismo aviso: sólo para mirar poses):
[Spider Punk, CVRxEarth](https://sketchfab.com/3d-models/none-31b9e56833d34121a9a0012985c6bc09) ·
[Miguel O'Hara, CVRxEarth](https://sketchfab.com/3d-models/none-ea60ca0885574fa8a6d85046dd884a60) ·
[The Spot, CVRxEarth](https://sketchfab.com/3d-models/none-f07168481ba047969512fa9c075d1181) ·
[Spider-Gwen ATSV, Kabiidev](https://sketchfab.com/3d-models/none-297c91b697f7428ea634ab454a598219) ·
[Pavitr Prabhakar, Kabiidev](https://sketchfab.com/3d-models/none-4c4dab68017c488596bdd39e8eaf383a) ·
[Gwen «Across Spider Verse», Artcon_3d](https://sketchfab.com/3d-models/none-9555d75d3d074dac84b4d705fc1d15b8) ·
[Miles, Gwen e ITSV en grupo](https://sketchfab.com/3d-models/none-beaf3ab63026425fb8aa9d1a2187e476).
**Rig libre** de Miles, Gwen o Hobie con licencia clara: **no lo
encontré** ⚠️ (Sketchfab y GitHub; ver Punto 18).

### 4.3 Fan art 2D (mirar, nunca pegar)

| Obra | Autor | Enlace |
|---|---|---|
| Hobie Brown / Spider-Punk | Ivan Shavrin | [ArtStation](https://www.artstation.com/artwork/BXVyml) |
| Spider Fanarts (Miles, Gwen, Hobie) | Conor Burke | [ArtStation](https://www.artstation.com/artwork/rJ0GvE) |
| Across the Spider-Verse Fanart | John Patrick Gañas | [ArtStation](https://www.artstation.com/artwork/qeZD4D) |
| Miles Morales (sudadera y Jordan) | Yann Lavrand | [ArtStation](https://yannlavrand.artstation.com/projects/aRONzL) |
| Miles Morales | Yashar Kassai | [ArtStation](https://www.artstation.com/artwork/8lvnOR) |
| Miles Morales (escultura) | Yan Sculpts | [ArtStation](https://yansculpts.artstation.com/projects/JlrNNR) |
| Hobie Brown, ilustración (sobre el concepto temprano de **Jesús Alonso Iglesias**) | ⚠️ autor no visto | [ArtStation](https://www.artstation.com/artwork/kQewnz) |
| Miles y Gwen, 4782×2097 | 林霰 (Lin Xian) | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1319119) |

### 4.4 Código: cómo se imita el estilo (GitHub) ✅

| Repositorio | Qué hace | Licencia |
|---|---|---|
| [aniketrajnish/SpiderVersePostProcess-Unreal-Unity](https://github.com/aniketrajnish/SpiderVersePostProcess-Unreal-Unity) | puntos Ben-Day y **rayado** en las sombras, con densidad y dirección ajustables | MIT |
| [nmagarino/Spiderverse-Styled-Rendering](https://github.com/nmagarino/Spiderverse-Styled-Rendering) | sombreado a 5 bandas, **aberración cromática** que crece con la distancia, Ben-Day, contorno, y **desplaza los puntos por canal CMYK** (el desfase de imprenta) | sin licencia (sólo mirar) |
| [smoothslerp/spiderverse-shader](https://github.com/smoothslerp/spiderverse-shader) | estudio de los puntos Ben-Day | MIT |
| [adamb70/Spiderverse-Shader-Unity](https://github.com/adamb70/Spiderverse-Shader-Unity) | trama de puntos (halftone) como efecto de imagen | sin licencia vista |

**En Blender** no encontré un complemento listo. Lo que hacen esos
repositorios se copia en el **compositor** así (propuesta mía ⚠️):
1. **Separar color** en canales.
2. **Mover** cada canal 2 a 4 px en distinta dirección, **más** cuanto
   más lejos esté el objeto (usa el pase de profundidad). Eso es el
   **desfase de impresión** que la película usa **en vez de desenfoque**.
3. **Juntar** otra vez.
4. En las sombras, multiplicar una **textura de puntos** (Ben-Day) o de
   **rayas** (hatching), sólo donde está oscuro.

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

| Sitio | Película y minuto | Cómo es |
|---|---|---|
| **Brooklyn**, la calle de Miles y su casa | UNU 00:03:37 a 00:04:10 (saluda a los vecinos) | barrio de ladrillo, mañana, pegatinas en farolas ✅ (subtítulo) |
| **Brooklyn Visions Academy**, el colegio y el pasillo | UNU 00:06:38 a 00:08:49; pasillo 00:16:14 | colegio moderno, luz de día fría ⚠️ |
| **La estación de metro abandonada** del grafiti | UNU 00:10:56 a 00:13:07 («Did an engineering job down here», 00:11:03) | oscura, paredes llenas de grafiti viejo, luz de linterna y de espray ✅ (subtítulo) / luz ⚠️ |
| **El cuarto de Miles** en casa, con sus dibujos | ATSV 00:46:17 a 00:46:48 | cuarto de adolescente, dibujos por todas partes, juguetes en caja ✅ (subtítulo) |
| **La torre del Williamsburgh Savings Bank** (el reloj) | ATSV 00:49:52 («Who needs a treadmill when you have the Williamsburgh Bank Building?») | la escena **boca abajo** de Miles y Gwen, atardecer ✅ (subtítulo). **Visto en vídeo**: cielo **violeta y azul lavanda**, casi sin naranja ✅ ([clip, 0:09-0:48](https://www.dailymotion.com/video/x8l73q0?t=27)) |
| **Casa de la tía May** y la guarida de Peter debajo | UNU 01:01:30 | sótano con trajes y pantallas ⚠️ |
| **Tierra-65** (Gwen): Nueva York en **acuarela**; el **Guggenheim** | ATSV 00:07:33 y 00:08:33 | el color cambia con el ánimo de Gwen («anillo del humor»); sus primarios son **cian, naranja y violeta** en vez de amarillo, rojo y azul (Dean Gordon, director de arte) ✅ |
| **Tierra-928, Nueva York** (Miguel, año 2099) | ATSV 01:17 a 01:30 (la sede) | futuro **brutalista y retro**, inspirado en **Syd Mead, Ron Cobb y Ralph McQuarrie**; arriba azules limpios, abajo oscuro tipo *Blade Runner* ✅. La ciudad se diseñó como **reflejo de Miguel**: «limpia, fuerte, unificada, de fachada única» ✅ ([SlashFilm](https://www.slashfilm.com/1327386/across-the-spider-verses-nueva-york-took-cues-sci-fis-most-respected-artists)). Medido en una vista aérea nocturna del tráiler: **violeta malva** (`#725780`, `#4C365D`, `#A6879D`), no azul ([tráiler ATSV, 1:06](https://www.dailymotion.com/video/x8gaz41?t=66)) ✅ ([Variety](https://variety.com/2023/artisans/news/spider-verse-pays-homage-to-the-sex-pistols-graphic-artist-syd-mead-and-canadian-hockey-easter-egg-1235638844/), [Popverse](https://www.thepopverse.com/spider-man-verse-spiderverse-universes-worlds-spider-man-marvel)) |
| **Tierra-138** (Hobie, Londres) | ATSV 01:10 (Hobie aparece en Mumbattan, no en su mundo) | como **entrar en un club punk ilegal** y pasar los dedos por **años de carteles** (Sex Pistols, Buzzcocks); fotocopia, collage, «fanzine» ✅. Lo confirma el propio estudio en el featurette **«Designing Spider-Punk»** (Kris Anka, Kemp Powers, Mike Lasker): su estilo se construyó pegando **fotocopias en blanco y negro, periódico y carteles de los Sex Pistols** (paneles rotulados «one black and white», «two newspaper», «three sex pistols», [0:25](https://www.dailymotion.com/video/x8oez5v?t=25)) ✅ ([befores & afters](https://beforesandafters.com/2023/06/17/the-across-the-spider-verse-spider-punk-character-hobie-was-animated-with-different-frame-rates-for-different-parts-of-his-own-body-and-accessories/), [Variety](https://variety.com/2023/artisans/awards/spider-punk-hobie-spider-verse-animators-1235707039/)) |
| **Mumbattan** (Tierra-50101, Pavitr) | ATSV 01:02:30 («Earth-50101») y 01:07:03 | Mumbai + Manhattan, colores saturados ✅ (subtítulo) / colores ⚠️ |

### 5.2 Luz, medida en el «código de barras» de UNU ⚠️

El repositorio [PrayerVoid/color_of_movies](https://github.com/PrayerVoid/color_of_movies)
trae el **código de barras de color** de UNU (1200×500, cada columna es
el color medio de unos 6 segundos) y un JSON con 9 tramos. Lo medí yo.
Son **medias**: salen apagadas, pero dicen **cuánta luz** hay:

| Momento | Color medio | Qué dice |
|---|---|---|
| Túnel del grafiti, 00:11:30 | `#01040B` | casi negro: el túnel está **muy oscuro** |
| Grafiti ya pintado, 00:12:30 | `#38322A` | sube a un **cálido** oscuro (la pieza de colores) |
| Pasillo de las cajas, 00:16:20 | `#7C7576` | **claro**, luz de día |
| Salto de fe, 01:23:45 | `#151421` | noche violácea |
| Final de Miles, 01:44:40 | `#376494` | **azul** limpio de día |
| Poscréditos (Nueva York 2099), 01:56:10 | `#61527C` | violeta |

Media de cada tramo del JSON: 0-13 min `#423E45`, 13-26 `#3D4045`,
68-77 (la revelación) `#221825`, 101-117 (el final) `#514664`.
**Conclusión**: la saga vive **de noche y en interiores oscuros**,
con el color puesto **encima** en luces fuertes. Una lámina clara y
pastel **no** parece Spider-Verse.

### 5.3 Paleta: medida en la segunda pasada ✅ (y lo que sigue de memoria ⚠️)

En la primera pasada no se pudo muestrear. Ahora los hex salen de
`estilo.py` y Pillow sobre **fotogramas reales** (clips de Dailymotion) y
**arte oficial plano** (sin luz de color encima).

| Qué | Hex medido | De dónde |
|---|---|---|
| Traje de Gwen: negro (no puro, tira a marrón) | `#2D2926` | turnaround de Kris Anka ✅ |
| Traje de Gwen: rosa magenta de capucha y brazos | `#E6145A` (grupo `#DC145A`-`#E6145A`) | mismo ✅ (antes `#FF4081` de fans) |
| Zapatillas de Gwen, cian | `#00FAFA` | mismo ✅ (antes `#6ACADF` de fans) |
| Miguel: azul marino del cuerpo | `#304080` | fotograma plano [Spider-Men (E-67) 001](https://static.wikia.nocookie.net/intothespiderverse/images/e/ed/Spider-Men_%28E-67%29_001.png) ✅ (antes `#1B2A5C` de memoria) |
| Miguel: rojo de máscara y guantes | `#E80038` | mismo ✅ (antes `#FF2B2B` de memoria) |
| Araña roja clásica (Peter B.) | `#BF0001` | [asset oficial, 1000×962](https://static.wikia.nocookie.net/intothespiderverse/images/5/52/Spider-Man_symbol_red.webp) ✅ (antes `#D7262E` de memoria) |
| Salto de fe: silueta roja sobre casi negro | `#3E0005` `#5A0008` `#E30014` | [clip, 0:10](https://www.dailymotion.com/video/x6yq9yg?t=10) ✅ |
| Salto de fe: picado nocturno | `#020210` `#0B143A` | [clip, 0:35](https://www.dailymotion.com/video/x6yq9yg?t=35) ✅ |
| Torre del reloj al atardecer | `#3E2D4F` `#AE8DAA` `#724764` `#5A6CA5` `#5E5FAF` `#44426E` | [clip, 0:09-0:48](https://www.dailymotion.com/video/x8l73q0?t=9) ✅ |
| Tierra-928 de noche | `#725780` `#4C365D` `#A6879D` `#D3C3C5` | [tráiler ATSV, 1:06](https://www.dailymotion.com/video/x8gaz41?t=66) ✅ |
| Título de UNU con desfase | `#8E0126` `#B00137` `#500314` `#644581` | [tráiler UNU, 2:12](https://www.dailymotion.com/video/x942l02?t=132) ✅ |
| Glitch (ATSV): amarillo, magenta, cian | `#D3AE17` `#BC1B22` `#3BC7DB` `#D096A5` | [tráiler ATSV, 2:06](https://www.dailymotion.com/video/x8gaz41?t=126) ✅ |
| Magenta y cian del desfase (tintas) | `#E6007E` / `#00AEEF` | estándar de imprenta CMYK ✅ |
| Rojo y negro del traje de **Miles** | `#D7262E` / `#141418` | **de memoria** ⚠️: todos los fotogramas son de noche o con neón encima |
| Traje de **Hobie** | — | **sin medir** ⚠️, por lo mismo |
| Amarillo de las cajas de texto | `#FFE14D` | **de memoria** ⚠️ |
| Violeta de Tierra-65 | `#753FB1` | paleta de fans ⚠️ ([color-hex](https://www.color-hex.com/color-palette/1024127)) |
| Paleta «Miles» de fans | `#79ADFF #0038C6 #FFFFFF #FF0000 #1A1C24` | [color-hex](https://www.color-hex.com/color-palette/1024196), sólo contraste ⚠️ |

**Lo que confirma el vídeo**: ninguno de los fotogramas es luz natural
plana. Todo son **focos de color puro** (rojo, violeta, cian, amarillo)
sobre negro o casi negro. La paleta **cambia con la emoción**: en la
pelea final de UNU va del **pasillo rojo** a las **manchas de tinta azul
cian** y al **fuego naranja** ([clip](https://www.dailymotion.com/video/x87pqho?t=55)).

### 5.4 Texturas reales equivalentes (todas CC0)

| Para qué | Textura | Enlace |
|---|---|---|
| Pared del túnel | Wall Bricks Plaster (8K), Brick Wall 04 (8K) | [Poly Haven](https://polyhaven.com/a/wall_bricks_plaster), [Poly Haven](https://polyhaven.com/a/brick_wall_04) |
| Pared pintada de cuarto | Painted Plaster Wall (16K) | [Poly Haven](https://polyhaven.com/a/painted_plaster_wall) |
| Hormigón | Concrete 010 / 012 / 020 | [ambientCG](https://ambientcg.com/view?id=Concrete010), [012](https://ambientcg.com/view?id=Concrete012), [020](https://ambientcg.com/view?id=Concrete020) |
| Papel del cómic y del fanzine | Paper 001; categoría Paper & Card | [ambientCG](https://ambientcg.com/view?id=Paper001), [Poly Haven](https://polyhaven.com/textures/paper-card) |
| Cartón (cajas, carteles) | Cardboard Set 001 | [ambientCG](https://ambientcg.com/view?id=CardboardSet001) |
| Luz de túnel (HDRI) | Mosaic Tunnel (azulejo azul, fluorescente frío y lámparas cálidas), Concrete Tunnel (lámparas cálidas, sombras duras) | [Poly Haven](https://polyhaven.com/a/mosaic_tunnel), [Poly Haven](https://polyhaven.com/a/concrete_tunnel) |
| Ciudad de noche (HDRI) | categoría Urban > Night | [Poly Haven](https://polyhaven.com/hdris/urban/night) |

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

- **El logo** de *Spider-Verse* es **rotulación a medida**, no una letra
  comercial ✅ ([Font In Logo](https://www.fontinlogo.com/famous-fonts/spider-verse-font),
  [Made Good Designs](https://madegooddesigns.com/spider-verse-font/)).
  En el foro de dafont apuntan a **Proxima Nova Extra Condensed
  ExtraBold** como lo más parecido, con la D y la M distintas ⚠️
  ([dafont](https://www.dafont.com/forum/read/377914/spider-man-into-the-spider-verse-fonts)).
  Hay otro hilo para el título de ATSV
  ([dafont](https://www.dafont.com/forum/read/534828/title-font-in-spider-man-across-the-spider-verse)).
- **Las cajas de texto** y los rótulos de pantalla son **grafismo hecho a
  mano** en movimiento, en **mayúsculas de rotulista de cómic**, gruesas
  y algo irregulares ✅ ([Made Good Designs](https://madegooddesigns.com/spider-verse-font/)).
- **Hobie**: letras **recortadas de revista** tipo nota de rescate, como
  los carteles de los **Sex Pistols** (Jamie Reid) ✅ (titular de
  [Variety](https://variety.com/2023/artisans/news/spider-verse-pays-homage-to-the-sex-pistols-graphic-artist-syd-mead-and-canadian-hockey-easter-egg-1235638844/)
  y [NamuWiki](https://namu.wiki/w/%EC%8A%A4%ED%8C%8C%EC%9D%B4%EB%8D%94%20%ED%8E%91%ED%81%AC)).
- **Miguel / 2099**: en los cómics *Marvel 2099* el número «2099» del
  logo va en **Zephyr / Chariot** (el diseñador quitó el trazo que sube
  del cero y lo puso en cursiva) y el texto en **Eurostile**; los nombres
  de personaje, rotulados a mano ✅ ([Fonts In Use](https://fontsinuse.com/uses/41204/marvel-2099-comic-books),
  abierto en la segunda pasada). Libre parecida a Eurostile: **Michroma**
  (Cyreal, OFL, Google Fonts); **tildes, ñ, ¿ y ¡ sin comprobar** con
  fontTools ⚠️ (usar Orbitron, ya comprobada, si falla).
- **El logo** sigue sin letra comercial identificada ⚠️ (segunda pasada:
  «Spider-Verse font identified», nada nuevo).

### 6.2 Letras libres comprobadas por mí

Bajadas de [google/fonts](https://github.com/google/fonts) y revisadas con
fontTools: **todas traen á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü**.

| Letra | Licencia | Para qué | Nota |
|---|---|---|---|
| **Bangers** (Vernon Adams) | OFL | onomatopeyas, rótulo de cómic | sólo mayúsculas; la que recomienda la guía de cuadros |
| **Comic Neue Bold** (Rozynski, Papazian) | OFL | **texto de las cajas amarillas**, en mayúsculas | se lee bien en pequeño |
| **Anton** (Vernon Adams) | OFL | títulos altos y estrechos, como el logo | |
| **Saira Extra Condensed Black** (Omnibus-Type) | OFL | alternativa al logo (más cerca de Proxima Nova condensada) | |
| **Bebas Neue** / **Staatliches** | OFL | etiquetas cortas, cartelas «Tierra-…» | mayúsculas |
| **Rubik Spray Paint** (NaN, Luke Prowse) | OFL | **grafiti de Miles** hecho con espray | |
| **Sedgwick Ave Display** (Vergani, Burke) | OFL | **firma** de grafiti (tag) | |
| **Permanent Marker** (Font Diner) | Apache 2.0 | lo que Miles escribe a rotulador en las pegatinas | |
| **Special Elite** (Astigmatic) | Apache 2.0 | letra de **máquina de escribir / fotocopia** para el fanzine de Hobie | |
| **Rubik Distressed** / **Rubik Dirt** | OFL | letra gastada para carteles punk | |
| **Rubik Glitch** (NaN, Luke Prowse) | OFL | el **glitch** (etiqueta Efectos) | úsala poco |
| **Orbitron** (Matt McInerney) / **Audiowide** | OFL | rótulos de Nueva York 2099 y de Lyla | |
| **Luckiest Guy** (Astigmatic) | Apache 2.0 | alternativa gordita a Bangers | |
| **Archivo Black**, **Bowlby One**, **Bungee** | OFL | letras recortadas para el collage de Hobie (mezclarlas) | |

**Para las letras recortadas de Hobie**, no hay una letra que lo haga
bien: se hace **letra por letra**, mezclando 4 o 5 de la tabla, cada una
en su recorte de papel de otro color, un poco torcida.

**No probadas** (no las pude bajar): **Komika Axis / Komika Title**
(Apostrophic Labs, dafont) y **Anime Ace 2.0 BB** (Blambot) ⚠️.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que la saga pone en pantalla

1. **La caja amarilla de pensamiento** (UNU) ✅. Rectángulo **amarillo**,
   con **borde negro fino** y el texto en **mayúsculas de cómic** negras
   ⚠️ (el color exacto y el borde, de memoria). Repite lo que oímos en
   la voz en off de Miles.
   - **Regla del equipo**: «**no dialogue boxes or anything too
     comic book-y until after Miles is bitten**» (Christopher Miller) ✅
     ([Looper](https://www.looper.com/207630/the-self-imposed-rule-spider-man-into-the-spider-verse-had-to-follow/),
     [CBR](https://www.cbr.com/into-the-spider-verse-rule-using-comic-book-dialogue-boxes/)).
   - Primera caja: UNU 00:14:22. Avalancha de cajas: 00:16:14 a 00:16:40.
   - En el pasillo **se multiplican** y **se apilan** ✅
     ([Project MUSE](https://muse.jhu.edu/article/907197)).
2. **Onomatopeyas** dibujadas («THWIP»), **puntos Ben-Day**, **viñetas
   partidas** (la pantalla se divide como una página), **líneas de
   movimiento** y **bordes de papel rasgado** ✅
   ([No Film School](https://nofilmschool.com/comic-panels-in-spiderverse-movies)).
   «Thwip» también se dice: la lección de Peter B., UNU 00:53:43 a
   00:53:52 («Thwip and release. Feel the rhythm?»).
3. **Las viñetas de origen**: cuando cada araña se presenta, su vida
   pasa en **páginas de cómic** con su portada ✅ (UNU 00:35:39, 00:55:04,
   01:02:25; el aspecto de las páginas, de memoria ⚠️).
4. **El glitch** ✅: una araña fuera de su mundo **se descompone en
   fragmentos** y duele. ATSV 00:09:29 («You're glitching, huh? Been
   there.»), 00:52:55 (el reloj de la Spider-Society «keeps you from
   glitching in other dimensions»).
5. **El desfase de impresión** en vez de desenfoque ✅: lo que está fuera
   de foco **separa sus tintas** (cian, magenta, amarillo), como un
   cómic mal registrado. Justin K. Thompson, diseñador de producción,
   se inspiró en **las planchas desalineadas** de los cómics que miraba
   de niño ([Cartoon Brew](https://www.cartoonbrew.com/feature-film/spider-man-into-the-spider-verse-production-design-is-about-character-not-style-168137.html),
   [fxguide](https://www.fxguide.com/fxfeatured/why-spider-verse-has-the-most-inventive-visuals-youll-see-this-year/)).
6. **Animación a doses** ✅: Miles se mueve a **12 dibujos por segundo**
   (cada uno dura dos fotogramas); Hobie tiene **la chaqueta a cuatros, el
   cuerpo a veces a treses y la guitarra aún más lenta** ✅
   ([befores & afters](https://beforesandafters.com/2023/06/17/the-across-the-spider-verse-spider-punk-character-hobie-was-animated-with-different-frame-rates-for-different-parts-of-his-own-body-and-accessories/),
   [SlashFilm](https://www.slashfilm.com/1305454/spider-man-across-the-spider-verse-spider-punk-three-years-animate/)).
   ATSV fue **la primera película de animación CG con un equipo propio
   de entintado** ✅ ([befores & afters](https://beforesandafters.com/2023/06/28/this-was-the-first-cg-animated-movie-ive-ever-heard-of-that-actually-had-a-dedicated-inking-team/)).
7. **Lyla**, la inteligencia artificial de Miguel, habla como **un
   holograma pequeño y burlón** que aparece al lado ✅ (subtítulo:
   «Nah, you gotta say it first», ATSV 00:12:50; «But I enjoyed that»,
   00:12:58).

### 7.2 Cómo hablan (por el subtítulo) ✅

| Personaje | Registro | Ejemplos con minuto |
|---|---|---|
| **Miles** | chaval de Brooklyn, nervioso, gracioso sin querer; mete español con su mamá | «Maybe I'm not late. Maybe you guys are early.» (UNU 00:07:33); «That's intentional.» (00:12:33); «I'm just a really emotionally intelligent guy. Beyond my years.» (ATSV 00:50:53) |
| **Rio**, su mamá | puertorriqueña, **habla en español** en el original | «Miles, **papá**, time for school!» (UNU 00:02:51); «Well, **qué barbaridad**.» (ATSV 00:52:53); «**Oye**.» (00:42:13) |
| **Peter B.** | cansado, sarcástico, se va por las ramas | el discurso de los caballitos de mar (UNU 00:36:33); «Don't invest in a spider-themed restaurant.» (00:36:09) |
| **Gwen** | seca, contenida, frases cortas | «I don't do friends anymore.» (UNU 00:55:34); «I joined it so I could hit my feelings with sticks.» (ATSV 00:03:03) |
| **Hobie** | jerga de Londres: **bruv, innit, mandem, jumper, a'ight**; contra todo | «I hate labels.» (ATSV 01:10:49); «I don't believe in teams.» «Aren't you in a band?» «**I don't believe in consistency.**» (01:11:12); «It's propaganda, bruv.» (01:22:26); «Don't enlist till you know what war you're fighting.» (01:23:31). En latino, **«Fuchis las etiquetas»** en su presentación ✅ (audio de Doblaje Wiki, §10.3; no es la traducción línea a línea de «I hate labels» ⚠️). El doblaje cambia su acento británico por **modismos urbanos** ✅ |
| **Miguel** | seco, manda, se enfada rápido | «LYLA, do the thing.» «The information-explainy thing.» (ATSV 01:26:34); «You're the original anomaly.» (01:42:31) |
| **Lyla** | holograma bromista | «No further anomalies. Canon remains intact.» (ATSV 00:18:49) |
| **Spider-Ham** | chistes de dibujo animado viejo | «I just washed my hands. That's why they're wet.» (UNU 01:02:07) → en latino «**Es agüita**» ⚠️ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Spider-Man:_Un_nuevo_universo), una fuente) |

### 7.3 Cómo se traduce a una lámina fija

- **El texto del canal va en cajas amarillas rectangulares**, una idea
  por caja, **en mayúsculas** de cómic (Comic Neue Bold o Bangers),
  **borde negro fino**, un poco torcidas, **apiladas** como en el
  pasillo de UNU.
- **Lo que «dice» el personaje en voz alta** también va en caja (en la
  saga no hay globos redondos para Miles: lo que se ve escrito es lo que
  piensa o narra) ⚠️ (en las viñetas de origen sí hay algún globo, de
  memoria).
- **El nombre del canal**, como **cartela de lugar** o como **grafiti**.
- **Las etiquetas**, como **pegatinas** «HELLO my name is» (lámina 2).
- **Imprime la caja con desfase**: el amarillo 1-2 px movido respecto
  al negro, y una trama de puntos suave. Así no parece una caja de
  PowerPoint.

### 7.4 En los videojuegos de la franquicia

Ver §13: no hay un juego de estas películas con cajas de diálogo propias.
Lo más útil de los juegos es la **carta de *Marvel Snap*** (temporada
«Spider-Versus»): marco negro grueso, coste en la esquina y texto en una
caja abajo ✅ ([Marvel.com](https://www.marvel.com/articles/games/marvel-snap-swings-into-new-season-spider-versus)).
Sirve de modelo de **ficha de personaje tipo cómic** para el foro, no
para lo que dice el personaje.

### 7.4b El texto en pantalla en el doblaje latino (segunda pasada) ✅

Dato de oro para la etiqueta **Subtítulos**, de los «Datos de interés»
de [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Spider-Man:_A_trav%C3%A9s_del_Spider-Verso)
(API; una fuente, pero es la ficha del propio doblaje):

- En **UNU**, los **letreros tipo cómic se tradujeron** al español, y así
  siguen en las versiones física y digital.
- En **ATSV** se dejaron **en inglés con subtítulos en español**, salvo el
  título de la película.
- En la tele (Studio Universal) UNU salía con los letreros en inglés;
  ATSV se emite con **subtítulos forzados** y los textos finales
  traducidos.
- En los créditos finales de las dos **no sale nadie del doblaje** (ni el
  reparto original).

**Para la lámina**: la misma saga probó las dos soluciones (traducir el
rótulo o subtitularlo). Es un ejemplo real para un hilo de «¿traduzco el
cartel o le pongo subtítulo?».

### 7.5 Qué NO hacer con el texto

- **Nube de pensamiento** o **globo blanco redondo** para Miles: lo suyo
  son **cajas rectangulares amarillas** ✅ (guía de cuadros).
- Cajas **perfectas**, con sombra paralela y esquinas redondeadas de
  programa de oficina.
- Poner Ben-Day **por todas partes y con el mismo tamaño**: en la
  película va **en las sombras y en los medios tonos**, no encima de
  todo ✅ (ver los shaders de §4.4, que lo aplican por brillo).
- Mezclar el estilo de Hobie (collage) con el de Gwen (acuarela) en el
  **mismo personaje**: cada uno lleva **su** técnica ✅ (§1).
- Glitch en **todo**: en la saga el glitch significa «**esto no es de
  aquí**». Úsalo sólo en la etiqueta **Efectos**.

---

## 8 · Los personajes

Voz original: en la segunda pasada **todos** quedan confirmados con la
tabla bilingüe de Doblaje Wiki (columna «actor original») y
[Marvel.com](https://www.marvel.com/articles/movies/spider-man-into-the-spider-verse-shameik-moore-jake-johnson-interview) ✅.
Edad, altura y gustos: Punto 20. Su cara en cada emoción: al final de
esta sección.

### Miles Morales — el protagonista ✅

- **Quién es**: chaval de **Brooklyn**, hijo de **Jefferson Davis**
  (policía; en ATSV, capitán) y de **Rio Morales** (puertorriqueña).
  Le muerde una araña y se vuelve Spider-Man. En UNU acaba de entrar en
  un colegio de élite, **Brooklyn Visions Academy**, que no quiere
  («I'm only here 'cause I won that stupid lottery», UNU 00:05:37). En
  ATSV ya lleva **«un año y cuatro meses»** de Spider-Man (ATSV 00:23:31)
  y está en segundo de bachillerato («just a sophomore», 00:20:30).
- **Qué le importa**: su familia, **su tío Aaron** (que resulta ser el
  Merodeador), **Gwen**, y **ser él mismo**: «I'm gonna do my own
  thing» (ATSV 01:44:37).
- **Miedos**: no estar a la altura («When will I know I'm ready?», UNU
  01:19:31), decepcionar a su papá, estar solo («Sometimes I just wish I
  wasn't the only one», ATSV 00:24:42).
- **El artista**: pinta **grafiti** (UNU 00:11), pega **pegatinas** «HELLO
  my name is» por el barrio (UNU 00:04:18, 01:44:20) ✅, llena su cuarto
  de **dibujos** (ATSV 00:46:38), saca **A en arte** (ATSV 00:28:00) y
  **se diseña el traje**: «I designed my new suit with some fly
  ambience down the side» (ATSV 00:23:54). En UNU **pinta el traje con
  espray** ⚠️ (§2.6).
- **Cómo se expresa**: rápido, se enreda, bromea para salir del paso,
  suelta frases de «listo» que no le salen («Einstein said time was
  relative, right?», UNU 00:07:31). Con su mamá, spanglish.
- **Gestos y manías**: **los cordones desatados, a propósito** («Yeah,
  I'm aware. **It's a choice.**», UNU 00:06:50) ✅; auriculares puestos
  cantando «Sunflower» (UNU 00:02:45 a 00:03:10) ✅; manos en los
  bolsillos de la sudadera ⚠️.
- **Con quién aparece**: Gwen, Peter B., su papá (la charla por la
  puerta, UNU 01:20:23), su tío Aaron (el túnel), su compañero de cuarto
  Ganke ⚠️.
- **Su miedo con nombre**: Miles tiene un **trastorno de ansiedad**,
  dicho en ATSV y en el corto *The Spider Within: A Spider-Verse Story*
  ✅ (ficha de la wiki `spiderverse`, con las dos obras como fuente). Por
  qué es el protagonista: Lord y Miller vieron en su cómic «el origen
  perfecto para alguien joven descubriendo qué clase de persona quiere
  ser» ✅ ([Marvel.com](https://www.marvel.com/articles/movies/phil-lord-christopher-miller-spider-man-into-the-spider-verse-interview)).
- **Voz original**: **Shameik Moore** ✅. **Latina**: **Emilio Treviño** ✅
  (también dobla al Miles de Tierra-42, que en inglés es otro actor).
  Voz medida con `voz.py`: registro medio (171 Hz), muy expresiva
  (26,2 semitonos), 2,97 palabras por segundo (§10.3).

### Gwen Stacy (Spider-Woman) — la coprotagonista, 1.ª en IMDb ✅

- **Quién es**: de **Tierra-65**. Su mejor amigo **Peter Parker** murió
  en sus brazos (se volvió el Lagarto), y su papá, el **capitán George
  Stacy**, persigue a Spider-Woman creyendo que lo mató (ATSV 00:05:43 a
  00:07:41). Toca la **batería** en **The Mary Janes** ✅. En ATSV está en
  la **Spider-Society** de Miguel.
- **Qué le importa**: no volver a perder a nadie; su papá; Miles.
- **Miedos**: los amigos («I don't do friends anymore», UNU 00:55:34),
  que su papá sepa quién es, que la historia de «Gwen se enamora de
  Spider-Man» acabe mal («In every other universe… it doesn't end
  well», ATSV 00:51:48).
- **Cómo se expresa**: poco, seca, irónica. Se desahoga **tocando**:
  «I joined it so I could hit my feelings with sticks» (ATSV 00:03:03).
  Al final, líder: «I never found the right band to join. So I started
  my own» (ATSV 02:12:44).
- **Gestos**: la **capucha** que se echa encima (su silueta), posturas
  de **ballet**, colgarse **boca abajo** ✅. **Visto en vídeo**: en la
  torre del reloj está **de pie contra la pared, cabeza abajo**, la
  capucha colgando ([clip, 0:09](https://www.dailymotion.com/video/x8l73q0?t=9)) ✅.
- **Prenda fija**: sus **tenis turquesa** (Converse), los lleve con lo que
  los lleve ✅ (wiki). Pone «muros» para parecer más segura; sólo se le
  caen con Miles y el Spider-Gang ✅ (wiki).
- **Voz latina medida**: registro agudo (316 Hz) y **la más expresiva
  de las cinco** (30,7 semitonos) en su confesión a su papá (§10.3).
- **Voz original**: **Hailee Steinfeld** ✅. **Latina**: **Alondra
  Hidalgo** ✅.

### Peter B. Parker — el mentor que no quería serlo ✅

- **Quién es**: un Peter Parker **de 38 años en UNU y 39 en ATSV**
  (nació en 1980) ✅ (ficha de la wiki), divorciado de
  Mary Jane en UNU, con barriga, **pantalón de chándal**, comiendo; «I
  broke my back, a drone flew into my face, I buried Aunt May» (UNU
  00:36:14). En ATSV ya es **papá de Mayday**, la bebé, y se la lleva
  de misión ✅ ([CBR](https://www.cbr.com/funniest-spider-men-in-across-the-spider-verse/)).
- **Qué le importa**: pasar de todo… hasta que Miles le importa. Su
  lección es el **salto de fe** (UNU 01:19:35).
- **Cómo se expresa**: sarcástico, cansado, se va por las ramas (los
  caballitos de mar, UNU 00:36:33). Enseña **haciendo**: «Thwip and
  release. Feel the rhythm?» (UNU 00:53:43).
- **Cuerpo**: 1,78 m; pasa de **84 kg a 77,2 kg** entre las dos
  películas: se pone en forma al volver con MJ ✅ (wiki).
- **Voz original**: **Jake Johnson** ✅. **Latina**: **Miguel Ángel Ruiz** ✅.
  Voz medida: 266 Hz, muy expresiva (19,9 semitonos) (§10.3). Curiosidad:
  el **Peter Parker rubio que muere** en UNU lo dobla el propio director
  del doblaje, **Gerardo García** ✅ (§10).

### Miguel O'Hara (Spider-Man 2099) — el jefe, el rey de los memes ✅

- **Quién es**: de **Tierra-928**, la **Nueva York del año 2099**. Fundó
  la **Spider-Society** con **Lyla**, su inteligencia artificial ✅. Cree
  que los **eventos canónicos** no se pueden tocar o el universo se
  rompe (ATSV 01:27:32 a 01:28:51) ✅.
- **Aspecto**: enorme, **colmillos** y **garras** retráctiles, traje de
  **nanotecnología** que aparece y desaparece; los rojos **brillan** y el
  azul oscuro lo mete en la sombra ✅ ([CBR](https://www.cbr.com/spider-man-2099-across-the-spider-verse-suit-tragic/)).
  Gwen lo resume: «**a ninja-vampire-Spider-Man but a good guy**»
  (ATSV 00:48:09) ✅.
- **Qué le importa**: que nada se rompa. Quedó **«emocionalmente
  marcado»** por no poder evitar la destrucción de una dimensión, y es un
  líder **sobrecargado de trabajo** ✅ (wiki, «Personality»). La wiki
  guarda una imagen titulada «Miguel loose his daugther» (sic), que
  apunta a la hija ⚠️ (sólo el nombre del archivo).
- **Cuerpo**: **2,06 m** (6'9"), 35 años, nacido en 2063-2064 ✅ (wiki).
  Voz latina medida: **grave (99 Hz), la menos expresiva** del grupo
  (12 semitonos) y la más lenta (1,98 palabras/s) (§10.3).
- **Cómo se expresa**: órdenes cortas, cero paciencia, se enfada a
  gritos. Lyla lo pica: «Nah, you gotta say it first» (ATSV 00:12:50).
  Detalle tierno: le gustan **las empanadas** de la cafetería (ATSV
  01:21:44) ✅.
- **Voz original**: **Oscar Isaac** ✅. **Latina**: **José Luis Rivera**
  ✅ (su segunda vez: ya salió en el poscréditos de UNU).

### Hobie Brown (Spider-Punk) — el favorito de las redes ✅

- **Quién es**: el Spider-Man **punk de Londres**, de **Tierra-138**.
  Guitarra a la espalda **siempre** ✅ ([NamuWiki](https://namu.wiki/w/%EC%8A%A4%ED%8C%8C%EC%9D%B4%EB%8D%94%20%ED%8E%91%ED%81%AC)).
  Amigo íntimo de Gwen: ella se queda en su dimensión («He lets me crash
  in his dimension sometimes», ATSV 00:48:52), y le deja **su jersey**
  («Gwendy, you left your jumper around my place», 01:10:59).
- **Qué le importa**: **la independencia** («Whole point of being
  Spider-Man is your independence. Being your own boss», 01:23:11), no
  obedecer, su «drummer» Gwen («Looking out for my drummer, is all»,
  01:23:17).
- **Cómo se expresa**: jerga de Londres (**bruv, innit, mandem,
  a'ight**), frases que se contradicen a propósito: «I hate labels»…
  «I thought you hated labels»; «I don't believe in teams» «Aren't you
  in a band?» «**I don't believe in consistency.**» (01:10:49 a
  01:11:16). Se niega a hacer la presentación de siempre: «I was bitten
  by a— **Wouldn't you like to know?**» (01:10:28).
- **Aspecto**: estilo **fanzine**: fotocopia, collage, recortes; los
  **ojos del traje dibujados a mano**; «todo parece hecho por él mismo»
  ✅ ([Cartoon Brew](https://www.cartoonbrew.com/feature-film/it-took-nearly-two-years-to-design-the-hundreds-of-characters-in-across-the-spider-verse-238379.html),
  [Variety](https://variety.com/2023/artisans/awards/spider-punk-hobie-spider-verse-animators-1235707039/)).
  Su color **cambia a saltos** ✅ (NamuWiki).
- **Tardaron dos o tres años** en dar con su animación ✅
  ([SlashFilm](https://www.slashfilm.com/1305454/spider-man-across-the-spider-verse-spider-punk-three-years-animate/)).
- **Película propia en desarrollo**: *Spider-Punk*, anunciada en agosto
  de 2025, con **Daniel Kaluuya** coescribiendo con Ajon Singh ✅
  ([Deadline](https://deadline.com/2025/08/spider-punk-animated-feature-daniel-kaluuya-ajon-singh-sony-1236478287/),
  [Variety](https://variety.com/2025/film/news/spider-verse-spinoff-spider-punk-daniel-kaluuya-1236478758/)).
- **Voz original**: **Daniel Kaluuya** ✅. **Latina**: **Óscar Garibay**
  ✅; en el doblaje le cambiaron el acento británico por **modismos
  urbanos** ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/%C3%93scar_Garibay)
  y notas de prensa). Japonés: 木村昴 (Subaru Kimura) ⚠️.
- **Cuerpo y edad**: **1,95 m, 68 kg, 16-17 años**; Phil Lord comparó su
  edad con la de los Sex Pistols al empezar ✅ (wiki y cita del artbook).
  Voz latina medida: 178 Hz y **la más rápida** (3,96 palabras/s) (§10.3).

### Los secundarios que conviene tener a mano

| Personaje | Qué es | Dato útil |
|---|---|---|
| **Lyla** | la IA de Miguel, un **holograma** pequeño | cofundadora de la Spider-Society ✅ ([Into the Spider-Verse Wiki](https://intothespiderverse.fandom.com/wiki/LYLA)); explica los eventos canónicos (ATSV 01:26:40) |
| **Spider-Ham** (Peter Porker) | cerdo de dibujo animado | «Es agüita» en latino ⚠️; voz latina **Óscar Flores** ✅ |
| **Peni Parker** y SP//dr | chica anime con robot | «I'm from New York in the year 3145» (UNU 01:02:40) |
| **Spider-Man Noir** | blanco y negro, años treinta | «Wherever I go, the wind follows» (UNU 01:01:50) |
| **Pavitr Prabhakar** (Spider-Man India) | de **Mumbattan** | voz latina **Tommy Rojas** ✅ (Doblaje Wiki y [StarCon MX](https://www.facebook.com/starconmx/videos/tommy-rojas-actor-de-doblaje-que-dio-voz-pavitr-prabhakar-spider-man-india-en-sp/457477063491081/)); también es Cat Noir en *Miraculous* |
| **Jessica Drew** | embarazada, en **moto** | «She rides a motorcycle» (ATSV 00:47:42) |
| **La Mancha** (the Spot) | el villano «de la semana» que abre agujeros | voz latina **Javier Ibarreche** ✅ |
| **Jefferson y Rio** | los papás de Miles | «I love you, Miles» / «That's a copy» (UNU 00:06:07 a 00:06:29) |
| **El tío Aaron** | el Merodeador; el que le enseña el grafiti | «Makin' mistakes is part of it» (UNU 00:11:59) |

---

## 9 · ¿Quién es el más querido?

**No existe encuesta oficial** de Sony (no es un manga con votaciones).
Lo que hay:

| Señal | Resultado | Fuente |
|---|---|---|
| Encuesta de IMDb, **póster de personaje favorito** de ATSV | 1.º **Gwen**, 2.º Miles, 3.º Spider-Cat, 4.º Ben Reilly, 5.º Peter B., 6.º **Hobie**, 7.º la Mancha, 8.º Jessica Drew, 9.º Miguel, 10.º Pavitr | [IMDb](https://www.imdb.com/poll/T4YMIpvxSW0/results) ✅ (vota el póster, no el personaje) |
| Looper, **mejor historia** (más de 17 000 votos) | **Miles 51 %**, Gwen 22 %, Miguel 5 % | [Looper](https://www.looper.com/1305600/looper-asks-which-character-spider-man-across-the-spider-verse-best-storyline/) ✅ |
| **Película propia** | sólo **Hobie** tiene una en marcha (*Spider-Punk*, 2025) | Deadline, Variety ✅ |
| Cuenta oficial | TikTok de @spiderversemovie: «**We salute you, Hobie. 🤘 What's your favorite Spider-Punk quote?**» | [TikTok](https://www.tiktok.com/@spiderversemovie/video/7294411001653579054) ✅ |
| Memes | **Miguel** y los «eventos canónicos» fueron **el meme de junio de 2023** | Know Your Meme ✅ (§14) |
| Prensa china | «百位蜘蛛侠…哪七侠最招人喜欢» (de cien arañas, cuáles siete gustan más), sin ranking claro | [Beijing News](https://m.bjnews.com.cn/detail/1685942718168300.html) ⚠️ |

**Conclusión para la lámina**: el **principal (Miles)** es de verdad el
más querido y el que mejor encaja con «crear» (grafiti, dibujos,
pegatinas, traje propio). **Gwen** es la más votada en IMDb. **Hobie**
es el secundario que el fandom ama y el más «editor» de todos (collage,
fanzine). **Miguel** es para el chiste, no para dar la bienvenida.

---

## 10 · Doblaje latino

> [!warning] No pude entrar a Doblaje Wiki
> La API (`doblaje.fandom.com/es/api.php`) está bloqueada desde aquí.
> Lo de abajo sale del **extracto que el buscador da de Doblaje Wiki**
> más **notas de prensa**. Regla del dueño: antes de rotular, alguien
> debe abrir la API desde su PC y confirmar.

### 10.1 *Spider-Man: Un nuevo universo* (2018)

| Personaje | Voz latina | Estado |
|---|---|---|
| Miles Morales | **Emilio Treviño** | ✅ Doblaje Wiki + prensa ([La Razón](https://www.razon.com.mx/entretenimiento/2023/06/03/spider-man-a-traves-del-spider-verso-conoce-a-emilio-trevino-la-voz-de-miles-morales/), [SinEmbargo](https://www.sinembargo.mx/4369345/emilio-trevino-presta-su-voz-a-miles-morales-lo-mas-complicado-es-mantenerlo-real/)) |
| Peter B. Parker | **Miguel Ángel Ruiz** | ✅ Doblaje Wiki + prensa de ATSV |
| Gwen Stacy | **Alondra Hidalgo** | ✅ Doblaje Wiki + prensa de ATSV |
| Spider-Ham | **Óscar Flores** | ✅ Doblaje Wiki (dos extractos) |
| Kingpin | **Rubén Moya** | ⚠️ una fuente |
| Miguel O'Hara (poscréditos) | **José Luis Rivera** | ✅ (Doblaje Wiki dice que ATSV es su segunda vez) |

Emilio Treviño y Óscar Flores **fueron de los pocos que conservaron el
papel desde los tráileres** ✅ (Doblaje Wiki, extracto).

### 10.2 *Spider-Man: A través del Spider-Verso* (2023)

| Personaje | Voz latina | Estado |
|---|---|---|
| Miles Morales | **Emilio Treviño** | ✅ |
| Gwen Stacy | **Alondra Hidalgo** | ✅ |
| Peter B. Parker | **Miguel Ángel Ruiz** | ✅ |
| Miguel O'Hara | **José Luis Rivera** | ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Jos%C3%A9_Luis_Rivera), [vídeo en Facebook](https://www.facebook.com/AnimexSeriesproduction/videos/jos%C3%A9-luis-rivera/689208810316395/), prensa) |
| Hobie Brown | **Óscar Garibay** | ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/%C3%93scar_Garibay) + prensa) |
| Pavitr Prabhakar | **Tommy Rojas** | ⚠️ una fuente |
| La Mancha | **Javier Ibarreche** (*influencer*) | ✅ ([YouTube](https://www.youtube.com/watch?v=d65-IKm8C-Q), [Facebook JetpackCave](https://www.facebook.com/JetpackCave/posts/de-%C3%BAltimo-momentojavier-ibarreche-le-dar%C3%A1-voz-a-the-spot-la-mancha-en-spider-man/752742346854111/)) |
| Otros *influencers* | **Alex Montiel** (el Escorpión Dorado), **Gaby Meza**, **Andrés Navy**, **Juan Guarnizo** | ✅ que participan ([SensaCine](https://www.sensacine.com.mx/noticias/noticia-1000024768/), [3DJuegos](https://www.3djuegos.lat/cine-y-tv/spider-man-a-traves-spider-verso-confirma-su-doblaje-latino-lleno-influencers-youtubers-tiktokers-todo-contrario-a-super-mario-bros)); **qué papel hace cada uno** ⚠️ (la dirección de 3DJuegos sugiere que Guarnizo es el Spider-Man de *Spectacular*) |
| Peruanos | **Adolfo Aguilar** y **Jorge Talavera** | ⚠️ ([Infobae Perú](https://www.infobae.com/peru/2023/05/20/spider-man-a-traves-del-spider-verso-adolfo-aguilar-y-jorge-talavera-daran-sus-voces-a-la-nueva-cinta-de-marvel/)); papel no visto |

- **Polémica**: tantos *influencers* **generaron quejas**, y tras las
  críticas hubo **funciones subtituladas** ✅
  ([Infobae](https://www.infobae.com/mexico/2023/05/17/spider-man-a-traves-del-spider-verso-desato-quejas-por-su-doblaje/),
  [El Financiero](https://www.elfinanciero.com.mx/entretenimiento/2023/05/20/spider-man-a-traves-del-spider-verso-tendra-funciones-con-subtitulos-tras-criticas-a-doblaje-de-influencers/)).
  Los cuatro principales que repitieron **fueron muy aplaudidos**.
  **Consejo**: la lámina debe citar a los **actores de siempre**, no a
  los *influencers*.
- **Emilio Treviño**: fan de Spider-Man desde niño, había hecho casting
  para Peter Parker sin suerte; en ATSV le dejaron **meter frases y
  «easter eggs»** suyos; «lo más complicado es **mantenerlo real**» ✅
  ([SinEmbargo](https://www.sinembargo.mx/4369345/emilio-trevino-presta-su-voz-a-miles-morales-lo-mas-complicado-es-mantenerlo-real/),
  [La Crónica](https://www.cronica.com.mx/escenario/emilio-trevino-empatia-miles-morales-spiderman-traves-spiderverso.html)).
- **Estudio y director de doblaje**: **no los encontré** en ninguna de
  las dos películas.
- **2026**: hubo un **Spider-Fest en la CDMX** con actores de doblaje
  ⚠️ ([Infobae, 13-jun-2026](https://www.infobae.com/mexico/2026/06/13/llega-el-spider-fest-a-la-cdmx-actores-de-doblaje-concursos-y-proyecciones-gratis-lugar-fecha-y-horario/)).

### 10.3 Frases del doblaje latino (sólo las que tienen fuente)

| Escena | Original | Latino | Estado |
|---|---|---|---|
| Spider-Ham sale del baño con la mano mojada (UNU 01:02:07) | «I just washed my hands. That's why they're wet.» | «**Es agüita**» | ⚠️ una fuente (Doblaje Wiki, extracto) |
| Miles a Kingpin en la pelea final (UNU 01:36:28) | «**Adiós.**» (en español en el original) | «**Sayonara**» | ⚠️ una fuente (guía de cuadros, que cita Doblaje Wiki) |
| Tío Ben | «With great power comes great responsibility» (UNU 00:01:33) | es **el audio de las películas de Raimi** | ⚠️ (guía de cuadros) |

**No encontré** cómo dice el doblaje «Anyone can wear the mask», «leap
of faith», «I hate labels» ni «I'm gonna do my own thing». Las frases de
la lámina, por tanto, van **traducidas por mí** y marcadas; si el dueño
tiene la película en latino, que las sustituya por las del doblaje.

---

## 11 · Música

| Tema | Película | Ambiente | Fuente |
|---|---|---|---|
| **«Sunflower»** — Post Malone y Swae Lee | UNU (Miles la canta con auriculares, 00:02:45) | relajado, adolescente | ✅ single del 18-oct-2018 |
| **«What's Up Danger»** — Blackway y Black Caviar | UNU, el salto de fe (01:22:56 a 01:24:30) | subidón, «ahora sí» | ✅ single del 1-nov-2018 |
| «Hypnotize» (The Notorious B.I.G.), por la letra «Biggie there e'rynight» | UNU, cuando Miles va a ver al tío Aaron (00:09:04 a 00:09:27) | Brooklyn noventero | letra en el subtítulo ✅ / título ⚠️ |
| «The Choice Is Yours» (Black Sheep), por la letra «You can get with this or you can get with that» | UNU, el túnel del grafiti (00:11:54 a 00:12:27) | hip-hop clásico, pintar con los colegas | letra en el subtítulo ✅ / título ⚠️ |
| **«Annihilate»**, **«Am I Dreaming»** (Metro Boomin, A$AP Rocky, Roisee), **«Calling»** | ATSV (disco de Metro Boomin, 13 temas, 47 min) | trap, épico y triste | ✅ ([Apple Music](https://music.apple.com/us/album/metro-boomin-presents-spider-man-across-the-spider/1690685331)) |
| **Partitura de Daniel Pemberton** (34 temas): «Spider-Woman (Gwen Stacy)», «Spider-Punk (Hobie Brown)», «Guggenheim Assemble» | ATSV | orquesta de 100 músicos + **scratch de DJ**, voces de ópera, techno, **punk**, percusión india tipo *acid house*… y **un ganso** sampleado | ✅ ([Rolling Stone](https://www.rollingstone.com/music/music-features/spider-man-across-the-spider-verse-soundtrack-exclusive-composer-daniel-pemberton-goose-score-1234742686/), [The Credits](https://www.motionpictures.org/2023/06/spider-man-across-the-spider-verse-composer-daniel-pemberton-reveals-a-few-score-secrets/)) |
| El tema de **Miguel / 2099** | ATSV | el que se usa en TikTok para los memes de «evento canónico» | ✅ Know Your Meme |

Pemberton: **cada universo tiene su paleta de sonido** y cada personaje
sus sonidos ✅ ([Screen Rant](https://screenrant.com/spiderman-across-the-spiderverse-composer-daniel-pemberton-interview/)).
**Para la lámina**: no suena, pero **unos auriculares** colgados del
cuello de Miles son un guiño a «Sunflower». Los títulos de los dos temas
de hip-hop los saco **por la letra** que trae el subtítulo: no los
verifiqué en los créditos.

---

## 12 · Vídeos

YouTube está bloqueado desde aquí: **no pude comprobar minutos dentro de
los vídeos**. Doy el enlace y, para las escenas, el **minuto de la
película** (§2).

### 12.1 Tráileres oficiales

| Vídeo | Enlace | Nota |
|---|---|---|
| UNU, tráiler 2 (2-oct-2018) | [YouTube](https://www.youtube.com/watch?v=tg52up16eq0) | presenta a Noir, Ham y Gwen |
| ATSV, tráiler 1 (13-dic-2022) | [YouTube](https://www.youtube.com/watch?v=cqGjhVJWtEg) | |
| ATSV, tráiler 2 (4-abr-2023) | [YouTube](https://www.youtube.com/watch?v=4WKHNNtVbUM) | Sony Animation |
| ATSV, **tráiler doblado al latino** | [YouTube](https://www.youtube.com/watch?v=b3_1cyJRaQ8), [tráiler 2 latino](https://www.youtube.com/watch?v=rVLFOx7AQp0) | canal no comprobado ⚠️ |
| *Beyond the Spider-Verse*, primer vistazo | [YouTube](https://www.youtube.com/watch?v=Fbu6JK0i78w) | ⚠️ puede ser de un canal no oficial |
| Logos de UNU en 4K | [YouTube](https://www.youtube.com/watch?v=MV2Xutd3BM8) | referencia del glitch |

### 12.2 Detrás de las cámaras y análisis

| Vídeo | Enlace |
|---|---|
| «Beyond The Screen: The Creators Behind *Spider-Man: Across the Spider-Verse*» (Sony, oficial) | [YouTube](https://www.youtube.com/watch?v=u7OpYJFQXms) |
| *Making of* de ATSV (recopilación) | [YouTube](https://www.youtube.com/watch?v=PITNvuEV0Co) |
| «Animating The Spot» | [YouTube](https://www.youtube.com/watch?v=V1A_BAo8x7A) |
| Cómo se usó Maya en ATSV | [YouTube](https://www.youtube.com/watch?v=j_x4sHWZqvg) |
| «Different Animation Styles», UNU | [YouTube](https://www.youtube.com/watch?v=MlVBMvKI2s4) |
| «Analysing the Art of SpiderVerse: Animation Styles Edition» | [YouTube](https://www.youtube.com/watch?v=q86tPSkGmgs) |
| «I Made a Across the Spider-Verse Animation in 24 Styles» (de un aficionado: ideal para #edicion) | [YouTube](https://www.youtube.com/watch?v=iPd-TQnLyS8) |
| Kris Anka enseña sus diseños (TikTok de Crunchyroll) | [TikTok](https://www.tiktok.com/@crunchyroll/video/7279197842877582635) |

### 12.3 Lo que se hace en TikTok (útil para el canal)

- **Tutoriales del efecto Spider-Verse** en **CapCut** y After Effects:
  plantillas, glitch, «filtro Spider-Verse», **la letra Spider-Verse en
  CapCut** ✅
  ([ejemplo con plantilla](https://www.tiktok.com/@akthawicked/video/7242753570527792389),
  [andar por el techo con CapCut](https://www.tiktok.com/@tylertometich/video/7253447911181176107),
  [búsqueda «Spiderverse Glitch Effect»](https://www.tiktok.com/discover/spiderverse-glitch-effect)).
- **Edits de Hobie** y de Miles a montones ✅ (§9).
- Los propios actores latinos **dicen frases icónicas** en un TikTok ⚠️
  ([enlace](https://www.tiktok.com/@chick_flick_of/video/7347184102971297030), no lo pude ver).

---

## 13 · Videojuegos de la franquicia

No hay **un juego de estas películas**. Lo que existe son **trajes y
aspectos** en otros juegos:

| Juego | Qué trae | Fuente |
|---|---|---|
| *Marvel's Spider-Man: Miles Morales* (Insomniac, 2020) | **traje «Un nuevo universo»** que **anima a doses** como la película | ✅ [Digital Trends](https://www.digitaltrends.com/gaming/spider-man-miles-morales-into-the-spider-verse-suit/), [GamesRadar](https://www.gamesradar.com/spider-man-miles-morales-into-the-spider-verse-suit/) |
| *Marvel's Spider-Man 2* (2023) | **tres** trajes de UNU (Noir para Peter; dos para Miles, niveles 30 y 33) y el **traje de ATSV** para Miles | ✅ [GameSpot](https://www.gamespot.com/gallery/all-marvels-spider-man-2-costumes-revealed-so-far/2900-4771/), [Kotaku](https://kotaku.com/spider-man-2-miles-morales-into-the-spider-verse-suit-1850950068) |
| *Fortnite* | **Miles** y **Miguel** de ATSV (desde el 23-may-2023); **Spider-Gwen** (pase del capítulo 3, temporada 4, 2022) | ✅ [esports.gg](https://esports.gg/news/fortnite/fortnite-x-spider-verse-collab-all-skins-release-date-and-cost/), [Tech Times](https://www.techtimes.com/articles/291661/20230518/fortnite-leaks-spider-verse-skins-include-miles-morales-man-2099.htm) |

- **Cajas de diálogo**: ninguno de estos juegos tiene una caja «de las
  películas». En los juegos de Insomniac el diálogo es **subtítulo
  sencillo** ⚠️ (de memoria). **No sirven de cuadro para la lámina.**
- The Cutting Room Floor y Game UI Database: **bloqueados** desde aquí.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todos reconocen

- **«Canon event»** ✅: el meme de **junio de 2023**. La gente llama
  «evento canónico» a cualquier desgracia propia («Realizing it was never
  trauma, just a canon event», @greekos_nikos, 2-jun-2023, **más de 4
  millones de vistas en una semana**). Se usa con **el tema musical de
  Miguel** de fondo ([Know Your Meme](https://knowyourmeme.com/memes/canon-events-spider-verse),
  [guía de KYM](https://knowyourmeme.com/editorials/guides/what-are-canon-events-the-spider-verse-meme-trend-explained),
  [The Tab](https://thetab.com/2023/06/13/canon-event-explained-tiktok-trend-spider-man-across-the-spider-verse-sony)).
  **Chiste para el canal**: «Que se te corra el subtítulo es un evento
  canónico» ⚠️ (idea mía).
- **El meme de los dos Spider-Man que se señalan**, rehecho en el
  **poscréditos de UNU** con Miguel y el Spider-Man de 1967 ✅
  (UNU 01:56:19 a 01:56:34: «How dare you point at me!» «You were
  pointing first.»). El meme viene de la serie animada de 1967 ⚠️.
- **El salto de fe** con «What's Up Danger» (UNU 01:23:23) ✅, y el
  plano **boca abajo** ⚠️.
- **«Anyone can wear the mask. You could wear the mask.»** (UNU 01:44:43)
  ✅. En España lo citan como «Cualquiera puede llevar la máscara»
  ([Cultture](https://www.cultture.com/into-the-spider-verse-20-mejores-frases-de-la-pelicula));
  la forma latina no la encontré ⚠️.
- **Miles y Gwen boca abajo** en la torre del reloj (ATSV 00:49:31 a
  00:52:14): es **el fondo de pantalla** más repetido ✅ (búsqueda
  «Miles and Gwen upside down» en [Alpha Coders](https://alphacoders.com/search/view?q=spider+man+across+the+spider+verse+miles+and+gwen+upside+down),
  [MoeWalls](https://moewalls.com/movies/miles-morales-and-gwen-stacy-spider-man-across-the-spider-verse-live-wallpaper/)).
- **Las frases de Hobie** (la cuenta oficial pidió «tu frase favorita de
  Spider-Punk») ✅, sobre todo «**I hate labels**» y el lío del
  «**jumper**» («What's a jumper?» «It's a sweater.», ATSV 01:11:01).
- **Los cordones de Miles**: «It's a choice.» (UNU 00:06:50) ✅.
- **El chico del LEGO** (§2.7) ✅.
- **Easter eggs** a montones: [Screen Rant, 80](https://screenrant.com/spider-man-across-the-spider-verse-easter-eggs/),
  [Looper](https://www.looper.com/1303117/easter-eggs-spiderman-across-the-spiderverse/),
  [ExtremeMovie, 31 (coreano)](https://extmovie.com/movietalk/91139937).

### 14.2 Qué NO hacer (lo que un fan notaría)

- **Miles con el traje rojo y azul** de Peter: el suyo es **negro con la
  araña roja** (y en ATSV, su versión rediseñada) ✅.
- **Gwen con melena rubia larga**: lleva el pelo **corto con un lado
  rapado** ✅ («I like your haircut.» «You don't get to like my
  haircut.», UNU 00:56:20) y en ATSV **más rosa** ✅ («Your hair has
  gotten pinker», ATSV 00:46:13).
- **Hobie ordenado, obediente o de un solo color**: es lo contrario.
  Y **nunca sin la guitarra** ✅.
- **Miguel dando la bienvenida con una sonrisa**: es el antagonista de
  ATSV. Si sale, **serio o gritando** ✅.
- **Todo el cuadro con el mismo estilo** o con **3D brillante de
  plástico**: la saga mezcla técnicas y usa textura de imprenta ✅.
- **Cajas antes de la picadura** (si se cuenta algo de «antes» de ser
  Spider-Man, sin cajas) ✅ — chiste fino para fans.
- **Nube de pensamiento o globo blanco** para Miles ✅.
- Títulos mal: en Latinoamérica son ***Spider-Man: Un nuevo universo***
  y ***Spider-Man: A través del Spider-Verso*** ✅. (En España la segunda
  se llamó distinto ⚠️.)
- **Destripar** el final de ATSV (Miles en la Tierra-42 y el otro Miles
  como Merodeador, 02:10:41 a 02:11:12): mejor no, **aún no ha salido**
  la tercera.
- Usar las voces de los *influencers* como «la voz» del personaje (§10).

---

## 15 · Poses analizadas por personaje

El **minuto** sale del subtítulo ✅ (es el momento en que se dice la
frase). **La postura** la describo **de memoria** ⚠️: hay que sacar el
fotograma en ese minuto y comprobarla antes de usarla.

### Miles

| # | Minuto | Qué hace (⚠️ postura de memoria) | Sirve para |
|---|---|---|---|
| 1 | UNU 00:02:45 | en su cuarto, **auriculares puestos**, cantando «Sunflower» mientras recoge | **presentar** relajado |
| 2 | UNU 00:06:48 | entra al colegio con los **cordones sueltos**: «It's a choice.» | presentar con actitud |
| 3 | UNU 00:11:37 a 00:12:41 | **pintando con espray** en el túnel, brazo estirado; luego se aparta: «Is it too crazy?» | **explicar el proceso** |
| 4 | UNU 00:16:14 a 00:16:40 | **agobiado** en el pasillo, rodeado de cajas amarillas | **dudar**, pensar |
| 5 | UNU 00:53:43 | practicando la telaraña con Peter B., **muñeca hacia delante** | **truco que funciona** |
| 6 | UNU 01:23:23 a 01:24:30 | **salto de fe**, cayendo boca abajo con los brazos abiertos | **animar**, celebrar |
| 7 | UNU 01:44:43 | **habla a cámara**: «Anyone can wear the mask. You could wear the mask.» | **invitar** al que mira |
| 8 | ATSV 00:25:12 a 00:25:23 | pelea con la Mancha **mientras contesta un mensaje** a su mamá («In a minute») | humor, hacer dos cosas a la vez |
| 9 | ATSV 00:46:38 | **se pone rojo** cuando Gwen ve sus dibujos: «Hey. What? No.» | **vergüenza** al enseñar tu trabajo |
| 10 | ATSV 01:44:31 | desafiante: «I'm gonna do my own thing.» | **regañar** con cariño, animar |

### Gwen

| # | Minuto | Qué hace | Sirve para |
|---|---|---|---|
| 1 | ATSV 00:02:45 a 00:03:35 | **aporreando la batería** con The Mary Janes | **celebrar**, energía |
| 2 | ATSV 00:07:11 a 00:07:41 | abrazo torpe con su papá («too punk rock to give your old man a hug?») | emoción |
| 3 | ATSV 00:08:55 a 00:10:30 | pelea en el Guggenheim, movimientos de **ballet** | acción |
| 4 | UNU 00:14:44 a 00:16:05 | conoce a Miles («Gwanda»), él se le pega al pelo | humor |
| 5 | UNU 00:55:04 a 00:56:10 | se presenta «one last time» | **presentar** |
| 6 | ATSV 00:46:38 a 00:46:48 | **mira los dibujos** de Miles: «They're good. Wow, there's so many.» | **valorar el trabajo ajeno** (¡la galería!) |
| 7 | ATSV 00:49:31 a 00:52:14 | **boca abajo** junto a Miles en la torre del reloj | **pensar**, charlar |
| 8 | ATSV 02:12:44 a 02:13:18 | arma su banda y pregunta: «**You want in?**» | **invitar** a unirse |

### Peter B.

| # | Minuto | Qué hace | Sirve para |
|---|---|---|---|
| 1 | UNU 00:35:39 a 00:37:06 | su resumen: comida, chándal, barriga | presentar con humor |
| 2 | UNU 00:53:43 a 00:54:05 | enseña a tirar telaraña; «We're a little team!» | **explicar**, truco |
| 3 | UNU 01:19:12 a 01:19:40 | le dice a Miles que aún no está listo: «It's a leap of faith.» | **consejo** serio |
| 4 | ATSV 01:25:19 a 01:25:29 | llega con **Mayday** en la mochila: «I have a baby.» | humor |
| 5 | ATSV 01:38:34 a 01:38:49 | le ofrece la bebé a Miguel para calmarlo: «Do you wanna hold my baby?» | calmar, mediar |

### Miguel

| # | Minuto | Qué hace | Sirve para |
|---|---|---|---|
| 1 | UNU 01:56:04 a 01:56:34 | **el meme de señalar** con el Spider-Man del 67 | chiste |
| 2 | ATSV 00:10:58 a 00:12:58 | llega al Guggenheim, serio; Lyla se burla | presentar serio |
| 3 | ATSV 01:21:49 a 01:22:14 | su monólogo, solo en la sede | **pensar** |
| 4 | ATSV 01:26:34 a 01:28:51 | **explica** los eventos canónicos con el holograma | **explicar** |
| 5 | ATSV 01:42:10 a 01:43:27 | «You're the original anomaly.» | **regañar** (de verdad) |

### Hobie

| # | Minuto | Qué hace | Sirve para |
|---|---|---|---|
| 1 | ATSV 01:09:58 a 01:11:16 | **entra** en Mumbattan y se presenta a medias, guitarra a la espalda | **presentar** |
| 2 | ATSV 01:22:20 a 01:23:31 | en la sede, con un aparato **arrancado de la pared**: «It's propaganda, bruv.» | **aconsejar** a su manera |
| 3 | ATSV 01:26:25 | le aplaude a Miles: «Taking a crap on the establishment. I salute you.» | **celebrar** |
| 4 | ATSV 02:12:54 | parte de la banda nueva de Gwen | grupo |

### Lyla

| # | Minuto | Qué hace | Sirve para |
|---|---|---|---|
| 1 | ATSV 00:12:47 a 00:12:58 | se hace de rogar: «Nah, you gotta say it first.» | humor |
| 2 | ATSV 00:18:44 a 00:18:51 | escanea: «No further anomalies. Canon remains intact.» | informar |
| 3 | ATSV 01:26:37 a 01:27:25 | «the information-explainy thing» | **explicar** |

---

## 16 · Vestuario ⚠️

| Personaje | Ropa icónica | Detalles | Fuente |
|---|---|---|---|
| **Miles**, UNU (civil) | sudadera, pantalón corto de baloncesto sobre el traje, **Air Jordan 1 «Chicago»** (rojo, blanco y negro), cordones sueltos, auriculares | la sudadera con capucha forma parte del «traje» | [CostumeWall](https://costumewall.com/dress-like-spider-man-miles-morales/), [Nerdist](https://nerdist.com/article/spider-verse-miles-morales-shoes-air-jordans-origins/) ✅ |
| **Miles**, traje | **negro** con la **araña roja** pintada con espray; en ATSV lo **rediseña él** («fly ambience down the side») | la araña del pecho parece **de grafiti** | subtítulo ✅ / forma ⚠️ |
| **Gwen** | traje **blanco y negro** con **capucha**; telaraña **rosa y azul** bajo los brazos y en el forro; **zapatillas de ballet** azul claro (UNU); en ATSV **guantes rosa** largos y **Converse turquesa** | la capucha es su silueta | [Into the Spider-Verse Wiki](https://intothespiderverse.fandom.com/wiki/Gwendolyn_Stacy_(Earth-65)), tiendas de cosplay ✅ (dos fuentes de fans) |
| **Peter B.** | traje viejo bajo **pantalón de chándal**, barriga; en ATSV **bata** y la bebé en mochila | «ya no intenta parecer Spider-Man» | [CBR](https://www.cbr.com/funniest-spider-men-in-across-the-spider-verse/) ⚠️ (una fuente) |
| **Miguel** | traje **azul oscuro** con rojos que **brillan**; capa y máscara de nanotecnología; garras marcadas | ver §8 | [CBR](https://www.cbr.com/spider-man-2099-across-the-spider-verse-suit-tragic/) ✅ |
| **Hobie** | chaqueta vaquera sin mangas con **pinchos** e **imperdibles**, **pelo en pinchos**, guitarra, **ojos pintados a mano** | los colores **cambian a saltos** | Cartoon Brew, NamuWiki, [Zhihu](https://zhuanlan.zhihu.com/p/636201673) ✅ |

**La ropa «que todos reconocen»**: la **sudadera negra y las Jordan** de
Miles, la **capucha blanca** de Gwen, el **chándal** de Peter B., el
**azul y rojo brillante** de Miguel y **la guitarra** de Hobie.

---

## 17 · Paisajes y fondos de pantalla

### 17.1 Los sitios, con su luz ⚠️

| Sitio | Hora y luz (de memoria) |
|---|---|
| Túnel del grafiti (UNU) | **noche**, oscuro, luz de linterna y de farola; el color lo pone la pintura (medido: casi negro, §5.2) ✅ |
| Calle de Miles (UNU) | **mañana**, sol bajo, ladrillo cálido |
| Torre del reloj (ATSV) | **atardecer**, ciudad abajo, cielo naranja y morado |
| Tierra-65 (Gwen) | acuarela que **cambia con su ánimo**: rosa y violeta tristes, cian cuando está en paz ✅ (primarios cian, naranja y violeta) |
| Nueva York 2099 (Miguel) | **día azul limpio** arriba, **oscuro de neón** abajo ✅ |
| Tierra-138 (Hobie) | interior de club: **carteles, fotocopia, sombras duras** ✅ |

### 17.2 Fondos de pantalla

| Imagen | Tamaño | Autor / origen | Enlace |
|---|---|---|---|
| Miles y Spider-Gwen, UNU | 3840×2160 | ⚠️ sin autor en el resultado | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=977082) |
| ATSV, muestra 4K | 6522×3669 | ⚠️ | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1295233) |
| Miles y Gwen, ATSV (fan art) | 4782×2097 | 林霰 | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1319119) |
| Miles y Gwen boca abajo, animado | 3840×2160 | ⚠️ | [MoeWalls](https://moewalls.com/movies/miles-morales-and-gwen-stacy-spider-man-across-the-spider-verse-live-wallpaper/) |
| Portada de ATSV | 4K, 5K, 8K | ⚠️ | [4kwallpapers](https://4kwallpapers.com/black-dark/spider-man-across-11476.html) |
| Colecciones | varias | — | [Alpha Coders (210+)](https://alphacoders.com/spider-man-across-the-spider-verse-wallpapers), [WallpaperAccess](https://wallpaperaccess.com/spider-man-across-the-spider-verse), [UHDpaper](https://www.uhdpaper.com/2022/09/spider-man-across-4k-8840h.html?m=1) |

Sirven para **mirar luz y encuadre**, no para pegarlos.

---

## 18 · Guía para generar con IA (Firefly, Canva)

> Para **fondos, texturas y pruebas de pose**. El personaje final se
> recorta de un fotograma o póster real (regla del dueño), no se
> inventa con IA.

### 18.1 Lo que nunca cambia

- **Técnica mezclada**: 3D con **contorno dibujado a mano**, **puntos
  Ben-Day** en las sombras, **rayado** (hatching) en vez de sombras
  suaves, y **desfase de tintas** en lo desenfocado.
- **Animación a doses**: en una imagen fija se nota en **líneas de
  movimiento dibujadas** y **poses muy marcadas**, no en desenfoque de
  movimiento.
- **Noche o interior oscuro**, con **color fuerte** puesto por la luz
  (neón, farolas, espray).
- Miles: **negro y rojo**. Gwen: **blanco, rosa y turquesa**, capucha.
  Hobie: **collage**, guitarra. Miguel: **azul oscuro y rojo que brilla**.

### 18.2 Palabras que ayudan (en inglés, que las IA entienden mejor)

`comic book halftone Ben-Day dots, CMYK misregistration, offset
printing error, chromatic aberration on out-of-focus areas, hand-drawn
ink linework over 3D, cross-hatching shadows, bold graphic lighting,
Brooklyn night, graffiti wall, spray paint drips, sticker bombing,
zine collage, photocopy texture, torn paper edges, stylized animation
still`

Para Gwen: `watercolor wash background, soft bleeding colors, cyan
orange violet palette`. Para Hobie: `punk zine, xerox, cut-out ransom
note letters, safety pins, poster wall`. Para 2099: `retro-futurist
brutalist city, Syd Mead style, clean blue daylight`.

### 18.3 Palabras que lo estropean

`Pixar, Disney, glossy 3D render, soft pastel, anime` (sale otra cosa),
`photorealistic`, `bokeh / depth of field blur` (la saga **no** desenfoca
así: desplaza las tintas), `speech bubble`, `thought cloud`, y nombres de
personajes (la IA mete el traje equivocado o se niega).

### 18.4 Qué referencias usar

- **Estilo general**: los pósters de personaje de ATSV (§3.1) y los
  shaders de §4.4 (para entender qué hace cada capa).
- **Grafiti y túnel**: fotograma UNU 00:12:41 + textura Poly Haven
  `wall_bricks_plaster` + HDRI `concrete_tunnel`.
- **Collage de Hobie**: póster de personaje de Hobie + fan art de Ivan
  Shavrin (§4.3) sólo para ver cómo se reparte el collage.
- **Acuarela de Gwen**: hilo #CreatingTheSpiderVerse (§3.2) y los
  *color keys* de @chuwenjie.

---

## 19 · Tres conceptos para la lámina de #edicion

Los tres usan los textos de §0. Las frases «en la voz de la serie» son
**traducción mía** del subtítulo inglés, no del doblaje latino (no lo
encontré). Recortes siempre por `v3/integrar.py` y comprobados a 1:1.
Los tres cumplen lo que pedía el plan: **cajas amarillas**, **viñetas**,
**glitch** y **desfase de impresión**.

### Concepto A — «La pared del túnel» (Miles pinta; el favorito)

- **Objeto y sitio**: la **pared de la estación de metro abandonada**
  donde el tío Aaron lleva a Miles a pintar (UNU 00:10:56 a 00:13:07).
  En Blender: pared curva de ladrillo y yeso
  ([wall_bricks_plaster](https://polyhaven.com/a/wall_bricks_plaster)),
  capas de grafiti viejo debajo, **una pieza nueva encima**, botes de
  espray en el suelo ([smakologg, CC BY](https://sketchfab.com/3d-models/spray-can-graffiti-low-poly-by-smakologg-bd4f3e7d509f4fd691d9ee6def794f19),
  [Shara Ritchey, CC BY](https://sketchfab.com/3d-models/spray-paint-can-360f6ce433894dc3baaa7e035b617aac)),
  una lámpara de obra. Luz del HDRI
  [concrete_tunnel](https://polyhaven.com/a/concrete_tunnel).
- **Personaje**: **Miles**, el protagonista y el más querido. Pose 3 de
  §15: **pintando con el brazo estirado** (UNU 00:11:37 a 00:12:41), o
  **dando un paso atrás para mirar su pieza** («Is it too crazy?»,
  00:12:41). Auriculares al cuello y cordones sueltos.
- **Cómo habla**: **cajas amarillas** de pensamiento, en **Comic Neue
  Bold** mayúsculas, borde negro, **apiladas** como en el pasillo de UNU.
  Frase de gancho: **«Equivocarse es parte de esto.»** (de «Makin'
  mistakes is part of it», 00:11:59). Y junto a un chorreón de pintura,
  una caja pequeña: **«Es a propósito.»** (de «That's intentional»,
  00:12:33).
- **Dónde va cada texto**:
  - La pieza de grafiti grande: **EDICIÓN**, en **Rubik Spray Paint**,
    con chorreones.
  - Debajo, como firma de grafitero: **Vídeo y arte** (Sedgwick Ave
    Display).
  - Caja amarilla 1: **Un hilo por cosa**.
  - Cinco **pegatinas «HELLO my name is»** pegadas en la pared, escritas
    a rotulador (Permanent Marker): **Montaje**, **Subtítulos**,
    **Miniaturas**, **Portadas**, **Diseño**.
  - Caja amarilla 2: **Lo terminado se enseña en galería**.
  - Caja amarilla 3: **Aquí, el proceso y las dudas** ⚠️ (pendiente
    del dueño).
- **Para que no quede plano**: botes de espray **en primer plano, fuera
  de foco y con las tintas desplazadas** (el «desenfoque» de la saga);
  **niebla de pintura** en el aire, cortada por la luz de la lámpara;
  fondo del túnel en negro con **trama de puntos** en las sombras; luz
  cálida baja por un lado y **fluorescente frío** al fondo (HDRI
  [mosaic_tunnel](https://polyhaven.com/a/mosaic_tunnel)).
- **Lámina 2**: la misma pared, **diez pegatinas** «HELLO my name is»,
  una por etiqueta, con su línea corta (tabla de §0). La de **Resuelto**
  con una ✓ pintada con espray encima; la de **Efectos**, con **glitch**
  (Rubik Glitch).

### Concepto B — «Sus dibujos» (Gwen en el cuarto de Miles)

- **Objeto y sitio**: el **cuarto de Miles** en casa de sus papás, con
  la pared **empapelada de dibujos** (ATSV 00:46:17 a 00:46:48). En
  Blender: papeles clavados con chinchetas y cinta (se curvan y hacen
  sombra), corcho, un escritorio con **un cómic abierto impreso con
  desfase**, flexo, el juguete «de colección» en su caja (00:46:26).
  Papel: [Paper 001](https://ambientcg.com/view?id=Paper001).
- **Personaje**: **Gwen**, la más votada en IMDb, **mirando los
  dibujos** (pose 6 de Gwen: «They're good. Wow, there's so many.»).
  Miles pequeño al lado, **abochornado** (pose 9 de Miles).
- **Cómo habla**: Gwen en **caja amarilla**: **«Están buenos. ¡Cuántos
  hay!»** (mía). Miles, en otra caja más pequeña y torcida: **«Lo
  terminado, a la galería.»**
- **Dónde va cada texto**:
  - En el escritorio, **un cómic cerrado** con portada: título
    **EDICIÓN** (Anton o Saira Extra Condensed), subtítulo **Vídeo y
    arte**, y el número «#1» con precio, como un cómic de verdad (la
    etiqueta **Portada** hecha objeto).
  - Clavados en la pared, **cinco dibujos**, cada uno con su rótulo:
    **Montaje** (una tira de fotogramas), **Subtítulos** (un fotograma
    con subtítulo), **Miniaturas** (un cuadrito de vídeo), **Portadas**
    (una portada de disco), **Diseño** (bocetos de un logo).
  - Un pósit amarillo en el corcho: **Un hilo por cosa**.
  - Caja de Gwen y caja de Miles (arriba).
  - Tarjeta pequeña: **Aquí, el proceso y las dudas** ⚠️.
- **Para que no quede plano**: **luz de atardecer** por la ventana que
  cruza la pared en diagonal; el **flexo** encendido; en primer plano, el
  **bote de lápices** y la caja del juguete **desenfocados con desfase
  de tintas**; los papeles **se levantan** del corcho y proyectan
  sombra.
- **Lámina 2**: el **cómic abierto**, doble página: **diez viñetas**,
  una por etiqueta, cada una con su caja amarilla. La viñeta de
  **Efectos**, con glitch; la de **Montaje**, partida en tres como las
  viñetas partidas de la película.

### Concepto C — «El fanzine de Hobie» (Spider-Punk)

- **Objeto y sitio**: una **pared de carteles punk** fotocopiados, como
  el «club punk ilegal» de Tierra-138 (§5.1): capas de carteles con
  grapas, cinta, bordes rotos; un **fanzine** grapado colgado de un
  clavo. En Blender: planos de papel con desplazamiento, grapas, cinta
  ([Cardboard Set 001](https://ambientcg.com/view?id=CardboardSet001)
  para cartones), **la guitarra** de Hobie apoyada (modelo por buscar ⚠️).
- **Personaje**: **Hobie**, el favorito de las redes. Pose 1 (entra
  con la guitarra a la espalda, 01:09:58) o pose 2 (con el aparato
  arrancado de la pared, «It's propaganda, bruv», 01:22:26): **apoyado
  en la pared, de lado, sin mirar**.
- **Cómo habla**: **letras recortadas de revista** (mezcla de Archivo
  Black, Bowlby One, Bungee, Anton y Special Elite, cada una en su
  papelito). Su frase, que es el chiste perfecto para un foro con
  etiquetas: **«Odio las etiquetas.»** (de «I hate labels», ATSV
  01:10:49) y debajo, en otra tira: **«Aquí úsalas.»** (mía).
- **Dónde va cada texto**:
  - Cartel grande, letras recortadas: **EDICIÓN**.
  - Tira de máquina de escribir: **Vídeo y arte**.
  - A rotulador grueso sobre un cartel: **Un hilo por cosa**.
  - Cinco **flyers** pequeños: **Montaje**, **Subtítulos**,
    **Miniaturas**, **Portadas**, **Diseño**.
  - Pegatina: **Lo terminado se enseña en galería**.
  - Nota con imperdible: **Aquí, el proceso y las dudas** ⚠️.
- **Para que no quede plano**: **flash duro** como de fotocopiadora,
  sombras negras; un **imperdible** enorme en primer plano, fuera de
  foco y con desfase; los colores del fondo **cambian a saltos** de un
  cartel a otro (como Hobie); grano de fotocopia.
- **Lámina 2**: **el estuche de la guitarra lleno de pegatinas**, una
  por etiqueta. Encaja con el tono: Hobie «odia las etiquetas» pero las
  lleva todas pegadas.

### ¿Cuál primero?

1. **A**: el objeto (la pared) y el sitio (el túnel) son reales y salen
   en la película; el personaje es el principal y **pintar es su
   proceso**; y todo se hace en Blender con recursos CC0 y CC BY ya
   localizados.
2. **C**: el más original y el más querido por el fandom joven, pero
   pide **mucho trabajo de collage** y encontrar la guitarra.
3. **B**: muy bonito para «galería», pero depende de un fotograma del
   cuarto que **no he visto**.

**Idea descartada**: la **línea de tiempo de Lyla** (ATSV 01:26:34).
Parece una línea de tiempo de edición, pero es **un panel flotante**, y
eso no le gusta al dueño.

---

## 20 · Lo que no pude verificar

- **Todas las imágenes**: no bajé ninguna; no hay hojas de contacto.
- **Posturas** de §15: minuto ✅, postura de memoria ⚠️.
- **Color exacto** de las cajas amarillas y de los trajes (§5.3).
- **Estudio y director** de los dos doblajes latinos.
- **Frases del doblaje latino**: sólo «Es agüita» y «Sayonara», con una
  fuente cada una. El resto de frases de la lámina son **mías**.
- **Voces latinas** de Kingpin (Rubén Moya) y Pavitr (Tommy Rojas):
  una fuente cada una. **Papeles** de los *influencers*.
- **Fecha exacta** de *Beyond the Spider-Verse*: 4 o 18 de junio de 2027.
- **Títulos** de los temas de hip-hop de UNU (por la letra).
- Si el **espray del traje** en UNU ocurre entre 01:21:35 y 01:22:56
  (hueco sin diálogo) ⚠️.
- **Licencia** de tres modelos de Sketchfab (§4.1).
- El final de la descripción del canal («…aquí_») y qué es «galería».

---

## 21 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)

- curl bloqueado (000 / CONNECT rechazado): `spiderverse.fandom.com`,
  `doblaje.fandom.com` (API), impawards, AWN, Cartoon Brew, Sketchfab
  (web y API), Poly Haven (web y API), ambientCG, TextureCan, Blambot,
  Fonts In Use, dafont, sonypictures.com, fxguide, No Film School,
  1001 Fonts, Font Squirrel, The Cutting Room Floor, Game UI Database,
  Deadline (el guion de ATSV en PDF).
- WebFetch bloqueado: disneylatino.com, viernesmagazine.com.mx,
  infobae.com, beforesandafters.com.
- GitHub responde: `raw.githubusercontent.com`, `git clone`, y la
  búsqueda de código y de repositorios por la herramienta de GitHub.
- Por eso **no hay `hojas/`** y no corrí `investigar_serie.py`.

### Búsquedas web (50)

| # | Idioma | Búsqueda (dominio si lo hubo) |
|---|---|---|
| 1 | ES | Spider-Man: Un nuevo universo doblaje latino reparto Miles Morales voz actor director de doblaje |
| 2 | ES | «A través del Spider-Verso» doblaje latino voces Miguel O'Hara Hobie Gwen Peter B. Parker |
| 3 | ES | Spider-Verso doblaje latino Hobie Spider-Punk «Alondra Hidalgo» «José Luis Rivera» «Miguel Ángel Ruiz» Pavitr Jessica Drew |
| 4 | ES | «Un nuevo universo» «Emilio Treviño» «Alondra Hidalgo» «Miguel Ángel Ruiz» estudio dirección Kingpin Spider-Ham |
| 5 | ES | frases doblaje latino «salto de fe» «cualquiera puede usar la máscara» |
| 6 | EN | chromatic aberration, misregistration, Ben-Day, Justin Thompson |
| 7 | EN | Hobie collage zine frame rates; Gwen Earth-65 watercolor |
| 8 | EN | yellow caption boxes, thought boxes, lettering typeface |
| 9 | EN | título, logo, tipografía (fontsinuse, typeroom, itsnicethat, artofthetitle, fontinlogo, dafont) |
| 10 | EN | personaje más popular, encuesta, Hobie, Miguel |
| 11 | EN | Hobie fan favorite, TikTok edits, spin-off |
| 12 | ES | «Garibay» Hobie doblaje latino |
| 13 | ES | Javier Ibarreche la Mancha; Juan Guarnizo; Alex Montiel |
| 14 | EN | impawards, pósters de personaje de ATSV |
| 15 | EN | Lyla, sede de la Spider-Society, Nueva York 2099, paleta |
| 16 | EN | diseño de Hobie, Jamie Reid, Sex Pistols, Kris Anka |
| 17 | EN | «canon event» meme, Know Your Meme, Miguel |
| 18 | EN | Preston Mutanga, LEGO, Blender |
| 19 | EN | bote de espray CC BY (sketchfab.com) |
| 20 | EN | cómic abierto o Miles Morales (sketchfab.com) |
| 21 | EN | tráileres oficiales (youtube.com) |
| 22 | EN | *Beyond the Spider-Verse*, fecha, primer vistazo |
| 23 | EN | Daniel Pemberton; «Sunflower»; «What's Up Danger» |
| 24 | EN | traje a doses en *Miles Morales*; Fortnite; *Spider-Man 2* |
| 25 | EN | traje de Miles (Jordan, sudadera) y de Gwen |
| 26 | EN | diseño de Miguel; Peter B. y Mayday |
| 27 | EN | logos de Columbia con glitch; cajas de narración de Gwen |
| 28 | EN | paletas hex (schemecolor, color-hex) |
| 29 | ES | estudio y director del doblaje latino |
| 30 | JA | スパイダーバース 人気キャラ ランキング ホービー 吹き替え 声優 |
| 31 | ZH | 蜘蛛侠：纵横宇宙 蜘蛛朋克 霍比 人气 最受欢迎 角色 投票 |
| 32 | EN | encuesta de personaje favorito con porcentajes |
| 33 | ES | «José Luis Rivera» Miguel O'Hara |
| 34 | ES | frases de Spider-Punk en latino, modismos |
| 35 | ES | «Emilio Treviño» entrevista |
| 36 | ES | tutorial efecto Spider-Verse CapCut After Effects |
| 37 | EN | libro de arte de ATSV, Ramin Zahed |
| 38 | EN | texturas CC0 papel, hormigón, cartón (polyhaven, ambientcg) |
| 39 | EN | ladrillo, yeso; HDRI de túnel y ciudad de noche (polyhaven) |
| 40 | EN | fan art de Hobie y Miles (artstation.com) |
| 41 | EN | fondos de pantalla 4K |
| 42 | EN | regla de no poner cajas antes de la picadura |
| 43 | EN | disco de ATSV (Metro Boomin) y partitura |
| 44 | EN | pegatinas «Hello my name is» de Miles |
| 45 | EN | Tierra-65, acuarela, «anillo del humor» |
| 46 | ES | tráiler doblado latino (youtube.com) |
| 47 | KO | 스파이더맨 어크로스 더 유니버스 스파이더 펑크 호비 인기 |
| 48 | EN | película de Spider-Punk, Daniel Kaluuya |
| 49 | ES | «es agüita» Spider-Ham |
| 50 | EN | *making of* y análisis de estilos (youtube.com) |

### GitHub (sin cupo)

- Búsqueda de código `"let's do this one last time" "Miles Morales"
  extension:srt` → **6 archivos**. Usé dos:
  [Bisbilge/subtitles](https://github.com/Bisbilge/subtitles) (UNU,
  1851 líneas) y
  [sydney-machine-learning/sentimentanalysis-Hollywood](https://github.com/sydney-machine-learning/sentimentanalysis-Hollywood)
  (ATSV, 2000 líneas). El tercero, de
  [PrayerVoid/color_of_movies](https://github.com/PrayerVoid/color_of_movies),
  no lo usé; de ese repositorio saqué el **código de barras de color** y
  el JSON de UNU (§5.2).
- Tres búsquedas de subtítulos **en español** («araña radiactiva»,
  «salto de fe»): **0 resultados**.
- Búsqueda de repositorios «spiderverse»: los shaders de §4.4.
- [google/fonts](https://github.com/google/fonts): 31 familias
  revisadas con fontTools.
- Todo quedó en mi carpeta temporal, **no en el repositorio**.

### Fuentes consultadas por tipo

- **Oficiales**: X @SpiderVerse, TikTok @sonypicturesanimation y
  @spiderversemovie, vídeo «Beyond The Screen» de Sony, Devastudios,
  web de Kris Anka, libros de Ramin Zahed (fichas), Apple Music.
- **Entrevistas al equipo**: Justin K. Thompson (Cartoon Brew, fxguide),
  Christopher Miller (Looper, CBR), Kris Anka y animadores de Hobie
  (befores & afters, Variety, SlashFilm, Cartoon Brew), Dean Gordon y
  Pav Grochola (Screen Rant, hilo oficial), Daniel Pemberton (Rolling
  Stone, The Credits, Screen Rant), @chuwenjie (Tumblr).
- **Otros idiomas**: japonés (Eiga.com, Cinema Today, Animate Times),
  chino (Beijing News, Gcores, Zhihu, Douban), coreano (NamuWiki,
  ExtremeMovie, brunch).
- **Wikis**: Doblaje Wiki (sólo extractos del buscador), Into the
  Spider-Verse Wiki, Marvel's Spider-Man Wiki, DubDB, NamuWiki.
  TV Tropes, Wikipedia, Wayback Machine: bloqueados.
- **Foros y comunidades**: foro de dafont, Know Your Meme, The Tab,
  TikTok (Discover). Reddit y Arctic Shift: bloqueados.
- **Arte**: ArtStation, Tumblr, Wallpaper Abyss, Pinterest (sólo como
  pista).
- **Vídeo**: YouTube (sólo títulos y enlaces), TikTok.
- **Código y recursos**: GitHub (subtítulos, shaders, código de barras),
  Sketchfab, Poly Haven, ambientCG, google/fonts.
- **Doblaje latino**: Doblaje Wiki, SensaCine, 3DJuegos, Infobae, El
  Financiero, La Razón, SinEmbargo, La Crónica, UnoTV, YouTube,
  Facebook, TikTok.

### Lo que NO encontré

- Imágenes descargadas y hojas de contacto (red cerrada).
- **Estudio y director** del doblaje latino de las dos películas.
- Frases latinas de «Anyone can wear the mask», «leap of faith», «I hate
  labels», «I'm gonna do my own thing».
- Subtítulos en español (latino o de España) con tiempos.
- Una **encuesta oficial** de popularidad (no existe).
- La **letra exacta** del logo y de las cajas.
- Un complemento de **Blender** para el estilo Spider-Verse.
- Un modelo 3D libre de **guitarra** para el concepto C (no lo busqué).
- Cajas de diálogo en los videojuegos (no las hay propias).
- The Cutting Room Floor y Wayback Machine: bloqueados.
- El guion oficial de ATSV (está en Deadline, bloqueado).
