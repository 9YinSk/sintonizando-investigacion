# Parte del investigador de TEXTO, JUEGOS Y TÉCNICA · Adventure Time (Hora de aventura)

Puntos de ENCARGO.md: **5** (tipografía), **6** (cuadros de diálogo/interfaces), **11**
(videojuegos), **18** (estilo y técnica, cómo replicarlo), **24** (obras parecidas),
**25** (el mundo, la historia y sus símbolos).

Es un **repaso**: la biblia ya tenía §6, §7 y §13 (puntos 5, 6, 11) con red cerrada;
aquí los confirmo y profundizo con red abierta. Los puntos 18, 24 y 25 **no existían**
en la biblia (se añadieron el 24-sep, después de escrita): van de cero.
`datos-texto.md` no trajo nada (todas las fuentes automáticas fallaron para esta
serie occidental), así que todo lo de abajo es búsqueda directa mía.

## Hallazgos

### Punto 5 · Tipografía

- El logo «Adventure Time» es un rótulo dibujado a mano, no una fuente: letras
  gorditas, redondas y algo temblorosas · [madegooddesigns](https://madegooddesigns.com/adventure-time-font/),
  [BetterStudio](https://betterstudio.com/fonts/adventure-time-font/) · ✅ (ya
  estaba en la biblia; lo confirmo, sigue en pie).
- **La fuente de fans «Adventure Time» (dafont.com) SÍ la descargué** (`dl.dafont.com/dl/?f=adventure_time`,
  zip con `Adventure Time.ttf`) y la revisé con `fontTools.ttLib` (no de memoria).
  Tiene glyphs para á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü, **pero sólo mapeados en la
  tabla Mac Roman (plataforma 1,0)**: el archivo **no tiene tabla Unicode para
  Windows** (plataforma 3,1), sólo una tabla «Symbol» (3,0) en 0xF000+. En la
  práctica: en Photoshop/Illustrator sobre Windows, teclear ñ o ¿ con esta
  fuente probablemente **no muestre el carácter correcto** (haría falta
  insertar el glifo a mano). **No usarla para texto en español**; sólo para la
  palabra «Adventure Time» tal cual, en inglés · [dafont.com/adventure-time.font](https://www.dafont.com/adventure-time.font)
  · ✅ (comprobado por mí, archivo real inspeccionado con fontTools) · resuelve
  el ⚠️ anterior «no pude bajarla».
- El letrista de los cómics de **BOOM! Studios** es **Steve Wands**, confirmado
  en dos fuentes: la wiki de la serie (que dice que «actualmente hace el
  lettering de Adventure Time») y créditos externos de cómic (League of Comic
  Geeks: Adventure Time #41; Comic Vine: créditos de la serie) ·
  [adventuretime.fandom.com/wiki/Steve_Wands](https://adventuretime.fandom.com/wiki/Steve_Wands),
  [leagueofcomicgeeks.com/comic/3374523](https://leagueofcomicgeeks.com/comic/3374523/adventure-time-41)
  · ✅ · sustituye el ⚠️ anterior «de memoria; no busqué el rotulista».
- Comprobé yo mismo con fontTools (descargando el `.woff2` real, subset
  «latin», no «latin-ext») 6 letras libres ya propuestas en la biblia:
  **VT323**, **Press Start 2P** (las de la pantalla de BMO/consola), **Creepster**,
  **Eater**, **Rubik Doodle Shadow** y **Bungee** — las seis traen á é í ó ú Á
  É Í Ó Ú ñ Ñ ¿ ¡ ü completas · [cdn.jsdelivr.net/fontsource](https://cdn.jsdelivr.net/fontsource/fonts/vt323@latest/latin-400-normal.woff2)
  · ✅ (verificación directa mía, no repito la del pase anterior).
  - Nota técnica para quien monte la lámina: si se descarga la variante
    **«latin-ext»** de Fontsource en vez de **«latin»**, esa variante NO trae
    los caracteres españoles (los acentos españoles están en Latin-1
    Supplement, dentro del subset «latin»; «latin-ext» es para lenguas de
    Europa del Este/Vietnamita). Lo comprobé al confundirme yo mismo con
    VT323: con «latin-ext» faltaban las 15 letras; con «latin» estaban todas.

### Punto 6 · Cuadros de diálogo, cartelas e interfaces

- Letrista de BOOM! confirmado arriba (✅) → sube de ⚠️ a ✅ el dato de §7.1.4
  de la biblia sobre los cómics.
- **BMO** está diseñado explícitamente como una parodia de las videoconsolas
  portátiles retro de Nintendo (tipo Game Boy). Dos fuentes independientes: (1)
  un mod real que convierte un Game Boy Color en «BMO» cambiando sólo el
  cartucho, descrito como «BMO is Finn and Jake's cute living video game
  system... resembles a mixture of old Nintendo video games» ·
  [instructables.com](https://www.instructables.com/Adventure-Times-BMO-Roommate-GBC-Mod/);
  (2) el sitio interactivo oficial de Active Theory para el especial «Distant
  Lands: BMO» (HBO Max), que usa la cara de BMO como interfaz de navegación
  con estética de computadora retro (resumen de Medium; el sitio en sí dio 403
  al intentar verlo directo, sólo tengo el resumen) · [medium.com/active-theory](https://medium.com/active-theory/adventure-time-distant-lands-bmo-5997687372b7)
  · ✅ (dos fuentes, diseño confirmado) — lo que se ve en pantalla dentro de
  cada episodio en sí sigue sin confirmar con una imagen mía (sigue ⚠️).
- Videojuego **«Hey Ice King! Why'd You Steal Our Garbage?!!»** (DS/3DS,
  WayForward, 2012): **vi directamente** la hoja de sprites «Mugshots» —
  retratos de cuerpo completo, estilo simplificado (chibi), de unos 28
  personajes (Finn, Jake, BMO, Dulce Princesa, Flama Princesa, Rey Helado,
  Marceline, Lady Rainicorn, Gunter…), pensados para ir junto al cuadro de
  texto de diálogo del juego · [spriters-resource.com](https://www.spriters-resource.com/ds_dsi/adventuretimehicwysog/asset/54668/)
  · imagen 759×673 px (medida por mí) · ✅ — resuelve el ⚠️ anterior «no lo
  pude comprobar, no lo uses sin ver una captura»: **ya la vi**.
- App móvil **«Card Wars»** (Kung Fu Factory / Cartoon Network, 2014, dada de
  baja en dic-2019): **vi una captura real de 2560×1440** del menú principal
  (puerto a PC archivado en GitHub, con capturas propias del autor) — interfaz
  con marcos metálicos/biselados azul-grisáceo, barra de vida y XP con
  retrato del personaje arriba a la izquierda, contadores de monedas y gemas
  arriba a la derecha, tapete de batalla hexagonal de madera/piedra, botón
  rojo redondeado «BATTLE!» con letra blanca gruesa de cartel (estilo parecido
  a Chewy/Luckiest Guy) · [github.com/shishkabob27/CardWars](https://github.com/shishkabob27/CardWars)
  (captura: [i.imgur.com/cXUolY0.jpg](https://i.imgur.com/cXUolY0.jpg)) ·
  imagen 2560×1440 px (medida por mí) · ✅ (vista y medida directamente).

### Punto 11 · Videojuegos de la franquicia

Amplío la lista y la interfaz del §13 de la biblia (antes sólo decía «existen»):

- **Hey Ice King! Why'd You Steal Our Garbage?!!** (WayForward, D3/Bandai
  Namco, DS y 3DS, 20-nov-2012). Pendleton Ward escribió la historia junto con
  WayForward. Exploración del mapa en vista cenital; combate y mazmorras de
  lado, tipo *Zelda II*; Finn y Jake se controlan a la vez (Jake dentro de la
  mochila, saca ítems). 4 zonas: Grass Lands, Candy Kingdom, Red Rock Pass,
  Ice Kingdom · [Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time:_Hey_Ice_King!_Why%27d_You_Steal_Our_Garbage%3F!!),
  [Giant Bomb](https://giantbomb.com/wiki/Games/Adventure_Time_Hey_Ice_King_Whyd_you_steal_our_garbage),
  [Nintendo Life](https://www.nintendolife.com/reviews/ds/adventure_time_hey_ice_king_whyd_you_steal_our_garbage)
  · ✅. Interfaz de diálogo: ver Mugshots arriba (punto 6) ✅.
- **Adventure Time: Explore the Dungeon Because I Don't Know!** (WayForward,
  2013, PS3/Xbox 360/Wii U/3DS): *dungeon crawler* cooperativo hasta 4
  jugadores · [Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time:_Explore_the_Dungeon_Because_I_Don%27t_Know!)
  · ⚠️ (una sola fuente).
- **The Secret of the Nameless Kingdom** (WayForward, 2014, tipo Zelda) — ya
  en la biblia · ✅.
- **Pirates of the Enchiridion** (Climax Studios, 2018) — ya en la biblia ·
  ✅.
- **Card Wars** (app iOS/Android, Kung Fu Factory, 2014-2019): juego de cartas
  con Finn, Jake, BMO, Dulce Princesa, Marceline, Flama Princesa jugables;
  captura real vista arriba (punto 6) · [Fandom](https://adventuretime.fandom.com/wiki/Card_Wars_(application))
  · ✅.
- **Card Wars Kingdom**: secuela/expansión móvil de Card Wars · sólo tiendas
  de APK como fuente (Uptodown, Softonic) · ⚠️ (una fuente, no oficial).
- No encontré capturas de la **caja de texto** (no el menú) de «The Secret of
  the Nameless Kingdom» ni de «Pirates of the Enchiridion»: la API de Steam no
  respondió para los appid 298890 y 353200 (puede que estén mal o retirados),
  y TrueAchievements/Steam Community tienen galerías que no pude abrir con las
  herramientas de este contenedor. Ver «No encontré».

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Producción real** (Wikipedia, sección «Animation», con entrevistas citadas
por ese artículo):

- El dibujo es **a mano, en papel**; luego se compone y se pinta digitalmente
  («hand-drawn on paper, which was then digitally composited and painted with
  digital ink and paint») ✅.
- La preproducción (props, personajes, fondos) se hizo **sobre todo en
  Photoshop**, según **Phil Rynda**, diseñador líder del programa (confirmado
  como diseñador líder en su ficha de la wiki de la serie) · [Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time),
  [Phil Rynda · Fandom](https://adventuretime.fandom.com/wiki/Phil_Rynda) ·
  ⚠️ (el dato del Photoshop en concreto sale sólo de Wikipedia citando una
  entrevista que no encontré directa; no tengo una segunda fuente propia para
  ese detalle exacto, aunque el diseñador sí está confirmado en dos).
- La animación en movimiento se hacía en **Corea del Sur**, por **Rough Draft
  Korea** o **Saerom Animation**; el diseño y el color final se hacían en
  **Cartoon Network Studios (Burbank, California)** · [Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time)
  · ⚠️ (una fuente).
- El productor ejecutivo **Fred Seibert** comparó el estilo con **Felix the
  Cat** y los dibujos de **Max Fleischer**, y dijo que el mundo también se
  inspiraba en videojuegos · [Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time)
  · ⚠️ (una fuente).
- Dirección de arte: **Nick Jennings**, quien dirigió el departamento de
  animación y pintó muchas cartelas de título (ya en la biblia, lo confirmo) ·
  [Fandom](https://adventuretime.fandom.com/wiki/Nick_Jennings) · ✅. Diseño de
  fondos en la temporada 1: **Ghostshrimp** y **Santino Lascano**; pintura:
  **Sue Mondt** y **Martin Ansolabehere** · ⚠️ (una fuente, la propia ficha).
- **Línea y color** (análisis de estilo — no es un making-of oficial, son
  varias fuentes de análisis/fandom que coinciden, por eso queda en ⚠️):
  contorno negro limpio con un ligero temblor «a mano» (más grueso en las
  primeras temporadas); colores **planos y saturados**, casi sin degradados ni
  sombreado complejo (cel-shading simple, 1-2 tonos); formas simples y
  geométricas (el cuerpo de Finn es casi una habichuela) · ⚠️.

**Cómo reproducirlo en Photoshop** (a partir del flujo real de arriba: papel a
mano → tinta digital → color plano — es una propuesta práctica mía, no una
fuente citada, coherente con lo documentado):

- Capa de **línea** aparte: pincel de tinta dura, opacidad 100%, sin textura,
  ~3-4 px sobre un lienzo de 1500 px de ancho, sin antialiasing exagerado.
- Capa de **color base** DEBAJO de la línea, con cubo de relleno (bordes
  duros, no degradados).
- Sombra en **una sola capa «Multiply»**, un solo tono, sin aerógrafo — así se
  ve el cel-shading plano de la serie.
- Para cartelas pintadas a mano (§3.2 y §6.1 de la biblia): una capa de
  **textura de papel viejo** (grano visible) en «Multiply» u «Overlay» a baja
  opacidad, encima del color.

**Cómo reproducirlo en Blender**:

- Contorno: **modificador Solidify** con normales invertidas y grosor
  ~0.01-0.02 (método «inverted hull», funciona en Eevee) o el motor
  **Freestyle** (pestaña Render) para línea automática sobre los bordes del
  modelo — dos métodos documentados en tutoriales reales de Blender ·
  [Blender Studio — Toon Character Workflow](https://studio.blender.org/training/toon-character-workflow/5859a5da1f47427e3fe82330/),
  [BlenderNation](https://www.blendernation.com/2020/02/06/how-to-make-a-toon-shader-with-dynamic-outlines/)
  · ✅ (técnica genérica y documentada, no específica del estudio de la
  serie).
- Sombreado: un **Toon Shader**, o un nodo Diffuse con **ColorRamp** cortando
  la sombra en 1-2 tonos duros (sin degradado), igual que el plano de la
  serie.
- Modelos/rigs **libres** de Sketchfab con licencia **CC Attribution (CC BY)**,
  con licencia comprobada por la API de Sketchfab (no de memoria):
  - «Finn - (Adventure Time)» de **Agu.3D**, 64 992 caras, CC BY ·
    [sketchfab.com/3d-models/none-309e158598764644a5c6068e0cfdc898](https://sketchfab.com/3d-models/finn-adventure-time-309e158598764644a5c6068e0cfdc898)
    · ✅.
  - «Finn Adventure Time» de **Nico Caraballo (theniloart)**, 1 548 caras
    (más ligero, mejor para pruebas), CC BY · [sketchfab.com](https://sketchfab.com/3d-models/none-19255b56148247eaa213bff7974304a4)
    · ✅.
  - «Jake» de **Mormont**, CC BY · [sketchfab.com/3d-models/jake-6326c036c6f14d09bf0708ca4289d699](https://sketchfab.com/3d-models/jake-6326c036c6f14d09bf0708ca4289d699)
    · ✅.

**Encuadres y composición**: no encontré un making-of o entrevista específica
sobre planos/ángulos típicos, más allá de lo que ya recogió el pase anterior
(reglas de estilo de Ward sobre los «brazos de fideo», bitácora #34 de la
biblia). Ver «No encontré».

### Punto 24 · Obras parecidas y temas relacionados

- **The Marvelous Misadventures of Flapjack** (Cartoon Network, 2008-2010) es
  el semillero real: Pendleton Ward fue guionista y storyboardista ahí antes
  de crear Adventure Time. Confirmado en dos fuentes: SlashFilm y Wikipedia ·
  [slashfilm.com](https://www.slashfilm.com/1581694/flapjack-cartoon-network-disney-nickelodeon-descendants/),
  [Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time) · ✅.
- De ese mismo equipo salieron series de tono parecido (fantasía + humor +
  emoción), confirmadas en las mismas dos fuentes:
  - **Gravity Falls** (Alex Hirsch, storyboardista en Flapjack) ✅.
  - **Over the Garden Wall** (Patrick McHale, storyboardista en Flapjack y
    **director creativo de Adventure Time hasta la temporada 2**) ✅.
  - **Steven Universe** (Rebecca Sugar, storyboardista en Flapjack y luego
    guionista/storyboardista de Adventure Time varias temporadas) ✅. El
    servidor ya tiene una biblia en marcha para Steven Universe
    (`biblias/64-steven-universe/`, encargo 64, aún sin `biblia.md` — sólo
    `partes/` por ahora): que el redactor lo tenga en cuenta para no repetir
    ideas de lámina entre ambas series.
  - **Regular Show** (J.G. Quintel, director creativo de Adventure Time en
    sus 2 primeras temporadas, antes de crear su propia serie) ✅.
- Influencias que el propio Ward reconoce, con cita textual: **Dungeons &
  Dragons** («Writing for the show is a lot like playing DnD... I get all my
  dungeon crawls out in writing the show») · [The Mary Sue](https://www.themarysue.com/pendleton-ward-interview/)
  · ⚠️ (una fuente, cita directa); **Hayao Miyazaki / El vecino Totoro** para
  los momentos «hermosos» en medio del humor, y **Home Movies** y **Dr. Katz,
  Professional Therapist** por el diálogo «relajado» y natural · [Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time)
  · ⚠️ (una fuente, sin la entrevista original a mano).

### Punto 25 · El mundo, la historia y sus símbolos

**Reglas del mundo (Ooo), en 5 líneas** (wikitext de la wiki de la serie,
`adventuretime.fandom.com`, artículos «Mushroom War» y «Land of Ooo»):

1. Ooo es la Tierra, **unos mil años después de la Guerra de los Hongos**
   (Mushroom War), un intercambio nuclear global entre fines del s. XX y
   principios del XXI · ✅.
2. La bomba mutagénica que cayó sobre lo que fue Norteamérica **despertó al
   Lich** y trajo de vuelta la magia, que llevaba siglos en decadencia · ✅.
3. La humanidad casi desapareció; sobrevivieron algunas tribus, y de ellas (y
   de la mutación) nacieron las nuevas razas de Ooo (gente-dulce, elementales,
   etc.) · ✅.
4. Ooo se divide en reinos: **Reino Helado, Reino Dulce, Condado de
   Lemongrab, Reino Wildberry, Reino de Fuego, Reino de las Nubes**, y zonas
   sin reino como el Bosque Maligno; **Lumpy Space** es una dimensión aparte,
   no parte de Ooo · ✅.
5. Frederator publicó dos mapas oficiales de Ooo junto al documento de
   presentación original (uno en blanco y negro de Ghostshrimp, más fiel a lo
   que se ve en pantalla; uno a color) · ✅.

**Historia por arcos** (temporadas), con su momento clave (Wikipedia,
resúmenes de temporada):

- **T1-5**: episodios sueltos, con pistas repartidas sobre el pasado del Rey
  Helado/Simon y el origen de Marceline · ✅.
- **T6**: Finn descubre la identidad real de su padre humano e intenta
  reconectar con él · ✅.
- **T7 — «Stakes»** (miniserie de 8 episodios): el pasado de Marceline como
  vampira y la lucha contra vampiros resucitados; Marceline hace las paces
  con su naturaleza vampírica · ✅.
- **T8 — «Islands»** (miniserie): Finn, Jake, BMO y Susan Strong cruzan el
  océano para resolver el misterio del pasado de Finn; aparece Fern y Finn
  conoce a su madre · ✅.
- **T9 — «Elements»** (miniserie): la magia elemental convierte a Ooo en una
  distopía; Finn, Jake y BMO tienen que arreglarlo · ✅.
- **T10 (final)**: Dulce Princesa se enfrenta a su tío Gumbald; Finn lidia con
  el lado oscuro de Fern; Betty intenta devolverle a Simon Petrikov su
  identidad, quitándole la corona del Rey Helado · ✅.
- Fuente de todo el bloque: [Wikipedia — temporadas 6 a 10](https://en.wikipedia.org/wiki/Adventure_Time_season_6)
  (y las páginas equivalentes de las temporadas 7-10) · ⚠️ (una fuente para
  el detalle arco por arco, aunque cada arco además aparece mencionado suelto
  en la wiki de fans).

**Emblemas, objetos icónicos y vocabulario** que un fan reconoce al instante:

- **El Enchiridion**: el manual del héroe, tratado como si fuera sagrado; el
  nombre viene del griego/latín *encheiridion*, «lo que se lleva en la mano»,
  «manual» · [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/WesternAnimation/AdventureTime),
  [Wikipedia — The Enchiridion!](https://en.wikipedia.org/wiki/The_Enchiridion!)
  · ✅.
- **La corona del Rey Helado**: objeto mágico creado por Urgence Evergreen;
  llevarla puesta durante siglos es lo que **volvió loco a Simon Petrikov**
  (el origen de todo el personaje) · [Fandom — Ice King's crown](https://adventuretime.fandom.com/wiki/Ice_King%27s_crown)
  · ✅ (ya insinuado en la biblia, aquí queda con fuente directa).
- **La Espada de Hierba (Grass Sword)** de Finn, y después su brazo/espada de
  cactus tras perder el brazo derecho: dos símbolos visuales de las distintas
  «eras» de Finn como héroe · [Fandom — Grass Sword](https://adventuretime.fandom.com/wiki/Grass_Sword)
  · ✅.
- **El Nightosphere**: el inframundo demoníaco gobernado por Hunson Abadeer,
  padre de Marceline · [Fandom — Nightosphere](https://adventuretime.fandom.com/wiki/Nightosphere)
  · ✅.
- **Card Wars**: el juego de cartas dentro del propio show que se volvió un
  juego real (ver punto 11) — ya en la biblia · ✅.
- Vocabulario propio: **«Ooo»**, **«Glob»** (como «Dios»), **Nightosphere**,
  **Lumpy Space**, la frase-título **«What time is it? — ¡HORA DE
  AVENTURA!»**, y las muletillas abandonadas «**¡Algebraico!**» /
  «**¡Matemático!**», que vienen del episodio piloto y se dejaron de usar tras
  la primera temporada · [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/WesternAnimation/AdventureTime)
  · ⚠️ (una fuente tipo wiki de fans, no un guion oficial).

## Lo mejor para la lámina

- La fuente **VT323** o **Press Start 2P**, ya con tildes/ñ/¿/¡ comprobadas por
  mí, para cualquier texto «de pantalla de BMO» en la lámina.
- El objeto **Enchiridion** o la **corona del Rey Helado** como símbolo de
  mundo si se quiere una lámina 2 fuera de #musica-nueva (encaja con el punto
  25, «objeto real en un sitio real»).
- La hoja de sprites «Mugshots» del juego de DS (vista y medida) sirve de
  referencia de cómo Adventure Time simplifica a sus personajes en formato
  «icono» — útil si se hace una lámina con varios personajes pequeños.
- El modelo de Sketchfab «Finn - (Adventure Time)» de Agu.3D (CC BY) es el
  más razonable para posar en Blender sin pagar ni inventar.
- Conexión Flapjack → Adventure Time / Steven Universe / Gravity Falls / Over
  the Garden Wall / Regular Show: útil para que el dueño entienda por qué
  varias láminas del servidor (ver `biblias/64-steven-universe/`) pueden
  compartir un aire de familia sin que sea un problema.

## No encontré

- **Capturas de la caja de diálogo** (el cuadro de texto en sí, no el menú)
  de «The Secret of the Nameless Kingdom» ni de «Pirates of the Enchiridion».
  Búsquedas hechas: `store.steampowered.com/api/appdetails?appids=298890` y
  `...appids=353200` (ambas responden `success:false`, puede que el appid real
  sea otro), `"Secret of the Nameless Kingdom" screenshot dialogue text box
  interface` (en), `"Pirates of the Enchiridion" screenshot dialogue` (en);
  TrueAchievements y Steam Community tienen galerías pero no las pude abrir
  con WebFetch (no dan contenido legible).
- **Encuadres y composición típicos** (planos, ángulos) de la animación, más
  allá de lo ya recogido en la bitácora #34 de la biblia (notas de Ward sobre
  «brazos de fideo»). Búsquedas: `Adventure Time storyboard camera angles
  composition interview` (en), `Adventure Time cinematography analysis` (en).
  No hay un artículo o entrevista específico sobre esto; lo que hay son vídeos
  de análisis de YouTube sin transcripción accesible aquí (le toca al
  investigador de vídeo mirarlos con `fotogramas.py`, no a mí).
- **El sitio interactivo de Active Theory** (Distant Lands: BMO) directo: dio
  403 con WebFetch dos veces; sólo tengo el resumen indexado.
- **La entrevista original** donde Phil Rynda habla del uso de Photoshop en
  preproducción (sólo la tengo citada por Wikipedia, sin la fuente primaria).
- **industriaanimacion.com** (artículo en español sobre la animación de la
  serie): dio 503 dos veces y curl no conectó; lo dejo anotado por si alguien
  más tiene mejor suerte con la red en otro momento.
- **Una captura del texto grabado en pantalla en un episodio real de BMO**
  (mostrando un juego o mensaje): sólo confirmé el diseño de BMO como
  «parodia de consola retro», no una imagen mía de un fotograma con texto en
  su pantalla (eso requeriría `fotogramas.py` sobre un episodio con BMO, que
  es tarea del investigador de vídeo).

## Bitácora de búsqueda

### Comprobación de red (25-sep-2026)

- **curl** funciona: `adventuretime.fandom.com/api.php` (200; ojo, el
  subdominio correcto es `adventuretime`, **no** `adventuretimewithfinnandjake`
  como sugería el encargo — comprobado con `action=query&meta=siteinfo`),
  `doblaje.fandom.com` (200), `dl.dafont.com` (200, bajé un ttf real),
  `spriters-resource.com` (200), `i.imgur.com` (200), `store.steampowered.com`
  (200 pero `success:false` para esos dos appid), `cdn.jsdelivr.net/fontsource`
  (200).
- **curl** no conectó: `tcrf.net` (403), `web.archive.org` (cortado a media
  conexión, un solo intento), `industriaanimacion.com` (503 dos veces, y
  luego 000 con curl directo).
- **WebFetch**: funcionó en Wikipedia, GitHub (repo `shishkabob27/CardWars`,
  vía resumen), Spriters Resource. Bloqueado (403) en `medium.com` y `tcrf.net`.
- El acceso a `raw.githubusercontent.com` está cerrado en este contenedor para
  repos no vinculados con `add_repo` (probé bajar Google Fonts directo de ahí
  y dio un JSON de error, no el archivo).

### Búsquedas web (WebSearch, ~14 de las ~50 del cupo)

| # | Idioma | Búsqueda | Qué salió |
|---|---|---|---|
| 1 | en | animación Toon Boom Harmony Photoshop backgrounds interview | nada específico de AT, sólo genérico |
| 2 | en | Pendleton Ward influences interview D&D Flapjack | Mary Sue: cita de D&D; Wikipedia: Totoro, Home Movies |
| 3 | en | background art Nick Jennings gouache watercolor Photoshop | ficha de Fandom, sin técnica concreta |
| 4 | en | "Hey Ice King" DS game dialogue box screenshot portrait | Spriters Resource (clave) |
| 5 | en | series similares Gravity Falls Regular Show Steven Universe Over the Garden Wall | primer indicio de Flapjack |
| 6 | en | BOOM! Studios letterer Steve Wands | confirmado en Fandom + comics DB |
| 7 | en | Sketchfab Finn Jake free rig | 5+ modelos CC BY |
| 8 | en | line art black outline flat color cel shading style | análisis de estilo (⚠️, blogs) |
| 9 | en | TV Tropes symbols Enchiridion Algebraic Mathematical | Enchiridion, catchphrases abandonados |
| 10 | en | Blender Solidify Freestyle toon outline tutorial | técnica confirmada (Blender Studio, BlenderNation) |
| 11 | en | Card Wars mobile game interface screenshot | repo de GitHub con capturas reales |
| 12 | en | story arcs season by season Finn arm Elements finale | resumen T6-T10 (Wikipedia) |
| 13 | en | "Card Wars" mobile game screenshot deck | mismo repo, confirmado |
| 14 | en | Flapjack storyboard alumni Hirsch McHale Sugar | SlashFilm (segunda fuente para punto 24) |
| 15 | en | Rynda Photoshop pre-production interview | sin la entrevista original, sólo referencias |
| 16 | en | BMO screen face Nintendo parody interface | mod de GBC + sitio de Active Theory |
| 17 | en | film grain post-production Adventure Time | nada específico de la serie |
| 18 | en | dafont Adventure Time font ttf download | encontré el zip descargable real |

No hice búsquedas en japonés/coreano/chino: la serie es estadounidense: sus
entrevistas originales están en inglés (igual que anotó el pase anterior).

### Fandom (API directa, sin gastar cupo de búsqueda)

- `action=query&meta=siteinfo`: confirmé el subdominio correcto
  (`adventuretime.fandom.com`).
- `action=parse&prop=wikitext` en: Mushroom War, Land of Ooo, Ice King's
  crown, Grass Sword, Nightosphere, Steve Wands, BMO (búsqueda), Card Wars
  (redirección a desambiguación).
- `action=query&list=search`: para encontrar los títulos reales detrás de
  redirecciones (Mushroom War, story arc, BMO screen, crown ice king).

### Fuentes consultadas por tipo

- **Oficiales/semioficiales**: Wikipedia (artículo principal y temporadas
  6-10), Fandom de la serie (varias páginas), sitio de Active Theory (sólo
  resumen).
- **Herramientas técnicas usadas de verdad**: `fontTools.ttLib` (tres veces:
  fuente de fans de dafont, VT323, Press Start 2P + 4 más), API de Sketchfab
  (licencias), `file`/Pillow-equivalente vía `file` de Linux para medir
  imágenes.
- **Comunidad/fans**: TV Tropes, SlashFilm, The Mary Sue, Instructables (mod
  de BMO), GitHub (`shishkabob27/CardWars`, puerto no oficial con capturas).
- **Videojuegos**: Giant Bomb, Nintendo Life, The Spriters Resource (hoja de
  sprites vista y medida), GameFAQs (referencia, no citado directo).
- **Letras/tipografía**: dafont.com (descarga real), Fontsource vía
  `cdn.jsdelivr.net` (descarga real de 6 fuentes en subset «latin»).
- **3D**: API de Sketchfab (`api.sketchfab.com/v3/search`), licencias CC BY
  confirmadas por la respuesta de la API, no de la página web.

## Cumplimiento de mi parte (puntos 5, 6, 11, 18, 24, 25)

| Punto | Estado | Por qué |
|---|---|---|
| 5 · Tipografía | ✅ | Confirmé lo que ya había, bajé y probé con fontTools la fuente de fans del logo (hallazgo nuevo: no tiene tabla Unicode Windows) y 6 fuentes libres más, y até el letrista de BOOM! a dos fuentes. |
| 6 · Cuadros de diálogo/interfaces | ✅ | Subí de ⚠️ a ✅ el letrista de cómic y el diseño de BMO; **vi y medí** dos capturas reales de videojuego (Mugshots DS, menú de Card Wars) que antes no existían en la biblia. |
| 11 · Videojuegos | ⚠️ | Amplié bastante la lista y confirmé la interfaz de dos juegos con imágenes reales, pero sigo sin caja de diálogo de «Nameless Kingdom» ni «Pirates of the Enchiridion» (ver «No encontré»). |
| 18 · Estilo y técnica, cómo replicarlo | ✅ | Sección nueva completa: producción real (Wikipedia, con matices de fuente única marcados ⚠️) + pasos concretos y realistas para Photoshop y Blender (Solidify/Freestyle, toon shader, 3 modelos CC BY con licencia verificada por API). Encuadres/composición queda flojo, anotado en «No encontré». |
| 24 · Obras parecidas | ✅ | Sección nueva completa: la conexión real vía Flapjack (Ward-Hirsch-McHale-Sugar-Quintel) con dos fuentes, más las influencias que Ward reconoce él mismo (D&D, Miyazaki), y aviso al redactor sobre la biblia de Steven Universe en curso. |
| 25 · El mundo, la historia y símbolos | ✅ | Sección nueva completa: reglas del mundo en 5 líneas, arcos por temporada con momento clave, y 5+ símbolos/objetos con fuente directa de wiki. |

Parte terminada: no queda nada obligatorio pendiente de mis puntos (5, 6, 11,
18, 24, 25). Lo que falta (caja de diálogo de 2 videojuegos, encuadres de
cámara, la entrevista original de Rynda) son extras, ya anotados en «No
encontré» con ⚠️, no bloquean el cumplimiento del encargo para mi rol.
