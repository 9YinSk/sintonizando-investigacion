---
tags: [biblia, serie, laminas, por-decidir]
serie: "Por decidir: seis canales sin serie (y las salas de voz)"
canal: "#destacados, #eventos, #noticias-anime, #noticias-gaming, #general-doblaje, #canto + salas de voz"
fecha: 2026-09-24
---

# Biblia · Seis canales sin serie — qué serie va en cada uno

> [!important] Cómo se hizo, y sus límites
> - Este encargo es **distinto** a los demás. No es una serie: son **seis
>   canales** (y ocho salas de voz) que no tenían serie. Aquí propongo **una
>   serie por canal**, y de cada una doy **lo esencial**: personaje, cuadro de
>   diálogo, letra, fondo, doblaje latino y 2-3 conceptos de lámina.
> - **No es una biblia completa de cada serie.** Cada una merece luego su
>   propio encargo. Al final (§9) dejo lo que falta.
> - **Primera mitad**: la red estaba cerrada y trabajé con la **búsqueda
>   web** (unas 40 búsquedas en español, inglés y japonés). **Segunda
>   mitad**: la red se abrió y lo comprobé todo de nuevo con:
>   - **Doblaje Wiki por su API** (`action=parse`): las fichas de las 13
>     películas y series. Cada nombre va cruzado con prensa, ANMTV o la
>     propia wiki de la serie.
>   - `herramientas/investigar_serie.py` con **siete wikis de Fandom** (Mario,
>     Phineas y Ferb, Bleach, Wreck-It Ralph, Pixar, Sing, Los Simpson):
>     **2.809 imágenes grandes** en **62 hojas de contacto** (en
>     `herramientas/referencias/p29-*/`, que no se sube). **Las miré** y cito
>     cada imagen por su número, tamaño real y URL. En `hojas/` dejo **3
>     hojas mías**: los objetos y sitios de cada canal, los personajes, y la
>     muestra de letras. Bajé las mejores para
>     **medir los colores** con Pillow (los hex marcados ✅ salen de ahí).
>   - **Subtítulos japoneses con tiempos** de Bleach
>     ([kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror)):
>     las escenas de la revista y de Hitsugaya tienen **minuto exacto**.
>   - **API de Sketchfab** (modelos 3D con licencia), **Poly Haven**
>     (texturas CC0), **Arctic Shift** (Reddit) y **google/fonts** + fontTools
>     (tildes, ñ, ¿ ¡).
>   - **yt-dlp** para encontrar tráileres y escenas (título, canal,
>     duración). **YouTube no dejó bajar subtítulos** («confirma que no eres
>     un bot»), así que en los vídeos sólo doy la duración, no el minuto.
> - **No respondieron**: TV Tropes y The Cutting Room Floor (403, también
>   por la Wayback Machine), Wikipedia (429, demasiadas peticiones), las
>   webs de prensa por WebFetch.
> - ✅ **confirmado**: dos fuentes, o el subtítulo con su minuto, o lo vi y
>   lo medí en la imagen. ⚠️ **dudoso**: una sola fuente, o de memoria.
> - **Segunda pasada (25-sep-2026, red abierta, equipo de 4 investigadores
>   + redactor)**: YouTube seguía pidiendo «iniciar sesión», así que los
>   vídeos se miraron por **Dailymotion** con `fotogramas.py` (6 tráileres,
>   uno por serie, con minuto) y se transcribieron con **`voz.py`**
>   (Whisper) los tráileres latinos de Ralph y Sing. Se usaron además las
>   API de **Wallhaven**, **Danbooru** (`rating:g`), **Doblaje Wiki** (fichas
>   de cada actor), **Fandom** y **Wikipedia**, y Pillow para medir hex en
>   arte oficial. Se añadieron los puntos 11, 16, 18-25 de ENCARGO.md, que no
>   existían, y la tabla «Cumplimiento del encargo».

## Segunda pasada · qué cambió

**Corregido (antes → ahora)**

| Dónde | Antes | Ahora | Fuente |
|---|---|---|---|
| §3.4 Bleach | la serie de 2010 la dirigió **Salvador Delgado** ⚠️ | **No**: Delgado dirigió la tanda de **2023** (eps. 230-366, Famasound); quién dirigió 2010, no lo encontré | [su ficha en Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Salvador_Delgado) + ficha de Bleach |
| §7.2 Los Simpson | los DJ de KBBL: Agustín Sauret y Alejandro Mayén | **no hay actor fijo**: cambia por episodio (T4: Sauret y Mayén; T5: José María Iglesias o Víctor Delgado para Bill, Mario Sauret para Marty). En la lámina no se nombra a nadie | [T4](https://doblaje.fandom.com/es/wiki/Los_Simpson/4%C2%AA_temporada), [T5](https://doblaje.fandom.com/es/wiki/Los_Simpson/5%C2%AA_temporada) |
| §1.7 Mario | música de la película: **Mahito Yokota** | Yokota es **del juego**; la película es de **Brian Tyler** con Koji Kondo ⚠️ | [Wikipedia (soundtrack)](https://en.wikipedia.org/wiki/The_Super_Mario_Galaxy_Movie_(soundtrack)) |
| §3.6 Bleach | uniforme `#121212` a ojo | `#26272D` medido | arte oficial de Hisagi |
| §4.6 Ralph | Vanellope `#4FC3A1` a ojo | `#5F8C73` / `#79AA8D` medidos | arte oficial |
| §5.6 Monsters | Mike `#9BCB3C`, Sulley `#3AB4E8`, manchas `#8A4FBF`, a ojo | Mike `#5C7531`/`#87A851`, Sulley `#2C7D74`/`#559C94`, manchas `#234163`, medidos | arte de *Monsters at Work* |
| §2.6 Phineas | Doofenshmirtz «morado» `#6A3D9A` a ojo | no hay morado en su arte oficial: bata `#FFFFFD`, camisa `#020202`, pelo `#773B16` | retrato oficial |
| §3.7 Bleach | openings viejos y TYBW mezclados | tabla de openings y endings de TYBW por parte (1-4) | Wikipedia (cita ANN y Natalie) |

**Añadido**

- En cada serie, una subsección «**Segunda pasada**» con: fan art de
  referencia, fondos de pantalla con tamaño y autor (16), videojuegos y su
  interfaz (11), técnica y cómo replicarla en Photoshop y Blender (18),
  texturas 2D (19), gustos (20), por qué la aman y qué hace llorar (21), fan
  dubs hispanos (22), colaboraciones, figuras y cosplay (23), obras parecidas
  (24) y el mundo con sus símbolos (25).
- **Minutos exactos** en 6 tráileres de Dailymotion (antes sólo daba la
  duración): el volante de Sing en el 0:40, la pantalla «MM» de Phineas en el
  0:20, Ralph y Vanellope en el 2:05, etc.
- **Frases latinas textuales con minuto**: la afirmación del villano de
  Ralph (1:51-2:03) y el discurso de Buster Moon (0:29-0:38).
- **Doblaje**: 7 nombres más con dos fichas (Gerardo Vásquez, Jerry
  Velázquez, Luis Daniel Ramírez, Mario Díaz Mercado, Óscar Flores, Marcela
  Páez, Roberto Carrillo).
- La guía para IA (§9.3) ampliada con **IA de texto** y rasgos fijos por
  personaje; la tabla «Cumplimiento del encargo» antes de la bitácora.

**⚠️**: había **93** al empezar la segunda pasada. Se resolvieron los hex a
ojo de Hisagi, Vanellope, Mike, Sulley y Doofenshmirtz, la pantalla del
Mayor Monograma y la música de TYBW; se añadieron ⚠️ nuevos, honestos, en lo
que sólo tiene una fuente (fandubs sin vistas, compositores con una sola
fuente, técnica de Pierrot). El recuento final está en la tabla de
cumplimiento.

---

## 0 · Cómo elegí las series

### 0.1 Las reglas que seguí

1. **Que no esté tomada.** Miré `MAPA.md`, `TANDAS.md`, `ls encargos/` (131
   encargos), `biblias/_ya_hechas/` (Dragon Ball, Bocchi, Attack on Titan)
   y las láminas que ya existen (Cowboy Bebop, según `reglas_del_dueno.md`). **Ninguna** de las seis que propongo sale en esas listas.
   Comprobado con `grep` en todo el repositorio.
2. **Que la quiera de verdad el público latino.** Con datos: taquilla en
   México, doblaje famoso, memes que todos conocen.
3. **Que el mundo de la serie ya tenga el objeto del canal.** Un canal de
   estrellas necesita una serie donde se juntan estrellas. Un canal de
   eventos, una serie donde cada día hay un plan. Así la lámina no es un
   personaje pegado sobre un fondo: es **un objeto real en un sitio real**
   (regla 1 del dueño).
4. **Que tenga doblaje latino conocido**, con nombres en dos fuentes.
5. **Que los canales vecinos no choquen de tono.** Por ejemplo, #canto y
   #general-doblaje están en EL ESTUDIO, junto a #demos (Evangelion) y
   #demos-canto (Bocchi).

### 0.2 La propuesta, de un vistazo

| Canal | Serie | Personaje | El objeto | Por qué |
|---|---|---|---|---|
| **#destacados** | **Super Mario Galaxy** (juego y película de 2026) | **Estela** (Rosalina) y los Destellos | el **libro de cuentos** de Estela en la Biblioteca del Observatorio, y las **Superestrellas** | en Mario las estrellas se **juntan**; México fue el **primer mercado de la película fuera de EE. UU.** |
| **#eventos** | **Phineas y Ferb** | **Phineas** (con Ferb e Isabella) | el **plano azul** del invento del día, en el **patio** bajo el árbol | cada capítulo es un evento: «Ya sé qué vamos a hacer hoy» |
| **#noticias-anime** | **Bleach** | **Shūhei Hisagi** (el editor) y **Hitsugaya** (el más votado) | la revista **Seireitei Tsūshin**, que existe en el anime (ep. 138) y en un **número extra oficial** de 2023, y la **mariposa infernal** que trae el mensaje | Bleach es la tercera del «Big Three»; Naruto y One Piece ya están tomadas |
| **#noticias-gaming** | **Ralph el demoledor** | **Ralph** y **Vanellope** (Félix para los parches) | los **letreros de LED** de la **Estación Central de Juegos** (y la recreativa nueva del salón de Litwak) | salidas = túneles a cada juego; parches = el martillo de Félix |
| **#general-doblaje** | **Monsters, Inc.** y **Monsters University** | **Mike Wazowski** (y Sulley) | el **tanque de gritos** y el **Piso de Sustos** | el oficio de la voz, con uno de los doblajes latinos más recordados (Andrés Bustamante, Víctor Trujillo, Humberto Vélez) |
| **#canto** | **Sing: ¡Ven y canta!** | **Meena** (la elefanta tímida) y **Buster Moon** | el **volante de la audición** y el **Teatro Moon** | es una película sobre cantar: nervios, técnica, escenario |

### 0.3 Las salas de voz

Van con el mundo de su canal vecino, para que cada sección parezca un
solo sitio (ver §7):

| Sala | Serie | El sitio |
|---|---|---|
| 📻 Radio 24/7 | **Los Simpson** (nueva) | la cabina de **Radio KBBL** de Bill y Marty |
| 🍿 Cine | **Los Simpson** | el **sillón** de la familia frente a la tele |
| 🎲 Juegos | Ralph el demoledor | la taberna de **Tapper** / la Estación Central |
| 🎙️ Grabación | Monsters, Inc. | una **estación del Piso de Sustos**, con su puerta y su tanque |
| 🎚️ Mesa de Trabajo | Monsters, Inc. | el **taller del equipo MIFT** (Monsters at Work) |
| 🎶 Karaoke | Sing | la **fila de audiciones** del Teatro Moon |
| 🔊 Aula | Monsters University | el **aula del profesor Knight** (o Assassination Classroom, para seguir con LA ACADEMIA) |
| 🎭 Escenario | Sing | el **escenario del Teatro Moon**, con el telón |

### 0.4 Las que descarté, y por qué

| Serie | Por qué no |
|---|---|
| Naruto, One Piece, Dragon Ball, Pokémon, Digimon, Caballeros del Zodiaco, Sailor Moon, Supercampeones… | ya están tomadas (encargos o `_ya_hechas`) |
| Coco, Encanto, KPop Demon Hunters, Hatsune Miku, K-On!, Bocchi, Oshi no Ko | eran lo natural para #canto, pero **ya están tomadas** |
| Animal Crossing (para #eventos) | encaja muy bien (Canela y el tablón), pero **no tiene doblaje**: habla en «animalés» |
| Yu Yu Hakusho (para #noticias-anime) | muy querida y con doblaje legendario, pero no tiene un objeto de «noticias» en su mundo |
| Sonic (para #noticias-gaming) | muy querido, pero Ralph **es** un salón de videojuegos: encaja mejor |
| Frozen o Moana (para #canto) | más famosas, pero **no tratan de aprender a cantar**; Sing sí |
| Los Simpson (para #general-doblaje) | el doblaje más famoso, pero su mundo no es un estudio de voz. La paso a la **radio** |

---

## 1 · #destacados → Super Mario Galaxy

### 1.1 El canal

Del inventario (sección **LA SALA**):

> **ıı・🌟・destacados** (texto) · 0 fijados — _Lo que junta estrellas acaba
> aquí solo. Aquí no se escribe._

Es un **tablero de estrellas**: un bot copia aquí los mensajes que reciben
muchas reacciones ⭐. Nadie escribe a mano.

**Textos de la lámina** (una idea cada uno):

| # | Texto | Idea |
|---|---|---|
| 1 | **Destacados** | nombre |
| 2 | **Lo que junta estrellas acaba aquí solo** | cómo funciona |
| 3 | **Reacciona con ⭐ a lo que te guste** | qué hace la gente |
| 4 | **Aquí no se escribe** | la regla |
| 5 | Frase de Estela, en su voz: «Cada estrella que traes cuenta una historia» ⚠️ (frase mía, en su tono, no del juego) | gancho |

Si el bot pide un número de estrellas para entrar (p. ej. 5 ⭐), ese número
va en grande, como el **contador de Superestrellas** del juego.

### 1.2 Por qué Mario, y por qué Galaxy

- **Estrellas que se juntan**: en los juegos de Mario en 3D, cada nivel da
  una **Superestrella** (Power Star). En Super Mario Galaxy (Wii, 2007) se
  juntan para devolver la energía al **Observatorio del Cometa** de Estela. Es
  justo lo que hace el canal: lo que junta estrellas sube solo.
- **La biblioteca y el libro de cuentos**: en el Observatorio hay una
  **Biblioteca**. Cuantas más estrellas junta Mario, más capítulos se abren
  del **libro de cuentos de Estela**. La primera vez, Estela se lo lee en voz
  alta a Mario y a los Destellos. El libro tiene **nueve capítulos** y lo
  escribió el director, **Yoshiaki Koizumi**, de noche y a escondidas ✅
  ([Super Mario Wiki: Library](https://www.mariowiki.com/Library_(Super_Mario_Galaxy)),
  [Super Mario Wiki: Rosalina's Storybook](https://www.mariowiki.com/Rosalina's_Storybook),
  [Mario Wiki en Fandom](https://mario.fandom.com/wiki/Rosalina's_Story)).
  → **Un libro que se llena con estrellas**: es el canal, dentro del mundo.
- **Lo quiere el público latino, con datos**: *Super Mario Galaxy: La
  película* se estrenó el **1 de abril de 2026**. **México fue su primer
  mercado fuera de EE. UU.**: 29,1 millones de dólares el primer fin de
  semana, más de 6 millones de personas, y unos **66,6 millones** en total;
  según *Crónica*, en mayo llegó a superar a EE. UU. y Japón ✅
  ([Noroeste](https://www.noroeste.com.mx/entretenimiento/espectaculos/triunfa-en-la-taquilla-mexicana-super-mario-galaxy-la-pelicula-obtiene-millones-en-su-estreno-LI21387936),
  [Crónica](https://www.cronica.com.mx/tendencias/2026/05/20/mexico-lidera-la-taquilla-mundial-de-super-mario-galaxy-supera-a-estados-unidos-y-japon/),
  [Vanguardia](https://vanguardia.com.mx/show/mexico-impulsa-exito-de-super-mario-galaxy-la-pelicula-con-millonaria-taquilla-NB19818498),
  [Xataka México](https://www.xataka.com.mx/cine-y-tv/super-mario-galaxy-fenomeno-mexico-sus-primeras-cifras-taquilla-dejan-claro-va-record-historico)).
- **«Aquí no se escribe»** pega con Mario: casi no habla («¡Wahoo!»). Quien
  habla en Galaxy es Estela.

### 1.3 El personaje: Estela (Rosalina), no Mario

- **Quién es**: la guardiana del cosmos. Vive en el Observatorio del Cometa y
  cuida de los **Destellos** (Lumas), unas estrellitas con ojos que la
  llaman «mamá» ✅ ([Super Mario Wiki: Rosalina](https://www.mariowiki.com/Rosalina),
  [Wikipedia](https://en.wikipedia.org/wiki/Rosalina_(Mario))).
- **Nombres en español** ✅: **Estela** (Rosalina), los **Destellos**
  (Lumas), el **Observatorio del Cometa**, las **Superestrellas** (Power
  Stars) y los **Trozos de Estrella** (Star Bits)
  ([Super Mario Wiki en español: Estela](https://mario.fandom.com/es/wiki/Estela),
  [SmashPedia: Destello](https://es.ssbwiki.com/wiki/Destello),
  [Nintendo Wiki: Observatorio del Cometa](https://nintendo.fandom.com/es/wiki/Observatorio_del_Cometa),
  [Super Mario Wiki: Trozo de Estrella](https://mario.fandom.com/es/wiki/Trozo_de_Estrella)).
  En la película latina la prensa la llama **Rosalina** ✅
  ([SDP Noticias](https://www.sdpnoticias.com/geek/quien-es-casandra-acevedo-sevilla-actriz-de-doblaje-en-super-mario-galaxy-la-pelicula/),
  [Universo Nintendo](https://universo-nintendo.com.mx/2025/11/12/super-mario-galaxy-la-pelicula-latino-rosalina-bowser-jr/)).
  → En la lámina, **mejor no escribir su nombre**: basta con verla.
- **Carácter** ⚠️ (de memoria, del juego): serena, maternal, un poco triste.
  Habla despacio y bajito. No grita nunca. Explica las cosas como quien lee
  un cuento a niños.
- **Aspecto** (✅ visto en el arte oficial de la hoja de contacto; hex
  medidos en la imagen #43):
  - pelo rubio platino, largo y liso, con un **flequillo largo que le tapa
    el ojo derecho** (el suyo: de frente, queda a la izquierda de quien
    mira) ✅ (visto en #43) `#EFCCAA` en la luz;
  - **corona plateada** con una gema **roja** y otra **turquesa**,
    **pendientes de estrella** dorados ✅ (#43);
  - vestido largo **turquesa** (aguamarina) `#54C0B4`, luces `#6CF0E4`, con
    mangas acampanadas y estrellas bordadas en el bajo (arte de Smash, #54);
  - broche de estrella en el pecho ⚠️;
  - **varita con una estrella** en la punta, casi siempre en la mano;
  - piel muy pálida, ojos azules.
- **Poses que sirven** ✅ (imágenes de la hoja `p29-mario-galaxy`, bajadas
  de la wiki de Fandom por su API):

| # | Imagen | Tamaño | Qué hace | Sirve para |
|---|---|---|---|---|
| 43 | [Rosalina with book](https://static.wikia.nocookie.net/mario/images/c/c0/Rosalina_with_book.png) | 1739×1925 | de pie, **libro en una mano**, la otra abierta | **explicar** (la mejor) |
| 82 | [SMG2 Rosalina screenshot](https://static.wikia.nocookie.net/mario/images/3/37/SMG2_Rosalina_screenshot.png) | 1359×618 | **sentada en su sillón verde de la Biblioteca**, libro en el regazo, Destellos alrededor | el **sitio** del concepto A |
| 69 | [Rosalina's story book](https://static.wikia.nocookie.net/mario/images/5/50/Rosalina%27s_story_book.png) | 1847×846 | primer plano del **libro**: tapa marrón, filete dorado en zigzag, estrella dorada | el **objeto** |
| 54 | [Rosalina & Luma SSBU artwork](https://static.wikia.nocookie.net/mario/images/7/73/Rosalina_%26_Luma_SSBU_artwork.png) | 1376×1606 | varita alzada, Destello al lado | **presentar** |
| 14 | [SSB4 Rosalina Key Art](https://static.wikia.nocookie.net/mario/images/d/d8/SSB4_Rosalina_Key_Art.jpg) | 2475×3500 | flotando en el espacio con un Destello | **celebrar**, portada |
| 8 | [SSB4 Rosalina Artwork (alt)](https://static.wikia.nocookie.net/mario/images/1/1e/SSB4_Rosalina_Artwork_%28alt%29.png) | 3302×3500 | de pie, mano tendida hacia el Destello | **animar** |
| 25 | [SMG Rosalina final concept](https://static.wikia.nocookie.net/mario/images/5/5c/SMG_Rosalina_final_concept.jpg) | 1891×3011 | boceto final del diseño (Wii) | estilo y línea |
| 5 | [Rosalina early concept](https://static.wikia.nocookie.net/mario/images/c/cc/Rosalina_early_concept.jpg) | 2470×5172 | boceto temprano | curiosidad |
| 62 | [SMG2 Rosalina Comet Observatory](https://static.wikia.nocookie.net/mario/images/1/1c/SMG2_Rosalina_Comet_Observatory.png) | 1920×1048 | primer plano, ojos cerrados, el Observatorio detrás | **pensar**, frase final |
- **Quién la acompaña**: el **Destello** amarillo
  ([arte #47](https://static.wikia.nocookie.net/mario/images/a/ad/Yellow_Luma_Art_%28Super_Mario_Galaxy%29.png), 1708×1704)
  y **Polari**, el Destello sabio, negro con ojos azules
  ([arte #45](https://static.wikia.nocookie.net/mario/images/f/ff/Polari_Art_%28Super_Mario_Galaxy%29.png), 1788×1692) ✅. Mario sólo como **silueta pequeña** que llega con una
  estrella.

### 1.4 Cómo habla en pantalla (el cuadro de diálogo)

- **El libro de cuentos** es su «cuadro» propio. La **tapa** ✅ (imagen
  #69, colores medidos): cuero marrón `#6D3715`, **filete dorado en zigzag**
  `#FFE08B` y una **estrella dorada** en el centro `#AC7A24`. Las páginas
  por dentro, con **dibujos de colores suaves, como pastel o acuarela**, son
  ⚠️ de memoria: comprobarlas en un vídeo del capítulo. Es lo ideal: **el
  texto del canal va en la página del libro**, no en un globo.
- **El globo del juego** ✅ (medido en la captura #63,
  [SMG Castle Spin](https://static.wikia.nocookie.net/mario/images/8/8a/SMG_Castle_Spin.png), 1920×1048):
  una **cápsula** muy redondeada, gris muy claro casi blanco `#E9E8ED`,
  con una **colita pequeña** hacia quien habla y una sombra suave. El
  texto va en **negrita redondeada gris oscuro**, centrado. Es un globo de
  cómic, pero **con la forma exacta de Galaxy**: no la «burbuja blanca
  rara», sino esta cápsula.
- **El aviso al conseguir una estrella**: la estrella gira, suena la fanfarria
  y aparece el nombre de la estrella. Es la imagen de «algo destacado».
- **La letra de la franquicia**: Nintendo tiene una letra oficial, la
  **«MARIO Font»**, hecha con **Fontworks**; su primera versión salió en la
  caja y el manual de Super Mario Galaxy 2 ✅ (una fuente:
  [Super Mario Wiki: List of fonts](https://www.mariowiki.com/List_of_fonts);
  la otra, [List of internal fonts](https://www.mariowiki.com/List_of_internal_fonts)).
  **No es libre.** Letras libres comprobadas en §8.

### 1.5 Fondo, luz y paleta

- **El sitio**: el **Observatorio del Cometa**, una nave-observatorio en el
  espacio, con cúpulas ([frente, #26](https://static.wikia.nocookie.net/mario/images/1/17/Comet_Observatory_front_SMG.png), 2560×1920;
  [dormitorio, #27](https://static.wikia.nocookie.net/mario/images/9/90/SMG_Comet_Observatory_Bedroom_Overview.png), 2560×1920).
  Dentro de la **Biblioteca** ✅ (captura #82): **estanterías de madera
  oscura** llenas de libros de colores, un **sillón verde** de respaldo alto,
  luz cálida y Destellos flotando con brillos.
- **La luz** ⚠️: afuera, azul noche con estrellas. Dentro, luz **cálida de
  lámpara** sobre el libro. Ese contraste frío-cálido es lo que da
  profundidad.
- **Paleta** ⚠️ (aproximada):

| Qué | Hex | Origen |
|---|---|---|
| espacio profundo | `#141F49` | medido en #63 ✅ |
| azul de la Vía Láctea | `#12255A` | medido en #63 ✅ |
| globo de diálogo | `#E9E8ED` | medido en #63 ✅ |
| vestido de Estela | `#54C0B4` | medido en #43 ✅ |
| tapa del libro | `#6D3715` | medido en #69 ✅ |
| filete dorado del libro | `#FFE08B` | medido en #69 ✅ |
| Destello amarillo | `#FEFF34` (núcleo) | medido en #82 ✅ |
| madera de la Biblioteca | `#2F0607` a `#483018` | medido en #82 ✅ |
| violeta de nebulosa | `#3B2A6E` | ⚠️ a ojo |

- **Texturas reales**: cuero marrón gastado (la tapa), papel de acuarela
  (grano grueso), madera oscura barnizada, polvo de estrellas (partículas).
- **Modelos 3D libres** (Sketchfab, se pueden bajar):
  - [Power Star](https://sketchfab.com/3d-models/1cc0216bc036486c9629afc2295d0769),
    de **Ludus101**, licencia **CC BY** → crédito: «Power Star by Ludus101
    (CC BY 4.0)».
  - [Luma - Super Mario Galaxy Fan Art](https://sketchfab.com/3d-models/d40d0bfbbc904ed88d85a9d25d0502a4),
    de **caiostange**, **CC BY**.
  - [Rosalina's Storybook](https://sketchfab.com/3d-models/fd49daadcafe427482dc9f4bd0c72008)
    y [Rosalina's Chair](https://sketchfab.com/3d-models/3b5a3e9ee224438c880c6180bd47e18d),
    de **haxagun**, licencia **Free Standard** de Sketchfab (no es CC). ⚠️
    Parecen sacados del juego: **sólo como referencia de forma**, no para
    publicarlos tal cual.

### 1.6 Doblaje latino ✅

**Película de 2026** (*Super Mario Galaxy: La película*): estudio **Grande
Studios**, dirección de **Luis Leonardo Suárez** ✅
([UnoTV](https://www.unotv.com/entretenimiento/de-chris-pratt-a-doblaje-latino-las-voces-de-super-mario-galaxy/),
[Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Super_Mario_Galaxy:_La_pel%C3%ADcula),
leída por su API). Traducción y adaptación: **Katya Ojeda Iturbide**;
mezcla en **Sound Studio Dub** ✅ (Doblaje Wiki). En el doblaje latino se
dice «**Princesa Rosalina**» y los Lumas son «**Destellos**» (Destello
amarillo, verde, naranja, morado…) ✅ (Doblaje Wiki y la prensa).

| Personaje | Voz latina | Fuentes |
|---|---|---|
| **Rosalina / Estela** | **Casandra Acevedo** | ✅ [UnoTV](https://www.unotv.com/entretenimiento/de-chris-pratt-a-doblaje-latino-las-voces-de-super-mario-galaxy/), [SDP Noticias](https://www.sdpnoticias.com/geek/quien-es-casandra-acevedo-sevilla-actriz-de-doblaje-en-super-mario-galaxy-la-pelicula/), [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Casandra_Acevedo) |
| Mario | **Raúl Anaya** | ✅ [UnoTV](https://www.unotv.com/entretenimiento/de-chris-pratt-a-doblaje-latino-las-voces-de-super-mario-galaxy/), [Nintenduo](https://nintenduo.com/reparto-doblaje-voces-mario-bros-pelicula-espanol-latino/) |
| Bowser | **Héctor Estrada** | ✅ las mismas dos |
| Bowser Jr. | Diego Becerril | ✅ UnoTV y [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Super_Mario_Galaxy:_La_pel%C3%ADcula) (API) |
| Destello amarillo | Diana Vanessa Suárez G. | ⚠️ una fuente (Doblaje Wiki) |
| Fox McCloud | **Alfonso «Poncho» Herrera** (el de RBD) | ✅ [UnoTV](https://www.unotv.com/entretenimiento/de-chris-pratt-a-doblaje-latino-las-voces-de-super-mario-galaxy/), [Posta](https://www.posta.com.mx/entretenimiento/super-mario-galaxy-y-el-actor-de-rbd-como-la-voz-a-fox-mcclaude-/vl2184574) |

**Película de 2023** (para Luigi, Peach y Toad), también Grande Studios y
Luis Leonardo Suárez ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Super_Mario_Bros.:_La_pel%C3%ADcula),
[Nintenduo](https://nintenduo.com/reparto-doblaje-voces-mario-bros-pelicula-espanol-latino/),
[DubDB](https://dubdb.fandom.com/wiki/Super_Mario_Bros._La_Pel%C3%ADcula_(Latin_American_Spanish))):
Luigi **Roberto Salguero**, Peach **Ale Pilar**, Toad **Miguel Ángel Ruiz**,
Donkey Kong **Mark Pokora**. Dato que gusta: **Pepe Toño Macías**, el Luigi
de la película de 1993, hace del tío Arthur ✅ (las mismas fuentes).

Casandra Acevedo también es Robin en *Stranger Things* y Hazel en el
remake de *Los Padrinos Mágicos* ✅ (UnoTV y SDP Noticias).

> [!warning] No hay frase latina famosa de Estela
> La película es de este año. No encontré una frase suya que se haya hecho
> meme. **No inventar una y ponerla como del doblaje.** Si se usa una frase,
> que sea del juego o que se diga que es del servidor.

### 1.7 Música ⚠️ (de memoria)

- El **vals del Observatorio del Cometa** (tranquilo, de caja de música) y
  **Gusty Garden Galaxy** (orquesta épica). Compositores **del juego**:
  **Mahito Yokota**, con **Koji Kondo** ⚠️.
- **Corregido (segunda pasada)**: la banda sonora de **la película** (2026)
  **no es de Yokota**: es de **Brian Tyler** (el de la película de 2023),
  que remezcla los temas de los dos Galaxy y de Star Fox, con la
  colaboración de **Koji Kondo** ⚠️ (una fuente:
  [Wikipedia: The Super Mario Galaxy Movie (soundtrack)](https://en.wikipedia.org/wiki/The_Super_Mario_Galaxy_Movie_(soundtrack)),
  que cita al sello Back Lot Music/iam8bit, 1 abr 2026).
- El ambiente que da: calma de noche estrellada, cuento antes de dormir.

**Vídeos** (encontrados con `yt-dlp`; YouTube no dejó bajar subtítulos, así
que no doy minuto dentro del vídeo, sólo su duración):

| Vídeo | Canal | Duración |
|---|---|---|
| [Tráiler final (México)](https://www.youtube.com/watch?v=ipzEY7c7it8) | Universal Pictures México (oficial) | 2:24 |
| [Tráiler en español latino](https://www.youtube.com/watch?v=pXBMPTKSdqA) | Cineteca | 2:05 |
| [Tráiler 2 latino (Yoshi)](https://www.youtube.com/watch?v=L5VGFQHyeL4) | ONE Media Español | 2:25 |
| [Tráiler 2 latino, versión extendida](https://www.youtube.com/watch?v=HgzB1rp9ae4) | Boxoffice Tráilers Español | 2:50 |

### 1.8 Lo que ama el fandom, y qué NO hacer

- Se ama ⚠️: el **capítulo final del libro** (triste: la madre que no
  vuelve); los Destellos que se transforman en planetas; la estrella que
  gira al conseguirla.
- **No hacer**:
  - poner a Estela **enfadada o gritando**: no es ella;
  - **voltear en espejo** una imagen suya: el flequillo pasaría al otro
    ojo. Le tapa siempre **su ojo derecho** ✅ (#43);
  - usar la «Estrella Warp» de Kirby o una estrella genérica de cinco
    puntas plana: la **Superestrella** de Mario tiene **ojos** y volumen;
  - mezclar el estilo de la película (3D de Illumination) con el del juego
    en la misma lámina.

### 1.8 bis · Segunda pasada: vídeo, juego, técnica, cruces y mundo

**Mirado en vídeo, con minuto** (Dailymotion, `fotogramas.py`):
- [Tráiler final latino](https://www.dailymotion.com/video/xa1o2hg?t=120)
  (2:24), **min. 2:00**: Estela de pie, brazo hacia una máquina, vestido
  ondeando, en una nave con **luz verde y neón magenta**. Vestido medido
  `#A4ECFA` ✅. Es la variante **de acción** de la pose #43. Si la lámina
  sigue el estilo de **la película**, el fondo es futurista y saturado, no
  la Biblioteca cálida del juego.
- La frase de Bowser que se oye en el tráiler latino
  ([x9to08e](https://www.dailymotion.com/video/x9to08e)) salió con demasiado
  ruido en `voz.py`: **no se cita** como textual ⚠️.

**Fan art de referencia (3)**: [masoq en Danbooru](https://danbooru.donmai.us/posts/11099671),
Rosalina, 2980×2412, `rating:g` ✅. Sólo para pose y color, nunca se pega.

**Fondo de pantalla (16)**: [wallhaven 2yrr3g](https://wallhaven.cc/w/2yrr3g),
1920×1080, pixel art de Rosalina, subido por **vye18756** (128 favoritos) ✅.

**Videojuego e interfaz (11)**: *Super Mario Galaxy* (Wii, 2007). HUD con
vidas y estrellas; ventanas de diálogo de **marco redondeado azul** con el
retrato a la izquierda ✅ ([Spriters Resource](https://www.spriters-resource.com/wii/supermariogalaxy/asset/136701/),
[Game UI Database](https://www.gameuidatabase.com/gameData.php?id=422)). La
letra interna del HUD se llama «**Classic HUD font**» ⚠️
([Super Mario Wiki](https://www.mariowiki.com/List_of_internal_fonts)); el
nombre «Pop Happiness» que sale en algún buscador es de otro juego: no usarlo.

**Técnica y cómo replicarla (18)**: la película es de **Illumination
Studios Paris** ✅ ([Illumination Wiki](https://illumination.fandom.com/wiki/The_Super_Mario_Galaxy_Movie),
[Wikipedia en español](https://es.wikipedia.org/wiki/Super_Mario_Galaxy:_la_pel%C3%ADcula)),
que modela en **Autodesk Maya** y compone en **Nuke**; el render es propio y
sin nombre público ✅ ([pipeline del estudio](https://www.illuminationstudiosparis.com/pipeline/)).
- **Blender**: Eevee con *toon shader* de nodos (rampa de color + Fresnel en
  el borde). Contorno con **Solidify invertido**, no Freestyle: Illumination
  no usa línea negra dura, sino oclusión ambiental marcada.
- **Photoshop**: luces en *Color Dodge* suave; sombras en *Multiply* de un
  solo tono, sin degradado largo.

**Gustos (20)**: a Estela le importan su **libro de cuentos** y los
Destellos, a los que llama sus hijos. Es una figura cósmica: el juego **no le
da** cumpleaños ni comida favorita ⚠️. No inventarlos.

**Colaboraciones, figura y cosplay (23)**:
- **amiibo de Rosalina** (serie Smash Bros., 1-feb-2015), con su varita:
  pose 3D oficial para el concepto B ✅ ([Nintendo](https://www.nintendo.com/us/store/products/amiibo-rosalina-super-smash-bros-100722/),
  [Amiibo Wiki](https://amiibo.fandom.com/wiki/Rosalina_(Super_Smash_Bros.))).
- **Cosplay comercial** (edición película 2026): satén cristal turquesa con
  forro de crepé, corona, broche y pendientes de estrella ✅ ([Takerlama](https://www.takerlama.com/products/rosalina-princess-dress-cosplay-costume-the-super-mario-galaxy-movie-fancy-dress-takerlama)).
  Sirve para ver cómo cae la tela de verdad.

**Obras parecidas (24)**: secuela directa de *Super Mario Bros.: La película*
(2023), mismo estudio; la saga pasa de **2.000 millones de dólares** ✅
([Infobae](https://www.infobae.com/malditos-nerds/2026/04/20/super-mario-galaxy-la-pelicula-impulsa-la-saga-de-illumination-y-nintendo-mas-alla-de-los-2-mil-millones/)).
Tono parecido: *Sonic, la película* y *Ralph el demoledor* (§4, que es de
#noticias-gaming: no repetir el salón recreativo aquí).

**El mundo en cinco líneas (25)**:
1. Las **Superestrellas** (Power Stars) dan energía al universo.
2. La **Gran Estrella** alimenta el Observatorio; Bowser la roba para su nave.
3. Estela vive en el **Observatorio Cometa**, biblioteca y nave a la vez.
4. Los **Destellos** (Lumas) son estrellas bebé; al crecer se vuelven planetas.
5. Mario viaja de galaxia en galaxia recuperando estrellas.
Vocabulario: Destello, Superestrella, Gran Estrella, Observatorio.

**Fan dubs (22)** y **escenas que hacen llorar (21)**: no encontré fandubs
en español de Galaxy (búsqueda «Mario Galaxy fandub español»); la película
es de 2026 y el doblaje oficial lo tapa todo ⚠️. Escena que hace llorar,
con fuente: no se buscó una para Galaxy en esta pasada ⚠️ (queda para su
biblia completa).

### 1.9 Conceptos de lámina

**Concepto A · El libro de cuentos de Estela** (el recomendado)
- **Objeto real en sitio real**: el **libro de cuentos abierto** en un atril
  de la **Biblioteca del Observatorio**. Se hace en **Blender** (tapa de tela,
  páginas curvas, lomo con estrellas bordadas).
- **Personaje**: Estela **sentada en su sillón verde, leyendo**, con tres
  Destellos flotando. Pose y sitio: la captura **#82**; si se quiere de pie,
  el arte **#43** (libro en la mano). El libro, como la tapa **#69**.
- **Cómo habla**: no hay globo. El texto **es la página del libro**, en letra
  de cuento (ver §8: *Fredoka* o *M PLUS Rounded 1c*), con un dibujo pequeño
  estilo pastel de una estrella.
- **Dónde va cada texto**: título **Destacados** en la tapa o arriba de la
  página izquierda; «Lo que junta estrellas acaba aquí solo» en la página
  izquierda; «Reacciona con ⭐» y «Aquí no se escribe» en la derecha, como
  capítulos 1 y 2.
- **Que no quede plano**: la lámpara cálida ilumina el libro; el espacio azul
  por la ventana del fondo; **un Destello delante, desenfocado**, tapando una
  esquina; polvo de estrellas flotando en el haz de luz.

**Concepto B · La cúpula que se llena de estrellas**
- **Objeto**: el **panel de Superestrellas** de la cúpula (la cuenta de
  estrellas encendidas y apagadas), como un tablero.
- **Personaje**: Mario de espaldas, **alzando una Superestrella**; Estela
  flotando arriba, varita alzada.
- **Texto**: el número de estrellas para entrar, enorme, junto a una
  Superestrella; las reglas en la caja de diálogo del juego.
- **Que no quede plano**: la estrella que Mario alza es la fuente de luz;
  contraluz sobre Estela; Destellos cruzando delante.

**Concepto C (rápido) · la Superestrella sola**: una Superestrella girando
sobre un pedestal del Observatorio, con el texto en la caja del juego. Sólo
si hace falta una versión pequeña (miniatura o icono).

---

## 2 · #eventos → Phineas y Ferb

### 2.1 El canal

Del inventario (sección **EN VIVO**):

> **ıı・🎟️・eventos** (texto) · 0 fijados — _Lo que se viene. Se convoca con
> /create y cada uno lo ve en su hora._

**Textos de la lámina**:

| # | Texto | Idea |
|---|---|---|
| 1 | **Eventos** | nombre |
| 2 | **Lo que se viene** | para qué es |
| 3 | **Se convoca con /create** | cómo se crea uno |
| 4 | **Cada uno lo ve en su hora** | la hora de cada país sale sola |
| 5 | Phineas: «**Ya sé qué vamos a hacer hoy**» ✅ (así se adaptó en latino, ver §2.4) | gancho |

Si hace falta explicar más (cómo marcar «Me interesa», el aviso antes de
empezar), va en una **lámina 2** con el plano paso a paso.

### 2.2 Por qué Phineas y Ferb

- **Cada capítulo es un evento.** Por la mañana, Phineas dice «Ferb, ya sé
  qué vamos a hacer hoy», dibujan un **plano azul**, lo construyen en el
  patio, invitan a todo el barrio… y a la tarde desaparece ⚠️ (de memoria,
  es la fórmula de toda la serie).
- **«Lo que se viene»**: la canción de entrada es **una lista de planes**
  para las vacaciones: «Lanzar un cohete, luchar con las momias, subir la
  torre Eiffel por fuera…», y acaba con «**No busques más, pues Phineas y
  Ferb lo van a demostrar**» ✅ (letra latina en
  [Cancioneros](https://www.cancioneros.com/lyrics/song/1963869/phineas-y-ferb-intro-espanol-latino-phineas-e-ferb);
  Doblaje Wiki cita las mismas líneas, «Tu hermana furiosa poner» y «No
  busques más…», como del doblaje latino). La canta en latino **Roberto
  Velázquez** ✅ (Doblaje Wiki). Desde la 3.ª temporada, el **calendario**
  que abre la intro («Junio») se tradujo al español ✅ (Doblaje Wiki).
- **Está viva en 2026**: la **quinta temporada** (40 episodios nuevos) se
  estrenó el **5 de junio de 2025** en Disney Channel y el 6 en Disney+
  Latinoamérica, con tráiler doblado ✅
  ([ANMTV, tráiler](https://www.anmtvla.com/2025/04/phineas-y-ferb-disney-latinoamerica.html),
  [ANMTV, estreno](https://www.anmtvla.com/2025/06/phineas-y-ferb-quinta-temporada-ya-esta.html),
  [SensaCine Colombia](https://www.sensacine.com.co/noticias/noticia-1000148279/)).
- **La quiere el público latino**: se emitió en Latinoamérica del **1 de
  febrero de 2008 al 21 de junio de 2015** ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Phineas_y_Ferb),
  [SensaCine Colombia](https://www.sensacine.com.co/noticias/noticia-1000148279/)).
  Es la infancia de casi todo el servidor.

### 2.3 Los personajes

**Phineas Flynn** — el que convoca (el principal)
- Optimista sin fin. Nunca duda de que se puede. Es el que **tiene la idea
  y la anuncia** ⚠️ (de memoria).
- **Cabeza en forma de triángulo**, pelo rojo. El dibujo nació en un
  restaurante de South Pasadena: **Dan Povenmire** garabateó un niño
  triangular en el papel de la mesa ✅ ([Wikipedia: Phineas Flynn](https://en.wikipedia.org/wiki/Phineas_Flynn),
  [Wikipedia: Dan Povenmire](https://en.wikipedia.org/wiki/Dan_Povenmire)).
- Estilo: **formas geométricas**, influido por **Tex Avery** ✅ (las mismas
  fuentes).
- Ropa ✅ (medida en el fotograma #21): camiseta de **rayas naranja**
  `#FA8836` **y crema** `#FBEDD4`, pantalón corto azul, zapatillas. Pelo
  rojo `#E84725`, piel `#FBBE9F`.
- Poses (hoja `p29-phineas-y-ferb`, bajada de la wiki de Fandom):

| # | Imagen | Tamaño | Qué hace | Sirve para |
|---|---|---|---|---|
| 21 | [First I know what we're gonna do today](https://static.wikia.nocookie.net/phineasandferb/images/8/87/First_I_know_what_we%27re_gonna_do_today.jpg) | 1896×1068 | Phineas **con los brazos abiertos** bajo el árbol; Ferb leyendo al lado; la cerca detrás | **anunciar** (la mejor) |
| 52 | [Phineas Flynn](https://static.wikia.nocookie.net/phineasandferb/images/5/52/Phineas_Flynn.png) | 744×1092 | de cuerpo entero, sonrisa, de perfil | recortar |
| 54 | [Profile - Ferb Fletcher](https://static.wikia.nocookie.net/phineasandferb/images/c/ca/Profile_-_Ferb_Fletcher.PNG) | 848×933 | Ferb **con el martillo en alto** | **construir** |
| 3 | [NF.jpg](https://static.wikia.nocookie.net/phineasandferb/images/d/d2/NF.jpg) | 2737×1536 | Ferb en el patio **con un rollo de papel** | el plano |
| 33 | [Make anything at all prints](https://static.wikia.nocookie.net/phineasandferb/images/9/95/Make_anything_at_all_prints.jpg) | 1280×720 | **todo el grupo sujeta un plano azul gigante** en el patio | el **objeto** |
| 2 | [Phineas-and-ferb-exclusive-3](https://static.wikia.nocookie.net/phineasandferb/images/1/1c/Phineas-and-ferb-exclusive-3.jpg) | 3000×1688 | Phineas e Isabella de la mano, frente a la casa | amistad |
| 16 | [Flop Starz](https://static.wikia.nocookie.net/phineasandferb/images/2/28/Flop_Starz.jpg) | 1920×1080 | los dos tocando en un **escenario** con focos | **Escenario** (sala) |
| 26 | [DoofenshmirtzPnFArt](https://static.wikia.nocookie.net/phineasandferb/images/0/08/DoofenshmirtzPnFArt.png) | 827×1820 | Doofenshmirtz frotándose las manos | el villano |
| 55 | [Interrupted Image95](https://static.wikia.nocookie.net/phineasandferb/images/c/c6/Phineas_and_Ferb_Interrupted_Image95.jpg) | 1181×665 | escenario con un cartel de **BLUEPRINTS** | idea de rótulo |

**Ferb Fletcher** — el que construye
- Casi no habla. Cuando habla, dice una frase perfecta al final ⚠️.
- Alto, **pelo verde** `#31B536`, camisa **amarillo pálido** de cuello
  blanco `#FDFCCA`, **pantalón morado** `#7E39CB` ✅ (medido en #21). Con
  martillo o herramienta (#54).

**Isabella García-Shapiro** — la vecina
- Entra por la puerta del patio y pregunta. En inglés es «Whatcha doin'?»;
  **en latino se adaptó como «¿Qué están haciendo?»**, salvo en el primer
  episodio, donde dijo «¿Qué hacen?» y sin su cantadito ✅ ([Doblaje
  Wiki](https://doblaje.fandom.com/es/wiki/Phineas_y_Ferb), leída por su API). Lazo rosa, uniforme de
  exploradora: en latino son «**las Exploradoras**» ✅ (Doblaje Wiki: «La
  fiesta de las exploradoras»); su emblema está en la hoja (#1).
- Voz latina: **Paulina García Casillas** (T1-T4); en la **T5**, **Habana
  Zoé** ✅ (Doblaje Wiki, fichas de la serie y de la
  [5.ª temporada](https://doblaje.fandom.com/es/wiki/Phineas_y_Ferb/5%C2%AA_temporada);
  y el buscador, que dice que García Casillas se retiró tras la película de
  2020). Contradicción resuelta.

**Dr. Heinz Doofenshmirtz** — el secundario más querido ⚠️
- El villano torpe de **Doofenshmirtz Malvados y Asociados** (así se llama
  su *jingle* en latino) ✅. Cada capítulo presenta su nuevo invento
  terminado en **«-inador»**, sufijo que el doblaje latino mantuvo ✅
  (Doblaje Wiki). Y cuenta una historia triste de su infancia en
  Gimmelshtump ⚠️ (de memoria).
- Es el que más memes da. **Ojo**: en inglés grita «Curse you, Perry the
  Platypus!», pero **en latino dice «¡Te odio, Perry el ornitorrinco!»**
  ✅ (Doblaje Wiki). «¡Maldito seas!» es la versión de España: **no usarla**.
- Voz latina: **Germán Fabregat** en todas las temporadas, también la T5 ✅
  ([Doblaje Wiki: la serie](https://doblaje.fandom.com/es/wiki/Phineas_y_Ferb),
  [la T5](https://doblaje.fandom.com/es/wiki/Phineas_y_Ferb/5%C2%AA_temporada),
  [Germán Fabregat](https://doblaje.fandom.com/es/wiki/Germ%C3%A1n_Fabregat)).

**Perry el ornitorrinco / Agente P** — el que desaparece
- En latino: «**Oye, ¿y Perry?**» (o «Oigan, ¿y Perry?»); a veces «Oye,
  ¿a dónde se fue Perry?» ✅ (Doblaje Wiki). Sombrero de agente, cara seria.
  Lo dobla (sus gruñidos) **Luis Daniel Ramírez** ✅ (Doblaje Wiki).

**Candace Flynn** — la hermana que quiere acusarlos
- «¡Mamá! ¡Phineas y Ferb están…!» ⚠️.

### 2.4 Doblaje latino

Todo leído en **Doblaje Wiki por su API** ([la serie](https://doblaje.fandom.com/es/wiki/Phineas_y_Ferb),
[la 5.ª temporada](https://doblaje.fandom.com/es/wiki/Phineas_y_Ferb/5%C2%AA_temporada))
y cruzado con la prensa. Estudio: primero **SDI Media de México**, luego
**Diseño en Audio (DNA)**; dirección: **Francisco Colmenero** ✅ (Doblaje
Wiki). La T5 también es de **DNA** con **Francisco Colmenero** ✅.

| Personaje | Voz (T1-T4) | Voz (T5, 2025) | Segunda fuente |
|---|---|---|---|
| **Phineas** | **Memo Aponte** | **Marc Winslow** (Aponte se retiró en 2020) | ✅ [SensaCine Colombia](https://www.sensacine.com.co/noticias/noticia-1000148279/) |
| **Ferb** | **Marco Portillo** (T1-T3), luego **Diego Ángeles** | Diego Ángeles | ✅ buscador (ficha de la T5) |
| **Candace** | **Christine Byrd** | **Fernanda Gastélum** | ✅ buscador (Byrd se retiró en 2016) |
| **Isabella** | **Paulina García Casillas** | **Habana Zoé** | ✅ buscador |
| **Doofenshmirtz** | **Germán Fabregat** | Germán Fabregat | ✅ [Doblaje Wiki: Germán Fabregat](https://doblaje.fandom.com/es/wiki/Germ%C3%A1n_Fabregat) |
| Perry | Luis Daniel Ramírez | (sin voz, N/A) | ⚠️ sólo Doblaje Wiki |
| Baljeet | Héctor Cuevas Ireta de Alba | Héctor Ireta de Alba | ✅ [su vídeo](https://www.youtube.com/watch?v=JncOXUN0Nrw) |
| Buford | Rodrigo Gutiérrez | Carlos Siller | ⚠️ sólo Doblaje Wiki |
| Mayor Monograma | Mario Díaz Mercado | — | ⚠️ sólo Doblaje Wiki |
| Vanessa | Erica Edwards | Erica Edwards | ⚠️ sólo Doblaje Wiki |

Datos que gustan ✅ (Doblaje Wiki):
- Marco Portillo se **retiró en 2012**: Ferb fue su último personaje.
- **Georgina Sánchez** (la voz habitual de Ashley Tisdale en México) iba a
  ser Candace, pero Disney eligió a Christine Byrd.
- La frase «**Ya sé qué vamos a hacer hoy**», con la voz de Memo Aponte,
  fue **tono de espera de Telcel** (Contestone).

### 2.5 Cómo habla en pantalla (el cuadro)

- **El plano azul** (blueprint) ✅ (existe como objeto en pantalla: el
  fotograma #33, todo el grupo sujetando un plano gigante): papel azul
  `#1E507C`-`#416C97` con **líneas más claras** `#2674B5` y blancas. Las
  notas a mano y las cotas son ⚠️ de memoria. **Es el cuadro de diálogo de la serie**: el texto del canal va
  escrito a mano en el plano, con flechas.
- **La cartela del invento de Doofenshmirtz**: el nombre del «-inador» en
  grande. En latino se mantiene el sufijo **«-inador»** ✅ (Doblaje Wiki).
- **La pantalla del Mayor Monograma** en la guarida de Perry: un monitor que
  da la misión del día ⚠️.
- **La letra**: el logo es propio (no libre). Para el plano, una letra de
  arquitecto a mano: **Architects Daughter** (§8).

### 2.6 Fondo, luz y paleta (medida en los fotogramas #21 y #33)

- **El patio trasero** de la casa Flynn-Fletcher: césped, **cerca de madera**,
  y el **árbol grande** donde se sientan Phineas y Ferb cada mañana.
- Luz de **mañana de verano**, cielo limpio, sombras cortas.
- La **ciudad** es **Danville**; el edificio de **Malvados y Asociados** de
  Doofenshmirtz es morado, con su balcón.

| Qué | Hex | Origen |
|---|---|---|
| cielo | `#61D0FF` | #33 ✅ |
| césped | `#4F812E` | #21 ✅ |
| cerca de madera | `#CF9D58` (luz) / `#DFA864` | #21 ✅ |
| tronco del árbol | `#957733` | #21 ✅ |
| naranja de Phineas | `#FA8836` | #21 ✅ |
| pelo de Ferb | `#31B536` | #21 ✅ |
| azul del plano | `#1E507C` / `#416C97` | #33 ✅ |
| líneas del plano | `#2674B5` y blanco | #33 ✅ |
| Doofenshmirtz: bata, camisa, pelo | `#FFFFFD` / `#020202` / `#773B16` | medido en [Doofenshmirtz_Portrait.jpg](https://static.wikia.nocookie.net/phineasandferb/images/5/5d/Doofenshmirtz_Portrait.jpg) (800×1000) ✅. El `#6A3D9A` «morado» de la primera pasada **no aparece** en ningún arte oficial ni en 3 fotogramas de tráiler: quitado |

- **Texturas reales**: papel de plano (cianotipo), madera de cerca pintada,
  cinta adhesiva, chinchetas. Libres (CC0) en Poly Haven:
  [wood_planks](https://polyhaven.com/a/wood_planks) para la cerca.
- **Modelos 3D libres** (Sketchfab, CC BY):
  [Old Blueprints](https://sketchfab.com/3d-models/4759259e450a4269a93c582dd276f1b9)
  de **FrodoUndead**; [Wooden Fence #free](https://sketchfab.com/3d-models/689c4692efc347328ed0daaa07effe5e)
  de **realMrAnderson**; [Bulletin Board](https://sketchfab.com/3d-models/8f06a1ffa3ca417e822f038c43d48d54)
  de **jaromir.ternavskiy**. Crédito: «<nombre> by <autor> (CC BY 4.0)».
- **Vídeos**: [tráiler oficial de la T5, Disney+ Latinoamérica](https://www.youtube.com/watch?v=L23qqubCBEA)
  (1:10); [tráiler de *Candace contra el universo*](https://www.youtube.com/watch?v=cuG-Typdck0) (1:37).

### 2.7 Qué NO hacer

- Dibujar a Phineas **de frente con la cara redonda**: su cabeza es un
  triángulo de perfil.
- Poner a Ferb hablando mucho.
- Que el invento sea **peligroso de verdad** o triste: el tono es verano,
  sol y risa.

### 2.7 bis · Segunda pasada: vídeo, juego, técnica, cruces y mundo

**Mirado en vídeo, con minuto** ([tráiler oficial T5, Disney+, en
español](https://www.dailymotion.com/video/x9ozu2m), 1:10, `fotogramas.py`):
- **min. 0:00**: Phineas de perfil, cabeza triangular, cerca de madera
  detrás. El diseño de perfil es igual en la temporada de 2025 ✅.
- **min. 0:20**: la pantalla del **Mayor Monograma** con sus iniciales «MM»
  en la esquina, verde agua con marco. Antes era ⚠️ de memoria: **ahora ✅**.
  Pose de **presentar misión**.
- **min. 1:00**: el gag de «¿y Perry?», todo el grupo en el patio y Perry
  asomando por la puerta de la cerca.
- El minuto exacto de la escena del **plano azul** no sale en los tráileres
  cortos; los capítulos no están en Internet Archive ⚠️.

**Música (9)**: compositor **Danny Jacob**; el opening «**Today Is Gonna Be
a Great Day**» lo canta **Bowling for Soup** (nominado al Emmy) ⚠️ (una
fuente: [Wikipedia](https://en.wikipedia.org/wiki/Phineas_and_Ferb)).

**Doblaje, nombres nuevos con dos fichas (8)** ✅: **Luis Daniel Ramírez**
es Perry en toda la franquicia ([su ficha](https://doblaje.fandom.com/es/wiki/Luis_Daniel_Ram%C3%ADrez));
**Mario Díaz Mercado** es el Mayor Monograma ([su ficha](https://doblaje.fandom.com/es/wiki/Mario_D%C3%ADaz_Mercado)),
también en *La ley de Milo Murphy* y *Candace contra el universo*. Erica
Edwards (Vanessa, T5) sigue con una sola fuente ⚠️.

**Fan art (3)**: [nokonorii en Danbooru](https://danbooru.donmai.us/posts/6926732),
Phineas y Ferb juntos, 722×450, `rating:g` ✅.

**Fondo de pantalla (16)**: Wallhaven no tiene **ninguno** (5 búsquedas, 0
resultados). En Wallpaper Abyss: [Perry y Doofenshmirtz](https://wall.alphacoders.com/big.php?i=860513),
1920×1080, subido por **Perceval21** ✅.

**Videojuego (11)**: *Phineas and Ferb: Across the 2nd Dimension* (Wii, PS3,
DS; 2011). Menú con selección de episodio e idioma y extra «Enter Code» ✅
([Wikipedia](https://en.wikipedia.org/wiki/Phineas_and_Ferb:_Across_the_2nd_Dimension_(video_game)),
[galería de la wiki](https://phineasandferb.fandom.com/wiki/Gallery:Phineas_and_Ferb:_Across_the_2nd_Dimension_(video_game))).

**Técnica y cómo replicarla (18)**: 2D digital en **Toon Boom**, animado por
**Rough Draft Studios** (Corea), **Wang Film** (Taiwán) y **Synergy/Hong
Ying** (Shanghái) ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Phineas_and_Ferb)).
Dan Povenmire toma de **Tex Avery** las formas geométricas, y de **Matt
Groening** (Los Simpson) la lección de las **siluetas reconocibles**; quería
personajes que un niño pudiera dibujar.
- **Photoshop**: capas de **color plano sin degradado**, recortadas con lazo
  poligonal; contorno negro uniforme de **1-2 px**.
- **Blender** (sólo si hace falta volumen, p. ej. la cerca o el plano):
  **Freestyle con grosor constante** y sombreado *toon* de **2 tonos**
  (Shader to RGB + ColorRamp de 2 paradas).
- **Encuadre típico**: los chicos en plano medio frente a la cerca; el
  invento, siempre enorme detrás.

**Gustos (20)**: Phineas dibuja el **plano azul** cada mañana y nunca se le
ve sin ideas ⚠️. **Doofenshmirtz** odia a su hermano **Roger** («el bueno de
la familia») y cuenta un recuerdo de **Gimmelshtump** en cada episodio ✅
([Phineas and Ferb Wiki](https://phineasandferb.fandom.com/wiki/Heinz_Doofenshmirtz), API).

**Fan dubs y comunidad (22)** ⚠️ (título y canal; YouTube no dejó ver las
vistas): el canal **SALMAR FANDUBS** hace parodias latinas («PHINEAS Y FERB
(MENCIÓN A BOB ESPONJA) / FANDUB LATINO»); el canal **anthpo** subió «Todos
los episodios de Phineas y Ferb | Español Latino (Fandub)».

**Cruces (23)** ✅: dos especiales reales de Disney, **Mission Marvel**
(16-ago-2013: Iron Man, Thor, Hulk y Spider-Man pierden sus poderes) y
**Star Wars** (26-jul-2014) ([Wikipedia: Mission Marvel](https://en.wikipedia.org/wiki/Phineas_and_Ferb:_Mission_Marvel),
[Wikipedia: Star Wars](https://en.wikipedia.org/wiki/Phineas_and_Ferb:_Star_Wars),
[Hollywood Reporter](https://www.hollywoodreporter.com/tv/tv-news/phineas-ferb-creators-marvel-superheroes-604392/)).
Traen **ropa nueva** (Vengadores, Jedi): buena para una lámina 2 de #eventos.

**Obras parecidas (24)**: *Gravity Falls* y *El asombroso mundo de Gumball*,
por el dibujo geométrico y la aventura de verano ⚠️ (comparación de crítica
general, sin una fuente que junte las tres).

**El mundo en cinco líneas (25)**:
1. Verano en **Danville**: cada día, Phineas y Ferb construyen algo imposible.
2. Candace intenta **delatarlos**; el invento desaparece justo antes.
3. Perry, la mascota, es el **Agente P** de la **O.S.B.A.** («Organización
   Sin un Buen Acrónimo»; en inglés O.W.C.A.) ✅ ([wiki en español](https://phineasyferb.fandom.com/es/wiki/Organizaci%C3%B3n_Sin_un_Buen_Acr%C3%B3nimo_(O.S.B.A)),
   [wiki en inglés](https://phineasandferb.fandom.com/wiki/Organization_Without_a_Cool_Acronym)).
4. Su jefe es el **Mayor Monograma**; su enemigo, Doofenshmirtz.
5. Cada invento de Doofenshmirtz lleva el sufijo **«-inador»** (§2.5).
Vocabulario: «-inador», «Ya sé qué vamos a hacer hoy», «¿Y Perry?»,
Danville, O.S.B.A. El logo de la O.S.B.A. sirve de **sello de «evento
secreto»** en la lámina.

### 2.8 Conceptos de lámina

**Concepto A · El plano del día, clavado en la cerca** (el recomendado)
- **Objeto real en sitio real**: un **plano azul** grande clavado con
  chinchetas en la **cerca del patio**, bajo el árbol. En **Blender**: papel
  ondulado, sombras de las hojas encima.
- **Personaje**: Phineas con los **brazos abiertos** como en el fotograma
  **#21** (el de «ya sé qué vamos a hacer hoy»), o con un lápiz señalando;
  Ferb detrás **con el martillo** (#54); Isabella asomada a la puerta (su
  «¿Qué están haciendo?» en un globo pequeño).
- **Cómo habla**: el texto va **escrito a mano en el plano**, en blanco, con
  flechas y cotas.
- **Dónde va cada texto**: «Eventos» en el cajetín del plano (abajo a la
  derecha, como en los planos de verdad); «Lo que se viene» como título;
  «Se convoca con /create» junto a un dibujo de un botón; «Cada uno lo ve
  en su hora» junto a **cinco relojitos** (Lima, Ciudad de México, Caracas,
  Bogotá, Quito).
- **Que no quede plano**: sombra de las hojas del árbol sobre el papel; el
  borde del plano levantado por el viento; una **herramienta desenfocada**
  en primer plano.

**Concepto B · El «Convoca-inador» de Doofenshmirtz**
- **Objeto**: una máquina absurda en el **balcón de Malvados y Asociados**,
  con un calendario gigante.
- **Personaje**: Doofenshmirtz presentando su invento con los brazos
  abiertos (#26, o el mapa del Área de los Tres Estados, #4 y #23); Perry
  atrapado al lado, con cara seria (#24, «Perry trapped»).
- **Texto**: el nombre del invento en su cartela; las reglas del canal en
  un panel de la máquina.
- **Que no quede plano**: contraluz de atardecer detrás del edificio
  morado; Perry delante, cortado por el borde.

---

## 3 · #noticias-anime → Bleach

### 3.1 El canal

Del inventario (sección **NOTICIAS**):

> **ıı・📰・noticias-anime** (texto) · 1 fijado — _Anime: estrenos,
> temporadas y doblajes. Lo trae un bot. Para comentar, abre un hilo en la
> noticia._

**Textos de la lámina**:

| # | Texto | Idea |
|---|---|---|
| 1 | **Noticias de anime** | nombre |
| 2 | **Estrenos, temporadas y doblajes** | qué trae |
| 3 | **Lo trae un bot** | nadie lo escribe a mano |
| 4 | **Para comentar, abre un hilo en la noticia** | la regla |
| 5 | Frase del personaje, seca, en su tono ⚠️ (la escribe el servidor) | gancho |

Vecino: **#noticias-series** es Rick and Morty (la tele interdimensional) y
**#noticias-gaming** será Ralph (§4). Las tres láminas de NOTICIAS pueden
compartir **una misma franja arriba**, como una cabecera de periódico.

### 3.2 Por qué Bleach

- **Tiene un periódico dentro de la serie.** La **Seireitei Tsūshin**
  (瀞霊廷通信, «Comunicación Seireitei») es la revista oficial de la Sociedad
  de Almas. La hace la **9.ª División**, y su editor es su teniente,
  **Shūhei Hisagi**. En la novela *Can't Fear Your Own World* (de Ryōgo
  Narita, que continúa el manga) Hisagi es el **editor jefe** y sale a
  investigar un artículo ✅
  ([Da Vinci Web](https://ddnavi.com/news/371044/a/),
  [ciatr](https://ciatr.jp/topics/324502),
  [Pixiv百科事典](https://dic.pixiv.net/a/%E6%AA%9C%E4%BD%90%E6%9C%A8%E4%BF%AE%E5%85%B5)).
- **La revista, con datos de la wiki** ✅ ([Bleach Wiki: Seireitei
  Communication](https://bleach.fandom.com/wiki/Seireitei_Communication),
  leída por su API): es **mensual**, la imprime la **Imprenta Reishi**, cuesta
  **380 kan** (el especial de verano, 680), el papel es «100 % reishi» y se
  puede **suscribir para recibirla en casa**. Según Yamamoto, se fundó hace
  **más de mil años para subir la moral** de los shinigami, y antes se
  imprimía con **gariban** (plantillas de papel encerado). Tiene columnas de
  todos: la novela de Ukitake (siempre en el top 3), los haikus de Kira, el
  artículo de Mayuri («sorprendentemente popular»)… y la columna de
  **Hisagi**, que debutó **tercera por la cola**.
- **Sale en el anime, con su minuto** ✅ (subtítulos japoneses con tiempos
  de [kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror),
  y los fotogramas de la wiki):
  - **Ep. 138, 11:00-11:43**: Hisagi le lleva a Ukitake la revista:
    «今月分の『瀞霊廷通信』です» («Aquí tiene el Seireitei Tsūshin de este
    mes»), «あと中に通販目録も» («y dentro, el catálogo de venta por
    correo»). Y se queja: «正直 隊長業務がこんな忙しいなんて知らなかったっす»
    («No sabía que el trabajo de capitán fuera tan pesado»). Traducción mía.
  - **Ep. 305, 4:50-5:28**: Kira le riñe por hacer demasiado: teniente,
    revista y hasta la Asociación de Shinigami Hombres. Hisagi:
    «好きでやってんだから» («Lo hago porque me gusta»), «できる男は辛いんだよ»
    («Ser un hombre capaz es duro») y «仕事ってのはな 損得だけでやるもんじゃねえだろが»
    («El trabajo no se hace sólo por lo que se gana»). **Es su voz para la
    lámina.**
- **«Lo trae un bot»** = la **mariposa infernal** (地獄蝶, jigokuchō): el
  cuerpo **negro**, las alas **moradas con borde negro**. Guían por el
  Senkaimon y **llevan mensajes y órdenes** entre los shinigami; las cuidan
  los **novatos** del Gotei 13 ✅ ([Bleach Wiki: Jigokuchō](https://bleach.fandom.com/wiki/Jigokuch%C5%8D),
  por su API; y Yamamoto la nombra como el correo de antes, en la página de
  la revista). Es el «bot» dentro del mundo.
- **Es noticia ahora mismo**: la **Parte 4, «The Calamity»**, de *Thousand-Year
  Blood War* se emite del **25 de julio al 26 de septiembre de 2026** (10
  episodios). El doblaje en español salió el **29 de agosto** en Hulu, y
  Disney+ lo lleva fuera de EE. UU. ✅
  ([Final Weapon](https://finalweapon.net/2026/08/01/bleach-thousand-year-blood-war-part-4-the-calamity-release-dates-schedule-episodes-hulu/),
  [VIZ](https://www.viz.com/blog/posts/where-to-watch-bleach-thousand-year-blood-war-part-4),
  [OtakuWire](https://otakuwire.net/news/bleach-thousand-year-blood-war-part-4-the-calamity-is-confirmed-to-premiere-in-2026)).
  El final del anime cae **justo esta semana**.
- **La quiere el público latino**: es la tercera del «Big Three» de Shōnen
  Jump. Las otras dos (Naruto y One Piece) ya están tomadas. Tiene doblaje
  latino desde **2010** ✅ ([ANMTV 2010](https://www.anmtvla.com/2010/08/hoy-comineza-el-doblaje-latino-de.html),
  [ANMTV: Eduardo Garza](https://www.anmtvla.com/2010/09/eduardo-garza-asi-se-dobla-bleach.html?m=0)).

### 3.3 ¿Quién presenta? Hisagi (el tema) o Hitsugaya (el más querido)

- **Toshirō Hitsugaya**, capitán de la 10.ª División, fue **1.º** en el
  **4.º concurso oficial de popularidad** de la Shōnen Jump (2008); en el
  3.º quedó 2.º, detrás de Ichigo ✅
  ([Setochan](https://setochan.net/blog-20250824/),
  [kamo2kamo: 4.º](https://kamo2kamo.com/bleach-rank4/),
  [kamo2kamo: 3.º](https://kamo2kamo.com/bleach-rank3/)).
- **Shūhei Hisagi** es el que **hace** la revista. Es menos famoso, pero es
  el personaje correcto para «noticias».
- **Mi propuesta**: **Hisagi** trabajando en la redacción y **Hitsugaya**
  leyendo la revista con cara de fastidio (y **Rangiku**, su teniente,
  asomada por detrás). El más querido sale, y la función queda clara.

**Shūhei Hisagi**
- Trabajador hasta pasarse, cumplidor, algo presumido cuando le sale bien
  («ser un hombre capaz es duro», ep. 305). Le da miedo su propia espada
  (Kazeshini) ⚠️.
- Rasgos que nunca cambian ✅ (vistos en los fotogramas #284 y #303): el
  **«69» tatuado** en la mejilla izquierda, una **franja azul tatuada** que
  le cruza la nariz, **tres cicatrices** verticales sobre el ojo derecho,
  pelo negro de punta, **gargantilla**, uniforme **sin mangas** con la banda
  de teniente en el brazo.
- Imágenes (hoja `p29-bleach`, 847 imágenes grandes de la wiki):

| # | Imagen | Tamaño | Qué hace | Sirve para |
|---|---|---|---|---|
| 282 | [Ep138SeireiteiCommunication.png](https://static.wikia.nocookie.net/bleach/images/a/a3/Ep138SeireiteiCommunication.png) | 1440×1080 | **la portada de la revista**: «月刊 瀞霊廷通信», Yamamoto en portada | el **objeto** |
| 283 | [Ep138SeireiteiCommunicationEditingDepartment.png](https://static.wikia.nocookie.net/bleach/images/e/eb/Ep138SeireiteiCommunicationEditingDepartment.png) | 1440×1080 | **la redacción**: Hisagi agobiado, manos en la cabeza; cartel vertical «瀞霊廷通信編集部» | el **sitio** |
| 284 | [Ep138UkitakeHisagiDiscuss.png](https://static.wikia.nocookie.net/bleach/images/f/fe/Ep138UkitakeHisagiDiscuss.png) | 1440×1080 | Hisagi y Ukitake hablando al aire libre | explicar |
| 303 | [Ep138HisagiDecidesReport.png](https://static.wikia.nocookie.net/bleach/images/b/b7/Ep138HisagiDecidesReport.png) | 1440×1080 | primer plano, **sonrisa con brillos**: decide hacer el reportaje | **celebrar** |
| 250 | [Hisagi Anime Fullbody.png](https://static.wikia.nocookie.net/bleach/images/7/73/Hisagi_Anime_Fullbody.png) | 1050×1500 | cuerpo entero, anime | recortar |
| 2 | [Hisagi's Bankai CFYOW.png](https://static.wikia.nocookie.net/bleach/images/3/31/Hisagi%27s_Bankai_CFYOW.png) | 2168×3952 | boceto de Kubo para la novela | estilo del autor |
| 19 | [CFYOWHisagi demands.png](https://static.wikia.nocookie.net/bleach/images/b/bf/CFYOWHisagi_demands.png) | 1210×2082 | boceto de Kubo, la novela | estilo |

**Toshirō Hitsugaya**
- Frío, serio, bajito, **pelo blanco** de punta y ojos turquesa. El
  **haori blanco** de capitán con el **10** a la espalda, y la espada a la
  espalda ⚠️ (de memoria; se ve en el arte de la hoja).
- **Se enfada si lo tratan de niño** ✅ (subtítulos): en el **ep. 114, 20:47-20:50**,
  Ichigo grita «¡Rangiku-san! ¡Tōshirō!» y él corta: «**日番谷隊長だ**» («Es
  *capitán* Hitsugaya»). En el **ep. 126, 4:31-4:34**: «何べんも何べんも言わせんじゃねえよ!
  日番谷君じゃなくて日番谷隊長だ» («¡No me hagas repetirlo mil veces! No es
  "Hitsugaya-kun", es capitán Hitsugaya»). Es su chiste de siempre.
- Pose: brazos cruzados, o leyendo con una ceja levantada. Con Rangiku:
  [Ep239RangikuBeratesHitsugaya.png](https://static.wikia.nocookie.net/bleach/images/d/d5/Ep239RangikuBeratesHitsugaya.png) (1920×1080), ella le riñe a él.
- Encuestas: los carteles de resultados en color están en la hoja
  ([2.ª](https://static.wikia.nocookie.net/bleach/images/7/73/ACBTBSecond_Popularity_Poll.png), [3.ª](https://static.wikia.nocookie.net/bleach/images/c/c3/209Third_Popularity_Poll_1-5.png), [4.ª](https://static.wikia.nocookie.net/bleach/images/3/30/307Fourth_Popularity_Poll_1-5.png), [5.ª](https://static.wikia.nocookie.net/bleach/images/0/0d/348Fifth_Popularity_Poll.png)).

**Rangiku Matsumoto** ⚠️: pelo naranja ondulado, **bufanda rosa**,
simpática y perezosa. Contrapunto de Hitsugaya.

### 3.4 Doblaje latino

| Personaje | Voz latina | Estado |
|---|---|---|
| **Ichigo Kurosaki** | **Eduardo «Lalo» Garza** (también en *Thousand-Year Blood War*) | ✅ [ANMTV](https://www.anmtvla.com/2010/09/eduardo-garza-asi-se-dobla-bleach.html?m=0), [GamerFocus](https://www.gamerfocus.co/anime/bleach-2022-primer-episodio-doblado-espanol-latinoamerica-voz-ichigo-orihime-lalo-garza/), [Wikipedia](https://en.wikipedia.org/wiki/Eduardo_Garza) |
| Rukia Kuchiki | **Liliana Barba** | ✅ [ANMTV 2022](https://www.anmtvla.com/2022/11/bleach-thousand-year-blood-war-estrena.html), [GamerFocus](https://www.gamerfocus.co/anime/bleach-2022-primer-episodio-doblado-espanol-latinoamerica-voz-ichigo-orihime-lalo-garza/) (según el buscador) |
| **Shūhei Hisagi** | **Edson Matus** (T2-5, T13-15 y TYBW); **Nacho Rodríguez** (T6-12) | ✅ [Doblaje Wiki: Bleach](https://doblaje.fandom.com/es/wiki/Bleach) y [TYBW](https://doblaje.fandom.com/es/wiki/Bleach:_Thousand-Year_Blood_War) (API), que anota el cambio |
| **Toshirō Hitsugaya** | **Luis Fernando Orozco** (T2-16 y TYBW) | ✅ las dos fichas de Doblaje Wiki |
| **Rangiku Matsumoto** | **Irene Jiménez** (T2-16 y TYBW) | ✅ Doblaje Wiki y el buscador |
| Byakuya | Christian Strempler; en TYBW **David Ramos** (Strempler dejó Grupo Macías en 2021) | ✅ Doblaje Wiki |
| Kenpachi | César Arias; en TYBW **José Luis Miranda** (Arias falleció en 2020) | ✅ Doblaje Wiki |

- **Serie original** (2010): producción de **Macias Group**, estudio
  **Famasound**. **Corregido en la segunda pasada**: **Salvador Delgado NO
  dirigió la tanda de 2010**. Su propia ficha de Doblaje Wiki (sección
  «Dirección de doblaje») sólo lo acredita en **Bleach, eps. 230-366
  (2023, Famasound)**, la continuación que se dobló para llegar a TYBW ✅
  ([Doblaje Wiki: Salvador Delgado](https://doblaje.fandom.com/es/wiki/Salvador_Delgado)
  + [ficha de Bleach](https://doblaje.fandom.com/es/wiki/Bleach)). Quién
  dirigió los eps. 1-109 de 2010: no lo encontré ⚠️.
- ***Thousand-Year Blood War***: **Macias Group**, grabado en **MCS**,
  dirección de **Jorge Roig** (partes 1-3) ✅ ([ANMTV](https://www.anmtvla.com/2022/11/bleach-thousand-year-blood-war-estrena.html),
  [ANMTV parte 3](https://www.anmtvla.com/2025/02/bleach-thousand-year-blood-war-disney.html),
  Doblaje Wiki). La **parte 4** la dirige **Pamela Cruz**; traducción de
  **Metzin R. Beyer** ⚠️ (sólo Doblaje Wiki).
- Historia ✅ (Doblaje Wiki): se emitió por **Animax y Sony Spin**
  (2008-2011), primero hasta el ep. 109; se retomó en 2015 (229 episodios) y
  a finales de 2021 se dobló hasta el **366** para preparar TYBW.
- Garza contó que para Ichigo buscó un tono entre el agudo y el grave del
  japonés ⚠️ (una fuente, ANMTV 2010).

### 3.5 Cómo habla en pantalla (el cuadro)

- **El manga de Tite Kubo** ⚠️ (de memoria): mucho **blanco**, fondos casi
  vacíos, negros muy puros; globos finos; y los **poemas** que abren cada
  tomo, en letra grande sobre blanco. Los títulos de capítulo mezclan
  inglés, **español** (los arrancar) y alemán (los quincy).
- **La revista Seireitei Tsūshin** ✅ (fotograma #282, ep. 138): portada
  de revista japonesa de verdad. Cabecera «**月刊 瀞霊廷通信**» en negro
  grueso `#303030`, lema arriba «尸魂界の今を徹底取材！» («¡La Sociedad de
  Almas de hoy, a fondo!»), **fondo melocotón** `#F0B090`, un **retrato en
  portada** (Yamamoto) y **titulares sueltos** en recuadros de color:
  «特集» (especial), «反論！激白！» (¡réplica! ¡confesión!), «女性副隊長が選ぶ
  話題のあのお店！» (la tienda de moda que eligen las tenientes). **Es el
  cuadro del canal**: los textos van como titulares de portada.
- **¡Existe un periódico oficial!** ✅ Para promocionar la parte 2 de
  TYBW, el anime publicó un **«号外 瀞霊廷通信»** (número extra, **2 de
  septiembre de 2023**, «TVアニメ『BLEACH 千年血戦篇』第2号»). En la
  cabecera: «**発行人: 九番隊副隊長 檜佐木修兵**» (editor: Shūhei Hisagi) y
  «発行: 月刊瀞霊廷臨時編集部» ([imagen, 1414×2000](https://i.redd.it/9z3324b26amb1.jpg),
  compartida en [r/bleach](https://reddit.com/r/bleach/comments/169zj5s/new_official_bleach_thousand_year_blood_war/),
  218 votos; con el crédito ©久保帯人/集英社・テレビ東京・dentsu・ぴえろ).
  **Es el modelo perfecto para la lámina**:
  - **cabecera** en un recuadro con borde de rombos, «号外» pequeño y
    «瀞霊廷通信» enorme en negro;
  - **titular vertical gigante** («黒崎一護帰還», «Ichigo Kurosaki
    vuelve»), en negro sobre blanco;
  - una **tabla** de «observación de combates» (quién luchó contra quién);
  - una columna de opinión, «**護廷声人語**» (parodia del «Tensei Jingo» del
    diario *Asahi*);
  - «**編集部員のつぶやき**» (lo que murmuran los redactores);
  - un **anuncio** de la tienda de Urahara;
  - un **sello rojo** «瀞廷編集部» abajo a la izquierda.
  - Colores medidos ✅: papel `#F0F0F0` y gris `#D0D0D0`, tinta `#101010`,
    franjas `#201010`; el rojo del sello ⚠️ (a ojo, `#A0282C`).
  - Traducido a la lámina: «Estrenos» = el titular, «Temporadas» = la
    tabla, «Doblajes» = la columna, «Lo trae un bot» = la firma del editor,
    «Para comentar, abre un hilo» = «lo que murmuran los redactores».
- **El cartel de la redacción** ✅ (#283): tira vertical de papel `#F0EFE7`
  con marco oscuro y el nombre a pincel, «瀞霊廷通信編集部». Oficina de techo
  verde oscuro `#406050` con **fluorescentes**.
- **La mariposa infernal** como «mensajero»: el texto puede ir en una tira
  de papel que lleva la mariposa, o aparecer al posarse.
- **La letra del logo**: la fuente de fans «**Bleach**» (Danilo
  Belardinelli, 2005) es **sólo para uso personal** ✅
  ([FontSpace](https://www.fontspace.com/bleach-font-f13188),
  [FontMeme](https://fontmeme.com/fonts/bleach-logo-font/)). Libres en §8.

### 3.6 Fondo, luz y paleta

- **El Seireitei** ⚠️ (de memoria): muros blancos altísimos, tejados de teja
  gris-azul, calles vacías, cielo muy azul.
- **La redacción** ✅ (#283): **no es tatami**, es una oficina: mesas en fila,
  techo verde con fluorescentes, shinigami con papeles. Mejor que la
  oficina tradicional que imaginé: parece una redacción de verdad.
- Luz: sol fuerte de mediodía y sombras duras; o atardecer naranja.

| Qué | Hex | Origen |
|---|---|---|
| portada de la revista | `#F0B090` | #282 ✅ |
| cabecera de la revista | `#303030` | #282 ✅ |
| cartel de la redacción | `#F0EFE7` | #283 ✅ |
| techo de la redacción | `#406050` | #283 ✅ |
| verde exterior (ep. 138) | `#547A44` | #282 ✅ |
| muros del Seireitei | `#EDEAE3` | ⚠️ a ojo |
| uniforme shinigami (shihakusho) | `#26272D` (negro azulado, no `#121212` puro) | medido con Pillow en [Hisagi Anime Fullbody.png](https://static.wikia.nocookie.net/bleach/images/7/73/Hisagi_Anime_Fullbody.png) (1050×1500) ✅ |
| faja (obi) de Hisagi | `#B3B1AA` | misma imagen ✅ |
| brazalete del 9.º escuadrón | `#BBAE7F` | misma imagen ✅ |
| tarjeta de nombre de TYBW (magenta de campaña) | `#EA006F` | [primer tráiler TYBW, min. 1:00](https://www.dailymotion.com/video/x8c7qz9) ✅ |
| mariposa infernal | cuerpo negro, alas moradas `#5B3B8C` con borde negro | wiki ✅, hex ⚠️ |

- **Texturas reales**: papel de revista satinado, papel washi, tinta sumi.
  Libres (CC0): [tatami_mat](https://polyhaven.com/a/tatami_mat) en Poly
  Haven. **Modelos 3D (CC BY)**: [Shoji Screen](https://sketchfab.com/3d-models/d3dec406af444af7b5025134005a9696)
  de **juyo**; [Japanese Tatami Room Set](https://sketchfab.com/3d-models/8b5108dde0f24f76bda2313750e80134)
  de **juyo**; [Orange Tip Butterfly](https://sketchfab.com/3d-models/e3a1027579e74d84be16340d9d3ac6fb)
  de **wattinstitution** (base para la mariposa, recolorear a negro y
  morado).
- **Vídeos**: [tráiler final de *The Calamity*, subtitulado](https://www.youtube.com/watch?v=7B4rg4rotY0)
  (IGN, 2:01); [teaser oficial de VIZ](https://www.youtube.com/watch?v=ASobpXYYoVQ)
  (2:04); [tráiler de cines de VIZ](https://www.youtube.com/watch?v=DKKZ10FsSBM)
  (0:37: *The Calamity* pasó por cines de EE. UU. el 25 de junio).

### 3.7 Música ⚠️ (de memoria)

- Banda sonora de **Shirō Sagisu**: «**Number One**» (coros solemnes), la
  que todo fan reconoce.
- Openings del **anime viejo (2004-2012)**: «Asterisk» (Orange Range),
  «Ichirin no Hana» (High and Mighty Color) ⚠️. No mezclarlos con TYBW.
- **TYBW, openings y endings por parte** (segunda pasada) ✅ (música de
  **Shirō Sagisu**, el mismo del anime viejo;
  [Wikipedia: Bleach TYBW](https://en.wikipedia.org/wiki/Bleach:_Thousand-Year_Blood_War),
  que cita a Anime News Network y Comic Natalie):

| Parte | Opening | Ending |
|---|---|---|
| 1 · The Blood Warfare (2022) | «Scar», Tatsuya Kitani | «Saihate», SennaRin |
| 2 · The Separation (2023) | «Stars», w.o.d. | «Endroll», Yoh Kamiyama |
| 3 · The Conflict (2024) | «Kotoba ni Sezu Tomo», Six Lounge | «Monochrome», Suisoh |
| 4 · The Calamity (2026, la que se emite ahora) | «I-Bull», Jo0ji | «Rasen», 9Lana |

- Si la lámina cita «el opening actual», es **«I-Bull»**, no «Scar».

### 3.8 Qué NO hacer

- Dibujar a Hisagi **sin el 69** o con las cicatrices en el otro ojo.
- Poner a Hitsugaya sonriendo como un niño feliz: siempre serio.
- Mezclar el estilo del anime viejo (2004-2012, más colores planos) con el
  de TYBW (2022-2026, más contraste y blanco y negro) en la misma lámina.
- Llenar el fondo: Bleach es **aire y blanco**.

### 3.8 bis · Segunda pasada: vídeo, juegos, técnica, cruces y mundo

**Mirado en vídeo, con minuto**: [«Primer tráiler» de TYBW,
subtitulado](https://www.dailymotion.com/video/x8c7qz9?t=60) (2:37,
`fotogramas.py`). Usa **tarjetas de nombre** en blanco y negro de alto
contraste con una **franja magenta** `#EA006F` (medida en el **min. 1:00**).
Es el color de la campaña: sirve para una variante «**noticia de última
hora**» de la lámina, frente a la revista *Seireitei Tsūshin*.

**Fan art (3)**: [tokishima_sikuka en Danbooru](https://danbooru.donmai.us/posts/5787798),
Ichigo, 2736×4096, `rating:g` ✅.

**Fondo de pantalla (16)**: [wallhaven lq3g3p](https://wallhaven.cc/w/lq3g3p),
1920×1200, grupo (Ichigo, Rukia, Byakuya, Renji, Hitsugaya), subido por
**sasukelric** ✅.

**Videojuegos e interfaz (11)**:
- ***Bleach: Rebirth of Souls*** (Tamsoft/Bandai Namco, 2025, PS4/PS5/Xbox/PC):
  el que más cuida el cuadro de diálogo; la Game UI Database cataloga sus
  pantallas de **diálogo con voz**, cinemáticas e **intros de personaje** con
  la letra de trazo grueso de la serie ✅ ([Game UI Database](https://www.gameuidatabase.com/gameData.php?id=2357),
  [Wikipedia](https://en.wikipedia.org/wiki/Bleach_Rebirth_of_Souls)). Es la
  referencia de caja de texto para la lámina, no un cómic genérico.
- ***Bleach: Brave Souls*** (móvil/Steam, gacha 3D): menú lateral de iconos y
  cuadros de **texto blanco sobre panel oscuro semitransparente** ✅
  ([wiki en español](https://bleach-brave-souls.fandom.com/es/wiki/Pantalla_de_Inicio),
  [Wikipedia](https://en.wikipedia.org/wiki/Bleach:_Brave_Souls)).

**Técnica y cómo replicarla (18)**: TYBW la anima **Studio Pierrot** (partes
1-2) y su nueva marca **Pierrot Films** (partes 3-4, con más de un año de
producción y más artistas externos) ✅ ([CBR](https://www.cbr.com/bleach-thousand-year-blood-war-season-3-studio-pierrot-brand/),
[Animehunch](https://animehunch.com/studio-pierrot-launches-new-sub-studio-for-bleach-thousand-year-blood-war/)).
El programa 2D exacto no es público ⚠️.
- **Photoshop**: tinta de **grosor variable por presión** (grueso en el
  contorno, fino en la tela) y **una sola capa de sombra dura** morada o
  azul sobre la piel, sin degradado.
- **Blender**: Freestyle de grosor variable, *toon shader* de 2-3 bandas y
  un **rim light frío** para el brillo del pelo, como en los bankai.

**Texturas 2D (19)**: [Manga Screentone Pack 1](https://assets.clip-studio.com/en-us/detail?id=2142037)
(Clip Studio Assets, gratis, licencia estándar de Clip Studio) ✅: tramas
para la revista y cualquier viñeta.

**Por qué la aman, y qué hace llorar (21)**: en TYBW, la **muerte de Bazz-B**
(ep. 38) frente a Haschwalth, cuando confiesa que nunca se sintió su rival,
es de lo que más ha hecho llorar al fandom ✅ ([Sportskeeda](https://www.sportskeeda.com/anime/bazz-b-s-death-bleach-thousand-year-blood-war-moves-fans-to-tears)).
No es personaje para la lámina, pero es la razón emocional del final.

**Fan dubs (22)** ⚠️ (sin vistas; YouTube bloqueado): «**soy el capitan
hitsugaya (fandub latino)**», que usa el mismo chiste de §3.3 («Es *capitán*
Hitsugaya»); fandubs de peleas de Ichigo («Ichigo vs Aizen», «Ichigo Libera
su Bankai»), uno de 2020 con el fandubber **Alexis Tello**. No hay clip
**oficial doblado** de Hisagi ni de Hitsugaya en Dailymotion ⚠️.

**Cruces (23)**: **Bleach × Fortnite** (anunciado en la Jump Festa, dic.
2025): skins de Ichigo, Rukia, Uryū y Orihime, torneo «Bleach Cup» el
19-dic-2025, tienda desde el 20-dic ✅ ([Vandal](https://vandal.elespanol.com/noticia/1350786043/bleach-aterriza-en-fortnite-ichigo-rukia-y-mas-personajes-del-manganime-combatiran-en-el-battle-royale/),
[LevelUp](https://www.levelup.com/noticia/fortnite-y-bleach-tendran-una-colaboracion-cuando-inicia-y-que-personajes-de-tite-kubo-llegaran-al-battle-royale/),
[Kotaku ES](https://es.kotaku.com/fortnite-amplia-su-universo-con-un-cruce-que-muchos-pedian-llego-la-colaboracion-con-bleach-2000030547)).
Es una **noticia real** para usar de ejemplo dentro de la lámina. Café
temático o UNIQLO: no lo confirmé con fecha ⚠️.

**Obras parecidas e influencias (24)**: Tite Kubo cita **Gegege no Kitaro**
(lo primero que calcó de niño), **Saint Seiya** (armas vistosas) y **Dragon
Ball** («los villanos deben ser fuertes, temibles y geniales») ✅
([CBR](https://www.cbr.com/bleach-tite-kubo-shonen-series-bible-gegege-no-kitaro/),
[VIZ, entrevista](https://www.viz.com/blog/posts/interview-tite-kubo-318)).
En el servidor se le parecen Jujutsu Kaisen, Naruto y One Piece: no repetir
sus ideas.

**El mundo en cinco líneas (25)** ✅ ([Bleach Wiki en español: Gotei 13](https://bleach.fandom.com/es/wiki/Gotei_13)):
1. La **Sociedad de Almas** guía el paso de las almas.
2. Lo hacen los **shinigami** del **Gotei 13**, trece divisiones con capitán.
3. Los **Hollow** son almas corrompidas que devoran otras almas.
4. Cada shinigami lleva una **zanpakutō**; se libera en **shikai** y, sólo
   los capitanes, en **bankai**.
5. Ichigo, humano con poderes de shinigami, entra en ese mundo.
Símbolo: el **rombo** con el número de la división, en la espalda del haori y
en la fachada del cuartel; cada división tiene además su **flor**. El rombo
sirve de **sello** en una esquina de la lámina.

### 3.9 Conceptos de lámina

**Concepto A · La redacción de la 9.ª División** (el recomendado)
- **Objeto real en sitio real**: un **número de la Seireitei Tsūshin**, con
  su portada como en el ep. 138, sobre una **mesa de la redacción** de la
  9.ª División. En **Blender**: la revista, con papel satinado y pliegue; el
  cartel vertical «瀞霊廷通信編集部» detrás.
- **Personaje**: Hisagi al fondo, en la redacción (#283: tal cual,
  agobiado, o #303: orgulloso); Hitsugaya delante, **leyendo la revista**
  con fastidio (porque sale en ella llamado «Hitsugaya-kun»: su chiste).
- **Cómo habla**: los textos del canal son **los titulares** de la revista.
- **Dónde va cada texto**: «Noticias de anime» como cabecera de la revista;
  «Estrenos, temporadas y doblajes» como las tres secciones; «Lo trae un
  bot» junto a la **mariposa infernal posada** en la página; «Para comentar,
  abre un hilo» como pie de página.
- **Que no quede plano**: luz de shōji (luz blanca difusa desde un lado);
  una **mariposa infernal desenfocada** volando delante; el haori de
  Hitsugaya cortado por el borde.

**Concepto C · El número extra (号外)** — la más fácil de leer en el móvil
- **Objeto**: el **号外** impreso, como el oficial de 2023, **clavado en el
  tablón** de la redacción o **en la mano de Hisagi**, que lo reparte.
- **Personaje**: Hisagi con un fajo de periódicos bajo el brazo (pose de
  #303, orgulloso).
- **Cómo habla**: la página entera **es el cuadro**: cabecera, titular
  vertical, tabla y columna (arriba, §3.5).
- **Que no quede plano**: el periódico doblado en perspectiva, con sombra
  real (Blender: plano con pliegue); una mariposa infernal posada en la
  esquina; el sello rojo como único color fuerte.

**Concepto B · La mariposa que trae la noticia**
- **Objeto**: una **tira de papel** doblada que lleva una mariposa infernal
  sobre los tejados del Seireitei.
- **Personaje**: Rangiku alargando la mano para cogerla; Hitsugaya detrás,
  brazos cruzados.
- **Texto**: la tira desplegada con la noticia; el resto en blanco sobre el
  cielo, estilo poema de tomo.
- **Que no quede plano**: atardecer naranja detrás; tejados en primer plano.

---

## 4 · #noticias-gaming → Ralph el demoledor

### 4.1 El canal

Del inventario (sección **NOTICIAS**):

> **ıı・🎮・noticias-gaming** (texto) · 1 fijado — _Videojuegos: salidas,
> parches y presentaciones. Las ofertas van en ofertas-y-gratis._

**Textos de la lámina**:

| # | Texto | Idea |
|---|---|---|
| 1 | **Noticias gaming** | nombre |
| 2 | **Salidas** | juegos que salen |
| 3 | **Parches** | arreglos y actualizaciones |
| 4 | **Presentaciones** | anuncios y tráileres |
| 5 | **Las ofertas van en ofertas-y-gratis** | a dónde no va (el canal de Bob Esponja) |
| 6 | Frase de Ralph o de Félix, en su voz ⚠️ | gancho |

### 4.2 Por qué Ralph

- **Es un salón de videojuegos por dentro.** Los personajes viven en las
  máquinas del **Family Fun Center & Arcade** del señor **Litwak** (abierto
  a principios de los 80), y se juntan en la **Estación Central de Juegos**,
  que **por fuera es una regleta** donde van enchufadas las máquinas ✅
  ([Wreck-It Ralph Wiki: Game Central Station](https://wreckitralph.fandom.com/wiki/Game_Central_Station),
  [Litwak's Arcade](https://wreckitralph.fandom.com/wiki/Litwak%27s_Arcade),
  leídas por su API). Por allí pasan Sonic, los fantasmas de Pac-Man y
  decenas de personajes de juegos reales.
- **Cada palabra del canal ya existe en la película**:
  - **salidas**: el señor Litwak **enchufa una máquina nueva** (Hero's
    Duty) y todos van a verla ⚠️; y la Estación Central **es una estación
    de tren**: su tablero de «salidas» sirve de doble sentido;
  - **parches**: **Félix** arregla todo con su **martillo dorado**; y
    **Vanellope** es un **fallo** del juego (un *glitch*) ⚠️;
  - **presentaciones**: las pantallas de presentación de cada máquina.
- **El diseño está pensado como videojuegos de verdad**: en el mundo de
  Félix «todo tenía que ser en ángulo recto», imitando los píxeles de 8 bits;
  y cada mundo debía sentirse como salir de un cine y entrar en otro ✅
  ([fxguide](https://www.fxguide.com/fxfeatured/wreck-it-ralph/),
  [Medium: A Walt Disney Production](https://filmknife.medium.com/a-walt-disney-production-wreck-it-ralph-a1588f44d8e3)).
- **Latino de verdad**: en la primera película, **Vanellope la dobló «La
  Chilindrina»**, María Antonieta de las Nieves ✅ (ver §4.4). Eso es algo
  que todo latino recuerda.

### 4.3 Los personajes ⚠️ (de memoria, salvo lo marcado)

**Imágenes** (hoja `p29-ralph`, 265 imágenes grandes de la wiki de
*Wreck-It Ralph* en Fandom, por su API):

| # | Imagen | Tamaño | Qué se ve | Sirve para |
|---|---|---|---|---|
| 8 | [Ralph & Vanellope Render 2.png](https://static.wikia.nocookie.net/wreckitralph/images/9/93/Ralph_%26_Vanellope_Render_2.png) | 2042×3056 | **Vanellope sentada en el hombro de Ralph** (render 3D) | el concepto A tal cual |
| 53 | [Game Central Station 02.jpg](https://static.wikia.nocookie.net/wreckitralph/images/c/c6/Game_Central_Station_02.jpg) | 1920×816 | **la Estación Central**: una gran estación con **túneles a cada juego** y encima de cada uno un **letrero de LED rojo** («PAC-MAN») | el **sitio** y el **tablero** |
| 40 | [GameCentralStationConcept.jpg](https://static.wikia.nocookie.net/wreckitralph/images/3/37/GameCentralStationConcept.jpg) | 1600×1233 | concepto de la Estación Central, con haz de luz por los ventanales | luz y color |
| 119 | [Litwak's arcade in WiR2.jpg](https://static.wikia.nocookie.net/wreckitralph/images/4/49/Litwak%27s_arcade_in_WiR2.jpg) | 1678×701 | el **salón de Litwak** de noche, por fuera, con su cartel | fondo del concepto B |
| 121 | [TappersHerosDutyDC.jpg](https://static.wikia.nocookie.net/wreckitralph/images/2/25/TappersHerosDutyDC.jpg) | 1600×729 | Ralph de espaldas en la **taberna de Tapper**; *Hero's Duty* en la pantalla | sala **Juegos** |
| 41 | [WIR8BIT Fullscreen Felix.jpg](https://static.wikia.nocookie.net/wreckitralph/images/5/58/WIR8BIT_Fullscreen_Felix.jpg) | 1600×1200 | fondo oficial **8 bits** de Félix, letra de píxeles «FIX-IT FELIX, JR.» | el **cuadro** de 8 bits |
| 28 | [WIR8BIT Widescreen Vanellope.jpg](https://static.wikia.nocookie.net/wreckitralph/images/f/ff/WIR8BIT_Widescreen_Vanellope.jpg) | 1920×1200 | Vanellope en **8 bits**, fondo fucsia | variante |
| 79 | [FelixNicelandersOutOfOrder2.jpg](https://static.wikia.nocookie.net/wreckitralph/images/7/74/FelixNicelandersOutOfOrder2.jpg) | 1681×787 | Félix y los vecinos ante el lío de **«fuera de servicio»** | **parches** |
| 30 | [Ralph01.jpg](https://static.wikia.nocookie.net/wreckitralph/images/4/40/Ralph01.jpg) | 1556×1421 | Ralph con los **brazos abiertos** (render) | **presentar** |
| 25 | [MainFourPromoPoster1.jpg](https://static.wikia.nocookie.net/wreckitralph/images/6/60/MainFourPromoPoster1.jpg) | 1920×1200 | póster de los cuatro protagonistas | grupo |

**Ralph** — el principal
- El «malo» de *Reparador Félix Jr.*. Grandote, **manos enormes**, pelo
  castaño revuelto, **camisa roja-naranja rota** y **overol**, descalzo.
- Carácter: bruto por fuera, tierno por dentro. Quiere que lo quieran.
- El lema del grupo de apoyo de villanos, **en latino** ✅ ([Doblaje
  Wiki](https://doblaje.fandom.com/es/wiki/Ralph,_el_demoledor), por su API):
  «**Soy malo y eso es bueno. Yo nunca seré bueno y eso no es malo. No hay
  nadie que quiera ser, además de mí.**» (En el 2.º tráiler decía otra cosa
  al final: «No quiero ser nadie más si soy feliz».)
- Poses: puños en alto a punto de golpear; agachado para hablar con
  Vanellope; sentado en su montón de ladrillos.

**Vanellope von Schweetz** — la más querida ⚠️
- De *Sugar Rush* (juego de carreras de dulces). **Sudadera verde menta**,
  falda marrón, medias de rayas, **coleta negra con dulces pegados**.
- Es un **fallo**: parpadea en píxeles de colores cuando se pone nerviosa.
- Burlona, rápida, lista. Le pone apodos a Ralph.

**Reparador Félix Jr.** — el de los parches
- El héroe del juego. **Gorra azul**, cinturón de herramientas, **martillo
  dorado** que arregla lo que toca con un «¡ding!» ⚠️. En el 8 bits oficial
  (#41) lleva camisa **azul claro**; en 3D, comprobar el color en #39 y #79.
- Educadísimo, alegre, habla como de los años 80.

**Sargento Calhoun** — de *Hero's Duty* (juego de disparos): armadura,
pelo rubio corto, dura y seca.

**Sonic** sale en la Estación Central dando **avisos de seguridad** ⚠️. En
*WiFi Ralph* lo dobla **Memo Aponte** ✅ (ver §4.4).

### 4.4 Doblaje latino ✅

**Ralph, el demoledor** (2012):

| Personaje | Voz | Fuentes |
|---|---|---|
| **Ralph** | **Mario Filio** | ✅ [Sitio de Mario Filio](https://mfilio.com/mf/locutor/doblaje/ralph-el-demoledor), [Milenio](https://www.milenio.com/espectaculos/cine/vanellope-voz-chilindrina-ralph-demoledor-2), [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Ralph,_el_demoledor) |
| **Vanellope** | **María Antonieta de las Nieves** («La Chilindrina») | ✅ [Milenio](https://www.milenio.com/espectaculos/cine/vanellope-voz-chilindrina-ralph-demoledor-2), [Sopitas](https://www.sopitas.com/noticias/wifi-ralph-doblaje-mexico-disney-sopitas-memo-aponte-influencers/) |
| **Félix** | **Moisés Iván Mora** | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Mois%C3%A9s_Iv%C3%A1n_Mora), [Fandoblaje Wiki](https://fandoblaje.fandom.com/es/wiki/Mois%C3%A9s_Iv%C3%A1n_Mora) |
| Calhoun | **Rebeca Patiño** | ✅ Doblaje Wiki (API) y el buscador |
| Rey Dulce / Turbo | Roberto Carrillo | ✅ ficha de la película + [su ficha de actor](https://doblaje.fandom.com/es/wiki/Roberto_Carrillo) (segunda pasada) |
| Sr. Litwak | Paco Mauri | ⚠️ sólo Doblaje Wiki |
| **Tapper** | **Mario Castañeda** (el Goku latino) | ✅ Doblaje Wiki; y él mismo dirige el doblaje (abajo) |
| Sonic (1.ª película) | **Yamil Atala** | ⚠️ sólo Doblaje Wiki |

**Estudio**: **Taller Acústico**; **dirección de Mario Castañeda**;
traducción de **Katya Ojeda** (la misma de la película de Mario 2026). Los
diálogos de La Chilindrina se grabaron **en Miami** ✅ (Doblaje Wiki). Ella
cree que la eligieron porque Vanellope se parece de carácter a la
Chilindrina ([entrevista en Cine PREMIERE](https://www.youtube.com/watch?v=yUUtRFo-vAI),
min. 0:25, citada por Doblaje Wiki).

***WiFi Ralph*** (2018), también Taller Acústico con Mario Castañeda:
Ralph otra vez **Mario Filio**; Vanellope pasa a **Liliana Barba** (la
misma Rukia de Bleach); **Sonic, Memo Aponte** (el Phineas original);
**Yesss**, el algoritmo de tendencias, **Erica Edwards** ✅
([Sopitas](https://www.sopitas.com/noticias/wifi-ralph-doblaje-mexico-disney-sopitas-memo-aponte-influencers/),
[Milenio](https://www.milenio.com/espectaculos/cine/vanellope-voz-chilindrina-ralph-demoledor-2)).
Disney **no siguió** con La Chilindrina para la secuela ✅ (Milenio).

> [!note] Duda resuelta
> Una web argentina titula «Franco Escamilla, la voz de Ralph en *Ralph
> rompe Internet*» ([Coop La Lonja](https://cooplalonja.com.ar/franco-escamilla-doblaje-wifi-ralph/)).
> Es un titular confuso: según [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Wifi_Ralph)
> (API, con foto de la grabación), Escamilla dobla a **FN-3181**, un
> soldado de asalto que sale un momento. Ralph sigue siendo Mario Filio ✅.

### 4.5 Cómo habla en pantalla (el cuadro)

- **Los letreros de la Estación Central** ✅ (#53): sobre cada túnel, un
  **letrero negro con letras de LED rojo** con el nombre del juego
  («PAC-MAN»). **Es el cuadro del canal**: cada noticia es un letrero sobre
  un túnel, como un tablero de salidas.
- **La pantalla de 8 bits** ✅ (#41): fondo azul muy oscuro a cuadros
  `#002040`, personaje en píxeles y el nombre en letra de píxeles blanca.
  El «INSERT COIN» parpadeando es ⚠️ de memoria.
- **La marquesina** (el cartel luminoso de arriba de cada máquina), con el
  nombre del juego ⚠️.
- **El tablero de la Estación Central**: letreros de estación de tren, con
  los nombres de los juegos ⚠️.
- **El cartel de «FUERA DE SERVICIO»** que pega el señor Litwak en una
  máquina rota ⚠️: perfecto para «parches».
- **Letras**: *Press Start 2P* o *Silkscreen* para la pantalla; *Bungee*
  para la marquesina (§8).

### 4.6 Fondo, luz y paleta ⚠️

- **El salón de Litwak** de noche, cerrado: sólo la luz de las pantallas.
- **La Estación Central**: una estación de tren enorme, de techo alto, con
  personajes de muchos juegos.

| Qué | Hex | Origen |
|---|---|---|
| salón de Litwak de noche | `#102030` | #119 ✅ |
| muros de la Estación Central | `#605040` | #53 ✅ |
| ventanales de la Estación | `#60B0A0` | #40 ✅ |
| fondo 8 bits oficial | `#002040` | #41 ✅ |
| pantalla de *Hero's Duty* | `#00B0D0` | #121 ✅ |
| LED rojo de los letreros | `#E0302A` | ⚠️ a ojo |
| rosa de *Sugar Rush* | `#FF9CC8` | ⚠️ a ojo |
| sudadera de Vanellope (sombra / luz) | `#5F8C73` / `#79AA8D` (no `#4FC3A1`, que era más turquesa) | medido con Pillow en [Vanellopewirdisney.png](https://static.wikia.nocookie.net/wreckitralph/images/a/ac/Vanellopewirdisney.png) (1728×3000) ✅ |
| medias a rayas de Vanellope | `#60AF90` | misma imagen ✅ |
| carretera arcoíris, franja verde / roja | `#51927C` / `#B27139` | [clip «Ralph vs. Turbo», min. 0:25](https://www.dailymotion.com/video/x39ewi4) ✅ (apagado por la compresión del vídeo) |
| dorado del martillo | `#E8B530` | ⚠️ a ojo |

- **Texturas reales**: vinilo de los laterales de una recreativa, rejilla de
  altavoz, moqueta de salón de juegos, cristal con reflejos.
- **Modelos 3D**: hay una recreativa de *Wreck-It Ralph* en
  [ArtStation Marketplace](https://www.artstation.com/marketplace/p/pBexG/wreck-it-ralph-arcade-cabinet)
  (**de pago**). **Libres (CC BY)** en Sketchfab:
  [Arcade Cabinet](https://sketchfab.com/3d-models/b0cf90709d634eee9b104bd6cb13cb1d)
  de **joshtmc**; [Neo-Geo Arcade Cabinet](https://sketchfab.com/3d-models/8cd460c31df543bb82934468fc4cec19)
  de **johnstone**; y para el tablero, [Split Flap Counter](https://sketchfab.com/3d-models/0bc03ff797b04c0499b4acea003669bb)
  de **JV0211**. Crédito: «<nombre> by <autor> (CC BY 4.0)».
- **Vídeos**: [tráiler oficial](https://www.youtube.com/watch?v=gZBeAqXKq3Q)
  (1:31); [tráiler 2 latino](https://www.youtube.com/watch?v=YM_RL5mHV-k)
  (2:47); [tráiler de *WiFi Ralph* latino](https://www.youtube.com/watch?v=IncCX305XMQ)
  (2:32).

### 4.7 Qué NO hacer

- Dibujar a Ralph **delgado** o con zapatos.
- Poner a Vanellope con el **vestido de princesa** (sólo lo usa un momento;
  ella lo odia).
- Llenar la lámina de logos de juegos reales: en la película salen, pero en
  la lámina se ven como publicidad.

### 4.7 bis · Segunda pasada: frases con minuto, juego, técnica, cruces y mundo

**Frases del doblaje latino, textuales y con minuto (8)** ✅, del [tráiler
oficial latino](https://www.dailymotion.com/video/x8x2a6q) transcrito con
`voz.py` (Whisper) y revisado de oído:
- [**1:32**](https://www.dailymotion.com/video/x8x2a6q?t=92) «Nadie cambia lo que es».
- [**1:38**](https://www.dailymotion.com/video/x8x2a6q?t=98) Vanellope: «Todos dicen que fui una equivocación».
- [**1:44**](https://www.dailymotion.com/video/x8x2a6q?t=104) Ralph: «No voy a dejarte aquí sola».
- [**1:51**](https://www.dailymotion.com/video/x8x2a6q?t=111) «Terminemos recitando la afirmación del villano».
- **1:53-1:58** «¡Soy malo! […] Y eso es bueno. [Yo nunca seré bueno] […] Y
  eso no es malo.» (Whisper oyó «yo camáseré bueno»; la frase completa es la
  de §4.3).
- [**2:01-2:03**](https://www.dailymotion.com/video/x8x2a6q?t=121) «No quiero ser nadie más […] ¡Soy feliz!».
- **Cómo suena Ralph** (`voz.py`): registro medio (**198 Hz**), muy
  expresivo (**29,8 semitonos**), rápido (**3,08 palabras/s**). Habla
  atropellado y con mucho vaivén: bruto por fuera, tierno por dentro.

**Su cara en dos emociones (13)**, fotogramas mirados:
- **Vergüenza aceptada**, [1:53](https://www.dailymotion.com/video/x8x2a6q?t=113):
  sentado y encogido en el círculo del grupo de villanos, brazos cruzados
  sobre las rodillas, hombros caídos.
- **Confundido y dolido**, [2:01](https://www.dailymotion.com/video/x8x2a6q?t=121):
  en la barra de Tapper, **manos abiertas hacia arriba**, cejas juntas, boca
  entreabierta. Sirve para «explicar con angustia».
- Alegría, rabia y miedo francos: no salen de Ralph en el tráiler ⚠️.

**Poses en vídeo (14)**, [clip «Ralph vs. Turbo», Disney XD
latino](https://www.dailymotion.com/video/x39ewi4) (4:10):
- [**0:50**](https://www.dailymotion.com/video/x39ewi4?t=50): Ralph atraviesa
  a puñetazos una estructura de caramelo, cuerpo inclinado: **regañar/pelear**.
- [**2:05**](https://www.dailymotion.com/video/x39ewi4?t=125): Ralph y
  Vanellope por la **carretera arcoíris**, ella señalando al frente:
  **explicar o animar en pareja**.

**Doblaje (8)**: **Roberto Carrillo** es el Rey Dulce/Turbo ✅ ([su ficha](https://doblaje.fandom.com/es/wiki/Roberto_Carrillo)).
Paco Mauri (Litwak) y Yamil Atala (Sonic): sus fichas de actor **no** listan
el papel ⚠️ (posible error de atribución; no confirmar).

**Música (9)**: **Henry Jackman**; canciones de **Owl City**, **AKB48** y
**Skrillex** ⚠️ (una fuente: [Wikipedia](https://en.wikipedia.org/wiki/Wreck-It_Ralph)).

**Lo que ama el fandom (12, 21)**: «Soy malo y eso es bueno» se repite fuera
de contexto como lema; y **La Chilindrina como Vanellope** es el dato de
doblaje más comentado en México (Milenio, §4.4) ✅.

**Gustos (20)**: Vanellope vive en un juego de **dulces**; su kart lo arma
ella misma con dulces del juego, y el **volante** es su objeto de siempre ✅
([Wreck-It Ralph Wiki](https://wreckitralph.fandom.com/wiki/Vanellope_von_Schweetz), API).

**Fan art (3)**: [juanmao en Danbooru](https://danbooru.donmai.us/posts/3152497),
Vanellope, 2048×1328 ✅. **Fondo de pantalla (16)**: [wallhaven 45k535](https://wallhaven.cc/w/45k535),
3840×2160, cartel de 2012, subido por **JosephTeAu** ✅.

**Videojuego e interfaz (11)**: *Wreck-It Ralph* (iOS, Disney
Interactive/Activision, 2012), en la **Estación Central**, con tres
minijuegos: **Fix-It Felix Jr.** (8 bits), **Hero's Duty** (HUD militar) y
**Sugar Rush** (kart en rosa) ✅ ([Arcade Heroes](https://arcadeheroes.com/2012/10/18/taking-a-look-at-two-fantasy-arcade-titles-from-disneys-wreck-it-ralph/),
[wiki: Sugar Rush](https://wreckitralph.fandom.com/wiki/Sugar_Rush)). Tres
interfaces en un juego: buena idea para una lámina 2 de #noticias-gaming.

**Técnica y cómo replicarla (18)**: Walt Disney Animation Studios. Ralph
(2012) **no** usó **Hyperion**, que llegó con *Big Hero 6* (2014); la
secuela de 2018 sí ✅ ([ACM](https://dl.acm.org/doi/fullHtml/10.1145/3182159),
[Disney Animation](https://disneyanimation.com/technology/hyperion/)). La
herramienta **Meander** es del corto *Paperman*, no de Ralph ⚠️.
- **Blender**: el 8 bits de Félix con **píxeles reales** (textura pequeña,
  interpolación *Closest*), no con filtros. Los caramelos de Sugar Rush:
  colores saturados y un falso *subsurface* (difuso + translúcido).

**Texturas 2D (19)**: packs de **pixel art CC0** en [itch.io](https://itch.io/game-assets/free/tag-cc0/tag-pixel-art)
para los letreros LED y las recreativas ⚠️ (listado general: comprobar la
licencia del pack elegido).

**Cruces y figuras (23)**: la escena de las **princesas Disney** con
Vanellope en *Ralph Breaks the Internet* (2018) es el cruce más citado ✅
([Den of Geek](https://www.denofgeek.com/movies/ralph-breaks-the-internet-disney-princesses-scene/),
[Critical Media Project](https://criticalmediaproject.org/wreck-it-ralph-2-ralph-breaks-the-internet-vanellope-meets-disney-princess/)).
Ralph y Vanellope tuvieron **figura física** en **Disney Infinity** ✅
([Disney Wiki](https://disney.fandom.com/wiki/Vanellope_von_Schweetz)).

**Obras parecidas (24)**: «*Toy Story* rehecho para la generación de los
videojuegos» ✅ ([TIME](https://entertainment.time.com/2012/11/01/wreck-it-ralph-toy-story-with-avatars/),
[Movie Smackdown](http://www.moviesmackdown.com/2012/11/wreck-it-ralph-vs-toy-story/)).
Cerca en tono: *Free Guy* (2021) y *Turbo* (DreamWorks, 2013).

**El mundo en cinco líneas (25)** ✅ ([wiki: Game Central Station](https://wreckitralph.fandom.com/wiki/Game_Central_Station)):
1. Cuando cierra **Litwak's Arcade**, los personajes de los juegos viven.
2. Viajan por los cables hasta la **Estación Central**, que por fuera es una
   **regleta de corriente**.
3. Allí conviven Sonic, los fantasmas de Pac-Man, Q*bert…
4. Perder una vida y volver a aparecer es **regenerar**.
5. Un juego sin su personaje queda «**fuera de servicio**».
Vocabulario: **Turbo** («usurpar un juego ajeno»), **glitch** (el «fallo» de
Vanellope), **regenerar**, «fuera de servicio».

### 4.8 Conceptos de lámina

**Concepto A · Los letreros de la Estación Central** (el recomendado)
- **Objeto real en sitio real**: los **letreros de LED rojo** que hay sobre
  cada túnel de la **Estación Central de Juegos** (#53). Tres túneles:
  «SALIDAS», «PARCHES», «PRESENTACIONES». Si se quiere más «tablero», un
  panel de letras que giran (tipo Solari). En **Blender**: los letreros son
  cajas con una textura de puntos que brilla.
- **Personaje**: Ralph mirando los letreros hacia arriba, con Vanellope
  **sentada en su hombro** señalando (el render **#8** es justo esa pose).
- **Cómo habla**: el texto **es el tablero**. Tres filas: «SALIDAS»,
  «PARCHES», «PRESENTACIONES», con un andén cada una.
- **Dónde va cada texto**: «Noticias gaming» en el cartel de la estación;
  las tres palabras en el tablero; «Las ofertas van en ofertas-y-gratis»
  como un **letrero de desvío** con una flecha.
- **Que no quede plano**: luz fría de estación arriba, luz de colores de las
  pantallas abajo; **un personaje de otro juego pasando delante**,
  desenfocado.

**Concepto B · La máquina nueva llega al salón**
- **Objeto**: una **recreativa nueva** con un lazo, recién enchufada en el
  salón de Litwak de noche, y otra con el cartel «FUERA DE SERVICIO».
- **Personaje**: Félix con el **martillo alzado** arreglando la rota;
  Ralph apoyado en la nueva.
- **Texto**: las noticias en la **pantalla** de la nueva, en letra de 8 bits.
- **Que no quede plano**: la pantalla es la única luz; brillo en la cara de
  Ralph; el cable de la regleta en primer plano.

---

## 5 · #general-doblaje → Monsters, Inc. (y Monsters University)

### 5.1 El canal

Del inventario (sección **EL ESTUDIO**):

> **ıı・💬・general-doblaje** (texto) · 1 fijado · **14 de personas en los
> últimos 15** — _Del oficio: micros, voces, técnica y dudas de novato. Tu
> voz grabada va a demos; los papeles, a castings._

Es de los canales **más vivos** del servidor. La lámina se verá mucho.

**Textos de la lámina**:

| # | Texto | Idea |
|---|---|---|
| 1 | **General doblaje** | nombre |
| 2 | **Del oficio** | de qué se habla |
| 3 | **Micros, voces, técnica y dudas de novato** | los cuatro temas |
| 4 | **Tu voz grabada va a demos** | a dónde no va (Evangelion) |
| 5 | **Los papeles, a castings** | a dónde no va (Oshi no Ko) |
| 6 | Frase de Mike, en su tono de entrenador ⚠️ | gancho |

### 5.2 Por qué Monsters, Inc.

- **Es una película sobre un oficio de la voz.** Los monstruos trabajan en
  una fábrica donde **el grito se recoge en un tanque**: la puerta, el
  susto, el grito, el tanque que se llena ⚠️ (de memoria; es la premisa).
  Es **grabar la voz** dentro del mundo de la serie.
- **Técnica y dudas de novato** = ***Monsters University***: Mike estudia
  para ser asustador, se sabe toda la teoría y aprende que la técnica no
  basta ⚠️ (de memoria). Es el novato de #general-doblaje.
- **El doblaje latino es leyenda**: Mike lo hizo **Andrés Bustamante**
  («el Güiri Güiri»), en **su primer trabajo de doblaje**, y Sulley **Víctor
  Trujillo** («Brozo»), amigos en la vida real como sus personajes ✅ (ver
  §5.4). Y **Roz** es de **Humberto Vélez**, el Homero Simpson latino.
- **Diseño**: la fábrica sale de la **América de posguerra** y el *baby
  boom*: la empresa creció en la «edad de oro» de los niños que asustar ✅
  ([Disney Wiki](https://disney.fandom.com/wiki/Monsters,_Inc.),
  [Wikipedia](https://en.wikipedia.org/wiki/Monsters,_Inc.)). Diseño de
  producción: **Harley Jessup** y **Bob Pauley**; dirección de arte: **Tia
  W. Kratter** y **Dominique Louis** ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Monsters,_Inc.),
  [TMDB](https://www.themoviedb.org/movie/585-monsters-inc/cast)).
- **Cada puerta es única**: forma, flores y colores elegidos uno a uno para
  que no haya dos iguales ✅ (una fuente, Disney Wiki) — como cada voz.

### 5.3 Los personajes ⚠️ (de memoria, salvo lo marcado)

**Imágenes** (hoja `p29-monsters-inc`, 132 imágenes grandes de la wiki de
Pixar en Fandom, por su API; ✅ vistas una a una):

| # | Imagen | Tamaño | Qué se ve | Sirve para |
|---|---|---|---|---|
| 66 | [Monsters Inc Screen 006.png](https://static.wikia.nocookie.net/pixar/images/5/56/Monsters_Inc_Screen_006.png) | 1920×1036 | **Mike con casco y carpeta en el panel de la estación**; puerta amarilla en su marco; tanque amarillo enchufado; «F5» pintado en la persiana | el **sitio** y la pose de **explicar** |
| 74 | [Mike and Sulley 002.jpg](https://static.wikia.nocookie.net/pixar/images/9/95/Mike_and_Sulley_002.jpg) | 1800×973 | Mike con la **tablilla**, pulgar arriba; tanques apilados; Sulley apoyado; la puerta de Boo | **presentar** |
| 56 | [Roz2.jpg](https://static.wikia.nocookie.net/pixar/images/b/b6/Roz2.jpg) | 1920×1040 | **Roz en su ventanilla**, cartel «IT'S MY WAY OR THE HIGHWAY» | **regañar** (fondo) |
| 61 | [Monsters inc logo by ethancartoons-dbpqug6.png](https://static.wikia.nocookie.net/pixar/images/b/bd/Monsters_inc_logo_by_ethancartoons-dbpqug6.png) | 1920×1038 | **título de apertura**: fondo negro, marco de **puertas de colores** dibujadas, «MONSTERS, INC.» en blanco | letra y color de cartel |
| 67 | [01 Mike and Sulley Rookie Card.jpg](https://static.wikia.nocookie.net/pixar/images/a/a8/01_Mike_and_Sulley_Rookie_Card.jpg) | 1600×1106 | **cromo de «novatos del año»** de Mike y Sulley, con su **récord de sustos** | idea de ficha / lámina 2 |
| 25 | [Monsters scare floor.jpg](https://static.wikia.nocookie.net/pixar/images/6/69/Monsters_scare_floor.jpg) | 3000×1622 | **el Piso de Sustos** entero, los asustadores en fila | panorámica |
| 16 | [MikeWazowski.png](https://static.wikia.nocookie.net/pixar/images/0/08/MikeWazowski.png) | 2612×2998 | Mike universitario **con libros** | **dudas de novato** |
| 39 | [Professor Knight with Mike.jpg](https://static.wikia.nocookie.net/pixar/images/1/11/Professor_Knight_with_Mike.jpg) | 1920×1080 | el **profesor Knight** con Mike | **Aula** |
| 2 | [MI Textless 02.jpg](https://static.wikia.nocookie.net/pixar/images/a/a8/MI_Textless_02.jpg) | 4033×5000 | póster sin texto: Sulley y Mike asomados a una puerta | portada |

**Mike Wazowski** — el recomendado para hablar
- Verde, redondo, **un solo ojo** grande, cuernitos. Es el **entrenador**
  de Sulley: le lleva los números, el papeleo y la técnica.
- Habla rápido, gesticula con todo el cuerpo, se da importancia, bromea.
- En *Monsters University* es el alumno que **se sabe todos los libros**.
- En *Monsters at Work* (Disney+) da **clases de comedia** a los nuevos ⚠️.
- Poses: con una **tablilla** (clipboard) y lápiz; con el brazo levantado
  dando órdenes; a hombros de Sulley.

**James P. Sullivan «Sulley»** — el grandote
- Azul turquesa con **manchas moradas**, enorme, bonachón. El mejor
  asustador. Con Boo se vuelve tierno.

**Roz** — la de la ventanilla
- Una babosa gris con gafas y labios rojos, detrás de la ventanilla de
  papeleo. Seca, lenta, **vigila a Mike**. Es un meme en latino: «¿No
  ordenaste tu papeleo anoche?» y «Cuidadito, Wazowski» ⚠️ (comprobar el
  texto exacto en la escena; lo recogen vídeos de TikTok:
  [«no ordenaste tu papeleo»](https://www.tiktok.com/discover/monsters-inc-no-ordenaste-tu-papeleo),
  [«cuidadito Wazowski»](https://www.tiktok.com/discover/cuidadito-wazowski-original?lang=en)).

**Boo** — la niña: coletas, camisón rosa, lo llama «**¡Gatito!**» ✅. En
latino la doblaron **Alicia Vélez** y **Mariana Lodoza**, con 2 y 3 años:
sólo se oyen en las palabras claras («Gatito», lo que canta en el baño);
los balbuceos y el «Mike Wazowski» son del audio en inglés ✅ ([Doblaje
Wiki](https://doblaje.fandom.com/es/wiki/Monsters,_Inc.), por su API).

**Randall** — el villano camaleón morado (voz latina: **Moisés
Palacios**). Al final, una familia lo confunde con un **pejelagarto**: es
un chiste **sólo del doblaje mexicano** ✅ (Doblaje Wiki).
**Decana Hardscrabble** — la de MU, alas de ciempiés, temible (voz latina:
**Rebeca Manríquez**); **profesor Knight** (**Gabriel Pingarrón**) ✅
(Doblaje Wiki, ficha de MU).

### 5.4 Doblaje latino

| Personaje | Voz | Estado |
|---|---|---|
| **Mike** (película, MU, cameo en *Cars*, corto, espectáculo sobre hielo) | **Andrés Bustamante** | ✅ [Doblaje Wiki: Mike Wazowski](https://doblaje.fandom.com/es/wiki/Mike_Wazowski), [Milenio](https://www.milenio.com/espectaculos/cine/victor-trujillo-sus-personajes-de-doblaje), [Doblaje Wiki: Monsters, Inc.](https://doblaje.fandom.com/es/wiki/Monsters,_Inc.) |
| **Sulley** | **Víctor Trujillo** | ✅ [Milenio](https://www.milenio.com/espectaculos/cine/victor-trujillo-sus-personajes-de-doblaje), [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Monsters,_Inc.) |
| **Roz** | **Humberto Vélez** (se inspiró en la voz de una delegada de la ANDA) | ✅ dos fuentes flojas: [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Monsters,_Inc.) y [TikTok «Roz latino»](https://www.tiktok.com/discover/roz-monsters-inc-latino) |
| Mike en *Monsters at Work* | **Erick Salinas** (Bustamante no volvió) | ✅ [Doblaje Wiki: Mike](https://doblaje.fandom.com/es/wiki/Mike_Wazowski), [DubDB](https://dubdb.fandom.com/wiki/Monsters_at_Work_(Latin_American_Spanish)) |
| Sulley en *Monsters at Work* | **Gerardo Vásquez** (Trujillo tampoco volvió) | ⚠️ sólo Doblaje Wiki |
| Tylor (el novato de *Monsters at Work*) | Jerry Velázquez | ⚠️ sólo Doblaje Wiki |

Erick Salinas ya había hecho a Mike en los tráileres de MU y en *Disney
Infinity* ✅ (las mismas dos fuentes).

**Estudios** ✅ (Doblaje Wiki, por su API):
- *Monsters, Inc.* (2001): **Taller Acústico**, dirección de **Ricardo
  Tejedo**, traducción de Raúl Aldana. Fue **la primera de Pixar** doblada
  en Taller Acústico; desde entonces ahí se doblan todas las de Disney para
  cines.
- *Monsters University* (2013): **Taller Acústico**, dirección de **Mario
  Castañeda**.
- *Monsters at Work* (2021): **Diseño en Audio (DNA)**, dirección de
  **Cristina Hernández**.
- La película ganó el **Óscar a mejor canción** («If I Didn't Have You»,
  de Randy Newman) ✅ (Doblaje Wiki).
- En la versión latina se **quitaron textos en pantalla**: el lema «We Scare
  Because We Care» y el cartel de «asustador del mes» se cambiaron por el
  nombre de la empresa ✅ (Doblaje Wiki). → En la lámina, **no poner el
  lema en inglés**.

**La escena del papeleo** (vídeos cortos de fans con el audio latino):
[«No ordenaste tu papeleo anoche»](https://www.youtube.com/watch?v=RmuKNpavYbs)
(0:38), [todas las escenas de Roz en latino](https://www.youtube.com/watch?v=uAtoPg7-fkE)
(3:51), [«Cuídate, Wazowski… cuidadito»](https://www.youtube.com/watch?v=fAQRH05VQrI)
(0:06). YouTube no dejó bajar subtítulos para dar el minuto exacto.

### 5.5 Cómo habla en pantalla (el cuadro)

- **La tablilla de Mike** ✅ (#74; en #66 es una **carpeta naranja**): el
  «cuaderno» del entrenador.
- **El marcador de asustadores** del Piso de Sustos: una pizarra con los
  nombres y los puntos ⚠️. Sirve para destacar «técnica».
- **La ventanilla de Roz** ✅ (#56): cristal, oficina verde llena de
  papeles, y un cartel pegado: «IT'S MY WAY OR THE HIGHWAY». En la lámina,
  ese cartel se puede **traducir** («A mi manera o a la calle») o poner la
  regla del canal.
- **Los créditos iniciales** ✅ ([Art of the Title](https://www.artofthetitle.com/title/monsters-inc/);
  fotograma #61): fondo **negro**, un marco de **puertas planas de colores**
  dibujadas a mano (amarillo `#F0D030`, verde lima `#B0F060`, naranja
  `#F0A020`, granate `#800030`, verde `#30D060`), y el título en blanco con
  una serif caprichosa. Estilo de cartel de los años 60.
- **Letras**: el logo es propio (no libre). Para la fábrica de posguerra,
  una geométrica tipo Futura: **Jost** (§8).

### 5.6 Fondo, luz y paleta ⚠️

- **El Piso de Sustos** ✅ (#66, #74, #25): una nave larga con **estaciones**
  en fila. Cada una tiene la **puerta** en un marco metálico con una **luz
  roja arriba**, un **panel de botones** a un lado, el **tanque** de gritos
  enchufado con una mirilla, y el **número de estación pintado** en la
  persiana de detrás («F5», «F6»). Mike lleva **casco azul** de trabajo.
- La **ciudad de Monstruópolis** de día; la **bóveda de puertas** (millones
  de puertas colgando en raíles).
- **MU**: campus universitario, ladrillo y hiedra, el aula en gradas.

| Qué | Hex | Origen |
|---|---|---|
| tanque de gritos | `#F0A050` | #66 ✅ |
| puerta amarilla | `#D0B060` | #66 ✅ |
| persiana del Piso de Sustos | `#6060A0` / `#505080` | #66 ✅ |
| suelo del Piso de Sustos | `#404060` | #66 ✅ |
| casco de Mike | `#5080A0` | #66 ✅ |
| piel de Mike (sombra / luz) | `#5C7531` / `#87A851` (no `#9BCB3C`) | medido en [MikeMAW.png](https://static.wikia.nocookie.net/pixar/images/9/96/MikeMAW.png) (763×775) ✅ |
| iris de Mike | `#375B5B` | misma imagen ✅ |
| pelaje de Sulley (sombra / luz) | `#2C7D74` / `#559C94` (verde azulado, no `#3AB4E8`) | medido en [SulleyMAW.png](https://static.wikia.nocookie.net/pixar/images/e/e7/SulleyMAW.png) (939×1268) ✅ |
| manchas de Sulley | `#234163` (azul-morado oscuro, no `#8A4FBF`) | misma imagen ✅ |
| otra puerta: roja en sombra / piloto encendido | `#42030E` / `#BC010C` | [tráiler de 2001, min. 0:45](https://www.dailymotion.com/video/x889mq6) ✅ |
| luz roja de puerta activa | `#E0402E` | ⚠️ a ojo |

- **Texturas reales**: chapa pintada, linóleo, papel de formulario, metal
  cepillado del tanque.
- **Modelos 3D libres** (Sketchfab, **CC BY**, se pueden bajar):
  [Monsters INC. scream canister](https://sketchfab.com/3d-models/6c270b8def2b4303869ec14484f2ab05)
  de **martinjohnsrud**; [Monsters Inc. Scream Canister](https://sketchfab.com/3d-models/bb2934a92ee3470d89c1b12701893a9a)
  de **Narizeki**; [Monsters Inc. Door rail](https://sketchfab.com/3d-models/6af1a34a634e414290e8b0496e756674)
  de **fordemekhi96**; [Document Clipboard with Pen](https://sketchfab.com/3d-models/8650234a2e7949ca9fe9b4124e000d97)
  de **kuroderuta**. Crédito: «<nombre> by <autor> (CC BY 4.0)». Ojo: la
  puerta de Boo que hay en Sketchfab es **no comercial** (NC).
- Hay también un proyecto del **Piso de Sustos en Blender** en
  [Blender Artists](https://blenderartists.org/t/monsters-inc-scare-floor/600073)
  (referencia de construcción; no dice licencia libre).
- Texturas libres (CC0, Poly Haven): [metal_plate](https://polyhaven.com/a/metal_plate),
  [blue_metal_plate](https://polyhaven.com/a/blue_metal_plate) para la
  estación y la persiana.

### 5.7 Qué NO hacer

- Poner a **Sulley** a hablar del oficio: el entrenador es Mike.
- Dar miedo de verdad: el tono es comedia de oficina.
- Mezclar las rayas de Sulley: son **manchas**, no rayas.

### 5.8 Conceptos de lámina

**Concepto A · La estación del Piso de Sustos** (el recomendado)
- **Objeto real en sitio real**: una **estación** del Piso de Sustos, con
  su **puerta**, su **tanque de gritos** y el panel. En **Blender**: el
  tanque (cilindro de cristal y metal) y la puerta son fáciles.
- **Personaje**: **Mike con la tablilla**, explicando (pose de #66 o
  #74); Sulley detrás, haciendo calentamiento de voz.
- **Cómo habla**: el texto va en la **tablilla** de Mike y en el **panel** de
  la estación.
- **Dónde va cada texto**: «General doblaje» en el cartel sobre la estación;
  «Micros, voces, técnica y dudas de novato» como cuatro filas de la
  tablilla; «Tu voz grabada va a demos» en un **tanque lleno** con una
  flecha; «Los papeles, a castings» en la **ventanilla de Roz** al fondo.
- **Que no quede plano**: la luz de la puerta encendida (roja) da en la cara
  de Mike; el tanque delante, con reflejo; Roz al fondo, desenfocada.

**Concepto B · El aula de Monsters University** (para las dudas de novato)
- **Objeto**: la **pizarra** del aula en gradas y los apuntes de Mike.
- **Personaje**: Mike en primera fila, levantando la mano con una duda.
- **Texto**: la pizarra con los cuatro temas; la duda de Mike en su libreta.
- **Que no quede plano**: luz de ventanal; pupitres en primer plano.

---

## 6 · #canto → Sing: ¡Ven y canta!

### 6.1 El canal

Del inventario (sección **EL ESTUDIO**):

> **ıı・🎵・canto** (texto) · 1 fijado — _Hablar de cantar. Tus covers van a
> demos-canto, un hilo por cover._

Vecino: **#demos-canto** ya tiene lámina de **Bocchi the Rock!** (con el
teclado en la lámina 2). #canto es para **hablar**; #demos-canto para
**enseñar** lo grabado.

**Textos de la lámina**:

| # | Texto | Idea |
|---|---|---|
| 1 | **Canto** | nombre |
| 2 | **Hablar de cantar** | para qué es |
| 3 | **Técnica, nervios, repertorio** ⚠️ (propuesta mía: los temas típicos) | de qué se habla |
| 4 | **Tus covers van a demos-canto** | a dónde no va |
| 5 | **Un hilo por cover** | la regla de allá |
| 6 | Frase de Buster Moon, animando ⚠️ | gancho |

### 6.2 Por qué Sing

- **Es una película sobre aprender a cantar en público.** Un koala, **Buster
  Moon**, organiza un **concurso de canto** para salvar su teatro. Cada
  concursante tiene su problema: nervios, timidez, falta de tiempo, un
  padre que no lo entiende ⚠️ (de memoria). Son las mismas dudas del canal.
- **Tiene un objeto que todos recuerdan**: el **volante de la audición**.
  Al escribirlo, a la señora **Crawly** (una iguana mayor) se le cae el
  **ojo de cristal** sobre el teclado, pulsa dos veces el 0, y el premio
  sale de **100.000 dólares** en lugar de 1.000. El ventilador lo echa por
  la ventana y vuela por toda la ciudad ✅
  ([Universal Studios Wiki](https://universalstudios.fandom.com/wiki/Miss_Crawly),
  [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/WesternAnimation/SingIllumination),
  [Sing Wiki](https://sing.fandom.com/wiki/Miss_Crawly),
  [la escena en YouTube](https://www.youtube.com/watch?v=KV5ARyNjGhY)).
- **El doblaje latino lo hicieron cantantes latinos famosos** (ver §6.4):
  **Benny Ibarra**, **Ha\*Ash**, y en la segunda, **Chayanne**. Para un canal
  de canto hispano, no hay mejor gancho.
- **Sigue viva**: *Sing 3* está confirmada y en desarrollo (Chris Meledandri
  lo repitió en **junio de 2026**); una fuente la pone el **8 de diciembre de
  2027** ⚠️ ([Screen Rant](https://screenrant.com/sing-3-updates/),
  [IMDb](https://www.imdb.com/title/tt29434162/),
  [Wikipedia: Sing (franchise)](https://en.wikipedia.org/wiki/Sing_(franchise))).

### 6.3 Los personajes ⚠️ (de memoria, salvo lo marcado)

**Imágenes** (hoja `p29-sing`: la wiki de *Sing* en Fandom tiene **1.398
imágenes grandes**, muchas en 4K; ✅ vistas y medidas):

| # | Imagen | Tamaño | Qué se ve | Sirve para |
|---|---|---|---|---|
| 58 | [Sing-production-art-moon-theater-exterior-front-gregory-georges.jpg](https://static.wikia.nocookie.net/singmovie/images/e/ef/Sing-production-art-moon-theater-exterior-front-gregory-georges.jpg) | 2000×1124 | **fachada del Teatro Moon** (arte de producción de **Gregory Georges**): barroco blanco con liras, **reloj sobre la marquesina** de letras sueltas, alfombra roja | el **sitio** (A) |
| 122 | [Moon Theater - lines.png](https://static.wikia.nocookie.net/singmovie/images/7/77/Moon_Theater_-_lines.png) | 1920×1090 | vista aérea: la **fila de audiciones** por la calle; marquesina «**OPEN AUDITIONS**» y el cartel vertical «**MOON**» | sala **Karaoke** |
| 61 | [Sing-production-art-moon-theater-stage-gregory-georges.jpg](https://static.wikia.nocookie.net/singmovie/images/3/34/Sing-production-art-moon-theater-stage-gregory-georges.jpg) | 2000×1124 | **el escenario**: telón rojo con flecos dorados, nubes de cartón, suelo de madera, **micro de pie** (Georges) | concepto B, sala **Escenario** |
| 59 | [Sing-production-art-moon-theater-interior-gregory-georges.jpg](https://static.wikia.nocookie.net/singmovie/images/f/fe/Sing-production-art-moon-theater-interior-gregory-georges.jpg) | 2000×1124 | **la sala por dentro**: paredes rojas, arcos, palcos, bombillas (Georges) | fondo |
| 580 | [Eddie Sees The Yellow Flyer.jpg](https://static.wikia.nocookie.net/singmovie/images/c/c2/Eddie_Sees_The_Yellow_Flyer.jpg) | 1680×897 | Eddie encuentra el **volante amarillo** | el **objeto** |
| 653 | [Prize In There.png](https://static.wikia.nocookie.net/singmovie/images/f/ff/Prize_In_There.png) | 1675×897 | Buster con el **cofre del premio** | gancho |
| 198 | [Meena sings Don't You Worry bout a Thing.jpeg](https://static.wikia.nocookie.net/singmovie/images/3/3e/Meena_sings_Don%27t_You_Worry_bout_a_Thing.jpeg) | 1920×1080 | **Meena canta «Don't You Worry 'bout a Thing»** | **celebrar** |
| 1 | [Sing-meena-tori-kelly.jpg](https://static.wikia.nocookie.net/singmovie/images/8/89/Sing-meena-tori-kelly.jpg) | 8636×4452 | Meena, render oficial | recortar |
| 2 | [Sing-buster-matthew-mcconaughey.jpg](https://static.wikia.nocookie.net/singmovie/images/8/86/Sing-buster-matthew-mcconaughey.jpg) | 8019×4133 | Buster Moon con micro, render oficial | **presentar** |
| 47 | [Sing 2 Poster (Meena).jpg](https://static.wikia.nocookie.net/singmovie/images/7/70/Sing_2_Poster_%28Meena%29.jpg) | 1440×1800 | póster de *Sing 2* de Meena, espejo de camerino con bombillas | camerino |
| 39 | [Bustermoonandmscrawly 0792.JPG](https://static.wikia.nocookie.net/singmovie/images/0/0b/Bustermoonandmscrawly_0792.JPG) | 3600×1946 | Buster y la señora Crawly | la del ojo de cristal |

**Meena** — la recomendada para #canto
- Una **elefanta adolescente** con una **voz enorme** y **pánico
  escénico**. Se esconde detrás del telón. Al final canta y todos se
  callan.
- Es la que representa a quien **empieza** en el canal: la que canta bien
  pero no se atreve.
- Poses: detrás del telón, **asomando** con las manos juntas; en el
  escenario, **ojos cerrados**, micro en la mano, cantando con todo.
- Canciones que se le asocian: «**Don't You Worry 'bout a Thing**» (Stevie
  Wonder), la del final ✅ (fotograma #198 de la wiki, con ese título) y
  «Hallelujah» (Leonard Cohen) ⚠️ (de memoria).

**Buster Moon** — el que presenta
- Koala pequeño, traje y **pajarita**, optimista hasta el absurdo. Dueño del
  **Teatro Moon**. Nunca se rinde.
- Poses: brazos abiertos en el escenario; subido a una silla para
  alcanzar el micro; con el **volante** en la mano.

**Johnny** (gorila, del piano), **Ash** (puercoespín rockera), **Rosita**
(cerdita, madre de 25), **Mike** (ratón, crooner arrogante), **Gunter**
(cerdo bailarín) ⚠️.

### 6.4 Doblaje latino ✅

| Personaje | Voz latina | Fuentes |
|---|---|---|
| **Buster Moon** | **Benny Ibarra** | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Sing_%C2%A1Ven_y_canta!) (API), [Espinof](https://www.espinof.com/netflix/sing-2-chayanne-a-ha-ash-estos-actores-cada-personaje-su-doblaje-latinoamericano-vs-su-version-original), [Versus Media](https://versusmedia.mx/asi-elenco-sing-espanol-latino/) |
| **Rosita** | **Hanna** (Ha\*Ash) | ✅ las mismas dos, y [Wikipedia: videografía de Ha\*Ash](https://es.wikipedia.org/wiki/Anexo:Videograf%C3%ADa_de_Ha*Ash) |
| **Ash** | **Ashley** (Ha\*Ash) | ✅ las mismas |
| **Johnny** | **Roger González** | ✅ Espinof, Versus Media |
| **Meena** | **María Eugenia «China» Suárez** | ✅ Espinof, [La Nación](https://www.lanacion.com.ar/espectaculos/cine/la-china-suarez-y-leonardo-sbaraglia-hablan-sobre-la-dificil-tarea-de-darle-voz-a-un-personaje-animado-nid1971390/) |
| **Mike** (ratón) | **Leonardo Sbaraglia** | ✅ Espinof, La Nación |
| Clay Calloway (*Sing 2*) | **Chayanne** | ✅ Espinof, [SensaCine México](https://www.sensacine.com.mx/peliculas/pelicula-253538/reparto/) |
| Porsha Crystal (*Sing 2*) | **Greeicy Rendón** | ✅ Espinof y [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Sing_2:_%C2%A1Ven_y_canta_de_nuevo!) |
| Gunter (las dos) | **Rubén Cerda** | ✅ Espinof y Doblaje Wiki |
| **Srta. Crawly** | **Óscar Flores** (un actor, como en inglés, donde la hace el director Garth Jennings) | ⚠️ sólo Doblaje Wiki |
| Nana Noodleman | Marcela Páez | ⚠️ sólo Doblaje Wiki |

**Estudio** ✅ (Doblaje Wiki): *Sing* en **Dubbing House**, *Sing 2* en
**Iyuno-SDI México**; las dos dirigidas por **Pepe Toño Macías** (el Luigi
de 1993 y el tío Arthur de Mario 2023), con traducción de Jesús Vallejo.
Dirección musical de *Sing*: **Gaby Cárdenas**.

> [!warning] ¿Cantan en español? Casi nunca ✅
> Según Doblaje Wiki: aunque casi todo el reparto son músicos, **la
> mayoría de las canciones (versiones de temas conocidos) se dejaron en
> inglés**. La excepción es «**Set It All Free**» (canción original), que
> **Ashley de Ha\*Ash cantó en español**. Y en la tele (Canal 5 y cable)
> los **letreros de pantalla salen en español**. → En la lámina: **ninguna
> letra de canción** (derechos, y además sonaría en inglés).

### 6.5 Cómo habla en pantalla (el cuadro)

- **El volante de la audición**: **amarillo** ✅ (la wiki lo llama «the
  Yellow Flyer», #580), con el premio de los ceros de más ✅. El diseño
  exacto de la letra es ⚠️: mirarlo en la escena
  ([«100.000 dollar mistake»](https://www.youtube.com/watch?v=KV5ARyNjGhY)). **Es el
  cuadro del canal**: las reglas van en un volante.
- **La marquesina del teatro** ✅ (#58, #122): letras sueltas sobre fondo
  claro, con un **reloj encima**, y un **cartel vertical «MOON»** en la
  esquina. En la audición pone «**OPEN AUDITIONS**». Sirve para el título.
- **El micrófono de pie** bajo un foco: la imagen de «canto».
- **Letras**: marquesina art déco → **Limelight**; volante → una slab gruesa
  como **Alfa Slab One** o **Rye** (§8).

### 6.6 Fondo, luz y paleta ⚠️

- **El Teatro Moon** ✅ (arte de producción de **Gregory Georges**, #58,
  #59, #61): fachada **barroca blanca** con liras y un reloj; dentro, sala
  **roja** con arcos, palcos y filas de **bombillas**; escenario con telón
  de terciopelo y flecos dorados.
- La **ciudad**: una gran ciudad de animales, tipo Los Ángeles, de noche con
  neón. En *Sing 2*, **Redshore City** (tipo Las Vegas) ⚠️.
- Luz: **cañón de seguimiento** blanco-cálido sobre el escenario oscuro.

| Qué | Hex | Origen |
|---|---|---|
| fachada del teatro | `#F0E0D0` | #58 ✅ |
| telón lateral (sombra) | `#400010` / `#500010` | #61 ✅ |
| paredes de la sala | `#704030` / `#A06040` | #59 ✅ |
| suelo del escenario | `#603020`, luz `#F09050` | #61 ✅ |
| terciopelo del telón, en luz | `#9E1B2F` | ⚠️ a ojo |
| dorado de molduras | `#D4A64A` | ⚠️ a ojo |
| moldura dorada con luz de sala | `#CE704A` | [tráiler largo, min. 2:20](https://www.dailymotion.com/video/x889jpx) ✅ (medida en fotograma) |
| butacas en sombra | `#471A17` | mismo fotograma ✅ |
| volante | amarillo `#F6D34A` | ⚠️ a ojo (el color, ✅) |

- **Texturas reales**: terciopelo (CC0: [velour_velvet](https://polyhaven.com/a/velour_velvet)
  en Poly Haven), pan de oro gastado, papel de volante barato, bombillas.
- **Modelos 3D libres (CC BY)**: [Theater Stage Curtains](https://sketchfab.com/3d-models/8633a0c7ef7540c099d4a1796fc12fef)
  de **fuglee**; [Vintage Microphone](https://sketchfab.com/3d-models/a5986b39102f47c5b32b212365dd7276)
  de **Klasy** (hay otras cuatro con el mismo nombre, todas CC BY);
  [Bulletin Board](https://sketchfab.com/3d-models/8f06a1ffa3ca417e822f038c43d48d54)
  de **jaromir.ternavskiy** para clavar el volante.

### 6.7 Qué NO hacer

- Poner a Meena **segura y sonriente** desde el principio: su gracia es que
  tiembla y luego brilla.
- Letras de canciones famosas en la lámina (derechos y, además, no sabemos
  la versión latina).
- Confundir el estilo de Illumination con el de Pixar: Sing tiene formas más
  redondas y ojos grandes.

### 6.8 Conceptos de lámina

**Concepto A · El volante de la audición en la puerta del Teatro Moon**
(el recomendado)
- **Objeto real en sitio real**: el **volante** pegado en la **puerta del
  escenario**, con otros volantes volando alrededor. En **Blender**: papeles
  curvados, cinta adhesiva.
- **Personaje**: **Meena asomándose** detrás del telón, tímida (render #1
  para recortar); **Buster** a su lado, animándola con el volante en la mano
  (render #2).
- **Cómo habla**: el texto **es el volante**. En vez de «Premio 100.000»,
  «Hablar de cantar» en grande.
- **Dónde va cada texto**: «Canto» en la marquesina de arriba; «Hablar de
  cantar» como titular del volante; «Técnica, nervios, repertorio» como la
  lista del volante; «Tus covers van a demos-canto» y «Un hilo por cover»
  en un **segundo volante** con una flecha.
- **Que no quede plano**: el foco cae de lado sobre el volante; el telón
  rojo en primer plano, desenfocado; polvo en el haz de luz.

**Concepto B · El micro bajo el foco**
- **Objeto**: un **micrófono de pie antiguo** solo en el escenario, con la
  sala vacía.
- **Personaje**: Meena **de espaldas**, a punto de acercarse al micro.
- **Texto**: la marquesina (título) y las reglas escritas en la **lista de
  turnos** pegada en la pared del escenario.
- **Que no quede plano**: contraluz del foco; butacas rojas oscuras delante.

---

## 7 · Las salas de voz

Las salas de voz también tienen chat, y el encargo las nombra. Propongo
**no abrir ocho mundos nuevos**: cada sala va con el mundo de su canal
vecino, para que cada sección del servidor parezca **un solo sitio**. Sólo
la radio y el cine estrenan serie: **Los Simpson**.

### 7.1 Tabla de salas

| Sala (sección) | Texto del inventario | Serie | Sitio y objeto | Personaje |
|---|---|---|---|---|
| 📻 **Radio 24/7** (EN VIVO) | — | **Los Simpson** | la cabina de **Radio KBBL, 102.5 FM**: micro, consola, cartel «EN EL AIRE» | Bill y Marty, los dos locutores |
| 🍿 **Cine** (EN VIVO) | — | **Los Simpson** | el **sillón** de la sala frente a la tele (el *couch gag*) | la familia entera, de espaldas |
| 🎲 **Juegos** (EN VIVO) | — | Ralph el demoledor | la **taberna de Tapper** dentro de su máquina, donde los personajes se juntan | Ralph y Félix en la barra |
| 🎙️ **Grabación** (EL ESTUDIO) | — | Monsters, Inc. | una **estación del Piso de Sustos** con su puerta, la luz roja encendida y el **tanque** llenándose | Mike al panel, Sulley en la puerta |
| 🎚️ **Mesa de Trabajo** (EL ESTUDIO) | — | Monsters, Inc. / *Monsters at Work* | el **taller del equipo de mantenimiento (MIFT)**: mesa llena de herramientas y tanques abiertos | Tylor, el novato, con Fritz ⚠️ |
| 🎶 **Karaoke** (EN VIVO) | — | Sing | la **fila de audiciones** del Teatro Moon: número en el pecho, micro de pie | Johnny, Ash y Rosita esperando turno |
| 🔊 **Aula** (LA ACADEMIA) | — | Monsters University **o** Assassination Classroom | el **aula en gradas** del profesor Knight / la clase 3-E | Mike en primera fila / Koro-sensei |
| 🎭 **Escenario** (EN VIVO) | _Charlas, entrevistas y directos. Sube quien invita el anfitrión._ | Sing | el **escenario del Teatro Moon**, telón rojo, un micro en el centro | Buster Moon presentando |

Notas:
- **Aula**: LA ACADEMIA ya es Assassination Classroom (#avisos-clases) y My
  Hero Academia (#material-de-clase). Si se quiere que la sala «parezca del
  mismo colegio», la opción es **reusar Assassination Classroom** (el aula
  de la 3-E), aunque repita serie. Si se quiere una serie nueva, **Monsters
  University** encaja: es una universidad y Mike es el alumno aplicado.
- **Escenario**: la regla «sube quien invita el anfitrión» es Buster Moon
  llamando por su nombre a cada concursante.
- **Karaoke**: casi todas las canciones de *Sing* se dejaron **en inglés**
  en el doblaje latino (§6.4). Justo como un karaoke de verdad.

### 7.2 Los Simpson, lo esencial (para Radio 24/7 y Cine)

**Por qué**: es, probablemente, **la serie animada más querida por el
público latino**, y su doblaje es parte de la historia del oficio.

- **Radio KBBL** es la radio de Springfield, en el **102.5 FM**; sus
  locutores son **Bill y Marty** ✅ ([Simpsons Wiki: KBBL Radio](https://simpsons.fandom.com/wiki/KBBL_Radio),
  [Bill and Marty](https://simpsons.fandom.com/wiki/Bill_and_Marty), por su
  API). **Dos locutores**, como la radio que el dueño presenta con una amiga.
- **Corregido (segunda pasada): los DJ de KBBL no tienen actor latino
  fijo; cambia de episodio a episodio**, como pasa con muchos secundarios de
  la serie clásica. En la **T4** («Homero el hereje») fueron **Agustín
  Sauret** y **Alejandro Mayén**; en la **T5**, a Bill lo hace **José María
  Iglesias** en un episodio y **Víctor Delgado** en otro, y a Marty **Mario
  Sauret** ✅ ([Doblaje Wiki: T4](https://doblaje.fandom.com/es/wiki/Los_Simpson/4%C2%AA_temporada),
  [Doblaje Wiki: T5](https://doblaje.fandom.com/es/wiki/Los_Simpson/5%C2%AA_temporada)).
  **En la lámina de Radio 24/7 no se nombra a ningún actor** para Bill y
  Marty: basta «voces rotativas, como en toda la serie clásica».
- **Homero**: **Humberto Vélez** (T1-T15), **Víctor Manuel Espinoza**
  (T16-T31) y otra vez **Humberto Vélez** desde la **T32 (2021)** ✅
  ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Los_Simpson), API;
  [LevelUp](https://www.levelup.com/noticias/despues-de-16-anos-vuelve-el-doblaje-original-de-los-simpson-con-humberto-velez-y-mas/)).
- **Humberto Vélez salió dibujado en la serie**: en el episodio **«The Fall
  Guy-Yi-Yi»** (T37, ep. 12), emitido en FOX el **28 de diciembre de 2025**,
  él y **Paty Acevedo** (la Lisa latina) aparecen como personajes ✅
  ([El Imparcial](https://www.elimparcial.com/espectaculos/2025/12/29/humberto-velez-se-convierte-en-un-personaje-oficial-de-los-simpson-la-serie-a-la-que-ha-prestado-su-voz-en-espanol-por-20-anos/),
  [Merca2.0](https://www.merca20.com/los-simpson-celebran-el-legado-del-doblaje-latino-con-una-aparicion-especial-de-humberto-velez/),
  [3DJuegos LATAM](https://www.3djuegos.lat/cine-y-tv/actores-doblaje-latino-simpson-prestaran-sus-voces-idioma-original-humberto-velez-paty-acevedo-estaran-capitulo-cultura-mexicana)).
- **El doblaje se nombra a sí mismo** ✅ (Doblaje Wiki):
  - «**¡Somos ricos, Marge! Más ricos que los del doblaje**» (Homero, «El
    autobús de la muerte»);
  - «Marge, me han botado de todo lo que he intentado, **hasta cuando quise
    ser actor de doblaje**» («La sazón del baile»);
  - un actor despedido que fue «el doctor Tad Winslow **y la voz de Ranma
    por 25 años**», doblado por **Carlos Hugo Hidalgo**, la voz de Ranma
    («Pigmoelion»).
  → Son frases perfectas para **#general-doblaje** si algún día se prefiere
  Los Simpson allí (§0.4).
- **Frases de Homero que no estaban en el guion** (Humberto Vélez): «Me
  quiero volver chango», «A la grande le puse Cuca», «¡Qué elegancia la de
  Francia!» ✅ (ya recogidas en `_ya_hechas/_Cuadros de dialogo…`, con
  [TV Azteca](https://www.tvazteca.com/azteca7/series/7-frases-iconicas-homero-simpson-doblaje-latino-nunca-olvidaremos)).
- **El cuadro de diálogo**: la **pizarra de Bart** (letra *Akbar*, gratis
  sólo para uso no comercial) ✅ (en `_ya_hechas`). Para la radio: el
  **cartel luminoso «ON AIR»** de la cabina ⚠️. Para el cine: la **tele** de
  la sala, con el texto en pantalla.
- **Imágenes** ✅ (hoja `p29-simpsons-kbbl`, de la wiki de Los Simpson en Fandom):
  - #8 [KBBL.jpg](https://static.wikia.nocookie.net/simpsons/images/a/a0/KBBL.jpg) (1400×994): **Bill y Marty en la cabina**, con auriculares, detrás de un mostrador con el letrero **KBBL** en rojo sobre blanco. Es la imagen para la Radio 24/7.
  - #3 [Kbbl radio simpsons game.png](https://static.wikia.nocookie.net/simpsons/images/1/1d/Kbbl_radio_simpsons_game.png) (1920×1080): la **torre de radio KBBL** (juego *The Simpsons Game*).
  - #12 [TO Kbbl-station.png](https://static.wikia.nocookie.net/simpsons/images/a/aa/TO_Kbbl-station.png) (650×784): el **edificio de KBBL** con su antena (*Tapped Out*): sirve de icono.
  - #1 [Simpsonsbg 2013 r1 sofa hires2.jpg](https://static.wikia.nocookie.net/simpsons/images/0/00/Simpsonsbg_2013_r1_sofa_hires2.jpg) (8334×4688): **el sillón**, la familia entera, en alta (8334×4688): para el Cine.
  - #2 [WoSEBGamesKBBLBillAndMarty.jpg](https://static.wikia.nocookie.net/simpsons/images/d/d2/WoSEBGamesKBBLBillAndMarty.jpg) (1600×1364): las figuras de juguete de Bill y Marty (*World of Springfield*).

**Concepto · La cabina de KBBL (Radio 24/7)**
- **Objeto real en sitio real**: el **micrófono** de la cabina de KBBL, con
  el **mostrador rojo y blanco «KBBL»** (#8) y un cartel «EN EL AIRE»
  encendido. En **Blender**: micro
  antiguo ([Vintage Microphone](https://sketchfab.com/3d-models/a5986b39102f47c5b32b212365dd7276),
  de **Klasy**, CC BY).
- **Personajes**: Bill y Marty, uno a cada lado del micro.
- **Texto**: en la **pantalla de la consola** y en el cartel luminoso.
- **Que no quede plano**: la luz roja del cartel sobre las caras; el micro
  delante, grande y desenfocado.

**Concepto · El sillón (Cine)**
- La familia en el sillón **de espaldas**, la tele con el texto de la sala
  («Se ve junto, se comenta en el chat»). Es el *couch gag*: todo el mundo
  lo reconoce.

---

## 8 · Letras libres, comprobadas

Bajé cada letra de [google/fonts](https://github.com/google/fonts) (clon
ligero) y comprobé con **fontTools** que trae **á é í ó ú ñ Ñ ¿ ¡ ü** y las
mayúsculas con tilde. **Todas pasan** ✅. Todas son **OFL** (libres, también
para uso comercial). La muestra está en `hojas/hoja_03_letras.jpg`.

| Serie | Para qué | Letra libre | Tildes, ñ, ¿ ¡ |
|---|---|---|---|
| Mario | página del libro de Estela | **Fredoka** | ✅ |
| Mario | globo del juego (cápsula) | **M PLUS Rounded 1c** Bold (se parece a la Rodin redondeada de Nintendo ⚠️) | ✅ |
| Mario | títulos gordos | **Titan One** | ✅ |
| Phineas y Ferb | el plano a mano | **Architects Daughter** | ✅ |
| Phineas y Ferb | cartela del «-inador» | **Bangers** | ✅ |
| Bleach | la revista, titulares | **Shippori Mincho** (trae kanji) | ✅ |
| Bleach | pincel, cartel de la redacción | **Yuji Syuku** (trae kanji) | ✅ |
| Ralph | pantalla de 8 bits | **Press Start 2P** | ✅ |
| Ralph | marcador pequeño | **Silkscreen** | ✅ |
| Ralph | marquesina, tablero | **Bungee** | ✅ |
| Monsters | carteles de la fábrica (años 50) | **Jost** (tipo Futura) | ✅ |
| Monsters | la tablilla de Mike | **Kalam** | ✅ |
| Sing | marquesina art déco | **Limelight** | ✅ |
| Sing | volante de la audición | **Alfa Slab One** o **Rye** | ✅ |
| Los Simpson | pizarra de Bart | *Akbar* (no es OFL: gratis sólo no comercial) | ⚠️ ver `_ya_hechas` |

Letras **oficiales o de fans que NO son libres**: la «MARIO Font» de
Nintendo y Fontworks; la «Bleach» de Danilo Belardinelli (uso personal);
los logos de Phineas y Ferb, Ralph, Monsters, Inc. y Sing (dibujados, sin
letra pública). Para los logos: **usar el logo oficial en imagen**, no
imitarlo con una letra.

> [!tip] Emojis
> Ninguna de estas letras dibuja el emoji ⭐. En la lámina de #destacados,
> la estrella **se dibuja** (o es la Superestrella en 3D), no se escribe.

---

## 9 · Lo que falta, y el orden que propongo

### 9.1 Qué hacer después

1. **Que el dueño elija.** Esta es una propuesta. Si alguna serie no le
   convence, en §0.4 están las alternativas ya pensadas (Animal Crossing,
   Yu Yu Hakusho, Sonic, Frozen/Moana, Los Simpson).
2. **Abrir un encargo de biblia completa** por cada serie elegida (como los
   de la carpeta `encargos/`), con estas prioridades:
   - **#general-doblaje** (Monsters, Inc.) primero: es el canal **más vivo**
     (14 de 15 mensajes recientes son de personas).
   - Después **#eventos** (Phineas y Ferb) y **#canto** (Sing).
   - **#noticias-anime** (Bleach) pronto: su anime **termina el 26 de
     septiembre de 2026** y la noticia está caliente.
   - **#destacados** y **#noticias-gaming** al final: casi nadie escribe
     allí.
3. **Las salas de voz** (§7) sólo cuando estén las de sus canales vecinos:
   así se reutilizan fondos y recortes.

### 9.2 Lo que no pude hacer

- **Minutos exactos en los vídeos de YouTube**: YouTube pidió «confirmar que
  no soy un bot» y no dejó bajar subtítulos. Doy el enlace y la duración.
  Sólo Bleach tiene minuto exacto (subtítulos de kitsunekko).
- **Frases latinas de Estela, Buster, Meena y Hisagi**: no encontré
  ninguna que el público cite. Las frases de la lámina **no se pueden
  presentar como del doblaje** si no lo son.
- **La página de dentro del libro de Estela**: tengo la tapa (#69) y la
  escena (#82), no una página con dibujos. Hay que sacarla de un vídeo del
  juego.
- **El diseño exacto del volante de Sing** (letras, colores): sólo sé que es
  amarillo. Sacarlo de la escena.
- **Voces latinas de Bill y Marty** (KBBL): no hay actor fijo; varía por
  episodio (T4 y T5 comprobadas, segunda pasada). No se nombra a nadie.
- **Encuestas de popularidad** de Phineas y Ferb, Ralph, Monsters y Sing:
  no hay encuestas oficiales como las de la Shōnen Jump. Uso la taquilla,
  el doblaje y los memes.
- **TV Tropes, The Cutting Room Floor y Wikipedia** no respondieron (403 y
  429).
- **Fan art** (Pixiv, DeviantArt, ArtStation): no lo busqué; con el arte
  oficial de las wikis (2.800 imágenes grandes) había de sobra para este
  encargo de decisión. Queda para cada biblia completa.

### 9.3 Guía corta para IA (Firefly, Canva)

Sólo para **fondos y objetos**, nunca para inventar personajes: los
personajes se recortan del arte oficial (las tablas de imágenes de cada sección) con `v3/integrar.py`.

| Serie | Palabras que ayudan | Palabras que lo estropean |
|---|---|---|
| Mario Galaxy | «biblioteca de madera oscura en una nave espacial, luz cálida de lámpara, estrellas por la ventana, estilo 3D de Nintendo Wii, colores saturados» | «realista», «fotografía», «oscuro y lúgubre» |
| Phineas y Ferb | «patio trasero con cerca de madera y árbol grande, mañana de verano, dibujo plano 2D de líneas geométricas, colores planos sin degradado» | «acuarela», «sombras suaves», «3D» |
| Bleach | «redacción japonesa de los 2000, fluorescentes, mesas en fila, cartel vertical escrito a pincel, anime 2D, contraste alto» | «colores pastel», «kawaii», «tatami tradicional» |
| Ralph | «gran estación de tren de los años 20 con túneles y letreros de LED rojo, haz de luz por ventanales verdes, 3D de Disney» | «cyberpunk», «neón rosa por todas partes» |
| Monsters, Inc. | «nave industrial de los años 50, persiana metálica azul violeta, puerta en un marco de metal con luz roja, 3D de Pixar» | «terror», «sangre», «oscuro» |
| Sing | «teatro barroco antiguo, telón de terciopelo rojo, bombillas, foco cálido, 3D de Illumination» | «teatro moderno», «pantalla LED», «neón» |

---

## Bitácora de búsqueda

### Búsquedas web (WebSearch), por idioma

**Español**
1. Super Mario Galaxy la película doblaje latino reparto Estela Rosalina voz
2. Super Mario Bros La Película doblaje latino Pepe Toño Macías Luigi Peach Bowser reparto
3. Super Mario Galaxy La Película taquilla México récord estreno abril 2026
4. «Estela» o «Rosalina» nombre en español latino Super Mario Galaxy película Casandra Acevedo
5. Super Mario Galaxy español «Destellos» «Observatorio Cometa» «Superestrella» Estela
6. Phineas y Ferb doblaje latino reparto Phineas Ferb Candace Doofenshmirtz Isabella
7. Phineas y Ferb nueva temporada 2025 doblaje latino voces originales regresan
8. voz latina de Doofenshmirtz… «Isabella» voz latina actriz «¿Qué hacen?»
9. Phineas y Ferb canción tema letra español latino «ciento cuatro días»
10. Isabella García-Shapiro doblaje latino actriz de voz… Christine Byrd
11. Bleach doblaje latino Ichigo Kurosaki voz latina TYBW Disney+ reparto
12. «Eduardo Garza» Ichigo Bleach doblaje latino Rukia «Rangiku» «Macias Group»
13. Bleach TYBW The Calamity part 4 2026 estreno doblaje latino Disney+
14. Ralph el demoledor doblaje latino reparto Ralph Vanellope Félix Calhoun
15. «Ralph el demoledor» Félix voz latina «Moisés Iván Mora»… «soy malo y eso es bueno»
16. Monsters Inc doblaje latino Andrés Bustamante… Roz Randall Boo… MU
17. Monsters at Work doblaje latino Mike Wazowski voz cambio
18. Monsters Inc frases doblaje latino Roz «papeleo» Wazowski
19. Sing ven y canta doblaje latino reparto Meena Buster Moon…
20. Sing doblaje latino las canciones se quedaron en inglés o español Ha*Ash…
21. Los Simpson doblaje latino regreso Humberto Vélez Homero temporada 36

**Inglés**
22. Super Mario Galaxy Rosalina storybook library Comet Observatory… Iwata Asks
23. Super Mario Galaxy in-game font dialogue text box font name Rodin…
24. Phineas and Ferb blueprint scene art style Dan Povenmire triangle head…
25. Bleach logo font free download Kubo Tite volume cover poems typography
26. Wreck-It Ralph Litwak's arcade production design… Game Central Station
27. Monsters Inc scare floor production design Harley Jessup Dominique Louis…
28. Sing 3 Illumination release date Buster Moon news 2026
29. Sing 2016 Miss Crawly glass eye flyer typo $100,000 Moon Theater Meena…

**Japonés**
30. 瀞霊廷通信 檜佐木修兵 編集長 九番隊 BLEACH 小説 Can't Fear Your Own World
31. BLEACH 人気投票 結果 順位 1位 日番谷 市丸ギン 公式 最新

### Consultas directas (con la red abierta)

- **Doblaje Wiki, API `action=parse`**: Super Mario Galaxy: La película;
  Super Mario Bros.: La película; Phineas y Ferb; Phineas y Ferb/5.ª
  temporada; Bleach; Bleach: Thousand-Year Blood War; Ralph, el demoledor;
  Wifi Ralph; Monsters, Inc.; Monsters University; Monsters at Work; Sing
  ¡Ven y canta!; Sing 2; Los Simpson; Los Simpson/4.ª temporada.
- **Fandom, API**: mario, phineasandferb, bleach (también el texto de
  «Seireitei Communication» y «Jigokuchō»), wreckitralph (texto de «Game
  Central Station» y «Litwak's Arcade»), pixar, sing, simpsons (texto de
  «KBBL Radio» y «Bill and Marty»).
- **`investigar_serie.py`**: 7 wikis, **2.809 imágenes grandes**, **62
  hojas** en `herramientas/referencias/p29-*/`. Bajadas y medidas: Mario
  #43 #63 #69 #82; Phineas #21 #33 #52 #54; Bleach #250 #282 #283 #284
  #303; Ralph #8 #40 #41 #53 #79 #119 #121; Monsters #25 #56 #61 #66 #67
  #74; Sing #58 #59 #61 #122 #198 #488 #580 #653.
- **kitsunekko-mirror** (GitHub, clon sparse): subtítulos japoneses de
  Bleach (eps. 114, 115, 126, 138, 219, 227, 305).
- **Arctic Shift** (Reddit): r/bleach «Seireitei Communication», «Hisagi
  editor»; r/Mario «Rosalina storybook»; r/Mexico y r/Monsters (sin
  resultados); r/phineasandferb (error 422).
- **Sketchfab API** (descargables, con licencia): power star, luma, arcade
  cabinet, split flap, scream canister, monsters inc door, vintage
  microphone, theater curtain, blueprint, butterfly, tatami, shoji, wooden
  fence, clipboard, open book.
- **Poly Haven API**: texturas CC0 (velour_velvet, tatami_mat, wood_planks,
  metal_plate, blue_metal_plate).
- **google/fonts** (clon sparse) + fontTools: 20 letras comprobadas.
- **yt-dlp** (`ytsearch`): tráileres de Mario Galaxy, Phineas y Ferb T5,
  Bleach *The Calamity*, Ralph, escenas de Roz. Subtítulos: bloqueados.

### Fuentes consultadas (más de 60 distintas)

- **Oficiales**: Universal Pictures México (YouTube), Disney+ Latinoamérica
  (YouTube), VIZ (blog y YouTube), el «号外 瀞霊廷通信» oficial de 2023,
  arte de producción de Gregory Georges (Sing), Art of the Title.
- **Doblaje**: Doblaje Wiki (15 fichas por API), ANMTV (6 notas), DubDB,
  sitio de Mario Filio, Milenio, Sopitas, SDP Noticias, UnoTV, Posta,
  Nintenduo, Espinof, Versus Media, La Nación, SensaCine México y Colombia,
  GamerFocus, El Imparcial, Merca2.0, 3DJuegos LATAM, LevelUp, TV Azteca.
- **Taquilla y prensa**: Noroeste, Crónica, Vanguardia, Xataka México,
  Infobae, Final Weapon, OtakuWire, Screen Rant, IMDb.
- **Wikis de fans**: Super Mario Wiki (mariowiki.com y Fandom en inglés y
  español), SmashPedia, Nintendo Wiki, Phineas and Ferb Wiki, Bleach Wiki,
  Wreck-It Ralph Wiki, Pixar Wiki, Disney Wiki, Sing Wiki, Universal
  Studios Wiki, Simpsons Wiki, Pixiv百科事典, TV Tropes (vía buscador).
- **En japonés**: Da Vinci Web, ciatr, Setochan, kamo2kamo, Pixiv百科事典.
- **Foros**: Reddit (r/bleach, r/Mario) por Arctic Shift.
- **Código y 3D**: GitHub (google/fonts, kitsunekko-mirror), Sketchfab,
  Poly Haven, Blender Artists, ArtStation Marketplace.
- **Letras**: FontSpace, FontMeme, Font In Logo, dafont (foro).
- **Vídeo**: YouTube (tráileres oficiales y escenas), TikTok (páginas de
  búsqueda sobre Roz y el papeleo).

### Lo que NO encontré

- Imágenes de las **páginas interiores** del libro de Estela.
- Frases del **doblaje latino** de la película de Mario Galaxy que se hayan
  hecho populares.
- El **diseño exacto** del volante amarillo de Sing.
- **Encuestas oficiales** de popularidad para las series occidentales.
- **Minutos exactos** en YouTube (bloqueado); **TV Tropes**, **TCRF** y
  **Wikipedia** (bloqueados o saturados).
