# Imagen · Death Note (puntos 1, 3, 15, 16, 19, 23 de ENCARGO.md)

Investigador de imagen, modo **repaso**. Parte de `partes/datos-imagen.md` (ya
recolectado) y de la biblia anterior (hecha con la red cerrada: casi todo
llevaba ⚠️ porque no se pudo abrir Fandom, Sketchfab ni pixiv). Con la red
abierta se confirma, se mide y se añaden **hojas de contacto** (antes 0) y el
punto 23 (colaboraciones), que faltaba entero.

## 1 · Arte oficial, en cantidad y variado

- **Hojas de contacto**: `investigar_serie.py` bajó **1181 imágenes** de 6
  páginas de `deathnote.fandom.com` (Light, L, Ryuk, Misa, Near, Mello) y
  montó **12 hojas** numeradas · fuente: `herramientas/referencias/death-note/`
  (`indice.json` con ancho, alto y URL de cada una) · ✅ (herramienta +
  `deathnote.fandom.com`, comprobado abriendo las hojas).
- **hojas/arte_oficial_01.jpg** (nº 1-96 de la hoja 1, ordenadas de más a
  menos grande): key visuals del manga a color de Obata — nº7 «Death Note
  Vol.1-ish» grupo, nº8 «Saint Valentine's Day» (Light y Misa, pareja, la
  misma serie que uso en vestuario), nº9 «LightMisa(art-book).jpg» (grupo
  completo, 3326×5000), nº13 «LNearMello(art-book).jpg» (Near y Mello juntos,
  3114×5000), nº15 «LMisaLight.jpg», nº17 grupo con Ryuk y Rem, nº37-42
  wallpapers oficiales del juego **Othellonia × Death Note** (Light, L, Misa,
  Near, Mello, uno por personaje, 2208×2208) ✅.
- **hojas/colaboraciones_02.jpg** (nº 241-288, hoja 6): nº244 «Universal Jump
  Summer.jpg» (evento de USJ, ver §23), nº259-260 arte de **Jump Force**
  (nº260 es Mello, mal nombrado «Jumpforcelight»), nº253 Light con Ryuk en
  CG del juego, nº261 fondo del piso de Wammy's, nº267 Ryuk manga a color
  con Misa muerta en brazos (escena del final).
- **hojas/colaboraciones_03.jpg** (nº 529-540, hoja 12): nº530 «デスノートと
  夢のコラボ» (colab con un juego móvil), nº531 y nº538-539 colab con **LINE
  Bubble 2** (ver §23), nº536 «Death Note the Escape» (sala de escape real).
- **Portada y banner oficiales** (AniList): 
  `https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx1535-kUgkcrfOrkUM.jpg`
  y `https://s4.anilist.co/file/anilistcdn/media/anime/banner/1535.jpg` ✅
  (AniList; datos-imagen.md).
- **Color pages oficiales del manga** (Obata, para tomo/Jump), confirmadas al
  abrirlas: «299276.jpg» = Light de perfil, camisa del instituto, 2001×4705
  ✅; «295978.jpg» = Misa «Saint Valentine's Day», 3466×5000 ✅; «DN 013.jpg»
  = Near, mano en la cara, 3039×5000 ✅; «Lfull.jpg» = L sentado comiendo
  chocolate, 1352×2200 ✅ — todas en `deathnote.fandom.com`, bajadas con
  `Referer: https://www.fandom.com/` (datos-imagen.md tiene las URL).
- **El artbook «blanc et noir»** (Obata, Shūeisha, 31-may-2006): B4, 168 pp,
  +120 ilustraciones de Death Note y Hikaru no Go, con *making of* a color
  ✅ ([HLJ](https://www.hlj.co.jp/product/SYU82146),
  [Books.or.jp](https://www.books.or.jp/book-details/9784087821468)). Es la
  referencia de pose y color más completa que existe; no está escaneado
  libre en ningún sitio que encontrara.
- **Death Note: Killer Within** (2024, Bandai Namco/Warner): arte clave con
  Kira y L ✅ ([Bandai Namco](https://www.bandainamcoent.com/games/death-note-killer-within),
  [Steam](https://store.steampowered.com/app/2213190/DEATH_NOTE_Killer_Within/)).
- **El musical** (HoriPro): posters de las giras taiwanesa 2017 (6000×4000,
  nº1-5 de la hoja 1) y coreana 2015/2017 (hoja 2) ✅ — arte oficial pero de
  actores reales, no del diseño de Obata: úsalo para poses, no para color.

---

## 15 · Vestuario

Colores **medidos con Pillow** (mediana de una zona de la prenda, código en
`sample.py`, guardado en la carpeta de trabajo) sobre imágenes oficiales
confirmadas en §1, no estimados de memoria como en la biblia vieja. Ojo:
la mediana toma sombra y luz juntas, así que el hex es el tono medio real
de la tinta, no el más saturado del dibujo.

| Personaje | Prenda | Hex medido | De qué imagen |
|---|---|---|---|
| Light Yagami | Camisa blanca del instituto | `#F9F5F4` | «299276.jpg», color page de Obata (perfil, de espaldas) ✅ |
| Light Yagami | Pelo | `#85542D` | misma imagen ✅ |
| Light Yagami | Corbata roja (uniforme, no aparece en esta pieza) | `#8E1B1B` | guía de cosplay, no medida en imagen oficial ⚠️ ([Carbon Costume](https://carboncostume.com/title/death-note/)) |
| L | Camiseta de manga larga | `#E6D19F` (zona de sombra; los blancos puros llegan a `#F5F0E0`) | «Lfull.jpg», color page de Obata ✅ |
| L | Vaquero ancho | `#596D76` | misma imagen, zona de sombra del pliegue ✅ |
| Ryuk | Piel | `#84889D` | «Ryuk DN Coloured.png» (wiki, color oficial) ✅ |
| Misa Amane | Vestido rojo (Saint Valentine's Day) | `#A74E44` | «295978.jpg», color page de Obata, mediana de la tela (no del brillo) ✅ |
| Misa Amane | Gargantilla y guantes de cuero negro | negro puro, no medido con precisión de píxel (mezcla con el pelo) | misma imagen ⚠️ |
| Misa Amane | Cruz del pendiente | rojo granate oscuro | misma imagen, visual ⚠️ |
| Near | Pijama (camisa) | `#F7F2EE` | «DN 013.jpg», color page de Obata ✅ |
| Near | Pantalón del pijama: **blanco en el manga, celeste en el anime** | manga `#F7F2EE` ✅; anime ⚠️ (de memoria, sin fotograma propio) | ver arriba |
| Mello | Gabardina de cuero negro | `#0E0D12` | wallpaper oficial «Othellonia × Death Note» (juego con licencia de Shūeisha/VAP/Madhouse, crédito en la propia imagen) ✅ |
| Mello | Pelo rubio ceniza | `#BB9786` | misma imagen ✅ |

**Lo que todos reconocen** (confirmado también en las hojas de contacto):
Light con **camisa blanca y corbata roja**; L **de blanco, en cuclillas**;
Misa **de negro/rojo gótico con la cruz**; Near **de pijama blanco jugando
con el pelo**; Mello **de cuero negro con el rosario y el chocolate**; Ryuk
**con las plumas negras y la manzana**. Coincide con el texto «Appearance»
de cada página de la wiki (`datos-imagen.md`) ✅.

---

## 16 · Ciudades, paisajes y fondos de pantalla

Los sitios de la serie y su luz están en el punto 4 (lo investiga vídeo);
aquí van sólo los **fondos de pantalla** en alta, oficiales y de fans.

### Oficiales (Zerochan, créditos «by MADHOUSE», tamaño comprobado con curl)

| Qué | Tamaño real | Enlace |
|---|---|---|
| Key visual (grupo) | 1920×1080 | [zerochan.net/4253569](https://www.zerochan.net/4253569) |
| Key visual (grupo) | 1920×1080 | [zerochan.net/4377401](https://www.zerochan.net/4377401) |
| Key visual (grupo) | 1920×1080 | [zerochan.net/4382652](https://www.zerochan.net/4382652) |
| Near, key visual | 1920×1080 | [zerochan.net/4377547](https://www.zerochan.net/4377547) |

✅ los 4: tamaño leído del `<meta property="og:image">` de la propia página,
25-sep-2026 (Zerochan aloja escaneos oficiales de Madhouse, no fan art, lo
dice el crédito «by MADHOUSE» junto a cada imagen).

### De fans, sólo aptos (Wallhaven, con ♥ real de la API — `datos-imagen.md`)

| Tamaño | ♥ | Qué sale | Enlace | Autor/origen |
|---|---|---|---|---|
| 4096×2304 | 136 | Misa Amane, cross | [wallhaven-6d5mll](https://w.wallhaven.cc/full/6d/wallhaven-6d5mll.jpg) | [jeonmin8974](https://twitter.com/jeonmin8974/status/1646235438745788416) |
| 2896×4494 | 124 | Misa Amane, Tokkyu (artista) | [wallhaven-g79mkd](https://w.wallhaven.cc/full/g7/wallhaven-g79mkd.jpg) | sin origen listado |
| 1920×2776 | 106 | Misa y Rem, retrato | [wallhaven-ogdg9p](https://w.wallhaven.cc/full/og/wallhaven-ogdg9p.jpg) | [En_D_D](https://x.com/En_D_D/status/1926586543260500217) |
| 2076×4096 | 94 | Misa y Rem, ilustración | [wallhaven-xe8pwd](https://w.wallhaven.cc/full/xe/wallhaven-xe8pwd.png) | [ZabiMasurao](https://x.com/ZabiMasurao/status/1956294807568921021) |
| 1920×1080 | 77 | Light, Ryuk, manzanas | [wallhaven-0wgqyx](https://w.wallhaven.cc/full/0w/wallhaven-0wgqyx.jpg) | sin origen listado |
| 2560×1440 | 166 | Ryuk, en un tren (crossover Chainsaw Man) | [wallhaven-p9qvge](https://w.wallhaven.cc/full/p9/wallhaven-p9qvge.png) | [gorzius](https://www.pixiv.net/en/users/20708445) |

⚠️ **«4kwallpapers.com/…ryuk-death-note-ai-14431.html»** (de la biblia
vieja): la propia página dice que está **hecha con Midjourney**. **No
usarla ni de referencia**: no es arte de la serie.
Wallpaper Abyss (`wall.alphacoders.com`) también tiene 480+ pero no dejó
leer el tamaño exacto por API sin cuenta ⚠️: usa Wallhaven o Zerochan, que sí
lo dan.

### Sitios y su luz (resumen; el detalle es de §4 de vídeo)

Noche azul con lámpara cálida (cuarto de Light) · gris sin sol (mundo
shinigami) · lluvia gris azul (azotea) · tiras de sol entre polvo (almacén
final) — confirmado también en las hojas de contacto (nº245 en
`colaboraciones_02.jpg` es una página de manga con el eyecatch nocturno).

---

## 19 · Texturas 2D (tramas, papel, pinceladas, patrones, con licencia)

### Tramas de manga (screentone) y pinceles de entintado, libres

| Recurso | Qué trae | Licencia | Enlace |
|---|---|---|---|
| [FREE] Manga Screentone Pack 1 | Set de tramas de puntos y líneas para Clip Studio Paint | Gratis en Clip Studio Assets (cuenta CSP, uso libre) ✅ | [assets.clip-studio.com/…2142037](https://assets.clip-studio.com/en-us/detail?id=2142037) |
| Essential Screentone Brushes | Tramas combinables para crear patrones nuevos, CSP | Gratis, Clip Studio Assets ✅ | [assets.clip-studio.com/…2087033](https://assets.clip-studio.com/en-us/detail?id=2087033) |
| Free Screen Tone Collection 1 | Tramas en PNG de 4500×4500 px (a 300 dpi cubren A4/B4/Carta), sirven en Krita, Procreate o Photoshop | Gratis, sitio de la autora (Manga with Stef) ⚠️ (leer su nota de uso antes de redistribuir) | [manga-with-stef.com](https://manga-with-stef.com/free-screen-tone-collection-1) |
| 65+ Halftone Brushes | Pinceles de medio tono para Photoshop y otros | Gratis, uso personal y comercial con atribución ✅ | [photoshopsupply.com](https://www.photoshopsupply.com/patterns-textures/halftone-texture) |
| 1000+ Manga Screentone Compilation | Compilación enorme de tramas (puntos, líneas, degradados) | DeviantArt, licencia del autor: revisar antes de usar comercialmente ⚠️ | [deviantart.com/theawesomeaki-kun](https://www.deviantart.com/theawesomeaki-kun/art/1000-Manga-Screentone-Compilation-681249872) |

✅/⚠️ confirmados abriendo cada página (25-sep-2026, red abierta). Con esto
se puede recrear el sombreado plano con trama del manga de Death Note
(Obata usa poca trama y mucho negro sólido; las tramas sirven sobre todo
para los fondos grises del mundo shinigami).

### Texturas reales equivalentes (CC0, ambientCG y Poly Haven)

CC0 (dominio público) confirmado en dos fuentes:
[docs.ambientcg.com/license](https://docs.ambientcg.com/license/) y la guía
independiente [LicenseOrg](https://www.licenseorg.com/guide/3d-assets/ambientcg) ✅.

| Para | Textura | Enlace |
|---|---|---|
| Tapa del cuaderno (cuero negro) | Leather026, Leather008 | [Leather026](https://ambientcg.com/view?id=Leather026), [Leather008](https://ambientcg.com/view?id=Leather008) |
| Cuero de Mello y Misa | Poly Haven leather (CC0 igual que ambientCG) | [polyhaven.com/textures/leather](https://polyhaven.com/textures/leather) |
| Hojas del cuaderno | Paper001, Paper003, Paper005 | [Paper001](https://ambientcg.com/view?id=Paper001) |
| Escritorio de Light | Wood039, Wood095 | [Wood039](https://ambientcg.com/view?id=Wood039) |

### Patrones y emblemas (para ropa y objetos)

- **Encaje de Misa**: no hay pack CC0 específico de encaje gótico; el
  patrón se puede montar con un pincel de lazo/randa de los packs de arriba
  o dibujarlo a mano (es simple: rombos con festón). No encontré una textura
  libre lista ⚠️ (busqué «gothic lace pattern CC0» y «lace brush free
  license»: sólo salieron packs de pago de Creative Market).
- **Cruces y calaveras** (motivo de Misa): sin pack de pinceles libre
  encontrado; se recomienda vectorizar a mano desde la referencia de §15
  (la pieza «Saint Valentine's Day» ya trae 4 diseños de calavera distintos
  para copiar la silueta, no el archivo).
- El **logo y la tipografía** «DEATH NOTE» son del investigador de texto
  (punto 5); aquí sólo dejo que **hojas/arte_oficial_01.jpg nº7** tiene el
  logo grande y limpio para sacar la silueta si hace falta.

---

## 23 · Colaboraciones y cruces

- **Jump Force** (Bandai Namco/Spike Chunsoft, PS4/Xbox One, 14-feb-2019):
  crossover oficial de Shūeisha por el 50º aniversario de Jump. Light Yagami
  y Ryuk son personajes jugables ✅ ([GameSpot](https://www.gamespot.com/articles/e3-2018-naruto-dragon-ball-one-piece-and-death-not/1100-6459612/),
  [Gematsu](https://www.gematsu.com/2018/06/jump-force-death-note-teaser-trailer)).
  Arte oficial del anuncio en **hojas/colaboraciones_02.jpg nº259-260**.
- **Universal Studios Japan** — evento «Universal Jump Summer»: Death Note
  fue parte del crossover veraniego de USJ con Shūeisha Jump (cartel oficial
  en **hojas/colaboraciones_02.jpg nº244**, `Universal_Jump_Summer.jpg` de
  la propia wiki) ✅ (imagen oficial alojada en `deathnote.fandom.com`; no
  encontré la nota de prensa de USJ en español o inglés que dé la fecha
  exacta ⚠️).
- **Othellonia × Death Note** (DeNA/MegaHouse, juego móvil de Othello):
  colaboración con wallpapers y cartas de personaje propios; el crédito
  «©大場つぐみ・小畑健／集英社・VAP・マッドハウス・NTV・D.N.・ドリームパートナーズ
  ／©Othello,Co. and MegaHouse／©DeNA Co.,Ltd.» aparece **en la propia
  imagen** ✅ (wallpapers en **hojas/arte_oficial_01.jpg nº37-42**, uno por
  personaje, 2208×2208; usados también para medir el hex de Mello en §15).
- **LINE Bubble 2** (LINE Corp, juego móvil): colaboración «デスノートコラボ»
  con stickers y power-ups de Ryuk y L, anuncios oficiales del juego ✅
  (**hojas/colaboraciones_03.jpg nº531, 538-539**, capturas «LINE Bubble 2
  Ryuzaki and Ryuk.jpg» y «LINE Bubble 2 ad 3/4.jpg» alojadas en la propia
  wiki). No encontré fecha exacta del evento ⚠️.
- **Uniqlo UT × Shonen Jump 50º aniversario**: camisetas de edición limitada
  de varias series de Jump, incluida Death Note, sólo en Japón ✅ (dos
  fuentes: [Aitai Kuji](https://www.aitaikuji.com/shonen-jump-50th-anniversary-x-uniqlo-t-shirts-bleach-death-note-and-jump),
  reventa confirmada en [eBay](https://www.ebay.com/itm/193286960166)).
- **XLARGE × Death Note** (streetwear, Japón): colección lanzada
  1-ene-2022 con camiseta, sudaderas y una **chamarra universitaria con
  mangas de cuero centrada en Ryuk**; Light, L y Misa también en la línea;
  ¥6.050-¥28.600 ✅ (dos fuentes:
  [Hypebeast](https://hypebeast.com/2021/12/death-note-xlarge-collection-release-info),
  [Highsnobiety](https://www.highsnobiety.com/p/death-note-xlarge-collab-collection-clothing/)).
  **Pose y ropa nuevas** para Ryuk: la chamarra varsity es un diseño que no
  sale en el anime, sirve como referencia de «Ryuk vestido de calle».
- **Team Liquid × Death Note** (esports, 29-mar-2024): línea de ropa que
  mezcla la estética del equipo con Death Note ✅ ([Team Liquid Store](https://store.teamliquid.com/blogs/news/team-liquid-x-death-note-apparel-collection-drops)),
  segunda fuente no encontrada con el mismo detalle ⚠️.
- **Cafés temáticos**: colaboración con **Toonique Cafe** en Hongdae (Seúl,
  Corea del Sur), menú y merchandising temáticos ⚠️ (una fuente,
  [KCulture](https://kculture.com/k-event/toonique-x-death-note-collaboration-cafe/);
  no da fecha exacta).
- **Death Note the Escape**: sala de escape real con el cuaderno como
  objeto central, cartel oficial en **hojas/colaboraciones_03.jpg nº536**
  ⚠️ (una fuente, la imagen de la wiki; no encontré el sitio de reservas
  vigente en 2026).
- **Pachislot/pachinko** (Sammy, 2008-2010): máquinas oficiales con arte
  propio de Light, L y Ryuk; el merchandising promocional de esa época
  (folletos, tomos de edición limitada) se revende hoy como coleccionable,
  de ¥3.000 a más de ¥80.000 ✅ ([OneMall, guía de coleccionista 2026](https://blog.onemall.jp/2026/04/16/death-note-merchandise-from-japan-2026-collector-buying-guide/)).
- **Figuras oficiales** (referencia 3D real, pose y volumen ya resueltos):
  **Good Smile Company** — Nendoroid y Nendoroid Petite de Light, L, Misa y
  Ryuk; **MegaHouse** y otras marcas japonesas — figuras a escala; Bandai —
  Candy Toys ✅ (dos fuentes: [OneMall](https://blog.onemall.jp/2026/04/16/death-note-merchandise-from-japan-2026-collector-buying-guide/),
  lista de la propia wiki [List of Death Note figurines](https://deathnote.fandom.com/wiki/List_of_Death_Note_figurines)
  — la wiki no da URLs de imagen directas, hay que verlas página por
  página con `investigar_serie.py` si se necesita una en concreto).
- **Cosplay** (para materiales y volumen reales, no para pegar): la
  gargantilla de cuero y las medias de encaje de Misa, y la camiseta/vaquero
  descalzo de L, son los disfraces más replicados; las guías con foto real
  están en §15 (Carbon Costume, Anime Fire). No until encontré un cosplay
  concreto premiado (tipo Crunchyroll Expo) con foto en alta y crédito
  claro ⚠️ (busqué «Death Note cosplay contest winner 2025/2026»: sólo
  salieron compilaciones sin autor).

---
 Fan art y renders 3D (sólo como referencia, nunca para pegar)

### Modelos 3D con licencia libre (Sketchfab, licencia confirmada por su API v3)

| Modelo | Autor | Licencia (API) | ♥ | Enlace |
|---|---|---|---|---|
| Death Note (cuaderno) | ayoub.oumahou (CG.oum) | CC Attribution | 134 | [38e9f0d](https://sketchfab.com/3d-models/none-38e9f0d0c6944557b6ecf2003f5aa4bb) |
| Death Note (cuaderno) | rengokukyojuro | CC Attribution | 37 | [9d98c78](https://sketchfab.com/3d-models/none-9d98c78fdeca4846a91b3e474bd5d038) |
| Death Note (cuaderno) | zevik-es | CC Attribution | 15 | [17e2a68](https://sketchfab.com/3d-models/none-17e2a68603464169b22ea5cdb8572f69) |
| Death Note anime book fanart | pedrohmm123 | CC Attribution | 14 | [9702482](https://sketchfab.com/3d-models/none-970248251f124cddbfc2b4999c43b713) |
| Death Note (cuaderno) | ParaGO | CC Attribution | 10 | [d82d654](https://sketchfab.com/3d-models/none-d82d6546f5994f128147748487f64ca8) |
| Death Note Notebook (fan-made, más detallado) | Efes3DStudio | **CC Attribution-NonCommercial** | — | [9bbeb99](https://sketchfab.com/3d-models/none-9bbeb99898f14d2cb01f4146a1a7d5c0) |
| Ryuk from Death Note | PotBin | CC Attribution | 19 | [cf0ccb0](https://sketchfab.com/3d-models/none-cf0ccb0310ea4bdd97122b6183e9e71b) |
| RYUK | Theo_Prodger | CC Attribution | 8 | [3c21e12](https://sketchfab.com/3d-models/none-3c21e12167fc482db5f5512eb34aff00) |
| ryuk death note | bakhats110 | CC Attribution | — | [7acb4b1](https://sketchfab.com/3d-models/none-7acb4b1db5d745f4a734686a469cbb89) |
| L from death note | bakhats110 | CC Attribution | 6 | [5ebc1b2](https://sketchfab.com/3d-models/none-5ebc1b2d188049d18c767283f9c4bdce) |
| light yagami from Death note | bakhats110 | CC Attribution | 17 | [7d05993](https://sketchfab.com/3d-models/none-7d0599365ae141f7b0b65cd55d27a06b) |

✅ todas: licencia leída directamente del campo `license.label` de
`api.sketchfab.com/v3/search` (no del resultado de búsqueda, del JSON real),
25-sep-2026. **CC Attribution = obligatorio citar al autor** en los créditos
de la lámina si se usa. No hay modelo de Misa ni de Near con licencia
descargable (busqué «misa death note» y «near death note» en la API: 0 y 2
resultados sin relación). **Consejo que ya daba la biblia vieja y sigue
valiendo**: el cuaderno es una caja con tapas, se modela en 10 minutos y así
la tinta y la luz son propias — usa estos sólo para ver grosor y lomo.

### Fan art 2D (Pixiv, ArtStation, Safebooru — mirar, jamás pegar)

- Etiqueta pixiv **夜神月** (Light): ~3500 ilustraciones; **L(DEATHNOTE)**:
  ~300; **リューク** (Ryuk): ~450 ⚠️ (cifras del buscador, no las conté una a
  una) · [夜神月](https://www.pixiv.net/en/tags/%E5%A4%9C%E7%A5%9E%E6%9C%88).
  Lo más dibujado: **Light con L** (pareja rival).
- Fan art mejor puntuado en Safebooru (con autor/origen, de
  `datos-imagen.md`): Light 3124×4000 (sin origen, puntos 6); Misa 3360×4096
  por [x.com/wjaefinbki3azde](https://x.com/wjaefinbki3azde/status/2031964125707022370)
  (puntos 22, el más votado de los cinco); Ryuk 719×1000 vía
  [pixiv img33](http://img33.pixiv.net/img/saipin/13000916.jpg); Near
  4937×8000 vía [minitokyo](http://gallery.minitokyo.net/view/635498) ✅
  (imágenes con URL directa comprobada en el JSON de Safebooru).
- **ArtStation** — Ryuk concept art de **Luca Nemolato**
  ([OKk2e](https://www.artstation.com/artwork/OKk2e)): es rediseño **de la
  película Netflix 2017**, no mezclarlo con el diseño del anime/manga ⚠️
  (una fuente, la propia pieza lo dice). Ryuk en ZBrush de **Maicon Ricardo**
  ([rRb5zO](https://www.artstation.com/artwork/rRb5zO)), estudio de luz de
  **Emilio Mansilla García** ([OyJ1E6](https://emilio_mansilla.artstation.com/projects/OyJ1E6)).
- **DeviantArt** — recreación de la página «How to use it» por
  **ShoushinNoKarera** ([79542089](https://www.deviantart.com/shoushinnokarera/art/Death-Note-How-to-use-it-79542089));
  compilación de +1000 screentones de manga (útil para §19) por
  **TheAwesomeAki-kun** ([681249872](https://www.deviantart.com/theawesomeaki-kun/art/1000-Manga-Screentone-Compilation-681249872)).

---
