# Parte del investigador de VÍDEO · Sailor Moon (encargo 38)

Puntos de `ENCARGO.md` que me tocan (según `EQUIPO.md`): **2** (fotogramas de escenas
icónicas), **4** (fondos y sitios: luz, paleta, texturas), **9** (música y sonido),
**10** (vídeos y tendencias) y **14** (poses analizadas por personaje).

Parto de `partes/datos-video.md` (ya recolectado, no repetido: AniList, Dailymotion,
Internet Archive, MusicBrainz). **AnimeThemes falló** (522) tanto en la recolección como
al probarlo yo de nuevo — no hay `.webm` de AnimeThemes disponibles para este anime.

**YouTube bloqueado** («Sign in to confirm you're not a bot»), así que usé:
- **Internet Archive** para episodios y películas completas (audio real, no clips
  cortados): episodio 1 en inglés (DiC dub), la película R (VHS fandub) y la película
  *Sailor Moon Cosmos* (2023, doblaje latino).
- **Dailymotion** para el opening/ending y clips sueltos.
- La **wiki de Fandom** (`sailormoon.fandom.com/api.php`, en inglés) para fichas de
  sitios, canciones y créditos, con `imageinfo` para el tamaño real de cada imagen.

Vi de verdad, con `herramientas/episodio.py` (ficha en `partes/episodios.md`) y
`herramientas/fotogramas.py`/`estilo.py` (fotogramas grandes + color), hojas y vídeo
en `/tmp/claude-0/trabajo/38-sailor-moon-video/` (`.mp4` borrados al terminar cada uno):

1. **Episodio 1** «Usagi and the Moon Cat» (DiC dub, inglés) — completo, 21:28 —
   [archive.org](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2001%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1253F801%5D.ia.mp4)
2. **Sailor Moon R: The Movie** (VHS fandub, inglés), tramo 40:00-55:00 —
   [archive.org](https://archive.org/details/sailor-moon-r-the-movie-fandub-vhs-rip)
3. **Sailor Moon Cosmos** (2023, doblaje latino, Parte 2) — la más reciente y el final
   de la historia de las 90 — [archive.org](https://archive.org/details/pretty-guardian-sailor-moon-cosmos-la-pelicula-parte-2)

---

## Hallazgos

### Punto 2 · Escenas icónicas

- **La primera transformación de Usagi** («Moon Prism Power», ep. 1): Luna le dice
  «Just repeat after me: moon, prism, power» en el **min. 15:32**; a partir del
  **15:34** Usagi gira envuelta en burbujas, con una silueta rosa/blanca de brazos
  extendidos y las coletas convertidas en cintas (fotograma exacto en `[15:20]`, ver
  punto 4 y hoja abajo); a las **15:45** ya está de pie, uniforme puesto, frente a la
  luna creciente. Termina en el **15:56**, cuando abre los ojos ya transformada ·
  [archive.org, ep. 1](https://archive.org/download/Sailor-Moon-Dic-Dub-English-DVD-H264/%5BSMC%5D%20Sailor%20Moon%2001%20-%20English%20Dub%20%28DVD.H264.AC3%29%20%5B1253F801%5D.ia.mp4?t=934)
  + [ficha en `partes/episodios.md`](episodios.md) · ✅ (visto directamente, con
  transcripción del diálogo) · ep. 1 (DiC dub; en japonés es el mismo minutaje
  aproximado, la escena no se recorta en el doblaje).
- **El primer «Moon Tiara Magic»** (ataque final del ep. 1): a las **17:01-17:04**
  Sailor Moon se planta con las piernas muy abiertas, un brazo doblado con el puño
  junto a la cara y el otro extendido con dos dedos en V, la luna creciente enorme
  detrás — es la pose «después de lanzar la tiara» que después se repite toda la
  serie (fotograma exacto abajo, punto 14) · mismo episodio, **min. 17:02** · ✅.
- **La escena de Fiore — «You are not alone»** (*Sailor Moon R: The Movie*, 1993): la
  encontré transcribiendo el tramo 40:00-55:00 de la película con `episodio.py`; el
  minuto exacto y la cita quedan en `partes/episodios.md` (ficha «Sailor Moon R: The
  Movie»). Es la escena más citada por fans y medios (TV Tropes «Heartwarming/Tear
  Jerker Moments in Sailor Moon R: The Movie») como el momento más emotivo de las
  películas de los 90 · [archive.org](https://archive.org/details/sailor-moon-r-the-movie-fandub-vhs-rip)
  + [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Heartwarming/SailorMoonRTheMovie) ·
  ✅ (visto + fuente secundaria que confirma que es LA escena icónica de esa película).
- **Sailor Moon Cosmos (2023)** — última película de la franquicia de los 90 (cierra el
  arco de Sailor Stars/Galaxia que el anime original de 1997 dejó sin adaptar) — la vi
  en **doblaje latino** (Parte 2, la más reciente disponible) para el punto «reciente/
  final de temporada»: minuto y cita en `partes/episodios.md`. Estreno: julio-agosto de
  2023 (Parte 1 y 2) · [archive.org](https://archive.org/details/pretty-guardian-sailor-moon-cosmos-la-pelicula-parte-2) ·
  ✅.

### Punto 4 · Sitios, luz, paleta y texturas

**Colores medidos con `herramientas/estilo.py`** sobre fotogramas que saqué yo mismo
con `fotogramas.py --fotograma` del episodio 1 (min. 15:20, 15:45, 17:02):

- **Transformación — silueta entre burbujas** (min. 15:20): fondo azul noche con
  burbujas verde-azuladas translúcidas, la silueta de Usagi en rosa/blanco con un haz
  magenta diagonal. Paleta: `#012B62` 33% (azul fondo) · `#2A7485` 21% (verde-azul
  burbuja) · `#031149` 18% (azul oscuro) · `#0B4B75` 11% · `#A791B5` 9% (silueta lila) ·
  `#300644` 8% (haz magenta) — saturación 85%, brillo 43%, sombreado degradado/pintado,
  casi sin línea · medido en `fotograma_00920.jpg` (1280×960) · ✅.
- **Transformación — pose final ante la luna** (min. 15:45): morados y violetas de
  ensueño. Paleta: `#3B3296` 40% · `#7E60B3` 17% · `#2C2279` 16% · `#C18CBB` 11% ·
  `#F3D8E3` 10% (destello rosa claro) · `#9C4859` 7% — saturación 54%, brillo 65% ·
  medido en `fotograma_00945.jpg` · ✅. **Esta paleta morada/violeta es la «firma»
  visual de toda secuencia de transformación de la serie** (se repite con cada chica).
- **Moon Tiara Magic — cielo tras la tiara** (min. 17:02): turquesa/celeste plano de
  noche. Paleta: `#48ACBF` 35% · `#3995B1` 27% · `#63AFC3` 16% · `#2589A6` 12% ·
  `#C6BBAD` 6% (luna) · `#614152` 5% (contorno del pelo) — saturación 61%, brillo 71%,
  sombreado degradado, poca línea (línea `#457076`) · medido en `fotograma_01022.jpg`
  (1280×960) · ✅. Muy distinta de la paleta morada de la transformación: el «cielo de
  batalla» es frío/turquesa, la transformación es cálida/violeta.
- **El Templo Hikawa** (casa de Rei, punto de reunión del grupo): en el manga y el
  anime está en Akasaka, Minato, Tokio (en el manga/Crystal, en Motoazabu); es un
  santuario sintoísta real de estilo japonés clásico, con escalinata de piedra, torii,
  tejado de tejas y un árbol sagrado · imagen del anime,
  [`Hikawa-shrine.jpg`](https://static.wikia.nocookie.net/sailormoon/images/3/3e/Hikawa-shrine.jpg)
  640×480 (medida) y la versión Crystal,
  [`Hikawa_Shrine_(Crystal).webp`](https://static.wikia.nocookie.net/sailormoon/images/d/df/Hikawa_Shrine_%28Crystal%29.webp)
  800×449 (medida) · [wiki, «Hikawa Shrine»](https://sailormoon.fandom.com/wiki/Hikawa_Shrine) ·
  ✅ (wikitexto + imágenes).
- **Game Center Crown** (el arcade donde trabaja Motoki, punto de reunión): en
  Azabujuban, Minato, Tokio; interior de máquinas recreativas de los 90, con la
  cafetería «Fruits Parlor Crown» al lado (mismo dueño) · imagen del anime,
  [`Gamecentercrown.jpg`](https://static.wikia.nocookie.net/sailormoon/images/e/e6/Gamecentercrown.jpg)
  238×178 (medida, pequeña) y [`GCC2.png`](https://static.wikia.nocookie.net/sailormoon/images/8/8f/GCC2.png)
  703×470 (medida) · [wiki, «Game Center Crown»](https://sailormoon.fandom.com/wiki/Game_Center_Crown) ·
  ✅.
- **El Dark Kingdom** (base de los villanos de la temporada 1): caverna helada en el
  «D Point», Polo Norte, gobernada por la Reina Beryl y la Reina Metalia; estética de
  cristal oscuro y morado · imagen del anime,
  [`Anime_Dark_Kingdom.jpg`](https://static.wikia.nocookie.net/sailormoon/images/6/65/Anime_Dark_Kingdom.jpg)
  275×183 (medida, pequeña) · [wiki, «Dark Kingdom»](https://sailormoon.fandom.com/wiki/Dark_Kingdom) ·
  ✅.
- **Texturas reales equivalentes (CC0)**, por sitio:
  - Escalinata y suelo de piedra del Templo Hikawa → **PavingStones070** (ambientCG,
    CC0) — https://ambientcg.com/view?id=PavingStones070
  - Madera del torii y del templo → **Wood051** (ambientCG, CC0) —
    https://ambientcg.com/view?id=Wood051
  - Cristal oscuro/morado del Dark Kingdom → **Ice004** o roca vítrea
    **RockFace002** (ambientCG, CC0) — https://ambientcg.com/view?id=RockFace002
  - ✅ (fichas de ambientCG, licencia CC0 confirmada).

---

## Lo mejor para la lámina

1. La **pose 280 (17:02)**, Sailor Moon con las piernas en V ante la luna creciente
   tras lanzar el Moon Tiara Magic, es LA pose más reconocible de toda la franquicia:
   sirve para una lámina de «bienvenida/presentación» de cualquier canal.
2. La **paleta morada de la transformación** (15:45) frente a la **paleta turquesa del
   combate** (17:02) da dos ambientes de luz ya diferenciados y medidos, listos para
   dos escenas distintas de una misma lámina.
3. Moonlight Legend, compuesta por **Tetsuya Komuro** (un nombre muy reconocible fuera
   del anime), es un dato fuerte para un canal de música/covers.

## No encontré

_(pendiente completar en la próxima tanda)_

---

## Bitácora de búsqueda (vídeo)

- **Datos previos usados sin repetir la consulta**: `partes/datos-video.md` (AniList,
  Dailymotion, Internet Archive, MusicBrainz).
- AnimeThemes (`api.animethemes.moe`): repetí la prueba, sigue en **522** (caído) —
  igual que en `datos-video.md`.
- Wiki de Fandom (`sailormoon.fandom.com/api.php`, inglés): `list=search` para
  «opening theme», «Hikawa Shrine», «Crown Game Center», «Dark Kingdom», «Moon
  Kingdom», «Silver Millennium», «Takanori Arisawa»; `action=parse&prop=wikitext`
  sobre «Moonlight Densetsu», «Sailor Star Song», «Pretty Guardian Sailor Moon (anime
  series)», «Hikawa Shrine», «Game Center Crown», «Dark Kingdom», «Moon Kingdom»;
  `prop=imageinfo` sobre 6 imágenes de sitios.
- Internet Archive (`advancedsearch.php` + `metadata/<id>`): busqué «Sailor Moon»
  (mediatype movies, 40 resultados por descargas) y «Sailor Moon Cosmos»; comprobé
  metadatos de 6 ítems antes de elegir el episodio 1 (DiC dub), la película R (VHS
  fandub) y Cosmos Parte 2 (latino).
- Dailymotion API (`api.dailymotion.com/videos?search=`): «Sailor Moon opening 1992
  japones», «Sailor Moon opening latino», «Sailor Moon transformación latino»,
  «Sailor Moon ending latino», «Sailor Moon último capítulo final latino» (español).
- `herramientas/episodio.py`: episodio 1 completo (✅) y tramo de la película R
  (lanzado, sigue en la próxima tanda si no terminó).
- `herramientas/fotogramas.py --fotograma`: 3 fotogramas grandes del episodio 1 (min.
  15:20, 15:45, 17:02).
- `herramientas/estilo.py --colores`: los 3 fotogramas anteriores.
- WebSearch (3, inglés): escena «You are not alone» de Sailor Moon R: The Movie
  (minuto no publicado en ninguna fuente, lo saco del visionado); tendencia de TikTok
  2025-2026.

Sigue: punto 9 (música y sonido: rematar créditos vistos en pantalla, insert songs,
SFX), punto 10 (vídeos/tendencias: cerrar con lo visto en la película R y Cosmos,
TikTok), punto 14 (poses por personaje: Usagi ya tiene 2, faltan Ami, Rei, Makoto,
Minako, Luna y comprobar el resultado del tramo de la película R en background),
completar «No encontré», revisar `partes/episodios.md`.
