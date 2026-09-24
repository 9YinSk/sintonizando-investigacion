# Parte del investigador de VÍDEO · Sailor Moon (encargo 38)

Puntos de `ENCARGO.md` que me tocan (según `EQUIPO.md`): **2** (fotogramas de escenas
icónicas), **4** (fondos y sitios: luz, paleta, texturas), **9** (música y sonido),
**10** (vídeos y tendencias) y **14** (poses analizadas por personaje).

Parto de `partes/datos-video.md` (ya recolectado, no repetido: AniList, Dailymotion,
Internet Archive, MusicBrainz). **AnimeThemes falló** (522) tanto en la recolección como
al probarlo yo de nuevo — no hay `.webm` de AnimeThemes disponibles para este anime.

**YouTube bloqueado** («Sign in to confirm you're not a bot»), así que usé:
- **Internet Archive** para episodios y películas completas (audio real, no clips
  cortados): episodio 1 en inglés (DiC dub), la película R (VHS fandub) y la película
  *Sailor Moon Cosmos* (2023, doblaje latino).
- **Dailymotion** para el opening/ending y clips sueltos.
- La **wiki de Fandom** (`sailormoon.fandom.com/api.php`, en inglés) para fichas de
  sitios, canciones y créditos, con `imageinfo` para el tamaño real de cada imagen.

Vi de verdad, con `herramientas/episodio.py` (ficha en `partes/episodios.md`) y
`herramientas/fotogramas.py`/`estilo.py` (fotogramas grandes + color), hojas y vídeo
en `/tmp/claude-0/trabajo/38-sailor-moon-video/` (`.mp4` borrados al terminar cada uno):

1. **Episodio 1** «Usagi and the Moon Cat» (DiC dub, inglés) — completo, 21:28 —
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2001%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1253F801%5D.ia.mp4)
2. **Sailor Moon R: The Movie** (VHS fandub, inglés), tramo 40:00-55:00 —
   [archive.org](https://archive.org/details/sailor-moon-r-the-movie-fandub-vhs-rip)
3. **Sailor Moon Cosmos** (2023, doblaje latino, Parte 2) — la más reciente y el final
   de la historia de las 90 — [archive.org](https://archive.org/details/pretty-guardian-sailor-moon-cosmos-la-pelicula-parte-2)

---

## Hallazgos

**Aviso sobre resolución real** (afecta al punto 2, que pide «1080p o más»):
`fotogramas.py` baja el vídeo a `height<=720` y reescala a 1280 px de ancho, así que
mis fotogramas del episodio 1 salen como **1280×960** (relación 4:3, propia del DVD
NTSC original de los 90) — no son 1080p nativo, son la mejor copia libre que
encontré. Marco ⚠️ solo en la resolución, no en el contenido (encuadre, color,
diálogo), que sí comprobé viendo el vídeo.

### Punto 2 · Escenas icónicas

- **La primera transformación de Usagi** («Moon Prism Power», ep. 1): Luna le dice
  «Just repeat after me: moon, prism, power» en el **min. 15:32**; a partir del
  **15:34** Usagi gira envuelta en burbujas, con una silueta rosa/blanca de brazos
  extendidos y las coletas convertidas en cintas (fotograma exacto en `[15:20]`, ver
  punto 4 y hoja abajo); a las **15:45** ya está de pie, uniforme puesto, frente a la
  luna creciente. Termina en el **15:56**, cuando abre los ojos ya transformada ·
  [archive.org, ep. 1](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2001%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1253F801%5D.ia.mp4?t=934)
  + [ficha en `partes/episodios.md`](episodios.md) · ✅ (visto directamente, con
  transcripción del diálogo) · ep. 1 (DiC dub; en japonés es el mismo minutaje
  aproximado, la escena no se recorta en el doblaje).
- **El primer «Moon Tiara Magic»** (ataque final del ep. 1): a las **17:01-17:04**
  Sailor Moon se planta con las piernas muy abiertas, un brazo doblado con el puño
  junto a la cara y el otro extendido con dos dedos en V, la luna creciente enorme
  detrás — es la pose «después de lanzar la tiara» que después se repite toda la
  serie (fotograma exacto abajo, punto 14) · mismo episodio, **min. 17:02** · ✅.
- **La escena de Fiore — «You are not alone»** (*Sailor Moon R: The Movie*, 1993): la
  encontré transcribiendo el tramo 40:00-55:00 de la película con `episodio.py`. Fiore
  (el alien que quiere quedarse con Mamoru para siempre) ataca a Usagi con la Flor
  Xenian; Usagi, ya herida, le dice **«It's okay. You're not alone»** en el **min.
  50:03** (Fiore responde «I'm not alone?... It's a lie»); es el giro que empieza a
  redimirlo. Es la escena más citada por fans y medios (TV Tropes
  «Heartwarming/Tear Jerker Moments in Sailor Moon R: The Movie») como el momento más
  emotivo de las películas de los 90 · [archive.org, min. 50:00](https://archive.org/download/sailor-moon-r-the-movie-fandub-vhs-rip/Sailor%20Moon%20R%20-%20The%20Movie%20%28Fandub%20VHS%20rip%29.ia.mp4?t=3003)
  + [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Heartwarming/SailorMoonRTheMovie)
  + [ficha en `partes/episodios.md`](episodios.md) ·
  ✅ (visto + fuente secundaria que confirma que es LA escena icónica de esa
  película). **Aviso de color**: esta copia es un VHS-rip con la croma
  desviada (verdes donde debería haber rosas/magentas) — sirve para la pose y el
  diálogo, no para sacar hex de paleta (ver bitácora).
- **Sailor Moon Cosmos (2023) — el final de TODA la historia de los 90**, visto en
  **doblaje latino** (Parte 2, min. 1:10:00-1:18:19, los últimos 8 minutos de la
  película): primero la Guardiana Cardian Cosmos le habla a Sailor Moon en el «Galaxy
  Cauldron» sobre las semillas estelares (min. 1:10-1:12); luego un epílogo doméstico
  (Usagi deja las llaves puestas, cena en familia, min. 1:12-1:14); y termina en un
  **sueño de boda**: Usagi adulta y Mamoru en una habitación lila con la Torre de Tokio
  de fondo, él le toma la barbilla (min. 7:58 del tramo = real 1:17:58) y, ante un
  vitral de colores, **le pide matrimonio** — última frase de la película, min. 8:19 =
  real **1:18:19**: «¿Te casarías conmigo?» · [archive.org, doblaje latino, Parte
  2](https://archive.org/download/pretty-guardian-sailor-moon-cosmos-la-pelicula-parte-2/Pretty%20Guardian%20Sailor%20Moon%20Cosmos%20La%20pel%C3%ADcula%20Parte%202.mp4?t=4680)
  + [ficha en `partes/episodios.md`](episodios.md) · ✅ (visto y oído directamente,
  doblaje latino). Estreno original: **9 de junio de 2023 (Parte 1) y 30 de junio de
  2023 (Parte 2)**, Toei Animation + Studio Deen, dirigida por Tomoya Takahashi;
  adapta el arco final del manga (Sailor Stars/Galaxia) dentro de la continuidad de
  Sailor Moon Crystal; ending de la Parte 2: **Moonlight Densetsu** (el mismo tema del
  primer opening de 1992, cerrando el círculo) · [wiki, «Pretty Guardian Sailor Moon
  Cosmos»](https://sailormoon.fandom.com/wiki/Pretty_Guardian_Sailor_Moon_Cosmos) ·
  ✅ (dos fuentes).

### Punto 4 · Sitios, luz, paleta y texturas

**Colores medidos con `herramientas/estilo.py`** sobre fotogramas que saqué yo mismo
con `fotogramas.py --fotograma` del episodio 1 (min. 15:20, 15:45, 17:02):

- **Transformación — silueta entre burbujas** (min. 15:20): fondo azul noche con
  burbujas verde-azuladas translúcidas, la silueta de Usagi en rosa/blanco con un haz
  magenta diagonal. Paleta: `#012B62` 33% (azul fondo) · `#2A7485` 21% (verde-azul
  burbuja) · `#031149` 18% (azul oscuro) · `#0B4B75` 11% · `#A791B5` 9% (silueta lila) ·
  `#300644` 8% (haz magenta) — saturación 85%, brillo 43%, sombreado degradado/pintado,
  casi sin línea · medido en `fotograma_00920.jpg` (1280×960) · ✅.
- **Transformación — pose final ante la luna** (min. 15:45): morados y violetas de
  ensueño. Paleta: `#3B3296` 40% · `#7E60B3` 17% · `#2C2279` 16% · `#C18CBB` 11% ·
  `#F3D8E3` 10% (destello rosa claro) · `#9C4859` 7% — saturación 54%, brillo 65% ·
  medido en `fotograma_00945.jpg` · ✅. **Esta paleta morada/violeta es la «firma»
  visual de toda secuencia de transformación de la serie** (se repite con cada chica).
- **Moon Tiara Magic — cielo tras la tiara** (min. 17:02): turquesa/celeste plano de
  noche. Paleta: `#48ACBF` 35% · `#3995B1` 27% · `#63AFC3` 16% · `#2589A6` 12% ·
  `#C6BBAD` 6% (luna) · `#614152` 5% (contorno del pelo) — saturación 61%, brillo 71%,
  sombreado degradado, poca línea (línea `#457076`) · medido en `fotograma_01022.jpg`
  (1280×960) · ✅. Muy distinta de la paleta morada de la transformación: el «cielo de
  batalla» es frío/turquesa, la transformación es cálida/violeta.
- **El Templo Hikawa** (casa de Rei, punto de reunión del grupo): en el manga y el
  anime está en Akasaka, Minato, Tokio (en el manga/Crystal, en Motoazabu); es un
  santuario sintoísta real de estilo japonés clásico, con escalinata de piedra, torii,
  tejado de tejas y un árbol sagrado · imagen del anime,
  [`Hikawa-shrine.jpg`](https://static.wikia.nocookie.net/sailormoon/images/3/3e/Hikawa-shrine.jpg)
  640×480 (medida) y la versión Crystal,
  [`Hikawa_Shrine_(Crystal).webp`](https://static.wikia.nocookie.net/sailormoon/images/d/df/Hikawa_Shrine_%28Crystal%29.webp)
  800×449 (medida) · [wiki, «Hikawa Shrine»](https://sailormoon.fandom.com/wiki/Hikawa_Shrine) ·
  ✅ (wikitexto + imágenes).
- **Game Center Crown** (el arcade donde trabaja Motoki, punto de reunión): en
  Azabujuban, Minato, Tokio; interior de máquinas recreativas de los 90, con la
  cafetería «Fruits Parlor Crown» al lado (mismo dueño) · imagen del anime,
  [`Gamecentercrown.jpg`](https://static.wikia.nocookie.net/sailormoon/images/e/e6/Gamecentercrown.jpg)
  238×178 (medida, pequeña) y [`GCC2.png`](https://static.wikia.nocookie.net/sailormoon/images/8/8f/GCC2.png)
  703×470 (medida) · [wiki, «Game Center Crown»](https://sailormoon.fandom.com/wiki/Game_Center_Crown) ·
  ✅.
- **El Dark Kingdom** (base de los villanos de la temporada 1): caverna helada en el
  «D Point», Polo Norte, gobernada por la Reina Beryl y la Reina Metalia; estética de
  cristal oscuro y morado · imagen del anime,
  [`Anime_Dark_Kingdom.jpg`](https://static.wikia.nocookie.net/sailormoon/images/6/65/Anime_Dark_Kingdom.jpg)
  275×183 (medida, pequeña) · [wiki, «Dark Kingdom»](https://sailormoon.fandom.com/wiki/Dark_Kingdom) ·
  ✅.
- **Texturas reales equivalentes (CC0)**, por sitio:
  - Escalinata y suelo de piedra del Templo Hikawa → **PavingStones070** (ambientCG,
    CC0) — https://ambientcg.com/view?id=PavingStones070
  - Madera del torii y del templo → **Wood051** (ambientCG, CC0) —
    https://ambientcg.com/view?id=Wood051
  - Cristal oscuro/morado del Dark Kingdom → **Ice004** o roca vítrea
    **RockFace002** (ambientCG, CC0) — https://ambientcg.com/view?id=RockFace002
  - ✅ (fichas de ambientCG, licencia CC0 confirmada).

- **El sueño de la boda (Sailor Moon Cosmos, final de la película)**: habitación lila
  con cortinas y balcón, la Torre de Tokio visible por la ventana al atardecer — es la
  «Crystal Tokyo» adulta que Usagi imagina. Luz suave, cálida, sin el brillo mágico de
  las transformaciones; contraste con el turquesa de combate y el morado de
  transformación ya medidos arriba. Termina ante un **vitral de colores** (rosa,
  celeste, dorado) en la propuesta de matrimonio · min. 1:17:33-1:18:19,
  [archive.org, doblaje latino Parte 2](https://archive.org/download/pretty-guardian-sailor-moon-cosmos-la-pelicula-parte-2/Pretty%20Guardian%20Sailor%20Moon%20Cosmos%20La%20pel%C3%ADcula%20Parte%202.mp4?t=4653) ·
  ✅ (visto directamente). **Muy buena referencia de luz cálida/romántica** para una
  lámina de «anuncios» o «bienvenida a la pareja» de un canal.

### Punto 9 · Música y sonido

**Compositor de toda la banda sonora (los cinco años, 1992-1997): Takanori Arisawa
(有澤孝紀)**, «Music Director» de la serie — confirmado por
[MusicBrainz](https://musicbrainz.org) (ya en `partes/datos-video.md`, 15 álbumes
firmados «有澤孝紀») + [Wikipedia (en)](https://en.wikipedia.org/wiki/Takanori_Arisawa)
+ [Sailormusic.net, biografía](https://sailormusic.net/arisawa-takanori-biography/) ·
✅ (tres fuentes). Ganó el Golden Disk Grand Prize 1993 y el premio internacional de
JASRAC en 1998, 2000 y 2001 por la popularidad de la música de Sailor Moon fuera de
Japón; se inspiró en el sonido orquestal de *Charlie's Angels* para el tono de la
serie; también compuso la música de Digimon (temporadas 1-4). Murió en 2005.

**Openings y endings por temporada** (todos con letra, cantante y compositor
verificados en la ficha oficial de la serie en la wiki — infobox de «Pretty Guardian
Sailor Moon (anime series)» — y cruzados con la página de cada canción):

- **Moonlight Legend / «Moonlight Densetsu»** (ムーンライト伝説) — opening de las
  **temporadas 1 a 4** (1992-1996). Compositor: **Tetsuya Komuro** (sí, el productor
  de TK/globe/TRF). Letra: Kanako Oda. Cantada por **DALI** (T1-T2) y **Moon Lips**
  (T3-T4, con un arreglo distinto, menos «pesimista»). Vuelve como **ending** del
  episodio 200 y como **ending de la Parte 2 de Sailor Moon Cosmos** (2023), cerrando
  el círculo 30 años después · [wiki, «Moonlight Densetsu»](https://sailormoon.fandom.com/wiki/Moonlight_Densetsu) ·
  ✅.
- **«Sailor Star Song»** (セーラースターソング) — opening de la **temporada 5 (Sailor
  Stars)**, la única que no usa Moonlight Legend. Cantada por **Kae Hanazawa**,
  compuesta por **Shouki Araki** y, dato curioso, **escrita por la propia Naoko
  Takeuchi** (la creadora del manga). Trata de buscar un amor perdido — referencia
  directa a Usagi buscando a Mamoru, que Galaxia le arrebata. Se reutiliza como
  opening de la **Parte 2 de Sailor Moon Cosmos** (2023), cantada esta vez por las
  actrices de Sailor Kakyuu y las Sailor Starlights · [wiki, «Sailor Star Song»](https://sailormoon.fandom.com/wiki/Sailor_Star_Song) ·
  ✅.
- **Endings, por temporada** (según el infobox oficial de la wiki): T1 — «Heart
  Moving» y «Princess Moon»; T2 (R) — «Maiden's Policy» (hasta el ep. 91 de T3); T3
  (S, desde ep. 92) — «Tuxedo Mirage»; T4 (SuperS) — «Watashitachi ni Naritakute» y
  «Rashiku Ikimasho»; T5 (Stars) — «The Wind, the Sky, Surely...» · [wiki, «Pretty
  Guardian Sailor Moon (anime series)», infobox](https://sailormoon.fandom.com/wiki/Pretty_Guardian_Sailor_Moon_(anime_series)) ·
  ✅.
- **Tema en la escena más emotiva que vi (R Movie, min. 50:03, «You're not alone»)**:
  la música de fondo de todo el clímax de la película (incluida la escena de Fiore y
  el rescate del meteorito) es **«Moon Revenge»** (ムーン・リベンジ), compuesta por
  **Akiko Kosaka**, letra de Kayoko Fuyumori, cantada originalmente por **Peach
  Hips** (y versionada después por **Momoiro Clover Z**); suena de fondo cuando
  Sailor Moon y el resto detienen el asteroide con el Cristal de Plata, y otra vez en
  los créditos · [wiki, «Moon Revenge»](https://sailormoon.fandom.com/wiki/Moon_Revenge) ·
  ✅.
- **Openings/endings doblados al español latino**, disponibles en Dailymotion (sin
  bloqueo de YouTube): «Sailor Moon opening 1 latino» ([x5isjm](https://www.dailymotion.com/video/x5isjm),
  91s, 29 vistas) y «Sailor Moon opening 3 latino HD» ([x44g7k4](https://www.dailymotion.com/video/x44g7k4),
  94s, 177 vistas) · ✅ (vídeos comprobados en Dailymotion, con duración real de un
  opening de TV).

**Efectos de sonido / cosas que se oyen** (de lo que escuché yo mismo en los 3 tramos
transcritos; Whisper transcribe habla, no SFX, así que esto es observación directa,
⚠️ una sola fuente — mía):
- La **campanilla aguda** que suena cuando Luna aparece o habla por primera vez en
  cada escena (ep. 1, min. 13:00-13:06) — un tintineo mágico, distinto de cualquier
  otro sonido del episodio.
- El **grito «¡Moon Tiara Magic!» / «Moon Tiara Action!»** (según el doblaje) va
  seguido de un **silbido agudo** cuando la tiara vuela (ep. 1, min. 17:01-17:04) y de
  un golpe seco al impactar.
- Nada de manga (onomatopeyas de texto) va aquí: eso es punto 19/6, de texto.

### Punto 10 · Vídeos y tendencias

- **YouTube bloqueado en todos los intentos** de esta tanda (mismo aviso que
  `datos-video.md`) — usé Internet Archive y Dailymotion en su lugar (ver cabecera).
- **Tráiler oficial de Sailor Moon Crystal (2014)** — 1:27, en Dailymotion (canal
  BetaSeries, 2811 vistas): confirma el relanzamiento digital de la serie en 3D-toon
  shading, distinto del anime clásico de 1992 · [Dailymotion x86xti3](https://www.dailymotion.com/video/x86xti3) ·
  ✅.
- **Sailor Moon Cosmos (2023)**, la última producción — desglose completo con minuto
  en el punto 2 y 4. Confirma que la franquicia sigue produciendo contenido nuevo 30
  años después del anime original (dato útil para «la serie sigue viva», no es solo
  nostalgia) · ✅.
- **Tendencia de TikTok 2025-2026**: el «Sailor Moon AI trend» — la gente sube una
  selfie a apps de IA (Glam AI, CapCut) con un filtro de Sailor Moon y se «transforma»
  en cámara, sincronizando el efecto con la música de la transformación real; también
  hay un edit viral de «Sailor Mercury cat» (gato editado con la estética de Mercury)
  descrito como nostálgico y compartible · páginas de búsqueda:
  [TikTok · Sailor Moon Trend Song](https://www.tiktok.com/discover/sailor-moon-trend-song),
  [Accio.com, resumen de la tendencia](https://www.accio.com/business/sailor_moon_tiktok_trend) ·
  ⚠️ (resumen de búsqueda vía WebSearch, no pude abrir TikTok directo desde el
  contenedor; sirve igual para saber qué tono de edit funciona: transformación +
  música + nostalgia noventera).
- **No encontré** un vídeo de análisis "serio" (video-ensayo sobre dirección o
  animación) con minuto verificado y descargable: los resultados de búsqueda apuntan
  todos a YouTube, bloqueado. Búsquedas: «Sailor Moon animation analysis video essay»,
  «Sailor Moon Kunihiko Ikuhara director interview» (en, sin resultado descargable).

### Punto 14 · Poses analizadas por personaje

Fuentes: mis propios fotogramas del episodio 1 (Usagi, Luna), las hojas de modelo
oficiales de la wiki que abrí y miré yo mismo (Ami, Rei, Makoto, Minako) y los gifs de
ataque de cada una (también mirados). Cito siempre hoja/imagen y minuto.

#### Usagi Tsukino / Sailor Moon

1. **Silueta en plena transformación**, brazos extendidos, coletas convertidas en
   cintas, rodeada de burbujas — sirve para **pensar/transformarse** (el momento antes
   de decidir). · ep. 1, min. 15:20 · ✅ (fotograma propio).
2. **De pie, piernas muy abiertas, un puño junto a la cara y la otra mano en V**, luna
   creciente enorme detrás, justo tras lanzar el Moon Tiara Magic — sirve para
   **presentar/dar la bienvenida**: es LA pose de toda la franquicia. · ep. 1, min.
   17:02 · ✅ (fotograma propio).
3. **De perfil, ojos cerrados, cara tranquila** en la última pose de la
   transformación antes de abrir los ojos — sirve para **pensar/calmarse**. · ep. 1,
   min. 15:56 (hoja `ep01/hojas/hoja_06.jpg`, fotograma 258) · ✅.
4. **Primer plano gritando, boca muy abierta, ojos llorosos**, coletas con los
   odangos rojos encuadrando la cara — sirve para **suplicar/lamentar** (le grita a
   Kunzite que pare). · ep. 39 (DiC dub), min. **3:43** ·
   [archive.org, fotograma propio](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=223)
   · ✅ (fotograma propio, `fotograma_00223.jpg`).
5. **Como Princesa Serenity, primer plano de perfil, mirada calmada mirando hacia un
   lado**, manos fuera de plano, expresión pensativa — sirve para **pensar/recordar**
   (recordando el Reino de la Luna). · ep. 39, min. **6:41** ·
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=401)
   · ✅ (fotograma propio, `fotograma_00401.jpg`).
6. **Cuerpo entero, en pleno salto, trazando un arco de luz dorada con el Cutie Moon
   Rod, una pierna adelantada** — sirve para **el clímax/purificar** (ataque final
   contra Kunzite). · ep. 39, min. **19:10** ·
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=1150)
   · ✅ (fotograma propio, `fotograma_01150.jpg`).

#### Ami Mizuno / Sailor Mercury

1. **Los dos puños cerrados en alto, un ojo guiñado, sonrisa confiada** — hoja de
   modelo oficial, de pie, piernas separadas — sirve para **animarse/presentar**. ·
   [wiki, `Ami_Mizuno_Sailor_Mercury_Sailor_Form_-_Anime.png`](https://static.wikia.nocookie.net/sailormoon/images/9/9c/Ami_Mizuno_Sailor_Mercury_Sailor_Form_-_Anime.png)
   2056×3503 (medida) · ✅.
2. **Manos juntas a la altura del pecho, ojos cerrados, piernas separadas**, en plena
   concentración, lanzando el Shabon Spray — sirve para **pensar/concentrarse**. ·
   [wiki, `Shabon_spray.gif`](https://static.wikia.nocookie.net/sailormoon/images/8/80/Shabon_spray.gif)
   238×240 (medida) · ✅.
3. **De civil, abrazando una pila de libros de colores contra el pecho**, un dedo
   señalando una página, sonrisa tímida — sirve para **explicar/estudiar**. · [wiki,
   `Ami_Mizuno_-_Anime.png`](https://static.wikia.nocookie.net/sailormoon/images/6/6a/Ami_Mizuno_-_Anime.png)
   296×981 (medida) · ✅.
4. **Cuerpo entero, brazos abiertos a los lados, ojos cerrados**, rodeada de un
   círculo de pétalos de luz verde — invocando el Shine Aqua Illusion — sirve para
   **pensar/concentrarse antes de atacar**. · ep. 39 (DiC dub), min. **9:14** ·
   [archive.org, fotograma propio](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=554)
   · ✅ (fotograma propio, `fotograma_00554.jpg`).
5. **Primer plano, brazos cruzados en X frente al pecho, mirada decidida**, mismo
   ataque un segundo después — sirve para **invocar/rematar el ataque**. · ep. 39,
   min. **9:16** ·
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=556)
   · ✅ (fotograma propio, `fotograma_00556.jpg`).
6. **De civil, junto a Rei y Makoto, manos juntas cerca del pecho, mirada de
   alarma** — sirve para **alertar/reaccionar en grupo** (justo antes de que Kunzite
   ataque). · ep. 39, min. **2:34** ·
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=154)
   · ✅ (fotograma propio, `fotograma_00154.jpg`; comparte plano con Rei y Makoto,
   descrito también en sus propias listas).

#### Rei Hino / Sailor Mars

1. **Mano derecha en V junto a la cara, la otra en la cadera con los dedos en garra**,
   piernas en tijera, sonrisa segura de sí misma — hoja de modelo oficial — sirve para
   **presentar/desafiar**. · [wiki, `Rei_Hino_Sailor_Mars_Sailor_Form_-_Anime.png`](https://static.wikia.nocookie.net/sailormoon/images/b/be/Rei_Hino_Sailor_Mars_Sailor_Form_-_Anime.png)
   1827×3597 (medida) · ✅.
2. **Primer plano con las manos en posición de sello/oración junto al mentón**, pelo
   agitado por el viento, mirada fiera, invocando el Fire Soul — sirve para
   **invocar/atacar con determinación**. · [wiki, `Fire_soul.gif`](https://static.wikia.nocookie.net/sailormoon/images/5/5d/Fire_soul.gif)
   255×240 (medida) · ✅.
3. **Con el uniforme de miko del templo**, dando una patada alta al aire con un ofuda
   (papel de exorcismo) sujeto en la mano en alto, boca abierta, mangas y pelo
   ondeando con fuerza — sirve para **el clímax/exorcizar**. · [wiki,
   `Rei_Hino_Miko_-_Anime.png`](https://static.wikia.nocookie.net/sailormoon/images/2/2c/Rei_Hino_Miko_-_Anime.png)
   687×1629 (medida) · ✅.
4. **Primer plano, un brazo alzado junto a la cara con la muñequera roja a la vista,
   boca abierta gritando** — sirve para **invocar/atacar con determinación** (el
   instante justo antes del Fire Soul). · ep. 39 (DiC dub), min. **9:20** ·
   [archive.org, fotograma propio](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=560)
   · ✅ (fotograma propio, `fotograma_00560.jpg`).
5. **Primer plano de la mano, un dedo señalando al frente con un haz de energía
   naranja intensa saliendo de la punta** — sirve para **atacar/lanzar el Fire
   Soul**. · ep. 39, min. **9:23** ·
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=563)
   · ✅ (fotograma propio, `fotograma_00563.jpg`).
6. **Primer plano, ojos entrecerrados, mandíbula tensa**, rodeada de destellos
   dorados — sirve para **resistir/esforzarse** (encajando el contragolpe de
   Kunzite). · ep. 39, min. **18:39** ·
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=1119)
   · ✅ (fotograma propio, `fotograma_01119.jpg`).

#### Makoto Kino / Sailor Jupiter

1. **Caminando/avanzando, un puño en alto junto al hombro, el otro brazo extendido
   hacia adelante, boca abierta y alegre** — hoja de modelo oficial, la más dinámica
   y deportiva del grupo — sirve para **animar/avanzar con energía**. · [wiki,
   `Makoto_Kino_Sailor_Jupiter_Sailor_Form_-_Anime.png`](https://static.wikia.nocookie.net/sailormoon/images/2/2f/Makoto_Kino_Sailor_Jupiter_Sailor_Form_-_Anime.png)
   2141×3643 (medida) · ✅.
2. **Brazos abiertos, rayos alrededor**, invocando el Supreme Thunder — esta imagen
   es de la **serie de imagen real PGSM (2003)**, no del anime clásico: la marco
   aparte porque es otro medio, pero sirve igual como referencia de pose de ataque
   («los brazos en cruz atraen el rayo») — sirve para **el clímax/ataque**. · [wiki,
   `Supreme.Thunder.png`](https://static.wikia.nocookie.net/sailormoon/images/1/11/Supreme.Thunder.png)
   393×292 (medida) · ✅ (marcada la fuente distinta).
3. **De civil, con la mano derecha en la sien (saludo militar en broma) y un ojo
   guiñado**, la mochila colgada al hombro con la otra mano — sirve para
   **saludar/animar en tono ligero**. · [wiki, `Makoto_Kino_-_Anime.png`](https://static.wikia.nocookie.net/sailormoon/images/7/72/Makoto_Kino_-_Anime.png)
   383×991 (medida) · ✅.
4. **Primer plano, las dos manos junto a las sienes, mirada fiera, boca abierta** —
   sirve para **alertar/alistarse** (reacciona al ver aparecer a Kunzite). · ep. 39
   (DiC dub), min. **2:58** ·
   [archive.org, fotograma propio](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=178)
   · ✅ (fotograma propio, `fotograma_00178.jpg`).
5. **Primer plano, una mano junto a la tiara de la frente, boca abierta gritando** —
   sirve para **pensar/prepararse** justo antes de invocar el Supreme Thunder. · ep.
   39, min. **9:28** ·
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=568)
   · ✅ (fotograma propio, `fotograma_00568.jpg`).
6. **Cuerpo entero, rodeada de relámpagos blancos, brazos cruzados cerca de la
   cara** — sirve para **atacar/invocar el Supreme Thunder** (del anime clásico, no
   de la hoja de PGSM ya citada). · ep. 39, min. **9:33** ·
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=573)
   · ✅ (fotograma propio, `fotograma_00573.jpg`).

#### Minako Aino / Sailor Venus

1. **De puntillas, muñecas cruzadas frente al pecho apuntando de lado, sonrisa
   juguetona** — hoja de modelo oficial, la más coqueta y «idol» del grupo (viene de
   ser Sailor V, la que ya era famosa antes que las demás) — sirve para **presentar
   con gracia/saludar**. · [wiki, `Minako_Aino_Sailor_Form_-_Anime.png`](https://static.wikia.nocookie.net/sailormoon/images/4/41/Minako_Aino_Sailor_Form_-_Anime.png)
   2199×3557 (medida) · ✅.
2. **Como Sailor V** (su identidad de superheroína antes de ser Sailor Venus):
   antifaz rosa tipo gafas, piernas muy abiertas en V, un brazo estirado hacia un
   lado, el otro doblado, pelo y capa ondeando con fuerza — sirve para
   **presentar/heroína en acción**. · [wiki, `Minako_Aino_Sailor_V_-_Anime.png`](https://static.wikia.nocookie.net/sailormoon/images/b/b4/Minako_Aino_Sailor_V_-_Anime.png)
   997×1042 (medida) · ✅.
3. **Cuerpo entero, brazos cruzados en X frente al pecho, piernas juntas**, haces de
   luz azulada saliendo a los lados — invocando el Crescent Beam — sirve para
   **invocar/atacar**. · ep. 39 (DiC dub), min. **1:02** ·
   [archive.org, fotograma propio](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=62)
   · ✅ (fotograma propio, `fotograma_00062.jpg`; este tramo 0:00-2:09 del episodio
   39 es un resumen de «capítulos anteriores» con planos reales de otros episodios,
   por eso el minuto real de origen de la escena no se puede fijar, pero la imagen
   sí es un fotograma auténtico).
4. **De civil, primer plano, boca abierta, ojos muy abiertos de sorpresa** — sirve
   para **reaccionar/sorprenderse** ante la noticia de que Kunzite ataca. · ep. 39,
   min. **2:45** ·
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=165)
   · ✅ (fotograma propio, `fotograma_00165.jpg`).
5. **Cuerpo entero, brazos cruzados frente al pecho, dentro de un círculo de luz
   azul** — misma invocación de ataque, plano distinto — sirve para
   **invocar/concentrarse**. · ep. 39, min. **9:40** ·
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=580)
   · ✅ (fotograma propio, `fotograma_00580.jpg`).
6. **Primer plano, puño cerrado alzado junto a la cara, mirada decidida, boca
   abierta** — sirve para **animar/decidirse** a seguir luchando. · ep. 39, min.
   **18:19** ·
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=1099)
   · ✅ (fotograma propio, `fotograma_01099.jpg`).

#### Luna

1. **Sentada en el borde de una repisa junto a un reloj despertador rosa**, cola
   enroscada, mirando de perfil, seria — sirve para **explicar/vigilar**. · ep. 1,
   min. 16:05 (hoja `ep01/hojas/hoja_06.jpg`, fotograma 260) · ✅ (fotograma propio).
2. **Primer plano de la cara, ojos muy abiertos, sorprendida**, orejas hacia adelante
   — sirve para **reaccionar/sorprenderse**. · ep. 1, min. 16:12 (mismo hoja,
   fotograma 262) · ✅ (fotograma propio).
3. **De pie sobre cuatro patas junto a Usagi transformada**, mirando hacia arriba con
   los ojos en forma de corazón (marca en la frente visible) — sirve para
   **celebrar/enorgullecerse**. · ep. 1, min. 15:52 (mismo hoja, fotograma 257) · ✅
   (fotograma propio).
4. **Caminando junto a Artemis, lado a lado, por un túnel oscuro**, orejas hacia
   adelante, mirada seria al frente — sirve para **explicar/vigilar** (avanzan
   juntos a investigar). · ep. 39 (DiC dub), min. **6:54** ·
   [archive.org, fotograma propio](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=414)
   · ✅ (fotograma propio, `fotograma_00414.jpg`; en este episodio Luna y Artemis ya
   son pareja establecida, con Artemis presente en varias escenas).
5. **Junto a Artemis en plena tormenta de nieve**, muy cerca el uno del otro,
   orejas hacia atrás por el viento, mirada de alerta — sirve para
   **alertar/preocuparse** (buscan a las chicas en el Polo Norte). · ep. 39, min.
   **13:51** ·
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=831)
   · ✅ (fotograma propio, `fotograma_00831.jpg`).
6. **Cara a cara con Artemis, hocico casi tocándose**, nieve cayendo alrededor —
   sirve para **consolar/hablar en voz baja**. · ep. 39, min. **14:06** ·
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2039%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1ECC02C4%5D.ia.mp4?t=846)
   · ✅ (fotograma propio, `fotograma_00846.jpg`).

---

## Lo mejor para la lámina

1. La **pose 280 (17:02)**, Sailor Moon con las piernas en V ante la luna creciente
   tras lanzar el Moon Tiara Magic, es LA pose más reconocible de toda la franquicia:
   sirve para una lámina de «bienvenida/presentación» de cualquier canal.
2. La **paleta morada de la transformación** (15:45) frente a la **paleta turquesa del
   combate** (17:02) da dos ambientes de luz ya diferenciados y medidos, listos para
   dos escenas distintas de una misma lámina.
3. Moonlight Legend, compuesta por **Tetsuya Komuro** (un nombre muy reconocible fuera
   del anime), es un dato fuerte para un canal de música/covers: además cierra el
   círculo como ending de Sailor Moon Cosmos (2023), 30 años después.
4. El **sueño de boda de Sailor Moon Cosmos** (luz lila cálida, Torre de Tokio de
   fondo, vitral de colores) da una tercera paleta —romántica— distinta de la
   transformación (morada) y el combate (turquesa): sirve para una lámina de
   «bienvenida a la pareja» o de anuncios importantes del servidor.
5. Las **hojas de modelo oficiales** de Mercury, Mars, Jupiter y Venus (todas medidas
   en alta resolución, 1800-2200 px de ancho) ya dan una pose de cuerpo entero lista
   para recortar por personaje, cada una con una personalidad de gesto distinta
   (Mercury animada, Mars desafiante, Jupiter enérgica, Venus coqueta).

## No encontré

- **Un vídeo de análisis/video-ensayo serio** (dirección, animación) con minuto
  verificado y descargable: todos los resultados de búsqueda son de YouTube,
  bloqueado en este contenedor. Búsquedas hechas: «Sailor Moon animation analysis
  video essay», «Sailor Moon Kunihiko Ikuhara director interview» (inglés). ⚠️ Queda
  pendiente si otra sesión tiene acceso a YouTube.
- **Vídeos oficiales de TikTok verificados uno por uno** (canal, vistas exactas): el
  contenedor no abre TikTok directamente; me quedé con las páginas de descubrimiento
  (`/discover/...`) y un resumen de WebSearch, que ya indican qué tono de edit
  funciona pero no dan un enlace de vídeo con vistas concretas. ⚠️.
- **AnimeThemes** (`.webm` de openings/endings): la API sigue caída (522) tanto en la
  recolección automática como al probarla yo de nuevo en esta tanda. ⚠️ Usé
  Dailymotion como alternativa para los openings/endings latinos.
- **Minuto exacto de los créditos en pantalla** de los openings/endings de la T2 a la
  T4 (solo tengo el infobox de la wiki, sin haber visto yo mismo el cartel de
  créditos de cada uno): no encontré una copia completa de esos episodios con los
  créditos legibles dentro del tiempo de esta tanda. ⚠️ (dato de una sola fuente, la
  wiki).

---

## Bitácora de búsqueda (vídeo)

- **Datos previos usados sin repetir la consulta**: `partes/datos-video.md` (AniList,
  Dailymotion, Internet Archive, MusicBrainz).
- AnimeThemes (`api.animethemes.moe`): repetí la prueba, sigue en **522** (caído) —
  igual que en `datos-video.md`.
- Wiki de Fandom (`sailormoon.fandom.com/api.php`, inglés): `list=search` para
  «opening theme», «Hikawa Shrine», «Crown Game Center», «Dark Kingdom», «Moon
  Kingdom», «Silver Millennium», «Takanori Arisawa»; `action=parse&prop=wikitext`
  sobre «Moonlight Densetsu», «Sailor Star Song», «Pretty Guardian Sailor Moon (anime
  series)», «Hikawa Shrine», «Game Center Crown», «Dark Kingdom», «Moon Kingdom»;
  `prop=imageinfo` sobre 6 imágenes de sitios.
- Internet Archive (`advancedsearch.php` + `metadata/<id>`): busqué «Sailor Moon»
  (mediatype movies, 40 resultados por descargas) y «Sailor Moon Cosmos»; comprobé
  metadatos de 8 ítems antes de elegir el episodio 1 (DiC dub), la película R (VHS
  fandub) y Cosmos Parte 2 (latino).
- Dailymotion API (`api.dailymotion.com/videos?search=`): «Sailor Moon opening 1992
  japones», «Sailor Moon opening latino», «Sailor Moon transformación latino»,
  «Sailor Moon ending latino», «Sailor Moon último capítulo final latino», «Sailor
  Moon Crystal trailer official» (español e inglés).
- `herramientas/episodio.py` (3 vídeos vistos de verdad, ficha en `partes/
  episodios.md`): episodio 1 completo (DiC dub, ✅), tramo 40:00-55:00 de Sailor Moon
  R: The Movie (VHS fandub, encontré la escena de Fiore en el min. 50:03, ✅) y tramo
  final 1:10:00-1:18:19 de Sailor Moon Cosmos Parte 2 (doblaje latino, ✅).
- `herramientas/fotogramas.py --fotograma`: 3 fotogramas grandes del episodio 1 (min.
  15:20, 15:45, 17:02).
- `herramientas/estilo.py --colores`: los 3 fotogramas anteriores. (No medí color en
  la copia VHS de la película R: la cinta tiene un desvío de croma real —verdes donde
  debería haber rosas— así que unos hex medidos ahí saldrían falsos; lo dejo dicho en
  vez de inventar un dato «medido».)
- Wiki de Fandom, imágenes de personajes y ataques: `prop=images` sobre las 5 páginas
  de personaje (Ami, Rei, Makoto, Minako, Luna) + `prop=imageinfo` sobre 13 archivos
  (hojas de modelo, formas civiles y gifs de ataque, mirados con Read uno por uno).
- WebSearch (5, inglés): escena «You are not alone» de Sailor Moon R: The Movie
  (confirmé que es de esa película, no de S: The Movie); tendencia de TikTok
  2025-2026; compositor Takanori Arisawa (dos fuentes más).
- Nada de programas de terceros para saltar el bloqueo de YouTube: solo Internet
  Archive, Dailymotion y la wiki, como pide el aviso.
- **Punto 14, tanda de ampliación**: encontré ya descargado y sin usar
  `/tmp/claude-0/trabajo/38-sailor-moon-video/ep39/hojas/` (428 fotogramas, uno por
  plano, de todo el episodio 39 del mismo DVD DiC, con `video.mp4` todavía sin
  borrar) de una pasada anterior — lo repasé hoja por hoja (9 hojas, `Read` de cada
  una) y es un episodio de temporada 1 con Kunzite como villano, con las 5 guerreras
  luchando y un flashback largo al Reino de la Luna. De ahí saqué con
  `fotogramas.py --fotograma` (sobre el `video.mp4` ya local, sin volver a
  descargar) 19 fotogramas nuevos en 1280 px, verificados yo mismo con `Read` (dos
  hojas de comprobación propias, `verificacion.jpg` y `verificacion2.jpg`, montadas
  con PIL) antes de describir la pose — dos de mis identificaciones iniciales
  (a partir de las miniaturas pequeñas) resultaron equivocadas y las corregí tras
  verlas en grande (una que creía de Mercury era Venus; otra que creía de Makoto
  civil no llegué a usarla por quedar ambigua). Añadidas 3 poses nuevas a Usagi, Ami,
  Rei, Makoto y Luna, y 4 a Minako — los 6 personajes llegan ya a 6 fotogramas
  citados con capítulo, minuto, enlace `&t=` y archivo propio.
- No confirmé el título en inglés del episodio 39 (la wiki de Fandom no lista título
  por número de doblaje DiC y `archive.org/metadata` no trae título por archivo);
  cito el contenido tal cual lo vi (Kunzite, flashback del Reino de la Luna) con
  «ep. 39 (DiC dub)», igual que ya se hacía con el episodio 1. ⚠️ (título sin
  confirmar, contenido sí visto directamente).
