# Parte de VÍDEO · Hellblade (Senua's Sacrifice + Senua's Saga: Hellblade II)

Investigador de vídeo. Puntos 2, 4, 9, 10 y 14 de `ENCARGO.md`. Es un videojuego: en vez de
opening/ending se miraron **tráileres, cinemáticas y escenas icónicas** (Dailymotion, Internet
Archive), con `herramientas/fotogramas.py` (`--cortes` = un fotograma por plano) y
`herramientas/episodio.py` (ficha minuto a minuto en `partes/episodios.md`). Parte de
`datos-video.md` (Dailymotion, Internet Archive, MusicBrainz): no se repiten esas consultas.
Es una libreta de datos: un dato por línea, con fuente, ✅ (dos fuentes) o ⚠️ (una).

## Índice
- [Punto 2 — Fotogramas de escenas icónicas](#punto-2)
- [Punto 4 — Fondos y sitios: niebla, luz y paleta](#punto-4)
- [Punto 9 — Música y sonido](#punto-9)
- [Punto 10 — Vídeos: tráileres, escenas, análisis, tendencias](#punto-10)
- [Punto 14 — Poses de Senua analizadas](#punto-14)
- [Lo mejor para la lámina](#lamina)
- [No encontré](#no-encontre)
- [Cumplimiento de mis puntos](#cumplimiento)
- [Bitácora de búsqueda](#bitacora)

---

<a name="punto-2"></a>
## Punto 2 — Fotogramas de escenas icónicas

Los tráilers de Dailymotion de `datos-video.md` sólo están espejados a 512×288 (comprobado con
`yt-dlp -F`, sección Bitácora); para llegar al **1080p o más** que pide el encargo se bajó el
**tráiler oficial de cada juego directamente del CDN de Steam** (`store.steampowered.com/api/appdetails`
→ `movies[].mp4/hls_h264`, sin necesitar YouTube ni iniciar sesión), a 1920×1080 real, y se sacó el
fotograma exacto con `ffmpeg -ss <segundo>` sin reescalar. Mismo contenido que las hojas de
Dailymotion ya vistas (incluidas en Punto 10), pero en la resolución que pide el punto 2.

### Hellblade: Senua's Sacrifice — tráiler oficial (Steam app 414340, «Official Trailer»)
_Fuente: https://store.steampowered.com/app/414340 · vídeo: video.akamai.steamstatic.com/store_trailers/414340/116148/…/hls_264_master.m3u8 (formato 5800, 1920×1080) ✅ (mismas escenas confirmadas en la copia de Dailymotion `x5v5lz0` de menor resolución)_

| Minuto | Escena | Qué se ve |
|---|---|---|
| 0:29 | Retrato de Hela | primer plano frontal: corona/tocado dorado con gema turquesa, cuello de piel, luz dorada de un prado en flor detrás (fotograma 1920×1080 medido en Punto 4) |
| 0:38 | El árbol de las ofrendas | silueta de un árbol muerto con restos colgando contra un cielo tormentoso magenta/púrpura — el árbol de Valravn |
| 1:22 | La espada rúnica | Hela empuña una espada larga que brilla en **azul eléctrico** entre ramas negras; la luz de la hoja ilumina su cara de perfil |
| 1:34 | Combate contra un draugr con cuernos | primer plano de lucha cuerpo a cuerpo; en la cadera de Senua brilla un **símbolo espiral azul-blanco** (el mismo icono que usa la interfaz de «foco»/parry del juego) sobre bruma roja de sangre |
| 1:45 | Cierre del tráiler | silueta de Senua desnuda caminando hacia una luz blanca cegadora, una pequeña hoguera a la izquierda; corta al logo «HELLBLADE: Senua's Sacrifice» |

### Senua's Saga: Hellblade II — tráiler oficial (Steam app 2461850, «Official Trailer»)
_Fuente: https://store.steampowered.com/app/2461850 · vídeo: video.akamai.steamstatic.com/store_trailers/2461850/638331/…/hls_264_master.m3u8 (formato 5800, 1920×1080) ✅ (mismas escenas que la copia de Dailymotion `x8qciu2`, con el hashtag #TheGameAwards, analizada abajo)_

| Minuto | Escena | Qué se ve |
|---|---|---|
| 0:10 | Costa tras el naufragio | Senua de espaldas frente a un barco vikingo destrozado en una playa de rocas, niebla marina y sol velado — la llegada a Islandia (ver Punto 4 para la paleta) |
| 0:52 | El sendero de calaveras | Senua camina de espaldas hacia una calavera humana clavada en una rama, en un bosque nocturno con niebla ocre; lleva los brazos manchados de sangre |
| 1:45-1:53 | Mano corrupta | una mano gris y descarnada agarra la cara de Senua; ella cierra los ojos y grita en silencio — la Oscuridad tomando forma física |
| 2:19 | Cierre del tráiler | tarjeta de título «Senua's Saga / Hellblade II» en rojo y blanco sobre negro (tipografía romana con remates, ver punto 5 de `texto.md`) |

### Otras escenas icónicas (resolución más baja, Dailymotion re-subido; sirven para identificar el momento, no como cita en 1080p)
- **Hela, combate final** («surrender»/rendirse): el jefe final obliga a soltar el arma en vez de seguir golpeando; escena descrita por reseñas y jugadores como el clímax emocional del juego, la cámara revela que Hela «es» la propia Senua · fuente textual (no fotograma propio) ✅ · https://www.mic.com/articles/183609 y foros de Steam Community
- **Garm, el lobo gigante** en ventisca: combate borroso en blanco casi total, capturado en baja resolución del vídeo «Ragnarok Trailer/dev diary» de Dailymotion, [0:19](https://www.dailymotion.com/video/x5pbur7?t=19) ⚠️ (512×288 de origen, sólo para identificar la escena)
- **El gigante/torre de fuego** al fondo de un valle en penumbra, Hellblade II tráiler Game Awards, [0:36](https://www.dailymotion.com/video/x8qciu2?t=36) ⚠️ (misma limitación de resolución que la fuente Dailymotion; el tráiler de Steam no llega tan lejos en el montaje)

---

<a name="punto-4"></a>
## Punto 4 — Fondos y sitios: niebla, luz y paleta

### Dónde está ambientada cada entrega
- **Senua's Saga: Hellblade II (2024)** ocurre en la **Islandia del siglo IX**; Senua es orcadiana (de las **Orcadas/Orkney**, Escocia) y es capturada por esclavistas nórdicos que la llevan a Islandia — la Islandia es el escenario real, Orkney es el origen del personaje, no un sitio recorrido en el juego · Windows Central y Xbox Wire (Wanderers) ✅ · https://www.windowscentral.com/senuas-saga-hellblade-ii · https://news.xbox.com/en-us/2024/05/20/hellblade-2-environmental-design-inspired-by-iceland/
- El director creativo **Tameem Antoniades** visitó Islandia tras salir el primer juego, viajó a **40 sitios** distintos y quedó tan impresionado que decidió ambientar la secuela allí; el jefe de estudio **Dom Matthews** la llama «una carta de amor a Islandia» y dice «la geografía de Islandia es mejor de lo que podríamos haber imaginado […] se siente anclada en la naturaleza, pero casi alienígena» · Xbox Wire, PCGamesN ✅ · https://news.xbox.com/en-us/2024/05/20/hellblade-2-environmental-design-inspired-by-iceland/ · https://www.pcgamesn.com/hellblade-2/preview
- Director de arte de entornos **Dan Attwell**: Islandia «es como un parque temático geológico, hay tanta diversidad»; la fotogrametría da «un nivel de realismo que no se consigue a mano»; el equipo guardó **rocas islandesas reales** en el estudio como referencia física · Xbox Wire ✅ (VFX director citado junto: **Mark Slater-Turnstill**) · https://news.xbox.com/en-us/2024/05/20/hellblade-2-environmental-design-inspired-by-iceland/
- **Hellblade II tiene más de 370 piezas de fotogrametría**, frente a **una sola** en el Hellblade original (2017): el primer juego no escaneó sitios reales, sus fondos son mayormente pintados/procedurales · Xbox Wire, comparado con Screen Rant/reseñas ✅
- Sitios reales reconocibles en Hellblade II: **Reykjanestá** (costa suroeste de Islandia: acantilados, playas de roca negra, volcanes submarinos) y **Freyslaug**, asentamiento ficticio inspirado en los manantiales termales de **Fosslaug** (norte de Islandia, colinas verdes) · Xbox Wire ✅ (un solo artículo pero cruza con Gameranx) · https://gameranx.com/updates/id/498673/article/senuas-saga-hellblade-ii-visual-team-discuss-recreating-iceland-for-realism/
- El estudio trabajó con **Quixel/Megascans** (Epic Games) para llevar la fotogrametría de rocas y suelos islandeses al motor · búsqueda con varias fuentes coincidentes ⚠️ (nombre técnico, sin cita textual de un solo artículo)

### Niebla, luz y paleta medidas en fotograma (con `herramientas/estilo.py`, Pillow)
Todas de fotogramas propios (1280×720) sacados con `fotogramas.py --fotograma`; el hex es el color dominante medido, no aproximado a ojo.

| Sitio / escena | Fuente y minuto | Luz | Paleta medida (dominante → acentos) |
|---|---|---|---|
| Prado con árbol a contraluz, Senua de espaldas entre flores lilas | Ragnarok Trailer (dev diary), Dailymotion, [0:01](https://www.dailymotion.com/video/x5pbur7?t=1) | sol de frente, niebla luminosa que quema el blanco | #FBFAF4 29% · #F4F0DF 21% · ocres #715B32 8% / #A18858 5% · saturación 26%, brillo 74% |
| Hela de cerca, corona dorada con gema turquesa, niebla plana detrás | Ragnarok Trailer, [0:09](https://www.dailymotion.com/video/x5pbur7?t=9) | niebla difusa sin sombra dura | #6C6C7D 15% · #C5C8D6 15% · #848597 13% (grises azulados) · saturación 18%, brillo 53% |
| Combate en tormenta de nieve, blanco casi total | Ragnarok Trailer, [0:19](https://www.dailymotion.com/video/x5pbur7?t=19) | ventisca, luz plana fría | #9CAABA 15% · #D3DAE4 15% · #B8C3D0 14% · azul marino #101929 12% · saturación 24%, brillo 64% |
| Relámpago azul bajo lluvia (Hela Trailer) | Hela Trailer, Dailymotion, [0:38](https://www.dailymotion.com/video/x5rr6d4?t=38) | noche cerrada, sólo el rayo ilumina | #091018 25% · #111823 22% · #19202E 22% (casi negro azulado) · saturación 53% pese a brillo 13% (azul eléctrico muy puro) |
| Colina con niebla, Hela de perfil con tocado y piel de animal | Hellblade 1 tráiler, Dailymotion, [0:07](https://www.dailymotion.com/video/x5v5lz0?t=7) | niebla blanca uniforme, sin horizonte | #AFA5BE 22% · #746B82 16% · negro #27272B 14% · saturación 16%, brillo 46% |
| Silueta de Senua caminando hacia la luz, fin del tráiler | Hellblade 1 tráiler, Dailymotion, [1:45](https://www.dailymotion.com/video/x5v5lz0?t=105) | contraluz total, fuego pequeño a la izquierda | negro #030206 25% → blanco casi puro #F7F9F0 12% (contraste extremo) |
| Costa con niebla y oleaje (Orkney/Islandia), Senua de espaldas | Hellblade II Game Awards Trailer, Dailymotion, [0:07](https://www.dailymotion.com/video/x8qciu2?t=7) | niebla marina, sol muy velado | casi monocromo: negro #000000 25% · gris #55554D 12% · beige #D5D6D0 12% · **saturación sólo 7%** (la más desaturada de toda la muestra) |
| Senua escondida tras una empalizada, cielo malva y fuego naranja | Hellblade II Trailer, [0:38](https://www.dailymotion.com/video/x8qciu2?t=38) | anochecer, fuego de acento | negro #000001 34% · violeta #655777 16% · #524867 10% · saturación 32%, brillo 18% |
| Mano corrupta agarrando la cara de Senua | Hellblade II Trailer, [1:46](https://www.dailymotion.com/video/x8qciu2?t=106) | casi sin luz, sólo un borde | negro #000000 27% · #020202 24% · #080608 17% · brillo medio **8%**, la escena más oscura medida |

**Patrón que se repite** (con estos 9 fotogramas medidos): la niebla desatura mucho la paleta (7-26% de saturación) salvo cuando hay fuego o un rayo, que meten un acento cálido o azul eléctrico muy saturado sobre un fondo casi en escala de grises; el brillo cae en picado (8-18%) en las escenas de miedo/persecución y sube (46-74%) en las de naturaleza o revelación.

### Texturas reales equivalentes (CC0, ambientcg.com)
- Roca volcánica / terreno irregular: **Rock064**, **Rock063**, **Rock058** · CC0 · https://ambientcg.com/view?id=Rock064 (equivalente a los acantilados de Reykjanestá) ⚠️ (comparación visual propia, no del estudio)
- Suelo/musgo de tierras altas: **Ground111**, **Ground068** · CC0 · https://ambientcg.com/view?id=Ground111
- Ninja Theory usó **Quixel Megascans** (mismo tipo de librería fotogramétrica) para las rocas islandesas reales, así que estas texturas CC0 son del mismo tipo de fuente, no una copia exacta ⚠️

---

<a name="punto-9"></a>
## Punto 9 — Música y sonido

### Compositores (uno por juego, casi nunca se cita a los dos)
- **Hellblade: Senua's Sacrifice (2017):** compositor principal **Andy LaPlegua** (de la banda industrial Combichrist), anunciado el 24-feb-2015; ya había compuesto toda la banda sonora de *DmC: Devil May Cry* (con Ninja Theory) con temas como «Never Surrender» y «Throat Full of Glass» · MCV/Develop ✅ (y lo repite Wikipedia) · https://mcvuk.com/development-news/combichrists-andy-laplegua-composing-hellblade-soundtrack/
- Cita del director creativo **Tameem Antoniades** sobre el fichaje: «sabía que Andy podía hacer la música de batalla vikinga, pero no estaba seguro de los demás estilos. Pensé que tenía sentido confiar en su talento musical y ver qué podía hacer» · MCV/Develop ✅
- El álbum del OST publicado en MusicBrainz (2018-12-04) acredita a **David García Díaz** (director de audio de Ninja Theory) como compositor principal — probablemente el crédito de estudio junto a LaPlegua y otros colaboradores externos: el tema del jefe final es **«Hela»**, de David García Díaz y **Passarella Death Squad** (4:16) y también se cita **«Just Like Sleep»** de Passarella Death Squad como tema del combate final · Spotify/Shazam + YouTube ✅ · https://open.spotify.com/track/1UaYT2vE5plDKPD8kKOVGQ
- **Canción de los créditos finales de Hellblade 1:** «**Illusion**», de **VNV Nation** (álbum *Judgement*, 2007) — confirmado en el propio archivo de Internet Archive del audio de créditos y repetido en varios vídeos de YouTube con el mismo nombre ✅ · https://archive.org/details/HellbladeSenuasSacrificeEndingSongIllusionByVnvNation
- **Senua's Saga: Hellblade II (2024):** compositor/director de audio principal, de nuevo **David García Díaz**; el equipo de sonido añade créditos propios de tema: **Matteo Tummino** («Sacrifices Must Have Meaning») y **Jamie Molloy** («Ingunn»), ambos Senior Sound Designer · LinkedIn de Tummino + tiendas de streaming (Amazon Music, Deezer, KKBOX) ✅
- **Heilung** (banda experimental germano-danesa-noruega: **Kai Uwe Faust** voz, **Christopher Juul** producción, **Maria Franz** voz) puso música al tráiler y a parte de la banda sonora de Hellblade II; el tema **«In Maidjan»** («corromper», de su disco *Ofnir*) sonó en el tráiler de anuncio de **TGA 2019** (13-dic-2019) · Louder Sound, GamesRadar, Wikipedia (Heilung) ✅ · https://www.loudersound.com/news/heilung-join-forces-with-ninja-theory-for-hellblade-ii
- El tráiler de **TGA (Xbox Game Pass, "2024")** que se miró fotograma a fotograma en el punto 2 usa, según el título de su subida a YouTube, el tema **«Seidh»** de Heilung ⚠️ (una sola fuente, título de vídeo, no artículo) · https://www.youtube.com/watch?v=85uI1LA5lcc

### Sonido binaural (el rasgo sonoro de la saga)
- Hellblade usa **grabación binaural** (dos micrófonos que imitan la forma del oído) para que las voces de la cabeza de Senua («las Furias») suenen con posición 3D real: pasan de un hombro al otro, se acercan por detrás, avisan de un enemigo fuera de cámara · Forbes, PCGamesN, Steam (aviso oficial de jugar con auriculares) ✅ · https://www.forbes.com/sites/davidthier/2017/08/10/dont-play-hellbalde-senuas-sacrifice-without-headphones/
- El equipo habló con personas reales con alucinaciones auditivas verbales para dar **personalidades distintas** a cada voz (una anima, otra insulta, otra avisa del peligro) · PCGamesN + reseña «The Incredibly Sound Storytelling…» (Medium) ✅
- Un reseñista describe texturas concretas del audio de las Furias como sonidos «de boca, aireados: sh, tsuk, tishk» ⚠️ (una sola fuente, blog) · https://medium.com/channel-cousin/the-incredibly-sound-storytelling-of-hellblade-senuas-sacrifice-533c6b9a7f29
- **Equipo de audio de Hellblade II** (GDC 2025 + A Sound Effect): director de audio **David García Díaz**; diseñador de sonido líder **Daniele Galante** (charla GDC 2025 «The Voices of Senua's Saga: Hellblade II: From Binaural Recording to Creative Manipulation»); también **Alessio Mellina**, **Pablo Cañas Llorente**, **Matteo Tummino**, **Jordan Payne**, **Jamie Molloy** · GDC schedule + asoundeffect.com ✅ · https://schedule.gdconf.com/session/the-voices-of-senuas-saga-hellblade-ii-from-binaural-recording-to-creative-manipulation/907004 · https://www.asoundeffect.com/senuas-saga-hellblade-ii-game-audio/
- Voces de las Furias en HB2 grabadas por las intérpretes **Abbi** y **Helen** (binaural, improvisado); **Ren** y **Arunka** aportan canto de garganta y texturas vocales; **The Monster Factory** puso las voces extremas (metal) para los momentos más oscuros; Galante: las voces están «rotas, deformadas, casi irreconocibles», reflejando síntomas reales; palabras clave como «fracaso» o «culpa» disparan distorsiones concretas ⚠️ (una sola fuente detallada, especializada) · asoundeffect.com
- Herramientas técnicas citadas por el equipo de HB2: middleware **Wwise**, **Project Acoustics** (Microsoft), auriculares de mezcla **Neumann NDH20/NDH30**, plugin binaural **dearVR**, **Sound Particles**, **Ableton Live** ⚠️ (misma fuente) · asoundeffect.com

### Psicosis: consultor y por qué suena así
- Ambos juegos se hicieron con el neurocientífico **Paul Fletcher** (Universidad de Cambridge, cátedra Bernard Wolfe de Neurociencia de la Salud), financiado en parte por el **Wellcome Trust**; en Hellblade II trabajaron además con el **RCE Wellbeing Hub** (Recovery College East) y personas con experiencia real de psicosis · Cambridge Independent + Xbox Wire + Safe In Our World ✅ · https://www.cambridgeindependent.co.uk/business/how-cambridge-game-developer-worked-with-addenbrooke-s-psych-9245228/ · https://news.xbox.com/en-us/2024/05/10/senuas-psychosis-hellblade-2-mental-health-feature/
- Ese trabajo con Fletcher ganó el premio a **Mejor Logro Técnico** en los BAFTA Games Awards 2025 · cambridgebrc.nihr.ac.uk ✅

### Efectos y «onomatopeyas» reconocibles
- El **susurro binaural constante** de las Furias (sh, tsuk, tishk) es el sonido más asociado al juego, hasta el punto de que Steam avisa: mejor jugar con auriculares · Steam Community, Forbes ✅
- El **grito/graznido de cuervo** ligado a Valravn (el cuervo-hombre) marca sus apariciones — visto en los fotogramas del punto 2 (cuervo en el tráiler HB1, 0:06) ⚠️ (deducido de las hojas, falta una fuente textual que lo confirme como «onomatopeya reconocida»)
- El sonido de la **Podredumbre (Dark Rot)** avanzando por el brazo de Senua acompaña la mecánica de falso permadeath (ver punto 10) ⚠️

---

<a name="punto-10"></a>
## Punto 10 — Vídeos: tráileres, escenas, análisis, tendencias

### Catálogo de tráileres oficiales (Steam, sin login; confirmado con `appdetails` API)
_Fuente: https://store.steampowered.com/api/appdetails?appids=414340 y …?appids=2461850 ✅_

**Hellblade: Senua's Sacrifice (appid 414340):**
- «Official Trailer» (2:01) — https://store.steampowered.com/app/414340 · analizado fotograma a fotograma en el punto 2
- «Ragnarok Trailer» — mismo appid, id 256686495
- «Accolades Trailer» (4:49 según Dailymotion) — premios y reseñas con nota, id 256697675; copia en Dailymotion: https://www.dailymotion.com/video/x89mj97
- «Enhanced for PC» (versión 2021 con ray tracing y DLSS/FSR) — id 256859910

**Senua's Saga: Hellblade II (appid 2461850):**
- «Official Trailer» (2:34, el del hashtag #TheGameAwards) — analizado en el punto 2 y en `partes/episodios.md` (ficha minuto a minuto) · https://www.dailymotion.com/video/x8qciu2
- «Hellblade II: Senua's Saga Enhanced release trailer» — id 257181429, publicado tras el lanzamiento (parche «Enhanced»)
- Tráiler de anuncio en **The Game Awards 2019** (13-dic-2019): usó la canción **«In Maidjan»** de Heilung, la presentación reveló por primera vez el nombre «Senua's Saga: Hellblade II» · YouTube (copia oficial de Xbox): https://www.youtube.com/watch?v=2TR0gaG01do ⚠️ (no se pudo bajar de este servidor por el bloqueo de sesión de YouTube; el dato de la canción sí está en dos fuentes: Louder Sound y GamesRadar)

### Vídeo de making-of visto (fotograma a fotograma, `fotogramas.py --cortes`)
- El clip subido a Dailymotion como «Trailer Ragnarok» (`x5pbur7`, 1:10, Gameblog) **no es sólo el tráiler cinemático**: a partir del segundo 0:20 alterna con un **vídeo de making-of** («Development Diary») donde aparece **Dominic Matthews** (rotulado «Product Development Ninja» en pantalla) hablando a cámara, una reunión de equipo, un artista dibujando a Senua en una tableta Wacom y una sesión de **captura de movimiento** con el traje de marcadores en un estudio con luces de colores — visto en directo con `fotogramas.py --cortes`, hoja en `/tmp/claude-0/trabajo/118-hellblade-video/ragnarok_trailer/hoja_01.jpg`, minutos [0:32](https://www.dailymotion.com/video/x5pbur7?t=32), [0:38](https://www.dailymotion.com/video/x5pbur7?t=38), [0:58-0:59](https://www.dailymotion.com/video/x5pbur7?t=58) ✅ (visto directamente) — dato para el investigador de texto/técnica (punto 18), aquí sólo se deja anotado
- Existe además un documental corto **«Hellblade - Development Diary: The Music»** en YouTube, específico de la banda sonora ⚠️ (título confirmado por búsqueda, no se pudo descargar por el bloqueo de YouTube) · https://www.youtube.com/watch?v=AY7rg3AbapA

### Análisis
- La charla de GDC 2025 **«The Voices of Senua's Saga: Hellblade II: From Binaural Recording to Creative Manipulation»** de Daniele Galante es el análisis técnico más profundo del sonido de HB2 (ver punto 9); la ficha pública del calendario de GDC confirma ponente y título, el vídeo completo está en el **GDC Vault** (de pago) ⚠️ · https://schedule.gdconf.com/session/the-voices-of-senuas-saga-hellblade-ii-from-binaural-recording-to-creative-manipulation/907004
- Xbox Wire publicó dos reportajes en vídeo/texto con el equipo de desarrollo sobre los entornos («The Wanderers») y la psicosis («How Senua's Experience of Psychosis…»), citados en los puntos 4 y 9 ✅

### Tendencias (con minuto donde lo hay)
- **La polémica del «permadeath»** (2017): el juego avisa de que si la Podredumbre llega a la cabeza de Senua se pierde toda la partida; se hizo viral en YouTube/Twitter/Reddit porque mucha gente dejó de jugar por miedo — luego se demostró que es un **farol**: la Podredumbre nunca pasa del hombro (probado muriendo más de 50 veces) · Digital Trends, KitGuru, PCGamesN, ComicBook.com ✅ (cuatro fuentes coincidentes)
- **Heilung + videojuegos**: la prensa de música extrema (Louder/Metal Hammer) cubrió el tráiler de HB2 como noticia propia («espera, la música del tráiler de Hellblade 2 es de una banda real») — cruce poco común entre el fandom del *folk/pagan metal* y el de los videojuegos, interesante para un servidor de doblaje/canto · GamesRadar, Louder Sound ✅
- Steam avisa expresamente en la propia ficha de la tienda que el juego está pensado para jugarse **con auriculares** por el audio binaural — la recomendación se repite en casi todas las reseñas y vídeos de reacción (Forbes, IGN, GamesRadar) ✅

---

<a name="punto-14"></a>
## Punto 14 — Poses de Senua analizadas

10 fotogramas propios (los 6 primeros en 1920×1080 real del tráiler de Steam, los 4 últimos de
Dailymotion a menor resolución pero con la pose clara), cada uno con minuto y enlace. No es un
personaje que «anime» o «celebre» en los tráileres (el tono es sombrío de principio a fin), así que
para esas dos categorías se apunta la pose más cercana que aparece de verdad.

| # | Fuente y minuto | Postura / manos / mirada / gesto | Sirve para… |
|---|---|---|---|
| 1 | HB1 tráiler Steam, 0:29 | de pie, cuerpo frontal a cámara, brazos fuera de plano, mirada baja y fija al frente, boca cerrada, cejas tensas | **presentar** (retrato icónico, funciona solo como imagen de perfil de personaje) |
| 2 | HB1 tráiler Steam, 1:22 | ambas manos cerradas sobre la empuñadura de una espada larga que brilla en azul, cuerpo de perfil, cabeza ladeada hacia el arma, mirada de reojo hacia el frente | **explicar / mostrar un poder** (objeto en la mano, gesto de revelar) |
| 3 | HB1 tráiler Steam, 1:34 | torso girado en combate, un brazo tensado empujando hacia delante contra un enemigo, la otra mano fuera de plano, mirada fija en el rival | **regañar / enfrentarse** (postura de choque directo) |
| 4 | HB1 tráiler Steam, 1:45 | de pie, brazos sueltos y ligeramente separados del cuerpo, cabeza algo baja, caminando despacio hacia una luz | **pensar / aceptar** (silueta contemplativa, cierre) |
| 5 | HB2 tráiler Steam, 0:10 | de espaldas, una mano sube hacia el pelo/la cabeza como si el viento o la lluvia molestasen, piernas firmes sobre roca, mirada hacia el mar | **explorar / decidir el camino** (equivalente a «animar»: mirar hacia delante con determinación pese al temporal) |
| 6 | HB2 tráiler Steam, 0:52 | camina de espaldas, brazos caídos y manchados de sangre, cabeza inclinada hacia la calavera clavada en la rama | **avanzar con cautela / advertir del peligro** |
| 7 | HB2 tráiler Dailymotion, [0:38](https://www.dailymotion.com/video/x8qciu2?t=38) | agachada tras una empalizada de madera, ojos muy abiertos, boca entreabierta, cabeza asomando apenas | **temer / avisar** (mejor equivalente a «regañar/alertar» en este juego) |
| 8 | HB2 tráiler Dailymotion, [1:46](https://www.dailymotion.com/video/x8qciu2?t=106) | cabeza sujeta por una mano ajena en el rostro, ojos cerrados con fuerza, boca abierta en grito silencioso | **dolor extremo / la Oscuridad tomándola** (no hay categoría del encargo que encaje: es la pose de terror corporal más repetida de la saga) |
| 9 | HB1 tráiler «dev diary», Dailymotion, [0:22](https://www.dailymotion.com/video/x5pbur7?t=22) | primer plano, boca abierta gritando, cejas juntas, pintura facial azul manchada | **regañar / rabia** (grito de furia, la expresión de ira más citada) |
| 10 | HB1 tráiler Steam, ~1:21 (hoja `steam_hb1/hoja_01.jpg`, plano 30) | brazo extendido con la mano abierta hacia una esfera de luz azul flotante, cuerpo inclinado hacia delante, mirada fija en el objeto | **explicar / señalar un objeto de poder** (gesto de alcanzar/mostrar) |

**Patrón de manos:** en las poses de combate y poder (2, 3, 10) Senua siempre tiene al menos una
mano cerrada con fuerza (arma o energía); en las de miedo (7, 8) las manos están fuera de su
control (ajenas o inertes); en las contemplativas (1, 4, 6) los brazos cuelgan sueltos. Útil para la
guía de IA del punto 17: «manos cerradas = determinación/poder, manos sueltas = duelo/aceptación».

---

<a name="lamina"></a>
## Lo mejor para la lámina

_(pendiente)_

---

<a name="no-encontre"></a>
## No encontré

_(pendiente)_

---

<a name="cumplimiento"></a>
## Cumplimiento de mis puntos

_(pendiente)_

---

<a name="bitacora"></a>
## Bitácora de búsqueda

_(pendiente)_
