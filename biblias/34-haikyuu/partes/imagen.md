# Investigador de imagen · Haikyuu!! (encargo 34) · repaso corto

Sólo los puntos **19** (texturas 2D) y **23** (colaboraciones y cruces): son
los únicos de mi rol que la biblia actual no cubre (`seccion.py 34-haikyuu
--indice` — mis otros puntos, 1/3/4/15/16, ya están en §3-§5 y §16-§17).
Parto de `partes/datos-imagen.md` (no repito esas consultas: portadas de
AniList, imágenes de los 5 personajes, Danbooru, Safebooru, Sketchfab,
Openverse). La biblia citaba 31 de 40 fuentes distintas: todo lo de abajo
son sitios **nuevos**, ninguno repetido de los 31 (comprobado con `grep -oE
'https?://[a-zA-Z0-9._-]+' biblia.md`).

## Hallazgos

### 19 · Texturas 2D

**Emblemas de instituto** (bajados de la wiki con `imageinfo` y medidos con
Pillow; son los mismos escudos que llevan en el pecho junto al número) ✅:

| Instituto | Escudo | Colores medidos | Tamaño | Fuente |
|---|---|---|---|---|
| **Karasuno** (烏野) | óvalo partido en dos triángulos de color, con los kanji 烏高 en blanco/negro y una corona de espigas plateadas alrededor; sobre fondo naranja de la camiseta | mitad verde-azulada `#518297`, mitad negro-azulado `#56555E`, espigas gris-plata `#9C6833` (sobre naranja de jersey `#865225`) | 104×152 | [Karasuno school crest s4-e6-1.png](https://static.wikia.nocookie.net/haikyuu/images/e/e4/Karasuno_school_crest_s4-e6-1.png) |
| **Nekoma** (音駒) | flor de cinco pétalos: pétalos rojos, anillo morado exterior, aro verde-azulado interior, y el kanji **駒** (koma, "pieza/potro") en dorado con un casco de samurái estilizado encima | pétalo rojo `#B23E41`, anillo morado `#8C5569`, aro interior `#CA915B`/verde apagado, kanji dorado `#B26F3C` | 264×263 | [Nekoma school crest s2-e1-1.png](https://static.wikia.nocookie.net/haikyuu/images/d/d0/Nekoma_school_crest_s2-e1-1.png) |
| **Shiratorizawa** (白鳥沢) | una **S** cursiva magenta dentro de una corona de alas blancas (cisne, «shiratori» = cisne blanco), fondo gris-azulado | fondo `#8FA6B1`, «S» `#995884` | 273×195 | [Shiratorizawa crest s4-e2-1.png](https://static.wikia.nocookie.net/haikyuu/images/3/32/Shiratorizawa_crest_s4-e2-1.png) |
| **Date Tech** (伊達工) | escudo romboidal militar: los kanji **伊達工** verticales en dorado sobre fondo oliva oscuro, con dos ramas de pino cruzadas abajo (viene de instituto técnico/industrial) | kanji `#9B8E72` sobre fondo `#F4F1EB` en la copia clara de la wiki (el original es oliva oscuro casi negro, se ve mejor en [Date Tech banner OVA 3-1.png](https://static.wikia.nocookie.net/haikyuu/images/e/e4/Date_Tech_banner_OVA_3-1.png) ⚠️ sin medir, resolución baja) | 172×183 | [Date Tech school crest OVA 3-1.png](https://static.wikia.nocookie.net/haikyuu/images/f/f5/Date_Tech_school_crest_OVA_3-1.png) |
| **Inarizaki** (稲荷崎) | estandarte con caligrafía a pincel «稲荷崎» y un zorro estilizado (稲荷 = altar-zorro Inari) | ⚠️ no medido (JPEG de imprenta, mucho ruido) | 1274×583 | [Inarizaki Banner Manga.png](https://static.wikia.nocookie.net/haikyuu/images/e/e7/Inarizaki_Banner_Manga.png) |

**Patrones de ropa** (más allá del uniforme de Karasuno, ya en §16 de la
biblia) ✅ vistos directamente:
- **Nekoma**: uniforme de invierno con blazer azul marino y corbata a
  **rayas diagonales rojo `#C34C4B` y azul marino**, en el arte oficial de
  merchandising «Ichiban Kuji» (ver §23) — [Nekoma colour uniform.jpg](https://static.wikia.nocookie.net/haikyuu/images/f/f0/Nekoma_colour_uniform.jpg), 736×520.
- **Shiratorizawa**: uniforme blanco con **pantalón/falda a cuadros
  (tartán) morado y burdeos**, corbata morada; el equipo de animadoras usa
  un **chevron rosa y morado** — [Shiratorizawa uniforms s3-e1-1.png](https://static.wikia.nocookie.net/haikyuu/images/7/73/Shiratorizawa_uniforms_s3-e1-1.png), 1355×756, y [Shiratorizawa uniform.jpg](https://static.wikia.nocookie.net/haikyuu/images/d/df/Shiratorizawa_uniform.jpg), 289×400.
- **Aoba Johsai**: fondo promocional con **motivo de hojas/enredadera turquesa
  `#A3CFC8`** repetido (usado en pósters de temporada) sobre blazer beige —
  [AobaJohsai(uniform).jpg](https://static.wikia.nocookie.net/haikyuu/images/3/39/AobaJohsai%28uniform%29.jpg), 412×581.
- **Fukurodani**: la camiseta de juego lleva **rayas diagonales doradas**
  sobre gris/blanco y el pie de búho **ics** en el pecho (visto en la
  figura oficial de Bokuto, §23) — no hay imagen de uniforme en la wiki en
  español/inglés (búsqueda `prop=images` sin resultado con «uniform» ni
  «jersey» en `Fukurōdani_Academy`) ⚠️.

**Cómo está «pintado» el manga/anime** (línea y sombreado; para replicar la
textura de trazo, no de tono) ⚠️ una fuente, tutorial de fan, no oficial:
- Grosor de línea **muy variable**: los contornos generales son finos,
  pero **la barbilla, el cuello y ciertas puntas del pelo llevan sombra
  sólida negra** (no degradado); el flequillo tiene luces como trazos
  rectos, gruesos arriba y finos hacia abajo. Descrito con capturas
  comparadas en [«ART TUTORIAL» de enzirin (DeviantArt)](https://www.deviantart.com/enzirin/art/ART-TUTORIAL-Haikyuu-Art-Style-Old-Animation-866245874).
  El color se aplica **plano** (flat colour), sin degradado interno: es
  coherente con lo que §5.2 de la biblia ya midió (colores sólidos, sin
  variación de tono dentro de una prenda).
- Ficha general de la técnica de screentone (熱transfer/rub-on) que usa el
  manga shonen en general, para quien no sepa qué es: [Screentone, Manga Wiki (Fandom)](https://manga.fandom.com/wiki/Screentone) ⚠️ genérico, no específico de Haikyuu (no encontré un making-of que
  describa qué trama concreta usa Furudate; ver «No encontré»).

**Texturas libres equivalentes, con licencia** (para reproducir lo de
arriba en Photoshop/Clip Studio):
- **Tramas de puntos (screentone) gratis**: 8 archivos PNG de 4500×4500 px,
  densidades de 10 a 80 puntos/pulgada a 300 dpi — [Manga with Stef, «Free Screen Tone Collection 1»](https://manga-with-stef.com/free-screen-tone-collection-1).
  Licencia: **libre para usar en tu obra, prohibido redistribuir los
  archivos desde otra web** (no dice si permite uso comercial de la obra
  final) ✅ comprobado en la página de descarga.
- **Pinceles de screentone** para Photoshop/Procreate/Clip Studio, pack
  gratuito (escribiendo «$0»): [GraphicsBunker, Comic Manga Screentone Brushes](https://www.graphicsbunker.com/brushes/free-comic-manga-screentone-brushes/)
  → enlaza a [ittaimanero (Gumroad), FREE Super Screentone Sample](https://ittaimanero.gumroad.com/l/FREESuperScreentoneSample).
  Licencia ⚠️: **no especifica** términos de uso comercial ni atribución en
  la página; comprobar antes de usarlo en algo que se publique.
- **Grano de papel** (para simular el papel del tomo o una cartela):
  [ambientcg, Paper004](https://ambientcg.com/get?file=Paper004_2K-JPG.zip)
  (marrón, tipo papel de embalaje/estraza), CC0, hasta 4K ✅. Distinto del
  Poly Haven que ya usa el equipo de vídeo en §5.3 (otra fuente, mismo
  tipo de banco).
- **Silueta de cuervo libre** (para una textura de fondo o marca de agua
  sutil con el motivo de Karasuno, no para copiar el logo): [Flaticon, iconos de «crow»](https://www.flaticon.com/free-icons/crow)
  (más de 1200), **gratis con atribución** (Flaticon Free License). ⚠️ el
  enlace directo a un icono concreto pide JavaScript/cuenta (la página del
  icono dio 403 por curl); no lo metí en `imagen.json` para no inventar una
  URL de imagen que no comprobé yo mismo — sólo queda la página de la
  colección, que sí abre.

### 23 · Colaboraciones y cruces

**Con el vóleibol real: SV.LEAGUE** (la liga profesional japonesa, antes
V.League) — la colaboración más «de verdad» de la serie con el deporte que
retrata:
- Para la apertura de la temporada 2024-25, **Furudate Haruichi dibujó una
  ilustración nueva** con Hinata y Kageyama junto a jugadores reales de los
  clubes campeones de las 3 temporadas previas, bajo el lema **"ATTACK THE
  TOP"**; se usó en la web oficial, redes, guías impresas y en el
  programa del partido de apertura (11-oct-2024) — anuncio oficial:
  [SV.LEAGUE, 10-oct-2024](https://www.svleague.jp/ja/topics/detail/23198)
  ⚠️ (una fuente oficial, sin imagen directa: la página sólo sirve una OG
  genérica, `img/news/default.jpg`).
- La colaboración **sigue cada temporada**: hay ilustraciones y merchandising
  (acrílicos, chapas, camisetas) en el *SV.LEAGUE CHAMPIONSHIP* 2024-25 y
  otra ronda anunciada para marzo de 2026 («春こそバレー祭»), con Furudate
  otra vez dibujando y comentando en broma que «Yū (Nishinoya) queda
  demasiado blanco» ✅ (dos fuentes): [SV.LEAGUE, mercancía del Championship](https://www.svleague.jp/ja/sv_men/topics/detail/23463)
  y [cuenta oficial de Haikyuu!! en X, anuncio 2026](https://x.com/haikyu_com/status/2002714408242524226).

**Cafés temáticos** (arte nuevo exclusivo, con las 6 escuelas juntas, algo
que no sale en el anime) ✅ tres fuentes:
- **«Haikyu!! ～勝利への道筋カフェ～» (Camino a la victoria)**, 5-sep a
  10-oct-2025, en BOX cafe&space (Tokio y Osaka) y BALLER:S Aeon Mall
  Shintoshi (Miyagi, prefectura natal de la serie). Ilustración nueva por
  parejas de **6 institutos** (Karasuno, Nekoma, Aoba Johsai, Fukurodani,
  Inarizaki, Shiratorizawa), cada una con el lema del equipo: Karasuno
  «飛べ» (Vuela), Nekoma «繋げ» (Conecta), Aoba Johsai «コートを制す»
  (Domina la cancha), Shiratorizawa «強者であれ» (Sé fuerte), Fukurodani
  «一球入魂» (Alma en cada balón), Date Tech «思い出なんかいらん» (No hacen
  falta los recuerdos). Posavasos de papel (6 diseños) al pedir bebida;
  postal de regalo con ¥2.200 en mercancía. Key visual con las 6 parejas,
  **1280×720**: [collabo-cafe.com, artículo del 27-ago-2025](https://collabo-cafe.com/events/collabo/haikyu-box-cafe-tokyo-osaka-miyagi2025/);
  confirmado en [Rakuten Books, «推し楽»](https://fan.books.rakuten.co.jp/articles/2941)
  y anunciado en la [web oficial de la serie](https://haikyu.jp/news/4097/).
  **Muy útil para la lámina**: enseña cómo empareja la serie a los rivales
  (ace + colocador de cada equipo) con una pose de brazos cruzados o con el
  balón, distinta de las poses de combate del anime.
- **Animate Café Ikebukuro**, 26-jul a 20-ago-2025, con ilustraciones
  «chibi» exclusivas del café y sorteo de entradas — [Animate Café, ficha del evento](https://www.animatecafe.jp/event/ac000636),
  confirmado en [collabo-cafe.com](https://collabo-cafe.com/events/collabo/haikyu-animate-cafe-stand-ikebukuro2025/).

**Figuras oficiales** (la pose sirve de referencia 3D real; producto
comercial, licencia **no libre**, sólo mirar) ✅:
- **Nendoroid Shōyō Hinata** (Good Smile Company, nº 4644): pose de
  voleibol con **3 caras intercambiables** (sonrisa, confianza, grito de
  emoción), balón, piezas de red y peana en forma de cancha; uniforme de
  Karasuno; ~100 mm, ABS/PVC articulado. Relanzada dic-2020 (original
  ene-2015), ¥4.074. 550×800: [Good Smile Company, ficha del producto](https://www.goodsmile.info/en/product/4644/Nendoroid+Shoyo+Hinata.html).
- **Ichiban Kuji «ハイキュー!! ～全国への道～»** (BANDAI SPIRITS, ago-2025):
  figuras de Bokuto (Fukurodani nº4, puño en alto, chaqueta al vuelo — pose
  lista para «celebrar», §14) y Akaashi (nº5, mirada seria, sujeta el
  balón); uniforme visto de cerca: camiseta blanca/gris con **rayas
  diagonales doradas**, «ics» y 梟谷 en el pecho. 1600×1600 y 1280×720:
  [1kuji.com, ficha «全国への道»](https://1kuji.com/products/haikyu30).
- **Serie Ichiban Kuji completa** (BANDAI SPIRITS, sitio oficial): al menos
  **6 lanzamientos** desde ago-2024: 10th anniversary (ago-2024 y
  reedición jun-2025), *La Batalla del Basurero 2* (mar-2025), *Camino a
  lo nacional* (ago-2025), *El retador más fuerte* (feb-2026), *El futuro
  de Karasuno* (ago-2026) — [1kuji.com, índice de Haikyuu!!](https://1kuji.com/characters/203).
  Cada lanzamiento trae **arte nuevo e ilustración exclusiva** del set de
  premios (no reciclan fotogramas del anime).

**Exposiciones de arte original** (原画展, eventos oficiales con dibujos e
storyboards reales, no fan-made) ✅ varias fuentes:
- Gira de **«劇場版ハイキュー!! ゴミ捨て場の決戦»展** (exposición de la
  película): Matsuya Ginza (27-dic-2024 a 22-ene-2025) → Hankyu Umeda →
  Daimaru Sapporo (15-oct a 3-nov-2025) → Niigata (8-nov a 1-dic-2025) —
  [Museo de manga/anime de Niigata](https://museum.nmam.jp/2025/10/07/haikyu_gomisuteba_ex/),
  [Hankyu Umeda](https://website.hankyu-dept.co.jp/honten/h/gallery_haikyu/),
  [collabo-cafe.com (Sapporo)](https://collabo-cafe.com/events/collabo/haikyu-movie-exhibition-sapporo-2025/).
- **«ハイキュー!!アニメ10周年記念展 全感覚EXHIBITION»** (10º aniversario del
  anime), con evento paralelo el 2-mar con los actores de doblaje japonés
  Ayumu Murase (Hinata) e Kaito Ishikawa (Kageyama) — sitio oficial:
  [haikyu-anime-10th-exhibition.com](https://haikyu-anime-10th-exhibition.com/),
  anunciado en [Dengeki Online](https://dengekionline.com/article/202408/14639).
- **«古舘春一 ハイキュー!!展 挑戦者たち»** (exposición del propio autor, con
  páginas originales), Mori Arts Center Gallery, 30-oct-2026 a
  11-ene-2027 — sitio oficial: [haikyu-challengers-ex.com](https://haikyu-challengers-ex.com/),
  primer key visual anunciado en [Animate Times](https://www.animatetimes.com/news/details.php?id=1776147080)
  ⚠️ (evento aún no ocurrido a fecha de hoy, 24-sep-2026: sólo hay key
  visual, no fotos del montaje).

**Cosplay bien hecho** (materiales y volumen reales, no genérico) ⚠️ fuentes
únicas cada una:
- **Construcción del jersey de Karasuno**: patrón base «raglan top»
  adaptado, cuello tipo *Peter Pan*/marinero de 5-6 cm hecho aparte y
  cosido, líneas blancas con cinta al biés de 12 mm planchada (no pintada
  ni termoadherida) — tutorial con fotos del proceso: [Danidere Cosplay (Tumblr), «Haikyuu jersey tips»](https://daniderecosplay.tumblr.com/post/123242897968/haikyuu-jersey-tips-links-for-patterns).
  La autora avisa que el cuello es la parte más difícil.
- **Galería internacional** (16 cosplayers, 8 países: Rusia, China, EE.UU.,
  Australia, Corea, Alemania, Taiwán, Tailandia), personajes Oikawa,
  Kageyama, Kuroo, Nishinoya, Hinata, Tsukishima, Yamaguchi, Yachi —
  [Animate Times, «世界の『ハイキュー!!』コスプレ»](https://www.animatetimes.com/news/details.php?id=1448472851)
  (28-nov-2015: es vieja, pero de una revista con criterio editorial, no
  una lista sin curar).

**Videojuegos: lo que la biblia ya tiene en §13** (J-Stars Victory VS,
Jumputi Heroes, Kotodaman, Puyopuyo!! Quest, Union Arena) es del rol de
texto/vídeo, no repito. Lo nuevo que encontré: **Puzzle & Dragons** tuvo
una colaboración del 21-mar al 7-abr-2025 ⚠️ (sólo confirmado por un
agregador, [hokope.com](https://hokope.com/archives/58023); no encontré
la nota oficial de GungHo ni de Weekly Shonen Jump con la fecha exacta —
lo dejo con aviso, no lo doy por ✅).

## Lo mejor para la lámina

1. La **key visual del café** (6 parejas escuela-a-escuela con su lema) es
   la mejor referencia para una lámina de **equipo/rivalidad**: pose de
   brazos cruzados o con el balón, sin repetir el combate del anime.
2. La figura **Ichiban Kuji de Bokuto** (puño en alto, chaqueta al vuelo)
   es una pose de **«celebrar»** ya resuelta en 3D con luz de estudio real.
3. Los **5 escudos de instituto** (Karasuno, Nekoma, Shiratorizawa, Date
   Tech, Inarizaki) con hex medidos sirven de **sello/marca de agua**
   por canal o por equipo, sin tocar el logo oficial de la serie.
4. El pack de **tramas de screentone gratis** (Manga with Stef) da la
   textura de punto para sombrear a mano un personaje recortado, sin que
   se note plano.
5. El cruce con la **SV.LEAGUE** es el gancho más fuerte para un canal de
   **deporte real** del servidor: la propia autora dibuja para la liga
   de verdad, no es un crossover de marca cualquiera.

## No encontré

- La **imagen exacta** del key visual de Furudate para la SV.LEAGUE 2024-25
  (la web sólo sirve una OG genérica; busqué en `svleague.jp` HTML y en
  Twitter/X oficial de la liga, sin la imagen en alta). ⚠️
- Licencia exacta del pack de pinceles de screentone de Gumroad
  (ittaimanero): la página no dice uso comercial sí/no. ⚠️
- Fuente oficial (no agregador) de la colaboración con **Puzzle &
  Dragons**: busqué «パズドラ ハイキュー コラボ 2025» y sólo aparecen
  blogs de terceros. ⚠️
- Imagen de **uniforme de juego** (jersey, no uniforme escolar) de
  Fukurodani en la wiki de Fandom: `prop=images` de `Fukurōdani_Academy`
  no devuelve ningún archivo con «uniform» ni «jersey» en el nombre; sólo
  la vi de cerca en la figura de Ichiban Kuji. ⚠️
- **Cosplay premiado en 2025-2026** con datos verificables: las búsquedas
  devolvían texto genérico de mercado (cifras no verificables tipo «mercado
  de $120 millones») que **no cito** por no poder confirmarlo en ninguna
  fuente real; me quedé con la galería curada de Animate Times (2015). ⚠️

## Bitácora de búsqueda

**Español**: «Haikyuu cosplay Karasuno jersey worldcosplay» (dio la galería
de Animate Times, no worldcosplay directo).
**Japonés**: `ハイキュー!! コラボ カフェ 2025`; `ハイキュー!! Vリーグ コラボ
公式パートナー`; `ハイキュー!! コラボ ソーシャルゲーム 2025`; `ハイキュー!!
一番くじ Ichiban Kuji バンダイ 私服`; `ハイキュー展 2025 原画展 開催`.
**Inglés**: «Haikyuu!! collaboration Japan Airlines JAL jet» (sin resultado:
no existe ese cruce, no lo confundo con otro anime); «Haikyuu Good Smile
Company Nendoroid figure official»; «Haikyuu manga screentone pattern
texture brush free»; «Haikyuu manga art style analysis linework shading
Furudate»; «flaticon free crow silhouette icon CC attribution».

**Por API/consulta directa** (sin buscador): `haikyuu.fandom.com/api.php`
(`prop=images` y `imageinfo` de Karasuno High, Nekoma High, Date Tech
High, Shiratorizawa Academy, Aoba Johsai High, Inarizaki High,
Fukurōdani Academy — 7 páginas de instituto, ninguna repetida de
`datos-imagen.md`); `ambientcg.com/api/v2` (texturas de papel);
`1kuji.com` (listado y fichas de producto); descarga y medición con
Pillow de 13 imágenes (escudos, uniformes, figuras, café).

**Fuentes nuevas de hoy** (ninguna de las 31 ya citadas en la biblia):
`manga-with-stef.com`, `graphicsbunker.com`, `gumroad.com` (ittaimanero),
`ambientcg.com`, `flaticon.com`, `svleague.jp`, `x.com` (haikyu_com),
`collabo-cafe.com`, `fan.books.rakuten.co.jp`, `haikyu.jp`,
`animatecafe.jp`, `goodsmile.info`, `1kuji.com`, `museum.nmam.jp`,
`website.hankyu-dept.co.jp`, `haikyu-anime-10th-exhibition.com`,
`dengekionline.com`, `haikyu-challengers-ex.com`, `daniderecosplay.tumblr.com`,
`manga.fandom.com`, `deviantart.com` (enzirin), `hokope.com` — **22
dominios nuevos**, de sobra para tapar el hueco de 9 que faltaba.

**Confirmado vs dudoso**: lo que lleva ✅ arriba está en dos fuentes o
medido directamente con Pillow sobre la imagen oficial; lo que lleva ⚠️
es de una sola fuente o sin poder comprobar la licencia/fecha exacta.

## Cumplimiento de mis puntos (19 y 23)

| # | Punto | Estado | Por qué |
|---|---|---|---|
| 19 | Texturas 2D: tramas, grano, pinceladas, patrones de ropa, emblemas/logos, con libres equivalentes y licencia | ✅ | 5 escudos de instituto medidos con Pillow, 4 patrones de ropa vistos y descritos, técnica de línea/sombreado (una fuente), 4 recursos libres con licencia comprobada (screentone, pinceles, papel, icono) |
| 23 | Colaboraciones y cruces: marcas, juegos, eventos, cafés, figuras oficiales, cosplay | ✅ | SV.LEAGUE (deporte real), 2 cafés temáticos con arte nuevo, 6 lanzamientos de Ichiban Kuji, Nendoroid oficial, 3 exposiciones de arte original, cosplay con materiales reales. Sólo el collab de Puzzle & Dragons quedó ⚠️ por falta de fuente oficial |
