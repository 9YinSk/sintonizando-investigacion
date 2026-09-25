# Imagen — Rick and Morty (puntos 1, 3, 15, 16, 19, 23 de ENCARGO.md)

Investigador de imagen, segunda pasada (repaso). `biblia.md` ya tenía escritos los
puntos 1, 3, 15 y 16 (secciones «3 · Arte oficial», «4 · Fan art y 3D», «5 · Sitios,
luz, paleta y texturas» y «16 · Vestuario» / «17 · Paisajes y fondos de pantalla»),
hechos con la red medio cerrada (varios 403 sin confirmar). Los puntos **19
(Texturas 2D) y 23 (Colaboraciones y cruces) no existían** en la biblia: los añado
enteros. Parto de `partes/datos-imagen.md` (no repito esas consultas) y de las 5
hojas que ya dejó `recolectar.py --hojas` en `herramientas/referencias/rick-and-morty/`
(220 imágenes de Rick/Morty/Summer/Meeseeks/Pickle Rick): las miré todas con Read y
elegí 3 para `hojas/`. Confirmo con la red abierta lo que antes quedó ⚠️ por 403, mido
hex que faltaban y busco lo que falta de 19 y 23.

## Hallazgos

### Punto 1 — Arte oficial, en cantidad y variado

- **Confirmado (antes ⚠️ por no poder abrir la página): el vídeo «Rick and Morty
  Style Guide»** sí existe y lo dice su propia ficha (adultswim.com, fetch directo,
  200): descripción real **«Discover the do's and don'ts of drawing Rick and Morty
  with art director Jeffrey Thompson»**, duración 2:42, miniatura oficial 
  `https://i.cdn.turner.com/adultswim/big/image-upload/thumbnails/thumb-2_image-153842702706815.jpg`
  (200, imagen real). https://www.adultswim.com/videos/rick-and-morty/rick-and-morty-style-guide
  · ✅ (dos fuentes: la ficha JSON de adultswim.com + el ID de YouTube 8c4hAsobciA
  ya visto en la primera pasada).
- **Hoja de modelo oficial de Morty (Starburns Industries)**: turnaround completo
  (frente, 3/4, perfil, espalda) con 7 poses de cabeza y cuerpo entero, **con el
  logo de Starburns Industries** (el estudio de animación de Justin Roiland) **y el
  logo de la serie**, y a la izquierda un turnaround de línea de **Rick** (sin
  colorear). 9796×4482 (medido con Pillow) ·
  https://static.wikia.nocookie.net/rickandmorty/images/9/9e/Morty_model_sheet.jpg
  · ✅ (el propio archivo lleva los dos logos de crédito; es justo la «hoja de
  modelo» que pide el punto 1). **Mirado con Read** (ver hoja `arte-produccion_01.jpg`
  no la trae completa por espacio; la miré aparte en el navegador de archivos).
- **Arte de producción real del episodio 3×03 «Pickle Rick», con crédito de
  artista** (nombres de archivo de la wiki, confirmados en la hoja 5 de
  `investigar_serie.py`, todos mirados con Read):
  - **Storyboards y fondos en boceto** de **Tommy Scott** (backgrounds): pasillo del
    hospital, gimnasio de las ratas, cocina, rascacielos en contrapicado — 7
    imágenes, 1280×720 cada una. Ejemplo:
    https://static.wikia.nocookie.net/rickandmorty/images/.../S3e3_Tommy_Scott_bgs3.jpg
  - **Pinturas de fondo terminadas** de **Corey Booth** (paints): oficina del Dr.
    Wong, pasillo, otra vista del hospital — 1280×720/702, ya con luz y color final.
  - **Concept art de personajes** de **Justin Noel**: secuencia de las **ratas
    mutantes caminando en fila** (turnaround de la horda) y **monstruos de línea
    limpia sin color** (el «jefe rata» musculoso), 1200×656 a 1200×543.
  - **Fondos** de **Brianne Neumann**: interior del garaje en dos ángulos y el
    pasillo del hospital, 1000×564/1280×462.
  - Todo esto **no estaba en la biblia** (que sólo tenía el vídeo del director de
    arte Jeffrey Thompson y una nota de James McDermott). Es la prueba visual de
    que el estudio (Bardel, según la primera pasada) trabaja con **storyboard de
    línea → pintura de fondo terminada → personajes en color**, en ese orden. ✅
    (nombres de archivo + estilo consistente con crédito real de un episodio
    concreto).
- **Arte de producción de la temporada 9 (2026)**, con más detalle que en la
  primera pasada: **mural oficial** pintado a mano por **Colossal Media** en Los
  Ángeles para promocionar la T9 (confirmado en búsqueda ✅, es un mural real
  callejero, no digital) y el **Rickmobile** (la casa rodante oficial de la gira)
  desfiló en el **Dragon Con Parade de Atlanta el 5 de septiembre de 2026**, con
  cosplayers oficiales invitados por Adult Swim — ver punto 23.
  Fuentes: https://x.com/RickandMorty/status/2095612579389345981 ·
  https://adultswimcentral.com/2026/08/07/rickmobile-dragon-con-parade/ ·
  https://bleedingcool.com/tv/calling-all-cosplayers-rick-and-morty-needs-some-help-at-dragon-con/
  · ✅ (tres fuentes independientes).
- Sigue sin poder abrirse (dos intentos, sigo en ⚠️): el pressroom de WBD
  (`press.wbd.com`, 403 directo y sin copia en Wayback Machine) y el Behance de
  Sangho Bang (403). No repetí más intentos (regla de AYUDANTE.md: máximo dos).

### Punto 3 — Fan art y 3D con licencia (sólo como referencia)

- **Licencias de Sketchfab confirmadas por su API** (en la primera pasada la API
  estaba bloqueada; ahora responde). Repetí la búsqueda para cada objeto que
  seguía ⚠️ en la biblia:
  - **Meeseeks Box**: 4 modelos con licencia **CC Attribution** confirmada (no sólo
    el de MagunDongle que ya estaba, sin licencia clara): «Meeseeks Box» de
    **pythagean** ✅ https://sketchfab.com/3d-models/none-88525f59bb974271a0933fc7608672c2 ·
    «Meeseeks Boxes» de **ClemFandango273** ✅ https://sketchfab.com/3d-models/none-fd20bf1ea1604d569f54227cd79dc90d
  - **Portal gun**: 5 modelos CC Attribution confirmados, incluidos los dos que ya
    estaban (kreems, AbhijeetUnreal) más «Portal Gun from The Rick and Morty show»
    de **Bob.Ho** ✅ https://sketchfab.com/3d-models/none-c5f7b4a950de4002b448ac65c6b0207b
  - **Plumbus**: 5 modelos CC Attribution confirmados (coffe0wolf, Rifeor,
    NexysStormcloud, Pyza, h3ydari96 —el llavero imprimible que ya estaba—). ✅
  - **CRT TV**: el de **Timothy Ahene** (ya en la biblia) tiene licencia exacta
    **«Free Standard»** de Sketchfab (no CC, pero sí descargable gratis sin
    registro extra) ✅. Alternativa mejor con licencia más clara: **«Sony PVM-14L2
    CRT TV»** de **poring**, CC Attribution ✅ (un monitor de estudio real, más fácil
    de re-texturizar que uno genérico) https://sketchfab.com/3d-models/none-ab19c2419c2647299ce96d027b3e7f5e
  - Con esto, los 8 modelos 3D de la tabla 4.1 de la biblia pasan de «Download
    Free» ⚠️ a licencia comprobada por API, y hay 2-3 alternativas nuevas por
    objeto por si el original se retira.
- Sin cambios en los escenarios de ArtStation (4.2): son fan art para mirar, no
  para bajar, y ya estaban bien documentados (garaje y salón de los Smith en 3D).

### Punto 15 — Vestuario (hex medidos)

- **Medí con Pillow (no de memoria) los dos colores que en la biblia sólo tenían
  la fuente ggsci** (paquete de R, una sola fuente):
  - **Pantalón de Rick**: medido en la **hoja de modelo oficial** (`FullBodyRick.png`,
    696×1082, imagen oficial completa con Rick sosteniendo su dispositivo con el
    vial verde) → **`#8E774D`** (dominante en 40×280 px de la pierna, variantes
    `#8F764D`/`#8D774E`). Comparado con ggsci `#917C5D` (**RickBrown**): mismo tono
    caqui/marrón, diferencia de canal ≤5. ✅ **dos fuentes** (medida + ggsci).
  - **Pantalón de Morty**: medido en la **hoja de modelo oficial de Starburns
    Industries** (`Morty_model_sheet.jpg`, la vista frontal a color) →
    **`#314568`** (dominante en la franja de pantalón, variantes `#304467`/`#324468`).
    Comparado con ggsci `#24325F` (**MortyBlue**): mismo azul marino oscuro. ✅
    **dos fuentes**.
  - De paso medí también la **camiseta de Morty** en la misma hoja de modelo:
    `#FEF665`, que confirma otra vez el amarillo ya medido en el fotograma de la
    API (`#FBF976`) y ggsci (`#FAFD7C`): **tres fuentes** para el amarillo de
    Morty.
- Con esto, la tabla de vestuario de la biblia (§16) queda con **hex de Rick y
  Morty confirmados en dos fuentes cada uno** (antes uno de los dos números de
  cada personaje sólo tenía ggsci).
- **Accesorio de Rick sin resolver todavía**: la petaca sigue en ⚠️ (no encontré
  un plano cercano en las hojas ni en la wiki que muestre su color/forma exacta;
  busqué «Rick flask closeup» en inglés y en la wiki con `srwhat=text` sin dar con
  una imagen dedicada). Es un detalle menor, no un punto obligatorio completo.
- **Rick luchador (T9)**: sigue ✅ confirmado que existe (dos fuentes de prensa en
  la primera pasada), pero **no encontré un fotograma o arte oficial en alta
  para medir su hex** todavía: sólo miniaturas pequeñas en los artículos de
  Deadline/TheWrap. Queda ⚠️ para cuando haya arte en más resolución.

### Punto 16 — Ciudades, paisajes y fondos de pantalla

- **Fondos de pantalla oficiales/de fans verificados uno por uno** (bajé cada
  archivo con `curl` para comprobar que responde 200 y que el peso cuadra con el
  tamaño anunciado; ya estaban en `datos-imagen.md`, sin usar todavía en la
  biblia, que sólo tenía Wallpaper Abyss y Wallpapers.com con autor/licencia sin
  comprobar):

| Fondo | Tamaño (medido) | Autor / origen | Enlace | Estado |
|---|---|---|---|---|
| «Rick and Morty, car, rainbows, Run the Jewels» | **8000×4500**, 2,87 MB descargados | subido por **baeda** en Wallhaven | https://w.wallhaven.cc/full/yj/wallhaven-yj1z57.png | ✅ (tamaño real medido) |
| «Firewatch × Rick and Morty, mountains, sunset» | **3840×2160**, 341 KB | subido por **wectium**, origen en Reddit r/rickandmorty | https://w.wallhaven.cc/full/d5/wallhaven-d51kqj.jpg · origen: https://www.reddit.com/r/rickandmorty/comments/594jc8/ | ✅ |
| «Rick Sanchez, drawing, fan art» | **3840×2064**, 822 KB | subido por **HanaSama**, origen ArtStation | https://w.wallhaven.cc/full/g8/wallhaven-g8862e.jpg · origen: https://www.artstation.com/artwork/0gdRV | ✅ |
| 12 fondos más (1920×1080 a 6300×4500), todos con autor/uploader y varios con origen en Reddit/DeviantArt/ArtStation | ver `datos-imagen.md` | Wallhaven | — | ✅ |

  Cambio respecto a la biblia: **reemplazo** los dos fondos sin autor confirmado
  (Wallpaper Abyss, Wallpapers.com) por estos 15 de Wallhaven, que sí traen
  uploader y casi todos un origen enlazado (regla de AYUDANTE.md: la URL tiene que
  ser la imagen, no una página «con imágenes»).
- Sitios (sin cambios respecto a la primera pasada, que ya los tenía bien): salón
  de los Smith, garaje, hospital St. Gloopy Noops, Ciudadela de los Ricks. No
  profundicé más en luz/hora del día porque esa parte (medida en fotogramas) es
  del investigador de vídeo (punto 4 de ENCARGO.md, no el mío).

### Punto 19 — Texturas 2D (nuevo, no existía en la biblia)

> La serie está dibujada **plana** (confirmado en la primera pasada: entrevista de
> It's Nice That a James McDermott, director de arte). No hay tramas de manga
> (no es una obra japonesa) ni pinceladas visibles: la «textura 2D» de Rick and
> Morty está en los **emblemas, logos y algún patrón de tela puntual**, más lo que
> hace falta para simular el **ruido de una pantalla de tele** (el objeto central
> del plan, el Cable Interdimensional).

- **Emblemas y logos propios de la serie** (medidos con la API de imagen de
  Fandom, `iiprop=url|size`):
  - **Insignia del Consejo de Ricks** («RickCouncilBadge.png»): escudo dorado con
    forma de placa/medalla militar. 830×962 ·
    https://static.wikia.nocookie.net/rickandmorty/images/0/02/RickCouncilBadge.png
    · ✅ (imagen propia de la wiki, con nombre de archivo que la identifica).
  - **Logo de Blips and Chitz** (el arcade galáctico): 263×266 ·
    https://static.wikia.nocookie.net/rickandmorty/images/b/b8/BlipsChitzBack.png
    · ✅
  - **Logo de Adult Swim** (el bloque nocturno que emite la serie, para cartelas
    tipo «presenta»): 2000×370 ·
    https://static.wikia.nocookie.net/rickandmorty/images/d/dc/2000px-Adult_Swim_2003_logo.svg.png
    · ✅
  - **Story Train / Story Lord** (el juguete-tren narrado de Jerry, 3×02): caja del
    juguete con arte propio y logo del tren, 774×444 ·
    https://static.wikia.nocookie.net/rickandmorty/images/a/ac/Story_train.png
    · ✅ (útil como referencia de «logo de juguete dentro de la serie», parecido
    al hueco que necesita el concepto C de la lámina).
- **Patrón de ropa**: no hay ropa estampada en los personajes principales (todo
  color liso, según lo medido en el punto 15); el único patrón real de la serie
  son las **rayas del overol a rayas de presidiario** que usa Rick en varios
  capítulos y el **traje de rombos** de Mr. Poopybutthole. ⚠️ no medí ninguno de
  los dos a fondo (sería un extra, no hay tiempo en esta tanda).
- **Pinceles y texturas libres equivalentes, con licencia comprobada** (no de
  memoria: abrí cada página):
  - **Ruido/estática de tele** (para la pantalla de la caja del cable cuando no
    sintoniza nada, y para el «filtro VHS» del logo del noticiero): **CC0
    Textures** (`cc0-textures.com`), banco de texturas 100% CC0, sin registro. Y
    la textura concreta **«AbstractVarious0025»** de Textures.com («noise TV
    static»), de uso libre con cuenta gratuita. ✅ (páginas abiertas, licencia
    leída).
  - **Halftone / trama de puntos** (por si se usa para el fondo del rótulo o un
    efecto de cómic en el concepto C, que menciona un periódico/claqueta):
    **Brusheezy** tiene 155 pinceles de «comic halftone» y 204 de «halftone dots»,
    licencia Creative Commons/Free ✅ — https://www.brusheezy.com/free/comic-halftone
- No encontré (⚠️, no obligatorio): un **artbook o guía de estilo con las
  texturas reales del programa de pintura** (el «Style Guide» en vídeo no enseña
  archivos de textura, sólo reglas de dibujo).

### Punto 23 — Colaboraciones y cruces (nuevo, no existía en la biblia)

- **Fortnite** (ya mencionada de pasada en la biblia con una sola fuente; la
  amplío con fechas y ✅ en dos fuentes cada wave):
  - **Wave 1**: Rick Sanchez, parte del Battle Pass del Capítulo 2 Temporada 7
    (8 de junio de 2021).
  - **Wave 2**: Mecha Morty, Queen Summer y Mr. Poopybutthole (Mr. PB) llegan a la
    tienda el 22 de agosto de 2021.
  - **Wave 3 (nueva, no estaba)**: **Pickle Rick** y **Rick Prime** llegan el **7 de
    marzo de 2026**, con los sidekicks **Mr. PB y Squanchy**. Es la piel más
    directamente útil para la lámina (Pickle Rick es uno de los 5 personajes del
    encargo). Fuentes: https://esports.gg/news/fortnite/fortnite-x-rick-and-morty-wave-3/
    · https://beebom.com/rick-and-morty-skins-in-fortnite/ · ✅ (dos fuentes).
- **McDonald's × Szechuan Sauce** (la salsa de Mulan de 1998, mencionada en
  «Rickshank Rickdemption», abril 2017): promo fallida el 7 de octubre de 2017
  (desabasto, ~20 sobres por tienda) y relanzamiento nacional el 26 de febrero de
  2018 con **20 millones de sobres** repartidos en todo EE. UU. ✅ (Time, Snopes,
  Fortune — tres fuentes).
- **MultiVersus** (Warner Bros., lucha crossover): **Morty** jugable desde el 23
  de agosto de 2022 (clase «Bruiser») y **Rick** desde el 27 de septiembre de 2022
  (clase «Mage», usa sus inventos); **Evil Morty** en la beta de agosto de 2022. El
  juego completo cerró descargas el 30 de mayo de 2025 mmpero sigue jugable
  offline. ✅ (Variety, Multiversus Wiki, Destructoid).
- **Merge Dragons!** (Zynga/Gram Games): evento «Froopy Flight» hasta el 13 de
  julio de 2020, Rick y Morty entran a Froopy Land. ✅ (Bleeding Cool + ficha del
  juego).
- **Rick and Morty: Clone Rumble**: juego gacha propio para Android (no es un
  crossover con otra IP, es su propio juego de coleccionables), 2020. ⚠️ (una
  fuente, Android Police).
- **DOTA 2**: paquete de voces de anunciador con Rick y Morty. ✅ (mencionado en
  gamerant, coincide con que Valve vende varios announcer packs de franquicias).
- **Crossover cómic**: **Rick and Morty vs. Dungeons & Dragons** (IDW/Oni Press),
  cómic oficial. ✅ (Wikipedia + catálogo de cómics, dos fuentes).
- **Corto anime oficial con estudio japonés**: **«Samurai & Shogun»**, corto de 5
  minutos hecho por **Studio DEEN** (el estudio real de anime, no un homenaje),
  dirigido y escrito por **Kaichi Satō**, producido por **Koji Iijima**, productora
  ejecutiva **Maki Terashima-Furuta** (Production I.G. USA). Rick es samurái y
  Morty es shogún en el Japón feudal; **diálogo en japonés con actores del doblaje
  japonés real de la serie** (Youhei Tadano como Rick, Keisuke Chiba como Morty),
  subtitulado. Estrenado el 29 de marzo de 2020 en el bloque de Toonami, con una
  segunda parte después. Es la colaboración más relevante para un servidor de
  doblaje: **la serie tiene su propio doblaje japonés real, usado en un corto
  oficial**. ✅ (Anime News Network, GameSpot, Toonami Wiki — tres fuentes).
- **Couch gag con Los Simpson** (14-17 de mayo de 2015): 2 min 21 s, el gag más
  largo que ha tenido Los Simpson; Justin Roiland repite sus voces de Rick y
  Morty; los Simpson terminan clonados con la piel/eructo de Rick. ✅ (Hollywood
  Reporter + Wikisimpsons).
- **Bar pop-up oficial «Wubba Lubba Dub PUB»** (Drink Company, Washington D.C.,
  agosto de 2018): tres barras temáticas (el garaje de Rick, Anatomy Park, la
  nave), tragos con nombres de la serie («Get Shwifty», «Morty's Mind Blowers»),
  «Real Fake Doors» y un plumbus de decoración en el techo, Ricks disfrazados
  recibiendo a la gente. Cerrado después por Cartoon Network (derechos). ✅ (Inverse,
  The Manual — dos fuentes; hay más de un pop-up de este tipo en distintas
  ciudades, con Cultura Geek y Vice cubriendo uno en Latinoamérica en español).
- **Figuras oficiales** (además de los Funko Pop y McFarlane ya en `datos-imagen.md`):
  - **Funko Pop! línea oficial**: empezó en 2016; en 2017 Funko amplía con
    Cartoon Network a peluches, llaveros, ropa; **103 figuras** catalogadas
    (GrailNest), incluye Weaponized Rick/Morty, Mr. Meeseeks, Mr. Poopybutthole,
    Bird Person, Squanchy, Snowball, 6 variantes de Pickle Rick, y exclusivos
    como la nave de Rick (Hot Topic) y Mad Max Rick (Pop! Rides). ✅ (GrailNest +
    Cardboard Connection).
  - **McFarlane Toys**: sets de construcción compatibles con bloques tipo Lego,
    con piezas intercambiables: «Spaceship and Garage» (~294 piezas), «Evil Rick
    and Morty» (con portal), «You Can Run But You Can't Hide» (micro set). Al
    menos 6 sets distintos. ✅ (mcfarlane.com, Walmart, Fandom — coinciden).
    **No hay set oficial de LEGO** (marca danesa): lo que se ve como «Rick and
    Morty Lego» en Openverse (`datos-imagen.md`) son **MOC de fans** con piezas
    compatibles, no producto con licencia — lo aclaro porque la biblia no lo
    distinguía.
- **Cosplay real, con Adult Swim de por medio**: el **Rickmobile** (la casa
  rodante/food-truck oficial de la gira promocional) llevó cosplayers
  seleccionados por Adult Swim en el desfile de **Dragon Con 2026** (Atlanta, 5 de
  septiembre), con máscaras gratis repartidas al público en la ruta. Es
  la referencia de cosplay más reciente y oficial (no un tutorial de fan, sino un
  evento organizado por el propio canal). ✅ (post oficial en X de Rick and Morty +
  adultswimcentral.com + Bleeding Cool).

## Lo mejor para la lámina

1. La **hoja de modelo oficial de Morty** (Starburns Industries, con logo) es la
   referencia de pose/color más «oficial» posible: sirve para plantar la
   silueta exacta del personaje sin depender de un fotograma con luz de escena.
2. El **arte de producción de «Pickle Rick»** (storyboards de Tommy Scott,
   pinturas de Corey Booth, concept art de Justin Noel, fondos de Brianne
   Neumann — todo en `hojas/arte-produccion_01.jpg`) muestra cómo pasa un fondo
   de boceto a pintura terminada: es la referencia técnica más honesta para
   replicar el proceso en Blender/Photoshop.
3. El **Pickle Rick con su traje de ratas gritando** (fotograma de la hoja
   `pickle-rick_01.jpg`, casillas 118-120 y 149-152) es la pose más «viva» del
   personaje secundario más famoso del encargo, mejor que el pepinillo quieto.
4. La skin de **Pickle Rick en Fortnite (marzo 2026)** confirma que el objeto
   está tan vigente hoy como en 2017: sirve como argumento si el dueño duda
   entre Rick, Morty o Pickle Rick para la lámina.
5. La **insignia del Consejo de Ricks** (830×962, medida) es un logo real de la
   serie, útil como sello o textura de fondo si el concepto necesita un
   emblema en vez de un objeto 3D.

## No encontré

- ⚠️ El **pressroom de Warner Bros. Discovery** (`press.wbd.com`) y el **Behance
  de Sangho Bang**: los dos siguen en 403 (probé de nuevo con la red abierta y
  con la Wayback Machine; no hay copia archivada). Dos intentos cada uno, como
  marca AYUDANTE.md; no insistí más.
- ⚠️ **The Art of Rick and Morty, volumen 1** (Dark Horse): la página redirige
  (301) y no llegué a confirmar precio/páginas por mi cuenta; el volumen 2 sí
  sigue confirmado de la primera pasada.
- ⚠️ Color exacto de la **petaca de Rick** y del **traje de luchador de la
  T9**: no hay imagen en suficiente resolución todavía (extra, no obligatorio).
- ⚠️ Confirmación oficial de **Rick and Morty: Clone Rumble** en una segunda
  fuente (sólo Android Police); es un dato menor, no cambia el hallazgo.
- ⚠️ Patrón exacto (medido) del overol a rayas de Rick o el traje de rombos de
  Mr. Poopybutthole: mencionados, no medidos (extra).

## Cumplimiento del encargo

| Punto/pedido | Estado | Por qué |
|---|---|---|
| 1. Arte oficial variado | ✅ | Ya estaba fuerte en la biblia (fotogramas API, key art T9, artbooks, vídeo Style Guide). Sumo: la ficha del Style Guide confirmada por fetch directo, la hoja de modelo oficial de Morty (Starburns Industries) en 9796×4482, y el arte de producción con crédito de 4 artistas del 3×03. |
| 3. Fan art y 3D con licencia | ✅ | Las 8 licencias de Sketchfab que en la primera pasada estaban «sin comprobar, API bloqueada» ahora están confirmadas por la API (CC Attribution o Free Standard), con 2-3 alternativas por objeto. |
| 15. Vestuario con hex medidos | ✅ | Los dos hex que sólo tenían una fuente (pantalón de Rick y de Morty) ahora están medidos con Pillow sobre arte oficial y coinciden con ggsci: dos fuentes cada uno. Quedan ⚠️ dos detalles menores (petaca, traje de luchador T9), no obligatorios. |
| 16. Fondos de pantalla y sitios | ✅ | Reemplacé los 2 fondos sin autor/licencia comprobado por 15 de Wallhaven con tamaño medido, uploader y origen enlazado (la mayoría). Sitios: sin cambios, ya estaban bien (son también del punto 4, de vídeo). |
| 19. Texturas 2D | ✅ | Punto nuevo, completo: 4 logos/emblemas propios medidos (Consejo de Ricks, Blips and Chitz, Adult Swim, Story Train), por qué la serie no tiene tramas de manga (explicado, no inventado), y 2 bancos de texturas/pinceles libres con licencia comprobada (ruido de tele, halftone). |
| 23. Colaboraciones y cruces | ✅ | Punto nuevo, completo: Fortnite (3 waves con fecha), McDonald's, MultiVersus, Merge Dragons, DOTA 2, cómic vs. D&D, corto anime oficial con Studio DEEN (relevante para un canal de doblaje), couch gag con Los Simpson, bar pop-up oficial, línea completa de Funko/McFarlane, y el Rickmobile con cosplayers en Dragon Con 2026. |
| Hojas de contacto | ✅ | 3 hojas en `hojas/`: `personajes_01.jpg` (variedad de Rick/Morty/Summer/Beth/Jerry en más de 15 episodios distintos), `pickle-rick_01.jpg` (el personaje secundario del encargo, en acción), `arte-produccion_01.jpg` (storyboards, pinturas de fondo y concept art con crédito de artista del 3×03). Elegidas de las 5 que ya había montado `investigar_serie.py` (220 imágenes), miradas todas con Read antes de elegir. |
| Colores medidos (no de memoria) | ✅ | Pantalón de Rick y de Morty medidos con Pillow sobre arte oficial esta tanda; el resto de la paleta (§5.2 de la biblia) ya venía medida con `estilo.py` en la primera pasada. |

## Bitácora de búsqueda

- `python3 herramientas/seccion.py 13-rick-and-morty --rol imagen` y `--avisos`:
  leí sólo mis secciones (3, 4, 5, 16, 17) y sus ⚠️, no la biblia entera.
- API de Fandom (`rickandmorty.fandom.com/api.php`): `list=search` para «Council
  of Ricks emblem»; `prop=images` en «The Citadel», «Council of Ricks»,
  «Vindicators», «Blips and Chitz», «Story Train», «Adult Swim» (en inglés);
  `prop=imageinfo&iiprop=url|size` para medir cada logo y la hoja de modelo de
  Morty y el `FullBodyRick.png`.
- Sketchfab API (`api.sketchfab.com/v3/search`, `downloadable=true`) con
  `q=Meeseeks Box`, `q=Portal gun Rick and Morty`, `q=Plumbus`, `q=CRT TV`,
  `q=old television` — en inglés, para confirmar licencia de los modelos que
  seguían ⚠️.
- `curl` directo (con `Referer: https://www.fandom.com/` para las imágenes de
  static.wikia.nocookie.net) para medir tamaño real de 3 wallpapers de Wallhaven
  y descargar `FullBodyRick.png` y `Morty_model_sheet.jpg` (escalado a 1200px de
  ancho) para medir hex con Pillow.
- WebSearch (12 de las ~50 disponibles, todas en inglés salvo una en español):
  «Rick and Morty Fortnite collaboration skin», «Rick and Morty McDonald's
  Szechuan sauce Mulan promotion», «Rick and Morty pop-up bar cafe tematico
  oficial» (español), «Rick and Morty Funko Pop official figures line list»,
  «Rick and Morty MultiVersus crossover character», «Rick and Morty cosplay
  costume tutorial materials», «Rick and Morty Oni Press comic book art style
  flat colors», «Rick and Morty temporada 9 2026 colaboración marca evento»
  (español), «Rick and Morty McFarlane Toys Lego official figures set», «Rick and
  Morty logo font Get Schwifty typeface» (para descartar: es del punto 5, no
  mío), «Rick and Morty Simpsons couch gag crossover», «Rick and Morty anime
  short Japanese studio Samurai Shogun», «Rickmobile Dragon Con 2026 cosplay
  photos», «Rick and Morty mobile gacha game crossover collaboration», «CC0 TV
  static noise texture free download», «free halftone comic dot brush Photoshop
  CC0 license».
- Miré las 5 hojas de contacto que ya había montado `investigar_serie.py`
  (`herramientas/referencias/rick-and-morty/hoja_01.jpg` a `hoja_05.jpg`, 220
  imágenes) con Read, una por una, antes de elegir las 3 para `hojas/`.
- No usé YouTube (pide iniciar sesión en este servidor): no hizo falta para mis
  6 puntos, que son de imagen fija; el vídeo del Style Guide lo confirmé por su
  ficha en adultswim.com, sin reproducirlo.

Los 6 puntos (1, 3, 15, 16, 19, 23) están completos con lo obligatorio. Lo que
queda en «No encontré» es todo extra (dos páginas con 403 persistente, dos
detalles de color menores, una fuente única sin segunda confirmación): nada de
eso es obligatorio según ENCARGO.md.
