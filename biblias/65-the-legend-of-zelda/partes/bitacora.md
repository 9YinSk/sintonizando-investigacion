## Bitácora

### Bitácora de imagen

- `herramientas/investigar_serie.py --serie "The Legend of Zelda" --wiki zelda --paginas "Link" "Princess Zelda" "Ganon"` → 247 imágenes enlazadas, 120 grandes, 3 hojas de contacto en `hojas/` (miradas con Read completas)
- `herramientas/estilo.py` sobre 8 artes oficiales bajadas (Link ×3 épocas, Zelda ×3 épocas, Ganondorf ×2 épocas) con cabecera `Referer: https://www.fandom.com/` para descargar de `static.wikia.nocookie.net`
- API de Sketchfab v3 (`/search` y `/models/<uid>`): consultas «zelda», «master sword», «hylian shield», «hyrule castle», «korok», «triforce», «ganondorf» — confirmado `isDownloadable` y licencia real de cada modelo elegido
- API de Poly Haven (`/assets?type=models`): 521 modelos totales, filtrados por palabras clave de ambientación (barril, farol, cofre, fogata, cajón) — sin contenido con marca, todo CC0
- API de ambientCG (`/api/v2/full_json`): «chainmail», «leather», «wood», «stone wall», «paper» — todo CC0 por política del sitio
- API de Wallhaven v1 (`/search`, `/w/<id>`): «zelda», «hyrule breath of the wild», «tears of the kingdom», filtro `purity=100` (aptas) y `atleast=1920x1080`
- API de Danbooru (`/posts.json?tags=... rating:general order:score`): «link», «princess_zelda», «ganondorf» — se descartaron los datos de Safebooru de `datos-imagen.md` por venir repetidos/idénticos entre personajes distintos (fallo del recolector)
- Búsqueda web (inglés): «Nintendo official Tears of the Kingdom wallpaper download», «free manga screentone brushes Clip Studio Paint CC0», «Hylian Crest Sheikah Eye Triforce SVG vector free download github», «"Cadence of Hyrule" crossover Zelda Crypt of the NecroDancer official», «Zelda Breath of the Wild collaboration Monster Hunter Rise Sunbreak Link armor quest», «"Mario Kart 8" Link DLC Master Cycle Zero official Nintendo crossover», «Zelda First 4 Figures official statue license best cosplay Link Zelda award», «screenrant Incredible Zelda Breath of the Wild Cosplay Brings Link to Life»
- Búsqueda web (español): «Zelda cafe temático colaboración Nintendo evento oficial Tokio»
- `herramientas/hermanas.py 65-the-legend-of-zelda` → sin serie hermana

### Bitácora de video

- Dailymotion API (`api.dailymotion.com/videos?search=`), español/inglés: «Zelda Breath of the Wild trailer», «Zelda Tears of the Kingdom trailer», «Zelda Ocarina of Time trailer», «Zelda Wind Waker trailer», «Zelda Ganondorf boss fight», «Zelda Hyrule Field gameplay», «Legend of Zelda 1989 cartoon opening», «excuse me princess zelda», «Zelda Ocarina of Time intro cutscene», «Zelda Ocarina of Time ending», «Legend of Zelda cartoon ending credits», «Zelda Ganon transformation», «Zelda pull master sword scene» — todas con resultados útiles salvo la de «excuse me princess» (sin resultado directo del clip).
- `herramientas/fotogramas.py` sobre 6 clips de Dailymotion (BOTW tráiler, OoT 3D intro, OoT créditos, cartoon 1989 opening, BOTW combate final Ganon, TOTK tráiler final): 62 fotogramas en total, todos mirados con Read.
- Colores medidos con Pillow directo sobre los fotogramas descargados (no sobre las miniaturas de la hoja de contacto).
- `zelda.fandom.com/api.php` (`list=search`, `srwhat` por defecto en texto): «It's dangerous to go alone», «Hey! Listen!» — confirmaron las páginas «Iconic quotes in The Legend of Zelda series» y «The Legend of Zelda in Popular Culture».
- MusicBrainz (`musicbrainz.org/ws/2/release-group`): «Zelda Symphony OR Zelda Sound Selection OR Hyrule Symphony», «"Symphony of the Goddesses"», «artist:Nintendo AND "Breath of the Wild"» (esta última sin resultados).
- WebSearch (2 búsquedas de las ~50 del cupo): «Zelda Tears of the Kingdom TikTok trend viral Ultrahand 2025», «"Legend of Zelda" análisis YouTube video ensayo más visto».
- `datos-video.md` (recolectar.py): revisado entero; sus bloques de AniList, AnimeThemes y Reddit vinieron vacíos o fallaron (ver «No encontré»); los de Dailymotion e Internet Archive se comprobaron pero no se reusaron literal porque no encajaban con los puntos 2/4/9/10/14 (eran vídeos de fans/gameplay genérico), así que busqué clips propios más precisos.

### Bitácora de voz

- Doblaje Wiki (API, es): ficha «The Legend of Zelda (franquicia)», «Link», «Zelda», «Ganondorf», con
  reparto completo, ficha técnica y notas de doblaje — la fuente más valiosa de toda la parte.
- Muestras de audio de Doblaje Wiki (`.ogg`, vía `imageinfo` de la API): Zelda, Revali, Impa, Sidon,
  Yunobo, Teba, Riju (URLs sacadas); transcritas con `herramientas/voz.py` las de Zelda y Revali
  (Whisper en local, modelo small, idioma es).
- WebSearch (es): «Jessica Ángeles voz Zelda…», «Xóchitl Ugarte dirección doblaje…», «ANMTV Zelda
  doblaje latino…», «Jorge Roig Jr Link…», «encuesta popularidad personajes Zelda Nintendo oficial»,
  «Triforce orden Poder Sabiduría Valor», «fandub español latino Zelda CDi parodia», «por qué la gente
  ama Zelda Breath of the Wild reseñas», «Link comida favorita manzanas», «Ganondorf horses love
  canon», «reddit r/zelda scene that made you cry» (sin resultado directo de Reddit).
- WebSearch (en): «GameFAQs Character Battle Zelda winner», «Zelda character birthday height Hyrule
  Historia Encyclopedia», «Legend of Zelda fandom pet peeve call Link Zelda», «Princess Zelda hobbies
  Breath of the Wild canon».
- WebSearch (ja): «ゼルダの伝説 キャラクター 人気投票 結果» → llevó a Nintendo Dream (ndw.jp), la mejor
  fuente de popularidad oficial de toda la parte.
- WebFetch: universozelda.com (resumen encuesta Nintendo Dream 2018), thegamer.com (encuesta de fans
  Schaffrillas), cbr.com (altura/edad/zodiaco), ndw.jp ×2 (rankings completos BOTW y TotK con votos
  reales), anmtvla.com ×2 (reparto BOTW y TotK), I_am_Error en Wikipedia (en).
- Dailymotion (API `api.dailymotion.com/videos?search=`): «Zelda CDi doblaje parodia», «Zelda fandub
  latino animado», «cover opening Zelda español», «recuerdos campeones Zelda BOTW español», «Zelda
  Breath Wild memorias aliados latino», «Tears of the Kingdom trailer español latino», «Zelda Tears
  Kingdom cinematica español», «Zelda Champions Ballad Español Latino Pelicula» → de ahí salieron los
  tráilers usados para los fotogramas de emoción y el fandub de Skyward Sword.
- `herramientas/fotogramas.py` sobre 4 vídeos de Dailymotion: tráiler final de *Tears of the Kingdom*
  (x8k22ef, contacto cada 3 s + 2 fotogramas grandes), tráiler de *The Champions' Ballad* (x6bc0bm,
  contacto cada 4 s), primeros minutos doblados de *BOTW* (x5ahli0, 0:00-3:00 cada 5 s) y el tráiler de
  anuncio E3 2019 de la secuela (hoy *Tears of the Kingdom*) (x7au2j3, contacto cada 2 s + 2 fotogramas
  grandes en 0:34 y 0:46). Se borraron todos los `video.mp4` de trabajo tras sacar las hojas (~92 MB).
- `yt-dlp --dump-json` sobre 2 vídeos de YouTube (fandubs): los dos devolvieron 429/«confirma que no
  eres un bot» — confirma el bloqueo de YouTube que avisa AYUDANTE.md.
- `herramientas/hermanas.py 65-the-legend-of-zelda`: sin serie hermana para este encargo.

### Bitácora de texto

- Búsquedas en inglés (WebSearch, ~14): tipografía del logo, diálogo BOTW/TOTK/OoT/WW, Game UI Database, cel-shading Wind Waker (inverted hull, Miyamoto/Aonuma), estilo pictórico BOTW (Takizawa, Aonuma, Jōmon), Skyward Sword impresionista (Cézanne), motor y herramientas de Nintendo EPD, Shadow of the Colossus/Elden Ring/Skyrim como influencias cruzadas, Tolkien y la infancia de Miyamoto, Hyrule Historia y la cronología en tres ramas, Triforce/Escudo Real/Ojo Sheikah/símbolo Gerudo, TCRF Ocarina of Time y Breath of the Wild.
- Descargas y comprobación con fontTools (tildes, ñ, ¿, ¡): Hylia Serif, TLOZ Minish Cap/ALttP/Four Sword, Return of Ganon, Reggae One y RocknRoll One (Google Fonts, vía Fontsource) — las 5 descargadas y comprobadas de verdad, no de memoria.
- Consultas a la API de Fandom (zelda.fandom.com/api.php, sin bloqueo): wikitext de «List of fonts used in The Legend of Zelda logos», «Eye Symbol», «Hylian Crest»; búsqueda de imágenes con imageinfo para 3 símbolos (Ojo Sheikah, Cresta Hyliana, Trifuerza).
- Bloqueos encontrados: dafontfree.net/zeldauniverse.net dieron 402 a WebFetch directo (rodeado buscando el contenido por otra vía o con caché de búsqueda); Game UI Database y TCRF dieron 403 tanto a curl como a WebFetch, y navegar.py falló porque el contenedor no tiene el navegador headless instalado (chrome-headless-shell ausente) — lo anoto para que el jefe lo sepa, no es un fallo mío de no intentarlo.
- No usé git ni toqué biblia.md; sólo escribí en partes/texto.md y partes/texto.json.
