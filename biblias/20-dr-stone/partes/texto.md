# Parte · TEXTO, JUEGOS Y TÉCNICA · Dr. Stone (20-dr-stone)

Rol: puntos **5** (tipografía), **6** (cuadros de diálogo), **11** (videojuegos),
**18** (estilo de dibujo y cómo replicarlo), **24** (obras parecidas) y **25**
(el mundo, la historia y sus símbolos) de `ENCARGO.md`.

**Contexto**: `biblia.md` ya existe (de antes del 24-sep-2026, red cerrada,
sin hojas de contacto). Tiene los puntos 5, 6 y 11 escritos pero con ⚠️
sueltos; **los puntos 18, 24 y 25 no existen en la biblia** (son los que
añadió la actualización del encargo). Este archivo: confirma/profundiza 5, 6,
11 y aporta 18, 24, 25 enteros para que el redactor los añada. No toco
`biblia.md`. Uso `datos-texto.md` (ya leído, no repito esas consultas de
AniList/Steam) y comparto hallazgos con lo que ya midió el investigador de
imagen en `/tmp/claude-0/trabajo/20-dr-stone-imagen/*/estilo.json` (lo cito
como tal).

---

## Hallazgos

### Punto 5 · Tipografía (confirma y amplía lo que ya hay en biblia §6)

- **Vi el cartel de título del episodio 1 en grande** (1920×1080, wiki de
  Fandom: [Episode 1 Title.png](https://static.wikia.nocookie.net/dr-stone/images/b/b8/Episode_1_Title.png/revision/latest?cb=20190705175621)).
  Esto resuelve el ⚠️ «el diseño del rótulo en pantalla» de la biblia vieja.
  Lo que se ve, medido con `herramientas/estilo.py`:
  - El logo **«Dr.STONE»** y el subtítulo japonés «ドクターストーン» van en
    **piedra fundida naranja-roja**: `#F29C0F` (naranja) y `#E74010`
    (rojo-naranja) con grietas negras/gris oscuro (`#272523`) marcando cada
    letra como una placa de roca partida, sobre fondo negro puro ✅ (medido
    en la imagen oficial de la wiki).
  - El **número y el título del episodio** («01.STONE WORLD»), debajo, usan
    **la misma familia de letra pero en piedra GRIS**: `#A49284` claro y
    `#C6C2BE` casi blanco, sin el naranja del logo ✅. Es un dato nuevo: la
    biblia vieja no distinguía logo (naranja) de título de episodio (gris).
  - Dos **líneas horizontales con brillo naranja** flanquean el subtítulo
    japonés, como un destello de lava ✅.
- **Letra base del logo**: sigue sin haber una fuente comercial confirmada
  (✅ ya en la biblia con madegooddesigns + fontinlogo + dos hilos de
  dafont). Sumo una tercera pista de comunidad: en un hilo de befonts,
  2 votantes proponen **Norwester** (Sam Parrett) como la más parecida al
  estilo «sans grueso agrietado» ⚠️ (comunidad, no oficial)
  ([befonts, hilo "Time To Lose Our Ship"](https://befonts.com/forum/time-to-lose-our-ship)).
  No cambia la recomendación ya dada (Anton/Bungee/Ewert + textura de
  piedra): Norwester es una alternativa más, con licencia gratis para uso
  personal (comprobar para uso comercial antes de usarla).
- **Letras libres ya comprobadas por el investigador anterior con
  fontTools** (Anton, Rubik Dirt, Bungee, Kalam, Caveat, Patrick Hand, Cabin
  Sketch, Oswald, Bangers, Yusei Magic, Klee One, Dela Gothic One, Ewert):
  las reviso contra el catálogo de Google Fonts y **siguen activas y con
  licencia OFL** ✅ (comprobado en [fonts.google.com](https://fonts.google.com/),
  24-sep-2026). No hace falta repetir el análisis de glifos, ya está hecho
  y es correcto.

### Punto 6 · Cómo hablan y piensan en pantalla (confirma y amplía biblia §7)

- **Resuelvo el ⚠️ «de su caja de diálogo no encontré capturas»**: la
  caja de diálogo del videojuego oficial *Dr.STONE Battle Craft* SÍ se ve en
  las capturas de su ficha de Google Play (antes de cerrar el 1-sep-2026).
  La miré en grande. Es un **cuadro con esquinas en bisel (octogonal, no
  redondo)**, borde fino **cian/turquesa claro** y relleno **azul-verde
  oscuro semitransparente** (para leer sobre el fondo del juego). El nombre
  del que habla («Senku») va en una **etiqueta más pequeña, pegada arriba a
  la izquierda del cuadro grande**, unida por una línea diagonal con un
  pequeño círculo (como un remache). El texto es **blanco con borde oscuro**,
  sin rayas ni comillas. Abajo a la derecha suele ir un icono para avanzar.
  Medido con `estilo.py` sobre la captura oficial: relleno `#21403D` /
  `#2F5D5D`, borde `#7EB6DF` / `#C7DCEC` ✅ (captura oficial, con crédito
  «©米スタジオ・Boichi／集英社・Dr.STONE製作委員会 ©Poppin Games Japan Co., Ltd.»
  visible en la propia imagen de la ficha)
  ([Google Play, ficha archivada](https://play.google.com/store/apps/details?id=com.poppingames.dsbc&hl=en_US)).
  Es **el mismo lenguaje visual** que el «test de Gen» y el «¡…, listo!» de
  la serie: cajas con esquinas cortadas, nunca óvalos.
- **Jerga invertida de Gen (倒語) en el doblaje latino**: repetí la
  búsqueda en el wikitext de Doblaje Wiki (`action=parse&prop=wikitext`,
  página «Dr. Stone») y no aparece ninguna adaptación de «ジーマー», «バイヤー»,
  «ドイヒー», «ゴイスー», «リームー» a una jerga en español ❌ **no lo encontré**
  (la página no tiene sección de curiosidades ni menciona el juego de
  palabras). Sigue como ⚠️ de la biblia vieja: no lo inventes, pide el clip
  doblado de 1×23 (00:19:15) si hace falta confirmarlo con oído.
- **Mecha Senku**, confirmado con una segunda fuente (Fandom ya daba una):
  aparece también citado como mascota física en eventos («AnimeJapan Mecha
  Senku mascot», OTAQUEST) ✅ ya estaba en la biblia con una fuente, ahora
  con la segunda (la propia entrada de la wiki, personajes menores) ✅
  confirmado con dos fuentes.

### Punto 11 · Videojuegos de la franquicia (amplía biblia §13)

- **Dr.STONE Battle Craft — cuadro de diálogo y capturas reales** (ver
  punto 6 arriba: mismo hallazgo, cubre los dos puntos). Además:
  - **Portada/arte de personaje del juego** (el «Intro Card» de Senku,
    1000×1000, con licencia visible del propio juego): Senku sonriendo,
    dedos chasqueando sobre un tubo de ensayo con «E=mc²» escrito en su
    venda, reacción química efervescente saliendo de un vaso de precipitados
    ✅ (vista en grande,
    [wiki, ficha del archivo](https://dr-stone.fandom.com/wiki/File:Battle_Craft_Intro_Card_Senku.png)).
    Sirve como referencia de **pose de acción con objeto de laboratorio**
    para el concepto A de la lámina.
  - **Pantalla de victoria**: iconos chibi de los 6 personajes en fila con
    barra de vida, marcador «Victory» en rojo con contorno blanco, cronómetro
    arriba a la derecha, botón «Next» en verde ✅ (misma ficha archivada).
  - **HUD de recursos**: un **diamante/gema azul** con el número de recurso
    y su nivel arriba a la izquierda («Resource Lv1 150»), iconos cuadrados
    de personajes abajo con nivel en una banderita amarilla y un botón
    «Leader» resaltado en dorado ✅.
- **Cierre confirmado con dos fuentes**: *Battle Craft* cerró el
  1-sep-2026 10:00 JST (biblia vieja lo tenía con dos fuentes de prensa
  japonesa; sumo que a fecha de esta revisión (24-sep-2026) **no hay
  ningún juego sucesor anunciado** ⚠️ (una búsqueda, sin resultado: «Dr.
  Stone 新作 ゲーム 2026 後継»).
- **Jump Force / Jump Assemble**: confirmo con una fuente adicional
  (CBR, cobertura del roster completo de *Jump Force*) que Dr. Stone **no
  estaba** en el reparto original y sólo aparece en propuestas de fans para
  una hipotética secuela ✅ (dos fuentes: la búsqueda anterior + CBR roster).
- **The Cutting Room Floor**: repetí la búsqueda (`site:tcrf.net Dr.
  Stone`) y no hay página del juego ❌ **no lo encontré**, es coherente con
  que *Battle Craft* es un juego móvil japonés sin beta filtrada conocida.

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo (NUEVO, no estaba en la biblia)

**Del manga (Boichi, dibujante)**

- Boichi **estudió Física** en la universidad «como preparación para dibujar
  obras de ciencia ficción», y después un posgrado centrado en tecnología de
  imagen ✅ (dos fuentes:
  [perfil de Boichi en Fandom](https://dr-stone.fandom.com/wiki/Boichi),
  recogido también por reseñas del manga). Explica el nivel de detalle
  técnico de las máquinas.
- **No copia fotos literalmente**: en su propia cuenta de X explica sobre el
  calculador de parametrones de Senku: «There was nothing I could simply
  copy, and even if there had been, drawing it exactly the same wouldn't
  make it "Senku's invention." It had to reflect the Stone World setting,
  and it also needed originality[…] The photo is a reference image of
  parametrons I found online» ✅ fuente primaria
  ([Boichi, X/Twitter](https://x.com/Boichi_Bo1/status/2051986720875282549)).
  Para el reboot *Byakuya* llegó a reunir **~1500 fotos de referencia** ⚠️
  (una fuente, resumen de entrevista).
- **Su proceso de tinta es casi sin corrección**: un vídeo suyo trabajando
  se hizo viral en Japón porque **apenas usa el borrador ni «deshacer»**,
  dibuja con un solo tamaño de pincel, sin capas ni selecciones, en papel
  digital, con un control de precisión que sorprendió a otros mangakas ✅
  ([Togetter, hilo con el vídeo](https://togetter.com/li/1615629)). Tiene
  **3 ayudantes, todos mangakas**, y tarda **1 a 1.5 horas por página** ⚠️
  (una fuente,
  [goodcomicsforkids.slj.com, AnimeNYC 2019](https://goodcomicsforkids.slj.com/2019/12/20/animenyc-a-peek-behind-the-scenes-of-dr-stone/)).
- **Simbolismo en el diseño**: Boichi dice sobre la ropa de Senku «Those
  pockets represent what Senku is thinking»: el número de bolsillos sube
  cuando el personaje está en peligro y baja cuando está a salvo ✅ (misma
  fuente, cita directa).
- **Referencia de cine real**: usó *Quest for Fire* (1981) como referencia
  de puesta en escena prehistórica, con el asesor científico de esa
  película, Desmond Morris, como influencia indirecta ⚠️ (una fuente).

**Del anime (TMS Entertainment)**

- **Plantilla de color deliberada sobre un manga en blanco y negro**: el
  director de la 4.ª temporada, **Shuhei Matsushita**, explica que como «la
  ciencia no tiene mentira» investigaron a fondo el color real de la
  vegetación, los ríos y las piedras, **incluida la variación de color de
  una llama según su temperatura**, y que al llegar a América (temporada 4)
  **rediseñaron los fondos enteros** por la diferencia de humedad y
  atmósfera con Japón, para que **el cambio de continente se note sin
  explicarlo con palabras** ✅
  ([jmagazine.myjcom.jp, entrevista de cierre](https://jmagazine.myjcom.jp/category/anime/post001463/)).
- **Ficha técnica de estilo, confirmada en dos fuentes** (AniList vía
  `datos-texto.md` + la ficha oficial de TMS Entertainment,
  [tms-e.co.jp](https://www.tms-e.co.jp/alltitles/2010s/762101.html)):
  director de arte **Shunjiro Yoshihara** (吉原俊一郎; AniList lo listaba
  para otro tramo como Tomoyuki Aoki, así que hubo más de un director de
  arte según la temporada ⚠️ eso sí, sin confirmar cuál va con cuál);
  diseño de color **Fusako Nakao** (中尾総子) ✅; director de fotografía
  **Takeshi Kuzuyama** (葛山剛士 — el mismo kanji que «Takeshi
  Katsurayama» de AniList: es la misma persona, sólo cambia la
  romanización) ✅; animador principal **Hiroyuki Horiuchi** ✅; estudio
  interno **TMS8PAN** ✅.
- Un dato suelto sin confirmar del todo: la forma del personaje **Whiteman**
  (Científico Futuro/*Science Future*) se resolvió con **3DCG**, para dar
  una sensación ondulante e inquietante tras varias pruebas ⚠️ (una fuente,
  resumen de foro japonés; no pude ver el making of original).

**Estilo medido (con `estilo.py`, sobre las muestras oficiales que ya bajó
el investigador de imagen a `/tmp/claude-0/trabajo/20-dr-stone-imagen/muestras/`,
dato compartido en el contenedor, cito el archivo exacto)**:

| Tipo de imagen | Sombreado | Línea | Color de línea |
|---|---|---|---|
| Retratos/settei de personaje (Senku, Chrome, Gen, Kohaku, Suika) | **plano (cel)** 64-84% zonas planas | poca a normal | **marrón/gris oscuro** (`#5A4A45` a `#8C7764`), casi nunca negro puro |
| Fondos y escenas de acción (`senku_chrome_lab.png`, `group_paradise.png`) | **degradado / pintado**, 54-65% degradado | poca línea | tonos cálidos de ambiente (`#B9A091`, `#63564A`) |
| Escena dramática (`chrome_determination.png`) | **mixto** 40/41 | línea normal | `#6E564E` |

**Lectura para replicarlo**: los **personajes van en cel-shading plano**
(2-3 tonos, sin degradado salvo alguna sombra suave) con **contorno de color,
no negro puro** (marrón o gris oscuro según la piel/pelo); los **fondos y
las luces de escena sí se pintan con degradado**, como pintura digital. Es
el patrón clásico anime: personaje "cell" + fondo pintado, y aquí se
confirma con números, no de memoria.

**Cómo replicarlo en Photoshop**
1. **Línea**: pincel de tinta con opacidad 100% pero **grosor variable
   (pluma/tableta)**, en un color por zona (marrón oscuro `#5A4A45` en piel,
   gris `#3E3E3E` en ropa oscura), nunca negro `#000000` puro salvo en las
   sombras muy cerradas del pelo.
2. **Color base**: capa «Multiplicar» plana, sin degradado, 2 tonos por
   zona (luz y una sombra dura con el *Lazo poligonal*, no el pincel suave).
3. **Fondos**: capa aparte, pintada con pincel de mezcla (degradados
   `#245E6B`→`#DED299` tipo atardecer, ver la paleta medida arriba),
   desenfoque de lente ligero para separar del personaje.
4. **Filtro final**: grano fino (Ruido → Monocromático, 2-3%) y un ajuste de
   **Curvas** que sube el naranja/amarillo y baja el azul en las escenas de
   laboratorio con fuego, replicando el look cálido que describe Matsushita.
5. **Título/logo**: capa de textura de piedra + estilo de capa «Bisel y
   relieve» alto, más grietas pintadas a mano en un canal alfa (ver §5).

**Cómo replicarlo en Blender**
1. **Personajes**: *toon shader* de 2-3 bandas (nodo `Shader to RGB` +
   `ColorRamp` con 2 escalones) en vez de degradado PBR; el contorno con
   **Solidify invertido** (más fiable que Freestyle para exportar a
   Photoshop) en el mismo marrón/gris medido arriba, no negro.
2. **Objetos de laboratorio** (tubos de ensayo, matraces): vidrio con
   *Principled BSDF* de transmisión alta + un poco de rugosidad (no vidrio
   perfecto: en la serie el vidrio está soplado a mano, con burbujas).
3. **Luz**: una luz clave cálida (horno/fuego, ~2800K) + un relleno frío
   (luna o nieve, ~7000K), igual que el contraste que ya está en la paleta
   medida de `senku_chrome_lab.png` (`#63564A` cálido / azules del cielo).
4. **Encuadre**: la cámara de la ficha «Intro Card» de *Battle Craft* (ver
   §11) es un **contrapicado cerrado**, personaje llenando el cuadro,
   objeto de ciencia en primer plano recortando el borde inferior: sirve de
   plantilla de composición para Blender + render.
5. **Modelos y rigs libres**: no los busco aquí para no duplicar: el
   investigador de imagen ya los dejó con licencia comprobada por la API
   de Sketchfab en `partes/imagen.md` §3.1 (Senku en varios modelos CC BY,
   uno ya en formato Blender 2.8; vidrio de laboratorio, radio de
   válvulas, tubo de vacío). Para el 18, úsalos como base del *rig* y pon
   el *toon shader* de arriba encima.

### Punto 24 · Obras parecidas (NUEVO, no estaba en la biblia)

- **Recomendadas por la propia comunidad de AniList** (ya en
  `datos-texto.md`, no repito la consulta): *Ascendance of a Bookworm*,
  *That Time I Got Reincarnated as a Slime*, *Astra Lost in Space*,
  *Cells at Work!*, *Food Wars!*, *7SEEDS* ✅.
- **Coinciden con webs de recomendación independientes** (segunda fuente
  para varias de las de arriba): *7SEEDS* y *Uninhabited Planet Survive!*
  por el género de supervivencia en grupo tras una catástrofe; *Made in
  Abyss* por el tono de aventura y exploración con un objetivo tecnológico
  claro ✅ ([Anime Corner](https://animecorner.me/five-anime-to-watch-if-you-like-dr-stone/),
  [Dualshockers](https://www.dualshockers.com/best-anime-like-dr-stone/)).
- **Comparación directa punto por punto**, *Dr. Stone* contra *Cells at
  Work!*, como las dos referencias del «anime educativo» (ciencia dura
  explicada con personajes) ✅ ([CBR](https://www.cbr.com/dr-stone-vs-cells-at-work-best-educational-anime/)).
- **Influencias que reconoce el propio guionista Riichiro Inagaki**: la
  personalidad de Senku bebe de **Agon Kongo**, el genio arrogante y
  manipulador de su manga anterior *Eyeshield 21* (mismo Inagaki) ✅ (dos
  fuentes: Wikipedia + reseñas del manga que citan la entrevista); y
  *Video Girl Ai* (Masakazu Katsura) como influencia declarada en el tono
  de la historia ⚠️ (una fuente, resumen de reseña, sin la cita textual
  original de la entrevista).
- **Género y tropo reconocido por la crítica** (TV Tropes): Senku encarna
  **"For Science!"** como motor de personaje, y la pareja con Taiju es un
  caso de manual de **"Brains and Brawn"** ✅ ([TV Tropes, Characters in Dr.
  STONE](https://tvtropes.org/pmwiki/pmwiki.php/Characters/DrStone)). Útil
  como «palabra clave» de género para explicar el tono del canal si hace
  falta un texto corto.
- **Qué otra lámina del servidor se le parece**: revisé los 130 encargos
  (`encargos/*.md`) buscando «hardware», «laboratorio», «ciencia»,
  «construc», «invent», «fabrica». **Ningún otro canal usa #hardware** y
  **ningún otro encargo ya con biblia comparte el tema «laboratorio /
  invención»** ✅ (búsqueda hecha sobre los 130 archivos de `encargos/`).
  El único con tecnología parecida sin biblia todavía es **114-cyberpunk-2077-juego**
  («interfaz, anuncios, neones» — estética muy distinta, cyberpunk urbano
  vs. artesanal-piedra) y **27-cyberpunk-edgerunners** (ya con biblia, mismo
  contraste de estilo). No hay riesgo de repetir concepto de lámina.

### Punto 25 · El mundo, la historia y sus símbolos (NUEVO, no estaba en la biblia)

**Las reglas del mundo en cinco líneas**

1. Un destello cegador petrifica a toda la humanidad (y a las golondrinas)
   de golpe, en el año que sería 2019 ✅.
2. La piedra **no envejece ni muere**: quien revive lo hace con el mismo
   cuerpo y la misma mente de hace 3.700 años ✅.
3. Sólo un líquido concreto (**«fluido de revivificación»**, ácido nítrico +
   alcohol sobre la piedra) rompe la petrificación, persona a persona ✅.
4. La naturaleza sí siguió su curso: **bosques, ríos y animales llevan
   3.700 años sin humanos** — de ahí la premisa de «reconstruir la
   civilización desde cero» ✅.
5. Hay una segunda arma de petrificación **deliberada y selectiva** (el
   arma de Ibara/Why-Man): no es el mismo fenómeno que la petrificación
   global, y es la gran pregunta de la serie («¿quién y por qué?») ✅.
   (Fuentes: [Fandom, Stone World](https://dr-stone.fandom.com/wiki/Stone_World),
   [Fandom, Petrification](https://dr-stone.fandom.com/wiki/Petrification),
   confirmado en dos fuentes.)

**La historia por sagas** (nombres oficiales de la propia wiki, que organiza
los capítulos así; los cito con su rango de capítulos) ✅ dos fuentes
(wikitext de [Fandom, Story Arcs](https://dr-stone.fandom.com/wiki/Story_Arcs)
+ el resumen por temporadas de Wikipedia):

| Saga | Capítulos | Qué pasa |
|---|---|---|
| **Prólogo** | 1-12 | Senku y Taiju despiertan; Senku se enfrenta a Tsukasa, que quiere revivir sólo a los jóvenes «puros» |
| **Aldea Ishigami** | 13-45 | Senku gana la confianza de la aldea, cura a la sacerdotisa Ruri y funda el **Reino de la Ciencia** junto a Chrome, Kaseki, Kohaku y Suika |
| **Guerra de las piedras** (*Stone Wars*) | 46-82 | El Reino de la Ciencia se enfrenta al Imperio de Tsukasa (Imperio de la Fuerza) por el control del mundo |
| **Origen de la petrificación** | 83-212 (incl. Isla del Tesoro, América) | Reino de la Ciencia e Imperio, ya aliados, construyen un barco (el *Perseus*) para buscar el origen de la petrificación; aparecen el Reino de la Petrificación de Ibara y el continente americano |
| **De la piedra al espacio** | 213-232 (final) | Construcción del cohete, selección de astronautas, viaje a la Luna y enfrentamiento con **Why-Man**, el ser que causó la petrificación |

**Momentos clave** (ya con minuto en la biblia vieja para varios; añado los
que faltaban de contexto): la fundación del Reino de la Ciencia (cap. 15),
la Guerra de las Piedras terminando en alianza y no en conquista (cap. ~80),
la revelación de que Byakuya (padre de Senku) estaba en la Estación Espacial
Internacional durante la petrificación, y el capítulo final «Dr. STONE»
(232) cerrando con el propio Why-Man ✅.

**Emblemas y logos de grupo**

- **Bandera del Reino de la Ciencia**: un **cohete estilizado flanqueado por
  dos estrellas**, izada en la torre de radio de Isla del Tesoro cuando se
  une al Reino ✅ (texto confirmado en el wikitext de Fandom, sección
  «Stone World» → Treasure Island: «The tower bears a flag signifying it is
  now part of the Kingdom of Science»). **El diseño exacto de la bandera
  (colores, proporciones) no lo pude confirmar con una imagen oficial** ⚠️
  (Wikimedia Commons devolvió error 429 al pedirlo; las que circulan en
  DeviantArt son reconstrucciones de fans, válidas sólo como boceto de
  referencia, nunca como fuente final).
- **Imperio de Tsukasa / Imperio de la Fuerza**: no tiene bandera propia
  documentada en la wiki (a diferencia del Reino de la Ciencia) ⚠️ — es un
  dato a favor de la idea de lámina: **la única facción con emblema gráfico
  es la de Senku**, coherente con que la ciencia «se puede dibujar» y la
  fuerza bruta no.

**Objetos icónicos y vocabulario que un fan reconoce al instante**

- **Stone World** (ストーンワールド) — el mundo sin gente, tal cual, en
  inglés incluso en japonés.
- **Fluido de revivificación** (復活の秘薬, *revival fluid*) — el líquido
  que rompe la petrificación.
- **Reino de la Ciencia** (科学の王国) / **Imperio de Tsukasa (de la
  Fuerza)** — las dos facciones.
- **Perseus** — el barco. **Corn City** y **Superalloy City** — las
  ciudades nuevas del arco americano.
- **Why-Man** — el nombre (juego de palabras con «why», por qué) de quien
  causó la petrificación.
- **«100 億%» (cien mil millones por ciento)** — la muletilla de Senku para
  «totalmente seguro»; en el doblaje latino es «10 mil millones por
  ciento» (ver biblia §10, no es mi punto pero conecta directo con el
  vocabulario del mundo).
  (Fuentes: [Fandom, Kingdom of Science](https://dr-stone.fandom.com/wiki/Kingdom_of_Science),
  [Fandom, Stone World](https://dr-stone.fandom.com/wiki/Stone_World) ✅ dos
  fuentes cada término, cruzado con Wikipedia para los nombres en inglés.)

---

## Lo mejor para la lámina

1. **El cartel de título** (naranja/rojo lava + gris piedra, medido) es la
   textura de letra perfecta para el nombre del canal «Hardware»: mismo
   agrietado, colores ya en hex.
2. **El cuadro de diálogo real del videojuego** (bisel turquesa sobre fondo
   azul-verde oscuro, etiqueta de nombre en diagonal) es la prueba de que
   la franquicia SÍ tiene un lenguaje de caja de texto propio: úsalo como
   referencia directa para las etiquetas de precio del foro, no inventes un
   globo.
3. **El «Intro Card» de Senku de Battle Craft** (chasquido de dedos sobre
   un tubo de ensayo con E=mc² en la venda) es otra pose de laboratorio con
   fuente 100% oficial y con crédito legible en la propia imagen.
4. **La bandera del Reino de la Ciencia** (cohete + 2 estrellas, sin
   imagen oficial confirmada) es una idea fuerte para un sello o marca de
   agua en la lámina 2, pero hay que dibujarla de cero, no calcarla de fan
   art.
5. Para el texto en la voz de Senku sobre ciencia real: la cita de Boichi
   sobre los bolsillos de Senku («representan lo que está pensando»)
   sirve para justificar por qué el personaje en la lámina debe llevar
   **herramientas visibles encima**, no las manos vacías.

## No encontré

- ⚠️ El **diseño exacto de la bandera del Reino de la Ciencia** en una
  imagen oficial (Wikimedia Commons dio 429; sólo hay reconstrucciones de
  fans). Búsquedas: «Kingdom of Science flag emblem meaning», Wikimedia
  Commons API (429, sin reintentar más de dos veces).
- ⚠️ **Jerga invertida de Gen adaptada al doblaje latino**: wikitext de
  Doblaje Wiki sin esa información. No lo inventes.
- ⚠️ **Sucesor de Battle Craft** tras su cierre (1-sep-2026): una búsqueda
  en japonés sin resultado.
- ⚠️ **Making of original** de la escena 3DCG de Whiteman (sólo un resumen
  de foro japonés de segunda mano).
- ⚠️ **Filtros de posproducción concretos** (grano de película, viñeta,
  aberración cromática, *bloom*): no encontré ninguna fuente que los
  documente por su nombre para este anime. Lo que sí está medido es el
  patrón de sombreado (plano en personajes, degradado en fondos, arriba);
  no inventé un filtro que no pude confirmar. Búsqueda: «"Dr. Stone" anime
  chromatic aberration OR film grain OR bloom lighting effect visual
  filter» (EN), sin resultado específico.
- ⚠️ **Entrevista original de Inagaki** citando *Video Girl Ai* como
  influencia (sólo aparece resumida en una reseña, no la cita directa).
- ⚠️ **Qué director de arte va con qué temporada**: confirmé con la ficha
  oficial de TMS que el director de fotografía es una sola persona
  (Takeshi Kuzuyama/葛山剛士, sólo cambiaba la romanización entre
  fuentes), pero el director de arte sí tiene **dos nombres distintos**
  (Tomoyuki Aoki en AniList, Shunjiro Yoshihara en la ficha de TMS) y
  ninguna fuente dice cuál dirigió qué temporada.

## Bitácora (segunda pasada, texto/juegos/técnica)

Búsquedas nuevas de este investigador, con idioma:

- ES: (ninguna búsqueda específica; los términos de la serie son en inglés
  o japonés incluso en fuentes en español).
- EN: "Boichi Dr. Stone art style interview drawing technique 3D
  machinery", "Dr. Stone anime TMS Entertainment animation technique
  interview director Shinya Iino", "\"Dr. Stone\" Iino director interview
  science animation hand-drawn background art color palette", "\"Dr. Stone\"
  animenewsnetwork Iino Kido scriptwriters interview 2026 looking back
  quote", "Boichi interview 3D reference models machines Dr. Stone Blender
  Clip Studio Paint drawing process", "\"Dr. Stone\" anime toon shader OR
  cel shading OR 3DCG Whiteman staff production", "Riichiro Inagaki Dr.
  Stone influences inspired by manga survival series comparison", "Dr.
  Stone world rules symbols petrification kingdom of science flag emblem
  meaning", "Dr. STONE Battle Craft gameplay screenshot dialogue box menu
  interface", "\"Dr. Stone\" episode title card screenshot font style stone
  carved letters", "\"Dr. Stone\" review compared to Cells at Work OR Made
  in Abyss OR Nausicaa science survival anime similar", "TV Tropes Dr Stone
  tropes YMMV comparisons similar works", "site:tcrf.net Dr. Stone",
  "\"Dr. Stone\" Jump Assemble OR Jump Force character roster crossover",
  "\"Dr. Stone\" anime chromatic aberration OR film grain OR bloom
  lighting effect visual filter".
- JA: "ボイチ Dr.STONE 作画 CG 3D 使って インタビュー", "ドクターストーン アニメ
  背景美術 セルルック 撮影 グレーディング インタビュー", "Dr. Stone 新作 ゲーム
  2026 後継 スマホ".
- Fuentes consultadas (además de las citadas arriba con enlace): la ficha
  oficial de TMS Entertainment (tms-e.co.jp/alltitles/2010s/762101.html),
  AniList
  (vía `datos-texto.md`, no repetido), API de Fandom `dr-stone.fandom.com`
  (wikitext de Kingdom of Science, Stone World, Story Arcs; imageinfo de
  `Battle Craft Intro Card Senku.png`, `Episode 1 Title.png`, categorías
  `Battle Craft Assets` y `Title Card Images`), API de Doblaje Wiki
  (wikitext de «Dr. Stone», sólo para buscar la jerga de Gen, no repetí el
  reparto que es del investigador de voz), Google Play (ficha archivada de
  Battle Craft, capturas), tcrf.net (bloqueado por Cloudflare, confirmado
  por búsqueda que no hay página), web.archive.org (falló por conexión,
  dos intentos, no insistí más), Crunchyroll News (dos URLs, ambas
  renderizadas por JavaScript, sin contenido accesible ni por WebFetch ni
  por curl).
- Herramientas usadas: `herramientas/estilo.py` sobre `ep1title.jpg`
  (cartel de título), sobre `dialogbox_hi.png` (recorte del cuadro de
  diálogo del juego) y reutilizando los `estilo.json` ya generados por el
  investigador de imagen (`/tmp/claude-0/trabajo/20-dr-stone-imagen/estilo{1..5}/`).
