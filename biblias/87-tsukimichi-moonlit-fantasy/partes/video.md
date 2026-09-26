# Parte de VÍDEO · Tsukimichi: Moonlit Fantasy

Investigador de vídeo (puntos 2, 4, 9, 10 y 14 de ENCARGO.md). Parte de
`datos-video.md` (AniList, Dailymotion, Internet Archive; AnimeThemes dio
522 en todos los intentos, YouTube da «Video unavailable» con el tráiler
oficial de AniList). Serie sin serie hermana declarada en este encargo.

**Fíjate especial del encargo**: comedia isekai — se nota sobre todo en el
gag recurrente del ending (misma canción, versión distinta cada temporada)
y en las pantallas de videojuego que aparecen dentro del propio anime.

Fuentes de vídeo real usadas (todas miradas fotograma a fotograma, no leídas
de reseñas):
- Tráiler oficial T1 (Dailymotion, doblado/subtitulado, canal `adorocinema`) — `fotogramas.py --cada 3`.
- Tráiler oficial T2 (Dailymotion, canal `FilmAffinity`, **audio/subtítulos en español**) — `fotogramas.py --cada 3`.
- «Highlight Moment 2024» (Dailymotion, canal The World Of Isekai - Clip): resultó ser un fragmento largo (6:35) **entero del episodio 24** (subtitulado en inglés), no un resumen — `fotogramas.py --cada 5`.
- Episodios 1, 2 y 3 completos (T1), archivos `Tsuki 1.mp4`, `Tsuki 2.mp4` y `Tsuki 3.mp4` (Internet Archive, ítem `tsuki-ga-michibiku-isekai-douchuu`, sub. español de AnimeFenix, 1920×1080) — vistos con `ffmpeg -ss` directo sobre la URL (sin bajar el archivo entero: el servidor de Internet Archive acepta *range requests*).
- Episodio 1 de la 2ª temporada completo, archivo `[SubsPlease] ...S2 - 01 (1080p)` (Internet Archive, ítem `subs-please-tsuki-ga-michibiku-isekai-douchuu-s-2-01-1080p-0316510-f.mkv`, derivado 1280×720, sub. inglés) — mismo método.
- Un tercer clip de Dailymotion resultó ser **contenido ajeno** (gameplay de un shooter con una vtuber, mal etiquetado como «episodio 5»): descartado, no se cita.

Hojas y fotogramas de trabajo en
`/tmp/claude-0/trabajo/87-tsukimichi-moonlit-fantasy-video/` (fuera del
repositorio; se borran los `video.mp4` al terminar).

## 2 · Fotogramas de escenas icónicas

**Tráiler oficial temporada 1** (voz/subtítulos en español, «Trailer Oficial», adorocinema) · https://www.dailymotion.com/video/x908684 · mirado entero cada 3 s (32 fotogramas, 0:00-1:35):
- Tsukuyomi (la diosa que resume a Makoto), silueta alada blanca de cuerpo entero, luz detrás · &t=18 · ✅ (coincide con su artwork de la wiki en imagen.md) · 0:18
- Cartel «月に導かれし彼らの旅が、今始まる» («El viaje de aquellos guiados por la luna empieza ahora») sobre paisaje de montañas · &t=39 · ✅ · 0:39
- Tomoe (pelo claro) sujetando la cara de Makoto de cerca, él grita «¡Tomoe! ¡Mio!» · &t=63-66 · ✅ · 1:03-1:06
- Créditos de reparto en japonés: 花江夏樹 (Makoto), 佐倉綾音 (Tomoe), 鬼頭明里 (Mio), dirección 石平信司 · &t=84 · ✅ (mismos nombres que en los créditos del ending de la T2, más abajo) · 1:24
- Hoja: `trailer_s1/hoja_01.jpg`.

**Tráiler oficial temporada 2, doblado/subtitulado en español** (FilmAffinity) · https://www.dailymotion.com/video/x8r9ybf · mirado entero cada 3 s (21 fotogramas, 0:00-1:00):
- «Ya pasaron muchos meses» / «espero poder cambiar», Makoto adulto hablando a cámara · &t=3-6 · ✅ · 0:03-0:06
- Logo «月が導く異世界道中 TSUKIMICHI -Moonlit Fantasy- Segunda Temporada» · &t=9 · ✅ · 0:09
- Ficha de personaje con nombre y actor: MIO 澪 (voz 鬼頭明里) diciendo «¡Viajaré por el mundo para mejorar como cocinera!»; SHIKI 識 (voz 津田健次郎) · &t=27-30 · ✅ · 0:27-0:30
- «Su misión para cambiar el mundo: 異世界世直し旅» sobre fondo de fuego · &t=36 · ✅ · 0:36
- Hoja: `trailer_s2/hoja_01.jpg`.

**Escena icónica: duelo final de Makoto contra Sofia «Lancer» Bulga, episodio 24** (clip largo de Dailymotion etiquetado «Highlight Moment 2024», en realidad el tramo final del episodio con marca de agua «EPISODE 24» en pantalla, subtítulos en inglés) · https://www.dailymotion.com/video/x9d51n2 · mirado entero cada 5 s (79 fotogramas, 0:00-6:34):
- Makoto revela su identidad real: «My real name is Misumi Makoto» (primer plano, ceja levantada) · &t=190 · ✅ (la escena coincide con el resumen de «Anime Episode 24» de la wiki) · 3:10
- Nombra su arco «Azusa»: «This weapon's name is Azusa» · &t=125 · ✅ · 2:05
- De pie sobre una plataforma de piedra en llamas, apuntando con arco, mirada tranquila en medio del combate · &t=255-315 · ✅ · 4:15-5:15
- Sofia/Lancer, piel morena con marcas tribales, furiosa, gritando «Bastard!» · &t=105 · ✅ · 1:45
- Hojas: `highlight2024/hoja_01.jpg` y `hoja_02.jpg`.
- Esta es la escena que se hizo viral en TikTok como «all he did was shoot a bow» (ver punto 10): coincide exactamente con este tramo.

**Escena icónica: Tomoe (con su nombre humano «Shin») pide que la llamen samurái, episodio 1** · `Tsuki 1.mp4` (Internet Archive) · minuto 22:00:
- Tomoe (pelo celeste, cuernos/adorno dorado, kimono rojo) guiña un ojo y dice «Prefiero que me llames samurái», con Makoto reaccionando en un recuadro azul · https://archive.org/details/tsuki-ga-michibiku-isekai-douchuu (archivo «Tsuki 1.mp4») · ✅ (el color de pelo «light blue» coincide con la ficha de Tomoe en la wiki, y la lista de personajes de «Anime Episode 01» confirma que Mio no aparece en este episodio; sólo «Shin», nombre humano provisional de Tomoe) · 22:00

**Escena icónica: contrato de sangre con Tomoe (forma de dragón), episodio 1** · `Tsuki 1.mp4` · minuto 20:00:
- Tomoe en forma de dragón (verde azulado, herida ardiente en la cabeza) protesta «¿Una herida? ¿Cómo? ¡Si soy resistente al fuego!» mientras una criatura chibi dorada la molesta y Makoto pide «Por favor, para» · ✅ (la wiki confirma que Tomoe es una dragona que se transforma en humana tras jurar lealtad a Makoto en el episodio 1) · 20:00

**Escena icónica: debut de Mio como «Araña Negra», episodio 2** · `Tsuki 2.mp4` · minuto 16:40:
- Una criatura enorme, oscura, con múltiples ojos amarillos brillando en la penumbra, se regenera mientras alguien comenta «pero si se sigue regenerando así, esto no tendrá fin» · https://archive.org/details/tsuki-ga-michibiku-isekai-douchuu (archivo «Tsuki 2.mp4») · ✅ (la lista de personajes de «Anime Episode 02» confirma el debut de «Mio, la Araña Negra»; en el episodio 2 todavía no tiene forma humana, la consigue recién en el episodio 3 junto con el nombre «Mio», según la wiki) · 16:40

## 4 · Fondos y sitios: luz y paleta medida en fotograma

Paletas sacadas con `herramientas/estilo.py` sobre fotogramas propios (1280 px), no de arte promocional:

- **Ciudad de Obitt** (calle de día, S2 ep.1, min. 2:40, `[SubsPlease] S2-01`): paleta `#E5E9E5` 20% · `#54474A` 20% · `#6F757F` 19% · `#A59089` 18% · `#C9BBAE` 18% · `#8BBEEF` 6%. Luz diurna suave, sombreado degradado, línea fina gris-marrón (`#786E6A`), saturación baja (20%), brillo alto (67%). Arquitectura entramada (tipo centroeuropea) con calles de piedra. ✅ (medido directamente)
- **Laboratorio/mazmorra subterránea con tanque verde brillante** (S2 ep.1, min. 1:40): paleta `#132D2F` 35% · `#091318` 22% · `#264E4B` 15% · `#3F8A72` 12% · `#4CC4A2` 11% · `#AFD4C5` 6%. Muy oscuro (brillo 33%), saturación media (57%), tono verde-teal dominante por la luz del tanque; poca línea de contorno. ✅ (medido)
- **Cumbre nevada de noche** (fondo del opening T2, min. 1:58): paleta `#2F56B0` 22% · `#4286CD` 21% · `#0A113E` 18% · `#183875` 16% · `#3CBCE2` 15% · `#90D0E6` 7%. Azul profundo dominante, saturación muy alta (73%) — es el fondo donde se ve a Tomoe sentada mirando las estrellas; encaja con el tono «Moonlit» (luz de luna) del título. ✅ (medido)
- Las tres paletas son de fotogramas propios, con su minuto arriba; sirven de referencia de luz/hora del día para el punto 16 (imagen).

## 9 · Música y sonido

- **Opening T1**: «Gambling» (ギャンブル), interpretada por **syudou** (productor/utaite conocido en Japón) · ✅ (wiki + créditos «オープニングアニメーション» vistos en el propio OP, `Tsuki 1.mp4` min. 1:50) · confirmado con `tsukigamichibikuisekaidouchuu.fandom.com` página «Gambling (song)».
- **Opening T2**: «Utopia» (ユートピア), interpretada por **Keina Suda** · ✅ (wiki «Utopia (song)» + créditos vistos en pantalla en `[SubsPlease] S2-01` min. 1:18-2:22, con logo «Season Two 第二幕»).
- **Ending, gag recurrente**: la misma canción, **«Aa Jinsei ni Namida Ari»** (ああ人生に涙あり, «Ah, hay lágrimas en la vida» — tema homenaje a una vieja canción de un dorama samurái), se repite con versión distinta cada tramo, cantada por los propios seiyuu **dentro del personaje**: Ver.1 T1 solo Makoto (Natsuki Hanae), Ver.2 T1 a dúo Tomoe y Mio, Ver.3 T2 a dúo Makoto y Shiki (Kenjiro Tsuda) · ✅ (wiki «Aa Jinsei ni Namida Ari (song)», confirmado también viendo el ending real de S2E1 con los créditos «BELAIR MUSIC PUBLISHING» en pantalla, min. 23:32). Es un gag de comedia: la lámina puede usar el logo redondo de la canción (el «sol»/luna en los créditos) como marco de cuadro de diálogo.
- **Ending T2, animación**: estilo *chibi* (los tres protagonistas caminando pequeños y redondeados, con un arcoíris y un sol sonriente), muy distinto del dibujo normal del anime — sólo se usa en el ending · ✅ (visto min. 22:12-23:40 de `[SubsPlease] S2-01`).
- Director de ambas temporadas: **Shinji Ishihira** (石平信司), confirmado en los créditos de OP y ED de las dos temporadas y en la wiki de episodios ✅.
- No se encontró aún el compositor de la banda sonora incidental (sólo los temas de OP/ED); ver «No encontré».

## 10 · Vídeos: tráileres, escenas y tendencias

- **Tendencia TikTok confirmada**: la escena del episodio 24 (Makoto derrotando a Sofia «Lancer» sólo con arco) circula como edit viral con el texto burlón «all he did was shoot a bow», etiquetas `#tsukimichimoonlitfantasy` `#moonlitfantasy` `#animeedit` · ✅ (coincide exactamente con el clip mirado arriba en el punto 2, min. 4:15-5:15 del clip largo) — búsqueda web «Tsukimichi Moonlit Fantasy TikTok viral clip edit».
- Otros edits de TikTok con Tomoe y Mio («Tomoe and Mio don't let nothing slide», 23.6 mil «me gusta») muestran a las dos poniendo en su lugar a aventureros arrogantes — escena de la novela ligera/manga, no localizada aún en el anime con minuto exacto ⚠️ (una fuente, sin minuto propio).
- **YouTube**: abundan vídeos de análisis y reseña en inglés («This Is What Peak Isekai Looks Like!», «Anime Review: Tsukimichi Moonlit Fantasy») y recaps largos; no se pudieron mirar por el bloqueo de YouTube desde este servidor (⚠️, sólo por título/descripción de la búsqueda, no vistos fotograma a fotograma).
- **3ª temporada**: anunciada para 2026-2027, aún sin fecha exacta ni tráiler oficial confirmado a 25-sep-2026 (estudio J.C.Staff continúa) · ⚠️ (medios de fans, sin confirmación oficial de la productora) — importante para no dar por hecho contenido de S3 que aún no existe.
- Tráileres oficiales de ambas temporadas: ver punto 2 (con minuto exacto ya citado).

## 14 · Poses analizadas por personaje

Todas de vídeo mirado con `ffmpeg`/`fotogramas.py` (episodios y tráilers de arriba), con minuto real.

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Makoto sonríe muy abierto, mano brillante alzada, cielo estrellado detrás, aceptando un trato absurdo | T1 ep. 1 | 5:00 | Animar / aceptar con humor |
| Makoto de perfil, ojos cerrados, palma extendida invocando («Brid.») | T1 ep. 1 | 12:30 | Pensar / invocar |
| Makoto de espaldas, manos abiertas, reacciona sorprendido a una criatura | T1 ep. 1 | 15:00 | Sorpresa / alerta |
| Makoto de pie sobre plataforma de piedra en llamas, apunta con arco, gesto calmado en pleno combate | T1 ep. 24 | 4:15-4:55 | Explicar con acción / combate seguro |
| Makoto primer plano serio revelando su nombre real | T1 ep. 24 | 3:10 | Explicar / revelar información |
| Makoto de perfil caminando, pensativo (opening T2) | T2 ep. 1 (OP) | 1:26-1:34 | Pensar |
| Tomoe en forma de dragón, cabeza herida, protesta indignada mientras una criatura la molesta | T1 ep. 1 | 20:00 | Regañar (en broma) |
| Tomoe humana sentada en un pico nevado, mirando las estrellas, rodillas recogidas | T2 ep. 1 (OP) | 1:58 | Pensar / momento de calma |
| Tomoe sujeta la cara de Makoto con ambas manos, de cerca | Tráiler T1 | 1:03-1:06 | Celebrar reencuentro / cercanía |
| Tomoe humana recién transformada («Shin»), pelo al viento, mano en la cabeza, mirando alrededor con curiosidad | T1 ep. 2 | 3:20 | Presentar / explicar situación nueva |
| Tomoe con un hacha al hombro, mano en la cadera, tono burlón hacia unos orcos | T1 ep. 2 | 10:00 | Explicar con autoridad / burla |
| Tomoe furiosa, marcas de enfado sobre la cabeza, boca abierta gritando, persiguiendo a Makoto | T1 ep. 2 | 20:00 | Regañar |
| Tomoe («Shin») guiña un ojo, mano cerca de la cara, sonrisa ladeada, pide que la llamen «samurái» | T1 ep. 1 | 22:00 | Explicar con humor / broma de personalidad |
| Tomoe de pie, brazos cruzados, sonrisa segura, mirando al frente (opening, junto a Mio) | T1 ep. 1 (OP) | 2:00 | Presentar / explicar con seguridad |
| Mio de pie, mano cerca del cuello de su kimono (con emblema de telaraña en el hombro), mirada seria y pensativa | T1 ep. 1 (OP) | 2:00 | Pensar |
| Mio en su forma original de Araña Negra, múltiples ojos amarillos brillando en la oscuridad, regenerándose | T1 ep. 2 | 16:40 | Alerta / amenaza (antes de tener forma humana) |
| Mio ya humana, pelo oscuro corto, adorno rojo, expresión serena junto a Tomoe (viñeta circular del ending) | T1 ep. 3 (ED) | 23:20 | Presentar (primera vez en forma humana) |
| Trío Makoto-Tomoe-Mio riendo juntos dentro de la viñeta circular de la luna (ending) | T1 ep. 3 (ED) | 23:30 | Celebrar / cierre alegre en grupo |
| Trío Makoto-Tomoe-Mio caminando de espaldas, en *chibi*, bajo un sol sonriente (ending) | T2 ep. 1 (ED) | 22:20-23:30 | Celebrar / cierre alegre en grupo |

## Lo mejor para la lámina

- El gag del ending «Aa Jinsei ni Namida Ari»: mismo tema, versión distinta por personaje cada temporada — un cuadro de diálogo circular (como el «sol» de los créditos) queda muy propio de la serie.
- La paleta azul profunda de la cumbre nevada del opening (`#2F56B0`/`#0A113E`) es la más «Moonlit Fantasy» de las tres medidas: sirve de fondo nocturno para cualquier lámina de este canal.
- La pose de Makoto de pie en la plataforma de fuego apuntando con el arco (ep. 24, 4:15) es la escena que se hizo viral en TikTok: puede ser la imagen de acción principal.
- El guiño de Mio pidiendo que la llamen «samurái» (ep. 1, 22:00) es su gesto de personalidad más citable y gracioso, mejor que una pose neutra.
- La ciudad de Obitt (día, calles entramadas, paleta clara y cálida) es el fondo «cotidiano» más reutilizable para textos largos del canal.

## No encontré

- Compositor de la banda sonora incidental (sólo se confirmaron los temas de OP/ED) — búsquedas: wiki de canciones, «Tsukimichi soundtrack composer» (web, en español e inglés). Sería un dato para el investigador de voz/texto si tiene tiempo.
- Onomatopeyas o efectos de sonido propios de la serie con minuto exacto — no se encontró un artículo o clip que los liste; se necesitaría ver más episodios completos.
- El opening y ending de la temporada 1 completos sin marca de agua ni subtítulos superpuestos (AnimeThemes caído con 522 en cuatro intentos a lo largo de la sesión; YouTube da «Video unavailable» en el tráiler y pide login en las búsquedas normales).
- Minuto exacto en el anime de la escena viral «Tomoe y Mio ponen en su lugar a aventureros arrogantes» (parece ser de la novela ligera o el manga, no confirmada en el anime).
- Fecha y tráiler oficial de la temporada 3 (aún no confirmados por la productora a fecha de hoy).

## Bitácora

- Dailymotion (API directa `api.dailymotion.com/videos?search=`), español/inglés/japonés: «Tsukimichi opening full», «月が導く異世界道中 OP», «TSUKIMICHI Moonlit Fantasy OP1», «Tsuki ga Michibiku Isekai Douchuu ED1», «月が導く異世界道中 ED» — sin un OP/ED limpio propio; sí sirvieron los tráilers ya usados en `datos-video.md`.
- `api.animethemes.moe` (dos rutas, `/anime?filter...` y `/search?q=`): error 522 las dos veces.
- YouTube: tráiler de AniList (`U8T63kIny7E`) → «Video unavailable» con yt-dlp.
- Internet Archive: `archive.org/metadata/<id>` para ver los archivos de vídeo reales de dos ítems (`tsuki-ga-michibiku-isekai-douchuu`, `subs-please-...-s-2-01-...`); frames sacados con `ffmpeg -ss <seg> -i <URL directa>` (usa *range requests*, no hace falta bajar el episodio entero).
- `tsukigamichibikuisekaidouchuu.fandom.com/api.php` (búsqueda de texto y `action=query&prop=revisions` sobre wikitexto): episodios 1, 5 y S2E1 para confirmar título, fecha, OP/ED y personajes; páginas «Gambling (song)», «Utopia (song)», «Aa Jinsei ni Namida Ari (song)».
- MusicBrainz (`musicbrainz.org/ws/2/release` y `/work` y `/recording`, query «Tsuki ga Michibiku Isekai Douchuu», «Gambling Tsukimichi», «Utopia Tsukimichi»): resultados genéricos sin relación real, no se usó nada de aquí (mejor la wiki, que sí tenía las fichas exactas).
- WebSearch (inglés): «Tsukimichi Moonlit Fantasy TikTok viral clip edit», «Tsukimichi Moonlit Fantasy YouTube analysis video explained», «Tsukimichi Moonlit Fantasy season 3 release date 2026».
- `herramientas/estilo.py` sobre 3 fotogramas propios de 1280 px para las paletas del punto 4.
- Un clip de Dailymotion descartado por no ser contenido real de la serie (gameplay de shooter con vtuber mal etiquetado); anotado arriba para que nadie lo reuse.
- Aviso de corrección propia: en un primer repaso confundí a Tomoe con Mio en dos fotogramas del episodio 1 (ambas pueden llevar tonos claros en el pelo a primera vista). Se corrigió comparando el color de pelo de la ficha de cada personaje en la wiki (Tomoe «light blue», Mio «black») y la lista oficial de «Characters in Order of Appearance» de cada episodio (Mio no aparece en el episodio 1; debuta como «Black Spider» en el 2 y consigue forma humana y nombre en el 3). La tabla del punto 14 ya queda con la atribución correcta.
