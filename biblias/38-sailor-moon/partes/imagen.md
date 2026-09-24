# Parte de IMAGEN · Sailor Moon (encargo 38)

Investigador de imagen: puntos **1, 3, 15, 16, 19 y 23** de `ENCARGO.md`. Parte de
`partes/datos-imagen.md` (AniList, Fandom, Danbooru, Safebooru, Openverse) y no
repite esas consultas. Formato: libreta de datos, un dato por línea.

## Hallazgos

### Punto 1 · Arte oficial, en cantidad y variado

- El recolector había dejado hojas de contacto de páginas **equivocadas**
  (`Ami Jr.`, `Rei Jr.`, `Makoto Hanmatsuura`, `Act 47 - Farewell, Minako` — todas
  desambiguaciones erróneas de la búsqueda automática). Comprobado con la API de
  Fandom (`list=search`): las páginas correctas son `Usagi Tsukino / Sailor Moon
  (anime)`, `Ami Mizuno / Sailor Mercury (anime)`, `Rei Hino / Sailor Mars
  (anime)`, `Makoto Kino / Sailor Jupiter (anime)`, `Minako Aino / Sailor Venus
  (anime)`, `Luna (anime)` · ✅ (confirmado con `action=query&list=search`).
- Rehecho con `investigar_serie.py --serie "Sailor Moon" --wiki sailormoon
  --paginas` con las 9 páginas correctas (las 6 protagonistas + Tuxedo Mask,
  Queen Beryl y Chibiusa, para variedad de reparto). Resultado: **369 imágenes
  grandes**, **8 hojas de contacto** en
  `herramientas/referencias/sailor-moon/` (se cortó por tiempo en la 8ª; las 7
  completas ya cubren de sobra, están ordenadas de mayor a menor tamaño). Las
  **3 mejores copiadas a `hojas/`** (miradas con Read, no sólo listadas):
  - `hojas/personajes_01.jpg` (hoja 1, imágenes 1-48): **settei de producción**
    sin color (línea limpia) de las 5 protagonistas — cuerpo entero, frente y
    espalda, con notas de producción en japonés (`決定稿` = "borrador
    definitivo") — más las primeras cartas oficiales a color de Mercury y Mars,
    y bocetos de Mamoru Chiba y Chibiusa niña · ✅.
  - `hojas/personajes_02.jpg` (hoja 2, imágenes 49-96): carátulas de LaserDisc
    de *Sailor Moon S* y *SuperS* (10 volúmenes, arte pintado de grupo),
    postales oficiales, Usagi/Rei/Ami de civil en escenas cotidianas (café,
    playa), Mamoru de civil · ✅.
  - `hojas/personajes_03.jpg` (hoja 3, imágenes 97-144): **calendarios de
    escritorio oficiales** (arte de grupo con las 5 en uniforme), a Queen
    Nehelenia (villana, #118), fotogramas de episodios con las 5 en poses de
    grupo y de acción, ropa de exterior/S Movie de Rei · ✅.
- **Poses VIVAS** confirmadas (pedidas explícitamente por el dueño, no "de pie
  con una ropa"): grupo completo (`hojas/personajes_03.jpg` #121-127, #136,
  #140-144; referencia suelta `SII.jpg` 2435×3457 con las 5 + Luna + Artemis);
  en acción/salto (Sailor Mars pateando, carta oficial `Sailor.Mars.
  full.2554554.jpg`, 4048×5728, inserto de LD *SuperS* vol.4); con su objeto
  (Ami con libros, Makoto saludando con la mano, Usagi con su maletín escolar,
  todas del infobox oficial de cada personaje en Fandom) · ✅.
- **Fuera de la wiki**: portada y banner oficiales en AniList (id 530,
  `bx530-O8q6KpJ244Qk.jpg` 460×690 y banner 1900×600, medidos con estilo.py) ·
  ✅. **30º aniversario (2022)**: *Pretty Guardian Sailor Moon Museum* en
  Roppongi (jul-dic 2022), con **key visual nuevo de Naoko Takeuchi** y más de
  180 dibujos originales a color inéditos expuestos por primera vez — Anime
  News Network, 3 artículos distintos (abr y jun 2022) · ✅ (dos fuentes:
  ANN + moshimoshi-nippon.jp).
- Hoja de modelo (settei) del vestido de la Princesa Serenity
  (`UsaSettei8.png`, 9359×6800, la imagen individual más grande de toda la
  wiki) — línea limpia sin color, con la nota "月のプリンセス" (Princesa de la
  Luna) y "決定稿" (versión definitiva) · ✅.

### Punto 3 · Fan art y 3D con licencia (referencia, nunca para pegar)

- **Fan art** (Safebooru, ya en `datos-imagen.md`, 6 personajes con top-6 cada
  uno, enlace + tamaño + autor/origen): el más votado de toda la serie es un
  fan art de Usagi en una "tabla periódica de personajes japoneses" (17 puntos,
  1600×1006, origen sankakustatic) · ✅. No repetido aquí; ver esa parte.
- **Modelos 3D con licencia libre** (Sketchfab, `type=models&downloadable=true`,
  la consulta automática del recolector había fallado — repetida a mano y sí
  respondió):
  - Moon Stick (bastón de transformación) — 3 versiones distintas (carlostorresvfx,
    JRxRay, feryzapata, fairvals, maxleite), todas **CC Attribution** · ✅.
  - Broche/Compact de Sailor Moon (`travka`, miniatura 1920×1080) y **Cosmic
    Heart Compact** con *rig* (RazyBerry) — **CC Attribution** · ✅.
  - Luna (la gata) modelada por `foxoutdabox` — **CC Attribution** · ✅.
  - Tamagotchi "Pet Sailor Moon" (Aldemona), frasco de perfume con diseño
    Sailor Moon (lilith) — **CC Attribution**, curiosidades de merchandising
    en 3D · ⚠️ (una sola fuente cada uno, son modelos de fans individuales).
  - Poly Haven: no tiene modelos ni HDRIs específicos de Sailor Moon (es un
    banco genérico de materiales/HDRI, no de personajes) — comprobado, sin
    resultados relevantes.

### Punto 15 · Vestuario, colores medidos, accesorios, peinado

Medido con `herramientas/estilo.py` (Pillow) sobre el **retrato oficial del
infobox de cada personaje en Fandom** (imágenes con fondo transparente, civiles
las 4 primeras, Usagi con civil+fuku juntas), y **visto con Read** para
confirmar qué prenda es cada hex:

- **Usagi Tsukino**: uniforme de Juban de civil — azul marino `#222993`, moño y
  cuello con rayas rojas `#C93A2E`, medias blancas. Como Sailor Moon: mismo
  azul marino en el cuello, falda y moño rojos `#C93A2E`, broche y tiara dorados
  `#ECCD1E`, botas rojas hasta el muslo · ✅ (medido + visto en la misma
  imagen, `Usagi_Tsukino_Sailor_Moon_-_Anime.png`).
- **Ami Mizuno**: uniforme de civil azul marino `#20308D` con moño rojo
  `#C2191A`, mocasines oscuros, pelo corto azul oscuro a la altura del cuello,
  a veces con gafas de lectura · ✅. Como Sailor Mercury (texto de la wiki,
  `action=parse`, sección Appearance): leotardo blanco con hombreras, cuello
  azul con dos rayas blancas, falda azul, tiara dorada con gema azul ovalada,
  botas azules cortas con ribete triangular blanco · ✅ (dos fuentes: texto de
  la wiki + etiquetas de Danbooru "blue_sailor_collar, blue_skirt, blue_boots"
  ya en `datos-imagen.md`).
- **Rei Hino**: uniforme de civil gris con lazo granate `#453B31`/`#442D32`
  (medido; confirma el texto "dark gray with red linings"), falda gris,
  calcetines blancos con rayas rojas, pelo largo negro con brillo violeta ·
  ✅. Como Sailor Mars (visto en la carta oficial `Sailor.Mars.
  full.2554554.jpg`, pose en salto): fuku roja/naranja-roja, guantes blancos,
  moño morado a la espalda, tiara dorada, botas rojas de tacón · ✅ (texto de
  wiki + visto directamente en el arte oficial).
- **Makoto Kino**: uniforme de civil caqui/mostaza `#BDB162` con corsé cruzado
  blanco al frente, coleta sujeta con liga verde, pendientes de rosa rosa; es
  la más alta de las Inner Senshi · ✅. Como Sailor Jupiter (texto de wiki):
  cuello y falda verdes, moño rosa, botas verdes — no se pudo medir hex de la
  fuku transformada en una imagen a color propia (⚠️ una sola fuente: el
  texto de la wiki; confirmado por las etiquetas Danbooru "green_sailor_collar,
  pink_bow" de `datos-imagen.md`).
- **Minako Aino**: uniforme de civil azul `#35258F` con pañuelo y moño rojos,
  pelo rubio muy largo suelto con lazo rojo grande · ✅. Como Sailor Venus
  (texto de wiki + Danbooru "orange_sailor_collar, orange_skirt"): cuello y
  falda naranjas, moño azul — la civil y la fuku usan paletas opuestas
  (azul↔naranja), dato útil para no confundirlas al dibujar · ✅.
- **Luna**: pelaje negro azulado `#1F2333`/`#2D3248`, luna creciente dorada en
  la frente, ojos rojos (en la primera temporada) · ✅ (medido + descripción
  de la wiki).
- **Ropa icónica que todo el mundo reconoce**: el fuku de Sailor Moon (cuello
  azul marino, moño rojo, botas rojas) y el uniforme escolar de Juban (mismo
  azul marino con el moño rojo) — es la MISMA paleta civil/heroína en Usagi, a
  diferencia de sus compañeras que cambian de color al transformarse · ✅.
- **Peinado y accesorios** (visto en los retratos ya citados + texto de wiki,
  `datos-imagen.md` ya trae las etiquetas de Danbooru que lo confirman):
  Usagi lleva **odango** (dos chongos con coletas larguísimas hasta el suelo);
  Ami el pelo corto a la altura del mentón y a veces gafas de lectura; Rei el
  pelo suelto muy largo con brillo violeta; Makoto una **coleta alta sujeta
  con una liga verde** y pendientes de rosa; Minako el pelo rubio suelto muy
  largo con un **lazo rojo grande** de adorno; Luna una marca de luna
  creciente dorada en la frente tanto en gata como en forma humana · ✅.
- **Ropa por temporada** (texto completo de wiki, `action=parse&prop=wikitext`,
  sección "Appearance", una por personaje — no repetir la consulta, ya
  guardada): las 4 (Ami, Rei, Makoto, Minako) cambian su outfit casual
  "principal" en la 3ª temporada (*Sailor Moon S*) y de nuevo visten uniforme
  compartido de instituto en *Sailor Stars* (5ª). Ejemplo Rei: campera turquesa
  con cuello alto naranja pálido (temporadas 1-2) → camisa azul de manga larga
  con chaleco rojo de cremallera (desde *S*). El detalle completo de las 4 está
  en el wikitext ya bajado (no hace falta volver a pedirlo).

### Punto 16 · Ciudades, paisajes y fondos de pantalla

- **Templo Hikawa** (santuario de Rei): imagen de fondo oficial,
  `Hikawa-shrine.jpg` (640×480, baja resolución de la propia wiki), atardecer
  con cielo degradado — paleta medida con estilo.py: `#A6D2DE` celeste,
  `#E3B9E1` rosa de nubes, `#4A8851` verde de árboles, sombreado "degradado /
  pintado" (fondo de producción, no cel-shading) · ✅.
- **Game Center Crown** (arcade de Motoki): sólo se encontró una viñeta de
  manga en blanco y negro (`Sm.gamecentercrown.manga.png`, 379×480) — sin
  color de referencia, ⚠️ una sola fuente y sin paleta útil.
- Juban (el distrito/barrio ficticio): página de la wiki existe pero sin imagen
  de fondo propia — ⚠️ no encontré una vista panorámica oficial del barrio,
  búsqueda hecha en la wiki (`list=search`) y en Google.
- **Fondos de pantalla de fans en alta** (Wallhaven, `/api/v1/search`, la
  consulta automática del recolector volvió vacía — repetida a mano y sí dio
  resultados): 238 resultados para "sailor moon" en la categoría anime; 177 de
  ellos ≥1920×1080. Los 2 más guardados: `wallhaven-g7x37l` (3900×5800, 339
  favoritos) y `wallhaven-x1xy9l` (3840×2160, 292 favoritos), ambos SFW · ✅
  (fecha y nº de favoritos verificables en la API, Wallhaven no publica el
  nombre del autor por imagen).
- **Fondos oficiales sueltos**: los fotogramas de fondo (detrás de las
  escenas de grupo) en `hojas/personajes_03.jpg` muestran cerezos en flor
  (#99, escena de primavera) y un patio escolar — son capturas de episodio,
  más del punto 2/4 (equipo de vídeo); anotado aquí para que el redactor no
  repita la búsqueda de "fondos oficiales de Sailor Moon".

### Punto 19 · Texturas 2D

- **Tramas de manga (screentones)**: no hay un paquete de tramas *scaneadas*
  del propio manga de Naoko Takeuchi con licencia libre (es material con
  copyright) → equivalente libre encontrado: **CLIP STUDIO ASSETS "Manga
  Screentone Pack 1"**, gratuito, tramas de punto clásicas · ✅. Alternativa:
  pinceles gratuitos de GraphicsBunker para Photoshop/Procreate/Clip Studio ·
  ✅ (dos fuentes, dos paquetes distintos).
- **Grano de papel**: `Paper006`/`Paper001`/`Paper003` de ambientCG, CC0,
  varias variantes de grano fino de papel de manga · ✅.
- **Patrones de ropa**: no hay tela con estampado propio en el vestuario
  principal (los uniformes son de color liso con vivos), salvo el pijama de
  Usagi (texto de la wiki: "pink shirt with pink pajamas") — ⚠️ no encontré
  una imagen clara del estampado del pijama, sólo la descripción en texto.
  Tela lisa equivalente: `Fabric081C`/`Fabric061`/`Fabric066` de ambientCG
  (CC0, weave fino, textura real de uniforme escolar) · ✅.
- **Emblemas y logos**: la luna creciente dorada (símbolo de Usagi/Luna/la
  Casa Lunar) y los símbolos astrológicos de cada planeta en el tiara/pendientes
  de cada Sailor Guardian (Mercurio ☿, Marte ♂, Júpiter ♃, Venus ♀) — descritos
  en el texto de la wiki y visibles en los retratos ya citados; ⚠️ no encontré
  un archivo de imagen dedicado sólo al emblema/símbolo suelto en la wiki
  (busqué `symbol`, `crest`, `emblem`, `crescent` en los títulos de imagen sin
  resultado), pero el símbolo se ve con claridad en las cartas oficiales y los
  settei ya citados.
- **Texturas de sitio equivalentes** (con el punto 4, "que no falte ninguna
  capa"): `Marble012`/`Onyx015` de ambientCG (CC0) para el mármol del Templo
  Hikawa y del Milenio de Plata.

### Punto 23 · Colaboraciones y cruces

- **Moda**: Sailor Moon × **Uniqlo UT** (2019, línea de camisetas) — SoraNews24
  ✅. Sailor Moon × **Samantha Vega / Samantha Thavasa** (Isetan, bolsos y
  carteras con el diseño del Cosmic Heart Compact) — Tokyo Otaku Mode + Anime
  News Network, dos fuentes ✅.
- **Cafés temáticos** (traen arte y poses nuevas, como pide el punto): **Q-Pot
  Café** (colaboración anual desde 2014, cada verano en Harajuku, pasteles con
  temática de transformación) y **Sailor Moon Eternal Café** (2020-2021, un
  plato por cada Guardiana: parfait de Ami, curry de Minako, etc.) — SoraNews24
  + Honey's Anime, dos fuentes ✅.
- **Figuras oficiales** (pose = referencia 3D real, como pide el punto):
  **S.H.Figuarts** de Bandai/Tamashii Nations, ~14 cm, con piezas
  intercambiables (3 expresiones, manos, 2 Moon Stick, efecto de tiara
  lanzada, Luna articulada) — ficha oficial en shfiguarts.com ✅. Hay
  versión "Animation Color Edition" (colores del anime de los 90) y "Crystal
  Star Compact Edition" (de *Sailor Moon R*).
- **Cosplay bien hecho** (materiales y volumen reales, como pide el punto):
  Sailor Pluto y Kunzite de la cosplayer "Alena", **Best Master Craftsmanship**
  en Midoricon 2014 y **Best Advanced Craftsmanship** en Ikasucon 2015 — blog
  "…And Sewing Is Half The Battle!" ⚠️ (una sola fuente; el blog no detalla
  telas ni técnicas de construcción, sólo el resultado y el premio — búsqueda
  adicional por tutoriales de tela/patronaje no dio resultados con detalle
  técnico verificable).
- **Evento grande / exposición**: *Pretty Guardian Sailor Moon Museum* (30º
  aniversario, 2022, Roppongi) — ya citado en el punto 1, aplica también aquí
  como evento de colaboración con más de 600 piezas expuestas · ✅.
- **Videojuegos/crossovers tipo gacha o battle royale**: **no encontré**
  ninguna colaboración oficial confirmada (ni Fortnite ni un gacha). Busqué
  "Sailor Moon Fortnite" (sólo hay peticiones de fans/change.org, nada
  oficial) y "Sailor Moon gacha collaboration" (sin resultados oficiales). Sí
  existe el videojuego propio con licencia *Sailor Moon Drops* (gacha oficial
  de la propia franquicia, no un crossover) — mencionado por
  `investigar_serie.py` en su documentación como ejemplo, pero no investigado
  a fondo aquí porque los videojuegos de la franquicia son punto 11 (texto).

## Lo mejor para la lámina

1. La carta oficial de Sailor Mars en pleno salto/patada
   (`Sailor.Mars.full.2554554.jpg`) es la prueba más clara de una pose VIVA y
   en acción real, no un personaje de pie.
2. El par civil+fuku de Usagi en una sola imagen (`Usagi_Tsukino_Sailor_Moon_-
   _Anime.png`) da los 3 hex exactos (azul `#222993`, rojo `#C93A2E`, dorado
   `#ECCD1E`) que definen su paleta en cualquier forma.
3. `SII.jpg` (las 5 + Luna + Artemis juntas) sirve de referencia directa para
   cualquier lámina en grupo.
4. El Moon Stick y el Cosmic Heart Compact en Sketchfab (CC Attribution) son
   objetos reales que se pueden llevar a Blender tal cual, con crédito.
5. El Templo Hikawa al atardecer (paleta pastel rosa-celeste) es el sitio con
   más personalidad lumínica encontrado; mejor que un fondo genérico de
   instituto.

## No encontré

- ⚠️ Modelos 3D de **sitios** de la serie (Templo Hikawa, Crystal Tokyo) con
  licencia libre en Sketchfab — sólo objetos pequeños, no arquitectura.
  Búsqueda: `sketchfab.com/v3/search?q=hikawa+shrine` y `q=crystal+tokyo` sin
  resultados relevantes con licencia.
- ⚠️ Un fondo de pantalla **oficial** (no de fans) publicado por Toei/Kodansha
  en alta resolución — el sitio oficial japonés de streaming no publica pack
  de wallpapers descargables; sólo se encontraron los de Wallhaven (de fans).
- ⚠️ Estampado textil real del pijama de Usagi (sólo hay descripción en
  texto, ninguna imagen clara del patrón).
- ⚠️ Detalle técnico (telas, moldes) de los cosplays premiados citados en el
  punto 23 — el blog fuente no lo detalla.
- ⚠️ Crossover oficial con un juego externo tipo Fortnite o gacha de terceros
  — no existe, comprobado con dos búsquedas distintas.

## Bitácora de búsqueda

- Fandom API (`sailormoon.fandom.com/api.php`, `list=search` y
  `action=parse&prop=wikitext|sections`), en inglés: nombres correctos de
  página de Usagi, Ami, Rei, Makoto, Minako, Luna, Tuxedo Mask, Queen Beryl,
  Chibiusa, Hikawa Shrine, Game Center Crown, Juban.
- `herramientas/investigar_serie.py --serie "Sailor Moon" --wiki sailormoon
  --paginas …` (9 páginas correctas) → 369 imágenes, 8 hojas de contacto (7
  completas por límite de tiempo).
- Sketchfab API (`api.sketchfab.com/v3/search?type=models&downloadable=true`),
  en inglés: "sailor moon", "moon stick sailor moon", "sailor moon compact",
  "luna cat sailor moon", "sailor moon tiara", "hikawa shrine", "crystal
  tokyo".
- Wallhaven API (`wallhaven.cc/api/v1/search`), en inglés: "sailor moon",
  "sailor moon aesthetic".
- ambientCG API (`ambientcg.com/api/v2/full_json`), en inglés: "fabric",
  "paper", "marble".
- Danbooru/Safebooru: ya cubierto por `datos-imagen.md`, no repetido.
- WebSearch (español e inglés, ~8 búsquedas de las ~50 de cupo): colaboración
  Uniqlo/Samantha Vega/Bandai, café Harajuku, figuras S.H.Figuarts, crossover
  Fortnite/gacha, meme "Redraw Challenge" y cosplay, cosplay World Cosplay
  Summit, 30º aniversario/museo 2022.
- Imágenes MIRADAS con Read (no sólo listadas): las 3 hojas de contacto
  completas, el settei del vestido de la Princesa Serenity, los 6 retratos
  civiles (Usagi, Ami, Rei, Makoto, Minako, Luna) y la carta oficial de Sailor
  Mars en acción.
- Colores medidos con `herramientas/estilo.py` (Pillow) sobre 11 imágenes:
  portada de AniList, settei de Usagi, los 6 retratos de personaje, la carta
  de Sailor Mars, el Templo Hikawa y Game Center Crown.
