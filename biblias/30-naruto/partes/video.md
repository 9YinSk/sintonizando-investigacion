# Vídeo · Naruto (repaso) · puntos 2, 4, 9, 10 y 14 de ENCARGO.md

Repaso sobre una biblia ya escrita y con la red abierta. No repito lo que ya
estaba bien en `biblia.md` (secciones 2, 5, 11, 12, 15): sólo **compruebo
mirando los fotogramas de verdad** (`herramientas/fotogramas.py` sobre los
episodios completos de Internet Archive, en vez de «de memoria»), añado lo
que faltaba (tendencias de TikTok, segundas fuentes de música) y corrijo lo
que el fotograma desmiente.

**Cómo miré**: descargué episodios completos y sub-clips con
`herramientas/fotogramas.py` desde `archive.org/download/naruto-completo/…`
(serie original, doblaje latino, numeración N001-N220 = archivo `Naruto -
0NN.mp4`) y `archive.org/download/naruto-shippuden-lat/…` (Shippuden,
numeración S001-S441 = archivo `Naruto Shippuden Lat NN.mp4`; **sólo llega
hasta el episodio 441**, así que S476-478 del Valle del Fin no se pudo
verificar así). Enlaces con `?t=segundos` para saltar directo al fotograma.

## Hallazgos por punto

### Punto 2 · Escenas icónicas (miradas de verdad)

- Confirmado con fotograma ✅ · N005, 00:19:54 «¡Aprobados!»: el plano real
  muestra a **Naruto todavía atado al tocón, riendo**, con Kakashi y Sakura
  saltando detrás y **un cielo nocturno morado con nubes**, no la escena de
  felicitación cara a cara que sugería la descripción anterior · [fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20005.mp4?t=1194) (1280×966) · ✅ (visto + subtítulo ya citado en biblia.md §2.1)
- Corrección de luz ✅ · el reto de los cascabeles **no termina con «sol alto,
  sombras duras»**: el fotograma del cierre (19:54) es de **noche, cielo
  morado tormentoso**; sólo el arranque (5 de la mañana) y la escena del
  golpe al tronco son de día. La sección 5.2 de la biblia mezcla ambos
  momentos → corregir «Luz» de ese sitio a «de madrugada a mediodía en el
  reto; de noche en la resolución» · [fotograma 19:54](https://archive.org/download/naruto-completo/Naruto%20-%20005.mp4?t=1194) ✅
- Confirmado ✅ · N005, 00:16:07, Kakashi ante la piedra de los caídos: **de
  espaldas, mano en el bolsillo**, tal como decía la biblia, con luz de
  atardecer anaranjada colándose entre los árboles (no gris) · [fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20005.mp4?t=967) ✅
- Corrección de pose ✅ · N025 (examen chūnin, «acepto la pregunta»): el
  fotograma real (10:45-10:54) muestra a **Naruto sentado en su pupitre,
  alzando el brazo con el puño cerrado, sudando, ceño fruncido**, NO
  «golpea la mesa y se levanta» como decía la biblia § 15 · [fotograma 10:48](https://archive.org/download/naruto-completo/Naruto%20-%20025.mp4?t=648) ✅ · minuto exacto revisado: 00:10:45-00:10:54 (antes decía 00:10:55, un segundo de diferencia, correcto)
- Confirmado ✅ · N086, 00:20:15, Jiraiya explicando el globo de agua:
  primer plano de su cara con el rasguño rojo, bosque detrás — coincide con
  la ficha de la biblia · [fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20086.mp4?t=1215) ✅
- Nuevo ✅ · Naruto graduándose (N001, 00:20:41): el fotograma exacto es un
  **primer plano de la banda ninja ya puesta**, cámara muy cerrada (no se ve
  a Iruka en ese fotograma exacto; el gesto de atarla es un segundo antes) ·
  [fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20001.mp4?t=1241) ✅

### Punto 4 · Sitios, luz y paleta (medida en fotogramas de verdad)

- Corregido ✅ · **capa de Akatsuki**: medí el color real en un fotograma
  (Hidan, N086/Shippuden ep. 86, 00:15:00) con Pillow (mediana 6×6 px):
  tela `#2A2B33` (**azul-negro muy oscuro, no negro puro**) y el interior de
  la nube roja `#431C29` a `#491B28` (**granate muy oscuro**, la escena es
  de noche/bosque en penumbra, así que el rojo se ve casi vino) — sustituye
  al `#1A1A1F` / `#C0282E` «de memoria» de la biblia § 5.3 · [fotograma](https://archive.org/download/naruto-shippuden-lat/Naruto%20shippuden%20Lat%2086.mp4?t=900) (1280×720) ✅ (medido por mí; ⚠️ la luz de esa escena es tenue, en luz de día el rojo será más vivo — dejar como aproximación)
- Sakura, vestido rojo ✅ · en el fotograma de N005 (16:07) se ve completo:
  medido `#9C2A38` (rojo cereza oscuro), más cercano al `#C8283C` que ya
  tenía la biblia (diferencia de matiz por la luz de atardecer de esa toma) ·
  [fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20005.mp4?t=967) ✅ medido por mí
- Confirmado ⚠️→⚠️ (sigue con una fuente, pero ahora con cita directa) ·
  Konoha inspirada en el pueblo natal de Kishimoto (Nagi, Okayama): sólo
  ScreenRant lo dice explícitamente; no encontré una segunda fuente (busqué
  en japonés «岸本斉史 出身 ナルト 木ノ葉隠れ 元ネタ» sin resultado directo) ⚠️

### Punto 9 · Música

- Resuelto a ✅ · **«Sadness and Sorrow» (Ai to Hi)**: la pieza mezcla
  **shakuhachi y shamisen japoneses con piano y violín occidentales**; la
  compuso Yasuharu Takanashi en su debut (2 horas la primera vez, luego la
  retocó), aunque el crédito en streaming suele decir Toshio Masuda · [Japan Nakama](https://www.japannakama.co.uk/creativity/music/who-composed-sadness-and-sorrow-naruto/) · [Wikipedia](https://en.wikipedia.org/wiki/Yasuharu_Takanashi) · ✅ (dos fuentes)
- Nuevo ✅ · **instrumentación real confirmada por tema**: «Sasuke's Theme»
  usa **bajo, taiko, shakuhachi, platillos, claves, guitarra eléctrica con
  ecualizador y cascabeles** (ficha de Narutopedia en español) · [Narutopedia ES](https://naruto.fandom.com/es/wiki/Sasuke's_Theme) · [Anexo Wikipedia ES](https://es.wikipedia.org/wiki/Anexo:Banda_sonora_de_Naruto) · ✅ (dos fuentes) — sustituye al «de memoria» de la biblia § 11.2
- Nuevo ✅ · **estilo general**: Takanashi usa más orquesta, coros e
  instrumentos japoneses tradicionales; Masuda prefería sintetizadores y
  electrónica en vez de orquesta — diferencia entre los dos compositores,
  útil para saber qué "sonido" pega a cada arco · [dodmagazine.es](https://www.dodmagazine.es/bandas-sonoras-naruto/) ⚠️ (una fuente, blog especializado)
- Confirmado con fuente directa ⚠️ (sigue con una) · **«Jiraiya no Theme»
  (Jiraiya's Theme)** SÍ es un título real del álbum (2:43 min, en el
  Anexo de la Wikipedia en español) — ya no es "de memoria", pero no lo
  encontré en el release de MusicBrainz vol. I que ya tenía `datos-video.md`
  (comprobé sus 21 pistas por la API; no aparece ahí, estará en el vol. II
  o III) · [Anexo Wikipedia ES](https://es.wikipedia.org/wiki/Anexo:Banda_sonora_de_Naruto) ⚠️
- Nuevo ✅ · **el opening «Rise» en Latinoamérica SÍ se emitió cantado (en
  inglés)**, igual que en EE. UU.; la versión instrumental de esa misma
  canción se usó como ending en la versión estadounidense, y Latinoamérica
  la heredó igual (Cartoon Network LatAm estrenó Naruto el 1-ene-2007) ·
  [búsqueda con dos coincidencias: Wikipedia (season 2) + Doblaje Wiki] ✅

### Punto 10 · Vídeos y tendencias (con minuto)

- **Opening mirado con fotogramas.py** ✅ · clip de Dailymotion etiquetado
  «Naruto Shippuden Opening» (subido por FILMSTARTS, 1:32): a 0:08 las
  siluetas del equipo 7 antes del amanecer; a **0:16 aparece el logo
  «NARUTO -ナルト-»** en naranja/rosa; a 0:24 Sakura y Sasuke frente a la
  Roca Hokage; a 0:32 primer plano de Kakashi; a 1:12-1:28 el equipo camina
  hacia un atardecer enorme — sirve como referencia de **encuadre y paleta
  de un opening real**, aunque no pude confirmar con una segunda fuente cuál
  opening exacto es (el título del uploader no lo precisa) · [Dailymotion](https://www.dailymotion.com/video/x88r3bd) ⚠️ (una fuente, número de opening sin confirmar) · fotogramas en `/tmp/claude-0/trabajo/30-naruto-video/op1/hoja_01.jpg`
- El clip «Naruto - Never Ending Spirit» (Dailymotion, 5:28) **NO es un
  ending oficial**: al mirarlo con fotogramas.py resultó ser un vídeo
  tributo/AMV de fan con el rótulo japonés «オープニングアニメーション»
  (animación de opening) superpuesto y marca de agua «AnimeYT.tv» — lo
  descarto como fuente de un ending real y lo anoto para que nadie lo cite
  como oficial ⚠️
- **Tráiler**: el de AniList (YouTube) no se pudo mirar (bloqueado). En
  Dailymotion, «Naruto Tráiler VO» (Sensacine, 1:57) es del **tráiler de
  cine en España** de una película de Naruto (no la serie), pendiente de
  identificar cuál exactamente — lo dejo anotado, no lo puse en «lo mejor»
  porque no llegué a mirarlo con fotogramas.py con este cupo de tanda ⚠️
- **Tendencia de TikTok, la que falta en la biblia** ✅✅ · el **«hand seal
  dance»** (baile de sellos de mano) se hizo viral con **«Silhouette»**
  (KANA-BOON, opening 16 de Shippuden, ep. 380-405): la propia banda lanzó
  el proyecto #silhouettetogether a finales de octubre pidiendo covers, y
  el tema llegó a lo más alto de las listas musicales de TikTok Japón; hay
  variantes con efecto de clon de sombra · [artículo 1](https://www.tiktok.com/@lento.lento/video/7538352262771395846) · [Wikipedia, Silhouette (canción)](https://en.wikipedia.org/wiki/Silhouette_(Kana-Boon_song)) · ✅ (dos fuentes) — **para la lámina de música/tendencias, ésta es la mejor pieza nueva del repaso**

### Punto 14 · Poses (con capítulo y minuto revisados en el fotograma)

- Kakashi, «Aceptado» (N005, 19:54): **NO** se inclina hacia el equipo como
  decía la biblia; el fotograma real muestra a Kakashi **saltando en el
  aire, brazos cruzados sobre el pecho**, con Sakura a su lado — corrección
  de pose ✅ [fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20005.mp4?t=1194)
- Naruto, «Acepto la 10.ª pregunta» (N025): pose real confirmada = **sentado
  en el pupitre, brazo derecho en alto con el puño cerrado, sudando, ceño
  fruncido** (00:10:45-00:10:54), no de pie golpeando la mesa · [fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20025.mp4?t=648) ✅ — sirve mejor para «**aceptar un reto sentado**» que para «regañar/afirmar de pie»
- Jiraiya explicando (N086, 20:15): primer plano de su cara con el
  rasguño, mirada de lado, **sin mostrar las manos** en ese segundo exacto
  (el globo de agua se ve un poco antes, hacia 20:10-20:13) — matiza el
  minuto de la biblia ⚠️ (lo tengo mirado, pero el instante exacto de
  "enseña el globo" cae un par de segundos antes del que cita la biblia)
- Itachi, adulto, capa de Akatsuki: no encontré el fotograma exacto de
  «Perdóname, Sasuke» de S135 en el archivo (a 00:01:10 sale Sasuke niño
  llorando en el bosque, no Itachi con la capa) — el minuto de la biblia
  puede estar desplazado por el corte de la copia latina; lo dejo como
  ⚠️ pendiente de recorte más fino (no alcanzó el cupo de esta tanda)

## Lo mejor para la lámina

1. **Tendencia real y verificable**: el «hand seal dance» con «Silhouette»
   (KANA-BOON) — con dos fuentes, minuto de opening 16 (ep. 380-405),
   perfecto para un texto de «¿sabías que…» en un canal de doblaje/canto.
2. **Pose de Naruto sentado, aceptando el reto** (N025, 00:10:45-00:10:54,
   puño en alto, sudando) — mejor que «de pie golpeando la mesa»: sirve
   para un personaje **sentado en un pupitre o mesa de trabajo** levantando
   la mano con decisión (encaja con un canal de escritura o estudio).
3. **Capa de Akatsuki, color real medido**: `#2A2B33` (casi negro con tinte
   azul) y nube en `#431C29`-`#491B28` en penumbra — para un elemento 3D o
   textura de fondo con esa paleta oscura.
4. Opening real mirado con logo «NARUTO -ナルト-» a 0:16 (Dailymotion) como
   referencia directa de tipografía y color del logo en movimiento.
5. «Sadness and Sorrow» (shakuhachi + shamisen + piano + violín) para
   musicalizar cualquier escena triste del canal; «Sasuke's Theme»
   (taiko + shakuhachi + guitarra eléctrica) para tensión seria.

## No encontré

- Segunda fuente sobre el origen del pueblo de Kishimoto como base de
  Konoha (busqué en japonés «岸本斉史 出身 ナルト 木ノ葉隠れ 元ネタ», sin
  resultado directo) ⚠️
- El tráiler oficial de anuncio de la serie (el de AniList, en YouTube,
  bloqueado en este servidor) mirado con fotogramas.py; sólo describí por
  encima el de Dailymotion «Naruto Tráiler VO» sin confirmar qué película es
- Un ending completo mirado y confirmado como oficial (el único clip largo
  de Dailymotion resultó ser un AMV de fan, no un ending real); los títulos
  de los endings (Wind, Yellow Moon, Viva★Rock…) siguen sólo con la lista de
  Narutopedia, sin fotograma propio
- El fotograma exacto de Itachi despidiéndose de Sasuke con la capa de
  Akatsuki puesta (S135 en el archivo de Internet Archive no coincidió con
  el minuto citado en la biblia; pendiente de recorte más fino)
- Vistas o número exacto de creadores del «hand seal dance» en TikTok (los
  artículos hablan de que es viral pero no dan una cifra fiable)

## Bitácora

- Herramienta directa (no buscador): `herramientas/fotogramas.py` sobre
  `archive.org/download/naruto-completo/…` (episodios 001, 005, 025, 086) y
  `archive.org/download/naruto-shippuden-lat/…` (episodios 86 y 135) — 8
  llamadas, unos 20 fotogramas mirados en pantalla.
- Herramienta directa: `herramientas/fotogramas.py` sobre dos clips de
  Dailymotion (opening x88r3bd, «ending» x1fsiw) y comprobación de
  `api.dailymotion.com` para el tráiler x8bc8i2.
- Medí color con Pillow (mediana de una región) sobre mis propios
  fotogramas: capa de Akatsuki y vestido de Sakura.
- Búsqueda web (inglés): `"Sadness and Sorrow" Naruto Yasuharu Takanashi
  composer` → Japan Nakama + Wikipedia (✅ resuelve un ⚠️ de la biblia).
- Búsqueda web (inglés): `Naruto TikTok trend viral sound 2024 2025` y
  `Naruto hand seal dance trend TikTok Silhouette KANA-BOON viral` →
  confirma la tendencia con dos fuentes.
- Búsqueda web (inglés): `chunin exam Naruto written test number of
  examinees 153` → Narutopedia confirma el número de 153 genin (biblia § 5.1
  lo tenía «de memoria»; ahora con cita directa, dejo ✅ con Narutopedia +
  el resumen ya usado por la biblia).
- Búsqueda web (español): `Naruto Latinoamérica Cartoon Network opening
  "Rise" tema en español o instrumental` → confirma que se emitió cantado en
  inglés en toda América.
- Búsqueda web (español): `Naruto anime instrumentación shakuhachi taiko
  guitarra eléctrica banda sonora estilo` → Narutopedia ES (Sasuke's Theme)
  + dodmagazine.es.
- Consulté `musicbrainz.org` (API) para comprobar si «Jiraiya no Theme»
  aparece en el OST vol. I: no aparece (21 pistas revisadas), lo dejo con
  una sola fuente (Wikipedia ES).
- No usé más buscador web de la cuenta (7 búsquedas en total en esta
  tanda): el resto del tiempo fue mirar vídeo directamente, como pide
  AYUDANTE.md.
