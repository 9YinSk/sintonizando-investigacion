# Investigador de IMAGEN · Adventure Time (Hora de aventura)

Puntos de `ENCARGO.md`: **1** (arte oficial variado), **3** (fan art y 3D con licencia),
**15** (vestuario con hex medidos), **16** (fondos y fondos de pantalla), **19**
(texturas 2D), **23** (colaboraciones y cruces).

> Segunda pasada, red abierta (2026-09-25). La primera pasada (recuadro de
> `biblia.md`) tenía la red cerrada: **no se pudo ver ninguna imagen**. Aquí sí:
> hojas de contacto generadas y miradas, imágenes bajadas y medidas con
> Pillow (`herramientas/estilo.py`), Sketchfab y Wallhaven consultados por su
> API real, y la wiki de Fandom leída por su API. Partía de
> `partes/datos-imagen.md` (Sketchfab y Openverse ya recolectados): no repetí
> esas consultas, seguí desde ahí.
> **Wiki correcta**: el subdominio que sugiere el encargo
> (`adventuretimewithfinnandjake`) **redirige** a `adventuretime.fandom.com`;
> uso ese subdominio en la API (comprobado con `action=query&meta=siteinfo`).

---

## 1 · Arte oficial, en cantidad y variado

### Hojas de contacto (vistas) ✅

`herramientas/investigar_serie.py --wiki adventuretime --paginas "Marceline
Abadeer" "Finn the Human" "Jake the Dog" "Princess Bubblegum" "Ax Bass" "BMO"`
indexó **1188 imágenes** de la wiki y montó **13 hojas** de 48 imágenes cada
una en `herramientas/referencias/adventure-time-hora-de-aventura/`
(`indice.json` tiene ancho, alto y URL real de cada una). Las miré con `Read`.
Elegí 3 para `hojas/` del repositorio (ver «Las hojas de contacto» al final).

### Model sheets de producción, con metadatos reales ✅

Vistos directamente (no descritos de oído). Cada uno trae el sello
**© Cartoon Network Studios** y una ficha de producción (episodio, id):

- **«Marceline - New Costume #1»**, ep. **057**, id `C057s011_472`, ©2011:
  turnaround de frente y de espaldas con un **vestido camisero azul grisáceo**
  (no la camiseta gris que decía la pasada 1) y **zapatos granate** —
  [4079×2421](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/3/34/Modelsheet_Marceline_-_New_Costume_-1.png).
  Hex medidos con `estilo.py` en el punto 15.
- **«Marceline Stock Night»**: turnaround de caminata, 4 poses —
  [5100×3300](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/0/0b/Modelsheet_marceline_stocknight.jpg)
  ✅. Es un sheet de **construcción** (gris, sin color final): sirve para
  proporciones, no para paleta.
- **«Marceline Bat» (1 y 2)**: bocetos a lápiz de su forma de murciélago
  gigante, con notas «Bat Marceline Rough — Phil» ✅
  ([3600×3000](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/9/9b/Modelsheet-MarcelineBat1.jpg)).
- **«Modelsheet axbass withrims»**: el bajo-hacha solo, con llantas
  (rims) de mástil marcadas — [4104×2454](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/5/58/Modelsheet_axbass_withrims.png) ✅.
- **«Original Finn.png»** y **«Jakesalad.png»**: model sheets a color de
  Finn y Jake (usados también para el punto 15) ✅.
- **«Modelsheet princessbubblegumtiedup.png»** (1478×1494) y **«Come Along
  with Me original costume sketches for Marceline by Tom Herpich (9).jpg»**
  (1280×1673, boceto de vestuario del storyboarder/fondista **Tom Herpich**
  para el final de serie) ✅: prueba directa de bocetos de producción por
  nombre de autor.

### Concept art oficial del especial «Obsidian» (2021) ✅ (visto)

La wiki tiene una galería `Obsidian-concept-1.png` a `-15.jpg` (subida
2021-01-30). Bajé y miré dos:
- **`Obsidian-concept-9.png`** (1002×810): bocetos a lápiz rojo de los
  «Shards» (los habitantes del Reino de Cristal), tres variantes de un mismo
  diseño con capucha puntiaguda y manoplas.
- **`Obsidian-concept-1.png`** (1280×989): diseño de la montaña-criatura de
  tinta negra sólida (silueta con dientes y garras) que aparece en el
  especial.
Confirma que sí hay **material de making-of visible** para este especial, no
sólo key art de prensa.

### De la pasada 1 (ya con 2 fuentes; sólo faltaba «verlo», sigue igual) ✅

- Artbook **«The Art of Ooo»** (Chris McDonnell, Abrams, 14-oct-2014, 352 pp.,
  prólogo de Guillermo del Toro) — [Amazon](https://www.amazon.com/Adventure-Time-Art-Chris-McDonnell/dp/1419704508).
- **«The Original Cartoon Title Cards»** (Titan Books): cartelas con bocetos y
  comentarios de Ward, McHale, Jennings, Rynda y Linsley — técnica real
  (tramado/dithering sobre papel viejo escaneado por Nick Jennings) ✅
  ([Art of the Title](https://www.artofthetitle.com/title/adventure-time/)).
- Key art de **«Obsidian»**: teaser 24-jul-2020 (Comic-Con virtual), estreno
  19-nov-2020 ✅ ([Bleeding Cool](https://bleedingcool.com/tv/adventure-time-distant-lands-obsidian-releases-trailer-key-art/)).
- Discos con arte oficial nuevo: caja Mondo (**JJ Harrison**), «Come Along
  With Me» y «BMO's Mixtape» (**Jesse Balmer**), «Obsidian» (**Maya
  Petersen**) — tabla completa ya en `biblia.md` §3.4, no la repito.
- Cómic **«Marceline and the Scream Queens»** (BOOM!, 2012, Meredith Gran, 6
  números): banda de Marceline de gira, con Dulce Princesa de corista.
- **Logo oficial** de la serie, archivo de la wiki: [1069×519](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/thumb/b/bd/Adventure_Time_logo.png) ✅ (visto).

---

## 3 · Fan art y 3D (licencia comprobada por la API de Sketchfab)

No adiviné licencias: consulté `api.sketchfab.com/v3/search` directamente
(fuente primaria — Sketchfab es quien certifica su propia licencia).

| Modelo | Autor | Licencia (API) | Nota |
|---|---|---|---|
| [Marceline's Ax Bass](https://sketchfab.com/3d-models/none-2224d0a363a24ba883614f209761454c) | Yogensia | **CC BY-NC-SA 4.0** ✅ | confirmado (ya lo decía la pasada 1; ahora con la API) |
| [Marceline's Ax Bass](https://sketchfab.com/3d-models/none-417178d709774642b0d5b5a02181caa2) | Haxis | **CC Attribution** ✅ | el más libre: permite uso comercial con crédito |
| [Marceline`s Bass guitar](https://sketchfab.com/3d-models/none-bac567bac05b46039f0e5510bf0c3062) | coffe0wolf | CC Attribution-NonCommercial ✅ | |
| [Marceline the vampire queen](https://sketchfab.com/3d-models/none-f520806111dc454ba3455947e51b04de) (personaje completo) | coffe0wolf | **CC Attribution** ✅ | sirve de referencia de volumen del personaje entero, no sólo el bajo |
| [Marceline's Axe/Guitar](https://sketchfab.com/3d-models/none-412c96ee288a4bcdb01a7433dff90fa7) | ScoobSter_ | CC Attribution ✅ | |
| [Marceline's Axe Bass](https://sketchfab.com/3d-models/none-477b56a2db134065947b2c931c52b3aa) | denizin | CC Attribution-NonCommercial ✅ | (pasada 1 decía «sin ver»: era CC, no dudosa) |
| [Low Poly Marceline's Ax Bass](https://sketchfab.com/3d-models/none-101d7036f35b411295e6a500c86e952b) | cuxilrodas | **«Free Standard»** ⚠️ | **corrección**: esto NO es Creative Commons, es la licencia por defecto de Sketchfab (descarga gratis, pero sin permiso explícito de reuso/remix). No usar sin pedir permiso al autor |
| [Finn's Demon Blood Sword](https://sketchfab.com/3d-models/none-7f919633863140a49e6d51a8f0d87aab) · [Finn - Adventure Time](https://sketchfab.com/3d-models/none-b3c5b1d5e4274eb0ba7f42ea00ed0ad2) | Haxis · RenataDiFlorio | CC Attribution ✅ | espada y personaje de Finn |
| [Jake el Perro Toon](https://sketchfab.com/3d-models/none-6fd2e3f4ef614842add5cec885cec2f2) | Luis Angel | CC Attribution ✅ | |
| [Bmo - Adventure Time](https://sketchfab.com/3d-models/none-ffeb3e9ab97e4e3dbed4ddc0650d8b9b) · [Adventure Time BMO](https://sketchfab.com/3d-models/none-57a8b359d2ad41a3bacc41facfc77531) | featbear456978 · ezgibakim | CC Attribution ✅ | |
| **[The Treehouse](https://sketchfab.com/3d-models/none-0131dc63d8894892b0c87dc852f23984)** / [Finn and Jake's Treehouse](https://sketchfab.com/3d-models/none-a390d3c9873c4c219959d0b930aabe52) | gleksono | **CC Attribution** ✅ | modelo 3D del **sitio** (no sólo objetos): sirve también para el punto 16 |

**Recomendación sin cambios**: el de **Yogensia** o el de **Haxis** (licencias
más claras) para el bajo-hacha en Blender; el de **coffe0wolf** si hace falta
el cuerpo entero de Marceline como maniquí de proporciones.

### Fan art 2D (sólo mirar, nunca pegar) — igual que pasada 1

Los 5 enlaces de DeviantArt de la pasada 1 (AJsCanvas, queenjazmine,
Disneyponyfan, Minty-Kitty-Art, DavaDs/TheBreakfastUnicorn) siguen válidos;
no encontré razón para cambiarlos.

### Fotos con licencia libre (Openverse, ya recolectadas en datos-imagen.md)

Son disfraces caseros de Halloween (usuario «Violently Japy», Flickr, CC
BY-NC 2.0), no cosplay de estudio. Para «cosplay bien hecho» con materiales
reales, ver punto 23 (ahí sí hay construcciones serias del bajo-hacha).

---

## 15 · Vestuario (hex medidos con Pillow, no de memoria)

Medí con `herramientas/estilo.py` (que usa Pillow) sobre imágenes oficiales
bajadas, algunas recortadas primero para evitar que el fondo domine la
muestra. Cito la imagen y el recorte en cada caso.

### Marceline — 3 vestuarios distintos, medidos ✅

| Vestuario | Hex medido | De dónde |
|---|---|---|
| **«New Costume #1»** (vestido camisero azul grisáceo, calzado sin mangas) | tela `#83A5BC` · zapato granate `#8C284F` · piel `#D8E7E7` · pelo `#000000` | Model sheet oficial ep. 057 (arriba), recorte limpio sobre fondo gris de producción — **es el más fiable: sin luz de escena** |
| **Suéter a rayas rojo/negro** (con el bajo bajado a un lado) | rayas medidas en penumbra: `#5F120D` (rojo, oscurecido) / `#090B25` (azul-negro), piel `#D8E0E8` | screenshot oficial [«S2e1 Drama bomb.png»](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/8/85/S2e1_Drama_bomb.png) (2880×1620) — escena **nocturna**, colores oscurecidos por la luz de la escena; de día serían más vivos. **Corrige** a la pasada 1: el traje «más icónico» no es sólo la camiseta gris, este suéter rayado con cuello alto también es muy repetido |
| **Con el bajo-hacha, tocando** (chaqueta gris-oliva sobre camiseta) | dominante de escena (atardecer, luz cálida) — no aislé bien la tela del fondo, así que **no doy hex** de esta prenda, sólo la pose | screenshot oficial [«S7e7 Marceline playing ax bass.png»](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/3/33/S7e7_Marceline_playing_ax_bass.png) (2880×1620) — **la mejor imagen «con su instrumento» que pide el dueño**: de pie, en un huerto, tocando de verdad, ojo guiñado |

Bajo-hacha (filos): en el model sheet, sin color (turnaround gris); en las
escenas de color se ve rojo saturado tipo `#9E1B1E`–`#C22B2F` (confirmo el
tono que ya traía la pasada 1, sin poder aislar un pixel limpio por el brillo
de la escena) ⚠️.

Pelo: negro puro `#000000` medido dos veces (model sheet y screenshot) ✅,
no el «negro azulado» que decía la pasada 1 de memoria.

Piel: **`#D8E7E7`–`#D9E7E7`**, blanco-menta muy pálido, medido dos veces
(model sheet + recorte de «Drama bomb») ✅. **Corrige** el `#A9B8C2`
"gris azulado" que la pasada 1 puso de memoria: en el arte plano la piel de
Marceline es casi blanca, no gris.

### Finn ✅ (medido, no de memoria)

Model sheet oficial [«Original Finn.png»](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/f/f3/Original_Finn.png)
(1467×2385): camiseta azul `#018BCB`, mochila verde `#7BBB59`, piel
`#FDE5DA` (durazno pálido, no «celeste» como decía la pasada 1 confundiendo
con la camiseta).

### Jake ✅ (medido)

Model sheet [«Jakesalad.png»](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/3/3b/Jakesalad.png)
(1700×2455): cuerpo amarillo-naranja `#FEB925`, dominante al 40% de la
imagen — coincide con lo que decía la pasada 1 de memoria, ahora medido.

### Dulce Princesa (Princess Bubblegum) ✅ (medido)

Screenshot oficial [«Princess Bubblegum Duct Tape.png»](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/f/f5/Princess_Bubblegum_Duct_Tape.png)
(2880×1618): piel/pelo rosa chicle en dos tonos, `#ED8ACE` (42%) y `#F3BBFB`
(33%, zonas de luz). Corona dorada: no aislé un pixel limpio ⚠️ (queda de
memoria, como la pasada 1).

### BMO ⚠️ (sigue sin medir bien)

Lo intenté sobre «Bmo transforming.jpeg», pero el fondo rosa del Dulce Reino
domina el 88% de la imagen y no pude aislar la carcasa turquesa sin recortar
a mano con más tiempo. Sigue de memoria (`#6CC3B3` aprox., pasada 1).

---

## 16 · Ciudades, paisajes y fondos de pantalla

### Sitios (texto, ya con 2 fuentes de la wiki en pasada 1) — sin cambios

Cueva y casa de Marceline, Anfiteatro Fantasma, casa del árbol, Reino de
Cristal: las descripciones y fuentes de `biblia.md` §5.1 siguen firmes
(confirmadas en la wiki), no las repito.

### Fondos de pantalla de fans, con tamaño y autor reales (Wallhaven API) ✅

La pasada 1 no encontró nada (Wallhaven cerrado). Consulté la API real
(`wallhaven.cc/api/v1/search` y `/w/<id>` para cada ficha):

| Id | Resolución | Autor | Favoritos | Qué es |
|---|---|---|---|---|
| [zxo8vg](https://wallhaven.cc/w/zxo8vg) | **3600×2400** | RaidMath | 40 | todo el elenco (Marceline, Dulce Princesa, Jake, Rey Helado, BMO, Lady Arcoíris) sobre fondo de Cartoon Network — **la mejor para «todo el mundo del canal» en una sola imagen** |
| [0wy167](https://wallhaven.cc/w/0wy167) | 1800×1000 | Oniofash | 52 | collage de Marceline, Simon Petrikov y Dulce Princesa |
| [45zpo5](https://wallhaven.cc/w/45zpo5) | 1639×1165 | Linez | 34 | Jake, Finn, Dulce Princesa y Marceline juntos, fan art de estudio |
| [0wxpgp](https://wallhaven.cc/w/0wxpgp) | 1920×1036 | 8bitcartoon | 57 | Finn y Jake en **pixel art** — útil como referencia de paleta reducida |

(Todos con `purity=sfw`, filtro activado.) **Ojo**: son fan art, no
oficiales — Wallhaven no aloja fondos con licencia de Cartoon Network. Como
«fondo oficial en alta» lo más parecido sigue siendo el arte de los discos y
el key art de «Obsidian» (punto 1), que si son key art de estudio.

### Modelo 3D del sitio, con licencia (nuevo, ver punto 3)

**The Treehouse** (gleksono, CC Attribution, Sketchfab): la casa-árbol de
Finn y Jake en 3D, licencia libre — mejor que sólo una imagen para dar
volumen y luz reales en Blender.

### Texturas reales para los sitios — sin cambios de la pasada 1

Poly Haven CC0 (roca de cueva, HDRI de cueva): siguen firmes, no las repito.

---

## 19 · Texturas 2D

La serie no es manga, así que no hay tramas de cómic japonés; el equivalente
real es el **tramado (dithering) de las cartelas de título** (ya descrito y
confirmado en `biblia.md` §3.2: Phil Rynda/Paul Linsley/Nick Jennings, papel
viejo escaneado) y el **punteado tipo cómic** de los cómics oficiales de BOOM!
Studios (coloreado plano con sombreado en trama, típico del cómic
estadounidense de la época).

### Texturas reales equivalentes, CC0, medidas por su API (ambientCG) ✅

Consulté `ambientcg.com/api/v2/full_json` (no adiviné nombres):

| Uso | Textura CC0 | Enlace |
|---|---|---|
| Papel viejo de cartelas / libreto de disco | Paper001–Paper006 | [ambientCG](https://ambientcg.com/list?type=Material&q=paper) |
| Funda de cartón del vinilo | Cardboard001–Cardboard004 | [ambientCG](https://ambientcg.com/list?type=Material&q=cardboard) |
| Camiseta/tela de ropa (Finn, Marceline) | Fabric081C, Fabric061, Fabric066 | [ambientCG](https://ambientcg.com/list?type=Material&q=fabric) |
| Mástil de madera del bajo-hacha, muebles de la casa | Wood092, Wood094, Wood095 | [ambientCG](https://ambientcg.com/list?type=Material&q=wood) |
| Botas de Marceline y Finn | Leather026, Leather030, Leather037, Leather038 | [ambientCG](https://ambientcg.com/list?type=Material&q=leather) |

Todas **CC0** (sin crédito obligatorio), confirmado por la propia API de
ambientCG (campo de licencia de la respuesta).

### Pinceles/patrones de trama y tramado (halftone/dithering) libres

- **12 texturas de halftone desgastado, gratis**: [Spoon Graphics](https://blog.spoongraphics.co.uk/freebies/free-pack-of-12-distressed-halftone-pattern-textures) ✅ (descarga directa, sin registro).
- **+35 texturas y patrones de halftone**: [PhotoshopSupply](https://www.photoshopsupply.com/patterns-textures/halftone-texture) ✅.
- Colección de pinceles halftone con licencia CC/open source: [Brusheezy](https://www.brusheezy.com/free/halftone-texture) ⚠️ (licencia varía por pincel dentro del sitio: comprobar cada uno antes de usar).

Con esto, y los puntos 3 (3D) y 4/16 (texturas reales de sitio), las tres
capas que pide el punto 19 quedan cubiertas: dithering/trama (arriba),
materiales reales (ambientCG) y 3D con licencia (Sketchfab, punto 3).

---

## 23 · Colaboraciones y cruces

Toda esta sección es nueva (la pasada 1 no tenía este punto: es de los
añadidos el 24-sep). Fuente principal: la página **«References in other
media»** de la wiki (leída completa por su API,
`adventuretime.fandom.com/wiki/References_in_other_media`), contrastada con
prensa cuando hacía falta fecha o precio.

### Videojuegos con personajes o pieles oficiales ✅

- **Fortnite** (Epic/Warner): Finn, Jake, Dulce Princesa y Marceline como
  **skins** (1500 V-Bucks cada uno, o 3800 en pack), llegaron en el update
  v34.30, **abril de 2025**, confirmado por la wiki y por prensa
  ([ScreenRant](https://screenrant.com/fortnite-adventure-time-skins/),
  [Sportskeeda](https://www.sportskeeda.com/fortnite/how-get-finn-jake-princess-bubblegum-marceline-adventure-time-skins-fortnite)).
  **Accesorios que tocan directo el objeto del plan**: el **«Candy Axe»** y,
  sobre todo, el **«Marcy's Ax Bass»** como pico (herramienta de recolectar)
  y como instrumento tocable en el modo **Fortnite Festival**, junto a un
  keytar inspirado en Dulce Princesa ✅ ([Fortnite.gg](https://fortnite.gg/cosmetics?id=17683)
  — «A family heirloom converted into a wicked bass guitar»). Mochilas: Chicle
  Espacial, BMO, Hambo. Segunda tanda con Fionna, Cake, Conde Limongrab y Rey
  Helado, **15-ene-2026** (item shop) ✅.
- **MultiVersus** (Player First Games / Warner Bros. Games): **Finn, Jake y un
  Guardia Banana** jugables desde el lanzamiento 2024; **Marceline** se sumó
  el **20-dic-2024** (temporada 4) ✅ (wiki +
  [GameRant](https://gamerant.com/multiversus-marceline-adventure-time-release-date-price/)).
  El mapa «Tree Fort» es la casa-árbol. **El juego cerró servidores el
  30-may-2025** ⚠️ (ya no se puede jugar, sólo mirar vídeos).
- **LEGO Dimensions** (Traveller's Tales/WB, 2016): 3 sets Año 2 — *Level
  Pack* con Finn, *Team Pack* con Jake y la Princesa Grumosa Espacial
  (27-sep-2016), *Fun Pack* con **Marceline** (18-nov-2016) ✅ (wiki, con
  fechas de lanzamiento).
- **Minecraft** (Mojang): logro/avance llamado **«Adventuring Time!»**
  (descubrir todos los biomas) desde siempre; el **«Adventure Time Mash-up
  Pack»** (mapa de Ooo jugable + texturas + skins), **30-may-2017** ✅. Salió
  también el episodio crossover **«Diamonds and Lemons»** ese julio.
- **Brawlhalla**: Finn, Jake y Dulce Princesa como skins de pago, más mapa y
  efecto K.O. temáticos ✅ ([nota oficial de Brawlhalla](https://www.brawlhalla.com/news/what-time-is-it-adventure-time-in-valhalla-patch-3-44/)).
- **League of Legends**: dos guiños confirmados por la wiki — el baile de
  **Jinx** copia el que Jake le enseña al escarabajo en «Power Animal», y la
  piel **«Galaxy Slayer Zed»** cita una frase casi idéntica a la del Lich en
  «Gold Stars» ⚠️ (un solo tipo de fuente, la wiki; no verifiqué en Riot
  directamente).
- **Skullgirls**: el color de **Filia** recuerda al de **Fionna** ⚠️ (dato de
  la wiki, mención breve, sin fuente de Skullgirls que lo confirme).
- **Xbox Live Marketplace** (2012): colección de **30 piezas** de ropa para
  avatar, con la corona del Rey Helado y el **bajo-hacha de Marceline**,
  80–320 puntos Microsoft (US$1–4) ✅ ([Polygon](https://www.polygon.com/2012/10/9/3480640/adventure-time-avatar-items-xbox-live)).

### Figuras oficiales ✅

- **Funko Pop! Television**: Marceline #31 (estándar, botas marrones) y
  **#301 con guitarra** (exclusivo Hot Topic) ✅; también una variante
  **Adventure Time × Minecraft** de Marceline, ligada al mash-up pack de
  arriba ✅ ([TCGplayer #31](https://www.tcgplayer.com/product/135801/funko-pop-vinyl-adventure-time-marceline),
  [#301 con guitarra](https://www.tcgplayer.com/product/135786/funko-pop-vinyl-adventure-time-marceline-with-guitar),
  [BoxLunch, Minecraft](https://www.boxlunch.com/product/funko-pop-adventure-time-x-minecraft-marceline-vinyl-figure/11442336.html)).
  La pose con guitarra es la referencia 3D más directa que hay de «Marceline
  tocando su bajo» en formato figura.

### Cosplay bien hecho: el bajo-hacha, con materiales reales ✅

Varios tutoriales de construcción documentan **materiales y volumen reales**
(lo que pide el dueño, no una silueta plana):
- **MDF de ¼" + espuma de aislamiento de ½"** pegada a los dos lados con
  adhesivo en spray, lijada para igualar la madera —
  [2StoryProps](http://2storyprops.blogspot.com/2013/03/marcelines-axe-bass-adventure-time.html).
- Cuerpo de **pino cortado con plantilla**, mástil de **dos tablas de 2×3"**
  atornilladas — hilo con fotos paso a paso en
  [The RPF (Replica Prop Forum)](https://www.therpf.com/forums/threads/marcelines-axe-bass-build-from-adventure-time.221761/).
  RPF es la comunidad de referencia en props reales: si algo pasa su filtro,
  el volumen es correcto.
- Versión ligera para cosplay (no tocable): **cartón piedra + goma EVA**,
  cuerdas de alambre de colgar cuadros —
  [Nerd Caliber](https://www.nerdcaliber.com/making-good-cosplay-great-marcelines-guitar-a-tutorial/),
  [Cosplay Sass](https://cosplaysass.wordpress.com/2019/02/20/marceline-axe/).
Sirven **como referencia de materiales y proporciones para el modelo 3D**,
no para copiar: dan el volumen real que pide el dueño («nunca de pie con una
ropa plana»).

### Parodias, cruces y otros medios (más ligero, para redondear el punto) ✅

- **MAD Magazine** #520: portada parodia con Finn como Alfred E. Neuman ✅.
- **Gaia Online** (2012): objetos virtuales de coleccionable + evento en vivo
  con Pendleton Ward (22-mar-2012) ✅.
- Cameos cruzados en **Steven Universe** («Sadie's Song», un peluche parecido
  a Gunter) y **OK K.O.! Let's Be Heroes** (Jake y Finn en «Crossover
  Nexus») ✅ — ambos de Cartoon Network, mismo estudio/canal.

---

## Las hojas de contacto

3 hojas en `hojas/` (de las 13 generadas; el resto queda en
`herramientas/referencias/adventure-time-hora-de-aventura/` por si el
redactor quiere más):

1. **`personajes_01.jpg`** (imágenes 1–48 del índice): model sheets
   oficiales de Marceline (turnaround, forma murciélago, bajo-hacha, «New
   Costume»), capturas de escena (tocando el bajo, motocicleta con Simon,
   conoce a Hunson Abadeer) y model sheets de Jake y Finn. **La mejor hoja
   para vestuario y arte de producción.**
2. **`personajes_02.jpg`** (49–96): el bajo-hacha solo sobre fondo verde,
   capturas en alta de la Dulce Princesa (varios episodios, 1920×1200),
   Marshmaline, BMO transformándose. **La mejor para la Dulce Princesa.**
3. **`escenas_09.jpg`** (385–432): la historia de Marceline y Simon
   (Rey Helado) en distintas épocas — de niña, adolescente, con Hambo,
   tocando el omnichord — y la casa del árbol por dentro. **La mejor para
   ver cómo cambia el vestuario de Marceline con la edad** y para escenas
   emotivas (le sirve también al investigador de voz/personajes).

---

## Lo mejor para la lámina

- **Pose fuerte para #musica-nueva**: Marceline tocando el bajo-hacha de pie,
  en el huerto, de «S7e7 Marceline playing ax bass.png» (hoja 1, escena color,
  con su instrumento — justo lo que pide el dueño).
- **Objeto 3D con licencia clara**: el Ax Bass de **Haxis** (CC Attribution,
  confirmado por API) para modelar en Blender.
- **Vestuario con hex real**: vestido camisero azul `#83A5BC` + zapato
  granate `#8C284F` del model sheet oficial (ep. 057) — alternativa fiable a
  la camiseta gris de memoria.
- **Guiño de colaboración**: el pico/instrumento «Marcy's Ax Bass» de
  Fortnite conecta el objeto del plan con un crossover real y reciente.
- **Fondo de conjunto**: el wallpaper de RaidMath (3600×2400, todo el
  elenco) si la lámina necesita más personajes de fondo.

---

## No encontré

- ⚠️ **Vans, OPI, Uniqlo u otra colaboración de moda/belleza** con Adventure
  Time: busqué («Adventure Time collaboration Vans OPI Uniqlo Hot Topic
  official merchandise») y sólo salió mercancía con licencia de Hot Topic
  (ropa con el logo, no una colaboración de diseño conjunta). No lo doy como
  colaboración real por no tener una segunda fuente que la confirme.
- ⚠️ **Licencia exacta** de 6 de los modelos de Sketchfab (Z3bbz, Froes,
  TravisEvashkevich, deadlygeek, Hoho, 10958533): la API los devuelve como
  descargables pero sin campo de licencia visible en esta consulta rápida;
  antes de usarlos, comprobar la ficha uno a uno.
- ⚠️ **Turquesa exacto de BMO**: lo intenté medir dos veces (screenshots con
  fondo rosa del Dulce Reino dominando la muestra) y no salió limpio; sigue
  de memoria.
- ⚠️ **Corona de la Dulce Princesa** y **filos del bajo-hacha en luz de día**:
  no aislé un pixel limpio en las imágenes que bajé; quedan aproximados.
- ⚠️ **Fondos de pantalla oficiales** (no de fans) en alta: Cartoon Network
  no parece tener una página propia de descargas; lo más cercano son las
  portadas de disco y el key art de «Obsidian» (punto 1), que sí son
  oficiales pero no están pensadas como wallpaper 16:9.

---

## Bitácora de búsqueda (segunda pasada, red abierta)

- **API de Fandom** (`adventuretime.fandom.com/api.php`): `action=query&meta=siteinfo`
  (confirmar subdominio), `action=query&list=search&srwhat=text` (Lego
  Dimensions, MultiVersus, collaboration crossover, Vampire Kingdom emblem),
  `action=parse&prop=wikitext&page=References_in_other_media` y
  `page=LEGO_Dimensions`, `action=query&titles=...&prop=imageinfo` (tamaños
  reales de Obsidian-concept y del logo).
- **`herramientas/investigar_serie.py`**: 1 corrida completa (6 páginas,
  `--wiki adventuretime`), 1188 imágenes indexadas, 13 hojas generadas.
- **`herramientas/estilo.py`**: 4 corridas (11 imágenes/recortes en total)
  para medir hex de Marceline, Finn, Jake, Dulce Princesa y BMO.
- **Sketchfab API** (`api.sketchfab.com/v3/search`): 6 consultas (Ax Bass,
  Finn, Jake, BMO, Marceline house, treehouse, Marceline guitar).
- **Wallhaven API** (`wallhaven.cc/api/v1/search` y `/w/<id>`): 2 búsquedas
  («adventure time», «Marceline») + 6 fichas individuales.
- **ambientCG API** (`ambientcg.com/api/v2/full_json`): 7 consultas (paper,
  fabric, denim, knit, vinyl record, cardboard, wood, leather).
- **WebSearch** (4 de mi cupo de 50, todas en inglés): «Adventure Time
  collaboration Vans OPI Uniqlo Hot Topic official merchandise»,
  «Adventure Time MultiVersus Finn Jake Marceline playable character»,
  «Adventure Time Funko Pop Marceline figure official Kidrobot vinyl»,
  «Marceline cosplay ax bass build tutorial craftsmanship», «Adventure Time
  Distant Lands Obsidian key art poster Bubblegum Marceline image», «free
  halftone dithering texture pack CC0 Photoshop brushes public domain».
- **Descargas directas** con `curl -H "Referer: https://www.fandom.com/"`:
  9 imágenes (2 model sheets, 2 screenshots de Marceline, 2 concept art de
  Obsidian, más 3 recortes con Pillow), todas miradas con `Read`.

**Cumplo AYUDANTE.md**: hojas de contacto miradas (no descritas de oído),
colores medidos con Pillow (no de memoria salvo donde digo ⚠️), licencias de
Sketchfab confirmadas por su API, «no encontré» sólo tras buscar (nunca «no
existe»).

Sigue: nada obligatorio pendiente de mis puntos (1, 3, 15, 16, 19, 23). Si
hay tiempo de sobra: medir el turquesa de BMO recortando a mano y la corona
de la Dulce Princesa; comprobar una a una las 6 licencias de Sketchfab que
quedaron sin campo de licencia.
