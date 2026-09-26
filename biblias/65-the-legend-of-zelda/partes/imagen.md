# Imagen — The Legend of Zelda (parte del investigador de imagen)

Puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md. Libreta de datos, no prosa.
Fuente base: `partes/datos-imagen.md` (recolectar.py, 2026-09-25) + búsqueda propia.
Sin serie hermana (comprobado con `herramientas/hermanas.py`).

## 1 · Arte oficial, en cantidad y variado

`investigar_serie.py` bajó 120 imágenes grandes de zelda.fandom.com (Link,
Princess Zelda, Ganon) en 3 hojas de contacto (`hojas/personajes_01.jpg`,
`personajes_02.jpg`, `objetos_01.jpg`). Cubre casi todos los juegos: TLoZ
(1986), ALttP, OoT, MM, OoA/OoS, WW, FS/FSA, TMC, TP, PH, ST, SS, ALBW, HW/HWL,
TFH, BotW, TotK. Están miradas (Read) las tres hojas completas.

- Link de pie con espada y escudo, pose «icónica» repetida en toda la franquicia (OoT, ALttP, TP) · hoja `personajes_01.jpg` nº 9,10,34 · zelda.fandom.com/wiki/Link · ✅ (visto en hoja + wiki) · 2782×3463 a 3786×2650
- Link EN ACCIÓN, no sólo de pie: a caballo/Master Cycle Zero (BotW), disparando arco (FS, BotW), luchando contra Ganondorf/Stalfos, con Wolf Link (TP) · hoja nº 3, 9, 42, 75, 81 · zelda.fandom.com · ✅ · 985×1407 a 3786×2650
- Link EN GRUPO: con Zelda en TotK (nº92), con el Rey de los Leones Rojos (modelo WW, nº116), con Midna/Wolf Link (nº81), «3 Triforce Heroes» (TFH, nº46) · zelda.fandom.com · ✅
- Zelda con su arma propia: arco de luz (nº87,90 «Tp lightarrow1», «Zelda LightArrow»), como Sheik (nº19), Zelda guerrera Hyrule Warriors (render nº13) · zelda.fandom.com · ✅
- Ganon/Ganondorf variado: forma humana con tridente (HWL, nº5), Ganon bestia (OoT, nº7), Calamity Ganon (BotW, nº30 «DemonDragonTotK2»), combate final Link vs Ganondorf (nº8, 1 «Final Battle in Hyrule» 5244×3968) · zelda.fandom.com · ✅
- Key visual/portada de manga: AniList lista una portada bajo «manga/143777» (adaptación); 3373×3609 no confirmado como portada real de tomo, ⚠️ revisar contra Viz Media antes de usar · https://anilist.co/manga/143777 · ⚠️ (una fuente, dato de recolectar.py sin contrastar)
- Logos oficiales por juego (para tipografía y para fondos de lámina): ALttP (nº55), OoA/OoS (nº62,63), ST (nº65), TMC (nº113), TFH (nº71), Zelda genérico dorado (nº76) · zelda.fandom.com · ✅
- Arte del 30 aniversario de la serie (grupo de Links de toda la franquicia) · hoja nº54 «Link 30th anniversary.jpg» 2520×1000 · zelda.fandom.com · ✅
- Modelos/render 3D oficiales de la propia Nintendo (no fan-render): TotK Zelda Model (nº77), TP Ganon Model (nº79), ALBW Ganon Model (nº119), TWW Ganondorf Model (nº117), TWW Princess Zelda Figurine Model (nº83), TWW Link & King of Red Lions Figurine Model (nº116) · zelda.fandom.com · ✅

### Fuera de la wiki de Fandom

- Nintendo tiene una página oficial de la franquicia con arte de portada de Tears of the Kingdom y Breath of the Wild en alta resolución · https://www.zelda.com/ · ⚠️ (no se pudo bajar el archivo en este servidor, sólo confirmado que existe la sección de fondos/arte) — pendiente de comprobar en máquina con acceso normal
- El artbook «Hyrule Historia» (Dark Horse, 2013) recopila arte conceptual de toda la franquicia hasta Skyward Sword; es la referencia más citada por fans y prensa especializada para poses y bocetos de producción · reseñas en IGN/Nintendo Everything (búsqueda web) · ⚠️ (no se descargó el PDF, sólo confirmado que existe y qué cubre)

## 3 · Fan art y renders 3D (referencia) + modelos 3D con licencia libre

Fan art es sólo referencia (enlace y autor, nunca para pegar). Los modelos 3D
con licencia sí son descargables: comprobados con la API v3 de Sketchfab
(`isDownloadable: true`) y con la API de Poly Haven (todo CC0 ahí).

### Fan art mejor valorado (Danbooru, rating:general, por personaje)

- Link, 1920×1080, arte de **sharlene_yap** · fuente: https://www.youtube.com/watch?v=B0FsOImlqVI · vía danbooru.donmai.us/posts?tags=link+rating:general · ⚠️ (una fuente, sólo referencia visual, no se usa el archivo)
- Link, 1588×2048, arte de **tixili** · https://twitter.com/tixi815/status/1667443596692443137 · ⚠️
- Zelda, 3582×2026, arte de **the_only_shoe** · https://twitter.com/The_Only_Shoe/status/1187730535570739206 · ⚠️
- Zelda, 1588×2048 (misma artista que Link arriba, estilo reconocible) · tixili · ⚠️
- Ganondorf, 2000×1376, arte de **snegovski** · https://i.pximg.net/img-original/img/2023/10/04/12/31/48/11226204 (Pixiv) · ⚠️
- Ganondorf, 3900×2800, arte de **bb_(baalbuddy)** · https://twitter.com/baalbuddy/status/1486616468666134531 · ⚠️
- Aviso: los datos de `datos-imagen.md` (Safebooru «fan art mejor valorado») están repetidos e idénticos para los 7 personajes de la lista (incluye Pikachu, Kirby, Samus…) — es un fallo del recolector (parece no filtrar por tag), **no se usaron**; se repitió la búsqueda a mano en Danbooru con `rating:general` filtrando NSFW.

### Modelos 3D con licencia libre — Sketchfab (objetos y sitios; comprobado `isDownloadable=true` vía API)

- **Legend of Zelda Master Sword** (Voldepreuss) · CC BY · https://sketchfab.com/3d-models/legend-of-zelda-master-sword-cb7f91aa8594406ea6fc7cb72846743b · ✅ (API confirma licencia y descarga) · 2808 caras
- **Hylian Shield** (MikeLuxton) · CC BY · https://sketchfab.com/3d-models/hylian-shield-c0a9c05d45174318a9a2b13ebc53b1b7 · ✅ · 5208 caras
- **Triforce** (Dryan5) · CC BY · https://sketchfab.com/3d-models/triforce-a8e46e9f5ea1491babc610360f2b57ff · ✅ · 752 caras
- **Korok - Legend of Zelda** (wersaus33) · CC BY-SA · https://sketchfab.com/3d-models/korok-legend-of-zelda-4e21d9b8eaef498da778863cc8fee8a7 · ✅ · 1170 caras
- **Legend of Zelda - Adventurer's backpack** (glenatron) · CC BY · https://sketchfab.com/3d-models/legend-of-zelda-adventurers-backpack-dc3b000a15fa4042ba7f756cc4bb3dfe · ✅ · 8596 caras
- **The Wind Waker - Hyrule Castle** (jkimmel694), sitio completo · CC BY · https://sketchfab.com/3d-models/the-wind-waker-hyrule-castle-9c30907ba24143ef85624084331d855b · ✅ · 22566 caras
- **[Voxel] Kakariko full Scene** (dysonson), pueblo completo estilo voxel · CC BY · https://sketchfab.com/3d-models/voxel-kakariko-full-scene-6ef46d45927945259127a73484f10d24 · ✅ · 1 062 062 caras (pesado)
- Más resultados descargables confirmados por la API (sin bajar el archivo): «Hyrule Castle» de allanromanreyes (Free Standard, no CC), «Cloths Zelda Sheikah», «Zelda's Masks», «Master Sword And Hylian Shield» de varios autores — todos con `q=<término> downloadable=true` en `api.sketchfab.com/v3/search`.

### CC0 (Poly Haven) — objetos genéricos que encajan con la ambientación de Hyrule

Poly Haven no tiene contenido con marca (todo es CC0 original), pero varios
objetos genéricos sirven tal cual para decorar una escena tipo Kakariko/aldea
Hyrule sin pedir crédito:

- **Treasure Chest** (cofre de madera con herrajes) · CC0 · https://polyhaven.com/a/treasure_chest · ✅ (licencia uniforme de Poly Haven, confirmada en su API)
- **Wooden Lantern 01** · CC0 · https://polyhaven.com/a/wooden_lantern_01 · ✅
- **Stone Fire Pit** · CC0 · https://polyhaven.com/a/stone_fire_pit · ✅
- **Wooden Barrels 01** · CC0 · https://polyhaven.com/a/wooden_barrels_01 · ✅
- **Wooden Crate 01** · CC0 · https://polyhaven.com/a/wooden_crate_01 · ✅

## 15 · Vestuario: colores medidos por arco/juego

Colores sacados con `herramientas/estilo.py` (paleta por *clustering* de color,
6 colores por imagen) sobre el arte oficial bajado de la wiki (con cabecera
`Referer`, igual que hace `investigar_serie.py`). Cada hex es de **una sola
imagen** (⚠️ salvo que se diga lo contrario): es una medición, no una cita
doble. El traje "icónico" que todos reconocen es la túnica verde de Link
(cualquier época) y el vestido/traje real con el Triforce dorado de Zelda.

Personaje | Prenda | Hex medido | De qué imagen
---|---|---|---
Link | Túnica clásica verde (era Ocarina of Time / A Link to the Past) — LA icónica | `#119E1A` | OoT Link Artwork.png (zelda.fandom.com), 2782×3463 ⚠️
Link | Túnica ALBW (verde oliva, más apagada que la clásica) | `#4C4D34` | ALBW Link Artwork.png, 3373×3609 ⚠️
Link | Túnica del Prócer/Campeón (Breath of the Wild), azul | `#277AAF` (con detalles claros `#BAE7E7`) | BotW Link Shooting Artwork 2.png, 985×1407 ⚠️
Link | Botas y guantes de cuero (constante en casi todas las épocas) | `#AC5614` / `#A86E3E` | OoT y ALBW Link Artwork ⚠️
Zelda | Vestido A Link Between Worlds (azul grisáceo con dorado) | `#59788E` (dorado `#E9CD75`) | ALBW Princess Zelda Artwork.png, 2158×2659 ⚠️
Zelda | Traje casual de exploradora (Breath of the Wild) | `#274249` (resalte `#467D8D`) | BotW Zelda Artwork.png, 2645×2992 ⚠️
Zelda | Vestido del espíritu/fantasma (Tears of the Kingdom, la Zelda del pasado que acompaña) | `#EEE4AA` con bordado dorado `#D99936` | TotK Princess Zelda Artwork.png, 790×1058 ⚠️
Ganondorf | Armadura de cuero + capa roja (Hyrule Warriors Legends, forma guerrera) | armadura `#544036`/`#2B1814`, capa `#C0361F` | HWL Ganondorf Thief's Trident Artwork.png, 3130×3810 ⚠️
Ganondorf | Piel y armadura oscura (Ocarina of Time) | piel `#733511`, armadura `#1E120A` | OoT Ganondorf Artwork.png, 2122×3734 ⚠️

- Peinado: Link siempre rubio con gorro puntiagudo verde (excepción: gorro azul en Champion's Tunic BotW/TotK); Zelda siempre rubia, con distintos recogidos/trenzas por juego (suelto en BotW/TotK, trenza en HW, diadema en ALttP/ALBW) · visto en las 3 hojas de contacto (`hojas/personajes_01.jpg`, `_02.jpg`) · ✅ (patrón repetido en >15 artes distintos)
- Accesorio constante de Link: el escudo Hyliano (rojo, con ala de pájaro dorada y triángulos azules) casi en cada época · hoja `personajes_01.jpg` nº 10, 17, 21, 40 · ✅
- Accesorio constante de Zelda: el pendiente/broche o colgante con el Triforce · hoja `personajes_01.jpg`/`_02.jpg` nº 15, 61, 70, 77, 92 · ✅
- Aviso de método: en TotK Princess Zelda Artwork.png aparecen DOS Zeldas superpuestas (la exploradora en primer plano con antorcha, y el espíritu/fantasma detrás); el clustering de color mezcla ambas prendas, así que el hex de la prenda de la exploradora en primer plano no se pudo aislar con garantía (la antorcha se solapa con el torso) — se dejó sólo el vestido del espíritu, que sí se pudo aislar.

## 16 · Ciudades, paisajes y fondos de pantalla

Los sitios en detalle (luz, hora del día por escena) los mide el investigador
de vídeo en fotogramas (punto 4); aquí van los **fondos de pantalla** en alta
resolución, oficiales y de fans, con tamaño y autor.

### Fondos oficiales (Nintendo, My Nintendo Rewards)

- Nintendo reparte fondos de pantalla oficiales de Tears of the Kingdom por personaje/escena a través de «My Nintendo Rewards» (canjeables con puntos, no descarga directa sin cuenta): «Link», «Ganondorf», «Zelda and Link», «Construct», aniversario de 1 año · https://my.nintendo.com/rewards/d9fa9f0adc29b641 (Link) y https://my.nintendo.com/rewards/f4c445a0b4c6a538 (Ganondorf) · ⚠️ (confirmado que existen por el buscador; no se pudo entrar a bajar el archivo sin cuenta de My Nintendo desde este servidor)

### Fondos de fans mejor valorados (Wallhaven, sólo aptos, ≥1920×1080)

- 2559×1440 · Link y Zelda abrazados con el Castillo de Hyrule al fondo (BotW) · autor **PhoenixBlood** · 189 favoritos · https://wallhaven.cc/w/5dodx5 · ✅ (visto en Wallhaven, confirmado con la API v1/w) · 3.3 MB
- 2000×1129 · Zelda y Link, bokeh (TotK) · autor **bubbleboba** · 177 favoritos · https://wallhaven.cc/w/3z85yy · ✅ · 1.4 MB
- 2000×1122 · Link, cielo (TotK) · autor **Rynios** · 147 favoritos · https://wallhaven.cc/w/yxg9rg · ✅ · 300 KB
- 2048×1408 · Link (TotK, misma autora) · **Rynios** · 146 favoritos · https://wallhaven.cc/w/zyo68g · ✅ · 451 KB
- 4000×2500 · Zelda, BotW/TotK · autor **Owl279** · 138 favoritos · https://wallhaven.cc/w/6dz5p6 · ✅ · 2.9 MB

### Sitios icónicos que aparecen en el arte y en los fondos (para elegir escenario de la lámina)

- Castillo de Hyrule: presente en casi todos los juegos, es EL sitio icónico de la saga; en BotW/TotK flota o está dañado por el Calamity Ganon · visto en el fondo Wallhaven nº1 y en el arte oficial (hoja `objetos_01.jpg` nº 30 «DemonDragonTotK2») · ✅
- Pueblo Kakariko: aldea de estilo rural japonés/medieval, recurrente desde OoT hasta BotW/TotK · confirmado también por el modelo 3D descargable «[Voxel] Kakariko full Scene» (punto 3) · ✅
- Bosque Korok/Bosque Kokiri: bosque encantado, entrada al mundo en varios juegos · nombre confirmado en el modelo 3D «Korok - Legend of Zelda» (punto 3) y en la wiki (zelda.fandom.com/wiki/Korok_Forest) · ✅
- Desierto Gerudo y Muerte (Death Mountain): extremos climáticos icónicos de Hyrule (arena/lava), mencionados en la wiki de zelda.fandom.com como localizaciones recurrentes desde OoT · zelda.fandom.com/wiki/Gerudo_Desert, zelda.fandom.com/wiki/Death_Mountain · ⚠️ (confirmado en wikitext, no se midió luz/paleta aquí: es tarea del investigador de vídeo, punto 4)

## Referencias

Ver `partes/imagen.json`.
