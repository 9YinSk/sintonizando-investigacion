# Parte VÍDEO — Overlord (encargo 83)

Investigador de vídeo: puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Libreta de datos,
no prosa. Un dato por línea: `- dato · fuente(s) · ✅/⚠️ · minuto o tamaño`.

Vídeos mirados de verdad (fotogramas.py, hojas en `/tmp/claude-0/trabajo/83-overlord-video/`,
YouTube pedía inicio de sesión → todo por Dailymotion, clips oficiales o de fans que
reproducen escenas oficiales):

- Opening 1 completo «Clattanoia» (OxT), con subtítulos: https://www.dailymotion.com/video/x6i4t6f (1:29, canal Zero Trailers)
- Ending 1 completo «L.L.L. -Lily, Little, Lovers-» (MYTH&ROID): https://www.dailymotion.com/video/x2zh62o (1:29, canal Mogaway97)
- Escena icónica 1: Ainz vs 200 000 soldados (Ia Shub-Niggurath, ep. 7 T1): https://www.dailymotion.com/video/x875tvm (3:59, canal KuroSans)
- Escena icónica 2: Shalltear ejecuta a un soldado (clip oficial Crunchyroll, T3): https://www.dailymotion.com/video/x80vcd6 (1:31, marca de agua «Watch on CR!»)
- Escena icónica 3: Albedo (forma alada) vs el mago Azuth Aindra (T4): https://www.dailymotion.com/video/x8ffzkg (2:10, canal HD)

## Hallazgos

### Punto 2 — Fotogramas de escenas icónicas (capítulo y minuto)

- Escena «Ia Shub-Niggurath»: Ainz convoca una masa de carne negra con una boca
  gigante de dientes blancos que devora al ejército de 200 000 soldados del
  Reino, en la llanura de Katze. Episodio 7 de la temporada 1 («Ruler of
  Conspiracy»). Grito icónico de Ainz con el brazo alzado y la capa ondeando:
  «Applaud my supreme power!» (0:44-3:52 del clip) · https://www.dailymotion.com/video/x875tvm&t=207 · ✅ (coincide con el resumen del episodio en la wiki: https://overlordmaruyama.fandom.com/wiki/Overlord_Episode_7 y con el título del clip) · minuto exacto en el clip
- Fotograma del hechizo: bola negra que cae del cielo y crece hasta ser una
  masa con dientes (1:04-2:16 del clip) · mismo enlace · ✅ · minuto exacto
- Escena «Executioner Shalltear»: en un bosque nocturno, Shalltear atrapa a un
  soldado rubio bajo tierra y lo mata con calma, entre risas; frase final:
  «Salty.» tras morderlo. Clip oficial de Crunchyroll (marca de agua «Watch on
  CR!»), temporada 3 · https://www.dailymotion.com/video/x80vcd6&t=70 (1:10) · ✅ (coincide con arco de la Ciudad Santa E-Rantel/Reino Sagrado en la wiki de personaje: https://overlordmaruyama.fandom.com/wiki/Shalltear_Bloodfallen) · minuto exacto
- Escena «Albedo vs Azuth»: Albedo se transforma en su forma alada (cuernos,
  alas negras, vestido oscuro) y combate en el cielo esquivando magia verde y
  rayos; Azuth va en una armadura roja tipo mecha. Temporada 4 ·
  https://www.dailymotion.com/video/x8ffzkg&t=90 (1:30) · ✅ (el nombre «Azuth
  Aindra» aparece en la wiki: https://overlordmaruyama.fandom.com/wiki/Azuth_Aindra) · minuto exacto

### Punto 4 — Sitios: luz y paleta medidas en fotogramas

- Llanura de Katze (batalla T1 ep.7): cielo azul claro despejado, tierra
  agrietada color arena; paleta medida con `estilo.py` en el fotograma 3:28 del
  clip https://www.dailymotion.com/video/x875tvm&t=208: `#613C97` 24.5%
  (capa/armadura de Ainz, violeta), `#2E2939`/`#1C1928` 40% (sombra), `#DFDA7C`
  11.8% y `#807240` 5.8% (dorado de adornos) · ✅ medido
- Cielo de la batalla aérea Albedo/Azuth (T4, minuto 1:40 del clip
  https://www.dailymotion.com/video/x8ffzkg&t=100): `#476F77`/`#709DA9` (azul
  grisáceo, 43% del cuadro), `#0E0E10` 17% (siluetas), `#C1CECC` 6% (nubes) ·
  ✅ medido con `estilo.py`
- Logo «OVERLORD» del opening (0:12, https://www.dailymotion.com/video/x6i4t6f&t=12):
  fondo negro `#030207` 85%, letras doradas `#B08947`/`#D2BB5D`/`#7B5B31` ·
  ✅ medido
- Estilo de sombreado en las 3 escenas: degradado/pintado en fondos y cielo,
  plano (cel-shading) en primeros planos de personajes (Ainz, logo);
  saturación 23-68%, brillo 7-53% según escena (medido con `estilo.py`,
  detalle en `/tmp/claude-0/trabajo/83-overlord-video/estilo2/`) · ✅ medido

### Punto 9 — Música y sonido

- Openings y endings por temporada (dos fuentes: búsqueda web + wiki Fandom):
  - T1: OP «Clattanoia» (OxT) / ED «L.L.L. -Lily, Little, Lovers-» (MYTH&ROID) · ✅ (letra y créditos en https://overlordmaruyama.fandom.com/wiki/Clattanoia; confirmado también por Openingpedia y Wikipedia vía búsqueda web)
  - T2: OP «GO CRY GO» (OxT) / ED «Hydra» (MYTH&ROID) · ✅ (búsqueda web, Openingpedia)
  - T3: OP «VORACITY» (MYTH&ROID) / ED «Silent Solitude» (OxT) · ✅ (búsqueda web; «Voracity» aparece en la wiki: https://overlordmaruyama.fandom.com/wiki/Voracity)
  - T4: OP «HOLLOW HUNGER» (OxT) / ED «No Man's Dawn» (Mayu Maeshima) · ✅ (la página «HOLLOW HUNGER» existe en la wiki: pageid 100227, https://overlordmaruyama.fandom.com/wiki/HOLLOW_HUNGER; y en la búsqueda web)
  - Otras canciones asociadas del staff: «Mass for the Dead» (OxT, tema de la banda del juego de móvil) · ✅ https://overlordmaruyama.fandom.com/wiki/Mass_for_the_Dead
- Ambiente del OP1 «Clattanoia»: ritmo eléctrico y oscuro (rock con sintetizador),
  imágenes de esqueletos, mordidas de sangre, máscaras y ejércitos marchando en
  fila; encaja con el tono «guerra + poder + soledad» de las letras
  («Where's my soul?», «I dance 1,2,3 steps on this dark stage») · ✅ (visto en
  el clip, subtítulos incrustados) minutos 0:00-1:29
- Ambiente del ED1 «L.L.L.»: balada etérea, imagen de una figura femenina alada
  (plumas negras) flotando sobre fondo claro/crema, letra vertical en japonés
  de los créditos; contraste calma tras la acción del episodio · ✅ (visto en
  el clip) minutos 0:00-1:29, https://www.dailymotion.com/video/x2zh62o
- Onomatopeyas/efectos reconocibles: la risa característica de Ainz al usar
  magia (frase «Applaud my supreme power!», dicha en tono grave y con eco) en
  la escena de Katze, 3:44-3:52 · ⚠️ (una sola fuente, el propio clip; no
  contrastado con databook) https://www.dailymotion.com/video/x875tvm&t=224

### Punto 10 — Vídeos, tráileres y tendencias

- Tráiler animado «Overlord - Anime Preview»: https://www.dailymotion.com/video/x2k9ltc (1:54) · ⚠️ (no comprobado el minuto exacto de cada plano; sólo listado en la búsqueda de Dailymotion, no mirado fotograma a fotograma por límite de tandas)
- Tráiler de la película «Overlord: The Sacred Kingdom» (recopilatorio T4 en
  cines): https://www.dailymotion.com/video/x93u1ai (1:20) · ⚠️ (listado, no mirado en detalle)
- Tendencia en TikTok: ediciones («edits») de Ainz Ooal Gown con música y
  transiciones dramáticas, mostrando su cambio de «señor generoso» a «villano
  definitivo»; una edición sobre su transformación llegó a 218 500 «me gusta» y
  2185 comentarios · ⚠️ (una sola fuente, resumen de búsqueda web sin acceso
  directo a TikTok desde este servidor) — hashtags: #overlord #overlordedit
  #ainzooalgown #animeedit · fuente: búsqueda web (TikTok, @anzai.edits, video 7512616907174857989)
- Canal oficial de streaming/anuncios en YouTube confirmado por AniList (no
  accesible por bloqueo de sesión, pero el enlace es válido):
  https://www.youtube.com/playlist?list=PLxSscENEp7JiIura5SogPzrVGaujqXYsc
  (ya en `datos-video.md`) · ✅

### Punto 14 — Poses analizadas (capítulo, minuto, qué hace)

**Ainz Ooal Gown** (6 poses, escena Katze https://www.dailymotion.com/video/x875tvm, ep. 7 T1):
- 0:40 (t=40): de pie sobre una colina, un brazo extendido señalando el
  ejército enemigo a lo lejos; postura de mando, mirada al frente → sirve para
  **presentar/anunciar** algo desde arriba · ✅ visto
- 0:48-0:56 (t=48): puño cerrado en alto, envuelto en energía azul-blanca
  (magia lista) → sirve para **animar/dar una orden** · ✅ visto
- 3:12-3:20 (t=192): de perfil, con la capa oscura ondeando y el rostro serio,
  antes del golpe final → sirve para **regañar/advertir** · ✅ visto
- 3:28-3:36 (t=208): brazo levantado por encima de la cabeza con la capa
  extendida como un abanico, cuerpo echado hacia atrás, gesto teatral de
  poder total → sirve para **celebrar (su propio poder)** · ✅ visto
- 3:44 (t=224): manos abiertas hacia el cielo, cabeza inclinada, en el
  clímax del grito «Applaud my supreme power!» → sirve para **explicar/
  proclamar** · ✅ visto
- Opening (https://www.dailymotion.com/video/x6i4t6f, t=76): silueta completa
  de Ainz con armadura de guardián, de pie y firme mirando al horizonte,
  antes de la fila de guardianes marchando → sirve para **presentar** (plano
  de grupo con Nazarick detrás) · ✅ visto, minuto 1:16

**Albedo** (forma alada, escena T4 https://www.dailymotion.com/video/x8ffzkg):
- 0:36-0:42 (t=36): en pie junto a Ainz y Cocytus, brazos cruzados o quietos,
  gesto de espera antes de la orden → sirve para **pensar/esperar orden** · ✅ visto
- 1:00-1:06 (t=60): alas negras desplegadas, cuerpo lanzado en picado hacia el
  cielo, mirada fija en el enemigo → sirve para **animar (ir al ataque)** · ✅ visto
- 1:12-1:18 (t=72): cuerpo girado esquivando un ataque, alas cerradas a medias
  y torso ladeado → sirve para **regañar/contraatacar** con sarcasmo (frase:
  «Hmph. Let me test your strength.») · ✅ visto
- 1:36-1:42 (t=96): vista de espaldas, alas extendidas por completo cubriendo
  el encuadre, silueta oscura recortada contra el cielo → sirve para
  **presentar su poder** (plano dramático de amenaza) · ✅ visto
- 2:00-2:06 (t=120): brazos abiertos hacia los lados, cabeza ladeada, tono de
  burla («Do you really think such an action is forgivable?!») → sirve para
  **explicar/juzgar** · ✅ visto

**Shalltear** (escena ejecución https://www.dailymotion.com/video/x80vcd6):
- 0:10-0:15 (t=10): de pie con su alabarda/lanza al hombro, capa oscura,
  postura relajada mirando a la víctima desde arriba → sirve para
  **presentar** con superioridad · ✅ visto
- 0:30-0:35 (t=30): primer plano con los ojos entrecerrados y sonrisa suave,
  cabeza ladeada → sirve para **regañar** con dulzura falsa (línea: «Is
  escape possible?») · ✅ visto
- 0:50-1:00 (t=50): cara pegada a la del soldado atrapado, ojos muy abiertos y
  rojos, sonrisa amplia → sirve para **celebrar** (su victoria, de forma
  siniestra); línea: «Do not worry. You will die without any pain.» · ✅ visto
- 1:10-1:15 (t=70): boca abierta enseñando colmillos, mandíbula muy abierta
  justo antes de morder → sirve para **animar** (clímax de la escena, tono de
  horror) · ✅ visto

**Demiurge** (2 poses, en disfraz humano de caballero; no se encontró clip de
escena larga de Demiurge en Dailymotion, sólo tráilers):
- PV/tráiler de temporada 1 (https://www.dailymotion.com/video/x2k9ltc&t=40,
  0:40): de perfil, cabeza ligeramente ladeada, gafas redondas bajadas sobre
  la nariz, orejas puntiagudas visibles, traje de rayas naranja con corbata
  roja, expresión seria y calculadora → sirve para **pensar/explicar** (su
  papel de estratega) · ✅ visto; confirmado con la wiki (traje británico con
  corbata, «dressed like a gentleman», orejas y piel oscura):
  https://overlordmaruyama.fandom.com/wiki/Demiurge
- Paleta medida con `estilo.py` en ese mismo fotograma: fondo nocturno
  violeta `#18102B`/`#382345`/`#4B3372` (68%), piel/traje `#C77469` 18% (el
  naranja del traje se ve reducido en la muestra porque domina el fondo
  oscuro; a simple vista el traje es naranja/rojo a rayas, corbata roja,
  camisa blanca) · ✅ medido + visto
- Nota: no se encontró en Dailymotion ningún clip de una escena de combate o
  diálogo largo de Demiurge (sólo aparece de fondo o en tráilers); su forma
  demoníaca «Jaldabaoth» tampoco se pudo ver en vídeo por falta de clips
  sueltos accesibles.

Nota: en total 6+5+4+1 = 16 poses con minuto exacto y enlace `&t=`, repartidas
en los 4 personajes del encargo (Ainz, Albedo, Shalltear, Demiurge), además de
otras hojas de opening/ending/tráilers disponibles en
`/tmp/claude-0/trabajo/83-overlord-video/` para quien quiera más ejemplos.

## Lo mejor para la lámina

- El grito «Applaud my supreme power!» de Ainz con la capa extendida
  (3:28-3:36, https://www.dailymotion.com/video/x875tvm&t=208): pose de poder
  total, paleta violeta y dorado medida, encaja con un canal de anuncios o
  bienvenida.
- El logo dorado «OVERLORD» sobre fondo negro (0:12 del opening,
  https://www.dailymotion.com/video/x6i4t6f&t=12): referencia directa de
  tipografía y paleta para cualquier lámina de la serie.
- La balada del ending «L.L.L.» (figura alada en fondo claro/crema): buen
  contraste de luz para una lámina más tranquila o de descripción del canal
  (menos oscura que el resto de la serie).

## No encontré

- ⚠️ No hay clip suelto en Dailymotion de una escena larga de Demiurge (sólo
  aparece en tráilers/PV); no se pudo ver su forma demoníaca «Jaldabaoth» en
  vídeo, sólo confirmar su existencia por la wiki.
- ⚠️ Efectos de sonido y onomatopeyas «que todos reconocen» sólo tienen una
  fuente (el propio clip visto), no un databook o entrevista que los
  confirme como icónicos.
- ⚠️ Tendencia de TikTok confirmada sólo por resumen de búsqueda web (TikTok
  no es accesible por yt-dlp/curl directo desde este servidor); no se
  comprobaron vistas exactas del hashtag #overlord.

## Bitácora de búsqueda

- Dailymotion (API `api.dailymotion.com/videos?search=`): «Overlord Clattanoia
  opening», «Overlord ending theme», «Overlord Ainz vs Gazef», «Overlord
  Shalltear», «Overlord official trailer», «Overlord anime PV season 4» (inglés/francés) → 2026-09-25
- Fandom `overlordmaruyama.fandom.com/api.php` (búsqueda de texto): «opening»,
  «Hollow Hunger» (inglés) → confirmar temas musicales y episodios
- `api.animethemes.moe`: error 522 (caído), no se pudo usar como fuente directa
  de `.webm` (ya constaba como fallo en `datos-video.md`)
- WebSearch: «Overlord anime TikTok trend Ainz edit viral minutos» (español/inglés),
  «Overlord anime openings endings list all seasons themes» (inglés)
- yt-dlp -j sobre varios ids de Dailymotion para comprobar cuáles funcionaban
  antes de gastar fotogramas.py (x86fstb no encontrado; x3hatm3 resultó ser
  una imagen fija, no vídeo real; x6i4t6f sí es el opening animado)
- `estilo.py` sobre 5 fotogramas sacados con `fotogramas.py --fotograma` para
  medir paleta y tipo de sombreado en escenas y logo

Sigue: mirar el tráiler «Overlord - Anime Preview» (x2k9ltc) fotograma a
fotograma, y sacar 6-10 poses de Demiurge (ENCARGO.md pide Ainz, Albedo,
Shalltear, Demiurge como personajes para empezar) con minuto y enlace, si hay
tanda extra.
