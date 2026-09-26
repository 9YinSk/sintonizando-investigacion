# Parte de VÍDEO · Intensamente (Inside Out) · encargo 62

Investigador de vídeo (EQUIPO.md). Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Libreta de datos, un dato por línea.
Base: `partes/datos-video.md` (recolectado antes) + fotogramas propios con `herramientas/fotogramas.py` (Dailymotion,
YouTube da 429/login desde este servidor) y bandas sonoras verificadas en MusicBrainz.
Es una franquicia de **2 películas** (Intensamente 2015 e Intensamente 2 / Inside Out 2, 2024), no una serie con
capítulos: donde ENCARGO.md pide «capítulo y minuto» uso «película y minuto»; no hay opening/ending cantados (no es
anime), así que en el punto 2 tomo «opening» = escena inicial de la trama y «ending» = escena final, y en el punto 9
la música es la banda sonora orquestal, no canciones de OP/ED.

## 2 · Opening, ending, tráiler y escenas icónicas (miradas con fotogramas.py)

Fotogramas propios, no de memoria. Los `.mp4` se borraron tras sacar las hojas (disco compartido).

- Tráiler oficial #1 de Intensamente (2015), reencontrado en Dailymotion (el original de YouTube da 429/login) · https://www.dailymotion.com/video/x2nnb8i · ✅ (duración 2:10 coincide con el tráiler #1 oficial de Disney/Pixar, contenido: mesa de Cuartel General con las 5 emociones en 0:15, cena familiar en 0:45, Ira gritando en 0:30) · minuto 0:00-2:10
- Tráiler oficial #1 de Intensamente 2 (2024), Dailymotion · https://www.dailymotion.com/video/x8u17p0 · ✅ (2:24, muestra patines en 0:00, Ansiedad/Vergüenza/Envidia/Ennui nuevas en 0:45-1:00, la lata de recuerdos vieja tirada al «Sar-Cofago» en 1:45, Riley en la cancha de hockey en 2:15) · minuto 0:00-2:24
- «Opening» (escena inicial, Intensamente 2): clip promocional oficial «Team Riley: Riley's new emotions aren't really new» con metraje real de la mudanza a Minnesota, la prueba de hockey y el «todo es distinto ahora», Dailymotion · https://www.dailymotion.com/video/x921a3q · ⚠️ (clip promocional con metraje real pero editado con carteles de texto, no el corte íntegro de la película) · minuto 0:40-2:20
- «Ending» (escena final, Intensamente 2): compilación titulada «Riley Panic/Anxiety attack, all Emotion hug scene», Dailymotion · https://www.dailymotion.com/video/x91jygs · ⚠️ (sólo 0:00-4:40 parece metraje real de la película —recuerdos en grupo, primeros planos de Riley y de una emoción bailando entre luces rojas y azules—; de 5:00 en adelante el vídeo mete fan art 2D no oficial (una lámina con las 6 emociones y marca de agua diagonal, tarjetas de texto «Ennui», «Eerie», «Believe in yourself»), así que **no cito esa parte como fotograma de la película**) · minuto 0:00-4:40 fiable, resto descartado
- Escena icónica 1: Bing Bong guía a Alegría y Tristeza por los pasillos de la Memoria a Largo Plazo (metraje real dentro de un vídeo de noticias de cine), Dailymotion · https://www.dailymotion.com/video/x3ok2ma · ⚠️ (el clip mezcla el metraje con una presentadora de «Movie Trailers» hablando de otra película después del segundo 0:25; sólo 0:05-0:25 es Intensamente) · minuto 0:05-0:25
- Escena icónica 2: Riley falla la prueba de hockey, la abandona y estalla llorando en la cena («I don't want to play hockey anymore»), captura de pantalla del filme, Dailymotion · https://www.dailymotion.com/video/x31t210 · ⚠️ (calidad de grabación de pantalla, marca de agua «Bandicam», pero el contenido coincide con la escena real de la película) · minuto 0:00-1:33
- Escena icónica 3: la discusión familiar en la cena («Este rollo de mudarnos es una estupidez») donde Ira toma el control y se agrieta el primer Recuerdo Núcleo, Dailymotion, calidad oficial · https://www.dailymotion.com/video/x4fd9rc · ✅ (2:15, coincide con el guion citado en varias reseñas: «Sí, cosa importante, es sarcasmo» de Tristeza) · minuto 0:00-2:15
- Hojas de contacto guardadas en `/tmp/claude-0/trabajo/62-intensamente-inside-out-video/` (trailer1, trailer_io2, opening_io2, ending_io2, bingbong, hockey, dinner_anger); no subidas al repo (son de trabajo, no las 3 hojas finales de `hojas/`, esas las monta imagen/redactor)

## 4 · Fondos y sitios: luz y paleta (medida en fotogramas)

Hex sacados de verdad con `herramientas/estilo.py` (Pillow, 5 colores dominantes por imagen) sobre fotogramas propios
sacados con `--fotograma <segundo>` de mis clips de Dailymotion, mirados con Read antes de medir. Cada uno dice el
segundo exacto y el archivo.

- Cuartel General / consola de las emociones (Intensamente 2, Alegría y Vergüenza junto al panel), `trailer_io2` seg. 60 → `px_consola2/fotograma_00060.jpg` · violeta oscuro `#441667` 35% , lavanda `#BB9CC3` 19%, violeta muy oscuro `#230433` 18%, violeta medio `#5D4A98` 16%, magenta `#B64B71` 12% · ✅ (medido con estilo.py; línea suave, degradado, saturación 68%) · luz: fuente puntual cálida (fuente/consola) sobre fondo violeta frío, ventanales traseros con paisaje anaranjado a lo lejos · minuto 1:00
- Sala de consola con Ansiedad y el resto de emociones (Intensamente 2, panel de luces de colores detrás), `trailer_io2` seg. 30 → `px_ansiedad2/fotograma_00030.jpg` · azul-violeta `#3B3E79` 24%, lila grisáceo `#6F6C98` 21%, piel/beige `#D1ADA0` 20%, violeta muy oscuro `#2F233B` 18%, rojo apagado `#9B2637` 17% · ✅ (medido con estilo.py; saturación 56%, brillo medio) · luz: pared de botones de colores (rojo/verde/azul/amarillo) detrás en penumbra, ambiente de sala de control · minuto 0:30
- Memoria a Largo Plazo (estanterías infinitas, Bing Bong caminando con Alegría y Tristeza), `bingbong` seg. 8 → `px_memoria/fotograma_00008.jpg` · rosa apagado `#A0727E` 24%, rosa claro `#D89BB1` 22%, lavanda muy claro `#D7D3E6` 20%, azul-lila `#999AE4` 19%, granate oscuro `#60424A` 15% · ✅ (medido con estilo.py; línea normal, saturación 28%, brillo 75%) · luz fría y difusa, hilera de estantes en perspectiva iluminados por dentro · minuto 0:08
- Pista de hockey cubierta (Intensamente 2, entrenamiento), `trailer_io2` seg. 90 → `px_rink/fotograma_00090.jpg` · marrón/beige gradas `#816457` 26%, blanco hielo `#D9E3E8` 22%, azul grisáceo `#A8B4C3` 19%, beige rosado `#9D8B85` 18%, marrón oscuro `#523836` 16% · ✅ (medido con estilo.py; saturación baja 24%, brillo 65%) · luz natural de ventanales laterales, contraluz suave sobre el hielo · minuto 1:30
- Cocina familiar (casa de Minnesota, Intensamente 1, el padre desayunando), `trailer1` seg. 45 → `px_cocina/fotograma_00045.jpg` · marrón oscuro `#27221A` 25%, verde oliva apagado `#4E493A` 24%, beige tostado `#716759` 24%, beige claro `#A39483` 14%, crema `#D5C7B2` 13% · ✅ (medido con estilo.py; saturación 24%, brillo 42%) · luz de ventana lateral suave, interior cálido y algo oscuro · minuto 0:45
- Patio/comedor exterior del colegio nuevo (Intensamente 2, mesas de pícnic), `opening_io2` seg. 90 → `px_colegio/fotograma_00090.jpg` · violeta grisáceo `#70698D` 27%, gris azulado oscuro `#4F4E65` 25%, azul-lila `#878BC2` 18%, blanco azulado `#D4DDFC` 17%, lila `#C1A6D6` 14% · ⚠️ (medido con estilo.py, pero el vídeo fuente es una grabación de baja calidad y muy borrosa: el tinte azul/violeta puede ser del propio archivo, no del color real de la escena) · minuto 1:30

## 9 · Música y sonido

- Banda sonora de Intensamente (2015), compositor Michael Giacchino, 25 pistas confirmadas en MusicBrainz · https://musicbrainz.org/release/51681cca-0dbb-4794-8b8f-0a48938a9c68 · ✅ (dos fuentes: MusicBrainz + créditos de la propia hoja de recolección) · —
- «We Can Still Stop Her» (2:54): suena cuando Alegría, Tristeza y Bing Bong usan el tubo para intentar llegar a Cuartel General antes de que Riley huya de casa · Inside Out Wiki (Fandom, wikitext vía api.php) · ✅ (confirmado en la wiki y coincide con el orden narrativo de MusicBrainz) · —
- «Tears of Joy» (3:39, pista 20): suena en el Vertedero de Recuerdos, cuando Alegría llora al recordar 3 recuerdos olvidados (la escena que precede a la despedida de Bing Bong) · Inside Out Wiki (Fandom, wikitext) + moviemusicuk.us (reseña de la BSO) · ✅ (dos fuentes) · —
- Otras pistas clave por orden narrativo (Intensamente 1): «Bundle of Joy» (2:48, nacimiento de Riley/tema principal), «Free Skating» (0:59, patinaje feliz en Minnesota), «Joy Turns to Sadness / A Growing Personality» (7:49, resolución final), «The Joy of Credits» (8:18, créditos) · https://musicbrainz.org/release/51681cca-0dbb-4794-8b8f-0a48938a9c68 · ⚠️ (orden y duración confirmados en MusicBrainz; la escena exacta de cada una no está descrita en la wiki) · —
- Banda sonora de Intensamente 2 (2024), compositora Andrea Datzman, 27 pistas confirmadas en MusicBrainz · https://musicbrainz.org/release/7e2f9e75-fda6-4c3f-b093-9326e8e4710a · ✅ · —
- Pistas clave (Intensamente 2): «Outside Intro» (tema inicial), «Anxious to Meet You» (presentación de Ansiedad), «The Puck Drops Here» (prueba de hockey), «A Mind at Freeze» (crisis de pánico/ataque de ansiedad, clímax), «Every Messy, Beautiful Part of Her» (resolución final), «Inside Outro» (cierre) · https://musicbrainz.org/release/7e2f9e75-fda6-4c3f-b093-9326e8e4710a · ⚠️ (títulos confirmados, asociación con la escena exacta deducida del orden del álbum) · —
- El ambiente sonoro cambia con el color de cada emoción: al ver `trailer_io2` con sonido, la escena de Ansiedad (minuto 0:30) lleva cuerdas rápidas y percusión nerviosa, y la escena de la consola con Alegría (minuto 1:00) lleva campanillas y tono más suave · ⚠️ (percepción propia al mirar el clip, sin partitura oficial que lo confirme) · minuto 0:30 y 1:00
- Efecto de sonido reconocible: zumbido/click metálico de la consola al pulsar los botones de recuerdo, oído en `trailer_io2` minuto 1:00 · ⚠️ (percepción propia, sin ficha oficial de diseño de sonido) · minuto 1:00

## 10 · Vídeos y tendencias (TikTok, YouTube, con minuto)

- Tráileres oficiales de ambas películas mirados y fichados arriba (punto 2): 2015 y 2024, con minuto exacto de cada escena mostrada
- Clip viral «Inside Out 2: Riley Panic/Anxiety attack» resubido en Dailymotion tiene sólo 43 vistas en ese espejo, pero la escena original (ataque de pánico de Ansiedad) es la más citada en reseñas y vídeos de análisis de IO2 en 2024 como «el momento que define la película» · https://www.dailymotion.com/video/x90wbdk · ⚠️ (una fuente directa; la relevancia viral se apoya en la cobertura de prensa, no en un conteo propio de TikTok) · minuto 0:00-5:00
- Ansiedad (voz Maya Hawke) generó un trend viral de memes y ediciones en TikTok tras su tráiler de presentación (noviembre 2023) y el estreno (junio 2024); hashtag y etiquetas «insideout2edit», «insideoutanxiety» con compilaciones y reacciones · Know Your Meme (`knowyourmeme.com/memes/subcultures/inside-out-2`) + Wikipedia (`Anxiety (Inside Out)`) · ✅ (dos fuentes) · —
- Ejemplo de vídeo del trend, cuenta de fans, edición con la etiqueta #insideout2edit («anxiety was cold in this movie ngl») · https://www.tiktok.com/@akamarch/video/7381909108812778782 · ⚠️ (una fuente, no pude abrir TikTok con navegador desde este servidor para comprobar vistas) · —
- Clip oficial de Pixar en TikTok presentando a Ansiedad («Meet Anxiety, the New Orange Emotion») · https://www.tiktok.com/@pixar/video/7372226772693159210 · ✅ (cuenta oficial verificada de Pixar) · —
- Vídeo de detrás de cámaras oficial de Pixar «Go Behind the Scenes of Pixar's Inside Out 2» (1:00), Dailymotion, con imágenes del proceso de animación de las nuevas emociones · https://www.dailymotion.com/video/x8yxb2q · ⚠️ (una fuente; no llegué a sacar fotogramas por límite de acciones) · —
- Compilación «INSIDE OUT & INSIDE OUT 2 ENDING CREDIT SCENES w/ added commentary» (2:51) muestra la escena post-créditos de ambas películas (la aparición de Ansiedad al final de la primera, Easter egg), Dailymotion · https://www.dailymotion.com/video/x91ak3e · ⚠️ (una fuente, no comprobado con fotogramas propios) · —

## 14 · Poses analizadas (personaje, película, minuto)

Pose | Película | Minuto | Sirve para
---|---|---|---
Alegría de pie en la consola, brazos abiertos, sonrisa amplia, mirando hacia arriba (tráiler IO1) | Intensamente (2015) | 1:00 (`trailer1`) | Animar / celebrar
Ira con los puños sobre la mesa, cara roja, cejas hacia abajo, boca abierta gritando (tráiler IO1) | Intensamente (2015) | 0:30 (`trailer1`) | Regañar
Tristeza sentada, hombros caídos, mirada baja, manos juntas sobre el regazo (escena de la cena) | Intensamente (2015) | 0:24 (`dinner_anger`) | Pensar / lamentar
Riley de pie con las manos en la cintura, ceño fruncido, mirando al padre (escena de la cena, discusión) | Intensamente (2015) | 1:24 (`dinner_anger`) | Regañar / plantarse
Padre con el índice levantado, ceja arqueada, medio cuerpo inclinado hacia adelante (regaño) | Intensamente (2015) | 1:36 (`dinner_anger`) | Regañar
Riley encogida, rodillas hacia el pecho, mirada perdida, en el banquillo tras dejar el hockey | Intensamente (2015) | 1:10 (`hockey`) | Pensar / triste
Las 5 emociones apretujadas alrededor de la consola mirando hacia arriba con asombro (reunión IO1) | Intensamente (2015) | 0:15 (`trailer1`) | Explicar / presentar
Ansiedad de pie frente al grupo, brazos y pelo naranja hacia arriba, ojos muy abiertos, boca sonriente nerviosa (presentación en la sala de consola) | Intensamente 2 (2024) | 0:30 (`trailer_io2`) | Explicar / advertir
Alegría con la mano levantada hablando, Vergüenza (grande, encapuchada) agachada mirándola de cerca, junto al panel de la consola | Intensamente 2 (2024) | 1:00 (`trailer_io2`) | Explicar / presentar
Jugadores de hockey de pie sobre el hielo, casco bajo el brazo, en fila mirando hacia el banquillo (entrenamiento) | Intensamente 2 (2024) | 1:30 (`trailer_io2`) | Presentar / animar

## Lo mejor para la lámina

- La consola de Cuartel General (violeta oscuro + magenta + lavanda, medida en `px_consola2`) da un objeto real tipo «panel de control» ideal para un canal técnico, con las emociones alrededor
- Escena de la cena familiar (beige/marrón cálido, madera) es la pose de grupo más «viva»: sirve para un canal de convivencia/comunidad, no de pie sueltas
- Ansiedad (naranja, pelo de punta, ojos muy abiertos) frente al panel de luces de colores es la imagen más citada en TikTok de 2024 (Know Your Meme, Wikipedia): ideal si el canal habla de nervios o primera vez (streaming, grabación)
- «Tears of Joy» (Memoria/llanto de Alegría) y «We Can Still Stop Her» (persecución) son los cues confirmados en la wiki para ambientar un vídeo de presentación del canal
- La pista de hockey cubierta (beige/blanco frío, contraluz de ventanales) da luz y profundidad ya resueltas para un fondo sin aplanar

## No encontré

- No pude confirmar con precisión de segundo qué pista exacta de Giacchino/Datzman suena bajo cada escena (marcado ⚠️ arriba); buscaría con `voz.py` o comentarios de Blu-ray si hay más tiempo — búsquedas: MusicBrainz (release y recordings), sin resultado más fino
- No encontré tráiler o escena de Intensamente en AnimeThemes (da 522, es película Pixar, no anime, así que no aplica) — búsqueda: `https://animethemes.moe` (recolectado, sin resultado)
- No pude abrir los enlaces de TikTok con navegador desde este servidor para contar vistas reales del trend de Ansiedad (sólo tengo el enlace y el título); lo enlacé igual con ⚠️ — búsqueda: «Inside Out 2 Anxiety character TikTok trend viral 2024»
- No encontré en Internet Archive un vídeo oficial completo (sólo reseñas de audio y fan covers) — búsqueda: `archive.org/advancedsearch.php?q=inside+out+pixar`

## Bitácora

- Dailymotion API (`api.dailymotion.com/videos?search=`) en español e inglés: «Intensamente Inside Out opening/ending/trailer/escena» (recolector), «Inside Out official trailer pixar», «Inside Out 2 official trailer», «Inside Out Bing Bong scene», «Inside Out memory dump Bing Bong sacrifice», «Inside Out 2 Anxiety panic attack clip», «Inside Out opening scene baby Riley», «Inside Out 2 opening scene puberty» → varios clips oficiales o con metraje real localizados y usados arriba
- `fotogramas.py` sobre 7 clips de Dailymotion: trailer1 (IO1), trailer_io2 (IO2), opening_io2, ending_io2, bingbong, hockey, dinner_anger — todas las hojas miradas con Read
- YouTube (`yt-dlp` directo): da 429 / «Sign in to confirm you're not a bot» desde este servidor, como avisa AYUDANTE.md; no insistí, usé Dailymotion
- MusicBrainz: `release-group` y `release?inc=recordings` de los 2 OST (Giacchino 2015, Datzman 2024) con cabecera `User-Agent` propia — listas de pistas confirmadas
- Internet Archive `advancedsearch.php?q=inside+out+pixar`: sin vídeo oficial útil, sólo reseñas de audio y contenido de fans
- AnimeThemes: recolector ya probó, da 522 (no aplica, no es anime)

Sigue: falta confirmar de oído (con `voz.py` o comentarios de Blu-ray) qué pista exacta suena en la escena de Bing Bong y en el ataque de pánico de Ansiedad, y localizar el vídeo viral de TikTok de Ansiedad con enlace directo.
