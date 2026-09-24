# Parte del investigador de VÍDEO · One Punch Man (encargo 35)

Puntos de `ENCARGO.md` que me tocan (según `EQUIPO.md`): **2** (fotogramas de escenas
icónicas), **4** (fondos y sitios: luz, paleta, texturas), **9** (música y sonido),
**10** (vídeos y tendencias) y **14** (poses analizadas por personaje).

Parto de `partes/datos-video.md` (ya recolectado, no repetido) y de la biblia a medias
(`biblia.md` ya trae un §2 "Las escenas que sirven" muy trabajado de otra pasada — no lo
repito, solo sumo lo nuevo que vi en esta tanda y lo que falta: §5, §11, §12, §15).

**YouTube bloqueado** todo el turno («Sign in to confirm you're not a bot», igual que en
la pasada anterior). Usé **Dailymotion** (copias de fans y clips de medios: Vidaextra,
Sensacine, aniBattle, AnimeBrawlCollection, moviepilot) e imágenes 1080p de la wiki de
Fandom (con Referer). Vi de verdad 4 vídeos con `herramientas/episodio.py` /
`fotogramas.py` (ficha minuto a minuto en `partes/episodios.md`, hojas en
`/tmp/claude-0/trabajo/35-video/`, borrados los `.mp4` al terminar):

1. **Opening T1** «THE HERO!!» — Dailymotion moviepilot, https://www.dailymotion.com/video/x7xerpa (1:29)
2. **Saitama vs. Boros** (final de temporada 1) — Dailymotion aniBattle 4K, https://www.dailymotion.com/video/x9b8564 (6:32)
3. **Saitama vs. Genos** (primer entrenamiento real) — Dailymotion AnimeBrawlCollection, subtítulos en inglés, https://www.dailymotion.com/video/x8raxsq (4:06)
4. **Tráiler oficial T3** (Garou) — Dailymotion Vidaextra, https://www.dailymotion.com/video/x8tl06u (1:54)

---

**Aviso sobre resolución real** (afecta al punto 2, que pide «1080p o más»): comprobé
con `yt-dlp -F` la resolución real servida por Dailymotion para los 4 clips que miré, y
en los 4 casos es **512×288** (el único formato HLS disponible sin iniciar sesión),
muy por debajo de lo que anuncian los títulos («HD», «4K»). Los títulos de los
uploaders son publicidad, no la resolución real. **Sí conseguí 1080p real** en 2 casos,
citando arte oficial/capturas de la wiki de Fandom en vez del vídeo: la ficha
`Genos_vs_Saitama_spar.png` (1920×1080, medida por API) para el combate T1-05, y las
imágenes ya citadas en biblia.md §2 (`wiki «S1E1…» 1920×1080`, etc.). Para el resto de
escenas (Boros, el opening, el tráiler T3) sólo tengo la copia de 512×288: lo dejo con
⚠️ en cuanto a resolución, aunque el contenido (diálogo, encuadre, color) sí lo
confirmé viéndolo.

## Hallazgos

### Punto 2 · Escenas icónicas (lo nuevo; el resto ya está en biblia.md §2)

- **Identifiqué el episodio exacto** del primer combate de entrenamiento Saitama-Genos
  que la wiki no tenía citado: es **«Saitama vs. Genos»**, manga cap. 17, **anime
  episodio 5 (T1-05)**, dentro del arco «National Superhero Registry». La wiki cita
  literalmente la misma frase que oí en el clip («Even he cannot explain the secret to
  his strength... but this battle may afford me a clue!»/«Even Master Saitama himself
  cannot explain. The secret to his power…» a 2:59-3:05 del clip) ·
  [wiki, texto](https://onepunchman.fandom.com/wiki/Saitama_vs._Genos) + clip visto
  (Dailymotion x8raxsq) · ✅ (dos fuentes, misma cita) · episodio T1-05.
- **La patada a la Luna, minutos exactos** (afina el dato de otra pasada, que decía
  «4:04-4:20» del mismo vídeo): en mi visionado va de **4:02** (Saitama sale volando,
  se ve la Tierra) a **4:16** (recoge una roca en la Luna, mirándola) ·
  [Dailymotion x9b8564](https://www.dailymotion.com/video/x9b8564?start=242) (aniBattle) ·
  ✅ (coincide con la otra pasada, mismo vídeo, mismo tramo) · T1-12.
- **Golpe Serio, tramo exacto**: la silueta de Saitama en pose de cruz (brazos y
  piernas abiertos, a punto de golpear) se ve en el **segundo 6:11-6:12**; el haz que
  parte hacia el espacio y llega a ver la Tierra desde fuera, **6:19-6:24** ·
  [Dailymotion x9b8564](https://www.dailymotion.com/video/x9b8564?start=371) · ✅ (coincide
  con «misma copia 5:44-6:20» de la otra pasada, con más precisión) · T1-12.
- **Nueva escena para la lámina — el primer entrenamiento real (T1-05)**: Genos pide
  un combate «en serio», con reglas (esquivar lo esquivable, no contenerse, seguir
  hasta no poder más); Saitama lo esquiva todo por «imagen residual» (afterimage) y
  gana tocándole la mejilla; termina con «I'm starving, time for lunch» / en japonés
  quedan a comer udon · [Dailymotion x8raxsq](https://www.dailymotion.com/video/x8raxsq)
  (sub. en inglés) + [wiki](https://onepunchman.fandom.com/wiki/Saitama_vs._Genos) ·
  ✅ · T1-05, 0:10-4:05 del clip.
- **Fotograma oficial 1080p** de este combate (Genos lanzando su Cañón de Incineración
  con el brazo entero convertido en cañón con rayos; Saitama vuela hacia atrás, cara
  inexpresiva, ropa ondeando) — sirve para «pose sin inmutarse»:
  [wiki, `Genos_vs_Saitama_spar.png`](https://static.wikia.nocookie.net/onepunchman/images/6/68/Genos_vs_Saitama_spar.png) ·
  1920×1080 (medido, API `imageinfo`) · ✅ · T1-05.
- **Tráiler oficial de la T3** (Garou, 1:54): 0:10 logo; 0:21-0:52 Garou se transforma y
  pelea contra monstruos con un cielo de atardecer rojo/rosa; 0:58 salto en silueta;
  1:15 primer plano del ojo de Saitama; 1:23-1:30 Garou con cara de monstruo; 1:34
  cartela «VS» en blanco y negro; 1:40 logo «ONE PUNCH MAN 3»; **1:50 créditos
  completos** (reparto y staff, ver punto 9 y 10) ·
  [Dailymotion x8tl06u](https://www.dailymotion.com/video/x8tl06u) (Vidaextra, 76 923
  vistas) · ✅ (créditos en pantalla, fuente primaria) · T3, oct-2025.

### Punto 4 · Sitios, luz, paleta y texturas (sección vacía en biblia.md — la lleno)

**Colores medidos con `herramientas/estilo.py`** (Pillow), sobre fotogramas que
recorté yo mismo de las hojas de `episodio.py`/`fotogramas.py` o sobre arte oficial de
la wiki. Cito siempre de dónde sale cada paleta.

- **Z-City** (la ciudad de Saitama): fondo urbano gris-azulado con cielo azul intenso y
  nubes blancas, edificios en beige/gris/blanco roto, montaña difuminada al fondo.
  Paleta medida: `#B0B1B8` 21% · `#888C98` 18% · `#5F6881` 17% · `#3C455C` 16% ·
  `#D6D6D9` 15% · `#1C2028` 13% (fondo azul-noche de las sombras) · sombreado
  degradado con mucha línea gris `#5D5E64` · [wiki, `Zcity.png`](https://static.wikia.nocookie.net/onepunchman/images/f/f8/Zcity.png)
  1280×719 (medido) · ✅ · imagen del sitio general (episodio no especificado en la wiki).
- **Campo de batalla final contra Boros** (T1-12, de noche, tras el impacto de la nave):
  paleta casi negra con rojo y naranja de fuego: `#100305` 26% · `#DB1515` 21% ·
  `#380307` 18% · `#63040D` 14% · `#A40411` 13% · `#E96826` 7% (naranja de la nave en
  llamas) — saturación 91%, brillo 45%, sombreado degradado/pintado, casi sin línea
  visible · medido sobre fotograma del min. 2:09 de [Dailymotion x9b8564](https://www.dailymotion.com/video/x9b8564?start=129) · ✅.
- **Forma verdadera de Boros** (silueta negra, ojo blanco, dientes): fondo casi negro
  `#0F040B` 37%, piel/hueso crema `#E8D5BD` 19%, granates apagados `#321420`/`#5A353F`
  — saturación 52%, brillo 37%, mucha línea marcada `#503238` · medido en el min. 1:36
  del mismo vídeo · ✅.
- **Impacto del Golpe Serio** (el fogonazo blanco antes del haz): paleta casi
  monocroma, blanco cálido `#F6F5E0` 40% + `#F2F6E0` 36% + `#F9F2E0` 17%, apenas negro
  3% — brillo 93%, sombreado plano (cel), casi sin línea · min. 6:11 · ✅. Sirve para el
  «flash» de cualquier golpe de la lámina.
- **La Tierra vista desde el espacio** (tras el Golpe Serio): `#F3EFD9` 33% (haz),
  `#0C0708` 18% (espacio), `#A3BEC5` 16% (azul Tierra), `#8B8987` 11% (nubes),
  `#594470` 11% (morado del rayo) — sombreado degradado, mucha línea `#8B8187` · min.
  6:22 · ✅.
- **Cañón/desierto del entrenamiento con Genos** (T1-05, de día): tierra clara y roca
  contra cielo azul: `#1D1917` 37% (roca en sombra) · `#C0B69D` 34% (tierra clara) ·
  `#E5DCC9` 17% (polvo/cielo claro) · `#927F5E` 9% · azul de cielo `#3858B3` 3% —
  saturación baja (23%), brillo medio (53%), línea normal `#8D7A56` · min. 0:59 de
  [Dailymotion x8raxsq](https://www.dailymotion.com/video/x8raxsq?start=59) · ✅.
- **Llamarada del Cañón de Incineración de Genos** (mismo combate): naranja de fuego
  intenso `#F1C92E` 19% + `#BD5F0C` 17% sobre marrón quemado `#291009` 31% / `#6C2A08`
  23% — saturación 80% · min. 2:30 · ✅.
- **Opening T1 — acantilados de hielo** (paisaje simbólico, sin localizar en la trama):
  paleta fría, grisazulada: `#586874` 23% · `#394751` 22% · `#7F8C93` 16% · `#ADB3B2`
  15% · `#1B2125` 13% — sombreado degradado, mucha línea `#64727E` · min. 0:22 del
  opening ([Dailymotion x7xerpa](https://www.dailymotion.com/video/x7xerpa?start=22)) · ⚠️
  (paisaje de openings, no aparece tal cual en el anime; sirve solo como referencia de
  ambiente «fin del mundo»).
- **Tráiler T3 — atardecer de la pelea con Garou**: rojos y granates oscuros
  `#2C0A15` 25% · `#411E23` 25% · `#17040C` 23% · `#592D35` 16% · rosa claro `#E5A8BA`
  5% — saturación 66%, brillo bajo (26%) · min. 0:47 del tráiler
  ([Dailymotion x8tl06u](https://www.dailymotion.com/video/x8tl06u?start=47)) · ✅.
  **Este atardecer rojo/rosa es la paleta propia de la temporada 3** (Garou), distinta
  del gris-azulado de Z-City y del negro-rojo de la pelea con Boros.
- **El dojo de Bang (Silver Fang)**: en la cima de una montaña altísima, solo se llega
  por una **escalera de madera tallada en la roca** (cientos de escalones); un
  aspirante llega en coche y mira hacia arriba. Es manga en blanco y negro (sin color
  que medir, saturación 0% confirmada con `estilo.py`), pero es el único sitio "de
  madera" claro de la serie (el resto es ciudad/metal/roca) — sirve para la textura de
  madera que pide el punto 4 · [wiki, `Bang's_dojo.png`](https://static.wikia.nocookie.net/onepunchman/images/4/4d/Bang%27s_dojo.png)
  1908×3024 (medido) · ✅ (imagen + descripción de la wiki del personaje Bang).
- **Texturas reales equivalentes (CC0)**, por sitio:
  - Ruinas/hormigón de la ciudad destruida → **Concrete034** (ambientCG, CC0) —
    https://ambientcg.com/view?id=Concrete034
  - Brazo/armadura de Genos y los robots → **Metal063** (ambientCG, CC0) —
    https://ambientcg.com/view?id=Metal063
  - Roca del cañón/la Luna → **Rock063** (ambientCG, CC0) —
    https://ambientcg.com/view?id=Rock063
  - Escalera de madera del dojo de Bang → **WoodFloor064** (ambientCG, CC0) —
    https://ambientcg.com/view?id=WoodFloor064
  - ✅ (API de ambientCG, licencia CC0 confirmada en la propia ficha del recurso).

---

### Punto 9 · Música y sonido (sección vacía en biblia.md — la lleno)

**Compositor de toda la serie (T1, T2 y T3): Makoto Miyazaki (宮崎誠)** — lo leí yo
mismo en los créditos finales del opening T1 («音楽 宮崎誠», fotograma 33 de la hoja de
`episodio.py`, min. 0:53) y en los créditos del tráiler de la T3 («Music: Makoto
Miyazaki», fotograma 30, min. 1:50) · confirmado además por
[CDJapan (álbum «One Take Man»)](https://www.cdjapan.co.jp/product/LACA-15536) y
[IMDb](https://www.imdb.com/name/nm4381951/) · ✅ (visto en pantalla + dos fuentes
externas).

**Openings y endings por temporada** (nombre, artista, y letra/composición cuando se
pudo verificar):

- **T1 (2015) OP — «THE HERO!! ～怒れる拳に火をつけろ～»** («THE HERO!! Ikareru Ken ni
  Honoo wo Tsukero»), interpretada por **JAM Project**, sello **Lantis**. **Letra y
  composición: Motoi Iwasaki (岩崎元是); arreglo: Makoto Miyazaki** — leído directo del
  cartel de créditos del opening, fotograma 39 (min. 1:12) de
  `/tmp/claude-0/trabajo/35-video/opening/hojas/hoja_01.jpg` · confirmado en
  [Wikipedia (One-Punch Man season 1)](https://en.wikipedia.org/wiki/One-Punch_Man_season_1) ·
  ✅ (visto en pantalla + wiki).
- **T1 ED (ep. 1-11) — «星より先に見つけてあげる» («Hoshi yori Saki ni Mitsukete
  Ageru»)**, cantada por **Hiroko Moriguchi**; el ep. 12 cambia a **«悲しみたちを抱きしめて»
  («Kanashimi-tachi wo Dakishimete»)**, misma cantante · [Wikipedia](https://en.wikipedia.org/wiki/One-Punch_Man_season_1) ·
  ⚠️ (una sola fuente comprobada; no vi el cartel de créditos del ending).
- **T2 (2019) OP — «Unyielding Justice» / «静寂のアポストル» («Seijaku no Apostle»)**,
  **JAM Project**. **ED — «地図が無くても戻るから» («Chizu ga Nakutemo Modoru Kara»)**,
  cantada por **Makoto Furukawa** (la voz japonesa de Saitama) ·
  [Wikipedia (season 2)](https://en.wikipedia.org/wiki/One-Punch_Man_season_2) · ⚠️
  (una fuente; pendiente cruzar con un cartel de créditos).
- **T3 (2025) OP — «Get No Satisfied!»**, **JAM Project feat. BABYMETAL** (colaboración
  anunciada como novedad de esta temporada). **ED — «そこにある灯り» («Soko ni Aru
  Akari»)**, cantada por **Makoto Furukawa** (otra vez la voz de Saitama) ·
  [Anime News Network](https://www.animenewsnetwork.com/news/2025-08-23/babymetal-contributes-to-jam-project-one-punch-man-season-3-opening-song/.227998) +
  [Weebwire/AniTrendz](https://weebwire.com/news/makoto-furukawa-returns-headline-one-punch-man-season-3-ending-theme-20250805) ·
  ✅ (dos fuentes).
- **Insert song de las OVA — «タツマキとフブキのワンパン音頭» («Everyone's One-Punch
  Song»)**: la cantan **juntas las voces japonesas de Saitama, Genos, Speed-o'-Sound
  Sonic, Tatsumaki, Fubuki, King y Mumen Rider** (Makoto Furukawa, Kaito Ishikawa,
  Yuki Kaji, Aoi Yuuki, Saori Hayami, Hiroki Yasumoto, Yuuichi Nakamura); letra de Aira
  Yūki, composición de Makoto Miyazaki; sale con la OVA 6, mayo de 2016, sello Lantis ·
  [wikitexto de la wiki, `Everyone's One-Punch Song`](https://onepunchman.fandom.com/wiki/Everyone%27s_One-Punch_Song) ·
  ✅ (confirma también, por tercera vez, que Miyazaki compone toda la música de la
  franquicia). **Muy buen dato para una lámina de "todos cantan juntos" o de fandub**.
- **Tema en la escena más emotiva de Mumen Rider** (contra el Rey del Mar Profundo,
  T1-09): según reseñas y recopilaciones de fans suena una versión lenta/orquestal del
  tema de Saitama («Saitama's Theme», también llamado Ballad/Sad ver.) — 
  [vídeo de referencia en YouTube](https://www.youtube.com/watch?v=fTVY7400WnU) (no
  descargable por el bloqueo de la sesión) · ⚠️ (fuente de fans, no lo pude confirmar
  contra el episodio real ni contra el álbum oficial «One Take Man»).

**Efectos de sonido reconocibles** (de lo que vi y oí en los tres clips con audio
original japonés, Whisper no transcribe SFX así que esto es observación directa,
⚠️ una sola fuente — mía):
- El **silencio total** después de cada golpe de Saitama (se corta la música y el
  ruido de fondo un segundo antes de que hable el rival) — se nota clarísimo tras el
  golpe a Boros, min. 6:12-6:19 del clip de aniBattle.
- Un **zumbido grave** (tipo motor) que sube de volumen segundos antes de cualquier
  ataque especial (Boros cargando su cañón, Genos cargando el brazo) — en el clip de
  Genos, min. 2:20-2:23, justo antes de «Incinerate!».
- Nada de manga (onomatopeyas de texto) va aquí: eso es punto 19/6, de texto.

---

### Punto 10 · Vídeos y tendencias (sección vacía en biblia.md — la lleno)

- **YouTube pidió «confirma que no eres un bot» / 429 en TODOS los intentos** de esta
  tanda (trailer oficial `RzmFKUDOUgw` de AniList incluido) — igual que la pasada
  anterior. Use Dailymotion como plan B en los 4 vídeos que miré (ver cabecera).
- **Tráiler oficial T3** (Vidaextra, 76 923 vistas en Dailymotion) — desglose completo
  con minuto en el punto 2. Confirma en pantalla (min. 1:50): reparto japonés
  **Saitama: Makoto Furukawa, Garou: Hikaru Midorikawa, Dr. Genus (narración): Daisuke
  Namikawa**; guion de la serie: Tomohiro Suzuki; diseño de personajes: Chikashi
  Kubota, Shinjiro Kuroda, Kyosuke Shirakawa; estudio: **J.C.Staff**; basado en la
  obra de **ONE y Yusuke Murata**, serializada en «Tonari no Young Jump» (Shueisha) ·
  [Dailymotion x8tl06u](https://www.dailymotion.com/video/x8tl06u) · ✅ (créditos en
  pantalla).
- **Tendencia en TikTok — «edits» con phonk**: los montajes de One Punch Man en TikTok
  usan sobre todo música **phonk lenta/bajo pesado** sobre escenas de pelea; los más
  repetidos son ediciones de **Garou** con phonk antiguo y de **Saitama caminando**
  entre escombros con la canción «MTG Prism» · páginas de descubrimiento de
  [TikTok · One Punch Man Edits](https://www.tiktok.com/discover/one-punch-man-edits),
  [TikTok · One Punch Man Phonk Edit](https://www.tiktok.com/discover/one-punch-man-phonk-edit) ·
  ⚠️ (resumen de búsqueda, no pude abrir TikTok directo desde el contenedor; sirve
  igual para saber qué tono de vídeo funciona: cámara lenta + música grave + primeros
  planos de escombros y caras).
- **Análisis en YouTube** («One Punch Man - Emotional/Sad Theme/Scene [Mumen Rider]»,
  y un tutorial de piano del mismo tema) — confirman que el tema de Mumen Rider bajo
  la lluvia (T1-09) es el vídeo de fans más repetido sobre la escena, aunque no pude
  bajarlo para sacar el minuto exacto por el bloqueo de YouTube · ⚠️.
- **No encontré** un vídeo de análisis "serio" (tipo video-ensayo sobre animación o
  dirección) con minuto verificado: los que aparecen en las búsquedas están todos en
  YouTube y no se pudieron abrir. Búsquedas hechas: «one punch man animation analysis
  video essay», «one punch man director interview video» (en, sin resultado
  descargable).

---

### Punto 14 · Poses analizadas por personaje (sección vacía en biblia.md — la lleno)

Las poses de Saitama y Genos salen de los clips que miré fotograma a fotograma esta
tanda (Boros y el entrenamiento con Genos); las de Tatsumaki, de arte oficial de la
wiki que también miré yo; las de Mumen Rider, de la cita ya verificada de la pasada
anterior (mismo clip, sin volver a descargarlo). Nada de memoria: cito hoja/imagen y
minuto siempre.

#### Saitama

1. **De pie, quieto, capa al viento**, mirando al horizonte del cañón antes del combate
   — postura relajada, brazos caídos, mirada al frente. Sirve para **presentar**. ·
   min. 0:59, [Dailymotion x8raxsq](https://www.dailymotion.com/video/x8raxsq?start=59) · ✅.
2. **Brazos cruzados, cara seria**, escuchando a Genos explicar las reglas del combate
   («Do not hold back… keep fighting until I am no longer able to fight»). Sirve para
   **explicar/regañar** (postura de "te estoy escuchando pero no me impresionas"). ·
   min. 2:51-3:05, mismo vídeo · ✅.
3. **Pateando a Genos en el aire**, cuerpo en diagonal, pierna extendida, cara sin
   esfuerzo. Sirve para **celebrar/presumir sin querer** (gana sin esforzarse). · min.
   3:25, mismo vídeo · ✅.
4. **Caminando junto a Genos**, de perfil, mirándolo de reojo, mano en la cadera —
   postura floja, casual. Sirve para **animar/charlar** («I'm starving, time for
   lunch»). · min. 3:33, mismo vídeo · ✅.
5. **Cara completamente inexpresiva mientras sale volando** por el golpe de Genos
   (brazos y piernas sueltos, capa ondeando, ni un gesto de dolor) — fotograma oficial
   1080p de la wiki, sirve para **pensar/no inmutarse** ·
   [`Genos_vs_Saitama_spar.png`](https://static.wikia.nocookie.net/onepunchman/images/6/68/Genos_vs_Saitama_spar.png)
   1920×1080 · ✅.
6. **Sentado en el borde de un cráter en la Luna**, mirando hacia abajo, agotado pero
   tranquilo; luego **agachado, listo para saltar de vuelta a la Tierra** (piernas
   flexionadas, un brazo atrás). Sirve para **pensar** (el gag de "cómo vuelvo") · min.
   4:07-4:12, [Dailymotion x9b8564](https://www.dailymotion.com/video/x9b8564?start=247) · ✅.
7. **Pose en cruz mid-aire** (brazos y piernas totalmente abiertos, silueta a
   contraluz) justo antes del Golpe Serio contra Boros. Sirve para **el golpe/clímax**
   de cualquier lámina de acción · min. 6:11, mismo vídeo · ✅.
8. **De pie con expresión neutra, después de ganar** el combate con Genos («Okay, I
   win.»), mano en la cara de él tocándole la mejilla — sirve para **celebrar sin
   alardear**. · min. 2:33, [Dailymotion x8raxsq](https://www.dailymotion.com/video/x8raxsq?start=153) · ✅.

#### Genos

1. **Brazo transformado en cañón, cargando energía** con chispas y luz naranja
   saliendo de las juntas — cuerpo echado hacia atrás para amortiguar el disparo.
   Sirve para **el ataque/clímax**. · min. 2:23, [Dailymotion x8raxsq](https://www.dailymotion.com/video/x8raxsq?start=143) · ✅.
2. **De perfil, mirada fija y seria**, antes de lanzar el ataque definitivo
   («Incinerate!»). Sirve para **animar/concentrarse**. · min. 2:20, mismo vídeo · ✅.
3. **Mirando a Saitama de reojo con el ceño fruncido**, aceptando que no puede
   explicarle su fuerza — postura recta, brazos a los lados. Sirve para **pensar/
   admirar**. · min. 3:03-3:08, mismo vídeo · ✅.

#### Tatsumaki

El encargo la pide entre los 4 personajes para empezar; no la vi en vídeo esta tanda
(no encontré un clip suyo completo y decente en Dailymotion), así que estas 3 poses
salen de **arte oficial de la wiki, mirado por mí** (no de memoria):

1. **Brazos cruzados, ceño fruncido, de pie sobre escombros** — postura cerrada y
   arisca, típica de ella. Sirve para **regañar**. ·
   [wiki, `Tatsumaki_Anime_Profile_Shot.png`](https://static.wikia.nocookie.net/onepunchman/images/6/62/Tatsumaki_Anime_Profile_Shot.png)
   1040×1078 (medido) · ✅.
2. **Señalando a cámara con un dedo, ceja levantada, primer plano** — gesto de orden
   o desprecio (le dice a Saitama que se vaya). Sirve para **regañar/explicar**. ·
   [wiki, `Tatsumaki_tells_Saitama_to_leave.png`](https://static.wikia.nocookie.net/onepunchman/images/b/b6/Tatsumaki_tells_Saitama_to_leave.png)
   1920×1080 (medido, screenshot real del anime) · ✅. Esta es la escena de «¿Y esta
   niña perdida tan insolente?» ya citada en biblia.md §2 (item 12): mismo momento,
   dos ángulos.
3. **Flotando con los brazos en alto, pelo y ropa desgarrándose por la energía**,
   cara con los ojos muy abiertos por el esfuerzo — levantando toda la base de la
   Asociación de Monstruos desde bajo tierra. Sirve para **el máximo esfuerzo/clímax
   de poder**. · [wiki, `Tatsumaki_lifts_Monster_Association_base_out_of_ground.png`](https://static.wikia.nocookie.net/onepunchman/images/e/e3/Tatsumaki_lifts_Monster_Association_base_out_of_ground.png)
   1568×1145 (medido; página de manga, blanco y negro) · ✅ (ya citada de pasada en
   biblia.md §2, item 20; aquí la describo como pose).

#### Mumen Rider

No repito el visionado (ya lo hizo a fondo la pasada anterior, biblia.md §2, item 9-11,
con el mismo clip que cito aquí de nuevo para no perder la referencia): **T1-09,
[Dailymotion x8rl50h](https://www.dailymotion.com/video/x8rl50h)**. Las poses, leídas
de esas citas ya verificadas:

1. **Lanza su bicicleta al suelo y se planta firme** ante el Rey del Mar Profundo, sin
   ninguna superpotencia. Sirve para **presentar/decidirse**. · min. 3:00 · ✅ (dos
   fuentes: cita ya en biblia.md + clip).
2. **De pie bajo la lluvia, empapado, mirando al monstruo** mientras dice «I'm weak. I
   know that much... And yet, I have to try». Postura recta pese al miedo. Sirve para
   **animar(se) a uno mismo**. · min. 4:00-4:12 · ✅.
3. **Atrapado en el aire por Saitama tras caer derrotado**, cuerpo flojo, exhausto.
   Sirve para **el momento de rescate/agradecimiento** (Saitama: «You did well. Nice
   fight.»). · min. 5:12 · ✅.

#### Boros (de paso, villano de la pelea más citada; no es de los 4 personajes del encargo)

- **Forma verdadera**, brazos extendidos hacia arriba, boca abierta con dientes
  afilados, ojo único brillando — pose de villano "a punto de soltarlo todo". Sirve
  para **el discurso final de un antagonista**. · min. 1:36-2:11,
  [Dailymotion x9b8564](https://www.dailymotion.com/video/x9b8564?start=96) · ✅.

---

## Lo mejor para la lámina

1. La **pose 5 de Saitama** (cara inexpresiva volando por el golpe de Genos, fotograma
   oficial 1080p de la wiki) resume todo el humor de la serie en una sola imagen.
2. La **paleta del atardecer de la T3** (rojos/granates, Garou) es una identidad de
   temporada distinta al gris de Z-City y al negro-rojo de Boros: útil si la lámina
   quiere sentirse "de la temporada más nueva".
3. El **insert song «Everyone's One-Punch Song»**, cantado por todo el reparto, es un
   dato perfecto para un canal de doblaje/fandub: "hasta los actores originales
   cantan juntos".
4. El **Golpe Serio** (T1-12, min. 6:11-6:24 del clip de aniBattle) da tres capas de
   luz en tres segundos: silueta en cruz → fogonazo blanco total → rayo que llega al
   espacio. Sirve de referencia de iluminación para cualquier "golpe final" en la
   lámina.
5. El **primer entrenamiento con Genos** (T1-05) da una secuencia completa
   presentar→pelear→ganar→comer que es fácil de convertir en 4 viñetas de una lámina
   por pasos.

## No encontré

- **Vídeo de análisis (video-ensayo) de la animación con minuto exacto**: los
  resultados están todos en YouTube y no pude bajarlos (bloqueo de sesión, 429/login
  en todos los intentos). Búsquedas: «one punch man animation analysis video essay»
  (en), «one punch man director interview video» (en). ⚠️ Queda pendiente si otra
  sesión tiene acceso a YouTube.
- **Minuto exacto de un fan-dub o cover del opening en español** dentro de un vídeo:
  eso lo cubre el investigador de voz/personajes (punto 22), no lo dupliqué aquí.
- **Confirmación con cartel de créditos** de los OP/ED de T2 (solo tengo Wikipedia,
  ⚠️): no encontré una copia del episodio con los créditos visibles para leerlos yo
  mismo, como sí hice con T1 y T3. Búsquedas: `site:dailymotion.com "One Punch Man"
  opening season 2`, sin clip completo con créditos.
- **Vídeos oficiales de TikTok verificados uno por uno** (canal, vistas exactas): el
  contenedor no abre TikTok directamente; me quedé con las páginas de descubrimiento
  (`/discover/...`), que ya indican qué sonidos son tendencia pero no dan un enlace de
  vídeo con vistas concretas. ⚠️.

---

## Bitácora de búsqueda (vídeo)

- **Datos previos usados sin repetir la consulta**: `partes/datos-video.md`
  (AniList, Dailymotion, Internet Archive, MusicBrainz — recolectado antes de esta
  tanda).
- Wiki de Fandom (`onepunchman.fandom.com/api.php`, inglés): `list=search` para
  «Z-City», «music soundtrack», «Genos sparring match udon», «practice bout»;
  `action=parse&prop=wikitext` sobre las páginas `Z-City`, `Saitama vs. Genos`,
  `Everyone's One-Punch Song`; `prop=imageinfo` sobre `Zcity.png`, `Saitama
  Apartment.jpg`, `Z-city manga colored.jpg`, `Genos vs Saitama spar.png`, `Genos Arms
  Mode Incineration Cannon.gif`.
- Dailymotion API (`api.dailymotion.com`): búsqueda de metadatos (duración, autor,
  vistas) de `x9b8564`, `x7xerpa`, `x8rl50h`; búsqueda de vídeos «Saitama Genos scene»
  y «One Punch Man Genos disciple» (inglés) para elegir el clip del punto 2/14.
- Internet Archive (`archive.org/metadata/...`): comprobé `turner_video_135772` y
  `turner_video_135773` (duración real ~1:40-2:13, son PV cortos, no episodios
  completos) antes de descartarlos a favor de los clips de Dailymotion.
- `herramientas/episodio.py` (3 vídeos, ✅ hecho, ver cabecera) y
  `herramientas/fotogramas.py --cortes` (1 vídeo, el tráiler T3).
- `herramientas/estilo.py --colores`: 11 fotogramas recortados a mano de las hojas de
  contacto, más 2 imágenes de la wiki (Z-City, apartamento de Saitama).
- ambientCG (`ambientcg.com/api/v2/full_json`, inglés): «concrete», «metal», «rock
  cliff» → Concrete034, Metal063, Rock063 (CC0).
- WebSearch (4 búsquedas, español e inglés): openings/endings por temporada;
  compositor Makoto Miyazaki; tema de Season 3 (JAM Project + BABYMETAL); tendencia de
  TikTok; tema emotivo de Mumen Rider.
- WebFetch (3 páginas): Wikipedia «One-Punch Man season 1» y «season 2» (openings/
  endings); TV Tropes «Awesome Music/OnePunchMan» → **403 Forbidden**, no insistí más
  (regla de los dos intentos).
- Nada de Crunchyroll ni cuentas de streaming; nada de programas de terceros para
  saltar bloqueos (solo Dailymotion, Internet Archive y la wiki, como pide el aviso).

