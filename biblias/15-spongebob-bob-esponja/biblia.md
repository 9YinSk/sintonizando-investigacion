---
tags: [biblia, serie, laminas]
serie: "SpongeBob SquarePants (Bob Esponja)"
canal: "#ofertas-y-gratis"
fecha: 2026-09-24
---

# Biblia · Bob Esponja — para #ofertas-y-gratis

> [!important] Cómo se hizo, y sus límites
> - **Segunda pasada (26-sep-2026), con la red abierta**: la hizo un equipo
>   de 4 investigadores (imagen, vídeo, voz, texto) y un redactor. Ya se
>   pudo usar la API de Fandom, Doblaje Wiki, Sketchfab, Wallhaven,
>   ambientCG, Dailymotion, Arctic Shift (Reddit), Wikipedia y Wayback
>   Machine. Hay **3 hojas de contacto** en `hojas/` (§3.6). Se miraron **7
>   vídeos enteros** (299 fotogramas) en Dailymotion, porque **YouTube dio
>   429** al primer intento. Lo nuevo está en «Segunda pasada · qué cambió».
> - **Primera pasada (24-sep-2026)**: la red estaba cerrada. **Fandom,
>   Doblaje Wiki, YouTube, Sketchfab, Steam, Game UI Database** y las webs de
>   letras daban 403. No se pudo correr `herramientas/investigar_serie.py`.
> - Hice **48 búsquedas web** en español e inglés (lista en §30).
> - Lo más útil salió de **GitHub**: los **subtítulos con tiempos** de 9
>   temporadas ([1440kHz/sbsp-chs-eng-sub](https://github.com/1440kHz/sbsp-chs-eng-sub)).
>   Con ellos doy el **minuto de cada escena** de Don Cangrejo y la caja.
>   También de GitHub: la letra **Some Time Later** (libre, OFL) y 18 fondos
>   de tarjetas de tiempo, texturas del menú, de la caja y de la fachada, y
>   portadas oficiales de los juegos. Todo lo **vi y medí yo** (colores
>   en hex, ±5 por canal).
> - Comprobé con fontTools si cada letra trae **á é í ó ú ñ ¿ ¡**.
> - **Cómo leo los minutos**: «03x07 00:13:15» = archivo de la temporada 3,
>   n.º 7 (media hora con dos episodios), minuto 13:15 desde el principio.
>   Puede moverse uno o dos minutos según la copia.
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su minuto,
>   o lo vi y medí yo. ⚠️ **dudoso**: una sola fuente, o de memoria.
> - **Dos formatos de minuto**: «03x07 00:13:15» es del archivo de
>   subtítulos de GitHub (primera pasada); «3:55» con enlace `?t=` es del
>   vídeo de Dailymotion mirado en la segunda pasada, contado desde el
>   principio de **ese** vídeo (un clip, no el episodio entero).

## Segunda pasada · qué cambió

(pendiente)

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección 📡 NOTICIAS):

> **ıı・🏷️・ofertas-y-gratis** (texto) · 1 fijados · 0 de personas en los
> últimos 15 — _Juegos gratis y rebajas de Steam, Epic y GOG, con el precio
> en soles. Los gratis caducan: reclámalos._

Y de su vecino, **ıı・🎮・noticias-gaming**: _«Videojuegos: salidas, parches
y presentaciones. Las ofertas van en ofertas-y-gratis.»_ Así que la lámina
tiene que dejar claro qué NO va aquí: noticias sin precio.

### Lo que hace especial a este canal

- Es un canal de **dinero**: precios, rebajas y cosas gratis. En Bob
  Esponja el dinero tiene dueño: **Don Cangrejo**. Ama el dinero más que
  nada, y **le cuesta decir «gratis»** (ver §2).
- «**Con el precio en soles**»: el público es de Perú y de toda
  Latinoamérica. La lámina tiene que enseñar un precio escrito como se
  escribe en Perú: **S/ 12.90** (símbolo «S/» y punto decimal) ⚠️. Antes de
  rotular, copiar el formato exacto de una captura de Steam Perú (ver §28).
- «**Los gratis caducan: reclámalos**»: es un aviso con prisa. En la serie
  la prisa la pone el **Narrador Francés** con sus tarjetas de tiempo
  («Unos momentos después…», «Dos horas después…»).

### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Ofertas y gratis** | nombre del canal |
| 2 | **Juegos gratis y rebajas** | qué se publica |
| 3 | **De Steam, Epic y GOG** | de dónde |
| 4 | **Con el precio en soles** | cómo se publica |
| 5 | **Los gratis caducan** | aviso |
| 6 | **Reclámalos** | acción |
| 7 | **Las noticias van en noticias-gaming** | qué no va aquí (sale del inventario) |
| 8 | Frase del personaje, en su voz (ver §7 y §27) | gancho |

### Lámina 2 (si hace falta): cómo se publica una oferta

El inventario no trae plantilla de publicación. Si el dueño la quiere,
propongo una **lámina 2 con un «ticket» de la caja registradora**: una
línea por dato. **Es una propuesta mía, no un texto del servidor** ⚠️:

| Línea del ticket | Qué va |
|---|---|
| JUEGO | el nombre |
| TIENDA | Steam, Epic o GOG |
| ANTES | precio normal en soles |
| AHORA | precio rebajado en soles, o GRATIS |
| HASTA | fecha en que caduca |
| ENLACE | el enlace a la tienda |

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué Bob Esponja encaja | En la serie **el dinero tiene dueño**: Don Cangrejo. Se presenta con «Hello, I'm Mr. Krabs, and I like money» (01x10 00:04:58), canta a la caja «cha-ching» (04x05 00:01:24) y **no le sale la palabra «free»** (15x11 00:01:20). Y le encanta lo gratis **si se lo dan a él**: «any fella who's giving away free stuff is a friend o' mine» (02x08 00:06:00). |
| Objeto | **La caja registradora en su barquito** («register boat», 16x12 00:20:17), con **el menú de precios «Galley Grub»** colgado encima. Los dos se hacen en Blender. |
| Cuadro de diálogo propio | La serie **no usa globos**. Usa **la tarjeta de tiempo del Narrador Francés** («Unos momentos después…», tela pintada y letra que baila), **el menú de precios**, **carteles** («ORDER HERE», «OPEN») y **el botón del uniforme de Calamardo** («I Really Wish I Weren't Here Right Now», 03x10 00:15:11). |
| El más querido | No hay encuesta oficial de Nickelodeon. En Ranker (fans): **Patricio**, luego **Calamardo**. En el bracket de The Ringer (2021, 2,5 millones de votos entre todos los personajes de Nickelodeon) ganó **Bob Esponja** (§9). Para este canal manda **Don Cangrejo**; **Calamardo** es el cajero y el favorito de los adultos. |
| La escena del canal (vista) | Don Cangrejo entra gritando **«THE MONEY IS ALWAYS RIGHT!»**, pinzas abiertas, en el *Krusty Krab Training Video*, [3:55](https://www.dailymotion.com/video/x3uvarj?t=235). La caja real es **gris antracita `#282927`** ([3:52](https://www.dailymotion.com/video/x3uhkek?t=232)). |
| Letras | **Some Time Later** (la de las tarjetas; libre, OFL; trae tildes, ñ, ¿ y ¡). **Anton** para el menú. **Luckiest Guy** o **Titan One** para rótulos. **Chewy** para carteles a mano. Todas comprobadas. |
| Voz latina | Estudio **Etcétera Group** (Caracas), y desde la temporada 16 **DAT** (México). Don Cangrejo: **Luis Pérez Pons** (†2023), **Carlos Vitale** en las temporadas 6-9, y ahora **Olin Garcés**. Calamardo: **Renzo Jiménez** (siempre). Bob: **Luis Carreño**. Patricio: **Alfonso Soto**. Plankton: **Ángel Mujica**. Narrador: **Orlando Noguera** y luego **Juan Guzmán**. |
| Ejemplo de oferta de la propia serie | **Bob Esponja: Titanes de la Marea** (2025): se vende en **Steam y GOG** y ya tuvo rebajas del 40 %. |
| Tono | Alegre, tropical, de marinero. Madera cálida, telas tiki, cielo con flores. |
| Qué no hacer | Don Cangrejo **regalando** contento; globos blancos; nombres de España; 3D brillante. |

---

## 2 · Las escenas que sirven para #ofertas-y-gratis (con minuto)

**De dónde salen los minutos.** Del repositorio
[1440kHz/sbsp-chs-eng-sub](https://github.com/1440kHz/sbsp-chs-eng-sub):
subtítulos en chino e inglés, **con tiempos**, de las temporadas 1, 2, 3,
4, 7, 13, 14, 15 y 16 (190 archivos). Faltan la 5, 6, 8, 9, 10, 11 y 12.

- Cada archivo es **media hora de tele**: la intro y **dos episodios
  seguidos**. El primero empieza hacia 00:01:00 y el segundo hacia
  00:11:30.
- «03x07 00:13:15» quiere decir: archivo de la temporada 3, n.º 7,
  minuto 13:15 **desde el principio del archivo**. Con otra copia puede
  moverse uno o dos minutos.
- Las frases están en **inglés** (el subtítulo). La versión latina la
  pongo sólo si la encontré en una fuente (§10).
- Las tarjetas del narrador («A few moments later») **no salen en el
  subtítulo**: no tengo su minuto.

### 2.1 Don Cangrejo y el dinero (el corazón del canal) ✅ subtítulo

| Archivo y minuto | Episodio | Qué pasa | Para qué sirve |
|---|---|---|---|
| 01x10 00:04:58 | *Culture Shock* | En el concurso de talentos, Don Cangrejo sale al escenario: **«Hello, I'm Mr. Krabs… and I like money»**. En latino es el meme **«Hola, me gusta el dinero»** (§10). | **Presentar.** Es su tarjeta de visita. |
| 02x20 00:01:03 | *Squid on Strike* | Canta contando billetes: «Counting me money, money sweeter than honey… Profit will make me wallet fat». | Pose de **contar dinero** con cara de felicidad. |
| 04x05 00:01:24 a 00:02:04 | *Selling Out* | La canción **«Cha-ching, cha-ching, cha-chingaree… Money, oh, money, how I love thee… From pennies to dollars any amount'll do»**. | **Celebrar.** El «cha-ching» es el sonido de la caja. |
| 03x07 00:13:08 a 00:14:04 | *Can You Spare a Dime?* | Cuadra la caja. Le falta **su primera moneda de diez centavos**: «I always keep it at the back of the register for luck» (00:13:15). Acusa a Calamardo: «three possibilities… you stole it, you stole it, or you stole it» (00:13:48). | **Regañar.** Y un detalle para la caja: **la moneda de la suerte, al fondo del cajón**. |
| 02x01 00:13:37 a 00:14:26 | *Squid's Day Off* | Se le caen monedas: «That sounds like me money dropping». Las recoge como a bebés: «My babies… Papa clean you up». Luego se le **atasca la pinza con una moneda** y no la suelta: «I can think of ten good reasons to never let go of a dime, boy». | **Gesto**: acuna el dinero. |
| 03x04 00:10:11 | *Nasty Patty* | «**It's Open Cash Register Night!** First two customers get all the money in the cash register» (para sobornar a dos falsos inspectores). | Sirve para un **«gratis»** exagerado: abrir la caja. |
| 15x11 00:01:16 a 00:01:27 | *Delivery of DOOM* | En su anuncio de reparto: «If your food isn't in your hands in ten minutes or less, **it's f-f-f…**». Otro le sopla: «The line is, "Free"». **No le sale decir «gratis».** Y a las 00:03:05: «I ain't givin' out no free meals». | **El chiste perfecto para el canal**: Don Cangrejo atragantado con la palabra GRATIS. |
| 02x08 00:06:00 | *Christmas Who?* | «**Any fella who's giving away free stuff is a friend o' mine**». | **Animar a reclamar** lo gratis, en su voz. |
| 04x17 00:15:13 a 00:15:19 | *Rule of Dumb* | Patricio, rey por un día, dice que todo es gratis. Don Cangrejo: «**Nobody eats in me restaurant for free.** King or no king». | Contraste: lo gratis lo pone la tienda, no él. |
| 03x16 00:06:52 a 00:07:02 | *Born Again Krabs* | Tras casi morir, se vuelve generoso: «**Free toys for everyone! And free refills!**». Un cliente: «I thought you were a cheap old tightwad». Él: «I was, son, I was». | **Celebrar gratis**. Pose de brazos abiertos. |
| 07x06 00:12:57 y 00:16:11 | 2.ª mitad del archivo 07x06 (el nombre dice *Kracked Krabs*) | Lo nominan al **premio al cangrejo más tacaño**. En la convención presume de viajar por «the price of a 1¢ stamp» (00:14:05) y hace el **saludo del tacaño**: «Penny pinching, penny pinching… Cheap, cheap, cheap» (00:16:15). | Idea de lámina: **cazar la oferta más barata** como un deporte. |
| 03x06 00:11:47 a 00:12:40 | *One Krab's Trash* | Monta su **venta de garaje**: «Open for business!» (00:12:12) y regatea un paraguas con agujeros de 10 dólares a 5: «Okay, Mr. Bargain Hunter». | **Rebaja** con regateo; «Open for business» como cartel. |
| 07x19 00:02:29 a 00:02:44 | *Buried in Time* | Vende un llavero de recuerdo por **$49.57** y como rebaja «I'll throw in a coupon for one free ice cube». | **Precio raro con céntimos**, como en una oferta real. |
| 14x06 00:15:51 | *Necro-Nom-Nom-Nom-I-Con* | «**I can't pass up a sale**». | Frase corta para rebajas. |
| 02x03 00:14:35 | *Bubble Buddy* | Obliga a Calamardo a atender a una burbuja: «**Everyone's money is good here.** At the Krusty Krab, we serves all kinds». | Su lema de tienda: todo el mundo puede comprar. |

### 2.2 La caja registradora en pantalla ✅ subtítulo

| Archivo y minuto | Episodio | Qué pasa |
|---|---|---|
| 03x10 00:14:11 | *Krusty Krab Training Video* | El vídeo de formación la presenta: «Here you see our **automated money-handling system**». Y le dicen «**Don't touch**». |
| 03x10 00:14:28 | *Krusty Krab Training Video* | Calamardo al cliente (por el contexto ⚠️): «Now are you going to buy something or just stand there 'cause **there's a standing fee**». |
| 03x10 00:15:11 | *Krusty Krab Training Video* | El empleado «no tan bueno»: Calamardo, con el botón **«I Really Wish I Weren't Here Right Now»** en el uniforme. |
| 02x01 00:15:17 a 00:16:07 | *Squid's Day Off* | Calamardo, de «nuevo gerente», «asciende» a Bob Esponja para escaquearse: «You get to run **the cash register**… You'll be wearing two hats now». Y le enseña a usarla en una frase: «**You push the button and put the money inside**» (00:16:07). |
| 02x04 00:01:43 | *Dying for Pie* | Calamardo: «Mr. Krabs, you pay me to **stand behind this register**». |
| 03x08 00:13:52 | *Squilliam Returns* | Calamardín le suelta a Calamardo: «You're a cashier». |
| 03x09 00:08:57 | *Krab Borg* | «Who's watching the cash register?» |
| 16x12 00:20:17 a 00:22:28 | *Happy Krabby Birthday* | «Where's me **register boat**? And where's the cash register filled with me money?». Confirma el nombre: **el barco de la caja**. |
| 01x01 00:05:55 | *Help Wanted* | Ante la avalancha de anchoas, alguien del Crustáceo pide «a neat single-file line in front of the register» (quién lo dice ⚠️). |
| 04x05 00:09:14 | *Selling Out* | La cadena nueva cambia todo por una «automated cash register». |

### 2.3 Otras que sirven

- **Día gratis del zoo** — 02x12 00:12:04 (*The Smoking Peanut*): «the
  Bikini Bottom Zoo is having its annual **free day**. Free balloons, free
  drinks… free light bulbs?». ✅
- **La tienda de ofertas de la serie**: en *Help Wanted* (01x01
  00:06:02) sale un anuncio: «**Barg'N-Mart**, meeting all your spatula
  needs». Por el nombre («Bargain Mart») es **la tienda de ofertas** de Fondo de Bikini ✅ (subtítulo). No sé
  cómo se llama en latino ⚠️.
- **Patricio al teléfono** — 02x03 00:04:25 a 00:04:48 (*Big Pink
  Loser*): «Is this the Krusty Krab? — No, this is Patrick» (tres veces) ✅.
  Latino en §10.
- **Calamardo, cajero que odia su trabajo**: 02x04 00:01:43 y 03x10
  00:15:11 (arriba).

### 2.4 Vistas de verdad, fotograma a fotograma (segunda pasada) ✅ visto

YouTube dio 429 al primer intento. Se miraron **clips de Dailymotion**
enteros con `fotogramas.py --cortes` (un fotograma por plano). Son
resubidas de fans, en **baja resolución** (320×240 a 512×312, medido con
`ffprobe`) ⚠️ resolución, no 1080p. El minuto es **del clip**, no del
episodio.

***Krusty Krab Training Video*** (corto de 5:37, [Dailymotion x3uvarj](https://www.dailymotion.com/video/x3uvarj)):

| Minuto | Qué se ve | Para qué sirve |
|---|---|---|
| [0:29](https://www.dailymotion.com/video/x3uvarj?t=29) | El Crustáceo de día: letrero de concha «THE KRUSTY KRAB», banderas de señales, flores en el cielo turquesa. | Fondo del sitio, de día. |
| [0:38](https://www.dailymotion.com/video/x3uvarj?t=38) | El mismo plano de noche, con luna llena. | Fondo de noche. |
| [0:42](https://www.dailymotion.com/video/x3uvarj?t=42) | **Don Cangrejo duerme dentro del Crustáceo**, en una cama con forma de barquito. | Dato de sitio (§5). |
| [1:20](https://www.dailymotion.com/video/x3uvarj?t=80) | Tablero **«YOUR WORK STATION»** con los ingredientes rotulados (Ketchup, Mustard, Mayo, Patties, Pickles, Misc., Onions, Tomatoes, Lettuce, Buns). | Cartel del mundo con casillas (§7). |
| [1:40](https://www.dailymotion.com/video/x3uvarj?t=100) | **Calamardo** apoyado en la caja, leyendo, con el botón **«I REALLY WISH I WEREN'T HERE RIGHT NOW»**. | Confirma con fotograma la pose que antes estaba deducida del subtítulo. |
| [3:52](https://www.dailymotion.com/video/x3uvarj?t=232) | **Primer plano de la caja**: gris oscura, cajón abierto y vacío, pantallita arriba, botones redondos. Don Cangrejo al lado. | El objeto del canal, de verdad. |
| [3:55](https://www.dailymotion.com/video/x3uvarj?t=235) | **«THE MONEY IS ALWAYS RIGHT!»**: Don Cangrejo irrumpe por la puerta, pinzas muy abiertas, ojos como platos, gritando. | **La frase del canal.** |

Créditos en pantalla del corto: storyboard de **Aaron Springer y C. H.
Greenblatt**, artista de storyboard **Caleb Meurer** ✅ visto.

***Born Again Krabs*** (03x16, corto de 5:49, [Dailymotion x3uhkek](https://www.dailymotion.com/video/x3uhkek)):

| Minuto | Qué se ve | Para qué sirve |
|---|---|---|
| [0:05](https://www.dailymotion.com/video/x3uhkek?t=5) | Créditos: director de animación **Tom Yasumi**, director creativo **Derek Drymon**. | Dato de estudio (§18). |
| [1:32](https://www.dailymotion.com/video/x3uhkek?t=92) a 2:31 | En la cama del hospital, un **fantasma verde de su propia tacañería** lo persigue y discute con él. | El «demonio del avaro», muy visual. |
| [3:12](https://www.dailymotion.com/video/x3uhkek?t=192) | Cuelga el cartel **«LIVE FOR TODAY»** con los brazos abiertos y regala comida; a las 3:21, «COMPANY POLICY» escrito en una hamburguesa. | **Celebrar gratis.** |
| [3:47](https://www.dailymotion.com/video/x3uhkek?t=227) | Llega la factura **«BILL — TOTAL DUE $10,000»**, primer plano en sus pinzas. | **Pánico por dinero.** Antes y después, a 35 s. |
| [3:52](https://www.dailymotion.com/video/x3uhkek?t=232) | Don Cangrejo y Calamardo cobrando en la caja, otro ángulo. | Paleta de la caja medida aquí (§5.4). |
| [4:53](https://www.dailymotion.com/video/x3uhkek?t=293) | Letrero nuevo **«GRAND RE-OPENING»** en la fachada. | Cartel de «reapertura», sirve de rótulo de oferta. |

***Se busca ayuda*** (01x01, en latino, recorte de 7:40 dentro de un
marco de tele falso, 512×288, [Dailymotion x51sid2](https://www.dailymotion.com/video/x51sid2)):

| Minuto | Qué se ve |
|---|---|
| [1:13](https://www.dailymotion.com/video/x51sid2?t=73) | Bob hace ejercicio bajo un cartel **«PAIN»**. |
| [4:30](https://www.dailymotion.com/video/x51sid2?t=270) | **La casa de Don Cangrejo es un cofre del tesoro**; Bob llama a la puerta. |
| [6:57](https://www.dailymotion.com/video/x51sid2?t=417) | Don Cangrejo **señala el letrero «THE KRUSTY KRAB»** y se lo presenta a Bob: pose de **presentar**. |
| [7:30](https://www.dailymotion.com/video/x51sid2?t=450) | Plano final del letrero y la fachada. |

> Lo mejor de estos vídeos para el canal: el grito de 3:55, la caja de
> 3:52 y el salto de «LIVE FOR TODAY» (3:12) a la factura de $10 000
> (3:47). Todo **visto**, no deducido.

---

## 3 · Arte oficial y referencias visuales

> [!note] Ya hay hojas de contacto (segunda pasada)
> En la primera pasada Fandom daba 403. Ahora `investigar_serie.py` sacó
> **214 imágenes grandes** de 6 fichas de la wiki en inglés. Las 3 mejores
> hojas están en `hojas/`; qué número sirve para qué, en **§3.6**.

### 3.1 Portadas oficiales de videojuegos (arte promocional con poses vivas) ✅ visto

Del archivo público [libretro-thumbnails (GameCube)](https://github.com/libretro-thumbnails/Nintendo_-_GameCube)
(carpetas `Named_Boxarts` y `Named_Snaps`). Son portadas de THQ con arte
oficial de Nickelodeon:

| Portada | Tamaño | Qué se ve | Sirve para |
|---|---|---|---|
| *Battle for Bikini Bottom* (2003) | 512×716 | **Bob Esponja saludando** como soldado, con **casco de camuflaje**, sonrisa pícara y un ojo entrecerrado. Se ve camisa blanca, **corbata roja** y pantalón marrón. | **Presentar** con autoridad. Colores de Bob medidos aquí (§16). |
| *Lights, Camera, Pants!* (2005) | 483×680 | Cuatro viñetas: Bob gritando, **Patricio de policía** enfadado, **Calamardo con capa y pajarita roja** alzando el puño, **Plankton con sombrero** riendo. | Caras **enfadadas y exageradas**. Calamardo y Plankton «actuando». |
| *Creature from the Krusty Krab* (2006) | 512×729 | Bob en avioneta, Plankton gigante detrás. | Acción. |
| *Revenge of the Flying Dutchman* (2002) | 466×672 | Bob **gritando con la boca enorme** sobre un tesoro. | Susto, prisa. |
| Captura de *Lights, Camera, Pants!* | 512×384 | Un minijuego en **la cocina del Crustáceo**, a pantalla partida: Patricio, Calamardo y Bob cocinan, hay **hamburguesas** y un **marcador de tiempo «2:35»** en letras amarillas. | Idea de **cuenta atrás** para «los gratis caducan». |
| Captura de *Battle for Bikini Bottom* | 512×384 | Rótulo del juego **«SUPER COMBO!»**: letra amarilla, gorda y redonda, con borde oscuro. | Estilo de rótulo de los juegos. |

### 3.2 Campañas oficiales recientes ✅

- **SpongeBob 25** (2024): Nickelodeon estrenó **arte nuevo por el 25.º
  aniversario** ([AWN](https://www.awn.com/news/exclusive-happy-25th-spongebob-squarepants-anniversary-artwork),
  [NickALive](https://www.nickalive.net/2024/07/nickelodeon-unveils-happy-25th.html),
  [PR Newswire](https://www.prnewswire.com/news-releases/nickelodeon-commemorates-25-years-of-spongebob-squarepants-with-larger-than-life-tribute-to-original-pilot-episode-at-comic-con-international-san-diego-2024-302193519.html)).
  Ahora **vistas** (segunda pasada) ✅✅:
  - **«25 con medusas»** ([imagen, 620×413](https://www.awn.com/sites/default/files/styles/inline/public/image/featured/25_anniversary_jellyfish_final-1280.jpg)):
    los 6 principales **cazan medusas con redes**. Don Cangrejo, Patricio,
    Bob (red en mano, lengua fuera) y Calamardo corren en fila por el
    césped; Gary detrás; Arenita con su traje espacial flota arriba;
    Plankton espía bajo una hoja. Las medusas rosas forman el «25». Fondo
    pintado, degradado turquesa y coral morado. Pose de **acción con
    objeto**.
  - **«25 con burbuja de flor»** ([imagen, 620×652](https://www.awn.com/sites/default/files/styles/inline/public/image/attached/1062874-25anniversarybubblefinalforpressonly-1280.jpg)):
    **foto de grupo mirando a cámara**. Bob sopla una burbuja con forma de
    flor que dibuja el «25»; a su lado Don Cangrejo, Arenita (lo abraza),
    Patricio, Calamardo y Gary. Pose de **grupo feliz que presenta**.
  - Estilo medido con `estilo.py`: **pintado con degradado**, saturación
    41-51 %, línea gris rosada suave. **No** es el color plano de la serie
    (ver §18).
  - En el mismo artículo de AWN hablan Tom Kenny, Bill Fagerbakke, Carolyn
    Lawrence, Rodger Bumpass, Clancy Brown y Mr. Lawrence ✅.
- Notas de prensa y fotos oficiales: [Paramount Press Express](https://www.paramountpressexpress.com/nickelodeon/shows/spongebob-squarepants/releases/).
- **Bob Esponja: En busca de los pantalones cuadrados** (cines, 25 de
  diciembre de 2025): tráileres doblados en [ANMTV (julio 2025)](https://www.anmtvla.com/2025/07/bob-esponja-en-busca-de-los-pantalones.html)
  y [ANMTV (noviembre 2025)](https://www.anmtvla.com/2025/11/bob-esponja-en-busca-de-los-pantalones.html). Tema pirata.
- **Plankton: La película** (Netflix, 7 de marzo de 2025): Karen se
  rebela ([Wikipedia](https://en.wikipedia.org/wiki/Plankton:_The_Movie),
  [Netflix](https://www.netflix.com/title/81221337)).

### 3.3 Hojas de modelo oficiales

- El **«Main Model Pack»** (1999): el libro que usaba el equipo para dibujar
  igual a Bob, Patricio, Calamardo, Don Cangrejo y Arenita. Trae dibujos de
  construcción con notas debajo ✅ ([Encyclopedia SpongeBobia](https://spongebob.fandom.com/wiki/Main_Model_Pack)).
  **Ya se pudo ver** (segunda pasada) ✅✅: lo usó Nickelodeon Animation
  Studio de 1999 a 2016. Al principio traía 8 personajes (Arenita en
  bañador y con traje espacial, Bob, Patricio, Calamardo, Don Cangrejo, la
  Sra. Puff y Perla); luego Gary y, tras la película de 2004, Plankton.
  Karen fue al «BG Layout Stock Pack» porque es un objeto. Segunda fuente:
  una foto de Vincent Waller (director de arte) citada en la wiki, y el
  *making of* *Show Design* del DVD *Nautical Nonsense and Sponge Buddies*
  (2002), minuto **18:00**.
- **Foto del cuaderno real** abierto en la mesa de un animador, con pinceles
  y botes de pintura; encima, un fondo con rocas y niebla y las siluetas en
  color de Patricio, Bob, Calamardo y Don Cangrejo ([imagen, 909×532](https://static.wikia.nocookie.net/spongebob/images/9/9a/Season_1_Complete_Model_Pack.png/revision/latest?cb=20190218054312)) ✅ visto.
- **«SpongeBob Main Characters», hoja de modelo oficial a color**
  ([imagen, 2200×2200](https://static.wikia.nocookie.net/spongebob/images/f/fa/SpongeBob-Main-Characters-sheet-color.jpg/revision/latest?cb=20260405224319)) ✅ visto y medido:
  cuerpo entero de frente y de lado. Página 1: Arenita en bikini y con
  traje espacial, Gary, Bob, Patricio (short verde de flores moradas).
  Página 2: Calamardo, Don Cangrejo, Sra. Puff, Perla. **Es la mejor
  referencia de vestuario**: de aquí salen los hex de §16.
- **Ficha Pantone oficial de color** ([imagen, 800×1100](https://static.wikia.nocookie.net/spongebob/images/8/8c/SpongeBob-character-model-colors-Pantone.jpg/revision/latest?cb=20210313185736)) ✅✅:
  la hoja de color del estudio (Bob, Arenita, Sra. Puff). Tabla en §16.
- **Bocetos de diseño**: Don Cangrejo de Hillenburg en 1996 ([imagen, 950×650](https://static.wikia.nocookie.net/spongebob/images/c/c6/Crabs-Stephen-Hillenburg-1996.jpg/revision/latest?cb=20211021073925))
  y Patricio ([imagen, 950×800](https://static.wikia.nocookie.net/spongebob/images/9/9c/Design-patrick.jpg/revision/latest?cb=20190725154202)) ✅ visto (hoja de objetos, n.º 211 y 203).
- **Logo de la serie en vector** ([SVG, 600×600](https://static.wikia.nocookie.net/spongebob/images/4/46/SVG_SpongeBob_SquarePants.svg/revision/latest?cb=20181117230211)),
  colores leídos del propio código ✅✅: amarillo `#FFF463`, contorno
  verde oliva `#B2B618` y `#919107`, rojo `#EF5240` y `#EB1C22`, marrón
  `#B26E2D`.

### 3.4 Objetos de la serie, recreados en juegos (sólo referencia) ✅ visto y medido

Texturas sacadas de juegos por fans y subidas a GitHub. **No son libres**:
el copyright es de Nickelodeon y THQ. Sirven para mirar formas y colores,
nunca para pegar.

- **El menú «Galley Grub»** (420×420), de un proyecto de Unity de un
  estudiante ([MishaalButt/Projects](https://github.com/MishaalButt/Projects),
  carpeta `Unity - Krusty Krab Kook-Off/Assets/SpongebobAssets/Objects/Menu`):
  - Título **GALLEY GRUB** en letra condensada muy gorda, rojo ladrillo
    `#954033` con borde marrón muy oscuro `#541713`.
  - Fondo crema `#E7D09C`. Texto de la lista en marrón `#51241D`, con
    **puntos guía** hasta el precio.
  - Precios: Krabby Patty **1.25** (con queso 1.50), Double **2.00**,
    Triple **3.00**, Coral Bits 1.00 a 1.50, Kelp Rings 1.50, Salty Sauce
    .50, Seafoam Soda 1.00 a 1.50, Krabby Meal 3.50…
- **El cartel «ORDER HERE»**: letras rojo vino `#500002`, de trazo a mano,
  sobre verde oliva `#697922`.
- **La caja registradora** (textura de 64×64; por el nombre del archivo, volcada de un juego de GameCube ⚠️):
  cuerpo **azul pizarra** `#427193`, ventanita azul claro `#89BED7`,
  teclas redondas, **contorno negro grueso**. Otra textura (128×128) trae
  blanco, gris azulado `#738E9C` y **rojo** `#BD0C10`.
  **Ojo (segunda pasada)**: en la serie, vista en vídeo, la caja es **gris
  antracita `#282927`**, no azul (*Born Again Krabs*, [3:52](https://www.dailymotion.com/video/x3uhkek?t=232), §5.4) ✅ medido.
  El azul es de la textura del juego. Para la lámina manda el gris del
  episodio; el azul puede ser otra temporada, por eso se dejan las dos.
- **Fachada del Crustáceo** (texturas de *Battle for Bikini Bottom* en el
  mod [hmmm2121/Doom-of-the-Bob](https://github.com/hmmm2121/Doom-of-the-Bob),
  carpeta `Assets/Maps/BikiniBottomHub/Textures`):
  - Letrero: **concha de almeja rosa** `#E4CBD6` con **«THE KRUSTY KRAB»**
    en letras rojas de palo.
  - Puertas **azules** `#4254A4` con tiradores **amarillos**.
  - Ventana azul `#3B5DB3` con cartel **«OPEN»** blanco y rojo.
  - Banderas náuticas de señales (rojo `#9D000B`, amarillo, azul).
  - Tablones de madera `#6A4B2D` y red de cadena de nasa.

### 3.5 Tarjetas de tiempo (fondos) ✅ visto

El generador de tarjetas de [Jordy3D](https://github.com/Jordy3D/Jordy3D.github.io)
(carpeta `projects/sometimelater`) trae **18 fondos** de tarjetas
(1000×~730, `bgs/001.webp` a `018.webp`). Son **telas pintadas**:
- burbujas azules (001), bambú negro sobre azul (002), flores y piñas
  sobre turquesa (003), tikis sobre cielo azul (004), espirales naranjas
  (005), medusas verdes sobre azul noche (006), **medusas rosas sobre
  negro** (007), bambú verde (008), **piñas sobre tapa amarilla** (009),
  flores blancas sobre rojo (010), **tela tiki azul** (011), **hibiscos
  naranjas** (012), tiki morado (013), hibiscos morados (014), **palmeras
  sobre amarillo** (015), **tela tiki roja** (016), casi negro (017),
  bellotas sobre verde (018).
- Promedios medidos: 009 `#D6B12F`, 015 `#DFC834`, 016 `#620C0B`,
  011 `#0C293F`, 007 `#130C25`.

### 3.6 Las hojas de contacto (`hojas/`) ✅ vistas

Salen de `investigar_serie.py --wiki spongebob` con 6 fichas en inglés
(«Eugene H. Krabs», «Squidward Tentacles», «SpongeBob SquarePants
(character)», «Patrick Star», «Sheldon J. Plankton», «Krusty Krab»): 254
imágenes, 214 grandes, 5 hojas. Quedan 3. El número es el del recuadro
amarillo de cada miniatura. Las revisé yo, una por una.

**`personajes_01.jpg`** (n.º 1-48): stock art de cuerpo entero, renders 3D
y fotogramas en 1920×1080.

| N.º | Qué es | Para qué |
|---|---|---|
| 1 | Bob feliz, brazos arriba, stock art 4429×4368 ([original](https://static.wikia.nocookie.net/spongebob/images/6/6b/Spongebob_happy_stock_art_1.octet-stream.png/revision/latest)) | **Celebrar**, presentar |
| 2 | Calamardo con desgana, stock art 3500×3500 ([original](https://static.wikia.nocookie.net/spongebob/images/4/49/Squidward_unhappy_stock_art.png/revision/latest)) | **Cajero harto** (concepto B) |
| 3 | Don Cangrejo sonriente, pinzas abiertas, 3000×3000 ([original](https://static.wikia.nocookie.net/spongebob/images/7/7f/Eugene_Krabs.png/revision/latest)) | **Presentar** la oferta (concepto A) |
| 8 | Patricio, stock art pintado, 2500×2500 ([original](https://static.wikia.nocookie.net/spongebob/images/5/5f/Patrick_stock_art_%28oil_painted%29.png/revision/latest)) | Animar |
| 9 | Plankton malvado, 2500×2500 ([original](https://static.wikia.nocookie.net/spongebob/images/6/6b/EvilPlankton24.png/revision/latest?cb=20251104033338)) | Concepto C |
| 11 | Calamardo con el clarinete, 2009×2421 ([original](https://static.wikia.nocookie.net/spongebob/images/7/72/Squidward_with_clarinet_stock_art.png/revision/latest?cb=20200812083255)) | Calamardo fuera del trabajo |
| 16 | Patricio en *Nickelodeon All-Star Brawl 2* (render 3D) | Cruces (§23) |
| 17 | El Crustáceo por fuera, stock 2400×1746 ([original](https://static.wikia.nocookie.net/spongebob/images/7/77/KrustyKrabStock.png/revision/latest?cb=20221031053149)) | Fondo de día |
| 19 y 38 | **La billetera de Don Cangrejo** con su carné de Fondo de Bikini | Objeto de dinero |
| 21 | Oficina de Don Cangrejo, 2071×1500 ([original](https://static.wikia.nocookie.net/spongebob/images/5/52/KrustyKrabOfficeDay.png/revision/latest?cb=20231121222630)) | Fondo interior |
| 23 | Cocina del Crustáceo, 1898×1500 ([original](https://static.wikia.nocookie.net/spongebob/images/2/20/KrustyKrabKitchenStock.png/revision/latest?cb=20231121223009)) | Fondo interior |
| 25, 27, 30, 32, 33 | Renders 3D de *Kamp Koral* (Don Cangrejo, Patricio, Plankton, Calamardo, Bob) | Volumen para Blender |
| 39 | Don Cangrejo gritando, primer plano (*Friendiversary*, 1920×1080, [original](https://static.wikia.nocookie.net/spongebob/images/f/f8/Friendiversary_130.png/revision/latest?cb=20230623224126)) | **Regañar** |
| 40 | Don Cangrejo con sonrisa enorme (*Krabby Patty Creature Feature*, [original](https://static.wikia.nocookie.net/spongebob/images/5/5a/Krabby_Patty_Creature_Feature_012.png/revision/latest?cb=20171022164932)) | **Celebrar** |
| 42 | Don Cangrejo abre la billetera con las dos pinzas (*Mall Girl Pearl*, [original](https://static.wikia.nocookie.net/spongebob/images/0/00/Mall_Girl_Pearl_034.png/revision/latest?cb=20220706154704)) | **Pagar / cobrar** |

**`fondos_01.jpg`** (n.º 49-96): fotogramas 1920×1080 de sitios.

| N.º | Qué es | Para qué |
|---|---|---|
| 75 | Laboratorio del Balde de Carnada con Karen (*Plankton Retires*, [original](https://static.wikia.nocookie.net/spongebob/images/2/27/Plankton_Retires_043.png/revision/latest?cb=20221221023340)) | Concepto C |
| 79 | La piña de Bob | Fondo |
| 84 | Bob y Don Cangrejo junto a la puerta «EMPLOYEES ONLY» | Interior |
| **86** | **Don Cangrejo en una escalera cuelga el cartel «DAILY SPECIAL BBQ NUTS»**, rojo con letras amarillas, junto a «ORDER HERE»; Calamardo en el **barquito de la caja** (*Hot Crossed Nuts*, [original](https://static.wikia.nocookie.net/spongebob/images/e/e0/Hot_Crossed_Nuts_045.png/revision/latest?cb=20230623060414)) | **Oferta del día** (concepto B) |
| **88** | **Cartel de madera colgante «KOWBOY KRAB'S NUT SHACK»** con precios y puntos guía: «NUTS…… 5.00», «KRABBY PATTY…… 1.25»; Don Cangrejo con sombrero vaquero, sonriendo (*Hot Crossed Nuts*, [original](https://static.wikia.nocookie.net/spongebob/images/c/c1/Hot_Crossed_Nuts_124.png/revision/latest?cb=20230623060311)) | **Cartel de precios de la propia serie** (concepto A) |
| 90 | El Crustáceo **nevado**, en stop-motion (*It's a SpongeBob Christmas!*, [original](https://static.wikia.nocookie.net/spongebob/images/6/63/It%27s_a_SpongeBob_Christmas%21_063.png/revision/latest?cb=20200105214847)) | Ofertas de Navidad |
| 93 | El Crustáceo de día (*The Patrick Star Show*, [original](https://static.wikia.nocookie.net/spongebob/images/a/af/The_Krusty_Krab_in_TPSS.png/revision/latest?cb=20230531052600)) | Fondo de día |
| 94 | El Crustáceo **de noche** con farolillos (*The Legend of Boo-Kini Bottom*, [original](https://static.wikia.nocookie.net/spongebob/images/9/90/The_Legend_of_Boo-Kini_Bottom_174.png/revision/latest?cb=20171014103718)) | Ofertas de Halloween o de noche |
| 96 | Bob y Don Cangrejo ante una pared de monitores (*Truth or Square*, [original](https://static.wikia.nocookie.net/spongebob/images/0/0e/Truth_or_Square_344.png/revision/latest?cb=20220205010123)) | Idea de «pantallas de tienda» |

**`objetos_01.jpg`** (n.º 193-214): fichas, carteles y bocetos.

| N.º | Qué es | Para qué |
|---|---|---|
| **194** | **El tablón de corcho del Crustáceo** (900×1000): notas clavadas, «Money of the Month Club», «IN CASE OF CHOKING», «Modern Dance Lessons», «ROOMMATE WANTED», «Canned Food Drive», «Mrs. Puff's Driving School», una lista de la compra ([original](https://static.wikia.nocookie.net/spongebob/images/5/55/KKbulletinboard.jpg/revision/latest?cb=20130619095820)) | **Tablón de ofertas** (lámina 2) |
| 196 | Ficha Pantone de color | Colores exactos (§16) |
| 200 | **Carné de conducir de Patricio**, «Bikini Bottom Driver License» (1024×768, [original](https://static.wikia.nocookie.net/spongebob/images/3/3f/License.jpg/revision/latest?cb=20120329082855)) | Documento del mundo (§19) |
| 203, 198 y 211 | Bocetos de Patricio y de Don Cangrejo (Hillenburg, 1996) | Línea de construcción |
| 204 | Biografía temprana de Plankton (2000), página de libro | Tono del mundo |
| **209** | **Don Cangrejo abraza un billete de $10.000.000** en su cama (950×675, [original](https://static.wikia.nocookie.net/spongebob/images/5/55/Krabs_with_money.png/revision/latest?cb=20200213000335)) | **Amor al dinero** |
| 214 | Cuadro del mundo «The Clam Calamity» con marco dorado | Cartel antiguo (§19) |

> Corrección del redactor: la parte de imagen decía que la billetera es la
> n.º 39 y que «Phylum Porifera» es la n.º 98 de esta hoja. Al mirarla, la
> billetera es la **19** (y la 38) y la hoja de personajes sólo llega a
> la 48: «Phylum Porifera» no está en las 3 hojas guardadas ⚠️.

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D en Sketchfab (licencias comprobadas por la API en la segunda pasada)

En la primera pasada Sketchfab no abría y la licencia salía del resultado
de búsqueda. En la segunda se miró el campo de licencia de la **API de
Sketchfab** (`/v3/search?type=models`). Lo que no se volvió a comprobar
queda como estaba («según la búsqueda»).

**Confirmado por la API** ✅:

| Modelo | Autor | Licencia (API) | Para qué |
|---|---|---|---|
| [BFBBR - Krusty Krab Cash Register](https://sketchfab.com/3d-models/bfbbr-krusty-krab-cash-register-cc79260fc5f44d73b8268f68dfb83a3f) | SMF Features Developed From Cheryl Hill | CC Attribution | la caja del Crustáceo, pero **sacada del juego** *Rehydrated* (THQ Nordic): mirar, no publicar |
| [The Krusty Krab](https://sketchfab.com/3d-models/the-krusty-krab-e109df8b1cb1487dbf2553e5e2d7eff1) | Mrlunettes | **CC Attribution-NonCommercial** | **corregido**: antes decía «descarga gratis»; es **no comercial** |
| [Mr Krabs (Spongebob)](https://sketchfab.com/3d-models/none-d7e712d733ae4de69623cd408d68a289) | Yanez Designs | CC Attribution | Don Cangrejo en 3D |
| [Krabby Patty (Spongebob)](https://sketchfab.com/3d-models/none-6bf2dc6ffc594a8598bcf84f5d0325f1) | Yanez Designs | CC Attribution | la Cangreburger, objeto suelto |
| [Krusty Krab Employee Hat (Spongebob)](https://sketchfab.com/3d-models/none-8d0e167b2eef4c9d8b99bfd4823d9329) | Yanez Designs | CC Attribution | el gorro de empleado |
| [Krusty Krab Menu (Spongebob)](https://sketchfab.com/3d-models/none-2d19327e22284f7e85ffd444e55bbbc8) | Yanez Designs | CC Attribution | **el menú de precios**, para el objeto del canal |
| [Jelly Fish (Spongebob)](https://sketchfab.com/3d-models/none-4227c0c46a1640ef9c61c455f7bc10f7) | Yanez Designs | CC Attribution | medusa |
| [The SpongeBob Squarepants](https://sketchfab.com/3d-models/none-74e87e0af5b2495792d8068d561fd816) | Pixel | CC Attribution | Bob completo |
| [Plankton](https://sketchfab.com/3d-models/none-683b0ce1f9324ae9ba59bcda10a18d80) | 1ooooJ0Y | CC Attribution | Plankton |
| [Sandy Bikini](https://sketchfab.com/3d-models/none-ee46def4864945198c053754725f9a9a) | Placidone | CC Attribution | Arenita |
| [Spongebob Rig](https://sketchfab.com/3d-models/spongebob-rig-5009dc11dd1f45d3ac8dda79b06e09db) | FreeModeler12345 | CC Attribution, descargable | *rig* de Bob; dedos y casi toda la cara **sin riggear** (lo dice el autor) |
| [Battle for bikini bottom SpongeBob Rig](https://sketchfab.com/3d-models/none-e0848f57d5074f9daf90d9b7817ce098) | — | CC Attribution | **sacado del juego**: mirar, no usar |

**Del recolector** (licencia de la API guardada en `datos-imagen.md`) ✅:
[Plankton de Vin D'Alembert](https://sketchfab.com/3d-models/none-3f1a3065100c44038aa0fee5886e5818),
[«Calamardo Fuerte Hermosura»](https://sketchfab.com/3d-models/none-79e86cbc30a94005af544fd1e8203c53)
y [«Calamardo en Reposo»](https://sketchfab.com/3d-models/none-84f4d2a5a4af43f1810045daabffdf6b) de Mike BlueG,
[Gary de Osvaldo Mendes](https://sketchfab.com/3d-models/none-873d034079d84b70b2c22bfe1d121558),
[«BOB ESPONJA RIGGED» de Sapx](https://sketchfab.com/3d-models/none-ba715233cda9453fb2ec47c6a641d84d)
y [«Colorburgers - Pretty Patties» de David Tena C.](https://sketchfab.com/3d-models/none-d95d332a61114c788b03aac3047c2fdf):
todos CC Attribution.

**Lo mejor**: el catálogo de **Yanez Designs** (Don Cangrejo, la
Cangreburger, el gorro, el menú, la medusa). Piezas sueltas, CC BY, fáciles
de juntar en Blender. Crédito: «*Título* por Yanez Designs, CC BY 4.0,
Sketchfab».

**Sin volver a comprobar** (tabla de la primera pasada, abajo): la
licencia de «The Krusty Krab» de pizzabrian no reapareció en la API ⚠️ (quizá
lo retiraron); la caja genérica de BumBácBonifác sale como descarga gratis
**sin licencia CC explícita** en la API ⚠️.

| Modelo | Autor | Licencia que dice | Ojo |
|---|---|---|---|
| [BFBBR - Krusty Krab Cash Register](https://sketchfab.com/3d-models/bfbbr-krusty-krab-cash-register-cc79260fc5f44d73b8268f68dfb83a3f) | SMF Features Developed From Cheryl Hill (@cherylhill28) | descarga gratis | **Sacado del juego** *Rehydrated*: el copyright es de THQ Nordic. Mirar, no publicar. |
| [SBFBBR - The Krusty Krab](https://sketchfab.com/3d-models/sbfbbr-the-krusty-krab-8c26feea1c244336aba17c138f894810) | el mismo | CC BY (según la búsqueda) | igual: sacado del juego. |
| [TSCP - Krusty Krab Interior](https://sketchfab.com/3d-models/tscp-krusty-krab-interior-360b06ee55de4fda975b7f58f4568045) | el mismo | descarga gratis | interior entero: barco de la caja, mesas. |
| [The Krusty Krab](https://sketchfab.com/3d-models/the-krusty-krab-45f210e1a77b481a872040b627832415) | pizzabrian | CC BY (según la búsqueda) | hecho por un fan. Comprobar licencia antes. |
| [The Krusty Krab!](https://sketchfab.com/3d-models/the-krusty-krab-4db13d7b4ac642028f51072a2b8b1eb5) | Phillyy cheesesteakk gamingg (@milene2009) | CC BY (según la búsqueda) | fan. |
| [The Krusty Krab](https://sketchfab.com/3d-models/the-krusty-krab-e109df8b1cb1487dbf2553e5e2d7eff1) | Mrlunettes | **CC BY-NC** (API, segunda pasada) | fan, interior y exterior. No comercial. |
| [Cash Register](https://sketchfab.com/3d-models/cash-register-1e04d7a73a004e2380e2ee715ce7bd06) | BumBácBonifác (@ondraman43) | descarga gratis | **caja genérica**: la más segura como base para modelarla a mano. |

**Recomendación**: modelar la caja y el barquito a mano en Blender (son
formas simples) mirando estas referencias. Si se usa un modelo CC BY, el
crédito va así: «*Título* por *autor*, CC BY 4.0, Sketchfab».

### 4.2 Fan art y 3D en ArtStation (mirar, nunca pegar)

- [spongebob krusty krab in blender](https://www.artstation.com/artwork/58rzyE) — bboDX ryuheun: low poly en Blender, con *timelapse*.
- [Krusty Krab 3D Model (Sponge on the Run)](https://www.artstation.com/artwork/o2yxK4) — Taina Santanna: exterior e interior.
- [Krusty Krab 3D Model](https://www.artstation.com/artwork/PmDYq3) — Clarissa Amelinda.
- [The Krusty Krab | Bikini Bottom Tales](https://www.artstation.com/artwork/mA8ZA9) — Derick Keplinger: para un juego de fans.
- [«The Krusty Krab» (SpongeBob)](https://www.artstation.com/artwork/oJWeyJ) — Victor Silva: *shaders* de dibujo animado con aire de PS2.
- [Krusty Krab](https://www.artstation.com/artwork/Ny5E1D) — autor no visto.
- [LEGO Ideas: The Krusty Krab](https://ideas.lego.com/projects/371ac729-1f11-4d8e-ba21-619dbed5e63f) — maqueta de fan que llegó a revisión.

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 El Crustáceo Cascarudo por fuera ✅

- Tiene forma de **nasa de langosta de Nueva Inglaterra**
  ([Encyclopedia SpongeBobia](https://spongebob.fandom.com/wiki/Krusty_Krab),
  [Wikipedia](https://en.wikipedia.org/wiki/Krusty_Krab)).
- Tablones de madera, ventanas y puertas azules, letrero de concha rosa,
  banderas de señales (medido en §3.4).

### 5.2 El Crustáceo Cascarudo por dentro ✅ (una wiki) ⚠️

Según [Encyclopedia SpongeBobia](https://spongebob.fandom.com/wiki/Krusty_Krab):
- **El puesto de pedidos** está junto a la puerta de la cocina. Es **un
  barquito**. Dentro va **la caja registradora** y ahí trabaja Calamardo.
- Detrás, **la ventana de la cocina**, con forma de **proa de barco**. Por
  ahí pasa los pedidos a Bob Esponja.
- El barquito **se ha llegado a conducir** («F.U.N.»).
- **Sillas de barril** y mesas hechas con **timones de barco**.
- **Un reloj de timón** encima de las puertas dobles.
- **La oficina de Don Cangrejo**: caja fuerte, escritorio hecho con un
  **baúl de marinero**, sillas de barril, cuadros y **dinero enmarcado en
  la pared**.
- La caja registradora es **gris pizarra o azul oscura** según la wiki.
  **Medida en un fotograma** (segunda pasada): **gris antracita `#282927`**
  ([*Born Again Krabs*, 3:52](https://www.dailymotion.com/video/x3uhkek?t=232)) ✅.
  En la wiki la llaman **«Betsy»** y **«Cashy»** ⚠️ ([ficha de la caja](https://spongebob.fandom.com/wiki/Krusty_Krab_cash_register)).
- El barquito de la caja se ve bien en la hoja `fondos_01.jpg`, n.º 86:
  casco blanco con franja roja, Calamardo dentro, caja gris encima ✅ visto.
- En la serie el sitio de la caja se llama **«register boat»** (16x12
  00:20:17, subtítulo) ✅.

### 5.3 Otros sitios que sirven

- **El Balde de Carnada** (Chum Bucket), de Plankton y Karen: el
  restaurante que **no triunfa** ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Plankton_and_Karen),
  [Plankton: The Movie](https://en.wikipedia.org/wiki/Plankton:_The_Movie)). Está
  **enfrente**, al otro lado de la calle ✅ (segunda pasada: [Wikipedia](https://en.wikipedia.org/wiki/SpongeBob_SquarePants)
  y la biografía de Plankton de 2000, «Across the street is the Chum
  Bucket», hoja `objetos_01.jpg`, n.º 204).
  En la 1.ª temporada latina se llamó **«El Balde de Bocados»** ✅ (Doblaje Wiki).
- **Barg'N-Mart**: la tienda barata (01x01 00:06:02, subtítulo) ✅.
- **El cielo de Fondo de Bikini**: nubes con forma de **flor**. Hillenburg
  dijo que eran para dar **«sensación hawaiana»** ✅ (segunda pasada: [foro de SBMania](https://www.sbmania.net/forums/threads/what-up-with-the-flower-clouds.43079/)
  y [Wikipedia](https://en.wikipedia.org/wiki/SpongeBob_SquarePants), con
  nota a Hogan's Alley: «como una camisa hawaiana floreada»).
  El **arco de flores** ya estaba en su biblia de 1996 ✅ ([Encyclopedia SpongeBobia](https://spongebob.fandom.com/wiki/Flower_arch)).
- **La casa de Don Cangrejo** (segunda pasada, visto en vídeo) ✅: hay **dos
  versiones**. En *Se busca ayuda* es **un cofre del tesoro** aparte
  ([4:30](https://www.dailymotion.com/video/x51sid2?t=270)). En el
  *Krusty Krab Training Video* duerme **dentro del Crustáceo**, en una cama
  con forma de barquito ([0:42](https://www.dailymotion.com/video/x3uvarj?t=42)).
  No es un error nuestro: la serie no cuida esa continuidad.

### 5.4 Luz (medida en fotogramas en la segunda pasada)

- **Fuera, de día** ✅ medido: fotograma 0:24 del *Krusty Krab Training
  Video* ([ver](https://www.dailymotion.com/video/x3uvarj?t=24)), con
  `estilo.py`. **Cielo `#289FBF`** (27 %), verde agua `#4BC2AB` (24 %),
  madera y sombra oscuras `#1F1F15` y `#465247` (15 % y 13 %), arena
  `#D0CFBA` (14 %), flor verde `#97A680` (7 %). Cielo turquesa **liso**,
  sombra **plana** bajo el edificio, flores de fondo en amarillo, celeste y
  violeta. **Luz plana de mediodía, sin sombras duras**: antes era de
  memoria, ahora está visto.
- **La caja, de cerca** ✅ medido: fotograma 3:52 de *Born Again Krabs*
  ([ver](https://www.dailymotion.com/video/x3uhkek?t=232)). Cuerpo **gris
  antracita `#282927`** (28 %), ventana del local azul `#3C95B7` (10 %),
  pinzas de Don Cangrejo `#B93F23` (5 %), negro del encuadre `#040505`
  (37 %, incluye las barras del vídeo).
- **Dentro del Crustáceo**: luz cálida de día, tonos de madera, sin
  sombras duras. Los ojos de buey dejan ver agua azul. ⚠️ No se midió un
  fotograma del interior (quedó pendiente, sobre todo de noche).
- **De noche**: el mismo plano del Crustáceo con luna llena ([0:38](https://www.dailymotion.com/video/x3uvarj?t=38))
  y la hoja `fondos_01.jpg`, n.º 94 (farolillos) ✅ visto.
- **Cierre de cada episodio**: cartela amarilla con flores de fondo para
  los «BACKGROUND PAINTERS» ([0:16](https://www.dailymotion.com/video/x3v1puo?t=16))
  y el logo de **United Plankton Pictures** dibujado a mano, plancton a
  rotulador sobre cian ([0:34](https://www.dailymotion.com/video/x3v1puo?t=34));
  después, el logo de Nickelodeon garabateado en naranja sobre negro
  ([0:39](https://www.dailymotion.com/video/x3v1puo?t=39)) ✅ visto.
- Dato del subtítulo: **«the store closes at 6:00»** (03x10 00:12:43,
  vídeo de formación). Es de día.

### 5.5 Paleta

| Qué | Hex | De dónde |
|---|---|---|
| Amarillo de Bob | `#FDEE4A` | medido en la portada de *BFBB* ✅ |
| Pantalón de Bob | `#AC5810` | medido en la portada ✅ |
| Corbata de Bob | `#DE1A11` | medido en la portada ✅ |
| Camisa de Bob | `#FCFAF1` | medido en la portada ✅ |
| Don Cangrejo (rojo) | `#F04A3E` (hoja de modelo); `#D34835` (stock art) | medido, dos fuentes ✅ (antes `#EA3941` de fans) |
| Calamardo (verde menta) | `#B6D5CA` (hoja); `#C3DDD3` (stock art) | medido, dos fuentes ✅ (antes `#54DBC2` de fans) |
| Patricio (rosa salmón) | `#FE9285` (hoja); `#F4B1B5` (stock art) | medido, dos fuentes ✅ (antes `#FF808B` de fans) |
| Plankton (verde) | `#00613B`, brillo `#6FA48C` | leído del SVG oficial ✅✅ (antes `#68A079` de fans) |
| Karen (azul) | `#5886E8` | paleta de fans ⚠️ (no se midió en la segunda pasada) |
| Logo (del SVG oficial) | `#FFF463` `#B2B618` `#919107` `#EF5240` `#EB1C22` `#B26E2D` | leído del código del vector ✅✅ (§3.3). Los de fans (`#FFF56C` `#AEAD0D` `#26B9C8` `#0457A0`, [ColorsWall](https://colorswall.com/palette/3918)) quedan sólo como contraste |
| Cielo y agua de fuera | `#289FBF` `#4BC2AB`, arena `#D0CFBA` | medido en fotograma §5.4 ✅ |
| Menú: crema, texto, título | `#E7D09C` `#51241D` `#954033` | medido §3.4 ✅ |
| Caja registradora (serie) | `#282927` | medida en fotograma §5.4 ✅ |
| Caja registradora (textura de juego) | `#427193` `#89BED7` | medido §3.4 ✅ |
| Letrero de concha | `#E4CBD6` | medido §3.4 ✅ |
| Puertas y ventanas | `#4254A4` `#3B5DB3` | medido §3.4 ✅ |
| Madera de la fachada | `#6A4B2D` | medido §3.4 ✅ |
| Tarjeta de tiempo roja (letra lila) | `#890008` / `#EF7EF2` | guía de cuadros de diálogo ✅ |

Las paletas de fans salen de [un hilo de Encyclopedia SpongeBobia](https://spongebob.fandom.com/f/p/4400000000000374215)
y [Brand Palettes](https://brandpalettes.com/spongebob-squarepants-color-codes/).

### 5.6 Texturas reales equivalentes (CC0) ✅

- Madera de la fachada y del barquito: [Weathered Planks](https://polyhaven.com/a/weathered_planks),
  [Wood Floor Deck](https://polyhaven.com/a/wood_floor_deck),
  [Wood Planks](https://polyhaven.com/a/wood_planks) (Poly Haven, CC0).
- Papel: [ambientCG Paper001](https://ambientcg.com/view?id=Paper001) a
  Paper006, CC0, 2K ✅ (API comprobada en la segunda pasada). Sirve para el
  grano de los fondos pintados. **Papel térmico** de ticket: no se
  encontró uno libre ⚠️.
- **Ojo**: la serie es **plana y pintada**. Si se usa textura real, que
  sea suave, como un fondo pintado a mano, no una foto.

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

| Dónde | Qué letra es | Fuente |
|---|---|---|
| Logo, palabra «SpongeBob» | recreada por fans como **Krabby Patty** (Seil), gratis para uso personal ⚠️ | [FontMeme](https://fontmeme.com/spongebob-squarepants-font/) |
| Logo, palabra «SquarePants» | **Las Vegas Jackpot** con la Q retocada ⚠️ | FontMeme |
| **Tarjetas de tiempo**, créditos y algunos títulos | recreada como **Some Time Later** | [1001 Fonts](https://www.1001fonts.com/some-time-later-font.html) |
| Menú «Galley Grub» | letra condensada muy gorda (no identificada) | §3.4 |
| Rótulos de *Battle for Bikini Bottom* | letra amarilla redonda con borde oscuro | §3.1 |

### 6.2 Letras libres comprobadas por mí (fontTools) ✅

Comprobé en cada archivo si trae **á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡**:

| Letra | Para qué | Licencia | Tildes, ñ, ¿ ¡ |
|---|---|---|---|
| **Some Time Later** 3.300 (Fredrick R. Brennan) | **tarjetas de tiempo** del narrador | **SIL OFL** (lo dice el propio archivo) | **todo sí** (1177 glifos). Copia en [Jordy3D.github.io](https://github.com/Jordy3D/Jordy3D.github.io), `projects/sometimelater/Some Time Later.otf`. Ojo: sus «¡» y «!» salen inclinadas, como en la serie. |
| **Anton** | el menú «Galley Grub» (condensada gorda) | OFL, Google Fonts | todo sí |
| **Luckiest Guy** | rótulos tipo logo, gordos y botones | Apache 2.0, Google Fonts | todo sí |
| **Titan One** | igual que Luckiest Guy, más redonda | OFL | todo sí |
| **Chewy** | el cartel «ORDER HERE» (trazo a mano) | Apache 2.0 | todo sí |
| Lilita One, Rammetto One, Ultra, Bangers, Sniglet, Fredoka, Patrick Hand | alternativas | OFL / Apache | todo sí |

Probé a escribir «OFERTAS Y GRATIS ¡Reclámalo! S/ 12.90» con cada una al
lado del menú. **Anton** es la que más se parece al título del menú.
**Luckiest Guy** y **Titan One**, a los rótulos de los juegos.

> [!tip] Some Time Later es la letra de la serie
> Es la de las tarjetas «A few moments later», y es **libre (OFL)**. Para
> la lámina, cualquier frase del narrador va en Some Time Later, en
> mayúsculas desiguales y en dos o tres líneas centradas.

### 6.3 Segunda pasada: lo comprobado de nuevo

- **Some Time Later, comprobada otra vez** ✅✅: el investigador de texto
  bajó el `.otf` real ([archivo](https://github.com/Jordy3D/Jordy3D.github.io/raw/master/projects/sometimelater/Some%20Time%20Later.otf))
  y con `TTFont(f).getBestCmap()` vio los 14 signos (á é í ó ú Á É Í Ó Ú
  ñ Ñ ¿ ¡) entre **1177 glifos**. La tabla `name` del archivo dice «SIL
  Open Font License, Version 1.1» (© 2016-2020 Fredrick R. Brennan).
- `1001fonts.com`, `dafont.com` y `fontmeme.com` **ya no dan 403**. Los
  datos no cambian; ahora se pueden enlazar.
- Las letras del logo (**Krabby Patty** y **Las Vegas Jackpot**) siguen
  con ⚠️: sólo las da FontMeme y no son libres para uso comercial.
- **La letra de los globos de los cómics** (*SpongeBob Comics*, United
  Plankton Pictures / Papercutz): **no la encontré** ⚠️. Sólo hay
  generadores de texto que imitan el logo. Búsquedas: «SpongeBob comics
  lettering font», «Papercutz SpongeBob lettering».

### 6.4 Una letra para cada uso (todas libres y con tildes, ñ, ¿ y ¡)

| Uso | En la serie | Letra libre | Comprobada |
|---|---|---|---|
| Logo o título | logo de la serie (Krabby Patty / Las Vegas Jackpot, no libres) | **Luckiest Guy** o **Titan One**, con los colores del SVG (`#FFF463` y contorno `#B2B618`) | ✅ fontTools |
| Globo normal | **la serie no usa globos** (§7) | no aplica en pantalla; en la lámina el texto va en un objeto del mundo (menú, cartel, ticket) con **Anton** o **Chewy** | ✅ |
| Grito | letras gordas y torcidas de los juegos («SUPER COMBO!», §3.1) | **Luckiest Guy** en mayúsculas, un poco girada | ✅ |
| Pensamiento | no hay convención propia vista en pantalla ⚠️ | la tarjeta del narrador en **Some Time Later** hace de «voz de fuera» | ✅ letra; ⚠️ convención |
| Onomatopeya | el «cha-ching» de la caja (§2.1) se oye, no se rotula ⚠️ | **Bangers** o **Luckiest Guy** | ✅ letra |
| Cartel del mundo | «ORDER HERE» a mano, «NUT SHACK» en madera (§3.6, n.º 88), menú «Galley Grub» | **Chewy** (a mano), **Anton** (menú) | ✅ |
| Interfaz de juego | rótulos amarillos redondos con borde oscuro de *BFBB* | **Titan One** o **Luckiest Guy**, amarillo con borde oscuro | ✅ |
| Subtítulos o créditos | tarjetas de tiempo y créditos | **Some Time Later** | ✅✅ |

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

**La serie no usa bocadillos.** Nadie habla en globo. El texto en
pantalla sale de **cinco sitios**, y cada uno puede ser el «cuadro» de la
lámina:

### 7.1 La tarjeta de tiempo del Narrador Francés ✅

- Pantalla completa con **tela pintada** (tiki, piñas, flores, medusas;
  §3.5) y **letras de colores** en Some Time Later.
- La lee el **Narrador Francés** con acento francés ✅
  ([Encyclopedia SpongeBobia](https://spongebob.fandom.com/wiki/French_Narrator),
  [SpongeBob Wiki](https://spongebobwiki.org/wiki/French_Narrator)).
- En latino: **«Unos momentos después…»** ✅ (clip oficial [«Unos momentos
  después... | Bob Esponja | Paramount+»](https://www.youtube.com/watch?v=Fn9BtA-rZ-w)
  y la recopilación [«Cartel De Tiempo En Bob Esponja»](https://www.youtube.com/watch?v=S_L1IF4YJgg)).
  Sale en «Amor cascarudo» (*Krusty Love*).
- **Para este canal es perfecto**: «Los gratis caducan» es una frase de
  tiempo. Ejemplo: tarjeta **«DOS DÍAS DESPUÉS…»** y debajo el juego ya
  sin regalar.

### 7.2 El menú de precios «Galley Grub» ✅

- El cartel colgado encima del puesto de pedidos. Nombre, puntos guía y
  precio (§3.4). **Es un sitio real donde se escriben precios**: ideal para
  «con el precio en soles».

### 7.3 Carteles y objetos con letras ✅

- **«ORDER HERE»** (puesto de pedidos) y **«OPEN»** (ventana).
- **La concha del letrero** con «THE KRUSTY KRAB».
- **El botón de Calamardo**: «**I Really Wish I Weren't Here Right Now**»
  (03x10 00:15:11). Un botón de uniforme con una frase: **un cuadro de
  diálogo que existe en la serie**. **Visto** en la segunda pasada: en el
  pecho, bien legible, mientras lee apoyado en la caja ([1:40](https://www.dailymotion.com/video/x3uvarj?t=100)) ✅.
- **El tablero «YOUR WORK STATION»** con casillas rotuladas (Ketchup,
  Mustard, Mayo, Patties…), visto en el *Training Video* ([1:20](https://www.dailymotion.com/video/x3uvarj?t=80)) ✅:
  un cartel con casillas, bueno para una lista de tiendas.
- **Carteles de oferta de la propia serie** ✅ vistos en la hoja
  `fondos_01.jpg`: «DAILY SPECIAL BBQ NUTS» (n.º 86, rojo con letras
  amarillas) y el cartel de madera «KOWBOY KRAB'S NUT SHACK» con
  «NUTS…… 5.00» y «KRABBY PATTY…… 1.25» (n.º 88). **Es el mejor modelo
  de cartel de precios**: madera colgada de una polea, puntos guía,
  precio a la derecha.
- **El tablón de corcho del Crustáceo** (hoja `objetos_01.jpg`, n.º 194) ✅:
  notas de colores clavadas con chinchetas. Modelo para la lámina 2.
- **La pantalla de Karen**: Karen es un ordenador; su cara es una pantalla
  ⚠️ (de memoria: una onda verde que se mueve al hablar; comprobar).
- **El ticket de la caja**: no encontré una escena con ticket impreso ⚠️.
  Es invención mía, pero pega con el objeto.

### 7.4 El narrador «de documental» ✅ subtítulo

- Abre episodios como un documental: «**Here we see Bikini Bottom, teeming
  with life, home of one of my favorite creatures, SpongeBob SquarePants.**
  Yes, of course he lives in a pineapple, you silly» (01x01 00:01:03).
- Está basado en **Jacques-Yves Cousteau**; se le ve con **traje de buzo
  antiguo y gorro rojo** ✅ (mismas dos fuentes de 7.1).
- La voz latina: §10.

### 7.5 La tarjeta de título del episodio ⚠️

- De memoria: el título sale sobre un fondo pintado con burbujas, tras
  una transición de burbuja. No lo comprobé.

### 7.6 En los videojuegos

- *Battle for Bikini Bottom*: rótulos amarillos, gordos y redondos con
  borde oscuro («SUPER COMBO!»), visto en la captura ✅.
- Cajas de diálogo de los juegos: **no pude verlas**. Game UI Database
  tiene la ficha de *Rehydrated* ([id 1490](https://www.gameuidatabase.com/gameData.php?id=1490))
  pero no abre desde aquí ⚠️. En la segunda pasada tampoco: ni en directo
  (403) ni en Wayback, que sólo guardó el armazón vacío de la web.
- **Avisos de *Rehydrated*, con el icono del botón dentro de la frase** ✅
  (segunda pasada): en el texto del juego se ve
  `<GameCmd>Press</GameCmd> <img id="R1_Button"/> <GameCmd>to travel to the Spongeball Arena</GameCmd>`
  ([The Cutting Room Floor vía Wayback](https://web.archive.org/web/20260911094445/https://tcrf.net/SpongeBob_SquarePants:_Battle_for_Bikini_Bottom_Rehydrated),
  archivo `Game.locres`). El icono va **metido en la frase**, no aparte.
  Modelo para un aviso corto: «Pulsa 🅡 para reclamarlo».

### 7.7 Cómo se traduce a una lámina fija

- **El personaje «dice» su frase en un objeto del Crustáceo**: el menú, un
  cartel, el botón del uniforme, el ticket.
- **El narrador «dice» la frase de tiempo** en una tarjeta pintada, en una
  esquina, como un fotograma aparte.
- Si hace falta que se vea quién habla: el objeto va **pegado a él** (el
  botón en su pecho; el menú encima de su cabeza).

### 7.8 Qué NO hacer con el texto

- **Nada de globo blanco**: la serie no los usa.
- Nada de letra recta de ordenador para el narrador: su letra **baila**.
- Nada de fondo liso en la tarjeta: siempre **tela pintada**.
- Nada de «·», «—» ni paréntesis (regla del dueño).

---

## 8 · Los personajes

Fuentes generales: [Wikipedia: Mr. Krabs](https://en.wikipedia.org/wiki/Mr._Krabs),
[Encyclopedia SpongeBobia: Eugene H. Krabs](https://spongebob.fandom.com/wiki/Eugene_H._Krabs),
[Wikipedia: Squidward](https://en.wikipedia.org/wiki/Squidward_Tentacles),
[Wikipedia: Plankton and Karen](https://en.wikipedia.org/wiki/Plankton_and_Karen),
[Wikipedia: SpongeBob (personaje)](https://en.wikipedia.org/wiki/SpongeBob_SquarePants_(character)).
Las frases con minuto salen del subtítulo inglés (§2).

### Don Cangrejo (Eugene H. Krabs) — el dueño del dinero, el mejor para este canal

- **Quién es**: dueño y fundador del Crustáceo Cascarudo. **Tacaño**,
  obsesionado con el dinero; **creció pobre** y de ahí le viene ✅
  ([Encyclopedia SpongeBobia](https://spongebob.fandom.com/wiki/Eugene_H._Krabs),
  [Nickelodeon Wiki](https://nickelodeon.fandom.com/wiki/Eugene_H._Krabs)).
- **Marinero y veterano de la Armada**. El vídeo de formación insinúa que
  la guerra le dejó huella ✅ (mismas fuentes; 03x10 00:13:15 «After the
  war, Krabs stayed secluded in a deep depression»).
- **Qué le importa**: el dinero y **su hija Perla** (una ballena). Por
  ella gasta ✅.
- **Con quién**: Bob Esponja (su cocinero fiel), Calamardo (su cajero, que
  lo odia), **Plankton** (su rival de toda la vida, que quiere la fórmula).
- **Su voz inglesa**: Clancy Brown ✅.
- **Cómo se presenta**: «Hello, I'm Mr. Krabs, and I like money» (01x10
  00:04:58).
- **Cómo saluda**: «**Ahoy**, SpongeBob. How goes the wieners?» (07x24
  00:07:41, *Krusty Dogs*); «Ahoy there, SpongeBob» (03x04 00:09:32).
- **Cómo celebra**: canta al dinero, «cha-ching, cha-ching,
  cha-chingaree» (04x05 00:01:24).
- **Cómo mima el dinero**: «My babies… Papa clean you up» (02x01 00:13:41).
- **Su regla de oro**: «**Everyone's money is good here.** At the Krusty
  Krab, we serves all kinds» (02x03 00:14:35, obligando a Calamardo a
  atender a Burbuja).
- **Cómo explica**: «Now, listen up, son. I've called you here on
  official Krusty Krab business» (07x06 00:12:53).
- **Cómo regaña**: con lógica tramposa: «three possibilities: you stole
  it, you stole it, or you stole it» (03x07 00:13:48).
- **Cómo habla**: de marinero: «**me** money» por «my money» (02x01
  00:07:51 y muchos más), «Here they come, **lads**» (04x05 00:01:08),
  «**boy-o**» (13x17 00:17:21), «lubbers» (02x08 00:06:00) ✅ subtítulo.
- **Su debilidad para este canal**: **lo gratis que recibe le encanta**
  («any fella who's giving away free stuff is a friend o' mine», 02x08
  00:06:00); **lo gratis que da le duele** («it's f-f-f…», 15x11 00:01:20).
- **Cuerpo**: ojos en **antenas** y **pinzas** enormes que se abren al
  gritar ✅ visto (hoja `personajes_01.jpg`, n.º 3, 39 y 40; vídeo
  [3:55](https://www.dailymotion.com/video/x3uvarj?t=235)). Que camine de
  lado con **ruido de tacones** y que olfatee el dinero con la nariz al
  aire sigue ⚠️ (de memoria).

### Bob Esponja — el protagonista, el cocinero

- **Quién es**: cocinero del Crustáceo, feliz con su trabajo. Su primera
  palabra fue «**May I take your order?**» (01x01 00:02:55) ✅.
- **Cómo se anima**: «Who's ready? **I'm ready!**» (01x01 00:03:12).
- **Cómo obedece**: «Aye aye, captain» / «Aye-aye, sir».
- **Qué le importa**: hacer Cangreburguers, sus amigos, que Don Cangrejo
  esté orgulloso. **No es el que maneja el dinero**: cuando le toca la
  caja, se lía (02x01 00:15:24).
- **Voz inglesa**: Tom Kenny, que también hace al Narrador ✅.

### Calamardo — el cajero (el más querido por los adultos)

- **Quién es**: el cajero del Crustáceo; **odia su trabajo** ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Squidward_Tentacles),
  [Great Characters Wiki](https://greatcharacters.miraheze.org/wiki/Squidward_Tentacles)).
- **Qué le importa**: el arte, **el clarinete**, la pintura, la paz ✅.
- **Miedo**: ser un fracasado; que Calamardín le vea de cajero (03x08
  00:13:52: «You're a cashier») ✅.
- **Por qué gusta**: **los adultos se ven en él**: trabajo que no quiere,
  jefe tacaño, compañero pesado ✅ ([Medium](https://jonessticky.medium.com/the-older-i-get-the-more-i-relate-to-squidward-e19b6b3081da),
  [The Odyssey](https://www.theodysseyonline.com/squidward)).
- **Cómo atiende**: seco, «**What'll it be?**» (02x03 00:14:20, en *Bubble
  Buddy*). Cuando Don Cangrejo le amenaza, lo dice bien, de mala gana:
  «May I take your order?» (02x03 00:14:50).
- **Cómo se burla del cliente**: «Now are you going to buy something or
  just stand there 'cause **there's a standing fee**» (03x10 00:14:28;
  por el contexto lo dice Calamardo desde la caja ⚠️, comprobar).
- **Cómo se queja**: «I'm getting paid overtime for this, right, Mr.
  Krabs?» (03x10 00:15:20).
- **Voz inglesa**: Rodger Bumpass ✅.
- **Cuerpo** ✅ visto: ojos medio cerrados, nariz larga caída, brazos
  cruzados o caídos, **apoyado en la caja leyendo** ([1:40](https://www.dailymotion.com/video/x3uvarj?t=100);
  hoja `personajes_01.jpg`, n.º 2).

### Patricio — el mejor amigo (el más votado en Ranker)

- **Quién es**: el mejor amigo de Bob Esponja, vive bajo una roca.
- **Sus momentos del Crustáceo**: al teléfono, «Is this the Krusty
  Krab? — **No, this is Patrick**» (02x03 00:04:25) ✅. Y en *Band Geeks*:
  «**Is mayonnaise an instrument?**» (02x15 00:15:10) ✅.
- **Qué le importa**: comer, dormir, su amigo.
- **Cuerpo** ✅ visto: panza fuera, brazos colgando, boca abierta (hoja
  `personajes_01.jpg`, n.º 8; tráiler 2025, [0:10](https://www.dailymotion.com/video/x9mmh7y?t=10)).

### Plankton y Karen — los del Balde de Carnada

- **Quién es**: dueño del **Balde de Carnada** (enfrente del Crustáceo ✅, §5.3).
  Quiere **robar la fórmula secreta**. Diminuto, verde, **un solo ojo** ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Plankton_and_Karen)).
- **Karen**: su esposa, **un ordenador**. En *Plankton: La película*
  (2025) se harta y quiere conquistar el mundo sola ✅.
- **Cómo habla**: «That secret formula **will be mine**» (14x01 00:09:35);
  «Karen, you're a genius» (14x04 00:07:00).
- **Para este canal**: es **la tienda sin clientes**, la mala oferta. El
  meme «Krusty Krab vs. Chum Bucket» lo usa así (§14).
- **Voces inglesas**: Mr. Lawrence (Plankton), Jill Talley (Karen) ✅.

### El Narrador Francés

- Buzo con **acento francés** que presenta los episodios como un
  documental y **lee las tarjetas de tiempo** ✅
  ([Encyclopedia SpongeBobia](https://spongebob.fandom.com/wiki/French_Narrator),
  [SpongeBob Wiki](https://spongebobwiki.org/wiki/French_Narrator)).
- Basado en **Jacques-Yves Cousteau**; en el guion del piloto lo llamaban
  «Jacques Cousteau». Voz inglesa: **Tom Kenny** ✅.
- Cuando se le ve: **traje de buzo antiguo y gorro rojo** ✅.
- **Cómo habla**: calmado, admirado, con humor: «Yes, of course he lives
  in a pineapple, you silly» (01x01 00:01:11).

### Su cara en cada emoción (segunda pasada, vista en vídeo)

Dos tipos de minuto. Los que llevan enlace son de los clips de Dailymotion
del investigador de vídeo ✅. Los que **no llevan enlace** los vio el
investigador de voz en otras hojas de contacto: *Born Again Krabs* entero,
*La Torta o la Vida* (*Dying for Pie*) y el tráiler de *Sponge Out of
Water* (2015). Están vistos, pero **la copia no está enlazada** ⚠️ y el
minuto puede no coincidir con otra copia.

| | Alegría | Rabia | Tristeza | Miedo | Vergüenza |
|---|---|---|---|---|---|
| **Don Cangrejo** | brazos abiertos bajo «LIVE FOR TODAY», [3:12](https://www.dailymotion.com/video/x3uhkek?t=192) ✅; sonrisa ancha regalando comida y abrazando a Calamardo (*Born Again Krabs* entero, 6:33-7:17) | grita «THE MONEY IS ALWAYS RIGHT!», [3:55](https://www.dailymotion.com/video/x3uvarj?t=235) ✅; guantes de boxeo, [0:39](https://www.dailymotion.com/video/x9mmh7y?t=39) ✅; su fantasma verde furioso, dientes afilados (8:50-9:40) | ❌ no se encontró | la factura de $10 000, pinzas temblando, [3:47](https://www.dailymotion.com/video/x3uhkek?t=227) ✅; temblando en el congelador, antenas rígidas (0:30-0:50) | ❌ no se encontró |
| **Calamardo** | sonrisa avergonzada abrazado a Bob con el libro «Friends 4-Ever» (*Dying for Pie*, 0:51-1:00) | fastidio, ojos entrecerrados, brazos caídos (*Born Again Krabs*, 6:39-7:15); desgana en la caja, [1:40](https://www.dailymotion.com/video/x3uvarj?t=100) ✅ | ojos rojos, grito mudo, temblando (*Dying for Pie*, 0:36-0:39) | ❌ no se encontró | la misma sonrisa avergonzada del final de *Dying for Pie* (0:51-1:00) |
| **Bob Esponja** | sale de la piña sonriendo, opening [0:14](https://www.dailymotion.com/video/x8hj84s?t=14) ✅ | ❌ no se encontró | sentado, cabizbajo, junto a un ladrillo, [0:33](https://www.dailymotion.com/video/x9mmh7y?t=33) ✅ | grito a pantalla completa, [0:04](https://www.dailymotion.com/video/x9mmh7y?t=4) ✅; susto con lágrima y boca en «o» (*Born Again Krabs*, 9:50) | ❌ no se encontró |
| **Patricio** | codo a codo con Bob, [0:57](https://www.dailymotion.com/video/x9mmh7y?t=57) ✅; puños en alto, gritando (tráiler 2015, 2:10-2:16) | cejas muy abajo, boca apretada, señalando (tráiler 2015, 1:15-1:16); asco, boca torcida (1:16) | ❌ no se encontró | boca abierta de golpe, [0:10](https://www.dailymotion.com/video/x9mmh7y?t=10) ✅ | ❌ no se encontró |
| **Plankton** | ❌ no se encontró en vídeo (sí en la hoja: n.º 9, risa malvada) | ❌ no se encontró en vídeo | ❌ | preocupado con su mascota descontrolada, [0:22](https://www.dailymotion.com/video/x6i3rnb?t=22) ✅; la cetafobia (*One Coarse Meal*) sólo por texto de la wiki ⚠️ | ❌ |

### Arcos, momentos clave y dinámicas

- **Don Cangrejo no cambia** (es de *sitcom*: siempre vuelve a la
  tacañería). El episodio que mejor lo explica es ***Born Again Krabs***:
  cree que ha muerto, se vuelve generoso y feliz, y al volver a ser él una
  cuenta de $10 000 lo destroza. Es **el** episodio para entender por qué
  «dar gratis» le cuesta un mundo ✅ visto.
- **Con quién**: se ríe con el ruido de las monedas, no con chistes;
  **discute** con Plankton (rivales de toda la vida); **regaña** a
  Calamardo por vago; trata a Bob **como a un hijo torpe pero querido** ✅
  ([Encyclopedia SpongeBobia](https://spongebob.fandom.com/wiki/Eugene_H._Krabs)).
- **Calamardo y Bob, odio y cariño**: en *La Torta o la Vida* cree que Bob
  va a morir por su culpa, pasa del alivio secreto al remordimiento, y
  acaban riéndose juntos ✅ visto ([Encyclopedia SpongeBobia: Dying for Pie](https://spongebob.fandom.com/wiki/Dying_for_Pie)).
  Es el episodio que más citan los fans para explicar que **sí lo quiere**.
- **Dinámica para una lámina en grupo** ✅ (patrón visto en las hojas):
  Don Cangrejo cuenta el dinero → Calamardo pone los ojos en blanco → Bob
  sonríe sin pillar el sarcasmo → Patricio pregunta algo fuera de lugar.
- **Qué transmite cada uno**: Don Cangrejo, el jefe tacaño que todos
  hemos tenido; Calamardo, el adulto atrapado en un trabajo que odia;
  Patricio, el amigo que no juzga; Bob, la alegría sin freno (§21).

---

## 9 · ¿Quién es el más querido?

- **No hay encuesta oficial** de Nickelodeon ni de Latinoamérica. Busqué
  en español e inglés y **no la encontré** (en la segunda pasada tampoco).
- **Corrección (segunda pasada): sí hay una votación grande**, aunque no es
  de Nickelodeon. **The Ringer** hizo en 2021 el «Best Nickelodeon
  Character Bracket»: **2,5 millones de votos** en 63 rondas entre todos
  los personajes de Nickelodeon. **Ganó Bob Esponja** en la final, contra
  Tommy Pickles (*Rugrats*) ✅ ([The Ringer](https://theringer.com/platform/amp/tv/2021/8/14/22624731/best-nickelodeon-character-bracket-final-results-spongebob-squarepants)).
- **Kids' Choice Awards, Mejor Caricatura**: la serie ganó **17 años
  seguidos** hasta 2025 (22 veces desde 2003; sólo perdió en 2008 contra
  *Avatar*) ✅ ([Animation Magazine 2025](https://www.animationmagazine.net/2025/06/inside-out-2-spongebob-squarepants-jack-black-win-big-at-2025-nickelodeon-kids-choice-awards/),
  [Wikipedia](https://en.wikipedia.org/wiki/Kids%27_Choice_Award_for_Favorite_Cartoon)).
  No separa por personaje.
- En 2001, en el episodio *Shanghaied*, el público votó quién se quedaba
  con un deseo y ganó **Bob Esponja** ⚠️ (una fuente, sin la nota de
  prensa original).
- **Ranker** (votos de fans, más de 4000): 1.º **Patricio**, 2.º
  **Calamardo**, 3.º Bob Esponja ✅ ([Ranker](https://www.ranker.com/list/the-best-spongebob-squarepants-character/tvs-frank)).
- **Calamardo** es el que más memes latinos tiene: «Calamardo guapo» y
  el de «Solo un bocado», que según la wiki latina **sólo existe en redes
  latinas** ⚠️ ([Bob Esponja Wiki: Lista de memes](https://bobesponja.fandom.com/wiki/Lista_de_memes),
  [psicocode](https://psicocode.com/cultura/calamardo-guapo-meme/)).
- **Don Cangrejo** tiene su propia línea de recopilaciones oficiales en
  YouTube: «RODANDO sobre dinero durante 60 minutos», «30 minutos de Don
  Cangrejo haciendo CUALQUIER COSA por dinero», «Los momentos MÁS TACAÑOS
  de Don Cangrejo» (canal **Bob Esponja en Español**, §12) ✅.

**Conclusión para la lámina**: para #ofertas-y-gratis **manda Don
Cangrejo** (el dinero es suyo). **Calamardo** es el secundario más querido
por adultos y **es el cajero**: la caja es literalmente su sitio.
Patricio, el más votado, sirve de cliente.

---

## 10 · Doblaje latino

**Estudio**: **Etcétera Group, Caracas (Venezuela)**, desde finales de
1999 ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Bob_Esponja),
[Bob Esponja Wiki](https://bobesponja.fandom.com/wiki/Doblaje)). La
**temporada 15** fue la última en la sede venezolana, que **cerró el 28 de
febrero de 2025**. La **16** pasó a **DAT Doblaje, Audio y Traducción
(México)**; el reparto principal siguió grabando desde Venezuela ✅
(Doblaje Wiki; [ANMTV](https://www.anmtvla.com/2024/04/bob-esponja-olin-garces-se-convierte-en.html)
confirma que DAT graba a Don Cangrejo desde México).

| Personaje | Voz latina | Cuándo | Fuentes |
|---|---|---|---|
| Bob Esponja | **Luis Carreño** | desde la 2.ª temporada (2000) hasta hoy | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Luis_Carre%C3%B1o), [ANMTV 2025](https://www.anmtvla.com/2025/07/bob-esponja-en-busca-de-los-pantalones.html), [Xataka](https://www.xataka.com.mx/videojuegos/bob-esponja-the-cosmic-shake-se-actualiza-gratis-incluye-doblaje-latino-actores-serie-television) |
| Bob Esponja (1.ª temporada) | Kaihiamal Martínez (habla, hasta el ep. 17); Luis Miguel Pérez (canto) | 1999 | ✅ segunda pasada: [ficha de la serie](https://doblaje.fandom.com/es/wiki/Bob_Esponja), [Kaihiamal Martínez](https://doblaje.fandom.com/es/wiki/Kaihiamal_Mart%C3%ADnez) y [Noroeste](https://www.noroeste.com.mx/entretenimiento/gente/visita-mazatlan-kai-martinez-la-voz-oficial-de-la-primera-temporada-de-bob-esponja-HF2070595). En el especial 59 también le pone voz Luis Lugo |
| Patricio | **Alfonso Soto** | desde la 4.ª temporada | ✅ Doblaje Wiki, ANMTV 2025, [VGEzone](https://vgezone.com/cinetv/noticias/voces-bob-esponja-al-rescate-doblaje-latino/) |
| Calamardo | **Renzo Jiménez** | desde 1999, **todas** las temporadas | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Calamardo_Tent%C3%A1culos), ANMTV 2025, VGEzone |
| Don Cangrejo | **Luis Pérez Pons** | **corregido**: temporadas 1-5, y de la 9 (ep. 190) a la 13. **Murió el 24 de octubre de 2023**, a los 72 años | ✅ [El Financiero](https://www.elfinanciero.com.mx/espectaculos/2023/10/24/muere-luis-perez-pons-actor-de-don-cangrejo-en-bob-esponja-a-los-72-anos/), [El Tiempo](https://www.eltiempo.com/cultura/cine-y-tv/murio-luis-perez-pons-la-iconica-voz-en-espanol-latino-de-don-cangrejo-en-bob-esponja-819537), Doblaje Wiki |
| Don Cangrejo | **Carlos Vitale** | **nuevo**: temporadas 6 a 9 (ep. 102-189); su último episodio se estrenó el 29-ago-2015 | ✅ [ficha de la serie](https://doblaje.fandom.com/es/wiki/Bob_Esponja), [Carlos Vitale](https://doblaje.fandom.com/es/wiki/Carlos_Vitale) («segunda voz de Don Cangrejo, hasta la 9.ª temporada») y [Encyclopedia SpongeBobia](https://spongebob.fandom.com/wiki/Eugene_H._Krabs) (sección «International») |
| Don Cangrejo | Walter Véliz | un solo episodio: temp. 7, ep. 148 («El Ataque de los Welk») | ⚠️ sólo la ficha de la serie |
| Don Cangrejo | **Olin Garcés** (México) | desde la 14.ª temporada (2024) | ✅ [ANMTV](https://www.anmtvla.com/2024/04/bob-esponja-olin-garces-se-convierte-en.html), [SuperGeek](https://www.supergeek.cl/noticias/cultura-pop/escuchen-a-la-nueva-voz-latina-de-don-cangrejo-en-bob-esponja/2024-04-16/211945.html), [TikTok de Luis Carreño](https://www.tiktok.com/@luiscarrenovoz/video/7358633626436750635) |
| Plankton | **Ángel Mujica** | desde la 9.ª temporada | ✅ Doblaje Wiki, ANMTV 2025 |
| Plankton (antes) | **Óscar Zuloaga** (temp. 1-2, ep. 3-28), **Luis Miguel Pérez** (temp. 2-8, desde el ep. 34), **Héctor Indriago** (sólo el ep. 183); Ángel Mujica desde el ep. 184 | temporadas 1-9 | ✅ segunda pasada: [ficha de la serie](https://doblaje.fandom.com/es/wiki/Bob_Esponja) y el [TikTok](https://www.tiktok.com/@nickvan029/video/7381272630441053446) de antes |
| Arenita | **Lileana Chacón** | desde la 6.ª temporada | ✅ Doblaje Wiki, ANMTV 2025 |
| Karen (hoy) | **Paulina Monfort** (México) | **nuevo**: desde el ep. 327A, temporada 16 (2025) | ✅ [ficha de la serie](https://doblaje.fandom.com/es/wiki/Bob_Esponja), [Paulina Monfort](https://doblaje.fandom.com/es/wiki/Paulina_Monfort) |
| Karen (antes) | **Melanie Henríquez** (temp. 5-9, hasta el ep. 186); María José Estévez (temp. 8, ep. 170-177); Gabriela Belén (temp. 9, ep. 198-203); **Sixnalie Villalba** (Chile, temp. 10-16, ep. 230-325) | 2007-2025 | ✅ ficha de la serie. Melanie Henríquez **se retiró en julio de 2015 al mudarse a Tenerife** y volvió al doblaje en 2022 desde España ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Melanie_Henr%C3%ADquez), [entrevista en El Retake](https://www.tiktok.com/@elretake/video/7539562416858762518)). Mariangny Álvarez también pasó por Karen en ese cambio ⚠️ una fuente |
| **Narrador Francés** y rótulos | **Orlando Noguera** | 1.ª temporada | ✅ Doblaje Wiki, [TikTok de Luis Carreño](https://www.tiktok.com/@luiscarrenovoz/video/7473616154968296734) |
| **Narrador Francés** y rótulos | **Juan Guzmán** | desde la 2.ª temporada | ✅ Doblaje Wiki ([Juan Guzmán](https://doblaje.fandom.com/es/wiki/Juan_Guzm%C3%A1n), [Narrador francés](https://doblaje.fandom.com/es/wiki/Narrador_franc%C3%A9s)); en la segunda pasada, también en la [ficha de la serie](https://doblaje.fandom.com/es/wiki/Bob_Esponja) (tres páginas) |

- En la película de 2025 **vuelven todos los actuales**: Carreño, Soto,
  Chacón, Jiménez, **Garcés** y Mujica; doblaje en México con
  **Dvinxi Studios** (Venezuela) ✅ (Doblaje Wiki, ANMTV).
- El juego **The Cosmic Shake** recibió **doblaje latino gratis** con los
  actores de la serie ✅ ([Xataka](https://www.xataka.com.mx/videojuegos/bob-esponja-the-cosmic-shake-se-actualiza-gratis-incluye-doblaje-latino-actores-serie-television),
  [Colectiva Xbox](https://www.colectivaxbox.com/2023/03/bob-esponja-cosmic-shake-ahora-tiene.html)).

### Nombres latinos que hay que usar ✅

- **Crustáceo Cascarudo** (Krusty Krab), **Cangreburguer** (Krabby Patty),
  **Balde de Carnada** (Chum Bucket; en la 1.ª temporada «Balde de
  Bocados»), **Fondo de Bikini**, **Don Cangrejo**, **Calamardo**,
  **Patricio**, **Arenita** (Doblaje Wiki; [Facebook oficial de Bob Esponja](https://www.facebook.com/bobesponja/videos/el-crust%C3%A1ceo-cascarudo-y-el-balde-de-carnada-combinados-escena-bob-esponja/644639737397637/)).
- Episodios: «**Choque Cultural**» (*Culture Shock*), «**El Día Libre de
  Calamardo**» (*Squid's Day Off*), «**Video de Entrenamiento del Crustáceo
  Cascarudo**», «**Amor Cascarudo**» (*Krusty Love*), «**Una Cangreburguer
  inmunda**» (*Nasty Patty*) ✅ ([Bob Esponja Wiki](https://bobesponja.fandom.com/wiki/Video_de_Entrenamiento_del_Crust%C3%A1ceo_Cascarudo),
  [Apple TV](https://tv.apple.com/mx/episode/turno-de-ultratumba--amor-cascarudo/umc.cmc.2ypx5u7r72vl9i68qgb65hss6?showId=umc.cmc.4b0em143bn491l5iwi12nj1vu),
  [HBO Max](https://www.hbomax.com/bo/es/shows/bob-esponja/s2/6237f381-2ab7-41ca-8e73-e177033de02f/e1-tus-cordones-estan-desatados-el-dia-libre-de-calamardo/2dcb2424-5dd6-4c87-989a-164cd70a0c88)).

### Frases del doblaje latino

| Frase | Quién | Estado |
|---|---|---|
| «**Hola, me gusta el dinero**» | Don Cangrejo («Choque Cultural») | ✅ como meme ([TikTok](https://www.tiktok.com/discover/hola-me-gusta-el-dinero-don-cangrejo?lang=en), [Facebook](https://www.facebook.com/turrilandia/posts/hola-me-gusta-el-dinero-spongebob-cangrejo-doncangrejomegusta-dinero-money-quinc/5106755876083172/)). La línea exacta del episodio ⚠️ |
| «**Unos momentos después…**» | Narrador | ✅ (clip oficial de Paramount+) |
| «**¡Oh, por todos mis tentáculos!**» | Calamardo («Pizza a domicilio») | ✅ Doblaje Wiki y guía de cuadros |
| «¿Hola, es el Crustáceo Cascarudo? — No, soy Patricio» | Patricio | ⚠️ los resultados dicen «soy» y «habla»; escucharlo |
| «Qué mal que Bob Esponja no está aquí para disfrutar que Bob Esponja no está aquí» | Calamardo | ⚠️ una fuente |
| «echar el muerto» (venezolanismo) | «Una Cangreburguer inmunda» | ✅ Doblaje Wiki y guía |

**No encontré** cómo dice Don Cangrejo en latino «free» en *Delivery of
DOOM* ni en *Christmas Who*. Las frases de la lámina basadas en esas
escenas son **traducción mía** y hay que decirlo así.

**Segunda pasada**:
- Tercera fuente del estudio: la ficha de la **Fandub Database**
  ([fandubdb](https://fandubdb.fandom.com/wiki/Bob_Esponja_(Latin_American_Spanish,_fictionalized)))
  da Etcétera Group (Caracas y Miami) y, desde la temporada 14, **DAT** para
  las líneas de **Olin Garcés** ✅. Pese al nombre, esa ficha documenta el
  doblaje **oficial**.
- Clips en latino **vistos**: *Se busca ayuda* entero ([Dailymotion x51sid2](https://www.dailymotion.com/video/x51sid2))
  y el promocional oficial de **Nickelodeon Latinoamérica** «La Mascota de
  Plankton», que cierra con el rótulo «Encuentra Bob Esponja más en Nick»
  ([0:48](https://www.dailymotion.com/video/x6i3rnb?t=48)) ✅ visto.
- **No se transcribió** ninguna frase nueva del doblaje con su minuto: los
  clips se miraron por la imagen, no se pasaron por `voz.py` ⚠️. Las
  frases latinas siguen siendo las de la tabla de arriba. Queda para oír en
  persona (§28).

---

## 11 · Música

- **El tema de entrada**: el capitán pregunta y los niños contestan.
  Inglés: «Are you ready, kids? — Aye aye, captain» (01x01 00:00:02) ✅
  subtítulo. En latino: «¿Están listos, chicos? — ¡Sí, capitán!» y «Vive
  en una piña debajo del mar» ⚠️ (letras de fans: [letras.com](https://www.letras.com/bob-esponja/1679384/),
  [musica.com](https://www.musica.com/letras.asp?letra=1538752)).
- **La música de fondo** es de **guitarra hawaiana (steel guitar) y
  ukelele**. La tocan **Jeremy Wakefield** (steel) y **Sage Guyton**
  (ukelele), del grupo The Lucky Stars ✅ ([Encyclopedia SpongeBobia](https://spongebob.fandom.com/wiki/Jeremy_Wakefield),
  [blog spongebobsoundtrack](https://spongebobsoundtrack.tumblr.com/post/635079443507986432/sage-guyton-jeremy-wakefield-grass-skirt-chase)).
  Ambiente: **tropical, perezoso, cálido**.
- **«Grass Skirt Chase»** (Guyton y Wakefield): la música de
  **persecución**, rápida ✅. Es la de **«¡corre, que se acaba!»**: encaja
  con «los gratis caducan».
- **«Hawaiian Link»** (Richard Myhill), de la biblioteca APM ✅ (mismas
  fuentes).
- **Canciones de Don Cangrejo sobre el dinero** ✅ subtítulo:
  - «Cha-ching, cha-ching, cha-chingaree» (04x05 00:01:24).
  - «Counting me money, money sweeter than honey» (02x20 00:01:03).
- Para un vídeo o GIF del canal: el **«cha-ching»** de la caja.

**El opening, mirado plano a plano (segunda pasada)** ✅ visto: 42 s, 19
planos ([Dailymotion x8hj84s](https://www.dailymotion.com/video/x8hj84s),
versión original en inglés):

| Minuto | Plano | Letra |
|---|---|---|
| [0:06](https://www.dailymotion.com/video/x8hj84s?t=6) | cortina negra y **retrato enmarcado del capitán pirata** | «Are you ready, kids?» |
| 0:11 | agua con burbujas | «Aye, aye, Captain!» |
| [0:14](https://www.dailymotion.com/video/x8hj84s?t=14) | Bob sale de su piña | «Who lives in a pineapple…?» |
| [0:16](https://www.dailymotion.com/video/x8hj84s?t=16) | salpicón en la bañera y primer plano sonriendo | «SpongeBob SquarePants!» |
| [0:22](https://www.dailymotion.com/video/x8hj84s?t=22) | **título «SpongeBob SquarePants»** en letras de colores tipo alga sobre violeta | el coro cantado |
| [0:29](https://www.dailymotion.com/video/x8hj84s?t=29) | pez, algas, Bob baila y da golpes de kárate | los golpes rápidos del ukelele |
| [0:38](https://www.dailymotion.com/video/x8hj84s?t=38) | bumper de Nickelodeon | — |
| [0:41](https://www.dailymotion.com/video/x8hj84s?t=41) | «created by Stephen Hillenburg» | — |

- **No hay ending cantado** ✅ visto: los créditos van sobre un fragmento
  instrumental corto, la cartela amarilla con flores de los «Background
  Painters» y el logo garabateado de United Plankton Pictures ([0:34](https://www.dailymotion.com/video/x3v1puo?t=34)).
  No aplica un «ending» musical.
- La letra latina del opening sigue ⚠️ (sólo letras de fans): el opening
  visto es el inglés.

---

## 12 · Vídeos

YouTube no abre desde aquí (en la segunda pasada dio **429**). Los
minutos de episodios están en §2; los de clips vistos, en §2.4 y abajo.

**Tráiler oficial doblado de «Bob Esponja: En busca de los pantalones
cuadrados»** (2025), visto entero en la segunda pasada: 63 s, 31 planos
([Dailymotion, canal sensacinemx](https://www.dailymotion.com/video/x9mmh7y)) ✅:

| Minuto | Qué se ve | Pose |
|---|---|---|
| [0:04](https://www.dailymotion.com/video/x9mmh7y?t=4) | tarjetas «ESTE AÑO / ALGO GRANDE / LLEGA A LOS CINES» y **Bob gritando** a pantalla completa | urgencia |
| [0:10](https://www.dailymotion.com/video/x9mmh7y?t=10) | **Patricio** abre la boca de golpe | sorpresa |
| [0:13](https://www.dailymotion.com/video/x9mmh7y?t=13) | todo el reparto corre en un interior de madera | «todos a por la oferta» |
| [0:31](https://www.dailymotion.com/video/x9mmh7y?t=31) | Don Cangrejo y Calamardo asustados ante un monstruo verde | miedo |
| [0:33](https://www.dailymotion.com/video/x9mmh7y?t=33) | Bob sentado, cabizbajo, junto a un ladrillo | pensar, desánimo |
| [0:39](https://www.dailymotion.com/video/x9mmh7y?t=39) | **Don Cangrejo con guantes de boxeo, furioso** | regañar |
| [0:49](https://www.dailymotion.com/video/x9mmh7y?t=49) | logo «BOB ESPONJA — En busca de los pantalones cuadrados» | — |
| [0:57](https://www.dailymotion.com/video/x9mmh7y?t=57) | **Bob y Patricio codo a codo**, listos | animar |
| [0:59](https://www.dailymotion.com/video/x9mmh7y?t=59) | tarjeta final **«AGÁRRATE LOS PANTALONES»**, logos de Nickelodeon y Paramount | — |

Es **CGI 3D**, más saturado y con luz de estudio: la franquicia tiene hoy
**dos estilos a la vez** (2D en la serie, 3D en el cine; §18).

**Clip oficial de Nickelodeon Latinoamérica**, «La Mascota de Plankton»
([Dailymotion x6i3rnb](https://www.dailymotion.com/video/x6i3rnb)), 17
planos ✅ visto. Poses de Plankton en §15.

**No encontré** tráileres de temporada en Dailymotion (sólo de las
películas de 2015, 2020 y 2025) ⚠️.

**Canal oficial «Bob Esponja en Español»**
([@bobesponjaespanol](https://www.youtube.com/@bobesponjaespanol)) ✅:
- [«Don Cangrejo RODANDO sobre dinero durante 60 minutos»](https://www.youtube.com/watch?v=YhtaF9O7JRg)
- [«30 minutos de Don Cangrejo haciendo CUALQUIER COSA por dinero»](https://www.youtube.com/watch?v=IX-8vv-MeoE)
- [«Los momentos MÁS TACAÑOS de Don Cangrejo»](https://www.youtube.com/watch?v=3bgXR9SpJ3M)
- [«Cada empleado del CRUSTÁCEO CASCARUDO»](https://www.youtube.com/watch?v=4R1IJXr6NSQ) (Nickelodeon en Español)
- [«Cada Momento del Crustáceo Cascarudo en NUEVOS Episodios»](https://www.youtube.com/watch?v=EN6lzRFAANQ)
- Lista [«El Crustáceo Cascarudo»](https://www.youtube.com/playlist?list=PLqvQQ3sEnukdmVfO_uHG-aArmQaiKM7TT)
- [«Unos momentos después... | Bob Esponja | Paramount+»](https://www.youtube.com/watch?v=Fn9BtA-rZ-w)
- Tráiler doblado de [«En busca de los pantalones cuadrados»](https://www.youtube.com/watch?v=DC0DLZjUmLQ)

**TikTok**:
- Cuenta de **Luis Carreño** (@luiscarrenovoz): [«La moneda de Don
  Cangrejo #bobesponja25anos»](https://www.tiktok.com/@luiscarrenovoz/video/7377555868155530538?lang=es),
  [«Orlando Noguera: Primer Narrador Francés»](https://www.tiktok.com/@luiscarrenovoz/video/7473616154968296734),
  [bienvenida a Olin Garcés](https://www.tiktok.com/@luiscarrenovoz/video/7358633626436750635) ✅.
- **Paramount+ México** usa a Bob y Calamardo en tendencias de audio
  («pipsssash», [vídeo](https://www.tiktok.com/@paramountplusmx/video/7481357691202325782)) ✅.
- Tendencias de fans en 2026: Calamardo bailando, «crecer es volverse
  Calamardo» ⚠️ (sólo páginas de búsqueda de TikTok).

---

## 13 · Videojuegos de la franquicia

| Juego | Año | Dato útil | Estado |
|---|---|---|---|
| **Bob Esponja: Titanes de la Marea** (*Titans of the Tide*) | 18 nov 2025 (Switch: 12 oct 2026) | Purple Lamp y THQ Nordic. **Está en Steam y en GOG**. En Steam Latinoamérica se llama «Bob Esponja: **Titanes de la Marea**» ([app 2479650](https://store.steampowered.com/app/2479650/SpongeBob_SquarePants_Titans_of_the_Tide/?l=latam)); ya tuvo rebajas del **40 %** y del **33 %**. | ✅ [Wikipedia](https://en.wikipedia.org/wiki/SpongeBob_SquarePants:_Titans_of_the_Tide), [THQ Nordic](https://thqnordic.com/news/spongebob-squarepants-titans-of-the-tide-demo-available-on-steam-and-consoles), Steam |
| *The Cosmic Shake* | 2023 | Purple Lamp. **Doblaje latino gratis** por parche. | ✅ |
| *Battle for Bikini Bottom – Rehydrated* | 2020 | Remake. En Steam ([app 969990](https://store.steampowered.com/app/969990/SpongeBob_SquarePants_Battle_for_Bikini_Bottom__Rehydrated/)). **Segunda pasada**: TCRF leído por [Wayback](https://web.archive.org/web/20260911094445/https://tcrf.net/SpongeBob_SquarePants:_Battle_for_Bikini_Bottom_Rehydrated). Corre en **Unreal Engine** (rutas `Engine/Content/SlateDebug/…` y archivos `Game.locres`); nombre interno del proyecto, **«Pineapple»** ⚠️ una fuente. Avisos con el icono del botón dentro de la frase (§7.6). Game UI Database sigue sin abrir. | ✅ existe; interfaz a medias ⚠️ |
| *Battle for Bikini Bottom* | 2003 | Rótulos amarillos redondos (§3.1). | ✅ visto |
| *SpongeBob: Krusty Cook-Off* | móvil | Tilting Point. **Llevas el Crustáceo**: sirves clientes y ganas **monedas de concha**. Gratis con compras dentro. Su interfaz la hizo [PUNCHev Group](https://punchev.com/cases/spongebob-krusty-cook-off-contributing-to-the-magic-of-deep-sea-cooking) y la revisó [Christopher Furniss](https://cargocollective.com/chrisfurniss/filter/ui/Spongebob-Squarepants-Krusty-Cookoff); no se pudieron ver sus pantallas ⚠️. | ✅ [Tilting Point](https://www.tiltingpoint.com/games/crusty_game), [App Store](https://apps.apple.com/us/app/spongebob-krusty-cook-off/id1433784188) |
| *Lights, Camera, Pants!* | 2005 | Minijuego de **cocina del Crustáceo con reloj** (§3.1). | ✅ visto |
| **Bob Esponja: El juego de Patricio Estrella** | 2024 | PHL Collective. Capturas 1920×1080 de Steam ([app 2322380](https://store.steampowered.com/app/2322380)) vistas en la segunda pasada: la piña y la roca en 3D **conservan el contorno negro grueso** (*toon shading* con línea); **nubes-flor** como líneas sueltas sin relleno; ventanas redondas de **portillo con remaches**; *Glove World!* muy saturado (magenta, amarillo canario, cian). | ✅ visto |
| *Nickelodeon All-Star Brawl 2* | 2023-2024 | Juego de peleas. Bob y Patricio desde el 1; en el 2, **Calamardo**, **Plankton** (con Karen en su traje robótico) y **Don Cangrejo** (DLC, 2024). Render en la hoja de personajes, n.º 16. | ✅ [Nintendo Life](https://www.nintendolife.com/guides/nickelodeon-all-star-brawl-2-character-roster-every-new-and-returning-fighter), [wiki del juego](https://nickelodeon-allstar-brawl.fandom.com/wiki/SpongeBob_(NASB_2)) |

> [!tip] Un ejemplo de oferta que es de la propia serie
> **Titanes de la Marea** se vende en **Steam y GOG**, dos de las tres
> tiendas del canal, y ya ha estado rebajado. Es el ejemplo perfecto
> para la lámina: «Bob Esponja: Titanes de la Marea, **-40 %**». El precio
> en soles hay que copiarlo de Steam Perú el día que se haga ⚠️.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### Lo que todos reconocen

- **«Krusty Krab vs. Chum Bucket»** ✅ ([Know Your Meme](https://knowyourmeme.com/memes/krusty-krab-vs-chum-bucket)):
  se ponen **dos cosas** en los letreros; la buena en el Crustáceo, lleno
  de gente, y la mala en el Balde, vacío. Nació en 2016 y explotó en
  **2018 con PS4 contra Xbox**. **Es un meme de videojuegos**: sirve para
  «oferta contra precio completo».
- **«Hola, me gusta el dinero»** (Don Cangrejo) ✅.
- **«Unos momentos después…»**: las tarjetas se usan como plantilla de
  meme ✅ ([TikTok](https://www.tiktok.com/@jorgek2k/video/7062358221817941254),
  [YouTube](https://www.youtube.com/watch?v=s4h4K7abhNA)).
- **Calamardo guapo** ✅ ([Bob Esponja Wiki](https://bobesponja.fandom.com/wiki/Las_Dos_Caras_de_Calamardo)).
- **«¿Es el Crustáceo Cascarudo? — No, soy Patricio»** ✅ en inglés
  (02x03 00:04:25); latino ⚠️.
- **«Is mayonnaise an instrument?»** (02x15 00:15:10) ✅.
- Otros memes muy conocidos, **de memoria** ⚠️: Don Cangrejo borroso y
  confundido, Calamardo triste en la ventana.
- **Confirmados en la segunda pasada** con la [Lista de memes de la Bob
  Esponja Wiki](https://bobesponja.fandom.com/api.php?action=parse&format=json&prop=wikitext&page=Lista_de_memes)
  (cita episodio y año) ✅:
  - **«¡Máxima Potencia!»**: del **Vídeo de Entrenamiento del Crustáceo
    Cascarudo**. Plankton huye montado en una Cangreburguer: «¡No cuando
    cambio a máxima velocidad!». Lo siguen usando creadores como SMG4. **Es
    el meme más pegado al canal**: sale de un vídeo institucional del
    Crustáceo.
  - **Patricio sorprendido**: fotograma de la película de 2004, boca
    abierta. Nickelodeon lo reutiliza en juegos (*Rehydrated*,
    *Nickelodeon Lanes*) y en un juguete.
  - **«¡No! ¡Es Patricio!»**: de «Perdedor Rosado» (*Big Pink Loser*); la
    wiki lo compara con «¡Esto es Esparta!».
  - **Bob Esponja Prehistórico** («Spongegar»): de *SB-129*; meme desde
    mayo de 2016; hay un huevo de pascua suyo como pintura rupestre en
    *Rehydrated*.
  - **Bob Esponja emo**: dibujo de fan (DeviantArt, 2007) en una página del
    libro oficial *I Ripped My Pants!*; viral en 2008-2009.
  - **Imaginación** (arcoíris con las manos): Bob se lo explica a
    Calamardo; plantilla para «explicar algo mágico».
  - **Calamardo guapo**, **«Hola, me gusta el dinero»** y **«¿La mayonesa
    es un instrumento?»** tienen entrada propia.
- **Bob Esponja burlón** (mayúsculas alternas, «Mocking SpongeBob»)
  **no está** en la lista latina ⚠️: es un meme global, de una sola fuente
  de memoria.

### Qué NO hacer (lo que un fan notaría)

- **Don Cangrejo regalando contento sin motivo.** Él **ama recibir** gratis
  y **odia dar** gratis. En la lámina, lo gratis lo regalan **las tiendas**
  y él corre a **reclamarlo**. Así sí es él.
- **Globos de cómic blancos**: la serie no los usa (§7).
- **Calamardo sonriendo y amable en la caja**: siempre aburrido o
  harto. Si sonríe, que sea de burla.
- **Nombres de España** en vez de los latinos ⚠️ (de memoria: en España
  el Krusty Krab es el «Crustáceo Crujiente»). Usar **Crustáceo
  Cascarudo**, **Balde de Carnada**, **Cangreburguer**.
- **Dibujo en 3D realista o brillante**: la serie es 2D, plana, con borde
  negro. El 3D sólo para el objeto, y con aspecto pintado.
- **El Balde de Carnada lleno de clientes**: sólo si es un chiste
  (como en *Plankton: La película*).
- **Usar el Bob burlón de mayúsculas alternas** sin comprobar que el
  canal lo usa: no está en la lista de memes latina. Mejor uno de los
  confirmados. Y el meme del canal es **institucional** (el Vídeo de
  Entrenamiento): un cartel o pantalla del Crustáceo, no una foto suelta
  de reacción.
- **Poner «$»** en la lámina: en la serie los precios van en dólares, pero
  el canal pide **soles (S/)**. Un guiño que pega: el menú del Crustáceo
  **reescrito en soles**.

---

## 15 · Poses analizadas por personaje

> [!warning] Cómo leer esta sección
> No pude ver los episodios. Para cada minuto sé **qué dice** el
> personaje (subtítulo) y deduzco la pose del diálogo. **La postura
> exacta hay que comprobarla en el fotograma** antes de recortar. Las
> portadas de §3.1 sí las vi.

### Don Cangrejo

| # | Dónde | Qué pasa | Pose que cabe esperar | Sirve para |
|---|---|---|---|---|
| 1 | 01x10 00:04:58 | «Hello, I'm Mr. Krabs, and I like money» en el escenario | de frente al público, saludo | **presentar** |
| 2 | 04x05 00:01:24 | canta «cha-ching» con el local lleno | brazos arriba, bailando | **celebrar** |
| 3 | 02x20 00:01:03 | cuenta billetes cantando | sentado, billetes en las pinzas | **presentar la caja** |
| 4 | 02x01 00:13:41 | recoge monedas del suelo: «My babies» | agachado, acunando monedas | **ternura con el dinero** |
| 5 | 03x07 00:13:08 | cuadra la caja y busca su moneda | inclinado sobre la caja, cajón abierto | **explicar la caja** |
| 6 | 03x07 00:13:48 | «you stole it, you stole it…» | pinza señalando | **regañar** |
| 7 | 07x06 00:12:53 | «Now, listen up, son» en su oficina | detrás del escritorio de baúl | **explicar** |
| 8 | 02x08 00:06:00 | «any fella who's giving away free stuff…» | pecho fuera, pinza en alto | **animar a reclamar** |
| 9 | 15x11 00:01:20 | «it's f-f-f…» no le sale «free» | sudando, atragantado | **chiste de «gratis»** |
| 10 | 03x06 00:12:12 | «Open for business» en su venta de garaje | brazos abiertos junto a la mesa | **rebajas** |

### Calamardo

| # | Dónde | Qué pasa | Sirve para |
|---|---|---|---|
| 1 | 03x10 00:14:28 | «there's a standing fee» al cliente que no compra | **regañar** con desgana |
| 2 | 03x10 00:15:11 | le enfocan el botón «I Really Wish I Weren't Here Right Now» | **presentar** (el botón = cuadro de texto) |
| 3 | 03x10 00:15:20 | «I'm getting paid overtime for this, right?» | queja |
| 4 | 02x03 00:14:20 y 00:14:50 | «What'll it be?» y, obligado por Don Cangrejo, «May I take your order?» | **atender** de mala gana |
| 5 | 02x04 00:01:43 | «you pay me to stand behind this register» | **pensar**, apoyado en la caja |
| 6 | 03x08 00:13:52 | Calamardín: «You're a cashier» | vergüenza |
| 7 | Portada *Lights, Camera, Pants!* | capa, pajarita roja, puño arriba, dientes apretados ✅ visto | **enfado teatral** |

### Bob Esponja

| # | Dónde | Qué pasa | Sirve para |
|---|---|---|---|
| 1 | Portada *BFBB* | saludo militar, casco, sonrisa ✅ visto | **presentar** |
| 2 | 01x01 00:03:12 | «I'm ready!» | **animar** |
| 3 | 02x01 00:15:24 | le dan la caja: «The cash register?» | sorpresa |
| 4 | 03x10 00:14:54 | «Hello, world, may I take your order?» | **presentar** con sonrisa |
| 5 | Portada *Revenge of the Flying Dutchman* | grito con la boca enorme ✅ visto | **urgencia** («¡caduca!») |

### Patricio

| # | Dónde | Qué pasa | Sirve para |
|---|---|---|---|
| 1 | 02x03 00:04:25 | al teléfono: «No, this is Patrick» | chiste |
| 2 | 02x15 00:15:10 | levanta la mano: «Is mayonnaise an instrument?» | **preguntar** |
| 3 | Portada *Lights, Camera, Pants!* | de policía, boca abierta, enfadado ✅ visto | regañar |

### Plankton

| # | Dónde | Qué pasa | Sirve para |
|---|---|---|---|
| 1 | 14x01 00:09:35 | «That secret formula will be mine» | **plan malvado** |
| 2 | Portada *Lights, Camera, Pants!* | con sombrero, riendo, brazos arriba ✅ visto | **celebrar** (malvado) |
| 3 | Portada *Creature from the Krusty Krab* | gigante detrás de Bob ✅ visto | amenaza |

---

## 16 · Vestuario

| Personaje | Ropa icónica | Colores | Estado |
|---|---|---|---|
| **Bob Esponja** | camisa blanca, **corbata roja**, pantalón **marrón cuadrado**; cinturón negro, calcetines altos con rayas, zapatos negros brillantes | `#FDEE4A` piel, `#FCFAF1` camisa, `#DE1A11` corbata, `#AC5810` pantalón | camisa, corbata y pantalón ✅ medido en la portada; el resto ⚠️ de memoria |
| Bob en el trabajo | gorro de papel del Crustáceo ⚠️ | blanco y azul ⚠️ | de memoria |
| **Don Cangrejo** | camisa azul claro, pantalón azul oscuro con cinturón ⚠️ | cuerpo rojo `#EA3941` ⚠️ | de memoria + paleta de fans |
| **Calamardo** | camisa marrón ⚠️; en el trabajo, el **botón** con frase ✅ | piel verde azulado `#54DBC2` ⚠️ | botón ✅ subtítulo; resto ⚠️ |
| **Patricio** | sólo un bañador **verde con flores moradas** ⚠️ | rosa `#FF808B` ⚠️ | de memoria |
| **Plankton** | nada; un ojo, antenas | verde `#68A079` ⚠️ | fans |
| **Narrador** | traje de buzo antiguo, **gorro rojo** | — | ✅ dos fuentes |

---

## 17 · Paisajes y fondos de pantalla

### Los sitios, con su luz

- **Crustáceo por dentro, de día**: madera cálida, barriles, el barquito
  de la caja delante de la ventana de proa (§5.2).
- **Crustáceo por fuera**: nasa de madera, concha rosa, puertas azules,
  banderas, agua turquesa y cielo de flores (§5.1).
- **Balde de Carnada**: enfrente, gris metálico y vacío ⚠️ (de memoria).

### Fondos de pantalla

- [«SpongeBob Flowers At Bikini Bottom Background», 2928×1431](https://wallpapers.com/background/spongebob-flower-background-2928-x-1431-gmoyqoppdrorzpj9.html)
  (Wallpapers.com; autor y licencia desconocidos ⚠️). Y la [colección de
  fondos de flores](https://wallpapers.com/spongebob-flower-background).
- Los **18 fondos de tarjeta de tiempo** de §3.5 (1000×~730).
- Arte oficial del 25.º aniversario (§3.2): pedirlo en Paramount Press
  Express.

---

## 18 · Estilo de dibujo y técnica, y cómo replicarlo

(pendiente)

## 19 · Texturas 2D

(pendiente)

## 20 · Gustos y detalles de cada personaje

(pendiente)

## 21 · Por qué la gente la ama (y las escenas que hacen llorar)

(pendiente)

## 22 · Fan dubs y comunidad hispana

(pendiente)

## 23 · Colaboraciones, cruces, figuras y cosplay

(pendiente)

## 24 · Obras parecidas y temas relacionados

(pendiente)

## 25 · El mundo, la historia y sus símbolos

(pendiente)

## 26 · Guía para generar con IA (imagen y texto)

**Sólo para fondos, texturas o bocetos. Nunca para inventar al
personaje**: el personaje sale de un fotograma o una portada real.

**Rasgos que nunca cambian**:
- Bob: **esponja cuadrada amarilla** con agujeros verde oliva, dos dientes
  grandes, ojos azules enormes con tres pestañas, camisa blanca, corbata
  roja, pantalón marrón cuadrado.
- Don Cangrejo: **cangrejo rojo**, ojos en antenas altas, pinzas grandes,
  camisa azul ⚠️.
- Calamardo: **pulpo verde azulado**, nariz larga caída, párpados medio
  cerrados.
- Plankton: **diminuto, verde, un ojo rojo**.

**Estilo**: dibujo animado 2D de los 2000, **línea negra gruesa y
limpia**, colores planos sin degradado en los personajes. **Fondos
pintados** a mano, con textura de acuarela o gouache, estampados tiki y
hawaianos, flores en el cielo.

**Luz**: plana, de mediodía; dentro del Crustáceo, cálida.

**Encuadre**: frontal, como plano de dibujo animado; el objeto grande en
primer término.

**Palabras que ayudan**: «2000s Nickelodeon cartoon style», «flat cel
animation», «thick black outlines», «hand-painted tropical background»,
«tiki pattern», «nautical wooden restaurant interior», «lobster trap
building», «hawaiian flowers in the sky», «underwater light, turquoise».

**Palabras que lo estropean**: «3D», «Pixar», «realistic», «anime»,
«glossy», «photographic», «cinematic lighting», «speech bubble».

**Imágenes de referencia de estilo**: portada de *BFBB* (§3.1), los fondos
de tarjeta 009, 011 y 016 (§3.5), el menú «Galley Grub» y el letrero de
concha (§3.4).

---

## 27 · Tres conceptos para la lámina de #ofertas-y-gratis

Los tres usan los textos de §0. Donde pongo una frase «en su voz» es
**traducción mía** del subtítulo inglés (no encontré la latina). Recortes
siempre por `v3/integrar.py` y comprobados a 1:1.

### Concepto A — «La caja de Don Cangrejo» (el objeto del plan, mejorado)

- **Objeto y sitio**: el **barquito de la caja** del Crustáceo Cascarudo
  («register boat», 16x12 00:20:17), con la **caja registradora** encima.
  Detrás, la **ventana de la cocina con forma de proa**. Arriba, colgado,
  **el menú**. Todo en Blender:
  - caja azul pizarra `#427193` con teclas redondas y **contorno negro**
    (textura §3.4); **ventanita de precio** arriba; **cajón abierto**
    lleno de monedas;
  - **tira de ticket** que sale de la caja y se curva por el borde;
  - barquito de tablas ([Wood Floor Deck](https://polyhaven.com/a/wood_floor_deck), CC0);
  - base para modelar: la [caja genérica de Sketchfab](https://sketchfab.com/3d-models/cash-register-1e04d7a73a004e2380e2ee715ce7bd06),
    mirando la del juego ([BFBBR](https://sketchfab.com/3d-models/bfbbr-krusty-krab-cash-register-cc79260fc5f44d73b8268f68dfb83a3f)).
- **Personaje**: **Don Cangrejo**, inclinado sobre el cajón como cuando
  cuadra la caja (03x07 00:13:08). Alternativa: acunando monedas (02x01
  00:13:41). En la otra pinza, levanta **el ticket**.
- **Cómo habla**:
  - Don Cangrejo **habla en el ticket** que sostiene: «**¡El que regala
    es amigo mío!**» (de 02x08 00:06:00). Letra: Anton, marrón `#51241D`.
  - El **Narrador** habla en una **tarjeta de tiempo** en la esquina, sobre
    la tela tiki roja (fondo 016): «**LOS GRATIS CADUCAN**». Letra: Some
    Time Later, lila `#EF7EF2`.
- **Dónde va cada texto**:
  - Menú colgado, título: **Ofertas y gratis** (Anton, rojo ladrillo con
    borde, como «GALLEY GRUB»).
  - Menú, primera línea con puntos guía: **Juegos gratis** ……… **S/ 0.00**.
  - Menú, segunda línea: **Rebajas** ……… **en soles**. Los puntos guía
    son los del menú real de la serie.
  - Menú, pie: **Steam**, **Epic**, **GOG** como tres «combos».
  - Ventanita de la caja: **S/ 0.00**.
  - Ticket de Don Cangrejo: su frase y, debajo, **Con el precio en soles**.
  - Tarjeta del narrador: **Los gratis caducan** / **Reclámalos**.
  - Cartel pequeño pegado al barquito: **Las noticias van en noticias-gaming**.
- **Para que no quede plano**:
  - el **cajón abierto con monedas** en primer plano, desenfocado;
  - el ticket **curvado hacia la cámara**, delante de la caja;
  - **contraluz cálido** de la ventana de proa, detrás de Don Cangrejo;
  - el menú proyecta **sombra de cuerdas** sobre la pared.
- **Lámina 2**: el **ticket largo** con la plantilla de publicación de §0.

### Concepto B — «Calamardo en la caja» (el secundario más querido)

- **Objeto y sitio**: **el menú «Galley Grub» reescrito en soles**,
  colgado con cuerdas y ganchos (así lo cuelga la recreación de §3.4:
  piezas «Menu Hook» y «Rope»). Debajo, el barquito con la caja y
  **Calamardo** apoyado en ella. En Blender: tablero de madera con cuerdas
  y la caja del concepto A.
- **Personaje**: **Calamardo**, aburrido, apoyado en la caja («you pay me
  to stand behind this register», 02x04 00:01:43). Lleva **su botón en el
  pecho** (03x10 00:15:11). Alternativa de cara: la portada de *Lights,
  Camera, Pants!* (§3.1) si se quiere enfado.
- **Cómo habla**:
  - **El botón** de su uniforme es su cuadro de diálogo, como en la
    serie: «**LOS GRATIS CADUCAN**».
  - Un **cartón escrito a mano** pegado a la caja, con su chiste del
    vídeo de formación («there's a standing fee», 03x10 00:14:28):
    «**Mirar sin reclamar también cuesta**». Letra: Chewy.
- **Dónde va cada texto**:
  - Título del menú: **Ofertas y gratis**.
  - Líneas del menú: **Juegos gratis**, **Rebajas**, cada una con su «S/».
  - Tres «combos» del menú: **Steam**, **Epic**, **GOG**.
  - Cartel del puesto (donde va «ORDER HERE»): **Con el precio en soles**.
  - Botón: **Los gratis caducan**. Cartón: la frase de Calamardo y
    **Reclámalos**.
  - Esquina baja, pequeño: **Las noticias van en noticias-gaming**.
- **Para que no quede plano**:
  - el menú **delante y arriba**, algo girado, con sombra;
  - por la ventana de proa, detrás, **la espátula de Bob Esponja** asomando;
  - luz de **ojo de buey** en diagonal sobre Calamardo.

### Concepto C — «El Crustáceo contra el Balde» (el meme, con el narrador)

- **Objeto y sitio**: la **fachada** del Crustáceo Cascarudo, con su
  **letrero de concha rosa** (un objeto de Blender con grosor) y la
  **ventana con cartel**. Al otro lado de la calle, el **Balde de
  Carnada** vacío. Es el meme «Krusty Krab vs. Chum Bucket» (§14), que
  nació con PS4 contra Xbox: **es de videojuegos**.
- **Personajes**: **Patricio** (el más votado) en la cola con otros
  clientes; **Plankton** solo en la puerta del Balde, mirando. Don
  Cangrejo en la puerta del Crustáceo, contento, contando la cola.
- **Cómo habla**:
  - El **letrero de concha** y los carteles de la fachada hablan por el
    sitio.
  - Una **tarjeta de tiempo** del narrador en una esquina, como segundo
    fotograma: «**DOS DÍAS DESPUÉS…**», con el cartel de la ventana ya
    cambiado a **«CADUCÓ»**. Así se cuenta «los gratis caducan» sin
    explicarlo.
- **Dónde va cada texto**:
  - Concha: **Ofertas y gratis**.
  - Cartel de la ventana (el «OPEN»): **Gratis hoy**.
  - Las **banderas de señales** de la fachada, una por tienda: **Steam**,
    **Epic**, **GOG**.
  - Pizarra en la puerta: **Rebajas con el precio en soles**.
  - Letrero del Balde: **Precio completo**.
  - Tarjeta del narrador: **Dos días después** y **Reclámalos**.
  - Pequeño, en la acera: **Las noticias van en noticias-gaming**.
- **Para que no quede plano**:
  - la **cola de clientes de espaldas** en primer plano;
  - **rayos de luz de agua** (cáusticas) sobre la arena;
  - el cielo con **nubes de flor** detrás;
  - el letrero de concha **sobresale** y hace sombra en la fachada.

### ¿Cuál primero?

**A**. Es el objeto del plan, el dinero es de Don Cangrejo y la caja se
hace entera en Blender. **B** si el dueño prefiere al personaje que más
gusta a los adultos. **C** es la más de «meme» y la que más gente
reconoce, pero lleva más dibujo.

---

## 28 · Lo que no pude verificar

- **Cómo escribe Steam Perú el precio** (¿«S/ 12.90» o «S/.12.90»?) y el
  precio de hoy de *Titanes de la Marea*: Steam no abre desde aquí ⚠️.
- **GOG en soles**: no encontré si GOG cobra en soles en Perú. **Epic**:
  un resultado dice que sí, sin fuente clara ⚠️.
- **La frase latina exacta** de Don Cangrejo en «Choque Cultural», *Delivery
  of DOOM* y *Christmas Who*.
- La **voz latina actual de Karen** y la de **Patricio en las temporadas
  1 a 3**.
- **Poses exactas**: deducidas del diálogo; mirar el fotograma.
- **Cajas de diálogo de los videojuegos** (Game UI Database no abre).
- **Arte del 25.º aniversario** y el **Main Model Pack**: existen, no los vi.
- **Nombres de la caja** («Betsy», «Cashy»): una sola wiki.
- **Vestuario de Don Cangrejo, Calamardo y Patricio**: de memoria.
- **Nombre latino de «Barg'N-Mart»**.
- Si los modelos de Sketchfab son **realmente libres**: los de «BFBBR» y
  «SBFBBR» salen del juego.
- Subtítulos de las temporadas **5, 6 y 8 a 12** (no están en el
  repositorio): ahí van *Money Talks* y *Penny Foolish*, dos episodios de
  Don Cangrejo y el dinero, **sin minuto**.

---

## 29 · Cumplimiento del encargo

(pendiente)

## 30 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)

- **Bloqueado** (403 o «egress blocked»): doblaje.fandom.com,
  spongebob.fandom.com, es.spongepedia.org, sensacine.com.mx, draquio.com,
  sketchfab.com, gameuidatabase.com, nickalive.net, huggingface.co,
  1001fonts.com, dafont.com, fontspace.com, fontmeme.com,
  store.steampowered.com (y su API), gog.com, store.epicgames.com.
  YouTube, Wikipedia, Reddit y TV Tropes ya se sabían bloqueados.
- **Funciona**: la herramienta WebSearch, GitHub (por la herramienta de
  búsqueda, por `git clone` y por `raw.githubusercontent.com` y
  `media.githubusercontent.com`).
- `herramientas/investigar_serie.py`: **no se corrió** (Fandom 403). **No hay
  `hojas/`**.

### Búsquedas web (48; es = español, en = inglés)

1. (es) reparto latino Don Cangrejo, Calamardo, Patricio, Plankton, Venezuela
2. (es) voz latina de Calamardo y Patricio
3. (es) voces latinas de «Bob Esponja: Al rescate»
4. (es) el doblaje se muda a México, temporadas nuevas
5. (es) Narrador Francés, Orlando Noguera, Juan Guzmán
6. (es) frases de Don Cangrejo sobre el dinero
7. (es) Olin Garcés y la muerte de Luis Pérez Pons
8. (es) voces anteriores de Plankton; Karen
9. (en) encuestas de personaje favorito
10. (es) encuesta de personaje favorito en Latinoamérica → **no hay**
11. (es) «Unos momentos después»
12. (en) letras del logo y de las tarjetas
13. (en) precios del menú del Crustáceo
14. (en) la caja registradora y el barquito de Calamardo
15. (en) Sketchfab: caja y Crustáceo
16. (en) *Titans of the Tide*
17. (es/en) *Titans of the Tide* en Steam, título en español
18. (es) Steam, Epic y GOG en soles en Perú
19. (es) «Hola, me gusta el dinero»
20. (es) memes latinos de Bob Esponja
21. (en) colores hex de los personajes
22. (en) cajas de diálogo de *Rehydrated* y *Cosmic Shake* → **no encontradas**
23. (en) *Krusty Cook-Off*
24. (en) nubes de flor, estilo de fondos, Hillenburg
25. (en) música de fondo: steel guitar, «Grass Skirt Chase»
26. (es) letra latina del tema de entrada
27. (es) *En busca de los pantalones cuadrados*, doblaje
28. (en) Don Cangrejo: carácter, Armada, Perla
29. (en) Calamardo: cajero, clarinete, por qué gusta a los adultos
30. (en) Plankton, Karen y *Plankton: La película*
31. (es) «¿Es el Crustáceo Cascarudo? — habla Patricio»
32. (es) adaptación de nombres del doblaje (Doblaje Wiki)
33. (es) voz de Bob en la 1.ª temporada; Patricio antes de la 4.ª
34. (es) clips oficiales de YouTube en español
35. (en) arte oficial del 25.º aniversario
36. (en) hojas de modelo (Main Model Pack)
37. (en) ArtStation: fan art 3D del Crustáceo
38. (en) texturas CC0 de madera (Poly Haven)
39. (en) el interior del Crustáceo
40. (es) tendencias de TikTok 2026
41-44. (es) títulos latinos de episodios (la herramienta hizo cuatro búsquedas)
45. (en) el Narrador Francés y Cousteau
46. (en) meme «Krusty Krab vs. Chum Bucket»
47. (es) frases de Calamardo en latino
48. (es) doblaje latino de *The Cosmic Shake*

**Otros idiomas**: la serie es de Estados Unidos; no busqué en japonés,
coreano ni chino. Los subtítulos que usé traen chino, pero sólo leí el
inglés.

### GitHub (sin cupo de búsquedas web)

- [1440kHz/sbsp-chs-eng-sub](https://github.com/1440kHz/sbsp-chs-eng-sub):
  190 archivos de subtítulos con tiempos. **La base de §2 y §15.**
- [Jordy3D/Jordy3D.github.io](https://github.com/Jordy3D/Jordy3D.github.io):
  la letra Some Time Later (OFL) y 18 fondos de tarjeta.
- [MishaalButt/Projects](https://github.com/MishaalButt/Projects): menú
  «Galley Grub», cartel «ORDER HERE», texturas de la caja.
- [hmmm2121/Doom-of-the-Bob](https://github.com/hmmm2121/Doom-of-the-Bob):
  texturas de la fachada del Crustáceo.
- [libretro-thumbnails/Nintendo_-_GameCube](https://github.com/libretro-thumbnails/Nintendo_-_GameCube):
  portadas y capturas de cinco juegos.
- [google/fonts](https://github.com/google/fonts): 11 familias comprobadas.
- También vi repositorios con **transcripciones sin tiempos**
  (p. ej. [speegled/SpongeBob](https://github.com/speegled/SpongeBob)); no
  hicieron falta.

### Fuentes consultadas por tipo

En total la biblia enlaza **110 direcciones distintas de 50 sitios**.

- **Oficiales**: canal de YouTube «Bob Esponja en Español», clip de
  Paramount+, Facebook oficial de Bob Esponja, TikTok de Paramount+ México,
  Steam (fichas de *Titanes de la Marea* y *Rehydrated*), THQ Nordic,
  Tilting Point, App Store, Netflix, Paramount Press Express, PR Newswire.
- **Staff y actores**: TikTok de Luis Carreño (tres vídeos).
- **Prensa**: ANMTV (3 notas), El Financiero, El Tiempo, Mediotiempo,
  SuperGeek, La Nuestra, Xataka México, Colectiva Xbox, AWN, NickALive,
  ComicBook, VGEzone.
- **Wikis**: Doblaje Wiki, Encyclopedia SpongeBobia, Bob Esponja Wiki,
  SpongeBob Wiki (spongebobwiki.org), Nickelodeon Wiki, Great Characters
  Wiki, Wikipedia (por resultados de búsqueda), Know Your Meme.
- **Foros y blogs**: SBMania, blog spongebobsoundtrack (Tumblr), Medium,
  The Odyssey.
- **Arte y 3D**: Sketchfab (7 modelos), ArtStation (6 obras), LEGO Ideas,
  Wallpapers.com, Poly Haven.
- **Letras**: 1001 Fonts, FontMeme, Google Fonts (GitHub).
- **Rankings**: Ranker.
- **TV Tropes**: sólo apareció en resultados (ficha de Don Cangrejo); no
  abre. **The Cutting Room Floor**: ficha de *Rehydrated* vista en
  resultados; no abre. **Reddit, Pixiv, DeviantArt y Wayback**: no
  accesibles o sin resultados útiles.

### Lo que NO encontré

- Encuesta oficial de popularidad (ni de Nickelodeon ni latina).
- Minutos de los vídeos de YouTube y TikTok.
- Las cajas de diálogo de los videojuegos.
- Las frases latinas de Don Cangrejo sobre «gratis».
- Imágenes del Main Model Pack y del arte del 25.º aniversario.
- El formato de precio de Steam Perú.
