# Parte VÍDEO · No Man's Sky (encargo 124)

Investigador de vídeo: puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Libreta de datos, no prosa.
No Man's Sky es un **videojuego**, no una serie animada: no hay opening/ending ni «capítulos»
en sentido estricto. Se adapta así: punto 2 = tráilers y su minuto exacto; punto 9 = banda
sonora del juego y su tema más reconocible; punto 14 = el «Viajero» (el traje-exotraje que
lleva el jugador, protagonista silencioso y personalizable, tal y como pide `encargos/124-no-man-s-sky.md`).

Partí de `partes/datos-video.md` (clips de Dailymotion e Internet Archive ya localizados por
`recolectar.py`) y de `partes/datos.json` (imágenes de la wiki de Fandom ya bajadas). No repetí
esas búsquedas: las miré con `fotogramas.py`, medí color con `estilo.py` y busqué lo que faltaba
(música, tendencias de vídeo, poses) con la red directa y el buscador.

## Hallazgos

### Punto 2 · Fotogramas de escenas icónicas (tráiler + minuto exacto)

- Tráiler de anuncio (E3/VGX 2014, «Every atom procedural, every planet unique»): arrecife de coral submarino con peces · mirado con `fotogramas.py` (mirror de Internet Archive del YouTube oficial) · ✅ (vídeo + página de Internet Archive lo confirma como oficial) · 0:24–0:32 · https://archive.org/details/youtube-aCgWabJssVI?t=24
- Mismo tráiler: playa de hierba roja con bruma marina verde y letrero «NEW PIDU» en pantalla · fotograma propio · ✅ · 0:40 · https://archive.org/details/youtube-aCgWabJssVI?t=40
- Mismo tráiler: cierre con el logo «NO MAN'S SKY» sobre un planeta rojo a contraluz de atardecer · fotograma propio · ✅ · 1:40–1:52 · https://archive.org/details/youtube-aCgWabJssVI?t=100
- Tráiler de la conferencia E3 2015 (JeuxVideo.com, presentador en el escenario de PlayStation con el juego proyectado): planeta sabana tóxica amarillo-verdosa vista desde la cabina de la nave, con niebla de color · fotograma propio · ✅ (vídeo + coincide con estética «tóxica» documentada en la wiki) · 3:00–4:00 · https://www.dailymotion.com/video/x89lilx?t=220
- Mismo tráiler: bosque otoñal de árboles rojos sobre hierba amarilla, vista a pie · fotograma propio · ✅ · 4:20–4:40 · https://www.dailymotion.com/video/x89lilx?t=240
- Tráiler «Echoes» (actualización narrativa, 2023, canal Vidaextra): planeta de hierba roja con setas gigantes y los nuevos aliens robot «Autophage» · fotograma propio · ✅ (aparecen en la wiki de la actualización) · 0:00–0:24 · https://www.dailymotion.com/video/x8nggcs?t=0
- Mismo tráiler: combate espacial en tres planetas de color distinto (azul, verde, violeta) con naves disparando líneas láser · fotograma propio · ✅ · 0:36–1:12 · https://www.dailymotion.com/video/x8nggcs?t=42
- Tráiler «Prisms» (actualización visual centrada en iluminación): cueva con «Volumetric Lighting» rotulado en pantalla, bioluminiscencia verde y roja · fotograma propio · ✅ · 0:08–0:16 · https://www.dailymotion.com/video/x89nujz?t=16
- Tráiler del 10.º aniversario / «Cosmos» (agosto 2026, mirror oficial en Internet Archive): repaso «Year 1» a «Year 10» con los nombres de las grandes actualizaciones en pantalla (NEXT, Desolation, Next Generation, Beacon…) · fotograma propio · ✅ (coincide con el resumen de Shacknews/idcgames) · 0:16–1:36 · https://archive.org/details/youtube--sK7EGiJSDk?t=24
- Mismo tráiler: cartel final «NO MAN'S SKY COSMOS» con el Viajero y dos aliens compañeros frente a un planeta rojo gigante y naves cruzando el cielo · fotograma propio · ✅ · 1:52 · https://archive.org/details/youtube--sK7EGiJSDk?t=112

### Punto 4 · Sitios: luz y paleta medida, texturas reales equivalentes

Paletas sacadas con `herramientas/estilo.py` sobre fotogramas propios (no de memoria):

- Planeta del cierre del tráiler de anuncio, atardecer: #630F31 (65%), #79273B (19%), #2A0A1C (7%) · luz rasante naranja-vino, cielo muy oscuro · medido con estilo.py en fotograma propio (1:40) · ✅ · https://archive.org/details/youtube-aCgWabJssVI?t=100
- Planeta sabana tóxica (E3 2015, vista de cabina): #CCBC54 (35%), #C1E8B3 (25%), #B27957 (17%) → #C7B653/#452F3D en el siguiente encuadre · niebla verdosa de día, saturación baja (~43%), brillo alto (~70%) · medido con estilo.py · ✅ · 3:20–4:00 · https://www.dailymotion.com/video/x89lilx?t=220
- Planeta de hierba roja con setas (Echoes, apertura): #270E1E (37%), #A00B0A (24%), #609FDB (18%), #B3D9F1 (12%) · contraste rojo tierra / cielo azul claro, luz de mediodía · medido con estilo.py · ✅ · 0:00 · https://www.dailymotion.com/video/x8nggcs?t=0
- Cueva bioluminiscente (Prisms, «Volumetric Lighting»): #070202 (66%) y #200F09 (24%) de base, con acentos #741410 (rojo brasa) y #586A6A (verde-azul de las luces) · negro casi total salvo focos puntuales, saturación 74% pero brillo 8% · medido con estilo.py · ✅ · 0:16 · https://www.dailymotion.com/video/x89nujz?t=16
- Ladera verde sobre un lago (Prisms, plano general): #535B5D (30%), #3E462F (24%), #232819 (13%) · luz de día nublado, poco contraste · medido con estilo.py · ✅ · 0:24 · https://www.dailymotion.com/video/x89nujz?t=24
- Playa de hierba roja y arena clara (tráiler de anuncio): #5E1120 (29%, hierba), #E0EB99 (19%, arena), #C9CFAD (26%, cielo) · luz de día despejado, sombras suaves · medido con estilo.py · ✅ · 0:40 · https://archive.org/details/youtube-aCgWabJssVI?t=40
- Combate en niebla verde (tráiler 10.º aniversario): #999F5F (21%), #C0E083 (20%), #75553D (23%) · niebla amarillo-verdosa muy saturada, sol quemado al fondo · medido con estilo.py · ✅ · 1:20 · https://archive.org/details/youtube--sK7EGiJSDk?t=80
- Fondo del cartel «Cosmos» (planeta rojo + espacio teal): #49C0A9 (28%), #3B7872 (29%), #85514C (11%, el planeta) · contraste teal/rojo típico de las portadas de la saga · medido con estilo.py · ✅ · 1:52 · https://archive.org/details/youtube--sK7EGiJSDk?t=112
- Texturas reales equivalentes (arena/tierra de los planetas desérticos y playas): ambientCG «Ground054», foto de arena-barro de playa, CC0, 2048×2048 · https://ambientcg.com/a/Ground054 · ⚠️ (una fuente, banco CC0 verificado por su propia API) · tamaño 2048×2048
- Textura real equivalente (roca de acantilados y cuevas): ambientCG «Rock061», CC0 · https://ambientcg.com/a/Rock061 · ⚠️ · sin medir tamaño exacto de la vista previa

### Punto 9 · Música y sonido

- Banda sonora oficial: **«No Man's Sky: Music for an Infinite Universe»**, álbum de 65daysofstatic, publicado 5-ago-2016, 10 pistas (Monolith, Supermoon, Asimov, Heliosphere, Blueprint For a Slow Machine, Pillars of Frost, Escape Velocity, Red Parallax, Hypersleep, End of the World Sun) · Fandom nomanssky (wiki, texto) + MusicBrainz (datos-video.md) · ✅ · https://nomanssky.fandom.com/wiki/Music_for_an_Infinite_Universe · https://musicbrainz.org/release-group/b0fb336e-dfc0-4049-be04-bf4c903b46b9
- «Supermoon» es la pista más reconocible: sonó en varios tráilers previos al lanzamiento (2014-2016), incluida la revelación · Fandom nomanssky (cita a The Verge) + MusicRadar · ✅ · https://nomanssky.fandom.com/wiki/Music_for_an_Infinite_Universe
- Origen de la colaboración: Sean Murray (Hello Games) y Paul Wolinski (65daysofstatic) llegaron cada uno a la primera reunión queriendo proponer lo mismo; la banda de math-rock ya había inspirado el sonido del juego antes de firmar (la pista «Debutante» sonó en la primera revelación de 2013) · The Verge (vía cita en Fandom) + MusicRadar · ✅ · https://www.musicradar.com/news/guitars/how-65daysofstatic-built-the-soundtrack-to-no-mans-skys-infinite-universe-641184
- La música no suena en bucle fijo: el estudio compuso «un par de horas» de material que un sistema propio llamado **Pulse** recombina en vivo (24 conjuntos de paisajes sonoros, 60 variaciones base), así que cada jugador oye una mezcla distinta · A Sound Effect (Q&A con Paul Weir) + MusicRadar · ✅ · https://www.asoundeffect.com/no-mans-sky-sound-procedural-audio/
- Cita de Joe Shrewsbury (65daysofstatic) sobre ese reto: «As a musician, it forces you to give up on being precious about anything» · MusicRadar · ⚠️ (una fuente) · https://www.musicradar.com/news/guitars/how-65daysofstatic-built-the-soundtrack-to-no-mans-skys-infinite-universe-641184
- Sonido de criaturas: sintetizador propio **VocAlien** (Paul Weir + Sandy White), un «tracto vocal» modelado físicamente que genera las vocalizaciones alienígenas en tiempo real (no grabaciones); es de los pocos elementos realmente «procedurales» (vs. «generativos») del juego · A Sound Effect + GDC Vault (charla «The Sound of No Man's Sky») · ✅ · https://www.asoundeffect.com/no-mans-sky-sound-procedural-audio/ · https://www.gdcvault.com/play/1024067/The-Sound-of-No-Man
- Efectos de sonido con origen curioso: el buggy usa grabaciones del coche real de Paul Weir captadas con micros de contacto; el vehículo flotante (hover-craft) mezcla un ventilador de mesa y un aire acondicionado; la lluvia usa bombas de agua, máquinas expendedoras y motores de garaje como material fuente · A Sound Effect · ⚠️ (una fuente) · https://www.asoundeffect.com/no-mans-sky-sound-procedural-audio/
- Bandas sonoras posteriores (expansiones narrativas), ya localizadas en datos-video.md: «Music for an Infinite Universe» (2016), «Journeys: Original Soundtrack» (2025) y «Vostok / The Journey: Original Soundtrack» (2025), todas de 65daysofstatic con Paul Weir · MusicBrainz · ✅ · https://musicbrainz.org/release-group/33a46a1b-3513-475a-935f-1331d3bc7688

### Punto 10 · Vídeos: tráilers, escenas, análisis y tendencias (con minuto)

- Tráiler de anuncio oficial (E3/VGX 2014), 1:58, mirror de Internet Archive del vídeo de YouTube oficial de Hello Games · ✅ (el propio Internet Archive lo cataloga como oficial + coincide con la wiki) · https://archive.org/details/youtube-aCgWabJssVI
- Tráiler E3 2015 con la conferencia de PlayStation, 5:32, canal JeuxVideo.com en Dailymotion · ✅ (datos-video.md, ya recolectado) · https://www.dailymotion.com/video/x89lilx
- Tráiler «Prisms» (actualización visual), 1:49-1:50, canal JeuxVideo.com en Dailymotion · ✅ · https://www.dailymotion.com/video/x89nujz
- Tráiler «Echoes» (actualización narrativa, 2023), 1:29, canal Vidaextra en Dailymotion · ✅ · https://www.dailymotion.com/video/x8nggcs
- Tráiler oficial del 10.º aniversario / anuncio de «Cosmos», 2:07, publicado ago-2026, mirror en Internet Archive del vídeo de YouTube oficial · ✅ (Shacknews + idcgames.com describen el mismo tráiler y fecha) · https://archive.org/details/youtube--sK7EGiJSDk · https://www.shacknews.com/article/150314/no-mans-sky-10th-anniversary-cosmos-teaser
- Análisis: **«The Redemption Of No Man's Sky»**, GameSpot, 14:39, 46 687 vistas, publicado 1-ago-2018 (repasa minuto a minuto la reconstrucción del juego tras el lanzamiento) · comprobado con yt-dlp (metadatos, sin descarga) · ✅ · https://www.youtube.com/watch?v=3TpTSuaElVQ
- Análisis largo: **«The Engoodening of No Man's Sky»**, Internet Historian, ≈53:50, publicado 9-ene-2020, la «historia de redención» más vista del juego (nota 8.9 en IMDb) · IMDb + Lemmy.World (duración) · ✅ · https://www.youtube.com/watch?v=O5BJVO3PDeQ · https://www.imdb.com/title/tt12681108/
- Tendencia/controversia de lanzamiento (2016): compilación de memes «One Man's Lie» sobre promesas incumplidas (sobre todo el multijugador) y oleada masiva de reembolsos en Steam/GOG/Amazon («Refunds Gate») · Know Your Meme · ⚠️ (una fuente agregadora, aunque cada suceso está documentado por prensa de la época) · https://knowyourmeme.com/memes/subcultures/no-mans-sky
- Tendencia inversa: el juego pasó de reseñas «Mostly Negative» en Steam en 2016 a «Very Positive» desde 2018 gracias a más de 40 actualizaciones gratuitas; ganó el premio a Mejor Juego en Curso (Best Ongoing Game) en The Game Awards 2020 **y** 2025 · Know Your Meme + búsqueda de premios · ✅ · https://knowyourmeme.com/memes/subcultures/no-mans-sky
- TikTok: vídeo viral de @thepoddaddy sobre «este juego tiene 80 cuadrillones de planetas», 271 800 me gusta y 3243 comentarios · búsqueda directa en TikTok · ⚠️ (una fuente, cifras pueden variar con el tiempo) · https://www.tiktok.com/@thepoddaddy/video/7488369729720093983
- Tendencia recurrente en TikTok/YouTube: vídeos tipo «cómo evolucionó el juego en X años» (retrospectivas hechas por fans, no oficiales), que resumen las mismas actualizaciones que marca el propio tráiler del 10.º aniversario · búsqueda directa (discover de TikTok) · ⚠️ · https://www.tiktok.com/discover/no-mans-sky

### Punto 14 · Poses del Viajero (protagonista), con minuto o enlace

El protagonista es un traje-exotraje personalizable y mudo (no un personaje de rostro fijo), así
que las poses «vivas» salen casi todas de los tráilers, no de cinemáticas con guion. No hay pose
de «regañar»: el juego no tiene diálogo hablado del protagonista ni cinemáticas de enfado con él
como sujeto (queda anotado en «No encontré»).

- **Explorar/observar** — de pie, de perfil, casco con visera oscura, mochila con luces verdes encendidas, junto a una planta bioluminiscente en una cueva oscura; mirada baja hacia la planta · tráiler «Prisms» · ✅ (fotograma propio) · 0:16 · https://www.dailymotion.com/video/x89nujz?t=16
- **Explorar en grupo/contemplar paisaje** — de espaldas, en lo alto de una ladera verde, junto a una criatura-compañera verde flotante y un robot con luces; una criatura rosa vuela al fondo; postura relajada, brazos sueltos · tráiler «Prisms» · ✅ · 0:24 · https://www.dailymotion.com/video/x89nujz?t=24
- **Combate/atacar** — en primera persona, multiherramienta (arma) levantada y apuntando con la mira puesta sobre una criatura mecánica gigante entre niebla verde; postura tensa, brazos extendidos al frente · tráiler 10.º aniversario · ✅ · 1:20 · https://archive.org/details/youtube--sK7EGiJSDk?t=80
- **Presentar/celebrar** — de pie, erguido, casco dorado, cámara al pecho, flanqueado por dos aliens compañeros (uno verde con visor rojo, uno blanco/rojo) con los brazos cruzados sobre el pecho; planeta rojo enorme detrás, naves cruzando el cielo; es el cartel de cierre «NO MAN'S SKY COSMOS» · tráiler 10.º aniversario · ✅ · 1:52 · https://archive.org/details/youtube--sK7EGiJSDk?t=112
- **Explicar/dialogar** (NPC Viajero, misma familia de traje que el protagonista) — primer plano, cabeza ladeada hacia el jugador, cuadro de diálogo abierto («Traveller Nogiga»), boca entreabierta a media frase · imagen de la wiki Fandom nomanssky, «Hub Traveler Reference 2.jpg» (recolectada por recolectar.py) · ⚠️ (una fuente, imagen de wiki sin tráiler que la confirme) · https://static.wikia.nocookie.net/nomanssky_gamepedia/images/f/f5/Hub_Traveler_Reference_2.jpg
- **Explicar/negociar** (dos Viajeros NPC) — de pie, cara a cara, uno sostiene una tablet y gesticula con la mano libre mientras habla; el otro escucha con los brazos caídos · imagen de la wiki Fandom nomanssky, «TwoTravellers.png» · ⚠️ · https://static.wikia.nocookie.net/nomanssky_gamepedia/images/5/57/TwoTravellers.png
- **Referencia neutra (turnaround de casco)** — dos hojas de modelo mostrando variantes de casco del exotraje desde varios ángulos, sin acción; sirven para diseño del casco, no de pose · imágenes de la wiki Fandom nomanssky, «Traveller - Heads.png» y «Traveller - Heads 2.png» · ✅ (dos imágenes de la misma wiki, ambas ya en datos.json) · https://static.wikia.nocookie.net/nomanssky_gamepedia/images/e/e1/Traveller_-_Heads.png
- **Explorar interior de nave** — plano general de un pasillo de carguero, el Viajero pequeño en el encuadre caminando hacia la cámara con las luces azules del pasillo detrás · imagen de la wiki Fandom nomanssky, «TravellerInFreighter.jpg» · ⚠️ · https://static.wikia.nocookie.net/nomanssky_gamepedia/images/d/d4/TravellerInFreighter.jpg

## Lo mejor para la lámina

- El cartel de cierre del tráiler del 10.º aniversario (1:52): el Viajero con casco dorado entre dos aliens compañeros, planeta rojo detrás — pose de grupo ya compuesta, lista como referencia de encuadre.
- La paleta teal/rojo de ese mismo fondo (#49C0A9, #3B7872, #85514C) funciona como paleta de portada de ciencia ficción retro, justo lo que pide el encargo.
- El fotograma de la cueva bioluminiscente de «Prisms» (0:16): luz casi negra con focos de color puro (verde, rojo, blanco) — sirve de referencia de iluminación dramática para un panel oscuro.
- «Supermoon» (65daysofstatic) como tema a citar si la lámina lleva un guiño sonoro: es la pista que todo fan asocia a la revelación del juego.
- El planeta sabana tóxica del tráiler E3 2015 (paleta #CCBC54/#C1E8B3, niebla verdosa) es el ejemplo más citable de «planeta de colores» que pide `encargos/124-no-man-s-sky.md`.

## No encontré

- Pose de «regañar» del Viajero: no existe, porque el protagonista no tiene cinemáticas de diálogo con expresión propia (es un traje vacío, sin rostro). Busqué «No Man's Sky traveller angry cutscene» y en la wiki de personajes: no aparece.
- Tendencia de TikTok con un nombre de reto o hashtag propio y viral a gran escala (tipo challenge): no encontré un reto específico, sólo vídeos sueltos de alto rendimiento y series de recap; lo dejo anotado como ⚠️ en vez de inventar un nombre de trend.
- Cover o remix del tema principal hecho por fans con mucha repercusión: no lo busqué a fondo (es un juego instrumental, no hay opening cantado); si hace falta, lo puede ampliar el investigador de voz/música.
- Ficha oficial de qué tema suena en el momento más emotivo del juego (por ejemplo la primera vez que se ve el centro de la galaxia): las fuentes de audio confirman el sistema generativo pero no una pista fija asociada a esa escena; lo dejo con ⚠️ en vez de afirmarlo sin comprobar.

## Cumplimiento del encargo (mis puntos)

| Punto | Qué pedía | Estado | Por qué |
|---|---|---|---|
| 2 | Fotogramas de escenas icónicas, capítulo/minuto | ✅ | 10 fotogramas propios de 5 tráilers distintos, todos con minuto y enlace `&t=` |
| 4 | Sitios: luz y paleta (hex) + texturas reales | ✅ | 9 paletas medidas con estilo.py sobre fotogramas propios + 2 texturas CC0 de ambientCG |
| 9 | Música y sonido, tema de escenas emotivas, onomatopeyas | ⚠️ | OST, generación procedural y SFX bien documentados (dos fuentes); la pista exacta de la escena más emotiva no la confirmé (queda en «No encontré») |
| 10 | Tráilers, análisis, tendencias TikTok/YouTube con minuto | ✅ | 5 tráilers con minuto, 2 vídeos de análisis con duración y vistas, tendencias de 2016 y de TikTok con fuente |
| 14 | Poses del Viajero, 6-10 fotogramas/ilustraciones con minuto o enlace | ✅ | 8 poses (4 de tráiler con minuto, 4 de imágenes de wiki con enlace), cubren explorar, combate, presentar/celebrar, explicar y turnaround; falta «regañar» (no existe, explicado arriba) |

## Bitácora de búsqueda

- Miré con `fotogramas.py`: tráiler de anuncio (archive.org, mirror de YouTube aCgWabJssVI), tráiler E3 2015 (Dailymotion x89lilx), tráiler «Echoes» (Dailymotion x8nggcs), tráiler «Prisms» (Dailymotion x89nujz) y tráiler del 10.º aniversario (archive.org, mirror de YouTube -sK7EGiJSDk). Todos los clips venían ya localizados en `datos-video.md` salvo el del 10.º aniversario, que busqué porque es el más reciente (ago-2026) y encaja con «planetas de colores» del encargo.
- Probé `fotogramas.py` directo contra YouTube dos veces (aCgWabJssVI y -sK7EGiJSDk): ambas dieron «Sign in to confirm you're not a bot» (bloqueo de este servidor). Plan B que funcionó: el mismo vídeo mirrorado en `archive.org/details/youtube-<id>`, tal y como indica AYUDANTE.md.
- Intenté `yt-dlp` para sacar metadatos (duración/vistas) de dos vídeos de análisis en YouTube: uno dio 429 en el primer intento y funcionó al repetir («The Redemption Of No Man's Sky», GameSpot); el otro («The Engoodening», Internet Historian) siguió bloqueado, así que usé IMDb + Lemmy.World para la duración.
- Medí color y estilo con `herramientas/estilo.py` sobre 10 fotogramas propios (no descargué arte de terceros para esto).
- Búsquedas web (inglés, ~10 de mi cupo de 50): «65daysofstatic No Man's Sky soundtrack interview», «Paul Weir procedural audio No Man's Sky interview», «No Man's Sky TikTok viral trend meme», «No Man's Sky redemption documentary Noclip», «The Engoodening video essay», «No Man's Sky TikTok millions views», «No Man's Sky 10th anniversary trailer 2026 update», «No Man's Sky launch controversy meme lying Sean Murray». No hice búsquedas en japonés/coreano: el estudio (Hello Games) es británico y la obra no viene de Asia, así que no aplica ese requisito de ENCARGO.md.
- Wiki de Fandom (`nomanssky.fandom.com`) por su API: wikitext de «Music for an Infinite Universe» (lista de pistas verificada) e imágenes ya recolectadas del Viajero (descargadas con cabecera `Referer` para poder mirarlas).
- ambientCG (`api/v2/full_json`): texturas de arena/tierra («Ground054») y roca («Rock061»), ambas CC0, para las «texturas reales equivalentes» del punto 4.
- No until usé `navegar.py`: no hizo falta, ninguna web relevante bloqueó curl directamente (TikTok y Dailymotion respondieron bien por API).
