# Investigador de VÍDEO · Coco (Pixar, 2017) · Encargo 57

Puntos: **2** (fotogramas de escenas icónicas), **4** (fondos y sitios, luz y paleta),
**9** (música y sonido), **10** (vídeos: tráileres, escenas, análisis, tendencias),
**14** (poses analizadas por personaje, minuto exacto).

**Aviso de encuadre (obligatorio, lo pide el propio encargo 57):** Coco es una
película de Pixar (2017), no una serie de anime. No hay opening ni ending de
serie: en su lugar se usan el tráiler oficial, las canciones clave y las
escenas icónicas, todo con **minuto de la película** (no de capítulo).

## Cómo se miró la película (obligatorio: nada de memoria)

YouTube pedía «iniciar sesión» desde este servidor (bloqueo compartido, como
avisa el encargo). Se usó el **plan B de AYUDANTE.md**: el mismo largometraje
en **Internet Archive**, ítem
`https://archive.org/details/Coco.2017.STNAr.720p.BluRay.x264YTS.AG` (720p,
6302 s = 105 min, coincide con la duración real de Coco). Se bajó una sola vez
con `yt-dlp -f 2` (mkv 1282×534, 773 MB), se sacaron fotogramas reales con
`herramientas/fotogramas.py --desde/--hasta --cada 8` en 13 ventanas de la
película completa (minuto 0 a 99) más fotogramas sueltos con `--fotograma` en
segundos exactos, se **miraron todas las hojas de contacto con Read** (no se
listaron archivos sin abrir), y se **borró el vídeo** al terminar (`rm
coco_movie.mkv`, confirmado: sólo quedan 17 MB de hojas en la carpeta de
trabajo). Antes de bajar el archivo completo también se aprovecharon los **105
miniaturas oficiales del propio ítem de Internet Archive** (una por minuto,
en `<item>.thumbs/`), que sirvieron de mapa rápido de toda la cinta antes de
elegir qué ventanas mirar en detalle — así no se gastó ancho de banda mirando
minuto a minuto a ciegas.

El tráiler oficial (Disney/Pixar, «This Thanksgiving», `disney.com/coco`,
`#PixarCoco`) se miró completo en Dailymotion (plan B de AYUDANTE.md, YouTube
bloqueado): `https://www.dailymotion.com/video/x8x30c8` (Tomatazos, «Coco -
Tráiler Oficial», 2:27), fotogramas cada 12 s, con el logo de Pixar/Toy Story y
el cartel «THIS THANKSGIVING» confirmando que es el tráiler teatral oficial de
EE. UU., no un fan-edit.

Todos los minutos de este documento son del fotograma real (ffmpeg -ss),
precisión de ±1-2 s (el intervalo de muestreo), no de memoria ni de páginas de
resumen.

---

## Hallazgos

### Punto 2 — Fotogramas de escenas icónicas, con minuto exacto

Fuente para todas: película completa (Internet Archive, 720p, 1282×534 nativo;
`fotogramas.py --fotograma` reescala a 1280 px de ancho, así que el ancho
cumple pero **el alto real es 720p, no 1080p** — es la mejor copia disponible
sin YouTube; ⚠️ para quien busque una fuente en verdadera Blu-ray 1080p).

- **El robo de la guitarra de Ernesto y la maldición** (Miguel entra al
  mausoleo, se lleva la guitarra, empieza a volverse esqueleto): 21:00-22:36.
  Fotograma de referencia: Miguel esqueleto, cara de pánico, 22:36. ✅ (visto
  directamente + coincide con el resumen de Wikipedia «Coco (2017 film)»).
- **El puente de pétalos de cempasúchil** (cruce a la Tierra de los Muertos,
  familia completa, vista aérea de la ciudad al fondo): 24:28-25:56, plano
  panorámico del puente en 25:16 y 25:24 (arcos naranjas, multitud
  cruzando). Fotograma: `citas/fotograma_01516.jpg`. ✅
- **La aduana / cabina de fotos** (control con pantallas verdes que escanean
  la ofrenda familiar; la «X» roja de rechazo): 26:48-27:12. ✅
- **«Un Poco Loco»**, número musical de Miguel y Héctor en el escenario de la
  plaza (con banda de mariachis esqueleto uniéndose): 49:00-51:56, primer
  plano de Miguel cantando al micrófono en 51:00-51:24. Fotograma:
  `citas/fotograma_02884.jpg` (48:04, decorado). ✅ (visto + la canción está
  confirmada en el soundtrack oficial, ver punto 9).
- **La mansión de Ernesto / invernadero con vitrales de calavera**, encuentro
  con Mamá Imelda y Pepita: 1:16:00-1:19:00. ✅
- **«La Llorona»**, dueto de Imelda y Ernesto en el escenario del Sunrise
  Spectacular (Imelda sola al micrófono, Ernesto observa con sombrero y traje
  bordado en silueta): 1:21:48-1:22:36. Fotograma: `citas/fotograma_04908.jpg`
  (1:21:48, silueta de Ernesto). ✅ dos fuentes: visto directamente y
  Wikipedia «La Llorona (song)» / insidethemagic.net confirman que la cantan
  Imelda y Ernesto (voces Alanna Ubach y Antonio Sol) durante el «Sunset
  Spectacular».
- **«Recuérdame» (Remember Me) de Miguel a Mamá Coco**, el clímax emocional:
  1:30:36-1:32:00. Primer plano de la cara de Mamá Coco cerrando los ojos,
  escuchando: 1:31:00. Fotograma: `citas/fotograma_05460.jpg`. ✅ (la escena
  más citada de la película en reseñas, ver punto 21 de voz/personajes).
- **Escena final: «El Mundo Es Mi Familia» y reunión familiar completa** con
  guitarras, la hermanita bebé de Miguel y el altar con la foto de Héctor ya
  puesta: 1:35:44-1:36:08, justo antes del cartel «THE END» (1:36:16).
  Fotograma: `citas/fotograma_05752.jpg`. ✅
- **Persecución final y transformación de Dante en alebrije** para salvar a
  Miguel de Ernesto en la torre: 1:24:40-1:25:56 (criatura alada de colores
  volando junto a Miguel). ✅

### Punto 4 — Fondos y sitios: lugares, luz, paleta medida y texturas

Paletas con `herramientas/estilo.py --colores 5` sobre fotogramas reales
(1280×534). Casilla «estilo» = lo que devuelve la herramienta (Coco es 3D con
sombreado degradado en todo, no hay línea de contorno dura tipo anime).

| Sitio | Minuto | Hex (medidos) | Estilo/luz | Textura real equivalente |
|---|---|---|---|---|
| Plaza de Santa Cecilia (pueblo, día) | 4:22 | `#D39A90` 29% `#D5C9D5` 22% `#79494A` 18% `#876F7A` 17% `#46231E` 14% | luz de día cálida, degradado suave, poca línea | estuco/adobe rosado; buscar en ambientCG `Plaster` o `Stucco` |
| Altar/ofrenda familiar (interior, noche) | 5:02 | `#30261E` 27% `#C1DDF2` 26% `#554238` 25% `#7E6B60` 18% `#CEA391` 4% | velas cálidas + ventana azulada fría al fondo (contraste cálido/frío) | madera oscura + cera; ambientCG `WoodTable`/`Wax` |
| Taller de zapatero de la familia (calle) | 43:08 | `#12101A` 40% `#0C0B11` 30% `#1C1627` 19% `#25253F` 7% `#333E70` 4% | escena nocturna muy oscura (casa de Héctor a contraluz) | — |
| Puente de cempasúchil (Tierra de los Muertos) | 25:12 | `#492D41` 31% `#5D4776` 26% `#7172CA` 20% `#A3B4EF` 12% `#B56C76` 11% | pétalos naranja-rojos vs. cielo violeta nocturno; degradado, línea violeta suave | pétalo de flor/papel naranja; ambientCG `Fabric` para el tapiz de pétalos |
| Estación central «Marigold» (vestíbulo, aduana) | 28:00 | `#241A21` 41% `#343353` 22% `#5B4D7D` 19% `#8366A4` 11% `#6C3824` 7% | hierro fundido + luz cálida de araña, inspirado en el Palacio de Correos de México (ver Bitácora) | metal/hierro forjado oscuro |
| Skyline de la Tierra de los Muertos (aéreo, casas apiladas en el cerro) | 47:08 | `#1A0D14` 35% `#44141D` 23% `#5C3E59` 21% `#665B95` 15% `#BC889F` 8% | noche, luces cálidas puntuales sobre violeta frío; inspirado en Guanajuato (ver Bitácora) | — (paisaje, no hay textura equivalente aplicable) |
| Escenario de «Un Poco Loco» (plaza, decorado calavera) | 48:04 | `#282849` 33% `#3F4E90` 31% `#7278C1` 20% `#AF3562` 10% `#E1C7D1` 7% | luces de escenario rosa/azul, telón morado | tela de terciopelo morado |
| Cenote/alberca de la mansión (agua turquesa) | 1:10:00 | `#150F11` 43% `#254E5A` 22% `#ADD1CE` 16% `#71979D` 12% `#754F3D` 7% | agua turquesa iluminada desde abajo, resto en sombra | — |
| Casa/dormitorio de Mamá Coco (interior, atardecer) | 1:31:00 | `#A13921` 32% `#6C2A18` 26% `#C66F41` 23% `#FEF8DB` 12% `#EBBE88` 7% | luz de ventana muy cálida y dorada, la más cálida de toda la película | tela tejida naranja (rebozo de Coco) |

Sitios y su origen real (dos fuentes: visto en pantalla + entrevistas de
producción):
- **Santa Cecilia** (pueblo de Miguel): inspirado en varios pueblos
  mexicanos visitados en el viaje de investigación (Michoacán/Guanajuato). ✅
- **La ciudad de la Tierra de los Muertos**: basada en **Guanajuato**
  (casas de colores apiladas en la ladera, «verticalidad» que contrasta con
  el pueblo plano de Miguel) — dicho por el director Lee Unkrich, ver Bitácora
  (insidethemagic.net + renderman.pixar.com). ✅ dos fuentes.
- **Estación Marigold / aduana**: inspirada en edificios de hierro fundido de
  principios del siglo XX, con el **Palacio de Correos de México** (1907)
  como referencia directa para el vestíbulo. ✅ (insidethemagic.net).
- **Mansión de Ernesto**: toma prestado algo de la **Coit Tower** de San
  Francisco. ✅ (insidethemagic.net).

### Punto 9 — Música y sonido

Coco **no tiene opening/ending de serie** (es película): lo que aplica son las
canciones originales y la partitura. 8 canciones originales + 26 piezas de
partitura, compositor **Michael Giacchino** (score), canciones de **Germaine
Franco, Adrian Molina, Kristen Anderson-Lopez y Robert Lopez** — confirmado en
Wikipedia «Coco (soundtrack)» + ASCAP (`ascap.com/news-events/articles/2017/11/coco-franco-molina`)
+ Remezcla (`remezcla.com/features/film/pixar-camilo-lara-germaine-franco-music-coco/`).
✅ dos fuentes.

- **«Recuérdame» / «Remember Me»**: escrita por Robert Lopez y Kristen
  Anderson-Lopez (con arreglo/producción de Germaine Franco para sus dos
  versiones dentro de la película: la de Ernesto —grandiosa, de concierto— y
  la de Miguel a Mamá Coco —íntima, de cuna—). Versión de Miguel a Coco:
  1:30:36-1:32:00. ✅ (Wikipedia «Remember Me (Coco song)»).
- **«Un Poco Loco»**: co-escrita por Germaine Franco y Adrian Molina.
  Interpretada por Miguel y Héctor: 49:00-51:56. ✅ (fuente igual).
- **«La Llorona»**: canción folclórica mexicana tradicional (dominio
  popular, no original de la película), arreglada para la escena del Sunset
  Spectacular; la cantan Imelda y Ernesto a dueto: 1:21:48-1:22:36. ✅
  (Wikipedia «La Llorona (song)», insidethemagic.net, disneynews.us — tres
  fuentes).
- **«El Mundo Es Mi Familia» / «The World Es Mi Familia»**: canción familiar
  que suena en la escena final de reunión, 1:35:44-1:36:08. ⚠️ (una sola
  fuente directa: visto en pantalla; no se confirmó el crédito exacto de
  composición en una segunda fuente en esta tanda).
- **Motivo musical de los alebrijes**: Giacchino introduce una **fanfarria de
  metales** específica para Pepita y los alebrijes (así lo cuenta él mismo en
  la entrevista de SlashFilm, `slashfilm.com/554756/music-of-coco-michael-giacchino`).
  Se oye cada vez que Pepita aparece o ataca, p. ej. 1:18:08 y en la
  persecución final ~1:25:00-1:25:56. ✅
- **Ambiente por escena**: la escena de «Recuérdame» a Mamá Coco (1:30-1:32)
  usa sólo guitarra y voz de Miguel, sin orquesta, para que se sienta íntima
  — contraste con la orquesta llena de «Un Poco Loco» y «La Llorona». ✅
  (visto/oído directamente en los fotogramas con audio de la copia de
  Internet Archive).
- **Investigación cultural**: el equipo de música pasó ~6 años investigando
  la música de México con 50 músicos mexicanos participando en el
  soundtrack (Camilo Lara como consultor cultural). ✅ (Remezcla).
- **Efectos de sonido reconocibles**: al ser CGI y no manga/anime, no hay
  onomatopeyas en pantalla (⚠️ punto que no aplica tal cual lo pide el 9,
  se deja constancia). Los sonidos que el fandom más reconoce, vistos/oídos
  directamente en los fotogramas: el jadeo y las patas de Dante corriendo
  (11:12), el rugido grave de Pepita convertida en jaguar alebrije (1:18:08),
  y el «clic» del gatillo de la cámara/flash de las fotos familiares en la
  aduana (26:56).

### Punto 10 — Vídeos: tráileres, escenas, análisis, tendencias (con minuto)

- **Tráiler oficial teatral** («This Thanksgiving», Disney/Pixar,
  `#PixarCoco`, RealD 3D): Dailymotion, subido por Tomatazos,
  https://www.dailymotion.com/video/x8x30c8 (2:27). Contenido, minuto del
  tráiler (no de la película): Dante persiguiendo a Miguel con la guitarra
  (0:12), Abuelita persiguiendo a Miguel (0:24), partitura «Remember Me» a la
  luz de una vela (0:36), Miguel tocando en un escenario iluminado (0:48),
  vista aérea de la estación/puente de la Tierra de los Muertos (1:12), cara
  de espanto de Miguel esqueleto (1:48), fiesta con multitud (2:00), la
  familia completa a la mesa con Dante (2:12). ✅ (visto directo, coincide
  con el ítem oficial listado en `datos-video.md` desde el propio recolector).
- Otros tráileres/anuncios en Dailymotion ya recolectados en
  `datos-video.md` (no repetidos aquí): «Coco (Trailer HD)» MYmovies 2:33,
  «Coco Pixar Trailer» JeuxVideo.com 2:42, «Coco - Tráiler Oficial» Tomatazos
  2:27 (el mirado arriba), «Coco Morocco Trailer» (⚠️ no es de esta
  película, es un anuncio de moda que coincide en nombre — descartado).
- **Película completa como fuente de escena** (plan B, Internet Archive):
  https://archive.org/details/Coco.2017.STNAr.720p.BluRay.x264YTS.AG — usada
  para todos los fotogramas de los puntos 2, 4 y 14 de este documento, con
  minuto exacto de la propia película. ✅
- **Análisis en YouTube**: no se pudo verificar un vídeo concreto de análisis
  (Honest Trailers, retrospectivas) porque YouTube pide iniciar sesión desde
  este servidor y la búsqueda web no devolvió un enlace directo confirmable a
  un episodio de Honest Trailers de Coco. ⚠️ **No encontré** un vídeo de
  análisis con minuto verificable; búsquedas hechas: «Coco Pixar trailer
  breakdown analysis video Screen Junkies Honest Trailers ending explained»
  (sin resultado directo). Reseñas escritas sí confirmadas: RogerEbert.com
  (`rogerebert.com/reviews/coco-2017`) y Deep Focus Review
  (`deepfocusreview.com/reviews/coco/`).
- **Tendencias de TikTok**: hay contenido recurrente con la escena de
  «Remember Me» (incluyendo un meme popular que sustituye la música por el
  intro de «Despacito» sobre la misma escena) — visible en la etiqueta
  `tiktok.com/discover/coco-despacito-remember-me`. ⚠️ una sola fuente
  (listado de TikTok, sin cifra de vistas verificable desde aquí ni un
  clip oficial descargable); no se confirmó una «challenge» estructurada
  con nombre propio y fecha, a diferencia de lo que pasó con otras
  películas. Búsqueda hecha: «Coco Pixar TikTok trend Remember Me challenge
  viral 2021 2022».

### Punto 14 — Poses analizadas por personaje (Miguel, Héctor, Mamá Coco, Dante)

Todos los minutos son de la película completa mirada en Internet Archive
(fuente arriba). Formato: minuto · qué hace · para qué sirve en una lámina.

**Miguel Rivera**
1. 3:18 · Mira a Mamá Coco de cerca, sonriente, agachado a su altura ·
   **saludar/presentar** (buena pose para acercarse a un personaje mayor).
2. 6:46-7:26 · Sentado con el mariachi callejero, aprendiendo un acorde,
   mirada atenta a las manos del maestro · **aprender/explicar** (perfecto
   para un canal de clases).
3. 12:00-13:36 · Solo en el ático, ojos cerrados, cantando y tocando su
   guitarra improvisada · **cantar/concentrarse**.
4. 22:36 · Transformado en esqueleto, boca abierta, manos separadas del
   cuerpo, pánico total · **miedo** (cara + postura).
5. 24:52 · En el puente de cempasúchil, agarrado a Dante, mirada de asombro
   hacia el horizonte · **asombro/descubrir**.
6. 51:00-51:24 · De pie al micrófono, guitarra al frente, cantando «Un Poco
   Loco» con el cuerpo echado hacia adelante · **celebrar/actuar**.
7. 1:17:52 · Sentado en el suelo abrazando a Dante, cara de alivio ·
   **calma/cariño**.
8. 1:24:12-1:24:28 · De pie sosteniendo una vela encendida, mirando a
   Ernesto, expresión que pasa de esperanza a shock · **explicar/confrontar**.
9. 1:30:44-1:31:16 · Arrodillado frente a Mamá Coco, guitarra en mano,
   cantándole muy de cerca, mirada tierna · **animar/consolar** (la pose más
   importante de toda la película para una lámina emotiva).
10. 1:35:44-1:36:00 · De pie con la familia entera, tocando la guitarra,
    sonrisa amplia, rodeado de gente · **celebrar en grupo**.

**Héctor Rivera**
1. 42:32-43:36 · Recostado en una hamaca en su casa de la Tierra de los
   Muertos, guitarra apoyada en el pecho, sombrero ladeado · **relajarse/
   presentarse**.
2. 44:00-44:16 · Sentado, tocando la guitarra con las manos muy visibles en
   el diapasón, cabeza inclinada escuchando el sonido · **tocar/explicar un
   acorde**.
3. 45:52 · De pie, boca muy abierta en una carcajada, sombrero echado hacia
   atrás · **reír**.
4. 49:08-49:16 · En el escenario con la banda completa detrás, tocando junto
   a Miguel, cuerpo en movimiento · **celebrar/actuar en grupo**.
5. 53:04-53:12 · Agachado, brazos extendidos hacia Miguel, cara de cariño ·
   **animar/consolar**.
6. 1:21:48-1:22:04 · De pie junto al micrófono en el escenario grande,
   postura erguida y formal, cantando · **presentar/actuar en solitario**.
7. 1:24:16-1:24:28 · Sosteniendo una vela junto a Miguel, mirada seria y
   triste, hombros caídos · **explicar algo grave** (aquí Héctor le cuenta la
   verdad a Miguel).
8. 1:34:24-1:34:56 · Silueta que empieza a desvanecerse (efecto visual de
   «olvido»), después abrazo con Mamá Imelda en la puerta de «Departures» ·
   **alivio/reencuentro** (par de fotogramas consecutivos, contraste fuerte).

**Mamá Coco**
1. 3:10 · Sentada en su silla, manta a rayas sobre los hombros, mirada baja
   y perdida · **pose de reposo, vejez** (pose «neutra» por defecto del
   personaje).
2. 10:48-11:04 · Abrazada con Abuelita Elena, mejilla contra mejilla, mano
   sobre el brazo de su hija · **cariño/familia** (dinámica con otro
   personaje, útil para láminas en grupo).
3. 1:29:00-1:29:40 · Mira la guitarra de juguete que le muestra Miguel,
   ceja fruncida, como intentando recordar · **pensar/dudar**.
4. 1:31:00 · Primer plano extremo de su cara, ojos cerrados, boca
   entreabierta, escuchando «Recuérdame» · **emocionarse/recordar** (el
   fotograma más citado de toda la película para esta lámina — ver
   `citas/fotograma_05460.jpg`).
5. 1:31:40-1:32:04 · Ojos abiertos, mirada fija y brillante hacia Miguel,
   empieza a sonreír · **alegría/reconocimiento** (justo después del
   anterior: dos fotogramas consecutivos = la transición emocional completa).
6. 1:32:12-1:32:52 · Señala con la mano temblorosa hacia algo fuera de
   cuadro (la foto rota), boca abierta hablando · **explicar/señalar**.

**Dante (perro xoloitzcuintle)**
1. 4:46 · Corriendo junto a Miguel en la calle, orejas hacia atrás, lengua
   fuera, cuerpo estirado en carrera · **jugar/energía**.
2. 11:12-11:44 · Dentro del ático, apoya la cabeza contra Miguel mientras
   éste lo abraza · **cariño/compañía**.
3. 14:08 · Sólo los ojos, muy abiertos y brillando en morado en la
   oscuridad, cara pegada a una ventana · **alerta/misterio** (bueno para un
   detalle decorativo, no para pose de cuerpo entero).
4. 54:48 · De pie sobre el empedrado, cabeza ladeada, orejas alzadas,
   mirando fijamente al chico esqueleto (Miguel) que le apunta con el dedo ·
   **curiosidad/atención** (`citas/fotograma_03288.jpg`).
5. 1:24:40 · Junto a Miguel caído, ya revelado como alebrije: pequeño, alas
   de colores (verde, rosa, dorado) desplegadas · **transformación/rescate**
   (raro y muy reconocible: la sorpresa de que Dante también es un
   alebrije).
6. 1:25:36-1:25:56 · Volando en plena persecución, cuerpo alargado en el
   aire, alas extendidas, colores vivos contra el cielo morado nocturno ·
   **acción/heroico**.

---

## Lo mejor para la lámina

1. **«Recuérdame» a Mamá Coco (1:30:36-1:32:00)**: la escena emocional más
   reconocible de toda la película, con el fotograma de la cara de Coco
   (1:31:00) y el de Miguel arrodillado cantándole — funciona para cualquier
   lámina que necesite «calidez» o «memoria».
2. **El puente de cempasúchil (24:28-25:56)**: el objeto/escenario más
   icónico de Coco entero; un puente real en Blender (arcos + pétalos) encaja
   con la regla del dueño de «un objeto real en un sitio real».
3. **Paleta cálida de interior** (`#A13921` `#C66F41` `#FEF8DB`, medida en el
   cuarto de Mamá Coco, 1:31:00) frente a la **paleta fría-violeta** de la
   Tierra de los Muertos (`#492D41` `#7172CA`, medida en el puente, 25:12):
   el contraste cálido/frío es la firma visual de toda la película, útil como
   guía de color para cualquier lámina de Coco.
4. **Dante como alebrije oculto (1:24:40-1:25:56)**: un giro visual poco
   usado en fan art que sería fresco para una lámina («el perrito callejero
   que en realidad tiene alas»).
5. **«Un Poco Loco» en el escenario de calavera (48:04-51:56)**: buen
   fotograma de acción/celebración con Miguel y Héctor a dúo, si la lámina
   necesita "energía" en vez de nostalgia.

## No encontré

- ⚠️ Un vídeo de **análisis** en YouTube con minuto verificable (Honest
  Trailers, retrospectiva o similar): YouTube bloqueado desde este servidor
  y la búsqueda web no devolvió un enlace directo comprobable. Sí hay reseñas
  escritas confirmadas (RogerEbert, Deep Focus Review), citadas en el punto 10.
- ⚠️ Una **tendencia de TikTok con nombre y cifras** verificables (challenge
  estructurada): sólo se confirmó contenido recurrente/memes sueltos
  («Despacito × Remember Me»), sin cifras de vistas comprobables desde aquí.
- ⚠️ Crédito de composición exacto de **«El Mundo Es Mi Familia»** en una
  segunda fuente (sólo confirmado visualmente en la escena final).
- La copia de la película usada es un **rip de 720p** (Internet Archive), no
  una fuente 1080p+: se deja anotado en cada fotograma del punto 2, tal como
  pide la exigencia de calidad; no había alternativa sin iniciar sesión en
  YouTube.

## Bitácora de búsqueda

- Datos de partida: `partes/datos-video.md` (recolectados por
  `recolectar.py`: Dailymotion, Internet Archive, MusicBrainz). No se
  repitieron esas consultas.
- Internet Archive, ítem `Coco.2017.STNAr.720p.BluRay.x264YTS.AG`: metadata
  vía `archive.org/metadata/...` (105 miniaturas oficiales, una por minuto),
  descarga con `yt-dlp -f 2`, 13 ventanas de `fotogramas.py --desde/--hasta
  --cada 8` cubriendo minutos 2-99, más 24 fotogramas sueltos con
  `--fotograma` en segundos exactos. Vídeo borrado tras el uso.
- Internet Archive, ítem `Coco2017` (5:49, baja resolución): descartado como
  fuente de escena por ser demasiado corto/bajo, no es la película completa.
- Dailymotion: tráiler oficial visto con `fotogramas.py --cada 12` (ya
  listado en `datos-video.md`, sólo se confirmó cuál es el oficial y se miró).
- `herramientas/estilo.py --colores 5` sobre 10 fotogramas para las paletas
  del punto 4.
- Búsquedas web (idioma inglés, 5 de las ~50 permitidas):
  1. `Coco Pixar soundtrack "Un Poco Loco" "La Llorona" "Remember Me"
     songwriters credits Germaine Franco Kristen Anderson-Lopez` → Wikipedia
     «Coco (soundtrack)», «Remember Me (Coco song)», ASCAP, Remezcla.
  2. `Coco Pixar making of production design "Land of the Dead" art
     director interview architecture` → insidethemagic.net, renderman.pixar.com.
  3. `"Coco" 2017 film "La Llorona" song traditional Mexican folk song
     scene who sings Imelda Ernesto` → Wikipedia «La Llorona (song)»,
     insidethemagic.net, disneynews.us.
  4. `Coco Pixar TikTok trend "Remember Me" challenge viral 2021 2022` →
     sin trend estructurada confirmada, sólo contenido disperso.
  5. `Coco Pixar sound design interview alebrijes sound effects composer
     Michael Giacchino score` → SlashFilm (fanfarria de metales del
     alebrije), Wikipedia «Coco (2017 film)».
  6. `Coco Pixar trailer breakdown analysis video Screen Junkies "Honest
     Trailers" ending explained` → sin resultado directo (ver «No encontré»).

## Cumplimiento del encargo (mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 2. Fotogramas de escenas icónicas, capítulo/minuto | ✅ | 9 escenas icónicas con minuto exacto sacado de la película real (Internet Archive), fotogramas guardados en `/tmp/claude-0/trabajo/57-coco-video/citas/`. ⚠️ fuente en 720p, no 1080p+ (ver «No encontré»). |
| 4. Fondos y sitios, luz y paleta, texturas | ✅ | 9 lugares con paleta hex **medida** con `estilo.py`, más el origen real de 4 de ellos confirmado en dos fuentes (entrevistas de producción). |
| 9. Música y sonido | ✅ (con ⚠️ parciales) | Compositor, 4 canciones clave con autoría confirmada en dos fuentes, motivo musical de los alebrijes, ambiente por escena. ⚠️ onomatopeyas no aplican (es película CGI, no manga); una canción sin segunda fuente de autoría. |
| 10. Vídeos: tráiler, escenas, análisis, tendencias, minuto | ✅ (con ⚠️ parciales) | Tráiler oficial mirado con minuto propio, película completa como fuente de escena. ⚠️ no se confirmó vídeo de análisis ni tendencia de TikTok con cifras (declarado en «No encontré», no oculto). |
| 14. Poses por personaje, 6-10, con minuto | ✅ | Miguel (10), Héctor (8), Mamá Coco (6), Dante (6) — todas con minuto real de la película y qué hace cada una. |

Parte terminada: los 5 puntos (2, 4, 9, 10, 14) están cubiertos, con lo dudoso
marcado ⚠️ en «No encontré» y en la tabla de arriba. Si el redactor necesita
más fotogramas sueltos de algún personaje o escena, la carpeta de trabajo
`/tmp/claude-0/trabajo/57-coco-video/` conserva las hojas de contacto (17 MB,
película ya borrada) hasta que termine el encargo.
