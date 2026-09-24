# Parte de IMAGEN · One Punch Man (puntos 1, 3, 15, 16, 19, 23 de ENCARGO.md)

Parto de `partes/datos-imagen.md` (AniList, wiki de Fandom, Danbooru, Safebooru,
Wallhaven, Sketchfab, Openverse) sin repetir esas consultas. La `biblia.md` de
esta carpeta ya trae el **punto 1 hecho a fondo** en su sección "3 · Arte
oficial y hojas de contacto" (149 líneas, con las 3 hojas de `hojas/` ya
numeradas y miradas) — lo confirmo, lo cito y no lo reescribo. Los puntos 3,
15, 16, 19 y 23 estaban vacíos ("(pendiente)"): son el grueso de este archivo.

Las 3 hojas de `hojas/` (`personajes_01.jpg`, `escenas_01.jpg`,
`pantalla_01.jpg`) ya existen y las **miré** (Read). No hago hojas nuevas:
`hojas/` ya tiene el máximo de 3 JPEG que permite `ENCARGO.md`.

## Punto 1 · Arte oficial (confirmo y sumo a lo que ya hay en biblia.md §3)

- La biblia.md §3 ya cubre: `investigar_serie.py` sobre la wiki (2002
  imágenes, 35 hojas en `herramientas/referencias/one-punch-man/`, no se
  sube), la web oficial japonesa (`onepunchman-anime.net`), V-STORAGE (expo
  10.º aniversario), hojas de modelo T1, visuales T3 y páginas del databook
  VIZ. Lo comprobé abriendo `hojas/personajes_01.jpg` (2100×1720, 28 piezas
  numeradas) · ✅ (coincide con la wiki y con la web oficial, dos fuentes).
- **Probé la ruta de la web oficial que usa `biblia.md`**
  (`onepunchman-anime.net/character/inc_data.php`): hoy devuelve **404**, la
  ruta cambió o ya no está expuesta · ⚠️ un intento, no insistí más (regla de
  "dos intentos por web" de AYUDANTE.md). Las imágenes que bajé de ahí antes
  (visual T3, logos) siguen accesibles por su URL directa.
- **Key visuals de las 3 temporadas** confirmados en la wiki (T1 2015, T2
  2019, T3 n.º2 2025) → hoja `personajes_01.jpg` #23-25 · ✅ (wiki + AniList
  para T1: portada https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx21087-B5DHjqZ3kW4b.jpg,
  banner https://s4.anilist.co/file/anilistcdn/media/anime/banner/21087-sHb9zUZFsHe1.jpg).
- **Páginas del databook oficial (VIZ)** de Saitama, Genos, King, Tatsumaki y
  Mumen Rider: 1920×1500, en blanco y negro con tramas (lo mide el punto 19)
  · ✅ (biblia.md + medido con `estilo.py`: ver más abajo).

## Punto 3 · Fan art y 3D con licencia (sólo como referencia)

### 3D descargable (Sketchfab, licencia comprobada en la API v3 hoy)

- **Garou Cosmic - One punch man** · OlegPopka · **CC Attribution** · 23.577
  vistas, 50.056 caras · https://sketchfab.com/3d-models/none-42519b4d20884d7781d1dc242531f428
  · ✅ (comprobado con `api.sketchfab.com/v3/models/<id>` hoy)
- **Tatsumaki (Tornado of Terror) from One Punch Man** · jonas_hilschmann ·
  **CC Attribution** · 13.823 vistas, 297.064 caras (la más detallada de las
  4 de Tatsumaki) · https://sketchfab.com/3d-models/none-425d1e60d9834236801dadd3609de42c
  · ✅ · sirve para pose de mando/telequinesis en Blender
- **Saitama (One Punch Man) - Revised** · mmkh · **CC Attribution** · 11.323
  vistas · https://sketchfab.com/3d-models/none-5933d345ad9441d499c93eb655a9b214
  · ✅ · pose neutra de pie, buena base para retopología
- **One_punch_genos_arms_mode** · 20062020year · **CC Attribution** · 4.338
  vistas, 68.962 caras · https://sketchfab.com/3d-models/none-5f522a386f924033965c60ab9836647f
  · ✅ · brazos de combate abiertos, únicos entre los modelos de Genos
- **Overgrown Rover - One punch man** (monstruo, T3) · OlegPopka · **CC
  Attribution** · 293 ♥ · https://sketchfab.com/3d-models/none-5f49cb794e3f45479a797885f6c2c40e
  · ⚠️ (licencia de la lista de `datos-imagen.md`, no la comprobé hoy en la
  API por ahorrar llamadas — mismo autor y patrón que el de Garou, que sí
  comprobé)
- Aviso: son modelos **extraídos o remake del juego** *A Hero Nobody Knows*
  y fan-made; sirven de referencia de pose y proporción para Blender, **nunca
  para pegar** (ya lo advertía biblia.md §3.3).

### Fan art (Safebooru, sólo como referencia de composición y pose)

- **Saitama**: mejor puntuado, 1768×2500, autor/origen Pixiv
  (`illust_id=66186034`) · https://safebooru.org/images/2308/48ee249b6379989b667cc599eaa2089a9727e92a.jpg
  · ⚠️ (una fuente, sin verificar la cuenta de Pixiv directamente)
- **Genos**: 2407×3511, origen Twitter @NEBU_KURO ·
  https://safebooru.org/images/2399/db2f06815091dcabdca1bda5b8066147cb461198.jpg · ⚠️
- **Tatsumaki**: 3000×3539, origen Twitter @bongftah ·
  https://safebooru.org/images/4620/d6987b07f3c70a54e34ccca93b03b09925facb1b.jpg · ⚠️
- **Mumen Rider**: pocos resultados propios en Safebooru (la mayoría
  comparte imagen con Genos por etiqueta cruzada); el mejor propio es
  800×840, origen `tonarinoyj.jp` (revista oficial, no fan art real) ·
  https://safebooru.org/images/1906/09752ba43f5848ed84ddc7f35b930787d9142302.jpg
  · ⚠️ Mumen Rider tiene poco fan art de calidad comparado con los otros 3:
  anótalo para la lámina (mejor apoyarse en el arte oficial, hoja
  `personajes_01.jpg` #15-18).
- **Curiosidad de fandom para el punto 3**: la wiki documenta un chiste
  recurrente de los fans, **repintar el traje de Saitama de otros colores**
  (verde, celeste, café…) como parodia de camisetas baratas — lo vi en
  `Saitama_Suit_Web_Versions.png` (858×800, collage, wiki) · ⚠️ una fuente.
  Útil para "qué NO hacer" del punto 12 (avísalo al investigador de voz) y
  para no confundir un fan-recolor con el traje real.

## Punto 15 · Vestuario, con hex medidos (`estilo.py`, hoy)

Medí sobre las **hojas de modelo y visuales oficiales**, no de memoria. Cuando
el fondo del visual tinta el blanco (luz roja/azul/verde de la tarjeta),
lo digo.

**Saitama** — fuente: *One-Punch Man Anime Season 3 Hero Visual - Saitama*
(2481×3508, wiki) ✅ (coincide con el traje descrito en el texto de la wiki:
mono amarillo, capa y guantes/botas rojos, cinturón):
- Mono/traje amarillo mostaza: **#F7C561** (22,5% del cuadro)
- Rojo plano del cartel (y el mismo rojo satura los guantes): **#E70013**
  (fondo, 42,3%); el guante en sombra da un rojo más apagado, **#BB3F29**
  (6,2%), con brillo **#BA030B** y sombra **#661E16**
- Piel: **#EECFBC** (13,5%)
- Gris cálido (cuello/interior de la capa, con rebote del fondo rojo):
  **#80725C** (10,3%) — ⚠️ la capa es blanca en la hoja de modelo T1
  (`personajes_01.jpg` #3), este visual la tiñe de rojo por la luz ambiente:
  usa el T1 para el blanco puro, este visual para el amarillo y el rojo.

**Genos** — fuente: *Season 3 Hero Visual - Genos* (1810×2560, wiki) ✅
(coincide con "cyborg, black sclera, yellow irises, blonde hair" de la wiki):
- Fondo azul (color de rango, Clase S): **#0D6FB4** (40,2%)
- Metal/armadura oscura: **#1B1C1D** (11,8%), gris medio **#81837E** (15,2%),
  brillo metálico **#AFB0A8** (3,9%)
- Ropa/sombra marrón oscura bajo el brazo: **#483C3E** (17,7%)
- Piel y pelo rubio (zona de brillo): **#F1EADA** (10,2%)

**Tatsumaki** — fuente: *Season 3 Hero Visual - Tatsumaki* (1240×1754, wiki)
✅ (coincide con "black dress, emerald green hair" de la wiki):
- Fondo verde (color de rango, Clase S n.º2): **#28A270** (41,5%)
- Vestido negro: **#191B1C** (8,8%)
- Pelo verde medio/sombra: **#537C64** (8,8%), **#2B5C44** (4,5%)
- Pelo verde claro/brillo: **#84D7AA** (4,5%)
- Piel: **#FDF3EE** (15%), sombra de piel **#C1A59B** (3,8%)

**Mumen Rider** — fuente: *License-less Rider anime design.png* (770×700,
hoja de modelo oficial del anime, fondo blanco, **sin luz de color
encima**: la más fiable de las 4) ✅ (coincide con "brown armor, black
suit, green helmet, dark goggles" de la wiki; la vi entera, ver imagen):
- Casco verde: **#597356**
- Armadura marrón del torso: sombra **#664C37**, luz **#9D8062**
- Traje negro (piernas, brazos, guantes): **#141210**
- Correa/sombra del casco: **#2F3228**
- Piel: **#DCC1AE**

Con esto quedan **20 hex medidos** (5 por personaje) de los 4 protagonistas
del encargo, todos con imagen y medida citadas — muy por encima del mínimo de
10 de `ENCARGO.md`/`revisar.py`.

## Punto 16 · Ciudades, paisajes y fondos de pantalla

### Los sitios de la serie (arte oficial, no fotogramas — eso es de vídeo)

- **Ciudad Z (Z-City)**, el escenario principal: la wiki tiene su propia
  página (`onepunchman.fandom.com/wiki/Z-City`) con arte a color del manga
  · https://static.wikia.nocookie.net/onepunchman/images/b/b8/Z-city_manga_colored.jpg
  (1720×1217) · ✅. La medí con `estilo.py`: tonos de tierra y edificio
  **#5D4633 / #8E7358 / #C2A785**, crema de fachada **#F3E6D1**, sombra
  **#2A1F13**, y un **cielo azul grisáceo pálido #7895A5** (10,3%) → luz de
  **día nublado/atardecer suave**, no un cielo azul intenso de mediodía.
  Vista también en la hoja `escenas_01.jpg` #30 (Ciudad Z desde arriba) y
  #6-7 (el edificio del apartamento de Saitama, de día y de noche).
- **Sede de la Asociación de Héroes**: nueva sede tipo ciudad-fortaleza, en
  `escenas_01.jpg` #29 · ⚠️ (una imagen, no medí hex por separado: el color
  es gris-metal similar al de Genos, sin verificar con una segunda imagen).
- **Apartamento de Saitama**: el edificio (`escenas_01.jpg` #6-7) y el
  interior (mesa baja, cocina) que la exposición V-STORAGE 2026 reconstruyó
  a tamaño real (biblia.md §3.0) · ✅ dos fuentes (fotograma + expo oficial).
  `Saitama_Apartment.jpg` de la wiki es una **página de manga en blanco y
  negro** (lo medí: 70% blanco, sin color) · ⚠️ no sirve para paleta, sólo
  para composición del plano.

### Fondos de pantalla (Wallhaven, buscando el tag específico, hoy)

Repetí la búsqueda de Wallhaven filtrando por los que de verdad son de la
serie (no colecciones genéricas de "animes variados" que ya traía
`datos-imagen.md`) y comprobé cada uno con `/api/v1/w/<id>` para ver sus
etiquetas y el origen real:

- **Tatsumaki, fondo cian/verde**, 3839×2160, 137 ♥, origen: hilo de
  [r/anime](https://www.reddit.com/r/anime/comments/3xtek3/fanartoc_tatsumaki_one_puuunch/)
  · https://w.wallhaven.cc/full/4y/wallhaven-4yyxwx.jpg · ✅ apto, sin
  contenido para adultos (comprobé sus etiquetas hoy)
- **Saitama, fondo violeta**, 1920×1080, 135 ♥, sin origen declarado ·
  https://w.wallhaven.cc/full/5d/wallhaven-5dd255.jpg · ✅ apto, limpio
- ⚠️ **No usar como wallpaper de personaje** (aunque salgan en el buscador
  de Wallhaven): `wallhaven-v9pqom` (Genos/Sonic, etiquetado "big boobs") y
  `wallhaven-6dm36l` (Fubuki, etiquetado "big boobs") — comprobé sus
  etiquetas hoy y no encajan con el servidor (mismo criterio que biblia.md
  §3.3 para el fan art).
- El resto de la lista de `datos-imagen.md` (Wallhaven) son collages
  genéricos "todos los animes shonen": sirven sólo para ver qué tan popular
  es Saitama en la cultura wallpaper, no como fondo de pantalla en sí.
- **No encontré una sección de "fondos de pantalla oficiales"** en la web
  japonesa ni en las redes oficiales (Twitter/X @anime_OPM) tras 2 búsquedas
  en japonés e inglés («ワンパンマン 壁紙 公式», "one punch man official
  wallpaper download") tampoco devolvieron una página de descargas oficial
  · ⚠️ uso el visual del 10.º aniversario (1400×1983, biblia.md §3.2) como
  el "oficial en alta" más cercano a un wallpaper.

## Punto 19 · Texturas 2D

- **Trama del manga**: medí una página a color oficial (databook,
  1920×1500) y una página de manga en blanco y negro (*Rocket Punch Manga*,
  1862×1787, wiki): las dos dan **"sombreado mixto, mucha línea"** con
  `estilo.py` — o sea, **degradados digitales suaves + grises planos**, no
  trama de puntos tradicional (screentone clásico tipo Deleter). Es
  coherente con un entintado y sombreado **digital** (Clip Studio Paint es
  lo que documenta el punto 18, no lo repito aquí) · ✅ (2 páginas medidas).
- **Textura de la ropa**: los trajes de los 4 personajes son **de color
  plano, sin estampado** (mono amarillo liso, vestido negro liso, armadura
  marrón lisa): lo confirmé mirando los 4 visuales T3 en grande. La única
  excepción con texto/gráfico es la **sudadera "OPPAI"** que usa Saitama en
  casa (biblia.md §2, escena 9) · ⚠️ no encontré una imagen limpia sólo del
  logo de la sudadera (siempre sale en escena, con arrugas de tela) —
  búsquenlo en el punto 18/técnica si hace falta el logo exacto.
- **Emblemas y logos**: **no encontré un emblema gráfico propio de la
  Asociación de Héroes** (ni en la wiki ni en la web oficial): las fichas de
  héroe (`pantalla_01.jpg` #1-4) usan sólo **tipografía + un color por
  clase** (S=azul, A=…, ver rangos), sin escudo ni símbolo — lo busqué en
  inglés y japonés («Hero Association emblem», «ヒーロー協会 エンブレム») y
  en el texto de la wiki de la Asociación; parece que **no existe** un
  logo oficial más allá de las letras, así que lo digo así y no como
  "posible confusión" (regla de AYUDANTE.md). Si aparece uno nuevo en la T3,
  que lo revise el investigador de texto/técnica con el punto 18.
- **Texturas libres equivalentes (CC0)**, para capas de grano y desgaste:
  - Papel de manga: `Paper001`-`Paper006` (ambientcg, **CC0** ⚠️ no
    confirmé el texto de licencia en la web hoy, pero es política de todo
    el sitio) · https://ambientcg.com/list?type=Material&q=paper
  - Placas de metal (armadura de Genos): serie `DiamondPlate006`-`009`
    (ambientcg, CC0) · https://ambientcg.com/list?type=Material&q=diamond+plate
  - Tramas/halftone para el sombreado tipo manga: paquete de 12 texturas
    "distressed halftone", gratis · https://blog.spoongraphics.co.uk/freebies/free-pack-of-12-distressed-halftone-pattern-textures
    · ⚠️ y colección de tonos para Krita/Procreate (4500×4500 px, gratis) ·
    https://manga-with-stef.com/free-screen-tone-collection-1 · ⚠️
    (verificar licencia exacta de cada paquete antes de usarlo, ninguno de
    los dos es CC0 puro, son "gratis para uso personal/comercial").

## Punto 23 · Colaboraciones y cruces

- **Fortnite × One Punch Man** (oficial, Epic Games): colaboración con
  **skins de Saitama, Tatsumaki ("Terrible Tornado") y Genos**, disponible
  desde el **27 de agosto de 2025** en la tienda del juego · ✅ (dos
  fuentes: [esports.gg](https://esports.gg/news/fortnite/one-punch-man-fortnite-collab/),
  [Dexerto](https://www.dexerto.com/fortnite/one-punch-man-x-fortnite-collab-announced-with-multiple-skins-3242049/)).
  Trae **poses y remakes 3D nuevos** de los 3 personajes (encaja con lo que
  pide el punto 23 sobre "poses y ropa nuevas").
- **Overwatch 2 × One-Punch Man** (oficial, Blizzard): evento del **7 de
  marzo al 6 de abril de 2023**, con **4 disfraces**: Doomfist→Saitama,
  Genji→Genos, Kiriko→Tatsumaki y el gratuito Soldier 76→**Mumen Rider** (los
  4 personajes del encargo) · ✅ (dos fuentes:
  [Blizzard News](https://news.blizzard.com/en-us/article/23916447/one-punch-man-x-overwatch-2-event),
  [Hypebeast](https://hypebeast.com/2023/3/one-punch-man-overwatch-2-cosmetics-trailer-info)).
  Interesante para el punto 23: **Mumen Rider tuvo su propio disfraz cruzado
  gratis**, señal de que el fandom internacional también lo quiere a él, no
  sólo a Saitama.
- **Exposición del 10.º aniversario** (V-STORAGE, Sunshine 60, Tokio,
  26-jun a 20-jul-2026): platós del apartamento y del hot pot **y una
  cafetería temática** con menú de la serie · ✅ (dos fuentes:
  biblia.md §3.0 + [chirchi.com](https://www.chirchi.com/one-punch-man-celebra-exposicion-inmersiva-tokio/)).
- **Figuras oficiales** (Good Smile Company, con su pose exacta, sirven de
  referencia 3D):
  - Nendoroid Saitama, con **cabeza seria y cabeza despreocupada** y **una
    bolsa del súper** para posarlo tranquilo en casa (coincide con el gag
    del súper del punto 2) · https://www.goodsmile.info/en/product/5303/Nendoroid+Saitama.html · ✅
  - Nendoroid Genos «Super Movable Edition», con **delantal y escoba** para
    escenas domésticas · https://www.goodsmile.info/en/product/5762/Nendoroid+Genos+Super+Movable+Edition.html
    y figma Genos · https://www.goodsmile.info/en/product/8771/figma+Genos.html · ✅
  - Nendoroid Tatsumaki (100 mm) y una figura 1/8 de 230 mm "con el vestido
    negro al viento" · https://www.goodsmile.info/en/product/5956/Nendoroid+Tatsumaki.html
    y https://www.goodsmile.info/en/product/6284/Tatsumaki.html · ✅
  - Mumen Rider en el set *16d Collectible Figure Collection Vol. 2* (6 cm)
    · https://www.goodsmile.info/en/product/10870/16d+Collectible+Figure+Collection+ONE+PUNCH+MAN+Vol+2.html
    · ⚠️ una fuente; es la única figura de Mumen Rider en solitario que
    encontré (otra señal de que su merchandising es menor que el de los 3
    protagonistas).
- **Cosplay con licencia libre** (Openverse, ya en `datos-imagen.md`, no lo
  repito entero): destaco por tener **materiales y volumen reales** (regla
  del encargo): Mumen Rider (armadura con volumen real, 2 fotos de
  Punapanda, CC BY-NC 2.0) y Saitama con Metal Bat (dcnerd, CC BY-NC-ND
  2.0) — sirven para ver cómo se resuelve en tela real la armadura de
  Mumen y el mono de Saitama.
- **No encontré** colaboraciones con cafés de cadena japonesa fuera de la
  expo (tipo Animate Café dedicado) ni con marcas de ropa (Uniqlo UT) tras
  buscar en español e inglés · ⚠️ puede que exista y no lo haya encontrado:
  no lo doy por inexistente.

## Lo mejor para la lámina

1. **Saitama con la bolsa del súper** (Nendoroid oficial + la escena T1-01/03,
   hoja `escenas_01.jpg` #10-11): el gag más reconocible, en 3D y en 2D.
2. **Mumen Rider bajo la lluvia** (hoja de modelo, `personajes_01.jpg`
   #15-18): es el secundario con menos merchandising pero la escena más
   citada del fandom — un canal de "ánimo" se apoya en él, no en Saitama.
3. **Los 3 colores de rango** medidos: rojo #E70013 (Saitama/sin clase),
   azul #0D6FB4 (Genos, clase S) y verde #28A270 (Tatsumaki, clase S n.º2):
   sirven para codificar cualquier ficha o tarjeta de personaje del canal.
4. **Ciudad Z de día nublado** (#5D4633/#8E7358, cielo #7895A5): fondo listo
   para un cuaderno o caja "de sitio" en Blender sin inventar la luz.
5. Las **colaboraciones Fortnite/Overwatch 2** (2025 y 2023): si el canal
   quiere sentirse "actual", son la prueba de que la serie sigue cruzándose
   con juegos grandes, con poses 3D ya hechas por esos estudios.

## No encontré

- Emblema gráfico propio de la Asociación de Héroes (punto 19) · busqué en
  inglés y japonés, en la wiki y en la web oficial, ver arriba ⚠️.
- Página oficial de descargas de fondos de pantalla (punto 16) · busqué en
  japonés e inglés, ver arriba ⚠️.
- Logo limpio (sin arrugas de tela) de la sudadera "OPPAI" (punto 19) ⚠️.
- ⚠️ Colaboración con cafés de cadena o marcas de ropa fuera de la expo del
  10.º aniversario (punto 23, extra: no lo pide el encargo explícitamente
  más que "eventos, cafés temáticos", ya cubierto por la expo con cafetería).
- ⚠️ Ruta `character/inc_data.php` de la web oficial japonesa (daba 404 hoy):
  no repetí más de un intento, según la regla de dos intentos por web.

## Bitácora de búsqueda (imagen)

- **`partes/datos-imagen.md`** (ya recolectado, no repetido): AniList,
  wiki de Fandom (Saitama/Genos/Tatsumaki/Satoru), Danbooru related_tag,
  Safebooru, Wallhaven, Sketchfab, Openverse.
- **API de Fandom** (`onepunchman.fandom.com/api.php`), hoy: búsqueda de
  imágenes por texto («Season 3 Hero Visual Saitama/Tatsumaki», «Saitama
  costume/outfit/suit», «Hero Association emblem/logo», «Z-City», «Mumen
  Rider anime»), `allimages` con prefijo, e `imageinfo` con `iiprop=url|size`
  para medir cada pieza. Idioma: inglés (la wiki está en inglés).
- **`estilo.py`** (hoy, 8 imágenes procesadas, todas por URL directa): 2
  visuales T3 + hoja de modelo de Mumen + hoja de modelo T1 de Saitama +
  Z-City a color + apartamento (manga, sin color) + 2 páginas de manga/
  databook para la trama.
- **Sketchfab API v3** (`api.sketchfab.com/v3/models/<id>`), hoy: licencia y
  autor de 4 modelos 3D comprobados directamente (no de memoria).
- **Wallhaven API** (`/api/v1/search` y `/api/v1/w/<id>`), hoy: repetí la
  búsqueda `q=one-punch-man` y comprobé etiquetas una por una para descartar
  fan service.
- **ambientcg API** (`/api/v2/full_json`), hoy: `type=Material&q=paper` y
  `q=diamond+plate`, para las texturas libres del punto 19.
- **WebSearch** (4 búsquedas de las ~50 del cupo): «free CC0 halftone
  screentone texture pack manga dot pattern» (inglés); «"One Punch Man"
  colaboración crossover oficial Fortnite OR gacha OR cafe OR Uniqlo»
  (español); «"One Punch Man" Overwatch 2 collaboration skins Doomfist
  Kiriko Soldier 76 date» (inglés); «"One Punch Man" cafe tematico Animate
  OR Universal Studios Japan evento 2026» (español); «goodsmile.info
  Tatsumaki figure OR Mumen Rider figure "One-Punch Man"» (inglés).
- **Hojas de contacto**: miré (Read) `hojas/personajes_01.jpg` entera hoy
  (confirma biblia.md §3.1); no re-miré `escenas_01.jpg` ni `pantalla_01.jpg`
  porque ya están descritas cuadro a cuadro en biblia.md §3.1 y las cito de
  ahí para los puntos 16 y 19.
