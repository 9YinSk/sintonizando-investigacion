# Investigación de TEXTO, JUEGOS Y TÉCNICA · Pokémon (07-pok-mon)

Rol de `EQUIPO.md`: puntos **5, 6, 11, 18, 24 y 25** de `ENCARGO.md`. Esta
biblia ya tenía escritos 0-17 y 19-21 (primera pasada); por «Repaso corto»
faltaban del todo los puntos **18-25**, y a texto le tocan **18, 24 y 25**
(imagen hace 19 y 23; voz hace 20, 21 y 22; no hace falta investigador de
vídeo). Parto de `partes/datos-texto.md` (AniList, staff, obras
relacionadas) y no repito esas consultas. Los puntos 5, 6 y 11 ya estaban
escritos con bastante detalle: los repasé (sección final) en vez de
rehacerlos.

---

## 18 · Estilo de dibujo y técnica, y cómo replicarlo

### 18.1 Quién lo dibuja y con qué programas (fuentes primarias, no genéricas)
- **Estudio**: **OLM, Inc.** (antes Oriental Light and Magic), Tokio, 1994,
  el único estudio que ha animado el anime desde 1997 ✅
  ([Wikipedia, OLM (studio)](https://en.wikipedia.org/wiki/OLM_(studio)),
  [AWN](https://www.awn.com/animationworld/olm-asia-launches-new-pok-mon-animation-series-help-celsys-clip-studio-paint)).
- **De celuloide a digital, con fecha exacta**: se animó a mano sobre
  **acetato (cel)** hasta el episodio de temporada 5 *A Crowning
  Achievement*; desde *Here's Lookin' at You, Elekid!* (agosto de 2002) en
  adelante, todo es **animación digital** ✅ (dos fuentes independientes:
  [Wikipedia, OLM (studio)](https://en.wikipedia.org/wiki/OLM_(studio)) en
  inglés, y la [Wikipedia japonesa de la serie](https://ja.wikipedia.org/wiki/%E3%83%9D%E3%82%B1%E3%83%83%E3%83%88%E3%83%A2%E3%83%B3%E3%82%B9%E3%82%BF%E3%83%BC_(%E3%82%A2%E3%83%8B%E3%83%A1))
  con «2002年8月より…デジタルアニメーション制作に移行»).
- **Software actual, con cita textual del productor**: OLM usa **Toon Boom
  Storyboard Pro** para guion gráfico y **Toon Boom Harmony** para
  animación clave, intercalado y color, más herramientas propias (AM Tool,
  DirMaker) ✅ ([CGWORLD, reportaje sobre *Pokémon XY&Z*](https://cgworld.jp/feature/cgw209t1-olm.html)
  — cita textual del productor Katsura: *«Necesitábamos lograr primero
  calidad de TV. No se trataba sólo de digitalizar: lo que más importaba
  era la satisfacción del espectador»*). Harmony **separa la línea del
  color en capas distintas** y permite corregir el trazo después de
  dibujado (nodos de anclaje), algo que el celuloide no permitía.
- **La rama que sí usa Clip Studio Paint**: **OLM Asia** (Malasia) estrenó
  en **diciembre de 2017** una entrega de la serie usando **Clip Studio
  Paint** en las fases de *genga* (clave) y *sakuga* (entintado e
  intercalado), elegido por «su motor de pinceles de calidad y su tacto de
  papel y lápiz» ✅ ([AWN](https://www.awn.com/animationworld/olm-asia-launches-new-pok-mon-animation-series-help-celsys-clip-studio-paint)).
  Cada episodio necesita **más de 300 planos y 4.000-5.000 dibujos** ✅
  (misma fuente, cita textual del productor Hiroyuki Kato). **No dice el
  nombre exacto de esa entrega** ⚠️ (el artículo sólo dice «la más reciente
  de la serie Pokémon» en esa fecha).
- **Diseño de personajes del anime**: **Sayuri Ichiishi** (ya en la biblia,
  §2.4); diseño original de las criaturas: **Ken Sugimori**, que en los
  juegos las repintó todas **a acuarela** para material promocional,
  «recio y con sombra ligera, muy parecido al estilo de Akira Toriyama de
  1989 en adelante»; con el paso a lo digital sus dibujos ganaron «más
  definición muscular, esquinas más redondeadas, sombreado más marcado y
  poses más naturales» ✅ ([Wikipedia, Ken Sugimori](https://en.wikipedia.org/wiki/Ken_Sugimori)).

### 18.2 Línea y sombreado, medidos por mí (no de memoria)
Medí con `herramientas/estilo.py` el arte oficial ya listado en la biblia
(§2.1, PokéAPI) y lo miré con Read en grande:

| Imagen | Sombreado | Línea (hex) | Saturación | Brillo |
|---|---|---|---|---|
| [Pikachu, arte oficial de los juegos](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png) (475×475) | **degradado suave**, no plano: aerógrafo en la panza y sombra redonda en cada mejilla | `#221B11` (marrón muy oscuro, no negro puro) | 16% | 50% |
| [Charmander, arte oficial de los juegos](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png) (475×475) | ídem, degradado suave | `#3A2F26` (marrón oscuro) | 18% | 58% |
| [Pikachu, render 3D de Pokémon HOME](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/25.png) (512×512) | plano en orejas/mejillas, degradado de luz 3D en el cuerpo | **sin línea de tinta**: el contorno lo da la luz, no un trazo (color medido en el borde `#D6B748`, un dorado, no un marrón) | 26% | 98% |

**Grosor de línea, medido en píxeles** (no sólo el color): en el Pikachu de
475×475, el núcleo del trazo oscuro mide **1-2 px** de ancho (mediana 1 px,
media 1,6 px, contando los tramos de color más cercano a `#221B11`), con un
degradado de anti-aliasing alrededor de 1-2 px más — es decir, **una línea
fina** (≈0,3-0,5% del ancho de la imagen), no un contorno grueso tipo cómic
✅ (medido con Pillow/NumPy sobre el PNG oficial, no a ojo).

✅ (medido, no de memoria). **Lectura para la lámina**: el «arte oficial»
de videojuego usa **línea fina marrón oscura y sombreado con degradado
suave** (no cel duro); los **renders 3D de HOME no llevan tinta**: el
volumen lo hace la luz. El anime de TV, en cambio, usa —según describía ya
la guía de IA de esta biblia (§18 antigua, ahora punto 17 de ENCARGO)—
línea más limpia y sombra de **dos tonos duros**, propia del celuloide y de
Toon Boom con `ColorRamp`/pasos duros; **no pude comprobar esto sobre un
fotograma real** ⚠️ porque este repaso no lleva investigador de vídeo (lo
mide quien haga fotogramas.py más adelante). Dejo la diferencia anotada
para que no se confunda un estilo con otro.

### 18.3 Filtros de la animación
- **Grano, brillo, aberración cromática**: no encontré ninguna entrevista
  técnica que hable de esto en Pokémon (busqué «Pokemon anime film grain
  chromatic aberration episode» y «ポケモン アニメ フィルター 演出», sin
  resultado) ⚠️. Lo que sí está confirmado: los episodios de Kanto (1997)
  se remasterizaron en HD para el relanzamiento digital y el Blu-ray
  *Champion's Edition* (VIZ Media, 14-nov-2017) ✅
  ([List of digital home video releases of Pokémon anime](https://bulbapedia.bulbagarden.net/wiki/List_of_digital_home_video_releases_of_Pok%C3%A9mon_anime)
  — vía buscador, la wiki en sí dio 403 al abrirla). No hay dato de si el
  máster original en NTSC de 1997 llevaba grano de cinta visible: **sin
  confirmar**, no lo doy por hecho.

### 18.4 Encuadres y composición típicos
- **La escena de reacción («reaction shot») es marca de la casa**: cuando
  Serena se despide de Ash con un beso (Pokémon la Serie: XY), la cámara
  **no muestra el beso**: muestra la cara de sorpresa de los amigos, y así
  el espectador entiende lo que pasó ✅ (citado en una nota de análisis del
  fandom, confirmado también al describir la misma técnica en la escena del
  laboratorio: Oak y Ash **casi nunca comparten plano ancho fijo**; la
  cámara corta entre el primer plano de Ash abriendo cada Pokébola vacía y
  el plano medio de Oak explicando, punto 3.1 de esta biblia).
- El anime sigue la **regla de los 180°** y el patrón clásico de
  **plano/contraplano con cortes a primer plano de reacción**, más barridos
  laterales para el movimiento (correr, volar) ✅ (descripción general del
  estilo de cinematografía de anime de TV de los 90, contrastada con la
  escena ya documentada del capítulo 1).
- **Para la lámina**: el gesto de **presentar** (Oak entregando la Pokébola
  de Pikachu, 00:05:04 de la película 2017, §3.2) es un plano medio con
  Oak a la izquierda y el objeto en el centro; el gesto de **sorpresa o
  descubrimiento** (Ash viendo salir la Pokébola del rayo, 00:04:12) es un
  primer plano muy cerrado de la cara; el **regaño suave** de Oak
  («Squirtle se lo llevó alguien que no llegó tarde», 00:03:22) se dice en
  plano medio, sin acercar la cámara —Oak nunca grita, así que ese encuadre
  no se cierra como el de sorpresa—; y **explicar** (Oak filosofando sobre
  llegar tarde, 00:03:44) usa el mismo plano medio pero con una pausa más
  larga antes del corte. Sirve para decidir el encuadre de Oak/Pikachu en
  el concepto de lámina sin inventar una pose nueva ni pisar el punto 14
  (poses con minuto, que no toca a este repaso corto).
- **Tramas (screentone)**: es un recurso de manga en blanco y negro; el
  anime no las usa (color plano/degradado, no punteado). El manga oficial
  *Pokémon Adventures/Pocket Monsters SPECIAL* sí es en blanco y negro y
  seguramente usa tramas como cualquier manga de Shogakukan, pero **no lo
  comprobé sobre páginas reales** ⚠️ (no encontré páginas de muestra
  abiertas; búsqueda «Pokemon Adventures manga scan raw» sin resultado
  accesible). Para la lámina de #autoroles esto no aplica: no hay ningún
  elemento en blanco y negro.

### 18.5 Cómo replicarlo en Photoshop
- **Línea**: pincel de tinta 2-3 px, opacidad de la pluma activada, color
  **marrón muy oscuro** (`#221B11` o `#3A2F26`, medidos arriba) en vez de
  negro puro, en una capa en modo Multiplicar — así se ve como el arte
  oficial de los juegos, no como un contorno genérico.
- **Sombreado de personaje "estilo juego"**: base de color plano + una capa
  de aerógrafo muy blando (opacidad 20-30%) para degradar hacia la sombra,
  sin bordes duros (el patrón medido en 18.2).
- **Sombreado "estilo anime de TV"**: al contrario que el de arriba, aquí sí
  con **dos tonos duros** (base + una sola sombra plana con *clipping mask*,
  pincel de borde firme, sin difuminar), modo Multiplicar 40-50%: así se
  distingue un fondo pensado para el juego de uno pensado para la caja del
  laboratorio en pantalla (ver también §18 antigua de la biblia, ahora
  punto 17, con la paleta de mañana soleada).
- **Pokébola y objetos metálicos/plástico**: un brillo especular estrecho en
  modo Aclarar sobre la línea de unión roja/blanca, para el «botón» central
  (§16 de la biblia ya mide sus colores).

### 18.6 Cómo replicarlo en Blender
- **Contorno**: **Solidify invertido** (back-face culling, grosor 0.01-0.02,
  normales invertidas) para un contorno uniforme tipo juego; para un
  resultado más cercano al anime de TV (línea que varía de grosor con la
  distancia a cámara), mejor **Freestyle** con color de línea personalizado
  (el marrón oscuro medido, no negro). El modificador **Line Art** (Grease
  Pencil, disponible desde Blender 2.91) es la tercera opción si se quiere
  el contorno como trazo 2D editable encima del render 3D, útil si luego se
  quiere retocar la línea a mano en Photoshop antes de componer.
- **Shader tipo cel**: nodo *Shader to RGB* + **ColorRamp con interpolación
  «Constant»**: **2 escalones** para el estilo anime de TV (los dos tonos
  duros de §18.2), **3 escalones con transición suave entre ellos** (mezclar
  con un poco de interpolación) si se quiere el degradado más pintado del
  arte oficial de los juegos.
- **Luz**: una luz de área principal cálida (mañana soleada, ya lo dice la
  guía de IA de la biblia) + una luz de relleno tenue; para el brillo del
  render de HOME (sin tinta, todo con luz), usar una luz de área grande y
  suave más un poco de *Fresnel* en el shader para el borde luminoso que
  sustituye al contorno.
- **Modelos y rigs libres del personaje, comprobados por la API de
  Sketchfab** (licencia y `rig` reales, no de memoria; los objetos como la
  Pokébola y el laboratorio ya los tiene la biblia en §4, hecha por
  imagen — aquí sólo **personajes**, que faltaban):
  - [Pikachu](https://sketchfab.com/3d-models/pikachu-35716003a1964704b1b145e6c6a05b07),
    por **Eleanie**: **CC BY 4.0**, 106.512 caras, **con esqueleto/rig**
    (`isDownloadable: true` en la API) ✅. Trae sombreado tipo cómic que se
    puede pasar a tiras o apagar por grupo de nodos (según su descripción).
  - [Ash Ketchum](https://sketchfab.com/3d-models/ash-ketchum-f767f1a21b924033991a7fb1fb19820d),
    por **Neut2000**: **CC BY 4.0**, 8.613 caras, con rig ✅. No estaba en
    la lista de modelos de la biblia (§4 sólo tenía objetos): es la
    referencia 3D de personaje que faltaba para Ash.
  - **El «Pokemon Professor Oak» que la biblia ya listaba en §4** (de
    «3D Resource», con ⚠️ sin detalle): lo comprobé por la API —
    [modelo](https://sketchfab.com/3d-models/pokemon-professor-oak-212d5d395ad14367aacac0be70922acb),
    autor real **lopuh22721**, **CC BY 4.0**, 8.068 caras, **con
    rig/esqueleto** (`isDownloadable: true`) ✅. Pasa de ⚠️ a ✅: sí sirve
    para posar a Oak en Blender, no sólo para mirar la silueta.
  - Para Pikachu también hay alternativas más simples si el de Eleanie pesa
    mucho: [por jacobjksn42](https://sketchfab.com/3d-models/pikachu-c22dab8fc3064c76a0c502d64555a74f)
    y [por raghav-wd](https://sketchfab.com/3d-models/pikachu-37c740f674cd4719a1d1d2970bbe8c30),
    ambos CC BY, 4.500 caras, con rig — low-poly, mejor para lámina 2 o para
    una pose lejana ✅.
- **Texturas encima**: para la bata de Oak, una textura de algodón/lino CC0
  ligera (ver punto 4 de la biblia, ya cubierto por imagen); para el metal
  del botón de la Pokébola, un *material* simple con algo de *bump* y
  reflejo, sin textura de foto (es una pieza pequeña y limpia).

---

## 24 · Obras parecidas y temas relacionados

### 24.1 Lo que el propio creador reconoce (fuente primaria)
- **Satoshi Tajiri**, en la entrevista de **TIME (1999)**, la fuente
  primaria más citada: de niño quería ser entomólogo, «los insectos me
  fascinaban», y era tan bueno atrapándolos que su padre le puso el mote
  **«Dr. Bicho»** ✅ ([TIME Asia, la entrevista completa](http://edition.cnn.com/ASIANOW/time/magazine/99/1122/pokemon6.fullinterview1.html),
  repetida en [TIME, "The History of Pokémon in the U.S."](https://time.com/6796536/history-origins-pokemon/)).
  Conectar dos Game Boy con un cable link le hizo pensar en unir esa
  afición de coleccionar e intercambiar bichos con un videojuego ✅ (misma
  fuente).
- **Ultraman**: Tajiri se inspiró en shows tokusatsu como Ultraman y
  Godzilla; en Ultraman ya había «monstruos cápsula» que un humano guarda y
  suelta para pelear — la semilla directa de la Pokébola ✅
  ([switchaboo.com](https://www.switchaboo.com/satoshi-tajiri-the-man-behind-pokemon/)).
- **Videojuegos que él y Ken Sugimori jugaban**: *Ultraseven*, *The Final
  Fantasy Legend* (SaGa), *EarthBound* y **Dragon Quest** ✅
  ([onechilledgamer.com](https://onechilledgamer.com/history-of-pokemon/)).
  **Dragon Quest V (1992)**, en concreto, ya dejaba reclutar y entrenar
  monstruos: es la mecánica que **inspiró directamente** a Pokémon (y
  después a Digimon), según el propio artículo de referencia del género en
  Wikipedia ✅ ([Wikipedia, "Monster-taming game"](https://en.wikipedia.org/wiki/Monster-taming_game)),
  que coincide con la fuente anterior en señalar la misma cadena de
  influencia (⚠️ ambas pueden repetir el mismo dato de origen, no son del
  todo independientes).
- **Urbanización de su pueblo**: Tajiri vio cómo su ciudad natal (Machida)
  se volvía urbana y los bichos desaparecían; quiso devolver ese pasatiempo
  al mundo a través del juego ✅ (mismas fuentes).

### 24.2 El género que Pokémon fijó (no que inventó)
- El **«Trope Maker»** del género de reclutar monstruos es *Shin Megami
  Tensei* (Famicom, 1987; demonios, no monstruos de bolsillo); Pokémon Rojo
  y Verde (1996) es su **«Trope Codifier»**: el que fijó las reglas que
  todos copian después (atrapar, entrenar, coleccionar, luchar por turnos)
  ✅ ([TV Tropes, Franchise/Pokemon](https://tvtropes.org/pmwiki/pmwiki.php/Franchise/Pokemon),
  confirmado también por [Wikipedia, "Monster-taming game"](https://en.wikipedia.org/wiki/Monster-taming_game)).
- **Lista de obras del mismo tono** (niños + criaturas + viaje), de la
  recomendación de usuarios de AniList ya en `datos-texto.md` (no repetido
  aquí): **Digimon** (76 votos), **Yu-Gi-Oh!** (73, cartas en vez de
  monstruos), **Yo-kai Watch** (66), **Dinosaur King**, **Medabots**,
  **Monster Rancher**, **Bakugan**, **Beyblade**, **Doraemon** (76, gadgets
  en vez de criaturas).
- **Frente a Digimon** (el rival histórico más citado): ambas nacieron casi
  a la vez y compartían público infantil, pero **Pokémon mantiene un tono
  ligero y de aventura para todas las edades**, mientras **Digimon se
  oscurece con el tiempo** (duelo, mortalidad, ambigüedad moral) y sus
  criaturas son «compañeras que piensan y hablan», más que mascotas ✅
  ([CBR, "10 Things Digimon Does Better Than Pokémon"](https://www.cbr.com/digimon-vs-pokemon/),
  [ScreenRant, "Digimon Is Finally Beating Pokemon"](https://screenrant.com/digimon-beat-pokemon-anime-gaming/)).
  Es la comparación más repetida por la crítica y por el propio fandom
  (`FandomRivalry` en TV Tropes ✅
  ([TVTropes.org](https://tvtropes.org/pmwiki/pmwiki.php/FandomRivalry/Pokemon))):
  hoy se ven como «fandoms amigos», no rivales de verdad.

### 24.3 En el propio servidor «Sintonizando»
- **Sólo Pokémon usa el canal #autoroles** ✅ (comprobado en todos los
  `encargos/*.md`: `grep -li autoroles encargos/*.md` sólo devuelve
  `07-pok-mon.md`). No hay riesgo de repetir ahí la metáfora de «elige tu
  rol como eliges tu inicial».
- De las bíblias **ya terminadas** (01-36), ninguna usa un objeto de
  «elegir entre varias opciones sobre una mesa» como concepto de lámina
  (comprobé con `grep` la frase «elige tu» en los 25 `biblia.md` que ya la
  tienen escrita: sólo aparece en la de Pokémon) ✅. La más parecida en
  **tono** (anime infantil/familiar, no en el mismo canal) es **Doraemon**
  (19, ya terminada): su concepto para #recursos usa un **catálogo/cajón de
  pedidos** sobre el escritorio de Nobita, un objeto distinto (pedir un
  invento, no elegir entre tres) — no hay que preocuparse por duplicar la
  idea ✅ (comparación directa, leí su §19).
- **Digimon**, **Yu-Gi-Oh!** y **Yo-kai Watch** (los más cercanos en
  género) **todavía no tienen encargo ni biblia** en `encargos/` ⚠️: no hay
  nada que comparar todavía, pero si se hacen algún día, la lámina de
  Pokémon (mesa + Pokébolas + elegir) debería evitarse en la de Digimon
  (partner elegido por destino, no por elección sobre una mesa).

---

## 25 · El mundo, la historia y sus símbolos

### 25.1 Las reglas del mundo, en 5 líneas
1. Los **Pokémon** son criaturas que los **entrenadores** capturan con una
   **Pokébola**, entrenan y hacen luchar; cada entrenador empieza con un
   **inicial** y una **Pokédex** que registra a los que ve o atrapa ✅
   ([Wikipedia, jugabilidad de Pokémon](https://es.wikipedia.org/wiki/Jugabilidad_de_Pok%C3%A9mon)).
2. Cada región tiene **Gimnasios Pokémon**, cada uno con un **Líder** que
   se especializa en un tipo; ganarle da una **medalla** ✅ ([WikiDex,
   Gimnasio Pokémon](https://www.wikidex.net/wiki/Gimnasio_Pok%C3%A9mon)).
3. Con **8 medallas** (4 en las Islas Naranja) el entrenador entra a la
   **Liga Pokémon** de esa región, donde reta al **Alto Mando** y al
   **Campeón** para ser el nuevo campeón ✅ (misma fuente y [WikiDex, Liga
   Pokémon](https://www.wikidex.net/wiki/Liga_Pok%C3%A9mon)). El sueño que
   persigue Ash es ser **«Maestro Pokémon»**, un título por encima incluso
   de campeón regional.
4. Los Pokémon **evolucionan** (por nivel, por piedra, por intercambio,
   por cariño, según el juego/generación) y cambian de forma y a veces de
   tipo ✅ (misma fuente de jugabilidad).
5. El **Equipo Rocket** (Jessie, James y Meowth) es la amenaza cómica fija
   del anime: quieren robar Pokémon raros, especialmente a Pikachu, y casi
   siempre acaban «saliendo volando» (su lema ya está en la biblia, §10).

### 25.2 La historia por arcos (regiones), con su momento clave
De la Wikipedia en inglés y en español de la serie, cruzadas entre sí ✅:

| Región / arco | Año de estreno | Momento clave |
|---|---|---|
| **Kanto** (Liga Índigo) | abril 1997 | Ash recibe a Pikachu en el laboratorio de Oak y sale de Pueblo Paleta (§3.1 de la biblia) |
| **Islas Naranja** | enero 1999 | Primer título de campeón que gana Ash, fuera de una Liga oficial |
| **Johto** | octubre 1999-2000 | Llega hasta el top 8 de la Conferencia Plata |
| **Hoenn** (Advanced) | noviembre 2002 | Viaja con May y su hermano Max; primeras Megaevoluciones no, esas son Kalos |
| **Sinnoh** (Diamante y Perla) | septiembre 2006 | Se une Dawn, coordinadora Pokémon; Ash llega a semifinales de la Liga |
| **Teselia/Unova** (Blanco y Negro) | septiembre 2010 | Viaja con Iris y Cilan; se enfrenta al Team Plasma |
| **Kalos** (XY) | octubre 2013 | Se une Serena; se introduce la **Megaevolución** como mecánica de combate |
| **Alola** (Sol y Luna) | noviembre 2016 | Ash va a una escuela Pokémon; gana su **primer campeonato regional** |
| **Viajes / Sinopsis final** | 2019-2023 | Ash **gana el título de Campeón Mundial** por primera vez (2022) y despide su viaje en *Aim to Be a Pokémon Master* (2023, ya en §2.4 de la biblia) |
| **Horizons** | 2023-presente | Nuevos protagonistas, **Liko y Roy**, sin Ash |

⚠️ Los años de cada arco están cruzados en dos wikipedias (inglés y
español) pero **no en Bulbapedia** (dio 403 al abrirla): si hace falta el
mes y día exactos de cada estreno, hay que reintentar esa wiki con la red
que tenga el redactor.

### 25.3 Emblemas, logos y objetos icónicos
- **El logo «Pokémon»**: amarillo con borde azul (ya en §6 de la biblia).
- **La Pokébola**: mitad roja, mitad blanca, franja negra, botón blanco
  (§6, §16). Es el objeto que más identifica a toda la franquicia en
  cualquier país.
- **La Pokédex**: el «diccionario» de bolsillo que describe a cada
  Pokémon; en el anime **tiene voz propia** y hasta es un poco sarcástica
  con Ash (§7.3 de la biblia, ya escrito).
- **Las medallas de gimnasio** y la **Master Ball** (la Pokébola morada
  con una M rosa: captura garantizada) son los dos objetos de
  «recompensa máxima» del juego, reconocibles al instante por cualquier
  fan aunque no sean del anime ✅ ([Wikipedia, jugabilidad](https://es.wikipedia.org/wiki/Jugabilidad_de_Pok%C3%A9mon)).
- **El lema del Equipo Rocket** («Prepárense para los problemas… Y más
  vale que teman…») ya está confirmado con dos fuentes en la biblia (§10);
  es, junto al «¿Quién es ese Pokémon?» (§7.3), la fórmula de texto en
  pantalla más repetida de toda la serie.

### 25.4 Vocabulario propio (glosario rápido para cartelas y subtítulos)
| Término (uso latino) | Qué es |
|---|---|
| **Pokébola** | así se dice «Poké Ball» en el doblaje latino desde el anime original ✅ ([WikiDex](https://www.wikidex.net/wiki/Pok%C3%A9bola/Pok%C3%A9_Ball_(anime)), confirmado también por reseñas de doblaje sobre la traducción de Pokémon GO que cambia otros términos pero mantiene «Pokébola» como ya asentado) |
| **Entrenador Pokémon** | quien captura y entrena; es el «rol» que se elige en el concepto de lámina |
| **Pokédex** | enciclopedia de bolsillo; en el anime, habla (§7.3) |
| **Gimnasio / Líder de Gimnasio / Medalla** | edificio de combate por región, su jefe, y el premio de ganarle |
| **Liga Pokémon / Alto Mando / Campeón** | el torneo final de cada región y sus rivales más fuertes |
| **Maestro Pokémon** | el sueño final de Ash, por encima de ser campeón de una sola región |
| **Equipo Rocket** | el trío villano cómico (Jessie, James, Meowth); su lema ya en §10 |
| **Tipo** (fuego, agua, planta, eléctrico…) | la «especialidad» de cada Pokémon y de cada gimnasio |
| **Evolución** | el cambio de forma de un Pokémon al crecer o cumplir una condición |
| **¿Quién es ese Pokémon?** | segmento de silueta antes del corte publicitario (§7.3) |

---

## Revisión de mis puntos ya existentes (5, 6, 11) — confirmé, no rehice
No eran mi encargo obligatorio en este repaso (ya estaban escritos y con
bastante detalle), pero repasé sus ⚠️ con la red abierta:
- **§6 Tipografía (punto 5)**: la letra **Rodin NTLG DB / UDKakuGo
  Condensed 80 M** de Fontworks, que la biblia daba con **una sola fuente**
  (un tuit de Fontendo), ahora tiene **dos**: el mismo tuit sobre
  Escarlata/Púrpura y **otro tuit distinto de la misma cuenta sobre Espada/
  Escudo** ([UDKakugo Large Pr6N](https://x.com/fontendou/status/1162760191898574848)),
  ambos coincidiendo en el fabricante (Fontworks) y la familia (UD
  Kakugo). **Pasa a ✅** (dos publicaciones independientes, mismo dato).
  Además, la letra **Pokémon Solid** del logo tiene diseñador identificado:
  **IPBP** ✅ ([VectorDad](https://vectordad.com/fonts/pokemon-solid/)), y
  la licencia sigue **igual de confusa** entre espejos (unos dicen «gratis
  para uso comercial citando a IPBP», otros «sólo personal») ⚠️: mantengo
  el aviso de revisarla antes de usarla en algo que se publique.
- **§13 Videojuegos (punto 11)**: no encontré nada nuevo que cambiar; los
  menús oficiales en español ya vienen del propio código del juego (fuente
  primaria, no hace falta una segunda).
- **§7 Cuadros de diálogo (punto 6)**: sin cambios; ya está bien
  documentado con el código del juego.

---

## Lo mejor para la lámina
1. **Pokébola de arte oficial, línea marrón oscura + degradado suave**
   (`#221B11`, medido): mejor referencia de línea/sombra que un contorno
   negro genérico para el objeto central del concepto A.
2. **3 rigs de personaje confirmados por API** (Pikachu de Eleanie, Ash de
   Neut2000, Oak ahora confirmado con rig): antes la biblia sólo tenía
   objetos en 3D, no personajes — llena un hueco real del punto 18.
3. **La cadena Tajiri → bichos → Ultraman → Dragon Quest V**: sirve para
   explicar en un texto corto «de dónde sale la idea de la Pokébola» sin
   inventar nada.
4. **Sólo Pokémon usa #autoroles y sólo esta biblia usa «elige tu inicial»**
   como metáforas: no hay riesgo de repetir la idea en otro canal del
   servidor.
5. **El glosario de vocabulario (25.4)**: Pokébola, Liga Pokémon, Maestro
   Pokémon, tipo, evolución — útil para cualquier texto corto del canal
   que quiera sonar «como Pokémon» sin copiar frases de los juegos.

## No encontré
- ⚠️ Nombre exacto de la entrega de Pokémon que estrenó OLM Asia en
  diciembre de 2017 con Clip Studio Paint (el artículo de AWN no lo dice).
- ⚠️ Confirmación de grano de película, brillo o aberración cromática como
  intención de estudio (busqué en inglés y japonés; nada).
- ⚠️ Fecha exacta (mes/día) de cada arco: sólo tengo el año, cruzado en dos
  wikipedias; Bulbapedia (que sí las tendría) dio 403 todo este repaso.
- ⚠️ Una cita directa del director Kunihiko Yuyama sobre la intención de
  color o estilo visual del anime (encontré que usó el mapa del juego de
  referencia, pero la fuente es una foto de revista en Facebook, sin texto
  completo verificable): no lo doy como cita textual por eso.

## Bitácora de búsqueda (texto, esta pasada)
- **Red directa (curl)**: `bulbapedia.bulbagarden.net`, `tcrf.net` y
  `pokemon.fandom.com` → **403** todo el rato, con y sin User-Agent.
  `en.wikipedia.org` y `es.wikipedia.org` → **200**. `raw.githubusercontent.com`
  y `api.sketchfab.com` → **200**, usados para medir y confirmar licencias.
- **WebFetch**: sirvió en Wikipedia (en/es), CGWORLD, AWN, WikiDex,
  letras.com; falló (403/402) en Bulbapedia y Doblaje Wiki normal (como
  avisa `AYUDANTE.md`, ésa sólo por su API, que no me hacía falta en este
  repaso).
- **WebSearch, inglés (11)**: OLM Incorporated animation technique · Ken
  Sugimori watercolor gouache · Satoshi Tajiri Time interview bug
  collecting · Pikachu Blender rig · Pokemon anime shot composition
  reaction shot · cel shading Blender Freestyle Solidify · TV Tropes trope
  codifier monster collecting · Pokébola Poké Ball dub name · Team Rocket
  motto latino · monster-taming genre history · Digimon vs Pokemon rivalry.
- **WebSearch, japonés (1)**: ポケモン アニメ 制作 セル画 デジタル彩色 OLM
  作画.
- **Sketchfab, por su API (no cuenta como búsqueda web)**: `pikachu rig`,
  `ash ketchum`, `professor oak`, `charmander rig` — licencias y `rig`
  comprobados uno a uno, no de memoria.
- **Lo que NO encontré**: ver arriba. No usé buscador en coreano ni chino
  para estos 3 puntos (ya se hicieron 1 y 0 búsquedas respectivamente en la
  primera pasada, según `datos-texto.md`/bitácora general; para 18/24/25 no
  hacía falta un tercer idioma distinto del japonés).
