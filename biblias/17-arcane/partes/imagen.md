# Parte · Imagen — Arcane (repaso)

Investigador de imagen. Puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md. Parto de
`datos-imagen.md` (ya recolectado) y de `biblia.md` §§3-5, 16-17 (ya escritos
en la primera pasada, con red cerrada). Esta pasada tiene la red abierta:
corro `investigar_serie.py` (antes daba error), confirmo licencias por API
(Sketchfab, Poly Haven, ambientCG) y abro páginas bloqueadas con `navegar.py`.
No repito lo que la biblia ya tiene bien: añado lo nuevo y resuelvo ⚠️.

---

## 1 · Arte oficial, en cantidad y variado

- **Carteles de personaje de la T2** (antes ⚠️ «no pude abrirlos»): confirmado
  y descrito. El de **Vi** lleva una **diana de grafiti pintada en su
  espalda** (la marca de Jinx); el de **Jinx**, apuntando, compuestos para
  leerse juntos: hermana contra hermana · [The Mary Sue](https://www.themarysue.com/netflix-drops-arcane-season-2-character-posters/) ✅ (con
  [CGMagazine](https://www.cgmagonline.com/news/new-arcane-season-2-poster-dropped/) sobre el cartel grupal) · sirve para el concepto «Vi y Jinx
  enfrentadas» de una lámina 2.
- **Cartel de Silco** (`Silco_Season_1_Poster_1.jpg`, 2025×3000): de perfil,
  mitad cara humana mitad textura de madera/metal verde (la cicatriz química
  cubre media cara), sosteniendo una jeringa de Shimmer morada que ilumina
  de rosa su mano; detrás, en transparencia, **su despacho de The Last
  Drop** con una lámpara Tiffany naranja ✅ (mirado directamente).
- Confirmado por pixel: **el oro de los escudos de Piltóver y Zaun es el
  mismo tono**, `#C7A965` (medido en `Piltover_Crest.png` y `Zaun_Crest.png`,
  4042×4167 y 3487×4167, fondo transparente de verdad — alfa 0-255) ✅. Antes
  la biblia sólo tenía el oro de la splash de Jayce (`#B4843C`, más oscuro
  por la iluminación de la escena); éste es el oro «de catálogo», sin luz
  encima: mejor para un grabado o un sello.
- `herramientas/investigar_serie.py` **sí corrió esta vez** (antes daba
  error de red): 7 páginas de personaje, **268 imágenes grandes** en 6 hojas
  de contacto. Las miré todas (sección aparte, abajo).

## 3 · Fan art y renders 3D

Licencias confirmadas por la API de Sketchfab (`api.sketchfab.com/v3/search`),
repasando uno por uno los ⚠️ de la biblia §4.1:

- Orivers - Hextech Gauntlet - Arcane (Frayseur): **CC Attribution** ✅ confirmado
- Orivers - Hextech hammer - Arcane (Frayseur): **CC Attribution** ✅ confirmado
- Arcane Jayce Hammer (KarmaDiya): **CC Attribution** ✅ confirmado
- **Game Ready - Arcane - Jinx's Grenade** — el autor real es
  **AllanJayBranscombe** (no «Allan-Jay Branscombe» con guion, es el
  usuario), licencia **CC Attribution** ✅ confirmado ·
  [Sketchfab](https://sketchfab.com/3d-models/none-82b0959b18524af2a6311586183bd8f7)
- Arcane Vi Gauntlet Fanart (potias): **CC Attribution-NonCommercial-NoDerivs** ✅ confirmado (para referencia, no para pegar)
- Poly Haven **Spray Paint Bottles**: autor **James Ray Cock**, **CC0** ✅ (API `polyhaven.com/info/spray_paint_bottles`)
- Poly Haven **Painted Brick**: autor **Amal Kumar**, **CC0** ✅ (API `polyhaven.com/info/painted_brick`)

Modelos nuevos encontrados (con licencia ya confirmada por la API, no sólo
por el buscador):
- **Vi Arcane Gauntlet**, karmadiya, CC Attribution ✅ · [Sketchfab](https://sketchfab.com/3d-models/none-16863169437d4050b307b9be759fe08a)
- **Vi Gauntlet - League of Legends**, Gustavo_Ribeiro, CC Attribution ✅ · [Sketchfab](https://sketchfab.com/3d-models/none-46092034259442ec91346f202fb2393e)
- **Chibi Vi – Arcane 3D Print Ready**, sergei_8888, CC Attribution ✅ · [Sketchfab](https://sketchfab.com/3d-models/none-936a0976aab94e9ca9a7148aa1f11cf5) — sirve de referencia de proporciones «chibi»
- **Jin'x Grenade GAME READY**, pipaboba530, CC Attribution ✅ · [Sketchfab](https://sketchfab.com/3d-models/none-3db9ceaa9516460f9e53d59c7ced90f2)

## 15 · Vestuario

| Personaje | Prenda | Hex medido | De qué imagen |
|---|---|---|---|
| Piltóver/Zaun (insignia, ambos escudos) | Oro del emblema grabado | `#C7A965` | `Piltover_Crest.png` y `Zaun_Crest.png` (fondo transparente, medido en 4042×4167 y 3487×4167) |
| Vi (cartel T2) | Fondo de su cartel individual: gris frío detrás, con la diana de grafiti en la espalda | descripción, sin hex fiable (cartel muy oscuro) ⚠️ | [The Mary Sue](https://www.themarysue.com/netflix-drops-arcane-season-2-character-posters/) |
| Silco | Camisa granate + jeringa de Shimmer que tiñe la mano de rosa | sin hex fiable: la única imagen abierta va teñida de verde de escena (`Silco_Season_1_Poster_1.jpg`) o casi negra por la luz nocturna (`Silco speaking to Marcus.png`) ⚠️ | descrito de la wiki: «maroon dress shirt… black and dark red-purple vest with gold accents, white tie» ([arcane.fandom.com/wiki/Silco](https://arcane.fandom.com/wiki/Silco#Appearance)) |

El resto de personajes (Jinx, Vi T1, Jayce, Viktor, Caitlyn, Ekko) ya está
medido y con ✅ en biblia §16: no repito esas filas, sólo añado la del
escudo y la de Silco, que faltaban.

## 16 · Ciudades, paisajes y fondos de pantalla

Sin cambios de fondo respecto a biblia §17 (ya ✅ con tamaño y autor). Un dato
nuevo: los **8 pop-ups oficiales** de RiotX/Arcane (ver §23) son fondos y
sitios **reales, con la estética de Piltóver/Zaun montada en tiendas**, así
que sirven de referencia de cómo Riot lleva la paleta a un espacio físico —
lo anoto aquí y lo desarrollo en §23.

## 19 · Texturas 2D

No estaba en la biblia (se añadió el 24-sep, después de la primera pasada).
Es enteramente mío: tramas, grano, pinceladas, patrones de ropa, emblemas —
con enlace a un recurso descargable y su licencia.

**Emblemas y logos** (los propios, del wiki, listos para usar como sello o estampado):
- `Piltover_Crest.png` y `Zaun_Crest.png`, 4042×4167 y 3487×4167, **PNG con
  fondo transparente de verdad**, oro `#C7A965` medido por mí ✅ · arte
  oficial de Riot, vía Fandom (mismo uso que cualquier imagen de la wiki,
  con crédito) · sirve de sello grabado en los planos de Hextech o de
  emblema de bando en la pared de Jinx.
- Logo «ARCANE» de los carteles (tipografía dorada en relieve, ver §6 de la
  biblia, no es mío repetirlo).

**Grano de papel / textura de los planos Hextech** (CC0, medida por su API):
- **Paper006** (ambientCG), papel beige-marrón, PBR completo (color, rugosidad,
  normal) · **CC0** ✅ · [ambientcg.com/a/Paper006](https://ambientcg.com/a/Paper006)
  — el color base es muy parecido al `#B39A84` que ya midió la biblia en el
  mapa-plano de RiotX; sirve de textura base para «envejecer» el plano en
  Photoshop o como *material* en Blender.

**Metal y superficies de Zaun/Piltóver** (CC0, por la API de ambientCG):
- **Metal063** (metal oscuro envejecido, `aged/dark/brown`) · CC0 ✅ · [ambientcg.com/a/Metal063](https://ambientcg.com/a/Metal063) — tuberías y máquinas de Zaun.
- **Metal041B** / **MetalWalkway014** (hierro oxidado, pasarela oxidada) · CC0 ✅ · [ambientcg.com/a/Metal041B](https://ambientcg.com/a/Metal041B) · [ambientcg.com/a/MetalWalkway014](https://ambientcg.com/a/MetalWalkway014) — óxido de Zaun.
- **DiamondPlate009** (chapa de metal estriada, tipo piso industrial) · CC0 ✅ · [ambientcg.com/a/DiamondPlate009](https://ambientcg.com/a/DiamondPlate009) — suelos y mesas de laboratorio.
- **Metal049A** (metal limpio plateado, la base más cercana a un latón sin
  pulir que tiene ambientCG; no hay «brass» exacto en su catálogo) · CC0 ⚠️
  (aproximado, no es latón) · [ambientcg.com/a/Metal049A](https://ambientcg.com/a/Metal049A)

**Patrón de tela** (para el chaleco a cuadros de la clase alta de Piltóver o
un forro):
- **Fabric060** y **Fabric054** (patrón tartán/cuadros) · CC0 ✅ ·
  [ambientcg.com/a/Fabric060](https://ambientcg.com/a/Fabric060) ·
  [ambientcg.com/a/Fabric054](https://ambientcg.com/a/Fabric054)
- **Leather037** (cuero marrón limpio, como los guantes de Jayce o la
  chaqueta de Caitlyn T1) · CC0 ✅ · [ambientcg.com/a/Leather037](https://ambientcg.com/a/Leather037)

**Pinceladas / pintura a mano** (el estudio pinta las texturas a mano sobre
el 3D, biblia §3.6): pinceles libres que imitan ese acabado:
- **106 Concept Art Brushes** (MyPhotoshopBrushes), pack .abr con texturas
  orgánicas, licencia **"Free for Commercial Use"** en la propia página ✅ ·
  [myphotoshopbrushes.com/brushes/id/3570](https://myphotoshopbrushes.com/brushes/id/3570/)
- **Grunge y grit brushes** — el propio Adobe publica un pack gratis
  («Alejandro Chavetta») en su web oficial, de uso libre ✅ ·
  [adobe.com — 72 free grunge and grit brushes](https://www.adobe.com/learn/photoshop/web/372-free-grunge-and-grit-brushes-for-photoshop)
  — sirve para el chisporroteo pintado a mano de los efectos de Jinx (biblia §3.6).

**Tramas / screentones** (Arcane no es manga, pero el encargo pide esta capa
para toda la serie; útil si se hace un cómic-lámina o una viñeta estilo
manga dentro del canal #arte):
- **[FREE] Manga Screentone Pack 1**, Clip Studio Assets, marcado «FREE» en
  la propia ficha ✅ · [assets.clip-studio.com/en-us/detail?id=2142037](https://assets.clip-studio.com/en-us/detail?id=2142037)

## 23 · Colaboraciones y cruces

No estaba en la biblia. Todo confirmado con dos fuentes (oficial + prensa
especializada), con fecha:

**Videojuegos (crossovers, con ropa y poses nuevas)**
- **Fortnite** (Gaming Legends Series): **Jinx** el 4-nov-2021 (con el
  hacha Pow Pow Crusher y el accesorio Dream Monkey), **Vi** en enero de
  2022 (con el martillo Piltover Warhammer) ✅ ·
  [exitlag.com](https://www.exitlag.com/blog/arcane-fortnite/) ·
  [ComicBook](https://comicbook.com/gaming/news/fortnite-skin-vi-arcane/)
  — **regresó** en 2025 con ambas skins otra vez ·
  [esportsinsider.com](https://esportsinsider.com/2025/11/fortnite-arcane-jinx-vi-skins-collaboration-return)
- **PUBG Mobile**: colaboración desde el **16-nov-2021** con **Jinx, Vi,
  Jayce y Caitlyn** jugables, más el vehículo volador «PowPow Flying
  Machine» de Jinx ✅ · [oneesports.gg](https://www.oneesports.gg/league-of-legends/champions-arcane-pubg-mobile/) ·
  post oficial de [@PUBGMOBILE en X](https://x.com/PUBGMOBILE/status/1455550081084493832)

**Con otra marca de juego de mesa**
- **Magic: The Gathering — Secret Lair x Arcane** (Wizards of the Coast),
  dos tandas: cartas clásicas rediseñadas con escenas de Vi, Jinx y Jayce
  (p. ej. Rhystic Study, Path to Exile), y una segunda con **tierras
  básicas** pintadas con los sitios de Piltóver y Zaun ✅ · oficial:
  [secretlair.wizards.com/us/en/product/696669/secret-lair-x-arcane](https://secretlair.wizards.com/us/en/product/696669/secret-lair-x-arcane) ·
  [businesswire.com](https://www.businesswire.com/news/home/20221019005346/en)
  — las tierras son referencia extra de paisaje pintado para el punto 16.

**Ropa y merchandising con marca**
- **tokidoki × Arcane** (colección «League of Legends»): mochila con
  personajes en el estilo *kawaii* de tokidoki (Caitlyn, Ekko,
  Heimerdinger, Jayce, Jinx, Mel, Silco, Vi, Viktor), lanzada el
  17-oct-2024, US$80 ✅ · oficial: [merch.riotgames.com — tokidoki x Arcane backpack](https://merch.riotgames.com/en-us/product/tokidoki-arc-backpack/) ·
  [tokidoki.it — colección](https://www.tokidoki.it/collections/tokidoki-x-arcane-restock)
  — la imagen ya está en `datos-imagen.md` (`Tokidoki_Backpack.png`,
  818×850) y en la hoja `colaboraciones_merch_01.jpg`, nº 245.
- **Sudaderas con frases del doblaje** (Viktor «In the pursuit of great, we
  failed to do good», y una doble «Jayvik») en la Riot Games Store ✅
  (imágenes de la propia wiki, `Viktor_Quote_HT_Hoodie.jpg` y
  `Jayvik_Hoodie.png`) — sirven de ejemplo de cómo la marca ya convierte una
  frase del guion en objeto de tela: útil para pensar el canal #arte.

**Figuras oficiales** (pose = referencia 3D real)
- **Nendoroid Jinx (Arcane Ver.), nº 2678** — Good Smile Arts Shanghai /
  **Good Smile Company**, en colaboración con Riot Games; salió en
  sept-2025 (¥7182 en Japón); trae 3 caras intercambiables (burlona, de
  locura, seria) y el arma Rhino ✅ · oficial:
  [goodsmile.com/en/product/61630](https://www.goodsmile.com/en/product/61630/Nendoroid+Jinx+Arcane+Ver.+) ·
  venta oficial: [merch.riotgames.com — Nendoroid Jinx](https://merch.riotgames.com/en-us/product/nendoroid-jinx-arcane-version/)
- **Youtooz — Vi & Jinx** (set «Lookin' good, Sis»), figuras de vinilo,
  **con licencia oficial**; Jinx con su Gatling gun, Vi con los guanteletes
  en alto ✅ · oficial: [youtooz.com/products/vi-and-jinx](https://youtooz.com/products/vi-and-jinx)
  · reventa verificada: [Amazon](https://www.amazon.com/Youtooz-Collectibles-Jinx-and-Vi/dp/B0DW9H5GRV)
  — imágenes en `datos-imagen.md`/wiki: `Vi_Jinx_Youtooz.png` (1141×747) y
  `Jinx_Youtooz.png` (741×747), hoja nº 186 y 263.
- **Funko Pop Jinx y Viktor** (`Jinx_Pop.png` 747×744, `Viktor_Pop.png`
  800×800, en la wiki) — existencia confirmada por la propia imagen oficial
  de la wiki ✅; no encontré ficha de Funko con fecha exacta ⚠️.

**Eventos y espacios físicos (RiotX Arcane)**
- **Cafés/exhibiciones pop-up** con la estética de la serie: **Seúl**
  (barrio Seongsu-dong, oct-2024, mural exterior de Vi y Jinx, galería de
  arte, pared de grafiti digital, prensa de serigrafía para bolsas) ✅ ·
  [dotesports.com](https://dotesports.com/league-of-legends/news/arcane-experience-exhibition-pop-up-held-at-cafe-in-korea)
  — **Yakarta** (Gandaria City Mall, con el escondite de Jinx reconstruido
  y **concurso de cosplay**) ✅ · página oficial:
  [arcane.com — Watch, Play, Experience](https://www.arcane.com/en-us/news/announcements/watch-play-experience-heres-how-were-celebrating-arcane-season-2-across-the-globe/)
  — **tiendas pop-up** en París, Londres, Madrid, Estambul, Los Ángeles y
  Singapur (misma fuente oficial) ✅.
- **Concurso oficial de cosplay** de Riot (acepta League, Arcane o
  Runeterra): top 3 por categoría se lleva mercancía + 10 000 RP; el gran
  campeón, US$5000 y viaje a Worlds ✅ · reglas oficiales:
  [merch.riotgames.com/en-us/arcane-contest-rules](https://merch.riotgames.com/en-us/arcane-contest-rules/)
  — sirve para pensar una etiqueta «Acepto encargos» de #arte con el
  espíritu de un concurso real de la marca.

## Las hojas de contacto

`investigar_serie.py --serie "Arcane" --wiki arcane --paginas "Jinx" "Vi"
"Jayce Talis" "Viktor" "Caitlyn Kiramman" "Ekko" "Silco"` — 268 imágenes
grandes de la wiki en 6 hojas (`herramientas/referencias/arcane/hoja_01..06.jpg`).
Las miré las 6 enteras. Dejo 3 en `hojas/` (las más útiles para mis puntos;
las otras 3 se pueden regenerar con el mismo comando si algún otro punto las
necesita):

- **`hojas/arte_modelos_01.jpg`** (hoja_02 original, números 49-96): **hojas
  de modelo oficiales** — nº 70 (Jayce, boceto de color con la paleta al
  lado), nº 75 (el Heraldo, escultura gris de turnaround), nº 77-79 (el pelo
  de Caitlyn en 5 ángulos), nº 86 (turnaround completo con 5 poses de baile,
  cartel «ARCANE»), nº 93 (bustos de personal del Consejo). Es la prueba
  visual de que el estudio trabaja con hojas de modelo de verdad: sirve para
  el punto 1 («hojas de modelo») y como referencia de proporciones si se
  monta algo en Blender.
- **`hojas/colaboraciones_figuras_01.jpg`** (hoja_04 original, números
  145-192): nº 150 (portada del cómic promocional de Jayce), nº 157-159 (tres
  vistas de concepto del Heraldo/criatura), nº 163 (render S2 de Jayce), nº
  182 (**Nendoroid Jinx**), nº 183 (sudadera con la cita de Viktor), nº 186
  (**Youtooz Vi y Jinx**), nº 187 (sudadera Jayvik), nº 188-189 (figuras de
  Jinx). Todo el material de §23 en una sola hoja.
- **`hojas/colaboraciones_merch_01.jpg`** (hoja_06 original, números
  241-268): nº 245 (**mochila tokidoki × Arcane**), nº 252 (Funko Viktor),
  nº 260-261 (turnaround oficial del modelo de Ekko, de frente y de perfil,
  webp), nº 262 (Funko Jinx), nº 263 (**Youtooz Jinx** suelta).

Las otras 3 hojas (`hoja_01`, `hoja_03`, `hoja_05`, no copiadas a `hojas/`)
tienen sobre todo fotogramas de escena (para el punto 2/13/14 del
investigador de vídeo y voz) y los carteles/splash arts que ya están
citados con su enlace directo de GitHub en biblia §3.1, así que no hacía
falta duplicarlas aquí.

## Lo mejor para la lámina

- El **escudo de Piltóver** (`Piltover_Crest.png`, fondo transparente,
  oro `#C7A965` exacto): grabado directo sobre el plano de Hextech de
  Jayce y Viktor, sin recortar nada.
- **Nendoroid Jinx** y **Youtooz Vi&Jinx**: son objetos 3D reales, con pose
  fija y licencia de marca — mejor referencia de volumen que cualquier fan
  art para una figura en Blender.
- Las **hojas de modelo oficiales** (nº 70, 75, 77-79, 86 de
  `arte_modelos_01.jpg`): turnarounds de verdad del estudio, con paleta al
  lado en el caso de Jayce.
- **Paper006** de ambientCG (CC0) para el grano del papel de los planos,
  compatible con el `#B39A84` ya medido.
- El **cartel de Silco** con la jeringa de Shimmer iluminándole la mano de
  rosa: la pose «sostener un objeto pequeño y peligroso, mirando de lado» es
  reutilizable para cualquier personaje que explique un secreto.

## No encontré

- **Hex fiable de la ropa de Silco**: las dos imágenes que pude abrir
  llevan luz de escena muy fuerte (verde de cartel, casi negro nocturno).
  Búsqueda: `Silco vestuario hex`, `Silco appearance colors` (inglés) — sin
  una imagen neutra no mido un color inventado.
- **Ficha oficial con fecha de los Funko Pop** de Jinx y Viktor: confirmé
  que existen (imagen de la propia wiki) pero no encontré la página de
  Funko con el número de la línea ni la fecha de salida. Búsqueda: `Funko
  Pop Arcane Jinx Viktor official release` (inglés).
- **Autor y licencia exacta** de «Alexia Ferry — Arcane Hextech Lab»
  (ArtStation): existe (ya en biblia §3.5), pero es arte de referencia, no
  descargable, así que no aplica al punto 3.

## Bitácora

- Corrí `herramientas/investigar_serie.py --serie "Arcane" --wiki arcane
  --paginas "Jinx" "Vi" "Jayce Talis" "Viktor" "Caitlyn Kiramman" "Ekko"
  "Silco"` (antes daba error de red): 268 imágenes, 6 hojas. Miré las 6.
- API de Sketchfab (`api.sketchfab.com/v3/search?type=models&q=…`): 6
  búsquedas para confirmar licencias de los modelos ya listados + 2 nuevas
  búsquedas (Vi gauntlet, chibi).
- API de Poly Haven (`api.polyhaven.com/info/<slug>`): 2 consultas (autor +
  licencia de Spray Paint Bottles y Painted Brick).
- API de ambientCG (`ambientcg.com/api/v2/full_json`): 9 búsquedas (ladrillo
  pintado, metal oxidado, hormigón, chapa, cuero, tela a cuadros, papel,
  metal genérico) para las texturas del punto 19.
- Medí colores por pixel con Pillow (Python) en `Piltover_Crest.png` y
  `Zaun_Crest.png` bajados directo de Fandom (con `Referer`).
- `navegar.py` (en inglés, 2 páginas): la galería de carteles de Netflix
  Tudum (sólo dio el título, sin alt-text de las imágenes) y el artículo de
  The Mary Sue sobre esos carteles (sí sirvió, con descripción).
- Buscador web, 8 búsquedas en inglés: pinceles/grunge libres, screentone
  gratis, colaboración Fortnite, cosplay oficial, café pop-up, gacha/PUBG
  Mobile, Magic the Gathering, tokidoki, Nendoroid/Youtooz/Funko.
- No usé japonés/coreano/chino en esta parte: todo el material oficial de
  colaboraciones y merchandising que encontré está en inglés (Riot Games es
  la fuente primaria en todos los casos).
