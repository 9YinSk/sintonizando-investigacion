# Vídeo — El castillo ambulante (investigador de vídeo: puntos 2, 4, 9, 10, 14)

Libreta de datos del investigador de vídeo, dentro del equipo de `99-el-castillo-ambulante`.
No repite lo de `datos-video.md` (AniList, Dailymotion, Internet Archive, MusicBrainz):
parte de ahí y comprueba, mira y amplía.

**Fuente principal mirada de verdad** (obligatorio del dueño: «no miras vídeos»):
película completa, doblada al francés con subtítulos franceses quemados, subida a
Internet Archive: `https://archive.org/details/howl-no-ugoku-shiro_202602` — vídeo
1920×1036, 7149,24 s (119 min 9 s). **Coincide con la duración oficial (119 minutos,
`https://ghibli.fandom.com/wiki/Howl%27s_Moving_Castle`) → ✅ dos fuentes** de que es
la película real completa. Bajada una sola vez con `fotogramas.py` (yt-dlp) y reutilizada
con symlinks en `/tmp/claude-0/trabajo/99-el-castillo-ambulante-video/` (carpetas
`overview`, `castillo_calcifer`, `melena_vuelo`, `guerra`, `final`, `rescate`,
`trailer_es`) para no volver a bajar los 2,2 GB cada vez. Mirada en tramos densos
(cada 15-25 s) del minuto 0 al 1:59, más las hojas generales cada ~3 min. Todas las
hojas e `indice.json` quedan en esa carpeta de trabajo (no en el repo).
`ffmpeg` no estaba instalado al empezar (`imageio_ffmpeg` chocaba con `libblas.so.3`);
se instaló con `apt-get install ffmpeg` (paquete del sistema, no un programa para
saltar bloqueos) y a partir de ahí `fotogramas.py` funcionó normal.

AnimeThemes volvió a fallar (HTTP 522, dos intentos: el de `recolectar.py` y uno mío) →
no hay openings/endings sueltos ahí porque es una película, no una serie con OP/ED en
AnimeThemes. YouTube no se tocó (pide iniciar sesión desde este servidor, como avisa
`AYUDANTE.md`): todo lo de vídeo sale de Internet Archive y Dailymotion.

## Punto 2 — Fotogramas de escenas icónicas (1080p+, con minuto)

Todos son de la copia de Internet Archive (1920×1036, ≈1080p) salvo que se diga otra
cosa. Enlace con `?t=` al segundo exacto. ✅ = escena que también describe la wiki
oficial de Ghibli (`ghibli.fandom.com/wiki/Howl's_Moving_Castle`, sección «Plot») o el
propio tráiler oficial; ⚠️ = sólo confirmado mirando el fotograma.

- Sophie caminando por el cielo de la mano de Howl, dedos entrelazados, escapando de la
  multitud tras el primer encuentro · min 6:40 ·
  `https://archive.org/details/howl-no-ugoku-shiro_202602?t=400` · **la imagen más
  usada para promocionar la película**: la wiki de Ghibli usa el mismo plano como
  imagen principal del artículo («Sophie walking across the sky with Howl») ✅
- La Bruja de la Landa maldice a Sophie (transformación en anciana, humo y caída al
  suelo) · min 14:20 · `…?t=860` · la sección «The Indelible Curse» de la wiki lo
  describe igual (Sophie sale maldita de la sombrerería) ✅
- Sophie conoce al espantapájaros Cabeza de Nabo en la colina, antes del castillo ·
  min 16:00-19:00 · `…?t=960` · wiki: «Sophie meets upon the hill the scarecrow Turnip
  Head» ✅
- Primera vista completa del castillo andante saliendo de la niebla (patas mecánicas,
  humo, torres) · min 19:40 · `…?t=1180` ✅ (coincide con el tráiler oficial español,
  min 0:20-0:35, ver punto 10)
- Sophie entra y conoce a Calcifer en la chimenea («¿Vous êtes Hauru?») · min 21:40 ·
  `…?t=1300` · wiki: «she meets the enchanted fire demon named Calcifer» ✅
- Trato de Sophie con Calcifer para romper su maldición mutua · min 30:00-31:00 ·
  `…?t=1800` · diálogo citado tal cual en la wiki («You promise to help me if I help
  you?») ✅
- Vuelo nocturno de Howl y Sophie sobre el lago/marisma de Porthaven, apoyados en la
  barandilla de la casa secreta · min 37:00-38:00 · `…?t=2220` ⚠️ (visto; la wiki
  confirma el sitio — «Porthaven Marshes» — pero no describe este plano exacto)
- Howl transformándose a medias en criatura alada de noche, volando sobre el mar ·
  min 40:20 · `…?t=2420` ⚠️
- El «ataque de histeria» de Howl: pelo teñido de negro por accidente, grita «¿Viste el
  color de mi pelo?», se derrumba junto a la chimenea, «¿de qué sirve vivir si no soy
  guapo?» · min 46:00-46:40 · `…?t=2760` · escena muy citada en reseñas y memes del
  fandom (ver punto 12 del investigador de voz; aquí sólo el fotograma) ⚠️
  (una fuente: el propio vídeo, pero es la escena más repetida en fan art según los
  hilos de r/ghibli revisados, p. ej. `https://www.reddit.com/r/ghibli/comments/1w71vn4/`)
- Howl completa su transformación en monstruo alado gigante para pelear en la guerra,
  Sophie grita «¡Hauru!» · min 1:31:50-1:34:10 · `…?t=5510` · wiki: «Howl is able to
  transform into a bird-like creature to interfere in the war» ✅
- Bombardeo aéreo nocturno sobre el pueblo, cielo rojo con aviones · min 1:34:30 ·
  `…?t=5670` · wiki: «the city is carpet-bombed by enemy aircraft» ✅
- Sophie destruye el castillo para salvar a Calcifer y perseguir a Howl, pelo ya
  blanco del todo · min 1:38:20-1:39:20 · `…?t=5900` · wiki: «Sophie moves everyone out
  of the castle... destroying the castle» ✅
- Flashback: la joven Sophie ve caer una estrella (Calcifer) y al joven Howl
  tragársela, origen del pacto · min 1:46:10-1:47:10 · `…?t=6370` · wiki, sección
  «The Boy Who Drank Stars»: «she sees Howl and Calcifer meet: Howl eats Calcifer, who
  gains his heart» ✅ (coincide además con el título de la pista 25 del disco,
  「星をのんだ少年」, «El chico que se tragó una estrella»: ver punto 9)
- Sophie devuelve el corazón (la llama de Calcifer) al pecho de Howl, manos brillando
  de azul · min 1:50:10-1:51:10 · `…?t=6610` · wiki: «places the heart back in Howl,
  resurrecting him» ✅
- Cabeza de Nabo recupera forma humana (era el príncipe hechizado) y la maldición de
  Calcifer se rompe · min 1:51:50-1:52:30 · `…?t=6710` ✅ (lo dice el propio subtítulo
  en pantalla, «Le sortilège de Calcifer a été défait»)
- Plano final: el castillo vuela sobre un campo en flor con la cabaña y el jardín
  pegados, Calcifer libre volando como una lucecita con alas · min 1:54:20-1:55:00 ·
  `…?t=6860` ✅ (plano de cierre, coincide con la portada de varias ediciones en DVD/BD)

## Punto 4 — Fondos y sitios: luz, paleta (hex medidos) y texturas reales

Paleta sacada con `herramientas/estilo.py` sobre el fotograma citado (medida, no de
memoria); el nombre del sitio, de la wiki de Ghibli (`Market Chipping`, `Porthaven`,
`Kingsbury` aparecen los tres, confirmados por búsqueda de texto en la wikitext ✅).

- **Sombrerería de la familia Hatter, Market Chipping** (interior, luz cálida de
  tienda) · min 2:58 · `…?t=178` · paleta: `#1C1513` `#472F22` `#60462C` `#88755F`
  `#A6A88B` — marrones y dorados apagados · textura de madera equivalente libre:
  ambientCG `Wood095` (CC0, `https://ambientcg.com/view?id=Wood095`)
- **Callejón/plaza de Market Chipping** (atardecer, adoquín) · min 5:56 · `…?t=356` ·
  paleta: `#3B3527` `#53463A` `#4A411D` `#735B4D` — ocres oscuros
- **Páramo/colina camino al castillo** (día despejado) · min 14:50 · `…?t=890` ·
  paleta: `#77714D` `#DDDACE` `#97AB46` `#A08963` `#74958F` — verde oliva, cielo casi
  blanco, muy alto en brillo (58%, medido)
- **Castillo andante, primera vista exterior** (niebla, atardecer) · min 19:40 ·
  `…?t=1180` · paleta: `#3B211F` `#545C62` `#5C3B2B` `#92552C` — óxidos y grises
  metálicos · textura de metal oxidado equivalente: ambientCG `CorrugatedSteel009`
  (CC0, `https://ambientcg.com/view?id=CorrugatedSteel009`) y `Metal063`
  (`https://ambientcg.com/view?id=Metal063`)
- **Castillo, interior junto a la chimenea de Calcifer** (fuego, penumbra) · min 21:40
  · `…?t=1300` · paleta: `#16120F` `#68342D` `#89533C` `#D97945` — el naranja
  `#D97945` es el color base de la llama de Calcifer
- **Porthaven, marisma secreta con la casa/balcón de Howl** (verde acuoso, de día) ·
  min 37:00 · `…?t=2220` · paleta: `#0D6C73` `#84AC4F` `#877444` `#CCB57B` — turquesa y
  verde vivo, el sitio más saturado medido (53%)
- **Porthaven, puerto pesquero** (barcos, buques de guerra) · min 43:20 · `…?t=2600` ·
  paleta: `#978F48` `#4A4C3D` `#7D743B` `#B6AB60` — caqui/oliva apagado, ambiente de
  guerra empezando
- **Castillo, vista de montaña con niebla azul-verdosa** (exterior de día) · min 38:20
  · `…?t=2300` · paleta: `#42493B` `#389FAA` `#536A60` `#D9D6C9` — el turquesa
  `#389FAA` domina el cielo/nieve
- **Kingsbury (capital), plaza con estatua ecuestre frente al palacio** (piedra, cielo
  despejado) · min 52:40 · `…?t=3160` · paleta: `#253227` `#207A92` `#A39B72`
  `#D0CFBA` — piedra clara y cielo azul-verdoso · textura de piedra equivalente:
  ambientCG `Metal063`/`CorrugatedSteel009` no aplican aquí; usar catálogo `PavingStones`
  de ambientCG (búsqueda vacía en el momento de mirar: **⚠️ no comprobé una ficha
  exacta**, queda pendiente)
- **Ruinas tras la transformación de Howl** (interior destruido, luz de humo) ·
  min 1:33:30 · `…?t=5610` · paleta: `#0F1A24` `#382B33` `#512B1F` `#DAB898` — azules
  muy oscuros y piel rosada, casi sin saturación de color ambiente
- **Cielo nocturno estrellado, escena del origen de Calcifer** (marisma, de noche) ·
  min 1:44:30 · `…?t=6270` · paleta: casi negro `#0A0A08` (68%) con acentos teal
  `#1E5356` `#2E6D6C` — sombreado plano (cel), no degradado, el único fotograma medido
  así: es la única escena "plana" de las diez medidas
- **Campo en flor final, castillo con cabaña volando** (día, primavera) · min 1:54:40
  · `…?t=6880` · paleta: `#35472E` `#526F40` `#7D9157` `#0A4D65` `#A4554C` — verdes de
  hierba, azul de cielo/lago, rojo de tejados
- Tela equivalente libre para el vestido verde de Sophie / cortinas de la casa:
  ambientCG `Fabric081C` (CC0, `https://ambientcg.com/view?id=Fabric081C`) ⚠️ (elegida
  por color, no verificada pieza por pieza contra el vestuario)

## Punto 9 — Música y sonido

- Banda sonora oficial: **「ハウルの動く城 サウンドトラック」** (Howl's Moving Castle
  Soundtrack), Joe Hisaishi (久石譲), Tokuma Japan Communications, 19-nov-2004 ·
  confirmado en dos fuentes independientes: MusicBrainz
  (`https://musicbrainz.org/release-group/464c5f95-7877-3701-92a3-292de7cbe7c5`) y
  Discogs (`https://api.discogs.com/releases/6200921`) ✅ — 26 pistas, lista completa
  sacada de MusicBrainz
- Tema principal (créditos de apertura): **「―オープニング―人生のメリーゴーランド」**
  ("Jinsei no Merry-Go-Round", "El carrusel de la vida"), pista 1, instrumental ·
  MusicBrainz + Discogs ✅
- Tema de cierre (créditos finales, con voz): **「―エンディング―世界の約束～人生のメリーゴーランド」**
  ("Sekai no Yakusoku ~ Jinsei no Merry-Go-Round", "La promesa del mundo"), pista 26 ·
  cantado por **Chieko Baishō** (voz japonesa de Sophie anciana), letra de Yumi Kimura
  y Shuntarō Tanikawa · confirmado en **tres** fuentes: Discogs (créditos de la pista,
  `extraartists`: Youmi Kimura, Shuntaro Tanikawa, Chieko Baisho), MusicBrainz y la
  wiki de Ghibli («Chieko Baisho... sing the theme song The Promise of the World»,
  `https://ghibli.fandom.com/wiki/Howl%27s_Moving_Castle`) ✅✅ — suena exactamente
  sobre el plano final del castillo volando (min 1:54:40-1:56:00): el subtítulo francés
  en pantalla dice «La promesse du monde» justo en ese tramo (`…?t=6880`), traducción
  literal del título de la canción
- Pistas que se pueden emparejar con escena por el propio título (mismo álbum, dos
  fuentes arriba) — sirven para saber qué suena en cada momento sin tener el audio
  transcrito:
  - 3 「空中散歩」("Paseo aéreo") → escena de caminar/volar por el cielo, min 6:40 y
    37:00 ⚠️ (coincidencia de título y escena, no timestamp exacto del cue)
  - 8 「消えない呪い」("La maldición que no desaparece") → maldición de la Bruja,
    min 14:20 ⚠️
  - 9 「大掃除」("Gran limpieza") → Sophie limpiando/cocinando en el castillo,
    min 27:40-28:40 ⚠️
  - 22 「戦火の恋」("Amor en el fuego de la guerra") → tramo de guerra y romance,
    min 1:20-1:40 ⚠️
  - 25 「星をのんだ少年」("El chico que se tragó una estrella") → origen de Calcifer,
    min 1:46:10-1:47:10 ✅ (mismo título que la sección «The Boy Who Drank Stars» de
    la wiki de Ghibli: dos fuentes independientes apuntan a la misma escena)
- Compositor confirmado también por la ficha de la propia wiki (`music = Joe Hisaishi`)
  ✅, tercera fuente además de MusicBrainz/Discogs
- Sonido: castillo con paso metálico pesado (clanc-clanc de las patas mecánicas),
  chisporroteo/crepitar de Calcifer al hablar, zumbido grave de motores de los
  bombarderos en la guerra, campana/silbato de tren al inicio · **⚠️ una sola fuente**
  (lo que se oye viendo la película; no encontré ficha de diseño de sonido en
  español/inglés con nombres de efectos concretos)
- Créditos de sonido vistos en pantalla al final (min 1:56:00-1:56:40, japonés):
  「音響」("sonido") y 「効果」("efectos") con varios nombres listados (p. ej.
  野口透 entre los créditos de 効果) · `…?t=6960` · ⚠️ (un solo fotograma, no crucé
  cada nombre con una segunda fuente — queda para quien complete el punto 8/18)
- No hay openings/endings de tipo «serie» en AnimeThemes (falló dos veces, HTTP 522):
  al ser película, el tema de apertura y cierre está dentro del propio metraje, no
  como clip suelto de streaming

## Punto 10 — Vídeos: tráileres oficiales, escenas, tendencias

- **Tráiler oficial español** (distribuidora Aurum, estreno en cines de España),
  mirado fotograma a fotograma cada 5 s: `https://www.dailymotion.com/video/x88np44`
  (mismo tráiler que en `datos-video.md`) · 2 min 48 s, 586×480 (resolución de la
  copia subida, no 1080p) · logotipo Aurum min 0:05, logo Studio Ghibli min 0:10,
  título «El Castillo Ambulante» min 1:05-1:10, cierre «MUY PRONTO / www.aurum.es»
  min 2:44 ✅ (la marca de agua y el logo de Aurum confirman que es material oficial
  de distribución, no un fan-edit)
- El tráiler muestra el **panel de control con botones de colores** de la puerta del
  castillo (min 1:10, `…video/x88np44?t=70`), que la wiki de Ghibli explica: cuatro
  colores llevan a cuatro sitios — verde el páramo, azul Porthaven, rojo Kingsbury,
  negro el frente de batalla (luego reordenados a verde/amarillo/rosa/negro) ✅ (dato
  cruzado entre el tráiler y `ghibli.fandom.com`)
- **Tráiler de reestreno por el 20 aniversario** (2024), también en español, más corto
  (0:56): `https://www.dailymotion.com/video/x91ac2m` · no mirado fotograma a fotograma
  (tiempo limitado), sólo confirmado que existe y su duración vía la API de
  Dailymotion ⚠️
- Otros tráileres/clips oficiales en español ya listados en `datos-video.md` (Sensacine,
  Vidaextra, Espinof, FilmAffinity, HobbyConsolas): mismo tráiler de Aurum re-subido
  por varios medios, comprobado que **no** son doblajes latinoamericanos (voz en
  castellano de España o sin diálogo) — el doblaje latino queda para el investigador
  de voz (punto 8)
- Streaming oficial confirmado (de `datos-video.md`, AniList): Netflix
  (`netflix.com/title/70028883`) y Max/HBO Max (dos fichas distintas, `max.com`) ✅
  (dos plataformas independientes lo listan)
- Tráiler japonés original de 2004: no se pudo bajar de YouTube (bloqueo de inicio de
  sesión en este servidor); el enlace de AniList (`youtube.com/watch?v=iwROgK94zcM`)
  queda sin mirar — **⚠️ pendiente si alguien tiene acceso a YouTube fuera de este
  contenedor**
- **Análisis en vídeo**: busqué en Dailymotion («Howl's Moving Castle explained») y
  sólo salieron clips cortos y repetidos de la propia película o de un cover de piano
  (`dailymotion.com/video/x4c7h1h` y similares, canal genérico «Howl s Moving
  Castle»), nada que sea un vídeo-ensayo real · **no encontré análisis en vídeo
  accesible desde aquí** (YouTube bloqueado, Dailymotion sin ese contenido)
- **Tendencias/fandom** (más punto 12/21 del investigador de voz, pero se anota aquí
  por ser "vídeo/tendencia"): hilos activos en `r/ghibli` sobre la película, señal de
  que sigue viva en el fandom en 2026: fan art de Howl y Sophie con más de 100 votos
  (`reddit.com/r/ghibli/comments/1wlhk3w/`, `reddit.com/r/ghibli/comments/1wnmrz6/`),
  preguntas sobre la trama del libro vs. la película con 1200+ votos
  (`reddit.com/r/ghibli/comments/1wh09ub/`) — vía Arctic Shift
  (`https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=ghibli&title=Howl`)
  ⚠️ (confirma que hay actividad, no mide TikTok directamente: TikTok no tiene API
  abierta desde aquí y no está en las herramientas del equipo)
- **No encontré tendencias de TikTok verificables**: ninguna herramienta del equipo
  llega a TikTok (ni siquiera indirectamente) y buscar "por fuera" iría contra "no
  instales programas de terceros para saltar bloqueos" — se deja para quien tenga
  acceso de navegador real

## Punto 14 — Poses analizadas (Howl, Sophie, Calcifer)

Todas con minuto y enlace `?t=` a la copia de Internet Archive (`…/howl-no-ugoku-shiro_202602`),
salvo que se diga otra cosa. Categoría según lo que pide el encargo (presentar,
explicar, celebrar, regañar, pensar, animar) cuando encaja.

### Howl (8 poses)
1. Caminando por el cielo, dedos entrelazados con Sophie, sonrisa tranquila, mirada al
   frente · min 6:40 · `?t=400` · **presentar/animar** (la rescata con calma, no con
   prisa) ✅ (misma imagen que usa la wiki como retrato del personaje con Sophie)
2. De pie junto a la chimenea, mano apoyada, hablándole a Calcifer con tono relajado de
   "esta es mi casa" · min 29:00-29:20 · `?t=1740` · **presentar** (primera vez que se
   le ve de cuerpo entero en su propio espacio)
3. Apoyado en la barandilla del balcón sobre la marisma, cuerpo de lado, mirando el
   paisaje con Sophie al lado · min 37:00-37:20 · `?t=2220` · **explicar** (le enseña
   su sitio secreto)
4. Semitransformado en ave nocturna, alas negras extendidas, volando sobre el mar ·
   min 40:20 · `?t=2420` · sin categoría de la lista (vigilar/espiar la guerra)
5. Agachado, manos aferrando el pelo ahora negro, hombros caídos, cara escondida ·
   min 46:00-46:20 · `?t=2760` · pose de **pánico/vergüenza** (no está en la lista del
   encargo pero es la pose más citada del personaje en el fandom)
6. Transformación completa en monstruo alado, cuerpo arqueado, plumas negras erizadas,
   pico/garras hacia el frente · min 1:32:10-1:32:30 · `?t=5530` · **regañar/atacar**
   (postura de amenaza, no de diálogo)
7. Joven, brazos abiertos hacia el cielo nocturno, a punto de tragarse una estrella
   caída (Calcifer) · min 1:46:50-1:47:10 · `?t=6410` · **pensar/asombro** (origen de
   todo el pacto)
8. Tendido, débil, recibiendo su corazón de vuelta en el pecho de manos de Sophie,
   ojos entreabiertos · min 1:50:30-1:51:10 · `?t=6630` · pose de **vulnerabilidad**
   (contraste total con la pose 6)

### Sophie (9 poses)
1. De pie en el mostrador de la sombrerería, ajustando un sombrero con las dos manos,
   concentrada · min 2:58 · `?t=178` · **trabajar/explicar**
2. Sujeta por Howl en el aire, un brazo levantado con los dedos entrelazados, cara de
   sorpresa tranquila · min 6:40 · `?t=400` · **sorpresa**
3. Encorvada de golpe por la maldición, manos en la cara, humo alrededor, cayendo de
   rodillas · min 14:20 · `?t=860` · **miedo** (transformación)
4. Ya anciana, entrando al castillo apoyada en su bastón, cuerpo muy encorvado pero
   mirada decidida hacia adelante · min 26:20-26:40 · `?t=1600` · **pensar/decidir**
5. Cocinando el desayuno, delantal puesto, moviendo la sartén con una mano y sirviendo
   con la otra · min 28:00-28:20 · `?t=1700` · **cuidar** (no está en la lista del
   encargo, pero es su pose "ama de casa" más repetida)
6. Manos en alto, boca abierta, reaccionando a los panfletos de guerra que caen del
   cielo · min 45:00-45:20 · `?t=2720` · **sorpresa/alarma**
7. Abrazando a su madre (la ex Bruja de la Landa), cara apoyada en su hombro, ojos
   cerrados · min 1:28:10-1:28:30 · `?t=5290` · categoría no listada: **cariño/consuelo**
8. De pie, con el pelo ya blanco del todo, dando una orden con la mano extendida hacia
   el castillo («Déplace le château») · min 1:39:20 · `?t=5960` · **animar/mandar**
   (es su pose de más autoridad en toda la película)
9. Sentada, sosteniendo el corazón de Calcifer/Howl entre las manos ahuecadas, luz azul
   reflejada en la cara, mirada tierna hacia abajo · min 1:50:50-1:51:10 · `?t=6650` ·
   **celebrar/amar** (clímax emocional de la película)

### Calcifer (7 poses)
1. Cara completa asomando entre los troncos encendidos, ojos muy abiertos mirando a
   Sophie de frente · min 21:40 · `?t=1300` · **presentar** (primera vez que se le ve
   entero)
2. Encogido a llama pequeña, ladeado, voz de miedo (según el subtítulo «Mamie!») ·
   min 22:40 · `?t=1360` · **miedo**
3. Llama estirada en horizontal bajo la sartén de Sophie, usado como fogón, cara de
   fastidio · min 28:00-28:20 · `?t=1700` · sin categoría de la lista: **quejarse/trabajar**
4. Encogiéndose de golpe, casi apagándose, suplicando «Hauru, arrête! Je vais
   m'éteindre!» · min 48:00-48:20 · `?t=2880` · **miedo/suplicar**
5. Reducido a un rescoldo pequeño y débil tras perder poder, apenas brasa ·
   min 1:30:50 · `?t=5450` · **debilidad** (no listada, pero clave para su arco)
6. Llama de tamaño normal, decidida, hablando con Markl «Je veux rejoindre Hauru» ·
   min 1:38:40 · `?t=5920` · **animar/decidir**
7. Ya libre de su pacto, volando como una lucecita con alas en el cielo abierto sobre
   el campo en flor final · min 1:54:20 · `?t=6860` · **celebrar** (única vez que se
   le ve fuera del fuego/castillo en toda la película)

## Lo mejor para la lámina

- El fotograma de Howl y Sophie caminando por el cielo (min 6:40) es LA imagen de la
  película: la misma wiki oficial de Ghibli la usa como retrato principal. Sirve para
  cualquier lámina que quiera transmitir "confianza/rescate".
- Paleta de Porthaven-marisma (`#0D6C73` `#84AC4F` `#CCB57B`) es la más saturada y
  "bonita" de las diez medidas: buena base de color si la lámina va a un canal cálido
  y acogedor.
- El tema "La promesa del mundo" (Sekai no Yakusoku), cantado por Chieko Baishō, es
  perfecto para citar en el texto del canal si se busca un tono nostálgico/romántico:
  suena justo sobre el plano final del castillo volando.
- La pose de Sophie dando la orden «Déplace le château» (min 1:39:20) es la única en
  la que ella manda con autoridad total: buena opción si el canal necesita un
  personaje "al mando" en vez de tierno.
- Calcifer volando libre al final (min 1:54:20) es la única imagen de él fuera del
  fuego: útil si se necesita un Calcifer "feliz" sin la chimenea de fondo.

## No encontré

- ⚠️ Tráiler japonés original (AniList lo enlaza a YouTube, bloqueado en este
  contenedor): no lo miré. Búsquedas hechas: ninguna alternativa en Dailymotion o
  Internet Archive con el tráiler japonés específico (sólo el tráiler español de
  Aurum y clips del propio filme).
- ⚠️ Análisis en vídeo (vídeo-ensayos tipo YouTube) sobre la película: sólo encontré
  clips cortos sin valor de análisis en Dailymotion (búsqueda: "Howl's Moving Castle
  explained", "Howl's Moving Castle analysis" — no hice la segunda por límite de
  tiempo, pero la primera no dio nada útil).
- ⚠️ Tendencias de TikTok: no hay herramienta del equipo que llegue a TikTok; sólo
  pude confirmar actividad de fandom en Reddit (r/ghibli), no en TikTok específicamente.
- ⚠️ Créditos de diseño de sonido/efectos con nombre y rol exacto: los vi en pantalla
  (japonés, min 1:56:00-1:56:40) pero no crucé cada nombre con una segunda fuente
  (créditos de Blu-ray, IMDb, etc.) por tiempo.
- ⚠️ Textura real equivalente para la piedra de la plaza de Kingsbury: busqué
  "PavingStones" en la API de ambientCG y no devolvió resultados en el momento de
  mirar; no probé otras palabras clave (p. ej. "Cobblestone", "Stone") por tiempo.
- No aplica: la película no tiene openings/endings sueltos tipo serie (AnimeThemes
  falló dos veces, HTTP 522, y de todas formas no tendría fichas para películas) — el
  tema de cierre está dentro del propio metraje, ya citado en el punto 9.

## Bitácora de búsqueda

- Español: "El castillo ambulante tráiler" (ya en `datos-video.md`, Dailymotion);
  comprobación de resoluciones vía API de Dailymotion.
- Inglés: `ghibli.fandom.com` — búsqueda de texto `srsearch=Howl's Moving Castle sound
  design`, lectura completa del wikitext de la página `Howl's Moving Castle`
  (secciones Plot, cast, música, ficha técnica); confirmación de "Market Chipping",
  "Porthaven", "Kingsbury" por conteo de apariciones en el wikitext.
- Japonés: nombres de las 26 pistas del álbum de Joe Hisaishi vía MusicBrainz
  (`release/7288e3eb-ef4e-48ce-84fe-f85e745e9cce`) y Discogs (`releases/6200921`),
  leídos y emparejados a mano con las escenas vistas.
- Herramientas de datos (no buscador web, cuenta aparte): `curl` directo a
  `musicbrainz.org`, `api.discogs.com`, `api.dailymotion.com`, `archive.org/metadata`,
  `ambientcg.com/api/v2`, `arctic-shift.photon-reddit.com` — ninguna gastó cupo del
  buscador.
- Intentos fallidos (máximo dos por sitio, como pide `AYUDANTE.md`): AnimeThemes
  (HTTP 522, dos veces); `ja.wikipedia.org` API (HTTP 429, un intento, no se insistió
  porque `ghibli.fandom.com` ya daba lo mismo confirmado); VGMdb (respuesta vacía, un
  intento, sustituido por Discogs).
- Vídeo mirado de verdad (obligatorio): película completa recorrida en tramos densos
  (0:00-10:05, 10:20-31:20, 36:40-53:20, 1:27:30-1:45:50, 1:45:50-1:59:09) más una
  pasada general cada ~3 min de punta a punta; tráiler oficial español completo
  (2:48) fotograma a fotograma cada 5 s. Total: más de 250 fotogramas mirados con
  `Read`, no sólo generados.

Sigue: nada obligatorio pendiente de mis puntos (2, 4, 9, 10, 14) — quedan sólo los
⚠️ de «No encontré» (textura de piedra de Kingsbury, tráiler japonés vía YouTube,
créditos de sonido cruzados) por si alguien con más tiempo o acceso a YouTube quiere
completarlos.
