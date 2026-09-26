# Vídeo · The Apothecary Diaries (El diario de la boticaria) — encargo 91

Investigador de vídeo. Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Serie sin canal propio
todavía. Sin serie hermana declarada en `encargos/91-*.md` (no hay otro encargo de
esta obra en `encargos/`; comprobado con `grep`).

Comprobación de partida (obligatoria antes de fiarse de `datos-video.md`): AniList
161645 = confirmado por API GraphQL propia (`Media(id:161645)` → romaji "Kusuriya
no Hitorigoto", english "The Apothecary Diaries") ✅, mismo id que usó el
investigador de imagen. El tráiler de AniList (`oyHqh8ue4zw`, YouTube, bloqueado
en este servidor) tiene gemelo en Dailymotion (`x8mmgoz`, mismo tráiler de 2:33,
verificado fotograma a fotograma: título "薬屋のひとりごと / The Apothecary Diaries"
y "TVアニメ 2023年放送決定" en pantalla) ✅ — es el mismo tráiler, no otra obra.
**Aviso sobre `datos-video.md`:** el bloque "Bandas sonoras publicadas
(MusicBrainz)" está casi todo mal filtrado por buscar sólo la palabra "Diaries":
de las 14 entradas sólo las **4 primeras** (con título en japonés 薬屋のひとりごと)
son de esta obra ✅; las otras 10 (*Vodka Diaries*, *Chernobyl Diaries*, *Ranchi
Diaries*, *The Nanny Diaries*, *The Princess Diaries* ×4, *Dhobi Ghat (Mumbai
Diaries)*, *Beyond Skyrim Dev Diaries*, *Red Shoe Diaries*) son bandas sonoras de
otras películas/juegos sin relación — las descarto todas. El resto de
`datos-video.md` (Dailymotion, Internet Archive) sí es de esta obra, comprobado
por título y por mirar los vídeos.

## 2 · Fotogramas de escenas icónicas (capítulo y minuto)

Miradas con `fotogramas.py` sobre el tráiler oficial (Dailymotion, gemelo del de
AniList) y sobre el episodio 1 en inglés (Internet Archive, BD 720p — bajado por
tramos con `--desde/--hasta`, nunca el archivo entero de golpe).

- Tráiler oficial (2:33, Dailymotion `x8mmgoz` = mismo que YouTube `oyHqh8ue4zw` de AniList): té en jardín con Maomao de gala (0:05-0:10), trébol de 4 hojas en primer plano (0:15), corredor de palacio con farolillos rojos y damas en fila (0:20-0:25), silueta en un tejado al atardecer (0:25), Jinshi de perfil sonriendo con picardía (0:45), Maomao cargando una caja (0:50), primer plano extremo de un ojo (prueba de veneno, 1:15), mano sujetando un cuchillo (1:40), figura saltando de espaldas contra el cielo nocturno (1:50) · fuente https://www.dailymotion.com/video/x8mmgoz?start=5 (y sucesivos `?start=`) · ✅ (mismo tráiler indexado también como `x9xnk6i`, subido por otro canal) · minuto exacto de cada fotograma
- Episodio 1 (inglés, Internet Archive `anime-pahe-kusuriya-no-hitorigoto-eng-dub-01-bd-720p-sam.mp-4-kw`): cold open con flor naranja en negro (0:20-0:40, presenta el motivo floral del OP), OP1 "Hana ni Natte" con Maomao envuelta en pétalos (1:00-1:40), mercado de la capital con Maomao regateando "If you want to gawk, pay up!" (2:20), Maomao secuestrada y envuelta en tela dándose cuenta "Yikes!" (3:20), nacimiento del príncipe en flashback (4:40), vista aérea del palacio trasero completo (5:30), primer plano resignado de Maomao "I guess, at the very least, I get paid" (6:30), patio nocturno en azules fríos (8:00), casa de té con cotilleo sobre las consortes (8:30-9:30), retrato de Gyokuyou entre flores lilas (9:15) · fuente https://archive.org/details/anime-pahe-kusuriya-no-hitorigoto-eng-dub-01-bd-720p-sam.mp-4-kw (episodio 1 completo, doblaje inglés, con subtítulos en pantalla) · ✅ (la misma escena de la vista aérea del palacio se repite como fondo de pantalla oficial en la wiki, y el diseño de Gyokuyou coincide con su ficha de personaje) · minuto exacto arriba

## 4 · Fondos y sitios: luz y paleta medida

Colores medidos con `estilo.py` (Pillow) sobre fotogramas propios del episodio 1
(no de arte promocional, para que la luz sea la real de escena).

- **Palacio trasero, vista aérea de día** (ep.1, 5:30): paleta #69696E, #C69062, #938182, #464149, #C3B9BB, #74AFC7 — tejados naranja/teja sobre muros grises, luz plana de mediodía, saturación baja (28%) y brillo medio (60%); sombreado degradado con mucha línea fina (#7E685B) para las tejas · fuente fotograma propio (`fotograma_00330.jpg`, medido con estilo.py) ✅ (el mismo complejo de tejados naranjas se repite en todos los planos exteriores del palacio del resto del episodio)
- **Patio de palacio de noche** (ep.1, 8:00): paleta #1E1832, #16204E, #0F1120, #243468, #3D507E — azules casi negros, sombreado degradado con poca línea, saturación alta para lo oscuro (58%) y brillo muy bajo (26%): la serie usa el azul noche cerrado (casi sin negro puro) para las escenas nocturnas de palacio · fuente fotograma propio (`fotograma_00480.jpg`) ✅ (mismo tono de azul nocturno en el tráiler, fotograma 1:50)
- **Retrato de consorte con fondo floral** (Gyokuyou, ep.1, 9:15): paleta #DCE4F1, #58497D, #BDC7E3, #F8DDDA, #8C7FC2, #D89DAC — pasteles lilas y rosas, brillo muy alto (83%) y saturación baja (22%), línea normal (#7B738F): es la paleta que la serie reserva para presentar a una consorte importante (fondo decorativo con flores, no un fondo realista) · fuente fotograma propio (`fotograma_00555.jpg`) ✅ (mismo tratamiento de fondo floral pastel en las fichas de personaje "Anime Design" de la wiki, ya medidas por el investigador de imagen con otros hex de vestuario)
- Contraste: exteriores de día = paleta cálida tierra/naranja de baja saturación (edificios, mercado); interiores/noche de palacio = azules fríos oscuros; escenas de "presentación de personaje" = fondo decorativo pastel casi monocromo. Sirve de guía de luz para la lámina.

## 9 · Música y sonido

Openings y endings confirmados en la wiki de Fandom (wikitext propio de la
página `.../anime songs S1` y `S2`), cada uno con su fuente cruzada (ANN,
Crunchyroll News, natalie.mu o la web oficial, citadas dentro del wikitext).

| Temporada | Opening | Ending | Episodios |
|---|---|---|---|
| S1 (1.ª mitad) | "Hana ni Natte" (花になって) — Ryokuoushoku Shakai | "Aikotoba" — AiNA THE END | ep. 1-12 |
| S1 (2.ª mitad) | "Ambivalent" — Uru | "Ai wa Kusuri" — wacci | ep. 13-24 |
| S2 (1.ª mitad) | "In Bloom" / 百花繚乱 — Lilas Ikuta | "Shiawase no Recipe" — Dai Hirai | ep. 1-12 (S2) |
| S2 (2.ª mitad) | "Kusushiki" (Mysterious) — Mrs. GREEN APPLE | "Hitorigoto" (Soliloquy) — Omoinotake | ep. 13+ (S2) |
| **S3 (estreno 2-oct-2026, ¡recién anunciado!)** | "Kumo wo Nuke Kazashimo e Watashi Dake" — Yorushika | "Aiyou" — Eve | desde ep. 1 (S3) |

- OP1 S1 "Hana ni Natte" y ED1 S1 "Aikotoba" **vistos** en el tráiler-remix oficial de Dailymotion (`x8ogai7`, "Trailer: OP — Green Yellow Society [=Ryokuoushoku Shakai], ED — Aina The End"): el OP muestra a Maomao rodeada de pétalos y palomas sobre los tejados de palacio (0:03-0:45), el ED corre sobre fondo nocturno con Jinshi de espaldas mirando la luna llena y el texto "アイナ・ジ・エンド「アイコトバ」" en pantalla confirmando la canción (1:12-1:27), cierra con el eslogan "毒を、暴け" ("Desenmascara el veneno") y "〈薬屋の少女〉が挑む謎解きエンタテイメント" ("el misterio que resuelve la chica de la botica") · fuente https://www.dailymotion.com/video/x8ogai7?start=15 · ✅ (wiki confirma autoría e imagen de infobox `KusuriyaHitorigoto-Anime-S01-...png` igual a lo visto) · minuto exacto arriba
- El propio OP1 vuelve a sonar al arrancar el episodio 1 (Internet Archive, doblaje inglés), con subtítulos de la letra traducida en pantalla: "Fretting over it is a waste of time" / "Be a flower! C'mon, bare that cynical smile" (0:40-2:00) · fuente episodio 1 completo, minuto propio ✅
- Compositores de la banda sonora original (los 3 openings/endings de arriba y el score): **Satoru Kōsaki**, **Kevin Penkin** y **Arisa Okehazama** (créditos repetidos en MusicBrainz para los 4 álbumes de OST S1/S2 y confirmados de nuevo para S3 en la nota de prensa de Anime Corner, ago-2026) · ✅ (MusicBrainz + Anime Corner)
- Canciones insertadas en momentos clave de S1 (cada una con su propio artista, distinta del OP/ED, para remarcar una escena concreta): "Omoi Kaze" (Yuiko Ōhara, ep. 3), "Ashita wo Tazunete"/"Towards the Light" (XAI, ep. 9), "Setchūka"/"Flower in the Snow" (Kanako Kishi, ep. 12, cierre de arco), "Sōkū no Honō"/"Blaze of Clear Sky" (Daichi Takenaka, ep. 19), "Omoi Saku Toki"/"When Wishes Bloom" (Aoiema, ep. 24, final de temporada) · fuente wiki (una página por canción, con enlace a Spotify que confirma el artista) ⚠️ (una sola fuente para la escena exacta de cada una; el artista sí tiene doble fuente wiki+Spotify/VGMdb)
- Insertada en S2: "Inochi no Tomoshibi" (Rimu Miyake, ep. 47 = ep.23 de S2) · misma fuente ⚠️
- **Efectos de sonido y onomatopeyas reconocibles** (créditos de librería de foley de la wiki especializada `soundeffects.fandom.com`, vía su API porque la web normal da 403 con navegador): la serie usa mucho la librería clásica de gags Hanna-Barbera/Sound Ideas para sus momentos de comedia — "Anime Sparkle Sound" (el brillo en los ojos cuando Maomao se emociona por un veneno nuevo, visto en el tráiler-remix a 0:15), silbido descendente "Hollywoodedge, Slide Whistleup" (caídas o golpes cómicos), "Sound Ideas, CARTOON - BOING" (rebotes), un maullido de gato individual ("CAT - DOMESTIC: SINGLE MEOW") como acento cómico, y el chirrido de rueda metálica grave "Hollywoodedge, Lg Metal Wheel Creak" **descrito explícitamente como el sonido de Maomao limpiándose/apartándose cada vez que toca algo de Jinshi** (gag recurrente de "insensibilidad" hacia él) · fuente https://soundeffects.fandom.com/wiki/The_Apothecary_Diaries (api.php) ✅ (categoría de la propia wiki "Shows That Use Hanna-Barbera Sound Effects" agrupa la serie con el resto de anime que comparte librería, mismo patrón que otras fichas de esa wiki) · sirve directo para el punto 6 (onomatopeyas) y el 18 (filtros/efectos)

## 10 · Vídeos: tráilers, análisis y tendencias

- **Tráiler oficial S1** (2:33): Dailymotion `x8mmgoz` (mismo que YouTube `oyHqh8ue4zw` de AniList) — ver fotogramas del punto 2 · ✅ (repetido como `x9xnk6i`)
- **Teaser S1** (2:11), dos subidas iguales: Dailymotion `x8rxzrg` y `x8rxzrl` · fuente `datos-video.md` (Dailymotion) ✅ (mismo teaser, dos canales)
- **Tráiler "The Deceased Empress' Treasure"** (0:51, arco de S2/S3 sobre el tesoro de la emperatriz fallecida): Dailymotion `xaktjqy`, por el canal Espinof · fuente https://www.dailymotion.com/video/xaktjqy ⚠️ (una sola fuente, no llegué a mirarlo fotograma a fotograma por presupuesto de acciones)
- **Teaser de temporada 2** (0:52): Dailymotion `x8vm652` (Espinof) ⚠️
- **Tráiler principal de temporada 3** (recién publicado, 15-ago-2026, canal oficial TOHO animation en YouTube — bloqueado en este servidor, no lo pude bajar): estreno confirmado **2 de octubre de 2026**, adelanta el OP "Kumo wo Nuke Kazashimo e Watashi Dake" de Yorushika, presenta a Reina Ueda como la nueva "doncella inmortal" Bai Niangniang, estudio de animación OLM (TOHO animation STUDIO ya no aparece en los créditos de esta tanda) · fuente https://animecorner.me/the-apothecary-diaries-season-3-reveals-new-trailer-visual-opening-theme-by-yorushika-october-2-premiere/ (Anime Corner, 15-ago-2026) ✅ (mismo anuncio recogido por Anitrendz, ComicBook.com y Hypebeast el mismo mes, según la propia búsqueda) — dato **muy reciente y de actualidad**, útil si la lámina se hace ahora
- Tras S3 (2 cours) se anuncia una **película** con historia original de la autora Natsu Hyuuga, estreno en Japón el 11-dic-2026 · misma fuente Anime Corner ✅
- **Vídeos de análisis en YouTube** (bloqueado el vídeo en sí en este servidor; título y enlace confirmados por búsqueda web, sin poder mirarlos fotograma a fotograma): *"The Hidden Message Nobody Noticed: Apothecary Diaries Video Essay"* (youtube.com/watch?v=CtSsIpauXWo), *"Chinese Dude Nitpicks The Apothecary Diaries"* del canal Accented Cinema (youtube.com/watch?v=2ko425hm6pw, análisis crítico de ritmo y traducción), *"When Loyalty Becomes DANGEROUS"* (youtube.com/watch?v=zEsTwQZelfM, sobre las damas de compañía del harén), *"The ENTIRE Story Of The Apothecary Diaries (so far) In 83 Minutes"* (resumen narrativo, youtube.com/watch?v=G5kIyw3s1IU) · ⚠️ (un solo dato: título+enlace, sin metadatos verificados porque yt-dlp da "Sign in to confirm you're not a bot" incluso sin descargar)
- **Tendencias de TikTok** (confirmadas por búsqueda, no se puede abrir TikTok con curl/navegador sin sesión desde aquí): edits de "Twins at the Carousel" (con Maomao, Xiaolan y Shisui), compilaciones "Animal x Maomao", la "escena del baile" citada como "la escena más bonita de la serie" en ediciones de fans, momentos de Jinshi asustado, y edits sobre la elección de concubina del emperador y la amistad Emperador-Maomao · fuente búsqueda web (tiktok.com/discover, varias etiquetas) ⚠️ (no verificable con una segunda fuente ni con vistas exactas, TikTok no da API pública aquí)

## 14 · Poses analizadas en varias escenas (por personaje, con capítulo y minuto)

Sacadas de mirar el tráiler oficial y el episodio 1 completo (doblaje inglés,
Internet Archive) fotograma a fotograma con `fotogramas.py`, no de memoria ni
sólo de arte promocional. Postura, manos y mirada descritas de lo que se ve.

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Maomao camina por el corredor de palacio cargando una bandeja de comida con las dos manos, mirada baja, hombros caídos | Ep. 1 | 5:00 | presentar (ella misma, su trabajo diario) |
| Maomao de perfil, ojos entornados, boca en línea recta, resignada («I guess, at the very least, I get paid») | Ep. 1 | 6:30 | pensar |
| Maomao sentada comiendo con Xiaolan, cuchara a medio camino de la boca, mejillas relajadas | Ep. 1 | 14:00 | animar / socializar |
| Maomao envuelta en tela al ser secuestrada, ojos muy abiertos, cejas arqueadas, boca en «O» | Ep. 1 | 3:20 | sorpresa / regañar (reacción cómica) |
| Maomao de pie firme ante Jinshi y Gyokuyou, explicando la causa del veneno (postura recta, barbilla algo alzada) | Ep. 1 | 18:30-19:00 | explicar |
| Maomao (primer plano extremo del ojo) concentrada probando un veneno, párpado entornado, pupila fija | Tráiler oficial | 1:15 | pensar / concentración |
| Maomao sosteniendo un cuchillo con mano firme, muñeca girada hacia arriba | Tráiler oficial | 1:40 | regañar / acción defensiva |
| Maomao de perfil cargando una caja/bandeja con ambos brazos, torso ligeramente inclinado hacia adelante | Tráiler oficial | 0:50 | presentar |
| Jinshi de perfil, sonrisa ladeada, un ojo entornado (mirada pícara característica) | Tráiler oficial | 0:45 | presentar / celebrar |
| Jinshi de pie solo en el corredor, manos ocultas en las mangas, mirando de frente a cámara («I was given to understand that you couldn't read») | Ep. 1 | 16:00 | regañar / poner a prueba |
| Jinshi mirando hacia abajo y a un lado, ceño ligeramente fruncido, pensativo tras la respuesta de Maomao | Ep. 1 | 17:30-18:00 | pensar |
| Jinshi de pie junto a Gyokuyou, gesto abierto de mano hacia Maomao, («What can I do for you?») | Ep. 1 | 20:00 | explicar / negociar |
| Jinshi saltando de espaldas contra el cielo nocturno, capa/manga ondeando, brazos extendidos | Tráiler oficial | 1:50 | celebrar / acción |
| Gyokuyou primer plano, ojos húmedos, ceja caída, mano cerca de la boca («I should have paid more attention…») | Ep. 1 | 19:30 | (secundaria) culpa / arrepentimiento — dinámica con Maomao |

- Nota de dinámica de grupo (sirve para láminas en pareja): la escena de las
  16:00-19:00 del episodio 1 es el **primer cara a cara real** de Maomao y
  Jinshi — él la pone a prueba de pie, ella responde con la deducción del
  veneno; sus posturas son opuestas (él relajado/de perfil, ella firme/de
  frente) y se repite como referencia de composición en el arte promocional
  (las poses "vivas" que pide el punto 1, ya cubiertas por el investigador de
  imagen con las fichas de diseño oficiales).

