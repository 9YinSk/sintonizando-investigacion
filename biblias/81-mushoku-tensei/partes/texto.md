# Parte de TEXTO, JUEGOS Y TÉCNICA · Mushoku Tensei: Jobless Reincarnation (encargo 81)

Investigador de texto: puntos 5, 6, 11, 18, 24 y 25 de `ENCARGO.md`. Libreta de
datos (no prosa), un dato por línea. Parte de `partes/datos-texto.md` (no se
repiten esas consultas: AniList, staff, obras parecidas, capturas de Steam).
Título oficial: "Mushoku Tensei: Jobless Reincarnation" (AniList id 108465).
Wiki de Fandom: `mushokutensei.fandom.com` (en inglés; no hay wiki grande en
español). Imágenes originales bajadas a `/tmp/claude-0/trabajo/81-mushoku-tensei-texto/`
(manga/, juego/, mundo/, lugares/, fuentes/) — se mira cada una con Read antes
de describirla, no de memoria.

## Punto 5 · Tipografía

### Logo (manga/novela, medido con Pillow sobre la portada del tomo 1)
- Portada del manga tomo 1 (edición en inglés de Seven Seas) · 1403×2000 ·
  https://static.wikia.nocookie.net/mushokutensei/images/5/52/Engch01.jpg ·
  Fandom Wiki · ✅ (vista en detalle, recorte del logo en `manga/logo_crop.png`)
- El logo **no es una fuente**: es rotulado a mano, con trazo de pincel
  irregular y grosor variable. «Mushoku» va en **negro casi puro** (medido
  `#060606`), «Tensei» mezcla negro y un **dorado/bronce con textura de pincel**
  (medido `#A3721C`, con variación visible dentro de cada letra — no es un
  color plano). Todas las letras llevan un **halo blanco fino** para que
  resalten sobre el fondo ilustrado. El subtítulo «jobless reincarnation» va
  en cursiva negra, más pequeña y condensada, con la misma familia de trazo
  a mano. ✅ (medido directamente).
- El logo internacional (el de Seven Seas Entertainment en EN, distinto del
  logo japonés 無職転生) está vectorizado en Wikimedia Commons como CC0, pero la
  página no dice qué fuente base se usó (puede ser rotulado a mano también) ·
  https://commons.wikimedia.org/wiki/File:Mushoku_Tensei_international_logo_(with_colour_gradient).svg
  · ✅ existencia del archivo, ⚠️ no identifica la fuente.
- Búsqueda en el foro de dafont sobre el logo: el único hilo que existe
  («Mushoku Tensei Font?», 2016) se quedó **sin respuesta**, no identifica nada
  · https://www.dafont.com/forum/read/272951/mushoku-tensei-font · ✅ (el hilo
  existe y está vacío; no es que no lo haya buscado, es que nadie lo contestó).
- **Letra libre más parecida propuesta** (no hay una réplica exacta porque es
  rotulado a mano): **Luckiest Guy** (Google Fonts, gruesa, redondeada,
  irregular, con textura de trazo grueso parecida al «Mushoku» negro) para
  títulos cortos. Comprobada con fontTools: **trae á é í ó ú ñ Ñ ¿ ¡** ✅
  (`fuentes/luckiestguy.ttf`, cmap completo). ⚠️ es una aproximación mía, no
  una identificación confirmada del rotulista original.

### Interfaz del videojuego (Quest of Memories, medido en captura de Steam)
- Nombre del personaje en una **pestaña ovalada** con degradado marrón oscuro
  a bronce, filete dorado fino y **filigrana bronce pálida** a los lados del
  nombre (motivo vegetal, no geométrico). Texto del nombre y del diálogo en
  **blanco, en una serif redondeada** (no sans). Caja de diálogo: panel
  traslúcido verde oliva/marrón muy oscuro con un **patrón de hojas de hiedra
  en relieve** de fondo (el mismo motivo vegetal que aparece en el escudo de
  Asura, ver punto 25) · recorte `juego/dialogobox_crop.png`, paleta medida
  con `estilo.py`: `#1F180E` 35% · `#31291B` 21% · `#483C2C` 20% · `#5E5443`
  17% · `#837C71` 7%, línea `#272015` ✅ (medido).
- No identifiqué la fuente serif exacta del juego con certeza ⚠️. **Letra
  libre propuesta**: una serif clásica suave tipo **PT Serif** o **Source
  Serif 4** (Google Fonts) para el cuerpo del texto, y **Cinzel** (comprobada
  con fontTools: trae á é í ó ú ñ ¿ ¡ ✅) para el nombre del hablante si se
  quiere un aire más noble/medieval.
- Menú de batalla: panel oscuro redondeado arriba a la izquierda con
  **ATTACK / SKILL / ITEM / GUARD / ESCAPE** en mayúsculas, cada uno con
  icono; abajo, **retratos circulares con barras HP/SP** por personaje. Botón
  de turno automático arriba a la derecha (AUTO/SKIP, iconos de mando). ✅
  (visto en capturas de Steam, contacto en `juego/contacto.jpg`).
- Minijuego de gestión del restaurante (dentro del mismo juego): contador de
  recursos arriba (iconos + número, `50/50`), reloj con hora del día, y una
  tarjeta **«MAIN GOAL»** con casilla de objetivo — letra de palo (sans) ahí,
  distinta a la serif del diálogo. Vista isométrica del local (mesas, barra,
  personajes chibi de cliente). ✅ (visto).
- No hay **localización al español** en ningún juego de la franquicia: Quest
  of Memories sólo trae inglés, chino tradicional y japonés (con doblaje sólo
  en japonés) · `datos-texto.md` (Steam) · ✅.

### Globos, gritos y pensamientos (manga)
- Busqué una página de manga con globo y texto visible dentro del wiki: la
  única imagen de interior de manga con globo que encontré («Silver Palace»,
  tomo 8, cap. 38) tiene los **globos vacíos** — parece un recorte hecho para
  usarse como referencia de fondo, sin el diálogo (la wiki no aloja páginas
  completas por derechos) · `manga/silver_palace_rgb.png` · ✅ la forma del
  globo (óvalo de trazo fino, limpio), ⚠️ no pude ver la letra usada dentro.
- Por lo mismo, **no pude confirmar directamente** cómo se dibujan el globo de
  grito, el de pensamiento ni la onomatopeya en esta obra concreta (búsquedas:
  TV Tropes bloqueado por Cloudflare, TCRF bloqueado por Cloudflare, la web de
  Seven Seas da 403, ANN da 403 — cuatro intentos, dos webs distintas cada
  vez). Lo dejo en «No encontré», no lo invento.
- **Dato fuerte y verificado en su lugar**: en el ANIME, los pensamientos de
  Rudeus **no se muestran con un cuadro ni un globo**: se resuelven por
  actuación de voz. El director Okamoto usa **dos actores distintos**:
  Tomokazu Sugita para los pensamientos internos de Rudeus y Yumi Uchiyama
  para lo que dice en voz alta, para marcar su doble edad mental (34 años por
  dentro, niño por fuera) sin necesidad de un rótulo en pantalla ✅
  (Wikipedia: https://en.wikipedia.org/wiki/Mushoku_Tensei_(TV_series) ).
  **Importante para el punto 17/lámina**: si se pone a Rudeus «pensando», no
  hace falta una nube de pensamiento clásica — la serie ya resuelve esto de
  otra forma; puede ir con letra más pequeña/cursiva sin globo, como
  monólogo interior de novela.
- **Letra libre para globos** (si hace falta rotular en español encima de una
  imagen): mismo estándar ya usado por el equipo en otras biblias del
  servidor, **Anime Ace 2.0 BB** (Blambot, gratis, con tildes) — no lo repito
  del catálogo del punto 5 de dafont porque ya está documentado en
  `biblias/_ya_hechas/_Cuadros de dialogo por franquicia (23-sep-2026).md`.

### Cartelas del mundo (rótulos in-universo)
- Busqué un tablón de misiones o cartel del Gremio de Aventureros con texto
  legible en la wiki (imágenes de la sede en Millishion y de las
  recepcionistas): las capturas disponibles muestran el edificio y al
  personal, **no hay un plano cerrado del tablón/cartel con letra visible** ·
  `lugares/guild_small.jpg` (edificio gótico blanco, sin cartel legible) · ⚠️
  no encontrado, no es que no exista.
- El «cartel del mundo» más claro y verificable que sí encontré es el
  **mural hexagonal de piedra** del Mundo de Seis Caras (ver punto 25): tallas
  con una escritura rúnica inventada en las columnas laterales, sin
  equivalente latino real — es simbólico, no alfabeto utilizable. ✅.

### Subtítulos y créditos
- No encontré una captura fiable de la tipografía exacta de los créditos o
  del rótulo de "Próximo episodio" del anime (búsquedas en la wiki y en
  Google no devolvieron una imagen clara del cartel de créditos) ⚠️. Lo que sí
  es dato firme: el opening **no es un solo tema fijo**: la primera temporada
  usó **cinco openings distintos** como música de fondo narrativa en vez del
  típico OP con animación de créditos — esto afecta a cómo se leería un
  «créditos» en una lámina (no hay una única cartela de OP que copiar) ✅
  (Wikipedia, artículo del anime).

## Punto 6 · Cómo hablan y piensan en pantalla

- **Resumen** (lo más importante del encargo, según sus propias palabras): la
  caja real de esta franquicia, si hay que elegir una, es la del **videojuego
  de rol tipo visual novel** — pestaña de nombre ovalada en bronce con
  filigrana vegetal + panel traslúcido oscuro con relieve de hiedra — no una
  burbuja de cómic genérica. Es la única «caja de diálogo» que pude ver
  completa y con texto real dentro. ✅ (ver punto 5, `juego/dialogobox_crop.png`).
- El manga usa **globos ovalados de trazo fino y limpio**, estilo shōnen/seinen
  estándar, sin decoración añadida (comprobado por la forma vacía del globo en
  `silver_palace_rgb.png`) ✅ forma, ⚠️ letra interior no verificada.
- Los pensamientos de Rudeus en el ANIME se resuelven **con un segundo actor
  de doblaje**, no con un cuadro de texto ni una nube (ver punto 5) ✅. Esto es
  un dato importante para «qué NO hacer»: poner una nube de pensamiento
  clásica encima de Rudeus sería menos fiel que, por ejemplo, un texto en
  cursiva sin globo, tipo monólogo de novela ligera (la obra nació como
  novela web, con monólogo interior en prosa) ⚠️ (inferencia razonable a partir
  del formato origen, no una fuente que lo diga explícitamente para la
  presentación en pantalla).
- **Qué no hacer con la caja de diálogo**: una burbuja blanca lisa de cómic
  occidental. La caja «canon» de la franquicia (juego oficial) es oscura,
  con textura y motivo vegetal, no blanca ni geométrica ✅.

## Punto 11 · Videojuegos de la franquicia

- **Mushoku Tensei: Jobless Reincarnation — Quest of Memories** (LANCARSE
  Ltd., 19 jun 2024, PC/Steam) · https://store.steampowered.com/app/2459420 ·
  ✅ (Steam, ya en `datos-texto.md`). Mezcla **tres interfaces distintas**:
  1) diálogo tipo visual novel (ver punto 5); 2) combate por turnos clásico de
  JRPG (menú ATTACK/SKILL/ITEM/GUARD/ESCAPE, retratos con HP/SP); 3) gestión
  de un restaurante en vista isométrica (contador de recursos, reloj,
  objetivos). Sin doblaje ni texto en español; audio sólo en japonés ✅.
- **Mushoku Tensei: I'll Seriously Try Even If It's Made Into a Game**
  (無職転生 ～ゲームになっても本気だす～), gacha para Android/iOS de **Aiming Co.,
  Ltd.**, publicado por Beaglee, gratis con micropagos. Anunciado el
  10-oct-2020, salió el 27-mar-2021 y **cerró el servicio el 31-ago-2022**
  (ya no se puede jugar) · https://mushokutensei.fandom.com/wiki/Mobile_Game ·
  ✅ (wiki, con enlace a la noticia oficial japonesa de octubre de 2020).
  - Presentación tipo **visual novel parcialmente doblada**, con
    **retratos Live2D animados** para los personajes jugables y retratos 2D
    estáticos para los secundarios; reutiliza escenas del anime.
  - Combate: equipo de 3 personajes + apoyo de otro jugador contra oleadas;
    ataque normal automático, el jugador controla 2 habilidades especiales
    por personaje.
  - Invocación (gacha) con la moneda «Phantom Stones»; rareza de personajes
    3★ (común) a 5★ (raro).
  - Cubría hasta el volumen 3 de la novela ligera antes de cerrar, e incluía
    escenarios exclusivos supervisados por el propio autor (Rifujin na
    Magonote), no canónicos del todo.
  - Imagen promocional del juego · 1024×538 ·
    https://static.wikia.nocookie.net/mushokutensei/images/b/b4/Mobile_game_visual.jpg
    · Fandom Wiki · ✅.
- **No encontré** contenido de The Cutting Room Floor para ningún juego de la
  franquicia: `tcrf.net` devuelve un reto de Cloudflare (Just a moment...) con
  `curl` normal y con user-agent de navegador — dos intentos, no lo salté con
  herramientas de terceros ⚠️. Es razonable que no haya página: son juegos
  pequeños/de licencia y TCRF se centra en juegos con más arqueología de
  datos.

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

### Quién hace el arte y con qué enfoque (equipo, de `datos-texto.md` + ampliado)
- Diseño de personaje original (novela/manga): **Shirotaka** (シロタか) ·
  AniList ✅. Diseño de personaje del anime: **Kazutaka Sugiyama** (S1),
  **Sanae Shimada** (S2), **Ryōta Furukawa** (S3) — el diseño cambia de
  responsable por temporada, lo que explica pequeñas diferencias de trazo
  entre temporadas ✅ (AniList para S1; Wikipedia para S2/S3, dos fuentes
  independientes que coinciden en el nombre de S1).
- Director de arte (fondos): **Masakazu Miyake** (三宅昌和), especialista de
  fondos de largo recorrido en el estudio ✅ (AniList + Real Sound, dos
  fuentes: https://realsound.jp/movie/2021/10/post-892127_2.html ).
- Diseño de color: **Makiko Doi** (土居真紀子) · AniList ✅.
- Estudio: **Studio Bind**, fundado en **noviembre de 2018** como empresa
  conjunta de White Fox y Egg Firm **sólo para producir este anime** con
  continuidad a largo plazo (no es un estudio genérico que reparte
  encargos) ✅ (Wikipedia: https://en.wikipedia.org/wiki/Studio_Bind ,
  animesenpai.net).

### El estilo tal cual se ve (verificado mirando las imágenes, no de memoria)
- Fondos **pintados con degradado**, sin tramas de línea dura: cielo, piedra y
  vegetación se resuelven con manchas de color suaves y mucho detalle
  arquitectónico (columnas, vidrieras, gárgolas) en vez de líneas gruesas ✅
  medido con `estilo.py` sobre el mural del Mundo de Seis Caras: paleta
  `#4F544C` 21% `#6B6B5F` 21% `#878476` 20% `#333A34` 14% `#A7A191` 14%
  `#D6CBB9` 9%, línea `#5C5E56`, saturación 14% (colores casi monocromos,
  piedra), brillo 47%.
- El **color de personaje** (portada de manga a color) es más saturado y con
  **mucha línea** (borde de tinta grueso alrededor de las figuras, casi nada
  alrededor de los fondos): paleta `#3D3438` 25% `#D9B796` 19% `#0570B4` 18%
  `#977D66` 17% `#EBEBE3` 16% `#71C1D8` 4%, línea `#696558`, saturación 44%,
  brillo 66% — medido con `estilo.py`.
- Crítica especializada (Real Sound, en japonés, ✅ segunda fuente en otro
  idioma) describe el resultado como «美術へのこだわり» (obsesión por el arte):
  paisajes rurales bajo cielos abiertos, arquitectura tratada con
  solemnidad, ciudades bulliciosas y terrenos variados (humedales, dunas),
  con «calidad de textura delicada que transmite un trabajo minucioso». Cita
  que la actriz Yumi Uchiyama preguntó en una entrevista si «esto se puede
  ver en cines», por lo inusual de la calidad para un horario de emisión
  nocturno · https://realsound.jp/movie/2021/10/post-892127_2.html · ✅.
- Cámara: movimientos deliberados y con ritmo, transiciones de foco
  (entrada/salida), desenfoque de movimiento en la acción, coreografía de
  espada y acrobacias cuidada · misma fuente · ✅.
- Cada temporada estrena **opening propio por arco narrativo** (no un único
  OP fijo con créditos), reforzando que cada tramo de la historia tiene su
  propio tratamiento visual · Wikipedia (EN) · ✅.
- **No encontré** qué programa exacto usa el estudio (Clip Studio Paint,
  Photoshop, Retas, 3D con *toon shader*…): probé en japonés («無職転生 美術
  CLIP STUDIO Photoshop SAI 三宅昌和») y en inglés, y sólo salen créditos de
  personal, no herramientas · ⚠️ sin confirmar, no lo invento.

### Cómo replicarlo (propuesta a partir de lo visto, no una instrucción del estudio)
- **Photoshop — fondos**: pintar por capas de color plano grande primero
  (cielo, piedra, vegetación), luego pinceles de textura suave (grano de
  piedra, follaje) en modo Multiplicar al 20-40%, sin contorno duro salvo en
  los bordes arquitectónicos más cercanos a cámara; usar un pincel de trazo
  fino sólo en los detalles góticos (ventanas, gárgolas, filigrana).
- **Photoshop — personajes**: línea de tinta con grosor variable (más gruesa
  en el contorno exterior, fina en pliegues internos), sombreado por
  degradado suave (no tramas planas de anime clásico), un toque de luz de
  borde (*rim light*) cálida en el pelo, como en la portada del manga.
- **Blender**: para un objeto o sitio en 3D (ver `AYUDANTE.md`/`reglas_del_dueno.md`,
  punto 1: «objeto real en un sitio real»), usar contorno con **Freestyle** o
  el modificador **Solidify** invertido para la línea negra variable, y un
  *toon shader* con **dos bandas** (luz/sombra) suavizadas con un pequeño
  degradado, no un corte duro — así se acerca al sombreado «degradado /
  pintado» medido arriba, en vez del plano típico de cel-shading duro.
- El escudo de Asura Kingdom (punto 25) es un objeto heráldico ideal para
  Blender: relieve grabado en piedra o metal, con **Bevel** suave en los
  bordes y una normal map de textura de piedra encima.

## Punto 24 · Obras parecidas y temas relacionados

### Recomendaciones de usuarios (AniList, ya en `datos-texto.md`, no repetido aquí completo)
- Las más votadas: *That Time I Got Reincarnated as a Slime* (460 votos),
  *The Rising of the Shield Hero* (309), *Re:ZERO* (284), *The Eminence in
  Shadow* (184), *Ascendance of a Bookworm* (140), *Frieren* (112) · AniList
  · ✅.

### Influencias reconocidas por el propio autor (Rifujin na Magonote)
- El autor descubrió **Re:Monster** en una librería y esa lectura le dio la
  confianza para publicar en Shōsetsuka ni Narō, lo que llevó directamente a
  Mushoku Tensei · cita textual: «It all began when I discovered a work
  called 'Re: Monster' in a bookstore, and upon reading it, I found it truly
  captivating» · https://animatedtimes.com/it-all-began-when-i-discovered-a-book-called-mushoku-tensei-has-a-very-unlikely-inspiration-according-to-author/
  · ✅.
- Para la construcción del mundo se apoyó en **videojuegos de rol de finales
  de los 80 a inicios de los 2000**: Dragon Quest, Final Fantasy, Legend of
  Mana, Ragnarok Online, y también **Rance** (juego adulto, explica parte del
  tono ecchi) · https://animecorner.me/works-that-inspired-the-author-of-mushoku-tensei/
  · ✅ (coincide con el género/tono descrito en la sinopsis de AniList:
  Ecchi, Fantasy).
- Reconoce la influencia directa de **Re:Zero** en el arco final de la obra ·
  misma fuente (Anime Corner) · ⚠️ una sola fuente para este dato en
  concreto (el resto de influencias sí tiene dos: Anime Corner + Animated
  Times para Re:Monster).
- Otras novelas ligeras citadas como influencia: *Isekai Meikyuu de Harem
  wo*, *Mashou*, *Heal Saikou* · Anime Corner · ⚠️ una fuente.
- Frase del autor sobre su método: toma partes de las historias que le
  gustan y las mezcla en una sola obra · misma fuente · ⚠️.

### Qué otras láminas del servidor se le parecen (para no repetir ideas)
- **Ya tienen biblia terminada** en este mismo repositorio: `03-solo-leveling`
  (1760 líneas) y `33-frieren` (2647 líneas) — ambas isekai/fantasía con
  sistema de magia o poder fuerte. Si la lámina de Mushoku Tensei toca el
  crecimiento mágico de Rudeus, conviene no repetir el enfoque visual ya
  usado para el «Sistema» de Solo Leveling (ventanas holográficas de HUD) ni
  el tono contemplativo/pastel de Frieren ✅ (comprobado: existen esos
  archivos en `biblias/`).
- **Carpetas creadas pero sin biblia todavía** (pendientes, incluidas en el
  mismo lote de encargos): `82-the-rising-of-the-shield-hero`,
  `83-overlord`, `84-no-game-no-life`, `85-sword-art-online-todas`,
  `86-saga-of-tanya-the-evil` — mismo género isekai; cuando se hagan, será
  bueno que ninguna copie el estilo de caja de diálogo elegido aquí ✅
  (comprobado: carpetas existen, sin `biblia.md` dentro todavía).

## Punto 25 · El mundo, la historia y sus símbolos

### Las reglas del mundo en pocas líneas
- El **Mundo de Seis Caras** (六面世界, *Roku-men Sekai*) es un mundo con forma
  de dado: **seis caras**, cada una un mundo regido por un dios (Dragón,
  Demonio, Bestia, Océano, Cielo, Humano), con un séptimo **Mundo Vacío**
  hueco en el centro. Lo creó un moribundo **Dios de la Creación** que no
  tuvo fuerza para hacer un solo mundo estable, así que pegó seis mundos
  deformes entre sí para que se sostuvieran unos a otros ·
  https://mushokutensei.fandom.com/wiki/Six-Faced_World · ✅.
- La **magia** (魔術) usa **maná** (魔力), una energía que todo ser vivo del
  mundo tiene de nacimiento; los invocados de otros mundos (como Rudeus) NO
  tienen maná propio salvo excepciones. El maná se aprendió imitando los
  hechizos de los **altos elfos**, que primero pactaron con espíritus del
  bosque · https://mushokutensei.fandom.com/wiki/Magic · ✅.
- **Rango de los hechizos** (de más débil a más fuerte, confirmado en la
  tabla de la wiki): **Elemental (novato) → Intermedio → Avanzado → Santo →
  Rey → Emperador** · https://mushokutensei.fandom.com/wiki/Magic_Spells ·
  ✅ (tabla con esos rangos verificada por grep del wikitext).
- Hay **razas** además de la humana: elfos, enanos, bestias, dragones,
  demonios y los **migurd** (pelo azul, cuerpo pequeño y aniñado, vida de
  200 años, dejan de crecer jóvenes — la raza de **Roxy**) ·
  https://mushokutensei.fandom.com/wiki/Migurd · ✅.

### La historia por arcos (oficializados por la propia wiki, «Story Arcs»)
- **Parte 1, Infancia**: Arco de la Infancia → Arco del Tutor → Arco del
  Aventurero Novato → Arco del Viaje → Arco del Reencuentro → Arco del
  Regreso a Casa.
- **Parte 2, Adolescencia**: Arco del Aventurero Intermedio → Arco de la
  Universidad → Arco de Recién Casados → Arco de las Hermanas → Arco del
  Laberinto → Arco de la Vida Diaria.
- **Parte 3, Subordinado del Dios Dragón**: Arco de la Invocación → Arco del
  Dios Humano → Arco del Reino de Asura → Arco de los Subordinados → Arco de
  Zanoba → Arco de Cliff → Arco de Zenith → Arco de la Organización.
- **Parte 4, La Batalla Final**: Arco del Cuarto Hijo → Arco de la Batalla
  Final → Arco de Conclusión.
  · https://mushokutensei.fandom.com/wiki/Story_Arcs · ✅ (estructura oficial
  de la wiki, con resumen de cada arco en la fuente).
- **Las tres Guerras Humano-Demonio**: la 1ª y 2ª las libró la Gran
  Emperatriz Demonio **Kishirika Kishirisu** contra la humanidad (con los
  Cinco Grandes Reyes Demonio); la 3ª, la **Guerra de Laplace**, la libró el
  Dios Demonio **Laplace** por rencor propio contra los humanos ·
  https://mushokutensei.fandom.com/wiki/Human-Demon_Wars · ✅.

### Emblemas, objetos icónicos y vocabulario (mirado en imagen, no de memoria)
- **Escudo del Reino de Asura**: dos unicornios rampantes sosteniendo una
  corona sobre una espada envuelta en hiedra, con espigas de trigo abajo y
  una cinta/listón en blanco — heráldica europea clásica, en tinta negra
  sobre blanco (manga) · 725×689 ·
  https://static.wikia.nocookie.net/mushokutensei/images/9/93/Asura-Kingdom-Emblem-MT-MN-V8-Ch40.png
  · Fandom Wiki · ✅ (visto en detalle, `manga/asura_emblem_rgb.png`). El
  mismo motivo de **hiedra** reaparece en el relieve de la caja de diálogo
  del videojuego (punto 5/6) — es un motivo visual recurrente de la realeza
  de Asura que vale la pena repetir en una lámina si el personaje es Eris o
  alguien de esa corte.
- La familia **Greyrat** (la de Rudeus y Eris) es una vieja nobleza de Asura
  dividida en 4 casas — **Notos, Boreas, Euros, Zephyrus** —, cada una con su
  propio emblema; los varones Greyrat son «tristemente famosos» por su
  libido, y el propio wiki lo dice sin rodeos · https://mushokutensei.fandom.com/wiki/Greyrat_Family
  · ✅.
- Los **Siete Grandes Poderes** (七大列強, *Nana Dai-Rekkyō*): los 7 guerreros
  más fuertes del mundo desde el fin de la 2ª Guerra Humano-Demonio. Hay
  **monumentos de piedra** repartidos por el mundo con un «7» tallado y el
  motivo de cada poder alrededor en sentido horario — se actualizan solos
  cuando cambia el ranking · https://mushokutensei.fandom.com/wiki/Seven_Great_Powers
  · ✅.
- **El mural del Mundo de Seis Caras** (visto en el anime S3E13): una losa de
  piedra hexagonal con una figura humana de brazos abiertos en el centro,
  rodeada de 6 círculos (los 6 mundos) y columnas de una **escritura rúnica
  inventada** a los lados, iluminada desde un arco inferior · 1920×1080 ·
  https://static.wikia.nocookie.net/mushokutensei/images/f/fc/MT-AN-S3-E13-PNG-07.png
  · Fandom Wiki · ✅ (visto en detalle, `mundo/mural_small.jpg`; paleta
  medida con `estilo.py`: casi monocroma, grises piedra de `#333A34` a
  `#D6CBB9`).
- **Vocabulario que un fan reconoce al instante**: *Mundo de Seis Caras*,
  *Guerra de Laplace*, *Siete Grandes Poderes*, *Factor de Laplace* (rasgo
  raro de renacer con enorme maná, ligado al alma de Laplace — lo tienen
  Rudeus y Sylphiette), *Hitogami* (el «Dios Humano», antagonista en la
  sombra), *Orsted* (el sucesor del Dios Dragón), *Gremio de Aventureros*,
  *Estilo Espada Dios del Agua* / *Estilo Espada Dios Norte* (escuelas de
  espada) · https://mushokutensei.fandom.com/wiki/Laplace_Factor ,
  https://mushokutensei.fandom.com/wiki/Classes · ✅.
- **Sede del Gremio de Aventureros** en Millishion: catedral gótica blanca
  con múltiples agujas y vidrieras, banderas azules en la entrada · 1920×2080
  · https://static.wikia.nocookie.net/mushokutensei/images/d/d8/MT-AN-S1-E16-PNG-18.png
  · Fandom Wiki · ✅ (visto, `lugares/guild_small.jpg`). Es un **sitio real**
  con función clara (tablón de misiones, mostrador) — encaja con la regla del
  dueño de «objeto/sitio real», aunque no encontré un plano cerrado del
  tablón con texto legible (ver punto 5).

## Lo mejor para la lámina

1. El **escudo de Asura** (unicornios + espada entre hiedra) como relieve
   tallado en Blender, si el canal encaja con un personaje noble (Eris,
   Ariel) — motivo de hiedra reutilizable en bordes del canal.
2. La **caja de diálogo del videojuego** (pestaña bronce + filigrana vegetal
   + panel de hiedra) es la referencia más fiel para «cómo habla» la
   franquicia — mejor que una burbuja de cómic genérica.
3. El **mural del Mundo de Seis Caras** como objeto de piedra en Blender
   (relieve + luz rasante) si el canal necesita transmitir «reglas del
   mundo» o misticismo.
4. Para Rudeus pensando: **sin nube de pensamiento** — cursiva sin globo,
   como monólogo de novela (la serie resuelve esto con doblaje, no con
   texto en pantalla).
5. Interfaz de rango de magia (Elemental → Intermedio → Avanzado → Santo →
   Rey → Emperador) como sistema de insignias/barras si el canal necesita
   mostrar progreso o niveles.

## No encontré

- ⚠️ La fuente exacta del logo «Mushoku Tensei» (rotulado a mano; el único
  hilo de dafont sobre el tema quedó sin respuesta desde 2016).
- ⚠️ La fuente exacta de los diálogos del videojuego Quest of Memories (sólo
  propuesta libre aproximada).
- ⚠️ Cómo se dibujan el globo de grito, el de pensamiento y la onomatopeya en
  el manga concreto de esta obra: las páginas de interior con texto no están
  alojadas en la wiki por derechos, y TV Tropes / TCRF / la web de Seven Seas
  / Anime News Network dieron 403 o el reto de Cloudflare en los intentos
  hechos (dos intentos cada uno, sin saltarme el bloqueo con herramientas de
  terceros).
- ⚠️ Qué programa de dibujo/animación usa exactamente Studio Bind (Clip
  Studio, Photoshop, Retas…): búsquedas en japonés e inglés no lo confirman,
  sólo dan créditos de personal.
- ⚠️ Un cartel o tablón in-universo con texto legible (el Gremio de
  Aventureros aparece de lejos, sin plano cerrado del tablón).
- ⚠️ La tipografía exacta de los créditos/cartela de «próximo episodio» del
  anime.
- Esto son datos que faltan por bloqueo de fuente o por derechos de autor de
  las páginas de manga, no cosas que no busqué: cada uno lleva las búsquedas
  hechas arriba.

## Bitácora de búsqueda

- Wiki de Fandom (`mushokutensei.fandom.com`), API `action=parse&prop=wikitext`,
  en inglés: páginas Seven Great Powers, Asura Kingdom, Greyrat Family,
  Adventure Guild, Classes, Magic, Six-Faced World, Races, Human-Demon Wars,
  Gods, Story Arcs, Timeline, Magic Spells, Migurd, Laplace Factor, Superd,
  Mobile Game, y la portada/panel del manga (Chapter 1, Silver Palace,
  Asura Kingdom Emblem). ✅ fuente principal para puntos 25 y parte del 11.
- Imágenes bajadas y miradas con Read (no descritas de memoria): portada de
  manga EN/JP, panel «Silver Palace», escudo de Asura, mural del Mundo de
  Seis Caras, sede del Gremio en Millishion, 5 capturas de Steam de Quest of
  Memories (más contacto), recorte del logo, recorte de la caja de diálogo
  del juego.
- `herramientas/estilo.py`, 4 veces: captura de Steam completa, recorte de
  caja de diálogo, portada de manga a color, mural de piedra — paletas y
  grosor de línea medidos, no inventados.
- `fontTools` sobre 8 fuentes bajadas de Google Fonts (Luckiest Guy, Cinzel,
  IM Fell English, Special Elite, MedievalSharp, Uncial Antiqua, Metal
  Mania, Pirata One): las 8 traen á é í ó ú ñ Ñ ¿ ¡ completos.
- WebSearch (cupo usado: 9 de ~50): "Mushoku Tensei anime logo font
  typeface" (en); "Mushoku Tensei Studio Bind art style making of interview
  3DCG background" (en); "無職転生 アニメ 美術監督 背景 インタビュー 制作" (ja);
  "Mushoku Tensei anime cel shading toon shader CGI background technique
  interview" (en); "無職転生 アニメ 美術 CLIP STUDIO OR Photoshop OR SAI 三宅昌和
  美術監督" (ja); "Rifujin na Magonote interview influences inspiration
  Mushoku Tensei" (en); más 3 WebFetch directos a artículos encontrados.
- WebFetch: Wikipedia (Mushoku Tensei TV series, Studio Bind), Real Sound
  (ja, art article), dafont forum, Wikimedia Commons (logo SVG), Anime
  Corner (influencias), Animated Times (Re:Monster), Anime News Network
  (403, bloqueado), ddnavi.com (403 directo y por Wayback, bloqueado),
  Seven Seas Entertainment (403), TV Tropes (403 Cloudflare), TCRF (403
  Cloudflare), MyAnimeList (404, ID incorrecto).
- Webs bloqueadas y no insistidas más de dos veces cada una: Anime News
  Network (403), ddnavi.com (403), Seven Seas Entertainment (403), TV
  Tropes (Cloudflare), TCRF (Cloudflare), GitHub raw de Google Fonts (403,
  se resolvió bajando de `fonts.gstatic.com` en su lugar, que sí funcionó).

## Cumplimiento de mis puntos (5, 6, 11, 18, 24, 25)

Parte terminada: los 6 puntos tienen lo obligatorio (logo medido, caja de
diálogo real del videojuego con paleta medida, dos videojuegos de la
franquicia, equipo y estilo de dibujo con dos fuentes, influencias del autor
con fuente directa, arcos e historia completa, y al menos 3 símbolos/emblemas
mirados en imagen con hex o paleta medida). Lo que falta (grito/pensamiento/
onomatopeya del manga, tablón legible, software exacto del estudio, fuente
del logo) son extras de detalle bloqueados por derechos de autor o por webs
con Cloudflare/403, ya documentados arriba en «No encontré» con ⚠️ y sus
intentos — no quedan como pendiente obligatorio.
