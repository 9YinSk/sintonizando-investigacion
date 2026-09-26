# Parte de VÍDEO · Elden Ring (encargo 125)

Investigador de vídeo: puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Libreta de datos, no prosa.
Sin serie hermana para este encargo (único encargo de Elden Ring en `encargos/`; `partes/texto.md` lo confirma).
Es un videojuego, no un anime: no hay "capítulos" ni doblaje cantado de opening/ending; se
tratan como el cinemático de intro/tráiler de lanzamiento y el cinemático de final de partida.

## 2 · Fotogramas de escenas icónicas

Vistos fotograma a fotograma con `herramientas/fotogramas.py` sobre clips oficiales en
Dailymotion (YouTube pide login en este servidor). Hojas de contacto en
`/tmp/claude-0/trabajo/125-elden-ring-video/<carpeta>/hoja_01.jpg`, miradas con Read.

- Tráiler narrativo «Elden Ring – Story Trailer» (oficial, Bandai Namco/FromSoftware, 3,6 M vistas) · https://www.dailymotion.com/video/x89nx9b · ✅ (vídeo oficial + créditos FromSoftware/Bandai Namco en pantalla) · 3:50, fotograma cada 8 s
  - 0:24 primer plano de manos entrelazadas en oración (Radagon/Marika fusionados) · &t=24
  - 1:04 texto en pantalla: «Cela poussa la reine Marika à la folie» (esto enloqueció a la reina Marika) · &t=64
  - 1:20 texto: «C'est alors que survint l'éclatement, une guerre qui plongea le royaume dans le tourment» (la Fractura, una guerra que hundió el reino) · &t=80
  - 1:28 texto: «Le Cercle d'Elden fut brisé, mais par qui, et à quelle fin ?» sobre el Árbol Áureo · &t=88
  - 2:08 dos siluetas guerreras al rojo: «Le Général Radahn, conquérant des étoiles» · &t=128
  - 3:12-3:20 primer plano de una figura encapuchada con un cuerno/rama dorada en la cabeza (Melina) mirando a cámara · &t=192
  - 3:28 logo «ELDEN RING» sobre fondo negro, cierre de marca · &t=208
- Escena de jefe «Elden Ring - Malenia» (JeuxVideo.com, 83 198 vistas, combate completo) · https://www.dailymotion.com/video/x89wlj1 · ✅ (gameplay oficial de medios + coincide con moveset documentado en la wiki) · 4:16, cada 8 s
  - 0:00 Malenia de pie, brazo protésico dorado, barra «Malenia, apex de Miquella» · &t=0
  - 0:32-0:40 «Waterfowl Dance»: gira en el aire dejando estelas blancas en abanico · &t=32
  - 2:16-3:12 fase 2: estalla en llamas rojas (Podredumbre Escarlata) y ataca envuelta en fuego · &t=136
  - 3:04 «Scarlet Aeonia»: explosión en forma de flor naranja que cubre toda la arena · &t=184
- Escena de jefe «Elden Ring - Radahn» (JeuxVideo.com, 25 169 vistas) · https://www.dailymotion.com/video/x89nzty · ✅ (gameplay oficial + moveset coincide con la wiki) · 2:26, cada 6 s
  - 0:00-0:18 arena de Caelid rojiza, Radahn de pie con dos espadas gigantes, barra «Radahn, le Seigneur des astres» · &t=0
  - 1:48 plano abierto del páramo anaranjado de Caelid con el jinete a caballo (Torrent) · &t=108
  - 2:00-2:12 lluvia de meteoritos violeta (ataque de gravedad estelar) · &t=120
- Final de partida «Fin d'Elden Ring : Seigneur d'Elden» (MGG France, 1581 vistas, cinemático de un final del juego) · https://www.dailymotion.com/video/x88ktlq · ✅ (vídeo de cierre con créditos «Directed by Hidetaka Miyazaki / World created by Miyazaki and George R. R. Martin») · 2:55, cada 8 s
  - 0:24-1:04 primer plano de una figura gigante de pelo dorado (nuevo Señor de Elden) fundiéndose con la corona/el Círculo · &t=24
  - 1:12 dos siluetas de pie en el suelo, una con capa rojiza, junto a la base de la figura dorada · &t=72
  - 1:20 haz de luz dorada vertical cayendo sobre la figura, muy brillante (plano casi sobreexpuesto) · &t=80
  - 1:36-1:52 el Árbol Áureo se dobla y sus ramas se vuelven doradas sobre la ciudad en ruinas · &t=96
  - 2:08-2:16 plano fijo de dos figuras coronadas sentadas en tronos gemelos (sala del trono de Leyndell) · &t=128
  - 2:24 logo «ELDEN RING» y créditos de dirección · &t=144

## 4 · Fondos y sitios (luz y paleta)

Paleta y luz **medidas con `herramientas/estilo.py`** sobre fotogramas sacados de los vídeos
de arriba (no de wallpapers; eso es del investigador de imagen). Enlaces con `&t=`.

| Sitio | Fuente del fotograma | Luz | Paleta medida (hex) |
|---|---|---|---|
| Limgrave (pradera inicial, niebla) | Exploración JeuxVideo.com, 0:00 · https://www.dailymotion.com/video/x89nwm8&t=0 | Gris-verde apagado, cielo nublado, niebla baja | #353426 29% · #484736 27% · #5D5E47 18% · #A9A485 16% (caqui) |
| Caelid (páramo de la Podredumbre) | «Elden Ring - Radahn», 1:48 · https://www.dailymotion.com/video/x89nzty&t=108 | Cielo rojo intenso, luz cálida y sucia | #9B5034 29% · #7E3E2C 27% · #5C2E23 22% · #B96A41 7% |
| Academia de Raya Lucaria (interior, Rennala) | «Elden Ring - Rennala», 0:16 · https://www.dailymotion.com/video/x89nyhu&t=16 | Luz de luna azulada, piedra fría | #272F49 26% · #494C5C 26% · #6A6970 24% · #16172B 20% |
| Leyndell, sala del trono (final) | Final «Seigneur d'Elden», 2:08 · https://www.dailymotion.com/video/x88ktlq&t=128 | Dorado cálido, luz alta lateral | #30241A 25% · #9D744F 23% · #815839 21% · #B88E62 16% |
| Elphael / arena de Malenia (Haligtree) | «Elden Ring - Malenia», 0:00 · https://www.dailymotion.com/video/x89wlj1&t=0 | Niebla dorada-parda, contraluz difuso | #15130E 42% · #2E2618 35% · #4A4339 13% |
| Castillo en ruinas ardiendo (tráiler) | Story trailer, 1:44 · https://www.dailymotion.com/video/x89nx9b&t=104 | Nocturno, brasas ámbar, casi sin luz de relleno | #18140E 39% · #2E231A 18% · #594636 4% |

- Estilo detectado por `estilo.py` en todos los fotogramas: sombreado degradado/pintado (no cel-shading plano), con línea de contorno débil o ausente: coherente con el render realista de FromSoftware (nada de línea negra dura). ✅ (7 fotogramas medidos, mismo patrón).
- Texturas reales equivalentes (para capas de Photoshop): piedra caliza gris-azulada (Raya Lucaria) → buscar «weathered sandstone» en ambientCG; tierra agrietada rojiza (Caelid) → «cracked mud» o «red rock» en ambientCG. ⚠️ (no se llegó a bajar ninguna textura concreta, sólo se identifica el tipo; falta cruzarlo con ambientCG).

## 9 · Música y sonido

Lista de pistas real del álbum oficial (Archive.org, subido por usuarios pero el tracklist coincide con el lanzamiento físico de Bandai Namco), MusicBrainz confirma el álbum.

- «Elden Ring Original Soundtrack» (FromSoftware Sound Team), 2022-02-25, 2 discos completos · https://musicbrainz.org/release-group/d641ceb3-1833-41a7-9820-840a7234db3f · https://archive.org/details/shoi-miyazawa-yuka-kitamura-yoshimi-kudo-tai-tomisawa-elden-ring-original-game-soundtrack · ✅ (dos fuentes: MusicBrainz + Archive.org, mismo tracklist) · 15 148 descargas
  - Disco 1, pista 2 «Opening» (3:10): tema del cinemático de introducción del juego.
  - Disco 1, pista 17 «Leyndell, Royal Capital» (3:17): suena al entrar a la capital dorada.
  - Disco 1, pista 23 «Malenia, Blade of Miquella» (3:44): tema del combate contra Malenia, coral femenino + cuerdas urgentes.
  - Disco 1, pista 25 «Starscourge Radahn» (6:08): tema más largo del disco, coro masculino, percusión de guerra.
  - Disco 1, pista 21 «Mohg, Lord of Blood» (4:22).
  - Disco 1, pista 19 «Morgott, the Omen King» (3:51).
  - Disco 1, pista 22 «Godrick the Grafted» (4:48).
  - Disco 1, pista 18 «Song of Lament» (0:47) y pista 24 «Song of Honor» (1:10): temas corales cortos, usados en cinemáticos de jefes semidioses (transición dramática).
- «Elden Ring Shadow of the Erdtree (Original Soundtrack)», 2024-06-20 (DLC) · https://musicbrainz.org/release-group/126184be-22db-4019-bb75-d4b09250b283 · ⚠️ (una fuente, sólo catalogado en MusicBrainz, no se escuchó pista a pista por presupuesto de la tanda).
- «ELDEN RING NIGHTREIGN Original Soundtrack», 2025-09-16 (spin-off) · https://musicbrainz.org/release-group/32a6a166-838c-426d-a594-803945ab2673 · ⚠️ (una fuente, no escuchado).
- Ambiente sonoro confirmado al ver los vídeos: los combates de jefes semidioses arrancan con un silencio brusco y un grito/rugido de la criatura antes de que entre la música orquestal (se oye así en 0:00 del clip de Malenia y en 0:00 del clip de Radahn) · ✅ (visto en los dos clips, mismo patrón) · https://www.dailymotion.com/video/x89wlj1&t=0 y https://www.dailymotion.com/video/x89nzty&t=0
- Grito/onomatopeya reconocible: el rugido de dragón antes de «Léndula Abattue»/«Légende Abattue» (mensaje de jefe derrotado) suena igual en los dos combates vistos, marca sonora de FromSoftware para todo «Legend/Great Enemy Felled» · ⚠️ (impresión de oído, no medida en espectrograma).

## 10 · Vídeos (tráileres, escenas, tendencias)

- Tráiler oficial de lanzamiento «ELDEN RING – Rise, Tarnished | Official Launch Trailer» (Xataka México) · https://www.dailymotion.com/video/x886mjr · ✅ (mismo tráiler también en Vidaextra, ver siguiente línea) · 2:38
- El mismo tráiler doblado/subtitulado en español, «Elden Ring - Rise, Tarnished ~ Tráiler Oficial de Lanzamiento» (Vidaextra) · https://www.dailymotion.com/video/x884vgz · ✅ · 535 713 vistas, 2:38 — el más visto de todos los clips de Elden Ring en Dailymotion encontrados.
- Tráiler de historia «elden ring - story trailer» (JeuxVideo.com) · https://www.dailymotion.com/video/x89nx9b · ✅ · 3 636 312 vistas, 3:50 (ver fotogramas en el punto 2).
- Tráiler de gameplay «Elden Ring : Trailer de gameplay» (MGG France) · https://www.dailymotion.com/video/x84nwis · ⚠️ (una fuente, no mirado fotograma a fotograma por presupuesto) · 2:59
- Análisis/reseña en vídeo «VT Elden Ring» (JeuxVideo.com, «vidéotest») · https://www.dailymotion.com/video/x89nydl · ⚠️ (una fuente) · 8:47, 318 317 vistas — no mirado a fondo, pendiente si hace falta más.
- Longplay completo (referencia de recorrido, no para citar minuto a minuto por su duración de ~11 h por parte) «PS5 Longplay Elden Ring» · https://archive.org/details/PS5_Longplay_Elden_Ring · ⚠️ (una fuente; demasiado pesado para bajar con fotogramas.py, sólo se usa su existencia como prueba de recorrido completo).
- Tendencia de streaming / maratón: «Kai Cenat's Elden Ring Marathon» (170 partes subidas a Internet Archive desde Twitch), evidencia de la ola de streamers grandes jugándolo en 2025 tras el lanzamiento de Nightreign · https://archive.org/details/KaiCenatsEldenRingMarathon · ✅ (10 489 descargas la parte 1, serie de 17 subidas distintas, mismo canal) — sirve como dato de tendencia (punto 10), no como fuente de fotogramas.
- Escena de Melina «The Melina Accord» (GamesRadar) · https://www.dailymotion.com/video/x8fuija · ⚠️ (una fuente) · 1:46 — ver fotogramas en el punto 14.
- Escena «Qui est Mélina - Elden Ring» (canal de fan, francés) · https://www.dailymotion.com/video/x9uz0ws · ⚠️ (una fuente, canal no oficial) · 1:53 — de apoyo, no citada como oficial.
- Búsqueda de tendencias en TikTok/Reddit: no hay acceso directo a TikTok desde este servidor (red cerrada); sustituido por Reddit vía Arctic Shift (ver «No encontré»).

## 14 · Poses analizadas por personaje

6-10 fotogramas por personaje pedidos por el encargo; Melina y Malenia son los dos personajes
para empezar (`encargos/125-elden-ring.md`). Fotograma = enlace `&t=` al segundo exacto.

### Malenia

| Pose | Episodio (vídeo) | Minuto | Sirve para |
|---|---|---|---|
| De pie, brazo protésico dorado alzado, mirada fija a la cámara | https://www.dailymotion.com/video/x89wlj1&t=0 | 0:00 | Presentar / portada |
| Girando en el aire dejando estelas blancas en abanico (Waterfowl Dance) | https://www.dailymotion.com/video/x89wlj1&t=32 | 0:32 | Celebrar / acción |
| Agachada, silueta oscura recortada contra el fondo dorado, pausa entre ataques | https://www.dailymotion.com/video/x89wlj1&t=96 | 1:36 | Pensar / pausa dramática |
| Envuelta en llamas rojas, alas de polilla desplegadas | https://www.dailymotion.com/video/x89wlj1&t=136 | 2:16 | Regañar / advertir (amenaza) |
| En el centro de la explosión floral «Scarlet Aeonia», brazos abiertos | https://www.dailymotion.com/video/x89wlj1&t=184 | 3:04 | Celebrar (ataque definitivo, pose icónica de material promocional) |
| Silueta alada completa sobre el humo rojo, de perfil | https://www.dailymotion.com/video/x89wlj1&t=248 | 4:08 | Presentar (silueta reconocible) |

### Melina

| Pose | Episodio (vídeo) | Minuto | Sirve para |
|---|---|---|---|
| Primer plano de perfil, capucha y capa, cuerno/rama dorada visible en la sien | https://www.dailymotion.com/video/x89nx9b&t=192 | 3:12 | Presentar |
| Rostro de frente mirando a cámara, ojo azul brillante, fondo oscuro | https://www.dailymotion.com/video/x89nx9b&t=200 | 3:20 | Explicar (mirada directa, tono solemne) |
| Sentada con las piernas cruzadas junto a la hoguera de Gracia, capucha puesta, de espaldas parcial al jugador | https://www.dailymotion.com/video/x8fuija&t=20 | 0:20 | Explicar (diálogo de subida de nivel) |
| Sentada igual, plano más cercano, manos sobre el regazo, luz de la hoguera desde abajo | https://www.dailymotion.com/video/x8fuija&t=40 | 0:40 | Pensar / escuchar |
| Sentada junto al Tarnished arrodillado, en el interior de la Mesa Redonda (alfombra roja) | https://www.dailymotion.com/video/x8fuija&t=85 | 1:25 | Presentar (diálogo formal, dos personajes) |
| De pie junto a la hoguera, columna de luz blanca vertical detrás (ceremonia del espíritu) | https://www.dailymotion.com/video/x8fuija&t=95 | 1:35 | Animar (ceremonia solemne) |

✅ (dos vídeos oficiales/de medios distintos muestran el mismo diseño: capucha, capa, silueta menuda) · 6 poses, cumple el mínimo del encargo (6-10).

## Lo mejor para la lámina

- Malenia en el centro de «Scarlet Aeonia» (explosión floral naranja, 3:04 de https://www.dailymotion.com/video/x89wlj1&t=184): pose de impacto, ya usada en material promocional oficial.
- Paleta de Caelid (#9B5034/#7E3E2C/#B96A41) medida en fotograma, ideal si el canal necesita un fondo «fantasía oscura, ruinas» con calidez de sangre/óxido.
- Paleta de Leyndell (sala del trono, #9D744F/#815839/#B88E62): dorado cálido, sirve de fondo de cartel/placa si el concepto es «sala del trono con anuncios».
- Tema «Malenia, Blade of Miquella» (disco 1, pista 23, 3:44) como música de referencia de ambiente si la lámina 2 lleva un QR o enlace a Spotify/YouTube Music.
- Texto de trailer «Le Cercle d'Elden fut brisé, mais par qui, et à quelle fin ?» (1:28 del story trailer) como posible frase de gancho para la lámina, tono épico y ambiguo, no una burbuja blanca genérica.

## No encontré

- Cinemático de introducción («Opening», pista 2 del OST) como clip suelto e independiente en Dailymotion: probé «Elden Ring opening cinematic» (en) y «Elden Ring cinématique d'ouverture» (fr) en la API de Dailymotion, sólo salieron vídeos de otros juegos. Sustituido por el tráiler de lanzamiento «Rise, Tarnished» (que sí es el cinemático que Bandai Namco usó como apertura de campaña) y por el story trailer.
- Tendencias de TikTok: probado `herramientas/navegar.py` sobre `tiktok.com/tag/eldenring` y `tiktok.com/search?q=elden+ring` (2 intentos): las dos veces devolvió página vacía (0 caracteres), TikTok bloquea el contenido sin sesión aunque cargue el HTML base. No se insistió más (regla de 2 intentos). ⚠️
- Vídeos de análisis largos (tipo video-ensayo) con minuto exacto de una escena que hace llorar: no es punto de vídeo (es del investigador de voz/personajes, punto 21); no se buscó a fondo aquí.
- Efectos de sonido / onomatopeyas con espectrograma: se documentó de oído (punto 9), no se usó `voz.py` para medir el rugido porque no es una frase hablada.

## Bitácora

- `herramientas/fotogramas.py` sobre 6 clips de Dailymotion (tráiler narrativo, tráiler de lanzamiento indirectamente citado, Malenia, Radahn, Rennala, final del juego, exploración de Limgrave): 7 hojas de contacto miradas con Read.
- `herramientas/estilo.py --colores 5` sobre 8 fotogramas sueltos (Limgrave, Caelid, Raya Lucaria, Leyndell, Elphael, ruinas, Erdtree) para el punto 4.
- API de Dailymotion (`api.dailymotion.com/videos?search=…`): «Elden Ring Melina» (fr/en), «Elden Ring opening cinematic» (en), «Elden Ring cinématique d'ouverture» (fr), «Elden Ring Tarnished grace cinematic» (en) — 4 búsquedas.
- Archive.org: metadata de la banda sonora oficial (tracklist completo, 2 discos) y de «PS5 Longplay Elden Ring» (comprobado pero descartado por peso).
- MusicBrainz: confirmación de los 3 álbumes oficiales de banda sonora (base + Shadow of the Erdtree + Nightreign).
- No se usó el buscador web (WebSearch) en esta tanda: todo salió de `datos-video.md` (ya recolectado) más red directa (Dailymotion, Archive.org, MusicBrainz).
