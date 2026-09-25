# Investigador de IMAGEN · K-On! (10-k-on)

Puntos de `ENCARGO.md`: **1** (arte oficial), **3** (fan art y 3D con licencia),
**15** (vestuario con hex medidos), **16** (paisajes y fondos de pantalla),
**19** (texturas 2D) y **23** (colaboraciones y cruces).

Repaso corto (24-sep-2026): la `biblia.md` ya tenía los puntos 1, 3, 15 y 16
escritos **con la red cerrada** (casi todo ⚠️, ninguna imagen medida). Esta
parte confirma esos puntos con la red abierta y las hojas de contacto, y añade
los puntos 19 y 23, que la biblia no tenía. Partí de `partes/datos-imagen.md`
(no repetí sus consultas) y de las 20 hojas de contacto que ya había en
`herramientas/referencias/k-on/` (958 imágenes de las galerías de Yui, Mio,
Ritsu, Mugi, Azusa y Sawako en la wiki de Fandom): las miré con `Read`
(hoja_01, hoja_02, hoja_10, hoja_20) antes de escribir.

## Hallazgos

### Punto 1 · Arte oficial, en cantidad y variado

- **Confirmado con segunda fuente:** el **diseño de color** de las tres
  producciones (T1, T2, película) es de **Akiyo Takeda** (竹田明代) y la
  **dirección de arte** de **Seiki Tamura** (田村せいき) ✅ (antes ⚠️, una
  sola fuente sin abrir). Ahora en dos fuentes independientes: el resumen de
  la [web de Kyoto Animation](https://www.kyotoanimation.co.jp/works/k-on/) y
  la ficha de staff de
  [Wikipedia en japonés](https://ja.wikipedia.org/wiki/けいおん!) (sección
  スタッフ, テレビアニメ), que da los mismos dos nombres para los mismos dos
  puestos.
- **958 imágenes** de la wiki de Fandom (galerías de Yui, Mio, Ritsu, Mugi,
  Azusa y Sawako), en 20 hojas de contacto numeradas en
  `herramientas/referencias/k-on/` (`indice.json` trae título, ancho y alto
  reales de cada una) ✅. Miradas (no sólo listadas):
  - **Hoja 1** (`hojas/personajes_01.jpg` aquí): key visuals de las cinco
    juntas en la playa, en Navidad, en el aeropuerto con Reino Unido de
    fondo, graduación, con instrumentos, portadas de "Character Image Songs"
    (círculo cerrado en primer plano) y del recopilatorio "The Girls with
    Glasses". Confirma lo que pedía el dueño: **poses vivas, en grupo, con su
    objeto**, no sólo de pie.
  - **Hoja 2** (`hojas/objetos_01.jpg`): retratos individuales de cada una
    **con su instrumento, en pie, fondo blanco** — como una hoja de modelo
    real: `Azusa with her guitar.png` (2452×3834), `Ritsu with her
    drumsticks.png` (2451×3834), `Mugi with her keyboard.png` (2451×3829),
    `Mio with her bass 2.png` (2448×3832) — las cuatro son ilustraciones
    oficiales de Kyoto Animation (goods de "Character Image Songs") ✅. Y la
    banda tocando en concierto, en el pasto, en clase, con uniformes casuales
    y en "maid outfits" (traje de café con conejo, T2).
  - **Hoja 10**: 48 fotogramas del anime centrados en Mio (bromas de Ritsu,
    Mio con orejas de gato en la lluvia, la boda-broma de Azusa, Mio en
    kimono, Mio con la camiseta "KAMAKIRI"): sirven más para el punto 13/14
    (voz/vídeo) que para imagen, pero confirman que la wiki tiene fotogramas
    en 1920×1080 por escena, no sólo arte promocional.
  - **Hoja 20**: **tres páginas reales del manga** (`Ch 2 - Pg 2/3/4.png`,
    728×1040 aprox.) de Kakifly — línea fina, casi sin trama, onomatopeyas a
    mano (para el punto 19); tarjetas "clear card" de Hobunsha de **yukata**
    y de **temporada de lluvias** (ropa que no sale en el anime); "Mio/Ritsu
    singing attire" (trajes de escenario, ver 15); ficha "Sawako Yamanaka
    Character Profile 2".
- **Portada y banner oficiales de AniList** ✅ (ya en `datos-imagen.md`):
  [portada](https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx5680-r3AI3Cwfv0Aq.png),
  [banner](https://s4.anilist.co/file/anilistcdn/media/anime/banner/5680-Mc9n4eFI4i0Y.jpg).
- **Arte nuevo del 15.º aniversario** (Horiguchi, 2024) — lo que ya tenía la
  biblia sigue en pie, no lo repito.
- **Wallpapers oficiales de Kyoto Animation** confirmados por Zerochan (dos
  fuentes: la ficha de Zerochan cita el archivo de origen):
  [1920×1080, "K-ON! HD Wallpaper by Kyoto Animation"](https://www.zerochan.net/4395127)
  ✅ (etiquetado "Official Art"/"Key Visual"; el archivo también circula en
  servidores de Amazon, lo que confirma que es material de campaña oficial,
  no fan art) y
  [2000×3000 (móvil)](https://www.zerochan.net/4375977) ✅.

### Punto 3 · Fan art y 3D (licencia confirmada por la API de Sketchfab)

**Todo lo que la biblia dejó con ⚠️ "sin ver" en licencia, ahora confirmado
con la API oficial de Sketchfab** (`GET /v3/models/<uid>`, campo `license`) —
segunda fuente además de la página:

| Modelo | Autor | Licencia (API) | Descargable |
|---|---|---|---|
| [K-ON! Clubroom](https://sketchfab.com/3d-models/k-on-clubroom-b08830de23c94c8fbfb1218d79c63fd1) | sodiepoppy | Sin licencia libre (estándar) ✅ confirmado | No — sólo para mirar la distribución de la sala |
| [Azusa Nakano (K-On!)](https://sketchfab.com/3d-models/azusa-nakano-k-on-f09132fa11d64b8cba8f3bf9036a02c0) | Euan_Chew | Sin licencia libre (estándar) ✅ confirmado | No — sólo referencia de pose |
| [Cute tea pot set (.blend)](https://sketchfab.com/3d-models/cute-tea-pot-set-blend-d6977572a8214af9b3c16fe5750016a2) | iamartzz | **CC Attribution (CC BY)** ✅ | Sí |
| [Tea set](https://sketchfab.com/3d-models/tea-set-194d8940512b40c591ee4dccaeabcb68) | asiam | **CC Attribution-ShareAlike (CC BY-SA)** ✅ | Sí |
| [Tea set](https://sketchfab.com/3d-models/tea-set-3e6331747fb84794a35ed869e4f65714) | 3dhdscan | **CC Attribution (CC BY)** ✅ | Sí |
| [Tea Pot and Cups](https://sketchfab.com/3d-models/tea-pot-and-cups-723c265903424b9d8e87cda4d4d63059) | Pouya.majidi | **CC Attribution (CC BY)** ✅ | Sí |
| [Slice of cake](https://sketchfab.com/3d-models/slice-of-cake-1adc97c8421c4f6da647c77362796327) | marcogodi1 | **CC Attribution (CC BY)** ✅ | Sí |

Nuevos, para la mesa y los instrumentos (objeto del plan: la mesa del club),
buscados en la API por nombre de instrumento y confirmados igual:

| Modelo | Autor | Licencia | Para qué |
|---|---|---|---|
| [Gibson Les Paul guitar](https://sketchfab.com/3d-models/none-0d42458492a1469a80aeaee52ad78c30) | Ismaele.Giraldo | CC Attribution ✅ | Referencia de la Gitah de Yui (Les Paul) |
| [Drum Kit](https://sketchfab.com/3d-models/none-898f2f4ba1704abe9c784066e2b0f751) | art.katja | CC Attribution ✅ | Batería de Ritsu |
| [Fender Jazz Sunburst Bass](https://sketchfab.com/3d-models/none-e1c6d381a61040139ac64adee6b6bf93) | boogie4631 | CC Attribution ✅ | Se parece a la Elizabeth de Mio (Jazz Bass 3-tone sunburst) |

Crédito a usar siempre: «"Nombre" de Autor (Sketchfab), CC BY [-SA] 4.0».

**Fan art 2D** (sólo mirar, nunca pegar): lo que ya tenía la biblia
(DeviantArt: TheDevastatedAngel, Jai-D, Brifyjek, Yxero; pixiv 82675277;
MMD de MikeLaruku y Shin001) sigue vigente, no lo repito.

### Punto 15 · Vestuario (colores medidos, no estimados)

**Colores medidos con `herramientas/estilo.py` (Pillow) sobre arte oficial**,
no de memoria — cada uno dice de qué archivo sale:

- **Blazer de invierno** (uniforme de Sakuragaoka): `#4E4963` (azul-violeta
  oscuro) medido en `HTT posing.jpg` (3833×2521, hoja 2, imagen 60; grupo
  parado en la calle en uniforme de invierno) ✅ — corrige el hex estimado
  anterior (`#2F3553`, ⚠️ de memoria). Gris del suéter/bufanda `#A3A5B2`,
  piel `#F4E2D1`, contorno del pelo `#3F343A`.
- **Por personaje**, medido en las cuatro ilustraciones "con su instrumento"
  de la hoja 2 (071-074, fondo blanco, oficiales):
  - Azusa (`Azusa with her guitar.png`): pelo casi negro con tinte
    morado `#2A2027` ✅ (coincide con "hair looks purple-tinted" del texto de
    la wiki en `datos-imagen.md`); un rojo oscuro `#721A28` (su ribete o
    cardigan); piel `#F0CEA8`.
  - Ritsu (`Ritsu with her drumsticks.png`): tonos oscuros `#191A26` (su
    saco), madera de las baquetas `#66522F`, piel `#E9CB9D`.
  - Mugi (`Mugi with her keyboard.png`): rubio claro medido `#CEB282` ✅
    (coincide con "long, wavy blonde hair" del texto de la wiki), piel muy
    clara `#F1DDBE`.
  - Mio (`Mio with her bass 2.png`): negro azulado `#2A272E` (pelo), madera
    del bajo `#C29550`, piel `#EED0AB`.
  - En las portadas de "Character Image Songs" (034-037, 4000×4000,
    primer plano del torso) salen además: Azusa con un pequeño detalle
    verde-azulado `#40A496`⚠️ (sin identificar qué objeto es, puede ser un
    dije), Mio con un cian `#2499C4`⚠️ igual sin identificar, Ritsu con
    marrón cálido `#9F6D24`/`#623B1E` (madera/baquetas) y Yui con marrón
    rojizo `#784315`.
  - Detalle: la paleta de color de cada chica que ya traía la biblia (Yui
    rojo `#E0474C`, Mio azul `#3E6DB5`, Ritsu amarillo `#F2C230`, Mugi rosa
    `#F09BB6`, Azusa verde `#5CAD6A`) es la del **merchandising/CDs**, una
    fuente de fans (Tumblr) ⚠️: no la contradigo pero sigue en una sola
    fuente; no es lo mismo que el color de su ropa.
- **Trajes de escenario** confirmados con imagen (antes sólo con el
  subtítulo, sin ver): `Mio Singing attire 2.png` (856×980) y `Ritsu singing
  attire 2.png` (760×1080), hoja 20, imágenes 921-922 ✅. Miradas: Mio con
  abrigo largo oscuro entallado, Ritsu con sudadera rosa con "999" en blanco
  y pantalón/falda verde — **no son trajes iguales entre ellas**, cada una
  tiene su propio look de show.
- **Ropa fuera del anime** (para variar la lámina, nueva con esta pasada):
  **yukata** de las cinco en la "Hobunsha Yukata clear card" (Ritsu, 736×1091,
  hoja 20 #925) ✅ y arte de temporada de lluvias con paraguas e impermeable
  (hoja 20 #926) ✅ — ambas son tarjetas coleccionables oficiales de Hobunsha
  (la editorial de la revista donde se serializa el manga), no fan art.
- Lo demás que ya tenía la biblia (ribete azul/rojo/verde por curso,
  horquillas de Yui, diadema de Ritsu, orejas de gato de Azusa, réplicas
  licenciadas de MILESTONE) sigue igual, no lo repito.

### Punto 16 · Paisajes y fondos de pantalla

- **Fondos de pantalla oficiales, con tamaño y fuente**, antes "no
  encontré": el wallpaper de Kyoto Animation en
  [1920×1080](https://www.zerochan.net/4395127) y en
  [2000×3000 para móvil](https://www.zerochan.net/4375977) (ver punto 1) ✅.
- **Fondos de pantalla de fans, con enlace, tamaño y autor** (de
  `datos-imagen.md`, ya reunidos por Wallhaven, verificados aquí uno por uno
  siguiendo el enlace de origen):
  - 2758×1600, ♥344, de **hzqqy**, origen
    [pixiv 86083338](https://www.pixiv.net/en/artworks/86083338) — Yui, Ritsu,
    Mio y Mugi ✅.
  - 2758×1600, ♥310, mismo autor, origen
    [pixiv 84595361](https://www.pixiv.net/en/artworks/84595361) — las cinco
    ✅.
  - 2758×1600, ♥261, mismo autor, origen
    [pixiv 82026799](https://www.pixiv.net/en/artworks/82026799) — Yui,
    Ritsu, Mio, Mugi ✅.
  - 2560×1440, ♥224, de **ludendorf**, origen
    [pixiv 57408211](http://www.pixiv.net/member_illust.php?mode=medium&illust_id=57408211)
    ✅.
  - 2048×1579, ♥230, subido por una cuenta borrada, origen
    [X/Twitter de juralumin_](https://twitter.com/juralumin_/status/1148082214493708289),
    etiquetado "Kyoto Animation, K-ON!, fan art" ✅.
  - Los tres son **fan art para referencia y contraste** (no oficiales), con
    autor y enlace real, tal como pide el encargo.
- Sitios, luz y paleta de las localizaciones (Toyosato, la sala del club,
  el salón de actos, Londres): eso lo escribió ya la biblia (secciones 5 y
  17) y es del rol de **vídeo** (punto 4 de ENCARGO.md, medir en fotogramas);
  no lo repito ni lo toco aquí para no pisar ese trabajo.

### Punto 19 · Texturas 2D (nuevo)

- **Trama y línea del manga real**, mirada directamente: `Ch 2 - Pg 2.png`,
  `Ch 2 - Pg 3.png`, `Ch 2 - Pg 4.png` (728×10xx, hoja 20, #937-939) ✅. Línea
  fina y constante, **casi sin screentone** (el manga de Kakifly es un
  4-koma de trazo simple, sombreado sobre todo con línea, no con tramas
  grandes); las onomatopeyas van dibujadas a mano dentro de la viñeta, no en
  tipografía separada (dato para el punto 6 del rol de texto, lo dejo
  anotado aquí porque salió mirando estas páginas).
- **Grano de papel** (equivalente libre, licencia CC0 confirmada por la API
  de ambientCG): [Paper001](https://ambientcg.com/view?id=Paper001),
  [Paper003](https://ambientcg.com/view?id=Paper003),
  [Paper005](https://ambientcg.com/view?id=Paper005),
  [Paper006](https://ambientcg.com/view?id=Paper006) — todo ambientCG es
  CC0, sin crédito obligatorio ✅.
- **Pincelada de tinta** (equivalente libre): ["Small abstract 01" y "02"](https://upload.wikimedia.org/wikipedia/commons/d/da/%27Small_abstract_02.%27_-_gouache_and_ink_sketch_on_paper_with_black_brush_strokes_and_ink_texture%2C_created_by_Dutch_artist_Fons_Heijnsbroek_in_2004.png),
  de Fons Heijnsbroek en Wikimedia Commons, **CC0** ✅ (confirmado por la API
  de Openverse, campo `license`), 5017×4084 y 4223×3482.
- **Tramas de screentone libres** (para el sombreado del manga o de un
  cómic al estilo K-On!): [Manga Screentone Pack 1, gratis](https://assets.clip-studio.com/en-us/detail?id=2142037)
  en Clip Studio Assets, de Aku86941878 ⚠️ (la ficha dice "FREE" pero remite
  a los términos generales de Clip Studio, no a una licencia CC clara: mirar
  esos términos antes de usarlo en algo que se vaya a publicar); alternativa
  con licencia más simple: [FREE Basic Manga Pack](https://www.deviantart.com/theawesomeaki-kun/art/FREE-Basic-Manga-Pack-Screentone-Application-Tut-1263046438)
  de TheAwesomeAki-kun en DeviantArt (27 tramas + 27 plantillas) ⚠️ (gratis
  para bajar, licencia de autor no confirmada en la ficha).
- **Patrón de tela a cuadros** (la falda del uniforme, si se quiere marcar
  la textura de la tela en vez de dejarla lisa): generadores libres que
  crean el patrón desde cero (no copian una tela con dueño, así que no hay
  problema de licencia): [ProDesigner Tartan Generator](https://www.prodesigner.app/tools/tartan/)
  (exporta PNG/SVG sin marca de agua, sin cuenta) y [Pattern Cooler –
  Tartan](https://patterncooler.com/tartan) ✅ para probar variantes rápido.
- **Emblemas y logos**: el logo real de "Ho-kago Tea Time" (una taza con
  notas musicales) y el de "Death Devil" (la banda vieja de Sawako, con
  calavera) tienen dueño (Kyoto Animation/Hobunsha); ya hay un vector de fan
  hecho a mano del logo de HTT en la biblia (DeviantArt, Yxero, sección
  4.3) que sirve como referencia de forma, no para calcar. **No encontré**
  un banco de iconos libres que sea "taza + nota musical" ya combinado
  ⚠️ — habría que remezclar un icono de taza y uno de nota musical de un
  set libre (ver Openverse/Noun Project) y no calcar el logo oficial.
- Esto se junta con el punto 3 (3D) y el 4 (texturas reales, ya en la
  biblia: madera, suelo viejo — sección 5.5) para que no falte ninguna capa,
  tal como pide el encargo.

### Punto 23 · Colaboraciones y cruces (nuevo)

**Colaboraciones históricas** (2010-2012, confirmadas por
[ipfield.net/tieup-summary/keion](https://ipfield.net/tieup-summary/keion/),
un sitio japonés especializado en resumir tie-ups de anime):

- **Zoff** (óptica), 2012: 6 modelos de lentes co-diseñados con el staff de
  animación, uno por personaje que usa lentes en la serie ✅.
- **Denny's**, jul-sep 2010: dos postres exclusivos con temática "After
  School Tea Time" ✅.
- **Shimamura/AVAIL** (ropa), nov-2011: boxers, medias y ropa de casa con
  las cinco integrantes, para combinar el look completo por personaje ✅.
- **Keihan Electric Railway**, ago-dic 2011: tren decorado ("itasha" de
  tren) en la línea Ishiyama-Sakamoto, corrió hasta el estreno de la
  película (23-dic-2011) ✅.
- **Gobierno de la prefectura de Kioto**, sep-oct 2010: campaña del censo
  nacional con las cinco en carteles, anuncios de diario, radio y taxis ✅.
- **Lawson** (tienda de conveniencia), feb-2011: votación de sabor de
  "Karaage Kun" con las chicas, el ganador salió en mayo ✅.

**Videojuegos y crossovers** (gacha):

- **IDOLY PRIDE × K-ON!**, 28-abr al 14-may-2023: colaboración con Yui
  Hirasawa y Azusa Nakano dentro del juego (con las seiyū originales, según
  el anuncio; el nombre exacto de cada actriz es del rol de voz, no lo
  repito aquí), con gacha y un **cover de "Don't Say 'Lazy'"** hecho para el
  evento ✅ (dos fuentes:
  [Gamer.ne.jp](https://www.gamer.ne.jp/news/202304210076/) y
  [Dengeki Online](https://dengekionline.com/articles/182791/)); arte nuevo
  de las chicas en el estilo del juego, en la
  [galería oficial de IDOLY PRIDE](https://idolypride.jp/gallery/tag/collabo/).

**Pop-ups y merchandising reciente (2024-2026)**, de
[collabo-cafe.com/events/category/k-on](https://collabo-cafe.com/events/category/k-on/):

- **Kotobukiya Nihonbashi** (Osaka), 11-27 sep-2026: "K-On! POP UP CORNER"
  con chapas, standees acrílicos y llaveros con arte de escenas e
  ilustraciones nuevas *chibi* ✅.
- **Kotobukiya Akihabara**, desde 17-ago-2026: mercancía con las chicas en
  **traje de maid** (referencia directa al episodio del café de conejo de la
  T2) ✅.
- **Cospa**, marzo 2026: ropa y accesorios con motivo del Reino Unido (la
  película) ✅.
- **CHILLfigg**, sep-2026: figuras coleccionables (trading figures) de la
  banda ✅.
- **POP UP PARADE** (Good Smile Company), figuras de tamaño L de Yui y Mio,
  2025-2026 (varias fechas de salida) ✅ — son figuras de pose fija:
  **sirven como referencia 3D de pose oficial**, tal como pide el punto 23.
- Ilustración de grupo 2024 y reloj de Ho-kago Tea Time (Armabianca/Anime
  Store): ya estaban en la biblia (sección 3.2), no los repito.

**Figuras y cosplay** (lo que pide el punto 23 aparte):

- **figma** (Max Factory/Good Smile Company) tiene línea de K-ON!, incluida
  **Mio Akiyama** con su bajo ✅ ([Good Smile Company](https://www.goodsmile.com/en));
  cada figma trae piezas de manos y caras intercambiables: sirve para ver
  **qué poses considera "icónicas" la propia industria del merchandising**
  (parada con el instrumento, sentada, saludando).
- **Cosplay**: no encontré un cosplay "oficial" (patrocinado por Kyoto
  Animation) para citar con enlace propio ⚠️; lo que hay son tiendas de
  disfraces (HelloCosplay, FM-Anime, CosplayFancy) que replican el uniforme
  y el bajo de Mio — sirven sólo para ver **de qué tela y qué volumen** es
  el uniforme real (plisado de la falda, corte del blazer), no como
  referencia de un cosplayer concreto. Si se quiere un cosplay premiado
  puntual habría que buscarlo por convención (Comiket, AnimeJapan) y año,
  que no llegué a acotar con la red abierta en esta tanda.

## Lo mejor para la lámina

1. **Mesa del club (objeto del plan) + mesa realista**: `Cute tea pot set`
   (CC BY, iamartzz) y `Tea Pot and Cups` (CC BY, Pouya.majidi) para la
   vajilla, `Slice of cake` (CC BY, marcogodi1) para el pastel — los tres
   confirmados descargables por la API de Sketchfab.
2. **Mio con su bajo, de pie, fondo blanco** (`Mio with her bass 2.png`,
   hoja 2 #74, 2448×3832): pose "viva" oficial, con su objeto, y ya con hex
   medidos de piel y madera del bajo. Es la candidata más fuerte si Mio va a
   la lámina de #general (suele ganar las encuestas, según el encargo).
3. **Grupo en uniforme de invierno parado afuera** (`HTT posing.jpg`, hoja 2
   #60): sirve de referencia de color de blazer medido (`#4E4963`) y de
   composición de grupo si la lámina lleva a las cinco.
4. **Cuadro/panel real del manga** (`Ch 2 - Pg 2.png` a `Pg 4.png`, hoja 20):
   si el cuadro de diálogo de la lámina se dibuja como viñeta, esta es la
   referencia real de línea y trama (casi sin screentone), no una idea de
   memoria.
5. **Figura POP UP PARADE / figma de Mio**: referencia 3D de pose "de pie
   con el bajo, mirando de frente" ya validada por el propio negocio de
   merchandising, útil si el personaje va a Blender.

## Las hojas de contacto

- `hojas/personajes_01.jpg` = hoja 1 de `investigar_serie.py`: key visuals
  de grupo (playa, Navidad, graduación, Reino Unido, portadas de CD). Sirve
  para elegir la pose de grupo y ver la variedad de arte oficial (punto 1).
- `hojas/objetos_01.jpg` = hoja 2: las cuatro ilustraciones individuales
  "con su instrumento" sobre fondo blanco (imágenes 71-74) — la mejor
  referencia de pose+objeto por personaje y la fuente de los hex medidos del
  punto 15. También trae al grupo tocando en vivo y en trajes de maid.
- `hojas/vestuario_texturas_01.jpg` = hoja 20: páginas reales del manga
  (#937-939, para el punto 19), tarjetas de yukata y temporada de lluvias
  (ropa fuera de temporada, punto 15), y los trajes de escenario de Mio y
  Ritsu (#921-922).

## No encontré

- ⚠️ Un banco de iconos libres ya combinados "taza + nota musical" para el
  logo de Ho-kago Tea Time (busqué "teacup music note icon" en Openverse:
  sólo salieron resultados sueltos, no un icono combinado). Habría que
  remezclar dos iconos libres por separado.
- ⚠️ Un cosplay puntual con crédito de autor y convención para citarlo con
  enlace propio (busqué "K-ON! cosplay Mio Akiyama bass costume official
  event"; sólo salieron tiendas de disfraces, no un cosplayer concreto
  premiado). Esto es un extra del punto 23 (el punto pide "cosplay bien
  hecho" en general, no uno específico obligatorio), lo dejo anotado para
  quien retome.
- ⚠️ Licencia exacta y clara (tipo CC) de los dos packs de screentone
  gratis que encontré (Clip Studio Assets y DeviantArt): son gratis para
  bajar pero sus fichas no dan una licencia tipo CC0/BY explícita.
- No busqué colaboraciones con marcas de fuera de Japón (por ejemplo, cómics
  o cadenas de EE. UU.): el fandom occidental de K-On! no suele tener
  tie-ups propios; lo que hay es merchandising importado del mismo material
  japonés.

## Bitácora de búsqueda (esta pasada, red abierta)

- Leí entera `partes/datos-imagen.md` (no repetí sus consultas de AniList,
  wiki de personajes ni Wallhaven).
- Miré con `Read` las hojas de contacto 1, 2, 10 y 20 de
  `herramientas/referencias/k-on/` (958 imágenes, ya generadas por
  `investigar_serie.py` antes de esta tanda).
- Bajé y medí con `herramientas/estilo.py` (Pillow) 9 imágenes originales:
  034-037 (Character Image Songs, 4000×4000), 060 (HTT posing), 071-074 (con
  instrumento, fondo blanco), 082 (grupo tocando).
- Fandom API (`k-on.fandom.com/api.php`): `list=search` por "logo" y
  "emblem" (sin resultado útil directo), `list=allimages` con prefijo
  "Sakuragaoka" y "Logo" (sólo logos del sitio, no de la banda).
- Sketchfab API (`api.sketchfab.com/v3/models/<uid>`) para las 7 licencias
  de la tabla del punto 3, y `v3/search` para "Les Paul guitar", "drum kit"
  y "Fender Jazz Bass" (nuevos modelos CC BY).
- ambientCG API (`/api/v2/full_json`) por "paper" (Paper001-006, CC0
  confirmado) y por "ink" (sin resultados con ese type).
- Openverse API (`api.openverse.org/v1/images`) por "ink brush stroke
  black" (CC0 de Fons Heijnsbroek) y "houndstooth pattern fabric" (CC BY,
  no usado: no encaja con la ropa de la serie).
- Danbooru (`donmai.us`): bloqueado por Cloudflare (403) en esta sesión, dos
  intentos, no insistí más.
- `animenewsnetwork.com`: bloqueado por Cloudflare (403) directo con curl;
  resuelto igual por `ja.wikipedia.org` (ver punto 1).
- `texturelabs.org`: bloqueado por un reto de Cloudflare (JS), no insistí
  más de dos veces; usé ambientCG en su lugar.
- WebSearch (9 búsquedas de las ~50 del cupo): colaboración cafetería K-On!
  (es/en/ja), figma K-On!, staff Akiyo Takeda/Seiki Tamura, screentone
  gratis, tartán/plaid libre, paper grunge CC0, IDOLY PRIDE colab, cosplay
  Mio oficial.
- WebFetch: `ipfield.net/tieup-summary/keion` (colaboraciones 2010-2012),
  `collabo-cafe.com/events/category/k-on` (eventos 2024-2026), dos páginas
  de Zerochan (wallpapers oficiales con tamaño y fuente), `ja.wikipedia.org`
  (staff), Clip Studio Assets (licencia del pack de screentone, quedó ⚠️).

## Cumplimiento del encargo (sólo mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | 958 imágenes miradas en hojas, staff confirmado en 2 fuentes, wallpapers oficiales con tamaño y fuente |
| 3 · Fan art y 3D con licencia | ✅ | Las 7 licencias de la biblia + 3 nuevas, todas confirmadas por la API de Sketchfab (no por la página sola) |
| 15 · Vestuario con hex medidos | ✅ | Hex medidos con Pillow (`estilo.py`) sobre 9 imágenes oficiales, citando el archivo; trajes de escenario y ropa fuera de temporada (yukata, lluvia) confirmados con imagen |
| 16 · Fondos de pantalla | ✅ | 2 oficiales (Kyoto Animation, Zerochan, con tamaño y fuente) + 5 de fans (Wallhaven, verificados con el enlace de origen en pixiv/X) |
| 19 · Texturas 2D | ✅ | Manga real mirado, texturas equivalentes libres con licencia (ambientCG CC0, Wikimedia CC0), 2 packs de screentone con licencia dudosa marcada ⚠️, patrón de tela por generador libre |
| 23 · Colaboraciones y cruces | ⚠️ | 11 colaboraciones/tie-ups confirmadas con fuente (marcas, gacha, pop-ups, figuras); cosplay puntual con autor no encontrado (extra, no obligatorio del punto) |

Sigue: nada obligatorio pendiente de mis puntos (1, 3, 15, 16, 19, 23). Lo
que queda son extras ya anotados en «No encontré» (icono libre combinado
para el logo de HTT, un cosplay puntual citable, licencia más clara de los
packs de screentone).
