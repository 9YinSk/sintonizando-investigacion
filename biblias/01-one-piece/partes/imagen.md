# Parte · imagen — One Piece (#bienvenidas)

Investigador de **imagen** (equipo económico, repaso). Puntos 1, 3, 15, 16, 19
y 23 de `ENCARGO.md`, y hojas de contacto. Un piloto anterior (equipo de 8) ya
dejó `partes/arte.md` (puntos 1 y 15, con las 3 hojas actualizadas a P1-P54,
O1-O24 y V1-V30) y `partes/fanart-3d.md` (punto 3, a fondo; 19 y 23 quedaron
`(pendiente)`). Esta parte **no repite eso**: confirma que 1/3/15 están
sólidos, cierra el hueco de 16 y **hace desde cero 19 y 23** (los dos puntos
nuevos del encargo), reutilizando el trabajo sin terminar que el piloto de
`fanart-3d` dejó en `/tmp/claude-0/trabajo/01-fanart-3d/p19/` (imágenes ya
bajadas y medidas con `estilo.py`, nunca escritas en su parte).
Formato: `- dato · fuente(s) con enlace · ✅ (dos fuentes) o ⚠️ (una) · tamaño medido`.

## Hallazgos

### Hojas de contacto — comprobadas, no rehechas
`hojas/` ya tiene sus **3 archivos** (el máximo que permite `AYUDANTE.md`):
`personajes_01.jpg`, `objetos_01.jpg` y `fondos_01.jpg`. Comprobé que de verdad
llevan lo que dice `arte.md` (P1-P54, O1-O24+V1-V30, F1-F24) **por tamaño**,
sin volver a abrir las 132 celdas: `personajes_01.jpg` y `objetos_01.jpg`
miden **2400×4104 px** (una rejilla mucho más alta que la de 24 celdas
original) y `fondos_01.jpg` **2400×3648 px** (sigue en 24, F1-F24, tal cual) ·
comprobado con Pillow hoy · ✅. No hacía falta una cuarta hoja para 19/23: las
imágenes nuevas de esta parte se citan por enlace directo.

### 1 · Arte oficial variado — revisado, no repetido
- **Sólido.** `partes/arte.md` ya reúne P1-P54 (wiki + one-piece.com, con
  `Referer` correcto), cartones de cuenta atrás #ONEPIECE1000LOGS, carteles y
  hojas de modelo de *Film Red*, key visuals (ep. 1000, Egghead, Elbaph),
  portadas de tomo (1, 61, 100, 111) y arte de *Odyssey*/*Pirate Warriors 4* ·
  releído hoy, sin cambios que corregir · ✅.
- Único añadido: la **web oficial `one-piece.com/present/` y
  `one-piece.com/wallpaper/` no tienen sección de fondos descargables**
  (la primera no lista wallpapers, la segunda da 404) · comprobado hoy con
  `curl` (dos rutas) · ✅ (no encontré, dos intentos). El arte de la web oficial
  para #bienvenidas sigue siendo el de `arte.md` (fichas de personaje).

### 3 · Fan art y 3D con licencia — revisado, no repetido
- **Sólido.** `partes/fanart-3d.md` ya trae 13 modelos nuevos de Sketchfab
  (banderas, cartel de WANTED ligero, espadas de Zoro, Baratie, Log Pose),
  objetos CC0 de Poly Haven («Smuggler's Cove»), el «Pirate Kit» CC0 de
  Kenney, modelos STL de Printables y fan art nuevo de Pixiv/ArtStation, con
  el aviso de qué modelos de Sketchfab son resubidos ajenos (Tigerar1,
  Cyrone™) · releído hoy, sin nada que corregir · ✅.

### 15 · Vestuario por arco — revisado, con un cruce a 19
- **Sólido.** `partes/arte.md` mide con Pillow y `estilo.py` el vestuario de
  los 5 en 6 épocas (V1-V29), con luz/sombra en hex y qué corrige de la
  biblia (Sanji no va de negro tras el salto, es azul marino `#151531`) · ✅.
- **Cruce con el punto 19:** los kimonos de Wano (Zoro V8/V9, Nami V15, Sanji
  V21) se ven con **motivos geométricos repetidos en el obi y el forro**
  (rombos y ondas), parecidos a los patrones tradicionales japoneses
  **seigaiha** (ola) y **asanoha** (hoja de cáñamo). **No encontré** una
  entrevista o *artbook* que diga que Oda usó esos patrones en concreto (sólo
  se ve a simple vista en las imágenes de la wiki) · ⚠️ (comparación visual,
  una sola fuente: las imágenes mismas). Sirve para elegir una textura 2D
  **de verdad** en vez de inventar un estampado (ver 19).

### 16 · Ciudades, paisajes y fondos de pantalla
**Lo que ya hay (biblia §6):** 5 capturas oficiales de la wiki en 1920×1080
(Sunny, Merry, familia, funeral) y 4 fondos de fans de DeviantArt con tamaño y
autor. `arte.md` lo dejó pendiente por el límite de uso. Esto añade lo que
recolectó `recolectar.py` y no se había mirado:

- **Los 3 wallpapers más guardados de Wallhaven que sí son de la serie (no
  mezclas de mosaico)** · `partes/datos-imagen.md` (ya recolectado, sólo
  revisado hoy) · ✅ (Wallhaven, con origen marcado):
  - 7680×4320, 842 «me gusta» — [Keep Sailing](https://w.wallhaven.cc/full/72/wallhaven-72lej9.png), de **Ombobon** (DeviantArt), subido por t1khon. El Sunny navegando entre nubes, estilo pintura digital.
  - 8192×4606, 679 «me gusta» — [wallhaven-v973e3.jpg](https://w.wallhaven.cc/full/v9/wallhaven-v973e3.jpg), arte de Yamato de la web MYGIORNI, subido por orsted2222.
  - 9874×1858, 526 «me gusta» — [wallhaven-yx3kok.jpg](https://w.wallhaven.cc/full/yx/wallhaven-yx3kok.jpg), un mural panorámico con Luffy, Bartolomeo, Robin, Law y Usopp, origen [Pixiv 101279304](https://www.pixiv.net/en/artworks/101279304).
  - Los otros de la lista de Wallhaven o son mosaicos de varias series (descartados) o repiten los tres de arriba.
- **La web oficial no tiene sección de wallpapers** (visto arriba, punto 1):
  para fondos en alta, la fuente sigue siendo Wallhaven + DeviantArt, nunca la
  oficial · ⚠️ (dato negativo, dos rutas probadas).

### 19 · Texturas 2D (tramas del manga, papel, pinceladas, patrones y logos)

**Cómo se hizo.** El piloto de `fanart-3d` bajó 19 imágenes y midió 8 con
`herramientas/estilo.py` (`saturación`, `zonas_planas_pct`, `degradado_pct`,
`densidad_linea_pct`, `color_linea`) en
`/tmp/claude-0/trabajo/01-fanart-3d/p19/`, pero nunca lo escribió. Esta parte
**mira esas imágenes** (`Read`), **confirma su origen en la wiki** (siete no
tenían fuente apuntada) y añade el vocabulario y las texturas libres
equivalentes que pedía el encargo.

**Las tramas del manga, medidas de verdad (estilo.py, ±ver JSON):**
- **Página a doble plana «llegan al Nuevo Mundo»** (usada en la wiki para
  *Punk Hazard Arc* y *Thousand Sunny*): **la más entramada de todas**,
  16,7 % de línea («mucha línea»), sin color (blanco y negro), degradado 24 %.
  A ojo (`Read` de la imagen): **líneas de velocidad**, **tramado cruzado**
  (*crosshatch*) en las manos-monstruo y el mar, y **una trama de puntos en
  degradado** (halftone) para el brillo de fondo · [wiki, «Straw Hats Arrive in the New World.png»](https://static.wikia.nocookie.net/onepiece/images/7/7e/Straw_Hats_Arrive_in_the_New_World.png) · ✅ (wiki + mirada directa) · 1520×1200
- **El cartel de SE BUSCA clásico** (O3, Luffy): línea normal (7,8 %), la
  mitad de la imagen en degradado (41 %): el papel envejecido se hace con
  puntos, no con una textura plana · ya en `hojas/objetos_01.jpg` (O3) · ✅ · 744×1074
- **El cartel de Wano** (O10, Nami, 人相手配書): **casi sin línea de trama**
  (3,2 %) y **muy poco saturado** (7, casi gris): es tinta a pincel sobre
  papel claro, sin el tramado occidental del cartel clásico. **Contraste útil
  para la lámina**: el cartel «de siempre» se dibuja con trama de puntos; el
  de Wano, con pincel seco · ya en `hojas/objetos_01.jpg` (O10) · ✅ · 825×1075
- **La bandera pirata (Jolly Roger)**: casi toda a color plano (57 %), muy
  poca línea (4,7 %): un logo se lee de lejos, así que no lleva trama fina ·
  [wiki, «Straw Hat Pirates' Jolly Roger.png»](https://static.wikia.nocookie.net/onepiece/images/8/87/Straw_Hat_Pirates%27_Jolly_Roger.png) (ya en O13) · ✅ · 1432×1029
- **El logo «ONE PIECE» del manga** (letras con relleno de calavera): 70 % de
  la imagen en color plano tipo *cel*, línea normal (5,3 %), línea en marino
  oscuro `#151924` · [wiki, «One Piece Logo.png»](https://static.wikia.nocookie.net/onepiece/images/7/75/One_Piece_Logo.png) · ✅ · 1600×548 · **Es un logo
  distinto al del anime** (biblia §6, degradado celeste `#1BBEED`→`#185CB2`):
  el del manga es plano y con la calavera integrada en la O; sirve para un
  rótulo que necesite leerse en blanco y negro.
- **Dos retratos de personaje del manga pre-salto** (páginas a color de
  *Color Walk*/portada, no del anime): Luffy con saturación muy alta (74) y
  poca línea (3,8 %, color `#796435`); Zoro con mucha línea (14 %) y casi sin
  zonas planas (4 %, todo degradado o textura) — **la diferencia de cuánta
  línea lleva cada personaje no es casualidad: Zoro siempre se dibuja con más
  sombreado cruzado (más «duro»), Luffy con menos (más «limpio»)** · [wiki, «Monkey D. Luffy Manga Pre Timeskip Infobox.png»](https://static.wikia.nocookie.net/onepiece/images/7/72/Monkey_D._Luffy_Manga_Pre_Timeskip_Infobox.png) y [«Roronoa Zoro Manga Pre Timeskip Infobox.png»](https://static.wikia.nocookie.net/onepiece/images/5/5d/Roronoa_Zoro_Manga_Pre_Timeskip_Infobox.png) · ✅ · 1115×1500 y 1095×1348
- Dos infobox más del mismo tipo, sólo miradas (sin medir): **Nami manga
  pre-salto** ([wiki](https://static.wikia.nocookie.net/onepiece/images/2/2c/Nami_Manga_Pre_Timeskip_Infobox.png), 1037×1200), **Chopper manga pre-salto** ([wiki](https://static.wikia.nocookie.net/onepiece/images/c/cd/Tony_Tony_Chopper_Manga_Pre_Timeskip_Infobox.png), 1158×1300) y **Zoro manga post-salto** ([wiki](https://static.wikia.nocookie.net/onepiece/images/4/42/Roronoa_Zoro_Manga_Post_Timeskip_Infobox.png), 905×1500) · ✅ (wiki).
- **Una viñeta en blanco y negro con un personaje fumando en una taberna, un
  cartel de SE BUSCA al fondo en la pared de madera**: mucha línea (15,9 %),
  el tramado cruzado marca la madera de las paredes · imagen sin numerar del
  trabajo anterior, **no confirmé la página exacta del manga** · ⚠️ (una sola
  fuente, sin numerar) · 1250×924
- **Vocabulario de tramas, mirado directamente** (recorte del trabajo
  anterior, sin numerar): trama de puntos en degradado para un resplandor
  redondo (luna o foco), rayado diagonal para lluvia y velocidad, tramado
  cruzado para el mar y las sombras duras, "SUCCESS!" en trama de puntos
  gruesa sobre la mano · ⚠️ (recorte sin fuente exacta, pero el vocabulario
  —puntos en degradado, rayado, cruzado— es el mismo que ya sale medido
  arriba con fuente).

**Patrones de ropa (con textura libre equivalente, licencia comprobada):**
- **Seigaiha** (ondas azules superpuestas) y **asanoha** (hexágono de hoja de
  cáñamo): los dos patrones tradicionales japoneses que más se parecen a los
  estampados de los kimonos de Wano (punto 15) · comparación visual, ⚠️ (ver
  arriba). **Textura libre real y con licencia comprobada**:
  [freesvg.org/seigaiha-blue](https://freesvg.org/seigaiha-blue) y
  [freesvg.org/japanese-pattern](https://freesvg.org/japanese-pattern), **CC0
  confirmado en la etiqueta `license` de la página**
  (`creativecommons.org/publicdomain/zero/1.0`), leída con `curl` hoy · ✅.
  SVG, así que se puede escalar sin perder nitidez para el obi o el forro.

**Grano de papel y pinceladas (equivalente libre, con licencia):**
- El grano de papel real ya está en la biblia §6 (Poly Haven `weathered_planks`
  CC0, ambientCG `Paper006`/`Paper003`/`Paper001` CC0): esto no se repite.
- **Pinceles de trama para imitar el manga en Photoshop/Clip Studio (con
  licencia)**, de Clip Studio Assets (`assets.clip-studio.com`, la misma
  tienda de materiales de la app que usan los estudios de manga):
  «[halftone shading pack](https://assets.clip-studio.com/en-us/detail?id=1944085)»
  de jaqdawks, «[Essential Screentone Brushes](https://assets.clip-studio.com/en-us/detail?id=2087033)»
  de barev (tramas, medios tonos y puntos) y
  «[Halftones](https://assets.clip-studio.com/en-us/detail?id=1807645)» (tres
  tamaños de trama sin costura) · gratis, «materiales de licencia limitada»
  (se reclaman una vez y quedan en la cuenta; uso dentro de la app) ·
  comprobado por búsqueda hoy · ⚠️ (la ficha de licencia exacta de cada
  paquete no se abrió una a una; el tipo «gratis, limitada» sí es el mismo en
  los tres).

**Emblemas y logos:** la bandera pirata (arriba) y el sombrero de paja ya
tienen modelo 3D con licencia CC BY en `fanart-3d.md` §3 (punto 3): no hace
falta repetir el emblema aquí, ya cubierto. El logo del manga (arriba) es lo
nuevo de esta parte.

**No cerré del todo (quedan como ⚠️ y se explican en «No encontré»):** el
capítulo exacto de la doble plana del «Nuevo Mundo», de la viñeta de la
taberna y del recorte de vocabulario de tramas; y si Oda usó de verdad
seigaiha/asanoha o es sólo parecido visual.

**Los 6 recortes que faltaban de `p19/` (segunda tanda), medidos con `estilo.py` y con página confirmada en la wiki (API, inglés y japonés):**

- **Corrección de nombre — `zoro_haramaki.png` no es un haramaki: son dos botellas de sake**, una en un armario con bisagra y otra en la mano de Zoro. Es el **mismo panel a color** que «Roronoa Zoro Manga Pre Timeskip Infobox.png» (ya citado arriba en este punto, 14 % de línea), sólo recortado sobre el mueble de botellas en vez de sobre la cara: comparé el recorte con la imagen completa (`Read` de `zoro_manga.png`) y coinciden la bisagra del armario, la botella verde con etiqueta «SAKE» y la banda verde a cuadros (el propio obi/haramaki de Zoro, de fondo, no un objeto aparte) · fuente de la wiki para la imagen completa: [«Roronoa Zoro Manga Pre Timeskip Infobox.png»](https://static.wikia.nocookie.net/onepiece/images/5/5d/Roronoa_Zoro_Manga_Pre_Timeskip_Infobox.png), **capítulo 595** o portada del tomo 1 (ficha `Source` de la wiki) · **renombrado a `zoro_botellas_sake.png`** en la carpeta de trabajo · ✅ (comparación directa con la imagen fuente completa) · 560×280 · `estilo.py`: 16,7 % de línea (mucha), degradado 39 %, saturación 38, línea `#423E25` — mismo vocabulario de «mucha línea» que ya se midió en el propio Zoro.
- **«Hacha» Morgan, ficha de manga en blanco y negro**, con su cartel de nombre en japonés (海軍大佐 「斧手のモーガン」, «Capitán de Marina "Morgan el de la mano de hacha"»): sombreado plano tipo *cel* (67 % zonas planas), línea normal (11 %, `#262626`), sin color · [wiki, «Morgan Manga Infobox.png»](https://static.wikia.nocookie.net/onepiece/images/f/fc/Morgan_Manga_Infobox.png) · ficha `Source` de la wiki: **portada del capítulo 4** (hay una segunda versión a color de la portada del capítulo 102, pero ésta es la de blanco y negro) · comprobado también en la wiki japonesa (`斧手のモーガン`): la ficha existe pero está **vacía** (sin imagen ni capítulo, plantilla sin rellenar) · ✅ (wiki inglesa, con la versión en B/N coincidiendo) · 460×1090.
- **Nekomamushi, ficha de manga**: cara enorme del mink en su forma más felina, riendo con toda la dentadura, mucha línea (15,1 %, `#5D5D5D`), sombreado mixto, sin color · [wiki, «Nekomamushi Manga Infobox.png»](https://static.wikia.nocookie.net/onepiece/images/6/66/Nekomamushi_Manga_Infobox.png) · la ficha `Source` de la wiki lista **seis capítulos posibles** (809, 815, 909, 982, 984, 1117) sin decir cuál es la viñeta exacta de esta imagen · la página japonesa equivalente (`ネコマムシ`) **no existe** con ese título exacto · ⚠️ (una fuente, capítulo exacto sin aislar entre los seis) · 672×1062.
- **Gol D. Roger, cartel de SE BUSCA a color** (el de la recompensa real que reveló Sengoku, 5.564.800.000): degradado/pintado (64 %), poca trama de línea (5,9 %, línea normal), saturación media (35) · [wiki, «Gol D. Roger Wanted Poster.png»](https://static.wikia.nocookie.net/onepiece/images/9/90/Gol_D._Roger_Wanted_Poster.png) · ficha `Source` con **tres fuentes**: **capítulo 957**, **episodio 958** y la [noticia oficial de one-piece.com, 17-ene-2021](https://one-piece.com/news/detail/20210117_11971) · comprobado en la wiki japonesa (`ゴール・D・ロジャー`): la sección de wikitexto no tiene el campo de primera aparición relleno · ✅ (tres fuentes en la wiki inglesa) · 1770×1440.
- **Chopper, ficha de manga pre-salto** (ya vista sin medir en la tanda anterior): trama de puntos digital muy marcada (22,8 % de línea, la más entramada de las seis nuevas), sombreado mixto, saturación 50 · [wiki, «Tony Tony Chopper Manga Pre Timeskip Infobox.png»](https://static.wikia.nocookie.net/onepiece/images/c/cd/Tony_Tony_Chopper_Manga_Pre_Timeskip_Infobox.png) · ficha `Source`: portada del **capítulo 507** o del **tomo 16** · ✅ (wiki, con las dimensiones exactas 1158×1300 ya citadas) · 1158×1300.
- **Nami, ficha de manga pre-salto** (ya vista sin medir en la tanda anterior): degradado/pintado (51 %), línea normal (7,5 %), brillo alto (82, acuarela clara) · [wiki, «Nami Manga Pre Timeskip Infobox.png»](https://static.wikia.nocookie.net/onepiece/images/2/2c/Nami_Manga_Pre_Timeskip_Infobox.png) · ficha `Source` con **cuatro orígenes posibles**: capítulo 9, *Color Walk 6*, portada del capítulo 516 y portada del capítulo 1 · ⚠️ (una fuente, capítulo exacto sin aislar entre los cuatro) · 1037×1200.

**Fondo de pantalla oficial reciente de Elbaph en `one-piece.com`: no hay ninguno nuevo.** La portada de `one-piece.com` (comprobada hoy con `curl`) todavía carga una función JavaScript `hide_wallpaper_popup()` ligada a una casilla `#top_wall_popup` (guarda una cookie `hide_wall_popup` para no repetir un aviso), pero **esa casilla y su ventana emergente ya no existen en el HTML actual**: es código muerto de una campaña de fondos de pantalla anterior, no algo activo hoy. Una búsqueda en japonés («one-piece.com 壁紙 エルバフ プレゼント») sólo encontró merchandising de Elbaph (figuras, pósters, pegatinas de Tapioka), nada de wallpaper · comprobado hoy (`curl` a la portada + 1 búsqueda) · ⚠️ (no encontré, dos vías probadas). Confirma lo ya escrito en los puntos 1 y 16: la web oficial sigue sin sección de wallpapers.

### 23 · Colaboraciones y cruces

**Marcas de moda:**
- **BAPE (A Bathing Ape) × One Piece**: colección de camisetas, lanzada el
  **6 de mayo de 2017** · [us.bapepirate.com](https://us.bapepirate.com/blogs/news/a-bathing-ape-x-one-piece) + [en.jp.bape.com/collections/one-piece](https://en.jp.bape.com/collections/one-piece) (la tienda oficial sigue vendiendo la línea) · ✅ (dos páginas de la propia marca).
- **Uniqlo UT × One Piece**: colaboración de años, no un lanzamiento suelto.
  La más reciente, **primavera-verano 2026, con arte del arco de Elbaph**
  ([hypebeast.com, abr-2026](https://hypebeast.com/2026/4/one-piece-uniqlo-ut-spring-summer-ss-2026-collaboration-collection-release-info)); antes, la del **arco Egghead** (abr-2025,
  [hypebeast](https://hypebeast.com/2025/4/uniqlo-ut-one-piece-egghead-arc-collaboration-collection-release-info)) y una **«UT Archive»** que repite 6 diseños viejos (Luffy y
  Ace, la despedida de Vivi, la tripulación reunida) (jun-2025,
  [hypebeast](https://hypebeast.com/2025/6/uniqlo-new-one-piece-collection-ut-archive-release-info)); y camisetas por el **100.º aniversario de Shueisha** (mar-2026,
  [soranews24.com](https://soranews24.com/2026/03/26/uniqlo-announces-new-t-shirts-for-one-piece-naruto-and-more-for-manga-publishers-100th-birthday/)) · ✅ (Hypebeast + soranews24 + la propia tienda [uniqlo.com/es/es/spl/ut/one-piece](https://www.uniqlo.com/es/es/spl/ut/one-piece)).

**Comida rápida:**
- **McDonald's × SpongeBob SquarePants × One Piece** (la colaboración más
  reciente y más rara): **15 juguetes** en el Happy Meal, **agosto-septiembre
  de 2026**, con cada personaje de Bikini Bottom vestido de un Sombrero de
  Paja (SpongeBob = Luffy, incluida su forma Gear 5; Patricio = Zoro; Arenita
  = Nami; Calamardo = Sanji; Gary = Chopper; Perla = Robin; Larry = Franky;
  Don Cangrejo = Jinbe; Hombre y Chico Percebe = Garp y Koby; el Holandés
  Errante = Barbanegra) · [wiki, «SpongeBob SquarePants x One Piece»](https://onepiece.fandom.com/wiki/SpongeBob_SquarePants_x_One_Piece) + [Anime News Network, 1-sep-2026](https://www.animenewsnetwork.com/interest/2026-09-01/one-piece-spongebob-squarepants-fuse-in-new-mcdonald-happy-meal-commercial/.241181) · ✅ · imagen de la wiki 688×1080. **No en Japón**: la campaña japonesa de McDonald's con cartas de One Piece se **canceló** antes por un cambio de política interna sobre promociones con cartas coleccionables · [gamerant.com](https://gamerant.com/one-piece-spongebob-mcdonalds-toys/) · ⚠️ (una fuente).

**Videojuegos y gacha:**
- **Fortnite**: **NO es oficial todavía**. Sólo hay archivos filtrados
  (*dataminer*) de una piel de Luffy desde febrero de 2024, y rumores de una
  segunda tanda con Nami, Zoro, Usopp y Sanji, sin fecha · [dexerto.com](https://www.dexerto.com/fortnite/fortnites-one-piece-crossover-skins-3172559/) + [esports.gg](https://esports.gg/news/fortnite/fortnite-x-one-piece-collab-leaks-what-we-know-so-far/) · ⚠️ **(rumor, no lo des por hecho en la lámina)**.
- **Monster Strike × One Piece Film Red**: gacha con **10 personajes**, del
  **20 al 31 de agosto de 2022** · [QooApp, 20-jul-2022](https://news.qoo-app.com/en/post/112106/monster-strike-one-piece) · ✅ (más la nota de abajo).
- La misma campaña de *Film Red* llegó también a **Puzzle & Dragons** y
  **Granblue Fantasy** (verano de 2022) · [QooApp](https://news.qoo-app.com/en/post/108990/one-piece-film-red-collab-2) · ✅ (dos juegos, misma fuente de prensa del sector).
- **Dragon Ball Z × One Piece: Battle Experience** (2008): un juguete-consola
  «Let's! TV Play» de **Bandai**, por el **40 aniversario de Weekly Shonen
  Jump**; se juega gritando «Kamehameha» o «Gomu Gomu no...» a un micrófono ·
  [wiki](https://onepiece.fandom.com/wiki/Dragon_Ball_Z_x_One_Piece:_Battle_Experience) · ✅ (ficha de producto de la wiki, con fecha e imagen) · imagen 963×750.

**Cruces oficiales de anime y manga:**
- **Cross Epoch** (25-dic-2006): *one-shot* de **Oda y Akira Toriyama**
  juntando personajes de One Piece y Dragon Ball, publicado en Weekly Shonen
  Jump · [wiki](https://onepiece.fandom.com/wiki/Cross_Epoch) · ✅ · portada 1000×723.
- **Toriko × One Piece × Dragon Ball Z**, tres episodios de anime: **ep. 492**
  «The Strongest Tag-Team! Luffy and Toriko's Hard Struggle!» y **ep. 542**
  «Team Formation! Save Chopper» (ambos emitidos originalmente en 2011-2013,
  con fecha de simulcast en la wiki del 18-oct-2014) y **ep. 590** «History's
  Strongest Collaboration vs. Glutton of the Sea», emitido el **5 de marzo de
  2023** (con Toonami/Crunchyroll) · [wiki, ep. 590](https://onepiece.fandom.com/wiki/Episode_590) + [wiki, ep. 492](https://onepiece.fandom.com/wiki/Episode_492) · ✅.
- **One Piece × Toriko, JHF 3D Comics** (mar-2011): *artbook* de 64 páginas de
  **Oda y Mitsutoshi Shimabukuro**, junto a la película *One Piece 3D: Straw
  Hat Chase* · [wiki](https://onepiece.fandom.com/wiki/One_Piece_x_Toriko_JHF_3D_Comics) · ✅.
- **One Piece × Boruto, Beginner's Book** (2019): guía de iniciación
  repartida en el Jump Victory Carnival 2019, mitad de cada serie, unidas boca
  abajo · [wiki](https://onepiece.fandom.com/wiki/One_Piece_x_Boruto_Beginner%27s_Book) · ⚠️ (una fuente).

**Eventos y parques:**
- **Universal Studios Japan**: el **«One Piece Premier Show»** es un
  espectáculo anual desde **2007** (pirotecnia, proyecciones 3D, canción y
  baile) · [wiki](https://onepiece.fandom.com/wiki/One_Piece_Premier_Show) · ✅. La edición de verano trae también un
  **«One Piece × Story Ride»** ambientado en Elbaf · [usj.co.jp, ONE PIECE PREMIER SUMMER 2025](https://www.usj.co.jp/company/company_e/news/2025/pdf/0402_e.pdf) · ✅ (dos ediciones, 2025 y 2026, en la propia web de USJ).
- **J-WORLD Tokyo**: parque temático techado de Weekly Shonen Jump (One
  Piece, Dragon Ball, Naruto) dentro de Sunshine City, Ikebukuro; **abrió en
  2013 y cerró el 17 de febrero de 2019** · [wiki](https://onepiece.fandom.com/wiki/J-WORLD_Tokyo) · ✅ · imagen 473×166 (logo, pequeña).
- **ONE PIECE DAY**: evento anual oficial de fans, con exposición. La de 2025
  fue el **9-10 de agosto** en Tokyo Big Sight con la exposición **«EPISODE
  OF ELBAPH»**; la de 2026 será el **22-23 de agosto en Makuhari Messe** ·
  [one-piece.com/news/74741](https://one-piece.com/news/74741/index.html) + [onepiece-day.onepiece-base.com](https://onepiece-day.onepiece-base.com/exhibition) (búsqueda en japonés) · ✅.
- **ONE PIECE EMOTION** (25.º aniversario del anime): evento en Osaka,
  **8-30 de noviembre de 2025**, ATC Hall · [onepiece-emotion.com](https://www.onepiece-emotion.com/) · ⚠️ (una fuente, sitio oficial del evento).

**Tiendas y cafés temáticos:**
- **Mugiwara Store**: la tienda oficial de merchandising más grande, **10
  tiendas en Japón** (Shibuya —la principal—, Ikebukuro, Odaiba, Tokyo
  Station, Harajuku, Abeno, Umeda, Nagoya, Fukuoka, Kumamoto) ·
  [japan.asoventure.jp, guía 2026](https://japan.asoventure.jp/en/article/one-piece-mugiwara-store-2026-tokyo-osaka-guide) · ⚠️ (una fuente, pero coincide con la lista de ciudades de otras guías de viaje).
  Junto a la tienda de la Tokyo Tower estaba el **«Cafe Mugiwara»** (café
  biblioteca, con más de 600 tomos para leer) · [otakumode.com](https://otakumode.com/news/57e1e402a2e5a47e0a87b5a0/Cafe-Mugiwara-Photo-Report) · ✅ (reportaje + reseñas de Yelp que confirman la ubicación); **cerró
  de forma permanente en 2026**, según una guía reciente · ⚠️ (una fuente, sin
  fecha exacta de cierre).
- Antes existió el **«Tokyo One Piece Tower»**, parque temático techado
  dentro de la Tokyo Tower (2015–2020), predecesor de la tienda y el café
  actuales · [Wikipedia](https://en.wikipedia.org/wiki/Tokyo_One_Piece_Tower) · ✅.

**Lo que no se pudo enlazar a un objeto de la lámina:** estas colaboraciones
sirven sobre todo para el bot y las láminas 2 (el dueño ya dijo que «lo que no
quepa se usa después»); ninguna encaja como el objeto central de #bienvenidas,
que sigue siendo el cartel de SE BUSCA (arte.md, punto 1).

## Lo mejor para la lámina

- El **contraste de trama entre el cartel clásico (puntos, O3) y el de Wano
  (pincel seco, O10)**: si la lámina usa un cartel «occidental», la textura de
  papel debe llevar puntos finos, no una foto de papel liso.
- El **logo plano del manga** (`One Piece Logo.png`, calavera en la O) es más
  fácil de recortar en Photoshop que el degradado del anime: sirve si el
  rótulo del canal necesita leerse pequeño o en un solo color.
- Las tramas **seigaiha/asanoha de freesvg.org (CC0)** son la textura de
  relleno más honesta para el obi o el forro de un personaje en Wano, en vez
  de inventar un estampado con IA.
- **SpongeBob vestido de Luffy Gear 5** (McDonald's, 2026) es un buen dato
  para el bot o una lámina 2 sobre «lo último de la serie», no para el cartel
  principal.

## No encontré

- **La página/capítulo exacto** de la doble plana del «Nuevo Mundo», de la
  viñeta de la taberna con cartel al fondo y del recorte de vocabulario de
  tramas: busqué por título de archivo en la wiki (`allimages`, `search`
  `intitle:`) y dos de los tres aparecieron (arriba); el tercero (el recorte
  compuesto) no tenía nombre de archivo que rastrear.
- **Confirmación de que Oda usó los patrones seigaiha/asanoha**: sólo
  comparación visual (punto 15/19); no hay entrevista o *artbook* citado.
- **Wallpapers oficiales descargables** en `one-piece.com`: probé
  `/present/index.html` y `/wallpaper/index.html`, ninguno tiene galería (la
  segunda ruta da 404).
- **One Piece × Levi's o × Vans** como colaboración propia: sólo salieron
  colaboraciones de BAPE con Levi's y con Vans (sin One Piece de por medio);
  no encontré una línea de Levi's o Vans con One Piece directamente.
- **Fecha exacta del cierre de Cafe Mugiwara**: una sola fuente, sin el día.
- **El capítulo exacto, de entre varios posibles**, de las fichas de manga de Nekomamushi (seis capítulos listados en la wiki: 809, 815, 909, 982, 984, 1117) y de Nami pre-salto (cuatro: capítulo 9, *Color Walk 6*, portadas de los capítulos 516 y 1): la ficha de origen de la wiki da varios candidatos sin decir cuál es la viñeta concreta usada en la imagen.
- **Un wallpaper oficial nuevo de Elbaph en `one-piece.com`**: sólo queda una función JavaScript muerta (`hide_wallpaper_popup`) de una campaña de fondos de pantalla anterior, sin ventana emergente activa hoy; probé la portada con `curl` y una búsqueda en japonés.

## Bitácora

- **Español**: «One Piece cafe temático oficial Mugiwara Store Animate Cafe
  Japón» (WebSearch).
- **Inglés**: «Clip Studio Assets free screentone halftone brush pack
  license», «One Piece Fortnite collaboration Luffy skin 2024», «One Piece
  Uniqlo UT collection», «One Piece McDonald's Japan Happy Meal collaboration
  toys», «One Piece Universal Studios Japan attraction Grand Battle», «One
  Piece Levi's OR Vans OR BAPE OR Pepsi Japan», «One Piece collaboration Fall
  Guys OR Puzzle & Dragons OR Monster Strike gacha», «seigaiha asanoha
  Japanese pattern SVG CC0 free vector public domain» (8 búsquedas de
  WebSearch).
- **Japonés**: «ワンピース コラボ 展覧会 2025 2026» (WebSearch; salieron ONE
  PIECE DAY, ONE PIECE EMOTION y el agregador charagoo.jp).
- **API directa** (sin gastar buscador): `onepiece.fandom.com/api.php`
  (`list=search` con `intitle:`, `generator=allimages`, `prop=imageinfo`,
  `prop=images`, `action=parse&prop=wikitext`) para Cross Epoch, SpongeBob x
  One Piece, J-WORLD Tokyo, Dragon Ball Z x One Piece: Battle Experience, One
  Piece x Boruto Beginner's Book, One Piece x Toriko JHF 3D Comics, episodios
  492/542/590, y los tamaños reales de 12 imágenes.
- **Imágenes miradas con `Read`** (no sólo leídas de una lista): la hoja de
  contacto `hoja_p19.jpg` del piloto anterior (10 imágenes), el recorte
  `zoom_manga.png` (vocabulario de tramas), el recorte `nuevo_mundo_small.jpg`
  (la doble plana completa) y `bn_otros.jpg` (Morgan + viñeta de taberna).
- **Reaprovechado sin rehacer**: los 8 análisis de `estilo.py` que dejó el
  piloto de `fanart-3d` en `estilo1/estilo.json` (nunca escritos en su parte).
- **Comprobado y descartado**: `freesvg.org` sí es CC0 (leído el `<meta
  license>` de la página); la ficha del BAPE OGP no traía una imagen de
  producto usable (era el logo genérico de la tienda).
- **Segunda tanda (imagen, punto 19 y wallpaper Elbaph)**: `estilo.py` sobre
  los 6 recortes que faltaban de `p19/` (salida en `p19/estilo2/estilo.json`).
  API de `onepiece.fandom.com/api.php`: `generator=allimages` (prefijos
  `Nekomamushi`, `Morgan`, `Sake`) para localizar el archivo exacto por
  dimensiones, `action=parse&prop=wikitext` sobre 5 páginas de archivo
  (`Nekomamushi Manga Infobox`, `Morgan Manga Infobox`, `Gol D. Roger Wanted
  Poster`, `Tony Tony Chopper Manga Pre Timeskip Infobox`, `Nami Manga Pre
  Timeskip Infobox`, `Roronoa Zoro Manga Pre Timeskip Infobox`) para sacar su
  ficha `Source` (capítulo/tomo), y `prop=imageinfo` por lotes para las URL y
  el tamaño real. **Wiki japonesa** (`onepiece.fandom.com/ja/api.php`,
  confirmada que existe y responde): comprobadas `斧手のモーガン`,
  `ゴール・D・ロジャー` (páginas existen pero con la plantilla de personaje
  vacía, sin capítulo) y `ネコマムシ` (no existe con ese título) · sin
  resultado, pero comprobado en las dos wikis como pide el encargo. Imágenes
  miradas con `Read`: los 6 recortes nuevos y, para comparar,
  `zoro_manga.png` completo (confirmó que `zoro_haramaki.png` era un recorte
  de botellas de sake, no del haramaki). **1 búsqueda en japonés** (WebSearch):
  «one-piece.com 壁紙 エルバフ プレゼント» (sin wallpaper, sólo merchandising).
  **1 `curl`** a la portada de `one-piece.com` con `grep -i wallpaper`.
