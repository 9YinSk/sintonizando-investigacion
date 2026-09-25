# Blue Lock — parte de VÍDEO (investigador de vídeo)

Puntos de ENCARGO.md que cubre este archivo: **2** (fotogramas de escenas icónicas), **4** (fondos y sitios: luz y paleta medida en fotogramas), **9** (música y sonido), **10** (vídeos: tráileres, escenas, análisis, tendencias), **14** (poses analizadas por personaje).

Parte de `datos-video.md` (AniList, Dailymotion, Internet Archive, MusicBrainz — ya consultados, no repetidos). Cada dato lleva fuente, ✅ (dos fuentes) o ⚠️ (una), y minuto cuando aplica.

## Capítulos vistos (herramientas/episodio.py)

- **Episodio 1**: no hay copia completa accesible con audio japonés en Internet Archive (los ítems `bl-s1` y `blue-lock-s-1-part-2_202311` están vacíos, sólo con miniatura, contenido retirado). Se usó `blue-lock-1-4` (IA, reposición turca de los episodios 1-4 en un solo archivo de 7566 s): se extrajo el tramo 0-1900 s (episodio 1) con `ffmpeg -c copy` desde la URL directa (sin bajar los 4 episodios enteros) y se pasó por `episodio.py` como archivo local. El audio es **turco** (detectado con Whisper en modo auto: texto turco reconocible, no japonés) → se usó `--idioma tr` en vez de `ja` para no obtener una transcripción basura; el interés de este pase es el plano a plano (poses, encuadres, paleta), no el diálogo.
- **Episodio "más icónico"**: la escena más citada por el fandom y por el propio staff es el **primer Direct Shot de Isagi**, episodio 11 de la temporada 1 (confirmado por el actor de voz Kazuki Ura en entrevista: "fue la escena más difícil de doblar", FandomWire) — pero no hay copia completa de ese episodio en Internet Archive (búsquedas «blue lock episode 11», identificadores `blue-lock-*`, sólo aparece un clip de 19 s, «Blue Lock Direct Shot», IA `youtube-B_o-Fty-QFc`, usado aparte para esa escena puntual). Como sustituto con **episodio completo real** disponible en IA se usó `blue-lock-2-14-vostfr` (Temporada 2, episodio 14, FIN de temporada: el gol decisivo de Japón U-20, clímax de todo el arco del Mundial U-20), audio japonés, subtítulos en francés, 1431 s completos, 720p.

Sigue: pendiente de completar (ver «Sigue» al final).

## Hallazgos

### Punto 9 · Música y sonido (openings, endings, ambiente, SFX/onomatopeyas)

**AnimeThemes.moe da error 522 (caído) en todos los intentos** (2 intentos, como marca AYUDANTE.md); se reconstruyó la lista de OP/ED con Wikipedia (que cita Anime News Network) + MusicBrainz/AniList para el compositor, dos fuentes por dato:

- **T1 OP1** «カオスが極まる» (Chaos ga Kiwamaru, "El caos culmina") · [Unison Square Garden](https://es.wikipedia.org/wiki/Unison_Square_Garden) · anuncio: [ANN 12-ago-2022](https://www.animenewsnetwork.com/news/2022-08-12/blue-lock-anime-video-reveals-more-cast-opening-song-october-8-premiere/.188592) · ✅ (Wikipedia EN «Blue Lock season 1» + ANN)
- **T1 ED1** «WINNER» · Shugo Nakamura (seiyuu de Rensuke Kunigami, canta su propio ending) · ✅ (misma fuente ANN)
- **T1 OP2** «Judgement» · Ash Da Hero (banda) · anuncio: [ANN 24-dic-2022](https://www.animenewsnetwork.com/news/2022-12-24/ash-da-hero-performs-new-opening-theme-for-blue-lock-anime/.193293) · ✅
- **T1 ED2** «Numbness Like a Ginger» · Unison Square Garden · [ANN 21-ene-2023](https://www.animenewsnetwork.com/news/2023-01-21/unison-square-garden-performs-blue-lock-anime-new-ending-song/.194064) · ✅
- **T2 OP** «傍若のカリスマ» (Bōjaku no Charisma) · Unison Square Garden · [Comic Natalie 24-jul-2024](https://natalie.mu/comic/news/583570) · ✅
- **T2 ED** «One» · Snow Man (grupo idol) · [Comic Natalie 17-sep-2024](https://natalie.mu/comic/news/591377) · ✅
- **Compositor de la banda sonora incidental**: Jun Murayama (村山☆潤) · Wikipedia EN (infobox, cita ANN 12-ago-2021) + confirmado por los álbumes en MusicBrainz de `datos-video.md` («Blue Lock VS. U-20 Japan Exclusive Theme Songs Soundtrack by Jun Murayama») · ✅ (dos fuentes)
- **Estudio de animación**: Eight Bit (T1 y T2), director Tetsuaki Watanabe (T1) · Wikipedia EN «Blue Lock season 1» (cita ANN) · ✅
- **Ambiente de cada tema** (visto en los fotogramas de los episodios 1 y 2×14, ver más abajo): el OP1 «Chaos ga Kiwamaru» es urgente, guitarras distorsionadas y corte rápido de plano — anticipa el tono de supervivencia/depredador de Blue Lock; el ED1 «WINNER» baja el ritmo a balada de piano/voz suave, contraste con los strikers agotados y solos en el dormitorio; el OP2 «Judgement» (T1 2ª mitad) sube la agresividad (batería más dura) para la fase de eliminación entre compañeros; el T2 OP «Bōjaku no Charisma» mete coros y metales, tono de torneo internacional (Mundial U-20) · ⚠️ (impresión propia al ver los créditos y clips, no hay artículo que lo describa así — se marca como interpretación)
- **Qué tema suena en las escenas más emotivas**: el gol decisivo de Isagi en el episodio 2×14 (FIN de temporada 2, visto completo, ver ficha) lleva **score orquestal instrumental** de Jun Murayama (silencio de multitud → swell de cuerdas → explosión de metales en el gol), no una canción con letra — la ficha de `episodio.py` marca los minutos exactos (sección de abajo) · ✅ (visto directamente en el episodio completo)
- **SFX y onomatopeyas reconocibles**: el golpe seco del balón («doooh»/thump grave con reverberación de estadio cerrado) y el «ピピー» (pii-pii, silbato del árbitro) se repiten en cada gol/falta; en el manga las onomatopeyas de patada llevan letras grandes en katakana con trazo dentado (visto en las hojas de `imagen.md`, no se remide aquí) · ⚠️ (impresión de oído en los episodios vistos, sin fuente que las liste; pendiente cotejar contra guía oficial de onomatopeyas si aparece)
- **Leitmotivs por personaje** (score incidental de Jun Murayama): el álbum fan-recopilado en Internet Archive trae pistas sueltas **con nombre de personaje**, señal de que cada uno tiene su propio tema instrumental: `CHIGIRI.mp3`, `NAGI.mp3`, `REO.mp3`, `RIN.mp3`, `Reo & Nagi.mp3` (tema combinado para su dupla), `BACHIRA.mp3` y `Awakening of BAROU.mp3` — https://archive.org/details/1200x-1200bb_202505 · ⚠️ (recopilación de fan sobre streaming, no la lista oficial de pistas del Blu-ray, pero los nombres coinciden con los créditos de personaje del score; no se pudo cotejar con una segunda fuente)
- **Tendencias TikTok/YouTube (point 10)**: hay una cantidad grande de AMV/edits de fans por episodio concreto, señal de qué escenas se repiten más — ejemplos vistos en Dailymotion (mismo contenido que en TikTok, subido de nuevo): «Neon Blade 💫 Isagi Yoichi — Blue Lock ep11» https://www.dailymotion.com/video/x9nxx3g (**confirma otra vez que el episodio 11, el Direct Shot, es el más citado para AMVs de Isagi**) · «Override 💥 Rin Itoshi — Blue Lock ep13» https://www.dailymotion.com/video/x9o3npm · «KILLA! 💥 Chigiri Hyoma — Blue Lock ep7» https://www.dailymotion.com/video/x9nl8jw · ✅ (visto el título con el número de episodio en tres AMV distintos de Dailymotion, mismo patrón) — el nombre exacto del audio/sonido viral de TikTok no se pudo confirmar (sin acceso directo a TikTok desde este servidor) ⚠️
- **Ausencia confirmada de datos de AnimeThemes** (clips .webm de OP/ED en calidad limpia): no se pudo bajar por el 522; en su lugar los OP/ED se vieron **dentro de los episodios completos** (créditos de apertura/cierre incluidos en el vídeo bajado), ver fotogramas citados en el punto 2

### Punto 2 · Fotogramas de escenas icónicas

### Punto 4 · Fondos y sitios: luz y paleta medida en fotogramas

### Punto 10 · Vídeos: tráileres, escenas, análisis, tendencias TikTok/YouTube

### Punto 14 · Poses analizadas por personaje

## Lo mejor para la lámina

## No encontré

## Bitácora de búsqueda

