## Bitácora

### Bitácora de imagen

- Fandom API: `hazbinhotel.fandom.com/api.php` y `helluvaboss.fandom.com/api.php` (ambas activas, comprobado
  con `list=search`; `datos-imagen.md` decía que no había wiki puesta — sí la hay, con estos dos subdominios).
- `python3 herramientas/investigar_serie.py --wiki hazbinhotel --paginas "Charlie Morningstar" "Alastor"
  "Angel Dust" "Vaggie" "Hazbin Hotel"`: se cortó a los 600 s (timeout) con 666 imágenes ya bajadas en 13
  hojas (`herramientas/referencias/hazbin-hotel/`); no llegó a procesar del todo la página general «Hazbin
  Hotel», así que sus fondos y objetos se buscaron aparte con la API (`generator=images`).
- `python3 herramientas/investigar_serie.py --wiki helluvaboss --paginas "Blitzo" "Loona" "Moxxie" "Millie"
  "Stolas" "I.M.P"`: 4 hojas, 192 imágenes (`herramientas/referencias/helluva-boss/`).
- API de Fandom directa (`generator=images`, `prop=pageimages`) para las páginas de sitio: «Hazbin Hotel
  (location)», «Pentagram City», «Cannibal Town».
- `herramientas/estilo.py --colores` sobre 11 imágenes descargadas (personajes y sitios) para los hex de los
  puntos 15 y 16.
- Sketchfab API (`api.sketchfab.com/v3/search`, `q=hazbin hotel` / `q=helluva boss`, `downloadable=true`):
  todos los modelos con licencia CC Attribution o CC Attribution-NonCommercial (señalado donde aplica).
- Poly Haven API (`api.polyhaven.com/assets`) y ambientCG API (`ambientcg.com/api/v2/full_json`): sólo assets
  CC0, sin marca de la serie (genéricos que encajan con la estética).
- Openverse API (`api.openverse.org/v1/images`): cosplay con licencia CC BY (Wikimedia Commons) y una textura
  halftone CC0.
- Wallhaven API (`wallhaven.cc/api/v1/search`, `q=hazbin+hotel` / `q=helluva+boss`, `sorting=favorites`).
- Búsquedas web (inglés): «Hazbin Hotel official collaboration Fortnite OR game OR brand crossover 2025»,
  «free halftone screentone brush pack CC0 procreate clip studio», «Hazbin Hotel Helluva Boss official pop-up
  cafe collaboration event Japan 2025».
- No usé git ni toqué `biblia.md`; sólo escribí en `partes/imagen.md`, `partes/imagen.json` y `hojas/`.

### Bitácora de video

- Dailymotion API (`api.dailymotion.com/videos?search=...`): "Hazbin Hotel official trailer" (es), "Helluva Boss opening" (en), "Inside of Every Demon is a Rainbow" (en, sin resultado útil), "Helluva Boss season 2 trailer" (en), "Hazbin Hotel Episode 1 Happy Hotel" (en, sin episodio completo), "Hazbin Hotel S1 E1" (en, sin resultado), "Hazbin Hotel viral moment" (en).
- `yt-dlp --skip-download --print` (sin descarga, sólo metadatos): `ytsearch3:Hazbin Hotel official trailer`, `ytsearch5:Hazbin Hotel edit`, `ytsearch5:Helluva Boss viral`, `ytsearch5:Hazbin Hotel Poison tiktok trend`, `ytsearch4:Hazbin Hotel video essay analysis` — todos en inglés.
- `fotogramas.py` sobre: tráiler S1 doblado IT (x8rhuws, cada 8 s), tráiler S1 oficial en (x8qjgw6, cada 7 s + fotogramas sueltos), piloto Helluva Boss (x8j7da8, cada 25 s + sueltos), "Murder Family" S1E1 Helluva Boss (x8j7dde, cada 30 s + sueltos).
- `estilo.py --colores 6` sobre 7 fotogramas sueltos (fachada y lobby del hotel, skyline de Pentagram City, oficina y casa de Blitzo, bosque y hoguera de "Murder Family").
- `hazbinhotel.fandom.com/api.php` (en): `action=query&list=search` para "opening theme song", "intro sequence OR title card", "credits song", "Alastor radio static filter voice"; `action=query&list=categorymembers&cmtitle=Category:Songs`; `action=parse&prop=wikitext` sobre "Happy Day in Hell", "Inside of Every Demon is a Rainbow", "I.M.P Jingle", "Hazbin Hotel Original Soundtrack", "Hell's Greatest Dad", "Loser, Baby", "Alastor", "Hazbin Hotel (series)/Episode Guide".
- `arctic-shift.photon-reddit.com/api/posts/search?subreddit=HazbinHotel` (en): sin filtro de orden por score real (la API sólo deja `asc`/`desc` por fecha), ordenado a mano en Python.
- `ambientcg.com/api/v2/full_json` (en): "velvet" (sin resultado), "Fabric", "Carpet", "WallpaperDamask" (sin resultado), "Metal", "Gold", "Wood".
- MusicBrainz y Dailymotion de `datos-video.md` (ya recolectados, revisados: la mayoría de MusicBrainz eran ruido —"Boss", "Yes Boss", etc.—, sólo sirvieron los 2 releases de Helluva Boss OST; el clip "Match Made in Hell" de Dailymotion resultó ser un montaje de fan no oficial, descartado).

### Bitácora de voz

- Doblaje Wiki, API `action=parse&prop=wikitext` sobre «Hotel Hazbin» y «Helluva Boss» (es): reparto completo con actor original y latino, estudio y dirección · usado para el punto 8.
- Búsqueda en Doblaje Wiki (`action=query&list=search`) con «Hazbin Hotel» y «Helluva Boss» para encontrar el nombre exacto de la página (el recolector automático había fallado) · es.
- ANMTV (`anmtvla.com`) y SDP Noticias: reparto de doblaje latino como segunda fuente de cada nombre · es, vía WebSearch + WebFetch.
- Hellaverse Wiki (`hazbinhotel.fandom.com`, cubre también Helluva Boss), API `action=parse&prop=wikitext` sobre Charlie Morningstar, Alastor, Angel Dust, Vaggie, Husk, Niffty, Blitzo, Loona, Stolas, Moxxie, Millie: personalidad, gustos/odios, edad · en (la wiki está en inglés; se tradujo al escribir la ficha).
- Wikipedia en inglés: «Angel Dust (Hazbin Hotel)», «Vox (Hazbin Hotel)», «Poison (Hazbin Hotel song)»: recepción de crítica, cifras de popularidad · en, vía WebFetch.
- `herramientas/voz.py` (Whisper local + Parselmouth) sobre 15 muestras oficiales de audio de Doblaje Wiki (una por personaje) bajadas con `curl -H "Referer: https://www.fandom.com/"`: frase textual, tono, expresividad y velocidad de cada voz · para el punto 8 y 13.
- `herramientas/voz.py` sobre el clip de Dailymotion «A Match Made in Hell» (x9iq344): se descartó, no es doblaje oficial (ver punto 8); tardó más de 280 s sin terminar de transcribir por el ruido de fondo.
- `herramientas/fotogramas.py --cada 3` sobre 4 tráileres oficiales de Dailymotion (Hazbin Hotel S1 subtitulado, Hazbin Hotel S2 doblado, Helluva Boss S3 doblado, y el clip x9iq344 que resultó no oficial): hojas de contacto y fotogramas sueltos con `&t=` · para el punto 13.
- API de Dailymotion (`api.php`... en realidad `api.dailymotion.com/videos?search=`) con «Hazbin Hotel español latino escena», «Helluva Boss español latino clip», «Hazbin Hotel cover español opening»: clips oficiales y de fans · es.
- WebSearch: «ANMTV Hazbin Hotel doblaje latino reparto voces» / «ANMTV Helluva Boss doblaje latino reparto de voces» (es), «Hazbin Hotel favorite character poll fandom most popular» (en), «Helluva Boss personaje favorito encuesta fans» (es), «Hazbin Hotel memes fandom running jokes» (en), «Hazbin Hotel escena que hace llorar Poison Hell's Greatest Dad Loser Baby» (es), «Hazbin Hotel fandub español latino YouTube canal» (es), «"Hazbin Hotel" reception praise fans identify with» (en).
- Arctic Shift (Reddit) para r/Hazbinhotel: dio timeout, no se insistió más de dos veces (regla de AYUDANTE.md).
- `herramientas/navegar.py` sobre thetoptens.com: falló (no hay navegador Chromium instalado en este contenedor) — se documenta como límite del entorno, no se insistió.
- No hay `biblias/55-hazbin-hotel/partes/voz.md` ni carpeta `biblias/55-hazbin-hotel/` todavía: nada que evitar repetir de la serie hermana.
- Relanzo (26-sep): `fotogramas.py --fotograma` sobre el tráiler S1 x8qjgw6 a 1:59 (escena de grupo de 7 personajes en el lobby: Alastor, Vaggie, Charlie, Niffty, Sir Pentious, Zestial y Husk — sin Angel Dust, se descartó para ese personaje) y sobre el tráiler S2 x9rrk90 en varios segundos entre 0:45-1:00, donde sí apareció Angel Dust con Cherri Bomb y Arackniss · para completar la fila que faltaba del punto 13.
- Relanzo (26-sep): `fotogramas.py --cada 4` sobre el episodio completo doblado «Murder Family» de Helluva Boss (x8j7dde, 12:20 min) para buscar un fotograma de miedo: se encontró un primer plano claro de Moxxie a los 5:16 · para la fila «miedo» del punto 13. No se usó el piloto x8j7da8 (no hizo falta, ya salió en el primer intento).

### Bitácora de texto

- Fandom API (`hazbinhotel.fandom.com/api.php`, inglés): `allpages`, `search` y `parse&prop=wikitext`
  para Rings of Hell, Overlords, Extermination, Seven Deadly Sins, Pentagram City, Hazbin Hotel
  (series), Hazbin Hotel (location), 666 News, VoxTek — todas abiertas y leídas.
- `tcrf.net` (inglés): búsqueda de texto completo «Hazbin» y «Helluva» → sin resultados, confirma
  que no hay contenido descartado de un juego que no existe.
- WebSearch (inglés): «Hazbin Hotel logo font typeface identify», «Helluva Boss logo font typeface
  identify», «"Mr Darcy" font dafont free download license», «Hazbin Hotel font free alternative
  Google Fonts dafont art deco», «TCRF Hazbin Hotel OR Helluva Boss», «Hazbin Hotel official video
  game mobile app 2024 2025», «Helluva Boss video game I.M.P. app», «"Hazbin Hotel" game announced
  2026 publisher official», «vivziepop twitter font hazbin hotel logo», «Hazbin Hotel end credits
  font typeface style title cards».
- Fontsource (`api.fontsource.org/v1/fonts`, descarga directa de `cdn.jsdelivr.net`): Cinzel
  Decorative, Poiret One, Nosifer, Butcherman, Creepster, Bangers, Monoton, Special Elite, Oswald,
  Permanent Marker, Caveat — comprobadas todas con `fontTools` (`getBestCmap`) para
  á/é/í/ó/ú/ñ/Ñ/¿/¡.
- WebFetch: `pixelframe.design` (Helluva Boss font), `audreyworks.fandom.com` (Five Nights at
  Hazbin Hotel, confirmado fan-made), `thelatenightplayers.com` (juego de mesa I.M.P.),
  `gamefound.com` y Kickstarter (bloqueados por 403, se usó la reseña de thelatenightplayers.com en
  su lugar, con Gamefound/Kickstarter como enlaces directos del producto), `vfxvoice.com` (técnica
  de animación, punto 18), `dexerto.com` (obras parecidas, punto 24).
- WebSearch (inglés) puntos 18/24/25: «Hazbin Hotel Helluva Boss animation software Toon Boom
  pipeline interview Vivienne Medrano», «Hazbin Hotel art style line art shading cel shading
  outline color interview», «Vivienne Medrano influences Cats Don't Dance Bruce Timm Tim Burton
  animation style hazbin», «Blender Freestyle toon shader flat cel shading tutorial free node
  setup 2D cartoon outline», «free Photoshop ink brush clean line art cartoon vector brush
  download», «Hazbin Hotel compared Panty and Stocking OR Invader Zim OR Murder Drones similar
  style review».
- Fandom API, wikitext adicional para el punto 25: `Sinners`, `Angelic Weapon`, `Helluva Boss`
  (serie), búsqueda de `I.M.P` (jingle y vídeo de entrenamiento).
- Comparación con biblias ya hechas del servidor (punto 24): se miró `canal:` de
  `biblias/104-steven-universe/biblia.md`, `biblias/17-arcane/biblia.md` y
  `biblias/13-rick-and-morty/biblia.md` (sólo la cabecera, no se leyeron enteras: no son mi rol).
- **Imágenes miradas de verdad** (bajadas con `curl` + cabecera `Referer`, convertidas de WebP con
  Pillow y abiertas con Read): `666 News main series.png` y `VoxTek Logo.png` — corrigió la
  descripción del punto 6, que al principio se basó sólo en el wikitext de la wiki y no coincidía
  con lo que se ve en la imagen real. Colores medidos con Pillow (`Image.getpixel`): fondo de 666
  News ≈ `#280101`, cian del logo ≈ `#64BBB7`, wordmark VoxTek ≈ `#50DADB`.
