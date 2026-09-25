# Investigador de VOZ Y PERSONAJES · K-On! (10-k-on)

Puntos de `ENCARGO.md`: **7** (personajes y encuestas de popularidad), **8**
(doblaje latino y frases), **12** (lo que ama el fandom y qué NO hacer), **13**
(descripción profunda de cada personaje) — los cuatro ya estaban escritos en
`biblia.md` con la red cerrada; aquí los **confirmo con segunda fuente** y
corrijo lo que hacía falta. Y los tres puntos nuevos que la biblia no tenía:
**20** (gustos y detalles), **21** (por qué la gente la ama) y **22** (fan dubs
y comunidad hispana).

Partí de `partes/datos-voz.md` (no repetí sus consultas de AniList) y de
`python3 herramientas/seccion.py 10-k-on --rol voz` / `--avisos` para ver lo ya
escrito y sus ⚠️.

**Dos errores de `datos-voz.md` que corrijo aquí** (para que el redactor no los
use): (1) el bloque «Doblaje latino: ficha de «Kon»» **no es de K-On!**: es
[Kon](https://doblaje.fandom.com/es/wiki/Kon), la mascota peluche de *Bleach* —
un falso positivo del recolector por el nombre parecido; lo comprobé leyendo el
wikitext completo. (2) el bloque de Reddit «r/Konosuba» tampoco es de K-On!:
es el subreddit de *Konosuba*, otra serie con nombre parecido. Ninguno de los
dos sirve para esta biblia.

## Hallazgos

### Punto 7 · Personajes y popularidad (confirmación)

La tabla de encuestas que ya tiene la sección 9 de la biblia (Newtype, Saimoe,
Akiba Souken…) está bien fundada; no encontré nada que la contradiga. Añado un
premio que no tenía, con **dos fuentes independientes**:

- **K-On! ganó el Anime Grand Prix de la revista Animage en 2009** (mejor
  título del año) ✅ ([Wikipedia, «List of Anime Grand Prix
  winners»](https://en.wikipedia.org/wiki/List_of_Anime_Grand_Prix_winners)).
  Ese mismo año **Yui Hirasawa quedó 1.ª en «mejor personaje»** y **Aki
  Toyosaki (su seiyū) 1.ª en «mejor actriz»** del mismo premio ✅ ([Wikipedia,
  ficha de Aki Toyosaki](https://en.wikipedia.org/wiki/Aki_Toyosaki)). Es el
  primer gran premio de la franquicia y confirma que, en Japón, el arranque
  fue con Yui como cara principal — aunque las encuestas de fans a medio plazo
  (sección 9) acaben favoreciendo a Mio.

### Punto 8 · Doblaje latino (confirmación a fondo + hallazgo grande)

**Sigue sin haber doblaje latino oficial.** Lo confirmo de nuevo, ahora
leyendo el wikitext completo (no sólo resultados de búsqueda) de Doblaje Wiki:
no existe página «K-On!»; busqué texto completo con
`srwhat=text` para «K-On!», «K-ON», «Houkago Tea Time», «Ho-kago Tea Time» y
«Sakuragaoka» y ninguna búsqueda devuelve una ficha de la serie ✅ (API de
Doblaje Wiki, comprobado 24-sep-2026).

**Pero sí existe un doblaje real, grabado y filtrado — sólo que nunca oficial.**
Esto es lo que la biblia tenía a medias (una fuente, dudosa) y ahora confirmo
y amplío mucho:

- **El estudio y los hechos** ✅ (dos fuentes que ya estaban, siguen en pie):
  **Elocuencia Studio**, estudio independiente **chileno**, grabó el episodio
  1 completo como demo profesional en **agosto de 2020**; se filtró en
  YouTube a finales de 2020 y se retiró por derechos de autor tras acumular
  unas 100 000 vistas
  ([SomosKudasai](https://somoskudasai.com/noticias/el-doblaje-latino-de-k-on-que-quizas-no-conocias/)).
- **El vídeo filtrado SIGUE disponible**, subido por un tercero al Internet
  Archive: [«K-On! Episodio 1 Latino [Doblaje Elocuencia
  Studio]»](https://archive.org/details/10000000-149823860194122-1366940053429074551-n)
  (MPEG4, 856×484, 24:11 min, subido originalmente como story/reel de
  Instagram) ✅. Es la prueba directa de que el doblaje existe: no es sólo un
  rumor.
- **Reparto confirmado con SEGUNDA fuente independiente** (antes era sólo
  SomosKudasai): un investigador de anime hispano contactó directamente a la
  actriz de Yui y al fundador del estudio, y publicó el reparto completo en
  vídeo largo en YouTube, con capítulos por personaje
  ([«¡DOBLAJE LATINO DE K-ON! Este es el elenco que lo
  conforma»](https://www.youtube.com/watch?v=1vadpuqpMIU), canal **ROCKERO
  ISRAEL-anime**, 19-jul-2024, 2825 vistas). Coincide en los cuatro nombres
  que ya teníamos:

  | Personaje | Actriz | Confirmación |
  |---|---|---|
  | Yui Hirasawa | **Lucía Suárez** | ✅ SomosKudasai + vídeo (min. 9:12) |
  | Mio Akiyama | **Carolina Cortés** | ✅ SomosKudasai + vídeo (min. 8:12) |
  | Ritsu Tainaka | **Marlene Pérez** | ✅ SomosKudasai + vídeo (min. 7:09) |
  | Tsumugi Kotobuki | **Bárbara Bustamante** (conocida como «Bárbara Usagi») | ✅ SomosKudasai + vídeo (min. 5:20) |

  Y **añade tres personajes que SomosKudasai no nombraba** (una sola fuente,
  ⚠️ hasta que aparezca en otro sitio):
  - **Ui Hirasawa** — **Pamela González** ⚠️ (vídeo, min. 1:37).
  - **Nodoka Manabe** — **Belén Marín** (el vídeo la llama «Belén marine»; el
    apellido «Marín» existe como actriz real en [Doblaje
    Wiki](https://doblaje.fandom.com/es/wiki/Bel%C3%A9n_Mar%C3%ADn)) ⚠️
    (vídeo, min. 4:23).
  - **Sawako Yamanaka** — **María Doris Cuevas** ⚠️ (vídeo, min. 3:02).
  - Comprobé las cuatro fichas de Doblaje Wiki de estas actrices (Lucía
    Suárez, Carolina Cortés, Marlene Pérez, Bárbara Bustamante) y de las tres
    nuevas: **ninguna menciona K-On!** en su wikitext completo — normal,
    porque nunca fue un trabajo oficial ni facturado, así que no entra en su
    filmografía de doblaje. No lo cuento como confirmación, sólo como
    identidad real de la persona.
  - **Quién dirigió y produjo**: el mismo investigador dice haber hablado
    directamente con Lucía Suárez y con **Felipe Waldhorn**, quien fundó
    Elocuencia Studio para intentar llevar el anime a Chile y dirigió tanto el
    doblaje como la mezcla musical; según él, el estudio **mutó después en lo
    que hoy es Sudamerican Voices** (vídeo anterior del mismo canal, [«K-ON!
    en español latino, toda la
    verdad»](https://www.youtube.com/watch?v=BH4oqr_m7Lk), min. 10:20-10:53).
    ⚠️ **dudoso**: la ficha oficial de [Sudamerican Voices en Doblaje
    Wiki](https://doblaje.fandom.com/es/wiki/Sudamerican_Voices) da como
    fundadores a **Cecilia Valenzuela** y **Raúl Valles Contador**, no a
    Waldhorn — aunque la ficha de [Felipe
    Waldhorn](https://doblaje.fandom.com/es/wiki/Felipe_Waldhorn) sí lo dice
    hoy «Operations Manager y Coach en Sudamerican Voices». Puede que ambas
    cosas sean ciertas (gente distinta fundando y luego trabajando ahí) pero
    no until pruebo que Waldhorn fundó Elocuencia; dejo la cita con la reserva.
- **FRASES TEXTUALES DEL DOBLAJE, con minuto exacto** — esto es lo que más
  faltaba. Bajé el vídeo del Internet Archive y le pasé
  `herramientas/voz.py` a dos tramos (el reproductor no permite `&t=` real
  porque es un `.mp4` alojado, así que enlazo con el segundo del archivo):

  > **[4:08]** «¿Ya han pasado dos semanas desde que iniciamos las clases?»
  > **[4:55]** «¡Al de música ligera, vamos!» **[4:57]** «Pero tenía planeado
  > unirme en la literatura.» **[5:20]** «Todos sus miembros se graduaron la
  > primavera pasada.» **[5:24]** «Por lo que será disuelto si no entran
  > cuatro personas durante este mes.» **[6:30]** «Si me uno ahora, seré la
  > presidenta.» **[6:44]** «Se refiere a música sencilla o popular.»
  > (transcrito con Whisper de
  > [archive.org/details/10000000-149823860194122-1366940053429074551-n](https://archive.org/details/10000000-149823860194122-1366940053429074551-n)
  > entre 4:00 y 7:44 ✅ — coincide con la escena real del episodio 1: Ritsu
  > arrastra a Mio y luego intenta reclutar a Yui y a Mugi para el club).
  > **[21:09]** «¿Al final sí te uniste al club?» **[21:19]** «No tengas fe
  > en mí para tocar la guitarra.» **[21:43]** «¿Qué habrán pensado cuando la
  > dejaron unirse al club?» (mismo archivo, 19:02-21:46 ✅ — Yui admite que
  > se apuntó sin tener guitarra).

  Esto **demuestra con audio real** que el doblaje de Elocuencia existe y
  cubre al menos el arco de reclutamiento del episodio 1. **Ojo:** es un
  *piloto no oficial, nunca lanzado*, no un doblaje licenciado — en la lámina
  no se debe presentar como «el doblaje latino de K-On!», sino como «el
  doblaje perdido» o «el piloto de Elocuencia Studio». Whisper se equivoca en
  nombres propios (transcribió «Ritsu» como «Richo» en el minuto 4:51):
  las frases citadas arriba son todas líneas sin nombres propios, para no
  arrastrar el error.
- **Ficha de voz del tramo** (con `voz.py`, mezcla de varias actrices, no
  sirve para un personaje suelto): registro agudo/medio (169-294 Hz según el
  tramo), **muy expresivo** (31-33 semitonos de rango) — es un doblaje con
  mucha entonación, no plano.
- **Dónde se ve K-On! en español hoy:** Crunchyroll, sólo **subtitulado** ✅
  ([Crunchyroll](https://www.crunchyroll.com/es/series/GXJHM3N2E/k-on)). Sigue
  sin doblaje oficial vigente.
- **Consecuencia para la lámina** (se mantiene lo que ya decía la biblia): las
  frases del personaje que hable en la lámina se traducen del japonés por
  nosotros, salvo que se quiera citar explícitamente el piloto perdido de
  Elocuencia (con su aviso de «no oficial»).

### Punto 12 · Lo que ama el fandom y qué NO hacer (confirmación)

Resuelvo el único ⚠️ dudoso de esta sección: **Junichi Eda, animador de K-On!,
murió en el incendio provocado de Kyoto Animation (18-jul-2019)** ✅ — ahora
con **segunda fuente independiente**: la lista de víctimas publicada por la
policía japonesa el 2-ago-2019, recogida en
[SoraNews24](https://soranews24.com/2019/08/05/names-of-10-kyoto-animation-arson-victims-released-family-and-friends-offer-words-of-remembrance/)
y en [Animation
Magazine](https://www.animationmagazine.net/2019/08/police-release-names-of-10-kyoto-animation-arson-victims/),
que lo nombra como animador de *Sound! Euphonium* y *K-On!*, 34 años, con
esposa e hija. Pasa de ⚠️ a ✅. El resto de la sección (té y pastel, Azu-nyan,
el coscorrón, «moeblob», la peregrinación a Toyosato) ya estaba bien fundado;
no encontré nada que corregir.

### Punto 13 · Descripción profunda de cada personaje (confirmación)

Cruce **altura, cumpleaños y edad** de AniList (ya en `datos-voz.md`) con la
ficha de personaje de **K-On! Wiki** (leída de nuevo, wikitext completo,
24-sep-2026): coinciden en las seis fichas → pasan de ⚠️ a **✅ confirmado en
dos fuentes** para Yui, Mio, Ritsu, Mugi, Azusa y Sawako (tabla completa en el
punto 20, abajo, para no repetirla).

- **Los ojos de Mio son gris-azulado**, no sólo «grises»: lo confirma
  [Anime Characters Database](https://www.animecharactersdatabase.com/characters.php?id=17059)
  («gray-blue eyes») además de NamuWiki (ya citada en la biblia) → pasa de ⚠️
  a ✅.
- **Tipo de sangre** (dato que la biblia no tenía): Yui O, Mio A, Ritsu B,
  Mugi O, Azusa AB, Sawako B — de la ficha de K-On! Wiki. Para Yui y Mio hay
  **segunda fuente** (Anime Characters Database, buscador) → ✅; Ritsu, Mugi,
  Azusa y Sawako quedan ⚠️ (una sola fuente) hasta cruzarlas.
- Nada que corrija en el carácter, miedos o relaciones ya escritos: son
  consistentes con lo que confirmé en las páginas de trivia de la wiki
  (`Yui_Hirasawa_Trivia`, `Mio_Akiyama_Trivia`, etc., leídas completas) — el
  detalle nuevo que sacan esas páginas va al punto 20, porque es de gustos y
  manías, no de carácter.

### Punto 20 · Gustos y detalles de cada personaje (NUEVO)

Fuente doble para altura/cumpleaños/edad: [AniList](https://anilist.co/anime/5680)
(ya en `datos-voz.md`) + wikitext completo de **K-On! Wiki**
([Yui](https://k-on.fandom.com/wiki/Yui_Hirasawa),
[Mio](https://k-on.fandom.com/wiki/Mio_Akiyama),
[Ritsu](https://k-on.fandom.com/wiki/Ritsu_Tainaka),
[Mugi](https://k-on.fandom.com/wiki/Tsumugi_Kotobuki),
[Azusa](https://k-on.fandom.com/wiki/Azusa_Nakano),
[Sawako](https://k-on.fandom.com/wiki/Sawako_Yamanaka)) — todas ✅ salvo donde
se avisa.

| | Yui | Mio | Ritsu | Mugi | Azusa | Sawako |
|---|---|---|---|---|---|---|
| Altura | 156 cm ✅ | 160 cm ✅ | 154 cm ✅ | 157 cm ✅ | 150 cm ✅ | 165 cm ✅ |
| Peso | 50 kg ⚠️ | 54 kg ⚠️ | 48 kg ⚠️ | 53 kg ⚠️ | 46 kg ⚠️ | 56 kg ⚠️ |
| Cumpleaños | 27 nov ✅ | 15 ene ✅ | 21 ago ✅ | 2 jul ✅ | 11 nov ✅ | 31 ene ✅ |
| Sangre | O ⚠️/✅* | A ✅ | B ⚠️ | O ⚠️ | AB ⚠️ | B ⚠️ |
| Objeto que siempre lleva | su guitarra **Gitah**, a la que habla como persona | su bajo **Elizabeth** y el cuaderno de letras | sus baquetas | el juego de té y algo dulce para repartir | su guitarra **Muttan** | la guitarra que esconde de su pasado |
| Comida favorita | «lo que sea, con tal de que esté dulce» ✅ (AniList + wiki) | *Gâteau au Chocolat* (pastel de chocolate en capas) ✅ (AniList + trivia de la wiki) | come mucho arroz (no hay «plato favorito» fijado) ⚠️ | dulces en general (los reparte para animar al club) ⚠️ | dulces, sobre todo pastel — pero **lo esconde** porque no quiere parecer «tierna» ⚠️ | pastel (se lo come aunque acabe de regañar a las chicas, sección 14) ✅ |
| Aficiones / manías | poner nombre a los objetos inanimados («Gitah», «Elizabeth», «Muttan», «Bukuro-chan» a unos guantes); no resiste un perro mono, sobre todo pugs; alérgica al aire acondicionado, se marea en coche | la fotografía tipo Lomography (cámara Lomo LC-A); escribe el kanji de «persona» 3 veces en la palma y se lo «come» cuando está nerviosa; le gustan el jazz y la música instrumental tranquila | fan de The Who y de **Keith Moon** como baterista; usa muchas palabrotas (la que más del grupo); toca la batería porque odia los movimientos finos de dedos | le gusta el *yuri* (tuvo fantasías Yui/Mio y Ritsu/Mio en el manga); de niña la educaron en casa; habla perfecto dialecto de Kansai | sus padres tocaban jazz, de ahí que ella tocara música; odia que la traten como a una niña o una gata, aunque actúa así sin querer | ocultó ser cantante y guitarrista de una banda de speed metal (**Death Devil**) durante años |
| Cómo se ve a sí misma | no se lo cuestiona: vive el momento, casi no piensa en el futuro | se cree la «adulta seria» del grupo, pero en realidad es la más infantil (llora fácil, le escriben letras «cursis», llama a sus padres «mamá» y «papá») ✅ (trivia de la wiki) | la líder natural, aunque **se autoproclamó** presidenta sin que nadie se lo pidiera | no le gusta alardear de su dinero; sólo quiere vivir cosas «normales» de instituto con sus amigas | la única sensata del grupo, y se enorgullece de ello — aunque las demás la traten como a la mascota | la profesora «dulce» de cara al instituto; no quiere que se sepa su pasado rockero |

\* Yui: blood type O confirmado en dos fuentes (K-On! Wiki + [Anime
Characters Database](https://www.animecharactersdatabase.com/characters.php?id=17064),
buscador).

- **Sobre Ui Hirasawa** (secundaria muy querida, sección 8 de la biblia):
  altura 154 cm, cumple 22 feb, sangre O — de AniList; es quien lleva la casa
  porque sus padres viajan (ya en la biblia) ⚠️ (una fuente para
  altura/sangre).
- **Sobre Nodoka Manabe**: altura 158 cm, cumple 26 dic, sangre A — de
  AniList ⚠️.

### Punto 21 · Por qué la gente la ama (NUEVO)

**Ventas y premios** (oficiales, dos fuentes cada uno):
- K-On! (T1+T2) vendió más de **520 000 Blu-ray/DVD** combinados a
  feb-2011, la cifra más alta de un anime de TV hasta entonces, superando a
  *Bakemonogatari* ✅ ([Anime News
  Network](https://www.animenewsnetwork.com/news/2011-02-22/k-on-is-1st-tv-anime-franchise-to-sell-500000+bds),
  [ANN, nota anterior](https://www.animenewsnetwork.com/news/2010-09-21/k-on-tops-bakemonogatari-as-no.1-tv-anime-in-bd-sales)).
  El primer volumen ya fue el **2.º Blu-ray más vendido de Japón** en su
  semana, cualquier categoría ✅ ([ANN](https://www.animenewsnetwork.com/news/2009-08-04/1st-k-on-volume-is-now-no.2-blu-ray-in-japan-so-far)).
- La película vendió **226 000 copias** en BD/DVD ✅ ([ANN](https://www.animenewsnetwork.com/news/2012-11-02/k-on-film-sells-226000-bd/dvd-copies-45000-in-rentals)).
- **Anime Grand Prix 2009** (mejor título del año, ver punto 7) ✅.

**Por qué conecta la gente** (ensayos/crítica, ya con enlace y cita):
- K-On! «codificó lo que hoy asociamos con moe» y cambió la estética del
  anime de KyoAni; lanzó la carrera de la directora **Naoko Yamada** ✅
  ([Anime Herald](https://animeherald.com/2022/02/12/why-k-on-deserved-its-second-chance/)).
  El mismo artículo dice que se identifica con **Yui y Azusa**: «Yui
  desarrolla una pasión por la guitarra para superar su inseguridad de ir a
  la deriva en la vida», y tocar una Gibson Les Paul (la de rockeros de
  verdad) hace la conexión más fuerte.
- Otro ensayo dice que el público conecta sobre todo con **Azusa**, «la
  estudiante de años menores, seria y solitaria», porque la serie no habla de
  sueños que se cumplen sino de la vida real: «muchos necesitan convertirse
  en oficinistas tranquilos; no todos están hechos para la cima» ✅
  ([bateszi anime
  blog](https://bateszi.me/2013/04/11/all-good-dreamers-pass-this-way/)).
- Reddit, todavía en 2025-2026, sigue lleno de gente diciendo que es su anime
  favorito de siempre: [«Today, I confess that K-ON is my favorite anime of
  all
  time»](https://reddit.com/r/anime/comments/1w6jgdr/today_i_confess_that_kon_is_my_favorite_anime_of/)
  ✅; hay hasta un vídeo-ensayo reciente sobre su impacto cultural, [«Japan Was
  Never The Same After This
  Anime»](https://reddit.com/r/anime/comments/1wi5gp6/japan_was_never_the_same_after_this_anime_video/)
  (2026) ✅; y un torneo de «Best Girl» de todo el foro donde K-On! sigue
  llegando a ronda de 128 ✅
  ([hilo](https://reddit.com/r/anime/comments/1vct8ci/best_girl_if_ranime_had_any_taste_ro128_kon/)).

**La escena que hace llorar:** la graduación, **T2 ep. 24** (última del
anime). Azusa se queda sola en el club cuando las otras cuatro se gradúan;
ellas le cantan **«Tenshi ni Fureta yo!»** («He tocado a un ángel») como
regalo de despedida — una canción a la vez triste y feliz ✅ ([Anime
Herald](https://animeherald.com/2022/02/12/why-k-on-deserved-its-second-chance/):
«a perfect moment of closure, as the girls finally find the words to show
their appreciation to younger guitarist Azusa»; cuenta oficiosa [Daily
K-ON!](https://x.com/DailyKEION/status/1816279105337282647) en X, 2024,
resume igual la escena). El minuto exacto de las frases de Azusa
(«estoy bien, seguiré con el club… está Ton», 17:43, y cuando pide que la
escuchen, 18:20) ya estaba sacado del subtítulo por el equipo en la sección 15
de la biblia — aquí confirmo que es precisamente la escena que la crítica y
el fandom señalan como la más emotiva de la serie, no sólo una elección
nuestra. Por qué duele: no es un final feliz sin más — es el primer
recordatorio de que el club (y la adolescencia) se acaba, y varios
comentarios de Reddit dicen literalmente que lloraron aunque no sean
sentimentales, sobre todo si vieron el capítulo cerca de su propia graduación
✅ (búsqueda web, resultados de MyAnimeList/foros citados arriba).

### Punto 22 · Fan dubs y comunidad hispana (NUEVO)

**Fandubs de aficionados en español** (no confundir con el piloto profesional
de Elocuencia del punto 8):
- [«K-ON! fandub doblaje latino»](https://www.youtube.com/watch?v=scal1_PRGh8)
  — canal **NVEdelMIZTERIO**, 3-ago-2011, 728 vistas, calidad casera («sin
  estudio ni dedicación», dice la propia descripción) ✅ (ficha bajada con
  yt-dlp).
- Coberturas cantadas en español de **«Fuwa Fuwa Time»** (canción-insignia
  de la serie, T1 ep. 6): [«Fuwa Fuwa Time - K-ON! | Cover en Español
  (Nani)»](https://www.youtube.com/watch?v=XSiJjPNVOMg), canal **nani**,
  12-nov-2021, 1160 vistas ✅ (ficha bajada con yt-dlp); hay más versiones
  con menos datos verificables porque YouTube bloqueó la extracción en este
  contenedor (canales «Lin Kaimane» y «NeqqoVer», ⚠️ sólo por el título de
  búsqueda).
- **Cover cantado en español latino del ending** «Don't say "lazy"» (T1),
  por **Daniel Sosa**, en SoundCloud: [«K-On! | Ending ~Tv Size~ (Don't say
  lazy) Español Latino»](https://soundcloud.com/daniel-sosa-811799457/k-on-ending-tv-size-dont-say)
  ⚠️ (una fuente, no pude reproducirlo desde aquí para comprobar el audio).
  No encontré un cover cantado del opening «Cagayake! GIRLS» en español —
  sólo versiones instrumentales (guitarra, bajo, jazz) y vídeos con
  subtítulos en español, que no son lo mismo que un cover cantado.
- **Parodias y memes hispanos específicos de K-On!:** no encontré ninguno
  propio de la comunidad hispana (con nombre de página, canal o hashtag) —
  busqué «Azu-nyan», «Gitah» y «Mio» combinados con «meme español/latino» y
  sólo aparecen memes genéricos de anime sin ligar a K-On!. **Sí existe** una
  parodia en inglés, [*K-On! The Abridged
  Series*](https://tvtropes.org/pmwiki/pmwiki.php/WebVideo/KOnTheAbridgedSeries)
  (ya citada en la sección 14 de la biblia), pero no es hispana.

**El hallazgo más grande de este punto** es que la comunidad hispana de anime
**sí se ha enganchado fuerte con el tema del doblaje perdido** (punto 8): el
canal **ROCKERO ISRAEL-anime** le dedicó **dos vídeos largos de YouTube**
(10:36 min y 10:49 min, ambos de julio de 2024, 6171 y 2825 vistas) y **al
menos 7 TikToks** (uno por personaje, más uno general con 2825 vistas
replicado) investigando quién dobló a cada una, contactando directamente a
la actriz de Yui y al fundador del estudio. Es, en la práctica, la pieza más
grande de «comunidad hispana hablando del doblaje de K-On!» que existe, más
que cualquier fandub — enlazada completa en el punto 8.

## Lo mejor para la lámina

1. **Las frases reales del piloto perdido** («¡Al de música ligera, vamos!»,
   min. 4:55; «Si me uno ahora, seré la presidenta», min. 6:30) dan una voz
   latina auténtica, aunque haya que rotularla como «doblaje no oficial,
   nunca lanzado» — es un dato único que ningún fan de K-On! hispanohablante
   conoce del todo.
2. **Mio sigue siendo la apuesta segura** para #general (gana casi todas las
   encuestas), pero **Yui ganó el primer gran premio** (Grand Prix 2009): sirve
   para una lámina 2 sobre «quién manda según la época».
3. **La graduación (T2 ep. 24, «Tenshi ni Fureta yo!»)** es, por lejos, la
   escena que la crítica y el fandom repiten como la que hace llorar: buena
   candidata para un evento o lámina emotiva del canal, no para #general
   (que pide tono ligero de bienvenida).
4. Ficha de gustos (punto 20) lista para usar en textos del bot o en una
   «lámina 2» tipo cromo de personaje: comida, manía y objeto por chica.
5. La comunidad de ROCKERO ISRAEL-anime demuestra que **sí interesa el
   doblaje latino de series sin doblaje oficial**: encaja con el espíritu del
   servidor (doblaje y locución) para un futuro evento o hilo fijado.

## No encontré

- ⚠️ **Reparto de Ui, Nodoka y Sawako del piloto de Elocuencia en una
  segunda fuente**: sólo el vídeo de ROCKERO ISRAEL-anime los nombra; busqué
  sus nombres en Doblaje Wiki (fichas de las actrices, wikitext completo) y
  no aparece K-On!, como es de esperar en un trabajo no facturado.
- ⚠️ **Quién fundó Elocuencia Studio de verdad**: el vídeo dice que fue
  Felipe Waldhorn: la ficha oficial de Sudamerican Voices en Doblaje Wiki da
  otros dos fundadores. No hay forma de resolver esto desde aquí sin
  contactar a las partes.
- ⚠️ **Audio de los covers de Fuwa Fuwa Time y del ending** de otros canales
  (Lin Kaimane, NeqqoVer, Daniel Sosa): no pude reproducirlos ni bajar su
  ficha porque YouTube y SoundCloud bloquearon la extracción automática desde
  este contenedor varias veces seguidas (aviso de «confirma que no eres un
  robot»); quedan citados sólo por su título y enlace.
- ⚠️ **Parodias o memes propios de la comunidad hispana**: busqué en español
  varias combinaciones (Azu-nyan, Gitah, Mio + meme español/latino) y no
  encontré ninguno específico de K-On!, sólo genéricos de anime.
- No hice más tramos de `voz.py` sobre el vídeo del Internet Archive por
  presupuesto de tiempo: quedan 24 minutos de audio real sin transcribir del
  todo, que darían más frases textuales si se necesitan para una lámina 2 de
  doblaje.
- Peso corporal (kg) de las seis: sólo la ficha de K-On! Wiki lo da: ⚠️ una
  fuente.

## Bitácora de búsqueda

**API de Doblaje Wiki** (wikitext completo, no sólo resultados de búsqueda):
`action=parse&prop=wikitext&page=K-On!` (no existe), `page=Kon` (es Bleach,
no K-On!), `page=Minako Kotobuki`, `page=Lucía Suárez`, `page=Carolina
Cortés`, `page=Marlene Pérez`, `page=Bárbara Bustamante`, `page=Pamela
Gonzales`, `page=María Doris Cuevas`, `page=Belén Marín`, `page=Felipe
Waldhorn`, `page=Sudamerican Voices`. Búsqueda de texto completo
(`list=search&srwhat=text`) con «K-On!», «K-ON», «Houkago Tea Time»,
«Ho-kago Tea Time», «Sakuragaoka».

**API de K-On! Wiki (Fandom)**, wikitext completo: fichas principales y de
trivia de Yui, Mio, Ritsu, Mugi, Azusa y Sawako Hirasawa/Akiyama/Tainaka/
Kotobuki/Nakano/Yamanaka.

**yt-dlp / voz.py** sobre
[archive.org/details/10000000-149823860194122-1366940053429074551-n](https://archive.org/details/10000000-149823860194122-1366940053429074551-n)
(dos tramos, 0-240 y 1140-1380 s más el tramo 240-480 s que sí dio texto);
metadatos de vídeo (`--write-info-json`) y subtítulos automáticos en español
(`--write-auto-subs --sub-langs es`) de
`youtube.com/watch?v=1vadpuqpMIU` y `youtube.com/watch?v=BH4oqr_m7Lk`
(canal ROCKERO ISRAEL-anime); `--write-info-json` de
`youtube.com/watch?v=scal1_PRGh8` y `youtube.com/watch?v=XSiJjPNVOMg`.

**Buscador web** (en español e inglés, unas 20 búsquedas de las ~50
disponibles): «Elocuencia Studio doblaje K-On chileno ANMTV», «K-On fandub
español latino YouTube canal», «K-On opening cover español "Cagayake girls"
Don't say lazy», «K-On databook gustos comida favorita cumpleaños altura»,
«rockeroisrael K-ON doblaje latino estudio director Elocuencia», «Elocuencia
Studio Felipe fundador director doblaje chileno», «Pamela González / María
Doris Cuevas / Belén Marín doblaje» (vía Doblaje Wiki), «rockeroisrael Azusa
Nakano doblaje latino Susana Cano voz» (sin confirmar), «why K-On is beloved
iyashikei moe», «K-On sales Blu-ray awards Animation Kobe Newtype», «K-On
graduation episode crying Tenshi ni Fureta yo», «Anime Grand Prix Animage
K-On 2009», «Junichi Eda Kyoto Animation K-On victim arson», «K-On fandub
español latino TikTok cover opening», «K-On meme español latino Azu-nyan
Mio Gitah», «Cagayake GIRLS cover español latino opening», «Don't say lazy
cover español latino ending».

**Reddit vía Arctic Shift** (`subreddit=anime&title=K-On`): 10 hilos reales
(el bloque de `datos-voz.md` era de otro subreddit por error, ver arriba).
Reddit.com directo sigue bloqueado desde este contenedor (403 Blocked);
Arctic Shift dio *timeout* en dos intentos posteriores (posible límite de
tasa) — no insistí más de dos veces seguidas, según la regla del encargo.

**WebFetch**: `animeherald.com` (reseña completa), `bateszi.me` (reseña
completa), `somoskudasai.com` (artículo completo); `x.com` bloqueado (403).

Sigue: nada obligatorio pendiente de los puntos 7, 8, 12, 13, 20, 21 y 22.
Quedan como posibles ampliaciones (no obligatorias, ver «No encontré»): más
tramos de `voz.py` sobre el resto del vídeo del Internet Archive, y resolver
quién fundó Elocuencia Studio si el redactor cree que hace falta.
