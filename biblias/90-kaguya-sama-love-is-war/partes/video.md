# Investigador de VÍDEO · Kaguya-sama: Love is War (90-kaguya-sama-love-is-war)

Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Enfoque de este encargo (90): **comedia y
rótulos**. La serie hermana `43-kaguya-sama-love-is-war` (COMPLETA) ya miró a
fondo los episodios 1 y 3 de la T1 (opening, ending, tráiler, sala del consejo,
poses); aquí se evita repetir eso y se mira el **episodio 2** entero (nuevo,
descargado de Internet Archive, ítem `kaguya-sama_202403`, nunca visto por el
otro equipo por falta de tiempo), con la cámara puesta en los **rótulos
cómicos** en pantalla (tarjetas de texto tipo manga) que es la firma visual de
la serie.

## 2 · Fotogramas de escenas icónicas

Vistas completas con `fotogramas.py` (panorámicas cada 8 s + fotogramas sueltos
en el segundo exacto) sobre `SEASON 1/02.mkv` del ítem
[kaguya-sama_202403](https://archive.org/details/kaguya-sama_202403) (Internet
Archive, 1280×720). Es el mismo opening/ending que confirmó la biblia hermana
(«Love Dramatic», «Sentimental Crisis»); aquí se listan escenas **nuevas**
propias del episodio 2, con foco en los rótulos cómicos.

- Tarjeta dorada 3D «生徒会長» (Presidente del Consejo Estudiantil), relámpagos blancos de fondo, estilo «anuncio de campeón» para presentar a Shirogane con ironía · ep. 2 min. 3:44 · ✅ (visto directo, patrón repetido de cartela-título que ya empieza el opening en el minuto 1:12 con el logo) · 1280×720
- Tarjeta roja/verde «海 VS 山!!» (mar contra montaña), rayo rojo de fondo, tipografía de combate de shōnen para una discusión trivial sobre el destino de un viaje · ep. 2 min. 11:04 · ✅ (visto directo) · 1280×720
- Anotación cómica tipo «ficha de personaje» «備考：カナヅチ» (nota: no sabe nadar) sobre un fotograma normal, y poco después «備考：童貞» (nota: virgen) con fondo a cuadros blanco/negro, burlándose de un dato privado de un personaje como si fuera una estadística oficial · ep. 2 min. 11:52 y 15:44-16:08 · ✅ (visto directo, dos apariciones) · 1280×720
- Etiqueta minúscula con nombre inventado «かしわざさん» puesta sobre una compañera de clase sin diálogo ni importancia en la trama (gag de «personaje random con nombre propio») · ep. 2 min. 16:32 · ✅ · 1280×720
- Cartel «本日の勝敗» (resultado de hoy) en dos versiones distintas a las que ya tiene la biblia hermana: aquí es un cartel de papel blanco simple (min. 15:12) y, al cierre del episodio, se amplía con un resumen completo del marcador «特に悪くなかったかぐやの機嫌を悪くして直して大分無駄骨を折った 白銀の一人負け» (Shirogane pierde él solo: por gastar mucho esfuerzo arreglando un humor de Kaguya que ni siquiera estaba mal) · ep. 2 min. 15:12 y 22:24 · ✅ (visto directo, la versión larga confirma que el marcador no es sólo un logo sino un texto narrativo completo) · 1280×720
- Texto suelto «ワナ» (trampa) junto al puño de Shirogane cuando urde un plan, funcionando como onomatopeya de intención en vez de sonido · ep. 2 min. 20:08 · ✅ · 1280×720
- Fondo a rayas de trama de semitono (halftone) tipo pantalla de vigilancia, usado para una mirada cómica de sospecha entre Shirogane e Ishigami · ep. 2 min. 15:44 · ⚠️ (una sola aparición vista, técnica distinta del fondo a cuadros psicodélico ya descrito en la biblia hermana)
- Secuencia de ending del episodio 2 (créditos técnicos con Kaguya y Shirogane asomados a la ventanilla de un avión de papel gigante, min. 22:48-23:52): confirma que el ending «Sentimental Crisis» cambia de animación cada episodio (no es una coreografía fija) · ✅ (visto directo, staff de animación legible en pantalla: A-real, DR movie, 電送屋, TAP, スタジオエル)

## 4 · Fondos y sitios: luz y paleta (medida en fotogramas)

Dos sitios nuevos del episodio 2 (la sala del consejo y la calle ya están
medidas en la biblia hermana), paleta sacada con `herramientas/estilo.py`
sobre fotogramas propios.

- **Sendero de montaña** (flashback de excursión familiar, mochila naranja, cielo despejado con nubes, luz de día franca) · fotograma de ep. 2 min. 10:00 · paleta medida: `#EEF4F6` 20.2% · `#82D1D6` 17.7% · `#275848` 17.3% · `#171922` 14.1% · `#4B8978` 12.1% · `#843131` 7.7% · `#BA9C7D` 6.6% · `#E0752A` 4.4% (mochila) · ✅ (medido) · sombreado degradado/pintado, línea normal `#4E5C4E`, saturación 43%, brillo 62% — es la escena más «luminosa» y natural de todo lo visto de la serie, contrasta con el interior del consejo
- **Pasillo del internado a contraluz** (ventanales en fila, luz de atardecer morado-rosa entrando de lado, columnas repetidas en perspectiva) · fotograma de ep. 2 min. 21:44 · paleta medida: `#4D3248` 17.6% · `#19101A` 17.0% · `#332335` 15.8% · `#674763` 13.0% · `#FBF8FB` 11.8% · `#D9B7D8` 9.2% · `#84647E` 9.1% · `#AE8BAE` 6.4% · ✅ (medido) · saturación 29%, brillo 45%, línea `#8F708A` — se usa para momentos íntimos de persecución/confesión, es el opuesto de la luz plana de la calle de Tokio que ya midió la biblia hermana
- Nota de continuidad: la sala del consejo (madera oscura + sofás verdes + alfombra roja) reaparece en este episodio con la MISMA paleta ya medida en la biblia hermana (min. 4:24, 18:00, 22:24) — confirma que es el color fijo del sitio, no un cambio puntual de iluminación.

## 9 · Música y sonido

- El opening («Love Dramatic feat. Rikka Ihara») y el ending («Sentimental Crisis», Halca) del episodio 2 son los MISMOS de toda la T1, ya identificados por la biblia hermana con fuente cruzada (Wikipedia + WebSearch); aquí se confirma de nuevo viéndolos completos en un episodio distinto (ep. 2, min. 0:56-2:16 y 22:24-23:52) · ✅
- Detalle nuevo del ending: la animación de créditos SÍ cambia cada episodio (aquí: avión de papel gigante con Kaguya y Shirogane asomados, min. 23:36-23:52) aunque la canción y su letra son fijas · ✅ (visto directo, contrasta con lo que decía la wiki de que el ending es «estático»)
- El gag central de audio del episodio 2 es el mismo que ya describió la biblia hermana (música orquestal falsamente épica bajo hechos triviales), pero aquí se ve con un ejemplo nuevo muy claro: la tarjeta «生徒会長» (min. 3:44) suena con fanfarria de trompetas y platillos tipo entrega de premios, para presentar sólo el cargo escolar de Shirogane · ✅ (visto y oído directo)
- Sonido del «ワナ» (trampa, min. 20:08): efecto de campanilla/chispa metálica corto, sin música de fondo, marca el cambio a modo «plan» del personaje · ⚠️ (un solo visionado, sin confirmar nombre de pista en el OST)
- Nombres de pistas del álbum «KAGUYA Music Collection Season 1» (compositor Kei Haneoka): «恋愛は戦» (Ren'ai wa Ikusa, «el amor es guerra», tema central), «私立秀知院学園» (Shiritsu Shuchiin Gakuen, tema del instituto — probablemente la música que suena en la sala del consejo), «二人の思考» (Futari no Shikō, «el pensamiento de los dos» — probable tema de las batallas mentales narradas), «突然の窮地» (Totsuzen no Kyūchi, «apuro repentino»), «カオス理論» (Kaosu Riron, «teoría del caos») · ⚠️ (una sola fuente agregada: búsqueda web que cita el blog Kayo Kyoku Plus; no se pudo abrir el blog ni Last.fm directamente —Cloudflare bloquea `navegar.py`— para confirmar con una segunda fuente propia)

## 10 · Vídeos (tráileres, escenas, tendencias, con minuto)

- Tráiler oficial adicional (colección `movie_trailers` de Turner/Internet Archive, sin voz en off, mismo material base que el tráiler VO de Dailymotion ya citado por la biblia hermana) · [Internet Archive, turner_video_136312](https://archive.org/details/turner_video_136312) · ⚠️ (confirmado que existe y es de la franquicia por su metadato `subject: Movie, Drama, trailer`, año 2019; no se comparó fotograma a fotograma con el de Dailymotion por tiempo)
- Película «Kaguya-sama wa Kokurasetai: First Kiss wa Owaranai», reacción completa en español de un youtuber (Darkraimola) sobre el film real (698 MB) · [Internet Archive](https://archive.org/details/kaguya-sama-movie-darkrai) · ⚠️ (localizado el ítem, no visionado completo por tiempo; sirve como pista de que hay reacciones en español a la película, útil para el investigador de voz/fandom hispano)
- **Tendencia de TikTok «Narrator's Mentality»**: clips cortos que recortan sólo las frases del narrador omnisciente (la voz que explica los pensamientos y hace comentarios sarcásticos, ligada a las cartelas de texto del punto 2) sobre música o mezclada con audio de otras fuentes (p. ej. mashups con diálogo de Barbie) · ✅ (dos fuentes: [TikTok, «Kaguya Love Is War Narrator»](https://www.tiktok.com/discover/kaguya-love-is-war-narrator) y [TikTok, «Kaguya-sama Love Is War Narrator Moments»](https://www.tiktok.com/discover/kaguya-sama-love-is-war-narrator-moments)) · el narrador en inglés lo dobla Ian Sinclair (dato de doblaje, para el investigador de voz)
- Búsqueda específica sobre el recurso cómico de las tarjetas de texto («chapter card», «text card gag», «鬼ごっこ 煽り文字» en japonés): no aparecen vídeos de análisis dedicados sólo a ese recurso visual en concreto (los análisis en vídeo hablan del humor o del narrador en general) · ⚠️ No encontré un vídeo-ensayo centrado sólo en los rótulos de texto (sí en el narrador, ver arriba).
- El vídeo-ensayo en inglés «How Kaguya-sama Won the War on Love: The Power of Premise» que ya cita la biblia hermana SÍ habla del recurso de la «voz de narrador todopoderoso» ligado a estas cartelas (confirmado por su descripción en Internet Archive, sin volver a bajarlo) · https://archive.org/details/how-kaguya-sama-won-the-war-on-love-the-power-of-premise · ⚠️ (descripción, no visionado propio en esta pasada)
- Episodio 2 completo, usado para todo lo anterior: [Internet Archive, `kaguya-sama_202403`](https://archive.org/details/kaguya-sama_202403), archivo `SEASON 1/02.mkv` · visto entero con `fotogramas.py` (panorámica cada 8 s, 180 fotogramas, + 13 fotogramas sueltos en el segundo exacto de cada hallazgo) · ✅

## 14 · Poses analizadas (capítulo y minuto)

Todas nuevas del episodio 2 (no repiten las ya analizadas por la biblia
hermana en los episodios 1 y 3).

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Kaguya girando la cabeza hacia atrás con mochila naranja de excursión, boca abierta hablando, montaña y bosque detrás | 2 | 10:00 | Presentar (en acción, al aire libre, con objeto) |
| Kaguya con un solo ojo rojo en primer plano y ceja alzada, mirada de sospecha antes de burlarse de Ishigami | 2 | 17:04 | Pensar / sospechar |
| Kaguya de pie sola en la sala del consejo tras irse Shirogane, manos juntas por delante, cabeza algo baja | 2 | 22:24 | Pensar / reflexionar a solas |
| Kaguya con los ojos muy abiertos, cejas levantadas, sorpresa genuina de cuerpo entero | 2 | 19:20 | Sorprenderse |
| Shirogane con la mirada fija y seria bajo el rótulo dorado «生徒会長», postura erguida de autoridad | 2 | 3:44-3:52 | Presentar (con cargo/título) |
| Shirogane con los ojos muy abiertos y ondas de «efecto de juego» dibujadas alrededor de la cabeza | 2 | 8:00-8:16 | Sorprenderse (cómico) |
| Shirogane flotando en un flotador de piscina, llorando a mares de forma exagerada (flashback «mar VS montaña») | 2 | 13:04-13:12 | Celebrar / en acción (cómico, autoparodia) |
| Shirogane con los puños cerca de la cara, sonrisa cerrada de plan siendo urdido, rótulo «ワナ» junto al puño | 2 | 20:00-20:08 | Regañar / tender una trampa |
| Shirogane sosteniendo un mechero encendido con chispa «ピカ», mirada de sorpresa hacia Kaguya | 2 | 17:20 | Animar / dar una idea |
| Chika sentada en el suelo, comiendo un dorayaki con las piernas encogidas, burbuja de texto «あなたといつでもお話がしたい» junto a ella | 2 | 7:12-7:28 | Explicar / pedir algo con cariño |
| Chika con las mejillas sonrojadas en rosa intenso y corazones alrededor, mirada de lado | 2 | 6:48-6:56 | Celebrar / coqueta |
| Chika con los ojos muy grandes y brillantes, manos cerca de la cara, fondo de flores | 2 | 14:16-14:40 | Sorprenderse (positivo) |
| Chika con las mejillas rojas por el gag «かしわざさん», mirada de lado avergonzada con chispas doradas de fondo | 2 | 16:24-16:40 | Explicar con gracia / coqueta |

## Lo mejor para la lámina

- La tarjeta «生徒会長» (min. 3:44): tipografía dorada 3D con relámpagos, plantilla perfecta para un cuadro de diálogo o cartela de «anuncio/título» en vez de una burbuja blanca genérica — es EXACTAMENTE lo que pide el encargo 90 en «rótulos».
- El cartel largo «本日の勝敗» con resumen de texto (min. 22:24): plantilla de pergamino/papel para mostrar un marcador de puntos o un resultado del canal, con su propio marco decorativo ya hecho por la serie.
- El sendero de montaña (min. 10:00) como fondo alternativo luminoso y natural, si el canal necesita algo fuera del internado.
- El gag «海 VS 山!!» (min. 11:04): plantilla de tipografía de combate roja/verde/rayos, útil para anunciar un «versus» o una votación del servidor con la propia estética de la serie.
- Chika con el dorayaki y su burbuja de texto (min. 7:12): ejemplo de cuadro de diálogo cómico con letra manuscrita informal, distinto del narrador serio.

## No encontré

- Confirmación en una segunda fuente propia (Last.fm o el blog Kayo Kyoku Plus directamente) de los nombres de pista del OST incidental: Last.fm bloquea con «Client Challenge» (Cloudflare) tanto a `curl` como a `navegar.py`, y el blog no devolvió el tracklist al leerlo con `curl` — se dejó como ⚠️ con la fuente agregada de la búsqueda web.
- Un vídeo-ensayo o análisis dedicado específicamente al recurso visual de los rótulos/cartelas de texto (si existe, está mezclado con vídeos sobre «el narrador» en general, que sí se encontraron) — búsquedas: WebSearch «Kaguya-sama text card gag analysis», «Kaguya-sama narrator captions comedy technique», «Kaguya-sama narrator text card meme tiktok trend» (inglés).
- El opening/ending «limpios» sin créditos superpuestos vía AnimeThemes: la API sigue devolviendo error 522 (caído), igual que en el recolector automático y que en la biblia hermana.
- Comparación fotograma a fotograma entre el tráiler de Turner (Internet Archive) y el de Dailymotion ya citado por la biblia hermana, por falta de tiempo en esta tanda — ⚠️ queda para un repaso si hace falta un tráiler alternativo.

## Bitácora

- `datos-video.md` (recolector): AniList (tráiler, enlaces oficiales), Dailymotion (búsqueda opening/ending/tráiler/escena), Internet Archive (vacío), MusicBrainz (vacío), AnimeThemes (522, caído) — punto de partida, no repetido.
- Leída primero `biblias/43-kaguya-sama-love-is-war/partes/video.md` (serie hermana, COMPLETA): confirma opening/ending/compositor/tráiler/sala del consejo/calle de Tokio y las poses de ep. 1 y 3; este documento evita repetir esos datos y se centra en el episodio 2 (no visto por el otro equipo) y en el enfoque «comedia y rótulos» del encargo 90.
- Internet Archive, `advancedsearch.php` (`q=kaguya-sama AND mediatype:movies`, inglés): 50 resultados revisados; se identificaron y comprobaron por metadato (`archive.org/metadata/<id>`) tres ítems nuevos no citados por la biblia hermana: `turner_video_136312` (tráiler), `kaguya-sama-movie-darkrai` (reacción a la película en español), `kaguya-sama_love_is_war_en-dub_subtitles` (subtítulos del doblaje inglés, no latino, no usado).
- Descarga completa de `Kaguya Sama Love is War/SEASON 1/02.mkv` (181 MB) del ítem `kaguya-sama_202403` (Internet Archive) a `/tmp/claude-0/trabajo/90-kaguya-sama-love-is-war-video/ep2.mkv`.
- `fotogramas.py` sobre `ep2.mkv`: panorámica completa cada 8 s (180 fotogramas, 4 hojas de contacto) + 13 fotogramas sueltos en el segundo exacto de cada hallazgo (rótulos, poses, sitios).
- `estilo.py` sobre 2 fotogramas propios nuevos: sendero de montaña (min. 10:00) y pasillo a contraluz (min. 21:44).
- AnimeThemes (`api.animethemes.moe`): reintentado (dos consultas), sigue con error 522.
- WebSearch (inglés): «Kaguya-sama Love is War OST tracklist Kei Haneoka soundtrack album titles», «Kaguya-sama Love is War narrator text card meme tiktok trend», «Kaguya-sama text card gag analysis», «Kaguya-sama narrator captions comedy technique».
- `curl` a Last.fm (bloqueado, «Client Challenge» de Cloudflare) y `navegar.py` sobre la misma URL (devolvió 0 caracteres): no se pudo confirmar el tracklist del OST con una fuente propia de segunda mano.
- Vídeo de `archive.org/metadata/<id>` consultado también para: `kaguya-sama-love-is-war-2019-720p-blu-ray` (ya descartado por la biblia hermana: es la película de imagen real, confirmado de nuevo por su metadato `mediatype`), `kaguya-sama-love-is-wars-fanservice` (compilación de fan, descartada por no aportar al enfoque de comedia/rótulos de este encargo).
