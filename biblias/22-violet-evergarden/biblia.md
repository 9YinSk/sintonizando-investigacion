---
tags: [biblia, serie, laminas]
serie: "Violet Evergarden"
canal: "#poemas"
fecha: 2026-09-24
---

# Biblia · Violet Evergarden — para #poemas

> [!important] Cómo se hizo, y sus límites
> - **Segunda pasada (24-sep-2026), con la red abierta.** La hizo un
>   equipo: 4 investigadores (imagen, vídeo, voz, texto) y un redactor.
>   Se pudo usar: la API de Fandom (wiki de la serie y **Doblaje Wiki**),
>   `investigar_serie.py` (**2 hojas de contacto** de la wiki),
>   `fotogramas.py` sobre **6 vídeos mirados de verdad** (opening,
>   tráiler, ending y 3 escenas, en Dailymotion e Internet Archive),
>   `voz.py` (Whisper) sobre un audio oficial de Doblaje Wiki, Pillow y
>   `estilo.py` para **medir colores**, la API de Sketchfab, AniList,
>   Danbooru, Arctic Shift (Reddit) y fontTools. **YouTube pedía iniciar
>   sesión** desde el servidor: por eso los clips salen de Dailymotion
>   (512×288) y no hay fotogramas en 1080p. TV Tropes, TCRF y Wayback
>   dieron 403 o bloqueo. Lo nuevo está en «Segunda pasada · qué
>   cambió», justo debajo.
> - **Formato de minutos en la segunda pasada**: «0:21» es el minuto del
>   clip que se enlaza (con `?t=` en el enlace); «00:12:37» sigue siendo
>   el minuto del episodio según el subtítulo japonés.
> - *Primera pasada (lo que sigue es su nota original):*
> - La red de esta sesión estaba cerrada. Fandom (incluida Doblaje Wiki y
>   su API), ANMTV, Bubbleblabber y la mayoría de webs daban **403** o
>   «bloqueado» por curl y por WebFetch. Por eso **no se pudo correr**
>   `herramientas/investigar_serie.py`: **no hay hojas de contacto** ni
>   carpeta `hojas/`. Las imágenes van sólo como enlaces.
> - Mi fuente principal fueron **50 búsquedas web** en español, inglés,
>   japonés, chino y coreano (lista completa al final, en la bitácora).
>   En total cito **más de 80 sitios distintos**.
> - GitHub sí respondía. De ahí saqué lo más útil: **los subtítulos
>   japoneses de Netflix de toda la serie, del especial y de la película,
>   con sus tiempos**, del repositorio
>   [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror).
>   La película trae además el inglés. Con ellos doy el **minuto de cada
>   escena** y la frase exacta. Es el minuto de ese archivo: puede moverse
>   uno o dos minutos según la plataforma.
> - **Cómo leo los episodios**: «ep. 5» es el episodio 5 de la serie (13
>   episodios, 2018). «Especial» es el episodio extra de 2018 (en Netflix,
>   «Violet Evergarden: Especial»). «Gaiden» es la película de 2019 sobre
>   Isabella y Taylor. «Película» es la de 2020. El minuto va así: 00:12:37.
> - Las frases japonesas las traduzco yo. **No son del doblaje latino**
>   salvo que lo diga con su fuente.
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su minuto.
>   ⚠️ **dudoso**: una sola fuente, o lo describo de memoria. Lo de memoria
>   siempre va marcado.

---

## Segunda pasada · qué cambió

Repaso del 24-sep-2026 con la red abierta. Sale de las partes de los
cuatro investigadores (`partes/imagen.md`, `video.md`, `voz.md`,
`texto.md`). Se editó cada sección en su sitio; lo nuevo va marcado con
«**Nuevo (2.ª pasada)**».

### Corregido (antes → ahora)

| Qué | Antes | Ahora | Fuente |
|---|---|---|---|
| Colores de Violet | Todos estimados ⚠️ | **Medidos** con Pillow y `estilo.py`: chaqueta `#2F444F`/`#3B5363`, broche `#4C8669`, lazo del cuello `#ECE2C9`, lazo rojo del pelo `#63394D`, ojos `#3BADB3`, pelo `#CBB56B` | opening 0:21, fotogramas de la wiki (§5.3, §16) |
| Broche | `#1E8A5A` | `#4C8669`, más verde oliva | opening, [0:48](https://www.dailymotion.com/video/x8c9bet?t=48) |
| Lazo rojo del pelo | `#9E2630` | `#63394D`, rojo vino apagado | `Violet's smile.jpg`, ep. 5 |
| Chaqueta | `#003153` / `#1F3A5C` | `#2F444F`–`#3B5363` a contraluz; `#2C3A56` en el databook | opening 0:21 y hoja de modelo |
| Uniforme militar | ⚠️ de memoria | Existe y se ve: casaca **verde oliva oscura** `#413228`, correa `#6A422A` | hoja 1 nº19-20, `Violet2.jpg` |
| Sketchfab | «Protoform», licencia sin ver; «Myylo»; «welvdax» | **jonhiggins**, CC BY-NC-SA; **Mylo21**; **KamiPedro** | API de Sketchfab (§4) |
| Nombre del oficio en la wiki | «Auto Memory Dolls» | La página se llama **«Auto Memories Doll»** | API de Fandom |
| Special Elite | ⚠️ parecido a ojo | ✅ es la letra **real** de la web oficial | análisis del CSS ([わくぱく](https://wakupaku.hmup.jp/blog/blog/design-anime-violetevergarden)) |
| Manga | ⚠️ «no hay manga» | ✅ no hay manga: las 3 entradas son `NOVEL` | API de AniList |
| Violet no parpadea | de memoria | ✅ decisión del director Ishidate | [entrevista](https://atmafunomena.wordpress.com/2018/08/26/violet-evergarden-interviews-taichi-ishidate-earnestness-immersion-subtlety/) |
| Voz japonesa de Hodgins | Takehito Koyasu ⚠️ | ✅ «cv 子安武人» en pantalla | tráiler [0:22](https://www.dailymotion.com/video/x7t0he2?t=22) |
| Popularidad | Benedict 2.º ⚠️ una fuente | ✅ Benedict 2.º en 2022 y 3.º en 2021 (Hodgins 2.º); **Gilbert** es el 2.º más dibujado | ねとらぼ 2021 y 2022, Danbooru (§9) |
| Pelo de Gilbert | sin describir | **azul muy oscuro** (hoja 1 nº12, 26, 31). La parte de imagen lo daba «castaño rosado» mirando `Ep1.14.png`, pero esa captura es de **Hodgins** (hoja 1 nº3) | hojas de contacto |
| Benedict | «uniforme de cartero, pelo largo» ⚠️ | **rubio**, camisa blanca con tirantes; **no usa el uniforme oficial** | tráiler 0:28, Fanbook |
| Loop de Violet en el ep. 10 | Arruti en toda la serie | En el **ep. 10** la dobla **Nycolle González** | Doblaje Wiki, ANMTV |

### Añadido

- **3 hojas de contacto** (antes 0): `personajes_01.jpg`, `personajes_02.jpg`
  (wiki) y `escenas_01.jpg` (fotogramas de vídeo). Ver §3.5.
- **6 vídeos mirados** con `fotogramas.py`: opening, tráiler, vídeo del
  ending y 3 escenas (ep. 1, ep. 10, ep. 11), con minuto y enlace `?t=`.
- **La primera frase textual del doblaje latino** (Andrea Arruti), sacada
  de su audio oficial en Doblaje Wiki (§10).
- **Reparto latino completo** (31 papeles) con el minuto de la muestra
  oficial de Doblaje Wiki, y los cambios de voz dentro de la serie.
- **Caras por emoción** con capturas reales; **altura y grupo sanguíneo**
  del Starter Book oficial; **Gilbert** en la tabla de poses.
- **Secciones nuevas para los puntos 18 a 25** de ENCARGO.md: técnica y
  cómo replicarla, texturas 2D, gustos, por qué la aman, fan dubs y
  comunidad hispana, colaboraciones, obras parecidas y el mundo.
- **Cumplimiento del encargo**: la tabla con los 25 puntos, antes de la
  bitácora.
- **Aviso para no repetir**: Frieren (biblia 33) ya propone para este
  mismo canal un **diario con pluma y tintero en luz dorada**. Los
  conceptos de Violet se quedan con la **máquina de escribir**, el sobre y
  el casillero (§19).

### Los ⚠️

- Antes: **70** ⚠️. Después: ver la última línea de esta sección (se
  cuenta al cerrar).
- Siguen dudosos: fotogramas en 1080p (YouTube bloqueado), la secuencia
  animada del ending, las caras de miedo y vergüenza, caras de Gilbert y
  Hodgins, comida favorita y cumpleaños (salvo Violet), el compositor por
  pista del OST, vistas de los fan dubs y el lacre de los sobres visto en
  un fotograma.

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, categoría EL TALLER):

> **ıı・✍️・poemas** (foro) · 2 hilos · etiquetas: Poema, Letra de
> cancion, Microrrelato, Frase suelta, En proceso, Terminado, Traduccion,
> Libre para usar, No usar sin permiso — _Un hilo por texto. Poemas,
> letras, microrrelatos. Se lee despacio: si comentas, comenta el texto._
>
> Hilos: «📌 Cómo se cuelga un texto aquí» (fijado, 1 mensaje) y
> «EJEMPLO · Tres mil ochocientos».

Función según el encargo: **foro de poemas, letras y microrrelatos**, con
las etiquetas **Libre para usar / No usar sin permiso**.

> [!warning] El texto del hilo fijado NO está en el inventario
> «Cómo se cuelga un texto aquí» tiene 1 mensaje, pero el inventario no
> copia su contenido. No lo invento: abajo propongo los textos a partir
> de la descripción del canal y de sus nueve etiquetas. Antes de rotular,
> conviene copiar el mensaje fijado real.

### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Poemas** | nombre del canal |
| 2 | **Un hilo por texto** | cómo se usa |
| 3 | **Poemas, letras, microrrelatos** | qué cabe |
| 4 | **Aquí se lee despacio** | el tono |
| 5 | **Si comentas, comenta el texto** | la norma |
| 6 | **Libre para usar** | etiqueta de permiso 1 |
| 7 | **No usar sin permiso** | etiqueta de permiso 2 |
| 8 | Frase de Violet, en su voz (ver §7 y §19) | gancho |

### Los textos de la lámina 2 (las etiquetas)

Las nueve etiquetas no caben con calma en la lámina 1. Propongo
**lámina 2**, repartida en tres grupos, como tres montones de cartas:

| Grupo | Etiquetas | Pregunta que contesta |
|---|---|---|
| **Qué es** | Poema · Letra de cancion · Microrrelato · Frase suelta · Traduccion | ¿Qué tipo de texto cuelgas? |
| **Cómo va** | En proceso · Terminado | ¿Está acabado? |
| **Quién lo usa** | Libre para usar · No usar sin permiso | ¿Se puede usar para doblar, cantar o editar? |

Nota: en Discord las etiquetas están escritas **sin tilde** («Letra de
cancion», «Traduccion»). En la lámina conviene rotularlas **igual que en
Discord**, para que la gente las reconozca al buscarlas, o pedir al dueño
que les ponga la tilde en el servidor. Es decisión suya.

La idea encaja con la serie: en la serie hay **sellos, sobres y sacas de
correo**; y en el especial todo el C.H. llena la mesa de **borradores de
letra de canción** (ver §2). La lámina 2 puede ser la mesa de clasificar
cartas de la oficina de correos.

---
## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué Violet Evergarden encaja con #poemas | Toda la serie trata de **poner en palabras lo que alguien siente**. Violet es una **«Auto Memory Doll»** (自動手記人形): escribe cartas por encargo, a máquina. Y el oficio nace **para una escritora**: el Dr. Orland inventó la máquina para su mujer Mollie, **novelista que se quedó ciega** (ep. 2, 00:20:09 a 00:20:27) ✅. |
| La escena que más encaja | **El especial** (2018): a Violet le piden **la letra de una canción** para una ópera, no una carta. Toda la oficina escribe borradores: Hodgins **un haiku**, Benedict **un grito punk** (Especial, 00:13:19 a 00:13:50) ✅. La letra final, «愛はいつも 陽だまりの中にある» («el amor siempre está donde da el sol»), la canta la soprano Irma (00:28:59) ✅. |
| Frase guía del oficio | «Una carta transmite el corazón de alguien. Una buena Doll rescata, de entre lo que la persona dice, **el corazón verdadero que quiere transmitir**» (la instructora, ep. 3, 00:08:23) ✅. Es exactamente lo que se pide al comentar en #poemas: **comentar el texto**. |
| Cuadro de diálogo propio | **No hay globo.** Los personajes «hablan» con **cartas escritas a máquina**, leídas en voz en off, y con **el sobre** (sello de lacre, sello de correos). En pantalla, la carta se ve como **hoja escrita en el alfabeto inventado** de la serie (el «tellsis», que los fans llaman *nunkish*) ✅. |
| Objeto para la lámina | **La máquina de escribir de Violet**, con una hoja puesta. Está inspirada en las **Underwood portátiles de cuatro filas de los años veinte** ✅ (fan en ArtStation + Yahoo! Chiebukuro y reventas japonesas). Hay un modelo 3D **libre CC BY** de una Underwood 4-bank portátil **con su maleta** (§4). |
| El más querido | **Violet**, con muchísima diferencia (53,8 % de los votos en la encuesta de fans de ねとらぼ, 2021; 48,4 % en la de 2022) ✅. Detrás: **Hodgins** 2.º y **Benedict** 3.º en 2021 (565 y 550 votos); **Benedict** 2.º en 2022 (12,9 %) ✅ (§9). En fan art, **Gilbert** es el 2.º más dibujado (Danbooru) ✅. No encontré una encuesta **oficial** de Kyoto Animation. |
| Letras | **Special Elite** o **Courier Prime** para la máquina; **Cormorant Garamond** o **IM Fell English** para títulos; **Pinyon Script** para una firma. Todas traen tildes, ñ, ¿ y ¡: **comprobado en el archivo** con fontTools. |
| Voz latina | Violet: **Andrea Arruti** (serie y especial; en el ep. 10, **Nycolle González**) ✅; frase textual suya: «Ya no quiero matar a nadie más. Las órdenes del mayor fueron vivir, nunca fueron matar» (§10) ✅; tras su muerte en enero de 2020, **Nycolle González** (Gaiden y película) ✅. Hodgins: **Carlos Hernández** ✅. Cattleya: **Carla Castañeda** ✅. Estudio **SDI Media de México** (luego Iyuno-SDI) ✅. |
| Tono | **Luz de tarde, polvo dorado, papel y tinta.** Melancólico y tierno. Nada de chistes sobre la guerra ni sobre el incendio de Kyoto Animation (2019). |

---

## 2 · Las escenas que sirven para #poemas (con minuto)

Todas salen de los subtítulos japoneses de Netflix de
[kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Violet%20Evergarden)
(carpeta `[Retimed]`, que trae el nombre de quien habla): el texto y el
minuto están comprobados ✅. La traducción es mía. Lo que **se ve** en
cada escena (postura, luz) lo describo de memoria ⚠️: mira el fotograma
antes de usarlo.

### 2.1 El especial: «la letra de una canción» (lo más útil)

Título: 「きっと"愛"を知る日が来るのだろう」, en inglés *«Surely, Someday
You Will Understand "Love"»*. Salió en julio de 2018 con el 4.º Blu-ray ✅
([ANN](https://www.animenewsnetwork.com/encyclopedia/anime.php?id=21959),
[MyAnimeList](https://myanimelist.net/anime/37095)). En Netflix
Latinoamérica: «Violet Evergarden: Especial», **doblado** ✅
([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Violet_Evergarden:_Especial)).

En esta escena el subtítulo no siempre dice quién habla: **el texto y
el minuto son seguros**; a quién atribuyo cada línea sin nombre (Benedict,
Cattleya) lo deduzco por el contexto y el modo de hablar ⚠️.

| Minuto | Qué pasa / qué se dice | Para qué sirve |
|---|---|---|
| 00:04:51 | Violet: «La letra estaba en lengua antigua… ¿de qué estaría cantando?» | Traducción (etiqueta **Traduccion**) |
| 00:11:49 a 00:12:02 | Aldo, que hizo el encargo: «No es una carta: es **la letra de una canción**, el aria del clímax de la nueva ópera». En la oficina, Hodgins se sorprende: «¿Entonces no era escribir una carta, sino **una letra**?» | **Letra de cancion** |
| 00:12:22 | Violet: «Es la escena en que la heroína **lee en voz alta la carta de amor** que escribió» | Poema = carta |
| 00:12:47 | Benedict: «¡Pues hacemos nosotros **la mejor letra**! Aquí hay un montón de Dolls buenas» | Taller colectivo |
| 00:13:22 | Hodgins: «Es **un poema de forma fija de Oriente**…»: 君を待つ／岸壁に吹く／風寒し («Te espero. / Sopla en el muelle / un viento frío»). Una Doll, probablemente Cattleya ⚠️: «Qué corto. ¿Servirá para una letra?» | **Poema** (un haiku de 5-7-5) |
| 00:13:36 | Benedict: «¡Mi turno! Una obra maestra»: «Esto es el infierno, **no hope** / sin ti, **no future**». «¡Es el grito de mi alma!» | Humor. **Frase suelta** |
| 00:14:04 | Violet: «Gracias a todos por tantas letras». 00:14:14: «He recibido **muchas armas**» | Violet agradece como soldado |
| 00:24:15 | Violet a Roland: «Yo, que no conozco el amor, ¿**puedo poner el amor en palabras**?» | La duda de todo escritor |
| 00:25:08 a 00:26:32 | El **almacén de cartas sin destino** del correo militar. Voces: «te amo», «a ti, amor mío», «de tu esposa que te quiere». Violet: «Todos meten **su propio "te amo"** en una carta» | Fondo para la lámina 2 |
| 00:27:34 | Violet: «Lo he reescrito» | **En proceso → Terminado** |
| 00:28:03 | Irma, llorando: «Esto… es lo que yo quería» | Terminado |
| 00:28:59 a 00:32:05 | Irma canta la letra: «ただ静かに／おなじ空に／風を聞こう…» y el estribillo «**愛はいつも 陽だまりの中にある**／見えなくても／ふれられなくても／そばにあるように» («El amor siempre está donde da el sol; aunque no se vea, aunque no se toque, como si estuviera a tu lado») | El poema terminado |

**La canción existe de verdad**: se llama **«Letter»**, la canta **TRUE**
(Miho Karasawa), y es **inserto** de la serie ✅
([uta-net](https://www.uta-net.com/song/246452/),
[UtaTen](https://utaten.com/lyric/mi18032603/)). La propia TRUE explicó
en X que **escribió la letra «como Violet» y la cantó «como la soprano
Irma»**, y que era la primera vez que hacía las dos cosas ✅
([X de TRUE](https://x.com/miho_karasawa/status/1231569784153620480)).
Es la mejor prueba de que Violet también es **letrista**.

### 2.2 La serie: escribir con el corazón de otro

| Escena | Minuto | Qué se dice | Para qué sirve |
|---|---|---|---|
| ep. 1 | 00:00:22 | Violet, de niña, ante el **broche verde**: «Aquí están **los ojos del Mayor**. Son del mismo color» | El broche: objeto de la lámina |
| ep. 1 | 00:12:43 | Hodgins le enseña la oficina: «El segundo piso es la oficina y **el departamento de escritura por encargo**» (代筆部門) | La casa de #poemas |
| ep. 1 | 00:21:31 | Violet: «Puedo manejar **una máquina de escribir**» | Presentación |
| ep. 2 | 00:06:12 | Iris: «Otro día entero **escribiendo direcciones**» | Humor de oficina |
| ep. 2 | 00:20:09 a 00:20:49 | Narra Erica: la máquina la inventó **el Dr. Orland**, experto en imprenta, para su mujer **Mollie, novelista que se quedó ciega**. Él la llamó «muñeca de escritura automática». Erica recuerda que **la novela de la Sra. Orland le hizo temblar el corazón** | **El origen del oficio es literario** |
| ep. 3 | 00:08:23 | La instructora Rhodanthe: «Una carta transmite el corazón de alguien. Una buena Doll rescata **el corazón verdadero** que la persona quiere transmitir» | **Norma: comenta el texto** |
| ep. 3 | 00:08:40 | «Escribes rápido y exacto. Pero **lo que escribes no se puede llamar carta**» | Lo técnico no basta |
| ep. 3 | 00:19:03 | La carta de Violet para el hermano de Luculia, de **una sola línea**: «**Gracias por estar vivo**» (生きていてくれて ありがとう) | **Microrrelato / Frase suelta** |
| ep. 4 | 00:16:12 | Violet: «"Te quiero" es **una palabra que pide mucho valor**» | Publicar da vértigo |
| ep. 5 | 00:05:51 | Violet escribe la carta pública de amor: «Cuando miro la luna… pienso que **la luna menguante es como un pétalo que cae**. Y me pregunto qué piensas tú al ver lo mismo». Charlotte: «**Tiene la luna y la flor**, como pedí» | **Poema por encargo** |
| ep. 5 | 00:15:08 | Violet a la princesa: «Esta vez escriba usted. **Con sus propias palabras**» | **No usar sin permiso**: la voz es del autor |
| ep. 5 | 00:15:16 a 00:17:45 | Las cartas de Charlotte y Damian **se leen en público** y la gente comenta: «¡Qué bonito! Parece una carta de amor de verdad» | Un foro leído por todos |
| ep. 6 | 00:04:40 | En el observatorio: «Trabajan por parejas: uno **descifra**, otro **copia**» | **Traduccion** |
| ep. 7 | 00:07:20 a 00:15:16 | Violet ayuda al dramaturgo **Oscar Webster** a terminar su obra: le lee los papeles de Olive. «Olive, abre tu paraguas. **Ese paraguas son tus alas**» | **En proceso**, escritura a dos |
| ep. 7 | 00:16:50 a 00:17:23 | Violet **cruza el lago con el paraguas**, pisando hojas. «Creo que di tres pasos» | La imagen más bonita de la serie |
| ep. 10 | 00:20:26 a 00:22:38 | Las **50 cartas** de cumpleaños de una madre para su hija, una por año | Textos guardados para el futuro |
| ep. 13 | 00:19:33 a 00:21:04 | La carta de Violet al Mayor: «Primavera, verano, otoño, invierno… **sólo la estación en que usted está no vuelve**». «Ahora… **"te quiero"**… lo entiendo un poco» | **El poema de Violet** |
| ep. 13 | 00:23:17 a 00:23:31 | «Encantada. **Allá donde el cliente lo desee, acudiré.** Servicio de Auto Memory Dolls, Violet Evergarden» | **El saludo del canal** |

El saludo «お客様がお望みなら どこでも駆けつけます» se repite en los
eps. 4, 5, 6, 7, 10 y 13 ✅ (lo he contado en los subtítulos). Es su
frase de presentación.

> [!warning] La frase en latino no la tengo
> No encontré con fuente cómo dice el doblaje latino ese saludo ni cómo
> traduce «Auto Memory Doll». Netflix titula la película de 2019 **«La
> eternidad y la muñeca de recuerdos automáticos»** ✅
> ([Netflix](https://www.netflix.com/es/title/81208936),
> [FilmAffinity](https://www.filmaffinity.com/us/film581891.html)), pero
> eso es el título, no el audio. **Hay que escucharlo en Netflix antes de
> rotular.** Mientras, uso mi traducción.

### 2.3 La película (2020) — por si se quiere a Violet adulta

Subtítulo en inglés y japonés con tiempos (archivo EMBER de
kitsunekko-mirror) ✅:

| Minuto | Qué pasa | Para qué sirve |
|---|---|---|
| 00:03:13 | Daisy encuentra **las cartas de la bisabuela** a la abuela: «Letters?» | Cartas que duran generaciones |
| 00:03:37 | «Hace mucho, un hombre hizo una máquina de escribir para su mujer ciega. La llamó "auto memory doll"» | El origen, otra vez |
| 00:11:29 a 00:12:13 | En el festival del mar, el presentador llama a **Violet, autora del «Himno al mar»** (海への賛歌), que se entrega a la soprano **Irma Felice**, «diosa del mar» de ese año | **Violet, poeta elegida** |
| 00:13:35 a 00:13:54 | Violet: «Era distinto de una carta normal. El mar es inmenso y hermoso, pero no tiene méritos, ni cargo, ni carácter como una persona. **Me costó alabarlo**» | Escribir un poema cuesta |
| 00:14:02 a 00:14:07 | Iris: «¡El año que viene lo escribo yo!». Benedict: «El himno al mar **sólo lo escribe quien es elegido**» | Ganas de publicar |
| 00:14:54 a 00:15:01 | El saludo, con subtítulo inglés: «If it is your wish, I will travel anywhere to meet your request. Auto memory doll Violet Evergarden, at your service» | Saludo |
| (final) | Gilbert en la isla Ecarlate ⚠️ (de memoria) | Tono de cierre |

### 2.4 Escenas miradas en vídeo (Nuevo, 2.ª pasada)

Vistas fotograma a fotograma con `fotogramas.py` (hoja
`hojas/escenas_01.jpg`). YouTube pedía iniciar sesión: son clips
reesubidos en **Dailymotion**, a 512×288. El minuto «0:18» es del clip;
el «00:01:19» es del episodio, cruzado con el subtítulo japonés ✅.

| Escena | Minuto | Qué se ve (mirado, no de memoria) | Para qué sirve |
|---|---|---|---|
| **Ep. 1, el primer texto de Violet** | ep. 00:01:19 a 00:01:34; clip [0:18](https://www.dailymotion.com/video/x947zqa?t=18) | Tumbada en el hospital con vendaje en la frente, sólo un ojo en cámara (clip 0:00-0:10). Luego, sentada en la cama, escribe con la **mano de metal**; la pluma tiembla sobre un papel con letras **Tellsis** (0:18-0:22). Subtítulo en español: «Mayor Gilbert, hoy es el día 120 de mi hospitalización… Solicito una pronta reintegración al servicio». Cierra con «Lo lamento» (0:40) ✅✅ (clip y `.srt` japonés) | **El origen de #poemas**: escribe sin saber aún qué es escribir con el corazón. Hoja escenas nº16-17 |
| **Ep. 10, las 50 cartas** | ep. 00:20:26 a 00:22:38; clip [0:05](https://www.dailymotion.com/video/x80vbaj?t=5), [1:20](https://www.dailymotion.com/video/x80vbaj?t=80), [3:15](https://www.dailymotion.com/video/x80vbaj?t=195) | La casa blanca de Ann (0:05); Ann adulta lee cartas en el campo (1:15); los **montones de cartas atadas** sobre la mesa (2:00): «These letters are to be delivered to Ann Magnolia for the next fifty years» (2:05); Violet llora en la oficina con Cattleya (3:10); cartela 「愛する人は　ずっと見守っている」 (3:15). Subtítulo en inglés, no doblaje ✅ | El episodio que más hace llorar (§21 del encargo, sección «Por qué la aman»). Hoja escenas nº18 |
| **Ep. 11, el paracaídas** | ep. 00:10:04 a 00:10:15; clip [0:09](https://www.dailymotion.com/video/x8qbypz?t=9) | Soldados entre cruces en la nieve al atardecer; el avión; se abre un **paracaídas naranja** sobre el bosque nevado; primeros planos de ojos azules. Violet cae **de espaldas** a cámara: la reconozco por el argumento (va a buscar al soldado Aidan) y el sonido del avión, no porque se vea ⚠️ | Violet en acción, no sólo en la oficina |
| **Opening, la máquina sola** | [0:39](https://www.dailymotion.com/video/x8c9bet?t=39) | La máquina negra sobre mesa de madera clara, sin manos, en penumbra ✅ | El objeto del concepto A. Hoja escenas nº2 |
| **Opening, la mano de metal** | [0:54](https://www.dailymotion.com/video/x8c9bet?t=54) a 1:03 | Dedos de metal que se cierran despacio sobre fondo blanco, las juntas visibles ✅ | Detalle de manos. Hoja escenas nº4 |
| **Tráiler, manos de metal tecleando** | [1:22](https://www.dailymotion.com/video/x7t0he2?t=82) | Las dos manos mecánicas sobre las teclas redondas de la máquina ✅ | **La mejor referencia de manos + máquina**. Hoja escenas nº14 |

---
## 3 · Arte oficial y referencias visuales

> [!note] Ya hay hojas de contacto (2.ª pasada)
> En la primera pasada la wiki no respondía y no se bajó ninguna imagen.
> Ahora hay **3 hojas** en `hojas/` (ver §3.5, qué número sirve para qué)
> y las mejores imágenes, con su tamaño medido, están en
> `referencias.json`.

### 3.1 Webs oficiales (el punto de partida)

| Qué | Enlace | Para qué |
|---|---|---|
| Web del anime de TV | [tv.violet-evergarden.jp](https://tv.violet-evergarden.jp/introduction/) · [música](https://tv.violet-evergarden.jp/music/) | Key visuals, fichas de personaje |
| Web de la película de 2020 | [violet-evergarden.jp](https://violet-evergarden.jp/) · [música](https://violet-evergarden.jp/music/) · [BD](https://violet-evergarden.jp/bddvd/) | Arte de la película |
| Kyoto Animation | [ficha de la obra](https://www.kyotoanimation.co.jp/works/VioletEvergarden/) · [las novelas](https://www.kyotoanimation.co.jp/books/violet/books/) | Portadas de las novelas (Akiko Takase) |
| X oficial | [@Violet_Letter](https://x.com/Violet_Letter/status/1141904986449727489) | Salió al buscar «タイプライター 設定»: probablemente habla de la máquina ⚠️ (no lo pude abrir) |

### 3.2 Key visuals, portadas y libros

| Qué | Dónde lo vi | Estado |
|---|---|---|
| Key visual del anime (anuncio de reparto, oct. 2017) | [MANTANWEB](https://mantan-web.jp/article/20171024dog00m200004000c.html) | ✅ existe; imagen sin ver |
| Key visual del Gaiden | [アニメハック](https://anime.eiga.com/news/109134/) | ✅ existe |
| Categoría «Key Visuals» de la wiki | [Violet Evergarden Wikia](https://violet-evergarden.fandom.com/wiki/Category:Key_Visuals) | bloqueada aquí |
| **Nuevo (2.ª pasada)** · Portada oficial del anime (key visual): Violet camina por un campo con su maleta, vestido blanco al viento, nubes pintadas a pincel | [AniList, 460×644](https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx21827-ubzq619ZA2E9.png) · [banner 1900×400](https://s4.anilist.co/file/anilistcdn/media/anime/banner/21827-ROucgYiiiSpR.jpg) | ✅ el key visual más reconocible |
| **Nuevo** · **Hoja de modelo oficial de Violet** (databook): giro con 3 trajes (militar, Doll, de calle) y expresiones; crédito «キャラクターデザイン：高瀬亜貴子» en la cabecera | [wiki, 3000×2357](https://static.wikia.nocookie.net/violet-evergarden/images/8/87/Violet.Evergarden.%28Character%29.full.2707089.jpg) · hoja 1 nº1-2 | ✅ **la mejor referencia de silueta y ropa** |
| **Nuevo** · Key visual de la película: Violet de pie ante el mar, vestido blanco de gala, luz dorada | [wiki, 1024×799](https://static.wikia.nocookie.net/violet-evergarden/images/6/6e/Violet_movie_%282%29.png) · hoja 2 nº54 | ✅ pose digna, de pie |
| **Nuevo** · Portada de la novela, tomo 1: Violet de cuerpo entero con capa militar sobre el traje de Doll | [wiki, 1024×1446](https://static.wikia.nocookie.net/violet-evergarden/images/a/ae/Violet_Evergarden_Volume_1.png) · hoja 1 nº27 | ✅ |
| Blu-ray 1 de la serie (funda especial en la 1.ª edición) | [animate](https://www.animate-onlineshop.jp/products/detail.php?product_id=1502323) | ✅ |
| **Libro de diseños oficial** «Violet Evergarden Official Design Works»: trae **hojas de modelo de los objetos, con primeros planos de la máquina de escribir** ✅ | [Goodreads](https://www.goodreads.com/book/show/58678237-violet-evergarden-official-design-works) + resultado de búsqueda | **La mejor referencia para modelar la máquina** |
| Libro de postales «Visual Collection» | [Kyoani Shop](https://kyoanishop.com/shopdetail/000000003413/) | ✅ |
| Libro «The Anniversary -Flower-» | [Kyoani Shop](https://kyoanishop.com/view/item/000000003606) | ✅ |
| **Portada del single «Michishirube»** (Minori Chihara): el director Ishidate dijo que **la máquina de esa portada es el modelo que usaron en la serie** | [Sakuga Blog](https://blog.sakugabooru.com/2018/01/13/violet-evergarden-interview-director-taichi-ishidate-shin-q-vol-2-2017/) | ⚠️ una fuente (resumen de búsqueda) |
| Sellos oficiales: **Japan Post** hizo una campaña con **sellos con marco** (フレーム切手) por la película, sept. 2020 | [Japan Post](https://www.post.japanpost.jp/campaign/posukumasns_202009.html) + [web oficial](https://violet-evergarden.jp/news/?id=125) | ✅ dos fuentes. **Sirven de modelo para los sellos de las etiquetas** |

### 3.3 Cómo se hizo (datos de producción)

- **La máquina es 3DCG** y se anima **fotograma a fotograma** para que
  encaje con las manos dibujadas a mano ✅
  ([vídeo oficial «制作風景 第5弾 3DCG»](https://www.youtube.com/watch?v=Ux9u5Zmi3zI),
  [polygonote](https://polygonote.com/2018_0208_4964/)).
- El plano de la máquina del **primer anuncio** tardó **un mes** en
  animarse, con un layout de **1,75 m de alto por 1,36 m de ancho** ⚠️
  ([Sakuga Blog, notas de producción](https://blog.sakugabooru.com/2018/01/13/violet-evergarden-production-notes-1/)).
- **Akiko Takase** ilustró las novelas y diseñó los personajes del anime;
  en el anime **hizo a Violet más joven y «pura e inocente»** en vez de
  «belleza fría» ⚠️
  ([entrevista del fanbook, traducida](https://atmafunomena.wordpress.com/2018/10/09/violet-evergarden-interviews-akiko-takase-highlights-high-heels-suspenders/)).
- El director **Taichi Ishidate** contó que al principio miraba a Violet
  **desde fuera, lo más objetivo posible**, y que **de los eps. 10 a 13
  añadieron planos desde los ojos de Violet**, para que se note que ya
  siente ⚠️
  ([ATMA & Funomena](https://atmafunomena.wordpress.com/2018/08/26/violet-evergarden-interviews-taichi-ishidate-earnestness-immersion-subtlety/),
  [JMAG](https://j-mag.org/en/2018/06/07/violet-evergarden_interview-2/)).
  **Para la lámina**: Violet vista de lado o de tres cuartos, trabajando,
  va con el tono de la serie. **Ojo (2.ª pasada)**: en la misma
  entrevista Ishidate dice que **Violet no parpadea** y que **mira a la
  gente de frente, nunca de reojo** ✅. La cámara puede verla de lado
  mientras teclea; cuando mira a alguien (o al lector), lo hace de frente.
- **Nuevo (2.ª pasada)** · Lo que dijo **Akiko Takase** del traje, en la
  propia hoja de modelo del databook (hoja 1 nº2): «Me fijé en la ropa de
  las **mujeres trabajadoras de la época Art Nouveau y Art Decó**, para
  que se notara que es ropa de trabajo y, por el nombre del oficio, que
  tuviera **aire de muñeca antigua**. La expresión de Violet era muy
  importante porque iba a madurar. Para que se note la elegancia, como
  en **cómo se mantiene erguida**, cuidé también la silueta» (traducción
  del japonés) ✅ (fuente primaria).
- Las **manos mecánicas**: el equipo ya había aprendido a dar detalle al
  metal en *Sound! Euphonium* (los instrumentos) ⚠️
  ([mesa redonda de animadores](https://ultimatemegax.wordpress.com/2022/01/11/violet-evergarden-roundtable-1-hand-drawn-animation-staff/)).

### 3.4 Las imágenes que hay que conseguir (lista para la sesión con red)

Ordenadas por utilidad para #poemas. Todas son **fotogramas** con su
minuto (ver §2) salvo que diga otra cosa:

1. Violet **tecleando** con las manos de metal a la vista (ep. 2,
   00:08:21; y el anuncio oficial de la máquina).
2. La **mesa del especial llena de borradores** (Especial, 00:13:19 a
   00:14:14).
3. **Hodgins leyendo su haiku** (Especial, 00:13:19).
4. **Cattleya leyendo el grito punk** de Benedict, con cara de asco
   (Especial, 00:13:40).
5. El **almacén de cartas perdidas** (Especial, 00:25:08).
6. Violet **cruzando el lago con el paraguas** (ep. 7, 00:16:50).
7. La **carta de una línea** para Luculia (ep. 3, 00:19:03).
8. Violet **saludando** en la puerta (ep. 13, 00:23:17).
9. La **entrega del «Himno al mar»** a Irma (película, 00:12:05).
10. El **broche** en el escaparate (ep. 1, 00:00:22; ep. 8, 00:14:06).
11. Hoja de modelo de la **máquina** (Official Design Works).
12. Portada del single **«Michishirube»** (la máquina «oficial»).

**Ya conseguidas en la 2.ª pasada**: nº1 a medias (manos de metal sobre
la máquina en el tráiler, [1:22](https://www.dailymotion.com/video/x7t0he2?t=82),
y Cattleya tecleando con manos de carne en
[0:34](https://www.dailymotion.com/video/x7t0he2?t=34); falta el plano del
ep. 2); nº10 (el broche en primer plano, opening
[0:48](https://www.dailymotion.com/video/x8c9bet?t=48)). El resto sigue
pendiente: YouTube no dejaba bajar los episodios ⚠️.

### 3.5 Las hojas de contacto (Nuevo, 2.ª pasada)

Tres hojas en `hojas/`, miradas una a una. El número es el de la esquina
amarilla; el tamaño del original va debajo de cada miniatura.

**`personajes_01.jpg`** (wiki, `investigar_serie.py`, nº1-48):

| Nº | Qué es | Para qué |
|---|---|---|
| 1-2 | Bocetos y **hoja de modelo oficial** de Violet (databook, 4060×3080 y 3000×2357) | Silueta, trajes, expresiones |
| 3 | `Ep1.14.png`: **Hodgins** (no Gilbert), «He asked me to come here» | Hodgins en el ep. 1 |
| 6, 8 | Violet vendada en el hospital (ep. 1) | Origen, pose de pensar |
| 12, 26, 31 | Gilbert: militar, de joven, ep. 12 (pelo **azul muy oscuro**, ojos verdes) | Gilbert en recuerdos |
| 13, 37-39 | Iris (asombrada, discutiendo, orgullosa) | Contraste de caras |
| 19-20 | Violet con el **uniforme militar verde oliva** | Pasado de soldado |
| 23 | Gilbert le lee a Violet junto a la chimenea | Aprender a leer |
| 27 | Portada del tomo 1 de la novela (1024×1446) | Pose de cuerpo entero |
| 33 | Violet con flores y texto vertical (`Violet_Anime.jpg`, 1280×780) | Promocional |
| 34 | Violet sentada en un muro ante el mar (`Anime icon.jpg`, 870×1106) | Pose sentada |
| 36 | Gilbert de perfil en la calle de noche | Presentar, pensar |
| 40 | Violet con su maleta junto a macetas de flores | Llegar a un encargo |
| 41 | Violet llorando (1280×720) | Tristeza |
| 42 | Violet sonríe, lazo rojo, cielo (`Violet's smile.jpg`, ep. 5) | Alegría |
| 44 | Violet de frente, broche verde (ep. 3) | **Presentar** |
| 46 | Hodgins de joven | — |

**`personajes_02.jpg`** (wiki, nº49-69):

| Nº | Qué es | Para qué |
|---|---|---|
| 54 | **Key visual de la película**: Violet ante el mar (1024×799) | Pose digna de pie |
| 56 | Luculia abraza a Violet | Amistad, grupo |
| 57 | Cattleya se burla de Hodgins (1200×675) | Humor de oficina |
| 58 | Gilbert y Violet abrazados | Final |
| 60, 69 | Fichas de diseño de cuerpo entero (Violet, traje de Doll y abrigo del Gaiden) | Proporciones |
| 61, 68 | Iris (película y ep. 1) | — |
| 63 | Violet bajo la lluvia (1024×576) | Luz fría |
| 64-65 | Violet de frente, broche y lazo | Retrato |
| 67 | Portada de *Ever After* | — |

**`escenas_01.jpg`** (fotogramas de vídeo, nº1-18; ver §2.4 y §12):

| Nº | Minuto y vídeo | Para qué |
|---|---|---|
| 1 | Opening [0:21](https://www.dailymotion.com/video/x8c9bet?t=21): Violet de busto, pelo al viento | Color medido del traje |
| 2 | Opening 0:39: la máquina sola | **Objeto del concepto A** |
| 3 | Opening 0:48: el broche | Color del broche |
| 4 | Opening 1:00: la mano de metal | Manos |
| 5 | Opening 1:18: la carta sobre la mesa | Papel y luz |
| 6 | Opening 0:12: letras **Tellsis** en tiza sobre negro | Alfabeto del mundo |
| 7-12 | Tráiler [0:22](https://www.dailymotion.com/video/x7t0he2?t=22) a 0:36: Hodgins, el **edificio de ladrillo de C.H.**, Benedict, Cattleya, manos tecleando, Erica (con su voz japonesa en pantalla) | Presentar al grupo |
| 13 | Tráiler [0:56](https://www.dailymotion.com/video/x7t0he2?t=56): Gilbert de noche, faroles | Luz nocturna |
| 14 | Tráiler 1:22: **manos de metal sobre las teclas** | **La mejor para el concepto A** |
| 15 | Tráiler 0:48: Violet de perfil ante Leiden y el mar | Fondo de ciudad |
| 16-17 | Ep. 1 (clip [0:18](https://www.dailymotion.com/video/x947zqa?t=18)): pluma temblando y Violet escribiendo en la cama | Origen de #poemas |
| 18 | Ep. 10 (clip 3:10): Violet llora en la oficina | Tristeza |

---

## 4 · Fan art y 3D (sólo como referencia, o con licencia libre)

### 4.1 Modelos 3D de la máquina (para Blender)

| Modelo | Autor | Licencia | Para qué |
|---|---|---|---|
| [Underwood 4-Bank Typewriter (Portable)](https://sketchfab.com/3d-models/underwood-4-bank-typewriter-portable-b872e2c3f4f7457796edebcb7c0a290e) | Ed Swinbourne (@EdSwinbourne) | **CC BY** ✅✅ (API de Sketchfab, descargable) | **El bueno.** Underwood de 4 filas de finales de los años veinte, **dentro de su maleta portátil**: justo el modelo en que se inspira la de Violet |
| [Underwood Typewriter Vintage Free Raw Scan](https://sketchfab.com/3d-models/underwood-typewriter-vintage-free-raw-scan-4c5e323a09e44c2f909a04c64c0c2cca) | Jordan F (@JordanF3DScans) | CC BY ✅ | Escaneo crudo (Polycam): textura real de metal viejo |
| [Underwood 5 typewriter](https://sketchfab.com/3d-models/underwood-5-typewriter-ad4df24b943e4f6ea4b8336072b0d6ae) | Museo de Ingeniería y Tecnología de Cracovia (usuario mitkrakow) | **CC BY-NC-SA** ✅ (API) | Máquina de oficina grande (1915-1920). NC: sin uso comercial |
| [Underwood Standard Portable](https://sketchfab.com/3d-models/underwood-standard-portable-typewriter-f203a8f060f74284833a68203d55a41b) | **jonhiggins** (antes decía «Protoform», que es el nombre de la colección) | **CC BY-NC-SA** ✅ (API, descargable) | Portátil de 1926. NC: sin uso comercial |
| [Violet Evergarden Typewriter](https://sketchfab.com/3d-models/violet-evergarden-typewriter-f132d3d21ac84410ae64e9c63cf339af) | Andrew Ooi (@ManhattanBat) | **no descargable, sin licencia** ✅ (API) | Sólo mirar: la máquina de la serie, en Maya, ZBrush y Substance |
| [Lowpoly Typewriter for Violet Evergarden](https://sketchfab.com/3d-models/lowpoly-typewriter-for-violet-evergarden-dc4b65aad6e14e5393ef349346941f66) | YoungYeh | **de pago** (licencia Standard) ✅ (API) | — |
| [Typewriter for Violet Evergarden](https://www.blenderkit.com/asset-gallery-detail/56c441ae-7eb0-433e-8bc5-c7e8f42af272/) | BlenderKit | ⚠️ sin ver si es gratis; también se vende en [Superhive](https://superhivemarket.com/products/typewriter-for-violet-evergarden) | Hecha ya para Blender |

**Crédito exacto** para el de Ed Swinbourne (CC BY confirmado por la API
de Sketchfab en la 2.ª pasada): «Underwood 4-Bank Typewriter (Portable)»
by Ed Swinbourne (EdSwinbourne), sketchfab.com, licensed under CC BY 4.0.

La máquina de la serie **no es una Underwood exacta**: es una inspirada
en las primeras Underwood portátiles de 4 filas, de mediados de los
veinte ✅ ([Isra ValRiq en ArtStation](https://www.artstation.com/artwork/E6xRv);
en Japón lo repiten [Yahoo! Chiebukuro](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q10247790020)
y [un blog de note](https://note.com/viaggiofran/n/n051a1b13d7d8)). Las
**teclas llevan el alfabeto inventado** (ver §6.3). Hay gente que se
compró una máquina tras ver la serie ✅
([tienda Ogawa Shōkai en X](https://x.com/ogawashokai/status/1342451672291835904),
[Bilibili](https://www.bilibili.com/video/BV1wQ4y1N7wy/)).

### 4.2 Objetos de escritorio (libres)

| Modelo | Licencia | Para qué |
|---|---|---|
| [CC0 - Wax Seal 2](https://sketchfab.com/3d-models/cc0-wax-seal-2-bd18fd7b6c1847bc8e7d9e779c122ed5) (plaggy) | **CC0** ✅ | Sello de lacre para «No usar sin permiso» |
| [CC0 - Paper](https://sketchfab.com/3d-models/cc0-paper-b0776948a05f4766a03856223344b264) (plaggy) | CC0 ✅ | Hojas sueltas |
| [CC0 - Candle](https://sketchfab.com/3d-models/cc0-candle-c011470fe2ae43fe9d05a51d885ef498) (plaggy) | CC0 ✅ | Sólo **apagada**, como adorno: nada de llamas (§14) |
| [CC0 - Pencil](https://sketchfab.com/3d-models/cc0-pencil-cb1b27db90eb469eb845017bb300b5d3) (plaggy) | CC0 ✅ | Detalle de mesa |
| [old envelope](https://sketchfab.com/3d-models/old-envelope-3189a8c84df44c5ab91e556736f291c1) (fox_en) | CC BY ✅ | Sobres |
| [Colección CC0 de plaggy](https://sketchfab.com/plaggy/collections/cc0-public-domain-free-models-c1af6539a9ee49f4b3d51fabd6c25a85) | CC0 | Más objetos |

### 4.3 Fan art y escenas 3D (mirar, nunca pegar)

| Obra | Autor | Qué tiene |
|---|---|---|
| [Violet Evergarden Typewritter](https://www.artstation.com/artwork/kQDZN0) | D Arte | **Escena en Blender**: la máquina en un escritorio con cartas, una vela, su maleta y una foto con Gilbert. **Casi el concepto A** |
| [Violet Evergarden still life render](https://www.artstation.com/artwork/r9B43m) | Leihaorambam Abhijit Singh | Bodegón en Blender y Substance: máquina, maleta, **broche**, lámpara |
| [Violet Evergarden - Typewriter](https://www.artstation.com/artwork/E6xRv) | Isra ValRiq | Modelo 3D de la máquina |
| [Violet Evergarden's Typewriter](https://www.artstation.com/artwork/w6mWgw) | (ArtStation) | Otra máquina en 3D |
| [Violet Evergarden + Typewriter](https://violvert.artstation.com/projects/5v2PEJ) | Viol_Vert | Violet con la máquina (2D) |
| [Violet Evergarden's Prosthetic Hand](https://www.artstation.com/artwork/oAYw8w) | (ArtStation) | **La mano mecánica**, de cerca |
| [Violet Evergarden Fan Art](https://liviadesimoneart.artstation.com/projects/qAwmon) | Livia De Simone | Retrato |
| [Violet Evergarden fan art](https://jiuge.artstation.com/projects/N1Vxq) | Fan Yang | Ilustración |
| [Violet Evergarden (Fan art)](https://www.deviantart.com/tokinizzzarts/art/Violet-Evergarden-Fan-art-910665112) | TokinizzzArts | Ilustración |
| [Modelo 3D de Violet](https://sketchfab.com/3d-models/violet-evergar-f65d7c542d814071aa1df14c9001763a) | kumo (@kumo510) | Para mirar poses; licencia ⚠️ |
| [Violet en VRoid Hub](https://hub.vroid.com/en/characters/7071143261300970946) | fan | Modelo para posar |
| [Building The Violet Evergarden CH Postal Office](https://www.youtube.com/watch?v=DQgcRfLXGjc) | Carrot (YouTube) | **Alguien reconstruye la oficina de C.H.**: sirve para ver la fachada |

### 4.4 Modelos 3D de fans con licencia, comprobados por la API (Nuevo, 2.ª pasada)

Licencia y usuario leídos en `api.sketchfab.com/v3/search` ✅ (antes
venían de la página de búsqueda; dos usuarios estaban mal escritos).

| Modelo | Usuario | Licencia | Para qué |
|---|---|---|---|
| [Violet Evergarden Realistic Outfit](https://sketchfab.com/3d-models/none-ee5f9ead63c54b938efc619a7382f885) | **Mylo21** (no «Myylo») | CC BY | Volumen del traje de Doll |
| [Violet Evergarden's Brooch](https://sketchfab.com/3d-models/none-4c9631b0b1f2406f95e4708ba6337784) | Growffle | CC BY | **El broche**, listo para Blender |
| [Violet Evergarden's brooch base](https://sketchfab.com/3d-models/none-ca6742ec90724ea991482876deb64812) | hoanghuygunneo | CC BY-NC | Montura del broche (sin uso comercial) |
| [Jewel · Gem · Violet Evergarden Fanart](https://sketchfab.com/3d-models/none-b7d331c18ecf481183403bdf58cf05ef) | GabrielaHGalicia | CC BY | La gema verde |
| [Violet Evergarden Arm](https://sketchfab.com/3d-models/none-c98c928a1b30411eb9b3e9f88aeb7140) | **KamiPedro** (no «welvdax») | CC BY | **El brazo mecánico** |

### 4.5 Fan art y cosplay con enlace y tamaño (Nuevo, 2.ª pasada)

Del recolector (Safebooru, con el autor u origen), sólo como referencia:

- Violet: [1275×1650](https://safebooru.org/images/4254/91a6f4870040a61acf3dd083c6e38ec1bf24f105.png)
  (origen [reshanims, Tumblr](https://reshanims.tumblr.com/post/714376654591541248)),
  [2051×2165](https://safebooru.org/images/3248/a5c5be77c1435b51f833e3e97f2b9ee851c2e5f0.jpg)
  (Pixiv 84608122, serie de 2020 con Gilbert en las páginas 8 y 10),
  [712×1024](https://safebooru.org/images/3118/a03f7704edceeadde7a25d6313d59bf26406f2bd.jpg)
  ([@bon_hanken](https://twitter.com/bon_hanken/status/1317122752994627584)).
- Gilbert: [2307×2271](https://safebooru.org/images/3248/9a21989a37f1fea7cec6fd4fa6ed32ea6aa5fbef.jpg),
  [2334×3541](https://safebooru.org/images/3250/085206905b7ea56021c1b6aa5eb78360f6c4290c.jpg).
- Hodgins: [3496×4961](https://safebooru.org/images/3360/9a6346a081ca04b16aa977d7c76fdd3077bea544.png)
  (Pixiv 90126306), [4096×1869](https://safebooru.org/images/1327/07f0e4acdb12763a61b20360b1e6aa777f760a5f.jpg)
  ([@minloafie](https://x.com/minloafie/status/2028782703169208458)).
- **Ojo**: el recolector mezcló fan art de **otras series** (Artoria y
  Saber de *Fate*, Frieren, 2B, Toki) porque salen como «relacionadas» en
  Danbooru. **No son de Violet Evergarden**: no usarlas.

**Cosplay** (volumen real de la tela; la parte de imagen lo pone también
en el punto 23):
- Fotos con **licencia libre** de Flickr (vía Openverse) ✅✅:
  [chripell, CC BY-SA 2.0](https://live.staticflickr.com/65535/52471110493_717fcaa09f_b.jpg)
  (684×1024); [esby.photo, CC BY-NC-SA 2.0](https://live.staticflickr.com/891/42755280762_de75ffb92a_b.jpg)
  (Lille, 1024×767) y [otra en Miramas](https://live.staticflickr.com/1891/44308232111_3ed2bdc4bd_b.jpg);
  una serie de **bdrc**, CC BY-NC-ND 2.0 (p. ej.
  [683×1024](https://live.staticflickr.com/7817/46760191944_271c7c1c35_b.jpg)).
  Sirven para ver **cómo cae la falda plisada** al moverse.
- Cosplay de **@swoochu** con foto de **@robinsonflowersphotography**:
  traje de Doll completo con broche y guantes ⚠️ (una fuente,
  [IMDb News](https://www.imdb.com/news/ni64774852); la imagen dio 403).

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

| Sitio | Qué es | En qué se inspira | Estado |
|---|---|---|---|
| **Leiden** | La ciudad-puerto donde vive Violet | Ciudades alemanas: **Núremberg, Mannheim, Fráncfort, Cochem**; en Japón también citan **Génova y la Toscana**. **No se parece** a la Leiden real de Holanda | ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Violet_Evergarden), [oranda.jp](https://oranda.jp/info/violet-evergarden/), [up-tsukuba](https://up-tsukuba.com/violetevergarden-model/)) |
| **Oficina de C.H.** (C.H.郵便社) | Casa vieja de tres pisos que Hodgins compró y reformó. Abajo el correo; en el **2.º piso, la oficina y las Dolls** (ep. 1, 00:12:43) | El **Museo de Kioto** (edificio de ladrillo rojo del barrio de Nakagyō) | ✅ subtítulo + ⚠️ el museo ([wiki](https://violet-evergarden.fandom.com/wiki/C.H_Postal_Company), [up-tsukuba](https://up-tsukuba.com/violetevergarden-model/)). **2.ª pasada**: en el tráiler se ve la fachada de **ladrillo rojo con molduras blancas y palmeras** ([0:24](https://www.dailymotion.com/video/x7t0he2?t=24), hoja escenas nº8) ✅. Su emblema de hierro: §Punto 19 |
| **Casa de Oscar** (ep. 7) | Casa junto a un lago, en otoño, con hojas en el agua | — | ✅ el lago y las hojas (subtítulo 00:15:09); la estación ⚠️ |
| **Observatorio Shahar** (ep. 6) | Biblioteca donde se copian libros antiguos; el cometa Alley pasa cada 200 años (00:06:39) | — | ✅ subtítulo |
| **Castillo de las camelias blancas** (ep. 5) | Palacio de Drossel, de la princesa Charlotte (白椿の城, 00:06:30) | — | ✅ subtítulo |
| **Internado del Gaiden** | Escuela de señoritas | El **castillo de Cochem** (Alemania); la cuenta oficial dijo que fueron a verlo | ✅ ([holyland-times](https://www.holyland-times.com/violet-evergarden-pilgrimage-to-sacred-places/), [seichi-junrei](https://seichi-junrei.info/855/)) |
| **Almacén de cartas perdidas** (Especial) | Almacén militar de correos sin uso, lleno de cartas sin destino | — | ✅ subtítulo 00:25:08 |
| **Teatro de la ópera** (Especial) y **festival del mar** (película) | Donde Irma canta | — | ✅ subtítulos |

### 5.2 Luz (comprobada en vídeo en la 2.ª pasada)

Antes iba «de memoria ⚠️». Ahora sale de los fotogramas de §2.4 y §12 ✅:

- **Tarde dorada**: sol bajo sobre el mar, cielo naranja y rojo
  (opening [1:12](https://www.dailymotion.com/video/x8c9bet?t=72) a 1:15).
  La serie es famosa por esta luz: sol bajo que entra por ventanas
  grandes, motas de polvo y bokeh suave.
- **Día abierto**: campo verde, cielo azul con nubes altas, viento en el
  pelo (opening 0:15 a 0:24; ep. 10, campo de Ann). Aquí se midieron los
  colores del traje.
- **Oficina**: lámparas cálidas, **madera oscura**, ventanales (tráiler
  [0:06](https://www.dailymotion.com/video/x7t0he2?t=6) a 0:10). La luz
  cae sobre la máquina y las manos de metal brillan (tráiler 0:34 y 1:22).
- **Noche de ciudad**: faroles ámbar y **bokeh muy marcado**, gente en
  silueta (Gilbert, tráiler [0:56](https://www.dailymotion.com/video/x7t0he2?t=56)).
  No estaba descrita en la primera pasada.
- **Hospital**: luz **fría** de ventana lateral sobre sábanas blancas,
  nada del dorado de fuera (ep. 1, clip [0:02](https://www.dailymotion.com/video/x947zqa?t=2) a 0:30).
- La tristeza va con **lluvia** (hoja 2 nº63) y **penumbra** (Violet llora
  en la oficina, ep. 10, clip 3:10); la alegría, con **flores y viento**
  (opening 0:27 a 0:36, la flor violeta).

### 5.3 Paleta (hex medidos en la 2.ª pasada)

Medidos con Pillow (bloques de 7×7 píxeles) y `estilo.py` sobre
fotogramas y arte oficial; se dice de dónde sale cada uno ✅. Los
fotogramas del opening son de un clip de 512×288: valen para el tono, no
para el detalle fino. Lo que sigue estimado lleva ⚠️. Paletas de fans
sólo como contraste: [Adobe Color](https://color.adobe.com/Violet-Evergarden-anime-1280x720-color-theme-13839048/),
[anime-colors](https://www.anime-colors.com/violet-evergarden-series/violet-evergarden-series).

| Elemento | Hex medido | De dónde | Nota |
|---|---|---|---|
| Chaqueta azul | `#2F444F` sombra, `#3B5363` luz | opening 0:21 (hoja escenas nº1) | Azul grisáceo oscuro, más apagado que el `#003153` «de libro» |
| Chaqueta en el databook | `#2C3A56` | hoja de modelo (hoja 1 nº2) | Azul marino; cae en la misma familia |
| Lazo del cuello | `#ECE2C9` | opening 0:21 | Crema, no blanco puro |
| Broche | `#4C8669` | opening 0:21 y [0:48](https://www.dailymotion.com/video/x8c9bet?t=48) | Verde oliva; antes se estimaba `#1E8A5A` |
| Pelo | `#CBB56B` base, `#E1D6C3` mechones claros | `Violet_Anime.jpg` (promocional) | Dorado apagado |
| Pelo en el opening | `#E6DAC0` luz, `#9E908C` sombra | opening 0:21 | La sombra tira a gris |
| Ojos | `#3BADB3` | `Violet_Anime.jpg` | **Verde azulado**, no azul puro |
| Ojos en el opening | `#426A6B` | opening 0:21 | ⚠️ un solo fotograma |
| Lazo rojo del pelo | `#63394D` | `Violet's smile.jpg` (ep. 5), 77 píxeles | **Rojo vino apagado**; antes `#9E2630` |
| Piel | `#B5A491` | opening 0:21 | — |
| Cuerpo de la máquina | `#1E1D1B` | opening [0:39](https://www.dailymotion.com/video/x8c9bet?t=39) (hoja escenas nº2) | Casi negro, nunca negro puro |
| Madera de la mesa | `#A27234` | opening 0:39 | Madera clara y cálida |
| Papel de carta | `#F0EDE2`, sombra `#DAD4C5` | ep. 10, clip [1:15](https://www.dailymotion.com/video/x80vbaj?t=75) | Coincide con el `#EFE6D2` estimado |
| Uniforme militar | casaca `#413228`, correa `#6A422A` | `Violet2.jpg` (flashback) | Verde oliva muy oscuro |
| Gilbert | chaqueta `#3E3932`, pelo `#3B3734` | tráiler [0:56](https://www.dailymotion.com/video/x7t0he2?t=56), de noche | Pelo oscuro (azul muy oscuro de día, hoja 1 nº12) |
| Cielo de día | `#59CBF4` | `Violet's smile.jpg` | — |
| Web oficial | fondo `#EFEED9`, texto `#B4832F` | CSS de la web ([わくぱく](https://wakupaku.hmup.jp/blog/blog/design-anime-violetevergarden)) | ⚠️ una fuente; crema y bronce |
| Guantes y botas | `#5A3A24` | — | ⚠️ estimado, sin medir |
| Manos de metal | `#B8BCC3`, juntas `#2E2F33` | — | ⚠️ estimado (ver opening 1:00) |
| Lacre | `#8C1F2A` | — | ⚠️ estimado; el lacre no se vio en un fotograma |
| Luz de tarde | `#F2C98A` | — | ⚠️ estimado |

### 5.4 Texturas reales equivalentes (libres)

| Material | Enlace | Licencia |
|---|---|---|
| Papel | [ambientCG Paper 005](https://ambientcg.com/view?id=Paper005), [Paper 001](https://ambientcg.com/view?id=Paper001) | CC0 ✅ |
| Papel viejo | [TextureCan: Paper](https://www.texturecan.com/category/Paper/) | CC0 ✅ |
| Madera de mesa | [ambientCG Wood 026](https://ambientcg.com/view?id=Wood026), [Poly Haven: madera](https://polyhaven.com/textures/wood), [TextureCan Old Wood](https://www.texturecan.com/details/458/) | CC0 ✅ |
| Cuero de la maleta | [Poly Haven Fabric Leather 01](https://polyhaven.com/a/fabric_leather_01) | CC0 ✅ |

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

- **El logo**: hay una versión vectorial en
  [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Violet_Evergarden_logo.svg).
  El logo es **bilingüe**: katakana arriba y «VIOLET EVERGARDEN» en
  versalitas muy espaciadas debajo (visto en el tráiler
  [0:16](https://www.dailymotion.com/video/x7t0he2?t=16) y 1:26 y en el
  opening 1:24) ✅. **La parte en katakana** usa **本明朝 小がな
  (Honmincho Komana)**, un mincho comercial de Morisawa «de trazos que
  fluyen», según el análisis del CSS de la web oficial ⚠️ (una fuente:
  [わくぱく](https://wakupaku.hmup.jp/blog/blog/design-anime-violetevergarden)).
  Su equivalente libre: **Shippori Mincho** o **Zen Old Mincho** (OFL).
  **La parte latina** sigue sin identificar ⚠️: la aproximación libre es
  Cormorant Garamond o Playfair Display.
- **La web oficial** usa **Special Elite** en los títulos de página y
  **Merriweather** en el menú (misma fuente, わくぱく) ✅: Special Elite
  deja de ser «parecida a ojo» y pasa a ser **la letra real** de la
  franquicia para lo tecleado. Colores de esa web: fondo `#EFEED9`, texto
  `#B4832F`.
- **Cartelas de los tráileres**: frase en japonés en mincho blanco muy
  espaciado sobre negro, y la traducción en versalitas pequeñas debajo
  («ERA UN INSTRUMENTO / SIN CORAZÓN», tráiler [0:12](https://www.dailymotion.com/video/x7t0he2?t=12);
  «AÚN NO CONOCE / EL SIGNIFICADO DE "TE QUIERO"», 1:02 a 1:04) ✅.
  **Nombre de cada personaje** en pantalla: katakana en mincho con «cv» y
  el actor debajo, pegado a un lado del plano (tráiler 0:22 a 0:36) ✅.
- **Las cartas en pantalla**: se ven **escritas a máquina, en el
  alfabeto inventado** de la serie (§6.3), no en letras latinas.
- **Subtítulos oficiales**: Netflix, letra de sistema. No sirven de estilo.

### 6.2 Letras libres comprobadas por mí

Bajé los archivos de [google/fonts](https://github.com/google/fonts) y
comprobé con fontTools que traen **á é í ó ú ñ Á É Í Ó Ú Ñ ¿ ¡ ü « »**.
**Todas las de la tabla las traen** ✅.

| Letra | Licencia | Para qué | Por qué |
|---|---|---|---|
| **Special Elite** | Apache 2.0 | **El texto escrito a máquina** (la hoja) | Máquina vieja con tinta irregular: la más parecida a una carta tecleada |
| **Courier Prime** | OFL | Texto a máquina largo | Más limpia y legible en el móvil |
| **Cutive Mono** | OFL | Texto a máquina fino | Máquina de oficina, trazo delgado |
| **Cormorant Garamond** | OFL | **Títulos** («Poemas») | Romana fina y elegante, cerca del tono del logo |
| **IM Fell English** | OFL | Rótulos de sobre, sellos | Imprenta antigua, con imperfecciones |
| **EB Garamond** | OFL | Texto impreso (partitura, programa de ópera) | Libro clásico |
| **Playfair Display** | OFL | Titular con más peso | Si Cormorant queda débil sobre foto |
| **Italiana** | OFL | Rótulo fino de una línea | Letras altas y delgadas |
| **Pinyon Script** | OFL | **Firmas** («Violet Evergarden») | Caligrafía de pluma |
| **Great Vibes** / **Lavishly Yours** | OFL | Dirección escrita a mano en un sobre | Letra inglesa de pluma |
| **Shippori Mincho** | OFL | Algún japonés (自動手記人形) | Mincho clásico, trae también las tildes; equivalente libre del logo en katakana |
| **Merriweather** | OFL | Texto largo impreso, alternativa a EB Garamond | **La usa la web oficial** en el menú; tildes, ñ, ¿ y ¡ comprobados con fontTools ✅ (2.ª pasada) |
| **Zen Old Mincho** | OFL | Japonés de título | Mincho clásico, alternativa a Shippori ⚠️ (tildes sin comprobar) |

### 6.3 El alfabeto inventado de la serie

- La escritura del mundo se llama **tellsis**; los fans la llaman
  **«nunkish»**. Es **una letra por cada letra del inglés** (un cifrado
  sencillo). En el opening, las teclas de la máquina coinciden con las de
  un teclado inglés, y así se descifró ✅
  ([Omniglot](https://www.omniglot.com/conscripts/nunkish.htm),
  [traductor en Python de Teck](https://teck78.blogspot.com/2021/01/telsis-language-nunkish-translator.html),
  [GamezaVon/NunkishTranslation](https://github.com/GamezaVon/NunkishTranslation),
  [Pawitsapak/Conlang-Nunkish](https://github.com/Pawitsapak/Conlang-Nunkish)).
- En Bilibili hay un artículo que traduce **lo que Violet escribe de
  verdad** en las cartas: [«薇尔莉特到底写了什么？»](http://www.bilibili.com/read/cv142910) ⚠️ (en la 2.ª pasada tampoco cargó: dos intentos).
- En el opening el alfabeto sale **como tiza clara sobre negro**,
  flotando (0:09 a 0:12 y 1:21 a 1:24, hoja escenas nº6), y en el ep. 1 la
  pluma de Violet lo escribe temblando (hoja escenas nº16) ✅.
- Los fans que lo tratan como idioma lo escriben **Tellsis** (el
  continente se llama テルシス): [traductor de Kairi003](https://kairi003.github.io/tellsis-translator/)
  y la letra [«テルシス大陸フォント»](https://www.pixiv.net/en/artworks/76979667) en Pixiv ✅.
- **Letra de fans**: [JxpoemYui/violet-evergarden-font](https://github.com/JxpoemYui/violet-evergarden-font),
  hecha por 汐月Jxpoem (Bilibili). **Sólo trae A-Z, a-z y 0-9**: **sin
  tildes, sin ñ, sin signos**. Licencia del README: uso libre, pero **no
  redistribuir, no modificar, no uso comercial sin permiso**. Para una
  lámina de un servidor sin ánimo de lucro vale **como adorno**
  (la cabecera de la carta, el rótulo de una tecla), **nunca para el
  texto que hay que leer**.
- Otra letra citada en el foro de la wiki, **abierta en la 2.ª pasada**:
  [«テルシス語フォント (ブロック体＋筆記体)»](https://booth.pm/ja/items/1979406)
  en booth.pm ✅. **Gratis (¥0)**, hecha a mano copiando el cuadernillo
  del Blu-ray, con versión de bloque y otra cursiva. **No dice licencia**:
  igual que la de JxpoemYui, **sólo de adorno**, nunca para texto que haya
  que leer ni para redistribuir.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que la serie pone en pantalla

- **No hay globos.** La obra es novela ligera y anime; **no hay manga
  oficial** ✅ (2.ª pasada: las tres entradas «manga» de AniList tienen
  `format: NOVEL`; la novela es de Kana Akatsuki con ilustraciones de Akiko
  Takase, en KA Esuma Bunko: [KyoAni](https://www.kyotoanimation.co.jp/books/violet/books/)).
- **La carta es el cuadro de diálogo.** Cuando alguien escribe, **se oye
  su voz leyendo la carta** mientras se ven imágenes. En los subtítulos
  japoneses de Netflix esas líneas van **entre comillas “ ”**, y las
  cartas de la madre de Ann (ep. 10) entre **〝 〞** ✅ (lo ves en §2).
- La hoja **en la máquina**: papel crema, texto tecleado con tinta
  oscura, en el alfabeto inventado ✅.
- **El sobre**: se ven sellos de lacre y la saca del cartero ⚠️ (de
  memoria). En la 2.ª pasada sólo se halló una pista indirecta: sellos de
  lacre de «Violet Evergarden» vendidos como merchandising
  ([Etsy](https://www.etsy.com/listing/775900036/30mm-violet-evergarden-wax-seal-stamp)).
  En el vídeo del ending, la carta se cierra con **lacre rojo** (§11), pero
  es acción real, no la serie ⚠️.
- Los **pensamientos** de Violet no salen en recuadro: se dicen en voz en
  off o no se dicen. Su cara casi no se mueve; la emoción va en **los
  ojos y las manos** ✅ (2.ª pasada): el director Taichi Ishidate decidió
  que **Violet no parpadee** («parpadear la haría parecer tonta, porque
  casi no tiene expresión») y que **mire a la gente de frente**, no de
  reojo ([entrevista del Fanbook, ATMA & Funomena](https://atmafunomena.wordpress.com/2018/08/26/violet-evergarden-interviews-taichi-ishidate-earnestness-immersion-subtlety/)).

### 7.2 Cómo hablan (según el subtítulo)

- **Violet** habla como **un soldado que da parte**: frases cortas y
  formales. En los subtítulos de la serie cuento **«了解しました»
  (entendido) 17 veces**, «問題ありません» (no hay problema) 10 veces y
  **«少佐» (el Mayor) 109 veces** ✅. Se presenta siempre igual:
  «お初にお目にかかります」+ el saludo del servicio (6 veces) ✅. Llama
  a la máquina **«arma»**: «Lo increíble es **esta arma**» (ep. 2,
  00:08:21) ✅; y a los borradores de letra, «**muchas armas**»
  (Especial, 00:14:14) ✅.
- **Hodgins** la llama **«ヴァイオレットちゃん»** (Violet-chan, cariñoso)
  27 veces en la serie ✅. Tono de tío bromista.
- **Cattleya**: segura, un poco burlona, de hermana mayor: «ヴァイオレット
  あなた 私に借りができたわね» («Violet, me debes una», ep. 5,
  00:22:04) ✅.
- **Benedict**: rezonga («何だよ！», «¿Qué pasa?») y presume ✅.
- **Iris**: se queja en voz alta («あーあ 今日も一日中 宛名書きか»,
  ep. 2, 00:06:12) ✅.

### 7.3 Cómo se traduce a una lámina fija

1. **La hoja en la máquina** es el cuadro principal: el texto del canal,
   tecleado, en **Special Elite** sobre papel crema. El papel **sale del
   rodillo y se curva**. Eso ya es de la serie; no hace falta globo.
2. **Una tarjeta o sobre** para la frase del personaje, con su firma en
   **Pinyon Script**.
3. **Sellos de correos** para las etiquetas (como los sellos con marco
   de Japan Post, §3.2).
4. La cabecera de la carta en **alfabeto inventado**, como adorno, con
   la traducción debajo en letra normal.
5. Comillas **« »** para lo que alguien «lee en voz alta».

### 7.4 En los videojuegos de la franquicia

**No hay videojuego oficial** ✅ (no aparece ninguno en la búsqueda; en la
2.ª pasada tampoco en japonés «公式ゲーム アプリ ノベルゲーム» ni en The
Cutting Room Floor, que no tiene página de la serie; sólo
modelos de fans en [VRoid Hub](https://hub.vroid.com/en/characters/7071143261300970946),
un [mundo de VRChat](https://en.vrcw.net/world/detail/wrld_0cb37037-834e-413a-bc9a-6b9d1537a7eb),
una [novela visual de fans](https://gbatemp.net/threads/project-violet-evergarden-vn-game-fan-made.504221/)
y el juego de fans [«The Letter»](https://www.youtube.com/playlist?list=PLniVpZLlVRvpoeJPluxsmughWGfUvV4o4)).
**No hay caja de diálogo de juego que copiar**: el cuadro es la carta.

### 7.5 Qué NO hacer con el texto

- **Una burbuja blanca de cómic.** En esta serie no existe.
- **Texto en el alfabeto inventado que haya que leer**: nadie lo lee y
  la letra no trae tildes.
- Letra de ordenador moderna (Arial, Helvetica) en la hoja: rompe la época.
- Papel blanco puro y tinta negra pura: todo es **crema y casi negro**.
- Poner en boca de Violet una frase alegre con exclamaciones: ella habla
  **en calma y con formalidad**.

---

## 8 · Los personajes

Voces japonesas del Blu-ray 1: 石川由依, 子安武人, 浪川大輔, 遠藤綾,
内山昂輝, 茅原実里, 戸松遥 ✅ ([Amazon.co.jp](https://www.amazon.co.jp/%E3%83%B4%E3%82%A1%E3%82%A4%E3%82%AA%E3%83%AC%E3%83%83%E3%83%88%E3%83%BB%E3%82%A8%E3%83%B4%E3%82%A1%E3%83%BC%E3%82%AC%E3%83%BC%E3%83%87%E3%83%B31-Blu-ray-%E7%9F%B3%E5%B7%9D%E7%94%B1%E4%BE%9D/dp/B078XH1JDL)).
Quién es quién abajo; lo que no tiene fuente va con ⚠️.

### Violet Evergarden (ヴァイオレット・エヴァーガーデン) — la protagonista y la más querida

- **Quién es**: una chica que **fue soldado de niña**. A Gilbert se la
  dieron como **«arma»** (ep. 1, 00:02:43) ✅. **Perdió los dos brazos**
  en la guerra y lleva **prótesis de metal plateado** de la compañía
  Esterk, fuertes para el combate y **tan precisas que puede teclear a
  ciegas** ✅ ([wiki](https://violet-evergarden.fandom.com/wiki/Violet_Evergarden_(anime_character)),
  resumen de búsqueda). Voz japonesa: **Yui Ishikawa** ✅.
- **Qué busca**: entender la última frase del Mayor, **«愛してる»**
  («te quiero»). «Quiero saber qué es "te quiero"» (ep. 1, 00:22:36; ep. 3,
  00:14:34; ep. 9, 00:11:33) ✅. Por eso se hace Doll.
- **Su nombre**: se lo puso Gilbert (ep. 4, 00:21:21) ✅. Violeta es una
  flor; en la película le dicen «sé una persona que esté a la altura de
  su nombre» (película, 00:11:20) ✅.
- **Miedos y culpa**: «Yo, que maté gente como un arma, ¿puedo vivir
  así? ¿No le quité a alguien su "algún día"?» (ep. 7, 00:19:16) ✅.
- **Qué le importa**: al principio, **las órdenes** («命令», 33 veces en
  los subtítulos) ✅; luego, **el corazón de quien le pide la carta**.
- **Cómo se expresa**: frases cortas, formales, sin adornos (§7.2).
  **Casi no sonríe**; su sonrisa es pequeña y llega tarde en la serie ✅
  (2.ª pasada: capturas de los eps. 5 y 9, abajo). No grita: la única vez
  que alza la voz es «¡Quiero saber qué es "te quiero"!» (ep. 1,
  00:21:29) ✅. Cuando se rompe, llora **sin desfigurar la cara** ✅. Explica las cosas
  como un informe: primero el dato, luego la conclusión («Era distinto
  de una carta normal… me costó alabarlo», película, 00:13:35) ✅.
- **Cómo saluda**: «Encantada. Allá donde el cliente lo desee, acudiré.
  Servicio de Auto Memory Dolls, Violet Evergarden» ✅, con una
  **reverencia formal** ⚠️ (de memoria: comprobar el gesto en el ep. 13,
  00:23:17).
- **Lenguaje corporal**: **espalda recta** ✅ (Takase cuidó «cómo se
  mantiene erguida», §3.3); **no parpadea y mira de frente** ✅ (Ishidate,
  §7.1). De memoria ⚠️: manos juntas delante, pasos medidos, teclea muy
  rápido y sin mirar, se toca el **broche** cuando piensa en el Mayor.
- **Nuevo (2.ª pasada) · Su cara en cada emoción** (capturas reales de la
  wiki, miradas):
  - **Alegría**: sonrisa breve, boca cerrada, ojos entornados:
    [«Violet's smile.jpg»](https://static.wikia.nocookie.net/violet-evergarden/images/2/2a/Violet%27s_smile.jpg)
    (1274×714, ep. 5, lazo rojo y cielo) y
    [«Violet smile ep9.png»](https://static.wikia.nocookie.net/violet-evergarden/images/f/f1/Violet_smile_ep9.png)
    (540×304, ep. 9, de perfil, luz de interior) ✅.
  - **Tristeza**: [«Violet crying.jpg»](https://static.wikia.nocookie.net/violet-evergarden/images/8/8f/Violet_crying.jpg)
    (1280×720): lágrimas en las mejillas, boca cerrada, broche a la vista
    ✅; episodio exacto ⚠️. Y en la oficina, ep. 10, clip
    [3:10](https://www.dailymotion.com/video/x80vbaj?t=190) ✅.
  - **Vergüenza o torpeza**: [«Violet awkward smile.jpg»](https://static.wikia.nocookie.net/violet-evergarden/images/0/07/Violet_awkward_smile.jpg)
    (700×394): **se empuja las comisuras con los dedos** para fabricarse
    una sonrisa ✅. Resume el personaje: aprende a sentir practicando el
    gesto.
  - **Miedo**: no hay captura etiquetada ⚠️. Lo más cercano: sus ojos muy
    abiertos en la batalla del tráiler ([0:44](https://www.dailymotion.com/video/x7t0he2?t=44)),
    tensión y no llanto.
  - **Rabia**: **no encontré ninguna** escena de Violet furiosa. Su enfado
    es quietud tensa. **No dibujarle una cara de furia.**
- **Nuevo · Datos oficiales**: **161 cm**; cumpleaños **25 de septiembre**
  ✅ (Starter Book oficial, traducido en
  [dennou-translations](https://dennou-translations.tumblr.com/post/173583642499/violet-evergarden-starter-book-character-profiles),
  e infobox de la wiki). Al final **se casa con Gilbert** (la wiki la da
  como su esposa) ✅: no contarlo en la lámina, es el final.
- **Con quién aparece**: Gilbert (recuerdos), Hodgins, Cattleya,
  Benedict, Erica, Iris; en cada episodio, el cliente.

### Gilbert Bougainvillea (ギルベルト・ブーゲンビリア) — el Mayor

- Oficial del ejército, **el «少佐» de Violet** ✅. Le compró **el broche
  verde**, del color de sus ojos (ep. 1, 00:00:22; ep. 8, 00:14:06) ✅.
  Le dijo **«愛してる»** al final de la guerra (ep. 9, 00:02:38) ✅.
- Habla bajo y con cariño: «君は ここにいるんだ» («tú quédate aquí»,
  ep. 8, 00:07:23) ✅. Voz japonesa: **Daisuke Namikawa** ✅ (Doblaje Wiki;
  y «cv 浪川大輔» en pantalla, tráiler [0:56](https://www.dailymotion.com/video/x7t0he2?t=56)).
- **Nuevo (2.ª pasada)**: **185 cm, grupo O** (Starter Book + wiki) ✅✅;
  **29 años** (novela, tomo 2, cap. 5) ✅. Pelo **azul muy oscuro** y ojos
  **verdes** (hoja 1 nº12, 26, 31; Danbooru `blue_hair`, `green_eyes`) ✅.
  En la película lleva **parche en un ojo** (hoja 2 nº59). Caras por
  emoción: la wiki no tiene capturas etiquetadas ⚠️.
- Sale sobre todo en **recuerdos**. Para #poemas **no es buen narrador**:
  su papel es ser **el destinatario** de las cartas de Violet.

### Claudia Hodgins (クラウディア・ホッジンズ) — el jefe

- Fundó y dirige la **compañía postal C.H.** en Leiden ✅
  ([wiki](https://violet-evergarden.fandom.com/wiki/C.H_Postal_Company)).
  **Amigo de Gilbert desde la Academia Militar** ✅ (Fanbook oficial,
  [dennou-translations](https://dennou-translations.tumblr.com/post/184406019584/violet-evergarden-official-fanbook-character),
  y wiki); tutor de Violet ⚠️.
- **Nuevo (2.ª pasada)**: **192 cm, grupo A** ✅✅ (Starter Book + wiki). Pelo
  **rojizo con coleta**, barba de pocos días (tráiler [0:22](https://www.dailymotion.com/video/x7t0he2?t=22);
  Danbooru `red_hair`, `stubble`, `ponytail`) ✅.
- La llama **«ヴァイオレットちゃん»** ✅. Bromista, cariñoso, un poco
  payaso: el meme de los **tres muñecos de animales** («¡elige uno ya,
  que se acaba el mundo!») sale de él ✅
  ([TV Tropes, momentos graciosos](https://tvtropes.org/pmwiki/pmwiki.php/Funny/VioletEvergarden)).
- Frase clave: «**燃えてるよ**» («estás ardiendo», ep. 1, 00:18:10) ✅:
  Violet no sabe que está herida por dentro.
- **Para #poemas**: **escribe un haiku** en el especial (00:13:19) ✅.
  Es el más «poeta aficionado» de la oficina.
- Voz japonesa: **Takehito Koyasu** (子安武人) ✅ (lista del Blu-ray y
  «cv 子安武人» en pantalla en el tráiler, 0:22).

### Cattleya Baudelaire (カトレア・ボードレール) — la Doll estrella

- La Doll **con más trayectoria** de C.H., **especialista en cartas de
  amor** ✅ (Fanbook oficial). **Pelo negro largo, chaqueta roja,
  colgante rojo**, elegante ✅ (tráiler [0:32](https://www.dailymotion.com/video/x7t0he2?t=32)).
  **167 cm, grupo B** ✅✅. Hace de **hermana mayor** de Violet.
- **Su cara de fastidio**: [«Angry Cattleya.png»](https://static.wikia.nocookie.net/violet-evergarden/images/6/66/Angry_Cattleya.png)
  (1366×768): boca tensa, ceja alzada, mira de lado. Es la pelea con
  Benedict del ep. 3, 00:20:03 a 00:20:13 («¡este tonto puso un vaso
  mojado sobre la carta que escribí!») ✅✅.
- Defiende el oficio: la máquina es un arma «**para que las mujeres que
  trabajamos luchemos en la sociedad**» (ep. 2, 00:08:25) ✅.
- **Para #poemas**: es **la lectora crítica**. En el especial lee los
  borradores y comenta: «Qué corto» (00:13:31, sin nombre en el
  subtítulo ⚠️), «…¿y esto qué es?» (00:13:45, tras leer en voz alta la
  hoja de Benedict, 00:13:40 ✅). Es la que mejor dice «**comenta el texto**».
- Se pelea con Benedict y luego toman el té juntos (meme) ✅ (TV Tropes).
- Voz japonesa: **Aya Endō** ✅ (lista del Blu-ray y «cv 遠藤綾» en el
  tráiler, 0:32). Voz latina: **Carla Castañeda** ✅ (§10).

### Benedict Blue (ベネディクト・ブルー) — el cartero

- **Repartidor** de C.H. y compañero de Violet ✅
  ([ねとらぼ](https://nlab.itmedia.co.jp/research/articles/694099/)).
  Guapo, seco pero honrado y amable ✅ (misma fuente). Lleva **botas de
  tacón** ⚠️ (el título de la entrevista de Takase habla de «High Heels»).
- **Nuevo (2.ª pasada)**: **rubio**, camisa blanca con **tirantes** (tráiler
  [0:28](https://www.dailymotion.com/video/x7t0he2?t=28)) ✅; **obsesionado
  con la moda, no usa el uniforme oficial** de cartero ✅ (Fanbook).
  **172 cm, grupo O** ✅✅.
- Gruñón: «何だよ！ 何で俺がお茶を» («¿Y por qué tengo que hacer yo el
  té?», ep. 13, 00:22:32) ✅.
- **Para #poemas**: en el especial propone «**¡hacemos nosotros la mejor
  letra!**» y escribe «Esto es el infierno, no hope / sin ti, no future:
  ¡el grito de mi alma!» (00:12:47 a 00:13:50) ✅. En la película:
  «el himno al mar sólo lo escribe quien es elegido» (00:14:05) ✅.
- **2.º en la encuesta de fans de 2022** y **3.º en la de 2021** de
  ねとらぼ ✅✅ (§9): **el secundario más querido**.
- Voz japonesa: **Kōki Uchiyama** ✅ («cv 内山昂輝» en el tráiler, 0:28;
  ([BTVA](https://www.behindthevoiceactors.com/characters/Violet-Evergarden/Cattleya-Baudelaire/), resumen).

### Erica Brown (エリカ・ブラウン) — la Doll que quería ser escritora

- Doll insegura. **Narra el origen del oficio** y confiesa que la
  **novela de la Sra. Orland** le hizo temblar el corazón; recuerda **su
  sueño olvidado** (ep. 2, 00:20:36 a 00:20:49) ✅.
- **Para #poemas**: es **la persona que escribe en el foro sin atreverse
  a publicar**. Perfecta para una frase de ánimo. Voz japonesa: **Minori
  Chihara** ✅ (lista del Blu-ray y «cv 茅原実里» en el tráiler,
  [0:36](https://www.dailymotion.com/video/x7t0he2?t=36); también canta el
  ending).
- **Nuevo (2.ª pasada)**: pelo castaño corto y **gafas redondas** (tráiler
  0:36) ✅; **155 cm, grupo AB**, la más baja ✅✅. El Starter Book dice que
  «**se preocupa por dentro en cada trato con un cliente y no tiene
  confianza en sí misma**» ✅.

### Iris Cannary (アイリス・カナリー) — la Doll joven

- Ambiciosa y quejica ✅ (ep. 2, 00:06:12). Viaja a su pueblo en el ep. 4
  ✅ (subtítulo 00:05:23). En la película: «**¡El año que viene el himno
  lo escribo yo!**» (00:14:02) ✅. Voz japonesa: **Haruka Tomatsu** ⚠️.
- **Nuevo (2.ª pasada)**: viene de **Kazaly** y quiere ser mujer
  independiente en la capital ✅ (Fanbook + ep. 2). **160 cm, grupo B** ✅✅.
  Pelo corto castaño claro, ojos ámbar, collar de cuentas turquesa (hoja 1
  nº13, 37-39; hoja 2 nº68) ⚠️ color sin medir. **Su cara de rabia**:
  [«Iris angry.jpg»](https://static.wikia.nocookie.net/violet-evergarden/images/d/d7/Iris_angry.jpg)
  (809×455): cejas muy fruncidas, dientes apretados. Es la cara más
  «de anime clásico» del reparto: sirve de **contraste** con Violet.

### Dinámicas para láminas en grupo (Nuevo, 2.ª pasada)

- **Cattleya y Benedict** se pelean y luego toman el té juntos ✅.
- **Hodgins** hace reír a toda la oficina (los muñecos) ✅; Cattleya se
  burla de él (hoja 2 nº57).
- **Violet y Erica** se parecen: ninguna se atreve al principio a escribir
  algo propio ✅.
- **Iris y Violet** chocan: Iris quiere que la vean; Violet no busca nada
  para sí misma ✅.

### Secundarios de un episodio que sirven a #poemas

| Personaje | Episodio | Por qué sirve |
|---|---|---|
| **Irma Felice** (soprano) | Especial; película | Canta la letra de Violet. **La letra de canción hecha persona** ✅ |
| **Oscar Webster** (dramaturgo) | ep. 7 | Escribe una obra a dos manos con Violet ✅ |
| **Rhodanthe** (instructora) | ep. 3 | «Rescata el corazón verdadero» ✅ |
| **Luculia** (compañera de escuela) | ep. 3 | Recibe la carta de una línea ✅ |
| **Charlotte** (princesa) | ep. 5 | Escribe **con sus propias palabras** ✅ |
| **Roland** (cartero viejo) | Especial | Enseña el almacén de cartas perdidas ✅ |
| **Dietfried** (hermano de Gilbert) | eps. 7-8 | «¿Con esas manos que quitaron tantas vidas vas a escribir cartas que unen a la gente?» (ep. 7, 00:18:34) ✅ |

---

## 9 · ¿Quién es el más querido?

| Encuesta | Resultado | Estado |
|---|---|---|
| ねとらぼ, 20 may. a 2 jun. 2021 (fans, Japón) | **1.º Violet, 3.382 votos, 53,8 %** | ✅ ([ねとらぼ](https://nlab.itmedia.co.jp/research/articles/240645/), [Yahoo! Japón](https://news.yahoo.co.jp/articles/9b954425e1ed2618c02d97d25112667f57eec8bf)) |
| ねとらぼ 2022 (fans) | 1.º Violet; **2.º Benedict, 298 votos, 12,9 %** | ⚠️ una fuente ([ねとらぼ](https://nlab.itmedia.co.jp/research/articles/694099/)) |
| Ranker (fans, en inglés) | 1.º Violet, 2.º **Hodgins**, 3.º Benedict; entre las chicas: Violet, **Cattleya**, Iris | ⚠️ ([Ranker](https://www.ranker.com/list/best-violet-evergarden-characters/rowan-blake)) |
| みんなのランキング | Ranking de personajes y de «神回» (mejores episodios) | sin abrir ([personajes](https://ranking.net/rankings/best-violet-evergarden-characters), [episodios](https://ranking.net/rankings/best-violet-evergarden-kamikai)) |
| Encuesta **oficial** de Kyoto Animation | **No encontré ninguna** | — |

**Conclusión**: aquí **la protagonista es la más querida**, con mucha
diferencia. La lámina 1 va con **Violet**. Para dar calor y humor, los
secundarios con tirón son **Benedict, Hodgins y Cattleya**, que además
son **los que escriben letras en el especial**. El episodio favorito de
los fans es el **10** (las cartas de Ann), «el mejor de los mejores» ✅
([magmix](https://magmix.jp/post/48216), resumen de búsqueda de
みんなのランキング).

---

## 10 · Doblaje latino

**Estudio**: SDI Media de México (luego Iyuno-SDI Group) ✅
([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Violet_Evergarden),
[FULLTV](https://www.fulltv.com.ar/peliculas/violet-evergarden-la-eternidad-y-la-muneca-de-recuerdos-automaticos.html)).
**Dirección de la serie**: **Carla Castañeda** ✅ (Doblaje Wiki y la
descripción del vídeo [«Voces del doblaje latino»](https://www.youtube.com/watch?v=wEgiayIdKR4)).
Especial: Carla Castañeda, Mireya Mendoza y Gabriela Garay ⚠️; película:
Carla Castañeda, Briana González y Gabriela Garay ⚠️ (sólo Doblaje Wiki).
Netflix la estrenó el 11 de enero de 2018 en varios países y el 5 de
abril en México ⚠️ (Doblaje Wiki).

| Personaje | Voz latina | Fuentes | Estado |
|---|---|---|---|
| **Violet** (serie y especial) | **Andrea Arruti** | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Violet_Evergarden_(personaje)), [Código Espagueti](https://codigoespagueti.com/noticias/cultura/fallecio-andrea-arruti-la-voz-latina-de-violet-evergarden-y-neeko-en-league-of-legends/), [Spoiler](https://spoiler.mx/noticia/fallece-andreaarruti-la-voz-latina-de-violetevergarden/) | ✅ |
| **Violet** (Gaiden, película, Recuerdos; y un *loop* del ep. 10) | **Nycolle González** | Doblaje Wiki, [Somos Kudasai](https://somoskudasai.com/noticias/netflix-revela-un-avance-con-doblaje-al-espanol-de-violet-evergarden-the-movie/), [Multianime](https://multianime.com.mx/2020/03/22/violet-evergarden-eternity-and-the-auto-memory-doll-si-se-estrenara-en-netflix-con-doblaje-latino-escuchalo-aqui/) | ✅ |
| **Claudia Hodgins** | **Carlos Hernández** | Doblaje Wiki, noticia del tráiler de la película | ✅ |
| **Cattleya Baudelaire** | **Carla Castañeda** | Doblaje Wiki, [Anime-Planet](https://www.anime-planet.com/people/carla-castaneda) | ✅ |
| **Gilbert Bougainvillea** | Alejandro Orozco | sólo páginas de Doblaje Wiki | ⚠️ |
| **Dietfried** (película) | Irwin Daayán | una noticia del tráiler | ⚠️ |
| **Benedict Blue** | Alan Fernando Velázquez | sólo Doblaje Wiki | ⚠️ |
| **Erica Brown** | Alondra Hidalgo | sólo Doblaje Wiki | ⚠️ |
| **Iris Cannary** | Andrea Orozco | sólo Doblaje Wiki | ⚠️ |

> [!note] Andrea Arruti
> Murió el **1 de enero de 2020**, a los 21 años ✅ (Doblaje Wiki;
> [Manga México, enero de 2020](https://mangamexico.blogspot.com/2020/01/fallecen-andrea-arruti-y-edilu-martinez.html)).
> Para los fans latinos **su voz es la de Violet**. Si la lámina cita una
> frase de la serie, es su voz; si es de la película, la de Nycolle.
> Trátalo con respeto: nada de chistes.

**Frases del doblaje latino**: **no encontré ninguna con fuente**. Clips
latinos para escucharlas (sin minuto, no pude verlos):
[«Violet y Gilbert confesión»](https://www.youtube.com/watch?v=7ZtkUmEUQSM),
[«Violet escribe una carta para Yuris»](https://www.youtube.com/watch?v=DlJ16gt7VHU),
[«Las cartas para Ann»](https://www.youtube.com/watch?v=eLbGi4ulk_s),
[tráiler latino vs. castellano](https://www.youtube.com/watch?v=smYaAOrzuMk),
[«Analizando el doblaje: Violet»](https://www.youtube.com/watch?v=QmGE_NpUstI).
Hay un **«Reto doblaje: sé Violet Evergarden»** en
[TikTok](https://www.tiktok.com/@_taniadubs_/video/7279503802078743841):
la escena se usa como prueba de voz, cosa que encaja con un servidor
de doblaje.

**Palabras que hay que comprobar en el audio latino antes de rotular** ⚠️:
cómo dice «Auto Memory Doll» (Netflix titula «muñeca de recuerdos
automáticos»), cómo dice «少佐» (¿«Mayor»?) y la frase del saludo.

---

## 11 · Música

| Tema | Quién | Ambiente | Fuente |
|---|---|---|---|
| **Opening «Sincerely»** | **TRUE** (Miho Karasawa, letra); música de Shota Horie, arreglos con Evan Call | Crece desde un piano hasta cuerdas enormes: esperanza | ✅ [IMDb](https://www.imdb.com/title/tt8044824/soundtrack/), [UtaTen](https://utaten.com/lyric/qk18011109/) |
| **Ending «みちしるべ» (Michishirube)** | **Minori Chihara** (letra y voz); música de Daisuke Kikuta | Balada lenta, de despedida | ✅ IMDb, [ticketjam](https://ticketjam.jp/magazine/music/anison/118173/2) |
| **Inserto «Letter»** | **TRUE**; letra escrita «como Violet», cantada «como Irma» | **Aria de ópera**; es la letra del especial | ✅ [uta-net](https://www.uta-net.com/song/246452/), [X de TRUE](https://x.com/miho_karasawa/status/1231569784153620480) |
| **Película: «WILL»** | **TRUE** | Cierre luminoso | ✅ resumen de búsqueda (IMDb, Wikipedia) |
| **Banda sonora** | **Evan Call**. Álbum **«Automemories»**; hay edición en vinilo | Orquesta de cuerdas y piano, muy de cine; tema principal «Theme of Violet Evergarden» | ✅ [Internet Archive](https://archive.org/details/violet-egard-ost), [Light in the Attic](https://lightintheattic.net/products/violet-evergarden-original-soundtrack), [Spotify](https://open.spotify.com/track/0fsb37XCuEDiF1oPNq4arG) |
| Tema del Gaiden | — | — | **no lo verifiqué** |

Un vídeo en español analiza **cómo la banda sonora usa la máquina de
escribir**: [«Violet Evergarden y la Máquina de escribir - Análisis de la
OST»](https://www.youtube.com/watch?v=b9I7J8j7Grk) ⚠️ (sin ver).

**Para la lámina**: el ambiente es **«Letter»** (una letra convertida en
canción) o el piano de «Theme of Violet Evergarden». Nada de rock.

---

## 12 · Vídeos

No pude abrir YouTube ni TikTok: **no doy minutos de los vídeos**, sólo
de los episodios (§2). Lo que hay, por si alguien con red los mira:

**Oficiales**
- [制作風景 第5弾「3DCG」](https://www.youtube.com/watch?v=Ux9u5Zmi3zI): cómo se anima la máquina.
- Emisión del «特別編集版» en Kinro (TV japonesa), oct. 2021:
  [Famitsu](https://www.famitsu.com/news/202110/29239030.html).

**Análisis en español**
- [El poder de las cartas | Violet Evergarden en menos de 5 minutos](https://www.youtube.com/watch?v=kOYOUcmP8VY)
- [Análisis del capítulo 10](https://www.youtube.com/watch?v=wfgCTOnBuQU)
- [La carta de la madre | escena](https://www.youtube.com/watch?v=0vBnVJM0ves)

**Canciones de fans en español** (la gente **escribe letras** sobre
Violet: justo lo que se cuelga en #poemas)
- [LKZ - «Cartas» (Violet Evergarden) feat. Anny](https://www.youtube.com/watch?v=Qrdu_22GhcE)
- [Chrono - «CARTAS» (Violet)](https://www.youtube.com/watch?v=Bg1ssY9xel8)
- [«Letter» en español latino, Emanuel Santiago](https://www.youtube.com/watch?v=o_gW7LBx4eM)

**TikTok**
- Ediciones con el opening «Sincerely», con subtítulos en español:
  [@gato_traductor_](https://www.tiktok.com/@gato_traductor_/video/7335631799827156229);
  versión en violín: [@little_violin](https://www.tiktok.com/@little_violin/video/7186243054683114758).
- Plantillas de «guion» de Violet: [búsqueda de TikTok](https://www.tiktok.com/discover/violet-evergarden-script-template?lang=en).
- El reto de doblaje: ver §10.

**Otros idiomas**
- Coreano: [바이올렛 에버가든 명언 시리즈](https://www.youtube.com/watch?v=25xRZqLGnJQ) (frases célebres).
- Chino: [«看完紫罗兰永恒花园买了一台打字机»](https://www.bilibili.com/video/BV1wQ4y1N7wy/) («Vi la serie y me compré una máquina»).

---

## 13 · Videojuegos de la franquicia

**No existe ningún videojuego oficial** ✅ (ver §7.4). Sólo proyectos de
fans. **Consecuencia para la lámina**: no hay interfaz ni caja de juego
que copiar. El «interfaz» de esta serie es **el papel**.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### Lo que todos reconocen

- **La máquina de escribir y las manos de metal** tecleando. Hay quien
  **se compró una máquina** tras ver la serie ✅ (§4.1).
- **El broche verde** en el cuello: el color de los ojos del Mayor ✅.
- **«愛してる»** («te quiero»): la pregunta de toda la serie ✅.
- **El ep. 10** (las 50 cartas de la madre para Ann): «el mejor de los
  mejores» ✅. Es el episodio con el que todos lloran.
- **Violet cruzando el lago con el paraguas** (ep. 7) ⚠️ (muy citado de
  memoria; no encontré una encuesta).
- El saludo **«Allá donde el cliente lo desee, acudiré»** ✅ (se repite
  en casi todos los episodios).
- El humor de oficina: **Hodgins y los tres muñecos**, **Cattleya y
  Benedict discutiendo y luego tomando el té**, Violet **leyendo con cara
  seria una carta de amor desastrosa** ✅
  ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Funny/VioletEvergarden)).
- **La animación**: se la cita como una de las más bonitas de Kyoto
  Animation; en Japón fue muy votada en encuestas de KyoAni ⚠️
  ([Honey's Anime](https://honeysanime.com/what-is-your-favorite-kyoani-anime-japanese-poll-celebrates-violet-evergarden-the-movie-release/)).

### Un tema delicado: el incendio de Kyoto Animation

El **18 de julio de 2019** un hombre prendió fuego al Estudio 1 de Kyoto
Animation: murieron **36 personas** ✅
([Variety](https://variety.com/2019/film/news/kyoto-arson-attack-kyoto-animation-studios-reactions-1203272657/),
[ANN](https://www.animenewsnetwork.com/news/2019-10-18/kyoto-animation-president-27-of-33-injured-staff-have-returned-to-work/.152377)).
El Gaiden se retrasó y **puso en sus créditos los nombres de todas las
víctimas** ✅ ([SoraNews24](https://soranews24.com/2019/09/06/kyoto-animation-to-release-full-list-of-arson-attack-victim-names-in-credits-of-new-anime-movie/)).
Para muchos fans, Violet es también **un homenaje a ese equipo**.
**Nunca** usar fuego, humo o incendios como adorno en esta lámina.

### Qué NO hacer (lo que un fan notaría)

- **Una burbuja blanca**. El diálogo de esta serie es **una carta**.
- **Manos de carne**. Sus manos son **de metal**; suele llevar **guantes
  marrones** encima. Si se ven, son plateadas con juntas oscuras.
- **Broche de otro color** o sin broche en el traje de Doll.
- **Un teclado moderno** o una máquina gris de oficina de los años 60: la
  suya es **pequeña y portátil, de cuatro filas de teclas redondas**,
  de los años veinte, y viaja en su maleta (el color exacto ⚠️:
  comprobar en la hoja de modelo).
- **Violet sonriendo de oreja a oreja**, guiñando un ojo o en pose
  «kawaii». Es seria y serena.
- **Colores chillones** o neón. La serie es luz dorada, crema, azul y verde.
- Llamar a Gilbert «su novio» o dar por hecha la historia de amor con
  un chiste: el vínculo es serio y doloroso.
- **Chistes sobre sus brazos, la guerra o el incendio**.
- Mezclar el traje de Doll con el uniforme militar de niña.
- Escribir el texto del canal en el alfabeto inventado.

---

## 15 · Poses analizadas por personaje

El **minuto y lo que se dice** salen del subtítulo ✅. **La postura, las
manos y la mirada** las describo de memoria ⚠️: hay que mirar el
fotograma antes de recortar. Para qué sirve cada una va en la última
columna (presentar, explicar, celebrar, regañar, pensar, animar).

### Violet

| # | Escena | Minuto | Qué pasa (subtítulo) | Postura ⚠️ | Sirve para |
|---|---|---|---|---|---|
| 1 | ep. 13 | 00:23:17 a 00:23:31 | «Encantada… acudiré… Violet Evergarden» | De pie en la puerta, traje de Doll, reverencia formal, manos juntas delante | **Presentar** |
| 2 | ep. 2 | 00:08:21 | «Lo increíble es esta arma» (la máquina) | Sentada a la máquina, espalda recta, manos de metal sobre las teclas | **Explicar** |
| 3 | ep. 1 | 00:21:29 a 00:21:45 | «Aún me cuesta coger una pluma, pero puedo usar una máquina». «¡Quiero saber qué es "te quiero"!» | De pie ante Hodgins; la única vez que alza la voz | **Presentar** con fuerza |
| 4 | ep. 3 | 00:19:03 | Voz en off: «Gracias por estar vivo» | Luculia lee la carta; Violet detrás, quieta | **Presentar un texto corto** |
| 5 | ep. 5 | 00:15:08 | «Esta vez escriba usted. Con sus propias palabras» | Frente a la princesa, mirada firme | **Explicar** la norma |
| 6 | ep. 6 | 00:09:21 a 00:09:30 | «Las Dolls vamos a donde el cliente quiera… casi todo el año con la maleta en la mano» | Caminando con la **maleta** | **Explicar** |
| 7 | ep. 7 | 00:16:50 a 00:17:23 | Cruza el lago con el paraguas: «Creo que di tres pasos» | En el aire, **paraguas abierto**, falda al viento; luego empapada y seria | **Celebrar / animar** |
| 8 | Especial | 00:14:04 a 00:14:14 | «Gracias por tantas letras. He recibido muchas armas» | Con un **montón de hojas** en brazos | **Agradecer / celebrar** |
| 9 | Especial | 00:24:15 | «Yo, que no conozco el amor, ¿puedo ponerlo en palabras?» | Mirada baja, junto a Roland | **Pensar** |
| 10 | película | 00:13:35 a 00:13:54 | «Era distinto de una carta normal… me costó alabar al mar» | Ante sus compañeros, tras el festival | **Explicar** |

### Hodgins

| # | Escena | Minuto | Qué pasa | Postura ⚠️ | Sirve para |
|---|---|---|---|---|---|
| 1 | ep. 1 | 00:12:43 | Enseña la casa: «El 2.º piso es la oficina y el departamento de escritura» | Brazo extendido, guía | **Presentar** |
| 2 | ep. 1 | 00:13:38 | A Benedict, que le suelta «¿Qué pasa, jefe?»: «Ahí se dice "¿Qué desea, jefe?"» | Corrige medio en broma | **Regañar** (suave) |
| 3 | ep. 1 | 00:18:10 | «Estás ardiendo» | Serio, mirada triste | **Pensar** |
| 4 | Especial | 00:13:19 a 00:13:29 | Lee su haiku: «Te espero. / Sopla en el muelle / un viento frío» | Con la hoja en la mano, algo cortado | **Celebrar** (con humor) |
| 5 | Especial | 00:12:15 | «El encargo vino de la asociación de correos… creí que era una carta» (sin nombre en el subtítulo; por contexto, él) | Rascándose la cabeza | **Explicar** |
| 6 | película | 00:13:28 | «Se nota que te costó escribirlo» | Sonriente | **Animar** |

### Cattleya

| # | Escena | Minuto | Qué pasa | Postura ⚠️ | Sirve para |
|---|---|---|---|---|---|
| 1 | ep. 2 | 00:08:25 | «Un arma para que las mujeres que trabajamos luchemos en la sociedad» | Junto a la máquina de Violet, orgullosa | **Animar** |
| 2 | ep. 2 | 00:21:17 | «¡Terminé!» | Estirándose en su mesa | **Celebrar** (Terminado) |
| 3 | ep. 3 | 00:20:03 a 00:20:13 | «¡Este tonto puso un vaso mojado sobre la carta que escribí!» | Discutiendo con Benedict | **Regañar** |
| 4 | Especial | 00:13:31 | «Qué corto. ¿Sirve para una letra?» (línea sin nombre: probablemente ella) | Leyendo el haiku con una ceja alzada | **Comentar el texto** |
| 5 | Especial | 00:13:40 a 00:13:45 | Lee en voz alta el grito punk y dice «…¿y esto qué es?» | Hoja en alto, cara de asco | **Regañar** con humor |
| 6 | película | 00:13:23 | «El himno al mar estuvo muy bien, Violet» | Cálida | **Animar** |

### Benedict

| # | Escena | Minuto | Qué pasa | Postura ⚠️ | Sirve para |
|---|---|---|---|---|---|
| 1 | Especial | 00:12:41 a 00:12:58 | «¿No es fácil? ¡Hacemos nosotros la mejor letra!» | Apoyado en la mesa, seguro | **Animar** |
| 2 | Especial | 00:13:34 a 00:13:50 | «¡Mi turno! Obra maestra… ¡el grito de mi alma!» | Enseñando su hoja, orgulloso | **Celebrar** |
| 3 | Especial | 00:13:53 | «¿Qué pasa? ¿Tienes queja?» | A la defensiva | **Regañar** |
| 4 | ep. 13 | 00:22:32 | «¿Y por qué tengo que hacer yo el té?» | Rezongando | Humor |
| 5 | película | 00:14:05 | «El himno al mar sólo lo escribe quien es elegido» | Brazos cruzados ⚠️ | **Explicar** |
| 6 | ep. 1 | 00:16:24 | «Yo pensaba repartirlo mañana» | Con la saca de cartas | **Presentar** al cartero |

### Iris y Erica

| Quién | Escena | Minuto | Qué pasa | Sirve para |
|---|---|---|---|---|
| Iris | ep. 2 | 00:06:12 | «Otro día entero escribiendo direcciones» | Humor |
| Iris | película | 00:14:02 a 00:14:22 | «¡El año que viene lo escribo yo! Déjamelo a mí» | **Animar** a publicar |
| Erica | ep. 2 | 00:20:36 a 00:20:49 | «Mi sueño olvidado… como la novela de la Sra. Orland» | **Pensar** |

### Referencias de pose que no son fotogramas

- **Violet tecleando, tumbada / de lado**: fondo de
  [WallpaperFlare, 3840×2160](https://www.wallpaperflare.com/violet-evergarden-typewriter-mechanical-arm-lying-down-anime-wallpaper-bqxzu)
  («typewriter, mechanical arm, lying down»).
- **«Typing in Tranquility»**, 2268×1700:
  [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=902250).
- Escenas en Blender de fans con la máquina (§4.3).

---

## 16 · Vestuario

### Violet

| Traje | Cuándo | Cómo es | Estado |
|---|---|---|---|
| **Traje de Doll** (el icónico) | Serie, especial, película | **Vestido blanco** con lazo en el cuello; **chaqueta corta azul de Prusia**; falda blanca plisada de seda; **broche esmeralda** en el centro del lazo; **guantes marrones**; **botas altas de tacón, marrón oscuro** | ✅ ([wiki](https://violet-evergarden.fandom.com/wiki/Violet_Evergarden_(anime_character)) + [Core Cosplay](https://corecosplay.com/anime/violet-evergarden-cosplay-ideas/)) |
| Detalles de la chaqueta | — | Adornos blancos en los hombros; líneas negras a los lados de la falda | ⚠️ (guías de cosplay) |
| **Pelo de Doll** | Desde que es Doll | Rubio dorado hasta la cintura; **dos trenzas francesas enrolladas en moños**, con **dos lazos rojos** | ⚠️ (wiki) |
| Pelo antes | Hospital, ep. 1 | **Coleta baja con lazo negro**, o suelto | ⚠️ (wiki) |
| Uniforme militar | Recuerdos, eps. 8-9 | Uniforme del ejército de Leidenschaftlich ⚠️ | de memoria |
| Brazos | Siempre | **Prótesis plateadas** («torpes pero resistentes», dice ella) | ✅ (wiki, resumen) |

Takase explicó que el traje junta **rigidez militar y gracia femenina**
con el broche y el contraste azul-blanco ⚠️ (resumen de búsqueda, sin
cita exacta).

### Los demás ⚠️ (de memoria)

- **Hodgins**: traje de tres piezas claro, pelo castaño rojizo peinado
  hacia atrás.
- **Cattleya**: vestido oscuro ceñido, pelo negro ondulado, labios rojos.
- **Benedict**: uniforme de cartero con chaleco, pelo largo recogido,
  botas de tacón.
- **Iris**: pelo rojizo corto, vestido de Doll con tonos rosados.
- **Erica**: pelo oscuro, aire tímido.

---

## 17 · Paisajes y fondos de pantalla

### Los sitios, con su luz ⚠️

| Sitio | Hora y luz | Para qué lámina |
|---|---|---|
| Oficina de C.H., 2.º piso | Tarde; ventanal lateral; polvo en el aire | Concepto A |
| Mesa común de la oficina | Día; luz blanda | Concepto B |
| Casillero y sacas del correo (planta baja) | Mañana; luz fría de puerta abierta | Concepto C |
| Lago de Oscar (ep. 7) | Otoño, tarde dorada | Frase de ánimo |
| Almacén de cartas perdidas (Especial, 00:25:08) | Penumbra, haces de luz | Lámina 2 alternativa |
| Puerto de Leiden | Cielo claro, mar | Fondo exterior |

### Fondos de pantalla en alta

| Imagen | Tamaño | Dónde | Autor |
|---|---|---|---|
| Violet con la máquina y el brazo mecánico | 3840×2160 | [WallpaperFlare](https://www.wallpaperflare.com/violet-evergarden-typewriter-mechanical-arm-lying-down-anime-wallpaper-bqxzu) | sin dato |
| «Violet Evergarden — 4K» | 3840×2160 | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=961806) | ncoll36 (quien lo subió) |
| «Typing in Tranquility» | 2268×1700 | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=902250) | sin dato |
| Colección 4K (más de 100) | 3840×2160 o más | [AlphaCoders](https://alphacoders.com/violet-evergarden-4k-wallpapers) | varios |
| Colección 4K | varios | [Wallpaper Cave](https://wallpapercave.com/4k-violet-evergarden-wallpapers) | varios |

Casi todos son **capturas o arte oficial** subidos por fans: sirven de
referencia, no para pegar.

---

## 18 · Guía para generar con IA (Firefly, Canva)

**Úsala sólo para fondos, objetos o pruebas de pose**, nunca para
«inventar» a Violet: la cara y el traje se sacan de fotogramas reales.

**Rasgos que nunca cambian**
- Pelo **rubio dorado pálido**, largo, con **dos trenzas recogidas en
  moños y lazos rojos**; flequillo recto.
- Ojos **azules**, grandes; cara serena, **boca casi cerrada**.
- **Chaqueta corta azul de Prusia** sobre **vestido blanco** con lazo;
  **broche verde esmeralda** en el cuello.
- **Guantes marrones** o manos **de metal plateado** articuladas.
- Botas marrón oscuro.

**Estilo**
- Anime de **Kyoto Animation**, 2018: línea **fina y limpia**, muchos
  **reflejos en el pelo**, sombras suaves en dos tonos, **luz de tarde
  dorada**, polvo en el aire, desenfoque de fondo (bokeh).
- Ambiente: Europa de principios del siglo XX, oficina con madera oscura,
  papel crema, ventanales.

**Palabras que ayudan**
«Kyoto Animation style», «soft golden hour light through window», «dust
particles», «1920s portable typewriter», «cream paper», «emerald brooch»,
«Prussian blue cropped jacket», «white ribbon-tie dress», «mechanical
silver prosthetic hands», «calm expression», «shallow depth of field».

**Palabras que lo estropean**
«smiling», «cute», «chibi», «neon», «cyberpunk», «robot» (la vuelve un
androide), «doll» a secas (sale una muñeca de juguete), «modern
keyboard», «laptop», «speech bubble», «maid».

**Encuadre**: tres cuartos o de lado, trabajando (§3.3: así la mira la
serie). Plano medio con la máquina en primer término.

**Referencias de estilo**: el fondo de WallpaperFlare 3840×2160 y la
escena en Blender de D Arte (§4.3). **De pose**: la tabla de §15.

---

## 19 · Tres conceptos para la lámina de #poemas

Los tres usan los textos de §0. Las frases «en la voz de la serie» son
**traducción mía** del japonés, no del doblaje latino (no lo encontré).
Recortes siempre por `v3/integrar.py` y comprobados a 1:1.
**Ninguno lleva llamas** (ni velas encendidas ni chimenea): ver §14.

### Concepto A — «La hoja en la máquina» (el objeto del plan, mejorado)

- **Objeto y sitio**: **la máquina portátil de Violet**, abierta en su
  maleta, sobre su mesa del **2.º piso de C.H.** (ep. 1, 00:12:43), junto
  al ventanal, a última hora de la tarde. **Una hoja puesta en el
  rodillo**, que sale y se curva. Delante, **dos sobres**. En Blender:
  [Underwood 4-Bank portátil, CC BY](https://sketchfab.com/3d-models/underwood-4-bank-typewriter-portable-b872e2c3f4f7457796edebcb7c0a290e)
  (con su maleta), hoja con simulación de tela para la curva,
  [lacre CC0](https://sketchfab.com/3d-models/cc0-wax-seal-2-bd18fd7b6c1847bc8e7d9e779c122ed5),
  [sobre CC BY](https://sketchfab.com/3d-models/old-envelope-3189a8c84df44c5ab91e556736f291c1),
  mesa con [madera CC0](https://ambientcg.com/view?id=Wood026). Las
  teclas, con el alfabeto inventado (§6.3), como en la serie.
- **Personaje**: **Violet**, la más querida. Sentada a la máquina, de
  tres cuartos, **las manos de metal sobre las teclas** (§15, Violet 2:
  ep. 2, 00:08:21). Referencias: el fondo 3840×2160 de
  [WallpaperFlare](https://www.wallpaperflare.com/violet-evergarden-typewriter-mechanical-arm-lying-down-anime-wallpaper-bqxzu)
  y la escena en Blender de [D Arte](https://www.artstation.com/artwork/kQDZN0).
- **Cómo habla**: **la hoja es su voz**. El texto va tecleado en
  **Special Elite**, tinta casi negra sobre papel crema. Al pie, su firma
  en **Pinyon Script**. Frase gancho, tecleada como última línea:
  **«Una carta lleva el corazón de quien la escribe.»** (de ep. 3,
  00:08:23).
- **Dónde va cada texto**:
  - Membrete impreso arriba de la hoja, en **Cormorant Garamond**:
    **Poemas**.
  - Líneas tecleadas: **Un hilo por texto.** / **Poemas, letras,
    microrrelatos.** / **Aquí se lee despacio.** / **Si comentas, comenta
    el texto.**
  - Sobre abierto, con la carta asomando y un sello de correos:
    **Libre para usar**.
  - Sobre cerrado con **lacre rojo**: **No usar sin permiso**.
  - Firma: **Violet Evergarden**.
- **Para que no quede plano**: la hoja curvada **proyecta sombra** sobre
  las teclas; los dos sobres **desenfocados en primer plano**; luz de
  ventana rasante desde un lado que hace **brillar el metal de las manos
  y el broche**; motas de polvo en el haz; al fondo, mesas de otras
  Dolls en bokeh.
- **Lámina 2**: la misma mesa vista desde arriba, con **nueve sobres**,
  cada uno con su **sello de marco** (como los de Japan Post, §3.2): una
  etiqueta por sello.

### Concepto B — «La mesa de las letras» (el especial, con amigos)

- **Objeto y sitio**: la **mesa común de la oficina de C.H.** cubierta de
  **borradores de letra** (Especial, 00:13:19 a 00:14:14): hojas
  tecleadas, hojas a mano, la **partitura del aria** y tazas de té. En
  Blender: mesa, hojas sueltas con curvatura, partitura, tazas, un
  [lápiz CC0](https://sketchfab.com/3d-models/cc0-pencil-cb1b27db90eb469eb845017bb300b5d3).
- **Personajes**: **Violet** en el centro con el montón de hojas en brazos
  («He recibido muchas armas», §15 Violet 8); **Hodgins** con su haiku
  (§15 Hodgins 4); **Cattleya** leyendo con la ceja alzada (§15 Cattleya
  4); **Benedict** señalando orgulloso su hoja (§15 Benedict 2). Es la
  escena de grupo que el dueño pide: **con amigos y con su objeto**.
- **Cómo habla**: cada hoja es una voz. Violet habla en **una tarjeta**
  sobre el montón, tecleada: **«Gracias por tantas letras.»** (Especial,
  00:14:04). Cattleya comenta **a lápiz rojo** en el margen de una hoja.
- **Dónde va cada texto**:
  - Portada de la partitura, en **EB Garamond**: **Poemas**.
  - Nota clavada en la mesa: **Un hilo por texto**.
  - La hoja de Hodgins, con su haiku traducido («Te espero. / Sopla en el
    muelle / un viento frío»): etiqueta **Poema**, con un sello
    **Libre para usar**.
  - La hoja de Benedict («¡el grito de mi alma!»): etiqueta **Letra de
    cancion**, con sello **No usar sin permiso** (es muy suyo).
  - Tarjeta de una línea de Violet, «Gracias por estar vivo» (ep. 3):
    **Microrrelato** o **Frase suelta**.
  - La partitura en «lengua antigua» (Especial, 00:04:51): **Traduccion**.
  - Comentario de Cattleya a lápiz rojo: **Si comentas, comenta el texto**.
  - Taza de té con una nota: **Aquí se lee despacio**.
- **Para que no quede plano**: cámara **a la altura de la mesa**; hojas
  en primer plano **cayendo del borde**, desenfocadas; vapor de las
  tazas; los cuatro personajes **a distinta distancia**; luz de tarde
  desde atrás, que atraviesa el papel.
- **Uso ideal**: **lámina 2**, porque reparte las nueve etiquetas en
  hojas que ya existen en el episodio.

### Concepto C — «El casillero de C.H.» (Benedict, el cartero)

- **Objeto y sitio**: el **casillero de clasificar cartas** de la planta
  baja de C.H. (la parte de correos, §5.1), de madera, con **placas de
  latón** para los nombres y cartas asomando. Una **saca de cartero** en
  el suelo. En Blender es fácil: rejilla de cajones, placas, sobres
  instanciados. Versión más triste: el **almacén de cartas perdidas** del
  especial (00:25:08), con haces de luz.
- **Personaje**: **Benedict** (2.º en la encuesta de fans de 2022),
  metiendo una carta en su casilla, con la saca (§15 Benedict 6). Violet,
  más pequeña detrás, con su maleta (§15 Violet 6), le entrega un sobre.
- **Cómo habla**: con **papeles de correos**: las placas de latón del
  casillero (**IM Fell English**) y **una hoja de reparto** en su mano,
  escrita con prisa. Frase propuesta, en su tono seco (mía, no del
  subtítulo): **«Un hilo por texto. No me mezcles las cartas.»**
- **Dónde va cada texto**:
  - Placa grande de arriba: **Poemas**.
  - Tres casillas grandes: **Poemas** · **Letras** · **Microrrelatos**.
  - Cartel pequeño al lado, como los de «silencio»: **Aquí se lee
    despacio**.
  - Hoja de reparto: **Si comentas, comenta el texto**.
  - Dos **sellos de goma** sobre el mostrador, con su tampón: **Libre
    para usar** (tinta verde) y **No usar sin permiso** (tinta roja).
  - En la lámina 2, **nueve casillas** con las nueve etiquetas.
- **Para que no quede plano**: cartas que **sobresalen** a distinta
  profundidad; la mano de Benedict **delante** de una casilla; luz fría
  de mañana por la puerta abierta y cálida desde dentro; la saca
  desenfocada en primer plano.

### ¿Cuál primero?

1. **A** para la lámina 1: es el objeto del plan, se hace en Blender y es
   lo que todo fan reconoce.
2. **B** para la lámina 2: escena real del especial, con amigos, que
   **reparte las etiquetas sin inventar nada**.
3. **C** si el dueño prefiere un secundario querido y más humor.

---

## 20 · Lo que no pude verificar

- **Todas las imágenes**: no bajé ninguna; los enlaces de §3, §4 y §17
  están sin abrir. Sin hojas de contacto.
- **El texto del mensaje fijado** «Cómo se cuelga un texto aquí» (no está
  en el inventario).
- **El doblaje latino**: las frases; cómo dice «Auto Memory Doll», «少佐»
  y el saludo. Las voces de Gilbert, Benedict, Erica, Iris y Dietfried
  tienen **una sola fuente**.
- **Encuesta oficial** de popularidad: no encontré ninguna.
- **La letra del logo**.
- **El color exacto de la máquina** y su hoja de modelo (está en el
  Official Design Works).
- **Los hex**: estimados, sin muestrear.
- Posturas y gestos de §15: de memoria.
- El tema musical del Gaiden.
- La licencia exacta del modelo de Ed Swinbourne (el resultado de
  búsqueda dice CC BY; confírmalo al abrirlo) y del de Protoform.
- Que la oficina de C.H. se inspire en el Museo de Kioto (wiki + un blog).
- Minutos de los vídeos de YouTube y TikTok.

---

## 21 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)

- curl y WebFetch **bloqueados**: doblaje.fandom.com (también la API),
  anmtvla.com, latam.bubbleblabber.com, nlab.itmedia.co.jp,
  atmafunomena.wordpress.com, blog.sakugabooru.com,
  tv.violet-evergarden.jp, kyotoanimation.co.jp, mantan-web.jp,
  omniglot.com, teck78.blogspot.com, api.sketchfab.com, blenderkit.com,
  api.polyhaven.com, ambientcg.com.
- La herramienta de GitHub del sistema sólo deja ver el repositorio del
  proyecto; **`git clone` sí funciona**.
- Por eso **no hay `hojas/`**.

### Búsquedas web (50)

| # | Idioma | Búsqueda (dominio si lo hubo) |
|---|---|---|
| 1 | ES | Violet Evergarden doblaje latino reparto Andrea Arruti Gilbert Hodgins Cattleya voz |
| 2 | ES | doblaje wiki reparto SDI Media México director de doblaje (doblaje.fandom.com) |
| 3 | ES | «Alejandro Orozco» Gilbert «Carlos Hernández» Hodgins doblaje |
| 4 | ES | «Muñecas/Muñeca de Automemorias» frase clientes doblaje latino |
| 5 | ES | falleció Andrea Arruti, fecha, Nycolle González nueva voz |
| 6 | ES | «Muñeca de Recuerdos Automáticos» Netflix latino |
| 7 | ES | español latino «quiero saber» «te amo» escena Violet Gilbert |
| 8 | JA | ヴァイオレット・エヴァーガーデン 人気投票 キャラクター 結果 順位 |
| 9 | EN | character popularity poll results Gilbert Hodgins Cattleya favorite |
| 10 | JA | ねとらぼ 人気キャラクター 2位 3位 ギルベルト ホッジンズ ベネディクト カトレア |
| 11 | EN | typewriter design real model inspiration Kyoto Animation prop |
| 12 | JA | タイプライター 設定 モデル 実物 デザイン |
| 13 | EN | vintage typewriter Underwood CC Attribution (sketchfab.com) |
| 14 | EN | «Violet Evergarden Typewriter» sketchfab ManhattanBat license |
| 15 | JA | ロケハン ヨーロッパ 美術 渡邊美希子 ライデン モデル 街 |
| 16 | EN | Taichi Ishidate interview letters hands prosthetic Akiko Takase |
| 17 | EN | Takase costume brooch jacket (atmafunomena, sakugabooru, animenewsnetwork) |
| 18 | EN | letters typewriter Ishidate interview (mismos + j-mag.org) |
| 19 | EN | alphabet font in-universe script decoded typewriter |
| 20 | EN | logo font typeface identify serif title |
| 21 | JA | キービジュアル 第1弾 第2弾 高瀬亜貴子 描き下ろし BD ジャケット |
| 22 | EN | key visual official illustration typewriter Blu-ray cover art |
| 23 | EN | special episode opera aria Irma song title singer |
| 24 | EN | soundtrack Evan Call Sincerely Michishirube WILL Amy |
| 25 | JA | 特別編 イルマ アリア 「愛はいつも」 歌唱 ソプラノ 曲名 |
| 26 | JA | TRUE «Letter» 歌詞 «陽だまり» 挿入歌 何話 |
| 27 | ES | «Carla Castañeda» Cattleya «Alan Velázquez» Benedict |
| 28 | ES | «Nycolle González» película Gilbert Dietfried Hodgins reparto Netflix 2021 |
| 29 | ES | «Automemorias» Netflix doblaje «servicio» |
| 30 | EN | color palette hex codes outfit blue jacket brooch |
| 31 | EN | outfit details cosplay guide Prussian blue jacket |
| 32 | EN | background art director Mikiko Watanabe, color Naomi Ishida |
| 33 | EN | video game OR mobile game OR VR official collaboration |
| 34 | EN | memes fandom jokes Benedict heels Hodgins |
| 35 | EN | Kyoto Animation arson 2019 Violet Evergarden staff victims |
| 36 | JA | 日本郵便 コラボ 切手 手紙 キャンペーン ふみの日 |
| 37 | EN | wallpaper 4K 3840x2160 typewriter (wallhaven, wallpapercave, alphacoders, wallpaperaccess, wallpaperflare) |
| 38 | EN | fan art typewriter illustration artist (pixiv, artstation, deviantart) |
| 39 | ZH | 紫罗兰永恒花园 打字机 书信 名场面 薇尔莉特 台词 bilibili |
| 40 | KO | 바이올렛 에버가든 명대사 타자기 편지 자동수기인형 인기 캐릭터 |
| 41 | ES | análisis español cartas máquina de escribir (youtube.com) |
| 42 | EN | tiktok trend letter typewriter edit Sincerely (tiktok.com) |
| 43 | EN | wax seal envelope fountain pen paper CC0 (sketchfab.com, polyhaven.com) |
| 44 | EN | CC0 aged paper, old wood, leather (ambientcg, polyhaven, texturecan) |
| 45 | JA | 神回 ランキング 1位 10話 7話 みんなのランキング |
| 46 | EN | CH Postal Company building Leiden setting design inspiration |
| 47 | EN | appearance hair braids ribbon gloves prosthetic arms |
| 48 | JA | Blu-ray 1巻 ジャケット イラスト 高瀬亜貴子 タイプライター 小説 表紙 |
| 49 | ES | latino frase presentación «a donde» cliente (youtube.com, tiktok.com) |
| 50 | JA | タイプライター 3DCG 義手 作画 1コマずつ 制作 インタビュー |

### GitHub (sin cupo)

- [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror):
  clon parcial de la serie (13 episodios, japonés de Netflix con nombre
  de quien habla), del **especial**, del **Gaiden** y de la **película**
  (japonés + inglés). Todos los minutos de este documento salen de ahí.
  Los dejé en mi carpeta temporal, **no en el repositorio**.
- [google/fonts](https://github.com/google/fonts): archivos de doce
  letras, comprobadas con fontTools.
- [JxpoemYui/violet-evergarden-font](https://github.com/JxpoemYui/violet-evergarden-font):
  README y licencia de la letra del alfabeto inventado.
- Búsqueda de repositorios: traductores de nunkish, temas de escritorio.

### Fuentes consultadas por tipo

- **Oficiales**: webs del anime y de la película, Kyoto Animation
  (obra y novelas), X oficial, Japan Post, Kyoani Shop, vídeo oficial
  de producción, animate, Amazon.co.jp (reparto del BD), Netflix.
- **Entrevistas al staff** (sólo por resúmenes de búsqueda): Ishidate
  (Sakuga Blog, ATMA & Funomena, JMAG), Takase (ATMA & Funomena), mesa
  redonda de animadores, X de TRUE (letrista y cantante).
- **Otros idiomas**: japonés (ねとらぼ, みんなのランキング, magmix, note,
  Yahoo! Chiebukuro, uta-net, UtaTen, polygonote, oranda.jp,
  up-tsukuba, seichi-junrei), chino (Bilibili, Zhihu), coreano (Namuwiki,
  Ruliweb, YouTube).
- **Wikis**: Violet Evergarden Wikia, Doblaje Wiki (sólo extractos),
  Wikipedia, TV Tropes (extractos), Omniglot.
- **Foros y comunidades**: Yahoo! Chiebukuro, foro de la wiki, 9GAG,
  Facebook de coleccionistas de máquinas. **Reddit**: no lo intenté (el
  buscador lo rechaza en otras sesiones y Arctic Shift está bloqueado).
- **Arte**: ArtStation, DeviantArt, VRoid Hub. **Pixiv**: la búsqueda
  no devolvió nada.
- **Vídeo**: YouTube, TikTok, Bilibili.
- **Código y recursos**: GitHub, Sketchfab, BlenderKit, Superhive, Poly
  Haven, ambientCG, TextureCan, Adobe Color.
- **Doblaje latino**: Doblaje Wiki, ANMTV, Código Espagueti, Spoiler,
  Manga México, Somos Kudasai, Multianime, Senpai, TierraGamer,
  Anime-Planet, BTVA, FULLTV, YouTube, TikTok.

### Lo que NO encontré

- Imágenes descargadas (red cerrada); sin hojas de contacto.
- Frases del doblaje latino con fuente.
- Encuesta oficial de popularidad.
- La letra del logo.
- Videojuego oficial (no existe) y, por tanto, su caja de diálogo.
- Manga oficial (no lo encontré).
- Entrevistas originales en japonés al director de arte (Mikiko
  Watanabe) sobre la luz.
- The Cutting Room Floor y Wayback Machine: no aplican o bloqueados.
- El contenido del mensaje fijado del canal.
