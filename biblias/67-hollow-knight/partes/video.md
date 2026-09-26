# Video — Hollow Knight (puntos 2, 4, 9, 10, 14 de ENCARGO.md)

Investigador de vídeo. Hollow Knight es un videojuego, no una serie por capítulos: donde ENCARGO.md
pide «capítulo y minuto» uso zona del mapa (o tráiler) y minuto/segundo exacto del clip.
Tráilers vistos fotograma a fotograma con `fotogramas.py` (hojas de contacto en
`/tmp/claude-0/trabajo/67-hollow-knight-video/`).

## 2 · Fotogramas de escenas icónicas

Dos tráilers oficiales vistos completos con `fotogramas.py` (cada 3 s, 42 y 38 fotogramas).
Hollow Knight 1 no tiene «opening/ending» de anime: su cinemática de apertura (caída a
Hallownest) y sus finales múltiples son las escenas equivalentes; describo las más citadas.

- Tráiler original «Hollow Knight Trailer» (Team Cherry, 2017) · 2:03 · https://www.dailymotion.com/video/x89m9g8 · visto entero con fotogramas.py, hoja de contacto en `hk1_trailer/hoja_01.jpg` · ✅ (vídeo + wiki confirma escenas) · 2:03
- 0:00-0:09 - el Caballero cae y despierta en Dirtmouth/Forgotten Crossroads (créditos «Hollow Knight», «Descend into a vast, ruined world») · misma fuente · ✅ · 0:00-0:09
- 0:24 - primer vistazo al mapa en blanco (mecánica de exploración, sin brújula) · misma fuente · ✅ · 0:24
- 0:39 - pantalla de «Charms» (amuletos), inventario de Nailmaster's Glory · misma fuente · ✅ · 0:39
- 1:06 (fotograma 66 guardado en `hk1_trailer/fotograma_00066.jpg`) - el Caballero salta atacando con el clavo en medio de un enjambre de enemigos junto al altar de calaveras de Ancestral Mound, luz blanca de impacto · misma fuente · ✅ (coincide con capturas de la wiki de esa sala) · 1:06
- 1:36-1:42 - montaje de charms y un «Mask Shard» roto, seguido de un destello blanco (referencia al final «Sealed Vessel») · misma fuente · ⚠️ (interpretación propia del montaje) · 1:36-1:42
- Tráiler «Hollow Knight: Silksong - Release Trailer» (Team Cherry, sep-2025) · 1:53 · https://www.dailymotion.com/video/x9p91g8 · 501 031 vistas en Dailymotion · hoja de contacto en `silksong_lanzamiento/hoja_01.jpg` · ✅ · 1:53
- 0:03-0:06 - logo «team cherry» sobre un claro verde brillante, primer plano de Hornet con su aguja · misma fuente · ✅ · 0:03-0:06
- 0:33 (fotograma guardado en `silksong_lanzamiento/fotograma_00033.jpg`) - Hornet esquiva/ataca en el aire con estela roja, cartel «Lethal Acrobatic Action» · misma fuente · ✅ · 0:33
- 1:03-1:09 - montaje «Ferocious Foes» / «Legendary Bosses», combates contra criaturas grandes con destellos blancos de impacto · misma fuente · ✅ · 1:03-1:09
- 1:32-1:45 - logo final «Hollow Knight Silksong» en rojo sobre fondo de brasas, fecha «September 4» (lanzamiento) · misma fuente · ✅ · 1:32-1:45

## 4 · Fondos y sitios: luz y paleta medida en fotogramas

Paleta y estilo medidos con Python (extracción de color dominante + histograma de saturación/brillo)
sobre 5 capturas oficiales del juego, resolución nativa (2560×1440 o 1920×1080). Datos completos en
`/tmp/claude-0/trabajo/67-hollow-knight-video/sitios/paleta/estilo.json`. Las capturas coinciden en
resolución y nombre de serie con la galería «Screenshot HK `<zona>` NN.png» de la wiki de Fandom
(`https://hollowknight.fandom.com/wiki/Category:Screenshots`, alojadas en `static.wikia.nocookie.net`);
el número exacto de archivo no quedó registrado por el intento anterior, así que marco ⚠️ hasta confirmar el nombre exacto.

- Greenpath (bosque verde bajo Hallownest) · paleta #09192A 26%, #112C46 26%, #010203 18%, #27515F 12%, #598F82 10%, #7EE8A9 8% · brillo medio 29/100, saturación 59/100 · 62% degradado / 24% zonas planas, poca línea visible (4.8% densidad, color #0B212A) · luz: verde bioluminiscente frío sobre fondo casi negro · fuente: wiki Fandom (galería Screenshots) · ⚠️ · 2560×1440
- Deepnest (zona oscura, telarañas) · paleta #010104 27%, #394054 16%, #212A47 16%, #50505E 15%, #0F132D 13%, #73626D 13% · brillo medio 24/100 (la más oscura de las 5), saturación 36/100 (la más desaturada) · 60% degradado / 31% zonas planas · luz: casi nula, azules grisáceos apagados · fuente: wiki Fandom · ⚠️ · 1920×1080
- Fungal Wastes (hongos, esporas) · paleta #000001 51%, #040716 14%, #09122F 12%, #0F244A 10%, #183C67 7%, #1F608B 6% · brillo medio 13/100 (más oscura de todas) · 50% zonas planas / 32% degradado (más «plana» que las demás), línea más marcada (7.2%, color #060F26) · luz: negro casi total con manchas azuladas de esporas · fuente: wiki Fandom · ⚠️ · 2560×1440
- City of Tears (ciudad bajo la lluvia) · paleta #060F12 27%, #072543 26%, #1A3E6B 22%, #3C5F97 13%, #6C8EBC 9%, #D0D7E4 2% · brillo medio 35/100, saturación 70/100 (la más saturada de las 5) · 85% degradado (la más pintada/difuminada), casi sin zonas planas (4%) · luz: azul frío de lluvia constante, escaso contraste · fuente: wiki Fandom · ⚠️ · 2560×1440
- Resting Grounds (cementerio de polillas, santuario) · paleta #ABDFF6 27%, #4370A1 18%, #7CAFD3 17%, #010207 16%, #1D3568 15%, #85F1F9 8% · brillo medio 65/100 (la más clara de las 5, casi el doble que las otras) · 65% degradado / 29% plano, línea muy poca (1.9%) · luz: azul cian cálido, sensación de paz · fuente: wiki Fandom · ⚠️ · 2560×1440
- Comparativa: las 5 zonas comparten la misma técnica (fondo pintado con degradados suaves, 60-85% del área, y poquísima línea de contorno, 2-7%); lo que cambia es el brillo (Fungal Wastes 13 vs Resting Grounds 65) y la saturación (Deepnest 36 vs City of Tears 70), así se distingue cada sitio sin cambiar el estilo de dibujo · elaboración propia sobre las 5 mediciones · ✅ (patrón repetido en las 5 capturas)

## 9 · Música y sonido

Compositor: Christopher Larkin (confirmado en MusicBrainz y en las notas del álbum de Internet Archive).

- Banda sonora original «Hollow Knight» (Christopher Larkin, 2017-02-10) · https://musicbrainz.org/release-group/9df7cf82-6ea3-4021-829f-f2192977ac8d y copia completa en Internet Archive (47 306 descargas) https://archive.org/details/official-hollow-knight-original-soundtrack · ✅ (dos fuentes)
- DLC «Hollow Knight: Hidden Dreams» (2017-08-03) y «Gods & Nightmares» (2018-08-09), mismo compositor · https://musicbrainz.org/release-group/91a79b91-a98c-447c-a7b9-c40e731d8d8d · https://musicbrainz.org/release-group/b1c402a5-2595-4276-a668-ce7001f7193a · ✅
- Banda sonora «Hollow Knight: Silksong» (2025-09-04, día de lanzamiento) · https://musicbrainz.org/release-group/d34d8658-6603-449e-b691-a982ccc79116 · copia en Internet Archive https://archive.org/details/hollow-knight-silksong-ost · ✅
- Tema «City of Tears»: pulso de piano suave + voz de sirena sin letra (sólo melodía); a partir del minuto ~1:00 entran las cuerdas y una flauta en llamada-respuesta, y hacia la mitad una sola violín lleva la melodía · es el único momento de música diegética del juego (el Caballero también la «oye» dentro de la historia) · sensación: melancolía, pérdida, el único respiro «en paz» de todo el juego · fuente: https://cogconnected.com/feature/hollow-sounds-how-the-music-of-hollow-knight-tells-its-story/ y https://virtualbastion.com/2019/07/28/resonance-city-of-tears/ · ✅ (dos fuentes) · usar en escenas de la Ciudad de las Lágrimas o de duelo
- Track «City of Tears» completo en YouTube (referencia de escucha, no descarga) · https://www.youtube.com/watch?v=MJDn70jh1V0 · ⚠️ (YouTube bloqueado para bajar en este servidor, sólo enlace de referencia)
- Onomatopeya/efecto reconocible: el «tintineo» de Geo (moneda del juego) al recogerla y el golpe metálico característico del clavo (nail) al acertar un golpe crítico (llamado «S-Rank hit» por el fandom) — mencionado en foros y vídeos de análisis de sonido · ⚠️ (una fuente, común en discusiones de Reddit/foros, no verifiqué con dos fuentes independientes)
- Álbum «Hollow Knight Piano Collection» (Kara Comparetto, 2025-08-29), arreglos de piano de los temas del juego, señal de que la banda sonora tiene vida propia fuera del juego · https://musicbrainz.org/release-group/ffc63f5b-2b45-4fee-904f-a9ff48f59d71 · ✅ (release en MusicBrainz + presencia en tiendas de música, dato de catálogo)

## 10 · Vídeos: tráilers, escenas, análisis y tendencias

- Tráiler original de Hollow Knight (Team Cherry, 2017) · 2:03 · https://www.dailymotion.com/video/x89m9g8 · visto entero, ver punto 2 para minutos exactos · ✅
- Tráiler de lanzamiento de Silksong (Team Cherry, sep-2025) · 1:53 · https://www.dailymotion.com/video/x9p91g8 · 501 031 vistas en Dailymotion (la más vista de todos los clips recolectados de la obra) · ✅
- Tráiler «Voidheart Edition» (contenido gratis añadido) · 1:06 · https://www.dailymotion.com/video/x89msuk · ✅
- Gameplay «JV Legends Hollow Knight», análisis largo · 18:28 · https://www.dailymotion.com/video/x8ltc75 · ⚠️ (no visto entero por tiempo, útil para el redactor si necesita más fotogramas)
- «HOLLOW KNIGHT SILKSONG SWITCH Gameplay» subido a Internet Archive · 6 933 descargas · https://archive.org/details/hollow-knight-silksong-switch-gameplay · ✅
- «Hollow Knight: Silksong Hands-On Demo | E3 2019», grabación de la demo jugable que se mostró 6 años antes del lanzamiento · 1 160 descargas · https://archive.org/details/youtube-XVCApKpayd0 · ✅ (confirma la larguísima espera del público, tema central de las tendencias en redes)
- Tendencia principal en TikTok/redes: la espera de 6 años por Silksong (anunciado 2019, lanzado sep-2025) se volvió meme recurrente («Silksong 2025 is real», cuentas dedicadas sólo a especular la fecha) · https://www.tiktok.com/discover/hollow-knight-silksong-2025-is-real y https://en.wikipedia.org/wiki/Hollow_Knight:_Silksong · ✅ (dos fuentes) · sin minuto exacto: son cientos de clips cortos, no un vídeo único
- Cifra de ventas citada como prueba del fenómeno: más de 7 millones de copias vendidas de Silksong a mediados de diciembre de 2025, más los jugadores de Xbox Game Pass · https://en.wikipedia.org/wiki/Hollow_Knight:_Silksong · ⚠️ (una fuente, wiki tropes/enciclopedia; recomendable cruzar con nota oficial de Team Cherry si el redactor la necesita)
- Contenido de fans en TikTok: ediciones de combates contra jefes, memes sobre la dificultad y el tiempo de espera, con las etiquetas #silksong #hollowknight #hollowknightsilksong · https://www.tiktok.com/discover/hollow-knight-silksong-memes · ⚠️ (una fuente, sin un clip individual destacado: es un patrón de cientos de vídeos cortos)

## 14 · Poses analizadas en varias escenas

Fotogramas sacados con `fotogramas.py` de los dos tráilers (únicas fuentes en vídeo con el
Caballero y Hornet en movimiento a las que tuve acceso sin bloqueo de YouTube).

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| El Caballero cae desde arriba con los brazos abiertos, capa oscura ondeando | Tráiler Hollow Knight (2017) | 0:00-0:03 | presentar / abrir escena |
| El Caballero de pie e inmóvil frente al cartel «Forge your own path», sin arma visible | Tráiler Hollow Knight (2017) | 0:18 | pensar / momento de calma |
| El Caballero salta y ataca con el clavo en el aire, estela blanca de impacto, rodeado de un enjambre (fotograma guardado en `hk1_trailer/fotograma_00066.jpg`) | Tráiler Hollow Knight (2017) | 1:06 | celebrar / acción heroica |
| El Caballero diminuto frente a un enemigo gigante en penumbra (postura defensiva, cuerpo encogido) | Tráiler Hollow Knight (2017) | 1:36 | regañar (postura de reto) / tensión |
| Hornet corriendo con su aguja al hombro, tela roja ondeando tras ella | Tráiler Silksong (2025) | 0:06 | presentar personaje |
| Hornet esquiva hacia adelante dejando una estela roja, cuerpo estirado horizontal (fotograma guardado en `silksong_lanzamiento/fotograma_00033.jpg`) | Tráiler Silksong (2025) | 0:33 | explicar mecánica / acción rápida |
| Hornet clava su aguja en el suelo en plena caída, cuerpo en diagonal, chispas blancas | Tráiler Silksong (2025) | 0:45 | animar / impacto dramático |
| Hornet de pie muy pequeña frente a una criatura enorme entre niebla verde | Tráiler Silksong (2025) | 1:06 | regañar (enfrentar algo más grande) |

## Lo mejor para la lámina

- La paleta de Resting Grounds (azul cian cálido, brillo 65/100, casi sin línea) es la más luminosa y «tranquila» de las 5 zonas: buena para un fondo de canal sereno.
- El fotograma 1:06 del tráiler original (el Caballero saltando con el clavo entre un enjambre, luz blanca de impacto) es la pose de acción más clara que encontré, con fuente y minuto exactos.
- El fotograma 0:33 de Silksong (Hornet en pleno esquive, estela roja) muestra el mismo tipo de acción pero con la otra protagonista, útil si el canal quiere alternar personaje.
- El dato de «6 años de espera» (2019→2025) explica por sí solo casi toda la conversación en redes sobre la obra: es el gancho más fuerte para un texto corto.
- El tema «City of Tears» (único momento de música diegética, con voz sin letra) es la pieza más citada como la más emotiva de toda la banda sonora.

## No encontré

- Minuto exacto de clips individuales de TikTok con vistas contadas (TikTok no da esa cifra por API abierta; busqué «Hollow Knight Silksong TikTok trend viral clip 2025» y sólo salieron páginas de descubrimiento, no vídeos sueltos con métricas).
- Análisis en YouTube con capítulos/minutos marcados: YouTube pide inicio de sesión desde este servidor: no pude usar `fotogramas.py` ni `episodio.py` sobre ningún vídeo de YouTube.
- Video con storyboards oficiales o making-of en vídeo (Team Cherry es un estudio de 2-3 personas y no publica mucho detrás de cámaras en vídeo).
- Nombre exacto del archivo de wiki de cada captura de sitio analizada (sé que pertenecen a la galería «Screenshot HK `<zona>` NN.png» por coincidir resolución y nomenclatura, pero el número de archivo no quedó guardado).

## Bitácora

- Recolector automático (`recolectar.py`): Dailymotion, Internet Archive, MusicBrainz — ya en `datos-video.md`, no repetido.
- Tráileres vistos con `fotogramas.py --salida ... --cada 3` sobre los dos clips de Dailymotion (hecho en un intento anterior, aprovechado de `/tmp/claude-0/trabajo/67-hollow-knight-video/`).
- Paleta y estilo medidos con script Python propio (histograma de color + saturación/brillo) sobre 5 capturas de sitios (trabajo de un intento anterior, aprovechado).
- Fandom API (`hollowknight.fandom.com/api.php`, `action=query&list=search`) para confirmar que las capturas de sitios corresponden a la galería oficial de screenshots de la wiki (español: no hay wiki en español activa para Hollow Knight, sólo inglés).
- WebSearch (inglés): «Hollow Knight soundtrack City of Tears theme emotional scene minute» → cogconnected.com, virtualbastion.com.
- WebSearch (inglés): «Hollow Knight Silksong TikTok trend viral clip 2025» → tiktok.com/discover (varias), Wikipedia.
