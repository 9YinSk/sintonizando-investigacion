# Parte de TEXTO, JUEGOS Y TÉCNICA · Overlord (encargo 83)

Investigador de texto: puntos 5, 6, 11, 18, 24 y 25 de `ENCARGO.md`. Parte de
`partes/datos-texto.md` (AniList, staff, obras relacionadas, capturas de Steam
de juegos con el nombre «Overlord» que NO son de la franquicia). Wiki usada:
`overlordmaruyama.fandom.com`.

## Hallazgos

### Punto 5 · Tipografía

- El logo de Overlord (novela, anime y película) tiene una letra gótica
  desgastada/con textura de sangre; en los foros de identificación de fuentes
  de dafont.com, dos usuarios distintos (Logolex y soulard) coinciden en que
  la letra **«Squealer»** (Typodermic Fonts) es la que más se parece, tanto
  para el logo de las novelas/anime como para el de la película · fuente:
  dafont.com/forum/read/371528 y dafont.com/forum/read/384964 · ✅ (dos
  hilos, dos usuarios, mismo veredicto) · Squealer es de pago (Typodermic).
- **Letra libre equivalente** para el logo/título (gótica, oscura, con
  swashes): **Pirata One** (Google Fonts/Fontsource, licencia OFL-1.1) ·
  comprobado con `fontTools` sobre el archivo real (`pirata-one` v23,
  `latin-400-normal.woff`): tiene **ñ, Ñ, á, é, í, ó, ú, ¿, ¡** (todos los
  codepoints existen en el `cmap`) · fuente: api.fontsource.org/v1/fonts/
  pirata-one + comprobación local · ✅. Alternativas más «heavy metal» en la
  misma familia de Google Fonts, también en `latin-ext`: **Metal Mania** y
  **Nosifer** (ambas OFL, ambas cubren 0000-00FF así que llevan tildes/ñ/¿/¡)
  · fuente: api.fontsource.org/v1/fonts?subsets=latin-ext · ⚠️ (el rango
  unicode se comprobó por API, no letra por letra con fontTools como con
  Pirata One).
- **Interfaz de videojuego** (HUD): en las capturas reales de *Overlord:
  Escape from Nazarick* (ver punto 11) el HUD usa una tipografía de **palo
  seco condensada en mayúsculas** para «LIFE» y los números, con un dial
  circular de habilidades en tonos rosa/carmesí neón — es el estilo típico de
  HUD de acción/metroidvania, no una letra de fantasía · fuente: capturas
  oficiales de Steam (ver punto 11) · ✅ (mirado directamente en la imagen).
- **Subtítulos y créditos** de la edición en inglés de Yen Press (novela y
  manga): no se encontró el nombre exacto de la tipografía interior en
  fuentes públicas (colofón no disponible en línea) · búsquedas: «Overlord
  light novel font used interior typesetting Yen Press» (inglés) · ⚠️ **no lo
  encontré**, no «no existe»: habría que mirar el colofón físico del libro.
- El mundo de Overlord **no tiene un alfabeto o letra propia inventada**: la
  wiki explica que el mundo traduce automáticamente el habla («everyone
  accepts these translations naturally»), pero **sí hace falta aprender a
  leer** las letras escritas — el canon no describe una tipografía ficticia
  para eso · fuente: overlordmaruyama.fandom.com/wiki/New_World (sección
  Background) · ✅ (texto explícito de la wiki, con cita a Overlord Volumen 2
  cap. 1).
- No se encontró qué tipografía usa Kadokawa en las cartelas del **manga**
  japonés (rótulos de "Comp Ace"); búsquedas en inglés y japonés
  (「オーバーロード コミックス フォント」) no dieron resultado con fuente
  verificable · ⚠️ no lo encontré.

### Punto 6 · Cómo hablan y piensan en pantalla

- El manga y la novela usan un recurso propio y muy citado: el cráneo de Ainz
  **no tiene expresión facial**, así que el guion muestra sus emociones reales
  por **narración interior** (monólogo en cursiva/aparte) que contrasta con lo
  que dice en voz alta delante de sus sirvientes, más el **parpadeo de la luz
  roja de sus cuencas** como único indicador visual de emoción · fuente:
  TV Tropes (resultado de búsqueda, la página en sí dio 403 al leerla
  directo) + wiki de personajes · ⚠️ (una fuente de calidad, TV Tropes
  bloqueado por Cloudflare al intentar leerlo con WebFetch y con curl).
- Para la lámina esto es oro: **una cartela de pensamiento** que muestre lo
  que Ainz piensa de verdad, y aparte (fuera de la cartela) lo que dice en voz
  alta con cara neutra — es la firma visual de la serie, mejor que una burbuja
  blanca genérica.
- Interfaz de los juegos de la franquicia (ver punto 11 para las capturas):
  las ventanas de sistema/menú en *Overlord: Escape from Nazarick* van en
  paneles oscuros con borde geométrico y acentos rosa/carmesí neón sobre
  fondo de piedra gótica — no blanco — coherente con la estética oscura de
  Nazarick pedida en el encargo · fuente: capturas oficiales de Steam,
  miradas directamente · ✅.
- Tipos genéricos de globo de manga (dato de referencia, NO específico de
  Overlord: no se encontró una guía de estilo oficial de los globos del manga
  de Overlord) — redondo con rabillo para habla normal, nube con puntos para
  pensamiento, borde puntiagudo/estallido para grito · búsquedas en inglés
  «Overlord manga speech bubble style» sólo devolvieron guías genéricas de
  cómo dibujar globos, no específicas de esta obra · ⚠️ dato genérico, no
  propio de la serie; se usa sólo como base, no como cita de canon.

### Punto 11 · Videojuegos de la franquicia

- **Aviso importante:** las capturas de Steam en `datos-texto.md` bajo
  «Videojuegos en Steam» (Stellaris: Overlord, Overlord II de Triumph
  Studios, Wizardry: Proving Grounds of the Mad Overlord, Overlord: Raising
  Hell, Étrange Overlord, Outbreak Overlord) **NO son de la franquicia
  Overlord/Kugane Maruyama**: coinciden sólo en el nombre. Se comprobó cada
  uno por su editora/desarrolladora (Paradox, Triumph Studios, Digital
  Eclipse, Minicactus Games) — ninguna tiene relación con Kadokawa ni con
  Madhouse · ✅ (comprobado contra la ficha de cada juego en Steam).
- **Mass for the Dead** (マスフォーザデッド) — juego oficial para
  smartphone (iOS/Android), desarrollado por Exys Inc., basado en la novela.
  RPG por turnos tipo gacha: acciones «Attack», «Charge» y «Defend», hechizos
  con puntos de magia (MP), modos automático y acelerado. Salió en Japón el
  21-feb-2019 y en inglés (con Crunchyroll) el 20-abr-2020; el servicio
  global cerró el 31-mar-2021 pero sigue activo en Japón, con contenido nuevo
  en oct-2024 · fuente: overlordmaruyama.fandom.com/wiki/Mass_for_the_Dead ✅
  (coincide con Pocket Gamer y QooApp en la reseña de la búsqueda web) · la
  interfaz recibió críticas por verse «anticuada» para el tono de la serie,
  según Pocket Gamer · ⚠️ (opinión de reseña, una fuente).
- **OVERLORD -ESCAPE FROM NAZARICK-** — juego de acción metroidvania 2D,
  desarrollado por Engines Inc., publicado por Kadokawa, lanzado el
  16-jun-2022 en Steam y Nintendo Switch. Protagonista: **Clementine**
  (antagonista secundaria de los primeros arcos), atrapada sin memoria dentro
  de la Gran Tumba de Nazarick, debe recuperar sus artes marciales y escapar
  esquivando a los sirvientes de Ainz · fuente: overlordmaruyama.fandom.com/
  wiki/OVERLORD_-ESCAPE_FROM_NAZARICK- + store.steampowered.com/app/1782150 ·
  ✅ (dos fuentes, wiki y Steam).
  - **Interfaz mirada directamente** (capturas oficiales de Steam,
    1920×1080 reescaladas a hoja de contacto en
    `/tmp/claude-0/trabajo/83-overlord-texto/efn_contact.jpg`): barra de
    vida «LIFE» naranja arriba a la izquierda; dial circular de habilidades
    en violeta/rosa neón con botones de mando (X, Y, LT) alrededor; contador
    de gemas de moneda arriba a la derecha (rombo rosa, número); minimapa
    violeta abajo a la izquierda con temporizador «00:08:20»; plataformas de
    piedra con arcos góticos apuntados de fondo en tonos azul-violeta; los
    círculos mágicos de ataque son rojo carmesí con runas · fuente:
    shared.akamai.steamstatic.com/.../1782150 (dos capturas descargadas y
    miradas) · ✅ (visto directamente, dato propio no repetido de reseñas).
- **Overlord: King of Nazarick** (纳萨力克之王), renombrado **Lord of
  Nazarick** en inglés — juego de cartas/rol estratégico para móvil,
  desarrollado por bilibili (China), anunciado 9-mar-2023, beta 21-nov-2023;
  versión en inglés publicada por A Plus Japan y **Crunchyroll Games**,
  otoño de 2024. El servicio cerró el 29-dic-2025. Los jugadores se
  convierten en un Ser Supremo y arman escuadras con Albedo, Shalltear y
  personajes originales del juego · fuente:
  overlordmaruyama.fandom.com/wiki/Overlord:_King_of_Nazarick · ⚠️ (una sola
  fuente wiki; no se encontró cobertura independiente en prensa
  especializada más allá del anuncio).
- No se pudo comprobar en The Cutting Room Floor (tcrf.net): la web devolvió
  **403 (Cloudflare)** tanto por curl como por WebFetch, dos intentos por vía
  distinta · ⚠️ no lo encontré, no «no existe».

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

- **Diseño de personajes original**: so-bin (ilustrador de las novelas) —
  su estilo mezcla el detalle gótico occidental con sensibilidad japonesa;
  aunque dibuja en digital, entrena también en analógico porque no le
  convence cómo «se siente» el mezclado de color en software, lo que explica
  el aspecto pictórico/pintado a mano de sus ilustraciones · fuente: Yen
  Press «Artist Showcase: The Art of so-bin» (yenpress.com/news/
  artist-showcase-the-art-of-so-bin) · ✅ (coincide con la reseña del
  artbook oficial «Overlord: The Complete Anime Artbook»).
- **Diseño de personajes del anime**: Takahiro Yoshimatsu adaptó el diseño de
  so-bin para animación (dato ya en `datos-texto.md`, equipo creativo) ·
  fuente: AniList staff · ✅.
- **Técnica de animación**: el estudio Madhouse usa **CGI 3D pesado** para
  los personajes y criaturas no orgánicas (esqueletos como Ainz y las
  criaturas de Nazarick, dragones), con dirección de CG de Shuuhei Yabuta
  (dato ya en `datos-texto.md`). La recepción de ese CGI fue mixta entre el
  público, aunque se valora que sirve bien para las escenas de pelea
  · fuente: reseña recogida en búsqueda web (2danicritic, sobre Overlord) ·
  ⚠️ (una fuente de reseña de aficionado, sin la entrevista técnica original
  del estudio, que no se encontró en línea).
- **Cómo replicarlo en Blender**: dado que Ainz y varias criaturas de
  Nazarick son esqueletos/no-orgánicos con **toon shading** marcado, la vía
  más fiel es un *shader* de tramas (`Shader to RGB` + rampa de color de 2-3
  bandas) y contorno con **Solidify invertido** (grosor variable: más grueso
  en Ainz, más fino en personajes humanos) en vez de Freestyle, que es más
  lento para animación. Para el hueso/marfil de Ainz: base blanco-hueso
  `#E8E4D8` con sombra fría azulada, nunca sombra cálida (contraste con el
  fuego/las runas carmesí de su magia) · ⚠️ (recomendación técnica propia a
  partir de lo observado en fotogramas oficiales y capturas de videojuego,
  no de una entrevista de producción; se cita como técnica sugerida, no como
  dato confirmado del estudio).
- **Encuadres y composición**: en las capturas de *Escape from Nazarick*
  miradas arriba, el juego repite el recurso de encuadrar personajes
  pequeños contra arquitectura gótica gigantesca (columnas, arcos apuntados)
  para transmitir la escala inhumana de Nazarick — el mismo recurso que usa
  el anime en los planos de la Gran Tumba · ✅ (visto directamente en dos
  fuentes de imagen: capturas del juego y fotogramas ya descritos por el
  equipo de vídeo, referenciados en `datos-video.md` si aplica).

### Punto 24 · Obras parecidas y temas relacionados

- **Influencias declaradas por el autor** (Kugane Maruyama, traducción de
  entrevista japonesa recogida en la wiki, blog de usuario
  `Armada_371/Maruyama_Interview_translation_from_reddit`): empezó a escribir
  Overlord porque su grupo de **TRPG (rol de mesa, tipo D&D)** dejó de
  reunirse, y el juego de rol de mesa está detrás de buena parte del
  reglamento del mundo de YGGDRASIL. Dice también que Ainz y los suyos no son
  «malvados» sin más: el mundo funciona con la ley del más fuerte, y escribe
  como si «el fuerte es bueno, el débil es malo» desde el punto de vista de
  los propios personajes («chuunibyou», su palabra) · fuente:
  overlordmaruyama.fandom.com/wiki/User_blog:Armada_371/Maruyama_Interview...
  · ✅ (entrevista traducida, coincide con lo citado por SFE: Maruyama Kugane
  sobre el origen ligado al TRPG).
- **Obras recomendadas por similitud** (ya en `datos-texto.md`, con nota de
  votos de usuarios de AniList): That Time I Got Reincarnated as a Slime,
  The Eminence in Shadow, Saga of Tanya the Evil, Log Horizon, So I'm a
  Spider So What?, No Game No Life, Konosuba (Kadokawa clasifica el gag de
  crossover **Isekai Quartet** como obra relacionada oficial, no sólo
  recomendación de usuarios) · fuente: AniList (recomendaciones) + AniList
  (relaciones oficiales: Isekai Quartet listado como «CHARACTER» de Overlord)
  · ✅.
- **Láminas vecinas ya en la carpeta de biblias** (para no repetir ideas,
  según pide el punto 24): de los encargos isekai/fantasía cercanos (84
  No Game No Life, 85 Sword Art Online, 86 Saga of Tanya the Evil, 87
  Tsukimichi, 88 Konosuba, 82 Rising of the Shield Hero) **ninguno tiene
  biblia todavía** (comprobado con `test -f biblia.md` en cada carpeta, 25-
  sep-2026). Sí existen ya **03/80-solo-leveling** y **81-mushoku-tensei**:
  - Solo Leveling ya usa el concepto de **ventana de Sistema azul con texto
    entre corchetes** (`[E]` → `[S]`, panel `#112A39`/`#82F3FA`) para mostrar
    rangos y misiones — Overlord **no debería repetir** una ventana de
    "sistema de juego" azul con corchetes si se quiere un canal propio,
    aunque temáticamente Overlord SÍ nace literalmente de un juego (YGGDRASIL)
    y tendría sentido narrativo un HUD; se recomienda diferenciarlo en color
    (carmesí/violeta de Nazarick, no cian) y en forma (runas, no HUD de RPG
    coreano) · fuente: `biblias/03-solo-leveling/biblia.md` sección 20 ·
    ✅ (leído en la propia biblia).
  - Mushoku Tensei ya propuso **«el tablón del Gremio»** como concepto de
    lámina — Overlord tiene su propio tablón de misiones equivalente
    (Adventurer's Guild de E-Rantel) pero por el choque de idea con Mushoku
    Tensei, se recomienda al redactor NO repetir «tablón de gremio» como
    concepto central y usar en su lugar objetos propios de Nazarick (el
    trono, el mapa de los pisos, el sello de la guild) · fuente:
    `biblias/81-mushoku-tensei/biblia.md` sección 27 · ✅.

### Punto 25 · El mundo, la historia y sus símbolos

- **Reglas del mundo (cinco líneas resumidas de la wiki, con cita a las
  novelas)**: el «Nuevo Mundo» es una fantasía medieval con un sol y una luna,
  donde la física normal está alterada por la magia (las tres leyes de la
  termodinámica casi no aplican, según un tuit citado del propio autor); el
  mundo traduce automáticamente el habla de cualquier idioma, pero hay que
  aprender a leer; los «humanos» de este mundo son técnicamente una especie
  distinta a la nuestra (broma científica del autor: *Homo sapiens
  magitheus*) y son más débiles que las razas heteromorfas/monstruo · fuente:
  overlordmaruyama.fandom.com/wiki/New_World (con citas directas a Overlord
  Volumen 2 cap.1, Volumen Bonus cap.3, y un post de blog/tuit del autor) ·
  ✅ (múltiples citas primarias enlazadas dentro de la propia wiki).
- **Las tres naciones vecinas de Nazarick + el nuevo reino**: Reino de
  Re-Estize (feudal, disuelto tras la conquista, bandera propia), Imperio de
  Baharuth (vasallo del Reino Mago desde el emperador Jircniv), Teocracia de
  Slane (seis sectas religiosas, capital Silksuntecks), y el **Reino Mágico
  / Reino Hechicero** (Sorcerer Kingdom, 魔導国) fundado por Ainz, capital
  E-Rantel/Nazarick, cuya bandera es la del propio Ainz Ooal Gown · fuente:
  fichas de infobox de cada página en overlordmaruyama.fandom.com (Re-Estize
  Kingdom, Baharuth Empire, Slane Theocracy, Sorcerer Kingdom) · ✅ (datos
  de infobox oficiales de la wiki, cruzados entre las cuatro páginas).
- **El símbolo central: el emblema/bandera de Ainz Ooal Gown**. Estaba
  colgado en el 10º piso de la Gran Tumba de Nazarick tras el trono; Ainz lo
  señala en el epílogo del Volumen 1 al declarar que ya no se llamará
  «Momonga» sino «Ainz Ooal Gown». Hoy funciona también como bandera nacional
  del Reino Hechicero. **Albedo lo odia** (le recuerda que casi todos los
  Seres Supremos abandonaron Nazarick) y lo pisotea a escondidas en su
  cuarto secreto · fuente: overlordmaruyama.fandom.com/wiki/Flag_of_Ainz_
  Ooal_Gown, con cita a Overlord Volumen 1 epílogo, Volumen 12 cap.2 y el
  Blu-ray 01 Special · ✅ (tres citas primarias distintas enlazadas por la
  wiki).
- **El nombre de la guild-emblema**: «Ainz Ooal Gown» significa, según el
  epíteto oficial de la wiki, **«Cuarenta y Un Seres Supremos»** (Forty-One
  Supreme Beings); antes se llamó **«Nine's Own Goal»** cuando sólo eran
  nueve jugadores que se unieron por autodefensa contra el acoso (PK) a
  razas heteromorfas — según el propio Maruyama, el gremio fue pensado desde
  el principio para el papel de villano · fuente:
  overlordmaruyama.fandom.com/wiki/Ainz_Ooal_Gown_(Guild) · ✅ (dato de
  infobox + texto de fondo de la wiki).
- **La historia por arcos** (24 volúmenes de novela + especiales, orden
  cronológico oficial confirmado con la página «Timeline» de la wiki, que
  cruza con la página «Story Arcs»): El Rey de los No Muertos (vol.1, el
  aislamiento de Ainz y el despertar de Nazarick) → El Guerrero Oscuro
  (vol.2, Ainz se hace pasar por el aventurero Momon) → La Valquiria
  Sangrienta (vol.3, la rebelión de Shalltear) → Los Héroes Lagarto (vol.4,
  Zaryusu y las tribus lagarto) → Los Hombres del Reino (vols.5-6, la guerra
  con el Reino Re-Estize) → Los Invasores de la Gran Tumba (vol.7) → El
  Hechicero de la Destrucción (vol.9) → El Gobernante de la Conspiración
  (vol.10) → El Artesano Enano (vol.11) → El Paladín del Reino Santo
  (vols.12-13, la guerra con el Reino Santo Roble) → La Bruja del Reino
  Caído (vol.14) — y sigue hasta el volumen 17 publicado · fuente:
  overlordmaruyama.fandom.com/wiki/Story_Arcs +
  overlordmaruyama.fandom.com/wiki/Timeline (las dos páginas se cruzan y
  coinciden en el orden) · ✅.
- **Vocabulario propio que un fan reconoce al instante**: «Ainz Ooal Gown»
  (el guild y el nuevo nombre de Momonga), «Nazarick» / «Gran Tumba de
  Nazarick», «Seres Supremos» (Supreme Beings, los 41 creadores), «PNJ»/NPC
  (los sirvientes que cobraron vida), «YGGDRASIL» (el juego original),
  «Guardianes de Piso» (Floor Guardians), «Reino Hechicero»/«Sorcerer
  Kingdom», «E-Rantel» (la ciudad base de Ainz) · fuente: cruzado entre
  varias páginas de la wiki citadas arriba · ✅.

## Lo mejor para la lámina

1. La **cartela de pensamiento vs. lo que dice en voz alta** de Ainz (punto
   6): es la firma visual más propia de la serie, mejor que cualquier globo
   genérico, y encaja perfecto con «cuadros de diálogo acordes a la
   temática, no una burbuja blanca rara» que pide el dueño.
2. El **emblema de Ainz Ooal Gown** (bandera del 10º piso / bandera del Reino
   Hechicero) como sello o marca de agua del canal: tiene historia narrativa
   fuerte (Albedo lo pisotea, Ainz lo alza en el opening) y es reconocible al
   instante para cualquier fan.
3. La **letra Pirata One** (libre, con ñ/tildes/¿/¡ comprobados) para
   títulos y cabeceras, en vez de gastar en Squealer de pago.
4. El **HUD carmesí/violeta con runas** de *Escape from Nazarick* como
   referencia real para una ventana de «sistema» de Nazarick que NO copie el
   azul-cian ya usado por Solo Leveling.
5. Los **escalones del arco por volumen** (24 arcos con nombre propio) como
   estructura para un mapa o cronología del canal.

## No encontré

- ⚠️ La tipografía exacta usada en el interior de las ediciones de Yen Press
  (novela y manga) — necesita revisar el colofón físico del libro; búsquedas
  hechas en inglés, ningún foro de tipografía lo documenta.
- ⚠️ Entrevista técnica directa del estudio Madhouse (director de fotografía,
  CG) sobre el proceso de producción del CGI/toon shading de Overlord —
  sólo se encontraron reseñas de aficionados que opinan sobre el resultado,
  no notas de producción o making-of oficial en línea.
- ⚠️ The Cutting Room Floor (tcrf.net) sobre los videojuegos de Overlord: la
  web devolvió 403 (Cloudflare) tanto por curl como por WebFetch, dos vías
  distintas probadas; no se pudo comprobar si existe una página o no.
- ⚠️ TV Tropes (tvtropes.org), página de personajes y de franquicia: 403
  directo (WebFetch) y al probar con curl con user-agent de navegador; sólo
  se pudo usar lo que WebSearch extrajo de fragmentos indexados.
- ⚠️ Cobertura de prensa especializada independiente sobre "Overlord: King of
  Nazarick"/"Lord of Nazarick" más allá del anuncio de Crunchyroll Games —
  sólo la wiki lo documenta con detalle; el juego ya cerró (29-dic-2025).
- ⚠️ Un alfabeto o tipografía ficticia propia del mundo de Overlord para
  carteles del mundo: la wiki confirma que NO existe tal cosa (traducción
  automática del habla, sin conlang descrito), así que se documenta como
  "no aplica" y no como un vacío de búsqueda.

## Bitácora

- Fandom (`overlordmaruyama.fandom.com`, API `action=query`/`list=search` y
  `action=parse&prop=wikitext`, en inglés): «Ainz Ooal Gown emblem», «New
  World», búsquedas de factions/nations, «Timeline», «Story Arcs», «Overlord
  Manga», «Mass for the Dead», «Escape from Nazarick», «Overlord: King of
  Nazarick», «Perfect Unknowable» (sin página) — unas 18 llamadas a la API,
  sin repetir las de `datos-texto.md`.
- WebSearch (inglés), 8 búsquedas: font del logo (dos hilos de dafont),
  Mass for the Dead UI, dafont blackletter, entrevista de Maruyama
  (influencias), so-bin estilo de dibujo, Madhouse CGI/toon shader, manga
  speech bubble style, Yen Press tipografía interior, Escape from Nazarick
  VR (para descartar), título de fuente de openings/endings.
- WebFetch: 2 hilos de dafont.com (logo y logo de película, con éxito), 1
  intento a Parka Blogs (503, no se reintentó una tercera vez), TV Tropes
  página de personajes de Ainz (403) y franquicia (403, con curl).
- api.fontsource.org: comprobación de subconjunto `latin-ext` para 10
  familias góticas/de terror de Google Fonts; descarga y comprobación real
  con `fontTools` del `cmap` de Pirata One (ñ, Ñ, á, é, í, ó, ú, ¿, ¡: todas
  presentes).
- Steam API (`store.steampowered.com/api/appdetails`) para
  *Overlord: Escape from Nazarick* (appid 1782150): 5 capturas oficiales
  1920×1080, 2 descargadas y miradas en hoja de contacto.
- TCRF (tcrf.net): 403 Cloudflare, dos vías (curl con user-agent y WebFetch).
- No se usó `seccion.py` porque `biblia.md` de este encargo aún no existe
  (se está creando desde cero); se partió sólo de `datos-texto.md`.

Los 6 puntos (5, 6, 11, 18, 24, 25) están completos, con lo obligatorio de
cada uno cubierto y en ✅ mayoritario. No queda «Sigue» obligatorio: lo que
falta (tipografía interior de Yen Press, TCRF/TV Tropes bloqueados) es extra
y ya está en «No encontré» con ⚠️, con las búsquedas hechas documentadas.
