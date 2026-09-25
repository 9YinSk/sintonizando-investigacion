---
tags: [biblia, serie, laminas]
serie: "JoJo's Bizarre Adventure (ジョジョの奇妙な冒険)"
canal: "#memes"
fecha: 2026-09-24
---

# Biblia · JoJo's Bizarre Adventure — para #memes

> [!important] Cómo se hizo, y sus límites
> - **Dos tiempos, el mismo día (24-sep-2026)**. Al empezar, la red
>   estaba **cerrada**: sólo funcionaban la búsqueda web y GitHub. A
>   media tarea **se abrió** y rehíce con las fuentes de verdad.
> - **Con la red abierta** usé:
>   - `herramientas/investigar_serie.py` sobre la wiki `jojo` de Fandom
>     (13 páginas de personajes): **1.735 imágenes grandes**, 34 hojas
>     de contacto en `herramientas/referencias/jojo-s-bizarre-adventure/`
>     (las 3 últimas no se hicieron por tiempo; son las más pequeñas).
>     **Miré las hojas** y cito las imágenes por número (F-n).
>   - La **API de JoJo Wiki** (jojowiki.com): To Be Continued, Stand
>     Stats, JOJODAY, Music, personajes, y **282 + 324 imágenes** de sus
>     páginas (W-n, con tamaño real).
>   - La **API de Doblaje Wiki** para el reparto latino de cada parte,
>     cruzado con ANMTV, JoJo Wiki, Star Con y clips (§10).
>   - `yt-dlp` para buscar vídeos y leer sus datos (duración, fecha,
>     vistas). **YouTube pidió iniciar sesión** para los capítulos y
>     casi todos los subtítulos: los **minutos dentro de los vídeos de
>     YouTube no se pudieron medir**.
>   - API de **Sketchfab** (modelos CC), **Poly Haven** (texturas CC0),
>     **Pixiv** (búsqueda por etiquetas), **Arctic Shift** (Reddit; las
>     búsquedas grandes daban «timeout»), **Wayback Machine** (The
>     Cutting Room Floor), y el **portal oficial** (fondos de pantalla).
>   - **No respondieron**: TV Tropes y The Cutting Room Floor en directo
>     (reto de Cloudflare; no lo salté), Wallhaven (0 resultados),
>     Oricon y Anime News Network por WebFetch.
> - **Subtítulos japoneses con tiempos** de **todas las partes**
>   (PB, BT, SC, DU, GW, SO y el ep. 1 de SBR) del repositorio
>   [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv).
>   Con ellos doy **el minuto** de cada escena y la frase japonesa. La
>   traducción al español es mía, **no la del doblaje**.
> - Letras de [google/fonts](https://github.com/google/fonts),
>   comprobadas con fontTools (á é í ó ú ñ ¿ ¡, y también ゴ ド 無駄).
> - Colores: **medidos al píxel** en los originales (lo digo en cada
>   caso) o **a ojo** (⚠️).
> - **Cómo leo los episodios.** El anime no numera por temporadas, sino
>   por **partes**. Uso estas siglas y el número de episodio **dentro de
>   cada parte**:
>   - **PB** Phantom Blood (2012, eps. 1-9)
>   - **BT** Battle Tendency (2012-13; eps. 10-26 de la serie de 2012,
>     y los cito con ese número: «BT ep. 10» es el primero de BT)
>   - **SC** Stardust Crusaders (2014-15, eps. 1-48; del 25 al 48 es
>     «Egypt Arc»)
>   - **DU** Diamond is Unbreakable (2016, eps. 1-39)
>   - **GW** Golden Wind (2018-19, eps. 1-39)
>   - **SO** Stone Ocean (2021-22, eps. 1-38)
>   - **SBR** Steel Ball Run (Netflix, 19 mar. 2026; semanal desde el
>     25 sep. 2026)
> - El minuto es **el del archivo de subtítulos** que usé (lo nombro en
>   la bitácora). Puede moverse **uno o dos minutos** según la
>   plataforma (Netflix, Crunchyroll, Blu-ray o TV).
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su
>   minuto, o lo vi en la imagen original. ⚠️ **dudoso**: una sola
>   fuente, o de memoria. Lo de memoria siempre va marcado.

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección **✦ LA SALA ✦**):

> **ıı・😂・memes** (texto) · 1 fijados · 0 de personas en los últimos 15
> — _El meme, sin más. Si lo doblas, va a fandub-de-memes._

Del encargo: **«ya le gustó, se puede mejorar»**. O sea: ya hay una
lámina de JoJo en #memes que el dueño aprobó. Esta biblia sirve para
**subirle el nivel**, no para empezar de cero.

Los vecinos de ✦ LA SALA ✦ son #a-que-juegas, #comandos-y-sorteos y
#general. En #memes la gente **cuelga una imagen o un vídeo y ya**. Es
el canal más relajado del servidor.

> [!warning] Un aviso para el coordinador
> El canal **#fandub-de-memes no aparece** en `servidor/inventario.md`
> (lo busqué entero: no hay ningún canal con «fandub» en el nombre). La
> lámina lo nombra porque lo dice la descripción del canal. **Hay que
> comprobar** que ese canal exista antes de publicar, o cambiar el texto
> por el canal real donde van los doblajes (¿#demos? ¿#proyectos?).

### Los textos de la lámina (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Memes** | nombre del canal |
| 2 | **El meme, sin más** | para qué es: se cuelga y ya |
| 3 | **Si lo doblas, va a fandub-de-memes** | la única regla: el meme doblado se va a otro canal |
| 4 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

Son **pocos textos**. **No hace falta lámina 2**: todo cabe en una.
La gracia de JoJo es que la frase del personaje **puede ser, ella
misma, un meme de la serie** (ver §2 y §14).

Una idea para el texto 3, en la voz de la serie: Joseph **adivina «tu
siguiente frase»** (次のセリフは, BT ep. 10, 00:16:19 ✅). La lámina
puede decir: «**Tu siguiente frase será: “¿y si lo doblo?”. Pues va a
fandub-de-memes.**» Así la regla sale **de un meme de la propia serie**
(ver §19, concepto A).

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué JoJo encaja en #memes | Es **el anime que más memes ha dado de sí mismo**: la flecha **«To Be Continued»** con «Roundabout» (meme mundial desde 2016), «ZA WARUDO», «ROAD ROLLER DA», «¡fue este Dio!», «Nigerundayo», «yare yare daze», la pose JoJo… Cada uno tiene **su minuto** en §2 ✅. |
| El objeto del plan | **El fotograma congelado con la flecha** (W1-W12) y **la ficha de Stand** del anime, que existe de verdad (W16-W23: reloj de seis notas A-E, «[STAND MASTER]», «[STAND NAME]») ✅. Los dos están medidos en §3. |
| Un objeto nuevo y mejor | La **cámara instantánea** que Joseph rompe para hacer **fotos psíquicas** con su Stand (SC ep. 1, 00:19:31 ✅; F234). En #memes se cuelgan imágenes: la foto que sale **es el meme**. |
| El más querido | **Jotaro** es la cara; **Dio y Joseph** son los reyes de los memes; **Bucciarati y Rohan** los secundarios favoritos (los 10 de Araki: 1.º Josuke, 2.º Kira, 3.º Bucciarati ✅). En la encuesta oficial de episodios de 2025 ganó **la muerte de Caesar** (55 %) ✅. De moda hoy: **Gyro** (SBR, semanal desde el 25-sep-2026). |
| Quién habla en la lámina | **Joseph** (concepto A), **Rohan** con «…pero me niego» (B) o **Dio** en la apisonadora (C). §19. |
| Cuadro de diálogo propio | **No es un globo blanco**: la **flecha TBC** (relleno `#B4C0A8`, letra `#48483C`), la **ficha de Stand**, la **carta de tarot** con nombre en mincho, **ゴゴゴ** gigante, el **texto de narrador**, las **páginas de Heaven's Door** y el **globo de manga japonés** del opening. §7. |
| Letras | **Dela Gothic One** (ゴゴゴ), **Shippori Mincho B1** (nombres en japonés), **EB Garamond / Cinzel** ([STAND NAME]), **Caveat Brush / Mali Bold** (flecha en español), **Anton / Bungee** (títulos). Todas con tildes, ñ, ¿ y ¡, comprobado. |
| Voz latina | Jotaro y Rohan **Irwin Daayán** ✅, Dio **Marc Winslow** ✅, Joseph **Miguel de León** (joven) y **Raúl Anaya** (viejo) ✅, Josuke **Luis Fernando Orozco** ✅, Giorno **José Luis Piedra** ✅, Bucciarati **Luis Leonardo Suárez** ✅, Kira **José Gilberto Vilchis** ✅, Jolyne **Alondra Hidalgo** ✅, Johnny **Max Durán** y Gyro **Xalisco Moreno** ✅. Iyuno • SDI México (dir. **Roberto Molina**); SBR en New Art (dir. Marc Winslow). «Yare yare daze» = **«Ay, por favor»** ✅. §10. |
| Tono | Pop y teatral: **colores que cambian por escena**, sombras duras, poses de modelo. Nada de sepia plano ni de colores pastel. |
| Aviso | El canal **#fandub-de-memes no está en el inventario**: comprobar que existe (§0). |

## 2 · Las escenas que sirven para #memes (con minuto)

JoJo es, probablemente, **el anime con más memes nacidos de la propia
serie**. Casi cada frase famosa es ya una plantilla de meme. Todas las
de abajo salen de los **subtítulos japoneses** de
[kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv):
el texto y el minuto están **comprobados** ✅. La traducción al español
es mía. Lo que **se ve** en cada una (postura, luz) lo describo de
memoria ⚠️: mira el fotograma antes de usarlo.

### 2.1 Los memes que nacen de una escena (el top)

| Meme | Escena | Minuto | Frase japonesa (subtítulo) | Qué dice |
|---|---|---|---|---|
| **«Yare yare daze»** | SC ep. 2 (la primera de Jotaro) | 00:02:19 | やれやれだぜ | «Qué fastidio» / en el doblaje latino, «**Ay, por favor**» ⚠️ (§10) |
| **«¡Soy yo, Dio!»** («Kono Dio da») | PB ep. 1 | 00:15:45 a 00:15:53 | 初めての相手は ジョジョではない / このディオだ！ | Dio le roba el primer beso a Erina: «Tu primera vez no fue JoJo… **¡fue este Dio!**» |
| **«¡Dejo de ser humano, JoJo!»** | PB ep. 2 | 00:23:33 | 俺は人間をやめるぞ ジョジョ！ | Dio se pone la máscara de piedra (se repite en PB ep. 3, 00:05:34) |
| **«¿Recuerdas cuántos panes te has comido?»** | PB ep. 5 | 00:07:33 | お前は 今まで食った パンの枚数を覚えているのか？ | Dio, cuando le preguntan a cuánta gente ha matado |
| **«Speedwagon se retira con estilo»** | PB ep. 4 | 00:03:41 | スピードワゴンは クールに去るぜ | Speedwagon se va solo, sin despedirse |
| **«Débil, débil»** | PB ep. 3 | 00:15:04 | 貧弱 貧弱うーっ！ | La burla de Dio |
| **«Tu siguiente frase será…»** | BT ep. 10 (el primero de Battle Tendency) | 00:16:19 a 00:16:26 | 次のセリフは― “分かったから どうだってんだよ このクソガキが”だ | Joseph **adivina** lo que va a decir el otro… y el otro lo dice palabra por palabra |
| (la misma) | BT ep. 22 | 00:18:27 | ワムウ そこで おめえの次のセリフはこうだ | Contra Wamuu: vuelve a acertar |
| **«¡Nigerundayo!»** («¡Hay que huir!») | BT ep. 11 | 00:08:44 | 逃げるんだよ スモーキー | La «estrategia secreta» de Joseph es **salir corriendo** |
| (la misma, gritada) | BT ep. 25 | 00:08:16 | 逃げるんだよーっ！ | |
| **«¡Oh, no!»** de Joseph | BT ep. 15 | 00:05:55 | オー ノー！ | |
| **«¡Qué injusticia!»** (el llanto de Esidisi) | BT ep. 16 | 00:25:05 | あんまりだああ～ | El villano **llora a gritos** para calmarse |
| **«Y Kars dejó de pensar»** | BT ep. 26 (el último de BT) | 00:14:40 | そのうちカーズは 考えるのをやめた | Kars, flotando en el espacio para siempre |
| **«Rero rero»** (Kakyoin y la cereza) | SC ep. 9 | 00:07:03 | レロレロレロレロ… | Kakyoin **da vueltas a una cereza con la lengua** |
| **La foto psíquica** (念写) de Joseph | SC ep. 1 | 00:19:31 a 00:20:07 | 能力は 遠い地のヴィジョンを フィルムに写す 念写！ … いちいち ３万円もするカメラを ぶっ壊さなくちゃあならんがな！ | Joseph **rompe una cámara de 30.000 yenes** para sacar una foto con su Stand (base del concepto A, §19) |
| **«Mejor el n.º 2 que el n.º 1»** | SC ep. 11 | 00:19:00 | １番より ナンバー２！ | El lema de Hol Horse |
| **«¡Oh, my god!»** de Joseph | SC ep. 27 | 00:16:17 | オー マイ ゴッド！ | Viejo, con sombrero, manos a la cabeza ⚠️ |
| **«¿Serán los dos puños? ¿Será ora ora?»** / «YES YES YES» / «OH MY GOD» | SC ep. 42 | 00:10:21 a 00:10:58 | 右の拳で殴るか 左の拳で殴るか… もしかして オラオラですか～!? / ＹＥＳ！ ＹＥＳ！ ＹＥＳ！ / OH MY GOD！ | Jotaro deja **elegir a Terence** con qué puño le pega. Terence: «¿Será… ora ora?». Jotaro: «**YES YES YES**». Terence: «**OH MY GOD**». Y la ráfaga. |
| **«Voy a contar lo que acaba de pasar…»** (Polnareff) | SC ep. 45 | 00:06:42 a 00:06:58 | ありのまま 今 起こったことを 話すぜ！ 俺は やつの前で 階段を上っていたと思ったら いつの間にか 下りていた | «Subía la escalera y, sin saber cómo, **la estaba bajando**. No sé qué me hizo». Plantilla de meme para «no entiendo qué pasó» |
| **«¿Oh? ¿Te acercas a mí?»** | SC ep. 46 | 00:19:59 a 00:20:23 | ほう… 向かってくるのか｡ … 近づかなきゃ てめえを ぶちのめせないんでな｡ | Dio y Jotaro **caminan el uno hacia el otro**. Jotaro: «Si no me acerco, no te puedo partir la cara» |
| **«¡ZA WARUDO! ¡Tiempo, detente!»** | SC ep. 46 | 00:23:37 | ｢世界｣ 時よ止まれ！ | Primera vez que Dio **para el tiempo** en pantalla (se repite en SC ep. 47, 00:00:44, y ep. 48, 00:05:09) |
| **«¡Me siento en lo más ALTO!»** | SC ep. 47 | 00:23:34 | 最高に ハイってやつだぁぁぁぁ！ | Dio tras beber la sangre de Joseph |
| **«¡ROAD ROLLER DA!»** («¡Es una apisonadora!») | SC ep. 48 | 00:08:36 | ロードローラーだ～！ | Dio **cae del cielo con una apisonadora** encima de Jotaro |
| **«Jotaro dejó de pensar»** | SC ep. 48 | 00:07:57 | 承太郎は 考えるのをやめた｡ | Eco de Kars |
| **«Me hiciste enojar»** | SC ep. 48 | 00:14:47 a 00:14:56 | てめえの敗因は たった一つだぜ… たった一つの シンプルな答えだ｡ てめえは 俺を 怒らせた｡ | El remate de Jotaro a Dio |
| **«¿Qué dijiste de mi pelo?»** | DU ep. 1 | 00:06:02 a 00:06:14 | このヘアースタイルがサザエさんみてェーだとォ | Josuke se transforma si alguien se burla de su **tupé** (nadie había dicho nada) |
| **«¡Great!»** de Josuke | DU ep. 2 | 00:17:09 | グレートですよ こいつはァ | La muletilla de Josuke |
| **«Me llamo Yoshikage Kira. Tengo 33 años…»** | DU ep. 21 | 00:20:25 a 00:21:27 | わたしの名は「吉良吉影」 年齢33歳 … 私は常に「心の平穏」を願って生きてる人間 | El **monólogo de Kira** (casa, trabajo, leche caliente, ocho horas de sueño). Es un *copypasta* famoso |
| **«Killer Queen»** | DU ep. 21 | 00:22:09 | 「キラークイーン」…と わたしはこいつを名付けて呼んでいる | |
| **«…pero me niego»** («Daga kotowaru») | DU ep. 28 | 00:20:15 a 00:20:22 | 呼べよ 早く呼べ / だが断る / この岸辺露伴が最も好きなことの一つは | Rohan dice que no **justo cuando le ofrecen salvarse**. «Una de las cosas que más me gustan es decirle que no a quien se cree que tiene razón» |
| **«Bites the Dust»** | DU ep. 35 | 00:16:49 | 「キラー・クイーン」第三の爆弾「バイツァ・ダスト」 | La tercera bomba de Kira |
| **«Star Platinum: The World»** | DU ep. 23 | 00:10:36 | やれやれだぜ 「スタープラチナ ザ·ワールド」 | Jotaro adulto, con su «yare yare» |
| **«Este es el sabor de un mentiroso»** | GW ep. 1 | 00:21:23 | この味は うそをついてる味だぜ ジョルノ・ジョバァーナ | Bucciarati **lame el sudor** de la cara de Giorno (se repite en GW ep. 2, 00:08:25) |
| **«Yo, Giorno Giovanna, tengo un sueño»** | GW ep. 5 | 00:22:49 | このジョルノ・ジョバァーナには夢がある | Con la música **«Il vento d'oro»** detrás (ver §11). Antes en GW ep. 4, 00:08:31: «…un sueño que creo justo» |
| **«Di molto bene»** | GW ep. 17 | 00:09:27 | ディ・モールト 非常にいいぞ | Melone y su Stand |
| **«Arrivederci»** | GW ep. 16 | 00:19:43 a 00:19:53 | アリアリアリ… / アリーヴェデルチ | La ráfaga de Bucciarati y su despedida |
| **«Nunca llegarás a la verdad»** | GW ep. 37 | 00:20:46 | しかし 実際に起こる真実に到達することは決してない | Gold Experience Requiem: Diavolo **muere una y otra vez** |
| **«Cuenta números primos»** | SO ep. 12 | 00:12:31 a 00:12:40 | 落ち着くんだ 素数を数えて落ち着くんだ / 素数は １と自分の数でしか 割ることのできない孤独な数字 | Pucci se calma **contando primos**. Se repite en SO ep. 22 (00:04:44) y ep. 35 (00:18:41) |
| **«Yare yare dawa»** | SO ep. 2 | 00:20:59 | やれやれだわ グェス | La versión **femenina** de Jolyne |
| **«Nyoho»** | SBR ep. 1 | 00:05:24 | ニョホ… ホ | La risa de Gyro (se repite en 00:22:05 y 00:26:25) |

### 2.2 El «To Be Continued» (el meme más usado fuera del fandom)

- **Qué es.** Al final de cada episodio de 2012, la imagen **se congela**,
  suena **«Roundabout»** de Yes y entra desde la derecha una **flecha
  que apunta a la izquierda** con «To Be Continued» escrito a mano ✅
  ([Gizmodo](https://gizmodo.com/to-be-continued-is-the-sleeper-meme-hit-of-the-summer-1781860391),
  [Teh Meme Wiki](https://meme.fandom.com/wiki/To_Be_Continued),
  [Cultural History of the Internet](https://internet.medialities.org/2020/11/16/roundabout/)).
- **Cómo se hizo meme.** Primer uso conocido: un vídeo de **Niconico en
  2012** que parodiaba *Madoka Magica*. El gran salto fue en **2016**, en
  Vine: un Calamardo bailando, cortado por la flecha. Desde entonces se
  pone **justo antes de un golpe, una caída o un choque** ✅ (las mismas
  fuentes).
- **Cómo se ve en el meme** (medido por mí en la herramienta de fans
  [JoJoTBCfier](https://github.com/MrPakoras/JoJoTBCfier), no en el
  anime):
  - El último fotograma se pasa a **sepia**: sombras `#1E1A12`, luces
    `#BFB196`.
  - La flecha ocupa **el 40 % del ancho**, a un **5 % del borde
    izquierdo** y al **70 % de la altura**. Entra deslizándose en 0,3 s.
  - Colores de su flecha: relleno **`#D6D3C5`** y texto y borde
    **`#7F7D71`** (gris cálido).
- **Cómo se ve en el anime** ✅ (medido por la guía de cuadros de
  diálogo de `_ya_hechas` y **otra vez por mí** en W1, W3 y W8, §3.3):
  relleno **verde salvia pálido `#B4C3AD` / `#B4C0A8`**, texto a mano
  **verde oliva oscuro `#5A5F4E` / `#48483C`**, contorno fino y **tres
  barras inclinadas en la cola**.
- **Primera flecha en el manga**: capítulo **167** (Stardust Crusaders)
  ✅ ([JoJo Wiki](https://jojowiki.com/To_Be_Continued), leído por su API; W13).
- En el anime, **el color del fotograma congelado cambia** según la
  parte y el episodio ✅ (lo vi en W1-W12, §3.3): gris violeta o blanco y
  negro en PB, sepia o rojo-violeta en SC, magenta en DU, verde agua en
  GW y SO, sepia verdoso en SBR.
- **Ojo**: el filtro del anime **no es un sepia plano**. Es un
  virado de color con el grano del fotograma. Si se hace sepia plano
  queda «de plantilla de meme», no «de la serie» ⚠️.

### 2.3 Los gritos de ráfaga (el sonido de JoJo)

| Stand / personaje | Grito | Dónde lo comprobé |
|---|---|---|
| Star Platinum (Jotaro, y Stone Free de Jolyne) | **ORA ORA ORA** (オラオラ) | SC ep. 42, 00:10:52 ✅ |
| Dio (y The World) | **MUDA MUDA** (無駄/ムダ, «inútil») | PB ep. 3, 00:17:54; PB ep. 8, 00:18:26 ✅. En SC el grito no va subtitulado |
| Giorno | **MUDA MUDA** también (es hijo de Dio) | GW ep. 2, 00:09:37 («無駄ぁ») ✅ |
| Crazy Diamond (Josuke) | **DORA DORA** (ドラララ) | DU ep. 29, 00:02:13 ✅ |
| Sticky Fingers (Bucciarati) | **ARI ARI** (アリアリ) | GW ep. 16, 00:19:43 ✅ |
| Echoes Act 3 (Koichi) | habla en mayúsculas: **«S・H・I・T»** | DU ep. 24, 00:07:07 ✅ |

---

## 3 · Arte oficial y referencias visuales

### 3.0 Cómo citar las imágenes de esta biblia

- **F-n** = imagen número *n* del índice de la wiki de Fandom
  (`jojo.fandom.com`), sacado con `herramientas/investigar_serie.py`.
  Son **1.735 imágenes grandes** en 37 hojas, en
  `herramientas/referencias/jojo-s-bizarre-adventure/` (con
  `indice.json`: archivo, tamaño y URL del original). Para bajar el
  original: `python herramientas/investigar_serie.py --bajar jojo-s-bizarre-adventure 190 278`.
- **W-n** = imagen de **JoJo Wiki** (jojowiki.com), numerada en mi
  hoja `hojas/hoja_1_tbc_y_fichas_stand.jpg`. La URL de cada una está
  en `referencias.json` y en esta biblia.
- Tres hojas copiadas a `biblias/28-jojo-s-bizarre-adventure/hojas/`:
  1. `hoja_1_tbc_y_fichas_stand.jpg` → **W1-W25**: los fotogramas
     «To Be Continued» de cada parte y las **fichas de Stand** del anime.
  2. `hoja_2_objetos_rohan_joseph.jpg` → objetos (Polaroid, cartas de
     tarot, apisonadora, fotos) y Rohan y Joseph (números F).
  3. `hoja_3_poses.jpg` → poses de Giorno, Bucciarati, Josuke, Dio,
     Jotaro y Jolyne (números F).
- **Tamaños comprobados** con la API de cada wiki (ancho × alto reales).

### 3.1 La ficha de Stand del anime (el objeto del plan) ✅

Desde Diamond is Unbreakable, el anime **corta a media escena con una
ficha** que presenta al Stand. Es la «ficha de Stand» oficial, y es el
mejor «cuadro de texto» que tiene la serie.

| # | Qué es | Tamaño | Enlace (original) |
|---|---|---|---|
| W16 | Crazy Diamond (Josuke), DU | 1920×1080 | [PNG](https://static.jojowiki.com/images/d/dd/latest/20191015214849/Crazy_Diamond_stats.png) |
| W17 | Killer Queen (Kira), DU | 1920×1080 | [PNG](https://static.jojowiki.com/images/6/6b/latest/20211112213632/Killer_Queen_Stats.png) |
| W18 | Gold Experience (Giorno), GW | 1920×1080 | [PNG](https://static.jojowiki.com/images/d/d5/latest/20211112210524/Gold_Experience_Stats.png) |
| W19 | Star Platinum (Jotaro), DU | 1920×1080 | [PNG](https://static.jojowiki.com/images/0/00/latest/20210602000733/Star_Platinum_%28Part_4%29_stats.png) |
| W20 | Stone Free (Jolyne), SO | 1920×1080 | [PNG](https://static.jojowiki.com/images/2/2f/latest/20211201172401/Stone_Free_stats.png) |
| W21 | Heaven's Door (Rohan), DU | 1920×1080 | [PNG](https://static.jojowiki.com/images/0/04/latest/20191015213752/Heaven%27s_Door_stats.png) |
| W22 | «Visual Book Stand File» de Crazy Diamond (libro oficial) | 2378×1800 | [PNG](https://static.jojowiki.com/images/c/cc/latest/20220128024940/Crazy_D_Visual_Book_Stand_File.png) |
| W23 | Star Platinum, «eyecatch» del ep. 36 de SO | 1920×1080 | [PNG](https://static.jojowiki.com/images/4/41/latest/20221201120548/Star_Platinum_Eyecatch_Ep_36.png) |

**Cómo está hecha** (medido por mí en W16 y W17, a tamaño real) ✅:

- **A la izquierda o derecha**, un **reloj de dos anillos blancos
  finos** con marcas como un bisel. Dentro, **seis etiquetas en
  japonés** en letra de palo blanca, que siguen la curva:
  破壊力 (arriba), スピード (arriba a la derecha), 射程距離 (abajo a la
  derecha), 持続力 (abajo), 精密動作性 (abajo a la izquierda), 成長性
  (arriba a la izquierda). El orden es **siempre ese, en el sentido del
  reloj** ✅ (también en la ficha del plugin libre
  [astrbot_plugin_jojo_stand_panel](https://github.com/Dogend233/astrbot_plugin_jojo_stand_panel)).
- Junto a cada etiqueta, **la nota en una letra enorme** (A, B, C, D o
  E) en blanco.
- En el círculo de dentro, seis ejes con rayitas y la escala **A B C D
  E** escrita sobre el eje de arriba (la A es la de fuera).
- El **polígono relleno** es **translúcido y del color del Stand**
  (magenta en Crazy Diamond y Killer Queen).
- Arriba y abajo, dos rótulos: **「[STAND MASTER]」** y
  **「[STAND NAME]」**, en **mayúsculas con serifa** (tipo Times), blancas
  con un bisel oscuro. Debajo, el nombre en **japonés, mincho grueso
  blanco** (東方仗助, クレイジー・ダイヤモンド).
- Detrás, **la silueta negra del usuario** y **el Stand a todo color**.
- El fondo lleva **la trama de cada parte**: rayado violeta en DU, fondo
  negro con **manchas rojas como sangre** en Killer Queen (W17), damero
  rosa y dorado en Gold Experience (W18), azul en Stone Free (W20).

**Las notas de los Stands de esta biblia** (JoJo Wiki, «Stand Stats»,
que cita los libros oficiales) ✅. Orden: Poder · Velocidad · Alcance ·
Aguante · Precisión · Potencial.

| Stand | Usuario | Notas |
|---|---|---|
| Star Platinum | Jotaro | A · A · C · A · A · A |
| The World | Dio | A · A · C · A · B · B |
| Hermit Purple | Joseph | D · C · D · A · D · E |
| Crazy Diamond | Josuke | A · A · D · B · B · C |
| Heaven's Door | Rohan | D · B · B · B · C · A |
| Killer Queen | Kira | A · B · D · B · B · A |
| Gold Experience | Giorno | C · A · C · D · C · A |
| Sticky Fingers | Bucciarati | A · A · C · D · C · D |
| Stone Free | Jolyne | A · B · C · A · C · A |
| Gold Experience Requiem | Giorno | ∅ en todo (no se puede medir) |

- **De dónde salen** las fichas en papel: en las **partes 5 y 6** van en
  las páginas entre capítulos de los tomos; las demás, en los libros de
  datos (JOJO A-GO!GO!, JOJOVELLER) ✅
  ([Wikipedia japonesa: スタンド](https://ja.wikipedia.org/wiki/%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%89_(%E3%82%B8%E3%83%A7%E3%82%B8%E3%83%A7%E3%81%AE%E5%A5%87%E5%A6%99%E3%81%AA%E5%86%92%E9%99%BA)),
  [JoJo Wiki: Stand Stats](https://jojowiki.com/Stand_Stats)).
- **Qué mide cada nota** ✅ (las mismas fuentes): *Poder destructivo*
  (cuánto rompe), *Velocidad*, *Alcance* (hasta dónde llega lejos del
  usuario), *Aguante* (cuánto dura), *Precisión* (qué tan fino trabaja)
  y *Potencial* (cuánto puede crecer; baja cuando el usuario ya lo
  domina).
- **Herramienta libre** para dibujar la gráfica con las medidas justas:
  [valkyrs/jojo-stands](https://github.com/valkyrs/jojo-stands),
  JavaScript con licencia **MIT** (2018). Sirve para sacar el polígono
  exacto y calcarlo en Photoshop.

### 3.2 La cartela del Stand en Stardust Crusaders (tarot) ✅

En SC no hay gráfica. Cuando sale un Stand nuevo, el anime pone **al
personaje con su carta de tarot** y los nombres en japonés.

| # | Qué es | Tamaño |
|---|---|---|
| F190 | Jotaro, Star Platinum y la carta **THE STAR**; rótulos 空条承太郎 / 星の白金 (スタープラチナ) | 1920×1080 |
| F278 | Joseph y la carta **THE HERMIT**; rótulos ジョセフ・ジョースター / 隠者の紫 (ハーミットパープル) | 1920×1080 |
| F258 | La carta **THE WORLD 21** brillando sobre humo violeta | 1920×1080 |
| F148 | La carta **17 · THE STAR** sola, de frente (arte oficial) | 1279×1920 |

- Cada Stand de SC se llama como **un arcano del tarot** (Star Platinum
  es La Estrella, The World es El Mundo) ✅ (JoJo Wiki, «Stand Stats»,
  tabla de SC; F190 y F258).
- La carta es **un objeto real**: cartón, bordes redondeados, marco
  azul noche con estrellas doradas (F148). **Se puede modelar en
  Blender** (hay una carta libre de base, §4).

### 3.3 El «To Be Continued» en cada parte (fotogramas de JoJo Wiki) ✅

Todos a **1920×1080**, de la página
[To Be Continued](https://jojowiki.com/To_Be_Continued). Colores
medidos por mí (margen ±12 por canal). Enlaces directos: [W1](https://static.jojowiki.com/images/e/e9/latest/20220614115334/E1-TBC.png),
[W3](https://static.jojowiki.com/images/6/6f/latest/20230324222102/E16-TBC.png),
[W5](https://static.jojowiki.com/images/2/22/latest/20220512145717/SC-E1-TBC.png),
[W8](https://static.jojowiki.com/images/8/8d/latest/20230324235144/DU-E1-TBC.png),
[W10](https://static.jojowiki.com/images/6/6e/latest/20240120091049/GW-E1-TBC.png),
[W12](https://static.jojowiki.com/images/9/94/latest/20260902150718/SBR_Episode_1_TBC.png)
(el resto de W1-W25, con su URL, en §3.6).

| # | Episodio | Filtro del fotograma | Nota |
|---|---|---|---|
| W1 | PB ep. 1 | gris violeta casi negro (`#241824`, `#181818`) | la **máscara de piedra** sobre papel pintado |
| W2 | PB ep. 9 | blanco y negro puro | |
| W3 | BT ep. 16 (serie ep. 16) | **sin imagen**: la flecha sola, grande, sobre **rojo carmesí `#600000`** | el único así ✅ (JoJo Wiki) |
| W4 | BT ep. 17 | sepia con **texto de narrador**: 「心臓に残った指輪溶解まで ―あと6日」 | el único con texto ✅ |
| W5 | SC ep. 1 | sepia oscuro (`#180C0C`, `#3C3024`) | Jotaro en la celda |
| W6 | SC ep. 42 | azul grisáceo | la cara de Terence |
| W7 | SC ep. 47 | rojo y violeta | Jotaro en El Cairo |
| W8 | DU ep. 1 | **magenta y violeta** en dos tonos | Angelo |
| W9 | DU ep. 19 | color casi normal, apagado | Okuyasu, Josuke y la rata |
| W10 | GW ep. 1 | **verde agua y rosa** (`#D8F0E4`, `#6C3048`) | Bucciarati |
| W11 | SO ep. 1 | verde agua y azul noche | Jolyne camino de la cárcel |
| W12 | SBR ep. 1 | **sepia verdoso y amarillo** (`#CCCC84`, `#B49078`) | Gyro a caballo |

- **La flecha del anime**, medida en W1, W3 y W8: relleno
  **`#B4C0A8`** (verde salvia pálido), letras y contorno **`#48483C` a
  `#606054`** (verde oliva oscuro), tres barras en la cola ✅ (coincide
  con la guía de `_ya_hechas`, que midió `#B4C3AD` y `#5A5F4E`).
- **Siempre abajo a la izquierda**, apuntando a la izquierda ✅ (W1-W12).
- **En el manga**: W13 (cap. 167, la primera) y W14 (cap. 226). En los
  juegos: W15 (*Last Survivor*, «再起不能»), W24 (*GioGio*, PS2) y W25
  (*Heritage for the Future*, flecha **naranja** con «To Be
  Continued...») ✅.
- **Episodios sin flecha**: SC 48, DU 39, GW 28, GW 39 y SO 38 ✅
  ([JoJo Wiki](https://jojowiki.com/To_Be_Continued)).
- **Rarezas útiles para un meme** ✅ (misma fuente):
  - En **DU ep. 19** el narrador **dice en voz alta** «To be continued!».
  - **DU ep. 28** tiene **dos flechas** (una a mitad de episodio).
  - **DU ep. 13** sigue animado tras la flecha (sin congelar ni filtro).
- **Por qué «Roundabout»**: el productor **Hiroyuki Omori** dijo que era
  de las canciones que **Araki** asoció con JoJo; primero la pensó para
  el opening y la pasó al final para que el público **quisiera volver
  la semana siguiente** ✅ (JoJo Wiki, citando la *Stand Up Guide* de
  2014). El director de sonido **Yoshikazu Iwanami** pidió un ending que
  pudiera **empezar desde cualquier momento** del episodio: por eso la
  canción arranca antes de la flecha ✅
  ([Portal oficial, notas de producción](https://jojo-portal.com/special/production-note/04/);
  [Anime! Anime!, entrevista a Tsuda](https://animeanime.jp/article/2013/05/14/14037.html)).

### 3.4 Ilustraciones y key visuals oficiales

| # / enlace | Qué es | Tamaño | Para qué |
|---|---|---|---|
| F2 · F3 · F4 · F5 | Renders oficiales de **All Star Battle**: Jolyne, Rohan, Jonathan, Jotaro, de cuerpo entero en **pose JoJo** sobre blanco | 4133×5500 · 4000×5318 · 4000×5307 · 3750×5000 | **Recorte limpio** para la lámina (fondo blanco) |
| F6 · F7 | **Cartones de cuenta atrás** del final de GW: Giorno con GER («最終話まであと1日») y Bucciarati con Sticky Fingers («あと2日») | 4677×3307 | Pose de presentación; letras a mano de colores |
| F183 | Cuenta atrás del final de DU: **Jotaro y Koichi**, «最終話まで あと23日» | 1920×1080 | Jotaro de blanco, con libro |
| F10-F12 | **Hojas de modelo** de Jotaro (David Production): gestos y cuerpo entero | 3400×2500 | Proporciones y ropa |
| F13-F15 | Hojas de modelo de la «sombra de DIO» (SC) | 3400×2500 | |
| F16-F28 | Hojas de modelo de Dio (PB) | 3400×2500 | |
| F29-F34 | Hojas de modelo de **Joseph viejo** (con la **mano de metal**) | 3400×2500 | |
| F45-F47 | Hojas de modelo de **Star Platinum** | 3400×2500 | |
| F50 | Hoja de colores de **Kira** | 3700×1800 | Traje y colores |
| F49 · F52 · F53 | Tres **murales de Araki** («Canvas») con los JoJo | 3000×2261 aprox. | Estilo y paleta de Araki |
| F67 · F68 · F69 · F117 | Portadas de **JoJonium** (reedición de lujo) | 2400×1748 | Marco verde y rojo de las portadas |
| F71 · F72 | Portada del libro **JOJOmenon** (Jotaro, amarillo y naranja) | 1706×2200 | |
| F138 · F142 | Jotaro y Star Platinum (arte de Araki y promo) | 1920×1401 · 1920×1352 | |
| F173 · F302 | Jotaro y Josuke en el OP «Crazy Noisy Bizarre Town»: **fondos pop con estrellas** | 1920×1080 | Paleta pop de DU |
| F431 · F435 | Giorno y Jolyne **como páginas de manga** en el **opening de 2012** («JoJo ~Sono Chi no Sadame~», que al final enseña a los JoJo del futuro); rótulo «あたしは空条徐倫ッ» | 1920×1080 | Pose + rótulo |
| [PV 10.º aniversario](https://www.youtube.com/watch?v=NIPpt48JIeA) | Vídeo oficial de Warner Bros. Japan (4 abr. 2022, 62 s, 2,08 millones de vistas) | — | Todos los JoJo juntos |
| [Proyecto 10.º aniversario](https://jojo-portal.com/special/jojoanime10th/) | **Key visual con todos los JoJo** (4 abr. 2022) y visual de la exposición (1 jul. 2022) ✅ ([Famitsu](https://www.famitsu.com/news/202207/01267053.html), [Natalie](https://natalie.mu/comic/news/472623), [Mantan](https://mantan-web.jp/article/20220701dog00m200013000c.html)) | ⚠️ no medido | Grupo de JoJo |
| [THE★JOJO WORLD](https://prtimes.jp/main/html/rd/p/000000007.000159118.html) | Tienda oficial (abrió el 24 jul. 2025) con **ilustración nueva de Araki** de 9 personajes ✅ (PR Times y JoJo Wiki, JOJODAY) | ⚠️ no medido | |
| [Key visual de SBR](https://www.anitrendz.com/news/2025/12/08/key-visual-for-steel-ball-run-jojos-bizarre-adventure-revealed) | Johnny y Gyro, dibujados por **Daisuke Tsumagari** (diseñador de personajes) ✅ ([AniTrendz](https://www.anitrendz.com/news/2025/12/08/key-visual-for-steel-ball-run-jojos-bizarre-adventure-revealed), [Anime Corner](https://animecorner.me/jojos-bizarre-adventure-steel-ball-run-part-7-anime-reveals-main-staff-david-production-returns/)) | ⚠️ no medido | Lo más reciente |

### 3.5 Los objetos que ya salen en la serie (y sirven de soporte) ✅

Los vi en las hojas (F = Fandom):

| # | Objeto | Escena |
|---|---|---|
| F234 | **Cámara instantánea (Polaroid)** golpeada por las zarzas violetas de Hermit Purple | DIO la usa en SC; Joseph hace lo mismo (念写, «foto psíquica») |
| F216 | Jotaro sostiene **una foto instantánea** al final de SC (ep. 48) | la foto del grupo |
| F1160 | La **foto del grupo de SC en un marco**, sobre el escritorio de Jotaro (GW) | 1280×720 |
| F250 | **La foto de DIO** que Giorno guarda en su cartera (GW) | |
| F499 | Kira con la **foto de su padre** en la pared (DU) | |
| F241 · F715 | Dio **encima de la apisonadora** («Road roller da!») | SC ep. 48 |
| F476 · F492 · F494 | **Heaven's Door**: la cara de Koichi **se abre en páginas con texto**; Rohan las lee y las arranca | DU |
| F450 | Rohan herido **dibujando** en su mesa | DU |

### 3.6 Lista completa de W1-W25 (hoja 1), con su original

| # | Archivo | Tamaño | Enlace |
|---|---|---|---|
| W1 | E1-TBC.png | 1920×1080 | [original](https://static.jojowiki.com/images/e/e9/latest/20220614115334/E1-TBC.png) |
| W2 | E9-TBC.png | 1920×1080 | [original](https://static.jojowiki.com/images/3/33/latest/20220730013043/E9-TBC.png) |
| W3 | E16-TBC.png | 1920×1080 | [original](https://static.jojowiki.com/images/6/6f/latest/20230324222102/E16-TBC.png) |
| W4 | E17-TBC.png | 1920×1080 | [original](https://static.jojowiki.com/images/e/e4/latest/20220606081719/E17-TBC.png) |
| W5 | SC-E1-TBC.png | 1920×1080 | [original](https://static.jojowiki.com/images/2/22/latest/20220512145717/SC-E1-TBC.png) |
| W6 | SC-E42-TBC.png | 1920×1080 | [original](https://static.jojowiki.com/images/7/71/latest/20230324225812/SC-E42-TBC.png) |
| W7 | SC-E47-TBC.png | 1920×1080 | [original](https://static.jojowiki.com/images/9/96/latest/20230324225826/SC-E47-TBC.png) |
| W8 | DU-E1-TBC.png | 1920×1080 | [original](https://static.jojowiki.com/images/8/8d/latest/20230324235144/DU-E1-TBC.png) |
| W9 | DU-E19-TBC.png | 1920×1080 | [original](https://static.jojowiki.com/images/f/f9/latest/20230324235230/DU-E19-TBC.png) |
| W10 | GW-E1-TBC.png | 1920×1080 | [original](https://static.jojowiki.com/images/6/6e/latest/20240120091049/GW-E1-TBC.png) |
| W11 | SO-E1-TBC.png | 1920×1080 | [original](https://static.jojowiki.com/images/5/52/latest/20260903170810/SO-E1-TBC.png) |
| W12 | SBR Episode 1 TBC.png | 1920×1080 | [original](https://static.jojowiki.com/images/9/94/latest/20260902150718/SBR_Episode_1_TBC.png) |
| W13 | TBC Chapter 167.png | 733×215 | [original](https://static.jojowiki.com/images/d/d6/latest/20240706011243/TBC_Chapter_167.png) |
| W14 | TBC Chapter 226.png | 729×296 | [original](https://static.jojowiki.com/images/e/e8/latest/20240706011242/TBC_Chapter_226.png) |
| W15 | Last Survivor to be continued.png | 1920×1080 | [original](https://static.jojowiki.com/images/9/96/latest/20240727130547/Last_Survivor_to_be_continued.png) |
| W16 | Crazy Diamond stats.png | 1920×1080 | [original](https://static.jojowiki.com/images/d/dd/latest/20191015214849/Crazy_Diamond_stats.png) |
| W17 | Killer Queen Stats.png | 1920×1080 | [original](https://static.jojowiki.com/images/6/6b/latest/20211112213632/Killer_Queen_Stats.png) |
| W18 | Gold Experience Stats.png | 1920×1080 | [original](https://static.jojowiki.com/images/d/d5/latest/20211112210524/Gold_Experience_Stats.png) |
| W19 | Star Platinum (Part 4) stats.png | 1920×1080 | [original](https://static.jojowiki.com/images/0/00/latest/20210602000733/Star_Platinum_%28Part_4%29_stats.png) |
| W20 | Stone Free stats.png | 1920×1080 | [original](https://static.jojowiki.com/images/2/2f/latest/20211201172401/Stone_Free_stats.png) |
| W21 | Heaven's Door stats.png | 1920×1080 | [original](https://static.jojowiki.com/images/0/04/latest/20191015213752/Heaven%27s_Door_stats.png) |
| W22 | Crazy D Visual Book Stand File.png | 2378×1800 | [original](https://static.jojowiki.com/images/c/cc/latest/20220128024940/Crazy_D_Visual_Book_Stand_File.png) |
| W23 | Star Platinum Eyecatch Ep 36.png | 1920×1080 | [original](https://static.jojowiki.com/images/4/41/latest/20221201120548/Star_Platinum_Eyecatch_Ep_36.png) |
| W24 | GioGio 5-1 to be continued.png | 640×480 | [original](https://static.jojowiki.com/images/5/58/latest/20240622160733/GioGio_5-1_to_be_continued.png) |
| W25 | HFTF Location Test JPN 2.png | 1440×1080 | [original](https://static.jojowiki.com/images/c/cc/latest/20240610234308/HFTF_Location_Test_JPN_2.png) |

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D con licencia libre (Sketchfab, API) ✅

Buscados con la API de Sketchfab (`downloadable=true`). La licencia es
la que dice Sketchfab; **el crédito va tal cual** en la descripción del
canal o del post.

**Objetos genéricos** (no son de la serie, se pueden usar):

| Modelo | Autor | Licencia | Caras | Enlace | Para qué |
|---|---|---|---|---|---|
| Road Roller | Lassi Kaukonen | CC BY 4.0 | 135.062 | [sketchfab](https://sketchfab.com/3d-models/02c2ffa7c88f40fca1718e568adebda6) | La apisonadora de Dio |
| Road Roller ARP 35 | Lassi Kaukonen | CC BY 4.0 | 445.124 | [sketchfab](https://sketchfab.com/3d-models/6a9b1acd83dd4463a2e839ba28ae1ded) | Ídem, más detalle |
| Polaroid Camera | Boxroom 3D | CC BY 4.0 | 271.257 | [sketchfab](https://sketchfab.com/3d-models/920ad62faa9d4aa48bc6e9535f3d07fe) | La cámara de la «foto psíquica» (concepto A) |
| Vintage Polaroid Camera | Fredrik Johansen | CC BY 4.0 | 16.220 | [sketchfab](https://sketchfab.com/3d-models/5aa71a3db5b84906a344c71f7620da3a) | Ídem, ligera |
| CRT television | Jackbooth325 | CC BY 4.0 | 26.762 | [sketchfab](https://sketchfab.com/3d-models/b1db78bdac0644b99ad24cc5ef1ea3ea) | El televisor del fotograma congelado (concepto C) |
| Retro CRT Television | crow | CC BY 4.0 | 15.254 | [sketchfab](https://sketchfab.com/3d-models/29314bf8b66f49f98ad50dffe4950abf) | Ídem |
| The Star (carta de tarot) | terpsichore | CC BY 4.0 | 16.710 | [sketchfab](https://sketchfab.com/3d-models/cd5829e8a5854fa994fded37916bb744) | Base para la carta de Stand |

**Objetos de la serie hechos por fans** (el modelo es CC, pero el
diseño es de Araki y Shueisha: **sólo para mirar volumen y luz**):

| Modelo | Autor | Licencia | Enlace |
|---|---|---|---|
| Stand Arrow (la flecha que da Stands) | Miaru3d | CC BY | [sketchfab](https://sketchfab.com/3d-models/b53212fb380d40678dd15475f9dd57f7) |
| (free) stone mask from JJBA | Sungsoo Park | CC BY | [sketchfab](https://sketchfab.com/3d-models/884d901a20134ae5a012e8591abd3370) |
| Menacing ゴ Symbol | 09williamsad | CC BY | [sketchfab](https://sketchfab.com/3d-models/9b0d8b545cc14f1597199c11d8095015) |
| Dio's Road Roller | DopamineWarlock | CC BY | [sketchfab](https://sketchfab.com/3d-models/31c863c69e6149b9bdb67bd07de60f4c) |
| Jotaro Hat | MariusDatSenpai | CC BY | [sketchfab](https://sketchfab.com/3d-models/a648b2d18ae546a8a5c44c9ad072d7e0) |
| Jotaro from JOJO | ComputerCat | CC BY | [sketchfab](https://sketchfab.com/3d-models/6db23021ff0d4ab5aa83a14dfc67b586) |
| Jojo - DIO | LorisC93 | CC BY-NC | [sketchfab](https://sketchfab.com/3d-models/65d50c019a444350a95393fef121fb16) |

### 4.2 Herramientas de fans en GitHub ✅

| Repositorio | Licencia | Qué hace | Para qué |
|---|---|---|---|
| [valkyrs/jojo-stands](https://github.com/valkyrs/jojo-stands) | MIT | Dibuja la **gráfica de Stand** en un canvas HTML | Sacar el hexágono con las notas exactas |
| [MrPakoras/JoJoTBCfier](https://github.com/MrPakoras/JoJoTBCfier) | sin licencia declarada ⚠️ | Hace el **meme «To Be Continued»** con cualquier vídeo | Medidas del meme (§2.2); **no copiar su flecha**: es un recorte |
| [Dogend233/astrbot_plugin_jojo_stand_panel](https://github.com/Dogend233/astrbot_plugin_jojo_stand_panel) | AGPL-3.0 | Bot de chat que te da **tu Stand del día** con su ficha | Idea para #memes: «¿cuál es tu Stand?» |

### 4.3 Fan art 2D (mirar, nunca pegar)

- **Pixiv** (API de búsqueda, 24-sep-2026): la etiqueta
  ジョジョの奇妙な冒険 tiene **107.481** obras; ジョジョ立ち (pose JoJo),
  **2.918**; ゴゴゴゴ, **365**; To_Be_Continued, **170**; y
  ジョジョ100users入り (las que pasan de 100 favoritos), **5.879**.
- **Parodias de la ficha de Stand** hechas por fans: la serie
  «スタンドアイキャッチ風» («estilo eyecatch de Stand») de
  **鯖Escalation**, por ejemplo
  [pixiv 79591005](https://www.pixiv.net/artworks/79591005) (1500×937).
  Demuestra que **la ficha de Stand funciona como plantilla de meme**
  para cualquier cosa.
- Obras recientes con la etiqueta ジョジョ パロディ (614): por ejemplo
  [«8番出口の無限ループに迷い込んだディアボロ»](https://www.pixiv.net/artworks/148995246)
  (Diavolo atrapado en el bucle del juego *El pasillo 8*, 2338×1699):
  el chiste de Diavolo que **muere para siempre** sigue vivo en 2026.
- **Reddit**: el subreddit de memes es **r/ShitPostCrusaders**. Lo más
  votado del verano de 2026 es **de Steel Ball Run** (§14).

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

| Sitio | Parte | Cómo es | Imagen |
|---|---|---|---|
| **Mansión Joestar** (Inglaterra, 1880) | PB | Casa victoriana, madera oscura, velas | F16-F28 (hojas de modelo) |
| **El Cairo y la mansión de DIO** | SC | Noche, ocres y negros; DIO en la azotea | F242 |
| **La celda de Jotaro** (Japón) | SC ep. 1 | Gris azulado, rejas, ドォォーン en violeta | F187 |
| **Morioh** (杜王町) | DU | Pueblo residencial de los 80-90, **cielo amarillo** en el anime | F315 · F320 |
| **Casa de Rohan** (su estudio) | DU | Mesa de dibujo, plumillas, tinta | F450 · F492 |
| **Nápoles** y la Italia de GW | GW | Piedra clara, atardeceres naranjas | F418 · F458 |
| **Cárcel Green Dolphin Street** (Florida) | SO | Verde agua y azul noche | W11 |
| **El oeste americano, 1890** | SBR | Desierto, sepia verdoso, caballos | W12 |

- **Morioh es Sendai**: el pueblo está cerca de «S City», en «M
  Prefecture», en referencia a **Sendai (Miyagi)**, la ciudad natal de
  Araki; él cuenta que Sendai era una ciudad histórica que en los 80 se
  llenó de casas nuevas ⚠️ (una fuente: [JoJo Wiki: Morioh](https://jojowiki.com/Morioh),
  que cita a Araki).
- La encuesta de JoJo Wiki de agosto de 2026 («¿en qué escuela te
  gustaría estudiar?») la ganó el **instituto Budogaoka de Morioh** con
  el **49,37 %** ✅ ([JoJo Wiki: Poll History](https://jojowiki.com/JoJo_Wiki:Poll_History)).

### 5.2 La luz y el color (lo que hace el anime) ✅

- **El color cambia a propósito.** El anime tiene un color base para
  cada personaje y, en los momentos fuertes, **cambia la paleta entera
  de la escena o del plano** («シーン特色», «カット特色»). Lo hace porque
  las **ilustraciones a color de Araki cambian de color** de una a otra
  ✅ ([Portal oficial, notas de producción 02](https://jojo-portal.com/special/production-note/02/);
  [Anime Da Vinci, entrevista al director visual](https://ddnavi.com/interview/208016/a/)).
- Por eso, **un Jotaro verde o un Dio violeta no es un error**: es JoJo.
- **Sombras duras y muchas**: rayado a pluma en la cara, labios
  marcados, ojos con línea gruesa ⚠️ (visto en F10-F12 y F190).
- El opening de Stone Ocean se hizo en 3D con **Kamikaze Douga**, y su
  regla era que **desde cualquier ángulo pareciera dibujo de JoJo** ✅
  ([CGWorld](https://cgworld.jp/article/jojo-kamikaze-2303.html)).

### 5.3 Paleta (medida por mí en fotogramas de la wiki, ±10) ✅

| Escena | Colores dominantes |
|---|---|
| Morioh, cielo amarillo (F315) | noche `#201E2B` · crema `#DFE1C2` · **amarillo mostaza `#B79E2D`** · gris `#706A5F` |
| El Cairo de noche (F242) | negro café `#160D08` · marrón `#2E1C11` · **oro viejo `#A97944`** |
| OP de DU con Jotaro (F173) | negro `#111216` · crema `#F1ECD6` · rojo teja `#A74733` · verde azulado `#4C7772` · **lima `#BCEB38`** · **fucsia `#A5116C`** |
| OP de DU con Josuke (F302) | verde gris `#8F987E` · berenjena `#560433` · crema `#EDE2C8` |
| Celda de Jotaro (F187) | grises azulados `#1E1E1C` a `#5B5F70` |
| Nápoles con Giorno (F418) | crema `#F2F0D2` · oliva `#7D7958` · vino `#523735` · rosa viejo `#AC8685` |
| Bucciarati al atardecer (F458) | casi negro `#1D1514` · **naranja piel `#C5976E`** · miel `#F1D199` |
| Casa de Rohan (F492) | gris violeta `#37353D` · papel `#E1D6BF` · malva `#A47C97` · verde `#92AD76` |
| Cámara y Hermit Purple (F234) | verde oscuro `#2E3223` · **rosa violeta `#AF6788` y `#D8A8C5`** |
| Flecha TBC (W1, W3) | relleno `#B4C0A8` · letra `#48483C` a `#606054` · fondo carmesí `#600000` |

**Colores de cada JoJo** (de la ropa icónica). **Segunda pasada:
medidos** con `herramientas/estilo.py` (paleta dominante, no a ojo) sobre
arte oficial de cuerpo entero de la wiki; donde la imagen tiene fondo
blanco sólo cuento los colores que no son blanco o negro puro ✅.

| Personaje | Imagen medida | Colores medidos |
|---|---|---|
| Jotaro (SC) | [Jotaro_ASB.jpg](https://static.wikia.nocookie.net/jjba/images/7/71/Jotaro_ASB.jpg) 3750×5000 | **azul noche del abrigo `#163F58`** · casi negro `#070F13` · gris `#AFA7A8` · la cadena dorada es <2 % del área. **La gorra es negra con insignia dorada, no blanca** (antes decía «blanco del gorro»: error). Visto así en el tráiler de All-Star Battle R, [Dailymotion x8x1bgw](https://www.dailymotion.com/video/x8x1bgw) **1:20**: cadena `#7B5325`, chaqueta `#221223`, camisa lila `#4B2750` (escena a contraluz, tonos apagados) ✅ |
| Jotaro (DU) | a ojo sobre F173 ⚠️ | **blanco `#F2F0E8`** · verde agua de la camisa `#4C7772` · oro |
| Dio (PB→SC) | [DioBrando-ASB.jpg](https://static.wikia.nocookie.net/jjba/images/6/60/DioBrando-ASB.jpg) 1280×720 | **dorado mostaza `#BA963C`** y `#916F38` · marrón oscuro `#271A19`, `#3E2D26` · piel `#C4A987` ✅ |
| Joseph | [Joseph_ASB.jpg](https://static.wikia.nocookie.net/jjba/images/0/0b/Joseph_ASB.jpg) 690×690 | verde botella `#11563A` · `#52A114` · turquesa `#0FC5AC` · lima `#C3EB35` · piel `#CEAB8B` ✅ |
| Josuke | [Josuke_Higashikata.png](https://static.wikia.nocookie.net/jjba/images/f/f8/Josuke_Higashikata.png) 567×901 | azul marino casi negro `#040306` · **celeste de la camisa `#A8D6EC`** · violeta del pelo `#493756`, `#625782` · piel `#ED9688` · oro de los broches (corazón y paz) ✅ |
| Giorno | [Giorno_Giovanna_Anime_2.png](https://static.wikia.nocookie.net/jjba/images/6/63/Giorno_Giovanna_Anime_2.png) 658×1223 | **rosa fucsia `#BD7DAD`**, `#65356B` · crema `#DBD1B0` · dorado `#DDBD60` · piel `#E4C29E` ✅ |
| Bucciarati | [Bruno_Bucciarati_Anime.png](https://static.wikia.nocookie.net/jjba/images/a/af/Bruno_Bucciarati_Anime.png) 1080×1311 | **crema del traje `#F4E6D3`** (no blanco puro) · lunares y pelo `#100A09` · rojo `#EF3841` · piel `#EEC68F` ✅ |
| Kira | [Yoshikage_Kira_pin-up.jpg](https://static.wikia.nocookie.net/jjba/images/a/a2/Yoshikage_Kira_pin-up.jpg) 850×1063 | **violeta azulado `#3C3A50`**, `#272133`, `#858ACB`, `#BAB7F3` · gris `#645A69` ✅ |
| Rohan | [Rohan_accepts_Ken's_challenge.png](https://static.wikia.nocookie.net/jjba/images/4/49/Rohan_accepts_Ken%27s_challenge.png) 1920×1080 | **verde apagado `#718F71`** · piel `#CCAC99` · acento magenta `#D62450` ✅ |
| Jolyne | [Jolyne_Cujoh.png](https://static.wikia.nocookie.net/jjba/images/8/84/Jolyne_Cujoh.png) 444×563 | **oliva lima `#B7B338`** (antes `#9CCB3C` a ojo: era más verde de lo real) · turquesa `#51ABB6` · piel `#ECAA80` · moños en la cabeza ✅ |

**Sitios medidos en vídeo** (segunda pasada, Pillow sobre fotogramas):
muro azteca del ending «Roundabout» `#8F7B61` a `#AFA07E` con la línea
roja `#8B1A1A` ([Dailymotion x3j25ta](https://www.dailymotion.com/video/x3j25ta), 0:40) ✅;
humo de Killer Queen `#110617` a `#5A058C`, máscara `#F3E6F2` (avance DU
ep. 36, [Dailymotion x547qml](https://www.dailymotion.com/video/x547qml), 0:04) ✅;
cielo de Morioh en el avance del ep. 33 ([x5mk7ho](https://www.dailymotion.com/video/x5mk7ho), 0:00)
confirma el mostaza `#B79E2D` de F315 ✅.

### 5.4 Texturas reales equivalentes (Poly Haven, CC0) ✅

Todas de [Poly Haven](https://polyhaven.com/textures), **licencia CC0**
(sin crédito obligatorio), vistas en su API.

| Para | Textura |
|---|---|
| La mesa de dibujo de Rohan o el escritorio de Jotaro | `wood_table_worn`, `wood_table_001` |
| Una calle de Morioh | `asphalt_02`, `worn_asphalt`, `painted_plaster_wall` |
| El Cairo / Egipto | `large_sandstone_blocks`, `sandstone_cracks`, `red_sand` |
| El desierto de SBR | `sand_01`, `sandy_gravel` |
| Nápoles | `yellow_plaster`, `clay_roof_tiles`, `herringbone_brick` |
| Cuero de la cartera de Giorno o de un álbum | `brown_leather`, `fabric_leather_01` |

- **Papel**: para la carta de tarot o una hoja de manga hace falta un
  papel real. Poly Haven no tiene uno bueno; usar un escaneo propio de
  cartulina o papel de dibujo ⚠️.
- **Película Polaroid**: el marco blanco es **más ancho abajo**; la
  imagen es cuadrada ⚠️ (de memoria; comprobar con una foto real).

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

- **No hay una letra oficial de JoJo**. El logo **se redibuja en cada
  parte** ✅ ([Made Good Designs](https://madegooddesigns.com/jojos-bizarre-adventure-font/);
  y a la vista en F67-F72 y en los openings).
- **La flecha «To Be Continued»**: escrita **a mano con rotulador**,
  gruesa, letras unidas («BeContinued»), en verde oliva sobre salvia
  (W3 a tamaño completo) ✅.
- **Los nombres de Stand en el anime**: japonés en **mincho grueso
  blanco**, con la lectura en katakana pequeña encima (F190, F278) ✅.
- **Los rótulos de la ficha de Stand**: «[STAND MASTER]» y «[STAND
  NAME]» en **mayúsculas con serifa**, tipo Times, con bisel (W16) ✅.
- **Las onomatopeyas** (ゴゴゴ, ドドド, ドォォーン): **dibujadas a mano**,
  enormes, con perspectiva, en katakana; el anime las pone **encima de
  la imagen** (F187, W13, W14) ✅. Araki las usa como **música de
  suspense de cine**: no son ruido, son la tensión ✅
  ([Portal oficial, notas de producción 02](https://jojo-portal.com/special/production-note/02/);
  [JoJo Wiki: Sound Effects](https://jojowiki.com/Sound_Effects)).
- **Fuentes de fans**: en FontSpace sólo hay **Jojomix** (i2f, 2007),
  de **36 glifos** y **sin uso comercial**: **no sirve** (no tiene ni
  tildes) ✅ (su ficha en [FontSpace](https://www.fontspace.com/category/jojos-bizarre-adventure)).
  En dafont, «jojo» no devuelve ninguna letra de la serie ✅.

### 6.2 Letras libres comprobadas por mí (fontTools)

Bajadas de [google/fonts](https://github.com/google/fonts). **Todas**
traen á é í ó ú ñ ¿ ¡ ✅. La columna «japonés» dice si traen además
ゴ, ド, 無駄 o 破壊力.

| Uso | Letra | Licencia | Japonés | Nota |
|---|---|---|---|---|
| **ゴゴゴ y ドドド** (onomatopeya) | **Dela Gothic One** | OFL | sí | Gruesa, con cuña; la mejor para ゴゴゴ |
| ゴゴゴ, versión «rota» | **Rampart One** | OFL | sí | Letra hueca en 3D, muy de cartel |
| ゴゴゴ, versión pincel | **Reggae One** · **RocknRoll One** · **Potta One** | OFL | sí | |
| **Nombre del Stand** en japonés (mincho) | **Shippori Mincho B1** (Bold/ExtraBold) · **Zen Old Mincho** · **Noto Serif JP** | OFL | sí | Como 星の白金 |
| **Etiquetas del reloj** (破壊力…) | **Zen Kaku Gothic New** Bold · **M PLUS 1p** Bold | OFL | sí | |
| **«[STAND MASTER]» / «[STAND NAME]»** | **EB Garamond** · **Libre Caslon Text** · **Cinzel** | OFL | no | Mayúsculas con serifa; Cinzel si se quiere más «grabado» |
| **La flecha TBC**, texto en español | **Caveat Brush** (escalar 115 % a lo ancho) · **Mali Bold** · **Itim** | OFL | no | La comparé con la flecha real (W3): la más parecida en trazo es Caveat Brush; en peso, Mali Bold ⚠️ |
| Títulos de cartel (ej. «MEMES») | **Anton** · **Bebas Neue** · **Bungee** | OFL | no | |
| Globo de cómic | **Bangers** · **Luckiest Guy** (Apache) | OFL / Apache | no | Bangers es la que usa el generador de fans del meme TBC |

> [!tip] La flecha, mejor calcada
> Las palabras **«To Be Continued»** son parte del meme: se reconocen por
> **la forma exacta de la letra**. Recomiendo **calcar la flecha del
> anime** (W3, que está sola sobre rojo, a 1920×1080) y usar Caveat
> Brush **sólo** para lo que se escriba en español dentro o al lado.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

**Lo más importante**: JoJo **casi nunca** usa un globo blanco neutro
como marca. Tiene **siete** formas propias de poner texto en pantalla.

### 7.1 Lo que la serie pone en pantalla

| # | Forma | Dónde se ve | Para qué sirve en #memes |
|---|---|---|---|
| 1 | **La flecha «To Be Continued»** sobre un **fotograma congelado con filtro de color** | final de casi todos los episodios (W1-W12) ✅ | **Es el meme**. La regla del canal puede ir en la flecha |
| 2 | **La ficha de Stand**: reloj con seis notas A-E, [STAND MASTER] y [STAND NAME] | eyecatches de DU, GW y SO (W16-W23) ✅ | **Ficha del «Stand» del canal** |
| 3 | **La carta de tarot** con el nombre en mincho y la lectura en katakana | presentaciones de SC (F190, F278) ✅ | Presentar a quien habla |
| 4 | **Onomatopeya gigante** ゴゴゴ / ドドド / ドォォーン, en violeta o negro | todo el anime (F187) ✅ | «Aquí pasa algo»: marco del texto principal |
| 5 | **Texto del narrador** sobre la imagen (mincho blanco, horizontal) | «心臓に残った指輪溶解まで ―あと6日» (W4) ✅ | Una frase seria de narrador para el chiste |
| 6 | **Páginas de libro en la cara** (Heaven's Door): texto en columnas sobre la piel | DU (F476, F492, F494) ✅ | **Rohan «escribe» la regla** en alguien |
| 7 | **La página de manga dentro del anime**: el **opening de 2012** muestra a los JoJo del futuro **en páginas de manga** con su frase en globo japonés («あたしは空条徐倫ッ») | F431, F435 ✅ | Globo de manga **auténtico** (vertical, a mano) |

Y en los videojuegos:

| Juego | Cuadro de diálogo | Imagen |
|---|---|---|
| *Phantom Blood* (PS2, 2006) | Caja **blanca con el borde rasgado como papel**, retrato del que habla en una esquina, texto japonés en negro; la escena va en **viñetas de manga** sobre fondo 3D | F82 a F116 (hojas 02-03 de la herramienta) ✅ |
| *GioGio's Bizarre Adventure* (PS2, 2002) | Flecha **To Be Continued** al ganar; letrero «再起不能» (fuera de combate) | W24 ✅ |
| *Heritage for the Future* (Capcom, arcade 1999; versión de prueba japonesa) | Flecha **naranja** «To Be Continued...» | W25 ✅ |
| *All Star Battle R* (2022) y *Eyes of Heaven* (2015) | Onomatopeyas en katakana cruzando la pantalla; barras de vida con el retrato | F185, F186, F212, F1203 ✅ |
| *Last Survivor* (arcade, 2019) | Flecha TBC **del anime** cuando cae el último | W15 ✅ |

(La historia de la flecha en cada juego está en
[JoJo Wiki: To Be Continued](https://jojowiki.com/To_Be_Continued) ✅.)

### 7.2 Cómo hablan (por el subtítulo japonés)

- **Frases cortas y con muletilla propia**: やれやれだぜ (Jotaro),
  グレート (Josuke), だが断る (Rohan), 無駄 (Dio, Giorno) ✅ (§2).
- **Terminan en ッ o ォ** para gritar: 「このヘアースタイルがサザエさんみてェーだとォ」
  (DU ep. 1, 00:06:08) ✅. En la lámina, el grito se nota con **letras
  estiradas** («¿Qué dijiste de mi peeelo?»).
- **Se presentan en tercera persona** con su nombre completo: «この
  ジョルノ・ジョバァーナには夢がある», «この岸辺露伴が», «このDIOだ» ✅.
  **En español funciona igual**: «Este Giorno Giovanna tiene un sueño».
- **Los villanos explican su plan** en voz alta, con calma, y **los
  héroes lo adivinan antes** («Tu siguiente frase será…») ✅.
- **Los nombres en inglés y en italiano** (Stands con nombres de
  canciones y grupos: Killer Queen, Sticky Fingers, Stone Free) ✅.

### 7.3 Cómo se traduce a una lámina fija

- **El texto principal** del canal va en **uno de estos cuatro**, no en
  un globo blanco:
  1. dentro de la **flecha To Be Continued** (salvia `#B4C0A8`, letra
     `#48483C`);
  2. en la **ficha de Stand** (etiquetas blancas sobre trama de color);
  3. **escrito en páginas** por Heaven's Door;
  4. en una **carta de tarot** con el nombre en mincho.
- **La voz del personaje** va en un **globo de manga japonés** (óvalo
  fino, a mano, con cola corta), como en el opening de 2012 (F431 y F435), **o**
  sin globo, como **texto de narrador** blanco en mincho.
- **La tensión** se marca con **ゴゴゴ** en Dela Gothic One, en violeta
  (`#6A3D9A` aprox. ⚠️) o negro con borde blanco, **detrás** del
  personaje, nunca tapándole la cara.

### 7.4 Qué NO hacer con el texto

- **Flecha apuntando a la derecha**, o en el centro de la imagen: la
  flecha va **abajo a la izquierda y apunta a la izquierda** ✅.
- **Sepia plano de plantilla** en todo: el anime usa **filtros de color
  de cada parte** (magenta en DU, verde agua en GW y SO) ✅.
- Poner ゴゴゴ en **hiragana** (ごごご) o en letra fina: es **katakana
  gruesa**.
- Traducir «ORA ORA» o «MUDA MUDA» en el grito escrito: los fans lo
  reconocen **en japonés**. (El doblaje latino dice «¡Inútil, inútil!»
  para MUDA: ver §10; se puede usar **como chiste**, no como norma).
- Usar Comic Sans o una letra infantil para la flecha.

---

## 8 · Los personajes

Los cinco del encargo primero (Jotaro, Dio, Joseph, Giorno, Josuke) y
luego los secundarios más queridos (Rohan, Bucciarati, Kira, Jolyne).
Voz japonesa y latina de la tabla de Doblaje Wiki (API, §10). El
carácter, de las páginas de [JoJo Wiki](https://jojowiki.com) ✅ y de
los subtítulos ✅; lo que es de memoria va con ⚠️.

### Jotaro Kujo (空条承太郎) — la cara de JoJo

- **Quién es**: estudiante japonés de 17 años en SC; en DU, adulto,
  biólogo marino; en SO, el padre de Jolyne. Stand: **Star Platinum**
  (A · A · C · A · A · A), que **para el tiempo** unos segundos.
- **Carácter** ✅ (JoJo Wiki): parece un **delincuente violento**, pero
  tiene **buen corazón** y es leal con los suyos. Muy listo y rápido.
  **Frío, callado, desganado**. Se expresa con **frases cortas** y cree
  que los demás le leen las emociones sin que hable.
- **De dónde sale** ✅: Araki se inspiró en **Clint Eastwood**. Jotaro
  **no corre**, se mueve poco, y su **pose de señalar con el dedo**
  viene de Eastwood **apuntando con su Magnum .44**; su muletilla, de
  frases de Eastwood ([JoJo Wiki: Jotaro Kujo](https://jojowiki.com/Jotaro_Kujo)).
- **Qué le importa**: su madre Holly (por ella viaja a Egipto), sus
  amigos, acabar el trabajo. **Miedo**: casi no lo muestra; en SC ep. 48
  «deja de pensar» ante Dio (00:07:57 ✅).
- **Cómo habla**:
  - Muletilla: **やれやれだぜ** («qué fastidio»), en latino **«Ay, por
    favor»** ✅. La dice **suspirando**, con la visera baja.
  - Remata con una frase fría: «てめえは 俺を 怒らせた» («me hiciste
    enojar», SC ep. 48, 00:14:56 ✅).
  - **Cómo se ríe**: casi nunca; una media sonrisa («フッ», SC ep. 6,
    00:05:14 ✅).
  - **Cómo se enfada**: no grita al principio; baja la voz y **deja
    que el Stand grite** (ORA ORA).
  - **Cómo saluda**: no saluda; se toca la visera ⚠️.
- **Lenguaje corporal** ⚠️ (visto en F5, F173, F190, F212):
  - Gorra calada hasta los ojos; se toca **la visera con dos dedos**.
  - Una mano en el bolsillo, la otra **señalando** al frente.
  - El abrigo (gakuran) abierto, con **la cadena dorada** del cuello.
  - En DU, abrigo **blanco** y camisa verde agua; más quieto aún.
- **Con quién sale**: Joseph (abuelo), Kakyoin, Polnareff, Avdol, Iggy
  (SC); Koichi y Josuke (DU); Jolyne (SO).
- **Voz japonesa**: Daisuke Ono ✅. **Latina**: **Irwin Daayán** (SC,
  DU y SO) ✅.

### Dio Brando / DIO — el villano que es un meme

- **Quién es**: hermano adoptivo de Jonathan en PB; se hace **vampiro**
  con la máscara de piedra; en SC vuelve como **DIO**, con el Stand
  **The World** (A · A · C · A · B · B), que **para el tiempo**. Es el
  padre de Giorno.
- **Carácter** ✅ (JoJo Wiki): **manipulador y dominante**, sin
  conciencia ni empatía. Araki lo describe como **un parásito** que se
  mete en la familia Joestar para quitárselo todo. Tuvo un **padre
  maltratador** y una infancia en la miseria: quiere ser **el más rico
  y el más poderoso**. Se rodea de **secuaces** atraídos por su carisma.
- **Qué le importa**: el poder y **estar por encima**. **Miedo**:
  que alguien sea su igual; le **enfurece y trastorna**.
- **Cómo habla**:
  - Se nombra a sí mismo: **«このディオだ!»** («¡fue este Dio!», PB
    ep. 1, 00:15:53 ✅). En latino: «Tu primer beso no fue con JoJo,
    **fue conmigo, Dio**» ✅ (clip del doblaje, §10).
  - Grita **MUDA MUDA** («¡inútil!», en latino **«¡Inútil, inútil,
    inútil!»** ✅) y **WRYYY**.
  - Presume: «最高に ハイってやつだ!» (SC ep. 47, 00:23:34 ✅).
  - **Cómo se ríe**: a carcajadas, con la cabeza hacia atrás ⚠️.
  - **Cómo explica algo**: despacio, con desprecio, como a un niño
    («¿Recuerdas cuántos panes te has comido?», PB ep. 5, 00:07:33 ✅).
- **Lenguaje corporal** ⚠️ (F237, F238, F239, F242):
  - **Poses imposibles**: torso girado, brazo sobre la cabeza.
  - **Dedo en la sien** con sonrisa de loco (F239, «high as hell»).
  - De pie **en la azotea de El Cairo** con capa, de noche (F242).
- **Voz japonesa**: Takehito Koyasu ✅. **Latina**: **Marc Winslow** es
  la voz base en las partes 1, 3 y 6 (PB, SC y SO) ✅. **Sergio Becerril**
  sólo dobla **el episodio 12 de Stone Ocean** ✅ ([Doblaje Wiki: Dio Brando](https://doblaje.fandom.com/es/wiki/Dio_Brando),
  [World Dubbing News ES](https://x.com/wdn_es/status/1466979864297328643)).
  El artículo de ANMTV que pone a Becerril en Phantom Blood **está mal**
  (ver §10.2).

### Joseph Joestar — el bromista (joven en BT, viejo en SC y DU)

- **Quién es**: nieto de Jonathan. En BT, joven peleador con Hamon
  («Jámon» en latino ✅). En SC, **abuelo** de Jotaro con el Stand
  **Hermit Purple** (D · C · D · A · D · E), unas zarzas violetas que
  hacen **fotos psíquicas** rompiendo una cámara (F234 ✅). En DU,
  anciano, **duro de oído** (F285).
- **Carácter** ✅ (JoJo Wiki): **impulsivo y provocador**; de joven
  estuvo **preso siete veces** y lo expulsaron del colegio por pelear.
  Sólo respeta a su abuela y a Lisa Lisa. **Juguetón**, odia las frases
  «trabajo duro» y «esfuérzate», y gana con **trucos absurdos**.
- **Qué le importa**: sus amigos (llora a Caesar, BT ep. 20); su
  familia. **Miedo**: trabajar ⚠️ (en broma).
- **Cómo habla**:
  - **«Tu siguiente frase será…»** y acierta (BT ep. 10, 00:16:19 ✅).
  - **«¡Nigerundayo!»** («¡hay que huir!», BT ep. 11, 00:08:44 ✅).
  - **«OH MY GOD!»** con las manos en la cabeza (SC ep. 27, 00:16:17 ✅)
    y **«OH NO!»** (BT ep. 15, 00:05:55 ✅).
  - **Cómo se ríe**: fuerte, burlón, sacando la lengua ⚠️.
  - **Cómo se enfada**: grita el nombre del otro («¡SHIIIZAAA!» en BT
    ep. 20) ⚠️.
  - **Cómo explica algo**: como un mago que enseña el truco **después**.
- **Lenguaje corporal** ⚠️ (F29-F34, F280, F285, F298): viejo con
  **sombrero de fieltro**, barba blanca, **guantes** (tiene una mano de
  metal), **walkman** en SC (F280), mano en la oreja porque no oye (F285).
- **Voz japonesa**: Tomokazu Sugita (joven) ✅; Unshō Ishizuka (viejo)
  ✅. **Latina**: **Miguel de León** (joven, BT) ✅; **Raúl Anaya**
  (viejo, SC y DU) ✅.

### Giorno Giovanna — el que tiene un sueño

- **Quién es**: hijo de DIO (con el cuerpo de Jonathan), 15 años, en
  Nápoles. Stand: **Gold Experience** (C · A · C · D · C · A), que **da
  vida** a las cosas; luego **Requiem** (∅: no se puede medir).
- **Carácter** ✅ (JoJo Wiki): de niño, **solo y maltratado** por su
  padrastro; cambió al ayudar a un gánster que lo protegió. Su rasgo es
  **el «覚悟» (la determinación)**: decide sin dudar y **lo lleva hasta
  el final**, aunque le hieran. Quiere ser **«Gang-Star»** (en latino,
  **«Gángster estrella»** ✅).
- **Cómo habla**:
  - **«Yo, Giorno Giovanna, tengo un sueño»** (このジョルノ・ジョバァーナ
    には夢がある, GW ep. 5, 00:22:49 ✅), con **«Il vento d'oro»** detrás.
  - Frío y cortés: «Repetir es una pérdida de tiempo» (GW ep. 1,
    00:14:41 ✅; en latino, «**odio repetir cosas**… repetir es una
    pérdida de tiempo» ✅ por subtítulo automático del clip).
  - Grita **MUDA** como su padre (GW ep. 2, 00:09:37 ✅); en latino,
    primero «¡Desperdicio!» y **desde el ep. 19 «¡Inútil!»** ✅
    (Doblaje Wiki).
- **Lenguaje corporal** ⚠️ (F431, F726, F415): **mano abierta en el
  pecho**, cadera ladeada, **mano en la cintura**; mirada serena.
  **Tres rizos** en la frente y **mariquitas** doradas en el traje.
- **Voz japonesa**: Kenshō Ono ✅. **Latina**: **José Luis Piedra** ✅.

### Josuke Higashikata — el del peinado

- **Quién es**: hijo secreto de Joseph, estudiante de Morioh. Stand:
  **Crazy Diamond** (A · A · D · B · B · C), que **arregla** lo que toca
  (y cura a otros, no a sí mismo).
- **Carácter** ✅ (JoJo Wiki): parece **un pandillero** y asusta al
  principio (Jotaro y Koichi lo creyeron «de miedo»), habla sin
  formalidad, pero es **muy bueno** y hace amigos de sus enemigos. **No
  soporta ver sufrir** y le cuesta aceptar la muerte, porque siempre
  pudo «arreglarlo todo». Jura **proteger Morioh** en lugar de su
  abuelo.
- **Qué le importa**: su madre, su abuelo, su pueblo… y el dinero
  (F330, con Okuyasu).
- **Cómo habla**:
  - **«¡Great!»** (グレートですよ こいつはァ, DU ep. 2, 00:17:09 ✅).
  - **La regla de oro**: si alguien se burla de su **tupé**, se
    transforma. «¿Qué dijiste de mi peinado?» (DU ep. 1, 00:06:08 ✅),
    aunque nadie haya dicho nada.
  - Grita **DORA DORA** (DU ep. 29, 00:02:13 ✅).
- **Lenguaje corporal** ⚠️ (F315, F320, F302, F318): **se peina el
  tupé** con las dos manos (F302), se agacha en cuclillas (F320), pose
  final con **dos dedos junto a la cara** y el cuerpo inclinado (F315) ✅.
- **Voz japonesa**: Yūki Ono ✅. **Latina**: **Luis Fernando Orozco** ✅.

### Rohan Kishibe — el secundario que tiene serie propia

- **Quién es**: mangaka de 20 años en Morioh. Stand: **Heaven's Door**
  (D · B · B · B · C · A): convierte a la gente **en libros**, lee su
  vida y **escribe órdenes** en sus páginas (F476, F492, F494 ✅).
  Tiene su propia serie (*Así habló Kishibe Rohan*, OVA con doblaje
  latino ✅ Doblaje Wiki).
- **Carácter** ✅ (JoJo Wiki): **entregado a su trabajo**, **borde**
  pero con buen fondo. «No dibujo manga por dinero: **dibujo porque
  quiero que me lean**». Busca **experiencias raras** para inspirarse,
  sin respetar la educación ni la ley (llega a **lamer una araña**,
  F488).
- **Cómo habla**:
  - **«…pero me niego»** (だが断る, DU ep. 28, 00:20:19 ✅): «una de las
    cosas que más me gustan es **decirle que no** a quien cree tener
    razón».
  - Se burla del pelo de Josuke (F398) y se pelean siempre.
- **Lenguaje corporal** (F3, F484, F450, F457): en su render oficial,
  **brazo sobre la cabeza y piernas cruzadas** (F3) ✅; sonrisa de lado,
  cinta verde en el pelo, **pendientes de plumilla** ✅; señalar con la
  plumilla ⚠️ (de memoria).
- **Voz japonesa**: Takahiro Sakurai ✅. **Latina**: **Irwin Daayán**
  (el mismo de Jotaro, con la voz **más suave y aguda**) ✅ (Doblaje
  Wiki y ANMTV).

### Bruno Bucciarati — el gánster honrado

- Stand: **Sticky Fingers** (A · A · C · D · C · D): pone **cremalleras**
  en todo.
- **Carácter** ⚠️ (de memoria, coherente con JoJo Wiki): gánster que
  **odia la droga**, protector, sereno; el líder que todos siguen.
- **Cómo habla**: «**Este es el sabor de un mentiroso**, Giorno
  Giovanna» (GW ep. 1, 00:21:23 ✅), tras **lamerle el sudor**.
  «**Arrivederci**» (GW ep. 16, 00:19:53 ✅). Grita **ARI ARI**.
- **Pose** (F458, F467, F7): mano en la cara, flequillo recto, traje
  blanco con cremalleras y lunares.
- **Voz latina**: **Luis Leonardo Suárez** ✅.

### Yoshikage Kira — el villano que quiere dormir ocho horas

- Stand: **Killer Queen** (A · B · D · B · B · A): convierte lo que toca
  en **bomba**. Tercera bomba: **Bites the Dust** (DU ep. 35, 00:16:49 ✅).
- **Carácter** ✅ (JoJo Wiki): **asesino en serie**, egocéntrico, con
  manías; **odia cualquier cambio** en su rutina; **nunca quiere quedar
  primero** (se queda tercero a propósito).
- **Cómo habla**: su **monólogo** (DU ep. 21, 00:20:25 a 00:21:27 ✅):
  «Me llamo Yoshikage Kira. Tengo 33 años. Mi casa está en la zona de
  villas del noreste de Morioh. No estoy casado. Trabajo en las tiendas
  Kame Yu. Vuelvo a casa a las ocho como tarde. No fumo; bebo poco. Me
  acuesto a las once y **duermo ocho horas**. Antes, **leche caliente**
  y veinte minutos de estiramientos… Sólo quiero **una vida tranquila**».
- **Voz latina**: **José Gilberto Vilchis** ✅ (Doblaje Wiki y
  [JoJo Wiki](https://jojowiki.com/Jos%C3%A9_Gilberto_Vilchis)).

### Jolyne Cujoh — la primera JoJo mujer

- Hija de Jotaro, presa en Florida. Stand: **Stone Free** (A · B · C ·
  A · C · A): se deshace **en hilo**.
- **Cómo habla**: **やれやれだわ**, la versión femenina del «yare yare»
  (SO ep. 2, 00:20:59 ✅), en latino también **«Ay, por favor»** ✅
  (Doblaje Wiki). Grita ORA ORA como su padre.
- **La mejor ropa de todos los JoJo** para los fans: **35,45 %** en la
  encuesta de JoJo Wiki de julio de 2026 (Jotaro 2.º con 17,73 %) ✅
  ([Poll History](https://jojowiki.com/JoJo_Wiki:Poll_History)).
- **Voz latina**: **Alondra Hidalgo**, que además **codirige** el
  doblaje de la parte 1 de SO ✅ (Doblaje Wiki y
  [Cinepremiere](https://cinepremiere.com.mx/jojos-bizarre-adventure-stone-ocean-anime-trailer-estreno.html)).

### Los secundarios que conviene tener a mano

| Personaje | Por qué | Frase con minuto | Voz latina |
|---|---|---|---|
| **Speedwagon** | El fan número uno de Jonathan | «Speedwagon se retira con estilo» (PB ep. 4, 00:03:41) ✅ | Víctor Ruiz ⚠️ |
| **Polnareff** | El que «no entiende qué pasó» | «Subía la escalera y la estaba bajando» (SC ep. 45, 00:06:42) ✅ | Miguel Ángel Leal ✅ |
| **Kakyoin** | La cereza «rero rero» | SC ep. 9, 00:07:03 ✅ | Héctor Emmanuel Gómez ✅ |
| **Okuyasu** | «¡Ñaaam!» con la comida de Tonio | «ンまあーいっ!» (DU ep. 10, 00:04:40) ✅ | Miguel Ángel Ruiz ✅ |
| **Koichi** | El amigo fiel; Echoes Act 3 dice «S・H・I・T» | DU ep. 24, 00:07:07 ✅ | Diego Becerril ✅ |
| **Pucci** | Cuenta números primos | SO ep. 12, 00:12:31 ✅ | Óscar Flores ⚠️ |
| **Gyro Zeppeli** | La risa «Nyoho» (SBR) | SBR ep. 1, 00:05:24 ✅ | **Xalisco Moreno** ✅ |
| **Johnny Joestar** | Protagonista de SBR | Monólogo final, SBR ep. 1, 00:44:49 ✅ | **Max Durán** ✅ |

---

## 9 · ¿Quién es el más querido?

| Encuesta | Tipo | Resultado |
|---|---|---|
| **Los 10 favoritos de Araki** (libro *JOJO A-GO!GO!*, 2000, p. 75) | Del autor | 1.º **Josuke**, 2.º **Kira**, 3.º **Bucciarati**, 4.º Doppio y Diavolo, 5.º Giorno, 6.º Joseph, 7.º Mista, 8.º Jotaro, 9.º Shigechi, 10.º DIO ✅ ([JoJo Wiki: Hirohiko Araki](https://jojowiki.com/Hirohiko_Araki)). Sus Stands favoritos: Crazy Diamond, Sex Pistols y Sticky Fingers ✅ |
| **Encuesta de episodios JOJODAY 2025** (oficial, 50.390 votos) | Oficial | Por partes: PB ep. 1 (22 %); **BT ep. 20, la muerte de Caesar (55 %, el más votado de todos)**; SC ep. 48 (12 %); **DU ep. 10, el restaurante de Tonio (15 %)**; GW ep. 28 (14 %); SO ep. 38 (28 %) ✅ ([JoJo Wiki: JOJODAY](https://jojowiki.com/JOJODAY); [portal oficial, resultado](https://jojo-portal.com/special/jojoday2025/episode-vote/result/); [ANN](https://www.animenewsnetwork.com/interest/2025-04-14/jojoday-2025-poll-names-fans-favorite-jojo-bizarre-adventure-episodes/.223542)) |
| **Ranking de los JoJo** (Nlab Research, 2021) | Fans, Japón | 1.º **Joseph**, 2.º Jotaro (3.491 votos, 26,4 %) ⚠️ una fuente, leída en el resumen de búsqueda ([Nlab](https://nlab.itmedia.co.jp/research/articles/202866/)) |
| **Minna no Ranking** (ranking.net, continuo) | Fans, Japón | Jotaro arriba «con mucha ventaja»; luego Jonathan y Joseph; Bucciarati 5.º ⚠️ (una fuente, cifras cambian) ([ranking.net](https://ranking.net/rankings/best-jojo-characters)) |
| **Encuesta de *All Star Battle*** | Fans | Empate en el 1.º: **Jonathan y Johnny** (534 votos) ⚠️ ([Renote](https://renote.net/articles/20661)) |
| **JoJo Wiki, julio 2026** | Fans, inglés | Mejor ropa: **Jolyne** 35,45 % ✅ |
| **JoJo Wiki, febrero 2026** | Fans, inglés | Personaje de SBR que más querían ver: **Gyro** (24,72 %) ✅ |

**Conclusión para #memes**:

- **El más reconocible** fuera del fandom: **Jotaro** (la pose, la
  gorra, el «yare yare»).
- **El rey de los memes**: **Dio** (Za Warudo, Road Roller, «¡fue este
  Dio!», WRYYY) y **Joseph** (Nigerundayo, «tu siguiente frase»,
  OH MY GOD). Los dos tienen **más frases-meme con minuto** que nadie
  en §2.
- **El secundario más querido** por el autor y por los fans que leen:
  **Bucciarati** y **Rohan** (Rohan tiene serie propia y un meme
  perfecto para un canal con una regla: «…pero me niego»).
- **El de moda en septiembre de 2026**: **Gyro** (Steel Ball Run se
  estrena semanal el 25 de septiembre).

---

## 10 · Doblaje latino

**Sí hay doblaje latino de todas las partes del anime**, en Netflix
Latinoamérica ✅. Cada nombre de abajo sale de **Doblaje Wiki por su
API** (`action=parse`, 24-sep-2026) y lo crucé con una segunda fuente:
**ANMTV**, JoJo Wiki, Star Con, Festival La Chida o el propio clip.
✅ = dos fuentes; ⚠️ = sólo Doblaje Wiki.

### 10.1 Estudios, directores y fechas

| Parte | Estudio | Dirección | Estreno latino | Fuentes |
|---|---|---|---|---|
| PB y BT (serie de 2012) | Iyuno • SDI Group, México | Roberto Molina | Netflix, **20 ene. 2022** | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/JoJo%27s_Bizarre_Adventure) · [ANMTV](https://www.anmtvla.com/2022/01/jojos-bizarre-adventure-doblaje-latino.html) · [TVLaint](https://www.tvlaint.com/2022/01/netflix-lanza-el-doblaje-latino-de-mas-partes-de-jojos.html?m=1) |
| SC («Los cruzados de polvo de estrellas») | Iyuno • SDI Group, México | Roberto Molina | Netflix, 20 ene. 2022 | ✅ mismas |
| DU | Iyuno • SDI Group, México | Roberto Molina | Netflix, **dic. 2021** | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/JoJo%27s_Bizarre_Adventure:_Diamond_is_Unbreakable) · [ANMTV](https://www.anmtvla.com/2021/12/jojos-bizarre-adventure-diamond-is.html) |
| GW | Iyuno • SDI Group, México | Roberto Molina | Netflix (2022) | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/JoJo%27s_Bizarre_Adventure:_Golden_Wind) · [Gamerfocus](https://www.gamerfocus.co/anime/cuando-jojos-bizarre-adventure-parte-5-golden-wind-netflix-actualiza-todas-las-temporadas-con-doblaje-al-espanol-de-latinoamerica/) |
| SO, parte 1 | Iyuno • SDI Group, México | **Alondra Hidalgo** y **Analiz Sánchez** | Netflix, dic. 2021 | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/JoJo%27s_Bizarre_Adventure:_Stone_Ocean) · [LevelUp](https://www.levelup.com/noticias/652383/Jojos-Bizarre-Adventure-Stone-Ocean-ya-esta-disponible-en-Netflix-con-doblaje-latino/) |
| SO, partes 2 y 3 | **New Art** | ⚠️ | 2022 | ⚠️ Doblaje Wiki |
| SBR | **New Art** | **Marc Winslow** | Netflix, **19 mar. 2026**; semanal desde el **25 sep. 2026** | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Steel_Ball_Run:_JoJo%27s_Bizarre_Adventure) · [ANMTV en X](https://x.com/ANMTVLA/status/2034641449514373435) |

- Traducción de PB a GW: **Ilda de Córdova** ⚠️. De SBR: **Abraham Vega** ⚠️.
- **Pluto TV Latinoamérica** sumó las cuatro primeras temporadas en
  febrero de 2024 ✅ ([ANMTV](https://www.anmtvla.com/2024/02/jojos-bizarre-adventure-pluto-tv.html)).
- Netflix **quitó el doblaje de España (Selecta Visión)** de las
  primeras partes al poner el latino ⚠️ (una fuente de búsqueda).

### 10.2 El reparto

| Personaje | Parte | Voz latina | ✅/⚠️ | Segunda fuente |
|---|---|---|---|---|
| **Jotaro Kujo** | SC, DU, SO | **Irwin Daayán** | ✅ | ANMTV; clip «Jotaro: Ay por favor» |
| **Dio / DIO** | PB, SC y SO (voz base en las partes 1, 3 y 6) | **Marc Winslow** | ✅ | [Doblaje Wiki: Dio Brando](https://doblaje.fandom.com/es/wiki/Dio_Brando); [FUNiAnime LA, elenco PB y BT](https://funianime.com/conoce-al-elenco-de-jojos-bizarre-adventure-phantom-blood-y-battle-tendency/) |
| DIO | **sólo SO ep. 12** | Sergio Becerril | ✅ | [Doblaje Wiki: Dio Brando](https://doblaje.fandom.com/es/wiki/Dio_Brando); [World Dubbing News ES](https://x.com/wdn_es/status/1466979864297328643) |
| Jonathan Joestar | PB | Ricardo Bautista | ✅ | búsqueda |
| Will A. Zeppeli | PB | César Garduza | ✅ | búsqueda |
| Speedwagon | PB, BT | Víctor Ruiz | ✅ | [SomosKudasai](https://somoskudasai.com/noticias/las-primeras-temporadas-de-jojos-bizarre-adventure-finalmente-consiguen-doblaje/) |
| Erina | PB | Montserrat Aguilar | ✅ | [FUNiAnime LA](https://funianime.com/conoce-al-elenco-de-jojos-bizarre-adventure-phantom-blood-y-battle-tendency/) |
| **Joseph (joven)** | BT | **Miguel de León** | ✅ | búsqueda |
| Caesar Zeppeli | BT | Carlo Vázquez | ✅ | SomosKudasai |
| Lisa Lisa | BT | Vianney Monroy | ⚠️ | sólo Doblaje Wiki ([ficha del actor](https://doblaje.fandom.com/es/wiki/Vianney_Monroy)) |
| Kars · Wamuu · Esidisi | BT | Jorge Badillo · Salvador Reyes · José Antonio Macías | ✅ | FUNiAnime LA (los tres juntos) |
| **Joseph (viejo)** | SC, DU | **Raúl Anaya** | ✅ | ANMTV |
| Kakyoin | SC | Héctor Emmanuel Gómez | ✅ | ANMTV |
| Polnareff | SC | Miguel Ángel Leal | ✅ | ANMTV |
| Avdol | SC | Alan Bravo | ✅ | ANMTV (y repite como Urmd en SBR) |
| Iggy | SC | Angélica Villa | ✅ | ANMTV |
| Hol Horse | SC | Carlo Vázquez | ✅ | [FUNiAnime LA, elenco SC](https://funianime.com/conoce-al-reparto-del-doblaje-latino-de-jojos-bizarre-adventure-stardust-crusaders/) |
| Holly Joestar · Enyaba · Mariah | SC | Jessica Ángeles · Magda Giner · Carla Castañeda | ⚠️ | sólo FUNiAnime LA |
| Terence D'Arby | SC | Fabián Rétiz | ⚠️ | sólo Doblaje Wiki ([ficha](https://doblaje.fandom.com/es/wiki/Fabi%C3%A1n_R%C3%A9tiz)) |
| Star Platinum (su voz) | SC | Mauricio Pérez | ⚠️ | — |
| The World (su voz) | SC | Eleazar Muñoz | ⚠️ | — |
| Narrador | todas | Osvaldo Trejo (SC eps. 1-4) → **Tommy Rojas** | ✅ | Doblaje Wiki cita entrevista de Tommy Rojas |
| **Josuke Higashikata** | DU | **Luis Fernando Orozco** | ✅ | ANMTV |
| Koichi Hirose | DU | Diego Becerril | ✅ | ANMTV |
| Okuyasu Nijimura | DU | Miguel Ángel Ruiz | ✅ | ANMTV |
| **Rohan Kishibe** | DU | **Irwin Daayán** | ✅ | ANMTV |
| **Yoshikage Kira** | DU | **José Gilberto Vilchis** | ✅ | JoJo Wiki |
| Tonio Trussardi | DU | Fabián Rétiz | ⚠️ | — |
| **Giorno Giovanna** | GW | **José Luis Piedra** | ✅ | Star Con; Festival La Chida |
| **Bruno Bucciarati** | GW | **Luis Leonardo Suárez** | ✅ | búsqueda |
| Guido Mista | GW | Eduardo Curiel | ✅ | búsqueda |
| Leone Abbacchio | GW | Geezuz González | ✅ | búsqueda |
| Narancia | GW | Luis Navarro | ✅ | búsqueda |
| Fugo | GW | Arturo Cataño | ✅ | [Gamerfocus](https://www.gamerfocus.co/anime/cuando-jojos-bizarre-adventure-parte-5-golden-wind-netflix-actualiza-todas-las-temporadas-con-doblaje-al-espanol-de-latinoamerica/) |
| Trish | GW | Wendy Malvárez | ✅ | búsqueda |
| Diavolo | GW | Roberto Mendiola (Óscar Rangel, eps. 33-38) | ✅ | Gamerfocus |
| Vinegar Doppio | GW | Emilio Treviño y Emmanuel Bernal | ⚠️ | sólo Gamerfocus |
| **Jolyne Cujoh** | SO | **Alondra Hidalgo** | ✅ | Cinepremiere; JoJo Wiki |
| Ermes | SO | Alicia Barragán | ✅ | búsqueda |
| Emporio | SO | Fernanda Robles | ✅ | búsqueda |
| Weather Report | SO | Manuel Campuzano | ✅ | búsqueda |
| Pucci | SO | Óscar Flores | ✅ | [FUNiAnime LA, elenco SO](https://funianime.com/conoce-al-reparto-del-doblaje-latino-de-jojos-bizarre-adventure-stone-ocean/) |
| Foo Fighters · Pale Snake · Johngalli A | SO | Alicia Vélez · Gerardo Vásquez · Juan Carlos Tinoco | ⚠️ | sólo FUNiAnime LA |
| **Johnny Joestar** | SBR | **Max Durán** | ✅ | ANMTV en X |
| **Gyro Zeppeli** | SBR | **Xalisco Moreno** | ✅ | ANMTV en X |
| Diego Brando | SBR | Marc Winslow (el mismo de Dio) | ✅ | búsqueda |
| Lucy Steel · Steven Steel | SBR | Andrea Orozco · Santos Alberto | ✅ | búsqueda |
| Pocoloco · Sand Man | SBR | José Arenas · Óscar López | ⚠️ | — |
| Comentarista de la carrera | SBR | Brandon Montor | ⚠️ | ANMTV en X |

> [!warning] Dos confusiones que circulan
> **1 · Dio en Phantom Blood.** El [artículo de ANMTV](https://www.anmtvla.com/2022/01/jojos-bizarre-adventure-doblaje-latino.html)
> del estreno de PB, BT y SC pone «Sergio Becerril como Dio Brando» en
> Phantom Blood. **Está mal**: Marc Winslow es la voz base de Dio en las
> partes 1, 3 y 6; Becerril sólo dobla el **ep. 12 de Stone Ocean**
> (Doblaje Wiki, ficha de la franquicia y del personaje; FUNiAnime LA) ✅.
> En España el reparto es otro ([eldoblaje.com](https://www.eldoblaje.com/)): no mezclar.
>
> **2 · Steel Ball Run.** Un resumen de búsqueda dio para SBR «Johnny: Armando Corona / Gyro:
> Alejandro Orozco». **Es falso**: en Doblaje Wiki, **Alejandro Orozco
> dobla a Mountain Tim**; Johnny es **Max Durán** y Gyro **Xalisco
> Moreno**, como dice también ANMTV ✅.

### 10.3 Cómo suena en latino (frases y decisiones)

| Original | En el doblaje latino | ✅/⚠️ |
|---|---|---|
| やれやれだぜ (Jotaro) | **«Ay, por favor»** (también la dicen Joseph y Jonathan) | ✅ Doblaje Wiki + [clip](https://www.youtube.com/watch?v=jSJT6gSmxTc) |
| やれやれだわ (Jolyne) | **«Ay, por favor»** | ⚠️ Doblaje Wiki |
| このディオだ! | «Tu primer beso no fue con JoJo, **fue conmigo, Dio**» | ✅ [clip](https://www.youtube.com/watch?v=wHYJ4Tkqj0o) (título y subtítulo automático) |
| 無駄無駄 (Dio) | **«¡Inútil, inútil, inútil!»** | ✅ Doblaje Wiki + [clip GW](https://www.youtube.com/watch?v=XpoTmSVNRDE) |
| 無駄 (Giorno) | «¡Desperdicio!» y, **desde el ep. 19, «¡Inútil!»** | ⚠️ Doblaje Wiki |
| ホラホラ (Polnareff) | **«¡Toma, toma, toma!»** | ⚠️ Doblaje Wiki |
| オラオラ (Jolyne) | «¡Toma, toma!» en el tráiler y el ep. 2; **luego se dejó en japonés** (ORA ORA), igual que el de Jotaro | ⚠️ Doblaje Wiki |
| Hey, baby (Zeppeli) | «Oye, amigo» | ⚠️ Doblaje Wiki |
| Hamon | «**Jámon**» | ⚠️ Doblaje Wiki |
| ロードローラー | «**Aplanadora**» | ⚠️ título de un [clip](https://www.youtube.com/watch?v=FNrvlqfz9CQ) |
| S・H・I・T (Echoes Act 3) | «¡Maldición!»; en el ep. 34, «M.I.E.R.D.A.» | ⚠️ Doblaje Wiki |
| Gang-Star | «Gángster estrella» | ⚠️ Doblaje Wiki |
| Star Platinum | mal pronunciado «Star Pla**tí**num»; bien sólo en SO ep. 35 | ⚠️ Doblaje Wiki |
| Steel Ball, Spin (SBR) | **se dejan en inglés** | ⚠️ Doblaje Wiki |

**Memes latinos metidos en el doblaje** (ideal para #memes) ⚠️ Doblaje
Wiki:

- **SC ep. 15**: Polnareff suelta el meme mexicano «**Ya siéntese,
  señora**».
- **DU ep. 35**: guiño al vídeo del presentador **Marco Martínez
  Soriano**: «**¿Ya estamos al aire? Avísenme**».
- **DU ep. 12**: el chiste de «Stand user / no vayas al dentista» pasa a
  «**¿Te encanta el pan?**», y Red Hot Chili Pepper a «**Chile Popó**».

**Fandubs** (no oficiales, útiles para #fandub-de-memes):

- «Jotaro Kujo Yare Yare Daze en español latino (**Ay, no me
  jodas!**)» de Sebastián Ono ([YouTube](https://www.youtube.com/watch?v=BhLhA0PnQTI), 30 s).
- «ROAD ROLLER-DA (fandub español latino)» de Eiji Animator
  ([YouTube](https://www.youtube.com/watch?v=6rICMl_QaQs), 37 s).
- «Giorno Giovanna tiene sueño (Oh, me duermo)» de MrpoopJPG
  ([YouTube](https://www.youtube.com/watch?v=qJnYsgjxx10), 21 s): un
  juego de palabras perfecto con «tengo un sueño».
- Ojo: ya circulan «doblajes latinos **con IA**» (p. ej.
  [este](https://www.youtube.com/watch?v=Kr-vJ0N1WIw)). **No usarlos**
  de referencia de voz.

---

## 11 · Música

### 11.1 Openings (verificados en [JoJo Wiki: Music](https://jojowiki.com/Music)) ✅

| Parte | Opening | Artista | Ambiente |
|---|---|---|---|
| PB | «JoJo ~Sono Chi no Sadame~» | Hiroaki «TOMMY» Tominaga | Épico, gritado, de anime clásico |
| BT | «BLOODY STREAM» | Coda | Elegante, con violines y baile |
| SC | «STAND PROUD» | Jin Hashimoto | Rock de viaje |
| SC Egipto | «JoJo ~Sono Chi no Kioku ~end of THE WORLD~» | JO☆STARS | Fin del mundo, coros |
| DU | «Crazy Noisy Bizarre Town» | THE DU | **Pop de pueblo**, colores de cómic (F173, F302) |
| DU | «chase» | batta | Misterio, persecución |
| DU | «Great Days» | Karen Aoki y Daisuke Hasegawa | Fiesta final |
| GW | «Fighting Gold» | Coda | Mafia dorada |
| GW | «Uragirimono no Requiem» | Daisuke Hasegawa | Oscuro, traición |
| SO | «STONE OCEAN» | ichigo (Kishida Kyoudan & The Akeboshi Rockets) | Rock de cárcel |
| SO | «heaven's falling down» | sana | Balada tensa |
| **SBR** | **«SPIN»** | **Kroi** | Funk; **se estrena en el ep. 2 (25-sep-2026)**; salió como single el 24-sep-2026 ✅ ([JoJo Wiki: Music](https://jojowiki.com/Music); [Final Weapon, 23-sep-2026](https://finalweapon.net/2026/09/23/jojos-bizarre-adventure-steel-ball-run-anime-opening-theme-song-artist/)) |

### 11.2 Endings: canciones occidentales ✅

| Parte | Ending | Artista |
|---|---|---|
| PB y BT (eps. 1-25), y el final de SO | **«Roundabout»** (1971) | **Yes** |
| SC | «Walk Like an Egyptian» | The Bangles |
| SC Egipto | «Last Train Home» | Pat Metheny Group |
| DU | «I Want You» | Savage Garden |
| GW | «Freek'n You» | Jodeci |
| GW (2.ª mitad) | «Modern Crusaders» | Enigma |
| SO | «Distant Dreamer» | Duffy |
| SBR ep. 1 | «Dance with STEEL BALL RUN» | Daisuke Hasegawa (música de Yugo Kanno) |

- **«Roundabout»**: 133 BPM, mi menor; en PB, el ending es un **mural
  azteca** por el que corre sangre hasta la máscara ✅
  ([JoJo Wiki: Roundabout](https://jojowiki.com/Roundabout)).
- **El meme usa la entrada acústica** de «Roundabout»: la imagen se
  congela **justo cuando entra el bajo** (en la herramienta de fans, el
  golpe está a 44,944 s del archivo de audio que usa) ✅.

- **Visto de verdad (segunda pasada)**: el ending sincronizado de
  [Dailymotion x3j25ta](https://www.dailymotion.com/video/x3j25ta)
  (3:04, 512×288), mirado con `fotogramas.py --cada 8`. De **0:00 a
  0:48** el muro azteca con una **línea roja** que corre por los
  relieves como una serpiente ✅. A **0:56** la cartela de créditos
  **«ROUNDABOUT · Jon Anderson / Steve Howe · YES»** ✅. A **1:12** una
  máscara pálida entre zarcillos verdes; de **1:28 a 1:36** **dos
  máscaras de piedra** (una dorada, otra con manchas violeta), no una
  sola. A **2:40** Joseph joven con sombrero ✅.
- **«SPIN»** de Kroi (OP de Steel Ball Run): se estrenó el 25-sep-2026;
  aún no hay clip oficial en plataformas abiertas (Dailymotion, Internet
  Archive) ⚠️.

### 11.3 Temas de la banda sonora

- **«il vento d'oro»** (GW): «el tema de Giorno». Compuesto por **Yugo
  Kanno**, cantado por Daisuke Hasegawa; 4:53; 135 BPM; si mayor ✅
  ([JoJo Wiki](https://jojowiki.com/Il_vento_d%27oro)). Suena cuando
  Giorno **gana**: «GioGio, Golden Wind». Meme de «**momento de
  victoria**».
- **«Awaken»** (BT): el tema de los **Hombres del Pilar**; compositores
  de PB y BT: **Hayato Matsuo** y **Taku Iwasaki** ✅ (JoJo Wiki:
  Music). El meme «Pillar Men theme» ⚠️ (de memoria; muy conocido).
- **Yugo Kanno** compone desde SC hasta SBR ✅.

---

## 12 · Vídeos (con minuto)

Metadatos sacados con `yt-dlp` (título, duración, fecha, canal). **Los
minutos dentro de los vídeos de YouTube no los pude medir** (YouTube
pedía iniciar sesión para ver capítulos); los minutos de escenas están
en §2, por subtítulo.

### 12.1 Oficiales

| Vídeo | Canal | Fecha | Duración | Qué sirve |
|---|---|---|---|---|
| [STEEL BALL RUN · Tráiler oficial](https://www.youtube.com/watch?v=tZRpLrZgr6w) | Netflix Latinoamérica | 19 feb. 2026 | 2:10 | **Voces latinas** de Johnny y Gyro; 437.470 vistas |
| [STEEL BALL RUN 2.ª ETAPA · Tráiler oficial](https://www.youtube.com/watch?v=2X_wKgSshNQ) | Netflix Latinoamérica | 3 jul. 2026 | 2:04 | Anuncia los **11 episodios, uno cada viernes desde el 25 de septiembre** |
| [「スティール・ボール・ラン」2nd STAGE 予告編](https://www.youtube.com/watch?v=xDDXgfNgzGk) | Netflix Japan | 2026 | 1:58 | Versión japonesa |
| [OP de SBR (evento)](https://www.youtube.com/watch?v=83kNllZEOMA) | Warner Bros. Japan Anime | 2025 | 2:35 | |
| [10.º aniversario, PV](https://www.youtube.com/watch?v=NIPpt48JIeA) | Warner Bros. Japan Anime | 4 abr. 2022 | 1:02 | Todos los JoJo |
| [「9人の“ジョジョ”たち」](https://www.youtube.com/watch?v=-_kqphBRMRo) | Jump Channel (Shueisha) | — | 2:15 | Presenta a los 9 JoJo |
| [OP de la serie de 2012](https://www.youtube.com/watch?v=BW4H15rK6iI) | Warner Bros. Japan Anime | — | 1:33 | |
| [Stone Ocean · nuevo OP](https://www.youtube.com/watch?v=RTacFlYONhY) | Warner Bros. Japan Anime | — | 1:31 | El OP en 3D de Kamikaze Douga |
| [Stone Ocean · Tráiler oficial](https://www.youtube.com/watch?v=EeCX8Y0a278) | Netflix | 2021 | 2:17 | |

**Vídeos mirados fotograma a fotograma (segunda pasada, 25-sep-2026).**
YouTube pidió iniciar sesión desde el servidor, así que se usaron copias
en Internet Archive y Dailymotion con `fotogramas.py` ✅:

| Vídeo | Dónde | Duración · resolución | Qué se ve, con minuto |
|---|---|---|---|
| OP1 «Sono Chi no Sadame» | [Internet Archive](https://archive.org/details/jojo-no-kimyou-na-bouken-op-1) | 1:31 · 1920×1080 | **0:04** Jonathan flexiona los brazos con líneas de velocidad verdes · **0:08** título ジョジョの奇妙な冒険 en rosa sobre negro · **0:12-0:16** viñeta de manga en blanco y negro, encuadre torcido · **0:24** Erina con atardecer naranja · **0:40** mano de Jonathan alzada hacia una luz blanca, anillos dorados · **0:44** puño en fuego naranja · **1:04-1:08** aura rosa y verde |
| Ending «Roundabout» (1 y 2) | [Dailymotion x3j25ta](https://www.dailymotion.com/video/x3j25ta) | 3:04 · 512×288 | Ver §11.2 |
| Tráiler de *All-Star Battle R* (2022) | [Dailymotion x8x1bgw](https://www.dailymotion.com/video/x8x1bgw), canal Level Up | 4:11 · 512×288 | **0:00-0:20** desierto de SBR con cinco jinetes · **0:30** HUD «SECRET FACTOR +2» · **0:40** «THE WORLD!» sobre una esfera azul · **0:50** ojos rojos de Dio en la oscuridad · **1:20** Jotaro en contrapicado, gorra negra con insignia dorada, cadena · **1:40-1:50** menú de Battle Tendency con cielo crema |
| Avance TV de DU ep. 33 | [Dailymotion x5mk7ho](https://www.dailymotion.com/video/x5mk7ho) | 0:15 · 512×288 | **0:00-0:01** Josuke de perfil con aura violeta y cielo dorado · **0:04-0:05** Yukako · **0:07** Crazy Diamond · **0:10-0:15** el sobre en el coche |
| Avance TV de DU ep. 36 | [Dailymotion x547qml](https://www.dailymotion.com/video/x547qml) | 0:15 · 512×288 | **0:00-0:03** Aya Tsuji llorando · **0:04-0:06** primer plano de Killer Queen con el detonador de Bites the Dust · **0:12-0:14** Killer Queen entre humo rojo |
| OP2 «BLOODY STREAM» | [Internet Archive](https://archive.org/details/jojo-no-kimyou-na-bouken-op-2) | 1:31 · 1920×1080 | Bajado, no analizado ⚠️ |
| Tráiler de SBR (Netflix LATAM) | [YouTube](https://www.youtube.com/watch?v=tZRpLrZgr6w) | 2:10 | `yt-dlp` se colgó; sin minutos internos ⚠️ |

AnimeThemes siguió caído (error 522 en `/anime` y en `/search`) ⚠️.

### 12.2 Recopilaciones y análisis

| Vídeo | Canal | Duración | Qué sirve |
|---|---|---|---|
| [Every JoJo's Episode Endings, Part 1-6](https://www.youtube.com/watch?v=FkXxlaYDUjY) | Spenify (17 mar. 2023) | 23:45 | **Todas las flechas TBC** seguidas: para ver el filtro de cada parte |
| [JoJo's To Be Continued Compilation](https://www.youtube.com/watch?v=RlGCjGymYNI) | Pitzocchero | 2:27 | El meme en su forma de internet |
| [Roundabout · pantalla verde](https://www.youtube.com/watch?v=bLGHyr4U11c) | — | — | Plantilla del meme (no oficial) |
| [JoJo's Bizarre Adventure is More than Just Memes](https://www.youtube.com/watch?v=dn6bNN6YsMk) | Benjuhmin | 7:03 | Por qué la serie genera memes |
| [The Genius Of JoJo's Bizarre Adventure](https://www.youtube.com/watch?v=jKwL5Q7mtno) | AlexEnterprises | 17:00 | Análisis |
| [JoJo's DOBLAJE LATINO en NETFLIX · todas las voces](https://www.youtube.com/watch?v=9TUwHvrPkJQ) | Nahu | 9:34 | Oír a cada actor latino |
| [Las voces detrás de JoJo (doblaje latino) · Voces que dan vida](https://www.youtube.com/watch?v=j29DsyAxJ54) | — | — | Ídem |
| [El Chavo del JoJo (español latino)](https://www.youtube.com/watch?v=AgzVliP-96Y) | Julio di esto | 1:20 | **Meme latino**: JoJo mezclado con *El Chavo* |
| [Técnica secreta Joestar en español latino](https://www.youtube.com/watch?v=o4vBtglR4HU) | Jgamer | 0:40 | Nigerundayo latino |

### 12.3 TikTok (búsquedas con resultados) ⚠️

Existen páginas de búsqueda de TikTok muy usadas: «[jojos español
latino](https://www.tiktok.com/discover/jojos-espa%C3%B1ol-latino)»,
«[to be continued jojo meme overlay](https://www.tiktok.com/discover/to-be-continued-jojo-meme-overlay)»,
«[Roundabout jojo meme](https://www.tiktok.com/discover/roundabout-jojo-meme)»
y «[voz de Kira Yoshikage español latino](https://www.tiktok.com/discover/voz-de-kira-yoshikage-espa%C3%B1ol-latino)».
No pude ver los vídeos ni sus minutos.

---

## 13 · Videojuegos de la franquicia

| Juego | Año | Qué tiene de útil |
|---|---|---|
| *JoJo's Venture* / *Heritage for the Future* (Capcom) | 1998 / 1999 | Lucha 2D; **flecha TBC al ganar**, naranja (W25) ✅ |
| *GioGio's Bizarre Adventure* (Capcom, PS2) | 2002 | Cel-shading; flecha TBC al acabar cada fase; letrero «再起不能» (W24) ✅ |
| *Phantom Blood* (Bandai, PS2) | 2006 | **Caja de diálogo blanca con borde de papel rasgado + retrato** y escenas en **viñetas de manga** (F82-F116) ✅ |
| *All Star Battle* / *All Star Battle R* | 2013 / 2022 | Onomatopeyas enormes en pantalla; retratos oficiales (F2-F5); flecha TBC al final del modo historia de JoJolion ✅ (JoJo Wiki) |
| *Eyes of Heaven* | 2015 | Cel-shading; «OH MY GOD» de Joseph viejo (F298) |
| *Last Survivor* (arcade) | 2019 | La flecha TBC **del anime** al caer el último (W15) ✅ |
| *Ora Ora Overdrive* («OraDora», gumi, móvil) | 25 sep. 2025 | RPG táctico con los personajes de las partes 1-6; cumple **un año mañana** ⚠️ una fuente ([JoJo Wiki](https://jojowiki.com/Ora_Ora_Overdrive); [web](https://jojo-oradora.com/)) |
| Mods: *JoJoStands* (Terraria), *JoJo's Bizarre Survival* (Minecraft) | — | Los fans **juegan a tener un Stand** ✅ ([GitHub](https://github.com/AnotherGuy7/JoJoStands)) |

- **La caja de diálogo del juego de PS2** (*Phantom Blood*, F82-F116)
  es la mejor referencia de **«cuadro de diálogo de videojuego de
  JoJo»**: blanca, con **borde irregular como papel roto**, el
  **retrato** del que habla en una esquina y **letras japonesas** en
  negro. Sirve si una lámina quiere **un cuadro que no sea la flecha**.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todos reconocen

| Meme | De dónde | Estado |
|---|---|---|
| **«To Be Continued» + «Roundabout»** | Final de episodio de 2012; meme en Vine desde **enero de 2016** (el primer remix fechado, 27 ene. 2016, según Know Your Meme) | ✅ [JoJo Wiki](https://jojowiki.com/To_Be_Continued) · [Gizmodo](https://gizmodo.com/to-be-continued-is-the-sleeper-meme-hit-of-the-summer-1781860391) · [KYM](https://knowyourmeme.com/memes/yes-roundabout-to-be-continued) |
| **«¿Eso es una referencia a JoJo?»** | Nació en **4chan /a/ en 2009**, se hizo famoso en Reddit; se dice ante cualquier pose o kanji | ✅ [TheGamer](https://www.thegamer.com/jojo-reference-meme-origin/) · [KYM](https://knowyourmeme.com/memes/is-this-a-jojo-reference) |
| **La pose JoJo** (ジョジョ立ち, *JoJo-dachi*) | El término entró en el **diccionario de palabras nuevas de Japón en 2005**; hubo **más de 500 fans posando ante el castillo de Osaka** y una «escuela de poses» en la Universidad de Tokio | ✅ [JoJo Wiki: JoJo Pose](https://jojowiki.com/JoJo_Pose) |
| **ゴゴゴゴ «Menacing»** | La onomatopeya de tensión; Araki la sacó del **cine de suspense** | ✅ [portal oficial](https://jojo-portal.com/special/production-note/02/) · [JoJo Wiki: Sound Effects](https://jojowiki.com/Sound_Effects) |
| **ZA WARUDO / ROAD ROLLER DA** | SC eps. 46-48 | ✅ (§2) |
| **«¡Fue este Dio!»** | PB ep. 1 | ✅ (§2) |
| **Nigerundayo / «tu siguiente frase»** | BT | ✅ (§2) |
| **«Yare yare daze»** | SC en adelante | ✅ (§2) |
| **El monólogo de Kira** | DU ep. 21 | ✅ (§2) |
| **«…pero me niego»** | DU ep. 28 | ✅ (§2) |
| **«Tengo un sueño» + Il vento d'oro** | GW ep. 5 | ✅ (§2) |
| **Números primos de Pucci** | SO ep. 12 | ✅ (§2) |
| **El compañero de trabajo de Kira** | Un extra de DU que los fans japoneses adoran: quedó **25.º en una encuesta no oficial**, por encima de Avdol | ⚠️ una fuente: [JoJo Wiki: Kira's Coworker](https://jojowiki.com/Kira%27s_Coworker), que cita un vídeo |

**Lo nuevo (septiembre de 2026)**:

- **Steel Ball Run** domina r/ShitPostCrusaders (el subreddit de memes
  de JoJo): lo más votado del verano es del tráiler y de «escenas
  filtradas del ep. 2» ✅ (Reddit vía
  [Arctic Shift](https://arctic-shift.photon-reddit.com), p. ej.
  [este post, 1.266 votos](https://reddit.com/r/ShitPostCrusaders/comments/1umv19p/steel_ball_run_trailer_but_only_the_parts_where_a/),
  4-jul-2026; [«Leaked Scene from SBR Episode 2»](https://reddit.com/r/ShitPostCrusaders/comments/1wa1g7l/leaked_scene_from_steel_ball_run_episode_2/),
  7-sep-2026).
- En Pixiv, **Diavolo atrapado en el bucle de *El pasillo 8***
  ([148995246](https://www.pixiv.net/artworks/148995246)) ✅.
- **Mañana (25-sep-2026)** sale el ep. 2 de SBR con el opening «SPIN» de
  Kroi: el canal va a ver memes nuevos de Gyro y Johnny.
- En el doblaje latino hay **chistes mexicanos metidos** («Ya siéntese,
  señora», «¿Ya estamos al aire? Avísenme») ⚠️ (§10.3).

### 14.2 Qué NO hacer (lo que un fan notaría)

- **La flecha al revés** (apuntando a la derecha) o **centrada**.
- **El sepia de plantilla** para todo: el anime usa el filtro de **su
  parte** (§3.3).
- Llamar **«Za Warudo»** al Stand de Jotaro: ese es **The World**, de
  Dio. Star Platinum **también para el tiempo** («Star Platinum: The
  World»), pero no se llama así a secas.
- Poner a **Jotaro sonriendo** abiertamente o **corriendo**: casi nunca
  lo hace (Eastwood no corre) ✅.
- Mezclar **ropas de partes distintas** (Jotaro de blanco con la cadena
  dorada de SC, Joseph joven con el sombrero de viejo).
- Escribir **«Joestar» con «JoJo» mal**: «JoJo» con la segunda J
  mayúscula.
- **Giorno sin sus tres rizos**, **Josuke sin tupé**, **Jolyne sin los
  dos moños**: son la silueta.
- Traducir los **nombres de Stand** (son nombres de canciones:
  Killer Queen, Sticky Fingers, Stone Free).
- Usar una voz **hecha con IA** como si fuera el doblaje (§10.3).

---

## 15 · Poses analizadas por personaje

F = índice de Fandom (hojas de `herramientas/referencias/…` y copias en
`hojas/`). Lo que describo lo **vi en la imagen** ✅; la escena exacta
de algunas, ⚠️.

### Jotaro

| # | Imagen | Postura | Manos | Mirada | Sirve para |
|---|---|---|---|---|---|
| 1 | F5 (ASB, 3750×5000) | De pie, **señalando al frente** con el brazo derecho estirado; abrigo abierto al viento | Índice extendido; la otra mano atrás | Al frente, dura | **Presentar / regañar** |
| 2 | F173 (OP DU) | Medio cuerpo, **ajustándose la visera** | Dos dedos en la visera | Por debajo de la gorra | **Presentar** con estilo |
| 3 | F190 (SC, cartela de Stand) | Medio cuerpo, con la **carta THE STAR**; Star Platinum detrás | Carta en la mano | De reojo | **Presentar** (ficha) |
| 4 | F187 (SC ep. 1, celda) | **Sentado** en la cama de la celda, rodillas abiertas, ドォォーン encima | Brazos sobre las rodillas | Al suelo | **Pensar** / «yare yare» |
| 5 | F184 (DU, «shut up») | Gritando de perfil, abrigo blanco | — | Furiosa | **Regañar** |
| 6 | F212 (juego, DU) | Primer plano torcido, apretando dientes | Puño | Al espectador | **Animar** (a pelear) |
| 7 | F216 (SC ep. 48) | Sólo el pecho: **sostiene la foto instantánea** del grupo | Dos dedos en la foto | — | **Explicar** («esto va aquí») |
| 8 | F183 (cuenta atrás DU) | De pie, de blanco, con un libro, junto a Koichi | Libro abierto | Al frente | **Explicar** |

### Dio

| # | Imagen | Postura | Sirve para |
|---|---|---|---|
| 1 | F239 («high as hell») | **Dedo en la sien**, sonrisa enorme | **Celebrar** / burlarse |
| 2 | F237 (WRYYY) | Gritando al cielo con The World delante | **Celebrar** a lo bestia |
| 3 | F238 (flashback) | **Pose imposible**, de espaldas, brazo arriba, luna roja | **Presentar** |
| 4 | F242 | En la azotea de **El Cairo** con capa, de noche | Fondo de amenaza |
| 5 | F241 · F715 | **Encima de la apisonadora**, brazos abiertos | **Celebrar** (el meme) |
| 6 | F234 | (sólo su mano) rompiendo **la cámara** con Hermit Purple | **Explicar** («así se hace una foto») |

### Joseph

| # | Imagen | Postura | Sirve para |
|---|---|---|---|
| 1 | F298 (Eyes of Heaven) | **Manos a la cabeza**, ojos fuera: «OH MY GOD» | **Reaccionar** a un meme |
| 2 | F285 (DU) | **Mano en la oreja**: «¿qué?» | **Explicar** («¿lo doblas? ¿cómo?») |
| 3 | F280 (SC) | Con el **walkman** y los cascos | Relajado |
| 4 | F278 (SC) | Con la carta **THE HERMIT** y Hermit Purple en la mano | **Presentar** |
| 5 | F64 (arte de Araki, 1955×2289) · F51 (con moto, 2161×3064) | Joven de BT: **mano en la cara** con los dedos abiertos (F64); **mano en la cabeza** junto a su moto (F51) | **Pensar** («tu siguiente frase será…») |

### Giorno

| # | Imagen | Postura | Sirve para |
|---|---|---|---|
| 1 | F431 (OP de 2012) | **Mano abierta en el pecho**, sobre página de manga | **Presentar** («tengo un sueño») |
| 2 | F726 | De pie, **mano en la cintura**, cadera ladeada | Explicar con calma |
| 3 | F415 | Primer plano de los **ojos**, sangre en la cara | Amenaza / MUDA |
| 4 | F6 (cuenta atrás) | Con Gold Experience Requiem detrás | Celebrar |

### Josuke

| # | Imagen | Postura | Sirve para |
|---|---|---|---|
| 1 | F302 (OP) | **Peinándose el tupé** con peine | **Presentar** |
| 2 | F315 | Pose final: **dos dedos levantados junto a la cara**, la otra mano en el cinturón, cuerpo inclinado; calle de Morioh, cielo amarillo | **Presentar** |
| 3 | F320 | En **cuclillas**, brazos sobre las rodillas | Pensar / explicar |
| 4 | F398 | Aura rosa: **se enfada** porque Rohan se burla del pelo | **Regañar** |
| 5 | F318 | Varios Josuke en fila (OP «Great Days») | Celebrar |

### Rohan

| # | Imagen | Postura | Sirve para |
|---|---|---|---|
| 1 | F3 (ASB, 4000×5318) | Pose JoJo: **brazo derecho sobre la cabeza**, mano en la nuca, piernas cruzadas, cadera ladeada | **Presentar** (pose de modelo) |
| 2 | F492 | **Leyendo la cara-libro** de Koichi, con calma | **Explicar** |
| 3 | F494 | **Arrancando una página** con una sonrisa | Regañar (en broma) |
| 4 | F484 | Primer plano de lado, ojo entornado | «…pero me niego» |
| 5 | F450 | Herido, **dibujando** sin parar | Animar («sigue creando») |
| 6 | F457 | Cara con manchas de tinta, gritando | Celebrar a lo loco |

### Bucciarati

| # | Imagen | Postura | Sirve para |
|---|---|---|---|
| 1 | F458 | **Mano en la cara**, luz de atardecer | «Arrivederci» (despedida) |
| 2 | F467 | Delante de su banda, explicando | **Explicar** |
| 3 | F7 (cuenta atrás) | Con Sticky Fingers detrás | Presentar |

---

### Poses de vídeo real (segunda pasada)

Salen de mirar los vídeos de §12.1, con minuto. Se suman a las de
arriba (que usan hojas F-n, en más resolución).

| Personaje | Vídeo | Minuto | Postura, manos, mirada | Sirve para |
|---|---|---|---|---|
| Jonathan | [OP1, Internet Archive](https://archive.org/details/jojo-no-kimyou-na-bouken-op-1) | 0:40 | Mano derecha alzada a una luz blanca, anillos dorados, guantelete oscuro | **Animar** |
| Joseph joven | [Ending, Dailymotion](https://www.dailymotion.com/video/x3j25ta) | 2:40 | Sombrero, mano junto a la barbilla, sonrisa de lado, de perfil | **Pensar, explicar** con ironía |
| Jotaro | [Tráiler ASBR](https://www.dailymotion.com/video/x8x1bgw) | 1:20 | Contrapicado, de pie, mirada fija al frente, gabardina abierta, cadena al hombro | **Presentar, amenazar** |
| Josuke | [Avance DU ep. 33](https://www.dailymotion.com/video/x5mk7ho) | 0:00-0:01 | De perfil, aura violeta, manos en el cinturón, cadera ladeada | **Presentar** |
| Killer Queen (Kira) | [Avance DU ep. 36](https://www.dailymotion.com/video/x547qml) | 0:04 | Primer plano, ojos rojos, puño con el disco dorado | **Amenazar, regañar** |

## 16 · Vestuario ⚠️ (visto en las hojas; colores a ojo)

| Personaje | Ropa icónica | Detalles que no pueden faltar |
|---|---|---|
| **Jotaro (SC)** | **Gakuran negro largo** abierto, cuello alto, **gorra** que se funde con el pelo | **Cadena dorada** al cuello del abrigo; insignias en la gorra y el cuello |
| **Jotaro (DU)** | Abrigo **blanco** largo, camisa verde agua | Gorra blanca con la **insignia «JO»** |
| **Dio (PB)** | Traje victoriano | Pelo rubio largo |
| **DIO (SC)** | Chaqueta amarilla corta, **pantalón verde**, torso a la vista | **Corazones en las rodillas/botas**, diadema |
| **Joseph (SC)** | Pantalón claro, camisa, **sombrero de fieltro** | Guante (mano de metal); walkman |
| **Josuke** | Gakuran **azul marino** ajustado | **Corazones dorados** y **símbolo de la paz** en el cuello; **tupé** |
| **Giorno** | Traje **rosa-fucsia** con escote en forma de **corazón** | **Tres rizos**; **mariquitas** doradas en el pecho |
| **Rohan** | Chaqueta verde, top corto | **Cinta verde** en el pelo, **pendientes de plumilla** |
| **Bucciarati** | Traje **blanco con lunares negros** y **cremalleras** | Flequillo recto, horquillas doradas |
| **Kira** | Traje **violeta**, corbata con **calaveras** | Pelo gris claro |
| **Jolyne** | Traje verde lima y azul con aberturas | **Dos moños**, **tatuaje de mariposa**, trenza |

**Los colores de cada parte**, sacados de los **fondos de pantalla
oficiales** (§17) ✅ (medidos al píxel, ±8):

| Parte | Color principal | Franja de acento |
|---|---|---|
| PB | lavanda `#B8A0D0` | violeta `#882090` |
| BT | violeta `#882090` | lima `#C0E000` |
| SC | **lima `#C0E000`** | rosa `#F848A0` |
| DU | **rosa `#F848A0`** | naranja `#F0A808` |
| GW | **naranja `#F0A808`** | lavanda `#B8A0D0` |

(Cada parte **pasa el color a la siguiente**: la franja de acento es el
color principal de la parte que viene.)

---

## 17 · Paisajes y fondos de pantalla

### 17.1 Los sitios, con su luz ⚠️ (de los fotogramas de §5)

| Sitio | Hora y luz |
|---|---|
| Morioh | **Tarde, cielo amarillo mostaza**, sombras violeta (F315) |
| El Cairo | **Noche**, luces doradas de la ciudad abajo (F242) |
| La celda | Luz fría gris azulada, sin sol (F187) |
| Nápoles | **Mediodía** claro, piedra crema (F418); **atardecer naranja** (F458) |
| Green Dolphin (SO) | Verde agua y azul noche (W11) |
| Oeste americano (SBR) | **Sol de desierto**, sepia verdoso (W12) |

### 17.2 Fondos de pantalla oficiales (medidos) ✅

Del [portal oficial, campaña de contenidos digitales](https://jojo-portal.com/special/digital-contents/)
(2021): cada JoJo en una franja vertical, **fondo negro con diagonales
de color** y el logo «JOJO THE ANIMATION» abajo a la derecha.

| Parte | PC (1920×1080) | Móvil (1080×2160) |
|---|---|---|
| PB · Jonathan | [PC](https://jojo-portal.com/special/digital-contents/assets/images/common/wallpaper_pc_phantom-blood.jpg) | [móvil](https://jojo-portal.com/special/digital-contents/assets/images/common/wallpaper_sp_phantom-blood.jpg) |
| BT · Joseph | [PC](https://jojo-portal.com/special/digital-contents/assets/images/common/wallpaper_pc_battle-tendency.jpg) | [móvil](https://jojo-portal.com/special/digital-contents/assets/images/common/wallpaper_sp_battle-tendency.jpg) |
| SC · Jotaro | [PC](https://jojo-portal.com/special/digital-contents/assets/images/common/wallpaper_pc_stardust-crusaders.jpg) | [móvil](https://jojo-portal.com/special/digital-contents/assets/images/common/wallpaper_sp_stardust-crusaders.jpg) |
| DU · Josuke | [PC](https://jojo-portal.com/special/digital-contents/assets/images/common/wallpaper_pc_diamond-is-unbreakable.jpg) | [móvil](https://jojo-portal.com/special/digital-contents/assets/images/common/wallpaper_sp_diamond-is-unbreakable.jpg) |
| GW · Giorno | [PC](https://jojo-portal.com/special/digital-contents/assets/images/common/wallpaper_pc_golden-wind.jpg) | [móvil](https://jojo-portal.com/special/digital-contents/assets/images/common/wallpaper_sp_golden-wind.jpg) |

- El anuncio oficial en X: [@anime_jojo](https://x.com/anime_jojo/status/1355078246447022080) ✅.
- **Fondos de fans**: hay webs de fondos japonesas
  ([kabekin](https://kabekin.com/tags/jojowp),
  [sumakabe](http://sumakabe.com/anime/jojo.html)) ⚠️ sin autor claro:
  **no usar**.

---

## 18 · Guía para generar con IA (Firefly, Canva)

> [!warning] Antes de empezar
> Firefly y Canva **suelen rechazar nombres de personajes con derechos**
> («Jotaro», «JoJo»). Hay que **describir sin nombrar**. Y la IA **no
> sustituye** a los recortes oficiales: úsala para **fondos, objetos y
> luz**, y deja a los personajes con imágenes reales (F2-F5, F190…)
> pasadas por `v3/integrar.py`.

### 18.1 Rasgos que nunca cambian

| Personaje | Siempre |
|---|---|
| Jotaro | Gorra que se funde con el pelo, gakuran negro largo con **cadena dorada** (SC) o abrigo blanco (DU); ojos verde azulado; mandíbula cuadrada; **no sonríe** |
| Dio | Rubio, **corazones** en la ropa (SC), torso a la vista, labios oscuros, pose imposible |
| Joseph viejo | Sombrero de fieltro, barba blanca corta, **guantes** |
| Giorno | **Tres rizos** en la frente, traje rosa con escote de corazón, **mariquitas** doradas |
| Josuke | **Tupé** enorme, gakuran azul marino con **corazones** y **símbolo de la paz** dorados |
| Rohan | **Cinta verde** en el pelo, **pendientes de plumilla** |

### 18.2 Estilo

- **Línea**: tinta **gruesa y negra**, con **rayado cruzado** en las
  sombras de la cara y el cuello (F10-F12).
- **Sombreado**: *cel shading* de dos tonos, sombras duras, **mucho
  negro**.
- **Color**: planos, saturados, y **cambian por escena** (verde, violeta
  o rosa en la piel sin que sea error; §5.2).
- **Poses**: de **modelo de moda**, torso girado, caderas fuera, manos
  abiertas (§14, JoJo Pose).
- **Encuadre**: contrapicado, escorzo fuerte, líneas de velocidad.
- **Texto en la imagen**: katakana enorme (ゴゴゴ, ドドド) **dibujado** en
  perspectiva.

### 18.3 Plantilla de texto para la IA (en inglés, que la entiende mejor)

> *1980s Japanese shonen manga style, thick black ink outlines,
> cross-hatching shadows on face and neck, flat saturated cel-shading,
> surreal color palette shift (magenta and lime), dramatic low angle,
> fashion-model pose with twisted torso, a tall young man in a long black
> school uniform coat with a gold chain on the collar and a cap merging
> into his hair, giant katakana sound effects floating in the air,
> freeze-frame with a vintage color filter.*

**Palabras que ayudan**: *thick ink outlines, cross-hatching, cel
shading, surreal palette, dramatic foreshortening, fashion pose, bold
black shadows, manga screentone, freeze-frame, sepia duotone,
magenta-violet duotone.*

**Palabras que lo estropean**: *chibi, kawaii, pastel, soft shading,
Pixar, 3D render, photorealistic, moe, watercolor, neon cyberpunk*
(ni *JoJo*, *Jotaro*, *Araki*: los rechaza o copia mal).

### 18.4 Para los fondos y objetos (lo que sí conviene generar)

| Qué | Descripción para la IA | Referencia de estilo |
|---|---|---|
| Hotel en El Cairo, de noche | *1980s Cairo hotel room at night, warm lamp, wooden table, window with city lights, ochre and black palette* | F242 |
| Estudio de mangaka | *Japanese manga artist desk 1999, drafting table, ink bottles, dip pens, manuscript pages, afternoon light, cream and lilac palette* | F492, F450 |
| Calle de Cairo con apisonadora | *night street in Cairo, 1989, stone buildings, road roller in the middle, golden city lights, red-violet duotone* | F241, F242, W7 |
| Morioh | *Japanese suburban street 1999, mustard yellow sky, violet shadows* | F315 |

### 18.5 Qué imágenes usar de referencia

- **Estilo de color y línea**: F10-F12 (hojas de modelo), F173 y F302
  (pop de DU), W16-W21 (fichas).
- **Pose**: F5 (Jotaro señala), F298 (Joseph «OH MY GOD»), F239 (Dio
  dedo en la sien), F431 (Giorno), F3 y F492 (Rohan).
- **Filtro del fotograma congelado**: W5 (sepia SC), W7 (rojo-violeta
  SC 47), W8 (magenta DU), W10 (verde agua GW), W12 (SBR).

### 18.6 Colores y técnica que la IA debe respetar (segunda pasada)

- **Hex medidos** (§5.3) para escribir en el prompt: abrigo de Jotaro
  `#163F58`, oro de Dio `#BA963C`, fucsia de Giorno `#BD7DAD`, violeta de
  Kira `#3C3A50`, verde de Rohan `#718F71`, crema de Bucciarati `#F4E6D3`,
  oliva lima de Jolyne `#B7B338` ✅.
- **Gorra de Jotaro en SC**: *black cap with a gold badge*, nunca blanca
  (blanca sólo en DU) ✅.
- **Color como Araki** (§Punto 18): planos grandes estilo *ukiyo-e*,
  complementarios en luz y sombra, **azul claro + rosa** como combinación
  favorita (Golden Wind) ✅. Palabras que ayudan: *flat ukiyo-e color
  areas, complementary shadows, light blue and pink scheme, sepia
  underpainting*.
- **Referencia de pose 3D real**: figuras Medicos *Super Action Statue*
  (colores aprobados por Araki, §Punto 23), no fan renders.

### 18.7 Para una IA de texto: cómo escribir en su voz

**Reglas de la voz de JoJo** (§7.2 y §10.3):

- **Frases cortas y rotundas**, con una muletilla por personaje:
  «Ay, por favor» (Jotaro, doblaje latino), «¡Great!» (Josuke),
  «…pero me niego» (Rohan), «¡Inútil, inútil!» (Dio, Giorno).
- **Se presentan en tercera persona** con nombre completo: «Este Giorno
  Giovanna tiene un sueño».
- **Gritos con letras estiradas y ¡!** : «¿Qué dijiste de mi peeelo?»,
  «¡ROAD ROLLER DAAA!». Las ráfagas se escriben repetidas y en
  mayúsculas: «¡ORA ORA ORA!», «¡MUDA MUDA MUDA!» (se dejan en japonés,
  como el doblaje hace con ORA ORA).
- **Los villanos explican su plan con calma**; el héroe **adivina la
  frase del otro**: «Tu siguiente frase será…».
- **Nombres en inglés o italiano** para poderes y ataques (Killer Queen,
  Sticky Fingers, Arrivederci).
- **Onomatopeyas de tensión** en katakana, dibujadas, no escritas en
  globo: ゴゴゴゴ (gogogo), ドドド (dododo).
- **Qué evitar**: humor tierno, emojis, diminutivos, «jeje». JoJo exagera
  con dramatismo serio, no con ternura.

**Frases reales por emoción** (subtítulo japonés con minuto, §2.1;
traducción de la biblia salvo donde dice «doblaje»):

| Emoción | Frase | Quién · dónde |
|---|---|---|
| Alegre, eufórico | «¡Me siento en lo más ALTO!» (最高に ハイってやつだぁぁぁぁ！) | Dio · SC ep. 47, 00:23:34 ✅ |
| Alegre, burlón | «¡YES YES YES!… ¡OH MY GOD!» | Dio y Jotaro · SC ep. 42, 00:10:21 ✅ |
| Enfadado | «¿Qué dijiste de mi pelo?» (このヘアースタイルがサザエさんみてェーだとォ) | Josuke · DU ep. 1, 00:06:02 ✅ |
| Enfadado, frío | «Tu error fue uno solo… me hiciste enojar» | Jotaro · SC ep. 48, 00:14:47 ✅ |
| Explicando | «Voy a contar lo que acaba de pasar…» | Polnareff · SC ep. 45, 00:06:42 ✅ |
| Explicando, con calma | «Me llamo Yoshikage Kira. Tengo 33 años… siempre deseo la paz mental» | Kira · DU ep. 21, 00:20:25 ✅ |
| Animando | «Este Giorno Giovanna tiene un sueño» | Giorno · GW ep. 5, 00:22:49 ✅ |
| Animando, pícaro | «Tu siguiente frase será…» | Joseph · BT ep. 10, 00:16:19 ✅ |
| Triste | «Y Kars dejó de pensar» | narrador · BT ep. 26, 00:14:40 ✅ |
| Triste, a gritos | «¡Qué injusticia!» (あんまりだああ～), el llanto de Esidisi | BT ep. 16, 00:25:05 ✅ |
| Fastidio | «Ay, por favor» (doblaje latino de やれやれだぜ) | Jotaro · SC ep. 2, 00:02:19 ✅ |
| Negarse | «…pero me niego» (だが断る) | Rohan · DU ep. 28, 00:20:15 ✅ |

**Vocabulario de expresiones para la IA de imagen** (cada gesto):

- **Cara seria con sombra de rayado** en la frente y el cuello
  (*cross-hatched shadow over the eyes*): amenaza, decisión.
- **Ojos en blanco o pupila diminuta** (*shrunken pupils*): terror,
  shock; Joseph y Polnareff.
- **Gotas de sudor gruesas** en la sien (*heavy sweat drops*): apuro;
  Bucciarati lame el sudor en GW ep. 1, 00:21:23.
- **Fondo de color plano que cambia** (*sudden flat background color
  shift*): la emoción cambia el color de toda la escena (§5.2).
- **Katakana gigante** ゴゴゴ detrás (*menacing katakana aura*): tensión.
- **Pose JoJo** (*contorted fashion pose, twisted torso*): presentarse.
- **Chibi**: la serie **no** usa *chibi* ni caras deformadas tiernas;
  el humor sale de la exageración dramática. No pedirlo.

---

## 19 · Tres conceptos para la lámina de #memes

Los tres usan **un objeto real en un sitio real** de la serie, se pueden
hacer en **Blender**, y **ninguno lleva globo blanco**. Los textos son
los de §0.

### Concepto A — «La foto psíquica de Joseph» (Polaroid + To Be Continued)

**La idea**: en #memes se cuelgan **imágenes**. En la serie, Joseph
**saca imágenes con su Stand**: rompe una **cámara instantánea** con
Hermit Purple y sale **una foto psíquica** (F234 ✅). La foto que sale
es **el meme**, congelado, con la flecha To Be Continued.

- **La escena real** (SC ep. 1, 00:19:31 a 00:20:07 ✅): en la mesa
  de un **restaurante** (hasta viene un camarero: «¿Le pasa algo,
  señor?»), Joseph enseña su Stand: «Mi poder es **pasar a la película
  visiones de lugares lejanos: la foto psíquica** (念写)… ¡aunque cada
  vez tenga que **romper una cámara de 30.000 yenes**!». Y: «**La
  imagen que aparezca en esta foto decidirá tu destino**».
- **Objeto y sitio**: una **cámara Polaroid** (Blender; base libre de
  Boxroom 3D, CC BY, §4.1) **rota por el golpe**, sobre la **mesa de
  ese restaurante** (mantel, taza, luz de tarde) o, si se quiere más
  noche, un hotel de El Cairo. De la ranura sale **una foto
  instantánea** un poco curvada. **Zarzas violetas** de Hermit Purple (`#AF6788` y
  `#D8A8C5`, medidas en F234) rodean la cámara.
- **Personaje**: **Joseph viejo** (el rey de los memes, 1.º en el
  ranking de JoJos de 2021). Pose: **manos a la cabeza, «OH MY GOD»**
  (F298) si se quiere risa; o **mano en la oreja** (F285) si se quiere
  que «pregunte». Recorte limpio: hojas de modelo F29-F34 para la ropa.
- **Cómo habla**: **globo de manga japonés** (óvalo fino, trazo a mano,
  como en F431/F435), con la letra **Mali Bold** o rotulada a mano:
  - «¡**Tu siguiente frase será**: “¿y si lo doblo?”!»
  (su meme de BT ep. 10, 00:16:19 ✅).
  - Alternativa: «**Lo que salga en esta foto decidirá tu destino.**»
  (SC ep. 1, 00:20:04 ✅) como texto de narrador.
- **Dónde va cada texto**:
  1. **«Memes»** → escrito **a rotulador en el margen blanco de abajo
     de la Polaroid** (Caveat Brush o a mano), como se rotula una foto.
  2. **«El meme, sin más»** → **texto de narrador** blanco en mincho
     (Shippori Mincho B1) arriba a la izquierda, como W4.
  3. **«Si lo doblas, va a fandub-de-memes»** → **dentro de la flecha
     To Be Continued**, **abajo a la izquierda de la foto**, apuntando a
     la izquierda: la flecha **ya significa «sigue en otro sitio»**.
     Calcar la flecha de W3; el texto español en Caveat Brush,
     `#48483C` sobre `#B4C0A8`.
  4. Frase de Joseph → su globo.
- **La foto dentro de la Polaroid**: un fotograma congelado de la serie
  con el **filtro sepia de SC** (W5: `#180C0C`, `#3C3024`); mejor una
  escena-meme de §2 (Dio en la apisonadora, F241).
- **Cómo no queda plano**:
  - Zarzas **delante** de la cámara y cruzando el borde de la lámina.
  - Luz **cálida de lámpara** desde la derecha; la foto brilla un poco
    (película recién salida).
  - La cámara **desenfocada en primer plano**, la foto nítida.
  - **ゴゴゴ** violeta (Dela Gothic One) detrás de Joseph.

### Concepto B — «…pero me niego»: la ficha de Stand en la mesa de Rohan

**La idea**: el objeto del plan es **la ficha de Stand**. La hacemos
**página de manga** en la **mesa de dibujo de Rohan**: está dibujando
**la ficha del Stand «MEMES»**. Y la regla del canal la dice **con su
meme**: «**…pero me niego**» (だが断る, DU ep. 28, 00:20:19 ✅).

- **Objeto y sitio**: una **hoja de manuscrito** (papel de dibujo con
  la tinta siguiendo la curva del papel, en Blender) sobre la **mesa de
  la casa de Rohan en Morioh** (F492, F450), con plumillas, tintero y
  goma. Luz de tarde por la ventana (paleta `#E1D6BF`, `#A47C97`,
  `#92AD76`, medida en F492).
- **La ficha** (calcada de W16-W21, medidas en §3.1):
  - **[STAND NAME]** → **«MEMES»** (y en japonés, ミーム, mincho).
  - **[STAND MASTER]** → **«Tú»**.
  - El **reloj de seis notas**, con las etiquetas **en español** y la
    nota en grande:
    Poder destructivo **A** · Velocidad **A** · Alcance **A** ·
    Aguante **E** · Precisión **E** · Potencial **A**
    (es un chiste: un meme pega fuerte, corre rápido, llega a todos…
    y dura un día). El polígono, **magenta translúcido** como W16.
  - Hacer el polígono con [valkyrs/jojo-stands](https://github.com/valkyrs/jojo-stands) (MIT).
- **Personaje**: **Rohan** (el secundario favorito de muchos fans y el
  único con serie propia). Pose: **sentado de lado, pluma en la mano,
  mirando al espectador por encima del hombro** ⚠️ (componer desde F492
  y F450), o la pose oficial **brazo sobre la cabeza** (F3, 4000×5318,
  fondo blanco: recorte fácil).
- **Cómo habla**: **escrito con Heaven's Door**: la regla aparece
  **en páginas** que salen de una cara-libro o de la propia hoja (F476,
  F492), en columnas de texto negro sobre papel. Y su frase en globo de
  manga:
  - «¿Doblar el meme aquí? **…Pero me niego.** Eso va a
    fandub-de-memes.»
- **Dónde va cada texto**:
  1. **«Memes»** → [STAND NAME] en la ficha, arriba.
  2. **«El meme, sin más»** → la **línea de habilidad** del Stand, bajo
     el reloj («Habilidad: el meme, sin más»).
  3. **«Si lo doblas, va a fandub-de-memes»** → el **globo de Rohan**,
     o escrito como orden de Heaven's Door en una página que sobresale.
- **Letras**: [STAND NAME]/[STAND MASTER] en **EB Garamond** o **Cinzel**
  con bisel; etiquetas del reloj en **Zen Kaku Gothic New** Bold; japonés
  en **Shippori Mincho B1**; globo en **Mali Bold** o a mano.
- **Cómo no queda plano**:
  - **Plumillas y tintero en primer plano**, desenfocados.
  - La hoja **curvada** y con **una mancha de tinta** real.
  - Luz lateral de ventana que proyecta la sombra de la mano de Rohan
    sobre el papel.
  - La trama violeta de DU **sólo dentro de la ficha**, no en todo.

### Concepto C — «¡ROAD ROLLER DA!»: el fotograma congelado de Dio

**La idea**: el meme más famoso de Dio **ya es un fotograma congelado**.
La lámina es **ese momento, parado**, con el filtro rojo-violeta de SC
47-48 y la flecha. El texto va **pintado en la propia apisonadora**.

- **Objeto y sitio**: la **apisonadora** (Blender; base libre de Lassi
  Kaukonen, CC BY, §4.1) cayendo **en una calle de El Cairo de noche**
  (SC ep. 48, F241, F242). Como es de obra, lleva **placas de metal y
  letras pintadas**: ahí va la información.
- **Personaje**: **Dio** encima, **brazos abiertos**, gritando (F241,
  F715); o con el **dedo en la sien** (F239) si se prefiere burla.
- **Cómo habla**: sin globo. **Onomatopeya gigante** a mano en
  katakana, como en el manga: **「ロードローラーだッ!」** en **Dela
  Gothic One** o rotulada, y debajo, pequeño, en español: «¡Es una
  apisonadora!» (en latino, «**aplanadora**» ⚠️). Y **ドドドド** alrededor.
- **Dónde va cada texto**:
  1. **«Memes»** → **letras pintadas en el lateral del rodillo** (como
     la marca de la máquina), en Anton o Bungee, con desconchones.
  2. **«El meme, sin más»** → **placa de metal atornillada** en la
     cabina (como la placa de fabricante).
  3. **«Si lo doblas, va a fandub-de-memes»** → **flecha To Be
     Continued abajo a la izquierda** del fotograma (calcada de W3).
- **El filtro**: el de **SC ep. 47** (W7): duotono **rojo y violeta**.
  **No sepia plano**.
- **Cómo no queda plano**:
  - La apisonadora **en escorzo**, enorme, **tapando parte del cielo**.
  - **Cuchillos** de Dio congelados en el aire, delante.
  - Luces doradas de El Cairo abajo (`#A97944`), desenfocadas.
  - Grano del fotograma y un poco de **líneas de velocidad** detenidas.

### ¿Cuál primero?

| | A · Polaroid de Joseph | B · Ficha de Rohan | C · Apisonadora de Dio |
|---|---|---|---|
| Objeto real en Blender | Cámara + foto | Hoja + mesa | Apisonadora |
| Usa lo que propone el plan | fotograma + flecha | **ficha de Stand** | fotograma + flecha |
| Dice la regla con un meme de la serie | «Tu siguiente frase será» | **«…pero me niego»** | la flecha TBC |
| Riesgo | que la foto se vea pequeña | que el reloj sature | que quede «plantilla de meme» |
| Recomendación | **1.ª** | **2.ª** (o lámina 2 si se quiere más) | 3.ª |

- **Recomiendo A**: es un **objeto nuevo** (la cámara) que explica el
  canal (fotos = memes), usa al **rey de los memes** (Joseph) y mete la
  flecha **con sentido** («sigue en otro canal»).
- Como la lámina que ya existe **le gustó**, lo más seguro es **mejorar
  la misma idea** (fotograma + flecha) con A, que añade objeto y luz.
- **No hace falta lámina 2**: el canal tiene tres textos. Si se quiere
  una, **B** funciona como «lámina 2: ficha del canal».


---

## 20 · Lo que no pude verificar

- **Minutos dentro de los vídeos de YouTube**: `yt-dlp` sólo pudo leer
  título, duración, fecha y vistas; YouTube pedía iniciar sesión para
  capítulos y subtítulos. Los minutos de escenas salen de los
  **subtítulos japoneses** (§2), no de YouTube.
- **Frases del doblaje latino** que sólo recoge Doblaje Wiki (⚠️ en
  §10.3): «¡Toma, toma, toma!», «Jámon», «¡Maldición!», «Gángster
  estrella», «Ya siéntese, señora», «¿Ya estamos al aire? Avísenme».
  Hay que oírlas en Netflix antes de citarlas en una lámina.
- **Cómo dice «Nigerundayo» el doblaje latino**: el subtítulo
  automático del clip dice «sigan el plan hasta que ya no puedan
  respirar…»; no es claro ⚠️.
- **«Aplanadora»** por *road roller*: sólo el título de un clip ⚠️.
- **Voces** con una sola fuente (⚠️ en §10.2): Speedwagon, Caesar, Lisa
  Lisa, Pucci, Diavolo, Hol Horse, Terence, Tonio.
- **Estudio de SO partes 2-3 y SBR (New Art)**: sólo Doblaje Wiki.
- **El key visual del 10.º aniversario y el de SBR a tamaño real**: no
  están en las wikis; no los medí.
- **TV Tropes (Memes)** y **The Cutting Room Floor** en directo: reto de
  Cloudflare. De TCRF sólo leí *JoJo's Venture* por Wayback Machine
  (sprites sin usar; nada de cajas de diálogo).
- **Encuesta oficial de personajes** reciente (con votos por
  personaje): no la encontré. Uso la lista de Araki (2000), la encuesta
  oficial de **episodios** (2025) y encuestas de fans.
- **Las 3 últimas hojas** de contacto de Fandom (imágenes más pequeñas)
  no se generaron.
- **Colores de ropa** de §5.3 y §16: a ojo ⚠️.
- **Búsquedas en coreano**: no hice; la obra es japonesa y el resto de
  idiomas cubrió lo necesario. Los subtítulos de GW traen también
  **chino** (grupo Kamigami), que no usé.

---

## 21 · Bitácora de búsqueda

### 21.1 Comprobación de red (24-sep-2026)

- **Primera hora**: Fandom, Doblaje Wiki, JoJo Wiki, Wikipedia,
  ANMTV, Arctic Shift, dafont, FontSpace, Sketchfab y el portal oficial
  daban **bloqueo** (curl `CONNECT 403`, WebFetch «egress blocked»).
  GitHub y WebSearch sí. Wayback Machine respondía a medias.
- **Después** (aviso del coordinador): red **abierta**. Fandom API,
  JoJo Wiki API, Doblaje Wiki API, Sketchfab API, Poly Haven API,
  Pixiv (ajax), Arctic Shift, portal oficial y YouTube (con límites)
  respondieron. Wikipedia en inglés dio **429** (demasiadas peticiones).
  TV Tropes y TCRF: **403 de Cloudflare**.

### 21.2 Búsquedas web (27, con su idioma)

1. JoJo's Bizarre Adventure doblaje latino reparto Jotaro Joseph Dio (es)
2. anmtvla JoJo doblaje latino Netflix Irwin Daayán elenco estudio (es)
3. «Golden Wind» doblaje latino Giorno Bucciarati Mista (es)
4. Phantom Blood doblaje latino Jonathan Dio Speedwagon (es)
5. dubdb JoJo «Latin American Spanish» Josuke Giorno Jolyne (en)
6. «José Luis Piedra» Giorno JoJo doblaje (es)
7. Steel Ball Run Netflix doblaje latino Johnny Gyro 2026 (es)
8. Stone Ocean doblaje latino «Alondra Hidalgo» director (es)
9. «Jonathan Joestar» doblaje latino Netflix 2022, Caesar (es)
10. «yare yare daze» doblaje latino «ay, por favor» (es)
11. ジョジョ 人気投票 公式 結果 1位 (ja)
12. JOJODAY 2025 エピソード総選挙 結果 (ja)
13. JOJODAY 2025 episode poll results por parte (en)
14. official JoJo character popularity poll Shueisha (en) — **sin resultado útil**
15. JJBATWT popularity poll 2025 (en) — **sin resultado útil**
16. みんなのランキング ジョジョ キャラ 1位 (ja)
17. knowyourmeme «To Be Continued» Roundabout origin (en)
18. TV Tropes memes «Is that a JoJo reference» menacing (en)
19. スタンド パラメータ 破壊力 … 六角形 (ja)
20. JoJo logo font free dafont (en)
21. ジョジョ アニメ 10周年 描き下ろし キービジュアル (ja)
22. Steel Ball Run anime Netflix 2026 key visual staff (en)
23. 津田尚克 インタビュー ラウンドアバウト 演出 (ja)
24. ジョジョ アニメ 色が変わる 演出 色彩設計 ゴゴゴ (ja)
25. All Star Battle R interface menus story mode UI (en) — **sólo mods**
26. «Gilberto Vilchis» Kira doblaje latino (es)
27. ジョジョ アニメ 公式 壁紙 配布 (ja)

### 21.3 APIs y herramientas (sin cupo de búsqueda)

- **GitHub**: kitsunekko-mirror (clon *sparse* de 9 carpetas de JoJo),
  google/fonts (47 familias), MrPakoras/JoJoTBCfier,
  valkyrs/jojo-stands, Dogend233/astrbot_plugin_jojo_stand_panel;
  búsqueda de repositorios «jojo stand» (168 resultados).
- **Fandom** (`investigar_serie.py`, wiki `jojo`, 13 páginas):
  1.735 imágenes grandes, 34 hojas.
- **JoJo Wiki API**: To Be Continued, Stand Stats, JoJo Wiki:Poll
  History, JOJODAY, JoJo Pose, Sound Effects, Roundabout, Il vento
  d'oro, Music, Steel Ball Run (Anime), Ora Ora Overdrive, Hirohiko
  Araki, Kira's Coworker, Morioh, y los personajes (Jotaro, Dio,
  Joseph, Giorno, Josuke, Rohan, Kira); imágenes de TBC (282) y Stand
  Stats (324).
- **Doblaje Wiki API**: JoJo's Bizarre Adventure, Los cruzados de polvo
  de estrellas, Diamond is Unbreakable, Golden Wind, Stone Ocean, Steel
  Ball Run, la franquicia, Jotaro, Dio, Joseph, Irwin Daayán y *Así
  habló Kishibe Rohan*.
- **yt-dlp** (búsquedas `ytsearch`, unas 20): tráileres de SBR y SO,
  PV del 10.º aniversario, OP, recopilaciones TBC, análisis, clips del
  doblaje latino (con subtítulo automático en 3 de ellos) y fandubs.
- **Sketchfab API**: jojo, road roller, steamroller, stand arrow, stone
  mask, tarot card, crt television, polaroid camera, jotaro, morioh.
- **Poly Haven API** (862 texturas; filtré papel, madera, asfalto,
  arena, yeso, cuero).
- **Pixiv** (ajax): ジョジョの奇妙な冒険, ジョジョ立ち, To_Be_Continued,
  ゴゴゴゴ, スタンドパラメータ, ジョジョ100users入り, ジョジョ パロディ.
- **Arctic Shift**: r/ShitPostCrusaders «Steel Ball Run» (40 posts);
  r/StardustCrusaders «popularity poll» → **timeout**.
- **Wayback Machine**: Doblaje Wiki (antes de abrirse la red) y TCRF
  (*JoJo's Venture*).
- **Portal oficial**: digital-contents (10 fondos de pantalla,
  medidos).

### 21.4 Fuentes consultadas por tipo (más de 40)

- **Oficiales**: [JOJO PORTAL](https://jojo-portal.com) (notas de
  producción [02](https://jojo-portal.com/special/production-note/02/)
  y [04](https://jojo-portal.com/special/production-note/04/),
  [fondos](https://jojo-portal.com/special/digital-contents/),
  [JOJODAY 2025](https://jojo-portal.com/special/jojoday2025/episode-vote/result/),
  [10.º aniversario](https://jojo-portal.com/special/jojoanime10th/)),
  [@anime_jojo en X](https://x.com/anime_jojo/status/1355078246447022080),
  canales de YouTube de **Warner Bros. Japan Anime**, **Netflix
  Latinoamérica**, **Netflix Japan** y **Jump Channel**,
  [PR Times (THE★JOJO WORLD)](https://prtimes.jp/main/html/rd/p/000000007.000159118.html),
  [web de Ora Ora Overdrive](https://jojo-oradora.com/).
- **Entrevistas y prensa (japonés)**: [Anime! Anime! (Tsuda)](https://animeanime.jp/article/2013/05/14/14037.html),
  [Anime Da Vinci (director visual)](https://ddnavi.com/interview/208016/a/),
  [CGWorld (Kamikaze Douga)](https://cgworld.jp/article/jojo-kamikaze-2303.html),
  [Natalie](https://natalie.mu/comic/news/472623), [Famitsu](https://www.famitsu.com/news/202207/01267053.html),
  [Mantan](https://mantan-web.jp/article/20220701dog00m200013000c.html),
  [Nlab Research](https://nlab.itmedia.co.jp/research/articles/202866/),
  [ranking.net](https://ranking.net/rankings/best-jojo-characters),
  [Renote](https://renote.net/articles/20661),
  [Wikipedia japonesa: スタンド](https://ja.wikipedia.org/wiki/%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%89_(%E3%82%B8%E3%83%A7%E3%82%B8%E3%83%A7%E3%81%AE%E5%A5%87%E5%A6%99%E3%81%AA%E5%86%92%E9%99%BA)).
- **Prensa (inglés)**: [ANN](https://www.animenewsnetwork.com/interest/2025-04-14/jojoday-2025-poll-names-fans-favorite-jojo-bizarre-adventure-episodes/.223542),
  [AniTrendz](https://www.anitrendz.com/news/2025/12/08/key-visual-for-steel-ball-run-jojos-bizarre-adventure-revealed),
  [Anime Corner](https://animecorner.me/jojos-bizarre-adventure-steel-ball-run-part-7-anime-reveals-main-staff-david-production-returns/),
  [Final Weapon](https://finalweapon.net/2026/09/23/jojos-bizarre-adventure-steel-ball-run-anime-opening-theme-song-artist/),
  [What's on Netflix](https://www.whats-on-netflix.com/news/anime/jojos-bizarre-adventure-steel-ball-run-sets-march-2026-netlfix-release/),
  [Gizmodo](https://gizmodo.com/to-be-continued-is-the-sleeper-meme-hit-of-the-summer-1781860391),
  [TheGamer](https://www.thegamer.com/jojo-reference-meme-origin/),
  [Made Good Designs](https://madegooddesigns.com/jojos-bizarre-adventure-font/).
- **Wikis de fans**: [JoJo Wiki](https://jojowiki.com) (API),
  [JoJo's Bizarre Wiki de Fandom](https://jojo.fandom.com) (API),
  [Teh Meme Wiki](https://meme.fandom.com/wiki/To_Be_Continued),
  [Know Your Meme](https://knowyourmeme.com/memes/is-this-a-jojo-reference),
  [Cultural History of the Internet](https://internet.medialities.org/2020/11/16/roundabout/),
  TCRF (Wayback). TV Tropes: **no respondió**.
- **Doblaje latino**: [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/JoJo%27s_Bizarre_Adventure_(franquicia)) (API),
  [ANMTV](https://www.anmtvla.com/2022/01/jojos-bizarre-adventure-doblaje-latino.html) (4 artículos y su [post en X](https://x.com/ANMTVLA/status/2034641449514373435)),
  [TVLaint](https://www.tvlaint.com/2022/01/netflix-lanza-el-doblaje-latino-de-mas-partes-de-jojos.html?m=1),
  [Gamerfocus](https://www.gamerfocus.co/anime/cuando-jojos-bizarre-adventure-parte-5-golden-wind-netflix-actualiza-todas-las-temporadas-con-doblaje-al-espanol-de-latinoamerica/),
  [LevelUp](https://www.levelup.com/noticias/652383/Jojos-Bizarre-Adventure-Stone-Ocean-ya-esta-disponible-en-Netflix-con-doblaje-latino/),
  [Cinepremiere](https://cinepremiere.com.mx/jojos-bizarre-adventure-stone-ocean-anime-trailer-estreno.html),
  [Star Con (Facebook)](https://www.facebook.com/starconmx/posts/jos%C3%A9-luis-piedra-actor-de-doblaje-que-dio-voz-a-giorno-giovanna-en-jojos-bizarre/1551328119698547/),
  [Festival La Chida (TikTok)](https://www.tiktok.com/@festivallachida/video/7497029187878931730),
  clips de YouTube del doblaje (§10.3).
- **Foros y comunidades**: Reddit r/ShitPostCrusaders (vía Arctic
  Shift), Pixiv, TikTok (páginas de búsqueda).
- **Arte**: Pixiv (7 etiquetas), Fandom y JoJo Wiki (galerías).
  ArtStation y DeviantArt: **no buscados** (Pixiv bastó para ver qué
  hacen los fans).
- **Código y recursos**: GitHub (5 repositorios), Sketchfab, Poly
  Haven, Google Fonts, FontSpace, dafont.

### 21.5 Lo que NO encontré

- Una **encuesta oficial de personajes** reciente con votos.
- **Minutos** dentro de vídeos de YouTube (§20).
- Una **letra libre** que sea la de la flecha TBC: no existe; hay que
  calcarla.
- Cómo se **dice en latino** «ORA ORA desu ka / YES YES YES» y «¿Te
  acercas a mí?»: no hay clip con subtítulo que lo confirme.
- Fondos de pantalla oficiales de **SO y SBR** (la campaña de 2021 sólo
  llega a GW).
