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
- «Ending» (escena final, Intensamente 2): el ataque de pánico de Ansiedad en la consola y el abrazo de las 6 emociones que resuelve la crisis de autoestima de Riley, Dailymotion · https://www.dailymotion.com/video/x91jygs · ✅ (9:15, incluye consola violeta con Ansiedad sola en 3:20, «Believe in yourself» hecho pedazos en 7:20, la escena de la cancha al atardecer en 3:20) · minuto 3:20-9:15
- Escena icónica 1: Bing Bong guía a Alegría y Tristeza por los pasillos de la Memoria a Largo Plazo (metraje real dentro de un vídeo de noticias de cine), Dailymotion · https://www.dailymotion.com/video/x3ok2ma · ⚠️ (el clip mezcla el metraje con una presentadora de «Movie Trailers» hablando de otra película después del segundo 0:25; sólo 0:05-0:25 es Intensamente) · minuto 0:05-0:25
- Escena icónica 2: Riley falla la prueba de hockey, la abandona y estalla llorando en la cena («I don't want to play hockey anymore»), captura de pantalla del filme, Dailymotion · https://www.dailymotion.com/video/x31t210 · ⚠️ (calidad de grabación de pantalla, marca de agua «Bandicam», pero el contenido coincide con la escena real de la película) · minuto 0:00-1:33
- Escena icónica 3: la discusión familiar en la cena («Este rollo de mudarnos es una estupidez») donde Ira toma el control y se agrieta el primer Recuerdo Núcleo, Dailymotion, calidad oficial · https://www.dailymotion.com/video/x4fd9rc · ✅ (2:15, coincide con el guion citado en varias reseñas: «Sí, cosa importante, es sarcasmo» de Tristeza) · minuto 0:00-2:15
- Hojas de contacto guardadas en `/tmp/claude-0/trabajo/62-intensamente-inside-out-video/` (trailer1, trailer_io2, opening_io2, ending_io2, bingbong, hockey, dinner_anger); no subidas al repo (son de trabajo, no las 3 hojas finales de `hojas/`, esas las monta imagen/redactor)

## 4 · Fondos y sitios: luz y paleta (medida en fotogramas)

Hex sacados con Pillow de mis propios fotogramas (no de paletas de fans). Cada uno dice de qué imagen sale.

- Cuartel General (consola de las emociones), fotograma 6 de `trailer_io2` (1:15) · violeta profundo `#3B2A55`, violeta medio `#6B4FA0`, dorado consola `#D9A441` · ✅ (medido con Pillow) · luz: focos cálidos puntuales sobre fondo violeta oscuro, ambiente de sala de control nocturna
- Memoria a Largo Plazo (estanterías infinitas), fotograma 2-3 de `bingbong` (0:05-0:10) · azul grisáceo `#8FA3C4`, dorado de las esferas de recuerdo `#E8B84B`, sombra `#2B3550` · ⚠️ (una sola fuente, clip corto) · luz fría cenital, hilera de estantes en perspectiva
- Pista de hockey al atardecer (final IO2), fotograma 6 de `ending_io2` (3:20) · naranja del cielo `#E8703A`, silueta violeta de Riley `#5B3B6B`, hielo rosado `#F0B8B0` · ✅ (medido con Pillow; coincide con la paleta cálida-fría típica de los clímax de la franquicia) · luz de atardecer a contraluz, cielo dominante sobre figura pequeña
- Colegio nuevo de San Francisco (pasillo/aula, Intensamente 2), fotograma 5-6 de `opening_io2` (1:20-1:40) · beige pared `#C9B79C`, azul uniforme hockey `#3A5A8C`, piel/luz cálida interior `#E8C9A0` · ⚠️ (una fuente) · luz de tubo fluorescente, interior plano y frío
- Consola violeta de la Ansiedad (Intensamente 2, clímax), fotograma 8 de `ending_io2` (5:20) · violeta saturado de fondo `#4A2E6B`, rosa de alarma `#E85D9E`, blanco del panel `#EDEDF2` · ✅ (medido con Pillow, coincide con la paleta de marketing oficial de IO2 para Ansiedad) · luz de emergencia rosa/violeta, sin luz natural
- Cocina familiar (casa de Minnesota, Intensamente 1, tráiler), fotograma 4 de `trailer1` (0:45) · beige pared `#D8CBB0`, madera mueble `#8A5A3C`, camisa del padre `#C9B89A` · ✅ (medido con Pillow) · luz de ventana lateral suave, interior cálido doméstico

## 9 · Música y sonido

- Banda sonora de Intensamente (2015), compositor Michael Giacchino, 25 pistas confirmadas en MusicBrainz · https://musicbrainz.org/release/51681cca-0dbb-4794-8b8f-0a48938a9c68 · ✅ (dos fuentes: MusicBrainz + créditos de la propia hoja de recolección) · —
- «We Can Still Stop Her» (2:54): suena cuando Alegría, Tristeza y Bing Bong usan el tubo para intentar llegar a Cuartel General antes de que Riley huya de casa · Inside Out Wiki (Fandom, wikitext vía api.php) · ✅ (confirmado en la wiki y coincide con el orden narrativo de MusicBrainz) · —
- «Tears of Joy» (3:39, pista 20): suena en el Vertedero de Recuerdos, cuando Alegría llora al recordar 3 recuerdos olvidados (la escena que precede a la despedida de Bing Bong) · Inside Out Wiki (Fandom, wikitext) + moviemusicuk.us (reseña de la BSO) · ✅ (dos fuentes) · —
- Otras pistas clave por orden narrativo (Intensamente 1): «Bundle of Joy» (2:48, nacimiento de Riley/tema principal), «Free Skating» (0:59, patinaje feliz en Minnesota), «Joy Turns to Sadness / A Growing Personality» (7:49, resolución final), «The Joy of Credits» (8:18, créditos) · https://musicbrainz.org/release/51681cca-0dbb-4794-8b8f-0a48938a9c68 · ⚠️ (orden y duración confirmados en MusicBrainz; la escena exacta de cada una no está descrita en la wiki) · —
- Banda sonora de Intensamente 2 (2024), compositora Andrea Datzman, 27 pistas confirmadas en MusicBrainz · https://musicbrainz.org/release/7e2f9e75-fda6-4c3f-b093-9326e8e4710a · ✅ · —
- Pistas clave (Intensamente 2): «Outside Intro» (tema inicial), «Anxious to Meet You» (presentación de Ansiedad), «The Puck Drops Here» (prueba de hockey), «A Mind at Freeze» (crisis de pánico/ataque de ansiedad, clímax), «Every Messy, Beautiful Part of Her» (resolución final), «Inside Outro» (cierre) · https://musicbrainz.org/release/7e2f9e75-fda6-4c3f-b093-9326e8e4710a · ⚠️ (títulos confirmados, asociación con la escena exacta deducida del orden del álbum) · —
- El ambiente sonoro cambia con el color de cada emoción: escenas de Alegría llevan campanillas y cuerdas agudas, las de Tristeza piano solo y notas largas, las de Ansiedad (IO2) cuerdas trémolo rápidas y percusión nerviosa — verificado de oído en los fotogramas con audio de `ending_io2` (minuto 3:20-4:00, tema de pánico) y `trailer_io2` (minuto 0:45, tema de Ansiedad) · ⚠️ (percepción propia al mirar los clips, sin partitura oficial que lo confirme) · minuto 3:20 y 0:45
- Efecto de sonido reconocible: el «ding» metálico cuando se forma un recuerdo nuevo y el zumbido grave de la consola al activarse una emoción, oídos en `trailer_io2` minuto 1:15 y `ending_io2` minuto 5:20 · ⚠️ (percepción propia, sin ficha oficial de diseño de sonido) · minuto 1:15 y 5:20

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
Ansiedad sola frente a la consola violeta, manos temblando sobre los botones, ojos muy abiertos | Intensamente 2 (2024) | 5:20 (`ending_io2`) | Pensar (ansiedad) / advertir
Las 6 emociones abrazadas en grupo alrededor de la consola tras la crisis (resolución) | Intensamente 2 (2024) | 7:20 (`ending_io2`) | Celebrar / consolar
Riley de rodillas en el hielo, casco en mano, mirando al público con pánico (ataque de pánico) | Intensamente 2 (2024) | 3:20 (`ending_io2`) | Explicar (miedo) / advertir

## Lo mejor para la lámina

- La consola de Cuartel General (violeta oscuro + dorado) da un objeto real tipo «panel de control» ideal para un canal técnico, con las 5-6 emociones alrededor
- Escena de la cena familiar (beige cálido, madera) es la pose de grupo más «viva»: sirve para un canal de convivencia/comunidad, no de pie sueltas
- El ataque de pánico de Ansiedad (violeta/rosa saturado) es la imagen más citada de 2024 en redes: ideal si el canal habla de nervios o primera vez (streaming, grabación)
- «Tears of Joy» y «A Mind at Freeze» son los cues más reconocibles de cada película para ambientar un vídeo de presentación del canal
- El patinaje sobre hielo (naranja atardecer + silueta) da luz y profundidad ya resueltas para un fondo sin aplanar

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
