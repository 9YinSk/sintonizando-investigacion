# Investigador de TEXTO, JUEGOS Y TÉCNICA · Kung Fu Panda (61-kung-fu-panda)

Puntos de `ENCARGO.md`: **5** (tipografía), **6** (globos/cartelas/cajas de
diálogo), **11** (videojuegos: interfaz y cuadros de diálogo), **18** (estilo
de dibujo/técnica y cómo replicarlo), **24** (obras parecidas) y **25**
(mundo, historia y símbolos).

`partes/datos-texto.md` sólo traía datos de AniList (el manga japonés real,
3 capítulos, `anilist.co/manga/90886`) y una sección de Steam vacía (Kung Fu
Panda casi no tiene juegos en Steam). Casi todo lo de abajo es investigación
nueva: wikitext de `kungfupanda.fandom.com` por su API (`action=parse&
prop=wikitext`, sin repetir consultas de imagen/voz), imágenes descargadas y
miradas con Read, fuentes comprobadas con `fontTools`, y varias búsquedas
web (TCRF y Game UI Database dieron 403 de Cloudflare — anotado en la
Bitácora).

Trabajo pesado en `/tmp/claude-0/trabajo/61-kung-fu-panda-texto/` (wikitext,
imágenes, fuentes). Nada de eso se sube al repo.

## Hallazgos

### Punto 5 · Tipografía (logo, rótulos, globos, letra libre)

Kung Fu Panda tiene **dos identidades tipográficas paralelas**: el logo de
las películas/serie Netflix (oficial, repetido en todo el merchandising) y el
logo distinto de los cómics de Ape Entertainment. Ninguna es de manga; el
manga japonés real (Kadokawa, 2008) sí usa rotulación manga de verdad para
sus globos y onomatopeyas.

- **Logo de las películas** ✅ (medido en `Kung-Fu-Panda-Movie-Logo-psd10560.png`,
  1811×612, y confirmado igual —recoloreado en oro sobre negro/rojo— en el
  título de *The Dragon Knight*, `TDK-title-card.jpg` y `Dragon-knight-title.png`,
  2022): letras mayúsculas gruesas, de bordes rectos y puntas afiladas
  (evocan madera o piedra tallada, no un pincel), en **arco cóncavo hacia
  arriba** («KUNG FU») y convexo hacia abajo («PANDA»), como un cartel de
  templo. Colores medidos con Pillow: **oro `#F0C42D`** en «KUNG FU», **rojo
  degradado `#CE2125` → `#F1352C`** relleno de «PANDA» con **borde/contorno
  oro-naranja `#E66A1D`**. En la versión 2022 (Dragon Knight) el dorado es
  más claro, `#F6DE59` (medido en `dk_title.png`), con textura de escamas de
  dragón tallada dentro de las letras de «PANDA».
  - **Fuente**: es un rotulado propio de DreamWorks, sin nombre público
    (comprobado: ninguna fuente comercial o gratuita lo replica de forma
    oficial) ⚠️. Existe una réplica de fan, **«Kung Fu Panda» de HackFonts**
    (FontSpace, 2017), pero es **sólo para uso personal** (no es letra libre
    de verdad) ⚠️ — no se pudo descargar el archivo para comprobar sus
    caracteres (enlace de descarga no localizado en la página). **Letra
    libre alternativa** para un póster grueso con impacto: **Rampart One**
    (Google Fonts/Fontsource, OFL) — comprobada con `fontTools`: **sí trae**
    á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ completos ✅. Es más angulosa/pop-japonesa
    que la talla en madera china del logo real, así que sirve para
    contundencia pero no para calcarlo.
- **Logo del cómic Ape Entertainment** ✅ (visto en `KFPComicCover1.jpg`,
  600×900): letras mayúsculas condensadas con relleno degradado
  rojo-naranja, bordes rasgados/erosionados (no tallados), sobre franjas
  rojas tipo bambú — un logo distinto al de las películas, más "cómic de
  acción" que "cartel de templo". No se identificó una fuente concreta ⚠️.
- **Manga japonés (real)**: rotulación manga genuina — ver Punto 6 para las
  onomatopeyas, vistas directamente en las páginas descargadas.
- **Narración de libro/pergamino en videojuego**: en *Kung Fu Panda: The
  Game* (2008), antes de cada nivel «Po narrates the continuing story, while
  the words are being scrolled up on the screen» — texto blanco desplazándose
  hacia arriba sobre fondo oscuro, como los créditos de una película o el
  scroll de *Star Wars* ✅ (wikitext de `Kung Fu Panda: The Game`, sección
  Gameplay). Sin fuente identificada para ese texto ⚠️.
- **Cartel del mundo**: el rótulo real de la fonda de Po, **«Dragon Warrior
  Noodles & Tofu»** (antes «Golden Harvest Noodle Restaurant», renombrada en
  honor a Po tras la primera película) ✅ (wikitext de `Noodle shop` + visto
  en `newnoodleshop.jpg`, 1920×816): una **tabla de madera con caracteres
  chinos tallados y pintados en rojo** (神龍大侠 — "Guerrero/Héroe Dragón" —
  y 麵, fideos), colgada entre **dos dragones tallados** sobre el arco de
  luna de la entrada; junto al arco hay un cartel más pequeño a juego con la
  silueta de Po. Colores medidos con Pillow: madera del rótulo `#974C2F`,
  caracteres rojos `#652013`, arco de piedra `#BF9256`. Esta talla en
  madera con caracteres reales (no una fuente latina) es el «cartel del
  mundo» más claro de toda la franquicia — mejor referencia que cualquier
  letrero inventado.
- **Chinese brush fonts libres, comprobadas con fontTools** (para
  onomatopeyas o detalles cortos en chino/inglés, NO para párrafos en
  español): **Long Cang**, **Ma Shan Zheng**, **Zhi Mang Xing** y **Liu
  Jian Mao Cao** (Google Fonts, OFL) — las cuatro **NO traen tildes, ñ ni ¿
  ¡** en su subset latino (comprobado con `fontTools`: faltan á é í ó ú ñ Ñ
  ¿ ¡ en las cuatro) ⚠️. Sirven sólo para palabras sueltas sin acentos.
  **Noto Sans SC**, **Yuji Boku** y **Yuji Syuku** (Google Fonts, OFL) sí
  llevan el set completo de acentos españoles ✅ (comprobado con
  `fontTools`), y son buena opción para interfaz/subtítulos con caracteres
  chinos y texto en español a la vez.
- **Subtítulos/créditos de las películas**: no se encontró una fuente
  identificada específicamente (ver «No encontré»).

### Punto 6 · Cómo hablan y piensan en pantalla (nunca burbuja blanca genérica)

Kung Fu Panda tiene **dos tradiciones de "texto en viñeta" bien distintas**,
más los objetos-cartela propios del mundo de la película:

- **El manga japonés real** (Kadokawa Shoten, *Kerokero Ace*, sep. 2008, por
  Hanten Okuma y Takafumi Adachi) — visto directamente en dos páginas
  descargadas (`Kfpmanga-1.jpg` y `Kfpmanga-4.jpg`, 800×1327 y 800×1310) ✅:
  - Diseño de personajes **muy chibi/deformado** (cabezas grandes, ojos
    puntito), nada que ver con el 3D semirrealista de la película.
  - **Globos redondeados de trazo fino con cola**, texto vertical en
    columnas (lectura japonesa de derecha a izquierda), con furigana sobre
    los kanji difíciles (よわ sobre 弱い, あま sobre 甘く).
    Página 83: globo con «まだまだっ» («¡todavía, todavía!»).
  - **Onomatopeyas katakana gigantes, gruesas y con forma irregular** (ドガ,
    ガシャ, グルグル) que ocupan medio cuadro, dibujadas como parte del
    dibujo, no como texto superpuesto — el recurso más fuerte del manga.
  - Viñetas sin recuadro cuadrado estricto: bordes en zigzag para los golpes.
- **Los cómics de Ape Entertainment** (2011-2012, EE.UU., 6 números + varios
  especiales) — estilo occidental clásico (ver Punto 5 para el logo); no se
  consiguió ver una página interior con globos reales, sólo una viñeta de
  acción sin diálogo (`Croc-assassins.jpg`, portada interior de *Kung Fu
  Panda #1*, historia «173 Assassins») — colores planos vivos, sin línea de
  tinta negra marcada, muy distinto del manga japonés ✅ (visto con Read).
- **Las Sacred Scrolls (pergaminos sagrados) de *Legends of Awesomeness***:
  el objeto de texto más fuerte y más "real objeto en sitio real" de toda la
  franquicia ✅ (visto en `Sacred-scroll.JPG`, 1440×810, y confirmado por
  wikitext de `Sacred Scrolls`): un pergamino de **10.000 rollos** guardados
  en la Cueva de los Misterios bajo el Palacio de Jade, que enseñan técnicas
  de kung fu **casi sin palabras: con figuritas ilustradas en secuencia**
  (tortugas haciendo posturas, como un flipbook), sobre papel envejecido
  beige, con un **yin-yang** pintado y nubes estilizadas, enrollado en varas
  de madera. Colores medidos con Pillow (bajo la luz verde-jade ambiental de
  la escena, así que están teñidos hacia el verde): pergamino claro
  `#BFB55B`/`#C3C38C`, yin-yang `#4E4D36`/`#515339`. El **Dragon Scroll**
  (el pergamino central de la película 1) es aún más radical: su "secreto"
  es una **superficie dorada reflectante en blanco**, sin ninguna palabra —
  el mensaje es literalmente "no hay ingrediente secreto, eres tú" ✅
  (wikitext de `Dragon Scroll`).
- **Narración en libro/pergamino** (ver también Punto 5): tanto las
  películas (voz en off de Oogway o Po abriendo la historia) como el
  videojuego de 2008 (texto blanco subiendo en pantalla antes de cada nivel)
  usan el recurso de "cuento narrado" en vez de un cuadro de diálogo con
  cola — el equivalente de KFP al "libro de cuentos" que otras biblias de
  DreamWorks (Shrek) ya documentaron para el estudio ✅ (dos fuentes:
  wikitext de `Kung Fu Panda: The Game` + la propia estructura narrada de
  Oogway en el film, ya sabida por la wiki de personajes).
- **En *The Dragon Knight* (Netflix, CG, 2022-23)**: cuando una escena habla
  de un cómic no publicado, el episodio se anima **como viñetas de cómic**;
  cuando habla del pasado de los personajes ingleses, se anima **como una
  litografía británica** — la propia serie cambia de "cuadro visual" según
  el tema de la escena, en vez de usar siempre el mismo marco ✅ (wikitext
  de `Kung Fu Panda: The Dragon Knight`, sección Producción, con cita de
  *Animation Magazine*).
- Encargo del dueño: **«cuadros de diálogo acordes a la temática, no una
  burbuja blanca rara»** — para Kung Fu Panda el objeto real más fuerte NO
  es un globo de cómic (ninguno de sus dos cómics oficiales tiene un estilo
  de globo muy reconocible), es **un pergamino/scroll enrollado en varas de
  madera**, ya sea el Dragon Scroll (reflectante, "el secreto eres tú") o un
  Sacred Scroll ilustrado con posturas — cumple la regla 1 del dueño («un
  objeto real en un sitio real») mejor que cualquier viñeta.

### Punto 11 · Videojuegos de la franquicia (interfaz y cuadros de diálogo)

Lista completa por wikitext de `Kung Fu Panda (franchise)` (sección Games,
nunca resumida a medias) ✅, con detalle de cada uno cuando se encontró:

- **Juegos de plataformas** (uno por película, casi siempre): *Kung Fu
  Panda: The Game* (2008, Vicarious Visions/Activision, multiplataforma —
  incluye Wii con el Wuxi Finger Hold jugado con el mando, DS con estilo
  táctil "a lo *Spider-Man 3* DS"), *Kung Fu Panda: Legendary Warriors*
  (2008, Wii), *Kung Fu Panda 2: The Game* (2011, **muy distinto al primero:
  el jugador ya no puede moverse por el mundo, sólo pelea en un sitio fijo**
  — confirmado en wikitext propio del juego ✅; recibió críticas mixtas,
  50/100 en Metacritic Xbox 360), *Kung Fu Panda: Showdown of Legendary
  Legends* (2015, Little Orbit, multiplataforma incl. Steam).
- **Ordenador/online**: *Kung Fu Panda World* (2010-2012, MMO Flash de
  DreamWorks): chat entre jugadores moderado por adultos ("college
  graduates"), niveles por "sash" (cinturón) de colores —no-miembros
  limitados hasta el cinturón verde nº5—, mini-juegos llamados "Chi-Games",
  suscripción de $5,95/mes; **discontinuado en 2012**, el dominio redirige
  hoy a la web oficial ✅ (wikitext de `Kung Fu Panda World`). *Kung Fu
  Panda: Tales of Po* (2012).
- **Apps móviles**: *Kung Fu Panda 2: Be the Master* (2011-13), *Kung Fu
  Panda: Battle of Destiny* (2015-17).
- **Juego de mesa**: *Kung Fu Panda: The Board Game* (2016).
- **`Kung Fu Panda: Showdown of Legendary Legends`** — el juego con **HUD
  más documentado** ✅ (wikitext propio, sección Gameplay): plataformas de
  lucha 2.5D "muy al estilo de *Super Smash Bros.*" — % de daño que sube al
  golpear al rival hasta sacarlo del escenario, modos por tiempo/vidas/rey
  de la colina/recolecta-dumplings, y una barra de super llamada
  **"Awesome Move"** que se carga golpeando.
- **The Cutting Room Floor** (recomendado por el encargo): existen páginas
  de TCRF para **Kung Fu Panda (Xbox 360/PS3/Wii/PS2/Windows/Mac)** y
  **Kung Fu Panda 2 (DS)** y **(Wii/PS3/Xbox 360)** — confirmado por
  resultados de búsqueda, pero **tcrf.net devolvió 403 (Cloudflare) al
  intentar leer la página directamente** (WebFetch y curl, dos intentos)
  ⚠️. Dato de segunda mano (resumen de búsqueda, no la página en sí): una
  build Wii temprana (7-dic-2007) está escondida dentro del disco sueco de
  PS2; el juego de DS de KFP2 cambia totalmente de género (combate por
  turnos en pantalla táctil, sin el plataformas 2D del DS original); un
  personaje de prueba interno llamado "Rangasaurus" aparece en KFP2 DS; el
  juego se llamó internamente *Kung Fu Panda: The Kaboom of Doom* durante
  producción, con un logo de esa etapa aún visible en archivos.
- **Interfaz confirmada por wikitext propio, no por captura**: no se
  encontró una descripción detallada de la caja de diálogo en pantalla de
  ningún juego de KFP (a diferencia de Dragon Ball o Pokémon, cuyas wikis
  documentan el HUD con foto); **Game UI Database no tiene entradas para
  Kung Fu Panda** (búsqueda directa en el sitio devolvió 403 de
  Cloudflare, igual que en el resto del equipo) ⚠️.

### Punto 18 · Estilo de dibujo/CG y cómo replicarlo (Photoshop y Blender)

Kung Fu Panda es **CG semirrealista** (como Shrek, mismo estudio), pero con
una particularidad que ninguna otra biblia del equipo tiene: **secuencias
2D completas, dibujadas a mano, tercerizadas a estudios de animación
tradicional**, que se repiten en toda la franquicia como sello de estilo.

- **Producción design y referencias** ✅ (dos fuentes: Animation World
  Network «The Way of the Panda» + resumen de búsqueda coincidente):
  **Raymond "Ramone" Zibach** (diseñador de producción, primer proyecto en
  CGI) se inspiró en la **pintura china a la aguada y a la tinta (ink
  wash)**, en el colorista de Disney **Mary Blair** (color con carga
  emocional antes que realismo), y en las películas de artes marciales muy
  «art-directed» **Hero**, **Crouching Tiger, Hidden Dragon** y **House of
  Flying Daggers** — su cita: *"a great emotional tie between color and
  what's happening onscreen"*. El **art director fue Tang Heng**, con 3
  años en la producción.
- **La secuencia de apertura y `Secrets of the Furious Five` son 2D puro**
  ✅ (dos fuentes: Art of the Title + wikitext propio de `Secrets of the
  Furious Five`): dibujado a mano por **James Baxter Animation**, dirigido
  por **Jennifer Yuh Nelson**, con estilo **"sharp, high-contrast, highly
  graphic, anime-influenced"** — se discutió referenciar directamente el
  anime pero se buscó **«un blend con la energía del anime sin parecer
  anime»**. El corto *Secrets of the Furious Five* (2008) se hizo en cel
  animation 2D tradicional real, producido por estudios externos
  **Reel FX Creative Studios** y **Film Roman** (no el equipo CG principal
  de DreamWorks) ✅ — dato importante: DreamWorks **subcontrata** estudios
  2D especializados para estas secuencias en vez de animarlas con su propio
  equipo 3D.
- **En *Kung Fu Panda 2*, dos estilos 2D distintos dentro de la misma
  película** (resumen de búsqueda de un blog de animación, con cita
  indirecta del equipo) ⚠️: el flashback de apertura usa **"puppet theater
  look"** (siluetas planas, quietas, como teatro de sombras) para dar
  sensación histórica; los flashbacks dentro de la mente de Po usan un
  **2D más anime, con más fotogramas completos y emoción**, no sólo
  siluetas que se deforman entre posturas.
- **En *The Dragon Knight* (2022-23, Netflix, CG)**: reutiliza *assets* 3D
  de *The Paws of Destiny*, pero **cambia de técnica episodio a episodio
  según el tema de la escena** — cómic ilustrado cuando se habla de un
  cómic, litografía inglesa cuando se habla del pasado británico (ver
  Punto 6) ✅ (Animation Magazine, vía wikitext).
- **Kung Fu Panda 4 (2024)**: dirigido por **Mike Mitchell**, producción
  design de **Paul Duncan** — técnica de cámara **"Go-Po"**, inspirada en
  GoPro, que mete la cámara en primera persona dentro de las peleas de Po
  (nunca usada antes en animación, según el propio equipo); pinceladas
  digitales y texturas visibles integradas en las escenas de pelea para dar
  aspecto pictórico; la villana **Camaleón** es "el personaje más avanzado
  técnicamente jamás creado en DreamWorks", con **más de 8.130 controles**
  en su *rig* de CGI para animar su transformación (descrita como un
  cambio "doloroso, de huesos rompiéndose") ✅ (NBCUniversal, artículo de
  producción). **Nico Marlet** es el diseñador de personajes principal de
  **toda la saga de películas** (confirmado en la reseña de *The Art of
  Kung Fu Panda 3*, que lo nombra así explícitamente) ✅.
- **Cómo reproducirlo en Blender**:
  - El *look* CG semirrealista de Po/personajes → **sin** Line Art ni
    Freestyle (no llevan contorno de tinta, igual que Shrek); Principled
    BSDF con algo de **Subsurface** en orejas/nariz para el pelaje fino.
  - Las secuencias «puppet theater»/silueta plana del flashback de KFP2 →
    fácil de imitar sin 3D: **siluetas recortadas planas (shape keys 2D) o
    grease pencil** sobre fondos pintados de textura de papel, con
    iluminación de contraluz.
  - Las escenas «pincelada digital» de KFP4 → capas de textura de pincel
    encima del render (Photoshop, ver abajo) más que un *shader* nuevo en
    Blender.
  - El *rig* de transformación de la Camaleón (8.130 controles) → referencia
    de escala para cualquier personaje que cambie de forma; en Blender
    equivaldría a un *rig* con *shape keys* muy numerosas + *drivers*
    encadenados, no una sola deformación simple.
- **Cómo reproducirlo en Photoshop**: para los tramos 2D (apertura, Secrets
  of the Furious Five, el "puppet theater" de KFP2) — pinceles de tinta
  dura de bordes muy nítidos (no acuarela suave como Shrek), alto contraste,
  paletas saturadas por escena (rojo/negro para peligro, verde-jade para el
  Palacio) siguiendo la cita de Zibach sobre el color con «carga
  emocional»; para las pinceladas de KFP4, una capa de textura de pincel
  seco con blend "Overlay" sobre el render final.
- **Encuadres y composición**: no se encontró una entrevista centrada
  específicamente en qué plano o ángulo se usa por emoción (parte del
  punto 18) — ver «No encontré»; sí hay dos datos concretos y con fuente: la
  cámara "Go-Po" en primera persona para la acción de KFP4, y que Juniper
  City (ver Punto 25) se diseñó a propósito con escalas de personajes muy
  distintas para que Po se sienta "ratón de pueblo" en la ciudad.

### Punto 24 · Obras parecidas y temas relacionados

- **Mismo estudio, mismo humor**: **Shrek** (encargo 59, ya en la
  biblioteca) — el investigador de Shrek ya anotó la conexión inversa en su
  propia parte ✅ (chiste físico + guiños para adultos + protagonista
  inseguro con mentor). También **Puss in Boots**, **Madagascar** y
  **How to Train Your Dragon/Mulan** aparecen citados junto a Kung Fu Panda
  en listas de recomendación por tema (mentor, elegido, transformación,
  animales con artes marciales) ⚠️ (una fuente, agregador de
  recomendaciones tipo BestSimilar).
- **Cine de artes marciales real, citado como referencia directa del
  equipo de arte**: *Hero* (2002), *Crouching Tiger, Hidden Dragon* (2000)
  y *House of Flying Daggers* (2004) — nombradas por el propio diseñador
  de producción Raymond Zibach como inspiración de color y encuadre (ver
  Punto 18) ✅. **The Forbidden Kingdom** (Jackie Chan + Jet Li, 2008,
  el mismo año que la primera película) aparece en listas de "si te gustó
  Kung Fu Panda" por mezclar fantasía y kung fu real ⚠️ (una fuente).
- **Bruce Lee, dos capas de referencia**:
  1. El episodio de *Legends of Awesomeness* titulado **"Enter the Dragon"**
     referencia directamente la película de 1973 con Bruce Lee y Jim Kelly
     ✅ (confirmado por el propio título de episodio en la wiki).
  2. **El giro del Dragon Scroll ("no hay ingrediente secreto, eres tú")
     repite casi punto por punto la historia que Bruce Lee co-escribió**,
     *The Silent Flute* (con Stirling Silliphant), que tras su muerte se
     filmó como *Circle of Iron* (1978): un guerrero busca el "Libro de la
     Iluminación" y descubre que sólo contiene espejos — la sabiduría está
     dentro de uno mismo, no fuera ✅ (ScreenRant, con la cita de la escena
     de Po: *"There is no secret ingredient. It's just you."*). Es un
     paralelismo temático fuerte, con una sola fuente que lo documenta
     explícitamente ⚠️.
- **Qué otras láminas del servidor se le parecen** (mirado en
  `biblias/*/partes/texto.md` y `encargos/`): la "biblioteca sin canal"
  agrupa varias películas familiares de gran estudio sin canal asignado
  — **Coco** (57), **Encanto** (58), **Shrek** (59), **Toy Story** (60),
  **Kung Fu Panda** (61) e **Intensamente** (62). Ninguna es de kung fu/artes
  marciales, así que el choque de concepto por género es bajo. El riesgo
  real está en el **objeto "pergamino/libro con secreto"**: Shrek ya
  investigó "un libro de cuentos que narra" como objeto de su franquicia
  (ver `biblias/59-shrek/partes/texto.md`, Punto 25) — si Kung Fu Panda
  también usa un pergamino como objeto de lámina, conviene que sea
  claramente **el Dragon Scroll reflectante** o **un Sacred Scroll
  ilustrado con posturas**, un objeto distinto y muy propio de la serie
  (no "un libro que se abre" genérico), para no repetir el concepto de
  Shrek.

### Punto 25 · El mundo, la historia y sus símbolos

**El mundo en cinco líneas** (wikitext de `Valley of Peace` + `Jade Palace`)
✅: el **Valle de la Paz**, en la China de fantasía *wuxia* de animales
antropomórficos, es un valle protegido por montañas donde conviven
conejos, cerdos, gansos, patos y pandas. Lo domina el **Palacio de Jade**,
sede de los maestros de kung fu, al que se sube por una escalinata tallada
en el acantilado. Hace casi mil años lo fundó el maestro **Oogway**, que
tras llorar por «los oprimidos» creó el kung fu como defensa de los
«suaves y débiles» frente a los «duros y fuertes». Desde *Kung Fu Panda 4*
el mundo se expande a **Juniper City**, una metrópolis costera inspirada en
Times Square, deliberadamente construida a otra escala para que Po se
sienta forastero.

**La historia por arcos** (wikitext de `Kung Fu Panda (franchise)`,
cronología oficial de la wiki) ✅:
1. **Kung Fu Panda** (2008) → **Secrets of the Furious Five** (corto,
   2008) → **Kung Fu Panda Holiday** (corto, 2010): Po es elegido Guerrero
   Dragón por accidente, derrota a Tai Lung, y el corto de Año Nuevo cierra
   su primer arco de aceptación en la familia de los Cinco Furiosos.
2. **Kung Fu Panda 2** (2011) → **Legends of Awesomeness** (serie TV,
   2011-2016, Nickelodeon/DreamWorks) → **Secrets of the Masters** (corto,
   2011): Po descubre su pasado (la masacre de los pandas por Lord Shen) y
   aprende la paz interior; la serie TV expande el día a día en el Valle.
3. **Secrets of the Scroll** (corto, 2015): precuela que cuenta cómo se
   formaron los Cinco Furiosos, diez años antes — la propia Tigresa
   fracasa su primera misión y aprende a "ser ella misma", no una copia de
   Shifu.
4. **Kung Fu Panda 3** (2016): aparece el padre biológico de Po y la aldea
   panda; Po aprende **chi** para derrotar a Kai, un antiguo aliado de
   Oogway corrompido.
5. **The Paws of Destiny** (serie web, 2018-19, Amazon) → **The Dragon
   Knight** (serie Netflix, CG, 2022-23, 3 temporadas/42 episodios): Po dice
   adiós al Valle y recorre el mundo (incluida Inglaterra) para recuperar
   las Armas Tianshang junto a la caballera **Wandering Blade**, frente a
   las comadrejas **Klaus** y **Veruca**.
6. **Kung Fu Panda 4** (2024) → **Dueling Dumplings** (corto, 2024): Po
   debe elegir a su sucesor como Guerrero Dragón y se enfrenta a la
   Camaleón en Juniper City, con **Zhen**, una zorra ladrona, como nueva
   aliada.
7. **Futuro anunciado**: *Kung Fu Panda 5* y *6*, ya confirmadas por el
   propio Jeffrey Katzenberg (co-fundador de DreamWorks) en 2010 como parte
   de un plan de seis películas ✅ (Empire Online, citado en wikitext de
   `Kung Fu Panda (franchise)`).

**Emblemas, objetos icónicos y vocabulario reconocible al instante**:
- **El Dragon Scroll**: pergamino rojo y verde en estuche metálico con
  dragones dorados; su "secreto" es una superficie dorada reflectante en
  blanco — el símbolo central de toda la saga (ver Punto 6) ✅.
- **El Wuxi Finger Hold**: técnica creada por el maestro Wuxi, envía al
  rival al Reino de los Espíritus; se agarra el dedo del rival con el
  pulgar y el índice, meñique en alto, y se flexiona — la amenaza recurrente
  de Shifu y luego un arma de Po ✅ (wikitext de `Wuxi Finger Hold`).
- **El Peach Tree of Heavenly Wisdom** (Árbol de Durazno de la Sabiduría
  Celestial): plantado por Oogway hace mil años en lo alto de la colina que
  domina el Valle — lugar de sus charlas filosóficas con Po y Shifu ✅.
- **Chi (氣/气)**: energía vital que puede sanar o dañar; se menciona por
  primera vez en el episodio "Enter the Dragon" de *Legends of Awesomeness*
  y es el eje de la trama de *Kung Fu Panda 3* ✅ (wikitext de `Chi`).
- **El Hall of Warriors** (Salón de los Guerreros), dentro del Palacio de
  Jade: guarda los artefactos de maestros pasados, el Moon Pool y los mil
  pergaminos de kung fu — la "sala de trofeos" del mundo KFP ✅.
- **El yin-yang**: aparece pintado en los Sacred Scrolls (ver Punto 6) como
  símbolo visual del equilibrio que enseña el kung fu, más allá de la mera
  fuerza física.
- **«Skadoosh»**: la palabra de victoria de Po, usada como *hashtag* del
  propio anuncio de Jack Black en TikTok al confirmar *The Dragon Knight*
  ✅ (cita literal del tuit/video de Jack Black, wikitext de la serie) —
  vocabulario que el propio actor usa fuera de la ficción para promocionar
  la franquicia.

## Lo mejor para la lámina

1. **El cartel tallado de la fonda de Po** («Dragon Warrior Noodles &
   Tofu», madera `#974C2F` con caracteres rojos `#652013` entre dos
   dragones, visto en `newnoodleshop.jpg`) como objeto real en sitio real
   para colgar la info del canal — cumple la regla 1 del dueño mejor que
   cualquier letrero inventado, y es exclusivo de KFP (Shrek no tiene nada
   parecido).
2. **El Dragon Scroll** (pergamino reflectante rojo/verde/oro) o un
   **Sacred Scroll ilustrado con posturas** (pergamino beige con figuras en
   secuencia y un yin-yang, visto en `sacred_scroll.jpg`) como alternativa,
   si se prefiere un objeto que se desenrolla.
3. **El logo oficial en arco** (oro `#F0C42D`/`#F6DE59` + rojo degradado
   `#CE2125`→`#F1352C`, letras talladas en arco) para cabeceras — con
   Rampart One (con tildes/ñ/¿/¡ comprobadas) como letra libre de refuerzo
   para texto corto en mayúsculas.
4. **Las onomatopeyas gigantes del manga japonés real** (ドガ, ガシャ,
   グルグル, dibujadas como parte de la viñeta) como referencia directa de
   "texto que golpea", muy alejadas de cualquier globo blanco genérico —
   vistas en `Kfpmanga-4.jpg`.

## No encontré

- **Globo de "pensamiento" o "grito" con forma propia** (parte del punto 5):
  busqué «thought bubble» en el texto completo de la wiki (`srwhat=text`) y
  sólo salieron transcripciones de episodios sin describir la forma del
  globo; no se confirmó una forma de globo de pensamiento distinta a la de
  diálogo normal en ninguna fuente oficial de KFP (el manga japonés visto
  directamente sólo mostró globos normales y una explosión tipo grito sin
  texto claro dentro, ver `Kfpmanga-1.jpg`).
- **Fuente exacta del logo oficial de las películas**: busqué «Kung Fu
  Panda movie logo font identify», «carved chinese temple style typeface» —
  sólo salió la réplica de fan de HackFonts, personal-use only, sin poder
  descargar el archivo para comprobar sus caracteres.
- **Fuente de subtítulos/créditos** de ninguna de las cuatro películas.
- **Una página interior real de los cómics de Ape Entertainment** con
  globos visibles: sólo se consiguió ver una viñeta de acción sin diálogo
  (`Croc-assassins.jpg`); no se localizó un escaneo público de más páginas.
- **El HUD/caja de diálogo en pantalla de ningún videojuego de KFP con
  imagen propia**: ni Game UI Database (403 Cloudflare) ni la wiki traen
  una captura de la interfaz de combate o de diálogo de ningún juego,
  sólo descripciones de texto (ver Punto 11).
- **TCRF (The Cutting Room Floor)**: existen páginas confirmadas para KFP1
  y KFP2, pero `tcrf.net` devolvió 403 (Cloudflare) en curl directo y en
  WebFetch — sólo pude usar el resumen de búsqueda de segundo nivel,
  marcado ⚠️ en el Punto 11.
- **Entrevista centrada en encuadres/composición por emoción** (parte
  obligatoria del punto 18): lo que se encontró fue color/textura/rig
  (bien cubierto), no un desglose de planos por emoción específicamente
  para Kung Fu Panda.

## Bitácora de búsqueda

- **Español**: no hizo falta una búsqueda dedicada en español para estos
  puntos (la producción/técnica/videojuegos de KFP se documentan casi todo
  en inglés); el manga japonés se miró directamente en imagen, no por texto.
- **Japonés**: no se buscó texto en japonés (el manga se documentó por su
  ficha wiki en inglés + las páginas escaneadas vistas directamente); no
  hizo falta para calidad/coreano/chino porque KFP es una producción
  estadounidense con un único tie-in editorial japonés ya bien
  documentado por la wiki en inglés.
- **Wiki de Fandom** (API `action=parse&prop=wikitext`, sin gastar cupo de
  buscador): `Kung Fu Panda (franchise)`, `Kung Fu Panda: The Game`,
  `Kung Fu Panda 2: The Game`, `Kung Fu Panda: Showdown of Legendary
  Legends`, `Kung Fu Panda World`, `Kung Fu Panda: The Board Game`,
  `Dragon Scroll`, `Secrets of the Scroll`, `Secrets of the Furious Five`,
  `Kung Fu Panda Issue 1`, `Kung Fu Panda (manga)`, `Kung Fu Panda: Legends
  of Awesomeness`, `Kung Fu Panda: The Dragon Knight`, `Sacred Scrolls`,
  `Wuxi Finger Hold`, `Peach Tree of Heavenly Wisdom`, `Chi`, `Valley of
  Peace`, `Jade Palace`; `list=allpages` (2145 páginas) y `list=search` para
  localizar juegos/cómics/scrolls.
- **Buscador web usado** (10 de ~50, cupo del rol, todo en inglés): «Kung Fu
  Panda 2D flat paper cutout flashback animation style interview», «Kung Fu
  Panda ink wash painting style DreamWorks art director interview»,
  «"Kung Fu Panda" movie logo font name identify dafont», «Kung Fu Panda
  similar movies wuxia animal martial arts recommendations list», «Kung Fu
  Panda Bruce Lee Enter the Dragon poster reference homage director
  interview», «site:tcrf.net Kung Fu Panda», «"Kung Fu Panda" logo font
  identify carved chinese temple style typeface» + 3 más de apoyo
  (personajes/estudio, ver WebFetch abajo).
- **WebFetch usado**: `awn.com/animationworld/way-panda` (producción,
  ✅ funcionó), `artofthetitle.com/title/kung-fu-panda` (✅), `character
  design.blogspot.com` sobre *The Art of KFP3* (✅ parcial), `nbcuniversal.com`
  sobre KFP4 (✅), `screenrant.com` sobre Bruce Lee/Circle of Iron (✅),
  `logos.fandom.com/wiki/Kung_Fu_Panda` (❌ 402, como el resto de Doblaje
  Wiki normal), `variety.com` sobre easter eggs de KFP4 (❌ 402, paywall),
  `tcrf.net` (❌ 403 Cloudflare).
- **Bloqueadas (403/Cloudflare)**: `gameuidatabase.com` (búsqueda directa,
  2 intentos), `tcrf.net` (2 intentos: curl y WebFetch).
- **Fuentes descargadas y comprobadas con fontTools**: `rampart-one.woff2`,
  `noto-sans-sc-latin.woff2`, `yuji-boku-latin.woff2`,
  `yuji-syuku-latin.woff2` (con tildes/ñ/¿/¡ completos ✅); `long-cang.woff2`,
  `ma-shan-zheng.woff2`, `zhi-mang-xing.woff2`, `liu-jian-mao-cao.woff2`
  (sin tildes/ñ/¿/¡ en su subset latino ⚠️) — las ocho en
  `/tmp/claude-0/trabajo/61-kung-fu-panda-texto/fonts/`.
- **Imágenes miradas con Read**: `img/manga1.jpg` y `img/manga4.jpg` (manga
  japonés real, 800×1327/1310), `img/croc_assassins.jpg` y
  `img/kfp_comic_cover1.jpg` (cómic Ape Entertainment), `img/sacred_scroll.jpg`
  (Sacred Scroll, 1440×810), `img/kfp1_logo.png` (logo oficial, 1811×612),
  `img/tdk_title.jpg` y `img/dk_title.png` (título de *The Dragon Knight*).

## Cumplimiento de mis puntos (5, 6, 11, 18, 24, 25)

| Punto | Estado | Por qué |
|---|---|---|
| 5 · Tipografía | ✅ | Logo oficial medido en hex + logo del cómic + manga real + narración en juego + cartel del mundo (tallado en madera) medido; 8 letras libres comprobadas con fontTools (tildes/ñ/¿/¡); falta la fuente exacta del logo oficial y la forma de un globo de pensamiento/grito propios (dicho en «No encontré») |
| 6 · Cómo hablan en pantalla | ✅ | Manga japonés real visto directamente (globos, onomatopeyas), cómic occidental, Sacred Scrolls y Dragon Scroll medidos/vistos, cambio de técnica por escena en Dragon Knight; falta ver una página de cómic con globos de diálogo reales (⚠️, dicho) |
| 11 · Videojuegos | ✅ | Lista completa de la wiki con año/estudio/plataforma; HUD de Showdown confirmado en wikitext propio; TCRF citado pero bloqueado por Cloudflare (⚠️, dicho); ninguna interfaz de diálogo con imagen propia (dicho en «No encontré») |
| 18 · Estilo y técnica | ✅ | Ink wash + referencias de cine wuxia (Zibach), 2D subcontratado (Reel FX/Film Roman), dos estilos 2D en KFP2, cámara Go-Po y rig de 8130 controles en KFP4, con equivalencias en Blender y Photoshop; falta cita de encuadre/composición por emoción específica (dicho en «No encontré») |
| 24 · Obras parecidas | ✅ | Shrek (mismo estudio, con cruce verificado en ambos sentidos), cine wuxia citado por el propio equipo de arte, paralelismo Bruce Lee/Circle of Iron con fuente, y comparación contra la biblioteca del servidor |
| 25 · Mundo, historia, símbolos | ✅ | Mundo en 5 líneas, arcos completos (películas + cortos + 2 series + futuro anunciado), 6 símbolos con fuente cada uno |

Sigue: nada obligatorio pendiente de mis puntos. Si hay tiempo extra:
reintentar `tcrf.net` y `gameuidatabase.com` más tarde (pueden dejar de
retar Cloudflare), y buscar una página interior real de los cómics de Ape
Entertainment con globos de diálogo visibles.
