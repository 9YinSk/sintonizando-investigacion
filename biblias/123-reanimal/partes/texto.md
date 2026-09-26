# Parte de TEXTO, JUEGOS Y TÉCNICA · Reanimal (encargo 123)

Investigador de texto, juegos y técnica. Puntos 5, 6, 11, 18, 24 y 25 de ENCARGO.md.
Aviso: `datos-texto.md` (recolectado automático) sólo trajo capturas de Steam; los
otros bloques del recolector (Danbooru/Safebooru/Wallhaven en `datos-imagen.md`)
se confundieron con Touhou/Madoka porque «los dos hermanos» no encontró página
en Fandom con ese nombre. Los personajes reales son **The Boy** y **The Girl**
(la wiki los llama también The Brother / The Sister), confirmado en
https://reanimal.fandom.com/wiki/The_Boy y https://reanimal.thqnordic.com ✅.

## 5 · Tipografía, una letra por uso

*REANIMAL* es un videojuego sin manga ni cómic propio (a diferencia de *Little
Nightmares*, que sí tiene tie-in). No hay globos, así que varias filas de la
tabla clásica «no aplican» y se explica por qué. Tildes, ñ y ¿¡ comprobadas
abriendo el archivo real de Google Fonts con `fontTools.ttLib.TTFont(...).getBestCmap()`
(script en `/tmp/claude-0/trabajo/123-reanimal-texto/fonts`), no de memoria.

| Uso | Qué se ve de verdad | Letra libre más parecida | ¿Tildes, ñ, ¿ ¡? |
|---|---|---|---|
| Logo o título | «REANIMAL» en el logo del soundtrack: mayúsculas muy condensadas, palo grueso uniforme, remates rectos, rojo sobre negro (visto en la carátula del álbum, captura de Steam del DLC *REANIMAL Soundtrack*) ✅ · https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4430060/2ce879b678581a26e0540f892a5e3ac8a3e73573/ss_2ce879b678581a26e0540f892a5e3ac8a3e73573.1920x1080.jpg | **Anton** (Google Fonts, OFL) por peso y condensación; alternativas **Big Shoulders Display** ExtraBold o **Bebas Neue Pro** ⚠️ (comparación visual del investigador; el sitio oficial no da crédito de letra para el logo) | Sí ✅ (cmap comprobado) |
| Web e interfaz oficiales | La web `reanimal.thqnordic.com` usa una letra de pago autoalojada, **«Fabrikat»** (Regular, Italic, Black, BlackItalic) en `/fonts/fabrikat-*.woff`, declarada en su CSS ✅ (visto en el HTML de la propia web) | **Barlow Condensed** ExtraBold (Google Fonts, OFL) por proporción y peso; también sirve para subtítulos y menús | Sí ✅ (cmap comprobado) |
| Cartel del mundo (letrero real, en juego) | Rótulo de neón rojo **«CINEMA»** sobre la marquesina del cine, en el pueblo inundado; tubo redondeado, mayúsculas anchas con relleno de bombillas debajo ✅ (visto, captura oficial de Steam) · https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2129530/7c4e789ddae8dbaaa8705f98ac3e77a58baee2d0/ss_7c4e789ddae8dbaaa8705f98ac3e77a58baee2d0.1920x1080.jpg | **Monoton** (Google Fonts, para el efecto de tubo de neón) o, si se quiere una letra de marquesina más plana, **Bungee** ⚠️ (propuesta visual, sin crédito oficial) | No se comprobó (decorativa, sólo mayúsculas de cartel) |
| Globo normal, grito, pensamiento, onomatopeya (manga) | **No aplica.** *Reanimal* no tiene manga ni cómic propio; no hay globos ni onomatopeyas dibujadas en pantalla en ninguna de las 14 capturas oficiales de Steam revisadas ✅ | — | — |
| Diálogo hablado / subtítulos | Hay diálogo susurrado y escaso —«por primera vez en tres juegos», dice la reseña— y **se subtitula entero**; sin pistas sólo de audio (accesibilidad) ✅ · https://gamecritics.com/jason-ricci/reanimal-review/ · confirmado también por la lista de idiomas de Steam (Subtítulos en 15 idiomas) ✅ | **Barlow Condensed** o **Noto Sans** (cubre además coreano/chino/japonés, ver abajo) | Sí ✅ |
| Interfaz de juego (menús, HUD) | **No se encontró ninguna captura de menú**: las 14 imágenes oficiales de Steam evitan mostrar HUD; en partida no hay barra de vida, mapa ni inventario visibles, igual que en *Little Nightmares* (comparación con 122-little-nightmares ✅) ⚠️ (sin captura propia de menú) | Barlow Condensed / Noto Sans | — |
| Letreros y coleccionables (Posters) | 20 «Posters» de papel por nivel; al recogerlos desbloquean arte conceptual en el menú, **no llevan texto legible**, son ilustraciones · https://reanimal.fandom.com/wiki/Posters ✅ | — | — |

**Letras para coreano, japonés y chino** (el juego trae interfaz y subtítulos en
Japonés, Coreano, Chino tradicional y Chino simplificado, comprobado en la
tabla de idiomas de Steam ✅): la familia libre equivalente es **Noto Sans**
(Noto Sans JP / KR / SC / TC, Google + Adobe, licencia OFL). Comprobado con
fontTools sobre el archivo real de Noto Sans JP: cubre hiragana (あ), katakana
(ア) y kanji comunes (字), además de tildes, ñ y ¿¡ latinas ✅. Es la opción
segura para cualquier texto del canal que quiera imitar la interfaz del juego
en otro idioma.

## 11 · Videojuegos de la franquicia

*Reanimal* es una IP nueva de Tarsier (no viene de otra franquicia), así que
«los videojuegos de la franquicia» son el juego base y su expansión. La tabla
sale de Steam (`datos-texto.md`) y de la wiki, cruzados ✅.

| Juego / DLC | Fecha | Qué añade |
|---|---|---|
| *REANIMAL* | 13-feb-2026 | Juego base: The Boy y The Girl, 9 capítulos, cooperativo a pantalla partida compartida (no split-screen) |
| *REANIMAL: The Prisoner* (cap. 1 de *The Expanded World*/Season Pass) | 7-ago-2026 | Nuevos protagonistas: The Prisoner y The Soldier, en una zona de guerra estilo I Guerra Mundial; The Mother y Spider Kids como monstruos nuevos ✅ https://reanimal.fandom.com/wiki/REANIMAL:_The_Expanded_World |
| *REANIMAL – Season Pass* | 13-feb-2026 | Acceso a los 3 capítulos de *The Expanded World* (2º cap. oct-dic 2026, 3º ene-mar 2027) ✅ |
| *REANIMAL - Foxhead and Muttonhead Masks* | 13-feb-2026 | DLC cosmético: dos máscaras desbloqueables, de zorro y de cordero, intercambiables por cualquiera de los dos hermanos como disfraz; **la máscara de identidad fija de cada uno es otra** (saco de arpillera del Niño, conejo de la Niña — ver punto 25) ✅ https://reanimal.fandom.com/wiki/Masks |
| *REANIMAL Soundtrack* | 21-jul-2026 | Banda sonora digital; su carátula trae el logo definitivo y el símbolo de la ballena espiral (punto 25) ✅ |
| *REANIMAL Demo* | 13-oct-2025 | Demo jugable previa al lanzamiento, disponible en Steam |

**Interfaz y menús:** no se encontró ninguna captura oficial de un menú o
pausa (ni en las 14 capturas de Steam ni en la wiki); en partida no hay HUD
visible (punto 6) ⚠️. Los **mandos** sí están documentados completos, con
tabla por plataforma (PS5, Xbox Series X/S, Switch 2, teclado) en
https://reanimal.fandom.com/wiki/Controls ✅: moverse, correr, agacharse,
interactuar, usar objeto, mechero/linterna (`F`/`RB`/`R`), «Llamar» al otro
jugador (`C`/`LB`/`L`, igual mecánica que en *Little Nightmares II*), y un
set aparte de controles de vehículo (barco/carrito) con acelerar, retroceder,
impulso y bocina/ataque.

**Cajas de diálogo: ninguna visible en pantalla** (punto 6): el diálogo
existe pero se resuelve con subtítulos de accesibilidad, no con un cuadro de
texto con marco propio del juego ✅.

**Logros (Achievements):** existen en Steam (categoría confirmada en la ficha
de la tienda) pero no se consiguió el texto exacto de cada uno ⚠️ — página de
la wiki https://reanimal.fandom.com/wiki/Achievements sin revisar a fondo por
límite de tiempo.

## 6 · Cómo hablan y piensan en pantalla

Es lo más importante para la lámina: aquí NO va una burbuja blanca genérica.
*Reanimal* apuesta por el silencio, no por el globo.

- **Sin globos ni cartelas de manga**: no hay tie-in de cómic (a diferencia de
  *Little Nightmares*, que sí tiene una miniserie). Confirmado revisando las 14
  capturas oficiales de Steam y la wiki de Fandom (no hay página de «cómic» o
  «comic») ✅.
- **Diálogo real pero mínimo y susurrado**: es la primera vez en tres juegos de
  Tarsier (los dos *Little Nightmares* no tenían diálogo hablado inteligible)
  que hay líneas habladas, aunque escasas, para no romper el misterio · reseña
  de Gamecritics ✅ · https://gamecritics.com/jason-ricci/reanimal-review/
- **Se subtitula todo**: «All dialogue is subtitled, and there are no
  audio-only cues for tasks that need to be completed. Subtitles cannot be
  resized» [Todo el diálogo lleva subtítulo, y no hay pistas sólo de audio
  para las tareas. Los subtítulos no se pueden agrandar] · misma reseña,
  sección de accesibilidad ✅.
- **15 idiomas con subtítulos** (incluido español de España y español
  Latinoamérica, con doblaje completo en LATAM) según la ficha de idiomas de
  Steam ✅ · https://store.steampowered.com/app/2129530/REANIMAL/ — dato que
  también interesa al investigador de voz (punto 8).
- **Nada de HUD ni iconos flotantes** sobre los personajes en ninguna de las 14
  capturas oficiales revisadas: sin barra de vida, sin indicador de objetivo,
  sin burbuja de pensamiento. La única señal en pantalla es la luz del
  mechero/linterna que llevan los hermanos ✅ (visto), igual que en *Little
  Nightmares* (comparación con 122-little-nightmares, punto 11 de esa biblia) ✅.
- **Los "Posters" y cuadros del mundo no llevan texto legible**: son ilustración
  pura (pinturas, retratos, fotos) — lista completa en
  https://reanimal.fandom.com/wiki/Paintings,_Portraits,_and_Photos ✅. No hay
  diarios ni notas escritas que se puedan leer en pantalla (a diferencia de
  otros juegos de terror con notas de papel).
- **Pensamiento:** no existe una convención visual para ello (no hay flash-back
  con texto ni burbuja); los sueños del Boy y la Girl se narran con escenas
  jugables, no con texto en pantalla · descripción de «Historia» en
  https://reanimal.fandom.com/wiki/The_Boy ✅.

**Para la lámina:** en vez de un globo de cómic, la voz del canal puede ir
escrita como si fuera un **subtítulo de juego**: una barra semitransparente
abajo, mayúsculas contenidas, sin comillas de cómic. Es fiel al juego y evita
la «burbuja blanca genérica» que rechazó el dueño.

**Fuentes comprobadas con fontTools** (glifos á é í ó ú ñ Ñ ü ¿ ¡, los diez
presentes = ✅): Anton ✅, Barlow Condensed ✅, Big Shoulders Display ✅,
Permanent Marker ✅, Yanone Kaffeesatz ✅, Noto Sans JP ✅ (+ hiragana/katakana/kanji).
La variable CSS `--yanonekaffeesatz-font` aparece en el HTML del sitio oficial
aplicada a los botones rojos «Wishlist»/«Buy», pero **no se puede confirmar si
carga de verdad esa letra** (no hay `@font-face` visible para ella en el HTML
descargado): posible resto de la plantilla genérica de THQ Nordic ⚠️.

## 18 · Estilo de dibujo y técnica (rigs y tramas: ver puntos 3 y 19)

**Quién y con qué**
- Desarrollado por **Tarsier Studios** (Suecia, los mismos creadores de *Little
  Nightmares*), publicado por **THQ Nordic**, con **Unreal Engine 5** ·
  Wikipedia (con referencia primaria del anuncio) ✅ https://en.wikipedia.org/wiki/Reanimal
- Concept art de **Konstantin Kostadinov**, **Petrus Johansson**, **Jonas
  (Steinick) Berlin** y **Lisbeth Moller Fly**, recopilado en el artbook
  digital *Art of REANIMAL* · https://reanimal.fandom.com/wiki/Art_of_REANIMAL ✅
  (créditos individuales sin confirmar quién hizo qué lámina más allá de lo
  que dice la propia wiki) ⚠️
- **Cámara dinámica compartida**: a diferencia de *Little Nightmares*, la
  cámara sigue a los DOS hermanos a la vez para «maximizar la claustrofobia y
  la tensión» y crear miedo compartido en cooperativo, según Wikipedia citando
  el material de desarrollo ✅.
- **Inspiración declarada por el estudio**: *It Takes Two*, *The Legend of
  Zelda: The Wind Waker* y *Silent Hill 2* ✅ (mismo artículo de Wikipedia,
  sección «Development»).

**Cómo está pintado** (visto en 14 capturas oficiales de Steam)
- **Claroscuro extremo**, como en *Little Nightmares*: 80-90 % del plano en
  negro o azul muy oscuro, con una sola fuente cálida (mechero, farol, neón)
  recortando a los niños ✅.
- **Paleta fría dominante** (azules y grises apagados) con **acentos cálidos
  puntuales**: neón rojo del cine, fuego, faros de coche — «smoky blues and
  dim lighting... bright neon signs or car lights», TechRaptor ✅
  https://techraptor.net/gaming/previews/tarsier-studios-reanimal-introduces-tense-and-terrifying-journey
- **Suciedad y decadencia como textura constante**: «every corner of the world
  is grey and decrepit, as if a layer of dust has settled atop the whole of
  it» [cada rincón del mundo es gris y decrépito, como si una capa de polvo lo
  cubriera todo], Gamecritics ✅ https://gamecritics.com/jason-ricci/reanimal-review/
- **Niebla y volumen atmosférico** muy marcados en exteriores (bosque, puente
  roto) para dar profundidad sin líneas de contorno duras ✅ (visto).
- **Sin contorno tipo cómic** (no hay *toon shader* de línea negra): el
  renderizado es realista/PBR con luz muy contrastada, no plano — coherente
  con el «hiperrealismo lúgubre» que la prensa atribuye al estudio ✅.
- **Escala niño-vs-mundo** como regla de composición, heredada de *Little
  Nightmares* (comparar con punto 18 de 122-little-nightmares) ✅.

**Encuadres y composición**
- Plano general con los niños diminutos en el encuadre, cámara que casi no
  corta a plano cercano en las capturas revisadas ✅.
- Vista lateral en zonas de plataformas (la cornisa de hormigón, la pasarela
  rota); vista frontal centrada en momentos de umbral (la reja circular del
  barco-prisión) ✅.
- Fuente de luz siempre motivada por un objeto de la escena (mechero, farol,
  letrero, faro de camión), nunca luz ambiental plana — refuerza que la
  oscuridad es la norma y la luz es un recurso escaso ✅.

**Cómo reproducirlo en Photoshop** (propuesta del investigador; no se encontró
tutorial oficial del estudio ⚠️)
1. Base en 2-3 tonos de azul-gris oscuro y un acento cálido saturado (rojo
   neón o ámbar de fuego); medir el hex exacto es tarea del investigador de
   imagen (punto 4), aquí sólo se describe la relación de color.
2. Capa Multiplicar al 85-95 % sobre casi toda la escena, con un agujero de
   pincel suave alrededor de la fuente de luz.
3. Ruido monocromático 3-5 % y una ligera niebla (capa blanca-azulada al
   10-15 % con máscara degradada) en el fondo.
4. Nada de línea de contorno negra: pintar con pinceles de borde suave, no de
   cómic.
5. Máscara de recorte (Clipping mask) para el brillo puntual del mechero o
   farol sobre los personajes.

**Cómo reproducirlo en Blender**
1. *Shading* PBR estándar (Principled BSDF), rugosidad alta en ropa y tela;
   nada de *toon shader* ni Freestyle (el juego no usa contorno de cómic).
2. Una sola luz Point o Spot cálida como fuente motivada, World casi negro o
   azul muy oscuro.
3. Niebla volumétrica (Volume Scatter / Mist Pass) para el aire húmedo de la
   isla.
4. Cámara con distancia focal media (35-50 mm) y los personajes ocupando poco
   del encuadre, para conservar la sensación de pequeñez.
5. Compositor: grano fino, viñeta suave y un Bloom bajo sobre las fuentes de
   luz cálida.
6. Modelos y *rigs* libres del personaje: **ver puntos 3 y 19** (el
   investigador de imagen ya trae los de Sketchfab: The Boy, The Girl, Mother,
   Hood, Sniffer, Bandage).

## 24 · Obras parecidas

**Influencias que reconoce el estudio** (citas directas, no de fans)
- ***It Takes Two***, ***The Legend of Zelda: The Wind Waker*** y ***Silent
  Hill 2*** — inspiraron «un sentido de aventura y un sentido de temor» y el
  diseño cooperativo, según el artículo de desarrollo de Wikipedia (con
  fuentes primarias) ✅ https://en.wikipedia.org/wiki/Reanimal
- **Su propio antecesor espiritual, *Little Nightmares* I y II** (mismo
  estudio): «REANIMAL proves that Tarsier doesn't need access to the IP in
  order to make *Little Nightmares*» [Reanimal demuestra que Tarsier no
  necesita los derechos de la saga para hacer *Little Nightmares*],
  Gamecritics ✅. *Little Nightmares III* pasó a Supermassive Games mientras
  Tarsier creaba esta IP nueva, confirmado por Wikipedia y por la propia
  biblia 122 ✅.
- Tarsier reconoce el cariño del público japonés por sus juegos y usó el Tokyo
  Game Show para mostrar Reanimal, entrevista de Cubed3 con Andreas Johnsson
  (cofundador) ✅ https://www.cubed3.com/features/interviews/tarsier-interview

**Comparaciones de prensa** (⚠️ salvo lo dicho)
- ***Coraline*** y el cine de Laika/Tim Burton, por el mismo motivo que en
  *Little Nightmares*: niños con máscaras cosidas o de tela ⚠️ (comparación
  del investigador, no citada literalmente en las reseñas revisadas).
- ***LIMBO*** e ***INSIDE*** (Playdead): comparación habitual del género de
  «puzzle-plataformas de terror atmosférico», mismo patrón que con *Little
  Nightmares* (ver punto 24 de 122-little-nightmares) ⚠️.
- Metacritic: 80/100 (PC y PS5), 83/100 (Xbox Series X/S); 82 % de
  recomendación en OpenCritic ✅ https://en.wikipedia.org/wiki/Reanimal
- Eurogamer, 4/5: «a thing of phenomenal artistry and mood» [algo de artesanía
  y ambiente fenomenales] ✅ https://www.eurogamer.net/reanimal-review
- Game Informer, 8.25/10, «Macabre Merit» ✅ https://gameinformer.com/review/reanimal/macabre-merit
- Destructoid, 8/10, «Frightful and delightful, very short and sweet» ✅
  https://www.destructoid.com/reviews/reanimal-review/

**Temas compartidos con *Little Nightmares*:** el miedo del niño al mundo
adulto/a la guerra de los adultos, el hambre y la mutación del cuerpo (la
oveja que devora y crece), las máscaras que ocultan identidad, la culpa y el
sacrificio entre hermanos.

**Láminas del servidor que se le parecen:** la única biblia de terror hecha
hasta ahora es **122-little-nightmares** (mismo estudio, mismo servidor). Para
no repetir sus 3 conceptos (el cuaderno del Maw → canal `guia`, la tele de la
Pale City → canal `que-estas-viendo`, la caja de música → canal `canto`):
*Reanimal* puede apuntar a **`noticias-gaming`** (canal ya existente, sin
lámina de terror todavía) o a un objeto propio de la isla (un poster
coleccionable, un mapa, una máscara) que no repita ni la tele ni el cuaderno.
No hay más biblias de terror ni de muñecos/máscaras en el servidor por ahora
✅ (comprobado con `ls biblias/`).

## 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo en cinco líneas** · https://reanimal.fandom.com/wiki/The_Island ✅
1. Todo pasa en **la Isla**, el lugar donde crecieron los hermanos, ahora
   inundado, en ruinas y en guerra.
2. La Isla tiene ciudades y pueblos enteros abandonados; el agua lo ha
   invadido casi todo (de ahí el barco y el arpón como herramientas).
3. Los monstruos nacen de heridas del pasado de los niños: el diseño de cada
   uno «gira en torno» a su trauma compartido, no son monstruos al azar
   (Wikipedia, sección Development) ✅.
4. **Las máscaras ocultan la identidad** de casi todos: los niños (zorro,
   cordero, conejo, saco con soga), los soldados (máscara de gas) y hasta
   algunos monstruos.
5. Hay una **guerra en curso** de fondo (soldados, minas navales, un
   lanzallamas, un francotirador) que se solapa con el horror sobrenatural.

**La historia por arcos** (resumen del argumento completo en Wikipedia, con
todas las referencias primarias que cita el propio artículo) ✅
https://en.wikipedia.org/wiki/Reanimal
1. **Despertar y reencuentro:** el Boy despierta en el mar tras soñar con sus
   tres amigos y su hermana mirando un pozo. Rescata a la Girl (camisón blanco,
   máscara de conejo) y llegan juntos a la Isla.
2. **Capítulos 1-2 (*Dead in the Water*, *The Cleaning House*):** rescatan a
   **Hood** de **Sniffer**, un humanoide que se teletransporta por dentro de
   cadáveres y controla los «Skins» (pieles humanas vacías y vivas).
3. **Capítulo 3 (*After the Flood*):** rescatan a **Bandage** de un pelícano
   monstruoso, atrapándolo en un granero en llamas.
4. **Capítulos 4-5 (*No Shelter*, *Down in a Hole*):** en un orfanato en
   ruinas, matan a **la Madre** (arácnida, seis patas) y rescatan a **Bucket**
   de los Spider Kids.
5. **Capítulo 6 (*Nobody Left Behind*):** los cuatro niños huyen en un camión
   de carga; para cruzar el mar, le quitan un ojo al **Caballo del Arroyo**
   (*Brook Horse*) y se lo dan a **la Ballena Espiral**, ciega, para que los
   deje pasar.
6. **Capítulo 7 (*The Spoils*):** en un metro subterráneo, la Girl vomita la
   oveja de sus visiones; la criatura crece y **se come a los tres amigos**.
7. **Capítulos 8-9 (*The Watcher*, *All-Consuming Past*):** cruzan una ciudad
   de guerra en un tanque; la oveja gigante los traga a ambos. Dentro de ella,
   un *flashback* revela que **el Boy y los tres amigos hicieron un ritual de
   sangre y arrastraron a la Girl, atada, hasta el pozo** — el sueño inicial
   era en realidad un recuerdo. La Girl «reanima» al final (de ahí el
   título) y aparece flotando en el pozo en la escena post-créditos.
8. **DLC *The Prisoner* (2026):** nuevos protagonistas, la Prisionera y la
   Soldado, en un flashback de guerra con soldados de estilo I Guerra Mundial;
   aparece un «Segundo Prisionero» misterioso que conecta con el resto de la
   trama (2º y 3º capítulo del DLC aún sin publicar, TBA en la wiki) ⚠️.

**Símbolos que un fan reconoce al instante**
- **Las máscaras de identidad, la más reconocible de todas**: **El Niño** lleva
  capucha de **saco de arpillera** con cordón al cuello (cara siempre oculta,
  sin agujeros de ojos ni boca) y **La Niña** lleva **máscara blanca de
  conejo** con una oreja rota/torcida (única con algo de cara visible: deja
  ver boca y barbilla) — descritas igual en sus fichas de personaje de la
  wiki y confirmadas también por los investigadores de imagen, vídeo y voz de
  este equipo (sin cruzarlos) ✅ https://reanimal.fandom.com/wiki/The_Boy y
  https://reanimal.fandom.com/wiki/The_Girl. Aparte hay 20+ máscaras
  coleccionables **intercambiables como disfraz** para cualquiera de los dos
  (zorro, cordero/mutón, pájaro, gusano, cerdo, cono…), incluida la DLC de
  pago *Foxhead and Muttonhead Masks* ✅ https://reanimal.fandom.com/wiki/Masks
  — pero **ninguna fuente (ni la ficha de Steam de esa DLC) confirma que el
  zorro sea fijo del Niño y el cordero fijo de la Niña**: son disfraces
  desbloqueables, no la máscara de identidad de cada uno ⚠️ (corregido en esta
  tanda: una versión anterior de esta línea sí los daba por fijos).
- **El pozo (the Well):** origen de la pesadilla y de todo el ritual de sangre;
  aparece en el sueño inicial y en el final ✅.
- **La oveja / Sheep Beast:** el monstruo central, nacido de la culpa y que se
  come a los tres amigos; su iconografía (ovejas erguidas, lluvia de sangre)
  es el clímax visual del juego ✅.
- **La ballena espiral** (*Spiral Whale*), ciega y enroscada sobre sí misma:
  su forma de espiral es el símbolo que usa la propia carátula del *REANIMAL
  Soundtrack* (espiral roja con espinas) ✅ — ver punto 5.
- **Los ataúdes (Coffins):** coleccionables que muestran los «espíritus» de
  los tres amigos y de un conejo; desbloquean un final secreto en el capítulo
  9 ✅ https://reanimal.fandom.com/wiki/Coffins
- **El mechero y el farol:** las únicas fuentes de luz de Boy y Girl,
  heredadas visualmente del mechero de Six en *Little Nightmares* ✅.
- **La guerra de fondo:** minas navales, soldados, un lanzallamas — vocabulario
  visual distinto al resto de la saga del estudio (aparece sobre todo en el
  DLC *The Prisoner*) ✅.
- **Vocabulario propio:** the Island, the Well, Sniffer, Skins, Boomers,
  Critters, the Sheep Beast, the Spiral Whale, the Brook Horse, the Mother,
  Spider Kids, Coffins, Posters, the Prisoner, the Second Prisoner, the
  Expanded World.

## Lo mejor para la lámina

- El cuadro de diálogo real del juego es un **subtítulo, no un globo**: barra
  semitransparente abajo, mayúsculas contenidas en Barlow Condensed — así se
  evita la «burbuja blanca genérica» que rechazó el dueño.
- El logo «REANIMAL» (rojo muy condensado sobre negro, tipo Anton) es un
  tratamiento de título fuerte y reconocible para encabezar la lámina.
- Un **Poster coleccionable** (papel encontrado en la Isla) es el objeto real
  perfecto para pegar el texto del canal: ya es «una hoja de papel en un sitio
  real», sin inventar nada.
- El símbolo de la **ballena espiral** (espiral con espinas, de la carátula del
  soundtrack) funciona como marca de agua o adorno de fondo sin tapar a los
  personajes.
- Luz motivada única (mechero o farol) + niebla de fondo: así la lámina no
  queda plana, igual que las 14 capturas oficiales revisadas.

## No encontré

- **TCRF (The Cutting Room Floor):** no tiene página de *Reanimal*. Comprobado
  con `tcrf.net/wiki/Reanimal` (403, verificación anti-bot de Cloudflare, dos
  intentos: `curl` directo y `navegar.py` con navegador) y con la Wayback
  Machine (`web.archive.org/cdx/search/cdx?url=tcrf.net/wiki/Reanimal` sin
  resultados). El contenido equivalente (diálogos y escenas cortadas) sí está
  en la propia wiki de Fandom, sección «Unused and Cut Content», usada en su
  lugar.
- **Captura oficial de un menú o pantalla de pausa:** ninguna de las 14
  capturas de Steam la muestra; tampoco se encontró en la wiki. Sin esto no se
  pudo confirmar la letra exacta de los menús (queda como candidata Barlow
  Condensed / Fabrikat, sin comprobar).
- **Crédito oficial de la letra del logo «REANIMAL»**: no hay press kit
  descargable enlazado desde `reanimal.thqnordic.com`; la letra libre
  propuesta (Anton) es comparación visual, no un dato confirmado por el
  estudio.
- **Texto exacto de los logros (Achievements) de Steam**: la wiki tiene la
  página pero no se revisó línea por línea por límite de tiempo de esta tanda.
- **Entrevistas técnicas en japonés o coreano**: *Reanimal* es sueco (Tarsier)
  y editado por THQ Nordic (Austria), no viene de Japón/Corea, así que no se
  buscaron entrevistas de making-of en esos idiomas más allá de confirmar que
  el juego se presentó en el Tokyo Game Show (Cubed3) y que tiene interfaz,
  subtítulos y voces en japonés, coreano y chino (tabla de idiomas de Steam).

## Bitácora

- Español: «Reanimal wiki fandom», «Reanimal tipografía logo» → sin resultados
  útiles en español; se pasó a inglés.
- Inglés (web): «Reanimal Tarsier Studios interview Unreal Engine art style»,
  «Reanimal Tarsier Studios "toon shader" OR "stop-motion" art director
  interview», «Reanimal review "no dialogue" OR "don't speak" OR subtitles
  gibberish language children», «"Reanimal" "Unreal Engine 5" Tarsier»,
  «Reanimal Tarsier Studios ArtStation concept artist "Konstantin Kostadinov"
  OR "Petrus Johansson" postmortem».
- Fandom API (`reanimal.fandom.com/api.php`): `list=allpages` (lista completa
  de páginas), `action=parse&prop=wikitext` sobre Masks, Controls, Unused and
  Cut Content, REANIMAL, The Boy, The Spiral Whale, Posters, Paintings
  Portraits and Photos, Art of REANIMAL, REANIMAL: The Expanded World,
  Coffins, The Island; `list=search` para «spiral» y «dialogue».
- `reanimal.thqnordic.com`: HTML completo descargado y filtrado con `grep`
  para fuentes (`font-family`, `.woff`) — reveló la letra «Fabrikat».
- Steam: ficha de la app 2129530 (`store.steampowered.com` + API
  `appdetails`) para descripción, 14 capturas, tabla de idiomas (interfaz,
  audio, subtítulos) y categorías.
- `en.wikipedia.org/wiki/Reanimal`: artículo completo (desarrollo, argumento,
  recepción con notas de Metacritic/OpenCritic y reseñas).
- `gamecritics.com/jason-ricci/reanimal-review`,
  `cubed3.com/features/interviews/tarsier-interview`: entrevistas y reseñas
  completas descargadas y filtradas con `python3 -re` (nunca impresas enteras).
- `tcrf.net`: dos intentos (curl y `navegar.py`), 403 verificación Cloudflare
  las dos veces; Wayback Machine CDX sin snapshots.
- fontTools: `TTFont(...).getBestCmap()` sobre Anton, Barlow Condensed, Big
  Shoulders Display, Permanent Marker, Yanone Kaffeesatz y Noto Sans JP
  (descargados de `fonts.googleapis.com`/`fonts.gstatic.com`), comprobando
  á é í ó ú ñ Ñ ü ¿ ¡ y (en Noto Sans JP) hiragana/katakana/kanji.
- Hojas de contacto propias armadas con Pillow a partir de las capturas de
  Steam (`/tmp/claude-0/trabajo/123-reanimal-texto/hoja_capturas*.jpg`),
  miradas con Read antes de describir el estilo.

## Cumplimiento de mis puntos (5, 6, 11, 18, 24, 25)

| Punto | Estado | Por qué |
|---|---|---|
| 5 · Tipografía | ✅ | Logo, web, cartel de neón y CJK comprobados con fontTools; interfaz sin captura confirmada (⚠️) |
| 6 · Cómo hablan y piensan en pantalla | ✅ | Subtítulos y ausencia de globos/HUD confirmados en dos fuentes |
| 11 · Videojuegos de la franquicia | ✅ | Tabla completa del juego base y las 5 DLC/ediciones; controles completos; sin captura de menú (⚠️) |
| 18 · Estilo y cómo replicarlo | ✅ | Motor, cámara e inspiración confirmados por Wikipedia; Photoshop/Blender son propuesta razonada del investigador (⚠️, como en 122) |
| 24 · Obras parecidas | ✅ | Influencias declaradas por el estudio + comparación con Little Nightmares y reseñas con nota |
| 25 · El mundo y sus símbolos | ✅ | Reglas del mundo, argumento completo por arcos y símbolos, todo con fuente |
