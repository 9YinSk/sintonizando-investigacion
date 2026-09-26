---
tags: [biblia, serie, laminas]
serie: "Death Note"
canal: "#textos"
fecha: 2026-09-24
repaso: 2026-09-26
---

# Biblia · Death Note — para #textos

> [!important] Cómo se hizo, y sus límites
> - **Segunda pasada, 26-sep-2026, con la red abierta.** Un equipo de
>   cuatro investigadores (imagen, vídeo, voz, texto) y un redactor. Se
>   pudo usar: la wiki de Fandom por su API (`investigar_serie.py`, 1181
>   imágenes, **3 hojas en `hojas/`**), Doblaje Wiki y The Dubbing
>   Database por su API, **Internet Archive** (los 37 episodios, mirados
>   fotograma a fotograma con `fotogramas.py`), Dailymotion (opening,
>   ending y tráiler), la API de Sketchfab (licencias exactas), Wallhaven,
>   Zerochan, ambientCG, AniList, Wikipedia, TV Tropes y Reddit por Arctic
>   Shift. Sigue cerrado: **YouTube para bajar vídeo** («Sign in to confirm
>   you're not a bot»); sí se leen sus páginas de resultados con vistas.
>   Lo que cambió va justo debajo, en «Segunda pasada · qué cambió».
> - **Primera pasada, 24-sep-2026.** La red de esa sesión estaba cerrada. Fandom (y Doblaje Wiki),
>   Wikipedia, YouTube, Reddit, Arctic Shift, Wayback Machine,
>   fonts.google.com y TV Tropes dan **403** (comprobado por la sesión
>   principal; yo además choqué con Madhouse, Nlab, Sketchfab y otros). Por eso **no se pudo correr**
>   `herramientas/investigar_serie.py`: entonces **no hubo hojas de
>   contacto** (ahora sí, ver «Las hojas de contacto», tras §3).
> - **Segunda pasada**: lo que ya **se vio** en un fotograma lleva ✅ y,
>   cuando lo hay, un enlace al segundo exacto en Internet Archive (`?t=`
>   en segundos). Ese minuto es el **del archivo de Internet Archive**, que
>   puede ir unos segundos desfasado del de Netflix; se dice en cada caso.
> - Mi fuente principal fue la **búsqueda web** (la lista está al final, en
>   la bitácora).
> - GitHub sí respondía. De ahí saqué lo más útil: **los subtítulos de los
>   37 episodios, con sus tiempos**, del repositorio
>   [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/DEATH%20NOTE).
>   Hay japonés de Netflix (los 37) e inglés de fans (TSR, del 1 al 24).
>   **Todos los minutos de esta biblia son del archivo japonés de
>   Netflix**, que empieza con el opening. Los archivos de Blu-ray van
>   unos **80 segundos antes** (lo medí línea a línea: el desfase es de 80 s
>   en los 24 episodios). Puede moverse un minuto según la plataforma.
> - También bajé de [google/fonts](https://github.com/google/fonts) las
>   letras propuestas y comprobé una a una, con fontTools, si traen
>   á é í ó ú ñ ¿ ¡.
> - **Cómo leo los episodios**: «ep. 8» es el episodio 8 de 37. El minuto
>   va así: 00:18:35.
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su minuto.
>   ⚠️ **dudoso**: una sola fuente, o lo describo de memoria. Lo de
>   memoria siempre va marcado.

---

## Segunda pasada · qué cambió

(en curso: se completa al terminar de editar)

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección EL ESTUDIO):

> **ıı・📖・textos** (foro) · 2 hilos · etiquetas: Monólogo, Diálogo,
> Escena de anime, Comercial, Narración, Original, Libre para usar, Pide
> crédito, Para dos voces — _Guiones para practicar: monólogos, diálogos,
> escenas y narraciones. Un hilo por guion, y di si se puede usar libre o
> hay que pedir permiso._
> - 📌 De qué va esto · adj: `textos.png` (la lámina que hay que hacer)
> - EJEMPLO · Monólogo — hombre adulto, 40 segundos, tono contenido

Y el encargo añade la **ficha** de cada hilo: **Tipo, Voces, Duración,
Tono, Uso**.

> [!tip] La casualidad que lo une todo
> El hilo de ejemplo dice **«40 segundos»**. Y la regla más famosa del
> Death Note, después de la primera, es justo esa: **si escribes la causa
> de la muerte en los 40 segundos siguientes al nombre, pasa así**. La
> ficha del guion y las reglas del cuaderno se parecen: nombre, cómo,
> cuánto tiempo, detalles. Ver §2.


### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis. Salen del inventario, tal
cual o partidos:

| # | Texto | Idea |
|---|---|---|
| 1 | **Textos** | nombre del canal |
| 2 | **Guiones para practicar** | para qué es |
| 3 | **Monólogos, diálogos, escenas y narraciones** | qué hay |
| 4 | **Un hilo por guion** | regla 1 |
| 5 | **Llena la ficha: Tipo, Voces, Duración, Tono, Uso** | regla 2 (la ficha) |
| 6 | **Di si se puede usar libre o hay que pedir permiso** | regla 3 |
| 7 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

La ficha, campo por campo, con el hilo de ejemplo del foro:

| Campo | Ejemplo (del inventario) |
|---|---|
| Tipo | Monólogo |
| Voces | Hombre adulto |
| Duración | 40 segundos |
| Tono | Contenido |
| Uso | Libre para usar, o Pide crédito |

### Los textos de la lámina 2 (las etiquetas)

**Las nueve etiquetas no caben bien en la lámina 1.** Propongo **lámina
2**, con las etiquetas repartidas en tres grupos, como las reglas del
cuaderno (ver §19):

| Grupo | Etiquetas |
|---|---|
| **Qué es** | Monólogo · Diálogo · Escena de anime · Comercial · Narración |
| **De quién es** | Original |
| **Cómo se usa** | Libre para usar · Pide crédito |
| **Cuántas voces** | Para dos voces |

(En la lámina, sin los «·»: una etiqueta por renglón o por papel.)

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué Death Note encaja | **Todo gira alrededor de un cuaderno con instrucciones escritas.** En el ep. 1 Light lo abre y lee «使い方» («How to use it», cómo se usa) y cinco reglas (ep. 1, 00:04:32 a 00:05:30) ✅. Un foro de guiones con su ficha es lo mismo: **un texto escrito con reglas para usarlo**. Y **L habla por una voz que lee un guion ajeno**: en el ep. 2 un preso, Lind L. Tailor, lee en la tele el texto de L (00:15:02) ✅. |
| Cuadro de diálogo propio | No hay globo propio. En pantalla, el texto sale en: **la página «HOW TO USE IT»** del cuaderno (inglés, numeración romana), **la pantalla blanca con la «L» gótica** cuando L habla con voz sintética (ep. 2, 00:17:36) ✅, **la pausa (eyecatch)** que enseña una regla por episodio ✅, y **los nombres escritos a mano** en las hojas del cuaderno. |
| Objeto para la lámina | **El cuaderno negro abierto sobre el escritorio de Light** (el del plan, mejorado): en la página izquierda «CÓMO SE USA» con las reglas del canal; en la derecha, la ficha escrita a mano. Al lado: **la manzana roja mordida**, la bolsa de papas y el cajón con doble fondo (ep. 2, 00:10:32) ✅. Todo se puede hacer en Blender. |
| El más querido | **L**, no Light. No hubo encuesta oficial de la Jump ⚠️ (Yahoo! Chiebukuro), pero en la de **Nlab (2021)** L sale **1.º con 397 votos (35,2 %)** y Light **2.º con 272 (24,1 %)** ⚠️ (las cifras, de una fuente). Que **L va primero** lo dicen también Yahoo! 知恵袋 («ネットならLが1位»), Ranker y Namuwiki ✅. Lo confirma una fuente nueva, los favoritos de [AniList](https://anilist.co/anime/1535): **L 26 512**, Light 20 343, Ryuk 7 079, Misa 7 010 ✅. **Ryuk** es la imagen más reconocible de la serie (casi el triple de favoritos que Mello) ✅. Secundario de culto: **Matsuda** (§9). |
| Letras | **UnifrakturMaguntia** para la «L» y el rótulo gótico; **IM Fell English** o **Special Elite** para las reglas; **Kalam** o **Nothing You Could Do** para la letra a mano; **Nosifer** sólo para una gota de sangre, nunca para el texto. Todas traen tildes, ñ, ¿ y ¡: comprobado en el archivo. |
| Voz latina | Light **Manuel Campuzano** ✅, L **Hugo Núñez** ✅, Ryuk **Rolando de Castro** (también director) ✅, Misa **Rebeca Gómez** ✅, Near **Bruno Coronel** ✅, Mello **Javier Olguín** ✅; y ahora también Rem **Erica Edwards**, Watari **Carlos del Campo**, Matsuda **Alfredo Leal**, Mikami **Arturo Mercado Jr.** y Sōichirō **José Lavat** ✅. Ver §10. |
| Tono | Negro, gris azulado y **rojo** (manzanas, ojos de shinigami, sangre del final). Sangriento, como pidió el servidor: **la sangre tiene base en la serie**: en el último episodio Light, herido, **intenta escribir un nombre con su sangre** (ep. 37, 00:14:28, «血で!», «¡con sangre!») ✅. |
| Juegos de la franquicia | **Kira Game** (DS, Konami, 2007) y su secuela **L o Tsugu Mono** (DS; el año, 2008, ⚠️) ✅; **Death Note: Killer Within** (PS4, PS5 y PC, Bandai Namco y Grounding, 2024) ✅. |

---

## 2 · Las escenas que sirven para #textos (con minuto)

Todas salen de los subtítulos de
[kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/DEATH%20NOTE):
el texto y el minuto están comprobados ✅ (minuto del archivo japonés de
Netflix). Lo que **se ve** en cada una (postura, luz) lo describí en la
primera pasada de memoria. **En la segunda pasada se miraron los
fotogramas de verdad** (Internet Archive, 1280×720): el resultado está
en §2.11, con dos correcciones (el 00:04:32 del ep. 1 y la sonrisa del
ep. 25).

### 2.1 «Cómo se usa»: el cuaderno trae sus instrucciones (ep. 1)

| Minuto | Qué pasa | Texto (japonés · inglés de fans) |
|---|---|---|
| 00:04:32 | Light lee la primera página. **Lo que se ve** (fotograma, 2.ª pasada): no es Light, es un **insert de la página negra** «DEATH NOTE / How to use it», letra blanca gótica, calavera con aureola, marco decorado ✅ | «“使い方”» · «"How to use"...» |
| 00:04:33 | Regla I | «The human whose name is written in this note shall die» |
| 00:05:09 | Regla II | «This note will not take effect unless the writer has the person's face in their mind…» |
| 00:05:22 | Regla III | «“40秒以内に死因を書くと そのとおりになる”» · «If the cause of death is written within 40 seconds…» |
| 00:05:26 | Regla IV | «“書かなければ 死因は全て心臓麻痺になる”» · heart attack |
| 00:05:30 | Regla V | «“死因を書くと さらに６分40秒⸺”» · 6 minutes and 40 seconds |
| 00:05:41 | Light, burlón | «Quite a lot of detail to go into for a simple prank… Not bad.» |
| 00:16:44 | Light a Ryuk | «丁寧に使い方まで書いて» («y encima con las instrucciones escritas con tanto cuidado») |

**Para qué sirve**: es la escena que convierte la lámina en «las reglas
del canal». El foro también tiene reglas cortas y numeradas.

### 2.2 El guion leído por otro: Lind L. Tailor (ep. 2)

| Minuto | Qué pasa | Texto |
|---|---|---|
| 00:14:50 | Retransmisión especial de la ICPO en toda la tele | «ＩＣＰＯ インターポールからの 全世界同時特別生中継» |
| 00:15:02 | Un hombre lee **el texto de L** ante la cámara | «I am the only person who can control the entire world's police forces, Lind L. Tailor. I go by the code name… "L".» |
| 00:16:14 | Sigue leyendo | «お前のしていることは悪だ» («lo que haces es el mal») |
| 00:16:24 | Light, furioso | «僕は正義だ！» («¡Yo soy la justicia!») |
| 00:17:10 | Light cuenta | «あと５秒 ４ ３ ２ １» |
| 00:17:36 | **Pantalla blanca con la «L» gótica**, voz sintética | «（Ｌ：合成音声）信じられない» («increíble») |
| 00:17:59 | L revela el truco | Tailor era un preso condenado a muerte ese mismo día: **leía un guion** |
| 00:18:23 | L reta a Light | «さあ 私を殺してみろ» («vamos, intenta matarme») |
| 00:21:10 a 00:21:16 | Cierre a dos voces | «必ず お前を 捜し出して始末する … 僕が… 私が… 正義だ！» |

**Para qué sirve**: es literalmente **un guion para dos voces**, con
réplica y contrarréplica. Y el final del ep. 2 (00:21:10) está **dicho a
la vez por dos personajes**: la etiqueta «Para dos voces» hecha escena.

### 2.3 El doble fondo del cajón (ep. 2)

| Minuto | Qué pasa |
|---|---|
| 00:09:41 | Light enseña a Ryuk dónde guarda el cuaderno: «この引き出しの中にね» |
| 00:10:32 | Ryuk: «なるほど 二重底か» («ya veo, doble fondo») |
| 00:11:06 | La trampa: si alguien fuerza el cajón, **arde gasolina en una bolsa fina** y quema el cuaderno |

**Para qué sirve**: es un objeto de Blender perfecto (cajón, doble
fondo, bolsita, bolígrafo). Puede ser el **sitio de la lámina 2**: las
etiquetas guardadas en el cajón secreto.

### 2.4 La papa frita (ep. 8)

| Minuto | Texto |
|---|---|
| 00:16:14 | Sayu: «お兄ちゃん ごはんのあとにポテチ？» («¿papas después de cenar?») |
| 00:18:06 | Light: «やってやるよ Ｌ！» («te lo voy a demostrar, L») |
| 00:18:26 | «右手で方程式を解き続け» (con la derecha resuelve ecuaciones) |
| 00:18:29 | «左手で名前を書き» (con la izquierda escribe nombres) |
| 00:18:35 | **«ポテチを取り 食べる»** («tomo una papa frita… y me la como») |

Se repite al principio del ep. 9 (00:01:39 a 00:01:45). Es **el meme más
conocido de la serie** ✅ ([ComicBook.com](https://comicbook.com/anime/news/death-note-potato-chip-scene-reddit/),
[AniLoop](https://aniloop.org/why-death-notes-potato-chip-scene-actually-works/),
[Peliplat](https://www.peliplat.com/en/article/10072541/the-potato-chip-scene-in-death-note-is-actually-brilliant)).
El director **Tetsurō Araki** la montó con música de orquesta y cortes
rápidos, como si fuera una batalla ⚠️ (lo cuenta AniLoop; lo de la
música se oye en el episodio). Que Araki dirigió la serie ✅
([SlashFilm](https://www.slashfilm.com/1251249/death-note-director-romance-stories-anime-isnt-ready/),
[Madhouse](https://www.madhouse.co.jp/works/2006-2005/works_tv_deathnote_interview.html)).

**Para qué sirve**: enseña que **un gesto pequeño leído con tono épico**
es un ejercicio de actuación. Guion de práctica perfecto: «Tono:
dramático exagerado».

### 2.5 L se presenta (ep. 9)

| Minuto | Texto |
|---|---|
| 00:14:39 | L, a Light, en la ceremonia de ingreso: **«私はＬです»** («Soy L») |
| 00:14:50 | Light, por dentro: «Ｌが“Ｌだ”と言うはずがない» («L no diría nunca que es L») |

### 2.6 L y su forma de sentarse (ep. 10)

| Minuto | Texto |
|---|---|
| 00:08:14 | L: **«一般的な座り方をすると 推理力が40％減です»** («si me siento normal, mi capacidad de deducción baja un 40 %») |
| 00:08:32 | L: «夜神君の推理力を テストしてみてもいいでしょうか？» («¿puedo poner a prueba tu capacidad de deducción?») |

Otra vez **el 40**. Y la escena del **partido de tenis** está en el
ep. 10 (00:01:28) ✅.

### 2.7 «Tal como lo planeé» (ep. 24)

| Minuto | Texto |
|---|---|
| 00:05:39 | Light, por dentro: «勝った» («gané») |
| 00:05:42 | **«計画どおり»** («todo según el plan») |

Es la cara malvada que los fans llaman *keikaku doori* ✅ (subtítulo).
Que sea meme mundial: ver §14.

### 2.8 La muerte de L (ep. 25)

| Minuto | Qué pasa |
|---|---|
| 00:01:57 a 00:02:23 | **Campanas** (鐘の音) |
| 00:10:30 a 00:11:05 | L en la azotea, bajo la lluvia: «鐘の音が 今日 すごく うるさいんですよね» («las campanas suenan muy fuerte hoy») |
| 00:13:36 a 00:14:21 | **L le seca los pies a Light** («マッサージもつけますよ») |
| 00:14:45 | L: **«寂しいですね … もうすぐ お別れです»** («qué triste… pronto nos despediremos») |
| 00:16:28 | Se va la luz, alarmas; muere Watari |
| 00:17:12 a 00:17:15 | L: «皆さん しにが…» y cae de la silla |
| 00:17:41 a 00:18:52 | Light lo sostiene: **la sonrisa** que todos recuerdan. **Corregido en la 2.ª pasada**: la sonrisa nítida (boca abierta, dientes, luz roja de alarma) está a las **00:18:00**; a las 00:17:41 aún no se ve clara ✅ (fotograma). Suena **«Kyrie II»** (§11) |

### 2.9 «Sakujo» (ep. 31)

| Minuto | Texto |
|---|---|
| 00:18:47 a 00:19:29 | Mikami, escribiendo con furia: **«削除»** («¡Eliminar!»), seis veces |

### 2.10 Los 40 segundos (ep. 36) y la sangre (ep. 37)

| Minuto | Texto |
|---|---|
| 36, 00:20:55 | «（秒針の音）» (el segundero) |
| 36, 00:20:58 a 00:21:10 | Light cuenta: «30… 31… 32… … 39…» |
| 36, 00:21:12 | **«ニア 僕の勝ちだ»** («Near, he ganado») |
| 36, 00:21:15 | Mikami: **«40！»** |
| 37, 00:10:09 a 00:10:16 | Light: «僕はキラ そして… 新世界の神だ» («soy Kira… y el dios del nuevo mundo») |
| 37, 00:14:28 | Aizawa: **«血で！»** («¡con sangre!»): Light, herido de bala, intenta escribir con su sangre |
| 37, 00:18:37 | Ryuk: **«お前の負けだ 月»** («perdiste, Light») |
| 37, 00:19:27 | Ryuk: «結構 長い間 互いの 退屈しのぎになったじゃないか» («nos quitamos el aburrimiento un buen rato») |

**Para qué sirve**: el **40** de la ficha de ejemplo («40 segundos») es
el número de la serie: 40 segundos para la causa de muerte (ep. 1),
40 % de deducción de L (ep. 10) y la cuenta de Mikami (ep. 36). Y la
sangre de verdad sale al final: **escribir con sangre** es la imagen
«sangrienta» que no inventa nada.

### 2.11 Lo que se ve en cada escena (segunda pasada, fotograma mirado)

Episodios completos de Internet Archive (`archive.org/download/death-note-XX`,
1280×720; el 11 es `death-note-11_202008`), fotograma sacado con
`fotogramas.py --fotograma <segundo>` y mirado uno a uno. Minuto de
partida: el de los subtítulos (coincide).

| Escena | Ep., minuto | Qué se ve de verdad | Cambia algo |
|---|---|---|---|
| Las reglas del cuaderno | 1, 00:04:32 | Insert en primer plano de la página negra «DEATH NOTE / How to use it», letra blanca gótica, calavera con aureola, marco decorado. Es el mismo insert del tráiler (0:36 y 1:00) | Sí: no es Light con el cuaderno |
| Ryuk se presenta | 1, 00:13:00 | Contrapicado: Ryuk enorme detrás de Light (de espaldas, en su escritorio), alas de pelo negro en punta, ventana con cortina azul, estantería | Confirma ✅ |
| Ryuk y la manzana | 1, 00:16:12 | Silueta de Ryuk a contraluz azul noche, ojos amarillos, cinturón con hebilla de calavera. El mordisco cae ±2 s | ⚠️ ajustar ±2 s |
| «¡Soy la justicia!» | 2, 00:16:24 | Primer plano de Light gritando a la tele, puño cerca de la cara | Confirma ✅ |
| La «L» gótica | 2, 00:17:36 | Tele CRT azul sobre un mueble, pantalla blanca con la **L** caligráfica negra, suelo verde | Confirma ✅ |
| La papa frita | 8, 00:18:35 | Plano dividido: la **derecha escribe** con bolígrafo en el cuaderno abierto mientras la **izquierda sube la papa** a la boca; bolsa naranja, luz lateral dura, estantería | Mejora: se ven las dos manos a la vez ✅ |
| *Keikaku doori* | 24, 00:05:42 | Primerísimo plano: media cara en sombra, **ojos rojos brillantes**, sonrisa torcida, **auricular de manos libres** junto a la boca (está al teléfono), borde del cuaderno abajo | Añade el auricular ✅ |
| L en cuclillas (café) | 10, 00:08:14 | L en cuclillas sobre la silla, dedo en el labio, jardinera verde detrás, luz cálida de persiana | Confirma ✅ |
| Muerte de L | 25, 00:17:12 y 00:18:00 | 17:12: plano rojo de emergencia, L girado hacia un panel. **18:00: la sonrisa** de Light, boca abierta, luz roja | Sí: la sonrisa es 00:18:00 ✅ |
| Light enloquece | 36, 00:21:12 | Primerísimo plano: pelo despeinado tapando un ojo, **bolígrafo entre los dientes**, mirada de locura, fondo blanco quemado | Nuevo ✅ |
| «¡Con sangre!» | 37, 00:14:28 | Contrapicado de Aizawa gritando, gabardina gris, corbata naranja, vigas metálicas del almacén | Confirma ✅ |

**Opening, ending y tráiler, mirados** (YouTube no deja bajar vídeo; se
usó Dailymotion con `fotogramas.py`):

- **Opening 1** «the WORLD» ([Dailymotion x31pve2](https://www.dailymotion.com/video/x31pve2)):
  0:30 Light de gabardina por una calle de Tokio con una manzana en la
  mano; 0:45 alguien en un sillón rojo envuelto en tela oscura; 1:00
  silueta por un pasillo oscuro; 1:15 figura alada sobre fondo
  dorado-rosado ✅.
- **Ending 1** «Alumina» ([Dailymotion x6alujt](https://www.dailymotion.com/video/x6alujt)):
  0:12 primer plano rojo de una mano o rostro con líneas de velocidad;
  0:24 silueta cayendo contra un cielo azul; 0:48 andamio a contraluz;
  1:00 rostro con ojos rojos muy cerca, rojo y negro ✅.
- **Tráiler del anime** ([Dailymotion x89nprz](https://www.dailymotion.com/video/x89nprz),
  el del anime, no el de la película de 2017: lleva el logo de la
  calavera con aureola): 0:12 ojos de Light; 0:24 una mano abre el
  cuaderno sobre un cadáver dibujado a tinta; 0:36 y 1:00 el insert
  «How to use it» con las reglas en pantalla; 0:48 un auditorio mirando
  la pantalla con la «L»; 1:12 Light y L cara a cara ✅.

⚠️ No hay fotogramas a 1080p: Internet Archive sólo tiene 1280×720
(`archive.org/metadata/death-note-01`) y YouTube no deja bajar.

---

## 3 · Arte oficial y referencias visuales

> [!note] Primera pasada sin imágenes; segunda pasada con 1181
> En la primera pasada ni la wiki de Fandom ni las webs oficiales se
> dejaban abrir: 3.1 a 3.5 son **las fuentes que existen y dónde
> buscarlas**. En la segunda pasada `investigar_serie.py` bajó **1181
> imágenes** de 6 páginas de la wiki (Light, L, Ryuk, Misa, Near, Mello),
> con su tamaño real: lo nuevo está en 3.6 y en «Las hojas de contacto»,
> justo después.

### 3.1 El manga (Tsugumi Ohba y Takeshi Obata, Shūeisha, 2003-2006)

- **12 tomos + el tomo 13, «How to Read»** (guía oficial) ✅
  ([Wikipedia: capítulos](https://en.wikipedia.org/wiki/List_of_Death_Note_chapters)).
- **Entre capítulo y capítulo**, el tomo japonés trae **una página «How to
  Use It»**: una regla del cuaderno **en inglés** con su traducción
  japonesa debajo ✅ ([YOSHI BLOG](https://yoshiblog.info/anime/deathnote/deathnote-yougo/),
  [TV Tropes: EyeCatch](https://tvtropes.org/pmwiki/pmwiki.php/EyeCatch/AnimeAndManga)).
  **Es el modelo de la lámina**: una regla por página, numerada.
- **Viz «Black Edition»**, en EE. UU. ✅ (que sean 6 tomos dobles ⚠️, de memoria)
  ([SciFi Japan](https://www.scifijapan.com/merchandise/revisit-the-world-of-death-note-in-the-new-black-edition-from-viz-media)).
- **Capítulos especiales**: «C-Kira» (2008 ⚠️) y **«a-Kira Story»**
  (Jump SQ, 4 de febrero de 2020), con **Ryuk que vuelve al mundo humano**
  diez años después; reunidos en **Death Note: Short Stories** (Viz, 10 de
  mayo de 2022) ✅ ([Hypebeast](https://hypebeast.com/2022/4/death-note-short-stories-manga-viz-media-release-info),
  [GameSpot](https://www.gamespot.com/articles/death-note-short-stories-brings-one-shots-to-print-including-that-infamous-trump-story/1100-6502665/),
  [Viz](https://www.viz.com/shonenjump/chapters/death-note-short-stories)).

### 3.2 El artbook de Obata

- **«blanc et noir»** (小畑健画集, Shūeisha, 31 de mayo de 2006): B4, 168
  páginas, **más de 120 ilustraciones** de Death Note y Hikaru no Go, con
  un *making of* de color ✅ ([HLJ](https://www.hlj.co.jp/product/SYU82146),
  [Books.or.jp](https://www.books.or.jp/book-details/9784087821468),
  [漫画全巻ドットコム](https://www.mangazenkan.com/items/46773/)).
  **Es la mejor referencia de pose y color**: Obata pinta con acuarela y
  tinta, blancos grandes y negros densos ⚠️ (de memoria).

### 3.3 El anime (Madhouse, 2006-2007, 37 episodios)

- Equipo: dirección **Tetsurō Araki** ✅ (Madhouse, SlashFilm,
  fullfrontal.moe). Diseño de personajes **Masaru Kitao**, dirección de
  arte **Mio Isshiki** (一色美緒), color **Ken Hashimoto** (橋本賢) ⚠️ (un
  resumen de búsqueda en japonés, con [Anime Staff DB](https://seesaawiki.jp/w/radioi_34/d/DEATH%20NOTE)
  y la [ficha de Madhouse](https://www.madhouse.co.jp/works/2006-2005/works_tv_deathnote.html)).
  Guion de la serie: Toshiki Inoue ⚠️
  ([AniLoop](https://aniloop.org/why-death-notes-potato-chip-scene-actually-works/)).
- Araki: «si el original vale 100, quise llegar a 120» y «es un manga con
  poco movimiento: todo está en cómo sostener la imagen» ✅ (resumen de su
  entrevista en [Madhouse](https://www.madhouse.co.jp/works/2006-2005/works_tv_deathnote_interview.html);
  no pude abrir la página).
- Hay una entrevista larga sobre **color y fotografía** con Araki
  ([fullfrontal.moe, 2024](https://fullfrontal.moe/tetsuro-araki/)).
  **Leída en la segunda pasada**: lo que dice está en «Punto 18» ✅.
- **Segunda pasada, equipo según AniList** (`datos-texto.md`): diseño de
  personajes **Masaru Kitao**, dirección de arte **Mio Isshiki**, diseño
  de arte **Shinji Sugiyama**, diseño de color **Satoshi Hashimoto** ✅.
  Kitao e Isshiki quedan confirmados con dos fuentes. El color: AniList
  dice **Satoshi** Hashimoto y el resumen japonés de la primera pasada
  decía **Ken** Hashimoto (橋本賢) ⚠️ (no se resolvió; usa el de AniList).
- **Ediciones**: 13 DVD en Japón (dic. 2006 a dic. 2007); **caja de
  Blu-ray** el 19 de octubre de 2016 ⚠️ (una fuente); en EE. UU., Viz
  «The Complete Series» ✅ ([Viz](https://www.viz.com/anime/tv-series/death-note-video-box-sets/product/4770),
  [SciFi Japan](https://www.scifijapan.com/dvd-blu-ray-digital/death-note-anime-series-complete-dvd-set-on-november-18th)).
- **Galería de imágenes del anime** en la wiki (bloqueada aquí):
  [Death Note (anime)/Image Gallery](https://deathnote.fandom.com/wiki/Death_Note_(anime)/Image_Gallery).

### 3.4 Juegos y otros

- **Death Note: Killer Within** (2024): arte clave oficial con Kira y L
  ✅ ([Bandai Namco](https://www.bandainamcoent.com/games/death-note-killer-within),
  [Steam](https://store.steampowered.com/app/2213190/DEATH_NOTE_Killer_Within/)).
- **El musical** (HoriPro) vuelve en **julio de 2026** en Londres ✅
  ([Screen Rant](https://screenrant.com/death-note-revival-2026-musical-stage-play-london/),
  [ComicBook.com](https://comicbook.com/anime/news/death-note-announces-surprise-2026-comeback/)).
- La **serie de Netflix** de los Duffer está en el aire: se fueron de
  Netflix en abril de 2026 ⚠️ ([What's on Netflix](https://www.whats-on-netflix.com/news/netflix-death-note-series-from-stranger-things-creators-what-we-know-so-far/),
  [ComicBook.com](https://comicbook.com/anime/news/netflix-death-note-live-action-status/)).
- **La película de Netflix (2017)** tiene otro Ryuk, otro Light y otro
  estilo. **No la mezcles** con el anime (ver §14).

### 3.5 Lo que falta ⚠️

- Las **portadas de los 12 tomos** una a una, con tamaño: sigue sin
  salir en la segunda pasada (la wiki no las separa por tomo; sólo
  tiendas de reventa sin medida) ⚠️.
- ~~Los **key visuals** del anime en alta~~: **resuelto**, 4 key visuals
  oficiales a 1920×1080 en Zerochan (§17).
- Las **pausas (eyecatch)** en fotograma: el subtítulo de fans marca su
  sitio (ep. 1, hacia el minuto 10:37 del archivo de fans «zza»; ep. 2,
  12:12; ep. 3, 12:31; sin alinear con Netflix) pero **no trae el
  texto** ⚠️. En la hoja 2, nº245, hay una página del manga con el
  eyecatch nocturno.

### 3.6 Arte oficial con tamaño real (segunda pasada)

Todo de la wiki de Fandom por su API, tamaño leído del archivo ✅.

| Qué | Tamaño | Original |
|---|---|---|
| Light de perfil, camisa del instituto (color page de Obata) | 2001×4705 | [299276.jpg](https://static.wikia.nocookie.net/deathnote/images/0/05/299276.jpg) |
| L de pie, de blanco, pareja de la anterior | 2088×4608 | [299276L.jpg](https://static.wikia.nocookie.net/deathnote/images/7/76/299276L.jpg) |
| Misa, «Saint Valentine's Day», vestido rojo y calaveras | 3466×5000 | [295978.jpg](https://static.wikia.nocookie.net/deathnote/images/6/60/295978.jpg) |
| Near, mano en la cara | 3039×5000 | [DN_013.jpg](https://static.wikia.nocookie.net/deathnote/images/8/8b/DN_013.jpg) |
| L sentado comiendo chocolate | 1352×2200 | [Lfull.jpg](https://static.wikia.nocookie.net/deathnote/images/0/0f/Lfull.jpg) |
| Ryuk a color, cuerpo entero | 860×1384 | [Ryuk_DN_Coloured.png](https://static.wikia.nocookie.net/deathnote/images/a/a8/Ryuk_DN_Coloured.png) |
| Grupo del artbook: L, Light, Misa y más | 3326×5000 | [LLightMisa(art-book)](https://static.wikia.nocookie.net/deathnote/images/e/e7/LLightMisa%28art-book%29.jpg) |
| L en un sillón con Near y Mello detrás (artbook) | 3114×5000 | [LNearMello(art-book)](https://static.wikia.nocookie.net/deathnote/images/6/61/LNearMello%28art-book%29.jpg) |
| Light y L espalda con espalda, con una cruz | 3467×5000 | [Death_note_4.jpg](https://static.wikia.nocookie.net/deathnote/images/1/19/Death_note_4.jpg) |
| Near sentado entre juguetes, ventanas con «N» | 3306×5000 | [2079.jpg](https://static.wikia.nocookie.net/deathnote/images/b/be/2079.jpg) |
| Light de negro entre shinigami | 2435×3485 | [DN_043.png](https://static.wikia.nocookie.net/deathnote/images/8/8a/DN_043.png) |
| Light, arte nuevo de la exposición de Death Note (rojo, blanco y negro) | 2892×2076 | [Light_new_art_DN_Exhibition](https://static.wikia.nocookie.net/deathnote/images/d/db/Light_new_art_DN_Exhibition.jpeg) |
| Wallpapers del juego *Othellonia* (Light, L, Light y L, Misa, Near, Mello) | 2208×2208 cada uno | [Light](https://static.wikia.nocookie.net/deathnote/images/a/af/Othellonia_wallpaper_Light.jpg), [L](https://static.wikia.nocookie.net/deathnote/images/3/3f/Othellonia_wallpaper_L.jpg), [Misa](https://static.wikia.nocookie.net/deathnote/images/d/d8/Othellonia_wallpaper_Misa.jpg), [Near](https://static.wikia.nocookie.net/deathnote/images/f/f0/Othellonia_wallpaper_Near.jpg), [Mello](https://static.wikia.nocookie.net/deathnote/images/0/05/Othellonia_wallpaper_Mello.jpg) |
| Portada y banner del anime | — | [AniList portada](https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx1535-kUgkcrfOrkUM.jpg), [banner](https://s4.anilist.co/file/anilistcdn/media/anime/banner/1535.jpg) |

- **El musical** (HoriPro): pósteres y fotos de las giras de Taiwán 2017
  (6000×4000) y Corea 2015 y 2017 ✅. Son actores reales: sirven para
  pose, **no para color ni diseño**.
- **Cuidado en la wiki**: mezcla el anime con las películas de imagen
  real (2006, *Light Up the New World* 2016), el drama de 2015 y la
  película de Netflix 2017. En las hojas van marcadas: no las uses como
  estilo.

---

## Las hojas de contacto

Tres hojas en `hojas/` (JPEG de menos de 1 MB), sacadas de las 12 que
montó `investigar_serie.py`. **Miradas una a una** por el redactor.
Cada número lleva debajo su tamaño real y el nombre del archivo en la
wiki.

**`hojas/arte_oficial_01.jpg`** (nº 1-48)

- **Sirven (anime y manga)**: nº7 Light y L espalda con espalda con la
  cruz · nº8 Misa «Saint Valentine's Day» · nº9 grupo del artbook ·
  nº10 L cabeza abajo (DN 022) · nº11 «L Lawliet», L con el dedo en el
  labio · nº12 Near con juguetes · nº13 L en el sillón con Near y Mello
  · nº14 Near, mano en la cara · nº15 Light, Misa y L · nº16 y nº17
  grupos con Ryuk y Rem · nº26 L de blanco y nº27 Light de perfil (la
  pareja 299276) · nº29 Light de negro entre shinigami · nº31 Near a
  los 21 años (cartel) · nº34 Light, arte de la exposición · nº36 Near
  de cuerpo entero · nº37-42 wallpapers de *Othellonia* · nº44 Ryuk
  (póster, 1720×2500) · nº46 primera aparición de Mello.
- **No sirven de estilo** (imagen real): nº1-5 y 25 musical de Taiwán,
  nº18-20 y 28 musical coreano, nº21-24, 30, 45 y 47 películas
  japonesas, nº6, 32-33, 35, 43 y 48 película de Netflix 2017.
- **Para qué**: nº8 y nº27 son las poses de Misa y Light de los
  conceptos A y C; nº11 y nº26 sirven para L «explicando»; nº13 para
  una lámina en grupo con los sucesores.

**`hojas/colaboraciones_02.jpg`** (nº 241-288)

- **Sirven**: nº241-243 color pages (Light con shinigami, Light
  tendiendo la mano, Misa con Light) · nº244 cartel de **Universal Jump
  Summer** (Ryuk con Luffy y Goku) · nº245 página del manga · nº251
  Ryuk con Light (DN 006) · **nº252-253 Light y Ryuk en 3D de *Jump
  Force*** · nº255 hoja de modelo de Light a lápiz (Pp140-141) · nº256
  Light cara a cara con Near · nº258 Near *chibi* de *Jumputi Heroes* ·
  nº259-260 Mello de cuero rojo · nº261 L de pie, descalzo · nº262
  página del manga con Near · nº265 Ryuk a color · nº267 Ryuk con una
  chica que abraza un Death Note (DNP 001, del piloto) · nº268 L y
  nº271 Near en el anime · nº272 Ryuk en rojo · nº276-285 fotogramas
  del ep. 1 (ojo rojo del shinigami, sonrisas de Ryuk, Light a
  contraluz) · nº286 Ryuk en el mundo shinigami · nº287 L empapado ·
  nº288 Mello en el anime.
- **No sirven de estilo**: nº246-250, 254, 257, 263-264, 266, 269-270,
  273-275 (películas, musical, Netflix).
- **Corrección a la parte de imagen**: *Jump Force* es **nº252-253**, no
  nº259-260 (esos son Mello). La nº261 es L de pie, no un fondo de
  Wammy's. La nº267 no es Ryuk con Misa muerta: es Ryuk con una chica y
  el cuaderno (piloto).

**`hojas/colaboraciones_03.jpg`** (nº 529-540)

- **Sirven**: nº530-531 y nº538-539 colaboración con **LINE Bubble 2**
  (anuncios con L y Ryuk *chibi*, stickers; el nº538 lleva el plazo
  «11/30 … 12/3 23:59», sin año) · nº532 **Light le da una patada a L**
  (página a color del manga, capítulo 45; buena para «regañar») · nº533
  L en el ep. 25 · nº536 **Death Note the Escape** (sala de escape, con
  «能力診断», 930×550).
- **No sirven de estilo**: nº529, 534-535, 537 y 540 (películas,
  musical coreano 2017, drama 2015).

Originales de las que se citan en los conceptos:
[Universal_Jump_Summer](https://static.wikia.nocookie.net/deathnote/images/c/c8/Universal_Jump_Summer.jpg) (1400×1027),
[Jumpforcelight1](https://static.wikia.nocookie.net/deathnote/images/b/ba/Jumpforcelight1.png) (1600×850),
[ChapterDN045](https://static.wikia.nocookie.net/deathnote/images/6/60/ChapterDN045.jpg) (712×728),
[DeathNoteL](https://static.wikia.nocookie.net/deathnote/images/9/90/DeathNoteL.png) (871×1480),
[DNP_001](https://static.wikia.nocookie.net/deathnote/images/a/ac/DNP_001.jpg) (1000×1168),
[Ryuk_in_the_Shinigami_Realm](https://static.wikia.nocookie.net/deathnote/images/0/04/Ryuk_in_the_Shinigami_Realm.jpg) (1391×782),
[LINE_Bubble_2_ad_3](https://static.wikia.nocookie.net/deathnote/images/d/dc/LINE_Bubble_2_ad_3.jpg) (800×638),
[Death_Note_the_Escape_03](https://static.wikia.nocookie.net/deathnote/images/8/86/Death_Note_the_Escape_03.jpg) (930×550) ✅
(tamaño leído en la API de la wiki, 26-sep-2026).

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D del cuaderno (Sketchfab)

Según los resultados de búsqueda, todos con licencia **CC BY**
(atribución obligatoria) ⚠️: **abre cada página y confirma la licencia
antes de bajarlo**; no pude entrar en Sketchfab.

| Modelo | Autor | Enlace |
|---|---|---|
| Death Note (2020) | CG.oum (@ayoub.oumahou) | [38e9f0d](https://sketchfab.com/3d-models/death-note-38e9f0d0c6944557b6ecf2003f5aa4bb) |
| Notebook of Death (2025): permite usarlo en juegos y animación con enlace o crédito | Kasuga (@kasuga) | [cee405b](https://sketchfab.com/3d-models/notebook-of-death-cee405b6e2a544e1a819bbc514233090) |
| Death Note (2024) | ParaGO | [d82d654](https://sketchfab.com/3d-models/death-note-d82d6546f5994f128147748487f64ca8) |
| Death note, sin textura (2023) | OFFICIALSAGAM | [6583eaa](https://sketchfab.com/3d-models/death-note-no-texture-so-far-blender-6583eaa92f21431580fe8734de1f4393) |
| Death note (2025) | Shah Bakhat026 | [a6fe57b](https://sketchfab.com/3d-models/death-note-a6fe57b372134841896f785a0253ebef) |

**Consejo**: el cuaderno es una caja con tapas. **Se modela en diez
minutos** y así la tinta y la luz son tuyas (como la estela de AoT). Usa
estos modelos sólo para mirar el grosor, el lomo y cómo cae la tapa.

Personajes en 3D (sólo para mirar poses): [L](https://sketchfab.com/3d-models/l-from-death-note-5ebc1b2d188049d18c767283f9c4bdce)
y [Light](https://sketchfab.com/3d-models/light-yagami-from-death-note-7d0599365ae141f7b0b65cd55d27a06b),
de Shah Bakhat026.

**Segunda pasada: licencias leídas en la API de Sketchfab** (campo
`license.label` de `api.sketchfab.com/v3/search`, 26-sep-2026) ✅.
*CC Attribution* = **hay que citar al autor** en los créditos.

| Modelo | Autor | Licencia (API) | ♥ | Enlace |
|---|---|---|---|---|
| Death Note (cuaderno) | ayoub.oumahou (CG.oum) | CC Attribution | 134 | [38e9f0d](https://sketchfab.com/3d-models/none-38e9f0d0c6944557b6ecf2003f5aa4bb) |
| Death Note (cuaderno) | rengokukyojuro | CC Attribution | 37 | [9d98c78](https://sketchfab.com/3d-models/none-9d98c78fdeca4846a91b3e474bd5d038) |
| Death Note (cuaderno) | zevik-es | CC Attribution | 15 | [17e2a68](https://sketchfab.com/3d-models/none-17e2a68603464169b22ea5cdb8572f69) |
| Death Note anime book fanart | pedrohmm123 | CC Attribution | 14 | [9702482](https://sketchfab.com/3d-models/none-970248251f124cddbfc2b4999c43b713) |
| Death Note (cuaderno) | ParaGO | CC Attribution | 10 | [d82d654](https://sketchfab.com/3d-models/none-d82d6546f5994f128147748487f64ca8) |
| Death Note Notebook (más detallado) | Efes3DStudio | **CC Attribution-NonCommercial** | — | [9bbeb99](https://sketchfab.com/3d-models/none-9bbeb99898f14d2cb01f4146a1a7d5c0) |
| Ryuk from Death Note | PotBin | CC Attribution | 19 | [cf0ccb0](https://sketchfab.com/3d-models/none-cf0ccb0310ea4bdd97122b6183e9e71b) |
| RYUK | Theo_Prodger | CC Attribution | 8 | [3c21e12](https://sketchfab.com/3d-models/none-3c21e12167fc482db5f5512eb34aff00) |
| ryuk death note | bakhats110 | CC Attribution | — | [7acb4b1](https://sketchfab.com/3d-models/none-7acb4b1db5d745f4a734686a469cbb89) |
| L from death note | bakhats110 | CC Attribution | 6 | [5ebc1b2](https://sketchfab.com/3d-models/none-5ebc1b2d188049d18c767283f9c4bdce) |
| light yagami from Death note | bakhats110 | CC Attribution | 17 | [7d05993](https://sketchfab.com/3d-models/none-7d0599365ae141f7b0b65cd55d27a06b) |

- Los de CG.oum y ParaGO de la tabla de arriba quedan **confirmados
  CC BY** ✅. Los de Kasuga, OFFICIALSAGAM y el cuaderno a6fe57b no
  salieron en la API: su licencia sigue ⚠️.
- **No hay modelo libre de Misa ni de Near** (la API dio 0 y 2
  resultados sin relación) ⚠️.

### 4.2 Fan art 2D (mirar, nunca pegar)

| Obra | Autor | Nota |
|---|---|---|
| [Ryuk, concept art](https://www.artstation.com/artwork/OKk2e) | Luca Nemolato | Es **de la película de Netflix**: otro diseño |
| [Ryuk](https://www.artstation.com/artwork/rRb5zO) | Maicon Ricardo | Escultura en ZBrush, para coleccionable |
| [Ryuk](https://emilio_mansilla.artstation.com/projects/OyJ1E6) | Emilio Mansilla García | Estudio de luz |
| [Ryuk y Light](https://www.artstation.com/artwork/442E1) | Sheridan Doose | Pareja clásica |
| [Ryuk, a lápiz](https://www.artstation.com/artwork/G8W4e1) | Carolina Akemi | Grafito |
| [«How to use it»](https://www.deviantart.com/shoushinnokarera/art/Death-Note-How-to-use-it-79542089) | ShoushinNoKarera | Página de reglas recreada |
| [Death Note](https://www.deviantart.com/giando1611990/art/Death-Note-392623223) | Giando1611990 | L, Light y Ryuk |

En **pixiv** hay miles: la etiqueta **夜神月** tiene unas 3.500
ilustraciones, **L月** unas 990, **月L** unas 650, **リューク** unas 450 y
**L(DEATHNOTE)** unas 300 ⚠️ (cifras del resumen de búsqueda)
([夜神月](https://www.pixiv.net/en/tags/%E5%A4%9C%E7%A5%9E%E6%9C%88),
[L(DEATHNOTE)](https://www.pixiv.net/tags/L(DEATHNOTE)),
[リューク](https://www.pixiv.net/en/tags/%E3%83%AA%E3%83%A5%E3%83%BC%E3%82%AF/illustrations)).
Lo que más se dibuja es **Light con L** (la pareja rival).

**Segunda pasada, fan art con autor** (Safebooru, URL directa leída en
su JSON) ✅: Misa 3360×4096 de
[wjaefinbki3azde](https://x.com/wjaefinbki3azde/status/2031964125707022370)
(el más votado de los cinco); Ryuk 719×1000 vía
[pixiv](http://img33.pixiv.net/img/saipin/13000916.jpg); Near 4937×8000
vía [minitokyo](http://gallery.minitokyo.net/view/635498); Light
3124×4000 (sin origen). Mirar, nunca pegar.

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

La columna «Luz» es de la primera pasada, de memoria; **la luz y la
paleta medidas en fotograma están en 5.5** (segunda pasada).

| Sitio | Qué es y cuándo sale | Luz (1.ª pasada, ver 5.5) |
|---|---|---|
| **El cuarto de Light** | Escritorio, **cajón con doble fondo** (ep. 2, 00:10:32) ✅, ventana, cama. Aquí lee las reglas (ep. 1, 00:04:32) y hace lo de la papa (ep. 8) ✅ | Noche, lámpara de escritorio cálida, el resto azul oscuro |
| **El mundo de los shinigami** | Desierto gris con huesos; juegan con **dados de calavera** (ep. 1, 00:02:01: «髑髏サイコロを振る音») ✅ | Gris sin sol, polvo |
| **El cuartel de la investigación** | Primero hoteles; luego el edificio que construye L. Pantallas por todas partes | Luz de monitores, fría |
| **La Universidad Tōō** (東応大学) | Donde L se presenta (ep. 9, 00:14:39) ✅. Inspirada en la Universidad de Tokio ⚠️ ([Lemon8](https://www.lemon8-app.com/@japanogcspm/7537973584863003142?region=us)) | **Corregido**: la ceremonia es de interior, gris malva cálido (5.5), no «día, luz dura» |
| **Sakura TV** | La cadena que emite las cintas de Kira (ep. 11, 00:02:02) ✅ | Plató, focos |
| **La azotea bajo la lluvia** | L y Light, con **campanas** (ep. 25, 00:10:30 a 00:11:05) ✅ | Gris azul, lluvia |
| **El almacén Yellow Box** | El final: la cuenta de 40 segundos (ep. 36) y la sangre (ep. 37) ✅ | Luz de naves: tiras de sol entre polvo |
| **Wammy's House** | El orfanato de L, Near y Mello en Inglaterra (ep. 27, 00:02:01) ✅ | Invierno, interiores de madera |

Lugares reales que inspiran la serie: la sede de la policía en
**Kasumigaseki 2-1-1**, **Torre de Tokio**, **Shibuya (Dōgenzaka)** y
**Shinjuku** ✅ ([AniTabi](https://www.anitabi.jp/works/296),
[Anime Pilgrimage: 24 sitios](https://www.animepilgrimage.com/ja/map?data=death-note),
[Lemon8](https://www.lemon8-app.com/@japanogcspm/7530328393926558264?region=us)).
Hay una guía de Wammy's House en [pixiv](https://www.pixiv.net/en/artworks/60506907).

### 5.2 Luz ⚠️

- **Contraluz y sombras duras**: la cara de Light **medio en sombra** cuando
  piensa mal. Araki es conocido por el **trabajo de fotografía** (撮影):
  luz con brillo, humo, rayos ✅ (lo dice la presentación de la entrevista de
  [fullfrontal.moe](https://fullfrontal.moe/tetsuro-araki/)); el detalle de
  Death Note no lo pude leer.
- **Los ojos de Light se ponen rojos** en los momentos de Kira ⚠️ (de
  memoria; la wiki relaciona a Light con el rojo y a L con el azul ✅
  [Fandom: Symbolism](https://deathnote.fandom.com/wiki/Symbolism)).
- La lámpara de escritorio es **la única luz cálida** del cuarto.

### 5.3 Paleta

Estimada por mí ⚠️ (compárala con un fotograma antes de fijarla):

| Uso | Hex | Qué es |
|---|---|---|
| Negro del cuaderno | `#0E0E10` | Tapa |
| Fondo de noche | `#141A24` | Cuarto de Light |
| Gris azulado | `#3A4350` | Sombras, lluvia |
| Piel de Ryuk | `#7C8794` | Gris azulado, casi muerto |
| Rojo manzana | `#B3121B` | Manzanas de Ryuk |
| Sangre | `#7A0A0A` | Fresca, oscura |
| Ojos de shinigami | `#E0242E` | Brillo rojo |
| Luz de lámpara | `#E9B872` | Cálida |
| Papel del cuaderno | `#EDE8DC` | Hueso, no blanco puro |
| Castaño de Light | `#7A4B2A` | Pelo |
| Rubio de Misa | `#E6C76A` | Pelo |
| Blanco de L y Near | `#F1F1EE` | Camisa, pijama |
| Vaquero de L | `#4F6B8C` | Pantalón |

Paleta de fans para comparar: `#1f1f1f #4a4a4a #7d7d7d #e0e0e0 #c92c3c`
⚠️ ([color-hex](https://www.color-hex.com/color-palette/1012638),
[ColorMagic](https://colormagic.app/palette/671fe563ab6cc866507fea60)).
**La regla**: gris y negro casi todo, **rojo sólo donde importa**.

### 5.4 Texturas reales equivalentes (CC0)

| Para | Textura | Enlace |
|---|---|---|
| Tapa del cuaderno | Cuero negro | [ambientCG Leather026](https://ambientcg.com/view?id=Leather026), [Leather008](https://ambientcg.com/view?id=Leather008), [Poly Haven: leather](https://polyhaven.com/textures/leather) |
| Hojas | Papel | [Paper001](https://ambientcg.com/view?id=Paper001), [Paper003](https://ambientcg.com/view?id=Paper003), [Paper005](https://ambientcg.com/view?id=Paper005) |
| Escritorio | Madera | [Wood039](https://ambientcg.com/view?id=Wood039), [Wood095](https://ambientcg.com/view?id=Wood095) |

ambientCG es **CC0** (dominio público) ✅ ([ambientCG](https://ambientcg.com/)).
No pude abrir las fichas para ver cuál es oscura o clara: elige al verlas.
La sangre, con `v3/sangre.py` (lo dice `servidor/reglas_del_dueno.md`).

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

| Dónde | Qué letra | Estado |
|---|---|---|
| **Logo «DEATH NOTE»** | Rotulado a mano, **estilo gótico** (blackletter); nunca salió como fuente | ✅ ([Made Good Designs](https://madegooddesigns.com/death-note-font/), [VectorDad](https://vectordad.com/fonts/death-note-font/)) |
| Imitación del logo de la tapa | «**Death Font**», de joshua1985 (gratis, uso personal) | ⚠️ licencia sin comprobar ([FontBolt](https://www.fontbolt.com/font/death-note-font/)) |
| **La «L» de L** | **Cloister Black** (Old English) | ✅ ([TextStudio](https://blog.textstudio.com/death-note-font/), guía de cuadros de diálogo) |
| Reglas «HOW TO USE IT» | Inglés, numeración romana | ✅ el texto; la letra ⚠️ |
| Letra del fansub en la pausa | 華康古印體 (Dynacomware, de pago) | ✅ (estilo en el archivo de subtítulos TSR) |

### 6.2 Letras libres comprobadas por mí

Bajadas de [google/fonts](https://github.com/google/fonts) y revisadas con
fontTools: **todas traen á é í ó ú ñ Á É Í Ó Ú Ñ ¿ ¡ ü** (sí = ✅).

| Letra | Licencia | Para qué | Tildes, ñ, ¿ ¡ |
|---|---|---|---|
| **UnifrakturMaguntia** | OFL | La «L» y el título «Textos» en gótico | ✅ |
| **UnifrakturCook** | OFL | Gótico más grueso, para rótulo grande | ✅ |
| **Pirata One** | OFL | Gótico estrecho y legible, para subtítulos | ✅ |
| **Grenze Gotisch** | OFL | Gótico moderno, legible en el celular | ✅ |
| **IM Fell English** | OFL | Las **reglas**: imprenta vieja, irregular | ✅ |
| **Special Elite** | Apache | Ficha a máquina (lo policial de L) | ✅ |
| **Kalam** | OFL | Letra a mano ordenada (Light) | ✅ |
| **Nothing You Could Do** | OFL | Letra a mano rápida (nombres) | ✅ |
| **Zeyada** | OFL | Garabato (Ryuk) | ✅ |
| **Shippori Mincho B1** / **Zen Old Mincho** | OFL | デスノート, 使い方 en japonés | ✅ (kana y latín) |
| **Nosifer** | OFL | Letra que gotea. **Sólo un acento**; nunca el texto | ✅ |
| Butcherman | OFL | — | ❌ le falta el **¿** |

**Mi elección**: título en **UnifrakturMaguntia**; reglas en **IM Fell
English**; lo escrito a mano en **Kalam**; la «L» sola, en
UnifrakturMaguntia negra sobre blanco.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que la serie pone en pantalla

En Death Note **no hay globo propio**. El texto sale así:

| Soporte | Dónde se ve | Estado |
|---|---|---|
| **La página «HOW TO USE IT»** del cuaderno, en inglés | ep. 1, 00:04:32 a 00:05:30 | ✅ |
| **Ryuk escribió esas instrucciones** «en inglés, la lengua más popular» | ep. 1, 00:16:37 | ✅ |
| **La pausa (eyecatch)**: una regla por episodio; en el 25 y el 26 sólo «Death Note» | cada episodio | ✅ ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/EyeCatch/AnimeAndManga), guía de cuadros) |
| **La pantalla blanca con la «L» gótica** y voz sintética | ep. 2, 00:17:36; ep. 3, 00:01:22 («ＩＣＰＯの皆様 Ｌです») | ✅ |
| **Near usa una «N»** del mismo modo | ep. 28, 00:01:57 («Ｎです») | ✅ el texto; la letra ⚠️ |
| **Las cintas de vídeo de Kira** leídas en la tele (voz sintética: «私はキラです») | ep. 11, 00:03:27 | ✅ |
| **Nombres escritos a mano** en las hojas | ep. 8, 00:18:29, y todo el anime | ✅ |
| **El monólogo interior** de Light: la voz en off lo explica todo | toda la serie | ✅ (lo dice [AniLoop](https://aniloop.org/why-death-notes-potato-chip-scene-actually-works/)) |

### 7.2 Cómo hablan (por el subtítulo)

| Quién | Cómo habla | Ejemplo (minuto) |
|---|---|---|
| **Light** | Educado por fuera («僕»); por dentro, **arrogante y teatral**. Se ríe «**フフフ… ハハハ**» cada vez más fuerte | ep. 8, 00:17:34: «フフフフフ ハハッ フフフ…»; ep. 1, 00:21:00: «新世界の神となる» |
| **L** | **Siempre de usted** («です/ます»), incluso con Light. **Habla en porcentajes** | ep. 9, 00:15:27: «キラである可能性は５％未満»; ep. 10, 00:07:20: «１％ぐらいです»; ep. 11, 00:19:24: «70％以上です» |
| **Ryuk** | Coloquial («俺», «〜だぜ»). Todo le parece **divertido**. **Pide manzanas** | ep. 2, 00:21:04: «やっぱり 人間って面白(おもしれ)え！»; ep. 8, 00:18:03: «マズい 禁断症状が！» |
| **Misa** | **Habla de sí en tercera persona** («ミサ») ✅ ([pixiv 百科](https://dic.pixiv.net/a/%E5%BC%A5%E6%B5%B7%E7%A0%82)). Alarga las vocales, cantarina | ep. 12, 00:09:13: «もっちろん»; ep. 13, 00:10:31: «見ーっけ» |
| **Near** | Tranquilo, frío, **de usted**. Todo es un juego | ep. 27, 00:02:01: «ゲームは勝たなければ»; ep. 28, 00:01:49: «２代目Ｌ はじめまして» |
| **Mello** | De niño, impulsivo; «ロジャー» a cada rato | ep. 27, 00:01:35: «死んだ？ あ… なんで？» |
| **Mikami** | Fanático; «神» (dios) | ep. 31, 00:18:47: «削除»; ep. 32, 00:07:44: «神が舞い降りた» |

### 7.3 Cómo se traduce a una lámina fija

1. **Lo que dice el personaje va escrito en el cuaderno** o en una hoja
   arrancada de él: tinta negra sobre papel hueso. Si es Ryuk, en inglés
   y en español, como la regla del manga (inglés arriba, traducción
   debajo).
2. **El nombre de quien habla** no va en una pestaña: va **en la letra**.
   Light, en Kalam ordenada. Ryuk, garabato. L, **su «L» gótica** en una
   pantalla blanca.
3. **La emoción** no es un globo con pinchos: es **el rojo** (ojos,
   manzana, sangre) y **la sombra** en media cara.
4. Si hace falta un **pensamiento**, imita el monólogo de Light: texto
   sin caja, en cursiva, en una esquina oscura.

### 7.4 Qué NO hacer con el texto

- Una **burbuja blanca redonda** flotando.
- Letras de cómic redondeadas o alegres.
- Escribir las reglas con la letra que gotea: se lee mal y parece de
  Halloween. La sangre va **encima del papel**, no en la letra.
- Inventar «reglas oficiales» que no están: las reglas del canal son del
  canal; las del cuaderno se citan tal cual.

---

## 8 · Los personajes

Datos de carácter y diseño: [Wikipedia: L](https://en.wikipedia.org/wiki/L_(Death_Note)),
[Wikipedia: Ryuk](https://en.wikipedia.org/wiki/Ryuk_(Death_Note)),
[Wikipedia: Light](https://en.wikipedia.org/wiki/Light_Yagami),
[pixiv 百科: 弥海砂](https://dic.pixiv.net/a/%E5%BC%A5%E6%B5%B7%E7%A0%82),
[Namuwiki (coreano)](https://namu.wiki/w/L(%EB%8D%B0%EC%8A%A4%EB%85%B8%ED%8A%B8)),
leídos a través de los resúmenes de búsqueda. Lo que dicen Ohba y Obata
viene del tomo **13: How to Read** (resumido en esas páginas y en
[LiveJournal](https://death-note.livejournal.com/357564.html)). Las frases,
del subtítulo ✅.

### Light Yagami (夜神月) — el protagonista, 2.º en votos

- **Quién es**: el mejor alumno de Japón, aburrido del mundo. Encuentra el
  cuaderno y decide **limpiar el mundo de criminales**: se convierte en
  **Kira**. Obata: «un estudiante brillante que no se mata a estudiar»; su
  diseño salió sin problemas ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Light_Yagami)).
- **Miedo**: que lo descubran. **Qué le importa**: ganar y ser «dios».
- **Con quién**: Ryuk (lo sigue a todas partes), L (rival y «amigo»),
  su padre Sōichirō, su hermana Sayu, Misa (la usa).
- **Cómo saluda**: con cortesía perfecta de buen hijo.
- **Cómo explica**: en su cabeza, paso a paso, con voz de cirujano (ep. 8,
  00:18:12 a 00:18:35).
- **Cómo se ríe**: «フッ… フッ ハハハ…», primero bajo y luego a carcajadas
  (ep. 1, 00:22:32; ep. 2, 00:17:24).
- **Cómo se enfada**: «僕は正義だ！» (ep. 2, 00:16:24), gritando a la tele.
- **Su frase**: «新世界の神となる» («seré el dios del nuevo mundo»,
  ep. 1, 00:21:00) y «計画どおり» (ep. 24, 00:05:42).
- **Cuerpo** ⚠️ (de memoria): recto, ordenado; cuando gana, **sonrisa
  torcida con media cara en sombra** y ojos con brillo rojo.

### L (エル) — el detective, 1.º en votos ✅

- **Quién es**: el mejor detective del mundo. Nadie conoce su cara hasta
  el ep. 6 («Ｌです», 00:01:35). Luego se hace llamar **Ryūzaki** (ep. 6,
  00:03:45).
- **Diseño**: Ohba pidió **su forma de sentarse**, que fuera «en parte
  inglés» y «desganado»; Obata le puso **ojeras negras** para que tuviera
  una cara «que queda bien según el ángulo» ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/L_(Death_Note))).
- **Manías** ✅: **se sienta en cuclillas** (dice que sentado normal
  razona un 40 % peor, ep. 10, 00:08:14), **sólo come dulces**, **coge las
  cosas con dos dedos**, va **descalzo**, ordena todo con manía
  ([Wikipedia](https://en.wikipedia.org/wiki/L_(Death_Note)),
  [Namuwiki](https://namu.wiki/w/L(%EB%8D%B0%EC%8A%A4%EB%85%B8%ED%8A%B8))).
  Pide pastel en el comedor: «ショートケーキ ありますかね？» (ep. 15,
  00:09:07).
- **Cómo habla**: **de usted con todos** y **en porcentajes** (ver §7.2).
- **Cómo se presenta**: sin aviso: «私はＬです» (ep. 9, 00:14:39).
- **Su lado triste**: «寂しいですね… もうすぐ お別れです» (ep. 25,
  00:14:45).
- **Cuerpo** ⚠️: encorvado, **pulgar en el labio**, mirada fija de ojos
  enormes, pelo negro revuelto.

### Ryuk (リューク) — el shinigami

- **Quién es**: «そのノートの落とし主 死神のリューク» («el dueño que dejó
  caer el cuaderno, el shinigami Ryuk», ep. 1, 00:13:00). Lo tiró **porque
  se aburría** (ep. 1, 00:16:51). **Él escribió las instrucciones en
  inglés** (ep. 1, 00:16:37) ✅.
- **No ayuda a nadie**: «キラとＬの どっちの味方もしない» (ep. 3,
  00:20:31). Sólo mira, se ríe y come.
- **Manzanas**: le encantan las del mundo humano («すごいぜ 人間界の
  リンゴは», ep. 1, 00:16:12). Sin ellas, **síndrome de abstinencia**
  (ep. 8, 00:18:03) ✅.
- **Diseño**: Obata quería shinigamis como **«estrellas de rock
  atractivas»**, pero Ryuk no podía ser más guapo que Light: le dio un
  aire de **reptil** ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Ryuk_(Death_Note))).
- **Cómo se ríe**: «フフフフフ…» (ep. 7, 00:18:34); «ククク» ⚠️ (de memoria).
- **Final**: escribe el nombre de Light (ep. 37, 00:18:37 a 00:19:27).
- **Cuerpo** ⚠️: alto, flaco, encorvado, **sonrisa enorme de dientes**,
  ojos amarillos con pupila roja, plumas negras, cinturón con cadena.

### Misa Amane (弥海砂) — la segunda Kira

- **Quién es**: modelo y actriz; la **segunda Kira**, con el cuaderno de la
  shinigami Rem. Se enamora de Light a primera vista ✅
  ([pixiv 百科](https://dic.pixiv.net/a/%E5%BC%A5%E6%B5%B7%E7%A0%82)).
- **Graba vídeos**: manda **cintas** a Sakura TV (ep. 11, 00:03:27) y, al
  ver la respuesta de «Kira», corre a grabar otra: «さあ！　ビデオ ビデオ»
  (ep. 12, 00:09:08) ✅. **Es el personaje que graba**: el más cercano a
  un canal de doblaje.
- **Cómo habla**: **se nombra a sí misma «Misa»** ✅; alarga las vocales:
  «もっちろん», «見ーっけ».
- **Carácter**: impulsiva, infantil, cómica y temeraria, pero lista para
  las coartadas ✅ ([pixiv 百科](https://dic.pixiv.net/a/%E5%BC%A5%E6%B5%B7%E7%A0%82)).
- **Momento duro**: atada y con los ojos vendados (ep. 16, 00:03:21) ✅.
- **Ropa**: **gótica lolita** (ver §16).

### Near (ニア) — el sucesor

- **Quién es**: niño de Wammy's House, sucesor de L con Mello. Se
  presenta a Light como **«Ｎ»** (ep. 28, 00:01:57) ✅. Descubre que
  **Light es Kira** (ep. 33, 00:11:53) y gana en el almacén (ep. 37).
- **Frase**: «ゲームは勝たなければ パズルは解かなければ» («un juego hay que
  ganarlo, un puzle hay que resolverlo», ep. 27, 00:02:01 a 00:02:04) ✅.
- **Cuerpo** ⚠️: sentado en el suelo, una rodilla arriba, **enrollándose
  un mechón blanco** con el dedo; juguetes (puzles blancos, dados,
  muñecos) por todas partes.

### Los secundarios que conviene tener a mano

| Quién | Por qué | Minuto |
|---|---|---|
| **Mello** | Rival de Near, chocolate, cuero negro | ep. 27, 00:01:35 |
| **Mikami** | «削除», el fan de Kira | ep. 31, 00:18:47 |
| **Matsuda** | El novato torpe; **dispara a Light** al final | ep. 37, 00:14:16 |
| **Sōichirō Yagami** | El padre honrado | ep. 6, 00:01:44 |
| **Watari** | El mayordomo de L | ep. 25, 00:16:38 |
| **Rem** | La shinigami de Misa | ep. 13, 00:02:25 |

---

## 9 · ¿Quién es el más querido?

| Encuesta | Resultado | Estado |
|---|---|---|
| **Jump, oficial** | **No hubo** encuesta oficial de personajes; «en internet, L es 1.º» | ⚠️ ([Yahoo! 知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13118117603), una respuesta de usuario) |
| **Nlab (ねとらぼ), 2021** | **1.º L** (397 votos, 35,2 %), **2.º Light** (272, 24,1 %), luego **Near** y **Mello** | ⚠️ las cifras, una fuente ([Nlab](https://nlab.itmedia.co.jp/research/articles/118759/); hay otra encuesta abierta: [ねとらぼ](https://nlab.itmedia.co.jp/research/articles/84945/)) |
| **みんなのランキング** | Ranking vivo de 52 personajes | ⚠️ no pude ver el orden ([ranking.net](https://ranking.net/rankings/best-deathnote-characters)) |
| **Ranker (EE. UU.)** | L, Ryuk y Light arriba | ⚠️ ([Ranker](https://www.ranker.com/list/all-death-note-anime-characters/reference)) |
| **Corea** | L tiene «popularidad de culto» por la postura, el pelo, las ojeras y los dulces | ✅ ([Namuwiki](https://namu.wiki/w/L(%EB%8D%B0%EC%8A%A4%EB%85%B8%ED%8A%B8)), [Wikipedia coreana](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%8A%A4%EB%85%B8%ED%8A%B8%EC%9D%98_%EB%93%B1%EC%9E%A5%EC%9D%B8%EB%AC%BC_%EB%AA%A9%EB%A1%9D)) |

**Conclusión**: **L es el más querido**, por delante del protagonista ✅
(cuatro fuentes coinciden, aunque ninguna es oficial).
Justo el caso que el dueño avisó («quizá un secundario es más querido que
el principal»). **Ryuk** es el más reconocible de lejos (por su cara y la
manzana) ⚠️. **Near** sale 3.º, empatado con Mello: úsalo para la
lámina 2, no para la 1. **Misa** no sale arriba en ninguna encuesta que
pude ver ⚠️.

---

## 10 · Doblaje latino

**Sí hay doblaje latino** del anime, hecho en México, y está en
plataformas: Netflix, Crunchyroll y otras ⚠️ (lista de
[The Dubbing Database](https://dubdb.fandom.com/wiki/Death_Note_(Latin_American_Spanish));
Netflix: [título 70204970](https://www.netflix.com/title/70204970)).

- **Estudio**: AF The Dubbing House / Fogarty Studios ⚠️ (una fuente: la
  guía de cuadros de diálogo, que lo sacó de Doblaje Wiki).
- **Dirección**: **Rolando de Castro**, que además hace de Ryuk. **Se leyó
  el primer tomo del manga** para guiar a los actores ✅ (Doblaje Wiki y
  The Dubbing Database, en los resúmenes).
- **Estreno**: en **Animax**, en su programación de **2008** ✅
  ([Animeol](https://animeol.wordpress.com/2008/05/29/mas-sobre-el-doblaje-de-death-note-en-latinoamerica/),
  [ANMTV, 2009](https://www.anmtvla.com/2009/03/que-opinas-sobre-el-doblaje-latino-de.html)).
- **El doblaje tardó un año y ocho meses**, y **se grabó en el orden de
  los episodios**, cosa rara en México: los actores crecieron con sus
  personajes (lo cuenta Rebeca Gómez) ✅ (The Dubbing Database y Doblaje
  Wiki, en los resúmenes).
- Animax publicó **entrevistas** a Campuzano, Núñez, Coronel y Olguín ✅.

| Personaje | Voz latina | De paso | Estado |
|---|---|---|---|
| **Light** | **Manuel Campuzano** | Chōji (Naruto), Urahara (Bleach), Franky (One Piece), Pantera Negra (MCU) | ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Manuel_Campuzano), [TikTok](https://www.tiktok.com/@theraer17/video/7372463782171397382?lang=es), [YouTube](https://www.youtube.com/shorts/1ibgO7BYhFs)) |
| **L** | **Hugo Núñez** | Nelson Muntz (Los Simpson), Laito (Diabolik Lovers) | ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Hugo_N%C3%BA%C3%B1ez), [Star Con](https://www.facebook.com/starconmx/videos/hugo-n%C3%BA%C3%B1ez-actor-de-doblaje-que-dio-voz-a-l-en-death-note-laito-sakamaki-en-diab/977152957527148/), [YouTube](https://www.youtube.com/watch?v=Mbc2Axk5v20)) |
| **Ryuk** | **Rolando de Castro** (y director) | Snape (Harry Potter), Freddy Krueger | ✅ ([Doblaje Wiki: Ryuk](https://doblaje.fandom.com/es/wiki/Ryuk), [Star Con](https://www.facebook.com/starconmx/videos/rolando-de-castro-actor-de-doblaje-que-di%C3%B3-voz-a-ryuk-en-la-serie-death-note-fre/1933706170137083/)) |
| **Misa** | **Rebeca Gómez** | — | ✅ ([TikTok de ella](https://www.tiktok.com/@rebecagomez_voz/video/7124101453160975621), [YouTube](https://www.youtube.com/watch?v=lEpcImh9vF4)) |
| **Near** | **Bruno Coronel** | — | ✅ ([TikTok de él](https://www.tiktok.com/@bruno_coronel/video/7125570347570564358), [The Dubbing Database](https://dubdb.fandom.com/wiki/Death_Note_(Latin_American_Spanish))) |
| **Mello** | **Javier Olguín** | — | ✅ (Doblaje Wiki y The Dubbing Database, en los resúmenes) |
| Sōichirō | José Lavat ⚠️ | — | ⚠️ dos pistas indirectas ([Propuestas fanon](https://propuestas-fanon.fandom.com/es/wiki/Death_Note_Relight), [TikTok](https://www.tiktok.com/@imitandupoficial/video/7626173420266425621)) |
| Rem, Watari, Matsuda, Mikami | **no lo encontré** | — | — |

Casting: Hugo Núñez **probó para varios personajes** (Matsuda, Ryuk,
Light y L) y se quedó con L ⚠️ (una fuente dice cuatro, otra cinco).

### Frases del doblaje latino

| Frase | Escena | Estado |
|---|---|---|
| **«Tomo una fritura… y la como»** (en latino es **«fritura»**, no «papa frita») | ep. 8, 00:18:35 | ✅ la palabra «fritura» ([YouTube: «LIGHT: ¡¡TOMO UNA FRITURA Y LA COMO!!»](https://www.youtube.com/watch?v=8V1szEGOGTs), [TikTok: «Ahora tomo una papa y me la como»](https://www.tiktok.com/discover/ahora-tomo-una-papa-y-me-la-como)); el orden exacto de las palabras ⚠️ |
| «Yo soy la justicia» | ep. 2, 00:16:24 | ⚠️ (webs de frases de fans; puede venir de fansubs) |
| «Seré el dios del nuevo mundo» | ep. 1, 00:21:00 | ⚠️ (igual) |
| «Los humanos son tan interesantes» (Ryuk) | final de la **película de Netflix** de 2017 | ⚠️ (Doblaje Wiki, en el resumen); en el anime, sin comprobar |

**Antes de rotular una frase del doblaje, escúchala en Netflix.** Si no
se puede, usa una frase **nueva en la voz del personaje**, sin decir que
es del doblaje.

---

## 11 · Música

✅ ([Wikipedia: OST](https://en.wikipedia.org/wiki/Death_Note_original_soundtracks),
[Apple Music](https://music.apple.com/us/album/death-note-original-soundtrack/1611734763);
y el archivo de letras de Moozzi2 en kitsunekko, que pone cada canción en
su episodio)

| Tema | Quién | Episodios | Ambiente |
|---|---|---|---|
| **«the WORLD»** (OP 1) | Nightmare | 1 a 19 | Rock visual kei, épico, de «revolución» («革命の契り») |
| **«Alumina»** (ED 1) | Nightmare | 1 a 19 | Balada oscura |
| **«What's up, people?!»** (OP 2) | Maximum the Hormone | 20 a 37 | Metal a gritos, caótico |
| **«Zetsubō Billy»** (ED 2) | Maximum the Hormone | 20 a 36 | Metal con humor negro |
| **Banda sonora** | **Hideki Taniuchi** (pistas 1-18 del OST 1) y **Yoshihisa Hirano** (19-28) | — | Coros latinos, órgano, guitarra eléctrica |
| «**L's Theme**» | OST | — | Piano y cuerdas: pensar, deducir |
| «**Low of Solipsism**» | OST | — | Coro y órgano: la iglesia de Kira |

Para la lámina: **coro y órgano** = luz de iglesia, vitral rojo;
**L's Theme** = pantallas, azul frío. Los OST se editaron el 21 de
diciembre de 2006 (I) y el 21 de marzo de 2007 (II), en VAP ✅.

---

## 12 · Vídeos

YouTube estaba bloqueado: **no pude ver ninguno**. No doy minutos de
vídeo: los minutos de las escenas están en §2 (subtítulos).

| Vídeo | Para qué |
|---|---|
| **Los 37 episodios, gratis en el canal de YouTube de Viz** (EE. UU.) ✅ ([Anime News Network](https://www.animenewsnetwork.com/news/2023-02-18/viz-media-youtube-channel-adds-death-note-inuyasha-hunter-x-hunter-more-anime/.195055), [Anime Corner](https://animecorner.me/viz-media-makes-death-note-inuyasha-and-more-available-to-stream-on-youtube-in-the-united-states/)) | Sacar fotogramas en HD |
| [Death Note, doblaje latino](https://www.youtube.com/watch?v=LH2By2Gd5vc) | Oír voces |
| [Las voces de Death Note (doblaje latino)](https://www.youtube.com/watch?v=eK5mMMzUcTc) | Reparto |
| [«¡¡Tomo una fritura y la como!!»](https://www.youtube.com/watch?v=8V1szEGOGTs) | La frase en latino |
| [Light come una papa, latino](https://www.youtube.com/watch?v=IFHxQOJT8NA) | Igual |
| [Entrevista a Hugo Núñez (L)](https://www.youtube.com/watch?v=Mbc2Axk5v20) | Cómo hizo a L |
| [Manuel Campuzano grabando como Light](https://www.youtube.com/shorts/1ibgO7BYhFs) | Cómo suena Light hoy |
| [Rebeca Gómez firmando (Misa)](https://www.youtube.com/watch?v=lEpcImh9vF4) | — |
| [El IMPACTO de L en Death Note](https://www.youtube.com/watch?v=9iyGff0-jng) | Análisis en español |
| [Lo que revelan las conversaciones entre Light y L](https://www.youtube.com/watch?v=vcknhV5VkGk) | Análisis en español (2024) |
| [Por qué perdió Light Yagami](https://www.youtube.com/watch?v=462Ia6vGres) | Final explicado |
| [Españoles reaccionan: latino vs. español](https://www.youtube.com/watch?v=lHUKue4evAU) | Comparar doblajes |
| [The Brilliance of Death Note's Potato Chip Scene](https://www.youtube.com/watch?v=eoHC_rfX50U) | La papa, en inglés |
| Bilibili: [计划通, doblajes comparados](https://www.bilibili.com/video/BV1Eb411L7Sn/) y [la risa de Light](https://www.bilibili.com/video/BV1Ny4y1e7T8/) | Fandom chino |

Tráileres: los que salen en Netflix con «Death Note | Tráiler» son **de
la película de 2017**, no del anime ([Netflix](https://www.youtube.com/watch?v=u2GX_z65k-s)).
**No los uses** de referencia.

TikTok: retos de doblaje con Light y Misa
([SDV servicios de voz: Light](https://www.tiktok.com/@sdv_serviciosdevoz/video/7187095780468034821),
[Misa](https://www.tiktok.com/@sdv_serviciosdevoz/video/7145238036119309573)).
**Son justo el tipo de guion que iría en #textos.**

---

## 13 · Videojuegos de la franquicia

| Juego | Qué es | Interfaz |
|---|---|---|
| **Death Note: Kira Game** (DS, Konami, 15-feb-2007, sólo Japón) | Juego de deducción: eres Kira o L. Fases de **investigación, votación y «L o Kira»**. 19 personajes ✅ ([StrategyWiki](https://strategywiki.org/wiki/Death_Note:_Kira_Game), [RetroAchievements](https://retroachievements.org/game/15499)) | Retratos con texto en caja ⚠️ (no vi capturas) |
| **L o Tsugu Mono** (DS, 2008 ⚠️) | Secuela ✅ (con Near y Mello ⚠️, de memoria) | ⚠️ |
| **Death Note: Killer Within** (Grounding y Bandai Namco, 5-nov-2024; PS4, PS5, PC) | Deducción social para 10: Kira, seguidores, L e investigadores. **Kira escribe en el cuaderno y se le ve con él en la mano**. L guía la reunión. En 2025 añadieron **X Kira** y **N** ✅ ([Bandai Namco](https://www.bandainamcoent.com/news/death-note-killer-within-available-now-on-playstation-and-pc), [Steam Deck HQ](https://www.steamdeckhq.com/game-reviews/death-note-killer-within/), [ANN](https://www.animenewsnetwork.com/news/2025-08-27/death-note-killer-within-social-deduction-game-adds-x-kira-n-roles-3d-mode/.228148), [Screen Rant](https://screenrant.com/death-note-killer-within-review-playstation/)) | Fase de reunión con votos ⚠️ |

**Para #textos**: la **reunión** de Killer Within es un **diálogo para
varias voces**. Buena idea de guion, no de lámina.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### Lo que todos reconocen

- **La papa frita** (ep. 8): el meme más grande; en inglés «I'll take a
  potato chip… and EAT IT!» (Brad Swaile) ✅ ([Know Your Meme](https://knowyourmeme.com/memes/just-according-to-keikaku),
  [ComicBook.com](https://comicbook.com/anime/news/death-note-potato-chip-scene-reddit/));
  en latino, **«fritura»** (§10). En chino, «一边学习，一边杀人，顺便吃薯片»
  ([Bilibili](https://www.bilibili.com/video/BV1Ww411F7hv/)).
- **«Just according to keikaku»** (ep. 24): un fansub puso «(T/N: keikaku
  means plan)»; es meme desde 2008 ✅ ([Know Your Meme](https://knowyourmeme.com/memes/just-according-to-keikaku),
  [萌娘百科: 计划通](https://zh.moegirl.org.cn/zh-hans/%E8%AE%A1%E5%88%92%E9%80%9A),
  [Namuwiki](https://namu.wiki/w/%EC%95%BC%EA%B0%80%EB%AF%B8%20%EB%9D%BC%EC%9D%B4%ED%86%A0)).
- **La postura de L** (cuclillas, pulgar al labio) ✅.
- **Ryuk y las manzanas** ✅.
- **«削除» de Mikami** (ep. 31) ⚠️ (meme de memoria; el minuto ✅).
- **La risa de Light** ✅ ([Bilibili](https://www.bilibili.com/video/BV1Ny4y1e7T8/)).
- **La pareja L y Light** domina el fan art (pixiv, §4.2).
- Tendencias en TikTok: cuadernos «Death Note» hechos a mano y cosplay
  de Ryuk ✅ ([TikTok](https://www.tiktok.com/discover/death-note-book-trend),
  [CapCut](https://www.capcut.com/explore/death-note-tiktok)).

### Qué NO hacer (lo que un fan notaría)

- **Mezclar la película de Netflix (2017)** con el anime: otro Light,
  otro Ryuk (el concept de Luca Nemolato es de la película).
- **Usar arte hecho con IA**: hay fondos «4K» de Ryuk hechos con
  Midjourney ([4kwallpapers](https://4kwallpapers.com/anime/ryuk-death-note-ai-14431.html)).
  El dueño no quiere que parezca IA.
- **Poner a L sentado normal** o con zapatos. **Poner a Ryuk con
  colores alegres**. **Poner a Near con ropa de color**.
- **Sangre en cada muerte**: en el cuaderno **se muere de infarto** (regla
  IV). La sangre de verdad está **al final** (ep. 37) y en la manzana roja.
  La lámina puede ser sangrienta, pero **la sangre sobre el papel, no
  gente destripada**.
- **Escribir un nombre real** en el cuaderno de la lámina: en un servidor
  de gente real, **nunca**. Se escriben títulos de guiones, no nombres de
  personas.
- Poner la «L» en cualquier letra gótica con adornos: es **una sola
  letra negra sobre blanco**.

---

## 15 · Poses analizadas por personaje

El minuto es del subtítulo ✅. **Lo que se ve (postura, manos, mirada)
es de memoria** ⚠️: saca el fotograma del episodio de Viz o Netflix y
compruébalo antes de usarlo. Columna «Sirve para»: presentar, explicar,
celebrar, regañar, pensar, animar.

### Light

| # | Ep., minuto | Qué dice | Qué hace ⚠️ | Sirve para |
|---|---|---|---|---|
| 1 | 1, 00:04:32 | «“使い方”» | Sentado al escritorio, el cuaderno abierto en las dos manos, lee con desdén | **explicar** |
| 2 | 1, 00:13:25 | «待ってたよ リューク» | Se gira en la silla hacia Ryuk, tranquilo, sin miedo | presentar |
| 3 | 1, 00:21:00 | «新世界の神となる» | De pie, de noche, mirada alta, sonrisa | **presentar** |
| 4 | 2, 00:16:24 | «僕は正義だ！» | Grita a la tele, puño cerrado | **regañar** |
| 5 | 2, 00:17:24 | «ハハハハハッ» | Risa desatada, cabeza atrás | celebrar (villano) |
| 6 | 8, 00:18:35 | «ポテチを取り 食べる» | Mano en la bolsa, papa en el aire, cara de guerra | **animar** (humor) |
| 7 | 24, 00:05:42 | «計画どおり» | Media cara en sombra, sonrisa torcida | **pensar** |
| 8 | 36, 00:21:12 | «ニア 僕の勝ちだ» | De pie en el almacén, cabeza gacha, sonríe | celebrar |
| 9 | 37, 00:10:16 | «新世界の神だ» | Brazos abiertos, confiesa | presentar (final) |

### L

| # | Ep., minuto | Qué dice | Qué hace ⚠️ | Sirve para |
|---|---|---|---|---|
| 1 | 2, 00:17:36 | «信じられない» | Sólo la **«L» gótica** en pantalla blanca | **presentar sin cara** |
| 2 | 6, 00:01:35 | «Ｌです» | De pie, encorvado, manos en los bolsillos, descalzo | **presentar** |
| 3 | 9, 00:14:39 | «私はＬです» | En la ceremonia, junto a Light, lo dice sin mirarlo | presentar (secreto) |
| 4 | 9, 00:15:27 | «キラである可能性は５％未満» | Pulgar en el labio | **pensar** |
| 5 | 10, 00:08:14 | «推理力が40％減です» | En cuclillas sobre la silla del café | **explicar** |
| 6 | 10, 00:01:28 | (tenis) | En la pista, raqueta, postura rara | acción |
| 7 | 15, 00:09:07 | «ショートケーキ ありますかね？» | Pide pastel con la cara seria | **animar** (humor) |
| 8 | 25, 00:10:30 | «鐘の音が…» | En la azotea, empapado, mirando al cielo | pensar (triste) |
| 9 | 25, 00:13:36 | «マッサージもつけますよ» | De rodillas, seca los pies de Light | cuidar |
| 10 | 25, 00:14:45 | «寂しいですね» | Sentado, de perfil, mirada baja | despedir |

### Ryuk

| # | Ep., minuto | Qué dice | Qué hace ⚠️ | Sirve para |
|---|---|---|---|---|
| 1 | 1, 00:02:01 | (dados de calavera) | Tumbado en el mundo shinigami, aburrido | presentar el mundo |
| 2 | 1, 00:13:00 | «死神のリュークだ» | Aparece detrás de Light, enorme, sonrisa de dientes | **presentar** |
| 3 | 1, 00:16:12 | «すごいぜ 人間界のリンゴは» | Muerde una manzana roja | **animar** |
| 4 | 1, 00:16:37 | «英語で説明を付けたんだぜ» | Explica que él escribió las reglas | **explicar** |
| 5 | 1, 00:21:04 | «やっぱり 人間って… 面白っ！» | Carcajada, brazos abiertos | **celebrar** |
| 6 | 2, 00:10:32 | «なるほど 二重底か» | Asoma la cabeza al cajón | pensar |
| 7 | 3, 00:20:09 | «死神の目玉の値段は…» | Se inclina hacia Light, ojos rojos | explicar (el trato) |
| 8 | 8, 00:18:03 | «マズい 禁断症状が！» | Se retuerce, del revés | humor |
| 9 | 37, 00:18:37 | «お前の負けだ 月» | Saca su cuaderno y escribe | **regañar** (final) |

### Misa

| # | Ep., minuto | Qué dice | Qué hace ⚠️ | Sirve para |
|---|---|---|---|---|
| 1 | 11, 00:03:27 | «私はキラです» (su cinta, voz sintética) | Sólo la cinta en la tele | presentar |
| 2 | 12, 00:09:08 | «さあ！　ビデオ ビデオ» | Corre a grabar la respuesta | **animar a grabar** |
| 3 | 12, 00:14:39 | «ウフッ» | Posa para la cámara en una sesión de fotos | **celebrar** |
| 4 | 13, 00:10:31 | «見ーっけ» | Ve a Light entre la gente, con los ojos de shinigami | presentar |
| 5 | 13, 00:15:26 | «は… はじめまして» | En la puerta de los Yagami, tímida | **presentar** |
| 6 | 15, 00:10:17 | «え～ ホント？　うれしい！» | L le dice que es su fan; se emociona | celebrar |
| 7 | 16, 00:03:21 | «目隠しだけでも取って» | Atada y con los ojos vendados | **no usar** |

### Near

| # | Ep., minuto | Qué dice | Qué hace ⚠️ | Sirve para |
|---|---|---|---|---|
| 1 | 27, 00:02:01 | «ゲームは勝たなければ» | De niño, en el suelo, con un puzle blanco | **explicar** |
| 2 | 28, 00:01:49 | «２代目Ｌ はじめまして» | Voz tras una **«N»** en pantalla | **presentar** |
| 3 | 28, 00:15:31 | «結構 難しいことを 簡単に言いますね» | Frío, girando un mechón | regañar suave |
| 4 | 33, 00:11:53 | «Ｌキラは夜神 月…» | Sentado entre juguetes, concluye | **pensar** |
| 5 | 37, 00:04:03 | «さっき 君は “僕の勝ちだ”と言った» (quién lo dice ⚠️) | En el almacén, frente a Light | regañar |

---

## 16 · Vestuario ⚠️

De guías de cosplay (no de hojas de modelo oficiales) y de memoria.
**Compara con el fotograma.**

| Personaje | Ropa icónica | Colores ⚠️ | Accesorios y pelo |
|---|---|---|---|
| **Light** (instituto) | Camisa blanca, **corbata roja**, americana caqui, pantalón oliva ✅ ([Carbon Costume](https://carboncostume.com/title/death-note/), [Costumet](https://www.costumet.com/death-note/light-yagami/)) | americana `#B79C6E`, corbata `#8E1B1B` | Pelo castaño liso con flequillo; reloj de pulsera (luego esconde un trozo del cuaderno en él ⚠️) |
| **Light** (adulto) | Traje oscuro, camisa blanca, corbata | `#2B2F36` | — |
| **L** | **Camiseta blanca de manga larga y vaqueros anchos**, descalzo ✅ ([Carbon Costume](https://carboncostume.com/title/death-note/), [Lemon8](https://www.lemon8-app.com/@smexymarie22/7462094351515304494?region=us)) | `#F1F1EE`, `#4F6B8C` | Pelo negro revuelto; **ojeras**; piel muy pálida |
| **Misa** | **Gótica lolita**: corsé de cuero negro, **gargantilla negra**, **cruz de plata**, falda negra, mangas y medias de encaje, botas; uñas rojas ✅ ([Carbon Costume: Misa](https://carboncostume.com/misa-amane/), [Anime Fire](https://animefire.com/2023/09/10/misa-cosplay-guide-how-to-cosplay-from-death-note/)) | negro `#111`, plata `#C9CCD1` | **Rubia con dos coletas finas** y flequillo |
| **Near** | **Pijama blanco**; en el anime, el pantalón cambia de color ✅ ([Carbon Costume](https://carboncostume.com/title/death-note/)) | `#F2F2F2` | Pelo blanco rizado; siempre un juguete |
| **Mello** | Cuero negro, rosario ⚠️ | `#141414` | Rubio, media melena; **tableta de chocolate** ✅ |
| **Ryuk** | Plumas negras, pantalón ajustado, cinturón con cadena y calavera ⚠️; **cuaderno colgado de la cadera** ⚠️ | piel `#7C8794` | Pelo en púas negras, ojos amarillos y rojos ⚠️ |

**Lo que todos reconocen**: Light con **camisa blanca y corbata roja**;
L **de blanco y vaqueros, en cuclillas**; Misa **de negro con la cruz**;
Ryuk **con la manzana**.

---

## 17 · Paisajes y fondos de pantalla

### Los sitios, con su luz ⚠️

Ver §5.1. Resumen: **noche azul con lámpara cálida** (cuarto de Light),
**gris sin sol** (mundo shinigami), **lluvia gris azul** (azotea de L),
**tiras de sol entre polvo** (almacén del final).

### Fondos de pantalla

| Qué | Tamaño | Enlace | Nota |
|---|---|---|---|
| «Shadowed Pact»: Light y Ryuk | 3840×2160 | [Wallpaper Abyss 1182462](https://wall.alphacoders.com/big.php?i=1182462) | Autor sin comprobar |
| Ryuk | 3840×2160 | [Wallpaper Abyss 961726](https://wall.alphacoders.com/big.php?i=961726) | Subido por ncoll36 |
| L, Ryuk y el cuaderno | 4K | [Wallpapers Clan](https://wallpapers-clan.com/desktop-wallpapers/death-note-l-and-ryuk-book/) | ⚠️ |
| Light y Ryuk | HD | [Wallpapers Den](https://wallpapersden.com/death-note-light-yagami-ryuk-wallpaper/) | ⚠️ |
| Varios | 1080p a 5K | [WallpaperFlare](https://www.wallpaperflare.com/search?wallpaper=death+note) | Mezcla oficial y fan |
| Ryuk «4K» | 3840×2160 | [4kwallpapers](https://4kwallpapers.com/anime/ryuk-death-note-ai-14431.html) | **Hecho con IA (Midjourney): NO usar** |

Los tamaños son los que dicen las páginas en el resultado de búsqueda ⚠️.

---

## 18 · Guía para generar con IA (Firefly, Canva)

Sólo para **fondos, luz o tanteos de pose**. **Nunca** para sacar a los
personajes finales: esos salen de fotogramas o del artbook, recortados
con `v3/integrar.py`.

### Rasgos que nunca cambian

- **Light**: chico japonés de 17-18 años, pelo castaño liso con flequillo
  hasta las cejas, ojos castaños rojizos, camisa blanca y corbata roja.
- **L**: joven delgado, **pelo negro muy revuelto**, **ojeras negras**,
  piel pálida, camiseta blanca de manga larga, vaqueros, **descalzo, en
  cuclillas**, pulgar en el labio.
- **Ryuk**: shinigami muy alto y flaco, piel gris azulada, **sonrisa
  enorme con muchos dientes**, ojos amarillos con pupila roja, pelo negro
  en púas, plumas negras, **manzana roja en la mano**.
- **El cuaderno**: **tapa negra lisa** con «DEATH NOTE» en letras góticas
  plateadas o blancas; hojas **hueso con renglones**.

### Estilo

- Línea **fina y precisa**, realista para ser anime (Obata); sombras
  **duras**, en bloques; mucho **negro**.
- Luz: **una sola fuente cálida** en un cuarto azul oscuro; o contraluz
  de ventana. Brillo rojo en ojos.
- Encuadre: **picado o contrapicado**, primeros planos de ojos y manos,
  el cuaderno en primer plano.

### Palabras que ayudan

`dark psychological thriller anime, Madhouse 2006 style, Takeshi Obata
character design, dramatic chiaroscuro, single desk lamp, deep blue
shadows, crimson accents, black leather notebook, gothic lettering,
rain, cinematic low angle, film grain`

### Palabras que lo estropean

`chibi`, `kawaii`, `pastel`, `bright colors`, `cartoon`, `3D render`,
`Netflix 2017`, `gore`, `zombie`, `blood everywhere`, `neon`. Y nunca
pidas el logo ni la «L»: **esos se ponen a mano con la letra**.

### Qué imágenes usar como referencia

- **De estilo**: un fotograma del ep. 1 (00:04:32, Light con el cuaderno)
  y del ep. 25 (00:10:30, la azotea con lluvia).
- **De pose**: §15 (las filas en **negrita**).
- **De color**: la paleta de §5.3.

---

## 19 · Tres conceptos para la lámina de #textos

Los tres usan los textos de §0. Donde pongo una frase «en la voz del
personaje» es **mía**, no del doblaje latino. Recortes siempre por
`v3/integrar.py` y comprobados a 1:1. Sangre, con `v3/sangre.py`.

> [!tip] Dos datos que dan pie a todo
> - **Las reglas del cuaderno las escribió Ryuk**, «en inglés, la lengua
>   más popular» (ep. 1, 00:16:37) ✅. Y hay reglas **en la primera página y
>   en la contratapa**: «裏表紙のほうの “How to use”» (ep. 24, 00:11:55) ✅.
> - Light, sobre las reglas: «ルールとは いつの世界も 神とされる者によって
>   作られるものだ» («las reglas, en cualquier mundo, las hace quien se
>   tiene por dios», ep. 24, 00:15:13) ✅.

### Concepto A — «Cómo se usa» (el cuaderno del plan, mejorado)

- **Objeto y sitio**: **el Death Note abierto sobre el escritorio de
  Light**, de noche (su cuarto, ep. 1, 00:04:32). Al lado: **una manzana
  roja mordida**, un bolígrafo, **la bolsa de papas** y **el cajón a medio
  abrir con el doble fondo** (ep. 2, 00:10:32). En Blender: cuaderno (caja
  con tapas y hojas curvadas), manzana, cajón. Texturas: cuero
  [Leather026](https://ambientcg.com/view?id=Leather026), papel
  [Paper003](https://ambientcg.com/view?id=Paper003), madera
  [Wood039](https://ambientcg.com/view?id=Wood039).
- **Personaje**: **Ryuk**, porque **él escribió las instrucciones**.
  Detrás del escritorio, inclinado sobre el cuaderno, con la manzana en la
  mano. Pose: ep. 1, 00:13:00 (aparece detrás de Light) o 00:16:12 (la
  manzana). La mano que sostiene la manzana **se ve entera, con su brazo**
  (regla 7 del dueño).
- **Cómo habla**: como en el manga, **la regla en inglés arriba y la
  traducción debajo**. Su frase, **garabateada en el margen** del cuaderno
  (letra Zeyada), sin globo: **«Las escribí yo. Léelas, que me aburro.»**
- **Dónde va cada texto**:
  - Arriba de la página izquierda, en gótico (UnifrakturMaguntia):
    **Textos**. Debajo, pequeño: *HOW TO USE IT*.
  - En IM Fell English: **Guiones para practicar**. **Monólogos,
    diálogos, escenas y narraciones.**
  - Las reglas, numeradas en romano: **I. Un hilo por guion.**
    **II. Llena la ficha.** **III. Di si se puede usar libre o hay que
    pedir permiso.**
  - Página derecha, **a mano** (Kalam), como Light escribe los nombres:
    **Tipo** Monólogo, **Voces** Hombre adulto, **Duración** 40 segundos,
    **Tono** Contenido, **Uso** Libre para usar. Es el hilo de ejemplo del
    foro, y el **40** es el de la regla del cuaderno.
- **Para que no quede plano**: lámpara de escritorio **cálida** a un lado,
  cuarto **azul oscuro**; la manzana **desenfocada en primer plano**; los
  ojos rojos de Ryuk como único brillo del fondo; **una gota de sangre**
  que cae de la punta del bolígrafo sobre el margen (sangre.py), y la
  sombra de Ryuk sobre la página derecha.
- **Lámina 2**: **el cajón con doble fondo**, abierto: las nueve
  etiquetas como fichas de papel escondidas en el hueco, en tres montones
  (Qué es, Cómo se usa, Cuántas voces).

### Concepto B — «Lo lee otro» (L y la emisión de Lind L. Tailor)

- **Objeto y sitio**: **la mesa del cuartel de la investigación** con un
  **televisor** que emite la pantalla blanca de la «L» (ep. 2, 00:17:36;
  **en la pantalla va el fotograma real**, regla 2 del dueño). Delante,
  **el guion impreso** que leyó Lind L. Tailor: un taco de folios con
  clip. En Blender: tele de tubo, folios, clip, taza y **una torre de
  terrones de azúcar**.
- **Personaje**: **L, el más querido** (§9). **En cuclillas en la silla**,
  sujetando el guion **con dos dedos**. Pose: ep. 10, 00:08:14 (en
  cuclillas) o ep. 9, 00:15:27 (pulgar en el labio).
- **Cómo habla**: L habla **de usted y en porcentajes**. Su frase, **a
  máquina** (Special Elite) en un post-it pegado al guion: **«Si llenas la
  ficha, la probabilidad de que alguien lo grabe sube mucho.»**
- **Dónde va cada texto**:
  - Portada del guion, a máquina: **Textos**. **Guiones para practicar.**
  - Debajo, en casillas, como una ficha policial: **Tipo, Voces,
    Duración, Tono, Uso**, ya llenas con el ejemplo del foro.
  - Tres folios abiertos en abanico, uno por regla: **Un hilo por guion**,
    **Llena la ficha**, **Di si es libre o pide crédito**.
  - En la esquina del guion, **un sello rojo** con una huella: **Pide
    crédito**. Al lado, un sello en tinta: **Libre para usar**.
- **Para que no quede plano**: la tele **ilumina a L por delante** en
  blanco frío; detrás, oscuridad; la torre de azúcar **desenfocada en
  primer plano**; la huella roja es la única mancha de color.
- **Lámina 2**: el **puzle blanco de Near** a medio armar en el suelo
  (ep. 27, 00:02:04: «パズルは解かなければ»): cada pieza, una etiqueta; la
  pieza que falta, **Para dos voces**.

### Concepto C — «La cinta de Misa» (grabar un guion)

- **Objeto y sitio**: **el tocador de Misa** con **una cinta de vídeo**, su
  sobre para **Sakura TV** y **una cámara de vídeo** con la luz roja de
  grabar encendida (ep. 11, 00:02:24: las cintas que llegan al canal; ep.
  12, 00:09:08: «さあ！　ビデオ ビデオ»). En Blender: cinta VHS con su
  etiqueta, sobre, cámara, espejo.
- **Personaje**: **Misa**, porque **es la que graba**. Pose: ep. 12,
  00:14:39 (posando) o 00:09:08 (va corriendo a grabar). Ropa gótica,
  **cruz de plata**.
- **Cómo habla**: **en tercera persona**, cantarina. Su frase en la
  **etiqueta de otra cinta**, a mano (Kalam), con un corazón negro:
  **«Misa ya grabó el suyo. ¡Ahora tú!»**
- **Dónde va cada texto**:
  - Lomo de la cinta: **Textos**.
  - Etiqueta grande de la cinta: **Guiones para practicar**.
  - En el sobre, como remitente y destino: **Un hilo por guion**.
  - En el papel que Misa lee delante de la cámara: la **ficha** (Tipo,
    Voces, Duración, Tono, Uso) y **Di si es libre o pide crédito**.
- **Para que no quede plano**: **luz roja** del piloto de la cámara en
  primer plano; bombillas del espejo de camerino detrás; una **mancha de
  pintalabios rojo** en el sobre que pasa por sangre (sangre.py, con
  cuidado).
- **Riesgo**: Misa no sale arriba en las encuestas ⚠️. Es la opción **más
  «de doblaje»**, pero la menos querida de las tres.

### ¿Cuál primero?

**A**. Es el objeto que pidió el servidor, se hace entero en Blender, y la
relación con el canal es **literal**: el cuaderno trae instrucciones
escritas y el foro también. Ryuk es reconocible al instante.
**Para no dejar fuera a L**, el más querido, se puede usar **B como
lámina 2** del canal, o poner a L en A **en el borde del encuadre**, en
cuclillas en una silla, leyendo el cuaderno con dos dedos (así lo tienen
en el ep. 24, 00:11:55 a 00:13:09, cuando leen las reglas de la contratapa)
⚠️ (que L lo sostenga así es de memoria).

---

## 20 · Lo que no pude verificar

- **Imágenes**: no se pudo bajar nada (Fandom, Wikipedia, YouTube,
  Sketchfab, pixiv, Madhouse: bloqueados). **Sin hojas de contacto.**
- **Lo que se ve en cada fotograma**: las posturas de §15 son de memoria.
- **Frases exactas del doblaje latino**: sólo confirmé que la papa es
  «**fritura**». «Yo soy la justicia» y «Seré el dios del nuevo mundo»
  pueden ser de fansubs.
- **Voces latinas** de Sōichirō (José Lavat, dudoso), Rem, Watari,
  Matsuda, Mikami.
- **El estudio** del doblaje: una sola fuente.
- **Encuesta oficial** de la Jump: parece que no hubo; lo dice un usuario
  de Yahoo! 知恵袋.
- **La letra de las reglas** «HOW TO USE IT» del anime y del manga.
- **Las pausas (eyecatch)**: qué regla sale en cada episodio y cómo es el
  fondo.
- **Capturas de los juegos** (Kira Game, Killer Within).
- **Licencias de Sketchfab**: sólo por el resultado de búsqueda.
- **Hex de la paleta**: estimados, no medidos.
- La **entrevista de Araki** sobre color (fullfrontal.moe) y la de la web
  de Madhouse: sólo resúmenes.

---

## 21 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)

- WebFetch bloqueado (EGRESS_BLOCKED): doblaje.fandom.com (API),
  nlab.itmedia.co.jp, madhouse.co.jp, fullfrontal.moe,
  animeol.wordpress.com. Dejé de probar después de cinco.
- curl sin respuesta: api.sketchfab.com, sketchfab.com, dafont.com,
  fontmeme.com, api.polyhaven.com, ambientcg.com.
- GitHub responde (git y raw; `api.github.com` dio 200).
- `herramientas/investigar_serie.py` no se corrió: sin Fandom no hay
  hojas. Por eso **no hay `hojas/`**.

### Búsquedas web (49)

| # | Idioma | Búsqueda (dominio si lo hubo) |
|---|---|---|
| 1 | ES | Death Note doblaje latino reparto Light L Misa Near Ryuk (doblaje.fandom.com) |
| 2 | ES | «Death Note» doblaje latino Misa, Near, Mello, Matsuda, Sōichirō, AF The Dubbing House, Rolando de Castro |
| 3 | ES | Death Note latino «Near» «Hugo Núñez» «Manuel Campuzano» «Rebeca Gómez» |
| 4 | ES | Death Note latino «papa frita» «me la comeré» |
| 5 | ES | frases Death Note latino «dios del nuevo mundo» «la justicia» Ryuk «humanos son» |
| 6 | EN | Death Note official popularity poll Jump L Light Mello Near |
| 7 | JA | デスノート 人気投票 結果 ジャンプ 1位 |
| 8 | EN | Death Note eyecatch rules «How to use it» each episode |
| 9 | EN | Death Note notebook cover font / logo typeface |
| 10 | ES | manga en español: reglas «Cómo usarlo» «cuyo nombre sea escrito…» |
| 11 | ES | «Death Note» latino «libreta» Ryuk Light |
| 12 | JA | デスノート 荒木哲郎 インタビュー ポテチ 北尾勝 美術監督 色彩設計 |
| 13 | EN | Tetsuro Araki potato chip scene interview |
| 14 | EN | Araki color cinematography (fullfrontal.moe) |
| 15 | EN | Kira Game DS gameplay interface L o Tsugu Mono |
| 16 | EN | Death Note: Killer Within gameplay UI |
| 17 | EN | Death Note notebook 3D model CC (sketchfab.com) |
| 18 | EN | «How to use it» rules page font / replica |
| 19 | JA | DEATH NOTE 20周年 小畑健 画集 Blanc et Noir キービジュアル |
| 20 | EN | anime key visual, DVD and Blu-ray covers, Viz |
| 21 | EN | OST Hirano, Taniuchi, «the WORLD», «What's up, people?!», «Alumina», «Zetsubō Billy» |
| 22 | EN | Know Your Meme: keikaku, potato chip |
| 23 | ES/EN | tendencia TikTok 2025-2026 Death Note |
| 24 | EN | noticias 2026: nuevo anime, serie de Netflix, musical |
| 25 | ES | doblaje latino: estudio, año 2008, Animax, Hugo Núñez, Bruno Coronel |
| 26 | ES | reparto latino: Rolando de Castro, Bruno Coronel, Javier Olguín, Sōichirō, Rem… |
| 27 | ES | «papita» «papa frita» «y me la comeré» (salió «fritura») |
| 28 | ES | Ryuk latino Rolando de Castro «humanos» «interesantes» |
| 29 | EN | cosplay: ropa y colores de Light, L, Misa, Near, Mello |
| 30 | JA | デスノート 聖地 モデル 東応大学 捜査本部 |
| 31 | EN | CC0 cuero negro, papel, madera (Poly Haven, ambientCG) |
| 32 | EN | ambientCG paper, wood, leather (ambientcg.com) |
| 33 | EN | wallpaper 4K 3840×2160 (alphacoders, wallhaven, wallpapercave) |
| 34 | EN | fan art Ryuk Light L (artstation.com, deviantart.com, pixiv.net) |
| 35 | JA | デスノート イラスト 人気 (pixiv.net) |
| 36 | EN | L: postura, pulgar, dulces, dedos, descalzo, diseño de Obata |
| 37 | JA | 弥海砂 一人称 ゴスロリ / ニア 玩具 パズル (pixiv 百科) |
| 38 | JA | デスノート アイキャッチ ルール 英文 «HOW TO USE IT» |
| 39 | ZH | 死亡笔记 名场面 薯片 计划通 L 坐姿 (Bilibili) |
| 40 | KO | 데스노트 명대사 계획대로 감자칩 L 인기 (나무위키) |
| 41 | EN | paleta de color hex Death Note |
| 42 | EN | «a-Kira Story» 2020, «Death Note Short Stories» |
| 43 | ES | voz latina de Rem, Watari, Sōichirō, Matsuda, Mikami |
| 44 | ES | «soy la justicia» «yo soy L» «tal como lo planeé» en latino |
| 45 | ES/EN | tráiler oficial del anime (Viz, Netflix Latinoamérica) |
| 46 | EN | Killer Within: fase de reunión, interfaz, roles |
| 47 | EN | Ohba y Obata en «How to Read»: diseño de Ryuk y Light |
| 48 | ES | entrevista a Hugo Núñez: casting de L |
| 49 | ES | análisis de Death Note en español (youtube.com) |

### GitHub (sin cupo)

- [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/DEATH%20NOTE):
  270 archivos. Usé **el japonés de Netflix (37 episodios)**, **el
  inglés de fans TSR (ep. 1-24)**, alineado con el japonés (desfase medio
  de 80 s en todos) y **las letras de OP y ED de Moozzi2**. Los dejé en mi
  carpeta temporal, **no en el repositorio**.
- [google/fonts](https://github.com/google/fonts): 45 familias,
  comprobadas con fontTools (tildes, ñ, ¿, ¡, ü) y con una hoja de muestra.

### Fuentes consultadas por tipo

- **Oficiales**: Madhouse (ficha y entrevista a Araki, sólo resumen), Viz
  (anime, Short Stories, YouTube), Bandai Namco (Killer Within), Steam,
  Shūeisha (artbook, por tiendas: HLJ, Books.or.jp, 漫画全巻), Netflix.
- **Otros idiomas**: japonés (Yahoo! 知恵袋, ねとらぼ, みんなのランキング,
  pixiv 百科, AniTabi, Anime Pilgrimage, YOSHI BLOG, Anime Staff DB),
  chino (Bilibili, 萌娘百科, Baidu), coreano (Namuwiki, Wikipedia).
- **Wikis**: Fandom (Death Note, Doblaje, Dubbing Database, Tropedia),
  TV Tropes, Wikipedia, StrategyWiki, Propuestas fanon.
- **Foros y comunidades**: Yahoo! 知恵袋, LiveJournal (death_note),
  foros en español (foroactivo, blogspot), Facebook (Star Con, Death Note
  Spanish), TikTok. Reddit: bloqueado.
- **Arte**: pixiv, ArtStation, DeviantArt, Wallpaper Abyss, WallpaperFlare.
- **Vídeo**: YouTube, TikTok, Bilibili (sólo títulos: no pude verlos).
- **Código y recursos**: GitHub, Sketchfab, ambientCG, Poly Haven,
  color-hex, ColorMagic.
- **Doblaje latino**: Doblaje Wiki (sólo extractos), The Dubbing
  Database, ANMTV, Animeol, TikToks y vídeos de los actores.
- **Prensa**: ComicBook.com, Screen Rant, SlashFilm, AniLoop, Peliplat,
  Anime News Network, Anime Corner, SciFi Japan, Hypebeast, GameSpot,
  What's on Netflix, CBR.

### Lo que NO encontré

- Imágenes descargadas y hojas de contacto.
- Una encuesta oficial de popularidad (parece que no existe).
- El orden completo de la encuesta de Nlab más allá del 4.º.
- Voces latinas de Rem, Watari, Matsuda y Mikami; la de Sōichirō, dudosa.
- Frases latinas con fuente, salvo «fritura».
- Qué regla sale en cada pausa del anime.
- La letra de las reglas del manga.
- Capturas de la interfaz de los juegos. The Cutting Room Floor: no lo
  busqué (no hay juegos de Death Note con betas documentadas que yo
  sepa ⚠️). Wayback Machine: bloqueada.
- Una hoja de modelo oficial del anime (Kitao).
