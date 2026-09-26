# Video · Hollow Knight (67-hollow-knight)

Investigador de vídeo. Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Libreta de datos, un dato por línea, con fuente y ✅/⚠️.
Hollow Knight es un videojuego (Team Cherry, 2017; secuela Silksong, 2025): no hay capítulos ni opening/ending de anime. Aquí «escena icónica» es tráiler oficial o cinemática de anuncio, y «capítulo» de la tabla del punto 14 es el vídeo o la imagen citada. Sin serie hermana en este encargo.

## 2 · Fotogramas de escenas icónicas (tráilers y cinemáticas, con minuto)

Todo mirado fotograma a fotograma con `herramientas/fotogramas.py` (YouTube pide iniciar sesión en este servidor; uso Dailymotion e Internet Archive, permitidos por AYUDANTE.md). La fuente es 1080p; la herramienta saca cada fotograma a 1280×720 fijo.

- **Silksong — tráiler oficial de lanzamiento** (Team Cherry, 4-sep-2025), mirado entero cada 8 s (15 fotogramas): abre con Hornet entrando de noche a un poblado (Bonebottom) junto a dos NPC sentados (0:08); salta un abismo entre hongos luminosos en Moss Grotto (0:24); en el aire, aguijón en alto, en medio de una explosión de luz de jefe (1:20); cierra con el logo y «SEPTEMBER 4» · mirror de prensa (3djuegos) en Dailymotion porque YouTube bloquea el servidor · https://www.dailymotion.com/video/x9p91g8 (&start=8, &start=24, &start=80) · ✅ (vídeo mirado entero, fecha confirmada en la wiki) · 0:08 / 0:24 / 1:20 de 1:53
- **Hollow Knight — tráiler «Ferocious Foes»** (Voidheart Edition, contenido gratis del juego base), mirado cada 8 s (16 fotogramas): el Knight de pie entre esporas azules canaliza un haz de energía naranja hacia una criatura oscura y redonda (0:32); camina junto a otros personajes sobre un montículo de máscaras bajo el cartel «EPIC BOSSES» (1:04–1:20); estallido de luz blanca (1:52); cierra con «TRAIN» y «FEBRUARY 24» · mirror en Dailymotion (JeuxVideo.com); el nombre del tráiler y su tema musical («Enter Hallownest») están confirmados en la tabla oficial de uso de la wiki del soundtrack · https://www.dailymotion.com/video/x89m9g8 · ✅ (mirror + wiki de soundtrack cita este tráiler por nombre) · 0:32 / 1:04 / 1:52 de 2:03
- **Cinemática de introducción de jefe**, demo jugable de Silksong (gameplay «Nintendo Treehouse Live @ E3 2019», mirror en Internet Archive): silueta de un jefe alado (alas rojo vino) enredada en telarañas antes del combate · https://archive.org/details/hollow-knight-silksong-switch-gameplay (archivo «Gameplay 2 BOSSES») · ⚠️ (vista, pero no identifiqué con certeza qué jefe es) · 1:30 de 23:30
- **Pelea de jefe en Bellhart** (mismo vídeo): Hornet avanza con paso firme y remata con un tajo de luz; salen despedidas varias criaturas pequeñas aladas · ídem · ✅ (coincide con el tema «Bell Beast» de la zona Bellhart, confirmado en la lista oficial de pistas) · 22:30 de 23:30
- **Boss reveal / combate largo**, demo «Silksong Demo Part 2» sin comentarios (1080p 60 fps): Hornet combate en la sala de la campana con tajos de seda que iluminan toda la pantalla en blanco · ídem, archivo «Demo Part 2» · ✅ · 11:15 de 15:00

## 4 · Luz y paleta de los sitios (medida en fotogramas de vídeo)

Complementa el punto 16 de imagen (que midió Dirtmouth, Fungal Wastes y Deepnest en capturas fijas de la wiki): aquí van sitios de **Silksong** medidos con `herramientas/estilo.py` sobre fotogramas de gameplay oficial, ninguno repetido de imagen.md.

- **Moss Grotto** (zona verde de entrada a Silksong): paleta degradado/pintado — #253F2A 19%, #39603A 15%, #62A461 12%, #8CCD7B 7%; línea #305224, saturación 45%, brillo 35% · medido con estilo.py sobre fotograma 4:00 de «Nintendo Treehouse Live @ E3 2019» (Internet Archive) · ✅ (medido) · 1280×720 (fuente 1080p)
- **Bellhart, corredor ornamentado en penumbra** (relieves dorados sobre verde oscuro): paleta casi negra con acentos oliva y dorado — #000100 49%, #0D1009, #191C13, #2C2A20, #4C4239; sombreado mixto, poca línea, saturación 38%, brillo 6% (el sitio más oscuro medido de toda la serie) · medido con estilo.py sobre fotograma 7:00 de «Silksong Demo Part 1» sin comentarios (Internet Archive) · ✅ · 1280×720
- **Bellhart, sala de la campana y el horno de lava**: paleta cálida degradada — #A15A37, #CA733E, #E89750, #794327; línea #492B19, saturación 62%, brillo 43% (la zona más luminosa medida de Silksong) · medido con estilo.py sobre fotograma 15:00 de «Gameplay 2 BOSSES» (Internet Archive) · ✅ · 1280×720
- **Bellhart, pasillo estructural con cadenas**: paleta de marrones apagados — #281E1B, #1A1514, #3E2D28, #5A4139; sombreado mixto, poca línea, saturación 30%, brillo 13% · medido con estilo.py sobre fotograma 8:00 de «Silksong Demo Part 1» · ✅ · 1280×720
- Comparación: Moss Grotto es la zona más saturada y luminosa medida en Silksong (verde vivo); Bellhart alterna penumbra casi negra en los corredores con la sala de la lava, la más cálida de toda la muestra — el juego trabaja el contraste luz/sombra por sala, no un degradado continuo · propio, comparando las 4 mediciones · ✅

## 9 · Música y sonido

Compositor: Christopher Larkin (ambos juegos). Tabla oficial de uso de cada pista tomada de la wiki (que reproduce los créditos del propio disco), cruzada con Wikipedia y con la duración exacta de MusicBrainz.

- Tema del **menú principal**: pista «Hollow Knight» · tabla oficial de uso de la wiki · https://hollowknight.fandom.com/wiki/Soundtrack_(Hollow_Knight) · ✅
- Tema de **apertura** (primer descenso a Hallownest): «Enter Hallownest», pista única; la misma wiki dice que es también el tema del tráiler «Ferocious Foes» (el mirado en el punto 2) · ídem · ✅ (tabla oficial + coincide con el tráiler mirado)
- Tema de los **finales**: «White Palace» suena en la zona White Palace y también sobre los créditos de cierre, según la tabla oficial · ídem · ✅
- Tema más **emotivo/climático**: «Sealed Vessel» (5:45, la pista más larga del disco) acompaña toda la secuencia final — Templo del Huevo Negro, la pelea contra el Hollow Knight (fase principal y clímax) y dos de los tres finales del juego (Ending 1 y Ending 3) · tabla oficial de la wiki + duración 345 s = 5:45 confirmada en MusicBrainz · ✅ (dos fuentes) · https://musicbrainz.org/release-group/9df7cf82-6ea3-4021-829f-f2192977ac8d
- Tema de **descanso**: «Reflection» suena en los bancos (bench) y en las aguas termales — el único momento sin amenaza con música propia · tabla oficial de la wiki · ✅
- Tema de **Hornet**: pista «Hornet», usada en sus peleas de jefe y, según la propia wiki, en «varios tráilers» — coincide con lo mirado en el punto 2 · ídem · ⚠️ (la wiki lo cita, no confirmé de oído el tráiler completo)
- **Silksong**, banda sonora nueva: 39+ pistas con nombre de zona o personaje — «Bell Beast» (jefe/zona Bellhart, coincide con la pelea mirada en el punto 2), «Lace» (personaje), «Moss Grotto», «Sister Splinter» · tracklist oficial en Internet Archive, cruzado con el catálogo del propio compositor (Bandcamp/Steam) · ✅ · https://archive.org/details/hollow-knight-silksong-ost
- Tono general (fuente ajena a la wiki, para no repetir sólo una fuente): Wikipedia describe la banda sonora de Larkin como «dark elegance» y «minimal instrumentation», «classical and melancholic», con piano extenso; usa viola en Dirtmouth/Hollow Knight y soprano en City of Tears (créditos del propio disco) · https://en.wikipedia.org/wiki/Music_of_Hollow_Knight · ✅ (dos fuentes: Wikipedia + créditos del disco en la wiki)
- **Efectos de sonido reconocibles** (no hay onomatopeyas en pantalla estilo manga — comprobado buscando `onomatopoeia` en el texto completo de la wiki, cero resultados; el juego marca el impacto con temblor de cámara y partículas, nunca con letras sobreimpresas): el tintineo al recoger Geo, el golpe seco del Nail al conectar (y el «clang» metálico del parry), el zumbido ascendente de Focus (curar canalizando soul) y el rugido grave de los jefes grandes (False Knight, Hollow Knight) · Voicy, soundboard con clips reales del juego · ⚠️ (una fuente, catálogo no oficial pero con audio genuino) · https://www.voicy.network/official-soundboards/games/hollow-knight

## 10 · Vídeos: tráileres, análisis y tendencias

- Tráiler oficial de lanzamiento de Silksong (Team Cherry, 4-sep-2025), 1:53, 501 031 vistas en el mirror · https://www.dailymotion.com/video/x9p91g8 · ✅
- Tráiler «Ferocious Foes» / Voidheart Edition (juego base), 2:03 · https://www.dailymotion.com/video/x89m9g8 · ✅
- Reveal Trailer de Silksong (anuncio 2019), 2:04, mirror JeuxVideo.com · https://www.dailymotion.com/video/x89mynp · ⚠️ (sólo comprobé título y duración, no lo miré fotograma a fotograma)
- Gameplay oficial completo «Nintendo Treehouse Live @ E3 2019» (Nintendo + Team Cherry), ~19 min mirados de presentadoras narrando en vivo mientras juegan Moss Grotto y Bellhart · mirror en Internet Archive (subido originalmente desde YouTube) · https://archive.org/details/hollow-knight-silksong-switch-gameplay · ✅
- Demos jugables oficiales de Silksong sin comentarios («Demo Part 1» y «Demo Part 2», 1080p 60 fps): usadas para medir paleta y poses limpias, sin overlay de cámara encima de la acción · mismo Archive.org · ✅
- Vídeo de análisis/preview en francés «JV Legends» (JeuxVideo.com), 18:28: los presentadores juegan una build muy temprana del Hollow Knight original, aún corriendo en un **Wii U dev kit** visible en cámara — curiosidad de making-of, el juego se probó en ese hardware antes de asentarse en PC/consolas actuales · https://www.dailymotion.com/video/x8ltc75 · ✅ (visto, minuto exacto del dev kit) · 13:00 de 18:28
- Tendencia viral: los años de espera por Silksong (anunciado 2019, salido 2025) generaron el meme recurrente de «8 segundos de gameplay» — burla por lo poco que Team Cherry mostraba en cada tráiler · TikTok, búsqueda «Hollow Knight Silksong got 8 seconds of footage» · ⚠️ (confirmado por el título del contenido, no medí vistas)
- Al salir Silksong (4-sep-2025) hubo una ola de clips de la primera pelea de jefe y «edits» de personajes en TikTok, además de celebraciones por el fin de la espera de 6 años · TikTok, tag #hollowknight y «Hollow Knight Silksong Official Video» · ⚠️ (una fuente/búsqueda, sin métricas propias)
- Varios medios hispanos (3djuegos, HobbyConsolas, Vidaextra, Vandal) resubieron el tráiler y el reveal de Silksong a Dailymotion como parte de su cobertura de noticias — confirma que la prensa en español cubrió el anuncio igual que la angloparlante · recolectado por recolectar.py, comprobado uno a uno · ✅ (varios medios coinciden en el mismo tráiler)

## 14 · Poses analizadas por personaje

Pose | Episodio (vídeo o imagen) | Minuto | Sirve para
---|---|---|---
Hornet entra de noche a un poblado, capa al viento, junto a dos NPC sentados | Silksong — tráiler de lanzamiento | 0:08 de 1:53 | presentar
Hornet salta un abismo entre hongos luminosos, aguijón atrás | Silksong — tráiler de lanzamiento | 0:24 de 1:53 | animar
Hornet en el aire, aguijón en alto, en medio de una explosión de luz de jefe | Silksong — tráiler de lanzamiento | 1:20 de 1:53 | regañar
Hornet combate a varias criaturas colgantes en un pasillo de cadenas | Nintendo Treehouse Live @ E3 2019 (Internet Archive) | 9:00 de 19:36 | regañar
Hornet, quieta, decide «Use Dock Key? Sí/No» frente a una puerta mecánica | Nintendo Treehouse Live @ E3 2019 (Internet Archive) | 15:00 de 19:36 | pensar
Hornet avanza con paso firme y remata a un jefe con un tajo de luz; salen despedidas criaturas pequeñas | Gameplay «2 BOSSES» (Internet Archive) | 22:30 de 23:30 | celebrar
Hornet de pie ante un arco en ruinas entre hongos, aguijón listo, calmada | Wiki — Screenshot HK Hornet 07 (enlace) | enlace | pensar
Hornet camina entre piedras rúnicas de un círculo antiguo, con una figura pequeña cerca | Wiki — Screenshot HK Hornet 02 (enlace) | enlace | presentar
Hornet se lanza en picada contra un enemigo entre chispas anaranjadas | Wiki — Screenshot HK Hornet 09 (enlace) | enlace | regañar
El Knight, entre esporas azules, canaliza un haz de energía naranja hacia una criatura oscura y redonda | Hollow Knight — tráiler «Ferocious Foes» | 0:32 de 2:03 | pensar
El Knight camina junto a otros personajes sobre un montículo de máscaras, bajo el cartel «EPIC BOSSES» | Hollow Knight — tráiler «Ferocious Foes» | 1:04-1:20 de 2:03 | presentar
Estallido de luz blanca alrededor del Knight (posible jefe cayendo) | Hollow Knight — tráiler «Ferocious Foes» | 1:52 de 2:03 | celebrar
El Knight sentado en un banco de Dirtmouth junto a una figura pequeña (Vessel), farola encendida | Wiki — Screenshot HK Knight 05 (enlace) | enlace | pensar
El Knight y otra figura pequeña sentados juntos a la orilla de un lago azul, en silencio | Wiki — Screenshot HK Knight 10 (enlace) | enlace | pensar
El Knight de pie frente a un NPC con capa y cuernos junto a la farola de Dirtmouth (conversación) | Wiki — Screenshot HK Knight 03 (enlace) | enlace | explicar
Quirrel de pie en un balcón, mano cerca de la barbilla, mirando la niebla azul | Wiki — Screenshot HK Quirrel 07 (enlace) | enlace | pensar
Quirrel de pie ante un gran arco de piedra con una máscara tallada y enredaderas | Wiki — Screenshot HK Quirrel 08 (enlace) | enlace | presentar
Quirrel mira hacia arriba un domo/caparazón gigante que brilla en azul, de noche | Wiki — Screenshot HK Quirrel 01 (enlace) | enlace | explicar
Quirrel camina por una estructura de arquitectura y seda, en movimiento | Wiki — Screenshot HK Quirrel 03 (enlace) | enlace | animar
Quirrel observa en silencio a una figura translúcida y blanca (la White Lady) en una sala verde | Wiki — Screenshot HK Quirrel 10 (enlace) | enlace | pensar
Quirrel, agachado, alza su estoque frente a una criatura gigante en forma de medusa cargada de electricidad | Wiki — Screenshot HK Quirrel 09 (enlace) | enlace | regañar
Quirrel sentado al borde de un muelle, piernas colgando, mirando un lago azul en silencio | Wiki — Screenshot HK Quirrel 11 (enlace) | enlace | pensar

Quirrel no aparece en ningún tráiler oficial ni en el gameplay de prensa mirado (es un NPC de ritmo lento, sin escenas de acción propias en material promocional): sus 7 poses salen de capturas fijas de la wiki, dentro del rango pedido. Enlaces de las imágenes de la wiki, en `video.json`.

## Lo mejor para la lámina

- Hornet entrando al poblado nocturno (tráiler de lanzamiento, 0:08): pose de «llegada», calmada, con capa al viento — sirve para presentar un canal.
- El Knight sentado en el banco de Dirtmouth junto a un Vessel (Screenshot HK Knight 05): la pose de «descanso/guardado» más reconocible del juego, perfecta para un rincón de «pensar» en la lámina.
- Bellhart, sala de la campana con lava (#A15A37/#CA733E/#E89750): el único sitio con luz cálida medida en todo Silksong, útil para dar profundidad de color sin caer en el azul-violeta dominante del resto del juego.
- «Sealed Vessel» (5:45) como referencia de qué tema suena en el momento más emotivo: piano y cuerdas in crescendo, útil si la lámina cita una frase o un cuadro de diálogo del clímax del juego.
- Quirrel mirando el domo glóbulo azul (Screenshot HK Quirrel 01): pose de asombro/quietud, buena para un personaje secundario que explica un lugar sin hablar.

## No encontré

- Identificación exacta del jefe alado de la cinemática de introducción de «2 BOSSES» (1:30) — sólo vi la silueta; no crucé el diseño con una ficha de la wiki para confirmar el nombre. ⚠️
- Métricas propias (vistas, likes) de los TikToks sobre Silksong — sólo confirmé que la tendencia existe por el título de los contenidos listados por el buscador, no abrí TikTok directamente (bloqueado sin sesión). ⚠️
- Audio exacto del tráiler «Ferocious Foes» para confirmar de oído que suena «Hornet» de fondo en la parte con máscaras — la wiki lo cita como uso de esa pista, pero no lo escuché con voz.py. ⚠️
- Vídeo de la cinemática final (créditos) del Hollow Knight original: no encontré un mirror completo fuera de YouTube (bloqueado); la música del final («White Palace») está confirmada por la wiki, pero no vi el vídeo. ⚠️

## Bitácora

- `herramientas/fotogramas.py` sobre 6 vídeos (Dailymotion x2, Internet Archive x4), unos 100 fotogramas mirados en hojas de contacto + 10 fotogramas sueltos en grande — sin bloqueos; YouTube dio «Sign in to confirm you're not a bot» en yt-dlp directo, como avisa AYUDANTE.md.
- `herramientas/estilo.py` sobre 4 fotogramas de vídeo (Moss Grotto, 3 rincones de Bellhart) para hex y estilo de sombreado medidos, no de memoria.
- Wiki de Fandom (`hollowknight.fandom.com/api.php`): `imageinfo` sobre 16 archivos «Screenshot HK …» para confirmar 1920×1080 real antes de citarlos, y `list=search&srwhat=text&srsearch=onomatopoeia` (cero resultados, comprobado antes de decir que no hay onomatopeyas en pantalla) y wikitext completo de `Soundtrack_(Hollow_Knight)` y `Dream_Nail`.
- MusicBrainz y Archive.org (ya recolectados por recolectar.py): tracklists completos de Hollow Knight OST y Silksong OST, comprobados y citados sin repetir la consulta.
- WebSearch (inglés): «Hollow Knight ending credits song theme Sealed Vessel OR Dream», «Hollow Knight iconic sound effects geo chime bench save dream nail whisper recognizable», «Hollow Knight Silksong TikTok trend viral 2025».
- WebFetch: `en.wikipedia.org/wiki/Music_of_Hollow_Knight` (tono de la banda sonora, temas de créditos y de la pelea final).
- No busqué en japonés/coreano: Hollow Knight es una obra australiana (Team Cherry) sin origen ni doblaje japonés/coreano relevante para vídeo o música; el doblaje y las voces son punto de otro investigador.
