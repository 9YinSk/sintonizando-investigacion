---
tags: [biblia, serie, laminas]
serie: "Rick and Morty"
canal: "#noticias-series"
fecha: 2026-09-24
---

# Biblia · Rick y Morty — para #noticias-series

> [!important] Cómo se hizo, y sus límites
> - **Segunda pasada, 25-sep-2026, con la red abierta** (lo de abajo es
>   la primera, del 24-sep). Se usaron: la API de Fandom (wiki de la serie
>   y Doblaje Wiki), `investigar_serie.py` (**3 hojas de contacto** en
>   `hojas/`, §3A), la API de Sketchfab (licencias), Arctic Shift
>   (Reddit), Fontsource + fontTools, `yt-dlp` para metadatos y
>   `fotogramas.py` sobre **Dailymotion e Internet Archive** (YouTube
>   pedía iniciar sesión): 8 vídeos mirados, entre ellos el «Style
>   Guide». Lo nuevo va marcado «segunda pasada» y está resumido justo
>   debajo. Las notas de trabajo, en `partes/`.
> - **Primera pasada, 24-sep**: la red de esta sesión estaba cerrada. Fandom (el wiki de la serie y
>   Doblaje Wiki), Wikipedia, YouTube, Reddit, Arctic Shift, ANMTV,
>   Bubbleblabber, tvwriting.co.uk, rickandmortyapi.com, la API de
>   Sketchfab y videogaming3d daban **403** por curl o por WebFetch.
>   Por eso **no se pudo correr** `herramientas/investigar_serie.py`:
>   **no hay hojas de contacto** ni carpeta `hojas/`.
> - Mi fuente principal fue la **búsqueda web** (la lista está al final, en
>   la bitácora). Los datos que sólo vi en el resumen de un buscador van
>   con ⚠️.
> - **GitHub sí respondía**, y de ahí salió lo más útil:
>   - **Subtítulos en inglés con sus tiempos** de las temporadas 1, 2 y 3
>     (hasta el 3×06) y del 4×01, en dos repositorios:
>     [alexlyzhov/sphere-neural](https://github.com/alexlyzhov/sphere-neural/tree/master/10_nlp/sub)
>     (Blu-ray y HDTV de la T1 y el principio de la T2) y
>     [lucas-dclrcq/ifi-atelier-spark](https://github.com/lucas-dclrcq/ifi-atelier-spark/tree/master/src/main/resources/data/rickandmorty)
>     (Addic7ed, del 1×01 al 3×06). Con ellos doy **el minuto de cada
>     escena**. Es el minuto de ese archivo: puede moverse uno o dos
>     segundos según la versión (lo comprobé: «Nobody exists on purpose» está
>     en 18:01 en el Blu-ray y en 17:59 en la de TV).
>   - **Fotogramas de la serie** (300×300) del repositorio de
>     [The Rick and Morty API](https://github.com/afuh/rick-and-morty-api/tree/master/images):
>     de ahí **medí los colores** de cada personaje (hex, ±5 por canal).
>   - Las **letras**: la del logo («Get Schwifty», de un repositorio de
>     fans) y las libres de [google/fonts](https://github.com/google/fonts).
>     Comprobé una a una, con fontTools, si traen á é í ó ú ñ ¿ ¡.
> - **Cómo leo los episodios**: «1×08» es temporada 1, episodio 8. El
>   minuto va así: 18:01.
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su minuto,
>   o lo medí yo en un archivo. ⚠️ **dudoso**: una sola fuente, o lo
>   describo de memoria. Lo de memoria siempre va marcado.
> - Las frases en **inglés** salen del subtítulo. Su versión en **español
>   latino** sólo va como cita cuando encontré una fuente; si no, la marco
>   como **traducción mía**.

---

## Segunda pasada · qué cambió

_(pendiente: se rellena en esta segunda pasada)_

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección 📡 NOTICIAS):

> **ıı・🍿・noticias-series** (texto) · 1 fijados · 0 de personas en los
> últimos 15 — _Series y cine: estrenos, temporadas y doblajes. Para
> comentar, abre un hilo._

Función según el encargo: **noticias de series con su debate**.

Su canal hermano es **ıı・📰・noticias-anime** («Anime: estrenos,
temporadas y doblajes. **Lo trae un bot.** Para comentar, abre un hilo
en la noticia»). En #noticias-series el inventario **no dice** que lo
traiga un bot. No lo pongo en la lámina hasta que el dueño lo confirme.

Y hay un canal con el que no hay que confundirlo:
**ıı・📺・que-estas-viendo** («lo que estás viendo y si lo recomiendas»).
La lámina tiene que dejar claro que aquí van **noticias**, y que la
charla va **en un hilo**.

### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Noticias de series** | nombre del canal |
| 2 | **Series y cine** | de qué va |
| 3 | **Estrenos** | bloque 1 |
| 4 | **Temporadas** | bloque 2 |
| 5 | **Doblajes** | bloque 3 |
| 6 | **¿Quieres opinar? Abre un hilo** | cómo se comenta |
| 7 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

### Lámina 2 (sólo si el dueño la quiere)

La lámina 1 cabe con esos 7 textos. Si el dueño quiere explicar **cómo se
abre un hilo** paso a paso, no cabe: propongo **lámina 2** con los pasos
de Discord (pasar el ratón por la noticia, «Crear hilo», ponerle nombre).
Idea para el dibujo: **el mando a distancia de la tele**, con un botón por
paso (ver §19). No invento reglas del canal: los pasos exactos los tiene
que confirmar el dueño.

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué Rick y Morty encaja | Tiene **su propio canal de noticias**: el **cable interdimensional**, «TV infinita de universos infinitos» (1×08, 1:00) ✅. Dentro salen **noticiarios de verdad**: «Opposite News with Michael Thompson» (2×08, 12:29) ✅, dos **«Breaking news»** (1×08, 19:09 y 2×08, 19:30) ✅, y el parte del tiempo de «Hamster in Butt World» (1×08, 21:20) ✅. Y la familia **siempre lo comenta en el sofá**: es el «debate». |
| El objeto | **La tele de los Smith con la caja del cable interdimensional**. Rick la abre y le mete un **cristal de xantenita** que «conduce electrones entre dimensiones» (1×08, 0:30) ✅. En Blender: tele, caja, cristal y mando. Hay tele libre CC0 en [Poly Haven](https://polyhaven.com/a/Television_01). |
| Cuadro de diálogo propio | La serie **no usa globos**. Su texto en pantalla es **el rótulo de la tele**: el nombre y el eslogan «abajo de la pantalla» (lo dice el vendedor de Puertas Falsas, 1×08, 11:18) ✅, la **cartela del programa** y la franja de **«Último momento»**. Y en los cómics de Oni Press, globo clásico ⚠️. |
| Quién habla | **Rick** con el mando (el que trae la señal) y **Morty** a su lado. El secundario más querido para este canal: **Pepinillo Rick** (3.º en Ranker, detrás de Rick y Morty ⚠️) o **el Sr. Meeseeks** (el meme de «¡Mírenme!») ⚠️. Para el «debate», **Summer** ✅ (ver §8). |
| Letras | Logo: **Get Schwifty** (gratis, de jonizaak) **no trae ni tildes, ni ñ, ni ¿ ¡, ni signos**: comprobado. Para títulos con tildes: **Creepster** (Google Fonts, sí las trae). Para el rótulo de noticias: **Anton** u **Oswald**. Todas comprobadas en el archivo. |
| Voz latina | Rick **Juan Guzmán** ✅, Morty **Eder La Barrera** ✅, Summer **Lileana Chacón** ✅. Doblaje venezolano de **IDS** ✅. Siguen en la temporada 9 (HBO Max, 25 de mayo de 2026) ✅. |
| Tono | Ciencia ficción **sucia y cínica**, pero **dibujada simple y amable**: línea negra gruesa, colores planos, sombras mínimas ⚠️. Mucho verde portal. |
| Dato de actualidad | La temporada 9 se anunció con «**No AI slop!** Just Grade A organic slop, made by real humans» ✅. Encaja con la regla del dueño: **que no parezca hecho por IA**. |

---

## 2 · Las escenas que sirven para #noticias-series (con minuto)

Todas salen de los subtítulos en inglés con tiempos (ver arriba). El
texto y el minuto están comprobados ✅. Lo que **se ve** en cada una
(postura, luz) lo describo de memoria ⚠️ salvo cuando lo digo: mira el
fotograma antes de usarlo.

### 2.1 «Rixty Minutes» (1×08): nace el cable interdimensional

En España se llamó «Sesenta Rick-nutos». La wiki en español lo titula
«Televisión Interdimensional» ✅ (segunda pasada: también en Doblaje Wiki,
«Rick y Morty/1.ª temporada»; el 2×08 es «Televisión interdimensional 2»)
([Wiki de Rick & Morty](https://wiki-de-rick-morty.fandom.com/es/wiki/Televisi%C3%B3n_Interdimensional)).

| Minuto | Qué pasa y qué se dice (inglés) | Para qué sirve |
|---|---|---|
| 0:04 | La familia ve un reality en la tele del salón. **Rick** ✅ (el subtítulo no dice quién; lo confirma el [transcript de la wiki](https://rickandmorty.fandom.com/wiki/Rixty_Minutes/Transcript), segunda pasada): «none of it mattered and the entire show was stupid» (0:19) | Abre con **la familia criticando la tele**: el debate |
| 0:21 | Jerry ✅ (subtítulo + transcript): «Okay, I've got an idea, Rick. You show us your concept of good TV, and we'll crap all over that» | El espíritu del canal: **enseña y se comenta** |
| 0:30 | Morty: «Is that crystallized xanthanite?» «It conducts electrons across dimensions» | **El cristal** que se mete en la caja: detalle para el objeto |
| 0:38 | Rick: «I just upgraded our cable package with programming from every conceivable reality» | La frase que explica el canal |
| 1:00 | Rick: «This is **infinite TV from infinite universes**» | **Lema posible** del canal |
| 1:13 | «Letterman from a timeline where Jerry's famous» | La tele trae **estrenos de otros mundos** |
| 2:38 | Rick: «Infinite timelines, infinite possibilities» | Otra frase de Rick |
| 3:37 | Anuncio de **Ants in My Eyes Johnson** | El anuncio más famoso ✅ |
| 5:56 | Tráiler de **«Two Brothers»** («It's in theaters now. Coming this Summer», 5:53) | Un **tráiler de estreno**: justo lo del canal |
| 9:59 | Anuncio de **Real Fake Doors** | El segundo más famoso ✅ |
| 11:18 | El vendedor: «That's our slogan. **See it on the bottom of the screen below our name.** Here's another slogan right below that one» | **El rótulo de abajo** es el cuadro de diálogo de esta serie (ver §7) |
| 11:39 | **Gazorpazorpfield** | Otro favorito del fandom |
| 16:00 | **Baby Legs** («Babylegs, you're a good detective») | Otro favorito |
| 18:01 a 18:06 | Morty a Summer: «Nobody exists on purpose. Nobody belongs anywhere. Everybody's gonna die. **Come watch TV.**» («Come watch TV» cae en 18:06) | **La frase más famosa del episodio** ✅. Invita a sentarse a ver y comentar |
| 19:09 | «**Breaking news**... Academy Award-Winning actor Jerry Smith is leading police on a slow-speed pursuit» | **Una noticia de última hora** dentro de la serie |
| 19:20 | Jerry: «It's my life, and we're watching it» | La familia comenta la noticia |
| 20:14 | Suena «Give me a name / Hear my faith…» (de **Mazzy Star**, que está en la banda sonora oficial ✅; el título, «Look On Down From The Bridge», de memoria ⚠️) | Música del momento triste |
| 21:20 | «Ha ha, **Hamster in Butt World Weather** is done, and now it's **sports time** coming up» | **Un noticiero con su tiempo y sus deportes**. Toda la familia junta ante la tele, preguntando cosas: el mejor «debate» |
| 21:45 | Rick: «I can't even hear the TV» | Rick harto de que comenten encima |

Nota: en la versión de TV (subtítulo de Addic7ed) la frase empieza en
**17:59** y «Come watch TV» cae en **18:03**; en el Blu-ray, en
**18:01** y **18:06**.

### 2.2 «Interdimensional Cable 2: Tempting Fate» (2×08): la secuela

| Minuto | Qué pasa y qué se dice (inglés) | Para qué sirve |
|---|---|---|
| 0:54 | En la **sala de espera** de un hospital alienígena. Rick: «Well, this won't do.» Morty: «What are you doing?» Rick: «**A sequel.**» | Rick **conecta su aparato a otra tele** (chispas en 1:13) |
| 1:01 | Rick: «We pretty much nailed it the first time» | Humor de secuela |
| 1:23 | «**Man vs. Car**, the newest hit show» | Un **estreno** anunciado |
| 2:35 | Anuncio de **Eyeholes** | Otro anuncio famoso |
| 5:53 | «Calling all **Jan Michael Vincents**» y el tráiler de «**Jan Quadrant Vincent 16**» (6:42) | Otro tráiler de estreno |
| 7:23 | «Hey, I'm **Stealy**» | Otro favorito |
| 8:03 | «We got a **plumbus**» | Presenta el plumbus |
| 12:29 | Locutor: «It's the **opposite news with Michael Thompson**». Michael: «Hey, everybody. It's me, Michael Thompson. Today the pope didn't get killed» | **Un noticiero**. El presentador (**Michael Thompson**) sale con **papeles en la mano, traje azul oscuro y corbata**, sobre fondo azul grisáceo: lo vi en el fotograma [225.jpeg](https://raw.githubusercontent.com/afuh/rick-and-morty-api/master/images/225.jpeg) ✅ |
| 12:44 | Morty: «why is his body, like, sloping off to the right side of the screen?» | El presentador está **torcido**: es media pareja |
| 12:52 | «Welcome to "**cooking things**." I'm **Pichael Thompson**» | Su **siamés**, cocinero ([264.jpeg](https://raw.githubusercontent.com/afuh/rick-and-morty-api/master/images/264.jpeg)) |
| 13:10 | Michael: «You quit tugging. **I'm in the middle of my news.**» | Chiste perfecto para un canal de noticias |
| 13:27 | Summer: «**I don't want to be that girl, but** maybe there would be less conflict if they didn't shoot their shows at the same time» | **Summer opinando**: el tono del debate |
| 14:52 | «Today on "**How They Do It**"... **Plumbuses**» | El plumbus explicado |
| 16:49 | «Tune in next week to the best show ever… "**The Personal Space Show**"» | Anuncio de **próximo episodio** |
| 19:05 | Summer: «Does all interdimensional TV have to rely on juvenile violence?» y **Morty le contesta con un discurso** (19:08 a 19:23) | **El debate** sobre lo que se ve en la tele |
| 19:30 | «**Breaking news.** Shrimply Pibbles is being held hostage» | Otra **última hora** |

### 2.3 Los personajes del plan, con su minuto

| Personaje | Escena | Minuto | Frase (inglés) |
|---|---|---|---|
| **Sr. Meeseeks** | 1×05, Rick presenta la caja | 2:31 | «This is a **Meeseeks Box**. Let me show you how it works. You press this.» |
| | primer Meeseeks | 2:35 | «**I'm Mr. Meeseeks! Look at me!**» |
| | cumple y desaparece | 2:43 | «The Meeseeks fulfills the request.» «**All done!**» (2:44) |
| | Rick avisa | 2:52 | «Just keep your requests simple. They're not gods.» |
| | «Can do!» | 3:31 | «Ooh, yeah! **Can do!**» |
| | el discurso | 16:42 | «**Existence is pain** to a Meeseeks, Jerry.» |
| **Pepinillo Rick** | 3×03, sobre el banco del garaje | 0:23 | Rick: «**Flip the pickle over.**» |
| | la revelación | 0:34 | «**Boom! Big reveal... I'm a pickle.**» |
| | el grito | 0:55 | «**I'm Pickle Rick!**» |
| | con Morty | 1:38 | «I don't do magic, Morty, I do science.» |
| **Rick** | 1×11, Birdperson lo explica | 18:22 | «Wubba lubba dub dub» significa «**I am in great pain. Please help me.**» |
| | 2×05, la cabeza gigante | 0:32 | «**Show me what you got.**» |
| | 2×05, la canción | 5:54 | «You gotta **get schwifty**» |
| | 3×01, la salsa | 5:03 | «a bunch of the **Szechuan sauce**» |
| **Mr. Poopybutthole** | 2×10, la escena final | 22:01 | «Hi, I'm Mr. Poopybutthole from episode 204» |

### 2.4 Segunda pasada: escenas miradas en vídeo (25-sep-2026)

YouTube pedía iniciar sesión. Los clips se miraron en **Dailymotion** e
**Internet Archive** con `fotogramas.py` (cada 2-6 s, hojas miradas con
Read). 7 vídeos, unos 7,5 minutos. Detalle en `partes/video.md`.

| Vídeo | Minuto | Qué se ve | Para qué |
|---|---|---|---|
| [Intro (viñeta previa al título)](https://www.dailymotion.com/video/x8x2x8y?t=8) | 0:08 | Rick **arrastra a Morty del brazo** por un planeta árido | Pose de «vamos» |
| [La misma](https://www.dailymotion.com/video/x8x2x8y?t=32) | 0:32 | Tarjeta «RICK AND MORTY», **cursiva turquesa sobre negro** | El logo real |
| [Clip Meeseeks, 1×05](https://www.dailymotion.com/video/x7xeqwl?t=16) | 0:00-0:18 | Rick **levanta la caja con una mano**; el Meeseeks sale **brazos arriba, dedos abiertos** | Confirma la pose de «Look at me!» ✅ |
| [Meeseeks y el golf, 1×05](https://www.dailymotion.com/video/x8bmk63?t=70) | 1:00-1:25 | La sala **llena de Meeseeks** gritando, pared marrón anaranjada | El caos de «Existence is pain» |
| [Promo de «Televisión interdimensional 2»](https://www.dailymotion.com/video/x3jf16p?t=8) | 0:08 | **Sala de espera** del hospital espacial: fondo azul marino estrellado, monitor turquesa | Resuelve «luz de hospital, de memoria» ✅ |
| [La misma](https://www.dailymotion.com/video/x3jf16p?t=20) | 0:20-0:22 | **Portal verde lima** y tarjeta «Next Sunday @ 11:30p» | Color del portal medido (§5) |
| [Promo «Pickle Rick»](https://www.dailymotion.com/video/x5ve1xh) | 0:02 | Morty **inyecta el suero** al pepino **sobre el banco** | Confirma el banco del garaje (3×03, 0:20) ✅ |
| [Tráiler T1, Turner](https://archive.org/details/turner_video_391819) | 1:12 | **Rick, Beth y Summer con armas en alto**, dentro de casa | Pose de grupo |
| [El mismo](https://archive.org/details/turner_video_391819) | 1:36 | Créditos: Sarah Chalke, Chris Parnell, Spencer Grammer; música de **Ryan Elder** | Confirma reparto y compositor ✅ |
| [Tráiler T9 subtitulado, HBO Max](https://www.dailymotion.com/video/xae2lba?t=51) | 0:51 | Tarjeta «**NUEVA TEMPORADA 25 DE MAYO**», **morada** con rayos | Noticia real en español para el canal |

Y del transcript de la wiki: en **21:45** del 1×08 Rick dice «All right,
that's it» **y saca la pistola de portales** ✅ (nueva pose, §15).

---

## 3 · Arte oficial y referencias visuales

> [!warning] No pude bajar ni mirar el arte oficial
> Fandom, Adult Swim, el pressroom de Warner y las webs de prensa daban
> 403. Las URLs de abajo **salieron en mis búsquedas**; lo que cuento de
> cada una es lo que dice el resultado, no lo que vi. Lo único que **sí
> vi** son los fotogramas de §3.1.

### 3.1 Fotogramas de la serie que sí vi (300×300) ✅

Salen del repositorio de [The Rick and Morty API](https://github.com/afuh/rick-and-morty-api/tree/master/images)
(licencia BSD del código; las imágenes son **fotogramas de la serie**,
© Adult Swim: sólo referencia). Cada una se abre así:
`https://raw.githubusercontent.com/afuh/rick-and-morty-api/master/images/<n>.jpeg`
(comprobado: responde 200). El nombre de cada número lo saqué del
[JSON completo de la API](https://github.com/rieger-jared/rick-and-morty-api/blob/main/internal/data/characters.json).

**Los del cable interdimensional** (la API los agrupa en el sitio
«Interdimensional Cable»):

| N.º | Quién | Qué se ve | Para qué |
|---|---|---|---|
| 225 | **Michael Thompson** | Presentador de noticias con **papeles en la mano**, sonrisa de dientes, traje azul oscuro, fondo de plató azul grisáceo | **El presentador del noticiero**: pose para «dar la noticia» |
| 264 | **Pichael Thompson** | Su siamés, cocinero con gorro y delantal, cara de sorpresa | Chiste de fondo |
| 277 | **Vendedor de Real Fake Doors** | Brazos abiertos, **puertas de colores detrás**, gorra roja y tirantes | Pose de «¡miren esto!» |
| 184 | **Jon** (Gazorpazorpfield) | Lee un **periódico que dice «NEWS»**, taza al lado | Un **periódico** dentro de la serie |
| 20 | Ants in My Eyes Johnson | Ojos llenos de hormigas, camisa amarilla y corbata roja | Meme del fandom |
| 410 | Two Brothers | Los dos hermanos | Tráiler de estreno |
| 29 / 279 / 417 | Baby Legs, Regular Legs y el jefe | La serie de policías | Otro favorito |
| 136 | Gazorpazorpfield | El gato naranja enfadado | Otro favorito |
| 409 | Mr. Sneezy | Al volante de su coche rojo | Anuncio |
| 408 | Presentador de «Quick Mystery» | — | Programa |
| 266 | Piece of Toast | La tostada con mantequilla del «SNL» | Chiste visual |
| 334 | Stealy | — | 2×08 |
| 460 | **Periodista traflorkiano** (2×08) | Alien celeste con **sombrero de reportero, chaleco y micrófono**, **levanta la mano para preguntar**, rodeado de otros periodistas | **La rueda de prensa**: la pose de «abrir un hilo» |
| 321 | Shrimply Pibbles (2×08) | En silla de ruedas, bata granate | La «noticia» del 2×08 |

**Los principales** (para poses, ver §15):

| N.º | Quién | Qué se ve |
|---|---|---|
| 1 | Rick | Busto, párpados a media asta, ceja fruncida, **dientes y baba**, bata blanca |
| 290 | Rick | Tres cuartos, cansado, boca abierta, apoyado en una mesa |
| 631 | Rick | **Enseña un objeto dorado en la palma de la mano**, luz cálida |
| 353 | Tiny Rick | **Manos arriba**, cuerpo de adolescente |
| 2 | Morty | De pie, **mira hacia arriba, preocupado**, brazos caídos |
| 630 | Morty | **Palma hacia arriba, explicando**, dientes a la vista |
| 232 | Morty | Desayunando con tenedor |
| 118 | Evil Morty | Parche en el ojo, mirada de lado |
| 3 | Summer | **Brazos cruzados**, cara de fastidio, junto a la nevera |
| 339 | Summer | **Brazos abiertos, boca abierta**: protesta en la mesa del desayuno |
| 629 | Summer | De pie en la cocina, sorprendida |
| 242 | Sr. Meeseeks | De pie, **sonriendo**, brazos largos y sueltos, junto a un cuadro de mariposa |
| 524 | Meeseeks marca Kirkland | Rosa, sentado |
| 265 | Pepinillo Rick | Dentro de su **traje de ratas**, **brazos arriba, gritando** |
| 244 | Mr. Poopybutthole | Cae de espaldas con **un dedo arriba**, pizza volando |

Evitar el 293 (Rick muerto) y el 234 (Morty muerto): son los cadáveres
del 1×06, no sirven para una lámina amable.

### 3.2 Arte oficial que existe (enlaces vistos en búsquedas)

| Qué | Dónde | Nota |
|---|---|---|
| **Key art** oficial de Adult Swim | [Pressroom de WBD](https://press.wbd.com/us/image/adultswimrickandmortykeyart-0) | ⚠️ no abrí la página |
| **Póster de la temporada 9** (Rick «con la cabeza muy grande») | [Deadline, galería](https://deadline.com/gallery/rick-and-morty-season-9-photos-adult-swim/) · [TheWrap](https://www.thewrap.com/creative-content/tv-shows/rick-and-morty-season-9-premiere-photos/) · [Bleeding Cool](https://bleedingcool.com/tv/rick-and-morty-and-you-thought-rick-had-a-big-head-before-season-9/) · [Cartoon Base en X](https://x.com/TheCartoonBase/status/2046986095577923870) | Primeras imágenes y póster, abril de 2026 ✅ (varias fuentes) |
| **Arte de producción de la T9**: Rick luchador, **Summer olímpica con medalla**, **Morty con cabeza de tele** («TV Head Morty»), Jerry ejecutivo, Randy loco, Reese y Seb; y una docena de fondos (bolera, valle brillante, cabaña con ranchera) | [Rick and Morty en X](https://x.com/RickandMorty/status/2046243740625347012?lang=en) · [Bleeding Cool](https://bleedingcool.com/tv/rick-and-morty-season-9-preview-wrestler-rick-tv-head-morty-more/) | ✅ (dos fuentes). **Morty con cabeza de tele** es oro para un canal de noticias |
| **Hoja de modelo temprana** | [Adult Swim en Facebook](https://m.facebook.com/adultswim/photos/a.10152113418021745.1073741833.67985126744/10152113418381745/) | ⚠️ |
| **Vídeo oficial «Rick and Morty Style Guide»**: el director de arte **Jeffrey Thompson** explica lo que se hace y lo que no al dibujarlos (3 de octubre de 2018) | [adultswim.com](https://www.adultswim.com/videos/rick-and-morty/rick-and-morty-style-guide) · [YouTube 8c4hAsobciA](https://www.youtube.com/watch?v=8c4hAsobciA) | ✅ existe (dos fuentes). **Visto en la segunda pasada** en su copia de [Internet Archive](https://archive.org/details/rick-and-morty-style-guide), 2:42: lo que enseña está en §18A |
| Guía de estilo para Adult Swim de **Sangho Bang** | [Behance](https://www.behance.net/gallery/90220333/Rick-and-Morty-Style-Guide) | ⚠️ |
| **The Art of Rick and Morty, vol. 2** (Dark Horse): temporadas 3 y 4, 216 páginas, con arte de Justin Roiland, **James McDermott**, **Jason Boesch**, Carlos Ortega y Andrew DeLange | [Dark Horse](https://www.darkhorse.com/Books/3006-618/The-Art-of-Rick-and-Morty-Volume-2-HC) · [Barnes & Noble](https://www.barnesandnoble.com/w/the-art-of-rick-and-morty-volume-2-jeremy-gilfor/1137831704) | ✅. Hay un vol. 1 (temporadas 1 y 2) ⚠️ de memoria |
| Recopilación del arte | [Character Design References](https://characterdesignreferences.com/art-of-animation-9/art-of-rick-and-morty) | ⚠️ |
| Los cuadernos del director de arte **James McDermott** | [It's Nice That](https://www.itsnicethat.com/features/inside-rick-and-morty-art-director-james-mcdermotts-sketchbooks-250717) | Dice que el dibujo mezcla **lo ingenuo, lo familiar y lo amable con lo macabro**, y que hasta lo más oscuro tiene algo de **comedia o rareza** ✅ (resumen de búsqueda). Las escenas pasan por el **equipo de color** y se animan en **Bardel** (Vancouver) |
| Sprites de **Pocket Mortys** | [The Spriters Resource](https://www.spriters-resource.com/mobile/pocketmortys/) | ⚠️ no abrí |

### 3.3 Lo que falta ⚠️

- **Fotogramas en 1080p** de 1×08 y 2×08: siguen sin bajar (YouTube pide
  iniciar sesión). Los minutos de §2 dicen **dónde** parar el vídeo. Hay
  que sacarlos en el PC. **Segunda pasada**: sí hay ya **fotogramas de
  1920×1080** de la wiki (sobre todo del 3×03, «Pickle Rick») en las hojas
  de contacto (§3A), y clips de 1280×720 del 1×05, del 2×08 y de los
  tráileres (§2.4).
- **Segunda pasada, arte nuevo con autor**: la [hoja de modelo de
  Morty](https://static.wikia.nocookie.net/rickandmorty/images/9/9e/Morty_model_sheet.jpg)
  de Starburns Industries (9796×4482) y el arte de producción del 3×03
  (Tommy Scott, Corey Booth, Justin Noel, Brianne Neumann): hojas 1 y
  193-220 (§3A) ✅. El pressroom de WBD y el Behance de Sangho Bang siguen
  dando 403 (dos intentos, sin copia en Wayback) ⚠️.
- **La caja del cable**: no la he visto. Sé por el subtítulo que Rick la
  abre y le mete el cristal (0:30) y por la wiki que la vuelve a
  **conectar a la tele** ⚠️. Su forma exacta, sin comprobar.

---

## 3A · Las hojas de contacto (qué número sirve)

Tres hojas en `hojas/`, montadas con `herramientas/investigar_serie.py`
sobre la wiki de Fandom (220 imágenes en 5 hojas; elegí 3 y **las miré
con Read**). El número es el del recuadro amarillo. Cada imagen lleva
debajo su tamaño real y su nombre de archivo en la wiki. Los originales
están en `static.wikia.nocookie.net` (piden la cabecera
`Referer: https://www.fandom.com/`).

### `personajes_01.jpg` (números 1-48) · personajes y poses variadas

| N.º | Qué es | Tamaño | Para qué |
|---|---|---|---|
| **1** | [Hoja de modelo oficial de Morty](https://static.wikia.nocookie.net/rickandmorty/images/9/9e/Morty_model_sheet.jpg) (Starburns Industries): giro completo y 7 poses, con Rick en línea a la izquierda | 9796×4482 | **Proporciones exactas** de Morty. Base para el 3D o para calcar la silueta |
| **2** | [Póster promocional de «Pickle Rick»](https://static.wikia.nocookie.net/rickandmorty/images/f/fe/S3e3_Peter_Slavik_promo.jpg), de Peter Slavik | 1920×2898 | **Arte promocional vertical** con logo: ejemplo de portada con acción y láser |
| **3** | [Rick con un aparato en la mano](https://static.wikia.nocookie.net/rickandmorty/images/6/6b/Pubescent_Rick.png), en el marco de una puerta | 2454×1620 | **Rick con su objeto**: pose para «explicar» o «presentar un invento» |
| **4** | [Morty recortado, enfadado y sudando](https://static.wikia.nocookie.net/rickandmorty/images/c/ce/MortyTransparent.png) (fondo transparente) | 1259×1920 | **Morty para regañar** o quejarse. Ya viene recortado |
| **7** | [Summer, Morty y Rick en la nave](https://static.wikia.nocookie.net/rickandmorty/images/5/5b/Love_Connection_Experience.png) | 1920×1090 | **Grupo de tres** mirando algo delante: pose para «mirad esta noticia» |
| **8** | [Beth abraza a Morty](https://static.wikia.nocookie.net/rickandmorty/images/f/fe/S2e4_beth_comforts_morty.png) (2×04) | 1920×1090 | Escena tierna: láminas de ánimo |
| **10** | [Sr. Meeseeks de cerca](https://static.wikia.nocookie.net/rickandmorty/images/2/21/Meeseeks_and_Destroy_6.png) (1×05) | 1920×1088 | **Meeseeks sonriente** para «¡pregúntame!» o para ayudar |
| **11** | [Morty sonriendo en el garaje](https://static.wikia.nocookie.net/rickandmorty/images/f/f7/S1e1_smiling_morty.png) (1×01) | 1920×1088 | **Morty contento**: para dar la bienvenida |
| **13** | [La familia en el salón de la terapeuta](https://static.wikia.nocookie.net/rickandmorty/images/9/9f/S3e3_Mooom.png) (3×03) | 1920×1080 | **Sofá verde y luz de interior**: referencia de salón |
| **18** | [Pepinillo Rick cayendo a la alcantarilla](https://static.wikia.nocookie.net/rickandmorty/images/f/f7/S3e3_rick_falling_into_sewer.png) | 1920×1080 | Pepinillo en acción, con luz verde azulada |
| **21** | [Rick y Morty juntos](https://static.wikia.nocookie.net/rickandmorty/images/e/e7/Vlcsnap-2015-01-31-04h33m02s175.png), fondo claro | 1920×1080 | **El dúo en plano medio**: Rick mira a Morty. Pose de charla |
| **30** | [La familia en el coche](https://static.wikia.nocookie.net/rickandmorty/images/2/27/S3e3_truly_awful_parental_units.png) (3×03) | 1920×1080 | **Los cinco en un plano**: lámina de grupo |
| **35** | [Pepinillo Rick con su pistola de pilas](https://static.wikia.nocookie.net/rickandmorty/images/b/b1/S3e3_battery_gun.png) | 1920×1080 | **Pepinillo con arma**, en acción (lo que pide el dueño: «con un arma») |
| **46** | [La familia en el garaje](https://static.wikia.nocookie.net/rickandmorty/images/e/e4/S3e3_cant_u_turn_normal.png) (3×03) | 1920×1080 | **El garaje de día** con la mesa de trabajo: fondo para los conceptos |

### `pickle-rick_01.jpg` (números 145-192) · Pepinillo Rick en acción y el dúo

| N.º | Qué es | Tamaño | Para qué |
|---|---|---|---|
| **145** | [Pepinillo Rick «listo para irse»](https://static.wikia.nocookie.net/rickandmorty/images/2/23/S3e3_rick_is_ready_to_go.png) con su traje de rata | 1920×1080 | **Pose de celebrar**: brazo arriba, garra abierta |
| **147** | [Pepinillo Rick satisfecho](https://static.wikia.nocookie.net/rickandmorty/images/8/8c/S3e3_rick_pleased.png) | 1920×1080 | Media sonrisa de listillo: **para presentar** |
| **148** | [Pepinillo Rick en una pantalla](https://static.wikia.nocookie.net/rickandmorty/images/7/7c/S3e3_rick_watching_u.png) | 1920×1080 | **Personaje dentro de un monitor**: sirve tal cual para el concepto de la tele |
| **149** | [Pepinillo Rick con su arma](https://static.wikia.nocookie.net/rickandmorty/images/1/15/S3e3_ricks_weapon.png) | 1920×1080 | Plano frontal, mira a cámara: **para regañar** |
| **151** | [«Run run run»](https://static.wikia.nocookie.net/rickandmorty/images/c/cc/S3e3_run_run_run.png) | 1920×1080 | Carrera con rayos: acción pura |
| **153** | [Grito en pantalla partida](https://static.wikia.nocookie.net/rickandmorty/images/7/71/S3e3_scream_split_screen.png) (Jaguar y Pepinillo) | 1920×1080 | **Grito**: la cara de «¡noticia urgente!» |
| **156** | [Beth, Morty y Summer sentados](https://static.wikia.nocookie.net/rickandmorty/images/0/00/S3e3_sitting_smiths.png) | 1920×1080 | Tres personajes en sofá: **público que mira** |
| **173** | [Pepinillo Rick visto entre dos agentes](https://static.wikia.nocookie.net/rickandmorty/images/1/1b/S3e3_what_the_hell_is_that.png) | 1920×1080 | Encuadre con **algo delante** (hombros en primer plano): cómo evitar lo plano |
| **176** | [Morty en el garaje](https://static.wikia.nocookie.net/rickandmorty/images/3/30/S3e3_who_would_do_this.png), brazos abiertos | 1920×1080 | **Morty explicando** o sorprendido, con la mesa de Rick detrás |
| **182** | [Rick y Summer en el garaje](https://static.wikia.nocookie.net/rickandmorty/images/5/5b/Vlcsnap-2015-01-31-02h39m43s236.png) | 1920×1080 | El garaje abierto a la calle, de día |
| **185** | [Rick y Morty cavando en el jardín](https://static.wikia.nocookie.net/rickandmorty/images/b/b3/Vlcsnap-2015-01-31-03h28m32s141.png) | 1920×1080 | Exterior de la casa con **luz de día y verde** |
| **186** | [Rick y Morty en el sofá del salón](https://static.wikia.nocookie.net/rickandmorty/images/f/fa/Vlcsnap-2015-01-31-03h49m20s197.png) | 1920×1080 | **El sofá azul visto desde la tele**: el punto de vista del concepto A ⚠️ (capítulo sin identificar) |
| **188** | [Morty y Rick de cerca](https://static.wikia.nocookie.net/rickandmorty/images/d/d0/Vlcsnap-2015-01-31-02h41m31s87.png) | 1910×1080 | Plano de dos caras: **conversación** |
| **191** | [Sr. Meeseeks recortado](https://static.wikia.nocookie.net/rickandmorty/images/f/f2/MrMeeseeks-render.png), mano levantada | 765×1462 | **Meeseeks de cuerpo entero para presentar**. Ya viene recortado |

### `arte-produccion_01.jpg` (números 193-220) · arte de producción del 3×03

| N.º | Qué es | Tamaño | Para qué |
|---|---|---|---|
| **196-203, 213-214** | Storyboards de fondos de **Tommy Scott** ([ejemplo, 198](https://static.wikia.nocookie.net/rickandmorty/images/e/ec/S3e3_Tommy_Scott_bgs3.jpg)): rascacielos, pasillos, despacho | 1280×720 | **Cómo se dibuja un fondo** antes de pintarlo: perspectiva y línea |
| **194, 195, 205, 207, 211** | Pinturas de **Corey Booth** ([207, Pepinillo en su trono](https://static.wikia.nocookie.net/rickandmorty/images/2/22/S3e3_Corey_Booth_paints.jpg)) | 1280×683 a 750 | **Color y luz finales** sobre el boceto |
| **204** | [Rick oficial, busto](https://static.wikia.nocookie.net/rickandmorty/images/a/a6/Rick_Sanchez.png) | 848×1080 | **Rick serio**, de frente: para regañar o para avisos |
| **208** | [Rick joven, busto](https://static.wikia.nocookie.net/rickandmorty/images/3/3f/Young_Adult_Rick.png) | 850×1000 | Variante (sin babas ni ojeras) |
| **209, 215-217** | Conceptos de **Justin Noel** ([209](https://static.wikia.nocookie.net/rickandmorty/images/e/ef/S3e3_Justin_Noel_concepts.jpg)): ratas y monstruos en línea limpia | 1200×656 | **Tipo de línea sin color**: guía del contorno |
| **210** | [Rick de cuerpo entero con el aparato del vial verde](https://static.wikia.nocookie.net/rickandmorty/images/6/68/FullBodyRick.png) | 696×1082 | **La pose oficial de Rick con objeto**. De aquí se midió el pantalón `#8E774D` |
| **218** | [Pelota antiestrés del Sr. Meeseeks](https://static.wikia.nocookie.net/rickandmorty/images/a/ad/14120_mrmeeseeksstressball_1525053727.jpg) (producto) | 631×1024 | Objeto real de merchandising |
| **219-220** | Fondos de **Brianne Neumann** ([219](https://static.wikia.nocookie.net/rickandmorty/images/a/ac/S3e3_Brianne_Neumann_bg6.jpg)) | 1280×452 / 1000×564 | Fondos azul grisáceo sin personajes |

**Las mejores para cada concepto de §19**: A (la tele del salón) → 186
(el sofá visto desde la tele), 210 y 3 (Rick con su aparato), 148
(personaje dentro de una pantalla) y 156 (público sentado). B (Pepinillo
Rick en el garaje) → 46 y 176 (el garaje y su mesa), 145, 147, 149 y 35
(el Pepinillo vivo, no quieto). C (la caja Meeseeks en la cocina) → 191
(Meeseeks recortado), 10 (su sonrisa) y 190 (la mesa de la cocina de los
Smith, con Jerry y Morty). Para calcar proporciones: 1 (Morty) y 210
(Rick). Las hojas 2 y 3 que no
subí (números 49-144) quedan en `herramientas/referencias/rick-and-morty/`,
con su lista en `indice.json`.

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D para la lámina

| Modelo | Autor | Licencia | Para qué |
|---|---|---|---|
| [Television 01](https://polyhaven.com/a/Television_01) | Poly Haven | **CC0** ✅ (sin crédito obligatorio). Trae madera, metal, vidrio y desgaste | **La tele**. Es una tele antigua de mueble de madera ⚠️: compárala con la del salón de los Smith antes de usarla |
| [CRT TV](https://sketchfab.com/3d-models/crt-tv-9ba4baa106e64319a0b540cf0af5aa9e) | Timothy Ahene | **Free Standard** de Sketchfab ✅ (API, 25-sep): se puede bajar y usar; no es CC | Tele de tubo |
| [Sony PVM-14L2 CRT TV](https://sketchfab.com/3d-models/none-ab19c2419c2647299ce96d027b3e7f5e) | poring | **CC BY 4.0** ✅ (API) | **Tele de tubo con licencia clara** (nueva, segunda pasada) |
| [Small CRT TV](https://sketchfab.com/3d-models/small-crt-tv-890c6ce1f6124c02b0cad54db0fdcb52) | rhcreations | **CC BY 4.0** ✅ (API) | Otra opción |
| [Portal gun (Rick and Morty)](https://sketchfab.com/3d-models/portal-gun-rick-and-morty-ac3226c6b9e64142af2065409f0162ee) | kreems | **CC BY 4.0** ✅ (API) | La pistola de portales, en primer plano |
| [Portal Gun - Rick and Morty](https://sketchfab.com/3d-models/portal-gun-rick-and-morty-149daa9d26354c4999394773cdf9867f) | AbhijeetUnreal | **CC BY 4.0** ✅ (API) | Otra pistola |
| [Meeseeks Box](https://sketchfab.com/3d-models/none-88525f59bb974271a0933fc7608672c2) | pythagean | **CC BY 4.0** ✅ (API) | **La caja Meeseeks** (concepto C): **usa esta** (nueva, segunda pasada) |
| [Rick and Morty Meeseeks Box](https://sketchfab.com/3d-models/rick-and-morty-meeseeks-box-c1480c8478c148b19ab4076bd8077be1) | MagunDongle | **Sin licencia y no se puede bajar** (API) ❌ | Sólo para mirar la forma |
| [Plumbus](https://sketchfab.com/models/ea0ca7e5d42744bb95dd32f6b5ff7f27/embed) | mskullkid | **Editorial**, no se puede bajar (API) ❌ | Sólo para mirar |
| [Plumbus (llavero, imprimible)](https://sketchfab.com/3d-models/plumbus-keychain-rick-and-morty-3d-printable-424de72d353049e4b6dae7ffffa5fa95) | Nima (@h3ydari96) | **CC BY 4.0** ✅ (API) | Objeto de fondo |
| [Morty Rig Blender](https://sketchfab.com/3d-models/morty-rig-blender-c99a7fbd39b84428ab99ec1af4b15800) | mfxmotions | **CC BY 4.0** ✅ (API) | **Morty con esqueleto** para posarlo en Blender |

Colecciones para buscar más:
[OblivionRazer](https://sketchfab.com/OblivionRazer/collections/rick-and-morty-a061400cdc2a454bad90869309c8b89e) ·
[double-helix](https://sketchfab.com/double-helix/collections/rick-and-morty-dcc0e006b3994f3d9a36126b945f1cf7).

> [!note] Crédito exacto
> Para lo que sea CC BY, el crédito va así: «<nombre del modelo>» de
> <autor> (Sketchfab), CC BY 4.0. En la segunda pasada (25-sep-2026) leí
> la licencia de cada uno en la API de Sketchfab (`/v3/models/<id>`): es
> la que dice la tabla.

### 4.2 Escenarios en 3D de fans (mirar, nunca pegar)

| Obra | Autor | Qué es |
|---|---|---|
| [Rick & Morty: Garage Environment](https://www.artstation.com/artwork/4Nz0k1) | Joshua Kolkin | El garaje en Unreal, para realidad virtual, con la pistola de portales que dispara |
| [Rick and Morty's Living Room](https://www.artstation.com/artwork/D5ZLL0) | Aziz Saadana | **El salón de los Smith**, en 3D semirrealista: la mejor referencia de la habitación del sofá y la tele que encontré |
| [Rick and Morty (Garage fan model)](https://www.artstation.com/artwork/xJvkr1) | Kellian Giraud | El garaje (Maya, Substance, Unreal) |
| [Recreate the Garage of Rick and Morty](https://www.artstation.com/artwork/obQBQB) | Pourya Sammy | Garaje estilizado |
| [Rick and Morty Garage (Fan Art)](https://www.artstation.com/artwork/bKBrlk) | Nika Mumladze | Garaje en Blender, con .blend descargable ⚠️ |
| [3D Model - Rick and Morty's Garage](https://www.artstation.com/artwork/39dbDB) | Isabela Efeiche | Garaje |
| [Rick and Morty Garage](https://www.artstation.com/artwork/v2eykx) | Edvinas Petrauskas | Garaje |
| [Virtual Rick-ality 3d garage scene](https://www.artstation.com/artwork/rGPLa) | Anthony Tan | El garaje del juego de realidad virtual |
| [(Rick and Morty) Smith Residence](https://steamcommunity.com/sharedfiles/filedetails/?id=901397224) | Steam Workshop | La casa entera como mapa de fans ⚠️ |

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios que sirven

| Sitio | Qué sé | Luz |
|---|---|---|
| **El salón de los Smith** | Paredes blancas, moqueta **tostada y verde**, **un sofá blanco y otro azul**, estantería marrón con libros y **la tele sobre un mueble** ⚠️ (una fuente: el wiki en inglés, por resumen de búsqueda). Aquí se ve el cable interdimensional (1×08) | Luz de día plana; de noche, la tele ilumina a la familia ⚠️ de memoria |
| **El garaje de Rick** | Banco de trabajo con cacharros; ahí está Pepinillo Rick (3×03, 0:20: «On my work bench, Morty») ✅ | Luz de tubo fluorescente ⚠️ |
| **Sala de espera del hospital** (2×08) | «Go in the waiting room, dad» (0:46) ✅. Rick conecta su aparato a la tele de la sala. **Vista en vídeo** (segunda pasada): fondo azul marino con estrellas `#0A1640`, monitor médico turquesa `#1ABABA`, sábanas `#DDF0F6` ✅ ([promo, 0:08](https://www.dailymotion.com/video/x3jf16p?t=8)) | Luz fría de hospital ✅ (medida) |
| **El plató de «Opposite News»** | Fondo **azul grisáceo** con una curva más clara ✅ (visto en el 225) | Luz de plató, plana |
| **La tienda de Real Fake Doors** | **Pared azul muy claro** llena de **puertas de colores** ✅ (visto en el 277) | Luz de anuncio barato |

### 5.2 Paleta medida (hex, ±5 por canal) ✅

La mido en los fotogramas de la API y la comparo con la paleta
«schwifty» del paquete de R [ggsci](https://github.com/nanxstats/ggsci/blob/master/R/palettes.R)
(hecha por Nan Xiao «inspirada en Rick y Morty»). Cuando las dos
coinciden, el color está confirmado.

| Qué | Medido por mí | ggsci | Uso |
|---|---|---|---|
| Pelo de Rick | `#AAD3E9` | `#B7E4F9` («RickBlue») | ✅ |
| Camisa de Rick | `#97D7D7` | `#A6EEE6` («RickGreen») | ✅ |
| Bata de Rick | `#E8E8E8` | — | blanco roto, nunca blanco puro |
| Piel de Rick | `#D2C9B8` | — | grisácea, más apagada que la de Morty |
| Pantalón de Rick | `#8E774D` (hoja de modelo, hoja 210) | `#917C5D` («RickBrown») | ✅ (segunda pasada) |
| Camiseta de Morty | `#FBF976` | `#FAFD7C` («MortyYellow») | ✅ |
| Pelo de Morty | `#8F5C23` | `#82491E` («MortyBrown») | ✅ |
| Pantalón de Morty | `#314568` (hoja de modelo, hoja 1) | `#24325F` («MortyBlue») | ✅ (segunda pasada) |
| Piel de Morty | `#F8C9A9` | — | melocotón |
| Top de Summer | `#DE6DC7` | `#E762D7` («SummerPink») | ✅ |
| Pelo de Summer | `#DB8A38` | `#E89242` («SummerOrange») | ✅ |
| Polo de Jerry | `#617734` | `#526E2D` («JerryGreen») | ✅ |
| Blusa de Beth | `#E85558` | `#FB6467` («BethRed») | ✅ |
| Sr. Meeseeks | `#63C4EE` | `#69C8EC` («MeeseeksBlue») | ✅ |
| Pepinillo Rick | `#659025` (cuerpo) · `#618825` (frente) | — | verde oliva, no verde chillón |
| Fondo del plató de noticias | `#A0BDCF` | — | visto en el 225 |
| Traje del presentador | `#515E6E` · corbata `#918C59` | — | visto en el 225 |
| Pared de Real Fake Doors | `#B5E4E7` | — | visto en el 277 |

El **verde de portal**, medido en la segunda pasada con Pillow en dos
vídeos ✅: en la [promo del 2×08, 0:20](https://www.dailymotion.com/video/x3jf16p?t=20)
el anillo va de `#324E00` (borde) a `#AFDB30` (medio) y `#DAF81E`
(centro): **más amarillo lima que verde puro**. En la [tarjeta de la T9,
0:51](https://www.dailymotion.com/video/xae2lba?t=51), casi blanco:
`#DEF7D7`. Las paletas de fans (`#97CE4C`, `#88E23B`,
[color-hex](https://www.color-hex.com/color-palette/9134),
[ColorsWall](https://colorswall.com/palette/243091)) salen más verdes que
lo real. **Usa `#AFDB30`/`#DAF81E` para un portal activo.**

La **tarjeta del título**: letra turquesa `#52FFEC` sobre negro
`#000000` (tráiler T1, 1:36); en la promo de la T9, **morada** ✅.
La **sala de los Meeseeks** (1×05) es marrón anaranjada, no el salón
azul de los Smith: no los confundas ✅ ([vídeo, 1:10](https://www.dailymotion.com/video/x8bmk63?t=70)).

### 5.3 Texturas reales equivalentes

La serie es **plana**: color liso, sin textura. La textura sólo va en
el **objeto de Blender** (la tele, la caja, el mueble), para que la luz
sea real:

- **Mueble de la tele**: chapa de madera barnizada (la trae el modelo
  CC0 de Poly Haven).
- **Pantalla**: vidrio con reflejo suave; si es de tubo, **líneas de
  barrido** muy finas.
- **Caja del cable**: plástico negro mate con una rejilla, y el **cristal**
  de xantenita con brillo interior.
- **Moqueta**: tostada con verde (según el wiki ⚠️).
- Busca estas texturas en [Poly Haven](https://polyhaven.com/) (todo CC0).

---

## 6 · Tipografía

Todas las comprobé con fontTools en el archivo: ¿trae á é í ó ú ñ ¿ ¡?

| Uso | Letra | Licencia | ¿Español? | Nota |
|---|---|---|---|---|
| **El logo** «Rick and Morty» | **Get Schwifty** (jonizaak), recreación de fans del logo, que es dibujado a mano ✅ ([FontBolt](https://www.fontbolt.com/font/rick-and-morty-font/), [Hyperpix](https://hyperpix.net/fonts/rick-and-morty-font/)) | Gratis, **pide crédito y enlace** al autor ⚠️ | **NO**. Sólo trae A-Z, a-z y 0-9: **ni tildes, ni ñ, ni ¿ ¡, ni puntos ni comas** ✅ (archivo de [este repositorio](https://github.com/fmiguezo/SkillFactory-SegundoProyecto/tree/main/src/font)) | Sirve para palabras sin tilde: «Noticias», «series», «Rick y Morty» |
| Títulos con tildes, en el mismo espíritu | **Creepster** | OFL ✅ | **Sí** ✅ | Letras de trazo irregular con picos; lo más parecido a Get Schwifty que trae español |
| Alternativa con goterones | **Rubik Wet Paint** | OFL ✅ | **Sí** ✅ | Más legible; gotea por abajo |
| **El rótulo de la noticia** (la franja de abajo) | **Anton** u **Oswald** | OFL ✅ | **Sí** ✅ | Condensadas y gruesas, como un rótulo de tele |
| Parecida a la de **Adult Swim** | El logo «[adult swim]» es **Helvetica Neue Condensed Bold** (desde 2003) ✅ ([Logopedia](https://logos.fandom.com/wiki/Adult_Swim), [fontinlogo](https://www.fontinlogo.com/logo/adult-swim)). Libre parecida: **Oswald** o **Bebas Neue** | OFL ✅ | **Sí** ✅ | Blanco sobre negro |
| **Pantallita de la caja del cable** | **VT323** o **Share Tech Mono** | OFL ✅ | **Sí** ✅ | Dígitos de aparato: «CANAL 137» |
| Gritos («¡Soy un pepinillo!») | **Bangers** o **Luckiest Guy** | OFL / Apache ✅ | **Sí** ✅ | Sólo para una palabra gritada |
| Texto de globo (si se usa el cómic) | **Sniglet** o **Grandstander** | OFL ✅ | **Sí** ✅ | Redondas y amables. El rotulista del cómic es **Crank!** (Christopher Crank) ✅ ([Blue Juice Comics](https://bluejuicecomics.com/about/crank/), [su blog](http://crankletters.blogspot.com/p/lettering.html)); rotula a mano, **no hay archivo de su letra**. La libre más parecida a rotulado de cómic: **[Comic Relief](https://fontsource.org/fonts/comic-relief)** (OFL-1.1), con á é í ó ú ñ ¿ ¡ ✅ (fontTools, segunda pasada) |

Archivos: [google/fonts](https://github.com/google/fonts) (carpetas
`ofl/creepster`, `ofl/rubikwetpaint`, `ofl/anton`, `ofl/oswald`,
`ofl/bebasneue`, `ofl/vt323`, `ofl/sharetechmono`, `ofl/bangers`,
`apache/luckiestguy`, `ofl/sniglet`, `ofl/grandstander`).

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que la serie pone en pantalla

La serie es de dibujos para la tele: **no tiene globos** ni pensamientos
escritos. El texto que aparece en pantalla es casi siempre **tele dentro
de la tele**:

1. **El rótulo de abajo** (el «zócalo»). El vendedor de Real Fake Doors lo
   dice en voz alta: «That's our slogan. **See it on the bottom of the
   screen below our name.** Here's another slogan right below that one»
   (1×08, 11:18) ✅. Es decir: **nombre arriba, eslogan debajo, y otro
   eslogan debajo del primero**. Una idea por línea: justo la regla 4
   del dueño.
2. **La cartela del programa**: «Two Brothers» (1×08, 7:00),
   «Jan Quadrant Vincent 16» (2×08, 6:42), «The Personal Space Show»
   (2×08, 16:55) ✅ por el subtítulo. Cómo se ven, de memoria ⚠️.
3. **El noticiero**: presentador de frente, con papeles, y el locutor que
   lo anuncia («It's the opposite news with Michael Thompson», 2×08,
   12:29) ✅.
4. **«Breaking news»** dicho por un locutor (1×08, 19:09; 2×08,
   19:30) ✅. Si lleva franja escrita, no lo sé ⚠️.
5. **El periódico «NEWS»** que lee Jon (fotograma 184) ✅.

Fuera de la serie:

- **Los cómics de Oni Press** (desde 2015, guion de **Zac Gorman**,
  dibujo de **CJ Cannon**, rótulos de **Crank!**) ✅ ([Paste](https://www.pastemagazine.com/comics/rick-and-morty/oni-presss-rick-and-morty-comics-bust-out-the-conn),
  [The Robot's Voice](https://www.therobotsvoice.com/2015/03/rick_morty_zac_gorman_capture_creatures_oni_press.php)).
  Globo blanco clásico de cómic ⚠️ (de memoria). **Es justo la burbuja
  blanca que el dueño no quiere**: no usarlo.
- **Adult Swim**, la cadena, habla con **cartelas negras con letra
  blanca** (sus «bumps») ⚠️ de memoria; la marca «[adult swim]» va en
  Helvetica Neue Condensed Bold ✅.

### 7.2 Cómo hablan (por el subtítulo)

| Quién | Rasgo | Ejemplo con minuto |
|---|---|---|
| **Rick** | **Eructa en mitad de las palabras** | «the best doctor in the ga-[Belches]-laxy» (2×08, 0:38) ✅. En los subtítulos de Addic7ed hay **unas 60 marcas de eructo** en 28 episodios |
| | Dice «**Morty**» cada dos frases | «Pedal to the metal, Morty» (1×08, 15:10) |
| | Cínico, rápido, desprecia lo que ve | «None of it mattered and the entire show was stupid» (1×08, 0:19; que lo dice él, de memoria ⚠️) |
| | Presume de ciencia | «I don't do magic, Morty, I do science» (3×03, 1:38) |
| **Morty** | **Tartamudea** al empezar | «W-why is his body, like, sloping off…» (2×08, 12:46) |
| | «**Aw, geez**» y «Oh, man» | «geez» sale **60 veces** en esos 28 episodios (casi siempre de Morty); el primer «Aw, geez», 1×01, 6:17 ✅ |
| | Cuando se harta, suelta un discurso | 2×08, 19:08 a 19:23 ✅ |
| **Summer** | Adolescente sarcástica, opina de todo | «**I don't want to be that girl, but**…» (2×08, 13:27); «Does all interdimensional TV have to rely on juvenile violence?» (2×08, 19:05) ✅ |
| | Dolida y seca | «Fine. I'll find a world where you bothered to have me» (1×08, 5:09) ✅ |
| **Sr. Meeseeks** | Voz aguda y alegre, **siempre se presenta** | «I'm Mr. Meeseeks! Look at me!» (1×05, 2:35); «Ooh, yeah! Can do!» (3:31); «All done!» (2:44) ✅ |
| **Pepinillo Rick** | Orgullo absurdo, repite | «I turned myself into a pickle, Morty!» (3×03, 0:32, 0:37 y 0:41); «Boom! Big reveal... I'm a pickle» (0:34) ✅ |
| **Los presentadores del cable** | Improvisan, se trabucan, se ríen | «It's called "Two Brothers." "Two Brothers." It's just called "Two Brothers."» (1×08, 7:00) ✅. Todo el cable se **improvisaba** en la cabina (ver §12) |

### 7.3 Cómo se traduce a una lámina fija

- **Nada de globo blanco.** El texto va **en la tele**: un **rótulo
  inferior** de dos o tres líneas (nombre, eslogan, otro eslogan), en
  Anton u Oswald, sobre una franja de color plano.
- La frase del personaje va como **subtítulo de la tele** (blanco con
  borde negro, abajo) o **en la franja del rótulo**: su nombre en la
  primera línea y la frase en la segunda. Sin «·» entre los dos.
- Si habla alguien **fuera de la tele** (Rick en el sofá), su frase va
  en la **pantallita de la caja del cable** (VT323) o en **un papel**
  pegado al mueble. Nunca flotando.
- Un **«¡Último momento!»** o **«¡Estreno!»** en franja roja arriba del
  rótulo: es lo que dice el locutor («Breaking news»).

### 7.4 En los videojuegos de la franquicia

- **Pocket Mortys** (2016, iOS y Android): parodia de Pokémon. Juegas con
  un Rick que **atrapa Mortys** y combate contra entrenadores ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Pocket_Mortys), por
  resumen). Caja de texto al pie, como Pokémon ⚠️ (de memoria). Sus
  **servidores oficiales cerraron** y en agosto de 2026 unos fans
  publicaron un parche para jugar la campaña sin conexión ✅ (la fecha
  exacta del cierre no la sé ⚠️)
  ([PocketMortysOfflinePatch](https://github.com/ClumsyPandal1/PocketMortysOfflinePatch)).
  Es una **noticia de la franquicia** buena para el canal.
- **Virtual Rick-ality** (2017, Owlchemy Labs, realidad virtual): eres un
  **clon de Morty** que hace recados en **el garaje de Rick** ✅
  ([wiki](https://rickandmorty.fandom.com/wiki/Rick_and_Morty:_Virtual_Rick-ality),
  por resumen).
- **Clone Rumble** (móvil, cerrado), y apariciones en **MultiVersus** y
  **Fortnite** ✅ ([Game Rant](https://gamerant.com/rick-and-morty-video-games-mobile-vr-crossover-cameo/)).
- No encontré capturas de sus cajas de diálogo (Game UI Database y
  Spriters Resource daban 403).

### 7.5 Qué NO hacer con el texto

- **No traducir «Wubba lubba dub dub»**: en el doblaje latino se queda
  igual ✅ (guía de cuadros de diálogo, §17).
- No usar la letra del logo con tildes: **se rompe** (no las tiene).
- No poner globos de cómic blancos ni nubes de pensamiento.
- No poner a Rick hablando **sin eructo ni «Morty»** si la frase es suya:
  queda falso. Pero ojo, **un eructo por frase como mucho**.

---

## 8 · Los personajes

Todo lo de carácter sale de los subtítulos (con minuto ✅) o de los
resúmenes de búsqueda; lo que describo de memoria va con ⚠️.

### Rick Sánchez — el abuelo científico

- **Quién es**: científico genial, cínico y bebedor («That is why he must
  numb himself», dice Birdperson, 1×11, 18:30 ✅). Vive con la familia
  de su hija Beth, tiene el laboratorio en el garaje y arrastra a su
  nieto Morty a sus aventuras.
- **Qué le importa**: aunque lo niega, su familia. Birdperson revela que
  «wubba lubba dub dub» significa «**I am in great pain. Please help
  me**» (1×11, 18:22) ✅: su risa es un grito de dolor.
- **Miedo**: perder a los suyos (lectura de fans). **Con fuente**: le dan
  miedo **los piratas** ✅ («Anatomy Park» y «Unmortricken», wiki, *Trivia*;
  segunda pasada). Llora a escondidas por Morty en 1×10 ✅ (§18C).
- **Cómo habla**: rápido, eructa, insulta con cariño, dice «Morty» sin
  parar (§7.2). **Cómo se ríe**: a carcajadas, con la boca muy abierta ⚠️.
  **Cómo se enfada**: párpados a media asta, ceja fruncida, dientes
  apretados (fotograma 1) ✅. **Cómo explica**: sin mirar, con prisa,
  «20% accurate as usual, Morty» (1×08, 0:34) ✅.
- **Lenguaje corporal**: encorvado, bata abierta, una mano en el
  bolsillo o con la petaca ⚠️.
- **Siempre con**: Morty. Su objeto: **la pistola de portales**.
- **Voz latina**: **Juan Guzmán** ✅.

### Morty Smith — el nieto

- **Quién es**: 14 años, inseguro, buen chico. Va con Rick a todo.
- **Qué le importa**: hacer lo correcto; Jessica, la chica que le gusta
  (fotograma 180) ⚠️.
- **Detalle clave para este canal**: el Morty de la serie **no es el
  original**: él y Rick vinieron de otro mundo y se enterraron a sí
  mismos en el jardín (1×06; lo cuenta en 1×08, 17:28 a 17:50) ✅.
- **Cómo habla**: tartamudea, «Aw, geez» (§7.2). **Cómo explica**:
  palma hacia arriba, dientes a la vista (fotograma 630) ✅.
  **Cómo se asusta**: mira arriba con los ojos muy abiertos y los
  brazos caídos (fotograma 2) ✅.
- **Frase de la serie para el canal**: «**Come watch TV**» (1×08,
  18:06) ✅.
- **Voz latina**: **Eder La Barrera** ✅.

### Summer Smith — la hermana (la voz del debate)

- **Quién es**: 17 años, al principio **superficial**, pegada al móvil y
  a su estatus en el instituto; con las temporadas se une a las
  aventuras y compite con Morty por el cariño de Rick. **Lista y con
  humor** ✅ ([wiki](https://rickandmorty.fandom.com/wiki/Summer_Smith)
  y [Wikipedia](https://en.wikipedia.org/wiki/Summer_Smith), por
  resumen). En temporadas tardías, más **despiadada** ⚠️.
- **Por qué ella para #noticias-series**: es la que **comenta y protesta
  lo que sale en la tele** (2×08, 13:27 y 19:05) ✅. Es el «abre
  un hilo» hecho persona.
- **Cómo se enfada**: brazos cruzados, cejas bajas (fotograma 3) ✅.
  **Cómo protesta**: brazos abiertos y boca abierta (fotograma 339) ✅.
- **En la temporada 9**: arte de producción con **ropa de atleta
  olímpica y medalla** ✅ (§3.2).
- **Voz latina**: **Lileana Chacón** ✅.

### Sr. Meeseeks — el ayudante de la caja

- **Quién es**: criatura azul que sale de **la caja Meeseeks** al
  **pulsar el botón**. Cumple **una petición** y **desaparece** (1×05,
  2:31 a 2:47) ✅.
- **Qué le importa**: acabar su tarea. «**Existence is pain** to a
  Meeseeks, Jerry» (16:42) ✅. Si la tarea no se cumple, se vuelve loco.
- **Cómo habla**: agudo, feliz, servicial: «Can do!», «Yes, siree!»
  (2:41) ✅.
- **Cuerpo**: alto, delgado, **brazos largos y sueltos**, sonrisa fija
  (fotograma 242) ✅.
- **Por qué sirve**: una noticia = **una petición**. La caja se pulsa, el
  Meeseeks trae la noticia y «¡listo!». Encaja con «un hilo por noticia».
- **Nombre en latino**: «Sr. Meeseeks» (así titula su ficha Doblaje Wiki).
- **Voz latina**: **Ángel Lugo** ✅ (dos fuentes en la segunda pasada, ver §10).

### Pepinillo Rick — el meme

- **Quién es**: Rick convertido en pepinillo **para no ir a terapia
  familiar** (3×03, 2:26) ✅. Luego se hace un **traje con ratas**
  (fotograma 265) ✅.
- **Cómo habla**: orgulloso y gritón: «I'm Pickle Rick!» (0:55) ✅.
- **En latino**: HBO Max Latinoamérica tituló sus clips «**¡¡Soy un
  pepinillo!!**» y «¡Convertirse en un Pepinillo!» ✅
  ([TikTok de HBO Max LA](https://www.tiktok.com/@streammaxla/video/7271440286755130629),
  [otro](https://www.tiktok.com/@streammaxla/video/7109188591141670149?lang=en)).
  Los fans citan «¡Mira, Morty, me acabo de convertir en un pepinillo!» ⚠️
  y «Voltea el pepinillo, Morty» ⚠️. El nombre en latino es **Pepinillo
  Rick** ✅ ([wiki en español](https://rickandmorty.fandom.com/es/wiki/Pepinillo_Rick)
  y [YouTube de HBO Max](https://www.youtube.com/watch?v=2_7Fryr5g_U)).
- **Premio**: el episodio ganó el **Emmy 2018 a mejor programa animado**,
  el primero de la serie ✅ ([Screen Rant](https://screenrant.com/rick-morty-wins-emmy-outstanding-animated-program/),
  [Toon Boom](https://www.toonboom.com/rick-and-morty-wins-its-first-emmy-and-the-case-for-2d-animation-series)).
- **Frase para el canal**: «**Boom! Big reveal**» (0:34) ✅ =
  **«¡Bum! Gran revelación»** (traducción mía).

### Los secundarios que conviene tener a mano

| Quién | Por qué | Dato |
|---|---|---|
| **Michael Thompson** | **El presentador de noticias** del cable (2×08) | Fotograma 225 ✅. Está unido a su siamés Pichael: por eso «se inclina» fuera del plano |
| **Jerry Smith** | El padre; el que sale en «Breaking news» en otra realidad (1×08, 19:09) ✅ | Voz latina **Héctor Indriago** ✅ (Doblaje Wiki y los repartos del anime) |
| **Beth Smith** | La madre, cirujana de caballos | Voz latina: **Rebeca Aponte** (T1-T6), **Carmen Lugo** (T7-T8) y **Arlet Matute** (T9) ✅ (dos fuentes cada una, §10) |
| **Mr. Poopybutthole** | Favorito de fans; sale en las escenas finales | «Ooh-wee!» ✅ ([wiki](https://rickandmorty.fandom.com/wiki/Mr._Poopybutthole)). Voz latina: Reinaldo Rojas → Nayip Rodríguez → Jaime de Abreu ⚠️ (una fuente, §10) |
| **Evil Morty** | Favorito de fans por sus giros ✅ ([Collider](https://collider.com/best-rick-and-morty-characters-ranked/), [CBR](https://www.cbr.com/best-rick-and-morty-characters-ranked/)) | Parche en el ojo; su tema es «For the Damaged Coda» (§11) |
| **Birdperson** | El amigo de Rick que explica el «wubba lubba» | 1×11 ✅ |

---

## 9 · ¿Quién es el más querido?

- **No hay encuesta oficial** de Adult Swim. No la encontré.
- **Ranker** (más de 6.000 votos de fans): **1.º Rick, 2.º Morty,
  3.º Pepinillo Rick** ⚠️ (una fuente, por resumen)
  ([Ranker](https://www.ranker.com/list/best-rick-and-morty-characters/greg-hahn)).
- Las listas de prensa (Collider, CBR, Screen Rant, MovieWeb) meten
  siempre al **Sr. Meeseeks**, **Mr. Poopybutthole** y **Evil Morty**
  como favoritos de los fans ✅ (varias fuentes).
- **Pepinillo Rick** es el caso claro de **secundario más famoso que el
  original** en merchandising: hubo versiones a la venta en internet **a los
  minutos** de emitirse ⚠️ (una fuente), y **ganó el Emmy** ✅.
- **YouGov** mide la serie, no los personajes ([YouGov](https://today.yougov.com/topics/entertainment/explore/tv_show/Rick_and_Morty)).

**Conclusión para la lámina**: **Rick y Morty** como pareja (son los más
votados), y como **gancho** el secundario: **Pepinillo Rick** (el meme
más reconocible) o **el Sr. Meeseeks** (el que mejor encaja con «una
petición, una noticia»). **Summer** para el **debate**.

---

## 10 · Doblaje latino

**Estudio** (corregido en la segunda pasada): Turner (hoy Warner Bros.
Discovery) encargó el doblaje a **Sonoclips, hoy IDS**, en **Venezuela**
✅ (Doblaje Wiki y varios artículos del anime). Pero Sonoclips **no lo
grabó en su casa al principio**:

- **T1-T2**: lo grabó **Dvinxi Studios**, subcontratado por Sonoclips.
- **T3**: **AGP Producciones**.
- **Desde la T4**: **IDS**, en su propio estudio (por la pandemia y
  porque vio el éxito de la serie; pidió grabar en persona).

⚠️ una fuente: [Doblaje Wiki, «Historia del doblaje»](https://doblaje.fandom.com/es/wiki/Rick_y_Morty#Historia_del_doblaje),
leída entera por su API. No encontré otra que entre en la subcontratación.

**Director de doblaje** (antes «no lo encontré»): **Ángel Balam** en la
T1 y la T2; desde la T3, autodirección ✅ (dos páginas distintas de
Doblaje Wiki: la de la serie y la [ficha de Ángel Balam](https://doblaje.fandom.com/es/wiki/Angel_Balam),
«Dirección de doblaje»). Balam también leyó los **insertos** (títulos en
pantalla) hasta la T3; desde la T4 los lee **Juan Guzmán** ⚠️ (Doblaje
Wiki, «Datos de interés»).

**Cómo se grabó** ⚠️ (Doblaje Wiki, «Datos de interés»): las dos primeras
temporadas se doblaron **en tres semanas** (lo cuenta Eder La Barrera);
Eder grabó a Morty **a distancia** para que Balam tuviera tiempo con los
demás. Se dobló sobre la versión **sin censura** del Blu-ray. Por orden del
cliente, los insultos fuertes se suavizan: «motherfucker» pasa a
«**desgraciado**», «**hijo de perra**» o «**malnacido**». En latino **Rick
eructa menos** que en inglés. Estreno del doblaje: **Netflix, 1-oct-2016**;
en TV, **TBS, 1-abr-2018**.

| Personaje | Actor | Estado |
|---|---|---|
| **Rick Sánchez** | **Juan Guzmán** (venezolano, más de 30 años en el doblaje) | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Juan_Guzm%C3%A1n), [El Heraldo](https://www.elheraldo.co/sociedad/los-actores-de-doblaje-ya-no-somos-invisbles-juan-guzman-943969), [La Estrella de Panamá](https://www.laestrella.com.pa/vida-y-cultura/cultura/juan-guzman-doblaje-da-KELE497836), [La República](https://larepublica.pe/cine-series/2026/05/22/rick-y-morty-temporada-9-capitulo-1-fecha-y-hora-de-estreno-del-primer-episodio-de-la-serie-en-hbo-max-327624) |
| **Morty Smith** | **Eder La Barrera** (venezolano, nacido en 1987) | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Eder_La_Barrera), [Fandoblaje](https://fandoblaje.fandom.com/es/wiki/Eder_La_Barrera) |
| **Summer Smith** | **Lileana Chacón** (también Arenita en Bob Esponja y Raven) | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Summer_Smith), [Doblaje Latino Wiki](https://doblaje-latino.fandom.com/es/wiki/Lileana_Chac%C3%B3n) |
| **Jerry Smith** | **Héctor Indriago** (el único que no ha cambiado desde el principio) | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Jerry_Smith) y los repartos del anime |
| **Beth Smith** | **Rebeca Aponte** (T1-T6); **Carmen Lugo** (T7-T8; Rebeca se mudó a España en 2023); **Arlet Matute** (T9, Carmen se mudó a España en 2025) | ✅ las tres. Aponte: [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Rick_y_Morty) y [Fandoblaje](https://fandoblaje.fandom.com/es/wiki/Rebeca_Aponte). Lugo: Doblaje Wiki y [su ficha](https://doblaje.fandom.com/es/wiki/Carmen_Lugo). Matute: [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Rick_y_Morty#Historia_del_doblaje) y [World Dubbing News en X](https://x.com/WDN_Topic/status/2058748920721768777) |
| **Sr. Meeseeks** | **Ángel Lugo** (venezolano, también director de doblaje) | ✅ (antes ⚠️) [reparto del 1×05 en Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Rick_y_Morty/1.%C2%AA_temporada) y [Fandoblaje](https://fandoblaje.fandom.com/es/wiki/%C3%81ngel_Lugo) |
| **Sr. Pantalones de Popó** (Mr. Poopybutthole) | **Reinaldo Rojas** (T2-T3) → **Nayip Rodríguez** (T4-T6) → **Jaime de Abreu** (T7-) | ⚠️ una fuente ([Doblaje Wiki, «Sobre el reparto»](https://doblaje.fandom.com/es/wiki/Rick_y_Morty#Sobre_el_reparto)); ninguno tiene ficha en Fandoblaje |
| **Hombre Pájaro** (Birdperson) | Salvador Pérez (T1-T2) → Alejandro Mejía (T3) → **Jonathan Avilán** (actual) | ⚠️ una fuente (Doblaje Wiki, «Datos de interés») |

**Lo importante**: cuando despidieron a **Justin Roiland** (enero de 2023)
y en inglés entraron **Ian Cardoni** (Rick) y **Harry Belden** (Morty)
desde la T7 ✅ ([Variety](https://variety.com/2023/tv/news/rick-and-morty-ian-cardoni-harry-belden-justin-roiland-1235752378/),
[The Hollywood Reporter](https://www.hollywoodreporter.com/tv/tv-news/rick-and-morty-new-voice-actors-revealed-casting-process-1235618102/)),
**en latino no cambió nada**: Guzmán y La Barrera siguen, también en la
**T9** ✅.

**Rick y Morty: El anime** (2024, dirigido por **Takashi Sano**, de
Telecom Animation Film; estreno 15 de agosto de 2024, en Max): **Rick
Gerardo Reyero** y **Morty Miguel Ángel Leal**, mexicanos ✅ (Doblaje
Wiki, ANMTV, TVLaint, FUNiAnime). Summer **Constanza de la Rosa**, Beth
**Elena Díaz Toledo**, Jerry **Héctor Indriago** y Elle (nueva)
**Abigaly Claro** ✅ (segunda pasada: [ANMTV, 11-jul-2024](https://www.anmtvla.com/2024/07/rick-y-morty-el-anime-max-revela.html),
con el elenco citado, y [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Rick_y_Morty:_El_anime)).
**Corregido**: la primera pasada decía que cambiaron el reparto «porque a
Warner no le convencieron las pruebas venezolanas». ANMTV no dice eso:
fue **una medida global de Max** «para dar un grado de diferencia» con la
serie original ✅.

### Frases en latino (con su fuente)

| Frase | Estado |
|---|---|
| «**Wubba lubba dub dub**» (igual que en inglés) | ✅ |
| «**¡Soy un pepinillo!**» | ✅ (títulos de HBO Max LA) |
| «**Pepinillo Rick**» (el nombre) | ✅ |
| «**¡Soy el Señor Meeseeks!**» | ✅ (varios vídeos «Latino»: [YouTube](https://www.youtube.com/watch?v=npFeQeK75bw), [YouTube](https://www.youtube.com/watch?v=BwoG8xOKiEY)); «**¡Mírenme!**» ⚠️ (un vídeo de Facebook). En España: «¡Miradme!» |
| «Nadie existe a propósito. Nadie pertenece a ninguna parte. Todos vamos a morir. **Ven a ver la televisión**» | ⚠️ ([vídeo en Facebook](https://www.facebook.com/Arcano44/videos/rick-y-morty-ven-a-ver-la-television/646732072523882/)). La cuenta de España dice «**Ven a ver la tele**» ([X](https://twitter.com/rickymortytv/status/917072362381692934)): no confundirlas |
| «Get Schwifty» = «**Ponte Ricoso**» (título del 2×05 en la wiki en español; en España, «Estamos Cerdis») | ⚠️ ([wiki](https://wiki-de-rick-morty.fandom.com/es/wiki/Ponte_Ricoso), [Vice](https://www.vice.com/es/article/creators-escuchar-get-schwifty-en-espanol/)) |
| «Show me what you got» = «**Muéstrenme lo que tienen**» o «Muéstrame lo que tienes» | ⚠️ no sé cuál es la del doblaje |
| El cable: «**Televisión interdimensional**» en 1×08 y «Cable interdimensional» en «Los recuerdos de Morty» | ⚠️ ([wiki en español](https://rickandmorty.fandom.com/es/wiki/Cable_interdimensional)) |

---

## 11 · Música

| Qué | Dato | Ambiente |
|---|---|---|
| **Tema de apertura** | Compuesto por **Ryan Elder**, el compositor de la serie ✅ ([Shazam](https://www.shazam.com/track/430354179/rick-and-morty-theme), [WhoSampled](https://www.whosampled.com/Rick-and-Morty/Rick-and-Morty-Theme/)) | Instrumental espacial de sintetizador, tipo «Doctor Who» ⚠️ de memoria |
| **Disco oficial** | 26 canciones, 18 de Ryan Elder; con **Chaos Chaos, Belly, Blonde Redhead y Mazzy Star** ✅ (resumen de búsqueda) | — |
| **«For the Damaged Coda»**, de **Blonde Redhead** | El **tema de Evil Morty** ✅ ([Apple Music](https://music.apple.com/us/album/for-the-damaged-coda-evil-morty-theme-song-from-rick/1564763349)) | Piano solemne; para un giro dramático |
| Canción del momento triste del 1×08 | «Give me a name / Hear my faith…» en 20:14 ✅ (subtítulo). Es de Mazzy Star, «Look On Down From The Bridge» ⚠️ | Melancolía; mientras Jerry y Beth deciden seguir juntos |
| **«Get Schwifty»** | La canción del 2×05 (5:54) ✅. En latino, «Ponte Ricoso» ⚠️ | Fiesta absurda |
| **Tráiler de la T9** | Con **«Rebel Yell», de Billy Idol** (7 de abril de 2026) ✅ ([Space](https://www.space.com/entertainment/space-movies-shows/rick-and-morty-season-9-promises-no-ai-slop-just-grade-a-organic-slop-when-it-drops-on-adult-swim-later-this-year), [JoBlo](https://www.joblo.com/rick-and-morty-season-9-trailer/)) | Rock de los 80, energía de estreno |

Para #noticias-series no hace falta música, pero si la lámina se anima
algún día: el **zumbido de la tele al cambiar de canal** y el tema de
Ryan Elder.

---

## 12 · Vídeos

En la primera pasada YouTube daba 403. En la segunda (25-sep-2026)
YouTube pedía iniciar sesión, así que **los vídeos se miraron en
Dailymotion e Internet Archive**, con minuto (tabla de abajo y §2.4). Los
de YouTube de esta tabla siguen **sin minuto propio**: los útiles están en
§2, sobre el episodio.

**Mirados de verdad en la segunda pasada** (`fotogramas.py`, hojas
miradas con Read) ✅:

| Vídeo | Enlace | Visto | Para qué |
|---|---|---|---|
| Intro: viñeta previa al título + tarjeta | [Dailymotion x8x2x8y](https://www.dailymotion.com/video/x8x2x8y) | 0:32 entero | No hay opening cantado: viñeta distinta cada vez + tarjeta (0:32) |
| Clip del Sr. Meeseeks, 1×05 (Moviepilot) | [Dailymotion x7xeqwl](https://www.dailymotion.com/video/x7xeqwl?t=16) | 1:08 entero | Pose «Look at me!» (0:16) |
| «Mr. Meeseeks Helps Jerry with His Golf Swing», 1×05 | [Dailymotion x8bmk63](https://www.dailymotion.com/video/x8bmk63?t=70) | 2:18 entero | La sala llena de Meeseeks (1:00-1:25) |
| Promo «Interdimensional Cable 2: Tempting Fate», 2×08 | [Dailymotion x3jf16p](https://www.dailymotion.com/video/x3jf16p?t=8) | 0:30 entero | Sala de espera (0:08) y portal (0:20) |
| Promo «Pickle Rick», 3×03 (HobbyConsolas) | [Dailymotion x5ve1xh](https://www.dailymotion.com/video/x5ve1xh) | 0:30 entero | El pepino en el banco (0:02) |
| Tráiler T1 con créditos (Turner) | [Internet Archive](https://archive.org/details/turner_video_391819) | 1:45 | Grupo con armas (1:12), créditos (1:36) |
| **Tráiler T9 subtitulado en español**, HBO Max (8-jun-2026) | [Dailymotion xae2lba](https://www.dailymotion.com/video/xae2lba?t=51) | 1:00 entero | «Hora de levantarse, hijo de perra» (0:00-0:03, subtítulo); «NUEVA TEMPORADA **25 DE MAYO**» (0:51); logo de HBO Max (0:54) |
| «Rick and Morty Style Guide», copia del oficial | [Internet Archive](https://archive.org/details/rick-and-morty-style-guide) | 2:42 entero (66 planos) | Photoshop CC 2016.3 (0:14); cómo dibuja a Morty y a Rick (§18A) |


| Vídeo | Enlace | Para qué |
|---|---|---|
| «Ants In My Eyes Johnson», Adult Swim (22 de julio de 2015) | [YouTube](https://www.youtube.com/watch?v=G4BkGJj5BXg) | El anuncio entero |
| «Interdimensional Cable: The Weirdest Ads», Adult Swim (23 de enero de 2026) | [YouTube](https://www.youtube.com/watch?v=11OyiuqAzA4) | «Rick cambia la caja del cable de los Smith»: **el objeto del plan** |
| «Every In-Universe Commercial in Rick and Morty», Adult Swim (24 de diciembre de 2024) | [YouTube](https://www.youtube.com/watch?v=P4w5GB1PyGo) | Todos los anuncios: **rótulos de abajo** para copiar el estilo |
| «Caos interdimensional con Rick y Morty», **Adult Swim LA** | [YouTube](https://www.youtube.com/watch?v=rIcoES14iU4) | **En español**: oír cómo suena el doblaje |
| «Real Fake Doors!» (subida de 2019, «property of Adult Swim») | [YouTube](https://www.youtube.com/watch?v=6h58uT_BGV4) | El anuncio con su eslogan abajo ⚠️ no es canal oficial |
| **«Rick and Morty Style Guide»**, Adult Swim (3 de octubre de 2018) | [YouTube](https://www.youtube.com/watch?v=8c4hAsobciA) | **El más importante para dibujar**: el director de arte explica las reglas |
| Tráiler de la T9 | [SYFY](https://www.syfy.com/syfy-wire/rick-and-morty-season-9-adult-swim-official-trailer-watch-now) · [AWN](https://www.awn.com/news/adult-swim-drops-rick-and-morty-season-9-trailer) | «Anything is possible when everything is possible» ✅ |
| «Voces de RICK Y MORTY en 1 minuto» | [YouTube](https://www.youtube.com/watch?v=ep6BmKC7HdQ) | Los actores latinos |
| «Evolución de todas las voces de Rick y Morty en español latino (2013-2024)» | [YouTube](https://www.youtube.com/watch?v=0uCJ0h2P5zQ) | Cambios de voz |
| Juan Guzmán dobla a Pepinillo Rick (su TikTok) | [TikTok](https://www.tiktok.com/@juanmanuelguzman92/video/7508592677353557268) | La voz latina de Rick, en persona |
| Spencer Grammer (Summer en inglés) saluda a los fans latinos | [TikTok de HBO Max LA](https://www.tiktok.com/@streammaxla/video/7315465087035165957) | Summer y Latinoamérica |
| «¡¡Soy un pepinillo!!», HBO Max LA | [TikTok](https://www.tiktok.com/@streammaxla/video/7271440286755130629) | La frase en latino |

**Cómo se hacía el cable interdimensional** ✅ ([Screen Rant](https://screenrant.com/rick-morty-interdimensional-cable-episodes-improvised/),
[WatchMojo](https://www.watchmojo.com/articles/top-10-unscripted-rick-and-morty-moments-that-were-left-in)):
Roiland **improvisaba** en la cabina de grabación **4 o 5 horas**
(hasta seis) con otros guionistas, **bebiendo**; Dan Harmon escogía lo
mejor y le daba forma. Por eso hay risas y tropiezos. Tarda más en
animarse porque **cada anuncio es un sitio distinto** y hay que dibujar
muchos fondos.

---

## 13 · Videojuegos de la franquicia

Ver §7.4. Resumen para la lámina:

- **Pocket Mortys** (13-ene-2016, de **Big Pixel Studios** para Adult Swim
  Games): parodia de Pokémon. **Cerró sus servidores**;
  los fans lo mantienen vivo con un parche de agosto de 2026 ✅. Buena noticia de
  ejemplo para el canal.
- **Virtual Rick-ality** (2017, Owlchemy Labs): en el **garaje de Rick**.
- **Clone Rumble** (cerrado), **MultiVersus**, **Fortnite** (apariciones).
- **Segunda pasada: capturas miradas** ✅. En *Virtual Rick-ality* (6
  capturas oficiales de Steam, 1920×1080) **no hay cajas de diálogo**: el
  texto vive **dentro del mundo**: el cartel «SALESMAN RICK'S», una nota
  pinchada («VOUCHER — REPLACEMENT MORTY», [captura](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/469610/ss_ad09661030ad427adb462929eb8b388fdb316766.1920x1080.jpg))
  y un **plano técnico azul** con círculos rojos («DETACH FROM BODY»,
  «TRAP IN BALL»). En *Pocket Mortys*, una **barra rosa pálida** abajo con
  texto negro en negrita ([crafteo, 1920×1080](https://static.wikia.nocookie.net/rickandmorty/images/2/2b/Crafting_Station_interface.png))
  y carteles de tienda con contorno negro ([mapa, 1280×720](https://static.wikia.nocookie.net/rickandmorty/images/5/52/Salesmanrick_in_game.png)).
  La **pantalla de combate** de Pocket Mortys sigue sin ver ⚠️.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### Lo que todos reconocen ✅

- **«I'm Pickle Rick!»** (3×03). En latino, «¡Soy un pepinillo!».
- **«Wubba lubba dub dub»**: y que en realidad significa «estoy sufriendo,
  ayúdame» (1×11, 18:22).
- **El Sr. Meeseeks**: «¡Soy el Señor Meeseeks! ¡Mírenme!».
- **«Get Schwifty»** y **«Show me what you got»** (2×05) ✅
  ([Know Your Meme](https://knowyourmeme.com/memes/show-me-what-you-got)).
- **El plumbus**: todos saben qué es menos tú ✅
  ([Daily Dot](https://www.dailydot.com/unclick/plumbus-rick-morty/)).
- **El cable interdimensional**: Ants in My Eyes Johnson, Real Fake
  Doors, Two Brothers, Gazorpazorpfield, Baby Legs ✅
  ([Screen Rant](https://screenrant.com/rick-and-morty-interdimensional-cable-funniest-shows/),
  [WatchMojo](https://www.watchmojo.com/articles/top-10-best-rick-and-morty-interdimensional-cable-moments-ever)).
- **«Nadie existe a propósito… ven a ver la tele»**: una de las frases
  más citadas, también en China («有时间讨论人生意义？不如来看电视吧»,
  «¿Tiempo para hablar del sentido de la vida? Mejor ven a ver la tele»,
  [Zhihu](https://zhuanlan.zhihu.com/p/383695194)) ✅.
- En China creen que **cada octavo episodio** va de ver la tele
  interdimensional ⚠️ ([Qidian](https://m.qidian.com/ask/qmifowzvxjd)).
  Es cierto en 1×08 y 2×08; el 3×08 es «Morty's Mind Blowers», otro
  episodio de «ver cosas en una pantalla» ✅ (la wiki en español lo llama
  «Los recuerdos de Morty»).

### Qué NO hacer (lo que un fan notaría)

- **No poner a Justin Roiland** (nombre, cara, crédito). Lo despidieron
  en enero de 2023 tras acusaciones; desde la T7 hay voces nuevas en
  inglés ✅. En latino, las voces no cambiaron.
- **No celebrar la salsa Szechuan**: el 7 de octubre de 2017 McDonald's
  la repartió con **sólo unos 20 sobres por local** y hubo colas, policía
  y peleas ✅ ([AV Club](https://www.avclub.com/rick-and-morty-fans-are-going-to-war-with-each-other-ov-1819283376),
  [Know Your Meme](https://knowyourmeme.com/memes/mcdonalds-mulan-szechuan-sauce)).
  Es el lado feo del fandom.
- **No sonar a «hay que ser muy listo para entenderla»**: es un meme
  que se ríe de los fans pedantes ✅ ([Felix](https://felixonline.co.uk/articles/2017-12-13-memes-marketing-and-szechuan-sauce/)).
  La lámina tiene que invitar, no presumir.
- **No mezclar el doblaje de España** con el latino: «¡Miradme!»,
  «la tele», «Ricknillo», «Estamos Cerdis» son de España.
- **No dar brazos a Pepinillo Rick** fuera del traje de ratas: sólo le
  funcionan **ojos y boca** ✅ (resumen del wiki en español).
- **No sombrear ni degradar** a los personajes: son **colores planos con
  línea negra** ✅ (visto en todos los fotogramas).
- **No dibujar pupilas grandes ni ojos brillantes de anime**: son
  **círculos blancos con un punto negro** ✅ (visto). Rick tiene **la
  ceja de lado a lado y los párpados caídos** ✅ (visto en el 1).
- **No usar los fotogramas de cadáveres** (293 y 234) ni el gore.
- **No hacer que parezca IA**: la propia T9 se vendió con «**No AI slop!**
  Just Grade A organic slop, made by real humans» ✅ ([Space](https://www.space.com/entertainment/space-movies-shows/rick-and-morty-season-9-promises-no-ai-slop-just-grade-a-organic-slop-when-it-drops-on-adult-swim-later-this-year),
  [Variety](https://variety.com/2026/tv/news/rick-and-morty-season-9-release-date-ai-slop-1236684010/)).
  Un Rick generado con manos raras o línea temblorosa se notaría el doble.

---

## 15 · Poses analizadas por personaje

Los números son los fotogramas de §3.1 (**vistos** ✅). Los minutos son
escenas del subtítulo cuya postura describo **de memoria** ⚠️: pausa el
vídeo en ese minuto y compruébala.

### Rick

| Ref. | Qué hace | Sirve para |
|---|---|---|
| 1 | Busto de frente, párpados caídos, ceja fruncida, dientes y baba | **Regañar** |
| 290 | Tres cuartos, cansado, boca abierta, brazo apoyado | **Pensar** (con fastidio) |
| 631 | **Palma arriba enseñando un objeto dorado**, la otra mano abierta, luz cálida | **Presentar** (cambia el objeto por el cristal o el mando) |
| 353 | Tiny Rick con **las dos manos arriba** | **Celebrar** |
| 1×08, 0:30 | Abre la caja del cable y mete el cristal ⚠️ | **Explicar** |
| 1×08, 1:00 | «This is infinite TV from infinite universes»: mando en mano, hacia la tele ⚠️ | **Presentar el canal** |
| 1×08, 21:47 | «All right, that's it»: harto de preguntas ⚠️ | **Regañar** |

### Morty

| Ref. | Qué hace | Sirve para |
|---|---|---|
| 2 | De pie, mira arriba, ojos muy abiertos, brazos caídos | **Pensar** / dudar |
| 630 | **Palma arriba**, boca abierta con dientes | **Explicar** |
| 232 | Sentado a la mesa, con el tenedor | Escena doméstica |
| 42 | Tres Mortys en fila | Grupo |
| 1×08, 18:01 | Le dice a Summer «Come watch TV» ⚠️ | **Animar** / invitar |
| 2×08, 19:08 | Su discurso a Summer ⚠️ | **Regañar** |

### Summer

| Ref. | Qué hace | Sirve para |
|---|---|---|
| 3 | **Brazos cruzados**, cejas bajas, junto a la nevera | **Regañar** |
| 339 | **Brazos abiertos, boca abierta**, en la mesa | **Debatir** / protestar |
| 629 | De pie en la cocina, sorprendida | Reaccionar a una noticia |
| 338 | Versión de mundo arrasado, con cicatrices | Acción (no para este canal) |
| 2×08, 13:27 | «I don't want to be that girl, but…» ⚠️ | **Opinar**: el hilo |
| Arte T9 | Atleta con **medalla** ✅ (existe; no lo vi) | **Celebrar** |

### Sr. Meeseeks

| Ref. | Qué hace | Sirve para |
|---|---|---|
| 242 | De pie, sonrisa, brazos largos colgando | **Presentarse** |
| 1×05, 2:35 | Sale de la caja: «I'm Mr. Meeseeks! Look at me!» ⚠️ | **Presentar** |
| 1×05, 2:44 | «All done!» y desaparece ⚠️ | **Celebrar** |
| 1×05, 3:31 | «Ooh, yeah! Can do!» ⚠️ | **Animar** |
| 1×05, 16:42 | «Existence is pain» ⚠️ | **Regañar** (dramático) |

### Pepinillo Rick

| Ref. | Qué hace | Sirve para |
|---|---|---|
| 265 | En su traje de ratas, **brazos arriba, gritando** | **Celebrar** / anunciar |
| 3×03, 0:34 | Tumbado en el banco: «Boom! Big reveal» ⚠️ | **Presentar** una noticia |
| 3×03, 0:55 | «I'm Pickle Rick!» ⚠️ | **Celebrar** |

### Los del cable

| Ref. | Qué hace | Sirve para |
|---|---|---|
| 225 | Michael Thompson con **papeles**, sonrisa | **Dar la noticia** |
| 277 | Vendedor de puertas con los **brazos abiertos** | **Presentar** («¡miren esto!») |
| 184 | Jon **leyendo el periódico «NEWS»** | Leer las noticias |
| 460 | Periodista con **micrófono y la mano levantada** | **Preguntar** / abrir el debate |

### Segunda pasada: poses vistas en vídeo y en las hojas ✅

| Quién | Qué hace | Dónde | Sirve para |
|---|---|---|---|
| Rick | **Arrastra a Morty del brazo**, paso rápido | [intro, 0:08](https://www.dailymotion.com/video/x8x2x8y?t=8) | Regañar, «¡vamos!» |
| Rick | Se levanta y **saca la pistola de portales**: «All right, that's it» | 1×08, 21:45 (transcript de la wiki) | Poner límite |
| Rick | Primer plano cansado, **lata en la mano**, cejas caídas | [tráiler T9, 0:57](https://www.dailymotion.com/video/xae2lba?t=57) | Pensar, hastío |
| Rick | De cuerpo entero con **el aparato del vial verde** | hoja 210 | **Presentar un invento** |
| Morty | **Manos arriba**, asustado, ante una energía azul | [tráiler T1, 0:42](https://archive.org/details/turner_video_391819) | Miedo |
| Morty | **Brazos abiertos** en el garaje | hoja 176 | Explicar, sorprenderse |
| Summer | Vestido morado, **esferas de luz** alrededor, boca abierta | [tráiler T1, 1:30](https://archive.org/details/turner_video_391819) | Asombro (no triunfo) |
| Grupo | Rick, Beth y Summer **con armas en alto** | [tráiler T1, 1:12](https://archive.org/details/turner_video_391819) | Lámina de grupo |
| Sr. Meeseeks | Sale de la caja, **brazos arriba**, dedos abiertos | [clip 1×05, 0:16](https://www.dailymotion.com/video/x7xeqwl?t=16) | **Presentar** |
| Sr. Meeseeks | Visera de golf, **se rasca la cabeza** | [clip golf, 0:50](https://www.dailymotion.com/video/x8bmk63?t=50) | Pensar, no entender |
| Sr. Meeseeks | Docenas gritando, dientes apretados | [clip golf, 1:15](https://www.dailymotion.com/video/x8bmk63?t=75) | Desesperar, en grupo |
| Pepinillo Rick | Brazo arriba con el traje de ratas | hoja 145 | **Celebrar** |
| Pepinillo Rick | De frente con su arma, mirando a cámara | hojas 149 y 35 | **Regañar** |
| Pepinillo Rick | Media sonrisa de listillo | hoja 147 | Presentar |

---

## 16 · Vestuario

| Personaje | Ropa icónica (la que todos reconocen) | Colores | Variantes |
|---|---|---|---|
| **Rick** | **Bata blanca** abierta, camisa **celeste verdoso**, pantalón marrón ✅ (visto y ggsci) | bata `#E8E8E8`, camisa `#97D7D7`, pantalón `#8E774D` ✅ (medido con Pillow en la hoja de modelo [FullBodyRick](https://static.wikia.nocookie.net/rickandmorty/images/6/68/FullBodyRick.png), hoja 210; ggsci da `#917C5D`), pelo `#AAD3E9` | Pepinillo Rick, Tiny Rick, **Rick luchador** (T9) ✅ |
| **Morty** | **Camiseta amarilla** y pantalón azul ✅ | `#FAFD7C` (hoja de modelo: `#FEF665`), pantalón `#314568` ✅ (medido en la [hoja de modelo de Starburns](https://static.wikia.nocookie.net/rickandmorty/images/9/9e/Morty_model_sheet.jpg), hoja 1; ggsci da `#24325F`), pelo `#82491E` | **Morty cabeza de tele** (T9) ✅, Evil Morty con parche ✅ |
| **Summer** | **Camiseta de tirantes rosa**, pelo naranja recogido ✅ | `#E762D7`, pelo `#E89242` | **Atleta olímpica con medalla** (T9) ✅ |
| **Sr. Meeseeks** | Sin ropa: **todo azul** ✅ | `#69C8EC` | Meeseeks marca Kirkland, rosa (524) ✅ |
| **Pepinillo Rick** | **Pepinillo verde** con la cara de Rick; luego traje de ratas ✅ | `#659025` | — |
| **Michael Thompson** | Traje azul oscuro, camisa blanca, corbata oliva ✅ | `#515E6E`, `#918C59` | — |

Accesorio de Rick: **la pistola de portales** (verde) y la petaca ⚠️.

---

## 17 · Paisajes y fondos de pantalla

### Los sitios, con su luz ⚠️

- **Salón de los Smith**: de día, luz plana de ventana; de noche, **la
  tele ilumina** a la familia. Es donde se ve el cable (1×08).
- **Garaje**: luz de tubo, banco de trabajo, cacharros; tiene muchas
  versiones 3D de fans (§4.2).
- **Hospital St. Gloopy Noops** (2×08: la API pone ahí al Dr. Glip-Glop,
  a Shrimply Pibbles y a un periodista, todos del episodio 19, que es el
  2×08 ✅): sala de espera con tele y **rueda de prensa**. Jerry sale a
  hablar en 14:05 («Hello, everyone!») y un portavoz anuncia en
  17:28: «Please, everyone, **I have news** about Shrimply Pibbles» ✅.
- **La Ciudadela de los Ricks** (otra ciudad de la serie ✅, en la API).

### Fondos de pantalla

| Fondo | Tamaño | Enlace |
|---|---|---|
| «Rick and Morty, car, rainbows, Run the Jewels» | **8000×4500** ✅ (bajado y medido) | [Wallhaven](https://w.wallhaven.cc/full/yj/wallhaven-yj1z57.png), subido por baeda |
| «Firewatch × Rick and Morty», montañas al atardecer | **3840×2160** ✅ | [Wallhaven](https://w.wallhaven.cc/full/d5/wallhaven-d51kqj.jpg), subido por wectium; origen en [Reddit](https://www.reddit.com/r/rickandmorty/comments/594jc8/) |
| Rick y Morty, dibujo de fan | **3840×2064** ✅ | [Wallhaven](https://w.wallhaven.cc/full/g8/wallhaven-g8862e.jpg), de HanaSama; origen en [ArtStation](https://www.artstation.com/artwork/0gdRV) |
| «Falling Out», Rick y Morty cayendo | 6300×4500 (dato de Wallhaven) | [Wallhaven](https://w.wallhaven.cc/full/j8/wallhaven-j8gqjm.jpg); autor: kcday en DeviantArt |
| Sr. Meeseeks en la tele, cian | 3840×2160 (dato de Wallhaven) | [Wallhaven](https://w.wallhaven.cc/full/eo/wallhaven-eokvyl.png), subido por MulligaMulle |
| «Rick & Morty: 4K Portal Panic» | **3840×2160** (lo dice la página) | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1099810) (autor y licencia sin comprobar ⚠️) |

Segunda pasada: los tres primeros se bajaron con `curl` para medir el
tamaño; hay 10 más en `partes/datos-imagen.md` (1920×1080 a 6144×3456,
todos con quien los subió). Quité «Wallpapers.com»: era una página con
imágenes, no una imagen. Todos son **de fans**: sólo como referencia.
| Fondos oficiales de la T9 (bolera, valle, cabaña) | ? | [Rick and Morty en X](https://x.com/RickandMorty/status/2046243740625347012?lang=en) |

---

## 18 · Guía para generar con IA (Firefly, Canva)

> [!warning] Úsala sólo para fondos y objetos
> Los **personajes** van siempre de fotogramas reales, recortados con
> `v3/integrar.py`. La serie se vendió en 2026 con «**No AI slop!**»:
> un Rick hecho por IA se nota y un fan lo odiaría.

**Rasgos que nunca cambian** (vistos en los fotogramas):

- **Línea negra de grosor uniforme**, **colores planos**, **sin
  sombras** o con una sola sombra dura.
- Ojos: **círculos blancos grandes con un punto negro**.
- Rick: pelo **celeste en picos**, **ceja única**, párpados caídos,
  **baba** en la comisura, bata blanca.
- Morty: cabeza redonda, pelo castaño liso, **camiseta amarilla**.
- Summer: pelo **naranja recogido**, **top rosa**.

**Paleta**: la de §5.2. Fondo de salón: blanco roto, moqueta tostada y
verde ⚠️; tele: azul grisáceo del plató `#A0BDCF`.

**Luz**: plana, de dibujo de tele. Para el objeto de Blender, luz real
cálida de lámpara + **luz fría de la pantalla**.

**Encuadre**: plano medio frontal, como una sitcom; o **por detrás del
sofá** mirando la tele.

**Palabras que ayudan** (en inglés, que las entienden mejor):
`flat 2D cartoon, thick uniform black outlines, flat colors, no gradients,
Adult Swim sitcom living room, 2010s suburban house interior, plain
daylight, simple background painting, cel animation`

**Palabras que lo estropean**: `anime`, `3D render`, `Pixar`,
`realistic`, `detailed shading`, `glossy`, `cinematic lighting`,
`bokeh`, y **el nombre de la serie o de los personajes** (sale una copia
deformada).

**Qué imágenes usar de referencia**:

- **Estilo**: los fotogramas 225 (plató), 277 (tienda) y 184
  (periódico), y el vídeo «Style Guide».
- **Pose**: 631 (Rick presentando), 630 (Morty explicando), 339
  (Summer protestando), 242 (Meeseeks), 265 (Pepinillo Rick).
- **Salón**: el 3D de fans de [Aziz Saadana](https://www.artstation.com/artwork/D5ZLL0),
  sólo para la distribución de muebles.

---

## 18A · Estilo de dibujo y técnica, y cómo replicarlo (punto 18)

### Con qué se hace (el estudio)

- **Storyboard y animación**: **Toon Boom Storyboard Pro** y **Toon Boom
  Harmony** ✅ ([blog de Toon Boom](https://www.toonboom.com/top-animation-news-mifa-rick-and-morty-the-dragon-prince-and-more)
  y Wikipedia). Es animación **2D**, no 3D.
- **Fondos y diseño de personajes**: **Adobe Photoshop**. Posproducción:
  **After Effects** ✅ (Wikipedia + lo vi en pantalla, abajo).
- **Estudios**: **Bardel Entertainment** (Vancouver), T1-T8. Desde la T9,
  **Mercury Filmworks** (Ottawa). **Lighthouse Studios** (Irlanda) ayuda
  desde la T7. La T1 la produjo **Starburns Industries** (su tarjeta sale
  en el [tráiler de la T1](https://archive.org/details/turner_video_391819),
  0:24) ✅.
- **El orden de trabajo**: storyboard, diseños, *color keys* y fondos en
  Burbank; se montan en Vancouver ⚠️ (cita de Justin Roiland en
  animationmagazine.net, que dio 403: una fuente).
- **Se ve en la hoja `arte-produccion_01.jpg`** (3×03): boceto de fondo de
  **Tommy Scott** (196-203) → pintura final de **Corey Booth** (194, 205,
  207) → personajes encima. Conceptos de línea sin color de **Justin
  Noel** (209, 215-217) ✅.

### Lo vi: el vídeo oficial «Style Guide»

El director de arte **Jeffrey Thompson** dibuja a Morty y a Rick en 2:42
([ficha en Adult Swim](https://www.adultswim.com/videos/rick-and-morty/rick-and-morty-style-guide)).
YouTube pedía iniciar sesión: lo miré en su copia de
[Internet Archive](https://archive.org/details/rick-and-morty-style-guide)
(640×360), con `fotogramas.py --cortes` (66 planos, mirados con Read).
**Esto resuelve el «no pude verlo» de la primera pasada** ✅.

- **0:14**: la barra de título dice **Adobe Photoshop CC 2016.3** (leído
  en dos fotogramas) ✅. Trabaja con 8-11 capas: guías y línea final.
- **0:26-1:22, Morty**: cabeza ovalada con **una guía curva cruzada**;
  **dos ojos de tamaño distinto** con la pupila en el centro; boca de una
  sola curva; orejas pegadas. El cuerpo, primero como **muñeco de
  palitos**, luego la ropa lisa.
- **1:16-2:42, Rick**: **primero el pelo en zigzag**, luego cejas
  fruncidas, arrugas de la frente, **un ojo más cerrado que el otro**,
  boca abierta con dientes.
- **La regla de oro: asimetría a propósito**. Thompson: «the characters
  are often drawn with odd or asymmetrical features, in order to avoid
  looking too normal» ✅ (cita + lo vi en el vídeo: los ojos nunca son
  iguales).

### Lo que dicen los directores de arte

- **James McDermott** (T1-T2), en
  [It's Nice That](https://www.itsnicethat.com/features/inside-rick-and-morty-art-director-james-mcdermotts-sketchbooks-250717):
  todo es **«shape language»** (el dibujo funciona por cómo hablan sus
  formas); los alienígenas, **«squishy and gross but also familiar»**; lo
  doméstico, **cutre a propósito**, para que contraste con lo alienígena;
  cada mundo con su lógica (en un planeta de perros, hasta los coches
  parecen perros). Inspiración: la ciencia ficción de los 70 (*Zardoz*,
  Roger Corman) ✅.
- **Jeffrey Thompson** (T3, venía de *Gravity Falls*), en el
  [Toronto Guardian](https://torontoguardian.com/2017/01/rick-and-morty-artist-jeffrey-thompson/):
  fija el ánimo de cada episodio con **color keys** antes de animar ✅.
- **Justin Roiland**: los dientes y las bocas, por *Los Simpson*; la
  **«boca en W»**, por *Ren & Stimpy* ✅ (Wikipedia, con cita).

### Línea, color y filtros

- **Línea**: negra, gruesa e irregular, casi sin variar de grosor ⚠️
  (análisis de terceros; coincide con lo medido en §5).
- **Sombreado**: **plano**, un solo tono más oscuro, sin degradado. Los
  portales llevan **luz de borde** (*rim light*) verde ⚠️.
- **Baba y líquidos**: formas gráficas planas (gotas, burbujas, anillos),
  nunca fluido realista ⚠️.
- **Filtros**: en los 7 vídeos mirados (§12) no se ve grano ni
  aberración en las escenas normales: imagen limpia. La «señal de tele
  vieja» sólo aparece dentro de los anuncios del cable ⚠️ (no encontré
  fuente del estudio; hay que mirarlo en el 1×08).

### Cómo replicarlo en Photoshop

1. Capa de **guías** (óvalo + cruz), capa de **línea**, capa de
   **relleno** debajo. Como en el Style Guide.
2. Pincel **duro, negro, sin presión** para la línea. Temblor ligero:
   no la hagas perfecta.
3. Relleno plano con el cubo. Bloquea transparencia (candado Alfa) y
   colorea dentro sin salirte ✅ (tutorial de
   [Jason Piperberg](https://jasonpiperberg.com/4140/4140/)).
4. **Sombra**: capa en Multiplicar, un tono, pincel duro. **Brillo** de
   portal: aerógrafo suave en capa **Trama** o **Luz suave** ✅ (mismo
   tutorial).
5. Ojos distintos, pelo de Rick en zigzag, babas sólo en la comisura.

### Cómo replicarlo en Blender

- **Sombreado**: nodo **Shader to RGB** + **ColorRamp** en modo
  *Constant* (dos o tres bloques, no degradado), o **Toon BSDF** ✅ (dos
  fuentes: [Blender Studio](https://studio.blender.org/blog/cartoon-character-shading-with-geometry-nodes/)
  y [artisticrender](https://artisticrender.com/cel-shading-in-blender/)).
- **Contorno**: **Line Art** o **Freestyle** negro, o **Solidify**
  invertido (normales hacia dentro) con material negro sin luz ⚠️
  (técnica genérica; el estudio no usa Blender).
- **Luz**: una sola luz principal fuerte + una de borde verde si hay
  portal. **Render**: Eevee, sin desenfoque de movimiento ni profundidad
  de campo exagerada.
- **Encima, en composición**: una textura de papel o grano **muy
  suave** sobre todo el render, no en el material ✅ (mismas dos
  fuentes). Para la pantalla de la tele, la estática de §18B.
- **Modelos y rigs libres** (licencia leída en la API de Sketchfab):
  [Morty Rig Blender](https://sketchfab.com/3d-models/morty-rig-blender-c99a7fbd39b84428ab99ec1af4b15800)
  de mfxmotions y [Portal gun](https://sketchfab.com/3d-models/portal-gun-rick-and-morty-ac3226c6b9e64142af2065409f0162ee)
  de kreems, los dos **CC BY 4.0** ✅ (crédito: «<modelo>» de <autor>
  (Sketchfab), CC BY 4.0). La **Meeseeks Box** de MagunDongle ya **no
  devuelve licencia**: sólo para mirar ⚠️. Más modelos con licencia en
  §4 y §18F.

### Encuadres y composición (lo que vi en vídeo)

- **Presentar**: plano medio frontal, personaje centrado, brazos arriba
  (Meeseeks saliendo de la caja,
  [1×05, 0:16](https://www.dailymotion.com/video/x7xeqwl?t=16)).
- **Grupo**: todos de pie en fila, armas en alto, cámara a la altura del
  pecho ([tráiler T1, 1:12](https://archive.org/details/turner_video_391819)).
- **Caos**: plano general lleno hasta los bordes (la sala de Meeseeks,
  [1×05, 1:10](https://www.dailymotion.com/video/x8bmk63?t=70)).
- **Cansancio o drama**: primer plano de Rick con la lata
  ([tráiler T9, 0:57](https://www.dailymotion.com/video/xae2lba?t=57)).
- **Amenaza o poder**: contrapicado (el rascacielos de Tommy Scott, hoja
  196); **algo delante del personaje** (hombros de los agentes, hoja 173).
- No encontré una entrevista del estudio sobre planos por emoción: lo de
  arriba sale de mirar los vídeos, no de una regla escrita.

---

## 18B · Texturas 2D (punto 19)

**Lo primero**: Rick y Morty está pintada **plana** (§18A). No es manga:
**no hay tramas** de puntos ni pinceladas a la vista. Su «textura 2D»
está en los **emblemas y logos**, en algún **patrón de ropa** y en el
**ruido de tele** de los anuncios del cable. Si una capa de la lámina
lleva textura, que sea poca.

### Emblemas y logos de la serie (tamaño medido con la API de Fandom)

| Emblema | Tamaño | Para qué |
|---|---|---|
| [Insignia del Consejo de Ricks](https://static.wikia.nocookie.net/rickandmorty/images/0/02/RickCouncilBadge.png): escudo dorado tipo placa | 830×962 | **Sello** o marca de agua en una lámina «oficial» ✅ |
| [Logo de Blips and Chitz](https://static.wikia.nocookie.net/rickandmorty/images/b/b8/BlipsChitzBack.png), el salón recreativo galáctico | 263×266 | Rótulo de neón de un sitio de la serie ✅ |
| [Logo de Adult Swim](https://static.wikia.nocookie.net/rickandmorty/images/d/dc/2000px-Adult_Swim_2003_logo.svg.png), la cadena | 2000×370 | Cartela de «presenta» ✅ (marca registrada: sólo como referencia) |
| [Caja del juguete Story Train](https://static.wikia.nocookie.net/rickandmorty/images/a/ac/Story_train.png) (3×02) | 774×444 | Cómo es **el envoltorio de un juguete** dentro de la serie: sirve para la funda de la caja Meeseeks del concepto C ✅ |

El logo de la serie y su letra están en §6.

### Patrones de ropa

- Los protagonistas visten **colores lisos**, sin estampado (medido en
  §16: bata `#E8E8E8` y pantalón `#8E774D` de Rick; camiseta `#FEF665` y
  pantalón `#314568` de Morty, medidos en las hojas de modelo 210 y 1).
- Los únicos patrones reales: el **mono a rayas de presidiario** de Rick
  (varios capítulos) y el **traje de rombos** del Sr. Pantalones de Popó
  (Mr. Poopybutthole) ⚠️ (vistos, no medidos).

### Texturas y pinceles libres (licencia leída en su página)

| Para qué | Recurso | Licencia |
|---|---|---|
| **Estática de tele** (la pantalla sin señal, el efecto VHS del noticiero) | [CC0 Textures](https://cc0-textures.com/) y la textura «AbstractVarious0025» (*noise TV static*) de Textures.com | CC0 / uso libre con cuenta gratis ✅ |
| **Trama de puntos** de cómic (fondo de un rótulo, el periódico del concepto C) | [Brusheezy, «comic halftone»](https://www.brusheezy.com/free/comic-halftone) (155 pinceles) | Creative Commons / Free: **mira cada pack** ✅ |
| **Grano de papel** encima del render (muy suave) | [Paper 006](https://ambientcg.com/a/Paper006) y [Paper 001](https://ambientcg.com/a/Paper001) de ambientCG | **CC0** ✅ (todo ambientCG es CC0) |
| **Tela** del sofá o del cojín | [Fabric 061](https://ambientcg.com/a/Fabric061) de ambientCG | **CC0** ✅ |

Las texturas reales de madera, metal y vidrio (tele, mueble, garaje)
están en §5, con Poly Haven (CC0). Los modelos 3D, en §4.

- ⚠️ No encontré un *artbook* ni un *making of* que enseñe los
  archivos de textura del estudio: el «Style Guide» sólo enseña reglas de
  dibujo.

---

## 18C · Gustos y detalles de cada personaje (punto 20)

**No hay ficha oficial** con altura, cumpleaños o comida favorita del
reparto principal. Busqué el *Rick and Morty Character Guide* (Dark
Horse, 2020): es un libro de personajes secundarios, narrado como informe
de un gromflomita, y no trae esos datos ⚠️
([ficha en Fandom](https://rickandmorty.fandom.com/wiki/Rick_and_Morty_Character_Guide)).
La wiki sólo da altura y grupo sanguíneo de **Mullet Rick** y su Morty
(versiones alternativas de «Fighting Mother») y avisa de que **no se
sabe si valen** para los protagonistas ✅. No lo uses para Rick C-137.

Todo lo de abajo sale de la wiki en inglés (secciones *Trivia* y
*Relationships*, leídas en su wikitexto por la API), con el capítulo.

| Personaje | Objeto que siempre lleva | Le encanta | Odia o le da miedo | Cómo se ve a sí mismo |
|---|---|---|---|---|
| **Rick** | La **pistola de portales**; bebida en la mano **izquierda** ⚠️ | El **bajo**: tocaba en **The Flesh Curtains** con Squanchy y Ave Persona («Get Schwifty» y 5×08) ✅. Los planetas ⚠️ («Childrick of Mort») | **Los piratas** ✅ («Anatomy Park» y «Unmortricken»). La rutina: quema su propia tienda antes que atarse a ella («Something Ricked This Way Comes») ✅ | «The hardest working liver in the galaxy» («Look Who's Purging Now») y, desde la T3, «el ser más listo del universo» ✅ |
| **Morty** | Nada fijo: depende del capítulo | **Jessica**, su compañera de clase, desde el 1×01 ✅. Los juegos de **Blips and Chitz** | El caos que trae Rick; se avergüenza fácil | Se cree normal y torpe. La serie lo muestra más valiente de lo que cree («Raising Gazorpazorp», «Anatomy Park») ✅ |
| **Summer** | El **móvil** (al principio); trofeos de voleibol en su cuarto ⚠️ | Los mundos **posapocalípticos** («Rickmancing the Stone») ⚠️. Dice «**boo-yah**» ✅ | La película *The Purge*; que la traten de niña ⚠️ | Empieza pendiente de su popularidad; luego compite con Morty por ir de aventura con Rick |
| **Sr. Meeseeks** | **La caja** de la que sale | Cumplir su tarea y **desaparecer** ✅ (1×05) | Una tarea imposible: «Existence is pain» (1×05, 16:42) ✅ | Una herramienta feliz, nunca alguien con derecho a seguir existiendo |
| **Pepinillo Rick** | El **traje de ratas** cosidas: sus «brazos» ✅ | Presumir: «Boom! Big reveal!» ✅ | **La terapia familiar**: por eso se volvió pepinillo (3×03) ✅ | Invencible («I'm Pickle Rick!»), aunque sólo mueve ojos y boca |

**Más detalles con fuente** (útiles para escribir en su voz):

- **Rick llora a escondidas por Morty**: en «Close Rick-counters of the
  Rick Kind» (1×10) ve recuerdos de Morty, se le escapan las lágrimas y
  dice que es «alérgico a los idiotas» ✅. En «A Rickle in Time» (2×01)
  se ofrece a sacrificarse por él ✅. Esto quita el ⚠️ «de memoria» de §8.
- **Rick es ambidiestro**: escribe con la derecha, bebe y dispara con la
  izquierda ⚠️ (una fuente). Grupo sanguíneo **B negativo** ⚠️.
- **Rick hispano**: en el comentario de audio de «Auto Erotic
  Assimilation» (2×03) los creadores dicen que es de origen hispano,
  medio en broma ⚠️ (una fuente, no lo oí).
- **Morty**: agnóstico ⚠️. Bajo la Federación Galáctica su «edad legal»
  pasa a 35 años (3×01): es un chiste, tiene 14 ✅.
- **Summer**: la wiki calcula que nació el **23 de noviembre de 1996**
  (17 años en 2013) ⚠️ (cálculo, no se dice en pantalla). **Bisexual**,
  confirmado en «The Old Man and the Seat» (4×02) ✅.
- **Sr. Meeseeks**: casi no cambia de nombre al doblarse (en francés,
  «Monsieur Larbin»; en italiano, «Mr. Miguardi») ⚠️. Sale también en el
  videojuego de Blips and Chitz dando consejos («Mortynight Run») ✅. El
  bot **MEE6** de Discord tomó su nombre y su cara ⚠️ (wiki, *Trivia*).

---

## 18D · Por qué la gente la ama (punto 21)

### Las razones, con cifras

- **Dos Emmy a Mejor Programa Animado**: 2018 por «Pickle Rick» y 2020
  por «The Vat of Acid Episode» (4×08) ✅
  ([Deadline](https://deadline.com/2020/09/rick-and-morty-outstanding-animated-program-1234580001/),
  [IndieWire](https://www.indiewire.com/awards/industry/rick-and-morty-wins-emmy-outstanding-animated-program-1234585898/)).
  Nominada otra vez en 2022 ✅
  ([Nerds and Beyond](https://www.nerdsandbeyond.com/2022/07/12/rick-and-morty-nominated-for-outstanding-animated-program-at-the-2022-emmys/)).
- **Crítica**: T1 con 97 % en Rotten Tomatoes; T3 y T4, 96 %. La **T9
  (2026) empezó con 100 % de crítica y 89 % de público**, su mejor
  arranque sin Justin Roiland ✅
  ([CBR](https://www.cbr.com/rick-and-morty-season-9-rotten-tomatoes-score/),
  [Screen Rant](https://screenrant.com/rick-morty-season-9-audience-rotten-tomatoes-score-debut/)).
- **Se ve mucho**: en 2026, n.º 2 del top 10 mundial de HBO Max (tras
  *Euphoria*) y n.º 1 en Apple TV ✅
  ([CBR](https://www.cbr.com/rick-and-morty-season-9-instant-success/)).
- **Mueve cosas fuera de la tele**: una frase de Rick sobre la salsa
  Szechuan (3×01, 5:03) acabó en **20 millones de sobres** de McDonald's
  (§18F) ✅.
- **El porqué, en corto**: ciencia ficción de verdad (Dan Harmon:
  «*Los Simpson* con *Futurama*»), chistes rápidos y, de golpe, **una
  escena que duele**. Rick parece cínico pero **quiere a Morty**
  (llora a escondidas en 1×10, §18C). Esa mezcla es lo que más se repite
  en Reddit.

### Con quién se identifica la gente

En el hilo de Reddit [«Which character do you identify with most?»](https://www.reddit.com/r/rickandmorty/comments/1r2zhxh/which_character_do_you_identify_with_most/)
(833 votos, 475 comentarios; citas leídas con Arctic Shift) ✅:

- **Beth**: «I relate to Beth (…) I grew up without my dad around». El
  padre ausente y el talento que no llegó a usar.
- **Jerry**: «Jerry 100%. I need a job». La inseguridad, con humor.
- **Summer**: «Summer 10000000%». La segunda más repetida.
- **Morty**: «on my best days I'm Morty. I'm generally a Jerry». Morty
  es el «yo ideal»; Jerry, el «yo real».
- **Rick**: pocos se reconocen en él: lo quieren **como aspiración**.

**Para el canal**: la gente se ríe con Rick, pero **se reconoce** en Beth,
Jerry y Summer. Summer, la que opina fuerte, funciona como voz de un canal
de comentarios (ya lo decía §9).

### Las escenas que hacen llorar

| Escena | Qué pasa | Por qué duele | Música y dibujo | Cómo reaccionó la gente |
|---|---|---|---|---|
| **1×08, 18:01-18:06** «Nobody exists on purpose» | Morty le cuenta a Summer que su Morty original murió y que él lo enterró en el jardín | El protagonista miedoso dice lo más duro de la serie **y lo cierra con un «Come watch TV»** | Los dos solos junto a la tumba del jardín, sin música de fondo ⚠️ (de memoria, sin fotograma; la tumba viene del 1×06: hoja 185, Rick y Morty cavando) | Es **la frase más citada** del episodio (§2) ✅ |
| **1×08, 20:14** | Beth y Jerry deciden seguir juntos | La pareja que no se aguanta elige quedarse | Suena **Mazzy Star** («Give me a name / Hear my faith…») ✅ subtítulo | — |
| **1×11, 18:22** «Wubba lubba dub dub» | Ave Persona le explica a Morty qué significa la frase de Rick | El grito de fiesta de Rick era, en su idioma, **«estoy sufriendo mucho, ayúdenme»** ✅ | Charla tranquila en plano medio ⚠️ | Se volvió un dato que todo fan conoce (§18H) |
| **5×03** «A Rickconvenient Mort» (4-jul-2021) | Morty rompe con **Planetina**, su primera novia de verdad, y llora en brazos de **Beth** | La misma canción sonó antes en el montaje feliz de la pareja: **vuelve para la ruptura** | **«I Am the Antichrist to You», de Kishi Bashi** ✅ | Adult Swim sacó un **vídeo musical** de la escena ✅ ([ComicBook](https://comicbook.com/anime/news/rick-and-morty-season-5-morty-planetina-break-up-flowers-music-video-adult-swim/), [Newsweek](https://www.newsweek.com/rick-morty-season-5-episode-3-morty-planetina-relationship-explained-1606826)). Minuto sin medir ⚠️ |
| **7×04** «That's Amorte» (5-nov-2023) | Un anciano cuenta que fue **el último de su planeta en quitarse la vida** | La serie habla de salud mental sin chiste; el episodio abre con **aviso de contenido** | Flashback ⚠️ (sin ver) | En Reddit: «the flashback from the old man (…) just hit me. It humanizes him» ✅ ([Variety](https://variety.com/2023/tv/news/dan-harmon-rick-and-morty-season-7-episode-4-spaghetti-interview-1235779646/), [Reddit](https://www.reddit.com/r/rickandmorty/comments/1mde14b/what_is_the_saddest_episode_of_rick_and_morty/)) |

Los hilos [«What is the saddest episode?»](https://www.reddit.com/r/rickandmorty/comments/1mde14b/what_is_the_saddest_episode_of_rick_and_morty/)
(403 votos), «What is your saddest scene?» (625) e «Is this the saddest
scene in the entire show?» (2004) repiten Planetina y el espagueti. Citan
también el final de la T8, sin decir el capítulo ⚠️.

### Las que hacen reír o gritar

- **3×03, 0:34 y 0:55**: «Boom! Big reveal... I'm a pickle» y «**I'm
  Pickle Rick!**» ✅ (subtítulo). Ganó el Emmy de 2018.
- **1×05, 2:35**: «**I'm Mr. Meeseeks! Look at me!**», brazos arriba
  ([vídeo, 0:16](https://www.dailymotion.com/video/x7xeqwl?t=16)) ✅. Y la
  sala llena de Meeseeks gritando
  ([vídeo, 1:10](https://www.dailymotion.com/video/x8bmk63?t=70)) ✅.
- **2×05, 0:32 y 5:54**: «**Show me what you got**» y «**Get schwifty**» ✅.
- **1×08, 3:37 y 9:59**: *Ants in My Eyes Johnson* y *Real Fake Doors*,
  los anuncios más compartidos ✅ (§2).

---

## 18E · Fan dubs y comunidad hispana (punto 22)

### Doblajes de fans en YouTube

Canal, fecha y vistas sacados con `yt-dlp --skip-download` (no de
memoria), el 25-sep-2026.

| Fandub | Canal | Fecha | Vistas | Enlace |
|---|---|---|---|---|
| Escena de **Pepinillo Rick** doblada por fans | zeusupchuck | 8-ago-2017 | 17 820 | [YouTube](https://www.youtube.com/watch?v=54KRtXDG1jU) ✅ |
| «Rick & Morty - Allahu Akbar», escena de humor | Kitsumaur | 3-may-2017 | 6 037 | [YouTube](https://www.youtube.com/watch?v=nKvcKRyR_fY) ✅ |
| «Rick and Morty **Señor Mezeeks** Fandub»: **un solo actor dobla a todos** (primer trabajo del canal) | Moises Aldana | 13-jul-2018 | 81 | [YouTube](https://www.youtube.com/watch?v=RKui4ah87xY) ✅ |
| «RICK Y MORTY ROBAN EL OMNITRIX»: cruce con *Ben 10* | Kicker Professional | sin dato | sin dato | [YouTube](https://www.youtube.com/watch?v=UL5uk05WVCg) ⚠️ (yt-dlp no respondió) |
| «EL FUTURO DE RICK Y MORTY» (*short*) | CHUCKLEBONE | sin dato | sin dato | [YouTube](https://www.youtube.com/shorts/vugSeeML1nQ) ⚠️ |

- **Redoblaje de fans del gag de *Los Simpson***: las primeras voces
  latinas de Rick y Morty fueron mexicanas, en el gag del sofá de
  «Hazaña matemática» (2015): **Ismael Castro** (Rick) y **Bruno
  Coronel** (Morty) ✅ (§10). En 2020, **Juan Guzmán y Eder La Barrera**
  lo redoblaron por su cuenta para el canal DALEHHOR STUDIOS ⚠️ (Doblaje
  Wiki, [vídeo](https://youtu.be/QaQdbhepkH8)).

### Covers del opening

**No hay**: la serie no tiene canción de entrada con letra. Abre con una
viñeta distinta cada vez y la tarjeta del título sobre un riff de Ryan
Elder ([intro vista, 0:32](https://www.dailymotion.com/video/x8x2x8y?t=32)) ✅.
Por eso no busques covers cantados: los fans doblan **escenas**.

### Memes y comunidad en español

- **Memes**: colección activa en [Memedroid, «Rick Y Morty en
  español»](https://es.memedroid.com/memes/tag/rick+y+morty) ⚠️ (sin contar
  vistas).
- **Audios en TikTok**: categoría [«Audios De Rick Y Morty En
  Español»](https://www.tiktok.com/discover/audios-de-rick-y-morty-en-espa%C3%B1ol) ⚠️.
- **Los actores y el cambio de voces**: la comunidad de doblaje sigue de
  cerca los cambios de reparto. El canal de TikTok
  [estrelladoblaje](https://www.tiktok.com/@estrelladoblaje/video/6994486723602386182)
  habla del cambio de voz de **Beth** ⚠️. Y en YouTube hay recopilaciones
  como «Voces de RICK Y MORTY en 1 minuto» y «Evolución de todas las
  voces… en español latino (2013-2024)» (§12).
- **Beth cambia de voz tres veces**: Rebeca Aponte (T1-T6), Carmen Lugo
  (T7-T8) y **Arlet Matute** (T9) ✅ (§10). Es un buen tema para el canal:
  «¿qué voz de Beth prefieres?».
- **Para Sintonizando**: las frases que más se doblan en fandubs son las
  de §2 y §10 («¡Soy el Señor Meeseeks!» ✅; «I'm Pickle Rick!» en su
  versión latina, sin fuente textual ⚠️). Un
  **reto de doblaje** con la escena de Pepinillo Rick (3×03, 0:34-0:55)
  encaja con el servidor.

---

## 18F · Colaboraciones, figuras y cosplay (punto 23)

Su arte trae **ropa y poses nuevas**: sirve como referencia extra.

### En otros juegos

- **Fortnite**, tres tandas ✅ (dos fuentes cada una):
  - **1**: Rick Sanchez, pase de batalla del Capítulo 2 Temporada 7 (8
    de junio de 2021).
  - **2**: **Mecha Morty**, **Queen Summer** y **Mr. Poopybutthole**, en
    la tienda el 22 de agosto de 2021.
  - **3**: **Pepinillo Rick** y **Rick Prime**, el **7 de marzo de 2026**,
    con Mr. PB y Squanchy de acompañantes
    ([esports.gg](https://esports.gg/news/fortnite/fortnite-x-rick-and-morty-wave-3/),
    [Beebom](https://beebom.com/rick-and-morty-skins-in-fortnite/)).
    **El Pepinillo en 3D, con pose de juego**: referencia viva para el
    concepto B.
- **MultiVersus** (lucha de Warner): **Morty** desde el 23-ago-2022 y
  **Rick** desde el 27-sep-2022 (usa sus inventos); **Evil Morty** en la
  beta ✅ (Variety, Multiversus Wiki, Destructoid). Dejó de venderse el
  30-may-2025; se juega sin conexión.
- **Merge Dragons!**: evento «Froopy Flight» (hasta el 13-jul-2020) ✅
  (Bleeding Cool + ficha del juego).
- **DOTA 2**: paquete de voces de anunciador de Rick y Morty ✅ (Game Rant).
- **Clone Rumble**: juego propio de colección para móvil (2020) ⚠️ (una
  fuente, Android Police).

### Marcas, tele y cómic

- **McDonald's y la salsa Szechuan**: Rick la pide en el 3×01 (5:03).
  Promo fallida el **7-oct-2017** (unos 20 sobres por local, colas y
  enfados) y relanzamiento el **26-feb-2018** con **20 millones de
  sobres** ✅ (Time, Snopes, Fortune). Ojo con celebrarlo: ver «qué NO
  hacer» en §14.
- **Gag del sofá de *Los Simpson*** (mayo de 2015): **2 min 21 s**, el
  más largo de *Los Simpson*; Roiland pone las voces ✅ (The Hollywood
  Reporter, Wikisimpsons).
- **Corto de anime oficial «Samurai & Shogun»** (29-mar-2020, Toonami):
  lo hizo **Studio DEEN**, dirigido por **Kaichi Satō**. Rick samurái,
  Morty *shōgun*, **hablado en japonés** con las voces del **doblaje
  japonés** de la serie (**Youhei Tadano** y **Keisuke Chiba**) ✅ (Anime
  News Network, GameSpot, Toonami Wiki). **Para un servidor de doblaje,
  la colaboración más interesante.**
- **Cómic *Rick and Morty vs. Dungeons & Dragons*** (IDW y Oni Press) ✅.

### Eventos y bares

- **Bar temporal «Wubba Lubba Dub PUB»** (Washington D. C., agosto de
  2018): tres barras (el garaje de Rick, Anatomy Park, la nave), cócteles
  con nombres de la serie, *Real Fake Doors* y un plumbus en el techo ✅
  (Inverse, The Manual). Hubo más de este tipo, también en Latinoamérica.
- **El Rickmobile** (la autocaravana oficial de la gira) en el **desfile
  de Dragon Con**, Atlanta, **5-sep-2026**, con cosplayers elegidos por
  Adult Swim y máscaras gratis para el público ✅
  ([X oficial](https://x.com/RickandMorty/status/2095612579389345981),
  [Adult Swim Central](https://adultswimcentral.com/2026/08/07/rickmobile-dragon-con-parade/),
  [Bleeding Cool](https://bleedingcool.com/tv/calling-all-cosplayers-rick-and-morty-needs-some-help-at-dragon-con/)).
- **Mural pintado a mano** por **Colossal Media** en Los Ángeles para la
  T9 ✅.

### Figuras oficiales (su pose es referencia 3D)

- **Funko Pop!**: desde 2016; unas **103 figuras**, entre ellas Rick y
  Morty armados, Sr. Meeseeks, Mr. Poopybutthole, Ave Persona, Squanchy,
  Snowball y **seis Pepinillo Rick** distintos ✅ (GrailNest, Cardboard
  Connection). Sirven para ver **al Pepinillo en volumen**.
- **McFarlane Toys**: sets de bloques compatibles, como «Spaceship and
  Garage» (unas 294 piezas) y «Evil Rick and Morty» con portal ✅
  (mcfarlane.com, Walmart). **El set del garaje** es una maqueta real del
  sitio del concepto B.
- **No hay LEGO oficial**: lo que sale como «Rick and Morty Lego» son
  montajes de fans ✅.
- **Pelota antiestrés del Sr. Meeseeks**: producto oficial (hoja 218).

### Cosplay

- El de referencia es el **oficial de Dragon Con 2026** (arriba): trajes
  hechos para Adult Swim, con volumen real.
- Lo que un cosplay bien hecho tiene que tener: la bata **blanca y
  rígida**, la camisa `#97D7D7`, el **pelo de Rick en pinchos** hacia
  atrás y la pistola de portales con **líquido verde** que brilla (§16) ⚠️
  (consejos míos a partir de §16; no encontré un tutorial con materiales
  que valga la pena citar).

---

## 18G · Obras parecidas y temas relacionados (punto 24)

### De dónde viene

- **Nació de una parodia de *Volver al futuro***: el corto de 2006 **«The
  Real Animated Adventures of Doc and Mharti»**, de Justin Roiland, para
  el festival **Channel 101** (cofundado por Dan Harmon). Doc y Mharti
  pasaron a ser Rick y Morty; el viaje en el tiempo se volvió viaje entre
  dimensiones para evitar líos legales ✅ (tres fuentes:
  [wiki](https://rickandmorty.fandom.com/wiki/The_Real_Animated_Adventures_of_Doc_and_Mharti),
  [Inverse](https://www.inverse.com/article/30812-rick-and-morty-troll-back-to-the-future-justin-roiland-origin-original-short),
  [Screen Rant](https://screenrant.com/rick-and-morty-back-to-the-future-origins-explained/)).
- **Harmon la define** como *Los Simpson* cruzado con *Futurama*:
  familia normal + ciencia ficción dura ✅ (Wikipedia, con cita).
- **Influencias británicas**: *The Hitchhiker's Guide to the Galaxy* y
  *Doctor Who* ✅ (Wikipedia).
- **Dibujo**: la boca en W viene de *Ren & Stimpy*; los dientes, de *Los
  Simpson*; el diseño, de la ciencia ficción de los 70 (*Zardoz*, Roger
  Corman) ✅ (§18A).

### Series del mismo tono

- **La más cercana: *Solar Opposites*** (Hulu), de **Justin Roiland y
  Mike McMahan**, los dos de Rick y Morty. Mismo dibujo y mismo humor,
  pero **sin** el «círculo de historia» (*story circle*) de Dan Harmon
  que ordena cada capítulo de Rick y Morty ✅
  ([Bubbleblabber](https://www.bubbleblabber.com/2020/06/exploring-the-similarities-and-differences-between-rick-and-morty-and-solar-opposites/),
  [Inverse](https://www.inverse.com/entertainment/solar-opposites-review-justin-roiland-hulu)).
- **Lista de TVLine** («si te gusta Rick y Morty») ✅
  ([TVLine](https://www.tvline.com/2121225/tv-shows-like-rick-and-morty/)):
  *Futurama*, *Star Trek: Lower Decks* (también de Mike McMahan), *The
  Venture Bros.*, *Doctor Who*, *Back to the Future: The Animated
  Series*, *Space Ghost Coast to Coast*, *South Park*, *American Dad!*,
  *BoJack Horseman*, *Loki*, *The Sandman*, *Bill & Ted*, *Voyagers!* y
  *Aeon Flux*.
- **Su propio anime**: *Rick y Morty: El anime* (2024), con otro reparto
  latino (§10), y el corto de Studio DEEN (§18F).

### Otras láminas del servidor (para no repetir ideas)

- **Ningún otro encargo usa #noticias-series** (`grep -il noticias-series
  encargos/*.md` sólo da este) ✅: no hay choque de canal.
- **Parecidas por tono o dibujo**, y qué no repetir:
  - **14 · Hora de aventura** (#musica-nueva): su concepto C es la
    «mixtape de **BMO**», una consola con pantalla. **No repitas** «un
    personaje dentro de una pantalla» igual: en el concepto A de Rick y
    Morty la tele es **un aparato del salón**, con la caja del cable
    abierta, no un personaje.
  - **15 · Bob Esponja** (#ofertas-y-gratis): su concepto A es «la caja
    de Don Cangrejo». La **caja Meeseeks** (concepto C) tiene que verse
    distinta: **caja de juguete con botón y funda impresa**, no una caja
    registradora.
  - **26 · Scooby-Doo** (#dudas): dibujo animado occidental, pero de
    misterio y tablero de pistas: no choca.
  - **27 · Cyberpunk: Edgerunners** (#a-que-juegas): ciencia ficción
    adulta, pero en estilo anime y con recreativa y neones. Evita el
    **neón morado**: aquí manda el verde de portal.
- Ninguna otra comparte el humor cínico y adulto de Rick y Morty.

---

## 18H · El mundo, la historia y sus símbolos (punto 25)

### Las reglas del mundo, en cinco líneas

1. Hay **infinitos universos**. Rick salta entre ellos con la **pistola
   de portales** ✅ ([wiki, *Portal Gun*](https://rickandmorty.fandom.com/wiki/Portal_Gun)).
2. Todos los Ricks viven dentro de la **Curva Finita Central**: un muro
   que encierra los universos donde **Rick es el más listo**. Fuera, no
   lo sería ✅ ([wiki](https://rickandmorty.fandom.com/wiki/Central_Finite_Curve); lo cuenta Evil Morty en 5×10).
3. Los Ricks de mil dimensiones viven en **la Ciudadela**, gobernada
   primero por el **Consejo de Ricks** y luego por un Morty presidente
   (Evil Morty) ✅ ([wiki](https://rickandmorty.fandom.com/wiki/The_Citadel)).
4. La pistola la inventó **Rick Prime**, que mató a la mujer y a la hija
   de Rick C-137 (Diane y Beth). De ahí sale su venganza ✅ (wiki).
5. Pase lo que pase en el espacio, **todo vuelve a la casa de los Smith**,
   una casa normal de las afueras. Lo doméstico, cutre; lo alienígena,
   elaborado ✅ (James McDermott, §18A).

### La historia por arcos

Fuente: [Den of Geek, «Just the Lore Episodes»](https://www.denofgeek.com/tv/rick-and-morty-just-the-lore-episodes/),
cruzada con la wiki ✅.

- **1 · El multiverso** (T1): en «Rick Potion #9» (1×06) Rick y Morty
  **rompen su mundo** y se mudan a otro donde sus «yo» acaban de morir:
  **se entierran a sí mismos** en el jardín. En 1×10 aparecen la
  Ciudadela, el Consejo y **Evil Morty**.
- **2 · La Federación Galáctica** (T2-T3): la boda de Ave Persona
  (2×10) es una trampa; la Federación ocupa la Tierra y Rick se entrega.
  «The Rickshank Rickdemption» (3×01) lo libera. En «The Ricklantis
  Mixup» (3×07) **Evil Morty llega al poder** en la Ciudadela.
- **3 · El pasado de Rick** (T5-T6): «Rickternal Friendshine of the
  Spotless Mort» (5×08) enseña su vida joven y la muerte de Diane.
  «Rickmurai Jack» (5×10) explica la Curva. En la T6 se sabe que el
  asesino fue **Rick Prime**.
- **4 · La caza de Rick Prime** (T7): en «Unmortricken» (7×05) Rick y
  Evil Morty se alían y casi lo vencen. «Fear No Mort» (7×10) enseña la
  vida que Rick pudo tener.
- **5 · Después** (T8-T9): en la T8, Summer y Morty escapan de una
  simulación. La **T9** (estreno: 25-may-2026, §12) abre con «There's
  Something About Morty»: Rick y Evil Morty trabajaban juntos en secreto
  contra una amenaza nueva para la Curva, **el Colectivo** ⚠️ (T9: una
  sola fuente).

### Símbolos, objetos y palabras que un fan reconoce al instante

| Símbolo | Qué es | Dónde |
|---|---|---|
| **La pistola de portales** | Abre un **portal verde en espiral**; necesita un líquido verde que brilla | [wiki](https://rickandmorty.fandom.com/wiki/Portal_Gun) · verde medido en §5 |
| **El portal** | Anillo lima `#AFDB30` con centro `#DAF81E`, casi blanco `#DEF7D7` si es suave | medido en [vídeo, 0:20](https://www.dailymotion.com/video/x3jf16p?t=20) ✅ |
| **La insignia del Consejo** | Escudo dorado de los Ricks | [imagen, 830×962](https://static.wikia.nocookie.net/rickandmorty/images/0/02/RickCouncilBadge.png) (§18B) |
| **La caja Meeseeks** | Aprietas el botón y sale un Meeseeks que cumple un deseo y desaparece | 1×05, 2:31 (§2) |
| **El plumbus** | Objeto doméstico alienígena que nadie entiende | 2×08, 8:03 y 14:52 (§2) |
| **El cable interdimensional** | La tele que ve todos los universos | 1×08 y 2×08 (§2) |
| **Blips and Chitz** | Recreativa galáctica con el juego «Roy: A Life Well Lived» | [wiki](https://rickandmorty.fandom.com/wiki/Blips_and_Chitz) |
| **Jerryboree** | Guardería de Jerrys en un asteroide | [wiki](https://rickandmorty.fandom.com/wiki/Jerryboree) |
| **Los Vindicadores** | Equipo de superhéroes, parodia de Los Vengadores | [wiki](https://rickandmorty.fandom.com/wiki/The_Vindicators) |
| **Cristales de la muerte** | Enseñan cómo vas a morir | [wiki](https://rickandmorty.fandom.com/wiki/Death_Crystal) |
| **El mundo Cronenberg** | Humanidad convertida en monstruos por un antídoto de Rick (1×06) | [wiki](https://rickandmorty.fandom.com/wiki/Cronenberg_World) |
| **Mr. Poopybutthole** | Amigo de la familia; dice «**Ooh-wee!**» y resume las temporadas | [wiki](https://rickandmorty.fandom.com/wiki/Mr._Poopybutthole) · 2×10, 22:01 |

**Palabras propias** (en el doblaje latino se dejan casi todas en
inglés, §7 y §10):

- «**Wubba lubba dub dub**»: el grito de Rick. En el idioma de Ave
  Persona significa «estoy sufriendo mucho, ayúdenme» (1×11, 18:22) ✅
  ([wiki, *Birdperson*](https://rickandmorty.fandom.com/wiki/Birdperson)).
- «**Get schwifty**» (2×05, 5:54), «**Show me what you got**» (2×05, 0:32).
- «**I'm Pickle Rick!**» (3×03, 0:55); «**Existence is pain**» (1×05,
  16:42).
- **Salsa Szechuan** (3×01, 5:03), **Cronenberg** (monstruo mutante),
  **Squanch** (el verbo de Squanchy, vale para todo) ⚠️ (de memoria).

---

## 19 · Tres conceptos para la lámina de #noticias-series

Los tres usan los textos de §0. Donde una frase va «en la voz de la
serie» y no encontré su versión latina, lo digo: es **traducción mía**.
Recortes siempre por `v3/integrar.py` y comprobados a 1:1. Los
personajes, de **fotogramas en 1080p** sacados en el PC en los minutos
que doy (los de 300×300 de la API sólo sirven para elegir la pose).

### Concepto A — «TV infinita» (la tele de los Smith, el objeto del plan)

- **Objeto y sitio**: el **salón de los Smith**, de noche. **La tele**
  sobre su mueble ([Television 01, CC0](https://polyhaven.com/a/Television_01),
  retocada para que se parezca a la de la serie ⚠️ compárala antes) y,
  encima, **la caja del cable interdimensional abierta**, con el
  **cristal de xantenita** brillando dentro (1×08, 0:30). Cables
  sueltos y **el mando** sobre el mueble. En Blender: tele, caja con
  tapa levantada, cristal emisivo, mando.
- **La pantalla**: un **fotograma** del noticiero del cable, «Opposite
  News» (2×08, 12:29 a 12:42), con **Michael Thompson** y sus
  papeles (ref. 225). La regla del dueño: si el marco es una pantalla,
  va un fotograma.
- **Personajes**: **Rick** de pie junto a la tele, **palma arriba
  enseñando el cristal** (pose del 631) y **Morty** sentado en el brazo
  del sofá, mirándolo (pose del 2). Rick es el que trae la señal.
- **Cómo habla**: sin globo. La frase de Rick va en **la pantallita de
  la caja**, en VT323: **«TV infinita de universos infinitos»**
  (traducción mía de «infinite TV from infinite universes», 1×08,
  1:00).
- **Dónde va cada texto**:
  - Cartela del programa, arriba en la pantalla: **Noticias de series**
    (Creepster, o Get Schwifty porque no lleva tildes).
  - Rótulo de abajo, primera línea: **Series y cine** (Anton).
  - Debajo, como los eslóganes apilados de Real Fake Doors (1×08,
    11:18), tres líneas o tres pestañas: **Estrenos**,
    **Temporadas**, **Doblajes**.
  - Un **pósit** pegado en el marco de la tele, con letra de Morty:
    **¿Quieres opinar? Abre un hilo**.
- **Para que no quede plano**: en primer plano, **el respaldo del sofá
  azul** y la **coleta naranja de Summer**, desenfocados; la **luz fría
  de la pantalla** (`#A0BDCF`) pinta la cara de Rick y Morty; el cristal
  da un **brillo verde desde abajo**; la tele proyecta sombra real sobre
  el mueble.

### Concepto B — «¡Bum! Gran revelación» (Pepinillo Rick en el garaje)

- **Objeto y sitio**: **el banco de trabajo del garaje** (3×03,
  0:20: «On my work bench, Morty»). Encima, **Pepinillo Rick**
  tumbado, y a su lado **una tele pequeña de tubo** con la caja del
  cable. Los **tres cajones** del banco llevan **etiquetas de cinta de
  carrocero escritas a mano**. En Blender: banco, cajones, cinta arrugada
  (la tinta sigue las arrugas), tornillo de banco, herramientas.
- **Personajes**: **Pepinillo Rick**, el secundario más famoso (Emmy
  2018, 3.º en Ranker). Pose: tumbado, mirando a cámara (3×03, 0:34)
  ⚠️ compruébala. **Morty** entero a un lado, **inclinado sobre el
  banco** y con cara de «¿y?» (pose del 2). Ojo con la regla 7: nada de
  una mano sin brazo entrando en el cuadro.
- **Cómo habla**: su frase va **en la pantalla de la tele pequeña**,
  como un rótulo de última hora, en Bangers: **«¡Bum! Gran revelación»**
  (traducción mía de «Boom! Big reveal», 3×03, 0:34). Si se prefiere
  la frase **verificada en latino**: **«¡Soy un pepinillo!»**.
- **Dónde va cada texto**:
  - Pantalla de la tele pequeña, arriba: **Noticias de series**.
  - Tira de cinta en el borde del banco: **Series y cine**.
  - Etiquetas de los tres cajones: **Estrenos**, **Temporadas**,
    **Doblajes**.
  - Papel sujeto con cinta en el tablero de herramientas de la pared:
    **¿Quieres opinar? Abre un hilo**.
- **Para que no quede plano**: **una llave inglesa y el tornillo de
  banco desenfocados delante**; luz de **tubo fluorescente** fría desde
  arriba y el **verde de un portal** entrando por un lado; el pepinillo
  hace sombra sobre la madera.

### Concepto C — «La caja Meeseeks» (una petición, una noticia)

- **Objeto y sitio**: **la caja Meeseeks** sobre **la mesa de la cocina
  de los Smith**. Es una caja con **un botón** arriba (1×05, 2:31:
  «This is a Meeseeks Box… You press this») ✅. En Blender: caja con
  botón, **funda de cartón impresa** como la de un juguete, mesa, platos
  del desayuno. Referencia 3D: [Meeseeks Box de pythagean](https://sketchfab.com/3d-models/none-88525f59bb974271a0933fc7608672c2),
  **CC BY 4.0** ✅ (segunda pasada, API de Sketchfab; la de MagunDongle
  no tiene licencia: sólo para mirar la forma). Pose del Meeseeks: hoja
  191 (recortado) y el [clip del 1×05, 0:16](https://www.dailymotion.com/video/x7xeqwl?t=16).
- **Personajes**: **tres Sr. Meeseeks** recién salidos de la caja (pose
  del 242, sonriendo), cada uno **sujetando un objeto real**: un
  **periódico «NEWS»** (como el de Jon, ref. 184), una **claqueta** y un
  **micrófono**. Al fondo, **Summer** de brazos cruzados junto a la
  nevera (pose del 3), la que va a opinar.
- **Cómo habla**: el Meeseeks habla desde **la funda de la caja**, como
  el eslogan de un juguete: **«¡Soy el Señor Meeseeks! ¡Mírenme!»**
  («Señor Meeseeks» ✅ en latino; «¡Mírenme!» ⚠️ compruébalo en el 1×05,
  2:35).
- **Dónde va cada texto**:
  - Tapa de la caja, grande: **Noticias de series**.
  - Frente de la funda: **Series y cine**.
  - Lo que sostiene cada Meeseeks: periódico **Estrenos**, claqueta
    **Temporadas**, banderita del micrófono **Doblajes**.
  - Etiqueta junto al botón: **¿Quieres opinar? Abre un hilo**. La idea:
    igual que cada Meeseeks cumple **una** petición (1×05, 2:43),
    **cada noticia tiene su hilo**.
- **Para que no quede plano**: un **plato con el desayuno** y un vaso de
  zumo desenfocados delante (como en el 339); luz de mañana por la
  ventana; el Meeseeks del centro **tapa un poco la caja**; sombras
  reales de los tres sobre la mesa.
- **Variante**: la **rueda de prensa del hospital** (2×08, 17:28, «I
  have news»), con el **periodista que levanta la mano** (ref. 460)
  como símbolo de «abre un hilo».

### ¿Cuál primero?

1. **A**: es el objeto del plan y la escena más exacta (la serie tiene
   **noticiero, última hora y familia comentando**).
2. **B**: el más reconocible por cualquiera (Pepinillo Rick).
3. **C**: el más original; bueno si el dueño quiere un secundario.

### Lámina 2 (si hace falta)

**El mando de la tele** en primer plano, sobre el cojín del sofá, con
**un botón por paso** para abrir un hilo en Discord. Los pasos y sus
nombres exactos en la interfaz en español **los tiene que confirmar el
dueño**: no los invento.

---

## 20 · Lo que no pude verificar

Actualizado en la segunda pasada (25-sep-2026). Tachado = resuelto.

**Sigue sin verificar** ⚠️:

- **Fotogramas en 1080p del 1×08 y del 2×08**: YouTube pide iniciar
  sesión y no encontré esos episodios en Dailymotion ni en Internet
  Archive. Hay 1920×1080 de otros capítulos en las hojas (§3A).
- **La caja del cable y la tele de los Smith**: sin ver de cerca.
- **Frases en latino** sin fuente textual: «Ven a ver la televisión»
  (sólo un vídeo de Facebook), «¡Mírenme!», «Muéstrenme lo que tienen»,
  «¡Mira, Morty, me acabo de convertir en un pepinillo!», «Voltea el
  pepinillo, Morty». No hay subtítulos latinos con tiempos.
- **Voces latinas con una sola fuente**: Mr. Poopybutthole (tres
  actores), Hombre Pájaro, el estudio exacto de cada temporada (Dvinxi,
  AGP, IDS) y quién lee los insertos desde la T4.
- **Qué dicen los rótulos** de los programas del cable (su letra, color).
- **Encuesta oficial de popularidad**: no la encontré (en inglés y en
  español).
- **Altura, cumpleaños y comida favorita** del reparto principal: no hay
  ficha oficial (§18C).
- **Minuto de las escenas tristes** de 5×03 y 7×04 (§18D) y el episodio
  de la T8 que citan los fans.
- **Vistas** de dos fandubs (§18E); **pantalla de combate** de Pocket
  Mortys; **licencias de BlendSwap** una por una; el **pressroom de WBD**
  y el **Behance de Sangho Bang** (403); la **petaca de Rick** y el traje
  de luchador de la T9 (sin imagen grande para medir).

**Resuelto en la segunda pasada** ✅:

- ~~Licencias de Sketchfab~~: leídas en su API (§4).
- ~~El vídeo «Style Guide»~~: visto entero en Internet Archive (§18A).
- ~~El verde de los portales~~: medido en dos vídeos (§5).
- ~~La tipografía de los cómics~~: el rotulista es Crank!, que rotula a
  mano; alternativa libre comprobada (§6).
- ~~El director del doblaje~~: Ángel Balam, T1-T2 (§10).
- ~~Beth y el Sr. Meeseeks con una fuente~~: ya con dos (§10).
- ~~El reparto del anime salvo Rick y Morty~~: ANMTV + Doblaje Wiki (§10).
- ~~Cajas de diálogo de los juegos~~: miradas; no hay cajas, hay objetos
  con texto (§13).
- ~~Título latino del 1×08~~: «Televisión interdimensional» (§2).

---

## Cumplimiento del encargo

_(pendiente: se rellena en esta segunda pasada)_

---

## 21 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)

- **403** (curl o WebFetch): rickandmorty.fandom.com, doblaje.fandom.com,
  en.wikipedia.org, youtube.com, arctic-shift, anmtvla.com,
  latam.bubbleblabber.com, videogaming3d.com, epicstream.com,
  tvwriting.co.uk (el guion del animatic del 1×08), rickandmortyapi.com,
  api.sketchfab.com, adultswim.com, gameuidatabase.com,
  spriters-resource.com.
- **Funciona**: WebSearch; GitHub por `git clone` y por
  `raw.githubusercontent.com`; la búsqueda de código de GitHub.
- Por eso **no se pudo correr** `herramientas/investigar_serie.py` y
  **no hay `hojas/`**.

### Búsquedas web (50)

| # | Idioma | Búsqueda |
|---|---|---|
| 1 | ES | Rick y Morty doblaje latino reparto voz de Rick Sanchez Morty Smith actor estudio director |
| 2 | EN | Interdimensional Cable episode Rixty Minutes improvised Real Fake Doors Ants in My Eyes Johnson Two Brothers list |
| 3 | ES | «Juan Guzmán» Rick «Eder La Barrera» Morty doblaje venezolano Summer Beth Jerry voces |
| 4 | ES | Rick y Morty doblaje latino frases «Soy Pepinillo Rick» «Señor Meeseeks» «mírenme» |
| 5 | ES | Rick y Morty doblaje latino Summer «Lileana Chacón» Beth «Carmen Lugo» Jerry voz IDS Venezuela |
| 6 | ES | «Pepinillo Rick» doblaje latino Rick y Morty |
| 7 | EN | Rick and Morty season 9 premiere date 2026 Adult Swim |
| 8 | EN | Rick and Morty season 9 «no AI slop» announcement trailer Adult Swim |
| 9 | ES | «Lileana Chacón» Summer Smith Rick y Morty voz |
| 10 | ES | «Rick y Morty» doblaje «Carmen Lugo» Beth «Héctor Indriago» Jerry Meeseeks voz latino |
| 11 | ES | Rick y Morty cambio de voz doblaje latino temporadas Rick Sánchez voz anterior Juan Guzmán |
| 12 | EN | Rick and Morty most popular character poll results fans favorite Meeseeks Poopybutthole Pickle Rick Evil Morty |
| 13 | EN | YouGov Rick and Morty popularity fame characters |
| 14 | EN | Rick and Morty logo font name free «Get Schwifty» font dafont license |
| 15 | ES | «Rick y Morty» temporada 9 estreno Latinoamérica HBO Max doblaje latino 2026 |
| 16 | EN | Rick and Morty «crystallized xanthanite» cable box Smith living room TV |
| 17 | EN | Rick and Morty official style guide model sheet character turnaround Adult Swim |
| 18 | EN | Rick and Morty background art director interview color palette Bardel |
| 19 | EN | Rick and Morty style guide video Jeffrey Thompson do's and don'ts |
| 20 | EN | how to draw Rick and Morty official tips eyes pupils art director |
| 21 | ES | «Nadie existe a propósito» «Ven a ver» televisión Morty Summer |
| 22 | ES | «Cable interdimensional» «Puertas falsas» «Hormigas en los ojos» Johnson doblaje latino |
| 23 | ES | «Soy el Señor Meeseeks» «mírenme» OR «mírame» latino |
| 24 | EN | Pocket Mortys dialogue box UI battle screen |
| 25 | EN | Rick and Morty video games list Virtual Rick-ality Pocket Mortys Clone Rumble MultiVersus Fortnite |
| 26 | EN | Rick and Morty theme song Ryan Elder Evil Morty theme «For the Damaged Coda» |
| 27 | EN | sketchfab Rick and Morty Meeseeks box portal gun plumbus CC (sólo sketchfab.com) |
| 28 | EN | polyhaven television model CC0 CRT TV (polyhaven.com, sketchfab.com) |
| 29 | EN | Smith residence living room couch television wiki |
| 30 | EN | Rick and Morty biggest memes Pickle Rick Szechuan sauce Get Schwifty Plumbus |
| 31 | ES | «Muéstrenme lo que tienen» OR «Muéstrame lo que tienes» OR «Ponte schwifty» latino |
| 32 | EN | Summer Smith character analysis |
| 33 | EN/ES | Rick and Morty: The Anime Takashi Sano doblaje latino Gerardo Reyero Miguel Ángel Leal |
| 34 | JA | リック・アンド・モーティ アニメ 佐野隆史 監督 インタビュー 絵柄 キャラクターデザイン |
| 35 | EN | Rick and Morty season 9 key art poster first look images |
| 36 | EN | «TV Head Morty» Rick and Morty season 9 production art |
| 37 | EN | Ian Cardoni Harry Belden new voices season 7 |
| 38 | EN | Rick and Morty comic Oni Press Zac Gorman CJ Cannon letterer Crank! |
| 39 | ES | «Soy Pepinillo Rick» OR «me convertí en pepinillo» latino HBO Max |
| 40 | EN | Interdimensional Cable how it was made improvised + Emmy «Pickle Rick» |
| 41 | EN | artstation Rick and Morty 3D living room garage (sólo artstation.com) |
| 42 | EN | Rick and Morty 4K wallpaper 3840x2160 |
| 43 | ZH | 瑞克和莫蒂 跨维度有线电视 名场面 最受欢迎角色 米西克斯先生 腌黄瓜瑞克 |
| 44 | EN | «The Art of Rick and Morty» Dark Horse artbook volume 2 |
| 45 | EN | Adult Swim bumps font white text black background |
| 46 | EN | Rick and Morty color palette hex codes portal green |
| 47 | EN | Adult Swim official YouTube clip Real Fake Doors / Ants in My Eyes Johnson (sólo youtube.com) |
| 48 | ES | «Rick y Morty» doblaje IDS dirección director de doblaje Venezuela |
| 49 | EN | Smith family television set flat screen TV stand cable box design |
| 50 | ES | «Sr. Meeseeks» voz doblaje latino actor venezolano |

No hice búsquedas en coreano: la serie es estadounidense y no hay
producción coreana. En japonés sólo una, por el anime de 2024.

### GitHub (sin cupo)

- [alexlyzhov/sphere-neural](https://github.com/alexlyzhov/sphere-neural/tree/master/10_nlp/sub):
  subtítulos en inglés de la T1 (Blu-ray y HDTV) y del 2×01 al 2×06.
- [lucas-dclrcq/ifi-atelier-spark](https://github.com/lucas-dclrcq/ifi-atelier-spark/tree/master/src/main/resources/data/rickandmorty):
  subtítulos de Addic7ed del 1×01 al 3×06 y el 4×01. **Fuente de todos
  los minutos.**
- [afuh/rick-and-morty-api](https://github.com/afuh/rick-and-morty-api):
  826 fotogramas de 300×300 y los datos de prueba (el sitio
  «Interdimensional Cable» con sus 61 personajes).
- [rieger-jared/rick-and-morty-api](https://github.com/rieger-jared/rick-and-morty-api):
  el JSON con el nombre de cada número.
- [nanxstats/ggsci](https://github.com/nanxstats/ggsci): la paleta
  «schwifty».
- [fmiguezo/SkillFactory-SegundoProyecto](https://github.com/fmiguezo/SkillFactory-SegundoProyecto):
  el archivo de Get Schwifty (el de
  [suheylaikbalicme/rick-morty-characters](https://github.com/suheylaikbalicme/rick-morty-characters)
  estaba vacío).
- [google/fonts](https://github.com/google/fonts): las letras libres.
- [ClumsyPandal1/PocketMortysOfflinePatch](https://github.com/ClumsyPandal1/PocketMortysOfflinePatch):
  el cierre de Pocket Mortys.

### Fuentes consultadas por tipo

- **Oficiales**: Adult Swim (vídeo Style Guide, clips de YouTube, clip
  de Adult Swim LA), pressroom de WBD, cuenta de Rick and Morty en X,
  HBO Max LA (TikTok y YouTube), Dark Horse (artbook).
- **Staff**: James McDermott (It's Nice That), Jeffrey Thompson (Style
  Guide), Bardel (Q&A con el director Nathan Litz, sin abrir), Ryan Elder.
- **Prensa**: Variety, Deadline, TheWrap, Space.com, Bleeding Cool, AWN,
  SYFY, JoBlo, The Hollywood Reporter, Screen Rant, Collider, CBR,
  AV Club, Know Your Meme, Daily Dot, Newsweek, Paste.
- **Latinoamérica**: La República (Perú), El Comercio (Perú), Excélsior
  (México), TV Azteca, El Heraldo (Colombia), La Estrella de Panamá,
  Vice en español.
- **Wikis**: Doblaje Wiki, Doblaje Latino Wiki, Fandoblaje, wiki en
  inglés y en español de la serie, Wikipedia (todas por resumen de
  búsqueda).
- **Otros idiomas**: japonés (Wikipedia JA, denfaminicogamer, note), chino
  (Zhihu, Qidian, Moegirl).
- **Arte y 3D**: ArtStation (8 obras), Sketchfab (8 modelos), Poly
  Haven, Steam Workshop, Behance.
- **Código**: los 8 repositorios de GitHub de arriba.

### Lo que NO encontré

- Ningún **fotograma en alta** ni captura de la **caja del cable**.
- El **guion del animatic** de «Rixty Minutes» existe
  ([tvwriting.co.uk](https://tvwriting.co.uk/tv_scripts/Collections/Animation/Rick_and_Morty/Rick_and_Morty_1x08_-_Rixty_Minutes.pdf),
  de Tom Kauffman), pero daba 403.
- **Subtítulos latinos con tiempos**: ninguno en GitHub.
- Subtítulos de **3×07 en adelante** (salvo el 4×01): no los hay en
  esos repositorios.
- La **encuesta oficial** de personajes.
- El **director del doblaje latino**.
- **Cajas de diálogo** de Pocket Mortys y Virtual Rick-ality.
- Comentarios de Blu-ray o entrevistas sobre **cómo se diseñaron los
  rótulos** del cable.

### Segunda pasada (25-sep-2026, red abierta)

Cuatro investigadores (imagen, vídeo, voz, texto) y un redactor. Sus
notas completas, con cada consulta, están en `partes/imagen.md`,
`partes/video.md`, `partes/voz.md` y `partes/texto.md`.

**Red directa (sin gastar buscador)**:

- **API de Fandom**, wiki de la serie (EN): wikitexto de Rick, Morty,
  Summer, Sr. Meeseeks, Portal Gun, The Citadel, Council of Ricks,
  Central Finite Curve, Mr. Poopybutthole, The Vindicators, Jerryboree,
  Blips and Chitz, Death Crystal, Cronenberg World, Birdperson y el
  transcript de «Rixty Minutes»; tamaños con `imageinfo`.
- **API de Doblaje Wiki** (ES): «Rick y Morty», «Rick y Morty/1.ª
  temporada», «2.ª temporada», «Rick y Morty: El anime», fichas de Carmen
  Lugo y Ángel Balam. **Fandoblaje Wiki**: Ángel Lugo, Rebeca Aponte.
- **`investigar_serie.py`**: 220 imágenes de la wiki en 5 hojas; las 5
  miradas con Read, 3 subidas (§3A).
- **API de Sketchfab**: licencias de 10 modelos, repasadas otra vez por
  el redactor (§4).
- **Arctic Shift** (Reddit): hilos «identify» (833 votos) y «saddest»
  (403, 625 y 2004 votos) y sus comentarios.
- **Dailymotion** (API de búsqueda, EN y ES) e **Internet Archive**: 8
  vídeos mirados con `fotogramas.py` (§2.4, §12).
- **`yt-dlp --skip-download`**: metadatos de 5 fandubs (3 respondieron).
- **Fontsource + fontTools**: Comic Relief con tildes, ñ, ¿ y ¡.
- **ambientCG** (API): texturas CC0 de papel y tela (§18B).
- `curl` a Wallhaven (3 fondos medidos), a ANMTV (artículo del anime) y
  a la ficha del «Style Guide» en adultswim.com.
- `grep -il noticias-series encargos/*.md`: ningún choque de canal.

**Buscador web** (unas 45 búsquedas entre los cuatro; EN salvo donde se
dice): colaboraciones (Fortnite, McDonald's, MultiVersus, Funko,
McFarlane, gag de *Los Simpson*, corto de Studio DEEN, Rickmobile en
Dragon Con), técnica (Toon Boom, Bardel, Jeffrey Thompson, James
McDermott, *cel shading* en Blender), obras parecidas (TVLine, *Solar
Opposites*, «Doc and Mharti»), lore (Den of Geek), premios y audiencias
(Emmy, Rotten Tomatoes, HBO Max), escenas tristes (Planetina, «That's
Amorte»), fandubs y memes (**ES**), doblaje de la T9 y Arlet Matute
(**ES**), Mr. Poopybutthole en latino (**ES**), pop-up bar temático
(**ES**). No se buscó en japonés ni en chino en esta pasada: la serie es
estadounidense y lo japonés (el anime, el corto de Studio DEEN) salió en
inglés.

**Lo que dio error**: YouTube («Sign in to confirm you're not a bot»,
todos los días); `press.wbd.com` y Behance (403, sin copia en Wayback);
yt-dlp con el espejo de Internet Archive (500: se bajó el mp4 directo);
`api.github.com` sin autenticar.

**Lo que NO encontré en la segunda pasada**: fotogramas en alta del 1×08
y del 2×08; la transformación completa de Pepinillo Rick en vídeo (la
promo sólo enseña el pepino); «Ants in My Eyes Johnson» y «Real Fake
Doors» fuera de YouTube; la pantalla de combate de Pocket Mortys; una
entrevista sobre encuadres por emoción; ficha oficial de gustos del
reparto principal; segunda fuente para Mr. Poopybutthole en latino.
