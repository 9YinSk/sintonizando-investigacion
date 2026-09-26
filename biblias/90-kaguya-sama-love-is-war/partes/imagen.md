# Parte IMAGEN · Kaguya-sama: Love is War (encargo 90)

Investigador de imagen. Puntos de ENCARGO.md: **1** (arte oficial), **3** (fan art
y 3D con licencia), **15** (vestuario con hex medidos), **16** (fondos de
pantalla y sitios), **19** (texturas 2D), **23** (colaboraciones y cruces).
Parte de `datos-imagen.md` (poco recolectado: sólo portada/banner de AniList).

**Serie hermana (misma obra):** el encargo 43 (biblioteca, sin foco de canal)
ya tiene una parte de imagen completa y a fondo (`biblias/43-kaguya-sama-love-is-war/partes/imagen.md`,
leída entera antes de empezar). Cubre bien lo general: 6 hojas de modelo
oficiales con hex medidos, 4 modelos 3D de Sketchfab, wallpapers de Wallhaven,
texturas ambientCG/Poly Haven y colaboraciones (Oshi no Ko, Mahjong Soul,
Monster Strike, Saing, cruces de portada, cosplay, figuras Good Smile). **No
repito esos datos** (están enlazados abajo cuando hacen falta): este encargo
(90) pide fijarse **especialmente en comedia y rótulos**, así que profundizo en
arte y recursos que sirven a ESE enfoque — variantes cómicas de personajes,
gags visuales del dibujo (ojos en blanco, letreros/carteles en la propia
imagen), fan art y 3D nuevos que 43 no encontró, y colaboraciones o figuras que
43 no cubrió.

## 1 · Arte oficial, en cantidad y variado (foco: comedia)

Además de las 3 hojas de 43 (portada, cuerpo entero, grupo, boda…), monté una
hoja nueva con páginas que 43 no tocó: la personalidad cómica de Chika, el
alter ego "tonta" de Kaguya y capítulos "Talk" (los extras de humor propios de
la serie). `hojas/comedia_01.jpg` (46 miniaturas, wiki Fandom).

- **Kaguya (Moron)** — alter ego oficial de Kaguya cuando se queda en blanco
  de la vergüenza: diseño con ojos vacíos y expresión ida, arte oficial del
  anime · hoja `comedia_01.jpg` #44 "Moron Anime.png" · Fandom (página propia
  "Kaguya (Moron)", distinta de "Kaguya (Ice)" que ya tenía 43) · ✅ (wiki +
  visible también en fotogramas del anime, es un gag recurrente) · 619×841
- **Gag de "ojos en blanco"**: cuando un personaje queda pasmado o furioso, el
  dibujo le sustituye los ojos por óvalos blancos vacíos — es una firma visual
  de la serie (Aka Akasaka), no un error de compresión · hoja `comedia_01.jpg`
  #20 "173 Preview.png" (panel de manga) y #38 "176 Preview.png" (Chika con
  diadema "Demon", panel de anime) · ✅ (se repite en varios capítulos y en el
  anime) · 1214×1094 y 1198×669
- Chika Fujiwara comiendo ramen a dos manos, cara de éxtasis cómico
  ("Degustation") · hoja `comedia_01.jpg` #11-12 · Fandom · ✅ · 2048×1158 y
  2048×1154 (43 sólo la mencionaba de pasada en la hoja 1, aquí en tamaño
  completo)
- Chika con silbato en la boca y diadema **blanca** con las letras 「おに」
  ("oni" = "quien la para", el equivalente a "el que se queda" del pillapilla)
  durante un juego de gimnasia — imagen corregida: al abrir el archivo en
  grande la diadema es blanca con texto negro, no roja como anoté al primer
  vistazo de la miniatura · hoja `comedia_01.jpg` #13 "ChikaWhistle.png" ·
  Fandom, usada en `Chika Fujiwara/Image Gallery` · ✅ (imagen mirada entera,
  descargada y comprobada en `/tmp/claude-0/trabajo/90-imagen/chikawhistle.png`)
  · 1686×1329
- Retrato oficial limpio de Chika (temporada 2, fondo transparente, cuerpo
  entero) — sirve como hoja de modelo alternativa a la de 43 · hoja
  `comedia_01.jpg` #43 "Chika Fujiwara S2 (Anime).png" · Fandom · ✅ · 666×829
- Portadas de "Talk Volume" (los extras de humor/radio del propio manga, no
  parte de la trama principal): #3 "Talk Volume 04.png" ya la tenía 43; aquí
  además el spin-off doujinshi oficial interno #8 "Doujinshi Volume 1.png" y
  el especial de imagen real "Edo Period" (comedia histórica, cap. especial)
  #34 "Edo Period Anime.png" 1280×720 · Fandom · ✅ (categoría "Extra
  Chapters" de la wiki, confirmada por la API `categorymembers`)
- Anuncio de temporada 2, banner oficial 1500×500 · hoja `comedia_01.jpg` #40
  "Season 2 Announcement Banner.png" · Fandom · ⚠️ (una fuente, banner
  promocional)
- Nota: la hoja trae también portadas de doujinshi oficial para adultos (#2,
  #17-18, #21-22, #28-29, #33) — **no usar en la lámina** (contenido +18), las
  dejo listadas sólo porque `investigar_serie.py` las trajo con la galería del
  personaje.

## 3 · Fan art y 3D con licencia libre

43 ya tenía 4 modelos de Sketchfab (Kaguya, Chibi Kaguya, Chika, Miko) y la sala
del consejo. Busqué con otras combinaciones de texto (nombre en romaji sin
"kaguya-sama") y apareció un **set completo de 5 modelos del mismo autor**, con
el mismo estilo, que 43 no encontró — mejor que tener autores sueltos porque
combinan bien entre sí en un mismo render de Blender.

**Modelos 3D nuevos (Sketchfab, todos CC Attribution 4.0, verificados
`isDownloadable: true` con la API `/v3/models/<uid>`):**
Personaje | Modelo | Autor | Caras | Enlace
---|---|---|---|---
Chika Fujiwara | Chika Fujiwara 藤原千花 | maya_2023 | 121.548 | https://sketchfab.com/3d-models/chika-fujiwara-1dc4c6832d904834ab5d6c8fd40efcdf
Kei Shirogane | Kei Shirogane 白銀圭 | maya_2023 | 145.168 | https://sketchfab.com/3d-models/kei-shirogane-66b618113cb344f0afc1e9a13a4d58c9
Miyuki Shirogane | Miyuki Shirogane 白銀御行 | maya_2023 | 82.599 | https://sketchfab.com/3d-models/miyuki-shirogane-7fb8a907e2114b2cad3a45fe8ac403c7
Yu Ishigami | Yu Ishigami 石上優 | maya_2023 | 92.412 | https://sketchfab.com/3d-models/yu-ishigami-da365a42604842d093d5df14d43b47b0
Ai Hayasaka | Ai Hayasaka 早坂愛 | maya_2023 | 49.406 | https://sketchfab.com/3d-models/ai-hayasaka-3d3289eabb274ee9a64907780809114c

- Los 5 son del mismo autor (`maya_2023`), mismo estilo de escultura y textura
  → sirven juntos para una lámina de grupo cómica en Blender sin que
  desentonen entre sí, cosa que no se puede garantizar mezclando autores
  distintos · ✅ (licencia y descarga confirmadas modelo por modelo)
- Con esto y los 4 modelos de 43 (Kaguya, Chibi Kaguya, Chika alt., Miko) el
  reparto principal completo (7 personajes) tiene modelo 3D libre, algo que 43
  no llegó a completar (le faltaban Miyuki, Ishigami, Hayasaka y Kei)

**Fan art / wallpapers con licencia o etiqueta que 43 no listó (Wallhaven,
sólo SFW):**
- Grupo de 4 (Kaguya, Chika, Hayasaka, Miko) estilo semirrealista, autor
  "Wachiroku" en la etiqueta, 5032×2670, 131 favoritos · https://wallhaven.cc/w/g7dwle · ✅ (API confirma tags con los 4 nombres) · 5,67 MB
- Kaguya sonrojada y avergonzada («blushing», «embarrassed»), primer plano,
  2923×1886, 129 favoritos — encaja con el gag central de la serie (quien se
  enamora primero pierde) · https://wallhaven.cc/w/xlo59d · ✅ · 4,85 MB
- Kaguya y Hayasaka de la mano, 2250×4000, 132 favoritos · https://wallhaven.cc/w/3zvqed · ✅ · 3,57 MB

**Danbooru/Safebooru:** seguí sin resultados, igual que 43 (`donmai.us` no
responde por Cloudflare; probé además `safebooru.org` con su API de tags —
`%kaguya%` no trae ninguna variante de "shinomiya" ni "kaguya_sama": la serie
apenas tiene etiqueta propia en esos bancos). Cubierto con Wallhaven, igual
que hizo 43.

## 15 · Vestuario, colores medidos, peinado

43 ya midió el uniforme (hex del lazo, vestido, gakuran) sobre las 6 hojas de
modelo oficiales — no repito esos hex, sirven igual para este encargo (enlace:
`biblias/43-kaguya-sama-love-is-war/partes/imagen.md#15`). Añado dos variantes
que 43 dejó como ⚠️ sin medir, y que son justo las que dan la nota cómica
(disfraces de broma, no el uniforme serio):

Personaje | Prenda | Hex medido | De qué imagen
---|---|---|---
Chika Fujiwara | Uniforme de gimnasia (camiseta blanca, cuello azul marino) — variante que 43 no midió, el uniforme normal sí lo tiene | blanco ≈ #DCDCDC (con sombra de escena nocturna azulada, no es el blanco "puro" de estudio) | ChikaWhistle.png, Fandom (medido con Pillow sobre la descarga completa, no la miniatura)
Kaguya (Moron) | Piel/rostro en el gag de "modo tonta" (mismo uniforme, pelo suelto y despeinado) | igual que el uniforme normal (#342E32 blazer, ya medido por 43) — lo que cambia es sólo la cara y el pelo, no hex nuevo | Moron Anime.png, Fandom

- No encontré una imagen limpia de cuerpo entero del traje de sirvienta
  temático de Halloween/festival cultural (las tiendas de cosplay lo venden,
  pero no hay foto oficial en la wiki con fondo transparente) para medir hex
  fiable · ⚠️ (una fuente indirecta: tiendas de cosplay como Magic Wardrobes y
  CosDaddy confirman que existe el diseño de sirvienta de Hayasaka como traje,
  pero es un disfraz de fans inspirado en su uniforme de sirvienta habitual,
  no una prenda nueva de la serie)
- El gag de "ojos en blanco" (ver punto 1) no es ropa pero sí un cambio de
  dibujo repetible en cualquier personaje — anotarlo aquí porque una lámina
  cómica puede usarlo en vez de cambiar de vestuario para mostrar personalidad

## 16 · Ciudades, paisajes y fondos de pantalla

43 ya describió Shuchi'in Academy y la sala del consejo (con su modelo 3D) y
midió las texturas ambientCG de madera/alfombra/tela/papel — no lo repito.
Sumo el sitio comedia que más peso tiene fuera de la sala del consejo: el
**festival escolar**, y wallpapers nuevos.

- **Festival cultural de Shuchi'in ("Devoted Hearts Festival")** — arco 13 del
  manga (caps. 122-137), «Dual Confessions Culture Festival Arc»: puestos,
  luces, disfraces de clase · Fandom, página del arco (wikitext vía API) ·
  ✅ (wiki + lista de capítulos con sus títulos, ej. "Chapter 123: Kaguya's
  Culture Festival") — dato corregido: descarté un primer apunte sobre un
  supuesto café donde trabajaría Ishigami (no lo confirma la wiki; era un
  cruce con otra serie, fuente falsa, no lo uso)
- **Festival deportivo ("Sports Festival Arc")** — arco 9 del manga (caps.
  82-90): la escena de Chika con silbato y diadema "oni" (punto 1 y 15) es de
  este arco, no del cultural — lo até mal a primera vista y lo corrijo aquí ·
  Fandom (confirmado: existe la página "Sports Festival Arc", caps. 82-90,
  Ishigami se une al equipo de animadoras) · ✅
- No encontré en Poly Haven un HDRI de "festival nocturno con puestos y
  farolillos" que encaje con esta escena — la más cercana, "Entrance Hall",
  ya la tiene 43 para interiores; queda como hueco real, no falta de mirar
  (comprobé con la API filtrando `festival`, `market`, `lantern`, `string
  light`, sin resultado cercano) · ⚠️
- Wallpaper de grupo (4 personajes) 5032×2670, ver punto 3 — también sirve
  como fondo de pantalla, no sólo como fan art · https://wallhaven.cc/w/g7dwle

## 19 · Texturas 2D

43 cubrió screentones genéricos (GraphicsBunker, Brusheezy, Gumroad) y la
textura de papel de ambientCG. Para el **enfoque cómico** de este encargo
busco específicamente el recurso que más se repite en las escenas de humor del
manga: las **líneas de velocidad / ráfagas de impacto** (el "shock lines" que
enmarca una reacción exagerada) y el efecto de "ojos en blanco".

- Pack de 20 pinceles gratis de líneas de velocidad y foco manga (.abr, con
  JPG fuente), licencia "Free for Commercial Use (Attribution)" · MyPhotoshopBrushes
  · https://myphotoshopbrushes.com/brushes/id/3816/ · ✅ (ficha del sitio +
  licencia explícita en la descarga, sin registro) · complementa los
  screentones de 43 para el efecto de "grito"/sorpresa
- El gag de "ojos en blanco" (punto 1) se puede replicar en Photoshop con una
  capa de óvalos blancos lisos — no hace falta una textura descargada, así que
  no cuenta como pendiente, pero sí queda documentado como técnica repetible.

## 23 · Colaboraciones, cruces, figuras oficiales y cosplay

43 ya cubrió Oshi no Ko, Mahjong Soul, Monster Strike, Saing, cruces de
portada y figuras Good Smile de escala/Pop Up Parade — no lo repito. El
enfoque de este encargo (rótulos/comedia) encaja con dos cosas que 43 no
tocó: los **stickers oficiales de LINE con voz** (rótulos cómicos literales,
hechos para chat) y los **Nendoroid con placas de cara intercambiables**
(la misma idea de "una cara por emoción" que pide el punto 17 de la guía IA).

- **Stickers oficiales de LINE con voz** — 24 diseños, 250 yenes, publicados
  el 23-jun-2020 por Aniplex: frases/momentos icónicos como «お可愛いこと»
  ("Qué mona...", muletilla de Kaguya) y «ドーンだYO!» (grito de Chika), con
  voces nuevas grabadas para el pack · Aniplex oficial
  (aniplex.co.jp/lineup/kaguya04) + Dengeki Hobby Web + collabo-cafe.com ·
  ✅ (dos fuentes, japonés) — es la referencia más directa a "rótulos": son
  literalmente frases + expresión + voz pensadas para usarse como reacción en
  texto, igual que pediría la lámina de un canal de edición/doblaje
- Segunda tanda de stickers («かぐやちゃん», Rare Kaguya chibi) ligada a la
  película "First Kiss That Never Ends" · aniplex.co.jp (noticia oficial) ·
  ⚠️ (una fuente, no crucé fecha exacta)
- **Nendoroid Kaguya Shinomiya** (#1288, Good Smile Company): 3 caras
  intercambiables (sonrisa normal, «qué mona…» y «¡qué lindo!» al ver a
  Shirogane con orejas de gato), incluye el teléfono plegable, orejas de gato
  y **cartelas de texto de escenas famosas** para recrear momentos —
  literalmente placas de rótulo de cartón dentro de la caja · goodsmile.com/en/product/6955
  + Kahotan's Blog (mikatan.goodsmile.info) · ✅ (dos fuentes oficiales) —
  la pose de pie con uniforme es buena referencia 3D; las cartelas de texto
  son referencia directa de cómo la propia franquicia diseña sus "rótulos"
- **Nendoroid Yu Ishigami** (Good Smile, ligado a la película): 3 caras
  intercambiables — neutra, llorando, y su frase meme «Cállate, idiota»
  (うるせえ、バカ野郎) · goodsmile.com/en/product/11986 + varias tiendas
  oficiales autorizadas (Kappa Hobby, P-Rex Hobby) que repiten la misma ficha
  · ✅ (dos fuentes) — Ishigami es el personaje secundario con más presencia
  de meme/cita cómica reconocible, encaja con «quizá un secundario es más
  querido» de las reglas del dueño

**Cosplay adicional (más allá de la foto CC BY-SA de Chika que ya tiene 43):**
No encontré más fotos de cosplay con licencia libre clara (Openverse repite
el mismo lote de 43); las tiendas de disfraces (Miccostumes, EZCosplay,
CosDaddy) no dan licencia de imagen, sólo sirven para ver cortes de tela —
anotado en «No encontré».

## Lo mejor para la lámina

- Set de 5 modelos 3D CC-BY del mismo autor (Chika, Kei, Miyuki, Ishigami, Hayasaka) que completan el reparto de 43: https://sketchfab.com/3d-models/yu-ishigami-da365a42604842d093d5df14d43b47b0
- Nendoroid Kaguya con cartelas de texto de escenas y 3 caras — referencia directa de "un rótulo por emoción": https://www.goodsmile.com/en/product/6955/Nendoroid+Kaguya+Shinomiya
- Nendoroid Ishigami con su cara-meme «Cállate, idiota», el secundario más citado: https://www.goodsmile.com/en/product/11986/Nendoroid+Yu+Ishigami
- Stickers oficiales de LINE con voz (24, con frases icónicas) como referencia de tono y de cuadro de diálogo cómico: https://www.aniplex.co.jp/lineup/kaguya04/news/detail/?id=62824
- Kaguya (Moron), alter ego oficial de ojos vacíos del anime, y el gag de "ojos en blanco" repetido en manga y anime: hoja `comedia_01.jpg` #44 y #20/#38

## No encontré

- Danbooru/Safebooru: bloqueado por Cloudflare (igual que constató 43);
  probé también `safebooru.org` (API de tags, `%kaguya%`) y no hay ninguna
  etiqueta de la serie — el fandom de fan art de esta obra parece vivir más
  en Pixiv/Twitter que en esos bancos.
- HDRI de Poly Haven para un festival nocturno con puestos y farolillos (el
  escenario cómico del arco 13): no existe uno cercano en su catálogo
  (comprobado con la API, filtros `festival`, `market`, `lantern`).
- Foto de cosplay con licencia libre del disfraz de sirvienta de Hayasaka o de
  algún disfraz del festival cultural: sólo tiendas de venta de disfraces
  (Miccostumes, CosDaddy, EZCosplay), sin licencia de imagen aprovechable.
- Trama a cuadros para el lazo (ya lo dijo 43): sigue sin hacer falta, se
  genera en Photoshop.
- Búsquedas hechas (además de las de la bitácora): «Nendoroid Kaguya Shinomiya
  Good Smile faceplates» (en), «Nendoroid Yu Ishigami dead fish eyes» (en),
  «Kaguya-sama culture festival maid costume cosplay» (en), «かぐや様は告らせたい
  LINEスタンプ 公式» (ja), «free manga speed lines impact brushes CC0» (en). No
  llegué a buscar en coreano/chino por límite de tiempo de esta tanda.

## Bitácora

- Leída entera `biblias/43-kaguya-sama-love-is-war/partes/imagen.md` (24 mil
  caracteres) antes de empezar, para no repetir consultas ni datos.
- `herramientas/investigar_serie.py --wiki kaguyasama-wa-kokurasetai --paginas
  "Kaguya (Moron)" "Nagisa Kashiwagi" "Go Kazamatsuri" "Chika Fujiwara"`: 106
  imágenes enlazadas, 46 grandes → 1 hoja (`comedia_01.jpg`), mirada entera.
- Fandom API `list=categorymembers&cmtitle=Category:Omake` y `Category:Extra
  Chapters` (en): confirma que "Talk Chapter" y "Doujinshi Chapter" son los
  extras cómicos oficiales de la serie.
- Fandom API `action=parse&prop=wikitext` sobre "Episode 33", "Episode 7", "Yu
  Ishigami", "Dual Confessions Culture Festival Arc" (en): para verificar (y
  descartar, en el caso del café) datos de ambientación antes de darlos por
  buenos.
- Sketchfab API (`v3/search` con `chika fujiwara`, `shirogane kaguya`,
  `ishigami kaguya`, `hayasaka kaguya`, en): 5 modelos nuevos del mismo autor,
  confirmados uno a uno con `v3/models/<uid>`.
- Wallhaven API (`atleast=1920x1080`, `purity=100`, ordenado por favoritos, en):
  15 resultados, comprobados 5 con el detalle `/api/v1/w/<id>` para tags y
  tamaño real; 3 no estaban en la parte de 43.
- Danbooru (`donmai.us`) y Safebooru (`safebooru.org` API de tags) (en):
  sin resultados para la serie, igual que constató 43.
- Poly Haven API (`assets?t=hdris`): filtros `class/school/library/hall/cafe`
  y `festival/market/lantern/string_light` (en) — "Comfy Café" encontrado
  pero descartado al no confirmarse la escena; sin resultado para festival.
- WebSearch (ja/en): Nendoroid Kaguya y Nendoroid Ishigami (faceplates),
  disfraces de festival/cosplay, LINE stickers oficiales, pinceles de líneas
  de velocidad — 5 búsquedas.
