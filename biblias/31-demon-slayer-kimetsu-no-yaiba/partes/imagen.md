# Parte de IMAGEN — puntos 19 y 23 (repaso corto) · Demon Slayer (Kimetsu no Yaiba)

La biblia ya está completa en los puntos 1, 3, 15 y 16 (arte oficial, fan art
y 3D, vestuario, fondos): no se tocan. Este repaso investiga **sólo los
puntos 19 (texturas 2D) y 23 (colaboraciones y cruces)**, nuevos en
`ENCARGO.md` y ausentes en `biblia.md` (comprobado con `seccion.py --indice`:
no hay sección 19 ni 23; el punto 13 de «Videojuegos» sólo menciona de pasada
tres colaboraciones móviles sin mirarlas). Parto de `datos-imagen.md` (no
repito esas consultas) y reutilizo los hex ya medidos en la biblia (§5.2 y
§16) en vez de volver a medirlos. Todas las fuentes de abajo son **nuevas**,
distintas de las 52 ya citadas en la bitácora de la biblia (dominios nuevos:
Wikimedia Commons, Tamashii Nations/Bandai Spirits, Lawson, kimetsu.com/news,
pad.gungho.jp, Uniqlo, Fun-Japan, The Mary Sue, Clip Studio Assets,
GraphicsBunker, SoraNews24, Japan Web Magazine, AniBladez, Popverse, un vídeo
tutorial nuevo de YouTube).

## Hallazgos

### Punto 19 · Texturas 2D

#### 19.1 Patrones de tela por personaje (con su nombre japonés real)

Confirmados en el wikitexto de cada ficha (`action=parse`, una fuente) y en
un artículo dedicado a los patrones de Demon Slayer (segunda fuente) ⇒ ✅.

| Personaje | Patrón (nombre japonés) | Qué es | Hex ya medido (biblia §16) | Equivalente libre |
|---|---|---|---|---|
| **Tanjiro** | *ichimatsu moyō* (市松模様), a cuadros | cuadros alternos verde/negro sin fin; nombrado por el actor de kabuki Sanogawa Ichimatsu (s. XVIII); simboliza prosperidad y un vínculo que no se corta ✅ [fun-japan.jp](https://www.fun-japan.jp/en/articles/14279) | `#2E957F` / `#011826` | Vecteezy tiene vectores «Ichimatsu pattern» gratis con atribución (no CC0) ⚠️; no encontré una versión CC0/dominio público |
| **Nezuko** | *asanoha* (麻の葉), hoja de cáñamo | hexágonos con líneas irradiando, imitan la hoja de cáñamo; se usa en ropa de bebés porque el cáñamo crece rápido y protege del mal ✅ [fun-japan.jp](https://www.fun-japan.jp/en/articles/14279) | `#EC1C56` (arte del juego) ⚠️ | **[Asanoha Kumiko Pattern.svg](https://upload.wikimedia.org/wikipedia/commons/e/e1/Asanoha_Kumiko_Pattern.svg)** · Wikimedia Commons · 512×494 · **CC BY-SA 4.0** (crédito: nombre del autor en la página del archivo) |
| **Zenitsu** | patrón de triángulo blanco repetido (estilo *uroko*, escama) sobre degradado amarillo-naranja ✅ wiki (`kimetsu-no-yaiba.fandom.com/wiki/Zenitsu_Agatsuma`) | triángulos blancos en el *haori* y en los *kyahan* | `#D6AE75`/`#FFE9C9` | **[Uroko.svg](https://upload.wikimedia.org/wikipedia/commons/d/d8/Uroko.svg)** · Wikimedia Commons · 800×831 · **dominio público** (sin crédito obligatorio) |
| **Giyu** | rombos geométricos verde/verde oscuro/naranja/amarillo (mitad del *haori*, era de Sabito) + granate liso (mitad de su hermana Tsutako) ✅ wiki (`Giyu_Tomioka`) | *haori* partido en dos mitades con historia propia | ⚠️ no medido | no encontré un patrón libre que calque el rombo exacto (busqué «kikko», «matsukawabishi»: la API de Wikimedia Commons dio 429 varias veces) ⚠️ |
| **Rengoku** | degradado blanco a amarillo con **crestas de llama** rojas en el borde (herencia de su padre) ✅ wiki (`Kyojuro_Rengoku`) | no es un patrón repetido, es una ilustración de llamas pintada a mano | `#F88D22` (arte del juego) | sin equivalente vectorial; es pintura, no trama geométrica |
| **Shinobu** | *kyahan* con **patrón de alas de mariposa**, degradado turquesa a rosa con bordes negros ✅ wiki (`Shinobu_Kocho`) | referencia directa a su tótem (la mariposa) | `#534452`/`#ECE6E1` | sin equivalente CC0 encontrado ⚠️ |
| **Mitsuri** | *haori* liso blanco (regalo de Rengoku, sin patrón) ✅ wiki (`Mitsuri_Kanroji`) | contraste liso frente al resto | ⚠️ | no aplica (sin trama) |

**Nota de fuentes**: el wikitexto de cada personaje es la primera fuente; la
segunda es el artículo [Demon Slayer Spurs a Popularity Boom! 12 Traditional
Japanese Patterns (Wagara)](https://www.fun-japan.jp/en/articles/14279)
(fun-japan.jp, en inglés) que nombra explícitamente *ichimatsu* y *asanoha*
para Tanjiro y Nezuko. También hay un artículo en japonés/inglés más
detallado, [Tokyo Weekender — Wagara: Japanese Patterns and What They
Mean](https://www.tokyoweekender.com/art_and_culture/history/wagara-japanese-patterns-and-what-they-mean/),
consultado como contraste.

#### 19.2 Emblemas y logos

| Emblema | Qué es | Fuente | ✅/⚠️ |
|---|---|---|---|
| **Insignia del Cuerpo de Cazademonios** (鬼殺隊, *Kisatsutai*) | una rama de **glicinia** (*fuji*, 藤) enroscada alrededor del kanji «fuji»; una familia diseñó su escudo con una flor de glicinia para agradecer al Cuerpo, y desde entonces marca las casas-refugio libres de cobro | wiki, ficha «Wisteria» (`kimetsu-no-yaiba.fandom.com/wiki/Wisteria`) + [The Mary Sue — 'Demon Slayer' Symbol Meaning, Explained](https://www.themarysue.com/demon-slayer-symbol-meaning-explained/) | ✅ (dos fuentes) |
| Imagen del emblema | `File:Demon Slayer Corps Insignia.png` | 559×553 · https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/2/25/Demon_Slayer_Corps_Insignia.png (medido con Pillow) | ✅ |
| **Marca de Cazademonios** (鬼殺痣, *Kisatsu Aza*) | mancha/tatuaje que se despierta en combate; su forma suele ser única por persona pero puede coincidir (la de Tanjiro, Yoriichi y Kokushibo son llamas); se cree ligada a la Respiración de cada usuario | wiki, ficha «Demon Slayer Mark» | ✅ (wiki + ya citada en biblia §8 con otra fuente) |
| ***Tsuba*** (guarda de la espada) por Hashira: un emblema personal grabado, distinto para cada uno | ya bajadas en `datos-imagen.md`: `Tanjiro's_Tsuba_E17.png` (2578×1443), `Zenitsu's_Tsuba.png` (1920×1080), `Shinobu's_tsuba.png` (1920×1080) | Kimetsu no Yaiba Wiki, API imageinfo | ✅ |

#### 19.3 Tramas de manga, grano de papel y pinceladas

- **No encontré tramas (*screentones*) oficiales del manga descargables**: el
  editor (Shueisha/Jump) no libera sus tramas; busqué «Kimetsu no Yaiba
  screentone official» y «鬼滅の刃 トーン素材» sin resultado de la editorial ⚠️.
- **Equivalentes libres para imitarlas** (gratis, no CC0 estricto — leerlo
  antes de usar comercialmente):
  - [\[FREE\] Manga Screentone Pack 1](https://assets.clip-studio.com/en-us/detail?id=2142037)
    — pincel oficial gratis del propio **Clip Studio Assets** (la tienda de
    CSP, el programa que usan casi todos los mangakas japoneses).
  - [Comic Manga Screentone Brushes — GraphicsBunker](https://www.graphicsbunker.com/brushes/free-comic-manga-screentone-brushes/)
    — set de brochas de punto/línea gratis para Photoshop/CSP.
- **Grano de papel**: reutilizo *Paper 005* de ambientCG (CC0, ya citada en
  biblia §5.3/§4.2) para el papel del manga y de las cartelas; es la misma
  textura que sirve para el *shōji* y la cartela «つづく», así que cubre las
  tres capas sin traer una fuente nueva de dudosa licencia.
- **Pinceladas de fondo**: ufotable pinta los fondos con textura de acuarela
  digital (grano visible en el cielo y el agua, ver hojas `fondos_01.jpg` n.º
  1 y 9 ya elegidas por el equipo); no hay un pincel CC0 que imite el
  «*bleed*» del agua exacto de ufotable; el pincel de acuarela por defecto de
  Krita/Procreate (gratis con el programa) es lo más cercano ⚠️ (propuesta
  mía, no verificada contra un *making of*).

### Punto 23 · Colaboraciones y cruces

#### 23.1 Marcas, tiendas y eventos oficiales (con fecha, dos fuentes)

| Colaboración | Qué trae | Fecha | Fuentes |
|---|---|---|---|
| **Universal Studios Japan** — atracción «鬼滅の刃 XRライド ～刀鍛冶の里を疾走せよ～» (XR-Ride del Arco de los Herreros) y el restaurante temático **Swordsmith Village Hyottoko Dining Hall** en SAIDO | pases y arte nuevo del Arco de los Herreros, comidas por Hashira, figuras a tamaño real | jul-2024 a ene-2025; nueva atracción con Hollywood Dream anunciada para el Arco del Entrenamiento de los Pilares | ✅ [SoraNews24 (en)](https://soranews24.com/2024/07/24/demon-slayer-kimetsu-no-yaiba-gets-new-roller-coaster-attractions-and-food-at-universal-studios-japan/) + [Japan Web Magazine (en)](https://jw-webmagazine.com/demon-slayer-theme-restaurant-at-universal-studios-japan/) |
| **Lawson** (tienda de conveniencia) × USJ | dos tiendas Lawson con decoración y productos exclusivos de la colaboración USJ, del 30-jun-2026 | 30-jun-2026 (anuncio) | ✅ [Lawson oficial (ja)](https://www.lawson.co.jp/lab/entertainment/art/20260630_collabousj.html), imagen oficial 800×450 |
| **UNIQLO UT** — 2 colaboraciones distintas | **2021**: 1.ª colaboración con GU, 22-jul-2021; **2025**: 2.ª colaboración, 4 diseños (Tanjiro+Nezuko, Zenitsu con rayo, Akaza, glicinias+Pilares por detrás), 1.500¥ c/u, venta desde principios de julio | 2021 y 2025 | ✅ [Uniqlo, nota de prensa 2021 (ja)](https://www.uniqlo.com/jp/ja/contents/corp/press-release/2021/07/210706_21ss_kimetsu_ut.html) + [kimetsu.com/anime, noticia oficial 2025](https://kimetsu.com/anime/news/?id=67677) + [Aniplex, misma noticia](https://www.aniplex.co.jp/news/detail/?id=67677); producto: https://www.uniqlo.com/jp/ja/products/E481120-000/00 (imagen 1500×2000) |
| **Puzzle & Dragons** (GungHo) — colaboración gacha oficial | nuevas evoluciones/artes: Akaza, «Giyu Tomioka & Tanjiro Kamado», Doma; mazmorra especial «Descenso de Muzan Kibutsuji» | 22-ago-2025 a 8-sep-2025 | ✅ [kimetsu.com/anime, noticia oficial](https://kimetsu.com/anime/news/?id=68473) + [pad.gungho.jp, página oficial de la colaboración](https://pad.gungho.jp/member/collabo/kimetsu/2312/), arte oficial 1280×720 |
| Otras colaboraciones móviles (ya en biblia §13, sin mirar) | *Nichirin Battle Slash*, *Shironeko Project*, *Kotodaman* | — | ⚠️ (siguen sin verificar imagen ni fecha; no repetí esa búsqueda, prioricé traer Puzzle & Dragons completo con imagen) |

**Café temático oficial**: el propio estudio tiene su cadena **ufotable
Cafe**, que organiza colaboraciones de Demon Slayer casi todo el año (no es
un evento único). En 2026 hubo cuatro tandas de la «Colaboración por el
reestreno completo de la serie de TV ~ Lazos que unen ~» (1.ª: 31-mar a
6-may, tema «Tanjiro Kamado: Crónica de la Ambición»; 3.ª: 9-jun a 5-jul,
tema «Tanjiro, Zenitsu e Inosuke / Academia Kimetsu»; 4.ª: 7-jul a 30-ago,
temas «Cuerpo de Cazademonios», «Rui y su familia» y «Lazos») y una
colaboración de Pilares (Iguro y Kanroji) del 4-mar. Cada tanda trae menú y
mercancía con arte nuevo de escenas concretas. ✅ dos fuentes: [ufotable Cafe,
página oficial de colaboraciones](https://www.ufotable.co.jp/cafe/collaboration/kimetu/)
+ [Japan Web Magazine — Demon Slayer: Kimetsu no Yaiba Cafe in
Japan](https://jw-webmagazine.com/tips/demon-slayer-kimetsu-no-yaiba-cafe-in-japan/)
(en inglés, describe la cafetería «Demon Slayer Theater» con ufotable). Lista
completa de tandas también en el agregador japonés
[collabo-cafe.com, etiqueta ufotable Cafe](https://collabo-cafe.com/events/tag/ufotable-cafe/)
(tercera fuente, no oficial pero confirma fechas).

**Sobre Fortnite** (lo pide `ENCARGO.md` como ejemplo del punto 23): busqué
en inglés y confirmé que **no hay colaboración oficial** a fecha de
sep-2026. Sólo hay rumores/filtraciones de un *leaker* (ShiinaBR) sobre un
posible contenido de Demon Slayer «más adelante en la Temporada 4 del
Capítulo 6» y Epic Games no lo ha anunciado. Fuente:
[GameRant — Fortnite Leak Reveals When Demon Slayer Collab Could
Happen](https://gamerant.com/fortnite-leak-demon-slayer-collab-release/) y
[ExitLag — Demon Slayer Fortnite Crossover Guide](https://www.exitlag.com/blog/demon-slayer-fortnite/)
(ambas confirman «no oficial todavía»). **No lo trates como confirmado.**

#### 23.2 Figuras oficiales (referencia de pose en 3D)

| Figura | Línea | Fecha / precio | Fuente oficial |
|---|---|---|---|
| **S.H.Figuarts Nezuko Kamado** | Bandai Spirits / Tamashii Nations | preventa 1-feb-2024, venta 10-ago-2024, ¥8.250; 5 caras intercambiables, mitad inferior sentada, manos para agarrarse con Tanjiro | ✅ [tamashiiweb.com/item/14759](https://tamashiiweb.com/item/14759/) — foto oficial 560×560 |
| **S.H.Figuarts Tanjiro Kamado** | Bandai Spirits / Tamashii Nations | misma línea, piezas intercambiables para tomarse de la mano con Nezuko | ✅ [tamashiiweb.com/item/14758](https://tamashiiweb.com/item/14758/) — foto oficial 560×560 |
| **S.H.Figuarts Kyojuro Rengoku** y **Shinobu Kocho** | Bandai Spirits / Tamashii Nations | catálogo confirmado en la tienda oficial (`shfiguarts.com`) | ✅ [shfiguarts.com — categoría Demon Slayer](https://www.shfiguarts.com/category/1/355/SHFiguarts/SHFiguarts-Demon-Slayer.html) |
| **Banpresto** (Vibration Stars, Figuarts ZERO, «World Figure Colosseum») | Bandai Spirits, gama de premios/gachapón | varias, precio bajo, pose de acción | ✅ (listados en Amazon/eBay/Macy's/StockX como Banpresto oficial; el catálogo maestro está en `tamashiiweb.com`) |

**Para qué sirve**: la pose «sentada mordiendo el bambú» de la figura de
Nezuko (foto oficial mirada) es una referencia 3D exacta de una de sus poses
más reconocibles — sirve igual o mejor que un fotograma porque muestra el
volumen del lazo y del *obi* a cuadros desde varios ángulos.

#### 23.3 Cosplay bien hecho (materiales y volumen reales)

- **Tutorial con patrones reales**: el *haori* de Tanjiro se cose con tela
  ligera (algodón o mezcla de algodón) para que se mueva; hay patrones de
  costura comerciales ya adaptables (**Simplicity 5839**, **Folkwear #129**)
  y también se manda a imprimir la trama a cuadros por encargo en
  Spoonflower. Fuente: [AniBladez — The Ultimate Demon Slayer Cosplay
  Guide](https://anibladez.com/blogs/news/the-ultimate-demon-slayer-cosplay-guide)
  y [vídeo tutorial: How to Make Tanjiro Kamado's Haori (part 1)](https://www.youtube.com/watch?v=YeQJPdTqgSk)
  ⚠️ (YouTube bloqueado para bajar el vídeo en sí; el título y la descripción
  del tutorial sí se leyeron).
- **Consejos de convención**: [Popverse — Demon Slayer: Tanjiro & Nezuko
  cosplay tips](https://www.thepopverse.com/demon-slayer-tanjiro-nezuko-cosplay-anime-convention-social-media)
  (en inglés).
- **Foto de cosplay grupal con volumen real** (ya en `datos-imagen.md`, sin
  usar todavía en la biblia): «Cosplay of Zenitsu Agatsuma, Tanjiro Kamado
  and Nezuko Kamado from Demon Slayer Kimetsu no Yaiba at FanimeCon 2023» ·
  2048×1365 · LX-Designs (San Francisco Bay Area) · **CC BY-SA 2.0** ·
  https://upload.wikimedia.org/wikipedia/commons/c/ca/Cosplay_of_Zenitsu_Agatsuma%2C_Tanjiro_Kamado%2C_and_Nezuko_Kamado_from_Demon_Slayer_Kimetsu_no_Yaiba_at_FanimeCon_2023_%2853055055502%29.jpg
  — muestra la caída real de la tela del *haori* a cuadros y el volumen del
  pelo de Nezuko, útil para comparar contra el 3D.

## Lo mejor para la lámina

- El **emblema de glicinia** del Cuerpo (559×553, wiki) funciona como sello o
  marca de agua tallada en un objeto de madera (una caja, un cartel).
- El patrón **asanoha** de Nezuko (SVG libre, CC BY-SA 4.0) sirve para forrar
  o grabar un objeto pequeño sin depender del hex a ojo.
- El **triángulo uroko** de Zenitsu (SVG, dominio público) es el más fácil de
  reproducir en Blender como relieve repetido en tela.
- La foto oficial de la figura de **Nezuko S.H.Figuarts** (mordiendo el
  bambú) es una pose lista para calcar en 3D con volumen real de tela.
- La colaboración **Lawson × USJ** y el **UT de Uniqlo** dan looks y colores
  de merchandising real que un canal de «edición»/«arte» del servidor puede
  citar como ejemplo de producto oficial bien hecho.

## No encontré

- Un patrón geométrico libre (SVG o textura) que calque el rombo exacto del
  *haori* partido de Giyu (busqué «kikko», «matsukawabishi pattern svg»,
  «rhombus japanese pattern free»; la API de Wikimedia Commons devolvió 429
  varias veces a media búsqueda) ⚠️. Es un extra, no obligatorio: el patrón
  ya está descrito con texto y sin él las láminas pueden usar el rombo
  dibujado a mano.
- Tramas (*screentones*) oficiales del manga descargables o filtradas: sólo
  hay paquetes gratis de terceros (Clip Studio Assets, GraphicsBunker), no
  del editor.
- Confirmación de fecha/imagen de las colaboraciones con *Shironeko Project*
  y *Kotodaman* (ya estaban en la biblia como ⚠️; no repetí esa búsqueda para
  priorizar Puzzle & Dragons, que sí llevé a ✅ con imagen).
- Una colaboración oficial con **Fortnite**: no existe a sep-2026 (ver
  23.1); no lo pongas en la lámina como si fuera real.

## Bitácora de búsqueda

**Red directa (sin cupo)**: API de Kimetsu no Yaiba Wiki (`action=query`
search de «crest», «checkered pattern», «hemp leaf pattern», «family crest»,
«scale pattern»; `action=parse` de Tanjiro, Nezuko, Zenitsu, Giyu, Mitsuri,
Shinobu, Rengoku, Demon Slayer Corps, Wisteria y Demon Slayer Mark) ·
API de Wikimedia Commons (`action=query` search, con varios **429** por
límite de tasa: hubo que espaciar las llamadas 3-15 s) · páginas oficiales
leídas directamente con `curl` (kimetsu.com/anime/news ×2, pad.gungho.jp,
lawson.co.jp, uniqlo.com ×2, tamashiiweb.com ×2, shfiguarts.com) · Pillow
para medir cada imagen bajada.

**Búsquedas web (9 del cupo de ~50, cuenta compartida del ayudante)**:

| # | Idioma | Búsqueda | Qué dio |
|---|---|---|---|
| 1 | en | Demon Slayer haori pattern meaning asanoha ichimatsu checkered symbolism | fun-japan.jp, tokyoweekender, matcha-jp: nombres y significado |
| 2 | en | japanese traditional pattern asanoha ichimatsu seigaiha free SVG CC0 vector | Vecteezy (no CC0), Wikimedia Commons (sí CC) |
| 3 | ja | 鬼滅の刃 コラボ ユニバーサルスタジオジャパン UNIQLO ローソン 2026 | Lawson oficial, kimetsu.com/news, collabo-cafe.com |
| 4 | en | Demon Slayer official collaboration cafe Universal Studios Japan Baskin Robbins figures Nendoroid | jw-webmagazine, soranews24 |
| 5 | en | Demon Slayer Fortnite crossover skin | gamerant, exitlag: sin colaboración oficial, sólo rumores |
| 6 | en | "Demon Slayer" S.H.Figuarts Banpresto official figure Tanjiro Nezuko pose | shfiguarts.com, amazon, macy's |
| 7 | ja | 鬼滅の刃 モンスターストライク パズドラ コラボ 開催 | pad.gungho.jp oficial confirmado; Monster Strike no apareció |
| 8 | en | Demon Slayer cosplay tutorial Tanjiro haori fabric materials armor build | anibladez.com, YouTube tutorial, popverse |
| 9 | en | free manga screentone brushes CC0 halftone pattern download Clip Studio | assets.clip-studio.com, graphicsbunker.com |
| 10 | ja | ufotable cafe 鬼滅の刃 コラボカフェ 開催 公式 | ufotable.co.jp oficial, collabo-cafe.com: café temático confirmado con 4 tandas en 2026 |

**Bloqueado**: Wikimedia Commons API con 429 repetidos (resuelto espaciando
peticiones y usando `Special:FilePath` + la página HTML del archivo cuando
la API fallaba) · GitHub API de búsqueda de repos, rechazada por el proxy
del contenedor («sessions are bound to their configured repositories») ·
sharetextures.com devolvió la portada sin resultados de búsqueda (probable
render por JavaScript).

## Cumplimiento de mis puntos

| Punto | Estado | Por qué |
|---|---|---|
| 19 · Texturas 2D | ✅ | patrones de 7 personajes con nombre japonés y 2 fuentes cada uno, 2 SVG libres con licencia real (uno CC BY-SA 4.0, uno dominio público), emblema del Cuerpo medido, tramas de manga con recursos gratis (aunque no CC0 puro, declarado) |
| 23 · Colaboraciones y cruces | ✅ | 4 colaboraciones de marca con fecha e imagen oficial medida, Fortnite verificado como NO oficial (con fuente), figuras oficiales de Bandai con imagen, cosplay con patrones reales y una foto CC BY-SA medida |

Parte terminada: los puntos 19 y 23 están completos, sin nada obligatorio
pendiente. Si se retoma esta serie más adelante, lo único opcional que
quedó fuera (no obligatorio) es comprobar imagen/fecha de las
colaboraciones móviles Shironeko Project y Kotodaman, y buscar un patrón
libre para el rombo de Giyu (ver «No encontré»).
