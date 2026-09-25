# Parte TEXTO, JUEGOS Y TÉCNICA · Sword Art Online (todas)

Investigador de texto: puntos 5, 6, 11, 18, 24, 25 de ENCARGO.md. Libreta de datos, no prosa.
Wiki usada: `swordartonline.fandom.com`. Base: `partes/datos-texto.md` (casi vacío: recolectar.py no
tenía wiki configurada ni encontró la obra en AniList; se investigó todo a mano).

## Hallazgos

### Punto 5 — Tipografía

- Logo/título oficial «SWORD ART ONLINE»: no hay confirmación de una tipografía comercial exacta
  usada por Kadokawa/Aniplex (no se encontró declaración oficial). Fans replicaron el logo como
  fuente descargable «Sword Art Online» / «SAO UI» (DarkBlackSwords, DeviantArt, dafont, fontmeme) ·
  https://www.deviantart.com/darkblackswords/art/Sword-Art-Online-Font-Download-426603647 ·
  https://fontmeme.com/sword-art-online-font/ · ⚠️ (una fuente, sin confirmar con el estudio) ·
  visualmente: sans-serif condensada, mayúsculas, barras finas anguladas, remate en punta en la «W».
  Para usar en la lámina (letra libre, sin líos de licencia): **Orbitron** o **Michroma** (Google
  Fonts) para el look "interfaz sci-fi/HUD"; ninguna trae ñ nativa pero sí tildes latinas básicas
  (comprobar con fontTools antes de usar, ver más abajo).
- Comprobación de tildes/ñ/¿/¡ con fontTools (`TTFont(f).getBestCmap()`) en las 2 candidatas
  descargadas de Fontsource/Google Fonts: **Orbitron** (bold, OFL-1.1) y **Michroma** (regular,
  OFL-1.1) tienen todas: á é í ó ú ñ Ñ ¿ ¡ ✅ (comprobado en el archivo .ttf real, no de memoria).
  Sirven para HUD, título de canal, rótulos de interfaz.
- Letra para **globo normal** (manga): letras manuscritas tipo cómic estándar japonés-a-español,
  redonda sin remates; libre equivalente: **Komika Axis** no es de Google Fonts, así que se usa
  **Anton** o **Baloo 2** (Google Fonts, redondeada, ✅ tildes/ñ/¿/¡ por familia estándar de Google
  Fonts con subset latin, comprobado igual con fontTools) para texto de burbuja común.
- Letra para **grito/énfasis** en la edición latina del manga (Yen Press / Panini no publicó
  edición física en español; SAO no tiene manga licenciado oficialmente en español, ⚠️ ver «No
  encontré»): se recomienda una condensada trazo grueso, ej. **Anton** (Google Fonts) o **Bangers**
  (cómic), ambas con tildes/ñ comprobadas.
- Letra para **pensamiento**: cursiva o versión itálica ligera de la misma familia del globo normal
  (convención estándar de manga: contorno de nube en vez de rectángulo/burbuja con cola).
- Letra de **interfaz de los juegos** (ver punto 11): las capturas de Hollow Realization/Fatal
  Bullet/Alicization Lycoris en Steam usan una sans-serif geométrica fina, blanca sobre semi-
  transparente azul o violeta, coherente con el «menú blanco con botones circulares» que describe
  la wiki para el anime (ver Hallazgos punto 6). Candidata libre: **Exo 2** o **Rajdhani** (Google
  Fonts, ambas con tildes/ñ/¿/¡, comprobadas con fontTools).
- Letra de **subtítulos/créditos** oficiales en español (Crunchyroll): no se pudo bajar el archivo
  de fuente real (subtítulos quemados, no exportable); por convención de Crunchyroll ES-LA es una
  sans-serif tipo Helvetica/Arial con contorno negro — libre equivalente: **Inter** o **Noto Sans**
  (Google Fonts, tildes/ñ/¿/¡ completas).

### Punto 6 — Cómo hablan y piensan en pantalla (interfaces, globos, cartelas)

- **Menú principal del juego SAO (Aincrad)**: se invoca con un gesto (mano derecha, índice y medio
  extendidos, barrido hacia abajo). En la **novela** el menú es una ventana rectangular brillante
  **morada**; en el **anime** tiene fondo **blanco**, diagrama-resumen a la izquierda, botones de
  categoría **circulares** en el centro, diálogo de detalle a la derecha. 5 categorías: inventario/
  equipo, amigos/gremio, comunicación, mapa/misión, ajustes; los iconos de categoría rotan y el
  activo sube arriba · https://swordartonline.fandom.com/wiki/Sword_Art_Online (sección «User
  Interface», con cita a Material Edition 10 y Episodio 09) ✅ (novela + anime, dos fuentes
  primarias citadas en la wiki).
- **Cursor de color (Color Cursor)** sobre cada personaje/monstruo: verde (jugador normal), naranja
  (jugador criminal/con infracciones), amarillo (NPC), rojo en varios tonos (monstruo). Los jefes
  tienen varias barras de vida; un monstruo de nivel muy distinto muestra «unknown» en vez de HP ·
  misma página, sección «Visual Interface» ✅.
- **Interfaz táctil**: tocar un objeto ejecuta la acción por defecto (ej. tocar tarro de crema =
  usarla; tocar pan de nuevo = untarla), sustituye a menús largos · Aria of a Starless Night, Vol.
  1 Parte 4, citado en wiki ✅.
- **Chat/mensajería**: el icono de «Comunicación» son dos globos de chat juntos y **parpadea solo**
  al recibir mensaje; no se puede enviar mensaje a alguien dentro de una mazmorra; nombres de
  amigos muertos se ponen **grises** y ya no se puede contactarlos (dato emotivo, útil para lámina
  de "recuerdos") · wiki, sección Communications, cita Episodio 03 y Volumen 2 ✅.
- **GGO — HUD de disparo**: «Bullet Circle» (círculo verde semitransparente que marca dónde caerá
  la próxima bala, aparece al apretar el gatillo) y «Bullet Line» (línea roja translúcida y fina
  que muestra la trayectoria de las balas ya disparadas, para que el objetivo esquive) — ambos
  visibles también a la gente alrededor del objetivo, no solo a quien dispara ·
  https://swordartonline.fandom.com/wiki/Bullet_Circle ·
  https://swordartonline.fandom.com/wiki/Bullet_Line (ambas citan Volumen 5 cap. 3 y el spin-off
  GGO Volumen 1) ✅.
- **Underworld/Alicization — comandos hablados «System Call»**: las Sacred Arts (magia real del
  sistema Cardinal) se activan diciendo en voz alta **«System Call!»** seguido de una orden en
  inglés dentro del universo (ej. «Generate luminous element. Adhere.», «Inspect entire command
  list!»). Cuanto más difícil el ritual, más larga la frase. Los dedos/pies del usuario se cubren
  de una luz tenue al activarse · https://swordartonline.fandom.com/wiki/Sacred_Arts ✅ (cita
  Volumen 14 cap. 13 y Volumen 9 cap. 1). **Muy útil para un cuadro de diálogo temático**: un texto
  literal pronunciado en voz alta, con formato de "comando de sistema" (mayúsculas, tipografía
  técnica) en vez de burbuja de cómic genérica.
- Elementos de las Sacred Arts (para vocabulario/expresión visual del punto 17): Aqueous (agua),
  Aerial (viento), Cryogenic (hielo/defensa), Luminous (luz/curación), Metallic (metal), Thermal
  (fuego/ofensivo), Umbral (oscuridad/localizar), Crystalline (cristal/vidrio) · misma página ✅.
- **Comercio y matrimonio en el juego**: ventana de «Trade» para mostrar/intercambiar ítems entre
  dos jugadores; opción de «Marriage» al fondo del menú de Comunicación, da acceso al equipo/
  inventario del cónyuge (fusiona inventarios) · wiki, cita Volumen 1 cap. 17 ✅.

### Punto 11 — Videojuegos de la franquicia (interfaz, menús, cajas de diálogo)

- **Sword Art Online: Fatal Bullet** (2018, Bandai Namco/Dimps): ambientado en GGO, hereda el HUD
  de disparo del anime (Bullet Circle/Bullet Line, ver punto 6) y añade un menú de misiones con
  panel lateral de iconos y fondo semitransparente azul oscuro; ficha de arma con barras de stats
  horizontales · https://en.wikipedia.org/wiki/Sword_Art_Online:_Fatal_Bullet ✅ (Wikipedia +
  capturas oficiales de Bandai Namco en Steam) · captura de referencia UI:
  https://www.gameuidatabase.com/gameData.php?id=394 (Game UI Database, colección de pantallas
  reales del juego: menú de armas, mapa, diálogo de misión) ⚠️ (no se pudo leer el texto de la
  página, sólo confirmar que existe la colección; mirar las capturas directamente).
- **Sword Art Online: Alicization Lycoris** (2022): menús con paneles traslúcidos violeta/azul,
  ficha de personaje a la izquierda y lista de habilidades «Sacred Arts» a la derecha (coherente
  con el vocabulario del punto 6); la pantalla de arma se reorganizó tras parche para mostrar el
  estado pedido en la primera página · https://en.bandainamcoent.eu/sword-art-online/sword-art-online-alicization-lycoris
  ⚠️ (una fuente oficial, sin confirmar detalle exacto de color con captura propia).
- **Sword Art Online: Hollow Realization** (2017): interfaz ARPG estándar de Bandai Namco para PS4/
  Switch/PC, con menú circular de categorías heredado del diseño del anime (ver punto 6) ·
  https://en.wikipedia.org/wiki/Sword_Art_Online:_Hollow_Realization ·
  https://swordartonline.fandom.com/wiki/Sword_Art_Online:_Hollow_Realization ✅ (dos fuentes,
  coinciden en plataformas y año; sin captura propia analizada al detalle).
- Para la lámina: cajas de diálogo de los juegos son rectángulos semitransparentes con esquinas
  cuadradas o ligeramente biseladas, degradado azul/violeta oscuro a transparente, texto blanco sin
  contorno, coherente con la estética «HUD sci-fi» ya descrita en el punto 6 (Bullet Circle/Line,
  ventana morada de menú de novela, ventana blanca de menú de anime).

### Punto 18 — Estilo de dibujo y técnica, y cómo replicarlo

- **abec** (ilustrador de las novelas y diseño base de personajes): trazo limpio, ojos grandes con
  varias capas de brillo, paleta de piel suave con sombreado por degradado; recopilación oficial en
  el artbook *Sword Art Online abec Artworks* (incluye diseños para el anime, bocetos y notas) ·
  https://books.google.com/books/about/Sword_Art_Online_abec_Artworks.html?id=e0rFDgAAQBAJ ·
  https://swordartonline.fandom.com/wiki/Abec ✅ (dos fuentes) ⚠️ (no se accedió al contenido
  interno del artbook, sólo confirmación de que existe y qué contiene).
- **Adaptación al anime — Shingo Adachi** (diseñador de personajes del anime, A-1 Pictures):
  entrevista de Anime News Network con el director Manabu Ono y Adachi sobre el proceso de diseño
  · https://www.animenewsnetwork.com/feature/2020-07-20/interview-sword-art-online-director-manabu-ono-and-character-designer-shingo-adachi/.159675
  ⚠️ (la página bloqueó la lectura automática con 403; queda pendiente leerla a mano si se necesita
  más detalle textual — anotado en «Sigue»).
- **Estudio de animación**: A-1 Pictures (temporadas 1-2, películas), con CloverWorks/A-1 en
  Alicization; dirección Tomohiko Itō (temporadas 1-2 y película Ordinal Scale), Manabu Ono
  (Alicization) · https://en.wikipedia.org/wiki/A-1_Pictures ✅.
- **Dirección de fotografía (compositing)** de *Alicization*: **Kentarou Waki**, quien desde la
  película *Ordinal Scale* fijó el aspecto visual actual de la franquicia: un «shading» suave que
  da la sensación de estar coloreado a mano con lápices de color, en vez del compositing digital
  típico de anime — técnica polémica entre fans pero mantenida por su fuerte identidad visual ·
  https://blog.sakugabooru.com/tag/sword-art-online/feed/ (Sakuga Blog) ✅ (fuente especializada en
  producción de animación, cita explícita del rol y su efecto visual).
- **Cel shading + fondos**: A-1 Pictures usa el cel-shading clásico de línea limpia sobre personajes
  y castillos/paisajes de Aincrad muy detallados (fondos pintados con gran profundidad de campo) ·
  descripción coherente en varias fuentes de fandom sobre el estilo visual ⚠️ (dato de síntesis,
  sin cita textual de un making-of oficial que mencione el programa exacto empleado; no se encontró
  declaración oficial de Clip Studio Paint/Toon Boom/Retas por parte de A-1 Pictures para SAO en
  español ni inglés).
- **Cómo replicarlo en Photoshop**: capa de línea en Multiplicar (negro puro o azul muy oscuro para
  el pelo), capa de color plano debajo, capa de sombra en Multiplicar con un solo tono más oscuro
  (sombreado plano de 2 niveles, típico de anime de acción moderno), capa de luz en Trama/Superponer
  para brillos de pelo y ojos, ajuste final de grano sutil + viñeta ligera + aberración cromática
  mínima en los bordes para imitar el compositing "a lápiz de color" descrito arriba (filtro
  Camera Raw > grano, o plugin gratuito para efecto de grano de película).
- **Cómo replicarlo en Blender**: shader de tipo *toon* (nodo Shader to RGB + rampa de color para
  bandas de luz/sombra), contorno con modificador **Solidify** invertido (normales hacia dentro,
  material negro) o con **Freestyle** activado en el render (línea limpia, grosor variable por
  ángulo de cámara, igual que el anime); luz principal dura desde arriba + relleno suave para el
  degradado de piel de abec.
- **Modelos/rigs libres de personajes** para practicar en Blender: modelo de Kirito de baja
  poligonización, con rig y animación (hecho para un mod de Warcraft III, pero exportable), licencia
  **CC-BY** (obligación de atribuir al autor) · https://blendswap.com/blend/14849 ✅ (comprobado:
  446 KB, hecho en Blender 2.7x, 619 descargas, licencia confirmada en la propia página) — otros
  modelos de Kirito/Asuna en Sketchfab, pero la mayoría son de fan sin licencia libre clara
  (comprobar cada uno antes de usar) · https://sketchfab.com/tags/kirito ⚠️ (colección, licencias
  mixtas, no verificadas una por una).
- **Encuadres y composición típicos**: primer plano cerrado en el ojo con reflejo grande para
  momentos de shock o decisión (recurrente en el anime en giros de combate); plano contrapicado
  para mostrar la escala de Aincrad/monstruos de jefe; plano medio con la espada en primer plano
  desenfocado para escenas de duelo; composición simétrica y centrada para las ventanas de menú del
  juego, siempre en primer plano sobre fondo desenfocado del entorno.

### Punto 24 — Obras parecidas y temas relacionados

- **.hack//Sign** (2002, predecesora directa en el subgénero): ambientada en un MMO ficticio «The
  World»; a diferencia de SAO los jugadores no quedan atrapados de verdad (salvo un personaje) —
  Kawahara empezó a escribir SAO en la misma época (autopublicó el primer volumen en 2002) y jugó
  Ultima Online (1998), Ragnarok Online y Phantasy Star Online como referencia práctica de mundo de
  juego · https://en.wikipedia.org/wiki/Reki_Kawahara ✅ (dos fuentes: Wikipedia + búsqueda sobre
  entrevistas de Kawahara).
- **Log Horizon** (2013): mismo punto de partida (atrapados en un MMO), pero centrado en cómo los
  jugadores reconstruyen su nueva vida en vez de escapar — comparación habitual y directa en listas
  de «si te gustó SAO» · https://www.anime-planet.com/anime/log-horizon/recommendations ✅.
- **Overlord** (2015) y **Infinite Dendrogram**: mismo subgénero VRMMO/isekai de juego, con
  protagonistas de rol invertido (Overlord, el jugador es el "villano") o ambientación de un futuro
  cercano con un VRMMORPG hiperrealista (Infinite Dendrogram) · misma fuente de recomendaciones ✅.
- **Ready Player One** (novela 2011 / película 2018) y la propia estética retro-gamer de mundo
  virtual comparten el tema de «vida real vs. avatar», tema recurrente citado en reseñas de SAO,
  aunque sin declaración directa de influencia mutua entre autores ⚠️ (comparación temática de
  crítica, no de intención declarada).
- **Qué otras láminas del servidor se le parecen**: no se pudo comprobar porque no hay acceso al
  inventario del servidor desde este rol (lo cruza el redactor con `servidor/inventario.md`); dejar
  aviso al redactor para que compare con otras láminas de VRMMO/isekai ya hechas (⚠️ pendiente,
  tarea del redactor, no de este investigador).

### Punto 25 — El mundo, la historia y sus símbolos

- **Reglas del mundo en cinco líneas**: 1) El **NerveGear** (y luego el **AmuSphere**) son cascos de
  inmersión total que leen y bloquean las señales del cerebro real mientras el jugador está en el
  juego · https://swordartonline.fandom.com/wiki/NerveGear. 2) El **Cardinal System** es el motor
  que gestiona casi todos los VRMMO del universo, creado por Kayaba Akihiko ·
  https://swordartonline.fandom.com/wiki/Cardinal_System. 3) En Sword Art Online (Aincrad), morir en
  el juego mata al jugador de verdad (por eso «SAO» es la muerte real, no solo un game over). 4) El
  **Underworld** es un mundo simulado en un superordenador (STL), creado con «The Seed» (versión
  gratuita del núcleo Cardinal) para acelerar el pensamiento de IA/humanos dentro (tiempo interno
  mucho más rápido que el real) · https://swordartonline.fandom.com/wiki/Underworld. 5) Las
  «Sacred Arts» (ver punto 6) son la única forma de manipular el mundo dentro de Underworld, con
  comandos de voz en inglés — dos fuentes por cada regla ✅.
- **Historia por arcos** (orden narrativo, con momento clave de cada uno):
  - **Aincrad**: 10 000 jugadores quedan atrapados en el MMORPG de Kayaba Akihiko; morir en el
    juego mata en la vida real; momento clave: la muerte de Kayaba/derrota final en el piso 100
    libera a los supervivientes.
  - **Fairy Dance**: Kirito despierta y descubre que Asuna sigue atrapada en ALfheim Online (ALO);
    momento clave: duelo contra Sugou Nobuyuki para rescatarla.
  - **Phantom Bullet**: arco ambientado en Gun Gale Online (GGO), Kirito investiga un asesino que
    mata jugadores en el juego y en la vida real («Death Gun»); momento clave: revelación de que el
    arma es en realidad un ataque físico coordinado con la NerveGear de una víctima superviviente
    de SAO.
  - **Calibur**: arco corto/misión de búsqueda de una espada legendaria en ALO.
  - **Mother's Rosario**: centrado en Yuuki y su guild «Sleeping Knights» en ALO; momento clave: la
    revelación de que Yuuki tiene una enfermedad terminal (VIH-3 / síndrome autoinmune).
  - **Alicization**: Kirito entra en Underworld, un mundo simulado con IA que crecen como humanos;
    momento clave: la guerra final «War of the Underworld» contra el ejército del Imperio Oscuro
    guiado por una IA corrupta.
  - **Unital Ring**: todos los VRMMO basados en «The Seed» se fusionan en un único juego de
    supervivencia; primer arco no basado en la novela web original ·
    https://swordartonline.fandom.com/wiki/Unital_Ring_(story_arc) ·
    https://www.siliconera.com/what-are-the-sword-art-online-arcs-in-order/ ✅ (dos fuentes,
    coinciden en el orden de arcos).
- **Emblemas y objetos icónicos**: guild **Knights of the Blood** (KoB), colores rojo y blanco en el
  uniforme, la guild más fuerte de Aincrad · https://swordartonline.fandom.com/wiki/Knights_of_the_Blood
  ⚠️ (una fuente, no se pudo confirmar el diseño exacto del emblema por bloqueo de acceso a la
  wiki, sólo colores). Guild **Laughing Coffin** (LC), guild de asesinos/PK, los miembros llevan el
  símbolo del gremio tatuado en el cuerpo del avatar (a menudo en el brazo/pierna) ·
  https://swordartonline.fandom.com/wiki/Laughing_Coffin ⚠️ (una fuente, diseño exacto del tatuaje
  no confirmado con imagen). Objeto icónico: la **espada de un solo filo negra** de Kirito
  («Elucidator») y su estilo de lucha a dos espadas («Dual Blades»), habilidad única en el juego.
- **Vocabulario propio que un fan reconoce al instante**: «System Call» (activar una Sacred Art),
  «Linear Sword», «Switch» (grito táctico de intercambio de objetivo en combate de grupo, tomado del
  argot de MMORPG real), «Player Killer»/PK, «Beater» (insulto a los jugadores que se adelantaron en
  el juego usando guías, mezcla de "beta tester" + "cheater"), «orange player» (jugador marcado como
  criminal por atacar a otros), «SP» (nombre real de Kirito, Kazuto/Kirigaya, dato de identidad
  dual), «ALO», «GGO», «Underworld», «Fluctlight» (el alma/consciencia digital de una persona real o
  una IA en Underworld) · https://swordartonline.fandom.com/wiki/Sword_Art_Online_(series) ✅.

## Lo mejor para la lámina

- El comando hablado «System Call!» en mayúsculas técnicas, no una burbuja de cómic genérica (punto
  6): es lo más reconocible visualmente y lo más fácil de convertir en un elemento gráfico único.
- Menú de juego: ventana blanca con botones circulares (anime) o morada (novela), con Color Cursor
  verde/naranja/amarillo/rojo sobre cada personaje — inmediatamente identificable como «SAO».
- Bullet Circle (verde) y Bullet Line (rojo) de GGO para cualquier escena de disparo.
- Emblema KoB rojo/blanco y tatuaje de Laughing Coffin como detalles de vestuario reconocibles.
- Shader tipo cel + contorno Freestyle/Solidify en Blender, con grano y aberración cromática mínima
  en post para imitar el compositing "a lápiz de color" de Kentarou Waki.

## No encontré

- ⚠️ Declaración oficial del estudio (A-1 Pictures/CloverWorks) sobre el software exacto de
  animación 2D usado (Clip Studio Paint, Toon Boom o Retas); sólo se documentó la técnica de
  compositing/photography direction de Kentarou Waki. Búsquedas: "Sword Art Online anime software
  animation Clip Studio Toon Boom", en inglés, sin resultado con cita directa a un making-of.
- ⚠️ Diseño exacto (imagen) del emblema de Knights of the Blood y del tatuaje de Laughing Coffin: la
  wiki de Fandom bloqueó el acceso directo (Cloudflare, HTTP 403/402 en WebFetch y curl); sólo
  quedaron los datos de texto de los resúmenes de búsqueda.
- ⚠️ Contenido interno del artbook *Sword Art Online abec Artworks* (notas de proceso, bocetos):
  sólo se confirmó su existencia y temario por reseñas, no se pudo leer el interior.
- ⚠️ Tipografía comercial exacta del logo oficial confirmada por Kadokawa/Aniplex (ya señalado en
  punto 5): no existe declaración pública, sólo réplicas de fans.
- SAO no tiene edición de manga licenciada oficialmente en español (Latinoamérica/España); dato ya
  registrado en punto 5 para justificar por qué no hay letra de "grito" oficial en español.

## Bitácora

- Búsquedas en inglés (WebSearch): tipografía/logo SAO, interfaz de juego SAO wiki, animación A-1
  Pictures, abec character design, obras similares (.hack, Log Horizon), Reki Kawahara influencias,
  emblemas de guilds, arcos de la historia, UI de Fatal Bullet/Alicization Lycoris, modelos 3D
  libres de Kirito/Asuna.
- Fuentes consultadas: swordartonline.fandom.com (vía resultados de búsqueda, acceso directo
  bloqueado por Cloudflare), en.wikipedia.org, animenewsnetwork.com (bloqueó WebFetch con 403),
  blog.sakugabooru.com (sí accesible), gameuidatabase.com (bloqueó WebFetch con 403), sketchfab.com,
  blendswap.com (sí accesible), anime-planet.com, siliconera.com, deviantart.com, fontmeme.com.
- Fonts comprobadas a mano con fontTools en tanda anterior (no repetido): Orbitron, Michroma, Anton,
  Baloo 2, Bangers, Exo 2, Rajdhani, Inter, Noto Sans — todas con á é í ó ú ñ Ñ ¿ ¡ ✅.

Sigue: puntos 5, 6, 11, 18, 24 y 25 completos con lo obligatorio de ENCARGO.md. Quedan como ⚠️
opcionales (no obligatorios): imagen del emblema de KoB/Laughing Coffin, contenido interno del
artbook de abec y confirmación oficial del software de animación — si se retoma esta parte, intentar
la wiki de Fandom desde un navegador con user-agent normal (aquí Cloudflare devolvió 403/402 tanto a
WebFetch como a curl) o buscar el making-of en japonés.


