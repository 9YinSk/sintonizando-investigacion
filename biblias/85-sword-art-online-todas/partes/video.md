# Parte VÍDEO · Sword Art Online (todas)

Investigador de vídeo: puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Libreta de datos, no prosa.
Wiki usada: `swordartonline.fandom.com`. Base: `partes/datos-video.md` — casi vacía: `recolectar.py`
no tenía la wiki configurada (falló AniList por el sufijo «(todas)»), AnimeThemes dio error 522
(servidor caído, comprobado varias veces, sigue caído) y la búsqueda automática de Dailymotion no
guardó resultados. Todo se rehizo a mano: búsquedas directas a la API de Dailymotion, descarga con
`fotogramas.py` (que usa yt-dlp) y medición de paleta con `estilo.py`.

**YouTube pide iniciar sesión desde este servidor** (aviso del encargo): los 4 clips imprescindibles
(opening, ending, tráiler, 3+ escenas) se miraron en **Dailymotion**, con `fotogramas.py` sacando
hojas de contacto cada 2-5 s. Limitación real: estas copias de Dailymotion son de baja resolución
(288p-360p, algunas 248p), no 1080p — es lo único accesible con YouTube bloqueado; se anota como ⚠️
en «No encontré». El *plan B* de AnimeThemes (openings/endings oficiales en alta) no funcionó por su
caída de servidor.

Carpeta de trabajo (fuera del repo): `/tmp/claude-0/trabajo/85-sao-video/` — hojas de contacto,
fotogramas sueltos e índices JSON de cada clip mirado (`video.mp4` ya borrado tras sacar las hojas).

## Hallazgos

### Punto 2 — Fotogramas de escenas icónicas, con capítulo y minuto

- **«The Gleam Eyes» (jefe del piso 74, Aincrad)**: pelea Kirito vs. el jefe demonio, activa el
  combo «Starburst Stream» (16 golpes), termina con pantalla «Congratulations!!» y barras de vida de
  Kirito/Asuna en la interfaz. Ocurre al final del **capítulo 8 «The Sword Dance of Black and White»**
  (aparece la puerta del jefe) y se resuelve en el **capítulo 9 «The Blue-Eyed Demon»** (9-1-2012) ·
  confirmado en la ficha de cada episodio de la wiki (`Sword Art Online Episode 08`,
  `Sword Art Online Episode 09`, con «The Gleam Eyes» nombrada en el texto) · clip mirado (recopilación
  de fotogramas reales del anime, canal *Anime Fights*) en
  https://www.dailymotion.com/video/x41mo7i (0:00-2:03) · fotogramas cada 3 s en
  `escena_gleameyes/hoja_01.jpg` · ✅ (wiki + vídeo) · minutos citados abajo (punto 14).
- **Reencuentro Kirito/Asuna tras la batalla** (misma noche, cueva con luz de cristal verde):
  Asuna arrodillada, exhausta; Kirito le sostiene la mano; ella dice «My life belongs to you, Asuna»
  [sic, doblaje inglés dice «to you» de Kirito] y «I'll protect you too»; escena de la misma franja de
  capítulos (8-9) · clip: https://www.dailymotion.com/video/x31uoid (0:00-1:36) · hoja en
  `escena_kiss/hoja_01.jpg` · ✅ (coincide con el lugar y diálogo del arco descrito en la wiki del
  capítulo 9, ⚠️ el minuto exacto dentro del episodio original no se pudo cruzar porque el clip es un
  recorte, no el episodio completo).
- **Sinon y Kirito antes del Bullet of Bullets** (GGO, Sword Art Online II): pasillo hexagonal de
  teletransporte, intercambian «Today, I won't lose» / «Neither will I» (subtítulo visto en italiano:
  «Oggi, non perderò!» / «Neanche io»); el vídeo dice **«Sword Art Online II Episode 7»** en el
  título, pero por el diálogo y el torneo (BoB) coincide con el arco Phantom Bullet ⚠️ (una fuente:
  el rótulo del vídeo; la ficha de la wiki del episodio II-07 «Crimson Memories» no menciona el BoB
  directamente, así que el número exacto de episodio queda sin confirmar en dos fuentes) · clip:
  https://www.dailymotion.com/video/x23wv4c (0:00-0:34) · hoja en `escena_sinon/hoja_01.jpg`.
- **Alicization: Alice y Asuna contra un monstruo abisal** (combate espacial/mecha, «Abyssal
  Horror»): Kirito activa «Release recollection!» con Elucidator, Asuna extiende la mano para curar,
  Alice ataca en picado con espada dorada; **es un vídeo de videojuego/cinemática** (no del anime de
  TV: naves, criatura cósmica), sirve como referencia de las tres poses juntas pero se marca aparte de
  «anime» ⚠️ (no se pudo confirmar el juego exacto: por el estilo 3D coincide con `Alicization Lycoris`
  o un evento de `Variant Showdown`/`Fractured Daydream`, sin confirmación en dos fuentes) · clip:
  https://www.dailymotion.com/video/x7wcnga (0:00-2:24) · hojas en `escena_alice/hoja_01.jpg` y
  `hoja_02.jpg`.
- Todas las hojas se **miraron** (Read de la imagen), no sólo se generaron: base de las poses del
  punto 14 más abajo.

### Punto 4 — Fondos y sitios: luz, paleta (hex) y texturas equivalentes

Paletas sacadas con `herramientas/estilo.py` sobre fotogramas reales (no de memoria); ✅ = medido con
la herramienta sobre el fotograma citado.

- **Sala de piedra de ALfheim Online** (capítulo del arco Mother's Rosario, grupo de las Sleeping
  Knights antes de la misión): pasillo oscuro con antorchas doradas, tonos azul-verdoso muy oscuros ·
  paleta: `#0C0E17` 49% · `#1D2130` 28% · `#3A4460` 10% · `#6977A0` 8% · `#A0A9BF` 5% · sombreado
  degradado/pintado, poca línea marcada · medido en `loc_sala/fotograma_00059.jpg` (0:59 de
  https://www.dailymotion.com/video/x5cgnco) · ✅ · textura real equivalente: piedra de castillo
  gris-azulada con musgo, ambientCG «Rock023» o «Cobblestone» tratada con tinte azul frío.
- **Bosque del Mundo Árbol (ALO)**, luz cálida de atardecer entre hojas: verdes y dorados suaves ·
  paleta: `#D7EDDB` 28% · `#969C7E` 22% · `#B6C09E` 20% · `#72745B` 16% · `#484739` 14% ·
  sombreado degradado/pintado · medido en `loc_alo/fotograma_00040.jpg` (0:40 de
  https://www.dailymotion.com/video/x33t3vs) · ✅ · textura real: hierba/musgo con luz solar
  filtrada, ambientCG «Grass001» + capa de destello (bloom) amarillo pálido.
- **Cielo nocturno de Underworld** (Alicization War of Underworld), nebulosa magenta sobre negro-azul:
  paleta: `#2A2839` 41% · `#7C2556` 21% · `#D8AFA4` 15% · `#667580` 15% · `#E0E4E9` 8% · medido en
  `loc_underworld/fotograma_00042.jpg` (0:42 del tráiler francés
  https://www.dailymotion.com/video/x8hvbsi) · ✅ · para fondo de lámina nocturna: degradado
  púrpura-negro con puntos de luz (partículas), sin textura física necesaria (es cielo).
- **Sala de teletransporte de Gun Gale Online (GGO)**: paredes con panel hexagonal oscuro y una
  compuerta de cristal turquesa · paleta: `#2C252B` 33% · `#413B41` 22% · `#191517` 20% ·
  `#617C80` 19% · `#BAC1BA` 6% · medido en `loc_ggo/fotograma_00004.jpg` (0:04 de
  https://www.dailymotion.com/video/x23wv4c) · ✅ · textura real: panel de metal cepillado oscuro
  (ambientCG «MetalPlates006») + vidrio esmerilado turquesa semitransparente.
- **Sala del jefe «The Gleam Eyes» (Aincrad, piso 74)**: piedra rojiza y azul oscuro con antorchas ·
  paleta: `#20161E` 41% · `#662125` 24% · `#233856` 16% · `#E7CFCD` 14% · `#8D747C` 5% · medido en
  `loc_aincrad/fotograma_00022.jpg` (0:22 de https://www.dailymotion.com/video/x41mo7i) · ✅ ·
  textura real: piedra volcánica oscura (ambientCG «Rock035») con luz de antorcha cálida puntual.
- **Cueva con cristal verde** (reencuentro tras la batalla): verdes muy oscuros y azul petróleo ·
  paleta: `#151A14` 30% · `#212F2B` 28% · `#29494B` 22% · `#526B6C` 15% · `#7EADAF` 5% · medido en
  `loc_cueva/fotograma_00003.jpg` (0:03 de https://www.dailymotion.com/video/x31uoid) · ✅ · textura
  real: roca húmeda verde-negra (ambientCG «Rock030») con luz punteada verde (cristales de
  teletransporte).
- **Pantalla de título del opening «courage» (SAO II, arco Mother's Rosario)**: violeta y negro con
  texto neón cian · paleta: `#010104` 59% · `#180E2A` 15% · `#8F96D7` 10% · `#342F60` 9% ·
  `#614AA0` 8% · medido en `loc_floor27/fotograma_00020.jpg` (0:20 del mismo opening) · ✅ · sirve
  como paleta de fondo para un logo o tarjeta de título con efecto neón morado.

### Punto 9 — Música y sonido

Lista de temas por arco, sacada del wikitext oficial de la wiki (con referencias primarias citadas
por la propia wiki: swordart-online.net, sao-alicization.net, gungale-online.net, Twitter oficial):

- **Aincrad**: apertura «[[crossing field]]» (LiSA) · cierre «Yume Sekai» / «ユメセカイ» (Tomatsu
  Haruka) · ✅ (wiki con referencia a swordart-online.net/aincrad/music).
- **Fairy Dance**: apertura «INNOCENCE» (Aoi Eir) · cierre «Overfly» (Haruna Luna) · ✅.
- **Extra Edition**: cierre «Niji no Oto» 虹の音 (Aoi Eir) · ✅.
- **SAO II — Phantom Bullet** (arco de Sinon/GGO): apertura «IGNITE» (Aoi Eir) · cierre «Startear»
  (Haruna Luna) · ✅ (ref. swordart-online.net/phantom/music).
- **SAO II — Calibur**: apertura «courage» (Tomatsu Haruka) · cierre «No More Time Machine» (LiSA) ·
  ✅ (ref. Dengeki Online / Sony Music).
- **SAO II — Mother's Rosario**: apertura «courage» (episodio 24: «Separate Ways», Tomatsu Haruka) ·
  cierre «Shirushi» シルシ (LiSA) · ✅. El vídeo mirado en `opening/` (Dailymotion x5cgnco) es este
  opening/cierre de este arco: aparecen las siluetas de personajes, el texto «Mother's Rosario» y
  «Sleeping Knights» (nombre del gremio de Yuuki), «Floor 27», relojes/mapa · minutos 0:00-1:53.
- **Ordinal Scale** (película): cierre «Catch the Moment» (LiSA) · ✅ (ref. sao-movie.net/music).
- **Alicization Lycoris (anime), parte 1**: apertura 1 «ADAMAS» (LiSA), cierre 1 «Iris» (Aoi Eir);
  apertura 2 «RESISTER» (ASCA), cierre 2 «forget-me-not» (ReoNa); cierre especial ep. 19 «Niji no
  Kanata ni» (ReoNa) · ✅ (refs. sao-alicization.net, Twitter oficial @sao_anime).
- **War of Underworld (parte 2)**: apertura 3 «Resolution» (Tomatsu Haruka), cierre 3 «unlasting»
  (LiSA); apertura 4 «ANIMA» (ReoNa), cierre 4 «I will...» (Aoi Eir) · ✅ (refs. sao-alicization.net).
- **Gun Gale Online (Alternative)**: apertura «Ryuusei» 流星 (Aoi Eir) · ✅ (ref.
  gungale-online.net/music).
- El clip de `ending/` (Dailymotion x33t3vs, «Sword art online ending 1») coincide en imágenes
  (Kirito/Asuna jóvenes, atardecer, bosque, silueta de dragón) con el cierre del arco Aincrad, «Yume
  Sekai» · ⚠️ (una fuente: coincidencia visual, el vídeo no lleva créditos de canción en pantalla).
- **Ambiente por escena**: la pelea contra The Gleam Eyes usa música orquestal tensa con coro que
  sube de intensidad justo antes de «Starburst Stream» (1:00-1:36 del clip mirado) · ⚠️ (percepción
  propia al escuchar el clip, sin ficha de la pista exacta).
- **Efectos de sonido y frases-sistema reconocibles por cualquier fan** (para onomatopeyas/UI de la
  lámina): el comando de voz **«Link Start»** para conectar el NerveGear y entrar al juego · ✅
  (confirmado en el wikitext de la página «Sword Art Online», sección «Initiation and Character
  Creation», y es la frase más citada de la franquicia en fandom en general). El aviso rojo en el
  cielo virtual, **«System Announcement»**, con el que Kayaba Akihiko explica que la muerte en el
  juego mata en la vida real (episodio 1) · ✅ (wikitext del episodio 1: «there was a system
  announcement that drew everyone's attention»). El cartel dorado **«Congratulations!!»** que aparece
  al vencer a un jefe de piso, visto directamente en el clip de The Gleam Eyes (minuto 1:36-1:44) · ✅
  (visto en vídeo).

### Punto 10 — Vídeos: tráileres, escenas, análisis y tendencias, con minuto

- **Tráiler oficial francés de "Alicization War of Underworld"** (Wakanim, estreno 11 julio 2020):
  blanco y negro con destellos de color, texto «SWORD ART ONLINE — ALICIZATION War of Underworld»,
  termina con «DÈS LE 11 JUILLET EN EXCLUSIVITÉ SUR WAKANIM» · https://www.dailymotion.com/video/x8hvbsi
  (0:00-2:28) · minutos clave: 0:45-0:55 (Asuna «Non! Tout mais pas ça!», mano en la boca, shock),
  1:15 (Kirito lanza un tajo de luz azul con Elucidator), 1:30-1:55 (espada blanca clavada en el
  suelo rojo, manos entrelazadas de Kirito y Alice: «Je t'en prie Kirito... mon cœur, ma vie») · ✅
  (vídeo mirado con fotogramas cada 5 s, hoja en `trailer/hoja_01.jpg`).
- **Tendencia en TikTok**: el opening «Crossing Field» (LiSA, apertura del arco Aincrad) sigue
  usándose en edits nostálgicos de anime en 2024-2025, con las etiquetas #crossingfield
  #swordartonline #sao; ejemplo con crédito y enlace directo:
  https://www.tiktok.com/@soundnime/video/7372160452756802821 («LiSA - Crossing Field (OP 1 Sword
  Art Online)») · ✅ (búsqueda web, resultado con URL de vídeo real, no sólo hashtag).
- **Vídeos de análisis en YouTube** (sólo como referencia de enlace — YouTube pide iniciar sesión
  desde este servidor y no se pudieron mirar con fotogramas.py): «Sword Art Online is the WORST Anime
  of All Time» (vídeo-ensayo crítico centrado en el arco Phantom Bullet, título tal cual aparece en
  YouTube) y el canal completo «Sword Art Online Abridged» (parodia/abridged de gran tamaño de
  fandom en inglés) · ⚠️ (enlace de búsqueda web, no visto en vídeo por el bloqueo de YouTube en este
  servidor; el jefe puede confirmarlo con `yt-dlp` fuera de este contenedor si hace falta el minuto
  exacto).
- **Interfaz visible en un vídeo real**: al final de la pelea contra The Gleam Eyes (minuto 1:36-1:57
  del clip https://www.dailymotion.com/video/x41mo7i) se ve el HUD clásico de SAO: barra de vida verde
  de «Asuna» y roja/vacía de «Kirito» apiladas en la esquina, con un botón «+» al lado — el marcador de
  salud que después copian casi todos los juegos y láminas «gamer» de la franquicia · ✅ (visto en
  vídeo).

### Punto 14 — Poses analizadas por personaje (capítulo/minuto + qué hace + para qué sirve)

**Kirito** (clips: `escena_gleameyes` = https://www.dailymotion.com/video/x41mo7i,
`escena_kiss` = https://www.dailymotion.com/video/x31uoid):
- 0:09-0:15 (gleameyes) — salta hacia atrás esquivando el zarpazo del jefe, abrigo negro ondeando,
  mirada fija en el monstruo · pose de **combate/esquivar** · ✅.
- 0:36 (gleameyes) «Starburst Stream!» — cuerpo inclinado en pleno combo de 16 golpes con Elucidator,
  estela azul · pose de **ataque especial** · ✅.
- 1:00 (gleameyes) «Even faster!» — primer plano, ojos entrecerrados, dientes apretados, ceño
  fruncido · pose de **regañarse a sí mismo / exigirse más** · ✅.
- 1:30-1:33 (gleameyes) — de espaldas, hombros caídos, respira hondo mirando el resultado de la
  pelea · pose de **pensar/reflexionar** · ✅.
- 1:39-1:44 (gleameyes) — silueta erguida con la espada en alto bajo el cartel «Congratulations!!» ·
  pose de **celebrar** · ✅.
- 0:48 (kiss) — de perfil, muy cerca de Asuna, mano izquierda alzada hacia su rostro · pose de
  **animar/consolar** · ✅.
- 1:21-1:24 (kiss) «I'll protect you too» — de espaldas, Elucidator apoyada contra la roca, hombro
  con hombro junto a Asuna · pose de **prometer/explicar** · ✅.

**Asuna** (mismos dos clips):
- 0:12 (gleameyes) — ojos muy abiertos, boca entreabierta, cuerpo en tensión al ver el peligro ·
  pose de **sorpresa/miedo** · ✅.
- 0:09 (kiss) — arrodillada en el suelo de piedra, cabeza gacha, pelo cayendo sobre la cara · pose de
  **vulnerabilidad/agotamiento** · ✅.
- 0:39-0:42 (kiss) — primer plano, ojos entrecerrados, mejillas sonrojadas, cabeza inclinada hacia
  Kirito · pose de **cariño/confianza** · ✅.
- 1:03-1:06 (kiss) «My life belongs to you» — manos entrelazadas contra el pecho, mirada hacia
  arriba · pose de **entrega/promesa** · ✅.
- 0:45-0:50 (trailer, https://www.dailymotion.com/video/x8hvbsi) «Non! Tout mais pas ça!» — manos
  cubriendo la boca, ojos muy abiertos, lágrimas asomando · pose de **negación/dolor** · ✅.
- 1:03-1:09 (escena_alice, https://www.dailymotion.com/video/x7wcnga) — de pie, brazo extendido con
  la palma abierta, luz azul saliendo de la mano · pose de **ofrecer ayuda/curar** · ⚠️ (clip de
  videojuego, no del anime de TV).

**Sinon** (clip `escena_sinon` = https://www.dailymotion.com/video/x23wv4c, arco GGO):
- 0:04 — camina de espaldas a cámara por el pasillo hexagonal, cuerpo erguido, bufanda blanca
  ondeando · pose de **entrar en escena/presentarse** · ✅.
- 0:16 — primer plano, mirada fija y seria, cejas rectas · pose de **decidirse/concentrarse** · ✅.
- 0:24 «Today, I won't lose» (subtítulo visto en italiano «Oggi, non perderò!») — mirada de reojo,
  mandíbula tensa · pose de **anunciar/desafiar** · ✅.
- 0:32-0:34 — de pie, sola, bajo dos focos de luz cenital que caen en la sala hexagonal antes de
  entrar al torneo · pose de **esperar/prepararse mentalmente** · ✅.

**Alice** (clip `escena_alice` = https://www.dailymotion.com/video/x7wcnga; ⚠️ es vídeo/cinemática de
videojuego, no del anime de TV — se anota igual porque el encargo pide explícitamente poses de Alice
y es lo único con ella en movimiento que se pudo mirar sin YouTube):
- 1:30-1:33 — sentada en el asiento de mando de una nave, manos cruzadas sobre el pecho, mirada
  seria al frente · pose de **mando/observar** · ⚠️.
- 1:39 «Il faut l'exterminer!» (hay que exterminarlo, subtítulo francés) — de pie, brazo en alto
  señalando al frente · pose de **ordenar/animar a la tropa** · ⚠️.
- 1:42-1:45 «Je connais ce Chevalier!» (conozco a este caballero) — de perfil, ojos muy abiertos,
  boca abierta · pose de **sorpresa/reconocer** · ⚠️.
- 1:48-1:51 — de pie, espada dorada en alto sobre la cabeza, capa ondeando tras ella · pose de
  **combate/celebrar el golpe** · ⚠️.
- 2:03-2:09 — lanzada en picado con la espada por delante y una estela dorada detrás · pose de
  **atacar/lanzarse** · ⚠️.
- 1:30-1:55 (trailer, https://www.dailymotion.com/video/x8hvbsi, ⚠️ personaje sin confirmar del
  todo por el plano cerrado, pero encaja con la escena de Alice entregando su fluctlight para revivir
  a Kirito descrita en la wiki del arco) — manos entrelazadas con las de Kirito, cabeza inclinada,
  súplica «mon cœur, ma vie» · pose de **entregarse/rogar**.

## Lo mejor para la lámina

1. El HUD real de SAO (barras de vida verde/roja apiladas + botón «+», minuto 1:36-1:57 del clip
   `escena_gleameyes`) es el icono más reconocible de interfaz de videojuego de toda la franquicia:
   perfecto para un canal de edición/pruebas técnicas.
2. La paleta violeta-negra con texto neón cian del opening de Mother's Rosario
   (`#010104`/`#8F96D7`/`#614AA0`) da un fondo de «pantalla de título» listo para un logo de canal.
3. La pose de Kirito «Even faster!» (1:00, gleameyes) — primer plano de determinación — sirve para
   cuadros de diálogo de auto-exigencia («no te rindas», útil en un canal de práctica vocal o edición).
4. La sala hexagonal de GGO con foco cenital (Sinon, 0:32-0:34) es un fondo limpio y futurista para
   texto de reglas o anuncios.
5. «Congratulations!!» (cartel dorado tras vencer al jefe) es un cuadro de diálogo de sistema listo
   para anunciar logros o subida de nivel en un canal de la comunidad.

## No encontré

- **AnimeThemes** (openings/endings oficiales en `.webm`, plan A de `datos-video.md`): la API
  (`api.animethemes.moe`) dio **error 522** (servidor caído) en todos los intentos, repetido varias
  veces en la misma sesión — no es bloqueo del proxy, es la web la que no responde. ⚠️.
- **Clips en 1080p+** de las mismas escenas: con YouTube bloqueado desde este servidor, las únicas
  copias que se encontraron en Dailymotion son de 248p-360p (comprobado con `ffprobe`). No hay forma
  de subir la resolución sin YouTube; se anota como límite real, no como «no busqué». ⚠️.
- **Minuto exacto dentro del episodio original** de la escena de reencuentro Kirito/Asuna y del
  clip de Sinon: los vídeos de Dailymotion son recortes de fans (re-subidos), no el episodio
  completo con su numeración de minuto oficial; se dio el minuto **dentro del clip mirado**, con su
  enlace, tal como pide el punto 2, pero no se pudo cruzar con el minuto exacto del episodio emitido
  en TV. ⚠️.
- **Vídeos de análisis y la tendencia de TikTok mirados fotograma a fotograma**: sólo se pudo dar el
  enlace (búsqueda web), no mirarlos con `fotogramas.py`, porque son de YouTube/TikTok y YouTube
  pide iniciar sesión desde este servidor; TikTok no lo lee `yt-dlp` de forma fiable en este
  contenedor. Esto es un extra (el punto 10 ya queda cubierto con el tráiler mirado en vídeo real),
  no una falta del mínimo obligatorio. ⚠️.
- **Nombre de la pista exacta** que suena en la pelea contra The Gleam Eyes: se describe el ambiente
  (orquestal, coro, sube de intensidad) pero no se identificó el título de la pista del OST porque el
  clip no lleva créditos musicales en pantalla y no se localizó una lista de pistas por escena. ⚠️.

## Bitácora de búsqueda

- Español: ninguna (todas las fuentes de vídeo son en inglés/japonés/francés/italiano según el
  clip encontrado).
- Inglés: `Sword Art Online opening official` / `trailer official` / `ending official` / `Kirito
  Asuna scene` / `Sinon Kirito Bullet of Bullets scene` / `Alice awakens memory scene` / `Kirito vs
  Heathcliff fight scene` (API de Dailymotion, `api.dailymotion.com/videos`).
- Inglés (wiki): `api.php?action=query&list=search` en swordartonline.fandom.com con
  `Sleeping Knights ending theme`, `list of theme songs opening ending`, `The Gleam Eyes episode
  floor 74 boss`, `Bullet of Bullets episode Sinon meets Kirito`, `Link Start catchphrase login
  command`, `"Link Start"`; y `action=parse&prop=wikitext` sobre `Sword Art Online Anime Main Page`,
  `Sword Art Online Episode 08`, `Sword Art Online Episode 09`, `Sword Art Online II Episode 07`,
  `Sword Art Online Episode 01`, `Sword Art Online` (página general).
- Inglés (web): `Sword Art Online TikTok trend edit viral opening "Crossing Field" 2024 2025`,
  `Sword Art Online video essay analysis YouTube "why" 2023 2024`, `"Sword Art Online" video essay
  youtube.com/watch analysis Aincrad` (WebSearch, 3 búsquedas de las ~50 disponibles).
- Japonés/coreano/chino: no hizo falta para este punto (los vídeos y la wiki en inglés ya daban
  minuto, capítulo y crédito de canción con fuente oficial citada por la propia wiki).
- Fuentes consultadas en total en esta parte: 8 clips de Dailymotion, 7 páginas/búsquedas de la wiki
  de Fandom (api.php), 3 búsquedas web (TikTok + 2 de YouTube), 1 comprobación técnica con `ffprobe`
  (resolución real de los clips) y 8 mediciones de paleta con `estilo.py` sobre fotogramas propios.
- AnimeThemes (`api.animethemes.moe`): 522 repetido, descartado como fuente para esta parte.

## Cumplimiento del encargo (mi parte: puntos 2, 4, 9, 10, 14)

| Punto | Estado | Por qué |
|---|---|---|
| 2. Fotogramas de escenas icónicas, capítulo y minuto | ✅ | 4 clips mirados fotograma a fotograma (Gleam Eyes ep. 8-9, reencuentro Kirito/Asuna, Sinon/GGO, Alice/Asuna en cinemática), cada uno con minuto y enlace. ⚠️ resolución real 248-360p (Dailymotion, no 1080p) por el bloqueo de YouTube. |
| 4. Fondos y sitios: luz, paleta, texturas | ✅ | 7 paletas medidas con `estilo.py` sobre fotogramas reales, con textura CC0 equivalente sugerida para cada una. |
| 9. Música y sonido | ✅ | Lista completa de aperturas/cierres por arco (Aincrad a War of Underworld + AGGO) con fuente oficial citada por la wiki; 3 efectos/frases de sistema reconocibles («Link Start», anuncio del sistema, «Congratulations!!»). ⚠️ no se identificó la pista exacta de la pelea contra Gleam Eyes. |
| 10. Vídeos: tráileres, escenas, análisis, tendencias, con minuto | ✅ | Tráiler oficial francés mirado con minutos exactos; tendencia de TikTok con enlace de vídeo real; vídeos de análisis enlazados (no mirados, YouTube bloqueado — esto es el extra, no lo obligatorio). |
| 14. Poses analizadas por personaje, minuto/capítulo, para qué sirven | ✅ | Kirito y Asuna con 6-7 poses cada uno de anime real (2 clips), Sinon con 4 (GGO), Alice con 6 pero marcadas ⚠️ por venir de una cinemática de videojuego, no del anime de TV — es lo único con ella en movimiento accesible sin YouTube. |
