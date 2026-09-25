# Imagen · Kakegurui — puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md

Parte del investigador de **imagen**. Sigue desde `partes/datos-imagen.md` (no
repite esas consultas) y desde las secciones 3-5, 16 y 17 de la `biblia.md`
vieja (hecha con la red cerrada, casi todo ⚠️). Aquí se confirma, se corrige y
se profundiza con la red abierta: 11 hojas de contacto nuevas (761→1051
imágenes de la wiki), licencias de Sketchfab por su API, colores medidos con
`estilo.py` sobre arte oficial, y colaboraciones/figuras que la biblia vieja
no tenía.

## Hallazgos

### Punto 1 · Arte oficial, en cantidad y variado

- Portada y banner oficiales de AniList: 230×320 y 1900×400 (medidos, son
  miniaturas; el original es más grande) · [portada](https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/b98314-TSJykxVwCCQN.jpg), [banner](https://s4.anilist.co/file/anilistcdn/media/anime/banner/98314-gwgiHiJOj2ls.jpg) · ✅ (AniList + `estilo.py` los abrió y midió paleta) · datos-imagen.md
- **761 imágenes → 1051 imágenes** de la wiki de Fandom (7 páginas: Yumeko,
  Kirari, Mary, Ririka, Midari, Runa, Student Council) montadas en **11 hojas
  de contacto** de 48 imágenes cada una en
  `herramientas/referencias/kakegurui/hoja_01.jpg`…`hoja_11.jpg`
  (`indice.json` con URL y tamaño real de cada original) ✅ (corrida propia,
  `investigar_serie.py`, 25-sep-2026). Las 3 mejores están en `hojas/` de esta
  biblia (ver más abajo qué trae cada una).
- Key visual de **×× (2019)**: 23 personajes, Yumeko y Kirari arriba; se
  publicó el 20-nov-2018 ✅ ([LisAni!](https://www.lisani.jp/0000117737/),
  [Animate Times](https://www.animatetimes.com/news/details.php?id=1542685544)),
  con hojas de personaje nuevas en [PASH! PLUS](https://www.pashplus.jp/anime/117240/).
  Ya estaba en la biblia vieja; se confirma igual.
- **«Gambling-School Visual.jpg»** (1499×2048, wiki): key visual de grupo con
  varios alumnos alrededor de una mesa de juego, colores planos rojo/negro ✅
  (medido por la API de la wiki) · hoja `personajes_01.jpg`, número 46.
- **«12 Gamers Bromide.png»** (1689×2498): postal/bromide oficial de 12
  personajes juntos, pose de grupo formal — sirve para la dinámica «con
  amigos» que pide el dueño ⚠️ (una fuente, la wiki; no hay fecha de edición
  del objeto físico).
- Portadas de **tomos y capítulos vistas directamente** en las hojas (números
  de `personajes_01.jpg` y `personajes_02.jpg`): Volumen 1, 10, 11, 12, 14,
  15, 16, 18, 20; Twin 6, 8, 9, 12, 13, 14; Kakkokari (spin-off cómico) 3, 4,
  5, 6; capítulos sueltos 71-121 y «Bonus Chapter» 11, 13, 15, 16 ✅ (vistas +
  wiki). Cubren mucho más que «un par de imágenes»: hay portada de acción
  (corriendo, cartas volando), de grupo, de retrato y de humor (Kakkokari).
- **Blu-ray**: BD1 T1 con cubierta dibujada por **Manabu Akita** (diseñador de
  personajes) ⚠️ (una fuente, [web oficial](https://www.kakegurui-anime.com/1st/discography/detail.php?id=1015051));
  caja de coleccionista con arte de **Tōru Naomura** (dibujante del manga) ⚠️
  (una fuente, [web oficial](https://kakegurui-anime.com/1st/discography/detail.php?id=1015068)).
  No se encontró una segunda fuente para ninguna de las dos en esta tanda: se
  mantiene ⚠️, no se puede subir a ✅ todavía.
- **Manga**: capítulo 1 gratis en [pixiv Comic](https://comic.pixiv.net/viewer/stories/4693),
  mejor referencia para ver los globos y el trazo reales (Naomura). Serie en
  [Gangan Joker](https://magazine.jp.square-enix.com/joker/series/kakegurui/).
  Portada de Kirari en color para **Gangan Joker de septiembre 2019**
  (891×1280, wiki) ⚠️ (una fuente).
- **Pachislot y pachinko oficiales** (arte promocional, poses muy distintas a
  «de pie»): **パチスロ 蛇喰夢子という女** (Net, 6.5-gō, instalada el
  3-jul-2023) y **eカケグルイ** (D-light/Daiichi Shōkai, dos versiones 7500 y
  219, instaladas el 11-may-2026) ✅ (dos fuentes cada una:
  [p-town.dmm.com/machines/4374](https://p-town.dmm.com/machines/4374) +
  [P-WORLD](https://www.p-world.co.jp/machine/database/9844) para la
  pachislot; [p-town.dmm.com/machines/5004](https://p-town.dmm.com/machines/5004)
  + [pachinkovillage.com](https://www.pachinkovillage.com/pachinko/p.php?M=7445)
  para la pachinko). **Miré las dos imágenes del gabinete**
  (360×550 cada una, medidas): la pachislot tiene a Yumeko con los ojos rojos
  de la locura mirando fijo, con «さぁ» en letras rojas grandes y a Yumeko y
  Kirari cara a cara abajo, gabinete rojo y negro; la pachinko (gabinete azul
  claro) tiene un primer plano de Yumeko mordiéndose la uña con sonrisa loca y
  rubor, rodeada de texto japonés y salpicaduras de tinta ✅ (visto,
  `estilo.py`/Read directo). También hay dato curioso: por regulación
  japonesa la máquina no puede llevar el kanji «賭» en su nombre comercial, por
  eso la pachinko se llama «eカケグルイ» en katakana ⚠️ (una fuente,
  ja.wikipedia.org, extracto propio).
- **Vídeojuegos oficiales de la franquicia** (imagen/arte, no la interfaz que
  es del investigador de texto): app móvil **賭ケグルイ チーティングアロード**
  (2018-11-20 a 2020-03-27) y navegador **賭ケグルイ ALL IN** (G123, lanzado
  23-mar-2026, sugoroku estratégico) ✅ (ja.wikipedia.org +
  [g123.jp/news/article/443078](https://g123.jp/news/article/443078?lang=ja)).
  Al lanzamiento, ALL IN regaló por X (Twitter) un **fondo de pantalla oficial
  para celular** con ilustración propia del juego a quien siguiera la cuenta y
  repostara ⚠️ (una fuente con el texto de la campaña; no se encontró el
  archivo de imagen en sí, sólo el anuncio).
- **SINoALICE** hizo un crossover con **Kakegurui ××** (anunciado 26-abr-2022)
  ✅ ([Anime News Network](https://www.animenewsnetwork.com/press-release/2022-04-26/sinoalice-has-started-a-collaboration-with-kakegurui-xx/.185026)) — puesto también en el punto 23.
- **Live action**: además del anime hay una **serie dramática** (T1 y T2,
  «Kirari drama season 1/1b/1c», Elaiza Ikeda como Kirari) y **películas**
  («Kakegurui movie.jpg»; «Kakegurui 2: Ultimate Russian Roulette», 2019) con
  fotos de elenco reales (ramos de flores, sesión de prensa) — visto en las
  hojas ⚠️ (una fuente, wiki; no se profundizó más por ser otro medio, fuera
  del encargo de imagen del anime/manga, pero sirve como referencia de
  vestuario real).

### Punto 3 · Fan art y 3D (sólo como referencia)

**Modelos 3D de objetos, con licencia confirmada por la API de Sketchfab**
(`api.sketchfab.com/v3/models/<uid>`, comprobado uno por uno, 25-sep-2026):

| Modelo | Autor | Licencia (API) | Para qué |
|---|---|---|---|
| [Low Poly Poker Chips & Cards](https://sketchfab.com/3d-models/low-poly-poker-chips-cards-8420090cc79a49d9a0b85f53c5074616) | designedbyjonathan | **CC BY 4.0** ✅ («Author must be credited. Commercial use is allowed») | fichas y cartas de relleno |
| [Casino Poker Table](https://sketchfab.com/3d-models/casino-poker-table-f36fc75d825148618aa6e5cbfb43f28e) | npowell | **CC BY 4.0** ✅ | la mesa |
| [Casino Poker Chip](https://sketchfab.com/3d-models/casino-poker-chip-b9efab875b9c4ac3a29ea5a0c7a260d1) | lejonlin | **CC BY 4.0** ✅ | ficha en primer plano |
| [Stylized Poker Table](https://sketchfab.com/3d-models/stylized-poker-table-game-asset-48fd86c57c2b497a900223d8f115f188) | MorganJ45 | **CC BY 4.0** ✅ | mesa, fichas, cartas y sillas |
| [Poker Table](https://sketchfab.com/3d-models/poker-table-a48473a5ae7c437496a7aa388f8c458b) | Badboy17Aiden | **CC BY 4.0** ✅ (antes ⚠️, ahora confirmado) | baraja entera y fichas, texturas 2048 |
| [Poker Chip Set](https://sketchfab.com/3d-models/poker-chip-set-b0cbee32720046e7b1e480cff44a5d41) | anna_bezzu (matveuk) | **CC BY-NC-ND 4.0** ✅ (antes ⚠️; **NO** vale para nada que se modifique o redistribuya, sólo mirar) | referencia de forma |
| [Poker Chip 500$](https://sketchfab.com/3d-models/poker-chip-500-3cd4d3b00c0349ad978d0c81d8f95409) | anna_bezzu | **CC BY-NC-ND 4.0** ✅ | referencia de forma |

Corrección sobre la biblia vieja: dos modelos que estaban con licencia ⚠️
(«gratis, licencia ⚠️») en realidad son **CC BY-NC-ND**: se pueden mirar y
usar como referencia, pero no se pueden modificar ni redistribuir (ni
regalar el `.blend` retocado). Para la lámina esto no cambia nada (es sólo
referencia), pero hay que decirlo si algún día se comparte el archivo 3D.

**Modelos 3D de personajes** (con copyright, sólo para girar la cámara y
entender la pose — nunca en la lámina):

| Modelo | Autor | Licencia (API) |
|---|---|---|
| [Yumeko](https://sketchfab.com/3d-models/yumeko-9834761e49a346cba73c8e1d9ab40122) | Yaanaa | **CC BY 4.0** ✅ (permite uso comercial, pero el personaje sigue con copyright de Square Enix/MAPPA) |
| [Mary Saotome](https://sketchfab.com/3d-models/mary-saotome-62bf9b36b5b64c29b27c8eadea263417) | acutee | **Sin licencia libre** ✅ (la API no devuelve licencia = todos los derechos reservados; sólo mirar en la página, no descargar) |
| [Runa Yomozuki](https://sketchfab.com/3d-models/none-70dafed89bcd4dd3b9f5654f90ebeef3) | Gustav_Johansson00 | **CC BY-NC** ✅ (datos-imagen.md, confirmado por recolectar.py) |

**Fan art 2D** (mirar, nunca pegar; ya estaba en datos-imagen.md y en la
biblia vieja, no se repite la búsqueda): pixiv (1.646 dibujos con la etiqueta
[賭ケグルイ 蛇喰夢子](https://www.pixiv.net/en/tags/%E8%B3%AD%E3%82%B1%E3%82%B0%E3%83%AB%E3%82%A4%20%E8%9B%87%E5%96%B0%E5%A4%A2%E5%AD%90)),
Safebooru (tamaños y autor/origen medidos, ver `datos-imagen.md`), DeviantArt
y ArtStation (Kirari a lápiz de William-Art, Mary de Esmerald1 y otros).

**Fotos con licencia libre de cosplay** (Openverse, ya en datos-imagen.md):
20 fotos CC BY-NC-SA 2.0 de timz2011 y otros (Yumeko, Mary, Runa), 683-1024 px
de lado, medidas ✅. Cosplay de referencia del uniforme:
[Imaginations Costume](https://www.imaginationscostumes.com/anime-kakegurui-yumeko-jabami-cosplay-uniform/).

### Punto 15 · Vestuario

**Texto oficial de la wiki** (sección «Appearance» de cada personaje,
`kakegurui.fandom.com`, ya en datos-imagen.md, ✅ fuente primaria de la wiki):

- **Yumeko**: pelo negro largo y grueso, corte hime, ojos «burgundy» que se
  ponen **rojo brillante** cuando se emociona; labios con brillo rosa, uñas
  pintadas de rojo (beige en la 1.ª temporada del anime). Uniforme: blazer
  rojo con ribete negro, camisa blanca, corbata cruzada negra, falda a
  cuadros negro y gris, medias negras, mocasines marrones. **Anillo de plata**
  en el pulgar izquierdo (de la boda de sus padres).
- **Mary**: ojos amarillo oscuro, pelo rubio largo en **coletas con lazos
  negros**. Mismo uniforme que Yumeko pero con **botones dorados** en el
  blazer. Falda **gris plisada** (no a cuadros como Yumeko). Maquillaje
  natural, labial rosa-beige.
- **Ririka**: cara casi siempre tapada por una **máscara blanca de teatro**
  (distorsiona la voz). Piel pálida, pelo platino largo (gris en el anime)
  con flequillo hime, labios con bálsamo rosa/melocotón, ojos celestes.
  Mismo uniforme; **no** usa labial ni esmalte salvo cuando se hace pasar por
  Kirari.
- Corrección: la máscara de Ririka es **blanca** (fuente textual de la wiki),
  no gris como decía la biblia vieja ⚠️→corregido con fuente directa; queda
  ✅ con la wiki en inglés.

**Colores medidos con `estilo.py`** sobre arte oficial (no de fans), con
Referer para `static.wikia.nocookie.net` ✅ (25-sep-2026):

| Imagen (oficial) | Paleta dominante medida |
|---|---|
| Portada AniList (key visual, escena nocturna) | `#832B27` `#AC3933` `#531B17` (rojos), `#1F1718`/`#070302` (negro), `#E4CEBC` (piel) |
| Banner AniList | `#18161E` `#0F0B0E` (fondo oscuro), `#461D1F`/`#922B30` (rojo), `#F4D5CB` (piel) |
| «Yumeko Kirari Love.png» (ilustración color oficial) | `#D63D2C` (rojo blazer), `#382234`/`#080612` (oscuros), `#DFD8DC` (blanco camisa) |
| «Kakegurui Love - Illustration of Mary Saotome and Yumeko Jabami» | `#E5392C`/`#C80812` (rojo blazer), `#F6E7D3`/`#E0AB8A` (piel), `#2A1B22` (negro) |
| «XX Rei + Kirari.jpg» (uniforme formal, pantalón) | `#C05051` (rojo), `#544C5A`/`#352D30` (grises oscuros) |

**Conclusión sobre el rojo del blazer**: la paleta de fans de color-hex.com
(`#C9020F`) sigue sirviendo como referencia rápida, pero el arte oficial
**varía entre `#C05051` y `#E5392C`** según la luz de cada ilustración (más
naranja en luz de día, más oscuro/vinoso en escenas nocturnas). Para la
lámina: usar un rojo medio, `#D6362A` aprox., y oscurecerlo si la escena es de
noche ✅ (medido en 5 imágenes oficiales distintas).

**Variantes de uniforme vistas en las hojas** (`personajes_01.jpg`,
`personajes_02.jpg`, `vestuario_03.jpg`):
- **Uniforme de verano femenino**: «Kirari Momobami in the female summer
  uniform version.jpeg» (1521×2160) ⚠️ (una fuente, wiki; no se ve en las
  hojas guardadas aquí pero está indexada).
- **Uniforme masculino** (Ryota, en «Team, Mary, Ryota.png»): blazer oscuro
  sin la falda, distinto del femenino ⚠️ (una fuente, visto en hoja).
- **Kimono de Año Nuevo**: Yumeko con kimono rojo estampado («Yumeko and Hana
  kimono», hoja 4, ficha #157-159) ⚠️ (visto, sin confirmar en texto de wiki
  todavía).
- **Perfumes oficiales con la ropa de cada una** dibujada en el frasco:
  «Yumeko perfume.png» y «Mary perfume.png» (1149×1500 cada uno, medidos por
  la API de la wiki) ✅ — ver punto 23, es colaboración/merchandising pero
  confirma cómo se dibuja el uniforme en producto oficial.

### Punto 16 · Ciudades, paisajes y fondos de pantalla

*(La luz y la hora del día medidas en fotograma son del investigador de
vídeo — punto 4 de ENCARGO.md. Aquí sólo los fondos de pantalla en alta con
tamaño y autor, que es mi punto.)*

**Fondos de pantalla de fans, medidos de verdad** (Wallhaven, ya en
`datos-imagen.md`, con tamaño real, corazones, subida por y origen — no se
repite la búsqueda, se listan los mejores para la lámina):

| Tamaño real | ♥ | Subido por | Origen | Enlace |
|---|---|---|---|---|
| 6752×4000 | 884 | Psychofruit | [Patreon](https://www.patreon.com/posts/yumeko-nsfw-39647346) | [wallhaven-832511](https://w.wallhaven.cc/full/83/wallhaven-832511.jpg) |
| 8102×2018 (doble monitor) | 183 | Dokkar | [pixiv 66560913](https://www.pixiv.net/member_illust.php?mode=medium&illust_id=66560913) | [wallhaven-1j5ze3](https://w.wallhaven.cc/full/1j/wallhaven-1j5ze3.jpg) |
| 6000×5050 | 111 | bubbleboba | — | [wallhaven-k7r6k6](https://w.wallhaven.cc/full/k7/wallhaven-k7r6k6.jpg) |
| 2600×4000 | 87 | MrFav | [X](https://x.com/MostlyBlueWyatt/status/1975312679415022067) | [wallhaven-k8xlym](https://w.wallhaven.cc/full/k8/wallhaven-k8xlym.png) |
| 1920×2463 | 152 | Mirokv | [ArtStation](https://www.artstation.com/artwork/34XkD) (Aoi Ogata) | [wallhaven-x1qzro](https://w.wallhaven.cc/full/x1/wallhaven-x1qzro.jpg) |

**Fondos que dicen «oficial»**: no encontré ningún fondo de pantalla
descargable en la web oficial (`kakegurui-anime.com`) — sólo el que regaló
**ALL IN** por X al lanzarse (ver punto 1/23), que es oficial pero de reparto
limitado por campaña, no un archivo público permanente ⚠️.
Las colecciones de AlphaCoders/WallpaperAccess/WallpaperCave de la biblia
vieja (más de 160 fondos) siguen ahí, pero sus tamaños («4K Ultra HD» en el
título) **no están medidos de verdad**: usar los de Wallhaven de la tabla de
arriba, que sí lo están.

**Sitios de la serie** (para que el investigador de vídeo mida su luz):
Academia Hyakkaou (122 años, exterior occidental/interior de mármol y
madera), sala del consejo (con el acuario), aula 2.º Flor, club de Cultura
Tradicional, escalera central — todo esto ya en la biblia vieja §5.1, con
fuente en subtítulos, no se repite.

**Corrección sobre la luz del acuario**: la biblia vieja decía «de memoria»
que la sala del consejo tiene luz **azul verdosa**. Al medir con `estilo.py`
un fotograma real del anime («Kakegurui anime episode 6 Kirari Momobami
profile image», wiki, 1280×720) la paleta dominante da
`#D5DE3E` `#B0B62D` `#65641F` — es decir, **amarillo-verde/oliva**, no azul.
Puede ser el reflejo del acuario en una escena distinta a la que yo imaginaba,
así que lo dejo como ⚠️ **corregido a medias**: hay luz verdosa confirmada por
imagen, pero el matiz exacto (verde-azul o verde-amarillo) depende de la
escena y lo debe fijar quien mire el capítulo completo con `fotogramas.py`
(video).

### Punto 19 · Texturas 2D

- **Tramas de manga (screentone) y grosor de línea**: visto directamente en
  ~40 páginas interiores en blanco y negro dentro de las hojas de contacto
  (por ejemplo números 58, 63, 67, 74, 90, 130, 149, 163-164, 170-172 de
  `personajes_02.jpg`/`vestuario_03.jpg`): pelo negro **relleno sólido**, muy
  poca trama de puntos (screentone) salvo en sombras de fondo y en las «caras
  de la locura» (rayas finas radiales alrededor de los ojos cuando un
  personaje se obsesiona), líneas de contorno **gruesas y limpias**, sin
  textura de papel visible (impresión digital) ✅ (visto, Read directo).
- **Equivalente libre de trama de manga**: [Manga Screentone Pack 1
  (gratis)](https://assets.clip-studio.com/en-us/detail?id=2142037) en CLIP
  STUDIO ASSETS ⚠️ (una fuente; comprobar la licencia exacta del asset al
  bajarlo, CSP la marca «gratis» pero es de un tercero).
- **Grano de papel / textura de impresión** equivalente libre (CC0):
  [ambientCG Paper001](https://ambientcg.com/view?id=Paper001),
  [Paper005](https://ambientcg.com/view?id=Paper005),
  [Paper006](https://ambientcg.com/view?id=Paper006) ✅ (ambientCG es CC0
  siempre, catálogo comprobado por API).
- **Cartón** para la caja de cartas/objetos del consejo:
  [ambientCG Cardboard002](https://ambientcg.com/view?id=Cardboard002), CC0 ✅.
- **Patrón de la falda a cuadros** (Yumeko: negro y gris; Mary: gris liso
  plisada): equivalente libre más cercano,
  [TextureCan: Red Tartan Pattern Fabric](https://www.texturecan.com/details/595/)
  (hay que recolorear a gris/negro, la textura es libre PBR) ⚠️, y
  [Raw Catalog: Tartan Pattern Cloth](https://www.rawcatalog.com/asset/3450/)
  (CC0) ⚠️ comprobar licencia exacta al bajar.
- **Emblema o escudo de la Academia Hyakkaou**: **no lo encontré**. Busqué
  «emblem», «crest», «badge», «insignia» en el texto de la wiki en inglés y
  «校章»/«エンブレム»/«紋章» en el extracto de ja.wikipedia.org: ningún
  resultado describe un escudo propio del colegio (⚠️ no existe ≠ no lo
  encontré: puede estar sólo en un fotograma que no miré). Lo único parecido
  es el **logo de la serie** (ya cubierto por tipografía, no es mío).
- **Cartas de juego**: el patrón de la baraja oficial
  («賭ケグルイ オールスール箔押しトランプ», con estampado metálico) no tiene
  imagen pública que yo encontrara; para textura de cartas, las figuras
  ARTFX J (ver punto 23) muestran de cerca el dorso y las caras de las cartas
  con un patrón de rombos rojo y negro repetido en la base de la figura ✅
  (visto directo en la imagen del producto).

### Punto 23 · Colaboraciones y cruces

Esta sección estaba casi vacía en la biblia vieja (sólo cosplay y la mención
de la gacha interna). Con la red abierta encontré bastante, todo en
`collabo-cafe.com` (agregador japonés de eventos, cruzado con una segunda
fuente cuando la hay):

| Colaboración | Cuándo | Qué es | Fuente(s) | Estado |
|---|---|---|---|---|
| **Karaoke no Tetsujin** × Kakegurui | 15-sep a 5-nov-2017, 7 locales (Ikebukuro, Shinjuku, Shibuya, Kanda, Machida) | Decoración y menú temáticos en una cadena de karaoke | [collabo-cafe](https://collabo-cafe.com/events/collabo/kakegurui-karatetsu/) | ⚠️ una fuente |
| **Myoujin Cafe** × Kakegurui (colaboración n.º 7 del café) | 30-ago a 1-oct-2017 (con extensión) | Menú especial «con mucho elemento de apuestas», bebidas con imagen de personaje | [collabo-cafe](https://collabo-cafe.com/events/collabo/kakegurui-myoujin-cafe/) | ⚠️ una fuente |
| **Kakegurui Cafe** en **Princess Cafe** (4 locales) | 27-abr a 31-may-2019 | Café oficial de Kakegurui ×× (MAPPA), menú temático, posavasos de regalo | [collabo-cafe](https://collabo-cafe.com/events/collabo/kakegurui-princess-cafe2019/) | ⚠️ una fuente |
| **SINoALICE** × Kakegurui ×× | anunciado 26-abr-2022 | Crossover de juego para móvil: personajes/objetos de Kakegurui dentro de SINoALICE | [Anime News Network](https://www.animenewsnetwork.com/press-release/2022-04-26/sinoalice-has-started-a-collaboration-with-kakegurui-xx/.185026) | ✅ (ANN + listado en Fandom «List of Kakegurui animated media») |
| **賭ケグルイ展** (Exposición Kakegurui) Tokio/Fukuoka/Osaka | desde 4-feb-2023 (firma de Kawamoto el 11-feb en Tokio) | Expone páginas originales del manga e ilustraciones a color; imagen 1280×803 medida | [collabo-cafe](https://collabo-cafe.com/events/collabo/kakegurui-exhibition-tokyo-fukuoka-osaka-2023/) | ⚠️ una fuente, pero con imagen propia y crédito «© Homura Kawamoto・Toru Naomura・Kei Saiki・Taku Kawamura・Yuichi Hiiragi / SQUARE ENIX» |
| **ARTFX J** figuras a escala de **Yumeko** y **Mary** (Kotobukiya), reproducción | anuncio de reproducción 20-oct-2024 | Figuras de acción: cartas volando, pelo al viento, pose dinámica de «lanzar cartas» | [collabo-cafe](https://collabo-cafe.com/events/collabo/kakegurui-reproduction-figure-ktobukiya-anime-store-goods2024/), imagen 2002×1082 medida | ✅ (collabo-cafe + imagen con copyright oficial visible) |
| **Union Creative** figura 1/6 de **Mary Saotome** | anuncio 20-sep-2025, venta marzo 2026 | Uniforme, sonrisa de «ya gané», cartas cayendo, base de mesa de casino | [collabo-cafe](https://collabo-cafe.com/events/collabo/kakegurui-mary-scale-figure-union-creative-anime-store-goods2025/), imagen 1200×615 medida | ⚠️ una fuente (pre-venta, aún no lanzada al 25-sep-2026) |
| **PALE TONE series** (Contents Seed): acrílicos y llaveros repintados en acuarela | anuncio 11-nov-2024, venta feb-2025; vol. 3 en 2025 | Yumeko, Kirari, Mary y Ryota en estilo pastel | [collabo-cafe vol.1](https://collabo-cafe.com/events/collabo/kakegurui-pale-tone-series-contents-seed-anime-store-goods2024/), [vol.3](https://collabo-cafe.com/events/collabo/kakegurui-pale-tone-series-vol3-contents-seed-anime-store-goods2025/) | ⚠️ una fuente |
| **Perfumes oficiales** Yumeko y Mary (marca フェアリーテイル/«essential-japan») | — | Eau de Parfum: Yumeko con nota almizclada+floral («adicta al juego, elegante»); Mary con nota floral exótica | imágenes en la wiki (1149×1500 cada una) + [essential-japan.com](https://essential-japan.com/news/kakegurui-perfume/) | ✅ dos fuentes (wiki + reseña) |
| **Pachislot/pachinko** (ver punto 1) | 2023 y 2026 | Máquinas recreativas con arte propio | ver tabla del punto 1 | ✅ |
| **Cosplay** | continuo | Ver punto 3: 20 fotos CC BY-NC-SA en Openverse, más [Imaginations Costume](https://www.imaginationscostumes.com/anime-kakegurui-yumeko-jabami-cosplay-uniform/) para patrón de costura | datos-imagen.md | ✅ |

No encontré colaboraciones con marcas fuera de Japón (tipo Fortnite o un
gacha global grande): puede que no existan para esta serie, o que estén en
chino/coreano y no las busqué en esos idiomas todavía (queda pendiente si
hace falta más profundidad).

## Las hojas de contacto (en `hojas/`)

Elegí 3 de las 11 generadas (todas en
`herramientas/referencias/kakegurui/hoja_*.jpg`, con `indice.json` con la URL
real de cada imagen para bajar cualquiera en grande):

1. **`personajes_01.jpg`** (=hoja_01, imágenes 1-48): portadas de tomo y de
   capítulo, ilustraciones a color, «Ace Cards.png» (cartas sueltas),
   fotos de coleccionable «Team, Mary, Ryota» y «The Avengers» (grupo, pose de
   acción). Sirve para el punto 1 (variedad) y como referencia rápida de
   portadas para el redactor.
2. **`personajes_02.jpg`** (=hoja_02, imágenes 49-96): serie de ilustraciones
   oficiales «Kakegurui Love» (Yumeko y Mary en color, fondo simple, buena
   referencia de paleta — es de donde salieron 2 de las 5 mediciones de hex
   de este documento), más ~20 páginas interiores del manga en blanco y negro
   (línea gruesa, poca trama) para el punto 19.
3. **`vestuario_03.jpg`** (=hoja_04, imágenes 145-192): más portadas de
   capítulo (74-121), los **dos frascos de perfume oficiales** (números 166 y
   167, con el uniforme de cada personaje dibujado en la etiqueta), fotos de
   elenco de imagen real (kimono y vestuario de la serie dramática/película,
   números 181-182) y varias portadas de Twin. Sirve para vestuario (punto
   15) y para el hallazgo de merchandising (punto 23).

Las otras 8 hojas (03, 05-11) quedan en
`herramientas/referencias/kakegurui/` (fuera del repositorio) por si el
redactor quiere mirar más: tienen sobre todo fotogramas del anime (útiles
para el investigador de vídeo, no para mí) y más portadas de capítulo.

## Lo mejor para la lámina

1. Las figuras **ARTFX J** de Yumeko y Mary (punto 23): pose de lanzar cartas,
   pelo al viento, ojos que brillan de locura — es la prueba más clara de una
   pose «viva» oficial, mejor que cualquier ilustración de pie.
2. El arte del gabinete de **pachislot/pachinko**: primer plano de cara con
   la sonrisa/mirada de la locura de apostar, distinto a cualquier pose de
   cuerpo entero que ya se tenía.
3. Rojo del blazer medido en 5 imágenes oficiales: usar **`#D6362A`** como
   base (no el `#C9020F` de un solo fan), oscurecer a `#832B27` si la escena
   es de noche.
4. Modelos 3D **CC BY** de mesa, fichas y cartas de Sketchfab (tabla del
   punto 3): sirven para armar la mesa de casino del objeto del canal sin
   pagar ni inventar.
5. El patrón de rombos rojo/negro de la base de las figuras ARTFX J y las
   texturas CC0 de ambientCG (Paper001/005/006, Cardboard002) para el fondo
   y la caja de cartas de la lámina.

## No encontré

- ⚠️ Un **artbook** propio de Naomura (sí existe el fanbook «賭ケグルイ愛」
  con resultados de popularidad, ya en la biblia vieja).
- ⚠️ El **archivo real** del fondo de pantalla que regaló ALL IN por X: sólo
  el anuncio de la campaña.
- ⚠️ Un **emblema o escudo propio** de la Academia Hyakkaou (busqué en inglés
  y japonés, ver punto 19).
- ⚠️ Colaboraciones **fuera de Japón** (marcas globales, gachas
  internacionales): no until profundizar en chino/coreano.
- ⚠️ Segunda fuente para el Blu-ray de Manabu Akita/Naomura (queda en ⚠️,
  no ✅, tras intentarlo).
- ⚠️ Precio y fecha exacta de venta de la figura Union Creative de Mary (sólo
  el anuncio de pre-venta).

## Bitácora de búsqueda (esta tanda, 25-sep-2026)

- **Español**: ninguna nueva (los datos base ya venían en español donde
  aplicaba).
- **Inglés**: `Kakegurui collaboration cafe Animate` (WebSearch),
  `free tartan plaid skirt pattern texture CC0 seamless` (WebSearch).
- **Japonés**: `Kakegurui コラボカフェ 2023 OR 2024 OR 2025` (WebSearch),
  `賭ケグルイ 香水 パルファム` (WebSearch), `eカケグルイ パチンコ D-light 公式サイト 2026`
  (WebSearch), `パチスロ 蛇喰夢子という女 2023 スペック 筐体 画像` (WebSearch),
  `賭ケグルイ 壁紙 プレゼント 公式サイト` (WebSearch), texto completo de
  `ja.wikipedia.org/wiki/賭ケグルイ` (API `action=query&prop=extracts`,
  búsqueda de「コラボ」「パチンコ」「スロット」「フィギュア」「カフェ」「グッズ」「校章」「エンブレム」「紋章」dentro del extracto).
- **Herramientas de red directa** (no cuentan contra el cupo de búsqueda):
  `investigar_serie.py` (11 hojas nuevas), `estilo.py` (7 imágenes oficiales
  medidas), API de Sketchfab (`/v3/models/<uid>`, 7 modelos), API de Fandom
  (`imageinfo` para perfumes y figuras), API de ambientCG, `collabo-cafe.com`
  (6 páginas de eventos leídas con curl), `p-town.dmm.com` y
  `p-world.co.jp`/`pachinkovillage.com` (pachislot/pachinko), `g123.jp`
  (nota de prensa de ALL IN), `essential-japan.com` (perfumes).
- **Fuentes consultadas en total en esta parte** (distintas de
  `datos-imagen.md`): AniList, Fandom API (imageinfo ×3 llamadas),
  ja.wikipedia.org, LisAni!, Animate Times, PASH! PLUS, kakegurui-anime.com
  (×3 páginas), pixiv Comic, Gangan Joker/Square Enix, Sketchfab API (×7),
  Openverse (ya contado en datos-imagen.md), Wallhaven (ya contado),
  collabo-cafe.com (×7 páginas), Anime News Network, essential-japan.com,
  fairytail.jp, p-town.dmm.com (×2), P-WORLD, pachinkovillage.com, g123.jp,
  assets.clip-studio.com, ambientCG (API + 4 páginas), TextureCan,
  Raw Catalog, Imaginations Costume. **Total: 27 fuentes nuevas** en esta
  parte, más las de `datos-imagen.md` (AniList, Fandom ×5 páginas, Danbooru,
  Safebooru, Wallhaven, Sketchfab, Openverse) → **más de 35 fuentes** entre
  las dos, dentro del cupo de 40 del encargo completo (el resto lo aportan
  video, voz y texto).

Sigue: nada obligatorio pendiente de mis puntos (1, 3, 15, 16, 19, 23) según
ENCARGO.md — quedan sólo extras anotados en «No encontré» (artbook, fondo de
ALL IN, emblema del colegio, colaboraciones fuera de Japón, segunda fuente
del Blu-ray, precio de la figura Union Creative). Si hay más tiempo: buscar
colaboraciones en chino/coreano y una segunda fuente para los dos datos de
Blu-ray.
