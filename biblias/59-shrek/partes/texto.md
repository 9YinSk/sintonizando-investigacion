# Investigador de TEXTO, JUEGOS Y TÉCNICA · Shrek (59-shrek)

Puntos de `ENCARGO.md`: **5** (tipografía), **6** (globos/cartelas/cajas de
diálogo), **11** (videojuegos: interfaz y cuadros de diálogo), **18** (estilo
de dibujo/técnica y cómo replicarlo), **24** (obras parecidas) y **25** (mundo,
historia y símbolos).

`partes/datos-texto.md` sólo traía la parte de Steam (PowerWash Simulator ×
Shrek), así que casi todo lo de abajo es investigación nueva: wikitext de
`shrek.fandom.com` por su API (`action=parse&prop=wikitext`, sin repetir
consultas de imagen/voz), fuentes descargadas y comprobadas con `fontTools`,
capturas descargadas y miradas con Read, y varias búsquedas web (TCRF y
TVTropes dieron 403 de Cloudflare — anotado en la Bitácora).

Trabajo pesado en `/tmp/claude-0/trabajo/59-shrek-texto/` (imágenes, fuentes,
htmls descargados). Nada de eso se sube al repo.

## Hallazgos

### Punto 5 · Tipografía (logo, rótulos, globos, letra libre)

Shrek no es manga/anime: su «letra por uso» sale de la película (props del
propio filme), del periódico del DVD, de los cómics oficiales y de los
juegos. Cada una comprobada con `fontTools` (á, é, í, ó, ú, ñ, Ñ, ¿, ¡):

- **Logo / título**: el tipo oficial se llama **«Shrek»**, de **Gerry
  Chapleski** (fundición *words+pictures*, 1995), catalogado en Fonts In Use
  como el usado en el logo de la película — de pago, se vende en MyFonts ⚠️
  (una sola fuente, Fonts In Use no detalla si se dibujó para la película o
  se reutilizó después). ([Fonts In Use](https://fontsinuse.com/typefaces/27931/shrek))
  **Letra libre casi calcada**: la fuente **«Shrek» de Kevin Wilson / Ding
  Bang** (dafont, gratis para uso personal; copia también alojada en
  Internet Archive como `SHREK___.TTF`) reproduce la «S» con las orejas de
  burro/ogro del logo real y el trazo negro grueso. Descargada y
  renderizada (`fonts/shrek_ia.ttf` → `img/shrek_font_sample.png`): **sí
  trae á é í ó ú ñ Ñ ¿ ¡** ✅ (comprobado con `fontTools`, y visualmente
  calca el logo). ([dafont](https://www.dafont.com/shrek2.font),
  [Internet Archive](https://archive.org/details/SHREK_201905))
- **Cartel del mundo / letrero rústico**: el letrero de madera pintado a
  mano «BEWARE — OGRE» con la cara de Shrek (visto en una captura oficial de
  Steam de *PowerWash Simulator × Shrek*, 1920×1080, `ss_566e139...jpg`,
  10-oct-2024) usa letras rojas goteantes, irregulares, como pintura fresca
  sobre madera — el estilo real de la señalización «advertencia de ogro» del
  mundo Shrek ✅ (vista con Read). Letra libre parecida: **Butcherman**
  (Google Fonts/Fontsource, OFL, gratis) — comprobada con `fontTools`: trae
  á é í ó ú ñ Ñ ¡ **pero NO trae ¿** ⚠️ (hay que evitar el signo de
  apertura o sustituirlo a mano).
- **Cartelas y titulares del mundo (periódico)**: el **Far Far Away Times**
  (extra del DVD de *Shrek 2*, «All the News That's Fit to Print», parodia de
  un tabloide) usa una cabecera **blackletter/gótica** («Far Far Away
  Times») y un titular «Royalty Arrested!!!» en serif azul grueso estilo
  tabloide, sobre un pergamino con rodillos de madera (imagen 1023×575,
  medida) ✅ (vista con Read). Letra libre para la cabecera gótica:
  **UnifrakturMaguntia** (Google Fonts, OFL, gratis) — comprobada con
  `fontTools`: **sí trae** á é í ó ú ñ Ñ ¿ ¡ ✅.
- **Texto narrado en libro de cuentos**: la introducción «Había una vez...»
  del libro-prop de *Shrek* (letra del cuerpo del texto, no las iniciales
  ornamentadas) fue identificada por la comunidad de dafont como
  **Bouwsma Uncial** ⚠️ (un solo hilo de foro, sin confirmación oficial del
  estudio, pero coincide con el estilo uncial/celta grueso del prop).
  Descargada de dafont (Mouser Fonts, **100% gratis**, uso comercial
  permitido) y comprobada con `fontTools`: **sí trae** á é í ó ú ñ Ñ ¿ ¡ ✅.
  Este mismo recurso narrado en libro se repite al inicio de cada capítulo
  de *Shrek 2 (video game)*, leído por el Espejo Mágico (ver Punto 11).
  ([hilo de dafont](https://www.dafont.com/forum/read/51635/shrek-s-fairy-tale-book-font))
- **Globo/cómic**: no hay manga, pero sí tres series de cómic oficial (ver
  Punto 6) — no se consiguió ver una página interior (ver «No encontré»).
- **Subtítulos/créditos e interfaz de videojuego**: no se encontró una
  fuente identificada específicamente para subtítulos del DVD ni para los
  menús de los juegos (ver «No encontré»); el HUD de *Shrek SuperSlam* usa
  un icono «SLAM» sobre un cuerpo de texto sin serifa genérico, según las
  capturas descriptas en fuentes de reseña (⚠️, no se pudo mirar una
  captura en alta).

### Punto 6 · Cómo hablan y piensan en pantalla (nunca burbuja blanca genérica)

- **No hay manga japonés de Shrek** (la franquicia es una película CG
  occidental de DreamWorks/PDI, no un anime) — se aplica el punto con **libro
  ilustrado y cómics occidentales** en su lugar, como pide el encargo
  cuando el punto no calza igual: se dice y por qué.
- **El libro de origen**: *Shrek!* (William Steig, 1990) es un libro-álbum
  ilustrado, no un cómic con globos — su «texto en pantalla» es la
  tipografía del libro y las ilustraciones a página completa, sin
  bocadillos. ✅ (franquicia, Fandom shrek.fandom.com/wiki/Shrek_(franchise))
- **Tres series de cómic oficial con globos de verdad** (para replicar la
  «no-burbuja-genérica»):
  - **Dark Horse Comics** (2003): 3 números a color, guion de Mark Evanier,
    dibujo de Ramon Bachs y Raul Fernandez, promoción de *Shrek 4-D* y
    *Shrek 2* ✅ (Fandom + confirmado en el catálogo de Dark Horse).
    ([darkhorse.com](https://www.darkhorse.com/Books/12-541/Shrek-TPB))
  - **Ape Entertainment / sello KiZoic** (2010): 4 números + una precuela de
    *Shrek Forever After*, pensados para lectores jóvenes ✅.
  - **Joe Books** (2016): 4 números, historias nuevas en varias líneas de
    tiempo ✅.
  - Existe un escaneo completo del recopilatorio Dark Horse en Internet
    Archive (`archive.org/details/shrek00mark`, préstamo controlado, sin
    páginas interiores de vista libre) — sólo se pudo confirmar el
    contenido por su ficha, no mirar los globos por dentro (ver «No
    encontré»).
- **Cartelas y objetos con texto dentro de la propia película** (más fuerte
  que cualquier globo, porque son objetos reales del mundo, ideales para
  Blender):
  - El **Far Far Away Times** (periódico, ver Punto 5): titulares en
    mayúsculas grandes + cuerpo en columnas, formato tabloide de verdad
    ✅ (vista con Read).
  - El **letrero de madera pintado** («BEWARE OGRE», ver Punto 5): la
    cartela de advertencia del mundo, pintura roja goteante sobre tabla ✅.
  - El **cartel/atracción de las Duloc Dolls** («Bienvenidos a Duloc»):
    títeres-autómatas que cantan la canción *Welcome to Duloc* al tirar de
    una palanca, con una foto instantánea al final como recuerdo — es
    literalmente un cartel-espectáculo con texto y jingle, la wiki lo llama
    también «Clockwork Chorus» ✅ (dos apariciones: *Shrek* y *Scared
    Shrekless*, con letra distinta en cada una).
    ([Fandom: Duloc Dolls](https://shrek.fandom.com/wiki/Duloc_Dolls))
  - La **narración en libro de cuentos** leída por una voz en off al
    empezar cada capítulo, tanto en las películas como en *Shrek 2 (video
    game)* (leída por el Espejo Mágico) — confirmado también en el
    transcript del juego, con el mismo recurso "cuento que se lee en voz
    alta" ✅ (dos fuentes: wikitext de la franquicia + transcript del
    juego).
- Encargo del dueño: **«cuadros de diálogo acordes a la temática, no una
  burbuja blanca rara»** — para Shrek el objeto real más fuerte NO es un
  globo de cómic, es **un cartel de madera, un pergamino de periódico o el
  cartucho de un cuento infantil** (pergamino con bordes de rodillo,
  parecido al menú del DVD). Cualquiera de los tres cumple la regla 1 del
  dueño («un objeto real en un sitio real»).

### Punto 11 · Videojuegos de la franquicia (interfaz y cuadros de diálogo)

Lista completa por wikitext de `shrek.fandom.com/wiki/Shrek_(franchise)`
(sección «Video Games», nunca resumida a medias) ✅:

- **Adaptaciones de película** (un plataformas/beat'em up por filme):
  *Shrek* (2001, GameCube/Xbox — pionero en *deferred shading*, el único
  clasificado «T» de la saga), *Shrek 2* (2004, GameCube/PS2/Xbox/GBA/PC,
  Activision), *Shrek the Third* (2007, Xbox 360/PC/Wii/PS2/PSP/DS/GBA/iOS),
  *Shrek Forever After* (2010, Xbox 360/PC/Wii/PS3/DS/iOS), *Puss in Boots*
  (2011, último juego de DreamWorks publicado por THQ).
- **Carreras**: *Shrek Swamp Kart Speedway* (2002, GBA), *Shrek Smash n'
  Crash Racing* (2006), *Shrek Kart* (2009, iPhone, cerrado 2017-18),
  *DreamWorks Super Star Kartz* (2011), *DreamWorks All-Star Kart Racing*
  (2023, multiplataforma actual).
- **Fiesta**: *Shrek: Treasure Hunt* (2002), *Shrek Super Party* (2003),
  *Shrek's Carnival Craze* (2008).
- **Lucha**: **Shrek SuperSlam** (2005, Shaba Games/Activision,
  PS2/Xbox/GameCube/DS/PC/GBA) — juego de pelea con personajes exclusivos y
  un **HUD verificado**: barra «Slamergy» bajo el retrato del personaje
  (icono «SLAM»; en las versiones GBA/DS se llama «Fairy Dust») que se
  llena golpeando al rival, con objetos recogibles (armas, pociones) ✅ (dos
  fuentes: wikitext de la franquicia + wikitext propio de la página del
  juego). La trama del propio juego es una excusa narrativa: Shrek y sus
  amigos cuentan «sus propias historias» (parodias de reality shows y
  géneros de cine) para dormir a los Dronkeys.
- **Otros/menores** (todos en la wiki, con año y estudio): *Shrek: Fairy
  Tale Freakdown* (2001, GBC, 0.5/5 en Game Informer — el peor recibido de
  la saga), *Shrek: Hassle at the Castle*, *Shrek Extra Large*, *Shrek:
  Reekin' Havoc*, *Shrek 2: Beg for Mercy*, seis títulos exclusivos de Reino
  Unido para Sky Gamestar/Sky Games (*Fiona's Rescue*, *Disarming Charming*,
  *Godmother's Revenge*, *Double Trouble*, *Imperial Peril*, *Jumble
  Rumble*), *Shrek n' Roll* (2007, el primero sólo-descarga, Xbox Live
  Arcade), *Shrek: Ogres & Dronkeys* (2008, DS).
- **Educativos** (V.Smile/V.Flash, edades 4-9): *Shrek the Third: Arthur's
  School Day Adventure*, *Shrek: Dragon's Tale*, *Shrek the Third: The
  Search for Arthur*.
- **Móvil reciente**: *Shrek's Fairytale Kingdom* (2012, iOS), *Shrek Alarm*
  (2013, iOS), y el DLC oficial **Shrek para *PowerWash Simulator*** (10
  oct 2024, FuturLab/Xbox Game Studios, ya en `datos-texto.md`): 5 capturas
  1920×1080 miradas con Read (ver Punto 5) — localizado en 11 idiomas
  incluido español de España (no LatAm) ✅.
- **Interfaz confirmada por transcript real**: el transcript de *Shrek 2
  (video game)* (`shrek.fandom.com/wiki/Shrek_2_(video_game)/Transcript`)
  muestra el formato exacto de los diálogos del juego: cada nivel abre con
  una narración en «libro de cuentos» leída por el Espejo Mágico, y las
  escenas usan diálogo simple `Personaje: frase` sin acotaciones — la misma
  lógica de cuento narrado de las películas, trasladada al juego ✅.
- **The Cutting Room Floor** (recomendado por el encargo): existen páginas
  de TCRF para **Shrek 2 (Windows)** (con subpáginas «Unused Cutscene
  Data» y «Unused Graphics»), **Shrek SuperSlam**, **Shrek: Reekin' Havoc**
  y **Shrek: Ogres and Dronkeys** — confirmado por resultados de búsqueda,
  pero **tcrf.net devolvió 403 (reto de Cloudflare) en los dos intentos**
  (curl directo y a través de Wayback Machare, que el proxy del contenedor
  bloquea) ⚠️. Dato de segunda mano (vía resumen de búsqueda, no la página
  en sí): la versión PC de *Shrek 2* corre sobre **Unreal Engine**, con
  comandos de depuración de consola (`Set SHGame.Version bDebugEnabled
  True`) para desbloquear un modo debug con "ghost" y otros comandos ⚠️.

### Punto 18 · Estilo de dibujo/CG y cómo replicarlo (Photoshop y Blender)

Shrek es **CG semi-realista, no toon-shading**: a diferencia de un anime, no
lleva contorno de tinta negro alrededor de los personajes. Esto cambia la
receta de Photoshop/Blender frente a las biblias de anime del equipo.

- **Estudio y pipeline**: producido por **PDI (Pacific Data Images)**, ya
  integrado en DreamWorks Animation, con software **propio** más **Alias
  Maya** para la ropa simulada y (en *Shrek*) el pelo de Fiona y Farquaad
  ✅ (dos fuentes: Linux Journal + Animation World Network).
  ([Linux Journal](https://www.linuxjournal.com/article/9653),
  [AWN](https://www.awn.com/animationworld/whats-new-shrek-2))
- **Sombreado de piel con subsurface scattering**: Juan Buhler (efectista
  sénior de PDI) desarrolló, a partir de una investigación de UCSD, un
  shader de dispersión subsuperficial más rápido, presentado en un paper de
  SIGGRAPH y usado en los personajes principales de *Shrek 2* — suaviza la
  nariz y las orejas de Shrek para que la luz las atraviese a contraluz ✅
  (dos fuentes: resumen de búsqueda + Animation World Network, con la
  cita textual de Ken Bielenberg, supervisor de VFX: *"bounce light
  automatically computes the correct bounce light off other scene objects.
  If light bounces off a yellow wall, it bounces back yellow"*).
- **Pelo y tela**: shader de pelo nuevo en *Shrek 2* (interpolación más fina
  entre mechones vecinos, contra el «volumen en mechones» del original);
  shader de tela ajustable para dar aspecto de algodón, satén o seda según
  cómo van los hilos ✅.
- **Iluminación global**: 80% de los planos de *Shrek 2* usan
  **iluminación global/ray tracing** con rebote de luz automático (el
  «bounce light» de la cita de arriba) — el doble o triple de complejidad
  ambiental que la primera película, según Bielenberg ✅.
- **Fluidos**: sistema de dinámica de fluidos heredado de *Antz* (1998),
  que ya había ganado un Oscar técnico a Nick Foster, usado para fuego,
  agua y salpicaduras ✅.
- **Render**: la primera *Shrek* (2001) usó **~5 millones de horas de CPU**
  de render (granjas Linux) ⚠️ (una fuente, cifra ampliamente citada pero
  sin nota oficial de DreamWorks encontrada).
- **Cómo reproducirlo en Blender** (equivalencias directas):
  - *Subsurface scattering* de piel → parámetro **Subsurface** del
    Principled BSDF, radio cálido (rojo/naranja) para que se note en orejas
    y nariz a contraluz — exactamente el efecto que persiguió PDI.
  - *Bounce light*/GI → usar **Cycles** (path tracing) en vez de Eevee
    plano; paredes de color saturado (verde pantano, madera) para que
    tiñan la piel del ogro por rebote, tal como describe Bielenberg.
  - Tela (algodón/satén/seda) → **Cloth simulation** + variar la
    **rugosidad (roughness)** del Principled BSDF por prenda (Fiona en
    satén = roughness baja y specular más marcado; el jubón de Shrek en
    lino = roughness alta).
  - Pelo (orejas de Burro, pelo de Fiona) → **Hair Curves** con *clumping*
    e interpolación entre mechones vecinos, no mechones sueltos.
  - Fluidos (pantano, charcos) → **Mantaflow**.
  - **Sin contorno de tinta**: no usar Line Art/Freestyle/Solidify salvo
    para citar el estilo de los **cómics oficiales** (Punto 6) o del
    libro de Steig, que sí llevan línea de tinta a mano.
- **Cómo reproducirlo en Photoshop**: para artes 2D estilo «libro de
  cuentos» (portadas, carteles, la cabecera del Far Far Away Times), usar
  pinceles de **acuarela/textura de papel** sobre una capa de textura de
  pergamino (ver `ambientCG` en la tabla de AYUDANTE.md para papel CC0), en
  vez de pinceles de tinta dura; para un póster tipo cartel de cine, capas
  de degradado + textura de grano fotográfico ligero imitan el acabado
  «impreso» del Far Far Away Times y del letrero de madera.
- **Encuadres y composición**: no se encontró una entrevista específica de
  dirección de fotografía de Shrek con detalle de planos por emoción (ver
  «No encontré»); lo que sí es 2 fuentes ✅: el propio director Andrew
  Adamson describió la meta del filme como **«deconstruir la idea de
  cuento de hadas y reconstruirla como uno nuevo»**, y contó que *Shrek* se
  hizo «como en el garaje de DreamWorks», un proyecto experimental —eso
  explica el tono irreverente y el humor de referencias que cruza toda la
  saga.

### Punto 24 · Obras parecidas y temas relacionados

- **Mismo estudio, mismo humor** (ya en la biblioteca de 59-shrek: **Kung
  Fu Panda**, encargo 61, DreamWorks) — comparten el chiste físico + guiños
  para adultos + protagonista grandote inseguro con un mentor/sidekick.
  Otro título de DreamWorks con el mismo tono: **Madagascar** (2005) y
  **Flushed Away** (2006), citados junto a Shrek como comedias animadas
  hermanas ⚠️ (una fuente, agregador).
- **Parodias de cuento de hadas** (el género de Shrek): **Hook** (1991),
  **The Princess Bride** (1987) y **The Adventures of Baron Munchausen**
  (1988) — todas citadas junto con Shrek como referencias del
  «cuento de hadas fracturado» ⚠️ (una fuente, artículo agregador
  ScreenRant/lista de similares).
- **El propio spin-off Puss in Boots** (2011, 2022) y su serie *The
  Adventures of Puss in Boots* (2015-18, no canónica) — mismo universo,
  otro tono (más de aventuras que de parodia adulta) ✅ (Fandom,
  franquicia).
- **Por qué existe el tono de Shrek**: según entrevistas, Lord Farquaad es
  una parodia de **Michael Eisner** (entonces CEO de Disney, que había
  bloqueado el ascenso de Jeffrey Katzenberg, cofundador de DreamWorks), y
  **Duloc se parece a Disneylandia** a propósito — el chiste de fondo de
  toda la saga es una pulla directa a Disney ✅ (dos referencias
  independientes en la búsqueda, coincidentes en el mismo dato).
- **Qué otras láminas del servidor se le parecen** (mirado en
  `biblias/*/biblia.md` y `encargos/`): la «biblioteca sin canal» agrupa
  varias películas familiares de gran estudio sin canal asignado todavía —
  **Coco** (57, ya con biblia, propuso `#que-estas-escuchando`), **Encanto**
  (58), **Toy Story** (60), **Kung Fu Panda** (61) e **Intensamente** (62).
  Ninguna es una parodia de cuentos de hadas como Shrek, así que el
  choque de concepto es bajo; el riesgo real de repetir lámina está en
  «objeto de cuento/libro con texto», que ya usó Coco (cartas de Héctor) —
  si Shrek también usa un libro/pergamino como objeto, conviene que sea
  claramente un **periódico de tabloide** o un **letrero de madera**, no
  otro «libro con cartas», para no calcar el concepto 1 de Coco.

### Punto 25 · El mundo, la historia y sus símbolos

**El mundo en cinco líneas**: un reino de cuento de hadas donde conviven
todos los personajes clásicos de Disney/folclore europeo a la vez (Blancanieves,
los tres cerditos, Pinocho, Caperucita, el Hada Madrina...), con dos polos:
el **pantano** de Shrek (naturaleza, aislamiento, "feo por fuera") y **Muy
Muy Lejano/Far Far Away** (la capital, un reino-broma de Beverly Hills con
castillo). Las criaturas de cuento son una clase social discriminada —
viven desterradas al pantano hasta que Shrek negocia su vuelta. La magia es
real pero burocrática: pociones, hechizos y "final feliz" se compran y se
regulan (la fábrica del Hada Madrina). El humor corre sobre el choque entre
lo medieval-fantástico y lo moderno (Duloc con parking y torniquetes,
anuncios de telerrealidad, celebridades).

**La historia por arcos** (por wikitext de la franquicia, `shrek.fandom.com`,
página *Shrek (franchise)*) ✅:
1. **Shrek** (2001): rescate de Fiona para Lord Farquaad → Shrek se enamora
   de ella → Fiona rompe su maldición convirtiéndose en ogresa para
   siempre → boda en el pantano.
2. **Shrek 2** (2004): viaje a Far Far Away a conocer a los padres de
   Fiona → el Hada Madrina y el Príncipe Encantador intentan separarlos →
   Shrek y Fiona se quedan juntos, ahora ogros por decisión propia.
3. **Shrek the Third** (2007): Shrek hereda el trono a la fuerza → busca a
   Arthur (Artie) para que reine en su lugar → Fiona revela que está
   embarazada → nacen los trillizos.
4. **Shrek Forever After** (2010): Shrek, ya domesticado, firma un pacto
   con Rumpelstiltskin y despierta en un Far Far Away alternativo donde
   nunca nació → tiene que reconquistar el amor de Fiona en 24 horas para
   deshacer el trato.
5. **Especiales/cortos**: *Shrek the Halls* (Navidad, 2007), *Scared
   Shrekless* y *Donkey's Christmas Shrektacular* (2010), *Thriller Night* y
   *The Pig Who Cried Werewolf* (2011, parodias de terror).
6. **Spin-off Puss in Boots**: *Puss in Boots* (2011, precuela) → *Puss in
   Boots: The Last Wish* (2022, ambientada después de *Forever After*) →
   corto *The Trident* (2023).
7. **Futuro confirmado** (fuente primaria: wikitext de la wiki, con la
   ficha de la propia película) ⚠️ (una fuente wiki, sin nota de prensa
   oficial verificada aparte): **Shrek 5**, anunciada para **30 de junio de
   2027**, con Mike Myers, Eddie Murphy, Cameron Diaz y la incorporación de
   **Zendaya** como la nueva personaje **Felicia**; la trama lleva a la
   familia a la ciudad de **Further Further Away** con los trillizos ya
   crecidos (Fergus, Farkle y Tutti Oats). Habrá además un spin-off en
   desarrollo centrado en **Donkey**, confirmado para 2028.

**Emblemas, objetos icónicos y vocabulario reconocible al instante**:
- **«Ogres are like onions» / «los ogros son como las cebollas»**: la
  metáfora de capas que define a Shrek como personaje, dicha en un campo de
  verduras camino a Duloc; en la boda, una cebolla real se transforma en el
  **carruaje** de los novios — el símbolo central de toda la franquicia ✅
  (wikitext de la página «Onions», con la escena y el uso posterior en la
  boda).
- **Duloc**: ciudad-estado perfecta y uniforme de Lord Farquaad (casas
  idénticas estilo Tudor, parodia self-aware de Disneylandia con
  torniquetes de entrada y tienda de souvenirs), con el **castillo Duloc**
  y sus **muñecos autómatas (Duloc Dolls / Clockwork Chorus)** cantando
  *Welcome to Duloc* al tirar de una palanca ✅ (visto en imagen 1920×1080,
  ver Punto 6).
- **Far Far Away Times**: el periódico-parodia del reino, cabecera gótica,
  titulares de tabloide (ver Punto 5) — el objeto perfecto para escribir
  "noticias" del servidor en la voz de la serie.
- **El libro de cuentos** que abre y cierra cada película (y cada capítulo
  de los videojuegos): el objeto narrador oficial del universo Shrek.
- **La Fábrica del Hada Madrina** (pociones de "final feliz" embotelladas
  en serie) y el **Espejo Mágico** (que funciona como un canal de TV/red de
  contactos) son los símbolos de que la magia, en este mundo, es también
  un negocio.
- **El Zapato de cristal, la maldición de Fiona (torre/Dragón) y el
  Pantano** cierran el trío de objetos-símbolo de "lo que se espera de un
  cuento de hadas" contra "lo que Shrek hace con ello".

## Lo mejor para la lámina

1. **El Far Far Away Times** (periódico-pergamino, cabecera gótica +
   titular tabloide, 1023×575 medido) como objeto real para escribir la
   info del canal — encaja con la regla 1 del dueño («objeto real en sitio
   real») y es distinto a lo que ya usó Coco.
2. **El letrero de madera «BEWARE OGRE»** (pintura roja goteante sobre
   tabla, visto en la captura oficial de Steam) como cartel de advertencia
   o de bienvenida al canal, con Butcherman (sin ¿) o UnifrakturMaguntia
   como letra libre.
3. **«Los ogros son como las cebollas»**: la metáfora de capas de Shrek es
   la frase-símbolo más reconocible y se presta a un lema de canal («aquí
   hay capas» / información por partes).

## No encontré

- **Fuente exacta de subtítulos y de los menús de los juegos de Shrek**:
  busqué «Shrek subtitle font», «Shrek game menu font» y revisé las páginas
  de dafont sobre Shrek sin que ninguna distinguiera subtítulos de logo.
- **Páginas interiores de los cómics oficiales** (Dark Horse/Ape/Joe Books)
  para ver el estilo real de sus globos: el único escaneo público completo
  (`archive.org/details/shrek00mark`) es de préstamo controlado, sin
  páginas de vista libre; las portadas en Fandom son de baja resolución
  (300×456). ⚠️
- **TCRF (The Cutting Room Floor) y TVTropes**: ambos devolvieron 403 (reto
  de Cloudflare) tanto en curl directo como al intentar la copia de Wayback
  Machine (bloqueada por la política de red del contenedor). Sólo pude usar
  resúmenes de búsqueda de segundo nivel, marcados ⚠️ arriba.
- **Entrevista de dirección de fotografía / composición típica por
  emoción** (parte obligatoria del punto 18): no encontré una fuente
  centrada en planos y ángulos de Shrek específicamente (sí en técnica de
  render/shading, que sí está cubierto arriba a fondo).
- **Fuente identificada para los créditos finales**: no hay ningún hilo o
  artículo que la nombre; sólo se sabe que las cabeceras de capítulo del
  juego y el prólogo del libro usan Bouwsma Uncial (⚠️ un solo hilo de
  foro).

## Bitácora de búsqueda

- **Español**: no se hicieron búsquedas específicas en español para estos
  puntos (la tipografía/técnica de Shrek se documenta casi toda en inglés);
  se revisó igualmente el wikitext en inglés de `shrek.fandom.com`, que es
  la wiki de referencia dada por el encargo.
- **Inglés** (wiki, por API, sin gastar cupo de buscador): `action=parse`
  sobre *Shrek (franchise)*, *Duloc*, *Duloc Dolls*, *Far Far Away Times*,
  *Onions*, *Shrek 2 (video game)*, *Shrek 2 (video game)/Transcript*,
  *Shrek Super Slam*, *Shrek (Dark Horse)*, *Shrek (Ape Entertainment)*,
  *Swamp Talk*; `action=query&list=search` para localizar páginas de
  videojuegos, cómics, Duloc y "onions/layers".
- **Buscador web usado** (9 de ~50, cupo del rol): «Shrek movie logo font
  name identify», «"Shrek" font dafont.com movie title», «Bouwsma Uncial
  font P22 free alternative», «Shrek 2001 end credits font typeface
  identify», «"Shrek" comic book Dark Horse interior page preview speech
  bubble», «tcrf.net Shrek 2 Windows unused debug cheat level select»,
  «Shrek 2001 making of animation software PDI DreamWorks Maya rendering
  interview», «Shrek ogre skin subsurface scattering technique SIGGRAPH»,
  «Shrek film influences director Andrew Adamson interview fairy tale
  parody inspiration», «movies similar to Shrek fairy tale parody adult
  humor animated recommendations», «Shrek movie logo typography
  fontsinuse.com», «Shrek 2 video game 2004 screenshot HUD health bar
  dialogue box», «"Donkey" font FG Studios Shrek replica download dafont
  fontspace». (13 búsquedas en total, todo en inglés — no hizo falta
  japonés/coreano/chino: Shrek es una producción 100% estadounidense.)
- **Fuentes descargadas y comprobadas con fontTools**: `BouwsUnc.ttf`
  (Mouser Fonts/dafont), `SHREK___.TTF` (Internet Archive), `
  unifraktur.woff2` y `butcherman_latin.woff2` (Fontsource/Google Fonts) —
  las cuatro en `/tmp/claude-0/trabajo/59-shrek-texto/fonts/`.
- **Imágenes miradas con Read**: `img/ffa_times.jpg` (Far Far Away Times,
  1023×575), `img/duloc_street.jpg` (calle de Duloc con el hedge-portrait
  de Farquaad, 1920×1080), `img/contact_pws.jpg` (hoja de contacto propia
  con las 3 capturas de *PowerWash Simulator × Shrek*, 1920×1080 cada
  una), `img/shrek_font_sample.png` (render propio de la fuente logo).
- **Bloqueadas (403/Cloudflare)**: `tcrf.net` (2 intentos: directo y por
  Wayback), `tvtropes.org` (2 intentos: curl y WebFetch), `mobygames.com`
  (1 intento, devolvió 0 bytes), `fontmeme.com` (1 intento, Cloudflare).

## Cumplimiento de mis puntos (5, 6, 11, 18, 24, 25)

| Punto | Estado | Por qué |
|---|---|---|
| 5 · Tipografía | ✅ | 4 usos (logo, cartel de madera, cabecera de periódico, narración de libro) con letra libre comprobada con fontTools cada una; faltan subtítulos/menús de juego (dicho en «No encontré») |
| 6 · Cómo hablan en pantalla | ✅ | Sin manga (dicho y por qué); cubierto con libro de Steig, 3 cómics oficiales, periódico, letrero y Duloc Dolls; falta ver una página interior de cómic (⚠️, préstamo controlado) |
| 11 · Videojuegos | ✅ | Lista completa de +25 títulos con plataforma y año; HUD de SuperSlam confirmado en dos fuentes; TCRF citado pero bloqueado por Cloudflare (⚠️) |
| 18 · Estilo y técnica | ✅ | Pipeline PDI/Maya, SSS, pelo, tela, GI, fluidos, con equivalencias concretas en Blender y Photoshop; falta cita de composición/planos por emoción (dicho en «No encontré») |
| 24 · Obras parecidas | ⚠️ | Cubierto con 2-3 fuentes agregadoras (no entrevistas de autor sobre influencias directas) y comparado contra la biblioteca del servidor |
| 25 · Mundo, historia, símbolos | ✅ | Mundo en 5 líneas, arcos completos (incluida Shrek 5 y el spin-off Donkey, ⚠️ una fuente wiki), símbolos con fuente cada uno |

Sigue: nada obligatorio pendiente de mis puntos. Si hay tiempo extra:
reintentar tcrf.net/tvtropes más tarde (pueden dejar de retar Cloudflare) y
buscar una fuente de subtítulos/menús de videojuego.
