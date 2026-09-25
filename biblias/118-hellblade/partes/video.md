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

_(pendiente)_

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

_(pendiente)_

---

<a name="punto-14"></a>
## Punto 14 — Poses de Senua analizadas

_(pendiente)_

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
