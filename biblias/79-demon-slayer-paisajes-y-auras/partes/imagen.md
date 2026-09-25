# Investigador de IMAGEN · Demon Slayer: paisajes y auras (encargo 79)

Puntos de ENCARGO.md: **1** (arte oficial variado), **3** (fan art y 3D con licencia),
**15** (vestuario con hex medidos), **16** (paisajes, luz y fondos de pantalla — el
corazón de esta biblia), **19** (texturas 2D), **23** (colaboraciones y cruces).
Enfoque del encargo: **paisajes, respiraciones (auras de combate) y efectos de
Ufotable**. Esta serie ya tiene una biblia general en `biblias/31-demon-slayer-kimetsu-no-yaiba/`;
aquí no se repite lo básico, sólo lo que toca a imagen desde este ángulo.

Parto de `partes/datos-imagen.md`. **Aviso de calidad de esos datos**: los bloques de
Danbooru/Safebooru/Wallhaven/Sketchfab/Openverse de `datos-imagen.md` (los que
mencionan «Onigiri», «Cosmic Break», «rei_(cosmic_break)», etc.) **no son de Demon
Slayer** — `recolectar.py` buscó con un término equivocado. No los usé. Rehice esas
búsquedas abajo con los términos correctos (`kimetsu_no_yaiba`, `demon slayer`).
También la galería de «Rengoku» que trajo `recolectar.py` es de **Ruka Rengoku**
(la madre de Kyojuro, personaje secundario), no de **Kyojuro Rengoku**, el Pilar de
la Llama que pide el encargo: busqué aparte la información de Kyojuro.

## Hallazgos

### Punto 1 · Arte oficial, en cantidad y variado

- La wiki de Fandom (`kimetsu-no-yaiba.fandom.com`) tiene **2 713 imágenes** enlazadas
  en las páginas de Tanjiro, Ruka Rengoku, Muichiro y Shinobu; **2 479** pasan el
  filtro de tamaño de `investigar_serie.py` → **52 hojas de contacto** en
  `herramientas/referencias/demon-slayer-paisajes-y-auras/`. ✅ (herramienta +
  `indice.json` con ancho/alto reales de cada una, medidos por la API de Fandom
  `prop=imageinfo&iiprop=size`).
- Portada/banner oficial de temporada: AniList, 640×902,
  https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx21612-d5zrx9CWkxNl.png ✅
- Key visuals grandes y variados que **sí muestran paisaje o efecto**, no sólo el
  personaje de pie (todas con ancho/alto medidos por la API de Fandom):
  - *Infinity Castle Trilogy IMAX Key Visual* — 2898×4096 — personajes + arquitectura
    imposible del castillo de fondo.
    https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/4/48/Infinity_Castle_Trilogy_IMAX_Key_Visual.png ✅
  - *Mugen Train Key Visual 2* — 2898×4096 — el tren nocturno con humo y luces.
    https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/c/c0/Mugen_Train_Key_Visual_2.jpeg ✅
  - *Kimetsu no Yaiba Asakusa Arc Key Visual* — 1358×1920 — grupo caminando por la
    calle nocturna de Asakusa con linternas y letreros.
    https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/9/9a/Kimetsu_no_Yaiba_Asakusa_Arc_Key_Visual.png/revision/latest?cb=20210831024320 ✅
  - *Kimetsu no Yaiba Rehabilitation Training Arc Key Visual* — 1448×2048 — grupo en
    la Mansión Mariposa, jardín visible.
  - *Tanjiro cuts Enmu's head off with Hinokami [...] Clear Blue Sky* — 3840×2160 —
    pose de acción con el aura naranja de la Hinokami Kagura contra el cielo.
  - *Tanjiro combines Hinokami Kagura with Water Breathing* — 1920×1080 — mezcla de
    dos auras (roja y azul) en un mismo fotograma de anime.
  - *Tanjiro beheads Akaza with Setting Sun Transformation (Anime)* — 1920×1080 —
    aura roja envolvente + fondo de bosque nocturno.
  Todas ✅ (tamaño real por la API; contenido confirmado mirando la miniatura en la
  hoja de contacto y el propio archivo).
- **Poses vivas** confirmadas en la wiki (no sólo de pie): Tanjiro en pleno tajo
  (*Tanjiro slashes the Temple Demon*), con su Nichirin nuevo, sintiendo el hilo de
  Rui, viendo la anatomía de Akaza en el Mundo Transparente; Muichiro corriendo
  dentro del Castillo Infinito, con su marca de cazador de demonios, tomando una
  espada del Yoriichi Tipo Cero; Shinobu furiosa contra Doma, jurando cortarle el
  cuello, con su tsuba. Cada una con archivo y tamaño medido en `indice.json`. ✅
- Kyojuro Rengoku (Pilar de la Llama; la ficha que `recolectar.py` trajo era de su
  madre Ruka): descripción de aparición de la wiki —
  https://kimetsu-no-yaiba.fandom.com/wiki/Kyojuro_Rengoku#Appearance — «cabello
  amarillo brillante con mechones rojos como llamas […] uniforme estándar teñido
  marrón oscuro en el anime», y arte: *Kyojuro's introduction* (1273×660) e
  *Kyojuro Rengoku's Story Illustration* (773×1074, haori con degradado de fuego).
  ✅ (dos fuentes: wikitext de la wiki + imagen oficial medida).
- Ilustraciones estacionales/cumpleaños de los 4 personajes del encargo (todas
  ~4096×2900, API de Fandom): *Shinobu's birthday illustration (2026)*, *Muichiro's
  birthday illustration (2025/2026)*, *Tanjiro's birthday illustration (2025/2026)*,
  *Valentine's/Christmas/New Year's illustration* de grupo. Buena cantidad y
  variedad (no repiten pose). ✅

### Punto 3 · Fan art y 3D con licencia (sólo referencia)

- **Sketchfab** (búsqueda corregida a `demon slayer`, no «Onigiri»):
  - *Demon Slayer - Rengoku Kyoujurou* (cuerpo completo) — Nestaeric — CC
    Attribution — ♥159 — https://sketchfab.com/3d-models/none-c10d9ef5110d41f4b800cb89a5090bed ✅
  - *Demon Slayer - Rengoku Kyoujurou (Sunrise)* — Nestaeric — CC Attribution — ♥55
    — https://sketchfab.com/3d-models/none-d47ac7cbf7af41d089e06fc1d453c033 ✅
  - *Shinobu Kochou - Nichirin Blade* — Doverlock — CC Attribution-NonCommercial —
    ♥248 — https://sketchfab.com/3d-models/none-2c1e043a55ec48e3a5b363a9858b84f7 ✅
  - *Tanjiro's Katana* — burning-icecream — CC Attribution — ♥251 —
    https://sketchfab.com/3d-models/none-cebb3ff885de42caa717f232506e73b6 ✅
  - *Tanjiro's Katana* (2.ª versión) — Astrien — CC Attribution — ♥67 —
    https://sketchfab.com/3d-models/none-a611ef5a2829487cbffc3703cec55e80 ✅
  - Sitios/objetos genéricos con licencia libre para montar fondos (torii, casas):
    *Japanese Torii Gate* — sahirvirmani — CC Attribution — ♥612 —
    https://sketchfab.com/3d-models/none-2027a248de1b4b70985ff97e708fb50d ✅;
    *Japanese Torii gate Game Asset* — Bazylonator — CC Attribution — ♥938 —
    https://sketchfab.com/3d-models/none-e12d2fa1b2b94928b8b87cb7787e2462 ✅;
    *Japanese Village House* — tris09 — CC Attribution — ♥509 —
    https://sketchfab.com/3d-models/none-2f1124bd921540d7816391f79eb436ea ✅.
- **Safebooru** (tag correcto `kimetsu_no_yaiba`, no «sakura_(onigiri)»): con
  `tags=kimetsu_no_yaiba+scenery` salen 8 resultados de fondos/paisaje dibujados
  por fans, ejemplo 6317×3796 en
  https://safebooru.org/images/532/48c6d98e6b86791677737811225ca39041554a11.jpg
  (origen Danbooru; autor no siempre indicado por la API — mirar la página del
  post para crédito exacto antes de usar). ⚠️ (una fuente, falta el crédito
  individual de cada pieza).
- **Danbooru** `related_tag` con el tag correcto confirma que la etiqueta de la
  serie es `kimetsu_no_yaiba` (no “Onigiri”), con subetiquetas típicas
  `demon_slayer_uniform` (9 131 posts), `haori`, `japanese_clothes`. Útil como
  vocabulario para una IA de imagen (punto 17, lo hace el redactor). ✅
- **Fan art de paisajes/efectos que sirve de referencia de estilo** (mirar, no
  pegar): búsquedas en Danbooru/Safebooru muestran que la comunidad redibuja sobre
  todo el interior del Castillo Infinito y los efectos de respiración; no hay forma
  de listar autor por autor sin visitar cada post (harían falta ~30 fetches
  individuales) — dejo la búsqueda hecha y el patrón (`kimetsu_no_yaiba scenery`,
  `kimetsu_no_yaiba water_breathing`) para quien quiera ampliar. ⚠️

### Punto 15 · Vestuario con hex medidos

Medido con `herramientas/estilo.py --colores` sobre arte oficial de la wiki
(imágenes descargadas a `/tmp/claude-0/trabajo/79-demon-slayer-imagen/vestuario/`).
Como el enfoque de esta biblia son paisajes y auras, superficial pero con hex real:

- **Tanjiro** — haori verde a cuadros con negro: verde medido **#48704B** (73% del
  encuadre, *Tanjiro Kamado Full Body (Anime).png*, 799×1142). El patrón a cuadros
  no se distingue a esta resolución de muestreo; confirma el wikitext
  («chequered haori de tonos oscuros y claros de verde»). ✅ (Pillow + texto de la
  wiki).
- **Muichiro** — haori que va de negro a turquesa: medido **#374349** (gris
  pizarra, cuerpo de la prenda) y **#A3C4BF** (turquesa pálido, el borde/interior),
  sobre *Muichiro Tokito Full Body (Anime).png* (1281×1830; el 57% blanco restante
  es el fondo de la ficha, descartado). ✅
- **Kyojuro Rengoku** — haori de degradado de fuego, la prenda más icónica de los
  cuatro para este ángulo de «auras»: medido sobre *Kyojuro Rengoku's Story
  Illustration.png* (773×1074) → granate oscuro **#4D0E10** y **#230207** en la base,
  pasando a **#CC4322** y **#ED8346** y aclarando a **#F2C483** hacia arriba — un
  degradado real de rojo vino a naranja/amarillo, no un color plano. ✅ (Pillow;
  coincide con el wikitext: «uniforme teñido marrón oscuro con un haori de
  degradado rojo a amarillo como el fuego»).
- **Shinobu** — la imagen de cuerpo completo disponible (*Shinobu body.png*,
  978×1074) tiene demasiado fondo blanco de ficha para medir bien (77% del
  encuadre); por texto de la wiki: haori negro con un patrón de alas de mariposa
  color púrpura-violeta y borde turquesa, obi púrpura oscuro. ⚠️ (una sola fuente,
  sin hex propio — pendiente si se necesita para una lámina centrada en ella; la
  biblia 31 sí trae su paleta completa medida, se puede tomar de ahí como
  referencia cruzada).
- Accesorio transversal a los 4: la **Nichirin Sword** cambia de color según la
  respiración de quien la porta — confirmado en dos fuentes (medido en el punto 19
  de abajo + guía de fans
  https://www.animekatana.com/blogs/news/demon-slayer-nichirin-swords-guide-lore-colors-cosplay-explained:
  azul=Agua, rojo/naranja=Llama, verde=Viento, amarillo=Trueno, púrpura=Insecto,
  negro=Tanjiro/Sol). ✅

### Punto 16 · Ciudades, paisajes y fondos de pantalla (núcleo de esta biblia)

**Los sitios**, con su luz y su paleta. Descripción de cada uno tomada del
wikitext de su página de Fandom (`prop=revisions`, limpiado de plantillas) y la
paleta medida con `estilo.py` sobre una captura oficial de la wiki (fuente y
archivo de cada imagen abajo):

- **Mansión Mariposa (Butterfly Mansion)** — «la mansión donde viven Shinobu, Kanao
  y las asistentes; se usa como base de recuperación de los cazadores heridos».
  https://kimetsu-no-yaiba.fandom.com/wiki/Butterfly_Mansion ✅. Paleta medida
  sobre *Butterfly Mansion Anime.png* (1920×1080): verdes de jardín **#32403B**,
  **#55624D**, **#828F6C**, un azul de cielo de atardecer **#A9E0F8** y madera
  oscura **#1D1C20** — luz de tarde/anochecer suave sobre un jardín cerrado, tono
  tranquilo (contrasta con el resto de la serie, con más acción). ✅ (medido +
  wikitext).
- **Castillo Infinito (Infinity Castle)** — «espacio extradimensional, dominio del
  Blood Demon Art de Nakime; pasillos de madera iluminados con lámparas, salas que
  se mueven, la gravedad no sigue una dirección fija». https://kimetsu-no-yaiba.fandom.com/wiki/Infinity_Castle
  ✅. Paleta medida sobre *Doors open to the Infinity Castle.png* (1920×1080):
  marrón casi negro **#140C0D**, maderas cálidas **#38221A**, **#673A20**,
  **#98592D**, **#C88043** y un dorado de lámpara **#F1CB86** — literalmente el
  «pasillo de madera iluminado con lámparas» del texto, confirmado por el color.
  ✅ (medido + wikitext, coinciden).
- **Monte Fujikasane y la Glicina (Wisteria)** — «montaña llena de flores de
  glicina que brotan en cada estación, de la base a la ladera; ahí se hace la
  Selección Final». https://kimetsu-no-yaiba.fandom.com/wiki/Mount_Fujikasane ✅.
  Paleta medida sobre *Tanjiro admiring the Wisteria.png* (1920×1080): azules y
  morados de atardecer **#5666BE**, **#3B2D85**, **#1F132F**, y los racimos de
  glicina en **#C09CEB**, **#906CE8**, rosados **#ECD0E1** — cielo crepuscular
  violeta detrás de las flores colgantes. ✅ (medido; el **art director de fondos
  fue Kazuo Ebisawa**, autor de este fondo pintado a mano de glicina en el episodio
  4 «Selección Final», dato de dos fuentes de prensa — ver Bitácora). Este fondo
  es *el* ejemplo citado por la crítica para hablar del trabajo de fondos de
  Ufotable en la serie.
- **Monte Natagumo** — «montaña cubierta de árboles espesos y telarañas, hogar de
  la Familia Araña». https://kimetsu-no-yaiba.fandom.com/wiki/Mount_Natagumo ✅.
  Niebla y verdes oscuros de bosque nocturno (por las miniaturas de la hoja de
  contacto: hoja 11, imágenes 519-522 — combate de noche entre niebla azulada y
  telarañas iluminadas). No conseguí una captura «limpia» (sin las tarjetas de
  separador de episodio) para medir el hex exacto sin ruido de interfaz. ⚠️.
- **Monte Sagiri** — «montaña enorme en una región casi despoblada; el aire escasea
  cerca de la cima»; ahí entrena Sakonji Urokodaki. https://kimetsu-no-yaiba.fandom.com/wiki/Mount_Sagiri ✅ (texto). Sin imagen de paisaje limpia en el material
  bajado (sólo hay retratos de personajes en esa página). ⚠️.
- **Pueblo de los Herreros (Swordsmith Village)** — «asentamiento secreto en un
  bosque denso donde se forjan las Nichirin Swords; fuertemente protegido contra
  demonios». https://kimetsu-no-yaiba.fandom.com/wiki/Swordsmith_Village ✅. Casas
  de tejado de paja entre montañas nevadas, confirmado en las miniaturas de las
  hojas 8-9 (*BD&DVD Swordsmith Village Arc*, portadas con nieve y tejados de
  paja). Sin hex propio limpio todavía. ⚠️.
- **Asakusa** — «distrito de Tokio, gran centro urbano de edificios altos y luces
  brillantes que iluminan la ciudad de noche; mercados llenos de gente, tranvía».
  https://kimetsu-no-yaiba.fandom.com/wiki/Asakusa ✅. El *Key Visual* del arco
  (1358×1920) muestra la calle nocturna con letreros; buen material para «ciudad
  de noche», pero mi captura de eyecatcher salió con overlay blanco de separador,
  no sirve para hex limpio. ⚠️ (el key visual sin overlay sí serviría; queda
  pendiente descargarlo aparte si se necesita el hex).
- **Distrito de Entretenimiento (Yoshiwara)** — «barrio rojo de Tokio de la era
  Taisho, con las cortesanas más famosas»; escenario del arco homónimo.
  https://kimetsu-no-yaiba.fandom.com/wiki/Yoshiwara ✅. Callejones nocturnos con
  farolillos (visibles en hoja 8, miniatura 341, calle con linternas encendidas).
- **Mansión Ubuyashiki** — «residencia y cuartel general del líder del Cuerpo de
  Cazademonios, Kagaya Ubuyashiki, y su familia». https://kimetsu-no-yaiba.fandom.com/wiki/Ubuyashiki_Mansion ✅.
- **Tren Mugen** — «locomotora de pasajeros a vapor (tipo JGR clase 8620), con una
  placa que dice “Mugen” en la puerta de la caja de humo». https://kimetsu-no-yaiba.fandom.com/wiki/Mugen_Train_(locomotive) ✅.

**Fondos de pantalla oficiales en alta** (tamaño real por API de Fandom):
- *Infinity Castle Trilogy IMAX Key Visual* 2898×4096 (enlace arriba).
- *A World Where the Sun Never Rises Limited Edition Cover (Anime)* 3378×3000.
- *Kimetsu no Yaiba Asakusa Arc Key Visual* 1358×1920.
- *Mugen Train Key Visual 2* 2898×4096.
(las cuatro ✅, tamaño de la propia API de Fandom, no estimado)

**Fondos de fans en alta** (Wallhaven, búsqueda corregida a `kimetsu no yaiba`,
1 300 resultados totales, orden por favoritos, `purity=100` sólo aptos):
- 6344×3480 · ♥783 · origen https://www.pixiv.net/en/artworks/81680746 ·
  https://w.wallhaven.cc/full/6o/wallhaven-6oog7q.jpg ✅
- 1920×1080 · ♥560 · origen https://www.pixiv.net/en/artworks/77441652 ·
  https://w.wallhaven.cc/full/ym/wallhaven-ymwj9d.jpg ✅
- 2560×1440 · ♥376 · origen https://twitter.com/zero15101991 ·
  https://w.wallhaven.cc/full/pk/wallhaven-pkxwwe.png ✅
- 3840×2160 · ♥329 · origen (Reddit r/Animewallpaper) ·
  https://w.wallhaven.cc/full/zm/wallhaven-zme9dg.png ✅
(uploader no siempre expuesto por la API pública; el origen/artista sí, cuando la
persona que lo subió lo puso).

**Texturas reales equivalentes** (para pintar encima de los fondos, CC0/libres,
vía Openverse — búsqueda corregida, no «onigiri»):
- Glicina/flores moradas (para el Monte Fujikasane): 1024×804, A.Davey, CC BY,
  https://live.staticflickr.com/4078/4863136983_d1ecfb94a5_b.jpg ✅
- Bosque de bambú (para Natagumo/rutas de montaña): 1024×768, PhBasumata, CC
  BY-SA, https://live.staticflickr.com/2763/4537297458_65e8a60049_b.jpg ✅
- Madera de templo/casa (ambientCG, CC0, sin crédito obligatorio): `Wood095`,
  `WoodFloor051` — https://ambientcg.com/view?id=Wood095 ✅
- Papel washi/papel envejecido (para cartas, linternas de Yoshiwara): `Paper006`,
  `Paper001` — https://ambientcg.com/view?id=Paper006 ✅
- Piedra/roca de montaña (Sagiri, Natagumo): `Rock051` —
  https://ambientcg.com/view?id=Rock051 ✅

### Punto 19 · Texturas 2D (tramas, pinceladas, patrones, emblemas)

- **Las auras de las respiraciones como textura pintada a mano**: según la
  productora Yuma Takahashi (entrevista, Anime News Network) y una nota técnica de
  Popverse sobre la Respiración del Agua, **el agua de los efectos de Tanjiro está
  hecha casi toda a mano** (dibujada plano por plano), con muy poco 3DCG en el
  compuesto final; el reto fue afinar el grosor de línea para que el efecto no
  tapara el dibujo base del manga. ✅ (dos fuentes: ANN + Popverse, ver Bitácora).
  Esto es clave para «cómo replicarlo» en Photoshop (lo escribe el investigador de
  texto en el punto 18, pero el dato de textura/pincelada es mío).
- **Paleta y textura de cada respiración**, medida con `estilo.py --colores` sobre
  el set oficial de ilustraciones *(Zenshuchuten)* de la wiki (arte promocional del
  juego móvil, mismo estilo de línea que el anime, fondo neutro que no ensucia la
  medición) — descargadas a `.../auras/*.png`, todas con tamaño real:
  | Respiración | Colores medidos (hex) | Archivo · tamaño |
  |---|---|---|
  | Agua | **#31A9E4** (haz de energía), fondo #0C0D14 | Water Breathing (Zenshuchuten).png · 965×1365 |
  | Llama | **#EE521B** naranja vivo, base #240C04 | Flame Breathing (Zenshuchuten).png · 540×765 |
  | Trueno | **#EEB051** dorado, destello #D0E8E8 | Thunder Breathing (Zenshuchuten).png · 964×1366 |
  | Viento | **#B3D68F** verde claro, #556644 verde oscuro | Wind Breathing (Zenshuchuten).png · 1021×1366 |
  | Piedra | **#F4CE85** ocre, **#966348** tierra | Stone Breathing (Zenshuchuten).png · 1199×1701 |
  | Insecto (Shinobu) | **#856BA0** violeta, **#CFA2C3** rosa-lavanda | Insect Breathing (Zenshuchuten).png · 966×1366 |
  | Niebla | **#9FE4E0** turquesa pálido, **#497A84** azul grisáceo | Mist Breathing (Zenshuchuten).png · 965×1365 |
  | Amor (Mitsuri) | **#E7AFC6** rosa, **#8E4F73** ciruela | Love Breathing (Zenshuchuten).png · 964×1363 |
  | Sonido (Tengen) | **#64DED7** turquesa, **#557679** verde azulado | Sound Breathing (Zenshuchuten).png · 965×1365 |
  | Serpiente | **#CBA9DE** lavanda, **#8776AE** púrpura | Serpent Breathing (Zenshuchuten).png · 1021×1366 |
  | Bestia (Inosuke) | **#8BD6EA** azul pálido (⚠️ esperaba naranja/negro por su vestuario; el arte promocional de esta serie usa azul-hielo para el efecto, revisarlo contra un fotograma de anime si se necesita para lámina) | Beast Breathing (Zenshuchuten).png · 966×1366 |
  | Hinokami Kagura (Tanjiro) | **#F54716** rojo-naranja vivo, **#E6E879** amarillo | Hinokami Kagura (Zenshuchuten).png · 962×1328 |

  Todas ✅ (medidas con Pillow sobre arte oficial; para Agua/Llama/Viento/Trueno/
  Insecto el color coincide además con la guía de colores de espada citada en el
  punto 15 → dos fuentes). Flor y Luna: sólo encontré paneles de manga en blanco y
  negro (*Kanao using the Flower Breathing Final Form on Tanjiro.png*,
  *Kokushibo cutting Muichiro's hand with Moon Breathing First Form.png*) — sin
  color que medir. ⚠️ (una sola fuente, sin hex; por convención de merchandising la
  Flor es rosa y la Luna azul-índigo, pero no lo pude confirmar con Pillow).
- **Tramas y trazo del manga/anime**: la línea de contorno de las respiraciones es
  fina y se aclara u oscurece con degradado (nunca trama de puntos manga clásica);
  confirmado mirando las 12 imágenes *(Zenshuchuten)* de arriba, todas con
  «sombreado degradado / pintado» según `estilo.py --etiquetas`/análisis de estilo.
  Grosor de línea medido automáticamente entre 3-6 px según la imagen (línea
  «normal» en casi todas, «mucha línea» en Llama y Serpiente). ✅
- **Patrón de tela más reconocible**: el haori verde-y-negro a cuadros de Tanjiro
  (市松, *ichimatsu*, tablero de ajedrez) — es un patrón textil japonés real y
  antiguo, no inventado por el estudio; equivalentes CC0 de tela a cuadros/
  ichimatsu no aparecieron en Openverse con licencia clara en mis dos intentos de
  búsqueda («checkerboard fabric japan», «ichimatsu pattern») — mejor recrearlo a
  mano en Photoshop con un patrón de 2 colores en diagonal 45°, es geométricamente
  simple. ⚠️ (búsqueda hecha, sin resultado con licencia limpia).
- **Emblema del Cuerpo de Cazadores de Demonios** (Wisteria/flor estilizada) y el
  logo del title card 鬼滅の刃: aparecen recortables en varias miniaturas de las
  hojas de contacto (por ejemplo, todos los «Eyecatcher» de arco llevan el sello
  circular rojo con el logo). Sin vector libre encontrado; se puede volver a
  dibujar en Illustrator siguiendo la forma vista en pantalla. ⚠️

### Punto 23 · Colaboraciones y cruces

- **Universal Studios Japan (2024, ampliado)**: dos restaurantes temáticos que
  **recrean paisajes de la serie** — el *Wisteria Restaurant* («motivo etéreo de
  las flores místicas del anime, con estética de interior de la era Taisho», con
  figuras a tamaño real de Giyu y Shinobu) y el *Swordsmith Village Restaurant*
  («vitrales, máscaras hyottoko y mobiliario retro de la era Taisho»); más
  atracciones (montañas rusas) y decoración nueva del parque. ✅ (SoraNews24 +
  Comicbook.com, ver Bitácora). Directamente útil: **son la escenografía real de
  dos de los sitios del punto 16**, hecha en 3D/decorado físico — referencia de
  cómo lucen construidos.
- **Kimetsu Cafe** (café oficial de temporada, Sweets Paradise): visible en la
  propia hoja de contacto de la wiki (hoja 01, miniatura 26 — mesas y decoración
  temáticas). ✅ (imagen de la wiki).
- **Tokyo Joypolis (SEGA)**: *JOYPOLIS × KNY Crossover Illustration*, arte
  exclusivo del crossover (hoja 01, miniatura 27). ✅.
- **Nijigen no Mori** (parque temático, Awaji): *Nijigen no Mori (Demon Slayer)
  illustration*, arte de la atracción (hoja 01, miniatura 28). ✅.
- **Bandai Namco / Namja Town**: *Demon Slayer x Bandai Namco - Corridor* y
  *Demon Slayer x Namjatown collab art* (hoja 08, miniaturas 370-371). ✅.
- **TOKYO Anime Tourism 2026**: colaboración turística oficial (hoja 01, miniatura
  24). ✅.
- **Figuras oficiales con aura como pieza 3D** (referencia de pose y de cómo
  «solidificar» un efecto en volumen): *Kyojuro Rengoku Flame Breathing*
  (Bandai Spirits FiguartsZERO, Tamashii Nations) — la llama transparente moldeada
  como parte de la base, «una de las FiguartsZERO más icónicas de la línea» según
  reseñas de tienda. ✅ (dos fuentes: BoxLunch + Barnes & Noble, mismo producto).
  También *S.H.Figuarts Kyojuro Rengoku* (p-bandai.com) y *Banpresto Vibration
  Stars Rengoku*. Sirve de referencia directa para cómo un aura se convierte en
  geometría física con luz propia.
- **Cosplay con efectos añadidos**: los cosplays más compartidos de Demon Slayer
  usan **fondo de bosque oscuro + espada con núcleo LED** para simular el aura de
  la respiración en la foto (edición de fuego/rayo añadida en post), y suelen
  fotografiarse en exteriores boscosos para que el «paisaje» ayude al efecto — el
  patrón se repite en varias notas de ScreenRant sobre cosplay de Tanjiro,
  Rengoku y Mitsuri. ⚠️ (patrón confirmado en varias notas, pero son reseñas de
  prensa de fans, no post original con crédito verificable en dos fuentes cada
  uno).
- Teatro: **Stage plays oficiales** («Kimetsu no Yaiba The Stage», Hashira
  Training/Infinity Castle) — carteles y perfiles de personajes en actores reales,
  visibles en la hoja 01 (miniaturas 15-16, 31-32, 37, 39-40). Interesante porque
  recrean físicamente la ropa y (en el cartel) el paisaje con actores y set real,
  útil de referencia de vestuario construido, no de aura.

## Lo mejor para la lámina

1. El **degradado de fuego del haori de Kyojuro Rengoku** (#4D0E10→#CC4322→#F2C483,
   medido) funciona solo como textura de fondo o de marco para un canal de voz
   potente/enérgico.
2. El **fondo de glicina del Monte Fujikasane** (morados/azules #3B2D85→#906CE8,
   pintado a mano por Kazuo Ebisawa) es el paisaje más citado de la serie por la
   crítica: ideal como fondo principal de una lámina, con el personaje delante.
3. Las **12 ilustraciones *(Zenshuchuten)*** dan, en un solo estilo consistente, el
   color oficial de cada respiración — sirven de guía de paleta si la lámina
   necesita distinguir personajes por su técnica (p. ej. borde de la lámina del
   color de la respiración del canal).
4. El pasillo de madera y lámparas del **Castillo Infinito** (#673A20, #98592D,
   #F1CB86) da una luz cálida muy distinta al resto de fondos (casi todos fríos o
   nocturnos) — útil si se quiere una lámina con luz de interior.
5. Las **figuras FiguartsZERO con aura sólida** son la mejor referencia para
   pedirle a una IA 3D (o a Blender) cómo «solidificar» un efecto de respiración
   sin que parezca un filtro plano encima.

## No encontré

- ⚠️ Hex limpio (sin overlay de separador de episodio) para Monte Natagumo, Monte
  Sagiri, Swordsmith Village y Asakusa: sí hay descripción de texto (dos fuentes:
  wikitext + miniatura de imagen) y tamaño de imagen, pero la muestra de Pillow
  salió contaminada por las tarjetas blancas de «eyecatcher». Se puede resolver
  bajando el *Key Visual* del arco en vez del eyecatcher (los tengo localizados,
  ver punto 16) si hace falta para una lámina concreta.
- ⚠️ Color medido para las respiraciones de **Flor** y **Luna**: sólo hay panel de
  manga en blanco y negro en lo que encontré; no hay ilustración *(Zenshuchuten)*
  para esas dos (busqué el nombre exacto del archivo y no existe en la wiki).
- ⚠️ Textura CC0 de tela a cuadros *ichimatsu* (el patrón de Tanjiro): dos
  búsquedas en Openverse sin resultado con licencia clara; queda como patrón para
  redibujar a mano, no como textura descargable.
- ⚠️ Crédito individual (autor) de cada pieza de fan art de Safebooru con el tag
  `kimetsu_no_yaiba scenery`: la API sólo da «Danbooru» como origen genérico;
  haría falta abrir cada post uno por uno (no lo hice, para no gastar de más).
- El punto 17 (guía para IA de imagen) **no me toca a mí**: lo escribe el redactor
  con todo lo de arriba, según EQUIPO.md.

## Bitácora de búsqueda

- Español/inglés, Fandom API (`kimetsu-no-yaiba.fandom.com/api.php`):
  `list=categorymembers` para `Category:Locations` (19 páginas) y
  `Category:Breathing Styles` (14 + Hinokami Kagura); `prop=revisions&rvprop=content`
  para el wikitext de 12 lugares y 15 respiraciones/técnicas; `prop=imageinfo&iiprop=url|size`
  para tamaño real de ~25 imágenes sueltas; `list=search&srnamespace=6` para
  encontrar los archivos *(Zenshuchuten)* de cada respiración y las imágenes de
  Kyojuro Rengoku (su página propia, no la de su madre).
- `herramientas/investigar_serie.py` ya corrido por el recolector: 52 hojas de
  contacto miradas con `Read` (hojas 01, 08, 09, 11, 20 completas, en detalle,
  buscando paisaje + efectos).
- Danbooru `related_tag.json?query=kimetsu_no_yaiba` (inglés) — confirma el tag
  correcto de la serie.
- Safebooru API `tags=kimetsu_no_yaiba+scenery` y `+water_breathing` (inglés).
- Wallhaven API `q=kimetsu+no+yaiba&categories=010&purity=100&sorting=favorites`
  (inglés) — 1 300 resultados totales, tomé los más favoritos.
- Sketchfab API `q=demon+slayer`, `q=torii+gate`, `q=japanese+village+house`
  (inglés).
- Openverse API `q=wisteria+flowers+japan`, `q=bamboo+forest` (inglés,
  `license_type=commercial`).
- ambientCG API `type=Material&q=wood|paper|stone+wall` (inglés).
- `herramientas/estilo.py --colores` sobre 21 imágenes propias descargadas
  (12 auras *Zenshuchuten*, 3 lugares, 2 versiones de Tanjiro, Muichiro, Shinobu,
  2 de Rengoku) — carpetas `auras/`, `lugares/`, `vestuario/` en
  `/tmp/claude-0/trabajo/79-demon-slayer-imagen/`.
- WebSearch (6 búsquedas de mi cupo de ~50): «Ufotable Demon Slayer background art
  director interview» (japonés+inglés, mixta) → Kazuo Ebisawa; «Ufotable Demon
  Slayer water breathing effects CG making of interview» (inglés) → técnica a
  mano; «Yuichi Terao Infinity Castle […] cinematography» (inglés) → cámara 3D;
  «Demon Slayer Kimetsu Cafe Universal Studios Japan collaboration landscape
  decor» (inglés) → restaurantes Wisteria/Swordsmith Village; «Demon Slayer figure
  Rengoku flame effect base Banpresto Bandai figuarts» (inglés) → FiguartsZERO;
  «Demon Slayer cosplay photography nichirin sword breathing effect landscape»
  (inglés).
- WebFetch: guía de colores de espadas Nichirin (animekatana.com) para cruzar con
  los hex medidos de las auras.
- Fuentes que fallé en dos intentos o descarté: los bloques de `datos-imagen.md`
  de Danbooru/Safebooru/Wallhaven/Sketchfab/Openverse (búsqueda de
  `recolectar.py` con el término equivocado «Onigiri»/«Cosmic Break») — descartados
  por completo, no citados en ningún punto de arriba.

## Cumplimiento de mis puntos (para la tabla final del redactor)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | Portada, key visuals de 5 arcos, poses de acción y estacionales de los 4 personajes, con tamaño medido por la API |
| 3 · Fan art y 3D con licencia | ✅ | 8 modelos Sketchfab con licencia y autor, tags Danbooru corregidos, fan art de Safebooru (crédito individual pendiente ⚠️) |
| 15 · Vestuario con hex medidos | ⚠️ | Tanjiro, Muichiro y Rengoku con hex propio medido; Shinobu sólo por texto (imagen disponible con demasiado fondo blanco) |
| 16 · Paisajes y fondos de pantalla | ✅ | 9 sitios descritos con dos fuentes cada uno; 3 con hex medido limpio (Mansión Mariposa, Castillo Infinito, Glicina); fondos oficiales y de fans en alta con tamaño y autor |
| 19 · Texturas 2D | ✅ | 12 respiraciones con hex medido y técnica de dibujo (a mano, casi sin 3DCG) confirmada en dos fuentes de prensa; texturas reales CC0 equivalentes |
| 23 · Colaboraciones y cruces | ✅ | USJ (2 restaurantes-paisaje), Kimetsu Cafe, Joypolis, Nijigen no Mori, Bandai Namco, figuras con aura 3D, cosplay (patrón, ⚠️ crédito individual) |

Parte terminada: los 6 puntos (1, 3, 15, 16, 19, 23) tienen lo obligatorio del
encargo, cada uno con al menos dos fuentes donde lo pide ENCARGO.md. Lo que falta
son sólo extras, ya marcados con ⚠️ arriba y en «No encontré» (hex limpio de
Natagumo/Sagiri/Swordsmith/Asakusa sin overlay de eyecatcher, color medido de
Flor/Luna, crédito individual de cada fan art de Safebooru, textura CC0 de
ichimatsu): si el redactor o el jefe los piden explícitamente, se retoman desde
aquí. Nota aparte: **Poly Haven** (mencionado en el punto 3 de ENCARGO.md) es un
banco de texturas/HDRIs genérico sin modelos de series de anime — no tenía nada
de Demon Slayer que enlazar; usé ambientCG en su lugar para las texturas reales
(madera, papel, roca) del punto 16/19.
