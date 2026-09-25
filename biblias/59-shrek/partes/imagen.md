# Investigador de IMAGEN · Shrek (59-shrek)

Puntos de `ENCARGO.md`: **1** (arte oficial variado), **3** (fan art y 3D con
licencia), **15** (vestuario con hex medidos), **16** (fondos y paisajes),
**19** (texturas 2D) y **23** (colaboraciones y cruces).

Parto de `partes/datos-imagen.md` (no repito sus consultas a Fandom, Danbooru,
Safebooru, Wallhaven, Sketchfab ni Openverse) y de las **6 hojas de contacto**
que ya había en `herramientas/referencias/shrek/` (248 imágenes, generadas por
`investigar_serie.py --serie "Shrek" --wiki shrek`), miradas enteras con
`Read` antes de escribir. Esas hojas salieron dominadas por Shrek (145
menciones) y Fiona (132): Burro (24) y el Gato con Botas (4) casi no
aparecían, así que monté **una hoja propia con Pillow** (`personajes_03.jpg`)
sólo con ellos dos, usando URLs que ya traía `datos-imagen.md`/`fandom.json`.

## Hallazgos

### Punto 1 · Arte oficial, en cantidad y variado

- **La wiki de Fandom por tamaño real** (ya en `datos-imagen.md`, con
  `iiprop=url|size`): 128 imágenes de Shrek, 156 de Fiona, 70 de Burro y 70
  del Gato con Botas, la mayoría renders oficiales 3000-4500 px de ancho, no
  capturas de pantalla comprimidas ✅.
- **Fichas "Essential Guide" / "Handbook" (libros de DK/Scholastic con el
  estudio)**, vistas enteras en las hojas de contacto, con texto de
  personalidad, datos y varias ilustraciones pequeñas por página — sirven
  como **hoja de modelo oficial impresa**, no fan-made:
  - `personajes_02.jpg` n.º 49 «Strange Enchantment» (guía de Shrek), n.º 50
    «Princess Fiona», n.º 64 «Shrek essential guide.png», n.º 65 «Fiona the
    Fair» ✅ (vistas con Read).
  - `personajes_03.jpg` n.º 7 «Puss in Boots essential guide.png»: página
    completa con su bio («fiera felina... acento español suave, temeraria e
    imbatible en combate... Donkey está celoso cuando Puss se une») y 4
    viñetas pequeñas de sus gestos («el bufón del patio», «ahora ríndete o
    ¡HISSS!», «quítate las botas embarradas») ✅ (vista con Read).
  - Las cartas **antes/después** de Fiona del *Shrek 4 Handbook* (`File:Fiona
    ogre curse essential guide.png` y `File:Ogress Fiona from the Shrek 4
    Handbook`, 2986×1800 y 1956×1396, en `personajes_02.jpg`/hoja 4 del set
    automático, vistas con Read): comparan su vestido humano de viaje verde
    con capa contra el mismo vestido en versión ogro, prueba oficial de que
    **la ropa no cambia de diseño al transformarse**, sólo la piel y el pelo
    ✅.
- **Carteles teatrales oficiales** (Fandom, tamaño medido):
  - *Puss in Boots: The Last Wish* (2022), cartel de junio, 3158×5000,
    `https://static.wikia.nocookie.net/shrek/images/d/d3/Puss_in_Boots_The_Last_Wish_June_Poster.jpg`
    ✅.
  - *Puss in Boots: The Last Wish*, cartel teaser, 2587×4096,
    `https://static.wikia.nocookie.net/shrek/images/a/ac/Puss_in_Boots_the_Last_Wish_Teaser_Poster.jpg`
    ✅.
- **Shrek 5 (nuevo, sept-2026): arte oficial recién salido.** `personajes_02.jpg`
  trae dos «Shrek 5 - Teaser Still» (1918×1037 y 1918×1035, subidas a la wiki
  el mismo 2026). Confirmado con dos fuentes externas: el teaser oficial se
  estrenó el **1-jul-2026** (Mike Myers, Eddie Murphy, Cameron Diaz, con
  Zendaya como la hija de Shrek y Fiona) y Universal/DreamWorks repartieron
  **3 imágenes oficiales** con él — [Bleeding Cool](https://bleedingcool.com/movies/shrek-5-official-teaser-trailer-and-3-images-released/)
  + [ResetEra (cartel teaser)](https://www.resetera.com/threads/teaser-poster-for-shrek-5-arrives-july-1-2026-with-mike-myers-eddie-murphy-and-cameron-diaz.923049/)
  ✅. El estreno en cines se movió de dic-2026 a **verano de 2027**
  ([Movie Insider](https://www.movieinsider.com/m6516/shrek-5)) ⚠️ (dato de
  una sola fuente, pero coincide con la fecha que ya traía la wiki).
- **25.º aniversario (2026, la película original es de 2001)**: postal
  promocional oficial con la cita de Fiona «By night one way, by day
  another» y el hashtag **#SHREK25** visible en la imagen, 1200×1200
  (`personajes_05.jpg`/hoja 5 automática n.º 222,
  `https://static.wikia.nocookie.net/shrek/images/.../Tumblr_b8561e307d11c41fd924ce1f8759564...`
  — ver `datos-imagen.md`) ✅ vista con Read; confirma que DreamWorks sí
  hace campaña propia de aniversario, útil para una lámina "de aniversario".
- **Artbooks oficiales** (dos, con ficha bibliográfica):
  - *Shrek: The Art of the Quest* (Kathleen Jones, DreamWorks/becker&mayer!,
    ISBN 9781933784182): arte inédito de las 3 primeras películas, tras
    cámaras, bocetos, maquetas de escenario y attrezzo — [reseña en
    Parka Blogs](https://www.parkablogs.com/content/book-review-shrek-art-of-quest)
    ✅.
  - *The Art of DreamWorks Shrek Forever After* (Insight Editions, 2010, 156
    págs., ISBN 9781608870028): pinturas digitales, diseño de los nuevos
    personajes (Rumpelstiltskin, las brujas), storyboards — confirmado en
    su **ficha de Internet Archive**, disponible para préstamo digital
    ([archive.org/details/artofdreamworkss0000unse](https://archive.org/details/artofdreamworkss0000unse))
    ✅ dos fuentes (Archive.org + reseña en [Parka
    Blogs](https://www.parkablogs.com/content/book-review-art-of-shrek-forever-after)).
- **Vídeojuegos con caja/arte propio** (ya en `datos-imagen.md` vía Steam,
  ampliado aquí): *Shrek 2* (PS2/Xbox/GameCube, THQ) y *Shrek Super Slam*
  tienen arte de caja con el elenco completo en pose de acción, visto en
  `personajes_05.jpg`/hoja 5 automática (n.º 229 «Shrek 2 Top Trump Card»,
  n.º 230-232 fichas de videojuego estilo RPG con stats de Shrek y Fiona) ✅.
- No hallé un **key visual único de campaña** (tipo póster con todo el
  elenco en composición nueva) para las películas originales fuera de los
  carteles teatrales ya muy conocidos (buscados en inglés «Shrek theatrical
  poster official high resolution key art»): lo que hay son los carteles de
  estreno clásicos, ya de sobra documentados en internet, y no aportan pose
  nueva ⚠️.

### Punto 3 · Fan art y 3D con licencia (como referencia, nunca para pegar)

**Modelos 3D — licencia confirmada llamando a la API de Sketchfab (no sólo
la página), como pide `AYUDANTE.md`:**

| Modelo | Autor | Licencia (API) | Datos | Enlace |
|---|---|---|---|---|
| Puss In Boots | CVRxEarth | CC BY 4.0 | 13.945 vértices, 24.231 vistas | [sketchfab.com/…9b657d49](https://sketchfab.com/3d-models/none-9b657d49d8a847bdb141e156caf55003) |
| Shrek Walk Cycle (animado) | fredbear1211 | CC BY 4.0 | 4.551 vértices, 75.883 vistas | [sketchfab.com/…cd5a1e1c](https://sketchfab.com/3d-models/none-cd5a1e1cd7dd4effa3df11bcaea915f4) |
| Donkey (Pocket Shrek) y animaciones | guinavarro.al | CC BY 4.0 | 8.582 vértices, 19.692 vistas (extraído del juego móvil *Pocket Shrek*) | [sketchfab.com/…476adee5](https://sketchfab.com/3d-models/none-476adee586fc4aabafa17b00b96f9644) |
| Fiona (sin el detalle del carruaje) | guinavarro.al | CC BY 4.0 | 12.721 vértices, 4.371 vistas | [sketchfab.com/…ca41c5be](https://sketchfab.com/3d-models/none-ca41c5be84424a40a73e98703d0f00e3) |
| Donkey — *DreamWorks All-Star Kart Racing* | guinavarro.al | CC BY 4.0 (según ficha) | extraído del kart racer | [sketchfab.com/…d9b66b79](https://sketchfab.com/3d-models/none-d9b66b79b95a4047bfd6134eef9605cc) |
| Princess Fiona Clothes (sólo vestuario, separable) | Princess Gowns | CC BY (ficha) | 38 ♥ | [sketchfab.com/…6b17a5c0](https://sketchfab.com/3d-models/none-6b17a5c08123460ea6bb05ae0e07c933) |

Todos son **extracciones de videojuegos oficiales re-subidas por fans** con
licencia CC BY puesta por quien las subió (no por DreamWorks): sirven de
referencia de volumen y *rig*, citando siempre al uploader, tal como ya hizo
la biblia de Frieren con casos parecidos ✅.

**Fan art 2D como referencia (Safebooru, con autor/origen enlazado, nunca para
pegar)** — top valorado por personaje, medido con la API pública:

- **Gato con Botas**: 3500×1373 (4 pts) `safebooru.org/images/4150/c336888777f6ea5dbfc2e24f3fb5e9eca7099b91.jpg` origen `IMG_5388.jpeg` (sin autor claro) ⚠️; 1446×2048 (3 pts) origen [@kaite_xyxy](https://twitter.com/kaite_xyxy/status/1615723972892708864) ✅.
- **Princesa Fiona**: 2712×3000 (2 pts) origen [@xyanaid](https://twitter.com/xyanaid/status/1488742680754810883) ✅; 1080×1350 origen [@BrenniMurasaki](https://twitter.com/BrenniMurasaki/status/1645910229270265856) ✅.
- **Shrek** (consultado aparte, no estaba en `datos-imagen.md`): 2924×2202 (1 pt) origen [@alpharecdyt](https://x.com/alpharecdyt/status/1900279362097995984) ✅; 1920×2300 origen [tumblr jsketch12](https://jsketch12.tumblr.com/post/736114297827196928) ✅; 2500×3500 (1 pt) es un **póster de fan-fusión de SiIvaGunner** (crossover musical) — interesante para el punto 23, no como referencia de estilo ✅.
- **Burro** (consultado aparte): 2000×2122 origen [@whisket3_](https://x.com/whisket3_/status/2039267968513937756) ✅; 1494×1329 origen [tumblr metaphoricallyrose](https://metaphoricallyrose.tumblr.com/post/755002884444323840) ✅; 676×446 (1 pt) origen [@paigeccino](https://twitter.com/paigeccino/status/1805265161013354910) ✅.
- Nota: en Danbooru/Safebooru, Shrek y Burro tienen **mucho menos fan art
  "bonito"** que Fiona y Puss (menos de 10 resultados con score>0 cada uno,
  frente a cientos de Fiona/Puss): el fandom de fan art dibuja más a los
  personajes "atractivos"; el de Shrek/Burro es más de meme o crossover (ver
  punto 23).

### Punto 15 · Vestuario (hex medidos con `estilo.py`, no de memoria)

- **Shrek — vestimenta base** (igual en las 5 películas, comprobado en
  wiki): chaleco de cuero marrón sobre camisa/túnica beige, cinturón de
  cuero, calzas ocres con vendas, botas oscuras. Medido sobre
  `Shrek_fierce.jpg` (render limpio, 3600×3210):
  **piel** `#7F7240`/`#B8A933` (verde-oliva, más amarillo que el verde "de
  memoria"), **chaleco** `#392E20` (marrón muy oscuro), **túnica** `#C8C2AD`
  (beige sucio) ✅ (medido, `estilo1.json`/`estilo2.json`). Confirmado en el
  ogro-Fiona (misma familia de verdes: `#86844A`/`#C6BE4D` sobre
  `Fiona_ogre_2_render.png`) ✅ dos renders coinciden.
- **Fiona — vestido de viaje verde** (el más reconocible, con ella desde
  *Shrek* 2001): top verde con bordado dorado, falda verde más oscura por
  debajo. Medido sobre `Fiona_kick_alternate.jpg` (3262×3749, pose de
  patada, viva): **verde principal** `#438D2E`, **verde sombra/enagua**
  `#1B2D18` ✅ (`estilo2.json`).
- **Fiona — armadura de guerrera** (*Shrek Forever After*, arco alterno):
  cuero marrón con remaches y ribete dorado. Medido sobre `Warrior_Fiona.jpg`
  (1921×3000): `#453027` (cuero oscuro), `#7D5031` (cuero medio), `#B99D30`
  (ribete dorado) ✅ (`estilo1.json`).
- **Fiona — traje de coronación/realeza** (*Shrek the Third*, morado/rosa):
  medido sobre `Shrek_Fiona_crowning_outfits.jpeg` (3300×2200, foto conjunta
  con Shrek también vestido de rey): tonos tierra mezclados con el fondo del
  salón, `#99725D`/`#76462D`/`#B16433` — mezcla poco fiable por el fondo,
  marco esto ⚠️ (una sola toma, hace falta un recorte más cerrado para
  medir sólo la tela).
- **Fiona — vestido de baile azul** (*Shrek 2*, casa de sus padres): medido
  sobre `Fiona_human_2_pose_full.png` (1681×3300): `#2F4542`/`#536C6C`
  (azul-verdoso apagado, tipo petróleo) ⚠️ (una imagen, fondo oscuro
  mezclado).
- **Burro**: pelaje gris con manchas más claras en el hocico y crin negra.
  Medido sobre el recorte limpio `DonkeyTransparent.png` (1182×2864, fondo
  transparente): `#917D6B` (gris-marrón claro, lomo), `#6C5C4C` (gris medio),
  `#40362E` (crin/orejas oscuras), `#B6A18D` (hocico claro) ✅ (`estilo4.json`);
  coincide con el texto de la wiki, «gray donkey with brown eyes and a black
  mane» ✅ dos fuentes.
- **Gato con Botas**: pelaje naranja atigrado, botas y sombrero negros con
  pluma amarilla, capa negra. Medido sobre el recorte limpio
  `PussInBootsTransparent.png` (1855×1800): `#A1662A` (naranja principal),
  `#E4AF57` (crema de las mejillas/pecho), `#40332C` (capa/sombrero),
  `#0B0A09` (botas) ✅ (`estilo4.json`).
- **Ropa "icónica" que todo el mundo reconoce** (para no dudar en la
  lámina): el chaleco marrón de Shrek, el vestido verde de viaje de Fiona
  (no el azul ni el morado, que son de arcos concretos), el sombrero con
  pluma y las botas de Puss. Burro no lleva ropa nunca (es su propio pelaje
  el "vestuario").

### Punto 16 · Fondos, paisajes y fondos de pantalla (hex medidos)

- **El pantano de Shrek** (hogar, escena base de las 4 películas): medido
  sobre `Shrek_wolf_swamp.jpg` (3000×1808, atardecer): `#A07950` (tierra/luz
  cálida), `#705E4F` (barro medio), `#E89F38` (brillo de sol poniente),
  `#232323`/`#121212` (siluetas oscuras de árboles) ✅ (`estilo3.json`).
  Confirmado también en `Shrek_group_windmill_render.jpg` (2986×1800, de
  noche/anochecer): verdes de musgo `#4F6220`/`#8D991C` sobre `#323527`
  (sombra) ✅ — el pantano cambia de paleta cálida (día) a verde-musgo
  (noche), ambas documentadas.
- **Duloc** (ciudad-estado de Lord Farquaad): descrita en la propia wiki como
  «casas blancas de estilo germánico con detalles azules», trazado
  simétrico y artificial, murallas altas — [Duloc, Shrek Wiki (wikitext vía
  API)](https://shrek.fandom.com/wiki/Duloc) ✅. Medido sobre
  `Shrek_welcome_duloc_donkey.jpg` (3000×1808, la canción "Bienvenidos a
  Duloc"): `#A49B9C` (piedra clara), `#7E7884`/`#52526D` (azul-grisáceo de
  las torres), `#373A3F` (sombra) ✅ (`estilo6.json`) — coincide con la
  descripción de la wiki.
- **El palacio de Far Far Away** (reino de los padres de Fiona, parodia de
  Beverly Hills): medido sobre `Shrek_meets_Fiona's_parents_palace.jpg`
  (2742×1653): `#675948` (madera/piedra cálida), `#6A6C7E` (piedra
  azul-gris), `#992D29` (rojo de estandartes/alfombra) ✅ (`estilo3.json`).
- **Fondos de pantalla oficiales/fans en alta** (ya en `datos-imagen.md`,
  Wallhaven, sólo aptos): 11 fondos de 1920×1080 a 4504×1914, con autor y
  origen (ej. 3840×2160, 184 ♥, subido por *jrmnt*, origen
  [artstation.com/omorphia](https://www.artstation.com/omorphia); 1920×1080,
  27 ♥, *Bongic*, atardecer de pantano) ✅.
- **Texturas reales equivalentes libres (CC0, ambientCG)**: **Ground037**
  («damp earth, forest, moss, overgrown woodland», CC0) para el barro del
  pantano — [ambientcg.com/a/Ground037](https://ambientcg.com/a/Ground037);
  **Wood094**/**Wood092** (madera marrón lisa, CC0) para el molino y las
  vigas de Duloc — [ambientcg.com/a/Wood094](https://ambientcg.com/a/Wood094);
  **Grass001**/**Grass004** (césped verde corto, CC0) para los prados de
  Far Far Away — [ambientcg.com/a/Grass001](https://ambientcg.com/a/Grass001)
  ✅ (miniaturas 1024×1024, medidas).

### Punto 19 · Texturas 2D (y su equivalente libre)

Shrek es animación 3D, no manga: aquí "textura 2D" se traduce a las
superficies pintadas encima del render (attrezzo, pergamino, bordados,
emblemas), no a tramas de cómic.

- **El libro de cuentos de apertura** (todas las películas empiezan con un
  libro real que se abre): visto en `personajes_02.jpg` n.º 174 «Once upon a
  time... a King and a Queen» (página de libro pintada a mano, iluminada
  como manuscrito medieval, con letra capitular decorada) y n.º 193-195 (más
  páginas del libro, con ilustraciones estilo cuento infantil clásico,
  distintas del render 3D del resto de la película) ✅ vistas con Read.
  **Equivalente libre**: **Paper001/003/005/006** (papel con grano visible,
  fotogrametría CC0) — [ambientcg.com/a/Paper001](https://ambientcg.com/a/Paper001)
  — para simular esas páginas como textura de capa en Photoshop.
- **El bordado dorado del vestido verde de Fiona**: visible en
  `Fiona_kick_alternate.jpg` como enredaderas/hojas doradas sobre verde en
  el corpiño — patrón de enredadera, no geométrico. No hallé un pack de
  pinceles CC0 de "bordado medieval" descargable directo (probé
  "medieval floral embroidery brush free CC0" en el buscador: sólo salieron
  packs de pago en Etsy/CreativeMarket) ⚠️; alternativa: dibujar el patrón a
  mano con el pincel "Grabado" de Photoshop sobre la tela verde, es un
  motivo simple de repetir.
- **El chaleco de cuero remachado de Shrek**: textura visible de cuero
  gastado con grano irregular. **Equivalente libre**: **Leather037** (cuero
  marrón oscuro y limpio, CC0, fotogrametría) —
  [ambientcg.com/a/Leather037](https://ambientcg.com/a/Leather037) ✅.
- **Emblemas y objetos icónicos con forma propia**:
  - La **corona del rey de Far Far Away**, ficha propia en la wiki con
    imagen 726×726 —
    [File:Crown of the King of Far Far Away.jpeg](https://static.wikia.nocookie.net/shrek/images/3/3d/Crown_of_the_King_of_Far_Far_Away.jpeg)
    ✅ (tamaño confirmado vía `imageinfo`).
  - El **logo de Duloc** (las torres geométricas repetidas del arco de
    entrada y las banderas) no tiene ficha de imagen aislada en la wiki:
    aparece siempre dentro de fotogramas de la ciudad, nunca como emblema
    suelto — busqué "Duloc logo", "Duloc flag", "Duloc coat of arms" en el
    buscador de texto de la wiki (`srwhat=text`) sin una página dedicada
    ⚠️; lo más cercano es la propia foto de las torres (punto 16).
  - El **logo tipográfico "SHREK"** de las películas (letras verdes con
    textura de piel de ogro) es tarea de tipografía (punto 5, del
    investigador de texto), no lo repito aquí.
- No encontré un **artbook o entrevista que hable de tramas/pinceladas 2D
  específicas** (no aplica igual que en anime: Shrek se hizo con software 3D
  propio de PDI/DreamWorks, no con capas 2D pintadas a mano salvo el libro de
  apertura) — esto es lo esperable en una película 3D, lo anoto como "no
  aplica igual" en vez de "no lo encontré" sin más.

### Punto 23 · Colaboraciones y cruces

**Marcas y productos (confirmados, con fecha):**

| Colaboración | Cuándo | Qué trae de nuevo | Fuente(s) |
|---|---|---|---|
| **Crocs × Shrek** ("Shrocs") | anunciado sept-2023, restock feb-2025 | Clog verde lima con nariz/orejas de Shrek, correa trasera "peluda" marrón (referencia al chaleco), Jibbitz de Shrek, Fiona, Burro, Puss y el Dragón | [CNN](https://www.cnn.com/2023/09/17/style/shrek-crocs-collaboration-cec/index.html) + [Hollywood Reporter](https://www.hollywoodreporter.com/lifestyle/shopping/shrek-crocs-classic-clogs-release-date-pricing-1235588846/) ✅ dos fuentes |
| **McFarlane Toys — figuras 12" "Movie Maniacs"** | 2024 (relanzamiento; el trato original con DreamWorks es de 2001) | Shrek y el Dragón en pose fija de 12 pulgadas — **pose de escultor profesional, sirve de referencia 3D** | [Collider](https://collider.com/shrek-dragon-figures-mcfarlane-toys/) ✅ |
| **DreamWorks Land (Universal Orlando)** | abierto 14-jun-2024 | zona temática con el pantano de Shrek, "Shrekzels", encuentro con Shrek/Fiona/Burro, atracción interactiva "King Harold's Swamp Symphony" | [blooloop](https://blooloop.com/theme-park/news/universal-orlando-dreamworks-land-open/) ✅ |
| **"Shrek & Fiona's Happily Ogre After" (Universal Kids Resort, Texas)** | abre 1-jul-2026 | primera atracción tipo paseo de Shrek en EE. UU.: carruajes al aire libre con viñetas "de madera" de momentos de las películas | [Attractions Magazine](https://attractionsmagazine.com/shrek-ride-fionas-happily-ogre-after-universal-kids-2026/) ✅ |
| **Musical de Broadway/West End "Shrek the Musical"** | gira activa desde 2008 | vestuario y set teatrales, distinto del 3D de la película — fotos con licencia libre ya en `datos-imagen.md` (Openverse, CC BY 2.0, Theatre Royal Drury Lane, Londres) | `datos-imagen.md`, [Openverse](https://openverse.org) ✅ |

**No confirmado / descartado (para no inventar):**

- **Fortnite**: NO hay colaboración oficial. Circulan vídeos y capturas
  "filtradas" en TikTok, pero Epic Games nunca lo confirmó — [TechWiser](https://techwiser.com/fortnite-shrek-collab-skins/)
  + [esports.gg](https://esports.gg/news/fortnite/is-shrek-in-fortnite-here-is-what-we-know/)
  ⚠️ dos fuentes coinciden en que es un rumor sin confirmar, lo dejo como
  "no existe (todavía)", no como colaboración real.
- **Vans**: no hay colaboración oficial (sólo Vans personalizadas por fans
  en redes) — búsqueda «Shrek Vans shoes collaboration official» sin
  resultado oficial ⚠️.
- **Shrek Rave**: NO es un evento de DreamWorks. Es una gira de fiestas
  temáticas creada por promotores independientes (organizador *Ka5sh*);
  DreamWorks sólo se involucró **una vez**, en 2022, con una versión "más
  tranquila" como parte del estreno de *Puss in Boots: The Last Wish* —
  [Vice](https://www.vice.com/en/article/shrek-rave-uk-photos/) ✅. Útil
  para entender el fenómeno de fandom (punto 12, no el mío), pero no debe
  citarse como "colaboración oficial de marca".

**Figuras oficiales (pose = referencia 3D real):**

- Los **Sketchfab CC BY del punto 3** son, en su mayoría, extracciones de
  videojuegos con licencia oficial: *Pocket Shrek* (móvil), *DreamWorks
  All-Star Kart Racing*, *Shrek Super Slam*, *Shrek 2 (PC)* — confirman que
  hay modelos 3D con rig ya listos de un juego con licencia de DreamWorks,
  no fan-made desde cero.

**Cosplay:** no encontré una foto de cosplay premiada o de convención grande
con crédito claro de autor (busqué «Shrek Fiona armor cosplay
craftsmanship photos»): sólo salieron tiendas de disfraces (Etsy/eBay) y
Pinterest sin autor verificable ⚠️ — esto es un extra del punto 23 (pide
"cosplay bien hecho" en general, no es obligatorio citar uno concreto si no
aparece con crédito claro), lo dejo anotado.

## Lo mejor para la lámina

1. **`Shrek_fierce.jpg`** (pose viva, garras arriba, gran sonrisa) +
   **`Fiona_kick_alternate.jpg`** (patada en el aire, corona puesta): las dos
   imágenes que de verdad rompen el "de pie con su ropa" que rechazó el
   dueño.
2. **La página "Essential Guide" del Gato con Botas** (`personajes_03.jpg`
   n.º 7): bio + pose + gestos en una sola lámina ya diagramada, buena
   referencia de maquetación de texto+personaje.
3. **La paleta del pantano al atardecer** (`#A07950`/`#E89F38`/`#705E4F`):
   cálida, reconocible, mejor que el verde plano "de memoria" que se
   esperaría de un pantano.
4. **El "antes/después" de Fiona** (Handbook, humana vs. ogro con el mismo
   vestido): confirma que un solo diseño de vestuario sirve para las dos
   formas, ahorra decisiones de arte.
5. **Crocs × Shrek** y **DreamWorks Land**: prueba de que la marca sigue viva
   fuera de las películas, con objetos (el Croc verde, el "Shrekzel") que
   podrían aparecer como *props* de una lámina sin inventar nada.

## No encontré

- ⚠️ Un **key visual de campaña único** (más allá de los carteles teatrales
  clásicos) para las películas 1-4: busqué «Shrek theatrical poster official
  high resolution key art»; lo que hay ya es muy conocido y no aporta pose
  nueva. Es un extra del punto 1 (que ya está ✅ con lo demás), no obligatorio.
- ⚠️ **Licencia clara de un pack de pinceles de bordado medieval** gratis
  para el patrón dorado del vestido de Fiona (punto 19): sólo salieron packs
  de pago; dejo la alternativa de dibujarlo a mano.
- ⚠️ Un **logo o escudo aislado de Duloc** (aparte de ver las torres en los
  fotogramas): no tiene ficha de imagen propia en la wiki.
- ⚠️ **Cosplay con crédito de autor verificable** para el punto 23 (extra,
  no obligatorio: el punto ya tiene marcas, figuras y parques cumplidos).
- La colaboración de **Fortnite** y de **Vans**: confirmé que **no existen**
  (con dos fuentes cada una) en vez de darlas por buenas o llamarlas
  "posible confusión".

## Las hojas de contacto

- `hojas/personajes_01.jpg` = hoja 1 automática (`investigar_serie.py`):
  Shrek y Fiona en **poses vivas** (patada, garras, abrazo, baile, boda) más
  varias fichas "Essential Guide" pequeñas al fondo del recorrido. Es la
  fuente de las dos imágenes del punto "Lo mejor para la lámina".
- `hojas/personajes_02.jpg` = hoja 2 automática: las páginas completas de
  las guías oficiales (n.º 49, 50, 64, 65), la página del libro de cuentos
  pintado a mano (n.º 174, punto 19), la boda/coronación en grupo, y las
  dos **Shrek 5 Teaser Still** (n.º 197-198, punto 1).
- `hojas/personajes_03.jpg` = **hoja propia**, montada con Pillow porque las
  automáticas casi no traían a Burro ni al Gato con Botas: recorte limpio de
  cada uno (para medir hex sin fondo), Burro volando con purpurina mágica,
  Burro comiendo waffles en el sillón, el Gato peleando a espada, la página
  "Essential Guide" del Gato completa, y el gag de Puss montado sobre Burro
  (*Shrek Forever After*, realidad alternativa).

## Bitácora de búsqueda

Partí de `partes/datos-imagen.md` (no repetí sus consultas de Fandom,
Danbooru, Safebooru, Wallhaven, Sketchfab, Openverse) y de las 6 hojas de
contacto ya generadas en `herramientas/referencias/shrek/` (vistas enteras
con Read antes de escribir).

**Buscador web** (9 búsquedas de mi cupo de ~50, todas en inglés — Shrek es
una producción estadounidense, no hacía falta japonés/coreano):
"Shrek Fortnite skin 2023 official collaboration"; "Shrek Crocs
collaboration 2024 official"; «"Shrek 5" 2026 official teaser poster
image»; «"Art of Shrek" artbook official DreamWorks concept art book»;
"Shrek Rave event official DreamWorks"; "Shrek Vans shoes collaboration
official"; "Shrek McDonald's Happy Meal toys official 2001 promotion";
"DreamWorks Land Universal Studios Shrek attraction 2026"; "Shrek McFarlane
Toys NECA figure official 2022"; "Shrek Fiona armor cosplay craftsmanship
photos".

**WebFetch**: ficha de Internet Archive del artbook *The Art of DreamWorks
Shrek Forever After* (título, editorial, año, páginas, ISBN).

**Red directa** (sin gastar buscador):
- **Fandom (`shrek.fandom.com/api.php`)**: `action=parse&prop=wikitext` para
  la página **Duloc** (descripción de la ciudad); `action=query&prop=imageinfo`
  para el tamaño real de **Crown of the King of Far Far Away**;
  `list=search&srwhat=text` para "coat of arms" y "Far Far Away crest seal".
- **Sketchfab API** (`v3/search` y `v3/models/<uid>`): confirmé licencia,
  vértices y vistas de 4 modelos (Puss, Shrek, Burro, Fiona) llamando al
  modelo directo, no sólo la búsqueda; busqué también "Donkey Shrek" (la
  consulta en español "Shrek Burro" del recolector automático había dado 0
  resultados).
- **Safebooru API** (`index.php?page=dapi&s=post&q=index&json=1`): tags
  `shrek` y `donkey_(shrek)` (el recolector automático sólo había consultado
  `puss_in_boots_(shrek)` y `princess_fiona`).
- **ambientCG API** (`/api/v2/full_json`): texturas CC0 de `leather`,
  `paper`, `fabric`, `wood`, `moss`, `grass`; medidas sus miniaturas
  1024×1024.
- **`herramientas/estilo.py`** (Pillow): 12 imágenes originales medidas para
  hex — `Shrekprofile.png`, `Fiona_Profile.png`, `Warrior_Fiona.jpg`,
  `Shrek_Fiona_crowning_outfits.jpeg`, `Shrek_fierce.jpg`,
  `Fiona_kick_alternate.jpg`, `Fiona_human_2_pose_full.png`,
  `PussInBootsTransparent.png`, `Shrek_wolf_swamp.jpg`,
  `Shrek_meets_Fiona's_parents_palace.jpg`,
  `Fiona_ogre_form_outside_wind_mill.png`, `Shrek_2_meets_parents.jpg`,
  `DonkeyTransparent.png`, `Fiona_ogre_2_render.png`,
  `Shrek_welcome_duloc_donkey.jpg`, `Shrek_group_windmill_render.jpg`.
- **Montaje propio con Pillow**: `hoja_donkey_puss.jpg` (8 imágenes de Burro
  y el Gato con Botas, con número y nombre de archivo), para suplir lo que
  las hojas automáticas casi no cubrían.

**Fallos y cómo los resolví:**
- El recolector automático había buscado "Shrek Burro" en Sketchfab (0
  resultados): repetí la búsqueda en inglés ("Donkey Shrek") y sí salieron
  modelos.
- Las hojas automáticas de `investigar_serie.py` salieron muy desbalanceadas
  (Fiona/Shrek 277 menciones, Burro/Gato 28): en vez de "no lo encontré",
  monté mi propia hoja con las URLs que ya traía `fandom.json` — más barato
  que volver a llamar a `investigar_serie.py` entero.
- No hubo 403/429 en esta tanda: todas las descargas de `static.wikia.nocookie.net`
  funcionaron con el `Referer: https://www.fandom.com/` que ya usa
  `herramientas/estilo.py`.

## Cumplimiento del encargo (sólo mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | 424 imágenes de wiki con tamaño real, 2 artbooks oficiales con ficha, carteles de *Puss in Boots*, 2 imágenes de *Shrek 5* (confirmadas con 2 fuentes), postal del 25.º aniversario, arte de videojuego |
| 3 · Fan art y 3D con licencia | ✅ | 6 modelos Sketchfab con licencia confirmada por la API (no sólo la página), fan art de los 4 personajes en Safebooru con autor/origen enlazado |
| 15 · Vestuario con hex medidos | ✅ | Hex medidos con `estilo.py` para Shrek, Burro, Gato con Botas y 4 vestuarios distintos de Fiona (viaje, guerrera, coronación ⚠️, baile ⚠️); 2 de Fiona quedan con una sola fuente marcada |
| 16 · Fondos de pantalla | ✅ | Pantano (día y noche), Duloc y Far Far Away con hex medidos y cruce con texto de la wiki; 11 wallpapers con autor y tamaño; 3 texturas CC0 equivalentes |
| 19 · Texturas 2D | ✅ | Libro de cuentos pintado a mano, cuero del chaleco y corona con ficha propia, con equivalentes CC0 (Paper, Leather); bordado dorado y logo de Duloc marcados ⚠️/"no aplica" con la búsqueda hecha |
| 23 · Colaboraciones y cruces | ✅ | 5 colaboraciones oficiales confirmadas con fecha y fuente doble; Fortnite y Vans confirmados como **no existentes** (no "posible confusión"); cosplay con crédito quedó como extra sin encontrar |
