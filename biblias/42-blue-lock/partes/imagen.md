# Imagen · Blue Lock (encargo 42)

Investigador de imagen: puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md. Parte de
`partes/datos-imagen.md` (recolectado por `recolectar.py` el 24-sep-2026);
no repite esas consultas, sólo las comprueba y completa lo que faltaba.

## Hallazgos

### 1 · Arte oficial, en cantidad y variado

- Portada/banner oficial de AniList (anime, temporada 2): https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx137822-U8naszP96vzC.png · banner: https://s4.anilist.co/file/anilistcdn/media/anime/banner/137822-oevspckMGLuY.jpg · ✅ (AniList + wiki usan el mismo arte de temporada) · 1000×1500 aprox (cover "large")
- Key visual principal del anime (grupo completo, tono nocturno morado/azul): https://static.wikia.nocookie.net/bluelock/images/6/6d/Blue_Lock_TV_Anime_Key_Visual.png · 2600×1962 · ✅ (wiki + repetido en AniList/MAL) · paleta medida con `estilo.py`: #10060D 41%, #100E3F 25%, #202C99 11%, #A65C88 8%, #DFC3D6 8% — sombreado degradado/pintado, saturación 61%, brillo 32%
- Key visual 2ª temporada (grupal, día): https://static.wikia.nocookie.net/bluelock/images/8/8a/Seishiro_Nagi_S2_anime_design.png (hoja `arte_01.jpg` nº 60) y "Blue Lock TV Anime 2nd Cour Key Visual" (hoja nº110) · ⚠️ (una fuente, tamaño no medido a mano)
- Portadas de tomo (JP Volume 1, 2, 5, 6, ×18/19/23 "skill parameter"): listadas en `datos-imagen.md` con tamaño real (ej. JP Volume 5: 1364×2048) · ✅ (wiki, tamaño de la API `imageinfo`)
- **Artbook oficial**: «ブルーロック キャラクターブック EGOIST BIBLE» (Kodansha, supervisado por Muneyuki Kaneshiro y Yusuke Nomura), vol. 1 17-oct-2022, vol. 2 centrado en el Japón U-20; trae perfiles inéditos, ranking «BEST 3», entrevista a los autores y el guion/nombre inicial del capítulo 1 · portada vol.1 en la hoja `colaboraciones_01.jpg` nº676 · ✅ (hanmoto.com/bookwalker.jp + portada en la wiki)
- **Videojuegos oficiales** (para arte y capturas, más allá del punto 11 que es de texto): «ブルーロック Project: World Champion» (móvil, Rudel Inc., +17 millones de descargas a su 3er aniversario, https://bluelock-pwc.com/) y «ブルーロック BLAZE BATTLE» (móvil, 3D, bael Inc.) · ✅ (Google Play + App Store + web oficial)
- Captura de **REMATCH: BLUE LOCK TRAINING PACK** (Steam, app 4868930): cabecera https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4868930/ebfe1df66d4e009451d9e0a2d7118fefee6b951f/header.jpg · captura 1920×1080: https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4868930/b89d62480d3e067a1ebe6f4cac11191684c395de/ss_b89d62480d3e067a1ebe6f4cac11191684c395de.1920x1080.jpg · ✅ (Steam API `appdetails` + anuncio de Sloclap, ver punto 23)
- **Live-action (Toho, estrenada 7-ago-2026 en Japón, coincidiendo con el Mundial)**: teaser visual oficial 2895×4096 https://static.wikia.nocookie.net/bluelock/images/7/7e/Blue_Lock_LA_Movie_Teaser_Visual.png y key visual 475×676 https://static.wikia.nocookie.net/bluelock/images/2/23/Blue_Lock_LA_Movie_Key_Visual.png; fotos de rodaje (BTS) de Isagi, Nagi, Bachira+Isagi: https://static.wikia.nocookie.net/bluelock/images/a/a9/Blue_Lock_LA_Movie_BTS_Isagi.png (952×634), https://static.wikia.nocookie.net/bluelock/images/e/ee/Blue_Lock_LA_Movie_BTS_Nagi.png (949×628), https://static.wikia.nocookie.net/bluelock/images/f/f8/Blue_Lock_LA_Movie_BTS_Bachira_Isagi.png (1920×1280) · ✅ (wiki + Variety/IMDb/Anime Corner) · ⚠️ para la lámina: es imagen real (fotografía), no arte 2D; sirve sólo como referencia de pose/vestuario real, nunca de estilo de dibujo
- Hojas de contacto con el resto (21/16/17/14 imágenes por personaje, key visuals de capítulo, portadas de revista Shonen Magazine): ver `hojas/arte_01.jpg` (modelos, portadas, viñetas b/n) — mirada y elegida, detalle en «Hojas de contacto» más abajo.
- Fan art más votado por personaje en Safebooru (Isagi, Bachira, Nagi confirmados con más de 900 imágenes cada uno en el recolector; Rin Itoshi faltaba — corregido abajo en el punto 3) — se usa sólo como referencia de pose, nunca para pegar, según pide el encargo.

### 3 · Fan art y renders 3D como referencia (con licencia libre)

- Fan art mejor valorado (Safebooru, orden por puntuación) de Isagi, Bachira y Nagi: ya en `datos-imagen.md` (autor/origen enlazado a Twitter/Pixiv en cada fila) · ✅ (tamaño real de la API)
- **Rin Itoshi faltaba en la recolección** (el tag de Danbooru es `itoshi_rin`, no "rin_itoshi": por eso el recolector no lo encontró y trajo tags genéricos de Danbooru sin relación). Corregido a mano:
  - Related tags (Danbooru, vocabulario IA): male_focus, short_hair, multiple_boys, black_hair, blue_eyes(sic, es verde/turquesa en color oficial), green_hair, aqua_eyes, soccer_uniform, sportswear, simple_background · ✅ (danbooru.donmai.us/related_tag.json)
  - Top fan art por puntuación (Safebooru, `itoshi_rin sort:score`): 3869×1900 https://safebooru.org/images/518/5789af77f608310ae275a103191b3d2f83b8a50e.jpg (origen Pixiv 124812082_p14) · 3300×3200 https://safebooru.org/images/518/00d3c0e2f1b85c37bbdb2bed9fecacd5acd1a1ba.jpg (origen Pixiv 109546107_p0) · 2376×4096 https://safebooru.org/images/517/ab6517ef96e68b99974a4747db69b069a66ad4c4.jpg (origen https://twitter.com/Eunhaha02/status/1874508749509136548) · ✅ (tamaño real de la API)
- **Modelos 3D con licencia libre (Sketchfab, todos descargables)**:
  - «NAGI BLUE LOCK FREE FIRE 2 STYLES» · rocklee.ff · CC Attribution · https://sketchfab.com/3d-models/none-0ea7bbb0771648a0aca45891bbd2b007 ✅
  - «ISAGI BLUE LOCK FREE FIRE 2 STYLES» · rocklee.ff · CC Attribution · https://sketchfab.com/3d-models/none-12d7ed39e8d54d5c8058fe2110f40315 ✅
  - «Seishiro Nagi - Official Blue Lock Model» · Yume Kurohime · CC Attribution · https://sketchfab.com/3d-models/none-12a92d5b590a498996fd2fd4dd37d34b ⚠️ (una fuente; el nombre sugiere ser un port del modelo del juego oficial, no confirmado con el estudio)
  - «Gun Cabinet» (prop libre) · Brandon Westlake · gratis · https://sketchfab.com/3d-models/none-27dd41060e8b4c9dae8590b0f47cf855 — no es de la serie, se descarta para la lámina
  - «Blue Lock Soccer Ball» · Sivo · CC Attribution · https://sketchfab.com/3d-models/none-84306d1b03464943b609f9af1b3624f4 ✅ — balón genérico con logo pintado a mano, sirve como base low-poly
  - Balones genéricos alternativos (por si el de arriba no sirve): «Soccer Ball» varios autores, CC Attribution, ej. https://sketchfab.com/3d-models/none-46c91864ef384158b0078e20bdbfe3e9 · ✅ (búsqueda propia en la API de Sketchfab, `q=soccer ball&downloadable=true`)
  - «Rusty Metal Gate» (escaneado) · Blue Scans · CC Attribution · https://sketchfab.com/3d-models/none-a1fd9cbf3b64403e9e402ca429edd724 — prop de ambiente genérico (verja), no del Blue Lock real; usar sólo si se necesita una verja metálica cualquiera
- **Modelos 3D de la instalación Blue Lock** (fan-made, con licencia libre): «Blue Lock training Stadium» · dey.rudransh · CC Attribution · https://sketchfab.com/3d-models/none-2537204b334d4af8a5bcc409115b60ea · «Blue Lock Training Facility» · optimusprime7 · CC Attribution · https://sketchfab.com/3d-models/none-f8225941e44e4d9090b2a6c14db95031 · ✅ (búsqueda propia en la API de Sketchfab) · ⚠️ son reconstrucciones de fans, no el asset oficial del videojuego: comprobar en el visor 3D si el hexágono coincide con el plano oficial (punto 16) antes de usarlas como base.
- Poly Haven no tiene modelos de esta franquicia (es un banco de fotogrametría/HDRI genérico): sólo sirve para texturas reales (ver puntos 16 y 19).

### 15 · Vestuario: trajes, colores medidos, accesorios, peinado

**Traje icónico que todos reconocen**: el mono (bodysuit) negro con rayas del
equipo emitido por Blue Lock + chándal a juego. Es igual de corte para los 300
jugadores; cambia el color de la raya por equipo. Confirmado en el texto de la
wiki (Appearance de cada personaje, ya citado en `datos-imagen.md`) y medido a
ojo en cada imagen oficial:

- **Yoichi Isagi**: bodysuit negro con **rayas azules**. Hex medido con
  `estilo.py` sobre "Yoichi Isagi uniform anime design.png" (modelo oficial
  1500×2142, https://static.wikia.nocookie.net/bluelock/images/f/f3/Yoichi_Isagi_uniform_anime_design.png):
  negro #020202 (27%), azul raya #5875C9 (23%), azul oscuro #333A54 (18%), piel
  #F7E2C8 · ✅ (medido en la imagen oficial + confirmado por el texto "black
  with blue stripes" de la wiki)
- **Meguru Bachira**: bodysuit negro con rayas gris-azuladas. Hex medido sobre
  su modelo (1500×2142): negro #030303 (27%), azul grisáceo #5A75C8 (20%), azul
  marino #363C53 (15%), piel #EEDABF · ✅
- **Seishiro Nagi**: bodysuit negro con rayas gris. Hex medido sobre su modelo
  (2138×3055): gris azulado #33353A (33%), negro #010102 (28%), gris claro
  #5E5E75 (3%) — el tono es más desaturado que el de Isagi/Bachira (7% de
  saturación medida vs 19-20%) · ✅
- **Rin Itoshi**: bodysuit negro con rayas gris. Hex medido sobre "Rin Itoshi
  suit anime design.png" (2250×3213, ojo: este archivo es en realidad el
  **traje formal** de gala, no el bodysuit — ver abajo): azul marino #32374F
  (36%), blanco #FEFDFC (31%, fondo), negro #000000 (26%) · ⚠️ (falta medir el
  bodysuit puro de Rin sobre una imagen sin fondo blanco; el texto de la wiki
  confirma "black with gray stripes" igual que Bachira/Nagi)
- **Traje formal/promocional** (el "suit anime design" que aparece en medio
  tomo de key visuals, hoja `arte_01.jpg` nº5-8): blazer/abrigo oscuro con
  cuello alto, usado en pósters y portadas — **no es un uniforme de partido**,
  es ropa de calle elegante para material promocional. Confirmado visualmente
  en la hoja y en el key visual de Nagi ("Blue Lock- Episode Nagi - Key
  Visuals.jpg", 1912×4260) · ✅
- **Uniformes por selección/torneo** (uno de los datos que más pide el
  encargo: "sus trajes por temporada o arco"):
  - Ichinan High School (antes de Blue Lock, sólo Isagi): blazer desabrochado
    sobre camiseta blanca, corbata de rayas · ⚠️ (una fuente, texto de la
    wiki, sin imagen medida)
  - Namikaze High (antes de Blue Lock, sólo Bachira): camiseta #8 con diseño
    de ave al centro · ⚠️ (texto de la wiki)
  - Primera Selección: Equipo Z nº11 azul (Isagi), nº8 azul (Bachira); Equipo
    V nº11 (Nagi); tacos con gorra gris para Z · ✅ (texto + hoja nº34-40,
    "S2 anime design" numerados 16, 8, 1, 10, 7, 15 según personaje/arco)
  - Segunda Selección: Equipo Blanco → luego rojo (todos); Rin: Equipo Rojo
    nº1 · ✅ (texto de la wiki + hoja nº35 "Rin Itoshi S2 anime design 2")
  - Tercera Selección: Equipo A negro (Isagi nº15, Rin nº1), Equipo C blanco y
    azul (Bachira nº7) · ✅ (texto de la wiki)
  - Japón U-20: uniforme azul oficial; Rin es capitán con brazalete (nº10),
    Isagi nº11 · ✅ (texto + hoja nº33 "Yoichi Isagi Blue Lock x Liverpool",
    nº106 "Blue Lock Seishiro Nagi Key Visual" con el uniforme verde de Japón
    alterno)
  - Neo Egoist League (clubes reales de fantasía): Rin ficha por **Paris X
    Gen** (uniforme rojo/burdeos), Nagi y Reo por **Manshine City** (azul
    claro, parodia de Manchester City) · ✅ (hoja `colaboraciones_01.jpg`
    nº678 "Paris x Gen vs Manshine City"; nombres confirmados en la wiki:
    páginas "Manshine City", "France U-20", "FC Barcha" —parodias con
    licencia narrativa de clubes reales, no colaboraciones de marca)
- **Peinado y rasgos fijos** (no cambian con el uniforme, van para la guía de
  IA del punto 17): Isagi pelo azul-negro corto con flequillo en V y un ahoge
  con forma de brote de planta; Bachira pelo castaño con reflejos dorados
  hasta la barbilla, ojos amarillos; Nagi pelo blanco medio largo con flequillo
  en V, ojos gris con iris grande; Rin pelo verde oscuro con flequillo que
  tapa el ojo derecho, ojos verde azulado, mismas pestañas marcadas que su
  hermano Sae · ✅ (texto "Appearance" de las 4 fichas, ya en `datos-imagen.md`)

### 16 · Ciudades, paisajes y fondos de pantalla

**La serie casi no sale del edificio Blue Lock**: no hay "ciudades" variadas
como en otros animes; el sitio icónico es la instalación en sí (más los
estadios de los partidos). Se investigó a fondo el único gran "lugar":

- **Estructura oficial** (texto de la ficha "Blue Lock" de la wiki, la
  instalación es la que da nombre a la serie): edificio-acantilado con forma
  de pentágono, 5 estratos (uno por cada equipo de la letra V a Z), cada
  estrato con canteen central, cuartos, sala de pesas, campos de entrenamiento
  y un campo de exhibición al centro. Plano oficial de fin de tomo, "A Guide
  to Blue Lock's Facilities": https://static.wikia.nocookie.net/bluelock/images/9/97/Blue_Lock_facility.png/revision/latest?cb=20191126111655
  (2140×1600, diagrama en blanco y negro, sin color que medir pero con **la
  distribución exacta** para construir la maqueta en Blender: planta 1F con
  vestuarios/dormitorio/sala de datos, 2F-3F con el campo de entrenamiento) ·
  ✅ (wikitext de la página + imagen del propio manga)
- **Exterior del edificio** (captura oficial del anime, usada como imagen de
  ficha en la wiki): https://static.wikia.nocookie.net/bluelock/images/3/3b/Blue_Lock_%28Anime%29.png
  (3584×2009). Es de día, cielo despejado con nubes, el edificio es un
  prisma azul oscuro con el logo "BLUE LOCK" en un panel negro y la insignia
  de diamante verde. Paleta medida con `estilo.py`: azul marino #182951 (26%),
  celeste #ACCFE1 (26%, cielo), azul acero #405764 (21%), azul intenso #274893
  (10%), casi blanco #DDEEF4 (10%) — sombreado degradado/pintado, saturación
  42%, brillo 59% · ✅ (imagen de la wiki, coincide con el color de logo de
  Openverse citado abajo)
- **Textura real equivalente** para el revestimiento del edificio (paneles
  metálicos azules): `Metal063` y `CorrugatedSteel009` de ambientCG, licencia
  **CC0** (dominio público, sin atribución obligatoria): https://ambientcg.com/view?id=Metal063
  y https://ambientcg.com/view?id=CorrugatedSteel009 · ✅ (ambientCG es CC0 en
  todo su catálogo, comprobado en su web)
- **Campo de juego** (césped bajo focos, de noche o cerrado): equivalente real
  `Grass005`/`Grass001` (CC0, ambientCG) para el pasto, y focos/luz de estadio
  se ve en las capturas de la hoja `fondos_01.jpg` (nº149, 152, 158: campo
  verde con líneas blancas, cielo artificial de nave cerrada) · ✅
- **Fondos de pantalla oficiales/fans en alta** (Wallhaven, filtrado por
  "Blue Lock" en vez de la búsqueda genérica del recolector, que traía ruido
  de otras series):
  - 3840×2160 · ♥17 · https://w.wallhaven.cc/full/gp/wallhaven-gppoj7.jpg · subido por orsted2222 · origen oficial: https://bluelock-pr.com/ (rueda de prensa oficial) · ✅
  - 2732×1536 · ♥5-8 (varias resoluciones del mismo art) · ilustración conceptual "ojo de Isagi reflejando el campo", con marca de agua de un PV oficial (origen: youtu.be/d6MrgyOio-E) · vista y confirmada: es arte gráfico estilizado, tono nocturno azul/magenta · ⚠️ (no se pudo confirmar el nombre del ilustrador)
  - 2422×1440 · ♥14 · https://w.wallhaven.cc/full/ml/wallhaven-mlqp88.jpg · Michael Kaiser con smartphone y toalla (backstage/día a día del personaje) · ⚠️ (una fuente)
  - 4800×2400 · ♥22 · https://w.wallhaven.cc/full/qr/wallhaven-qrrzdl.jpg · viñeta de manga de Nagi a color, motion blur · ✅
  - El resto de fondos altos ya está en `datos-imagen.md` (15 más, con favoritos y autor de subida)
- **Hora del día / luz por arco**: instalación Blue Lock = interiores con luz
  fría artificial (fluorescente blanca en dormitorios, azul en pasillos según
  el logo del edificio); los partidos de selección son de día con luz natural
  dura (sombras marcadas); el Mundial U-20 y Neo Egoist League usan estadios
  nocturnos con reflectores (contraluz muy marcado, cielo casi negro) — visto
  en las capturas de la hoja `fondos_01.jpg` (comparar nº145 día vs nº168
  noche) · ✅ (comprobado a ojo en la hoja, mirada con Read)

### 19 · Texturas 2D (tramas, grano, patrones, emblemas)

- **Logo oficial "Blue Lock"** (el diamante verde con cadena): visible en alta
  definición en la fachada del edificio (captura de arriba) y suelto en
  Openverse/Wikimedia: 1776×435 · CC BY-SA 4.0 · PatoAnidae02 ·
  https://upload.wikimedia.org/wikipedia/commons/3/35/Blue_Lock_Logo_Japan.png
  · ✅ (Wikimedia Commons + visible en el edificio del anime)
- **Tramas de manga (screentones)**: el manga usa trama de puntos clásica para
  sombras y fondos de emoción (ver hoja `arte_01.jpg` nº17-20, retratos en
  blanco y negro con textura de puntos en el pelo) y líneas de velocidad muy
  marcadas en las jugadas ("GOOOAL!!!", hoja nº30-31, nº52-56) · ✅ (mirado en
  la hoja)
- **Equivalente libre de screentone/trama de manga**: colección gratuita
  "Free Screen Tone Collection 1" (manga-with-stef.com/free-screen-tone-collection-1),
  imágenes de trama de 4500×4500 px pensadas para Krita/Procreate a tamaño de
  página completa; también "Halftone Brushes" en Brusheezy
  (brusheezy.com/brushes/50379-mabecman-s-screentones-halftone-brushes, 34
  pinceles) · ⚠️ (existen y son gratis, comprobado que la página carga, pero
  **no se pudo confirmar el texto exacto de la licencia** de ninguna de las
  dos — revisar los términos de uso antes de usarlas en un encargo)
- **Grano de papel/impresión** (para que la lámina no se vea "digital
  perfecta"): equivalente real `Paper001` de ambientCG, CC0:
  https://ambientcg.com/view?id=Paper001 · ✅
- **Patrón de tela del uniforme** (malla técnica de poliéster de las
  camisetas de fútbol): equivalente real `Fabric081C`/`Fabric066` de
  ambientCG, CC0 · ✅
- **Textura de balón** (cuero/PU con costuras): equivalente real `Leather037`
  o `Leather026` de ambientCG, CC0, para la base antes de pintar el patrón de
  pentágonos · ✅. El modelo 3D de balón con el patrón ya pintado está en el
  punto 3 (Sketchfab, CC Attribution)
- **Emblemas de equipo dentro de la ficción** (parodias de clubes reales,
  útiles como "logos de grupo" del punto 25): Manshine City (azul, parodia de
  Manchester City), Paris X Gen (parodia de PSG), FC Barcha (parodia de
  Barcelona), Ubers, Arsenaly — todos en páginas propias de la wiki
  (`bluelock.fandom.com/wiki/Manshine_City`, etc.) pero **sin archivo de
  escudo subido** en la wiki en inglés a la fecha de esta consulta · ⚠️ (se
  buscó `list=allimages` con prefijo "Manshine"/"Team" y no aparecieron
  escudos sueltos; si hacen falta, se recortan de las viñetas de la hoja
  `colaboraciones_01.jpg` nº678)

### 23 · Colaboraciones y cruces

- **REMATCH × Blue Lock** (colaboración muy reciente y de peso: empezó el
  **24-sep-2026**, un día antes de esta investigación): el juego multijugador
  de fútbol "REMATCH" (Sloclap/IDC Games) sacó la "BLUE LOCK TRAINING PACK" en
  Steam (app 4868930) con uniforme, carta de jugador y una animación de
  victoria; la Temporada 5 de Rematch trae a Isagi, Bachira, Nagi y Rin (los
  4 personajes de este encargo) y un modo nuevo "Aura Striker" inspirado en el
  Ego del manga · fuentes: https://store.steampowered.com/app/4868930/REMATCH_BLUE_LOCK_TRAINING_PACK/
  · https://www.gematsu.com/2026/09/rematch-x-blue-lock-collaboration-announced
  · https://www.playrematch.com/post/what-you-need-to-know-before-rematch-x-blue-lock
  · ✅ (Steam + Gematsu + el blog oficial de Rematch, tres fuentes)
- **eFootball 2024 × Blue Lock** (Konami, 21-mar-2024 a 11-abr-2024): cartas y
  avatares de personajes, camisetas "Team White" y "Team Red" jugables en
  cualquier plantilla, fichajes gratis de jugadores reales tematizados ·
  https://www.konami.com/games/eu/en/topics/17812/ · https://www.cbr.com/blue-lock-anime-efootball-pes-video-game-release/
  · ✅ (web oficial de Konami + CBR)
- **Blue Lock × Sanrio Characters** (pop-up shop, 20-ene a 26-feb-2023):
  peluches con llavero mezclando cada jugador con un personaje de Sanrio
  (Hello Kitty, Cinnamoroll, Pompompurin, entre otros); explica por qué el
  recolector automático encontró esos personajes como "relacionados" en
  Danbooru — no es un error, son fan art reales de la colaboración · portada
  del evento en la hoja `colaboraciones_01.jpg` nº680 ("Sanrio Collab
  Promotion") · ✅ (sanriowiki.com + goodsrepublic.com + hoja propia)
- **Blue Lock × Treevillage Cafe** y **Blue Lock × JR Central (Japan
  Railway)**: cafetería temática y colaboración con trenes, carteles oficiales
  en la hoja `colaboraciones_01.jpg` nº673 y nº674 · ⚠️ (una sola fuente: la
  propia wiki; no se confirmó fecha ni ciudad exacta por falta de tiempo de
  búsqueda)
- **Pop-up "Surf Style"** (ropa de verano con estampado de tabla de surf):
  cartel en la hoja `colaboraciones_01.jpg` nº675 · ⚠️ (una fuente, wiki)
- **Ado (cantante) × Blue Lock (película live-action)**: Ado canta el tema
  "Monstruo" (con Giga y TeddyLoid, letra de ryo de Supercell) para la
  película live-action que se estrenó el 7-ago-2026 en Japón · ✅
  (animecorner.me + animenewsnetwork.com + otomo.net, tres fuentes) — esto
  también explica el tag "chando" (el personaje/mascota ilustrada con la que
  Ado se presenta sin mostrar la cara) que aparecía mezclado en los datos de
  Danbooru
- **Ojo, esto NO es una colaboración real**: Umamusume × Blue Lock no existe
  como colaboración oficial (comprobado con búsqueda propia); todo lo que
  aparece mezclado (personajes como "Agnes Tachyon" o "T.M. Opera O" en los
  datos de Danbooru/Safebooru del recolector) es **fan art independiente**,
  coincidencia de tags populares en Danbooru, no crossover licenciado. No usar
  para la lámina como si fuera oficial.
- **Figuras oficiales** (referencia de pose 3D real): Nendoroid Isagi Yoichi
  (nº1998, Good Smile Company/Orange Rouge, con caras intercambiables) y
  Nendoroid Meguru Bachira (con balón y una piña como accesorios, guiño a su
  personalidad) · https://www.goodsmile.com/en/product/60957 (Bachira) ·
  amiami.com/eng/detail/?gcode=FIGURE-167214 (Isagi) · ✅ (Good Smile + AmiAmi,
  dos fuentes) · ⚠️ no se encontró Nendoroid oficial de Nagi ni de Rin a la
  fecha de esta búsqueda (puede que aún no exista, o que se venda sólo en
  prize figures de bandai/Union Creative — no confirmado, falta buscar más)
- **Cosplay real** (materiales y volumen, no ilustración): cosplayer de
  Meguru Bachira en el evento "Destination Tokyo 2024" (peluca bicolor
  azul/verde real, camiseta blanca #2 con número rosa, balón de utilería) ·
  1024×1024 · CC BY 2.0 · Isabelle + Stéphane Gallay ·
  https://live.staticflickr.com/65535/54161951673_8864c634a1_b.jpg · ✅
  (Openverse/Flickr, imagen mirada y confirmada con Read) — es la única foto
  de cosplay con licencia libre que se encontró; el resto de "Blue Lock
  cosplay" en Openverse son resultados de hardware real (candados azules), no
  de la serie

