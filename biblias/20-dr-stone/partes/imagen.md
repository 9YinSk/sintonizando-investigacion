# Imagen · Dr. Stone (encargo 20) — puntos 1, 3, 15, 16, 19, 23

Investigador de imagen, red abierta (24-sep-2026). Parto de `partes/datos-imagen.md`
(no repito esas consultas) y de la biblia ya escrita (`biblia.md`, secciones 3, 4,
16, 17 — todas con ⚠️ porque el equipo anterior no pudo abrir ninguna imagen).
Aquí sí las abrí y las medí. Escribo sólo aquí y en `imagen.json`; no toco
`biblia.md` (lo hace el redactor).

Formato: un dato por línea, con fuente, ✅ (dos fuentes) o ⚠️ (una), y minuto o
tamaño si aplica.

---

## Punto 3 · Fan art y 3D (sólo como referencia)

### 3.1 Modelos 3D con licencia comprobada por la API de Sketchfab

Antes decía «la licencia no se pudo leer». La comprobé con
`https://api.sketchfab.com/v3/models/<uid>` (campo `license.label`):

| Modelo | Autor | Licencia (API) | Descargable | Enlace |
|---|---|---|---|---|
| Dr. Stone \| Senku 3D Model, Environment & Props (Senku, **laboratorio**, hacha, poción, **teléfono**, bandera del Reino de la Ciencia) | jerryteng | **CC Attribution (CC BY)** ✅ | Sí | https://sketchfab.com/3d-models/dr-stone-senku-3d-model-environment-props-8dc007444003431f80e8ae69b7a0833d |
| Senku Ishigami DR Stone (327k caras) | fossyl | **CC Attribution (CC BY)** ✅ | Sí | https://sketchfab.com/3d-models/senku-ishigami-dr-stone-c1979af69a68490482a99d0a43fcf286 |
| Senku DR Stone 3d model (Blender 2.8, 22,7k tris) | leonardo.sensei2 | **CC Attribution (CC BY)** ✅ | Sí | https://sketchfab.com/3d-models/senku-dr-stone-3d-model-e7436cf85cbd483fa08e9922b69ce5f5 |
| SENKU Dr Stone | HaroldXd | **CC Attribution (CC BY)** ✅ | Sí | https://sketchfab.com/3d-models/senku-dr-stone-db3599b14a5f4aa2939b8de61e522035 |
| SUIKA MASK DR STONE (el casco de Suika) | Axel.Slaughter | **CC Attribution (CC BY)** ✅ | Sí | https://sketchfab.com/3d-models/suika-mask-dr-stone-dd63b40689b146da9858e2f1af04454e |

Son personajes con copyright: sirven **sólo para mirar pose, volumen y
proporción**, nunca para pegar el render; la licencia CC BY obliga a dar
crédito si se usa el modelo tal cual (no es el caso aquí).

### 3.2 Modelos 3D de objetos genéricos, licencia comprobada

| Para qué | Modelo | Autor | Licencia (API) | Enlace |
|---|---|---|---|---|
| Vidrio de laboratorio (matraces) | Chemistry Glassware | maxdragon | **CC Attribution** ✅ | https://sketchfab.com/3d-models/chemistry-glassware-b8594f7dc7e8442dbaaae7a11da4a962 |
| Radio antigua de válvulas (interior) | Vintage Radio 1940s | ponchoguy | **CC Attribution** ✅ | https://sketchfab.com/3d-models/old-radio-7724f81ad4e043079b7bf4b16146c087 |
| Tubo de vacío | Vacuum tube | aa050928777003 | **CC Attribution** ✅ | https://sketchfab.com/3d-models/vacuum-tube-3867ca5c3cd74cb882b22d0eee75567a |
| Megáfono (base del micro de Senku) | Megaphone | cacybernetic | **Free Standard** (no CC, uso libre en Sketchfab pero sin redistribuir el archivo) ⚠️ | https://sketchfab.com/3d-models/megaphone-afc27df368144fe892d8e22c1f4b1e8a |

**Sigue la recomendación de hacerlo a mano en Blender** en vez de bajar el
megáfono genérico: el de Senku es un cono de plástico fenólico sin pulir
(marrón, mate, con las vetas de moldeo visibles) con cristales de sal de
Rochelle pegados (prismas transparentes irregulares) — un modelo comercial
de megáfono metálico brillante no sirve de referencia real.

### 3.3 Fan art 2D — confirmado que las páginas cargan (antes no se sabía)

Comprobé con `curl` que las páginas existen (no que el dibujo sea bueno,
eso se mira):

- **DeviantArt**: [Senku Ishigami, de Jiance](https://www.deviantart.com/jiance/art/Senku-Ishigami-Dr-Stone-812555318)
  (HTTP 200 ✅) · [Kohaku Wallpaper, de dinocozero](https://www.deviantart.com/dinocozero/art/Kohaku-Wallpaper-812210990)
  (HTTP 200 ✅). Licencia DeviantArt por defecto: **todos los derechos
  reservados** — son referencia de pose/color, nunca para usar.
- **ArtStation**: hoja para colorear de Senku, de Kelvin Ellis
  (https://www.artstation.com/artwork/aoPzx9) — la página da 403 al
  comprobarla por API/curl (bloqueo anti-bot, no prueba que no exista) ⚠️.
- **Pixiv**: etiqueta [Dr.STONE](https://www.pixiv.net/en/tags/Dr.STONE) y
  la enciclopedia de personajes (千空 Senku, クロム Chrome, カセキ Kaseki) —
  ya en `datos-imagen.md`, sin abrir de nuevo (cuota de red).

### 3.4 Cosplay (referencia real de materiales y volumen)

Bajé y **miré** una de las fotos de Openverse (licencia CC BY-NC-SA 2.0,
esby.photo, Roseraie de la Beaujoire, Nantes):
https://live.staticflickr.com/65535/51772988428_88df4b0f8b_b.jpg (767×1024) ✅

Es un cosplay de **Senku muy fiel**: túnica **color crema/hueso** (no
blanca pura) con «E=mc²» pintado en el pecho, cuello levantado, vendas de
tela en los antebrazos, bolsa de tela atada al cinturón, y **botas de dos
piezas** — bota alta blanca cosida con zigzag + refuerzo de cuero marrón en
la puntera y el borde, tal como se ve en el anime. La peluca reproduce el
degradado exacto: **raíz color crema/blanco hueso y puntas verde menta**,
partida en un mechón que cae sobre la cara. Confirma a ojo el hex medido en
§15 (la túnica NO es blanca, es un crema cálido ~#F5EBD6).

---

## Punto 1 · Arte oficial, en cantidad y variado

### 1.1 Key visuals y portadas (medidos)

- Key visual **Dr. Stone Stone Wars** nº1 (Senku de pie, capa verde) ·
  2324×3277 (el más grande de los 8 de la wiki) · hoja `arte_01` nº1 ·
  https://static.wikia.nocookie.net/dr-stone/images/9/9f/Dr._Stone_Stone_Wars_Key_Visual_3.png ✅ (wiki + visible en la hoja)
- Key visual **Dr. Stone Stone Wars** nº1, otra pose (Senku con el puño) ·
  1830×2529 · hoja `arte_01` nº14 ·
  https://static.wikia.nocookie.net/dr-stone/images/1/1e/Dr._Stone_Stone_Wars_Key_Visual_1.png ⚠️ (no confirmé el nº exacto en la wiki, sólo la hoja)
- Key visual serie 1, dos variantes (grupo, 4 personajes) · 1449×2048 c/u ·
  hoja `arte_01` nº38 y 39 ·
  https://static.wikia.nocookie.net/dr-stone/images/d/d5/Dr._Stone_Key_Visual_3.png ·
  https://static.wikia.nocookie.net/dr-stone/images/e/e4/Dr._Stone_Key_Visual_4.png ⚠️ (urls reconstruidas del nombre del archivo, sin volver a pedir su imageinfo)
- **Season 2 Main Visual** · 1000×1414 · hoja `arte_01` nº40-ish (fila 4) ✅ vista en la hoja
- Portadas de **volúmenes del manga en inglés** (US Volume 8, 12, 25...) y
  japonés (Volume 4, 5, 17...), cada una vista en la hoja de contacto: son
  ilustraciones de cuerpo entero con objeto o grupo, nunca sólo de pie
  (ej. Volume 25: Senku, Chrome y Kohaku corriendo con el brazo mecánico al
  fondo) ✅ (vistas directamente, `arte_01`)
- **Banners de Weekly Shonen Jump** (portada de la revista): 2017-40,
  2018-51, 2019-31, 2020-48, 2021-02, 2021-15 · todos vistos en `settei_01`
  y `vestuario_01`, 1200×480 a 2000×800 ✅
- **Portada del fanbook** «Dr.STONE 公式ファンブック 科学王国事典» (4-ago-2022,
  Shueisha): más de 50 fichas de personaje, cronología, **hojas de ruta de
  cada invento** y preguntas a los autores ✅ (Shueisha, S-MANGA — ya en
  `datos-imagen.md`, confirmado con la wiki de capítulos)
- Portada **«Dr. STONE Speak Towards the Future»** (novela/guía) · 800×1259 ·
  hoja `settei_01` nº258 ✅ vista

### 1.2 Hojas de ruta (roadmaps): así son de verdad, ya no es un ⚠️

La biblia anterior decía «existe; el aspecto ⚠️». Lo miré: descargué
**«Roadmap Senku Spaceship.png»** (1455×1063,
https://static.wikia.nocookie.net/dr-stone/images/8/89/Roadmap_Senku_Spaceship.png)
y lo abrí. Es la doble página del capítulo de la nave: **estilo árbol de
habilidades de videojuego**. Iconos circulares o en cajas con esquinas
irregulares (tipo cómic, borde grueso) para cada material — «Rare Metals»,
«Superalloys» (Inconel, Stainless Steel, Hastelloy), «Oil», «Aluminum»,
«Liquid Oxygen Producer», «High-Power Dynamo», «Engine», «Computer» —
unidos por **flechas-tubo gruesas con relleno de tráma de puntos** (screentone)
que confluyen en el dibujo técnico del **motor del cohete** (dibujado como
maquinaria real, con pernos y líneas de sección). Cajas de texto con **rayos
de velocidad radiales** detrás («START!», «GOAL») y niveles tipo RPG
(«Level 1» → «LV. 99»). Es EXACTAMENTE el lenguaje visual que pide el canal
#hardware (una ruta de materiales hasta el aparato). ✅ (imagen vista entera)
Lo mismo aplica a **«Moon Rocket Roadmap.png»** (2036×352) y a
**«Roadmap Senku Rocket Manga.png»** (nº52 en `settei_01`), mismo estilo ✅.
Para el micrófono y el teléfono, el mismo tipo de diagrama sale en el manga
(capítulos 1×19 según Fandom) pero no lo tengo descargado aparte: el estilo
es el mismo que el del cohete (confirmado por analogía visual, no por ver
esa página exacta) ⚠️.

### 1.3 Las monedas Drago: SÍ tienen diseño (antes decía «no lo vi»)

`File:Drago Coins.png` (959×649,
https://static.wikia.nocookie.net/dr-stone/images/4/4c/Drago_Coins.png) ✅
vista entera. **Corrección**: no son «billetes», son **monedas acuñadas**
(el texto antiguo decía «billete»). Hay 4 denominaciones — 500, 1.000, 5.000
y 10.000 «$» (ドラゴ, Drago) — cada una con el **perfil grabado de un
personaje** (para la de 500, un anciano de barba larga tipo Kaseki; la de
1.000, un joven con pañuelo; la de 10.000, dos cabezas grandes juntas) y un
nombre de **aleación industrial** debajo en japonés (フェロクロム
ferrocromo, フェロモリブデン ferromolibdeno, フェロニッケル ferroníquel,
フェロニオブ ferroniobio): un chiste de guion — el dinero literalmente vale
lo que pesa en metal. Diseño grabado estilo moneda antigua, con orla de
perlitas y textura de trama de puntos en el relieve. Útil para el canal:
un «precio» del hardware podría ir en una moneda así en vez de en un
cartel. ✅

### 1.4 Objetos del canal #hardware, ahora con imagen (antes 0)

- **Roadmap del cohete** (equivalente visual al roadmap del micrófono) → §1.2.
- El **micrófono/teléfono en sí** siguen sin fotograma propio: no encontré
  una imagen fija de la wiki que los muestre de cerca (son props de
  fondo/animación, 1×23-1×24 y 2×02). **Sigue pendiente sacar fotograma**
  con `fotogramas.py` — es tarea del investigador de vídeo (punto 2), pero
  lo anoto aquí porque es el objeto central del canal.
- Staff de arte confirmado (japonés): diseño de personajes **Yuko Iwasa**
  (岩佐裕子) — también dibuja las carátulas de los Blu-ray (múltiples
  fuentes de tienda: Amazon Japan, blu-ray.com) ✅; color **中尾総子**;
  diseño de fondos **青木智由紀**; dirección de arte **吉原俊一郎** ✅ (ya
  confirmado en `datos-imagen.md`/biblia, dos fuentes).

### 1.5 Videojuego oficial: Dr. STONE Battle Craft

Confirmado con Google Play, App Store y TMS Entertainment ✅: **«Dr. STONE
Battle Craft»**, desarrollado por **Poppin Games Japan** (no Bandai Namco,
que sólo aparece como distribuidor en alguna ficha de tienda), estrategia
móvil, publicado el 1-sep-2021 en Japón y el 28-nov-2023 en Norteamérica
(Android/iOS). Las **tarjetas de personaje** («Intro Card») de Chrome, Gen,
Kaseki y Suika están en `settei_01` nº259-262: son retratos de cuerpo
entero en pose de acción con su elemento (Chrome con rayo azul, Gen con
remolino de agua, Kaseki envuelto en llamas con un martillo, Suika como
mascota-fruta saltando) sobre fondo de estrellas — **arte oficial de
videojuego con poses nuevas**, no repetidas del anime/manga. Fuentes:
https://play.google.com/store/apps/details?id=com.poppingames.dsbc ·
https://tmsanime.com/news/dr-stone-battle-craft-mobile-game-now-available-in-north-america

---
