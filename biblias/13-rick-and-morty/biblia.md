---
tags: [biblia, serie, laminas]
serie: "Rick and Morty"
canal: "#noticias-series"
fecha: 2026-09-24
---

# Biblia · Rick y Morty — para #noticias-series

> [!important] Cómo se hizo, y sus límites
> - La red de esta sesión estaba cerrada. Fandom (el wiki de la serie y
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
«Televisión Interdimensional» ⚠️
([Wiki de Rick & Morty](https://wiki-de-rick-morty.fandom.com/es/wiki/Televisi%C3%B3n_Interdimensional)).

| Minuto | Qué pasa y qué se dice (inglés) | Para qué sirve |
|---|---|---|
| 0:04 | La familia ve un reality en la tele del salón. Alguien (Rick, creo ⚠️; el subtítulo no dice quién): «none of it mattered and the entire show was stupid» (0:19) | Abre con **la familia criticando la tele**: el debate |
| 0:21 | Jerry ⚠️: «Okay, I've got an idea, Rick. You show us your concept of good TV, and we'll crap all over that» | El espíritu del canal: **enseña y se comenta** |
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
| **Vídeo oficial «Rick and Morty Style Guide»**: el director de arte **Jeffrey Thompson** explica lo que se hace y lo que no al dibujarlos (3 de octubre de 2018) | [adultswim.com](https://www.adultswim.com/videos/rick-and-morty/rick-and-morty-style-guide) · [YouTube 8c4hAsobciA](https://www.youtube.com/watch?v=8c4hAsobciA) | ✅ existe (dos fuentes). **Verlo antes de dibujar**: no pude abrirlo |
| Guía de estilo para Adult Swim de **Sangho Bang** | [Behance](https://www.behance.net/gallery/90220333/Rick-and-Morty-Style-Guide) | ⚠️ |
| **The Art of Rick and Morty, vol. 2** (Dark Horse): temporadas 3 y 4, 216 páginas, con arte de Justin Roiland, **James McDermott**, **Jason Boesch**, Carlos Ortega y Andrew DeLange | [Dark Horse](https://www.darkhorse.com/Books/3006-618/The-Art-of-Rick-and-Morty-Volume-2-HC) · [Barnes & Noble](https://www.barnesandnoble.com/w/the-art-of-rick-and-morty-volume-2-jeremy-gilfor/1137831704) | ✅. Hay un vol. 1 (temporadas 1 y 2) ⚠️ de memoria |
| Recopilación del arte | [Character Design References](https://characterdesignreferences.com/art-of-animation-9/art-of-rick-and-morty) | ⚠️ |
| Los cuadernos del director de arte **James McDermott** | [It's Nice That](https://www.itsnicethat.com/features/inside-rick-and-morty-art-director-james-mcdermotts-sketchbooks-250717) | Dice que el dibujo mezcla **lo ingenuo, lo familiar y lo amable con lo macabro**, y que hasta lo más oscuro tiene algo de **comedia o rareza** ✅ (resumen de búsqueda). Las escenas pasan por el **equipo de color** y se animan en **Bardel** (Vancouver) |
| Sprites de **Pocket Mortys** | [The Spriters Resource](https://www.spriters-resource.com/mobile/pocketmortys/) | ⚠️ no abrí |

### 3.3 Lo que falta ⚠️

- **Fotogramas en 1080p** de 1×08 y 2×08: no pude bajar ninguno. Los
  minutos de §2 dicen **dónde** parar el vídeo. Hay que sacarlos en el PC.
- **La caja del cable**: no la he visto. Sé por el subtítulo que Rick la
  abre y le mete el cristal (0:30) y por la wiki que la vuelve a
  **conectar a la tele** ⚠️. Su forma exacta, sin comprobar.

---

## 3A · Las hojas de contacto (qué número sirve)

_(pendiente: se rellena en esta segunda pasada)_

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D para la lámina

| Modelo | Autor | Licencia | Para qué |
|---|---|---|---|
| [Television 01](https://polyhaven.com/a/Television_01) | Poly Haven | **CC0** ✅ (sin crédito obligatorio). Trae madera, metal, vidrio y desgaste | **La tele**. Es una tele antigua de mueble de madera ⚠️: compárala con la del salón de los Smith antes de usarla |
| [CRT TV](https://sketchfab.com/3d-models/crt-tv-9ba4baa106e64319a0b540cf0af5aa9e) | Timothy Ahene | «Download Free» ⚠️: mira la licencia en la página | Tele de tubo |
| [Small CRT TV](https://sketchfab.com/3d-models/small-crt-tv-890c6ce1f6124c02b0cad54db0fdcb52) | rhcreations | ⚠️ | Otra opción |
| [Portal gun (Rick and Morty)](https://sketchfab.com/3d-models/portal-gun-rick-and-morty-ac3226c6b9e64142af2065409f0162ee) | kreems | «Download Free» ⚠️ | La pistola de portales, en primer plano |
| [Portal Gun - Rick and Morty](https://sketchfab.com/3d-models/portal-gun-rick-and-morty-149daa9d26354c4999394773cdf9867f) | AbhijeetUnreal | «Download Free» ⚠️ | Otra pistola |
| [Rick and Morty Meeseeks Box](https://sketchfab.com/3d-models/rick-and-morty-meeseeks-box-c1480c8478c148b19ab4076bd8077be1) | MagunDongle | ⚠️ el título no dice que se pueda bajar | **La caja Meeseeks** (concepto C) |
| [Plumbus](https://sketchfab.com/models/ea0ca7e5d42744bb95dd32f6b5ff7f27/embed) | mskullkid | ⚠️ | Objeto de fondo |
| [Plumbus (llavero, imprimible)](https://sketchfab.com/3d-models/plumbus-keychain-rick-and-morty-3d-printable-424de72d353049e4b6dae7ffffa5fa95) | Nima (@h3ydari96) | «Download Free» ⚠️ | Objeto de fondo |

Colecciones para buscar más:
[OblivionRazer](https://sketchfab.com/OblivionRazer/collections/rick-and-morty-a061400cdc2a454bad90869309c8b89e) ·
[double-helix](https://sketchfab.com/double-helix/collections/rick-and-morty-dcc0e006b3994f3d9a36126b945f1cf7).

> [!note] Crédito exacto
> Para lo que sea CC BY, el crédito va así: «<nombre del modelo>» de
> <autor> (Sketchfab), CC BY 4.0. **Compruébalo en la página**: la API de
> Sketchfab estaba bloqueada y no pude leer la licencia de ninguno.

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
| **Sala de espera del hospital** (2×08) | «Go in the waiting room, dad» (0:46) ✅. Rick conecta su aparato a la tele de la sala | Luz de hospital, fría ⚠️ |
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
| Pantalón de Rick | — | `#917C5D` («RickBrown») | ⚠️ una fuente |
| Camiseta de Morty | `#FBF976` | `#FAFD7C` («MortyYellow») | ✅ |
| Pelo de Morty | `#8F5C23` | `#82491E` («MortyBrown») | ✅ |
| Pantalón de Morty | — | `#24325F` («MortyBlue») | ⚠️ una fuente |
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

El **verde de portal** no lo pude medir: no tengo un fotograma con un
portal. Las paletas de fans lo ponen en `#97CE4C` o `#88E23B` ⚠️
([color-hex](https://www.color-hex.com/color-palette/9134),
[ColorsWall](https://colorswall.com/palette/243091)).

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
| Texto de globo (si se usa el cómic) | **Sniglet** o **Grandstander** | OFL ✅ | **Sí** ✅ | Redondas y amables. La letra real del cómic (rotulista **Crank!**) no la identifiqué ⚠️ |

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
- **Miedo**: la soledad y perder a los suyos ⚠️ (lectura de fans).
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
- **Voz latina**: **Ángel Lugo** ⚠️ (una fuente, ver §10).

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
| **Beth Smith** | La madre, cirujana de caballos | Voz latina: **Rebeca Aponte** y, desde la T7, **Carmen Lugo** ⚠️ (una fuente) |
| **Mr. Poopybutthole** | Favorito de fans; sale en las escenas finales | «Ooh-wee!» ⚠️ |
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
Gerardo Reyero** y **Morty Miguel Ángel Leal**, mexicanos, porque a
Warner no le convencieron las pruebas venezolanas ✅ (Doblaje Wiki,
ANMTV, TVLaint, FUNiAnime). Summer **Constanza de la Rosa**, Beth
**Elena Díaz Toledo**, Jerry **Héctor Indriago** ⚠️.

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

No pude abrir YouTube (403): **no puedo dar el minuto dentro de estos
vídeos**. Los minutos útiles están en §2, sobre el episodio.

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

- **Pocket Mortys** (2016): parodia de Pokémon. **Cerró sus servidores**;
  los fans lo mantienen vivo con un parche de agosto de 2026 ✅. Buena noticia de
  ejemplo para el canal.
- **Virtual Rick-ality** (2017, Owlchemy Labs): en el **garaje de Rick**.
- **Clone Rumble** (cerrado), **MultiVersus**, **Fortnite** (apariciones).
- No hay capturas verificadas de sus cajas de diálogo ⚠️.

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

---

## 16 · Vestuario

| Personaje | Ropa icónica (la que todos reconocen) | Colores | Variantes |
|---|---|---|---|
| **Rick** | **Bata blanca** abierta, camisa **celeste verdoso**, pantalón marrón ✅ (visto y ggsci) | bata `#E8E8E8`, camisa `#97D7D7`, pantalón `#917C5D` ⚠️, pelo `#AAD3E9` | Pepinillo Rick, Tiny Rick, **Rick luchador** (T9) ✅ |
| **Morty** | **Camiseta amarilla** y pantalón azul ✅ | `#FAFD7C`, pantalón `#24325F` ⚠️, pelo `#82491E` | **Morty cabeza de tele** (T9) ✅, Evil Morty con parche ✅ |
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
| «Rick & Morty: 4K Portal Panic» | **3840×2160** ✅ (lo dice la página) | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1099810) (autor y licencia sin comprobar ⚠️) |
| Fondos de portales, HD, 4K y 8K | varios | [Wallpapers.com](https://wallpapers.com/rick-and-morty-portal) ⚠️ |
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

_(pendiente: se rellena en esta segunda pasada)_

---

## 18B · Texturas 2D (punto 19)

_(pendiente: se rellena en esta segunda pasada)_

---

## 18C · Gustos y detalles de cada personaje (punto 20)

_(pendiente: se rellena en esta segunda pasada)_

---

## 18D · Por qué la gente la ama (punto 21)

_(pendiente: se rellena en esta segunda pasada)_

---

## 18E · Fan dubs y comunidad hispana (punto 22)

_(pendiente: se rellena en esta segunda pasada)_

---

## 18F · Colaboraciones, figuras y cosplay (punto 23)

_(pendiente: se rellena en esta segunda pasada)_

---

## 18G · Obras parecidas y temas relacionados (punto 24)

_(pendiente: se rellena en esta segunda pasada)_

---

## 18H · El mundo, la historia y sus símbolos (punto 25)

_(pendiente: se rellena en esta segunda pasada)_

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
  del desayuno. Referencia 3D: [Meeseeks Box de MagunDongle](https://sketchfab.com/3d-models/rick-and-morty-meeseeks-box-c1480c8478c148b19ab4076bd8077be1)
  ⚠️ (sólo para mirar la forma).
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

- **Fotogramas en alta**: ninguno. Sólo los de 300×300 de la API.
- **Cómo son la caja del cable y la tele de los Smith**: sin ver. Sé que
  hay tele sobre un mueble (wiki, una fuente) y que Rick abre la caja y
  mete el cristal (subtítulo).
- **Frases en latino** sin fuente: «Ven a ver la televisión», «¡Mírenme!»,
  «Muéstrenme lo que tienen», «¡Mira, Morty, me acabo de convertir en un
  pepinillo!», «Voltea el pepinillo, Morty», y el título latino del 1×08.
- **Voces latinas** con una sola fuente: Beth (Rebeca Aponte y Carmen
  Lugo), Sr. Meeseeks (Ángel Lugo), el reparto del anime salvo Rick y
  Morty, y quién dirige el doblaje.
- **Licencias de Sketchfab**: la API estaba bloqueada; ninguna leída.
- **El vídeo «Style Guide»**: existe, pero no pude verlo. Sus reglas de
  dibujo, sin saber.
- **Qué dicen los rótulos** de los programas del cable (su letra, color):
  sin ver.
- **La tipografía de los cómics** de Oni Press (Crank!): sin identificar.
- **Encuesta oficial de popularidad**: no existe o no la encontré.
- **El verde de los portales**: sin medir.

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
