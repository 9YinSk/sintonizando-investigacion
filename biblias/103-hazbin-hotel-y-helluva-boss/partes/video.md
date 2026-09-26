# Vídeo · Hazbin Hotel y Helluva Boss

Investigador de vídeo. Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. YouTube pide inicio de sesión en este
servidor (confirmado: descarga bloqueada, sólo metadatos con `--print`); todo lo mirado a fondo sale
de reups oficiales/idénticos en Dailymotion, vistos con `fotogramas.py` fotograma a fotograma. Serie
hermana 55-hazbin-hotel: sin `partes/video.md` ni `biblia.md` todavía, así que no hay nada que evitar repetir.

## 2 · Fotogramas de escenas icónicas

Vistas con `fotogramas.py` (hojas de contacto + fotogramas sueltos), no descritas de memoria. Los reups
de Dailymotion están a 1280×720 (o 1280×660 con barras), por debajo del 1080p que pide el encargo: es
el límite de red del servidor, lo anoto en «No encontré».

- Letrero de neón "HAZBIN HOTEL" bajándose entre farolas, con el gag "CALL NOW!!! OR DON'T! I DON'T CARE! WE STILL DON'T HAVE A WORKING PHONE!" · tráiler oficial S1, https://www.dailymotion.com/video/x8qjgw6?t=24 · ✅ (mismo plano, doblado al italiano, en https://www.dailymotion.com/video/x8rhuws?t=24) · 0:24 · 1280×720.
- Elenco completo reunido en el salón del hotel (Charlie, Vaggie, Alastor, Husk, Niffty, Angel Dust, Sir Pentious), plano general fijo tipo "foto de familia" · tráiler oficial S1, https://www.dailymotion.com/video/x8qjgw6?t=119 · ✅ (mismo plano en https://www.dailymotion.com/video/x8rhuws?t=?, aparece recortado con logo italiano superpuesto en el mismo tramo final) · 1:59 · 1280×720.
- Charlie y Vaggie de la mano, frente con frente, con Pentagram City ardiendo al fondo · tráiler oficial S1, https://www.dailymotion.com/video/x8qjgw6?t=56 · ✅ (mismo plano en x8rhuws?t=32) · 0:56 · 1280×720.
- Revelación de la forma real de exorcista de Vaggie: piel gris, ojo tachado con X, halo tipo mira, lanza en alto, fondo de líneas rojas cruzadas · tráiler oficial S1, https://www.dailymotion.com/video/x8qjgw6?t=77 · ⚠️ (sólo la vi en este reup) · 1:17 · 1280×720.
- Apertura del piloto de Helluva Boss: Blitzo señala una pizarra "FIXING SHIT" con una gráfica de ventas cayendo en picado · piloto completo, https://www.dailymotion.com/video/x8j7da8?t=0 · ✅ (mismo piloto, mismo segundo 0, en el segundo reup https://www.dailymotion.com/video/x8j9p8o) · 0:00 · 1280×660.
- Transformación demoníaca en el bosque nocturno, silueta violeta con una constelación dibujada a mano brillando sobre el cuerpo · "Murder Family" (S1E1 Helluva Boss), https://www.dailymotion.com/video/x8j7dde?t=450 · ⚠️ (un solo reup con el episodio completo) · 7:30 · 1280×660.
- Cartel pintado a mano "KILLED THE BITCH" frente a la casa, cierre cómico del episodio tras la matanza · "Murder Family", https://www.dailymotion.com/video/x8j7dde?t=720 · ⚠️ · 12:00 · 1280×660.

## 4 · Fondos y sitios

Luz y paleta medidas con `herramientas/estilo.py` sobre fotogramas sueltos sacados con `--fotograma`
(no de memoria ni de fan art). Texturas reales equivalentes buscadas en ambientCG.

- **Fachada del Hazbin Hotel** (letrero de neón, farolas): dominante carmesí `#740F2B`/`#9B1C39`, focos cálidos `#E2BD87`, saturación 78%, brillo 55% · medido en fotograma 0:24 del tráiler S1 (x8rhuws) · ✅ (mismo tono en x8qjgw6?t=24) · —
- **Salón/lobby del Hazbin Hotel** (art déco, sofá granate, molduras doradas): dominante vino `#300A18`/`#6C0E2A`, línea de contorno `#784747`, saturación 61%, brillo 43% (luz baja, cálida, tipo casino nocturno) · medido en fotograma 1:59 del tráiler S1 (x8qjgw6) · ✅ (mismo lobby reaparece con overlay italiano en x8rhuws) · —
- **Pentagram City al atardecer** (vista desde el hotel, skyline ardiendo, humo negro): dominante magenta `#450D2F`/`#AA0A39`/`#D21A4D`, saturación 72% (la escena con más color), brillo 58% · medido en fotograma 0:56 (x8qjgw6) · ⚠️ · —
- **Oficina de I.M.P.** (Helluva Boss, de día: pizarra de ventas, paredes rosa-marrón desteñido): dominante `#735861`/`#433039`/`#523D44`, línea `#595253`, saturación sólo 25%, brillo 42% — colores casi sepia, muy planos, de oficina cutre · medido en fotograma 3:20 del piloto (x8j7da8) · ✅ (misma paleta en el 2.º reup x8j9p8o) · —
- **Casa de Blitzo de noche** (cocina, refrigerador abierto): dominante malva `#7D5C64`/`#2E1820`, blancos `#D8CACC`/`#F4EFEE`, acento rojo `#BF3C55` del refrigerador, saturación 26%, brillo 62% (la luz del refrigerador es la única fuente fría de la escena, el resto es cálido) · medido en fotograma 6:15 del piloto · ⚠️ · —
- **Bosque nocturno** ("Murder Family", momento de transformación): dominante violeta oscuro `#09021F`/`#1C073F`/`#632ACD`/`#BA76DD`, saturación 86% — la más alta de todas las medidas —, brillo 40% · medido en fotograma 7:30 · ⚠️ · —
- **Misma escena, hoguera**: naranjas y amarillos `#FBF07D`/`#F1AE56`/`#C15F3B` sobre negro casi puro `#22090A`, saturación 74%, brillo 52%, fuerte contraluz · medido en fotograma 10:00 · ⚠️ · —
- Texturas reales equivalentes (CC0, ambientCG): alfombra roja del lobby → `Carpet016` (https://ambientcg.com/view?id=Carpet016); terciopelo del sofá → `Fabric028`/`Fabric081C` (https://ambientcg.com/view?id=Fabric028); molduras doradas del hotel → `Metal048A` (https://ambientcg.com/view?id=Metal048A); madera de la casa de Blitzo → `Wood095` (https://ambientcg.com/view?id=Wood095) · ambientcg.com/api/v2 · ✅ (existencia y licencia CC0 confirmadas por la propia API) · —

## 9 · Música y sonido

Ni Hazbin Hotel ni Helluva Boss tienen opening/ending al estilo anime: Hazbin es un musical (cada
episodio trae 1-3 canciones originales) y Helluva Boss abre con un jingle in-universe. Confirmado en
`hazbinhotel.fandom.com` (wikitext, categoría «Songs» con más de 90 páginas) y viendo los propios vídeos.

- "Happy Day in Hell" (S1E1 "Overture", Sam Haft y Andrew Underberg, cantada por Charlie/Erika Henningsen) hace de número de apertura de la serie: presenta Pentagram City mientras Charlie camina cantando hacia la Embajada del Cielo · https://hazbinhotel.fandom.com/wiki/Happy_Day_in_Hell (wikitext) · ✅ (fecha de adelanto 14-oct-2023 y lanzamiento 20-oct-2023 citadas con tuit de Sam Haft) · dura 2:57.
- "Inside of Every Demon is a Rainbow" (canción promocional del piloto 2019, Parry Gripp, cantada por Elsie Lovelock) es el tema asociado al piloto viral; tiene una reprise cantada por Alastor justo después, cuando la convence de que él tiene buenas intenciones · https://hazbinhotel.fandom.com/wiki/Inside_of_Every_Demon_is_a_Rainbow · ✅ (lanzamiento 5-oct-2018 en Spotify/Amazon/iTunes con enlaces directos en la wiki; luego fue retirada de Spotify) · dura 1:37.
- "Loser, Baby" (S1E4 "Masquerade", Husk y Angel Dust) es la canción de la escena más emotiva entre ambos: Husk anima a Angel a dejar de odiarse y aceptarse · https://hazbinhotel.fandom.com/wiki/Loser,_Baby · ✅ · dura 2:50 (versión de la serie).
- Helluva Boss abre cada episodio con el **I.M.P Jingle**, un comercial cantado in-universe (Parry Gripp en el piloto, versión rock de Lyle Rath en "Mission: Zero") · https://hazbinhotel.fandom.com/wiki/I.M.P_Jingle · ✅ (se oye y se ve el logo I.M.P en el minuto 2:55 del reup del piloto, y está descrito igual en la wiki) · dura 0:29 (piloto) / 0:36 (rock).
- Bandas sonoras oficiales en streaming: "Hazbin Hotel Original Soundtrack" (A24 Music, publicada en 3 partes entre el 19-ene y el 2-feb-2024) y "Helluva Boss: Season One/Two (Original Soundtrack)" · MusicBrainz (ya en datos-video.md, release-groups 1d1b2728… y 1b046058…) + https://hazbinhotel.fandom.com/wiki/Hazbin_Hotel_Original_Soundtrack · ✅ · —
- Efecto de sonido reconocible: la voz de Alastor lleva un filtro de radio (estática, eco, cambios de tono) que él controla como poder llamado "Acoustokinesis"; también proyecta risas, abucheos o gritos de sus víctimas como efectos desde su bastón-micrófono · https://hazbinhotel.fandom.com/wiki/Alastor (wikitext, sección de poderes) · ✅ (se oye el filtro exactamente en el tramo 1:38-1:59 del tráiler S1 visto arriba, y la wiki lo describe igual) · —
- Origen real de ese filtro: su creadora Vivienne Medrano contó en entrevista que se inspiró en la versión con filtro de radio de "You're Never Fully Dressed Without a Smile" (de la película *Annie*) para decidir cómo sonaría Alastor · citado en la wiki de Alastor, que enlaza a movieweb.com · ⚠️ (una sola fuente indirecta, no vi la entrevista original) · —

## 10 · Vídeos

Tráileres y escenas con minuto exacto (arriba, punto 2); aquí lo que no encaja ahí: análisis, alcance y
tendencias.

- Tráiler oficial temporada 1 de Prime Video ("NEW SERIES | January 19"), reup en Dailymotion, 2:19 · https://www.dailymotion.com/video/x8qjgw6 · ✅ (mismo tráiler doblado al italiano en https://www.dailymotion.com/video/x8rhuws, 2:07) · visto completo con hojas cada 7 s.
- Tráiler oficial temporada 2 de Prime Video: localizado por título y duración con `yt-dlp --print` (sin descargar, YouTube pidió confirmar que no soy un robot) · https://www.youtube.com/watch?v=Ro311cUw5b0 · ⚠️ (sólo metadatos: título "Hazbin Hotel - Season 2 Official Trailer", 161 s; no pude verlo fotograma a fotograma) · —
- Piloto completo de Helluva Boss (2020), 10:02, visto entero · https://www.dailymotion.com/video/x8j7da8 · ✅ (mismo piloto, mismos 603 s, en el reup https://www.dailymotion.com/video/x8j9p8o) · —
- Episodio "Murder Family" (S1E1 Helluva Boss), 12:20, visto entero · https://www.dailymotion.com/video/x8j7dde · ⚠️ (un solo reup con el episodio completo) · —
- Tendencia de fan edits en YouTube Shorts/TikTok con la canción "Poison" (Angel Dust): un short "POISON… [CW]" tiene 4,2 millones de vistas; un animatic de fan "Gossip" pasa de 7,4 millones · búsqueda `ytsearch` (metadatos con yt-dlp, sin descarga) · ⚠️ (vistas de YouTube, no pude confirmar el dato específico de TikTok: su API pública no da métricas desde este servidor) · —
- Tendencia de "edits"/AMV de Hazbin Hotel: compilaciones con CapCut llegan a 300 mil vistas, "Stayed Gone but more threatening" (remix de fan) a 238 mil · `ytsearch5:Hazbin Hotel edit` (yt-dlp --print) · ⚠️ · —
- Canciones de Helluva Boss con más tirón en YouTube: "Cotton Candy" (Queen Bee, S1E8) 2 millones de vistas, "F**K YOU" (canción final de Fizzarolli, S2E7) 3 millones · `ytsearch5:Helluva Boss viral` (yt-dlp --print) · ⚠️ · —
- Vídeos de análisis en YouTube (metadatos con yt-dlp, sin descarga): "Hazbin Hotel: The 7 Deadly Sins of Modern Writing" (canal Roaming Trend, 1,55 millones de vistas) y "A Comprehensive Evisceration of Hazbin Hotel Season 2" (Random Film Talk, 391 mil vistas) son los análisis/críticas más vistos que encontré; también hay defensas como "An Exhaustively Detailed Deep Dive of Hazbin Hotel Season 2" (Maddie's Maxis, 81 mil vistas) · `ytsearch4:Hazbin Hotel video essay analysis` · ⚠️ (sólo metadatos, no vi el contenido completo de los análisis) · —
- Actividad reciente en r/HazbinHotel (no es "tendencia viral" histórica, sólo pulso actual del sub): el post con más votos de las últimas semanas es sobre qué personaje "asustaría más" físicamente (1634 puntos, 173 comentarios); el segundo es fan art de un ship Husk×Angel Dust ("Huskerdust") · Arctic Shift, https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=HazbinHotel · ⚠️ (muestra parcial, sin orden por "top histórico" real: la API sólo deja ordenar por fecha) · —

## 14 · Poses analizadas

Sacadas de los mismos fotogramas del tráiler S1 y del piloto de Helluva Boss (arriba), con minuto y qué
hace cada quien. Cubre los 4 personajes de arranque del encargo (Charlie, Alastor, Angel Dust, Vaggie)
y el elenco principal de Helluva Boss, con el que hay más metraje disponible sin bloqueo de YouTube.

Pose | Episodio | Minuto | Sirve para
---|---|---|---
Charlie sonríe segura, sentada con las piernas cruzadas en el sofá del lobby, manos relajadas sobre las rodillas | Tráiler S1 (elenco en el salón) | 1:59 · https://www.dailymotion.com/video/x8qjgw6?t=119 | presentar / animar
Charlie y Vaggie frente a frente, manos entrelazadas, mirada hacia arriba, sonrisa cómplice | Tráiler S1 | 0:56 · https://www.dailymotion.com/video/x8qjgw6?t=56 | animar / celebrar
Vaggie, forma real de exorcista: piel gris, lanza en alto con las dos manos, ceño fruncido, halo tipo mira sobre la cabeza | Tráiler S1 | 1:17 · https://www.dailymotion.com/video/x8qjgw6?t=77 | regañar / amenazar
Vaggie sentada en el sofá, brazos cruzados, mirada de lado (X en el ojo bien visible) | Tráiler S1 (elenco en el salón) | 1:59 · https://www.dailymotion.com/video/x8qjgw6?t=119 | explicar / vigilar
Alastor de pie junto al sofá, un brazo apoyado en el bastón-micrófono, sonrisa amplia con dientes afilados, orejas de ciervo erguidas | Tráiler S1 (elenco en el salón) | 1:59 · https://www.dailymotion.com/video/x8qjgw6?t=119 | presentar / amenazar (sonriendo)
Angel Dust sentado en el suelo, sombrero de copa ladeado, una de sus 4 manos apoyada en la cadera | Tráiler S1 (elenco en el salón) | 1:59 · https://www.dailymotion.com/video/x8qjgw6?t=119 | celebrar / relajarse
Angel Dust de pie, brazo alzado con una pistola en la mano, torso echado hacia atrás | Tráiler S1 (grupo en la calle) | 0:21 · https://www.dailymotion.com/video/x8qjgw6?t=21 | explicar (con dramatismo) / amenazar
Blitzo apuntando con el dedo a una pizarra con gráficas cayendo, ceja fruncida, postura inclinada hacia adelante | Piloto de Helluva Boss | 0:00 · https://www.dailymotion.com/video/x8j7da8?t=0 | explicar / regañar
Loona con la puerta del refrigerador abierta, un brazo apoyado en la puerta, mirada de fastidio de lado | Piloto de Helluva Boss | 6:15 · https://www.dailymotion.com/video/x8j7da8?t=375 | pensar (desinterés) / regañar
Moxxie y Millie con las manos entrelazadas sobre la mesa, mirándose, pastel de cumpleaños detrás | Piloto de Helluva Boss | 4:35 · https://www.dailymotion.com/video/x8j7da8?t=275 | celebrar / animar
Husk apoyado en el escritorio del lobby, un brazo colgando, mirada de lado, postura relajada/cansada | Tráiler S1 (elenco en el salón) | 1:59 · https://www.dailymotion.com/video/x8qjgw6?t=119 | pensar (hastío) / explicar
Sir Pentious de pie muy erguido, cola enroscada en el suelo, sosteniendo una piruleta gigante cerca de la boca | Tráiler S1 (elenco en el salón) | 1:59 · https://www.dailymotion.com/video/x8qjgw6?t=119 | presentar / celebrar
Niffty asomando sólo la cabeza y un ojo enorme por detrás del respaldo del sofá | Tráiler S1 (elenco en el salón) | 1:59 · https://www.dailymotion.com/video/x8qjgw6?t=119 | pensar (curiosidad) / gag visual
Angel Dust abraza a Charlie por detrás, mejilla con mejilla, expresión tierna (versión doblada IT) | Tráiler S1 doblado | 0:56 · https://www.dailymotion.com/video/x8rhuws?t=56 | animar / consolar

## Lo mejor para la lámina

- El letrero de neón "HAZBIN HOTEL" (0:24 del tráiler, https://www.dailymotion.com/video/x8qjgw6?t=24): objeto real, tipografía y luz cálida ya resueltos, perfecto para encabezar cualquier lámina del hotel.
- La escena de grupo en el lobby (1:59, mismo tráiler): un plano con los 7 personajes principales ya en pose de "sala de estar", útil como referencia de composición si la lámina lleva a varios.
- El filtro de radio de Alastor (estática + eco) es la seña sonora más reconocible de la serie: cualquier lámina sobre "radio" o "locución" del servidor puede citarlo directo.
- La paleta violeta muy saturada del bosque de "Murder Family" (7:30, saturación 86%) sirve de contraste si se quiere una lámina "de miedo" en vez del rojo dominante del resto de la obra.
- "Loser, Baby" (Husk y Angel Dust) es la canción-ejemplo si el redactor necesita un momento emotivo con música real y verificable, no inventada.

## No encontré

- Fotogramas a 1080p+ reales: YouTube bloquea la descarga en este servidor ("Sign in to confirm you're not a bot"); todo lo mirado sale de reups de Dailymotion a 1280×720/660. Búsquedas: `yt-dlp` directo a varias URLs de YouTube (Prime Video, VivziePop/SpindleHorse), todas rechazadas igual.
- AnimeThemes: no aplica, es una web para openings/endings de anime y esta obra es occidental — comprobado que el buscador de AnimeThemes no tiene ninguna entrada para "Hazbin" ni "Helluva".
- Métrica real de TikTok (vistas, "tendencia" con cifras): la API pública de TikTok no responde desde este servidor; usé YouTube (`ytsearch` con yt-dlp) como proxy razonable, marcado con ⚠️.
- Vídeo completo de un capítulo de Hazbin Hotel (para sacar más poses de Charlie/Alastor fuera del tráiler): sólo encontré clips cortos y trailers en Dailymotion; los episodios completos están detrás del muro de Prime Video. Búsquedas: `Hazbin Hotel Episode 1`, `Hazbin Hotel S1 E1`, `Hazbin Hotel Overture` en la API de Dailymotion, sin resultado válido (sólo trailers repetidos y clips de segundos).
- Personaje de la ficha "1:38" del tráiler S1 (ave/pájaro morado sobre fondo turquesa): no lo identifiqué con seguridad, podría ser un vistazo a un personaje secundario de temporadas posteriores; lo dejo fuera de la tabla de poses por no tener nombre confirmado.

## Bitácora

- Dailymotion API (`api.dailymotion.com/videos?search=...`): "Hazbin Hotel official trailer" (es), "Helluva Boss opening" (en), "Inside of Every Demon is a Rainbow" (en, sin resultado útil), "Helluva Boss season 2 trailer" (en), "Hazbin Hotel Episode 1 Happy Hotel" (en, sin episodio completo), "Hazbin Hotel S1 E1" (en, sin resultado), "Hazbin Hotel viral moment" (en).
- `yt-dlp --skip-download --print` (sin descarga, sólo metadatos): `ytsearch3:Hazbin Hotel official trailer`, `ytsearch5:Hazbin Hotel edit`, `ytsearch5:Helluva Boss viral`, `ytsearch5:Hazbin Hotel Poison tiktok trend`, `ytsearch4:Hazbin Hotel video essay analysis` — todos en inglés.
- `fotogramas.py` sobre: tráiler S1 doblado IT (x8rhuws, cada 8 s), tráiler S1 oficial en (x8qjgw6, cada 7 s + fotogramas sueltos), piloto Helluva Boss (x8j7da8, cada 25 s + sueltos), "Murder Family" S1E1 Helluva Boss (x8j7dde, cada 30 s + sueltos).
- `estilo.py --colores 6` sobre 7 fotogramas sueltos (fachada y lobby del hotel, skyline de Pentagram City, oficina y casa de Blitzo, bosque y hoguera de "Murder Family").
- `hazbinhotel.fandom.com/api.php` (en): `action=query&list=search` para "opening theme song", "intro sequence OR title card", "credits song", "Alastor radio static filter voice"; `action=query&list=categorymembers&cmtitle=Category:Songs`; `action=parse&prop=wikitext` sobre "Happy Day in Hell", "Inside of Every Demon is a Rainbow", "I.M.P Jingle", "Hazbin Hotel Original Soundtrack", "Hell's Greatest Dad", "Loser, Baby", "Alastor", "Hazbin Hotel (series)/Episode Guide".
- `arctic-shift.photon-reddit.com/api/posts/search?subreddit=HazbinHotel` (en): sin filtro de orden por score real (la API sólo deja `asc`/`desc` por fecha), ordenado a mano en Python.
- `ambientcg.com/api/v2/full_json` (en): "velvet" (sin resultado), "Fabric", "Carpet", "WallpaperDamask" (sin resultado), "Metal", "Gold", "Wood".
- MusicBrainz y Dailymotion de `datos-video.md` (ya recolectados, revisados: la mayoría de MusicBrainz eran ruido —"Boss", "Yes Boss", etc.—, sólo sirvieron los 2 releases de Helluva Boss OST; el clip "Match Made in Hell" de Dailymotion resultó ser un montaje de fan no oficial, descartado).
