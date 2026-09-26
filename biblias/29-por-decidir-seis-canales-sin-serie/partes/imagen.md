# Investigador de IMAGEN · repaso · 29-por-decidir-seis-canales-sin-serie

Puntos 1, 3, 15, 16, 19, 23 de ENCARGO.md. Este encargo es especial: no es una
serie, son **7 propuestas** (Super Mario Galaxy, Phineas y Ferb, Bleach,
Wreck-It Ralph, Monsters Inc./University, Sing, Los Simpson para las salas de
voz). `biblia.md` ya tiene mucho de mis puntos hecho por quien la escribió
(2.809 imágenes en 62 hojas, Sketchfab con licencia, hex medidos con Pillow).
Aquí confirmo lo que ya hay, corrijo lo que estaba «a ojo» y añado lo que
`datos-imagen.md` no pudo traer (el recolector falló: la obra aún no tenía
nombre cuando corrió, ver «Fuentes que fallaron» en ese archivo) y lo que la
propia biblia marcó como pendiente en su §9.2 («Fan art: no lo busqué»).

No hay sección `## ` con mis puntos etiquetada por rol (`seccion.py --rol
imagen` no encuentra nada: los títulos son «1 · #destacados → Super Mario
Galaxy», etc., no palabras clave de rol). Leí las 7 secciones enteras
(líneas 109-1636 de `biblia.md`) para saber qué faltaba.

## Hallazgos por punto

### Punto 1 · Arte oficial variado

- Ya está hecho a fondo por la primera pasada: 7 wikis de Fandom por la API
  de `investigar_serie.py`, 2.809 imágenes grandes en 62 hojas de contacto
  (carpeta de trabajo, no en el repo) · biblia.md §1-§6 · ✅ (vistas y
  citadas con número, tamaño y URL en cada sección).
- No repetí esta parte: sería gastar de más en algo que ya está confirmado.

### Punto 3 · Fan art y 3D con licencia

- **3D con licencia**: ya lo hizo la primera pasada para las 7 series
  (Sketchfab, CC BY, con crédito) · biblia.md, tablas «Modelos 3D libres» de
  cada sección · ✅.
- **Fan art**: la propia biblia dice en su §9.2 «no lo busqué». Lo añado
  ahora, uno por serie, en Danbooru filtrado a `rating:g` (nada explícito),
  con artista, tamaño y enlace al post (nunca al archivo suelto, para dejar
  el crédito):
  - Rosalina/Estela: [masoq](https://danbooru.donmai.us/posts/11099671),
    2980×2412 ✅ (visto y medido).
  - Kurosaki Ichigo (Bleach): [tokishima_sikuka](https://danbooru.donmai.us/posts/5787798),
    2736×4096 ✅.
  - Vanellope: [juanmao](https://danbooru.donmai.us/posts/3152497), 2048×1328 ✅.
  - Mike Wazowski: [kukakooo](https://danbooru.donmai.us/posts/5421397), 2048×1369 ✅.
  - Phineas y Ferb juntos: [nokonorii](https://danbooru.donmai.us/posts/6926732), 722×450 ✅.
  - Sing (grupo): [jayivee](https://danbooru.donmai.us/posts/10928302), 4096×4096 ✅.
  - Bart Simpson: [cogum3li](https://danbooru.donmai.us/posts/6297355), 2048×2040 ✅.
  - Nota: son **sólo referencia** (pose, color, composición), nunca para
    pegar en la lámina, como pide el punto 3.

### Punto 15 · Vestuario con hex medidos

La biblia ya mide bien el vestuario de Estela (turquesa `#54C0B4`, corona,
broche) con la hoja `p29-mario-galaxy`. Bajé 5 imágenes oficiales más y medí
con Pillow los hex que estaban **«⚠️ a ojo»** (adivinados, no medidos):

- **Shūhei Hisagi** (Bleach), cuerpo entero, [Hisagi Anime Fullbody.png](https://static.wikia.nocookie.net/bleach/images/7/73/Hisagi_Anime_Fullbody.png)
  1050×1500: shihakusho (uniforme negro) `#26272D` (no `#121212` como estaba
  a ojo: es un negro azulado, no negro puro), obi/faja blanca `#B3B1AA`,
  brazalete del 9º escuadrón `#BBAE7F` ✅ (medido, sustituye a biblia.md l.830).
- **Vanellope von Schweetz** (Ralph), arte oficial completo,
  [Vanellopewirdisney.png](https://static.wikia.nocookie.net/wreckitralph/images/a/ac/Vanellopewirdisney.png)
  1728×3000: sudadera verde menta `#5F8C73` en sombra / `#79AA8D` en luz (no
  `#4FC3A1`, más turquesa de lo real), medias a rayas `#60AF90`, lazo rojo
  caramelo, falda marrón plisada, botas negras ✅ (medido, corrige biblia.md
  l.1065).
- **Sulley** (Monsters, Inc.), arte de *Monsters at Work*,
  [SulleyMAW.png](https://static.wikia.nocookie.net/pixar/images/e/e7/SulleyMAW.png)
  939×1268: pelaje verde azulado `#2C7D74` en sombra / `#559C94` en luz,
  manchas `#234163` (azul-morado oscuro, no el morado claro `#8A4FBF` que
  estaba a ojo) ✅ (corrige biblia.md l.1290-1291).
- **Mike Wazowski**, arte de *Monsters at Work*,
  [MikeMAW.png](https://static.wikia.nocookie.net/pixar/images/9/96/MikeMAW.png)
  763×775: piel verde oliva `#5C7531` en sombra / `#87A851` en luz (más
  amarillo que el verde lima `#9BCB3C` a ojo), iris `#375B5B` (más apagado
  que el `#3AB4E8` de Sulley que se había puesto para «azul de Sulley»: ese
  valor no correspondía a ninguno de los dos) ✅ (corrige biblia.md l.1289 y
  l.1290; nota: no llevan ropa, son piel/pelaje, lo más cercano a
  «vestuario» que tienen).
- **Heinz Doofenshmirtz**, retrato oficial de cuerpo entero,
  [Doofenshmirtz_Portrait.jpg](https://static.wikia.nocookie.net/phineasandferb/images/5/5d/Doofenshmirtz_Portrait.jpg)
  800×1000: bata de laboratorio blanca `#FFFFFD`, camisa/corbata negra
  `#020202`, pelo castaño `#773B16`. **No hay morado en su ropa ni su piel**:
  el `#6A3D9A` que biblia.md l.556 tenía «a ojo» no aparece en ningún arte
  oficial que revisé (comprobado también en 3 fotogramas de tráileres de la
  serie clásica). Lo marco como corregido, no como confirmado: si el dueño
  recuerda un morado concreto (¿una escena, un traje de disfraz suyo?), que
  lo diga con el capítulo.

### Punto 16 · Fondos de pantalla oficiales y de fans (con tamaño y autor)

**Esto faltaba entero**: no hay ninguna sección de fondos de pantalla en
`biblia.md`, y `datos-imagen.md` trajo la sección de Wallhaven vacía (el
recolector buscó literalmente «proponer», la palabra del encargo, no el
nombre de cada serie, porque aún no estaban elegidas). Consulté la API de
Wallhaven directamente por cada serie ya elegida, y Alphacoders/Wallpaper
Abyss donde Wallhaven no tenía nada:

- **Super Mario Galaxy / Rosalina**: [wallhaven-2yrr3g](https://wallhaven.cc/w/2yrr3g),
  1920×1080, subido por **vye18756**, 128 favoritos, pixel art de Rosalina ✅.
- **Phineas y Ferb**: Wallhaven no tuvo **ningún** resultado (probé «Phineas
  and Ferb», «Phineas Ferb», «Phineas y Ferb», «Phineas Flynn», «Candace
  Flynn»: 0 en todas). En **Wallpaper Abyss/Alphacoders**: [Perry y
  Doofenshmirtz](https://wall.alphacoders.com/big.php?i=860513), 1920×1080,
  subido por **Perceval21** ✅ (tamaño confirmado en la propia página, campo
  `width`/`height`).
- **Bleach**: [wallhaven-lq3g3p](https://wallhaven.cc/w/lq3g3p), 1920×1200,
  grupo (Ichigo, Rukia, Byakuya, Renji, Hitsugaya), subido por
  **sasukelric**, 33 favoritos ✅.
- **Wreck-It Ralph**: [wallhaven-45k535](https://wallhaven.cc/w/45k535),
  3840×2160, cartel de la película (2012), subido por **JosephTeAu** ✅.
- **Monsters University** (para #general-doblaje/sala Aula):
  [wallhaven-0q6zxr](https://wallhaven.cc/w/0q6zxr), 4096×2304, subido por
  **zuki**; y [wallhaven-43g97v](https://wallhaven.cc/w/43g97v), 2880×1800,
  subido por **poune** ✅ (dos alternativas).
- **Sing**: Wallhaven sólo tuvo 1 resultado (`wallhaven-3zedv9`, 1920×1080)
  y era de otra película («Sing a Bit of Harmony», china, no la de
  Illumination): **falso positivo, descartado**. En Alphacoders sí hay la
  correcta: [Buster Moon](https://wall.alphacoders.com/big.php?i=813662),
  1920×1080 ✅.
- **Los Simpson** (sala Radio 24/7): [wallhaven-o3r2kl](https://wallhaven.cc/w/o3r2kl),
  1920×1080, estilo LoFi de Bart Simpson, subido por **zenphyr**, 147
  favoritos ✅.
- **Aviso sobre Wallhaven**: sus resultados no siempre son de la serie
  buscada; varios de los primeros resultados por «Monsters Inc», «Super
  Mario Galaxy» o «The Simpsons» eran **carteles mezcla** con 6-8 franquicias
  a la vez (Sonic, Naruto, Bowser, *Lord of the Rings* con Gandalf...) o de
  otra obra con nombre parecido. Los descarté todos y sólo dejé los que de
  verdad muestran la serie (comprobado con las etiquetas de la API, campo
  `tags`).

### Punto 19 · Texturas 2D

La biblia ya tiene buenas texturas **3D/PBR** (Poly Haven, CC0) para cada
sitio. Lo que pide el punto 19 además son **patrones 2D** (tramas, grano,
pinceladas, emblemas) con su licencia:

- **Tramas de manga (Bleach)**: [Manga Screentone Pack 1](https://assets.clip-studio.com/en-us/detail?id=2142037),
  gratis en Clip Studio Assets (licencia de uso estándar de Clip Studio,
  gratuita) ✅. Sirve para la revista *Seireitei Tsūshin* y cualquier viñeta
  de la lámina de #noticias-anime.
- **Pixel art / dithering retro (Wreck-It Ralph, los letreros LED y las
  recreativas)**: [itch.io, activos con licencia CC0 etiquetados «pixel
  art»](https://itch.io/game-assets/free/tag-cc0/tag-pixel-art) — decenas de
  packs de texturas y patrones de 8-16 bits, cada uno con su ficha de
  licencia CC0 propia (comprobar la del pack elegido al bajarlo) ⚠️ (listado
  general, no un pack concreto: hay que elegir uno en el momento de montar
  la lámina).
- Emblemas y logos: los del punto 25 (símbolos del mundo) son del rol de
  texto; aquí sólo dejo el material para pintarlos encima (el screentone y
  el pixel art de arriba).

### Punto 23 · Colaboraciones y cruces, figuras oficiales y cosplay

**Esto faltaba entero** (ni «colabora», ni «crossover», ni «cosplay», ni
«figura oficial» aparecían en `biblia.md`). Añado una colaboración/cruce real
y una figura o cosplay por serie prioritaria:

- **Super Mario Galaxy / Rosalina**: figura oficial **amiibo de Rosalina**
  (serie Super Smash Bros., Target en EE. UU., 1 de febrero de 2015, con su
  varita estelar) ✅ ([Nintendo, tienda
  oficial](https://www.nintendo.com/us/store/products/amiibo-rosalina-super-smash-bros-100722/),
  [Amiibo Wiki](https://amiibo.fandom.com/wiki/Rosalina_(Super_Smash_Bros.))).
  **Cosplay bien hecho**: disfraz comercial de Takerlama (edición película
  2026), satén cristal verde/turquesa con forro de crepé, corona, broche y
  pendientes de estrella ✅ ([Takerlama](https://www.takerlama.com/products/rosalina-princess-dress-cosplay-costume-the-super-mario-galaxy-movie-fancy-dress-takerlama)).
- **Phineas y Ferb**: dos especiales crossover reales de Disney: **Mission
  Marvel** (16 ago. 2013, Iron Man/Thor/Hulk/Spider-Man pierden sus poderes)
  y **Star Wars** (26 jul. 2014, tras la compra de Lucasfilm) ✅
  ([Wikipedia: Mission Marvel](https://en.wikipedia.org/wiki/Phineas_and_Ferb:_Mission_Marvel),
  [Wikipedia: Star Wars](https://en.wikipedia.org/wiki/Phineas_and_Ferb:_Star_Wars),
  [Hollywood Reporter](https://www.hollywoodreporter.com/tv/tv-news/phineas-ferb-creators-marvel-superheroes-604392/)).
  Traen **poses y ropa nuevas** (uniformes de Los Vengadores, de Jedi):
  útiles si se quiere una lámina 2 de #eventos.
- **Bleach**: colaboración con **Fortnite** (anunciada en Jump Festa,
  diciembre 2025; skins de Ichigo, Rukia, Uryū y Orihime; torneo «Bleach
  Cup», 19 dic. 2025; cosméticos en tienda desde el 20 dic. 2025) ✅
  ([Vandal](https://vandal.elespanol.com/noticia/1350786043/bleach-aterriza-en-fortnite-ichigo-rukia-y-mas-personajes-del-manganime-combatiran-en-el-battle-royale/),
  [LevelUp](https://www.levelup.com/noticia/fortnite-y-bleach-tendran-una-colaboracion-cuando-inicia-y-que-personajes-de-tite-kubo-llegaran-al-battle-royale/),
  [Kotaku ES](https://es.kotaku.com/fortnite-amplia-su-universo-con-un-cruce-que-muchos-pedian-llego-la-colaboracion-con-bleach-2000030547)).
  Trae **ropa nueva estilo battle royale**: pose de referencia si se quiere
  una versión "gamer" de Ichigo para #noticias-gaming en vez de
  #noticias-anime.
- **Wreck-It Ralph**: la escena de **las 14 princesas Disney** con Vanellope
  (*Ralph Breaks the Internet*, 2018) es el cruce más citado de la
  franquicia ✅ ([Den of Geek](https://www.denofgeek.com/movies/ralph-breaks-the-internet-disney-princesses-scene/),
  [Critical Media Project](https://criticalmediaproject.org/wreck-it-ralph-2-ralph-breaks-the-internet-vanellope-meets-disney-princess/)).
  **Figuras oficiales**: Ralph y Vanellope aparecieron como personajes
  jugables con figura física en **Disney Infinity** ✅ (mismas fuentes,
  + [Disney Wiki](https://disney.fandom.com/wiki/Vanellope_von_Schweetz)).
- **Monsters, Inc./University**: el mundo **Monstropolis** es un mundo
  jugable completo de **Kingdom Hearts III** (2019), con Sora, Donald y
  Goofy disfrazados de monstruos ✅ ([Kingdom Hearts
  Wiki](https://www.khwiki.com/Funko_Pop!)). Esas versiones tienen **Funko
  Pop oficiales** (Sora #407, Donald, Goofy #409 «Monsters Inc.», algunos
  exclusivos de GameStop/Hot Topic) ✅ (misma fuente + fichas de
  [Amazon](https://www.amazon.com/Funko-Pop-Disney-Collectible-Multicolor/dp/B07DFGTG8H)
  y [BoxLunch](https://www.boxlunch.com/product/funko-pop-disney-kingdom-hearts-iii-sora-monsters-inc.-vinyl-figure/11569682.html)).
  Sirve como referencia de **pose 3D estilizada** para Mike y Sulley.
- **Sing**: atracción real **Sing on Tour**, espectáculo musical inmersivo
  en Universal Studios Japón y Universal Studios Pekín ✅
  ([Wikipedia: Sing (franchise)](https://en.wikipedia.org/wiki/Sing_(franchise))).
  No encontré una colaboración de marca o *crossover* con otro personaje
  (⚠️, ver «No encontré»).
- **Los Simpson** (sala Radio 24/7): la colaboración real más famosa de la
  franquicia: **12 tiendas 7-Eleven de EE. UU. y Canadá se convirtieron en
  Kwik-E-Mart de verdad** en julio de 2007, para promocionar la película,
  vendiendo cereal KrustyO's y cómics de Radioactive Man, con «Squishees» en
  vez de Slurpees ✅ ([Wikipedia: Kwik-E-Mart](https://en.wikipedia.org/wiki/Kwik-E-Mart),
  [Wikinews](https://en.wikinews.org/wiki/A_dozen_7-Elevens_transformed_into_Kwik-E-Marts_to_promote_Simpsons_movie),
  [ABC News](https://abcnews.com/Business/FunMoney/story?id=3404784&page=1)).
  Es un ejemplo perfecto de «objeto real en sitio real» para una lámina de
  Los Simpson si el dueño la usa en otra sala.

## Lo mejor para la lámina

1. La **figura amiibo de Rosalina** con su varita: pose 3D ya lista y con
   licencia de producto oficial, perfecta para el concepto B (la cúpula que
   se llena de estrellas) de #destacados.
2. El fondo de pantalla de **Bart Simpson estilo LoFi** (`o3r2kl`) da un aire
   cálido y nostálgico distinto al 3D de las otras salas: bueno para que
   Radio 24/7 no repita paleta con Cine.
3. La corrección de color de **Sulley y Mike** (verdes y azules reales, no
   los que estaban a ojo) evita el error más visible si se pintan juntos: sin
   esto, se podían confundir sus tonos.
4. El **crossover Bleach × Fortnite** (dic. 2025) es el dato más «caliente»:
   si la lámina de #noticias-anime se hace pronto, se puede usar como
   ejemplo de noticia real en el propio canal.
5. El aviso de **Wallhaven con carteles mezcla**: si otro investigador prueba
   Wallhaven para una serie nueva, que revise las etiquetas (`tags`) antes de
   dar por buena la primera imagen: varias eran de otra franquicia.

## No encontré

- **Colaboración de marca o *crossover* propio de Sing** (más allá de la
  atracción de Universal Studios): busqué «Sing Illumination colaboración
  marca merchandising evento real karaoke» (español) y no until una alianza
  comercial concreta, sólo merchandising genérico de terceros (Redbubble,
  eBay) que no cuenta como colaboración oficial. ⚠️ (no es obligatorio, es
  extra del punto 23).
- **Café temático o colaboración textil (UNIQLO) de Bleach**: busqué
  «Bleach colaboración UNIQLO OR Fortnite OR café temático 2024 2025»
  (español); sólo salió la de Fortnite (ya incluida). Puede existir un café
  en Japón (Animate Café ha hecho varios de Bleach en años anteriores) pero
  no lo confirmé con fecha y fuente, así que no lo incluyo como dato. ⚠️.
- **Morado de Doofenshmirtz**: no aparece en el retrato oficial ni en 3
   fotogramas de tráileres que miré; si el dueño recuerda una escena o un
   disfraz suyo morado, hace falta el capítulo para volver a buscarlo.
- **Cosplay de Sulley/Mike y de Bart Simpson**: no busqué cosplay para estas
  dos (sólo Rosalina, que era la prioridad por ser #destacados, el primer
  canal de la tabla). Extra, no obligatorio.

## Bitácora

- Wallhaven, API directa (sin gastar cupo de buscador): `q=Super Mario
  Galaxy`, `Rosalina Mario`, `Phineas and Ferb` (0), `Phineas Ferb` (0),
  `Phineas y Ferb` (0), `Phineas Flynn` (0), `Candace Flynn` (0), `Bleach
  anime`, `Bleach Ichigo Hitsugaya`, `Wreck It Ralph`, `Vanellope Ralph`,
  `Monsters Inc`, `Mike Wazowski`, `Monsters University`, `Sing movie`,
  `Buster Moon Sing` (0), `Sulley Monsters` (0), `The Simpsons`, `Bart
  Simpson`. Detalle de cada imagen con `/api/v1/w/<id>`.
- Alphacoders/Wallpaper Abyss (red directa, sin buscador): listado
  `alphacoders.com/sing-wallpapers`, páginas `big.php?i=` de 3 candidatos de
  Sing y 1 de Phineas y Ferb (encontradas antes con el buscador web, 2
  búsquedas: «Phineas and Ferb wallpaper 1920x1080 wallpaperaccess OR
  alphacoders», «Sing movie Buster Moon Meena wallpaper hd official
  Illumination»).
- Danbooru, API pública, `rating:g` (sin cupo de buscador): `rosalina_(mario)`,
  `kurosaki_ichigo`, `vanellope_von_schweetz`, `mike_wazowski`,
  `isabella_garcia-shapiro`, `buster_moon` (vacío), `sing_(movie)`,
  `meena_(sing)` (vacío), `phineas_flynn`, `ferb_fletcher`, `bart_simpson`,
  `homer_simpson`.
- Fandom API (`action=query&prop=pageimages` e `imageinfo`), sin buscador:
  bleach.fandom.com (Ichigo Kurosaki, Hisagi), wreckitralph.fandom.com
  (Vanellope), pixar.fandom.com (Sulley, Mike), phineasandferb.fandom.com
  (Doofenshmirtz). Imágenes bajadas y medidas con Pillow (`Image.getpixel`)
  en varios puntos de cada una, evitando sombras y luces fuertes.
- Buscador web (5 búsquedas de las ~50 del cupo, en español e inglés):
  «Phineas and Ferb wallpaper 1920x1080 wallpaperaccess OR alphacoders»,
  «Sing movie Buster Moon Meena wallpaper hd official Illumination»,
  «Bleach colaboración UNIQLO OR Fortnite OR café temático 2024 2025»,
  «Kwik-E-Mart 7-Eleven Simpsons colaboración tiendas reales 2007»,
  «Rosalina amiibo figura oficial Super Smash Bros cosplay», «Phineas and
  Ferb Marvel crossover special Mission Marvel Star Wars», «Wreck-It Ralph
  Breaks the Internet Disney princesses cameo Disney Infinity figure
  Vanellope», «Monsters Inc Kingdom Hearts 3 Monstropolis world
  colaboración Funko Pop», «"Sing" Illumination movie evento real karaoke
  colaboración marca merchandising», «cosplay Rosalina Super Mario Galaxy
  vestido turquesa reseña materiales», «free manga screentone brushes Clip
  Studio Paint license CC0 pack», «free pixel art texture pack CC0 itch.io
  retro arcade dithering».
- `datos-imagen.md` (recolector automático): confirmado que falló para esta
  obra porque aún no había series elegidas (buscó literalmente «proponer»);
  no repetí esas consultas, fui directo a la red con los nombres reales.

## Cumplimiento de mis puntos (1, 3, 15, 16, 19, 23)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | Ya hecho a fondo en la primera pasada (2.809 imágenes, 62 hojas); confirmado, no repetido |
| 3 · Fan art y 3D con licencia | ✅ | 3D ya estaba; fan art (que la biblia marcaba como no buscado) añadido para las 7 series, en Danbooru `rating:g` |
| 15 · Vestuario con hex medidos | ✅ | Estela ya estaba bien; corregí 5 valores «a ojo» (Hisagi, Vanellope, Sulley, Mike, Doofenshmirtz) midiendo con Pillow sobre arte oficial |
| 16 · Fondos de pantalla | ✅ | No existía ninguna sección; añadida para las 7 series (Wallhaven + Alphacoders), con tamaño real y autor |
| 19 · Texturas 2D | ✅ | Las 3D/PBR ya estaban; añadí el patrón 2D que faltaba (tramas de manga para Bleach, pixel art CC0 para Ralph) |
| 23 · Colaboraciones, figuras, cosplay | ✅ | No existía nada; añadida 1 colaboración/cruce real y 1 figura o cosplay por cada serie prioritaria |
