# Vídeo · Captain Tsubasa (Supercampeones) · investigador de vídeo

Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Libreta de datos (no prosa), un dato por línea.
Sin serie hermana (no la menciona `encargos/47-captain-tsubasa-supercampeones.md`).
YouTube funcionó a ratos en esta tanda; el grueso del trabajo se hizo con capítulos completos
subidos a Internet Archive (mejor que la única review de DVD que trajo `recolectar.py`) y con
Dailymotion para tráilers.

## Hallazgos

### 2 · Fotogramas de escenas icónicas (capítulo y minuto)

Mirados de verdad con `herramientas/fotogramas.py` sobre capítulos completos (no reseñas).
Resolución real de los archivos (medida con `ffprobe`): 960×720 la serie de 1983, 1280×720 el
remake de 2018 — no hay copia pública en 1080p+ de episodios enteros; el 1080p sólo existe en
capturas sueltas oficiales, ya citadas por imagen en sus hojas de contacto (punto 16 de su parte).

- Tsubasa niño remata con una chilena/tijera en el aire justo antes del título, mirada fija en el
  balón · Captain Tsubasa (1983), ep. 1 «Kick full of dreams» · 0:10 · ✅ (fotograma visto) ·
  https://archive.org/details/captain-tsubasa-1983-s-1-ep-1
- El mismo Tsubasa celebra el gol con el puño en alto y una sonrisa amplia mientras la narración
  dice «This is the story of two young boys who dream to become the best soccer players in the
  world» · mismo episodio · 0:45-0:55 · ✅ · mismo enlace
- El joven Tsubasa patea el balón desde lo alto de una colina rural; cruza todo el valle y cae en
  el jardín de la mansión Wakabayashi, dejando a Genzo y su hermano boquiabiertos («¡Es imposible!
  ¡Llegó hasta allá! ¡Esa fue una patada increíble!») · Captain Tsubasa (2018), ep. 1 «¡Emprende
  vuelo!» · 16:44-17:56 · ✅ · https://archive.org/details/c-4pt-41n-tsub-4s-4-2018-01
- Flash-forward de cierre del mismo capítulo: un Wakabayashi ya adulto y profesional detiene de un
  manotazo el disparo del pequeño Tsubasa en un entrenamiento callejero bajo la lluvia («¡Detuvo mi
  disparo!») · mismo episodio · 21:30-21:35 · ✅ · mismo enlace
- Kojiro Hyuga (Meiwa FC) remata con una tijera por encima de un rival de su propio equipo, ya
  caído en el suelo, en su episodio de debut · Captain Tsubasa (1983), ep. 11 «El lobo solitario,
  Kojiro, aparece» (capítulo 10 del manga, confirmado en la wiki) · 7:24 · ✅ ·
  https://archive.org/details/captain-tsubasa-1983-s-1-ep-11

### 4 · Fondos y sitios: luz y paleta medida en fotogramas

Colores medidos con `herramientas/estilo.py` (Pillow) directamente sobre fotogramas de capítulo,
no sobre arte promocional (eso ya lo mide imagen en su punto 16 con wallpapers).

- Patio/playa escolar de Nankatsu al atardecer (donde juega Tsubasa de niño): cielo y luz casi
  totalmente anaranjados, sin verde ni azul · paleta: `#EC1F05` 54,6%, `#CE1105` 18,3%, `#CD612F`
  16,6%, línea de contorno `#883721` · sombreado plano con poca línea, saturación 89%, brillo 82% ·
  Captain Tsubasa (1983) ep. 1, fotograma 0:18 · ✅ (medido) ·
  https://archive.org/details/captain-tsubasa-1983-s-1-ep-1
- Colinas y valle rural donde vive Genzo Wakabayashi (remake 2018): verdes de campo y bosque con
  cielo celeste brillante · paleta: `#1F603A`, `#4CA761`, `#85D493`, cielo `#40D8FB` · sombreado
  degradado/pintado, línea `#5A825C`, saturación 53%, brillo 69% · Captain Tsubasa (2018) ep. 1,
  fotograma 15:08 · ✅ · https://archive.org/details/c-4pt-41n-tsub-4s-4-2018-01
- Cielo de atardecer/anochecer sobre el campo de entrenamiento callejero (escena final del mismo
  episodio): azul violeta con destellos rosados · paleta: `#1D2DC6`, `#292444` (sombra), `#6199E8`
  (cielo medio), `#9F7899` (nubes rosa) · sombreado degradado, saturación 51%, brillo 75% · mismo
  episodio, fotograma 21:55 · ✅ · mismo enlace
- Texturas reales equivalentes (CC0, `ambientcg.com/api/v2`): césped de cancha de barrio →
  **Grass001** (https://ambientcg.com/view?id=Grass001, disponible hasta 8K); malla/verja metálica
  de las canchas → **Fence007A** (https://ambientcg.com/view?id=Fence007A) · ✅ (todo el catálogo
  ambientCG es CC0, licencia confirmada en su web)

### 9 · Música y sonido

- Opening del remake 2018: **「スタートダッシュ!」(“Start Dash!”)** por **Johnny's WEST**, letra en
  pantalla («オープニングテーマ「スタートダッシュ!」») a partir del propio capítulo · Captain Tsubasa
  (2018) ep. 1, canción de 1:38 a 3:20 (logo «CAPTAIN TSUBASA» en pantalla a 1:50) · ✅ (créditos en
  vídeo + Mynavi News y Barks lo confirman) ·
  https://archive.org/details/c-4pt-41n-tsub-4s-4-2018-01· [Mynavi](https://news.mynavi.jp/article/20181003-700628/) ·
  [Barks](https://www.barks.jp/news/?id=1000160346)
- Ending del mismo remake: **「燃えてヒーロー」(“Moete Hero”, “Arde, héroe”)**, cantado EN PERSONAJE
  por «大空翼 (cv. 三瓶由布子)» —o sea, la propia voz de Tsubasa Ozora, Yūko Sanpei— con letra de
  Osamu Yoshioka, música de Hiroshi Uchiki y arreglo de Yutaka Sasaki, créditos leídos en pantalla ·
  mismo episodio, 22:35-23:25 · ✅ (créditos en vídeo + Natalie Music) ·
  [Natalie](https://natalie.mu/music/news/302165)
- Dato curioso confirmado en dos fuentes: para el arco de secundaria («chugakusei-hen») el mismo ED
  «Moete Hero» se reversionó en clave rock con el guitarrista **Marty Friedman** (ex-Megadeth) ·
  ✅ (Barks + Natalie) — sirve como gancho de música para redes.
- El ED «Moete Hero» **no es una canción nueva**: en el álbum recopilatorio oficial **「キャプテン翼・
  ベスト11」** (Best 11, 1993, disco de la serie/franquicia original) ya aparece como pista 11,
  etiquetada allí como tema de OPENING («燃えてヒーロー(オープニング・テーマ)») — es un tema clásico de
  toda la vida reciclado como ED en el remake · ✅ (MusicBrainz release-group
  `e49f7f8d-899c-486a-9347-edcfad36fd75`, dos ediciones del disco)
- El mismo álsum trae un **tema propio de personaje** para Kojiro Hyuga: «荒野の叫び(日向小次郎のテーマ)»
  (“Grito del páramo, tema de Kojiro Hyuga”), y un insert cantado en personaje por Tsubasa: «大空翼が
  歌う「明日に向かってシュート」» · ✅ (MusicBrainz, tracklist del disco)
- Ambiente: el OP 2018 es enérgico y coral (idol group masculino, ritmo de marcha deportiva); el ED
  «Moete Hero» es una power ballad más lenta con letra de superación («arde, héroe») cantada por el
  propio protagonista, casa con los créditos de fin de capítulo, no con la acción · ✅ (visto y oído
  en el propio capítulo)
- Efectos de sonido/onomatopeya que todo fan reconoce: el **grito del nombre de la técnica antes del
  remate** (“¡Drive Shoot!”, “¡Tiger Shot!”…) es la seña sonora de la franquicia, no un efecto de
  Foley — ya documentado con las técnicas exactas en `partes/texto.md` punto 25, se enlaza aquí para
  no repetir la lista completa · ✅
- Biblioteca de efectos 8-bit completa del videojuego original de Famicom (Tecmo, 1988), útil como
  referencia de "bit-crush" retro si la lámina quiere un guiño chiptune · ya citada en
  `partes/texto.md` punto 11 (The Sounds Resource) · ✅

### 10 · Vídeos: tráileres, escenas, análisis y tendencias

- **Tráiler oficial de TV Tokyo** para el anuncio del remake 2018 («再びアニメーションに!!» / «¡De
  nuevo en animación!!», estreno abril 2018, David Production): presenta a Tsubasa Ozora, Genzo
  Wakabayashi, Kojiro Hyuga y Roberto Hongo con el nombre de su actor de voz en pantalla, y el
  dominio oficial `ball-ha-tomodachi.com` · copia en Dailymotion (canal adorocinema) · 1:19 · ✅
  (logo de producción y créditos de staff propios en el vídeo) ·
  https://www.dailymotion.com/video/x88pglb
- Tráiler oficial del videojuego **«Captain Tsubasa: Rise of New Champions»** (Bandai Namco/Tamsoft,
  2020), copia subida por HobbyConsolas · 1:25 · ⚠️ (confirmada su existencia y canal, no se abrió
  cuadro por cuadro por presupuesto de tanda) · https://www.dailymotion.com/video/x7qvk2g
- **Análisis en inglés**: «Captain Tsubasa: How an anime series changed football in Japan and
  beyond» — Spolitix, canal **TRT World**, 6:30, subido 2021-10-04, 243 630 vistas (metadatos
  confirmados con `yt-dlp`) · explica cómo la serie empujó el fútbol real en Japón y motivó a
  futbolistas profesionales (Del Piero, Zidane, Nakata…) a jugar · ✅ ·
  https://www.youtube.com/watch?v=meO6vnleLQk
- **Cultura hispana / nostalgia** (no es vídeo, pero es la misma «tendencia» que pide el punto):
  tres medios latinoamericanos distintos (ENTER.co, Bagre.life, Fútbol y Asociados) coinciden en que
  Supercampeones fue «la puerta de entrada al anime» para niños de los 90 en la región y en que
  muchos se lastimaban intentando repetir sus jugadas en la vida real · ✅ (tres fuentes
  independientes con el mismo relato) ·
  [ENTER.co](https://www.enter.co/cultura-digital/entretenimiento/tbt-nostalgia-de-anos-atras-supercampeones/) ·
  [Bagre.life](https://bagre.life/contenido/cultura-pop/supercampeones-serie-futbol-mundial/) ·
  [Fútbol y Asociados](https://www.futbolyasociados.com/cultura/el-fenomeno-de-super-campeones/)
- **TikTok**: existen etiquetas activas con contenido (`#captaintsubasa`, memes y ediciones de
  escenas), comprobado que tienen vídeos, pero no se encontró una tendencia concreta y medible (reto
  de baile, sonido viral con cifra de uso) dedicada a la serie, a diferencia de otras franquicias ·
  ⚠️ no hay una tendencia específica que citar con datos.

### 14 · Poses analizadas en varias escenas

Postura, manos, mirada y gesto vistos fotograma a fotograma; capítulo y minuto de cada uno.

**Tsubasa Ozora**

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Salta y remata con una chilena/tijera, brazos abiertos para el equilibrio, mirada fija en el balón | Captain Tsubasa (1983) ep. 1 | 0:10 | celebrar / presentar |
| Puño en alto, sonrisa amplia, cabeza hacia atrás, celebrando el gol | Captain Tsubasa (1983) ep. 1 | 0:45-0:55 | celebrar |
| De bebé, sostiene el balón con ambas manos y sonríe mirando hacia arriba | Captain Tsubasa (2018) ep. 1 (opening) | 1:15 | presentar |
| Sostiene el balón contra el pecho, mirada de reojo hacia su amigo, ceja algo fruncida | Captain Tsubasa (2018) ep. 1 | 15:24 | explicar / preguntar |
| Primer plano sonriente, ojos muy abiertos y brillantes, mirando al horizonte («Siento que vamos a vivir grandes cosas») | Captain Tsubasa (2018) ep. 1 | 15:40 | animar |
| Se agacha a recoger algo del suelo y sonríe agradecido («¡Ten! ¡Gracias!») | Captain Tsubasa (2018) ep. 1 | 18:52-19:00 | agradecer / explicar |
| Primer plano serio, cejas rectas, boca entreabierta, preguntando «¿Qué pasa, Wakabayashi?» | Captain Tsubasa (1983) ep. 11 | 10:36 | pensar / preguntar |

**Genzo Wakabayashi**

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Brazos totalmente extendidos en cruz, gorra roja con «W», mirada firme a cámara | Tráiler oficial 2018 (TV Tokyo) | 0:21 | presentar / animar |
| Primer plano, ojos y boca muy abiertos, cara de shock | Tráiler oficial 2018 | 0:42 | reaccionar / explicar sorpresa |
| De pie con los brazos extendidos frente a la portería, gorra roja, aceptando un reto de tiros | Captain Tsubasa (2018) ep. 1 | 8:20 | presentar / desafiar |
| Salta lateralmente y estira el brazo para atajar algo en el aire | Captain Tsubasa (2018) ep. 1 | 9:50 | atajar / celebrar |
| De perfil, ceño fruncido, boca torcida en molestia («¡Maldito! ¿Escuchaste lo que dije?») | Captain Tsubasa (2018) ep. 1 | 16:12 | regañar |
| Boca y ojos muy abiertos mirando a lo lejos, incrédulo («¡No puede ser…! ¡Imposible!») | Captain Tsubasa (2018) ep. 1 | 17:08-17:16 | reaccionar / explicar asombro |
| Mano en el pecho, sonrisa de admiración genuina («¡Esa fue una patada increíble!») | Captain Tsubasa (2018) ep. 1 | 17:56 | animar / alabar |
| Ya adulto: extiende un brazo y detiene de un manotazo el disparo de un niño, gesto sereno | Captain Tsubasa (2018) ep. 1 (flash-forward final) | 21:30-21:35 | atajar / regañar con humildad |

**Kojiro Hyuga**

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Salta y remata con una tijera por encima de un rival ya caído, pelo alborotado hacia arriba | Captain Tsubasa (1983) ep. 11 | 7:24 | celebrar / atacar |
| Manos en la cintura, ojos cerrados, sonrisa arrogante, rival vencido detrás | Captain Tsubasa (1983) ep. 11 | 7:36 | regañar / burlarse con superioridad |
| Primer plano desafiante, cejas muy fruncidas, gritando «Veremos de quién es mejor el fútbol» | Captain Tsubasa (1983) ep. 11 | 9:00 | regañar / desafiar |
| De pie, solo con el balón bajo el pie, mirada seria mientras sus compañeros se alejan | Captain Tsubasa (1983) ep. 11 | 8:48 | pensar / decidir |
| Cabecea el balón con un brazo en alto, uniforme de Meiwa FC, marcador 8-0 en pantalla a su favor | Captain Tsubasa (1983) ep. 11 | 9:36 | celebrar ⚠️ (rostro no confirmado en grande, sólo por contexto de uniforme/marcador) |
| Retrato de presentación con nombre y actor de voz en pantalla, sonrisa confiada, mirada de reto | Tráiler oficial 2018 (TV Tokyo) | 0:36-0:39 | presentar |

## Lo mejor para la lámina

- La escena del «tiro imposible» de Tsubasa cruzando el valle hasta la mansión Wakabayashi (2018
  ep. 1, 16:44-17:56) es un momento de origen visualmente grande (colinas, cielo, casa) e ideal como
  fondo, con el balón cruzando el aire.
- Pose de Wakabayashi con los brazos en cruz y gorra roja (tráiler, 0:21) es un cuadro de «portero
  listo» perfecto, reutilizable en cualquier canal de deportes o edición del servidor.
- La paleta cálida naranja del atardecer escolar (punto 4, `#EC1F05`/`#CE1105`/`#CD612F`) da una
  lámina con identidad propia, distinta del típico verde de estadio.
- Hyuga solo con el balón mientras sus compañeros se alejan (ep. 11, 8:48) es una pose fuerte de
  personaje secundario, útil si el dueño quiere destacar a alguien distinto del protagonista.
- El ED «Moete Hero» cantado en personaje por la propia voz de Tsubasa es un dato único (poco común
  que el protagonista «cante» su propio ending) y buen gancho de texto para acompañar la lámina.

## No encontré

- Copias públicas en 1080p+ de episodios completos: sólo 720p en Internet Archive; el 1080p sólo
  existe en capturas sueltas oficiales de la wiki (ya citadas por imagen) · búsqueda en
  `archive.org/advancedsearch.php` y en la categoría «Screenshots» de `captaintsubasa.fandom.com`.
- `api.animethemes.moe` devolvió error 522 (servidor caído) en dos intentos distintos en esta tanda,
  igual que ya le pasó a `recolectar.py`: no se pudieron sacar los `.webm` oficiales de OP/ED que
  ese sitio suele tener listos para `fotogramas.py`.
- Una tendencia de TikTok concreta y medible (reto de baile, sonido viral con cifra) dedicada a
  Captain Tsubasa: sólo hay etiquetas genéricas con memes/ediciones sueltas · búsqueda «Captain
  Tsubasa TikTok tendencia viral 2024 2025».
- Tráiler oficial específico del anime de 1983 en japonés: sólo apareció el material de reseña de
  DVD de HobbyConsolas (ya en `datos-video.md`) y nada en Dailymotion/Internet Archive con «キャプテン翼
  1983 予告編» · ⚠️
- Confirmación directa de qué tema suena en las escenas más lacrimógenas de los arcos tardíos
  (Golden-23, Rising Sun): sólo se pudo confirmar la música mirando directamente el episodio 1 del
  remake 2018; los arcos posteriores no se descargaron por presupuesto de tanda.
- Vídeo cuadro a cuadro del tráiler del videojuego «Rise of New Champions»: sólo se confirmó que
  existe y su canal, sin analizarlo en detalle.

## Bitácora

- Español/inglés (WebSearch): «Captain Tsubasa TikTok tendencia viral 2024 2025 baile edit»,
  «"Captain Tsubasa" video essay analysis YouTube why influential football anime», «Supercampeones
  análisis video ensayo por qué es importante nostalgia latinoamérica» → TRT World/Spolitix
  (YouTube), ENTER.co, Bagre.life, Fútbol y Asociados, munaskamakis.com.
- Japonés (WebSearch): «キャプテン翼 2018 オープニング スタートダッシュ ジャニーズWEST エンディング 燃えてヒーロー» →
  Mynavi News, Barks, Natalie (música), Wikipedia japonesa; confirma OP/ED y el dato de Marty
  Friedman en el arreglo del ED de secundaria.
- `archive.org/advancedsearch.php` (API) para localizar episodios completos subidos por usuarios:
  33 episodios de 1983 (`captain-tsubasa-1983-s-1-ep-*`, 960×720) y 52 del remake 2018
  (`c-4pt-41n-tsub-4s-4-2018-*`, 1280×720, sub. español).
- `archive.org/metadata/<id>` para confirmar nombre exacto de archivo y duración antes de bajar con
  `fotogramas.py`.
- `captaintsubasa.fandom.com/api.php` (`action=query&list=allpages`, `prop=revisions&rvprop=content`)
  para el episodio exacto del debut de Kojiro Hyuga (ep. 11 de 1983, «The stray wolf, Kojiro
  appears», capítulo 10 del manga) y para la ficha del «Drive Shot» (primera aparición: manga cap.
  67).
- `musicbrainz.org/ws/2/release-group` y `/release` para el álbum recopilatorio oficial «キャプテン翼・
  ベスト11» (1993, MBID `e49f7f8d-899c-486a-9347-edcfad36fd75`) y su lista completa de pistas.
- `api.dailymotion.com/videos?search=` (cinco consultas) para tráilers del anime 2018 y del
  videojuego «Rise of New Champions»; ya se habían agotado en `recolectar.py` las búsquedas
  genéricas de opening/ending/escena, así que aquí se probaron términos más específicos.
- `api.animethemes.moe`: error 522 en dos intentos (mismo fallo que `recolectar.py`), no se insistió
  una tercera vez.
- `ambientcg.com/api/v2/full_json` para texturas CC0 de césped y malla metálica equivalentes a las
  canchas de barrio.
- `herramientas/fotogramas.py` sobre 4 fuentes de vídeo (1983 ep. 1, 1983 ep. 11, 2018 ep. 1,
  tráiler 2018 en Dailymotion) y `herramientas/estilo.py` (Pillow) para las 3 paletas medidas del
  punto 4. Resolución de cada vídeo confirmada con `ffprobe`.
- Vídeos borrados de `/tmp` tras sacar las hojas y los fotogramas grandes, según la regla de
  AYUDANTE.md (el disco es compartido).
