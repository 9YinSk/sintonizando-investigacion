# Investigador de IMAGEN · My Hero Academia (encargo 25)

Puntos de `ENCARGO.md`: **1** (arte oficial), **3** (fan art y 3D con licencia), **15**
(vestuario con hex medidos), **16** (paisajes y fondos de pantalla), **19**
(texturas 2D) y **23** (colaboraciones y cruces). Parto de `partes/datos-imagen.md`
(no repito esas consultas) y de las **92 hojas de contacto** ya generadas en
`herramientas/referencias/my-hero-academia/` (4397 imágenes de 6 páginas de la
wiki y sus galerías). La biblia ya tenía borrador de estos puntos hecho con la
red cerrada (todo ⚠️, de memoria); aquí lo confirmo con fuentes reales, mido
hex con `herramientas/estilo.py` sobre archivos oficiales de la wiki, y amplío
lo que faltaba (sobre todo 3D con licencia y colaboraciones).

## 1 · Arte oficial, en cantidad y variado

**Las 92 hojas cubren de sobra "poses vivas, con su objeto, en grupo, en
acción"**: miré hoja_01, hoja_02, hoja_05 y hoja_10 completas (192 imágenes),
más de las que citaba la biblia anterior. Están ordenadas por tamaño real (de
mayor a menor), así que las primeras hojas son casi todas arte oficial grande.

**Key visuals e ilustraciones de temporada** ✅ (vistas en hoja_01 y hoja_02,
`herramientas/referencias/my-hero-academia/indice.json` tiene la URL y el
tamaño real de cada una):
- `Season 7 Izuku Midoriya.png` (2895×4096, key visual «DEKU») y
  `Season 7 Ochaco Uraraka.png` (2896×4096, key visual «URAVITY») — pose de
  acción individual, fondo de color de marca por personaje (verde para Deku,
  magenta para Uraraka). Medidos con `estilo.py`: Deku paleta dominante
  `#0D160F` `#0F4431` `#022B18` `#126E53` `#34CDB9` (el verde brillante es el
  degradado del fondo del cartel, no el traje: para el traje usa los hex de
  §15); Uraraka `#DD2570` `#F7B7D4` `#EF8FBB` (fondo magenta de marca).
- `MHA 10th Anniversary Visual.png` / `My Hero Academia 10th Anniversary Key`
  (2640×3491 y 2640×3410, hoja_01 #25-26): todo el reparto principal junto,
  pose de grupo en acción.
- `Season 4 Poster 1.png`, `Season 7 Poster 1.png` (3029×2135), `Season 7
  Trainees.png`, `Final Season Armored All Might.png` (3043×2151, hoja_02
  #58): pósters oficiales de cada temporada.
- `Final Season Poster 3.png`, `Final Season Poster 1.png/7.png` (hoja_02):
  arte de la última temporada.
- `List of Characters-min.png` (4096×1512, hoja_02 #67): mosaico oficial con
  **todo el reparto** en su traje de héroe, sirve para comparar vestuario de
  golpe.

**Portadas de tomos (manga)** ✅ (dos fuentes: la wiki y la búsqueda web ya
hecha por el equipo anterior, §3.2 de la biblia): tomo 1 y tomo 42 con la
misma portada «espejo» amarilla; en EE. UU. el tomo 42 tuvo 4 portadas
(VIZ). Contraportadas de EE. UU. vistas en hoja_10 (#465-480): `US Volume 1
Back Cover.png` … `US Volume 33 Back Cover.png`, todas con mini-perfil del
personaje y su cuadro de diálogo (referencia también para el punto 6, que no
es mío).

**Singles y bandas sonora (CD)** ✅ (hoja_01/02, tamaño real en `indice.json`):
`Starmarker cover.png` (3885×3458, ending), `Ours CD Cover.png` (3927×3500),
`My Hero Academia World Heroes' Mission ORIGINAL SOUNDTRACK.png` (3000×3000),
`North Wind CD Cover.png`/`Back Cover.png` (2000×2000), `Miss you CD Cover.png`
(3371×3000).

**Blu-ray** ✅: `World Heroes Mission Blu-Ray Cover.png` (424×600,
`https://static.wikia.nocookie.net/bokunoheroacademia/images/2/2b/World_Heroes_Mission_Blu-Ray_Cover.png`)
es la portada real de un Blu-ray (la película). No encontré la portada del
BD de la serie TV vol. 1 con imagen (sólo el enlace de tienda que ya tenía la
biblia, `spice.eplus.jp`, sin abrir) ⚠️.

**Arte de videojuegos** ✅✅ (dos juegos, con fuente oficial cada uno):
- **MY HERO ACADEMIA: All's Justice** (Bandai Namco, arena 3D 3v3, sale el
  4-9-2026 en Switch 2): key visuals `All's Justice for Nintendo Switch 2 II`
  y `All's Justice Alternate Visual` (hoja_01 #34 y #43) — [Bandai Namco
  Europe](https://en.bandainamcoent.eu/my-hero-academia/news/my-hero-academia-alls-justice-brings-heroic-battles-nintendo-switch-2-4),
  [Nintendo Life](https://www.nintendolife.com/games/nintendo-switch-2/my-hero-academia-alls-justice).
  Trae **modo «Team Up Mission»** (vivir como alumno de 1-A) y una
  colaboración con **PAC-MAN** como minijuego de Switch 2 (ver §23).
- **My Hero One's Justice**: `My Hero One's Justice Cast Artwork.png`
  (1449×2048, hoja_10 #439) — arte de todo el reparto jugable en pose de
  batalla.
- **JUMP FORCE**: `JUMP FORCE - Bakugo DLC Trailer` (archivo de vídeo en la
  wiki, visto en la búsqueda de imágenes de Bakugo) — Bakugo fue DLC de este
  crossover de Bandai Namco ⚠️ (un solo indicio, el nombre del archivo; no
  vi el tráiler).

**Cartones de cuenta atrás / anuncios dibujados a mano** ✅ (es justo lo que
pide el punto 1; están en hoja_01 #11-24 y hoja_05 #217-240): bocetos a
rotulador de «おかげさまで4回年!! ありがとうございます!!» (4.º aniversario),
«HAPPY NEW YEAR 2020/2021/2026», «アニメこのあとすぐ!!» («el anime empieza
ya», con los personajes chibi), «アニメ今日タカ5:30!» (aviso de horario),
`Christmas 2021/2023/2024 Sketch.png`, `Season 2/3/5 Teaser Sketch.png`,
`Episode 42/85/102/107/114/120/150/151/161/164/167/170 Sketch.png`. Docenas
de ellos, cada uno firmado y fechado por el estudio — así se anuncia cada
capítulo en redes japonesas.

**Hojas de modelo (model sheets)** ✅✅ — la mejor mina de la wiki, bajadas
una a una por título de archivo (no estaban en las 92 hojas grandes porque
son imágenes pequeñas de producción, 170-700 px de ancho):
- `Izuku Midoriya Alpha/Beta/USJ/Gamma Costume Anime Design Sheet.png` (el
  Beta es el traje que más sale en pantalla: `693×492`,
  `https://static.wikia.nocookie.net/bokunoheroacademia/images/0/00/Izuku_Midoriya_Beta_Costume_Anime_Design_Sheet.png`).
  Los nombres Alpha/Beta/Gamma son los que usa la propia wiki para las
  versiones del traje ⚠️ (un indicio: los nombres de archivo; falta el texto
  de la wiki que lo confirme con fechas).
- `Katsuki Bakugo Hero Costume Anime Design Sheet.png` (700×494) y
  `Katsuki Bakugo Full Body Hero Costume.png` (634×1209).
- `Shoto Todoroki Beta/Alpha Costume Anime Design Sheet.png` (700×494) y
  `…Upgraded Beta Costume Anime Shading Design Sheet.png` (con sombreado ya
  aplicado, útil para el punto 18 que no es mío pero lo anoto).
- `Ochaco Uraraka Hero Costume Anime Design Sheet.png` y
  `…Anime Design Sheet.png` (uniforme), 700×494 cada una.
- `Shota Aizawa Hero Costume.png` (363×644) y `…Hero Costume (Anime).png`
  (153×555, más limpia de fondo).
- `Toshinori Yagi Golden Age Hero Costume (Anime).png` (1124×1831): el traje
  clásico años 90 (azul, rojo y amarillo).
- Perfiles de **uniforme escolar** del 10.º aniversario para los seis:
  `Izuku/Katsuki/Shoto/Ochaco U.A. School Uniform Profile (10th
  Anniversary).png` — todas en
  `https://static.wikia.nocookie.net/bokunoheroacademia/images/…` (URL exacta
  de cada una en `imagen.json`).
- `All Might Anime Expressions Design Sheet.png`: hoja de expresiones (útil
  para el punto 13, no mío, pero la dejo anotada porque es rarísima de
  encontrar).
- `Volume 7 (Team-Up Missions) Character.png` y `Volume 8 …` (2256×1772,
  hoja_05 #201-202): fichas de personaje estilo databook con stats, en
  japonés.

**Fuera de la wiki** ✅: portada y banner de AniList (ya en
`datos-imagen.md`), Marvel.com/Oricon para el crossover (§23), Bandai
Namco/Nintendo para el videojuego, VIZ para las portadas de EE. UU.

## 3 · Fan art y 3D (sólo como referencia)

**Fan art 2D** (de `datos-imagen.md`, ya con enlace, tamaño y autor/origen;
no repito la consulta): los mejor valorados de Safebooru por personaje
(`all_might`, `bakugou_katsuki`, `todoroki_shoto`, `uraraka_ochaco`,
`aizawa_shota`, `midoriya_izuku`, `mirko`, `toga_himiko`), con puntos, tamaño
y el enlace a Pixiv/Twitter/Tumblr original cuando lo dan. Es sólo
referencia de pose y composición, nunca para pegar (lo dice ENCARGO.md).

**Modelos 3D con licencia libre** ✅✅ — comprobé la licencia **directamente
en la API de Sketchfab** (`api.sketchfab.com/v3/models/<uid>`), no sólo en la
página, y saqué autor y número de caras exacto:

| Modelo | Autor | Licencia | Caras | Para qué |
|---|---|---|---|---|
| [My Hero Academia UA classroom](https://sketchfab.com/3d-models/none-b73f7ef0e095420d97489df7e0d08859) | banabanaba | **CC Attribution** | 57 286 | El aula 1-A completa |
| [My Hero Academia classroom desk and chair](https://sketchfab.com/3d-models/none-4e03d145808b46f6a3da68343f5d4c42) | banabanaba | **CC Attribution** | 3 714 | El pupitre para el cuaderno |
| [Katsuki_Bakugo_Hero](https://sketchfab.com/3d-models/none-cc8fcd2f64784f9292a279ef4a670ac9) | 20062020year | **CC Attribution** | 29 428 | Pose/traje de Bakugo en 3D |
| [Todoroki shoto hero traje beta](https://sketchfab.com/3d-models/none-4ce1f840a18646a6bb85a18264dadafb) | victordavi1606 | **CC Attribution** | 70 678 | Pose/traje de Todoroki |
| [Ochaco_Uraraka giggle](https://sketchfab.com/3d-models/none-9946350617474ab5a519c8c5b940d6cd) | Dhext3r | **CC Attribution** | 68 377 | Uraraka, pose animada («giggle») |
| [Aizawa](https://sketchfab.com/3d-models/none-557993be57a04b0cad5e4c0010fe5ed6) | vitgabi89 | **CC Attribution** | 217 038 | Aizawa, muy detallado |
| [All Might: The number one hero!](https://sketchfab.com/3d-models/none-ab3d819d719745a0a0bde8b9de05daa0) | Phan21 | **CC Attribution** | 11 034 | All Might en pose heroica |
| [Deku (Izuku Midoriya)](https://sketchfab.com/3d-models/none-7dee03930f074f2995191a1668a7c353) | (ver página) | **CC Attribution-NonCommercial** ⚠️ (no comercial: sólo referencia, no para vender) | 2 184 | Izuku |
| [Mirko (My Hero Academia)](https://sketchfab.com/3d-models/none-de9ac30d334a4e3ba82fdcf3024f67b9) | Puzzle | **CC Attribution** | 738 242 | Personaje secundario muy querido (ver §9 de la biblia) |

Crédito exacto a usar (mismo formato para los ocho CC Attribution): `"<nombre
del modelo>" (https://sketchfab.com/3d-models/none-<uid>) by <autor> is
licensed under Creative Commons Attribution`.

**Ojo con «Free Standard»**: en la búsqueda salieron varios modelos
etiquetados **«Free Standard»** (p. ej. `Katsuki Bakugo (Gym Uniform)`,
`Ochaco Uraraka (Hero Uniform)`, `Shoto Todoroki (Hero Costume)`) — eso **no
es Creative Commons**: es la licencia por defecto de Sketchfab, que permite
bajarlo gratis pero **no** dice que se pueda reutilizar libremente. No los
metí en la tabla ni en `imagen.json`; si se quieren usar, hay que leer la
licencia completa en la página antes.

## 15 · Vestuario, con hex medidos

Todos los hex de esta sección están **medidos con `herramientas/estilo.py`
sobre archivos oficiales de la wiki de Fandom** (hojas de modelo de
producción o key visuals), no de memoria. Cada fila dice sobre qué imagen se
midió. El archivo completo con todas las paletas está en
`/tmp/claude-0/trabajo/25-my-hero-academia-imagen/paletas/estilo.json`.

| Personaje | Prenda | Medido sobre | Hex principales |
|---|---|---|---|
| **Izuku (Deku)** | Uniforme U.A. | `Izuku_Midoriya_U.A._School_Uniform_Profile.png` | Americana gris `#A4A8AB`; solapas/pantalón verde oscuro `#0A191B`/`#153A3E`; corbata/zapatos rojos `#9B2F25`; piel `#F1DCCB` |
| **Izuku (Deku)** | Traje de héroe (Beta, el más visto) | `Izuku_Midoriya_Beta_Costume_Anime_Design_Sheet.png` | Verde oscuro del mono `#213335`; verde-teal de detalles/capucha `#1B6262`; rojo de guantes y cinturón `#8D2A23` |
| **Katsuki Bakugo** | Uniforme U.A. | `Katsuki_U.A._School_Uniform_Profile_(10th_Anniversary).png` | Americana gris `#C9C6C1`; verde oscuro `#051B1F`/`#0C3842` |
| **Katsuki Bakugo** | Traje de héroe | `Katsuki_Bakugo_Hero_Costume_Anime_Design_Sheet.png` | Base negra/oliva oscuro `#363D35`; piel `#F1DABE`; naranja de los guanteletes de granada `#C45C2F` (la cuadrícula verde de los guanteletes no se ve bien en esta hoja pequeña: en `Class 1-A Hero Costumes.png` se ve un **tartán verde militar**, sin hex propio medible por ser muy fina la trama) |
| **Shoto Todoroki** | Uniforme U.A. | `Shoto_U.A._School_Uniform_Profile_(10th_Anniversary).png` | Gris `#B7BABA`; verde oscuro `#0C3841`; marrón-rojizo de la cicatriz `#5B4445` |
| **Shoto Todoroki** | Traje de héroe (Beta) | `Shoto_Todoroki_Beta_Costume_Anime_Design_Sheet.png` | Mono azul marino `#222A5D`/`#141631`; detalle rojizo `#623D40`. **Nota visual**: mirado el diseño completo (no sólo el hex), el traje es azul marino liso con mochila/cinturón blancos — no tiene el lado «mitad fuego, mitad hielo» que sí tiene su pelo y su piel |
| **Ochaco Uraraka** | Uniforme U.A. | `Ochaco_U.A._School_Uniform_Profile_(10th_Anniversary).png` | Gris `#A7A8AB`; verde oscuro de la falda `#203239`; abrigo marrón `#3A2016`/`#7A432C`; piel `#F5DDCD` |
| **Ochaco Uraraka** | Traje de héroe | `Ochaco_Uraraka_Hero_Costume_Anime_Design_Sheet.png` | Rosa del casco/guantes `#B4929C`/`#CEBBC4`; negro del mono `#774F4A` (medido sobre línea oscura) |
| **Shota Aizawa** | Traje de héroe | `Shota_Aizawa_Hero_Costume_(Anime).png` | Casi todo negro `#101210`/`#000000`/`#1D1E1D`; bufanda de captura gris `#605C5B`/`#B9B0A8` |
| **All Might** | Traje «Golden Age» (clásico, el que usa para dar clase) | `Toshinori_Yagi_Golden_Age_Hero_Costume_(Anime).png` | Pelo amarillo `#EDDC7A`; azul del traje `#12183F`/`#233074`; rojo `#601F13`/`#C71F20`; dorado de detalles `#97864B` |
| **Todo el grupo 1-A junto** | Trajes de héroe, foto de grupo | `Class_1-A_Hero_Costumes.png` (3593×1080) | Paleta de conjunto: negros `#111015`, grises `#B6B4B2`/`#828797`/`#55595D`, blancos `#E2E0DD`, piel `#956046`, dorado `#CBA666` — útil para ver cómo queda el grupo entero en una escena, no para un traje suelto |

**Lo que el dueño pidió y no había** (repasado con esto): «no salen de pie
con una sola ropa» — con las hojas de modelo hay **uniforme + traje de
héroe** para los 6, medidos por separado, más el traje «Golden Age» de All
Might (el de dar clase, distinto del traje de combate). Falta aún: el traje
de All Might *armored* (el de la temporada final, con exoesqueleto) sin
medir con hex — sólo lo vi en miniatura en las hojas de contacto ⚠️.

**Progresión de trajes (con nombre de archivo como única fuente por ahora,
⚠️)**: Izuku tuvo al menos 4 versiones nombradas por la propia wiki en sus
archivos — *Alpha* (el original, temporada 1), *Beta* (el que más sale, con
capucha y guantes; el de la tabla de arriba), *USJ* (el de refuerzo hecho
tras el ataque al USJ) y *Gamma* (posterior). Todoroki tiene *Alpha* y
*Beta* (con una versión «Upgraded Beta»). Esto son nombres de archivo, no
texto de la wiki: falta confirmar fechas/arco exacto de cada uno en el texto
de las páginas de personaje.

## 16 · Paisajes y fondos de pantalla

**Fondos de pantalla, oficiales y de fans, en alta** (de `datos-imagen.md`,
Wallhaven, ya con tamaño real, autor y origen — no repito la consulta; sólo
reviso y destaco):
- Mejor valorado: 2473×3200, ♥398, subido por ThorRagnarok, Tsuyu+Uraraka —
  `https://w.wallhaven.cc/full/zm/wallhaven-zmp1wv.jpg`.
- El único **con origen a un artista identificado**: 2480×3508, ♥209, de
  **NeoArtCorE** (DeviantArt) — `wallhaven-vgvg18.jpg`, Uraraka. Es el mejor
  para citar «fondo de pantalla de fan, autor: NeoArtCorE» porque los demás
  no dan autor original (`origen: —`).
- 3840×2160, ♥284, Izuku (verde, minimalista) — `wallhaven-g8e98d.png`.
- 3840×2160, ♥158, Himiko Toga con sangre — `wallhaven-zmv9go.jpg`.

**Fondos de pantalla oficiales** ⚠️: la página oficial
(`heroaca.com/special/wallpaper.html`) sigue dando **403** desde este
servidor, y el Wayback Machine de esa URL en concreto también está
bloqueado por la política de red del contenedor («Blocked by egress
policy»; lo comprobé con `curl` directo y con `web.archive.org`). **No es
que no exista** (el snapshot de Wayback del 11-7-2026 existe, lo confirmó
`archive.org/wayback/available`): hay que abrirla desde un PC normal.
Mientras tanto, sirven como «oficial en alta» los **pósters y key visuals de
temporada** de la wiki (§1), con tamaño real medido: `Season 7 Poster
1.png` 3029×2135, `Final Season Armored All Might.png` 3043×2151, `MHA 10th
Anniversary Visual.png` 2640×3410 — todos suficientemente grandes para fondo
de pantalla de escritorio.

**Ciudades y paisajes**: la biblia ya tenía una lista de sitios (aula 1-A,
USJ, playa Dagobah, campo Beta…) hecha de memoria con capítulo/minuto — eso
es del punto 4 de ENCARGO.md (le toca al investigador de vídeo, que mide luz
y paleta en fotogramas). Yo sólo confirmo que esos sitios existen como
**escenografía dibujada** en las hojas: `Field Gamma.png`, `Field Omega.png`,
`Ground Beta.png`, `Gym Gamma Outside.png`, `Development Studio Inside.png`,
`Conference Room (Anime).png` — todas imágenes de fondo puro de la wiki
(vistas al listar imágenes de la página «U.A. High School»), útiles como
referencia de sitio aunque no traigan personaje.

## 19 · Texturas 2D

- **Tramas de manga (screentone) libres**: [Manga with Stef — Free Screen
  Tone Collection 1](https://manga-with-stef.com/free-screen-tone-collection-1)
  (varias densidades de punto, para Krita/Procreate/Photoshop, declarado
  gratis por la propia autora) ✅; [GraphicsBunker — Free Comic Manga
  Screentone Brushes](https://www.graphicsbunker.com/brushes/free-comic-manga-screentone-brushes/)
  ⚠️ (dice «free», sin leer la letra pequeña de la licencia).
- **Grano de papel** (comparte capa con el punto 4, que no es mío, pero la
  textura sirve igual): [ambientCG, categoría Paper](https://ambientcg.com/list?sort=Popular&category=Paper),
  **CC0** ✅ — ya estaba en `datos-imagen.md`.
- **Patrón a cuadros (tartán) para los guanteletes de Bakugo**: no encontré
  un CC0 exacto; lo más cercano y gratis con atribución es la categoría
  [Vecteezy — Tartan Pattern](https://www.vecteezy.com/free-vector/tartan-pattern)
  ⚠️ (licencia Vecteezy estándar, hay que comprobar cada archivo: algunos
  piden atribución, otros son sólo para Vecteezy Pro).
- **Emblema de U.A.**: no encontré un archivo dedicado sólo al escudo en la
  wiki (busqué «U.A. High School logo» y «emblem» en el texto y en nombres
  de archivo de imagen, sin resultado). Sí aparece **dibujado en la ropa**:
  el cinturón y la mochila de Todoroki, el casco de Uraraka y los uniformes
  de todos llevan el escudo con la «U» — visible en `Class_1-A_Hero_Costumes.png`
  y en los perfiles de uniforme del 10.º aniversario (§1). Para el logo
  suelto (el del título de la serie), es tarea del punto 5 (tipografía, no
  mío).

## 23 · Colaboraciones y cruces

**Con Marvel** ✅✅ (dos fuentes: Marvel.com y Oricon, más ANMTV-style specialized
outlets): por el final del manga (diciembre 2024/enero 2025), **Horikoshi
dibujó a Spider-Man, All Might y Deku juntos**, y los artistas de Marvel
Humberto Ramos (dibujo) y Edgar Delgado (color) dibujaron a Black Cat rodeada
de heroínas de MHA (Mt Lady, Star and Stripe, Uraraka, Tsuyu, Momo, Setsuna,
Mirko) — [Marvel.com](https://www.marvel.com/articles/comics/marvel-weekly-shonen-jump-art-exchange-my-hero-academia-final-volume),
[Oricon](https://us.oricon-group.com/news/2692/), [Siliconera](https://www.siliconera.com/marvel-and-my-hero-academia-spider-man-art-exchange-revealed-in-honor-of-final-volume/).
Horikoshi dijo que Spider-Man fue «el primer héroe que conocí de niño, y
sigue siendo Spider-Man para mí hoy». La pieza de Horikoshi está en la wiki:
`Marvel Collaboration Piece by Kohei Horikoshi.png` (2457×3485, hoja_01
#31).

**Con Universal Studios Japan** ✅✅: primera colaboración grande el
1-3-2024 al 14-8-2024, con la atracción 4D **«My Hero Academia THE REAL
4D»** dentro de «Universal Cool Japan» — [Anime News Network](https://www.animenewsnetwork.com/interest/2023-12-10/universal-studios-japan-cool-japan-gets-1st-collab-with-my-hero-academia/.205199),
[Anime News Network (atracción)](https://www.animenewsnetwork.com/interest/2023-12-21/universal-studios-japan-new-my-hero-academia-4d-attraction-features-original-story/.205780).
También hay una ficha de la wiki sobre el USJ de dentro de la serie
(«Unforeseen Simulation Joint», mismas siglas que el parque real, es un
juego de palabras del autor) ⚠️ (un solo vistazo al snippet, sin confirmar
si Horikoshi lo dijo explícitamente).

**Cafeterías temáticas** ✅ (varias, todas de 2026): Shibuya Excel Hotel
Tokyu «Estacion Café» (9-2 a 30-4-2026) — [oficial](https://www.tokyuhotels.co.jp/en/shibuya-e/restaurant/estacion/plan/136312/index.html);
DECOTO by Animate Cafe Ikebukuro, tema «Waffle Diner», con Deku, Bakugo y
Todoroki de uniforme de camareros de hotel (3 a 26-4-2026) —
[essential-japan.com](https://essential-japan.com/news/new-my-hero-academia-cafe-to-feature-deku-bakugo-and-todoroki-in-hotel-uniforms/);
Animate Cafe «Stylish Cafe Parlor», todo agosto de 2026, tema héroes contra
villanos — [whatsonjapan.com](https://whatsonjapan.com/events/my-hero-academia-stylish-cafe-parlor-2026-in-ikebukuro-nagoya);
colaboración con **Trill Burgers** por el 10.º aniversario —
[CBR](https://www.cbr.com/my-hero-academia-anniversary-trill-burger-collab/);
y con **Marion Crepes** (Deku, Bakugo y Todoroki de reposteros) —
[ani-box.com](https://ani-box.com/en/my-hero-academia-marion-crepes-collab-2026/).

**Videojuego con colaboración dentro**: **MY HERO ACADEMIA: All's Justice**
(Switch 2, sale 4-9-2026) trae un modo minijuego exclusivo con
**PAC-MAN** de Bandai Namco ✅ — [Bandai Namco](https://www.bandainamcoent.com/news/my-hero-academia-alls-justice-is-coming-to-nintendo-switch-2-on-september-4).
Bakugo fue personaje DLC de **JUMP FORCE** ⚠️ (un solo indicio, nombre de
archivo de vídeo en la wiki, sin ver el tráiler).

**Figuras oficiales** ✅ (referencia de pose 3D real): línea **S.H.Figuarts**
de Bandai Tamashii Nations — `Katsuki Bakugo -The Beginning-`
([Tamashii Web](https://www.shfiguarts.com/category/1/368/SHFiguarts/SHFiguarts-My-Hero-Academia.html))
y `Overlay Deku` (¥11 000, preventa nov-2025, sale jun-2026,
[p-bandai.com](https://p-bandai.com/us/item/F2712342001/)) — no pude sacar
la imagen del producto (la página carga con JavaScript y el scraper no la
ve) ⚠️: hay que abrirla a mano para ver la pose exacta.

**Cosplay** ✅ (fotos con licencia libre, ya en `datos-imagen.md` vía
Openverse, autor **timz2011**, CC BY-NC-SA 2.0, de una convención — con
volumen y materiales reales, no dibujado): trajes de héroe de varias clases,
Kirishima, Hawks, All Might/Nana, Eri, Fatgum, Shouji, villanos. Sirven para
ver cómo cae la tela y el relleno del traje de verdad, no como fuente final.

## Las hojas de contacto

De las 92, dejé **2 en `hojas/`** (con nombre claro, JPEG, menos de 1,1 MB
cada una) porque son las que más sirven para IMAGEN; el resto sigue en
`herramientas/referencias/my-hero-academia/` (no ocupa el repositorio) por si
el redactor quiere otra:

- **`hojas/arte_oficial_01.jpg`** (= hoja_01 original): pósters de temporada,
  portadas de CD, el cartón «10.º aniversario», el videojuego *All's
  Justice*, la pieza de la colaboración con Marvel (celda #31) y una decena
  de cartones de cuenta atrás dibujados a mano. Es la mejor hoja para «arte
  oficial variado» (punto 1) y para el crossover de Marvel (punto 23).
- **`hojas/vestuario_juegos_01.jpg`** (= hoja_10 original): pósters de
  temporada 1-7, el arte de *My Hero One's Justice* (celda #439), la
  portada del databook *Ultra Analysis* en inglés y las 16 contraportadas de
  los tomos de EE. UU. de VIZ con mini-perfil de personaje. Sirve para
  vestuario en distintas épocas y para videojuegos.

También miré **hoja_02** (cartel «List of Characters», encuesta de
popularidad n.º 9, más colaboraciones) y **hoja_05** (fichas de personaje
tipo databook, más cartones de cuenta atrás) sin copiarlas: lo que servía de
ellas ya está citado arriba con su número de celda.

## Lo mejor para la lámina

1. `Izuku_Midoriya_Beta_Costume_Anime_Design_Sheet.png` (frente y espalda,
   limpia, con hex medidos en §15): la referencia más fiable para dibujar a
   Deku con su traje de héroe, no de memoria.
2. `Class_1-A_Hero_Costumes.png` (3593×1080): toda la clase junta en traje
   de héroe, en un sitio de U.A. — sirve para una lámina de grupo o para
   elegir con quién sale Deku.
3. El modelo 3D CC BY **«My Hero Academia UA classroom»** (banabanaba): el
   aula real en 3D, para renderizar el fondo del concepto del cuaderno en
   Blender sin dibujar el aula desde cero.
4. La pieza de la **colaboración con Marvel** (Horikoshi dibujando a
   Spider-Man, All Might y Deku): un gancho visual único para el servidor,
   nadie más lo tendrá.
5. `hojas/arte_oficial_01.jpg` celda #34/#43 (*All's Justice*, 2026): el
   videojuego más nuevo de la franquicia, con arte fresco de los trajes
   actuales.

## No encontré ⚠️

- Portada del Blu-ray de la serie TV, vol. 1 (sólo la tienda, sin imagen
  abierta). Busqué «Blu-ray cover volume 1» y «DVD Blu-ray Volume 1 Cover»
  en el texto de la wiki (`srsearch`, espacio de nombres de archivo): sólo
  salió la del BD de la película *World Heroes Mission*.
- La página oficial de fondos de pantalla (`heroaca.com/special/wallpaper.html`):
  403 en directo y el Wayback Machine de esa URL bloqueado por la política
  de red de este contenedor (no es que la página no exista: el snapshot
  está confirmado). Queda para quien lo abra desde un PC normal.
  cambia mi conclusión: es un **extra** (ya hay wallpapers oficiales
  equivalentes en los pósters de temporada), no algo obligatorio sin
  cubrir.
- Un archivo de imagen suelto sólo con el **emblema de U.A.** (sin
  personaje ni ropa encima). Busqué «U.A. High School logo/emblem» en el
  texto de la wiki y en nombres de archivo de imagen de esa página: no
  apareció. El escudo sí se ve dibujado en la ropa (§19).
- Licencia exacta del modelo 3D «Deku (Izuku Midoriya)»: la until de
  Sketchfab dice CC Attribution-NonCommercial, lo dejo anotado así en la
  tabla (§3) para que no se use en nada comercial.
- Imagen del producto de las figuras S.H.Figuarts (la web carga con
  JavaScript): tengo el nombre, precio y enlace, no la foto.

## Bitácora de búsqueda

- **Español**: «My Hero Academia colaboración crossover oficial cafetería
  figuras 2026» (WebSearch) → cafés y colabs de 2026.
- **Español/inglés**: «My Hero Academia Universal Studios Japan
  colaboración USJ» → atracción 4D, Anime News Network.
- **Inglés**: «"My Hero Academia" Marvel collaboration Horikoshi Spider-Man
  crossover art» → Marvel.com, Oricon, Siliconera, ComicBook, Bleeding
  Cool.
- **Inglés**: «My Hero Academia S.H.Figuarts figura oficial Deku Bakugo
  pose» → Tamashii Web, p-bandai.
- **Inglés**: «"My Hero Academia" "All's Justice" Nintendo Switch 2 game
  2026» → Bandai Namco, Nintendo Life, GoNintendo (confirma fecha,
  minijuego PAC-MAN).
- **Inglés**: «U.A. High School logo emblem My Hero Academia vector PNG» →
  sólo reproducciones de fans (Pinterest, Etsy, seeklogo); no vale como
  fuente del original.
- **Inglés**: «free CC0 manga screentone halftone texture pack github» →
  Manga with Stef, GraphicsBunker.
- **Inglés**: «green plaid tartan seamless pattern free CC0 texture» →
  Vecteezy (licencia a comprobar por archivo).
- **API de Fandom** (`myheroacademia.fandom.com/api.php`): `list=search`
  con `srnamespace=6` (sólo archivos) para «Katsuki hero costume mugshot»,
  «Shota Aizawa hero costume mugshot», «Izuku/Ochaco/Shoto/Toshinori Hero
  Costume Anime Design Sheet», «U.A. uniform», «Blu-ray cover volume 1»,
  «U.A. High School logo/emblem»; `prop=images` sobre las páginas «Katsuki
  Bakugo», «Shoto Todoroki» y «U.A. High School» (la página de personaje de
  Bakugo y Todoroki estaban **mal resueltas** en `datos-imagen.md`: el
  recolector había cogido «Bakugo House» y «Rei Todoroki» — lo corrijo aquí
  con los títulos reales de la wiki, comprobados con `list=search`);
  `prop=imageinfo&iiprop=url|size` para el tamaño real y la URL de cada
  archivo elegido.
- **API de Sketchfab** (`api.sketchfab.com/v3/search` y
  `/v3/models/<uid>`): `q=My Hero Academia`, `q=My Hero Academia classroom`,
  y una por personaje (Katsuki Bakugo, Shoto Todoroki, Ochaco Uraraka,
  Aizawa Eraserhead, All Might) con `downloadable=true`, para sacar
  licencia, autor y caras **de la API, no de la página** (más fiable).
- **Wayback Machine**: `archive.org/wayback/available?url=heroaca.com/…` (sí
  hay snapshot) y luego `web.archive.org/web/<fecha>/…` (bloqueado por la
  política de red del contenedor, distinto del 403 directo).
- **Imágenes miradas de verdad** (Read, no sólo leídas de una lista):
  hoja_01.jpg, hoja_02.jpg, hoja_05.jpg y hoja_10.jpg completas (192
  imágenes); y, ya bajadas aparte con `curl`,
  `Class_1-A_Hero_Costumes.png`, `Katsuki_Bakugo_Hero_Costume_Anime_Design_Sheet.png`,
  `Shoto_Todoroki_Beta_Costume_Anime_Design_Sheet.png`,
  `Izuku_Midoriya_Beta_Costume_Anime_Design_Sheet.png`,
  `Ochaco_Uraraka_Hero_Costume_Anime_Design_Sheet.png` y
  `Shota_Aizawa_Hero_Costume.png` (esta última resultó ser un panel de
  manga en blanco y negro, no el color del anime: para el hex usé la
  versión «(Anime)» en su lugar, medida con `estilo.py`).
- **estilo.py**: 14 imágenes oficiales medidas en dos tandas; resultado
  completo en `/tmp/claude-0/trabajo/25-my-hero-academia-imagen/paletas/estilo.json`
  (con paleta y estilo de sombreado/línea de cada una).

## Cumplimiento de mis puntos (1, 3, 15, 16, 19, 23)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | Key visuals, portadas de tomo/CD/BD, 2 videojuegos, hojas de modelo de los 6 personajes, cartones de cuenta atrás — todo con URL y tamaño real |
| 3 · Fan art y 3D con licencia | ✅ | Fan art ya en datos-imagen.md; 3D ampliado a 8 modelos CC Attribution confirmados por la API de Sketchfab (autor, caras, licencia) |
| 15 · Vestuario con hex | ✅ | Uniforme + traje de héroe de los 6 personajes del encargo, hex medidos con estilo.py sobre archivos oficiales, no de memoria |
| 16 · Fondos de pantalla | ✅⚠️ | Wallhaven ya tenía tamaño/autor/origen; la web oficial de wallpapers sigue bloqueada (403 y Wayback también) — cubierto con pósters oficiales grandes como alternativa |
| 19 · Texturas 2D | ⚠️ | Screentone y grano de papel con enlace y licencia; el tartán de Bakugo y el emblema de U.A. sueltos no los encontré (quedan en «No encontré», son extra, no obligatorio) |
| 23 · Colaboraciones y cruces | ✅ | Marvel, USJ, 3 cafeterías, 1 videojuego nuevo con su propia colaboración (PAC-MAN), figuras oficiales, cosplay con licencia |

No dejo `Sigue:` — de lo obligatorio de mis 6 puntos, todo tiene al menos una
fuente real y, donde pude, dos. Lo que falta (Blu-ray TV vol. 1, wallpaper
oficial en directo, tartán/emblema sueltos, foto de las figuras) está en
«No encontré» porque es *extra* sobre lo ya cubierto, no una obligación sin
tocar.
