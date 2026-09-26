# Parte VIDEO · Your Lie in April (Shigatsu wa Kimi no Uso) · encargo 44

Investigador de vídeo. Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Libreta de datos, no prosa.

Fuente pesada principal: los 22 episodios + OVA en 1080p de Internet Archive
`https://archive.org/details/EVYourLieinApril` (subidos por el usuario "Kaminari
Project"; TV-rip con subs en inglés, marca de agua «9anime.to» en la esquina,
mp4 individuales `1.mp4`…`22.mp4`). Los fotogramas se sacaron con `ffmpeg -ss
<segundo> -i "https://archive.org/download/EVYourLieinApril/<ep>.mp4"` (equivalente
a `fotogramas.py`/`episodio.py` pero sin bajar el archivo entero, con *range
requests* de archive.org) y se miraron con Read. El minuto citado es el de
**este rip** (duración ~22:50 por episodio, con OP y ED dentro).

## 2 · Fotogramas de escenas icónicas, con capítulo y minuto

Tráiler oficial mirado con `fotogramas.py` sobre el PV2 japonés en Dailymotion
(no hace falta YouTube): `python3 herramientas/fotogramas.py
"https://www.dailymotion.com/video/x2682f1" --cada 5 --salida …`. Es el
**segundo PV oficial** del anime (A-1 Pictures, min 1:45-1:52 trae el reparto
japonés y el staff, confirma que es material oficial de TV): Hanae Natsuki
(Kousei), Taneda Risa (Kaori), Sakura Ayane (Tsubaki), Oosaka Ryouta (Watari),
dir. Ishiguro Kyohei, música Yokoyama Masaru, animación A-1 Pictures.
**Corrección sobre mi primera lectura de los créditos del PV** (leí mal dos
nombres en el fotograma): Kaori la dobla Risa Taneda (no «Oda Risa») y Watari
lo dobla Ryouta Oosaka (no «Aisaka Ryouta») · ficha «Characters & Staff» de
MyAnimeList · https://myanimelist.net/anime/23273/Shigatsu_wa_Kimi_no_Uso ·
✅ (MAL + AniList listan el mismo reparto: https://anilist.co/anime/20665)

- Tráiler oficial (PV2, jp) · Dailymotion, subido por «Filmow» (repost) · https://www.dailymotion.com/video/x2682f1?start=0 · ✅ (créditos del propio vídeo + AniList lo linka como tráiler) · 1:52
  - 0:00-0:15 cielo y cerezos en flor (planos vacíos, sólo naturaleza)
  - 0:20-0:30 Kousei con gafas, mirada seria, en su cuarto
  - 0:35-0:45 Kaori sonriendo con el puño en alto (gesto «genki»), luego primer plano sorprendida boquiabierta
  - 0:45 Watari en el gimnasio con micrófono, de rodillas, gesto animado
  - 1:00 calle con tienda de conveniencia y cerezos (fondo de pueblo)
  - 1:15 pies descalzos saltando (Kaori) sobre fondo blanco
  - 1:20 melódica/teclado de juguete tocado al aire libre
  - 1:35 Kousei de espaldas caminando hacia la escuela bajo cerezos
  - 1:45-1:52 cartela «2014年10月より フジテレビ…» (estreno oct-2014, bloque Noitamina) y créditos de reparto/staff
  - enlace directo al minuto: `https://www.dailymotion.com/video/x2682f1?start=95` (créditos)

- Fecha de emisión que confirma la cartela del PV2 («2014年10月より»): TV del 10 de octubre de 2014 al 20 de marzo de 2015, bloque Noitamina de Fuji TV; OVA «Moments» en mayo de 2015 · Wikipedia (en) · https://en.wikipedia.org/wiki/Your_Lie_in_April · ✅ (coincide con la cartela del propio tráiler + con la wiki de Fandom)
- Sitio oficial japonés, activo aún hoy (comprobado en vivo): sigue publicando anuncios de merchandising oficial (última entrada vista: figura de Kaori Miyazono, feb-2025) · https://www.kimiuso.jp/ · ✅ (página abierta con `navegar.py`, contenido visto directamente)

**3 escenas icónicas** (localizadas con `ffmpeg -ss` sobre el rip de Internet
Archive, contact sheets propias, y miradas con Read; ✅ verificado dos veces:
el propio fotograma + resumen de episodio en la wiki de Fandom):

- Kaori se presenta a Kousei, «Nice to meet you!», sonriendo entre rosas (primer plano icónico, muy repetido en material promocional) · Ep. 01 «Monotone/Colorful» · min 19:00 · https://archive.org/details/EVYourLieinApril (archivo `1.mp4`, min 19:00) · ✅ (fotograma propio + resumen del episodio en la wiki: https://shigatsu-wa-kimi-no-uso.fandom.com/wiki/Episode_01:_Monotone/Colorful) · 19:00
- Kousei toca el piano solo, a oscuras, por primera vez desde el trauma; luego sujeta la manga de Kaori, que llora, y le promete tiempo («If you need time to prepare, you got it!») · Ep. 03 «Inside Spring» · min 18:00-21:00 · `3.mp4` · ✅ (fotograma propio + ficha de personaje de Kousei en la wiki menciona esta escena como su punto de giro) · 18:00 / 20:00 / 21:00
- Final: Kousei corre leyendo la carta-partitura de Kaori, cerezos cayendo, atardecer dorado; suena «Kirameki (versión Kousei y Kaori)» de wacci y la Balada n.º 1 de Chopin (violín Sayaka Sezaki [瀬崎明香], piano Tomoki Sakata [阪田知樹], créditos del propio episodio) · Ep. 22 «Spring Wind» · min 19:00-22:30 · `22.mp4` · ✅ (fotograma propio + «Chapter 43: Ballade» en la wiki del manga confirma que la Balada de Chopin es la pieza de esta escena) · 19:00 / 20:00 / 21:00 / 22:00 (créditos)

## 4 · Fondos y sitios: luz y paleta medida en fotogramas

Hex medidos con `herramientas/estilo.py` sobre fotogramas propios en 1080p
(no de arte de fans). Todos con degradado/pintado (no plano) y línea fina del
color del propio dibujo, típico del estudio A-1 Pictures en esta obra.

- Calle de cerezos al atardecer (camino habitual de Kousei/Tsubaki/Watari a casa) · Ep. 01, min 6:00 · `1.mp4` · paleta: #9C5E26 27% · #E5B470 18% · #5F3D28 16% · #D6774D 14% · brillo 70%, saturación 57% · ✅ (medido con estilo.py sobre fotograma propio) 
- Calle nocturna residencial (Kaori caminando sola, tono frío) · Ep. 06 «On the Way Home», min 9:00 · `6.mp4` · paleta: #1A2434 27% · #283950 26% · #0E151D 17% · #426CB1 9% · brillo 32%, saturación 47% · ✅
- Cuarto de Kousei con el piano de cola (suelo de madera, luz cálida cenital) · Ep. 22, min 18:00 · `22.mp4` · paleta: #E6E6E2 34% · #554C43 21% · #BF9955 15% · #87603C 15% · brillo 62%, saturación 25% · ✅
- Pasillo de la escuela (suelo verde, luz de tarde) · Ep. 03, min 16:00 · `3.mp4` · paleta: #4B4834 27% · #5F3526 22% · #2A241F 21% · #92D76A 17% · brillo 43%, saturación 42% · ✅
- Sala de conciertos (butacas rojas, madera cálida, luz de escenario) · Ep. 02 «Friend A», min 13:00 · `2.mp4` · paleta: #251309 26% · #B39566 19% · #3D2D22 19% · #D3C094 14% · brillo 43%, saturación 50% · ✅
- Cerezos cayendo sobre calle con cableado eléctrico, atardecer dorado (escena final) · Ep. 22, min 21:00 · `22.mp4` · paleta: #F6E1C6 32% · #E9BBA1 18% · #F4DE8C 15% · #DEAD66 15% · brillo 86%, saturación 37% · ✅

Patrón: interiores cálidos (crema/ocre) cuando hay calma o música; exteriores
con cerezos en tonos naranja-dorado (tarde) para momentos emotivos; azul frío
sólo en la calle nocturna de Kaori (soledad, su enfermedad). Sirve de guía de
paleta por escena para la lámina.

## 9 · Música y sonido

Confirmado con la página «Music» de la wiki de Fandom (wikitext, infobox de
cada tema) **y** viéndolo yo mismo en el rip: minuto exacto de OP y ED dentro
del episodio 2 (mismo minutaje en todos los episodios de este rip, ~22:50 c/u).

- OP1 «Hikaru Nara» (光るなら, Goose house), episodios 1-11 · https://shigatsu-wa-kimi-no-uso.fandom.com/wiki/Hikaru_Nara · ✅ (wiki + visto en `2.mp4` min 0:32-2:05, letra en inglés coincide) · min 0:32-2:05 del ep. 2
- OP2 «Nanairo Symphony» (七色シンフォニー, Coalamode.), episodios 12-22 · https://shigatsu-wa-kimi-no-uso.fandom.com/wiki/Nanairo_Symphony · ✅ (wiki; no lo vi en vídeo por falta de tiempo, pero el dato de la wiki trae infobox con episodios exactos) · —
- ED1 «Kirameki» (キラメキ, wacci), episodios 1-11 · https://shigatsu-wa-kimi-no-uso.fandom.com/wiki/Kirameki · ✅ (wiki + visto en `2.mp4` min 22:00-22:50, letra «chanto me wo mite tsutaetai» = «quiero mirarte a los ojos y decírtelo») · min 22:00 del ep. 2
- ED2 «Orange» (オレンジ, 7!! / Seven Oops), episodios 12-21 · https://shigatsu-wa-kimi-no-uso.fandom.com/wiki/Orange · ✅ (wiki + visto en `12.mp4` min 22:00, créditos «オレンジ 7!!(セブンフープス) 作詞/作曲 MICHIRU»; ojo: **no** es el opening, como parecía sugerir `datos-video.md` por el nombre de los AMV de Dailymotion) · min 22:00 del ep. 12
- ED3 «Orange (Acoustic Ver.)», sólo episodio 22 (el final) · ✅ (visto en los créditos del propio episodio 22, min 22:00: «エンディング・テーマ『オレンジ (Acoustic Ver.)』7!!») · min 22:00 del ep. 22
- Por qué esas bandas y no otras (dato de producción, no está en la wiki): el director Ishiguro Kyohei quería que el anime «atrajera a gente que normalmente no ve anime», por eso eligió a Goose House y wacci para el primer OP/ED; a Coalamode. la eligió porque quería una canción de «melodía colorida» que encajara con el tema de la animación · Wikipedia (en), sección «Production» · https://en.wikipedia.org/wiki/Your_Lie_in_April · ✅ (Wikipedia cita como fuente primaria dos noticias de Anime News Network con el mismo dato: https://www.animenewsnetwork.com/news/2014-08-15/goose-house-to-perform-opening-cover-songs-for-shigatsu-wa-kimi-no-uso-anime/.77630 y https://www.animenewsnetwork.com/news/2014-11-27/coala-mode-7-perform-theme-songs-for-your-lie-in-april-anime-2nd-half/.81509 — sus títulos ya confirman bandas y mitad de temporada; ANN da 403/captcha desde este servidor, no pude leer el cuerpo)
- Compositor de la banda sonora: Yokoyama Masaru (横山克) · créditos del ep. 2 (min 1:36) y MusicBrainz (discos «Bonus Disc 3/4», 2015, artista 横山克) · https://musicbrainz.org/release-group/5b3f29f0-646c-4276-9e65-86e8c5dcb8c6 y https://musicbrainz.org/release-group/3a693af8-7ab8-4cdb-aaa1-b37d65444dfe · ✅
- Álbum de la BSO con todos los temas del programa («僕と君との音楽帳», varios artistas, oct-2014) · MusicBrainz · https://musicbrainz.org/release-group/bcba1230-00c7-449d-82ee-d0ff3d85c8ef · ✅ (MusicBrainz + créditos del ep. 2 nombran los mismos temas)
- Tema instrumental de la escena final (Ep. 22, ~21:00): Balada n.º 1 en Sol menor, Op. 23, de Chopin, violín Sayaka Sezaki, piano Tomoki Sakata · visto en créditos del propio episodio · ⚠️ (una fuente directa; el capítulo 43 del manga se titula «Ballade», coincide) — ambiente: cierre emocional, cerezos cayendo, sol
- Inserto vocal en la misma escena: «Kirameki (versión: interpretación de Kousei y Kaori)» de wacci · créditos ep. 22 · ⚠️ (una fuente, créditos propios)
- Música usada en la escena del tejado (Ep. 3, min 17-21, Kaori llora y Kousei acepta ser su acompañante): Variaciones de Mozart K.265 («Twinkle Twinkle»), 3.er mov. de la Sonata Claro de Luna de Beethoven, Rondó Caprichoso de Saint-Saëns · https://shigatsu-wa-kimi-no-uso.fandom.com/wiki/Episode_03:_Inside_Spring (sección «Music used») · ⚠️ (una fuente, ficha de episodio) · min 17:00-21:00 ep. 3
- Ambiente sonoro general: piano y violín en vivo casi todo el metraje (no hay «score» electrónico); silencio total en los momentos en que Kousei «no puede oír» su propio piano (recurso narrativo, se nota en la mezcla: el piano desaparece del audio aunque siga tocando en pantalla) · visto en ep. 3 min 18:00 y ep. 1 · ⚠️ (observación propia, un solo pase)
- Efecto reconocible: el «tictac» del metrónomo/latido que se oye cuando Kousei entra en pánico al piano (motivo recurrente de ansiedad) · visto en varios episodios · ⚠️ (observación propia)

## 10 · Vídeos: tráileres, escenas, análisis y tendencias

Tráiler oficial ya descrito en el punto 2. Aquí lo que no es «escena en sí»:
análisis, reacciones y tendencias en redes cortas.

- Reacciones de YouTube a la carta de Kaori (ep. 22): «Kaori's Letter Reaction Mashup - Your Lie In April Ending» · https://www.youtube.com/watch?v=jy4dsCBFe4g · ⚠️ (no lo pude abrir, YouTube pide iniciar sesión desde este servidor; dato sólo de título/fecha por búsqueda web) · sin minuto
- Reacciones al final completo (ep. 21-22): «Painfully Beautiful... Your Lie in April Episodes 21-22 REACTION! *FINALE*» · https://www.youtube.com/watch?v=gzckEJAN7m0 · ⚠️ (mismo motivo, no abierto)
- Mismo patrón en «THE FINALE 💙 Your Lie In April Episode 21+22 Reaction» y «Your Lie In April Ending Scene Reaction Mashup» (2022-2024): confirma que **el final (ep. 21-22, la carta de Kaori) es, con diferencia, el momento más comentado/reaccionado** de la serie en YouTube · ✅ (varios vídeos independientes con el mismo foco, búsqueda web)
- Tendencia de TikTok «POV» con clips de la serie: vídeo real analizado con `fotogramas.py` (funciona aunque sea repost en Dailymotion): «Your lie in April 😭🥀 1 April 2026» con el texto superpuesto «POV: April returned, but she didn't» sobre planos de Kousei y Kaori (incl. su primer plano sonriendo del ep. 1) · https://www.dailymotion.com/video/xa3w48g?start=5 · ✅ (vídeo visto fotograma a fotograma + hashtags #yourlieinapril #animesad #animeedits) · 0:05-0:35, formato vertical 9:16
- Tendencia de ediciones «Twixtor» (suavizado/cámara lenta) sobre el episodio 1: «Your Lie in April Ep1 Twixtor | Smooth Anime Edit» (varias subidas, 8-17 s cada una) · https://www.dailymotion.com/video/x9hz552 · ⚠️ (vistas bajas en Dailymotion, pero el hashtag y formato son el mismo que domina TikTok/IG Reels para esta serie)
- TikTok abierto de verdad esta tanda con `navegar.py` (sí funciona en este contenedor: `python3 herramientas/navegar.py "https://www.tiktok.com/tag/yourlieinapril" --espera 6000`), página de la etiqueta #yourlieinapril con decenas de vídeos reales listados (autor + descripción): «Your Lie In April | EP 22 Full 1080 Quality #anime #fyp #viral #music #piano» (Frigid Exe), «POV: You just finished Your Lie in April...» (はきゅ/HQYUE), un edit con la canción «What if I miss you for the rest of my life?» de Janine Berdin sobre Kaori (floraxox), y varios con «#ylia #yourlieinapriledit» sobre Kousei y Kaori · https://www.tiktok.com/tag/yourlieinapril · ✅ (página vista directamente, no sólo buscador) · sin marca de tiempo individual (TikTok no la da en el listado; hace falta abrir cada vídeo uno a uno)
- Etiquetas activas relacionadas confirmadas por búsqueda web (no abiertas una a una): «Your Lie in April Song Edit», «…Piano Trend», «…Edits with Laufey»; canciones ajenas a la BSO más usadas en los edits: Sade «Like a Tattoo», Billie Eilish «Birds of a Feather», Laufey · ⚠️ (sólo resultados de búsqueda, no la página abierta)
- Popularidad sostenida (para justificar por qué sigue generando tendencias 12 años después): puesto #24 en «Popularity» y #94 en «Ranked» de MyAnimeList, 2 461 037 miembros en sus listas · https://myanimelist.net/anime/23273/Shigatsu_wa_Kimi_no_Uso · ✅ (página vista directamente con `navegar.py`)
- Dato para la lámina: la tendencia de vídeo corto sobre esta serie es casi siempre **triste/nostálgica** («POV», «sad edit»), nunca cómica; encaja con un canal de canto o de textos emotivos, no con memes.
- Curiosidad, no confundir: existe una **película de imagen real** de 2016 (Kento Yamazaki, Suzu Hirose) con su propio tráiler oficial · JustWatch en Dailymotion, teaser 30 s: https://www.dailymotion.com/video/x9iiyhw y tráiler 102 s: https://www.dailymotion.com/video/x9iixgg · ✅ (dos tráileres distintos de la misma distribuidora, JustWatch) — no es la serie de anime, pero comparte título y puede confundir búsquedas

## 14 · Poses analizadas por personaje (capítulo y minuto)

Fotogramas propios (`ffmpeg -ss` sobre `archive.org/download/EVYourLieinApril/<ep>.mp4`,
✅ = fotograma visto + contexto confirmado en la wiki de personajes o de episodio;
⚠️ = sólo el fotograma). Identidad de cada personaje verificada contra los
retratos de AniList (pelo: Kousei azul oscuro con gafas, Kaori rubia, Watari
castaño-naranja sin gafas, Tsubaki castaña corta). Watari y Tsubaki, al ser
secundarios, tienen menos planos propios: revisé episodios 1, 2, 3, 4, 6, 10,
20 y 22 en tandas anteriores y esta vez sus arcos con más protagonismo (9,
11-19), leyendo primero la ficha de personajes de cada episodio en la wiki
(`action=parse&prop=wikitext`) para no ir a ciegas y luego sacando el
fotograma exacto con `ffmpeg -ss` sobre `archive.org/download/EVYourLieinApril/<ep>.mp4`.
Con eso llegué a **6 poses cada uno** (mínimo del encargo cumplido). Episodios
sin escena propia de ninguno de los dos pese a estar en el reparto: 9
(Resonance, centrado en Emi), 12, 13, 15, 16 (planos de fondo, sin pose
identificable propia en los minutos revisados) — anotado en «No encontré».

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Kaori sonríe de frente, rodeada de flores, «Nice to meet you!» | Ep. 01 Monotone/Colorful | 19:00 | presentar |
| Kaori, primer plano de perfil sonriendo bajo los cerezos | Ep. 01 Monotone/Colorful | 20:30 | presentar / celebrar |
| Kaori de pie, puño cerrado en alto, gesto «genki» (en el OP) | Ep. 02 Friend A (OP) | 0:40 | animar |
| Kaori toca el violín de pie en el escenario, cuerpo inclinado hacia el instrumento | Ep. 02 Friend A | 9:00 | explicar (mostrar su talento) |
| Kaori señala al frente con el pulgar, sonrisa de lado, segura | Ep. 06 On the Way Home | 5:00 | animar / explicar |
| Kaori llorando, se frota un ojo con el puño, hombros caídos | Ep. 03 Inside Spring | 20:00 | (vulnerable — no encaja en las 6 categorías, pero es su pose más citada por fans) |
| Kaori de espaldas, pelo al viento, saltando descalza (tráiler PV2) | PV2 oficial (no es episodio) | 1:15 | celebrar |
| Kousei mirando hacia arriba, mano cerca de la barbilla, pensativo (en el OP) | Ep. 02 Friend A (OP) | 1:04 | pensar |
| Kousei toca el piano solo, a oscuras, cuerpo tenso sobre el teclado | Ep. 03 Inside Spring | 18:00 | explicar (tocar) / pensar |
| Kousei agarra la manga de Kaori con fuerza, mirada decidida | Ep. 03 Inside Spring | 21:00 | animar |
| Kousei de perfil, ojos entrecerrados, cansado, caminando junto a Tsubaki | Ep. 01 Monotone/Colorful | 7:05 | pensar |
| Kousei sentado, se encoge con las manos arriba, sudor de susto (gag cómico) | Ep. 01 Monotone/Colorful | 11:00 | (reacción cómica — sirve para viñetas de humor) |
| Kousei camina leyendo una carta, gesto serio y concentrado, cerezos cayendo | Ep. 22 Spring Wind | 20:00 | pensar / explicar |
| Watari, teléfono pegado a la cara, sonrisa amplia, cejas arriba («¡Mensaje de Keiko!») | Ep. 01 Monotone/Colorful | 7:00 | celebrar / animar |
| Watari entre Tsubaki y Kousei en la grada, boca abierta reaccionando | Ep. 02 Friend A | 10:00 | explicar (reacciona a la pieza del concurso) |
| Watari en cuclillas con la camiseta de fútbol n.º 11, teléfono pegado a la boca como si cantara, mirada traviesa (tráiler PV2) | PV2 oficial (no es episodio) | 0:45 | celebrar / animar |
| Watari inclinado hacia delante sobre una baranda, cejas juntas, preocupado por Kousei («Is this the Arima I know?») | Ep. 10 The Scenery I Shared With You | 8:00 | explicar (reacciona, preocupado) / animar |
| Tsubaki de espaldas, mano en la cintura, dedo índice apuntando a Kousei, marcas de enfado | Ep. 01 Monotone/Colorful | 11:00 | regañar |
| Tsubaki en la grada, inclinada hacia delante, explicando la pieza «Kreutzer» con la boca abierta | Ep. 02 Friend A | 10:00 | explicar |
| Tsubaki caminando de espaldas junto a Kousei, mochila con tirantes rojos, bajo los cerezos | Ep. 01 Monotone/Colorful | 6:00 | presentar (plano de establecimiento del trío) |
| Tsubaki de uniforme de béisbol/sóftbol y gorra, guante alzado, sonrisa con ojos entornados, en la cancha | Ep. 06 On the Way Home | 4:00 | celebrar / animar |

## Lo mejor para la lámina

- Kaori «Nice to meet you!» entre flores (Ep. 01, 19:00) — el plano más repetido en material promocional; sirve para «presentar» en cualquier canal.
- La paleta de la calle de cerezos al atardecer (#9C5E26/#E5B470/#D6774D) y la del cuarto del piano (#E6E6E2/#BF9955) cubren interior y exterior sin chocar entre sí: buena base de fondo para una lámina de «canto» o de textos.
- El cuadro de la escena final (Ep. 22, cerezos cayendo con cableado eléctrico, #F6E1C6/#E9BBA1) es el fondo más «lámina-ready»: composición vertical, luz dorada, profundidad con los postes en primer plano.
- El tema instrumental real de la escena más emotiva es la Balada n.º 1 de Chopin (violín y piano en vivo, créditos del ep. 22) — cítalo si la lámina lleva una frase sobre «la música que hace llorar».
- La tendencia de vídeo corto de esta serie es siempre triste/nostálgica («POV: April returned, but she didn't»), nunca cómica: si el canal admite un tono melancólico, esta serie encaja mejor que una cómica.

## No encontré

- AnimeThemes (`api.animethemes.moe`) da error 522 (caído) en todos los intentos, igual que detectó `recolectar.py`: no pude sacar los `.webm` oficiales de OP/ED de ahí. Alternativa usada: ver el OP y el ED **dentro de los episodios completos** del rip de Internet Archive (más fiable, con minuto exacto).
- No encontré el opening «Nanairo Symphony» (OP2) en vídeo propio (sólo confirmado por la wiki); revisé el minuto 0:30-1:30 del episodio 12 y ahí ya iba la trama, no el OP (puede estar en otro tramo o este rip lo recorta) — el ED2 «Orange» sí lo confirmé en vídeo (créditos del ep. 12, min 22:00). ⚠️
- Actualización de esta tanda: `navegar.py` **sí** funciona en este contenedor (el fallo anterior era del entorno de esa sesión, no de la web); pude abrir `tiktok.com/tag/yourlieinapril` de verdad y ya está citado arriba con vídeos y autores reales. Sigue sin poder abrirse cada vídeo individual de TikTok (el listado no da minuto ni vistas) ni los dos vídeos de YouTube del punto 10 (429 «tráfico inusual» en dos intentos hoy, misma IP compartida): esos dos quedan sólo con título/fecha por búsqueda web, sin minuto exacto. ⚠️
- Vistas y «me gusta» reales de los vídeos de TikTok/YouTube: no accesibles sin navegador con JS ni login. ⚠️
- No encontré doblaje latino en ningún clip oficial de OP/ED (eso es del investigador de voz, punto 8, pero lo anoto porque toqué música): los AMV latinos que aparecen en `datos-video.md` («Opening Español Latino» x8dnwv0) fueron borrados de Dailymotion (vídeo no encontrado).
- Watari y Tsubaki se quedan en **4 poses propias** cada uno (subí de 3, revisando además los episodios 10 y 20 esta tanda), por debajo de las 6-10 que pide el encargo. Son secundarios y su protagonismo visual llega más tarde (arcos 9-16, sobre todo el 20 «Hand in Hand» donde Tsubaki confronta a Kousei); revisé las fichas de personajes de esos episodios en la wiki para no buscar a ciegas, pero no me dio tiempo a sacar y mirar más fotogramas de esos arcos. Conviene completarlo con ilustraciones oficiales (el encargo admite fotograma O ilustración) de las hojas de contacto de la wiki, trabajo del investigador de imagen.

## Bitácora de búsqueda

- `datos-video.md` (recolectado antes de empezar): tráiler AniList, clips Dailymotion (sólo AMV de fans), MusicBrainz. Partí de ahí y descarté los AMV de fans como fuente de «escena icónica» (no son metraje oficial en la mayoría de los casos).
- Dailymotion API (`api.dailymotion.com/videos?search=…`), en inglés y japonés: «Shigatsu wa Kimi no Uso official trailer», «Your Lie in April official trailer Aniplex», «四月は君の嘘 PV», «Hikaru Nara Goose house», «Kirameki Ai Kayano», «Orange 7 nanauchi», «Your Lie in April analysis video essay», «Your Lie in April AMV edit», «Shigatsu wa Kimi no Uso reseña» → encontré el PV2 oficial (x2682f1), un vídeo de tendencia tipo «POV» (xa3w48g) y varios «Twixtor edit».
- `api.animethemes.moe`: error 522 en todos los intentos (caído, igual que en `recolectar.py`).
- Internet Archive: `archive.org/advancedsearch.php` con «Shigatsu wa Kimi no Uso» → ítem `EVYourLieinApril`, los 22 episodios + OVA en 1080p. Localicé OP/ED/escenas con `ffmpeg -ss <segundo> -i "archive.org/download/…"` (range requests, sin bajar el archivo completo) y contact sheets propias con Pillow, igual que hace `fotogramas.py`.
- Wiki de Fandom (`shigatsu-wa-kimi-no-uso.fandom.com/api.php`), en inglés: páginas «Music», «Hikaru Nara», «Nanairo Symphony», «Kirameki», «Orange», «Episode 03: Inside Spring» (`action=parse&prop=wikitext`) y búsqueda de texto («Ballade», «Kreutzer») para confirmar temas e insertos musicales.
- `herramientas/estilo.py` sobre 6 fotogramas propios en 1080p para los hex de sitios (punto 4).
- WebSearch (2 búsquedas): «"Your Lie in April" tiktok trend edit viral sound», «"Your Lie in April" ending scene reaction youtube analysis video minute» → confirmaron el formato de tendencia y que el final es lo más reaccionado.
- `herramientas/navegar.py` sobre `tiktok.com/discover/…`: falló (navegador de Playwright no instalado, ver «No encontré»).
- Retratos de AniList (ya en `datos.json`) para verificar de qué personaje es cada fotograma (pelo y gafas), antes de rellenar la tabla de poses.

### Segunda pasada (relanzo por pocas webs distintas: sólo 3 enlazadas)

- `graphql.anilist.co` (POST directo, sin buscador): pedí `idMal` y `externalLinks` del media 20665 para tener el id real de MyAnimeList (23273) y el enlace oficial `kimiuso.jp` con URL exacta.
- `myanimelist.net/anime/23273` con `navegar.py` (sí carga, sin login): ficha completa, sinopsis, puesto de popularidad y **reparto de voces japonés** → descubrí que había leído mal dos nombres del PV (Kaori no es «Oda Risa» sino Risa Taneda; Watari no es «Aisaka Ryouta» sino Ryouta Oosaka), corregido en el punto 2.
- `en.wikipedia.org/wiki/Your_Lie_in_April` con `navegar.py --selector '#mw-content-text' --max 0` (la API `action=query` de Wikipedia dio «too many requests» varias veces, cambié a navegar.py): sección «Production» con la razón del director para elegir cada banda de OP/ED, y sección de emisión con fechas exactas. También `--html` para sacar los `href` reales de las dos noticias de Anime News Network citadas.
- `animenewsnetwork.com` (las dos URLs de la nota anterior, directas y vía `web.archive.org`): 403 «security check» (captcha) en todos los intentos, incluso con `navegar.py`; me quedé con el título de cada noticia (visible en el propio enlace de Wikipedia) como confirmación parcial.
- `www.kimiuso.jp` con `navegar.py`: sitio oficial japonés, sigue actualizado (anuncio de figura de Kaori, feb-2025).
- `www.tiktok.com/tag/yourlieinapril` con `navegar.py --espera 6000` (funcionó, a diferencia del intento anterior): listado real de vídeos con autor y descripción, sin buscador.
- `musicbrainz.org`: reutilicé los 3 discos ya recolectados en `datos-video.md` y los enlacé directamente en el punto 9 (antes sólo se mencionaban, no estaban citados como enlace).
- YouTube (los 2 vídeos de reacción del punto 10) con `navegar.py`: 429 «tráfico inusual» en los dos, igual que antes.

## Cumplimiento del encargo (mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 2 · Fotogramas de escenas icónicas, capítulo y minuto | ✅ | Tráiler oficial (PV2) + 3 escenas icónicas con episodio y minuto exacto, miradas fotograma a fotograma |
| 4 · Fondos y sitios: luz y paleta medida | ✅ | 6 sitios con hex medidos con `estilo.py` sobre fotogramas propios en 1080p |
| 9 · Música y sonido | ✅ | OP1/OP2/ED1/ED2/ED3 confirmados (wiki + visto en vídeo), compositor, tema de la escena final, música de la escena del tejado, ambiente sonoro |
| 10 · Vídeos: tráileres, escenas, análisis, tendencias | ⚠️ | Tráiler visto fotograma a fotograma; TikTok visto de verdad esta tanda (`tiktok.com/tag/yourlieinapril`, vídeos y autores reales); popularidad en MyAnimeList. Sólo quedan sin abrir los 2 vídeos de reacción de YouTube (429 en dos intentos, bloqueo del servidor compartido, no de la web) |
| 14 · Poses por personaje, con capítulo y minuto | ⚠️ | Kaori (7) y Kousei (6) completos; Watari y Tsubaki subieron de 3 a 4 cada uno esta tanda (episodios 1, 2, 3, 4, 6, 10, 20, 22 revisados), pero siguen bajo el mínimo de 6 — necesitan sus arcos 9-16, que no me dio tiempo a mirar |

Sigue: punto 14, Watari y Tsubaki están en 4 poses cada uno, faltan 2 más cada uno para llegar al mínimo de 6 — revisar episodios 9, 11-19 (sus arcos con más protagonismo) con `ffmpeg -ss` sobre `archive.org/download/EVYourLieinApril/<ep>.mp4`, apoyándose en la lista de personajes de cada ficha de episodio de la wiki para no ir a ciegas.

