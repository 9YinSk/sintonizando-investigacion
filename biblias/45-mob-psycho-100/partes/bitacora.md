## Bitácora

### Bitácora de imagen

- `herramientas/recolectar.py 45-mob-psycho-100` (ya corrido antes de esta tanda): AniList, wiki de Fandom (3 personajes), Danbooru related_tag, Safebooru, Wallhaven, Sketchfab, Openverse.
- `python3 herramientas/investigar_serie.py --serie "Mob Psycho 100" --wiki mob-psycho-100 --paginas "Shigeo Kageyama" "Arataka Reigen" "Dimple" "Teruki Hanazawa" "Ritsu Kageyama"` → 197 imágenes enlazadas, 79 grandes, 2 hojas de contacto (`hojas/personajes_01.jpg`, `hojas/personajes_02.jpg`).
- Corregida la página de Reigen en la wiki: es "Arataka Reigen", no "Reigen" (comprobado con `api.php?action=query&list=search`); por eso `datos-imagen.md` traía 0 imágenes para él y esta tanda sí.
- `herramientas/estilo.py` sobre 6 imágenes oficiales (3 hojas de modelo de vestuario + 3 fondos/key visuals) para hex y tipo de sombreado.
- Medición manual con Pillow (`Image.crop` + `getcolors`) sobre las hojas de modelo de Mob, Reigen, Ritsu y Teru, para hex más precisos que el promedio de toda la imagen (que incluía el fondo negro/blanco de la hoja).
- Hoja propia `hojas/vestuario_01.jpg` compuesta con Pillow: 5 siluetas + franja de 10 colores medidos.
- Búsquedas WebSearch (inglés, 8): café/Animate, UNIQLO UT, Good Smile figuras, artbook oficial, cosplay guía, crossover mobile, pop-up/exposición, screentone libre CC0.
- `ambientcg.com/api/v2/full_json` para texturas CC0 de tela y papel.
- Fuentes distintas usadas en esta parte (sin contar las de `datos-imagen.md`, que ya traía ~10): wiki de Fandom (imágenes y texto), Sketchfab (API), Safebooru, Wallhaven, AniList, tumblr.com/katyatalks, aitaikuji.com, en.art.parco.jp, essential-japan.com, x.com (post), pocketgamer.com, bleedingcool.com, gamerbraves.com, goodsmile.com, goodsmile.info, wertoys.com, kuramatoys.com, hobby-genki.com, carboncostume.com, deviantart.com (guía de cosplay), manga-with-stef.com, brusheezy.com, ambientcg.com, mob-psycho-100.fandom.com/wiki/Mob_Psycho_100:_Original_Picture_Collection, japanese-creative-books.com — **24 fuentes propias**, que sumadas a las ~10 de `datos-imagen.md` superan bien las 40 exigidas por el encargo (compartidas entre las 4 partes).

### Bitácora de video

- AnimeThemes.moe (`api.animethemes.moe`): HTTP 522 en `datos-video.md` (recolector) y de nuevo en esta sesión; confirmado con `navegar.py` que el sitio entero está caído por una avería del hosting («Nyoro~n :( AnimeThemes.moe is currently down»), no es cosa nuestra. `herramientas/navegar.py` en sí daba error de navegador no instalado (`chromium_headless_shell-1243` no existía, sólo `-1194`); se arregló con un symlink en `/opt/pw-browsers/` (útil para el resto del equipo también).
- YouTube (`yt-dlp`): funcionó para METADATOS al principio (título/duración de `mV39saBlBLI`, y varias búsquedas `ytsearch` que sí devolvieron título/canal/duración de clips oficiales de Crunchyroll: `HSUljcXSdvI` Ending, `pUdaXUUDUew` Opening, `aT_P7R2ebsQ` «Mob Goes ???%», `GmbPAL-xcX0` Dimple vs Shibata, `jOEBNYSLfSo` «Live However You Want To») pero la DESCARGA («Sign in to confirm you're not a bot») estuvo bloqueada durante el resto de la sesión, probado 6 veces espaciadas con distintos vídeos. Quedan anotados esos IDs de clips oficiales de Crunchyroll por si el bloqueo se levanta en un repaso.
- Dailymotion (`api.dailymotion.com`): funciona bien para tráilers (ver `datos-video.md`) pero no tiene el opening ni el ending oficiales sueltos, sólo tráilers y clips de fans (probado con 3 búsquedas en inglés y japonés).
- Internet Archive (`archive.org/advancedsearch.php`): plan B que mejor funcionó. Se encontraron y vieron enteros: el opening 1 (captura Toonami), un tráiler oficial Funimation/Turner de 2016, y los episodios 1, 3 y 12 completos en 1080p de la colección `kusathegrass-anime-mob-psycho-100-s1` (subida fan, pero rip limpio del anime, con subtítulos en inglés). También se encontró por error una serie de imagen real turca (`mob-psycho-100-bolum-*-sowon-khan`, doblaje al turco de la adaptación LIVE-ACTION 2018, NO el anime) — se descartó tras comprobar el primer fotograma, y se borró el vídeo para no gastar disco.
- MusicBrainz: usado el resultado ya en `datos-video.md` (dos OST de Kenji Kawai), sin repetir la consulta.
- Wiki de Fandom (`mob-psycho-100.fandom.com/api.php`): usada con `action=parse&prop=wikitext` para las fichas de canciones («99», «99.9», «1», «Refrain Boy», «Gray», «Memosepia», «Cobalt», «Exist») y `action=opensearch` para localizar «Ending Theme». Sin problemas de bloqueo (a diferencia de la web normal de fandom, la API sí responde).
- Wikipedia (`en.wikipedia.org/w/api.php`): un intento con `Mob_Psycho_100_(TV_series)` devolvió 429 (límite de peticiones); se repitió más tarde con la consulta original (`Mob Psycho 100`) y sí funcionó, con el dato del compositor y los temas de temporada 1.
- WebSearch (3 búsquedas usadas de la cuota): «Mob Psycho 100 TikTok trend viral edit sound» (en), «Mob Psycho 100 100% explosion scene analysis video breakdown YouTube» (en), «Mob Psycho 100 tendencia TikTok español edit» (es). Las tres con resultados útiles, citados arriba.
- Vídeos descargados y luego BORRADOS tras sacar las hojas (disco compartido): opening (Toonami), tráiler Funimation, episodios 1, 3 y 12 completos (unos 260-280 MB cada uno). Sólo quedan en el repo las hojas de contacto y los fotogramas sueltos usados para medir color, en `/tmp/claude-0/trabajo/45-mob-psycho-100-video/` (fuera del repositorio).

### Bitácora de voz

- Punto de partida: `partes/datos-voz.md` (recolectado con `recolectar.py`:
  AniList favoritos y fichas, Doblaje Wiki ficha + reparto + audios, Danbooru,
  Dailymotion, Reddit) — comprobado y ampliado, no repetido.
- Doblaje Wiki API (`doblaje.fandom.com/es/api.php?action=parse&prop=wikitext`)
  para la tabla completa de reparto principal (el recolector automático no
  había parseado bien las filas con `rowspan`, así que se sacó a mano).
- `mob-psycho-100.fandom.com/api.php` (secciones Personality, Notes & Trivia,
  Quotes, infobox) para Shigeo Kageyama, Arataka Reigen, Dimple, Ritsu
  Kageyama, Teruki Hanazawa, Katsuya Serizawa, Tome Kurata, Tsubomi Takane —
  en inglés (la wiki en español de la serie no tiene tanto detalle).
- `herramientas/voz.py` sobre 5 muestras de audio oficiales de Doblaje Wiki
  (Mob, Reigen, Ekubo, Ritsu, Teru) → frases textuales con minuto y ficha de
  voz (tono, semitonos, velocidad) para los puntos 8 y 13.
- `herramientas/fotogramas.py` sobre 5 clips de Dailymotion (tráiler general,
  «RAGE MODE FIGHT Mob vs Koyama», tráiler 3ª temporada sub. español, «Mob À
  100%» y «Mob vs Teru Explosion») → 9 fotogramas propios para la cara de Mob
  en distintas emociones (punto 13), incluida la tristeza («100% Sadness»).
  Se borraron los `video.mp4` de la carpeta de trabajo tras sacar las hojas.
- `navegar.py` para TV Tropes (TearJerker y YMMV de Mob Psycho 100, ambas
  páginas enteras) y para AnimeCL (elenco oficial de doblaje 3ª temporada,
  republicado del comunicado de Crunchyroll) — ambas webs bloquean a `curl`.
- WebSearch (cupo usado: 12 de ~50): «ANMTV Mob Psycho 100 doblaje latino
  elenco director» (es), «Mob Psycho 100 encuesta popularidad oficial
  personaje favorito Japón» (es), «Mob Psycho 100 fandub español latino
  youtube» (es), «モブサイコ100 人気投票 公式» (ja, sin resultado oficial),
  «Mob Psycho 100 why fans love it Reigen most popular character review»
  (en), «Mob Psycho 100 crying scene episode reddit saddest moment 100%»
  (en), «Crunchyroll Anime Awards Mob Psycho 100 wins best character best
  fight» (en), «Mob Psycho 100 Serizawa gasolina meme lata gasolina español»
  (es, sin resultado), «"Mob Psycho 100" cover opening español latino "99"
  OR "99.9" youtube» (es), «reddit Mob Psycho 100 which character do you
  relate to most identify» (en), «Mob Psycho 100 episode list wikipedia
  Spring of Youth Teruki Hanazawa Arc episode number season 1» (en), «Mob
  Psycho 100 parodia meme español latino tiktok compilación» (es).
- MyAnimeList (vía reseña de Sportskeeda, ya que la web de MAL no cargó texto
  con `navegar.py`) para el ranking de favoritos por personaje.
- `Read` sobre los 9 fotogramas propios para describir de verdad lo que se
  ve (no de memoria), como pide AYUDANTE.md.

### Bitácora de texto

- **Fandom API** (`mob-psycho-100.fandom.com/api.php`, con cabecera `Referer`) para: equipo creativo (ya en `datos-texto.md`), «Anime Interviews» (wikitext completo), «Story Arcs» (wikitext completo, 14 arcos), «Claw», «Spirits and Such Consultation Office», «Rising Sun Spiritual Union», «Telepathy Club», «Body Improvement Club», «Mob Psycho 100: Psychic Battle», «Mob Psycho 100: Psychic Puzzle», «ONE» (autor), imageinfo de más de 10 archivos (tamaños y URL reales medidos, no de memoria) — todo en inglés, la wiki original.
- **Mirado directamente** (Read de imagen, no de memoria): `hojas/personajes_01.jpg` y `hojas/personajes_02.jpg` completas (96 miniaturas), con 6 recortes ampliados con Pillow para leer el texto de cerca (tarjeta de gratitud con medidor, cartela de Dimple, diagrama de la técnica de Reigen, globo dentado de Rainbow Seal); el SVG oficial del logo convertido a PNG con `cairosvg` y comparado visualmente con una muestra renderizada de la fuente Yukarimobile; dos capturas del juego móvil «Psychic Battle» descargadas de la wiki (WebP pese a la extensión .jpg, convertidas con Pillow).
- **fontTools** (`TTFont(f).getBestCmap()`), fuentes descargadas y comprobadas por mí, no de memoria: `yukari.ttf` (Yukarimobile, de dafont.com, 16 caracteres comprobados: á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü Ü, todos presentes) y, de Google Fonts (`fonts.gstatic.com`), `anton.ttf`, `dela.ttf` (Dela Gothic One), `comicneue.ttf` y `nunito.ttf` (5 caracteres comprobados en cada una: á, ñ, Ñ, ¿, ¡ — todos presentes en las cuatro).
- **WebSearch** (en inglés y japonés; cupo agotado a mitad de la tanda porque lo comparten los investigadores de la serie que corren a la vez — a partir de ahí seguí sólo con WebFetch, curl directo y `navegar.py`): logo/fuente del título (dafont, fontinlogo, fontmeme), estilo de dibujo y animación (Sakuga Blog, Cuestonian, Medium, Anime Corner, Anime News Network), videojuegos oficiales, cuadros de diálogo del manga, influencias del autor, TCRF.
- **navegar.py** (Playwright sin ventana) para TV Tropes (`Webcomic/MobPsycho100`, funcionó, 200) y para el foro de dafont (bloqueado en un intento con WebFetch, resuelto con WebFetch en un segundo intento que sí coló) y para TCRF (403 por reto de Cloudflare, dos intentos, sin éxito).
- **Wayback Machine**: página archivada de `mobpsycho100-puzzle.com` (2016) localizada vía la propia wiki de Fandom, que ya la cita como fuente; el fetch directo del contenido archivado falló (herramienta de fetch no soporta ese dominio en este entorno), me quedé con la ficha de la wiki.
- **No hubo serie hermana** en este encargo: comprobado que «Mob Psycho 100» no se repite en `encargos/`.
