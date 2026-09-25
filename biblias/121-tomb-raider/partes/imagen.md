# Parte de IMAGEN · Tomb Raider (encargo 121)

Investigador de imagen: puntos 1, 3, 15, 16, 19 y 23 de `ENCARGO.md`. Parte de
`partes/datos-imagen.md` (Fandom/laracroft.fandom.com bajo el dominio
tombraider.fandom.com, Danbooru, Safebooru, Wallhaven, Sketchfab, Openverse) y
lo amplío con: la página `Lara's Outfits` completa de la wiki (todo el
vestuario por juego, wikitext entero), la página `Tomb Raider Crossovers`
(colaboraciones oficiales una por una), los «Cosplay Guides» y «Gear Up
Guides» oficiales de tombraider.com (texto del director de arte Brenoch
Adams), capturas oficiales de Steam de los 3 reboots (API `appdetails`),
Poly Haven y ambientCG (CC0) y dos símbolos medidos (Croft Family Crest,
Trinity). Enfoque pedido en el encargo: **exploración y ruinas**. Es un
videojuego (varias épocas gráficas: renders PS1 poligonales, reboot
foto-realista): "texturas 2D" se lee como logos, emblemas y parches de tela,
no manga.

## 1 · Arte oficial, en cantidad y variado

- **La wiki tiene una subpágina "Artwork" por juego** (comprobado en
  `Tomb Raider (1996 Game)/Artwork`, wikitext completo): separa Box Artwork
  (Sega Saturn, PC, N-Gage), Renders (más de 30 renders numerados de Lara
  sola y con objetos), Game Screens, **Game Logos por región** (NA, Europa,
  **Japón** — logo distinto, `TOMBRAIDERLOGO5.png`), FMV Screenshots,
  Character Renders (Larson, gorila, cocodrilo, dinosaurio) y Advertisements
  (postal EE. UU., anuncio de revista japonesa de la versión Sega Saturn) ·
  https://tombraider.fandom.com/wiki/Tomb_Raider_(1996_Game)/Artwork · ✅
  (wikitext de la propia wiki; el patrón de subpágina "/Artwork" se repite en
  cada juego de la franquicia, confirmado en dos juegos distintos).
- **Key art de Rise of the Tomb Raider**, la imagen más grande de toda la
  wiki de Lara Croft: 9000×5762, Lara escalando con un pico de hielo, nieve y
  luz fría · https://static.wikia.nocookie.net/laracroft/images/2/27/Rise-of-the-Tomb-Raider.jpg
  · ✅ (tamaño confirmado por la API `imageinfo` de Fandom, dos veces:
  `datos-imagen.md` y mi propia consulta).
- **Render de portada TR1 Classic** (1996, pose "viva" de disparo, mirada
  furiosa, luz de foco): mint tank top, shorts marrón, trenza · medido con
  `estilo.py`: paleta dominante `#020201` 52.7% (fondo), `#973625` 3.7% (luz
  roja de foco), tono de piel `#9E9485`/`#DECCB0` · sombreado
  degradado/pintado, poca línea · https://static.wikia.nocookie.net/laracroft/images/4/44/TR1_Classic_Outfit.jpg
  (4000×3000) · ✅ (wiki + medido con estilo.py, mirado en `hojas/vestuario_02.jpg` nº1).
- **"Many Changes of Lara Croft 2.jpg"** (4875×1300) y **"20 Years of
  Croft.jpg"** (1600×904): dos collages oficiales/semioficiales que muestran
  a Lara en TODAS sus épocas visuales lado a lado (poligonal 1996 → reboot
  fotorrealista), útiles para explicar de un vistazo el cambio de estilo ·
  https://static.wikia.nocookie.net/laracroft/images/f/f0/Many_Changes_of_Lara_Croft_2.jpg
  y https://static.wikia.nocookie.net/laracroft/images/5/5a/20_Years_of_Croft.jpg
  · ✅ (imágenes de la wiki, ambas con más de 15 años de histórico de edición).
- **"Home of Adventure" — Croft Manor en grupo** (`Lara Croft and the
  Guardian of Light`, 1920×1080, `Gol1.jpg`): pose en acción a media altura,
  con arco tensado, salto entre ruinas · ✅ (wiki, ya en `datos-imagen.md`).
- **Capturas oficiales de Steam de los 3 reboots** (API `appdetails`,
  1920×1080, no repito la consulta del recolector, pido appid nuevo sólo
  para las capturas que faltaban):
  - Rise of the Tomb Raider (appid 391220): 8 capturas — templo de la selva
    con estatua tallada y Lara saltando entre ruinas (nº4 de
    `hojas/fondos_03.jpg`), arco nevado de piedra (nº2), cueva con haz de luz
    (nº6), primer plano de la cara con cicatriz y polvo (emoción de
    determinación) · https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/391220/ss_749f99146e5ebad371e37d95bfab7b17847c1d81.1920x1080.jpg
    (templo selva) · ✅ (Steam API, coincide con lo descrito en reseñas).
  - Shadow of the Tomb Raider (appid 750920): 10 capturas — templo maya con
    farolillos y multitud en fiesta (Paititi, nº3 de `hojas/fondos_03.jpg`),
    aldea con pirámide entre árboles (nº4), puñal/combate sigiloso en la
    selva · https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/750920/ss_3fcd62a2831bcc1e557a0fe2a061b6369ba030d1.1920x1080.jpg
    (templo con farolillos) · ✅.
  - Tomb Raider (2013, appid 203160): 10 capturas — puente de cuerda entre
    ruinas con niebla y luz de amanecer (nº5 de `hojas/fondos_03.jpg`),
    explosión en aldea japonesa, Lara colgando de una estructura en llamas ·
    https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/203160/ss_c93f9a97f2fd890f21c829cf8781850484eec7f3.1920x1080.jpg
    (puente/niebla) · ✅.
- **Artbook oficial**: *Tomb Raider: The Art of Survival* (BradyGames, para
  el reboot de 2013), con comentario del director creativo y los artistas ·
  citado por ConceptArtWorld y Goodreads · ⚠️ (no encontré copia completa
  legal para leer el texto, sólo reseñas que confirman su existencia y
  contenido — dos fuentes de reseña sí cuentan como confirmación de que
  existe, no de su contenido interno).
- **No encontré** una copia navegable del artbook de *Rise of the Tomb
  Raider* (Exclusive Edition) más allá de fotos de unboxing en
  tombraidercollection.com — lo dejo como referencia, no como fuente citada
  con detalle.

## 3 · Fan art y renders 3D como referencia

- **Modelos 3D con licencia libre en Sketchfab** (API v3, ya en
  `datos-imagen.md`, comprobados): "Tomb Raider Laracroft" (ItsKrish7, CC
  Attribution, ♥481), "Home of Adventure" (PippyJ, CC Attribution, ♥260 — un
  **sitio** de la serie, no sólo el personaje, encaja con "exploración"),
  "Ice Axe (DMM Rebel)" (Yogensia, CC Attribution-NonCommercial-ShareAlike,
  ♥237 — el piolet de escalada, objeto icónico de Rise/Shadow), "Lara Croft -
  Default Style" (Yxboireal, CC Attribution, ♥214) · ✅ (licencia confirmada
  en la respuesta de la API, no sólo en la miniatura).
- **Fan art 2D mejor puntuado** (Safebooru, ya en `datos-imagen.md`): el más
  grande con licencia de tag `lara_croft` es 3500×2000 (origen DeviantArt,
  "Lara Croft Reborn" por kokecit) y 1717×2447 (origen desconocido) · ⚠️
  origen exacto no siempre resoluble (varios enlaces de DeviantArt/Pixiv ya
  caídos), pero el enlace de Safebooru en sí es estable.
- **Fotos con licencia libre de cosplay/exposiciones** (Openverse, ya en
  `datos-imagen.md`): serie de 8 fotos CC BY-NC 2.0 de la exposición "Rise of
  the Tomb Raider" por K-putt en Flickr, y 3 fotos CC BY-NC-ND 2.0 de
  "Kanracakes" vestida de Lara Croft Reboot en JAFAX 2013
  (https://live.staticflickr.com/5318/14230572907_d81b27f9d5_b.jpg,
  683×1024) · ✅ (licencia Creative Commons explícita de Flickr/Openverse).
- **Poly Haven (CC0)** — objetos/sitios equivalentes a los de la serie, para
  "exploración y ruinas": HDRI **"Colosseum"** (ruinas de piedra reales, luz
  de mañana/tarde, alto contraste, hasta 16K disponible) ·
  https://polyhaven.com/a/colosseum · y HDRI **"Blue Grotto"** (cueva con
  cascada y roca, hasta 8K) · https://polyhaven.com/a/blue_grotto · ambas CC0,
  buena referencia real de luz para las ruinas/cuevas de Tomb Raider · ✅
  (licencia CC0 de la propia API de Poly Haven).
- **No encontré** modelos 3D fan-made específicos de "Croft Manor" o de un
  templo concreto de la serie en Sketchfab con licencia libre (busqué "Croft
  Manor Sketchfab downloadable" y "Tomb Raider temple Sketchfab CC"): sólo
  aparecen modelos sin licencia de descarga o de pago.

## 15 · Vestuario

Fuente principal: la página **`Lara's Outfits`** completa de la wiki
(wikitext entero, 18 143 caracteres, organizada por línea temporal — Original,
Legend, Survivor — y por juego), cruzada con los **"Cosplay Guide" y "Gear Up
Guide" oficiales** de tombraider.com (texto real citado, con nombre del
director de arte) y medidas de hex con `estilo.py`/Pillow sobre 5 renders
descargados (mirados en `hojas/vestuario_02.jpg`).

- **El "traje icónico" que todo fan reconoce** (confirmado por la propia
  wiki): "Lara's signature ensemble consists of a tank top, shorts, socks and
  combat boots, which she wore in every game until the 2013 Reboot" ·
  https://tombraider.fandom.com/wiki/Lara%27s_Outfits · ✅. Es el TR I/II/III
  Classic: **tank top verde menta** — medido en el render de portada TR1
  (`hojas/vestuario_02.jpg` nº1) con Pillow, píxel de la prenda `#82A084` —,
  **shorts marrón** (zona iluminada `#542E0D`, zona en sombra `#321E0C`),
  botas y guantes sin dedos negros, trenza castaña · ✅ (wiki + medido dos
  veces en la misma imagen).
- **Legend (2006)**: crop top y shorts en tonos tierra. Cita textual del
  **Cosplay Guide oficial** de tombraider.com: *"Lara Croft's main outfit in
  Tomb Raider: Legend is a sporty ensemble in earthy tones. She dons a brown
  nylon and spandex layered crop top with shorts, along with double hip
  leather holsters, a belt, black combat boots, and fingerless gloves. Her
  iconic backpack has been redesigned into a sleek black leather snap
  backpack. Lara ties her hair into a stylish ponytail with an elastic brown
  hair tie."* · https://www.tombraider.com/news/cosplay/cosplay-guide-tomb-raider-legend
  (23-sep-2024) · ✅ (fuente oficial de Crystal Dynamics, con el material
  exacto: nylon + spandex, no "tela genérica"). Variantes por 100% de
  coleccionables: Legend Pink (Ghana), Union Jack (Bolivia), Black (Croft
  Manor), Blue (Perú) — mismo artículo.
- **Reboot 2013 (Survivor Timeline)**: tank top gris ceñido y pantalón de
  cargo desgarrado y manchado de barro y sangre, botas de combate marrones.
  Medido en el render "Standard Outfit" (`hojas/vestuario_02.jpg` nº3): tank
  top gris-verdoso, pantalón marrón-óxido con manchas oscuras (estilo.py:
  sombreado degradado/pintado, saturación 8%, brillo 78% por el fondo blanco
  del render) · ✅ (wiki `Lara's Outfits` + medido). Variantes DLC: Sure-Shot,
  Mountaineer, Hunter, Guerrilla, Demolition, Aviatrix.
- **Rise of the Tomb Raider (2015)**: primer juego con ropa "funcional, no
  sólo cosmética" (perks), según la propia wiki. Outfit "Desert Tank Top",
  con cita textual del **Gear Up Guide oficial**, firmada por **Brenoch
  Adams, director de arte**: *"Lara wears this ribbed grey tank top with
  support and slim fit to keep her agile and comfortable in warmer climates.
  The dark material balances well with her lighter value pants and the
  leather drop bag design that sits on her hips and keeps the tank
  comfortably in place."* — visible en la propia hoja de referencia oficial
  (`hojas/vestuario_02.jpg` nº4, "FROM THE ART DIRECTOR — Brenoch Adams") ·
  https://static.wikia.nocookie.net/laracroft/images/6/6b/ROTTR_Desert_Tank.png
  · confirmado que Brenoch Adams es el director de arte de la saga por un
  segundo Gear Up Guide independiente ("Shadowrunner Outfit", firmado igual)
  · https://www.tombraider.com/news/cosplay/gear-up-guide-shadowrunner-outfit
  · ✅ (dos artículos oficiales distintos, mismo autor acreditado). Más de 20
  outfits desbloqueables en Rise (Huntress, Apex Predator, Commando,
  Infiltrator, Shadow Runner, Siberian Ranger…), todos listados en
  `Lara's Outfits`.
- **Shadow of the Tomb Raider (2018)**: outfit por defecto = **tank top
  azul-grisáceo ceñido + pantalón cargo verde oliva con parche gris-azul en
  la rodilla + guantes sin dedos + botas**. Cita textual oficial (misma que
  aparece en la hoja de referencia, `hojas/vestuario_02.jpg` nº5):
  *"Equipped in performance gear designed to keep her cool and dry in one of
  Earth's most hostile environments... A fitted moisture-wicking tank top,
  pants with reinforced knees, fingerless tactical gloves, and waterproof
  boots aid her in becoming one with the jungle, overcoming terrifying tombs,
  and persevering through her darkest hour."* ·
  https://www.tombraider.com/news/cosplay/shadow-of-the-tomb-raider-gear-guide
  (16-sep-2024) y la propia imagen oficial en
  https://static.wikia.nocookie.net/laracroft/images/e/ed/SOTTR_Tank_Top.png
  · ✅ (mismo texto en dos publicaciones de Crystal Dynamics: el artículo web
  y la imagen-cartel que circula en la wiki). Hex medidos con Pillow sobre el
  render frontal: tank top `#606B7C`, pantalón oliva `#444338` · ✅ (medido).
  Más de 15 outfits temáticos de Paititi (Robes of Puka Huk, Serpent Guard,
  Blue Heron Tunic, Condor Cowl of Urqu…), todos con nombre inspirado en
  cultura andina/maya, listados en `Lara's Outfits`.
- **Serie completa de "Cosplay Guides" oficiales**: tombraider.com publica
  desde 2021 una guía por outfit con el hashtag #TombRaider para que los fans
  suban su cosplay — confirma que Crystal Dynamics apoya activamente el
  cosplay de la comunidad, con guías para TR I (Workout Gear), TR II (Bomber
  Jacket, Sola Wetsuit, Manor/Dressing Gown), TR III (Nevada/Assault,
  Antarctica/South Pacific), Chronicles (Catsuit), Underworld (Doppelgänger),
  Legend, Rise (Shadowrunner) y Shadow · https://www.tombraider.com/news/cosplay
  · ✅ (listado directo de la sección oficial de noticias).

## 16 · Ciudades, paisajes y fondos de pantalla

Enfoque del encargo: **exploración y ruinas**. Fuentes: capturas oficiales de
Steam (API `appdetails`, medidas y miradas en `hojas/fondos_03.jpg`) +
Wallhaven (ya en `datos-imagen.md`) + nombres de sitios de la wiki.

- **Templo de la selva con estatua tallada, niebla y luz cenital** (Rise of
  the Tomb Raider, captura Steam, `hojas/fondos_03.jpg` nº1): Lara saltando
  entre ruinas cubiertas de vegetación · paleta medida con estilo.py:
  `#4C3F2D` 24.3%, `#68573F` 23.3%, `#86714F` 18.9%, dorado claro `#E9C392`
  6.6% — tonos tierra cálidos, mucha línea de contorno en la vegetación ·
  ✅ (Steam API + medido) · https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/391220/ss_749f99146e5ebad371e37d95bfab7b17847c1d81.1920x1080.jpg
- **Arco de piedra nevado, ruina excavada en la nieve** (Rise, nº2 de la
  hoja): paleta fría desaturada, `#605949` 27.1% (piedra), blanco nieve
  `#E9E3D2` 11.1%, un acento rojo `#922F27` 3.9% (el abrigo de Lara) — el
  único punto de color cálido en un fondo gris-beige · ✅ medido.
- **Templo maya con farolillos de colores, multitud en fiesta** (Shadow of
  the Tomb Raider, Paititi, nº3): la ciudad escondida, evento festivo con
  globos y linternas · paleta con azul frío de la niebla `#41758C` 7.8% y
  piedra rojiza `#6D4733`/`#A4703E` (30%) — mezcla de piedra antigua y luz de
  fiesta, único caso "cálido+festivo" entre los fondos de ruinas · ✅ medido.
- **Aldea entre árboles con pirámide de fondo** (Shadow, nº4): verdes oscuros
  `#2A2F27` 28.3% y `#4B4F47` 18.9%, casi sin color cálido — selva densa,
  poca luz directa · ✅ medido.
- **Puente colgante entre ruinas, niebla y sol rasante** (Tomb Raider 2013,
  nº5): el más "postal" de los seis, alto brillo (53%) — beige/crema
  dominante `#C9C5B0` 15.9% y `#9B927C` 11.2%, blanco de niebla `#FCFCF5`
  18.7% · ✅ medido — sirve de mejor candidato a fondo de pantalla luminoso.
- **Cueva con haz de luz vertical** (Rise, nº6): fría y oscura, `#3B444B`
  23.3% y `#52606B` 11.8%, brillo bajo (26%) — buena referencia de "tensión
  en la ruina", opuesta a la del puente · ✅ medido.
- **Sitios con nombre propio** (para no describir "una ruina" en general,
  wiki + Steam): **Paititi** (ciudad perdica escondida en la selva peruana,
  Shadow), **Kitezh** (ciudad sumergida, Shadow, aparece hasta en una carta
  de Magic: The Gathering — "Kitezh, Sunken City" — ver punto 23), **Siberia**
  (Rise, ruinas nevadas de la Orden de Trinity), **Croft Manor** (mansión
  familiar, aparece en todas las líneas temporales) · ✅ (wiki + Steam +
  Fandom Crossovers).
- **Fondos de pantalla de fans en alta resolución** (Wallhaven, ya en
  `datos-imagen.md`, API comprobada): el más guardado es 3840×2160 con 268
  favoritos (Gameerraza, arte de Rise sobre Nexus Mods), y hay uno
  específico de exploración/ruinas: 4500×3971, 96 favoritos, "artwork,
  jungle, eclipse" (Shadow of the Tomb Raider) ·
  https://w.wallhaven.cc/full/k9/wallhaven-k9p181.jpg · Wallhaven no da
  licencia explícita (fan-made, sólo referencia) · ⚠️ licencia.
- **Poly Haven CC0 equivalentes reales** (ver también punto 3): "Colosseum"
  (ruinas de piedra reales) y "Blue Grotto" (cueva con cascada) — luz y
  material reales para maquetar un fondo de ruinas sin depender de una
  captura de videojuego con copyright.

## 19 · Texturas 2D

No hay tramas de manga (es videojuego): leo el punto como **emblemas, logos y
parches de tela** de la serie, más texturas reales equivalentes de piedra
antigua para las ruinas.

- **Croft Family Crest** (escudo de armas de la familia, coleccionable de
  *Rise of the Tomb Raider: Blood Ties*): escudo cuartelado en azul-grisáceo
  con cruz dorada, yelmo de caballero con dos espadas cruzadas arriba,
  monograma "C" en el centro y una cinta con "Croft" debajo, marco de metal
  con remaches · medido con estilo.py: dorado envejecido `#7F7A6E`/`#C0B9A8`
  sobre azul-gris oscuro, sombreado plano tipo "cel" (poca transición) ·
  747×747 · https://static.wikia.nocookie.net/laracroft/images/7/72/Croft_Family_Crest.png
  · ✅ (existe como objeto in-game + wiki, imagen mirada directamente,
  ver `hojas/vestuario_02.jpg` nº6).
- **Emblema de Trinity** (la organización antagonista): parche/tatuaje
  triangular en tono rojo oscuro/granate, visto sobre el uniforme de un
  cadáver en una foto tipo polaroid dentro del juego (1019×1019) ·
  https://static.wikia.nocookie.net/laracroft/images/1/1d/Trinity_Badge.png
  · ⚠️ (la escena está muy oscura — el hex exacto del rojo no se puede medir
  con fiabilidad por la iluminación baja del plano; el triángulo y el color
  "rojo sangre/granate" sí están confirmados visualmente).
- **Parches de tela citados con material exacto** (ver punto 15): el Gear Up
  Guide de Shadowrunner describe un "tactical collared **polyester mesh**
  constructed vest with ammo pouches" y correas de "**thermoplastic
  molded**" — confirma que el estudio piensa el vestuario como capas de
  materiales reales (nylon, spandex, poliéster, cuero, termoplástico), no
  como "ropa" genérica · ✅ (cita oficial, ver punto 15).
- **Equivalentes libres (CC0) para piedra de ruina tallada**:
  - `ambientCG` **"PavingStones151"**: adoquín/piedra de cantera, 2K típico
    (2048×2048, hasta 8K) · https://ambientcg.com/view?id=PavingStones151 ·
    CC0.
  - `ambientCG` **"Rock064"**: roca con musgo, la más cercana a las ruinas
    cubiertas de vegetación de Rise/Shadow · https://ambientcg.com/view?id=Rock064
    · CC0.
  - `ambientCG` **"Ground068"**: tierra/musgo de suelo de selva ·
    https://ambientcg.com/view?id=Ground068 · CC0.
  · ⚠️ resolución exacta de descarga no verificada píxel a píxel (la API no
  la expone directo para materiales tileable); ambientCG ofrece 1K/2K/4K/8K
  por convención del sitio, igual que en otras partes de imagen ya hechas
  (ver `biblias/120-days-gone/partes/imagen.md`).

## 23 · Colaboraciones y cruces

Fuente principal: la página **`Tomb Raider Crossovers`** de la wiki
(wikitext completo, 20 936 caracteres, cada colaboración con su propia
sección y fuente primaria citada — tuits oficiales, blogs de los juegos
socios). Es una franquicia con muchísimos cruces oficiales activos, más que
la media de las bibliografías de este equipo.

- **Fortnite** (el cruce más grande): Capítulo 2 Temporada 6, skins Lara
  Croft Classic, 25th Anniversary, Gold Anniversary y Survivor, más
  accesorios ("Little Bird", "Pry Axe", "Salvaged Chute"…). Además, el
  evento **"Mystery at Croft Manor"** metió la mansión Croft entera como isla
  jugable en modo creativo (código `0116-9392-3142`) · fuente primaria:
  https://www.epicgames.com/fortnite/en-US/news/mystery-at-croft-manor-experience
  citada en la wiki · ✅ (wiki + página oficial de Epic Games).
- **Call of Duty: Warzone / Modern Warfare II** (2023): paquete "Tracer Pack:
  Tomb Raider" con blueprints del piolet de hielo y las pistolas dobles
  Mach-5 de Lara · fuente primaria: tuit oficial de @CallofDuty citado en la
  wiki (23-ago-2023) y blog oficial de Call of Duty · ✅ (dos fuentes:
  Twitter oficial + callofduty.com/blog).
- **Dead by Daylight** (jul-2024) y **Naraka: Bladepoint** (ago-2024, con
  doblaje propio en inglés y chino) y **Rainbow Six Siege** (elite skin de
  Ash, mar-2020) y **Delta Force** (abr-2026): Lara como personaje/skin
  jugable en cuatro shooters distintos, cada uno con su tráiler oficial
  citado en la wiki · ✅ (wiki, con tráileres embebidos como fuente).
- **Magic: The Gathering — Secret Lair** (20-nov-2023): set de cartas
  ilustradas de Tomb Raider, incluida una carta "Kitezh, Sunken City" (el
  sitio de Shadow of the Tomb Raider) · ✅ (wiki).
- **Final Fantasy** (tres cruces distintos): traje de Lara en *Lightning
  Returns: Final Fantasy XIII* (con hacha de escalada gigante y escudo),
  outfit desbloqueable en *Final Fantasy XV* (parche 1.26, sep-2018), y Lara
  como unidad jugable en *Final Fantasy Brave Exvius* y *War of the
  Visions* · ✅ (wiki, cuatro juegos distintos con su propio tráiler citado).
- **Otros cruces oficiales confirmados** (todos con tráiler o anuncio oficial
  citado en la wiki): Ghost Recon Breakpoint ("Relics of the Ancients",
  jul-2021), PowerWash Simulator (DLC "Croft Manor", ene-2023), Team Fortress
  2 (objetos ganados en concurso comunitario, dic-2014), World of Tanks
  (jul-2025, Lara vuelve a ser doblada por Keeley Hawes), Animal Crossing:
  New Horizons (diseños gratis de ropa, código de creadora
  `MA-5858-0335-8877`), Brawlhalla, Fall Guys, Hero Wars, State of Survival,
  The Walking Dead: Survivors, Pinball FX.
- **Figuras oficiales (referencia 3D real)**:
  - **Gaming Heads / Sideshow**: estatua "Tomb Raider: Lara Croft" polystone
    1:6 (~14"), pose clásica con pistolas listas, basada en el arte de
    portada original · https://www.sideshow.com/collectibles/tomb-raider-lara-croft-gaming-heads-903481/
    · más ediciones exclusivas de TR III y Survivor y Rise ·
    https://www.gamingheads.com/rise-of-the-tomb-raider-lara-croft-exclusive-edition-statue.html
    · ✅ (Sideshow + Gaming Heads, dos tiendas oficiales del fabricante).
  - **Weta Workshop**: estatua exclusiva 1:4 de Shadow of the Tomb Raider,
    revelada en la San Diego Comic-Con 2018, esculpida digitalmente en ZBrush
    por Daniel Cockersell, edición limitada a 750 piezas; y una estatua 1:4
    "Lara Croft: Quest for Avalon" (basada en Underworld, 2025-2026) ·
    https://www.wetanz.com/us/lara-croft y
    https://tombraiderhorizons.com/2025/07/22/weta-workshop-unveils-lara-croft-quest-for-avalon-statue/
    · ✅ (sitio oficial de Weta + prensa especializada del fandom).
- **Cosplay bien hecho, con apoyo oficial**: Crystal Dynamics mantiene una
  sección permanente **"Cosplay"** en tombraider.com con guías oficiales de
  vestuario (ver punto 15) y pide a los fans compartir sus fotos con
  `#TombRaider` para salir destacados en los canales oficiales —confirma que
  el estudio valida activamente el cosplay de la comunidad, más allá de una
  simple foto suelta · https://www.tombraider.com/news/cosplay · ✅.
- **No encontré** colaboraciones de moda real (tipo Prada/MAC Cosmetics) para
  Tomb Raider más allá de merchandising propio de la marca (pines, ropa con
  el logo, skate deck) en la tienda oficial tombraider.com/news/merch:
  busqué "Tomb Raider Nike", "Lara Croft MAC Cosmetics", "Tomb Raider Prada
  costume" (inglés) y no aparece ningún acuerdo de marca de moda confirmado
  para los videojuegos (si existió fue para las películas con Angelina
  Jolie, fuera del alcance de "imagen del juego" que me toca a mí).

## Lo mejor para la lámina

1. El **Gear Up Guide oficial de Shadow of the Tomb Raider**
   (`hojas/vestuario_02.jpg` nº5) da vestuario exacto con cita textual del
   estudio: es la referencia más segura para dibujar a Lara "de verdad", sin
   inventar materiales.
2. La **captura del puente entre ruinas con niebla** (TR2013,
   `hojas/fondos_03.jpg` nº5) es el mejor fondo "postal" de exploración, ya
   con paleta cálida medida.
3. El **Croft Family Crest** (`hojas/vestuario_02.jpg` nº6) es un símbolo
   compacto y "de objeto real" (un escudo de familia) — perfecto si la
   lámina quiere un emblema tallado en piedra o metal, no un logo plano.
4. El modelo Sketchfab **"Home of Adventure"** (CC Attribution) es la única
   referencia 3D con licencia libre de un *sitio* (no sólo el personaje):
   útil si la lámina se monta en Blender.
5. El **templo maya con farolillos de Shadow** (`hojas/fondos_03.jpg` nº3)
   mezcla ruina antigua con luz cálida de fiesta: sirve si el canal quiere
   una sensación de comunidad/celebración sin perder el tono de exploración.

## No encontré

- ⚠️ Colaboraciones de moda real (Nike, MAC Cosmetics, Prada) para los
  videojuegos de Tomb Raider: no existen, sólo merchandising propio de la
  marca. Búsquedas en inglés: "Tomb Raider Nike", "Lara Croft MAC Cosmetics",
  "Tomb Raider Prada costume".
- ⚠️ Copia legal completa y navegable del artbook *The Art of Survival*
  (BradyGames): confirmado que existe por reseñas (ConceptArtWorld,
  Goodreads), pero no pude leer su contenido interno.
- ⚠️ Hex fiable del emblema de Trinity: la única imagen disponible en la
  wiki está muy oscura (foto in-game de un cadáver), el triángulo se ve
  rojo/granate pero no pude medir un tono estable.
- ⚠️ Origen exacto (artista/Pixiv/DeviantArt) de dos fan art de Safebooru:
  varios enlaces de origen que da la propia Safebooru ya no cargan.
- No busqué en japonés ni coreano más allá del logo/anuncio japonés de 1996
  ya documentado en la propia wiki: Tomb Raider es una franquicia británica
  (Core Design, luego Crystal Dynamics, EE. UU.), así que el foco de "otros
  idiomas" del encargo pesa menos aquí que en una obra japonesa o coreana;
  aun así confirmé que existe logo y anuncio de revista japonesa distintos
  para TR1 (ver punto 1).

## Bitácora de búsqueda

- **Red directa (sin buscador), la mayoría de mis datos**: Fandom API
  `tombraider.fandom.com/api.php` — `action=parse&prop=wikitext` sobre
  `Lara's Outfits` (18 143 caracteres, completo), `Tomb Raider Crossovers`
  (20 936 caracteres, completo), `Tomb Raider (1996 Game)/Artwork`, `Croft
  Family Crest`, `Jeep Wrangler Rubicon and Tomb Raider Bundle`; `action=query
  &list=search&srwhat=text` para "Fortnite", "crossover", "statue figure",
  "cosplay", "Nike/Land Rover/MAC Cosmetics", "Croft family crest coat of
  arms", "Trinity symbol logo"; `action=query&prop=imageinfo&iiprop=url|size`
  para dimensiones exactas de 7 imágenes distintas · Steam API `appdetails`
  para las capturas de Rise (391220), Shadow (750920) y TR2013 (203160) — 24
  capturas descargadas, miradas en `hoja_fondos.jpg` de mi carpeta de trabajo
  y 6 elegidas para `hojas/fondos_03.jpg` · Poly Haven API (`/assets?t=hdris`,
  `/info/colosseum`, `/files/colosseum`) · ambientCG API v2 (`stone`, `moss`,
  `rock`) · tombraider.com directo (curl, sin buscador) para 4 "Cosplay
  Guide"/"Gear Up Guide" (Legend, Shadow, Shadowrunner, TR III Nevada) y la
  lista de la sección `/news/cosplay` y `/news/merch` · Internet Archive
  `advancedsearch.php` (sin resultado para el artbook) · `herramientas/estilo.py`
  sobre 5 renders de vestuario y 6 capturas de fondos + Pillow directo
  (`getpixel`) para hex puntuales de prendas y de los dos símbolos.
- **Buscador web** (inglés, 4 búsquedas de ~50 usadas): "Lara Croft official
  statue Gaming Heads OR PCS Collectibles OR Weta figure" ·
  ""Tomb Raider" official cosplay recognized Crystal Dynamics OR Square Enix
  Comic-Con"" · "Tomb Raider 1996 Japanese PlayStation box art cover
  different Lara Croft" · ""Art of Tomb Raider" OR "Art of Survival" artbook
  Dark Horse Crystal Dynamics concept art".
- **Confirmado con dos fuentes (✅)**: traje icónico TR I-III (wiki + medido),
  material del Legend (cita oficial), Brenoch Adams como director de arte
  (dos Gear Up Guides distintos), tank top+pantalón de Shadow (artículo web +
  imagen oficial con el mismo texto), Fortnite/Call of Duty/Magic (wiki +
  fuente primaria citada en ella), estatuas de Gaming Heads y Weta (tienda
  oficial + prensa del fandom), sección de cosplay oficial (página propia de
  tombraider.com).
- **Imágenes miradas de verdad con Read** (no sólo enlazadas): las 20
  imágenes de `hojas/arte_oficial_01.jpg` (ya hecha por
  `investigar_serie.py`), las 6 que monté en `hojas/vestuario_02.jpg`
  (incluye recortes a resolución completa de TR1 Classic y Shadow Tank Top
  para sacar hex de píxel exacto) y las 6 de `hojas/fondos_03.jpg`, más la
  hoja de 24 capturas de Steam sin recortar en mi carpeta de trabajo antes de
  elegir las 6 finales.

## Cumplimiento del encargo (mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 1. Arte oficial variado | ✅ | Key art 9000×5762, patrón de subpágina "/Artwork" con logos por región (incluido Japón), 24 capturas oficiales de Steam de 3 juegos miradas y 6 elegidas, dos collages de evolución, artbook confirmado (contenido no accesible, declarado en ⚠️) |
| 3. Fan art y 3D con licencia | ✅ | 4 modelos Sketchfab CC verificados por API (incluye un *sitio*, no sólo el personaje), fan art de Safebooru con tamaño real, fotos de cosplay/exposición con licencia CC de Openverse, 2 HDRI CC0 de Poly Haven como referencia de ruinas/cuevas reales |
| 15. Vestuario con hex medidos | ✅ | 5 trajes (TR I-III Classic, Legend, Reboot 2013, Rise, Shadow) con hex medidos con estilo.py/Pillow, citas textuales oficiales con nombre del director de arte para 2 de ellos, toda la lista de variantes por juego de `Lara's Outfits` |
| 16. Fondos de pantalla y paisajes | ✅ | 6 capturas oficiales con paleta medida (estilo.py), enfoque en ruinas/exploración como pide el encargo, sitios con nombre propio (Paititi, Kitezh, Siberia, Croft Manor), wallpapers de Wallhaven con favoritos y licencia declarada como no explícita |
| 19. Texturas 2D | ✅ | 2 símbolos oficiales medidos/descritos (Croft Family Crest, Trinity), cita textual de materiales reales del vestuario (nylon, spandex, poliéster, termoplástico), 3 texturas CC0 equivalentes de piedra/musgo de ambientCG |
| 23. Colaboraciones y cruces | ✅ | Página wiki completa de crossovers con +20 colaboraciones oficiales una por una (Fortnite, Call of Duty, Magic, Final Fantasy×3, Dead by Daylight, Naraka…), 2 líneas de figuras oficiales (Gaming Heads/Sideshow, Weta) con fuente oficial, sección de cosplay oficial de tombraider.com confirmada; moda real declarada como "no encontré", no "no existe" |
| Hojas de contacto (máx. 3) | ✅ | `hojas/arte_oficial_01.jpg` (20 imágenes de la wiki, hecha por investigar_serie.py), `hojas/vestuario_02.jpg` (5 trajes oficiales + Croft Family Crest), `hojas/fondos_03.jpg` (6 capturas oficiales de ruinas/exploración con paleta medida) — las tres miradas con Read antes de citar, todas menos de 3 MB |
| `imagen.json` (mín. 20 referencias) | ✅ | referencias con url, fuente, ancho, alto (medidos donde aplica), qué es, para qué y licencia |

Fin de mi parte. No queda pendiente ningún punto obligatorio de mi rol
(1, 3, 15, 16, 19, 23).
