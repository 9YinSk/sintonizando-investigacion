# Parte IMAGEN · Sword Art Online (todas)

Investigador de imagen: puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md. Libreta de datos, no prosa.
Wiki usada: `swordartonline.fandom.com`. Base: `partes/datos-imagen.md` (casi vacío: `recolectar.py`
no tenía wiki configurada y AniList/Danbooru automáticos fallaron; se investigó todo a mano con
`investigar_serie.py` + búsquedas directas a las APIs de Danbooru, Safebooru, Wallhaven, Sketchfab
y Openverse).

Hojas de contacto generadas con `herramientas/investigar_serie.py --wiki swordartonline --paginas
"Kirito" "Asuna Yuuki" "Shino Asada" "Alice Zuberg" "Sword Art Online"`: **1 637 imágenes** de la
wiki indexadas en `herramientas/referencias/sword-art-online-todas/indice.json` (no se sube al
repo), montadas en 20 hojas de contacto de 48 imágenes cada una. Las 3 elegidas para el repo están
en `hojas/` (ver abajo).

## Hallazgos

### Punto 1 — Arte oficial, en cantidad y variado

- **abec Art Works** (artbook oficial de portada, Kadokawa/ASCII Media Works, ISBN 978-4-04-865709-9,
  2 800¥): cubierta y contraportada con Kirito, Asuna (Knights of Blood), Alice y Eugeo (Integrity
  Knights), Sinon/Leafa/Silica y Klein juntos, más de 15 poses vivas en grupo y en acción ·
  https://static.wikia.nocookie.net/swordartonline/images/6/67/Abec_Art_Works_Cover-Back.jpg
  (5175×3488) y https://static.wikia.nocookie.net/swordartonline/images/8/8e/Abec_Art_Works_Alice_%26_Eugeo_designs.jpg
  (4940×7020, hoja de modelo con Alice niña/adulta e integrity knight, Eugeo niño/adulto y sus
  espadas) · ✅ (wiki + producto real con ISBN verificable en Kadokawa) · tamaño arriba.
- **Portadas de revista** (Dengeki Bunko, Newtype, Megami) 2013-2020, todas 4000-6900 px de ancho:
  Newtype 201302/201403/201405/201408, DengekiBunko July 2014, NewType July2014 SAOII, Animedia
  Magazine Feb 2019 (Alicization) · listadas en `indice.json` posiciones 2-16 · ✅ (wiki, imágenes
  originales de revista escaneada) · 4000-6900×~4100 px cada una.
- **Portadas de novela ligera y manga**: Progressive, Fairy Dance, Alicization, Aincrad — decenas de
  cubiertas (`Fairy_Dance_Manga_Volume_3_cover.png` 1800×2560, etc.) y las últimas novelas 2025-2026
  (ADAMAS, Forget-me-not, IGNITE: portadas «anime limited» a color, 3700-6900 px) · ✅.
- **Colaboraciones con arte propio** ya en la wiki (ver también punto 23): «SAO x GENCO x THE KISS
  Collaboration V» (2896×2048) y «SAO x FujiQ Collaboration Visual April-June 2019» (2853×2106),
  ambas en la hoja 1 (números 47-48 del índice) · ✅.
- **Hojas de modelo (settei) sueltas**: `Demon_Kirito_Design_Works_art_book.png`,
  `Kirito_Millennium_Twilight_character_design.png`, `Kazuto-Body-Design_SAOII.png` /
  `Kazuto-Head-Design_SAOII.png` / `Kirito-GGO_Body-Designs_SAOII.png` (three-quarter turnarounds,
  1280×880), `Asuna_PB_Character_Design.png` (turnaround frontal+trasero, 1280×880),
  `Code_Register_KoB_Kirito_Original_Outfit.png` (867×822) · ✅.
- Fuera de la wiki: Danbooru y Safebooru tienen miles de posts con la etiqueta `sword_art_online`
  (fan art, no oficial — usado en el punto 3).

### Punto 3 — Fan art y renders 3D (como referencia, nunca para pegar)

- **Fan art más votado en Danbooru** (orden por *score*, sólo enlace+autor, nunca para pegar):
  post 4895802 (score 1592) por *nyantcha* · https://danbooru.donmai.us/posts/4895802 ·
  https://cdn.donmai.us/original/80/18/8018b107ecd2fd27637ff0f32f2b86a0.jpg · ⚠️ (una fuente, es
  agregador) · sin medida de licencia (fan art, sólo referencia).
- Más fan art votado: post 8495962 (score 522, *arado_balanga*), post 5355713 (score 501, *caisan*),
  post 4304823 (score 402, *asou_(asabu202)*), post 6388762 (score 392, *tokupyon*) ·
  https://danbooru.donmai.us/posts/8495962 · https://danbooru.donmai.us/posts/5355713 ·
  https://danbooru.donmai.us/posts/4304823 · https://danbooru.donmai.us/posts/6388762 · ⚠️.
- **Safebooru** (todas apto para todo público, `tags=asuna_(sword_art_online)+sort:score`): posts
  con score 4-5, autores/fuentes en Danbooru y Gelbooru re-indexados, ejemplo
  `https://safebooru.org/index.php?page=post&s=view&id=` con imagen 4077×5933 (Gelbooru) · ⚠️.
- **Renders 3D con licencia libre (Sketchfab, filtrados por CC Attribution/descargables)**:
  - «Sword Art Online - Elucidator» (espada de Kirito) — Kroed — CC Attribution —
    https://sketchfab.com/3d-models/none-67e18b82f18e4a99afa9cb53791b0857 ✅ (Sketchfab declara la
    licencia en su ficha, comprobado por API).
  - «Sword Art Online - Blue Rose Sword» — R4ven3D — CC Attribution —
    https://sketchfab.com/3d-models/none-e12d1bf75e554e0caa8827aebebeb769 ✅.
  - «SAO Kirito sword» (x3 variantes) — sirerdees — CC Attribution —
    https://sketchfab.com/3d-models/none-072503179c2a4a56ac2e9fc2d8b64b9c ✅.
  - «Kirito (SAO) (Simple)» — Senpai3689 — CC Attribution —
    https://sketchfab.com/3d-models/none-d107038c01bb46408a97c345ab5f2cae ✅.
  - «Asana (SAO:LS)» [sic, Asuna] — Senpai3689 — CC Attribution —
    https://sketchfab.com/3d-models/none-677b4ab2d76444dd81dc520a40111abe ✅.
  - «Yuuki Asuna Warrior 3D Model» — CesPaul — **CC Attribution-ShareAlike** —
    https://sketchfab.com/3d-models/none-7a1715af60a74e0baf1391833e843006 ✅.
  - «Sinon 3D Model (SAO)» — Senpai3689 — CC Attribution —
    https://sketchfab.com/3d-models/none-9a0aa3e82dd349e7b85eaabe60a482f7 ✅.
  - «Hightpoly Sinon SAO» — liye.yan1994 — CC Attribution —
    https://sketchfab.com/3d-models/none-f488abd66db34e18b48b76cbf10782fc ✅.
  - «Anime Academy from Sword Art Online» (aula/sitio, no personaje) — ani111 — CC Attribution —
    https://sketchfab.com/3d-models/none-e2110c991a24429c936d3eaceeb89cce ✅ (sirve para el punto 16
    también, es un lugar de la serie).
  - «Sword Art Online - Gun Gale Lobby» (sitio) — fizzlefreshh — CC Attribution —
    https://sketchfab.com/3d-models/none-cffc4b99140b408ca795a5b96411ce77 ✅.
  Todas comprobadas vía `https://sketchfab.com/v3/search?type=models&q=<busqueda>&downloadable=true`
  (API pública, licencia viene en el JSON, no de memoria).
- **Cosplay real con licencia libre (Openverse, Flickr CC)**: «Sinon (Gun Gale Online)» — CC BY-SA
  2.0 — https://live.staticflickr.com/8631/15464151893_53f08f611c_b.jpg ✅ (licencia en metadatos de
  Openverse) · «Asuna» (x2) — CC BY-SA — https://live.staticflickr.com/7439/10408103156_7dec420ef1_b.jpg
  y https://live.staticflickr.com/3683/10408132766_d6ea2a9aaa_b.jpg ✅ · «Asuna Aincrad ver.» (x4,
  distintas convenciones) — CC BY-NC-ND — no reutilizable comercialmente, sólo referencia visual de
  cómo queda el traje real, ⚠️ licencia restrictiva · varias fotos genéricas «Sword Art Online»
  (cosplay de grupo en convención) — CC BY 2.0 — https://live.staticflickr.com/563/20776554476_c905008e1b_b.jpg
  y 6 más de la misma búsqueda ✅.

### Punto 15 — Vestuario (hex medidos, no de memoria)

Medidos con Python/Pillow, promedio de un parche de 9×9 a 11×11 px sobre la imagen fuente real
descargada (no estimados a ojo). Son **aproximados** (el color varía con la iluminación de cada
escena, tal como pide el encargo).

- **Kirito, abrigo negro (Aincrad/KoB, «Coat of Midnight»)**: `#010b08`-`#0a0a0a` (negro casi puro,
  con un pelín de verde/azul por el tinte de la imagen) · muestreado en
  https://static.wikia.nocookie.net/swordartonline/images/6/67/Abec_Art_Works_Cover-Back.jpg y en
  el fotograma ALO `Asuna's_realisation.png` (mismo abrigo negro con cuello de piel blanca en la
  versión Spriggan de ALO) · ✅ (dos imágenes oficiales distintas, mismo tono).
- **Kirito, cuello de piel (ALO, avatar Spriggan)**: blanco cálido `#e3cea4` en la sombra (la piel
  real es blanca, este tono incluye la sombra ambiental azul de la escena) · misma fuente ALO · ⚠️
  (una imagen).
- **Kirito, ropa real/uniforme escolar** (turnaround `Kazuto-Body-Design_SAOII.png`): chaqueta negra
  con paneles gris pizarra en hombros y costados, vaqueros azul marino oscuro con parches de rodilla
  marrón — ficha de diseño oficial, colores planos sin sombreado (no se midió hex por ser lineart
  coloreado plano, pero es la referencia más fiable de color base) · ✅.
- **Asuna, KoB (blanco/rojo, «Flashing Flash»/Knights of the Blood)**: blanco frío `#eefdfd` en el
  hombro/solapa, rojo profundo `#630f17` en la falda con vivos dorados · muestreado en
  Abec_Art_Works_Cover-Back.jpg (recorte de alta resolución de Asuna, zona sin brillo de partículas)
  · ⚠️ (una imagen; la escena tiene iluminación azulada de fondo que puede desviar el blanco hacia
  el cian — comprobar contra una figura física antes de imprimir, ver Good Smile «Asuna -Knights of
  the Blood Ver.-» abajo).
- **Asuna, ALO (Titania, cian/blanco)**: pelo cian saturado `#61fdfe`, vestido blanco-hielo `#e2eff9`
  · muestreado en `Asuna's_realisation.png` (captura de anime, SAO II) · ⚠️ (una imagen, escena con
  luz submarina verdosa que puede sesgar el balance de color).
- **Asuna, uniforme real (chaqueta blanca doble botonadura + falda escocesa granate)**: turnaround
  oficial `Asuna_PB_Character_Design.png` — blanco puro de la chaqueta, falda de cuadros granate/
  blanco, medias grises, botas marrón oscuro · colores planos de la ficha, sin sombreado · ✅.
- **Alice Zuberg, Integrity Knight (azul marino + dorado)**: armadura dorada en hombro `#c29c52`,
  abrigo azul marino `#183267`/`#0f2f66`, emblema de rosa azul sobre el pecho tono similar al abrigo
  · muestreado en Abec_Art_Works_Cover-Back.jpg (recorte de alta resolución) · ✅ (coherente con la
  hoja de modelo a línea `Abec_Art_Works_Alice_%26_Eugeo_designs.jpg`, que muestra el mismo corte de
  armadura sin color).
- **Sinon, uniforme escolar real** (Shino Asada, imagen de perfil oficial de la wiki 1920×1080):
  blazer gris-marrón `#846c6c`, corbata roja oscura `#733434` · ✅ (imagen infobox oficial de la
  página del personaje, vía API de MediaWiki `action=query&prop=pageimages`).
- **Sinon, traje GGO (negro/gris oscuro)**: en la única captura nocturna disponible el traje se ve
  casi negro `#10090d`-`#251a1b`; es una escena de contraluz al anochecer, así que el tono real bajo
  luz de día es más claro (gris oscuro con vivos, según descripciones de la wiki) · ⚠️ (una imagen,
  contraluz — falta una captura de GGO en plena luz para confirmar el gris exacto del traje de
  camuflaje urbano).
- **Peinados icónicos** (para la lámina, sin hex): Kirito pelo negro corto despeinado; Asuna pelo
  castaño/naranja larguísimo con mechón trenzado alrededor de la cabeza (marca de identidad, se ve
  en casi todas las portadas); Sinon coleta baja oscura con lazo blanco; Alice pelo rubio muy largo
  suelto con diadema — ✅ (visto en >10 imágenes oficiales distintas cada uno, patrón consistente).

### Punto 16 — Ciudades, paisajes y fondos de pantalla (oficiales y de fans, en alta)

- **Wallhaven** (`q=sword art online`, orden por favoritos, sólo contenido apto): 
  `j5g2pq` 4000×2775, 395 favoritos, https://wallhaven.cc/w/j5g2pq · `ey7vjl` 2560×1440, 382 favs,
  https://wallhaven.cc/w/ey7vjl · `01329n` 1920×1080, 321 favs, https://wallhaven.cc/w/01329n ·
  `x1xy9l` 3840×2160, 292 favs, https://wallhaven.cc/w/x1xy9l · `28j5dm` 1920×1080, 235 favs,
  https://wallhaven.cc/w/28j5dm · `p9yjze` 6956×3897 (el más grande), 200 favs,
  https://wallhaven.cc/w/p9yjze · `o53ro5` 2835×4368 (vertical, sirve para móvil), 199 favs,
  https://wallhaven.cc/w/o53ro5 · todos ✅ (API pública de Wallhaven, con resolución y nº de favoritos
  reales, filtro `purity=100` = sólo apto).
- **4kwallpapers.com** tiene una colección con más de 20 fondos 4K de «Sword Art Online: Echoes of
  Aincrad» y Sinon, y **alphacoders.com** tiene 14+ fondos de Aincrad descargables gratis en varias
  resoluciones · https://4kwallpapers.com/sword-art-online · https://alphacoders.com/aincrad-(sword-art-online)-wallpapers
  · ⚠️ (agregadores, no se pudo verificar autor original de cada imagen individual).
- **Fondos oficiales de la wiki** (key visuals usables como wallpaper, ya en `indice.json`):
  `IGNITE_anime_limited_exterior.jpg` (6881×2912, panorámico), `ADAMAS_anime_limited_poster.jpg`
  (3764×5676), `Forget-me-not_anime_limited_poster.jpg` (5671×3754) · ✅.
- **Sitios de la serie con modelo 3D libre reutilizable** (además de la referencia real, ver punto 3):
  «Sword Art Online Cabin» — pcmonster — CC Attribution —
  https://sketchfab.com/3d-models/none-aba812a1fa3e479d8e3817b44e105b93 ✅.

### Punto 19 — Texturas 2D (tramas, grano, patrones, emblemas y logos)

- **Screentones/tramas de manga con licencia libre**: «[FREE] Manga Screentone Pack 1» —
  CLIP STUDIO ASSETS (gratis, licencia de la propia tienda de Celsys/Clip Studio, uso permitido en
  obras propias) — https://assets.clip-studio.com/en-us/detail?id=2142037 ✅ · alternativa gratuita
  «Comic Manga Screentone Brushes» (Gumroad, pon $0) — GraphicsBunker —
  https://www.graphicsbunker.com/brushes/free-comic-manga-screentone-brushes/ ⚠️ (licencia de uso no
  99% clara, revisar el término exacto del Gumroad antes de usarla en un producto público).
- **Emblema oficial del gremio Knights of the Blood** (aparece en el uniforme de Asuna y Kirito, cruz
  roja sobre fondo blanco al estilo Templario, según la propia wiki: «a white and red motif similar
  to the Knights Templar... a Red Cross for a symbol»): dos archivos oficiales distintos en la wiki —
  `K.O.B_Simbol.png` https://static.wikia.nocookie.net/swordartonline/images/d/da/K.O.B_Simbol.png y
  `KOB_Logo.png` https://static.wikia.nocookie.net/swordartonline/images/5/5b/KOB_Logo.png · ✅ (dos
  archivos de infobox de la wiki + texto descriptivo de la propia página, dos fuentes).
- **Manchas de tinta / pinceladas manga**: no se encontró una textura oficial descargable; para
  reproducir el entintado de Progressive/Aincrad manga (línea fina con algo de grano en sombras),
  usar pinceles de tinta libres de Krita/CSP (`brushapes.com` tiene pack gratuito de tinta básica,
  aunque el pack de screentone de arriba ya cubre lo esencial) · ⚠️.
- **Grano de papel / textura de portada de novela ligera**: las portadas de Kadokawa (ver punto 1)
  usan papel satinado liso, sin grano visible marcado; no aplica textura de papel rugoso.

### Punto 23 — Colaboraciones y cruces, figuras oficiales, cosplay

- **Cafés temáticos oficiales**: «Sword Art Online: Alicization Themed Cafe» en SEGA Akihabara
  Building 4 (5º piso), abrió 23 de marzo — https://www.moshimoshi-nippon.jp/181099 ✅ · «SEGA
  Collaboration Cafe Sword Art Online Alicization War of Underworld», 12 sept-25 oct 2020, mismo
  edificio — https://home.akihabara.kokosil.net/en/archives/27588 ✅ (dos fuentes coinciden en el
  local SEGA Akihabara 4th, fechas de eventos distintos = dos cafés, no un duplicado) · «SAO café»
  itinerante en Osaka, 2019 — https://animeanime.global/2019/10/21/49030.html ⚠️ (una fuente).
- **Colaboraciones de videojuego con arte propio**: «Mahjong Soul × Sword Art Online [Oath of the
  Sword]» — https://www.gamespress.com/Mahjong-Soul-X-Sword-Art-Online-Oath-of-the-Sword-Collab-Is-Now-Live
  ✅ · «Persona 5 Royal × SAO Memory Defrag/Integral Factor» (personajes de Persona 5 Royal añadidos
  a los juegos de SAO, con arte cruzado de ambos estilos) —
  https://www.siliconera.com/persona-5-royal-collaboration-announced-for-sword-art-online-memory-defrag-integral-factor/
  y https://www.dualshockers.com/persona-5-royal-sword-art-online-crossover/ ✅ (dos fuentes) ·
  «That Time I Got Reincarnated as a Slime × SAO Integral Factor» (ene 2026, skill records
  cruzados) — https://saointegralfactor.fandom.com/wiki/Collab_Skill_Records ⚠️ (una fuente,
  wiki de fans del juego).
- **Colaboraciones comerciales con arte propio ya en la wiki**: «SAO x GENCO x THE KISS
  Collaboration V» y «SAO x FujiQ Collaboration Visual April-June 2019» (parque de atracciones Fuji-Q
  Highland) — ambas imágenes ya citadas en el punto 1, con poses y vestuario nuevos de los
  personajes vestidos de empleados/paseantes del parque · ✅.
- **Figuras oficiales (referencia de pose 3D)**: Good Smile Company «Asuna -Knights of the Blood
  Ver.-» 1/8, posando con su espada Lambent Light —
  https://www.goodsmile.info/en/product/4053/Asuna+Knights+of+the+Blood+Ver.html ✅ · Kotobukiya
  «Asuna - Aincrad ver.» 1/8 — https://myfigurecollection.net/item/126835 ✅ · Good Smile Nendoroid
  Asuna (fairy ver., ALO) con 3 caras intercambiables — https://www.amazon.com/-/es/Good-Smile-Sword-Art-Online/dp/B00J69T8ZE
  ⚠️ (ficha de tienda, no del fabricante) · líneas activas confirmadas en
  https://www.goodsmileus.com/collections/sword-art-online-series ✅.
- **Cosplay bien hecho** (materiales y volumen reales, licencia libre): ver punto 3 → fotos Openverse/
  Flickr CC de Sinon y Asuna listadas ahí mismo, sirven también aquí.

## Lo mejor para la lámina

1. La página doble de **abec Art Works** (Cover-Back) es la única imagen que junta a Kirito, Asuna,
   Alice, Sinon y Eugeo con sus trajes icónicos completos y bien iluminados: úsala como referencia
   maestra de vestuario y paleta (hoja 1, `hojas/hoja_01_arte-oficial.jpg`).
2. El **emblema Knights of the Blood** (cruz roja/blanca, `K.O.B_Simbol.png`) es un logo real,
   pequeño y reconocible: perfecto para grabar en Blender sobre un objeto (broche, caja, cuaderno).
3. Los **Sketchfab CC Attribution** de Elucidator y Blue Rose Sword (espadas) se pueden importar
   directos a Blender para dar profundidad 3D delante del personaje 2D.
4. El fondo de **Wallhaven `p9yjze`** (6956×3897) es el de mayor resolución con más favoritos: sirve
   de fondo de pantalla o de lámina 2 sin perder calidad al recortar.
5. Las **fotos de cosplay CC BY/BY-SA de Openverse** dan volumen y materiales reales de tela para
   pintar la textura de la ropa sin depender sólo del cel-shading plano del anime.

## No encontré

- ⚠️ Modelos 3D con licencia libre de **sitios completos** de Aincrad/Underworld más allá de «SAO
  Cabin» y «GGO Lobby» (búsquedas: `sketchfab.com/v3/search?q=aincrad`, `q=underworld+sao`,
  `q=alfheim` — sólo devolvieron props sueltos, no arquitectura de piso completo).
- ⚠️ Fondos de pantalla **oficiales** (no fan-made) publicados directamente por Aniplex/A-1
  Pictures para descarga; los que hay en Wallhaven/alphacoders son todos recortes o remontajes de
  fans a partir de key visuals — es un extra, no bloquea el punto 16 (que ya tiene fondos de fans en
  alta con enlace, tamaño y favoritos).
- ⚠️ Captura de GGO en **plena luz de día** para confirmar el hex exacto del traje de camuflaje de
  Sinon (sólo se encontró una escena de contraluz nocturno en la wiki con las 5 páginas indexadas).
- ⚠️ Texturas CC0 de **grano de papel** específicas para portada de novela ligera (no aplica: las
  portadas de Kadokawa usan papel satinado sin grano marcado, así que no hace falta esta capa).
- ⚠️ Modelos 3D de **Alice o Eugeo** con licencia libre en Sketchfab (búsquedas `q=alice zuberg`,
  `q=eugeo sao` no devolvieron resultados con licencia CC, sólo con licencia de tienda o sin
  licencia declarada) — sí hay de Kirito, Asuna y Sinon.

## Bitácora

- Español/inglés, wiki: `swordartonline.fandom.com` vía `investigar_serie.py --wiki swordartonline
  --paginas "Kirito" "Asuna Yuuki" "Shino Asada" "Alice Zuberg" "Sword Art Online"` → 1637 imágenes,
  20 hojas de contacto en `herramientas/referencias/sword-art-online-todas/`.
- API Danbooru: `https://danbooru.donmai.us/posts.json?tags=kirito+order:score` y
  `...tags=asuna_(sword_art_online)+order:score` (sin `rating:general` porque con ese filtro la
  API devolvió vacío) y `...tags=shino_asada+order:score` (vacío, sin fan art etiquetado con ese
  tag exacto en Danbooru).
- API Safebooru: `https://safebooru.org/index.php?page=dapi&s=post&q=index&json=1&tags=asuna_(sword_art_online)+sort:score`.
- API Wallhaven: `https://wallhaven.cc/api/v1/search?q=sword+art+online&sorting=favorites&categories=010&purity=100`.
- API Sketchfab: `https://sketchfab.com/v3/search?type=models&q=<término>&downloadable=true` con
  términos `sword art online`, `kirito sao`, `asuna sao`, `sinon sao`, `alice zuberg`, `eugeo sao`,
  `aincrad`, `underworld sao`, `alfheim`.
- API Openverse: `https://api.openverse.org/v1/images/?q=sword+art+online+cosplay&license_type=commercial,modification`
  y `...q=sword+art+online+figure`.
- API MediaWiki de la wiki: `action=query&titles=Knights of the Blood&prop=revisions` (wikitext con
  los nombres de archivo del emblema) y `action=query&titles=Asada Shino&prop=pageimages` (imagen
  de perfil oficial de Sinon).
- Búsquedas web (WebSearch, español e inglés): «Sword Art Online colaboración crossover Fate Grand
  Order Bandai Namco cafe temático 2024 2025», «"Sword Art Online" fondos de pantalla oficial
  wallpaper 4K sitio Aincrad ALO GGO», «"Sword Art Online" official collaboration cafe Animate ×
  event 2023 2024 2025», «Sword Art Online Integral Factor Memory Defrag collaboration crossover
  game list», «"Knights of the Blood" Sword Art Online emblem guild logo image», «manga screentone
  halftone texture pack free CC0 CC-BY brushes Clip Studio download», «"Sword Art Online" Kirito
  Asuna figura oficial Good Smile Company Kotobukiya ARTFX pose».
- Medición de hex: script Python/Pillow local en `/tmp/claude-0/trabajo/85-sao-imagen/` sobre
  imágenes descargadas de la propia wiki (no se subieron al repo, sólo quedó el hex y la fuente).

Sigue: nada obligatorio pendiente de mis puntos (1, 3, 15, 16, 19, 23) — quedan sólo extras en «No
encontré» (sitios 3D completos, wallpaper 100% oficial de Aniplex, luz de día de GGO, modelos 3D de
Alice/Eugeo).
