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
- `referencias.json`: de 35 a **todas las útiles de las partes**, con
  tamaños medidos, las mejores primero.

**Los ⚠️**: había **96**; el recuento final está al pie de la tabla de
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
| Otra de *Stone Wars* | [imagen, 1830×2529](https://static.wikia.nocookie.net/dr-stone/images/1/1e/Dr._Stone_Stone_Wars_Key_Visual_1.png) | Senku con el puño. Hoja `arte_01` nº14 ⚠️ (el número de la wiki no confirmado) |
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
| **La hoja de ruta** (ロードマップ) | La primera, hacia la medicina: «これは万能薬へ向かう科学のロードマップだ» (1×08, 00:03:26; el subtítulo va arriba, sobre el dibujo). La del móvil: 1×19, 00:21:25 y 1×21, 00:13:00. La del cohete: 4×24, 00:21:32 | ✅ existe; el aspecto ⚠️ |
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
| **Senku** | Rudo y rápido, habla «de chico de barrio» (テメー, ブチ〜, アホほど). **Exagera con 100億** (diez mil millones): «100億％», «100億倍». Se ríe **«ククク»** (343 veces en la serie). Explica con recetas cortas: «足し算引き算» | 1×23, 00:15:40: «La química es sumar y restar» |
| **Chrome** | Chico de aldea, entusiasta. Dice **«ヤベえ»** (¡qué fuerte!, ¡qué pasada!) sin parar (la palabra sale 185 veces en la serie, en boca de varios). Grita **«しゃあ!»** al ganar | 1×24, 00:04:34: «¿Lo ves, Ruri? ¡La ciencia es la bomba!» |
| **Gen** | Habla con **jerga al revés de la tele japonesa** (倒語): **ジーマー** (maji, «en serio»), **バイヤー** (yabai, «qué fuerte»), **ドイヒー** (hidoi, «qué crueldad»), **ゴイスー** (sugoi, «increíble»), **リームー** (muri, «imposible»). Añade «〜ちゃん» a todos («千空ちゃん») ✅ ([Yahoo! Chiebukuro](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q10319251340), [pixiv 業界用語](https://dic.pixiv.net/a/%E6%A5%AD%E7%95%8C%E7%94%A8%E8%AA%9E)) | 1×23, 00:19:15: «ドイヒ～» (¡qué crueldad!) al saber que son 800 pilas |
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

Ver §13. De su caja de diálogo **no encontré capturas** ⚠️.

### 7.5 Qué NO hacer con el texto

- Una **burbuja blanca redonda** flotando.
- Letra de ordenador limpia y fría para lo que escribe Senku: en la serie
  **todo está hecho a mano**.
- Escribir **«10 millones por ciento»**: es «**10 mil millones**». El
  actor latino lo grabó mal una vez y hubo que regrabar (§10).
- Poner la jerga de Gen en japonés sin traducir: el doblaje latino la
  cambia (no encontré cómo ⚠️).
- Rayas «—», «·» o paréntesis en los textos (regla del dueño).

---
## 8 · Los personajes

Lo que está en el subtítulo va con su minuto ✅. El aspecto físico y los
gestos que no salen en el texto son **de memoria** ⚠️.

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
- **Voz**: latino **Brandon Santini** ✅ (§10).

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

### Los secundarios que conviene tener a mano

| Personaje | Por qué sirve aquí | Voz latina |
|---|---|---|
| **Ukyo Saionji** (西園寺羽京), 4.º en votos (2021) | Fue **sonarista**; su oído lo oye todo (3×04, 00:07:57). **El de los auriculares** | Eduardo Garza ✅ |
| **Minami Hokutozai** (北東西南) | Periodista. Llora con **su cámara** nueva (3×02, 00:18:12). **La de la cámara** | ⚠️ no la busqué |
| **Ryusui Nanami** (七海龍水), 3.º en votos (2021) | Rico, lo quiere todo, emite **el Drago**, **compra lo más caro** (especial, 00:35:51). **El de «Más de 400»** | Óscar Flores ✅ |
| **Kohaku** (コハク), 2.ª en 2018 | Hace el micrófono con Kinro y Ginro; dice «**¡Micrófono, listo!**» (1×23, 00:21:16) | Alicia Barragán ✅ |
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

**Conclusión**: **Gen es el más querido** desde 2021 y gana en todas las
franjas de edad en 2023. **Senku** es la cara de la serie. Para #hardware
funcionan los dos: **Senku fabrica**, **Gen vende y explica los precios**.
Kaseki y Suika son muy reconocibles pero no están arriba en votos.

---

## 10 · Doblaje latino

> [!note] Doblaje Wiki no se abre desde aquí
> Ni su API (`action=parse`) ni la web. Cada nombre lo di por bueno cuando
> salió en **dos búsquedas distintas**: una abierta (que incluye Doblaje
> Wiki, Atamashi, Depor y Atomix) y otra limitada a prensa (Depor,
> Gamerfocus, TierraGamer, Arata, Versus Media). Antes de rotular,
> conviene abrir Doblaje Wiki una vez.

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
| **Tsukasa** | Arturo Cataño | ⚠️ una búsqueda |

### 10.2 Estudio, dirección y dónde se ve

- **Estudio**: **Audiomaster Candiani** (México) ⚠️ (lo dicen los
  resúmenes de ANMTV y Doblaje Wiki; no pude abrir ninguno).
- **Dirección**: **Bardo Miranda** en la temporada 1 y **Jorge García**
  desde la 2 hasta la primera parte de *New World* ⚠️ (una búsqueda).
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
| Gen | Su jerga al revés (ジーマー…) en latino | **No lo encontré** ⚠️ |

---

## 11 · Música

| Temporada | Opening | Ending | Estado |
|---|---|---|---|
| T1, 1.ª parte (2019) | «Good Morning World!», **BURNOUT SYNDROMES** | «LIFE», **Rude-α** | ✅ |
| T1, 2.ª parte | «三原色» (Sangenshoku), **PELICAN FANCLUB** | «夢のような», 佐伯ユウスケ | OP ✅, ED ⚠️ |
| *Stone Wars* (2021) | «楽園» (Rakuen), **Fujifabric** | «声？» (Koe?), **Hatena** | ✅ ([ANN](https://www.animenewsnetwork.com/news/2020-11-15/fujifabric-hatena-perform-theme-songs-for-dr-stone-stone-wars-anime/.166333)) |
| *New World*, 1.ª parte (2023) | «ワスレガタキ» (Wasuregataki), **Huwie Ishizaki** | «Where Do We Go?», OKAMOTO'S | OP ✅ ([vídeo oficial](https://www.youtube.com/watch?v=81H41vp96ag)), ED ⚠️ |
| *New World*, 2.ª parte | «Haruka», Ryujin Kiyoshi | ⚠️ | ⚠️ ([ANN](https://www.animenewsnetwork.com/news/2023-08-26/dr-stone-new-world-anime-2nd-part-reveals-october-12-debut-theme-song-artists/.201655)) |
| *Science Future* | 1.ª y 2.ª parte: sólo resúmenes contradictorios; 3.ª parte: [Animate Times](https://animatetimes.com/news/details.php?id=1775134655) | — | ⚠️ |

**La canción que importa para un servidor de canto**: «**One Small Step**»,
la que canta **Lillian Weinberg** en el disco de Byakuya (1×24, 00:15:53).
La canta **Laura Pitt-Pulford**, con letra de Kanata Okajima y JAKAZ y
música de **Hiroaki Tsutsumi** ✅ ([Fandom](https://dr-stone.fandom.com/wiki/One_Small_Step), [UtaTime](https://www.utatime.com/global/lyrics/lillian-weinberg-song-performed-by-laura-pitt-pulford/one-small-step/)).
En la serie, al oírla, alguien dice «Es demasiado bonita» (1×24, 00:17:54,
suena a Suika) y otro «Senku, ¿antes había tanta música así de buena?»
(00:18:20, suena a Chrome). El texto ✅; quién lo dice ⚠️ (el subtítulo
no lo marca).

**Ambiente** ⚠️: la banda sonora (Tatsuya Kato, Hiroaki Tsutsumi y Yuki
Kanesaka, de memoria) mezcla orquesta épica para los inventos con temas
cómicos. El «**tema de la fabricación**» que suena en los montajes (1×23,
00:20:03 a 00:21:04, justo antes del «¡listo!») es el que todo fan
reconoce.

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

**Los minutos exactos** de estos vídeos **no los pude ver** (YouTube y
TikTok no se abren) ⚠️. Los minutos buenos son los del episodio (§2).

---

## 13 · Videojuegos de la franquicia

### Dr.STONE バトルクラフト (*Battle Craft*), móvil

- **Popping Games Japan**. Salió en Japón el **1 de septiembre de 2021** y
  en Norteamérica el 28 de noviembre de 2023 ⚠️. **Cerró el 1 de
  septiembre de 2026, a las 10:00**, a los cinco años ✅
  ([4Gamer](https://www.4gamer.net/games/544/G054403/20260707006/),
  [gamebiz](https://gamebiz.jp/news/429025),
  [Dengeki](https://dengekionline.com/article/202607/82597)).
- **Cómo es**: juntas materiales, **fabricas objetos** y los llevas a la
  batalla; la historia del anime se revive **en formato aventura**, con
  voces ✅ (resúmenes de 4Gamer y de las tiendas).
- **Su caja de diálogo**: no encontré capturas ⚠️. Fichas de tienda donde
  quizá se vean: [Google Play](https://play.google.com/store/apps/details?id=com.poppingames.dsbc&hl=en_US),
  [App Store](https://apps.apple.com/us/app/dr-stone-battle-craft/id1513882973),
  [QooApp](https://m-apps.qoo-app.com/en_us/app/16172), [web oficial](https://dsbc.poppin-games.com/).
- **Para la lámina**: la idea de **combinar materiales en un árbol de
  fabricación** es la misma de la hoja de ruta. Refuerza el concepto A.

**Jump Force / Jump Assemble**: no encontré a Dr. Stone en ellos ⚠️.

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

### 14.2 Qué NO hacer (lo que un fan notaría)

- **Un smartphone o un micrófono moderno** en manos de Senku. Él mismo lo
  dice: «**No es *smart*, sólo *phone***» (1×19, 00:21:07). El Fifine va
  **sólo escrito en una etiqueta**, nunca dibujado.
- **Un laboratorio blanco y limpio**, con neones o pantallas. El
  laboratorio es **una cabaña de madera** con vidrio soplado a mano.
- **Plástico brillante de colores**: la primera plástica (fenolita,
  1×23, 00:16:02) sale **marrón oscuro y mate** ⚠️ (dato químico real; en
  el anime compruébalo).
- **Senku sonriendo dulce** o haciendo el «corazón» con las manos. Su
  sonrisa es **de medio lado, con dientes**, y su risa es «ククク» ⚠️.
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
postura la describo de memoria** ⚠️: saca el fotograma de ese minuto y
compruébalo antes de calcarla.

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
| **Senku** (T1) | Túnica de **piel** clara con mangas cortas acampanadas, **cuello levantado**, bajo en picos hasta la rodilla y una costura que baja zigzagueando. **Cinturón con bolsas de cuero**. Zapatos de saco de cuero atados al tobillo. Lleva **E=mc²** escrito en el pecho | ✅ una fuente ([Fandom](https://dr-stone.fandom.com/wiki/Senku_Ishigami)); el color ⚠️ |
| **Senku** (antes de la piedra) | Uniforme escolar y **bata de laboratorio** encima | ⚠️ una fuente |
| **Senku** (*New World*) | Ropa moderna cosida por Yuzuriha para la sesión de fotos de Minami | ⚠️ una fuente |
| **Senku** (*Science Future*) | **Capa roja** que le da Suika al revivirlo en Sudamérica | ⚠️ una fuente |
| **Senku**, rasgos fijos | Pelo de punta, **blanco con puntas verdes**, **ojos rojos**, **marcas de petrificación** que suben desde las cejas | ✅ (Fandom y la ficha de Mecha Senku) |
| **Suika** | **Casco de sandía** con agujeros; después, **gafas** | ✅ |
| **Kaseki** | Ropa de aldea; al emocionarse, **sin camisa**, con la cuerda de la aldea al cuello | ✅ |
| **Gen** | Pelo **negro y blanco**, ropa oscura larga de mago | ⚠️ |
| **Chrome** | Ropa de aldea, bolsas de minerales | ⚠️ |

**Lo icónico**: Senku con **la túnica clara de la temporada 1**. Es la que
reconoce todo el mundo.

---

## 17 · Paisajes y fondos de pantalla

### 17.1 Los sitios, con su luz ⚠️

- **La aldea Ishigami en invierno** (1×23-1×24): nieve, cielo blanco,
  brasas dentro de las casas. Es **cuando se fabrica el micrófono**.
- **El laboratorio**: interior de madera, fuego y vidrio. Luz cálida.
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

---

## 18 · Guía para generar con IA (Firefly, Canva)

Úsala **sólo para fondos, objetos y ambientes**. Los personajes se
recortan de fotogramas reales por `v3/integrar.py`.

**Rasgos que nunca cambian**
- Senku: pelo de punta hacia arriba, **blanco con puntas verdes**, **ojos
  rojos**, **grietas que suben desde las cejas**, túnica clara de piel con
  cuello alto y cinturón con bolsas.
- Suika: casco de sandía **o** gafas redondas. Kaseki: viejo pequeño de
  cejas y barba blancas; músculos sólo si se emociona ⚠️.
- **Todo está hecho a mano**: madera, piedra, cuerda, vidrio con burbujas,
  cobre martillado.

**Estilo**
- Anime de TV (TMS Entertainment), **línea fina y limpia**, **sombreado de
  dos tonos**, colores naturales y cálidos. Fondos pintados, con textura.
- Luz: **fuego de horno** naranja por un lado y **luz fría de invierno**
  por la ventana.

**Palabras que ayudan**
> primitive wooden workshop, stone age laboratory, hand-blown glass
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

**Imágenes de referencia** (cuando se puedan abrir): el visual de
*Science Future* 3 (§3.1) para el estilo; las **hojas de modelo** de
WebNewtype para las proporciones; el modelo de **Jerry Teng** en
Sketchfab para el volumen del laboratorio y del teléfono; y los
fotogramas de 1×23 (00:19:43 a 00:21:32) para el micro.

---
## 19 · Tres conceptos para la lámina de #hardware

Los tres usan los textos de §0. Las frases «en la voz de la serie» son
**traducción mía del japonés** (con su minuto); las latinas comprobadas son
sólo «¡Qué malote!» y «10 mil millones por ciento». Recortes siempre por
`v3/integrar.py` y comprobados a 1:1. **Ninguna mano sin apoyo**: cada
personaje toca algo visible.

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

### ¿Cuál primero?

**A** para la lámina 1: es el objeto del plan, sale **del capítulo en que
Senku fabrica un micrófono de verdad** (1×23) y el laboratorio es el sitio
más reconocible. **B** para la lámina 2: el mostrador con precios es justo
lo que hacen las etiquetas, y lo presenta **Gen, el más querido**. C es la
alternativa si el dueño prefiere una escena exterior.

---

## 20 · Lo que no pude verificar

- **Ninguna imagen**: no hay hojas de contacto. Todo lo visual va ⚠️.
- **La moneda de los rangos** (supongo USD) y **el texto del mensaje
  fijado** «Cómo se recomienda algo aquí».
- **Cómo es en pantalla** la hoja de ruta, el micrófono, el teléfono y el
  billete de Drago.
- **La frase latina** de «唆るぜ これは» y cómo tradujo el doblaje la
  jerga de Gen.
- **Director del doblaje** (Bardo Miranda / Jorge García) y **estudio**
  (Audiomaster Candiani): una sola búsqueda cada uno. **Tsukasa** (Arturo
  Cataño): una sola fuente. Voces latinas de **Minami**, **Nikki** y
  **Lillian**: no las busqué.
- **Anécdota** del «10 millones por ciento»: sólo Doblaje Wiki.
- **Doblaje de la 3.ª parte de *Science Future***.
- Los puestos 3.º a 5.º de la **encuesta de 2023**.
- **Los endings** de *New World* 2 y los temas de *Science Future*.
- **La caja de diálogo** de *Battle Craft*.
- **Colores**: todos los hex son propuesta, sin medir.
- **Licencias exactas** de los modelos de Sketchfab.
- **Los minutos** de los vídeos de YouTube y TikTok.

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
- Una escena de **tratamiento acústico**: no existe en la serie (lo más
  cercano es el oído de Ukyo).
- Reddit, Arctic Shift, TV Tropes y Doblaje Wiki: bloqueados.
