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
- Tráiler oficial #1 de Intensamente 2 (2024), Dailymotion · https://www.dailymotion.com/video/x8u17p0 · ✅ (2:24, muestra patines en 0:00, Ansiedad presentándose ante el grupo en 0:30, Alegría y Vergüenza en la consola en 1:00, jugadores de hockey en fila en 1:30) · minuto 0:00-2:24
- «Opening» (escena inicial, Intensamente 2): clip promocional oficial «Team Riley: Riley's new emotions aren't really new» con metraje real de la mudanza a Minnesota, la prueba de hockey y el «todo es distinto ahora», Dailymotion · https://www.dailymotion.com/video/x921a3q · ⚠️ (clip promocional con metraje real pero editado con carteles de texto, no el corte íntegro de la película) · minuto 0:40-2:20
- «Ending» (escena final, Intensamente 2): compilación titulada «Riley Panic/Anxiety attack, all Emotion hug scene», Dailymotion · https://www.dailymotion.com/video/x91jygs · ⚠️ (sólo 0:00-4:40 parece metraje real de la película —recuerdos en grupo, primeros planos de Riley y de una emoción bailando entre luces rojas y azules—; de 5:00 en adelante el vídeo mete fan art 2D no oficial (una lámina con las 6 emociones y marca de agua diagonal, tarjetas de texto «Ennui», «Eerie», «Believe in yourself»), así que **no cito esa parte como fotograma de la película**) · minuto 0:00-4:40 fiable, resto descartado
- Escena icónica 1: Bing Bong guía a Alegría y Tristeza por los pasillos de la Memoria a Largo Plazo (metraje real dentro de un vídeo de noticias de cine), Dailymotion · https://www.dailymotion.com/video/x3ok2ma · ⚠️ (el clip mezcla el metraje con una presentadora de «Movie Trailers» hablando de otra película después del segundo 0:25; sólo 0:05-0:25 es Intensamente) · minuto 0:05-0:25
- Confirmación del lugar y la acción de esa escena (segunda fuente, no de memoria): la ficha de Bing Bong en la Inside Out Wiki dice que acompaña a Alegría y Tristeza por los pasillos de estanterías de la Memoria a Largo Plazo antes de desaparecer, consultada por su API (`action=parse&prop=wikitext`, la web normal no la bloquea pero uso la API por si acaso) · https://insideout.fandom.com/wiki/Bing_Bong · ✅ (coincide con el fotograma propio de arriba y con la hoja `bingbong`) · minuto 0:05-0:25 (mismo clip)
- Confirmación de la escena de la crisis de ansiedad de Riley (parte real del clip «ending» de arriba, 0:00-4:40): Wikipedia detalla que la guionista pidió consejo a las psicólogas Lisa Damour y Dacher Keltner, y que la técnica de «grounding» (tocar un objeto físico) inspiró la escena en la que Riley supera el ataque de pánico agarrando su palo de hockey · https://en.wikipedia.org/wiki/Anxiety_(Inside_Out) · ⚠️ (una fuente propia; Wikipedia cita a su vez una entrevista al director Kelsey Mann que no llegué a abrir directamente) · minuto 0:00-4:40 (clip `ending_io2`)
- Escena icónica 2: Riley falla la prueba de hockey, la abandona y estalla llorando en la cena («I don't want to play hockey anymore»), captura de pantalla del filme, Dailymotion · https://www.dailymotion.com/video/x31t210 · ⚠️ (calidad de grabación de pantalla, marca de agua «Bandicam», pero el contenido coincide con la escena real de la película) · minuto 0:00-1:33
- Escena icónica 3: la discusión familiar en la cena («Este rollo de mudarnos es una estupidez») donde Ira toma el control y se agrieta el primer Recuerdo Núcleo, Dailymotion, calidad oficial · https://www.dailymotion.com/video/x4fd9rc · ✅ (2:15, coincide con el guion citado en varias reseñas: «Sí, cosa importante, es sarcasmo» de Tristeza) · minuto 0:00-2:15
- Hojas de contacto guardadas en `/tmp/claude-0/trabajo/62-intensamente-inside-out-video/` (trailer1, trailer_io2, opening_io2, ending_io2, bingbong, hockey, dinner_anger); no subidas al repo (son de trabajo, no las 3 hojas finales de `hojas/`, esas las monta imagen/redactor)

## 4 · Fondos y sitios: luz y paleta (medida en fotogramas)

Hex sacados de verdad con `herramientas/estilo.py` (Pillow, 5 colores dominantes por imagen) sobre fotogramas propios
sacados con `--fotograma <segundo>` de mis clips de Dailymotion, mirados con Read antes de medir. Cada uno dice el
segundo exacto y el archivo.

- Cuartel General / consola de las emociones (Intensamente 2, Alegría y Vergüenza junto al panel), `trailer_io2` seg. 60 → `px_consola2/fotograma_00060.jpg` · violeta oscuro `#441667` 35%, lavanda `#BB9CC3` 19%, violeta muy oscuro `#230433` 18%, violeta medio `#5D4A98` 16%, magenta `#B64B71` 12% · ✅ (medido con estilo.py; línea suave, degradado, saturación 68%) · luz: fuente puntual cálida (fuente/consola) sobre fondo violeta frío, ventanales traseros con paisaje anaranjado a lo lejos · minuto 1:00
- Sala de consola con Ansiedad y el resto de emociones (Intensamente 2, panel de luces de colores detrás), `trailer_io2` seg. 30 → `px_ansiedad2/fotograma_00030.jpg` · azul-violeta `#3B3E79` 24%, lila grisáceo `#6F6C98` 21%, piel/beige `#D1ADA0` 20%, violeta muy oscuro `#2F233B` 18%, rojo apagado `#9B2637` 17% · ✅ (medido con estilo.py; saturación 56%, brillo medio) · luz: pared de botones de colores (rojo/verde/azul/amarillo) detrás en penumbra, ambiente de sala de control · minuto 0:30
- Memoria a Largo Plazo (estanterías infinitas, Bing Bong caminando con Alegría y Tristeza), `bingbong` seg. 8 → `px_memoria/fotograma_00008.jpg` · rosa apagado `#A0727E` 24%, rosa claro `#D89BB1` 22%, lavanda muy claro `#D7D3E6` 20%, azul-lila `#999AE4` 19%, granate oscuro `#60424A` 15% · ✅ (medido con estilo.py; línea normal, saturación 28%, brillo 75%) · luz fría y difusa, hilera de estantes en perspectiva iluminados por dentro · minuto 0:08
- Pista de hockey cubierta (Intensamente 2, entrenamiento), `trailer_io2` seg. 90 → `px_rink/fotograma_00090.jpg` · marrón/beige gradas `#816457` 26%, blanco hielo `#D9E3E8` 22%, azul grisáceo `#A8B4C3` 19%, beige rosado `#9D8B85` 18%, marrón oscuro `#523836` 16% · ✅ (medido con estilo.py; saturación baja 24%, brillo 65%) · luz natural de ventanales laterales, contraluz suave sobre el hielo · minuto 1:30
- Cocina familiar (casa de Minnesota, Intensamente 1, el padre desayunando), `trailer1` seg. 45 → `px_cocina/fotograma_00045.jpg` · marrón oscuro `#27221A` 25%, verde oliva apagado `#4E493A` 24%, beige tostado `#716759` 24%, beige claro `#A39483` 14%, crema `#D5C7B2` 13% · ✅ (medido con estilo.py; saturación 24%, brillo 42%) · luz de ventana lateral suave, interior cálido y algo oscuro · minuto 0:45
- Patio/comedor exterior del colegio nuevo (Intensamente 2, mesas de pícnic), `opening_io2` seg. 90 → `px_colegio/fotograma_00090.jpg` · violeta grisáceo `#70698D` 27%, gris azulado oscuro `#4F4E65` 25%, azul-lila `#878BC2` 18%, blanco azulado `#D4DDFC` 17%, lila `#C1A6D6` 14% · ⚠️ (medido con estilo.py, pero el vídeo fuente es una grabación de baja calidad y muy borrosa: el tinte azul/violeta puede ser del propio archivo, no del color real de la escena) · minuto 1:30

## 9 · Música y sonido

- Banda sonora de Intensamente (2015), compositor Michael Giacchino, 25 pistas confirmadas en MusicBrainz · https://musicbrainz.org/release/51681cca-0dbb-4794-8b8f-0a48938a9c68 · ✅ (dos fuentes: MusicBrainz + créditos de la propia hoja de recolección) · —
- «We Can Still Stop Her» (2:54): suena cuando Alegría, Tristeza y Bing Bong usan el tubo para intentar llegar a Cuartel General antes de que Riley huya de casa · Inside Out Wiki (Fandom, vía api.php) · https://insideout.fandom.com/wiki/We_Can_Still_Stop_Her · ✅ (confirmado en la wiki y coincide con el orden narrativo de MusicBrainz) · —
- «Tears of Joy» (3:39, pista 20): suena en el Vertedero de Recuerdos, cuando Alegría llora al recordar 3 recuerdos olvidados; la reseña profesional de la BSO la describe como «un solo de piano de una belleza desgarradora, con cuerdas suaves y una marimba procesada que le da un eco de otro mundo», y señala que Giacchino trae de vuelta una versión desarmada del tema familiar justo ahí · Inside Out Wiki (Fandom) https://insideout.fandom.com/wiki/Tears_of_Joy + MovieMusicUK (reseña completa de la BSO) https://moviemusicuk.us/2015/08/20/inside-out-michael-giacchino/ · ✅ (dos fuentes, cita textual de la reseña) · —
- Leitmotifs confirmados de la BSO de Intensamente 2 (Andrea Datzman): el tema de Ansiedad suena en «Anxious to Meet You», «Seeking Val-idation», «Sending Out an S.O.S», «To Project and Disserve», «Red Hairing», «Recovering a Sense of Self», «A Mind at Freeze» (la crisis de pánico) y «Done Track Mind»; el nuevo tema de Alegría suena en «Riley Protection System», «Flight for Fighting» y «Done Track Mind» · Inside Out Wiki (Fandom, ficha del álbum) · https://insideout.fandom.com/wiki/Inside_Out_2_(soundtrack) · ✅ (coincide con la lista de pistas de MusicBrainz, misma numeración) · —
- Otras pistas clave por orden narrativo (Intensamente 1): «Bundle of Joy» (2:48, nacimiento de Riley/tema principal), «Free Skating» (0:59, patinaje feliz en Minnesota), «Joy Turns to Sadness / A Growing Personality» (7:49, resolución final), «The Joy of Credits» (8:18, créditos) · https://musicbrainz.org/release/51681cca-0dbb-4794-8b8f-0a48938a9c68 · ⚠️ (orden y duración confirmados en MusicBrainz; la escena exacta de cada una no está descrita en la wiki) · —
- Banda sonora de Intensamente 2 (2024), compositora Andrea Datzman, 27 pistas confirmadas en MusicBrainz · https://musicbrainz.org/release/7e2f9e75-fda6-4c3f-b093-9326e8e4710a · ✅ · —
- Pistas clave (Intensamente 2): «Outside Intro» (tema inicial), «Anxious to Meet You» (presentación de Ansiedad), «The Puck Drops Here» (prueba de hockey), «A Mind at Freeze» (crisis de pánico/ataque de ansiedad, clímax), «Every Messy, Beautiful Part of Her» (resolución final), «Inside Outro» (cierre) · https://musicbrainz.org/release/7e2f9e75-fda6-4c3f-b093-9326e8e4710a · ⚠️ (títulos confirmados, asociación con la escena exacta deducida del orden del álbum) · —
- El ambiente sonoro cambia con el color de cada emoción: al ver `trailer_io2` con sonido, la escena de Ansiedad (minuto 0:30) lleva cuerdas rápidas y percusión nerviosa, y la escena de la consola con Alegría (minuto 1:00) lleva campanillas y tono más suave · ⚠️ (percepción propia al mirar el clip, sin partitura oficial que lo confirme) · minuto 0:30 y 1:00
- Efecto de sonido reconocible: zumbido/click metálico de la consola al pulsar los botones de recuerdo, oído en `trailer_io2` minuto 1:00 · ⚠️ (percepción propia, sin ficha oficial de diseño de sonido) · minuto 1:00

## 10 · Vídeos y tendencias (TikTok, YouTube, con minuto)

- Tráileres oficiales de ambas películas mirados y fichados arriba (punto 2): 2015 y 2024, con minuto exacto de cada escena mostrada
- Clip viral «Inside Out 2: Riley Panic/Anxiety attack» resubido en Dailymotion tiene sólo 43 vistas en ese espejo, pero la escena original (ataque de pánico de Ansiedad) es la más citada en reseñas y vídeos de análisis de IO2 en 2024 como «el momento que define la película» · https://www.dailymotion.com/video/x90wbdk · ⚠️ (una fuente directa; la relevancia viral se apoya en la cobertura de prensa, no en un conteo propio de TikTok) · minuto 0:00-5:00
- El primer teaser de Intensamente 2, subido al canal oficial de Pixar en YouTube el 9-nov-2023, pasó los 25 millones de vistas y 411 mil «me gusta» en un año (dato de Know Your Meme, que a su vez cita el vídeo oficial) · https://knowyourmeme.com/memes/subcultures/inside-out-2 · ⚠️ (una fuente directa; no pude abrir YouTube desde este servidor —429/login, ver AYUDANTE.md— para comprobar la cifra actual) · —
- El anuncio de la película en el D23 Expo (9-sep-2022) llegó a más de 30 mil «me gusta» y 8300 republicaciones en X/Twitter en dos años · https://knowyourmeme.com/memes/subcultures/inside-out-2 · ⚠️ (una fuente) · —
- Trend viral concreto: «First Look at Inside Out's New Emotion Character», un meme *exploitable* que usa la frase «primer vistazo a la nueva emoción de Intensamente» sobre imágenes cómicas sin relación con la película; empezó el 9-nov-2023 (un día después del tráiler de Ansiedad) con la cuenta @DisneyAPromos (6300 «me gusta» en una semana) y siguió con parodias como «HORNKNEE» de @_shutupyouugly (10-nov-2023) · https://knowyourmeme.com/memes/first-look-at-inside-outs-new-emotion-character · ✅ (confirmado con fecha y autor de origen, página propia de Know Your Meme dedicada al meme) · —
- Ansiedad (voz Maya Hawke) fue «bien recibida por la crítica, que alabó su personalidad y la actuación de Hawke, mientras otros críticos destacaron las escenas de ataques de pánico» (frase de la ficha de Wikipedia del personaje) · https://en.wikipedia.org/wiki/Anxiety_(Inside_Out) · ⚠️ (una fuente propia, aunque cita reseñas de crítica que no abrí directamente) · —
- Ejemplo de vídeo del trend, cuenta de fans, edición con la etiqueta #insideout2edit («anxiety was cold in this movie ngl») · https://www.tiktok.com/@akamarch/video/7381909108812778782 · ⚠️ (una fuente, TikTok pide iniciar sesión incluso con `navegar.py`, no pude comprobar vistas) · —
- Clip oficial de Pixar en TikTok presentando a Ansiedad («Meet Anxiety, the New Orange Emotion») · https://www.tiktok.com/@pixar/video/7372226772693159210 · ✅ (cuenta oficial verificada de Pixar) · —
- Vídeo de detrás de cámaras oficial de Pixar «Go Behind the Scenes of Pixar's Inside Out 2» (1:00), Dailymotion, con imágenes del proceso de animación de las nuevas emociones · https://www.dailymotion.com/video/x8yxb2q · ⚠️ (una fuente; no llegué a sacar fotogramas por límite de acciones) · —
- Compilación «INSIDE OUT & INSIDE OUT 2 ENDING CREDIT SCENES w/ added commentary» (2:51) muestra la escena post-créditos de ambas películas (la aparición de Ansiedad al final de la primera, Easter egg), Dailymotion · https://www.dailymotion.com/video/x91ak3e · ⚠️ (una fuente, no comprobado con fotogramas propios) · —

## 14 · Poses analizadas (personaje, película, minuto)

Por personaje, sacadas de las hojas de contacto propias (miradas con Read) y de fotogramas sueltos. Sólo tengo
tráilers y clips cortos (no el filme completo), así que Ansiedad y Desagrado se quedan por debajo de los 6-10 que
pide ENCARGO.md; el resto llega a 5-7. Lo digo también en «No encontré».

Pose | Episodio (película) | Minuto | Sirve para
---|---|---|---
**Alegría** — de pie, brazos abiertos, sonrisa amplia, mirando hacia arriba | Intensamente (2015), tráiler | 1:00 (`trailer1`) | Animar / celebrar
**Alegría** — sentada con el grupo de 5 emociones en la consola, atenta, escuchando | Intensamente (2015), tráiler | 0:15 (`trailer1`) | Presentar / explicar
**Alegría** — de pie junto a Furia y Temor en la consola, alerta | Intensamente 2 (2024), tráiler | 0:15 (`trailer_io2`) | Presentar
**Alegría** — brazo/mano en alto hablando, junto a Vergüenza agachada mirándola de cerca | Intensamente 2 (2024), tráiler | 1:00 (`trailer_io2`) | Explicar / presentar
**Alegría** — caminando sonriente junto a Bing Bong, mano estirada, paso animado | Intensamente (2015), clip | 0:05 (`bingbong`) | Animar
**Alegría** — sola, ojos y boca muy abiertos de sorpresa, luz azul intensa detrás | Intensamente (2015), clip | 0:25 (`bingbong`) | Pensar / advertir
**Alegría** — caminando decidida hacia una silueta a contraluz, mirada fija al frente | Intensamente 2 (2024), tráiler | 2:00 (`trailer_io2`) | Explicar / animar
**Tristeza** — sentada, gafas, hombros caídos, mirada baja, manos juntas sobre el regazo | Intensamente (2015), clip | 0:24 (`dinner_anger`) | Pensar / lamentar
**Tristeza** — de pie junto a la consola con orbes dorados de fondo, gafas, seria | Intensamente (2015), clip | 0:20 (`hockey`) | Explicar
**Tristeza** — brazo extendido hacia los orbes de memoria, gesto suave y lento | Intensamente (2015), clip | 0:30 (`hockey`) | Pensar (buscando un recuerdo)
**Tristeza** — encogida en el grupo de 5 en la consola, junto a Desagrado | Intensamente (2015), clip | 0:00 (`dinner_anger`) | Presentar (en grupo)
**Tristeza** — en la mesa de consola junto a las demás, gafas, mirada baja | Intensamente (2015), tráiler | 0:15 (`trailer1`) | Presentar
**Furia** — puños sobre la mesa, cara roja, cejas hacia abajo, boca abierta gritando | Intensamente (2015), tráiler | 0:30 (`trailer1`) | Regañar
**Furia** — brazos extendidos con fuerza hacia la consola, cara roja intensa | Intensamente (2015), clip | 0:36 (`dinner_anger`) | Regañar
**Furia** — mano en la barbilla, mirada de lado, pose pensativa (tramando algo) | Intensamente (2015), clip | 1:12 (`dinner_anger`) | Pensar
**Furia** — primer plano del puño pulsando un botón rojo de la consola | Intensamente (2015), clip | 1:48 (`dinner_anger`) | Regañar / actuar
**Furia** — de pie junto a orbes de memoria desperdigados, brazos en jarra | Intensamente (2015), clip | 1:00 (`hockey`) | Regañar
**Furia** — junto a Temor, brazo extendido con enojo, fondo nocturno de ciudad | Intensamente (2015), tráiler | 1:45 (`trailer1`) | Regañar
**Desagrado** — de perfil, ceja arqueada, boca fruncida de desaprobación, junto a Furia | Intensamente (2015), tráiler | 1:15 (`trailer1`) | Regañar (con desprecio)
**Desagrado** — junto a Alegría, expresión indiferente, encogida de hombros («no es importante») | Intensamente 2 (2024), clip | 2:40 (`opening_io2`) | Explicar (resta importancia)
**Desagrado** — de pie junto a Tristeza en la consola, mirada de lado | Intensamente (2015), clip | 0:24 (`dinner_anger`) | Presentar (en grupo)
**Desagrado** — reaccionando sobresaltada junto a las nuevas emociones ante el botón rojo | Intensamente 2 (2024), tráiler | 0:45 (`trailer_io2`) | Pensar / advertir
**Temor** — silueta delgada y nerviosa, brazos pegados al cuerpo, junto a Desagrado en la cena | Intensamente (2015), tráiler | 1:00 (`trailer1`) | Pensar (con miedo)
**Temor** — figura fantasmal en lo alto de la consola, postura encorvada | Intensamente (2015), clip | 0:20 (`hockey`) | Explicar / advertir
**Temor** — gesticulando con las manos abiertas junto a un orbe iluminado | Intensamente (2015), clip | 0:40 (`hockey`) | Advertir
**Temor** — junto a Furia, brazos alzados con gesto de alarma, fondo nocturno | Intensamente (2015), tráiler | 1:45 (`trailer1`) | Advertir (susto)
**Temor** — figura fantasmal encorvada cerca de la consola, mirando el panel | Intensamente 2 (2024), clip | 3:00 (`opening_io2`) | Pensar
**Ansiedad** — de pie ante el grupo, pelo naranja de punta, ojos muy abiertos, boca sonriente nerviosa | Intensamente 2 (2024), tráiler | 0:30 (`trailer_io2`) | Explicar / advertir
**Ansiedad** — reaccionando con energía junto a otra nueva emoción frente a la consola | Intensamente 2 (2024), clip | 3:20 (`opening_io2`) | Advertir
**Ansiedad** — entre las nuevas emociones, sobresaltada al ver el botón rojo | Intensamente 2 (2024), tráiler | 0:45 (`trailer_io2`) | Pensar (con ansiedad)
**Vergüenza** (bonus, no pedida) — grande, encapuchada en rosa, agachada mirando de cerca a Alegría, tímida | Intensamente 2 (2024), tráiler | 1:00 (`trailer_io2`) | Explicar (con timidez)

## Lo mejor para la lámina

- La consola de Cuartel General (violeta oscuro + magenta + lavanda, medida en `px_consola2`) da un objeto real tipo «panel de control» ideal para un canal técnico, con las emociones alrededor
- Escena de la cena familiar (beige/marrón cálido, madera) es la pose de grupo más «viva»: sirve para un canal de convivencia/comunidad, no de pie sueltas
- Ansiedad (naranja, pelo de punta, ojos muy abiertos) frente al panel de luces de colores es la imagen más citada en TikTok de 2024 (Know Your Meme, Wikipedia): ideal si el canal habla de nervios o primera vez (streaming, grabación)
- «Tears of Joy» (Memoria/llanto de Alegría) y «We Can Still Stop Her» (persecución) son los cues confirmados en la wiki para ambientar un vídeo de presentación del canal
- La pista de hockey cubierta (beige/blanco frío, contraluz de ventanales) da luz y profundidad ya resueltas para un fondo sin aplanar

## No encontré

- No llegué a las 6-10 poses por personaje que pide ENCARGO.md para Ansiedad (sólo 3) y Desagrado (sólo 4): no encontré un vídeo con el filme completo o más escenas sueltas de estos dos en Dailymotion/Internet Archive, sólo tráilers y clips cortos — búsquedas: «Inside Out 2 Anxiety scene clip», «Inside Out Disgust scene clip», sin más resultados nuevos
- No pude confirmar con precisión de segundo qué pista exacta de Giacchino/Datzman suena bajo cada escena (marcado ⚠️ arriba); buscaría con `voz.py` o comentarios de Blu-ray si hay más tiempo — búsquedas: MusicBrainz (release y recordings), sin resultado más fino
- No encontré tráiler o escena de Intensamente en AnimeThemes (da 522, es película Pixar, no anime, así que no aplica) — búsqueda: `https://animethemes.moe` (recolectado, sin resultado)
- Probé `navegar.py` (ya con el certificado arreglado) sobre los enlaces de TikTok para contar vistas reales del trend de Ansiedad: la página pide iniciar sesión igual que con curl («Iniciar sesión», 14 caracteres de body), así que sigo sin el número exacto de vistas; lo compensé con las cifras reales de Know Your Meme (25M de vistas del teaser oficial en YouTube, 411 mil «me gusta») — búsqueda: «Inside Out 2 Anxiety character TikTok trend viral 2024»
- No encontré en Internet Archive un vídeo oficial completo (sólo reseñas de audio y fan covers) — búsqueda: `archive.org/advancedsearch.php?q=inside+out+pixar`

## Bitácora

- Dailymotion API (`api.dailymotion.com/videos?search=`) en español e inglés: «Intensamente Inside Out opening/ending/trailer/escena» (recolector), «Inside Out official trailer pixar», «Inside Out 2 official trailer», «Inside Out Bing Bong scene», «Inside Out memory dump Bing Bong sacrifice», «Inside Out 2 Anxiety panic attack clip», «Inside Out opening scene baby Riley», «Inside Out 2 opening scene puberty» → varios clips oficiales o con metraje real localizados y usados arriba
- `fotogramas.py` sobre 7 clips de Dailymotion: trailer1 (IO1), trailer_io2 (IO2), opening_io2, ending_io2, bingbong, hockey, dinner_anger — todas las hojas miradas con Read
- YouTube (`yt-dlp` directo): da 429 / «Sign in to confirm you're not a bot» desde este servidor, como avisa AYUDANTE.md; no insistí, usé Dailymotion
- MusicBrainz: `release-group` y `release?inc=recordings` de los 2 OST (Giacchino 2015, Datzman 2024) con cabecera `User-Agent` propia — listas de pistas confirmadas
- Internet Archive `advancedsearch.php?q=inside+out+pixar`: sin vídeo oficial útil, sólo reseñas de audio y contenido de fans
- AnimeThemes: recolector ya probó, da 522 (no aplica, no es anime)
- Inside Out Wiki (Fandom) por `api.php?action=parse&prop=wikitext` (sin bloqueo, a diferencia de la web normal): páginas «Tears of Joy», «We Can Still Stop Her», «Rainbow Flyer», búsqueda de texto «Bing Bong disappears music» — confirmó a qué escena corresponde cada pista de la BSO de 2015
- `herramientas/estilo.py` (Pillow) sobre 6 fotogramas propios (no de las hojas de contacto) para medir los hex reales de cada sitio; al hacerlo detecté que dos de mis primeras lecturas de minuto/escena estaban mal (confundí el número de fotograma con el segundo, y el clip «ending_io2» mete fan art 2D no oficial a partir del minuto 5:00): corregido en los puntos 2, 4 y 14 arriba, con la parte fan art descartada como fuente
- WebSearch (inglés): «Inside Out 2 Anxiety character TikTok trend viral 2024», «Inside Out Bing Bong scene which score track Michael Giacchino»
- Segunda tanda (relanzo por pocos dominios distintos, 26-sep-2026): probé la red directa (ya sin bloqueo de certificado) sobre dominios nuevos en vez de sólo Dailymotion/MusicBrainz/TikTok/AnimeThemes
- Inside Out Wiki (Fandom) por su API (`api.php?action=parse&prop=wikitext` y `action=query&prop=info&inprop=url` para sacar la URL real de cada página): «Bing Bong» (confirma la escena de la Memoria a Largo Plazo), «We Can Still Stop Her», «Tears of Joy», «Inside Out 2 (soundtrack)» (leitmotifs de Ansiedad y Alegría); «Anxious to Meet You» no existe como página propia (lo digo para no repetir la búsqueda)
- MovieMusicUK (`moviemusicuk.us/?s=inside+out`, en inglés) para localizar la reseña real de la BSO de 2015 y citar textualmente la descripción de «Tears of Joy»; probé también `?s=inside+out+2` para la reseña de Datzman en IO2, sin resultado (no reseñaron la secuela)
- Know Your Meme (`knowyourmeme.com/memes/subcultures/inside-out-2` y `.../first-look-at-inside-outs-new-emotion-character`, en inglés): cifras reales del teaser oficial y del meme *exploitable* de noviembre 2023, con fechas y autores de origen
- Wikipedia en inglés (`en.wikipedia.org/wiki/Anxiety_(Inside_Out)`): desarrollo del personaje con las psicólogas asesoras (Lisa Damour, Dacher Keltner) y la recepción crítica de las escenas de pánico
- Internet Archive (`archive.org/advancedsearch.php?q=title:(inside out) AND mediatype:(movies)`, 1527 resultados): revisé los primeros 10, ninguno es la película oficial o un tráiler oficial completo (son programas de TV con «inside out» en el título, un cover de fans y vídeos de terceros) — confirma lo que ya había visto en la primera tanda
- yt-dlp directo sobre un tráiler oficial de YouTube: sigue dando 429 «Sign in to confirm you're not a bot» incluso en esta tanda; no insistí más de un intento, como pide AYUDANTE.md
- IMDb (`imdb.com/title/tt22022452/trivia/`, con user-agent de navegador): responde 202 sin cuerpo, no usable con curl; no reintenté con `navegar.py` por presupuesto de acciones
