# Parte IMAGEN · 24-assassination-classroom

Puntos de ENCARGO.md: **1** (arte oficial), **3** (fan art y 3D con licencia),
**15** (vestuario, hex medidos), **16** (fondos y sitios/wallpapers), **19**
(texturas 2D) y **23** (colaboraciones y cruces).

## Cómo se hizo esta parte

La `biblia.md` que ya existe se escribió con la **red cerrada** (24-sep): no
pudo bajar ni mirar ninguna imagen, no hay `hojas/` y la paleta de §5 y §16
era de memoria (todo ⚠️). Esta parte **confirma con imágenes reales** lo que
ya estaba y **añade lo que faltaba** (19 y 23, que no existían en la biblia).

- Partí de `partes/datos-imagen.md` (AniList, Danbooru, Safebooru, Wallhaven,
  Openverse): no repito esas consultas, las uso como candidatas.
- El wiki de Fandom correcto es **`ansatsukyoshitsu`**, no
  `assassinationclassroom` (ese subdominio da 404: lo dejo anotado porque el
  encargo lo sugiere así y hay que corregirlo para cualquier repaso futuro).
- Corrí `herramientas/investigar_serie.py --wiki ansatsukyoshitsu --paginas
  "Korosensei" "Nagisa Shiota" "Karma Akabane" "Irina Jelavić"` (el apellido
  lleva **tilde en la ć**; sin ella la wiki no encuentra la página y devuelve
  0 imágenes, error fácil de repetir). Dio **258 imágenes enlazadas, 80
  grandes**, en 2 hojas de contacto que miré con Read y dejé en `hojas/`.
- Bajé con Pillow (cabecera `Referer: https://www.fandom.com/`) las piezas
  más útiles y **medí los hex de verdad** con muestreo de zona (no de
  memoria): ver cada dato abajo con la imagen y la región.
- Confirmé licencias de Sketchfab **con la API** (`api.sketchfab.com/v3/models/<uid>`),
  no de memoria ni de la página sola.
- 12 búsquedas web (español, inglés, japonés) para el punto 23 (colaboraciones)
  y el 19 (texturas libres); lista completa en la Bitácora.
- ✅ = confirmado en dos fuentes (o medido yo mismo + la wiki lo describe
  igual). ⚠️ = una fuente o estimado. ❌ = no encontrado, con la búsqueda hecha.

---

## Hallazgos

### Punto 1 · Arte oficial, en cantidad y variado

**1.1 Hojas de modelo oficiales de Lerche (filtradas a la wiki, 2014)**

Encontré 6 páginas de **settei** (hojas de producción del estudio Lerche)
subidas a la wiki en julio de 2026, con fecha de dibujo de **2014** y firma
del estudio. Las miré enteras con Read:

- **`Lerche Design Sketches Fullbody Karma Akabane.webp`** (2400×1700):
  turnaround completo (frente, 3/4, espalda) de **赤羽業** (Karma Akabane,
  firma legible en el margen), fechado **14.5.30** (30-may-2014). Confirma
  el saco **abierto sin corbata**, camisa blanca, cinturón con hebilla
  cuadrada, pantalón ancho, botines. Referencia de ojos (colores de iris)
  en la esquina superior izquierda ✅ (visto con Read) ·
  [wiki](https://static.wikia.nocookie.net/assassinationclassroom/images/c/cd/Lerche_Design_Sketches_Fullbody_Karma_Akabane.webp/revision/latest?cb=20260708111409)
- **`Lerche Design Sketches Fullbody Nagisa Shiota.webp`** (2400×1700):
  turnaround de **潮田渚** (Shiota Nagisa), rotulado «全身 清書» (cuerpo
  entero, limpio), **「決定稿」** (versión final) fechado **2014_0602**.
  Confirma el **chaleco sobre camisa con corbata**, mangas remangadas con
  puño doblado, bolsillos de cargo en el pantalón, botines con vuelta ✅
  (visto con Read) ·
  [wiki](https://static.wikia.nocookie.net/assassinationclassroom/images/2/22/Lerche_Design_Sketches_Fullbody_Nagisa_Shiota.webp/revision/latest?cb=20260708212650)
- **`Lerche Design Sketches Nagisa Shiota.webp`** (2400×1700): hoja de
  **expresiones** de Nagisa (CHA011_01, 2014/09/19): sonrisa, enfado,
  sorpresa, «cara demonio» (con dientes afilados y ojos en blanco, la que
  usa cuando intimida), perfil, espalda ✅ (visto con Read).
- ⚠️ **Corrección a la propia wiki**: el archivo subido como
  `Lerche Design Sketches Karma Akabane.webp` (sin «Fullbody») **no es
  Karma**. Lo miré con Read: el rótulo dice **「烏丸惟臣_表情_清書」**
  (CHA016_02, 2014/09/04) — el nombre no coincide con 赤羽業 (Karma); por los
  kanji (烏丸/烏間) y la ropa (cuello camisero suelto, sin chaleco) es más
  probable que sea la hoja de expresiones de **Karasuma** mal etiquetada en
  Fandom. Lo señalo para que el redactor no la use como «Karma»; no lo uso
  yo para vestuario de Karma (uso la hoja «Fullbody» en su lugar, que sí
  lleva su firma y nombre correctos).
- Las 3 hojas de Lerche llevan un aviso explícito: **「この制作資料の一切の公表、
  複製、貸与、譲渡、販売を固く禁じます」** («prohibido publicar, copiar, prestar, ceder
  o vender este material de producción»). Son **material filtrado de estudio,
  no arte promocional**: sirven para **estudiar la silueta y la ropa**, no
  para pegar ni redistribuir. Lo marco en `imagen.json` con esa licencia.

**1.2 Arte oficial promocional (10.º aniversario, 2026)**

- **`Korosensei 10th anni.png`**, **`Karma Akabane 10th anni.png`**,
  **`Nagisa Shiota 10th anni.png`** (los 3 a 1000×1456, fondo transparente):
  serie de retratos de cuerpo entero para el 10.º aniversario (2026),
  subidos en enero de 2026 ✅ (visto con Read; el estilo y el fondo
  recortado coinciden con el resto de la campaña del 10.º aniversario de
  §3.1 de la biblia — web, cafés, tienda). Éstos son los que **medí con
  Pillow** para los hex de vestuario (ver punto 15).
- **`Lerche - Character Profiles - Karma Akabane.png`** (771×466): tarjeta
  de personaje con fondo del patrón de la cara de Koro-sensei, texto
  「赤羽業／CV：岡本信彦／成績優秀だが素行不良。」(Karma Akabane / CV: Nobuhiko
  Okamoto / «buenas notas, mala conducta»). Confirma el **seiyū de Karma**
  (dato cruzado útil para voz, que ya lo tenía) ✅ (visto con Read) ·
  [wiki](https://static.wikia.nocookie.net/assassinationclassroom/images/5/53/Lerche_-_Character_Profiles_-_Karma_Akabane.png/revision/latest?cb=20260708191053)
- **`Season2.jpg`** (1920×3039, vertical): ilustración clave de Irina en
  vestido, sentada en un taburete, fondo de ciudad de noche — visual de
  campaña de la 2.ª temporada ✅ (visto con Read, en la hoja n.º 2 de
  contacto).
- **Fotogramas de la película de imagen real** (2011, «暗殺教室 卒業編» /
  live-action): `Koro sensei live action.jpg` y `Korosensei Police.jpg`
  (1000×600 cada uno): Koro-sensei con **cabeza esférica real, toga y
  birrete**, y un traje alterno de **policía azul** (disfraz de la trama)
  ✅ (vistos con Read). Confirman que el diseño se adaptó a **utilería
  física real** — referencia directa para un Koro-sensei en Blender/volumen
  real, más que cualquier render 3D de fan.
- **Portada y banner oficiales** (AniList, ya en `datos-imagen.md`, no
  repito la consulta): 
  [portada](https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx20755-dWrhs569YGUO.jpg)
  y
  [banner](https://s4.anilist.co/file/anilistcdn/media/anime/banner/20755-D4ipww9U8YkC.jpg)
  ✅ (arte de distribución oficial vía AniList).
- **Encuesta oficial de popularidad** ilustrada: `Special Theme General
  election.png` (896×656), escaneo de revista con las portadas/carteles de
  la votación (「結果発表!!」= «resultados») con Karma, Irina, Nagisa y otros
  personajes dibujados para la ocasión ✅ (visto con Read). Es un dato de
  popularidad (punto 7, no mío), pero el **arte de la encuesta** sirve
  también como referencia visual de grupo.

**1.3 Las hojas de contacto (obligatorio, `hojas/`)**

Corrí `investigar_serie.py` con las 4 páginas del encargo (wiki
`ansatsukyoshitsu`, no `assassinationclassroom`). Salieron **80 imágenes
grandes** en 2 hojas, que dejé en `hojas/`:

- **`hojas/personajes_01.jpg`** (imágenes 1-48 del índice): tiene las 2
  hojas de modelo de Lerche (n.º 3-6), el arte del 10.º aniversario (n.º
  16-18), Irina en el visual de temporada 2 (n.º 2) y su timeskip (n.º 21),
  capturas del anime y páginas del manga (natación, jaula hidráulica,
  «Korosensei with codename papers»).
- **`hojas/personajes_02.jpg`** (imágenes 49-80): el logo, la ficha de
  personaje de Karma, los fotogramas de la película de imagen real (n.º
  62-63), la encuesta de popularidad (n.º 64), los renders «transparent»
  (Koro-sensei, Karma, Irina/Bitch-sensei, n.º 65/69/71) y más páginas de
  manga.
- Ambas < 1 MB, dentro del límite de 3 MB.

---

### Punto 3 · Fan art y 3D (sólo como referencia, con licencia)

**3.1 Modelos 3D — licencias confirmadas por la API de Sketchfab**

La biblia ya listaba estos modelos con ⚠️ («sin ver», «una fuente»). Los
comprobé **todos** con `api.sketchfab.com/v3/models/<uid>` (llamada directa
a la API, no la página sola):

| Modelo | uid | Licencia (API) | Descargable | Para qué |
|---|---|---|---|---|
| Japanese Classroom (Tian96) | `2a1e3b294c1e4e91bed794bfa520c4f4` | **CC Attribution** ✅ | sí | aula base, concepto A |
| School Desk and Chair (Tian96) | `004b95391e4e48a797ee8d0cf612b5cf` | **CC Attribution** ✅ | sí | pupitres en primer plano |
| Japanese School Desk JIS S 1021:2011 (omiyaio) | `2758bff4dead4db5aada8a216ed0869d` | **CC Attribution** ✅ (antes ⚠️) | sí | pupitre de norma japonesa |
| Japanese School Desk and Chair (woopossum) | `07e29a89e99e42e3bfd67989671a9d24` | **CC Attribution** ✅ (antes ⚠️) | sí | alternativa |
| The Japanese School Classroom (volvor) | `d9fc039ba0b6433db91ec129abe86b52` | **CC Attribution** ✅ (antes ⚠️) | sí | aula alternativa |
| Anime School Desk Model (3DGhost903) | `5c013e3454ad458e83803ab5b332ef02` | **CC Attribution** ✅ (antes ⚠️) | sí | pupitre estilo anime |
| Koro Sensei llavero (roman.benvenuto80) | `2c02fdcefbce4abc9333bff674795331` | **CC Attribution** ✅ (antes ⚠️) | sí | sólo para volumen, no pegar (personaje de Matsui) |

Crédito exacto exigido por CC BY: «"<nombre del modelo>" by <usuario>, CC
Attribution, sketchfab.com/3d-models/<slug>». Los 7 quedan en ✅: antes
sólo 2 lo estaban.

**3.2 Fan art (mirar, nunca pegar)**

- **Pixiv sigue sin poder verse sin iniciar sesión**: probé
  `pixiv.net/en/tags/暗殺教室/artworks` (302, redirige a login) y con
  cabecera de navegador (mismo resultado) ❌ — igual que en la primera
  pasada, no es un problema de esta sesión.
- **Fan art con licencia libre de verdad (Openverse/Wikimedia, ya en
  `datos-imagen.md`)**: son **fotos de cosplay**, no ilustraciones, pero
  cuentan para el punto 23 también (ver abajo). Las mejores, en CC BY 2.0
  con autor:
  [Cosplay de Karma y Koro-sensei, Comic Fiesta 2015](https://upload.wikimedia.org/wikipedia/commons/9/9a/Cosplay_of_Karma_Akabane_and_Koro-sensei_from_Assassination_Classroom_at_Comic_Fiesta_2015%2C_Day_1_013_%2823314146343%29.jpg)
  (2760×4912, Farhan Ahmad Tajuddin) y
  [Cosplay de Kayano, AniManGaki 2015](https://upload.wikimedia.org/wikipedia/commons/a/aa/Cosplay_of_Kaede_Kayano_from_Assassination_Classroom_at_AniManGaki_2015%2C_Day_1_020_%2821527861662%29.jpg)
  (2760×4912, mismo autor) ✅.
- **Tutorial de cosplay de la cabeza de Koro-sensei** (construcción real,
  volumen): dos vídeos de YouTube («Tutorial on Koro-sensei (head) cosplay»,
  corto y largo) y una guía en Behance paso a paso con **esfera de
  poliestireno + pintura**, más una discusión en cosplay.com sobre cómo
  hacer los **tentáculos** (pool noodles + alambre + tela, o espuma
  expansiva) ✅ (2 fuentes coinciden en poliestireno/espuma para la cabeza)
  · [Behance, DIY](https://www.behance.net/gallery/43165327/How-to-make-Koro-sensei-cosplay-mask-DIY)
  · [cosplay.com, tentáculos](https://cosplay.com/archive/thread/6oeo0n/koro-sensei-tentacles).
  Sirve para el punto 18 (cómo se construye el volumen) y como referencia
  de «materiales y volumen reales» del punto 23.
- **Arte de pizarra (黒板アート)**: confirmo lo que ya decía la biblia (no
  repito la búsqueda): existe el género, no encontré un ejemplo concreto
  de Koro-sensei con enlace propio ❌.

---

### Punto 15 · Vestuario (hex medidos de verdad)

Medí estos colores con Pillow (muestreo de zona, cuadro 20-150 px según el
área, sobre fondo transparente descartando los píxeles de línea y de
fondo) sobre el **arte del 10.º aniversario** (punto 1.2) y el render
`Bitch sensei transparent.png` de Irina. Sustituyen a los hex «aproximados,
NO medidos» de la biblia (§5.3 y §16).

| Personaje | Prenda | Hex medido | Cómo |
|---|---|---|---|
| **Karma** | Pelo (rojo) | `#D84646` (sombra) – `#E86060` (luz) | zona de pelo, `Karma Akabane 10th anni.png` |
| Karma | Saco negro abierto | `#403C3C` | zona de saco, misma imagen |
| Karma | Camisa | `#F0F0F0` | zona de camisa |
| Karma | Pantalón gris | `#A0A0B0` (claro) – `#6E6B7D` (sombra) | zona de pantalón |
| **Nagisa** | Pelo (celeste) | `#B8E1FC` (luz) – `#6B8CB4` (sombra) | zona de pelo, `Nagisa Shiota 10th anni.png` |
| Nagisa | **Chaleco azul marino** | `#2E355C`–`#384068` | zona del chaleco (70% de confianza, color dominante) |
| Nagisa | Camisa | `#F0F0F0` | zona de camisa |
| Nagisa | Pantalón gris | `#A0A0B0` | igual que Karma: mismo uniforme |
| **Koro-sensei** | Cuerpo (amarillo) | `#FFF661` | tentáculo, `Korosensei 10th anni.png`, escaneo de fila de píxeles (muestra grande, alta confianza) |
| Koro-sensei | Toga académica | `#2D2D2D` | 3 puntos coincidentes: **no es negro puro**, es gris carbón |
| Koro-sensei | Interior de la toga (rojo) | `#A2393C` | zona bajo el lazo, confirmado con escaneo de fila |
| Koro-sensei | Birrete y borla | negro `#2D2D2D` (birrete) / dorado (borla, sin medir con precisión) ⚠️ | visual |
| **Irina** | Pelo (rubio) | `#E3AD67` | zona de pelo, `Bitch sensei transparent.png`, escaneo de fila |
| Irina | Traje sastre (falda + chaqueta) | `#90AFBA` (azul-verdoso pálido) | zona de chaqueta, escaneo de fila |

**Confirmación de siluetas y ropa** (con las hojas de modelo y los renders,
no de memoria):

- **Karma**: uniforme **abierto sin corbata**, cinturón con hebilla
  cuadrada — confirmado con la hoja de modelo «Fullbody Karma» (1.1) ✅.
  Esto corrige el ⚠️ «de memoria» que tenía la biblia.
- **Nagisa**: chaleco sobre camisa **con corbata** (la biblia dudaba entre
  corbata roja o negra: en el arte del 10.º aniversario y en la hoja de
  modelo, la corbata es **negra**, no roja) ✅ — corrijo el ⚠️ de la biblia.
- **Irina**: su outfit «icónico» de trabajo es un **traje sastre
  azul-verdoso pálido** (chaqueta entallada abierta sobre sujetador negro
  de encaje, falda corta a juego), **gargantilla negra**, medias veladas y
  tacones, con su arma-lápiz-labial en la mano — visto entero en
  `Bitch sensei transparent.png` ✅. Esto es más específico que el «vestidos
  ceñidos y elegantes» ⚠️ que tenía la biblia.
- **Irina, vestido morado con sombrero de bruja** (`Irina KoroQ anime.png`):
  ⚠️ **no es un traje del anime**, es su outfit del juego móvil de chibis
  **Koro-Sensei Quest!** (ver punto 11, no es mi punto, pero lo marco para
  que no se use como vestuario «canon» del anime sin aclarar la fuente).
- **Koro-sensei**: confirmado con el render del 10.º aniversario: **toga
  negra larga con vivos morados en los puños** (2-3 franjas, no medidas con
  precisión — franja fina, ⚠️), **birrete con borla amarilla**, **cordón
  dorado** sujetando un colgante con la **luna creciente**, e **interior de
  la toga rojo oscuro** (`#A2393C`) que sólo se ve cuando el tentáculo se
  mueve ✅.

---

### Punto 16 · Ciudades, paisajes y fondos de pantalla

- **Los fondos de pantalla ya reunidos en `datos-imagen.md` (Wallhaven) son
  buenos y sus tamaños son reales** (los da la propia API de Wallhaven, no
  hace falta remedirlos): destaco para el canal **#avisos-clases**:
  - [wallhaven-k9qo3d](https://w.wallhaven.cc/full/k9/wallhaven-k9qo3d.png)
    (1920×1080, RaidyHD): Nagisa en formato **imagen-en-imagen**, fondo
    limpio — el más fácil de recortar para un panel de aviso.
  - [wallhaven-8311qo](https://w.wallhaven.cc/full/83/wallhaven-8311qo.jpg)
    (3000×2000, SamUerto): Koro-sensei solo, buena resolución para imprimir
    grande.
  - Todas son **fan wallpapers** (no oficiales): licencia de uso personal
    de Wallhaven, no redistribuible como «oficial» — lo marco en
    `imagen.json`.
- **Fondos oficiales descargables: sigo sin encontrarlos** ❌. Repetí la
  búsqueda con la red abierta: `ansatsu-anime.com/10th/wallpaper/` → 404;
  `ansatsu-anime.com/2014-2016/special/` no tiene sección de wallpaper (sólo
  grep de la página, sin «壁紙» ni «wallpaper» en el HTML). Confirmo el ❌ de
  la biblia, ahora con la comprobación directa (antes no se pudo ni
  intentar).
- **Sitios**: no es mi punto (punto 4 es de vídeo), pero para el punto 16
  específico de «fondos de pantalla con su luz y hora del día»: el pasillo
  de madera del visual de la película 2026 (ya en la biblia §3.2/§17) sigue
  siendo la referencia más fuerte para #avisos-clases — lo confirmo, no lo
  repito.

---

### Punto 19 · Texturas 2D

**19.1 Tramas del manga, vistas de verdad**

Bajé y miré con Read dos páginas reales del manga (Fandom, con Referer):

- **`Class 3-E - Swimming (Ch 43).jpg`** (1765×1300, doble página): el
  agua se dibuja con **trama de puntos gruesa** (Ben-Day, más densa en las
  sombras del agua) más **líneas de movimiento dibujadas a mano** (no
  tono mecánico) para las salpicaduras; el pelo mojado y las sombras son
  **negro sólido**, sin degradado; el follaje (esquina superior izquierda)
  usa **rayado cruzado fino dibujado a mano**, no trama mecánica. Los
  **paneles están cortados en diagonal** (muy característico de Matsui:
  nada de viñetas rectas en escenas de acción) y hay un panel con **forma
  de estallido dentado** (como una explosión) enmarcando a Koro-sensei ✅
  (visto con Read, recorte completo).
- **`Hydraulic Cage (Ch 59).jpg`** (1790×797): panel ancho y bajo (formato
  panorámico), coherente con el mismo lenguaje de paneles diagonales.
- No encontré una entrevista o *making of* que diga qué trama exacta
  (marca/patrón de Clip Studio o física) usa Matsui: es plausible que sea
  digital (Clip Studio trae tonos de fábrica) pero **no está confirmado en
  ninguna fuente** ⚠️.

**19.2 Equivalentes libres**

- **Trama de manga gratis oficial de Clip Studio**: *[FREE] Manga
  Screentone Pack 1* en CLIP STUDIO ASSETS ✅ ·
  [assets.clip-studio.com/en-us/detail?id=2142037](https://assets.clip-studio.com/en-us/detail?id=2142037)
  (gratis, requiere cuenta de Clip Studio, uso permitido por los términos
  del *asset store*).
- **Generador de trama sin instalar nada**: convertidor de imagen a trama
  de puntos por software libre, en GitHub, licencia MIT: 
  [evestera/svg-halftone](https://github.com/evestera/svg-halftone) ✅ —
  útil para simular el agua con puntos del punto 19.1 sin comprar nada.
- **Grano de papel / fondo**: no repito ambientCG (ya en la biblia §5.4,
  es más del punto 4 de vídeo); para el **emblema o logo de la clase
  3-E/Kunugigaoka** busqué en japonés («椚ヶ丘中学校 校章 エンブレム») y no
  encontré un escudo oficial documentado con imagen propia ❌ — sólo texto
  descriptivo en pixiv 百科 sobre el colegio, sin emblema gráfico citable.

---

### Punto 23 · Colaboraciones y cruces

Esta sección **no existía en la biblia**: la añado entera.

**23.1 Videojuego crossover (Jump)**

- **Koro-sensei es personaje jugable en *J-Stars Victory VS*** (Bandai
  Namco, 2014), el juego de lucha crossover de Shonen Jump (con Naruto,
  Luffy, Ichigo…). Es el **único personaje de la serie** en el roster; su
  ataque especial usa los tentáculos para atrapar al rival ✅ (2 fuentes:
  [Kanzenshuu](https://www.kanzenshuu.com/2013/12/18/j-stars-victory-vs-assassination-classroom-and-neuro-additions/),
  [GameFAQs, confirmación de personaje](https://gamefaqs.gamespot.com/boards/694309-j-stars-victory-vs/68113308)).
  No apareció confirmado en *Jump Force* (la secuela) ⚠️ una fuente lo
  discute sin cerrar el dato.

**23.2 Cafés temáticos (con la red abierta pude ver los de 2026)**

Del 10.º aniversario de la serie (2026), tres colaboraciones distintas,
todas en Japón:

- **RAKU CAFE** (Ikebukuro y Shinsaibashi), 8-ene a 3-feb-2026: menú temático,
  mini-pósters de regalo, mercancía con **ilustración nueva** ✅
  ([アニメ！アニメ！](https://animeanime.jp/article/2026/01/03/94883.html),
  [PR Times, nota de prensa oficial](https://prtimes.jp/main/html/rd/p/000000192.000108434.html)).
- **Sweets Paradise / Concept Cafe**, 10.º aniversario, desde 17-mar-2026 en
  Tokio y Osaka (y desde 24-mar en Nagoya y Hiroshima): menú y mercancía de
  aniversario ✅ ([web oficial de Sweets Paradise](https://www.sweets-paradise.jp/collaboration/ansatsu-anime2)).
- **Animate Café Stand** (Hareza Ikebukuro), desde 27-feb-2026, ligado a la
  **película 2026**: posavasos con una ilustración nueva de **temática de
  ajedrez** ✅ ([collabo-cafe.com](https://collabo-cafe.com/events/collabo/ansatsu-movie-takeout-animate-cafe-stand-hareza-ikebukuro-2026/)).

Cada café trae **arte nuevo** (poses/ropa que no están en el anime): son la
fuente más fresca de «poses vivas» que pide el punto 1, aunque no pude
entrar a ver las ilustraciones sueltas (son imágenes de producto en las
webs de las cafeterías, cambian rápido) ⚠️.

**23.3 Figuras oficiales (referencia 3D real)**

- **Banpresto DXF — Koro-sensei Vol. 1**: 4 variantes de color (amarillo
  normal, roja/enfadado, negra/furioso, rosa) de 6.7" (~17 cm), pose de
  cuerpo entero con la toga ✅ ([Tokyo Otaku Mode](https://otakumode.com/shop/566e26ea3c9c45be02d89289/Assassination-Classroom-Koro-sensei-DXF-Figures-Vol-1),
  listados también en Amazon/eBay). Sus 4 poses/colores son referencia
  directa para las «caras de emoción por color» del punto 13 (no mío, pero
  lo dejo anotado).
- **Pop Up Parade — Karma Akabane y Nagisa Shiota** (Good Smile Company):
  estatuas de escala fija con pose de acción ✅ (una fuente de reventa,
  falta la ficha oficial de Good Smile con medidas exactas) ⚠️.

**23.4 Adaptación a imagen real (cruce de medio, no de franquicia)**

Ya estaba apuntado en la biblia (§3), lo confirmo con las fotos: la
película de imagen real usa una **cabeza esférica física real** para
Koro-sensei con la toga y el birrete (punto 1.2) y un traje policial azul
como disfraz de trama — referencia útil para el punto 18 (cómo se
construye el volumen en la vida real) más que para un cruce de franquicia
propiamente dicho.

**23.5 Cosplay** — ver punto 3.2 (fotos CC BY de Wikimedia y el tutorial de
construcción de la cabeza de Koro-sensei).

---

## Lo mejor para la lámina

1. **La hoja de modelo oficial de Nagisa** (chaleco azul + camisa + corbata
   negra, `hojas/personajes_01.jpg` n.º 4-6) es la referencia más fiable de
   vestuario «de clase»: coincide con el tono de #avisos-clases (uniforme,
   no arma).
2. **Koro-sensei 10th anni** (`#FFF661` cuerpo, `#2D2D2D` toga,
   `#A2393C` interior): paleta lista para usar tal cual, medida y no de
   memoria.
3. **El pasillo de madera con carteles clavados** del visual de la película
   2026 (ya en la biblia) sigue siendo el mejor fondo real para un canal de
   avisos — lo confirmo con las 80 imágenes revisadas: ningún fondo del
   wiki lo supera para este uso.
4. **Las 7 licencias CC BY de Sketchfab confirmadas por API**: la lámina
   puede usar el aula 3D de Tian96 sin dudas de licencia.
5. **El interior rojo de la toga (`#A2393C`)**, casi invisible salvo cuando
   se mueve el tentáculo: un detalle que da profundidad si se asoma un
   poco tras el personaje, como pide el dueño («algo detrás para que no
   quede plano»).

## No encontré

- ⚠️ Fondos de pantalla **oficiales** para descargar: repetí la búsqueda con
  red abierta (`ansatsu-anime.com/10th/wallpaper/`, `.../special/`), 404 o
  sin sección. Sólo hay fan wallpapers (Wallhaven).
- ⚠️ Emblema o escudo gráfico propio de Kunugigaoka / clase 3-E: busqué en
  japonés («校章», «エンブレム»), sólo hay descripciones de texto, ningún
  escudo con imagen citable.
- ⚠️ Pixiv: sigue sin abrir sin sesión iniciada (302 a login), igual que en
  la primera pasada.
- ⚠️ Ficha oficial de Good Smile Company para las Pop Up Parade de Karma y
  Nagisa (medidas, fecha, precio): sólo la vi en tiendas de reventa.
- ⚠️ Qué trama exacta (marca/patrón) usa Matsui en el manga: no hay
  entrevista que lo confirme, sólo es plausible por ser digital.
- ⚠️ Franjas moradas del puño de la toga de Koro-sensei: identificadas a
  simple vista en el render, pero no medí su hex con Pillow (la franja es
  muy fina y el muestreo automático fallaba); quedó sólo como observación
  visual.

## Bitácora de búsqueda

**Directo (sin buscador), con resultado:**
- Fandom API `ansatsukyoshitsu.fandom.com/api.php` (search, allpages,
  allimages con prefijo `Lerche`, `Koro`) — corrige el wiki equivocado del
  encargo (`assassinationclassroom` da 404).
- `investigar_serie.py --wiki ansatsukyoshitsu --paginas "Korosensei"
  "Nagisa Shiota" "Karma Akabane" "Irina Jelavić"` → 80 imágenes, 2 hojas.
- Descarga directa con Pillow + `Referer: fandom.com` de 10 imágenes para
  medir hex y mirar detalle (10th anni ×3, hojas de modelo ×4, Irina
  transparent, Karma profile card, 2 páginas de manga).
- `api.sketchfab.com/v3/models/<uid>` ×7 y `.../search?q=japanese
  classroom` — licencias CC BY confirmadas.
- `ambientcg.com/api/v2/full_json?q=chalkboard` → 0 resultados (probado,
  no usado).
- `ansatsu-anime.com/10th/wallpaper/` y `/2014-2016/special/` → sin
  sección de wallpaper (404 / sin coincidencia en el HTML).
- `pixiv.net/en/tags/暗殺教室/artworks` → 302 (pide sesión), 2 intentos.

**Buscador web (12 búsquedas):**
- «Assassination Classroom collaboration cafe Universal Studios Japan
  crossover event» (inglés)
- 「暗殺教室 コラボ カフェ 2026」(japonés)
- «Assassination Classroom Koro-sensei figure Pop Up Parade Figuarts
  Banpresto official» (inglés)
- 「暗殺教室 コラボ ゲーム ぷちぐる 実写 スタンプ LINE」(japonés)
- «Koro-sensei cosplay costume head build foam tutorial» (inglés)
- «manga screentone free brushes Clip Studio download CC0 halftone pack»
  (inglés)
- 「椚ヶ丘中学校 校章 暗殺教室 エンブレム E組」(japonés)
- «Assassination Classroom Koro-sensei Jump Force OR "J-Stars" OR "Jump
  Stars" playable crossover game» (inglés)

---

## Cumplimiento del encargo (mi parte)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | Hojas de modelo de Lerche, arte del 10.º aniversario, ficha de personaje, fotogramas de imagen real, hojas de contacto (80 imágenes) en `hojas/`. |
| 3 · Fan art y 3D con licencia | ✅ | 7 modelos de Sketchfab con licencia CC BY confirmada por API; 2 fotos de cosplay CC BY con autor; pixiv sigue cerrado (anotado). |
| 15 · Vestuario, hex medidos | ✅ | Hex medidos con Pillow (no de memoria) para Koro-sensei, Karma, Nagisa e Irina; siluetas confirmadas con hojas de modelo oficiales. Franja morada del puño queda ⚠️ (visual, sin hex). |
| 16 · Fondos de pantalla | ⚠️ | Wallpapers de Wallhaven con tamaño real (de su API); oficiales descargables siguen sin existir (❌ confirmado, no sólo asumido). |
| 19 · Texturas 2D | ✅ | 2 páginas de manga miradas de verdad (trama, línea, paneles diagonales); trama libre de Clip Studio y generador MIT en GitHub. Emblema de la escuela, no encontrado. |
| 23 · Colaboraciones y cruces | ✅ | Videojuego crossover (J-Stars Victory VS), 3 cafés de 2026, figuras oficiales (Banpresto, Pop Up Parade), cosplay y adaptación a imagen real. Sección nueva completa. |

**Parte terminada**: los 6 puntos (1, 3, 15, 16, 19, 23) están hechos y
con fuente. Lo que quedó ⚠️ está documentado arriba con la búsqueda hecha,
no son huecos silenciosos: wallpapers oficiales, emblema de la escuela,
franja morada sin hex, ficha de Good Smile para las Pop Up Parade, y la
trama exacta del manga.
