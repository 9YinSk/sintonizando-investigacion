---
tags: [biblia, serie, laminas]
serie: "Neon Genesis Evangelion"
canal: "#demos"
fecha: 2026-09-24
repaso: 2026-09-26
---

# Biblia · Neon Genesis Evangelion — para #demos

> [!important] Cómo se hizo, y sus límites
> - **Segunda pasada, 26-sep-2026, con la red abierta.** Un equipo de
>   cuatro investigadores (imagen, vídeo, voz, texto) y un redactor. Se
>   pudo usar: la wiki de Fandom por su API (`investigar_serie.py`, 455
>   imágenes, **3 hojas en `hojas/`**), Doblaje Wiki por su API y sus
>   muestras de audio (`voz.py`), **Internet Archive** (episodios
>   completos, opening, ending y el tráiler de GKIDS, mirados con
>   `fotogramas.py`), la API de Sketchfab (licencias exactas), las de
>   Wallhaven y ambientCG, EvaWiki, Know Your Meme y TV Tropes. Siguen
>   cerrados: YouTube (pide sesión), Reddit (ni por Arctic Shift), The
>   Cutting Room Floor y Wayback Machine (fallo de certificado y de túnel).
>   Lo que cambió va justo debajo, en «Segunda pasada · qué cambió».
> - **Primera pasada, 24-sep-2026, con la red cerrada**: Fandom (y Doblaje
>   Wiki), Wikipedia, YouTube, Reddit, Wayback Machine, Google Sites, ANMTV
>   y Xataka daban **403 o «egress blocked»**. Por eso entonces no hubo
>   hojas de contacto y todas las imágenes iban como **enlace**.
> - En la primera pasada la fuente principal fueron las **búsquedas web**
>   (la lista completa, con su idioma, está al final, en la bitácora).
> - GitHub sí respondía. De ahí saqué lo más útil de todo el trabajo:
>   **los subtítulos japoneses de los 26 episodios y de The End of
>   Evangelion, con sus tiempos**, del repositorio
>   [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Shin%20Seiki%20Evangelion)
>   (archivos «Erai-raws … [JPN].ass»: son los subtítulos japoneses para
>   sordos de **Netflix**, con el nombre de quien habla entre paréntesis).
>   Con ellos doy el **minuto de cada escena**. Es el minuto de la versión
>   de Netflix: en el Blu-ray va **un segundo antes** (lo comprobé con los
>   subtítulos del BD del mismo repositorio).
> - También bajé de [google/fonts](https://github.com/google/fonts) las
>   letras propuestas y comprobé una a una, con fontTools, si traen
>   á é í ó ú ñ ¿ ¡.
> - **Cómo leo los episodios**: «ep. 15» es el episodio 15 de la serie de
>   TV (1995-96). «EoE» es la película *The End of Evangelion* (1997). El
>   minuto va así: 00:11:10.
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su minuto.
>   ⚠️ **dudoso**: una sola fuente, o lo describo de memoria. Lo de memoria
>   siempre va marcado. Lo que **se ve** en un fotograma (postura, luz) lo
>   describo de memoria ⚠️ aunque el minuto esté comprobado: mira el
>   fotograma antes de dibujar.
> - **Segunda pasada**: lo que ya **se vio** en un fotograma lleva ✅ y un
>   enlace al segundo exacto en Internet Archive (`?t=` en segundos). Ese
>   minuto es el **del archivo**, que puede ir unos segundos desfasado del
>   de Netflix; se dice en cada caso.

---

## Segunda pasada · qué cambió

Fecha: 26-sep-2026. Se corrigió y completó la biblia en su sitio, sin
rehacerla. Las fuentes de cada dato están en su sección.

**Corregido (antes → ahora)**

- **Voz latina de Gendo** (doblaje de 1999): «no pude sacar el nombre» →
  **Humberto Solórzano** ✅ (Doblaje Wiki por su API y AniList).
- **Voz latina de Ritsuko**: ⚠️ → **Maru Guerrero** ✅ (las mismas dos).
- **Estudio de *Renewal of Evangelion***: «no lo encontré» → Grabaciones y
  Doblajes Internacionales, dirección de Gerardo García, grabado en 2007 y
  emitido en 2008 ⚠️ (sólo lo dice Doblaje Wiki).
- **Pose «silueta de Rei», ep. 6, 15:32** → es **Shinji llorando** (visto
  en los fotogramas vecinos). Se quita de las poses de Rei.
- **«La ficha de Rei», ep. 5, 4:25** (era de memoria) → **no existe** ese
  plano. Ese tramo es un resumen técnico de la Unidad 00. Lo que sí hay: la
  placa «402 綾波» en la puerta de Rei (13:12) y sus gafas rotas (14:15).
- **Vestuario**: hex «de memoria» → **medidos** en arte oficial con fondo
  transparente: traje de Shinji `#036ED3`, pichi de Asuka `#022A51`, traje
  de Rei `#E9EDF3`, chaqueta de Misato `#E02824`.
- **Paleta de los sitios**: paletas de fans → **medidas en fotogramas
  oficiales** con `estilo.py` (jaula de las Eva `#3D4D2E` `#536347`
  `#88A27E`).
- **Encuesta NHK 2020**: puestos 4 (Shinji) y 5 (Misato) con una fuente →
  ✅ con Kimigaku.
- **Memes «Get in the robot, Shinji» y «pose Gendo»**: ⚠️ → ✅ (Know Your
  Meme).
- **Chicago (monolitos de SEELE)**: «no lo comprobé» → ChiKareGo2 pasado
  por fontTools: trae á é í ó ñ ¿ ¡; **le faltan ú y ü** minúsculas.
- **Caras de Asuka (ep. 8), Misato (ep. 2) y Kaworu (ep. 24)**: minuto de
  oído → **visto en fotograma** ✅. La de Asuka es el segundo 244 (4:04),
  no el 246.

**Añadido**

- **Hojas de contacto**: 3 en `hojas/`, con qué número sirve para qué
  (sección nueva «Las hojas de contacto», tras la 3).
- **`referencias.json`**: 225 referencias, juntadas de las cuatro partes y
  del recolector.
- **12 modelos 3D** de Sketchfab con la licencia leída en su API, entre
  ellos un **rig de Asuka** (CC BY) y una tablilla para la ficha de piloto.
- **Fotogramas vistos de verdad** con su segundo: ep. 1, 2, 5, 6, 8, 24,
  el opening, el ending y el tráiler oficial de GKIDS.
- **Frases del doblaje latino textuales con minuto**, oídas en los
  episodios doblados: «¿Por qué no pruebas sonreír, Rei?» (ep. 6, 21:34) y
  «¡Yo te amo, Shinji!» (ep. 24, 9:37). Y seis muestras oficiales de
  Doblaje Wiki transcritas y medidas con `voz.py`.
- **Efectos de sonido** con el nombre exacto de su librería (la sirena de
  NERV es de Hollywood Edge).
- **Secciones nuevas de los puntos 18 a 25** del encargo: técnica y cómo
  replicarla, texturas 2D, gustos de cada personaje, por qué la aman, fan
  dubs, colaboraciones (McDonald's Japón, *The First Descendant*, Ichiban
  Kuji del 30 aniversario), obras parecidas y el mundo con su glosario.
- La tabla **«Cumplimiento del encargo»** y la bitácora de la segunda
  pasada.

**Los ⚠️**: había **108** antes de esta pasada. Los que quedan se cuentan
al final de la tabla de cumplimiento. Siguen abiertos, sobre todo: las
cajas de diálogo de los juegos (The Cutting Room Floor no abre), el
bocadillo del manga visto en una página, fan dubs de voz en español
(YouTube no abre), el piano de Kaworu y un fotograma propio de la pose
Gendo.

## Índice

Ojo: los números de sección son los de la primera pasada, no los del
encargo. La tabla «Cumplimiento del encargo» dice dónde está cada punto.

- 0 · El canal y lo que tiene que decir
- 1 · Resumen para quien tenga prisa
- 2 · Las escenas que sirven para #demos (con minuto)
- 3 · Arte oficial · y «Las hojas de contacto»
- 4 · Fan art y 3D
- 5 · Sitios, luz, paleta y texturas
- 6 · Tipografía
- 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)
- 8 · Los personajes
- 9 · ¿Quién es el más querido?
- 10 · Doblaje latino
- 11 · Música y sonido
- 12 · Vídeos
- 13 · Videojuegos de la franquicia
- 14 · Lo que ama el fandom, y qué NO hacer
- 15 · Poses analizadas por personaje
- 16 · Vestuario
- 17 · Paisajes y fondos de pantalla
- 18 · Guía para generar con IA (imagen y texto)
- Puntos 18 a 25 del encargo: técnica · texturas 2D · gustos · por qué la
  aman · fan dubs · colaboraciones · obras parecidas · el mundo
- 19 · Tres conceptos para la lámina de #demos
- 20 · Lo que no pude verificar
- Cumplimiento del encargo
- 21 · Bitácora de búsqueda (y la de la segunda pasada)

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección EL ESTUDIO):

> **ıı・🎧・demos** (foro) · 6 hilos · etiquetas: Voz masculina, Voz
> femenina, Voz andrógina, Infantil, Joven, Adulto, Anciano, Narración,
> Comercial, Canto, Imitación, Disponible, Ocupado, Anime, Series,
> Películas, Videojuegos, Audiolibro, Colaboración — _Tu ficha de
> DOBLAJE: un hilo con tu nombre, tus demos y tu rango vocal._
>
> Hilos hoy: Shira · AlcachofasjuanitO-Demos.exe · Rikipe · Liva ·
> 📌 **Tu ficha de voz (léeme antes de abrir la tuya)** · YinX-Demos.

Lo que dicen de #demos los canales vecinos (sirve para la lámina):
- **general-doblaje**: «Tu voz grabada va a demos; los papeles, a castings.»
- **canto**: «Tus covers van a demos-canto, un hilo por cover.»
- **demos-canto**: «Tu ficha de CANTO, **aparte de la de doblaje**.»

Función según el encargo: **foro donde cada uno sube su ficha de voz y sus
demos (19 etiquetas)**. Objeto que propone el plan: **ficha de piloto de
NERV**. La idea es buena y la serie la respalda con escenas reales (ver §2):
a cada piloto lo elige **el informe del Instituto Marduk** y tiene su
**ficha**, su **número de «Children»** y su **tarjeta de seguridad**.

### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Demos** | nombre del canal |
| 2 | **Tu ficha de doblaje** | qué es |
| 3 | **Un hilo con tu nombre** | cómo se abre |
| 4 | **Tus demos** | qué subes |
| 5 | **Tu rango vocal** | qué subes |
| 6 | **Lee la ficha fijada antes de abrir la tuya** | el léeme |
| 7 | **Ponle tus etiquetas** | remite a la lámina 2 |
| 8 | **Tus covers van a demos-canto** | lo que NO va aquí |
| 9 | **Los papeles, a castings** | lo que NO va aquí |
| 10 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

### Los textos de la lámina 2 (las 19 etiquetas)

**No caben en la lámina 1.** Van en una lámina 2, agrupadas en seis
bloques. Los bloques son míos (el inventario sólo da la lista):

| Bloque | Etiquetas (tal cual, 19) |
|---|---|
| **Tu voz** | Voz masculina · Voz femenina · Voz andrógina |
| **Tu edad de voz** | Infantil · Joven · Adulto · Anciano |
| **Lo que haces** | Narración · Comercial · Canto · Imitación |
| **Para qué medio** | Anime · Series · Películas · Videojuegos · Audiolibro |
| **Tu estado** | Disponible · Ocupado |
| **Buscas equipo** | Colaboración |

> [!tip] La serie ya tiene su «lámina 2»
> En la sala de mando de NERV los datos salen como **bloques de estado
> encendidos o apagados** (el panel de la sincronización, los paneles
> «REFUSED/ACCEPTED»). Las etiquetas pueden ser **pilotos de un panel**:
> «Disponible» encendido en verde, «Ocupado» en rojo ⚠️ (descrito de
> memoria; ver §7).

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué Evangelion encaja con #demos | En la serie **a cada piloto lo elige un informe y tiene su ficha**, que alguien **lee en voz alta** (Rei, ep. 5, 00:04:25; Kaworu, ep. 24, 00:05:58). Y luego hay una **prueba** que se comenta con números (ep. 12, 00:05:22; ep. 16, 00:03:20). Es un hilo de #demos. |
| La frase del canal | Misato antes de la prueba de Kaworu: **«素直に彼の実力 見せてもらいましょ»** (Que nos enseñe lo que sabe hacer, ep. 24, 00:06:31) ✅ |
| El gancho de voz | Kaworu: **«歌はいいね 歌は心を潤してくれる»** (Cantar es bueno, le da agua al corazón, ep. 24, 00:05:13) ✅ |
| Cuadro de diálogo propio | **La cartela negra** con letras blancas en mincho extranegrita **comprimida** (Matisse EB) ✅. Y para la voz: los **monolitos «SOUND ONLY»** de SEELE ✅. Nada de globos blancos. |
| Objeto para la lámina | **La ficha de NERV**: carpeta con hoja, foto, **tarjeta de seguridad** y sello (concepto A). Alternativas: los **monolitos** (B) y **el chelo de Shinji con Asuka aplaudiendo** (C, ep. 15, 00:11:10). |
| El más querido | **Asuka**, 1.ª en el voto oficial de NHK (2020, 109.577 votos) ✅; **Kaworu** 2.º y **Rei** 3.ª ✅, Shinji 4.º ⚠️. Asuka protagoniza el **corto del 30 aniversario** (2026) ✅. La frase más votada es de Rei: «あなたは死なないわ 私が守るもの» ✅. |
| Letras libres | **Zen Old Mincho Black**, **Shippori Mincho B1 ExtraBold** o **Noto Serif JP Black** para la cartela; **Noto Serif Display** (trae eje de ancho: se comprime sola) para el español. Todas con tildes, ñ, ¿ y ¡: comprobado en el archivo. |
| Voz latina | Shinji **Víctor Ugarte** y Rei **Circe Luna** en el original, en Netflix y en las *Rebuild* ✅; Asuka **Norma Echevarría** (1999) y **Georgina Sánchez** (Netflix y *Rebuild*) ✅; Misato **Toni Rodríguez** (1999) y **Marisol Romero** (Netflix) ✅; Kaworu **Ernesto Lezama** (1999) y **Alberto Bernal** (Netflix) ✅. Netflix: **Audiomaster Candiani**, dirección de **América Torres** ✅. |
| Tono | Verano brillante pero serio. Negro, blanco y **naranja de pantalla**. Personajes de **14 años**: nada de *fanservice*. |
| Lo nuevo (2026) | Serie nueva anunciada el 23-feb-2026 (guion de **Yoko Taro**, Khara y CloverWorks) ✅; libro de arte de **Sadamoto** el 10-nov-2026 ✅; el juego XR ***Δ Cross Reflections*** (eres **un aprendiz de NERV que quiere ser piloto**) ✅. |

---

## 2 · Las escenas que sirven para #demos (con minuto)

Todas salen de los subtítulos japoneses de Netflix
([kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Shin%20Seiki%20Evangelion)):
**el texto y el minuto están comprobados** ✅. La traducción al español es
**mía**, no la del doblaje latino. Lo que **se ve** en cada una lo describo
de memoria ⚠️: mira el fotograma antes de usarlo.

### 2.1 La «ficha de piloto» existe en la serie (y se lee en voz alta)

En Evangelion **a cada piloto lo elige un informe** (el del Instituto
Marduk) y cada uno tiene un **número**: First, Second, Third, Fourth y
Fifth «Children». Cuando llega uno nuevo, alguien **lee su ficha**. Es
exactamente lo que es un hilo de #demos.

| Escena | Minuto | Qué se dice (japonés → mi traducción) | Para qué sirve |
|---|---|---|---|
| ep. 1 | 00:10:04 → 00:10:19 | Misato: «お父さんからIDもらってない？» (¿Tu padre no te dio una identificación?). Shinji se la da. Misato: «じゃあ これ 読んどいてね» (**Entonces lee esto**). Shinji lee: «ネルフ» | **El léeme**. Es el folleto de bienvenida de NERV ⚠️ (en pantalla se lee «ようこそNERV江», de memoria) |
| ep. 1 | 00:12:06 | Misato presenta a Shinji a Ritsuko: «マルドゥックの報告書による サードチルドレン» (el Third Children, según el informe Marduk) | Presentar a alguien por su ficha |
| ep. 5 | 00:04:25 → 00:04:38 | Ritsuko **lee la ficha de Rei**: «綾波レイ 14歳 / マルドゥックの報告書によって選ばれた最初の被験者 ファーストチルドレン / エヴァンゲリオン試作零号機 専属操縦者 / 過去の経歴は白紙 全て抹消済み» (Rei Ayanami, 14 años. Elegida por el informe Marduk, primera sujeto, First Children. Piloto asignada del prototipo Unidad 00. Historial en blanco, todo borrado) | **La ficha de piloto, dicha en voz alta**. Es el modelo de la lámina: nombre, edad, unidad, rango |
| ep. 5 | 00:11:57 → 00:12:16 | Ritsuko: «綾波レイの更新カード … 届けてもらえないかしら？» (la tarjeta renovada de Rei, ¿se la llevas?) | **La tarjeta de seguridad con foto**, objeto real |
| ep. 5 | 00:12:25 | Misato, burlona: «レイの写真を ジーッと見ちゃったりして» (mirando fijo la foto de Rei, ¿eh?) | La tarjeta **lleva foto** ✅ |
| ep. 5 | 00:16:11 | Shinji, tartamudo, en casa de Rei: «カ… カード！ カード 新しくなったから» (¡La… la tarjeta! Que la renovaron) | Shinji nervioso = el novato que abre su hilo |
| ep. 8 | 00:03:43 → 00:03:46 | Asuka se presenta sola: «エヴァンゲリオン弐号機の専属パイロット セカンドチルドレン 惣流・アスカ・ラングレーよ» (Piloto asignada de la Unidad 02, Second Children, Asuka Langley Soryu) | **Cómo se presenta una ficha**: unidad, rango, nombre. La pose de «presentar» |
| ep. 8 | 00:04:09 | Asuka: «で ウワサの サードチルドレンは どれ？» (¿Y cuál es el famoso Third Children?) | Buscar una ficha |
| ep. 17 | 00:08:08 → 00:08:22 | Ritsuko: «テストパイロットは 4人目を使うわよ» (usaremos al cuarto); Misato: «フォースチルドレンが見つかったの？»; Ritsuko: «正式な書類は明日届くわ» (**los papeles oficiales llegan mañana**) | El expediente en papel |
| ep. 17 | 00:21:17 → 00:21:24 | Asuka, en el ordenador de Kaji: «これ 私たちのシンクロデータね / えっ 4人!? / フォースチルドレンが なんで こいつなの？» (Son nuestros datos de sincronización. ¿Cuatro? ¿Por qué el Fourth es este?) | Una **lista de fichas en pantalla** |
| ep. 24 | 00:05:36 → 00:05:48 | Kaworu se presenta: «僕はカヲル 渚カヲル / 君と同じ仕組まれた子ども フィフスチルドレンさ / カヲルでいいよ 碇君» (Soy Kaworu, Kaworu Nagisa. Un niño elegido como tú, el Fifth Children. Llámame Kaworu) | Presentarse, en tono amable |
| ep. 24 | 00:05:58 → 00:06:03 | Misato lee la ficha de Kaworu: «渚カヲル 過去の経歴は抹消済み レイと同じくね»; Hyuga: «ただ生年月日は セカンドインパクトと同一日です» (su fecha de nacimiento es la del Segundo Impacto) | La ficha con un dato raro |
| ep. 24 | 00:06:26 → 00:06:31 | Hyuga: «フィフスのシンクロテスト どうします？»; Misato: «素直に彼の実力 見せてもらいましょ» (**que nos enseñe lo que sabe hacer, sin trucos**) | **La frase del canal**: subir tu demo es enseñar lo que sabes hacer |

### 2.2 La prueba de sincronización = la demo

La **prueba de sincronización** es la audición de un piloto: se mide, se
comenta, se compara. Es lo que pasa con una demo.

| Escena | Minuto | Qué se dice | Para qué sirve |
|---|---|---|---|
| ep. 1 | 00:19:58 | Maya: «シンクロ率 41.3パーセント» (sincronización 41,3 %) | El número en pantalla |
| ep. 12 | 00:05:02 → 00:05:11 | Ritsuko: «それで この数値？ 大したものだわ»; Maya: «ハーモニクス シンクロ率も アスカに迫ってますね»; Ritsuko: «これを才能というのかしら» (¿A esto se le llama talento?) | Escuchar una demo y valorarla |
| ep. 12 | 00:05:22 → 00:05:37 | Ritsuko por radio: «3人とも お疲れさま / シンジ君 よくやったわ / ハーモニクスが前回より8も伸びているわ»; Asuka: «でも 私より50も少ないじゃん»; Ritsuko: «10日で8よ 大したものだわ» | **Dar ánimo con datos**. Ritsuko = la que comenta demos |
| ep. 16 | 00:03:14 → 00:03:20 | Misato por radio: «聞こえる？ シンジ君»; Shinji: «今のテストの結果 どうでした？»; Misato: «ハ〜イ ユーアー ナンバーワン！» (¡Hai, you are number one!) | **Celebrar**. Misato al micro |
| ep. 16 | 00:03:23 → 00:03:44 | Asuka, picada: «あ〜っさり 抜かれちゃったじゃなぁい … 無敵のシンジ様！» (Me pasó así sin más… ¡el invencible señor Shinji!) | Lo que NO hay que hacer al comentar demos (ironía) |
| ep. 9 | 00:11:03 → 00:11:34 | Misato: «2人の協調 完璧なユニゾンが必要なの … この曲に合わせた攻撃パターンを覚え込むのよ» (hace falta unísono perfecto; aprendan el ataque al ritmo de esta canción) | **Sincronía con música**: como doblar a tiempo con la boca |

### 2.3 Música y voz dentro de la serie

| Escena | Minuto | Qué pasa | Para qué sirve |
|---|---|---|---|
| ep. 15 | 00:11:10 → 00:11:44 | Shinji **toca el chelo** solo en casa (♪チェロの音色). **Aplausos**. Asuka: «結構 いけるじゃない そんなの持ってたの？» (No está nada mal. ¿Tenías eso?). Shinji: «5歳のときから始めて この程度だからね / 才能なんて別にないよ» (Empecé a los 5 y mira hasta dónde llegué. No tengo talento) | **La escena de #demos**: alguien enseña lo que hace y otro aplaude. Y el miedo del que sube su primera demo |
| ep. 24 | 00:04:55 → 00:05:20 | Kaworu tararea el «Himno de la alegría» (交響曲第9番) y le dice a Shinji: «歌はいいね / 歌は心を潤してくれる / リリンが生み出した文化の極みだよ / そう感じないか？» (**Cantar es bueno. Le da agua al corazón. Es la cumbre de la cultura de los Lilin. ¿No lo sientes?** «歌» es canción o cantar) | **El gancho perfecto** para un canal de voz |
| ep. 1, 3, 8, 9, 12, 13 | 00:23:19 (final) | Misato cierra el avance: «この次も サービス サービス！» (¡Y la próxima, más servicio!) | Despedida alegre, la muletilla de Misato ✅ |

### 2.4 Otras frases que todo fan reconoce (con minuto)

| Frase | Quién | Dónde |
|---|---|---|
| «乗るなら早くしろ でなければ帰れ！» (Si vas a subir, hazlo ya. Si no, vete) | Gendo | ep. 1, 00:15:38 |
| «逃げちゃダメだ 逃げちゃダメだ…» (No debo huir) → «やります 僕が乗ります！» (Lo haré. Yo lo piloto) | Shinji | ep. 1, 00:18:33 → 00:18:42 |
| «“ミサト”でいいわよ» (Llámame Misato) | Misato | ep. 1, 00:06:20 |
| «知らない天井だ» (Un techo que no conozco) | Shinji | ep. 2, 00:03:53 |
| «こういうとき どんな顔すればいいのか…» / «笑えばいいと思うよ» (No sé qué cara poner / Creo que deberías sonreír) | Rei / Shinji | ep. 6, 00:21:30 y 00:21:35 |
| «あんたバカァ？» (¿Eres idiota?) | Asuka | ep. 8, 00:11:02 (y ep. 9, 11, 12, 15, 20) |
| «好意に値するよ» (Mereces mi afecto) | Kaworu | ep. 24, 00:09:35 |
| «僕は ここにいてもいいんだ！» → «おめでとう» (¡Puedo quedarme aquí! → Felicidades) | Shinji / todos | ep. 26, 00:21:17 y 00:21:33 |

---

## 3 · Arte oficial y referencias visuales

> [!note] Segunda pasada: ya hay imágenes vistas
> En la primera pasada no se pudo bajar nada. Ahora `investigar_serie.py`
> bajó de la wiki de Fandom **455 imágenes (208 grandes)** y montó 5 hojas;
> las 3 mejores están en `hojas/` (sección «Las hojas de contacto», justo
> después). Lo nuevo está en §3.5.

### 3.1 Quién hizo el aspecto de la serie ✅

- **Diseño de personajes**: **Yoshiyuki Sadamoto** (también dibujó el manga,
  14 tomos, 1994-2013 ⚠️ de memoria).
- **Diseño de las Eva**: **Ikuto Yamashita**. En 2025 dibujó el **logo del
  30 aniversario** y la portada del vinilo de Yoko Takahashi
  ([web del 30 aniversario](https://30th.evangelion.jp/)).
- **Dirección de arte (fondos)**: **Hiroshi Katō** (nacido en Nara, 1965),
  también en las películas *Rebuild*
  ([ANN](https://www.animenewsnetwork.com/encyclopedia/people.php?id=16),
  [TMDB](https://www.themoviedb.org/person/52215-hiroshi-kato?language=en-US)).
- **Director**: **Hideaki Anno**. Estudio: **Gainax** (serie, 1995-96) y
  **Khara** (películas *Rebuild*, 2007-2021).

### 3.2 Libros de arte

| Libro | Qué trae | Enlace |
|---|---|---|
| **Der Mond** (Sadamoto, 1999; Viz en inglés, 2003) | Las ilustraciones a color de Sadamoto: 74 páginas de Evangelion | [Amazon (Viz)](https://www.amazon.com/Mond-Art-Neon-Genesis-Evangelion/dp/1421507676) · [Evangelion Wiki](https://evangelion.fandom.com/wiki/Yoshiyuki_Sadamoto) |
| **Die Sterne** (Kadokawa, 11-jul-2003) | Ilustraciones de varios artistas de Gainax: Sadamoto, Takeshi Honda, Tsurumaki, Yamashita, Matsubara | [Evangelion Wiki](https://evangelion.fandom.com/wiki/Die_Sterne) · [Amazon JP](https://www.amazon.com/Die-Sterne-Genesis-Evangelion-Japanese/dp/4048536524) |
| **貞本義行画集 EVANGELION** (edición limitada) | **Nuevo**: sale el **10 de noviembre de 2026**, con 4 mini *shikishi* dibujados para él | [eva-info.jp (oficial)](https://www.eva-info.jp/27248) · [Denfaminicogamer](https://news.denfaminicogamer.jp/news/2607233l) |
| **Groundwork of Evangelion 3.0+1.0** | Fotogramas clave y *layouts* de color, incluida la estación de Ube-Shinkawa | [Tokyo Otaku Mode](https://otakumode.com/shop/632adc73d8ada200d22bd642/Groundwork-of-Evangelion-3-0-1-0-Thrice-Upon-a-Time-02-w-Bonus) |

### 3.3 El 30 aniversario (2025-2026): el arte más nuevo ✅

- **Web oficial**: [30th.evangelion.jp](https://30th.evangelion.jp/), con
  secciones [#Official](https://30th.evangelion.jp/articles/official) y
  [#Items](https://30th.evangelion.jp/articles/items).
- **Exposición «ALL OF EVANGELION»**: del 14-nov-2025 al 12-ene-2026 en
  Tokyo City View (Roppongi Hills). Fotos:
  [Animate Times](https://www.animatetimes.com/news/details.php?id=1763006385).
- **Concurso de ilustración en pixiv** por el 30 aniversario, con un efecto
  de «campo AT»: [pixiv](https://www.pixiv.co.jp/2025/07/15/120000).
- **Arte de Sadamoto** para el 30 aniversario de la revista Shōnen Ace:
  [eva-info.jp](https://www.eva-info.jp/22856).
- Goods de Sadamoto a la venta en todo el mundo:
  [eva-info.jp](https://www.eva-info.jp/14599).

### 3.4 Objetos oficiales que existen de verdad (sirven para Blender)

| Objeto | Qué es | Fuente |
|---|---|---|
| **Tarjeta de piloto NERV** (NERVパイロットIDカード) | Tarjetas de plástico de Shinji, Rei, Asuka, Kaworu y Mari, premio de las máquinas del **«EVANGELION 京都基地»** en el Tōei Uzumasa Eigamura de Kioto | [Yahoo! Flea Market (5 tipos)](https://paypayfleamarket.yahoo.co.jp/item/z62064902) · [Kaworu](https://paypayfleamarket.yahoo.co.jp/item/z57264404) ⚠️ (dos anuncios de reventa: mira las fotos) |
| **La tarjeta de Rei** (ep. 5) | La tarjeta de seguridad que Shinji le lleva a Rei. Una imagen de ella | [Tumblr @shin-seiki-evangelion](https://www.tumblr.com/shin-seiki-evangelion/36482967167/rei-ayanami-nerv-id-card) ⚠️ (no pude abrirla) · resumen del episodio en [NERV Archives](http://www.nervarchives.com/tv.series.05.php) y [Evangelion Wiki](https://evangelion.fandom.com/wiki/Episode:05) |
| **El SDAT de Shinji** | El reproductor real es un **Sony WMD-DT1** (DAT portátil, sólo reproduce) | [WorthPoint](https://www.worthpoint.com/worthopedia/retro-sony-wmd-dt1-portable-dat-1844870058) ⚠️ una fuente |
| **Walkman F «SDAT»** (Sony, 2014) | Walkman oficial grabado como el SDAT de Shinji, con cascos XBA-H3 y caja retro; 87.000 yenes | [ANN](https://www.animenewsnetwork.com/interest/2014-04-19/shinji-tape-player-gets-a-tech-upgrade-with-new-sony-walkman-f) · [Operation Rainfall](https://operationrainfall.com/2014/04/17/sony-evangelion-walkman-details/) ✅ |
| **Letra oficial EVA-Matisse** (Fontworks, 2016) | «EVA-Matisse Classic» (la de la serie) y «EVA-Matisse Standard» (la de las películas) | [ANN](https://www.animenewsnetwork.com/interest/2016-11-07/replicate-evangelion-stark-episode-titles-with-special-font-package/.108496) ✅ (**de pago**) |

- **Ojo con «la tarjeta de Rei»** (segunda pasada): el ep. 5 se miró
  minuto a minuto de 0:00 a 15:00 y **no hay un primer plano de la
  tarjeta en 4:25**. Ese tramo es un resumen técnico de la Unidad 00. Lo
  que sí se ve: la placa «402 綾波» en la puerta de Rei (13:12) y sus gafas
  rotas en el suelo (14:15). Para dibujar la tarjeta, usa las de reventa
  de arriba.

### 3.5 Lo que ya se vio (segunda pasada) ✅

Todo visto en las hojas de `investigar_serie.py`, con enlace a la imagen
original de la wiki:

- **Las 13 portadas de los laserdisc «Genesis 01-13»**, cada una con un
  personaje y su Eva, a **3660×3660** (por ejemplo
  [Genesis 06](https://static.wikia.nocookie.net/evangelion/images/e/e2/Genesis_06_LD.jpg)).
- **Hojas de personaje a color «Evangelion Chronicle»** de Shinji, Rei,
  Misato y Gendo.
- **Hojas de producción a lápiz** (決定稿, «versión final») de Rei, Asuka y
  Misato, con notas en japonés ⚠️ (el Tumblr de origen no dice de qué
  libro salen).
- **Portadas del manga** con Asuka y Rei; y la **enciclopedia de robots de
  Media Works** dibujada por Yamashita (5672×7108).
- **Figuras oficiales fotografiadas**: premios B y C del Ichiban Kuji del
  30 aniversario ([premio C](https://static.wikia.nocookie.net/evangelion/images/c/ca/Ichiban_Kuji_Neon_Genesis_Evangelion_30th_Anniversary_Prize_C.jpg))
  y la figura S-FIRE de Asuka sentada en la playa (Punto 23).
- **Portada de AniList** ([bx30](https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx30-AI1zr74Dh4ye.jpg)),
  al tamaño servido, no el de imprenta.
- Siguen **sin mirar** ⚠️: los pósteres de *The End of Evangelion* y de las
  *Rebuild*, y las carátulas de los Blu-ray.

---

## Las hojas de contacto

Tres hojas en `hojas/`, elegidas entre las 5 que dio
`investigar_serie.py` (se miraron las 5). Cada número de la hoja es una
imagen de la wiki; su original está en `referencias.json`.

| Hoja | Qué trae | Números que sirven | Para qué |
|---|---|---|---|
| `arte_oficial_01.jpg` (nº 1-48) | Portadas de laserdisc, key visual del *EVANGELION STORE TOKYO-01* (Rei y Asuka con el traje, nº 6), hojas «Evangelion Chronicle», calendarios, pósteres | **16-24** portadas de LD (personaje + su Eva, 3660×3660); **7-15** hojas de personaje a color; **36** Asuka con el uniforme; **41** Rei con el traje dañado; **26, 28, 34** Misato (con pistola en la 28) | Poses vivas con su Eva; color de referencia para la IA (§18) |
| `vestuario_pantallazos_02.jpg` (nº 49-96) | Ilustraciones de trajes, fotogramas de *The End of Evangelion* y de los ep. 1-2 | **53** Asuka de rojo cayendo, con Misato (póster de LD); **54** Rei de blanco tumbada; **55** Shinji señalando (portada de *Refrain*, Yamashita); **56** «The adults in NERV» (ropa de los adultos); **59** Gendo con pistola y gafas naranja; **71** **una tarjeta de identidad de NERV en la mano de Shinji** (*Rebuild*); **86** la sala de mando; **91** Misato con la lata «YEBISU» (ep. 2) | Vestuario (§16), el objeto del concepto A, fondos |
| `settei_figuras_03.jpg` (nº 97-144) | Hojas de producción a lápiz, arte promocional, figuras | **99** **pantalla «TEST PLUG-02 · HARMONICS TEST PROCEEDING · LIVE · SUBJECT: FIFTH C. KAWORU NAGISA»**; **104-112, 114-117, 119, 123, 127-130** hojas a lápiz (決定稿); **101** Shinji con el traje; **102** grupo de cinco; **133** arte del juego *Girlfriend of Steel 2*; **134-135** figuras de Rei y Shinji del Ichiban Kuji; **136** figura S-FIRE de Asuka en la playa | Línea (Punto 18), poses 3D (Punto 23), rótulo de pantalla del concepto A |

Las otras dos hojas (manga y pachinko/fondos de fans) quedaron fuera por
el límite de 3. Lo útil de ellas va enlazado en el Punto 19 (manga) y en
el Punto 23 (pachinko).

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D de objetos para la lámina (Sketchfab)

> [!note] Segunda pasada: licencias leídas en la API de Sketchfab
> El 26-sep-2026 se leyó la licencia exacta y las caras de cada modelo en
> `api.sketchfab.com/v3/search` (todos siguen descargables). **CC BY** =
> hay que dar crédito; **CC BY-SA** = crédito y compartir igual. Y ojo: el
> **diseño** de una Eva es de Khara aunque la malla sea libre. Úsalas como
> base o referencia de pose, nunca como producto oficial.

| Modelo | Autor | Para qué | Licencia |
|---|---|---|---|
| [Clipboard](https://sketchfab.com/3d-models/clipboard-a37158f20ccf436483029e8295629738) | Cookie (@cookiepop) | **La tablilla de la ficha de piloto** (2.256 caras) | **CC BY** ✅ |
| [Cello](https://sketchfab.com/3d-models/cello-d67ed4cbbc0c4477ba5d89413e715c82) | Lordricker | **El chelo de Shinji** (ep. 15; 134.552 caras) | **CC BY** ✅ |
| [Sony Walkman TPS-L2](https://sketchfab.com/3d-models/none-3cad4141c9aa4e67ba1d2ab1e5b9d277) | berilbaska | Base para el **SDAT** (el real es un Sony WMD-DT1, sin malla libre; 11.215 caras) | **CC BY** ✅ |
| [Asuka Langley Sohryu / Rig](https://sketchfab.com/3d-models/none-5e66c14e43164330a6dbd4bc863913f7) | JoeTrekV | **Asuka con esqueleto**, lista para posar (6.752 caras) | **CC BY** ✅ |
| [Evangelion - Eva 01 Rigged](https://sketchfab.com/3d-models/none-cec471affcb445cb9231bba50267191a) | najwanazhiim | Unidad 01 con esqueleto (873.951 caras, muy pesado) | **CC BY** ✅ |
| [Evangelion Unit-01](https://sketchfab.com/3d-models/none-9fddeb0a7143436598c805dab2f147bf) | allanromanreyes | Unidad 01; el autor tiene también la 00, 02, 03 y las de serie | **CC BY-SA** ✅ |
| [EVANGELION MARI (rigged)](https://sketchfab.com/3d-models/none-82bcdbde1483490f896418476b2c9d6f) | browniecoats | Mari con esqueleto (241.778 caras) | **CC BY** ✅ |
| [Gendo Ikari](https://sketchfab.com/3d-models/none-49a40e59a5b34ed7b34838027d573809) | 185684 | Busto de Gendo, pocos polígonos (1.598 caras) | **CC BY** ✅ |
| [Pen Pen - Rig](https://sketchfab.com/3d-models/none-7672ac8bd3454ff9aee30d270874d01d) | sirliks | Pen Pen con esqueleto | **CC BY** ✅ |
| [Sachiel](https://sketchfab.com/3d-models/none-3c212c7ce6ac4284a8b718078bc6fc0f) | solodovnykov | El primer Ángel que ataca Tokio-3 | **CC BY** ✅ |
| [Lilith](https://sketchfab.com/3d-models/none-c8c4c0f24f854f8084f8038a34057d9d) | solodovnykov | Lilith crucificada (dos versiones) | **CC BY** ✅ |
| [sony walkman 1985](https://sketchfab.com/3d-models/sony-walkman-1985-70984e9a3bb4497da196275feb343713) | milkmanfromhell | Base para modelar el **SDAT** | «Download Free» ⚠️ |
| [SONY WALKMAN](https://sketchfab.com/3d-models/sony-walkman-72e212b9f0894abbad50530f01a0adff) | rr025073 | Ídem | «Download Free» ⚠️ |
| [Walkman Cassete Player](https://sketchfab.com/3d-models/walkman-cassete-player-14daacbaf0f94f458851e15dfd717426) | Merow (@TehMerow) | Ídem | «Download Free» ⚠️ |
| [Evangelion - Entry Plug (with sound)](https://sketchfab.com/3d-models/evangelion-entry-plugwith-sound-3e4245a5f40b45eca02dab55e6b47a93) | Jongmin (@kingjongmin) | La cápsula del piloto | **de pago** (Sketchfab Store) |
| [Evangelion unit 01](https://sketchfab.com/3d-models/evangelion-unit-01-49c7a77272c84154a711d7cfd5cb47f4) | lefort | Unidad 01 para el 25 aniversario (2020) | la API no dio su licencia; mírala en la página ⚠️ |
| [EVANGELION Unit-01](https://sketchfab.com/3d-models/evangelion-unit-01-2bae40f88a494086a251cc63df100327) | aqua-blender | Unidad 01 | «Download Free» ⚠️ |
| [Eva Unit 01 Rigged](https://sketchfab.com/3d-models/eva-unit-01-rigged-a9c89d4df6b04818984cffd00cc5f634) | TitanGoji1954 | Unidad 01 con esqueleto (para posar) | «Download Free» ⚠️ |
| [Neon Genesis Evangelion Unit 01](https://sketchfab.com/3d-models/neon-genesis-evangelion-unit-01-2e0c150a4d864e838d1bed40b173ff8b) | lucaspitaperex | Unidad 01 | «Download Free» ⚠️ |

Más en las etiquetas [evangelion](https://sketchfab.com/tags/evangelion),
[walkman](https://sketchfab.com/tags/walkman),
[cello](https://sketchfab.com/tags/cello) y
[clipboard](https://sketchfab.com/tags/clipboard).

### 4.2 Renders y arte de fans (mirar, nunca pegar)

| Obra | Autor | Para qué |
|---|---|---|
| [Evangelion SDAT Walkman](https://www.artstation.com/artwork/gRq1gx) | Delphana Arts (Timothy Bryan), ArtStation | **Render 3D del SDAT**: medidas, botones, cable |
| [Misato - Neon Genesis Evangelion Fan Art](https://www.artstation.com/artwork/GvPEEd) | ArtStation | Misato con su chaqueta |
| [Misato Katsuragi (2v)](https://www.deviantart.com/sciamano240/art/Misato-Katsuragi-Evangelion-2v-1004695462) | Sciamano240, DeviantArt | Misato, pose de pie |
| [Asuka and Rei fanart](https://www.pixiv.net/en/artworks/78452459) | pixiv | Las dos juntas |
| [Etiqueta エヴァンゲリオン](https://www.pixiv.net/en/tags/%E3%82%A8%E3%83%B4%E3%82%A1%E3%83%B3%E3%82%B2%E3%83%AA%E3%82%AA%E3%83%B3) | pixiv (más de 65.000 dibujos) | Buscar poses |
| [Etiqueta evangelion](https://www.deviantart.com/tag/evangelion) | DeviantArt | Ídem |
| [Neon Genesis Evangelion Screen Graphics](https://www.behance.net/gallery/96540159/Neon-Genesis-Evangelion-Screen-Graphics) | Pedro Fleming (Behance, también en [su web](https://www.pedrofleming.com/neongenesisevangelion)) | **Recreación de las pantallas de NERV** |

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

| Sitio | Cómo es | Sitio real | Luz ⚠️ (de memoria) |
|---|---|---|---|
| **Tokio-3** | Ciudad fortaleza: los rascacielos **se esconden bajo tierra** cuando llega un Ángel | **Hakone** (Kanagawa): la caldera, el **lago Ashi**, Gōra, Sengokuhara ✅ ([SoraNews24](https://soranews24.com/2022/11/21/visiting-evangelions-tokyo-3-anime-locations-in-real-life-hakone%E3%80%90photos%E3%80%91/), [Tokyo Cheapo](https://tokyocheapo.com/entertainment/anime-and-gaming/hakone-evangelion/)) | **Verano eterno**: cielo azul fuerte, nubes altas, cigarras. Atardecer naranja |
| **Cuartel de NERV / GeoFront** | Una pirámide negra dentro de una caverna gigante con bosque y lago | — | Luz filtrada desde arriba, verde y dorada |
| **Sala de mando** | Varias plataformas en escalera frente a una pantalla enorme; detrás, **MAGI** | — | **Oscuridad** con el brillo **naranja** de las pantallas |
| **Laboratorio de pruebas** | Donde se hacen las **pruebas de sincronización**: cápsulas de prueba y cristal | — | Luz fría y blanca, cristal |
| **El piso de Misato** | Cocina con latas de cerveza, la nevera de **Pen Pen**, el cuarto de Shinji | — | Luz cálida de casa, de noche fluorescente |
| **La sala de SEELE** | Oscuridad total y **monolitos negros** numerados «SEELE 01…12» con **«SOUND ONLY»** ✅ ([EvaWiki](https://wiki.evageeks.org/SEELE), [Evangelion Wiki](https://evangelion.fandom.com/wiki/SEELE)) | — | Negro puro; los monolitos brillan cuando habla su dueño |
| **Estación de Ube-Shinkawa** | El final de *3.0+1.0*: estación de la ciudad natal de Anno | **Ube** (Yamaguchi) ✅ ([EvaWiki](https://wiki.evageeks.org/Ube-Shinkawa_Station), [GIGAZINE](https://gigazine.net/gsc_news/en/20231006-station-ube-city-evangelion/)) | Luz de mañana, real |

En Hakone hay de verdad cosas de NERV: en Sengokuhara, **un baño público
pintado como «puesto de NERV»**, y la estación de **Hakone-Yumoto** sale en
la serie (Shinji huye en tren) ✅
([Tokyo Cheapo](https://tokyocheapo.com/entertainment/anime-and-gaming/hakone-evangelion/),
[Japan City Tour](https://japancitytour.com/anime-evangelion-hakone/)).
En Ube pusieron una **mano de la Unidad 01 de 3,6 metros**
([Toy People](https://www.toy-people.com/en/?p=105251)).

### 5.2 Paleta

**Pantallas de NERV** (del proyecto de fans
[nerv-ui](https://github.com/TheGreatGildo/nerv-ui), licencia MIT; los
valores son suyos, no oficiales ⚠️):

| Color | Hex | Para qué |
|---|---|---|
| Negro de fondo | `#000000` / panel `#0C0C0A` | fondo de toda pantalla |
| **Naranja NERV** | `#FF9830` (apagado `#C87020`, vivo `#FFCC50`) | cabeceras, etiquetas, clasificación |
| Verde de datos | `#50FF50` | lecturas, estado normal |
| Cian de alambre | `#20F0FF` | mallas, datos espaciales |
| Rojo de alerta | `#FF3030` | **sólo** emergencias |
| Acero | `#D8D8D0` | texto secundario |

En emergencia, **todo el verde y el cian pasan a rojo** (lo describe
[Astromono en Medium](https://medium.com/astromono/the-amazing-ui-design-of-evangelion-de1126a7a85d)
y el mismo nerv-ui).

**Las Eva** (paletas de fans ⚠️ [color-hex 8250](https://www.color-hex.com/color-palette/8250)):
Unidad 01 morado `#765898` y verde `#52D053`; Unidad 02 rojo `#D3290F` y
naranja `#E6770B`. La marca «Evangelion» en productos usa amarillo `#F6E201`,
negro, blanco y naranja `#F66E25` ⚠️
([Brand Palettes](https://brandpalettes.com/neon-genesis-evangelion-color-codes/)).

**Cartelas**: blanco puro `#FFFFFF` sobre negro puro `#000000`. Nada más.

**Segunda pasada: colores medidos en fotogramas oficiales** ✅ (con
`estilo.py` sobre fotogramas vistos en Internet Archive; ya no son
paletas de fans):

| Sitio | Luz y hora | Hex medidos | Fotograma |
|---|---|---|---|
| **Jaula de las Eva** (la Unidad 01 encadenada) | Penumbra industrial | musgo `#3D4D2E`, oliva `#536347`, verde claro `#88A27E`, vigas `#0B0C03` | [ep. 1, 20:58](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=1258) |
| **Cápsula de entrada** (LCL) | Luz verdosa difusa | `#5E6146`, `#559671`, luz `#ECF3DD` | [ep. 1, 19:55](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=1195) |
| **Transporte a NERV** | Interior de metal, tapicería granate | `#141411`, `#544E29` | [ep. 1, 10:16](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=616) |
| **Tokio-3 al atardecer** (silueta de una Eva) | Tarde, ocre y dorado | `#967E2E`, `#403411`, cielo `#544E29` | opening, 1:00 |
| **La Unidad 02 de pie** | Fondo rojo | `#EA5E41`, `#96422E`, sombra violeta `#3A273E` | opening, 1:15 |
| **La luna del ending** | Noche | `#182032`, `#162F4C`, `#214868`, luna `#678E9C` / `#84A1A5` | ending, 0:20 |
| **Crucifixión** (*The End of Evangelion*) | Rojo de LCL | `#C5344A`, granate `#421E27`, hueso `#DECDD1` | [tráiler de GKIDS, 0:16](https://archive.org/download/youtube-JGcbdUgNYOY/JGcbdUgNYOY.mp4?t=16) |
| **Cielo del Tercer Impacto** | Rosa apocalíptico | magenta `#ED5AB9`, `#572145`, `#793662` | [tráiler de GKIDS, 0:32](https://archive.org/download/youtube-JGcbdUgNYOY/JGcbdUgNYOY.mp4?t=32) |

La paleta de pantallas de nerv-ui (arriba) sigue siendo de fans ⚠️; la de
esta tabla sí es de fotograma oficial. La columna «Luz» de §5.1 sigue de
memoria salvo en estos sitios.

### 5.3 Texturas reales equivalentes ⚠️

- **Papel de expediente** (la ficha): papel de oficina blanco algo
  amarillento, con clip y sello rojo. Por ejemplo
  [ambientCG «Paper 001»](https://ambientcg.com/view?id=Paper001).
  [ambientCG](https://ambientcg.com/), [Poly Haven](https://polyhaven.com/textures)
  y [TextureCan](https://www.texturecan.com/) son **CC0** o libres para uso
  comercial, sin crédito obligatorio ✅ (lo dicen sus webs y
  [CraftPBR](https://craftpbr.com/guides/free-pbr-textures)).
- **Plástico de tarjeta** (la tarjeta NERV): plástico blanco satinado, con
  reflejo suave.
- **Metal pintado y hormigón** (el cuartel): chapa gris con arañazos,
  hormigón con manchas de agua. Para el **verde oxidado de la jaula**:
  [ambientCG «Metal038»](https://ambientcg.com/view?id=Metal038), CC0 ✅.
- **Papel CC0 comprobado en la API de ambientCG** (segunda pasada):
  `Paper001`, `Paper003`, `Paper004`, `Paper005` y `Paper006`, con difuso,
  normal y rugosidad ✅.
- **Cristal de pantalla CRT** (la sala de mando): negro con líneas de
  barrido, ligero brillo curvo.

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia ✅

- **Cartelas de título** (el sello de la serie): **Matisse EB** de
  **Fontworks** (1994, diseñada con Shun Sato). Mincho extranegrita,
  **blanco sobre negro**, y **comprimida a mano** para encajar en
  composiciones que se entrelazan ✅
  ([Fonts In Use](https://fontsinuse.com/uses/28760/neon-genesis-evangelion),
  [Fontworks: entrevista «エヴァンゲリオンが証明した、フォントのチカラ»](http://route2015.evastore.jp/interview/01/3/)).
- **La composición en «L»** de los títulos es un homenaje a **Kon Ichikawa**
  (*La familia Inugami*); Anno lo ha reconocido. En la película de 1997 usó
  una versión aún más gruesa, **Matisse UB** ✅
  ([uakira: «市川崑のタイポグラフィ»](https://uakira.hateblo.jp/entry/20100726),
  [artículo académico en CiNii](https://cir.nii.ac.jp/crid/1390009224766565504),
  [Excite](https://www.excite.co.jp/news/article/E1282847996176/)).
- El estudio de CiNii dice que Anno **fue cambiando su forma de componer**
  y que su estilo propio se asienta **hacia el episodio 16** ⚠️ (una fuente, por
  el resumen de búsqueda).
- **Resto de letras** (según Fonts In Use y la guía de cuadros):
  **Helvetica** en mayúsculas en interfaces y títulos en inglés; **Times
  comprimida** en los episodios 12, 26 y 26'; **Chicago** en los números de
  los monolitos «SOUND ONLY»; Eurostile y Futura en detalles de Tokio-3.
- **Letra oficial de pago**: «EVA-Matisse Classic» y «EVA-Matisse Standard»,
  Fontworks, 2016 ✅
  ([ANN](https://www.animenewsnetwork.com/interest/2016-11-07/replicate-evangelion-stark-episode-titles-with-special-font-package/.108496)).
  **No uses** las copias piratas que circulan (hay una en Internet Archive).

### 6.2 Letras libres comprobadas por mí

Bajadas de [google/fonts](https://github.com/google/fonts) y comprobadas con
fontTools. **Todas** traen á é í ó ú ñ ¿ ¡ (y Á É Í Ó Ú Ñ ü). Todas son
**OFL** (libres, también para uso comercial).

| Letra (Google Fonts) | Sustituye a | Pesos | ¿Japonés? | Nota |
|---|---|---|---|---|
| **Shippori Mincho B1** | Matisse EB (cartelas) | hasta **ExtraBold** | sí | La mejor para kanji. Estírala a lo alto |
| **Zen Old Mincho** | Matisse EB | hasta **Black** | sí | Más gruesa que Shippori: más «Eva» |
| **Noto Serif JP** | Matisse EB | variable 200-**900** | sí | Black 900 para el golpe |
| **Kaisei Tokumin** | Matisse EB | hasta ExtraBold | sí | Mincho de titular, con contraste |
| **Noto Serif Display** | Matisse / Times comprimida (texto latino) | variable 100-900, **ancho 62,5-100** | no | **Trae su propio eje de ancho**: a 62,5 sale comprimida sin deformar. La mejor para el español |
| **Tinos** | Times | 4 | no | Métricas de Times |
| **Arimo** | Helvetica | variable | no | Métricas de Helvetica |
| **Archivo Narrow** / **Roboto Condensed** | Helvetica Condensed (interfaz) | variable | no | Datos de pantalla |
| **Michroma** | Eurostile ancha | 1 | no | Rótulos técnicos |
| **JetBrains Mono** / **Share Tech Mono** | texto de terminal de MAGI | variable / 1 | no | Datos |
| **Saira Extra Condensed** | sellos de «WARNING» | hasta Black | no | Avisos |
| **DotGothic16** | pantallas de pocos píxeles | 1 | sí | Para un contador o reloj |

**Chicago** (números de SEELE): no hay equivalente en Google Fonts. La
recreación libre **«ChiKareGo2»** (Creative Commons ⚠️, una fuente) se
bajó de [GitHub](https://github.com/lowercasename/helloedit/blob/master/resources/fonts/ChiKareGo2.woff)
y se pasó por fontTools en la segunda pasada ✅: **trae** á é í ó ñ Ñ Á É Í
Ó Ú Ü ¿ ¡; **le faltan ú y ü minúsculas**. Sirve para «SEELE 01» o «SOUND
ONLY» (todo en mayúsculas); si un texto lleva «ú», escríbelo en versalitas
o usa otra letra. Descripción de la letra:
[suppertime.co.uk](http://www.suppertime.co.uk/blogmywiki/2017/04/chicago/).

**Receta de cartela** (la que usa también nerv-ui): letra serif muy negra,
**comprimida al 78-85 % de ancho** (`scaleX(0.78–0.85)`), blanca sobre negro,
sin sombra ni borde.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que la serie pone en pantalla

1. **La cartela negra** ✅. Pantalla completa, fondo negro, letras blancas
   en mincho extranegrita comprimida. Se usa para:
   - el **título del episodio** (en japonés grande y en inglés debajo ⚠️);
   - **monólogos interiores** y preguntas («¿Por qué pilotas el Eva?»),
     sobre todo en los episodios 25 y 26;
   - **avisos** y lugares.
   Anno la usa para cortar la escena en seco: **una idea, un golpe**.
   Es el cuadro de diálogo de la franquicia (ver la guía
   `biblias/_ya_hechas/_Cuadros de dialogo por franquicia (23-sep-2026).md`,
   apartado 21).
2. **Las pantallas de NERV** ✅: fondo negro, **hexágonos** y cuadros de
   estado naranjas, datos en verde, alambres en cian y **«EMERGENCY»** en rojo
   ([gist «Emergency hexagons»](https://gist.github.com/6b24ac6705298b2dba7a),
   [nerv-ui](https://github.com/TheGreatGildo/nerv-ui)). Las palabras salen
   **en inglés y en mayúsculas**: «REFUSED», «ACCEPTED», «EMERGENCY» ⚠️
   (de memoria).
3. **Los monolitos de SEELE** ✅: losas negras que sólo dicen **«SEELE 01 …
   SOUND ONLY»**. Los miembros **no enseñan la cara: sólo la voz**. Para un
   canal de demos de voz es una metáfora exacta.
4. **El logo de NERV** ✅: media **hoja de higuera** junto a la palabra
   **NERV**, y debajo la frase de Browning **«God's in his heaven, all's
   right with the world.»** En las *Rebuild* cambian la «V» y la hoja, y a
   veces va sobre **una manzana invertida**
   ([EvaWiki: Nerv Logo](https://wiki.evageeks.org/Nerv_Logo),
   [Evangelion Wiki: NERV](https://evangelion.fandom.com/wiki/NERV),
   [NERV Archives](http://www.nervarchives.com/glossary.nerv.php)). Va en
   todo lo oficial de NERV: tarjetas, carpetas, uniformes.
5. **Los papeles y las tarjetas** ✅: la **ficha** que Ritsuko lee en voz alta
   (ep. 5), la **tarjeta de seguridad con foto** (ep. 5), los **papeles
   oficiales** que llegan al día siguiente (ep. 17), el **folleto de NERV**
   que Misato da a Shinji (ep. 1). Todo en §2.
6. **El avance del próximo episodio** ✅: Misato lo narra y siempre acaba
   con «この次も サービス サービス！» (ep. 1, 3, 8, 9, 12, 13, 00:23:19).
7. **El manga** ⚠️: globos redondos normales, texto japonés vertical. No
   tiene un globo propio reconocible; lo reconocible es la cartela y la
   pantalla. Segunda pasada: el análisis de
   [AIPT Comics](https://aiptcomics.com/2021/02/04/revisiting-sadamotos-evangelion-manga-p1/)
   habla de sus **viñetas que se estrechan hacia el centro** y de su
   línea afilada, pero no de un globo especial. Hay páginas del manga en
   la hoja `settei_figuras_03.jpg` (nº 132 y 143) y en las hojas que no se
   subieron (nº 146-152), con trama de puntos; el globo sigue sin
   comprobarse de cerca.
8. **Las pantallas de prueba con nombre** ✅ (visto en la hoja
   `settei_figuras_03.jpg`, nº 99): rótulo naranja **«TEST PLUG-02 ·
   HARMONICS TEST PROCEEDING · LIVE»** arriba a la izquierda y abajo
   **«SUBJECT : FIFTH C. · KAWORU NAGISA»**. Es la ficha en pantalla de un
   piloto durante una prueba: el formato exacto para una ficha de voz.
9. **Los juegos** (§13): *Girlfriend of Steel* y sus secuelas son novelas
   visuales con retrato y caja de diálogo abajo ⚠️ (descripción, sin
   captura: The Cutting Room Floor no abre). Arte del juego 2 en la hoja
   `settei_figuras_03.jpg`, nº 133.

### 7.2 Cómo hablan (por el subtítulo)

- **Misato**: habla a los chicos como una hermana mayor. Pide que la tuteen
  («“ミサト”でいいわよ», ep. 1, 00:06:20), se burla con cariño («レイの写真を
  ジーッと見ちゃったりして», ep. 5), celebra en inglés macarrónico («ハ〜イ
  ユーアー ナンバーワン！», ep. 16). Por radio, **siempre pregunta primero**:
  «聞こえる？ シンジ君» (¿Me oyes, Shinji?).
- **Ritsuko**: técnica y seca, **lee datos** en frases cortas: nombre, edad,
  unidad, estado (ep. 5, 00:04:25). Pero **da ánimo con números**: «10日で8よ
  大したものだわ» (ep. 12).
- **Asuka**: se presenta **con su rango completo** (ep. 8, 00:03:46),
  insulta con «あんたバカ？», saluda en inglés y alemán («ハロー シンジ！
  グーテンモルゲン», ep. 9, 00:02:24; «ハロー ミサト 元気してた？», ep. 8,
  00:03:30) y se pica cuando alguien la supera (ep. 16).
- **Shinji**: tartamudea, se disculpa por reflejo (Asuka se lo dice en el
  ep. 16, 00:02:01: «条件反射的に謝ってる»), y se repite frases para darse
  valor («逃げちゃダメだ»).
- **Rei**: frases mínimas, sin adornos: «何？» (¿Qué?), «さよなら» (Adiós).
- **Gendo**: órdenes secas. «説明を受けろ» (Que te lo expliquen), «乗るなら早く
  しろ でなければ帰れ». Casi no mueve la boca.
- **Kaworu**: amable, poético, llama a la gente por su nombre y la invita a
  tutearlo («カヲルでいいよ»). Habla de **música** y de **cultura**.

### 7.3 Cómo se traduce a una lámina fija

- **Título del canal** = **cartela negra** con letras blancas comprimidas.
  Es lo más reconocible de toda la serie. No lleva marco ni bocadillo.
- **Lo que dice el personaje** = **una línea de subtítulo** o **una cartela
  pequeña** al lado, nunca un globo blanco. Si hace falta que sea «voz»,
  se puede poner como el **monolito «SOUND ONLY»**: el texto en una losa
  negra con el número y el nombre.
- **Los datos** (demos, rango vocal, etiquetas) = **la ficha** en papel o
  **la pantalla de NERV** (naranja y verde sobre negro).
- **La lámina 2** (etiquetas) = un **panel de estado** con bloques
  hexagonales naranjas, uno por etiqueta; «Disponible» en verde y
  «Ocupado» en rojo.

### 7.4 Qué NO hacer con el texto

- **Nada de globos blancos redondos.** La serie no los usa para marcar
  identidad.
- **Nada de mincho sin comprimir** ni de mincho fina: la fuerza está en
  que sea **negrísima y apretada**.
- **Nada de cartelas de color** (roja, azul): son **blanco sobre negro**.
- **Nada de letras «futuristas»** redondas (tipo Orbitron) en el título. En
  1995 la ciencia ficción usaba sans; Anno eligió serif a propósito.
- En las pantallas, **el rojo sólo para alertas**. Si todo es rojo, deja de
  significar «emergencia».

---

## 8 · Los personajes

> [!note] Cómo está hecho este apartado
> Lo que va **con minuto** sale del subtítulo ✅. La historia y el carácter
> los resumo de memoria ⚠️, contrastados con los resúmenes de búsqueda
> (wikis en inglés, español, chino y coreano). Los tres doblajes latinos,
> en §10.

### Asuka Langley Soryu (惣流・アスカ・ラングレー) — la más votada ✅

- **Quién es**: la **Second Children**, piloto de la **Unidad 02** (roja).
  Llega de Alemania en el ep. 8. 14 años, y ya fue a la universidad allí
  («向こうの大学じゃ習ってなかったし», ep. 10, 00:05:39 ✅).
- **Carácter**: orgullosa, competitiva, ruidosa. **Necesita ser la mejor y
  que la miren**. Por dentro, miedo a que nadie la quiera y a acabar como
  su madre ⚠️. Se derrumba cuando Shinji la supera (ep. 16, 00:03:23:
  «あ〜っさり 抜かれちゃったじゃなぁい»).
- **Cómo habla**: «あんたバカ？» a todo el mundo (ep. 8, 9, 11, 12, 15, 20
  ✅). «バカシンジ» (ep. 20). Saluda en inglés y alemán («ハロー シンジ！
  グーテンモルゲン», ep. 9, 00:02:24). **Se presenta con su título entero**
  (ep. 8, 00:03:46). Presume: «見て見て シンジ！ バックロール・エントリー！»
  (¡Mira, mira, Shinji! ¡Entrada de espaldas!, ep. 10, 00:06:33).
- **Cómo se ríe / se enfada**: carcajada de superioridad, manos en la
  cintura ⚠️; cuando se enfada, **da la espalda** o **abofetea** (ep. 8,
  00:04:06, «何すんのよ！» tras la bofetada ✅).
- **Con quién**: pelea con **Shinji** (convive con él desde el ep. 9),
  admira a **Kaji**, **se burla de Rei** llamándola «優等生» (la
  empollona, ep. 11, 00:12:14 ✅), trata a Misato
  como a una igual.
- **Lo que le importa**: ganar, ser adulta, que la reconozcan.
- **Para #demos**: la que **se presenta con orgullo** y la que **mira las
  fichas de los demás** («で ウワサのサードチルドレンは どれ？»). Buena para
  «presentar» y «retar». Mala para «dar la bienvenida con cariño».

### Kaworu Nagisa (渚カヲル) — el 2.º más votado ✅

- **Quién es**: el **Fifth Children**. Sale **en un solo episodio** (el 24)
  y aun así es el segundo más votado. Su ficha está borrada y **nació el día
  del Segundo Impacto** (ep. 24, 00:06:03 ✅). Es el último Ángel ⚠️.
- **Carácter**: sereno, amable, sonriente, curioso por los humanos.
  **Habla de música y de cultura**. Es el único que le dice a Shinji que
  le quiere («好意に値するよ … 好きってことさ», ep. 24, 00:09:35 ✅).
- **Cómo habla**: suave, frases largas y poéticas; tutea enseguida
  («カヲルでいいよ 碇君», 00:05:46); llama «リリン» a los humanos.
- **Cómo se ríe**: una risa corta y tranquila («アッ ハハ», 00:05:51).
- **Gesto**: **tararea el «Himno de la alegría»** sentado sobre una estatua
  en ruinas junto al lago ⚠️ (ep. 24, 00:04:55).
- **Para #demos**: **el mejor gancho de voz**: «歌はいいね». Da la
  bienvenida con calma. Perfecto para «animar» y «presentar».

### Rei Ayanami (綾波レイ) — la 3.ª más votada ✅ y la frase n.º 1 ✅

- **Quién es**: la **First Children**, piloto de la **Unidad 00**. Su
  historial está **en blanco** (ep. 5, 00:04:38). Vive sola en un piso
  vacío.
- **Carácter**: callada, obediente a Gendo, sin saber qué sentir. Va
  aprendiendo a sonreír (ep. 6). Protege a Shinji.
- **Cómo habla**: **frases de una o dos palabras**: «何？» (ep. 5, 00:15:55),
  «さよなら» (ep. 16, 00:03:49), «絆だから … そう 絆» (Porque es un vínculo,
  ep. 6, 00:16:25). Nunca grita.
- **Su frase más votada**: «あなたは死なないわ 私が守るもの» (No morirás. Yo
  te protegeré), ep. 6, **00:15:32** ✅. Es la **n.º 1 del voto de NHK** ✅.
- **Gesto**: quieta, mirada al frente, manos a los lados ⚠️. La sonrisa del
  ep. 6 (00:21:35) es su momento más querido.
- **Para #demos**: la ficha en sí (su ficha se lee en voz alta, ep. 5).
  Buena para «explicar» con pocas palabras. Mala para «celebrar».

### Shinji Ikari (碇シンジ) — el protagonista, 4.º ✅

- **Quién es**: el **Third Children**, piloto de la **Unidad 01**. Su padre
  le llama después de tres años sin verse (ep. 1, 00:12:25).
- **Carácter**: inseguro, se disculpa por todo («条件反射的に謝ってる», le
  dice Asuka, ep. 16, 00:02:01). Miedo a que le rechacen. Quiere que le
  digan que lo hace bien, pero **cuando le elogian no se lo cree** (ep. 12,
  00:06:05: «褒められても あまり うれしくないし»).
- **Lo que hace**: **toca el chelo** desde los 5 años (ep. 15, 00:11:40) y
  **escucha su SDAT** para aislarse (ep. 2, 00:16:16; ep. 9, 00:15:16).
- **Cómo habla**: bajito, con puntos suspensivos, tartamudea (ep. 5,
  00:16:11). Se da valor repitiendo «逃げちゃダメだ».
- **Para #demos**: **es el novato que sube su primera demo**: «才能なんて
  別にないよ» (No tengo talento). Una lámina con él dice «no pasa nada, súbela
  igual».

### Misato Katsuragi (葛城ミサト) — 5.ª ✅

- **Quién es**: jefa de operaciones de NERV. Capitana, luego **mayor**
  (ascenso en el ep. 12, 00:04:11 ✅). Tutora de Shinji y Asuka.
- **Carácter**: alegre y desordenada en casa, dura y seria en el trabajo.
  Bebe cerveza sin parar («プッハー!! くぅ〜！ … やっぱ人生 このときのために
  生きてるようなもんよね〜», ep. 2, 00:13:14 ✅). Esconde un trauma del
  Segundo Impacto ⚠️.
- **Cómo habla**: cercana, de hermana mayor: «“ミサト”でいいわよ» (ep. 1,
  00:06:20). **Por radio empieza con «聞こえる？»** (ep. 16, 00:03:14).
  Celebra fuerte: «ハ〜イ ユーアー ナンバーワン！». **Explica planes** paso a
  paso: el de la **Operación Yashima** (ep. 6, 00:09:20 → 00:09:26) y el del
  **unísono** (ep. 9, 00:11:03).
- **Con quién**: Pen Pen (su pingüino), Ritsuko (amiga), Kaji (ex), Shinji
  y Asuka (casi hijos).
- **Para #demos**: **la mejor para explicar el canal**. Es la que da el
  folleto («じゃあ これ 読んどいてね», ep. 1, 00:10:16), la que lee fichas
  (ep. 24, 00:05:58) y la que celebra resultados. Y cierra con «サービス
  サービス！».

### Gendo Ikari (碇ゲンドウ) — el comandante

- **Quién es**: comandante de NERV, padre de Shinji.
- **Carácter**: frío, calculador, lejano. Sólo habla de lo necesario.
  Detrás, la obsesión por volver a ver a su mujer, Yui ⚠️.
- **Cómo habla**: órdenes secas. «乗るなら早くしろ でなければ帰れ！» (ep. 1,
  00:15:38). «問題ない» (No hay problema, ep. 1, 00:09:48; ep. 14,
  00:21:17). «全ては心の中だ» (Todo está en el corazón, ep. 15, 00:10:26).
- **La pose**: **sentado, codos en la mesa, manos juntas delante de la
  boca, gafas que brillan** (la «pose Gendo», meme mundial ✅,
  [Know Your Meme](https://knowyourmeme.com/memes/gendo-pose)). Ojo: en
  el plano de las gafas del ep. 1 (15:38) **no** tapa la boca con las
  manos; esa pose hay que sacarla de otro fotograma o del arte oficial ⚠️.
- **Para #demos**: sólo para **la norma seca** (p. ej. «Un hilo por
  persona»). Nunca para dar la bienvenida.

### Los secundarios que conviene tener a mano

| Personaje | Por qué | Frase o escena |
|---|---|---|
| **Ritsuko Akagi** | Científica jefe. **Lee las fichas y evalúa las pruebas**: es la «jurado» de las demos | ep. 5, 00:04:25 (lee los datos de Rei; **en pantalla** no se ve una ficha, sino diagramas de la Unidad 00, visto en la segunda pasada); ep. 12, 00:05:22 («よくやったわ») |
| **Maya Ibuki** | La que **canta los datos** en la sala de mando | ep. 1, 00:19:58 («シンクロ率 41.3パーセント») |
| **Makoto Hyūga** | Operador; lee datos de Kaworu y **se cuela en archivos** | ep. 24, 00:06:03 |
| **Pen Pen** | El pingüino de Misato. Mascota del fandom | ep. 2, 00:15:05 («名前は ペンペン») |
| **Ryōji Kaji** | Espía encantador; cultiva sandías | ep. 17, 00:21:02 |
| **Mari Makinami** | Sólo en las *Rebuild*. Canta mientras pilota ⚠️ | (no está en la serie de TV) |
| **Toji Suzuhara** | El **Fourth Children**; su ficha sale en el ep. 17 | ep. 17, 00:21:24 |

### Su cara en cada emoción (fotogramas vistos en la segunda pasada)

Sacados de Internet Archive y mirados uno a uno. El ítem
`evangelion-the-full-series` trae los 26 episodios en 1080p con el corte
japonés, así que su minuto coincide con el de este dossier. El ítem de
Toonami es una grabación de TV con anuncios: su minuto es **el de la
grabación**, no el del episodio.

| Personaje | Emoción | Cómo se ve | Episodio y minuto |
|---|---|---|---|
| Asuka | **Rabia / vergüenza** | Cara roja, boca muy abierta gritando «何すんのよ！» | [ep. 8, 00:04:04](https://archive.org/download/evangelion-the-full-series/1.70A%20Neon%20Genesis%20Evangelion%20-%20Episode%208%20%28SUB%29%201920x1080%20-%20Asuka%20Arrives%20in%20Japan.mp4?t=244) ✅ |
| Asuka | **Presentarse** | De pie, barbilla alta, carpeta en la mano | [ep. 8, 3:46](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2008%20Asuka%20Strikes%21%20%5BC6590C43%5D.mp4?t=226) ✅ |
| Misato | **Alegría** | Ojos cerrados, sonrisa enorme, bebiendo cerveza | [ep. 2, 00:13:14](https://archive.org/download/evangelion-the-full-series/1.10A%20Neon%20Genesis%20Evangelion%20-%20Episode%202%20%28SUB%29%201920x1080%20-%20Unfamiliar%20Ceilings.mp4?t=794) ✅ |
| Kaworu | **Ternura** | Media sonrisa cálida, luz de atardecer, mirando a Shinji | [ep. 24, 00:05:40](https://archive.org/download/evangelion-the-full-series/3.30A%20Neon%20Genesis%20Evangelion%20-%20Episode%2024%20%28SUB%29%201920x1080%20-%20The%20Last%20Cometh.mp4?t=340) ✅ |
| Rei | **La sonrisa rara** | Primer plano en la cápsula, mirada de lado, sonrisa pequeña | [ep. 6, 21:45](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2006%20Rei%20II%20%5B6F5224E2%5D.mp4?t=1305) ✅ |
| Rei | **Dolor** | Cabeza vendada, ojos entrecerrados | [Toonami, 20:30 de la grabación](https://archive.org/download/neon-genesis-evangelion-toonami-rip/Neon%20Genesis%20Evangelion%20Toonami%20Rips.mp4?t=1230) ✅ |
| Shinji | **Miedo** | Ojos muy abiertos, sudor, boca tensa | [Toonami, 41:00 de la grabación](https://archive.org/download/neon-genesis-evangelion-toonami-rip/Neon%20Genesis%20Evangelion%20Toonami%20Rips.mp4?t=2460) ✅ |
| Shinji | **Valor** | Sólo el ojo y el pelo, dientes apretados («no debo huir») | [ep. 1, 18:33](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=1113) ✅ |
| Ritsuko | **Alarma** | Cejas fruncidas, boca abierta gritando | [Toonami, 20:15 de la grabación](https://archive.org/download/neon-genesis-evangelion-toonami-rip/Neon%20Genesis%20Evangelion%20Toonami%20Rips.mp4?t=1215) ✅ |
| Gendo | **Frialdad** | Primerísimo plano de las gafas con el carnet de Shinji reflejado dos veces | [ep. 1, 15:38](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=938) ✅ |

Faltan con fotograma propio ⚠️: la tristeza y la vergüenza de Shinji y
de Misato, y cualquier emoción de Gendo que no sea frialdad.

---

## 9 · ¿Quién es el más querido?

### 9.1 El voto oficial: «発表！全エヴァンゲリオン大投票» (NHK, 2020) ✅

NHK BS Premium hizo un **voto nacional** del 27-mar al 29-abr-2020 con
**109.577 votos**, y lo emitió el 16-may-2020
([Famitsu](https://www.famitsu.com/news/202005/16198567.html),
[MANTANWEB](https://mantan-web.jp/article/20200517dog00m200000000c.html),
[Wikipedia JA](https://ja.wikipedia.org/wiki/%E7%99%BA%E8%A1%A8!%E5%85%A8%E3%82%A8%E3%83%B4%E3%82%A1%E3%83%B3%E3%82%B2%E3%83%AA%E3%82%AA%E3%83%B3%E5%A4%A7%E6%8A%95%E7%A5%A8)):

| Puesto | Personaje | Estado |
|---|---|---|
| 1 | **Asuka** | ✅ (Famitsu, MANTANWEB) |
| 2 | **Kaworu** | ✅ ([Kimigaku](https://kimigaku.jp/archives/388/), [SMZDM, en chino](https://post.smzdm.com/p/alpw8g5e/)) |
| 3 | **Rei** | ✅ (las mismas) |
| 4 | Shinji | ✅ (segunda pasada: [Kimigaku](https://kimigaku.jp/archives/388/) da el mismo orden 1-5) |
| 5 | Misato | ✅ (la misma) |
| 7 | Kaji | ⚠️ una fuente |

**Frases más votadas** ✅ (Famitsu y MANTANWEB):
1. «……いいえ、あなたは死なないわ、私が守るもの» (Rei) → ep. 6, 00:15:32.
2. «……笑えばいいと思うよ» (Shinji) → ep. 6, 00:21:35.
3. «……逃げちゃダメだ。やります。僕が乗ります» (Shinji) → ep. 1, 00:18:33.

Otros datos del mismo voto: Eva favorita, la **Unidad 01**; Ángel
favorito, **«el 6.º»** ✅ (título de Famitsu). ⚠️ Ojo con la cuenta: en las
*Rebuild* el 6.º es **Ramiel** (el octaedro azul); en la serie de TV el 6.º
es Gaghiel (el pez). No sé cuál de las dos cuentas usó NHK.

### 9.2 Otros votos

- **Anime Grand Prix de Animage**: **Rei** ganó personaje femenino en 1995 y
  1996; **Shinji**, masculino en 1996 y 1997 ⚠️ (una fuente, resumen de
  wiki). Rei fue **la cara de los 90**.
- **Voto de las películas *Rebuild*** (Nlab / ITmedia): 1.ª **Asuka
  Shikinami** ✅ ([ねとらぼ](https://nlab.itmedia.co.jp/research/articles/88497/)).
- **Voto de *Shin Evangelion*** (rankingoo): 1.ª **Rei**, con más de 1.100
  votos ⚠️ ([rankingoo](https://rankingoo.net/articles/comic/00096a)).
- Otros de fans: [Anime!Anime! (2023)](https://animeanime.jp/article/2023/06/10/77844.html)
  (Shinji y Kaworu empatados 3.º), [みんなのランキング](https://ranking.net/rankings/best-eva-characters),
  [All About](https://news.allabout.co.jp/articles/o/63728/) (2.ª Asuka).
- En China también se discute **«Asuka contra Rei»**
  ([Zhihu](https://zhuanlan.zhihu.com/p/131678834),
  [Zhihu 2](https://www.zhihu.com/question/372082399)): la conclusión común
  es que **Rei reinó en los 90 y Asuka manda hoy**.
- **El 30 aniversario lo protagoniza Asuka**: el **corto de 14 minutos y
  medio** que se estrenó en la fiesta «EVANGELION:30+;» (Yokohama Arena,
  21-23 de febrero de 2026) es **de Asuka**; Khara lo subió gratis a su
  YouTube el **8 de marzo de 2026** y tuvo **más de 2,5 millones de vistas
  en 24 horas** ✅ ([evangelion.jp](https://www.evangelion.jp/news/260307-2/),
  [Famitsu](https://www.famitsu.com/article/202603/68082),
  [Denfaminicogamer](https://news.denfaminicogamer.jp/news/260307g),
  [Dengeki](https://dengekionline.com/article/202603/68081)).

### 9.3 Qué significa para la lámina

- **Asuka** es la más querida hoy y la cara del 30 aniversario.
- **Kaworu** es el secundario (sale en un solo episodio) que supera a Rei,
  la heroína de los 90, y a Shinji, el protagonista: justo el caso que pide
  el dueño. Y **su frase va
  de música**.
- **Misato** no gana votos, pero es **la que explica** en la serie.
- **Recomendación**: Asuka o Kaworu como cara; Misato como la voz que
  explica.

### 9.4 Otras dos medidas (segunda pasada) ✅

| Personaje | Favoritos en [AniList](https://anilist.co/anime/30) (todo el mundo) | Dibujos de fans en [Danbooru](https://danbooru.donmai.us/posts?tags=neon_genesis_evangelion) |
|---|---|---|
| Asuka | **14.666** | **17.588** |
| Rei | 11.549 | 10.518 |
| Shinji | 11.348 | 6.470 |
| Misato | 10.981 | 2.105 |
| Kaworu | 5.450 | 4.666 |
| Kaji | 1.019 | — |
| Ritsuko | 925 | — |
| Gendo | 729 | — |
| Mari (sólo *Rebuild*) | — | 2.833 |

**Asuka gana en las tres medidas** (voto de NHK, favoritos, fan art): es
la apuesta más segura. Kaworu gana a Misato en fan art igual que en NHK,
aunque sale en un solo episodio. En AniList, Rei pasa a Kaworu: fuera de
Japón pesa más la heroína de los 90. El ranking numérico de MyAnimeList
no se encontró ⚠️.

---

## 10 · Doblaje latino

**Sí hay doblaje latino. Hay tres de la serie**, y otro de las películas
*Rebuild*. Esto importa para un servidor de doblaje: **el fandom latino
discute cuál es «el bueno»** (hay hilos enteros: [foros eldoblaje](https://www.foroseldoblaje.com/foro/viewtopic.php?t=69136&start=20),
[grupo de Facebook](https://www.facebook.com/groups/1261902114792639/posts/1368629127453270/),
[Atamashi: «Fans se quejan por el doblaje latino»](https://atamashi.net/38153-2/)).

En la primera pasada la API de Doblaje Wiki daba 403 y los nombres
salieron de extractos de búsqueda. **En la segunda pasada sí se leyó el
wikitext** de las fichas [Neon Genesis Evangelion](https://doblaje.fandom.com/es/wiki/Neon_Genesis_Evangelion)
y [Renewal of Evangelion](https://doblaje.fandom.com/es/wiki/Renewal_of_Evangelion)
por la API, y se cruzó con [AniList](https://anilist.co/anime/30).

### 10.1 Los tres doblajes de la serie

| Doblaje | Dónde se vio | Estudio y dirección | Estado |
|---|---|---|---|
| **1.º, el original** | **Locomotion**, estreno el **1 de noviembre de 1999**, un año en exclusiva | Dirección de **Enrique Cervantes** ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Neon_Genesis_Evangelion), por extracto). Estudio **Roman Sound** ✅ (la guía de cuadros y [Dub Database](https://dubdb.fandom.com/wiki/Neon_Genesis_Evangelion_(Latin_American_Spanish,_Roman_Sound))) | ✅ |
| **2.º, *Renewal of Evangelion*** | **Animax** ✅ (Internet Archive y Dub Database lo llaman «Latino Animax») | **Grabaciones y Doblajes Internacionales**, dirección de **Gerardo García**, grabado en **2007** y emitido en **2008** ⚠️ (segunda pasada; sólo lo dice [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Renewal_of_Evangelion), no hallé otra fuente). Su reparto (Georgina Sánchez, Marisol Romero) **pasó al de Netflix** | ✅ |
| **3.º, Netflix** | Netflix, **21 de junio de 2019** | **Audiomaster Candiani** (producción de VSI Group), dirección de **América Torres**, traducción de **Andrés Magos** ✅ ([Cine Premiere](https://cinepremiere.com.mx/neon-genesis-evangelion-netflix-doblaje.html), [Xataka México](https://www.xataka.com.mx/streaming/neon-genesis-evangelion-llega-a-netflix-tercer-doblaje-latino-para-mexico-estas-nuevas-voces-personajes), [Spoiler Time](https://spoilertime.com/noticia/evangelion-nuevo-doblaje/)) | ✅ |

**Rasgos del doblaje original** ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Neon_Genesis_Evangelion), por extracto; y la guía de cuadros):
- Usa **«amigo» y «amiga» sin parar**, de relleno, para cuadrar el
  movimiento de labios. Es lo que más recuerda el fandom.
- Dicen **«Evanjelion»** (con jota) y **«Langlu»** en vez de «Langley» ⚠️
  (una fuente).
- El hermano de **Norma Echevarría** (la Asuka original) hablaba alemán y
  les **asesoró con el alemán de Asuka** (lo cuenta Enrique Cervantes) ⚠️
  (una fuente).

### 10.2 Quién dobla a quién

| Personaje | Original (Locomotion, 1999) | Netflix (2019) | *Rebuild* (Prime Video, 2021) |
|---|---|---|---|
| **Shinji Ikari** | **Víctor Ugarte** ✅ | **Víctor Ugarte** ✅ | **Víctor Ugarte** ✅ |
| **Rei Ayanami** | **Circe Luna** ✅ | **Circe Luna** ✅ | **Circe Luna** ✅ |
| **Asuka Langley** | **Norma Echevarría** ✅ (fallecida) | **Georgina Sánchez** ✅ (ya la hizo en *Renewal*) | **Georgina Sánchez** ✅ |
| **Misato Katsuragi** | **Toni Rodríguez** ✅ (1969-2021) | **Marisol Romero** ✅ (ya la hizo en *Renewal*, Animax) | **Luciana Falcón** ✅ |
| **Gendo Ikari** | **Humberto Solórzano** ✅ (segunda pasada: Doblaje Wiki por la API y [AniList](https://anilist.co/character/1257)); repite en *Renewal* | **Idzi Dutkiewicz** ✅ (Tony Stark, Toretto, Hit) | **Javier Gómez** ⚠️ |
| **Kaworu Nagisa** | **Ernesto Lezama** ✅ (retirado) | **Alberto Bernal** ✅ | **Federico Llambí** ✅ |
| **Ritsuko Akagi** | **Maru Guerrero** ✅ (Doblaje Wiki y [AniList](https://anilist.co/character/1251)) | **América Torres** ✅ (la directora) | **Noelia Socolovsky** ⚠️ |
| **Kōzō Fuyutsuki** | Jesse Conde ⚠️ (vuelve en Netflix, según un extracto) | **Jesse Conde** ✅ (Tigger, Stan Lee) | **Lucas Medina** ⚠️ |
| **Makoto Hyūga** | Enzo Fortuny ⚠️ (vuelve en Netflix, según un extracto) | **Enzo Fortuny** ⚠️ | Juan Balvín ⚠️ |
| **Mari Makinami** | — | — | **Mireya Mendoza** ✅ (desde *2.22*) |
| Maya Ibuki | ⚠️ | ⚠️ | Andrea Higa ⚠️ |
| Ryōji Kaji | ⚠️ | ⚠️ | Sebastián Castro Saavedra ⚠️ |

**Del doblaje original y de *Renewal*, a una sola fuente** (Doblaje Wiki,
segunda pasada) ⚠️: Yui Ikari, **Belinda Martínez**; Naoko Akagi, **Rebeca
Patiño**; Shinji de niño, **Alondra Hidalgo**; en *Renewal*, Ritsuko es
**Gabriela Gómez** y Fuyutsuki, **Rolando de Castro**.

Fuentes de la tabla:
- **Netflix, reparto entero**: [Dub Database: Netflix](https://dubdb.fandom.com/wiki/Neon_Genesis_Evangelion_(Latin_American_Spanish,_Netflix))
  y [Voice over Wiki](https://voice-over-and-voice-acting.fandom.com/wiki/Neon_Genesis_Evangelion_(2003)) (por extracto: Marisol Romero y Alberto Bernal).
- **Original y Netflix**: [Cine Premiere](https://cinepremiere.com.mx/neon-genesis-evangelion-netflix-doblaje.html),
  [Xataka México](https://www.xataka.com.mx/streaming/neon-genesis-evangelion-llega-a-netflix-tercer-doblaje-latino-para-mexico-estas-nuevas-voces-personajes),
  [Doblaje Wiki: Shinji Ikari](https://doblaje.fandom.com/es/wiki/Shinji_Ikari)
  («Víctor Ugarte lo dobla en todas sus apariciones»),
  [Doblaje Wiki: Asuka](https://doblaje.fandom.com/es/wiki/Asuka_Langley_Soryu),
  [Doblaje Wiki: Georgina Sánchez](https://doblaje.fandom.com/es/wiki/Georgina_S%C3%A1nchez).
- **Toni Rodríguez** (murió el **22 de abril de 2021**, a los 51): [Infobae](https://www.infobae.com/america/entretenimiento/2021/04/22/murio-toni-rodriguez-la-voz-en-espanol-de-misato-katsuragi-personaje-de-evangelion/),
  [Somos Kudasai](https://somoskudasai.com/noticias/cultura-otaku/fallece-toni-rodriguez-la-voz-de-misato-katsuragi-en-espanol-latino/),
  [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Toni_Rodr%C3%ADguez).
  Según esos obituarios, **la llamaron para las *Rebuild* tres veces y no
  llegaron a un acuerdo económico**; la sustituyeron Yanelly Sandoval y
  Vivian Magos en otros proyectos ⚠️.
- **Rebuild en Prime Video** (agosto de 2021): **doblaje «colaborativo»
  entre México y Argentina**, dirigido por **Jorge Gabriel Riveros Torres**
  (el del redoblaje argentino de Harry Potter) para **Marmac Group** ✅
  ([ANMTV](https://www.anmtvla.com/2021/08/revelado-doblaje-colaborativo-de-la.html),
  [Cine Premiere](https://cinepremiere.com.mx/rebulid-of-evangelion-doblaje-latino-prime-video.html),
  [MasGamers](https://www.masgamers.com/evangelion-3-0-1-01-doblaje-latino-voces-anime),
  [Atomix](https://atomix.vg/estos-son-los-actores-de-doblaje-latino-para-evangelion-3-0-1-0/),
  [LevelUp](https://www.levelup.com/noticias/636839/Parece-que-Evangelion-30-101-llegara-con-doblaje-latino-y-voces-conocidas/)).

### 10.3 Frases en latino

- **«No debo huir»** es como se dice en español el 逃げちゃダメだ de Shinji:
  lo usa la wiki en español ([Evangelion Wiki ES](https://evangelion.fandom.com/es/wiki/Shinji_Ikari))
  y los edits de TikTok ([ejemplo](https://www.tiktok.com/@mangeel_07/video/7386463894581054726)).
  **No confirmé** que sea la frase exacta de ninguno de los tres doblajes ⚠️.
- **No encontré** con fuente cómo dicen en latino «あんたバカ？» ni «歌はいいね».
  Míralo en los vídeos de §12 antes de rotular ⚠️.

**Segunda pasada: frases oídas en los episodios doblados** ✅. En Internet
Archive está el ítem [`26-neon-genesis-evangelion`](https://archive.org/details/26-neon-genesis-evangelion)
(«español latino», los 26 episodios completos, ≈23:20 cada uno, mismo
corte que el japonés). Se oyeron dos escenas con `voz.py` (Whisper se
equivoca con los nombres: «Xinyi» por Shinji, «Rey» por Rei; la frase se
comprobó reescuchando):

| Escena | Frase textual | Minuto |
|---|---|---|
| Ep. 6, Rei tras el combate | «Estoy apenada. No tengo idea de lo que debo hacer o sentir en un momento como este» | segundos antes de 00:21:34 |
| Ep. 6, Shinji (el «笑えばいいと思うよ») | **«¿Por qué no pruebas sonreír, Rei?»** | [00:21:34](https://archive.org/download/26-neon-genesis-evangelion/6%20Neon%20genesis%20Evangelion.mp4?t=1294) |
| Ep. 24, Kaworu | «El hombre debe soportar el sufrimiento, es parte de la vida […] Tu corazón es demasiado frágil, frágil como el cristal. Mi corazón, si es digno de ser amado, amigo amado… **¡Yo te amo, Shinji!**» | [00:09:37](https://archive.org/download/26-neon-genesis-evangelion/24%20Neon%20genesis%20Evangelion.mp4?t=577) |

⚠️ **De qué doblaje es ese ítem**: por el tamaño de los archivos y la
sinopsis calcada de la de Netflix, **probablemente el de Netflix (2019)**,
pero no se comparó el timbre con una muestra de cada doblaje.

**Las muestras oficiales de Doblaje Wiki** (doblaje original de 1999),
transcritas y medidas con `voz.py` ✅:

| Personaje (actor) | Frase textual | Cómo suena |
|---|---|---|
| Gendo ([Humberto Solórzano](https://static.wikia.nocookie.net/doblaje/images/1/1f/NGEGend%C5%8DIkari.ogg/revision/latest?cb=20180725052538&path-prefix=es)) | «Olvidar el sufrimiento es la forma en que sobrevivimos, pero hay cosas muy importantes que recordar» · «Todo está en mi corazón, es suficiente con eso» | Grave (98 Hz), **muy expresiva** (31,7 semitonos), 2,9 palabras/s: solemne, no robótico |
| Ritsuko ([Maru Guerrero](https://static.wikia.nocookie.net/doblaje/images/8/80/NGERitsukoAkagi.ogg/revision/latest?cb=20180725052714&path-prefix=es)) | «Jamás tuvo alguna esperanza o expectativa de mí. Yo no era nada, nada, nada» · «Mamá, dime qué puedo hacer, por favor» | Aguda (267 Hz), expresiva (9,1), 2,98 palabras/s |
| Shinji ([Víctor Ugarte](https://static.wikia.nocookie.net/doblaje/images/0/00/NGEShinjiIkari.ogg/revision/latest?cb=20180725052014&path-prefix=es)) | «¡Díganme qué debo hacer!» · «Todavía debo pilotarlo, aunque me obliga a asesinar» · «Todo el mundo me aprecia y me felicita. ¡Todos están orgullosos de mí!» | Muy aguda (361 Hz), 8,4 semitonos, **la más rápida**: 3,52 palabras/s |
| Asuka ([Norma Echevarría](https://static.wikia.nocookie.net/doblaje/images/8/88/NGEAsukaLangleyS%C5%8Dry%C5%AB.ogg/revision/latest?cb=20180725052246&path-prefix=es)) | «No valgo nada. Nadie me necesita. Nadie desea a una piloto que no puede controlar a su Eva» · «La basura soy yo» | Aguda (274 Hz), 11,6 semitonos, rápida (3,32) |
| Rei ([Circe Luna](https://static.wikia.nocookie.net/doblaje/images/f/f8/NGEReiAyanami.ogg/revision/latest?cb=20180725052117&path-prefix=es)) | «Yo soy quien soy. Me convertí en mí a través de la instrumentalización de los lazos y las relaciones entre las demás personas y yo» | Media (218 Hz), 10,4 semitonos, 3,64 palabras/s (es un monólogo, no sus frases cortas) |
| Misato ([Toni Rodríguez](https://static.wikia.nocookie.net/doblaje/images/6/63/NGEMisatoKatsuragi.ogg/revision/latest?cb=20180725052424&path-prefix=es)) | «Pero yo odiaba a mi padre, y odiaba a ser una niña buena» · «¡Lo odio!» | Muy aguda (387 Hz), 13,6 semitonos: momento de crisis, no su tono de hermana mayor |

Son frases de monólogos, no las más alegres: sirven para el carácter
(Gendo grave y sereno; Shinji y Asuka rápidos y agudos por la ansiedad).
Para textos alegres del canal, usa las de §2 y §18.6.
- Si la lámina usa una frase de la serie, **ponla como traducción propia**
  o compruébala antes en Netflix con el audio latino.

### 10.4 Entrevistas a las voces (para el canal, es oro)

- **Víctor Ugarte** (Shinji; también Harry Potter y Sasuke): [#LaEntrevista, DubZoneLA](https://www.youtube.com/watch?v=QsD3N_4QsqM),
  [Radio Anime Obsesión, 2012 (iVoox)](https://www.ivoox.com/en/radio-anime-obsesion-entrevista-a-victor-ugarte-audios-mp3_rf_1272070_1.html),
  [«Victor Ugarte - Voz Shinji Ikari»](https://www.youtube.com/watch?v=XEjsJJuLFLk),
  [«Shinji Ikari saluda a Evangelion Doblaje Latino Original»](https://www.youtube.com/watch?v=e80MUSH_v0M).
- **Georgina Sánchez** (Asuka): [«su experiencia como voz de Asuka»](https://m.youtube.com/watch?v=MLG9Yy4Ou6g).
- **Ernesto Lezama** (Kaworu): [TikTok de @lavidadeldoblaje_](https://www.tiktok.com/@lavidadeldoblaje_/video/7498023547160235282).
- **Minutos sin verificar** (YouTube no abre desde aquí).

---

## 11 · Música

| Tema | Qué es | Ambiente | Estado |
|---|---|---|---|
| **残酷な天使のテーゼ** («A Cruel Angel's Thesis») | Opening. Canta **Yoko Takahashi**; letra de **Neko Oikawa**; música de Hidetoshi Satō y Toshiyuki Ōmori. Single doble con «Fly Me to the Moon», **25-oct-1995** | Energía, épica pop. **Todo el mundo la reconoce** | ✅ ([Wikipedia](https://en.wikipedia.org/wiki/A_Cruel_Angel%27s_Thesis), [Evangelion Wiki](https://evangelion.fandom.com/wiki/A_Cruel_Angel's_Thesis_/_FLY_ME_TO_THE_MOON_(1995_single))) |
| **Fly Me to the Moon** | Ending (estándar de jazz). Voz de **CLAIRE**; hay **muchas versiones** a lo largo de la serie (Yoko Takahashi en bossa, y las de las actrices ⚠️) | Calma, jazz de bar, nostalgia | ✅ single; ⚠️ la lista de versiones. En el subtítulo de Netflix Japón suena al final: ep. 1, 00:22:01; ep. 26, 00:22:02 |
| **Komm, süsser Tod** | Canción de *The End of Evangelion*; letra original de **Anno**, voz de **Arianne** | Alegre por fuera, apocalíptica por dentro. **Hoy es meme** («la de la Fanta») | ✅ ([TikTok @wusodream](https://www.tiktok.com/@wusodream/video/7623511430721047816), [SiIvaGunner Wiki](https://siivagunner.fandom.com/wiki/Komm,_s%C3%BCsser_Tod)) |
| **Banda sonora de Shiro Sagisu** | «Decisive Battle» (la marcha de los ataques) y «Thanatos» (EoE) ⚠️ | Urgencia militar / tristeza | ⚠️ nombres de memoria |
| **Clásica en la serie** | **Himno de la alegría** (Beethoven, 9.ª) que tararea Kaworu, ep. 24, 00:04:55 ✅. **Bach al chelo** en el ep. 15, 00:11:10 ⚠️ (el subtítulo sólo dice «チェロの音色») | Calma, ironía | ✅ / ⚠️ |
| **El SDAT de Shinji** | Suena «música que se escapa de los auriculares» (ep. 2, 00:16:16; ep. 9, 00:15:16) y se oye **rebobinar la cinta** (ep. 9, 00:16:26) | Aislamiento | ✅ |

Para el 30 aniversario salió **el vinilo de Yoko Takahashi** con portada de
Ikuto Yamashita ([Black Screen Records](https://blackscreenrecords.com/products/a-cruel-angels-thesis),
[web 30 aniversario](https://30th.evangelion.jp/)) ✅.

**Para #demos**: la canción que **cualquier persona del servidor ha
cantado o doblado alguna vez** es «残酷な天使のテーゼ». Si la lámina lleva
un guiño musical, es ése (sin copiar la letra: derechos).

### 11.1 Segunda pasada: lo visto y oído

- **El opening completo** (4:03) se miró con `fotogramas.py` ✅: planos de
  los tres pilotos, siluetas de las Eva al atardecer (1:00), la Unidad 02
  sobre rojo (1:15), el ojo verde de Rei y **una figura colgando en cruz
  sobre la luna llena** ([3:45](https://archive.org/download/y-2mate.com-neon-genesis-evangelion-opening-full-english-version-a-cruel-angels-thesis-360p/y2mate.com%20-%20Neon%20Genesis%20Evangelion%20Opening%20Full%20English%20Version%20A%20Cruel%20Angels%20Thesis_360p.mp4?t=225)),
  el plano más repetido en fan art del opening. Ojo: es una subida con la
  **versión en inglés** de la canción.
- **El ending del ep. 1**: una **imagen fija** de la luna llena entre
  ramas, 65 segundos, sin animación ✅. El ending cambia de imagen según el
  capítulo.
- **«Himno de la alegría» en toda la escena final del ep. 24** (Kaworu) ✅
  ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Awesome/NeonGenesisEvangelion)).
  Que Kaworu lo **tararee o lo toque** no se pudo confirmar: se recorrió
  el tramo 56:30-1:03:00 del archivo de los ep. 22-24 cada 10 s y no sale
  ningún piano ⚠️ (falta oírlo).

### 11.2 Efectos de sonido que todos reconocen ✅

Catalogados por su nombre de librería en la
[Sound Effects Wiki](https://soundeffects.fandom.com/wiki/Neon_Genesis_Evangelion);
el [foro EvaGeeks](https://forum.evageeks.org/viewtopic.php?t=6384)
confirma que la sirena es de Hollywood Edge:

| Sonido | Dónde suena | Clip de librería |
|---|---|---|
| **La alarma de Ángel detectado** | Sala de mando, cada ataque | «Hollywoodedge, Warning Buzzer Space PE194501» / «Sound Ideas, ALARM - SPACE WARNING SYSTEM: INTRUDER ALERT» |
| **La puerta de la jaula de las Eva** | El hangar verde (§5) | «Hollywoodedge, Warehouse Door HugeM PE185501» |
| **Las cigarras** | Todas las escenas de día: el verano eterno | «Discovery Sound, CICADA» |
| **El tren a lo lejos** | Escenas de calma y soledad | «Hollywoodedge, Train Long From Dista PE064401» |

- **La voz que canta el número**: Maya diciendo «シンクロ率 41.3パーセント»
  (ep. 1, 00:19:58) es un sonido reconocible de recopilaciones y memes
  ([TikTok](https://www.tiktok.com/discover/sonido-de-chicharra-evangelion) ⚠️).
- Una **recreación libre** de la alarma (no es la original):
  [esffects.net](https://esffects.net/en/176.html) ⚠️.
- **Para #demos**: el «ding» de una demo nueva podría ser la alarma de
  NERV, y el número de sincronía, el «nivel» de la demo.

---

## 12 · Vídeos

> YouTube y TikTok siguen sin abrir: **los minutos de los vídeos de
> YouTube no están comprobados** ⚠️. Los de la serie (§2) sí. En la segunda
> pasada se usaron copias en **Internet Archive**, que sí dan minuto (§12.5).

### 12.1 Oficiales

| Vídeo | Para qué |
|---|---|
| [Tráiler oficial de Netflix](https://www.youtube.com/watch?v=3bdjDmYc8J4) (también [otra subida](https://www.youtube.com/watch?v=zEnsYn43TpA)) | Estreno mundial en Netflix, **21 de junio de 2019** |
| [Tráiler VOS en español, Netflix España](https://www.youtube.com/watch?v=BOXFsKGM49M) | Rótulos en español |
| [Corto de Asuka del 30 aniversario](https://www.evangelion.jp/news/260307-2/) (en el YouTube oficial de Khara desde el 8-mar-2026) | **El arte más nuevo y oficial de Asuka**, 14 min y medio |
| [Tráiler de *3.0+1.0* doblado al latino](https://codigoespagueti.com/noticias/anime/trailer-evangelion-3-01-0-doblaje-espanol-latino/) (Prime Video) | Voces latinas de las *Rebuild* |
| [Primer tráiler en inglés de la serie nueva de Yoko Taro](https://kotaku.com/the-first-english-trailer-for-yoko-taros-evangelion-series-is-here-to-remind-you-its-coming-and-looks-great-2000712671) | Lo que viene (anunciada el 23-feb-2026) |

### 12.2 Doblaje latino en vídeo

- [«Neon Genesis Evangelion (Netflix) / Doblaje Español Latino»](https://www.youtube.com/watch?v=n6MXBsCvlHw)
- [«EVANGELION DOBLAJE LATINO ORIGINAL»](https://www.youtube.com/watch?v=36R6Uz0bVfQ)
- Entrevistas a las voces: §10.4.

### 12.3 Análisis en español

- [«Evangelion y el Dilema del Erizo»](https://www.youtube.com/watch?v=xww37raedG8)
- [«Psicólogo explica el dilema del erizo en Evangelion»](https://www.youtube.com/watch?v=0lDyEbJxVD0)
- [«La psicología de Shinji Ikari»](https://m.youtube.com/watch?v=XYF_vm8cZw8)
- [«Asuka Langley: el problema de fingir que todo está bien»](https://www.youtube.com/watch?v=Abl2BnJWLMo)
- [«Análisis psicológico»: Shinji, Rei, Asuka y Misato](https://www.youtube.com/watch?v=BOsBch3FZ4w)

El «dilema del erizo» lo cuenta Ritsuko en el **ep. 3, 00:04:53** ✅
(«ヤマアラシのジレンマって話 知ってる？»).

### 12.4 TikTok

- [Etiqueta «Komm Süsser Todd»](https://www.tiktok.com/discover/komm-s%C3%BCsser-todd) y
  [«Fanta Evangelion»](https://www.tiktok.com/discover/fanta-evangelion): el meme
  de la Fanta (el LCL naranja del final).
- [«Third Impact Evangelion»](https://www.tiktok.com/discover/third-impact-evangelion).
- [«Shinji Cassette Player»](https://www.tiktok.com/discover/shinji-cassette-player): el SDAT.
- [Edit «No debo huir»](https://www.tiktok.com/@mangeel_07/video/7386463894581054726).

### 12.5 Segunda pasada: vídeos mirados de verdad ✅

- **Tráiler oficial del 30 aniversario de *The End of Evangelion*** (GKIDS,
  copia en Internet Archive `youtube-JGcbdUgNYOY`, 57 s), minuto a minuto:
  logo de GKIDS (0:00) · piedras y LCL rojo (0:08-0:12) ·
  [silueta crucificada roja (0:16)](https://archive.org/download/youtube-JGcbdUgNYOY/JGcbdUgNYOY.mp4?t=16) ·
  Tokio-3 con los rascacielos ya fuera (0:24) ·
  [cielo rosa del Tercer Impacto sobre el mar (0:32-0:36)](https://archive.org/download/youtube-JGcbdUgNYOY/JGcbdUgNYOY.mp4?t=32) ·
  Gendo en primer plano con «03F» detrás (0:40) · rayos rojos (0:44-0:48) ·
  [título y fecha, «IN THEATRES JULY 22 ONLY» (0:52)](https://archive.org/download/youtube-JGcbdUgNYOY/JGcbdUgNYOY.mp4?t=52).
- **El opening entero** (4:03) y **el ending** del ep. 1: §11.1.
- **Episodios enteros para seguir mirando** sin YouTube (Internet Archive,
  comprobados con `curl -I`): 19 episodios sueltos en
  [`neon-genesis-evangelion-episode-21-…`](https://archive.org/details/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12),
  los ep. 22-24 juntos en [`neon-genesis-evangelion-22-al-24`](https://archive.org/details/neon-genesis-evangelion-22-al-24),
  los 26 en 1080p en [`evangelion-the-full-series`](https://archive.org/details/evangelion-the-full-series)
  y **los 26 doblados al latino** en [`26-neon-genesis-evangelion`](https://archive.org/details/26-neon-genesis-evangelion) (§10.3).
- Hay también un ítem con el **doblaje de España** (`evangelion_202506`,
  1997-2017): **no es latino**, se descarta a propósito.

---

## 13 · Videojuegos de la franquicia

| Juego | Año y plataforma | Qué es | Para la lámina |
|---|---|---|---|
| **Girlfriend of Steel** (鋼鉄のガールフレンド) | 1997 PC; luego PlayStation, Saturn, PS2, PSP | **Novela visual**: Shinji conoce a Mana Kirishima, una chica nueva que Asuka cree espía | Caja de texto de novela visual ⚠️ ([Wikipedia](https://en.wikipedia.org/wiki/Neon_Genesis_Evangelion:_Girlfriend_of_Steel), [4Gamer](https://www.4gamer.net/games/032/G003267/)) |
| **Girlfriend of Steel 2nd** | 2003 ⚠️, PS2 ⚠️ | Continuación, historia paralela | [Wikipedia](https://en.wikipedia.org/wiki/Neon_Genesis_Evangelion:_Girlfriend_of_Steel_2nd) |
| **Ayanami Raising Project** (綾波育成計画) | 2001 PC ⚠️; Dreamcast 18-abr-2002 ✅; PS2; DS | Eres el tutor de Rei (y de Asuka) durante un año, con horario semanal | [Wikipedia](https://en.wikipedia.org/wiki/Neon_Genesis_Evangelion:_Ayanami_Raising_Project), [Game Soft Navi](https://gamesoft-navi.com/product/18004/) |
| **Shinji Ikari Raising Project** | 2004 PC | Eres **Misato** y decides el horario de Shinji; universo alternativo del ep. 26 | [Wikipedia](https://en.wikipedia.org/wiki/Neon_Genesis_Evangelion:_Shinji_Ikari_Raising_Project), [EvaWiki](https://wiki.evageeks.org/Shinji_Ikari_Raising_Project) |
| **Neon Genesis Evangelion 2** | 2003 ⚠️, PS2 ⚠️ | Juego de «simulación» de la historia ⚠️ | [Wikipedia](https://en.wikipedia.org/wiki/Neon_Genesis_Evangelion_2) |
| **Evangelion Battlefields** | móvil, *gacha* (ya cerrado) | Combates de Eva en tiempo real y **reclutar pilotos** | [Gacha Games Wiki](https://gachagames.fandom.com/wiki/Evangelion_Battlefields) |
| **EVANGELION: Δ CROSS REFLECTIONS** | XR (Quest), Pixelity. Anunciado el **5-sep-2025** | **Eres un aprendiz de NERV que sueña con ser piloto**. Historia nueva durante los ep. 1-11; primera parte de una trilogía; modo historia y combate. Demo en la primera mitad de 2026; **retrasado a 2027** (anuncio del 25-ago-2026 ⚠️ una fuente) | ✅ ([Road to VR](https://roadtovr.com/evangelion-cross-reflections-quest-3-release-2026/), [AV Club](https://www.avclub.com/evangelion-cross-reflections-release-date-announced), [Final Weapon](https://finalweapon.net/2025/09/05/evangelion-%CE%B4-cross-reflections-xr-game-launches-in-2026/), [XR Source](https://xrsource.net/11488/evangelion-cross-reflections-to-feature-story-and-battle-modes/)) |

Resumen de la historia de los juegos: [4Gamer (2021), «歴代ゲーム化作品を発掘»](https://www.4gamer.net/games/032/G003267/20210428016/).

**Lo que NO pude ver**: capturas de las cajas de diálogo de estos juegos.
Game UI Database y The Cutting Room Floor no respondían. **No hay caja de
diálogo de videojuego verificada**: usa la cartela y la pantalla de NERV
(§7), que son de la serie.

**Segunda pasada** ⚠️: **The Cutting Room Floor sí tiene páginas** de
*Girlfriend of Steel* ([PS1](https://tcrf.net/Neon_Genesis_Evangelion:_Koutetsu_no_Girlfriend_(PlayStation)),
material de depuración) y de su *Special Edition* ([PS2](https://tcrf.net/Shin_Seiki_Evangelion:_Koutetsu_no_Girlfriend_Special_Edition_(PlayStation_2)),
texto de desarrollo oculto y gráficos sin usar), según el resumen del
buscador. No se pudieron abrir: el proxy falla con el certificado de
Cloudflare, y Wayback Machine cortó el túnel, aunque confirma copias del
[23-ago-2025](http://web.archive.org/web/20250823031232/https://tcrf.net/Neon_Genesis_Evangelion:_Koutetsu_no_Girlfriend_(PlayStation))
y del [26-ago-2025](http://web.archive.org/web/20250826032103/https://tcrf.net/Shin_Seiki_Evangelion:_Koutetsu_no_Girlfriend_Special_Edition_(PlayStation_2)).
No hay página de TCRF para los *Raising Project*. Por descripción:
*Girlfriend of Steel* es una **novela visual** (retrato del personaje y
caja de texto abajo) y los *Raising Project* son de **crianza** (menú
semanal con estadísticas y retrato). Arte de *Girlfriend of Steel 2*: hoja
`settei_figuras_03.jpg`, nº 133 ✅.

**Idea útil**: *Cross Reflections* hace de ti **un aprendiz de NERV que
quiere ser piloto**. Es la misma situación que alguien que abre su ficha
en #demos.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todos reconocen

| Cosa | Dónde | Estado |
|---|---|---|
| «逃げちゃダメだ» / «No debo huir» | ep. 1, 00:18:33 | ✅ |
| «Si vas a subir, hazlo ya» → el meme **«Get in the robot, Shinji»** | ep. 1, 00:15:38 | ✅ escena / ⚠️ nombre del meme |
| **La pose Gendo** (manos juntas delante de la boca) | toda la serie | ⚠️ |
| **«おめでとう»**: todos aplauden a Shinji en círculo, **hasta Pen Pen** («クッ クッ クーク！») | ep. 26, 00:21:33 → 00:21:53 | ✅ ([Know Your Meme](https://knowyourmeme.com/memes/subcultures/neon-genesis-evangelion)) |
| **La sonrisa de Rei** | ep. 6, 00:21:30 | ✅ |
| «あんたバカ？» | ep. 8, 00:11:02 | ✅ |
| **La cerveza de Misato** («プッハー!! くぅ〜！») | ep. 2, 00:13:14 | ✅ |
| **Pen Pen**, el pingüino | ep. 2, 00:15:05 | ✅ |
| **«La Fanta»** (el LCL naranja) y **«Komm, süsser Tod»** | EoE | ✅ (TikTok) |
| «大人のキスよ» (Es un beso de adultos) → meme «That Was a Grown-up Kiss» | EoE, 00:32:52 | ✅ ([Know Your Meme](https://knowyourmeme.com/memes/subcultures/the-end-of-evangelion)) |
| «Gendowned» | vídeos de fans | ✅ (Know Your Meme) |
| El **dilema del erizo** | ep. 3, 00:04:53 | ✅ |
| **«amigo» / «amiga»** del doblaje original; «Evanjelion» | doblaje de 1999 | ✅ (Doblaje Wiki) |
| Recopilación: [«20 of the best memes… Evangelion»](https://knowyourmeme.com/editorials/collections/20-of-the-best-memes-from-the-world-of-evangelion-to-commemorate-the-beloved-anime) | | |

### 14.2 Qué NO hacer (lo que un fan notaría)

- **Nada de sexualizar a los pilotos.** Tienen **14 años** (lo dicen en la
  serie: «14歳の子どもたちに 委ねざるを得ないのよ», ep. 4, 00:08:27 ✅). Nada
  de poses de *fanservice* con los trajes de conector.
- **Las Eva no son robots** ⚠️: el fandom insiste en que son seres vivos con
  armadura. No las dibujes como mecha brillante de juguete.
- **No mezclar la serie con las *Rebuild*** sin querer: en las películas
  Asuka se apellida **Shikinami** (no Soryu), lleva parche en *3.0* ⚠️ y
  aparece **Mari**, que no existe en la serie.
- **Asuka lleva sus pinzas rojas del pelo siempre**, también de calle ⚠️.
  Rei no las lleva igual. No se las cambies.
- **Rei no grita ni se ríe a carcajadas. Gendo no sonríe con calidez.
  Kaworu no se enfada.**
- **La cartela no va en color** ni con mincho fina (§7.4).
- **No colores alegres de dibujos infantiles**. Evangelion es verano
  brillante, pero el tono es serio. El rojo de alerta, sólo para alertas.
- **No uses la letra de las canciones** (derechos). El título, sí.

---

## 15 · Poses analizadas por personaje

El **minuto** está comprobado en el subtítulo ✅. **Lo que se ve** (postura,
manos, mirada) es de memoria ⚠️: abre el fotograma en tu PC antes de usarlo.

### Misato

| Escena | Minuto | Qué hace (⚠️) | Sirve para |
|---|---|---|---|
| ep. 1, se presenta | 00:06:20 | De pie junto a su coche, sonriendo, mano en la cadera | **presentar** |
| ep. 1, da el folleto | 00:10:16 | En el coche/tren hacia el GeoFront, **tiende el folleto de NERV** | **explicar** (el léeme) |
| ep. 2, la cerveza | 00:13:14 | Echa la cabeza atrás con la lata, ojos cerrados | **celebrar** (en casa) |
| ep. 6, Operación Yashima | 00:09:20 → 00:09:26 | En la sala de mando, **señala el mapa en la pantalla** | **explicar** |
| ep. 9, plan del unísono | 00:11:03 → 00:11:34 | Delante de los dos, dedo arriba, con la cinta de música | **explicar** |
| ep. 16, «You are number one» | 00:03:20 | Al micrófono de la sala de pruebas, pulgar arriba | **celebrar / animar** |
| ep. 24, lee la ficha de Kaworu | 00:05:58 | Mira la pantalla con Hyuga, seria | **pensar** |
| Avances | 00:23:19 | Sólo voz: «サービス サービス！» | despedirse |

### Asuka

| Escena | Minuto | Qué hace (⚠️) | Sirve para |
|---|---|---|---|
| ep. 8, llega al portaaviones | 00:03:30 | Vestido amarillo, al viento, sonrisa de superioridad | **presentar** |
| ep. 8, se presenta | 00:03:46 | Manos en la cintura, barbilla alta | **presentar** |
| ep. 8, «あんたバカァ？» | 00:11:02 | Se inclina hacia Shinji, dedo acusador | **regañar** |
| ep. 9, «Guten Morgen» | 00:02:24 | Saludo desde la puerta del colegio | **saludar** |
| ep. 10, «見て見て シンジ！» | 00:06:33 | En la piscina, presume antes de tirarse | **celebrar** |
| ep. 15, aplaude el chelo | 00:11:33 | Aplaude despacio, apoyada en la puerta | **animar** (dar feedback) |
| ep. 16, «無敵のシンジ様！» | 00:03:36 | Aplausos irónicos | **regañar** (con ironía) |
| ep. 17, lee la lista de pilotos | 00:21:17 | Frente al ordenador de Kaji, sorprendida | **pensar** |

### Rei

| Escena | Minuto | Qué hace (⚠️) | Sirve para |
|---|---|---|---|
| ep. 5, su ficha | 00:04:25 | (Ritsuko la lee; Rei en la cápsula de prueba) | **la ficha** |
| ep. 5, «何？» | 00:15:55 | Recién salida de la ducha en su piso; mirada neutra | — (evitar: escena de desnudo) |
| ep. 6, «私が守るもの» | 00:15:32 | Sentada de noche junto a Shinji, mira al frente | **animar** (proteger) |
| ep. 6, «絆» | 00:16:25 | De pie, con el traje de conector, mira la ciudad | **pensar** |
| ep. 6, la sonrisa | 00:21:30 → 00:21:35 | Sentada en la cápsula abierta, **sonríe por primera vez** | **celebrar** (suave) |
| ep. 16, «さよなら» | 00:03:49 | Se va, de espaldas | despedirse |

### Shinji

| Escena | Minuto | Qué hace (⚠️) | Sirve para |
|---|---|---|---|
| ep. 1, «逃げちゃダメだ» | 00:18:33 | Puños apretados, mirada baja | **animar** (valor) |
| ep. 2, «知らない天井だ» | 00:03:53 | Tumbado en la cama del hospital | **pensar** |
| ep. 2, el SDAT | 00:16:16 | Tumbado, auriculares puestos | **escuchar demos** |
| ep. 5, la tarjeta | 00:16:11 | Tartamudea, tarjeta en la mano | **presentar** (nervioso) |
| ep. 15, el chelo | 00:11:10 → 00:11:44 | **Tocando el chelo**, arco en la mano | **la pose del canal** |
| ep. 16, «結果 どうでした？» | 00:03:17 | Dentro de la cápsula, pregunta por radio | **preguntar por la demo** |
| ep. 26, «ここにいてもいいんだ！» | 00:21:17 | Brazos abiertos, sonrisa | **celebrar** |

### Kaworu

| Escena | Minuto | Qué hace (⚠️) | Sirve para |
|---|---|---|---|
| ep. 24, tararea | 00:04:55 | Sentado en una estatua rota junto al lago, al atardecer | **presentar** (con música) |
| ep. 24, «歌はいいね» | 00:05:13 | Se gira hacia Shinji, sonrisa suave | **gancho del canal** |
| ep. 24, se presenta | 00:05:36 → 00:05:48 | Mano abierta, invita a tutearle | **presentar / saludar** |
| ep. 24, «好意に値するよ» | 00:09:35 | En el baño público, junto a Shinji | **animar** |
| ep. 24, prueba de sincronización | 00:06:26 | (En la cápsula de prueba) | **la demo** |

### Gendo

| Escena | Minuto | Qué hace (⚠️) | Sirve para |
|---|---|---|---|
| ep. 1, «乗るなら早くしろ» | 00:15:38 | Arriba, en la cabina, mirando a Shinji desde lejos | **regañar** (norma) |
| ep. 1, «問題ない» | 00:09:48 | Pose Gendo en la sala de mando | **la norma** |
| ep. 5, salva a Rei | 00:04:05 | Abre la cápsula ardiendo con las manos; las gafas caen ⚠️ | — |
| ep. 15, en la tumba de Yui | 00:10:26 | De pie, de espaldas, con Shinji | **pensar** |

---

## 16 · Vestuario ⚠️

Todo de memoria: **compruébalo con las hojas de modelo de Sadamoto** antes
de dibujar. Los hex son aproximados. Ayudas:
[EvaWiki: diseños de personajes](https://wiki.evageeks.org/Evangelion_Character_Designs),
[guía de cosplay de calle](https://closetchloecosplay.wordpress.com/2018/03/12/evangelion-10-outfits-to-closet-cosplay/),
[paleta del traje de Asuka](https://www.pixilart.com/palettes/evangelion-asuka-plugsuit-40378).

| Personaje | Lo icónico | Colores aprox. | Accesorios |
|---|---|---|---|
| **Shinji** | Uniforme escolar: camisa blanca de manga corta y pantalón negro. Traje de conector **blanco y azul** | `#F4F4F0` · `#1F3F8F` · `#1A1A1A` | **SDAT con auriculares** |
| **Asuka** | **Vestido amarillo** de la llegada (ep. 8). Traje de conector **rojo** | `#F2D04A` · `#D3290F` · pelo `#E07A3A` | **Pinzas rojas del pelo** («interfaz») siempre |
| **Rei** | Uniforme escolar (blusa blanca, vestido azul). Traje de conector **blanco** | pelo `#9FC4E8` · ojos `#C8283C` · `#F4F4F0` | Vendas en los primeros episodios |
| **Misato** | **Chaqueta roja** sobre vestido negro corto. En casa, camiseta y pantalón corto | `#B3262A` · `#1A1A1A` · pelo `#4B3566` | **Cruz** colgada del cuello; **lata de cerveza** |
| **Kaworu** | Uniforme escolar blanco y negro | pelo `#C8CCD4` · ojos `#C8283C` | — |
| **Gendo** | Uniforme de comandante oscuro, **guantes blancos** | `#2A2A2A` · gafas `#D9822B` | **Gafas tintadas**, barba |
| **Ritsuko** | Bata de laboratorio blanca sobre ropa oscura | pelo rubio teñido `#E8D7A0` | Lunar bajo el ojo |

La ropa que **todos reconocen**: los **trajes de conector** (azul, rojo,
blanco) y el **vestido amarillo de Asuka**. En una lámina de voz, mejor el
**uniforme escolar o la ropa de calle** que el traje de conector (se evita
lo ceñido: son menores).

---

## 17 · Paisajes y fondos de pantalla

### 17.1 Los sitios, con su luz ⚠️

- **Tokio-3 al atardecer**: rascacielos que suben del suelo, cielo naranja,
  **postes y cables eléctricos** en primer plano, **cigarras** sonando. Es
  el plano más fotografiado de la serie.
- **La calle de Hakone en verano**: cielo azul fuerte, sombras duras,
  verde saturado. Hakone de verdad:
  [SoraNews24 (fotos)](https://soranews24.com/2022/11/21/visiting-evangelions-tokyo-3-anime-locations-in-real-life-hakone%E3%80%90photos%E3%80%91/),
  [MikeHattsu](https://mikehattsu.blogspot.com/2015/06/neon-genesis-evangelion-tokyo-3.html),
  [AnimeTrips](https://anime-trips.com/en/blog/evangelion-seichi-junrei).
- **La sala de mando**: oscura, iluminada por pantallas naranjas.
- **El GeoFront**: luz verde y dorada desde el techo de la caverna.
- **La sala de SEELE**: negro total y monolitos.
- **Ube-Shinkawa** (final de *3.0+1.0*): mañana nublada, luz real.

### 17.2 Fondos de pantalla en alta (mirar autor y licencia antes de usar)

| Fondo | Tamaño | Autor | Enlace |
|---|---|---|---|
| *3.0*: Shinji, Rei y Asuka | 3840×2160 | shirakawa mayo | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=691150) |
| Rei Ayanami | 3840×2160 | ⚠️ | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=949384) |
| «Asuka: Neon Skyline» | 3840×2160 | ⚠️ | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1399756) |
| Unidad 01 | 3840×2160 | ⚠️ | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1163434) |
| Pilotos y Eva con cielo nublado | 3840×2160 | ⚠️ | [Wallpaper Alchemy](https://www.wallpaperalchemy.com/wallpaper/neon-genesis-evangelion-characters-mechs-4k-wallpaper-2056) |
| Más de 120 fondos 4K | varios | varios | [alphacoders](https://alphacoders.com/neon-genesis-evangelion-4k-wallpapers) |
| Fondos de la serie (cuenta de fans) | — | «Anime Background Art» | [X](https://x.com/backgroundsbot/status/960223392547864576?lang=en) |

---

## 18 · Guía para generar con IA (Firefly, Canva)

> [!warning] Primero, lo que dijo el dueño
> Quiere que **no parezca hecho por IA**. Úsala **sólo para fondos, luz y
> objetos de apoyo**. Los personajes, **de fotogramas reales** (§15) pasados
> por `v3/integrar.py`. Además, Firefly suele **negarse a dibujar
> personajes con nombre** de una franquicia: describe, no nombres.

### 18.1 Lo que nunca cambia en Evangelion

- **Dibujo de celuloide de los 90** (Gainax, 1995): línea fina y limpia,
  sombra de **dos tonos** con borde duro, sin degradados en la piel ⚠️.
- **Fondos pintados a mano** (dirección de arte de Hiroshi Katō): mucho
  detalle, **postes y cables eléctricos**, cielo de verano.
- **Luz**: sol duro de verano con sombras marcadas; atardecer naranja; o
  **oscuridad con brillo naranja de pantallas**.
- **Encuadre de Anno** ⚠️: planos fijos y largos, contrapicados, siluetas
  a contraluz, primeros planos de ojos, **cortes a cartela negra**.
- **Paleta**: la de §5.2. Negro puro, naranja NERV `#FF9830`, blanco puro
  en los textos.

### 18.2 Cómo describirlo (en inglés, que la IA entiende mejor)

**Fondo de la sala de pruebas (concepto A):**
> dark underground laboratory control room, 1990s anime cel style,
> hand-painted background, black room lit only by orange CRT monitors,
> large glass window to a test chamber, cold fluorescent light from above,
> film grain, muted colors, no people

**Fondo de la sala de los monolitos (concepto B):**
> pitch black void room, twelve tall black stone monoliths arranged in a
> circle, glossy reflective black floor, faint red glow, minimalist,
> 1990s anime film still, film grain, no people, no text

**Fondo del piso de Misato de noche (concepto C):**
> small Japanese apartment living room at night, 1995, cluttered with beer
> cans, low table, sliding door, warm lamp and blue moonlight from the
> balcony, cicadas summer night, 1990s anime cel background, hand-painted,
> film grain, no people

### 18.3 Palabras que ayudan y palabras que lo estropean

| Ayudan | Estropean |
|---|---|
| 1990s anime cel, hand-painted background, film grain, muted colors, hard shadows, summer, telephone wires, cicadas, CRT glow, orange monitors, static composition, low angle | chibi, kawaii, moe, sparkles, glossy 3D render, Unreal Engine, cyberpunk neon pink, vaporwave, cute, pastel, bokeh everywhere, lens flare, cleavage, pin-up |

### 18.4 Qué imágenes usar de referencia de estilo

- **Estilo de fondo**: los fotogramas de §15 (sala de mando del ep. 6,
  00:09:20; piso de Misato del ep. 15, 00:11:10; el lago del ep. 24,
  00:04:55) y la cuenta [Anime Background Art](https://x.com/backgroundsbot/status/960223392547864576?lang=en).
- **Estilo de pantallas**: [Pedro Fleming](https://www.pedrofleming.com/neongenesisevangelion)
  y [nerv-ui](https://github.com/TheGreatGildo/nerv-ui).
- **Estilo de cartela**: cualquier título de episodio (el del ep. 1 en
  00:01:33, tras el opening ⚠️).
- **Segunda pasada, fotogramas ya vistos** (Internet Archive, con su
  segundo): la jaula de las Eva ([ep. 1, 20:58](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2001%20Angel%20Attack%20%5B5F116C28%5D.mp4?t=1258))
  para el verde de NERV; el apartamento a oscuras de Rei
  ([ep. 6, 14:45](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2006%20Rei%20II%20%5B6F5224E2%5D.mp4?t=885))
  para una habitación vacía; la luna del ending
  ([ending, 0:20](https://archive.org/details/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12))
  para el azul noche. Hojas: `settei_figuras_03.jpg` nº 105-119 para la
  línea de los diseños y `arte_oficial_01.jpg` nº 9-15 para el color.

### 18.5 Cómo describir a cada personaje (sin nombrarlo)

Rasgos que **nunca cambian**, con los hex **medidos** en arte oficial (§16)
y las etiquetas de Danbooru que más se repiten al dibujarlos (es el
vocabulario que entienden las IA de imagen; [Danbooru](https://danbooru.donmai.us/posts?tags=neon_genesis_evangelion),
sacado en `partes/datos-imagen.md`).

| Personaje | Cómo describirlo | Hex | Etiquetas que ayudan |
|---|---|---|---|
| Asuka | 14 años, pelo largo **rojo anaranjado** con dos pinzas rojas a los lados, ojos azules, barbilla alta | pelo `#A5360F`, pichi `#022A51`, blusa `#D5E0DA`, lazo `#A5190D` | two_side_up, interface_headset, red_bodysuit, tokyo-3_middle_school_uniform |
| Shinji | 14 años, pelo **castaño corto**, ojos azules, camisa blanca de manga corta y pantalón negro, auriculares | pelo `#583535`, traje `#036ED3`, torso `#DCEFF3` | short_hair, white_shirt, black_pants, holding |
| Rei | pelo **azul claro muy corto**, ojos rojos, piel pálida, **cara casi sin expresión** | pelo `#B0C4E4`, traje `#E9EDF3` | expressionless, parted_lips, white_bodysuit |
| Misato | mujer adulta, pelo **largo morado oscuro**, chaqueta roja, vestido negro sin mangas, cruz al cuello, lata en la mano | chaqueta `#E02824`, vestido `#100B0D`, pelo `#1C1231` | red_jacket, cross_necklace, beer_can |
| Gendo | hombre, barba, **gafas de cristal naranja** que no dejan ver los ojos, guantes blancos, uniforme oscuro | gafas `#E97151`, uniforme `#413C53` ⚠️ | gendou_pose, interlocked_fingers, opaque_glasses |
| Kaworu | chico de pelo **gris claro**, ojos rojos, sonrisa tranquila, camisa blanca | pelo `#EAE4E7`, sombra `#8797C6`, pantalón `#3F3B54` | grey_hair, red_eyes, smile, school_uniform |

- **Traje de conexión**: descríbelo como «sleek bodysuit with hard
  shoulder and chest plates, neural clips in the hair». Nunca «armor» ni
  «robot suit».
- **Encuadre**: pide «static shot, low angle» o «extreme close-up on the
  eyes». Los fotogramas vistos del ep. 1 (15:38 las gafas de Gendo, 18:33
  el ojo de Shinji) son el modelo.

### 18.6 Para una IA de texto: cómo escribir en su voz

**Reglas generales** (de §7.2 y de los clips oídos en la segunda pasada):
frases cortas; nada de onomatopeyas escritas en pantalla (la serie usa
cartelas y subtítulos, no globos); las emociones fuertes van en **una
línea sola**, no en párrafos.

| Personaje | Puntuación y tics | Cómo exagera |
|---|---|---|
| Asuka | Signos de exclamación, preguntas retóricas, mete palabras en inglés y alemán | Insulta para no mostrar miedo: «¿Eres idiota?» |
| Shinji | Puntos suspensivos, se disculpa sin motivo, se repite frases | Se habla a sí mismo: «No debo huir» tres veces |
| Rei | Punto final, una o dos palabras, **nunca** exclamación | No exagera: el silencio es su énfasis |
| Misato | Tutea, pregunta primero por radio, inglés macarrónico al celebrar | Celebra a lo grande, luego se hunde en serio |
| Gendo | Imperativo seco, sin saludo | Nunca grita salvo al dar un ultimátum |
| Kaworu | Frases largas y suaves, llama a la gente por su nombre | Habla de música y de «los Lilin» |

**Frases reales, por emoción** (japonés del subtítulo con su minuto, o
español del doblaje latino oído):

- **Alegre**: Misato, «ハ〜イ ユーアー ナンバーワン！» (¡Eres el número uno!,
  ep. 16) · Misato con la cerveza, ojos cerrados (ep. 2, 00:13:14) ·
  Kaworu, «アッ ハハ» (ep. 24, 00:05:51) · Misato, «この次も サービス
  サービス！» (ep. 1, 00:23:19).
- **Enfadado**: Asuka, «あんたバカァ？» (¿Eres idiota?, ep. 8, 00:11:02) ·
  Asuka, «何すんのよ！» (¿Qué haces?, ep. 8, 00:04:04) · Gendo, «乗るなら早く
  しろ でなければ帰れ！» (Si vas a subir, hazlo ya. Si no, vete, ep. 1,
  00:15:38) · Misato en latino: «¡Lo odio!» (muestra de Doblaje Wiki).
- **Explicando**: Misato, el plan de la Operación Yashima (ep. 6,
  00:09:20) · Rei, «絆だから» (Porque es un vínculo, ep. 6, 00:16:25) ·
  Gendo, «説明を受けろ» (Que te lo expliquen) · Gendo en latino: «Todo está
  en mi corazón, es suficiente con eso».
- **Animando**: Rei, «あなたは死なないわ 私が守るもの» (No morirás. Yo te
  protegeré, ep. 6, 00:15:32) · Ritsuko, «10日で8よ 大したものだわ» (ep. 12)
  · Shinji en latino: **«¿Por qué no pruebas sonreír, Rei?»** (ep. 6,
  00:21:34) · Shinji, «逃げちゃダメだ» (No debo huir, ep. 1).
- **Triste**: Asuka en latino: «No valgo nada. Nadie me necesita» · «La
  basura soy yo» · Rei en latino: «Estoy apenada. No tengo idea de lo que
  debo hacer o sentir en un momento como este» (ep. 6, segundos antes de
  00:21:34) · Shinji
  en latino: «¡Díganme qué debo hacer!» · Ritsuko en latino: «Yo no era
  nada, nada, nada».
- **Tierno**: Kaworu en latino: **«¡Yo te amo, Shinji!»** (ep. 24,
  00:09:37).

⚠️ Cómo dice el doblaje latino «あんたバカ？» sigue sin comprobarse (§10).
Si la IA lo necesita, que use «¿Eres idiota?» y lo marque como traducción.

### 18.7 Vocabulario de gestos para la IA de imagen

En los fotogramas vistos esta pasada (ep. 1, 2, 6, 8 y 24) **no sale ni un
chibi, ni una gota de sudor de caricatura, ni fondos de emoción**. Las
emociones se dibujan así:

- **Miedo**: ojos muy abiertos, sudor real en la frente, boca tensa
  (Shinji). Prompt: «wide eyes, cold sweat, tense mouth, extreme close-up».
- **Rabia**: boca muy abierta gritando, cara roja (Asuka, ep. 8, 04:04).
  Prompt: «shouting, flushed face, clenched fists».
- **Alegría**: ojos cerrados en arco, sonrisa enorme (Misato, ep. 2).
- **Ternura**: media sonrisa, luz de atardecer (Kaworu, ep. 24, 05:40).
- **La sonrisa rara**: sonrisa pequeña, mirada de lado (Rei, ep. 6, 21:45).
- **Frialdad**: gafas opacas que reflejan, manos juntas delante de la boca
  (Gendo). Prompt: «opaque glasses reflecting light, hands clasped in front
  of mouth».
- **Palabras que lo estropean** (además de §18.3): «sweat drop», «anime
  reaction face», «chibi», «speech bubble».

---

## Punto 18 · Estilo de dibujo, técnica y cómo replicarlo

### Cómo se hizo la serie

- **Celuloide tradicional de 1995**, fotografiado con grano de película
  real. Gainax **no** usaba Clip Studio ni Toon Boom (no existían). Hubo
  retoques digitales sólo en momentos puntuales (créditos, *glitches* de
  los ep. 25-26) ⚠️: no encontré qué programa usaron.
- **Planos fijos a propósito**: al final se animó con muy poco tiempo, y
  Anno sostuvo fotogramas quietos como si la cámara se parara. Los dos
  famosos: el ascensor con Rei y Asuka, y la Unidad 01 sosteniendo a
  Kaworu. ¿Presupuesto o tiempo? Se discute, pero la quietud es un recurso
  dramático ⚠️ ([CBR](https://www.cbr.com/neon-genesis-evangelion-other-anime-ran-out-of-budget-quality-decline/),
  [foro EvaGeeks](https://forum.evageeks.org/thread/19083/Did-Evangelion-really-run-out-of-budget/),
  que se citan entre sí).
- **Capas densas de línea en la acción**: animadores como **Mitsuo Iso**
  hacían que los Eva se movieran como seres vivos, no como robots ⚠️ (una
  fuente).
- **Maquetas de General Products** (la tienda de *garage kits* de Gainax)
  como referencia de luz y perspectiva para el storyboard ⚠️ (una fuente).
- **Línea de Sadamoto**: «arrugada», afilada pero orgánica
  ([AIPT Comics](https://aiptcomics.com/2021/02/04/revisiting-sadamotos-evangelion-manga-p1/) ⚠️).
- **Lo que midió `estilo.py`** en fotogramas oficiales ✅: personajes con
  sombra plana de un solo tono; fondos y luces con **degradado de
  aerógrafo**; línea casi ausente en la piel de los primeros planos; línea
  marcada sólo en metal y estructuras (`#414F37` en la jaula de las Eva).

### Encuadres y composición (el «vocabulario» de Anno)

Según el análisis de [AnnoCinema (Medium)](https://medium.com/@annocinema/annos-compositional-vocabulary-f28ef87d45f7)
y su [Tumblr](https://annocinema.tumblr.com/post/159747328453/a-type-of-shot-that-anno-uses-in-all-of-his-works)
⚠️ (análisis de fans, no entrevista):

- **Primer plano de la parte que actúa**: una mano en el interruptor, un
  pie en el pedal, en vez de la persona entera.
- **Corte al objeto del que se habla**: alguien lo nombra y el siguiente
  plano ES el objeto.
- **Sobre el hombro «que aísla»**: el de delante y el de detrás muy
  distintos en tamaño o luz, para marcar distancia.
- **Cada emoción, su encuadre** (visto en la segunda pasada): el miedo en
  primerísimo plano del ojo (Shinji, ep. 1, 18:33); la frialdad en las
  gafas que reflejan (Gendo, ep. 1, 15:38); la soledad en plano general
  pequeño dentro de algo enorme (la Unidad 01 en la jaula, ep. 1, 20:58).

### Cómo reproducirlo en Photoshop

1. **Línea**: pincel duro, color **gris muy oscuro**, no negro puro. Capa
   en **Multiplicar**, encima del color.
2. **Color**: una capa plana por zona (piel, pelo, traje), sin degradado.
   **Sombra** en otra capa en Multiplicar, un solo tono más oscuro, borde
   **duro**.
3. **Grano**: capa blanca → Filtro > Ruido > Añadir ruido (25-30 %,
   uniforme, monocromático) → Multiplicar al 15-30 %.
4. **Orden**: fondo → color → luces → sombras → línea → texto → grano.
5. **Pantallas de NERV**: brillo verde o naranja en Sobreexponer color
   sobre negro, y **líneas horizontales finas** al 10 % (efecto de
   monitor de 1995).

Fuentes: [MicahBuzan.com](https://www.micahbuzan.com/cel-shading-tutorial/),
[zombiebass](https://zombiebass.portfolio.site/anime-cel-tutorial),
[Adobe: guía de cel shading](https://www.adobe.com/uk/creativecloud/animation/discover/cel-shading.html)
⚠️ (técnica general, no de Eva).

### Cómo reproducirlo en Blender

1. **Contorno**: modificador **Solidify** con grosor negativo, *Flip
   Normals* y material negro con *Backface Culling*; o **Grease Pencil →
   Line Art**; o **Freestyle** ([StraySpark](https://www.strayspark.studio/blog/how-to-get-anime-toon-look-blender),
   [tutorial de contornos](https://www.youtube.com/watch?v=cO4BDrdUHc0) ⚠️).
2. **Sombreado de celuloide**: **Shader to RGB → Color Ramp en
   Constante**, con dos paradas (luz y sombra) o tres (tono medio). EEVEE
   con *View Transform: Standard*, o Blender suaviza los cortes.
3. **Render**: pásalo por el Compositor y añade grano, como en Photoshop.
4. **Modelos y rigs libres** (licencias leídas en la API de Sketchfab, §4):
   [Asuka con rig, JoeTrekV, CC BY](https://sketchfab.com/3d-models/none-5e66c14e43164330a6dbd4bc863913f7),
   [Unidad 01 con rig, najwanazhiim, CC BY](https://sketchfab.com/3d-models/none-cec471affcb445cb9231bba50267191a),
   [Pen Pen con rig, sirliks, CC BY](https://sketchfab.com/3d-models/none-7672ac8bd3454ff9aee30d270874d01d).
5. **Texturas encima**: las de papel de ambientCG (Punto 19) y el óxido
   verde [Metal038](https://ambientcg.com/view?id=Metal038) (CC0) para la
   jaula.

---

## Punto 19 · Texturas 2D

Junto con §4 (3D) y §5 (texturas reales): no falta ninguna capa.

- **Tramas del manga**: en las páginas de Sadamoto vistas en la hoja del
  manga (nº 146-152, 164 y 172 de `investigar_serie.py`) hay **trama de
  puntos** en fondos y sombras, y **rayado fino** en la tensión. No existe
  un pack de tramas 100 % CC0. Lo mejor gratis:
  - [SuperScreentones, muestra gratis](https://ittaimanero.gumroad.com/l/FREESuperScreentoneSample)
    (Procreate, Photoshop, CSP) ⚠️ licencia de uso, no CC0.
  - [23 pinceles de trama gratis (Graphics Bunker)](https://www.graphicsbunker.com/brushes/free-comic-screentone-procreate-brushes/).
  - [Brusheezy, SCREENTONES Halftone Brushes (Mabecman)](https://www.brusheezy.com/free/halftone), `.abr` de Photoshop.
- **Grano de papel**: [ambientCG](https://ambientcg.com/) `Paper001`,
  `Paper003` a `Paper006`, **CC0** de verdad (comprobado en su API), con
  difuso, normal y rugosidad ✅. Para una tarjeta de plástico, busca
  `Plastic` en la misma web.
- **Patrones de ropa**: el traje de conexión es liso, con paneles. El
  pichi del uniforme de Tokio-3 sí lleva cuadros: no hay textura hecha;
  usa un tartán CC0 genérico y recoloréalo a `#022A51` ⚠️.
- **Emblemas y logos**: el de NERV y el de Evangelion están trazados por
  fans en [Worldvectorlogo](https://worldvectorlogo.com/logo/nerv) y
  [SeekLogo](https://seeklogo.com/free-vector-logos/evangelion). **No son
  libres**: la marca es de Khara. Sirven para ver las proporciones, no para
  pegarlos ⚠️.
- **Pantallas de NERV**: la recreación limpia de
  [Pedro Fleming en Behance](https://www.behance.net/gallery/96540159/Neon-Genesis-Evangelion-Screen-Graphics)
  y el proyecto [nerv-ui](https://github.com/TheGreatGildo/nerv-ui) (MIT).
- **Pincel de tinta**: ⚠️ no verificado. Usa un pincel de tinta gratuito de
  Krita o de Clip Studio y ajústalo con la receta del Punto 18.

---

## Punto 20 · Gustos y detalles de cada personaje

Cumpleaños y altura de las fichas de AniList (que citan *Newtype* y las
guías oficiales). Carácter de §8 y de la [wiki de Evangelion](https://evangelion.fandom.com/wiki/Rei_Ayanami#Personality).
No hay *databook* oficial en español al alcance: los libros son de pago y
en japonés.

| Personaje | Le gusta | Odia | Aficiones | Cumpleaños | Altura |
|---|---|---|---|---|---|
| [Asuka](https://anilist.co/character/94) | Que la reconozcan como la mejor, ganar, Kaji | Perder, que Shinji la supere, que la comparen con su madre | Fue a la universidad en Alemania de niña | 4 de diciembre ✅ | 155 cm ✅ |
| [Rei](https://anilist.co/character/86) | La psicología y la genética (lee un libro en alemán, ep. 9) | ⚠️ nada explícito, coherente con ella | Vive sola, apenas cuida su piso | 30 de marzo ✅ | 149 cm ✅ |
| [Shinji](https://anilist.co/character/89) | El chelo (desde los 5 años), su SDAT, que lo elogien aunque no se lo crea | El rechazo, el conflicto, sentirse una carga | Chelo y música | 6 de junio ✅ | 155 cm ✅ |
| [Misato](https://anilist.co/character/1259) | La cerveza al llegar a casa, celebrar a lo grande | Su trauma del Segundo Impacto (su desorden no le molesta) | Beber y desordenar | 8 de diciembre ✅ | 163 cm ✅ |
| [Kaworu](https://anilist.co/character/1261) | La música, la cultura de «los Lilin», hablar de sentimientos | ⚠️ nada: no rechaza nada humano | Tararear el «Himno de la alegría» | 13 de septiembre ✅ | ⚠️ no está |
| [Gendo](https://anilist.co/character/1257) | El recuerdo de Yui, el control | Perder el control | ⚠️ ninguna fuera de NERV | 29 de abril ✅ | ⚠️ no está |
| [Ritsuko](https://anilist.co/character/1251) | ⚠️ sin lista | Su madre (la admira y la desprecia) | La ciencia, el MAGI | 21 de noviembre ✅ | ⚠️ no está |
| [Pen Pen](https://anilist.co/character/1892) | ⚠️ sin ficha | — | Vive en el refrigerador de Misato | — | — |

**El objeto que siempre lleva**: Asuka, las **pinzas rojas** del pelo;
Shinji, el **SDAT** con auriculares (§8, con minuto); Misato, una **lata de
cerveza Yebisu**: en el fotograma del ep. 2 de la hoja
`vestuario_pantallazos_02.jpg` (nº 91) se lee «YEB…» en la lata ✅ (visto;
ninguna ficha lo dice por escrito).

**Cómo se ve a sí mismo** (de sus frases oídas en latino, §10): Shinji
cree que no vale y que lo quieren sólo si pilota («Todo el mundo me
aprecia y me felicita»); Asuka sólo vale si gana («Nadie desea a una
piloto que no puede controlar a su Eva»); Rei se define por sus vínculos
(«Me convertí en mí a través de… los lazos»).

---

## Punto 21 · Por qué la gente la ama

- **Es la más votada de Japón y de fuera**: la votación oficial de NHK de
  2020 (109.577 votos, §9) y los favoritos de [AniList](https://anilist.co/anime/30)
  dan el mismo podio (§9) ✅.
- **Con quién se identifica el público**: con **Shinji**, «todos nosotros
  en la adolescencia»: miedo al rechazo, no creerse los elogios, querer
  desaparecer. Es la razón más repetida en los foros ⚠️ (Reddit no abre ni
  por Arctic Shift; resumen de foros como EvaGeeks).
- **Premios**: Animage Anime Grand Prix de 1996 a mejor anime; ese año Rei
  y Shinji ganaron mejor personaje femenino y masculino ⚠️ (una fuente).

### Las escenas que hacen llorar

1. **La sonrisa de Rei** (ep. 6). Rei le dice a Shinji «No morirás. Yo te
   protegeré» (00:15:32). Tras el combate, él abre la cápsula y le pide que
   sonría; en el doblaje latino: **«¿Por qué no pruebas sonreír, Rei?»**
   ([00:21:34](https://archive.org/download/26-neon-genesis-evangelion/6%20Neon%20genesis%20Evangelion.mp4?t=1294)).
   Ella sonríe: [fotograma, 21:45](https://archive.org/download/neon-genesis-evangelion-episode-21-he-was-aware-that-he-was-still-a-child-dc-b-3-c-5-af-12/Neon%20Genesis%20Evangelion%20Episode%2006%20Rei%20II%20%5B6F5224E2%5D.mp4?t=1305) ✅.
   - **Por qué duele**: es el único gesto cálido de alguien presentado como
     una muñeca. El público siente que «algo humano sobrevive» en ella.
   - **Cómo está dibujada**: primer plano, mirada de lado, sonrisa pequeña
     (visto). La luz de atardecer y el silencio en el instante exacto van
     de memoria ⚠️.
   - **Cómo reaccionó la gente**: su frase «No morirás» es la **n.º 1** del
     voto de NHK ✅.
2. **Kaworu** (ep. 24). Le confiesa a Shinji que lo quiere; en latino:
   **«¡Yo te amo, Shinji!»** ([00:09:37](https://archive.org/download/26-neon-genesis-evangelion/24%20Neon%20genesis%20Evangelion.mp4?t=577)).
   Poco después Shinji tiene que matarlo con la Unidad 01.
   - **Por qué duele**: es la primera vez que alguien le dice a Shinji que
     lo quiere, y él mismo tiene que destruirlo.
   - **Qué suena**: el «**Himno de la alegría**» de Beethoven en toda la
     escena final ✅ ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Awesome/NeonGenesisEvangelion)).
   - **Cómo está dibujada**: la Unidad 01 sostiene a Kaworu en un **plano
     fijo que dura muchísimo** (Punto 18). Minuto aproximado en el archivo
     combinado 22-24 de Internet Archive: 1:08-1:11 ⚠️.

### Las que hacen reír o gritar

- **Misato y su cerveza** (ep. 2, [00:13:14](https://archive.org/download/evangelion-the-full-series/1.10A%20Neon%20Genesis%20Evangelion%20-%20Episode%202%20%28SUB%29%201920x1080%20-%20Unfamiliar%20Ceilings.mp4?t=794)):
  ojos cerrados, sonrisa enorme ✅.
- **Asuka sale gritando** de debajo de la falda levantada de una
  tripulante (ep. 8, [00:04:04](https://archive.org/download/evangelion-the-full-series/1.70A%20Neon%20Genesis%20Evangelion%20-%20Episode%208%20%28SUB%29%201920x1080%20-%20Asuka%20Arrives%20in%20Japan.mp4?t=244)) ✅.
- **«¡Y la próxima, más servicio!»**: Misato cierra el avance de varios
  episodios (00:23:19, §2) ✅.

---

## Punto 22 · Fan dubs y comunidad hispana

- **Cover cantado del opening en español**: «Evangelion - opening
  español», 90 s, subido por kidabashasha, 13 vistas
  ([Dailymotion x3bwse](https://www.dailymotion.com/video/x3bwse); copia en
  [x4sdbj](https://www.dailymotion.com/video/x4sdbj)). Letra propia, oída
  con `voz.py`: «Con esa sonrisa… / es lo que tú buscas con obsesión / y no
  puedes ver tu destino así / con ojos tan inocentes» (0:32-0:50). Voz
  aguda y muy expresiva ✅. **No es el doblaje oficial**: la canción nunca
  se dobló (§10).
- **Un «fandub» de Asuka**: «cosplay butterfly-fairy (asuka langley soryu)
  evangelion fandub NeoPhantom2007» ([Dailymotion xlka0b](https://www.dailymotion.com/video/xlka0b),
  85 s, 1 vista) ⚠️ no se escuchó.
- **Un AMV, no un fandub**: «Neon Genesis Evangelion - Rammstein - Engel»
  ([Dailymotion](https://www.dailymotion.com/video/x2yjm4k), 4:21, 906
  vistas).
- **Fan dubs de voz completos en español**: ⚠️ no encontrados. YouTube
  pide iniciar sesión y TikTok no tiene buscador abierto. Covers del
  opening sí existen según foros de karaoke, pero no se pudo abrir ninguno
  concreto más que el de arriba.
- **Lo que de verdad mueve a la comunidad hispana**: discutir **cuál de
  los tres doblajes oficiales** es el bueno (original de 1999, *Renewal*
  de 2007-08 y Netflix de 2019), en foros de eldoblaje, grupos de Facebook
  y Atamashi (§10). Es una comunidad del doblaje oficial más que del
  fandub.
- **Memes hispanos propios**: ⚠️ no encontré ninguno. Los memes de Eva
  («Get in the robot», la pose Gendo) circulan en inglés.

---

## Punto 23 · Colaboraciones, figuras y cosplay

Su arte trae poses y ropa que no están en la serie de 1995.

- **The First Descendant × Evangelion** (juego de disparos de Nexon, del
  18-jun al 30-jul-2026): Bunny, Valby y Gley llevan los **trajes de
  conexión de Asuka, Rei y Mari**, con armas, peinados y gestos a juego ✅
  ([Anime News Network](https://www.animenewsnetwork.com/press-release/2026-06-16/the-first-descendant-reveals-details-of-evangelion-collaboration-arriving-june-18/.238581),
  [Siliconera](https://www.siliconera.com/evangelion-characters-join-the-first-descendant-in-new-crossover/)).
- **McDonald's Japón** (6-ene a principios de feb-2026, 30 aniversario):
  tres figuras de Eva que se transforman en comida: Big Mac = Unidad 01,
  patatas = Unidad 02, batido = Unidad 00, con anuncio de TV propio ✅
  ([SNKRDUNK](https://snkrdunk.com/en/magazine/2024/12/19/neon-genesis-evangelion-mcdonalds-value-figurine-set-release-date-price-where-to-buy/),
  [GameRant](https://gamerant.com/mcdonalds-x-evangelion-collab-confirms-release-date-menu-items-exclusive-figures/)).
- **GU × Evangelion** (ropa, dentro de «EVANGELION:30+») ⚠️: sólo sé que
  existe ([SNKRDUNK](https://snkrdunk.com/en/magazine/2025/01/03/evangelion-unveils-30th-anniversary-plans/)),
  sin fotos de las prendas.
- **Ichiban Kuji del 30 aniversario** (lotería de premios de Bandai
  Spirits, desde el 6-feb-2026, 790 yenes la tirada): el premio A es la
  **Unidad 01 desplegando alas**, 43 cm, una pose que no estaba en el arte
  clásico ✅ ([Toy People](https://www.toy-people.com/en/?p=107064),
  [Otaku House](https://shop.otakuhouse.com/en-us/products/ichiban-kuji-evangelion-30th-anniversary-full-set-of-60)).
  Premios B y C fotografiados en la hoja `settei_figuras_03.jpg`, nº 134-135.
- **Pachislot Evangelion Magokoro2** (tragamonedas japonesa) con arte de
  Rei ([imagen oficial](https://static.wikia.nocookie.net/evangelion/images/e/ee/Pachislot_Evangelion_Magokoro2_Rei_3.png)) ✅.
- **Exposición «ALL OF EVANGELION»** (14-nov-2025 a 12-ene-2026, Tokyo
  City View), fotos en [Animate Times](https://www.animatetimes.com/news/details.php?id=1763006385) ✅;
  web del aniversario: [30th.evangelion.jp](https://30th.evangelion.jp/).
- **Figura de escala S-FIRE de Asuka** (*3.0+1.0*): **sentada en la playa
  con las piernas cruzadas**, una pose tranquila muy distinta a las de
  acción ([foto oficial](https://static.wikia.nocookie.net/evangelion/images/e/ea/S-FIRE_Evangelion_3.0%2B1.0_Thrice_Upon_a_Time_Figure_-_Asuka_Langley_1.jpg),
  hoja `settei_figuras_03.jpg` nº 136) ✅.
- **Cosplay**:
  - [Alodia Gosiengfiao, Rei «Grimrock»](https://en.wikipedia.org/wiki/Alodia_Gosiengfiao)
    (Supanova 2010): versión con armadura, sirve de acabado, no de traje
    liso ✅.
  - [SecondImpactCosplay, traje de Rei cosido](https://www.deviantart.com/secondimpactcosplay/art/Rei-Ayanami-Plugsuit-484359771)
    ⚠️ no se miró de cerca.
  - **Lo que no sirve**: los disfraces baratos de licra impresa de tiendas
    en línea. No tienen el volumen de placas del traje real.
- **Evangelion × Fortnite**: ⚠️ **no es real** a fecha de hoy. Circula en
  TikTok, pero ni Epic Games ni Khara la anunciaron.

---

## Punto 24 · Obras parecidas y temas relacionados

### Influencias que reconoce Anno

- **Ultraman**: Anno contó que la idea de los Ángeles le vino de ver, en el
  manga *BASTARD!!*, un ángel **con cara de Ultraman**: «¡así que Ultraman
  era un ángel!» ✅ (en japonés, [500type-eva.jp](https://www.500type-eva.jp/evangelion-ultraman-relationship-explained/)
  y [evamania.net](https://evamania.net/archives/1833)).
- **Space Runaway Ideon** (Tomino, 1980-81): el final de *The End of
  Evangelion* es un homenaje al de *Ideon: Be Invoked* (destrucción total y
  renacimiento) ✅ ([chiebukuronews](https://chiebukuronews.blog.jp/archives/31803850.html),
  [Ameblo](https://ameblo.jp/maumau21floyd/entry-12661092996.html)). Anno y
  Tomino se entrevistaron en *Animage* en julio de 1994 ⚠️
  ([Wave Motion Cannon](https://wavemotioncannon.com/2016/11/08/interview-hideaki-anno-vs-yoshiyuki-tomino-animage-071994/)).
- **Devilman** y el manga de **Nausicaä**: citadas junto a las anteriores
  en repasos japoneses ⚠️ (sin entrevista directa).
- **Kunihiko Ikuhara** (*Utena*, 1997): amigo de Anno; el fandom compara
  las dos series por su tono psicológico ⚠️
  ([TV Tropes: Hideaki Anno](https://tvtropes.org/pmwiki/pmwiki.php/Creator/HIDEAKIANNO)).

### Series parecidas según el público

De las recomendaciones de usuarios de AniList ⚠️ (votos, no lista
oficial): *Serial Experiments Lain*, *Madoka Magica*, *Gurren Lagann*,
*Akira*, *Devilman Crybaby*, *FLCL*, *Gunbuster*, *Sonny Boy*, *Utena*,
*Gundam*, *Berserk*, *RahXephon* (le llaman «el Evangelion pobre»),
*Ideon* y *Darling in the Franxx*. Comparten mecha, trauma y preguntas
sobre quién es uno.

### Otras láminas del servidor

Ninguna biblia usa #demos ni un terminal militar como lámina (búsqueda de
«demos» en `biblias/*/biblia.md`) ✅. En tono se parecen *Attack on Titan*
(02) y *Cyberpunk: Edgerunners* (27), pero van a otros canales: no hay
riesgo de repetir la idea.

---

## Punto 25 · El mundo, la historia y sus símbolos

Todo de [EvaWiki](https://wiki.evageeks.org/Second_Impact), que cita sus
fuentes primarias, y de la Wikipedia japonesa.

### Las reglas del mundo, en cinco líneas

1. En **2000**, el **Segundo Impacto** derritió la Antártida e inundó las
   costas. La ONU dijo «meteorito»; fue el despertar de **Adán** ✅.
2. Los **Ángeles** (使徒, «apóstoles») atacan Tokio-3 buscando a
   **Lilith**, bajo NERV. Sus nombres son de ángeles judeocristianos
   (Sachiel, ángel del agua) ✅ ([note.com](https://note.com/bunnygirlman/n/na6197925aea9),
   [Wikipedia en japonés](https://ja.wikipedia.org/wiki/%E4%BD%BF%E5%BE%92_(%E6%96%B0%E4%B8%96%E7%B4%80%E3%82%A8%E3%83%B4%E3%82%A1%E3%83%B3%E3%82%B2%E3%83%AA%E3%82%AA%E3%83%B3))).
   **La humanidad es el 18.º Ángel** ✅.
3. Sólo los **Eva** (seres vivos con un alma humana dentro, **no robots**)
   crean un **Campo AT** capaz de romper el de un Ángel. Lo atraviesa
   también la **Lanza de Longinus** ✅ ([EvaWiki: AT Field](https://wiki.evageeks.org/AT_Field),
   [Lance of Longinus](https://wiki.evageeks.org/Lance_of_Longinus)).
4. **NERV** (de la ONU) pilota los Eva; **SEELE**, 12 ancianos que sólo se
   muestran como monolitos negros, la controla en la sombra ✅
   ([EvaWiki: Human Instrumentality Project](https://wiki.evageeks.org/Human_Instrumentality_Project)).
5. SEELE quiere el **Tercer Impacto**: fundir todas las almas en una y
   borrar al individuo ✅.

### La historia por arcos

- **Ep. 1-6 · Los Ángeles**: Shinji llega a Tokio-3 y pilota la Unidad 01
  (ep. 1); Rei; se descubre que los Eva **sienten dolor**. Momento clave:
  la sonrisa de Rei (ep. 6).
- **Ep. 8-15 · Llega Asuka**: la Unidad 02 (ep. 8), la vida en el piso de
  Misato, el chelo de Shinji (ep. 15).
- **Ep. 16-24 · El derrumbe**: cada uno choca con su propio muro; la
  Unidad 03 poseída y Toji herido (ep. 18); Kaworu llega y muere (ep. 24).
- **Ep. 25-26 y *The End of Evangelion***: la Instrumentalización; un
  final hacia dentro (TV) y otro apocalíptico (película) ✅.

### Glosario que un fan reconoce al instante

| Término | Qué es |
|---|---|
| **NERV** | Agencia de la ONU. Logo con media hoja de higuera y la frase de Browning «God's in his heaven, all's right with the world» (§7) |
| **SEELE** | Comité en la sombra: 12 monolitos negros «SOUND ONLY» (§7) |
| **MAGI** | Tres superordenadores que deciden por mayoría: **Melchior** (Naoko Akagi como científica), **Balthasar** (como madre) y **Caspar** (como mujer) ✅ ([EvaWiki: MAGI](https://wiki.evageeks.org/MAGI)) |
| **Children** | Los pilotos: Rei, 1.ª; Asuka, 2.ª; Shinji, 3.º; Toji, 4.º; Kaworu, 5.º ✅ ([EvaWiki: Children](https://wiki.evageeks.org/Children)) |
| **Campo AT** | El muro que protege a Ángeles y Eva… y a cada persona |
| **Lanza de Longinus** | Arma roja de dos puntas del tamaño de un Eva |
| **LCL** | Líquido naranja que llena la cápsula; el piloto lo respira ⚠️ |
| **Árbol de la Vida** | Sale en el opening y en el Tercer Impacto. Anno dijo que usaron símbolos cristianos «porque se veían bien» ⚠️ ([ScreenRant](https://screenrant.com/neon-genesis-evangelion-pretentious-hidden-meaning-philosophical-factoid/)) |

**Para la lámina**: usa los símbolos **como estética** (logo, monolitos,
árbol), no como teoría que haya que explicar. Así los trata el propio
Anno.

---

## 19 · Tres conceptos para la lámina de #demos

Los tres usan los textos de §0. Las frases entre comillas de la serie son
**traducción mía del subtítulo japonés**, no del doblaje latino (no las
encontré con fuente; ver §10.3). Recortes siempre por `v3/integrar.py` y
comprobados a 1:1.

### Concepto A — «La ficha del Instituto Marduk» (el objeto del plan, mejorado)

- **Objeto y sitio**: una **carpeta de expediente de NERV** abierta sobre la
  mesa de control de la **sala de pruebas de sincronización**, con el
  cristal de la cámara de prueba detrás. En la carpeta: **una hoja de ficha
  con foto grapada**, una **tarjeta de seguridad NERV** sujeta con clip y un
  **sello rojo**. En Blender: carpeta de cartón con pestaña, hojas con
  curvatura, clip, tarjeta de plástico, sobre una
  [tablilla](https://sketchfab.com/3d-models/clipboard-a37158f20ccf436483029e8295629738).
  Papel: [ambientCG Paper 001](https://ambientcg.com/view?id=Paper001).
  En la tapa, el **logo de NERV** (hoja de higuera + «God's in his heaven,
  all's right with the world.», §7.1).
  Referencias de `referencias.json` (por su posición en la lista): 10 (logo),
  11 y 12 (tarjetas), 16 (tablilla), 20 (papel), 1 (subtítulos con minuto).
- **Por qué este objeto**: en la serie **las fichas se leen en voz alta**
  (Rei, ep. 5, 00:04:25; Kaworu, ep. 24, 00:05:58) y **los papeles
  oficiales llegan al día siguiente** (ep. 17, 00:08:22). Es exactamente un
  hilo de #demos.
- **Personaje**: **Misato**, la que explica. Pose: **tender el folleto**
  (ep. 1, 00:10:16) o **leer la ficha** mirando de reojo (ep. 24, 00:05:58).
  Ropa: **chaqueta roja** y cruz (§16).
- **Cómo habla**: su frase va como **una línea de subtítulo** blanca con
  borde negro fino abajo, en **Noto Serif Display** comprimida:
  **«Que nos enseñe lo que sabe hacer.»** (素直に彼の実力 見せてもらいましょ,
  ep. 24, 00:06:31). Alternativa: **«Lee esto antes.»** (じゃあ これ
  読んどいてね, ep. 1, 00:10:16).
- **Dónde va cada texto**:
  - **Cartela negra** pegada en la tapa, como etiqueta de archivo: **DEMOS**
    (Zen Old Mincho Black o Shippori Mincho B1 ExtraBold, blanca, comprimida
    al 80 %).
  - Pestaña de la carpeta: **Tu ficha de doblaje**.
  - Tres campos de la hoja, escritos a máquina, uno por línea: **Un hilo
    con tu nombre**, **Tus demos**, **Tu rango vocal** (Tinos o Noto Serif
    Display).
  - **Sello rojo** en diagonal: **Lee la ficha fijada antes de abrir la tuya**.
  - En la tarjeta de seguridad: **Ponle tus etiquetas** (y la franja de
    colores de la lámina 2).
  - Post-it amarillo en el borde, en dos líneas: **Tus covers van a
    demos-canto** y debajo **Los papeles, a castings**.
- **Para que no quede plano**: la **tarjeta y un bolígrafo desenfocados en
  primer plano**; luz fría de fluorescente arriba y **brillo naranja de las
  pantallas** a contraluz; el reflejo de Misato en el cristal de la cámara
  de prueba; una esquina de la hoja levantada.
- **Lámina 2**: la **segunda hoja** de la ficha: **«Hoja de selección»**
  con **las 19 etiquetas** en seis bloques (§0) como **casillas para marcar**.
  «Disponible» con tinta verde y «Ocupado» con sello rojo.

### Concepto B — «SOUND ONLY» (Kaworu entre los monolitos)

- **Objeto y sitio**: la **sala de SEELE**: negro total, suelo negro que
  refleja, y **monolitos negros** con su número y **«SOUND ONLY»** en rojo
  (§5.1, §7.1; `referencias.json` 9, 8 y 2). En la serie los miembros
  **sólo ponen la voz, no la cara**:
  es lo que hace un actor de doblaje. En Blender son **losas negras
  brillantes** (fáciles de modelar) con el texto emisivo.
- **Aviso**: en la serie los monolitos son proyecciones; aquí se tratan
  como losas sólidas para que la luz sea real. Si al dueño le parece «panel
  de interfaz suelto», pasa a A o C.
- **Personaje**: **Kaworu**, el 2.º más votado, que llega **enviado por el
  comité** (委員会が直で送ってきた子どもよ, ep. 24, 00:06:07). Pose: la de
  presentarse con la mano abierta (ep. 24, 00:05:36) o sentado con la
  cabeza girada (00:05:13). Uniforme escolar (§16).
- **Cómo habla**: su frase va **en su propio monolito**, el que está
  encendido, en mincho blanca: **«Cantar es bueno. Le da agua al
  corazón.»** (歌はいいね 歌は心を潤してくれる, ep. 24, 00:05:13). Si se
  prefiere una frase de voz y no de canto: **«Llámame Kaworu.»**
  (カヲルでいいよ, 00:05:46), como bienvenida.
- **Dónde va cada texto** (un monolito por idea, numerados como SEELE):
  - Monolito 01, el grande del centro: **DEMOS 01** arriba y **SOUND ONLY**
    debajo, en dos líneas, como «SEELE 01» / «SOUND ONLY».
  - Un texto por monolito (el «·» de aquí sólo separa monolitos; en la
    lámina no va): 02 **Tu ficha de doblaje**; 03 **Un hilo con tu nombre**;
    04 **Tus demos**; 05 **Tu rango vocal**; 06 **Lee la ficha fijada antes
    de abrir la tuya**; 07 **Ponle tus etiquetas**; 08 **Tus covers van a
    demos-canto**; 09 **Los papeles, a castings**.
  - Número de cada monolito en letra tipo Chicago (§6.2) y el texto en
    mincho comprimida.
- **Para que no quede plano**: los monolitos **en semicírculo y a distinta
  distancia** (desenfoque en los de atrás); **reflejo rojo en el suelo**;
  Kaworu con **contraluz** del monolito encendido; uno de los monolitos
  cortado por el borde de la imagen en primer plano.
- **Lámina 2**: **19 monolitos pequeños**, uno por etiqueta, agrupados en
  seis filas (§0), con el nombre del bloque en la base.

### Concepto C — «結構いけるじゃない» (el chelo de Shinji, Asuka aplaude)

- **Objeto y sitio**: el **salón del piso de Misato de noche** (ep. 15,
  00:11:10 → 00:11:44): Shinji toca el **chelo** y **Asuka aplaude**
  apoyada en la puerta. Delante, un **atril con partituras** y el **SDAT**
  con sus auriculares en la mesa baja. En Blender: [chelo](https://sketchfab.com/3d-models/cello-d67ed4cbbc0c4477ba5d89413e715c82),
  atril, hojas, SDAT (a partir de un
  [walkman](https://sketchfab.com/3d-models/sony-walkman-1985-70984e9a3bb4497da196275feb343713)
  y del [render de Delphana Arts](https://www.artstation.com/artwork/gRq1gx);
  `referencias.json` 13, 14, 15, 17 y 18).
- **Por qué esta escena**: es **alguien que enseña lo que hace y otro que le
  responde**. Y Shinji dice lo que siente cualquiera al subir su primera
  demo: «No tengo talento» (才能なんて別にないよ, 00:11:44).
- **Personajes**: **Asuka** (la más votada, cara del 30 aniversario) como la
  que habla; **Shinji** con el chelo, de perfil. Asuka en ropa de casa ⚠️
  (mira el fotograma), **con sus pinzas rojas**.
- **Cómo habla**: su frase como **subtítulo** bajo ella: **«No está nada mal.
  ¿Tenías eso guardado?»** (結構 いけるじゃない そんなの持ってたの？,
  ep. 15, 00:11:37).
- **Dónde va cada texto**:
  - **Cartela negra** arriba, como corte de Anno: **DEMOS**.
  - En la **partitura del atril** (la hoja de arriba), una línea cada uno,
    como títulos de piezas: **Tu ficha de doblaje**, **Un hilo con tu
    nombre**, **Tus demos**, **Tu rango vocal**.
  - **Etiqueta del estuche del chelo**, abierto en el suelo: **Lee la ficha
    fijada antes de abrir la tuya**.
  - **Pantallita del SDAT** (en DotGothic16): **Ponle tus etiquetas**.
  - Nota pegada en la nevera de Pen Pen ⚠️, en dos líneas: **Tus covers van
    a demos-canto** y **Los papeles, a castings**.
- **Para que no quede plano**: el **SDAT y el cable de los auriculares
  desenfocados en primer plano**; luz de lámpara cálida en Shinji y **luz
  azul de noche** desde el balcón; Asuka a contraluz en la puerta; **Pen
  Pen asomando** (el subtítulo lo pone ahí: ペンペン, 00:11:20).
- **Lámina 2**: el **atril con el cuaderno de partituras abierto**: una
  página por bloque de etiquetas (§0), con las etiquetas como títulos de
  piezas.

### ¿Cuál primero?

- **A** si el dueño quiere **el objeto del plan** y la voz que explica.
- **B** si quiere **lo más único**: nadie más en el servidor tendrá los
  monolitos, y «SOUND ONLY» es literalmente un canal de voz.
- **C** si quiere **emoción y la más querida**: Asuka aplaudiendo es un
  momento real y cálido de la serie.

---

## 20 · Lo que no pude verificar

- **Ninguna imagen**: Fandom, tiendas, Sketchfab, Game UI Database, The
  Cutting Room Floor, Fonts In Use y EvaGeeks daban 403. No hay hojas de
  contacto. Todo lo que **se ve** en un fotograma lo describo de memoria.
- **Frases del doblaje latino**: ninguna frase exacta confirmada. «No debo
  huir» es la traducción popular, no sé si la del doblaje.
- **La voz latina original de Gendo** (sólo sé que es un actor mexicano
  nacido en 1957, conocido por Raditz), de **Ritsuko** en el original, y
  el estudio y director del doblaje de ***Renewal*** (Animax).
- **Puestos 4.º a 7.º del voto de NHK** (una fuente).
- **El 6.º Ángel del voto de NHK**: depende de la cuenta (TV o *Rebuild*).
- **Cajas de diálogo de los videojuegos**: no vi ninguna captura.
- **Lo que pone el folleto de NERV** del ep. 1 («ようこそNERV江», de memoria).
- **Licencias exactas** de los modelos de Sketchfab.
- **Colores de vestuario** (hex de memoria).
- **Que *Cross Reflections* se retrase a 2027** (una fuente).
- **Si Evangelion sigue en Netflix Latinoamérica en 2026**: un resumen de
  búsqueda dice que la exclusiva de Netflix acabó en 2025 ⚠️. Míralo en tu
  cuenta antes de citar «en Netflix».
- **Chicago libre** («ChiKareGo2»): no la bajé ni la comprobé.

---

## 21 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)

- WebFetch bloqueado («egress blocked»): sites.google.com (Comunidad
  Evangelion 2015, «Los seiyuus latinos»), xataka.com.mx, anmtvla.com,
  famitsu.com, wiki.evageeks.org.
- curl bloqueado: api.sketchfab.com, gameuidatabase.com, tcrf.net,
  fontsinuse.com, evamonkey.com. Fandom, YouTube, Reddit, Wikipedia y
  Wayback Machine: bloqueados (comprobado en sesiones anteriores, no insistí).
- **GitHub responde** (git y raw). Por eso **no hay `hojas/`**.

### Búsquedas web (49 hechas)

| # | Idioma | Búsqueda (dominio si lo hubo) |
|---|---|---|
| 1 | ES | Neon Genesis Evangelion doblaje latino reparto Shinji Asuka Rei Misato Gendo actores |
| 2 | ES | doblaje latino Roman Sound «Shinji Ikari» voz «Asuka» «Rei Ayanami» doblaje.fandom |
| 3 | ES | Netflix doblaje latino Candiani América Torres Misato Gendo Kaworu reparto completo |
| 4 | ES | «Misato» «Kaworu» Netflix 2019 «Víctor Ugarte» «Circe Luna» «Georgina Sánchez» |
| 5 | ES | Rebuild Prime Video doblaje latino colaborativo reparto Misato Kaworu Mari 2021 |
| 6 | ES | «Misato Katsuragi» doblaje latino «Toni Rodríguez» primer doblaje Locomotion |
| 7 | ES | Netflix latino 2019 «Vivian Magos» OR «Yanelly Sandoval» Misato |
| 8 | JA | エヴァンゲリオン キャラクター 人気投票 結果 1位 公式 |
| 9 | JA | 全エヴァンゲリオン大投票 NHK 好きなキャラクター 好きなセリフ ランキング |
| 10 | ES | frases «no debo huir» «amigo» muletilla primer doblaje |
| 11 | EN | title cards Matisse EB compressed Anno typography Toho NERV Helvetica |
| 12 | EN | NERV monitor graphics UI «EMERGENCY» hexagon orange |
| 13 | JA | エヴァンゲリオン 30周年 キービジュアル 描き下ろし 貞本義行 |
| 14 | JA | NERV IDカード レプリカ 公式 セキュリティカード |
| 15 | EN | Shinji SDAT player real model Sony DAT Walkman replica |
| 16 | EN | Evangelion SDAT / NERV / entry plug / Unit 01 3D (sketchfab.com) |
| 17 | EN | cello / walkman / DAT / folder / clipboard / ID badge free CC (sketchfab.com) |
| 18 | EN | video games Girlfriend of Steel, Raising Project, dialogue box, Battlefields |
| 19 | JA | 鋼鉄のガールフレンド 綾波育成計画 画面 メッセージウィンドウ バトルフィールズ |
| 20 | EN | Cruel Angel's Thesis, Fly Me to the Moon versions, Sagisu, Komm süsser Tod |
| 21 | EN | SEELE monoliths «SOUND ONLY» red text Chicago font |
| 22 | EN | memes Get in the robot, Gendo pose, Congratulations, Pen Pen (Know Your Meme) |
| 23 | EN | real locations Hakone, Lake Ashi, Sengokuhara, Ube-Shinkawa, Hiroshi Katō |
| 24 | EN | plugsuit colors hex palette Unit-01 |
| 25 | EN | wallpaper 4K 3840×2160 (wallhaven, wallpapercave, alphacoders) |
| 26 | EN | fan art Asuka Rei Misato NERV (artstation, deviantart, pixiv) |
| 27 | ES | tráiler oficial Netflix español latino / 3.0+1.0 Prime (youtube.com) |
| 28 | ES | Víctor Ugarte voz de Shinji entrevista; Circe Luna |
| 29 | ES | «Asuka» voz latina primer doblaje «Georgina Sánchez» Renewal Rebuild |
| 30 | ES | «Misato» voz en el doblaje de Netflix actriz 2019 |
| 31 | EN | Sadamoto artbooks Der Mond, Die Sterne, manga covers |
| 32 | JA | 庵野秀明 エヴァ 明朝体 サブタイトル 市川崑 マティスEB インタビュー |
| 33 | ES | 3.0+1.01 doblaje latino Prime Víctor Ugarte Georgina Sánchez Marmac |
| 34 | ES | «Gendo Ikari» voz latina doblaje original actor 1957; Fuyutsuki, Ritsuko |
| 35 | ES | doblaje original «amigo» «amiga» muletilla labios Locomotion Cloverway |
| 36 | ZH | 新世纪福音战士 角色 人气 投票 明日香 绫波丽 渚薰 名场面 哔哩哔哩 |
| 37 | KO | 에반게리온 인기 캐릭터 투표 아스카 레이 카오루 명대사 «도망치면 안 돼» |
| 38 | EN | new Evangelion anime Yoko Taro Tsurumaki Khara CloverWorks 2026 |
| 39 | EN | Cross Reflections VR / Evangelion Battlefields |
| 40 | ES/EN | TikTok tendencia 2025-2026 Komm süsser Tod, Fly me to the moon, Shinji latino |
| 41 | ES | análisis explicado en español, dilema del erizo (youtube.com) |
| 42 | EN | vestuario: Misato chaqueta roja y cruz, Asuka vestido amarillo y pinzas, Rei |
| 43 | EN | Rei NERV security card ep. 5 design |
| 44 | JA | エヴァンゲリオン 公式 YouTube カラー 30周年 特報 アスカ 短編 |
| 45 | EN | CC0 paper / painted metal / concrete (ambientCG, Poly Haven, TextureCan) |
| 46 | EN | Animage Anime Grand Prix 1995-1997 Rei, Shinji, Kaworu |
| 47 | EN | NERV logo fig leaf «God's in his heaven» Browning |
| 48 | ES | Evangelion Netflix sale del catálogo 2025-2026 Latinoamérica |
| 49 | EN | «Marisol Romero» Misato / «Alberto Bernal» Kaworu Netflix latino |

### GitHub (sin cupo)

- [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Shin%20Seiki%20Evangelion):
  bajé **26 subtítulos «Erai-raws … [JPN].ass»** (Netflix, japonés para
  sordos, con nombre de quien habla), los **25 «McBalls» del BD** (para
  comparar tiempos: el BD va 1 s antes) y los **3 de The End of
  Evangelion**. En mi carpeta temporal, **no en el repositorio**.
- [google/fonts](https://github.com/google/fonts): 24 familias comprobadas
  con fontTools (§6.2).
- [TheGreatGildo/nerv-ui](https://github.com/TheGreatGildo/nerv-ui) (MIT):
  paleta y letras de las pantallas de NERV.

### Fuentes consultadas por tipo

- **Oficiales**: evangelion.jp, 30th.evangelion.jp, eva-info.jp, la
  entrevista de Fontworks (route2015.evastore.jp), NHK (voto de 2020, vía
  Famitsu y MANTANWEB), Khara (YouTube, vía noticias), Sony (Walkman SDAT,
  vía ANN).
- **Otros idiomas**: japonés (Famitsu, MANTANWEB, Kimigaku, ねとらぼ,
  Anime!Anime!, 4Gamer, Denfaminicogamer, Dengeki, uakira, CiNii, Excite),
  chino (Zhihu, SMZDM, HK01), coreano (Namuwiki), inglés.
- **Wikis**: Evangelion Wiki (Fandom, EN y ES), EvaGeeks, Doblaje Wiki (sólo
  extractos), Dub Database, Voice over Wiki, Wikipedia (sólo extractos), NERV
  Archives. TV Tropes salió en resultados pero no abre.
- **Foros y comunidades**: foros de eldoblaje.com, EvaGeeks Forum, grupo de
  Facebook, Atamashi, Tumblr. Reddit y Arctic Shift: no accesibles.
- **Arte**: pixiv, ArtStation, DeviantArt, Behance (Pedro Fleming), X
  (Anime Background Art).
- **Vídeo**: YouTube (tráileres, entrevistas, análisis), TikTok, iVoox.
- **Código y recursos**: GitHub, Sketchfab, ambientCG, Poly Haven,
  TextureCan, color-hex, Brand Palettes, alphacoders.
- **Doblaje latino**: Doblaje Wiki (extractos), Dub Database, Cine Premiere,
  Xataka, ANMTV, MasGamers, Atomix, LevelUp, Infobae, Somos Kudasai, Código
  Espagueti, DubZoneLA.

### Lo que NO encontré

- Imágenes: no se pudo bajar nada; sin hojas de contacto.
- Frases exactas del doblaje latino.
- Voz latina original de Gendo y de Ritsuko; estudio de *Renewal*.
- Capturas de las cajas de diálogo de los juegos; The Cutting Room Floor
  y Wayback Machine, bloqueados.
- Una encuesta oficial en Latinoamérica.
- Qué pone exactamente la tarjeta de seguridad de NERV (campos, código).
