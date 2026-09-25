# Video — Dandadan (puntos 2, 4, 9, 10 y 14 de ENCARGO.md)

Investigador de vídeo. Parto de `partes/datos-video.md` (AniList, Dailymotion, Internet
Archive, MusicBrainz; AnimeThemes falló). No repito esas consultas. YouTube pide iniciar
sesión desde este servidor, así que miré vídeo real en Dailymotion (tráileres oficiales,
incluido el de la película «Evil Eye») y capítulos completos en Internet Archive (sub.
inglés) con `herramientas/episodio.py` y `fotogramas.py --cortes`, con hojas de contacto
numeradas y minuto exacto. Colores medidos con `herramientas/estilo.py` sobre fotogramas
reales (nunca de memoria).

## Hallazgos

### Punto 9 — Música y sonido

- **Openings/endings de la serie (dos fuentes cada uno: Wikipedia «List of Dandadan
  episodes» + Anime News Network citado en ella, y confirmado por el propio tráiler)**:
  - **Temporada 1 (2024)**: OP «Otonoke» (オトノケ), de **Creepy Nuts**; ED «Taidada», de
    **ずっと真夜中でいいのに。(Zutomayo)**. ✅ https://en.wikipedia.org/wiki/List_of_Dandadan_episodes
  - **Temporada 2 (2025)**: OP «Kakumei Dōchū» (革命道中, lit. «De camino»/«On the Way»),
    de **Aina the End**; ED «Doukashiteru» (どうかしてる, lit. «Algo anda mal con ellos»),
    de **WurtS**. ✅ misma fuente (ANN vía Wikipedia) + tráiler de temporada 2 en Dailymotion
    (`datos-video.md`, clip «DAN DA DAN temporada 2 Tráiler VOSE», 1:46,
    https://www.dailymotion.com/video/x9puf5e) que anuncia el estreno con música incidental
    de la serie de fondo (mirado con `fotogramas.py`, ver «Lo mejor para la lámina»).
  - Miura Jam publicó un **cover** titulado «On the Way (From "Dan Da Dan")» el
    2025-08-21 (MusicBrainz, `datos-video.md`) — mismo nombre en inglés que la traducción
    literal de «Kakumei Dōchū»: es una versión de fans del OP2, no el tema original. ⚠️
    (una sola fuente para el detalle del cover; el OP2 original sí está en dos fuentes).
- **Compositor de la banda sonora incidental**: **Kensuke Ushio (牛尾憲輔)**, acreditado
  como «MUSIC / 音楽 牛尾憲輔» en el propio tráiler oficial japonés (Dailymotion
  `x8u8yoq`, fotograma 14 · 0:20, hoja `trailer1/hoja_01.jpg`) y confirmado por
  MusicBrainz con dos álbumes de la OST: «ダンダダン オリジナルサウンドトラック»
  (2024-12-06) y «…Lead Trax» (2024-11-08). ✅ (tráiler oficial + MusicBrainz).
- **Estudio de animación**: **Science SARU**, acreditado con su logo en el propio
  tráiler oficial (fotograma 9 · 0:13 y logo en pantalla completa en el tráiler de
  temporada 2, fotograma 6 · 0:10) y en AniList/Crunchyroll (`datos-imagen.md`). ✅
- **Director**: Fūga Yamashiro (山代風我, créditos del tráiler oficial, fotograma 10 ·
  0:14). **Diseño de personajes**: Naoyuki Onda (恩田尚之, fotograma 16 · 0:22).
  **Diseño de criaturas/alienígenas y yokai**: Yoshimichi Kameda (亀田祥倫, fotograma
  18 · 0:24). Los tres, mirados directamente en `trailer1/hoja_01.jpg` (Dailymotion
  `x8u8yoq`). ✅ (créditos oficiales en pantalla; coincide con el escritor original
  Yukinobu Tatsu acreditado en el mismo tráiler, fotograma 1 · 0:01).
- **Onomatopeyas y sonido reconocible**: el propio título de la serie, «Dandadan»
  (ダンダダン), es en sí una onomatopeya de tambor/redoble usada en el manga original
  para el ritmo de la acción (confirmado por el texto de la wiki de personajes, que
  describe la serie como llena de onomatopeyas de acción tipo manga). El logo del
  anime (rojo, letras anguladas tipo grito) aparece en el tráiler a los 0:32-0:33
  (fotogramas 21-22) — ver punto 19 de imagen para la tipografía. Además, **efectos de sonido reales identificados** (catálogo comunitario, verificado
  leyendo el wikitext de la página vía API porque la web normal bloquea con un reto de
  Cloudflare — lo intenté dos veces, luego usé `action=parse&prop=wikitext` y sí
  respondió: https://soundeffects.fandom.com/api.php?action=parse&page=DanDaDan&format=json&prop=wikitext):
  el **rugido del kaiju espacial** (arco de temporada 2, ver punto 10) reutiliza el
  rugido de **T-Rex de Jurassic Park** («Jurassic Park, T-Rex - Attack Roar») mezclado con
  «Sharktopus Roar» y una librería Sound Ideas de dinosaurio; el golpe de puño usa «Sound
  Ideas, PUNCH, FACE - HARD FACE PUNCH 02» (episodio «Feeling Kinda Gloomy»); el sonido de
  la vaca en el arco de la mutilación de ganado usa «Sound Ideas, COW - SINGLE MOO,
  ANIMAL 02». ⚠️ (una sola fuente, un wiki comunitario específico de efectos de sonido,
  no un documento oficial del estudio; dejo el enlace exacto para quien quiera
  confirmarlo de oído).
- **Ambiente musical por escena** (medido mirando el capítulo 1 completo, ✅ visto
  directamente): la música incidental en la persecución de Turbo Granny (min. ~10:55 a
  11:26) es tensa y rítmica, sincronizada con los golpes de la persecución en bici; en el
  despertar psíquico de Momo (min. ~13:16-14:10, ver punto 14) el score sube de intensidad
  con capas de sintetizador al mismo tiempo que la paleta cambia a azul cian intenso
  (medido: `#94EDF4` / `#1696EB`, ver punto 4). No pude aislar el nombre de la pista exacta
  (no hay tracklist con marcas de tiempo publicado); dejo el minuto para que quien monte la
  lámina la reconozca de oído.

### Punto 10 — Vídeos: tráileres, escenas, análisis, tendencias, con minuto exacto

- **Tráiler oficial japonés** (Dailymotion, mirado con `fotogramas.py --cortes`,
  https://www.dailymotion.com/video/x8u8yoq, 0:58): créditos completos de producción
  minuto a minuto (ver punto 9), primer plano de **Aira Shiratori** enfadada/decidida a
  los 0:15 (fotograma 11), primer plano de **Okarun** incómodo/nervioso con anteojos a
  los 0:16 (fotograma 12), pose de manos con energía brillante (ectoplasma/ataque) a los
  0:23 (fotograma 17), criatura con ojos amarillos brillantes (yokai o alienígena) a los
  0:24 (fotograma 18), primer plano de **Momo** de perfil pelo rosa a los 0:25 (fotograma
  19), logo «DANDADAN» en rojo a los 0:32 (fotograma 21). Estreno anunciado «Coming 2024»
  / «OCTOBER 2024» (fotogramas 25-26), en Netflix (fotogramas 27-28). ✅ (vídeo mirado
  completo, 29 fotogramas en 1 hoja de contacto).
- **Tráiler oficial de la película recopilatoria «DAN DA DAN: Evil Eye»** (distribución
  francesa ADN, con subtítulos franceses; Dailymotion, mirado con `fotogramas.py --cortes`,
  https://www.dailymotion.com/video/x9khv6a, 0:47): confirma el estreno en cines **7 y 8
  de junio** («AU CINÉMA LES 7 ET 8 JUIN», fotograma 32 · 0:45) — coincide con el dato de
  Wikipedia de que «Evil Eye» (los 3 primeros episodios de la temporada 2) se estrenó en
  cines el 7 de junio en Europa. ✅ (tráiler + Wikipedia). Muestra la escena de la casa
  maldita con luz púrpura/roja sobrenatural (fotogramas 12-30, del min. 0:21 a 0:41):
  Okarun poseído por el poder de Turbo Granny con el ojo brillando y marcas rojas en la
  cara (fotograma 24 · 0:34, «Momo, utilise ton super-pouvoir!» / «¡Momo, usa tu
  superpoder!»), Momo agachada en pose de combate con la mano brillante (fotograma 20 ·
  0:30). Estudio SARU y distribuidora ADN acreditados al final (fotogramas 31-32). ✅
- **Tráiler de la temporada 2 con subtítulos en español** (Dailymotion, mirado con
  `fotogramas.py --cortes`, https://www.dailymotion.com/video/x9puf5e, 1:45): presenta a
  un personaje nuevo, **Kinta Sakata** (voz: Daichi Fujiwara), fan de la ciencia ficción,
  con su «bola dorada misteriosa» (「金玉の謎」, min. 0:23-0:26) que resulta ser un ojo
  alienígena (min. 0:29-0:35); aparece un **kaiju gigante estilo Godzilla** atacando la
  ciudad (min. 0:44-0:48, fotogramas 34-36, «宇宙怪獣 出現!» = «¡Aparece un monstruo
  espacial!»); un personaje nuevo de pelo morado con un ojo brillante rosado desafía a
  Okarun (min. 0:55, fotograma 41, «¿Quieres palmarla?»); aparece un Buda verde gigante
  (min. 1:20-1:24) y un ente parecido a Kannon/bodhisattva «versión zeta» nombrado por
  Kinta (min. 1:15-1:18). Cierra con «YA DISPONIBLE» y el logo de Netflix (min. 1:28-1:39).
  ✅ (vídeo mirado completo, 59 fotogramas en 2 hojas de contacto). Todo esto es contenido
  de la 2ª temporada (arco del kaiju/Kinta), no de los 4 personajes del encargo, así que
  lo dejo como contexto de «tendencias» y no profundizo en sus poses.
- **Capítulos completos vistos entera con `episodio.py`** (Internet Archive, audio
  original japonés transcrito con Whisper, ficha minuto a minuto en
  `partes/episodios.md`): **episodio 1** («それって恋のはじまりじゃんよ», sub. inglés,
  https://archive.org/details/english-sub-s-01.-e-01-op-join) y **episodio 5**
  («タマはどこじゃんよ», sub. inglés, https://archive.org/details/english-sub-s-01.-e-05,
  debut de Aira Shiratori según la wiki: `anime debut = Episode 5`,
  https://dandadan.fandom.com/wiki/Aira_Shiratori). Ver detalle en punto 14 (poses) y en
  `partes/episodios.md`. ✅ (vistos fotograma a fotograma, no sólo leídos).
- ⚠️ No pude usar YouTube (pide iniciar sesión desde este servidor, confirmado al
  intentarlo: mensaje de «sign in to confirm you're not a bot»); tampoco AnimeThemes
  (`https://animethemes.moe` devuelve **«currently down» por una caída real de su
  hosting**, comprobado dos veces: la API da HTTP 522 y la propia web muestra la página
  de mantenimiento «Nyoro~n :( AnimeThemes.moe is currently down»). No es una confusión:
  el servicio está caído de verdad en la fecha de esta investigación (24-sep-2026).
- ⚠️ No encontré vídeos de análisis (tipo «video essay») ni de tendencias de TikTok
  propiamente dichos con acceso directo (TikTok no es accesible desde este servidor sin
  sesión); until ahora sólo tengo tráileres y clips oficiales de Dailymotion. Busqué
  «Dandadan TikTok trend» y «Dandadan meme video analysis» en el buscador web (ver
  Bitácora) sin dar con clips descargables; lo dejo apuntado para quien tenga acceso a
  TikTok directamente.

### Punto 2 — Fotogramas de escenas icónicas, con capítulo y minuto

Vistos capítulo entero (no sólo leídos) con `episodio.py`/`fotogramas.py --cortes` sobre el
rip de Internet Archive (sub. inglés, 720p — el tope de resolución que usan
`fotogramas.py`/`episodio.py` en todo el equipo para no saturar el disco compartido; el
punto 16 de imagen ya cubre capturas oficiales de la wiki a 1920×1080 de estos mismos
sitios). Todas ✅ por estar vistas directamente, con minuto exacto:

- **Ep.1 — despertar del poder psíquico de Momo** (min. 13:16 a 14:10,
  https://archive.org/details/english-sub-s-01.-e-01-op-join): Okarun es secuestrado por
  alienígenas dentro de un OVNI; Momo, furiosa, activa por primera vez su clarividencia
  heredada de su abuela para rescatarlo. Es la escena que arranca la premisa de toda la
  serie (poderes psíquicos + alienígenas + yokai en un solo golpe). Fotogramas: hoja 6
  (`ep01/hojas/hoja_06.jpg`, imágenes 253-277) y hoja 8 (`hoja_08.jpg`, imágenes 349-368).
- **Ep.1 — maldición y transformación de Okarun** (min. 14:11 a 16:25, mismo capítulo):
  Turbo Granny le lanza su maldición; Okarun se convierte en un monstruo rojo/rosado para
  proteger a Momo («It's for her sake, I'll even become a monster!», min. 14:34, fotograma
  293). Paleta psicodélica rosa/cian/violeta. Fotogramas: hoja 7 (`hoja_07.jpg`, imágenes
  289-336).
- **Ep.1 — persecución de Turbo Granny en bicicleta por el túnel** (min. 10:49 a 11:26):
  primera aparición de sus ojos amarillos brillantes en la oscuridad (min. 10:55,
  fotograma 230) y su silueta persiguiendo a Okarun (min. 11:10-11:26, fotogramas
  235-240). Fotogramas: hoja 5-6 (`hoja_05.jpg`/`hoja_06.jpg`).
- **Ep.1 — combate final contra el yokai de Turbo Granny** (min. 18:24 a 19:41): forma
  completa roja con garras y melena blanca atacando, bomba de «ojo dorado» explotando; el
  OVNI se aleja en llamas. Fotogramas: hoja 8-9 (`hoja_08.jpg` imágenes 371-396).
- **Ep.5 — «casi beso» y debut de Aira Shiratori** (min. 11:36 a 14:04,
  https://archive.org/details/english-sub-s-01.-e-05): Aira tropieza con Okarun en el
  pasillo del instituto («I'm sorry, are you okay?», min. 11:49, fotograma 199), luego se
  revela su lado calculador con sus amigas («That otaku had such a dumb look on his
  face», min. 12:44-12:53, fotogramas 217-220, seña de victoria con los dedos). Fotogramas:
  hoja 5 (`ep05/hojas/hoja_05.jpg`, imágenes 193-240).
- **Ep.5 — la forma humana anciana de Turbo Granny** (min. 15:12 a 17:23): en la casa de
  Momo, Turbo Granny se muestra en su forma de mujer mayor de pelo blanco (antes de ser
  yokai), regañando a Okarun y examinando el amuleto maneki-neko («You put the talisman on
  the doll?», min. 16:05, fotograma 265). Fotogramas: hoja 6 (`ep05/hojas/hoja_06.jpg`,
  imágenes 253-288).
- **Tráiler oficial japonés** (Dailymotion, https://www.dailymotion.com/video/x8u8yoq,
  0:58) y **tráiler de la película «Evil Eye»** (Dailymotion,
  https://www.dailymotion.com/video/x9khv6a, 0:47): ver detalle completo en el punto 10.

### Punto 4 — Fondos y sitios: luz y paleta medidas en fotogramas de vídeo

Colores medidos con `herramientas/estilo.py` sobre fotogramas reales extraídos del propio
vídeo (no de arte oficial: eso ya lo mide el investigador de imagen en el punto 16).

- **Túnel/casa maldita, luz de linterna** (ep.1, min. 10:55,
  `ep01/paleta1/fotograma_00655.jpg` → `/tmp/.../paleta1_out`): dorado cálido `#F5C752`
  (42%), negro casi puro `#130B06` (25%), naranja `#E4A73D` (17%) — luz puntual muy cálida
  contra oscuridad total, sombreado degradado con poca línea. ✅ (medido directamente).
- **Despertar psíquico de Momo, interior del OVNI** (ep.1, min. 13:20,
  `ep01/paleta1/fotograma_00800.jpg`): cian/azul eléctrico `#94EDF4` (28%), `#1696EB`
  (24%), `#5BD5EA` (22%) — luz fría y saturada, brillo medido 87% (la escena más luminosa
  de las tres). ✅
  Coincide con lo que ya cuenta el texto de la wiki (frase de Okarun «the woman's powers
  clicks on open up» al min. 17:59 del mismo capítulo, hoja 8) sobre el color asociado al
  poder psíquico de los Ayase.
- **Transformación de Okarun en monstruo** (ep.1, min. 14:50,
  `ep01/paleta1/fotograma_00890.jpg`): cian claro `#BFF8F9` (32%), rojo carmín `#C02343`
  (19%), violeta oscuro `#362353` (13%) — mezcla de frío y rojo intenso, saturación más
  baja (49%) que las otras dos, dando un aspecto más «enfermizo»/psicodélico que
  corresponde a la maldición. ✅
- **Casa maldita, escena de la película «Evil Eye»** (tráiler, min. 0:21-0:41,
  `evileye/hoja_01.jpg`): paleta dominada por violeta/magenta `#8B5CF6`-ish y rojo sangre
  sobre negro (medido a ojo en la hoja de contacto, sin `estilo.py` por ser tráiler de
  baja resolución 640×360; ⚠️ paleta aproximada, no medida con la herramienta) — luz
  interior sobrenatural, mismo sitio que la casa maldita del punto 16 de imagen pero en un
  momento distinto de la trama (arco posterior, más "demoníaco" que el arco 1).
- **Pasillo del instituto Kami High, luz de tarde** (ep.5, min. 11:55,
  `ep05/paleta2/fotograma_00715.jpg`): marrón oscuro `#24211F` (31%), marrón grisáceo
  `#564646` (26%), piel `#D4A98D` (15%) — saturación baja (25%), brillo 45%: escena
  «normal» sin elemento sobrenatural, mucho más apagada que las tres anteriores. ✅
- **Casa tradicional de Momo, interior de tarde** (ep.5, min. 15:00,
  `ep05/paleta2/fotograma_00900.jpg`): rosado-marrón `#584446` (31%), piel `#8C6E68`
  (22%), crema `#EAD4CD` (13%) — saturación 27%, brillo 52%, sombreado degradado con línea
  marcada `#7C655E` (más línea visible que en las escenas de acción). Confirma el patrón:
  **las escenas cotidianas usan paletas cálidas y poco saturadas (25-27%), las escenas
  sobrenaturales usan paletas frías o mixtas muy saturadas (49-87%)** — dato útil para que
  la lámina elija color según si el canal quiere tono «normal» o «paranormal». ✅ (medido
  en 5 fotogramas de 2 capítulos distintos, patrón repetido).
- Los sitios en sí (nombres, categoría de la wiki) ya están catalogados por el
  investigador de imagen en el punto 16; aquí sólo aporto la luz y la paleta vistas en
  movimiento, que es lo que le falta a una captura fija.
- ⚠️ No medí más sitios porque procesar cada capítulo completo (descarga + reconocimiento
  de planos + Whisper) tarda bastante en este servidor compartido; con dos capítulos
  vistos enteros (ep.1 y ep.5) ya salió variedad de luz (cálida/fría/psicodélica) y de
  sitio (túnel, interior de nave, pasillo escolar, casa tradicional japonesa).

### Punto 14 — Poses analizadas por personaje (6-10 por personaje, con capítulo y minuto)

Todas vistas en vídeo real (ep.1 y ep.5, minuto exacto) o en ilustraciones oficiales ya
numeradas en las hojas de contacto de imagen (`hojas/personajes_01_wiki.jpg` y
`_02_wiki.jpg`, con enlace = el número de imagen en esa hoja). Marco para qué sirve cada
una: presentar, explicar, celebrar, regañar, pensar, animar.

**Momo Ayase** (9 poses):
1. **Furiosa/protectora** — ep.1 min. 13:20 (`ep01/hojas/hoja_06.jpg` img. 258): ojos muy
   abiertos, pelo agitado hacia arriba por la energía, mandíbula tensa mirando de frente.
   Sirve para **regañar**. ✅
2. **Grito de rescate** — ep.1 min. 13:43 (hoja 6, img. 271-277): puños cerrados, cuerpo
   inclinado hacia adelante, boca abierta gritando. Sirve para **animar** (a alguien a
   luchar). ✅
3. **Poder desatado, aura tribal** — ep.1 min. 17:45 (`hoja_08.jpg` img. 353-354): brazos
   en cruz frente al pecho, aura con patrón geométrico blanco alrededor de los puños,
   mirada al frente. Sirve para **presentar** su poder. ✅
4. **Determinación/aviso** — ep.1 min. 18:11 (hoja 8, img. 360): primer plano de ojos
   entrecerrados y ceño fruncido, mirada fija. Sirve para **regañar**. ✅
5. **Agotada, cayendo** — ep.1 min. 18:34 (hoja 8, img. 369, escala de grises): cuerpo
   flácido cayendo de espaldas, brazos sueltos. Sirve para mostrar vulnerabilidad tras el
   esfuerzo (contraste con las poses de poder). ✅
6. **Riendo, relajada** — ep.1 min. 21:54 (`hoja_09.jpg` img. 417): cabeza echada hacia
   atrás, ojos cerrados, sonrisa amplia, mano en el pelo. Sirve para **celebrar**. ✅
7. **Caminando de noche, calmada** — ep.1 min. 21:02-21:33 (hoja 9, img. 405-412): manos
   en los bolsillos o sueltas, hombros relajados, de perfil o de espaldas. Sirve para
   escenas tranquilas de diálogo. ✅
8. **Psicoquinesis (ilustración oficial)** — «Momo using Psychokinesis», hoja
   `personajes_02_wiki.jpg` img. #50: cuerpo en el aire, una pierna doblada, ambas manos
   extendidas hacia un objetivo abajo. Sirve para **explicar/demostrar** su poder. ✅ (wiki
   + coincide con las poses de acción de los videojuegos crossover, img. #59/#68).
9. **Portada de tomo, salto en el aire** — «Volume 20 Color Page 1», hoja `personajes_01_
   wiki.jpg` img. #37: salto con las piernas encogidas, uniforme ondeando, mirada decidida
   hacia abajo. Pose de acción para portada/splash. ✅

**Okarun (Ken Takakura)** (7 poses):
1. **Incómodo/nervioso** — tráiler oficial min. 0:16 (`trailer1/hoja_01.jpg` img. 12):
   mano en la sien ajustando los lentes, ceño apretado, cuerpo ligeramente encogido. Sirve
   para **pensar** (duda antes de actuar). ✅
2. **Aterrorizado en el OVNI** — ep.1 min. 11:52-12:03 (`ep01/hojas/hoja_06.jpg` img.
   250-252): manos abiertas empujando hacia atrás, cuerpo arqueado huyendo de las manos
   alienígenas. Sirve para mostrar miedo/rechazo. ✅
3. **Determinación, transformado en monstruo** — ep.1 min. 14:34 (hoja 7, img. 293-294):
   cuerpo agachado en cuclillas, garras extendidas hacia adelante, ojo brillante rojo.
   Sirve para **animar** (proteger a otro) pese a la forma monstruosa. ✅
4. **Suplicando ayuda** — ep.1 min. 14:39-14:46 (hoja 7, img. 295-298): manos juntas cerca
   del pecho, cabeza inclinada, «Please help, I can't control myself!». Sirve para pedir
   ayuda/vulnerabilidad. ✅
5. **Explicando avergonzado** — ep.1 min. 21:29-21:39 (`hoja_09.jpg` img. 410-414): mano
   rascándose la nuca, mirada de lado, hombros encogidos. Sirve para **explicar** con
   torpeza. ✅
6. **Ajustando los lentes, calmado** — ep.5 min. 14:18-14:50 (`ep05/hojas/hoja_06.jpg`
   img. 242-251): dos dedos en el puente de las gafas, cabeza ligeramente baja, expresión
   neutra/seria. Gesto recurrente del personaje (aparece también en el tráiler, ver pose
   1). Sirve para **pensar/pausa** antes de hablar. ✅
7. **Sprite de videojuego, puños en guardia** — «Jump+ Jumble Rush Okarun (TG) Sprite A»,
   hoja `personajes_02_wiki.jpg` img. #52: postura de combate de pie, puños en alto,
   ceño fruncido. Sirve para **presentar** en modo «listo para pelear». ✅

**Turbo Granny** (7 poses):
1. **Primera aparición, ojos en la oscuridad** — ep.1 min. 10:55 (`ep01/hojas/hoja_05.jpg`
   img. 230): sólo dos ojos amarillos brillantes y colmillos apenas visibles entre la
   negrura. Sirve para **presentar** la amenaza sin mostrar el cuerpo entero. ✅
2. **Persiguiendo en silueta** — ep.1 min. 11:10-11:23 (hoja 5, img. 235-239): forma
   encorvada corriendo a cuatro patas/dos patas, siluetada contra un fondo rojo.
   Transmite velocidad y agresión. ✅
3. **Forma yokai completa, atacando** — ep.1 min. 18:41-18:59 (`hoja_08.jpg` img.
   371-378): de pie, brazos en alto con garras curvas, melena blanca alborotada
   cubriéndole media cara, boca abierta con colmillos. Sirve para **regañar/amenazar**.
   ✅
4. **Forma humana anciana, sentada** — ep.5 min. 15:24-15:37 (`ep05/hojas/hoja_06.jpg`
   img. 255-257): de rodillas en el tatami, postura formal (seiza), pañuelo blanco en la
   cabeza. Sirve para **explicar** con calma (revela el amuleto y su historia). ✅
5. **Examinando de cerca, seria** — ep.5 min. 15:54-16:01 (hoja 6, img. 262-264): cabeza
   inclinada hacia adelante, ceño fruncido, mirada fija de lado. Sirve para **pensar**
   (analizando el problema del amuleto). ✅
6. **Dando órdenes, brazo extendido** — ep.5 min. 16:45-16:54 (hoja 6, img. 275-277):
   sentada de espaldas, brazo derecho extendido con un abanico, gesto autoritario. Sirve
   para **regañar/mandar**. ✅
7. **Concept art oficial, de pie** — «Turbo Granny Anime Concept Art», hoja
   `personajes_02_wiki.jpg` img. #74: de pie, cuerpo completo, kimono/haori rojo, pelo
   blanco largo cayendo a un lado, postura erguida y calmada. Sirve de referencia neutra
   para **presentar** el personaje fuera de una escena de acción. ✅ (ya citada por
   imagen en el punto 15 para el vestuario; aquí se usa sólo para la pose).

**Aira Shiratori** (7 poses):
1. **Disculpándose, inclinada** — ep.5 min. 11:49-12:19 (`ep05/hojas/hoja_05.jpg` img.
   199-210): torso ligeramente inclinado hacia adelante, manos juntas o cerca del pecho,
   ojos grandes y expresión preocupada. Sirve para **presentar** su fachada amable. ✅
2. **Sonriendo halagador** — ep.5 min. 12:15-12:19 (hoja 5, img. 208-210): cabeza ladeada,
   sonrisa amplia, mano tocándose el propio pelo. Sirve para **celebrar/coquetear**. ✅
3. **Chismeando con amigas, seña de victoria** — ep.5 min. 12:53-13:06 (hoja 5, img.
   220-222): de espaldas al espectador, mano levantada haciendo el signo de «V» con los
   dedos, hombros relajados en corrillo con sus amigas. Sirve para **celebrar** (en
   privado, distinto de su cara pública). ✅
4. **Sorprendida/preocupada de verdad** — ep.5 min. 13:36-13:38 (hoja 5, img. 232-233):
   ojos muy abiertos, cuerpo girado bruscamente hacia la caída de Momo, boca
   entreabierta. Sirve para mostrar que su preocupación por los demás sí es real a veces.
   ✅
5. **Burlona/sarcástica** — ep.5 min. 13:50 (hoja 5, img. 236): media sonrisa, ceja
   levantada, mirada de lado hacia Okarun. Sirve para **regañar** con sarcasmo. ✅
6. **Pateando (Acrobatic Silky)** — «Aira kicks Chorus giant», hoja `personajes_01_wiki.jpg`
   img. #28: pierna extendida en una patada alta, brazos abiertos para el equilibrio,
   pelo y falda ondeando por el movimiento. Sirve para **animar**/pose de acción de su
   arco de posesión. ✅
7. **De pie, casual (concept art)** — «Aira Anime Concept Art», hoja `personajes_02_wiki.
   jpg` img. #66: de pie, cuerpo completo, uniforme de instituto, postura neutra con las
   manos junto al cuerpo, mirada al frente. Sirve para **presentar** al personaje fuera de
   contexto. ✅

## Lo mejor para la lámina

- El contraste de paleta medido con `estilo.py`: escenas cotidianas cálidas y poco
  saturadas (25-27%) contra escenas sobrenaturales frías/mixtas muy saturadas (49-87%) —
  regla de color lista para usar en cualquier lámina de Dandadan.
- Momo con el aura tribal en los puños (ep.1, min. 17:45) para una pose de «presentar el
  poder» que no es sólo un puñetazo genérico.
- Aira haciendo el signo de «V» de espaldas mientras chismea (ep.5, min. 12:53) — su cara
  pública contra su cara privada en una sola pose, muy útil para un canal de «personajes
  que no son lo que parecen».
- El compositor Kensuke Ushio y el estudio Science SARU, ambos acreditados en pantalla en
  el propio tráiler oficial: dan pie a un cuadro de «ficha técnica» en la lámina sin
  inventar nada.
- La onomatopeya del propio título (ダンダダン) como posible elemento tipográfico
  decorativo de fondo, ya que es parte del ADN visual de la serie (ver también punto 19
  de imagen).

## No encontré

- ⚠️ **Vídeos de análisis / tendencias de TikTok**: TikTok no es accesible desde este
  servidor sin sesión; busqué «Dandadan TikTok trend» y «Dandadan meme video analysis» en
  el buscador web (ver Bitácora) sin dar con clips descargables.
- ⚠️ **AnimeThemes**: la API devuelve HTTP 522 y la web muestra directamente su página de
  mantenimiento («AnimeThemes.moe is currently down» por una caída real de su hosting,
  comprobado el 24-sep-2026, dos intentos). No es una confusión de mi parte: el servicio
  está caído de verdad.
- ⚠️ **YouTube**: pide iniciar sesión desde este servidor («sign in to confirm you're not
  a bot»); usé Dailymotion e Internet Archive en su lugar, tal como indica el aviso de
  arranque.
- ⚠️ **Resolución de los tráileres de Dailymotion**: son mirrors a 512×288 (baja
  calidad), no el archivo oficial en alta; los capítulos de Internet Archive están al
  tope de 720p que usan las herramientas del equipo (`fotogramas.py`/`episodio.py`) para
  no saturar el disco compartido. El punto 16 de imagen ya cubre capturas oficiales de la
  wiki a 1920×1080 de los mismos sitios, así que entre las dos partes sí hay material en
  alta.
- ⚠️ **Tracklist con marcas de tiempo de la OST**: no encontré una lista oficial de qué
  pista de Kensuke Ushio suena en qué escena; dejo el minuto de cada escena para
  reconocerla de oído.
- ⚠️ **Efectos de sonido**: el catálogo del wiki de efectos de sonido es la única fuente
  (comunitaria, no oficial) que lista las librerías de sonido reales usadas; no hay
  confirmación oficial del estudio.
- ⚠️ **Paleta de la escena de «Evil Eye»**: la medí a ojo sobre la hoja de contacto (el
  tráiler es de 512×288, demasiado bajo para que `estilo.py` dé una lectura fiable de
  cada plano suelto), no con la herramienta como las demás.

## Bitácora de búsqueda

- **Español**: «Dandadan tráiler», «Dandadan escena» (ya en `datos-video.md`, no
  repetidas).
- **Inglés**: «Dandadan anime opening theme "Otonoke" ending song season 1 list»
  (WebSearch, resultado: Wikipedia + ANN + Fandom, ✅), «Dandadan season 2 opening ending
  theme song 2025» (WebSearch, ✅), «Dandadan anime iconic sound effect running gag
  catchphrase "Okarun" onomatopoeia» (WebSearch → llevó al Soundeffects Wiki).
- **Directo (sin buscador)**: `api.animethemes.moe` (2 intentos, HTTP 522 y web de
  mantenimiento), `animethemes.moe/anime/dandadan` (confirma la caída), API de
  `dandadan.fandom.com` (`Aira Shiratori` wikitext, para la fecha de debut en anime),
  API de `soundeffects.fandom.com` (`action=parse&prop=wikitext`, tras dos intentos
  fallidos con la web normal bloqueada por un reto de Cloudflare), Wikipedia
  `List_of_Dandadan_episodes` (texto plano extraído con Python/regex), MusicBrainz (ya en
  `datos-video.md`), yt-dlp directo sobre 3 clips de Dailymotion y 2 capítulos completos
  de Internet Archive (720p, con `episodio.py`/`fotogramas.py --cortes`).
- **Herramientas usadas**: `fotogramas.py --cortes` (3 tráileres, 9 hojas de contacto),
  `episodio.py` (2 capítulos completos → `partes/episodios.md`, 484 y 404 planos,
  transcripción Whisper en japonés), `estilo.py --colores 5` (5 fotogramas propios,
  paleta y tipo de sombreado).
- Nada quedó vacío: cada punto (2, 4, 9, 10, 14) tiene hallazgos con fuente, minuto o
  enlace, y lo que no encontré está listado arriba con ⚠️, no omitido.

## Sigue: (ninguno) parte terminada — puntos 2, 4, 9, 10 y 14 completos, con `partes/episodios.md` (2 capítulos) y `partes/video.json` (11 referencias) ya escritos.
