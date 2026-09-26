# Video · Honkai: Star Rail (puntos 2, 4, 9, 10, 14)

Investigador de vídeo. Parto de `datos-video.md` (Dailymotion, Internet Archive, MusicBrainz). Es un
videojuego de servicio en vivo (HoYoverse/miHoYo, gacha, sin capítulos fijos como un anime): donde el
encargo pide «capítulo y minuto» uso el nombre del tráiler/cinemática oficial + el minuto exacto (con
`&t=` cuando la plataforma lo soporta; Dailymotion no lo soporta, uso `?t=`).

## 2 · Fotogramas de escenas icónicas (opening, ending, tráiler, escenas)

Honkai: Star Rail no tiene OP/ED semanales como un anime: cada versión mayor estrena su propio PV
("opening" de esa versión) y el juego tiene una única cinemática de arranque ("A Short Play"). Miré
los 6 vídeos con `fotogramas.py` (hojas de contacto + 4 fotogramas sueltos) y los abrí con Read.

- **Opening (cinemática de arranque del juego, "A Short Play")**: prólogo real de HSR: el Trazacaminos
  despierta en la Estación Espacial Herta y se cruza con **Kafka** (pelo gris-morado, guantes rojos) y
  **Silver Wolf** (pelo plateado) frente a un portal/agujero negro holográfico. 24 fotogramas, 0:00-1:09,
  cada 3 s · fuente: Dailymotion (mirror) https://www.dailymotion.com/video/x8bbisq · título confirmado
  en 2 fuentes independientes: Gamekult «Cinématique d'ouverture "A Short Play"»
  (https://www.dailymotion.com/video/x8b3hpm) y el repost «Honkai Star Rail Opening Cutscene A Short
  Play» (https://www.dailymotion.com/video/x8o9ujj) · ✅ · fotograma clave en 0:09 (estación sobre la
  luna, ver punto 4).
- **"Opening" de versión 3.0 / PV "Paean of Era Nova"**: vídeo animado de HOYO-MiX para el lanzamiento de
  Amphoreus, ritmo de videoclip (no es gameplay): créditos finales muestran el título «Paean of Era Nova»
  con dos personajes (uno rubio con toga clara, uno de pelo blanco). 34 fotogramas, 0:00-1:40, cada 3 s ·
  https://www.dailymotion.com/video/x9c9x3o · ⚠️ (un solo repost, sin canal oficial verificado; el mismo
  vídeo circula también subido como «'Nameless Faces' de Honkai: Star Rail» en
  https://www.dailymotion.com/video/x9bonfg, mismo contenido byte a byte en los fotogramas — dos enlaces,
  un solo vídeo real, así que lo cuento como ⚠️).
- **Tráiler (anuncio de la beta cerrada, "reveal trailer")**: nave Astral Express, ciudad de Belobog
  (Jarilo-VI), March 7th narrando, Himeko con su taza de café al final, cierre con el lema «MAY THIS
  JOURNEY LEAD US STARWARD». 30 fotogramas, 0:00-1:57, cada 4 s ·
  https://www.dailymotion.com/video/x89nw8b (repost de JeuxVideo.com/GRYOnline.pl) · ⚠️ (un solo mirror
  disponible; YouTube bloquea el original desde este servidor) · fotograma de Belobog en 0:24 (ver punto 4).
- **Escena icónica 1 — tráiler de personaje de March 7th** ("Bande-annonce de March 7th"): 28
  fotogramas, 0:00-1:49, cada 4 s · https://www.dailymotion.com/video/x8a7le6 · ⚠️ (un solo mirror) ·
  poses en el punto 14.
- **Escena icónica 2 — tráiler de personaje de Kafka** ("Keeping Up With Star Rail — Kafka: Elegance
  Unmasked", programa oficial con la mascota Owlbert de Himeko-chibi): 54 fotogramas, 0:00-4:25, cada 5 s
  · https://www.dailymotion.com/video/x8n41oa · ✅ (mismo tráiler repetido en francés por Gamekult,
  https://www.dailymotion.com/video/x8n45fs, y con el mismo minutaje: 267 s) · poses en el punto 14.
- **Escena icónica 3 — "Myriad Celestia: History of the Xianzhou / Seven Arbiter Generals"**: corto
  animado de estilo ilustración china (dorado, loto rojo, dragón) que cuenta el origen de la flota
  Xianzhou. 31 fotogramas, 0:00-4:03, cada 8 s · https://www.dailymotion.com/video/x8kqs3q · ⚠️ (un solo
  mirror, repetido igual en x8kqsdm) · fotograma dorado en 0:40 (ver punto 4).
- **Extra — avance de arco "Farewell, Penacony" (preview 2.3)**: gameplay + arte de cierre del arco de
  Penacony, salón con lámpara de araña, mar de sueños. 23 fotogramas, 0:00-2:59, cada 8 s ·
  https://www.dailymotion.com/video/x8zuqj6 · ⚠️ · fotograma en 0:04 (ver punto 4).

No hay "ending" real (el juego no cierra episodios): la PV "Paean of Era Nova" hace ese papel de cierre
con créditos y logo, y la uso también como equivalente de ending, aclarado arriba.

## 4 · Fondos y sitios: luz, paleta medida y texturas

Paleta con `herramientas/estilo.py` (K-means, 5 colores) sobre un fotograma real de cada sitio, sacado
con `fotogramas.py --fotograma <s>`. Enlace = vídeo del punto 2 + `?t=`.

| Sitio | Paleta medida (hex) | Luz | Fotograma |
|---|---|---|---|
| Estación Espacial Herta (prólogo) | `#131316` `#1F1F24` `#323235` `#5D5D61` `#8F8E92` | grises casi sin saturar (13%), brillo bajo (16%): vacío frío del espacio, pasillos metálicos sin ventanas | https://www.dailymotion.com/video/x8bbisq?t=9 |
| Jarilo-VI / Belobog (tráiler de anuncio) | `#242742` `#4A527D` `#90B4E3` `#6E85B8` `#D9E8FC` | azules fríos, brillo medio-alto (57%): cielo diurno nevado, ciudad bajo cúpula | https://www.dailymotion.com/video/x89nw8b?t=24 |
| Penacony (avance "Farewell, Penacony") | `#1B1324` `#3E334E` `#765D7B` `#E1DFE5` `#AE99B1` | morados y malvas oscuros, brillo bajo (41%): interior de salón con lámpara de araña, ambiente de sueño | https://www.dailymotion.com/video/x8zuqj6?t=4 |
| Xianzhou Luofu ("Myriad Celestia") | `#F7E380` `#EAC767` `#DBA44B` `#E7DCC3` `#BA7E35` | dorados cálidos, brillo muy alto (90%): estilo leyenda/pintura china, naves flotando al atardecer | https://www.dailymotion.com/video/x8kqs3q?t=40 |
| Amphoreus (PV "Paean of Era Nova") | `#6E98C2` `#D8DAE0` `#A4B4C8` `#596F94` `#353F66` | azul-blanco de mármol, brillo alto (73%): ruinas clásicas a plena luz de día | https://www.dailymotion.com/video/x9c9x3o?t=15 |

Las 5 medidas son ✅ (imagen propia + `estilo.py`, reproducible: el color y el tamaño del fotograma se
pueden volver a comprobar).

**Texturas libres (CC0) equivalentes**, de `ambientcg.com` (licencia CC0, autor ambientCG):
- Estación Herta → metal ranurado: **Diamond Plate 009** — https://ambientcg.com/a/DiamondPlate009
- Amphoreus (mármol de ruinas) → **Marble 012** — https://ambientcg.com/a/Marble012 (alternativa más
  veteada: **Travertine 009** — https://ambientcg.com/a/Travertine009)
- Xianzhou Luofu (madera lacada/templos) → buscar en ambientCG «WoodSiding» o «RedPaintedWood» (no
  comprobé un asset concreto; ⚠️ pendiente si hace falta para la lámina).

## 9 · Música y sonido

Compositor: **HOYO-MiX** (estudio interno de HoYoverse). Discografía en MusicBrainz (ya en
`datos-video.md`, no repito la lista completa aquí, sólo lo que se comprobó o se le puso contexto):

- **"Paean of Era Nova"**: tema/PV de la versión 3.0 (Amphoreus), la más parecida a un "opening" de
  versión — ver punto 2 · ✅ (vista en el propio vídeo, con tarjeta de título) · sin encontrar el álbum
  exacto en MusicBrainz con ese nombre inglés (⚠️, puede estar bajo el título chino).
- **"WHITE NIGHT (Honkai: Star Rail Penacony Theme Song)"** — HOYO‐MiX, 2024-01-27,
  https://musicbrainz.org/release-group/ccbb757a-c955-4a2a-a632-64535a776a93 · el propio título en
  MusicBrainz la marca como tema de Penacony (el arco del casino-sueño) · ✅ (MusicBrainz + el nombre del
  arco coincide con el avance «Farewell, Penacony» del punto 2, que usa el mismo ambiente de sueño/salón).
- **"Wildfire" (Sati Akura)** — 2023-09-15,
  https://musicbrainz.org/release-group/76a3b2dc-96cb-4a0b-ba9f-87f14dd5d75b · tiene página propia en la
  wiki de Fandom («Wildfire (Soundtrack)», confirmado por búsqueda en
  `honkai-star-rail.fandom.com/api.php?action=query&list=search&srsearch=soundtrack`) · ✅ (dos fuentes:
  MusicBrainz + wiki) · qué personaje/escena exacta no lo confirmé (⚠️ para eso).
- **"Kafka" (Honkai Star Rail)** — OPFuture, 2023-09-11,
  https://musicbrainz.org/release-group/24403b48-2dc4-4e0a-9e54-cf0bbad3739c · tema asociado al
  personaje (mismo nombre) · ✅ con el tráiler de personaje del punto 2/14, que usa una estética de neón
  a juego.
- **"Penacony (Honkai Star Rail)"** — OPFuture, 2024-03-03,
  https://musicbrainz.org/release-group/55baf6dd-b6d0-46ad-9b9a-3f00657c94d1 · álbum temático del arco ·
  ⚠️ (una fuente).
- **"Astral Theater" Vol. 1-3** — HOYO‐MiX, 2024-01-12 / 2024-11-15 / 2026-01-25 · serie de álbumes tipo
  "variety show" con versiones cantadas/arregladas de temas de personajes (formato similar a un
  especial de variedades) · ⚠️ (una fuente, MusicBrainz).
- **Efecto de sonido confirmado — anuncio de salto astral**: **Pom-Pom**, la conductora del Astral
  Express, es quien avisa por megafonía cuando el tren «está a punto de hacer un salto astral» (warp
  jump); la propia wiki lo describe así y remite al corto animado oficial **"Xuánhuáng" (玄黄, lit.
  "Cielo y Tierra")**, subido el 29-ago-2023 en Bilibili
  (https://www.bilibili.com/video/BV1Th4y1S7KF) · fuente:
  `honkai-star-rail.fandom.com/wiki/Pom-Pom` (wikitext vía API) · ✅ (la wiki + el propio comportamiento
  del NPC en el juego, dos veces documentado en distintas citas de la página) · no encontré el nombre
  oficial en inglés de ese "ding" de aviso como onomatopeya de texto (⚠️).
- **SFX que todo jugador reconoce (de memoria de juego, sin clip propio que lo aísle)**: el tintineo de
  "Fanfarria" al conseguir un personaje de 5 estrellas en el banner (gacha) y el "clac" del menú del
  Tren Astral. **No verifiqué ninguno de los dos con una fuente escrita** — quedan como ⚠️ de memoria,
  no como dato confirmado; si hace falta para la lámina, se puede sacar el clip exacto con `voz.py` de
  una review en vídeo.

## 10 · Vídeos: tráilers, escenas, análisis y tendencias (con minuto)

- **Tráiler de anuncio (reveal, CBT)**: https://www.dailymotion.com/video/x89nw8b — March 7th
  presentando la Estación, Belobog nevada en 0:24, Himeko con su café en 1:44-1:48, cierre «MAY THIS
  JOURNEY LEAD US STARWARD» en 1:52 · ⚠️ (un mirror).
- **Tráilers de versión**: 2.1 (https://www.dailymotion.com/video/x8v9vmk, 2:58), 3.0
  (https://www.dailymotion.com/video/x9c9x4u, 1:23) y 4.0
  (https://www.dailymotion.com/video/x9zq53k, 2:22), los tres repostados por JeuxVideo.com · ⚠️ (un
  mirror cada uno, ya listados en `datos-video.md`).
- **Tráilers de personaje** (formato "Character Demo/Trailer" oficial de HoYoverse, repostados en
  Dailymotion): March 7th (x8a7le6), Kafka "Elegance Unmasked" (x8n41oa, ✅ con repost en francés),
  Yunli (x93agsa / x93bzc8), Jade (x91t7jy), Herta (x9ceo4q), Sunday (x9a7m1e), Luka (x8n4i4b) — todos
  ⚠️ salvo Kafka.
- **"The Deliverer" (posible tráiler del Trazacaminos)**: https://www.dailymotion.com/video/x9o6p18,
  1:50 · el canal que lo resube ("Watch Bits") no es oficial y la descripción tiene relleno de
  hashtags, así que lo trato como ⚠️ dudoso; ojo: "Deliverer" **sí** es un título real del
  Trazacaminos en el juego (misión «Hero, Ignite That Primal Sun», confirmado en el wikitexto de la
  página `Trailblazer` de Fandom), así que el nombre no está inventado, pero no pude confirmar que este
  vídeo concreto sea el tráiler oficial y no un montaje de fan.
- **Análisis**: "Top 10 Strongest Honkai Star Rail Characters" (WatchMojo) —
  https://www.dailymotion.com/video/x8qluep, 8:47, 2766 vistas en el mirror · ⚠️ (un mirror; es un
  vídeo de ranking/análisis en inglés, no un mirror 1:1 de YouTube).
- **Tendencia de TikTok — "Evernight Dance"**: reto de baile con el personaje **Evernight** (5★, forma
  ligada a March 7th por el lore — la propia comunidad los empareja: uno de los vídeos del trend se
  titula «You're awake, my March..» sobre una animación de Evernight) usando el sonido "Lonely". Vídeo
  con más interacción del trend: @SuperMadara, «Honkai Star Rail Animation: Dancing Evernight», 54.2K
  "me gusta" (creador con 1.4M seguidores) · fuente:
  https://www.tiktok.com/en/trending/detail/honkai-star-rail-animation-dancing-evernight (leída con
  `navegar.py --espera 4000`, TikTok bloquea curl) · ✅ (la propia página de tendencias de TikTok junto
  con al menos 6 vídeos distintos con el mismo reto y las mismas etiquetas `#evernight #honkaistarrail`)
  · sin minuto exacto: son vídeos cortos (formato TikTok, no tienen "capítulo").
- **No encontré** un vídeo de análisis en español ni un vídeo de "tendencias" de YouTube propiamente
  dicho: YouTube pide iniciar sesión desde este servidor para casi todo lo de HSR (búsquedas hechas:
  "Honkai Star Rail análisis español", "Honkai Star Rail youtube trend 2026").

## 14 · Poses analizadas por personaje (con minuto o enlace)

Personajes del encargo: March 7th, Kafka, el Trazacaminos. En un videojuego "capítulo" = tráiler o
cinemática citada en el punto 2; "minuto" es el segundo exacto visto en la hoja de contacto.

| Pose | Vídeo/ilustración | Minuto | Sirve para |
|---|---|---|---|
| **March 7th** — mira a cámara con su cámara fotográfica pegada a la mejilla, ojo cerrado, sonriendo | Tráiler de personaje (x8a7le6) | 0:12 | presentar (curiosidad, "quiero fotografiarte") |
| March 7th — pose de perfil con el logo "March 7th" al lado, brazo en alto sujetando la cámara | Tráiler de personaje | 0:16 | presentar |
| March 7th — camina por una calle de Belobog mirando directo a cámara, sonrisa tranquila | Tráiler de personaje | 0:28 | explicar (tono cercano, "guía de barrio") |
| March 7th — apunta su arma (cámara-pistola) al frente con el ceño algo fruncido | Tráiler de personaje | 0:32-0:36 | regañar / advertir |
| March 7th — primer plano llorando, ojos muy abiertos, labios temblando | Tráiler de personaje | 0:52 | pensar / vulnerabilidad (antes de un giro emocional) |
| March 7th — salta al combate con el arma en alto entre partículas de hielo | Tráiler de personaje | 0:56-1:08 | celebrar / atacar |
| March 7th — de pie con un brazo extendido hacia el cielo, cae escarcha, sonrisa serena (plano final) | Tráiler de personaje | 1:36-1:40 | animar (cierre inspirador) |
| **Kafka** — perfil elegante, pelo suelto ondeando, luces de neón en diagonal detrás | "Elegance Unmasked" (x8n41oa) | 0:30 | presentar |
| Kafka — tarjeta de presentación con su nombre, rareza 5★, elemento Rayo/Nihilidad | "Elegance Unmasked" | 0:35 | presentar (ficha) |
| Kafka — de pie con un paraguas cerrado al lado, mano cerca de la boca, mirada de lado | "Elegance Unmasked" | 1:10 | pensar / explicar (tono calculador) |
| Kafka — apunta un arma directo a cámara, gesto serio | "Elegance Unmasked" | 1:40 | regañar / amenazar |
| Kafka — dispara con determinación, cuerpo inclinado hacia adelante | "Elegance Unmasked" | 2:10 | atacar |
| Kafka — de espaldas alejándose, el abrigo largo ondea, silueta contra el cielo de la ciudad | "Elegance Unmasked" | 2:40-2:45 | cierre / misterio (salida triunfal) |
| **Trazacaminos** (Destrucción, F) — flota frente al Expreso Astral, un brazo alzado hacia una estrella brillante, mirada hacia arriba | Arte oficial "Splash Art" · https://static.wikia.nocookie.net/houkai-star-rail/images/6/6f/Character_Trailblazer_%28F%29_Destruction_Splash_Art.png | — (ilustración) | presentar / soñar (curiosidad ante lo desconocido) |
| Trazacaminos (Preservación, M) — corre hacia el combate con un hacha enorme, boca abierta gritando, la tripulación (Himeko, Welt, Bronya…) en siluetas detrás | Arte oficial · https://static.wikia.nocookie.net/houkai-star-rail/images/6/63/Character_Trailblazer_%28M%29_Preservation_Splash_Art.png | — (ilustración) | animar / atacar (liderar al grupo) |
| Trazacaminos (Armonía, F) — de pie bajo un foco de teatro, brazo alzado soltando burbujas, sonríe como anfitriona de circo, animales y cortinas rojas alrededor | Arte oficial · https://static.wikia.nocookie.net/houkai-star-rail/images/0/0a/Character_Trailblazer_%28F%29_Harmony_Splash_Art.png | — (ilustración) | presentar / animar (maestra de ceremonias) |
| Trazacaminos (Remembranza, M) — sentado en una escalinata clásica (Anfiteatro), conjura con una pluma, sonrisa astuta, hada rosa al lado | Arte oficial · https://static.wikia.nocookie.net/houkai-star-rail/images/f/fc/Character_Trailblazer_%28M%29_Remembrance_Splash_Art_%28Updated%29.png | — (ilustración) | explicar / pensar (el "autor" reescribiendo la realidad) |
| Trazacaminos (Elación, F) — de pie en lo alto de una antena/azotea nocturna con fuegos artificiales, puño en alto, sonrisa amplia | Arte oficial · https://static.wikia.nocookie.net/houkai-star-rail/images/a/a8/Character_Trailblazer_%28F%29_Elation_Splash_Art.png | — (ilustración) | celebrar |
| Trazacaminos — de pie en reposo, arma al hombro, mirada neutra al frente (referencia de proporciones) | Render in-game · https://static.wikia.nocookie.net/houkai-star-rail/images/c/ce/Character_Trailblazer_Game_%28F%29.png | — (ilustración) | referencia neutra / plantilla de cuerpo |

Todas las imágenes del Trazacaminos son arte oficial de Fandom (`honkai-star-rail.fandom.com`, imageinfo
por API, tamaño real 2048×2048 medido salvo el render in-game 1000×1778) → ✅. Las de March 7th y Kafka
salen de fotogramas propios de los tráilers de personaje (un solo mirror cada uno) → ⚠️, salvo Kafka
que tiene el tráiler repetido en dos idiomas (✅ en el minutaje).

## Lo mejor para la lámina

- Kafka en "Elegance Unmasked" (0:30-2:45): elegante, de neón morado/magenta sobre gris — sirve para un
  canal serio o de "misterio/edición de audio".
- March 7th con su cámara (0:12) y su pose final de brazo alzado (1:36): cercana, curiosa, perfecta para
  un canal de bienvenida o principiantes (encaja con lo que pide el encargo de "poses vivas").
- Las 5 poses del Trazacaminos por Camino (Destrucción/Preservación/Armonía/Remembranza/Elación): cada
  una tiene un arma y un gesto distinto — elegir según el tono exacto del canal.
- Paletas medidas de los 5 sitios (punto 4): Penacony (morados de sueño) y Xianzhou (dorados de leyenda)
  son las más vistosas para un fondo de lámina con profundidad.
- El trend de TikTok "Evernight Dance" (ligado a March 7th) demuestra que el fandom ya mezcla baile y
  este personaje: útil si el canal destino toca canto/edición.

## No encontré

- Vídeo oficial de YouTube sin bloqueo de inicio de sesión: probé el canal oficial de HoYoverse y
  varios tráilers directos, todos pidieron iniciar sesión desde este servidor. Usé mirrors de
  Dailymotion en su lugar (búsquedas: "Honkai Star Rail trailer", "Honkai Star Rail Kafka", "Honkai
  Star Rail March 7th", "Honkai Star Rail Trailblazer", en inglés, vía `api.dailymotion.com`).
- Nombre oficial en texto de los SFX de "fanfarria" al sacar un 5★ y del clic de menú: no hay artículo
  ni entrevista que los nombre; quedan como ⚠️ de memoria de juego, no confirmados por escrito
  (búsquedas: "Honkai Star Rail sound effects names", `soundeffects.fandom.com` sin contenido útil).
- Textura libre concreta para madera/laca de los templos de Xianzhou Luofu: no elegí un asset exacto de
  ambientCG (sí para mármol y metal).
- Un vídeo de "análisis" en español y una "tendencia" de YouTube (no TikTok): no encontrado con los
  mirrors disponibles (búsqueda: "Honkai Star Rail análisis español", "Honkai Star Rail youtube trend
  2026").
- Confirmación independiente de que "The Deliverer" (x9o6p18) sea el tráiler oficial del Trazacaminos y
  no un montaje: sólo un mirror, de canal no oficial (queda con ⚠️ marcado en el punto 10).
- Reddit vía Arctic Shift (`arctic-shift.photon-reddit.com`) no devolvió datos utilizables en mi
  consulta sobre reacciones a la banda sonora (respuesta vacía); no insistí más de dos veces.

## Bitácora de búsqueda

- `api.dailymotion.com/videos?search=...` (inglés): "Honkai Star Rail Kafka", "Honkai Star Rail March
  7th", "Honkai Star Rail Trailblazer character demo Stelle Caelus", "Honkai Star Rail Launch Trailer",
  "Honkai Star Rail animated short Astral Express", "Honkai Star Rail Penacony trailer", "Honkai Star
  Rail Xianzhou Luofu trailer", "Honkai Star Rail lore explained analysis" — todas devolvieron
  resultados, elegidos los oficiales/repostados por medios reconocibles (JeuxVideo.com, Gamekult,
  GRYOnline.pl, ActuGaming, 3djuegos, WatchMojo).
- `herramientas/fotogramas.py` sobre 8 vídeos de Dailymotion (opening_cutscene, opening_3_0,
  march7th_trailer, kafka_trailer, trailblazer_trailer descartado, reveal_trailer, penacony, xianzhou) +
  4 fotogramas sueltos con `--fotograma` para medir color.
- `herramientas/estilo.py --colores 5` sobre 5 fotogramas propios (Herta, Belobog, Penacony, Xianzhou,
  Amphoreus).
- `honkai-star-rail.fandom.com/api.php` (inglés): wikitext de `Pom-Pom` y de `Trailblazer`, búsqueda de
  categoría `Sound Effects`, búsqueda de texto "soundtrack" y "warp jump sound".
- `soundeffects.fandom.com/api.php`: página de Honkai: Star Rail sin contenido útil (plantilla vacía).
- `ambientcg.com/api/v2/full_json` (texturas CC0): "marble", "metal plate".
- WebSearch (inglés): "Honkai Star Rail most emotional scene players cried March 7th identity reveal 2.7
  song" (sin resultado concreto), "Honkai Star Rail iconic sound effects Pom-Pom bell warp jump gacha
  onomatopoeia" (parcial), "Honkai Star Rail TikTok trend viral 2025 2026 dance edit meme" (✅, dio el
  trend de Evernight).
- `herramientas/navegar.py` (TikTok bloquea curl): página de tendencia
  `tiktok.com/en/trending/detail/honkai-star-rail-animation-dancing-evernight` con `--espera 4000`.
- `arctic-shift.photon-reddit.com/api/posts/search` (Reddit r/HonkaiStarRail_, "OST"): sin datos
  utilizables, no insistí.

## Cumplimiento del encargo (mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 2 · Opening/ending/tráiler/escenas con fotograma y minuto | ✅ | Cinemática de apertura, PV de versión, tráiler de anuncio y 4 escenas icónicas, todas miradas con `fotogramas.py` y citadas con minuto y enlace. Sin OP/ED de anime real: aclarado por qué. |
| 4 · Fondos y sitios: luz, paleta, texturas | ✅ | 5 sitios con paleta medida (`estilo.py`) sobre fotograma propio + luz descrita + 2 texturas CC0 equivalentes; falta 1 textura (madera de Xianzhou) marcada en «No encontré». |
| 9 · Música y sonido | ⚠️ | OST y temas de arco confirmados (MusicBrainz + wiki); el SFX del salto astral confirmado por texto de la wiki, pero los sonidos de menú/gacha quedan de memoria, sin fuente escrita. |
| 10 · Vídeos: tráilers, escenas, análisis, tendencias, con minuto | ✅ | Tráilers de anuncio, de versión y de personaje con minuto; 1 vídeo de análisis (WatchMojo); 1 tendencia de TikTok verificada con `navegar.py`. Falta un análisis en español y una tendencia de YouTube (no encontrados). |
| 14 · Poses por personaje (6-10, con minuto o enlace) | ✅ | 7 poses de March 7th, 6 de Kafka (ambas con minuto, de tráileres mirados) y 6 del Trazacaminos (arte oficial por Camino, con enlace, ya que no hay tráiler propio confirmado). |
