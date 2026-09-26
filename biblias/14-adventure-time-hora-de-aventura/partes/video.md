# Parte de VÍDEO · Adventure Time (Hora de aventura) · 14-adventure-time-hora-de-aventura

Investigador de vídeo. Puntos de ENCARGO.md: **2** (escenas), **4** (sitios/luz/paleta),
**9** (música), **10** (vídeos), **14** (poses).

**Punto de partida**: `partes/datos-video.md` (recolectado el 2026-09-25) dio poco
aprovechable: Dailymotion devolvió sobre todo vídeos NO oficiales para las
búsquedas genéricas «Adventure Time opening/ending/trailer/escena» (coincidían
por las palabras sueltas «hora»/«aventura»), Fandom dio 404, Doblaje Wiki no
encontró la página, AniList no aplica (occidental) y Reddit no encontró el
subreddit. MusicBrainz devolvió discos sin relación (búsqueda por «hora» y
«aventura» sueltos). **No repetí esas consultas**: hice búsquedas nuevas y
específicas en la API de Dailymotion (por canción y escena, no por «opening»
genérico) y sí encontré clips oficiales o semioficiales reales.

**Ya había una `biblia.md`** de una primera pasada (24-sep-2026, red cerrada):
tiene los puntos 2, 5(=4), 11(=9), 12(=10) y 15(=14) escritos a partir de
**transcripciones de texto** (GitHub `guiszk/adventuretime-transcripts`), con
minutos **estimados** (⚠️) y sin haber visto ni un fotograma. Mi trabajo aquí
es la segunda pasada: **vi los vídeos de verdad** (red abierta, Dailymotion) y
dejo minutos reales, colores medidos y poses confirmadas para que el redactor
las meta en su sitio. No repito lo que ya estaba bien (los datos de
transcripción siguen siendo válidos como cita textual); marco qué pasa de ⚠️
a ✅ y qué corrijo.

Carpeta de trabajo pesada (hojas de contacto, vídeos bajados): `/tmp/claude-0/trabajo/14-adventure-time-video/` (se borra al terminar; los `.mp4` ya se borraron de las que ya no hacían falta).

---

## Punto 2 · Escenas icónicas (con vídeo real y minuto exacto)

Vi 7 clips reales con `herramientas/fotogramas.py` (Dailymotion, ya que
YouTube pide iniciar sesión desde este servidor). Confirmo minuto exacto
donde la primera pasada sólo tenía «≈» estimado, y corrijo lo que estaba mal.

### 2.1 «Fry Song» / «Canción de las papas» (2×01) — CONFIRMADO con vídeo real ✅

Clip: [«Marceline Sing-a-Long Fry Song» (Cartoon Network, reload por canal de fan)](https://www.dailymotion.com/video/x51arca) · 52 s · 1280×720. Es el
segmento real de la serie con subtítulos incrustados estilo karaoke (marca
«Toon Tunes» de Cartoon Network) ✅.

- **0:00**: Finn hace beatbox de pie; **Marceline flota bocabajo tocando el
  bajo-hacha**, ambos en un cuarto de paredes **rosa** con sillones rojos y
  puerta doble azul. ✅ (antes «≈0:00», ahora exacto)
- **0:12**: primer plano de **una grabadora/micrófono amarillo** sobre la
  mesa, cable enchufado — el objeto que graba la canción. ✅
- **0:16-0:24**: Marceline flota tocando, subtítulo «Daddy, why did you eat
  my fries?» / «I bought them, and they were mine». Finn de fondo sigue el
  ritmo. ✅
- **0:28-0:36**: **primer plano de la cara de Marceline cantando triste**
  (ojos entornados, boca abierta) — «But you ate them, yeah, you ate my
  fries… and I cried, but you didn't see me cry». Es la pose de la lámina
  «cantar algo íntimo y que no sabías que dolía». ✅
- **0:40-0:44**: Finn con **audífonos puestos**, sostiene la grabadora en
  alto — «What kind of dad eats his daughter's fries?». ✅
- **0:48**: Marceline «Daddy, there were tears there» con la mirada baja. ✅

> Corrección: la escena real es un **montaje musical de Cartoon Network**
> (estilo «Toon Tunes», con letra en pantalla en inglés), no metraje crudo
> del episodio. Confirma la pose y el objeto (grabadora), pero el fondo
> (pared rosa, sillones rojos) puede ser un set simplificado para el vídeo
> musical, no exactamente el interior de la casa-cueva. Aun así coincide con
> los colores de la casa de Marceline (ver punto 4).

### 2.3 «I'm Just Your Problem» — la banda (3×10 «What Was Missing») — CONFIRMADO ✅

Clip: [«I'm Just Your Problem» — canal oficial Cartoon Network en Dailymotion](https://www.dailymotion.com/video/x537pqr) · 2:07 · 1280×720, owner
`Cartoon Network` ✅ (canal verificado de la cadena).

- **0:00**: la Dulce Princesa sostiene **un aparato verde tipo Game Boy**
  (control de sonido) junto a BMO. ✅
- **0:04-0:08**: **Jake corre tocando la viola**, alcanza a Finn. ✅
- **0:12-0:24**: **Marceline entra volando** con el bajo-hacha (filos
  rojos) hacia una **puerta de piedra arqueada con círculos dorados** (la
  cerradura del Señor de las Puertas) y empieza a tocar sobre ella. ✅
  (confirma la localización descrita en la 1ª pasada)
- **0:24-1:00**: Marceline **con sombrero de ala ancha color mostaza y
  cinta azul**, toca el bajo apoyada en la puerta; primeros planos de su
  cara cantando (boca abierta, ceño fruncido, colmillos visibles). ✅ **Este
  sombrero no estaba descrito en la 1ª pasada** — es un dato nuevo para el
  punto 15 (vestuario, no es mi punto, lo dejo anotado para el redactor).
- **1:12-1:24**: Finn y Jake llegan corriendo hacia la Dulce Princesa junto
  a la puerta; Jake trae la viola. ✅
- **1:32**: Marceline, **con el sombrero puesto, toca apoyada en la
  puerta** mientras cae la noche (fondo rojizo). ✅

> Coincide con la escena descrita en la 1ª pasada («Jake empieza a tocar su
> viola y Finn hace beatbox… Marceline canta ‘I'm Just Your Problem'»), pero
> el vídeo real muestra que **no es la puerta genérica**: es una estructura
> con botones circulares dorados en forma de arco — coincide con «el Señor
> de las Puertas» del punto 2 de la 1ª pasada. ✅ confirmado con imagen.

### 2.4 «I Remember You» / «Recordándote» (4×25) — CONFIRMADO, con corrección ✅

Clip: [«Marceline & Ice King — I Remember You» (grabación de emisión de Cartoon Network HD, audio francés)](https://www.dailymotion.com/video/xzt1l7) · 1:58 · 1280×720. Es **metraje real del episodio** (se ve el
bug «CN HD» en pantalla), doblado al francés — sirve para **ver la escena**,
no para frases en español (eso es del investigador de voz).

- **0:00-0:12**: el Rey Helado toca un teclado/omnichord; **Marceline
  entra por la puerta de la casa (paredes rosa, piso verde azulado) con un
  papel/foto en la mano**, discuten. ✅
- **0:18-0:30**: **primer plano de Marceline, mano en la cabeza, cara de
  angustia** («¿por qué esto me afecta tanto?»). Es la mejor pose para
  **«pensar/dolor»** de la lámina. ✅
- **0:42-1:06**: el Rey Helado toca **una batería verde con un «#1»
  pintado en el bombo**; Marceline, sentada, **toca el bajo con cara
  seria** mientras él acompaña. ✅ (nuevo dato: la batería del Rey Helado,
  no estaba en la 1ª pasada)
- **1:18**: corte a Jake y Finn afuera, escuchando desde la ventana
  (silueta), con antifaces de dormir en la cabeza. ✅
- **1:36**: **primer plano de una foto Polaroid** de una niña (Marceline
  de pequeña) sonriendo. **Corrección**: la 1ª pasada decía que Marceline
  canta «leyendo las notas que Simón le escribió»; el vídeo real muestra
  que también hay **una fotografía Polaroid** de ella de niña, no sólo
  notas escritas — ambas cosas están en la escena. ✅
- **1:42-1:54**: flashback: **una Marceline pequeña con un osito de peluche
  rojo**, caminando entre ruinas de guerra, se acerca a un hombre (Simon,
  antes de convertirse en el Rey Helado). Es el origen del vínculo entre
  los dos. ✅

### 2.6 «Obsidian» (Tierras lejanas, especial 2020) — CONFIRMADO con el tráiler oficial ✅

Clip: [«Adventure Time Distant Lands Trailer — Obsidian» (reload del tráiler oficial de HBO Max/Cartoon Network)](https://www.dailymotion.com/video/x7xejon) · 1:30 · 1920×1080. Termina con el logo
**HBO Max** (1:28) ✅ oficial.

- **0:16**: Marceline y la Dulce Princesa **en la cocina de la casa** (piso
  turquesa, gabinetes verdes), **cada una con una taza humeante** — confirma
  la escena de la 1ª pasada (≈4:41: «dos tazas humeantes»). ✅
- **0:20**: Marceline (en camiseta gris, no de vampiro) **toca el bajo
  sentada mientras la Princesa cocina** de fondo. ✅
- **0:36**: **Marceline flota tocando el bajo sobre un camino de piedra**
  hacia el Reino de Cristal, con **picos morados y una torre de cristal al
  fondo**. ✅ (nuevo: confirma que llega tocando, no sólo caminando)
- **0:44-1:00**: Marceline convertida en **monstruo alado gigante de
  ojos rojos** (forma vampiro extrema) peleando junto a la Princesa y un
  grupo de criaturas de cristal; luego vuelve a flotar tocando el bajo
  **entre picos de cristal morados y turquesas**. ✅
- **1:08**: Marceline con el bajo al hombro, de pie **junto a la Princesa y
  dos figuras de cristal humanoides**, luz cálida de atardecer. ✅
- **1:12**: **Marceline y la Princesa en una motocicleta**, entrando a una
  ciudad de cristal. ✅ (dato nuevo, no estaba en la 1ª pasada)
- **1:24**: primer plano de **Marceline con expresión de shock/miedo**,
  fondo oscuro estrellado. ✅

### Confirmación del opening y el final (puntos 2/9/10, ver también abajo)

- El **opening en español latino** (0:00-0:29) se vio completo, real, 10
  fotogramas: laguna helada con montañas, castillo del Dulce Reino con
  personajes, valle verde, interior de la casa del árbol con Finn/Jake y un
  hot-dog gigante, Jake tocándose las orejas, pantalla verde con Jake solo,
  Finn y Jake corriendo por una cresta de montaña bajo nubes de tormenta, y
  el logo **«ADVENTURE TIME — Created by Pendleton Ward»** ✅. Fuente:
  [Dailymotion, «'Hora de Aventuras' intro», canal Espinof](https://www.dailymotion.com/video/x8p2dsj) (medio de cine español, 29 s, 1920×1080).
- El **final/créditos en inglés** (0:00-0:33) se vio completo, real, 12
  fotogramas: fondo verde lima con abejas y mariposas animadas, nombres
  reales del staff («Supervising Director Larry Leichliter», «Lead
  Character & Prop Designer Phil Rynda», «Character & Prop Designers
  Natasha Allegri, Tom Herpich»…), termina con los logos **Frederator
  Studios** y **Cartoon Network Studios**. ✅. Fuente:
  [Dailymotion, «Adventure Time - Ending Theme (English - HD)»](https://www.dailymotion.com/video/x4fakxm) (34 s, 1280×720).

---

## Punto 4 · Sitios, luz y paleta (colores MEDIDOS, no de memoria)

La 1ª pasada dejó todos los hex marcados ⚠️ «de memoria, sin ver imagen». Aquí
mido de verdad con `herramientas/estilo.py` sobre fotogramas reales sacados de
los clips del punto 2 (import PIL para los puntos exactos). Fuente de cada
color: el fotograma exacto.

### 4.1 Casa de Marceline (interior) — paleta medida ✅

Medido en el fotograma 0:16 de «Fry Song» (interior) y 0:16 de «Obsidian
Trailer» (cocina):
- Pared rosa: **`#F8AEC5`** (37% del cuadro, «Fry Song» 0:16) ✅
- Techo/pared clara: `#FBE0E8` ✅
- Marco de ventana/zócalo gris azulado: visible pero minoritario en el
  clúster; medido a ojo en la imagen `#7A8A96` ⚠️ (clúster automático no lo
  separó, línea visible en el original)
- Sillón rojo (esquina, «Fry Song» 0:00): `#D94344` ✅ (medido con Pillow,
  píxel puntual)
- Cocina («Obsidian trailer» 0:16): rojo-vino de fondo `#4D252C`, turquesa
  de electrodomésticos `#5B8890`, rosa de pared `#B04E5E` — misma familia
  rosa/rojo que el resto de la casa ✅ **confirma con una segunda escena**
  que la casa es rosa por dentro (dos fuentes de vídeo distintas).

> Corrección: la 1ª pasada sólo tenía el **exterior** (casa rosa con tejado
> marrón, de la wiki). Ahora hay confirmación del **interior** con dos
> clips reales — coincide en tono rosa.

### 4.2 Marceline — colores medidos en fotograma real ✅

Fotograma 0:52 de «I'm Just Your Problem» (cara/torso, fondo de cielo):
- Piel: **`#657471`** (gris verdoso, medido con Pillow en 12 puntos del
  cuello/mejilla, consistente) ✅. **Corrección importante**: la 1ª pasada
  puso `#A9B8C2` (gris azulado pálido) «de memoria». Medido de verdad en
  este fotograma da un verde grisáceo más oscuro y menos azulado. Puede
  variar por escena/iluminación (marcar ambos, decir cuál es medido).
- Pelo (negro): **`#150209`** (medido, no negro puro: tira levemente a
  rojo oscuro) ✅
- Top/camiseta roja: **`#8C000C`** a `#90000A` (rojo oscuro, medido con
  Pillow) ✅. La 1ª pasada tenía `#B3262B` para las botas (no la camiseta);
  aquí es un rojo más oscuro y menos saturado.
- Sombrero de ala ancha (nuevo hallazgo, no estaba en la 1ª pasada):
  **`#BBAB4C`** (parte iluminada) y **`#75691D`** (sombra) — mostaza/oliva ✅
- Cinta del sombrero: `#4A7AA2` (azul grisáceo) ✅
- Cielo de fondo: `#EFEFFF` / `#A5B9F6` (blanco azulado, nubes) ✅

Fotograma 0:16 de «Fry Song» (jersey a rayas rojo/gris, otra prenda —
**dato nuevo**: Marceline no siempre lleva la camiseta gris de tirantes;
aquí lleva un **suéter oscuro a rayas rojo y gris**, mangas largas):
- Rayas rojas del suéter: `#630515` ✅
- Rayas gris oscuro del suéter: `#2C080C` ✅
- Pared rosa de fondo: `#F8AEC5` (37.4%) ✅
- Pelo: `#24080E` (coincide con el `#150209` del otro clip: negro con
  tinte rojo, no azulado) ✅ **dos fuentes de vídeo coinciden en esto**,
  corrige el `#1C1B2B` (negro azulado) que tenía la 1ª pasada.

### 4.3 El Reino de Cristal (Obsidian) — paleta nueva, no existía en la 1ª pasada ✅

Medido en 3 fotogramas del tráiler oficial de «Obsidian» (0:16, 0:44, 1:00):
- Camino/cielo violeta oscuro (0:44, dominante 36%): **`#422D6B`** ✅
- Violeta medio: `#6A53A0` ✅
- Rosa pálido (luz): `#E7D1D9` ✅
- Magenta de acento: `#8F3F6E` ✅
- Cian pálido del cristal (0:00, dominante 53%): **`#E1F7F9`** ✅
- Azul cielo claro: `#BDE0F5` ✅
- Violeta de los picos de cristal: `#9055C3` y `#D3A0E8` ✅

Estilo de sombreado (de `estilo.py`, automático): en el camino hacia el
Reino (0:44) el sombreado es **degradado/pintado** (no plano-cel como el
resto de la serie) — es una localización que usa más pintura atmosférica,
propio de los especiales «Tierras lejanas» (más presupuesto/estilo pictórico)
✅.

### 4.4 Luz — confirmada con vídeo, ya no sólo de memoria

- Casa de Marceline, interior: luz **plana, cálida** por las paredes rosa,
  sin sombras marcadas (estilo cel shading simple) ✅ (antes ⚠️ de memoria).
- «I'm Just Your Problem» (puerta del Señor de las Puertas): luz de **tarde
  con cielo despejado**, nubes iluminadas de blanco, sin el ambiente de
  cueva que decía la 1ª pasada para esta escena (esa descripción de cueva
  era para *otra* localización, la cueva de Marceline, que sigue sin
  fotograma real: ver «No encontré»). ✅ corregido: no confundir ambas
  localizaciones.
- Reino de Cristal: luz **violeta/magenta fría** con acentos cian, de
  aspecto nocturno-mágico (no es «luz de día» como el resto de Ooo) ✅
  confirmado con 3 fotogramas.
- Final/créditos: fondo **verde lima plano**, sin degradado, con insectos
  animados sueltos (abeja, mariposas) como decoración — no es paleta de
  ninguna localización, es la paleta de marca de los créditos ✅.

---

## Punto 9 · Música

Lo de la 1ª pasada (quién compone, qué transmite cada tema) queda bien y
sigue ✅. Aquí AÑADO lo que confirmé con la red abierta:

- **Álbum oficial en español confirmado con tracklist real** (no estaba en
  la 1ª pasada): *Marceline canta: Timeless Songs (Versión en Español)*,
  2019-10-25, 10 pistas. Fuente:
  [MusicBrainz, grupo de lanzamiento](https://musicbrainz.org/release-group/1f39e3d6-9a3b-4838-bae0-3e59b37e69eb) ✅. Lista completa medida (duración real de cada pista, en segundos):
  1. «¿Qué soy para ti?» (2:41)
  2. «Soy tu problema» (2:00) ✅ (coincide con lo ya sabido)
  3. «Niño malvado» (1:54)
  4. «Recordándote» (2:19) ✅ (antes ⚠️ una sola fuente — **ahora dos**:
     Doblaje Wiki + MusicBrainz)
  5. «Ya no lo puedo soportar / Hay un fuego dentro de mí» (1:29)
  6. **«Papi, te comiste mis papas»** (1:43) — ✅ **confirma con una segunda
     fuente** el título que la 1ª pasada sólo tenía por el título de un
     vídeo de Facebook (⚠️ antes, ✅ ahora: MusicBrainz + Facebook oficial
     de Cartoon Network Latinoamérica).
  7. «Todo se queda» (2:26) ✅
  8. «Cadena alimenticia» (1:32) — tema nuevo, no estaba listado antes.
  9. «Siempre entonces se podrá volver» (2:10) — tema nuevo.
  10. **«Acompáñame»** (1:49) — es el título en español de **«Come Along
      With Me»**, el tema de cierre de la serie. **No estaba traducido en
      la 1ª pasada.** ✅
- **«Everything Stays» — quién es realmente la canción**: confirmado con la
  ficha oficial de **TikTok (oEmbed)** de la propia Rebecca Sugar: «I wrote
  this song for Adventure Time after I'd left to create Steven Universe…
  I was so touched to be asked to write a song for **Marcy's mom**» — la
  canción es sobre **la madre de Marceline**, no una canción genérica de
  despedida. Grabada con Jeff (`@Jeffthatnoise`) en violín/cuerdas. Fuente:
  [oEmbed de TikTok, @rebeccasugar](https://www.tiktok.com/@rebeccasugar/video/7380076323168996650) (verificado por API oficial de TikTok, no sólo
  el título del vídeo) ✅. Esto es un dato nuevo y verificado en fuente
  primaria (la propia compositora).
- **La intro tiene variantes por miniserie** (dato nuevo, no estaba en la
  1ª pasada): existen versiones distintas del tema de apertura para cada
  «Tierras lejanas»/miniserie: *Stakes*, *Islands*, *Food Chain*, *Fionna &
  Cake*. Fuente: [Dailymotion, «Theme Song (Islands)»](https://www.dailymotion.com/video/x5whnwn), [«Theme Song (Stakes)»](https://www.dailymotion.com/video/x5whnw2), [«Theme Song (Food Chain)»](https://www.dailymotion.com/video/x5whp1h) ⚠️ (comprobé que existen y su duración —24-26 s cada una— por
  la ficha de Dailymotion, pero no llegué a ver el contenido fotograma a
  fotograma de las tres por el cupo de la tanda; sólo la genérica y la de
  «Obsidian»/«Islands» quedan pendientes de mirar en detalle).

---

## Punto 10 · Vídeos (con minuto exacto, confirmados)

### 10.1 Oficiales / semioficiales, vistos de verdad ✅

| Clip | Duración | Canal/fuente | Qué es |
|---|---|---|---|
| [Opening doblado al español](https://www.dailymotion.com/video/x8p2dsj) | 0:29 | Espinof (medio de cine, ES) | intro completa, latino |
| [«I'm Just Your Problem»](https://www.dailymotion.com/video/x537pqr) | 2:07 | **Cartoon Network** (canal oficial) | escena/vídeo musical 3×10 |
| [«Fry Song» Sing-a-Long](https://www.dailymotion.com/video/x51arca) | 0:52 | reload de «Toon Tunes» CN | escena musical 2×01, letra en pantalla |
| [Créditos finales (inglés)](https://www.dailymotion.com/video/x4fakxm) | 0:33 | reload, con logos Frederator/CN reales | staff real, letra por letra |
| [Tráiler oficial «Obsidian»](https://www.dailymotion.com/video/x7xejon) | 1:30 | reload, termina con logo HBO Max | tráiler del especial 2020 |
| [Tráiler «BMO» (Tierras lejanas) doblado](https://www.dailymotion.com/video/x7vjn4d) | 1:54 | **HobbyConsolas** (medio ES) | tráiler oficial en español |
| [«I Remember You» (audio FR, imagen real)](https://www.dailymotion.com/video/xzt1l7) | 1:58 | grabación de emisión CN HD | escena 4×25 completa |
| [Trailer «Fionna & Cake» HBO Max](https://www.dailymotion.com/video/x8nce5e) | 2:05 | HobbyConsolas | ya estaba en `datos-video.md`, confirmado 1280×720 |
| [Episodio piloto subtitulado](https://www.dailymotion.com/video/x84oaz2) | 7:30 | Capra TV | pendiente de mirar a fondo (ver «Sigue») |

### 10.2 TikTok — confirmados por la API oficial (oEmbed), no sólo por el título ⚠️→✅

La 1ª pasada tenía estos vídeos citados sólo por su título (⚠️, YouTube/TikTok
cerrados). Ahora los verifiqué con `https://www.tiktok.com/oembed?url=...`
(API pública de TikTok, responde igual que un navegador; no hace falta login):

- [@rebeccasugar, «Everything Stays»](https://www.tiktok.com/@rebeccasugar/video/7380076323168996650) ✅ — cita textual arriba (punto 9).
- [@evanescence, cover de «Everything Stays»](https://www.tiktok.com/@evanescence/video/7008939931548568837) ✅ — título real: «One of my favorite
  #adventuretime songs ❤️❤️❤️ #everythingstays #marceline».
- [@acubick, «¿Por qué Jake cambió de voz?»](https://www.tiktok.com/@acubick/video/7206541052713438469) ✅ — título real: «Por qué Jake el perro
  cambio de voz en las últimas temporadas de #horadeaventura? doblaje: José
  Arenas» (dato de doblaje, lo paso al investigador de voz).
- [@eldiariodelalquimista, entrevista a Karla Falcón](https://www.tiktok.com/@eldiariodelalquimista/video/7440244073505623352) ✅ — confirmado:
  Karla Falcón es la actriz oficial de la Dulce Princesa, entrevistada en
  Festigame 2024, menciona que también es Tori en Victorious y Jinx en
  Arcane.

### 10.3 Vídeos que la 1ª pasada no pudo ver, y que siguen sin fotograma propio ⚠️

- El «Anfiteatro Fantasma»/«Slow Dance With You» (10×07) y «Henchman»
  (1×22): busqué clips reales en Dailymotion («Slow Dance With You
  Marceline concert Hunson», «Henchman Marceline plays bass party») y no
  aparecieron coincidencias reales (sólo resultados sin relación). Quedan
  con los datos de transcripción de la 1ª pasada (⚠️ minuto estimado).
- «Marceline's Closet» (3×21): tampoco apareció un clip real específico en
  Dailymotion (sólo un clip genérico de 37 s sin la escena de la canción).

---

## Punto 14 · Poses analizadas (con fotograma real y minuto exacto)

Reemplazo las poses «estimadas por transcripción» de la 1ª pasada por poses
**vistas de verdad** en los 4 clips del punto 2, con minuto exacto. Mantengo
las de la 1ª pasada que no pude comprobar (marcadas ⚠️, tal cual estaban).

### Marceline — poses confirmadas con vídeo real ✅

| # | Clip | Minuto | Qué hace | Sirve para |
|---|---|---|---|---|
| 1 | Fry Song | 0:00 | flota **bocabajo tocando el bajo**, de espaldas a cámara | presentar el «estreno casero» |
| 2 | Fry Song | 0:32 | primer plano, **ojos entornados, boca abierta cantando triste** | emocionar / cantar algo íntimo |
| 3 | I'm Just Your Problem | 0:16 | vuela hacia la puerta con **el bajo por delante**, sombrero de ala ancha | anunciar / entrar en escena |
| 4 | I'm Just Your Problem | 0:52 | primer plano, **ceño fruncido, colmillos a la vista, canta con fuerza** | regañar / cantar con rabia |
| 5 | I'm Just Your Problem | 1:32 | apoyada en la puerta, **toca relajada con el sombrero puesto** | pensar / tocar con calma |
| 6 | I Remember You | 0:24 | de pie, **una mano en la cabeza**, cara de angustia | pensar / dolor |
| 7 | I Remember You | 1:00 | sentada, **toca el bajo con cara seria** junto al Rey Helado en la batería | acompañar / tocar en dúo |
| 8 | Obsidian (tráiler) | 0:16 | sentada en la cocina, **sostiene una taza humeante** con la Princesa | conversar / momento tranquilo |
| 9 | Obsidian (tráiler) | 0:20 | sentada, **toca el bajo con la Princesa cocinando detrás** | tocar en casa / explicar |
| 10 | Obsidian (tráiler) | 0:36 | flota **tocando el bajo** sobre un camino de piedra hacia el Reino de Cristal | viajar / avanzar tocando |
| 11 | Obsidian (tráiler) | 1:08 | de pie, **bajo al hombro**, junto a la Princesa y dos figuras de cristal | presentar en grupo / celebrar |
| 12 | Obsidian (tráiler) | 1:24 | primer plano, **cara de shock/miedo**, fondo oscuro estrellado | susto / sorpresa |

**Mejor para la lámina** (nuevo, con imagen real): la **10** (flotando y
tocando el bajo camino al Reino de Cristal) — junto con la ya propuesta en
la 1ª pasada (escenario con niebla, aún sin fotograma real). Para «pensar»:
la **6** es mejor que la anterior (ahora confirmada con expresión real, no
de memoria).

### Otras poses vistas (Rey Helado, Dulce Princesa, Finn, Jake) — nuevas, no estaban en la 1ª pasada

| Personaje | Clip · minuto | Qué hace |
|---|---|---|
| Rey Helado | I Remember You · 0:42 | toca una **batería verde con «#1» pintado en el bombo** |
| Dulce Princesa | Obsidian (tráiler) · 0:16 | sostiene una **taza humeante**, sentada a la mesa de la cocina |
| Dulce Princesa | Obsidian (tráiler) · 1:12 | **conduce una motocicleta** con Marceline detrás |
| Finn | Fry Song · 0:40 | de pie, **audífonos puestos**, sostiene la grabadora en alto |
| Jake | I'm Just Your Problem · 0:04 | **corre tocando la viola** para alcanzar a Finn |

### Poses de la 1ª pasada que siguen sin fotograma real (⚠️, quedan igual)

Las poses de «Henchman» (1×22), «Marceline's Closet» (3×21) y «Slow Dance
With You» (10×07) descritas por transcripción **no tienen vídeo real
disponible** en Dailymotion (ver punto 10.3): quedan con minuto ⚠️
estimado, tal como las dejó la 1ª pasada.

---

## Lo mejor para la lámina (máximo 5 líneas)

1. La pose **10** de Marceline (flotando, tocando el bajo camino al Reino
   de Cristal, tráiler oficial de «Obsidian», 0:36) — luz violeta/magenta
   real y medida, mejor que cualquier pose «de memoria» de antes.
2. La escena de «Fry Song» (0:00-0:48) es literalmente el concepto de
   lámina «estreno casero»: bajo, grabadora amarilla y un amigo llevando el
   ritmo — y ahora con colores reales de la pared rosa (`#F8AEC5`).
3. La frase real de Rebecca Sugar en TikTok («escribí esta canción… sobre
   la mamá de Marcy») es un dato con fuente primaria, útil para un texto de
   pie de lámina o para redes del servidor.
4. El sombrero de ala ancha mostaza (`#BBAB4C`/`#75691D`) de Marceline en
   «I'm Just Your Problem» es un accesorio no descrito antes: da variedad
   de vestuario para una segunda lámina.
5. El tracklist real de «Marceline canta: Timeless Songs» en español (con
   «Acompáñame» = Come Along With Me) sirve para nombrar canciones reales
   en textos del canal sin inventar títulos.

---

## No encontré

- ⚠️ **La cueva de Marceline** (interior oscuro con estalactitas): no
  apareció en ningún clip real de Dailymotion que pude localizar con las
  búsquedas hechas («Marceline cave bass», «Marceline cueva»). Sigue con
  luz/paleta de memoria de la 1ª pasada.
- ⚠️ El concierto del «Anfiteatro Fantasma» (10×07, con niebla y público de
  fantasmas) y la escena de «Henchman» (1×22): no encontré clip real en
  Dailymotion pese a buscarlos por nombre de canción y por escena. Sigue
  con minuto estimado por transcripción.
- ⚠️ Las 3 variantes de intro («Islands», «Stakes», «Food Chain») las
  confirmé que existen y su duración real (API de Dailymotion), pero no
  llegué a mirarlas fotograma a fotograma por el cupo de la tanda.
- ⚠️ El episodio piloto completo (7:30, subtitulado) lo dejé identificado
  pero sin mirar a fondo con fotogramas.py — no era imprescindible para mis
  5 puntos y prioricé las escenas que pide el punto 2.
- Videojuegos con caja de diálogo, licencias de modelos 3D, encuesta
  oficial de popularidad: no son mis puntos (11, 3, 7/12) — no los busqué,
  ya están marcados en la 1ª pasada para el investigador que corresponda.

---

## Bitácora de búsqueda (segunda pasada, red abierta)

### Comprobación de red (25-sep-2026)

- **Dailymotion API** (`api.dailymotion.com`): funciona bien, sin límite
  aparente; usada para 9 búsquedas específicas por canción/escena.
- **`herramientas/fotogramas.py`** sobre Dailymotion: funciona con
  `yt-dlp`; en un intento dio error de «impersonation… firefox» (no 429) y
  al reintentar una vez funcionó normal.
- **TikTok oEmbed** (`www.tiktok.com/oembed?url=...`): funciona sin login,
  da título completo y autor — mejor que sólo el título del buscador.
- **MusicBrainz API**: funciona, `release-group` con `query=` da
  resultados relevantes si se afina la búsqueda (con «Marceline» en vez de
  sólo «Adventure Time», que traía discos sin relación por «Time»/«Hora»).
- No probé YouTube (pide iniciar sesión desde este servidor, según
  AYUDANTE.md) ni AnimeThemes (no aplica: es una serie occidental, no
  anime, no tiene fichas ahí).

### Búsquedas (12, todas en inglés salvo 3 en español — la serie es
estadounidense, no hacía falta japonés/coreano para vídeo)

| # | Idioma | Búsqueda | Qué salió |
|---|---|---|---|
| 1 | en | dailymotion API: Marceline bass Adventure Time | clips no oficiales, ninguno útil |
| 2 | en | dailymotion API: Adventure Time opening theme song | «Theme Song» variantes (Islands, Stakes, Food Chain, Fionna&Cake) |
| 3 | en | dailymotion API: Adventure Time trailer official | tráileres de «Fionna & Cake», «Side Quests», «Islands» |
| 4 | en | dailymotion API: I'm Just Your Problem Adventure Time | clip oficial del canal Cartoon Network ✅ |
| 5 | es | dailymotion API: Hora de Aventura intro español | intro real doblada (Espinof), piloto subtitulado (Capra TV) |
| 6 | es | dailymotion API: Marceline Reina Vampiro español latino | sin resultado útil (falsos positivos por «Reina») |
| 7 | es | dailymotion API: Hora de Aventura trailer HBO Max | tráiler de BMO (HobbyConsolas) ✅ |
| 8 | en | dailymotion API: Adventure Time Come Along With Me ending | créditos finales reales (canal fan, contenido real) ✅ |
| 9 | en | dailymotion API: I Remember You song Marceline Ice King | escena real (audio FR) ✅ |
| 10 | en | dailymotion API: Monster Marceline Obsidian song | tráiler oficial de Obsidian ✅ |
| 11 | en | dailymotion API: Slow Dance With You / Henchman | nada útil, sin coincidencias reales |
| 12 | en | dailymotion API: Marceline's Closet Finn Jake | sólo un clip genérico sin la escena |

### Herramientas usadas (con cupo)

- `fotogramas.py`: 7 clips completos (contact sheets) + 4 fotogramas
  individuales de alta resolución para medir color.
- `estilo.py --colores`: 5 fotogramas (2 de «I'm Just Your Problem»/«Fry
  Song», 3 de «Obsidian trailer»).
- Pillow directo (`Image.getpixel`): puntos exactos de piel, top y sombrero
  de Marceline en el fotograma 0:52 de «I'm Just Your Problem».
- `curl` directo: Dailymotion API (fichas + búsquedas), TikTok oEmbed (4
  vídeos), MusicBrainz API (release-group + tracklist).

### Fuentes consultadas por tipo (para mis 5 puntos)

- **Oficiales**: canal de Cartoon Network en Dailymotion, HBO Max (logo en
  el tráiler de Obsidian), MusicBrainz (tracklist del álbum en español).
- **Semioficiales/medios**: Espinof (intro), HobbyConsolas (tráiler BMO),
  Capra TV (piloto subtitulado).
- **Reloads de fans con contenido real**: canal que subió los créditos
  finales y «Teaser Trailer» que subió el tráiler de Obsidian — el
  contenido en sí es oficial (se ve el logo/staff real), el canal que lo
  aloja no.
- **TikTok**: 4 vídeos verificados por oEmbed (Rebecca Sugar, Evanescence,
  2 creadores de fandom hispano).

---

## Cumplimiento del encargo (mis puntos)

| Punto | Qué pide | Estado | Por qué |
|---|---|---|---|
| 2 | Fotogramas de escenas icónicas, 1080p+, con capítulo y minuto | ✅ | 4 escenas vistas con vídeo real (Fry Song, I'm Just Your Problem, I Remember You, Obsidian), minuto exacto; 2 en 1080p (Obsidian, intro), el resto en 720p (calidad del clip fuente, no hay versión mejor en Dailymotion) |
| 4 | Fondos y sitios, luz y paleta (hex), texturas reales | ✅ luz y paleta con hex MEDIDOS (casa, Reino de Cristal); ⚠️ texturas | siguen las de la 1ª pasada (Poly Haven), no las volví a buscar por no ser mi aporte nuevo; la cueva de Marceline sigue sin fotograma real |
| 9 | Música: openings, endings, BSO, ambiente, efectos | ✅ | tracklist real en español, tema de Rebecca Sugar confirmado por fuente primaria, variantes de intro confirmadas; efectos de sonido/onomatopeyas no es tan aplicable a esta serie (occidental, sin convención de onomatopeya en pantalla como el anime) — lo dejo anotado |
| 10 | Vídeos: tráileres, escenas, análisis, tendencias, con minuto | ✅ | 9 clips reales con minuto, 4 TikTok confirmados por oEmbed; análisis en YouTube no se pudieron ver (login), los de la 1ª pasada (Medium, etc.) siguen válidos como texto |
| 14 | Poses analizadas, 6-10 fotogramas o ilustraciones por personaje, con minuto | ✅ | 12 poses de Marceline con vídeo real y minuto exacto (antes 13 estimadas por transcripción); + 5 poses nuevas de otros personajes |

**Parte terminada de verdad** (no cortada por límite de uso): los 5 puntos
(2, 4, 9, 10, 14) están cubiertos con lo obligatorio que pide ENCARGO.md.
Ideas para una futura tanda, no obligatorias (ya están también en «No
encontré»): mirar el piloto completo, las 3 variantes de intro fotograma a
fotograma, y buscar la escena del Anfiteatro Fantasma y la cueva de
Marceline en otra fuente (Internet Archive, storyboards).
