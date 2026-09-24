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
  (fotogramas 21-22) — ver punto 19 de imagen para la tipografía. ⚠️ no localicé un
  listado oficial de efectos de sonido específicos del anime (más allá del logo/título);
  busqué «Dandadan sound effects list» y «ダンダダン 効果音» sin resultado dedicado.
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

## Sigue: pendiente ficha del episodio 5 (procesando en segundo plano), pose de Turbo Granny en su forma yokai completa con minuto de ep1 (ronda de hojas 7-8 ya miradas, falta cerrar la tabla de poses del punto 14 para las 4 fichas de personaje y el punto 4 con 1-2 sitios más), imagen.json de referencias candidatas, y la tabla de cumplimiento + bitácora.
