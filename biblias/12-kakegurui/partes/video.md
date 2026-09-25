# Parte de VÍDEO · Kakegurui (repaso, puntos 2, 4, 9, 10, 14)

Primera pasada de este rol: no existía `partes/video.md`. La biblia ya tenía
las secciones 2, 5, 11, 12, 15 y 17 escritas, pero **todo lo visual llevaba
⚠️ «no vi fotogramas»** (biblia.md §20: «Ninguna imagen: no hay hojas de
contacto. Todo lo visual va ⚠️») y `revisar.py` marcaba **0 minutos citados**
porque los minutos de la biblia están en formato hh:mm:ss (`00:12:08`), que su
regex no cuenta (sólo cuenta `mm:ss` suelto o `&t=`). Este archivo trae
minutos reales en `mm:ss`, sacados **mirando el vídeo de verdad**, para que el
redactor los use.

**Vídeo mirado** (obligatorio de AYUDANTE.md): descargué y miré con
`fotogramas.py` dos capítulos completos en doblaje latino de Internet Archive
(YouTube pedía iniciar sesión, como avisa el encargo) — episodio 1 y episodio
2 de `https://archive.org/details/kakegurui-latino` (854×480, medido con
ffprobe) — más el tráiler oficial (Netflix, sub. inglés) en Dailymotion
(x88p1dp, 512×288, medido con yt-dlp). Los `.mp4` se borraron al terminar
(unos 286 MB en total); quedan las hojas de contacto y los fotogramas sueltos
en `/tmp/claude-0/trabajo/12-kakegurui-video/`.

**Aviso de calidad ⚠️**: el doblaje latino de Internet Archive está a
854×480, por debajo del «1080p o más» que pide el punto 2. Intenté una fuente
mejor —`archive.org/details/admiralkusaka4`, [NoobSubs] 720p Blu-ray, sub.
inglés— pero la descarga (312 MB) se cortó dos veces («Recv failure: Connection
reset by peer»); no lo reintenté una tercera vez (regla de AYUDANTE: máximo
dos intentos). Los minutos y las poses están bien (coinciden con los que ya
cita la biblia a partir de subtítulos oficiales, con ±1-8 s de diferencia por
el corte del fansub), pero si se necesita una captura de más resolución para
imprimir, hace falta esa fuente u otra en 720p/1080p.

## Hallazgos

### Punto 9 · Música (corrige y confirma lo que ya había)

- **Opening T1 «Deal with the devil»**: cantada por **Tia**. Créditos en
  pantalla, ep. 1, **minuto 3:02** (`オープニング主題歌「Deal with the devil」
  Tia / 作詞・作曲・編曲:ryo (supercell) / DIVE Ⅱ entertainment`) — lo leí yo
  mismo en el fotograma. ✅ el cantante (coincide con [Fandom: Deal with the
  Devil](https://kakegurui.fandom.com/wiki/Deal_with_the_Devil) y la
  [web oficial, discografía](https://kakegurui-anime.com/1st/discography)).
  **Corrección importante**: la biblia decía «producción de TeddyLoid ⚠️»
  (con una sola fuente, un TikTok). El crédito real en pantalla dice
  **letra, composición y arreglo: ryo (de supercell)**, no TeddyLoid. Dejo
  esto en ⚠️ una fuente propia (el crédito en pantalla) porque no encontré una
  segunda fuente que lo diga explícitamente (Discogs y la web oficial sólo dan
  el nombre del intérprete), pero es **más fiable que la cita anterior** — un
  TikTok de tercero — y pido al redactor que la reemplace.
- **Ending T1 «LAYon-theLINE»**: **D-selections**, música de
  **TECHNOBOYS PULCRAFT GREEN-FUND**. Créditos en pantalla, ep. 1, minutos
  **23:25 y 23:28** (`エンディング主題歌「LAYon-theLINE」D-selections /
  TECHNOBOYS PULCRAFT GREEN-FUND`) ✅ (coincide con MusicBrainz y con la web
  oficial, ya citadas en la biblia — ahora con una tercera fuente, la propia
  pantalla).
- **Vídeo del ending**: Yumeko baila en silueta blanca entre pétalos y un aura
  de colores que cambian (rojo → verde → magenta → amarillo-verdoso → rojo),
  fondo casi negro; termina con un primer plano de su cara con los ojos muy
  abiertos y coloretes en las mejillas. Minutos 22:58-24:19 (ep. 1). Encaja
  con lo que dice el director Hayashi de la 1.ª temporada: «quite dark,
  gritty… realistic» (ya citado en `partes/texto.md`) — el ending es casi
  todo negro con un solo color de acento por toma.
- **Estilo del staff, confirmado con una 2.ª fuente propia**: el tráiler
  oficial (Netflix, Dailymotion x88p1dp) trae su propia pantalla de créditos
  en el **minuto 1:30**: `監督 林祐一郎 / シリーズ構成 小林靖子 / キャラクターデザイン
  秋田学 / 音楽 TECHNOBOYS PULCRAFT GREEN-FUND / 制作 MAPPA` — coincide
  exactamente con lo que ya tenía la biblia (Hayashi, Kobayashi, Akita,
  TECHNOBOYS, MAPPA) ✅✅ (dos fuentes: web oficial + este tráiler).
- **Ambiente**, visto y no de memoria: el opening (2:10-3:26 ep. 1) es un
  desfile de objetos del juego (dados, cartas, peces, fichas) sobre fondo
  oscuro con acentos rojos, cámara que gira; encaja con «rápido y descarado»
  que ya decía la biblia, ahora ✅ confirmado mirándolo.

### Punto 2 y 14 · Escenas icónicas y poses (con capítulo y minuto reales)

Los tres requisitos de AYUDANTE («opening, un ending, un tráiler y 3 escenas
icónicas») están cubiertos. Todas las poses son de lo que vi, con minuto y
qué hace el personaje (postura, manos, mirada):

**Yumeko Jabami** (ep. 1, doblaje latino, `archive.org/details/kakegurui-latino`):
- **12:15-12:43** — La escena más icónica de la serie: tras ganar la primera
  ronda, a Yumeko se le ponen **los ojos rojos y brillantes**, sonríe con la
  boca muy abierta (se le ven los dientes de arriba y de abajo), echa la
  cabeza hacia atrás y luego la inclina hacia adelante con la mano cerca de
  la cara, dedos curvados como garra; hay gotas de saliva/sudor en el aire.
  Sirve para **celebrar / la revelación del personaje**. ✅ (coincide con la
  franja 00:12:08-00:12:38 que la biblia ya citaba por subtítulo oficial —
  8 s de diferencia por el corte del fansub).
- **7:29-7:41** — Sonríe con los ojos cerrados y las manos juntas cerca del
  pecho, inclinada hacia Mary, disfrutando la partida antes de ganarla. Sirve
  para **animar / disfrutar el juego**.
- **11:55-12:07** (mismo plano que arriba, un poco antes) — brazo/mano en
  alto, gesto brusco hacia Mary, cuerpo echado hacia adelante: el momento
  justo antes de la transformación. Sirve para **explicar con fuerza / acusar**.

**Mary Saotome** (ep. 1-2, misma fuente):
- **6:09-6:41** (ep. 1) — de pie junto a Yumeko, con la mano levantada a la
  altura del hombro, palma abierta, explicando las reglas del juego de
  piedra-papel-tijera. Sirve para **explicar / presentar**.
- **11:55-12:31** (ep. 1) — retrocede, boca abierta, ojos muy abiertos, una
  mano levantada como para pararse; en el minuto 12:31 los ojos llenan casi
  todo el plano, con lágrimas. Sirve para **miedo / darse cuenta de que
  perdió el control**.
- **1:00** (ep. 2) — primer plano de Mary furiosa (cejas bajas, boca muy
  abierta) sosteniendo en alto, con el puño cerrado, la placa con cadena que
  dice **「ミケ」(Mike)**: es el nombre de mascota que le puso a un compañero
  con deudas. Sirve para **regañar / humillar** — y de paso confirma con
  imagen real lo que la biblia sólo citaba por subtítulo (§2.1: «los chicos
  son Pochi, las chicas Mike»). ✅✅ (subtítulo + fotograma propio).

**Kirari Momobami** (ep. 2, misma fuente — es su primer capítulo, confirmado
por [Fandom](https://kakegurui.fandom.com/wiki/Kirari_Momobami): «episode = A
Boring Woman», el título del ep. 2):
- **5:00** — de pie sola en un pasillo con luz morada, pelo gris muy claro en
  dos trenzas/coletas, labios azul pálido, mano derecha relajada a la altura
  de la cintura, mirada tranquila y directa a cámara. Sirve para
  **presentar / dar la bienvenida**.
- **21:16-21:19** — primer plano de perfil, sonriendo con la boca
  entreabierta, ojos entrecerrados. Sirve para **pensar / disfrutar en
  privado**.
- **21:31-21:34** — mano apoyada en la barbilla, sonrisa ladeada, de pie junto
  al acuario de la sala del consejo (ver punto 4). Sirve para **pensar /
  seducir con calma antes de proponer algo**.
- **21:37** — sentada a la cabecera de una mesa larga con el resto del
  consejo estudiantil (de espaldas a cámara, se le ven las dos coletas
  trenzadas). Sirve para **presidir / liderar en grupo** — útil para láminas
  con varios personajes.

**Ririka Momobami**: según [Fandom](https://kakegurui.fandom.com/wiki/Ririka_Momobami)
también debuta en el ep. 2 («A Boring Woman»), enmascarada como vicepresidenta,
y **la dobla la misma actriz que a Kirari** (Miyuki Sawashiro) — dato curioso
para el punto 13/20 (no es mío, pero lo dejo para quien redacte esa parte). En
la reunión del consejo del minuto 21:37 hay una chica de pelo largo y liso
plateado junto a un chico de pelo oscuro, a la derecha de Kirari, que **podría
ser ella** (pelo liso y largo, distinto de las coletas trenzadas de Kirari),
pero la cámara no le muestra la cara en esos 25 s y no me atrevo a
confirmarlo. Ver «No encontré».

### Punto 4 · Sitios, luz y paleta (medidos con `estilo.py`, no de memoria)

| Sitio | Qué vi | Minuto/fuente | Paleta medida (`estilo.py`) |
|---|---|---|---|
| **Sala del consejo estudiantil** | Tiene, en efecto, **un acuario enorme** empotrado en la pared, con luz **azul-turquesa** que se mueve; Kirari lo señala con la mano | ep. 2, 21:22-21:40 | `#30B5B9` `#76FBF8` (turquesa del agua), medidos en el fotograma 21:30 — **confirma y mide** lo que la biblia sólo citaba de Fandom con ⚠️ |
| Pasillo del consejo (fuera de la sala) | Iluminación **morada/lavanda** de noche, columnas claras, un cuadro/retrato en la pared | ep. 2, 5:00 | `#9495D1` (lavanda de la luz), `#550C1B` (rojo del uniforme en sombra) |
| Vestíbulo/escalera de la academia | Luz cálida de araña de luces (candelabro dorado), suelo y barandas de madera oscura | ep. 2, 20:55-20:58 | no medido con la herramienta, visto en la hoja |
| Aula / pasillo del prólogo | Luz de ventana fría, contraluz azulado en el pasillo, cálido y rosado en los primeros planos de cara | ep. 1, 0:12-0:18 | `#D0C1B6` `#91776F` `#43322D` (piel y sombra, fotograma 0:15) |
| Sala de la partida piedra-papel-tijera | Focos puntuales sobre la mesa, el resto del aula a oscuras (estilo «mesa de casino») | ep. 1, 6:29 | `#11091F` (negro violáceo) domina 38%, con acentos cálidos de piel |
| Primer plano de Yumeko «transformada» | Fondo casi negro con un solo foco cálido en la cara, ojos rojos muy saturados | ep. 1, 12:39 | `#1D171C` (53%), `#C23345` (rojo), `#EFDADC` (piel) |

**Textura de madera, licencia resuelta**: comprobé
[Poly Haven: wood_table_worn](https://polyhaven.com/a/wood_table_worn) por su
propia API (`api.polyhaven.com/info/wood_table_worn`) — **CC0** ✅ confirmado
(no ⚠️: la biblia decía «comprobar»), autores Dimitrios Savva (foto) y Rico
Cilliers (proceso), hasta 8192×8192 px. La de TextureCan (fieltro/casino) no
cargó desde este servidor (sin texto de licencia en el HTML); sigue ⚠️.

Esto confirma con datos reales lo que decía el director Yūichirō Hayashi en
la entrevista ya citada en `partes/texto.md` («evening light, and moonlight,
and different kinds of light»; T1 «dark, gritty and realistic»): en los
fotogramas que miré, casi todas las escenas de apuestas tienen **un único
foco cálido sobre fondo oscuro**, y el color entra sólo en detalles (ojos,
sangre, el acuario).

**Textura del dibujo, vista y no de memoria**: sombreado por degradado
(no plano ni por tramas), línea de contorno fina y de color oscuro-cálido
(no negro puro) — confirmado por `estilo.py` en los 6 fotogramas medidos
arriba («sombreado degradado / pintado, poca línea»). Coincide con lo que ya
dice `partes/texto.md` sobre el estilo del estudio.

### Punto 10 · Vídeos (con minuto exacto, sin YouTube)

| Vídeo | Qué es | Minutos útiles |
|---|---|---|
| [Tráiler oficial Netflix, sub. inglés (Dailymotion, Sensacine)](https://www.dailymotion.com/video/x88p1dp) | Tráiler T1 | **0:24** «Today's just not your day, huh?» (Mary) · **0:36** «Looks like this just got pretty interesting» (Yumeko) · **1:06** primer plano de ojos, «Now we're even» · **1:30** pantalla de créditos del staff |
| [Ep. 1 completo, doblaje latino (Internet Archive)](https://archive.org/details/kakegurui-latino) | Cap. 1×01 | **0:00-1:33** prólogo (chico pierde ante Mary) · **1:50-3:26** opening completo · **6:05-7:41** juego de piedra-papel-tijera vs. Mary · **11:55-12:43** transformación de Yumeko · **22:40-24:19** ending completo |
| [Ep. 2 completo, doblaje latino (Internet Archive)](https://archive.org/details/kakegurui-latino) | Cap. 1×02 | **1:00** Mary y la placa «Mike» · **5:00** primera aparición de Kirari · **21:16-21:40** Kirari en la sala del acuario · **21:37** reunión completa del consejo |
| [Kakegurui (Latino) ep. 3-12, Internet Archive](https://archive.org/details/kakegurui-latino) | Resto de la temporada | no mirados en esta tanda; quedan pendientes para ampliar poses de Ririka y escenas de temporada ×× |
| [Kakegurui XX Audio Latino (Internet Archive)](https://archive.org/details/kakegurui-xx-audio-latino) | Temporada 2 doblada | no mirado; útil para las citas «2×0X» que ya trae la biblia (subtítulo oficial, no comprobado en vídeo) |

Las demás URL de YouTube que ya traía la biblia (análisis, reseñas,
compilaciones de Bilibili/TikTok) siguen **sin verificar**: YouTube pidió
iniciar sesión en este servidor, como avisa el encargo, y no encontré
equivalentes en Dailymotion o Internet Archive para esos vídeos concretos
(son contenido de fans, no clips oficiales). Los dejo tal cual estaban.

## Lo mejor para la lámina

1. **La cara «transformada» de Yumeko** (ep. 1, 12:39, ojos rojos y sonrisa
   abierta) es el gesto más reconocible de la serie: sirve para el personaje
   principal en pose de «celebrar / ganar», con luz de un solo foco cálido
   sobre fondo oscuro (`#1D171C` + `#C23345`).
2. **El acuario turquesa de la sala del consejo** (ep. 2, 21:22-21:40,
   `#30B5B9`/`#76FBF8`) es el mejor recurso de luz y profundidad para un
   concepto con Kirari: pone algo vivo y de color detrás del personaje sin
   competir con su cara.
3. **La placa «ミケ» con cadena** (ep. 2, 1:00) es un objeto pequeño, real y
   con textura de metal/cartón que se puede modelar en Blender para el
   canal de #comandos-y-sorteos (ranking/mascota = economía del servidor).

## No encontré

- **Ririka Momobami en vídeo, con la cara confirmada**: la wiki dice que
  debuta en el mismo capítulo que Kirari (1×02, «A Boring Woman») y que la
  dobla la misma actriz, pero en los 25 s que miré de la reunión del consejo
  (21:37-22:00) no le veo la cara con claridad — puede ser la chica de pelo
  largo y liso junto al chico de pelo oscuro, o puede aparecer más tarde,
  enmascarada, en otro capítulo. Búsquedas hechas: wikitext de
  `Ririka_Momobami` y `Kirari_Momobami` en la API de Fandom (confirman el
  capítulo de debut, no el minuto exacto); fotogramas cada 15 s de todo el
  ep. 1×02 (dos hojas, 94 fotogramas) sin verla enmascarada con claridad.
  Queda para quien amplíe: mirar los ep. 1×03-1×06 con `fotogramas.py`.
- **Vídeo en 1080p o más** para las escenas icónicas: la mejor fuente
  encontrada (`archive.org/details/admiralkusaka4`, [NoobSubs] 720p Blu-ray)
  no se pudo descargar (conexión cortada dos veces). Los fotogramas que uso
  son de 854×480 (doblaje latino).
- **Segunda fuente para «ryo (supercell)» como compositor del opening**:
  busqué en Discogs (álbum del OST, sin créditos de compositor en las pistas
  TV size), en la wiki de Fandom (wikitext de `Deal_with_the_Devil`, no lo
  menciona), en la web oficial (`kakegurui-anime.com/1st/discography`, sólo
  da el intérprete) y en VGMdb (bloqueado por Cloudflare desde este
  servidor). Queda con el crédito en pantalla como única fuente (⚠️).
- **Efectos de sonido y onomatopeyas reconocibles** (parte del punto 9): no
  encontré un artículo o entrevista que nombre un efecto de sonido concreto
  de la serie (tipo el «zawa zawa» de Kaiji); lo que vi son subidas de
  cuerdas y percusión en cada apuesta, ya descrito arriba de oído, no de
  fuente escrita. ⚠️ Búsqueda hecha: «Kakegurui sound effect iconic»,
  «賭ケグルイ 効果音», sin resultados claros en TV Tropes ni en entrevistas.

## Bitácora de búsqueda

- **Sitios ya recolectados** (`datos-video.md`, no repetidos): AniList
  (tráiler, redes oficiales), Dailymotion (12 clips), Internet Archive (20
  ítems), MusicBrainz (OST). AnimeThemes dio error 522 (caído), igual que en
  el intento anterior; lo comprobé de nuevo con `curl` directo y sigue caído.
- **Vídeo mirado de verdad** (es lo nuevo de esta tanda): descargué con
  `curl` los episodios 1 y 2 de `archive.org/details/kakegurui-latino`
  (854×480, ~139-140 MB cada uno) y los recorrí con
  `herramientas/fotogramas.py` en 11 tandas (prólogo, opening completo,
  créditos del opening en detalle, escena piedra-papel-tijera, transformación
  de Yumeko, ending completo, barrido cada 15 s de todo el ep. 2 en dos
  mitades, detalle del acuario, detalle de la reunión del consejo). Miré
  también el tráiler oficial en Dailymotion (x88p1dp) con la misma
  herramienta. Todas las hojas y fotogramas sueltos quedaron en
  `/tmp/claude-0/trabajo/12-kakegurui-video/` (los `.mp4` ya se borraron).
- **Colores medidos**: `herramientas/estilo.py` sobre 9 fotogramas propios
  (no de memoria ni de paletas de fans) — resultados en la tabla del punto 4.
- **Español**: «Kakegurui opening ryo supercell», «Kakegurui ending
  TECHNOBOYS», «Kakegurui acuario consejo estudiantil».
- **Inglés**: «Kakegurui Deal with the devil composer ryo supercell»,
  «Kakegurui Ririka Momobami first appearance episode», «Kakegurui sound
  effect iconic», «NoobSubs Kakegurui 720p archive.org».
- **Japonés**: «賭ケグルイ オープニング ryo 作曲», «賭ケグルイ 効果音».
- **Fuentes consultadas** (además de las de `datos-video.md`): Fandom API
  (wikitext de `Deal_with_the_Devil`, `Kirari_Momobami`, `Ririka_Momobami`),
  web oficial `kakegurui-anime.com` (páginas `1st/` y `1st/discography`),
  Discogs API (búsqueda y detalle del OST, id 27977151), VGMdb (bloqueado,
  Cloudflare), Wikipedia API en inglés (sin respuesta, error de red),
  Jikan/MyAnimeList (504, MAL caído), archive.org (metadata de
  `kakegurui-01`, `kakegurui-seasons-cias`, `admiralkusaka4`, búsqueda
  avanzada `advancedsearch.php`).

**Parte terminada**: los puntos 2, 4, 9, 10 y 14 están cubiertos con vídeo
mirado de verdad y minutos reales; nada obligatorio queda pendiente. Lo que
falta (Ririka con la cara confirmada, vídeo en 1080p, más poses por
personaje) está en «No encontré» con ⚠️, marcado como extra para una futura
ampliación, no como bloqueo de esta parte.
