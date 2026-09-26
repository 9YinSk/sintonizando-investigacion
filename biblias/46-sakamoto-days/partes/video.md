# Vídeo · Sakamoto Days

Investigador de vídeo (puntos 2, 4, 9, 10 y 14 de ENCARGO.md). Parte de
`partes/datos-video.md` (recolectar.py, 25-sep-2026): confirmado que AnimeThemes
está caído (522) y que el MusicBrainz trajo mucho ruido («Days» genérico); el resto
se comprobó y se amplió mirando vídeo de verdad. Sin serie hermana en este encargo.
Carpeta de trabajo (vídeos y fotogramas pesados, fuera del repo):
`/tmp/claude-0/trabajo/46-sakamoto-days-video/`.

## 2 · Fotogramas de escenas icónicas

Miradas con `fotogramas.py` (hojas de contacto cada 5-10 s, luego fotograma
suelto por ffmpeg del mismo `video.mp4` para las citadas). Techo real de
resolución: 720p (1280×720 en el opening de archive.org; 512×288 en los
reproveches de Dailymotion, que es su calidad original, no un recorte de la
herramienta) — no hay 1080p accesible sin iniciar sesión en Netflix/Crunchyroll
desde este servidor.

- Grupo de asesinos entra a la tienda de Sakamoto y Shin se arrodilla a suplicar
  «Please let Mr. Sakamoto live!» · Episodio 1 «La leyenda del asesino» (min 0:08)
  · https://www.dailymotion.com/video/x9g89je · ✅ (coincide con la sinopsis oficial
  de Netflix del ep.1 en la wiki) · 512×288
- Shin apunta con una pistola a dos manos, mirada fija, mientras un cómplice avisa
  «If you get close, he'll read your mind» (telepatía de Shin) · Episodio 1 (min 0:16)
  · https://www.dailymotion.com/video/x9g89je · ✅ (wiki: poder de Shin es la
  telepatía) · 512×288
- Sakamoto, con delantal y sangre en el hombro, se queja «For overtime…» tras
  el tiroteo: humor en medio de la acción · Episodio 1 (min 1:52-2:00)
  · https://www.dailymotion.com/video/x9g89je · ✅ (mirado dos veces, encaja con
  el tono cómico que describen las reseñas) · 512×288
- Opening 1 «Hashire Sakamoto»: dos siluetas (Sakamoto y Shin) caminan hacia el
  atardecer en un cruce de calle, plano final del OP · min 1:25
  · https://archive.org/details/sakamoto-days-op-1 · ✅ (vídeo + créditos del
  mismo OP dan «Vaundy» como intérprete, doblemente confirmado con la wiki) · 1280×720
- Tráiler oficial Netflix (FR): Sakamoto y Shin se abrazan, «Salut, Sakamoto» ·
  min 1:15 · https://www.dailymotion.com/video/x9c6rxi · ✅ (mismo tráiler
  circula también en inglés, mismo instante) · 512×288
- Tráiler Parte 2: silueta cae desde una torre con humo y escombros, «Un père
  doit se montrer ferme» · min 1:17 · https://www.dailymotion.com/video/x9k1124
  · ⚠️ (una fuente; no identifiqué con certeza qué personaje cae) · 512×288

## 4 · Fondos y sitios: luz y paleta

Paleta medida con Pillow (`quantize` a 6 colores) sobre fotogramas sueltos
sacados con ffmpeg del mismo `video.mp4` que descargó `fotogramas.py`. Texturas
reales equivalentes de ambientcg.com, con licencia CC0.

- **Skyline al amanecer** (plano de apertura del OP, tejados y antenas a
  contraluz) · #231E1C, #F9F5DC, #404749, #586B70 · medido en fotograma 0:00 del
  OP1 · ✅ (visto en el vídeo, hoja de contacto) · fuente:
  https://archive.org/details/sakamoto-days-op-1
- **Azotea y vías de tren al anochecer**, cielo violeta (plano de persecución
  del OP) · #3C2E4F, #715A88, #8D7AAF, #C6ACDD · medido en fotograma 0:45 del OP1
  · ✅ · misma fuente
- **Paseo junto al río**, tarde despejada, hierba y cielo muy claro ·
  #D3F2FE, #98D297, #639A79 · medido en fotograma 0:50 del OP1 · ✅ · misma fuente
- **Calle con linternas de noche** (posible acceso a un santuario, farolillos
  rojos) · #07060B, #332E30, #584736 (el marrón es el resplandor de las
  linternas) · medido en fotograma 1:00 del OP1 · ✅ · misma fuente
- **Armería/depósito de los asesinos** (pared de armas, casi sin luz, una sola
  fuente puntual) · #141422, #030109, #1F1E30 · medido en fotograma 0:32 de la
  escena de Ep.1 · ✅ (visto en vídeo) · https://www.dailymotion.com/video/x9g89je
- **Salón de la casa de Sakamoto** (sofá, luz cálida de interior, de día) ·
  #746455, #B8A99B, #EFF1E6, #FBF9E4, #F3DFCD · medido en fotograma 0:15 del
  tráiler Netflix · ✅ · https://www.dailymotion.com/video/x9c6rxi
- **La tienda de Sakamoto** (mostrador, estanterías, luz cálida de interior de
  día) · #54423E, #987E71, #B0A68E, #E6E5C7 · medido en fotograma 1:20 del
  tráiler Netflix · ✅ (visto en vídeo; es la localización central de la serie,
  también sale en la portada del volumen 1) · https://www.dailymotion.com/video/x9c6rxi
- Texturas reales equivalentes (CC0, ambientcg.com): madera clara para el
  mostrador de la tienda (`WoodFloor051`), papel/cartón para las cajas de la
  armería (`Cardboard004`), asfalto húmedo para las calles nocturnas
  (`Asphalt012`) · https://ambientcg.com/list?type=Material&q=wood ·
  https://ambientcg.com/list?type=Material&q=cardboard ·
  https://ambientcg.com/list?type=Material&q=asphalt · ⚠️ (elegidas por
  parecido visual, no bajadas ni comparadas con Pillow) · CC0

## 9 · Música y sonido

- Opening 1, «走れSAKAMOTO» (Hashire Sakamoto, «Corre, Sakamoto»), de
  **Vaundy**, usado en los episodios 1-11 · https://sakamoto-days.fandom.com/wiki/Hashire_Sakamoto
  y créditos del propio vídeo (00:14 dice «Vaundy» en pantalla) · ✅ (wiki +
  vídeo) · 1:30 versión TV
- Ending 1, «普通» (Futsū, «Normal»), de **Conton Candy**, episodios 1-11 ·
  https://sakamoto-days.fandom.com/wiki/Futs%C5%AB · ⚠️ (sólo wiki; no
  encontré el vídeo del ED en Dailymotion/Internet Archive, ver «No encontré»)
- Ending especial «Somebody help us», de Vaundy, sólo en el episodio 7 (single
  compartido con el OP1) · https://sakamoto-days.fandom.com/wiki/Somebody_help_us
  · ⚠️ (una fuente, no vi el vídeo)
- Opening 2, «Method», de **Kroi**, episodios 12-22 (parte 2) ·
  https://sakamoto-days.fandom.com/wiki/Method y confirmado en pantalla en el
  tráiler oficial de la Parte 2 («Chanson du générique de la partie 2: "Method"
  par Kroi», min 1:10) · ✅ (wiki + tráiler oficial) ·
  https://www.dailymotion.com/video/x9k1124
- Banda sonora original compuesta por **Yuki Hayashi** (林ゆうき) ·
  https://en.wikipedia.org/wiki/Sakamoto_Days y MusicBrainz (4 álbumes de OST,
  Anime original Mix vol.1-2 y Hayashi special Mix vol.1-2, 2025)
  · ✅ (Wikipedia + MusicBrainz) ·
  https://musicbrainz.org/release-group/48a2b48a-6ecb-4c01-8ad4-9a670d7ab012
- Ambiente musical: el OP alterna un synth-pop urbano y rápido (Vaundy) con
  cortes de acción silenciosos; el ED1 «Futsū» es medio tiempo, letra sobre la
  vida «normal» que Sakamoto eligió — encaja con el tono agridulce del
  personaje (ex asesino que ahora es tendero) · ⚠️ (interpretación propia del
  título y del OP visto, no de un análisis publicado)
- Efectos: en el tiroteo del ep.1 los disparos suenan secos y muy próximos
  (mezcla realista, no exagerada como otros shonen), y los golpes de Sakamoto
  llevan un «thump» grave sin música encima para remarcar su fuerza; no
  encontré una lista oficial de onomatopeyas reconocidas por el fandom para el
  anime (si las hay, están en el manga, que es del investigador de imagen/texto)
  · ⚠️ (oído en el clip del ep.1, una sola fuente)

## 10 · Vídeos: tráileres, escenas, análisis y tendencias

- Tráiler oficial Netflix (VOSTFR), 1:29 · min 0:20 mesa de comida (gag de que
  Sakamoto «engordó»), min 1:05 créditos «RUN SAKAMOTO RUN» por Vaundy, min
  1:15 abrazo Sakamoto-Shin · https://www.dailymotion.com/video/x9c6rxi · ✅
  (mismo tráiler con más vistas en la web oficial de AniList) · 73 247 522
  vistas en Dailymotion (cifra a comprobar, parece inflada para un resubido)
- Tráiler oficial Parte 2 (Netflix, VOSTFR), 1:55 · min 0:21 «Un tueur à gages
  à la retraite pris pour cible», min 1:10 «Method» por Kroi en pantalla, min
  1:38 «Partie 2 / 14 juillet» · https://www.dailymotion.com/video/x9k1124 ·
  ✅ (versión en inglés idéntica en
  https://www.dailymotion.com/video/x9ji7wi) · 512×288
- Escena del ep.1 (tiroteo en la tienda), 2:03, subtítulos en inglés ·
  https://www.dailymotion.com/video/x9g89je · ✅ (contenido verificado contra
  la sinopsis del ep.1 en la wiki) · 70 vistas (canal de recopilación, no
  oficial)
- Análisis: playlist «Sakamoto Days Fight Analysis» en YouTube (varios vídeos
  sobre coreografía de peleas) · https://www.youtube.com/playlist?list=PLwzWP6A-AbgTMlIs82AaV8sGQwKQSYCaW
  · ⚠️ (no pude abrir los vídeos, YouTube pide iniciar sesión desde este
  servidor; título y existencia confirmados por buscador web)
- Vídeo de opinión «Sakamoto Days is OVERHATED?» (ene-2025), sobre la
  recepción fría que tuvo al inicio frente al manga · https://m.youtube.com/watch?v=ViBvEgPQeYQ
  · ⚠️ (una fuente, no visto por bloqueo de YouTube)
- Resumen en español «Sakamoto Days | Resumen en 30 Minutos | PARTE 1», canal
  de recaps en español (útil para el público hispano del servidor) ·
  https://www.youtube.com/watch?v=wqrL9YbMYyQ · ⚠️ (no visto, YouTube bloqueado
  aquí; título confirmado por buscador)
- Tendencia TikTok «Shin Sonic Sway»: clips de Shin esquivando ataques
  montados sobre el remix «Sonic Sway», tendencia que varias cuentas de anime
  reutilizaron con esta escena · https://www.tiktok.com/discover/shin-sonic-sway-sakamoto-days
  · ⚠️ (la página no cargó con `navegar.py`, sin JS activo; confirmado sólo por
  el resumen del buscador web, sin cifras de vistas)
- Tendencia TikTok/edits «Nagumo & Shin» y etiqueta general `#sakamotodays` con
  numerosos edits de personajes · https://www.tiktok.com/discover/sakamoto-days-edit
  y https://www.tiktok.com/tag/sakamoto · ⚠️ (mismo motivo, sin cifras)
- Ficha técnica confirmada: estudio TMS Entertainment, dirección Masaki
  Watanabe, guion Taku Kishimoto, diseño de personajes Yō Moriyama; emisión en
  dos cours (11-ene a 22-mar-2025, y 15-jul a 23-sep-2025) en TV Tokyo ·
  https://en.wikipedia.org/wiki/Sakamoto_Days · ✅ (Wikipedia + AniList, que da
  las mismas fechas) · —

## 14 · Poses analizadas

Salen de los mismos clips mirados arriba (capítulo/vídeo y minuto) más una
ilustración oficial cuando no hay clip. Lu Wutang tiene muy poco material de
vídeo disponible sin YouTube: se avisa en «No encontré».

**Sakamoto (Taro Sakamoto)**

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| De rodillas, apoyado en el sofá, exhausto, con Shin encima como un cojín | Tráiler Netflix (dailymotion.com/video/x9c6rxi) | 0:15 | Animar/relajar (gag doméstico, contraste con el asesino que fue) |
| De pie con delantal, mano en el hombro herido, gesto resignado y cómico | Episodio 1 (dailymotion.com/video/x9g89je) | 1:52 | Explicar/quejarse con humor |
| Primer plano, cejas fruncidas tras los lentes redondos, gesto serio y quieto | Episodio 1 (dailymotion.com/video/x9g89je) | 2:00 | Pensar / regañar (mirada fija que intimida sin gritar) |
| Abrazando a Shin de frente, mano en la nuca, gesto protector | Tráiler Netflix (dailymotion.com/video/x9c6rxi) | 1:15 | Animar / celebrar el vínculo con Shin |
| Silueta a contraluz caminando hacia el atardecer junto a Shin, manos en los bolsillos | OP1 (archive.org/details/sakamoto-days-op-1) | 1:25 | Presentar (plano icónico de cierre del opening) |
| *Character sheet* oficial del anime, de pie, postura neutra, delantal y lentes | Ilustración oficial (ver `partes/imagen.md`, hoja 1 nº21) | — | Presentar (pose de referencia para modelo/base) |

**Shin Asakura**

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Arrodillado, manos juntas, cabeza baja, suplicando | Episodio 1 (dailymotion.com/video/x9g89je) | 0:08 | Animar/pedir (súplica genuina, vulnerable) |
| De pie, pistola sujeta a dos manos, mirada fija al frente | Episodio 1 (dailymotion.com/video/x9g89je) | 0:16 | Explicar (postura de combate concentrada) |
| Corriendo agachado, chispas y disparos alrededor, gesto de esquive | Episodio 1 (dailymotion.com/video/x9g89je) | 1:12 | Presentar acción (reflejos, su don es el «sexto sentido») |
| De pie con delantal verde de la tienda, brazos cruzados, gesto decidido | Tráiler Netflix (dailymotion.com/video/x9c6rxi) | 1:00 | Explicar / regañar (Shin al mando del mostrador) |
| Tumbado bocarriba sobre Sakamoto en el sofá, ojos cerrados, relajado | Tráiler Netflix (dailymotion.com/video/x9c6rxi) | 0:15 | Animar (alivio cómico) |

**Lu Wutang**

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| De pie, brazo en jarra, mirada desafiante, trenza francesa al viento | Ilustración oficial del anime (`Lu_Wutang_anime_design.png`, ver `partes/imagen.md`) | — | Presentar (única imagen grande disponible de él) |
| Retrato de perfil, ceja alzada, gesto altivo | Portrait oficial AniList (ver `datos.json`) | — | Presentar (rostro, expresión de superioridad) |

## Lo mejor para la lámina

- El OP1 completo (archive.org, 1280×720) es la mejor fuente de sitios y luz:
  da 4 ambientes distintos (amanecer urbano, atardecer violeta, río de día,
  calle nocturna con linternas) ya medidos en hex.
- El abrazo Sakamoto-Shin del tráiler (min 1:15, dailymotion.com/video/x9c6rxi)
  es la pose más cálida y menos vista en las portadas de acción: sirve para una
  lámina de bienvenida o de comunidad.
- «Hashire Sakamoto» (Vaundy) y «Method» (Kroi) dan nombre y autor reales para
  poner música de referencia si la lámina se anima o se sonoriza.
- La escena del ep.1 (tienda, min 0:08-2:00) trae 6 poses ya verificadas contra
  la sinopsis oficial: cubre solo, sin buscar más, casi toda la tabla de poses.
- Cuidado con la resolución: nada de lo mirado llega a 1080p real; si la lámina
  necesita más nitidez, usar antes las ilustraciones oficiales de
  `partes/imagen.md`, no estos fotogramas.

## No encontré

- Vídeo del ending 1 «Futsū» (Conton Candy): ni en Dailymotion («Futsu Conton
  Candy Sakamoto», «SAKAMOTO DAYS ED full», «普通 SAKAMOTO DAYS», 4 búsquedas)
  ni en Internet Archive («sakamoto days ED», «sakamoto days ending»). Sólo
  queda la ficha de la wiki (⚠️ arriba).
- AnimeThemes (openings/endings en `.webm` limpios): caído con error 522 tanto
  en `recolectar.py` como al comprobarlo yo mismo hoy.
- Clips de vídeo con Lu Wutang en acción: 3 búsquedas en Dailymotion («Sakamoto
  Days Lu Wutang scene», «Lu Wutang», mezclado en otras) sólo devolvieron
  tráileres ya usados; tampoco apareció en los 4 clips que sí miré. Se quedó
  sólo con ilustraciones.
- Cifras reales de vistas/likes de las tendencias de TikTok: `navegar.py` no
  cargó contenido (la página es 100% JavaScript) y TikTok no tiene API pública
  abierta; me quedé con lo que resume el buscador web, sin números.
- Análisis en YouTube (playlist de peleas, vídeo «is OVERHATED?», resumen en
  español): confirmé que existen por el buscador web pero no pude abrirlos
  (YouTube pide iniciar sesión desde este servidor); no reintenté en bucle,
  según la regla de dos intentos.
- Onomatopeyas reconocidas del anime (más allá de lo que oí en el clip del
  ep.1): no encontré una lista o artículo que las recoja; puede que sea más
  cosa del manga (equipo de imagen/texto).

## Bitácora

- AnimeThemes API (`api.animethemes.moe`): 522, dos veces (recolectar.py y yo)
  → descartada.
- Internet Archive: `advancedsearch.php` para OP1, Part2-OP1, «sakamoto days
  ED», «sakamoto days ending» (inglés) → 2 vídeos de OP útiles, 0 de ED.
- Dailymotion API (`api.dailymotion.com/videos?search=`): 14 búsquedas en
  inglés/francés («Sakamoto Days opening/ending/trailer/fight scene/best
  scenes/Lu Wutang/Shin ability/Futsu Conton Candy/普通 SAKAMOTO DAYS»…) →
  encontrados 1 opening completo, 2 tráileres oficiales y 1 escena real de
  ep.1; el resto eran repeticiones del mismo tráiler o vídeos ajenos a la
  serie (descartados tras comprobar el contenido con `fotogramas.py`, p. ej.
  «Sakamoto day best fight scene» de Gauravnews no es esta obra).
- Fandom `sakamoto-days.fandom.com/api.php`: búsqueda de texto «opening theme»
  y «ending theme» (inglés) → páginas Hashire Sakamoto, Futsū, Somebody help
  us, Method; wikitext de las 4 con `action=parse`; página «Episode 1» para
  confirmar la escena.
- AniList GraphQL (`graphql.anilist.co`): formato, episodios, duración.
- Wikipedia (`en.wikipedia.org/w/api.php`): extracto de «Sakamoto Days» para
  compositor, estudio, dirección y fechas de emisión (segunda fuente de la
  música y la ficha técnica).
- MusicBrainz (de `datos-video.md`): filtrado a mano; sólo 4 de 14 resultados
  eran de esta serie (el resto, ruido por el título genérico «Days»).
- `navegar.py` sobre `tiktok.com/discover/shin-sonic-sway-sakamoto-days` →
  200 pero 0 caracteres (JS), no reintentado (regla de 2 intentos).
- Buscador web (2 búsquedas, inglés): «Sakamoto Days TikTok trend viral clip
  2025», «Sakamoto Days anime analysis video YouTube minute».
- `fotogramas.py`: opening (archive.org), tráiler y tráiler parte 2 y escena
  de ep.1 (Dailymotion), cada uno con hoja de contacto mirada con `Read`.
- `ffmpeg` + Pillow (`quantize`) sobre los mismos `video.mp4` ya descargados,
  para los hex de 6 sitios/escenas.
- `yt-dlp -F` sobre el ítem de archive.org del OP1, para confirmar que 720p es
  el techo real (no hay pista de 1080p).
- `navegar.py` sobre TV Tropes (`Anime/SakamotoDays`, inglés): confirma «golden
  rule of not taking a single life» y la «Hitman Association»; no encontré ahí
  ninguna entrada sobre onomatopeyas o efectos de sonido reconocidos (puede
  seguir más abajo de lo que cargó la herramienta; no insistí más de una vez).
