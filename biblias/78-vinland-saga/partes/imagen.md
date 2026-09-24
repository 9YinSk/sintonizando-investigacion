# Imagen · Vinland Saga (encargo 78)

Investigador de imagen. Puntos 1, 3, 15, 16, 19 y 23 de `ENCARGO.md`. Parte de
`partes/datos-imagen.md` (AniList, Fandom, Safebooru, Wallhaven, Sketchfab,
Openverse) y añade lo que faltaba: categorías de la wiki no consultadas por
`recolectar.py` (lugares, portadas de tomo/capítulo/revista, el artbook oficial),
colores medidos con `estilo.py`, modelos 3D genéricos de barco/casa vikinga,
texturas CC0 y colaboraciones/figuras/cosplay. Trabajo pesado en
`/tmp/claude-0/trabajo/78-vinland-saga-imagen/`.

## Hallazgos

### 1 · Arte oficial, en cantidad y variado

- Portada y banner oficiales de AniList (bx101348) · https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx101348-2fhDFPCuMNiz.jpg · ✅ (AniList + usada también por la wiki) · tamaño real no expuesto por AniList (imagen "large")
- 15 retratos oficiales de personaje en AniList (Thorfinn, Askeladd, Thorkell, Canute, Thors, Narrator, Leif Erikson, Bjorn, Ylva, Willibald, Helga, Ragnar, Anne, Halfdan, Mimi) · en `datos.json` (fuente AniList) · ✅ · buena base para secundarios, no sólo protagonistas.
- 3 key visuals oficiales de temporada 1 (750×1058, Fandom, con arte de la portada de barco entre témpanos, el grupo de Askeladd bajo la lluvia de sangre, y Thorfinn+Askeladd+Einar sobre fondo blanco) · https://static.wikia.nocookie.net/vinlandsaga/images/4/48/Vinland_Saga_Key_Visual_1.jpg · .../0/01/Vinland_Saga_Key_Visual_2.jpg · .../5/52/Vinland_Saga_Key_Visual_3.jpg · ✅ (Fandom + confirmado como pósters oficiales por ComicBook.com, "Vinland Saga Poster Hypes Season 2") · hoja `arte_01.jpg` #1-3
- 2 key visuals oficiales de temporada 2, ilustrados por el animador Raita Kazama (fondo pastel, Thorfinn y aliados) (750×1058) · https://static.wikia.nocookie.net/vinlandsaga/images/1/10/Vinland_Saga_S2_Key_Visual_1.png · .../7/7b/Vinland_Saga_S2_Key_Visual_2.png · ✅ (Fandom + Facebook oficial VinlandWorld) · hoja `arte_01.jpg` #4-5
- Portadas de tomo (manga, Kodansha "Afternoon KC"): Volumen 1 (840×1200), 10 (610×880), 20 (1011×1440), 27 (1055×1500) · https://static.wikia.nocookie.net/vinlandsaga/images/b/b1/Volume_1.jpg (y análogos) · ✅ (son ediciones publicadas, confirmadas en la propia wiki y en librerías) · hoja `arte_01.jpg` #8-11
- Portada del capítulo 1 (webcómic, 1607×1200) y portada de revista Afternoon 2019-08 (anuncio del anime, 1080×1551) y Afternoon 2006-10 (primera aparición en revista, 347×500) · https://static.wikia.nocookie.net/vinlandsaga/images/c/cc/Chapter_001.jpg · .../d/0/Afternoon_2019-08.jpg · ✅ · hoja `arte_01.jpg` #12-13
- Artbook oficial **"Vinland Saga Animation Works"** (WIT Studio, 2020, 272 páginas: diseños de personaje, arte de fondos, props, comentarios de staff) · portada 1390×1964 https://static.wikia.nocookie.net/vinlandsaga/images/0/04/VinlandSagaWITAnimationWorksCover.png · ✅ (Fandom + ficha en eBay "VINLAND SAGA ART BOOK ANIME WIT STUDIO 2020" + MyFigureCollection.net) · hoja `arte_01.jpg` #7
  - 3 páginas de muestra descargadas y miradas: **hoja de diseño de color de Thorfinn** (turnaround frente/espalda/cuerpo entero con su traje de granjero del arco de Vinlandia, 12 expresiones y detalle de ojo) · https://static.wikia.nocookie.net/vinlandsaga/images/9/94/AnimationWorksPreview_Thorfinn.png (1500×1059) · paleta medida con `estilo.py`: #BAA16E (caqui capucha), #E4CCAD (crema luces), #7E6A46 (sombra), #443A2D (línea/oscuro) — el traje de granjero, no el de vikingo joven.
  - **hoja de diseño de personaje de Askeladd** (turnaround con armadura de cuero sin mangas y hombreras metálicas, versión "con heridas de flecha" del arco de Inglaterra, dos sets de expresiones) · https://static.wikia.nocookie.net/vinlandsaga/images/c/c7/AnimationWorksPreview_Askeladd.png (1500×1059) · línea gris sin colorear (concept art) · hoja `fondos_01.jpg` no, ver imagen directa citada.
  - **correcciones de dirección de animación** de Takahiko Abiru sobre Thorfinn adolescente en el Arco de la Guerra (hacha, daga, gestos de furia) · https://static.wikia.nocookie.net/vinlandsaga/images/c/cb/AnimationWorksPreview_Thorfinn2.png (1500×1059)
  - 3 páginas más de fondos/props del mismo artbook, ver punto 16.
- Figura oficial **figma Thorfinn** (Good Smile Company, nº 608, ~145 mm, ropa de tela real, caras intercambiables y dagas) anunciada 30-may-2023, salió feb-2024 · https://www.goodsmile.com/en/product/12106/figma+Thorfinn · imagen de producto: http://images.goodsmile.info/cgm/images/product/20230525/14421/115784/medium/eb50ff9ce2f5d562b420a52397b2aa63.jpg (250×250, "medium"; hay tamaños mayores en la ficha) · ✅ (goodsmile.com + hobby-genki.com) — sirve de referencia de pose/color oficial además de figura.
- ⚠️ No encontré portadas de Blu-ray/DVD sueltas en la wiki (búsqueda `srsearch=Blu-ray` en espacio de archivos, sin resultados). Si hacen falta, mirar Amazon Japón o CDJapan a mano.

### 3 · Fan art y renders 3D como referencia

**Fan art (Safebooru, con enlace y autor/origen — nunca para pegar):**
- Thorfinn: 2663×4096 · https://safebooru.org/images/1607/9ad014051e207e675e1892a16b01552687451625.jpg · autor: https://x.com/icebuko/status/2076979563817836965 · ⚠️ (sin puntuación registrada, un solo listado)
- Thorfinn: 2560×1440 · https://safebooru.org/images/825/e7495f75df0ffd099b797c5b4012c31880a17126.jpg · autor: https://x.com/velupium/status/2041344911346139581
- Askeladd: 609×750 · 4 pts · https://safebooru.org/images/550/128a6882491efac98f651f809fcc759d4e88a65a.jpg · autor: pixiv (chicken79) http://img15.pixiv.net/img/chicken79/7467751.jpg (dato ya en `datos-imagen.md`)
- Canute: 1105×1600 · 3 pts · https://safebooru.org/images/103/3233183b9add3e1d8afae558fb730f6c38a1534a.jpeg (dato ya en `datos-imagen.md`)
- Einar: 1073×1266 · https://safebooru.org/images/4616/b2f301cef5c919058ae683d03fc74ce8112c9c12.png · autor: 4chan/a/ archivo https://i.4cdn.org/a/1740795508976049.png
- Einar: 900×558 · https://safebooru.org/images/622/261c7c12f13c956b254ffa8c6f83047219997582.jpg · autor: DeviantArt karaii "Vinland Saga Wheat" http://karaii.deviantart.com/art/Vinland-Saga-Wheat-194965245 (escena de trigo del arco de granja, muy citada por fans)
- ⚠️ Aviso: en `datos-imagen.md`, el bloque "Rasgos que más se repiten… (Danbooru)" y parte de "Fan art mejor valorado (Safebooru)" traen personajes de OTRAS series (hatsune_miku, artoria_pendragon, yakumo_yukari, inubashiri_momiji, raiden_shogun) — no son de Vinland Saga; probable arrastre de otra consulta de `recolectar.py`. Los ignoré.

**Modelos 3D con licencia libre (Sketchfab, todos CC Attribution):**
- Thorfinn's Knives From Vinland Saga · SILVER KEY · ♥15 · https://sketchfab.com/3d-models/none-10ec8a60e33b43449e835ee6e3e1d6f0
- Thorfinn's Knife · Elliott_Lowes · ♥15 · https://sketchfab.com/3d-models/none-3ac2763a9fb741b7a024b2b7b0bc4a0e
- Thorfinn's Dagger (Vinland Saga) · SMich017/Samantha Michelson · ♥8 · https://sketchfab.com/3d-models/none-0f430617c66142d283d13029bac42de4
- Snake Sword - Vinland Saga · obamazz · ♥12 · https://sketchfab.com/3d-models/none-448c5654adcf4097822473f85846ac88
- Lowpoly Model Askeladd Bonavera · Sebastian Bonavera · ♥0 · https://sketchfab.com/3d-models/none-8b98182fd8db45788399aa01e5129163 (único personaje completo en 3D que encontré con licencia)
- (genéricos, para complementar sitios del punto 16, no de la serie pero de tema vikingo real): Viking Longship · massive-graphisme · ♥285 · https://sketchfab.com/3d-models/none-3d649f8373514860b69ff6f874c0efb5 · Longboat · kreinin · ♥324 · https://sketchfab.com/3d-models/none-ecc03f0875e34a0cb2e66c40b22383e5 · Viking shaman hut · JulienSchoots · ♥153 · https://sketchfab.com/3d-models/none-eb98d1aef0fa4e01ab5584fff0c23742 · Medieval viking house · vlad_design228 · ♥25 · https://sketchfab.com/3d-models/none-1a720687cb1f4747ade741508cd505bc
- ⚠️ No hay modelo 3D con licencia libre de Thorfinn, Askeladd, Canute o Einar completos (sólo dagas/espada y un lowpoly de Askeladd). Para un busto/cuerpo, usar cosplay o figuras oficiales como referencia de volumen.

### 15 · Vestuario

- **Thorfinn**: en el Arco de la Guerra (niño soldado, ~1013-1014) capa/capucha con ribete de piel oscuro, ropa ajustada de cuero — visto en las correcciones de animación de Abiru (arriba). En el Arco de Vinlandia (granjero, 27 años) túnica con capucha caqui/beige, polainas envueltas en paja, cinturón con funda de daga — hoja de diseño de color oficial, paleta medida: #BAA16E, #E4CCAD, #7E6A46, #443A2D. Siempre lleva **dos cuchillos** (su objeto icónico, confirmado también por Sketchfab: 4 modelos distintos de su daga). Pelo: corto y despeinado toda la infancia/adultez temprana; se lo empieza a peinar hacia atrás antes de partir a Vinlandia (27 años) · fuente texto: https://vinlandsaga.fandom.com/wiki/Thorfinn#Appearance · ✅ (wiki + confirmado visualmente en el artbook)
- **Askeladd**: de niño, ropa raída sin calzado, cubierto de ceniza de sus trabajos ("el Muchacho Ceniciento"/Ashen Lad) · adulto: coraza/chaleco de cuero sin mangas con hombreras metálicas sobre túnica de manga larga, pelo rubio ondulado a la altura del mentón, perilla · hoja de diseño oficial (concept art, sin colorear) https://static.wikia.nocookie.net/vinlandsaga/images/c/c7/AnimationWorksPreview_Askeladd.png, con variante "con flechas clavadas" del final del Arco de Inglaterra. Colores de la ficha de la wiki (fondo negro, cautela ⚠️ con el peso del fondo en la medición): #6D5B42 y #D9C08D (marrón/beige de su túnica) · fuente texto: https://vinlandsaga.fandom.com/wiki/Askeladd#Appearance · ✅
- **Canute**: temporada 1, pelo rubio largo, cara casi femenina, muchos lo confunden con una chica (algunos hombres creen que es la diosa Freyja reencarnada) · temporada 2 (rey), pelo corto tipo bob, perilla, cicatriz bajo el ojo izquierdo (se la hizo Thorfinn), capa y diadema/circlet casi siempre puestos · colores medidos de las hojas de diseño oficiales del anime: S1 #9C403B (túnica rojiza), S2 #B46746 (capa terracota) · fuente texto: https://vinlandsaga.fandom.com/wiki/Canute#Appearance · ✅
- **Einar**: alto, pelo castaño rojizo (auburn), ojos cafés en el manga y azules en el anime, lunar junto al puente de la nariz, complexión musculosa por años de trabajo agrícola · color medido de su diseño S2: #7A7646 (camisa/chaqueta verde) · fuente texto: https://vinlandsaga.fandom.com/wiki/Einar#Appearance · ✅
- Método: todos los hex de esta sección salen de `herramientas/estilo.py --colores 6` sobre las imágenes oficiales bajadas a `/tmp/claude-0/trabajo/78-vinland-saga-imagen/img/` (hojas de diseño de personaje del anime/artbook, no fan art). Donde el fondo de la imagen (negro o blanco puro) domina la paleta, lo aviso con ⚠️.
- ⚠️ Ropa "icónica" que todo fan reconoce: el manto/capucha caqui de granjero de Thorfinn en Vinlandia y sus dos cuchillos — confirmado por ser la imagen de key visual de temporada 2 y la portada del artbook. No alcancé a medir hex de la armadura de Thorkell (secundario muy citado): queda para quien complete el punto 20 o una vuelta más.

### 16 · Ciudades, paisajes y fondos de pantalla

- Lugares con categoría propia en la wiki (`Category:Locations`): **Iceland**, **Jomsborg**, **Markland**, **Vinland**, **Wales**, **Arnheid Village** · https://vinlandsaga.fandom.com/wiki/Category:Locations · ✅
  - Iceland: 2 imágenes (mapa dibujado y paisaje de fiordos nevados, 1024×488 y 1000×703) · https://static.wikia.nocookie.net/vinlandsaga/images/f/f2/Iceland%282%29.jpg
  - Vinland: 3 imágenes, incluido el mapa animado del OP y un mapa "Epekwitk" (nombre real de Isla del Príncipe Eduardo, referencia histórica del lugar que inspira Vinlandia)
  - Markland: 1 mapa
  - Wales: 4 imágenes, mapas de los reinos galeses de la época (Morgannwg, Wessex) usados en el Arco de Inglaterra — 1584×1304 y 1160×754 · https://static.wikia.nocookie.net/vinlandsaga/images/d/d9/Wales.png
  - Jomsborg (base de los Jomsvikings): 8 imágenes, capturas de manga con vista aérea del fuerte circular y su plaza de mercado (Cap. 130, 138, 146) · https://static.wikia.nocookie.net/vinlandsaga/images/a/a4/Chapter_130_Screenshot.PNG (1115×808)
  - ⚠️ "Ketil's Farm" tiene página en la wiki pero **0 imágenes propias** (comprobado con `prop=images`); es donde pasa gran parte del Arco de Vinlandia — usar capturas de episodio (le toca al investigador de vídeo) o arte del artbook.
- Arte oficial de fondos del artbook "Vinland Saga Animation Works" (WIT Studio): 3 láminas de muestra, 1500×1059 cada una —**Entorno** (interior de casa larga vikinga + acantilado con playa + aurora boreal sobre el mar), **Paisaje/Escenario** (turnaround técnico del knarr/drakkar vikingo con vistas de perfil, popa y proa), y una tercera con un brazo encadenado en fundido a blanco (prop/escena) · https://static.wikia.nocookie.net/vinlandsaga/images/7/7c/AnimationWorksPreview_Environment.png · .../e/0/AnimationWorksPreview_Scenery.png · .../c/8/AnimationWorksPreview_Ship.png · ✅ · hoja `fondos_01.jpg` #8-11 (mirada directamente, no sólo el nombre)
- Fondos de pantalla más guardados en Wallhaven (todos aptos, 1920×1080 o más, con autor): ya listados en `datos-imagen.md` — repito los 3 mejor puntuados: 3840×2160 ♥143 "mushit" (minimalista, blanco y negro) https://w.wallhaven.cc/full/6d/wallhaven-6d5zgl.jpg · 1920×1080 ♥101 "nidko8" (espada/arma, blanco y negro) https://w.wallhaven.cc/full/po/wallhaven-poj76e.png · 4096×2340 ♥54 "theflyboy667" (Thorfinn con globo de diálogo en inglés) https://w.wallhaven.cc/full/1p/wallhaven-1pzgl1.png
- Paleta y luz medidas con `estilo.py` en 2 wallpapers descargados: ruinas de noche con luna (wallhaven-q6oor5, 1920×1080) → #1C394B / #152429 / #448AA1 / #65C5D9 (azul noche desaturado con acento cian en el cielo) · paisaje al amanecer (wallhaven-lmddyq, 1920×1080) → #1A3B4A / #2B5B70 / #4A7EA7 / #97B1DA (misma familia azul-verdosa, más clara). Coincide con lo que dice la wiki de Islandia como tierra fría y desolada: los fondos de pantalla más queridos por los fans son casi todos de noche o amanecer, paleta fría, muy poca saturación. Contraste: Wales/Inglaterra en los mapas y capturas de manga es blanco y negro puro (línea de manga), no da paleta de color — el color de Inglaterra hay que sacarlo de fotogramas del anime (le toca al investigador de vídeo, punto 4).
- ⚠️ No encontré fondos de pantalla oficiales (sólo de fans en Wallhaven); si el estudio publicó wallpapers oficiales de promoción, no aparecieron en las búsquedas hechas (Fandom, AniList, Wallhaven).

### 19 · Texturas 2D

- Tramas de manga (screentone) visibles en las portadas de capítulo/tomo y en las capturas de Jomsborg (Cap. 130/138/146): predominan puntos finos para sombra de piedra/nieve y líneas rectas paralelas para agua — mirado directamente en `img/` (arriba) y en la hoja `fondos_01.jpg`.
- Texturas reales libres (CC0, ambientCG, para capas de "papel", tela y piel de la lámina):
  - Papel: **Paper001** (grano de papel) · https://ambientcg.com/view?id=Paper001 · CC0
  - Tela (lana/lino, para túnicas): **Fabric081C**, **Fabric061** · https://ambientcg.com/view?id=Fabric081C · https://ambientcg.com/view?id=Fabric061 · CC0
  - Cuero (armadura de Askeladd, cinturones): **Leather037**, **Leather030** · https://ambientcg.com/view?id=Leather037 · CC0
  - Metal (hombreras, hebillas, hachas): **Metal063**, **Metal049A** · https://ambientcg.com/view?id=Metal063 · CC0
- Pinceles/texturas de screentone libres para Photoshop/Clip Studio (equivalente a la trama del manga): Brusheezy "34 Free Hi-Res Screentone Halftone Brushes" (gratis) https://www.brusheezy.com/brushes/50379-mabecman-s-screentones-halftone-brushes · Photoshop Supply "+35 Halftone Textures, Patterns, Brushes & Action" (gratis, uso personal y comercial con atribución) https://www.photoshopsupply.com/patterns-textures/halftone-texture · ✅ (dos catálogos independientes)
- ⚠️ Emblemas o logos de grupo (heráldica de bandas/reinos): busqué `srsearch=emblem`, `symbol` y `banner` en el texto de la wiki (`action=query&list=search&srwhat=text`) y no aparece un emblema ficticio propio de ningún bando (Jomsvikings, banda de Askeladd, ejército de Canute) más allá de motivos vikingos históricos reales (barcos, hachas). El único "logo" reconocible es el rótulo del título "VINLAND SAGA" que aparece en todas las portadas de tomo/capítulo ya citadas en el punto 1 — la letra exacta le toca al investigador de texto (punto 5).

### 23 · Colaboraciones y cruces

- **Assassin's Creed Valhalla × Vinland Saga**: cómic crossover oficial de una entrega, dibujado y escrito por el propio Makoto Yukimura, publicado en la web de Ubisoft Japón el 23-oct-2020 · https://comicbook.com/anime/news/assassins-creed-vinland-saga-manga-crossover/ · https://assassinscreed.fandom.com/es/wiki/Assassin's_Creed:_Valhalla_x_Vinland_Saga · ✅ (dos fuentes independientes)
- **The Northman (película, 2022) × anime de Vinland Saga**: colaboración oficial con video promocional, con los actores de doblaje japonés Yūto Uemura (Thorfinn) y Kenshō Ono (Canute) · https://www.animenewsnetwork.com/interest/2023-01-05/vinland-saga-the-northman-come-together-for-the-ultimate-viking-crossover/.193451 · https://codigoespagueti.com/noticias/anime/vinland-saga-the-northman-tienen-genial-colaboracion-oficial/ · ✅
- **Zombieland Saga × Vinland Saga**: ilustración crossover publicada por la cuenta oficial de Zombieland Saga para celebrar el estreno del anime de Vinland Saga · https://www.anmosugoi.com/de-interes/zombieland-saga-estrena-una-ilustracion-crossover-con-vinland-saga/ · ⚠️ (una sola fuente encontrada, no confirmé en una segunda)
- **Colaboración con la prefectura de Saga** ("Sagaprise!", proyecto de revitalización regional): campaña "Vinland Saga (佐賀)" con el evento principal "Búsqueda de Vinlandia: Gran Rally de Sellos Misteriosos del Viaje", en Akihabara (Tokio) del 3 al 18-oct-2019, más una exposición en Tokio con materiales de producción (diseños de personaje, dibujos originales, arte de fondos) hasta el 5-oct · https://www.animenewsnetwork.com/interest/2019-09-17/vinland-saga-vikings-enjoy-saga-prefecture-bounty/.151221 · https://animeanime.global/2019/09/24/48410.html · ✅
- **Figura oficial** figma Thorfinn (Good Smile Company nº608, ~145 mm, ropa de tela real, caras y dagas intercambiables), anunciada 30-may-2023, salió feb-2024 — su pose de cuerpo entero es una referencia 3D/volumen fiable · https://www.goodsmile.com/en/product/12106/figma+Thorfinn · https://hobby-genki.com/en/figma/18144-figma-thorfinn-vinland-saga-action-figure-limited-edition-4545784068939.html · ✅
- **Cosplay bien hecho** (materiales y volumen reales, no dibujado): foto de cosplay de Askeladd, 819×1024, CC BY-NC 2.0, autor plumvs-photo · https://live.staticflickr.com/65535/52593952796_33fbe2f334_b.jpg (ya en `datos-imagen.md`) · lista de materiales típicos de un cosplay de Thorfinn (peluca rubia desordenada, ribete de piel marrón, túnica beige tipo vikingo, cinturón con hebilla plateada, daga de utilería) según guía de Carbon Costume https://carboncostume.com/thorfinn-from-vinland-saga/ · ⚠️ (guía de referencia, no fotos propias verificadas en dos fuentes)
- ⚠️ No hay videojuego oficial de la franquicia Vinland Saga (busqué "Vinland Saga videojuego/juego móvil"): "Dead in Vinland" es un juego francés de gestión SIN relación con esta obra (ambientación vikinga genérica, otro estudio) — **no confundir los dos**, aviso porque el nombre es parecido. El cruce con videojuegos más cercano sigue siendo el cómic de Assassin's Creed Valhalla de arriba.

## Lo mejor para la lámina

- La hoja de diseño de color oficial de Thorfinn granjero (artbook WIT Studio) da turnaround completo + 12 expresiones + su paleta caqui/crema exacta: es la referencia más fiable para pose y color de cuerpo entero.
- Los key visuals de ambas temporadas (750×1058, alta calidad) sirven para recortar poses de grupo o solas sin depurar mucho.
- Las 3 láminas de fondo del mismo artbook (interior de casa larga + aurora + turnaround del barco) son oro para dibujar un sitio real "tipo Vinland Saga" en Blender.
- El modelo 3D CC de "Longboat"/"Viking Longship" (Sketchfab) es la base más práctica para un barco en 3D con licencia, ya que no hay modelo del barco exacto de la serie.
- Paleta fría azul-noche (#1A3B4A / #2B5B70 / #448AA1) de los paisajes más queridos por los fans: usarla de fondo de cualquier lámina para que "huela" a Vinland Saga sin necesitar personaje.

## No encontré

- ⚠️ Portadas de Blu-ray/DVD sueltas (busqué en archivos de la wiki, sin resultado; no insistí fuera de la wiki por presupuesto de búsquedas).
- ⚠️ Modelo 3D con licencia libre de Askeladd, Canute o Einar de cuerpo entero (sólo dagas/espada de Thorfinn y un lowpoly simple de Askeladd).
- ⚠️ Fondos de pantalla oficiales de estudio/editorial (sólo encontré de fans en Wallhaven).
- ⚠️ Emblemas o heráldica ficticia de bandas/reinos (busqué "emblem", "symbol", "banner" en el texto de la wiki); la serie no parece usarlos más allá de motivos vikingos reales.
- ⚠️ Imágenes propias en la página de "Ketil's Farm" (0 resultados en `prop=images`), pese a ser un sitio central del Arco de Vinlandia.
- ⚠️ Segunda fuente para el crossover con Zombieland Saga (sólo un sitio lo cubre en las búsquedas hechas).

## Bitácora de búsqueda

- Fandom (API `action=query`, inglés): `list=categorymembers` sobre `Category:Locations`, `Category:Weapons` (vacía), `Category:Merchandise` (vacía), `Category:Media`, `Category:Volumes`, `Category:Gallery` (vacía); `list=allcategories` completo (dos tandas, A-R y S-Z); `prop=images` sobre Iceland, Vinland, Jomsborg, Markland, Wales, Ketil's Farm, Jomsvikings, Vinland Saga Animation Works, Season 2, Vinland Saga (anime); `prop=imageinfo&iiprop=url|size` sobre ~25 archivos sueltos (tomos, capítulos, revistas, key visuals, artbook, lugares); `list=search&srwhat=text` con "emblem", "symbol", "banner" (sin resultados útiles) y `srsearch=Blu-ray&srnamespace=6` (sin resultados); `action=parse&prop=sections` y `prop=wikitext&section=1` sobre Thorfinn (Appearance completo).
- Safebooru (API `page=dapi`, inglés): tags `thorfinn`, `thorfinn_thorsson`, `einar`, `vinland_saga`, ordenados por puntuación.
- Sketchfab (API `v3/search`, inglés): `Vinland Saga Thorfinn`, `viking longship`, `viking village hut`.
- ambientCG (API `v2/full_json`, inglés): `Fabric`, `Wood`, `Leather`, `Metal`, `Paper` (CC0).
- goodsmile.info (curl directo): og:image de la ficha del figma Thorfinn.
- Búsqueda web (inglés/español, 6 usadas de la cuota ~50): "Vinland Saga colaboración anime crossover café evento" (es) · "Vinland Saga collaboration cafe event Japan" (en) · "Vinland Saga Thorfinn figura oficial Good Smile Company Pop Up Parade" (es) · "Vinland Saga cosplay Thorfinn armor build tutorial" (en) · "Vinland Saga artbook Vinland Saga Exhibition illustration key visual season 2" (en) · "Vinland Saga videojuego juego móvil app" (es) · "free manga screentone halftone texture pack Photoshop license free" (en).
- Imágenes miradas de verdad (Read, no sólo listadas): hoja de contacto `herramientas/referencias/vinland-saga/hoja_01.jpg` (17 imágenes de personajes); hojas propias `hojas_fondos/hoja_01.jpg` (15 fondos/mapas/paisajes) y `hojas_arte/hoja_01.jpg` (15 portadas/key visuals); `AnimationWorksPreview_Thorfinn.png` y `_Askeladd.png` y `_Thorfinn2.png` en grande.
- Colores medidos con `herramientas/estilo.py --colores 6`: 5 hojas de diseño de vestuario (Askeladd, Canute×2, Einar, Thorfinn granjero) + 2 mapas/paisajes (Iceland, Wales) + 2 wallpapers de Wallhaven (ruinas de noche, amanecer) + retratos AniList de Thorfinn/Askeladd + 1 captura de Einar.

Sigue: nada obligatorio pendiente de los puntos 1, 3, 15, 16, 19 y 23. Si hay
más tiempo: buscar portadas de Blu-ray a mano (Amazon Japón/CDJapan), una
segunda fuente para el crossover con Zombieland Saga, y un modelo 3D con
licencia de Askeladd o Canute más elaborado que el lowpoly encontrado.
