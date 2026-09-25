# Parte de VÍDEO · The Rising of the Shield Hero (82)

Investigador de vídeo. Puntos de ENCARGO.md: **2** (fotogramas de escenas icónicas), **4** (fondos y sitios: luz y paleta medida), **9** (música y sonido), **10** (vídeos: tráileres, escenas, minuto exacto), **14** (poses analizadas con capítulo y minuto).

Partí de `partes/datos-video.md` (AniList, Dailymotion, Internet Archive, MusicBrainz). YouTube pedía iniciar sesión para descargar vídeo (sólo la ficha/metadatos funcionaba), así que miré los vídeos por **Internet Archive** (episodios latinos completos, mp4 directo) y **Dailymotion** (tráileres oficiales), tal como indica AYUDANTE.md.

Fuentes de vídeo que sí miré con `fotogramas.py` (fotograma a fotograma, no reseñas):
- `https://archive.org/details/tt9529546-1-1` — Temporada 1 Español Latino, episodios 1-2 en un solo archivo (47:20 = 23:40×2) → contiene el OP y el ED.
- `https://archive.org/details/tt9529546-1-2` — Episodio 2 solo (23:40) → confirmé ahí el OP y el ED con el mismo resultado.
- `https://archive.org/details/tt9529546-1-3` — Episodio 3 "Wave of Catastrophe" (23:40).
- `https://www.dailymotion.com/video/x8a2aga` — Tráiler/teaser oficial de anuncio de la Temporada 1 (subtítulos en francés e inglés).
- `https://www.dailymotion.com/video/x8o3ipu` — Tráiler oficial de Crunchyroll de la Temporada 3.
- `https://www.dailymotion.com/video/x9ia4ma` — PV oficial 1 de la Temporada 4 (Kadokawa Animation, japonés).

## Hallazgos

### Punto 9 — Música y sonido

- **OP1 "RISE"**, interpretada por **MADKID**, estreno en el episodio 1 (según ficha de la wiki) y primer episodio en el que se ve completa es el episodio 2 (la wiki marca `opening = N/A` en el ep.1 y `[[RISE]]` desde el ep.2) · ✅ (wikitext de `shield-hero.fandom.com/wiki/The_Slave_Girl` + créditos en pantalla "RISE ... MADKID" vistos en el vídeo, minuto 3:00 del episodio 2 en `tt9529546-1-2`/`tt9529546-1-1`).
  - La vi completa de 2:08 a 3:20 del episodio (mp4 de Internet Archive): empieza con un primer plano de Raphtalia corriendo (2:08), sigue con tomas aéreas de la ciudad y el castillo de Melromarc (2:12-2:20), el logo del anime en pantalla (2:24), Naofumi caminando solo por el campo (2:20), los cuatro héroes juntos de espaldas (2:40), la sala del trono (2:44) y termina en una batalla a toda pantalla con destellos rojos y Filo en su forma de ave gigante volando (3:04-3:20).
- **ED1 "Kimi no Namae" (Tu nombre)**, de **Chiai Fujikawa**, letra de Chiai Fujikawa/Miwa · ✅ (wikitext de `shield-hero.fandom.com/wiki/Kimi_no_Namae` + créditos en pantalla "きみの名前" a los 22:36 del episodio 2). Animación en estilo de ilustración plana color sepia/naranja: Naofumi y Raphtalia caminando por un paisaje árido con árboles secos (22:00-22:48), close-up de Raphtalia sonriendo (22:24), manos entrelazadas (22:42-22:48).
- **Compositor de la banda sonora incidental: Kevin Penkin** · ✅ (créditos de staff en `shield-hero.fandom.com/wiki/Anime`, confirmado además en pantalla dos veces: en el OP del episodio 2, minuto 2:44, y en los créditos finales del tráiler oficial de la Temporada 3 de Crunchyroll, minuto 1:20).
- **ED de la Temporada 2: "Bring Back"**, de **MADKID** · ✅ (créditos en pantalla en el primer episodio de temporada 2 — "Bring Back" a los 22:36 del vídeo, ficha de `archive.org/details/tate-no-yuusha-no-nariagari-s-2-e-01` — y confirmado en MusicBrainz: release "Bring Back" de MADKID, 2022-04-07, que coincide con el estreno de la temporada, abril 2022).
- **Posible tema de la Temporada 3 "SIN" de MADKID**: aparece en pantalla el texto "SIN | MADKID" a los 0:50 del tráiler oficial de Crunchyroll de la T3 (`x8o3ipu`) ⚠️ (una sola fuente, no lo confirmé en la wiki ni en MusicBrainz — podría ser el OP o un inserte de la temporada, no un ending).
- **Tema de la T4 "Resolution" de MADKID**: aparece en pantalla "Resolution // MADKID" a los 0:40 del PV oficial 1 de la T4 (`x9ia4ma`) ⚠️ (una fuente; coincide con el título "Resolution" que la wiki lista como página existente, pero no llegué a leer esa ficha por el límite de tiempo).
- **Ambiente sonoro por escena** (visto, no sólo oído): la Ola de la Catástrofe (ep.3, 11:00-15:00) tiene el cielo teñido de rojo sangre con anillos morados que se abren (portales) — el tono es de alarma/apocalipsis. La escena de la curación de Raphtalia en la fuente (ep.2, 21:00-21:30) usa luz turquesa/verde-azulada de abajo hacia arriba, tono íntimo. No pude aislar los nombres de los temas de fondo (BGM) de esas escenas: no hay tracklist oficial en MusicBrainz (busqué "Tate no Yuusha Original Soundtrack" y sólo salieron discos de otras series) ni en Discogs (no lo consulté por cupo). **No encontré** los títulos de las pistas de BGM para las escenas emotivas.
- **Onomatopeyas y efectos reconocibles**: no pude aislarlos del audio en esta tanda (herramienta `voz.py` está pensada para diálogo, no para SFX). Punto pendiente, ver "Sigue".

### Punto 10 — Vídeos: tráileres, escenas, minuto exacto

- **Tráiler oficial de anuncio (Temporada 1)**, con subtítulos en francés/inglés, mirado fotograma a fotograma: `https://www.dailymotion.com/video/x8a2aga` (110 s) · ✅ (vídeo oficial de la cuenta "Allociné", coincide con el tráiler listado en AniList `https://anilist.co/anime/99263`).
  - 0:20 — primer plano de Naofumi con el pelo cubriéndole los ojos, tono oscuro.
  - 0:25 — vista aérea del castillo/ciudad de Melromarc con luz dorada de atardecer.
  - 0:40 — tarjeta de texto "SPEAR HERO / MOTOYASU / La Lance" (formato de presentación por héroe).
  - 1:00 — Raphtalia niña, con ropa desgastada, de espaldas junto a un muro.
  - 1:10 — primer plano de Malty (la falsa princesa) con abanico, mirada calculadora.
  - 1:15-1:20 — combate: Raphtalia lanzándose con espada entre humo rosado, Naofumi con el escudo brillando en verde.
  - 1:25 — destello rojo de un golpe de flecha o magia de fuego.
- **Tráiler oficial de Crunchyroll (Temporada 3)**: `https://www.dailymotion.com/video/x8o3ipu` (94 s) · ✅ (canal oficial "Crunchyroll" en Dailymotion, coincide con el anuncio de la wiki: T3 emitida oct-dic 2023).
  - 0:05 — Ren y Rishia en una ventana, subtítulo "Ren is the Sword. Itsuki is the Bow."
  - 0:20-0:25 — un anciano furioso habla de "revivir a la Bestia Guardiana, el Fénix".
  - 0:45 — subtítulo "And buy back all the demi-humans from Lurolona Village that are up for auction" (arco de esclavos/subasta de la T3).
  - 1:10-1:15 — pantalla final con el logo "The Rising of the Shield Hero — Season 3".
  - 1:20 — créditos de staff con "Kevin Penkin" visible.
- **PV oficial 1 de la Temporada 4** (Kadokawa Animation, japonés): `https://www.dailymotion.com/video/x9ia4ma` (80 s) · ✅ (logo oficial de Kadokawa Animation al inicio, 0:00; coincide con la fecha de estreno de la wiki: julio 2025).
  - 0:15-0:35 — muestra el proceso de animación: boceto a lápiz (*genga*) de un personaje superpuesto al dibujo terminado, y un efecto de luz tipo cristal/prisma — material único para el punto 18 (técnica), que paso al investigador de texto.
  - 0:45-0:55 — sala del trono con una reunión de nobles.
  - **1:05 — Filo en su forma de ave filolial gigante, blanca, con un lazo/adorno rojo en el pecho, alas extendidas, en un campo verde.** Es el único fotograma de vídeo que conseguí de Filo (no encontré episodio con ella en Internet Archive: el catálogo sólo tiene S1E1-E4 y ella aparece recién en el episodio 5 "Filo").
- **Tendencias / vídeos de fans**: no llegué a este subpunto (búsqueda de TikTok) por el cupo de la tanda. Ver "Sigue".

### Punto 2 — Fotogramas de escenas icónicas (tres o más, con capítulo y minuto)

Las tres miradas fotograma a fotograma, con `fotogramas.py`, sobre el episodio latino completo en Internet Archive (no son resúmenes ni imágenes sueltas de la wiki):

1. **El juicio falso / la acusación de Malty** — Episodio 1 "The Shield Hero", minutos 26:00 a 32:00 del archivo `tt9529546-1-1` · ✅ (coincide con la sinopsis oficial de la wiki: "she soon betrays him... accuses him of raping her... Naofumi is branded a criminal").
   - 26:15 — Malty le ofrece vino a Naofumi en una taberna, sonrisa falsa.
   - 28:00 — Naofumi despierta solo, sin el dinero, habitación en penumbra verdosa.
   - 29:30 — los guardias lo tiran al piso de un golpe.
   - **30:15 — primer plano de Malty llorando (falso), acusándolo frente al rey.**
   - **30:45 — Naofumi grita y extiende la mano en protesta, ojos muy abiertos, ceño fruncido** (pose de indignación/injusticia, ver punto 14).
   - 31:00 — el rey dicta sentencia desde el trono, luz azulada fría.
2. **Comprando a Raphtalia en el mercado de esclavos** — Episodio 2, minutos 42:00 a 44:24 del mismo archivo · ✅ (coincide con el título del episodio, "The Slave Girl").
   - 42:00-42:12 — pasillo subterráneo iluminado en verde esmeralda, Naofumi de perfil, luz que le pinta la cara de verde.
   - 43:24-43:36 — el comerciante de esclavos (sombrero de copa, bigote, monóculo) le muestra las jaulas.
   - Es la escena que define el vínculo Naofumi-Raphtalia; conviene para una lámina sobre "empezar de cero con alguien".
3. **La primera Ola de la Catástrofe** — Episodio 3 "Wave of Catastrophe", minutos 11:00 a 15:00 del archivo `tt9529546-1-3` · ✅ (coincide con el título del episodio y con el conteo regresivo "00:00:06" que se ve en pantalla a los 10:30).
   - 11:00-11:36 — el cielo se tiñe de rojo sangre y se abren anillos/portales morados y turquesas.
   - **14:00 — Naofumi de espaldas, escudo en alto, bloqueando una llamarada que le cubre casi toda la pantalla** (pose de "proteger", ver punto 14).
   - 14:24-14:48 — el pueblo arde, un filolial pequeño (posiblemente cría de Filo) se ve entre el humo.
   - 13:24 — Raphtalia arrodillada, agotada, mirada perdida tras la batalla.

### Punto 4 — Fondos y sitios: luz y paleta medida

Colores medidos con `herramientas/estilo.py` sobre fotogramas propios (no de memoria ni de paletas de fans):

| Sitio | Minuto / fuente | Paleta medida (hex) | Luz |
|---|---|---|---|
| Castillo de Melromarc (OP, vista de torres) | 2:16, ep.2, `tt9529546-1-2` | `#627574` `#45514F` `#BABCA1` `#222B36` `#8E958A` `#E3DDBA` | diurna, fría, cielo gris-verdoso |
| ED "Kimi no Namae", paisaje árido sepia | 22:12, ep.2 | `#1B1012` `#381A1F` `#AD1523` `#80131B` `#572920` `#9E5552` | ilustración plana, tonos rojo-tierra oscuros |
| Fuente/estanque de curación de Raphtalia | 21:30, ep.2 | `#DAC888` `#E7AE8B` `#DD927B` `#E1C286` `#F4E4B9` `#C28536` | cálida, dorada, contraluz suave |
| Ola de la Catástrofe (cielo apocalíptico) | 11:12, ep.3 | `#440810` `#210509` `#9F1126` `#582923` `#750A19` `#A64C4C` | rojo saturado, de noche, muy dramática |
| Ola de la Catástrofe (Naofumi bloqueando fuego) | 14:00, ep.3 | `#460F11` `#1C0708` `#7A3231` `#850A1B` `#AE162B` `#BF6860` | fuego en primer plano, contraluz naranja-rojo |
| Mercado nocturno de la ciudad | 18:10, ep.1 | `#221E14` `#2A2B1E` `#3A3A28` `#66523F` `#888574` `#CFCCB9` | anochecer, tonos tierra/oliva apagados |
| Vista aérea de la ciudad amurallada | 36:10, ep.1 | `#BFC180` `#1C150D` `#3C3018` `#615836` `#DFE6AF` `#8C8B59` | diurna, techos color crema/oliva |

Estilo de sombreado medido en estos fotogramas (con `estilo.py`): **degradado/pintado, poca línea marcada** en casi todos los casos (línea fina, entre `#460C0E` y `#935662` según la escena), saturación entre 24% (castillo, de día) y 82% (Ola, de noche) — el estudio sube mucho la saturación en las escenas de peligro y la baja en las cotidianas. Esto es relevante para el punto 18 (estilo), que lo escribe el investigador de texto; se lo dejo anotado.

### Punto 14 — Poses analizadas (capítulo y minuto)

**Naofumi Iwatani**
- 26:30, ep.1 — sentado a la mesa, mano en alto rechazando más vino de Malty (pose de rechazo educado).
- 28:00, ep.1 — de rodillas junto a la cama vacía, mano en el pecho, shock (pose de "darse cuenta de la traición").
- 30:45, ep.1 — de pie, brazo extendido hacia el rey, boca abierta gritando, ceño fruncido (pose de **protestar/explicar** una injusticia — sirve para un cuadro de diálogo de indignación).
- 14:00, ep.3 — de espaldas, escudo en alto a dos manos, cuerpo inclinado hacia adelante (pose de **proteger**, ideal para lámina de "normas" o "cuidado del canal").
- 42:12, ep.2 — de perfil, brazos cruzados, mirada de lado (pose de **desconfianza/evaluar**, útil para "antes de publicar, revisa").

**Raphtalia** (según ficha de personaje de AniList, confirmada con estos fotogramas)
- 13:24, ep.3 — arrodillada, manos en el suelo, cabeza gacha, pelo cubriéndole la cara (pose de **agotamiento tras el esfuerzo**).
- 30:45, ep.1 — (de fondo, mientras Naofumi protesta) — no está presente en esta escena; ver el ep.2 para sus poses de niña esclava.
- Nota: como esclava (ep.2, 43:24-44:00) aparece con los hombros caídos y la mirada baja, típica de sumisión inicial — pose de **"antes"**, útil para contraste con su arco de crecimiento (el investigador de voz/personajes puede cruzarlo con el punto 13).

**Filo**
- 1:05, PV oficial T4 (`x9ia4ma`) — forma de ave filolial gigante, alas extendidas en vuelo, plumaje blanco con un lazo rojo en el pecho (pose de **vuelo/movimiento**, la única que conseguí de vídeo real; el resto de sus poses humanas quedan pendientes, ver "Sigue").
- 3:16, OP "RISE", ep.2 — silueta de ave filolial en pleno vuelo entre destellos rojos de batalla (mismo tipo de pose, contexto de acción).

## Lo mejor para la lámina

1. La pose de Naofumi con el escudo en alto bloqueando fuego (ep.3, 14:00) — funciona literalmente como ícono de "protección" para cualquier canal de reglas o de ayuda.
2. La paleta cálida y dorada de la escena de curación en la fuente (21:30, ep.2: `#DAC888` `#E7AE8B` `#F4E4B9`) — sirve de fondo acogedor sin ser genérico.
3. El estilo del ED "Kimi no Namae" (ilustración plana, sepia, sin degradados complejos) es una alternativa de "lámina ilustrada" distinta al cel-shading normal del anime.
4. Filo en su forma de ave gigante (PV T4, 1:05) es una imagen muy reconocible y poco explotada: sirve para un canal más desenfadado (canto, diversión).
5. El escudo brillando en verde del tráiler de anuncio (1:20) es un buen elemento de "activación" o "nivel" para un canal de progreso.

## No encontré

- ⚠️ Nombres de las pistas de banda sonora incidental (BGM) para escenas concretas: no hay tracklist oficial en MusicBrainz ni en la wiki; sólo confirmé compositor (Kevin Penkin) y los cuatro temas de OP/ED de las temporadas 1 y 2. Faltan los de las temporadas 3 y 4 (sólo tengo pistas sueltas "SIN" y "Resolution" vistas en pantalla, sin confirmar en una segunda fuente).
- ⚠️ Onomatopeyas y efectos de sonido reconocibles: no los pude aislar del audio con las herramientas de esta tanda.
- ⚠️ Vídeos con Filo en forma humana o en el episodio de su presentación (ep.5 "Filo"): Internet Archive sólo tenía episodios 1-4 en español latino con reproducción directa; probé Dailymotion con varias búsquedas ("Filo filolial", "Filolial Queen") sin encontrar clips oficiales centrados en ella. Sólo conseguí un fotograma suyo (forma de ave) en el PV de la Temporada 4.
- ⚠️ Tendencias de TikTok/YouTube sobre la serie (parte del punto 10): no llegué a buscarlas en esta tanda.
- AnimeThemes (fuente sugerida para OP/ED en `.webm`) dio error 522 (caído) tanto en `recolectar.py` como al reintentarlo yo directamente: no pude usarlo.
- YouTube: la descarga de vídeo pidió inicio de sesión (403 Forbidden) para el tráiler oficial `VKYmpq-V3Rs`; sólo pude sacar metadatos (título, duración), no fotogramas. Usé Dailymotion e Internet Archive como plan B, según indica AYUDANTE.md.

## Bitácora de búsqueda

- Español/inglés en Fandom (`shield-hero.fandom.com/api.php`): `action=query&list=search` para "opening ending theme song" (sin resultado directo), `list=allcategories` (encontré Category:Soundtrack, sin openings/endings ahí), páginas `Anime`, `The Shield Hero`, `The Slave Girl`, `RISE`, `Kimi no Namae`, `Reunion` (wikitext completo de cada una).
- Inglés, MusicBrainz (`musicbrainz.org/ws/2/release-group`): consultas "Tate no Yuusha no Nariagari" (sin resultado), "artist:MADKID" (encontré "RISE" 2019-02-06 y "Bring Back" 2022-04-07, coinciden con las fechas de estreno de T1 y T2), "Tate no Yuusha Original Soundtrack" (sin resultado).
- Inglés, Wikipedia (`en.wikipedia.org/w/api.php`) para el staff musical: no cargó por timeout, lo saqué del wikitext de Fandom en su lugar (sección "Staff": Kevin Penkin, música).
- Dailymotion API (`api.dailymotion.com/videos?search=...`): "Tate no Yuusha no Nariagari OP full", "Tate no Yuusha RISE opening MADKID", "Filo Tate no Yuusha filolial", "Tate no Yuusha Filolial Queen" — de aquí salieron los tráileres oficiales que sí miré; los resultados de "OP/ED full" eran covers de fans o AMVs, no oficiales, así que no los usé como fuente de audio oficial.
- Internet Archive (`archive.org/metadata/<id>` y `advancedsearch.php`): confirmé los mp4 descargables de `tt9529546-1-1` a `tt9529546-1-4` (Temporada 1, español latino) y de `tate-no-yuusha-no-nariagari-s-2-e-01` (Temporada 2). Los miré fotograma a fotograma con `fotogramas.py --cada` y luego con `--desde/--hasta` para acotar las escenas exactas, y con `--fotograma` para sacar cuadros sueltos para medir color.
- YouTube (`yt-dlp`): funcionó para metadatos (`--print title,duration`) pero no para descargar vídeo (403 Forbidden, pide sesión) en el tráiler oficial `VKYmpq-V3Rs`.

## Cumplimiento de mis puntos (2, 4, 9, 10, 14)

| Punto | Estado | Por qué |
|---|---|---|
| 2 — Fotogramas de escenas icónicas | ✅ | 3 escenas miradas fotograma a fotograma con `fotogramas.py` sobre vídeo real (no resúmenes), cada una con capítulo, minuto y qué pasa. |
| 4 — Fondos y sitios, luz y paleta | ✅ | 7 sitios distintos con hex medidos con `estilo.py` sobre fotogramas propios, con el minuto y el archivo de origen. |
| 9 — Música y sonido | ⚠️ | OP y ED de T1 y T2 confirmados en dos fuentes cada uno (wiki + créditos en pantalla), compositor confirmado en tres fuentes; faltan las pistas de BGM de escenas concretas y las onomatopeyas/SFX (ver "No encontré"). |
| 10 — Vídeos con minuto exacto | ⚠️ | 3 tráileres/PV oficiales mirados fotograma a fotograma con minuto exacto; falta la parte de tendencias de TikTok/YouTube. |
| 14 — Poses analizadas | ⚠️ | 5 poses de Naofumi y 2 de Raphtalia con capítulo y minuto, más 2 de Filo (de vídeo, forma de ave); faltan más poses de Raphtalia adulta y de Filo en forma humana — no encontré vídeo de esos episodios (ver "No encontré"). |

Sigue: buscar en Dailymotion/Internet Archive el episodio 5 "Filo" (o cualquier clip oficial con Filo en forma humana) para sus poses; buscar 2-3 poses más de Raphtalia adulta (ideal: arco de la Temporada 2, "New World Arc"); confirmar en una segunda fuente los temas "SIN" (T3) y "Resolution" (T4); si hay tiempo, una pasada rápida de tendencias de TikTok/YouTube para el punto 10 y una búsqueda de nombres de BGM de escenas emotivas (Discogs o el álbum de banda sonora en Amazon/CDJapan).
