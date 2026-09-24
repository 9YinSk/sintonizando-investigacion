---
tags: [biblia, serie, laminas]
serie: "【推しの子】 Oshi no Ko"
canales: ["#redes-y-novedades", "#en-directo", "#castings"]
fecha: 2026-09-24
---

# Biblia · Oshi no Ko — para #redes-y-novedades, #en-directo y #castings

> [!important] Cómo se hizo esta investigación (léelo primero)
> **Dos pasadas.**
> - **Segunda pasada, 24-sep-2026, con la red abierta.** Se pudo usar:
>   la **wiki de Fandom** (`oshinoko.fandom.com`) por su API, con dos
>   tandas de `investigar_serie.py` (**979 imágenes, 21 hojas**, y otra de
>   sitios y episodios), **miradas**; 3 hojas propias en `hojas/` (§3.0);
>   **Doblaje Wiki** por su API, **ANMTV** y la **API de noticias de
>   Crunchyroll** (reparto y staff latino); **YouTube** con yt-dlp
>   (bajar el vídeo pide «iniciar sesión», así que se miraron los
>   *storyboards*, un cuadro por segundo); Sketchfab por su API;
>   fontTools; Arctic Shift (Reddit). El detalle, en la bitácora (§21).
> - **La segunda pasada se hizo en dos tandas** (el límite de uso cortó
>   la primera). En la segunda tanda: `herramientas/fotogramas.py`
>   volvió a fallar («Sign in to confirm you're not a bot», 4 clientes
>   de yt-dlp probados), así que se miraron por *storyboard* 7 vídeos
>   oficiales más (Akane y la visita al estudio de doblaje, §10 y §14);
>   **`referencias.json` rehecho** (40 entradas, 34 medidas por la API
>   de la wiki o bajando la imagen); **Crunchyroll News en español** por
>   su API (entrevista al director y artículo de los ojos); Anime Corner,
>   ranking.net, Ruliweb y ANMTV abiertos de verdad; los subtítulos
>   japoneses de la emisión para dar minuto a las frases del doblaje.
> - **Primera pasada (misma fecha, red cerrada).**
> La red del contenedor estaba cerrada: Fandom, Doblaje Wiki, Wikipedia,
> YouTube, Crunchyroll, ANMTV, Sketchfab, Pixiv, X y la web oficial daban
> error 403. Se usó el buscador web (47 búsquedas, en español,
> inglés, japonés, coreano y chino) y GitHub, que sí responde.
> Por GitHub se abrieron de verdad cuatro cosas muy útiles:
> - **Los subtítulos japoneses de la temporada 1** (repositorio
>   *NanakoRaws*, archivos .ass/.srt de la emisión de TV). Dan el
>   **minuto exacto** de cada frase. Se leyeron los 11 episodios.
> - **Las fichas de Anime News Network** (copia en GitHub) de las cuatro
>   temporadas: staff, reparto japonés, inglés y **español**, openings,
>   endings, canciones de B小町 y títulos de episodio.
> - **20 ilustraciones de B小町** guardadas en una extensión de navegador
>   de fans. Una lleva el copyright oficial. Se miraron todas y se
>   **midieron colores** en ellas.
> - **Las letras de Google Fonts**: se bajaron los archivos y se comprobó
>   letra por letra que traen á é í ó ú ñ ¿ ¡ y los corchetes 【 】.
>
> En la primera pasada no hubo hojas de contacto; ahora sí (§3.0).
> ✅ = confirmado en dos fuentes (o un archivo que abrí o medí).
> ⚠️ = dudoso o una sola fuente.
> «hoja P·7» = número 7 de `hojas/personajes_01.jpg`; «O·3» =
> `hojas/objetos_01.jpg`; «V·5» = `hojas/video_01.jpg` (fotogramas).
>
> **Ojo con el wiki:** el encargo sugería `oshi-no-ko.fandom.com`, que
> da **404**. El bueno es **`oshinoko.fandom.com`** ✅ (comprobado por su
> API: 428 artículos, 2963 imágenes).

## Segunda pasada · qué cambió

**Corregido (antes → ahora)**
- **Wiki:** `oshi-no-ko.fandom.com` (404) → **`oshinoko.fandom.com`** ✅.
- **Letra del logo:** «gótica muy gruesa» → **mincho** con la «の»
  magenta `#E70082` y una estrella de seis puntas dentro (O·22, V·7) ✅.
- **Magda Giner:** «es del doblaje de España, no usar» → **es del
  latino**: la madre de Gotanda (Doblaje Wiki + ANMTV + ANN) ✅.
- **Nobuyuki Kumano:** Armando Ibarrola (ANN) → **Armando Corona**
  (Doblaje Wiki + ANMTV) ✅.
- **T3:** el ep. 29 no es «Casting» → **«営業» (Marketing)**; en el
  ep. 34 no elige Gotanda → **Ruby, Akane y Frill se prueban entre
  ellas** (wiki) ✅.
- **`bg20`:** «trajes de San Valentín» → **trajes de «POP IN 2»**
  (renders oficiales P·11, 15, 19) ✅.
- **Key visual de Ai del proyecto de fans:** «origen dudoso» → **oficial**
  (*Season 1 Key Visual 2*, mismo tamaño, P·1) ✅.
- **Modelos de *plaggy* en Sketchfab:** «CC0» (por el título) → **CC BY**
  (API de Sketchfab): hay que dar crédito ✅.
- **Estrellas:** «nunca cinco puntas» → **ojo = seis; cartelas y
  adornos = cinco** redondeadas (O·19-21) ✅.
- **Pelo de MEM:** «limón» → **rubio miel `#E2A144`** en los renders;
  limón sólo bajo los focos ✅.
- **Encuesta de Ruliweb:** «sondeo coreano de 20.000 votos, Kana 5.ª» →
  el post (5-oct-2023) **copia el ranking japonés de ranking.net**, donde
  Kana era **6.ª**. Hoy (24-sep-2026) ranking.net la pone **4.ª por nota
  y 1.ª en número de votos** (5.590) ✅.
- **«Blogs japoneses: Kana sube al primer puesto»** → sólo lo dice
  **カイの漫画考察** (22-sep-2026); en ranking.net es 4.ª ✅.
- **Parejas de Anime Corner:** «resumen confuso» → **Aqua × Kana 12,9 %,
  Aqua × Akane 12,38 %** (página abierta) ✅.
- **Frases del doblaje latino:** sin minuto → **ep. 2 · 20:23** y **ep. 4
  · 19:52** (cruzadas con los subtítulos japoneses de la emisión) ✅.
- **Los tres conceptos:** el «post» inventado (A), las カンペ inventadas
  (B) y la hoja sin sitio (C) → **formatos oficiales vistos**: el
  directo de MEM y su noticiero (A), el cartón oficial «ON AIR» y la
  pizarra de MEM (B), la puerta de Ichigo Pro con la cartela de
  estrella (C).

**Añadido**
- **3 hojas de contacto** propias (§3.0): 27 personajes, 25 objetos y
  sitios, 26 fotogramas de vídeo, todos con tamaño o minuto.
- **`referencias.json` rehecho:** antes 38 entradas, 22 sin tamaño y 16
  que eran páginas (y 3 vídeos sin minuto); ahora **40**, todas la imagen misma o el vídeo con
  `&t=`, **34 con ancho y alto medidos** (las 6 de vídeo no se pueden
  medir: sólo hay *storyboard* de 320×180).
- **Minutos y `&t=`** de opening, ending, tráiler y 6 clips (§4.1, §15), y de
  7 vídeos oficiales más en la segunda tanda (§10, §14).
- **Reparto latino completo** con dos o tres fuentes (Doblaje Wiki,
  ANMTV, API de noticias de Crunchyroll) y el staff (adaptación, mezcla,
  producción) (§12).
- **Cuadros de diálogo oficiales** (§8.1): el directo de MEM, el
  noticiero «最新», los cartones de cuenta atrás, las cartelas de
  estrella, la caja de *IDOLM@STER Shiny Colors* y el «mensaje especial».
- **Poses:** Akane pasa de 5 a 11 y Ai de 6 a 7 (§10).
- **Licencias de 15 modelos 3D** por la API de Sketchfab (§5.1) y **7
  letras más** comprobadas con fontTools (§7).
- Tabla **«Cumplimiento del encargo»** (antes de la bitácora).

**Marcas de duda (⚠️):** había **52**; quedan **29**, contadas
con `grep` (23 son datos dudosos; el resto son la leyenda,
este resumen y la tabla de cumplimiento). El porqué de cada una va a su
lado y resumido en §19.

> [!warning] Spoiler que condiciona todo
> Ai muere en el episodio 1. El manga terminó en noviembre de 2024 con la
> muerte de Aqua, y el final enfadó a mucha gente (punto 16). Las láminas
> **no deben tocar el final** ni jugar con la muerte de Ai. Son canales
> alegres del servidor: se usa la cara brillante de la serie (B小町, el
> plató, las redes), no la venganza.

---

## 1 · Los tres canales y lo que tiene que decir cada lámina

El encargo junta tres canales. Cada uno pide su lámina. Los tres
conceptos del final (punto 18) son **uno por canal**.

### 1.1 · #redes-y-novedades
**Canal:** `ıı・🔗・redes-y-novedades` (texto), categoría ✦ EMPIEZA AQUÍ ✦.
Texto real: *«Nuestras redes. Cada vídeo se avisa en novedades.»*
([inventario](../../servidor/inventario.md)).

**Función:** enseñar las redes del servidor y avisar de cada vídeo nuevo.
El inventario **no dice cuáles son las redes**. En la lámina van huecos
para ponerlas (YouTube, TikTok, Instagram… las que sean de verdad).
El dueño hace fandubs y clips para TikTok, Shorts y Reels
([proyectos](../../contexto/proyectos.md)).

| Pieza | Texto propuesto |
|---|---|
| Título | **NUESTRAS REDES** |
| MEM-cho | **¡Síguenos! Yo sé cómo se hace viral.** |
| Bloque 1 | Aquí están todas nuestras redes. |
| Bloque 2 | Cada vídeo nuevo se avisa aquí. |
| Bloque 3 (redes) | Una fila por red: icono, nombre y usuario (los reales) |
| Pie | Dale a seguir y no te pierdas nada. |

¿Por qué MEM-cho? Es YouTuber y tiktoker. En el episodio 7 presume: *«¿Sabes
qué día y a qué hora subirlo para sacar más retuits? Soy una profesional
de hacer virales»* (punto 4). En el 9 celebra *«¡10.000 suscriptores!»*.

### 1.2 · #en-directo
**Canal:** `ıı・🔴・en-directo` (texto), categoría ✦ EN VIVO ✦.
Texto real: *«¿Estás haciendo algo ahora? Dilo aquí y quien quiera se
mete a mirar.»*

**Función:** avisar de directos (de cualquiera del servidor).

| Pieza | Texto propuesto |
|---|---|
| Letrero | **ON AIR** (encendido en rojo) |
| Ruby (o Ai) | **¡Estamos en vivo! ¡Pasa a mirar!** |
| Bloque 1 | ¿Estás haciendo algo ahora? Dilo aquí. |
| Bloque 2 | Pon el enlace y qué estás haciendo. |
| Bloque 3 | Quien quiera, se mete a mirar. |

### 1.3 · #castings
**Canal:** `ıı・🎬・castings` (foro), categoría ✦ EL ESTUDIO ✦.
Texto real: *«Cada casting es un hilo. Ciérralo cuando el papel esté
cubierto.»* Hilos fijos: **«📌 Cómo se abre un casting (léeme)»** (1
mensaje) y **«EJEMPLO · Casting cerrado, para ver el formato»**.
En #general-doblaje se dice: *«Tu voz grabada va a demos; los papeles, a
castings.»*

**Etiquetas reales (15):** Anime, Videojuego, Serie, Película, Corto,
Comercial, Audiolibro, Pagado, Sin paga, Abierto, Cerrado, Urgente,
Oficial del servidor, Canto, +18.

**La ficha:** el inventario **no copia** el mensaje del hilo fijado. Abajo
va una ficha propuesta; hay que cotejarla con el hilo real antes de
rotular ⚠️.

| Pieza | Texto propuesto |
|---|---|
| Título | **HOJA DE AUDICIÓN** |
| Kana | **Un buen papel no se regala. ¡Se gana!** |
| Paso 1 | Un casting, un hilo. |
| Paso 2 | Rellena la ficha: proyecto, personaje, tipo de voz, líneas de prueba, fecha límite, pago. |
| Paso 3 | Ponle etiquetas: formato, pago y estado. |
| Paso 4 | Cuando el papel esté cubierto, ciérralo. |

**Lámina 2 de #castings (si la primera se llena):** las 15 etiquetas en
tres grupos, como los sellos de una hoja de audición:
- **Formato:** Anime, Videojuego, Serie, Película, Corto, Comercial,
  Audiolibro, Canto.
- **Pago:** Pagado, Sin paga.
- **Estado:** Abierto, Cerrado, Urgente, Oficial del servidor, +18.

Los textos no llevan «·», «—» ni paréntesis de relleno. Cada uno va en
su propio sitio del objeto (pantalla, letrero, casilla de la hoja).

---
## 2 · ¿Quién es el más querido?

**Respuesta corta: Kana Arima** ✅ (lo dicen a la vez Anime Corner, la
prensa china, blogs japoneses y CBR). Ai es el icono (la cara de la
serie y la 1.ª en ranking.net por nota), pero en 2026 la más votada y
comentada es Kana: en ranking.net es la que más gente puntúa (5.590).

**No hay encuesta oficial de personajes** ⚠️. Un artículo de enero de 2026
dice que la editorial no ha hecho ninguna. Lo oficial fue el
«推しデミー賞» (premio a la mejor escena de actuación)
([ABEMA Times](https://times.abema.tv/articles/-/10128876)).
La revista Young Jump sí tiene una página propia para animar a Kana:
«#有馬かな元気かな» ([Young Jump](https://youngjump.jp/manga/oshinoko/genkikana/)).

| Encuesta | Resultado | Estado |
|---|---|---|
| Anime Corner, invierno 2026 (45.490 votantes en total) | **Oshi no Ko T3, anime de la temporada n.º 1** ([ranking](https://animecorner.me/winter-2026-anime-of-the-season-rankings/)) | ✅ página abierta (2.ª pasada) |
| Anime Corner, seiyū de la temporada (más de 24.000 votos) | **Megumi Han (Kana) 1.ª, con el 10,08 %**, «por su actuación emotiva como Kana» ([ranking](https://animecorner.me/winter-2026-seiyuu-of-the-season-rankings/)) | ✅ página abierta |
| Anime Corner, parejas (6.310 votos) | **Aqua × Kana 1.ª (12,9 %)**, Aqua × Akane 2.ª (12,38 %) (misma página que el anime de la temporada) | ✅ página abierta (antes «resumen confuso») |
| Encuesta semanal china, invierno 2026 | **Kana, 1.ª chica más popular** varias semanas; Ruby 4.ª ([Sina](https://www.sina.cn/news/detail/5265276628376440.html)) | ⚠️ (una fuente; sina.cn bloqueado por el proxy en la segunda pasada) |
| Blog japonés カイの漫画考察 (22-sep-2026) | **Kana 1.ª** («首位に躍り出たのは… 有馬かな») ([blog](https://manga-comic-netabare.com/archives/61568/oshinoko-character-ranking-arima-kana/)) | ✅ página abierta |
| みんなのランキング (ranking.net, 24-sep-2026) | Ai 1.ª (92,5), Ruby 2.ª, Aqua 3.º, **Kana 4.ª (81,1) pero la que más gente votó: 5.590**; MEM 5.ª, Akane 8.ª ([ranking](https://ranking.net/rankings/best-oshinoko-characters)) | ✅ página abierta (**corregido**: no pone a Kana 1.ª) |
| Prensa en inglés | «La favorita del fandom por mucho» ([CBR](https://www.cbr.com/oshi-no-ko-kana-arima-popularity-explained/), [CBR 2](https://www.cbr.com/crunchyroll-oshi-no-ko-kana-arima-anime-best-girl/)); «el personaje mejor escrito» ([Anime Corner](https://animecorner.me/oshi-no-ko-episode-10-kana-arima-is-the-best-written-character-in-the-series/)) | ✅ |
| Ranker (fans de EE. UU.) | Akane, Ruby, Ai en el podio ([Ranker](https://www.ranker.com/list/best-oshi-no-ko-characters/rowan-blake)) | ⚠️ (Ranker responde 401 en la segunda pasada; no lo pude abrir) |
| Ruliweb (Corea, 5-oct-2023) | **No es un sondeo coreano:** el post copia ranking.net de 2023 («출처: ranking.net»): Ai, Ruby, Aqua, Miyako, Minami, **Kana 6.ª**, Akane 7.ª, MEM 8.ª ([Ruliweb](https://bbs.ruliweb.com/community/board/300143/read/63270152)) | ✅ página abierta (**corregido**: decía «Kana 5.ª») |

**Qué significa para las láminas:**
- **Kana** (la más querida) va en **#castings**: toda su historia es
  actuar, hacer pruebas y pelear papeles.
- **MEM-cho** (secundaria muy querida, YouTuber) va en
  **#redes-y-novedades**.
- **Ruby** con **Ai** en pantalla van en **#en-directo**: el escenario
  y la tele en vivo.
- Aqua casi no sirve: es frío y su historia es la venganza. Puede salir
  de fondo, nunca de anfitrión alegre.

---

## 3 · Arte oficial reunido (poses vivas, no hojas de modelo)

### 3.0 · Las hojas de contacto (segunda pasada) ✅

Corrí `investigar_serie.py` dos veces sobre `oshinoko.fandom.com`:
- `herramientas/referencias/oshi-no-ko/`: 11 páginas (Ai, Aqua, Ruby,
  Kana, Akane, MEM-cho, B-Komachi, Gotanda, Pieyon, Miyako, Frill) y
  sus galerías: **979 imágenes, 21 hojas**.
- `herramientas/referencias/oshi-no-ko-sitios/`: 22 páginas (material
  promocional, Ichigo Production, Yōtō, Lalalai, el reality, episodios
  1, 5, 9, 11, 29 y 34, canciones): **531 imágenes, 12 hojas**.

**Las miré.** Hay mucho oficial que no se conocía: cartones de cuenta
atrás con **«ON AIR»**, cartelas de episodio, avisos de hitos del canal
(«100.820 suscriptores»), dibujos de animadores con **«本日ON AIR»**
(«hoy ON AIR»), renders de cuerpo entero sobre verde (recortables) y
cajas de diálogo del juego *IDOLM@STER Shiny Colors*. Mucho otro no
sirve: unas 150 son **genga y storyboards** a lápiz (fondo amarillo o
verde) y unas 60 son **viñetas del manga** en blanco y negro.

Monté **3 hojas propias** con Pillow (en `hojas/`). En cada celda va el
tamaño real (API de la wiki) y, en la de vídeo, el minuto. Los vídeos se
miraron por sus *storyboards* de YouTube (un cuadro por segundo, ±1 s):
bajar el vídeo daba «Sign in to confirm you're not a bot».

**`hojas/personajes_01.jpg`** (P·)

| N.º | Qué es | Tamaño | Para qué | Original |
|---|---|---|---|---|
| 1 | Ai KV T1-2: guiño y micro | 2152×3044 | **Ai en directo**: guiño, micro, dedo a cámara → monitor del concepto B | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/e/e0/Season_1_Key_Visual_2.png) |
| 2 | Ai KV T1: de espaldas | 2500×3535 | Ai de espaldas ante el público: portada, luz de escenario | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/5/5f/Season_1_Key_Visual.png) |
| 3 | Ai señala (staff) | 1510×952 | Ai señalando a cámara (dibujo de animador): «¡mira aquí!» | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/d/dc/Idol_Ai_by_urkbil126.jpg) |
| 4 | Ai render idol | 656×1584 | Ai de cuerpo entero, traje idol: recorte limpio | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/4/40/AiRender2.png) |
| 5 | B-Komachi Newtype 2023-08 | 6080×4097 | **B小町 con el uniforme rojo**, Kana al centro con micro | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/2/27/Newtype_2023_08_Poster.jpg) |
| 6 | B-Komachi KV T1-5 escenario | 2000×2828 | Las tres en el escenario con focos: fondo de #en-directo | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/d/d3/Season_1_Key_Visual_5.png) |
| 7 | Kana render uniforme | 1600×4057 | Kana de uniforme, cuerpo entero: recorte | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/e/ee/Kana_Arima_Anime.png) |
| 8 | Kana boina, V (staff) | 2000×3000 | Kana con boina y «V»: saludar | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/b/b1/Kana_Ep6_by_bunyamadesu.jpg) |
| 9 | Kana índice arriba (staff) | 1446×2048 | **Kana con el índice arriba**: explicar (concepto C) | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/f/f3/Kana_Episode_5_by_makitamikan.jpg) |
| 10 | Kana señala (staff) | 1510×952 | **Kana señalando a cámara**: animar | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/0/00/Kana_Episode_11_by_urkbil126.jpg) |
| 11 | Kana render POP IN 2 | 800×1479 | Kana traje «POP IN 2» (boina blanca, lunares): recorte | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/5/58/Kana_Arima_Anime-POP_IN_2.png) |
| 12 | Kana BD vol. 4 | 1906×2382 | Kana sentada, sudadera: tono tranquilo | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/a/ad/Volume_4_BD%26DVD.png) |
| 13 | MEM BD vol. 6 | 1906×2382 | **MEM sentada con su nombre gigante detrás**: diseño de cabecera | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/f/f8/Volume_6_BD%26DVD.png) |
| 14 | MEM verificada (Mengo) | 1804×2362 | **MEM con insignias de «verificada»** (Mengo): #redes | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/7/7a/MEMVerifiedbyMengo.jpg) |
| 15 | MEM render POP IN 2 | 800×1479 | MEM traje «POP IN 2»: recorte | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/7/74/Mem-Cho_Anime-POP_IN_2.png) |
| 16 | MEM render uniforme | 592×1712 | MEM de uniforme: recorte | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/b/b0/MemchoRender.png) |
| 17 | Ruby idol, manos a cámara | 2000×2048 | Ruby con las dos manos a cámara y guiño: invitar | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/9/96/Idol_Ruby_by_pi_ro_ri.jpg) |
| 18 | Ruby corazón (pose de Ai) | 1884×2048 | Ruby corazón con las manos: celebrar | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/9/98/Ruby_recreating_the_pose_of_Ai.png) |
| 19 | Ruby render POP IN 2 | 800×1479 | Ruby traje «POP IN 2»: recorte | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/b/bf/Ruby_Hoshino_Anime-POP_IN_2.png) |
| 20 | Ruby KV T3-4 plató | 1920×2715 | **Ruby en un plató con croma y cámaras**: #en-directo / #castings | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/b/b1/Season_3_Key_Visual_4.png) |
| 21 | Akane ojos de estrella ep7 | 2560×1440 | Akane con estrellas en los ojos: actriz genio | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/2/2f/Ep_7_Akane_Captivating_Eyes.png) |
| 22 | Akane render | 600×1550 | Akane cuerpo entero | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/6/63/Akane_Kurokawa_Anime.png) |
| 23 | Aqua render | 600×1629 | Aqua cuerpo entero (uniforme) | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/d/d1/Aqua_Hoshino_Anime.png) |
| 24 | Gotanda diseño | 472×1189 | **Gotanda**: pelo largo castaño, barba, chaqueta azul | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/3/3c/Taishi_Gotanda_Character_Design.png) |
| 25 | Pieyon render | 472×1191 | Pieyon: cuerpo de culturista, cabeza de pollito | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/8/83/PieyonRender.png) |
| 26 | Miyako render | 445×1263 | Miyako: pelo rosado, vestido granate y rebeca | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/4/4b/MiyakoRender.png) |
| 27 | Akane imita a Ai (Mengo) | 1880×2074 | Akane imitando la «V» de Ai | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/7/7e/ActorAkanebyMengo.jpg) |

**`hojas/objetos_01.jpg`** (O·)

| N.º | Qué es | Tamaño | Para qué | Original |
|---|---|---|---|---|
| 1 | Cartón «hoy ON AIR» (Ai) | 1440×1080 | **Cartón oficial «hoy se estrena» con «ON AIR»**: modelo del concepto B | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/6/6b/%F0%9F%8C%9FToday%27s_broadcast_of_the_%F0%9F%8C%9F.png) |
| 2 | Cartón «faltan 8 días» | 1440×1080 | Cartón «faltan 8 días»: pizarra blanca, firma, franja negra | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/4/49/%F0%9F%8C%9F_8_days_left_until_the_broadcast_%F0%9F%8C%9F.png) |
| 3 | Cartón «faltan 3» (Kana) | 1440×1080 | Cartón «faltan 3 días» (Kana, firma de Megumi Han) | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/3/33/%F0%9F%8C%9F_3_days_left_until_the_broadcast_%F0%9F%8C%9F.png) |
| 4 | Cartón «faltan 5» (MEM) | 1440×1080 | Cartón «faltan 5 días» (MEM) | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/5/51/%F0%9F%8C%9F_5_days_left_until_the_broadcast_%F0%9F%8C%9F.png) |
| 5 | Pizarra MEM «entrevista en vivo» | 2048×1536 | **Pizarra de MEM «entrevista EN VIVO»**, a rotulador: #en-directo | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/f/f8/%F0%9F%9A%A8The_TV_anime_that_will_be_live_just_before_the_emergency_%F0%9F%9A%A8.png) |
| 6 | 100.820 suscriptores (MEM) | 1080×1885 | **MEM celebra 100.820 suscriptores** del canal oficial: #redes | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/4/47/%F0%9F%8C%9FOver_100%2C000_Subscribers_%F0%9F%8C%9F.png) |
| 7 | 300.000 seguidores en X | 828×683 | 300.000 seguidores en X, con Ai: #redes | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/4/4c/%F0%9F%8C%9FOver_300%2C000_followers_%F0%9F%8C%9F.png) |
| 8 | «Ep5 hoy ON AIR» (staff) | 1920×1082 | «Ep. 5, hoy ON AIR» a mano (animador): #en-directo | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/b/b5/Akane_Ep5_by_naota0048.png) |
| 9 | «Ep3 hoy ON AIR» (staff) | 1536×864 | «Ep. 3, hoy ON AIR» con Kana boceto: #en-directo | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/c/c2/Kana_Episode_3_by_naota0048.png) |
| 10 | Caja de diálogo IM@S: Kana | 1922×1079 | **Caja de diálogo de videojuego** (IDOLM@STER Shiny Colors) con Kana | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/2/28/Kana_x_IDOLM%40STER.jpg) |
| 11 | Caja de diálogo IM@S: Ruby | 1915×1079 | Caja de diálogo del mismo juego con Ruby | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/f/fa/Ruby_x_IDOLM%40STER.jpg) |
| 12 | Informe de doblaje (afureco) | 2000×1125 | **«Informe de doblaje»** con la actriz de Ruby en la cabina | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/2/21/%F0%9F%8E%99Post-recording_report_%F0%9F%8E%99.png) |
| 13 | Periódico DAILY NEWS: Kana | 2897×4096 | **Periódico sensacionalista** sobre Kana: #redes-y-novedades | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/2/2f/DAILYNEWS_Extra.png) |
| 14 | «Bicarbonato-chan» anuncio | 2897×4096 | Anuncio de «Bicarbonato-chan» (Kana): humor | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/6/6e/%22Baking_Soda-chan%22.png) |
| 15 | Kana con el móvil ep11 | 1920×1080 | **Kana enseña el móvil** con un post: #redes | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/e/eb/Arima_Kana_Episode_11._2.jpg) |
| 16 | Cuarto con aros de luz ep21 | 1920×1080 | Cuarto con dos aros de luz, micro y pantallas: set de directo | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/7/79/Ep_21_B-Komachi_do_a_tour_of_Kana%27s_room.png) |
| 17 | Claqueta «Actors×Job» | 960×960 | Claqueta «Actors × Job»: #castings | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/6/64/Oshi_no_Ko_x_Taito_Toys_%28Actors_x_Job%29.png) |
| 18 | Kana con guion (T2) | 1200×675 | **Kana con un guion en la mano**: #castings | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/7/7d/Episode_15_Teaser_4.png) |
| 19 | Cartela ep11 «Idol» | 1920×1080 | **Cartela de episodio**: estrella negra sobre rombos rojos: marco de título | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/c/c3/Episode_11_Title_Card.png) |
| 20 | Cartela ep5 | 1920×1080 | La misma cartela en cian | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/6/64/Episode_5_Title_Card.png) |
| 21 | Cartela ep9 «B-Komachi» | 1920×1080 | La misma cartela en violeta | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/9/90/Episode_9_Title_Card.png) |
| 22 | Cartela ep1: logo | 1920×1080 | Logo 【推しの子】 en blanco: medir la letra | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/6/63/Episode_1_Title_Card.png) |
| 23 | Puerta «Ichigo Pro · Saitō» | 1920×1080 | **Placa «(株)苺プロ 斉藤» en la puerta**: sitio de #castings | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/8/83/Ichigo_Productions_Anime.png) |
| 24 | Sala de ensayo Lalalai | 1920×1080 | Sala de ensayo de Lalalai: sitio de pruebas | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/0/04/Lala_Lai_Theatrical_Company_Anime.png) |
| 25 | Instituto Yōtō | 1920×1080 | Instituto Yōtō por fuera | [enlace](https://static.wikia.nocookie.net/oshi_no_ko/images/9/9d/Youtou_High_Anime.png) |

**`hojas/video_01.jpg`** (V·)

| N.º | Qué es | Minuto · tamaño | Para qué | Enlace |
|---|---|---|---|---|
| 1 | OP T1 · ojo de Ruby | 0:03 · 320×180 | Estrella de seis puntas en el ojo | [vídeo](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=2) |
| 2 | OP T1 · Ruby «shh» | 0:25 · 320×180 | **Ruby «shh»**, dedo en los labios, estrella: secreto, pedir silencio | [vídeo](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=25) |
| 3 | OP T1 · buscador | 0:30 · 320×180 | Parodia de buscador «I'm feeling good»: #redes | [vídeo](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=30) |
| 4 | OP T1 · MEM baila | 0:33 · 320×180 | **MEM bailando en una azotea**, brazos arriba: celebrar | [vídeo](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=33) |
| 5 | OP T1 · Kana boina | 0:35 · 320×180 | Kana con boina, mano en la mejilla: pensar | [vídeo](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=35) |
| 6 | OP T1 · Ai en escena | 0:57 · 320×180 | Ai con micro en escalera de luces rosa | [vídeo](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=56) |
| 7 | OP T1 · logo | 1:16 · 320×180 | Logo: letra con remate (mincho), «の» rosa con estrella | [vídeo](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=76) |
| 8 | ED T1 · Ruby magenta | 0:19 · 424×180 | Fondo plano magenta para Ruby | [vídeo](https://www.youtube.com/watch?v=0saw1cGIl1A&t=18) |
| 9 | ED T1 · MEM amarillo | 0:25 · 424×180 | Fondo plano amarillo para MEM | [vídeo](https://www.youtube.com/watch?v=0saw1cGIl1A&t=24) |
| 10 | ED T1 · Kana rojo | 0:27 · 424×180 | Fondo plano rojo para Kana | [vídeo](https://www.youtube.com/watch?v=0saw1cGIl1A&t=26) |
| 11 | Tráiler · lente y Kana | 0:37 · 320×180 | **Lente de cámara con Kana dentro**: #castings | [vídeo](https://www.youtube.com/watch?v=gKWEUJ4r5do&t=36) |
| 12 | Tráiler · Akane y guion | 0:40 · 320×180 | **Akane leyendo un guion rojo**: #castings | [vídeo](https://www.youtube.com/watch?v=gKWEUJ4r5do&t=40) |
| 13 | Tráiler · directo de MEM | 0:44 · 320×180 | **Directo de MEM con marco de neón**: #redes / #en-directo | [vídeo](https://www.youtube.com/watch?v=gKWEUJ4r5do&t=44) |
| 14 | Tráiler · «ON AIR» | 1:01 · 320×180 | «4月12日(水) ON AIR» en mincho sobre blanco | [vídeo](https://www.youtube.com/watch?v=gKWEUJ4r5do&t=61) |
| 15 | Ep11 · escenario JIF | 0:03 · 320×180 | Escenario al aire libre, barras amarillas | [vídeo](https://www.youtube.com/watch?v=S-UmqvA7uR8&t=2) |
| 16 | Ep11 · MEM apunta | 0:07 · 320×180 | MEM apunta con los dos índices | [vídeo](https://www.youtube.com/watch?v=S-UmqvA7uR8&t=6) |
| 17 | Ep11 · Kana índice | 0:08 · 320×180 | Kana apunta arriba con guante rosa | [vídeo](https://www.youtube.com/watch?v=S-UmqvA7uR8&t=7) |
| 18 | Ep11 · las tres | 0:27 · 320×180 | Las tres en fila: pose de grupo | [vídeo](https://www.youtube.com/watch?v=S-UmqvA7uR8&t=27) |
| 19 | Cuarto MEM · rótulo | 0:05 · 320×180 | **Rótulo naranja «MEMちょだよー!»** en su directo | [vídeo](https://www.youtube.com/watch?v=TvIOIATbUYE&t=4) |
| 20 | Cuarto MEM · mensaje | 1:29 · 320×180 | **Ventana blanca de mensaje de fan** («こんめむ〜♪») | [vídeo](https://www.youtube.com/watch?v=TvIOIATbUYE&t=88) |
| 21 | Noticias · «NEWS» | 0:00 · 320×180 | Cartón rosa «Next Corner >>> NEWS» | [vídeo](https://www.youtube.com/watch?v=VjyCYUdmlnc&t=0) |
| 22 | Noticias · rótulo «Saishin» | 0:03 · 320×180 | **Rótulo de noticias: círculo rojo «最新» + franja blanca** | [vídeo](https://www.youtube.com/watch?v=VjyCYUdmlnc&t=2) |
| 23 | Noticias · barras conejo | 0:44 · 320×180 | **Carta de ajuste con conejos**: «estamos en pausa» | [vídeo](https://www.youtube.com/watch?v=VjyCYUdmlnc&t=43) |
| 24 | Noticias · uchiwa de fan | 0:15 · 320×180 | Uchiwa en corazón «アイ 無限恒久永遠推し!» | [vídeo](https://www.youtube.com/watch?v=VjyCYUdmlnc&t=15) |
| 25 | Ep9 · «Piman Taisou» | 0:00 · 320×180 | Cartela infantil de «Piman Taisou» | [vídeo](https://www.youtube.com/watch?v=BPvD-dfIiEs&t=0) |
| 26 | Ep25 · Kana T3 | 0:19 · 320×180 | Kana con el traje de la T3 («Bのリベンジ») | [vídeo](https://www.youtube.com/watch?v=5B-ZPcq8KxQ&t=18) |

**Otras joyas de los índices** (no caben en las hojas):
- **Hojas de modelo oficiales** de Kana (trajes y caras,
  [2048×1306](https://static.wikia.nocookie.net/oshi_no_ko/images/a/a7/Kana_Arima_Concept_Art.jpg)),
  de Aqua y de Ai (índice personajes n.º 244, 246 y 558).
- **Cartones de cuenta atrás** de todo el reparto (n.º 519-523, 604,
  605): mismo diseño, cada uno con la firma de su seiyū.
- **«MEMちょの【推しの子】NEWS»** y **«MEMちょの部屋»**: MEM-cho presenta
  las novedades del anime en el canal oficial, como una streamer (§14).
- **Colaboración real de *IDOLM@STER Shiny Colors*** (2023-2024):
  tarjetas de Ruby, Kana, MEM y Akane (índice sitios n.º 191-192,
  226-233, 372-374, 413-419).
- **Juego real de escape (SCRAP)** «Escapa del escándalo tramado»:
  Aqua con una revista, Ruby con el móvil, un portátil con el directo
  de MEM (índice sitios n.º 214 y 340).
- **«Good Oshi Day»** (4 de noviembre): 16 dibujos del staff, entre
  ellos el director Daisuke Hiramaki y Kanna Hirayama (índice sitios
  n.º 236-259).
- **«47 prefecturas»**: un personaje por prefectura con su paisaje
  (índice sitios n.º 77-104 y 282-302). Buenos fondos con personaje.

### 3.1 · Imágenes de la primera pasada (bajadas de GitHub)
Vienen de una extensión de navegador de fans que guarda 20 ilustraciones
de B小町 en alta ([repositorio](https://github.com/jacobjuarezguerra/Oshi-No-Ko-Browser-extension-B-Komachi)).
La extensión **no dice de dónde salen**. Se revisaron una a una:

| N.º | Tamaño | Qué es | ¿Oficial? |
|---|---|---|---|
| `bg20` | 1920×1080 | Ruby, Kana y MEM de cuerpo entero, fondo de regalos y corazones. **Corrección:** no son «trajes de San Valentín»: son los **trajes de «POP IN 2»** (los mismos de los renders oficiales P·11, 15 y 19) | ✅ **lleva el copyright del comité** «©赤坂アカ×横槍メンゴ／集英社・【推しの子】製作委員会» |
| `bg19` | 3840×2160 | Las tres con el uniforme rojo del festival, láseres y focos. Kana en el centro señalando a cámara | ⚠️ estilo del anime, sin firma (el traje coincide con el del ep. 11, V·16-18) |
| `bg12` | 4096×2257 | Kana con micro señalando arriba, Ruby con la lengua fuera, MEM con cara «:3» y **Akane** de uniforme escolar detrás | ⚠️ estilo oficial, sin firma |
| `bg11` | 4096×2244 | Primer plano de Kana con texto «推しの子#11 よろしくお願い致します» | ⚠️ parece dibujo de staff para el episodio 11 |
| `bg4` | 4096×2883 | San Valentín: las tres tumbadas entre bombones | ⚠️ 4kwallpapers tiene uno de B小町 del mismo tamaño ([enlace](https://4kwallpapers.com/anime/oshi-no-ko-b-25258.html)) |
| `bg10` | 4096×2897 | Año Nuevo: las tres en kimono con sombrilla | ⚠️ |
| `bg7`, `bg18` | 2658×1718, 3857×2245 | Saltando (bg7) o cantando (bg18: Kana con micro señalando a cámara) con focos azules y verdes | ⚠️ |
| `bg1`, `bg3`, `bg13`–`bg16` | varios | Estilo distinto al del anime | parecen **fan art** |

Enlace directo a cada una:
`https://raw.githubusercontent.com/jacobjuarezguerra/Oshi-No-Ko-Browser-extension-B-Komachi/HEAD/bgN.jpg`
(cambiar N). Pesan de 0,5 a 22 MB: **no se suben al repositorio**.

**Segunda pasada, origen de las `bg` sin firma:** busqué su tamaño
exacto entre las **2963 imágenes de la wiki** (API, `list=allimages`):
ninguna coincide. 4kwallpapers tiene la de B小町 en **4096×2883** (el
tamaño de `bg4`) y la de Ai en **5263×3206**, pero **no nombra autor ni
fuente**. Por eso siguen marcadas como dudosas: estilo oficial, origen sin probar.
Para dibujar, mejor las oficiales de §3.0.

**Ai en el escenario** (key visual con micro, guiño y dedo apuntando a
cámara, 2152×3044), guardada en un proyecto de fans de una cinta de
casete 3D ([imagen](https://raw.githubusercontent.com/TheFabi8A/oshi-no-ko/HEAD/public/front-page/oshi-no-ko.webp),
[proyecto](https://github.com/TheFabi8A/oshi-no-ko)). **Segunda pasada:
es oficial ✅**, el *Season 1 Key Visual 2* de la wiki, mismo tamaño
(P·1, [original](https://static.wikia.nocookie.net/oshi_no_ko/images/e/e0/Season_1_Key_Visual_2.png)). En el mismo repositorio hay un fan art de Ai
firmado y su autógrafo (`back-page/ai.webp`, `firma.webp`).

### 3.2 · Arte oficial localizado en la primera pasada
En la segunda pasada casi todo esto está en la wiki: los visuales de la
T3 (*Season 3 Key Visual* 2-9, 1920×2715), las carátulas de los BD
(*Volume 1-6 BD&DVD*, 1906×2382; P·12 y P·13) y los pósteres (§3.0).
- **Web oficial, temporada 3**: nuevas ilustraciones de personajes
  ([noticia](https://ichigoproduction.com/Season3/news/index00540000.html)),
  **visual principal con Aqua y Ruby espalda con espalda** y PV 1
  ([noticia](https://ichigoproduction.com/Season3/news/index00570000.html)),
  segundo teaser ([noticia](https://ichigoproduction.com/Season3/news/index00450000.html)),
  **visual de fin de temporada** ([noticia](https://ichigoproduction.com/Season3/news/index01250000.html)).
- **Natalie**: anuncio de la T3 con Kamiki ([594182](https://natalie.mu/comic/news/594182)),
  visual principal de la T3 ([646883](https://natalie.mu/comic/news/646883)).
- **Animate Times**: teaser de la T3 ([nota](https://www.animatetimes.com/news/details.php?id=1742621823)),
  carátula del Blu-ray 1 de la T2 ([nota](https://www.animatetimes.com/news/details.php?id=1726645100)).
- **Carátulas de Blu-ray dibujadas por Kanna Hirayama** (diseñadora de
  personajes): la del BD 6 de la T2 trae a **Ruby y MEM-cho**
  ([X oficial](https://x.com/anime_oshinoko/status/1894673764849508395)),
  la del BD 3 ([X oficial](https://x.com/anime_oshinoko/status/1861696464491098451)),
  BD 1 de la T1 ([KADOKAWA](https://store.kadokawa.co.jp/shop/g/g302303003603/)).
- **Pósteres de cada temporada** en la ficha de ANN (T2 550×780, T3
  566×800) ([T2](https://cdn.animenewsnetwork.com/images/encyc/A28810-1387633428.1721856657.jpg),
  [T3](https://cdn.animenewsnetwork.com/images/encyc/A33662-2443054890.1767562958.jpg)).
- **Vídeos de Kanna Hirayama dibujando** a Kana
  ([YouTube](https://www.youtube.com/watch?v=q4bzYqoFGvo)) y a Ai
  ([YouTube](https://www.youtube.com/watch?v=CYxj4xCcGmI)). Son la mejor
  lección de línea y color que hay.
- **Manga**: tomo 1 en inglés ([Yen Press](https://yenpress.com/titles/9781975363178-oshi-no-ko-vol-1)),
  en español de Argentina ([Ivrea](https://www.ivrea.com.ar/titulo/oshi-no-ko/))
  y de México, con el subtítulo **«Mi idol favorita»**
  ([Whakoom, Panini México](https://www.whakoom.com/comics/dODF7/_oshi_no_ko__mi_idol_favorita/1)).
- **Juego oficial** *【推しの子】Puzzle Star* ([web](https://oshinoko-puzzle.com/),
  [App Store](https://apps.apple.com/jp/app/%E6%8E%A8%E3%81%97%E3%81%AE%E5%AD%90-puzzle-star/id6744346921)).

---

## 4 · Escenas icónicas con su minuto

**De dónde salen los minutos:** de los subtítulos japoneses de la emisión
de TV (NanakoRaws, [repositorio](https://github.com/kienkzz/NanakoRaws-Anime-Japanese-subtitles)).
En esa versión el **episodio 1 dura 81:52**. En Crunchyroll puede haber
±1 minuto de diferencia. Las frases son **traducción mía del japonés**,
no el doblaje latino.

| Ep. | Minuto | Qué pasa | Frase (japonés → español) | Sirve para |
|---|---|---|---|---|
| 1 | 00:02–00:30 | Voz de Goro sobre negro | «この世界において嘘は武器だ» → «En este mundo, la mentira es un arma» | tono general |
| 1 | 01:01–02:16 | Goro pone un DVD de Ai en el hospital; Sarina niña le enseña B小町 con «STAR☆T☆RAIN» de fondo | «やっぱ私の推しは～ アイ一択でしょ！» → «¡Mi *oshi* es Ai y punto!» | ser fan |
| 1 | 09:46 | Ai con Goro en el hospital | «嘘はとびきりの愛なんだよ？» → «La mentira es el amor más grande, ¿sabes?» | carácter de Ai |
| 1 | 18:00–18:03 | El presidente anuncia la vuelta de Ai **en un programa en directo** | «生放送だけど いけるよな？» «もちろん» → «Es en directo. ¿Puedes?» «Claro.» | **#en-directo** |
| 1 | 21:36–22:54 | Ai canta **«Sign wa B»** en el programa en directo «Nステ»; Aqua bebé la ve | «あなたのアイドル サインはB» | **#en-directo** (fotograma para una pantalla) |
| 1 | 22:58–23:17 | Ruby bebé despierta tarde: «¡Ya empezó *N-Sute*! ¿Por qué no me despertaste?», y luego chilla de fan | «『Nステ』もう始まってるじゃん！」「ママかわいすぎ～！» | **#en-directo** |
| 1 | 23:34 | Ruby insiste | «生放送はリアタイに意味あるってのに» → «¡Un directo tiene gracia verlo en vivo!» | **#en-directo** (la idea del canal) |
| 1 | 38:52–39:17 | Los gemelos bailan con barras de luz en el concierto; el vídeo se hace viral | «21万リツイート… 転載動画も200万再生» → «210.000 retuits… y 2 millones de vistas» | **#redes-y-novedades** |
| 1 | 42:37–42:41 | Aqua bebé habla como un adulto; Gotanda alucina | «ユーチューブで少々…» «すげえなユーチューブって！時代だなあ～！» → «Un poco de YouTube…» «¡Qué época!» (meme) | redes, humor |
| 1 | 43:15–43:48 | Gotanda explica los **tres tipos de actor** en un reparto | «役者ってのは3つある» → «Hay tres clases de actores» | **#castings** |
| 1 | 47:26–47:56 | Gotanda explica **cómo se decide un casting** en Japón | «日本の場合 キャスティングってのは 上のほうであらかた決まってる» | **#castings** |
| 1 | 48:24 | Gotanda: «a esto se le llama *bāter*» (un actor a cambio de otro) | «これを業界ではバーターっつうんだ» | #castings |
| 1 | 49:29–49:41 | **Aparece Kana niña.** Ruby: «¿La niña que lame bicarbonato?» Kana: «¡La niña genio que llora en 10 segundos!» | «重曹を舐める天才子役？» «10秒で泣ける天才子役！» | **Kana, #castings** |
| 1 | 61:57 | Ai: «Ya paso del millón de seguidores» | «フォロワーも100万人を超えた» | redes |
| 1 | 62:30 | «¡La semana que viene, el Domo!» | «いよいよ来週はドームだ～！» | escenario |
| 2 | 02:12–02:34 | Ruby espera el resultado de su **audición de idol** | «このオーディションを2年も待ち続けてきた» | #castings |
| 3 | 16:34–16:57 | **Kana explica cómo se rueda un drama** (ensayo, cámara, pasada) | «ドラマってのは…» | Kana explicando |
| 5 | 08:09 | **MEM-cho se presenta**: «¡Soy MEM-cho, de 3.º! Transmito en YouTube» | «高3のMEMちょです。ユーチューブで配信してます！» | **#redes** |
| 6 | todo | Acoso en redes a Akane | — | 🚫 **no usar** (punto 16) |
| 7 | 11:14–11:30 | **MEM-cho: «Soy una profesional de hacer virales»** | «何曜日の何時にアップするのが一番リツイート数稼げて…バズらせのプロなんだけどぉ？» | **#redes** (la frase clave) |
| 7 | 16:23 | El vídeo de Aqua llega a 74.000 retuits en 24 horas | «7万4,000リツイートを達成» | #redes |
| 8 | 02:09–02:20 | Akane vuelve **imitando a Ai**; Aqua la mira como a un fantasma | «あかね～！おかえり！» | Akane |
| 9 | 01:55–01:58 | Miyako lee las cifras de MEM: 370.000 suscriptores en YouTube, 638.000 en TikTok | «チャンネル登録者数37万人。ティックトックフォロワー数63万8千人» | **#redes** |
| 9 | 04:21–05:01 | MEM cuenta que dejó las audiciones: «todas pedían chicas de hasta 20 años» | «応募要項には満20歳までの女子って» | #castings (contexto) |
| 9 | 09:42–09:51 | **«¡10.000 suscriptores!»** «¡Ahora sí parece oficial!» | «登録者1万人！」「なんか公式って感じ！» | **#redes** |
| 9 | 18:07 | Kana canta «Piman Taisou» (su canción de niña) | «ピーマン体操 はじまるよ～！» | Kana, humor |
| 10 | 05:09–05:57 | Pieyon entrena a B小町: «¡10 cuestas más!» | «坂道ダッシュあと10本！» | ensayo |
| 11 | 03:34–03:53 | Kana ve los colores de las barras de luz: «Si da igual, blanco» | «何でもいいなら白» | colores del grupo |
| 11 | 04:15–05:32 | B小町 canta «STAR☆T☆RAIN» con el público: «We! are! STAR T RAIN / Check! Now!» | (canción) | **#en-directo** |
| 11 | 06:19 | Ruby anuncia la canción: «¡Sign wa B!» | «“サインはB”！» | #en-directo |
| 11 | 07:41–07:49 | **Kana ve a Aqua con la barra blanca**: «¡Voy a teñir tu barra de blanco! ¡Seré tu *oshi no ko*!» | «あんたのサイリウムを真っ白に染め上げてやる！」「あんたの推しの子になってやる！» | **la escena de Kana más querida** |

**Temporada 3.** No se le ponen minutos: ninguna escena de la T3 entra
en las láminas (es la parte oscura). Si hicieran falta, **sí hay
subtítulos de la T3 en GitHub** (en indonesio, de Limenime:
`limedriveku/limesub`, carpeta `Winter2026/Oshi no Ko Season 3`),
hallados en la segunda pasada y no usados.
**Corregido en la segunda pasada** (texto de la wiki por su API):
- El **ep. 29** no se llama «Casting»: es **«営業» (*Eigyō*, «Marketing»)**,
  emitido el 11-feb-2026 ([wiki](https://oshinoko.fandom.com/wiki/Episode_29)).
- El **ep. 34** es **«個人間オーディション» («Audición entre ellas»;
  en el canal oficial, *Private Audition*)**, 18-mar-2026. No es Gotanda
  quien elige: **Ruby, Akane y Frill se prueban entre ellas** hasta la
  noche por el papel de Ai en *La mentira de 15 años*, y Ruby gana. Es
  un episodio oscuro (Ruby habla de morir): **no usar** en la lámina
  ([wiki](https://oshinoko.fandom.com/wiki/Episode_34),
  [avance oficial](https://www.youtube.com/watch?v=POxdm79d23c),
  [epílogo oficial](https://www.youtube.com/watch?v=PYhvvBwIhIo)).

### 4.1 · Minutos comprobados en clips oficiales (segunda pasada) ✅
Miré estos vídeos del canal oficial por sus *storyboards* (±1 s). Los
números V· son de `hojas/video_01.jpg`.

| Vídeo | Minuto | Qué se ve | Sirve para |
|---|---|---|---|
| [Opening T1, «Idol»](https://www.youtube.com/watch?v=PgBvV9ofjmA) | [0:01-0:04](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=1) | ojos de Aqua, Ruby y Kana; estrella de **seis** puntas (V·1) | detalle |
| ídem | [0:25-0:27](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=25) | **Ruby, dedo en los labios, sonrisa pícara**, fondo de puntos LED (V·2) | pose «shh» |
| ídem | [0:30-0:31](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=30) | **buscador tipo Google «I'm feeling good»** (V·3) | #redes |
| ídem | [0:32-0:33](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=32) | **MEM baila en una azotea**, jersey turquesa, brazos arriba (V·4) | celebrar |
| ídem | [0:35-0:37](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=35) | Kana con boina, mano en la mejilla; luego en una puerta (V·5) | pensar |
| ídem | [0:51](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=51) | pancarta de fan «アイ無限恒久永遠推し!!» | fans |
| ídem | [0:57-0:58](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=57) | **Ai canta en una escalera de luces rosa** (V·6) | #en-directo |
| ídem | [1:10](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=70) | matrícula «45510»: la **contraseña del blog de B小町** en el relato «45510» de Akasaka que inspiró «Idol» ([wiki](https://oshinoko.fandom.com/wiki/45510)) | guiño de fan, #redes |
| ídem | [1:16-1:22](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=76) | **logo**: negro sobre blanco y blanco sobre azul `#22215A` (V·7) | tipografía |
| [Ending T1, «Mephisto»](https://www.youtube.com/watch?v=0saw1cGIl1A) | [0:18-0:27](https://www.youtube.com/watch?v=0saw1cGIl1A&t=18) | cada personaje sobre **su color plano**: Aqua azul, Ruby magenta, Akane violeta, MEM amarillo, Kana rojo (V·8-10) | paleta |
| ídem | [0:01-0:08](https://www.youtube.com/watch?v=0saw1cGIl1A&t=1) | conejo de peluche colgado de hilos, bajo un foco | tono oscuro: **no** |
| [Tráiler principal 2 (T1)](https://www.youtube.com/watch?v=gKWEUJ4r5do) | [0:36-0:37](https://www.youtube.com/watch?v=gKWEUJ4r5do&t=36) | **objetivo de una cámara con Kana dentro** (V·11) | #castings |
| ídem | [0:40](https://www.youtube.com/watch?v=gKWEUJ4r5do&t=40) | **Akane lee un guion rojo** (V·12) | #castings |
| ídem | [0:44-0:45](https://www.youtube.com/watch?v=gKWEUJ4r5do&t=44) | **MEM en directo con un marco de neón** cian y amarillo, sofá, osito (V·13) | #redes |
| ídem | [1:01-1:04](https://www.youtube.com/watch?v=gKWEUJ4r5do&t=61) | «4月12日(水) ON AIR» en mincho negro sobre blanco (V·14) | #en-directo |
| [«STAR☆T☆RAIN», ep. 11](https://www.youtube.com/watch?v=S-UmqvA7uR8) | [0:03-0:05](https://www.youtube.com/watch?v=S-UmqvA7uR8&t=3) | escenario al aire libre con torres de focos y un mar de **barras amarillas** (V·15) | #en-directo |
| ídem | [0:07-0:09](https://www.youtube.com/watch?v=S-UmqvA7uR8&t=7) | **MEM apunta con las manos en «pistola»; Kana, los dos índices junto a la cara; Ruby, el brazo arriba** (V·16-17) | animar |
| ídem | [0:26-0:27](https://www.youtube.com/watch?v=S-UmqvA7uR8&t=26) | las tres en fila, cada una con su gesto (V·18) | presentar |
| ídem | [1:20](https://www.youtube.com/watch?v=S-UmqvA7uR8&t=80) | **Ai aparece sobre Ruby**, brazo arriba | emoción |
| [«Piman Taisou», ep. 9](https://www.youtube.com/watch?v=BPvD-dfIiEs) | [0:00-0:02](https://www.youtube.com/watch?v=BPvD-dfIiEs&t=0) | cartela infantil verde y amarilla; Kana niña entre dos pimientos (V·25) | humor |
| [«Bのリベンジ», ep. 25](https://www.youtube.com/watch?v=5B-ZPcq8KxQ) | [0:19-0:20](https://www.youtube.com/watch?v=5B-ZPcq8KxQ&t=19) | Kana T3 con moños y lazos rojos (V·26) | vestuario T3 |
| [«MEMちょの部屋» #37](https://www.youtube.com/watch?v=TvIOIATbUYE) | [0:05](https://www.youtube.com/watch?v=TvIOIATbUYE&t=5) · [1:29-2:13](https://www.youtube.com/watch?v=TvIOIATbUYE&t=89) | **MEM hace directo**: rótulo naranja «MEMちょだよー!» y **ventana blanca con el mensaje de un fan** (V·19-20) | **#redes** |
| [«最新NEWS», canal oficial](https://www.youtube.com/watch?v=VjyCYUdmlnc) | [0:00-0:06](https://www.youtube.com/watch?v=VjyCYUdmlnc&t=0) | **noticiero dentro de la serie**: cartón «NEWS» y rótulo **«最新»** (V·21-22) | **#redes-y-novedades** |
| ídem | [0:44](https://www.youtube.com/watch?v=VjyCYUdmlnc&t=44) | **carta de ajuste con conejos** (V·23) | #en-directo |

---
## 5 · 3D y fan art (sólo como referencia o con su licencia)

### 5.1 · Objetos 3D para Blender (Sketchfab y Poly Haven)
**Segunda pasada:** licencias **comprobadas por la API de Sketchfab**
(`api.sketchfab.com/v3/models/<uid>`) ✅. **Corrección:** los dos modelos
de *plaggy* se llaman «CC0 - …» pero en Sketchfab están publicados con
**CC Attribution** (CC BY 4.0): hay que dar crédito.

| Objeto | Modelo | Licencia (API) | Para qué |
|---|---|---|---|
| Letrero **ON AIR** | [On Air Sign, de aricshow](https://sketchfab.com/3d-models/on-air-sign-0a5b90a7c5704803b2317c271fd8d156) | CC BY ✅ | **Concepto B** |
| Caja de luz | [Light box, de .after moon.](https://sketchfab.com/3d-models/light-box-f0dbe7d7a8854e44b672f515667c8ff2) | CC BY ✅ | alternativa al ON AIR |
| Neón | [CC0 - Neon Sign Open, de plaggy](https://sketchfab.com/3d-models/cc0-neon-sign-open-9a924db296cf4a1eb12991702ab48da5) | **CC BY** ✅ (no CC0) | letrero de fondo |
| **Claqueta** | [CC0 - Clapperboard, de plaggy](https://sketchfab.com/3d-models/cc0-clapperboard-b541acf3a4f040f98b1bbf4137a66d09) | **CC BY** ✅ (no CC0) | **Concepto C** |
| Claqueta | [Film Clapperboard, de Quince Creative](https://sketchfab.com/3d-models/film-clapperboard-free-3d-model-c5c798aa23024b868f7653229911b915) | CC BY ✅ | alternativa |
| **Portapapeles** | [Clipboard, de Cookie](https://sketchfab.com/3d-models/clipboard-a37158f20ccf436483029e8295629738) | CC BY ✅ | **Concepto C** (la hoja) |
| **Barra de luz** | [Glow Stick, de scbenoit](https://sketchfab.com/3d-models/glow-stick-e287b5f03d6d404198b7ed8c4cd91bc7) | CC BY ✅ | conceptos A y B |
| Barra de luz | [Glowstick, de Rofnay](https://sketchfab.com/3d-models/glowstick-cbc7f31c658247219c32b083183513e5) | CC BY ✅ | alternativa |
| **Aro de luz** | [Ring Light, de Mehdi Shahsavan](https://sketchfab.com/3d-models/ring-light-fe2d9eda3939484ea10c3ebc4887c28a) | CC BY ✅ | **Concepto A** |
| **Silla gamer** (la de MEM es rosa) | [Gaming Chair, de Kiiba](https://sketchfab.com/3d-models/gaming-chair-ccb3ada5917a4b90b689e1d1bf852dc2) | CC BY ✅ (nuevo) | **Concepto A** |
| **Uchiwa** (abanico de fan) | [Japanese Uchiwa Hand Fan 02, de HQ3DMOD](https://sketchfab.com/3d-models/japanese-uchiwa-hand-fan-02-be561cd8b01b49c482a4b26a8ec20bf0) | CC BY ✅ (nuevo) | primer plano de B |
| Focos de escenario | [STAGE LIGHTS, de Maxime GUINARD](https://sketchfab.com/3d-models/stage-lights-373fdaaa7fd94665b421c3a344cfbff5) | CC BY ✅ (nuevo) | concepto B |
| Torre de focos | [Square Truss Straight Segment 21, de akerStudio](https://sketchfab.com/3d-models/square-truss-straight-segment-21-f43719b6267645a587a9d3959b5f2d2b) | CC BY ✅ (nuevo) | escenario del ep. 11 (V·15) |
| Silla de director | [Director's Chair, de creativejenna](https://sketchfab.com/3d-models/directors-chair-d664c3ed7e1d48f5a0c0ad7f6581477b) | CC BY ✅ (nuevo) | fondo de C |
| Micro de mano | [Hand Mic 3d low poly, de abdurrazzak3441](https://sketchfab.com/3d-models/hand-mic-3d-low-poly-model-693fc3c678204b7892ce135d3a697869) | CC BY ✅ (nuevo) | Ruby en B |
| Papel | [Poly Haven, Paper & Card](https://polyhaven.com/textures/paper-card) | **CC0** | la hoja de audición |
| Metal pintado | [Poly Haven, Painted Metal Shutter](https://polyhaven.com/a/painted_metal_shutter) | **CC0** | pasillo del plató |
| Caja de cartón | [Poly Haven, Cardboard Box 01](https://polyhaven.com/a/cardboard_box_01) | **CC0** | trastienda del plató |

**Crédito exacto** para un modelo CC BY: «"On Air Sign" by aricshow
(sketchfab.com/aricshow), CC BY 4.0». Igual con cada uno: nombre del
modelo, autor, Sketchfab, CC BY 4.0. Los enlaces son los `viewerUrl` que da
la API.

**Modelos de personajes** (sólo para mirar volúmenes, **nunca** para la
lámina: son personajes con copyright):
[Ai, de DarienToad](https://sketchfab.com/3d-models/ai-hoshino-oshi-no-ko-64ce3c96f9524644a38c47c390b40488),
[Ai, de HiGuys920](https://sketchfab.com/3d-models/oshi-no-ko-hoshino-ai-3d-model-fv-dl-5d92181a0dec48d4a6a71c4a1d0fd5ec),
[Akane, de HiGuys920](https://sketchfab.com/3d-models/oshi-no-ko-akane-kurokawa-3d-model-fv-dl-5e6377c8751240dda0011c8d5536bb1e),
[Kana chibi](https://sketchfab.com/3d-models/kana-arima-chibi-oshi-no-ko-a92ff7003f534e3fbaf4f1cf0d01d001),
[etiqueta «oshinoko»](https://sketchfab.com/tags/oshinoko).

**Proyecto 3D en GitHub:** una **cinta de casete** de Oshi no Ko que se
abre en 3D con capas (Atropos.js), de TheFabi8A
([repositorio](https://github.com/TheFabi8A/oshi-no-ko),
[captura 1535×863](https://raw.githubusercontent.com/TheFabi8A/oshi-no-ko/HEAD/public/screenshots/oshi-no-ko-open.webp)).
Buena idea de objeto con capas, pero es de fans.

### 5.2 · Fan art (enlace y autor; nunca para pegar)
**Segunda pasada:** autor, tamaño y fecha leídos de la API de Pixiv
(`pixiv.net/ajax/illust/<id>`) ✅.
- Kana, «あんたの推しの子になってやる！», de **62KI**, 4093×2774,
  2-jul-2023, 1358 favoritos ([pixiv 109531606](https://www.pixiv.net/en/artworks/109531606)).
- Kana, de **むぎ (Mugi)**, 2400×3000, 1-ago-2023 ([pixiv 110449082](https://www.pixiv.net/en/artworks/110449082)).
- Kana, de **Nia (ニア)**, 2560×2560, 9-jul-2024 ([pixiv 120384765](https://www.pixiv.net/en/artworks/120384765)).
- Kana, «あ...あげる！», de **ややちゃん**, 3188×3560, 12-sep-2024,
  1145 favoritos ([pixiv 122364606](https://www.pixiv.net/en/artworks/122364606)).
- **MEM en directo**: «『こんめむー、今日も来てくれてありがとー！』»
  («¡Kon-memu! Gracias por venir hoy también»), de **ﾘﾝｺ (Rinko)**,
  1337×1863, 25-nov-2023 ([pixiv 113692523](https://www.pixiv.net/en/artworks/113692523)).
  Prueba de que los fans reconocen el saludo «こんめむ» (§8).
- Ficha de B小町 en la enciclopedia de Pixiv ([dic.pixiv](https://dic.pixiv.net/a/B%E5%B0%8F%E7%94%BA)).
- Fondos 4K: [Ai, 4kwallpapers](https://4kwallpapers.com/anime/ai-hoshino-oshi-no-16193.html),
  [B小町, 4kwallpapers](https://4kwallpapers.com/anime/oshi-no-ko-b-25258.html) (4096×2883),
  [Alpha Coders, 420+](https://alphacoders.com/oshi-no-ko-wallpapers).

**Fondos de pantalla en alta, con tamaño y autor (segunda pasada)**

| Fondo | Tamaño | Autor · fuente | Tipo |
|---|---|---|---|
| [Póster Newtype 2023-08, B小町](https://static.wikia.nocookie.net/oshi_no_ko/images/2/27/Newtype_2023_08_Poster.jpg) | 6080×4097 | revista Newtype (API de la wiki) | oficial |
| [Akane, Año Nuevo 2025](https://static.wikia.nocookie.net/oshi_no_ko/images/d/d9/Akane_New_Year_2025.png) | 4096×2906 | canal oficial (API de la wiki) | oficial |
| [Key visual 1 de la T1, Ai de espaldas](https://static.wikia.nocookie.net/oshi_no_ko/images/5/5f/Season_1_Key_Visual.png) | 2500×3535 (vertical) | comité de producción (API de la wiki) | oficial |
| [Key visual T1 de Crunchyroll](https://a.storyblok.com/f/178900/1000x1415/4edef43ef1/oshi-no-ko-visual.jpg) | 1000×1415 (vertical) | Crunchyroll Latinoamérica (medido) | oficial |
| [Kana, «あんたの推しの子になってやる！»](https://www.pixiv.net/en/artworks/109531606) | 4093×2774 | **62KI**, Pixiv, 2-jul-2023 (medido) | fan art |
| [B小町, 4kwallpapers](https://4kwallpapers.com/anime/oshi-no-ko-b-25258.html) | 4096×2883 | **sin autor** en la página | desconocido |
| [Ai, 4kwallpapers](https://4kwallpapers.com/anime/ai-hoshino-oshi-no-16193.html) | 5263×3206 | **sin autor** en la página | desconocido |

---

## 6 · Sitios, luz, paleta y texturas

### 6.1 · Los sitios que sirven
| Sitio | Dónde sale | Luz y hora | Para qué canal |
|---|---|---|---|
| **Plató de un programa musical en directo** | ep. 1, 18:00–21:48 (vuelta de Ai) | noche, focos de color, pasillos oscuros | **#en-directo** |
| **Escenario del Japan Idol Festival** | ep. 11 | escenario con focos y un mar de barras de luz rojas, blancas y amarillas | #en-directo |
| **Oficina de Ichigo Production** (苺プロ) | todo el anime | interior de día, luz de fluorescente | #redes, #castings |
| **Sala de pruebas y rodaje** (drama de Kana, película de Gotanda) | ep. 1 (43:00–48:30), ep. 3, T3 ep. 34 | mesa larga, luz blanca | **#castings** |
| **Instituto Yōtō, sección de espectáculos** | ep. 2–4 | día, pasillos claros | secundario |
| **Shibuya: Starbucks del TSUTAYA, 2.ª planta** (donde reclutan a Ai) | ep. 1 | día | secundario ([聖地巡礼.com](https://anime-pilgrimage.com/oshi-no-ko/)) |
| **Takachiho (Miyazaki)**: hospital de Goro y santuario Aradate, **dios de las artes escénicas** | ep. 1, final de T2 | bosque, niebla, luz de tarde | no para estas láminas ([ciatr](https://ciatr.jp/topics/324247), [たかちほまびぃ](https://takachiho.online/archives/19611)) |
| **Pasillo de Ichigo Pro con la placa «(株)苺プロ 斉藤»** (con una fresa) | anime (O·23, 1920×1080) | puerta azul noche `#121A25`, placa gris cálido `#CFC7C0` con letras `#7D6564`, luz fría de pasillo | **#castings** (la puerta de la agencia) ✅ |
| **El cuarto de directo de MEM** (canal oficial) | «MEMちょの部屋» (V·19-20) | añil `#2A0F6E` y violeta `#9F4AC1`, luna amarilla, neón cian arriba, silla gamer rosa, peluches de B小町 | **#redes** ✅ |
| **Plató de noticias** dentro de la serie | «最新NEWS» (V·22) | fondo celeste `#A4D9D3` con franjas blancas, presentador de traje | **#redes-y-novedades** ✅ |
| **Cuarto con dos aros de luz, micro de brazo y dos pantallas** | T2, ep. 21 (O·16) | interior de día, luz blanca de aro | #en-directo ✅ |
| **Sala de ensayo de Lalalai** | T2 (O·24) | nave grande, luz blanca | #castings ✅ |
| **Instituto Yōtō** por fuera | T1-T2 (O·25) | día claro, edificio beige | secundario ✅ |
| **Escenario al aire libre del Japan Idol Festival** | ep. 11 (V·15) | noche azul `#1E2F7D`→`#465EB9`, torres de focos, ciudad detrás, mar de barras amarillas | #en-directo ✅ |
| **Cabina de doblaje real** (grabación de la T3) | visita oficial al estudio ([1:44](https://www.youtube.com/watch?v=izzRjaUZig4&t=104)) | interior, luz cálida; listones de madera `#9A6B4B`, paneles oscuros `#41383C`, micro de condensador | **#castings** ✅ (2.ª tanda) |

### 6.2 · Paleta medida
Medida con Pillow (mediana de cada zona, **±10 por canal** porque las
zonas se marcaron a mano) en `bg19`, `bg12`, `bg20` y el key visual de Ai.

| Qué | Hex | Dónde se midió |
|---|---|---|
| Pelo de **Kana**, rojo vivo | `#E2102F` / `#C00E25`, sombra `#8E1223` | bg19 |
| Uniforme rojo de B小町 | `#C41E34` / `#981A34`, sombra `#68172A` | bg19 |
| Capa de Ruby (más magenta) | `#AF204F` | bg12 |
| Negro de lazos y faldas | `#261C33` / `#28142B` | bg19, bg12 |
| Chorrera blanca | `#F4EFEA` | bg19 |
| Guantes rosa | `#CF6E9C` / `#F16691` | bg12, bg19 |
| Pelo de **Ruby**, dorado | `#FDF18A` luz, `#ECB26D` medio, `#D9A857` sombra | bg19, bg12 |
| Pelo de **MEM-cho**, limón | `#FEE63E` / `#FEF757`, sombra `#EFC65F` | bg19, bg12 |
| Pelo de **Akane**, azul violeta | `#2B1652` / `#4F4175` / `#615B93` | bg12 |
| Pelo de **Ai**, índigo | `#3F255D`, reflejo vino `#6D1E49` | key visual de Ai |
| Ojo de Ai, violeta | `#6A3FA3` | key visual de Ai |
| Vestido y guantes de Ai, fucsia | `#E43F7D` / `#EA629A` | key visual de Ai |
| Fondo de escenario rosa (Ai) | `#BA5E84` / `#D8ACCC` | key visual de Ai |
| Noche del escenario (bg19) | `#222B32` / `#293B40`, brillo verde azulado `#5CA19B` | bg19 |
| Fiesta de San Valentín | `#FDD6D0`, `#ED6A7C`, `#FFE874` | bg20 |
| Fondo de lunares azul | `#B9E4FE` | bg12 |

**Colores de cada idol** (para las barras de luz): **Ruby rojo, Kana
blanco, MEM-cho amarillo** ✅ (ep. 11, 03:34–03:53: «el rojo destaca»,
«si da igual, blanco»; y [ciatr](https://ciatr.jp/topics/324070) /
[manganasekai](https://manganasekai.com/bcomachi/)). Hay vasos oficiales
con el «color de cada una» en Lawson ([Lawson](https://www.lawson.co.jp/lab/entertainment/art/20241008_bookoshinoko.html)).
**Segunda pasada:** lo confirman los nombres de las cartas oficiales de
*IDOLM@STER Shiny Colors*: «**In Red** Ruby», «**In White** Kana»,
«**In Yellow** MEMCho» (índice sitios n.º 226-231) ✅.
El color de Ai: sigue sin encontrarse ⚠️ (busqué «image color»,
«member color», «penlight» y «glow stick» en el texto de la wiki y en la
ficha de B-Komachi; ninguna le asigna color).

**Colores medidos en la segunda pasada** (Pillow; en *storyboards* de
320 px, ±10 por canal; en archivos de la wiki, mediana por cuantización):

| Qué | Hex | Dónde |
|---|---|---|
| Cartela de episodio: rombos rojo-rosa · blanco · negro | `#E74D64` · `#F8F8F8` · `#10110E` | O·19 (1920×1080) |
| Cartela: variante cian · variante violeta | `#00AFCA` · `#9867A5` | O·20, O·21 |
| Fondo azul del logo en el opening | `#22215A` (±`#282762`) | V·7 |
| Fondos planos del ending: Aqua · Ruby · Akane · MEM · Kana | `#347DBA` · `#B5408B` · `#4A308E` · `#C9B33D` · `#A31D3A` | V·8-10 (ED 0:18-0:27) |
| Cuarto de MEM: pared añil · luz violeta · blanco del mensaje · cabecera lila | `#2A0F6E`/`#411B6D` · `#9F4AC1` · `#FFFFFF` · `#9E81C3` | V·19-20 |
| Rótulo de MEM: relleno naranja · borde crema · borde exterior morado | `#DCAC64` · `#FFF3CE` · `#A0628B` | V·19 |
| Noticiero: cartón «NEWS» rosa · rojo del rótulo «最新» | `#D87FB9` · `#AC3065` (círculo) | V·21-22 |
| Pelo de **Kana** (render oficial, sin luz de escenario) | `#83132C`, sombra `#58182E`; boina azul marino | P·7 |
| Pelo de **MEM** (render) | miel `#E2A144`, sombra `#C08445`, puntas `#E5B266` | P·16 |
| Pelo de **Ruby** (render) | rubio `#EAC189`/`#D8B682`, mechas rosa | P·19 |
| Pelo de **Akane** (render) | azul pizarra `#4B4970`/`#50557A`, puntas verdosas | P·22 |
| Pelo de **Ai** (render) | índigo `#31266A`/`#452872`, sombra `#211C52`, mecha rosa `#AF7794` | P·4 |
| Traje idol de Ai (render) | carmesí `#D32650`, lazo `#441544`, blanco `#EFDEE7` | P·4 |
| Pelo de **Gotanda** · su chaqueta | castaño `#794B56`/`#543541` · azul noche `#2E3150` | P·24 |
| **Magenta del key visual T1** (fondo con destellos) · jersey de MEM · guion de Kana | `#E30182`/`#E60182` (casi el `#E70082` de la «の» del logo) · verde menta `#BEE69D` · lila `#E485F1` | key visual de Crunchyroll, 1000×1415 (2.ª tanda) |
| «Mensaje especial» de Akane: fondo · marco | lila `#E5C5EC`/`#DDBDE4` · violeta `#9D58A9` | *storyboard* de [L-ZNenzreyU](https://www.youtube.com/watch?v=L-ZNenzreyU&t=1) (2.ª tanda) |
| Estudio de doblaje real: listones de madera · paneles · cartela rosa | `#9A6B4B` (sombra `#5D331A`) · `#41383C` · `#F8D8DD` y `#FDF2F5` | *storyboard* de [izzRjaUZig4](https://www.youtube.com/watch?v=izzRjaUZig4&t=104) (2.ª tanda) |

**Ojo con los tonos:** bajo los focos (bg19, ep. 11) el pelo de Kana
sale rojo vivo (`#E2102F`) y el de MEM, limón (`#FEE63E`); en los
renders oficiales, sin luz de escenario, **Kana es carmesí oscuro y MEM
es rubio miel**. Para una lámina de día, usar los del render.

### 6.3 · Luz de la serie
- El director de fotografía **Takafumi Kuwano** propuso que **las
  estrellas de los ojos brillen distinto en cada plano**, y se sube el
  brillo cuando se ven de cerca ([Febri ②](https://febri.jp/topics/oshinoko_imamaki_02/)).
- En el último episodio se hizo brillar **a Ruby más que a Ai** en
  algunos planos del concierto ([Febri ③](https://febri.jp/topics/oshinoko_imamaki_03/)).
- En el episodio 6 el **espejo** se usa para confundir verdad y mentira
  ([Dengeki](https://dengekionline.com/articles/186111/)).
- En los fondos vistos: escenario = **negro azulado con focos
  cian y láseres rosa/violeta**; eventos alegres = **rosa y amarillo
  con desenfoque**.

### 6.4 · Texturas reales equivalentes
- Hoja de audición: **papel** ([Poly Haven](https://polyhaven.com/textures/paper-card)).
- Pasillo del plató: **metal pintado** ([Poly Haven](https://polyhaven.com/a/painted_metal_shutter)).
- Cajas del backstage: **cartón** ([Poly Haven](https://polyhaven.com/a/cardboard_box_01)).
- Letrero ON AIR: acrílico rojo retroiluminado (el modelo de Sketchfab).

---

## 7 · Tipografía (y si trae tildes, ñ, ¿ y ¡)

**El logo** es **【推しの子】**: el título va **dentro de corchetes
lenticulares 【 】** ([Wikipedia, archivo del logo](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB:Oshi_no_Ko_logo.svg)).

> [!warning] Corregido en la segunda pasada
> Antes decía «gótica muy gruesa». **No es gótica: es una mincho**
> (letra con remates, trazo grueso y fino, puntas de pincel). Lo vi en
> la cartela del ep. 1 (O·22, 1920×1080) y en el opening (V·7,
> [1:16](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=76)). Detalles
> medidos con Pillow en la cartela:
> - Letras en **negro puro `#000000`**; sobre azul `#22215A`, en blanco.
> - La **«の» va en magenta `#E70082`** y lleva dentro, en blanco, una
>   **estrella de seis puntas** (el ojo de la serie).
> - Cada corchete 【 】 lleva **una raya fina vertical por fuera**.
> - En los rótulos del tráiler, la misma mincho, pequeña, gris, con la
>   palabra clave en rosa («アイドル»), y «ON AIR» en mincho latina
>   ([tráiler, 1:01](https://www.youtube.com/watch?v=gKWEUJ4r5do&t=61)).

**El nombre de la letra oficial sigue sin aparecer** ⚠️. Hay una guía japonesa
de letras que combinan con la serie ([DesignPocket #093](https://designpocket.jp/static/font/fontguide/093.html))
y una letra gratis hecha por fans, «推しゴ», pensada para abanicos y
carteles de idol ([ffont](https://ffont.jp/oshigo/), [BOOTH](https://booth.pm/ja/items/5635169)).
Gratis y con uso comercial, de «アトリエこたつ». Su ficha de BOOTH dice
que trae **hiragana, katakana, letras y números, símbolos, 121 kanji y
32 iconos para abanicos**; no nombra tildes ni ñ. No la pude abrir con
fontTools: **BOOTH pide iniciar sesión para bajarla** ⚠️. Si se usa,
sólo para palabras sin tildes (ON AIR, B小町).

**Letras libres comprobadas.** Se bajó cada archivo de Google Fonts y se
miró su tabla de caracteres con fontTools
([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/delagothicone/METADATA.pb)).
Todas son **OFL** (libres).

| Letra | á é í ó ú ñ ¿ ¡ | 【 】 | ★ ☆ | Uso |
|---|---|---|---|---|
| **Dela Gothic One** | ✅ | ✅ | ✅ | títulos gruesos con corchetes (**no** es la del logo: ver arriba) |
| **M PLUS Rounded 1c** ExtraBold | ✅ | ✅ | ✅ | pantalla del móvil, texto amable |
| **Zen Maru Gothic** Bold | ✅ | ✅ | ✅ | cuerpo de texto redondo |
| **Mochiy Pop One** | ✅ | ✅ | ❌ (sí ♡) | letra de idol, pop |
| **RocknRoll One** | ✅ | ✅ | ✅ | rótulo de TV (telop) |
| **Kiwi Maru** | ✅ | ✅ | ✅ | texto suave |
| **Hachi Maru Pop** | ✅ | ✅ | ✅ | **letra a mano de chica** (notas de Kana) |
| **BIZ UDPGothic** Bold (Morisawa) | ✅ | ✅ | ✅ | **impreso de la hoja de audición** |
| **DotGothic16** | ✅ | ✅ | ✅ | pantallas LED del escenario |
| **Bebas Neue** | ✅ | ❌ | ❌ | **ON AIR** (sólo mayúsculas latinas) |
| **Courier Prime** | ✅ | ❌ | ❌ | guion, sello de fecha |
| **Montserrat** ExtraBold | ✅ (latin) | — | — | textos largos en español |
| **Shippori Mincho B1** ExtraBold | ✅ | ✅ | ✅ | **la más parecida al logo** (mincho) · nueva |
| **Zen Old Mincho** Black | ✅ | ✅ | ✅ | títulos estilo logo, más negra · nueva |
| **Noto Serif JP** Black | ✅ | ✅ | ✅ | mincho de reserva, muchos pesos · nueva |
| **M PLUS Rounded 1c** Black | ✅ | ✅ | ✅ | **rótulo naranja de MEM** y «第X話» de las cartelas · nueva |
| **Noto Sans JP** Black | ✅ | ✅ | ✅ | **rótulo de noticias «最新»** · nueva |
| **Kaisei Decol** Bold | ✅ | ✅ | ✅ | alternativa redondeada con remate · nueva |
| **Playfair Display** Italic | ✅ | ❌ | ❌ | el cartón **«NEWS»** en cursiva con remate (V·21) · nueva |

(Las «nueva» se comprobaron en la segunda pasada con fontTools, sobre
los .ttf de `google/fonts`: `á é í ó ú ñ Ñ ¿ ¡ 【 】 ★ ☆ ♡ ♪` y los
kanji 最 新 推.)

**Letra de los globos del manga:** no encontré cuál usa Yen Press ni
Panini ⚠️ ([Yen Press](https://yenpress.com/series/oshi-no-ko)).

---

## 8 · Cómo hablan en pantalla (el «cuadro de diálogo» de Oshi no Ko)

Oshi no Ko **no tiene un globo propio famoso**. Su firma son el **marco**
y la **pantalla**: todo es actuación y todo pasa por un dispositivo.

1. **Los corchetes 【 】.** Están en el logo y en **los títulos de
   episodio**: el 6 se llama **【エゴサーチ】** en la ficha de la cadena
   ✅ ([TOKYO MX](https://s.mxtv.jp/anime/oshinoko/episode.html?ep_id=1bgjyr9388eeltqi),
   [blog de reseñas](https://lastbreath.hatenablog.com/entry/2023/05/18/115322);
   [web oficial del ep. 6](https://ichigoproduction.com/Season1/story/06.html)).
   **Úsalos como marco del título** de cada lámina: 【NUESTRAS REDES】,
   【ON AIR】, 【HOJA DE AUDICIÓN】.
2. **La estrella de seis puntas** en los ojos. **Blanca** = carisma,
   la «mentira bonita»; **negra** = venganza (Aqua) o la etapa oscura de
   Ruby ✅ ([Attack of the Fanboy](https://attackofthefanboy.com/anime/oshi-no-ko-why-do-some-characters-eyes-have-bright-dark-stars/),
   [Game Rant](https://gamerant.com/oshi-no-ko-why-do-aqua-and-ruby-have-stars-in-their-eyes/)).
   Ai en los dos ojos; **Aqua en el derecho, Ruby en el izquierdo**.
   Lo confirma en español **Crunchyroll News** («estrellas de seis
   puntas», blancas o doradas = carisma; negras = la verdadera
   naturaleza; Akane las gana cuando interpreta a Ai)
   ([artículo, 2-abr-2026](https://www.crunchyroll.com/es/news/features/2026/4/2/significado-ojos-estrellados-oshi-no-ko)) ✅.
   **Úsala como viñeta** delante de cada paso, siempre blanca.
3. **Voces que llegan por un aparato.** En los subtítulos japoneses de
   la emisión de TV se marcan con 📱 (teléfono) y 🖥️ (monitor): Kana habla por
   videollamada en el ep. 3 (10:48). Los mensajes, retuits y
   suscriptores salen en pantallas (ep. 1, 7 y 9).
4. **Comentarios de redes flotando** en el ep. 6 (el acoso a Akane)
   ([Anime Corner](https://animecorner.me/oshi-no-ko-episode-6-shows-the-best-depiction-of-cyberbullying/)).
   Sirve el **formato** (tarjeta de post), **nunca** el contenido.
5. **El «call» del público**: «We! are! STAR T RAIN / Check! Now! /
   Come on! Come on!» (ep. 11, 04:15). Mayúsculas y signos de
   exclamación, como en un concierto de idols.

### 8.1 · Lo que encontré en la segunda pasada (visto, con minuto) ✅
6. **Las cartelas de episodio** (O·19-21, 1920×1080): una **estrella
   negra grande de cinco puntas, con las esquinas redondeadas**, en el
   centro; arriba «第十一話» en letra redonda gruesa rosa `#E74D64`,
   una fila de estrellitas blancas y el título en blanco. Detrás, un
   **damero de rombos** (rojo-rosa y blanco en el ep. 11, cian en el 5,
   violeta en el 9), manchas negras y puntos blancos. **Es el marco de
   título más propio de la serie.**
7. **El directo de MEM** («MEMちょの部屋», canal oficial,
   [0:05](https://www.youtube.com/watch?v=TvIOIATbUYE&t=5) y
   [1:29](https://www.youtube.com/watch?v=TvIOIATbUYE&t=89); V·19-20):
   - lo que dice MEM va en un **rótulo naranja `#DCAC64` con doble
     borde crema y morado**, abajo: «MEMちょだよー!» («¡Soy MEM-cho!»);
   - lo que escriben los fans va en una **ventana blanca con cabecera
     lila `#9E81C3`** («MEMber: サンデーエレファント»), sombra rosa y un
     piquito abajo a la derecha, como un globo de chat;
   - el saludo del canal es **«こんめむ〜♪»** (*kon-memu*, «hola» a lo
     MEM) y el «buen trabajo», **«おつめむー!»** (*otsu-memu*); los dos
     salen en los mensajes de fans que ella lee (1:29 y 2:28). A sus
     fans los llama **«MEMber»** ✅ (vídeo oficial + fan art de Pixiv
     que usa el saludo, §5.2).
8. **El noticiero de la serie** («最新NEWS», canal oficial,
   [0:00-0:06](https://www.youtube.com/watch?v=VjyCYUdmlnc&t=0); V·21-22):
   cartón rosa `#D87FB9` «Next Corner >>> **NEWS**» en cursiva con
   remate, y el **rótulo de noticia**: círculo rojo con «**最新**»
   («lo último») + franja blanca con el titular en gótica negra y una
   raya roja debajo. **Es el cuadro natural de #redes-y-novedades.**
9. **Los cartones oficiales de cuenta atrás** (O·1-4, 1440×1080): fondo
   magenta con destellos, esquina negra con «あと8日» («faltan 8 días»)
   o «本日放送» («hoy»), una **cartulina blanca escrita a rotulador y
   firmada por el seiyū**, el chibi del personaje y una **franja negra
   abajo: «【推しの子】4.12水 ONAIR»** con el papel y el nombre. **Es el
   «ON AIR» de la propia serie.**
10. **«本日ON AIR» a mano**: los animadores subían dibujos con «推しの子
    5話 本日ON AIR» («hoy se emite el ep. 5») escrito a lápiz (O·8-9).
11. **La pizarra de MEM** en un atril: «MEMちょの AJステージ直前 突撃"生"
    インタビュー!» («¡entrevista *en vivo* de MEM antes del escenario de
    AnimeJapan!»), a rotulador negro con estrellitas (O·5). **Es la
    cartulina de directo que buscaba la primera pasada** (ya no hace
    falta inventar la カンペ).
12. **La carta de ajuste con conejos** (V·23,
    [0:44](https://www.youtube.com/watch?v=VjyCYUdmlnc&t=44)): barras de
    colores con cabezas de conejo blancas y negras (el conejo es el
    peluche de Ai). Para «volvemos enseguida».
13. **Hitos del canal** (O·6-7): tarjeta «TVアニメ【推しの子】公式チャンネル
    **100,820** チャンネル登録者数» con MEM celebrando, y la captura del X
    oficial con **300.000** seguidores y Ai guiñando.
14. **El «mensaje especial» de un personaje** (canal oficial, 1-may-2026,
    [0:01-0:53](https://www.youtube.com/watch?v=L-ZNenzreyU&t=1), visto
    por *storyboard*): Akane de medio cuerpo, quieta, sobre **fondo lila
    `#E5C5EC` con rayas diagonales** y un **marco violeta `#9D58A9`** de
    esquinas redondas; arriba a la derecha su nombre y «スペシャルメッセージ»;
    abajo, **lo que dice en subtítulos blancos gruesos con borde morado**,
    frase a frase: «みなさん こんにちは / 劇団ララライの黒川あかねです /
    B小町の東名阪ツアーがスタートしています!» («Hola a todos, soy Akane
    Kurokawa, de Lalalai: ¡empezó la gira de B小町!»). **Es un aviso de
    novedades dicho por un personaje**: sirve tal cual para
    #redes-y-novedades (alternativa al noticiero).
15. **«推しセリフ» («la frase favorita»)**: la seiyū escribe la frase en
    un **shikishi** (cartón blanco firmado) y lo enseña a cámara
    ([#05, Manaka Iwami, 0:33-1:14](https://www.youtube.com/watch?v=VrIF12uKg1Y&t=33)).
    La frase se ve antes en la escena, en blanco entre 「 」 sobre el
    plano: «**「絶対に負けない」**» («No voy a perder»), T2 ep. 16
    ([0:29](https://www.youtube.com/watch?v=VrIF12uKg1Y&t=29)). Según sus
    subtítulos (0:35-0:44), **Kana y Akane lo piensan a la vez** al
    cruzarse antes del estreno de *Tokyo Blade*: rivales que sienten lo
    mismo. Idea para
    #castings: la frase del papel escrita en un cartón firmado.
16. **La visita al estudio de doblaje** («アフレコ現場を深掘れ☆ワンチャン‼»
    n.º 6, 19-feb-2026, [0:00-14:18](https://www.youtube.com/watch?v=izzRjaUZig4)):
    puerta «**STUDIO 1**» (0:00); **cabina** con marcos de listones de
    madera `#9A6B4B` (sombra `#5D331A`) sobre paneles oscuros `#41383C`
    y un **micro de condensador con araña** ([1:44](https://www.youtube.com/watch?v=izzRjaUZig4&t=104));
    Megumi Han (Kana) cuenta su escena favorita del ep. 30 (rótulo
    amarillo «潘さんの第三十話いち押しのワンシーン», [7:25](https://www.youtube.com/watch?v=izzRjaUZig4&t=445));
    cartela del programa con **rayas diagonales rosa `#F8D8DD` y blanco
    `#FDF2F5`** y un perrito con micro ([8:40](https://www.youtube.com/watch?v=izzRjaUZig4&t=520));
    y la **sala de control con la mesa de mezclas**, con el director de
    sonido Takeshi Takadera ([9:24](https://www.youtube.com/watch?v=izzRjaUZig4&t=564)).
    **Es el sitio real de un casting de voz**: sirve de fondo alternativo
    para #castings.

**Estrellas:** en los **ojos**, seis puntas; en las **cartelas y la
decoración**, cinco puntas (redondeadas). No mezclar: nada de estrella
de cinco en un ojo.

**El cuadro propio de cada lámina (actualizado):**
- **#redes-y-novedades:** el **rótulo de noticia «最新»** (círculo rojo +
  franja blanca) para el titular, y la **ventana de mensaje del directo
  de MEM** (blanca, cabecera lila) para los pasos. Letra: Noto Sans JP
  Black (rótulo) y M PLUS Rounded 1c (ventana). La frase de MEM, en su
  **rótulo naranja** (M PLUS Rounded 1c Black).
- **#en-directo:** el **cartón de cuenta atrás**: cartulina blanca
  escrita a mano (Hachi Maru Pop) sobre magenta con destellos y la
  **franja negra «ON AIR»** abajo (Shippori Mincho B1 para 【推しの子】,
  Bebas Neue para ON AIR). El letrero ON AIR físico sigue valiendo.
- **#castings:** la **cartela de estrella negra sobre rombos** para el
  título, y la **ficha de talento de Ichigo Pro** (como las de la web
  oficial: nombre, estatura, «活動実績» = «trabajos hechos») para la
  hoja de audición; notas a mano (Hachi Maru Pop) y sello rojo.

---
## 9 · Personajes: quién es, cómo habla, qué le importa

Voces: japonés e inglés de las fichas de ANN
([T1](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/anime/25783.json),
[T2](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/anime/28810.json),
[T3](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/anime/33662.json)).
Latino: ver punto 12. Frases: subtítulos japoneses (traducción mía).

### Kana Arima (有馬かな) — la más querida → **#castings**
- **Quién es:** fue la **niña prodigio** de la tele. Se presenta como
  «¡la niña genio que llora en 10 segundos!» (ep. 1, 49:41). Ruby la
  oye mal y la llama «la que lame bicarbonato» (重曹, 49:38). De ahí su
  apodo de fans: **«Bicarbonato-chan»** ✅ ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Memes/OshiNoKo)).
- **Su historia:** de niña tuvo un éxito, «Piman Taisou», que llegó al
  n.º 1 de Oricon (ep. 9, 17:57). Luego dejaron de llamarla. Entra en
  B小町 sin querer ser la del centro (ep. 10, 01:50).
- **Qué le importa:** que la vean, no quedarse olvidada. Actuar bien.
  Aqua, aunque no lo admita.
- **Miedo:** ser un juguete roto de la industria
  ([CBR](https://www.cbr.com/oshi-no-ko-kana-arima-popularity-explained/),
  [Anime Corner](https://animecorner.me/oshi-no-ko-episode-10-kana-arima-is-the-best-written-character-in-the-series/)).
- **Cómo habla:** lengua afilada y rápida. Suelta «¡Qué asco!» (きっも！,
  ep. 3, 01:58). Presume: «Hmph. Es que yo soy adulta» (フフフン。私オトナだから,
  ep. 3, 14:42). **Explica con jerga de rodaje**, como una profesional:
  lectura, ensayo, cámara, pasada completa (ep. 3, 16:34–16:57).
- **Cómo se ríe:** «フフン» de suficiencia. **Cómo se enfada:** grita y
  luego se pone roja. **Tsundere**, según [CBR](https://www.cbr.com/oshi-no-ko-kana-arima-popularity-explained/).
- **Con quién:** pelea con Ruby, rivaliza con Akane desde niñas, discute
  con MEM. Enamorada de Aqua.
- **Su momento:** ep. 11, 07:41–07:49. Ve a Aqua con la barra blanca y
  jura: «¡Seré tu *oshi no ko*!».
- **Voz:** Megumi Han (JA), Natalie Rial (EN), **Ginette Zavala** (LAT) ✅.
- **Estatura: 150 cm**, la más baja del grupo ✅ ([web oficial](https://ichigoproduction.com/talent/arima.html) + wiki).
  La web oficial la trata como talento real de Ichigo Pro, con su lista
  de «trabajos hechos»: la película *Sore ga Hajimari*, anuncios de
  bicarbonato «重曹ちゃん» (O·14), pimientos de Miyazaki… Es humor
  interno: **Kana vive de trabajos pequeños y los enseña con orgullo**.

### MEM-cho (MEMちょ) — la de las redes → **#redes-y-novedades**
- **Quién es:** YouTuber y tiktoker. **370.000 suscriptores en YouTube y
  638.000 seguidores en TikTok** (ep. 9, 01:55–01:58). Trabaja por su
  cuenta, con un acuerdo con la agencia FARM (ep. 9, 02:08–02:20).
- **Su secreto:** dice ir a 3.º de instituto («高3のMEMちょです», ep. 5,
  08:09), pero es mayor. Dejó el instituto para cuidar a su madre y
  pagar los estudios de sus hermanos. Cuando pudo volver a su sueño,
  las audiciones pedían «chicas de hasta 20 años» (ep. 9, 04:21–05:01)
  ✅ ([ANIHK](https://anihk.com/en/blogs/characters/oshi-no-ko-mem-cho-real-age-revealed),
  [wiki](https://oshinoko.fandom.com/wiki/Mem-Cho)).
- **Qué le importa:** cumplir por fin su sueño de idol. Y los números.
- **Cómo habla:** alarga las vocales y endulza («アクたんはいいのぉ？»,
  ep. 6, 07:32). Llama a Aqua **«Aqu-tan»** (アクたん) ✅.
  Cuando se pone seria habla de datos: **«¿Sabes qué día y a qué hora
  subirlo para sacar más retuits, y cuántas letras rinden más? Soy una
  profesional de hacer virales»** (ep. 7, 11:16–11:30).
- **Cómo celebra:** chilla con las cifras: «¡10.000 suscriptores!» (ep. 9,
  09:42).
- **Con quién:** hermana mayor de B小町; cómplice de Aqua en el reality.
- **En su canal** (vídeos oficiales «MEMちょの部屋»): saluda con
  «こんめむ〜♪», sus fans son los «MEMber», lee sus mensajes y responde
  sonriendo a cámara, con la mano abierta o el índice en la barbilla
  (V·19-20) ✅.
- **Estatura: 155 cm** ✅ ([web oficial](https://ichigoproduction.com/talent/memcho.html) + wiki).
- **Voz:** Rumi Ōkubo (JA), Juliet Simmons (EN), **Paulina García** (LAT) ✅.

### Ruby Hoshino (星野ルビー) — la idol → **#en-directo**
- **Quién es:** hija de Ai. Renacida de Sarina, una niña enferma, fan de
  Ai y paciente de Goro ([ANN](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/anime/25783.json)).
- **Qué quiere:** ser idol como su madre: «¡Yo voy a ser idol!»
  (私はアイドルになるんだよ！, ep. 2, 03:56). Llama a Aqua «お兄ちゃん»
  (hermano).
- **Cómo es:** alegre, impulsiva, fan de su madre hasta el tuétano. De
  bebé se enfada porque no la despertaron para ver a Ai **en directo**
  (ep. 1, 23:34). Más tarde tiene una **etapa oscura** con la estrella
  negra ([Attack of the Fanboy](https://attackofthefanboy.com/anime/oshi-no-ko-why-do-some-characters-eyes-have-bright-dark-stars/)).
- **En el escenario:** anuncia las canciones: «¡Sign wa B!» (ep. 11,
  06:19). Estrella en el **ojo izquierdo**.
- **Estatura: 158 cm** ✅ ([web oficial](https://ichigoproduction.com/talent/ruby.html) + wiki).
- **Voz:** Yurie Igoma (JA), Alyssa Marek (EN), **Polly Huerta** (LAT) ✅;
  de niña, Lilian Vela; de bebé, Lucía Suárez ✅ (Doblaje Wiki + ANMTV).

### Ai Hoshino (星野アイ) — el icono
- **Quién es:** «la as absoluta de B小町, la del centro, la chica más
  guapa, 16 años» (ep. 1, 00:38–00:49). Madre secreta de los gemelos.
  Muere en el ep. 1.
- **Lo que piensa:** «La mentira es el amor más grande» (ep. 1, 09:46).
  Teme no saber querer: «No podré querer a mis fans» (ep. 1,
  65:04–65:07). Le dicen: «Los idols dicen "¡os quiero a todos!". El
  público quiere una mentira bonita» (65:15–65:24).
- **Cómo es:** alegre, caprichosa («Hoshino Ai es codiciosa», 10:23),
  guiña el ojo, apunta al público. Estrella en **los dos ojos**.
- **Estatura: 151 cm** ✅ ([web oficial](https://ichigoproduction.com/talent/ai.html) + wiki).
- **Voz:** Rie Takahashi (JA), Donna Bella Litton (EN),
  **Stephanie Filigrana** (LAT) ✅.

### Akane Kurokawa (黒川あかね) — la actriz genio
- **Quién es:** «la joven estrella de la compañía Lalalai», **actriz de
  método** que estudia a fondo a cada personaje (ep. 8, 01:41–02:04, en
  palabras de Kana) ✅ ([ANIHK](https://anihk.com/en/blogs/characters/oshi-no-ko-akane-kurokawa-character-guide)).
- **Su historia:** de niña era tímida; admiraba y temía a Kana. En el
  reality sufre acoso en redes (ep. 6). Vuelve **imitando a Ai** tan
  bien que a Aqua se le hiela la cara (ep. 8, 02:09).
- **Cómo habla:** suave, llama a Aqua «アクアくん» (ep. 8, 18:24).
  En su «mensaje especial» oficial saluda formal y cálida: «みなさん
  こんにちは / 劇団ララライの黒川あかねです» y anima a las demás por su
  nombre: «かなちゃん、ルビーちゃん、メムちゃん» ([0:01-0:38](https://www.youtube.com/watch?v=L-ZNenzreyU&t=1)) ✅ (visto).
- **Cuando actúa de Ai** le salen las **estrellas en los ojos** (P·21;
  [Crunchyroll News](https://www.crunchyroll.com/es/news/features/2026/4/2/significado-ojos-estrellados-oshi-no-ko)) ✅.
- **Con Kana:** rivales que se admiran. Antes del estreno de *Tokyo
  Blade* las dos piensan a la vez «絶対に負けない» («no voy a perder»)
  (T2 ep. 16; [推しセリフ #05](https://www.youtube.com/watch?v=VrIF12uKg1Y&t=29)) ✅ (visto).
- **Aspecto en el arte de 2025-2026** (vídeos oficiales): media melena
  azul marino que **degrada a verde agua en las puntas**, vestido negro
  de volantes ([mensaje, 0:03](https://www.youtube.com/watch?v=L-ZNenzreyU&t=3)).
- **Estatura: 163 cm**, la más alta ✅ ([web oficial](https://ichigoproduction.com/talent/kurokawa.html) + wiki).
- **Voz:** Manaka Iwami (JA), Kristen McGuire (EN), **María García** (LAT) ✅.

### Aqua Hoshino (星野アクア) — el hermano frío
- Renacido de Goro, el médico de Ai. Busca a quien mandó matar a su
  madre. Actor. Frío, pocas palabras («Qué chapuza», 雑だな, ep. 3,
  16:59). Pero hace el vídeo que salva a Akane (ep. 7) y baila con las
  barras de luz para animar a Kana (ep. 11) ✅ ([Game Rant](https://gamerant.com/oshi-no-ko-fulfilling-dreams/)).
  Estrella en el **ojo derecho**.
- **Aspecto** (render oficial, P·23): rubio con flequillo largo, ojos
  azules, uniforme de Yōtō (chaqueta azul, corbata roja, pantalón gris).
- **Voz:** Takeo Ōtsuka (JA), Jack Stansbury (EN), **Manuel Carmona**
  (LAT, adolescente; Crunchyroll lo acreditó como «Mani») ✅; de niño,
  Stefanie Izquierdo; de bebé, Ana Alvarado ✅ (Doblaje Wiki + ANMTV).

### Secundarios útiles
- **Taishi Gotanda (五反田泰志)**, director de cine: brusco, cínico,
  sabe todo del oficio. Maestro de Aqua ✅ ([DualShockers](https://www.dualshockers.com/oshi-no-ko-director-taishi-gotanda/),
  [wiki](https://oshinoko.fandom.com/wiki/Taishi_Gotanda)). Explica
  castings (ep. 1, 43:15 y 47:26). Su «¡Qué época!» es meme. En la T3
  preside la prueba de *La mentira de 15 años* y elige a Ruby.
  **Su aspecto** (diseño oficial, P·24): pelo castaño largo y
  despeinado, barba de tres días, chaqueta azul noche `#2E3150` sobre
  camiseta oscura, vaqueros. En el tráiler 2 acaricia la cabeza de
  Aqua niño en un banco del parque ([0:19](https://www.youtube.com/watch?v=gKWEUJ4r5do&t=19)) ✅.
  Voz latina: **Carlo Vázquez** ✅.
- **Pieyon (ぴえヨン)**: YouTuber de fitness con **cabeza de pollito**,
  ex bailarín profesional y coreógrafo (ep. 10, 05:19). Entrena a B小町:
  «¡10 cuestas más!» (05:47). Su canción: «Pieyon Boot Dance» (ep. 5).
  Aspecto (P·25): cuerpo de culturista, bañador azul, cabeza de
  pollito amarillo. Voz latina: **Ángel Mota** ⚠️ (Doblaje Wiki;
  Crunchyroll lo nombra sólo entre las voces adicionales).
- **Miyako Saitō**: la presidenta de Ichigo Production, la que ficha a
  todas (ep. 9, 01:42). Aspecto (P·26): pelo largo rosado, vestido
  granate y rebeca rosa. En el opening sale trabajando con un portátil
  ([1:11](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=71)). Voz latina:
  **Rosa María Martínez** ✅.

---

## 10 · Poses analizadas (con la imagen donde se ve)

Sólo se describen **imágenes que se miraron de verdad** (punto 3.1).
Para escenas del anime sin fotograma, se dice qué pasa, no la pose.

### Kana
| Imagen | Postura | Manos | Mirada y gesto | Sirve para |
|---|---|---|---|---|
| `bg19` | de frente, cuerpo girado | **índice derecho apuntando a cámara** (guante rosa) | boca abierta, grito alegre, micro de diadema | **animar** |
| `bg12` | inclinada hacia delante | micro en la derecha, **índice izquierdo arriba** | risa abierta, ojos grandes | **presentar** |
| `bg20` | de pie, cuerpo entero | un índice junto a la cara, el otro señalando al lado | sonrisa con dientes, pícara | **explicar** |
| `bg5` | medio cuerpo | micro y una «V» | ojos cerrados, carcajada | **celebrar** |
| `bg11` | primer plano | — | sonrisa tranquila, sombrerito | **saludar** |
| `bg2` | en grupo | manos en corazón | sonrisa | celebrar |
| ep. 3, 01:58 | (escena) | — | «¡Qué asco!» | **regañar** |
| ep. 11, 07:41 | (escena) | — | decisión, emoción | **animar** |
| **P·9** (animador, ep. 5) | de frente, medio cuerpo | **índice derecho arriba**, izquierda relajada | seria, un poco sonrojada | **explicar** ✅ |
| **P·10** (animador, ep. 11) | escorzo hacia cámara | **índice a cámara**, guante rosa | boca abierta, grito alegre | **animar** ✅ |
| **P·8** (animador, ep. 6) | de pie, boina | «V» con las dos manos | sonrisa suave | **saludar** ✅ |
| **V·5** · [OP 0:35](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=35) | sentada, boina | mano en la mejilla, codo en la rodilla | sonrisa ladeada | **pensar** ✅ |
| **V·17** · [ep. 11, 0:08](https://www.youtube.com/watch?v=S-UmqvA7uR8&t=8) | cantando, coletitas | **los dos índices junto a la cara**, guantes rosa | boca abierta | **presentar** ✅ |
| **O·18** (avance T2, ep. 15) | medio cuerpo | **guion en la mano izquierda** | sonrisa amplia | **#castings** ✅ |
| **O·15** (ep. 11) | primer plano | **enseña el móvil** con un post | sorpresa | **#redes** ✅ |
| Key visual T1 de Crunchyroll ([1000×1415](https://a.storyblok.com/f/178900/1000x1415/4edef43ef1/oshi-no-ko-visual.jpg)) | medio cuerpo, boina | **guion morado abierto** en las manos | **boca muy abierta, gritando** | **#castings, regañar** ✅ |
| [San Valentín 2026, 0:05](https://www.youtube.com/watch?v=pZSm3lQQqok&t=5) | primer plano, lazo negro | **muerde un bombón** | ojos grandes, sorprendida | **celebrar** ✅ |

### MEM-cho
| Imagen | Postura | Manos | Mirada y gesto | Sirve para |
|---|---|---|---|---|
| `bg19` | a la derecha, inclinada | **palma abierta hacia cámara** | guiño, boca abierta | **saludar** |
| `bg12` | abajo a la izquierda | mano en «L» bajo la barbilla | cara «:3», ojos azules | **pensar, explicar** |
| `bg20` | cuerpo entero, pierna atrás | puños arriba como garras | boca abierta | **celebrar** |
| `bg13`, `bg16` | primer plano | dedo en la mejilla | sonrisa | presentar |
| ep. 7, 11:16 | (escena) | — | presume de datos | **explicar** |
| **O·6** (canal oficial, 100.820 suscr.) | chibi, de frente | **brazos abiertos, palmas a cámara** | boca abierta, feliz | **celebrar** ✅ |
| **V·4** · [OP 0:33](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=33) | de pie en una azotea | **brazos arriba** | ojos cerrados, risa | **celebrar** ✅ |
| **V·16** · [ep. 11, 0:07](https://www.youtube.com/watch?v=S-UmqvA7uR8&t=7) | de frente, medio cuerpo | **las dos manos en «pistola», índices a cámara** | sonrisa, micro de diadema | **animar** ✅ |
| **V·19** · [directo, 0:05](https://www.youtube.com/watch?v=TvIOIATbUYE&t=5) | sentada en su silla gamer | índice en la barbilla | boca abierta, saluda | **saludar, presentar** ✅ |
| **P·13** (BD vol. 6, Hirayama) | sentada con las piernas cruzadas | manos en los tobillos | guiño, lengua fuera | **presentar** (su nombre gigante detrás) ✅ |
| **P·14** (Mengo) | de rodillas, saltando | un brazo arriba | risa | **#redes** (insignias de verificada) ✅ |
| Key visual T1 de Crunchyroll ([1000×1415](https://a.storyblok.com/f/178900/1000x1415/4edef43ef1/oshi-no-ko-visual.jpg)) | medio cuerpo, jersey verde | **brazo arriba con el móvil: selfie**, la otra mano junto a la cara | guiño | **#redes** (la pose del concepto A) ✅ |

### Ruby
| Imagen | Postura | Manos | Mirada y gesto | Sirve para |
|---|---|---|---|---|
| `bg19` | a la izquierda | **dos «V» bajo la barbilla** | sonrisa de dientes, estrella en el ojo | **celebrar** |
| `bg12` | medio cuerpo | índices en las mejillas | **lengua fuera**, pícara | **pensar, bromear** |
| `bg20` | cuerpo entero, dando un paso | «V» junto al ojo | boca abierta | **presentar** |
| `bg9` | primer plano | «V» | guiño | saludar |
| ep. 1, 23:34 | (escena, bebé) | — | enfado cómico | **regañar** |
| **V·2** · [OP 0:25](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=25) | de tres cuartos, sudadera | **índice en los labios** | sonrisa pícara, estrella | **«shh», secreto** ✅ |
| **P·17** (pi ro ri) | de frente, traje rojo | **las dos manos abiertas a cámara**, guantes negros | guiño | **invitar** ✅ |
| **P·18** (wiki) | primer plano | **corazón con las manos** | guiño con estrella | **celebrar** ✅ |
| **P·20** (KV T3) | de pie en un plató con croma | micro en la mano | mirada a cámara | **#en-directo, #castings** ✅ |

### Ai
| Imagen | Postura | Manos | Mirada y gesto | Sirve para |
|---|---|---|---|---|
| key visual (TheFabi8A) | escenario, cuerpo en diagonal | **micro en la derecha, índice izquierdo a cámara** | **guiño**, boca abierta, estrella | **presentar, en directo** |
| fan art (mismo repo) | de frente | micro y dedo a cámara | guiño y lengua fuera | referencia |
| **P·1** (KV T1-2, oficial) | escenario, cuerpo en diagonal | micro en la derecha, **índice izquierdo a cámara** | guiño, boca abierta | **presentar, en directo** ✅ |
| **P·2** (KV T1, oficial) | **de espaldas**, en un círculo de luz, ante un mar de barras rojas | **brazo derecho arriba, índice al cielo** | — | portada, «¡aquí estoy!» ✅ |
| **P·3** (animador) | escorzo | **índice a cámara**, micro | sonrisa | **animar** ✅ |
| **V·6** · [OP 0:57](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=57) | cantando en una escalera de luz | micro a la boca | alegre | **#en-directo** ✅ |
| Fotograma del ep. 1 de Crunchyroll ([1920×1080](https://a.storyblok.com/f/178900/1920x1080/e768593236/oshi-no-ko-season-1.png)) | primer plano, sudadera blanca | **«V» junto a la cara** | **guiño con la lengua fuera**, estrella en el ojo; fondo de conejos y huellas | **saludar, bromear** (su pose más famosa) ✅ |

### Akane
| Imagen | Postura | Manos | Mirada y gesto | Sirve para |
|---|---|---|---|---|
| `bg12` | detrás, de uniforme escolar | mano en el pecho | seria, mirando de lado | **pensar, escuchar** |
| **V·12** · [tráiler 2, 0:40](https://www.youtube.com/watch?v=gKWEUJ4r5do&t=40) | de pie, camiseta celeste | **guion rojo abierto** | concentrada, habla | **#castings** ✅ |
| **P·21** (ep. 7) | primer plano | — | **estrellas en los ojos** (imita a Ai) | actriz genio ✅ |
| **P·27** (Mengo) | medio cuerpo | **«V» sobre el ojo**, como Ai | sonrisa | imitar ✅ |
| **P·22** (render) | de pie, vestido azul | se coge la falda | tímida | recorte ✅ |
| [Mensaje especial, 0:03](https://www.youtube.com/watch?v=L-ZNenzreyU&t=3) (ilustración oficial, 2026) | medio cuerpo, cabeza un poco ladeada | **mano derecha en el pecho** | sonrisa suave, mirada a cámara | **presentar, saludar** ✅ |
| [Halloween 2025, 0:07](https://www.youtube.com/watch?v=wUgdw7EQmhc&t=7) | primer plano, disfraz de bruja | — | **guiño** y mejillas rojas | **bromear, celebrar** ✅ |
| [San Valentín 2026, 0:03](https://www.youtube.com/watch?v=pZSm3lQQqok&t=3) | primer plano, junto a Kana | **muerde un bombón** con la mano en la boca | ojos entornados | **celebrar** (con Kana, 0:09) ✅ |
| [Año Nuevo 2025, 0:05](https://www.youtube.com/watch?v=DUdhJfJeAaQ&t=5) | sentada, kimono celeste, flor en el pelo | algo en brazos | sonrisa abierta, dentro de un círculo | **saludar** («あけましておめでとうございます», 0:10) ✅ |
| [Día del Mar 2026, 0:07](https://www.youtube.com/watch?v=vRrwzroLO9Y&t=7) | tumbada junto a MEM, hibisco amarillo | — | sonrisa tranquila | **descansar**, cierre «HAPPY SUMMER TIME!» (0:18) ✅ |
| Key visual T1 de Crunchyroll ([1000×1415](https://a.storyblok.com/f/178900/1000x1415/4edef43ef1/oshi-no-ko-visual.jpg)) | de tres cuartos, detrás | **móvil en la mano** | seria, de lado | **#redes** ✅ |

**Aqua** (segunda pasada): **P·23** render de uniforme, mano en la nuca;
[OP 0:18-0:22](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=18) con
sudadera negra en un escenario vacío y primer plano con ojos cerrados;
[tráiler 2, 0:48](https://www.youtube.com/watch?v=gKWEUJ4r5do&t=48)
sonriendo de lado. Sigue sin servir de anfitrión alegre. El visual
«side Aqua» de la T3: [noticia ANN](https://www.animenewsnetwork.com/news/2025-03-22/oshi-no-ko-anime-3rd-season-reveals-aqua-visual-video/.222695).

---

## 11 · Vestuario (lo que todos reconocen)

**Uniforme nuevo de B小町** (Japan Idol Festival, ep. 11), visto en
`bg19` y `bg12`:
- Chaqueta roja de manga corta con **capita** (`#C41E34`).
- **Chorrera blanca** con **broche rojo** (Kana), lazo negro (Ruby, MEM).
- Borde de la capa con una **cinta blanca de rombos verdes** (MEM).
- Falda negra; la de Ruby acaba en **picos blancos**. MEM con pantalón.
- Guantes: **rosa** (Kana), **negros** (Ruby).
- Cabeza: **Kana, sombrerito de copa negro**; **Ruby, lazo negro** en
  la coleta de lado; **MEM, cuernos negros de diablilla** y lazo (los
  lleva en todas las ilustraciones miradas).
- Visto también en el clip oficial del ep. 11 (V·16-18,
  [0:06-0:09](https://www.youtube.com/watch?v=S-UmqvA7uR8&t=6)): capa
  roja con cinta blanca de dibujos verdes, micrófono de diadema, **Kana
  con dos coletitas y el sombrerito**, guantes rosa (Kana) y negros
  (Ruby); **MEM sin guantes**, con pulseras (una de cordón negro) ✅.

**Ai:** vestido **fucsia de volantes** con cinturón negro, guantes rosa,
**horquilla de conejito** con estrellas en el pelo índigo (key visual
mirado; y guías de cosplay ✅ [Sketchok](https://sketchok.com/anime/oshi-no-ko/how-to-draw-ai-hoshino-from-oshi-no-ko-in-her-idol-outfit/),
[YesStyle](https://www.yesstyle.com/blog/2023-07-05/idol-worthy-looks-inspired-by-oshi-no-ko-persona-investigator/)).

**Traje de «POP IN 2»** (antes lo llamé «San Valentín»; **corregido**:
los renders oficiales de la wiki se llaman «…Anime-POP IN 2», P·11, 15
y 19, y coinciden con `bg20`): Ruby, vestido rojo de lunares blancos
con lazo negro y botas blancas; Kana, **boina blanca**, blusa con lazo
amarillo y falda roja de lunares blancos con volantes; MEM, blusa
amarilla con lazo y pantalón corto rojo ✅.

**Uniforme del instituto Yōtō** (renders P·7, 16, 22, 23): chaqueta azul
marino `#302F57`, camisa blanca, **lazo rosa-granate `#802D57`** (Kana),
falda gris plisada `#B5B4B1`, calcetines blancos altos y mocasines.
Kana lleva **boina azul marino**; MEM, chaleco negro sobre la camisa;
Aqua, corbata roja y pantalón gris ✅.

**Trajes de la T3** («Bのリベンジ», ep. 25,
[0:19](https://www.youtube.com/watch?v=5B-ZPcq8KxQ&t=19), V·26): Kana
con **dos moños y lazos rojos**, blusa blanca de hombros caídos y falda
globo; MEM con un **volante amarillo** al cuello; Ruby con lazo rosa.

**MEM en casa** (sus directos y el tráiler 2, V·13 y V·19): jersey
turquesa de hombros caídos (tráiler) o camisón verde menta con diadema
lila («MEMちょの部屋»).

**Akane:** uniforme escolar: chaleco negro, camisa blanca, falda gris
plisada (`bg12`).

**Lo icónico:** el **uniforme rojo con capita** del festival para las
tres, y el **vestido fucsia con el conejito** para Ai.

---
## 12 · Doblaje latino

> [!important] Segunda pasada: todo pasado por tres fuentes
> 1. **Doblaje Wiki por su API** ([página](https://doblaje.fandom.com/es/wiki/Oshi_no_Ko)):
>    ficha técnica, reparto completo, datos de interés y errores.
> 2. **ANMTV**, los dos artículos abiertos de verdad
>    ([T1](https://www.anmtvla.com/2026/07/oshi-no-ko-doblaje-de-la-primera.html),
>    [T2](https://www.anmtvla.com/2026/08/oshi-no-ko-doblaje-de-la-2-temporada-ya.html)).
> 3. **Crunchyroll**: su anuncio del elenco, leído por la API de noticias
>    (`cr-news-api-service…/v1/es-419/stories?slug=…`), porque la web
>    sólo carga con JavaScript ([anuncio](https://www.crunchyroll.com/es/news/announcements/2026/7/14/elenco-staff-doblaje-latino-oshi-no-ko-temporada-1)).
> 4. Contraste: la ficha de **ANN** (idioma ES) en su copia de GitHub.

### 12.1 · La producción ✅

| Dato | Valor | Fuentes |
|---|---|---|
| Estudio | **Audiomaster Candiani** (México) | Doblaje Wiki + ANMTV + Crunchyroll ✅ |
| Dirección | **Jorge Reyes** | las tres ✅ |
| Adaptación | **Luis Fernando Gurrea** | Doblaje Wiki + Crunchyroll ✅ (nuevo) |
| Mezcla | **Alejandro Yáñez** (Crunchyroll añade a Jorge Reyes) | Doblaje Wiki + Crunchyroll ✅ (nuevo) |
| Producción | Karina Escalante, Luis Espinosa, Jahaziel Rodríguez, Rodolfo Olivares | Doblaje Wiki + Crunchyroll ✅ (nuevo) |
| Grabación | inicios de 2026; guiones de Crunchyroll en inglés, audio japonés de referencia | Doblaje Wiki ⚠️ (una fuente) |
| T1 en Crunchyroll | **14-jul-2026** (11 ep.) | Doblaje Wiki + ANMTV + Crunchyroll ✅ |
| T2 en Crunchyroll | **4-ago-2026** (13 ep.) | Doblaje Wiki + ANMTV ✅ |
| T3 | **sin doblaje latino anunciado** («próximamente» en Doblaje Wiki; «aún no se ha anunciado» en ANMTV) | ✅ |
| Canciones | **se dejaron en japonés** (sólo el doblaje alemán cantó las de B小町) | Doblaje Wiki ⚠️ |

### 12.2 · Las voces (cada nombre con dos fuentes)

| Personaje | Voz latina | Fuentes | Estado |
|---|---|---|---|
| **Ai Hoshino** | **Stephanie Filigrana** (Erika Kose en *Kaguya-sama*) | DW + ANMTV + CR + ANN | ✅ |
| **Aqua** (joven) | **Manuel Carmona** (Crunchyroll lo acreditó «Mani») | DW + ANMTV + CR + ANN | ✅ |
| Aqua (niño) · (bebé) | **Stefanie «Stefi» Izquierdo** · **Ana Alvarado** | DW + ANMTV + CR | ✅ (antes dudoso) |
| Goro Amemiya | **Óscar López** | DW + ANMTV + CR | ✅ (nuevo) |
| **Ruby** (joven) · niña · bebé | **Polly Huerta** · **Lilian Vela** · **Lucía Suárez** | DW + ANMTV + CR | ✅ |
| Sarina Tendōji | **Jean Bautista** | DW + ANMTV + CR | ✅ (nuevo) |
| **Kana Arima** | **Ginette Zavala** | DW + ANMTV + ANN | ✅ |
| **Akane Kurokawa** | **María García** | DW + ANMTV + ANN | ✅ |
| **MEM-cho** | **Paulina García** | DW + ANMTV + ANN (CR la pone en «voces adicionales» de la T1: MEM sale desde el ep. 5) | ✅ |
| Miyako Saitō | **Rosa María Martínez** | DW + ANMTV + CR + ANN | ✅ (antes dudoso) |
| Taishi Gotanda | **Carlo Vázquez** | DW + ANMTV + CR + ANN | ✅ (antes dudoso) |
| Madre de Gotanda | **Magda Giner** | DW + ANMTV + ANN | ✅ (**corregido**, ver abajo) |
| Ichigo Saitō | **Ferso Velázquez** | DW + CR | ✅ (nuevo) |
| Frill Shiranui | **Andrea Soto** | DW + ANMTV + ANN | ✅ (antes dudoso) |
| Minami Kotobuki | **Fernanda Ornelas** | DW + ANMTV + ANN | ✅ (nuevo) |
| Yuki Sumi | **Denisse Leguizamo** | DW + ANMTV + ANN | ✅ (antes dudoso) |
| Nobuyuki Kumano | **Armando Corona** | DW + ANMTV | ✅ (**corregido**: ANN dice Armando Ibarrola) |
| Kengo Morimoto · Masaya Kaburagi | **José Luis Piedra** · **Galo Balcázar** | DW + ANMTV | ✅ (nuevo) |
| Yoriko Kichijōji | **Valentina Souza** | DW + ANMTV + ANN | ✅ (nuevo) |
| Director de *Love Now* | **Alberto Meléndez** | DW + ANMTV | ✅ (nuevo) |
| Melt Narushima · Sumiaki Raida | **Dión González** · **Brandon Montor** | DW + ANMTV | ✅ (nuevo) |
| Abiko Samejima (T2) | **Sofía Baltazar** | DW + ANMTV | ✅ (antes dudoso) |
| Toshirō Kindaichi (T2) | **Carlos Hernández** | DW + ANMTV | ✅ (antes dudoso) |
| Taiki Himekawa (T2) | **Jorge Valladares** | DW + ANMTV | ✅ (antes dudoso) |
| GOA · Norio Mita · Mei Adashino (T2) | **Dave Ramos** · **Tommy Rojas** · **Susana Cohe** | DW + ANMTV | ✅ (nuevo) |
| Hikaru Kamiki (T2, ep. 22 y 24) | **Daniel Lacy** | DW (ANMTV T2 no lo nombra; MyAnimeList no respondió) | ⚠️ (una fuente) |
| Pieyon | **Ángel Mota** | DW; CR lo pone en «voces adicionales» de la T1 sin papel; ANMTV no lo nombra | ⚠️ (el papel, una fuente) |
| Madre de Kana | **Ellie Rojo** | DW; CR la pone en «voces adicionales» de la T1 sin papel | ⚠️ (el papel, una fuente) |

**Corrección importante.** La primera pasada decía que **Magda Giner**
y **Gracia Comitre** eran del doblaje de España y que «no se usaran».
**Magda Giner sí es del latino** ✅: dobla a la **madre de Gotanda**
(Doblaje Wiki + ANMTV + ANN). **Gracia Comitre** sólo aparece en ANN
como segunda voz de Kana; ni Doblaje Wiki, ni ANMTV, ni Crunchyroll la
nombran ⚠️: no usarla hasta confirmarla.

**Dato curioso, confirmado** ✅: la Akane latina **es la misma actriz
que la Bocchi latina**. Su ficha personal de Doblaje Wiki
([María García](https://doblaje.fandom.com/es/wiki/Mar%C3%ADa_Garc%C3%ADa))
pone en su galería a Hitori «Bocchi» Gotoh y a Akane Kurokawa, junto a
Kaede Kayano (*Assassination Classroom*) y Tsireya (*Avatar: El camino
del agua*).

### 12.3 · Frases propias del doblaje latino (textuales)
**Clips oficiales doblados: no hay.** Lo busqué de cinco maneras en la
segunda pasada:
- **Canal de Crunchyroll en Español** (búsqueda dentro del canal y sus
  *shorts*, con yt-dlp): sólo hay clips de la **T3**, de febrero-abril
  de 2026, que no tiene doblaje latino (p. ej. [«¡Akane descubrió toda
  la verdad!», 20-mar-2026](https://www.youtube.com/watch?v=Gdigwu7pJyY)).
- **Anuncio del elenco de Crunchyroll** (API de noticias): sólo texto
  y dos imágenes, ningún vídeo.
- **Doblaje Wiki**: la página no tiene muestras de audio y la búsqueda
  de archivos no da ninguno de la serie.
- **Subidas de fans del audio oficial** en YouTube: existen
  ([Otaku en Linea, 16-jul-2026](https://www.youtube.com/watch?v=x3gKIAtsfLc),
  [voz de Ai, 15-jul-2026](https://www.youtube.com/watch?v=SaEMd_pdLT8),
  [clip, 14-jul-2026](https://www.youtube.com/watch?v=qVLvI7dBffM)),
  pero **no tienen subtítulos** (ni automáticos) y YouTube no deja
  bajar el audio. En X, los posts probados no tenían vídeo; TikTok da
  error en yt-dlp.
- **Subtítulos latinos en GitHub** («Producciones Ichigo», «Frutilla
  Producciones», archivos .ass): nada.

Lo textual que sí hay sale de **Doblaje Wiki** (una fuente ⚠️, pero son
citas literales). El **minuto** lo saqué cruzando cada escena con los
subtítulos japoneses de la emisión (NanakoRaws); en Crunchyroll puede
moverse ±1 minuto:
- **Gotanda a Aqua (T1, ep. 2 · 20:23-20:29):** «**Pero tú nunca podrás
  ser tu mamá.**» (Doblaje Wiki lo marca como error: en japonés dice
  «だけど お前はアイにはなれないし / アイも お前にはなれない», «pero tú no
  puedes ser Ai, ni Ai puede ser tú».)
- **Aqua ante Ruby y Minami (T1, ep. 4 · 19:52-19:57):** «**Mi favorita
  siempre fue y siempre será Ai Hoshino.**» (En japonés: «俺の最推しは
  今も昔もアイだけだし», sin el apellido.)
- **La agencia se llama «Producciones Ichigo» en la T1 y «Frutilla
  Producciones» en la T2** (error de continuidad). Para la lámina,
  **«Producciones Ichigo»** (T1).
- **Twitter se dice «X»** en el doblaje (el original es anterior al
  cambio de nombre). En #redes, decir «X», no «Twitter».
- El doblaje usa **modismos y referencias de internet latinoamericanas**,
  como su serie hermana *Kaguya-sama* (que se dobló en otro estudio,
  VSI México, según Doblaje Wiki).

Más frases textuales del doblaje: no las hay con fuente. Para
rotular una frase de Kana, Ruby o MEM en latino, **escucharla antes en
Crunchyroll** (T1 y T2, con doblaje desde el 14-jul y el 4-ago-2026).

### 12.4 · Reacciones y vídeos sobre el doblaje
- «The Latin Spanish dub of Oshi no Ko is finally here: meet the voice
  cast» ([KennedyCosplayAlan, 5:14](https://www.youtube.com/watch?v=5BcwY6jUxno))
  y su versión de la T2 ([5:01](https://www.youtube.com/watch?v=0H8ZqcSNdtM)).
- «I hate the dubbing of Oshi no Ko» y «The Oshi no Ko Latin Spanish dub
  case» ([Nerdwork](https://www.youtube.com/watch?v=7E6WpqqCuNY),
  [Nerdwork 2](https://www.youtube.com/watch?v=AaPMDlpG7yU)): opiniones
  mixtas, como ya decía la primera pasada
  ([X, SlimperSuprime](https://x.com/SlimperSuprime/status/2077560351114076657)).
- Antes del oficial hubo **fandubs**: el ep. 1 por Sparrow Doblaje
  Studio ([Patreon](https://www.patreon.com/posts/oshi-no-ko-1-114383809)),
  BLANSSTER ([«La muerte de Ai»](https://www.youtube.com/watch?v=x0nvQBo1HKo)),
  Yerxfandubs y muchas versiones de «Idol» en español (§13).
- **Crunchyroll tiene también el castellano de España** (doblaje aparte;
  Doblaje Wiki lo marca «Doblajes disponibles en España»). No mezclar.

## 13 · Música

Fuente: fichas de ANN (T1, T2, T3).

| Temporada | Opening | Ending | Ambiente (según la escena) |
|---|---|---|---|
| T1 (2023) | **«Idol» (アイドル), YOASOBI** | «Mephisto» (メフィスト), Queen Bee | **visto** (V·1-10): el opening es pop rápido, puntos LED rosa, ojos con estrella, logo en mincho; el ending es **oscuro y en panorámica** (2,35:1), un conejo de peluche colgado de hilos, cada personaje sobre su color plano |
| T2 (2024) | «Fatale», GEMN | «Burning», Hitsujibungaku | teatro, rivalidad |
| T3 (2026) | «TEST ME», CHANMINA | «Serenade» (セレナーデ), natori | la película y el pasado de Ai |

- **«Idol» es la canción más rápida en llegar a 1.000 millones de
  reproducciones** en la lista de Oricon ([ANN](https://www.animenewsnetwork.com/news/2025-11-25/oricon-yoasobi-idol-is-fastest-song-to-top-1-billion-times-streamed/.231400)).
- **Canciones de B小町:** «Sign wa B», «STAR☆T☆RAIN», «HEART's♡KISS»
  (versiones de Ai en el ep. 1 y nuevas del grupo en el 11), **«POP IN
  2»** (T2), **«B no Revenge»** (T3, ep. 25).
  **Segunda pasada** (ficha de B-Komachi en la wiki + títulos del canal
  oficial ✅): además **«Say What?»**, **«深海52Hz» (*Deep Sea 52Hz*)**,
  y **una canción propia para cada una**: **«チェキチェキ LOVE ME»** (Ruby),
  **«MY WILL»** (Kana) y **«キミインプレッション» (*Kimi Impression*)**
  (MEM) ([canal oficial](https://www.youtube.com/@anime_oshinoko/videos)).
  El canal publica **vídeos de práctica de «call»** (lo que grita el
  público) para la gira «B小町 Live Tour 2026» (p. ej. [«POP IN 2»](https://www.youtube.com/watch?v=FsnRIQgdFCg)).
- **«B no Revenge» es un «falso opening»:** el director Daisuke
  Hiramaki cuenta que en el primer episodio de la T3 quisieron
  «engañar al público» con esa canción de B小町 montada como si fuera
  la apertura nueva, con planos de todos los personajes
  ([entrevista de Newtype en Crunchyroll News, 28-abr-2026](https://www.crunchyroll.com/es/news/interviews/2026/4/28/oshi-no-ko-anime-director-entrevista)) ✅
  (y se ve en el clip oficial, V·26). El opening real de la T3 es de
  **Ciao Nekotomi** y el ending, de **Naoya Nakayama** (misma entrevista).
- **«45510»**: relato corto de Akasaka que sirvió de base a «Idol»; el
  número es la contraseña del blog de B小町 ([wiki](https://oshinoko.fandom.com/wiki/45510)).
  Sale en el opening, en una matrícula ([1:10](https://www.youtube.com/watch?v=PgBvV9ofjmA&t=70)).
- **Canciones de Kana:** «Piman Taisou» (su éxito de niña) y
  «Full moon...!» (ep. 9).
- Canción de **Pieyon**: «Pieyon Boot Dance» (ep. 5).
- Banda sonora: **Takurō Iga**.
- **Para cada lámina:** #en-directo suena a «Sign wa B» (el directo de
  Ai en la tele); #redes a «POP IN 2» (el vídeo del grupo); #castings a
  la T3 («TEST ME»).
- **Versiones en español de «Idol»** (útiles para un servidor de canto):
  [David Delgado](https://www.youtube.com/watch?v=nS2v4MHh0iM),
  [MoonTsuki15](https://www.youtube.com/watch?v=ql7r0MhWLXw),
  [Kira0loka](https://www.youtube.com/watch?v=87AvK83BIkE),
  [Snake](https://www.youtube.com/watch?v=dACPWP4Y0f8),
  [Eiko-tan con AlphaDubs](https://soundcloud.com/eikotan/yoasobi-idol-eiko-tan-cover-espanol).

---

## 14 · Vídeos

Canal oficial: [@anime_oshinoko](https://www.youtube.com/@anime_oshinoko)
(496 vídeos listados con yt-dlp el 24-sep-2026).
**Segunda pasada:** los **52 enlaces de YouTube** de esta biblia
existen (comprobados uno a uno con el oEmbed de YouTube al terminar,
24-sep-2026) ✅. Los que miré fotograma a fotograma, con minuto, están
en §4.1 y en `hojas/video_01.jpg`.

**Mirados en la segunda tanda** (por *storyboard*, porque
`fotogramas.py` da «Sign in to confirm you're not a bot»):

| Vídeo oficial | Duración | Lo que sirve (minuto) |
|---|---|---|
| [Mensaje especial de Akane, gira B小町 2026](https://www.youtube.com/watch?v=L-ZNenzreyU) | 0:57 | formato «mensaje especial» con subtítulos (0:01); Akane mano en el pecho (0:03) |
| [推しセリフ #05, Manaka Iwami](https://www.youtube.com/watch?v=VrIF12uKg1Y) | 1:23 | escena de *Tokyo Blade* con «絶対に負けない» (0:19-0:31); shikishi firmado (0:33) |
| [Visita al estudio de doblaje n.º 6](https://www.youtube.com/watch?v=izzRjaUZig4) | 14:32 | puerta STUDIO 1 (0:00), cabina (1:44), cartela rosa (8:40), mesa de mezclas (9:24) |
| [HAPPY HALLOWEEN 2025, Akane](https://www.youtube.com/watch?v=wUgdw7EQmhc) | 0:16 | guiño (0:07), tarjeta «Happy Halloween» (0:12) |
| [HAPPY VALENTINES DAY 2026, Kana y Akane](https://www.youtube.com/watch?v=pZSm3lQQqok) | 0:23 | las dos con un bombón (0:03-0:19), corazón rojo (0:13) |
| [HAPPY NEW YEAR 2025, Akane](https://www.youtube.com/watch?v=DUdhJfJeAaQ) | 0:15 | «謹賀新年» en círculo rojo (0:00); Akane en kimono (0:05) |
| [Día del Mar 2026, Akane y MEM](https://www.youtube.com/watch?v=vRrwzroLO9Y) | 0:23 | las dos tumbadas con flores (0:02-0:14), «HAPPY SUMMER TIME!» (0:18) |

Las felicitaciones de fiestas (Halloween, San Valentín, Año Nuevo,
verano) salen **cada año** en el canal con uno a tres personajes: son
ilustraciones oficiales con poses vivas. **La wiki guarda la imagen
entera** (API, tamaño real): [Akane Halloween 2025](https://static.wikia.nocookie.net/oshi_no_ko/images/c/cd/Akane_Halloween_2025.png)
(2048×1426), [Kana y Akane San Valentín 2026](https://static.wikia.nocookie.net/oshi_no_ko/images/7/74/Kana_%26_Akane_Valentine_2026.png)
(2000×1395), [Akane Año Nuevo 2025](https://static.wikia.nocookie.net/oshi_no_ko/images/d/d9/Akane_New_Year_2025.png)
(**4096×2906**), [Akane y MEM Día del Mar 2026](https://static.wikia.nocookie.net/oshi_no_ko/images/6/6c/Akane_%26_Mem-Cho_Marine_Day_2026.png)
(1000×707), [Kana, Akane y MEM Año Nuevo 2026](https://static.wikia.nocookie.net/oshi_no_ko/images/c/c2/Kana%2C_Akane_%26_Mem-Cho_New_Year_2026.png)
(1200×840), [MEM San Valentín 2024](https://static.wikia.nocookie.net/oshi_no_ko/images/f/fe/Mem-Cho_Valentine_2024.png)
(1200×849) y [B小町 San Valentín 2025](https://static.wikia.nocookie.net/oshi_no_ko/images/7/7d/B-Komachi_Valentine_2025.png)
(2048×1442). Sirven también de **fondos de pantalla oficiales** (punto
16 del encargo).

**Series del canal oficial que sirven a estos canales** (nuevas):
- **«MEMちょの【推しの子】NEWS»** (#01 a #28): **MEM-cho presenta las
  novedades del anime** delante de una pizarra negra con dibujos de
  neón ([#01, ene-2023](https://www.youtube.com/watch?v=DdiRyWNkYSc),
  [#28](https://www.youtube.com/watch?v=vxxb2ekatzI)). **Es, literalmente,
  un canal de «novedades» con MEM de anfitriona** → concepto A.
- **«MEMちょの部屋»** (#31 a #37): MEM en su cuarto, lee mensajes de
  fans ([#37, 1:29](https://www.youtube.com/watch?v=TvIOIATbUYE&t=89)).
- **«最新NEWS»**: noticiero dentro de la ficción
  ([0:03](https://www.youtube.com/watch?v=VjyCYUdmlnc&t=3)).
- **«アフレコ現場を深掘れ☆ワンチャン!!»** («Metidos en el estudio de
  doblaje»): visitas a la grabación de voces, con el reparto japonés
  ([ep. 1 con Rumi Ōkubo, MEM](https://www.youtube.com/watch?v=RNd2UWSImOw),
  [ep. 6 con Megumi Han y el director de sonido Takeshi Takadera](https://www.youtube.com/watch?v=izzRjaUZig4)).
  **Para un servidor de doblaje, oro.** **Segunda pasada: el n.º 6 ya
  lo miré entero** por *storyboard* (14:32, un cuadro cada 5 s): cabina
  de listones de madera, micro de condensador, Megumi Han hablando de su
  escena del ep. 30 y la sala de mezclas (detalle y minutos en §8.1,
  punto 16). Hay 8 entregas en el canal (n.º 1-8; la 7 con Manaka Iwami,
  [byWluteoKvk](https://www.youtube.com/watch?v=byWluteoKvk)).
- **Vídeos de «call»** para practicar lo que grita el público
  ([«POP IN 2»](https://www.youtube.com/watch?v=FsnRIQgdFCg)).
- **«B小町チャンネル!»**: las tres idols hacen retos como youtubers
  ([#7](https://www.youtube.com/watch?v=HFkpwHJECoc)).

| Vídeo | Para qué |
|---|---|
| [T3 PV 1](https://www.youtube.com/watch?v=WJnPGGzkX9Y) | pose y luz de la T3 |
| [T3 PV 2, con «TEST ME»](https://www.youtube.com/watch?v=JGYY6Pui5Kc) | ritmo, montaje |
| [Opening T3 sin créditos](https://www.youtube.com/watch?v=QgIQbeRzkkc) | fotogramas limpios |
| [Anuncio de la T3](https://www.youtube.com/watch?v=YMsDROPoe1o) | — |
| [Vídeo del visual «side Aqua»](https://www.youtube.com/watch?v=yPe5Mg2ahYk) | Aqua |
| [Anuncio para TV de la T3](https://www.youtube.com/watch?v=a506wjtia18) | — |
| [PV de fin de la T3 (anuncia la T4)](https://www.youtube.com/watch?v=YZc8gUB0Y-Q) | — |
| [Avance web del ep. 33](https://www.youtube.com/watch?v=A89c9EUbfvg) | — |
| [Directo oficial de novedades de la T3](https://www.youtube.com/watch?v=tfD5wA0zAII) | **un directo oficial** («第3期新情報解禁生放送», desde el festival Kantō Nōryō): idea para #en-directo |
| [Hirayama dibuja a Kana](https://www.youtube.com/watch?v=q4bzYqoFGvo) | **línea y color** |
| [Hirayama dibuja a Ai](https://www.youtube.com/watch?v=CYxj4xCcGmI) | línea y color |
| [«Llegó el doblaje latino, conoce las voces»](https://www.youtube.com/watch?v=5BcwY6jUxno) | voces latinas |

**Análisis en español** (autor comprobado por oEmbed ✅):
[«El lado oscuro de la industria» (Multiverso Otaku)](https://www.youtube.com/watch?v=s0uRTRITzxQ),
[«Oshi no Ko es maravilloso» (Shu Hoshino)](https://www.youtube.com/watch?v=Y9qroEAC6z0),
[**«Arima Kana: el sinónimo de fracaso en la industria» (Teici C)**](https://www.youtube.com/watch?v=UHsHyERB89Q),
[«Una crítica al entretenimiento» (Yez!)](https://www.youtube.com/watch?v=kE6I2RhIoPI).

**TikTok:** el baile de «Idol» es tendencia desde 2023 y sigue en 2026,
con cosplay de Ai ([TikTok, Idol dance](https://www.tiktok.com/discover/oshi-no-ko-idol-dance),
[TikTok, tendencia](https://www.tiktok.com/discover/oshi-no-ko-dance-trend)).

---

## 15 · Videojuegos

**【推しの子】Puzzle Star** (NHN desarrolla, KADOKAWA publica), para
iOS y Android, **desde el 25 de febrero de 2026** ✅
([Denfaminicogamer](https://news.denfaminicogamer.jp/news/260218q),
[KADOKAWA](https://group.kadokawa.co.jp/information/promotional_topics/article-14251.html)).
- Puzzle de unir bloques. **Pantalla de inicio con tu personaje
  favorito**, al que vistes con trajes, peinados y accesorios.
- **Voces** en las habilidades y en la pantalla de inicio.
- **«Tablero de colección»**: al ganar se completan escenas famosas del
  anime y se ven animadas.
- Cartas con dibujos **supervisados por Kanna Hirayama** ✅ ([GameWith](https://gamewith.jp/gamedb/12821/articles/39800),
  [KADOKAWA](https://www.kadokawa.co.jp/product/game2659/)).
- Reseñas: [GameFoliage](https://gamefoliage.com/2026/02/26/puzzle_star/),
  [Dengeki](https://dengekionline.com/article/202602/66916).
- **Segunda pasada: ya lo vi** ✅, en el vídeo oficial en que **MEM-cho
  juega a *Puzzle Star* en su directo** ([canal oficial, 20-abr-2026](https://www.youtube.com/watch?v=LmVk85v-O5w),
  *storyboard* cada ~5 s):
  - pantalla **vertical de móvil**, con la **pantalla de inicio con tu
    personaje favorito de pie en un cuarto** (MEM la tiene puesta,
    [0:39](https://www.youtube.com/watch?v=LmVk85v-O5w&t=39));
  - banner de gacha «スタートダッシュガチャ» ([0:59](https://www.youtube.com/watch?v=LmVk85v-O5w&t=59));
  - tablero de **bloques de colores de unir tres** con la carta del
    personaje arriba ([3:07](https://www.youtube.com/watch?v=LmVk85v-O5w&t=187));
  - **«STAGE CLEAR»** en rosa ([5:54](https://www.youtube.com/watch?v=LmVk85v-O5w&t=354));
  - modo **vestir y foto con marcos** ([7:03](https://www.youtube.com/watch?v=LmVk85v-O5w&t=423)).
  - En el mismo directo, lo que dice MEM va en su **rótulo naranja** y
    la explicación de una habilidad, en una **caja blanca de bordes
    redondos** ([2:37](https://www.youtube.com/watch?v=LmVk85v-O5w&t=157)).
- The Cutting Room Floor: no tiene página (juego móvil de 2026).

**Colaboración oficial con *IDOLM@STER Shiny Colors*** (2023-2024,
nueva) ✅: Ruby, Kana y MEM salieron como idols jugables (O·10-11;
cartas «In Red Ruby», «In White Kana», «In Yellow MEMCho» en la wiki).
**Su caja de diálogo** (O·10, 1922×1079): **ventana blanca translúcida
de esquinas redondas** con una **pestaña de nombre** arriba a la
izquierda («✦かな»), texto gris oscuro, botones «SKIP», «早送り×4 OFF»
y «^» (historial), sobre un fondo 3D de sala de ensayo con espejo. En
el cartel, la frase de Kana va en **dos franjas, roja con letra blanca
y blanca con letra roja**: «また……終わった人扱い / されちゃうかな»
(«¿otra vez me van a tratar como a una acabada?»), y su nombre en una
**placa azul marino** («有馬 かな»). Es una caja de videojuego real y
oficial con los personajes: **alternativa válida** al globo blanco.

**Juegos de fans en GitHub** (sólo curiosidad): un selector de
personajes estilo juego de lucha ([oshiNoKoSelector](https://github.com/ThomasRoR/oshiNoKoSelector))
y un juego en Ren'Py ([Chompita](https://github.com/Chompita/OSHI-NO-KO)).

---

## 16 · Lo que el fandom ama, y qué NO hacer

### Lo que todos reconocen
- **Kana y la barra blanca** (ep. 11, 07:41). La escena más querida.
- **«¡La niña genio que llora en 10 segundos!» / «Bicarbonato-chan»**.
- **Los gemelos bebés bailando** con barras de luz en el concierto de
  Ai y el vídeo viral (ep. 1, 38:52).
- **Gotanda: «¡Qué época!»** (時代だなあ) ✅ ([TV Tropes, memes](https://tvtropes.org/pmwiki/pmwiki.php/Memes/OshiNoKo)).
- **Ai y Hu Tao** (Genshin): misma seiyū, Rie Takahashi, y ojos raros.
- **Mamoru Miyano** como Kamiki: chistes con la Death Note.
- **El pelo de Aqua** en los visuales especiales: siempre hay burla.
- **«This shit is so ass»**: imagen de reacción de la serie, viral en
  2024 ([Know Your Meme](https://knowyourmeme.com/memes/this-shit-is-so-ass)).
- **Parodias del ending** con Getter Robo en Japón (TV Tropes).
- **Kana contra Akane**: el debate eterno de la «mejor chica»
  ([CBR](https://www.cbr.com/oshi-no-ko-kana-or-akane-best-girl/)).
- **«Bicarbonato-chan» se hizo real**: la marca de jabón Kaneyo sacó el
  bicarbonato «重曹ちゃん» con Kana de imagen (O·14; web oficial) ✅.
- **«こんめむ〜♪»**, el saludo de MEM en su canal (§8.1) ✅.
- **«45510»**, la contraseña del blog de B小町, escondida en el opening
  (§13) ✅.
- **Reddit** (Arctic Shift, jul-ago 2026): lo más votado fueron fan art,
  cosplay de Kana y el **guion de *La mentira de 15 años* firmado por
  todo el reparto** ([hilo](https://reddit.com/r/OshiNoKo/comments/1vhzqqu/the_15_year_lie_script_with_all_of_the_cast/));
  del doblaje latino **no hay hilos** en r/OshiNoKo esas semanas.

### Qué NO hacer (le parecería falso a un fan)
- **Estrellas de cinco puntas en los ojos.** En los ojos son de
  **seis** (V·1). *Corrección de la segunda pasada:* en las **cartelas
  y la decoración** la serie sí usa estrellas de **cinco** puntas
  redondeadas (O·19-21). La regla es: ojo = seis; adorno = cinco.
- **Corchetes rectos [ ].** Son **【 】**.
- **Estrella en el ojo equivocado:** Aqua derecho, Ruby izquierdo, Ai
  los dos. **Estrellas negras** sólo para la venganza.
- **Colores cambiados:** Kana es **pelo rojo corto y color blanco**;
  Ruby **rubia larga y color rojo**; MEM **rubia miel (limón sólo bajo
  focos), cuernos y color amarillo**; Ai **pelo índigo**, no rubio.
- **Escribir «Twitter»** o «Frutilla Producciones»: el doblaje latino
  dice **«X»** y, en la T1, **«Producciones Ichigo»** (§12.3).
- **Poner la letra del logo en gótica gruesa**: el logo es **mincho**
  con la «の» magenta (§7).
- **Tocar el final.** El manga acabó con la muerte de Aqua y el final
  fue muy criticado ([Dexerto](https://www.dexerto.com/anime/oshi-no-ko-manga-slammed-for-terrible-ending-2974344/),
  [Screen Rant](https://screenrant.com/oshi-no-ko-ending-good-bad-controversy/)).
  Nada de guiños a eso.
- **Usar el acoso a Akane (ep. 6).** Se basa en una tragedia real, la
  de la luchadora Hana Kimura ([Screen Rant](https://screenrant.com/oshi-no-ko-darkest-moment-real-tragedy-akane/),
  [Animehunch](https://animehunch.com/oshi-no-ko-episode-6-gets-criticized-for-replicating-deceased-hana-kimuras-cyberbullying-tragedy/)).
  En #redes, **nada de comentarios de odio** como decoración.
- **Jugar con la muerte de Ai** o ponerla «de fantasma». En #en-directo,
  Ai sale **cantando, viva, en un fotograma de la tele**.
- **Burlarse de la edad de MEM.** Es su herida, no un chiste para la
  lámina.

---

## 17 · Guía para describir el estilo a una IA de imagen

(Sólo para el dueño, con Firefly o Canva. Aquí no se generó nada.)

**Rasgos que nunca cambian**
- Ai: pelo largo **índigo** con reflejos violeta, ojos violeta con
  **estrella blanca de seis puntas en los dos**, horquilla de conejito.
- Ruby: pelo **rubio dorado** largo con coleta de lado y lazo negro,
  ojos rosa, estrella en el **izquierdo**.
- Kana: **media melena carmesí (`#83132C`) con flequillo recto**, ojos
  rojos, sin estrellas; a menudo **boina** (P·7-8). Es **bajita**
  (150 cm): la más baja junto a Ai (151).
- MEM-cho: **rubia miel (`#E2A144`) corta con flequillo recto**, ojos
  turquesa, **cuernos negros** de diablilla (P·16).
- Akane: media melena **azul violeta**, ojos azules, mirada seria.

**Estilo:** anime moderno de Doga Kobo. **Línea fina y limpia**, sombras
en dos tonos, brillos grandes en el pelo, **ojos enormes con muchos
colores y un toque de color claro sobre las pestañas** (Hirayama lo
explica en [Real Sound](https://realsound.jp/movie/2023/06/post-1345012_2.html)).
Luz de escenario con **destellos, bokeh y láseres**.

**Paleta:** la del punto 6.2 (rojo `#C41E34`, negro `#261C33`, blanco
`#F4EFEA`, rosa `#F16691`, noche `#222B32`).

**Palabras que ayudan:** *idol anime key visual, stage lights, lens
flare, bokeh, penlights, six-pointed star in the eye, clean cel shading,
Doga Kobo style, glossy hair highlights*.

**Palabras que lo estropean:** *realistic, 3D render, chibi, watercolor,
five-pointed star, horror, blood* (salvo que se quiera lo oscuro),
*generic anime girl*.

**Encuadre:** medio cuerpo, un poco desde abajo, personaje en diagonal
señalando a cámara (así están `bg19`, `bg12` y el key visual de Ai).

**Referencias de estilo (segunda pasada, todas oficiales):** P·1 (KV
de Ai: color y brillo), P·6 (B小町 en escenario), los **renders sobre
verde** P·4, 7, 11, 15, 16, 19, 22-26 (cuerpo entero, línea limpia,
para recortar o para que la IA copie proporciones), O·19 (cartela:
rombos y estrella negra), V·19-20 (el directo de MEM) y el **key
visual principal de la T1** de Crunchyroll (magenta `#E30182` con
destellos blancos y negros de cuatro puntas, todo el reparto con sus
objetos). **De pose:** MEM con el móvil en alto (key visual, selfie),
P·9 Kana (explicar), P·10 Kana (animar), O·6 y V·4 MEM (celebrar),
V·19 MEM (presentar), P·17 Ruby (invitar), V·2 Ruby («shh»), P·1 Ai
(en directo).

**Proporciones** (web oficial): Kana 150 cm, Ai 151, MEM 155, Ruby 158,
Akane 163. En un grupo, Kana es la más baja y Akane la más alta.

**Palabras extra que ayudan:** *six-pointed star in the eye*, *mincho
title typography*, *harlequin diamond pattern background* (cartelas),
*vtuber stream overlay, chat message window* (MEM), *TV news lower
third* (noticiero), *countdown card with handwritten message*.

### 17.1 · Para una IA de texto (repaso corto)

Para que una IA escriba los textos de la lámina, del bot o de un
doblaje en la voz de cada personaje. Todo sale de frases ya citadas en
esta biblia (§4, §9, §12.3). **Ojo:** salvo las dos del doblaje latino,
son **traducción mía del japonés** (subtítulos de la emisión), no el
latino. Antes de rotular una frase como «del doblaje», oírla en
Crunchyroll (§12.3).

**Reglas de voz**
- **Kana:** frases cortas y afiladas. Presume y luego se sonroja.
  Explica con jerga de rodaje (ensayo, cámara, pasada). Ríe con un
  «¡Hmph!» de suficiencia. Nunca dulce del todo.
- **MEM-cho:** alarga las vocales y endulza («Aqu-tan»). Saluda con
  «¡Konmemu~!». Cuando se pone seria, habla de **cifras y horas de
  publicar**. Celebra gritando números.
- **Ruby:** exclamaciones de fan. Signos ¡! por todas partes. Llama a
  Aqua «hermano» (お兄ちゃん). Habla de ser idol como su madre.
- **Akane:** formal y cálida. Saluda presentándose («Soy Akane
  Kurokawa, de la compañía Lalalai»). Anima a las demás **por su
  nombre**.
- **Aqua:** pocas palabras, seco. Frases de dos o tres palabras.
- **Gotanda:** brusco, de oficio. Explica el mundillo como un profesor
  cansado.
- **Puntuación:** ¡! y ¿? siempre dobles. Nada de «·», «—» ni
  paréntesis de relleno (regla 4 del dueño). Una idea por cuadro.
- **El doblaje latino dice «X»**, no «Twitter», y «**Producciones
  Ichigo**» en la T1 (§12.3).

**Frases reales, por emoción**

| Emoción | Quién | Frase | Dónde |
|---|---|---|---|
| alegre | MEM | «¡10.000 suscriptores!» «¡Ahora sí parece oficial!» | ep. 9 · 09:42–09:51 |
| alegre | Ruby | «¡Yo voy a ser idol!» | ep. 2 · 03:56 |
| alegre | MEM | «¡Konmemu~!» (こんめむ〜♪, su saludo) | vídeos oficiales «MEMちょの部屋» (§9) |
| enfadada | Kana | «¡Qué asco!» (きっも！) | ep. 3 · 01:58 |
| enfadada | Ruby (bebé) | «¡Un directo tiene gracia verlo en vivo!» | ep. 1 · 23:34 |
| enfadado | Aqua | «Qué chapuza.» (雑だな) | ep. 3 · 16:59 |
| explicando | MEM | «¿Sabes qué día y a qué hora subirlo para sacar más retuits, y cuántas letras rinden más? Soy una profesional de hacer virales.» | ep. 7 · 11:14–11:30 |
| explicando | Gotanda | «Hay tres clases de actores.» | ep. 1 · 43:15 |
| explicando | Kana | cómo se rueda un drama: lectura, ensayo, cámara, pasada | ep. 3 · 16:34–16:57 |
| animando | Kana | «¡Voy a teñir tu barra de blanco! ¡Seré tu *oshi no ko*!» | ep. 11 · 07:41–07:49 |
| animando | Pieyon | «¡10 cuestas más!» | ep. 10 · 05:47 |
| animando | Akane y Kana | «No voy a perder.» (絶対に負けない) | T2 ep. 16 ([推しセリフ #05](https://www.youtube.com/watch?v=VrIF12uKg1Y&t=29)) |
| presumiendo | Kana | «Hmph. Es que yo soy adulta.» | ep. 3 · 14:42 |
| triste | Gotanda (**latino**, textual) | «Pero tú nunca podrás ser tu mamá.» | ep. 2 · 20:23 ⚠️ (Doblaje Wiki) |
| nostálgico | Aqua (**latino**, textual) | «Mi favorita siempre fue y siempre será Ai Hoshino.» | ep. 4 · 19:52 ⚠️ (Doblaje Wiki) |
| lema | Ai | «La mentira es el amor más grande, ¿sabes?» | ep. 1 · 09:46 |

Las frases tristes de Ai del ep. 1 (65:04–65:24) **no** se usan en las
láminas (punto 16: no jugar con su muerte).

**Vocabulario de expresiones (para la IA de imagen)**
- **Estrella en el ojo:** blanca de **seis puntas**; Ai en los dos,
  Aqua en el derecho, Ruby en el izquierdo. **Estrella negra** = modo
  venganza: no en canales alegres (§16). En Akane salen **cuando actúa
  de Ai** (P·21). Etiquetas que entienden las IA: *star-shaped pupils,
  symbol-shaped pupils, mismatched pupils* (Danbooru, `partes/datos-imagen.md`).
- **Sonrojo:** Kana se pone roja al enfadarse o al presumir (*blush*).
- **Fondo de emoción:** brillos y estrellitas sueltas (*sparkles*) y
  las **luces del escenario en rejilla**, como en la trama del manga
  (punto 19).
- **Chibi:** sólo en los **cartones oficiales** de cuenta atrás y en las
  tarjetas del canal (O·1-6) y en el Nendoroid (punto 23). Para el
  personaje principal de la lámina, **no**: estropea (§17).
- **Gotas de sudor:** no encontré en las partes cómo las usa la serie
  ⚠️. Mejor no pedirlas.

---

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

> De `partes/texto.md` (repaso corto, 24-sep-2026), con el equipo de
> `partes/datos-texto.md` (AniList). Complementa §17 (rasgos, paleta,
> palabras) sin repetirlo.

### 18.1 · Quién lo hace
- **Estudio Doga Kobo** (動画工房). Director **Daisuke Hiramaki**
  (平牧大輔). Diseño de personajes y dirección de animación **Kanna
  Hirayama** (平山寛菜). Subdirectora y guion de color **Ciao
  Nekotomi** (猫富ちゃお). Director de fotografía (撮影, la etapa que
  pinta luces y filtros encima del dibujo) **Takafumi Kuwano**
  (桒野貴文) ✅ ([AniList, staff](https://anilist.co/anime/150672/staff),
  [Real Sound](https://realsound.jp/movie/2023/06/post-1345012.html),
  [MANTANWEB](https://mantan-web.jp/article/20240816dog00m200078000c.html)).
- **Diseño original:** Mengo Yokoyari (横槍メンゴ). **Logo del título:**
  Miku Makifuchi (巻渕美紅). **Vestuario:** Maho Yoshikawa, Satomi
  Watanabe, Asami Hayakawa, Miki Matsumoto y Nanami Hakoda. **Objetos
  (props):** Miki Matsumoto y Nanami Hakoda ⚠️ (sólo AniList).

### 18.2 · La línea: más, no menos
- Casi todos los animes **simplifican** el trazo del manga para
  animarlo rápido. Aquí hicieron **lo contrario**: recogen todo lo
  posible de las sombras y del trazo del manga. Por eso *Oshi no Ko*
  «tiene más líneas que un anime normal» ✅ ([MANTANWEB](https://mantan-web.jp/article/20240816dog00m200078000c.html),
  [Yahoo/Febri](https://article.yahoo.co.jp/detail/094230118938ecb262b1cc245b02d40caec0224e)).
- Hirayama corrigió **unos 1.000 cortes** sólo en el episodio 1 ⚠️
  ([Sakuga Blog](https://blog.sakugabooru.com/2023/04/18/introduction-to-oshi-no-kos-team-maximizing-impact-through-an-adaptation/)).
- En el manga, la línea es **fina** y las sombras van con **trama de
  puntos** y **rayado a pluma** sólo en lo más oscuro (visto en una
  página real, punto 19).

### 18.3 · Los ojos y el color: subir el número de colores
- Hiramaki pidió a Hirayama reproducir **entera** la estrella de seis
  puntas del ojo del manga ✅ ([MANTANWEB](https://mantan-web.jp/article/20240816dog00m200078000c.html);
  §17).
- Hirayama, textual: *«When you color in animation, it becomes one
  color. The amount of information from the manga to the anime gets
  reduced… By increasing the number of colors, you can achieve a
  similar effect to the manga»*. O sea: **al colorear se pierde
  información; se compensa con más tonos** en pelo e iris ✅
  ([ComicBook](https://comicbook.com/anime/news/oshi-no-ko-anime-art-style-animation/),
  [Real Sound, parte 2](https://realsound.jp/movie/2023/06/post-1345012_2.html)).
- **Guion de color** (カラースクリプト): Nekotomi pinta un *storyboard*
  en color que fija el ambiente de cada escena **antes** de animar.
  La regla compartida: «convertir en color la emoción que se sintió al
  leer el manga» ✅ ([MANTANWEB](https://mantan-web.jp/article/20240816dog00m200078000c.html),
  [Sakuga Blog, T2](https://blog.sakugabooru.com/2024/09/04/oshi-no-ko-stage/)).
- **Colores saturados también en escenas normales**, no sólo en las
  clave ⚠️ ([MANTANWEB](https://mantan-web.jp/article/20240816dog00m200078000c.html)).
- **Sombras con focos de color**, no gris ni negro liso. Hiramaki dice
  que lo toma del cine y la tele de imagen real (cita *City Hunter*,
  1999) ⚠️ (MANTANWEB).
- **Fotografía (撮影):** ahí van destellos, *bokeh* y brillo de focos
  (vistos en los fotogramas, §17). Qué filtros exactos usa Kuwano: sin
  entrevista que lo detalle ⚠️.
- **Programa:** **no lo encontré**. Ninguna entrevista leída (Real
  Sound, MANTANWEB, Sakuga Blog, ComicBook, Febri) nombra el software
  de Doga Kobo. El estándar de la tele japonesa es **RETAS STUDIO** o
  **CLIP STUDIO PAINT EX** ([ficha de RETAS](https://www.clip-studio.com/clip_site/tool/items/rs_d_plan),
  [Wikipedia JA](https://ja.wikipedia.org/wiki/RETAS_STUDIO)), pero
  **no es un dato de esta serie** ⚠️.

### 18.4 · Cómo trabajaron las escenas grandes
- **Episodio 1 (el largo: 81:52 en la emisión de TV, §4; se estrenó
  en cines):** coreografiaron el
  baile **antes** de tener la música final, con **referencia 3D** de
  vídeos de baile, y dibujaron el *storyboard* sobre la canción.
  Metieron **cortes pintados a pincel a mano** para un estilo «vívido y
  contundente» ✅ ([Wikipedia, «Mother and Children»](https://en.wikipedia.org/wiki/Mother_and_Children_(Oshi_no_Ko)),
  [Sakuga Blog](https://blog.sakugabooru.com/2023/04/18/introduction-to-oshi-no-kos-team-maximizing-impact-through-an-adaptation/)).
- **T2, el teatro 2.5D (*Tokyo Blade*):** **luz diegética** (la que
  habría de verdad en el escenario) y **cables y micros a la vista**
  para que se note que es una función. El director de esos capítulos,
  **Kuniyasu Nishina**, usa **cortes de montaje muy marcados** y planos
  fijos muy compuestos. La cámara mezcla movimiento con **planos desde
  la butaca**. El supervisor de acción, «**amoji**», mezcla dibujo
  *cartoon* con **papel y tinta suelta** e **imágenes de estrellas**
  para sacar la emoción fuera del cuerpo ⚠️ ([Sakuga Blog, T2](https://blog.sakugabooru.com/2024/09/04/oshi-no-ko-stage/)).

### 18.5 · Encuadres: cómo se enmarca cada emoción
| Emoción o uso | Encuadre | De dónde |
|---|---|---|
| **Presentar, invitar** | plano medio **en diagonal, señalando a cámara**, un poco desde abajo | key visuals de Ai y MEM (§17) |
| **Presión, soledad** | plano abierto y espacioso: el personaje **pequeño** y la agencia o el edificio **enorme** detrás | Hiramaki ([Sakuga Blog](https://blog.sakugabooru.com/2023/04/18/introduction-to-oshi-no-kos-team-maximizing-impact-through-an-adaptation/)) |
| **Dudas, lo que piensa** | encuadre **subjetivo**, dentro de su cabeza | ídem |
| **Emoción de escenario** | **desde el público**: barras de luz y focos hacia cámara, contraluz | opening (V·1-6) y Sakuga Blog T2 |
| **Golpe emocional** | plano fijo muy compuesto y **corte seco** | Sakuga Blog T2 |
| **Detrás / delante del telón** | camerino y pasillo **fríos y apagados**; escenario **saturado** (noche `#222B32` contra rojo `#C41E34`, §6.2) | guion de color de Nekotomi + paleta medida |

### 18.6 · Cómo replicarlo en Photoshop
1. **Línea:** pincel duro, poco *jitter* de grosor (2-4 px a 150 ppp),
   **negro o gris casi negro**, nunca marrón. Más líneas de lo normal
   (18.2): pliegues, mechones, sombras dibujadas.
2. **Sombreado:** capa en **Multiplicar** con **2-3 tonos planos**, no
   degradado. Sombra base y otra más oscura en el pliegue.
3. **Iris:** 2-3 franjas de color (claro, medio, oscuro) y encima la
   **estrella blanca de seis puntas** en modo **Trama** o **Aclarar**.
4. **Luz de escenario:** capa en **Trama** o **Sobreexponer color** con
   pinceles de destellos y *bokeh* (Brusheezy o CLIP STUDIO ASSETS,
   punto 19).
5. **Fotografía final:** **grano fino** (Filtro > Ruido > Añadir ruido,
   2-3 %, monocromático) y un **mapa de degradado** azul-magenta en
   **Superponer** al 15-20 %. Es mi aproximación al acabado del
   estudio, no su receta ⚠️.

### 18.7 · Cómo replicarlo en Blender
1. **Contorno:** modificador **Solidify** (grosor 0,01-0,02, normales
   invertidas, material con **Backface Culling**) o **Freestyle** si se
   quiere una línea que cambie de grosor ✅ ([Artisticrender](https://artisticrender.com/cel-shading-in-blender/),
   [StraySpark, 2026](https://www.strayspark.studio/blog/how-to-get-anime-toon-look-blender)).
2. **Sombreado en celdas:** **Shader to RGB** + **Color Ramp** con 2-3
   escalones, en *Constant* (mismas fuentes).
3. **Luz de escenario:** luces de área **rosa, cian y ámbar** desde
   varios lados (los focos de §6) y, en el compositor, **Glare** (*Fog
   Glow* o *Streaks*) y una textura de **ruido** para el grano.
4. **Modelos para practicar el *shader* y el *rig*** (CC BY, dar
   crédito; **nunca** para la lámina, §5.1): Ai de
   [DarienToad](https://sketchfab.com/3d-models/ai-hoshino-oshi-no-ko-64ce3c96f9524644a38c47c390b40488),
   de [HiGuys920](https://sketchfab.com/3d-models/oshi-no-ko-hoshino-ai-3d-model-fv-dl-5d92181a0dec48d4a6a71c4a1d0fd5ec)
   y de [criticaldamage9211](https://sketchfab.com/3d-models/none-a25f0b9dee474ec0af6b0cf9d91a405e);
   Kana de [Teana](https://sketchfab.com/3d-models/none-a9497f1c3cb0471885374ed1c4d130de);
   Ruby, Aqua y Akane de HiGuys920 ([Ruby](https://sketchfab.com/3d-models/none-9d9c913ad2bd4cf692aa064167865494),
   [Aqua](https://sketchfab.com/3d-models/none-7c3df0f902e54b17986b893fa4b016f7))
   ✅ (licencia por la API de Sketchfab, `partes/texto.json` y
   `partes/datos-imagen.md`).
5. **Volumen de la ropa:** la falda de idol lleva **enagua**; en 3D,
   varias capas, no una falda plana (cosplay de Marsella, punto 23).

---

## Punto 19 · Texturas 2D (tramas, papel, patrones, emblemas y logos)

> De `partes/imagen.md` (repaso corto). Las texturas reales y 3D
> (papel, metal, cartón de Poly Haven) ya están en §5.1 y §6: con estas
> no falta ninguna capa.

### 19.1 · Las tramas del manga, vistas en una página real
En la página de manga oficial de B小町 en el escenario
([Fandom, 1299×1423](https://static.wikia.nocookie.net/oshi_no_ko/images/f/fe/B-Komachi_Current_Manga.jpg),
página [«B-Komachi»](https://oshinoko.fandom.com/wiki/B-Komachi)) hay
**cuatro capas** ✅ (mirada, tamaño por la API):
1. **Trama de puntos en degradado** para pelo y piel: más densa en la
   sombra, se aclara hacia la luz.
2. **Brillos y estrellitas sueltas** por el fondo (el *sparkle* de las
   escenas de idol).
3. **Rejilla de cuadritos** en dos franjas: las **luces del escenario**
   vistas de lejos (el mismo recurso que el fondo de focos de los
   renders, §6).
4. **Rayado fino a pluma** sólo en lo más oscuro: bajo el pelo y en
   los pliegues.

### 19.2 · Pinceles y texturas libres equivalentes
| Capa | Recurso | Licencia | Para qué |
|---|---|---|---|
| Trama de puntos | [Brusheezy, 34 pinceles de *screentone*](https://www.brusheezy.com/brushes/50379-mabecman-s-screentones-halftone-brushes) (Photoshop) | «community»: uso personal y comercial, sin reventa ⚠️ (no dice si la atribución es obligatoria) | sombras de la trama 1 |
| Brillos | [CLIP STUDIO ASSETS, «Shoujo Manga Sparkle»](https://assets.clip-studio.com/en-us/detail?id=1887489) | gratis (pide cuenta y CSP) ✅ | capa 2 y destellos de escenario |
| Papel | [CLIP STUDIO ASSETS, «Paper textures»](https://assets.clip-studio.com/en-us/detail?id=1752867) | gratis ✅ | grano de papel en 2D |
| Papel 3D | Poly Haven *paper-card* (§5.1, concepto C) | CC0 | la misma textura sirve en 2D y 3D |
| Patrón de ropa | [freesvg.org, lunares sin costuras](https://freesvg.org/polka-dot-seamless-pattern) | CC0 ✅ | adornos de trajes de idol |

### 19.3 · Patrones de ropa (vistos, no inventados)
- Los trajes de B小町 (uniforme rojo, «POP IN 2», los de Taito) llevan
  **lazos, corazones y estrellas sueltas** como adorno, **no** una tela
  estampada ✅ (hojas P· y O·, fotos de cosplay).
- El uniforme de **Yōtō** es **azul marino liso con ribete dorado**, sin
  cuadros (cosplay de San Diego, punto 23). No inventar un tartán.

### 19.4 · Emblemas y logos (medidos)
- **Ichigo Production, Inc:** placa de metal grabada «Ichigo
  Production, Inc · Saitou» con una **fresa con coronita**
  ([Fandom, 323×205](https://static.wikia.nocookie.net/oshi_no_ko/images/b/b9/Ichigo_Productions.png))
  ✅ (misma placa que O·23: dos fuentes).
- **B小町, 1.ª generación:** monograma cursivo «B» con 「小町」 en negro,
  insignia con **borde de picos blancos**, aire antiguo
  ([Fandom, 313×313](https://static.wikia.nocookie.net/oshi_no_ko/images/e/e2/BKomachi_Gen1_Logo.png)) ✅.
- **B小町, 2.ª generación:** «B小町» en letras de burbuja
  **rosa-magenta con degradado** sobre un **corazón rojo**, con una
  **estrella y estela amarilla** que lo cruza como una varita
  ([Fandom, 600×600](https://static.wikia.nocookie.net/oshi_no_ko/images/9/98/BKomachi_Gen2_Logo.jpg)) ✅.
  Ya es una **pegatina**: el más fácil de llevar a una lámina.
  Los dos juntos cuentan el **antes y después** del grupo.
- **Escudo del instituto Yōtō:** **no lo encontré** ⚠️ (ni página ni
  archivo en la wiki; el uniforme de las hojas y del cosplay no lleva
  escudo bordado visible).
- **Estrellas:** ojo = seis puntas; cartelas y adornos = cinco
  redondeadas (§16).

---

## Punto 20 · Gustos y detalles de cada personaje

> De `partes/voz.md` (repaso corto). Fuente base: el wikitext de cada
> personaje en la [wiki de Fandom](https://oshinoko.fandom.com/wiki/Ai_Hoshino)
> por su API, la [web oficial de talento](https://ichigoproduction.com/talent/arima.html)
> y la ficha de [AniList](https://anilist.co/character/188783).
> **Aviso:** la ficha de la wiki **no tiene** cumpleaños ni tipo de
> sangre, y el único artbook (*Glare×Sparkle*) es de ilustraciones, no
> un *databook*. Por eso casi no hay cumpleaños.

### Resumen para la lámina
| | Altura | Color de idol | Come / odia | Lo que siempre lleva |
|---|---|---|---|---|
| **Ai** | 151 cm ✅ | **rojo** ⚠️ | no encontrado | su **móvil** (clave «45510») |
| **Ruby** | 158 cm ✅ | **rojo**, por Ai ✅ | no encontrado | la barra de luz roja |
| **Kana** | 150 cm ✅ | **blanco** ✅ | dieta baja en hidratos; **odia los pimientos** | boina y guion |
| **MEM-cho** | 155 cm ✅ | **amarillo** ✅ | no encontrado | móvil y cámara |
| **Akane** | 163 cm ✅ | — | **vegetariana**; cocina muy bien | no encontrado ⚠️ |
| **Aqua** | 172 cm ✅ | — | **odia los pimientos** | cámara y edición |

### Ai Hoshino
- **Cumpleaños:** sin fecha. Muere hacia su **20.º cumpleaños**; el
  manga deja en duda si fue justo antes o después (tomo 1, pp. 163, 167
  y 198) ⚠️ ([Wikipedia JA](https://ja.wikipedia.org/wiki/%E3%80%90%E6%8E%A8%E3%81%97%E3%81%AE%E5%AD%90%E3%80%91)).
- **Su móvil y «45510»:** la clave de su teléfono y del blog son las
  **iniciales de las cuatro fundadoras** de B小町. Aqua la descifra en
  el capítulo 14 ✅ ([wiki](https://oshinoko.fandom.com/wiki/Ai_Hoshino) +
  el relato oficial [*45510* en Young Jump](https://youngjump.jp/oshinoko/novel_45510/novel_01.html)).
  En §13 y §16 ya salía como guiño; aquí está el porqué.
- **Color de idol: rojo.** Ruby lo elige después como homenaje ⚠️ (la
  wiki, en las páginas de Ai y de Ruby, cita el manga cap. 38, pág. 4:
  una sola web). **Corrige** lo que decía §6.2 («sin encontrar»).
- **Cómo se ve:** en su cabeza es «egoísta» y «codiciosa» por vivir de
  mentiras calculadas; la wiki dice que en realidad se sacrificaba y
  nunca se compadeció ⚠️ (análisis de la wiki, no cita textual). Cuadra
  con «Hoshino Ai es codiciosa» (ep. 1, 10:23, §9).
- **Comida:** no encontré ni favorita ni odiada ⚠️.

### Aqua Hoshino
- **Cumpleaños:** entre el **10 y el 19 de diciembre**, igual que Ruby
  (mellizos); sale en los volantes que reparte Ichigo Saitō en el
  **ep. 28** ⚠️ (una fuente primaria, citada en las dos fichas).
- **Odia los pimientos** (ピーマン): lo confiesa disfrazado de Pieyon
  (manga cap. 35, pág. 16) ✅ (wiki + el mismo gag de Kana).
- **Le gustan las mujeres mayores que él** (se lo dice a Kana, cap. 30,
  pág. 8) ⚠️.
- **Afición:** edición de vídeo y cámara, aprendidas con Gotanda ✅
  (wiki, *Trivia*; el vídeo que salva a Akane, ep. 7, §9).
- **Gastó más de 5 millones de yenes** buscando a su padre (cap. 72,
  pág. 9) ⚠️ (wiki).
- **Cómo se ve:** se desprecia por no haber salvado a Ai; su venganza
  es un castigo a sí mismo ⚠️ (wiki, *Personality*).

### Ruby Hoshino
- **Cumpleaños:** el mismo rango que Aqua, 10-19 de diciembre ⚠️.
- **Color de idol: rojo**, el de su madre, a propósito ✅ (wiki, cap.
  38, pág. 4 + las cartas «**In Red** Ruby» de *IDOLM@STER*, §6.2).
- **Odia mentir**, pero miente para su venganza: es su choque interno
  ⚠️ (wiki).
- **Cómo se ve:** llama a su venganza una «cruzada sagrada» por su
  madre; se rompe y llora como la niña que sólo quería a su madre
  cuando Aqua le cuenta la verdad en el rodaje de *La mentira de 15
  años* ✅ (wiki + la «etapa oscura» de §9).
- **Comida y aficiones** fuera del trabajo de idol: no encontradas ⚠️.

### Kana Arima
- **Cumpleaños:** no encontrado ⚠️.
- **Come poco hidrato** (dieta baja en carbohidratos, cap. 14, pág. 7)
  ✅ (wiki; dato nuevo).
- **Odia los pimientos**… y su éxito de niña fue «**El ejercicio del
  pimiento**» (ピーマン体操). La ironía es su gag ✅ (wiki + [AniList](https://anilist.co/character/188783):
  «She also hates bell peppers»). La canta en el ep. 9, 18:07 (§4).
- **Color de idol: blanco** ✅ (wiki, cap. 38, pág. 4 + «Si da igual,
  blanco», ep. 11, 03:34 + «**In White** Kana»).
- **Cómo se ve:** finge confianza para seguir siendo «la niña genio»,
  pero duda de su talento y teme acabar como un **juguete roto** de la
  industria ✅ (wiki + [CBR](https://www.cbr.com/oshi-no-ko-kana-arima-popularity-explained/)).

### Akane Kurokawa
- **Cumpleaños:** no encontrado ⚠️.
- **Vegetariana:** se llama a sí misma «精進の身» (*shōjin no mi*), juego
  de palabras con la cocina vegetariana budista (cap. 23, pág. 7) ✅
  (wiki; dato nuevo).
- **Cocinera:** hace una cena de varios platos; aprendió en cursos con
  su madre. La madre de Gotanda le dice a Aqua que «sería una buena
  esposa» ✅ (wiki).
- **Instagram en la ficción: `akanecco_2323`** (cap. 40, pág. 10) ✅
  (wiki).
- **Cómo se ve:** se siente **vacía**, sin identidad propia; sólo se
  siente real dentro de un papel escrito. Por eso improvisar en el
  *reality* la paralizaba ✅ (wiki + el análisis de Reddit [«A Black
  Hole»](https://www.reddit.com/r/OshiNoKo/comments/1nxfjsk/a_black_hole_an_analysis_of_akane/),
  88 votos).

### MEM-cho
- **Cumpleaños:** no encontrado. Tiene **23 años** y dice tener 18
  (§9).
- **Tiene una perra y un gato** (cap. 21, págs. 7-8) ✅ (wiki; dato
  nuevo). Cómo son: no encontré imagen ⚠️.
- **Vive en Meguro, Tokio** (ep. 8) ✅ (wiki; dato nuevo).
- **Instagram en la ficción: `memmem_cho_o`**; da *like* a las fotos de
  Akane y Aqua (cap. 40, pág. 10) ✅ (wiki).
- **Color de idol: amarillo** ✅ (§6.2, «**In Yellow** MEMCho»).
- **Cómo se ve:** sabe que finge la edad para debutar y cuida mucho su
  imagen de «estudiante» ✅ (wiki). **No es un chiste** para la lámina
  (§16).

---

## Punto 21 · Por qué la gente la ama (y las escenas que hacen llorar o gritar)

> De `partes/voz.md` (repaso corto). Cada premio, cruzado con el
> artículo que lo cita. Lo que no se pudo confirmar, fuera.

### 21.1 · Ventas y premios
- **Más de 25 millones de copias** del manga a diciembre de 2025 ⚠️
  ([Wikipedia EN](https://en.wikipedia.org/wiki/Oshi_no_Ko), lista de
  mangas más vendidos).
- Las ventas **subieron un 140 %** con el estreno del anime ⚠️
  ([Ramen Para Dos](https://ramenparados.com/las-ventas-del-manga-de-oshi-no-ko-aumentaron-un-140-tras-el-estreno-del-anime/),
  con datos de Oricon). **680.052 copias en una semana** (abril de
  2023, Oricon) ⚠️ ([Espinof](https://www.espinof.com/anime/oshi-no-ko-se-agota-completo-japon-volumenes-manga-idols-rompen-records-ventas-e-incluso-ha-pillado-sorpresa-a-su-dibujante)).
- **Ganó el 7.º Next Manga Award** (papel), agosto de 2021 ✅
  ([ANN](https://www.animenewsnetwork.com/interest/2021-08-24/kaiju-no-8-oshi-no-ko-win-next-manga-awards-web-print-categories/.176367) + Wikipedia).
- **Nominado, sin ganar:** Manga Taishō (5.º en 2021, 8.º en 2022),
  Shogakukan (2021), Kodansha (2022 y 2024), Tezuka Osamu (2022 y 2024)
  ✅ (ANN + [Comic Natalie](https://natalie.mu/comic/news/420300), vía
  Wikipedia). *El buscador dijo que ganó el Kodansha: es falso, sólo
  fue nominado.*
- **«Idol» de YOASOBI ganó Mejor Canción de Anime** en los 8.º
  Crunchyroll Anime Awards (2024). La serie tuvo **12 nominaciones**,
  tercera tras *Chainsaw Man* (25) y *Jujutsu Kaisen* (17) ✅
  ([Wikipedia, 8th Crunchyroll Anime Awards](https://en.wikipedia.org/wiki/8th_Crunchyroll_Anime_Awards)).
  Un supuesto premio de Rie Takahashi en la 10.ª edición: **no
  confirmado**, fuera.
- **Estreno récord:** tras el ep. 1, fue el anime **mejor puntuado de
  MyAnimeList** ⚠️ ([Radio Times](https://www.radiotimes.com/tv/fantasy/anime/oshi-no-ko-how-to-watch/)).
  **HIDIVE:** el mejor estreno de su historia en espectadores, altas y
  pruebas gratis ✅ ([ANN, 22-abr-2023](https://www.animenewsnetwork.com/news/2023-04-22/hidive-oshi-no-ko-anime-has-biggest-series-launch-in-streaming-service-history/.197374),
  [ComicBook](https://comicbook.com/anime/news/oshi-no-ko-top-streaming-series/)).

### 21.2 · Por qué gusta
- **La crítica a la industria idol:** relaciones parasociales,
  explotación mediática y el precio de la fama, con más matiz que otras
  series del género ✅ ([The People's Movies](https://thepeoplesmovies.com/anime-review-oshi-no-ko-season-1-2023/),
  4,5/5; [Anime Feminist](https://www.animefeminist.com/oshi-no-ko-episode-1/)).
- El autor lo quería así: «que la gente sepa cómo se hace daño a los
  talentos jóvenes» (punto 24).

### 21.3 · Con quién se identifica el público
- **Kana:** «la favorita del fandom, por mucho» y «el personaje mejor
  escrito», por su lucha con la autoestima en una industria que la
  desecha ✅ (§2, §9: CBR y Anime Corner). En ranking.net es 1.ª en
  número de votos (§2).
- **Akane:** la gente se ve en su **vacío**: sin forma propia hasta que
  encuentra un papel o una máscara ✅ ([Reddit, «A Black Hole»](https://www.reddit.com/r/OshiNoKo/comments/1nxfjsk/a_black_hole_an_analysis_of_akane/),
  88 votos).

### 21.4 · La escena que hace llorar: la muerte de Ai (ep. 1)
**No se usa en ninguna lámina** (§16). Va aquí para entender al fandom.
- **Cuándo:** ep. 1 «Mother and Children» (estreno en cines el
  17-mar-2023). Después del 62:30 («¡La semana que viene, el Domo!»,
  §4); **el minuto exacto del ataque no se midió** ⚠️.
- **Qué pasa:** el día del Tokyo Dome, un fan acosador apuñala a Ai.
  Herida, habla de la mentira como su forma de querer y muere abrazando
  a Aqua.
- **Por qué duele:** los **recuerdos felices** que se cruzan con el
  ataque son **del anime**, no del manga: lo feliz dentro de lo más
  cruel ✅ ([wiki, «Episode 1»](https://oshinoko.fandom.com/wiki/Episode_1)).
- **Qué suena:** una pieza **sólo de piano** de **Takurō Iga**, la
  última de las 60 que compuso para la T1. El director de sonido,
  Takeshi Takadera, no la quería «sólo triste»; Iga la escribió para
  el **cariño de Ai**, no para la pena de los mellizos ✅
  ([Wikipedia, «Mother and Children»](https://en.wikipedia.org/wiki/Mother_and_Children_(Oshi_no_Ko)),
  que cita el vídeo oficial [«Behind the Scenes Ep4: Soundtrack
  Recording»](https://www.youtube.com/watch?v=xHY11jIL7ZE)).
- **Cómo reaccionó la gente:** «This was the first animated show that
  made me cry» (394 votos): vio el *spoiler* en TikTok, no se lo creyó
  y quedó «destrozado» ✅ ([Reddit](https://www.reddit.com/r/OshiNoKo/comments/1skwn16/this_was_the_first_animated_show_that_made_me_cry/)).
  El clip de la escena resubido por un fan: **1.846.227 vistas** ✅
  ([Villenthessis](https://www.youtube.com/watch?v=WGO48upjurM&t=1),
  medido con yt-dlp).
- **Contexto delicado:** se parece al ataque real a la cantante Mayu
  Tomita (2016) ⚠️ (wiki, «Episode 1»). Otra razón para no tocarla.

### 21.5 · La escena que hace gritar de emoción: Kana y la barra blanca
- **Ep. 11 · 07:41–07:49** ✅ (§4). Entre barras amarillas y rojas,
  Aqua sostiene una **blanca**, el color de Kana. Ella grita: «¡Voy a
  teñir tu barra de blanco! ¡Seré tu *oshi no ko*!».
- Es **la escena de Kana más querida** (§16) y la mejor para las
  láminas alegres: barras de luz, escenario, color de cada una.

---

## Punto 22 · Fan dubs y comunidad hispana

> De `partes/voz.md` (repaso corto). Vistas y duración **medidas con
> yt-dlp** (sólo metadatos) el 24-sep-2026. TikTok, sólo por buscador
> (yt-dlp no baja de TikTok desde aquí). Las reacciones al doblaje
> oficial ya están en §12.4.

### 22.1 · Covers en español (lo más visto)
| Qué | Canal | Vistas | Duración | Enlace |
|---|---|---|---|---|
| **«Mephisto»** (ED T1), latino | **David Delgado** | **577.494** | 3:51 · jun-2023 | [YouTube](https://www.youtube.com/watch?v=CEbEKN7A8rM) ✅ |
| **«Idol»** (OP T1), latino | **David Delgado** | **336.481** | 3:35 · may-2023 | [YouTube](https://www.youtube.com/watch?v=ff48MN5E5fk) ✅ |
| «Idol», latino | Amor Shipping | 36.180 | 3:31 · oct-2024 | [YouTube](https://www.youtube.com/watch?v=oELciwGCftQ) ✅ |

**David Delgado** canta el OP y el ED: es **el nombre más visible** del
fandom hispano de esta serie. Hay más covers de «Idol» (MoonTsuki15,
DanieGreen, Kira0loka) y de «Mephisto» (Marshu, Valuxഒ en SoundCloud)
sin vistas medidas ⚠️.

### 22.2 · Fandubs (la escena más doblada: la muerte de Ai)
| Qué | Canal | Vistas | Duración | Enlace |
|---|---|---|---|---|
| «【Oshi No Ko】La Muerte de Ai · Fandub Español Latino» | Mari - Uchiha | 2.666 | 5:53 · oct-2024 | [YouTube](https://www.youtube.com/watch?v=e7kymeIxaH4) ✅ |
| «La muerte de Ai Hoshino Español Latino» | Variado | 548 | 5:49 | [YouTube](https://www.youtube.com/watch?v=tx6Y6uyyT6Q) ✅ |
| Capítulo 1 completo, doblaje de fans | Sparrow Doblaje Studio | sin datos (Patreon) | — | [Patreon](https://www.patreon.com/posts/oshi-no-ko-1-114383809) ⚠️ |
| «La muerte de Ai (Fandub Latino)» | Aiko Fujiwara Studios | sin medir | — | ⚠️ |
| capítulos doblados por fans | «hiro21t0» (citado en foros) | sin confirmar | — | ⚠️ |

**Para el servidor:** los fandubs son **pocos y pequeños** (miles de
vistas), frente a los **covers cantados** (cientos de miles). Y todos
doblan la escena que **no** se usa en las láminas. Una prueba de
doblaje del servidor con escenas **alegres** (el directo de MEM, Kana
explicando un rodaje, §17.1) llenaría un hueco.

### 22.3 · Cosplay hispano
- **Rinaco** (México) hizo de **Ai** con el traje de B小町 en escenario,
  «interpretando su personalidad e incluso sus movimientos al cantar»
  ✅ ([Geekmi News](https://www.geekmi.news/series/Cosplayer-mexicana-recrea-a-Ai-Hoshino-de-Oshi-no-Ko-y-conquista-el-escenario-20230622-0001.html),
  [Universo Nintendo](https://universo-nintendo.com.mx/2023/04/13/oshi-no-ko-ai-hoshino-cosplay-cosnekomaru/)).
- **Kana** con pelo corto rojo, falda plisada y chaqueta azul marino ✅
  ([Código Espagueti](https://codigoespagueti.com/noticias/anime/oshi-no-ko-cosplayer-kana-arima/),
  [AlfaBetaJuega](https://alfabetajuega.com/series/kana-arima-de-oshi-no-ko-cobra-vida-gracias-a-este-genial-cosplay)).
  Otro de Kana, «impresionante y realista» ⚠️ ([Vandal](https://vandal.elespanol.com/random/recrean-a-la-encantadora-protagonista-de-oshi-no-ko-kana-arima-con-un-cosplay-impresionante-y-realista/31613.html)).

### 22.4 · Memes y parodias hispanas
- El **doblaje latino oficial** da que hablar en TikTok (acento,
  adaptación): ver §12.4.
- «**80 % of the Oshi no Ko fandom after the end of the season**»:
  meme en inglés que también circula en cuentas hispanas ⚠️ (sin canal
  ni vistas).
- **Parodias actuadas** (sketch) hechas por hispanos: **no encontré
  ninguna** ⚠️. Sólo fandubs, covers y memes de imagen.
- El clip más visto de todo el punto es el de la muerte de Ai resubido
  por un fan, sin audio en español (1,8 millones, punto 21).

---

## Punto 23 · Colaboraciones, figuras y cosplay

> De `partes/imagen.md` (repaso corto). La wiki tiene una página entera
> de colaboraciones, [«Promotional Material»](https://oshinoko.fandom.com/wiki/Oshi_no_Ko_(anime)/Promotional_Material),
> con **más de 25** marcas y eventos. Ya estaban en la biblia:
> *IDOLM@STER Shiny Colors*, el juego de escape de SCRAP, los vasos de
> Lawson y el jabón «重曹ちゃん» (§3, §6.2, §15, §16).

### 23.1 · Marcas, cafés y eventos (ropa y poses nuevas)
Todas en la wiki (una fuente ⚠️ salvo donde se dice). Tamaños medidos
por la API:
| Colaboración | Qué trae | Imagen |
|---|---|---|
| **Sanrio** ✅ (wiki + [CBR](https://www.cbr.com/sanrio-hello-kitty-oshi-no-ko-official-crossover/) + [Siliconera](https://www.siliconera.com/oshi-no-ko-sanrio-crossover-merchandise-will-pair-characters/)) | parejas: Ruby-Hello Kitty, Aqua-Cinnamoroll, Akane-Kuromi, Ai-Little Twin Stars, Kana-My Melody, MEM-Pompompurin, Pieyon-Bad Badtz-maru. **Dibujado por Kanna Hirayama**, la diseñadora del anime. A la venta desde el 8-nov-2024 | [Ai, 849×1200](https://static.wikia.nocookie.net/oshi_no_ko/images/8/83/Oshi_no_Ko_X_Sanrio_Collaboration_%28Ai_X_Little_Twin_Stars%29_By_Kanna_Hirayama.jpg) · [Ruby, 849×1200](https://static.wikia.nocookie.net/oshi_no_ko/images/9/90/Oshi_no_Ko_x_Sanrio_Collaboration_%28Ruby_X_Hello_Kitty%29_by_Kanna_Hirayama.jpg) |
| **Taito**, premios de grúa «Sweet Sailor Style» | Kana, Aqua, Ai, Ruby y MEM con **uniformes de marinero** | [960×960](https://static.wikia.nocookie.net/oshi_no_ko/images/f/ff/Oshi_no_Ko_x_Taito_Toys_%28Sweet_Sailor_Style%29.png) |
| **Taito**, «White Angel» | Ruby, Akane, Aqua y Kana **con alas** y ropa blanca | [960×960](https://static.wikia.nocookie.net/oshi_no_ko/images/c/cb/Oshi_no_Ko_x_Taito_Toys_%28White_Angel%29.png) |
| **Ichiban Kuji** (lotería con figuras; may-2024, oct-2024, feb-2026) | Kana, Aqua (**traje militar dorado**), Ruby, Akane y Miyako con **vestidos góticos de época** | [cartel mayo 2024, 1239×697](https://static.wikia.nocookie.net/oshi_no_ko/images/7/72/1kuji_2024_May_Main_Visual.png) |
| **Sweets Paradise** (café, 2025) | Ruby, Kana y MEM **con delantal** de camarera | [2048×1448](https://static.wikia.nocookie.net/oshi_no_ko/images/9/98/Sweets_Paradise_B-Komachi_2025.png) |
| **Animate Cafe** (2024) | todo el reparto | [890×629](https://static.wikia.nocookie.net/oshi_no_ko/images/5/57/Oshi_no_Ko_x_Animate_Cafe_%28All_Cast%29.png) |
| **Natslive Cafe** (2025) | cartel del café | [1200×630](https://static.wikia.nocookie.net/oshi_no_ko/images/d/d4/Oshi_no_Ko_x_Natslive_Cafe_2025.png) |
| **DyDo** (máquinas de bebidas) | **fondos de móvil** con poses nuevas (cruza con §5.2) | [Kana, 1290×2796](https://static.wikia.nocookie.net/oshi_no_ko/images/5/51/DyDo_x_Kana_%28Wallpaper%29.jpg) |
| **GiGO** (recreativos de Sega) | cartel de premios | [1280×720](https://static.wikia.nocookie.net/oshi_no_ko/images/2/25/Oshi_no_Ko_x_GiGO.png) |
| **Yomiuri Giants** (béisbol) | personajes con la **camiseta** del equipo; lanzamiento inicial de las seiyū | [1920×1080](https://static.wikia.nocookie.net/oshi_no_ko/images/c/cb/Giants_x_Oshi_no_Ko_Collaboration.jpg) |

Más, sólo nombradas en la wiki: Gamers, Kujibikido, Tower Records,
Animate, HotPepperBeauty, RakuSpa, Yomiuri Land, Sega Plaza, Gindaco,
Don Quijote, Family Mart, Meiji y Seibu Yuenchi ⚠️.

### 23.2 · Juegos (tipo gacha)
- ***IDOLM@STER Shiny Colors*** (2023 y 2024) ✅: ya en §15, con su caja
  de diálogo.
- ***Monster Strike***: **dos rondas**; la 2.ª empezó el **13-feb-2026**,
  con versiones de **verano** y **San Valentín** que no salen en el
  anime ✅ ([Gachago](https://gachago.com/en/news/monster-strike-announces-second-crossover-event-with-oshi-no-ko-anime),
  [Mix Vale](https://www.mixvale.com.br/2026/02/13/monster-strike-begins-second-collaboration-with-oshi-no-ko-and-highlights-powerful-arima-kana-en/)).
- ***Othellonia*** (reversi gacha): ilustraciones nuevas tipo carta de
  Ai, Aqua y MEM, Ruby y Kana, Miyako y Akane ⚠️
  ([Ai, 1920×1080](https://static.wikia.nocookie.net/oshi_no_ko/images/e/e7/Ai_Othellonia.jpg),
  [Ruby y Kana, 1920×1080](https://static.wikia.nocookie.net/oshi_no_ko/images/a/a3/Ruby_%26_Kana_Othellonia.jpg)).
- ***Caravan Stories***: Aqua, Kana y Ruby de 5 y 6 estrellas ⚠️ (wiki).
- ***KOTODAMAN***: gacha de colaboración (vídeo oficial «OSHI NO KO
  Collaboration Gacha on KOTODAMAN») ⚠️.
- ***BanG Dream! Girls Band Party!***: existe la página «Oshi no Ko x
  Girls Band Party! Part 1 Gacha» en su wiki; el contenido no se pudo
  leer (Cloudflare) ⚠️.
- ***Fortnite***: **no lo encontré** (0 resultados en el texto de la
  wiki y nada en la web). El encargo lo pone como ejemplo de tipo de
  cruce.

### 23.3 · Figuras oficiales (su pose es referencia 3D)
- **Ai, escala 1/7** (Good Smile Company, producida por Kadokawa):
  **215 mm** con peana, pose de concierto con el pelo y las coletas al
  viento, ¥21.780 ✅ ([Good Smile](https://www.goodsmile.info/en/product/14226/Ai.html),
  [Anime Corner](https://animecorner.me/ai-hoshino-from-oshi-no-ko-gets-a-figure-pre-orders-open/)).
- **Ai, Nendoroid n.º 2300** (Good Smile, *chibi*) ✅
  ([foto de producto, 726×1000](https://solarisjapan.com/cdn/shop/files/f749ba60-bf53-11ee-90a6-5600040d5bd1.jpg),
  [ficha](https://solarisjapan.com/products/oshi-no-ko-hoshino-ai-nendoroid-2300-good-smile-company)).
- **Premios de Taito e Ichiban Kuji:** cada figura trae **ropa que no
  sale en el anime** (marinero, ángel, época). Buena **lámina 2 de
  vestuario** sin tocar el traje icónico.

### 23.4 · Cosplay bien hecho (materiales y volumen, mirados)
- **Ai** en el Palais Longchamp de Marsella ([esby.photo, 1024×769](https://live.staticflickr.com/65535/53387752817_964c0b074b_b.jpg),
  CC BY-NC-SA 2.0): vestido **rosa satinado**, falda de **volantes
  fruncidos sobre enagua** (de ahí el volumen), cinturón negro ancho,
  **guantes magenta largos**, medias a juego, plataformas blancas con
  correa, peluca morada. Es el traje del key visual de la T1 ✅.
- **Ruby y Aqua** con el uniforme de Yōtō en San Diego ([coolanimeboy25,
  1023×665](https://live.staticflickr.com/65535/54334350241_4fba9307d5_b.jpg),
  CC BY 2.0): **blazer azul marino con galón dorado cosido** en solapa y
  puños, camisa blanca. La tela cae **menos rígida** que en el dibujo ✅.
- **MEM** en Lyon: 12 fotos más de esby.photo (CC BY-NC-SA 2.0), sin
  analizar ([una de ellas, 769×1024](https://live.staticflickr.com/65535/54192880322_18f332c779_b.jpg)).
- Cosplay hispano (Rinaco, Kana): punto 22.

---

## Punto 24 · Obras parecidas y láminas vecinas

> De `partes/texto.md` (repaso corto) y `partes/datos-texto.md`
> (AniList).

### 24.1 · De dónde salió, según el autor
Aka Akasaka en su entrevista a ANN (mayo de 2023). El
[original](https://www.animenewsnetwork.com/feature/2023-05-10/how-accurate-is-oshi-no-ko-about-the-japanese-entertainment-industry-an-interview-with-aka-akasaka/.197795)
da 403 y no está en Wayback; se leyó el resumen con citas literales de
[@talkingnerd en Tumblr](https://www.tumblr.com/talkingnerd/716972147650838528/highlights-from-aka-akasaka-interview-with-ann) ⚠️:
- **Una broma de Japón:** «quiero renacer como hijo de mi idol», que se
  tuitea cada vez que una idol anuncia su boda. La tenía apuntada años
  antes.
- **Por qué oscura y por qué ahora:** el rodaje en imagen real de su
  manga anterior, ***Kaguya-sama: Love is War***, y las quejas del
  mundillo que le contaban amigos *streamers*.
- **Un amigo famoso atacado por un fan** parecía duro en público y le
  confesó que le había dolido mucho. Textual: *«talents hide their
  true colors for the sake of their works and for their fans (…) I want
  people to know how young talents are being hurt, exploited, and
  suffering»*.
- **No es un documental:** usa piezas reales (una filtración de un
  *reality* que acabó en suicidio, YouTube comiéndose a la tele), pero
  no retrata a nadie. Sólo cambiaron un diseño porque se parecía
  demasiado a una persona real.
- **Su humor viene de *Kaguya-sama***: dice que ese estilo cómico fue
  «una fórmula pedida por la editorial»; él se siente autor «del estilo
  de *Oshi no Ko*».

### 24.2 · Con qué la compara el público (no el autor)
- ***Perfect Blue*** (1997, Satoshi Kon): la comparación más repetida,
  por el lado oscuro del mundo idol. Pero **son opuestas**: *Perfect
  Blue* critica la industria de frente; *Oshi no Ko* la usa de
  escenario para un *thriller* de venganza ✅ ([FandomWire](https://fandomwire.com/oshi-no-ko-fans-have-been-gravely-wrong-about-the-purpose-of-aka-akasakas-manga/),
  [«Perfect Blue Criticizes The Idol Industry. Oshi no Ko Does Not.»](https://letsdiscoverthingsthataregood.wordpress.com/2023/04/29/perfect-blue-criticizes-the-idol-industry-oshi-no-ko-does-not/)).
  **Ninguna entrevista** dice que sea una influencia de Akasaka ⚠️.
- **Recomendaciones de usuarios de AniList** (nota de 0 a 100 y votos)
  ⚠️ (es del público): *Perfect Blue* (85, 438), *ERASED* (81, 285),
  *Kaguya-sama* (83, 213, **mismo autor**), *Rascal Does Not Dream of
  Bunny Girl Senpai* (81, 150), *NEEDY GIRL OVERDOSE* (68, 65,
  *streaming* y redes), *Kageki Shojo!!* (76, 50, teatro Takarazuka),
  *Zombie Land Saga* (74, 28, grupo idol en comedia), *Oddtaxi* (85,
  24), ***The Many Sides of Voice Actor Radio*** (68, 24: **seiyū y
  radio**, el tema del servidor), *ReLIFE*, *Looking for the Full Moon*,
  ***Skip Beat!*** (77, 22: **venganza en el mundo del espectáculo**,
  el paralelo más directo), *Vivy* y *Jellyfish Can't Swim in the
  Night* ([AniList](https://anilist.co/anime/150672)).

### 24.3 · La misma franquicia (no confundir con «parecidas»)
- **Imagen real:** serie de Amazon Prime Video (Toei), 8 capítulos
  (27-nov-2024 los 6 primeros, 4-dic-2024 los 2 últimos), y la película
  ***Oshi no Ko -The Final Act-***, en cines de Japón desde el
  20-dic-2024. Reparto: Umi Sakurai (Aqua), Asuka Saito (Ai), Nagisa
  Saito (Ruby), Nanoka Hara (Kana), Mizuki Kayashima (Akane), Ano (MEM)
  ✅ ([wiki, «Oshi no Ko (live action)»](https://oshinoko.fandom.com/wiki/Oshi_no_Ko_(live_action))).
- **Novela *Spica the First Star*** (一番星のスピカ), de Hajime Tanaka,
  con un relato de Akasaka (*POV B*): el pasado de Ai antes de ser el
  centro de B小町, y Sarina y Goro. Japón 17-nov-2023; inglés
  8-jul-2025 (Yen Press) ✅ ([wiki](https://oshinoko.fandom.com/wiki/Spica_the_First_Star),
  [portada, 1511×2148](https://static.wikia.nocookie.net/oshi_no_ko/images/0/03/Ichibanboshi_no_Spica.png)).

### 24.4 · Láminas vecinas del servidor (para no repetir)
Revisadas en las biblias del repositorio por el investigador de texto:
- **K-On! (10):** club de música escolar; su lámina usa una carta de té
  doblada y una pizarra con texto a mano. *Oshi no Ko* es **industria
  profesional**: sus objetos se ven **de trabajo** (móvil, guion, ficha
  de casting, letrero ON AIR), no de club. Ojo con la **pizarra** del
  concepto B: que se vea de plató (atril, rotulador, cartón oficial),
  no de aula.
- **Kakegurui (12):** «bonito por fuera, turbio por dentro». Enseña a
  dar peso sin *gore* en un servidor familiar.
- **Violet Evergarden (22):** un **objeto de trabajo que también es
  emocional** (cartas). Aquí es la hoja de audición o el guion: mismo
  mecanismo, objeto distinto.
- **Ninguna otra biblia es de idols** japonesas: *Oshi no Ko* no pisa el
  hueco de ninguna serie del servidor.

---

## Punto 25 · El mundo, la historia por arcos y sus símbolos

_(pendiente)_

---
## 18 · Tres conceptos de lámina (uno por canal)

> [!note] Segunda pasada: qué cambió en los conceptos
> Los tres se mantienen (uno por canal), pero ahora se apoyan en
> **formatos oficiales vistos de verdad**: A pasa del «post» inventado al
> **directo de MEM y su noticiero** (V·19-22); B cambia las カンペ
> inventadas por el **cartón oficial de «ON AIR»** y la **pizarra de
> MEM** (O·1-5); C sitúa la hoja en la **puerta de Ichigo Pro** (O·23)
> con la **cartela de estrella** de título (O·19). Las poses salen ahora
> de las hojas (P·, V·), no de imágenes de origen dudoso.
> **Segunda tanda:** A cambia su pose principal por **MEM haciéndose un
> selfie con el móvil** (key visual principal de la T1, de Crunchyroll);
> C suma la **Kana gritando con el guion** del mismo visual y la
> **cabina de doblaje real** como sitio alternativo.

### Concepto A — #redes-y-novedades · «El directo de noticias de MEM-cho»
**Objeto y sitio.** La lámina es **la pantalla del directo de MEM**,
como sus vídeos oficiales «MEMちょの部屋» y «MEMちょの【推しの子】NEWS»
(V·19-20; [0:05](https://www.youtube.com/watch?v=TvIOIATbUYE&t=5),
[1:29](https://www.youtube.com/watch?v=TvIOIATbUYE&t=89)): su **cuarto
añil** (`#2A0F6E`) con cortinas violeta, **lámpara de luna amarilla**,
estrellas, **peluches de B小町**, un **disco de oro** en la pared y la
**silla gamer rosa** ([Gaming Chair, CC BY](https://sketchfab.com/3d-models/gaming-chair-ccb3ada5917a4b90b689e1d1bf852dc2)).
En la mesa, su **móvil** (el objeto del plan: en el directo de *Puzzle
Star* lo sostiene con las dos manos, [0:39](https://www.youtube.com/watch?v=LmVk85v-O5w&t=39))
y un **aro de luz** ([Ring Light, CC BY](https://sketchfab.com/3d-models/ring-light-fe2d9eda3939484ea10c3ebc4887c28a)).
Arriba, la **barra de neón cian** del marco. Todo se modela en Blender.

**Personaje.** **MEM-cho**, la YouTuber de la serie y **presentadora
oficial de las novedades del anime** en el canal real. **Pose nueva
(segunda tanda), la mejor:** la del **key visual principal de la T1**
([Crunchyroll, 1000×1415](https://a.storyblok.com/f/178900/1000x1415/4edef43ef1/oshi-no-ko-visual.jpg)):
**brazo arriba con el móvil haciéndose un selfie**, la otra mano junto
a la cara, guiño y boca abierta. Junta a la vez el personaje, el
objeto del plan (el móvil) y la idea del canal. Otras: **V·19**
(sentada en su silla, índice en la barbilla: «¡hola!») o, para
celebrar, **O·6** (brazos abiertos, la tarjeta oficial de los 100.820
suscriptores). Ropa de casa: jersey verde menta `#BEE69D` (key visual)
o turquesa de hombros caídos (tráiler, V·13); o uniforme (P·16).

**Cómo habla.** Con los **tres cuadros reales** de sus vídeos, nada de
burbuja blanca:
- su frase, en el **rótulo naranja** `#DCAC64` con doble borde crema y
  morado (M PLUS Rounded 1c Black), abajo, como «MEMちょだよー!»;
- los pasos, en **ventanas de mensaje** blancas con **cabecera lila**
  `#9E81C3` y piquito (M PLUS Rounded 1c), como los mensajes de sus
  «MEMber»;
- la novedad, con el **rótulo de noticia «最新»** (círculo rojo +
  franja blanca, Noto Sans JP Black), sacado de «最新NEWS» (V·22).

**Dónde va cada texto.**
- Cartón de entrada arriba a la izquierda, rosa `#D87FB9` con destellos
  (V·21): **【NUESTRAS REDES】** en Shippori Mincho B1.
- Rótulo naranja de MEM: **«¡Síguenos! Yo sé cómo se hace viral.»**
  (guiño de fan opcional delante: «¡Konmemu~!»).
- Ventana 1 (cabecera «MEMber: Sintonizando»): **«Aquí están todas
  nuestras redes.»**
- Ventanas 2, 3, 4…: **una por red**, con icono, nombre y usuario
  reales en la cabecera (como si cada red fuera un fan escribiendo).
- Rótulo «最新» → en español **«LO ÚLTIMO»** en el círculo rojo, y en
  la franja: **«Cada vídeo nuevo se avisa aquí.»**
- Pie, en letra pequeña de la barra del directo: **«Dale a seguir y no
  te pierdas nada.»**

**Cómo no queda plano.**
- La **pantalla del móvil** y el **aro de luz** iluminan a MEM de
  frente en blanco frío; la **luna** mete un contraluz amarillo.
- **Delante**, desenfocados: el **cojín de corazón** y la **estrella
  amarilla** de su mesa, y el borde del teclado rosa.
- **Detrás**, el póster de 【推しの子】 y los peluches, con bokeh.
- Paleta: añil y violeta del cuarto, rosa de la silla, naranja del
  rótulo, amarillo de su color de idol.

### Concepto B — #en-directo · «El letrero ON AIR y el cartón de cuenta atrás»
**Objeto y sitio.** El **letrero ON AIR encendido en rojo** ([On Air
Sign, CC BY](https://sketchfab.com/3d-models/on-air-sign-0a5b90a7c5704803b2317c271fd8d156))
sobre la puerta del plató del **programa musical en directo «Nステ»**
donde Ai vuelve (ep. 1, 18:00: «es en directo, ¿puedes?»). Al lado, un
**monitor del estudio** con **Ai cantando** (pose de **P·1**, el key
visual oficial: micro, guiño, dedo a cámara). Delante de la puerta, en
un **atril**, una **pizarra de rotulador** como la de MEM «entrevista
EN VIVO» (**O·5**). Y la **franja negra de los cartones oficiales**
«【推しの子】 … ON AIR» (**O·1-4**) recorre el pie de la lámina.

**Personaje.** **Ruby** de adolescente, con el **uniforme rojo de
B小町** (visto en el ep. 11, V·17-18), asomada a la puerta con una
**barra de luz roja**. Pose de **P·17** (las dos manos abiertas a
cámara con guiño: «¡pasa!») o de **P·20** (en el plató con cámaras,
micro en la mano). Si se quiere un toque pícaro: **V·2** («shh», dedo
en los labios: «se está grabando»).

**Por qué Ruby.** De bebé se enfadó porque no la despertaron: «¡Un
directo tiene gracia verlo en vivo!» (ep. 1, 23:34). Es exactamente
la idea del canal.

**Cómo habla.** Como en los **cartones oficiales de cuenta atrás**:
- la frase de Ruby, **escrita a mano en la pizarra** (Hachi Maru Pop,
  rotulador negro con estrellitas y corazones, como O·1-5);
- los pasos, en **tres notas** pegadas a la pizarra;
- abajo, la **franja negra** con **【SINTONIZANDO】 EN DIRECTO · ON AIR**
  (mincho blanca + Bebas Neue en rosa `#E70082`), como «【推しの子】4.12
  ON AIR».

**Dónde va cada texto.**
- Letrero: **ON AIR** (Bebas Neue, en el acrílico).
- Pizarra de Ruby: **«¡Estamos en vivo! ¡Pasa a mirar!»**
  (alternativa fiel al ep. 1: «¡Los directos se ven en vivo!»).
- Nota 1: **«¿Estás haciendo algo ahora? Dilo aquí.»**
- Nota 2: **«Pon el enlace y qué estás haciendo.»**
- Nota 3: **«Quien quiera, se mete a mirar.»**
- Esquina negra del cartón (arriba a la izquierda, en diagonal, como
  «本日放送»): **«HOY»**.
- En el monitor, junto a Ai, un rótulo pequeño: **EN DIRECTO**. Si se
  quiere lámina 2 («volvemos enseguida»), la **carta de ajuste con
  conejos** (V·23).

**Cómo no queda plano.**
- La **luz roja del ON AIR** tiñe la pared y el pelo rubio de Ruby.
- El **monitor** mete luz rosa del escenario de Ai por el otro lado.
- **Delante**, desenfocados: cables, una caja de cartón
  ([Poly Haven](https://polyhaven.com/a/cardboard_box_01)), la punta de
  una barra de luz y un **uchiwa de fan** en corazón «アイ 無限恒久永遠推し!»
  (V·24; [modelo de uchiwa, CC BY](https://sketchfab.com/3d-models/japanese-uchiwa-hand-fan-02-be561cd8b01b49c482a4b26a8ec20bf0)).
- **Fondo**: pasillo de metal pintado que se pierde en la oscuridad.

### Concepto C — #castings · «La hoja de audición de Kana en la puerta de Ichigo Pro»
**Objeto y sitio.** Una **hoja de audición** sujeta a un **portapapeles**
([Clipboard, CC BY](https://sketchfab.com/3d-models/clipboard-a37158f20ccf436483029e8295629738)),
colgada en la **puerta azul noche de la agencia**, bajo la **placa
real de la serie «(株)苺プロ 斉藤»** con su fresa (**O·23**, 1920×1080).
La placa, en la lámina, dice **«Producciones Ichigo · Castings»** (el
nombre que usa el doblaje latino en la T1). En una mesita al lado:
**claqueta** ([CC0 - Clapperboard de plaggy, **CC BY**](https://sketchfab.com/3d-models/cc0-clapperboard-b541acf3a4f040f98b1bbf4137a66d09)),
**sello rojo**, bolígrafo rojo y un **guion** con tapa azul (el que
lleva Kana en O·18). Papel con curva ([Poly Haven, CC0](https://polyhaven.com/textures/paper-card)).
Alternativa de sitio: la **sala de ensayo de Lalalai** (O·24).

**Personaje.** **Kana**, la más querida y la que más sabe de pruebas:
«¡la niña genio que llora en 10 segundos!» (ep. 1, 49:41). Pose de
**P·9** (dibujo de animador del ep. 5: **índice arriba, cara seria**,
«te lo explico») con el **guion** de O·18 en la otra mano; o **P·10**
(índice a cámara) si se quiere más energía. Con **boina azul marino**
(P·7-8), que es su seña de todos los días. **Alternativa nueva (segunda
tanda):** la Kana del **key visual principal de la T1**
([Crunchyroll, 1000×1415](https://a.storyblok.com/f/178900/1000x1415/4edef43ef1/oshi-no-ko-visual.jpg)),
con boina, **un guion abierto en la mano y gritando**: para una
versión con más carácter («¡se gana!»).

**Sitio alternativo (segunda tanda):** la **cabina de doblaje real**
de la visita oficial al estudio (§8.1, punto 16; [1:44](https://www.youtube.com/watch?v=izzRjaUZig4&t=104)):
listones de madera `#9A6B4B`, paneles oscuros y micro de condensador.
Para un servidor de doblaje, la hoja de audición pegada en la puerta
de la cabina cuenta lo mismo que la puerta de Ichigo Pro.

**Cómo habla.** El **título** va en la **cartela de la serie**: estrella
negra de cinco puntas redondeadas sobre rombos rojo-rosa `#E74D64` y
blanco (**O·19**), con «**CASTINGS**» en blanco y, arriba, «第X話» →
«**HOJA DE AUDICIÓN**» en letra redonda rosa. La **ficha** imita la de
**talento de la web oficial** (nombre, estatura, «trabajos hechos»).
Kana corrige a mano en rojo (Hachi Maru Pop) y su frase va en un
**pósit**.

**Dónde va cada texto.**
- Cartela arriba de la hoja: **CASTINGS / HOJA DE AUDICIÓN**.
- Pósit de Kana: **«Un buen papel no se regala. ¡Se gana!»**
- Nota 1, junto al título: **«Un casting, un hilo.»**
- Casillas impresas de la ficha (BIZ UDPGothic Bold): **Proyecto,
  Personaje, Tipo de voz, Líneas de prueba, Fecha límite, Pago**
  (cotejar con el hilo fijado ⚠️).
- Nota 2, con flecha a las casillas: **«Rellena la ficha.»**
- Tres filas de casillas al pie: **Formato, Pago, Estado**, con la nota
  **«Ponle etiquetas.»**
- **Sello rojo** «CERRADO» y la nota: **«Cuando el papel esté cubierto,
  ciérralo.»**

**Lámina 2 de #castings:** la segunda hoja con las **15 etiquetas**
como casillas con sello, en tres grupos (punto 1.3), con la cartela
en su variante cian (O·20) para distinguirla.

**Cómo no queda plano.**
- **Luz fría de pasillo** desde arriba (como O·23) y una **lámpara
  cálida** desde la mesita: frío contra cálido.
- La **mano de Kana proyecta sombra** sobre la hoja; la **claqueta**
  delante, desenfocada; la **silla de director** ([CC BY](https://sketchfab.com/3d-models/directors-chair-d664c3ed7e1d48f5a0c0ad7f6581477b))
  asoma al fondo del pasillo.
- El papel curvado recibe la luz de forma desigual (así la tinta sigue
  la hoja, como pidió el dueño).
- Paleta: carmesí de Kana `#83132C`, puerta `#121A25`, placa
  `#CFC7C0`, rombos `#E74D64`, sello rojo.

---

## 19 · Lo que no pude verificar

Tras la segunda pasada quedan (cada uno va marcado en su sitio):
- **El texto real** del hilo fijado «Cómo se abre un casting (léeme)» y
  **las redes reales** del servidor: el inventario no los copia. La
  ficha de §1.3 y del concepto C es una propuesta.
- **Frases del doblaje latino:** sólo hay dos, citadas por Doblaje Wiki
  (una fuente). No hay clips oficiales doblados; las subidas de fans no
  tienen subtítulos y YouTube no deja bajar el audio (§12.3).
- **Tres voces latinas con una sola fuente para el papel:** Kamiki
  (Daniel Lacy), Pieyon (Ángel Mota) y la madre de Kana (Ellie Rojo).
  MyAnimeList (Jikan) no respondió. Tampoco se confirmó a **Gracia
  Comitre** (sólo en ANN).
- **Dos datos de la producción latina** sólo en Doblaje Wiki: que se
  grabó a inicios de 2026 y que las canciones se dejaron en japonés.
- **Origen de las ilustraciones `bg*`** de la extensión de fans (salvo
  `bg20`, oficial): ninguna coincide en tamaño con las 2963 de la wiki.
- **Encuestas de una sola fuente o sin abrir:** la china de Sina (el
  proxy bloquea sina.cn) y Ranker (401). Tampoco hay encuesta oficial
  (lo dice ABEMA Times).
- **La letra del logo** (nadie oficial la nombra), **la de los globos**
  del manga de Yen Press y Panini, y si **«推しゴ»** trae ñ (BOOTH pide
  iniciar sesión).
- **El color de idol de Ai:** ni la wiki ni la ficha de B小町 le dan uno.
- **Fotogramas grandes de los vídeos:** YouTube sólo da *storyboards* de
  320×180; sirven para mirar, no para recortar. Para recortar: las
  imágenes de la wiki (§3.0) o el episodio en Crunchyroll.

Lo que la primera pasada no pudo y **ahora sí está**: voces latinas de
secundarios (dos o tres fuentes), si hay doblaje de la T3 (no),
minutos de vídeos de YouTube, autores de Pixiv, licencias de Sketchfab,
menús y caja de diálogo de *Puzzle Star*, el aspecto de Gotanda y Aqua.

---

## 20 · Fuentes consultadas (103 principales; 335 enlaces distintos de 76 sitios en total)

**Abiertas de verdad (GitHub)**
1. [ANN T1, ficha 25783 (copia en GitHub)](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/anime/25783.json)
2. [ANN T2, ficha 28810](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/anime/28810.json)
3. [ANN T3, ficha 33662](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/anime/33662.json)
4. [ANN T4, ficha 38810](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/anime/38810.json)
5. [ANN manga, ficha 24571](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/manga/24571.json)
6. [Subtítulos japoneses T1, NanakoRaws](https://github.com/kienkzz/NanakoRaws-Anime-Japanese-subtitles)
7. [Extensión B小町 con 20 ilustraciones](https://github.com/jacobjuarezguerra/Oshi-No-Ko-Browser-extension-B-Komachi)
8. [Casete 3D de Oshi no Ko, TheFabi8A](https://github.com/TheFabi8A/oshi-no-ko)
9. [Google Fonts, repositorio (METADATA y archivos)](https://github.com/google/fonts)

**Oficiales y staff**
10. [Web oficial T3](https://ichigoproduction.com/Season3/)
11. [Web oficial: nuevas ilustraciones T3](https://ichigoproduction.com/Season3/news/index00540000.html)
12. [Web oficial: visual principal y PV 1 de la T3](https://ichigoproduction.com/Season3/news/index00570000.html)
13. [Web oficial: visual de fin de la T3](https://ichigoproduction.com/Season3/news/index01250000.html)
14. [Web oficial: ep. 6](https://ichigoproduction.com/Season1/story/06.html)
15. [TOKYO MX: ep. 6 【エゴサーチ】](https://s.mxtv.jp/anime/oshinoko/episode.html?ep_id=1bgjyr9388eeltqi)
16. [Febri: entrevista al director ①](https://febri.jp/topics/oshinoko_imamaki_01/)
17. [Febri ②](https://febri.jp/topics/oshinoko_imamaki_02/)
18. [Febri ③](https://febri.jp/topics/oshinoko_imamaki_03/)
19. [Real Sound: Kanna Hirayama y el staff](https://realsound.jp/movie/2023/06/post-1345012_2.html)
20. [anan: el staff de la T2](https://ananweb.jp/categories/entertainment/23266)
21. [X oficial: carátula BD 6 (Ruby y MEM)](https://x.com/anime_oshinoko/status/1894673764849508395)
22. [X oficial: carátula BD 3](https://x.com/anime_oshinoko/status/1861696464491098451)
23. [KADOKAWA: Blu-ray 1](https://store.kadokawa.co.jp/shop/g/g302303003603/)
24. [Young Jump: #有馬かな元気かな](https://youngjump.jp/manga/oshinoko/genkikana/)
25. [Canal oficial de YouTube](https://www.youtube.com/@anime_oshinoko)
26. [Hirayama dibuja a Kana](https://www.youtube.com/watch?v=q4bzYqoFGvo)
27. [Hirayama dibuja a Ai](https://www.youtube.com/watch?v=CYxj4xCcGmI)
28. [Juego Puzzle Star, web](https://oshinoko-puzzle.com/)
29. [KADOKAWA: Puzzle Star](https://group.kadokawa.co.jp/information/promotional_topics/article-14251.html)

**Prensa (japonés)**
30. [Natalie: anuncio T3](https://natalie.mu/comic/news/594182)
31. [Natalie: visual T3 y ending](https://natalie.mu/comic/news/646883)
32. [Animate Times: teaser T3](https://www.animatetimes.com/news/details.php?id=1742621823)
33. [Animate Times: carátula BD T2](https://www.animatetimes.com/news/details.php?id=1726645100)
34. [ABEMA Times: no hay encuesta oficial](https://times.abema.tv/articles/-/10128876)
35. [Dengeki: ep. 6](https://dengekionline.com/articles/186111/)
36. [Denfaminicogamer: Puzzle Star](https://news.denfaminicogamer.jp/news/260218q)
37. [GameWith: Puzzle Star](https://gamewith.jp/gamedb/12821/articles/39800)
38. [ciatr: miembros de B小町](https://ciatr.jp/topics/324070)
39. [ciatr: lugares reales](https://ciatr.jp/topics/324247)
40. [聖地巡礼.com](https://anime-pilgrimage.com/oshi-no-ko/)
41. [Lawson: vasos por color](https://www.lawson.co.jp/lab/entertainment/art/20241008_bookoshinoko.html)
42. [DesignPocket: letras para Oshi no Ko](https://designpocket.jp/static/font/fontguide/093.html)
43. [ffont: letra 推しゴ](https://ffont.jp/oshigo/)

**Prensa y wikis (inglés)**
44. [ANN: Crunchyroll suma T1 y T2](https://www.animenewsnetwork.com/news/2026-02-25/crunchyroll-adds-oshi-no-ko-anime-1st-2-seasons/.234566)
45. [ANN: «Idol», 1.000 millones](https://www.animenewsnetwork.com/news/2025-11-25/oricon-yoasobi-idol-is-fastest-song-to-top-1-billion-times-streamed/.231400)
46. [ANN: visual de Aqua T3](https://www.animenewsnetwork.com/news/2025-03-22/oshi-no-ko-anime-3rd-season-reveals-aqua-visual-video/.222695)
47. [Oshi no Ko Wiki: Kana](https://oshinoko.fandom.com/wiki/Kana_Arima)
48. [Oshi no Ko Wiki: MEM-cho](https://oshinoko.fandom.com/wiki/Mem-Cho)
49. [Oshi no Ko Wiki: Gotanda](https://oshinoko.fandom.com/wiki/Taishi_Gotanda)
50. [Oshi no Ko Wiki: ep. 34](https://oshinoko.fandom.com/wiki/Episode_34)
51. [TV Tropes: memes](https://tvtropes.org/pmwiki/pmwiki.php/Memes/OshiNoKo)
52. [Know Your Meme](https://knowyourmeme.com/memes/subcultures/oshi-no-ko)
53. [CBR: por qué Kana es tan popular](https://www.cbr.com/oshi-no-ko-kana-arima-popularity-explained/)
54. [CBR: Kana o Akane](https://www.cbr.com/oshi-no-ko-kana-or-akane-best-girl/)
55. [Anime Corner: anime de la temporada, invierno 2026](https://animecorner.me/winter-2026-anime-of-the-season-rankings/)
56. [Anime Corner: seiyū de la temporada](https://animecorner.me/winter-2026-seiyuu-of-the-season-rankings/)
57. [Anime Corner: ep. 6](https://animecorner.me/oshi-no-ko-episode-6-shows-the-best-depiction-of-cyberbullying/)
58. [Game Rant: estrellas en los ojos](https://gamerant.com/oshi-no-ko-why-do-aqua-and-ruby-have-stars-in-their-eyes/)
59. [Attack of the Fanboy: estrellas blancas y negras](https://attackofthefanboy.com/anime/oshi-no-ko-why-do-some-characters-eyes-have-bright-dark-stars/)
60. [Screen Rant: ep. 6 y Hana Kimura](https://screenrant.com/oshi-no-ko-darkest-moment-real-tragedy-akane/)
61. [Dexerto: críticas al final](https://www.dexerto.com/anime/oshi-no-ko-manga-slammed-for-terrible-ending-2974344/)
62. [DualShockers: Gotanda](https://www.dualshockers.com/oshi-no-ko-director-taishi-gotanda/)
63. [ANIHK: MEM-cho](https://anihk.com/en/blogs/characters/oshi-no-ko-mem-cho-real-age-revealed)
64. [ANIHK: Akane](https://anihk.com/en/blogs/characters/oshi-no-ko-akane-kurokawa-character-guide)
65. [Oricon: ep. 34](https://us.oricon-group.com/news/8027/)
66. [Yen Press: tomo 1](https://yenpress.com/titles/9781975363178-oshi-no-ko-vol-1)

**Otros idiomas**
67. [Sina (chino): Kana, la chica más popular](https://www.sina.cn/news/detail/5265276628376440.html)
68. [Ruliweb (coreano): encuesta de fans](https://bbs.ruliweb.com/community/board/300143/read/63270152)
69. [Namu Wiki (coreano): Kana](https://namu.wiki/w/%EC%95%84%EB%A6%AC%EB%A7%88%20%EC%B9%B4%EB%82%98)

**Doblaje latino y español**
70. [Crunchyroll: elenco del doblaje latino T1](https://www.crunchyroll.com/es/news/announcements/2026/7/14/elenco-staff-doblaje-latino-oshi-no-ko-temporada-1)
71. [ANMTV: doblaje T1](https://www.anmtvla.com/2026/07/oshi-no-ko-doblaje-de-la-primera.html)
72. [ANMTV: doblaje T2](https://www.anmtvla.com/2026/08/oshi-no-ko-doblaje-de-la-2-temporada-ya.html)
73. [Doblaje Wiki: Oshi no Ko](https://doblaje.fandom.com/es/wiki/Oshi_no_Ko)
74. [The Dubbing Database](https://dubdb.fandom.com/wiki/Oshi_no_Ko_(Latin_American_Spanish))
75. [The Project Arcade](https://theprojectarcade.com/oshi-no-ko-estrena-doblaje-latino-en-crunchyroll-reparto-episodios-y-proximas-temporadas/)
76. [Ivrea Argentina](https://www.ivrea.com.ar/titulo/oshi-no-ko/)

**Arte, 3D y fondos**
77. [Sketchfab: On Air Sign](https://sketchfab.com/3d-models/on-air-sign-0a5b90a7c5704803b2317c271fd8d156)
78. [Poly Haven: Paper & Card](https://polyhaven.com/textures/paper-card)

**Segunda pasada (red abierta), abiertas de verdad**
79. [Oshi no Ko Wiki, API](https://oshinoko.fandom.com/api.php) (texto, imágenes y tamaños; `investigar_serie.py`)
80. [Doblaje Wiki, página de la serie por la API](https://doblaje.fandom.com/es/wiki/Oshi_no_Ko)
81. [Crunchyroll News: entrevista al director Daisuke Hiramaki (Newtype)](https://www.crunchyroll.com/es/news/interviews/2026/4/28/oshi-no-ko-anime-director-entrevista)
82. [Crunchyroll News: el significado de los ojos estrellados](https://www.crunchyroll.com/es/news/features/2026/4/2/significado-ojos-estrellados-oshi-no-ko)
83. [Crunchyroll: key visual T1 del anuncio latino](https://a.storyblok.com/f/178900/1000x1415/4edef43ef1/oshi-no-ko-visual.jpg)
84. [みんなのランキング (ranking.net)](https://ranking.net/rankings/best-oshinoko-characters)
85. [カイの漫画考察: ranking de personajes](https://manga-comic-netabare.com/archives/61568/oshinoko-character-ranking-arima-kana/)
86. [Canal oficial: «MEMちょの部屋» #37](https://www.youtube.com/watch?v=TvIOIATbUYE)
87. [Canal oficial: «最新NEWS»](https://www.youtube.com/watch?v=VjyCYUdmlnc)
88. [Canal oficial: opening T1 «Idol»](https://www.youtube.com/watch?v=PgBvV9ofjmA)
89. [Canal oficial: ending T1 «Mephisto»](https://www.youtube.com/watch?v=0saw1cGIl1A)
90. [Canal oficial: tráiler principal 2](https://www.youtube.com/watch?v=gKWEUJ4r5do)
91. [Canal oficial: «STAR☆T☆RAIN», ep. 11](https://www.youtube.com/watch?v=S-UmqvA7uR8)
92. [Canal oficial: MEM juega a *Puzzle Star*](https://www.youtube.com/watch?v=LmVk85v-O5w)
93. [Canal oficial: mensaje especial de Akane](https://www.youtube.com/watch?v=L-ZNenzreyU)
94. [Canal oficial: 推しセリフ #05](https://www.youtube.com/watch?v=VrIF12uKg1Y)
95. [Canal oficial: visita al estudio de doblaje n.º 6](https://www.youtube.com/watch?v=izzRjaUZig4)
96. [Canal oficial: HAPPY VALENTINES DAY 2026](https://www.youtube.com/watch?v=pZSm3lQQqok)
97. [Crunchyroll en Español: clip de la T3](https://www.youtube.com/watch?v=Gdigwu7pJyY)
98. [Subida de fans del doblaje latino (Otaku en Linea)](https://www.youtube.com/watch?v=x3gKIAtsfLc)
99. [Sketchfab API: licencia de cada modelo](https://sketchfab.com/3d-models/on-air-sign-0a5b90a7c5704803b2317c271fd8d156)
100. [Pixiv API: fan art de MEM de Rinko](https://www.pixiv.net/en/artworks/113692523)
101. [BOOTH: letra 推しゴ](https://booth.pm/ja/items/5635169)
102. [Reddit por Arctic Shift: el guion firmado](https://reddit.com/r/OshiNoKo/comments/1vhzqqu/the_15_year_lie_script_with_all_of_the_cast/)
103. [Subtítulos de la T3 (Limenime, GitHub)](https://github.com/limedriveku/limesub)

(Además, todos los enlaces de YouTube, Pixiv, Sketchfab y fondos
citados en los puntos 5, 13 y 14.)

---

## Cumplimiento del encargo

| Punto de `ENCARGO.md` | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial, en cantidad y variado | ✅ | 1510 imágenes de la wiki revisadas (dos tandas de `investigar_serie.py`); 52 escogidas en las hojas P· y O·; key visuals, carátulas de BD, cartones de cuenta atrás, renders, dibujos del staff, fiestas (§3, §14) |
| 2 · Fotogramas de escenas icónicas con capítulo y minuto | ✅ | capturas 1920×1080 de la wiki con su episodio (O·15-16, O·23-25, P·18, P·21) y 26 cuadros de vídeo con minuto y `&t=` (V·); minutos de 31 escenas por los subtítulos japoneses (§4). Los cuadros de vídeo son de 320×180 (*storyboard*) |
| 3 · Fan art y 3D con licencia | ✅ | 15 modelos de Sketchfab con licencia por su API y 3 texturas CC0; 5 fan arts de Pixiv con autor, tamaño y fecha (§5) |
| 4 · Fondos y sitios, luz, paleta, texturas | ✅ | 15 sitios con luz y hora, 5 con hex medidos (más la paleta de §6.2), incluida la cabina de doblaje real; texturas CC0 de Poly Haven (§6) |
| 5 · Tipografía con tildes | ✅ | 19 letras libres comprobadas con fontTools. Falta: la letra real del logo no es pública y «推しゴ» no se pudo bajar (§7) |
| 6 · Cómo hablan en pantalla | ✅ | 16 formatos (11 vistos en vídeo y arte oficial en la segunda pasada): directo de MEM, noticiero «最新», cartones «ON AIR», cartelas de estrella, «mensaje especial», caja de *IDOLM@STER* (§8) |
| 7 · Personajes y popularidad | ✅ | Anime Corner, ranking.net, blog japonés y Ruliweb abiertos; no existe encuesta oficial (§2) |
| 8 · Doblaje latino, dos fuentes | ⚠️ | reparto y staff: 32 papeles con dos o más fuentes, 3 con una. **Frases:** sólo 2, de Doblaje Wiki, con minuto cruzado; no hay clips oficiales doblados (§12) |
| 9 · Música | ✅ | OP, ED, canciones de B小町 y de cada idol, el «falso opening» de la T3 (§13) |
| 10 · Vídeos con minuto | ✅ | 52 enlaces de YouTube comprobados; 16 vídeos mirados por *storyboard* con minuto (§4.1, §14). TikTok sólo por sus páginas de tendencia |
| 11 · Videojuegos: interfaz y cajas | ✅ | *Puzzle Star* visto en el directo de MEM; caja de diálogo de *IDOLM@STER Shiny Colors* (§15). TCRF no tiene página |
| 12 · Lo que ama el fandom y qué NO hacer | ✅ | memes, Reddit por Arctic Shift, chistes internos y 10 cosas que no hacer (§16) |
| 13 · Descripción profunda y forma de hablar | ✅ | Kana, MEM, Ruby, Ai, Akane, Aqua y 3 secundarios, con frases y minuto (§9) |
| 14 · Poses analizadas (6-10 por personaje) | ✅ | Kana 17, MEM 12, Akane 11, Ruby 9, Ai 7, con número de hoja o minuto (§10). Aqua sólo 3: no es anfitrión |
| 15 · Vestuario con hex | ✅ | uniforme rojo, «POP IN 2», uniforme de Yōtō, T3 y ropa de casa, con hex medidos (§6.2, §11) |
| 16 · Paisajes y fondos de pantalla con tamaño y autor | ✅ | tabla de fondos (§5.2) y fiestas oficiales con tamaño (§14). Los de 4kwallpapers no tienen autor |
| 17 · Guía para IA | ✅ | rasgos fijos, paleta medida, palabras que ayudan y estropean, qué imagen usar (§17) |
| 3 conceptos de lámina | ✅ | uno por canal, con objetos de Sketchfab, pose con número de hoja y textos del canal (§18) |
| 40 fuentes distintas | ✅ | 335 enlaces de 76 sitios (§20) |
| Tipos de fuente: oficiales | ✅ | web oficial, canal y X oficiales, entrevistas (Febri, Real Sound, Newtype en Crunchyroll News) |
| Tipos de fuente: otros idiomas | ✅ | japonés (Natalie, Febri, ranking.net), chino (Sina), coreano (Ruliweb, Namu Wiki) |
| Tipos de fuente: wikis, TV Tropes, TCRF, Wayback | ⚠️ | Fandom y Doblaje Wiki sí; TV Tropes da 403; TCRF no tiene página; Wayback tiene la copia pero corta la conexión |
| Tipos de fuente: foros | ✅ | Reddit por Arctic Shift, Ruliweb |
| Tipos de fuente: arte (Pixiv, ArtStation, DeviantArt) | ⚠️ | Pixiv sí (API); DeviantArt responde pero lo que sale es pequeño o hecho con IA; ArtStation no probado |
| Tipos de fuente: vídeo con minuto | ✅ | YouTube por yt-dlp y *storyboards* |
| Tipos de fuente: código y recursos | ✅ | GitHub (subtítulos, fichas de ANN, letras), Sketchfab, Poly Haven, Google Fonts |
| Tipos de fuente: doblaje latino | ⚠️ | Doblaje Wiki, ANMTV y Crunchyroll sí; entrevistas a los actores latinos en vídeo: no encontré ninguna |
| Hojas de contacto | ✅ | 3 hojas propias en `hojas/`, miradas, con tabla y enlaces (§3.0) |
| `referencias.json` (20-40, medidas) | ✅ | 40 entradas: 34 imágenes con ancho y alto medidos; 6 vídeos con `&t=` (sin tamaño: sólo *storyboard*) |

---

## 21 · Bitácora de búsqueda

### Primera pasada (24-sep-2026, red cerrada)

#### Estado de la red
- `curl https://community.fandom.com` → **000 (403 del proxy)**. Sin red
  completa: **no se usó `investigar_serie.py`, no hay hojas de contacto
  ni carpeta `hojas/`**.
- También dieron 403 (curl o WebFetch): oshinoko.fandom.com, Doblaje
  Wiki (API), Wikipedia, Crunchyroll, ANMTV, ichigoproduction.com,
  Sketchfab (API), Poly Haven (API), ambientCG, Ranker, Febri, Wayback
  Machine, Arctic Shift, App Store, Google Play, la web del juego, la CDN
  de ANN, Wikimedia, las imágenes de Fandom, YouTube e imágenes de X.
- El buscador **no admite `reddit.com`** como dominio (error 400).
- **Sí respondieron:** `raw.githubusercontent.com`, `pypi.org` (para
  instalar fontTools y Pillow) y la búsqueda de código de GitHub (MCP).
  La API de árboles de GitHub no (repos no habilitados).

#### Búsquedas hechas (47, idioma)
1. 【推しの子】 公式 キャラクター人気投票 結果 順位 有馬かな (japonés)
2. Oshi no Ko official character popularity poll results ranking (inglés)
3. Oshi no Ko doblaje latino reparto voces (español)
4. Elenco, Audiomaster Candiani, Filigrana, Carmona, Huerta, en Crunchyroll/ANMTV/Doblaje Wiki (español)
5. Voz de Aqua adolescente, director Jorge Reyes (español)
6. Reparto de Ai, Ruby, Kana, Akane y MEM en The Project Arcade/ANMTV (español)
7. Ginette Zavala, Polly Huerta, Paulina García, María García (español)
8. 第3期 キービジュアル 解禁 (japonés, natalie/animatetimes/web oficial)
9. 平山寛菜 インタビュー 目の星 (japonés)
10. Febri 平牧大輔 制作論 色彩 光 (japonés)
11. Ep. 11, Kana y la barra blanca (inglés)
12. Modelos 3D de Oshi no Ko en Sketchfab (inglés)
13. Letrero «On Air» CC en Sketchfab (inglés)
14. Letra del logo 【推しの子】 ロゴ フォント (inglés y japonés)
15. Ep. 6, redes sociales en pantalla (inglés)
16. B小町 メンバーカラー ペンライト 衣装 (japonés)
17. 【推しの子】 パズルスター 画面 (japonés)
18. T3, ep. 29 y 34, la audición (inglés)
19. MEM-cho, edad y personalidad (inglés)
20. Kana, la más popular (inglés)
21. Críticas al final del manga (inglés)
22. Memes en reddit/TV Tropes/Know Your Meme (inglés): **rechazada**, reddit.com no admitido
23. La misma sin reddit (inglés)
24. 推しの子 イラスト 有馬かな pixiv (japonés)
25. 【推しの子】 第3期 PV 公式 en YouTube (japonés)
26. «Idol» en español latino, covers y fandubs (español)
27. 최애의 아이 인기투표 결과 (coreano)
28. 我推的孩子 人气投票 结果 (chino)
29. Anime Corner, encuestas de invierno 2026 (inglés)
30. 推しの子 聖地巡礼 宮崎 高千穂 (japonés)
31. 推しの子 Blu-ray ジャケット 平山寛菜 (japonés)
32. Estrellas negras en los ojos (inglés)
33. 推しの子 演出 SNS 画面 6話 テロップ (japonés)
34. Opiniones y frases del doblaje latino (español)
35. «Stephanie Filigrana» y «Manuel Carmona» (español)
36. Traje de idol de Ai (inglés)
37. Akane, personalidad (inglés)
38. Taishi Gotanda (inglés)
39. Claqueta, barra de luz, portapapeles, aro de luz en Sketchfab (inglés)
40. Texturas CC0 en Poly Haven (inglés)
41. Tendencias de TikTok (inglés)
42. Análisis en español en YouTube (español)
43. Fondos de pantalla 4K (inglés)
44. Puzzle Star, pantallas y reseñas (japonés)
45. Letras de los globos de Yen Press (inglés)
46. Manga en español: Panini México e Ivrea (español)
47. Escena de Ai en el doblaje latino (español)

#### Por GitHub (abierto de verdad, sin cupo)
- `ToshY/anime-news-network-encyclopedia`: listado de 13.778 animes para
  hallar los 4 números de Oshi no Ko; fichas 25783, 28810, 33662, 38810
  y manga 24571; 106 titulares de noticias de ANN.
- `kienkzz/NanakoRaws-Anime-Japanese-subtitles`: 11 episodios de la T1
  (.ass y .srt), pasados a texto con su minuto y leídos.
- `jacobjuarezguerra/Oshi-No-Ko-Browser-extension-B-Komachi`:
  `newtab.js` (nombres de las 20 imágenes), `bg1`–`bg20.jpg` y logos;
  todas miradas a ojo, 4 medidas con Pillow.
- `TheFabi8A/oshi-no-ko`: README, `index.html` y 4 imágenes (el key
  visual de Ai medido).
- `google/fonts`: METADATA de 21 letras y 11 archivos .ttf revisados con
  fontTools (á é í ó ú ñ ¿ ¡ 【 】 ★ ☆ ♡).
- Búsqueda de repositorios «oshi no ko» (42) y de subtítulos (.ass):
  `foxofice/sub_share` tiene la T1 y T2 en chino (no usados).

#### Lo que NO encontré (primera pasada; revisado abajo)
- Encuesta oficial de personajes (no existe, según ABEMA Times).
- Frases del doblaje latino con fuente; doblaje latino de la T3.
- El texto del hilo fijado de #castings y las redes del servidor.
- Minutos de la T2, la T3 y de los vídeos.
- Autores de fan art; licencias exactas de Sketchfab.
- La letra oficial del logo y de los globos del manga.
- Cajas de diálogo y menús del juego; página en TCRF.
- Entrevistas en coreano o chino al staff (sólo encuestas y noticias).

### Segunda pasada (24-sep-2026, red abierta)

Se hizo en **dos tandas**: el límite de uso cortó la primera y su
carpeta de trabajo (vídeos, *storyboards*, subtítulos) se perdió; lo
escrito en la biblia y las 3 hojas sí quedaron.

#### Herramientas y lo que dieron
- **`investigar_serie.py` × 2** sobre `oshinoko.fandom.com`: personajes
  (11 páginas, 979 imágenes, 21 hojas) y sitios y episodios (22 páginas,
  531 imágenes, 12 hojas). Montaje propio de 3 hojas con Pillow.
- **API de la wiki:** texto de páginas (episodios 1, 5, 9, 11, 29, 34;
  45510; B-Komachi…), búsqueda de texto para el color de Ai
  («image color», «member color», «penlight», «glow stick»), tamaño de
  las 30 imágenes de `referencias.json` (`prop=imageinfo`) y la lista
  entera de 2963 imágenes (`list=allimages`) para buscar el origen de
  las `bg*` por tamaño (sin coincidencias) y las ilustraciones de fiestas.
- **Doblaje Wiki (API):** página de la serie (reparto, staff, datos de
  interés, errores); búsqueda de archivos de audio (`srnamespace=6`):
  ninguno de la serie.
- **ANMTV** (dos artículos abiertos), **API de noticias de Crunchyroll**
  (`cr-news-api-service…/v1/es-419/stories?slug=…` y `stories/search?tag=OSHI NO KO`:
  12 artículos; leídos el anuncio del elenco, la entrevista al director
  y el de los ojos). El anuncio de la T2 no existe con los nombres
  probados (5 fechas, 2 nombres: 404).
- **YouTube con yt-dlp:** `fotogramas.py` falla («Sign in to confirm
  you're not a bot»; probados los clientes por defecto, `tv_embedded`,
  `web_embedded` y `android_vr`). Con el cliente `mweb` sólo salen los
  *storyboards*: 16 vídeos mirados así (9 en la primera tanda, 7 en la
  segunda con un script propio, `sb.py`, en mi carpeta de trabajo).
  Canal oficial listado (496 vídeos); canal de Crunchyroll en Español
  buscado por dentro. Los 52 enlaces de la biblia, comprobados por oEmbed.
- **Subtítulos japoneses** de la emisión (NanakoRaws) bajados otra vez
  para dar minuto a las frases del doblaje (ep. 2 y 4).
- **Pillow:** colores del key visual de Crunchyroll, del «mensaje
  especial» de Akane y del estudio de doblaje (mediana por cuantización;
  en *storyboards*, ±10 por canal).
- **Sketchfab API** (15 licencias), **Pixiv** por su API `ajax/illust`
  (5 fan arts: autor, tamaño, fecha), **fontTools** (7 letras nuevas),
  **Arctic Shift** (r/OshiNoKo, jul-ago 2026), **DeviantArt** por su
  RSS (60 resultados de Kana: pequeños o hechos con IA, no usados).
- **Páginas abiertas de verdad:** Anime Corner (dos rankings), ranking.net,
  カイの漫画考察, Ruliweb (con su imagen), 4kwallpapers, ffont y BOOTH.

#### Búsquedas web (4 en la segunda tanda; la primera tanda no dejó cuenta)
1. Crunchyroll_la «OSHI NO KO» doblaje latino clip x.com (español)
2. «Oshi no Ko» doblaje latino frase Kana Ginette Zavala escena clip (español)
3. WDN_Topic «Oshi No Ko» doblaje latino clip (español)
4. «así suena» / «así se escucha» doblaje latino «Oshi no Ko» (español)

Ninguna dio un clip oficial doblado: sólo anuncios, reacciones y
posts sin vídeo (yt-dlp lo confirmó en tres de ellos).

#### Siguen cerrados o fallan
- TV Tropes (403), Ranker (401), sina.cn (bloqueado por el proxy),
  Wayback Machine (la API `archive.org/wayback/available` responde y hay
  copia del ep. 6 oficial de 12-feb-2026, pero `web.archive.org` corta
  la conexión: 2 intentos), MyAnimeList por Jikan (504), TikTok por
  yt-dlp (error), BOOTH para bajar la letra (pide sesión), descarga de
  vídeo y audio de YouTube.

#### Los «no encontré» de la primera pasada, revisados
- Encuesta oficial de personajes → **sigue sin existir** (ABEMA Times);
  las de fans, abiertas y corregidas (§2).
- Frases del doblaje latino con fuente → **2 encontradas** (Doblaje
  Wiki) y **con minuto**; clips oficiales doblados, **no hay**.
- Doblaje latino de la T3 → **no hay** (Doblaje Wiki + ANMTV).
- Texto del hilo fijado de #castings y redes del servidor → **siguen
  sin estar** en el inventario.
- Minutos de la T2, la T3 y de los vídeos → los de los vídeos, **sí**
  (16 vídeos); la T3 tiene subtítulos en GitHub (indonesio), no hacían
  falta.
- Autores de fan art; licencias de Sketchfab → **encontrados** (Pixiv y
  Sketchfab por sus API).
- Letra oficial del logo y de los globos del manga → **sigue sin
  encontrarse**; el logo, al menos, es mincho.
- Cajas de diálogo y menús del juego → **encontrados** (*Puzzle Star*
  en el directo de MEM; caja de *IDOLM@STER Shiny Colors*); TCRF no
  tiene página.
- Entrevistas en coreano o chino al staff → **siguen sin encontrarse**;
  sí una entrevista japonesa (Newtype) traducida por Crunchyroll.

#### Marcas de duda
Había **52** al empezar la segunda pasada; quedan **29** con
`grep` (23 de datos; el resto son la leyenda, el resumen del
principio y la tabla de cumplimiento). Lo que queda es, sobre todo: lo
que no está en el inventario (hilo fijado, redes), voces latinas y datos
de producción con una sola fuente, encuestas que no se pudieron abrir,
el origen de las `bg*`, las letras (logo, globos, «推しゴ») y el color de
Ai.
