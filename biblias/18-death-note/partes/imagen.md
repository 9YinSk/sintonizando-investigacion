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

## 3 · Fan art y renders 3D (sólo como referencia, nunca para pegar)

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
