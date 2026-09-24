# Parte de VÍDEO · Big Hero 6 (Grandes Héroes) · puntos 2, 4, 9, 10 y 14 de ENCARGO.md

Repaso completo (equipo de 8). Partí de `partes/datos-video.md` (Dailymotion e IA de
`recolectar.py` con resultados irrelevantes por el nombre genérico «Heroes») y de
`biblia.md` ya existente (secciones 4, 6, 11, 12, 15), que tenía casi todo
marcado **⚠️ «de memoria», «minuto sin verificar», «no se pudo abrir YouTube»**.
YouTube sigue pidiendo iniciar sesión desde este servidor (confirmado: yt-dlp
da «Sign in to confirm you're not a bot»). Usé **Dailymotion** (clips oficiales
cortos) e **Internet Archive** (escena eliminada y vídeo de «Immortals»), los
bajé enteros (son cortos, no el archivo completo) y los miré de verdad con
`fotogramas.py --cortes`. Todo lo de abajo tiene fotograma + minuto real del
clip citado (no de memoria). Trabajo pesado en `/tmp/claude-0/trabajo/08-video/`.

## Hallazgos

### Punto 2 · Escenas icónicas (con fotograma y minuto reales)

**Clip «Meet Baymax»** (CGMeetup, Dailymotion, 2:02) — activación de Baymax
en el cuarto de Hiro: https://www.dailymotion.com/video/x2553ox
- 0:09 — primer plano del botón rojo circular de encendido en el pecho ✅ (visto).
- 1:02 — el pecho de Baymax **enciende la escala de dolor de 10 caras**
  (confirma lo que decía el TV Tropes citado antes, ahora con fotograma
  propio) ✅ (visto + [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Funny/BigHero6)).
- 1:12 — Baymax escanea a Hiro: cabeza inclinada, una mano apoyada en el
  hombro del paciente ✅ (visto).
- 1:53 — HUD azul de escaneo en pantalla («SYMPTOMS», signos vitales en
  números): sirve también para el punto 6/11 de texto (interfaz), lo anoto
  para el investigador de texto ✅ (visto).

**Clip «Low Battery»** (oficial, Dailymotion, 1:04): https://www.dailymotion.com/video/x283k45
(la misma escena en francés, también vista: https://www.dailymotion.com/video/x31z3kn)
- 0:22-0:30 — Baymax baja las escaleras de madera de la casa Hamada
  tambaleándose, batería baja, de noche ✅ (visto, dos cortes del mismo plano).
- 0:40-0:44 — en la cocina, la tía Cass está fregando; Baymax choca con Hiro
  al entrar («drunk walk», pasos irregulares, brazos sueltos) ✅ (visto).
- **Corrección importante:** la biblia actual (sección 4) dice que en esta
  escena Baymax «coge al gato Mochi y le llama bebé peludo». **Eso NO es de
  la película de 2014.** Es un gag de un corto distinto, *Big Chibi 6:
  «Low Battery»* (2019, spin-off chibi de la serie de TV, dirigido por Ben
  Juwono), donde Mochi sí ayuda a meter a Baymax en su cargador. Lo confirmé
  en la propia wiki con el guion completo del corto (ficha, reparto y
  argumento) ✅ ([bighero6.fandom.com/wiki/Low_Battery](https://bighero6.fandom.com/wiki/Low_Battery),
  vídeo oficial de Disney Channel: https://youtu.be/vmy5afLiIVc) y viendo la
  escena real de la película (arriba), que no tiene gato. **Hay que corregir
  la sección 4 de la biblia**: separar «batería baja en la película» (cocina,
  sin Mochi) de «batería baja, corto Big Chibi 6» (con Mochi, 2019, serie).

**Clip «Fist Bump»** oficial Movieclips-style (Dailymotion, 0:31): https://www.dailymotion.com/video/x3wn7x2
- 0:21 — es el choque de puños **final** (epílogo, Baymax ya con la nueva
  armadura verde, sala con biombo japonés en SFIT): Hiro extiende el puño,
  Baymax lo imita despacio y dice su frase; ambos sonríen ✅ (visto).
  El choque de puños «clásico» de mitad de película (el que enseña Hiro con
  el «ba-la-la-la-la» de los dedos) no lo encontré como clip suelto en
  Dailymotion/IA; sigue con el enlace de YouTube sin verificar
  (`--fotograma` con storyboard sería el plan C, no hizo falta: ya hay dos
  fist-bumps reales confirmados).

**Escena del clímax** (batalla final en la isla/portal), «Last Fighting
Scene» (Dailymotion, 4:58): https://www.dailymotion.com/video/x7vbgp7
- 0:24 — Fred (traje verde-lagarto) escupe fuego, postura agachada, brazos
  extendidos ✅ (visto).
- 0:30-0:33 — Honey Lemon lanza bolas químicas rosas (esfera expansiva) ✅.
- 0:56-1:06 — Baymax y Hiro caen en picado sujetos con el brazo del traje
  morado antes de cruzar el portal (la escena que hace llorar, ver parte de
  voz/texto para el punto 21) ✅ (visto).
- 1:26 — Wasabi (traje verde), Fred y el resto de pie tras la batalla,
  Baymax con el puño extendido saludando ✅ (visto).
Sirve para las poses de equipo (abajo) y confirma los colores reales de los
trajes en acción (fuego naranja de Fred, rosa de Honey Lemon, morado de Hiro).

**Escena eliminada** «Hamada Brother Robotics» (Internet Archive, storyboard
en blanco y negro, no animación final; ±2 s): https://archive.org/details/youtube-wnDrECylMOU
- 0:42 — plano del storyboard: Tadashi de espaldas mostrando algo a Hiro en
  el garaje ✅ (visto, es boceto, no color final; marcarlo como storyboard).

**Serie de TV** — no hay «3 escenas icónicas» de una serie clásica (Big Hero
6: The Series es de 2017-2021, comedia episódica, sin arco tan marcado), pero
sí un corto oficial de acción del elenco completo: «Big Hero Battle» (clip
oficial, canal *teasertrailer*, Dailymotion, 1:28): https://www.dailymotion.com/video/x7x6uz7
- 0:01 — equipo completo en pose de combate: Baymax rojo, Wasabi verde, Fred
  naranja, en la calle junto a la autocaravana ✅ (visto). El resto del clip
  es un villano-boyband (parodia), no escenas del elenco: lo anoto pero no es
  «icónico» del team, sólo sirve para confirmar el vestuario de la serie
  (colores más saturados que la película: rojo puro, verde lima, naranja).

### Punto 4 · Sitios, luz y paleta (medidos con Pillow en fotogramas reales)

Corrijo los hex «a ojo, sin medir» de la sección 6 de la biblia por estos,
medidos con `herramientas/estilo.py` sobre fotogramas de los clips de arriba
(archivo de paleta: `/tmp/claude-0/trabajo/08-video/color/paleta`):

| Sitio / toma | Hex medidos (dominante → 6.º) | Fuente y minuto |
|---|---|---|
| Cuarto de Hiro, luz de tarde (persiana), fotograma 1:02 del clip Meet Baymax | `#C5B9AA` 32% · `#241203` 29% · `#4C2F11` 14% · `#3B4B37` 12% · `#F6F5E3` 9% | ✅ medido, clip x2553ox 1:02 |
| Mismo cuarto, escaneo 1:12 (más sombra) | `#322820` 31% · `#0C0705` 25% · `#554D40` 18% · `#88816F` 12% · `#E6F0F6` 5% (blanco-azulado de Baymax) | ✅ medido, clip x2553ox 1:12 |
| Cocina Lucky Cat, noche, plano general 0:30 | `#66462F` 29% · `#392721` 27% · `#975B44` 14% (madera/terracota) · `#3F4C59` 11% (azulado ventana) · `#BFBA89` 11% · `#848E6E` 10% (verde agua alacena) | ✅ medido, clip x31z3kn/x283k45 0:30 |
| Cocina, mesa de la tía Cass 0:40 | `#35241D` 45% · `#543C31` 23% · `#7E5E4C` 12% · `#98977C` 9% · `#D5C29F` 7% · **`#DA3F3D` 3% (la encimera roja)** | ✅ medido, mismo clip 0:40 — visto: alacenas verde menta, pared amarillo-verdosa, encimera roja, lámpara de techo cálida |
| Vuelo nocturno sobre San Fransokyo entre nubes, tráiler latino 1:48 | `#4C1F25` 28% · `#986461` 18% · `#B68370` 16% · `#65505B` 16% · `#220B17` 12% · `#971E24` 10% (rojo de la armadura de Baymax) | ✅ medido, clip x889whz 1:48 |
| Vuelo del grupo al atardecer sobre nubes, tráiler latino 1:55 | `#6954A7` 24% · `#514B94` 22% · `#404174` 20% · `#8262BD` 14% · `#5657D0` 12% · `#A57CDE` 9% | ✅ medido, clip x889whz 1:55 — **corrige** el «atardecer dorado» de memoria de la sección 6: en esta toma concreta el cielo es **morado-azulado**, no dorado; el dorado sí aparece en otras tomas de ciudad (sección 6, sin medir todavía) |

`estilo.py` clasifica las seis tomas como **sombreado degradado/pintado, poca
línea** (no hay contorno duro tipo anime), saturación 43-50%, brillo 34-65%:
consistente con render 3D fotorrealista de Hyperion, no cel-shading.

### Punto 9 · Música y sonido

- **Lista completa de la BSO confirmada** (antes la biblia sólo tenía el
  nombre de una pista con ⚠️): 19 pistas de Henry Jackman + «Immortals» (Fall
  Out Boy) = 20 temas, 53:57 en total. Orden real: Immortals (3:16) · Hiro
  Hamada (1:57) · Nerd School (2:12) · Microbots (1:46) · Tadashi (1:46) ·
  **Inflatable Friend** (1:56, la activación de Baymax) · Huggable Detective
  (1:35) · The Masked Man (1:29) · One of the Family (1:49) · Upgrades (2:27)
  · The Streets of San Fransokyo (4:08) · To the Manor Born (1:15) · So Much
  More (3:01) · First Flight (2:35) · **Silent Sparrow** (4:39, la más larga
  después del tema de acción: por el nombre y el orden, es la música de la
  muerte de Tadashi) · Family Reunion (2:39) · **Big Hero 6** (6:57, tema de
  acción, el más largo: batalla final) · **I Am Satisfied with My Care**
  (5:29, la frase final de Baymax: tema del cierre/despedida) · Signs of Life
  (1:14) · Reboot (1:48) ✅ ([Wikipedia, wikitext de la ficha del álbum](https://en.wikipedia.org/wiki/Big_Hero_6_(soundtrack)),
  contrastado con [AllMusic](https://www.allmusic.com/album/big-hero-6-original-motion-picture-soundtrack--mw0002772854)).
  Edición japonesa añade «Story» (versión en inglés) de **Ai**, publicada
  aparte por EMI/Disney ✅ (misma ficha de Wikipedia).
- **«Immortals» (Fall Out Boy) suena en la escena de entrenamiento/montaje**
  (cuando Hiro y los «nerds» arman sus trajes y se convierten en superhéroes)
  y otra vez en los **créditos finales** ✅ (dos fuentes de reseña/fandom
  citadas por el buscador: [Dubbing Database](https://dubdb.fandom.com/wiki/Immortals_(Big_Hero_6)),
  vídeos de la escena en YouTube «Big Hero 6: Immortals – Movie Scene»).
  Audio oficial del single completo (240 s, MP3 160k) en Internet Archive:
  https://archive.org/details/fall-out-boy-immortals-official-music-video-from-big-hero-6-160k
- **Dato curioso confirmado**: en la película suena un fragmento instrumental
  de **«Eye of the Tiger»** (Survivor), que NO está en el álbum de la BSO ✅
  ([The Tufts Daily, reseña de estreno](http://tuftsdaily.com/arts/2014/11/12/big-hero-6-succeeds-box-office),
  citado también en el wikitext de Wikipedia). Útil como referencia de tono
  (montaje motivador) sin poder usar la canción por derechos.
- **Diseño de sonido de Baymax**: el equipo evitó pitidos electrónicos de
  robot a propósito para que sonara «achuchable»; el sonido de Baymax
  moviéndose se hizo con una **pelota de ejercicio que chirría** (Skywalker
  Sound + Disney Sound), no sonidos sintéticos ⚠️ (una sola fuente hallada,
  no pude abrir el artículo completo, sólo el resumen del buscador):
  [Disney Digital Studio Services, «The Baymax Buzz»](https://www.disneydigitalstudio.com/the-baymax-buzz-behind-the-mix-of-big-hero-6/).
  Encaja con lo que se oye en los clips vistos arriba: pasos con «chirrido de
  globo/hule», nunca bips.
- **Onomatopeyas reconocibles**: «¡Ay!» (Hiro, dispara la activación) y el
  «ba-la-la-la-la» de los dedos de Baymax en el choque de puños (frase
  hablada, no escrita en pantalla; no encontré una onomatopeya de cómic
  oficial para ese gesto — lo digo como «no encontré», no como que no
  exista).
- **Serie de TV, opening real** — Sí hay opening propio: intro de *Big Hero
  6: The Series* (Disney XD), tema de **Adam Berry** ✅ ya citado en la
  biblia; lo miré con fotogramas.py, clip «Season 3 Intro» (Dailymotion,
  0:33): https://www.dailymotion.com/video/x7we0ri
  - 0:03-0:06 — el círculo rojo del botón de Baymax se ilumina y se funde con
    su silueta (mismo lenguaje visual que la película) ✅ (visto).
  - 0:07-0:09 — Baymax abraza a Hiro; encuadre en panal hexagonal rojo/dorado
    (motivo gráfico propio de la serie, distinto del filme) ✅ (visto).
  - 0:15-0:25 — paneles hexagonales con cada héroe en acción (GoGo velocidad,
    Wasabi cuchillas de plasma verde, Fred forma naranja, Honey Lemon esfera
    rosa) ✅ (visto): confirma la paleta más saturada de la serie frente al
    filme (útil para el investigador de imagen, punto 15/16).
  - 0:32 — logo final «BIG HERO 6 THE SERIES» sobre panal rojo ✅ (visto).

### Punto 10 · Vídeos (con minuto exacto)

**Tráiler oficial latino** «Grandes Héroes – Tráiler oficial en español
latino» (sensacinemx, Dailymotion, 2:31, el primer teaser, va pegado a un
avance de *Ralph, el Demoledor*): https://www.dailymotion.com/video/x889whz
Lo miré entero con `fotogramas.py --cortes` (92 fotogramas). Momentos con
minuto real:
- 0:16-0:33 · logo Disney y "Ralph El Demoledor" (con el que compartió sala) ✅.
- 0:39-1:00 · presentación de Baymax en el cuarto de Hiro, escala de dolor,
  HUD de escaneo en inglés todavía (el doblaje no traduce el texto en
  pantalla) ✅.
- 1:00-1:16 · quema del incendio del SFIT sugerida (nubes negras, sirenas),
  Hiro llega a la comisaría, Baymax aparece detrás del mostrador (gag) ✅.
- 1:25-1:49 · montaje de los microbots, hologramas verdes, el traje rojo de
  Baymax completo, primer despegue ✅.
- 1:51-2:05 · vuelo sobre San Fransokyo, el grupo completo en el aire ✅.
- **Textos en pantalla, en español** (para el investigador de texto):
  «MUY PRONTO» (0:51) · «UN GRAN DESCUBRIMIENTO LLEGARÁ» (0:58) · «ÉL NOS
  GUIARÁ» (2:02) · «ÉL NOS CUIDARÁ» (2:06) · «ÉL CAMBIARÁ NUESTRO MUNDO»
  (2:10) · logo final «GRANDES HÉROES» en rótulo rojo con bisel blanco
  (2:21) ✅ (visto, tipografía condensada en mayúsculas, la misma familia que
  el logo de EE.UU. con letras traducidas).
- Otros tráilers latinos del mismo estudio, por si el redactor quiere más
  cortes: «Grandes Héroes Tráiler (3)» https://www.dailymotion.com/video/x889whh ·
  «6 Grandes Heroes Trailer 2» https://www.dailymotion.com/video/x2ez5rq ·
  «Grandes Héroes: Tráiler Oficial» (Tomatazos) https://www.dailymotion.com/video/x8x29d6

**Escena eliminada oficial** (ver punto 2) y **featurette** «Animating
Baymax» (Internet Archive, mp4 directo, 104 s, canal Disney vía FilmIsNow):
https://archive.org/details/youtube-koKlm22FLk0 — no la analicé fotograma a
fotograma (es más del punto 18, técnica, del investigador de texto), la dejo
anotada para que la use.

**Tendencias TikTok** (ya estaban en la biblia con ✅, las dejo, añadí
contexto de minuto donde pude sin poder abrir TikTok desde aquí — sigue
⚠️ el minuto exacto dentro de cada TikTok):
- «Estoy satisfecho con mi cuidado» sigue siendo tendencia de nostalgia.
- Retos de doblaje de SDV: relevante para el servidor (es de doblaje).

### Punto 14 · Poses analizadas (con fotograma y minuto reales; sustituye lo «de memoria»)

**Baymax** (clip Meet Baymax salvo que se diga otra cosa):
| # | Momento | Postura, manos, mirada | Sirve para |
|---|---|---|---|
| 1 | 0:09, botón rojo se enciende | primer plano del pecho, sin postura corporal aún | activar/encender |
| 2 | 1:02, escala de dolor | de pie, brazos abajo, pecho iluminado de frente | **explicar** |
| 3 | 1:12, escaneo | cabeza inclinada hacia Hiro, una mano apoyada en su hombro | **pensar** / revisar |
| 4 | Fist Bump ending, 0:21 | puño levantado despacio, imitando el gesto de Hiro, cabeza ladeada | **celebrar** (versión formal, con armadura) |
| 5 | Low Battery, 0:25 | pasos irregulares, brazos sueltos a los lados, cuerpo inclinado | batería baja / cómico |
| 6 | Low Battery, 0:44 | de frente, chocando por accidente con Hiro, brazos hacia adelante | mismo gag, gesto de disculpa |
| 7 | Clímax, 1:26 | de pie firme tras la batalla, un brazo (puño) extendido saludando | **animar** / cerrar |
| 8 | Poses con esqueleto visible (Kevin Nelson, ya citado) | referencia de articulaciones | construir cualquier pose |

**Corrección**: quito la pose «Batería baja con Mochi… chiste de lámina 2» de
la lista de Baymax: es del corto *Big Chibi 6* (2019, ver punto 2), no de la
película; si se quiere usar para lámina, debe citarse como «serie/corto»,
no como «película».

**Hiro:**
| # | Momento | Postura | Sirve para |
|---|---|---|---|
| 1 | Meet Baymax, 0:01-0:07 | de pie junto a la ventana con persiana, luego se acerca a la cama, gesto de sorpresa | reacción inicial |
| 2 | Meet Baymax, 1:17 | agachado tras la cama, cara de susto (Baymax gigante encima) | **sorpresa/miedo cómico** |
| 3 | Fist Bump ending, 0:21 | de pie, puño extendido hacia Baymax, torso ligeramente inclinado hacia adelante | **celebrar** |
| 4 | Low Battery, 0:44 | sujeta a Baymax por el brazo intentando llevarlo al cargador | **guiar/ayudar** |
| 5 | Clímax, 0:56-1:06 | sujeto al brazo del traje morado, cayendo, mirada hacia abajo, cuerpo en tensión | **acción/dramático** (no para #soporte) |

**Tadashi**: sigo sin clip propio suyo en Dailymotion/IA con acción clara (el
storyboard de la escena eliminada lo muestra de espaldas, sin cara). Las
poses 1-3 de la sección 15 de la biblia (presentar a Baymax, vídeo de prueba,
anima a Hiro) **siguen sin verificar con vídeo**: quedan ⚠️ de memoria, ahora
explícito. Búsquedas hechas sin resultado: «Tadashi Hamada scene clip»,
«Tadashi lab Baymax clip» (Dailymotion e IA sólo devuelven el storyboard de
arriba y clips de terceros sin él en plano).

**Equipo (bonus, visto en el clímax, útil para láminas de grupo — no pedido
explícitamente en el punto 14 pero surgió al mirar el vídeo):**
- Fred, 0:24: agachado, boca abierta escupiendo fuego, brazos hacia atrás — **defender/atacar**.
- Honey Lemon, 0:30: brazo extendido lanzando la esfera química rosa — **actuar/resolver**.
- Wasabi, 1:26 (de pie tras la batalla): postura relajada, sin cuchillas activas — **descansar/celebrar**.

## Lo mejor para la lámina

- El **botón rojo del pecho de Baymax** (0:09 del clip Meet Baymax) y la
  **escala de dolor de 10 caras** (1:02, mismo clip) son la referencia más
  literal para la "tabla del dolor" del canal #soporte: son el objeto real
  de la serie que ya cumple esa función.
- El **choque de puños final** (0:21, clip Fist Bump, Baymax con armadura
  verde) es mejor pose de "cierre de ticket resuelto" que el clásico
  (no verificado en vídeo).
- Paleta cálida de madera/rojo de la **cocina Lucky Cat** (hex medidos arriba)
  para un fondo de "canal cálido, de confianza" si se usa el café en vez de
  un hospital genérico.
- El **HUD de escaneo azul** (1:53, Meet Baymax) da una referencia real de
  interfaz para mostrar datos del ticket (coordinar con el investigador de
  texto).
- La **escena del portal/clímax** (colores fuego-naranja, rosa químico,
  morado) sirve como paleta secundaria de "acción" si el canal necesita un
  fondo dinámico.

## No encontré

- **Minuto absoluto dentro de la película completa** (102 min) para ninguna
  escena: sólo tengo minuto **relativo al clip** citado, porque no bajé la
  película entera (así lo pide AYUDANTE.md: «sin bajar el vídeo entero»).
  Búsquedas hechas: el archivo completo existe en Internet Archive
  (`1080_20260525`, 1080.mp4, 6112 s) pero no lo usé para recortar tramos
  porque los clips sueltos de Dailymotion/IA ya cubrían las escenas
  necesarias con menos riesgo y menos peso; queda como opción para quien
  necesite el minuto exacto de la version íntegra.
- **Choque de puños "clásico"** de mitad de película (el de "ba-la-la-la-la")
  como clip suelto: no apareció en Dailymotion ni Internet Archive.
  Búsquedas: «Big Hero 6 fist bump clip», «Big Hero 6 ba-la-la-la clip»,
  «Big Hero 6 teach fist bump». Sólo salió el del final (usado arriba).
- **Clip propio de Tadashi** (presentación de Baymax, vídeo de prueba) en
  Dailymotion/IA: no lo encontré. Búsquedas: «Tadashi Hamada clip»,
  «Tadashi Baymax lab scene», «Tadashi test video Big Hero 6». Sólo la
  escena eliminada (storyboard, sin cara de Tadashi visible) y fan art.
- **Segunda fuente completa** para el diseño de sonido de Baymax (pelota que
  chirría): el artículo de Disney Digital Studio Services no cargó su texto
  completo (posible contenido cargado por JavaScript); sólo tengo el resumen
  del buscador. Búsqueda hecha: «Big Hero 6 sound design Baymax squeaky
  exercise ball Skywalker Sound» — otras fuentes (Sound & Picture) dieron
  error de conexión (Cloudflare). Queda ⚠️ una sola fuente.
- **Minuto exacto dentro de cada vídeo de TikTok**: TikTok no se puede abrir
  desde este servidor (como YouTube). Sin cambios respecto a la biblia.

## Bitácora de búsqueda (segunda pasada, red abierta)

- Confirmado: YouTube bloquea con «Sign in to confirm you're not a bot» (probado con yt-dlp en `yl8yriCIzCE`).
- Dailymotion, API `api.dailymotion.com/videos?search=`, en inglés: «Big Hero 6 Baymax hello», «Big Hero 6 fist bump», «Big Hero 6 flying scene San Fransokyo», «Big Hero 6 Immortals», «Big Hero 6 low battery Mochi», «Big Hero 6 flight scene official», «Big Hero 6 microbots garage clip», «Big Hero 6 The Series opening intro», «Big Hero 6 The Series clip», «Baymax Returns short film».
- Dailymotion, en español: «Big Hero 6 trailer latino», «Grandes Heroes trailer español», «Baymax escaneando a Hiro», «Big Hero 6 escena».
- Internet Archive, `advancedsearch.php?q=title:(Big Hero 6)`: 30 resultados revisados; elegí la escena eliminada (`youtube-wnDrECylMOU`), el featurette (`youtube-koKlm22FLk0`) y el single de Immortals.
- Descargados y mirados con `fotogramas.py --cortes`: x2553ox, x3wn7x2, x31z3kn, x283k45, x7vbgp7, wnDrECylMOU, x889whz (tráiler latino, 92 fotogramas), x7we0ri (intro serie), x7x6uz7 (clip serie).
- Colores medidos con `estilo.py` sobre 6 fotogramas extraídos con `--fotograma` de los clips ya vistos.
- WebSearch (2 búsquedas de las ~50 del cupo): «"Big Hero 6" "Immortals" scene montage armor training which scene plays» → confirma escena de entrenamiento + créditos; «Big Hero 6 sound design onomatopoeia Baymax sound effects boop foley» → diseño de sonido de Baymax.
- Wikipedia vía API REST y `action=parse&prop=wikitext` (en inglés): ficha del álbum de la BSO completa, con las 20 pistas y el dato de «Eye of the Tiger» sin publicar.
- Fandom de Big Hero 6 (`bighero6.fandom.com/api.php?action=query&list=search`) y `action=parse&pageid=` para verificar que la escena de Mochi es del corto *Big Chibi 6* y no de la película.
- Archivos borrados al terminar cada hoja: los `.mp4` de `/tmp/claude-0/trabajo/08-video/clips/` (quedan las hojas y `indice.json`, más ligeros).

## Cumplimiento de mis puntos (2, 4, 9, 10, 14)

| Punto | Estado | Por qué |
|---|---|---|
| 2 · Escenas icónicas | ✅ | 6 escenas de la película + 1 de la serie, todas con fotograma y clip vistos de verdad; corregí un dato mal atribuido (Mochi) |
| 4 · Sitios, luz y paleta | ✅ | 6 tomas con hex medidos con Pillow (`estilo.py`) sobre fotogramas reales, ya no «a ojo» |
| 9 · Música y sonido | ✅ | Lista completa de la BSO (20 pistas) con dos fuentes, escena de «Immortals» confirmada, dato de «Eye of the Tiger», diseño de sonido de Baymax (⚠️ una fuente), opening de la serie visto y descrito |
| 10 · Vídeos | ✅ | Tráiler latino completo visto y desglosado (92 fotogramas, minuto y texto en pantalla), escena eliminada y featurette anotados |
| 14 · Poses por personaje | ⚠️ | Baymax e Hiro con 5-7 poses reales (fotograma+minuto); Tadashi sigue sin clip propio pese a buscar — queda ⚠️ de memoria, explicado en «No encontré» |

Sigue: nada obligatorio pendiente de mis puntos (2, 4, 9, 10, 14). Si hay más
presupuesto: buscar un clip propio de Tadashi (sin éxito hasta ahora) y medir
paleta de 2-3 tomas más de ciudad de día (todas las que medí son de interior
o de noche/atardecer).
