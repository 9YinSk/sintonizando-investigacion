# Parte de TEXTO, JUEGOS Y TÉCNICA · Reanimal (encargo 123)

Investigador de texto, juegos y técnica. Puntos 5, 6, 11, 18, 24 y 25 de ENCARGO.md.
Aviso: `datos-texto.md` (recolectado automático) sólo trajo capturas de Steam; los
otros bloques del recolector (Danbooru/Safebooru/Wallhaven en `datos-imagen.md`)
se confundieron con Touhou/Madoka porque «los dos hermanos» no encontró página
en Fandom con ese nombre. Los personajes reales son **The Boy** y **The Girl**
(la wiki los llama también The Brother / The Sister), confirmado en
https://reanimal.fandom.com/wiki/The_Boy y https://reanimal.thqnordic.com ✅.

## 5 · Tipografía, una letra por uso

*REANIMAL* es un videojuego sin manga ni cómic propio (a diferencia de *Little
Nightmares*, que sí tiene tie-in). No hay globos, así que varias filas de la
tabla clásica «no aplican» y se explica por qué. Tildes, ñ y ¿¡ comprobadas
abriendo el archivo real de Google Fonts con `fontTools.ttLib.TTFont(...).getBestCmap()`
(script en `/tmp/claude-0/trabajo/123-reanimal-texto/fonts`), no de memoria.

| Uso | Qué se ve de verdad | Letra libre más parecida | ¿Tildes, ñ, ¿ ¡? |
|---|---|---|---|
| Logo o título | «REANIMAL» en el logo del soundtrack: mayúsculas muy condensadas, palo grueso uniforme, remates rectos, rojo sobre negro (visto en la carátula del álbum, captura de Steam del DLC *REANIMAL Soundtrack*) ✅ · https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4430060/2ce879b678581a26e0540f892a5e3ac8a3e73573/ss_2ce879b678581a26e0540f892a5e3ac8a3e73573.1920x1080.jpg | **Anton** (Google Fonts, OFL) por peso y condensación; alternativas **Big Shoulders Display** ExtraBold o **Bebas Neue Pro** ⚠️ (comparación visual del investigador; el sitio oficial no da crédito de letra para el logo) | Sí ✅ (cmap comprobado) |
| Web e interfaz oficiales | La web `reanimal.thqnordic.com` usa una letra de pago autoalojada, **«Fabrikat»** (Regular, Italic, Black, BlackItalic) en `/fonts/fabrikat-*.woff`, declarada en su CSS ✅ (visto en el HTML de la propia web) | **Barlow Condensed** ExtraBold (Google Fonts, OFL) por proporción y peso; también sirve para subtítulos y menús | Sí ✅ (cmap comprobado) |
| Cartel del mundo (letrero real, en juego) | Rótulo de neón rojo **«CINEMA»** sobre la marquesina del cine, en el pueblo inundado; tubo redondeado, mayúsculas anchas con relleno de bombillas debajo ✅ (visto, captura oficial de Steam) · https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2129530/7c4e789ddae8dbaaa8705f98ac3e77a58baee2d0/ss_7c4e789ddae8dbaaa8705f98ac3e77a58baee2d0.1920x1080.jpg | **Monoton** (Google Fonts, para el efecto de tubo de neón) o, si se quiere una letra de marquesina más plana, **Bungee** ⚠️ (propuesta visual, sin crédito oficial) | No se comprobó (decorativa, sólo mayúsculas de cartel) |
| Globo normal, grito, pensamiento, onomatopeya (manga) | **No aplica.** *Reanimal* no tiene manga ni cómic propio; no hay globos ni onomatopeyas dibujadas en pantalla en ninguna de las 14 capturas oficiales de Steam revisadas ✅ | — | — |
| Diálogo hablado / subtítulos | Hay diálogo susurrado y escaso —«por primera vez en tres juegos», dice la reseña— y **se subtitula entero**; sin pistas sólo de audio (accesibilidad) ✅ · https://gamecritics.com/jason-ricci/reanimal-review/ · confirmado también por la lista de idiomas de Steam (Subtítulos en 15 idiomas) ✅ | **Barlow Condensed** o **Noto Sans** (cubre además coreano/chino/japonés, ver abajo) | Sí ✅ |
| Interfaz de juego (menús, HUD) | **No se encontró ninguna captura de menú**: las 14 imágenes oficiales de Steam evitan mostrar HUD; en partida no hay barra de vida, mapa ni inventario visibles, igual que en *Little Nightmares* (comparación con 122-little-nightmares ✅) ⚠️ (sin captura propia de menú) | Barlow Condensed / Noto Sans | — |
| Letreros y coleccionables (Posters) | 20 «Posters» de papel por nivel; al recogerlos desbloquean arte conceptual en el menú, **no llevan texto legible**, son ilustraciones · https://reanimal.fandom.com/wiki/Posters ✅ | — | — |

**Letras para coreano, japonés y chino** (el juego trae interfaz y subtítulos en
Japonés, Coreano, Chino tradicional y Chino simplificado, comprobado en la
tabla de idiomas de Steam ✅): la familia libre equivalente es **Noto Sans**
(Noto Sans JP / KR / SC / TC, Google + Adobe, licencia OFL). Comprobado con
fontTools sobre el archivo real de Noto Sans JP: cubre hiragana (あ), katakana
(ア) y kanji comunes (字), además de tildes, ñ y ¿¡ latinas ✅. Es la opción
segura para cualquier texto del canal que quiera imitar la interfaz del juego
en otro idioma.

## 11 · Videojuegos de la franquicia

*Reanimal* es una IP nueva de Tarsier (no viene de otra franquicia), así que
«los videojuegos de la franquicia» son el juego base y su expansión. La tabla
sale de Steam (`datos-texto.md`) y de la wiki, cruzados ✅.

| Juego / DLC | Fecha | Qué añade |
|---|---|---|
| *REANIMAL* | 13-feb-2026 | Juego base: The Boy y The Girl, 9 capítulos, cooperativo a pantalla partida compartida (no split-screen) |
| *REANIMAL: The Prisoner* (cap. 1 de *The Expanded World*/Season Pass) | 7-ago-2026 | Nuevos protagonistas: The Prisoner y The Soldier, en una zona de guerra estilo I Guerra Mundial; The Mother y Spider Kids como monstruos nuevos ✅ https://reanimal.fandom.com/wiki/REANIMAL:_The_Expanded_World |
| *REANIMAL – Season Pass* | 13-feb-2026 | Acceso a los 3 capítulos de *The Expanded World* (2º cap. oct-dic 2026, 3º ene-mar 2027) ✅ |
| *REANIMAL - Foxhead and Muttonhead Masks* | 13-feb-2026 | DLC cosmético: máscaras de zorro y cordero para ambos hermanos (nombres que dan origen a los apodos «Fox»/«Mutton» del encargo) ✅ https://reanimal.fandom.com/wiki/Masks |
| *REANIMAL Soundtrack* | 21-jul-2026 | Banda sonora digital; su carátula trae el logo definitivo y el símbolo de la ballena espiral (punto 25) ✅ |
| *REANIMAL Demo* | 13-oct-2025 | Demo jugable previa al lanzamiento, disponible en Steam |

**Interfaz y menús:** no se encontró ninguna captura oficial de un menú o
pausa (ni en las 14 capturas de Steam ni en la wiki); en partida no hay HUD
visible (punto 6) ⚠️. Los **mandos** sí están documentados completos, con
tabla por plataforma (PS5, Xbox Series X/S, Switch 2, teclado) en
https://reanimal.fandom.com/wiki/Controls ✅: moverse, correr, agacharse,
interactuar, usar objeto, mechero/linterna (`F`/`RB`/`R`), «Llamar» al otro
jugador (`C`/`LB`/`L`, igual mecánica que en *Little Nightmares II*), y un
set aparte de controles de vehículo (barco/carrito) con acelerar, retroceder,
impulso y bocina/ataque.

**Cajas de diálogo: ninguna visible en pantalla** (punto 6): el diálogo
existe pero se resuelve con subtítulos de accesibilidad, no con un cuadro de
texto con marco propio del juego ✅.

**Logros (Achievements):** existen en Steam (categoría confirmada en la ficha
de la tienda) pero no se consiguió el texto exacto de cada uno ⚠️ — página de
la wiki https://reanimal.fandom.com/wiki/Achievements sin revisar a fondo por
límite de tiempo.

## 6 · Cómo hablan y piensan en pantalla

Es lo más importante para la lámina: aquí NO va una burbuja blanca genérica.
*Reanimal* apuesta por el silencio, no por el globo.

- **Sin globos ni cartelas de manga**: no hay tie-in de cómic (a diferencia de
  *Little Nightmares*, que sí tiene una miniserie). Confirmado revisando las 14
  capturas oficiales de Steam y la wiki de Fandom (no hay página de «cómic» o
  «comic») ✅.
- **Diálogo real pero mínimo y susurrado**: es la primera vez en tres juegos de
  Tarsier (los dos *Little Nightmares* no tenían diálogo hablado inteligible)
  que hay líneas habladas, aunque escasas, para no romper el misterio · reseña
  de Gamecritics ✅ · https://gamecritics.com/jason-ricci/reanimal-review/
- **Se subtitula todo**: «All dialogue is subtitled, and there are no
  audio-only cues for tasks that need to be completed. Subtitles cannot be
  resized» [Todo el diálogo lleva subtítulo, y no hay pistas sólo de audio
  para las tareas. Los subtítulos no se pueden agrandar] · misma reseña,
  sección de accesibilidad ✅.
- **15 idiomas con subtítulos** (incluido español de España y español
  Latinoamérica, con doblaje completo en LATAM) según la ficha de idiomas de
  Steam ✅ · https://store.steampowered.com/app/2129530/REANIMAL/ — dato que
  también interesa al investigador de voz (punto 8).
- **Nada de HUD ni iconos flotantes** sobre los personajes en ninguna de las 14
  capturas oficiales revisadas: sin barra de vida, sin indicador de objetivo,
  sin burbuja de pensamiento. La única señal en pantalla es la luz del
  mechero/linterna que llevan los hermanos ✅ (visto), igual que en *Little
  Nightmares* (comparación con 122-little-nightmares, punto 11 de esa biblia) ✅.
- **Los "Posters" y cuadros del mundo no llevan texto legible**: son ilustración
  pura (pinturas, retratos, fotos) — lista completa en
  https://reanimal.fandom.com/wiki/Paintings,_Portraits,_and_Photos ✅. No hay
  diarios ni notas escritas que se puedan leer en pantalla (a diferencia de
  otros juegos de terror con notas de papel).
- **Pensamiento:** no existe una convención visual para ello (no hay flash-back
  con texto ni burbuja); los sueños del Boy y la Girl se narran con escenas
  jugables, no con texto en pantalla · descripción de «Historia» en
  https://reanimal.fandom.com/wiki/The_Boy ✅.

**Para la lámina:** en vez de un globo de cómic, la voz del canal puede ir
escrita como si fuera un **subtítulo de juego**: una barra semitransparente
abajo, mayúsculas contenidas, sin comillas de cómic. Es fiel al juego y evita
la «burbuja blanca genérica» que rechazó el dueño.

**Fuentes comprobadas con fontTools** (glifos á é í ó ú ñ Ñ ü ¿ ¡, los diez
presentes = ✅): Anton ✅, Barlow Condensed ✅, Big Shoulders Display ✅,
Permanent Marker ✅, Yanone Kaffeesatz ✅, Noto Sans JP ✅ (+ hiragana/katakana/kanji).
La variable CSS `--yanonekaffeesatz-font` aparece en el HTML del sitio oficial
aplicada a los botones rojos «Wishlist»/«Buy», pero **no se puede confirmar si
carga de verdad esa letra** (no hay `@font-face` visible para ella en el HTML
descargado): posible resto de la plantilla genérica de THQ Nordic ⚠️.
