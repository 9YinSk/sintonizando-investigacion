---
tags: [biblia, serie, laminas]
serie: "Dr. Stone"
canal: "#hardware"
fecha: 2026-09-24
---

# Biblia · Dr. Stone — para #hardware

> [!important] Cómo se hizo, y sus límites
> - **Primera pasada** (24-sep-2026, mañana): red cerrada. Sólo buscador
>   (48 búsquedas en español, inglés, japonés, chino y coreano) y GitHub.
>   De ahí salen **los subtítulos japoneses de Netflix de toda la serie**
>   ([Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv)),
>   con el nombre de quien habla: dan el minuto de cada escena en formato
>   `00:19:25`. Es el minuto del archivo de Netflix: puede moverse uno o dos
>   minutos en Crunchyroll.
> - **Segunda pasada** (24-sep-2026, tarde): **red abierta**, con el
>   método de equipo (`EQUIPO.md`): el recolector gratuito
>   (`herramientas/recolectar.py`: AniList, Doblaje Wiki, Fandom, Wallhaven,
>   Sketchfab, Openverse, Dailymotion, Internet Archive, MusicBrainz, Steam,
>   Reddit) y cuatro investigadores (imagen, vídeo, voz, texto). Sus notas
>   están en `partes/`. Lo nuevo de esta pasada va marcado **«2.ª pasada»**.
> - **Qué se pudo usar ahora**: la API de la wiki de Dr. Stone (tamaños
>   reales de cada imagen), **3 hojas de contacto** en `hojas/`, la API de
>   Doblaje Wiki (reparto completo), la API de Sketchfab (licencias), la de
>   ambientCG (texturas CC0), Arctic Shift (Reddit) y **vídeos mirados de
>   verdad** con `fotogramas.py`: el opening 1 sin créditos en 1080p, cinco
>   tráileres oficiales (Dailymotion) y cuatro episodios de la temporada 1
>   (Internet Archive). Los minutos de esos vídeos van en formato `16:53` y
>   con enlace `?t=`.
> - **Colores medidos** con `herramientas/estilo.py` y Pillow sobre
>   fotogramas y hojas de modelo oficiales (dice de cuál en cada tabla).
>   Voces medidas con `herramientas/voz.py` sobre muestras de Doblaje Wiki.
> - **Lo que siguió cerrado**: YouTube pide iniciar sesión desde este
>   servidor (los clips doblados oficiales no se pudieron bajar otra vez),
>   dr-stone.jp da 403, TikTok no sirve los vídeos, AnimeThemes caído.
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su minuto, o
>   se vio en el fotograma. ⚠️ **dudoso**: una sola fuente, o de memoria.
> - Las traducciones de los subtítulos japoneses son **mías**, no del
>   doblaje latino. Las frases latinas comprobadas están en §10.
---

## Segunda pasada · qué cambió

Repaso del 24-sep-2026 con la red abierta. Sólo con lo que trajeron las
partes (`partes/imagen.md`, `video.md`, `voz.md`, `texto.md` y los
`datos-*.md`). Nada inventado: lo que no se encontró sigue con ⚠️.

**Corregido (antes → ahora)**

- **Pelo de Senku**: `#7DBF4A` verde manzana, de memoria → **`#5D906A`
  verde salvia** en la luz y **`#2E5538`** en la sombra, medido en el
  retrato oficial ✅ (§16).
- **Túnica de Senku**: «blanca» → **crema cálido `#F5EBD6`**, medido en un
  fotograma y confirmado por un cosplay real ✅ (§16).
- **El dinero Drago**: «billetes» → **monedas acuñadas** de 500, 1.000,
  5.000 y 10.000, con un perfil grabado y el nombre de una aleación ✅
  (`Drago_Coins.png`, §3).
- **La hoja de ruta**: «existe; el aspecto ⚠️» → vista entera: árbol de
  habilidades de videojuego, con «START!» y «GOAL», flechas-tubo con trama
  de puntos ✅ (§3 y §7).
- **Paleta de los sitios**: 10 hex «de memoria» → **8 sitios medidos** en
  fotogramas con `estilo.py`, con minuto y enlace (§5).
- **Música**: el ending 2 y el de *New World* 2.ª parte estaban en ⚠️ o
  ambiguos → confirmados con dos fuentes; «Haruka» es **opening**, no
  ending. Añadida toda la música de *Science Future* (§11).
- **Estudio latino**: Audiomaster Candiani ⚠️ → ✅ (ficha de Doblaje Wiki por
  la API). Tsukasa = Arturo Cataño pasa a ✅ (§10).
- **Caja de diálogo del videojuego**: «no encontré capturas» → vista en la
  ficha de Google Play y medida: bisel turquesa sobre azul verdoso (§7 y
  §13).
- **Licencias de Sketchfab**: «no se pudo leer» → **CC BY** comprobada por
  la API en 8 modelos; el megáfono es «Free Standard» (§4).

**Añadido**

- **Las hojas de contacto** (sección nueva, antes de §19): `arte_01`,
  `vestuario_01` y `settei_01`, con qué número sirve para qué.
- **Vídeos mirados de verdad**: opening 1 sin créditos, 5 tráileres y 4
  episodios, con **fotogramas descritos y minuto `?t=`** (§2, §12, §15).
- **Reparto latino completo** (secundarios, niños, cambios de voz, los
  cuatro directores) y **voces medidas** de Gen y Senku con `voz.py` (§10).
- **Trivia de cada personaje** (muletillas, alergias, objetos) en §8.
- **Los puntos 18 a 25 del encargo**, que no existían: técnica y cómo
  replicarla, texturas 2D, gustos y detalles, por qué la aman, fan dubs,
  colaboraciones, obras parecidas y el mundo con sus símbolos (§18.1 a
  §18.8, entre la guía para IA y los conceptos).
- **Tabla «Cumplimiento del encargo»** antes de la bitácora, y un apartado
  de la segunda pasada en la bitácora.
- `referencias.json`: de 35 a **183**, todas las útiles de las partes y
  del recolector, con tamaños medidos (108 con ancho y alto), las mejores
  primero. Se quitaron los enlaces a páginas cuando había la imagen
  directa, y lo que no era de la serie (juegos de Steam con «Stone» en el
  nombre, fotos de otras cosas).
- **Gen**: su cicatriz cambia con lo que hace, su ropa de día es una
  túnica lila (a ojo en las hojas, sin medir ⚠️) y **en latino habla
  normal**, sin la jerga al revés (Doblaje Wiki).
- **Popularidad fuera de Japón**: en AniList y en los premios de
  Crunchyroll gana **Senku**; en las encuestas de Jump, **Gen** (§9).
- «Tratamiento acústico: no existe en la serie» → «**no la encontré**» en
  los subtítulos (el encargo manda: nunca «no existe»).

**Los ⚠️**: había **96**. Se resolvieron unos 25; el total sube porque se
añadió mucho dato nuevo con una sola fuente. Detalle al pie de la tabla de
cumplimiento.

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección EL ESTUDIO):

> **ıı・🎛️・hardware** (foro) · 2 hilos · etiquetas: Micrófono, Interfaz,
> Auriculares, Cámara, Tratamiento acústico, Menos de 50, De 50 a 150,
> De 150 a 400, Más de 400, Lo tengo y lo recomiendo, No lo compres,
> Alternativa barata — _Micros, interfaces, auriculares y cámaras, **con el
> precio delante**. Un hilo por cacharro. Si lo tienes, di cómo te fue de
> verdad._
> - 📌 Cómo se recomienda algo aquí (1 msj)
> - EJEMPLO · Fifine K669 — unos 35 USD (0 msj)

Función según el encargo: **foro de micrófonos, interfaces y auriculares
con el precio delante (rangos de precio)**.

> [!warning] Dos cosas que el dueño tiene que confirmar
> - **La moneda de los rangos.** Las etiquetas dicen «Menos de 50», «De 50
>   a 150»… sin moneda. El hilo de ejemplo dice «unos 35 USD». Supongo
>   **dólares (USD)** ⚠️. En la lámina conviene escribir «USD» una vez.
> - **El texto del mensaje fijado** («Cómo se recomienda algo aquí») no
>   está en el inventario: sólo su título. No lo invento.

### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Hardware** | nombre del canal |
| 2 | **Micros, interfaces, auriculares y cámaras** | de qué se habla |
| 3 | **Con el precio delante** | la regla de oro |
| 4 | **Un hilo por cacharro** | cómo se abre un hilo |
| 5 | **Si lo tienes, di cómo te fue de verdad** | la reseña honesta |
| 6 | **Ejemplo: Fifine K669, unos 35 USD** | así se titula (sin raya) |
| 7 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

### Los textos de la lámina 2 (las 12 etiquetas)

Las etiquetas no caben con lo de arriba. Propongo **lámina 2**, en tres
grupos, como las tres columnas de una **hoja de ruta de Senku** (ver §7):

| Grupo | Etiquetas |
|---|---|
| **Qué es** | Micrófono · Interfaz · Auriculares · Cámara · Tratamiento acústico |
| **Cuánto cuesta** | Menos de 50 · De 50 a 150 · De 150 a 400 · Más de 400 |
| **Qué opinas** | Lo tengo y lo recomiendo · No lo compres · Alternativa barata |

(En la lámina, cada etiqueta en su propia pieza; los «·» de esta tabla
son sólo para leerla aquí.)

La serie da **un objeto real para cada etiqueta** (todo con minuto en §2):

| Etiqueta | Objeto de Dr. Stone | Dónde |
|---|---|---|
| Micrófono | megáfono de plástico con **sal de Rochelle** pegada | 1×23, 00:19:25 |
| Interfaz | el **tubo de vacío** («el engranaje de los electrones») que convierte y amplifica | 1×21, 00:14:01 |
| Auriculares | la **«インカム»** (intercomunicador) escondida en un pendiente: bobina de cobre y sal de Rochelle en el gancho de la oreja | New World, 3×10, 00:00:21 |
| Cámara | la **cámara de daguerrotipo** de Kaseki, «la más antigua de la historia» | New World, 3×02, 00:17:19 |
| Tratamiento acústico | no hay escena propia ⚠️. Lo más cercano: **el oído de Ukyo** (sonar) y la **grabación del disco** en cristal | 1×24, 00:12:28 |
| Precios | la **ドラゴ (Drago)**, la moneda que imprime Ryusui | especial *Ryusui*, 00:20:56 |
| Alternativa barata | «**Esto es lo más rentable**» (コスパ最強, Gen) y «la radio de galena: **no necesita pilas**» | 3×04, 00:19:01; 3×10, 00:03:04 |

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué Dr. Stone encaja | Porque **Senku fabrica de verdad un micrófono** en la Edad de Piedra. En 1×23 (00:19:25) dice: «Vamos a hacer **las cuerdas vocales del móvil: el micrófono**». Lo hace con **sal de Rochelle** del poso del vino, pegada a **un megáfono de plástico** ✅. Luego saca un altavoz, un tocadiscos, una cámara y un auricular escondido en un pendiente. Todo con minuto en §2. |
| El objeto | **El banco de trabajo del laboratorio** (la «ラボ» de 1×11, 00:16:49) con **el megáfono-micrófono**, los **tubos de vacío** de Kaseki, el hilo de oro y la caja del **teléfono**. En Blender: banco de madera, megáfono, tubos de vidrio, cristales, cables y etiquetas de madera colgadas. |
| El precio delante | La serie tiene **su propia moneda, el Drago** (ドラゴ), que emite Ryusui ✅ (especial *Ryusui*, 00:20:56). Y una tienda: **«Grandes Almacenes Senku»** (デパート千空), idea de Gen, con **precios y un artículo de lujo** que sólo compra Ryusui ✅ (especial, 00:33:38 y 00:35:36). |
| Cuadro de diálogo propio | No es un globo. Son **la hoja de ruta de Senku** (科学ロードマップ: cajas unidas por flechas hasta el invento final) y el **«¡…, listo!»** (クリア) que grita cada uno al terminar su pieza (1×23, 00:21:04). Para explicar, **Mecha Senku** (メカ千空), el robot que sale en una esquina a dar recetas (1×04, 00:05:08). Y para las etiquetas, **el test de Gen**: «A… B… C… ¡Correcto! Diez mil millones de puntos» (2×01, 00:15:25). |
| El más querido | **Gen Asagiri**. Ganó la encuesta oficial de 2023-2024 con **41.317 votos** ✅ (dos fuentes) y la de 2021 (1.º Gen, 2.º Senku, 3.º Ryusui) ⚠️ (una fuente). Senku ganó las dos primeras, 2018 y 2019 ⚠️. En 2021 Chrome fue 7.º, Suika 12.ª y Kaseki no entró en el top 20. |
| Gen y el doblaje | Gen es **mentalista e imitador de voces**. En *Stone Wars* imita a la cantante Lillian por teléfono y se aprovecha de que **el teléfono suena fatal** (2×01, 00:16:21). Una superfán, Nikki, **le corrige como una directora de doblaje** (2×07, 00:03:06). Para este servidor, es perfecto. |
| Voz latina | Senku **Alejandro Orozco**, Chrome **José Luis Piedra**, Gen **Brandon Santini**, Kaseki **Óscar Rangel**, Suika **Valeria Mejía** ✅. Estudio **Audiomaster Candiani** (México) ✅ (2.ª pasada: ficha de Doblaje Wiki por la API). Gen cambia de voz en el ep. 76: **Iván García**. Frases: «**10 mil millones por ciento**» (Senku) y «**¡Qué malote!**» (Chrome) ✅. |
| Letras | **Kalam** o **Caveat** (notas a mano de Senku), **Anton** o **Rubik Dirt** (título de piedra), **Oswald** (precios), **Yusei Magic** (algún kanji a mano). Todas con tildes, ñ, ¿ y ¡ (comprobado en el archivo). |
| Colores medidos (2.ª pasada) | Túnica de Senku **`#F5EBD6`** (crema, no blanca), pelo **`#5D906A`**/**`#2E5538`**, ojos **`#59050F`**; camisa de Chrome **`#245E6B`**; poncho de Suika **`#373C42`**; laboratorio en grises piedra **`#B0B1A2`**/**`#848276`**. Detalle en §5 y §16. |
| Tono | **Alegre, curioso y de taller**: madera, piedra, vidrio soplado, cobre, fuego de horno, verde del bosque. Humor constante. Nada de ciencia de laboratorio blanco y limpio. |
| Lo que se vio en vídeo (2.ª pasada) | La hoja de ruta del móvil ([1×19, 21:07](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1267)), el laboratorio por dentro ([1×11, 16:53](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1013)), la sal de Rochelle en un vaso ([1×23, 19:49](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1189)) y la torre con la bocina de cobre ([1×24, 2:17](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=137)). |
| Tres conceptos (§19) | **A** «¡Micrófono, listo!» (Senku en el laboratorio). **B** «Grandes Almacenes Senku» (Gen vende, con los precios). **C** «La primera llamada» (Chrome y Suika prueban el teléfono: la reseña honesta). |

---

## 2 · Las escenas que sirven para #hardware (con minuto)

Todo sale de los **subtítulos japoneses de Netflix (con acotaciones de
sonido y nombre de quien habla)**, del repositorio
[Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Dr.%20STONE).
El texto y el minuto están comprobados ✅. La traducción al español es mía.
Lo que **se ve** (postura, luz) lo describí de memoria en la primera
pasada ⚠️. **2.ª pasada**: diez de estas escenas ya se miraron en vídeo,
fotograma a fotograma; están en §2.5 con su enlace. El minuto es el del archivo de Netflix; en
Crunchyroll puede moverse uno o dos minutos.

**Cómo leo los episodios**: «1×23» es temporada 1, episodio 23.
«2×» es *Stone Wars* (2021). «Especial» es *Ryusui* (2022, un solo
episodio de 54 min). «3×» es *New World* (2023, 22 episodios).
«4×» es *Science Future* (2025-2026, 37 episodios en tres partes).

### 2.1 El gran proyecto: Senku fabrica un micrófono (1×19 a 1×24)

Es **la escena del plan**, y existe de verdad. En la temporada 1 Senku se
propone fabricar **un teléfono móvil en la Edad de Piedra** para ganar la
guerra contra Tsukasa. Lo divide en piezas y cada equipo hace una. **La
última pieza es el micrófono.**

| Escena | Minuto | Qué se dice (japonés) | Traducción mía | Para qué sirve |
|---|---|---|---|---|
| 1×19 | 00:20:42 | 大樹「スマホか？」千空「いいな スマホ！」 | Taiju: «¿Un smartphone?». Senku: «¡Qué buena idea, un smartphone!» | Arranca el proyecto |
| 1×19 / 1×20 | 00:21:07 / 00:00:07 | まあ 今回はスマートじゃなく― ただのホーンだがな | «Bueno, esta vez no será *smart*. Sólo *phone*» | Humor de Senku |
| 1×19 / 1×20 | 00:21:32 / 00:00:32 | どんだけ遠くに見えようがな― ルールをたぐれば １００億％ゴールに着く それが科学だ！ | «Por lejos que parezca, si sigues las reglas llegas a la meta al diez mil millones por ciento. ¡Eso es la ciencia!» | **Frase para la lámina 2** (los rangos como camino) |
| 1×21 | 00:13:00 | 携帯作りのロードマップ | «La hoja de ruta del móvil» | La hoja de ruta (ver §7) |
| 1×21 | 00:14:01 | コンピューターの卵を作る 電子のギア 真空管だ | «Vamos a hacer el huevo de un ordenador: el engranaje de los electrones, **el tubo de vacío**» | **Interfaz** |
| 1×21 | 00:14:25 | 高熱で電子をブチ飛ばして 電流の向きをそろえたり パワーアップしたりする | «Lanza electrones con calor, ordena la corriente y **la amplifica**» | Qué hace una interfaz/previo |
| 1×23 | 00:18:25 | 作り方説明書と材料 用意してあんぞ | «Te dejé preparados el manual y los materiales» (a Gen) | Gen fabrica **800 pilas** |
| 1×23 | 00:18:43 | ♪ 海苔は亜鉛 おにぎりのマンガン… | **La canción de la pila de manganeso** de Gen («el alga es el zinc, el arroz es el manganeso…») | Meme, gancho de humor |
| 1×23 | 00:19:10 | それを800個な / えっ 800個!? / ドイヒ～ | «Pues 800». «¿¡800!?». «¡Qué crueldad!» (ドイヒー, jerga de Gen) | Humor |
| 1×23 | 00:19:25 | 携帯の声帯 マイクを作る | «Vamos a hacer **las cuerdas vocales del móvil: el micrófono**» | **La frase del canal** |
| 1×23 | 00:19:33 | ワインの栓とかに こびりついてる― ピンクの粒な | «Las bolitas rosas que se pegan al corcho del vino» | El material |
| 1×23 | 00:19:43 | コハク「そのマイクとやらは 一体 どれなのだ？」 | Kohaku: «¿Y cuál de todo esto es el tal micrófono?» | Pregunta de novato |
| 1×23 | 00:19:49 | ロッシェル塩つってな 音を電気に変える | «Se llama **sal de Rochelle**. **Convierte el sonido en electricidad**» | Explicación |
| 1×23 | 00:19:55 | プラスチックのメガホンにでも 貼り付けりゃ マイクの完成だ | «La pegas en algo ligero, un **megáfono de plástico**, y ya tienes el micrófono» | **El objeto** |
| 1×23 | 00:21:04 a 00:21:16 | クロム「プラスチック クリアだぜ！」 スイカ「電線 クリアだよ～！」 カセキ「真空管 クリアじゃ～い！」 コハク「マイク クリアだ！」 | Chrome: «¡Plástico, listo!». Suika: «¡Cables, listo!». Kaseki: «¡Tubo de vacío, listo!». Kohaku: «**¡Micrófono, listo!**» | **Cada uno con su pieza**: pose de grupo (se repite en 1×24, 00:00:03 a 00:00:10) |
| 1×23 / 1×24 | 00:21:22 / 00:02:17 | 無限のかなたに声を届ける 現代戦最強武器… 携帯の爆誕だ！ | «El arma más poderosa de la guerra moderna, la que lleva **la voz hasta el infinito**… ¡Nace el móvil!» | Presentar |
| 1×23 | 00:22:12 | 唆るぜ これは！ | «¡Esto sí que me emociona!» (ver §10: la frase del doblaje no la encontré) | Cierre |
| 1×24 | 00:02:56 | いっけね もう１台 必要だったわ～ | «Uy, se me olvidó: hacía falta **otro aparato**» (para recibir) | Humor: «ahora compra otro» |
| 1×24 | 00:03:01 | ゲン「最初っから２台って言うと みんな作ってて 心折れるから」 | Gen: «Si decías desde el principio que eran dos, a todos se les caía el alma» | Humor |
| 1×24 | 00:04:19 | 通話スイッチ！ / スイカ「オンなんだよ！」 | «¡Botón de llamada!». Suika: «¡Encendido!» | Probar el aparato |
| 1×24 | 00:04:34 | 見たか ルリ ヤベえだろ！ 科学はよ！ | Chrome: «¿Lo ves, Ruri? ¡La ciencia es la bomba!» | **Primera prueba de micro** |
| 1×24 | 00:04:55 | マグマ「なんで こんな小せえのが しゃべんだよ？」 | Magma: «¿Por qué habla una cosa tan pequeña?» | Humor |
| 1×24 | 00:05:03 | マイクとスピーカーは 音と電気を変換するだけで 同じもんに… | «**El micrófono y el altavoz son lo mismo**: sólo convierten sonido en electricidad y al revés» | Explicar |
| 1×24 | 00:09:24 a 00:09:39 | レコードの仕組みは アホほど簡単だ… 音で針を震わせて ガッタガタに溝を彫る | «El disco es facilísimo: el sonido hace vibrar una aguja, que talla un surco…» | Grabación |
| 1×24 | 00:11:41 | レコードプレーヤーは… わたあめ機のギアも使う | «El tocadiscos se hace con piezas que ya tenemos: el engranaje de **la máquina de algodón de azúcar**» | Reciclar |
| 1×24 | 00:12:28 | だが録音側は そうはいかねえ ガラス削るんだから 硬え石がいる | «**Grabar** es otra cosa: para rayar vidrio hace falta una piedra durísima» | Grabar cuesta más |
| 1×24 | 00:12:39 | ダリヤ「これ 使ってよ」 | Daria da **su anillo de boda (diamante)** para la aguja de grabación | Lo caro de verdad |
| 1×24 | 00:13:56 a 00:14:09 | （スピーカーのノイズ）百夜「私は宇宙飛行士の 石神百夜と申します」 | Ruido del altavoz y **la voz grabada de Byakuya** | Escuchar |
| 1×24 | 00:15:53 | （リリアンの歌声） | **La canción de Lillian** suena en el disco | Canto |
| 1×24 | 00:18:25 | ゲーム テレビ 漫画 映画… 科学の進歩で作れるようになった エンタメどもだ | «Juegos, tele, manga, cine… **el entretenimiento que la ciencia hizo posible**» | Por qué importa el equipo |

### 2.2 La voz: Gen imita voces y el sonido malo del teléfono (*Stone Wars*)

Gen Asagiri es **mentalista y hace imitaciones de voz** (声帯模写). Para
un servidor de doblaje es oro.

| Escena | Minuto | Qué se dice | Traducción mía | Para qué sirve |
|---|---|---|---|---|
| 1×20 | 00:01:04 | （ゲン：司の声） | Gen **imita la voz de Tsukasa** | Imitación |
| 1×20 | 00:01:18 | 似すぎだろ テメーの声帯模写 | «**Tu imitación de voz** se parece demasiado» | Elogio |
| 2×01 | 00:15:25 | Ａ 食べ物 Ｂ 美女 Ｃ 司ちゃん自身 / ピンポーン 100億点 | Gen hace **un test de tres opciones**: «A, comida; B, mujeres; C, el propio Tsukasa». «¡Correcto! **Diez mil millones de puntos**» | **Molde para la lámina 2** (A, B, C… como etiquetas) |
| 2×01 | 00:15:56 | （ゲン：リリアンの声）Hi！ I'm Lilian Weinberg！ | Gen imita a Lillian | Imitación |
| 2×01 | 00:16:13 | さすがに100億％ 偽って分かるわ 男の声じゃ | Senku: «Se nota al diez mil millones por ciento que es falso. Es voz de hombre» | Crítica honesta |
| 2×01 | 00:16:21 | でもね 音質 荒れ荒れの うちらの電話越しだったら？ | Gen: «Pero ¿y si suena **por nuestro teléfono, con un sonido malísimo**?» | **Calidad de audio** |
| 2×01 | 00:16:28 | んで レコードの歌が身分証か / ピンポーン 1000億点 | «Y el disco con su canto sirve de carné». «¡Cien mil millones de puntos!» | Humor |
| 2×07 | 00:03:06 | ガチファン ニッキーちゃんの― スパルタ特訓のおかげで― リリアンちゃんのマネっこ再現度は バッチリよ / ニッキー「違う！ 全然 違う！」 | Gen: «Gracias al **entrenamiento espartano** de Nikki, la superfán, mi imitación de Lillian está perfecta». Nikki: «¡No! ¡Nada que ver!» | **Una directora de doblaje** corrigiendo |
| 2×07 | 00:08:20 | ガチファンの ニッキー先生に― 満点もらった 俺のモノマネＶＳ― 羽京ちゃんの聴力で イチかバチかの勝負 | «Mi imitación, con **nota máxima** de la profe Nikki, **contra el oído de Ukyo**: todo o nada» | El oído fino |
| 2×07 | 00:08:37 | 羽京「すごいね 本当にリリアンだ」 | Ukyo: «Impresionante. **Es Lillian de verdad**» (y los deja pasar) | Aprobar |
| 2×08 | 00:17:21 | （ゲン：リリアンの声）Don't worry！ | Gen, de Lillian, por el teléfono | Imitación |
| 2×08 | 00:17:41 | 氷月「こんな原始的な携帯電話で― アメリカまで 通話できるわけないでしょう」 | Hyoga: «Con **un móvil tan primitivo** es imposible llamar a América» | Límite del aparato |
| 4×23 | 00:03:10 a 00:06:21 | （スイカ：松風の声マネ）（スイカ：フランソワの声マネ）（スイカ：銀狼の声マネ）… | **Suika imita las voces** de Matsukaze, François, Ginro, Ryusui, Ukyo y Kohaku, sola durante años: «さみしいんだよ» (me siento sola) | Emoción. Suika también imita voces |
| 4×36 | 00:05:23 / 00:07:51 | 千空のマイクの周波数と 声色を使った偽通信 / 俺の声マネで偽の通信 | Ukyo: «Una transmisión falsa con **la frecuencia del micro de Senku** y su timbre». Senku: «alguien me imitó la voz» | Imitación como amenaza |

### 2.3 Auriculares, cámara, sonar, radio (*New World* y *Science Future*)

| Escena | Minuto | Qué se dice | Traducción mía | Etiqueta |
|---|---|---|---|---|
| 3×02 | 00:17:19 | ダゲレオタイプ 人類史上 最古の… カメラだ | «Un daguerrotipo: **la cámara más antigua** de la historia» | **Cámara** |
| 3×02 | 00:18:12 | 南「私のカメラ」 | Minami, la periodista, llora: «**Mi cámara**» (la perdió hace miles de años) | Cámara, emoción |
| 3×02 | 00:18:31 | 人類がゼロから文明を作ってく… 新世界の記録を | «Voy a fotografiar cómo la humanidad rehace la civilización desde cero» | Cámara |
| 3×03 | 00:00:36 | カセキ「オッホホー さっすが ワシの かわいいカメラたち」 | Kaseki: «¡Oh-ho-ho! Así se hace, **mis camaritas**» | Kaseki fabrica cámaras |
| 3×04 | 00:08:03 | 見えない敵が見える— 科学の眼 | «Ver al enemigo invisible: **el ojo de la ciencia**» (radar) | — |
| 3×04 | 00:08:13 | 接続先をアンテナから マイクに変えりゃ 海中のソナーにもなる / 羽京 てめえの専門だ | «Si cambias la antena **por un micrófono**, es un sonar bajo el mar. Ukyo, eso es lo tuyo» | **Micrófono** + Ukyo |
| 3×04 | 00:19:01 | ゲン「コスパ最強だよね」 | Gen: «**Es lo más rentable que hay**» (el asfalto: 90 % grava) | **Alternativa barata** |
| 3×10 | 00:00:21 a 00:01:00 | 銅線グルグル巻きのリングが 飾り本体と見せて まんまコイルだ / 耳にかけるフックには ワインから採ったロッシェル塩を 貼り付ける / 遠隔で指示が出せる— 超絶便利な スパイアイテム インカムの完成だ | «El aro de cobre enrollado parece un adorno, pero **es una bobina**. En **el gancho que va en la oreja** pego sal de Rochelle, la del altavoz. Un aparato espía para recibir órdenes a distancia: **¡el intercomunicador!**» | **Auriculares** |
| 3×10 | 00:03:04 | 要らねえぞ つけっぱで永遠に聞ける / 仕組みとしちゃ 鉱石ラジオっつうやつだ / 音はアホほど小せえがな | «**No necesita pilas**: lo dejas puesto y escuchas para siempre. Es una **radio de galena**. Eso sí, **el sonido es bajísimo**» | **Alternativa barata** (y su pega) |
| 4×08 | 00:17:02 | 通話は全て録音している | «**Grabamos** todas las llamadas» | Grabación |
| 4×19 | 00:17:45 a 00:17:55 | 物見やぐらのタワーに メデューサ＆スピーカー / マイクは砦ん中 あらゆる場所にアホほど伸びてる / 襲われたその瞬間 誰かがマイクに叫びゃいい | «En la torre, la Medusa y **el altavoz**. **Los micros**, por todo el fuerte. Si nos atacan, basta con **gritar al micro**» | Micrófono |

### 2.4 El precio: la moneda Drago y «nada es gratis»

| Escena | Minuto | Qué se dice | Traducción mía | Para qué sirve |
|---|---|---|---|---|
| 1×01 | 00:01:57 a 00:02:03 | 「フラれるに100円」「300円」「500円」 千空「意外とフラれねえに１万円」 | Los del club apuestan **100, 300 y 500 yenes** a que rechazan a Taiju. Senku: «**Diez mil** a que no» | Rangos de precio en el ep. 1 |
| 1×09 | 00:05:50 | ともかく世の中 タダ食いはねえ | Senku: «**En este mundo nada es gratis**» | Con el precio delante |
| Especial | 00:20:56 | 龍水財閥の発行する通貨 ドラゴだ | Ryusui: «**El Drago**, la moneda que emite el grupo Nanami» | La moneda |
| Especial | 00:20:59 | この100ドラゴで １ミリリットル 石油を売ってやる | «Por **100 dragos** te vendo **un mililitro** de petróleo» | Precio con cifra |
| Especial | 00:21:54 | 通貨も立派な科学の発明品だ 人の力をまとめ上げる | Senku: «La moneda también es **un invento de la ciencia**: une la fuerza de la gente» | Por qué importa el precio |
| Especial | 00:33:33 a 00:33:38 | ゲン「商品 作って売ったら いいんじゃないの？」「フッ デパート千空」 | Gen: «¿Y si hacemos productos y los vendemos?». «**Grandes Almacenes Senku**» | **La tienda de Senku** (ver §19) |
| Especial | 00:34:29 a 00:34:57 | （ゲン）エスニックな雰囲気の セットアップには… | Gen **presenta un desfile de ropa como un locutor de moda**, prenda por prenda | Gen «vendiendo» |
| Especial | 00:35:12 | 未来「めちゃ高っ」 | Mirai: «**¡Carísimo!**» | Reacción al precio |
| Especial | 00:35:27 | あずら「すてきなんだけど値段がね」 | Una aldeana: «Es precioso, **pero el precio…**» | «Pero el precio» |
| Especial | 00:35:36 | デパート千空 初の超高級品だから 売れるまで ちょ～っと時間かかるかもね | Gen: «Es **el primer artículo de lujo** de Grandes Almacenes Senku; tardará en venderse» | Gama «Más de 400» |
| Especial | 00:35:46 a 00:35:56 | カネに糸目つけねえ物欲の権化が １人 いんだろうが / お買い上げ ありがとうございます / 龍水「ハッハー！」 | Senku: «Hay uno que es **la codicia en persona** y no mira el precio». Gen: «**Gracias por su compra**». Ryusui: «¡Ja-ja!» | Humor: el que compra lo más caro |
| 3×05 | 00:04:32 | ゲン「また技術料 100億ドラゴ～とか…」 | Gen: «¿Otra vez **10.000 millones de dragos** por mano de obra?» | Precio exagerado |

### 2.5 Lo que se ve, mirado en vídeo (2.ª pasada)

YouTube pide iniciar sesión desde el servidor. El investigador de vídeo usó
**Internet Archive**: el opening 1 sin créditos en 1080p y los episodios
1×11, 1×19, 1×23 y 1×24 (fansub en español), con `fotogramas.py`. Abrió
cada hoja y la miró. El minuto es **el de ese archivo**: puede moverse uno
o dos minutos frente al de Netflix de las tablas de arriba.

| # | Vídeo y minuto | Qué se ve (mirado) | Para qué |
|---|---|---|---|
| 1 | [1×11, 16:45](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1005) | Suika **sin casco**: pelo claro, ojos muy abiertos, boca abierta, sonrojo de rayitas, junto a un bidón | Cara de sorpresa |
| 2 | [1×11, 16:53](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1013) | **El laboratorio por dentro**: cortinas de tela blanca de puerta, muros de piedra apilada, estantes de madera con tinajas de barro, mesa con paneles verdes de vidrio. Senku de espaldas; Chrome: «Oye, ¿qué pasa, Senku?» (fansub) | **El sitio del concepto A** |
| 3 | [1×19, 20:42](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1242) | Senku en primer plano, **sonrisa ladeada**, fondo de bosque: «¡Smartphones!» | Presentar |
| 4 | [1×19, 21:07](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1267) | **La hoja de ruta del móvil**: nodos redondos 水銀 (mercurio), 金 (oro), プラスチック (plástico, con iconos de bolsa, vaso y pieza de lego), 蜂の巣 (panal), 木炭 y 石炭 (carbón), y un cartel grande **START** | **El cuadro de la lámina 2** |
| 5 | [1×23, 19:49](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1189) | Kohaku (capa con ribete de piel, espada a la espalda) mira **un vaso con piedritas transparentes: la sal de Rochelle**, boca abierta | El material del micro |
| 6 | [1×23, 21:04](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1264) | Senku con **abrigo de piel**, cejas fruncidas, **gotea con un cuentagotas** sobre un vaso de líquido pálido | Explicar, experimentar |
| 7 | [1×24, 2:17](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=137) | **La torre-vigía**: cabaña de madera y paja en lo alto de un árbol enorme, con **una gran bocina de cobre** en la punta; monos alrededor. «¡Nace el móvil!» | Objeto real en sitio real |
| 8 | [1×24, 4:34](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=274) | Ruri en primer plano (pelo rubio, ojos turquesa), asombrada; detrás, gente con ropa de invierno en un recinto de cuerdas y madera. Primera prueba del micro | Reacción |
| 9 | [1×24, 22:10](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=1330) | Senku junto a una hoguera, luz cálida, mirada seria | Cierre nocturno |
| 10 | [OP1, 0:24](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=24) | Senku camina entre **árboles petrificados que brillan en violeta y azul** | El mundo de piedra |

El micrófono y el teléfono **no tienen arte fijo** en la wiki: sólo salen
animados. Para dibujarlos, los fotogramas 5, 7 y 8 de esta tabla ✅.

---
## 3 · Arte oficial y referencias visuales

> [!note] 2.ª pasada: ahora sí se abrieron
> En la primera pasada ninguna imagen se pudo abrir. Ahora el investigador
> de imagen **bajó, midió y miró** las de la wiki (tamaño real por la API
> de Fandom, `prop=imageinfo`). Lo que sigue en ⚠️ es lo que no se pudo
> abrir (dr-stone.jp da 403 y no está en la Wayback Machine).

### 3.1 Key visuals del anime

| Qué | Dónde | Qué se sabe |
|---|---|---|
| Visual del **último tramo** (*Science Future*, 3.ª parte) | [dr-stone.jp, noticia 5824](https://dr-stone.jp/news/5824/) · [Natalie](https://natalie.mu/comic/news/650788) | Publicada el 5 de marzo de 2026. **Senku y Xeno miran la Luna** de noche con el Reino de la Ciencia ✅ (dos fuentes). Se estrenó el 2 de abril de 2026 en Tokyo MX. |
| Teaser de ese tramo | [SPICE](https://spice.eplus.jp/articles/342538) | Visual previa ⚠️ |
| Fichas de personaje del anime (settei) | [WebNewtype](https://webnewtype.com/news/article/190514/) | **Hojas de modelo** de la temporada 1 y comentario de **Yuko Iwasa** (diseño de personajes): Kohaku «divertida de dibujar en acción», Chrome «pone muchas caras» ✅ |
| Personajes en la web oficial | [dr-stone.jp/character](https://dr-stone.jp/character/) | Retratos oficiales ⚠️ (no se abre) |
| Staff | [dr-stone.jp/staffcast](https://dr-stone.jp/staffcast/) · [ficha de TMS](https://www.tms-e.co.jp/alltitles/2010s/762101.html) | Diseño de personajes **Yuko Iwasa** (岩佐裕子), que también dibuja las carátulas de los Blu-ray; color **中尾総子**; diseño de fondos **青木智由紀**; dirección de arte **吉原俊一郎** ✅ (búsqueda en japonés + ficha de TMS) |
| **Key visual de *Stone Wars*** (2.ª pasada) | [imagen, 2324×3277](https://static.wikia.nocookie.net/dr-stone/images/9/9f/Dr._Stone_Stone_Wars_Key_Visual_3.png) | Senku de pie con **capa verde**. El más grande de la wiki. Hoja `arte_01` nº1 ✅ |
| Otra de *Stone Wars* | [imagen, 1830×2529](https://static.wikia.nocookie.net/dr-stone/images/1/1e/Dr._Stone_Stone_Wars_Key_Visual_1.png) | Cartel «闘戦»: **dos manos que se agarran**, una con vendas (Senku y Tsukasa). Hoja `arte_01` nº14 ✅ (visto en la hoja; nombre del archivo en la wiki) |
| Key visual de la temporada 1 | hoja `arte_01` nº38 y nº39, 1449×2048 | **Grupo de cuatro**, dos variantes ✅ vistas |
| Especial *Ryusui* | [imagen, 1420×2000](https://static.wikia.nocookie.net/dr-stone/images/4/4e/Dr._Stone_Ryusui_Key_Visual_1.png) | El más grande de la categoría ✅ |
| *New World* y *Science Future* | *New World* KV 1 (849×1200) · [*Science Future* KV 1, 849×1200](https://static.wikia.nocookie.net/dr-stone/images/5/5c/Dr._Stone_Science_Future_Key_Visual_1.png) | ✅ medidos. La wiki tiene **22 key visuals** en [Category:Key Visuals](https://dr-stone.fandom.com/wiki/Category:Key_Visuals) |
| Cuenta atrás | [X, «8 Days»](https://x.com/animeupdates/status/2036759330528154071) · [X, «tomorrow»](https://x.com/animeupdates/status/2039517302257856758) | Cartones de *Science Future* 3.ª parte (abril 2026) ⚠️ (una cuenta que republica lo oficial) |

### 3.2 Manga, libros y fanbook

- **Manga**: guion de **Riichiro Inagaki**, dibujo de **Boichi**. Shūkan
  Shōnen Jump, 26 tomos (de 2017 a 2022 ⚠️, de memoria), y un tomo 27
  con la historia de después ✅ ([Wikipedia, lista de capítulos](https://en.wikipedia.org/wiki/List_of_Dr._Stone_chapters), [collabo-cafe](https://collabo-cafe.com/events/collabo/dr-stone-character-popular-ranking-vol4-2024/)).
- **Fanbook oficial** «**Dr.STONE 公式ファンブック 科学王国事典**» (4 de
  agosto de 2022): más de 50 fichas de personajes, cronología, **las hojas
  de ruta de cada invento y cómo se fabrica cada uno**, y preguntas y
  respuestas con los autores ✅ ([Shueisha](https://www.shueisha.co.jp/books/items/contents.html?isbn=978-4-08-883248-7), [S-MANGA](https://www.s-manga.net/items/contents.html?isbn=978-4-08-883248-7)).
  **Es la mejor referencia para dibujar el micrófono y el teléfono**, si
  alguien la tiene.
- **Boichi estudió física** y luego tecnología de imagen: por eso sus
  diagramas son exactos y bonitos ✅ ([Fandom: Boichi](https://dr-stone.fandom.com/wiki/Boichi), [CBR sobre su entintado](https://www.cbr.com/dr-stone-artist-boichi-relaxing-inking-process/)).
- Entrevista a los autores sobre cómo hacer legible la ciencia:
  [Nikkei xTrend](https://xtrend.nikkei.com/atcl/contents/18/00316/00035/) ⚠️ (no la pude abrir).
- **Portadas de tomos** (2.ª pasada, vistas en `arte_01`): en inglés (US 8,
  12, 25…) y japonés (4, 5, 17…). **Nunca de pie sin más**: cuerpo entero
  con objeto o en grupo. El US 25: Senku, Chrome y Kohaku corriendo con un
  brazo mecánico detrás ✅.
- **Portadas de Weekly Shōnen Jump** (2017-40, 2018-51, 2019-31, 2020-48,
  2021-02, 2021-15), de 1200×480 a 2000×800, vistas en `settei_01` y
  `vestuario_01` ✅.
- **«Dr. STONE Speak Towards the Future»** (libro), portada 800×1259,
  `settei_01` nº258 ✅.
- **Doble página del capítulo 216** «Z=216 HELLO WORLD», el despegue del
  cohete SENKU7: [imagen, 2190×1600](https://static.wikia.nocookie.net/dr-stone/images/6/69/Chapter_216.png) ✅. Cómo
  está tramada, en §18.2.

### 3.3 Los objetos del canal, tal como salen en la serie

Lo que se dice está en el subtítulo ✅. Lo que se ve, en la 1.ª pasada era
de memoria ⚠️; en la **2.ª pasada** se miró en los fotogramas de §2.5 y en
las imágenes de la wiki.

| Objeto | Cómo es | Estado |
|---|---|---|
| **Micrófono** (1×23) | **Cristales de sal de Rochelle** («キラッキラの石», piedras brillantísimas, 00:19:46) pegados a **un megáfono de plástico**. La sal sale de las **bolitas rosas del corcho del vino** y del alga quemada | ✅ lo dicho. **Visto** (2.ª pasada): la sal es un vaso de **piedritas transparentes** ([1×23, 19:49](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1189)). El megáfono en primer plano sigue sin fotograma ⚠️ |
| **Teléfono / móvil** (1×23-1×24) | «No es *smart*, sólo *phone*». Lleva **tubos de vacío** (Kaseki), **hilo de oro** (Suika y los niños), **plástico** (Chrome), **800 pilas** (Gen) y el micro (Kohaku). Tiene un **interruptor de llamada que se gira** («通話スイッチを回す音», 2×02, 00:21:38) | ✅ piezas. La **bocina de cobre** en la torre-vigía, vista ([1×24, 2:17](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=137)). La caja del aparato en primer plano ⚠️ |
| **Tocadiscos** (1×24) | Motor de la **maquinilla de afeitar** de Byakuya (00:11:29), **engranaje de la máquina de algodón de azúcar** (00:11:47), **aguja de hueso** (00:12:23). El disco es **el fondo de una botella** (00:08:08) | ✅ |
| **Intercomunicador** (3×10) | Un **pendiente**: el aro de cobre es una bobina y el gancho de la oreja lleva sal de Rochelle. Radio de galena: **sin pilas** | ✅ lo dicho |
| **Cámara** (3×02) | **Daguerrotipo**, «la cámara más antigua». Kaseki fabrica varias: «mis camaritas» (3×03, 00:00:36) | ✅ lo dicho |
| **Moneda Drago** (especial) | **Corregido: no son billetes, son monedas acuñadas.** Cuatro: **500, 1.000, 5.000 y 10.000** (ドラゴ). Cada una con **el perfil grabado** de un personaje (la de 500, un anciano de barba larga; la de 10.000, dos cabezas juntas), **orla de perlitas**, trama de puntos en el relieve y el nombre de **una aleación** debajo (フェロクロム ferrocromo, フェロニッケル ferroníquel…): el dinero vale lo que su metal. [Drago_Coins.png, 959×649](https://static.wikia.nocookie.net/dr-stone/images/4/4c/Drago_Coins.png) | ✅ vista entera |
| **Hoja de ruta** | Cajas con cada material unidas por flechas hasta el invento ([Fandom: Roadmap Diagrams](https://dr-stone.fandom.com/wiki/Roadmap_Diagrams), [Tumblr: Cellphone Roadmap](https://www.tumblr.com/omniotaku/189085357014/dr-stone-cellphone-roadmap)). **Vista en la 2.ª pasada**: la del móvil en el anime ([1×19, 21:07](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1267)), nodos redondos con el material y un cartel **START**; y la del manga, [Roadmap_Senku_Spaceship.png, 1455×1063](https://static.wikia.nocookie.net/dr-stone/images/8/89/Roadmap_Senku_Spaceship.png): **árbol de habilidades de videojuego**, iconos en círculos o cajas de esquinas irregulares con borde grueso («Rare Metals», «Superalloys», «Oil», «Engine», «Computer»), **flechas-tubo gruesas rellenas de trama de puntos**, rayos de velocidad detrás de «START!» y «GOAL», niveles «Level 1» → «LV. 99», y el motor dibujado como maquinaria real, con pernos. Mismo estilo en «Moon Rocket Roadmap» (2036×352) y `settei_01` nº52 | ✅ vista entera |
| **Nendoroid de Senku** (nº1262) | Tres caras (normal, seria, riendo con picardía) y **objetos fabricados a mano**: tarro de barro, botella de medicina, algodón de azúcar ([Good Smile](https://www.goodsmile.info/en/product/9106/Nendoroid+Senku+Ishigami.html)) | ✅ (imagen sólo de 250×250 ⚠️) |
| **Tarjetas del videojuego** *Battle Craft* | Cuerpo entero en acción con su elemento, sobre estrellas: Chrome con un rayo azul, Gen con un remolino de agua, **Kaseki envuelto en llamas con un martillo**, Suika saltando. `settei_01` nº259-262. La de Senku: chasquea los dedos sobre un tubo de ensayo, «E=mc²» en la venda ([1000×1000](https://static.wikia.nocookie.net/dr-stone/images/6/66/Battle_Craft_Intro_Card_Senku.png)) | ✅ poses nuevas, oficiales |

### 3.4 Lo que falta ⚠️

- ~~Ninguna captura de la hoja de ruta~~ → vista (1×19, 21:07). ~~El
  billete de Drago~~ → son monedas, vistas.
- **El micrófono y el teléfono en primer plano**: no hay arte fijo en la
  wiki (búsquedas `microphone` y `telephone` en su API, sin imagen de esos
  objetos solos). Hay fotogramas de 720p (§2.5); en 1080p no se pudo.
- **Las portadas de los tomos**: no encontré cuál muestra el teléfono.
- **Carátulas de Blu-ray** en alta: se sabe que las dibuja Yuko Iwasa (dos
  tiendas), pero no se bajó ninguna.
- **dr-stone.jp/character/** y la noticia 5824: 403 y sin copia en la
  Wayback Machine.

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D de la serie (Sketchfab)

**2.ª pasada: licencia comprobada** con la API de Sketchfab
(`api.sketchfab.com/v3/models/<uid>`, campo `license.label`). Los cuatro
de Senku y el casco de Suika son **CC Attribution (CC BY)** y se pueden
descargar ✅. Son personajes con copyright: **sólo para mirar poses y
volúmenes**, no para pegarlos. Si se usara el modelo tal cual, CC BY obliga
a dar crédito al autor.

| Modelo | Autor | Qué trae | Enlace |
|---|---|---|---|
| **Dr. Stone \| Senku 3D Model, Environment & Props** | Jerry Teng | Senku, **el laboratorio**, hacha, poción, **teléfono**, cuchillo y escudo de Kohaku, **bandera del Reino de la Ciencia** | [Sketchfab](https://sketchfab.com/3d-models/dr-stone-senku-3d-model-environment-props-8dc007444003431f80e8ae69b7a0833d) |
| Senku Ishigami DR Stone | fossyl | Senku | [Sketchfab](https://sketchfab.com/3d-models/senku-ishigami-dr-stone-c1979af69a68490482a99d0a43fcf286) |
| Senku DR Stone 3d model | Leo Nyanko (leonardo.sensei2) | Senku (Blender 2.8, 22,7 k triángulos): **el mejor para usar de base en Blender** | [Sketchfab](https://sketchfab.com/3d-models/senku-dr-stone-3d-model-e7436cf85cbd483fa08e9922b69ce5f5) |
| SENKU Dr Stone | HaroldXd | Senku | [Sketchfab](https://sketchfab.com/3d-models/senku-dr-stone-db3599b14a5f4aa2939b8de61e522035) |
| SUIKA MASK DR STONE (2.ª pasada) | Axel.Slaughter | **El casco de sandía de Suika**, CC BY ✅ | [Sketchfab](https://sketchfab.com/3d-models/suika-mask-dr-stone-dd63b40689b146da9858e2f1af04454e) |
| Todos los de la etiqueta | — | — | [#senku](https://sketchfab.com/tags/senku) · [#drstone](https://sketchfab.com/tags/drstone) |

### 4.2 Modelos 3D de objetos para el banco de trabajo

Genéricos, gratis en Sketchfab. **2.ª pasada**: el vidrio de laboratorio
(maxdragon), la radio de los años 40 (ponchoguy) y el tubo de vacío son
**CC BY** ✅ por la API. El megáfono de Console Art Cybernetic es **«Free
Standard»**: no es Creative Commons, se usa pero no se redistribuye el
archivo ⚠️. Los demás de la tabla no se comprobaron uno a uno ⚠️.

| Para qué | Modelo | Enlace |
|---|---|---|
| **Tubo de vacío** | Vacuum tube (lulu the black dog) | [Sketchfab](https://sketchfab.com/3d-models/vacuum-tube-3867ca5c3cd74cb882b22d0eee75567a) |
| **Megáfono** (base para el micro de Senku) | Megaphone (Console Art Cybernetic) · MEGAPHONE (maxielr) · Megaphone (alp555) | [1](https://sketchfab.com/3d-models/megaphone-afc27df368144fe892d8e22c1f4b1e8a) · [2](https://sketchfab.com/3d-models/megaphone-39fb70cab11e4f0f931088e8b287d3f3) · [3](https://sketchfab.com/3d-models/megaphone-d66a9e50afca478fbbf6306162759753) |
| **Radio antigua de válvulas** (para mirar el interior) | Old Radio (Guy in a Poncho, una Admiral 7T10 con sus piezas) | [Sketchfab](https://sketchfab.com/3d-models/old-radio-7724f81ad4e043079b7bf4b16146c087) |
| Radio y micro antiguos | Old Radio and Microphone (Jekichani) | [Sketchfab](https://sketchfab.com/3d-models/old-radio-and-microphone-bd21f2ff43ff45e0aa94b96021d65b7c) |
| **Material de laboratorio** (matraces, vasos) | Chemistry Glassware (maxdragonn) · Chemical Flask (BrimstoneAz) · Conical Flask (Naked Singularity) | [1](https://sketchfab.com/3d-models/chemistry-glassware-b8594f7dc7e8442dbaaae7a11da4a962) · [2](https://sketchfab.com/3d-models/chemical-flask-3f762f5dc19844fba49494f69f3b82c8) · [3](https://sketchfab.com/3d-models/free-conical-flask-laboratory-low-poly-f2991abcaaa44616ad5f72d29a3d47b3) |

**Mejor hacerlo a mano en Blender** (propuesta, la comparten la 1.ª y la
2.ª pasada): el megáfono de Senku es un cono de plástico fenólico marrón,
mate, sin pulir, con vetas de moldeo; los cristales de Rochelle son prismas
transparentes irregulares (en el anime, piedritas en un vaso: §2.5); los
tubos de vacío son de vidrio soplado a mano, con burbujas. Un megáfono
comercial metálico y brillante queda demasiado limpio. La **bocina de
cobre** de la torre (§2.5, fotograma 7) sí es metálica.

### 4.3 Fan art 2D (mirar, nunca pegar)

- **pixiv**: etiqueta [Dr.STONE](https://www.pixiv.net/en/tags/Dr.STONE)
  (más de 11.800 dibujos según el resumen del buscador ⚠️), por ejemplo
  [«文系ゲンくん»](https://www.pixiv.net/en/artworks/131413422) y
  [«ゲン！！»](https://www.pixiv.net/en/artworks/140091266).
  Enciclopedia: [千空](https://dic.pixiv.net/a/%E5%8D%83%E7%A9%BA),
  [クロム](https://dic.pixiv.net/a/%E3%82%AF%E3%83%AD%E3%83%A0(dr.stone)),
  [カセキ](https://dic.pixiv.net/a/%E3%82%AB%E3%82%BB%E3%82%AD(Dr.STONE)).
- **DeviantArt**: [Senku Ishigami, de Jiance](https://www.deviantart.com/jiance/art/Senku-Ishigami-Dr-Stone-812555318)
  y [Kohaku Wallpaper, de dinocozero](https://www.deviantart.com/dinocozero/art/Kohaku-Wallpaper-812210990)
  (las dos responden, 2.ª pasada ✅). Licencia por defecto: todos los
  derechos reservados; sólo para mirar.
- **ArtStation**: [hoja para colorear de Senku, de Kelvin Ellis](https://www.artstation.com/artwork/aoPzx9) (útil para ver su contorno). Da 403 a los robots ⚠️.

### 4.4 Cosplay (2.ª pasada: materiales reales)

[Foto de un cosplay de Senku](https://live.staticflickr.com/65535/51772988428_88df4b0f8b_b.jpg)
(767×1024, Openverse, **CC BY-NC-SA 2.0**, esby.photo, Roseraie de la
Beaujoire, Nantes), mirada ✅:

- Túnica **crema-hueso, no blanca**, con «E=mc²» pintado en el pecho y el
  cuello levantado.
- **Vendas de tela** en los antebrazos y una bolsa de tela atada al
  cinturón.
- **Botas de dos piezas**: bota alta blanca cosida en zigzag, con refuerzo
  de cuero marrón en la puntera y el borde.
- Peluca con el degradado exacto: **raíz crema, puntas verde menta**, y un
  mechón que cae sobre la cara.

Confirma a ojo el color medido de la túnica, `#F5EBD6` (§16).

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios que sirven

| Sitio | Cuándo sale | Luz | Estado |
|---|---|---|---|
| **El laboratorio** (ラボ) de la aldea Ishigami | Lo consiguen en 1×11, 00:16:49: «¡Por fin tenemos laboratorio!». Mecha Senku enseña el mapa del Reino de la Ciencia a las 00:17:21 | Interior de madera y paja, fuego de horno, luz cálida. **Visto** (2.ª pasada, [1×11, 16:53](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1013)): cortinas blancas de puerta, **muros de piedra apilada**, estantes con tinajas, mesa con vidrio verde; luz difusa y neutra en la entrada | ✅ visto; paleta medida en §5.2 |
| **El almacén y la aldea en invierno** | 1×23: hace frío, Senku pone **estufas de cobre** en las casas (00:17:11 «¡qué calentito está dentro!») mientras queman carbón | Nieve fuera, brasas dentro | ✅ lo dicho |
| **El taller de Kaseki** | 1×11 (vidrio), 1×23 (tubos de vacío), 3×03 (cámaras) | Horno, chispas | ⚠️ |
| **Los Grandes Almacenes Senku** | Especial *Ryusui*, 00:33:38 a 00:35:56: puesto de ropa y **desfile** | Día, aire libre | ✅ existe; aspecto ⚠️ |
| **El barco Perseus** (sala de radio y sonar) | *New World*, 3×04 (radar y sonar) | Madera de barco, noche en el mar | ⚠️ |
| **La tumba de Byakuya** (la «lápida» que es una cápsula del tiempo) | 1×24, 00:06:34 a 00:08:22 | Exterior, día | ✅ lo dicho |

### 5.2 Paleta medida (2.ª pasada)

**Medida con `herramientas/estilo.py`** sobre fotogramas reales (enlace y
segundo en cada fila). Sustituye a la propuesta de memoria de la 1.ª
pasada, que queda debajo sólo para lo que no se midió.

| Sitio | Hex medidos | Luz | Fotograma |
|---|---|---|---|
| **Laboratorio** (entrada, piedra y madera) | `#B0B1A2` `#848276` `#9B9988` `#EAE2D3` `#6E695E` `#4B4E47` `#CCCCC1` `#2A2B29`; línea `#5C5548` | Interior, luz difusa, tonos neutros | [1×11, 16:53](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1013) |
| **Bosque petrificado** | `#39313C` `#F4FBFE` `#636C7E` `#BFDDF9` `#9BBCEB` `#7295D0` | Azul violeta frío, contraluz | [OP1, 0:24](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=24) |
| **Campo de girasoles** (recuerdo) | `#F2DC3C` `#C4F0F9` `#D0A822` `#5DA2EA` `#365A3F` `#807D22` | Sol de mediodía, rayos marcados | [OP1, 1:12](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=72) |
| **Torre-vigía de la bocina** | `#393934` `#595D5B` `#A3CAEB` `#878B8C` `#D0E8F2` `#73A3E5` | Día claro, bosque y cielo | [1×24, 2:17](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=137) |
| **Interior en invierno** (pieles, abrigos) | `#D1B9A5` `#998773` `#5E5548` `#D8D3C5` `#A8A28F` | Cálido, sombra mixta | [1×23, 21:04](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1264) |
| **Ending nocturno** (luna, estrellas) | `#3E559A` `#352C96` `#28346F` `#E0E0D5` `#7E8DBE` | Noche, **acuarela** | [1×24, 22:40](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=1360) |
| **Cuartel de Ryusui** (arenisca, arcos) | `#E7DECF` `#847363` `#634D3F` `#A0988A` `#BEBEB8` | Día mediterráneo | [Tráiler *Ryusui*, 0:09](https://www.dailymotion.com/video/x8bnxd8?t=9) |
| **El barco** (velas) | `#2B3E63` `#D9DAD0` `#6E6D6A` `#9D9E98` `#3779BA` | Cielo azul despejado | [Tráiler *Ryusui*, 0:12](https://www.dailymotion.com/video/x8bnxd8?t=12) |
| **Cueva de roca** (Senku con la túnica) | `#71655E` piedra media · `#BEB8A6` piedra iluminada | Día difuso desde arriba, sin sombras duras | [`Senku's fearlessness.png`](https://static.wikia.nocookie.net/dr-stone/images/1/12/Senku%27s_fearlessness.png), 1920×1080 |

Lo que se lee de los números: el laboratorio es **gris piedra y neutro**,
no marrón cálido; el calor lo pone el fuego, no la madera. El exterior de
la aldea nevada (donde se hace el micro) no tiene paleta propia medida ⚠️.

**Propuesta de la 1.ª pasada** (de memoria ⚠️; sólo para lo que no se
midió arriba. El pelo y los ojos de Senku están **corregidos** en §16):

| Uso | Hex aprox. | De dónde |
|---|---|---|
| Madera del laboratorio | `#7A5534` | tablones y postes |
| Paja y cuerda | `#C9A86A` | tejados, cuerdas |
| Piedra del mundo de piedra | `#A8A59B` | estatuas, grietas |
| Verde bosque | `#4E7A3A` | fondo exterior |
| ~~Verde del pelo de Senku~~ | ~~`#7DBF4A`~~ → medido `#5D906A` / `#2E5538` | pelo (§16) |
| ~~Rojo de los ojos~~ | ~~`#C8322D`~~ → medido `#59050F` | ojos (§16) |
| Brasa del horno | `#F2A541` | luz cálida |
| Cobre del hilo y la estufa | `#B87333` | cables, bobinas |
| Vidrio soplado | `#BFD8D2` con 40 % de opacidad | tubos y matraces |
| Noche de invierno | `#1E2A44` | fuera, por la ventana |

### 5.3 Texturas reales (CC0, Poly Haven y ambientCG)

**2.ª pasada**: las tres de Poly Haven responden (HTTP 200) y son CC0 por
norma del sitio ✅. Las de ambientCG, comprobadas por su API ✅.

| Para qué | Textura | Licencia |
|---|---|---|
| Banco de trabajo | [Rough Wood](https://polyhaven.com/a/rough_wood) (madera agrietada y gastada, 8K) | CC0 |
| Suelo y paredes del laboratorio | [Wood Planks](https://polyhaven.com/a/wood_planks) · [Worn Planks](https://polyhaven.com/a/worn_planks) | CC0 |
| Postes con corteza | [Poly Haven, cortezas](https://polyhaven.com/textures/wood/bark/natural) | CC0 |
| **Piedra** de las estatuas y muros del laboratorio (2.ª pasada) | [Rock Cliff](https://polyhaven.com/a/rock_cliff_large_02) (roca agrietada, 8K) | CC0 ✅ |
| **Cuerda** de la aldea (cinturones, collares, recintos) | [Rope001](https://ambientcg.com/view?id=Rope001) · [Rope002](https://ambientcg.com/view?id=Rope002) | CC0 ✅ |
| **Papel** (grano de página impresa) | [Paper001](https://ambientcg.com/view?id=Paper001) (y 003, 005, 006) | CC0 ✅ |

La **tela de cáñamo** de la ropa sigue sin textura concreta ⚠️ (se buscó
«linen» en ambientCG; no quedó ninguna elegida).

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

- **El logo «Dr.STONE»** es **rotulado propio**: letras de piedra con
  grietas y bordes tallados. **No es una fuente comercial** ✅
  ([madegooddesigns](https://madegooddesigns.com/dr-stone-font/),
  [fontinlogo](https://fontinlogo.com/famous-fonts/dr-stone-font); en el
  foro de dafont lo han preguntado dos veces sin respuesta oficial:
  [1](https://www.dafont.com/forum/read/386992/dr-stone-font),
  [2](https://www.dafont.com/forum/read/409234/dr-stone-font-name-please)).
  Proponen imitarlo con **Anton** o **Bungee** más una textura de piedra,
  o con **Ewert**.
- **Los títulos de los episodios** están casi todos **en inglés y en
  mayúsculas**: «STONE WORLD», «CLEAR WORLD», «STONE WARS», «HOT LINE»,
  «SCIENCE IS ELEGANT», «WHOLE NEW WORLD» ✅ (los nombres de los archivos
  de Netflix). **El rótulo en pantalla, visto y medido** (2.ª pasada) en
  el [cartel del episodio 1](https://static.wikia.nocookie.net/dr-stone/images/b/b8/Episode_1_Title.png/revision/latest?cb=20190705175621)
  (1920×1080, con `estilo.py`) ✅:
  - El logo **«Dr.STONE»** y «ドクターストーン» van en **piedra fundida
    naranja y roja**: `#F29C0F` y `#E74010`, con **grietas** gris casi
    negro `#272523` que parten cada letra como una placa de roca, sobre
    **fondo negro puro**.
  - El número y el título («01.STONE WORLD») usan **la misma letra en
    piedra gris**: `#A49284` y `#C6C2BE`, sin naranja. Logo naranja,
    título gris: la 1.ª pasada no lo distinguía.
  - Dos **líneas horizontales con brillo naranja**, como un destello de
    lava, a los lados del subtítulo japonés.
- **Otra pista para el logo** (2.ª pasada): en un hilo de
  [befonts](https://befonts.com/forum/time-to-lose-our-ship) dos personas
  proponen **Norwester** (sans gruesa) ⚠️ (comunidad, no oficial; gratis
  para uso personal, **comprobar la licencia comercial**; sus tildes no se
  comprobaron con fontTools ⚠️).
- **Letras del manga**: la imprenta estándar de Jump en los globos; las
  explicaciones científicas llevan **diagramas dibujados por Boichi** ✅
  ([análisis](https://smart.columbus.gov/columbus-news/unveiling-the-genius-boichis-dr-stone-panels-explained-1764798310)).

### 6.2 Letras libres comprobadas por mí

Bajé cada archivo de [google/fonts](https://github.com/google/fonts) y
miré con fontTools si trae **á é í ó ú ñ Á É Í Ó Ú Ñ ¿ ¡ ü $**. Todas
**sí** ✅ (Ewert no trae «€», que aquí no hace falta).

| Letra | Para qué | Licencia | Japonés |
|---|---|---|---|
| **Anton** | Título «Hardware» con textura de piedra encima | OFL | no |
| **Rubik Dirt** | Título ya «sucio», como piedra rota | OFL | no |
| **Bungee** | Rótulos de las etiquetas, gruesos y cuadrados | OFL | no |
| **Kalam** (Bold) | **Notas a mano de Senku** en la hoja de ruta | OFL | no |
| **Caveat** | Alternativa más suelta para las notas | OFL | no |
| **Patrick Hand** | Texto largo a mano, muy legible en el móvil | OFL | no |
| **Cabin Sketch** | Letras de tiza o carboncillo sobre madera | OFL | no |
| **Oswald** | **Precios** («Menos de 50 USD») en etiquetas estrechas | OFL | no |
| **Bangers** | Grito o golpe de humor («¡Qué malote!») | OFL | no |
| **Yusei Magic** | **Kanji a mano** («唆るぜ これは!») | OFL | **sí** |
| **Klee One** | Kanji a lápiz, más fino | OFL | **sí** |
| **Dela Gothic One** | Onomatopeya japonesa gorda | OFL | **sí** |
| Ewert | Imitación del logo (opción de madegooddesigns) | OFL | no |

Mi elección ⚠️: **Rubik Dirt** para el nombre del canal, **Kalam** para
todo lo que «escribe» Senku, **Oswald** para las cifras y **Yusei Magic**
si va algún kanji.

**2.ª pasada**: las 13 siguen en Google Fonts con licencia OFL ✅
(comprobado en [fonts.google.com](https://fonts.google.com/) el
24-sep-2026). No hizo falta repetir el análisis de glifos.

### 6.3 Una letra para cada uso (2.ª pasada)

Todas de la tabla de arriba: todas traen á é í ó ú ñ ¿ ¡ (fontTools).

| Uso | Qué hace la serie | Letra libre | Cómo |
|---|---|---|---|
| **Logo o título** | Rotulado de piedra agrietada, naranja lava | **Rubik Dirt** o **Anton** | Relleno `#F29C0F`→`#E74010`, grietas `#272523`, bisel alto, fondo oscuro |
| **Subtítulo del título** | Misma letra en piedra gris | **Anton** | `#A49284`/`#C6C2BE`, sin naranja |
| **Globo normal** | Imprenta estándar de Jump | **Patrick Hand** | Negro, mayúsculas y minúsculas |
| **Grito** | Letras grandes y torcidas | **Bangers** | Contorno grueso, algo inclinado |
| **Pensamiento o nota a mano** | Senku escribe fórmulas y la hoja de ruta | **Kalam** Bold (o Caveat) | Tinta oscura sobre papel o madera |
| **Onomatopeya** | Kana dibujados por Boichi | **Dela Gothic One** (japonés) o Bangers | Con rayas de velocidad detrás (§18.2) |
| **Cartel del mundo** | Tiza, carbón, madera tallada | **Cabin Sketch** | Sobre tabla de madera |
| **Interfaz de juego** | *Battle Craft*: texto **blanco con borde oscuro** (§7.4) | **Oswald** o **Bungee** ⚠️ (la letra del juego no está identificada) | Blanco + trazo oscuro |
| **Precios y cifras** | «100 dragos», «10.000 millones de puntos» | **Oswald** | Estrecha, se lee a tamaño pequeño |
| **Subtítulos o créditos** | Los títulos de episodio en inglés y mayúsculas | **Oswald** ⚠️ (propuesta; no se identificó la letra de los créditos) | Mayúsculas, espaciado amplio |

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que la serie pone en pantalla

Dr. Stone **no usa un globo propio**. Pone texto en pantalla de estas
maneras:

| Soporte | Dónde se ve | Estado |
|---|---|---|
| **La hoja de ruta** (ロードマップ) | La primera, hacia la medicina: «これは万能薬へ向かう科学のロードマップだ» (1×08, 00:03:26; el subtítulo va arriba, sobre el dibujo). La del móvil: 1×19, 00:21:25 y 1×21, 00:13:00. La del cohete: 4×24, 00:21:32. **Vista en la 2.ª pasada** ([1×19, 21:07](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1267) y la del cohete del manga, §3.3): **árbol de habilidades de videojuego**, nodos redondos o cajas de borde grueso, flechas-tubo con trama, «START!» y «GOAL» con rayos detrás | ✅ vista |
| **El «¡…, listo!»** (クリア) en cadena | 1×23, 00:21:04 a 00:21:16 y 1×24, 00:00:03 a 00:00:10: cada uno anuncia su pieza terminada | ✅ |
| **Mecha Senku** (メカ千空), el robot que explica | 1×04, 00:05:08: «¡Buenas! Me llamo Mecha Senku. Todas estas recetas son de verdad. **No lo intentes en casa**». Vuelve en 1×11, 1×15, 1×22, 2×02, 2×05, 3×09, 3×18, 4×17, 4×18, 4×25 y 4×28 (23 líneas en total) | ✅ |
| **El test de Gen** (A, B, C y «¡Correcto!») | 2×01, 00:15:25 a 00:15:34 | ✅ |
| **La voz por el teléfono** | Ruido de altavoz («スピーカーのノイズ», 1×24, 00:13:56), el disco de Byakuya, la voz de Lillian | ✅ |
| **El «¡Esto me emociona!»** (唆るぜ これは) al final | Cierra muchos episodios: 1×01 00:22:11, 1×23 00:22:12, 1×24 00:22:11… (14 veces en toda la serie) | ✅ |

**Mecha Senku**, cómo es: un **Senku robot** gris claro con detalles
**amarillos, rojos y azul marino**; las marcas de la frente son **juntas
de placas de metal** en vez de grietas; **sólo se le ven la cabeza, los
hombros y los brazos**. En el manga contesta las preguntas de los
lectores en los tomos ✅ ([Fandom, personajes menores](https://dr-stone.fandom.com/wiki/List_of_Minor_Characters),
[OTAQUEST: mascota en AnimeJapan](https://www.otaquest.com/animejapan-dr-stone-mecha-senku-mascot/)).

### 7.2 Cómo habla cada uno (por el subtítulo)

| Quién | Cómo habla | Ejemplo (minuto) |
|---|---|---|
| **Senku** | Rudo y rápido, habla «de chico de barrio» (テメー, ブチ〜, アホほど). **Exagera con 100億** (diez mil millones): «100億％», «100億倍». Se ríe **«ククク»** (343 veces en la serie). Explica con recetas cortas: «足し算引き算». **2.ª pasada**, según la trivia de la wiki: «**Not one millimeter**» (ni un milímetro) cuando algo es imposible, y «This is exhilarating» / «Get excited» ante un avance ✅ ([Fandom, Senku](https://dr-stone.fandom.com/wiki/Senku_Ishigami#Trivia)) | 1×23, 00:15:40: «La química es sumar y restar» |
| **Chrome** | Chico de aldea, entusiasta. Dice **«ヤベえ»** (¡qué fuerte!, ¡qué pasada!) sin parar (la palabra sale 185 veces en la serie, en boca de varios). Grita **«しゃあ!»** al ganar | 1×24, 00:04:34: «¿Lo ves, Ruri? ¡La ciencia es la bomba!» |
| **Gen** | Habla con **jerga al revés de la tele japonesa** (倒語): **ジーマー** (maji, «en serio»), **バイヤー** (yabai, «qué fuerte»), **ドイヒー** (hidoi, «qué crueldad»), **ゴイスー** (sugoi, «increíble»), **リームー** (muri, «imposible»). Añade «〜ちゃん» a todos («千空ちゃん») ✅ ([Yahoo! Chiebukuro](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q10319251340), [pixiv 業界用語](https://dic.pixiv.net/a/%E6%A5%AD%E7%95%8C%E7%94%A8%E8%AA%9E)). **El mecanismo** (2.ª pasada): parte la palabra en sílabas y **pone la primera al final** («yabe» → «beya», «muri» → «rimu»); en inglés se tradujo con *Pig Latin* («crazy» → «azy-cray») ✅ ([Fandom, Gen](https://dr-stone.fandom.com/wiki/Gen_Asagiri#Trivia)) | 1×23, 00:19:15: «ドイヒ～» (¡qué crueldad!) al saber que son 800 pilas |
| **Kaseki** | Viejo artesano: «**オホー!**», «〜じゃい», «〜ぞい», «ワシ» (yo). Sube la voz cuando se emociona | 1×11, 00:15:53: «¡Oh-ho! ¡Que llevo cincuenta años de artesano!» |
| **Suika** | Niña: habla de sí misma en tercera persona («スイカは…») y termina en **«〜なんだよ»** | 1×08, 00:09:17: «Suika quiere ayudar» |
| **Kohaku** | Guerrera, frases firmes, «〜のだ», «めっぽう» | 1×23, 00:19:43: «¿Y cuál es el tal micrófono?» |
| **Ukyo** | Suave, amable. Fue **operador de sonar**: su oído lo oye todo | 3×04, 00:07:57: «Yo, que soy sonarista, debí darme cuenta el primero» |
| **Ryusui** | «**欲しい!**» (¡lo quiero!), **chasquea los dedos** (131 chasquidos en los subtítulos) y se ríe «**ハッハー!**» | 3×02, 00:03:06: «El "lo quiero": nadie resiste esa pasión» |

### 7.3 Cómo se traduce a una lámina fija

1. **Lo que dice el personaje va escrito a mano** en un trozo de papel o
   de corteza **clavado a la hoja de ruta**, con Kalam. No en un globo.
2. **Cada texto del canal es una caja de la hoja de ruta**, unida con
   flechas a la siguiente, como la del móvil (1×19). La última caja es
   la meta.
3. **Lo ya explicado lleva «¡Listo!»** (el クリア de 1×23) como un sello
   o una marca de tiza.
4. **Los consejos pequeños los dice Mecha Senku** desde una esquina,
   recortado a la altura del pecho (así sale en la serie).
5. **Las etiquetas de la lámina 2** van como **el test de Gen**: «¿Cuánto
   cuesta? A, B, C, D».
6. La emoción no es un globo con pinchos: es la **sonrisa de Senku con
   los dientes** y el «ククク» pequeño al lado ⚠️ (gesto de memoria).

### 7.4 En los videojuegos de la franquicia

**2.ª pasada: la caja de diálogo existe y se vio** en las capturas de la
ficha de *Dr.STONE Battle Craft* en [Google Play](https://play.google.com/store/apps/details?id=com.poppingames.dsbc&hl=en_US)
([captura del diálogo, 512×236](https://play-lh.googleusercontent.com/PkUHa17AsrSFd-aAR4u6vks7a8RB2IThAY1LkudkxC5iGyp4qyUuVjRGBnnLIvMqfbuYxHuG)).
Medida con `estilo.py` ✅:

- Un **cuadro con las esquinas cortadas en bisel** (octogonal), **nunca
  redondo**.
- **Borde fino cian claro** `#7EB6DF` / `#C7DCEC`.
- **Relleno azul verdoso oscuro semitransparente** `#21403D` / `#2F5D5D`,
  para leer sobre el fondo del juego.
- **El nombre** («Senku») va en **una etiqueta más pequeña arriba a la
  izquierda**, unida al cuadro por una línea diagonal con un circulito
  como un remache.
- **Texto blanco con borde oscuro**, sin rayas ni comillas.
- Abajo a la derecha, un icono para avanzar.
- En la imagen se lee el crédito «©米スタジオ・Boichi／集英社・Dr.STONE製作委員会
  ©Poppin Games Japan Co., Ltd.».

Es el mismo lenguaje que el test de Gen y el «¡…, listo!»: **cajas de
esquinas cortadas**. Sirve de molde para las **etiquetas de precio** de
la lámina 2. Más del juego en §13.

### 7.5 Qué NO hacer con el texto

- Una **burbuja blanca redonda** flotando.
- Letra de ordenador limpia y fría para lo que escribe Senku: en la serie
  **todo está hecho a mano**.
- Escribir **«10 millones por ciento»**: es «**10 mil millones**». El
  actor latino lo grabó mal una vez y hubo que regrabar (§10).
- Inventarle a Gen una jerga al revés en español: **en el doblaje latino
  habla normal**, su 倒語 no se adaptó (2.ª pasada: «Datos de interés» de
  Doblaje Wiki) ⚠️ una fuente.
- Rayas «—», «·» o paréntesis en los textos (regla del dueño).

---
## 8 · Los personajes

Lo que está en el subtítulo va con su minuto ✅. El aspecto físico y los
gestos que no salen en el texto eran **de memoria** ⚠️ en la 1.ª pasada.
**2.ª pasada**: cada personaje lleva debajo lo nuevo (trivia de la wiki,
colores medidos, voces medidas con `voz.py`). Gustos, cumpleaños y alturas
en §18.3; caras vistas en vídeo en §15.

### Senku Ishigami (石神千空) — el protagonista, 2.º en votos (2021 y 2023)

- **Quién es**: un chico de instituto, del club de ciencias, que despierta
  de la piedra miles de años después. Durante la petrificación **contó
  los segundos**: «1164億2706万5530秒» (1×01, 00:11:19) ✅. Nació el
  **4 de enero** («el uno y el cuatro: *ishi*, piedra», 1×24, 00:06:20) ✅.
  Su padre, **Byakuya**, era astronauta (1×24, 00:14:09) ✅.
- **Qué quiere**: **revivir a toda la humanidad con la ciencia**, paso a
  paso, desde cero.
- **Carácter**: frío por fuera, **generoso por dentro, pero no lo admite**.
  En 1×23 pone estufas en las casas y dice: «Sólo queremos la ceniza del
  carbón. Si queréis calentaros, allá vosotros» (00:17:25) ✅. Con su
  padre: «¿Eres de los que no quieren sentimentalismos, eh?». «ククク, me
  conoces» (1×24, 00:15:07 y 00:15:13) ✅.
- **Cómo explica**: reduce todo a una receta corta y segura: «La química
  es sumar y restar» (1×23, 00:15:40); «El disco es facilísimo» (1×24,
  00:09:24) ✅. Nunca dice «creo»: dice «**al diez mil millones por
  ciento**».
- **Cómo se ríe**: «ククク», con los ojos entrecerrados y media sonrisa ⚠️.
- **Cómo se emociona**: «**唆るぜ これは!**» (¡esto me emociona!) al final
  de cada reto ✅.
- **Cómo regaña**: seco, con apodos: «雑頭» (cabeza hueca) a Taiju
  (3×04, 00:18:56), «脳筋» (cerebro de músculo) a Magma (1×24, 00:07:27) ✅.
- **Gestos** ⚠️: se **hurga la oreja con el meñique** cuando algo le
  aburre; brazos cruzados; señala con el índice; sostiene el invento en
  alto.
- **Con quién**: Chrome (su compañero de ciencia), Gen (su socio en los
  engaños), Kaseki (sus manos), Suika (su ayudante), Kohaku (su primera
  aliada), Taiju y Yuzuriha (sus amigos de antes).
- **Voz**: japonés **Yusuke Kobayashi** ✅ ([GetNews](https://getnews.jp/archives/3726522));
  latino **Alejandro Orozco** ✅ (§10).
- **2.ª pasada**:
  - **Aspecto medido**: túnica **crema `#F5EBD6`** (no blanca), pelo de
    raíz **`#D0CEBF`** y puntas verde salvia **`#5D906A`** (sombra
    `#2E5538`), ojos **`#59050F`** rojo sangre oscuro, piel `#D0B6A1` ✅
    (§16).
  - Muletillas de la wiki: «**ni un milímetro**» para lo imposible; «esto
    es emocionante» ante un avance ✅ ([Fandom](https://dr-stone.fandom.com/wiki/Senku_Ishigami#Trivia)).
  - Chiste recurrente: **se casó con Ruri y se divorció casi al momento**;
    lo usa para cortar coqueteos ✅. Explica su sequedad con el romance
    sin ser frío de verdad.
  - Es **alérgico a la laca urushi**: se le hincha la cara ⚠️ (una fuente,
    la wiki). Sirve para una cara de incomodidad distinta.
  - **Boichi**: «Esos bolsillos representan lo que Senku está pensando»;
    tiene más bolsillos cuando está en peligro ✅ ([SLJ, AnimeNYC 2019](https://goodcomicsforkids.slj.com/2019/12/20/animenyc-a-peek-behind-the-scenes-of-dr-stone/)).
    En la lámina, **herramientas visibles encima**, nunca las manos vacías.
  - Voz del actor medida (carrete general, no Senku en pantalla):
    registro medio, **174 Hz**, muy expresivo (26,3 semitonos), velocidad
    normal (2,51 palabras/s) ⚠️ como retrato del personaje.

### Gen Asagiri (あさぎりゲン) — el más querido, 1.º en votos (2021 y 2023)

- **Quién es**: **mentalista y mago de la tele** antes de la piedra.
  Tsukasa lo manda como espía, y se cambia de bando **por una botella de
  cola**: «Una alianza atada con una cola: la más endeble del mundo»
  (Senku, 1×10, 00:21:38). Gen: «Qué mal negocio, por una cola» (00:21:45) ✅.
- **Qué hace mejor**: **leer a la gente, mentir bien e imitar voces**.
  Imita a Tsukasa (1×20, 00:01:04) y a la cantante Lillian (2×01,
  00:15:56; 2×08, 00:17:21) ✅.
- **Carácter**: se hace el vago y el cobarde, se queja de todo («ドイヒ～»)
  pero **cumple**: fabrica las 800 pilas cantando (1×23, 00:18:43) ✅.
  Kaseki le ha cogido cariño y lo explota (1×23, 00:15:00 a 00:15:14) ✅.
- **Cómo habla**: jerga al revés de la tele japonesa (ジーマー, バイヤー,
  ドイヒー, ゴイスー, リームー), «〜ちゃん» para todos, **tests de tres
  opciones** con «¡Correcto! Diez mil millones de puntos» (2×01, 00:15:34) ✅.
- **Cómo vende**: presenta el desfile de los Grandes Almacenes Senku
  **como un locutor de moda** (especial, 00:34:29) y dice «Gracias por su
  compra» (00:35:51) ✅. **Es el vendedor perfecto para #hardware.**
- **Aspecto** ⚠️: pelo partido en dos colores, negro y blanco; ropa
  larga oscura, de mago; manos que siempre hacen algo (cartas, gestos).
- **Voz**: latino **Brandon Santini** ✅ (§10); desde el ep. 76, **Iván
  García**.
- **2.ª pasada**:
  - **Pelo**: según la wiki, «bicolor, mitad izquierda corta y negra,
    mitad derecha blanca, con mechones más largos junto a la cara» ✅. En
    su retrato (`vestuario_01` nº228) se ve así **desde el que mira**:
    negro a la izquierda, blanco a la derecha.
  - **Cicatriz de piedra**: una marca quebrada que baja desde el ojo
    izquierdo con una cuña como una boca en el pómulo. **Cambia con lo que
    hace**: parece una flor cuando imita la voz de una mujer y se vuelve
    más quebrada cuando trama algo ✅ (texto de la wiki, `datos-imagen.md`).
    Ojos oscuros con ojeras, rasgados hacia arriba; cejas cortas.
  - **Ropa**: la parte de imagen sólo tenía dos imágenes con luz de
    atardecer o violeta (abrigo largo, cuello alto, silueta oscura) y **no
    pudo medir el color** ⚠️. En las hojas, de día (`arte_01` nº5 y nº17,
    `settei_01` nº271 y nº278, `vestuario_01` nº228), **se ve una túnica
    lila o violeta claro con ribete de piel blanca** ⚠️ (a ojo en
    miniaturas, sin medir).
  - **Sólo bebe cola**, nunca alcohol: «strictly a cola man» ✅
    ([Fandom](https://dr-stone.fandom.com/wiki/Gen_Asagiri#Trivia)).
  - Lleva siempre **una baraja de cartas hechas a mano** con **tres
    comodines** con frases escritas ✅. Su flor para los trucos es la
    **hierba mora negra**, que en el lenguaje de las flores significa
    **«mentiroso»** ✅.
  - **Esconde las manos y encorva la espalda**, y parece más bajo de lo
    que es ⚠️ (una fuente, un post citado en la wiki).
  - **Voz latina medida** con `voz.py` en la [muestra de Doblaje Wiki](https://static.wikia.nocookie.net/doblaje/images/6/6b/GenAsagiriBrandonSantini.mp3)
    (Gen a Magma): «Espera un momentito, por favor. ¿A dónde vas?… No es
    tan sencillo como crees, Magma». **Muy aguda (398 Hz), muy expresiva
    (22,9 semitonos), rápida (3,1 palabras/s)** ✅: la voz que vende rápido.

### Chrome (クロム) — el aprendiz, 7.º en votos (2021)

- **Quién es**: el «hechicero» de la aldea Ishigami. Desde niño **colecciona
  minerales** y los mezcla y quema; a lo que no entiende lo llama «magia» ✅
  ([Fandom](https://dr-stone.fandom.com/wiki/Chrome), [CBR](https://www.cbr.com/dr-stone-chrome-character-arc/)).
  Con Senku pasa a ser «**usuario de la ciencia**»: «Ya no me llamo
  hechicero» (1×10, 00:17:06 a 00:17:15) ✅.
- **Carácter**: curioso, impaciente, competitivo y noble. **Explorador**:
  «¡Vamos, equipo de excavación científica!» (1×21, 00:12:41); «Explorando
  te gano por cientos de miles de millones» (00:12:47) ✅.
- **Qué le importa**: **Ruri**, la sacerdotisa. En la primera llamada,
  todos esperan que se declare… y dice «¡La ciencia es la bomba!» (1×24,
  00:04:34) ✅.
- **Cómo habla**: «ヤベえ!» → en latino **«¡Qué malote!»** ✅ (§10).
  Grita «しゃあ!» cuando algo sale bien (1×23, 00:21:34) ✅.
- **Aspecto** ⚠️: pelo oscuro y de punta recogido, ropa de aldea de
  cáñamo, bolsa de piedras.
- **Voz**: latino **José Luis Piedra** ✅.
- **2.ª pasada**:
  - **Camisa azul petróleo `#245E6B`**, medida en [`Chrome's determination.png`](https://static.wikia.nocookie.net/dr-stone/images/4/41/Chrome%27s_determination.png)
    (1920×1080); la wiki dice «camisa azul oscuro de manga corta» ✅. Lleva
    **el logo del Reino de la Ciencia en las mangas** (texto de la wiki; no
    hay primer plano limpio ⚠️).
  - Su nombre es **el cromo** (Cr, número 24) y nació **el 4 de febrero**,
    2/4 = 24: chiste del autor ✅.
  - Gag: **Kohaku le pega cuando la llama «gorila»**, y sólo a él (a veces
    a Ginro); a Senku, que dice lo mismo, no ✅.

### Kaseki (カセキ) — el artesano

- **Quién es**: el artesano de la aldea: «Llevo cincuenta años de
  artesano» (1×11, 00:15:53) ✅. **Sopla el vidrio** (1×11), hace **los
  tubos de vacío** del teléfono (1×23, 00:21:13) y **las cámaras**
  (3×03, 00:00:36) ✅.
- **Su gesto famoso**: parece un viejo frágil, pero **cuando se emociona
  se le hinchan los músculos y le revienta la camisa**; se queda con la
  parte de abajo y la cuerda de la aldea al cuello ✅
  ([Fandom](https://dr-stone.fandom.com/wiki/Kaseki), [ciatr](https://ciatr.jp/topics/337399)).
  En 1×11: «¡Déjame a mí!» y Senku: «¿En serio, esos músculos?»
  (00:15:10 a 00:15:13) ✅.
- **Cómo habla**: «**オホー!**» (¡oh-ho!, 59 veces en la serie), «ワシ»,
  «〜じゃい», «〜ぞい» ✅.
- **Qué le importa**: **hacer cosas nunca vistas con las manos**. Se
  pica si le retan (Gen lo provoca, 1×23, 00:15:02) ✅.
- **Voz**: latino **Óscar Rangel** ✅.
- **2.ª pasada**:
  - **Túnica con capucha marrón cuero `#5B4A34`**, sombra `#362C1D`,
    medida en [`Kaseki Anime Profile.png`](https://static.wikia.nocookie.net/dr-stone/images/7/71/Kaseki_Anime_Profile.png)
    (621×946); la wiki: «como el hábito de un monje» ✅.
  - **Se le rompe la ropa al emocionarse**, incluso la difícil de hacer que
    le cosió Yuzuriha ✅. Si se le pone ropa nueva, que quede **rota o a
    punto de romperse**.
  - **Le duele que desguacen sus vehículos** (el primer coche, el
    laboratorio móvil, el barco Perseus); se consuela si sabe que se
    reconstruirán en algo mejor ✅ ([Fandom](https://dr-stone.fandom.com/wiki/Kaseki#Trivia)).
    Tristeza propia: no llora, **se queda en silencio mirando la máquina**.
  - En *Battle Craft* sale **envuelto en llamas con un martillo**
    (`settei_01` nº261) ✅.

### Suika (スイカ) — la pequeña exploradora, 12.ª en votos (2021)

- **Quién es**: niña de la aldea **miope** («enfermedad de verlo todo
  borroso»). Lleva **un casco de sandía** para esconderse y sentirse útil ✅
  ([Fandom](https://dr-stone.fandom.com/wiki/Suika)). Senku y Kaseki le dan
  **gafas** («les debo lo de las gafas», 4×14, 00:15:12) ✅.
- **Qué quiere**: **ayudar**: «Suika quiere ayudar. Como siempre llevo
  esto, no le sirvo a nadie» (1×08, 00:09:17 a 00:09:20) ✅. Se nombra
  «**¡Detective Suika!**» (00:15:05) ✅.
- **En el teléfono**: trenza **el hilo de oro** con los niños (1×23,
  00:21:06) y aprieta **el botón de llamada**: «¡Encendido!» (1×24,
  00:04:21) ✅.
- **Su gran momento** (*Science Future*): **sola durante años**, fabrica el
  líquido de revivir desde cero y despierta a Senku ✅
  ([Namu Wiki](https://namu.wiki/w/%EB%8B%A5%ED%84%B0%20%EC%8A%A4%ED%86%A4)).
  Para no sentirse sola **imita las voces de todos** (4×23, 00:03:10 a
  00:06:21) ✅. Luego le da a Senku **una capa roja** ⚠️ (una fuente).
- **Cómo habla**: en tercera persona y con «〜なんだよ»: «スイカは いっぱい
  採るんだよ 黒い砂!» (Suika va a sacar un montón de arena negra, 1×08,
  00:10:19) ✅.
- **Voz**: latino **Valeria Mejía** ✅.
- **2.ª pasada**:
  - **Colores medidos** en las hojas de modelo oficiales (settei, 1200×848,
    [con casco](https://static.wikia.nocookie.net/dr-stone/images/c/c7/Suika_with_Melon_TV_Animation_Design_Sheet.png) y
    [sin casco](https://static.wikia.nocookie.net/dr-stone/images/5/58/Suika_without_Melon_TV_Animation_Design_Sheet.png)):
    casco **`#B4C856`** con rayas **`#70872B`**, poncho **`#373C42`**
    (azul gris casi negro), pelo **`#F3DD89`** ✅.
  - **El casco lo hizo Kaseki**, no ella ✅. **Dejó de hablar en tercera
    persona al crecer** ✅ ([Fandom](https://dr-stone.fandom.com/wiki/Suika#Trivia)):
    útil si se dibuja a Suika mayor.
  - Sin casco (visto, [1×11, 16:45](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1005)):
    ojos muy abiertos, boca abierta, sonrojo de rayitas.

### Los secundarios que conviene tener a mano

| Personaje | Por qué sirve aquí | Voz latina |
|---|---|---|
| **Ukyo Saionji** (西園寺羽京), 4.º en votos (2021) | Fue **sonarista**; su oído lo oye todo (3×04, 00:07:57). **El de los auriculares** | Eduardo Garza ✅ |
| **Minami Hokutozai** (北東西南) | Periodista. Llora con **su cámara** nueva (3×02, 00:18:12). **La de la cámara** | ⚠️ no la busqué |
| **Ryusui Nanami** (七海龍水), 3.º en votos (2021) | Rico, lo quiere todo, emite **el Drago**, **compra lo más caro** (especial, 00:35:51). **El de «Más de 400»**. Cita de la wiki: «**Mi instinto de marinero nunca falla**» ✅. Pose oficial: puño en alto con un estallido de luz ([tráiler, 0:27](https://www.dailymotion.com/video/x8bnxd8?t=27)) | Óscar Flores ✅ |
| **Tsukasa Shishio** (獅子王司) | El rival: quiere un mundo sin ciencia moderna ni jerarquías; su apellido significa **«rey león»** ✅ | Arturo Cataño ✅ (2.ª pasada) |
| **Kohaku** (コハク), 2.ª en 2018 | Hace el micrófono con Kinro y Ginro; dice «**¡Micrófono, listo!**» (1×23, 00:21:16). Vista mirando la sal de Rochelle (§2.5). Según la wiki, **la primera en pisar la Luna** ✅ | Alicia Barragán ✅ |
| **Nikki Hanada** (花田仁姫) | Superfán de Lillian: **corrige la imitación de Gen** como una directora (2×07, 00:03:06) | ⚠️ |
| **Byakuya y Lillian** | La voz grabada y la canción del disco (1×24) | ⚠️ |

---

## 9 · ¿Quién es el más querido?

**Encuestas oficiales de Shūkan Shōnen Jump:**

| Encuesta | 1.º | 2.º | 3.º | Fuente |
|---|---|---|---|---|
| 1.ª (2018) | **Senku** (3.518 votos) | Kohaku | Gen | [ANN](https://www.animenewsnetwork.com/interest/2018-07-20/dr-stone-popularity-poll-picks-senku-as-king/.134369) ⚠️ (una fuente) |
| 2.ª (2019) | **Senku** | Ryusui (Japón) | Gen | [ANN](https://www.animenewsnetwork.com/interest/2019-07-29/senku-tops-shonen-jump-dr-stone-popularity-polls/.149492) ⚠️ |
| 3.ª (2021, 4.º aniversario) | **Gen** | Senku | Ryusui | [Shonen Jump News en X](https://x.com/WSJ_manga/status/1410135635575382016) ⚠️ |
| 4.ª (2023-2024, tras el epílogo) | **Gen** (41.317 votos) | Senku | ⚠️ | [X oficial](https://x.com/DrSTONE_off/status/1735597212074414291) + [collabo-cafe](https://collabo-cafe.com/events/collabo/dr-stone-character-popular-ranking-vol4-2024/) ✅ |

Top 20 de 2021: 1 Gen, 2 Senku, 3 Ryusui, 4 Ukyo, 5 Tsukasa, 6 Kohaku,
7 Chrome, 8 Stanley, 9 Xeno, 10 Hyoga, 11 Taiju, 12 Suika, 13 Kinro,
14 François, 15 Ginro, 16 Byakuya, 17 Joel, 18 Mozu, 19 Yuzuriha,
20 Chelsea. **Kaseki no está.**

Otras: en la encuesta de lectores en inglés de VIZ (septiembre de 2021),
1 Senku, 2 Gen, 3 Chrome ⚠️ ([VIZ](https://www.viz.com/blog/posts/dr-stone-popularity-poll-results-sept-2021)).
En la web japonesa **Nijimen** (público femenino), **1.º Gen** ⚠️
([Nijimen](https://nijimen.kusuguru.co.jp/topics/547296)). En la de
**Dengeki Online** (junio de 2026) no vi el resultado ⚠️
([Dengeki](https://dengekionline.com/article/202606/78820)).

**2.ª pasada, votos de fans fuera de Japón:**

- **AniList**, favoritos de usuarios (no es encuesta, es otro tipo de
  voto): **1.º Senku (15.479)**, 2.º Gen (5.241), 3.º Kohaku (3.237),
  4.º Chrome (2.779), 5.º Suika (2.287), 7.º Tsukasa (2.025), 9.º Kaseki
  (985) ✅ ([AniList](https://anilist.co/anime/105333)). Ojo: aquí **Senku
  gana con mucha ventaja**; Gen es 2.º. Suika y Kaseki suben mucho frente
  a las encuestas de Jump.
- **MyAnimeList**: 31.662 usuarios tienen la serie entre sus favoritas, de
  1.974.878 miembros ✅ ([MAL](https://myanimelist.net/anime/38691), vía
  la API de Jikan).
- **Premio**: **Senku ganó «Mejor protagonista»** en los 4.º Crunchyroll
  Anime Awards (2020) ✅ ([Wikipedia](https://en.wikipedia.org/wiki/4th_Crunchyroll_Anime_Awards), [CBR](https://www.cbr.com/crunchyroll-anime-award-winners/)).
  Suika, nominada en 2025 y 2026 ⚠️ (la categoría exacta no se confirmó).
- Reddit: «Is Ryusui Nanami your favorite character?», 615 votos ⚠️
  ([r/DrStone](https://www.reddit.com/r/DrStone/comments/1rnfnto/)).
- La encuesta de Dengeki Online (junio 2026) sigue **sin verse** ⚠️.

**Conclusión**: en Japón, **Gen es el más querido** desde 2021 y gana en
todas las franjas de edad en 2023. Fuera de Japón (AniList, premios),
**Senku** va primero. **Senku** es la cara de la serie. Para #hardware
funcionan los dos: **Senku fabrica**, **Gen vende y explica los precios**.
Kaseki y Suika son muy reconocibles pero no están arriba en votos.

---

## 10 · Doblaje latino

> [!note] 2.ª pasada: Doblaje Wiki ya se abrió
> En la 1.ª pasada no se abría, y cada nombre se dio por bueno con dos
> búsquedas distintas (una abierta con Doblaje Wiki, Atamashi, Depor y
> Atomix; otra sólo de prensa: Depor, Gamerfocus, TierraGamer, Arata,
> Versus Media). Ahora se leyó **el wikitext completo por la API**
> ([action=parse](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Dr._Stone), 32.300 caracteres). Donde la 1.ª pasada y la API
> coinciden, ✅. Lo que sólo sale en la API, ⚠️ una fuente.

### 10.1 Reparto

| Personaje | Actor latino | Estado |
|---|---|---|
| **Senku** | **Alejandro Orozco** | ✅ (también dirige doblaje; Usopp en *One Piece*, Gyutaro en *Demon Slayer*) |
| **Chrome** | **José Luis Piedra** | ✅ |
| **Gen** | **Brandon Santini** | ✅. Al principio se anunció a **Javier Olguín**; dos semanas después Crunchyroll confirmó en directo a Santini, sin decir por qué ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Dr._Stone), [Depor](https://depor.com/depor-play/anime/dr-stone-en-espanol-latino-el-anime-ya-cuenta-con-actores-para-su-doble-latinoamericano-mexico-noticia/)). Santini y Orozco grabaron un vídeo juntos en La Mole ([TikTok](https://www.tiktok.com/@brandon.santini3/video/7482971349279870213)) |
| **Kaseki** | **Óscar Rangel** | ✅ |
| **Suika** | **Valeria Mejía** | ✅ |
| **Kohaku** | **Alicia Barragán** | ✅ |
| **Ukyo** | **Eduardo Garza** | ✅ |
| **Ryusui** | **Óscar Flores** | ✅ |
| **Taiju** | **Miguel Ángel Ruiz** | ✅ |
| **Yuzuriha** | **Jessica Ángeles** | ✅ |
| **Tsukasa** | Arturo Cataño | ✅ (2.ª pasada: búsqueda + API de Doblaje Wiki). De niño: José Gilberto Vilchis (ep. 24) y Diego Becerril (ep. 33) ⚠️ |
| **Ruri** | Alexa Navarro | ✅ (Doblaje Wiki + AniList) |
| **Magma** | Ismael Verástegui | ✅ (Doblaje Wiki + AniList) |

**Cambios de voz** (2.ª pasada, Doblaje Wiki):

- **Gen**: Santini dobla hasta el ep. 75. **Desde el ep. 76, Iván
  García**: Santini se fue a dar clases a Colombia; el cambio es
  permanente en la 3.ª parte de *Science Future* ✅ (una página, pero es la
  ficha del propio doblaje).
- Senku de niño: **Alejandro Orozco** en la 4.ª (ep. 64); en la 1.ª y la
  3.ª, actor sin identificar. Taiju de niño: **Diego Becerril** (ep. 4).
- Ryusui de niño: Pascual Meza (ep. 40) y Ellie Rojo (ep. 84).
- Loops sueltos de otros actores: Senku en el ep. 31; Senku, Kohaku y
  Ryusui en el ep. 76; Suika en el ep. 29 (Susana Moreno, que luego es
  Mirai).

**Secundarios y recurrentes** (sólo Doblaje Wiki ⚠️ una fuente cada uno,
salvo donde se dice):

| Personaje | Actor latino |
|---|---|
| Kinro | Alan Huarte (1.ª) → **Diego Estrada** (2.ª-4.ª) |
| Ginro | **Francisco «Paco» Vargas**; un loop de Michell Cerón (ep. 79) |
| Kokuyo | Alejandro Ortega |
| François | **Carla Castañeda** (3.ª-4.ª) |
| Soyuz | Carlo Vázquez; de bebé, Paola García |
| Matsukaze | Alfredo Gabriel Basurto (eps. 48-66) → Óscar López (ep. 67) |
| Sai Nanami | Tommy Rojas |
| Jasper | Víctor Delgado (hasta el ep. 13) → Andrés García |
| Mirai | Susana Moreno |
| Episódicos | Anciano y Profesor (eps. 4 y 16): Hugo Navarrete y Bardo Miranda; Gozan (ep. 18): Hugo Núñez |

Minami, Nikki, Byakuya, Lillian, Akashi, Sagara y otros: **sin actor
identificado** en la propia Doblaje Wiki (sale «¿?»). No inventar.

### 10.2 Estudio, dirección y dónde se ve

- **Estudio**: **Audiomaster Candiani** (México) ✅ (2.ª pasada: campo
  `estudio_doblaje` de la ficha por la API, más los resúmenes de ANMTV de
  la 1.ª pasada).
- **Dirección** (2.ª pasada, ficha de Doblaje Wiki): **Bardo Miranda**
  (1.ª temporada) · **Jorge García** (2.ª y 3.ª parte 1) · **Víctor
  Medina** (3.ª parte 2) · **Jorge Reyes** (4.ª) ✅ (las dos primeras ya
  salían en la búsqueda de la 1.ª pasada; las dos últimas, una fuente ⚠️).
- **Traducción**: Regina Barajas (1.ª-2.ª), Lesslye Munguía Bautista (3.ª),
  Jaime Chaparro (4.ª). Audio de referencia: el japonés; guiones de
  Crunchyroll. 93 episodios doblados, 2020-2026 ⚠️ (una fuente).
- **Entrevista al reparto principal**, canal Funianime:
  [YouTube](https://www.youtube.com/watch?v=6A0cUyBgMc0) ⚠️ (existe, por
  `oembed`; no se pudo ver: YouTube pide iniciar sesión).
- **Crunchyroll** anunció el doblaje el 31 de octubre de 2020 ⚠️. Hubo
  doblaje del especial *Ryusui* ([ANMTV, 2022](https://www.anmtvla.com/2022/08/dr-stone-ryusui-crunchyroll-estrena-el.html)),
  *simuldub* de *New World* ([ANMTV, 2023](https://www.anmtvla.com/2023/04/dr-stone-3-temporada-comienza-su.html))
  y de *Science Future* ([Crunchyroll, 9-ene-2025](https://www.crunchyroll.com/es/news/announcements/2025/1/9/elenco-staff-doblaje-latino-dr-stone-science-future)) ✅.
  De la 3.ª parte de *Science Future* (2026) **no encontré** si ya está
  doblada ⚠️.
- También pasó por **Toonami en Cartoon Network** ([Gamerfocus](https://www.gamerfocus.co/anime/dr-stone-llegara-a-cartoon-network-bajo-el-bloque-toonami/),
  [TierraGamer](https://tierragamer.com/noticias/dr-stone-espanol-toonami/),
  [Arata](https://arata.lat/toonami-nos-lleva-a-una-era-de-piedra-con-dr-stone/)) ✅
  y por **Claro Video** en 2024, las dos primeras temporadas
  ([Bubbleblabber](https://latam.bubbleblabber.com/2024/07/dr-stone-llega-con-sus-primeras-dos-temporadas-a-claro-video/),
  [TVLaint](https://www.tvlaint.com/2024/07/seguro-al-10000000000-dr-stone-llego.html)) ✅.

### 10.3 Frases del doblaje latino

| Quién | Frase | Estado |
|---|---|---|
| Senku (Orozco) | «**10 mil millones por ciento**». La primera vez lo grabó como «10 millones por ciento» y **hubo que regrabar todas esas escenas** | La frase ✅ (Doblaje Wiki, TikTok [#10 mil millones por ciento](https://www.tiktok.com/discover/10-mil-millones-por-ciento), titular de TVLaint «¡Seguro al 10.000.000.000%!»). La anécdota ⚠️ (sólo Doblaje Wiki) |
| Chrome (Piedra) | «**¡Qué malote!**» por «ヤベえ». Es meme y guarda los dos sentidos del japonés (malo y asombroso) | ✅ (Doblaje Wiki; titular de [wdnes](https://www.wdnes.com/2023/04/que-malote-descubre-al-elenco-completo.html); clip oficial [«Problemas malotes»](https://www.youtube.com/watch?v=54hxtndu9Oc)) |
| Ginro | «Con permisito, dijo Ginrito» (guiño a Don Ramón) | ⚠️ sólo Doblaje Wiki (según la guía de cuadros de diálogo) |
| Gen (Santini) | «Calladito te ves más bonito» | ⚠️ sólo Doblaje Wiki |
| Senku | «唆るぜ これは» en latino | **No lo encontré** ⚠️. No lo inventes: pide el fotograma del episodio doblado |
| Gen | Su jerga al revés (ジーマー…) en latino | **No se adaptó: habla normal** ⚠️ (2.ª pasada, «Datos de interés» de Doblaje Wiki) |
| Senku | En 3×01 dice que harán un mapa «**como en Minecraft**»; en japonés no nombra ningún juego | ⚠️ sólo Doblaje Wiki (2.ª pasada) |
| Gen y Suika | Ep. 9: Gen dice «harén» en español y Suika lo pronuncia en inglés | ⚠️ sólo Doblaje Wiki (2.ª pasada) |
| Gen (Santini), muestra de audio | «Espera un momentito, por favor. ¿A dónde vas?… No es tan sencillo como crees, Magma» | ✅ oída con `voz.py` ([mp3](https://static.wikia.nocookie.net/doblaje/images/6/6b/GenAsagiriBrandonSantini.mp3)); sin episodio ⚠️ |

**Clips oficiales doblados**: la 1.ª pasada citó dos de Crunchyroll
([«La magia de Gen»](https://www.youtube.com/watch?v=Z3r3E6KgtUE) y
«Problemas malotes»). En la 2.ª pasada YouTube pidió iniciar sesión y
**no se pudieron bajar sus subtítulos** ⚠️: sus frases textuales siguen
sin minuto. Tampoco hay muestras con nombre de personaje para Kaseki,
Chrome ni Suika en Doblaje Wiki.

---

## 11 · Música

| Temporada | Opening | Ending | Estado |
|---|---|---|---|
| T1, 1.ª parte (2019) | «Good Morning World!», **BURNOUT SYNDROMES** | «LIFE», **Rude-α** | ✅. El OP1 sin créditos en 1080p, **mirado entero** en la 2.ª pasada ([Internet Archive](https://archive.org/details/dr-stone-op-1-ncbd-1080)) |
| T1, 2.ª parte | «三原色» (Sangenshoku), **PELICAN FANCLUB** | «夢のような» (Yume no You na), **佐伯ユウスケ** (Yusuke Saeki); single del 20-nov-2019, vídeo de estilo pastel | ✅ (2.ª pasada: [SPICE](https://spice.eplus.jp/articles/257466), [BARKS](https://www.barks.jp/news/?id=1000172895), [Apple Music](https://music.apple.com/jp/album/%E5%A4%A2%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA-tv%E3%82%A2%E3%83%8B%E3%83%A1-dr-stone-%E7%AC%AC2%E3%82%AF%E3%83%BC%E3%83%AB%E3%82%A8%E3%83%B3%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%83%86%E3%83%BC%E3%83%9E-ep/1484769945)) |
| *Stone Wars* (2021) | «楽園» (Rakuen), **Fujifabric** | «声？» (Koe?), **Hatena** | ✅ ([ANN](https://www.animenewsnetwork.com/news/2020-11-15/fujifabric-hatena-perform-theme-songs-for-dr-stone-stone-wars-anime/.166333)) |
| *New World*, 1.ª parte (2023) | «ワスレガタキ» (Wasuregataki), **Huwie Ishizaki** | «Where Do We Go?», **OKAMOTO'S** (single del 24-may-2023) | ✅ ([vídeo oficial](https://www.youtube.com/watch?v=81H41vp96ag)); ED ✅ en la 2.ª pasada ([ANN](https://www.animenewsnetwork.com/news/2023-03-25/dr-stone-new-world-anime-reveals-main-visual-ending-theme-song/.196419), [Anime Corner](https://animecorner.me/dr-stone-new-world-reveals-creditless-opening-and-ending-videos-for-1st-cour/)) |
| *New World*, 2.ª parte | «Haruka», **Ryujin Kiyoshi** (es el **opening**) | «好きにしなよ» (Suki ni Shinayo), **Anly**; vídeo de **arte de arena** | ✅ (2.ª pasada: OP en [ANN](https://www.animenewsnetwork.com/news/2023-08-26/dr-stone-new-world-anime-2nd-part-reveals-october-12-debut-theme-song-artists/.201655); ED en [TMS en X](https://x.com/tmsanime/status/1714325403941421462) y [Fandom](https://dr-stone.fandom.com/wiki/Suki_ni_Shinayo)) |
| *Science Future*, 1.ª parte (2025) | «CASANOVA POSSE», **ALI** | «Rolling Stone», **BREIMEN** | ✅ (2.ª pasada) |
| *Science Future*, 2.ª parte | «SUPERNOVA», **KANA-BOON** | «no man's world», **音羽-otoha-** | ✅ (2.ª pasada) |
| *Science Future*, 3.ª parte (2026) | «スキンズ» (Skins), **ASIAN KUNG-FU GENERATION** | «ROCKET», **BURNOUT SYNDROMES**: el grupo del primer opening cierra el círculo | ✅ (2.ª pasada) |

*Science Future*: dos fuentes que coinciden, [anime-song-info](https://anime-song-info.com/lp-drstone-op-ed/)
y [Animate Times](https://animatetimes.com/news/details.php?id=1736399013),
que confirma que hay vídeo oficial sin créditos de cada uno. La 3.ª parte,
también en [Animate Times](https://animatetimes.com/news/details.php?id=1775134655).

**La canción que importa para un servidor de canto**: «**One Small Step**»,
la que canta **Lillian Weinberg** en el disco de Byakuya (1×24, 00:15:53).
La canta **Laura Pitt-Pulford**, con letra de Kanata Okajima y JAKAZ y
música de **Hiroaki Tsutsumi** ✅ ([Fandom](https://dr-stone.fandom.com/wiki/One_Small_Step), [UtaTime](https://www.utatime.com/global/lyrics/lillian-weinberg-song-performed-by-laura-pitt-pulford/one-small-step/)).
En la serie, al oírla, alguien dice «Es demasiado bonita» (1×24, 00:17:54,
suena a Suika) y otro «Senku, ¿antes había tanta música así de buena?»
(00:18:20, suena a Chrome). El texto ✅; quién lo dice ⚠️ (el subtítulo
no lo marca).

**Ambiente** ⚠️: la banda sonora (**Tatsuya Kato, Hiroaki Tsutsumi y
YUKI KANESAKA** ✅ en la 2.ª pasada: seis bandas sonoras en [MusicBrainz](https://musicbrainz.org/release-group/89245a8e-e518-4c3e-a849-7db62035eb90),
de 2019 a 2026) mezcla orquesta épica para los inventos con temas
cómicos. El «**tema de la fabricación**» que suena en los montajes (1×23,
00:20:03 a 00:21:04, justo antes del «¡listo!») es el que todo fan
reconoce. **2.ª pasada**: el montaje se vio en el fansub, del
[19:49](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1189) al [21:04](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1264); **el nombre de la pista
no está** en los álbumes con nombre de escena ⚠️.

**El ending de las últimas semanas de la T1 es acuarela** (visto, [1×24,
22:40](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=1360)): luna, estrellas, siluetas a contraluz, azules
`#3E559A` `#352C96`. Muy distinto del cel nítido de la serie ✅.

---

## 12 · Vídeos

| Vídeo | Para qué | Enlace |
|---|---|---|
| PV 1 oficial de la T1 (2019) | Tono y personajes | [YouTube](https://www.youtube.com/watch?v=2ei4KpfCOAI) |
| Teaser 1 de la T1 | Primer vistazo | [YouTube](https://www.youtube.com/watch?v=J0jszHaElvA) |
| PV de *Stone Wars* | La guerra del teléfono | [YouTube](https://www.youtube.com/watch?v=esjDq0JQ_1s) |
| PV del especial *Ryusui* | El Drago y los Grandes Almacenes | [YouTube](https://www.youtube.com/watch?v=xR0mAOlclHg) |
| PV de *New World* | La cámara, el barco | [YouTube](https://www.youtube.com/watch?v=bITRcLr4xR8) |
| Tráiler de *Science Future* parte 3 (Crunchyroll) | El final | [YouTube](https://www.youtube.com/watch?v=FVNQnGIeRmc) |
| **«科学部 ＜千空'sラボ＞» nº 1**, serie oficial de ciencia | **El laboratorio como marca** | [YouTube](https://www.youtube.com/watch?v=EFh9izkrQqk) |
| Lista oficial de vídeos | Todo | [YouTube](https://www.youtube.com/playlist?list=PLtdSPZNWT1AtYMycjEmi83rWuFvRDTHnz) |
| Clips latinos de Crunchyroll: «La magia de Gen», «El mensaje de Byakuya», «Batalla de estática», «¡Feliz cumpleaños, Senku!», «Problemas malotes» | **Oír las voces latinas** | [1](https://www.youtube.com/watch?v=Z3r3E6KgtUE) · [2](https://www.youtube.com/watch?v=isEqsYxUbv4) · [3](https://www.youtube.com/watch?v=6wrypJwqmhQ) · [4](https://www.youtube.com/watch?v=lg5ReT8b98o) · [5](https://www.youtube.com/watch?v=54hxtndu9Oc) |
| «Voces de Dr. Stone \| Doblaje latino» | Comparar actores | [YouTube](https://www.youtube.com/watch?v=4jPDEEGK5fY) |
| Brandon Santini firmando (voz de Gen) | Material del actor | [YouTube Shorts](https://www.youtube.com/shorts/PlUKSINgzFU) |
| Redibujar una viñeta de Boichi | Entender su línea | [YouTube](https://www.youtube.com/watch?v=UyKIb7U6Jtk) |
| TikTok: «10 mil millones por ciento» | La frase viva en 2026 | [TikTok](https://www.tiktok.com/discover/10-mil-millones-por-ciento) |

**Los minutos exactos** de estos vídeos de YouTube **no se pudieron ver**
(YouTube pide iniciar sesión, también en la 2.ª pasada) ⚠️.

**2.ª pasada: tráileres oficiales mirados en Dailymotion** (mismo material,
republicado por medios), con minuto real:

| Vídeo | Minuto y qué se ve |
|---|---|
| [Tráiler oficial en español, Vidaextra](https://www.dailymotion.com/video/x8xu1ty) (1:42) | [0:45](https://www.dailymotion.com/video/x8xu1ty?t=45) «¡Salí!», Senku libre de la piedra · [0:50](https://www.dailymotion.com/video/x8xu1ty?t=50) Taiju rompe roca a golpes · [1:15](https://www.dailymotion.com/video/x8xu1ty?t=75) montaña verde · [1:20](https://www.dailymotion.com/video/x8xu1ty?t=80) el mar |
| [Tráiler *Stone Wars*, VO con subtítulos FR](https://www.dailymotion.com/video/x8a1zqs) (1:33) | [0:20](https://www.dailymotion.com/video/x8a1zqs?t=20) **el tocadiscos**: plato verde translúcido en un aparato de madera · [1:00](https://www.dailymotion.com/video/x8a1zqs?t=60) ficha de Nikki con su actriz · [1:04](https://www.dailymotion.com/video/x8a1zqs?t=64) «チート聴力をもつ弓使い» (el arquero del oído tramposo: Ukyo). Placas de texto útiles de referencia |
| [Tráiler *New World*](https://www.dailymotion.com/video/x8j8l2f) (0:47) | [0:24](https://www.dailymotion.com/video/x8j8l2f?t=24) Ryusui con sombrero pirata y el puño al aire · [0:36](https://www.dailymotion.com/video/x8j8l2f?t=36) «¡Icen las velas!» |
| [Tráiler del especial *Ryusui*](https://www.dailymotion.com/video/x8bnxd8) (1:40) | [0:27](https://www.dailymotion.com/video/x8bnxd8?t=27) **Ryusui con el puño en alto** y un estallido de luz · [0:33](https://www.dailymotion.com/video/x8bnxd8?t=33) tres chicas con top «E=mc²». Fecha en pantalla: 10-jul-2022 |
| [Tráiler *Science Future*, VOSTFR](https://www.dailymotion.com/video/x9boaek) (1:39) | [0:40](https://www.dailymotion.com/video/x9boaek?t=40) «La ciencia siempre ha sido nuestra ventaja» · [1:10](https://www.dailymotion.com/video/x9boaek?t=70) cartel «科学vs科学» (ciencia contra ciencia) · [1:30](https://www.dailymotion.com/video/x9boaek?t=90) «Así que tú eres Senku Ishigami». Fecha: 9-ene-2025, Tokyo MX |
| [OP1 sin créditos, 1080p](https://archive.org/details/dr-stone-op-1-ncbd-1080) (1:30) | [0:24](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=24) bosque petrificado · [0:45](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=45) Senku, puño al pecho · [1:12](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=72) campo de girasoles · [1:18](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=78) Senku y Taiju espalda con espalda |

- **TikTok** «10 mil millones por ciento»: la etiqueta existe (responde),
  pero no sirve los vídeos a los robots ⚠️. Cuántos y cuáles, sin ver.
- **Análisis en YouTube** (de `datos-video.md`: «Anime Truth #13e», «The
  real appeal of Dr. Stone», «Nobody is Talking About Dr Stone, BUT…»):
  candidatos **sin mirar** ⚠️.

---

## 13 · Videojuegos de la franquicia

### Dr.STONE バトルクラフト (*Battle Craft*), móvil

- **Poppin Games Japan** (Bandai Namco sólo sale como distribuidor en
  alguna tienda). Salió en Japón el **1 de septiembre de 2021** y en
  Norteamérica el **28 de noviembre de 2023** ✅ (2.ª pasada: Google Play,
  App Store y [TMS](https://tmsanime.com/news/dr-stone-battle-craft-mobile-game-now-available-in-north-america)). **Cerró el 1 de
  septiembre de 2026, a las 10:00**, a los cinco años ✅
  ([4Gamer](https://www.4gamer.net/games/544/G054403/20260707006/),
  [gamebiz](https://gamebiz.jp/news/429025),
  [Dengeki](https://dengekionline.com/article/202607/82597)).
- **Cómo es**: juntas materiales, **fabricas objetos** y los llevas a la
  batalla; la historia del anime se revive **en formato aventura**, con
  voces ✅ (resúmenes de 4Gamer y de las tiendas).
- **Su caja de diálogo** (2.ª pasada): **vista y medida** en las capturas
  de [Google Play](https://play.google.com/store/apps/details?id=com.poppingames.dsbc&hl=en_US):
  bisel octogonal, borde cian `#7EB6DF`, relleno azul verdoso oscuro
  `#21403D`, nombre en etiqueta aparte arriba a la izquierda. Detalle en
  §7.4 ✅. Otras fichas: [App Store](https://apps.apple.com/us/app/dr-stone-battle-craft/id1513882973),
  [QooApp](https://m-apps.qoo-app.com/en_us/app/16172), [web oficial](https://dsbc.poppin-games.com/).
- **Pantalla de victoria** ([captura](https://play-lh.googleusercontent.com/SxCKs_GBz5pXoKi-Yt0k3U993rzJ0tjwGbYsrBRDhM4AOyBU_vSwW-mWvQTbMUJQge7ngfJk)):
  iconos *chibi* de los seis personajes en fila con barra de vida,
  «Victory» en rojo con contorno blanco, cronómetro arriba a la derecha,
  botón «Next» verde ✅.
- **HUD de recursos** ([captura](https://play-lh.googleusercontent.com/TkkB69zh-01tVzL4O1Pas58x6Q67Vc1ggGKfRZDXLAfwN1AgBZNB5vrilfbM218ntXDmCFCJ)):
  **una gema azul** con el número y el nivel arriba a la izquierda
  («Resource Lv1 150»), personajes en iconos cuadrados abajo con el nivel
  en **una banderita amarilla**, botón «Leader» en dorado ✅. La gema con
  nivel sirve de modelo para **el rango de precio**.
- **Tarjetas de personaje** («Intro Card», 1000×1000): poses nuevas y
  oficiales (§3.3). La de Senku: **contrapicado cerrado**, personaje
  llenando el cuadro, el objeto de ciencia en primer plano cortando el
  borde de abajo.
- **Sucesor**: ninguno anunciado a 24-sep-2026 ⚠️ (una búsqueda en
  japonés).
- **Para la lámina**: la idea de **combinar materiales en un árbol de
  fabricación** es la misma de la hoja de ruta. Refuerza el concepto A.

**Jump Force / Jump Assemble**: Dr. Stone **no está** en el reparto de
*Jump Force* ✅ (2.ª pasada: búsqueda + roster de CBR); sólo sale en
propuestas de fans. **The Cutting Room Floor**: no hay página del juego
(no lo encontré; tcrf.net bloquea a los robots) ⚠️.

---
## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todos reconocen

| Qué | Dónde | Estado |
|---|---|---|
| «**100億％**» / «**10 mil millones por ciento**» | Desde el ep. 1 (1×01, 00:00:50). En TikTok sigue vivo en 2026, sobre todo en español | ✅ |
| «**唆るぜ これは!**» (¡esto me emociona!) | Cierre de muchos episodios | ✅ |
| «**¡Qué malote!**» de Chrome | Doblaje latino | ✅ |
| **La alianza por una cola** de Gen | 1×10, 00:21:38 | ✅ |
| **La canción de las pilas de manganeso** de Gen («乾電マンガン, さんざんマンガン…») | 1×23, 00:18:43 a 00:19:08 | ✅ |
| **Kaseki revienta la camisa** | Desde 1×11 | ✅ |
| **La ramen de cola de zorra** (猫じゃらしラーメン), «la gastronomía de la ciencia» | Mecha Senku la presenta en 1×11, 00:17:40 | ✅ |
| **El disco de Byakuya y la canción de Lillian** | 1×24, 00:14:01 a 00:17:52. El momento que hace llorar | ✅ |
| **Senku contó los segundos** durante 3.700 años | 1×01, 00:11:19 | ✅ |
| La jerga de Gen **en los eventos**: en Japón el público responde «ジーマーで?», «バイヤー!» | [post de una fan en X](https://x.com/Harum_dcst/status/1807888745645195501) | ⚠️ |
| «**Se me olvidó que hacían falta dos**» (el móvil sin receptor) | 1×24, 00:02:56 | ✅ |
| **Kohaku pega a Chrome** cuando la llama «gorila» (a Senku no) | Gag recurrente ([Fandom](https://dr-stone.fandom.com/wiki/Chrome#Trivia)) | ✅ (2.ª pasada) |
| El meme en español, con ejemplos | [TikTok de @alcadadegrasas](https://www.tiktok.com/@alcadadegrasas/video/7481294116182052102) y variantes «estoy seguro al 10 mil millones» (2024-2026) | ✅ (2.ª pasada; vistas sin ver ⚠️) |
| Fans que se identifican con **Chrome y Gen**: «coleccionaba piedras… me encantan los chicos científicos (y la cola)» | [Reddit, 126 votos, 210 comentarios](https://www.reddit.com/r/DrStone/comments/1v9z5u5/) | ✅ (2.ª pasada, comentario leído) |

### 14.2 Qué NO hacer (lo que un fan notaría)

- **Un smartphone o un micrófono moderno** en manos de Senku. Él mismo lo
  dice: «**No es *smart*, sólo *phone***» (1×19, 00:21:07). El Fifine va
  **sólo escrito en una etiqueta**, nunca dibujado.
- **Un laboratorio blanco y limpio**, con neones o pantallas. El
  laboratorio es **piedra apilada, madera, cortinas de tela y tinajas de
  barro**, con vidrio soplado a mano (visto, [1×11, 16:53](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1013)).
- **Plástico brillante de colores**: la primera plástica (fenolita,
  1×23, 00:16:02) sale **marrón oscuro y mate** ⚠️ (dato químico real; en
  el anime compruébalo).
- **Senku sonriendo dulce** o haciendo el «corazón» con las manos. Su
  sonrisa es **de medio lado**, con ceja levantada (vista, [1×19,
  20:42](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1242)) ✅, y su risa es «ククク».
- **La túnica de Senku blanca pura** o el pelo verde manzana: es **crema
  `#F5EBD6`** y **verde salvia `#5D906A`** (medidos, §16).
- **Gen con alcohol**: sólo bebe cola ✅ (2.ª pasada).
- **Kaseki con ropa nueva impecable**: se le rompe al emocionarse ✅ (2.ª
  pasada).
- **Calcar la bandera del Reino de la Ciencia de un fan art**: no hay
  imagen oficial confirmada (§18.8) ⚠️.
- **Gen como villano**: se cambió de bando en la temporada 1. Es el
  simpático.
- **Kaseki musculoso siempre**: sólo cuando se emociona; el resto del
  tiempo es un viejo pequeño.
- **Suika sin su casco o sin gafas** sin mirar el arco: las gafas llegan
  después del ep. 11 ⚠️.
- Escribir «**10 millones por ciento**» o «**mil millones por ciento**»:
  es «**10 mil millones**» (100億).
- **Inventar frases latinas**: sólo están comprobadas las de §10.3.
- Mezclar épocas sin querer: la **capa roja** de Senku es de *Science
  Future*; el traje de piel, de la temporada 1 ⚠️.

---

## 15 · Poses analizadas por personaje

La escena, el minuto y lo que se dice están en el subtítulo ✅. **La
postura de estas tablas es de memoria** ⚠️: saca el fotograma de ese
minuto y compruébalo antes de calcarla.

### Poses vistas en vídeo e imagen (2.ª pasada)

Éstas **sí se miraron** (fotograma abierto o imagen oficial). Empieza por
aquí.

| Personaje | Dónde (mirado) | Pose | Sirve para |
|---|---|---|---|
| **Senku** | [1×19, 20:42](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1242) | Primer plano, **sonrisa ladeada de suficiencia**, ceja levantada, bosque detrás. Confirma la fila 3 de su tabla | **Presentar** ✅ |
| **Senku** | [1×23, 21:04](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1264) | **Cuentagotas en una mano, vaso en la otra**, cejas fruncidas, abrigo de piel | **Explicar, experimentar** ✅ |
| **Senku** | [OP1, 0:45](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=45) | **Puño al pecho**, mirada decidida, camiseta «E=MC²» | **Animar** ✅ |
| **Senku y Taiju** | [OP1, 1:18](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=78) | **Espalda con espalda**, sonrisa cómplice, ciudad de noche desenfocada | **Celebrar en pareja** ✅ |
| **Senku** | [Intro Card de *Battle Craft*](https://static.wikia.nocookie.net/dr-stone/images/6/66/Battle_Craft_Intro_Card_Senku.png) | **Chasquea los dedos** sobre un tubo de ensayo, «E=mc²» en la venda, un vaso efervescente | **Presentar un invento** ✅ |
| **Senku** | [1×24, 22:10](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=1330) | De cerca junto a la hoguera, luz cálida, serio | **Pensar** ✅ |
| **Kohaku** | [1×23, 19:49](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1189) | De perfil, capa con ribete de piel, espada a la espalda, **boca abierta mirando un vaso de cristales** | **Preguntar**, la novata ✅ |
| **Ruri** | [1×24, 4:34](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=274) | Primer plano, ojos muy abiertos, boca entreabierta | **Asombro** ✅ |
| **Suika** (sin casco) | [1×11, 16:45](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1005) | Boca y ojos muy abiertos, **sonrojo de rayitas** | **Alegría, sorpresa** ✅ |
| **Ryusui** | [Tráiler especial, 0:27](https://www.dailymotion.com/video/x8bnxd8?t=27) | Torso desnudo, **puño al aire**, estallido de luz detrás | **Celebrar, anunciar** ✅ |
| **Chrome, Gen, Kaseki, Suika** | `settei_01` nº259-262 (tarjetas de *Battle Craft*) | Cuerpo entero en acción con su elemento: rayo, remolino, **llamas y martillo**, salto | **Presentar**, versión videojuego ✅ |

**Gen y Kaseki** siguen **sin fotograma propio**: sus episodios (1×10,
1×20, 2×01, 2×07, 3×03) no estaban sueltos en Internet Archive ni en
Dailymotion ⚠️. Sus tablas de abajo siguen de memoria, salvo las tarjetas
del juego.

### Senku

| # | Escena | Minuto | Qué pasa | Pose (⚠️) | Sirve para |
|---|---|---|---|---|---|
| 1 | 1×01 | 00:19:14 | Se libera de la piedra: «唆るぜ これは…» | De pie, trozos de piedra cayendo, sonrisa | **Presentar** |
| 2 | 1×09 | 00:05:50 | «En este mundo nada es gratis» | Brazos cruzados, mirada de reojo | **Regañar** (el precio) |
| 3 | 1×19 | 00:21:32 | «Si sigues las reglas, llegas a la meta» | Índice arriba, de medio lado | **Explicar** |
| 4 | 1×23 | 00:19:49 | «Sal de Rochelle: convierte el sonido en electricidad» | Cristal en la mano, mostrándolo | **Explicar** (micro) |
| 5 | 1×23 | 00:21:32 / 1×24, 00:02:28 | «¡Nace el móvil!» | El aparato en alto, todos detrás | **Celebrar** |
| 6 | 1×24 | 00:03:09 | «てへ» tras olvidar el segundo móvil | Mano en la nuca | Humor |
| 7 | 1×24 | 00:09:24 | «El disco es facilísimo» | Explicando junto al tocadiscos | **Explicar** |
| 8 | 1×24 | 00:15:13 | «ククク, me conoces» oyendo a su padre | Quieto, de espaldas o de perfil | **Pensar** |
| 9 | 3×02 | 00:18:44 | «Fotografía, fotografía» (la cámara) | Señalando al cielo (el globo) | **Animar** |
| 10 | 3×10 | 00:00:50 | «¡El intercomunicador!» | El pendiente entre dos dedos | **Presentar** (auriculares) |

### Gen

| # | Escena | Minuto | Qué pasa | Pose (⚠️) | Sirve para |
|---|---|---|---|---|---|
| 1 | 1×10 | 00:21:45 | «Qué mal negocio, por una cola» | Hombros caídos, sonrisa torcida | Humor (precio) |
| 2 | 1×20 | 00:01:04 | Imita la voz de Tsukasa | Mano en la garganta o en la barbilla | **Imitar voces** |
| 3 | 1×23 | 00:18:32 | «O sea, que me toca a mí» (las pilas) | Suspiro, manos abiertas | Humor |
| 4 | 1×23 | 00:18:43 | La canción de las pilas | Bailando con las pilas | **Animar** |
| 5 | 2×01 | 00:15:25 | El test: «A, B o C» | Dedos contando, cara de presentador | **Explicar** (etiquetas) |
| 6 | 2×01 | 00:15:34 | «¡Correcto! Diez mil millones de puntos» | Dedo arriba, guiño | **Celebrar** |
| 7 | 2×07 | 00:03:06 | Nikki le corrige | Gen tieso, Nikki gritando | **Regañar** (Nikki) |
| 8 | 2×07 | 00:08:28 | Respira antes de imitar a Lillian | Ojos cerrados, mano al pecho | **Pensar** / concentrarse |
| 9 | Especial | 00:34:29 | Presenta el desfile de moda | Brazo extendido hacia la «pasarela» | **Presentar** |
| 10 | 3×04 | 00:19:01 | «Lo más rentable que hay» | Dedo índice, sonrisa pícara | **Explicar** (barato) |

### Chrome

| # | Escena | Minuto | Qué pasa | Pose (⚠️) | Sirve para |
|---|---|---|---|---|---|
| 1 | 1×07 | 00:10:28 | «¡Mira mi magia de la buena!» | Brazos abiertos, pecho fuera | **Presentar** |
| 2 | 1×10 | 00:17:06 | «Soy un genio "usuario de la ciencia"» | Pulgar al pecho | **Presentar** |
| 3 | 1×21 | 00:12:41 | «¡Vamos, equipo de excavación!» | Corriendo con la mochila | **Animar** |
| 4 | 1×23 | 00:21:04 | «¡Plástico, listo!» | Puño en alto | **Celebrar** |
| 5 | 1×24 | 00:04:19 | «¡Botón de llamada!» | Inclinado sobre el aparato | Probar |
| 6 | 1×24 | 00:04:34 | «¿Lo ves, Ruri? ¡La ciencia es la bomba!» | Gritando al micro | **La reseña honesta** |

### Kaseki

| # | Escena | Minuto | Qué pasa | Pose (⚠️) | Sirve para |
|---|---|---|---|---|---|
| 1 | 1×11 | 00:15:04 | «¡Déjame a mí!» | Se hincha, la camisa revienta | **Celebrar** / animar |
| 2 | 1×11 | 00:15:53 | «Llevo cincuenta años de artesano» | Pecho fuera, vidrio en la caña | **Presentar** |
| 3 | 1×23 | 00:15:00 | Manda trabajar a Gen | Señalando, pícaro | **Regañar** |
| 4 | 1×23 | 00:21:13 | «¡Tubo de vacío, listo!» | Tubo en alto | **Celebrar** |
| 5 | 1×24 | 00:09:48 | «¡Oh-ho! ¡Qué sorpresa!» | Ojos como platos | Asombro |
| 6 | 3×03 | 00:00:36 | «Mis camaritas» | Abrazando las cámaras | **Presentar** (cámara) |

### Suika

| # | Escena | Minuto | Qué pasa | Pose (⚠️) | Sirve para |
|---|---|---|---|---|---|
| 1 | 1×08 | 00:09:17 | «Suika quiere ayudar» | Casco de sandía, cabeza gacha | Pensar |
| 2 | 1×08 | 00:15:05 | «¡Detective Suika!» | Pose de detective, casco puesto | **Presentar** |
| 3 | 1×23 | 00:21:06 | «¡Cables, listo!» | Brazos arriba | **Celebrar** |
| 4 | 1×24 | 00:04:21 | «¡Encendido!» | Dedo en el interruptor | **Explicar** (cómo se usa) |
| 5 | 4×23 | 00:03:10 | Imita voces sola | Sola en la oscuridad | Emoción |

### Ukyo y Minami

| Escena | Minuto | Qué pasa | Sirve para |
|---|---|---|---|
| 2×07 | 00:08:37 | Ukyo escucha el teléfono: «Es Lillian de verdad» | **Auriculares** (escuchar con atención) |
| 3×04 | 00:08:19 | «Ukyo, eso es lo tuyo» (el sonar) | Auriculares |
| 3×02 | 00:18:12 | Minami llora con su cámara | **Cámara** |

---

## 16 · Vestuario

| Personaje | Ropa | Estado |
|---|---|---|
| **Senku** (T1) | Túnica de **piel** clara con mangas cortas acampanadas, **cuello levantado**, bajo en picos hasta la rodilla y una costura que baja zigzagueando. **Cinturón con bolsas de cuero**. Zapatos de saco de cuero atados al tobillo. Lleva **E=mc²** escrito en el pecho | ✅ ([Fandom](https://dr-stone.fandom.com/wiki/Senku_Ishigami) + cosplay mirado, §4.4). **Color medido** (2.ª pasada): **crema `#F5EBD6`**, no blanca ✅ |
| **Senku** (antes de la piedra) | Uniforme escolar y **bata de laboratorio** encima | ⚠️ una fuente |
| **Senku** (*New World*) | Ropa moderna cosida por Yuzuriha para la sesión de fotos de Minami | ⚠️ una fuente |
| **Senku** (*Science Future*) | **Capa roja** que le da Suika al revivirlo en Sudamérica | ⚠️ una fuente |
| **Senku**, rasgos fijos | Pelo de punta, **blanco con puntas verdes**, **ojos rojos**, **marcas de petrificación** que suben desde las cejas | ✅ (Fandom y la ficha de Mecha Senku) |
| **Suika** | **Casco de sandía** con agujeros; después, **gafas** | ✅ |
| **Kaseki** | Ropa de aldea; al emocionarse, **sin camisa**, con la cuerda de la aldea al cuello | ✅ |
| **Gen** | Pelo **negro y blanco** (según la wiki, mitad izquierda negra y corta, mitad derecha blanca). Ropa: con luz dramática parece un abrigo oscuro de cuello alto; **de día, en las hojas, una túnica lila con ribete de piel blanca** (§8) | Pelo ✅; **el color de la ropa sin medir** ⚠️ |
| **Chrome** | Ropa de aldea, **camisa azul oscuro de manga corta** con el logo del Reino de la Ciencia en las mangas, bolsas de minerales | ✅ (2.ª pasada: imagen + texto de la wiki) |
| **Invierno** (1×23-1×24, cuando se hace el micro) | **Abrigos de piel** con ribete; Kohaku con capa de ribete de piel y la espada a la espalda | ✅ visto ([1×23, 19:49](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1189), [21:04](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1264)) |
| **Colaboraciones** | Ropa que sólo sale ahí: uniforme de **Lawson**, etiqueta de bar, circo, Navidad (§18.6) | ✅ |

**Colores medidos** (2.ª pasada, `estilo.py` y Pillow con filtro de tono;
nunca de memoria):

| Personaje | Parte | Hex | Medido en |
|---|---|---|---|
| **Senku** | Túnica | **`#F5EBD6`** crema cálido | [`Senku's fearlessness.png`](https://static.wikia.nocookie.net/dr-stone/images/1/12/Senku%27s_fearlessness.png), fotograma 1920×1080 con luz neutra, 3 puntos coinciden |
| Senku | Pelo, raíz | **`#D0CEBF`** crema apagado | [`Senku Ishigami Portrait.png`](https://static.wikia.nocookie.net/dr-stone/images/8/8b/Senku_Ishigami_Portrait.png), 1080×1080 |
| Senku | Pelo, puntas | **`#5D906A`** verde salvia (luz) · **`#2E5538`** verde botella (sombra) | retrato, filtro de tono |
| Senku | Ojos | **`#59050F`** rojo sangre oscuro | retrato, zona del iris |
| Senku | Piel | **`#D0B6A1`** | píxel directo |
| **Chrome** | Camisa | **`#245E6B`** azul petróleo | [`Chrome's determination.png`](https://static.wikia.nocookie.net/dr-stone/images/4/41/Chrome%27s_determination.png), 12,4 % de la imagen |
| **Suika** | Casco, cáscara | **`#B4C856`** verde lima | hoja de modelo oficial (settei) |
| Suika | Casco, raya | **`#70872B`** verde oliva | settei |
| Suika | Poncho | **`#373C42`** azul gris casi negro | settei |
| Suika | Pelo | **`#F3DD89`** rubio pálido | settei |
| **Kaseki** | Túnica, tono medio | **`#5B4A34`** marrón cuero | [`Kaseki Anime Profile.png`](https://static.wikia.nocookie.net/dr-stone/images/7/71/Kaseki_Anime_Profile.png) |
| Kaseki | Túnica, sombra | **`#362C1D`** | ídem |
| **Gen** | Ropa | sin medir ⚠️ | — |

Esto **corrige** la paleta de la 1.ª pasada: el pelo no es verde manzana
`#7DBF4A` sino salvia; la túnica no es blanca sino crema (lo confirma el
cosplay de §4.4).

**Lo icónico**: Senku con **la túnica crema de la temporada 1**. Es la que
reconoce todo el mundo y la de casi todos los key visuals de `arte_01` ✅.
Segundo: **el casco de sandía de Suika**, único en el reparto ✅.

---

## 17 · Paisajes y fondos de pantalla

### 17.1 Los sitios, con su luz

**2.ª pasada**: la luz y la paleta medidas de ocho sitios están en §5.2,
con su fotograma. Aquí, lo que falta o cambia:

- **La aldea Ishigami en invierno** (1×23-1×24): nieve, cielo blanco,
  brasas dentro de las casas. Es **cuando se fabrica el micrófono**. El
  interior se vio y se midió (§5.2); **el exterior nevado no tiene paleta
  medida** ⚠️.
- **El laboratorio**: **piedra apilada, madera y tela**; la luz de la
  entrada es difusa y neutra, el calor lo pone el fuego (§5.2) ✅.
- **El puesto de los Grandes Almacenes** (especial): día, sol, gente.
- **El Perseus** (*New World*): barco de madera, mar de noche, radio.
- **La Luna** (*Science Future*, parte 3): el cartel final, Senku y Xeno
  mirando la Luna de noche (§3.1).

### 17.2 Fondos de pantalla en alta

| Qué | Tamaño | Enlace |
|---|---|---|
| Senku Ishigami, 4K | 3840×2160 | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1126614) |
| «Senku & Team», de Thomas V. Kristiansen | 3840×2160 | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1042353) |
| Colección 4K (24 fondos) | ≥ 3840×2160 | [Alpha Coders](https://alphacoders.com/dr-stone-4k-wallpapers) |
| Colección general (140) | variable | [Alpha Coders](https://alphacoders.com/dr-stone-wallpapers) |
| Otras | variable | [Wallpaper Cave](https://wallpapercave.com/dr-stone-4k-wallpapers) · [WallpaperAccess](https://wallpaperaccess.com/dr-stone) · [WallpaperFlare](https://www.wallpaperflare.com/search?wallpaper=Dr.+Stone) |

Son **capturas o arte oficial resubido por fans**: sólo para mirar ⚠️.

**2.ª pasada: tamaños medidos** y más fondos con autor:

- Los dos de Wallpaper Abyss, bajados y medidos con Pillow: [Senku 4K](https://images8.alphacoders.com/112/1126614.jpg)
  **3840×2160, 5,45 MB** (resubido, sin autor original) y [«Senku &
  Team»](https://images3.alphacoders.com/104/1042353.jpg) **3840×2160,
  0,52 MB**, acreditado a Thomas V. Kristiansen ✅.
- **Wallhaven** (tamaño de su API; licencia: sólo fondo personal, no
  redistribuir):

| Qué | Tamaño | Subido por | Enlace |
|---|---|---|---|
| **Kohaku**, el más guardado de la serie (♥97) | 2400×3597 | ThorRagnarok | [imagen](https://w.wallhaven.cc/full/9m/wallhaven-9mgkg1.jpg) |
| **Chrome y Kohaku** | 5500×3000 | Zains | [imagen](https://w.wallhaven.cc/full/e7/wallhaven-e757vw.jpg) |
| Senku con un matraz | 2560×1440 | dexterb8 | [imagen](https://w.wallhaven.cc/full/kw/wallhaven-kw25d6.png) |
| Grupo: Senku, Suika, Kinro, Ginro, Kohaku | 1920×1081 | EsQdero64 | [imagen](https://w.wallhaven.cc/full/73/wallhaven-73l7l9.png) |
| Noche, estrellas y Luna | 2560×1440 | SCPZero | [imagen](https://w.wallhaven.cc/full/r2/wallhaven-r21qgq.jpg) |
| «Kingdom of Science face», de vk-for-da-win (DeviantArt) | 3840×2160 | Aniru | [imagen](https://w.wallhaven.cc/full/vg/wallhaven-vge265.png) |
| Kohaku, de dinocozero (DeviantArt) | 1920×1080 | Aniru | [imagen](https://w.wallhaven.cc/full/dg/wallhaven-dgv81j.jpg) |

---

## 18 · Guía para generar con IA (Firefly, Canva)

Úsala **sólo para fondos, objetos y ambientes**. Los personajes se
recortan de fotogramas reales por `v3/integrar.py`.

**Rasgos que nunca cambian**
- Senku: pelo de punta hacia arriba, **raíz crema `#D0CEBF` con puntas
  verde salvia `#5D906A`**, **ojos rojo oscuro `#59050F`**, **grietas que
  suben desde las cejas**, túnica **crema `#F5EBD6`** con cuello alto,
  «E=mc²» en el pecho y cinturón con bolsas (medido, §16).
- Suika: casco de sandía **o** gafas redondas. Kaseki: viejo pequeño de
  cejas y barba blancas; músculos sólo si se emociona ⚠️.
- **Todo está hecho a mano**: madera, piedra, cuerda, vidrio con burbujas,
  cobre martillado.

**Estilo**
- Anime de TV (TMS Entertainment), **línea fina y limpia**, **sombreado de
  dos tonos**, colores naturales y cálidos. Fondos pintados, con textura.
- **Medido** (2.ª pasada, §18.1): personajes en **cel plano** (64-84 % de
  zonas planas) con **línea marrón o gris oscuro** (`#5A4A45` a
  `#8C7764`), **casi nunca negra**; fondos **pintados en degradado**
  (54-65 %). El laboratorio es gris piedra; el calor lo pone el fuego.
- Luz: **fuego de horno** naranja por un lado y **luz fría de invierno**
  por la ventana.

**Palabras que ayudan**
> stone and wood laboratory, stacked stone walls, cloth curtain door,
> clay jars on wooden shelves, primitive wooden workshop, stone age laboratory, hand-blown glass
> vacuum tubes, brown bakelite megaphone, rochelle salt crystals,
> copper wire coils, hemp rope, straw roof, warm furnace glow, snowy
> night outside the window, anime background art, cel shading, TMS style

**Palabras que lo estropean**
> sci-fi, cyberpunk, neon, hologram, smartphone, condenser microphone,
> studio, chrome metal, clean white lab, photorealistic, chibi

**Ejemplo de prompt (fondo del concepto A)** ⚠️ propuesta:
> Interior of a primitive wooden laboratory hut at night in winter,
> anime background art. A rough wooden workbench with a dark brown
> hand-made plastic megaphone, sparkling transparent crystals, three
> hand-blown glass vacuum tubes glowing orange, coils of copper and gold
> wire, clay jars. On the back wall a large board with paper notes
> connected by hand-drawn arrows. Warm furnace light from the left, cold
> blue light from a small window with snow. No people. Cel shading,
> clean lines.

**Imágenes de referencia** (2.ª pasada: ya abiertas):

- **Estilo**: [key visual de *Stone Wars*](https://static.wikia.nocookie.net/dr-stone/images/9/9f/Dr._Stone_Stone_Wars_Key_Visual_3.png)
  (2324×3277, `arte_01` nº1).
- **Proporciones y color**: las hojas de modelo de `settei_01` (nº246 Gen,
  nº247 Chrome con el sombreado, nº254-255 Suika) y los retratos de
  `vestuario_01` (nº222 Chrome, nº224 Kohaku, nº225 Senku, nº228 Gen).
- **Cómo se reparte la luz y la sombra**: [hoja de sombreado de Chrome](https://static.wikia.nocookie.net/dr-stone/images/b/b5/Chrome_Shading_TV_Animation_Design_Sheet.png)
  (1200×877).
- **El laboratorio**: el fotograma [1×11, 16:53](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1013) y el modelo
  de Jerry Teng en Sketchfab para el volumen.
- **El micro**: [1×23, 19:49](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1189) (la sal) y la hoja de ruta
  [1×19, 21:07](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1267).
- **Pose de acción con objeto**: la tarjeta de Senku de *Battle Craft* (§15).

**Vocabulario de expresiones** para la IA de imagen (lo visto en la serie):

| Emoción | Cómo se dibuja en Dr. Stone | Palabras |
|---|---|---|
| Suficiencia, presentar | **Sonrisa ladeada**, ceja levantada (Senku, 1×19, 20:42) | smirk, raised eyebrow, confident |
| Sorpresa, alegría | Ojos muy abiertos, boca abierta, **sonrojo de rayitas** (Suika, 1×11, 16:45) | wide eyes, open mouth, blush lines |
| Concentración | Cejas fruncidas, mirada al objeto (Senku, 1×23, 21:04) | furrowed brows, focused |
| Asombro | Primer plano, boca entreabierta (Ruri, 1×24, 4:34) | close-up, awestruck |
| Impacto | **Rayas de velocidad radiales**, trama de puntos (manga, cap. 216) | speed lines, screentone |
| Celebrar | Puño en alto con estallido de luz (Ryusui) | fist raised, light burst |
| *Chibi* | Sólo en los iconos de *Battle Craft* (pantalla de victoria) | chibi icon |
| Gotas de sudor, venas de enfado, fondos de emoción | **No documentados** en las partes ⚠️: no inventarlos | — |

**Para una IA de texto** (diálogos en su voz):

- **Senku**: frases cortas y rudas, recetas de un paso. **Exagera con
  cifras enormes**: «al **10 mil millones por ciento**» (nunca «10
  millones»). Se ríe «ククク» (en español, «Je, je, je» pequeño ⚠️
  propuesta). Nunca dice «creo». Cierra con «¡Esto sí que me emociona!».
- **Gen**: vendedor, suave y rápido. **Tests de tres opciones** y «¡Correcto!
  **Diez mil millones de puntos**». Quejas teatrales («¡Qué crueldad!»).
  En latino **habla normal**, sin jerga al revés. Diminutivos: «Espera un
  momentito» (muestra real de Santini).
- **Chrome**: entusiasta, gritón: «**¡Qué malote!**» (latino ✅). Grita al
  terminar una pieza.
- **Kaseki**: «¡Oh-ho!», viejo artesano que presume de sus cincuenta años.
- **Suika**: de niña habla de sí misma en tercera persona: «Suika quiere
  ayudar».
- **Puntuación**: ¡! en todo lo que se anuncia; el «¡…, listo!» como
  cierre de cada pieza. Sin rayas ni paréntesis (regla del dueño).

**Frases reales por emoción** (subtítulo japonés con minuto, traducción mía
salvo las marcadas «latino»):

| Emoción | Frase | Quién y dónde |
|---|---|---|
| **Alegre** | «¡Esto sí que me emociona!» | Senku, 1×23, 00:22:12 |
| Alegre | «¿Lo ves, Ruri? ¡La ciencia es la bomba!» | Chrome, 1×24, 00:04:34 |
| Alegre | «¡Micrófono, listo!» | Kohaku, 1×23, 00:21:16 |
| **Enfadado** | «En este mundo nada es gratis» | Senku, 1×09, 00:05:50 |
| Enfadado | «¡No! ¡Nada que ver!» | Nikki a Gen, 2×07, 00:03:06 |
| Burla | «Calladito te ves más bonito» (latino ⚠️) | Gen a Senku, 3×10 |
| **Explicando** | «Se llama sal de Rochelle. Convierte el sonido en electricidad» | Senku, 1×23, 00:19:49 |
| Explicando | «El micrófono y el altavoz son lo mismo: sólo convierten sonido en electricidad y al revés» | Senku, 1×24, 00:05:03 |
| Explicando | «No necesita pilas. Eso sí, el sonido es bajísimo» | Senku, 3×10, 00:03:04 |
| **Animando** | «Por lejos que parezca, si sigues las reglas llegas a la meta al diez mil millones por ciento. ¡Eso es la ciencia!» | Senku, 1×19, 00:21:32 |
| Animando | «¡Vamos, equipo de excavación científica!» | Chrome, 1×21, 00:12:41 |
| Animando | «10 mil millones por ciento» (latino ✅) | Senku |
| **Triste** | «Mi cámara» | Minami, 3×02, 00:18:12 |
| Triste | «Me siento sola» (さみしいんだよ) | Suika, 4×23, 00:03:10 a 00:06:21 |
| **Vendiendo** | «Es el primer artículo de lujo; tardará en venderse» · «Gracias por su compra» | Gen, especial, 00:35:36 y 00:35:51 |

---
## 18.1 · Estilo de dibujo y técnica, y cómo replicarlo (2.ª pasada)

Punto 18 del encargo. No existía en la 1.ª pasada.

### Del manga: Boichi

- **Estudió Física** «como preparación para dibujar ciencia ficción», y
  luego un posgrado en tecnología de imagen ✅ ([Fandom: Boichi](https://dr-stone.fandom.com/wiki/Boichi) + reseñas).
- **No copia fotos**: sobre la calculadora de parametrones de Senku dijo
  que no había nada que copiar, y que aunque lo hubiera, «dibujarlo igual
  no lo haría un invento de Senku»: tenía que ser del Mundo de Piedra y
  original ✅ ([Boichi en X](https://x.com/Boichi_Bo1/status/2051986720875282549)).
  Para el *reboot* de *Byakuya* juntó unas 1.500 fotos de referencia ⚠️.
- **Entinta casi sin corregir**: un vídeo suyo se hizo viral en Japón
  porque **apenas usa el borrador ni «deshacer»**, con un solo tamaño de
  pincel, sin capas ni selecciones ✅ ([Togetter](https://togetter.com/li/1615629)).
  Tiene tres ayudantes (todos mangakas) y tarda **1 a 1,5 horas por
  página** ⚠️ ([SLJ, AnimeNYC 2019](https://goodcomicsforkids.slj.com/2019/12/20/animenyc-a-peek-behind-the-scenes-of-dr-stone/)).
- **Los bolsillos de Senku** dicen lo que piensa: más bolsillos cuando
  está en peligro ✅ (misma fuente).
- Tomó *En busca del fuego* (1981) como referencia de puesta en escena
  prehistórica ⚠️ (una fuente).

### Del anime: TMS Entertainment

- El director de la 4.ª temporada, **Shuhei Matsushita**: como «la
  ciencia no miente», estudiaron el color real de plantas, ríos y
  piedras, **incluso el color de una llama según su temperatura**. Al
  llegar a América **rehicieron los fondos** por la humedad y el aire,
  para que el cambio de continente se note sin decirlo ✅ ([entrevista, J:COM](https://jmagazine.myjcom.jp/category/anime/post001463/)).
- **Ficha de estilo** (AniList + [ficha de TMS](https://www.tms-e.co.jp/alltitles/2010s/762101.html)):
  color **Fusako Nakao** (中尾総子) ✅; fotografía **Takeshi Kuzuyama**
  (葛山剛士; «Katsurayama» en AniList es la misma persona) ✅; animador
  principal **Hiroyuki Horiuchi** ✅; estudio interno **TMS8PAN** ✅.
  Dirección de arte: **Shunjiro Yoshihara** (TMS) y **Tomoyuki Aoki**
  (AniList); cuál hizo cada temporada, sin confirmar ⚠️.
- **Whiteman** (*Science Future*) se hizo en **3DCG** para que ondulara
  y resultara inquietante ⚠️ (un resumen de foro japonés).
- **Filtros de posproducción** (grano, aberración, *bloom*): no hay
  fuente que los nombre para este anime ⚠️. No inventarlos.

### Medido con `estilo.py` (sobre las imágenes oficiales de la wiki)

| Tipo de imagen | Sombreado | Línea | Color de línea |
|---|---|---|---|
| Retratos y hojas de modelo (Senku, Chrome, Gen, Kohaku, Suika) | **plano (cel)**, 64-84 % de zonas planas | poca a normal | **marrón o gris oscuro** `#5A4A45` a `#8C7764`, casi nunca negro |
| Fondos y escenas de acción | **degradado pintado**, 54-65 % | poca | tonos cálidos del ambiente `#B9A091`, `#63564A` |
| Escena dramática (`Chrome's determination.png`) | mixto, 40/41 | normal | `#6E564E` |
| Ending de la T1 | **acuarela** (visto, §11) | — | — |

**Personaje en cel plano con línea de color + fondo pintado**: el patrón
clásico del anime, aquí con números ✅.

### El manga, visto de cerca

En la [doble página del cap. 216](https://static.wikia.nocookie.net/dr-stone/images/6/69/Chapter_216.png) (2190×1600) ✅:
**trama de puntos fina y regular** en piel y pelo (no degradado digital);
**rayas de velocidad radiales** muy densas, blancas sobre negro o negras
sobre blanco; el **metal del cohete con rayado cruzado a mano**, sin gris
de trama; y **«SENKU7» rotulado** en el fuselaje.

### Cómo replicarlo en Photoshop

1. **Línea**: pincel de tinta al 100 % con **grosor variable** (tableta),
   marrón `#5A4A45` en la piel y gris `#3E3E3E` en la ropa oscura. Negro
   puro sólo en las sombras cerradas del pelo.
2. **Color**: planos, **dos tonos por zona** (luz y una sombra dura hecha
   con el lazo poligonal, no con pincel suave).
3. **Fondo**: capa aparte, pincel de mezcla con degradados, desenfoque
   ligero para separarlo del personaje.
4. **Final**: ruido monocromático 2-3 % y **curvas** que suban el naranja
   en las escenas con fuego (el «look» cálido que describe Matsushita).
5. **Título**: textura de piedra + **bisel y relieve** alto + grietas a
   mano; colores del cartel del ep. 1 (§6.1).

### Cómo replicarlo en Blender

1. **Personajes**: *toon shader* de 2-3 bandas (`Shader to RGB` +
   `ColorRamp` con escalones). Contorno con **Solidify invertido** en el
   marrón o gris medido, no negro.
2. **Vidrio de laboratorio**: *Principled BSDF* con transmisión alta y algo
   de rugosidad, **con burbujas**: está soplado a mano.
3. **Luz**: una clave cálida de horno (~2800 K) y un relleno frío de nieve
   o luna (~7000 K).
4. **Encuadre**: el de la tarjeta de *Battle Craft*: **contrapicado
   cerrado**, el personaje llena el cuadro y **el objeto de ciencia en
   primer plano** corta el borde de abajo.
5. **Modelos base**: los de §4.1 (CC BY). El de leonardo.sensei2 ya viene
   en Blender 2.8. Encima, el *toon shader* de arriba.

### Encuadres y composición (lo visto)

- **Presentar**: primer plano con sonrisa ladeada (1×19, 20:42).
- **Explicar**: plano medio con el objeto en las manos a la altura del
  pecho (1×23, 21:04).
- **Asombro**: primer plano frontal de quien mira el invento (1×24, 4:34).
- **Objeto en su sitio**: plano general, el objeto arriba y pequeño, el
  sitio enorme (la torre de 1×24, 2:17).
- **Pareja**: espalda con espalda (OP1, 1:18).

## 18.2 · Texturas 2D (2.ª pasada)

Punto 19 del encargo. Junto con el 3D (§4) y las texturas reales (§5.3),
son las tres capas.

| Capa | Qué hace la serie | Recurso libre | Licencia |
|---|---|---|---|
| **Trama de puntos** (sombras) | Puntos finos y regulares en piel y pelo (cap. 216) | [FREE Manga Screentone Pack 1](https://assets.clip-studio.com/en-us/detail?id=2142037), Clip Studio Assets | Gratis dentro de Clip Studio ✅ |
| Trama, en PNG sueltos | Ídem | [Free Screen Tone Collection 1](https://manga-with-stef.com/free-screen-tone-collection-1), Manga with Stef | Gratis según el sitio ⚠️ |
| **Rayas de velocidad** | Radiales, detrás de «START!» y del cohete | Dibujarlas: no se buscó recurso aparte ⚠️ | — |
| **Rayado cruzado** | Metal y máquinas | A mano (Boichi no usa trama ahí) | — |
| **Grano de papel** | Página impresa | [Paper001](https://ambientcg.com/view?id=Paper001), 003, 005, 006 (ambientCG) | CC0 ✅ |
| **Cuerda y tejido** | Cinturones, recintos de la aldea | [Rope001](https://ambientcg.com/view?id=Rope001), [Rope002](https://ambientcg.com/view?id=Rope002) | CC0 ✅ |
| **Flechas-tubo con trama** | Las de la hoja de ruta (§3.3) | Trazo grueso + la trama de arriba dentro | — |
| **Emblema del Reino de la Ciencia** | Según la wiki, **un cohete entre dos estrellas** en una bandera | Sólo hay reconstrucciones de fans ([Commons](https://commons.wikimedia.org/wiki/File:Flag_of_Kingdom_of_Science.svg), DeviantArt): **no calcar**; dibujarlo de cero ⚠️ | — |
| **Moneda Drago** | Relieve con orla de perlitas y trama de puntos (§3.3) | Dibujarla de cero a partir de `Drago_Coins.png` | — |
| **«E=mc²»** | Pintado en la túnica de Senku, en la venda de la tarjeta del juego | Letra a mano (Kalam) | OFL ✅ |

## 18.3 · Gustos y detalles de cada personaje (2.ª pasada)

Punto 20 del encargo. Cumpleaños, sangre y altura de [AniList](https://anilist.co/anime/105333)
(fichas de personaje); gustos y objetos de la trivia de la wiki de Fandom.

| Personaje | Cumpleaños · sangre · altura | Le gusta | Odia o rechaza | Siempre lleva | Cómo se ve a sí mismo |
|---|---|---|---|---|---|
| **Senku** | 4 de enero · AB · 171 cm ✅ (también lo dice él, 1×24, 00:06:20) | **Videojuegos**: cita Mario, Civilization, Dragon Quest y sobre todo Monster Hunter (cap. 63); de niño, Doraemon ✅ | El sentimentalismo; que algo sea imposible («ni un milímetro») ✅ | El cinturón con bolsas (§16). La bata de laboratorio es de antes de la piedra ⚠️ | Genio frío que **no admite ser generoso**; corta el romance con su «boda y divorcio» con Ruri ✅ |
| **Gen** | 1 de abril · B · 175 cm ✅ | Su baraja hecha a mano; **la cola** ✅ | **El alcohol** ✅ | **La baraja con tres comodines** con frases ✅ | El mentalista más hábil; se encoge para parecer inofensivo ⚠️ |
| **Chrome** | 4 de febrero · A · 170 cm ✅ | Coleccionar minerales desde niño; explorar ✅ | Que lo traten de aficionado en lo suyo ⚠️ | **Su bolsa de piedras** ✅ | Antes «hechicero», ahora **«usuario de la ciencia»** ✅ |
| **Kaseki** | 9 de febrero · AB · 155 cm ✅ (AniList + wiki) | Hacer lo nunca visto con las manos; **sus vehículos** (coche, laboratorio móvil, el Perseus) ✅ | Que desguacen sus máquinas sin rehacerlas ✅ | La cuerda de la aldea al cuello cuando revienta la camisa ✅ | El artesano de la aldea desde hace cincuenta años ✅ |
| **Suika** | 9 de septiembre · 119 cm ✅ | Ayudar y ser útil; **imitar voces** ✅ | Sentirse inútil (1×08) ✅ | **El casco de sandía**, que le hizo Kaseki ✅ | De niña, en tercera persona; lo deja al crecer ✅ |
| **Kohaku** | 8 de agosto · B · 160 cm ✅ | Pelear, cazar; **cuidar de Ruri** ✅ | Que Chrome la llame «gorila» ✅ | Su espada ✅ (vista, §2.5) | Protectora de la aldea y de Ruri ✅ |
| **Ryusui** | sin dato | El lujo, el mar; «**lo quiero**» (欲しい) ✅ | — | Su barco, su fortuna | Capitán de leyenda: «Mi instinto de marinero nunca falla» ✅ |
| **Tsukasa** | 10 de octubre · 195 cm ✅ | Un mundo sin jerarquías ni ciencia moderna ✅ | La ciencia que deja a los adultos dañar a los jóvenes ✅ | — | Protector de los jóvenes; «rey león» ✅ |
| **Ukyo** | 5 de junio · A · 173 cm ✅ | La paz: odia la sangre sin sentido ✅ | La violencia inútil ✅ | Su arco; el oído del sonar | — |
| **Taiju** | 2 de abril · 189 cm ✅ | Trabajar aunque sea en lo pequeño, gritando ✅ | — | — | — |

## 18.4 · Por qué la gente la ama (2.ª pasada)

Punto 21 del encargo.

**Los números**

- **MyAnimeList**: **8,26/10** con 1.191.080 votos, puesto 372 general,
  49 en popularidad, 1.974.878 miembros ✅ ([MAL](https://myanimelist.net/anime/38691)).
- **Manga**: **20 millones de copias** (27 tomos, con digital), marzo de
  2026 ✅ ([The Fandom Post](https://www.fandompost.com/2026/03/22/manga-by-the-numbers-dr-stone-crosses-20-million-volume-mark/),
  [Manga Mogura RE](https://x.com/MangaMoguraRE/status/2035286156691333167)).
  En mayo de 2022 eran 13 millones: **casi duplicó en cuatro años**.
- **Senku, «Mejor protagonista»** en los Crunchyroll Anime Awards 2020 ✅
  (§9).

**Con quién se identifica el público**

- Con **Chrome y Gen**: coleccionar piedras, la cola, «los chicos
  científicos» ✅ ([Reddit, 126 votos](https://www.reddit.com/r/DrStone/comments/1v9z5u5/)).
- Un programador, con **Sai**: «el anime es exacto» ⚠️ (sólo el título,
  [Reddit, 114 votos](https://www.reddit.com/r/DrStone/comments/1sn8x9v/)).
- Reseñas de MAL: engancha **por los personajes** más que por la ciencia
  ⚠️ (resumen, sin cita textual).
- Un fan hispano: la vio **«de casualidad por Cartoon Network»** y el
  final le pareció «impresionante y conmovedor» ✅ (comentario textual,
  hilo de abajo). Encaja con Toonami (§10.2).

**Las escenas que hacen llorar** (hilo «Has Dr. Stone ever made you cry?»,
[734 votos, 94 comentarios](https://www.reddit.com/r/DrStone/comments/1v6dnxe/),
el más votado sobre el tema ✅):

| Escena | Dónde | Por qué duele | Estado |
|---|---|---|---|
| **El disco de Byakuya** y la canción de Lillian («One Small Step») | 1×24, 00:14:01 a 00:17:52 | El padre de Senku le habla desde hace 3.700 años; construyó el «cofre del tesoro» para él. Suena la voz grabada con ruido de altavoz | ✅ (subtítulo + Reddit) |
| **Minami y su cámara** | 3×02, 00:18:12 | La perdió hace miles de años; Senku le hace otra. «Se derrumbó, y yo también» | ✅ (subtítulo + Reddit) |
| **Suika sola** imitando las voces de todos | 4×23, 00:03:10 a 00:06:21 | Años sola, rehace el líquido de revivir; «me siento sola» | ✅ subtítulo |
| **Suika ve por primera vez** con gafas | — | Sin minuto ⚠️ | ⚠️ Reddit |
| **Ruri curada**: no recuerda la última vez que pudo levantarse | — | Sin minuto ⚠️ | ⚠️ Reddit |
| **La invasión de Stanley** (*Science Future*): caen Taiju y Ryusui, Suika se queda sola | — | Sin minuto ⚠️ | ⚠️ Reddit |
| **Que se acabe** la serie | final | Muchos comentarios; uno en español | ✅ |

Las que hacen **reír**: la canción de las pilas de Gen (1×23, 00:18:43),
«se me olvidó que hacían falta dos» (1×24, 00:02:56), Kaseki reventando
la camisa (§14.1). Música, luz y encuadre de cada escena de llanto: sólo
el disco de Byakuya tiene música identificada; el resto, sin ver ⚠️.

## 18.5 · Fan dubs y comunidad hispana (2.ª pasada)

Punto 22 del encargo. YouTube no deja bajar vídeo ni metadatos desde el
servidor: **canal y título confirmados con `oembed`**, pero **sin vistas
ni fecha** ⚠️.

**Fandubs latinos de escenas**

| Canal | Vídeo | Enlace |
|---|---|---|
| **Alex Fandubs** | «Dr. Stone: New World "Búsqueda del tesoro" [Fandub Latino]» | [YouTube](https://www.youtube.com/watch?v=0nQIJhVza68) ✅ |
| **Zacky-Kun Fandubs** | «DR. STONE (Trailer) - Fandub Latino» | [YouTube](https://www.youtube.com/watch?v=vwxypyHzAN0) ✅ |
| **Olea Dubs** | «La cocina de Senku (Fandub Latino)» | [YouTube](https://www.youtube.com/watch?v=qAwQZEOBDRc) ✅ |
| **EnmaDS** | «Dr. Stone - Ending - Fandub Latino/Cover en Español (Full Version)» | [YouTube](https://www.youtube.com/watch?v=VmHCWf4_ByU) ✅ |
| ¿? | «El Reencuentro de Taiju y Senku [Fandub Latino]» | [YouTube](https://www.youtube.com/watch?v=c6_Buonxdnc) ⚠️ no cargó (¿privado o borrado?) |

**Covers de openings en español**

| Canal | Vídeo | Enlace |
|---|---|---|
| **David Delgado** | «DR.STONE Opening 2 Full - Cover Español Latino \| Sangenshoku» | [YouTube](https://www.youtube.com/watch?v=WT3Gm4_igIs) ✅ |
| David Delgado | «Dr. STONE Todos los Openings en Español Latino» | [YouTube](https://www.youtube.com/watch?v=mGPjLinWsO8) ✅ |
| **André - A!** (Edgardo Artieda) | OP 8 «SKINS» · OP 6 «CASANOVA POSSE» | [1](https://www.youtube.com/watch?v=MAzpBwx41Kc) · [2](https://www.youtube.com/watch?v=CKUm45hXEdI) ✅ |
| **FUGATOON** | «DR STONE Opening 3 [Rakuen] (Cover Español Latino)» | [YouTube](https://www.youtube.com/watch?v=eNZ_2736ZB4) ✅ |

La comunidad hispana canta **casi todos los openings** (al menos 1, 2, 3,
6 y 8), no sólo los mira.

**Memes y parodias**: el «**10 mil millones por ciento**» en TikTok, con
clips propios de usuarios hispanos (2022-2026) ✅ (§14.1). Una **parodia
hispana larga** (tipo sketch): no la encontré ⚠️ (dos búsquedas, TikTok y
YouTube). El propio doblaje mete guiños latinos: «Con permisito, dijo
Ginrito» (Don Ramón) y «como en Minecraft» ⚠️ (§10.3).

## 18.6 · Colaboraciones y cruces (2.ª pasada)

Punto 23 del encargo. Su arte trae **ropa y poses nuevas**.

**Cafés temáticos en Japón**

| Café | Fechas | Arte nuevo | Fuente |
|---|---|---|---|
| **AMO CAFE**, cafetería retro de los 60-70 (Ikebukuro, Namba) | 12-sep a 7-oct-2025 | Estilo *kissaten* | [collabo-cafe](https://collabo-cafe.com/events/collabo/dr-stone-amo-cafe-tokyo-osaka-2025/) ✅ |
| **NATSLIVE «Christmas Party»** (Tokio, Nagoya, Osaka) | 5 a 24-dic-2025 | **Ropa navideña** | [collabo-cafe](https://collabo-cafe.com/events/collabo/dr-stone-natslive-cafe2025/) + X ✅ |
| **«Bar Francois»** | 19-mar a 9-abr-2026 | Todos **de etiqueta**, François de barman | [X](https://x.com/weretigers/status/1895490016245383491) ⚠️ una fuente |
| **mixx garden «holiday picnic»** (Tokio, Osaka) | 15-may a 14-jun-2026 | **Picnic** al aire libre | [collabo-cafe](https://collabo-cafe.com/events/collabo/dr-stone-holiday-picnic-cafe-mixx-garden-2026/) + mixxgarden ✅ |
| **Circo** (Animate Cafe Stand Ikebukuro) | 2 a 28-jul-2026 | Todos como **troupe de circo** | [Essential Japan](https://essential-japan.com/news/new-dr-stone-collaboration-cafe-offers-fans-circus-inspired-drinks-food-and-collectibles/) ⚠️ una fuente |

Todos en [collabo-cafe, categoría Dr. STONE](https://collabo-cafe.com/events/category/dr-stone/).

**Marcas y museos**

- **Lawson Store 100** (20-ago a 9-sep-2025, 634 tiendas): **Senku, Gen,
  Suika, Kohaku, Ryusui y Ginro con el uniforme de Lawson**, tradicional y
  moderno: ropa que no sale en ningún otro sitio ✅ ([Essential Japan](https://essential-japan.com/news/a-new-dr-stone-collab-is-coming-to-convenience-store-chain-lawson/),
  [X](https://x.com/weretigers/status/1952052749425602937)).
- **Space Travelium TeNQ**, «ROAD TO THE MOON» (18-jul a 18-oct-2026):
  café temático y **una grabación de voz exclusiva del actor de Senku** ✅
  ([Have a Good Holiday](https://www.haveagood-holiday.com/en/articles/dr-stone-tenq-road-to-the-moon-exhibition)).
- **Museo Nacional de Naturaleza y Ciencia** (Ueno): exposición sobre la
  ciencia de Dr. STONE ⚠️ ([una fuente](https://home.ueno.kokosil.net/en/archives/65547)).
- **Mecha Senku** como mascota física en AnimeJapan ✅ (§7.1).

**Figuras oficiales** (pose en 3D real)

- **Nendoroid Senku** (nº1262, Good Smile): tres caras y objetos hechos a
  mano: tarro de barro, botella de medicina, algodón de azúcar ✅ ([Good Smile](https://www.goodsmile.info/en/product/9106/Nendoroid+Senku+Ishigami.html)).
  **Cómo sostiene un invento**: referencia directa para #hardware.
- **POP UP PARADE Senku** (Good Smile), más grande, sin piezas ✅ ([Good
  Smile](https://www.goodsmile.info/en/product/9900/POP+UP+PARADE+Senku+Ishigami.html)).

**Cosplay**: el de Senku de §4.4 (materiales reales) ✅.

**Cruces con otros juegos o gachas** (tipo Fortnite): **no los encontré**
⚠️ (dos búsquedas). No es «no existe».

## 18.7 · Obras parecidas y temas relacionados (2.ª pasada)

Punto 24 del encargo.

- **Recomendadas por los usuarios de AniList**: *Ascendance of a
  Bookworm*, *That Time I Got Reincarnated as a Slime*, *Astra Lost in
  Space*, *Cells at Work!*, *Food Wars!*, *7SEEDS* ✅.
- Webs de recomendación que coinciden: *7SEEDS* y *Uninhabited Planet
  Survive!* (supervivencia en grupo tras una catástrofe), *Made in Abyss*
  (exploración con meta) ✅ ([Anime Corner](https://animecorner.me/five-anime-to-watch-if-you-like-dr-stone/),
  [Dualshockers](https://www.dualshockers.com/best-anime-like-dr-stone/)).
- **Dr. Stone contra *Cells at Work!***: los dos grandes del «anime que
  enseña» ✅ ([CBR](https://www.cbr.com/dr-stone-vs-cells-at-work-best-educational-anime/)).
- **Influencias del guionista, Riichiro Inagaki**: Senku bebe de **Agon
  Kongo**, el genio arrogante de su *Eyeshield 21* ✅ (Wikipedia +
  reseñas). *Video Girl Ai* como influencia de tono ⚠️ (una fuente, sin
  la cita original).
- **TV Tropes**: Senku es «**For Science!**»; Senku y Taiju, «**Brains
  and Brawn**» ✅ ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/DrStone)).
- **Otras láminas del servidor**: se revisaron los encargos de
  `encargos/` buscando hardware, laboratorio, ciencia, construir,
  inventar, fabricar. **Ningún otro canal es #hardware** y **ninguna otra
  biblia tiene el tema laboratorio o invento** ✅. Lo más cercano,
  *Cyberpunk Edgerunners* (27) y *Cyberpunk 2077* (114): tecnología urbana
  y neón, lo contrario de este taller de piedra. No hay riesgo de repetir.

## 18.8 · El mundo, la historia y sus símbolos (2.ª pasada)

Punto 25 del encargo. De la wiki ([Stone World](https://dr-stone.fandom.com/wiki/Stone_World),
[Petrification](https://dr-stone.fandom.com/wiki/Petrification),
[Kingdom of Science](https://dr-stone.fandom.com/wiki/Kingdom_of_Science),
[Story Arcs](https://dr-stone.fandom.com/wiki/Story_Arcs)) y Wikipedia ✅.

**Las reglas en cinco líneas**

1. Un destello **petrifica a toda la humanidad** (y a las golondrinas) de
   golpe, en lo que sería 2019.
2. La piedra **no envejece**: quien despierta tiene el mismo cuerpo y la
   misma mente de hace 3.700 años.
3. Sólo el **fluido de revivificación** (ácido nítrico y alcohol) rompe la
   piedra, persona a persona.
4. La naturaleza siguió: **3.700 años de bosques y animales sin humanos**.
   Hay que rehacer la civilización desde cero.
5. Hay un arma de petrificación **deliberada** (Ibara, Why-Man): la gran
   pregunta es quién y por qué.

**La historia por sagas**

| Saga | Capítulos | Qué pasa |
|---|---|---|
| **Prólogo** | 1-12 | Senku y Taiju despiertan; Tsukasa quiere revivir sólo a los jóvenes «puros» |
| **Aldea Ishigami** | 13-45 | Senku se gana a la aldea, cura a Ruri y funda **el Reino de la Ciencia** con Chrome, Kaseki, Kohaku y Suika. Aquí se hace **el móvil** |
| **Guerra de las piedras** (*Stone Wars*) | 46-82 | Reino de la Ciencia contra el Imperio de Tsukasa; acaba en **alianza**, no en conquista |
| **Origen de la petrificación** | 83-212 | El barco **Perseus**, la Isla del Tesoro (Ibara), América (Stanley, Xeno, Corn City) |
| **De la piedra al espacio** | 213-232 | El cohete, los astronautas, **la Luna** y Why-Man. Kohaku es la primera en pisarla |

**Momentos clave**: la fundación del Reino de la Ciencia (cap. 15), la
alianza al final de la guerra (cap. ~80), Byakuya estaba en la Estación
Espacial durante la petrificación (1×24), y el capítulo final «Dr. STONE»
(232) ✅.

**Emblemas**

- **Bandera del Reino de la Ciencia**: **un cohete entre dos estrellas**;
  se iza en la torre de radio de la Isla del Tesoro ✅ (texto de la wiki).
  **El dibujo exacto** (colores, proporciones) **no se confirmó** en una
  imagen oficial ⚠️: Commons dio error 429 y las de DeviantArt son de fans.
- **El Imperio de Tsukasa no tiene bandera** documentada ⚠️: **sólo la
  ciencia tiene emblema**. Buen argumento para la lámina.
- **«SENKU7»** rotulado en el cohete (cap. 216) ✅.
- **Las monedas Drago** (§3.3) ✅.

**Vocabulario que un fan reconoce al instante**

| Término | Japonés | Qué es |
|---|---|---|
| **Stone World** | ストーンワールド | El mundo sin gente |
| **Fluido de revivificación** | 復活の秘薬 | Lo que rompe la piedra |
| **Reino de la Ciencia** | 科学の王国 | El bando de Senku |
| **Imperio de Tsukasa** (de la Fuerza) | — | El bando de la fuerza |
| **Perseus** | — | El barco |
| **Why-Man** | — | Quien petrificó el mundo («why», por qué) |
| **Corn City**, **Superalloy City** | — | Las ciudades nuevas de América |
| **10 mil millones por ciento** | 100億% | «Totalmente seguro» |
| **¡…, listo!** | クリア | Pieza terminada |
| **Hoja de ruta** | ロードマップ | El plan hasta el invento |
| **Drago** | ドラゴ | La moneda |
| **Mecha Senku** | メカ千空 | El robot que explica |

## Las hojas de contacto (2.ª pasada)

Las montó `herramientas/investigar_serie.py` con la wiki de Fandom
(páginas de Senku, Chrome, Gen, Kaseki y Suika y sus galerías): **449
imágenes enlazadas, 371 grandes, 8 hojas de 48**. Se miraron las 8 y se
dejaron **3 en `hojas/`** (2400×1704, JPEG, menos de 1,1 MB cada una). Cada
miniatura lleva **su número arriba a la izquierda y su tamaño y nombre de
archivo debajo**: el original se baja con ese nombre de la wiki
(`https://dr-stone.fandom.com/wiki/File:<nombre>`). Las otras cinco hojas
(fotogramas sueltos y páginas de manga repetidas) quedan en
`herramientas/referencias/dr-stone/`, fuera del repositorio.

### `hojas/arte_01.jpg` — arte oficial y portadas (punto 1)

| Nº | Qué es | Para qué |
|---|---|---|
| **1** | [Key visual de *Stone Wars*](https://static.wikia.nocookie.net/dr-stone/images/9/9f/Dr._Stone_Stone_Wars_Key_Visual_3.png), 2324×3277 | **Estilo** general; la capa verde |
| **5** | «Senku and Gen love money», 2880×1619 | **Concepto B**: Senku y Gen con dinero, caras de codicia |
| **7** | «Manganese Battery», 2880×1618 | Gen con una pila en la mano: **las 800 pilas** |
| **14** | *Stone Wars* KV 1, «闘戦», 1830×2529 | Dos manos que se agarran |
| **17** | «"it means liar", in flowers», 1920×2257 | Gen con la flor de «mentiroso» (§8) |
| **18** | «I'm an insanely smart genius sorcerer», 1920×2075 | **Chrome, pulgar al pecho**: presentar |
| **24** | «Chrome making sodium hypochlorite», 1920×1916 | Chrome trabajando con las manos |
| **28-29** | Capítulos 216-217, 2190×1600 | **Trama, rayas de velocidad**, el cohete (§18.1) |
| **36, 40, 43** | Tomos US 8 y 12, tomo 25 | Portadas: cuerpo entero con objetos, en grupo |
| **38-39** | Key visuals de la T1, 1449×2048 | **Grupo** de cuatro |
| **41** | «Senku and Gen samurai», 1918×1517 | Senku y Gen en pareja, ropa distinta |
| **45-48** | Portadas a color de capítulos (Jump), 1918×1400 | Poses de grupo, títulos grandes |

### `hojas/vestuario_01.jpg` — caras y ropa (puntos 13 y 15)

| Nº | Qué es | Para qué |
|---|---|---|
| **222** | Retrato de Chrome, 1080×1080 | Cara de frente, sonrisa |
| **224** | Retrato de Kohaku, 1080×1080 | Cara, ojos turquesa, gargantilla |
| **225** | [Retrato de Senku](https://static.wikia.nocookie.net/dr-stone/images/8/8b/Senku_Ishigami_Portrait.png), 1080×1080 | **Cara de Senku** y hex del pelo y los ojos (§16) |
| **228** | Retrato de Gen, 1078×1077 | **Cara de Gen**, cicatriz, pelo bicolor, túnica lila |
| **205** | Capítulo 123: Gen como **as de picas**, «切り札は、自分。» (el as soy yo) | **Concepto B**: Gen y su baraja |
| **221** | «Kaseki Face Detail», 1067×1097 | Cara de Kaseki en manga, cejas y barba |
| **230** | «Calcite Anime», 1440×802 | Chrome mostrando un mineral al sol |
| **234** | «Ten leaders of KoS», 2000×560 | **Los diez del Reino de la Ciencia** en fila: lámina en grupo |
| **239** | «Suika's and Kaseki's Fashion Outfits» (manga), 870×1270 | Ropa de Suika y Kaseki |

### `hojas/settei_01.jpg` — hojas de modelo y videojuego (puntos 1, 11 y 15)

| Nº | Qué es | Para qué |
|---|---|---|
| **246** | Gen, hoja de referencia de la Isla del Tesoro, 1244×860 | Proporciones de Gen, con capucha |
| **247** | [Chrome, hoja de sombreado](https://static.wikia.nocookie.net/dr-stone/images/b/b5/Chrome_Shading_TV_Animation_Design_Sheet.png), 1200×877 | **Cómo se reparte la sombra** (cel de dos tonos) |
| **254-255** | Suika con y sin casco (settei), 1200×848 | **Colores medidos** de Suika (§16); caras |
| **256** | «Radio waves» (manga), 1033×983 | Una página con **«SENKU'S PHONE»** rotulado: el teléfono en el manga |
| **259-262** | Tarjetas de *Battle Craft*: Chrome, Gen, Kaseki, Suika, 1000×1000 | **Poses de acción oficiales** con su elemento |
| **263** | «Gen doctor outfit», 816×1224 | Gen de cuerpo entero con bata blanca |
| **270** | «Copper Tube», 1283×721 | **Gen con abrigo de piel en la nieve**, un tubo de cobre: invierno del micro |
| **271, 278** | Gen y Chrome en el bosque, de día, 1280×720 | Pareja; ropa con luz neutra |
| **280** | «Gen drinks the Cola (anime)», 1280×720 | **La cola** de Gen |
| **287** | «Senku and Gen at the observatory», 1280×720 | Noche, cielo estrellado |

**Lo mejor para #hardware**: `arte_01` nº5 (el dinero, concepto B),
`settei_01` nº256 (el teléfono en el manga) y nº270 (invierno y cobre), y
`vestuario_01` nº205 (Gen as de picas) y nº225 (cara de Senku).

---
## 19 · Tres conceptos para la lámina de #hardware

Los tres usan los textos de §0. Las frases «en la voz de la serie» son
**traducción mía del japonés** (con su minuto); las latinas comprobadas son
sólo «¡Qué malote!» y «10 mil millones por ciento». Recortes siempre por
`v3/integrar.py` y comprobados a 1:1. **Ninguna mano sin apoyo**: cada
personaje toca algo visible.

**2.ª pasada**: los tres conceptos siguen, pero ahora con **imágenes
vistas** en vez de memoria. Cambia el aspecto del laboratorio (piedra,
no sólo madera), el estilo de la hoja de ruta (árbol de videojuego), la
pose de Senku (vista en vídeo), los colores (medidos) y los precios de B
(monedas Drago). Lo nuevo va en cada concepto como «2.ª pasada».

### Concepto A — «¡Micrófono, listo!» (Senku en el laboratorio)

- **Objeto y sitio**: el **banco de trabajo del laboratorio** (1×11,
  00:16:49), una **noche de invierno** (el ep. 23 pasa en invierno, con
  estufas de cobre). Encima: **el megáfono-micrófono** con cristales de sal
  de Rochelle pegados (1×23, 00:19:55), **tres tubos de vacío** de vidrio
  soplado, **una bobina de hilo de oro**, un puñado de **pilas de
  manganeso** (las 800 de Gen) y un tarro con el poso rosa del vino.
  Detrás, en la pared, **la hoja de ruta**: papeles clavados en un tablón,
  unidos por flechas a mano.
  En Blender: banco ([Rough Wood, CC0](https://polyhaven.com/a/rough_wood)),
  tablón ([Worn Planks, CC0](https://polyhaven.com/a/worn_planks)), megáfono
  (cono), tubos (vidrio con burbujas), cristales (prismas), bobina, pilas,
  papeles con curvatura y chinchetas de madera.
- **Personaje**: **Senku**. Pose de 1×23, 00:19:49 (**explicar**): un
  cristal en una mano y **la otra apoyada en el megáfono** sobre el banco.
  Si hace falta más energía, la de 1×24, 00:02:28 (**celebrar**). Detrás,
  pequeño y desenfocado, **Chrome** asomando por el borde del tablón.
- **Cómo habla**:
  - Senku, en **una nota de papel clavada** junto a su cabeza, con Kalam:
    **«En este mundo nada es gratis»** (1×09, 00:05:50).
  - Chrome, en un trozo de corteza, con Bangers: **«¡Qué malote!»**
    (frase latina comprobada).
- **Dónde va cada texto**:
  - Tallado en el tablón, arriba, con Rubik Dirt: **Hardware**.
  - Hoja de ruta, de izquierda a derecha, cajas de papel con Kalam:
    **Micros, interfaces, auriculares y cámaras** → **Un hilo por
    cacharro** → **Con el precio delante** → y la caja final, la meta,
    con una estrella: **Si lo tienes, di cómo te fue de verdad**.
    Cada caja lleva el sello «**¡Listo!**» de 1×23.
  - Etiqueta de madera atada con cuerda al megáfono, con Oswald:
    **Ejemplo: Fifine K669, unos 35 USD**.
- **Para que no quede plano**: **un tubo de vacío desenfocado en primer
  plano**, brillando naranja; la bobina corta el borde de abajo; **luz de
  horno** por la izquierda, **azul de nieve** por la ventana; destellos en
  los cristales; la sombra de Senku cae sobre la hoja de ruta.
- **2.ª pasada**:
  - **El sitio, visto** ([1×11, 16:53](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1013)): **muros de piedra
    apilada**, estantes de madera con **tinajas de barro**, cortina de
    tela en la puerta, vidrio verde en la mesa. Paleta medida: grises
    piedra `#B0B1A2` `#848276` `#6E695E`, claro `#EAE2D3`; el calor, del
    fuego. Textura de muro: [Rock Cliff, CC0](https://polyhaven.com/a/rock_cliff_large_02).
  - **La pose**: mejor la **vista** de [1×23, 21:04](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1264):
    **cuentagotas en una mano y el vaso en la otra**, cejas fruncidas,
    abrigo de piel (es invierno, cuadra con el ep. 23). Para la cara, la
    **sonrisa ladeada** de [1×19, 20:42](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1242). Colores de §16:
    pelo `#5D906A`, ojos `#59050F`.
  - **La hoja de ruta** con el estilo real: **nodos redondos** con el
    material (como [1×19, 21:07](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1267)), **flechas-tubo gruesas con
    trama de puntos** y un **«START!»** con rayos de velocidad al principio
    y **«GOAL»** en la última caja (como el [roadmap del cohete](https://static.wikia.nocookie.net/dr-stone/images/8/89/Roadmap_Senku_Spaceship.png)).
  - **Los cristales**: piedritas transparentes **en un vaso** (así salen
    en [1×23, 19:49](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1189)), no sueltas.
  - **Referencias de hoja**: `arte_01` nº1 (estilo), `vestuario_01` nº225
    (cara de Senku), `settei_01` nº247 (cómo cae la sombra).
- **Lámina 2**: el mismo tablón en grande, con **tres columnas de la hoja
  de ruta** (Qué es, Cuánto cuesta, Qué opinas) y **las 12 etiquetas como
  etiquetas de madera** colgadas de clavos. **Mecha Senku** en la esquina
  de abajo, a la altura del pecho, dice con Kalam: **«Elige una de cada
  columna»** ⚠️ (frase mía).

### Concepto B — «Grandes Almacenes Senku» (Gen vende)

- **Objeto y sitio**: el **puesto de «デパート千空»** del especial
  *Ryusui* (00:33:38), de día, en la plaza de la aldea. Un **mostrador de
  madera** con los cacharros de la serie en exposición, cada uno con su
  **etiqueta de precio** colgada: el **megáfono-micrófono** (Micrófono),
  el **tubo de vacío** (Interfaz), **el pendiente-intercomunicador** sobre
  un paño (Auriculares), **la cámara de Kaseki** (Cámara) y **una estera
  de paja colgada** detrás (Tratamiento acústico ⚠️, idea mía: en la serie
  no hay escena de acústica).
  En Blender: mostrador, toldo de tela, etiquetas de madera con cordel,
  los cuatro objetos, estera.
- **Personaje**: **Gen**, el más querido, detrás del mostrador. Pose del
  test (2×01, 00:15:25): **una mano sobre el mostrador** y la otra
  contando con los dedos. Al fondo, pequeños: **Ryusui** chasqueando los
  dedos junto a lo más caro («¡Lo quiero!», 欲しい) y **Suika** con el
  pendiente-radio («no necesita pilas», 3×10, 00:03:04).
- **Cómo habla**: **el test de Gen** en una pizarra de madera colgada del
  toldo, con Kalam: **«¿Cuánto cuesta?»** y debajo **«¡Correcto! Diez mil
  millones de puntos»** (2×01, 00:15:34).
- **Dónde va cada texto**:
  - Letrero del toldo, pintado, con Rubik Dirt: **Hardware**.
  - Tira de tela bajo el letrero: **Micros, interfaces, auriculares y
    cámaras**.
  - Cartelito en el mostrador, con Oswald: **Con el precio delante**.
  - Cada objeto, su etiqueta: así se ve **Un hilo por cacharro** (una
    tarjeta de madera junto a los objetos lo dice).
  - **Un cuaderno abierto** sobre el mostrador, con una pluma: **Si lo
    tienes, di cómo te fue de verdad**.
  - Etiqueta del micro: **Ejemplo: Fifine K669, unos 35 USD**.
- **Para que no quede plano**: **sol entre las rayas del toldo**
  (sombras en franjas), etiquetas que se balancean, el borde del mostrador
  desenfocado delante, gente borrosa detrás.
- **Lámina 2** (la mejor de las tres para esto): el mismo mostrador **con
  las 12 etiquetas**. Las de tipo, colgadas sobre cada objeto. Las de
  precio, **como el test de Gen**: A **Menos de 50**, B **De 50 a 150**,
  C **De 150 a 400**, D **Más de 400** (en la D, Ryusui). Las de opinión,
  **como sellos** junto al cuaderno: **Lo tengo y lo recomiendo**, **No lo
  compres**, **Alternativa barata** (esta última con Suika y la radio sin
  pilas).
- **2.ª pasada**:
  - **Los precios, en monedas Drago**: la serie tiene **cuatro monedas
    acuñadas** ([Drago_Coins.png](https://static.wikia.nocookie.net/dr-stone/images/4/4c/Drago_Coins.png)), y el canal
    **cuatro rangos**. Cada rango, **una moneda de relieve** con orla de
    perlitas y trama de puntos, colgada de su objeto: la pequeña para
    **Menos de 50**, la grande de dos cabezas para **Más de 400**. Se
    modelan en Blender (relieve, metal gastado). Encaja con el chiste de
    la serie: el dinero vale lo que su metal.
  - **Gen**: su pose sigue sin fotograma ⚠️. Usar su tarjeta de *Battle
    Craft* (`settei_01` nº260) y su retrato (`vestuario_01` nº228) para la
    cara. Que lleve **la baraja** en la mano libre, apoyada en el
    mostrador (su objeto de siempre). Nada de alcohol a la vista: **una
    botella de cola** si hace falta un gesto.
  - **Ryusui**: la pose vista del tráiler, **puño en alto** ([0:27](https://www.dailymotion.com/video/x8bnxd8?t=27)),
    pequeño al fondo junto a la moneda de «Más de 400».
  - **La pizarra del test**: si se quiere algo más «de juego», la caja de
    *Battle Craft* (bisel, borde cian `#7EB6DF`, relleno `#21403D`, nombre
    en etiqueta aparte, §7.4) sirve para **las etiquetas A, B, C, D**.
    Queda más frío que la madera: probar las dos.

### Concepto C — «La primera llamada» (Chrome y Suika)

- **Objeto y sitio**: **el primer teléfono** del Reino de la Ciencia, en
  la nieve, con **el cable tendido** desde la aldea hasta el almacén
  (1×24, 00:03:21: «Si tendemos el cable, funciona como teléfono»). Una
  caja de madera con **el interruptor de llamada que se gira**, los tubos
  de vacío asomando y **el megáfono-micrófono** en la mano de Chrome.
  En Blender: caja, interruptor, cable sobre postes, nieve.
- **Personaje**: **Chrome**, gritando al micro (1×24, 00:04:34), con
  **las dos manos en el megáfono**. **Suika**, a su lado, con **el dedo en
  el interruptor** (00:04:21). Al fondo, desenfocados, Kaseki y Kohaku.
- **Cómo habla**: los textos van **en etiquetas de papel atadas al
  cable**, como las piezas de la cadena «¡…, listo!» (1×23, 00:21:04).
  Chrome grita en Bangers, en un papel pegado a la caja: **«¡Qué
  malote!»**.
- **Dónde va cada texto**:
  - Tallado en la tapa de la caja, con Rubik Dirt: **Hardware**.
  - Etiquetas en el cable, con Kalam, una tras otra: **Micros,
    interfaces, auriculares y cámaras** / **Con el precio delante** /
    **Un hilo por cacharro**.
  - Lo que «dice» Chrome al micro, en un papel grande: **Si lo tienes, di
    cómo te fue de verdad**. Es su momento: probó el aparato y lo contó.
  - Etiqueta del megáfono, con Oswald: **Ejemplo: Fifine K669, unos 35
    USD**.
- **Para que no quede plano**: **el cable cruza en diagonal por delante**,
  desenfocado; copos de nieve; **el vaho** de Chrome al gritar; luz cálida
  saliendo de la puerta del almacén detrás.
- **2.ª pasada**:
  - **Otro sitio real, visto**: **la torre-vigía** con **la bocina de
    cobre** en lo alto de un árbol enorme ([1×24, 2:17](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=137)).
    El cable puede bajar de la torre a la caja de Chrome. Paleta medida:
    `#393934` `#595D5B` `#A3CAEB` `#D0E8F2` (bosque y cielo claro). Es de
    día: si se usa, la escena pasa de la noche nevada al día.
  - **La reacción**: **Ruri** asombrada en primer plano ([1×24, 4:34](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=274)),
    a quien Chrome le grita «¡La ciencia es la bomba!». Pone la cara de
    quien lee la reseña.
  - **Ropa**: todos con **abrigo de piel con ribete** (visto en 1×23 y
    1×24). Camisa de Chrome `#245E6B` asomando; poncho de Suika `#373C42`,
    casco `#B4C856`.

### ¿Cuál primero?

**A** para la lámina 1: es el objeto del plan, sale **del capítulo en que
Senku fabrica un micrófono de verdad** (1×23) y el laboratorio es el sitio
más reconocible. **B** para la lámina 2: el mostrador con precios es justo
lo que hacen las etiquetas, y lo presenta **Gen, el más querido**. C es la
alternativa si el dueño prefiere una escena exterior.

**2.ª pasada**: se mantiene el orden. A gana más con lo visto: el
laboratorio y la hoja de ruta ya tienen imagen real, y la pose del
cuentagotas es de vídeo. B mejora con las monedas Drago.

---

## 20 · Lo que no pude verificar

**2.ª pasada**: lo tachado ya se resolvió; lo demás sigue abierto.

- ~~Ninguna imagen: no hay hojas de contacto~~ → 3 hojas en `hojas/`.
- **La moneda de los rangos** (supongo USD) y **el texto del mensaje
  fijado** «Cómo se recomienda algo aquí»: siguen sin estar en el
  inventario ⚠️. Los decide el dueño.
- ~~Cómo es en pantalla la hoja de ruta y el billete de Drago~~ → vistos
  (§3.3). **El micrófono y el teléfono en primer plano**: sin arte fijo;
  sólo fotogramas de 720p (§2.5) y la página de manga `settei_01` nº256 ⚠️.
- **La frase latina** de «唆るぜ これは» ⚠️. ~~La jerga de Gen en latino~~
  → no se adaptó, habla normal (Doblaje Wiki, una fuente).
- ~~Estudio y directores~~ → ✅ ficha de Doblaje Wiki. ~~Tsukasa~~ → ✅.
  Voces latinas de **Minami**, **Nikki**, **Byakuya** y **Lillian**: la
  propia Doblaje Wiki no las identifica ⚠️. Los secundarios de §10.1,
  una fuente ⚠️.
- **Anécdota** del «10 millones por ciento»: sólo Doblaje Wiki ⚠️.
- **Doblaje de la 3.ª parte de *Science Future***: Doblaje Wiki dice 93
  episodios hasta 2026 y el cambio de Gen «en la tercera parte», pero no
  se confirmó con Crunchyroll ⚠️.
- Los puestos 3.º a 5.º de la **encuesta de 2023** y la de **Dengeki
  (2026)** ⚠️.
- ~~Los endings de *New World* 2 y los temas de *Science Future*~~ → ✅.
  **El nombre de la pista** del montaje de fabricación ⚠️.
- ~~La caja de diálogo de *Battle Craft*~~ → vista y medida.
- ~~Colores sin medir~~ → medidos (§5.2, §16). **Falta**: la ropa de Gen
  con luz neutra y el exterior nevado de la aldea ⚠️.
- ~~Licencias de Sketchfab~~ → CC BY por la API. El megáfono, «Free
  Standard» ⚠️.
- **Los minutos de YouTube y TikTok** ⚠️: YouTube pide iniciar sesión.
  Los tráileres se vieron en Dailymotion (§12).
- **Frases latinas textuales de clips oficiales con minuto** ⚠️: los clips
  de Crunchyroll en YouTube no se pudieron bajar. Hay una muestra de audio
  de Gen sin episodio (§10.3).
- **Poses de Gen y Kaseki en vídeo** ⚠️: sus episodios no estaban sueltos.
- **Bandera del Reino de la Ciencia** en imagen oficial ⚠️.
- **Vistas** de los fandubs y covers ⚠️ (sólo título y canal).
---

## Cumplimiento del encargo

Estado tras la 2.ª pasada. ✅ hecho · ⚠️ a medias · ❌ no hecho.

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | Key visuals medidos (22 en la wiki), portadas de tomos y de Jump, fanbook, hojas de ruta, monedas Drago, tarjetas del videojuego, Nendoroid (§3, `arte_01`). Falta arte fijo del micro y del teléfono: no existe en la wiki |
| 2 · Fotogramas de escenas icónicas | ⚠️ | 10 escenas miradas con capítulo, minuto y enlace (§2.5) y 30 con minuto de subtítulo (§2.1-2.4). Pero en **720p** (fansub de Internet Archive); sólo el opening está en 1080p. YouTube pide iniciar sesión |
| 3 · Fan art y 3D con licencia | ✅ | 5 modelos de la serie y 3 de objetos con licencia CC BY leída en la API de Sketchfab; fan art con autor; cosplay mirado (§4) |
| 4 · Sitios, luz, paleta y texturas | ✅ | 9 sitios con hex medidos en fotogramas (§5.2); texturas CC0 de Poly Haven y ambientCG. Sin medir: el exterior nevado |
| 5 · Tipografía, una letra por uso | ✅ | Cartel del título medido; 13 letras libres con tildes, ñ, ¿ y ¡ comprobadas con fontTools; tabla por uso (§6.3). La letra del juego y de los créditos no se identificó (propuesta marcada) |
| 6 · Cómo hablan en pantalla | ✅ | Hoja de ruta vista, «¡…, listo!», Mecha Senku, test de Gen, caja de *Battle Craft* medida (§7) |
| 7 · Personajes y popularidad | ✅ | 4 encuestas de Jump, VIZ, Nijimen, AniList, MAL, premio de Crunchyroll (§8, §9). Falta Dengeki 2026 |
| 8 · Doblaje latino y frases | ⚠️ | Reparto principal con dos fuentes, estudio y 4 directores por la API de Doblaje Wiki (§10). Frases latinas: «10 mil millones por ciento» y «¡Qué malote!» ✅; otras, una fuente; **ninguna frase textual de clip oficial con minuto** (YouTube bloqueado). Secundarios, una fuente |
| 9 · Música y sonido | ✅ | Todos los openings y endings de las 4 temporadas con dos fuentes; «One Small Step»; compositores; acuarela del ending (§11). Falta el nombre de la pista del montaje |
| 10 · Vídeos con minuto | ⚠️ | 5 tráileres y el OP1 mirados con minuto (§12). Análisis de YouTube y tendencias de TikTok **sin ver** (bloqueo) |
| 11 · Videojuegos | ✅ | *Battle Craft*: fechas, cierre, caja de diálogo, victoria y HUD medidos; *Jump Force* confirmado sin la serie (§13) |
| 12 · Lo que ama el fandom y qué no hacer | ✅ | Memes, gags, identificación de fans con fuente; lista de qué no hacer ampliada con colores y trivia (§14) |
| 13 · Descripción profunda de cada personaje | ⚠️ | Carácter, historia, forma de hablar, trivia y voces medidas (§8). **Cara en cada emoción con fotograma**: sólo alegría, sorpresa, concentración y asombro (Senku, Suika, Kohaku, Ruri); de Gen y Kaseki, ninguna en vídeo |
| 14 · Poses analizadas con minuto | ⚠️ | 36 poses con minuto de subtítulo y 11 vistas de verdad (§15). Senku, completo; **Gen y Kaseki sin fotograma** (sus episodios no estaban sueltos) |
| 15 · Vestuario con hex | ⚠️ | Hex medidos de Senku, Chrome, Suika y Kaseki (§16). **Gen sin medir**: sus imágenes tienen luz de color; en las hojas, a ojo, túnica lila |
| 16 · Paisajes y fondos de pantalla | ✅ | 2 fondos 4K medidos con Pillow y 7 de Wallhaven con tamaño y autor (§17.2) |
| 17 · Guía para IA de imagen y de texto | ✅ | Rasgos, paleta medida, estilo medido, palabras que ayudan y que estropean, vocabulario de expresiones, voz de cada personaje y frases reales por emoción (§18). Gotas de sudor y fondos de emoción no documentados |
| 18 · Técnica y cómo replicarla | ✅ | Boichi y TMS con entrevistas, sombreado y línea medidos, Photoshop y Blender paso a paso, encuadres (§18.1). Filtros de posproducción sin fuente |
| 19 · Texturas 2D | ✅ | Trama, rayas, rayado, papel, cuerda con licencia; emblema y moneda (§18.2). Bandera oficial sin imagen |
| 20 · Gustos y detalles | ✅ | 10 personajes con cumpleaños, altura, gustos, objeto y cómo se ven (§18.3) |
| 21 · Por qué la aman | ⚠️ | Números (MAL, ventas, premio), identificación y 7 escenas que hacen llorar con reacción de Reddit (§18.4). **Tres sin minuto** y sin describir música ni encuadre |
| 22 · Fan dubs y comunidad hispana | ⚠️ | 4 fandubs y 5 covers con canal y enlace (§18.5). **Sin vistas ni fecha** (YouTube sólo deja `oembed`); sin parodia larga |
| 23 · Colaboraciones y cruces | ✅ | 5 cafés, Lawson, 2 museos, 2 figuras, cosplay (§18.6). Cruces con gachas: no encontrados |
| 24 · Obras parecidas | ✅ | AniList, webs de recomendación, CBR, influencias de Inagaki, TV Tropes y las láminas del servidor (§18.7) |
| 25 · El mundo y sus símbolos | ✅ | Reglas en cinco líneas, sagas con capítulos, momentos clave, emblemas y vocabulario (§18.8) |
| Tres conceptos de lámina | ✅ | A, B y C con objeto, sitio, personaje, pose vista, letra, textos y profundidad (§19), actualizados con lo visto |
| 40 fuentes distintas | ✅ | Más de 90 webs distintas enlazadas |
| Oficiales | ✅ | dr-stone.jp (1.ª pasada), TMS, X oficial, Shueisha, Good Smile, Google Play, entrevistas de Matsushita y Boichi |
| Otros idiomas | ✅ | Japonés, inglés, chino, coreano (1.ª pasada) y francés |
| Wikis, TV Tropes, TCRF, Wayback | ⚠️ | Fandom y Doblaje Wiki por API, Wikipedia, TV Tropes ✅. TCRF bloquea y no tiene página del juego; Wayback sin copia de dr-stone.jp |
| Foros y comunidades | ✅ | Reddit por Arctic Shift, foros de dafont y befonts, X. Discords y 4chan no hicieron falta |
| Arte | ✅ | pixiv, DeviantArt, ArtStation, Wallhaven, Alpha Coders, Openverse |
| Vídeo | ⚠️ | Dailymotion e Internet Archive mirados; YouTube y TikTok bloqueados |
| Código y recursos | ✅ | GitHub (subtítulos, letras), Sketchfab, Poly Haven, ambientCG, Clip Studio Assets, MusicBrainz |
| Doblaje latino (fuentes) | ⚠️ | Doblaje Wiki por API y muestras de audio, ANMTV y prensa (1.ª pasada). Entrevista al reparto de Funianime sin ver; créditos de Crunchyroll sin abrir |
| Vídeos mirados de verdad (opening, ending, tráiler, 3 escenas) | ✅ | OP1 en 1080p, ending de 1×24, 5 tráileres, 4 episodios (§2.5) |
| Hojas de contacto | ✅ | 3 en `hojas/`, miradas, con qué número sirve (sección «Las hojas de contacto») |
| `referencias.json` | ✅ | Todas las útiles de las partes, mejores primero, con tamaños medidos donde los hay |

**Los ⚠️ del texto**: la 1.ª pasada tenía **96**. Se resolvieron unos 25
(fotos, colores, licencias, música, estudio y directores del doblaje,
Tsukasa, caja del juego). El total sube a 180 porque la 2.ª pasada
**añadió mucho dato nuevo** y marca con ⚠️ todo lo que tiene una sola
fuente (sobre todo el reparto secundario del doblaje y los cafés). Lo que
el dueño tendría que oír o ver: frases latinas con minuto, la ropa de Gen
de día y las poses de Gen y Kaseki.

---

## 21 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)

- `curl` a dr-stone.fandom.com, doblaje.fandom.com (API), api.polyhaven.com,
  sketchfab.com, dr-stone.jp, gameuidatabase.com → **000** (sin conexión).
- `curl` a AniList, MyAnimeList, Kitsu, Jikan, Shikimori, imgur,
  pbs.twimg.com, img.youtube.com, dafont.com, huggingface.co → **000**.
- WebFetch bloqueado: doblaje.fandom.com, crunchyroll.com, wdnes.com,
  anmtvla.com, anime-colors.com.
- Funcionan: raw.githubusercontent.com, api.github.com, git clone de
  GitHub y PyPI.
- Por eso **no hay `hojas/`** y no se corrió `investigar_serie.py`.

### Búsquedas web (48 hechas)

| # | Idioma | Búsqueda (dominio si lo hubo) |
|---|---|---|
| 1 | ES | Dr. Stone doblaje latino reparto Senku Alejandro Orozco Chrome Gen Asagiri Kaseki Suika |
| 2 | ES | «José Luis Piedra» Chrome «Brandon Santini» Gen «Óscar Rangel» Kaseki «Valeria Mejía» Suika |
| 3 | ES | doblaje latino estudio director Crunchyroll 2020 (depor, atomix, atamashi, tierragamer, gamerfocus, arata, versusmedia) |
| 4 | ES | Gen «Javier Olguín» «Brandon Santini» cambio de voz |
| 5 | ES | doblaje mexicano estudio «Dubbing House» OR «SDI Media» OR «Candiani»… |
| 6 | ES | «Dr. Stone» «Candiani» «Jorge García» dirección |
| 7 | ES | Science Future doblaje latino elenco staff Crunchyroll 2025 |
| 8 | ES | New World elenco latino Kaseki Suika Chrome Ukyo Ryusui (prensa) |
| 9 | ES | frases «10 mil millones por ciento» «qué malote» «emocionante» |
| 10 | ES/EN | «sosoru ze kore wa» traducción latina |
| 11 | JA | Dr.STONE キャラクター人気投票 結果 1位 |
| 12 | JA | 第4回 キャラクター人気投票 あさぎりゲン 41317票 |
| 13 | EN | official character popularity poll results history |
| 14 | JA | SCIENCE FUTURE 第3クール キービジュアル 解禁 2026 |
| 15 | JA | スタッフ インタビュー 美術 色彩設計 岩佐裕子 |
| 16 | EN | all opening ending songs list |
| 17 | JA | 歴代 主題歌 一覧 OP ED |
| 18 | EN | New World opening/ending; Stone Wars ending «Koe» |
| 19 | JA | バトルクラフト アプリ 画面 サービス終了 |
| 20 | EN | «Battle Craft» OR «Jump Assemble» OR «Jump Force» |
| 21 | EN | logo font typeface similar free font |
| 22 | EN | Senku «roadmap» anime graphic «Mecha Senku» |
| 23 | EN | «Mecha Senku» robot explainer |
| 24 | EN | Senku 3D model (sketchfab.com) |
| 25 | EN | vacuum tube, megaphone, crystal radio, old microphone (sketchfab.com) |
| 26 | EN | bellows camera, crank telephone, chemistry glassware (sketchfab.com) |
| 27 | EN | rough wood planks bark CC0 (polyhaven.com) |
| 28 | EN | Senku color palette hex codes |
| 29 | JA | 公式ファンブック 科学王国民 Boichi 画集 |
| 30 | EN | memes «ten billion percent» «get excited» Kaseki shirt |
| 31 | JA | カセキ 服が弾ける ゲン 業界用語 ジーマー 意味 |
| 32 | EN/ES | Lillian Weinberg «One Small Step» cantante, doblaje latino |
| 33 | JA | 公式 PV 本PV 第1弾 (youtube.com) |
| 34 | ES | clip doblaje latino Senku celular micrófono (youtube.com) |
| 35 | ZH | 石纪元 千空 做手机 麦克风 名场面 浅雾幻 人气 哔哩哔哩 |
| 36 | KO | 닥터 스톤 센쿠 명대사 «100억 퍼센트» 겐 인기 투표 |
| 37 | EN | wallpaper 4K 3840x2160 (alphacoders, wallpapercave, wallhaven…) |
| 38 | JA | 千空 ゲン クロム イラスト 科学王国 (pixiv.net) |
| 39 | ES | «qué malote» Chrome «yabe» José Luis Piedra |
| 40 | EN | Rochelle salt microphone real science piezoelectric |
| 41 | EN | Senku cell phone design, episodes 23-24 review |
| 42 | JA | 背景美術 石神村 ラボ 美術設定 吉原俊一郎 |
| 43 | EN/ES | TikTok «10 mil millones» «ten billion percent» (tiktok.com) |
| 44 | EN | Senku outfit season 1, New World, Science Future |
| 45 | ES | Science Future parte 3 doblaje latino 2026 |
| 46 | EN | Suika helmet glasses; Kaseki clothes burst; Chrome profile |
| 47 | EN | Boichi art style panels diagrams lettering |
| 48 | ES | «Reino de la Ciencia» Senku «esto me emociona» |

### GitHub (sin cupo)

- [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror):
  bajé **los 95 subtítulos japoneses de Netflix** (con acotaciones) de
  todas las temporadas: T1 (24), *Stone Wars* (11), especial *Ryusui* (1),
  *New World* (22) y *Science Future* (37). Los busqué con grep (マイク,
  スピーカー, レコード, 真空管, 声マネ, ドラゴ, カメラ, ロードマップ,
  メカ千空…). Están en mi carpeta temporal, **no en el repositorio**.
- [google/fonts](https://github.com/google/fonts): 21 letras, comprobadas
  con fontTools.

### Fuentes consultadas por tipo

- **Oficiales**: dr-stone.jp (noticias, staff, personajes), X oficial
  (@DrSTONE_off), Shueisha / S-MANGA (fanbook), WebNewtype (hojas de
  modelo), YouTube oficial (PV, «科学部 千空's ラボ»), Crunchyroll
  (anuncio de doblaje), 4Gamer, gamebiz, Dengeki (juego), Natalie, SPICE,
  Animate Times, Nikkei xTrend, GetNews, J:magazine (entrevista al
  director Shūhei Matsushita).
- **Otros idiomas**: japonés (arriba, más みんなのランキング, Nijimen,
  ciatr, Yahoo! Chiebukuro), chino (萌娘百科, Zhihu, Baidu), coreano
  (Namu Wiki).
- **Wikis**: Fandom de Dr. Stone (vistas en resultados), Doblaje Wiki
  (resúmenes), Wikipedia. TV Tropes salió en un resultado; no lo abrí.
- **Foros y comunidades**: foro de dafont, Tumblr, X de fans. Reddit y
  Arctic Shift: bloqueados.
- **Arte**: pixiv, DeviantArt, ArtStation, Alpha Coders.
- **Vídeo**: YouTube, TikTok.
- **Código y recursos**: GitHub, Sketchfab, Poly Haven.
- **Doblaje latino**: Doblaje Wiki, ANMTV, Depor, Atomix, Atamashi,
  Gamerfocus, TierraGamer, Arata, Versus Media, wdnes, TVLaint,
  Bubbleblabber, TikTok de Brandon Santini.
- **Ciencia**: Britannica (sal de Rochelle), rimstar.org, OneTubeRadio.

### Lo que NO encontré

- Imágenes: nada descargado; sin hojas de contacto.
- La frase latina de «唆るぜ これは» y la jerga de Gen en latino.
- El aspecto de la hoja de ruta, del teléfono y del billete de Drago.
- La caja de diálogo de *Battle Craft*. The Cutting Room Floor: no lo
  busqué (un juego de móvil cerrado rara vez está). Wayback Machine:
  bloqueada.
- Los colores medidos de cada personaje.
- Una escena de **tratamiento acústico**: no la encontré en los
  subtítulos de toda la serie (lo más cercano es el oído de Ukyo).
- Reddit, Arctic Shift, TV Tropes y Doblaje Wiki: bloqueados.

### Segunda pasada (24-sep-2026, red abierta)

Método de equipo (`EQUIPO.md`): el recolector gratuito y cuatro
investigadores. Sus bitácoras completas están en `partes/*.md`. Resumen:

**Recolector** (`herramientas/recolectar.py --hojas`): AniList (ficha,
personajes, favoritos, staff, recomendaciones), Doblaje Wiki (ficha y
datos de interés), Fandom (imágenes y textos de 5 personajes), Danbooru y
Safebooru, Wallhaven (fondos con tamaño), Sketchfab, Openverse (cosplay),
Dailymotion, Internet Archive, MusicBrainz (6 bandas sonoras), Steam y
Reddit. Hojas de contacto: 449 imágenes, 8 hojas.

**Imagen**: API de Fandom (`list=search`, `categorymembers` de Key
Visuals: 22; `imageinfo` de 15 imágenes); API de Sketchfab (9 modelos, uno
a uno); API de ambientCG (rope, linen, paper); curl a blu-ray.com,
goodsmile.info, Google Play, Alpha Coders (bajando y midiendo con Pillow).
9 búsquedas web en inglés y japonés: cafés colaborativos, Lawson, figuras,
logo del Reino de la Ciencia, screentone libre, Blu-ray, *Battle Craft*,
cuenta atrás. `estilo.py` en 11 imágenes; 15 imágenes miradas con Read.

**Vídeo**: `fotogramas.py` en 11 vídeos (unos 90 fotogramas en hojas y 14
en grande); `estilo.py` en 8 paletas. Dailymotion (español «Dr Stone
opening», «capitulo 1 español»; francés «Bande Annonce»), Internet Archive
(`advancedsearch` de episodios, Ryusui y endings). Web: japonés «Dr Stone
アニメ 2期 エンディング 夢のような 佐伯ユウスケ», «Science Future
オープニング エンディング 主題歌»; inglés «New World part 2 ending
theme», «Suki ni Shinayo Anly», «Where Do We Go? OKAMOTO'S». Descartado un
vídeo mal titulado (era otra serie, comprobado mirándolo).

**Voz**: API de Doblaje Wiki (wikitext de la serie, 32.300 caracteres, y
páginas de Alejandro Orozco, Brandon Santini y Óscar Rangel); API de
Fandom (trivia de 8 personajes); Jikan (MAL); Arctic Shift (r/DrStone:
llorar, identificarse, favoritos); `oembed` de YouTube (8 fandubs y
covers). Web: español «Dr Stone fandub español latino», «opening cover
español latino», «meme 10 mil millones por ciento tiktok»; inglés «manga
sales million copies», «Crunchyroll Anime Awards», «Senku Best
Protagonist 2020», «why fans love reddit». `voz.py` en 2 muestras.

**Texto, juegos y técnica**: inglés «Boichi Dr. Stone art style
interview», «TMS animation technique interview», «Riichiro Inagaki
influences», «Kingdom of Science flag emblem», «Battle Craft gameplay
dialogue box», «episode title card font», «compared to Cells at Work»,
«TV Tropes Dr Stone», «site:tcrf.net Dr. Stone», «Jump Assemble OR Jump
Force roster», «chromatic aberration OR film grain»; japonés «ボイチ
Dr.STONE 作画 CG 3D インタビュー», «ドクターストーン アニメ 背景美術 セルルック
撮影», «Dr. Stone 新作 ゲーム 2026 後継». Ficha de TMS, Google Play
(capturas de *Battle Craft*), `estilo.py` en el cartel del ep. 1 y en la
caja de diálogo. Revisión de los encargos de `encargos/` (obras del
servidor que se parecen).

**Redactor**: miró las 3 hojas de `hojas/` (números en «Las hojas de
contacto») y juntó `referencias.json`.

**Fuentes nuevas de la 2.ª pasada, por tipo**

- **Oficiales**: ficha de TMS Entertainment, TMS USA (X), Google Play y
  App Store (*Battle Craft*), Good Smile Company, entrevista a Matsushita
  (J:COM), X de Boichi, Animate Times, SPICE, BARKS, Apple Music.
- **Otros idiomas**: japonés (collabo-cafe, Togetter, animatetimes,
  anime-song-info), francés (tráileres con subtítulos de Crunchyroll FR).
- **Wikis**: Fandom por su API, Doblaje Wiki por su API, Wikipedia, TV
  Tropes. **The Cutting Room Floor**: bloquea a los robots; no hay página
  del juego (no la encontré). **Wayback Machine**: sin copia de
  dr-stone.jp/character/.
- **Foros**: Reddit por Arctic Shift, befonts, hilos de X.
- **Arte**: DeviantArt, Wallhaven, Alpha Coders, Openverse/Flickr.
- **Vídeo**: Dailymotion, Internet Archive, YouTube (sólo `oembed`),
  TikTok (sólo la etiqueta).
- **Código y recursos**: Sketchfab (API), ambientCG, Poly Haven, Clip
  Studio Assets, MusicBrainz.
- **Doblaje latino**: Doblaje Wiki (API y muestras de audio), canales de
  fandub en YouTube.
- **Prensa**: ANN, Anime Corner, CBR, The Fandom Post, Essential Japan,
  Have a Good Holiday, SLJ, Dualshockers.

**Lo que NO se encontró en la 2.ª pasada**: el micrófono y el teléfono en
arte fijo; la bandera oficial del Reino de la Ciencia; cruces con gachas;
vistas de fandubs; minutos de YouTube y TikTok; frases latinas textuales de
clips oficiales con minuto; poses de Gen y Kaseki en vídeo; el nombre de
la pista del montaje; filtros de posproducción; el sucesor de *Battle
Craft*; la parodia hispana larga; la categoría de la nominación de Suika;
la encuesta de Dengeki 2026.
