---
tags: [biblia, serie, laminas]
serie: "Kakegurui"
canal: "#comandos-y-sorteos"
fecha: 2026-09-24
---

# Biblia · Kakegurui — para #comandos-y-sorteos

> [!important] Cómo se hizo, y sus límites
> - **Segunda pasada (25-sep-2026, red abierta)**: un equipo de cuatro
>   investigadores (imagen, vídeo, voz, texto) y un redactor. Se pudo usar:
>   las APIs de Fandom (Kakegurui Wiki), **Doblaje Wiki**, Sketchfab,
>   Poly Haven, ambientCG, Wikipedia, AniList y Arctic Shift (Reddit);
>   **1051 imágenes de la wiki en 11 hojas de contacto** (3 en `hojas/`,
>   §3.0); los **episodios 1 y 2 con doblaje latino** de
>   [Internet Archive](https://archive.org/details/kakegurui-latino) y el
>   **tráiler oficial** en [Dailymotion](https://www.dailymotion.com/video/x88p1dp),
>   mirados con `fotogramas.py`; `estilo.py` para medir colores en 9
>   fotogramas y 5 ilustraciones oficiales; `yt-dlp` para las fichas de
>   fan dubs y covers (vistas reales).
> - **Lo que no se pudo en la segunda pasada**: YouTube pidió iniciar
>   sesión para ver vídeos (sólo dio fichas). Los vídeos mirados son SD:
>   **854×480** los episodios y **512×288** el tráiler; la copia 720p
>   Blu-ray se cortó dos veces. AnimeThemes dio 522. TV Tropes, Comic
>   Natalie, TCRF y VGMdb dieron 403 o Cloudflare. TikTok bloquea `yt-dlp`.
>   Crunchyroll no se usa.
> - **Dos formatos de minuto**: `mm:ss` (por ejemplo 12:39) es un minuto
>   **visto** en la copia de Internet Archive; `00:mm:ss` es el minuto del
>   **subtítulo** de la primera pasada. Entre los dos hay de 1 a 8 segundos.
> - **Primera pasada (24-sep-2026)**: lo que sigue.
> - La red de esta sesión estaba cerrada. Fandom, Doblaje Wiki, TV Tropes,
>   Tumblr, la web oficial del anime, la de Square Enix, Natalie, G123,
>   Wayback Machine, Google Fonts y Arctic Shift daban **403** por curl o
>   por WebFetch. Reddit ni siquiera se deja buscar. Por eso **no se pudo
>   correr** `herramientas/investigar_serie.py`: **no hay hojas de
>   contacto** ni carpeta `hojas/`.
> - Hice **47 búsquedas web** en español, inglés, japonés, chino y coreano
>   (la lista está al final, en la bitácora).
> - GitHub sí respondía. De ahí saqué lo más útil de todo el trabajo:
>   **los subtítulos de las dos temporadas, con sus tiempos**, del
>   repositorio [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Kakegurui).
>   La temporada 1 trae japonés e inglés de Netflix juntos. La temporada 2
>   (××) trae el japonés de Netflix. Con ellos doy el **minuto de cada
>   escena**. Es el minuto de ese archivo: puede moverse uno o dos minutos
>   según la plataforma.
> - También bajé de [google/fonts](https://github.com/google/fonts) las
>   letras propuestas y comprobé una a una, con fontTools, si traen
>   á é í ó ú ñ ¿ ¡.
> - **Cómo leo los episodios**: «1×02» es temporada 1, episodio 2. La
>   temporada 2 es **Kakegurui ××** («2×05» es su episodio 5). El minuto va
>   así: 00:12:37.
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su minuto.
>   ⚠️ **dudoso**: una sola fuente, o lo describo de memoria. Lo de memoria
>   siempre va marcado.

> [!note] Segunda pasada · qué cambió
> **Corregido (antes → ahora)**
> - **Compositor del opening** «Deal with the devil»: «producción de
>   TeddyLoid», según un TikTok → **letra, música y arreglo de ryo
>   (supercell)**, leído en los créditos del ep. 1, en 3:02 (visto). Una
>   sola fuente, pero es la pantalla misma (§11).
> - **Voz latina de Kirari, Ririka y dirección**: «no encontrado ❌» →
>   **Adriana Núñez** dobla a las dos gemelas; dirige **Guillermo Rojas**
>   (Daniel Lacy en los eps. 17-21). Dos páginas de Doblaje Wiki por
>   nombre. Se suman Sayaka, Runa, Itsuki, Midari, Yumemi, Kaede y Yuriko
>   (§10).
> - **Máscara de Ririka**: «gris `#8E8E94`» → **blanca**, según el texto
>   «Appearance» de la wiki (§16, §18).
> - **Luz de la sala del consejo**: «azul verdosa, de memoria» → **acuario
>   turquesa medido**, `#30B5B9` y `#76FBF8`, en el ep. 2, 21:30 (visto)
>   (§5, §17).
> - **Rojo del blazer**: `#C9020F`, de la paleta de un fan → **`#D6362A`**,
>   medido en 5 ilustraciones oficiales (va de `#C05051` a `#E5392C`; de
>   noche, `#832B27`) (§16).
> - **Licencias de Sketchfab**: «⚠️ comprobar» → leídas en su API: 5 son
>   CC BY 4.0 y 2 son **CC BY-NC-ND** (sólo mirar). Madera de Poly Haven:
>   CC0 confirmado (§4, §5).
> - **Encuesta oficial**: Yumeko 5.ª y Kirari por debajo de Mary, antes con
>   un solo resumen → lo cuenta **el propio Kawamoto** en un podcast
>   (hilo traducido por un fan) (§9).
> - **Kirari y Ririka salen en el ep. 2** (1×02, «A Boring Woman»), vistas
>   en vídeo; las dos tienen la misma seiyū, Miyuki Sawashiro (§8).
>
> **Añadido**
> - Hojas de contacto (§3.0). Opening, ending, tráiler y 3 escenas
>   **mirados**, con minuto `mm:ss` (§2, §11, §12, §15).
> - Colores medidos con `estilo.py` en fotogramas y arte oficial (§5, §16).
> - Pachislot y pachinko oficiales, figuras ARTFX J y Union Creative,
>   perfumes, cafés, exposición y SINoALICE (§3, §F).
> - Fondos de pantalla de Wallhaven con tamaño medido (§17).
> - Puntos nuevos del encargo: estilo y técnica (§A), texturas 2D (§B),
>   gustos (§C), por qué la aman (§D), fan dubs (§E), colaboraciones (§F),
>   obras parecidas (§G) y el mundo (§H). Tabla «Cumplimiento del encargo».
> - Guía para IA de texto con frases reales por emoción (§18).
>
> **Sigue dudoso**
> - Las citas de la **temporada 2 (××)**: el investigador de voz no halló
>   la carpeta ×× en el espejo de subtítulos en esta pasada; esos minutos
>   `2×…` son los de la primera pasada, sin volver a comprobar.
> - Ririka con la cara visible en vídeo: no se vio.
> - Las cartas y las manos en 3DCG: sigue con una fuente indirecta.
>
> **Los ⚠️**: había **73**. El recuento de ahora está al pie de la tabla
> «Cumplimiento del encargo».

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección LA SALA):

> **ıı・🤖・comandos-y-sorteos** (texto) · 0 fijados · 0 de personas en los
> últimos 15 — _Aquí se usan los bots, para no ensuciar el resto._

Función según el encargo: **los comandos de los bots (juegos, sorteos,
economía)**.

> [!info] Esta biblia es general
> Decisión del dueño (25-sep): la biblia sirve para cualquier uso
> (láminas, vídeos, diseño, textos, doblaje), no sólo para Discord. El
> canal #comandos-y-sorteos es una propuesta; ninguna otra biblia lo pide
> hasta ahora, y si alguna lo pidiera no bloquea nada.

> [!warning] La lista de comandos NO está en el inventario
> El encargo dice «la lista está en servidor/inventario.md». La busqué con
> grep: **no está**. El inventario sólo da la frase de arriba. Hay dos
> pistas más, sin la lista:
> - **ıı・🔧・config-bots** (privado): «Checklist de bots y qué configurar
>   en cada uno».
> - El foro **ıı・🗺️・guia** tiene la etiqueta **«Bots y comandos»**.
> - **📻・RADIO EN VIVO**: «Pides por comandos y suena aquí». No sé si esos
>   comandos se escriben en #comandos-y-sorteos.
>
> **No invento comandos.** Antes de rotular, el dueño tiene que pasar la
> lista real: qué bot, qué comando y para qué.

### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Comandos y sorteos** | nombre del canal |
| 2 | **Aquí se usan los bots** | para qué es |
| 3 | **Así no ensuciamos el resto** | por qué |
| 4 | **Juegos** | bloque 1 |
| 5 | **Sorteos** | bloque 2 |
| 6 | **Economía** | bloque 3 |
| 7 | *(un comando real por bloque, el más usado)* | ejemplo |
| 8 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

### Los textos de la lámina 2 (la lista completa)

Cuando el dueño pase la lista, **no cabe en la lámina 1**. Propongo
**lámina 2**: una carta de baraja por comando, agrupadas en tres palos:

| Palo | Qué va |
|---|---|
| **Juegos** | comandos de minijuegos |
| **Sorteos** | cómo entrar, cómo se anuncia el ganador |
| **Economía** | saldo, diario, tienda, ranking |

La idea encaja con la serie: en el episodio 1 las cartas salen **de una
caja**, y en el 2 el consejo publica **un ranking de lo que pagó cada
alumno** (ver §2). La lámina 2 puede ser ese ranking.

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué Kakegurui encaja | Es **un colegio donde todo se decide jugando**. El consejo estudiantil **emite las fichas** («100万円チップ», ep. 1×02, 00:08:06), **publica un ranking** de lo que paga cada alumno (1×02, 00:03:42) y **organiza votaciones y sorteos**. Es justo lo que hace un bot de economía. |
| Cuadro de diálogo propio | No hay globo propio verificado. Lo que la serie usa para poner texto en pantalla son **objetos**: la **carta** que sale de la caja, la **ficha** del consejo, la **placa de mascota** colgada al cuello («BOTTOM-FEEDER 0001 MITTENS», 1×03, 00:20:44) y los **papeles del consejo** (el «人生計画表», plan de vida, 1×04, 00:00:48). Y un gesto fijo: **los ojos que se ponen rojos** cuando Yumeko se emociona ✅. |
| Objeto para la lámina | **La mesa del voto a piedra, papel o tijera** (ep. 1): la caja de cartas, las fichas en pilas y tres cartas boca arriba. En Blender: caja, cartas, fichas y tapete. Dato de producción: en el anime **las cartas y las manos que las giran se hicieron siempre en 3DCG** ⚠️ (lo dice el resumen de mi búsqueda en japonés sobre el director Hayashi; no pude abrir la página para saber cuál de los resultados lo cuenta). |
| El más querido | **Mary Saotome**, 1.ª en el **concurso oficial de popularidad de Gangan Joker** («賭ケグルイ頂上戦», 2017) ✅. Yumeko, la protagonista, quedó **5.ª**: lo dice también el autor, Kawamoto, en un podcast (traducción de un fan, §9). En AniList gana Yumeko (8732 favoritos) ✅. |
| Letras | **Playfair Display** o **Cormorant Garamond** para los rótulos elegantes. **Bodoni Moda** para cifras de fichas. **Shippori Mincho B1** o **Zen Antique** para algún kanji. Todas traen tildes, ñ, ¿ y ¡: comprobado en el archivo. |
| Voz latina | Yumeko **Jocelyn Robles** ✅, Mary **Valentina Souza** ✅, Kirari y Ririka **Adriana Núñez** ✅ (segunda pasada). Estudio **Sysdub**, México; dirige **Guillermo Rojas** ✅. |
| Lo más visto en vídeo | La **cara de Yumeko con los ojos rojos**, ep. 1, 12:15-12:43 (visto); **Mary con la placa «ミケ»**, ep. 2, 1:00; **Kirari junto al acuario turquesa**, ep. 2, 21:22-21:40. |
| Tono | Elegante y enfermizo: rojo y negro, sonrisas que dan miedo, **caras exageradas** («顔芸»). Nada de colores alegres ni de chibis. |
| Juegos de la franquicia | **Kakegurui ALL IN** (G123, 23 de marzo de 2026): un **tablero con dados, monedas y cartas** ✅. Y **Kakegurui Cheating Allowed** (Avex, cerró el 27 de marzo de 2020) ✅. |

---

## 2 · Las escenas que sirven para #comandos-y-sorteos (con minuto)

Todas salen de los subtítulos de
[kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Kakegurui):
el texto y el minuto están comprobados ✅. Lo que **se ve** en cada una
(postura, luz) lo describo de memoria ⚠️: mira el fotograma antes de usarlo.
Las escenas de la tabla 2.0 sí están **vistas** (segunda pasada).

### 2.0 Visto en vídeo (segunda pasada)

Fuente: episodios 1 y 2 con doblaje latino en
[Internet Archive](https://archive.org/details/kakegurui-latino)
(854×480) y el tráiler oficial de Netflix en
[Dailymotion](https://www.dailymotion.com/video/x88p1dp) (512×288),
recorridos con `fotogramas.py`. Los minutos son los de esas copias.
No llegan a 1080p: sirven para pose, minuto y color, no para calcar.

| Dónde | Minuto | Qué se ve | Sirve para |
|---|---|---|---|
| Ep. 1 | 0:00-1:33 | Prólogo: un chico pierde contra Mary en el aula | abrir, tono |
| Ep. 1 | 0:15 | Aula del prólogo: ventana fría, cara cálida (`#D0C1B6` piel, `#43322D` sombra) | luz de aula |
| Ep. 1 | 1:50-3:26 | Opening entero: dados, cartas, peces y fichas sobre fondo oscuro con acentos rojos; la cámara gira | ritmo, objetos |
| Ep. 1 | 3:02 | Créditos del opening: «Deal with the devil», Tia; letra, música y arreglo de **ryo (supercell)** | dato de música |
| Ep. 1 | 6:05-7:41 | La mesa del voto a piedra, papel o tijera: focos sobre la mesa, el aula a oscuras | **objeto del canal** |
| Ep. 1 | 6:09-6:41 | Mary, de pie junto a Yumeko, mano a la altura del hombro con la palma abierta, explica las reglas | **explicar** |
| Ep. 1 | 6:29 | La mesa: negro violáceo `#11091F` domina el 38 % del fotograma | fondo |
| Ep. 1 | 7:29-7:41 | Yumeko sonríe con los ojos cerrados, manos juntas cerca del pecho, inclinada hacia Mary | **animar** |
| Ep. 1 | 11:55-12:07 | Yumeko echa el cuerpo adelante, brazo en alto hacia Mary | **acusar** |
| Ep. 1 | 12:15-12:43 | **Los ojos rojos**: boca muy abierta, cabeza atrás y luego adelante, dedos en garra cerca de la cara | **celebrar** |
| Ep. 1 | 12:31 | Mary: los ojos llenan el plano, con lágrimas | **miedo** |
| Ep. 1 | 12:39 | Yumeko transformada: fondo `#1D171C` (53 %), rojo `#C23345`, piel `#EFDADC` | paleta |
| Ep. 1 | 22:40-24:19 | Ending entero: Yumeko baila en silueta blanca entre pétalos; el aura pasa de rojo a verde, magenta y otra vez rojo | cierre |
| Ep. 1 | 23:25 | Créditos del ending: «LAYon-theLINE», D-selections, TECHNOBOYS PULCRAFT GREEN-FUND | dato de música |
| Ep. 2 | 1:00 | Mary furiosa levanta en el puño la **placa con cadena «ミケ»** | **regañar** |
| Ep. 2 | 5:00 | Kirari sola en un pasillo con luz lavanda `#9495D1`, mirada a cámara | **presentar** |
| Ep. 2 | 20:55 | Vestíbulo: araña dorada, madera oscura | fondo |
| Ep. 2 | 21:16-21:19 | Kirari de perfil, sonrisa entreabierta, ojos entrecerrados | **pensar** |
| Ep. 2 | 21:22-21:40 | La sala del consejo con el **acuario**: agua `#30B5B9` y `#76FBF8` | fondo con luz |
| Ep. 2 | 21:31-21:34 | Kirari, mano en la barbilla, junto al acuario | **proponer** |
| Ep. 2 | 21:37 | Kirari a la cabecera de la mesa larga del consejo | **presidir** |
| Tráiler | 0:24 | Mary: «Today's just not your day, huh?» | burla |
| Tráiler | 0:36 | Yumeko: «Looks like this just got pretty interesting» | gancho |
| Tráiler | 1:06 | Primer plano de ojos: «Now we're even» | tensión |
| Tráiler | 1:30 | Créditos del staff: Hayashi, Kobayashi, Akita, TECHNOBOYS, MAPPA | dato |

Enlaces con minuto: [tráiler, 0:36](https://www.dailymotion.com/video/x88p1dp?start=36)
y [tráiler, 1:30](https://www.dailymotion.com/video/x88p1dp?start=90).
Los minutos vistos coinciden con los del subtítulo (tabla 2.2) con 1 a 8
segundos de diferencia.

### 2.1 El sistema del colegio = el sistema de un bot

| Escena | Minuto | Qué se dice (Netflix inglés / japonés) | Para qué sirve |
|---|---|---|---|
| 1×01 | 00:00:03 | Suzui presenta el colegio: «Hyakkao Private Academy», 私立百花王学園, «a punto de cumplir 122 años» | Voz en off de apertura |
| 1×02 | 00:03:42 | «Donations are made to the student council, which controls all the gambling» | El consejo controla todo el juego = el bot |
| 1×02 | 00:03:46 | «The amount you donate determines your rank. Rankings are announced on an irregular basis» | **Ranking de economía** |
| 1×02 | 00:03:51 | «If you're in the bottom 100 of the 3,000-strong student body…» → «house pet» (家畜) | Los últimos del ranking |
| 1×02 | 00:03:59 | 家畜の名前は 男ならポチ 女ならミケ: los chicos son **Pochi**, las chicas **Mike** | Placa de mascota |
| 1×02 | 00:04:59 | «That's when the donation and Fido-Mittens systems were created» | Origen del sistema |
| 1×02 | 00:08:06 | 生徒会発行の 100万円チップ 20枚: **veinte fichas de un millón emitidas por el consejo** | **Las fichas las emite el consejo** |
| 1×03 | 00:24:09 | Sayaka anuncia, en el avance del ep. 4: «We call it the Debt Swap Game» (借金つけかえゲーム) | Anuncio de un juego |
| 2×02 | 00:04:32 | Runa por megafonía: «みんな こんにちは〜! 選挙管理委員長 黄泉月るなで〜す 掲示は見てくれたかな?» (Hola a todos, soy Runa, jefa de la comisión electoral. ¿Vieron el aviso?) | **Anunciar un sorteo** |
| 2×05 | 00:07:01 | Kirari: «オールイン» (all in), dos veces | Apostarlo todo |

### 2.2 El voto a piedra, papel o tijera (1×01): la mesa del plan

Es el primer juego de la serie, contra Mary. Encaja con **juegos**,
**sorteos** y **economía** a la vez.

| Minuto | Qué pasa |
|---|---|
| 00:06:31 | Mary: «It's called Ballot Rock-Paper-Scissors, a gambling game that our class devised» |
| 00:06:38 | Cada compañero **dibuja piedra, papel o tijera en una carta** |
| 00:06:44 | «Then they drop those cards **into the box** so we can't see them» |
| 00:06:48 | «We both **draw three cards from the box**, choose just one» |
| 00:07:11 | Yumeko: 楽しそう! ぜひ やってみたいです («Sounds fun! I'd love to try it») |
| 00:07:18 | Mary a Suzui: «Fido, fetch the chips» |
| 00:07:31 | Mary: «**These are the chips.** The rate is 10,000 yen per chip. For starters, here are 120 of them» |
| 00:11:19 | Mary se burla: «Oh, my, Jabami. I see you've run out of chips» |
| 00:12:08 | Yumeko: «Insanity is the essence of gambling, right?» |
| 00:12:37 | Yumeko: さあ 賭け狂いましょう! «**Now, then, let's get our gambling freak on**» |
| 00:15:02 | Yumeko destapa la trampa: «Your methods are crude» |
| 00:22:32 | ギャンブル狂 / 賭け狂いだ: «A gambling freak… A compulsive gambler!» |

La caja de cartas es **un sorteo**: la mano sale de una caja, sin mirar.
Tres cartas = **tres bloques** del canal (juegos, sorteos, economía).

### 2.3 Otros juegos, por si hace falta otra mesa

| Episodio | Minuto | Juego |
|---|---|---|
| 1×02 | 00:07:40 | ダブル神経衰弱: **memoria doble** con dos barajas |
| 1×03 | 00:06:08 | 生か死か: se apuesta **en qué agujero entra la espada**, con fichas |
| 1×04 | 00:13:40 | ２枚インディアンポーカー: **póquer indio de dos cartas**, fichas de colores |
| 1×10 | 00:05:15 | póquer donde se puede **invertir el orden de las manos** |
| 1×12 | 00:08:00 | «The name of this gamble is… **the Tarot Cards of Fate**» |
| 2×01 | 00:00:18 | 指切りギロチン: la **guillotina de dedos** (evítala: ver §14) |
| 2×03 | 00:07:31 | Ririka: «100票ある»: **cien votos** en juego, adivinar dónde están |

Títulos de los capítulos (Netflix inglés, dentro del subtítulo):
«Lame Girl» (1×02), «Slit-Eyed Woman» (1×03), «The Girl Who Became a House
Pet» (1×04), «The Girl Who Became Human» (1×05), «The Inviting Girl» (1×06),
«The Girls That Refuse» (1×07), «Dreaming Girl» (1×09), «The Girl Who
Chooses» (1×10), «The Girl Who Would Stake Her Life» (1×11), «The Woman Who's
a Compulsive Gambler» (1×12). En japonés, en
[Syoboi (T1)](https://cal.syoboi.jp/tid/4623/subtitle) y
[Syoboi (××)](https://cal.syoboi.jp/tid/5151/subtitle).

---

## 3 · Arte oficial y referencias visuales

No pude abrir ninguna página con imágenes. Lo que sigue son **fichas de
dónde está cada cosa**, con lo que dicen los resultados de búsqueda.

### 3.1 Key visuals del anime

- **T1 (2017)**: la web oficial guarda los personajes en
  [kakegurui-anime.com/1st/character](https://kakegurui-anime.com/1st/character/)
  y el equipo en [1st/caststaff](https://kakegurui-anime.com/1st/caststaff/).
- **×× (2019)**: key visual con **23 personajes**: Yumeko y Kirari arriba,
  los del primer arco y **11 nuevos**; abajo, la familia Momobami. Se
  publicó el **20 de noviembre de 2018** ✅
  ([LisAni!](https://www.lisani.jp/0000117737/),
  [Animate Times](https://www.animatetimes.com/news/details.php?id=1542685544)).
  Con **hojas de personaje** de los nuevos en
  [PASH! PLUS](https://www.pashplus.jp/anime/117240/). Personajes de ××:
  [kakegurui-anime.com/character](https://kakegurui-anime.com/character/group01.php).
- **Twin (2022)**: la precuela con Mary de protagonista. Tráiler oficial
  de Netflix en [YouTube](https://www.youtube.com/watch?v=yihlMRSUiCo).

### 3.2 Blu-ray y cajas

- El Blu-ray 1 de la T1 trae **una cubierta dibujada por Manabu Akita**, el
  diseñador de personajes. Amazon Japón regalaba por comprar todos **una
  caja dibujada con Yumeko y Mary** ✅
  ([Amazon.co.jp](https://www.amazon.co.jp/%E3%80%90Amazon-co-jp%E9%99%90%E5%AE%9A%E3%80%91%E8%B3%AD%E3%82%B1%E3%82%B0%E3%83%AB%E3%82%A4-%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E5%84%AA%E5%85%88%E5%85%88%E8%A1%8C%E5%8F%97%E4%BB%98%E7%94%B3%E8%BE%BC%E5%88%B8%E4%BB%98-%E5%85%A8%E5%B7%BB%E8%B3%BC%E5%85%A5%E7%89%B9%E5%85%B8-%E3%80%8C%E6%8F%8F%E3%81%8D%E4%B8%8B%E3%82%8D%E3%81%97%E5%85%A8%E5%B7%BB%E5%8F%8E%E7%B4%8DBOX%E3%80%8D%E5%BC%95%E6%8F%9B%E3%82%B7%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%B3%E3%83%BC%E3%83%89%E4%BB%98-Blu-ray/dp/B07356KN1N),
  [web oficial, BD](https://www.kakegurui-anime.com/1st/discography/detail.php?id=1015051)).
- Otra edición trae una **caja de tres lados dibujada por Tōru Naomura**, el
  dibujante del manga ⚠️
  ([web oficial](https://kakegurui-anime.com/1st/discography/detail.php?id=1015068)).
- ××: Blu-ray BOX en [la web oficial](https://kakegurui-anime.com/discography/detail.php?id=1016327)
  y en la tienda de MBS [Animaru](https://animaru.jp/anmr/product/P0091266).

### 3.3 El manga (Tōru Naomura)

- Capítulo 1 **oficial y gratis** en
  [pixiv Comic](https://comic.pixiv.net/viewer/stories/4693) («蛇喰夢子という女»).
  Es la mejor referencia para ver **cómo son los globos** del manga.
- Página de la serie en [Gangan Joker](https://magazine.jp.square-enix.com/joker/series/kakegurui/).
- Ilustración de Naomura para el tomo 13: **Amabie con el uniforme de
  Hyakkaou** ([X de Gangan Joker](https://x.com/gangan_joker/status/1274992545651585024)).
- Portada y color de Gangan Joker enero 2020 ([Neowing](https://www.neowing.co.jp/product/NEOBK-2392751)).
- Lista de tomos en [la wiki de Fandom](https://kakegurui.fandom.com/wiki/List_of_Kakegurui_Volumes).
  Yen Press lo publica en inglés desde 2015.

### 3.4 Objetos oficiales que existen de verdad

Útiles para modelar en Blender sin inventar:
- **«賭ケグルイ オールスター箔押しトランプ»**: baraja oficial con todos los
  personajes y **estampado metálico** ⚠️ ([ficha](https://www.qsab.se/qnqsagh-282857ditems/etid.html),
  [Amazon: baraja](https://www.amazon.co.jp/%E3%83%8E%E3%83%BC%E3%83%96%E3%83%A9%E3%83%B3%E3%83%89%E5%93%81-%E8%B3%AD%E3%82%B1%E3%82%B0%E3%83%AB%E3%82%A4-%E3%83%88%E3%83%A9%E3%83%B3%E3%83%97/dp/B0BWWQ1C4G),
  [Amazon: cartas estilo baraja](https://www.amazon.co.jp/%E3%83%8E%E3%83%BC%E3%83%96%E3%83%A9%E3%83%B3%E3%83%89%E5%93%81-%E8%B3%AD%E3%82%B1%E3%82%B0%E3%83%AB%E3%82%A4-%E3%83%88%E3%83%A9%E3%83%B3%E3%83%97%E9%A2%A8%E3%82%AB%E3%83%BC%E3%83%89/dp/B0D97K7D6J)).
- Tarjetas del consejo estudiantil ([Amazon](https://www.amazon.co.jp/%E3%83%8E%E3%83%BC%E3%83%96%E3%83%A9%E3%83%B3%E3%83%89%E5%93%81-m49584524914-%E8%B3%AD%E3%82%B1%E3%82%B0%E3%83%AB%E3%82%A4-%E7%94%9F%E5%BE%92%E4%BC%9A-%E3%82%A4%E3%83%A9%E3%82%B9%E3%83%88%E3%82%AB%E3%83%BC%E3%83%89/dp/B0CL5939C8)).
- Tienda oficial de licencias: [Colleize](https://colleize.com/lineup/1072).

### 3.5 Lo que falta ⚠️

- No vi **ninguna imagen**: ni key visuals, ni portadas de tomos, ni hojas
  de modelo. Con red abierta, corre `investigar_serie.py --wiki kakegurui`
  con Yumeko, Mary, Kirari, Ririka, Midari, Runa y «Student Council».
- No sé **qué personaje va en cada portada** de los tomos.
- No encontré un **artbook** de Naomura. Sí hay fanbook oficial,
  «賭ケグルイ愛(ラブ)», que trae los resultados del concurso de popularidad ⚠️.

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D de objetos para la mesa (Sketchfab)

La licencia es la que dice el resultado de búsqueda. **Ábrela en la página
antes de usarla** y copia el crédito tal cual.

| Modelo | Autor | Licencia | Para qué |
|---|---|---|---|
| [Low Poly Poker Chips & Cards](https://sketchfab.com/3d-models/low-poly-poker-chips-cards-8420090cc79a49d9a0b85f53c5074616) | Designed By Jonathan (@designedbyjonathan) | CC BY ✅ según la búsqueda | fichas y cartas de relleno |
| [Casino Poker Chip](https://sketchfab.com/3d-models/casino-poker-chip-b9efab875b9c4ac3a29ea5a0c7a260d1) | lejonlin | CC BY ✅ según la búsqueda | la ficha del consejo, en primer plano |
| [Casino Poker Table](https://sketchfab.com/3d-models/casino-poker-table-f36fc75d825148618aa6e5cbfb43f28e) | Nathan Powell (@npowell) | CC BY ✅ según la búsqueda | la mesa |
| [Stylized Poker Table](https://sketchfab.com/3d-models/stylized-poker-table-game-asset-48fd86c57c2b497a900223d8f115f188) | Morgan.J (@MorganJ45) | CC BY ✅ según la búsqueda | mesa, fichas, cartas y sillas |
| [Poker Table](https://sketchfab.com/3d-models/poker-table-a48473a5ae7c437496a7aa388f8c458b) | Pieter Ferreira (@Badboy17Aiden) | gratis, licencia ⚠️ | baraja entera y fichas, texturas 2048 |
| [Poker Chip Set](https://sketchfab.com/3d-models/poker-chip-set-b0cbee32720046e7b1e480cff44a5d41) | matveuk (@anna_bezzu) | gratis, licencia ⚠️ | juego de fichas |
| [Poker Chip 500$](https://sketchfab.com/3d-models/poker-chip-500-3cd4d3b00c0349ad978d0c81d8f95409) | matveuk (@anna_bezzu) | gratis, licencia ⚠️ | ficha de valor alto |

Crédito tipo (CC BY): «"Casino Poker Chip" by lejonlin, CC BY 4.0, sketchfab.com».
Comprueba la versión de la licencia en la página.

### 4.2 Modelos 3D de personajes (sólo para mirar poses)

- [Yumeko](https://sketchfab.com/3d-models/yumeko-9834761e49a346cba73c8e1d9ab40122) de Yaanaa (Sketchfab).
- [Mary Saotome](https://sketchfab.com/3d-models/mary-saotome-62bf9b36b5b64c29b27c8eadea263417) de Acutee (Sketchfab).
- [Runa Yomozuki](https://sketchfab.com/models/70dafed89bcd4dd3b9f5654f90ebeef3/embed) de Gustav_Johansson00.
- Etiqueta [kakegurui en Sketchfab](https://sketchfab.com/tags/kakegurui).
- MMD de Yumeko, Mary y Kirari: [HatsuneDKaname en DeviantArt](https://www.deviantart.com/hatsunedkaname/art/Kakegurui-X-MMD-TDA-Yumeko-Mary-Kirari-DL-831077003).

Son personajes con copyright: **nunca en la lámina**, sólo para girar la
cámara y entender una pose.

### 4.3 Fan art 2D (mirar, nunca pegar)

| Obra | Autor | Qué tiene |
|---|---|---|
| [Kirari, dibujo tradicional](https://www.deviantart.com/william-art/art/Kirari-Momobami-Kakegurui-Traditional-Drawing-814756754) | William-Art (DeviantArt) | Kirari a lápiz |
| [Saotome Mary](https://www.artstation.com/artwork/6bG446) | ArtStation | Mary, hecha tras ver Twin |
| [Mary Saotome](https://www.deviantart.com/esmerald1/art/Kakegurui-Mary-Saotome-969430937) | Esmerald1 (DeviantArt) | Mary en el casino, segura y relajada |
| [Mary, a lápiz](https://www.artstation.com/artwork/mA12vv) | ArtStation | Mary |
| [Yumeko (fanart)](https://www.artstation.com/artwork/8xavw) | keith zarraga (ArtStation) | Yumeko |
| [Yumeko preview](https://www.artstation.com/artwork/eodaG) | Raed D (ArtStation) | Yumeko |
| [Yumeko, abril 2025](https://www.pixiv.net/en/artworks/129414635) | pixiv | Yumeko |
| [「賭ケグルイ ミケ」](https://www.pixiv.net/en/artworks/75267959) | pixiv | la placa de Mike |

En pixiv hay **1.646 dibujos** con la etiqueta
[賭ケグルイ 蛇喰夢子](https://www.pixiv.net/en/tags/%E8%B3%AD%E3%82%B1%E3%82%B0%E3%83%AB%E3%82%A4%20%E8%9B%87%E5%96%B0%E5%A4%A2%E5%AD%90).
Los más votados: etiqueta
[賭ケグルイ1000users入り](https://www.pixiv.net/en/tags/%E8%B3%AD%E3%82%B1%E3%82%B0%E3%83%AB%E3%82%A41000users%E5%85%A5%E3%82%8A).

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

| Sitio | Qué sé | Fuente |
|---|---|---|
| **Academia Privada Hyakkaou** (私立百花王学園) | **122 años**, «tradition and prestige» (伝統と格式) | ✅ subtítulo 1×01, 00:00:06 |
| Sus lazos | «heavy connections in the financial and political worlds» (政財界) | ✅ subtítulo 1×04, 00:03:49 |
| Alumnos | **3.000** | ✅ subtítulo 1×02, 00:03:51 |
| El edificio por dentro | Antes de Kirari era **un colegio japonés tradicional**; ahora es **moderno y de estilo occidental** | ⚠️ [Fandom](https://kakegurui.fandom.com/wiki/Hyakkaou_Private_Academy) |
| **Sala del consejo estudiantil** | Kirari adora los peces tropicales: hay **un acuario enorme** | ⚠️ [Fandom: Student Council](https://kakegurui.fandom.com/wiki/Student_Council) |
| Aula de **2.º, clase Flor** | La clase de Yumeko, Mary y Suzui | ✅ subtítulo 1×01, 00:12:52 («Year Two, Flower Class») |
| Club de Cultura Tradicional (伝文研) | El club de Yuriko, con su propio fondo de dinero | ✅ subtítulo 1×03, 00:16:31 |
| **Escalera central** | Kirari monta un juego allí: «no tiene puertas a los pisos de en medio» | ✅ subtítulo 2×09, 00:11:16 |
| Tablón de avisos (掲示) | Runa pregunta por megafonía si vieron el aviso | ✅ subtítulo 2×02, 00:04:40 |

Staff de fondos y color, de la web oficial ✅
([T1](https://kakegurui-anime.com/1st/caststaff/),
[××](https://kakegurui-anime.com/caststaff/),
[Anime@wiki](https://w.atwiki.jp/anime_wiki/pages/23218.html)):
- **Dirección de arte**: Haruka Matsuda y Masanobu Nomura (T1); Haruka Matsuda (××).
- **Color**: Chikako Kamata (T1); Ayako Suenaga (××).
- **Diseño de personajes y supervisión de animación**: Manabu Akita.
- **Director**: Yūichirō Hayashi. **Estudio**: MAPPA.

### 5.2 Luz ⚠️

No vi fotogramas. De memoria, y hay que comprobarlo:
- Las partidas se ven en **interiores cálidos** con sombras duras.
- Cuando alguien «se vuelve loco», el fondo cambia a **plano de color o
  negro**, con un **brillo rojo** en los ojos.
- La sala del consejo: si el acuario es real, da una **luz azul verdosa**
  que se mueve. Es la mejor baza para que la lámina no quede plana.

### 5.3 Paleta

**Uniforme** (paleta publicada en
[color-hex.com](https://www.color-hex.com/color-palette/103520),
«Kakegurui Uniform») ⚠️ una fuente, medida por un fan:

| Hex | Qué es |
|---|---|
| `#C9020F` | rojo de la chaqueta |
| `#292329` | negro del ribete y de la falda |
| `#1E181C` | negro más profundo |
| `#F2DED2` | piel clara |
| `#F7F6FD` | blanco de la camisa |

El uniforme, según [Fandom](https://kakegurui.fandom.com/wiki/Yumeko_Jabami):
**chaqueta roja con ribete negro** en puños y cuello, camisa blanca,
**corbata negra cruzada**, **falda a cuadros negra y gris**, medias negras y
mocasines marrones ⚠️.

Colores de cada personaje ⚠️ (**sin medir**, de memoria: muestréalos en un
fotograma antes de usarlos):

| Personaje | Rasgo | Hex aproximado |
|---|---|---|
| Yumeko | ojos rojos encendidos | alrededor de `#E0102A` |
| Mary | coletas rubias | alrededor de `#E8C15A` |
| Kirari | pelo gris muy claro, **labios azules** | pelo `#D8D8DE`, labios `#3E5FB0` |
| Ririka | máscara gris | alrededor de `#8E8E94` |

Un fan de Tumblr asigna **un color a cada personaje** (Yumeko = rojo):
[kiraris-fish-tank](https://www.tumblr.com/kiraris-fish-tank/163196515310/kakegurui-color-theory-yumeko-jabamired) ⚠️.

### 5.4 Texturas reales equivalentes

| Material | Enlace | Licencia |
|---|---|---|
| **Tapete de fieltro** (paño de billar) | [TextureCan 527](https://www.texturecan.com/details/527/) | gratis, PBR ⚠️ comprobar |
| Más tapetes y «casino» | [TextureCan: Felt](https://www.texturecan.com/tag/Felt/), [Casino](https://www.texturecan.com/tag/Casino/) | gratis ⚠️ |
| Tela | [ambientCG Fabric 031](https://ambientcg.com/view?id=Fabric031) | **CC0** ✅ (ambientCG es CC0) |
| Madera de mesa gastada | [Poly Haven: wood_table_worn](https://polyhaven.com/a/wood_table_worn) | CC0 ⚠️ comprobar |
| Catálogo | [Poly Haven](https://polyhaven.com/textures), [ambientCG](https://ambientcg.com/) | CC0 |

Para la caja de cartas: **madera lacada roja** o **cartón negro** con canto
dorado. Para las fichas: plástico con anillo de color.

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

- **El logo en inglés** está en Wikimedia Commons:
  [Kakegurui_logo.svg](https://commons.wikimedia.org/wiki/File:Kakegurui_logo.svg).
  No lo pude abrir.
- **Nadie ha identificado su letra.** En el foro de dafont alguien la pidió y
  no quedó claro si sale de una fuente real o está dibujada ⚠️
  ([dafont](https://www.dafont.com/forum/read/415090/kakegurui-gambling-school)).
  Los sitios que dicen tener «la fuente de Kakegurui»
  ([cufonfonts](https://www.cufonfonts.com/search/kakegurui),
  [font.download](https://font.download/search/kakegurui)) no son oficiales.
- **Letras del manga**: los globos llevan la letra estándar de imprenta
  japonesa. Míralo en el [capítulo 1 oficial](https://comic.pixiv.net/viewer/stories/4693) ⚠️.

### 6.2 Letras libres comprobadas por mí

Bajé cada archivo de [google/fonts](https://github.com/google/fonts) y miré
con fontTools si trae **á é í ó ú ñ Á É Í Ó Ú Ñ ¿ ¡ ü**. Todas **sí** ✅.

| Letra | Para qué | Archivo |
|---|---|---|
| **Playfair Display** (Black) | Título «Comandos y sorteos»: serif de alto contraste, de colegio de élite | [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/playfairdisplay/METADATA.pb) |
| **Bodoni Moda** | **Cifras de fichas y esquinas de cartas** | [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/bodonimoda/METADATA.pb) |
| **Cormorant Garamond** | Texto de los **papeles del consejo** | [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/cormorantgaramond/METADATA.pb) |
| **Cinzel** | Sellos y palos en mayúsculas | [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/cinzel/METADATA.pb) |
| **Oswald** | **Placa de mascota** («MININA 0001») y etiquetas estrechas | [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/oswald/METADATA.pb) |
| **Shippori Mincho B1** (ExtraBold) | Un kanji o el «賭ケグルイ» de adorno | [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/shipporiminchob1/METADATA.pb) |
| **Zen Antique** | Alternativa a la anterior, más antigua | [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/zenantique/METADATA.pb) |
| **Dela Gothic One** | Onomatopeya en katakana (ざわ, ゾク) | [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/delagothicone/METADATA.pb) |

Todas con licencia **OFL** (libre, también para uso comercial).
La elección es **de estilo, no un calco del logo** ⚠️.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que la serie pone en pantalla

En Kakegurui **no hay un globo propio**: el texto aparece **sobre objetos
del juego y del colegio**. Todo esto está comprobado en los subtítulos:

| Soporte | Dónde se ve | Estado |
|---|---|---|
| **Cartas** escritas a mano y metidas en una caja | 1×01, 00:06:38 a 00:06:48 | ✅ |
| **Fichas** con su valor, emitidas por el consejo | 1×01, 00:07:31; 1×02, 00:08:06 | ✅ |
| **Placa de mascota** al cuello: «BOTTOM-FEEDER 0001 MITTENS» (así la traduce Netflix en pantalla) | 1×03, 00:20:44 | ✅ el texto; el diseño ⚠️ |
| **Papel del consejo**: el «plan de vida» (人生計画表) de Yumeko; a Mary le llega otro que la casa con un desconocido («今朝方 生徒会から こんなものが届いた», «me, getting married?») | 1×04, 00:00:48, 00:02:53 y 00:03:55 | ✅ |
| **Megafonía del colegio** (校内アナウンス) con Runa | 2×02, 00:04:32 | ✅ |
| **Tablón de avisos** (掲示) | 2×02, 00:04:40 | ✅ |
| **Rótulo del título** a mitad del capítulo («THE GIRL WHO BECAME A HOUSE PET») | 1×04, 00:04:53 | ✅ existe; el diseño ⚠️ |

Y el gesto que todos reconocen:
- **Los ojos que se vuelven rojo brillante** cuando Yumeko se emociona ✅
  ([Fandom](https://kakegurui.fandom.com/wiki/Yumeko_Jabami),
  [Animate Times, sobre el drama: «赤目で賭け狂う»](https://www.animatetimes.com/news/details.php?id=1513761386)).
- **Las caras exageradas** (顔芸, «arte de la cara») ✅
  ([4Gamer](https://www.4gamer.net/games/338/G033856/20170809048/)).
  En China el comentario típico es «暂停学颜艺», «pausa para aprender la
  cara» ✅ ([Bilibili](https://www.bilibili.com/video/av926870921/)).

### 7.2 Cómo hablan (por el subtítulo)

| Quién | Cómo habla | Ejemplo (minuto) |
|---|---|---|
| **Yumeko** | Muy educada, con «desu/masu». Sube el ritmo con «さあ» repetido antes de estallar | 1×03, 00:15:58: «さあ さあ さあ さあ! … さあ〜! 賭け狂いましょう!» |
| **Mary** | En público, falsa y dulce («あ〜ら あら»). Enfadada, **muy grosera**: «ナメやがって», «クソッ», «ウッゼ〜» | 1×01, 00:11:19 y 00:13:19; 1×04, 00:12:34 |
| **Kirari** | Frases cortas de dama («〜わ», «〜かしら»). Preguntas raras y bellas | 1×06, 00:24:09: «月の裏側って見たことある?» (¿Has visto la cara oculta de la Luna?) |
| **Ririka** (con máscara) | Seca, casi militar: «お前», «やろう» | 2×03, 00:07:36: «Si aciertas dónde están los votos, te doy estos cien» |
| **Midari** | Ruda, se ríe «**ウヘッ**» | 1×06, 00:07:48: «ウヘッ 見つけたぜ〜 夢子» |
| **Runa** | Aniñada, se ríe «**ニャハハ**», alarga las vocales | 2×02, 00:04:34: «みんな こんにちは〜!» |
| **Sayaka** | Secretaria perfecta: «会長» (presidenta) | 1×01, 00:12:52 |
| **Suzui** | Narra en off, entre paréntesis en el subtítulo | 1×01, 00:00:03 |

### 7.3 Cómo se traduce a una lámina fija

1. **Lo que dice el personaje va en una carta** que sostiene o que está
   boca arriba en la mesa. Letra: Bodoni Moda o Playfair.
2. **El nombre de quien habla, en una ficha** al lado de la carta, como
   la pestaña de nombre de un videojuego. Ficha roja para Yumeko, dorada
   para Mary, azul pálido para Kirari.
3. **Los avisos del bot** van en un **papel del consejo**, con sello rojo.
4. **La emoción** no es un globo con pinchos: es el **brillo rojo** en los
   ojos y un fondo que se oscurece detrás del personaje.
5. Si hace falta un «pensamiento», imita la voz en off de Suzui: **texto
   sin caja**, pequeño, en una esquina.

### 7.4 En los videojuegos de la franquicia

Ver §13. De sus cajas de diálogo **no encontré capturas** ⚠️.

### 7.5 Qué NO hacer con el texto

- Una **burbuja blanca redonda** flotando.
- Letras de cómic americano o redondeadas y alegres.
- Poner el «賭け狂いましょう» traducido como si fuera del doblaje latino:
  **no encontré cómo lo dice el doblaje** (ver §10).

---

## 8 · Los personajes

Datos de carácter: [Fandom](https://kakegurui.fandom.com/wiki/Yumeko_Jabami),
[TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/Kakegurui),
[Wikipedia](https://en.wikipedia.org/wiki/List_of_Kakegurui_characters),
[Namuwiki (coreano)](https://namu.wiki/w/%EC%B9%B4%EC%BC%80%EA%B5%AC%EB%A3%A8%EC%9D%B4/%EB%93%B1%EC%9E%A5%EC%9D%B8%EB%AC%BC)
y [Baidu (chino)](https://baike.baidu.com/item/%E7%8B%82%E8%B5%8C%E4%B9%8B%E6%B8%8A/14902484),
leídos a través de los resúmenes de búsqueda. Las frases, del subtítulo ✅.

### Yumeko Jabami (蛇喰夢子) — la protagonista, 5.ª en votos ⚠️

- **Quién es**: alumna nueva de 2.º, clase Flor. Educada y alegre por
  fuera. Por dentro, **adicta al riesgo**: no juega por dinero, **juega
  por la emoción** ✅ ([Fandom](https://kakegurui.fandom.com/wiki/Yumeko_Jabami),
  [Villains Wiki](https://villains.fandom.com/wiki/Yumeko_Jabami)).
- **Miedos**: casi ninguno. Lo que la aburre son **los tramposos torpes**:
  «You'll never deceive anyone unless you're prepared to shed blood!»
  (1×01, 00:15:21).
- **Qué le importa**: jugar contra alguien fuerte. Por eso busca a Kirari.
- **Con quién**: Suzui (su amigo), Mary (rival y luego aliada; CBR la
  compara con Batman y el Joker ⚠️ [CBR](https://www.cbr.com/kakegurui-yumeko-mary-relationship-joker-batman/)),
  Kirari (su gran rival). Tiene una hermana, Sōko ⚠️
  ([Bilibili](https://www.bilibili.com/video/BV1Vs4y1y7Dd/),
  [pixiv 百科](https://dic.pixiv.net/a/%E8%9B%87%E5%96%B0%E6%83%B3%E5%AD%90)).
- **Pelo negro largo con flequillo recto** («hime») y **ojos burdeos que
  se vuelven rojo brillante** ✅.
- **Cómo saluda**: «皆様 はじめまして 蛇喰夢子と申します ふつつか者ですが…»
  (Encantada, me llamo Yumeko Jabami; soy torpe, pero espero que me
  acepten) (1×01, 00:03:48).
- **Cómo se entusiasma**: «楽しそう! ぜひ やってみたいです» (1×01, 00:07:11).
- **Cómo explica**: tranquila, con datos: «You made the same play twice in
  a row when there was 500,000 yen on the line» (1×01, 00:15:06).
- **Cómo se ríe o juega**: con la placa de gata al cuello, dice
  «にゃん にゃん» (1×03, 00:21:24) y «Cats are cute, though, right?» (00:21:20).
- **Su frase**: «さあ 賭け狂いましょう!» (1×01, 00:12:38). En coreano dicen
  que la entonación de **Saori Hayami** (su voz japonesa) es **la firma de
  la serie** ⚠️ ([Namuwiki](https://namu.wiki/w/%EC%B9%B4%EC%BC%80%EA%B5%AC%EB%A3%A8%EC%9D%B4)).
- **Cuerpo** ⚠️ (de memoria): postura recta y educada; al emocionarse,
  **se sonroja, se lleva la mano a la mejilla** y se inclina hacia la mesa.

### Mary Saotome (早乙女芽亜里) — la más querida, 1.ª en votos ✅

- **Quién es**: la primera que reta a Yumeko (1×01). Pierde, **cae a
  «Mike»** (mascota) y trepa de nuevo. Es la protagonista de **Kakegurui
  Twin**, un año antes ✅ ([Fandom](https://kakegurui.fandom.com/wiki/Mary_Saotome),
  [DualShockers](https://www.dualshockers.com/kakegurui-twin-anime-netflix-spinoff-with-mary-saotome-explained/)).
- **Por qué la quieren**: tiene **el arco de un protagonista shōnen**:
  derrota, humillación y vuelta ✅ ([CBR](https://www.cbr.com/kakegurui-mary-saotome-best-girl/),
  [Screen Rant](https://screenrant.com/kakegurui-main-characters-likable/)).
- **Miedo**: volver a ser mascota; perder su sitio.
- **Defecto**: se confía demasiado ⚠️ ([CBR](https://www.cbr.com/kakegurui-twin-netflix-spoilers-mary-saotome-overconfidence-fatal-flaw/)).
- **Aspecto**: **rubia con coletas y lazos negros**, ojos amarillo oscuro ⚠️
  (sólo Fandom).
- **Cómo manda**: «ポチ… チップ持ってきて» («Fido, fetch the chips», 1×01, 00:07:18).
- **Cómo explica**: rápido y sin rodeos, con reglas y cifras: «The rate is
  10,000 yen per chip. For starters, here are 120 of them» (1×01, 00:07:33).
- **Cómo se burla**: «あ〜ら あら 蛇喰さん チップなくなっちゃったね» (1×01, 00:11:19).
- **Cómo se enfada**: «ボンボンのバカ娘が ナメやがって» (1×01, 00:13:19),
  «ウッゼ〜» (1×04, 00:12:34), «私はこいつに呪われてんのか!» (1×04, 00:13:33).
- **Cómo celebra**: «この勝負 勝てる!» (¡Esta la gano!) (2×04, 00:00:01).

### Kirari Momobami (桃喰綺羅莉) — la presidenta, 2.ª en votos ⚠️

- **Quién es**: presidenta del consejo estudiantil (la 105.ª, según
  [Baidu](https://baike.baidu.com/item/%E6%A1%83%E5%96%B0%E7%BB%AE%E7%BD%97%E8%8E%89/19838128) ⚠️).
  Creó el sistema de donaciones y de mascotas ✅
  ([Fandom: Student Council](https://kakegurui.fandom.com/wiki/Student_Council)).
- **Aspecto**: **pelo gris muy claro, ojos azules y labios azules** ✅
  ([Fandom](https://kakegurui.fandom.com/wiki/Kirari_Momobami),
  [Namuwiki](https://en.namu.wiki/w/%EB%AA%A8%EB%AA%A8%EB%B0%94%EB%AF%B8%20%ED%82%A4%EB%9D%BC%EB%A6%AC)).
- **Qué le importa**: el espectáculo de alguien que se lo juega todo:
  «人生が燃え尽きるときの 一瞬のきらめき» (el destello de una vida que se
  consume) (1×11, 00:21:16).
- **Qué la aburre**: «つまらないわね 清華… 誰かいないかしら 私を本気で殺ろうとする者»
  (Qué aburrido, Sayaka. ¿No hay nadie que intente matarme en serio?)
  (2×04, 00:20:49).
- **Con quién**: Sayaka, su secretaria, que **la ama** ✅
  ([Shipping Wiki: Kirasaya](https://shipping.fandom.com/wiki/Kirasaya)); su gemela Ririka.
- **Cómo saluda**: «お邪魔するわね» (Con permiso) (1×03, 00:17:04);
  «よく来てくれたわね みんな» (Gracias por venir, todos) (2×02, 00:00:18).
- **Cómo empieza algo**: «さて 始めましょうか» (Bien, empecemos) (1×10, 00:00:19).
- **Cómo reta**: «文句があるなら かかってくるがいい» (Si tienes quejas, ven a por mí) (1×11, 00:00:28).
- **Cómo lo apuesta todo**: «オールイン» (2×05, 00:07:01).
- **Cuerpo** ⚠️: quieta, sentada, **taza de té** en la mano (1×06,
  00:13:43: «これはセイロン島のディンブラ», un té de Ceilán).

### Ririka Momobami (桃喰リリカ) — la vicepresidenta, 4.ª en votos ⚠️

- **Quién es**: gemela de Kirari y vicepresidenta. Sale con **una máscara
  gris de teatro**: ojos almendrados y **sonrisa curva**. Pelo suelto, sin
  pintalabios ✅ ([Fandom](https://kakegurui.fandom.com/wiki/Ririka_Momobami),
  [Heroes Wiki](https://hero.fandom.com/wiki/Ririka_Momobami)).
- **Carácter**: **muy tímida**, introvertida.
- **Con máscara habla seco**: «100票ある… どちらに票があるか 当たれば
  この100票をやろう» (Tengo cien votos. Si aciertas dónde están, son tuyos)
  (2×03, 00:07:31).
- **Sin máscara se traba**: «わっ 私は… 私は…» (2×03, 00:18:05).
- **Anima**: «約束しただろう 2人でこの選挙を戦い抜くと» (Prometimos pelear
  juntas esta elección) (2×05, 00:15:33).
- ⚠️ En la serie las gemelas **se hacen pasar una por la otra**. Comprueba
  en el fotograma quién es quién.

### Los secundarios que conviene tener a mano

- **Midari Ikishima**: parche médico en el ojo izquierdo, vendas en los
  antebrazos, **revólver** del consejo. Sádica y masoquista ✅
  ([Fandom](https://kakegurui.fandom.com/wiki/Midari_Ikishima),
  [Villains Wiki](https://villains.fandom.com/wiki/Midari_Ikishima)).
  Risa «**ウヘッ**» (1×06, 00:07:48). **No sirve para este canal** (armas).
- **Runa Yomozuki**: consejo estudiantil, árbitra y **anunciadora**.
  Sudadera naranja de conejo, piruleta y consola ⚠️ (una sola fuente).
  Risa «**ニャハハ**» (1×02, 00:21:19). Hace el **anuncio por megafonía** de
  la elección (2×02, 00:04:32). **Buena para anunciar sorteos.**
- **Sayaka Igarashi**: secretaria del consejo, 3.ª en votos ⚠️. Anuncia
  juegos: «借金つけかえゲーム!» (1×03, 00:24:09, en el avance del ep. 4).
- **Ryōta Suzui**: el narrador y amigo de Yumeko. Fue «Pochi» (1×01, 00:04:23).

---

## 9 · ¿Quién es el más querido?

**Mary Saotome.** La secundaria gana a la protagonista.

| Encuesta | Resultado | Estado |
|---|---|---|
| **Oficial**: «賭ケグルイ頂上戦», Gangan Joker, 2017 ([página del avance](https://magazine.jp.square-enix.com/joker/series/kakegurui/special/1710vote.html)) | **1.ª Mary**, 2.ª Kirari, 3.ª Sayaka, 4.ª Ririka, 5.ª Yumeko | Mary 1.ª ✅ ([Tumblr que recoge el avance oficial](https://www.tumblr.com/kake-gurui/166641286590/official-kakegurui-character-popularity-poll-mid), [página de Facebook «Kakegurui» con el top 6](https://www.facebook.com/Kakegurui/posts/the-current-top-6-in-the-official-popularity-poll-has-been-posted-on-jokers-offi/1711985735502238/), resumen de la búsqueda en japonés). Del 2.º al 5.º ⚠️ (un solo resumen) |
| Análisis del voto por fans | [admiralyurii](https://www.tumblr.com/admiralyurii/182367489383/kakegurui-meta-popularity-poll-breakdown), [yun-fang-xiii](https://www.tumblr.com/yun-fang-xiii/623080819472384000/kakegurui-meta-popularity-poll-breakdown), [fuyuyuu](https://fuyuyuu.tumblr.com/post/168748945840/pkjd-kakegurui-character-popularity-poll) | no pude abrirlos |
| Votación de fans japoneses, [みんなのランキング](https://ranking.net/rankings/best-kakegurui-characters) | **1.ª Mary** | ✅ |
| Otra de fans, [ランこれ (2.ª votación)](https://rancolle.com/ranking.php?id=uid4_1639143940) | no vi el orden | ⚠️ |
| Prensa en inglés | «Mary, **best girl**» ([CBR](https://www.cbr.com/kakegurui-mary-saotome-best-girl/)); [Looper, top 10](https://www.looper.com/1040021/most-popular-kakegurui-characters-ranked/) | ✅ / ⚠️ |

El concurso oficial tuvo tres categorías: **personaje, pareja y episodio**
favoritos. Los resultados completos están en el fanbook
**«賭ケグルイ愛(ラブ)»** ⚠️.

**Pero Yumeko es la cara de los memes** (ver §14): el «kakegurui mashou»
volvió a ser viral en 2026 ✅.

**Para este canal**: Mary es la que **reparte las fichas y explica las
reglas** en el episodio 1. Es la más querida y la que mejor encaja.

---

## 10 · Doblaje latino

**Sí hay doblaje latino**, hecho en **México** por **Sysdub** para
Netflix. Fue **el primer anime que dobló Sysdub** ✅
([Doblaje Wiki: Kakegurui](https://doblaje.fandom.com/es/wiki/Kakegurui),
[Doblaje Wiki: Sysdub](https://doblaje.fandom.com/es/wiki/Sysdub),
[ANMTV](https://www.anmtvla.com/2018/02/kakegurui-ya-disponible-en-netflix-y.html)).
Llegó a Netflix el **1 de febrero de 2018** ✅.

No pude abrir la API de Doblaje Wiki (403). Los nombres salen de los
extractos de búsqueda:

| Personaje | Voz latina | Fuentes | Estado |
|---|---|---|---|
| **Yumeko Jabami** | **Jocelyn Robles** | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Kakegurui) (en la guía de cuadros) · [Voice over Wiki](https://voice-over-and-voice-acting.fandom.com/wiki/Kakegurui_(2017)) | ✅ |
| **Mary Saotome** | **Valentina Souza** | [Voice over Wiki](https://voice-over-and-voice-acting.fandom.com/wiki/Kakegurui_(2017)) · [Doblaje Wiki: Valentina Souza](https://doblaje.fandom.com/es/wiki/Valentina_Souza) | ✅ (comprobar en la API) |
| Ryōta Suzui | Ricardo Bautista | un solo extracto de búsqueda | ⚠️ dudoso |
| Saori (T1) | Gabriela Ortiz | [Doblaje Wiki: Gabriela Ortiz](https://doblaje.fandom.com/es/wiki/Gabriela_Ortiz) | ⚠️ dudoso |
| **Kirari Momobami** | **no encontrado** | | ❌ |
| **Ririka Momobami** | **no encontrado** (existe [su ficha](https://doblaje.fandom.com/es/wiki/Ririka_Momobami)) | | ❌ |
| Director de doblaje | **no encontrado** | | ❌ |

Detalles del doblaje latino (una sola fuente, Doblaje Wiki) ⚠️:
- **Pochi y Mike pasan a ser «Fido» y «Minina».** Netflix en inglés dice
  «Fido» y «Mittens» ✅ (subtítulo 1×02, 00:04:59).
- Se conserva el sufijo **«-senpai»**.
- Dicen **«fichas»**: en un capítulo Yumeko dice «apuesto 2 fichas Jabami»
  cuando había tres (un error del doblaje). La wiki lo pone en el ep. 4; en
  el subtítulo japonés el «蛇喰チップ» sale en 1×05, 00:06:54 ⚠️.

**Frases latinas**: **no encontré** con fuente cómo dice el doblaje el
«さあ 賭け狂いましょう». En portugués es «Vamos apostar até a loucura!» ⚠️.
Para el latino, mira estos vídeos con el doblaje:
[«Las Voces de KAKEGURUI»](https://www.youtube.com/watch?v=_8F1j9vb9Aw),
[Yumeko en latino](https://www.youtube.com/watch?v=di9Dv_XuXoQ),
[TikTok: la mejor escena en latino](https://www.tiktok.com/@the_boy_of_hearts/video/6920293973768654085).
**Minuto sin verificar.**

Otros doblajes y obras:
- **Kakegurui Twin** también tiene doblaje latino en Netflix ✅
  ([ANMTV](https://www.anmtvla.com/2022/08/kakegurui-twin-ya-esta-disponible-en.html),
  [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Kakegurui_Twin)).
- Hay **doblaje de España** y alguien comparó los dos
  ([Centurión el Mago Oscuro](https://centurionelmagooscuro.home.blog/2019/09/15/versus-doblaje-latino-vs-doblaje-castellano-i-kakegurui-temporadas-1-y-2/),
  [TikTok](https://www.tiktok.com/@kira.bug/video/6917750424757931269)).
- La serie de imagen real estadounidense **«Apuesta»** («Bet», 2025) tiene
  su propia ficha ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Apuesta)).
- **Para un servidor de doblaje**: en TikTok hay **retos de doblaje** con
  Yumeko y Mary ([@jarigrt](https://www.tiktok.com/@jarigrt/video/7344802281633746181)).

---

## 11 · Música

| Tema | Quién | Estado |
|---|---|---|
| **Opening T1**: «Deal with the devil» | **Tia**; producción de **TeddyLoid** ⚠️ | ✅ ([Fandom](https://kakegurui.fandom.com/wiki/Deal_with_the_Devil), [J-pop Wiki](https://jpop.fandom.com/wiki/Deal_with_the_devil), [Suruga-ya: el CD](https://www.suruga-ya.com/en/product/120114449)) |
| **Ending T1**: «LAYon-theLINE» | **D-selections** | ✅ |
| **Opening ××**: «コノユビトマレ» | JUNNA | ⚠️ un resumen |
| **Ending ××**: «AlegriA» | D-selections | ⚠️ un resumen |
| **Banda sonora** | **TECHNOBOYS PULCRAFT GREEN-FUND** | ✅ |

- Letra de «Deal with the devil»: [animesonglyrics](https://www.animesonglyrics.com/kakegurui/deal-with-the-devil).
  TeddyLoid, según [un TikTok](https://www.tiktok.com/@tunerune.jp/video/7381491312874261765) ⚠️.
- **Ambiente** ⚠️ (de memoria): el opening es electrónico, rápido y
  descarado, con coros. La banda sonora sube la tensión con cuerdas y
  percusión en cada apuesta.
- En TikTok, «Deal with the devil» es **el audio de los edits** de Yumeko ✅
  ([TikTok: edits](https://www.tiktok.com/discover/deal-with-the-devil-from-kakegurui-edit),
  [el audio](https://www.tiktok.com/music/deal-with-the-devil-kakegurui-6812060954390498053?lang=en)).

---

## 12 · Vídeos

| Vídeo | Qué es | Minuto útil |
|---|---|---|
| [Tráiler T1, sub. latino (Netflix)](https://www.youtube.com/watch?v=6Fy2WFWNYrA) | tráiler | sin verificar |
| [Tráiler oficial, sub. español](https://www.youtube.com/watch?v=hZ27-_1lf-8) | tráiler | sin verificar |
| [Tráiler oficial de Twin (Netflix)](https://www.youtube.com/watch?v=yihlMRSUiCo) | Mary protagonista | sin verificar |
| [Las Voces de KAKEGURUI](https://www.youtube.com/watch?v=_8F1j9vb9Aw) | reparto latino | sin verificar |
| [«No le importa perder, le importa sentir»](https://www.youtube.com/watch?v=qDDltVILCNY) | psicología de Yumeko, en español | sin verificar |
| [«¿Yumeko, la mente más peligrosa?»](https://www.youtube.com/watch?v=MkZNbCG4cmo) | análisis en español | sin verificar |
| [Resumen en 11 minutos](https://www.youtube.com/watch?v=QHRBimft-nk) | resumen en español | sin verificar |
| [Reseña sin spoilers](https://www.youtube.com/watch?v=UU-fuuwCUSU) | reseña en español | sin verificar |
| [Bilibili: las caras de Yumeko](https://www.bilibili.com/video/av926870921/) | recopilación de 颜艺 | sin verificar |
| [Bilibili: «cambio de cara en un segundo»](https://www.bilibili.com/video/BV1t4411x787) | recopilación | sin verificar |
| [TikTok: caras de Yumeko](https://www.tiktok.com/@parkozue/video/7597656119984540949) | recopilación | sin verificar |

**Los minutos exactos útiles están en §2 y §15**, sacados del subtítulo de
cada episodio. Para la escena más icónica: **1×01, 00:12:08 a 00:12:38**.

---

## 13 · Videojuegos de la franquicia

### Kakegurui ALL IN (2026) — el más útil para este canal

- **Tablero de «sugoroku» estratégico** en el navegador (G123), de **CTW**.
  Salió el **23 de marzo de 2026** ✅
  ([4Gamer](https://www.4gamer.net/games/889/G088912/20260323017/),
  [G123](https://g123.jp/news/article/443079?lang=en),
  [AOL / nota de prensa](https://lite.aol.com/entertainment/story/0022/20260323/9676296.htm)).
- Se tiran **dados**, se compran casillas y **el que cae en la tuya paga
  peaje**. Hay **cartas**, **monedas**, objetos y habilidades por personaje.
  Más de **40 personajes** ✅
  ([Fandom](https://kakegurui.fandom.com/wiki/Kakegurui_ALL_IN),
  [OnlineGame-pla](https://onlinegame-pla.net/kakegurui-allin/)).
- Lema de la preinscripción: **«Now… I leave it all up to you!»**
  ([G123](https://g123.jp/news/article/173797?lang=en),
  [Comfy Cozy Gaming](https://www.comfycozygaming.com/2025/03/08/press-release-kakegurui-all-in/)).
- Cuenta oficial: [@kakegurui_allja](https://x.com/kakegurui_allja?lang=ja).
- **Es casi un bot de economía**: dados, monedas y ranking.
- Interfaz y cajas de diálogo: **no las vi** ⚠️.

### Kakegurui Cheating Allowed (2018-2020)

- App de móvil de **Avex Pictures** ([web](https://kakegurui-ca.com/)).
  Juegos del anime: **voto a piedra, papel o tijera** e «Indian Hold'em».
  Duelos entre jugadores con **trampas** («イカサマ») como habilidades.
  Las **fichas** ganadas se gastan en la **gacha** ✅
  ([Famitsu App](https://app.famitsu.com/20181122_1382832/),
  [4Gamer](https://www.4gamer.net/games/390/G039052/20181120057/)).
- **Cerró el 27 de marzo de 2020** ✅
  ([4Gamer](https://www.4gamer.net/games/390/G039052/20200123134/)).
- Interfaz: **no la vi** ⚠️. La web oficial y la Wayback Machine dan 403.

### Juegos de fans en GitHub (para ideas de minijuegos del bot)

- [akay25/kakegurui](https://github.com/akay25/kakegurui): juego de **memoria** por turnos.
- [ravener/three-hit-dice](https://github.com/ravener/three-hit-dice): el **«Three Hit Dice»** de Twin.
- [kimmyungsup/DQN_kakegurui_NimZero](https://github.com/kimmyungsup/DQN_kakegurui_NimZero): el **Nim Type Zero**.
- [EvannBerthou/War](https://github.com/EvannBerthou/War): «War game from Kakegurui».
- [kakegurui-club/shuffle](https://github.com/kakegurui-club/shuffle): utilidades para **barajar**.

No busqué en The Cutting Room Floor: son juegos de navegador y móvil, y el
cupo de búsquedas no daba ⚠️.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### Lo que todos reconocen

- **«さあ 賭け狂いましょう»** y la voz de Saori Hayami.
- **En 2026 la serie volvió a ser viral** por el audio «kakegurui mashou» ✅
  ([CBR](https://www.cbr.com/netflix-psychological-thriller-anime-kakegurui-meme/),
  [Know Your Meme](https://knowyourmeme.com/memes/kakegurui-masho-kakeguruimashou-trend)).
- **Las caras**: «pausa para aprender la cara» ✅.
- **Mary**, la «best girl». La pareja **Kirari y Sayaka** («Kirasaya»).
- **Pochi y Mike** (Fido y Minina): las placas de mascota.
- **Los ojos rojos** de Yumeko.
- Los **retos de doblaje** con Yumeko y Mary en TikTok.

### Qué NO hacer (lo que un fan notaría)

- **El meme de 2026 es sexual**: Yumeko agarrándose el pecho mientras dice
  la frase ✅ ([Know Your Meme](https://knowyourmeme.com/editorials/guides/what-is-the-yumeko-grabbing-her-chest-meme-the-context-of-the-viral-kakegurui-memes-explained)).
  **No lo uses**. Know Your Meme lo sitúa en el ep. 2 de ××; en el archivo
  de Netflix la frase está en **2×01, 00:14:44**, en el juego de la
  guillotina de dedos ⚠️.
- **Nada de la serie de EEUU «Bet»**: los fans la odian ✅
  ([Screen Rant](https://screenrant.com/kakegurui-live-action-anime-netflix-embarassing-insult-op-ed/),
  [ANN](https://www.animenewsnetwork.com/review/bet/live-action-streaming-series/.224789)).
  Tenía 67 % en Rotten Tomatoes en enero de 2026 ⚠️
  ([CBR](https://www.cbr.com/netflix-live-action-anime-kakegurui-almost-great/)).
- **Yumeko no insulta.** Incluso cuando se emociona, habla con educación («〜ましょう»).
- **Kirari no sonríe con calidez.** Sonríe como quien mira una pecera.
- **No quites la máscara a Ririka** sin avisar: es un giro de la serie.
- **Armas, guillotinas y autolesiones** (Midari): fuera de un canal de bots.
- **La placa de «Minina» nunca contra un usuario**: la broma es sobre el
  personaje, no sobre quien lee.
- Colores alegres, pastel o chibis.

---

## 15 · Poses analizadas por personaje

El minuto y la frase son del subtítulo ✅. **La postura, las manos y la
mirada las describo de memoria ⚠️**: abre el capítulo en ese minuto y
confírmalo antes de calcar nada. Es lo primero que hay que hacer con red.

### Yumeko

| # | Escena | Qué pasa | Pose a buscar ⚠️ | Sirve para |
|---|---|---|---|---|
| 1 | 1×01, 00:03:47 | Se presenta a la clase | de pie, recta, manos juntas delante, leve reverencia, sonrisa | **presentar** |
| 2 | 1×01, 00:07:11 | «楽しそう! ぜひ やってみたいです» | manos juntas junto a la cara, ojos brillantes | **animar** |
| 3 | 1×01, 00:12:08 a 00:12:31 | Discurso: «Insanity is the essence of gambling» | se inclina sobre la mesa, cara en sombra, ojos que empiezan a enrojecer | **explicar** |
| 4 | 1×01, 00:12:37 | «さあ 賭け狂いましょう!» | ojos rojos, sonrojo, mano en la mejilla o abierta hacia el rival | **celebrar** |
| 5 | 1×01, 00:15:02 | «Your methods are crude» | tranquila, señala a Mary con la mirada, mano abierta | **regañar** |
| 6 | 1×03, 00:15:58 a 00:16:07 | «さあ さあ さあ…» | cuerpo hacia delante, brazos abiertos, empuja al rival | **animar** |
| 7 | 1×03, 00:21:20 a 00:21:24 | con la placa de gata: «にゃん にゃん» | manos en forma de pata, sonrisa | humor, **presentar** reglas |
| 8 | 1×10, 00:22:19 | «さあ 皇さん 私と共に賭け狂いましょう» | mano tendida, invita | **animar** |
| 9 | 1×12, 00:18:15 | «さあ… 賭け狂いましょう» ante Kirari | frente a frente, calma | **pensar** |

### Mary

| # | Escena | Qué pasa | Pose a buscar ⚠️ | Sirve para |
|---|---|---|---|---|
| 1 | 1×01, 00:06:31 | Explica el voto a piedra, papel o tijera | de pie junto al pupitre, un dedo arriba, segura | **explicar** |
| 2 | 1×01, 00:07:18 | «Fido, fetch the chips» | brazos cruzados, mirada de reojo | **regañar** |
| 3 | 1×01, 00:07:31 | «These are the chips» | mano sobre las pilas de fichas | **presentar** economía |
| 4 | 1×01, 00:11:19 | «あ〜ら あら… チップなくなっちゃったね» | mano en la boca, burla | burla |
| 5 | 1×01, 00:13:19 | «ボンボンのバカ娘が ナメやがって» | **cara deformada de rabia** (顔芸), dientes | **regañar** |
| 6 | 1×01, 00:16:59 | «なんで こんなことになった?» | manos en la cabeza, sudor | **pensar**, pánico |
| 7 | 1×04, 00:13:33 | «私はこいつに呪われてんのか!» | puño, cara cómica | humor |
| 8 | 1×04, 00:14:57 | «私のチップは１枚500万» | ficha entre los dedos | **presentar** economía |
| 9 | 2×04, 00:00:01 | «この勝負 勝てる!» | puño cerrado, sonrisa | **celebrar** |
| 10 | 2×05, 00:15:27 | «ついてくんなっつってんだろ!» | se gira, señala | **regañar** |

### Kirari

| # | Escena | Qué pasa | Pose a buscar ⚠️ | Sirve para |
|---|---|---|---|---|
| 1 | 1×01, 00:12:59 | Sayaka le informa de la alumna nueva | sentada, apenas mira | **pensar** |
| 2 | 1×03, 00:17:04 | «お邪魔するわね» | entra por la puerta, erguida | **presentar** |
| 3 | 1×06, 00:13:43 | El té de Ceilán | taza en la mano, piernas cruzadas | **explicar** con calma |
| 4 | 1×06, 00:24:09 | «月の裏側って見たことある?» | mirada perdida, cara de lado | **pensar** |
| 5 | 1×10, 00:00:19 | «さて 始めましょうか» | manos en la mesa, empieza | **presentar** |
| 6 | 1×11, 00:00:28 | «文句があるなら かかってくるがいい» | de pie, desafía | **regañar** |
| 7 | 1×11, 00:16:20 | «ショウダウン» | enseña las cartas | **celebrar** |
| 8 | 2×01, 00:19:18 | «生徒会を解散しようと思うの» | anuncio ante todos | **anunciar** |
| 9 | 2×05, 00:07:01 | «オールイン» | empuja las fichas | **sorteo**, apostar todo |

### Ririka

| # | Escena | Qué pasa | Pose a buscar ⚠️ | Sirve para |
|---|---|---|---|---|
| 1 | 2×03, 00:07:31 | «100票ある» | máscara, votos en la mano | **presentar** un sorteo |
| 2 | 2×03, 00:13:13 | «Una condición» | quieta, un dedo | **explicar** |
| 3 | 2×03, 00:15:04 | «ダメだ 私はお前に強要する» | se acerca | **regañar** |
| 4 | 2×03, 00:17:27 | «Se los di todos a Saotome» | manos vacías | ceder |
| 5 | 2×03, 00:18:05 | «私は… 私は…» | encogida, tímida | **pensar** |
| 6 | 2×05, 00:15:33 | «Prometimos pelear juntas» | frente a Mary | **animar** |

### Runa (anunciadora)

| # | Escena | Qué pasa | Sirve para |
|---|---|---|---|
| 1 | 2×02, 00:04:32 | Megafonía: «みんな こんにちは〜!» | **anunciar un sorteo** |
| 2 | 1×03, 00:17:31 | «ニャッハハ 百合子ちゃん 真っ青だけど大丈夫?» | burla |
| 3 | 1×03, 00:22:12 | «おっはよ〜» | **saludar** |

---

## 16 · Vestuario ⚠️

| Quién | Ropa icónica | Detalle |
|---|---|---|
| Todos | **Uniforme de Hyakkaou**: chaqueta **roja** `#C9020F` con ribete negro, camisa blanca, corbata negra cruzada, falda a cuadros negro y gris, medias negras, mocasines marrones | [Fandom](https://kakegurui.fandom.com/wiki/Yumeko_Jabami), [color-hex](https://www.color-hex.com/color-palette/103520) |
| Yumeko | el uniforme tal cual; **pelo negro con flequillo recto** | lo que todos reconocen |
| Yumeko, mascota | **placa al cuello** de «Mike» (1×03 y 1×04) | 1×03, 00:20:44 |
| Mary | uniforme y **coletas rubias con lazos negros** | [Fandom](https://kakegurui.fandom.com/wiki/Mary_Saotome) |
| Kirari | uniforme; pelo gris claro, **labios azules** | [Fandom](https://kakegurui.fandom.com/wiki/Kirari_Momobami) |
| Ririka | **máscara gris** de ojos almendrados y sonrisa curva | [Fandom](https://kakegurui.fandom.com/wiki/Ririka_Momobami) |
| Midari | parche médico, vendas | [Fandom](https://kakegurui.fandom.com/wiki/Midari_Ikishima) |
| Runa | sudadera naranja de conejo | una sola fuente |

La ropa es **la misma en las dos temporadas y en Twin** ⚠️ (de memoria).
Cosplay de referencia del uniforme:
[Imaginations Costume](https://www.imaginationscostumes.com/anime-kakegurui-yumeko-jabami-cosplay-uniform/).

---

## 17 · Paisajes y fondos de pantalla

### Los sitios, con su luz ⚠️

| Sitio | Hora y luz (de memoria, comprobar) |
|---|---|
| Aula de 2.º Flor | tarde, luz cálida de ventana; pupitres juntados como mesa |
| Sala del consejo | interior, **acuario** de fondo, luz fría azul verdosa |
| Pasillos y escalera central | interior de mármol y madera, luz blanca |
| Club de Cultura Tradicional | tatami y madera, luz suave |

### Fondos de pantalla

| Fondo | Tamaño | Autor |
|---|---|---|
| [Kirari Momobami 4K](https://wall.alphacoders.com/big.php?i=1134912) | «4K Ultra HD» según el título; medida exacta sin ver | Alpha Coders (subido por un usuario) |
| [Yumeko minimalista 4K](https://wall.alphacoders.com/big.php?i=854420) | «4K Ultra HD» según el título | Alpha Coders |
| [Colección 4K](https://wall.alphacoders.com/by_sub_category.php?id=269743&name=Kakegurui+Wallpapers&filter=4K+Ultra+HD) | 3840×2160 o más, según el sitio | varios |
| [160+ fondos](https://alphacoders.com/kakegurui-wallpapers) | varios | varios |
| [WallpaperAccess](https://wallpaperaccess.com/kakegurui) | incluye 3840×2160 según el sitio | varios |
| [Wallpaper Cave](https://wallpapercave.com/kakegurui-wallpapers) | varios | varios |

Casi todos son capturas o arte oficial sin crédito: **sólo para mirar**.

---

## 18 · Guía para generar con IA (Firefly, Canva)

> Úsala sólo para **fondos, objetos o bocetos de pose**. El personaje final
> se calca de un fotograma real (§15), nunca de la IA.

**Rasgos que nunca cambian**
- Yumeko: pelo **negro, largo, liso, flequillo recto**; ojos **rojos**
  cuando juega; chaqueta **roja** con ribete negro; corbata negra cruzada.
- Mary: **coletas rubias con lazos negros**, ojos amarillos, mismo uniforme.
- Kirari: **pelo gris muy claro**, ojos azules, **labios azules**.
- Ririka: **máscara gris** con ojos almendrados y sonrisa curva.

**Paleta**: rojo `#C9020F`, negros `#292329` y `#1E181C`, blanco
`#F7F6FD`. Acentos: dorado de ficha, verde de tapete.

**Línea y sombra** ⚠️: anime de MAPPA de 2017; línea fina y limpia, sombras
en bloque, **sombras duras en la cara** cuando la escena se pone tensa;
brillos húmedos en ojos y labios.

**Luz**: una fuente cálida lateral y un **contraluz rojo** o **azul de
acuario**. Fondo que se oscurece detrás del personaje.

**Encuadre**: plano medio, mesa en primer plano, cámara un poco baja.

**Palabras que ayudan** (en inglés): «anime key visual, MAPPA style,
elite private academy, red school blazer with black trim, casino chips and
playing cards on a green felt table, dramatic rim light, glowing red eyes,
cel shading, high contrast».

**Palabras que lo estropean**: «chibi», «kawaii», «pastel», «3D render»,
«photorealistic», «Las Vegas neon», «revealing», «sexy». Evita cualquier
pose sugerente: el meme viral de 2026 lo es.

**Referencias de estilo**: el key visual de ×× ([LisAni!](https://www.lisani.jp/0000117737/)),
las hojas de personaje de ×× ([PASH! PLUS](https://www.pashplus.jp/anime/117240/)).
**Referencias de pose**: los minutos de §15.

---

## 19 · Tres conceptos para la lámina de #comandos-y-sorteos

Los tres usan los textos de §0. Donde pongo una frase «en la voz de la
serie» es **traducción mía**, no del doblaje latino (no la encontré).
Recortes siempre por `v3/integrar.py` y comprobados a 1:1.

### Concepto A — «La caja de Mary» (el objeto del plan, mejorado)

- **Objeto y sitio**: la mesa del **voto a piedra, papel o tijera** del
  ep. 1 (1×01, 00:06:31 a 00:07:39). Encima: **la caja de las cartas**,
  **tres cartas boca arriba** y **pilas de fichas** sobre tapete verde.
  El aula de 2.º Flor detrás ⚠️ (comprueba en el fotograma si juegan en el
  aula). En Blender: caja de madera lacada roja con ranura, cartas con
  curvatura leve, fichas ([Casino Poker Chip, CC BY](https://sketchfab.com/3d-models/casino-poker-chip-b9efab875b9c4ac3a29ea5a0c7a260d1)),
  tapete ([TextureCan 527](https://www.texturecan.com/details/527/)).
- **Personaje**: **Mary**, la más querida. Pose 1×01, 00:07:31 («These are
  the chips»): una mano sobre las fichas. Alternativa: 00:06:31, explicando
  con un dedo arriba.
- **Cómo habla**: su frase va **en una carta** que sostiene entre dos
  dedos, en Bodoni Moda. Su nombre, **en una ficha dorada** al lado.
  Frase propuesta: **«Aquí se juega con los bots»**.
- **Dónde va cada texto**:
  - Tapa de la caja, en dorado y en relieve: **Comandos y sorteos**
    (Playfair Display Black).
  - Precinto de papel alrededor de la caja: **Aquí se usan los bots**.
  - Etiqueta en el frente de la caja: **Así no ensuciamos el resto**.
  - Las tres cartas: **Juegos**, **Sorteos**, **Economía**. En la esquina
    de cada una, como el índice de una baraja, **el comando real**.
- **Para que no quede plano**: fichas **desenfocadas en primer plano**;
  la caja proyecta sombra sobre las cartas; luz cálida de ventana por un
  lado y **contraluz rojo** por el otro; una carta a medio caer del borde.
- **Lámina 2**: la baraja entera **abierta en abanico** sobre el tapete:
  una carta por comando, un palo por bloque.

### Concepto B — «Lo emite el consejo» (Kirari y el acuario)

- **Objeto y sitio**: el escritorio de la presidenta en la **sala del
  consejo**, con el **acuario** detrás ⚠️ (una sola fuente). Encima: un
  **estuche de fichas** abierto, con las fichas «100万» del consejo
  (1×02, 00:08:06), y **un papel oficial con sello rojo**, como el «plan de
  vida» (1×04, 00:00:48). En Blender: estuche con ranuras, papel con
  pliegue, sello, taza de té.
- **Personaje**: **Kirari**, sentada con el té (1×06, 00:13:43) o empujando
  las fichas en su «オールイン» (2×05, 00:07:01). Sayaka de pie detrás,
  pequeña y desenfocada.
- **Cómo habla**: casi no habla. Su voz es **el papel del consejo**, en
  Cormorant Garamond, con sello. Una línea suya, en una tarjeta junto a la
  taza: **«Bien. Empecemos.»** (de «さて 始めましょうか», 1×10, 00:00:19).
- **Dónde va cada texto**:
  - Título del papel: **Comandos y sorteos**.
  - Primera línea: **Aquí se usan los bots**.
  - Segunda línea: **Así no ensuciamos el resto**.
  - Tres fichas grandes en el estuche, cada una con su palabra grabada:
    **Juegos**, **Sorteos**, **Economía**. El comando, en una etiqueta
    bajo cada ficha.
- **Para que no quede plano**: **luz azul del acuario** que se mueve sobre
  Kirari y el papel (cáusticas), **lámpara cálida** de escritorio, taza en
  primer plano desenfocada, reflejo en el cristal.
- **Lámina 2**: **Ririka con máscara** y los **cien votos** (2×03,
  00:07:31) para explicar los sorteos. O **Runa por megafonía** (2×02,
  00:04:32) anunciando al ganador.

### Concepto C — «El tablón del ranking» (Yumeko)

- **Objeto y sitio**: el **tablón de avisos** del pasillo (2×02, 00:04:40)
  con el **ranking de donaciones** (1×02, 00:03:46). Hojas clavadas con
  chinchetas y una **placa de «MININA 0001»** colgada de un cordel
  (1×03, 00:20:44). En Blender: tablón con marco, hojas que se curvan,
  chinchetas, placa con cordel. El aspecto del tablón en la serie es ⚠️.
- **Personaje**: **Yumeko**, con la mano apoyada en una hoja del tablón (la
  mano toca algo visible) y los **ojos rojos** de 1×01, 00:12:37. Para un
  tono más amable: 1×03, 00:21:20, con la placa de gata.
- **Cómo habla**: su frase va en **una tarjeta clavada** al tablón, en
  Bodoni Moda: **«¡Qué divertido! Quiero jugar»** (de «楽しそう! ぜひ
  やってみたいです», 1×01, 00:07:11). Nombre en una ficha roja.
- **Dónde va cada texto**:
  - Cabecera del tablón: **Comandos y sorteos**.
  - Aviso grande: **Aquí se usan los bots**.
  - Aviso pequeño: **Así no ensuciamos el resto**.
  - Hoja de ranking: **Economía**, con su comando.
  - Hoja con cupones para arrancar: **Sorteos**, con su comando.
  - Hoja con una carta pegada: **Juegos**, con su comando.
  - La placa «MININA 0001»: sólo decoración, **nunca contra el usuario**.
- **Para que no quede plano**: hojas curvadas con sombra, brillo en las
  chinchetas, luz de ventana en diagonal, pasillo desenfocado detrás.
- **Variante**: el **tablero de dados** de «Kakegurui ALL IN» (§13), si con
  red se consiguen capturas.

### ¿Cuál primero?

**A.** Es el objeto del plan, sale del **primer capítulo**, la protagonista
es **Mary** (la más querida) y la caja de cartas **ya es un sorteo**. B es
la más bonita de luz. C es la mejor para una **lámina 2 de economía**.

---

## 20 · Lo que no pude verificar

- **La lista real de comandos** del canal: no está en el inventario.
- **Ninguna imagen**: no hay hojas de contacto. Todo lo visual va ⚠️.
- **Voces latinas** de Kirari, Ririka, Midari, Sayaka y Runa; el director
  del doblaje; la frase latina de «賭け狂いましょう».
- **El orden 2.º a 5.º** del concurso oficial de popularidad.
- **Los colores** de cada personaje: sólo tengo la paleta del uniforme.
- **La letra del logo**.
- **El aspecto** del tablón, de la placa de mascota, de los rótulos de
  título y de las interfaces de los dos juegos.
- **El opening y el ending de ××**: un solo resumen.
- **El acuario** de la sala del consejo: una sola fuente.
- **Los minutos de los vídeos** de YouTube y TikTok.

---

## 21 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)

- `curl https://community.fandom.com` → **000 / 403**. Sin red completa.
- WebFetch bloqueado: doblaje.fandom.com (API), kakegurui-anime.com,
  magazine.jp.square-enix.com, tumblr.com, tvtropes.org, natalie.mu,
  g123.jp.
- curl bloqueado: arctic-shift.photon-reddit.com, web.archive.org,
  fonts.google.com.
- WebSearch rechaza el dominio reddit.com.
- GitHub responde: `raw.githubusercontent.com` y la búsqueda de código.
- Por eso **no hay `hojas/`**.

### Búsquedas web (47 hechas, 1 rechazada)

| # | Idioma | Búsqueda (dominio si lo hubo) |
|---|---|---|
| 1 | ES | Kakegurui doblaje latino reparto Sysdub (doblaje.fandom.com) |
| 2 | ES | Kakegurui doblaje latino Yumeko Jocelyn Robles Kirari Mary Saotome voz |
| 3 | ES | doblaje latino Netflix actores Kirari Ririka Midari (anmtvla, doblaje, voice-over, dubdb) |
| 4 | ES | «Kakegurui ya disponible en Netflix y detalles de su doblaje» reparto dirección |
| 5 | ES | «Jocelyn Robles» «Valentina Souza» «Ricardo Bautista» Kirari Midari Sayaka |
| 6 | JA | 賭ケグルイ アニメ 公式 キービジュアル 解禁 夢子 綺羅莉 |
| 7 | JA | 賭ケグルイ チーティングアロード アプリ ゲーム 画面 ガチャ UI |
| 8 | JA | 賭ケグルイ 人気投票 結果 1位 キャラクター |
| 9 | EN | Kakegurui official character popularity poll results Gangan Joker |
| 10 | JA | 賭ケグルイ 公式 人気投票 早乙女芽亜里 1位 ガンガンJOKER 桃喰綺羅莉 2位 |
| 11 | JA | «賭ケグルイ頂上戦» 結果発表 順位 |
| 12 | JA | 賭ケグルイ ALL IN ゲーム 配信 リリース 画面 |
| 13 | EN | Kakegurui ALL IN G123 game review dice board cards Yumeko |
| 14 | JA | 賭ケグルイ 林祐一郎 監督 インタビュー 顔芸 作画 MAPPA |
| 15 | EN | Kakegurui opening ending songs Deal with the devil Tia LAYon-theLINE TECHNOBOYS |
| 16 | JA | 賭ケグルイ キャラクターデザイン 秋田学 美術監督 色彩設計 スタッフ |
| 17 | JA | 尚村透 賭ケグルイ 画集 表紙 イラスト カラー 描き下ろし |
| 18 | EN | Kakegurui manga volume covers Yen Press character cover list |
| 19 | EN | Yumeko Jabami personality red glowing eyes character analysis |
| 20 | EN | Kirari blue lipstick; Ririka mask twin; Midari eyepatch gun; Sayaka |
| 21 | EN | Mary Saotome blonde twintails Kakegurui Twin Netflix 2022 key visual |
| 22 | EN | Hyakkaou student council room design background art uniform |
| 23 | EN | poker table casino chips cards free CC Attribution (sketchfab.com) |
| 24 | EN | Kakegurui Yumeko 3D model (sketchfab, deviantart, artstation) |
| 25 | JA | 賭ケグルイ 夢子 イラスト 人気 ファンアート (pixiv.net) |
| 26 | ZH | 狂赌之渊 蛇喰梦子 名场面 颜艺 桃喰绮罗莉 人气 哔哩哔哩 |
| 27 | KO | 카케구루이 유메코 명대사 도박에 미치자 인기 캐릭터 메아리 |
| 28 | EN | Kakegurui logo font typeface similar free font |
| 29 | EN | Yumeko Jabami color palette hex codes uniform red black |
| 30 | ES | Kakegurui trailer oficial Netflix español latino (youtube.com) |
| 31 | ES | Yumeko latino frase doblaje «apostemos» «como locas» «hasta enloquecer» |
| 32 | EN | Kakegurui meme Know Your Meme Yumeko face |
| — | EN | fans y crítica del live action (reddit.com): **rechazada** por el buscador |
| 33 | EN | fans favorite Mary; Bet live action criticism (cbr, myanimelist, screenrant, ann, gamerant) |
| 34 | EN | Kakegurui wallpaper 4K 3840x2160 (wallhaven, wallpaperaccess, wallpapercave, alphacoders) |
| 35 | EN | CC0 green felt, red velvet, dark walnut (polyhaven, ambientcg, texturecan) |
| 36 | JA | 賭ケグルイ トランプ 公式グッズ カード 生徒会 チップ |
| 37 | ES | Kakegurui análisis Yumeko psicología (youtube.com) |
| 38 | ES | Kirari doblaje latino actriz; Twin Mary voz latina (doblaje, anmtvla) |
| 39 | ES | «Kakegurui» Sysdub director de doblaje voces Kirari Midari Sayaka Runa |
| 40 | JA | 賭ケグルイ アイキャッチ サブタイトル 演出 赤 目 光る |
| 41 | EN | Kakegurui characters favorites (myanimelist.net): **0 resultados** |
| 42 | EN | Kakegurui trend Yumeko edit Deal with the devil 2026 (tiktok.com) |
| 43 | JA | 賭ケグルイ Blu-ray ジャケット 秋田学 描き下ろし 第1巻 |
| 44 | EN | student council ranking, house pet tag (kakegurui.fandom, tvtropes, ann, cbr) |
| 45 | EN | Kakegurui fan art Kirari Mary illustration (artstation, deviantart) |
| 46 | ES | «Kakegurui» Yumeko «¡Apostemos» «apostemos como» «a apostar como locos» |
| 47 | EN | Toru Naomura art style faces eyes lettering speech bubbles |

### GitHub (sin cupo)

- Búsqueda de repositorios «kakegurui»: juegos de fans (§13).
- Búsqueda de código: subtítulos en
  [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror).
  Bajé **33 archivos**: T1 ep. 1 a 12 (DragsterPS, japonés e inglés; el 7
  sólo en japonés, de Erai-raws) y ×× ep. 1 a 12 (Netflix, japonés).
  Los dejé en mi carpeta temporal, **no en el repositorio**.
- [google/fonts](https://github.com/google/fonts): METADATA y TTF de ocho
  letras, comprobadas con fontTools.

### Fuentes consultadas por tipo

- **Oficiales**: web del anime (T1, ××, BD), Gangan Joker y su X, pixiv
  Comic, Avex, 4Gamer y Famitsu (juegos), G123, LisAni!, PASH! PLUS,
  Animate Times, Natalie (entrevista), Syoboi.
- **Otros idiomas**: japonés (arriba), chino (Bilibili, Baidu, Zhihu),
  coreano (Namuwiki).
- **Wikis**: Fandom (Kakegurui, Doblaje, Villains, Heroes, Shipping,
  J-pop, Voice over), TV Tropes, Wikipedia.
- **Foros y comunidades**: Tumblr (análisis del voto), la página de Facebook «Kakegurui»,
  みんなのランキング, ランこれ. Reddit: no accesible.
- **Arte**: pixiv, ArtStation, DeviantArt.
- **Vídeo**: YouTube, TikTok, Bilibili.
- **Código y recursos**: GitHub, Sketchfab, TextureCan, ambientCG, Poly
  Haven, color-hex.
- **Doblaje latino**: Doblaje Wiki (sólo extractos), ANMTV, Voice over
  Wiki, YouTube, TikTok.

### Lo que NO encontré

- La lista de comandos del canal (no está en el inventario).
- Imágenes: no se pudo bajar nada; sin hojas de contacto.
- Voces latinas de Kirari, Ririka, Midari, Sayaka y Runa; director del doblaje.
- La frase latina de «賭け狂いましょう».
- La letra del logo.
- Capturas de la interfaz de los dos juegos. The Cutting Room Floor: no
  lo busqué. Wayback Machine: bloqueada.
- Un artbook de Naomura.
- Reddit y Arctic Shift: bloqueados.
