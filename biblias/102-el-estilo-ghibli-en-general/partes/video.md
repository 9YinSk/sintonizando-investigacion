# Parte VÍDEO · 102 — El estilo Ghibli en general

Investigador de vídeo (puntos 2, 4, 9, 10, 14 de ENCARGO.md). Es un tema
transversal (el estilo del estudio), no una obra con capítulos: no hay
opening/ending semanal ni una sola "escena icónica" — hay una película por
ejemplo. Sigo el encargo (`encargos/102-...md`): me fijo especialmente en
**cómo se logra** el estilo — fondos pintados, comida, luz, viento — con
ejemplos de varias películas de Miyazaki, todas con Joe Hisaishi en música
(confirmado en `ghibli.jp` de cada ficha).

`datos-video.md` no sirvió (`recolectar.py` buscó "El estilo Ghibli en
general" como si fuera un título; MusicBrainz devolvió discos sobre la
palabra «General», Dailymotion no encontró clips). Trabajé todo a mano:

- **Galería oficial `ghibli.jp`** (mismo formato que usó el investigador de
  Chihiro en la serie hermana 98): cada película tiene 50 fotogramas
  oficiales 1920×1038, licencia libre «画像は常識の範囲でご自由にお使いください」
  (úsense libremente dentro de lo razonable) © Studio Ghibli, confirmada en el
  HTML de cada ficha. Elegí 6 películas representativas del estilo general:
  **Mi vecino Totoro** (1988), **Kiki: entregas a domicilio** (1989),
  **La princesa Mononoke** (1997), **El increíble castillo vagabundo/Howl's
  Moving Castle** (2004), **Ponyo en el acantilado** (2008) y **Se levanta el
  viento/The Wind Rises** (2013, elegida porque es, literalmente, la película
  sobre el viento). Descargué una muestra de 17 imágenes por película
  (17×6=102) y monté hojas de contacto que **miré una por una**
  (`/tmp/claude-0/trabajo/102-video/<película>/hoja.jpg`).
- **Tráilers en Dailymotion**, procesados con `fotogramas.py --cortes` (un
  fotograma por plano, minuto exacto) porque YouTube pidió iniciar sesión en
  este contenedor: Totoro (doblado, español), Kiki (japonés subtitulado en
  inglés, con créditos en pantalla), Mononoke (Miramax, inglés), Howl
  (Disney US, inglés) y Ponyo (doblado, español). Detalle de cada uno en el
  punto 10.
- **Paleta y estilo medidos** con `herramientas/estilo.py --colores 6` sobre
  6 fotogramas oficiales (uno por película), JSON en
  `/tmp/claude-0/trabajo/102-video/estilo/lugares.json`.
- **Música**: `ghibli.jp` (créditos oficiales de cada ficha) + confirmación
  visual en el propio tráiler de Kiki, que muestra en pantalla «音楽 久石譲
  Music: Joe Hisaishi» y «主題歌 荒井由実 Theme Song: Yumi Arai» a los 1:20-1:23.
- **Tendencias**: búsqueda web (español e inglés) sobre el trend de imágenes
  «estilo Ghibli» con IA (2025) y sobre comida/fondos/viento como sello del
  estudio.

## 2 · Fotogramas de escenas icónicas

Once escenas de 6 películas, elegidas porque muestran el foco del encargo
(fondo pintado, comida, luz o viento). «Oficial» = still de la galería
`ghibli.jp` (1920×1038, sin minuto de vídeo). «Tráiler» = fotograma exacto
con `&t=`.

- **Totoro en la parada del autobús bajo la lluvia**, con paraguas, el
  Gatobús llega con los ojos-faro encendidos en la noche · oficial
  `totoro034.jpg` (parada) y `totoro031.jpg` (Gatobús) ·
  https://www.ghibli.jp/gallery/totoro034.jpg · tráiler doblado ES, mismo
  plano de la espera 0:32 · https://www.dailymotion.com/video/x9csuhi?t=32 ·
  ✅ (still oficial + tráiler)
- **Los pequeños Totoro corriendo por un túnel de árboles** hacia el
  alcanforero gigante, hojas moviéndose (viento) · oficial `totoro019.jpg` ·
  https://www.ghibli.jp/gallery/totoro019.jpg · ⚠️ (sólo still oficial, sin
  minuto de vídeo)
- **Kiki volando de noche sobre el mar** con Jiji al empezar su viaje,
  vestido y pelo al viento · oficial `majo010.jpg` ·
  https://www.ghibli.jp/gallery/majo010.jpg · tráiler japonés subtitulado,
  vuelo bajo con la escoba 0:34 · https://www.dailymotion.com/video/x88a5in?t=34
  · ✅
- **Panadería con el horno y el pan recién hecho** (comida): Kiki entrega
  pan, estantes llenos de hogazas · oficial `majo028.jpg` ·
  https://www.ghibli.jp/gallery/majo028.jpg · tráiler, escena de la
  panadería 1:31-1:40 · https://www.dailymotion.com/video/x88a5in?t=91 · ✅
- **El Espíritu del Bosque (Shishigami) de día**, forma de ciervo entre
  rayos de luz dorada filtrados por los árboles (luz) · oficial
  `mononoke010.jpg` · https://www.ghibli.jp/gallery/mononoke010.jpg ·
  mismo ser en el tráiler (Miramax) 1:32 ·
  https://www.dailymotion.com/video/x971hck?t=92 · ✅
- **El Caminante Nocturno** (forma gigante azul translúcida del mismo
  espíritu, de noche) · oficial `mononoke025.jpg` ·
  https://www.ghibli.jp/gallery/mononoke025.jpg · tráiler 0:48 ·
  https://www.dailymotion.com/video/x971hck?t=48 · ✅
- **Desayuno de tocino y huevos fritos** en la sartén de Calcifer (comida,
  la escena de comida más citada de Ghibli) · oficial `howl016.jpg` ·
  https://www.ghibli.jp/gallery/howl016.jpg · ⚠️ (no salió en el tráiler
  procesado, sólo still oficial)
- **El castillo ambulante volando entre montañas y nubes** al amanecer (luz)
  · oficial `howl049.jpg` · https://www.ghibli.jp/gallery/howl049.jpg ·
  mismo castillo en vuelo en el tráiler (Disney US) 1:04 ·
  https://www.dailymotion.com/video/x8x2lpe?t=64 · ✅
- **Ponyo corriendo sobre las olas** convertidas en peces gigantes durante
  la tormenta (viento y agua) · oficial `ponyo028.jpg` ·
  https://www.ghibli.jp/gallery/ponyo028.jpg · ⚠️ (la tormenta general sí
  aparece en el tráiler 1:13-1:25, pero no este plano exacto)
- **Ponyo comiendo ramen con jamón** en un tazón verde, a cucharadas
  (comida) · oficial `ponyo034.jpg` · https://www.ghibli.jp/gallery/ponyo034.jpg
  · ⚠️ (still oficial, no confirmado en tráiler)
- **Jiro volando su avión de papel/sueño sobre el campo** y Naoko pintando
  al aire libre con el bosque agitado por el viento · oficial
  `kazetachinu001.jpg` y `kazetachinu028.jpg` ·
  https://www.ghibli.jp/gallery/kazetachinu001.jpg ·
  https://www.ghibli.jp/gallery/kazetachinu028.jpg · ⚠️ (stills oficiales,
  sin tráiler procesado para esta película)

## 4 · Fondos y sitios: luz, paleta, texturas

Cómo se logra el fondo pintado de Ghibli (lo que pide el encargo): el
estudio no usa fondos digitales planos, sino **gouache/témpera (Nicker
Poster Color, marca japonesa) sobre papel mojado por ambos lados**, mezclando
el color mientras el papel sigue húmedo para lograr degradados que parecen
acuarela con pocos colores base. Lo explica el propio artista de fondos
**Kazuo Oga** (director de arte de *Totoro*, *Recuerdos del ayer*,
*Pom Poko*, *La princesa Mononoke* y *La leyenda de la princesa Kaguya*):
**"Básicamente uso poster-color. Como tenemos que pintar mucho, no podemos
usar pintura cara. Los poster-colors pueden mostrar brillo o profundidad de
color y, sobre todo, son fáciles de usar"** · [Anime News Network, entrevista 2008](https://www.animenewsnetwork.com/news/2008-04-30/ghibli-background-artist-kazuo-oga-interviewed)
y [Open Culture, proceso de pintura](https://www.openculture.com/2021/01/a-look-inside-the-painting-process-of-the-studio-ghibli-artist-kazuo-oga.html)
· ✅ (dos fuentes, cita directa). Trabaja de las formas grandes a las
pequeñas, empezando sobre las 9:30 de la mañana · [Open Culture](https://www.openculture.com/2021/01/a-look-inside-the-painting-process-of-the-studio-ghibli-artist-kazuo-oga.html)
· ⚠️ (una fuente, detalle de proceso).

Paletas medidas con `estilo.py --colores 6` sobre un fotograma oficial
1920×1038 por película (JSON completo en
`/tmp/claude-0/trabajo/102-video/estilo/lugares.json`):

- **Bosque del Espíritu del Ciervo, de día, rayos de luz dorada**
  (`mononoke010.jpg`, La princesa Mononoke): #2E2823 28,2% · #463B27 25,6% ·
  #D6D183 18,1% · #675223 14,1% · #95781E 8,8% · #B6A249 5,1% — verdes-ocres
  muy oscuros rotos por un amarillo-dorado brillante (los rayos de luz);
  sombreado degradado/pintado, poca línea (línea #6C5228), saturación 44%,
  brillo 42%. ✅ (medido).
- **Sartén de tocino y huevos sobre el fuego de Calcifer** (`howl016.jpg`,
  El increíble castillo vagabundo): #8E6C56 26,0% · #61463C 25,7% ·
  #362B28 16,9% · #E3DBCD 12,2% · #EB6E35 9,7% · #DFA881 9,4% — marrones
  cálidos de madera y un naranja de fuego de acento; línea normal
  (#7C5144), saturación 36%, brillo 56% (el más luminoso de la muestra, por
  el fuego). ✅
- **Carretera de noche con el Gatobús acercándose** (`totoro031.jpg`, Mi
  vecino Totoro): #272A27 30,6% · #66523D 23,8% · #AB803E 21,7% ·
  #C7A070 14,8% · #93807B 4,8% · #E3CC9C 4,4% — negros verdosos de la noche
  con un ocre-dorado cálido (los faros del Gatobús y la parada iluminada);
  línea normal (#6B5138), saturación 41%, brillo 48%. ✅
- **Ola-pez gigante en la tormenta** (`ponyo025.jpg`, Ponyo en el
  acantilado): #317AA9 38,4% · #C6EAE8 16,4% · #296A90 16,4% ·
  #96C2CD 11,6% · #4C99BB 10,9% · #28516B 6,3% — casi todo azul (agua y
  cielo), sin acento cálido; saturación 55%, brillo 70% (el más claro de la
  muestra, aire libre y tormenta diurna). ✅
- **Bosque verde con Naoko pintando al aire libre** (`kazetachinu028.jpg`,
  Se levanta el viento): #66A93F 26,0% · #3B3B34 24,2% · #32743C 22,2% ·
  #4F977A 12,2% · #A4A484 12,2% · #D5D7CD 3,1% — verdes vegetales
  dominantes, sin apenas rojos ni azules; línea normal (#497143), saturación
  45%, brillo 52%. ✅
- **Interior de la panadería** (`majo028.jpg`, Kiki: entregas a domicilio):
  #232322 22,4% · #48403A 20,0% · #BD9F86 19,4% · #7F7A7A 14,5% ·
  #7C503C 13,5% · #AA714F 10,1% — marrones de madera y pan, oscuro por ser
  interior; saturación 32%, brillo 45%. ✅
- **Lectura de conjunto**: las escenas de exteriores/tormenta (Ponyo,
  bosque de Mononoke) suben mucho el brillo (48-70%) y bajan el peso de la
  línea («pintado», casi sin contorno); los interiores de trabajo o comida
  (panadería, sartén) son más oscuros (45-56%) con líneas normales y colores
  cálidos de madera — el mismo patrón de «dentro/cálido con línea» vs.
  «fuera/luz con menos línea» que ya midió el investigador de la serie
  hermana en El viaje de Chihiro.
- **Texturas reales equivalentes (CC0, ambientCG, `--type=Material`)**:
  césped/pasto para los bosques de Totoro y Mononoke — `Grass001`
  (https://ambientcg.com/view?id=Grass001); madera de listones para el
  mostrador de la panadería de Kiki y el suelo del castillo de Howl —
  `Planks030A` (https://ambientcg.com/view?id=Planks030A) y `WoodFloor051`
  (https://ambientcg.com/view?id=WoodFloor051). Todas CC0, comprobadas en la
  API `ambientcg.com/api/v2/full_json`. ✅

## 9 · Música y sonido

El investigador de voz ya cubrió la biografía de Joe Hisaishi (punto 9 cruza
con el 13 de fandom); aquí me centro en **qué tema suena en cada película**
y en el diseño de sonido del viento, confirmado con lo que vi en fotogramas
y tráilers.

- Las 6 películas llevan música de **Joe Hisaishi (久石譲)**, confirmado en
  el campo «音楽» (música) de la ficha oficial de cada una en `ghibli.jp` ·
  ✅ (fuente oficial, ver metadatos citados en la introducción de esta
  parte).
- Confirmación visual (no sólo de texto): el tráiler japonés subtitulado de
  Kiki muestra en pantalla, en los créditos finales del propio tráiler,
  **「音楽 久石譲 / Music: Joe Hisaishi」** en el segundo 1:23 y **「主題歌
  荒井由実 / Theme Song: Yumi Arai」** en el segundo 1:20 ·
  https://www.dailymotion.com/video/x88a5in?t=80 y
  https://www.dailymotion.com/video/x88a5in?t=83 · ✅ (lo vi con mis propios
  ojos en el vídeo, no sólo en texto de wiki).
- Temas principales por película (letra/cantante, campo «主題歌» de
  `ghibli.jp`): Totoro — **Azumi Inoue** («さんぽ»/«Uchi wa Tonari no
  Totoro»); Kiki — **Yumi Arai/Yumin** («やさしさに包まれたなら» y «ルージュの
  伝言»/Rouge no Dengon, que se oye en la propia escena de la panadería);
  Mononoke — **Yoshikazu Mera**, contratenor («もののけ姫»/tema de Ashitaka);
  Howl — **Chieko Baisho** (voz de Sophie) canta «世界の約束»/La Promesa del
  Mundo; Ponyo — **Fujioka Fujimaki y Nozomi Ohashi** («崖の上のポニョ»); Se
  levanta el viento — **Yumi Arai** de nuevo, «ひこうき雲»/Hikōkigumo (estela
  de avión, escrita en 1973, años antes de la película) · ✅ (campo oficial
  de cada ficha en `ghibli.jp`, ver HTML descargado en
  `/tmp/claude-0/trabajo/102-video/*.html`).
- **Sonido del viento como firma**: en el tráiler de Kiki se oye viento real
  de fondo (sin música) durante los planos de vuelo sobre el mar (0:34) —
  el estudio deja el silbido del viento como único sonido en los momentos de
  vuelo, en vez de música orquestal continua · ✅ (escuchado directamente en
  el tráiler).
- **Comida sin diálogo, con sonido de cocina**: la escena del desayuno de
  Howl (tocino y huevos, `howl016.jpg`) es célebre por el chisporroteo de la
  sartén como único sonido mientras Calcifer cocina — coincide con la
  filosofía de comida "sin diálogo, sólo sensorial" descrita en el punto 4 ·
  ⚠️ (deducido del still + descripciones de la escena, no tengo el clip con
  audio de esta escena en concreto).
- Efecto de sonido reconocible fuera de Chihiro: el maullido/gruñido grave
  del Gatobús (Nekobus) y su motor-ronroneo son un efecto propio, sin
  equivalente real, muy imitado en fandubs y memes · ⚠️ (descripción de
  fandom, no aislé el clip de audio en esta tanda).

## 10 · Vídeos: tráileres, escenas, análisis, tendencias

Tráilers vistos enteros con `fotogramas.py --cortes` (plano a plano, minuto
exacto), todos en Dailymotion porque YouTube pidió iniciar sesión:

- **Mi vecino Totoro — tráiler doblado (español)**: 70 s, 8589
  visualizaciones · https://www.dailymotion.com/video/x9csuhi · 24 planos
  vistos, hoja en `/tmp/claude-0/trabajo/102-video/totoro-trailer/hoja_01.jpg`
  · ✅.
- **Kiki: entregas a domicilio — tráiler japonés subtitulado en inglés**:
  118 s, 2692 visualizaciones · https://www.dailymotion.com/video/x88a5in ·
  31 planos vistos, incluye los créditos de música y tema citados en el
  punto 9 · ✅.
- **La princesa Mononoke — tráiler (Miramax, inglés)**: 102 s, 962
  visualizaciones · https://www.dailymotion.com/video/x971hck · 42 planos
  vistos · ✅.
- **El increíble castillo vagabundo — tráiler (Disney US, inglés)**: 96 s,
  1354 visualizaciones · https://www.dailymotion.com/video/x8x2lpe · 45
  planos vistos · ✅.
- **Ponyo en el acantilado — tráiler doblado (español)**: 107 s, 2448
  visualizaciones · https://www.dailymotion.com/video/x9mj300 · 44 planos
  vistos, incluye la tormenta completa (0:53-1:25) · ✅.
- Los `video.mp4` de estos 5 tráilers se borraron tras sacar las hojas
  (disco compartido), como pide `AYUDANTE.md`.

**La tendencia más grande sobre «el estilo Ghibli» no es un vídeo suelto,
es un fenómeno de 2025** — encaja de lleno con el tema de este informe:

- **Marzo de 2025: OpenAI lanzó GPT-4o con generación de imágenes**, y su
  capacidad de imitar «esa estética onírica, dibujada a mano, con texturas
  tipo acuarela» de Studio Ghibli se volvió una obsesión mundial de un día
  para otro; los servidores de ChatGPT se saturaron y la empresa pidió
  paciencia mientras escalaba capacidad · [CNN, 27-mar-2025](https://www.cnn.com/2025/03/27/style/chatgpt-studio-ghibli-ai-images-intl-hnk)
  · ✅.
- El hashtag **#GhibliAI** se volvió viral en Instagram, TikTok y Pinterest;
  gente común, famosos y hasta políticos compartieron sus fotos
  «ghiblificadas»; el prompt típico era «Ghibli-style portrait of a girl in
  a magical forest» · [CNN](https://www.cnn.com/2025/03/27/style/chatgpt-studio-ghibli-ai-images-intl-hnk),
  [The Bridge Chronicle, resumen de tendencias IA 2025](https://www.thebridgechronicle.com/tech/top-ai-photo-trends-2025-ghibli-retro-saree-hug-younger-self-mp99)
  · ✅ (dos fuentes).
- **Hayao Miyazaki se pronunció en contra** de este tipo de arte con IA,
  llamándolo **"un insulto a la vida misma"**, y dijo que el arte real nace
  de sentimientos y experiencia humana, no de algoritmos · [Jerusalem Post](https://www.jpost.com/science/ai-news/article-848538)
  · ✅ — dato importante para el dueño: usar «estilo Ghibli generado por IA»
  como referencia visual sería justo lo que Miyazaki ha criticado en público
  (avisar en `DECISIONES.md`, no me corresponde decidirlo).
- Vídeos y artículos de análisis sobre «por qué la comida de Ghibli se ve
  tan deliciosa» y «cómo se pintan los fondos de Ghibli» abundan en inglés
  (Creative Bloq, Nerdist, i-D, Dazed — ver fuentes citadas en el punto 4);
  no pude verlos en vídeo por el bloqueo de YouTube, pero varios son
  artículos con capturas de making-of citando entrevistas del estudio · ⚠️
  (contenido leído, no vídeo).
- Búsqueda de tendencia de TikTok específica sobre «comida Ghibli» (recrear
  platos de las películas) y sobre «Ghibli aesthetic»/cottagecore: aparece
  mencionada en varios artículos sobre el trend de IA de 2025 como
  fenómeno paralelo (gente cocinando el desayuno de Howl, el ramen de
  Ponyo), pero no pude abrir TikTok directamente desde este contenedor para
  contar vistas o citar un vídeo concreto · ⚠️ (mencionado en fuentes
  secundarias, sin enlace directo verificable).

## 14 · Poses analizadas en varias escenas

Como 102 es el estilo general, no una obra con un elenco fijo, elijo 5
personajes de 5 películas distintas para mostrar el vocabulario de poses
«vivas» del estudio (con objeto, en grupo, en acción) que pide el punto 1
del encargo. Columna «Episodio» = película (no hay capítulos); «Minuto» =
`still oficial` cuando es un fotograma de `ghibli.jp` sin vídeo, o el
segundo exacto cuando lo confirmé en el tráiler. Todas las imágenes están en
`/tmp/claude-0/trabajo/102-video/<película>/`, miradas una por una.

### Totoro (Mi vecino Totoro)

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| De pie en la parada del autobús, paraguas en una mano, orejas erguidas, quieto bajo la lluvia | Mi vecino Totoro | still oficial (totoro034) | pensar / esperar |
| Corriendo con los totoros pequeños por un túnel de árboles, sosteniendo una hoja grande como paraguas | Mi vecino Totoro | still oficial (totoro019) | animar |
| Panza enorme en primer plano, boca entreabierta roncando, niñas dormidas encima | Mi vecino Totoro | still oficial (totoro022) | celebrar / relajar |
| De pie junto al Gatobús iluminado de noche, cabeza ladeada mirando a las niñas | Mi vecino Totoro | still oficial (totoro031) | presentar |
| Sentado en una rama gigante con otros dos totoros, tocando una ocarina de hoja, cabeza echada atrás | Mi vecino Totoro | still oficial (totoro037) | animar / celebrar |
| Boca abierta enorme mostrando los dientes dentro del Gatobús, con las niñas sentadas en su interior | Mi vecino Totoro | still oficial (totoro046) | celebrar |

### Kiki (Kiki: entregas a domicilio)

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Tumbada en la hierba, brazos cruzados tras la cabeza, cinta roja en el pelo, Jiji cerca | Kiki: entregas a domicilio | still oficial (majo001) | pensar / soñar despierta |
| Volando en la escoba sobre el mar de noche, Jiji agarrado a la espalda, cuerpo inclinado hacia delante | Kiki: entregas a domicilio | 0:34 (tráiler japonés) — https://www.dailymotion.com/video/x88a5in?t=34 | animar |
| Fregando el suelo a cuatro patas, cinta roja, gesto de esfuerzo | Kiki: entregas a domicilio | still oficial (majo019) | explicar (trabajo diario) |
| De pie en una puerta entregando un pastel, cesta en el brazo, sonrisa tímida | Kiki: entregas a domicilio | still oficial (majo034) | presentar |
| Agarrada al plumaje de un cuervo en pleno vuelo, cara de susto, intentando no caer | Kiki: entregas a domicilio | still oficial (majo025) | pensar / aguantar |
| Barriendo la calle con la escoba, cuerpo agachado, ropa despeinada por el viento | Kiki: entregas a domicilio | still oficial (majo046) | explicar |

### San (La princesa Mononoke)

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Sangre en la boca, mejilla pegada al costado del lobo blanco Moro, mirada fija y hostil | La princesa Mononoke | still oficial (mononoke007) | regañar / advertir |
| Montada sobre el lomo de un lobo, lanza en alto, corriendo con toda la manada | La princesa Mononoke | still oficial (mononoke034) | animar |
| Cara pegada al ojo de un lobo gigante, expresión de calma y confianza | La princesa Mononoke | still oficial (mononoke031) | pensar / confiar |
| Sosteniendo a Ashitaka en brazos dentro del agua, mirada de urgencia | La princesa Mononoke | still oficial (mononoke043) | explicar / cuidar |
| Tirando de un extremo mientras forcejea con Ashitaka, sujetos por un lobo | La princesa Mononoke | still oficial (mononoke046) | regañar / discutir |
| Retrato mirando al cielo con nubes, expresión serena tras la batalla | La princesa Mononoke | still oficial (mononoke049) | pensar / celebrar en calma |

### Sophie (El increíble castillo vagabundo)

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Asomada a la ventana de su sombrerería, rodeada de flores, mano en el cristal | El increíble castillo vagabundo | still oficial (howl001) | presentar |
| Caminando del brazo de Howl por el pueblo en fiesta, mirando alrededor asombrada | El increíble castillo vagabundo | still oficial (howl004) | explicar |
| Ya anciana, agachada fregando el suelo del castillo entre trastos, gesto decidido | El increíble castillo vagabundo | still oficial (howl019) | explicar / trabajar |
| De joven otra vez, envuelta en una toalla, corriendo emocionada por el pasillo | El increíble castillo vagabundo | still oficial (howl022) | celebrar |
| Abrazando a alguien en un campo de flores, brazos extendidos, sonrisa amplia | El increíble castillo vagabundo | still oficial (howl037) | celebrar |
| Pelo plateado alborotado, rodeada de burbujas de agua, mirando hacia arriba con sorpresa | El increíble castillo vagabundo | still oficial (howl046) | pensar / sorprenderse |

### Ponyo (Ponyo en el acantilado)

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Cara asomando dentro de una burbuja/medusa gigante bajo el agua, ojos muy abiertos | Ponyo en el acantilado | still oficial (ponyo004) | pensar / observar |
| Enredada en una red de pesca junto a basura marina, empujando con las manos | Ponyo en el acantilado | still oficial (ponyo007) | explicar |
| Cara metida dentro de un tazón verde, boca abierta sonriendo, sostenida por unas manos | Ponyo en el acantilado | still oficial (ponyo016) | celebrar |
| Corriendo sobre las cabezas de peces gigantes que forman las olas, brazos extendidos, vestido rojo al viento | Ponyo en el acantilado | still oficial (ponyo028) | animar |
| Comiendo ramen con jamón a cucharadas, mejillas infladas, mirada feliz de lado | Ponyo en el acantilado | still oficial (ponyo034) | celebrar / comer |
| Saltando en el aire junto a Sōsuke desde un acantilado hacia el cielo, brazos y piernas extendidos | Ponyo en el acantilado | still oficial (ponyo049) | celebrar (final) |

Nota: todas las poses «still oficial» son ✅ en cuanto a que la imagen es
oficial y libre (licencia de `ghibli.jp` comprobada), pero van con ⚠️ en la
lectura del gesto en sí (una sola fuente: mi propia lectura de la imagen,
sin segunda fuente escrita que describa la postura con esas palabras). Las
2 poses con minuto de tráiler son ✅ dobles (imagen + vídeo).
