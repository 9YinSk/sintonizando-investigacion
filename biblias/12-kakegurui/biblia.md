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

En la primera pasada no se pudo abrir ninguna imagen. En la segunda sí:
**1051 imágenes de la wiki** (7 páginas: Yumeko, Kirari, Mary, Ririka,
Midari, Runa y el consejo) en **11 hojas de contacto** de 48 imágenes,
hechas con `investigar_serie.py` el 25-sep-2026 ✅. Las 3 mejores están en
`hojas/`.

### 3.0 Las hojas de contacto (en `hojas/`)

Cada imagen lleva su número, su tamaño real y su nombre en la wiki. Las
miré las tres. El original se baja de
`https://kakegurui.fandom.com/wiki/Special:FilePath/<nombre>` o con la API
de la wiki (las de `static.wikia.nocookie.net` piden la cabecera
`Referer: https://www.fandom.com/`).

**`personajes_01.jpg`** (imágenes 1-48: portadas, key visuals y grupo)

| N.º | Qué es | Tamaño | Sirve para |
|---|---|---|---|
| 1 | «XX Rei + Kirari»: portada de ×× con Kirari en uniforme de pantalón | 2828×3994 | Kirari formal, de pie, pose de mando |
| 4 | «XX Mary + Yumeko»: las dos de pie, portada de ×× | 2115×2998 | pareja, cuerpo entero |
| 5 | «Mary Manga»: Mary sobre verde tapete | 2048×2916 | Mary sola, color del tapete |
| 8 | «Ace Cards»: cuatro ases sobre paño verde | 2494×2065 | **cartas de la mesa** |
| 15 | «12 Gamers Bromide»: postal oficial | 1689×2498 | grupo |
| 21 | «17 Inside Cover»: Yumeko y Mary juntas | 1530×2160 | pareja con amigos |
| 25-26 | Kirari con el **uniforme de verano** | 1521×2160 | vestuario |
| 30 | «Twin 13 Inside Cover»: Mary con cartas volando | 1513×2160 | **Mary en acción** |
| 33 | «Volume 10 Kari»: todo el reparto en Kakkokari | 1513×2149 | grupo, humor |
| 43 | «16 Inside Cover»: Yumeko con la **cara de locura** | 1495×2160 | kaogei |
| 46 | «Gambling-School Visual»: key visual de grupo, rojo y negro | 1499×2048 | **grupo alrededor de la mesa** |
| 47 | «Chapter 107 large cover»: Yumeko a la carrera, horizontal | 2048×1468 | acción, formato ancho |
| 48 | «Volume 11 cover»: Kirari con la mano en la cara | 1452×2062 | Kirari de cerca |

**`personajes_02.jpg`** (imágenes 49-96: ilustraciones «Kakegurui Love»,
manga en blanco y negro, fotos de imagen real)

| N.º | Qué es | Tamaño | Sirve para |
|---|---|---|---|
| 55 | «Kakegurui Love»: Yumeko y Mary, fondo rojo con damero | 1350×1920 | paleta medida (§16) |
| 56-60 | «Kakegurui Love»: Yumeko sola en 5 poses (la 58, con cartas de tarot) | 1350×1920 | poses de Yumeko |
| 61 | «Yumeko Kirari Love» | 1350×1920 | paleta medida (§16) |
| 63-70, 73-76, 90-91 | páginas y portadas del manga en blanco y negro | 1284-1337 de ancho | línea y trama (§B) |
| 80 | «Twin Chapter 13 cover»: Mary con cartas y copa | 1800×1291 | Mary ganadora |
| 83 | «Twin Chapter 39 cover»: cartas volando | 1800×1291 | acción |
| 88 | «A Girl Named Mary Saotome», portada: Mary señala con cartas | 1800×1280 | **Mary explicando** |
| 94 | Kirari y Sayaka, «Pocky Game» | 1337×1584 | dinámica |
| 95 | «MaryGamble»: Mary con los ojos amarillos encendidos | 1299×1600 | cara de Mary jugando |
| 96 | Ririka haciéndose pasar por Kirari (drama) | 1920×1080 | imagen real |

**`vestuario_03.jpg`** (imágenes 145-192: portadas de capítulo, perfumes,
imagen real)

| N.º | Qué es | Tamaño | Sirve para |
|---|---|---|---|
| 163 | «Mary royal flush»: Mary con cartas en abanico | 1263×1395 | **Mary con su objeto** |
| 166-167 | perfumes oficiales de Yumeko y Mary | 1149×1500 | uniforme en producto (§F) |
| 176 | Kirari intenta quitarle la máscara a Ririka | 1027×1541 | **máscara blanca** |
| 178 | tomo 1: Yumeko con los ojos rojos | 1049×1498 | cara icónica |
| 181-182 | imagen real (serie y película) | 1033-1480 de ancho | vestuario real |
| 186 | «Kakegurui Ai Love»: el fanbook con la encuesta | 1000×1422 | fuente de §9 |
| 191 | Mary abraza a Tsuzura | 1080×1299 | el pasador de Tsuzura (§C) |

Las otras 8 hojas quedaron fuera del repositorio (fotogramas del anime y
más portadas de capítulo).

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

- ~~No vi ninguna imagen~~: resuelto con las hojas (§3.0). Portadas vistas
  en las hojas: tomos 1, 10, 11, 12, 14, 15, 16, 18 y 20; *Twin* 6, 8, 9,
  12, 13 y 14; *Kakkokari* 3 a 6; capítulos sueltos del 71 al 121 ✅.
- No encontré un **artbook** de Naomura. Sí hay fanbook oficial,
  «賭ケグルイ愛(ラブ)» (hoja 3, n.º 186), que trae los resultados del
  concurso de popularidad ⚠️.
- El Blu-ray de Akita y la caja de Naomura siguen con **una fuente** (la
  web oficial) ⚠️.

### 3.6 Arte oficial nuevo (segunda pasada)

- **Pachislot «パチスロ 蛇喰夢子という女»** (Net, instalada el 3-jul-2023) y
  **pachinko «eカケグルイ»** (D-light / Daiichi Shōkai, 11-may-2026) ✅
  (dos fuentes cada una: [p-town, 4374](https://p-town.dmm.com/machines/4374)
  y [P-WORLD](https://www.p-world.co.jp/machine/database/9844);
  [p-town, 5004](https://p-town.dmm.com/machines/5004) y
  [pachinkovillage](https://www.pachinkovillage.com/pachinko/p.php?M=7445)).
  Vistas las dos imágenes del mueble (360×550): la pachislot, roja y negra,
  lleva a Yumeko con los **ojos rojos** mirando fijo, un «**さぁ**» rojo
  enorme y a Yumeko y Kirari cara a cara; la pachinko, azul claro, un
  primer plano de Yumeko **mordiéndose la uña** con rubor y salpicaduras
  de tinta. Por ley, la máquina no puede llevar el kanji «賭»: por eso se
  llama «eカケグルイ» ⚠️ (una fuente, ja.wikipedia).
- **Portada y banner de AniList**: [portada](https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/b98314-TSJykxVwCCQN.jpg)
  (230×320) y [banner](https://s4.anilist.co/file/anilistcdn/media/anime/banner/98314-gwgiHiJOj2ls.jpg)
  (1900×400), medidos con `estilo.py` (§16).
- **Kirari en color para Gangan Joker de septiembre de 2019** (891×1280,
  wiki) ⚠️ una fuente.
- **Fondo de pantalla oficial de ALL IN**: se regaló por X al lanzar el
  juego ⚠️; no se encontró el archivo, sólo el anuncio
  ([g123.jp](https://g123.jp/news/article/443078?lang=ja)).
- **Imagen real**: serie de TV (Elaiza Ikeda como Kirari) y dos
  películas, con fotos de elenco en las hojas (n.º 2-3, 53, 181-182) ⚠️.
  Sirven para ver el uniforme en tela de verdad.


---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D de objetos para la mesa (Sketchfab)

Licencias **leídas en la API de Sketchfab** (`api.sketchfab.com/v3/models/<uid>`,
25-sep-2026), una por una ✅. Copia el crédito tal cual.

| Modelo | Autor | Licencia | Para qué |
|---|---|---|---|
| [Low Poly Poker Chips & Cards](https://sketchfab.com/3d-models/low-poly-poker-chips-cards-8420090cc79a49d9a0b85f53c5074616) | Designed By Jonathan (@designedbyjonathan) | **CC BY 4.0** ✅ (API) | fichas y cartas de relleno |
| [Casino Poker Chip](https://sketchfab.com/3d-models/casino-poker-chip-b9efab875b9c4ac3a29ea5a0c7a260d1) | lejonlin | **CC BY 4.0** ✅ (API) | la ficha del consejo, en primer plano |
| [Casino Poker Table](https://sketchfab.com/3d-models/casino-poker-table-f36fc75d825148618aa6e5cbfb43f28e) | Nathan Powell (@npowell) | **CC BY 4.0** ✅ (API) | la mesa |
| [Stylized Poker Table](https://sketchfab.com/3d-models/stylized-poker-table-game-asset-48fd86c57c2b497a900223d8f115f188) | Morgan.J (@MorganJ45) | **CC BY 4.0** ✅ (API) | mesa, fichas, cartas y sillas |
| [Poker Table](https://sketchfab.com/3d-models/poker-table-a48473a5ae7c437496a7aa388f8c458b) | Pieter Ferreira (@Badboy17Aiden) | **CC BY 4.0** ✅ (API) | baraja entera y fichas, texturas 2048 |
| [Poker Chip Set](https://sketchfab.com/3d-models/poker-chip-set-b0cbee32720046e7b1e480cff44a5d41) | matveuk (@anna_bezzu) | **CC BY-NC-ND 4.0** ✅ (API): sólo mirar, no modificar ni repartir | forma de las fichas |
| [Poker Chip 500$](https://sketchfab.com/3d-models/poker-chip-500-3cd4d3b00c0349ad978d0c81d8f95409) | matveuk (@anna_bezzu) | **CC BY-NC-ND 4.0** ✅ (API): sólo mirar | forma de la ficha de valor alto |

Crédito tipo (CC BY): «"Casino Poker Chip" by lejonlin, CC BY 4.0, sketchfab.com».
Los dos de matveuk **no** valen para un `.blend` retocado que se comparta.

### 4.2 Modelos 3D de personajes (sólo para mirar poses)

- [Yumeko](https://sketchfab.com/3d-models/yumeko-9834761e49a346cba73c8e1d9ab40122) de Yaanaa: **CC BY 4.0** según la API ✅ (el personaje sigue con copyright).
- [Mary Saotome](https://sketchfab.com/3d-models/mary-saotome-62bf9b36b5b64c29b27c8eadea263417) de Acutee: **sin licencia libre** (la API no da ninguna): sólo mirar en la página ✅.
- [Runa Yomozuki con rig](https://sketchfab.com/3d-models/runa-yomozuki-kakegurui-70dafed89bcd4dd3b9f5654f90ebeef3) de Gustav_Johansson00: **CC BY-NC**, 40 434 caras, `.blend` y FBX ✅.
- [Runa en alta densidad](https://sketchfab.com/3d-models/kakegurui-runa-b015aaa7272c4191a543722ead37a316) de claener: **CC BY**, 2 459 421 caras, sin rig ✅.
- No hay Yumeko, Mary ni Kirari **descargables** con licencia libre (búsqueda en la API con `downloadable=true`) ⚠️.
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

### 4.4 Fotos de cosplay con licencia libre (segunda pasada)

De [Openverse](https://openverse.org) (Flickr), **CC BY-NC-SA 2.0**,
tamaño medido ✅. Sirven para ver el uniforme en tela, con volumen y luz
reales:

| Foto | Autor | Tamaño |
|---|---|---|
| [Mary Saotome](https://live.staticflickr.com/65535/51993321805_fcbae7f80b_b.jpg) | timz2011 | 819×1024 |
| [Yumeko Jabami](https://live.staticflickr.com/65535/52168451785_7d7fd1969e_b.jpg) | timz2011 | 819×1024 |
| [Yumeko Jabami](https://live.staticflickr.com/65535/49593369942_3398840cc9_b.jpg) | timz2011 | 683×1024 |
| [Runa Yomozuki](https://live.staticflickr.com/65535/49548910152_8ce02899eb_b.jpg) | timz2011 | 683×1024 |
| [Cosplay de grupo](https://live.staticflickr.com/4678/39488187244_5a06f27b0c_b.jpg) | Poooyjie | 683×1024 |

Patrón de costura del uniforme: [Imaginations Costume](https://www.imaginationscostumes.com/anime-kakegurui-yumeko-jabami-cosplay-uniform/).

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

| Sitio | Qué sé | Fuente |
|---|---|---|
| **Academia Privada Hyakkaou** (私立百花王学園) | **122 años**, «tradition and prestige» (伝統と格式) | ✅ subtítulo 1×01, 00:00:06 |
| Sus lazos | «heavy connections in the financial and political worlds» (政財界) | ✅ subtítulo 1×04, 00:03:49 |
| Alumnos | **3.000** | ✅ subtítulo 1×02, 00:03:51 |
| El edificio por dentro | Antes de Kirari era **un colegio japonés tradicional**; ahora es **moderno y de estilo occidental** | ⚠️ [Fandom](https://kakegurui.fandom.com/wiki/Hyakkaou_Private_Academy) |
| **Sala del consejo estudiantil** | Kirari adora los peces tropicales: hay **un acuario enorme**, empotrado en la pared, con luz turquesa que se mueve; Kirari lo señala con la mano | ✅ [Fandom: Student Council](https://kakegurui.fandom.com/wiki/Student_Council) y visto en el ep. 2, 21:22-21:40 |
| Pasillo del consejo | Luz lavanda de noche, columnas claras, un retrato en la pared | visto, ep. 2, 5:00 |
| Vestíbulo y escalera | Araña de luces dorada, suelos y barandas de madera oscura | visto, ep. 2, 20:55-20:58 |
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

### 5.2 Luz

**Segunda pasada: medida en fotogramas** con `estilo.py` (episodios 1 y 2,
[Internet Archive](https://archive.org/details/kakegurui-latino), 854×480) ✅.
Casi todas las apuestas tienen **un solo foco cálido sobre fondo oscuro**;
el color entra sólo en detalles: los ojos, la sangre, el acuario.

| Sitio | Qué se ve | Minuto | Hex medidos |
|---|---|---|---|
| **Sala del consejo** | acuario turquesa detrás de Kirari | ep. 2, 21:30 | `#30B5B9` `#76FBF8` |
| Pasillo del consejo | luz lavanda de noche | ep. 2, 5:00 | `#9495D1` (luz), `#550C1B` (uniforme en sombra) |
| Aula del prólogo | ventana fría, contraluz azulado, caras cálidas | ep. 1, 0:15 | `#D0C1B6` `#91776F` `#43322D` |
| Mesa de piedra, papel o tijera | focos sobre la mesa, el aula a oscuras | ep. 1, 6:29 | `#11091F` (38 %) |
| Yumeko con los ojos rojos | casi negro con un foco cálido en la cara | ep. 1, 12:39 | `#1D171C` (53 %), `#C23345`, `#EFDADC` |
| Vestíbulo | araña dorada, madera oscura | ep. 2, 20:55 | sin medir |

- Corrección: la primera pasada decía «luz azul verdosa, de memoria».
  Es **turquesa**, medida. Ojo: el investigador de imagen midió otro
  fotograma de la sala (ep. 6, en la wiki, 1280×720) y le salió
  **verde oliva** (`#D5DE3E` `#B0B62D` `#65641F`). Es otra escena: el
  matiz cambia según el plano ⚠️. Para la lámina, el turquesa del ep. 2.
- Cuando alguien «se vuelve loco», el fondo se apaga a casi negro con un
  solo foco en la cara y **ojos rojos saturados** (visto, ep. 1, 12:39).
- Director Hayashi: quería jugar con «evening light, and moonlight, and
  different kinds of light» y la T1 «dark, gritty… realistic» ✅ (§A).

### 5.3 Paleta

**Segunda pasada**: el rojo del blazer se midió en 5 ilustraciones
oficiales; la base es **`#D6362A`** (ver §16). La paleta de fan de abajo
sirve sólo de contraste.

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
| Ririka | ~~máscara gris~~ **máscara blanca** (texto de la wiki; hoja 3, n.º 176) | sin medir ⚠️ |

Un fan de Tumblr asigna **un color a cada personaje** (Yumeko = rojo):
[kiraris-fish-tank](https://www.tumblr.com/kiraris-fish-tank/163196515310/kakegurui-color-theory-yumeko-jabamired) ⚠️.

### 5.4 Texturas reales equivalentes

| Material | Enlace | Licencia |
|---|---|---|
| **Tapete de fieltro** (paño de billar) | [TextureCan 527](https://www.texturecan.com/details/527/) | gratis, PBR ⚠️ (la página no cargó en la segunda pasada: sin texto de licencia) |
| Más tapetes y «casino» | [TextureCan: Felt](https://www.texturecan.com/tag/Felt/), [Casino](https://www.texturecan.com/tag/Casino/) | gratis ⚠️ |
| Tela | [ambientCG Fabric 031](https://ambientcg.com/view?id=Fabric031) | **CC0** ✅ (ambientCG es CC0) |
| Madera de mesa gastada | [Poly Haven: wood_table_worn](https://polyhaven.com/a/wood_table_worn) | **CC0** ✅ (API de Poly Haven; foto de Dimitrios Savva, proceso de Rico Cilliers; hasta 8192×8192) |
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

### 6.3 Una letra para cada uso

Sólo con las letras de 6.2 (todas traen tildes, ñ, ¿ y ¡). Es una
propuesta de estilo: la serie no tiene globos propios (§7).

| Uso | Letra | Por qué |
|---|---|---|
| Logo o título | **Playfair Display** Black | serif de alto contraste, colegio de élite |
| Lo que dice el personaje (la «carta», §7.3) | **Bodoni Moda** o **Playfair Display** | como las esquinas de una baraja |
| Grito | **Dela Gothic One**, en rojo y grande | la pachislot pone un «さぁ» rojo enorme sobre la cara de Yumeko (§3.6) |
| Pensamiento | **Cormorant Garamond**, pequeña, sin caja | imita la voz en off de Suzui |
| Onomatopeya | **Dela Gothic One** en katakana (ざわ, ゾク) | peso negro, sin redondeos |
| Cartel del mundo (papel del consejo, tablón) | **Cormorant Garamond**, sello en **Cinzel** | documento oficial |
| Placa de mascota, etiquetas | **Oswald** | estrecha, como una chapa grabada |
| Interfaz de juego | **Oswald** para botones, **Bodoni Moda** para cifras | no hay capturas de las cajas de los juegos ⚠️ (§13) |
| Subtítulos o créditos | **Shippori Mincho B1** para el japonés | los créditos del opening y del ending (ep. 1, 3:02 y 23:25) salen en letra japonesa fina; la letra exacta no está identificada ⚠️ |

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que la serie pone en pantalla

En Kakegurui **no hay un globo propio**: el texto aparece **sobre objetos
del juego y del colegio**. Todo esto está comprobado en los subtítulos:

| Soporte | Dónde se ve | Estado |
|---|---|---|
| **Cartas** escritas a mano y metidas en una caja | 1×01, 00:06:38 a 00:06:48 | ✅ |
| **Fichas** con su valor, emitidas por el consejo | 1×01, 00:07:31; 1×02, 00:08:06 | ✅ |
| **Placa de mascota** al cuello: «BOTTOM-FEEDER 0001 MITTENS» (así la traduce Netflix en pantalla) | 1×03, 00:20:44 | ✅ el texto |
| **La placa vista** (segunda pasada): chapa colgada de una **cadena**, con «**ミケ**» grabado; Mary la levanta en el puño. En la wiki, dos placas **con forma de pata**, una de gata y otra de perro ([Kakegurui_collar.jpg](https://static.wikia.nocookie.net/kakegurui/images/c/c3/Kakegurui_collar.jpg/revision/latest?cb=20201225202413), 749×807) | ep. 2, 1:00 (visto) | ✅ |
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

Ver §13. De sus cajas de diálogo **no encontré capturas** ⚠️ (tampoco en
la segunda pasada: los juegos son de móvil y de navegador, no están en
Steam). Lo más parecido que sí se vio es el **mueble de la pachislot**:
cara de Yumeko con los ojos rojos y un «さぁ» rojo enorme (§3.6).

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
Segunda pasada: los gestos marcados «visto» salen de los episodios 1 y 2
(§2.0); gustos, alturas y objetos, en §C.

### Yumeko Jabami (蛇喰夢子) — la protagonista, 5.ª en votos (lo confirma Kawamoto, §9)

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
- **Cuerpo** (visto): disfruta con **los ojos cerrados y las manos juntas
  cerca del pecho**, inclinada hacia la rival (ep. 1, 7:29-7:41); antes de
  estallar echa el cuerpo adelante con el brazo en alto (11:55-12:07); al
  estallar, **ojos rojos**, boca muy abierta y **dedos en garra** cerca de la
  cara (12:15-12:43). En el arte oficial se muerde la uña con rubor
  (pachinko, §3.6).
- **Es la única sin monólogo interno** en todo el anime ✅ ([Fandom, Trivia](https://kakegurui.fandom.com/wiki/Yumeko_Jabami)):
  nunca se oye lo que piensa.

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
- **Aspecto**: **rubia con coletas y lazos negros**, ojos amarillo oscuro ✅
  (Fandom y las etiquetas de Danbooru `twintails`, `yellow_eyes`). Blazer
  con **botones dorados** y falda **gris plisada**, no a cuadros (Fandom).
- **Cuerpo** (visto): explica **de pie, con la palma abierta a la altura
  del hombro** (ep. 1, 6:09-6:41); pierde el control con los ojos muy
  abiertos y lágrimas (12:31); humilla **levantando la placa «ミケ»** en el
  puño, cejas bajas y boca muy abierta (ep. 2, 1:00).
- **Cómo manda**: «ポチ… チップ持ってきて» («Fido, fetch the chips», 1×01, 00:07:18).
- **Cómo explica**: rápido y sin rodeos, con reglas y cifras: «The rate is
  10,000 yen per chip. For starters, here are 120 of them» (1×01, 00:07:33).
- **Cómo se burla**: «あ〜ら あら 蛇喰さん チップなくなっちゃったね» (1×01, 00:11:19).
- **Cómo se enfada**: «ボンボンのバカ娘が ナメやがって» (1×01, 00:13:19),
  «ウッゼ〜» (1×04, 00:12:34), «私はこいつに呪われてんのか!» (1×04, 00:13:33).
- **Cómo celebra**: «この勝負 勝てる!» (¡Esta la gano!) (2×04, 00:00:01).

### Kirari Momobami (桃喰綺羅莉) — la presidenta, 2.ª en votos ⚠️ (Mary la superó, dice Kawamoto)

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
- **Visto** (primer capítulo suyo, 1×02): de pie sola en el pasillo, **mano
  derecha relajada a la cintura**, mirada tranquila a cámara, dos coletas
  trenzadas y **labios azul pálido** (ep. 2, 5:00); de perfil con sonrisa
  entreabierta (21:16-21:19); **mano en la barbilla** junto al acuario
  (21:31-21:34); a la cabecera de la mesa del consejo (21:37).
- Su peinado se inspira en **donas y cuentas de oración budistas** ⚠️
  (podcast de Kawamoto, §C).

### Ririka Momobami (桃喰リリカ) — la vicepresidenta, 4.ª en votos ⚠️

- **Quién es**: gemela de Kirari y vicepresidenta. Sale con **una máscara
  blanca de teatro** (corregido: antes decía gris; la wiki dice «white»,
  y se ve en la hoja 3, n.º 176) que le cambia la voz: ojos almendrados y
  **sonrisa curva**. Pelo platino suelto, sin pintalabios ✅ ([Fandom](https://kakegurui.fandom.com/wiki/Ririka_Momobami),
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
- **La misma seiyū que Kirari**, Miyuki Sawashiro ✅ (AniList y Fandom); en
  latino, también la misma: Adriana Núñez (§10). Debuta en el ep. 2, pero
  **no se le vio la cara** en vídeo ⚠️.

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

### 8.1 Su cara en cada emoción (segunda pasada)

«Visto» = fotograma mirado en los episodios 1-2 (§2.0). «Sub» = minuto del
subtítulo, con la frase, pero la cara sin mirar ⚠️. Vacío = no encontrado.

| | Alegría | Rabia | Tristeza | Miedo | Vergüenza |
|---|---|---|---|---|---|
| **Yumeko** | ojos cerrados, manos juntas, ep. 1, 7:29 (visto); euforia con ojos rojos, 12:15-12:43 (visto) | fría, «You'll never deceive anyone…», 1×01, 00:15:21 (sub) ⚠️ | no encontrada | no aplica: casi no tiene miedo (Fandom) | no encontrada |
| **Mary** | burla «あ〜ら あら», 1×01, 00:11:19 (sub); tráiler, 0:24 (visto) | la placa «ミケ» en el puño, ep. 2, 1:00 (visto) | «How did this happen, anyway?», en el suelo, 1×01, 00:16:59 (sub) ⚠️ | ojos enormes con lágrimas, ep. 1, 12:31 (visto) | no encontrada |
| **Kirari** | placer tranquilo de perfil, ep. 2, 21:16 (visto) | no encontrada | no encontrada | no encontrada | no encontrada |
| **Ririka** | no encontrada | no encontrada | no encontrada | no encontrada | sin máscara se traba, 2×03, 00:18:05 (sub, sin reverificar) ⚠️ |

**6 de 20** casillas vistas en vídeo; 4 más con el minuto del subtítulo.
Faltan los episodios 3-24 mirados con `fotogramas.py` (en Internet Archive
están los 12 de la T1 y la T2 en latino).

---

## 9 · ¿Quién es el más querido?

**Mary Saotome.** La secundaria gana a la protagonista.

| Encuesta | Resultado | Estado |
|---|---|---|
| **Oficial**: «賭ケグルイ頂上戦», Gangan Joker, 2017 ([página del avance](https://magazine.jp.square-enix.com/joker/series/kakegurui/special/1710vote.html)) | **1.ª Mary**, 2.ª Kirari, 3.ª Sayaka, 4.ª Ririka, 5.ª Yumeko | Mary 1.ª ✅ ([Tumblr que recoge el avance oficial](https://www.tumblr.com/kake-gurui/166641286590/official-kakegurui-character-popularity-poll-mid), [página de Facebook «Kakegurui» con el top 6](https://www.facebook.com/Kakegurui/posts/the-current-top-6-in-the-official-popularity-poll-has-been-posted-on-jokers-offi/1711985735502238/), resumen de la búsqueda en japonés). Del 2.º al 5.º: ahora con **segunda fuente**, el propio Kawamoto (abajo) ✅ |
| Análisis del voto por fans | [admiralyurii](https://www.tumblr.com/admiralyurii/182367489383/kakegurui-meta-popularity-poll-breakdown), [yun-fang-xiii](https://www.tumblr.com/yun-fang-xiii/623080819472384000/kakegurui-meta-popularity-poll-breakdown), [fuyuyuu](https://fuyuyuu.tumblr.com/post/168748945840/pkjd-kakegurui-character-popularity-poll) | no pude abrirlos |
| Votación de fans japoneses, [みんなのランキング](https://ranking.net/rankings/best-kakegurui-characters) | **1.ª Mary** | ✅ |
| Otra de fans, [ランこれ (2.ª votación)](https://rancolle.com/ranking.php?id=uid4_1639143940) | no vi el orden | ⚠️ |
| Prensa en inglés | «Mary, **best girl**» ([CBR](https://www.cbr.com/kakegurui-mary-saotome-best-girl/)); [Looper, top 10](https://www.looper.com/1040021/most-popular-kakegurui-characters-ranked/) | ✅ / ⚠️ |

El concurso oficial tuvo tres categorías: **personaje, pareja y episodio**
favoritos. Los resultados completos están en el fanbook
**«賭ケグルイ愛(ラブ)»** ⚠️.

**Lo confirma el autor (segunda pasada).** En un podcast de radio con su
hermano, traducido tuit a tuit por un fan en X
([@Shishi_Odoshii, 2/21](https://x.com/Shishi_Odoshii/status/2005734414832263348),
[3/21](https://x.com/Shishi_Odoshii/status/2005734417889997114),
[13/14](https://x.com/Shishi_Odoshii/status/2005737123933217025)),
Homura Kawamoto dice ⚠️ (traducción de fan):
- que **Kirari no quedó 1.ª** y que **Yumeko quedó 5.ª** («sin Yumeko la
  historia ni empezaría»; le dio pena);
- que le sorprendió que **Mary superara a Kirari** y que Mary y Ririka
  quedaran tan arriba;
- que cree que **Ririka subiría** si la encuesta se repitiera hoy;
- que su favorita es **Yumeko** y la de su hermano, **Sumika Warakubami**
  ([4/21](https://x.com/Shishi_Odoshii/status/2005734420251304234)).

**Otra votación, AniList** (favoritos de usuarios, [ficha](https://anilist.co/anime/98314)) ✅:
1.ª Yumeko (8732), 2.ª Mary (4278), 3.ª Midari (2324), 4.ª Kirari (2320),
5.ª Ririka (1524), 6.ª Runa (1502). Fuera de Japón gana la protagonista;
en Japón, Mary.

**La favorita de la seiyū de Yumeko**: Saori Hayami eligió a **Midari**
(«pone la misma cara que un cachorro esperando a su dueño»)
⚠️ ([entertainmentstation.jp](https://entertainmentstation.jp/388789/2),
leída a través de la wiki).

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

**Segunda pasada**: la API de Doblaje Wiki ya responde. Cada nombre está
en **dos páginas** de la wiki (la ficha de
[Kakegurui](https://doblaje.fandom.com/es/wiki/Kakegurui) y la del actor)
o en la ficha y en [AniList](https://anilist.co/anime/98314) ✅. AniList
dice «Spanish» y mezcla España y Latinoamérica: sólo cuenta como segunda
fuente cuando el nombre coincide con Doblaje Wiki.

| Personaje | Voz latina | Fuentes | Estado |
|---|---|---|---|
| **Yumeko Jabami** | **Jocelyn Robles** | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Kakegurui) · [Voice over Wiki](https://voice-over-and-voice-acting.fandom.com/wiki/Kakegurui_(2017)) · AniList | ✅ |
| **Mary Saotome** | **Valentina Souza** | [Doblaje Wiki: Valentina Souza](https://doblaje.fandom.com/es/wiki/Valentina_Souza) · Voice over Wiki · AniList | ✅ |
| **Kirari Momobami** | **Adriana Núñez** | ficha de Kakegurui · [ficha de Adriana Núñez](https://doblaje.fandom.com/es/wiki/Adriana_N%C3%BAñez) · AniList | ✅ (antes ❌) |
| **Ririka Momobami** | **Adriana Núñez** (las gemelas, la misma voz, como en japonés) | ficha de Kakegurui · AniList | ✅ (antes ❌) |
| Sayaka Igarashi | Sofía Huerta | ficha · [ficha de Sofía Huerta](https://doblaje.fandom.com/es/wiki/Sof%C3%ADa_Huerta) | ✅ |
| Runa Yomozuki | Azul Valadez | ficha · [ficha de Azul Valadez](https://doblaje.fandom.com/es/wiki/Azul_Valadez) | ✅ |
| Itsuki Sumeragi | Montserrat Aguilar | ficha · [ficha de Montserrat Aguilar](https://doblaje.fandom.com/es/wiki/Montserrat_Aguilar) | ✅ |
| Midari Ikishima | Liliana Barba | ficha · [ficha de Liliana Barba](https://doblaje.fandom.com/es/wiki/Liliana_Barba) | ✅ |
| Yumemi Yumemite | Annie Rojas | ficha · AniList | ✅ |
| Kaede Manyuda | David Allende | ficha · AniList | ✅ |
| Yuriko Nishinotōin | Georgina Sánchez (T1) / Mayra Arellano (T2) | ficha; AniList sólo da a Georgina Sánchez | ✅ T1 / ⚠️ T2 |
| Ryōta Suzui | Ricardo Bautista | extracto de búsqueda · AniList | ✅ |
| Saori (T1) | Gabriela Ortiz | [Doblaje Wiki: Gabriela Ortiz](https://doblaje.fandom.com/es/wiki/Gabriela_Ortiz) · AniList | ✅ |
| Nanami Tsubomi, Kumagusu, Shinnōji | Araceli Romero, Jahel Morga, Carlos Mireles | sólo AniList | ⚠️ |
| **Dirección de doblaje** | **Guillermo Rojas**; **Daniel Lacy** en los eps. 17-21 | ficha de Kakegurui · [ficha de Guillermo Rojas](https://doblaje.fandom.com/es/wiki/Guillermo_Rojas) («Anime: Kakegurui (2017-2019)») | ✅ (antes ❌) |

Resto del equipo, según la ficha de Doblaje Wiki ⚠️ (una fuente):
traducción **Samatha Castrillón** y **Doralí Sanginés** (T2); adaptación y
producción **Joaquín Alpizar**; mezcla **Daniel RC**, **Jahir Sosa** y
**Eduardo Robles**; ingeniero de sonido **Mario Aldana**. Versión doblada:
audio original de referencia y **guiones de Netflix**.

**Muestras de audio** (Doblaje Wiki, una por personaje, 57 en total):
[Yumeko](https://static.wikia.nocookie.net/doblaje/images/2/25/KAKEGURUIYumekoJabami-1.ogg/revision/latest?cb=20211207164708&path-prefix=es),
[Mary](https://static.wikia.nocookie.net/doblaje/images/2/29/KAKEGURUIMarySaotome-1.ogg/revision/latest?cb=20211207164707&path-prefix=es),
[Kirari](https://static.wikia.nocookie.net/doblaje/images/9/95/KAKEGURUIKirariMomobami-1.ogg/revision/latest?cb=20211207165230&path-prefix=es),
[Ririka](https://static.wikia.nocookie.net/doblaje/images/c/cb/KAKEGURUIRirikaMomobami-1.ogg/revision/latest?cb=20211207165230&path-prefix=es),
[Runa](https://static.wikia.nocookie.net/doblaje/images/e/e5/KAKEGURUIRunaYomozuki-1.ogg/revision/latest?cb=20211207172320&path-prefix=es).
**Nadie las transcribió todavía** con `voz.py` ⚠️: son la vía más corta
para tener frases latinas textuales.

Detalles del doblaje latino (sección «Datos de interés» de Doblaje Wiki,
leída por la API) ⚠️ una fuente:
- Es **el primer anime doblado en Sysdub**.
- **Pochi y Mike pasan a ser «Fido» y «Minina».** Netflix en inglés dice
  «Fido» y «Mittens» ✅ (subtítulo 1×02, 00:04:59).
- Se conserva el sufijo **«-senpai»**.
- Groserías: «perra» y «jodido» en un solo episodio de la T1; en la T2,
  «mierda», «perra» y «carajo».
- «Sumeragi» se pronuncia «Sumeragui»; en el ep. 2 Suzui dice
  «Sumeragüi» varias veces.
- Dicen **«fichas»**: en un capítulo Yumeko dice «apuesto 2 fichas Jabami»
  cuando había tres (un error del doblaje). La wiki lo pone en el ep. 4; en
  el subtítulo japonés el «蛇喰チップ» sale en 1×05, 00:06:54 ⚠️.

**Frases latinas, oídas** (redactor, 25-sep): saqué el audio del ep. 1
latino de [Internet Archive](https://archive.org/download/kakegurui-latino/Kakegurui%20(Latino)%20-%2001%20%5BCrisAnime%5D.mp4#t=731)
(minutos 11:55-12:47 de esa copia) y lo pasé por `voz.py` (Whisper):

| Minuto | Yumeko, en latino (textual según Whisper) | Fiabilidad |
|---|---|---|
| 12:11 | «La locura es la esencia de las apuestas.» | ⚠️ un modelo (small) |
| 12:14 | «En una sociedad capitalista, el dinero y la vida son lo mismo.» | ⚠️ un modelo |
| 12:31 | «En ese caso, mientras más loco estés, más disfrutas apostar.» | ✅ dos modelos (small y medium) dicen lo mismo |
| 12:39 | **«¡Comencemos esta locura!»** (= «さあ 賭け狂いましょう») | ⚠️ medium; small oyó «¿Cómo hacemos esta locura?». Confirmar de oído |

Su voz en esa escena: aguda (268 Hz de media), **muy expresiva**
(27 semitonos de rango) y rápida (3,1 palabras/s), medido por `voz.py`.
En portugués es «Vamos apostar até a loucura!» ⚠️.
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
| **Opening T1**: «Deal with the devil» | **Tia**; letra, música y arreglo de **ryo (supercell)** (corregido: antes decía TeddyLoid) | Tia ✅ ([Fandom](https://kakegurui.fandom.com/wiki/Deal_with_the_Devil), [J-pop Wiki](https://jpop.fandom.com/wiki/Deal_with_the_devil), [web oficial](https://kakegurui-anime.com/1st/discography), [Suruga-ya: el CD](https://www.suruga-ya.com/en/product/120114449)). ryo ⚠️ una fuente, pero primaria: los créditos en pantalla, ep. 1, 3:02 (visto) |
| **Ending T1**: «LAYon-theLINE» | **D-selections**; música de **TECHNOBOYS PULCRAFT GREEN-FUND** | ✅ (MusicBrainz, web oficial y créditos en pantalla, ep. 1, 23:25) |
| **Opening ××**: «コノユビトマレ» | JUNNA | ⚠️ un resumen |
| **Ending ××**: «AlegriA» | D-selections | ⚠️ un resumen |
| **Banda sonora** | **TECHNOBOYS PULCRAFT GREEN-FUND** | ✅ |

- Letra de «Deal with the devil»: [animesonglyrics](https://www.animesonglyrics.com/kakegurui/deal-with-the-devil).
- ~~TeddyLoid, según un TikTok~~: **error corregido**. El crédito del
  opening en pantalla dice 「作詞・作曲・編曲:ryo (supercell)」 (ep. 1,
  3:02, visto). No se encontró una segunda fuente escrita: Discogs y la web
  oficial sólo dan la intérprete, y VGMdb dio Cloudflare ⚠️.
- **Premio**: «Deal with the devil» fue **nominado a mejor opening** en los
  **Crunchyroll Anime Awards** de 2018 (3.ª edición); no ganó ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Crunchyroll_Anime_Award_for_Best_Opening_Sequence)).
- **Ambiente** (visto): el opening (ep. 1, 1:50-3:26) es un desfile de
  dados, cartas, peces y fichas sobre fondo oscuro con acentos rojos, con
  la cámara girando: rápido y descarado. El **ending** (22:40-24:19) es casi
  todo negro: Yumeko baila en silueta blanca entre pétalos y el aura cambia
  de color en cada toma (rojo, verde, magenta, amarillo verdoso, rojo);
  termina en un primer plano de su cara con los ojos muy abiertos y rubor.
- La banda sonora sube cuerdas y percusión en cada apuesta ⚠️ (oído, sin
  fuente escrita). **No encontré un efecto de sonido** que todos reconozcan
  (tipo el «zawa zawa» de *Kaiji*): búsquedas «Kakegurui sound effect
  iconic» y «賭ケグルイ 効果音», sin resultado.
- No se sabe **qué pista suena** en las escenas más fuertes (§D) ⚠️.
- En TikTok, «Deal with the devil» es **el audio de los edits** de Yumeko ✅
  ([TikTok: edits](https://www.tiktok.com/discover/deal-with-the-devil-from-kakegurui-edit),
  [el audio](https://www.tiktok.com/music/deal-with-the-devil-kakegurui-6812060954390498053?lang=en)).

---

## 12 · Vídeos

### 12.1 Mirados de verdad (segunda pasada), con minuto

| Vídeo | Qué es | Minutos útiles |
|---|---|---|
| [Tráiler oficial Netflix, sub. inglés](https://www.dailymotion.com/video/x88p1dp?start=24) (Dailymotion, 512×288) | tráiler T1 | **0:24** Mary: «Today's just not your day, huh?» · **0:36** Yumeko: «Looks like this just got pretty interesting» · **1:06** ojos en primer plano, «Now we're even» · **1:30** créditos del staff |
| [Ep. 1, doblaje latino](https://archive.org/download/kakegurui-latino/Kakegurui%20(Latino)%20-%2001%20%5BCrisAnime%5D.mp4#t=365) (Internet Archive, 853×480) | 1×01 entero | **0:00-1:33** prólogo · **1:50-3:26** opening · **6:05-7:41** piedra, papel o tijera · **11:55-12:43** los ojos rojos · **12:39** «¡Comencemos esta locura!» (§10) · **22:40-24:19** ending |
| [Ep. 2, doblaje latino](https://archive.org/download/kakegurui-latino/Kakegurui%20(Latino)%20-%2002%20%5BCrisAnime%5D.mp4#t=1282) (Internet Archive) | 1×02 entero | **1:00** Mary y la placa «ミケ» · **5:00** Kirari en el pasillo lavanda · **21:16-21:40** Kirari y el acuario · **21:37** el consejo reunido |
| [Eps. 3-12 en latino](https://archive.org/details/kakegurui-latino) | resto de T1 | no mirados. Ojo: el mismo archivo trae **cada episodio también en MKV 1280×720** (leído en su API, `archive.org/metadata`): es la copia buena para capturas |
| [Kakegurui ×× en latino](https://archive.org/details/kakegurui-xx-audio-latino) | T2 doblada | no mirado; serviría para confirmar los minutos `2×…` |

Minuto a minuto, con la pose de cada fotograma, en §2.0.

### 12.2 Análisis, reseñas y recopilaciones (sin mirar)

YouTube pidió iniciar sesión en las dos pasadas; son vídeos de fans, sin
copia en Dailymotion ni en Internet Archive. Quedan **sin minuto** ⚠️.

| Vídeo | Qué es |
|---|---|
| [Tráiler T1, sub. latino (Netflix)](https://www.youtube.com/watch?v=6Fy2WFWNYrA) | tráiler |
| [Tráiler oficial, sub. español](https://www.youtube.com/watch?v=hZ27-_1lf-8) | tráiler |
| [Tráiler oficial de Twin (Netflix)](https://www.youtube.com/watch?v=yihlMRSUiCo) | Mary protagonista |
| [Las Voces de KAKEGURUI](https://www.youtube.com/watch?v=_8F1j9vb9Aw) | reparto latino |
| [«No le importa perder, le importa sentir»](https://www.youtube.com/watch?v=qDDltVILCNY) | psicología de Yumeko, en español |
| [«¿Yumeko, la mente más peligrosa?»](https://www.youtube.com/watch?v=MkZNbCG4cmo) | análisis en español |
| [Resumen en 11 minutos](https://www.youtube.com/watch?v=QHRBimft-nk) | resumen en español |
| [Reseña sin spoilers](https://www.youtube.com/watch?v=UU-fuuwCUSU) | reseña en español |
| [Bilibili: las caras de Yumeko](https://www.bilibili.com/video/av926870921/) | recopilación de 颜艺 |
| [Bilibili: «cambio de cara en un segundo»](https://www.bilibili.com/video/BV1t4411x787) | recopilación |
| [TikTok: caras de Yumeko](https://www.tiktok.com/@parkozue/video/7597656119984540949) | recopilación |

Fan dubs y covers en español, con vistas medidas: §E.

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

## 16 · Vestuario

Texto «Appearance» de cada ficha de la
[wiki](https://kakegurui.fandom.com/wiki/Yumeko_Jabami) (leída por su API)
y colores medidos con `estilo.py` en arte oficial.

| Quién | Ropa icónica | Detalle que no se puede fallar |
|---|---|---|
| Todas | **Uniforme de Hyakkaou**: blazer **rojo** con ribete negro, camisa blanca, corbata negra cruzada, falda a cuadros negro y gris, medias negras, mocasines marrones ✅ | el rojo, medido abajo |
| Yumeko | el uniforme tal cual; pelo negro largo, **corte hime** (flequillo recto); ojos burdeos que se vuelven **rojo brillante**; uñas rojas (beige en la T1 del anime) ✅ | **anillo de plata en el pulgar izquierdo**, de la boda de sus padres ✅ (§C) |
| Yumeko, mascota | **placa de «Mike»** al cuello | 1×03, 00:20:44; placa real en §H |
| Mary | **coletas rubias con lazos negros**, ojos amarillo oscuro; blazer con **botones dorados**; falda **gris lisa y plisada**, no a cuadros ✅ | el pasador de Tsuzura (§C) |
| Kirari | pelo gris claro con dos rodetes y lazos, **labios azules**, ojos celestes ✅ | los rodetes salen de **donas y cuentas budistas** ⚠️ (§C) |
| Ririka | **máscara blanca** de teatro que distorsiona la voz; pelo platino (gris en el anime); sin labial salvo cuando se hace pasar por Kirari ✅ | máscara blanca, **no gris** (corregido) |
| Midari | parche médico en un ojo, vendas | [Fandom](https://kakegurui.fandom.com/wiki/Midari_Ikishima) ✅ |
| Runa | sudadera naranja con capucha de orejas | ⚠️ una fuente |

**El rojo del blazer, medido** ✅ (`estilo.py`, 5 ilustraciones oficiales):

| Imagen oficial | Rojo | Otros |
|---|---|---|
| «Yumeko Kirari Love.png» | `#D63D2C` | oscuros `#382234`, camisa `#DFD8DC` |
| «Mary Saotome and Yumeko Jabami» | `#E5392C` / `#C80812` | piel `#F6E7D3`, negro `#2A1B22` |
| «XX Rei + Kirari.jpg» (uniforme formal) | `#C05051` | grises `#544C5A` |
| Portada de AniList (de noche) | `#AC3933` / `#832B27` | negro `#1F1718`, piel `#E4CEBC` |
| Banner de AniList | `#922B30` | fondo `#18161E` |

**Para la lámina: `#D6362A`**; oscurécelo hacia `#832B27` si la escena es
de noche. El `#C9020F` de la paleta de un fan
([color-hex](https://www.color-hex.com/color-palette/103520)) es más
saturado que cualquier ilustración oficial: sólo como contraste.

**Variantes** (vistas en `hojas/`):
- **Uniforme de verano** femenino: Kirari, 1521×2160 en la wiki ⚠️.
- **Uniforme de chico** (Ryota): blazer oscuro, en «Team, Mary, Ryota.png»
  ([2690×1929](https://static.wikia.nocookie.net/kakegurui/images/6/60/Team%2C_Mary%2C_Ryota.png)) ⚠️.
- **Kimono de Año Nuevo** rojo estampado de Yumeko (hoja
  `vestuario_03.jpg`, n.º 157-159) ⚠️.
- **Uniforme formal con pantalón** de Kirari («XX Rei + Kirari») ✅.
- **Perfumes oficiales** con el uniforme dibujado en el frasco (1149×1500
  cada uno) ✅ (§F).

La ropa **no cambia entre temporadas**: el mismo uniforme en T1, ×× y Twin;
lo que cambia es la luz (§A) ✅ (hojas + key visuals de las dos).
Patrón de costura del uniforme:
[Imaginations Costume](https://www.imaginationscostumes.com/anime-kakegurui-yumeko-jabami-cosplay-uniform/).

---

## 17 · Paisajes y fondos de pantalla

### Los sitios, con su luz (vistos en vídeo)

Fotogramas de los eps. 1 y 2 en latino (§2.0, §12), medidos con
`estilo.py`. Detalle de cada sitio en §5.

| Sitio | Hora y luz | Minuto | Paleta medida |
|---|---|---|---|
| Sala del consejo | interior; **acuario enorme** empotrado, luz **turquesa** que se mueve ✅ | ep. 2, 21:22-21:40 | `#30B5B9` `#76FBF8` |
| Pasillo del consejo | noche; luz **lavanda**, columnas claras, un retrato | ep. 2, 5:00 | `#9495D1`, rojo en sombra `#550C1B` |
| Vestíbulo y escalera | araña dorada, madera oscura, luz cálida | ep. 2, 20:55 | sin medir |
| Aula y pasillo | día; ventana fría, contraluz azulado; caras cálidas | ep. 1, 0:12-0:18 | `#D0C1B6` `#91776F` `#43322D` |
| Aula en partida | focos sobre la mesa, el resto a oscuras | ep. 1, 6:29 | `#11091F` (38 %) |
| Primer plano de la locura | fondo casi negro, un foco cálido | ep. 1, 12:39 | `#1D171C` (53 %), `#C23345` |
| Club de Cultura Tradicional | tatami y madera | — | sin ver ⚠️ |

La regla que se repite: **un solo foco cálido sobre fondo oscuro**; el
color entra en detalles (ojos, acuario, sangre). Es lo que pide el director
Hayashi (§A). Otro fotograma de Kirari (ep. 6, en la wiki, 1280×720) da un
verde oliva (`#D5DE3E` `#B0B62D`): el acuario cambia de tono según la
escena ⚠️.

### Fondos de pantalla (tamaño medido)

De [Wallhaven](https://wallhaven.cc/search?q=kakegurui), con tamaño real
leído en su API. Arte de fans: **sólo para mirar**.

| Tamaño | ♥ | Autor / origen | Enlace |
|---|---|---|---|
| 6752×4000 | 884 | Psychofruit ([Patreon](https://www.patreon.com/posts/yumeko-nsfw-39647346)) | [wallhaven-832511](https://w.wallhaven.cc/full/83/wallhaven-832511.jpg) |
| 8102×2018 (dos monitores) | 183 | Dokkar ([pixiv 66560913](https://www.pixiv.net/member_illust.php?mode=medium&illust_id=66560913)) | [wallhaven-1j5ze3](https://w.wallhaven.cc/full/1j/wallhaven-1j5ze3.jpg) |
| 6000×5050 | 111 | bubbleboba | [wallhaven-k7r6k6](https://w.wallhaven.cc/full/k7/wallhaven-k7r6k6.jpg) |
| 2600×4000 | 87 | MostlyBlueWyatt ([X](https://x.com/MostlyBlueWyatt/status/1975312679415022067)) | [wallhaven-k8xlym](https://w.wallhaven.cc/full/k8/wallhaven-k8xlym.png) |
| 1920×2463 | 152 | Aoi Ogata ([ArtStation](https://www.artstation.com/artwork/34XkD)) | [wallhaven-x1qzro](https://w.wallhaven.cc/full/x1/wallhaven-x1qzro.jpg) |
| 3840×2160 | — | minimalista de Yumeko | [wallhaven-1j55g9](https://w.wallhaven.cc/full/1j/wallhaven-1j55g9.png) |

**Oficiales**: la web del anime no ofrece fondos. Sólo **ALL IN** regaló
uno para celular por X al lanzarse (2026), por campaña, sin archivo
público ⚠️. Las colecciones de
[Alpha Coders](https://wall.alphacoders.com/by_sub_category.php?id=269743&name=Kakegurui+Wallpapers&filter=4K+Ultra+HD),
[WallpaperAccess](https://wallpaperaccess.com/kakegurui) y
[Wallpaper Cave](https://wallpapercave.com/kakegurui-wallpapers) dicen
«4K» en el título, pero **no están medidas**: mejor las de arriba.

---

## 18 · Guía para generar con IA (Firefly, Canva)

> Úsala sólo para **fondos, objetos o bocetos de pose**. El personaje final
> se calca de un fotograma real (§15), nunca de la IA.

### 18.1 Para una IA de imagen

**Rasgos que nunca cambian** (§16)
- Yumeko: pelo **negro, largo, liso, corte hime**; ojos **rojos** cuando
  juega; blazer **rojo** con ribete negro; corbata negra cruzada; anillo
  de plata en el pulgar izquierdo.
- Mary: **coletas rubias con lazos negros**, ojos amarillos, botones
  dorados, falda gris lisa.
- Kirari: **pelo gris muy claro** con dos rodetes, ojos celestes,
  **labios azules**.
- Ririka: **máscara blanca** de teatro, pelo platino.

**Paleta medida**: rojo `#D6362A` (de noche `#832B27`), negro de fondo
`#1D171C`, piel `#EFDADC`, rojo de ojos `#C23345`, turquesa de acuario
`#30B5B9`, lavanda de pasillo `#9495D1` (§5, §16, §17).

**Línea y sombra**: línea fina y limpia, **oscura y cálida**, no negro
puro; sombra en bloques con el acabado suavizado por la fotografía
(`estilo.py` lo lee como «degradado, poca línea»); **sombra dura** en la
cara cuando la escena se tensa; dos brillos en el iris y en los labios
(§A).

**Luz**: **un solo foco cálido** y un **contraluz rojo** o **turquesa de
acuario**. Fondo que se oscurece detrás del personaje.

**Encuadre**: plano medio, mesa en primer plano algo desenfocada, cámara
un poco baja. Para la cara de locura, primer plano cerrado sobre fondo
negro o de un color (§A).

**Palabras que ayudan** (en inglés): «anime key visual, MAPPA 2017 style,
elite private academy, red school blazer with black trim, casino chips and
playing cards on a green felt table, single warm spotlight, dark
background, dramatic rim light, glowing red eyes, cel shading, high
contrast».

**Vocabulario de expresiones** (para pedir cada gesto):
- **kaogei / 顔芸** (la cara exagerada de ganar o perder): «wide manic
  grin, glowing red eyes, flushed cheeks, hands clawed near face» — es el
  gesto del ep. 1, 12:15-12:43.
- **Cara normal**: «calm gentle smile, closed eyes, hands together» (ep. 1,
  7:29). Akita cuida más la cara normal para que el kaogei golpee (§A):
  pide las dos, nunca una intermedia.
- **Miedo**: «tiny pupils, teary huge eyes, extreme close-up» (Mary, ep. 1,
  12:31).
- **Rabia**: «gritted teeth, furrowed brows, raised fist» (Mary, ep. 2,
  1:00).
- **Pensar**: «profile view, half-closed eyes, hand on chin» (Kirari, ep. 2,
  21:16-21:34).
- En los eps. 1-2 mirados **no hay** gotas de sudor cómicas ni *chibi*;
  el humor deformado va al spin-off cómico **Kakkokari** (portadas en
  `hojas/`) ⚠️ (visto en 2 de 24 episodios).

**Palabras que lo estropean**: «chibi», «kawaii», «pastel», «3D render»,
«photorealistic», «Las Vegas neon», «revealing», «sexy», «sweat drop».
Evita cualquier pose sugerente: el meme viral de 2026 lo es.

**Referencias de estilo**: el key visual de ××
([LisAni!](https://www.lisani.jp/0000117737/)), las hojas de personaje de
×× ([PASH! PLUS](https://www.pashplus.jp/anime/117240/)), «Gambling-School
Visual» (1499×2048, hoja `personajes_01.jpg` n.º 46).
**Referencias de pose**: los minutos de §2.0 y §15.

### 18.2 Para una IA de texto (cómo escribir sus diálogos)

**Cómo habla cada una** (§7.2):
- **Yumeko**: muy educada, «usted» en español; sube el ritmo con una
  palabra repetida («さあ さあ さあ…») y estalla con **una** exclamación.
  Nunca insulta. Explica la locura como algo lógico, en frases cortas.
- **Mary**: dos voces. En público, dulce y falsa («あ〜ら あら» → «¡Vaya,
  vaya!»). Enfadada, **muy grosera** y corta: «クソッ», «ナメやがって».
- **Kirari**: dama tranquila; preguntas raras y bellas; nunca grita.
- **Ririka** (con máscara): seca, casi militar, sin adornos.
- **Runa**: alarga las vocales («〜»), se ríe «¡Nyahaha!».
- **Midari**: ruda, se ríe «ウヘッ» («¡Uhé!»).

**Frases reales, por emoción** (con minuto):

| Emoción | Frase | Quién, dónde |
|---|---|---|
| Alegre / celebrar | «¡Comencemos esta locura!» | Yumeko, latino, 1×01, 12:39 ⚠️ (§10) |
| Alegre / celebrar | «さあ さあ さあ さあ! … 賭け狂いましょう!» | Yumeko, 1×03, 00:15:58 |
| Alegre / gancho | «Looks like this just got pretty interesting» | Yumeko, tráiler, 0:36 |
| Enfadada | «ボンボンのバカ娘が ナメやがって» («¡La niña rica tonta se burla de mí!») | Mary, 1×01, 00:13:19 |
| Enfadada | «クソッ» / «ウッゼ〜» | Mary, 1×01, 00:11:19; 1×04, 00:12:34 |
| Burla | «Today's just not your day, huh?» | Mary, tráiler, 0:24 |
| Explicando | «La locura es la esencia de las apuestas.» | Yumeko, latino, 1×01, 12:11 ⚠️ |
| Explicando | «En ese caso, mientras más loco estés, más disfrutas apostar.» | Yumeko, latino, 1×01, 12:31 |
| Explicando / retar | «Si aciertas dónde están los votos, te doy estos cien» | Ririka, 2×03, 00:07:36 |
| Animando / saludo | «みんな こんにちは〜!» («¡Hola a todos〜!») | Runa, 2×02, 00:04:34 |
| Pensando | «月の裏側って見たことある?» («¿Has visto la cara oculta de la Luna?») | Kirari, 1×06, 00:24:09 |
| Triste | «How did this happen, anyway?» | Mary, 1×01, 00:16:59 |
| Triste / vergüenza | «私は… 私は…» («Yo… yo…») | Ririka sin máscara, 2×03, 00:18:05 ⚠️ |

**Puntuación y exageración**: puntos suspensivos antes de estallar;
exclamación al final, no en cada frase; la tilde de alargar («〜») sólo
para Runa y para la dulzura falsa de Mary. Nada de emojis ni de
«jajaja»: cada una tiene su risa.

**Vocabulario del mundo** para los textos del bot (§H): *mascota*
(«Pochi», «Mike»), *donación*, *combate oficial*, *plan de vida*,
*consejo estudiantil*, *los 100 votos*, *all in*.

---

## A · Estilo de dibujo y técnica, y cómo replicarlo (punto 18)

### A.1 Lo que dice el equipo

- **Pensar como cine de imagen real.** El director **Yuichiro Hayashi**
  (林祐一郎) se preguntaba «si esto fuera imagen real, ¿cómo lo filmaría?».
  Buscaba encuadres con «peso emocional, energía y tridimensionalidad» y
  **jugar con la luz**: «luz de tarde, luz de luna, distintas luces», lo que
  el manga en blanco y negro no puede dar ✅
  ([easternkicks](https://www.easternkicks.com/features/yuichiro-hayashi-interview/),
  [All the Anime](https://blog.alltheanime.com/interview-yuichiro-hayashi/)).
- **Dos temporadas, dos filtros.** La T1 es «oscura, sucia y realista»;
  la ×× es «más colorida, más vibrante» ✅ (easternkicks +
  [Anime UK News](https://animeuknews.net/2019/08/interview-kakegurui-director-yuichiro-hayashi/)).
- **La cara normal se cuida más.** El diseñador **Manabu Akita** (秋田学)
  dibuja las caras normales «simples y monas» a propósito, para que el
  contraste con el **顔芸** (kaogei, la cara exagerada) golpee más ✅
  ([MANTANWEB](https://mantan-web.jp/article/20190309dog00m200005000c.html),
  [4Gamer](https://www.4gamer.net/games/338/G033856/20170809048/)).
- **Manos y cartas en 3DCG.** Cada temporada tiene un **director de CG**
  (Jae-Hun Sin en la T1; Motoi Okuno en ××) ✅
  ([AniList](https://anilist.co/anime/98314/staff)). Que las cartas y las
  manos se animen en 3D dentro del dibujo 2D sale de un resumen de la
  entrevista de [Comic Natalie](https://natalie.mu/comic/pp/kakegurui_anime01),
  que da 403 directa y en Wayback ⚠️.
- **Programas del estudio** (Clip Studio, RETAS, Toon Boom…): **no lo
  encontré** en ninguna entrevista ⚠️ (búsquedas en japonés e inglés,
  bitácora).

### A.2 Línea, sombra y luz

- **Línea** fina y limpia, **oscura y cálida**, no negro puro ✅ (`estilo.py`
  en 6 fotogramas, §17).
- **Sombra**: el diseño es de bloques (piel y sombra), pero la fotografía
  lo suaviza: `estilo.py` lo lee como «degradado, poca línea» ✅. En los
  primeros planos de tensión la sombra se vuelve **dura y angulosa**
  (mandíbula, párpado) ⚠️ (visto en ep. 1, 12:15-12:43).
- **Ojos**: dos brillos redondos en el iris; labios húmedos ⚠️.
- **Luz**: un foco cálido y un **contraluz de color** (rojo cuando gana,
  turquesa cerca del acuario) ✅ (§17 + Hayashi).
- **Manga** (Naomura): pelo negro relleno, poca trama, rayas finas
  radiales alrededor de los ojos en la locura; línea gruesa, sin grano de
  papel (§B) ✅.

### A.3 Encuadres y composición

- **Apuesta**: plano medio, **mesa en primer término** algo desenfocada,
  cámara un poco baja ✅ (ep. 1, 6:05-7:41).
- **Kaogei**: primer plano muy cerrado, cámara a la altura de los ojos,
  fondo que se apaga a negro o a un color ✅ (ep. 1, 12:39, fondo `#1D171C`
  en el 53 % del cuadro).
- **Consejo**: plano medio-largo, simétrico, Kirari centrada a la cabecera
  ✅ (ep. 2, 21:37).
- **Miedo**: los ojos llenan el plano (Mary, ep. 1, 12:31) ✅.

### A.4 Cómo reproducirlo en Photoshop

1. **Línea**: pincel duro de borde limpio, 2-3 px en un lienzo de 2000 px;
   color `#2A1B22`, no negro puro. Sin textura de papel.
2. **Sombra**: una capa en **Multiplicar** recortada sobre el color base,
   pintada con **lazo poligonal** (formas duras). Después, desenfoque
   gaussiano de 1-2 px sólo en esa capa: así sale el bloque suavizado.
3. **Contraluz**: capa en **Trama** o **Aclarar**, sólo en el borde del pelo
   y el hombro; rojo `#C23345` o turquesa `#30B5B9`.
4. **Ojos**: dos elipses blancas y un degradado sutil en **Superponer**.
5. **Kaogei**: exagera **sólo** boca, cejas y pupilas; el resto de la
   cara queda como el diseño de Akita.
6. **Grano**: ruido del 2-3 % en **Superponer** para la T1; quítalo y sube
   algo la saturación para ××. Es una receta para llegar al mismo aspecto,
   no el proceso del estudio ⚠️.

### A.5 Cómo reproducirlo en Blender

1. **Sombreado de dibujo**: `Shader to RGB` → `Color Ramp` de 2-3 bandas
   en **Constant** → `Emission` (Eevee).
2. **Contorno**: modificador **Solidify** con normales invertidas, material
   negro cálido, grosor 0,01-0,02; o **Freestyle** a 1-1,5 px.
3. **Luz**: una **key** cálida (unos 3200 K) y un **rim light** rojo o
   turquesa detrás; sin relleno de frente, para no perder la sombra dura.
4. **Modelos y rigs libres** (API de Sketchfab):
   - [Runa Yomozuki con rig](https://sketchfab.com/3d-models/runa-yomozuki-kakegurui-70dafed89bcd4dd3b9f5654f90ebeef3),
     Gustav_Johansson00, **CC BY-NC**, 40 434 caras ✅.
   - [Kakegurui Runa](https://sketchfab.com/3d-models/kakegurui-runa-b015aaa7272c4191a543722ead37a316),
     claener, **CC BY**, 2,46 millones de caras, sin rig ✅.
   - [Yumeko](https://sketchfab.com/3d-models/yumeko-9834761e49a346cba73c8e1d9ab40122),
     Yaanaa, CC BY 4.0 (el personaje sigue siendo de Square Enix: sólo
     para posar y mirar) ✅.
   - Mary y Kirari: **no hay** modelo libre y descargable ⚠️ (API,
     `q=kakegurui mary`, `q=kakegurui kirari`).
   - Mesa, fichas y cartas: §4.1.
5. **Encima**: textura de sarga fina en Multiplicar sobre el blazer y una
   **aberración cromática muy leve** en los bordes del contraluz rojo, para
   el aspecto «sucio» de la T1.

---

## B · Texturas 2D (punto 19)

| Capa | Qué se ve en la serie | Equivalente libre | Licencia |
|---|---|---|---|
| **Trama de manga** | poca trama; rayas radiales en los ojos de la locura (hojas `personajes_02.jpg` y `vestuario_03.jpg`, n.º 58, 63, 67, 74, 90, 130, 149, 163-164, 170-172) ✅ | [Manga Screentone Pack 1](https://assets.clip-studio.com/en-us/detail?id=2142037), CLIP STUDIO ASSETS | gratis, de un tercero ⚠️ comprobar al bajar |
| **Grano de papel** | el manga no lo tiene (impresión digital); úsalo sólo en el papel del objeto | [ambientCG Paper001](https://ambientcg.com/view?id=Paper001), [Paper005](https://ambientcg.com/view?id=Paper005), [Paper006](https://ambientcg.com/view?id=Paper006) | **CC0** ✅ |
| **Cartón** | caja de cartas del consejo | [ambientCG Cardboard002](https://ambientcg.com/view?id=Cardboard002) | **CC0** ✅ |
| **Falda a cuadros** | Yumeko: negro y gris; Mary: gris lisa | [TextureCan, Red Tartan](https://www.texturecan.com/details/595/) (recolorear), [Raw Catalog, Tartan Cloth](https://www.rawcatalog.com/asset/3450/) | libre ⚠️ comprobar al bajar |
| **Dorso de carta** | rombos rojos y negros, visto en la base de las figuras ARTFX J (§F) ✅ | dibujarlo: patrón de rombos en Photoshop | propio |
| **Tapete y madera** | mesa de juego | §5.4 ([Poly Haven wood_table_worn](https://polyhaven.com/a/wood_table_worn)) | **CC0** ✅ |
| **Emblemas** | placas de mascota, clan Momobami (§H) | usar su forma como referencia y redibujar | © titulares |

**Escudo del colegio**: **no lo encontré**. Busqué «emblem», «crest»,
«badge», «insignia» en la wiki inglesa y «校章», «エンブレム», «紋章» en
Wikipedia japonesa; ninguna describe uno ⚠️. Lo más parecido es el sello
rojo de los papeles del consejo (§7). La baraja oficial con estampado
metálico (賭ケグルイ 箔押しトランプ) no tiene imagen pública que encontrara
⚠️.

---

## C · Gustos y detalles de cada personaje (punto 20)

No hay *databook* oficial. La fuente más rica es un **podcast del propio
autor, Homura Kawamoto, con su hermano**, traducido en un hilo de X por
[@Shishi_Odoshii](https://x.com/Shishi_Odoshii/status/2005737101116203158)
(29-dic-2025), leído con `api.fxtwitter.com`. Es la voz del autor, pero
traducida por un fan: por eso lleva ⚠️. El resto, de las fichas de la
[wiki](https://kakegurui.fandom.com/wiki/Yumeko_Jabami) y de
[AniList](https://anilist.co/character/121889).

| | Yumeko | Mary | Kirari | Ririka |
|---|---|---|---|---|
| **Altura** | 166 cm ✅ (wiki + AniList) | 162 cm ✅ (wiki + AniList) | 166 cm ⚠️ | 166 cm, gemela ✅ |
| **Cumpleaños** | no revelado | **8 de marzo** ✅ (AniList + manga, cap. 21) | no revelado (el 24/8 de AniList no tiene fuente) | no revelado |
| **Comida** | — | — | **McDonald's, donas y café**; kimchi y pulpo; casi no come carne ⚠️ | — |
| **Afición** | apostar por la emoción, no por el dinero ✅ | — | **baloncesto** ⚠️ | — |
| **Ama / odia** | — | odia **los abrazos**; le gusta la gente muy honesta ⚠️ | se aburre: ya sabía todo lo del colegio antes de llegar ⚠️ | — |
| **Siempre lleva** | **anillo de plata** en el pulgar izquierdo, de la boda de sus padres ✅ | el **pasador de Tsuzura**, su amiga de *Twin* ✅ | rodetes inspirados en **donas y cuentas budistas** ⚠️ | **máscara de repuesto**; un iPhone ⚠️ |
| **Cómo se ve** | nunca tiene monólogo interno: no sabemos qué piensa ✅ | **becada** y sin dinero; quiere «ser una ganadora de verdad» ✅ | — | sólo **la suplente** de Kirari ✅; más cercana a Mary y Yumeko que su hermana ⚠️ |

**Por qué casi nadie tiene cumpleaños**: Kawamoto dice que no los fija
«porque podrían usarse en la historia, como pasó con Mary» ⚠️. Las fichas
de la wiki dejan vacío el campo en Yumeko, Kirari, Ririka, Midari y Runa ✅.

**Secundarias**:
- **Runa**: 130 cm, la más bajita ⚠️; su risa «にゃはは» es la única risa
  propia de un personaje ✅.
- **Midari**: 170 cm, la más alta ⚠️; **zurda** ⚠️; la única con peso en
  todos los medios (manga, Twin, anime, drama) ✅.
- **El favorito del autor** es Yumeko; el de su hermano, Sumika
  Warakubami ⚠️. La seiyū de Yumeko, **Saori Hayami**, eligió a **Midari**:
  «pone la misma cara que un cachorro esperando a su dueño» ✅
  ([entertainmentstation.jp](https://entertainmentstation.jp/388789/2), vía
  la [wiki](https://kakegurui.fandom.com/wiki/Midari_Ikishima)).

---

## D · Por qué la gente la ama (punto 21)

### D.1 Ventas y premios

- **El manga no para de crecer**: 4 millones de copias (feb-2018) → 5 (2019)
  → 6,2 (2021) → **6,8 millones** (jun-2022) ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Kakegurui),
  [ANN](https://www.animenewsnetwork.com/daily-briefs/2018-02-01/kakegurui-manga-has-4-million-copies-in-print/.127149)).
- **«Deal with the Devil»** fue **nominado a mejor opening** en los 3.º
  Crunchyroll Anime Awards (2018), contra *Darling in the Franxx* y *JoJo*;
  no ganó ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Crunchyroll_Anime_Award_for_Best_Opening_Sequence)).
- **Resurgir en 2020**: Megan Thee Stallion y Poppy se disfrazaron de
  Yumeko y hablaron de la serie; trajo fans nuevos tres años después ✅
  ([CBR](https://www.cbr.com/how-kakegurui-anime-became-popular/)).
  En 2026, el meme «kakegurui mashou» la volvió viral otra vez (§14).

### D.2 Con quién se identifica el público

- **Yumeko**: parece ingenua pero pilla cualquier trampa y **disfruta el
  juego, no el premio**. La gente se identifica con esa falta de miedo ⚠️
  (resumen de hilos de MyAnimeList).
- **Mary**: pierde, se humilla y vuelve. Y en *Twin* se sabe que es
  **becada en un colegio de ricos**: su hambre de ganar tiene raíz de clase.
  Por eso es la más votada ✅ (§9).
- **El autor se sorprendió**: Kirari no quedó 1.ª, Mary la superó y
  Yumeko quedó 5.ª; cree que **Ririka subiría** si se repitiera ⚠️ (podcast,
  tuits [2/21](https://x.com/Shishi_Odoshii/status/2005734414832263348) y
  [13/14](https://x.com/Shishi_Odoshii/status/2005737123933217025)).
- Aquí nadie gusta por huir: gusta **plantarse y apostarlo todo**.

### D.3 Las escenas: aquí no se llora, se grita

Kakegurui **no es una serie que haga llorar**: hace gritar de emoción o
reír de vergüenza ajena. Estas son las que todos recuerdan.

| Escena | Minuto | Qué pasa | Cómo está hecha | Cómo reaccionó la gente |
|---|---|---|---|---|
| **«¡Comencemos esta locura!»** (grito) | 1×01, 00:12:08-00:12:40 (sub); 11:55-12:43 (visto, latino) | Yumeko explica por qué apostar la vida da placer y reta a Mary | un foco cálido, fondo negro `#1D171C`, ojos rojos, cámara que se acerca; cuerdas y percusión que suben | la frase es el meme de 2026 y el clip más repetido ([Know Your Meme](https://knowyourmeme.com/memes/kakegurui-masho-kakeguruimashou-trend), CBR) |
| **Mary en el suelo** (vergüenza ajena, y algo de pena) | 1×01, 00:16:59 (sub) | la que humillaba acaba de mascota, «How did this happen, anyway?» | el aula a oscuras, Mary pequeña en el encuadre ⚠️ | el inicio del arco favorito de los fans (wiki, Screen Rant, CBR) |
| **Mary con la placa «ミケ»** (rabia) | ep. 2, 1:00 (visto) | Mary furiosa levanta la placa con cadena | primer plano del puño | — |
| **Ririka sin máscara** (lo más cercano a la pena) | 2×03, 00:18:05 (sub) ⚠️ | la Momobami fría se traba: «私は… 私は…» | sin ver ⚠️ | según el autor, la primera vez que se planta ante Kirari ⚠️ |

**Qué música suena** en cada una: **no lo encontré** ⚠️ (el OST no trae
minutos y VGMdb da 403). Lo oído: subidas de cuerda y percusión en cada
apuesta (§11).

---

## E · Fan dubs y comunidad hispana (punto 22)

Todo con título, canal, vistas y fecha leídos con `yt-dlp` (sin descargar
el vídeo) ✅, salvo TikTok, que bloquea `yt-dlp` ⚠️.

### E.1 Fan dubs en español

| Qué | Canal | Vistas | Fecha |
|---|---|---|---|
| [Capítulo 1 (clip), fandub español](https://www.youtube.com/watch?v=ub4zVzGiD8w) | **Sakato Irumi**, con Lirin1996 y JonTenox | 94 330 | 07-mar-2018 |
| [Live action, fandub latino](https://www.youtube.com/watch?v=6OFbbHMq7-I) | **El DMNT** | 15 398 | 19-nov-2020 |
| [Yumeko vs Mary, fandub latino](https://www.youtube.com/watch?v=YjKNo0ajMO8) | **Sekai no Yuro FD** | 1922 | 08-jun-2021 |
| [OVA 1, Maid Café Hyakkaou, fandub latino](https://www.youtube.com/watch?v=b9vkToczwjU) | **GoldFandubs** | 203 | 22-dic-2024 |

Créditos que traen: en el cap. 1, traducción y adaptación de Lirin1996; en
la OVA, Yumeko es *Dian_dubs*, Mary *Takiry*, Suzui *Affter!Vibes*.

### E.2 Covers del opening en español

| Cover | Canal | Vistas | Fecha |
|---|---|---|---|
| [Deal With The Devil (cover español)](https://www.youtube.com/watch?v=TbAUB9c0Lgk) | **Miree**, con Aryes Anime y Pidrosax | **634 563** | 04-dic-2020 |
| [Opening FULL, fandub español](https://www.youtube.com/watch?v=TQKT8qLqt8E) | **Hana** | 202 072 | 03-sep-2017 |
| [Opening, fandub español](https://www.youtube.com/watch?v=2LMGHGeasfw) | **Hana** | 21 564 | 06-jul-2017 |
| [OP, fandub latino](https://www.youtube.com/watch?v=50RHkSSOTs0) | **Skargu** | 8233 | 20-jul-2017 |
| [Opening, fandub latino](https://www.youtube.com/watch?v=lSfFW6GQOvw) | **Val** | 2703 | 08-may-2018 |
| [Cover español](https://soundcloud.com/user-652528345/kakegurui-opening-deal-with) | bestendista (SoundCloud) | 135 | — |

El de **Miree** sale en diciembre de 2020, justo con el resurgir que cuenta
CBR (§D).

### E.3 Parodias y memes (TikTok, sin poder abrirlos) ⚠️

- [@kazumaldito](https://www.tiktok.com/@kazumaldito/video/7490415201846660358):
  «kakegurui mashou» en japonés contra el doblaje; unos **288 mil me gusta**
  según el buscador.
- [@marhinafrances](https://www.tiktok.com/@marhinafrances/video/7245344327600278810):
  doblaje casero de Yumeko y Mary.
- [@kodenwatch](https://www.tiktok.com/@kodenwatch/video/6986793041587703046):
  «¿Cuál prefieres?», análisis de doblajes.
- [@kira.bug](https://www.tiktok.com/@kira.bug/video/6917750424757931269)
  (latino contra castellano) y el reto de
  [@jarigrt](https://www.tiktok.com/@jarigrt/video/7344802281633746181), en §10.

**No encontré** fan dubs ni covers de *Twin* ni de ×× en español: la
comunidad hispana se quedó con la T1 y el *live action*.

---

## F · Colaboraciones, figuras y cosplay (punto 23)

Casi todo sale de [collabo-cafe.com](https://collabo-cafe.com/) (agregador
japonés de eventos), cruzado con otra fuente cuando la hay.

| Qué | Cuándo | Qué trae | Fuente | Estado |
|---|---|---|---|---|
| **Karaoke no Tetsujin** × Kakegurui | 15-sep a 5-nov-2017, 7 locales de Tokio | decoración y menú temático | [collabo-cafe](https://collabo-cafe.com/events/collabo/kakegurui-karatetsu/) | ⚠️ |
| **Myoujin Cafe** × Kakegurui | 30-ago a 1-oct-2017 | menú «con mucho de apuesta», bebidas con personaje | [collabo-cafe](https://collabo-cafe.com/events/collabo/kakegurui-myoujin-cafe/) | ⚠️ |
| **Kakegurui Cafe** (Princess Cafe, 4 locales) | 27-abr a 31-may-2019 | café oficial de ××, posavasos | [collabo-cafe](https://collabo-cafe.com/events/collabo/kakegurui-princess-cafe2019/) | ⚠️ |
| **SINoALICE** × Kakegurui ×× | abr-2022 | cruce en el gacha para móvil | [ANN](https://www.animenewsnetwork.com/press-release/2022-04-26/sinoalice-has-started-a-collaboration-with-kakegurui-xx/.185026) + wiki | ✅ |
| **Exposición 賭ケグルイ展** | desde 4-feb-2023, Tokio, Fukuoka, Osaka | páginas originales e ilustraciones a color; firma de Kawamoto | [collabo-cafe](https://collabo-cafe.com/events/collabo/kakegurui-exhibition-tokyo-fukuoka-osaka-2023/) (imagen 1280×803) | ⚠️ |
| **Pachislot «蛇喰夢子という女»** y **pachinko «eカケグルイ»** | 2023 y 2026 | arte propio: Yumeko con «さぁ» en rojo; Yumeko mordiéndose la uña | [p-town](https://p-town.dmm.com/machines/4374) + [P-WORLD](https://www.p-world.co.jp/machine/database/9844); [p-town](https://p-town.dmm.com/machines/5004) + [pachinkovillage](https://www.pachinkovillage.com/pachinko/p.php?M=7445) | ✅ |
| **Perfumes** de Yumeko y Mary | — | el uniforme dibujado en el frasco (1149×1500) | wiki + [essential-japan](https://essential-japan.com/news/kakegurui-perfume/) | ✅ |
| **PALE TONE** (Contents Seed) | 2024-2025 | acrílicos en acuarela pastel: Yumeko, Kirari, Mary, Ryota | [vol. 1](https://collabo-cafe.com/events/collabo/kakegurui-pale-tone-series-contents-seed-anime-store-goods2024/), [vol. 3](https://collabo-cafe.com/events/collabo/kakegurui-pale-tone-series-vol3-contents-seed-anime-store-goods2025/) | ⚠️ |

**Figuras oficiales** (su pose es una referencia 3D):
- **ARTFX J de Yumeko y de Mary** (Kotobukiya, reedición anunciada el
  20-oct-2024): cartas volando, pelo al viento, pose de **lanzar cartas**;
  la base lleva el dorso de carta de rombos ✅
  ([collabo-cafe](https://collabo-cafe.com/events/collabo/kakegurui-reproduction-figure-ktobukiya-anime-store-goods2024/),
  imagen 2002×1082).
- **Mary 1/6 de Union Creative** (anuncio 20-sep-2025, venta mar-2026):
  uniforme, sonrisa de «ya gané», cartas cayendo, base de mesa de casino ⚠️
  ([collabo-cafe](https://collabo-cafe.com/events/collabo/kakegurui-mary-scale-figure-union-creative-anime-store-goods2025/),
  imagen 1200×615).

**Cosplay**: 20 fotos **CC BY-NC-SA 2.0** en Openverse (Yumeko, Mary, Runa;
683-1024 px, medidas) ✅, en §4.4. Patrón del uniforme:
[Imaginations Costume](https://www.imaginationscostumes.com/anime-kakegurui-yumeko-jabami-cosplay-uniform/).
Megan Thee Stallion y Poppy de Yumeko: §D.

**No encontré** colaboraciones fuera de Japón (Fortnite, gachas globales
grandes) ⚠️: no busqué en chino ni en coreano.

---

## G · Obras parecidas y temas relacionados (punto 24)

**De tono parecido** (recomendaciones de usuarios de
[AniList](https://anilist.co/anime/98314)): *No Game No Life*, *Classroom of
the Elite*, *Death Parade*, *Kaiji*, *Death Note*, *Prison School*, *Akagi*,
*Tomodachi Game*, *Talentless Nana*. Todas son **juegos psicológicos con
mucho en juego** ✅.

**Lo que reconoce el autor** (entrevista en japonés,
[Big Comic BROS.NET](https://bigcomicbros.net/8281/)) ⚠️ una fuente, pero
es su propia voz:
- ***Kaiji*** de Nobuyuki Fukumoto: «¡Existe un manga así!».
- Fuera de las apuestas: la novela *El caso de los crímenes del zodíaco*
  (Sōji Shimada), *Satsuriku ni Itaru Yamai* (Takemaru Abiko) y la novela
  visual *Kamaitachi no Yoru*.
- Su regla: **«se dibuja a la persona que juega, no el juego»**. Por eso
  manda la cara, no las reglas.
- La escena de Sayaka acariciando la silla de la presidenta fue **idea del
  dibujante, Tōru Naomura**.

**Otras láminas del servidor** (para no repetir):
- **Death Note** (`biblias/18-death-note/`): mismo género, pero sus
  conceptos usan **un cuaderno** y **un televisor**; ni mesa, ni cartas, ni
  fichas. No choca ✅.
- **No Game No Life** (`encargos/84-no-game-no-life.md`): su biblia aún no
  existe. Si se hace, que **no repita la mesa con cartas y fichas** como
  objeto central (aviso para el dueño) ⚠️.
- **Assassination Classroom**: colegio, pero sin apuestas; no choca.

---

## H · El mundo, la historia y sus símbolos (punto 25)

### H.1 Las reglas, en cinco líneas

1. En la **academia Hyakkaou** (私立百花王学園, 122 años) no mandan las notas
   ni el deporte: **manda el que gana apostando** ✅
   ([wiki](https://kakegurui.fandom.com/wiki/Hyakkaou_Private_Academy)).
2. El **consejo estudiantil** cobra «donaciones», voluntarias en teoría y
   obligatorias en la práctica, y con eso controla todo ✅.
3. Los **últimos 100 de 3000** se vuelven **mascotas** (家畜): «Pochi» los
   chicos y «Mike» las chicas, con placa al cuello y sin derechos. Salen
   ganando un **combate oficial** o pagando un millón de yenes ✅
   ([wiki](https://kakegurui.fandom.com/wiki/Housepet)).
4. Quien no puede pagar recibe un **plan de vida** (人生計画表), un
   cuadernillo que le dicta trabajo y boda al graduarse ✅.
5. Detrás está el **clan Momobami** (百喰一族, «las cien familias
   devoradoras»): ramas rivales, apellidos acabados en «-bami», cada una
   con un negocio. Kirari lo manda desde los siete años ✅
   ([wiki](https://kakegurui.fandom.com/wiki/The_Hundred_Devouring_Families)).

### H.2 La historia por arcos

Según la [wiki](https://kakegurui.fandom.com/wiki/Story_Arcs):

**Temporada 1** (eps. 1-12): Yumeko llega y gana a Mary a piedra, papel o
tijera → cae a mascota y juega póquer indio → Midari la reta a un juego de
vida o muerte → gana a Yumemi (la ídolo) y a Kaede (el contable) → duelo
final con Sayaka en la **Torre de las Puertas**.

**Temporada 2, ××** (eps. 13-24): la guillotina de dedos → Nim Type Zero
con dos Momobami → el juego del bien común por los votos → concurso de
actuación con Yumemi → la subasta de cien votos (sólo del anime) → la
elección: Ririka enmascarada y sus **100 votos**, y Kirari reelegida.

El manga sigue con arcos (la guerra, el gran torneo) **sin anime** ✅.

**Momentos clave, en orden**:
- 1×01, 00:12:37: «さあ 賭け狂いましょう!», el título dicho en voz alta.
- 1×02, 00:03:51-00:04:59: se explica el sistema de mascotas.
- 2×03, 00:07:31: Ririka y los 100 votos.
- 2×05, 00:07:01: Kirari dice «オールイン» (all in) dos veces.

### H.3 Emblemas y objetos (medidos en la wiki)

| Objeto | Qué es | Imagen | Tamaño |
|---|---|---|---|
| Placas de mascota | chapa con forma de pata, una de gata y otra de perro | [Kakegurui_collar.jpg](https://static.wikia.nocookie.net/kakegurui/images/c/c3/Kakegurui_collar.jpg/revision/latest?cb=20201225202413) | 749×807 ✅ |
| Placas juntas | muchas sobre una mesa (drama) | [Housepet_tags_drama.jpg](https://static.wikia.nocookie.net/kakegurui/images/e/e3/Housepet_tags_drama.jpg/revision/latest?cb=20190714181215) | 1000×667 ✅ |
| Sistema de mascotas (manga) | viñeta que lo explica | [Volume_1_Pet_System](https://static.wikia.nocookie.net/kakegurui/images/6/65/Volume_1_Pet_System_explanation_image.PNG/revision/latest?cb=20170630200326) | 881×343 ✅ |
| La academia | fachada occidental | [HyakkaoAcademy.jpg](https://static.wikia.nocookie.net/kakegurui/images/7/78/HyakkaoAcademy.jpg/revision/latest?cb=20190809132405) | 669×435 ✅ |
| Clan Momobami | árbol de las familias | [Clan.jpg](https://static.wikia.nocookie.net/kakegurui/images/a/a1/Clan.jpg/revision/latest?cb=20190206092249) | 1880×947 ✅ |

El consejo **no tiene logo propio** aparte del sello rojo de sus papeles;
no encontré un escudo de tela o metal ⚠️.

### H.4 Vocabulario que un fan reconoce

- **賭ケグルイ** (kakegurui): «loco por el juego»; el título mezcla kanji y
  katakana para que se vea más agresivo ✅.
- **家畜** (kachiku): mascota, el estatus de los últimos.
- **ポチ / ミケ** (Pochi / Mike): sus motes de perro y gata; en inglés,
  «Fido» y «Mittens» ✅.
- **生徒会** (el consejo) y **公式戦** (combate oficial, el único derecho de
  una mascota) ✅.
- **人生計画表**: el plan de vida ✅.
- **百喰一族**: el clan Momobami ✅.
- **顔芸** (kaogei): la cara exagerada; la palabra que hay que usar con una
  IA de imagen (§18) ✅.
- **オールイン** (all in) y **los 100 votos**: la elección de ××.

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

Actualizado tras la segunda pasada. Lo resuelto se tacha.

- **La lista real de comandos** del canal: no está en el inventario.
- ~~Ninguna imagen~~ → hay **11 hojas de contacto** (3 en `hojas/`, §3.0)
  y 2 episodios y el tráiler mirados (§2.0).
- ~~Voces latinas de Kirari, Ririka, Midari, Sayaka, Runa y el director~~
  → resueltas con dos páginas de Doblaje Wiki cada una (§10).
- **La frase latina de «賭け狂いましょう»**: Whisper oye «¡Comencemos esta
  locura!» (1×01, 12:39), pero otro modelo oyó otra cosa: **falta
  confirmarla de oído** ⚠️ (§10).
- ~~El orden 2.º a 5.º de la encuesta~~ → lo cuenta el autor en un
  podcast, traducido por un fan: Mary 1.ª ✅; Kirari 2.ª y Yumeko 5.ª ⚠️ (§9).
- ~~Los colores de cada personaje~~ → medidos en arte oficial y en
  fotogramas (§5, §16, §17).
- **La letra del logo** ⚠️ (§6).
- **El aspecto real del tablón** y de las interfaces de los dos juegos ⚠️
  (§13). La placa de mascota ya tiene imagen (§H).
- **El opening y el ending de ××**: un solo resumen ⚠️ (§11).
- **Los minutos de los vídeos** de YouTube y TikTok: YouTube pidió sesión
  y TikTok bloquea `yt-dlp` ⚠️ (§12.2, §E.3).
- **Las citas de la T2 (××)**: minutos del subtítulo de la primera pasada,
  sin volver a comprobar ⚠️. El doblaje de ×× está en Internet Archive sin
  mirar.
- **Vídeo en 1080p**: lo mirado es 853×480. La misma colección de Internet
  Archive trae **MKV 1280×720** de cada episodio: es la vía para capturas.
- **Qué música suena** en las escenas fuertes ⚠️ (§D).
- **Manos y cartas en 3DCG**: sólo un resumen de la entrevista de Natalie ⚠️ (§A).
- **Programas del estudio** y **escudo del colegio**: no encontrados ⚠️
  (§A, §B).
- **Ririka con la cara visible** en vídeo: no se vio ⚠️ (§8.1).

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
