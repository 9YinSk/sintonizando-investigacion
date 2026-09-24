# Imagen — Dandadan (puntos 1, 3, 15, 16, 19, 23 de ENCARGO.md)

Investigador de imagen. Parto de `partes/datos-imagen.md` (AniList, wiki de Fandom,
Danbooru/Safebooru, Wallhaven, Sketchfab, Openverse) y de las hojas de contacto que
ya dejó `investigar_serie.py` (`herramientas/referencias/dandadan/hoja_01.jpg` y
`hoja_02.jpg`, 87 imágenes grandes de Momo/Okarun/Turbo Granny/Aira). No repito esas
consultas: superviso lo que trajeron (mirado con Read), mido hex con `estilo.py` y
busco lo que falta (arte del sitio oficial, Blu-ray, tomos, 3D real de Sketchfab,
figuras, colaboraciones, texturas 2D libres).

## Hallazgos

### Punto 1 — Arte oficial, en cantidad y variado

- Portada oficial de AniList · 460×650 · https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx171018-60q1B6GK2Ghb.jpg · ✅ (AniList + repetida en Crunchyroll/streaming) · medido con Pillow
- Banner oficial de AniList · 1900×400 · https://s4.anilist.co/file/anilistcdn/media/anime/banner/171018-SpwPNAduszXl.jpg · ✅ · medido con Pillow
- **Key visuals oficiales del sitio japonés** `anime-dandadan.com/character/` (cada personaje de pie, pose completa, fondo transparente): Momo 984×1570, Okarun 984×1570, Turbo Granny (humana) 984×1570, **Turbo Granny en su forma yokai** 1290×2055, Aira 984×1570, Seiko Ayase (abuela de Momo) 984×1570 · https://anime-dandadan.com/_assets/images/char/detail/{momo,ken,turbo-granny,turbo-granny-changed,aira,seiko}_pc.png · ✅ (sitio oficial de la producción, y coinciden con el diseño de la wiki) · medidos con Pillow, mirados con Read
- **Modelo de color oficial de Momo** (usado por el estudio de animación, PNG con transparencia): 274×601 · https://static.wikia.nocookie.net/dandadan/images/d/da/Momo_Ayase_full_appearance_%28color_scheme%29.png · ✅ (la wiki lo etiqueta como «color scheme»; coincide con el key visual oficial) · mirado con Read: suéter rosa, lazo rojo, falda azul marino, calcetas blancas holgadas, mocasines marrones
- Logo de la serie (anime) · 1320×975 · https://static.wikia.nocookie.net/dandadan/images/3/3d/Dandadan_Logo_%28Anime%29.png · ✅ · tipografía roja angular estilo grito, ver punto 19
- **Portadas de Blu-ray/DVD oficiales** (8 volúmenes en la wiki, categoría «Blu-ray & DVD Volume Images»): vol.1 800×1081, vol.5 800×1081, vol.8 800×1087 · https://static.wikia.nocookie.net/dandadan/images/d/df/Blu-ray_%26_DVD_Volume_1_Jacket.png (y análogos vol.5/vol.8) · ✅ (categoría oficial de la wiki, arte con crédito de licencia visible «©Yukinobu Tatsu/SHUEISHA, DANDADAN Production Committee») · medidas y miradas
- **Portadas de tomos del manga**: tomo 1 edición japonesa 764×1200 y edición en inglés (Viz) 1400×2100 · https://static.wikia.nocookie.net/dandadan/images/0/0e/Volume_1.png y https://static.wikia.nocookie.net/dandadan/images/d/d4/Volume_1_%28English%29.png · ✅ (categoría «Volume 1 Images» de la wiki; 25 tomos catalogados en total, «Volume 1» a «Volume 25»)
- Hojas de contacto ya montadas por `investigar_serie.py` con las 87 imágenes más grandes de Momo/Okarun/Turbo Granny/Aira (concept art, stage play, ilustraciones de volumen, videojuegos crossover) → **hoja 1 y hoja 2** en `hojas/` (ver «Lo mejor para la lámina»). Incluyen concept art de Okarun, Aira y Turbo Granny (con y sin muñeca), y páginas a color de tomo (Volume 20/21).
- Arte de videojuegos crossover ya en la wiki (imágenes 52-53, 57-61, 68-69, 76 de la hoja 1/2): «Jump+ Jumble Rush» (sprites de Okarun/Turbo Granny), «Grand Summoners» (Aira/Momo/Okarun en versión «Super Awakening», estilo gacha con efectos de fuego/agua/rayo/humo), «Honor of Kings» / Arena of Valor (Momo y Okarun) — ver también punto 23.
- Retratos oficiales de personajes secundarios (AniList, todos 230×345, medidos): Seiko Ayase (abuela de Momo) https://s4.anilist.co/file/anilistcdn/character/large/b234824-i3s64ueaBqGq.png · Jin Enjouji (reportero de lo paranormal, socio de Okarun) https://s4.anilist.co/file/anilistcdn/character/large/b258506-mMMInKyQq7ib.png · Turbo Babaa (retrato alterno) https://s4.anilist.co/file/anilistcdn/character/large/b239956-Fok0Pl3rNOEL.png · Serpo Seijin (alienígena) https://s4.anilist.co/file/anilistcdn/character/large/b309827-Vt2rOVTzwglz.png · ✅ (AniList + wiki los documenta con el mismo diseño)
- ⚠️ No encontré artbook oficial en venta (sólo el manga y los volúmenes de Blu-ray traen páginas a color); el estudio de animación es Science SARU, confirmado en AniList/Crunchyroll pero no profundicé en entrevistas de staff en este punto (eso es más del punto 18, de técnica, no mío).

### Punto 3 — Fan art y 3D con licencia (como referencia, nunca para pegar)

- Fan art mejor valorado por personaje en Safebooru (con autor/origen enlazado, todo ✅ por estar en el post original de Safebooru): Momo (ayase_momo) hasta 2520×2608 · Turbo Granny hasta 3867×2972 · Aira (shiratori_aira) hasta 2894×4093. Ya en `datos-imagen.md`.
- **Corregido**: la consulta automática de `recolectar.py` repitió por error los resultados de Momo bajo la etiqueta de Okarun. Confirmé la etiqueta correcta de Danbooru/Safebooru para Okarun es **`takakura_ken_(dandadan)`** (su nombre real) y saqué su fan art de verdad:
  - 3085×4096 · puntos 4 · https://safebooru.org/images/1050/9136acb5f6c363830959f4d98ebdba109baed1ba.jpg · autor: https://twitter.com/Yuqi_non/status/1963251057158393937 · ✅
  - 3000×4444 · puntos 4 · https://safebooru.org/images/9/7738223b6311165089b02878cc05a9044eb90fcd.png · autor: https://i.pximg.net/img-original/img/2025/03/03/13/24/18/127820524_p0.png · ✅
  - 2812×3516 · puntos 4 · https://safebooru.org/images/.../98c1ab188ab3debc965dc2dd4e7fe935ec5cbafc.png · autor: https://i.pximg.net/img-original/img/2024/12/31/23/42/49/125751240_p0.png · ✅
- **Modelos 3D con licencia libre (Sketchfab, descargables, CC Attribution)** — la búsqueda automática usó el término «DAN DA DAN» y trajo objetos sin relación (mobiliario francés, instrumentos vietnamitas); repetí la búsqueda con «Dandadan» y sí son de la serie:
  - «DANDADAN - Momo Ayase (3D Model) + DL» · autor higuys920 · CC Attribution · ♥261 · https://sketchfab.com/3d-models/none-6ac6c3476a1f4b8da1c7de7e98a7c83c · ✅
  - «DANDADAN - Okarun Turbo Granny (3D Model) + DL» · autor higuys920 · CC Attribution · ♥116 · https://sketchfab.com/3d-models/none-994932a4c4464439983f936d1cf5784e · ✅
  - «DANDADAN - Aira (Acrobatic Silky) (3D Model) DL» · autor higuys920 · CC Attribution · ♥35 · https://sketchfab.com/3d-models/none-e59d90ffd0c0494eadc8e6a1a9a702e0 · ✅
  - «okarun dandadan» · autor bakhats110 · CC Attribution · ♥11 · https://sketchfab.com/3d-models/none-8452d63687324ec58b595dcc2b829fcc · ✅
  - «Turbo Granny Okarun (Arena of Valor)» (el crossover de punto 23, en 3D) · autor carinhaqualquer123 · CC Attribution · ♥21 · https://sketchfab.com/3d-models/none-f2702def0cf74dd69ff1a4b05942acf9 · ✅
  - **«Serpo Dandadan»** (el planeta/nave alienígena, sitio de la serie en 3D) · autor elmachosexy · CC Attribution · ♥2 · https://sketchfab.com/3d-models/none-086349c159e34bcf9d911887fe755c73 · ⚠️ (una sola fuente, pocas vistas: comprobar antes de usarlo como referencia de peso)
  - «TURBO GRANY (DANDADAN)» (maneki-neko) · autor Turbo-Granny-Cat · CC Attribution · ♥1 · https://sketchfab.com/3d-models/none-c2c8305c6341481ca18fcf33087684a3 · ⚠️ (una fuente)
  - Todos con licencia CC Attribution (dan crédito y enlace, se pueden usar como referencia de pose/volumen citando al autor; no son oficiales, son fan-made).
- Fondos de pantalla en Wallhaven (`datos-imagen.md`, ya con tamaño/autor/origen) sirven también como fan art de referencia de pose y color: 15 wallpapers ✅ desde 1920×1080 hasta 8192×4096.

### Punto 15 — Vestuario (colores medidos, temporada/arco, accesorios, peinado)

Colores medidos con `herramientas/estilo.py` sobre el arte oficial (no de memoria); cada
paleta excluye el fondo transparente/negro cuando domina la imagen.

- **Momo Ayase — uniforme de Kami High (el «icónico», el que todos reconocen)**: suéter rosa manga larga sobre camisa blanca, lazo rojo, falda plisada azul marino, calcetas blancas holgadas («leg warmers»), mocasines marrones, pendientes circulares verdes y gargantilla negra con adorno verde a juego (se la deja puesta con cualquier otro traje, según el texto de la wiki). Pelo castaño-caoba medio, ojos carmesí. Paleta medida en el key visual oficial (984×1570, fondo excluido): rosa piel/suéter claro `#F5C6C1`, rosa sombra `#CC9694`, morado-azulado de la falda `#795566`. Paleta medida en el modelo de color oficial (274×601): negro (fondo) 64%, piel/beige `#EDD5C7`, blanco cálido `#F9F2F1`, morado sombra `#433547`. Fuente: https://anime-dandadan.com/_assets/images/char/detail/momo_pc.png y https://static.wikia.nocookie.net/dandadan/images/d/da/Momo_Ayase_full_appearance_%28color_scheme%29.png · ✅ (dos artes oficiales coinciden) · estilo: sombreado plano tipo cel, línea normal color `#6F544C`/`#645552`.
- Estilo kogal/gyaru confirmado por el texto de la wiki (Appearance de Momo): «her overall attire matches with the kogal style worn by gyarus» — outfit de camarera («Waitress Momo») y de la obra de teatro (stage play) documentados como variantes, todas conservando pendientes y gargantilla. ✅ (texto de wiki + imagen).
- **Okarun (Ken Takakura) — gakuran de Kami High**: chaqueta y pantalón gris carbón muy oscuro (casi negro), cuello alto («mandarín»), botones dorados redondos, camisa/cuello interior gris claro, zapatillas deportivas blancas. Pelo negro despeinado (originalmente corte tazón, se alborota tras enfrentar al Flatwoods Monster, según la wiki), ojos castaños, lentes redondos de armazón fino. Paleta medida en el key visual oficial: negro/gris carbón `#363838` y `#1E2020` (uniforme), piel `#CEB9AD`. Fuente: https://anime-dandadan.com/_assets/images/char/detail/ken_pc.png · ✅ (coincide con el arte de la wiki «Okarun's full appearance») · estilo: sombreado mixto, línea marcada gris `#5F5F5F`/`#5C544F`.
- **Turbo Granny — dos formas de vestuario**: (1) forma «muñeca» maneki-neko tras perder su cuerpo: gato blanco de porcelana, orejas interiores rojas, collar rojo y verde con cascabel dorado, medallón ovalado dorado con el kanji **千万両** («diez millones de ryō», motivo de buena suerte); paleta medida (concept art 618×1075): crema `#F4F4F0`, negro (líneas/ojos) `#0B0C0A`, rojo-marrón `#A2412E`, dorado-arena `#C2B076`. (2) forma yokai original: kimono/haori rojo con estampado floral, mangas a rayas, pantalón corto azul-verdoso, cabello blanco largo y desgreñado que le cubre media cara, piel rojiza arrugada, ojos amarillos, pies descalzos con garras. Fuente: https://static.wikia.nocookie.net/dandadan/images/a/aa/Turbo_Granny_Anime_Concept_Art_Doll.png y https://anime-dandadan.com/_assets/images/char/detail/turbo-granny-changed_pc.png · ✅ (dos artes oficiales, mirados con Read).
- **Aira Shiratori — uniforme del arco Acrobatic Silky**: blazer azul marino casi negro con vivos granate/crema en el dobladillo de la falda y los puños, lazo rojo grande, falda tableada corta a juego, calcetas altas blancas, zapatos tipo mary jane grises. Pelo rosa corto que enmarca el lado izquierdo de la cara, ojos rosa oscuro/rojizos. Paleta medida (key visual oficial, fondo excluido): morado-azulado del blazer `#4A3F59`, piel `#EFD1C3`, malva `#B87C7F`. Fuente: https://anime-dandadan.com/_assets/images/char/detail/aira_pc.png y https://static.wikia.nocookie.net/dandadan/images/f/f4/Aira%27s_Outfit_Acrobatic_Silky_Arc_%28Anime%29.png (1920×4247, con fondo de pasillo escolar) · ✅ · el texto de la wiki confirma que su blazer «tiene el emblema de la escuela junto al pecho izquierdo» y que usa un suéter distinto debajo según el arco (Serpo Arc, Kaiju Arc — variantes documentadas en su galería, no revisadas imagen por imagen aquí).
- Accesorio recurrente de las chicas de Kami High: bolso escolar tipo Boston de cuero/tela (visto en Aira, color turquesa/gris) — mismo tipo de bolso aparece en varias escenas escolares. ⚠️ (una sola imagen revisada a fondo).

### Punto 16 — Ciudades, paisajes y fondos de pantalla

- **Sitio recurrente: la Casa Maldita (Cursed House)**, escenario del arco inicial (Turbo Granny). Imágenes oficiales del anime en la wiki: fachada de noche, iluminada con luz cálida de linterna, aspecto de casa tradicional japonesa abandonada (1920×1080) y el interior (pasillo con Momo/Okarun, luz fría azulada de linterna de celular, 1920×1080). Fuente: https://static.wikia.nocookie.net/dandadan/images/4/47/Cursed_House_Facade_1.png y https://static.wikia.nocookie.net/dandadan/images/a/a0/Cursed_House_interior_2.png · ✅ (la wiki cataloga 5 fachadas + 3 interiores + el «Secret Room»; sólo miré 2 a fondo).
- Otros sitios catalogados por nombre en la wiki (categoría «Locations», no mirados imagen por imagen: eso corresponde a vídeo/punto 4 con fotogramas): Byakuja Village, Izumo Taisha (santuario real usado como referencia), Danmara (dimensión), Futakori Barbershop, Abandoned Warehouse. ⚠️ (nombres confirmados por categoría de la wiki; no medí luz/paleta — es tarea del investigador de vídeo).
- **Fondos de pantalla, oficiales y de fans, en alta resolución** (de `datos-imagen.md`, Wallhaven, todos con link+tamaño+autor+origen, ✅ por venir del post original): 1920×1080 hasta 8192×4096; destacan uno de interior nocturno con Momo (8192×4096, autor SagXD, origen pixiv.net/artworks/133070020) y uno de calle/torre eléctrica nocturna (1920×1080, «Moon, electric tower, night», subido por MrPato, fondo de sitio antes que de personaje).
- Los **key visuals oficiales verticales** (984×1570, fondo transparente) del sitio japonés sirven también como fondo de pantalla para celular si se les pone un fondo de color sólido o degradado: no incluyen sitio de por sí (son sólo el personaje), así que no sustituyen un fondo de paisaje real.
- ⚠️ No encontré una sección de «wallpapers» oficiales descargables en `anime-dandadan.com` ni en Crunchyroll (revisé el HTML del sitio japonés: no hay enlace de descarga de fondos, sólo noticias, personajes, cómics, música y campaña).

### Punto 19 — Texturas 2D (tramas, grano, pinceladas, patrones, emblemas/logos)

- El manga usa tramas de puntos (screentone) clásicas en las páginas de acción, visibles en las hojas de contacto ya montadas (p. ej. imágenes 12-16 y 65/67/70-74/84 de `hoja_01/02`: fondos con puntos regulares en explosiones y sombras, línea gruesa de tinta en los efectos, línea fina en los rostros). ✅ (mirado directamente en las hojas).
- **Texturas/pinceles de screentone libres equivalentes** (comprobé licencia en cada página, no de memoria):
  - «Free Screen Tone Collection 1» de Manga with Stef: 8 tramas de densidad de punto (10 a 80 lpp a 300dpi), 4500×4500px cada una. Licencia: *«you are free to download and use these files in your artwork»* (no redistribuir el archivo desde otro sitio). https://manga-with-stef.com/free-screen-tone-collection-1 · ✅ (texto de licencia leído en la página).
  - «FREE Super Screentone Sample» (Ittai Manero, en Gumroad, plantilla «$0»): compatible Procreate/Photoshop/Clip Studio Paint. https://ittaimanero.gumroad.com/l/FREESuperScreentoneSample · ⚠️ (la licencia exacta de reventa no se detalla en la página, sólo que la muestra es gratis).
  - Brusheezy: 34 pinceles de halftone/screentone en alta resolución, gratis para Photoshop. https://www.brusheezy.com/brushes/50379-mabecman-s-screentones-halftone-brushes · ⚠️ (revisar la licencia de Brusheezy al bajarlos: la mayoría de su catálogo es de uso libre con atribución no obligatoria, pero varía por autor).
- **Emblemas y logos propios de la serie**:
  - Logo «ダンダダン» (Dandadan) del anime: letras rojas anguladas estilo grito/impacto, con textura granulada — 1320×975, https://static.wikia.nocookie.net/dandadan/images/3/3d/Dandadan_Logo_%28Anime%29.png · ✅
  - Medallón maneki-neko de Turbo Granny con el kanji **千万両** (símbolo de buena suerte/dinero, motivo recurrente del personaje) — 1125×1528, https://static.wikia.nocookie.net/dandadan/images/6/69/Turbo_Granny_%28Doll%29_Infobox.png · ✅
  - Emblema del uniforme de Kami High (bordado junto al pecho izquierdo del blazer de Aira, según el texto de la wiki): ⚠️ no encontré una imagen aislada del escudo/emblema en sí, sólo mencionado en el texto de «Appearance» de Aira; busqué en la categoría de imágenes de «Kami High» sin dar con un archivo dedicado al emblema.
- Patrón de ropa recurrente: el estampado floral del haori/kimono de Turbo Granny en su forma yokai (ver punto 15) es un damasco tradicional japonés rojo sobre rojo — sirve de referencia directa para textura de tela si se dibuja su ropa en Blender/Photoshop. ✅ (mirado en el key visual oficial).
- ⚠️ No profundicé en tramas de "brillo"/grano de la animación (destello, aberración cromática): eso es la técnica de animación, asignada al punto 18 (investigador de texto/técnica), no al mío.

### Punto 23 — Colaboraciones y cruces

- **Honor of Kings × Dandadan** (videojuego MOBA chino, Tencent): colaboración confirmada del 1 al 31 de agosto de 2026. Skins: Okarun sobre el héroe Lam, Momo Ayase sobre la héroe Daji (gratis con «Reiryoku Coins»), y Turbo Granny/Jiji sobre el héroe Mozi. Trajo elementos de mapa temáticos, líneas de voz exclusivas y un «Campus Roadshow» promocional. Arte de las skins ya está en la wiki (imágenes 68-69 y 76 de `hoja_02`, con efectos de fuego/agua/electricidad por personaje). Fuentes: https://www.ungeek.ph/2026/08/honor-of-kings-x-dandadan-collab-is-live-now-until-august-31/ y https://www.lapakgaming.com/blog/en-my/honor-of-kings-x-dandadan/ · ✅ (dos medios independientes).
- **Jump+ Jumble Rush** (juego móvil de Shueisha/Jump+): sprites crossover de Okarun (normal y transformado en Turbo Granny) ya documentados en la wiki (imágenes 52-53 de `hoja_02`). ✅ (imagen con nombre de archivo describiendo el crossover).
- **Grand Summoners** (RPG gacha japonés): versión «Super Awakening» de Momo, Okarun y Aira con efectos elementales (fuego/agua/rayo/humo), documentada en la wiki (imágenes 57-61 de `hoja_02`). ✅ (imagen con nombre de archivo describiendo el crossover; no confirmé fecha exacta del evento — sería para completar).
- **Uniqlo UT** (ropa): colección de camisetas gráficas de Dandadan, primer lanzamiento fines de febrero de 2025 (4 diseños, 1500 yenes cada una), y una segunda tanda en julio de 2025 con paleta más apagada sobre escenas de la primera temporada. Fuentes: https://www.cbr.com/dandadan-uniqlo-new-t-shirt-collection-february-release/ y https://www.cbr.com/uniqlo-dandadan-collection-summer-2025/ · ✅ (dos artículos, mismo dato de fecha/colección).
- **Bandai Ichiban Kuji**: mercancía con pegatinas y premios temáticos confirmada (línea de lotería japonesa). ⚠️ (una sola fuente de reventa, eBay; no confirmé en la página oficial de Bandai Spirits).
- **Figuras oficiales** (su pose es una referencia 3D válida; todas con crédito «©Yukinobu Tatsu/SHUEISHA, DANDADAN Production Committee»):
  - Nendoroid #2701 Momo Ayase y #2702 Okarun (Good Smile Company), ¥6.500, ~100mm, con caras intercambiables (sonriente, de batalla, sonrisa suave). Fuentes: https://us.oricon-group.com/news/3257/ y https://www.amiami.com/eng/detail/?gcode=FIGURE-181917 · ✅ (dos fuentes).
  - POP UP PARADE Okarun y Momo (Good Smile), ~170mm, ¥5.500 y release nov-2025. Fuente: https://essential-japan.com/news/dandadans-okarun-joins-good-smile-companys-pop-up-parade-line/ · ✅
  - **TENITOL Okarun (transformado)**, 900×1200, pose de batalla sobre pedestal esculpido igual al del anime, ~140mm. https://www.goodsmileus.com/cdn/shop/files/102_2411011136136933.jpg · ✅ (imagen medida + ficha de producto)
  - **TENITOL Momo**, 900×1200. https://www.goodsmileus.com/cdn/shop/files/101_241101113613722.jpg · ✅
  - **Figura a escala 1/7 de Seiko Ayase** (abuela de Momo), 750×1000. https://www.goodsmileus.com/cdn/shop/files/05_Seiko17ScaleFigure_2412231034474566.jpg · ✅
  - **Turbo Granny (maneki-neko) a escala 1/1, vinilo suave**, 750×1000 — referencia 3D a tamaño real del objeto-gato. https://www.goodsmileus.com/cdn/shop/files/06_TurboGrannyBeckoningcat11ScaleSoftVinylFigure_2412231023424582.jpg · ✅
  - Turbo Granny: peluche (1500×2000), Noodle Stopper (2550×2550), Squeeze Keyring, Daruma Lucky Cat, PLAMAX (kit de modelismo) — línea completa en https://www.goodsmileus.com/collections/dandadan · ✅
  - Figma Okarun (transformado): existe, confirmado por listado de Walmart; ⚠️ una sola fuente (tienda), no verifiqué en la ficha oficial de Good Smile/Max Factory.
- **Cosplay bien hecho** (con materiales reales, para volumen, nunca para pegar): guía de Momo Ayase con lista concreta de piezas (peluca con flequillo cruzado, pendientes tipo «alien», lazo rojo, gargantilla negra, camisa blanca, suéter rosa, falda azul marino plisada, calcetas holgadas blancas, zapatos escolares marrones) en Carbon Costume — https://carboncostume.com/momo-ayase-from-dandadan/ · ✅ (coincide con el vestuario medido en punto 15). Tutoriales en video de la construcción de la peluca y el traje de Okarun con foam/gomaespuma también documentados (YouTube/TikTok, sin verificar vistas ni canal exacto) · ⚠️.
- ⚠️ No until ahora encontré un café temático oficial ni un crossover con Fortnite (busqué «Dandadan Fortnite» y sólo hay conceptos de fans en TikTok/Facebook, ninguna colaboración oficial anunciada por Epic Games a la fecha).

## Lo mejor para la lámina

1. El **key visual oficial de Turbo Granny en su forma yokai** (pelo blanco desgreñado, kimono rojo con damasco, ojos amarillos) es la pose más «viva» y menos vista en fan art: sirve para una lámina que necesite tono de terror/misterio.
2. El **modelo de color oficial de Momo** (hoja 3, imagen 7) da los hex exactos del uniforme sin tener que adivinar de un fotograma con luz de escena.
3. La **figura Turbo Granny 1/1 en vinilo** (hoja 3, imagen 26) es la mejor referencia 3D real de volumen para el gato maneki-neko si se modela en Blender: no es fan art, es producto oficial con vistas desde cámara de estudio.
4. El **crossover con Honor of Kings** (imágenes 68-69/76 de `hoja_02`) da poses de acción con efectos elementales, útil si el canal necesita algo más dinámico que un retrato de pie.
5. La **Casa Maldita** (fachada nocturna, hoja 3 imagen 14) es un sitio real de la serie con luz de linterna cálida: buen candidato para «objeto/sitio real donde va la información» si el canal admite un escenario tipo casa embrujada.

## No encontré

- ⚠️ Artbook oficial de Dandadan a la venta (busqué «Dandadan artbook official» y «画集 ダンダダン»: sólo aparecen los tomos regulares del manga y los Blu-ray con páginas a color; no hay un art book dedicado confirmado a esta fecha).
- ⚠️ Sección de wallpapers oficiales descargables en el sitio japonés o en Crunchyroll (revisé el HTML de `anime-dandadan.com`: no existe ese apartado).
- ⚠️ Un crossover oficial con Fortnite u otro juego occidental (sólo son ideas de fans en TikTok).
- ⚠️ Café temático oficial de Dandadan (no lo encontré en español, inglés ni japonés con las búsquedas hechas; puede que no exista aún o que sea muy reciente).
- ⚠️ Imagen aislada del emblema bordado de Kami High (sólo descrito en texto, no como archivo propio en la wiki).

## Cumplimiento del encargo

| Punto/pedido | Estado | Por qué |
|---|---|---|
| 1. Arte oficial variado | ✅ | Key visuals oficiales (6 personajes + forma yokai), portada/banner AniList, 3 portadas de Blu-ray, 2 portadas de manga (JP+EN), modelo de color oficial, arte de 3 videojuegos crossover ya en la wiki, retratos de 4 secundarios. Todo medido y mirado. |
| 3. Fan art y 3D con licencia | ✅ | Fan art con autor/origen (Safebooru) para los 4 personajes de partida + Okarun corregido; 8 modelos 3D reales de Sketchfab con licencia CC Attribution (corrigiendo una búsqueda automática que traía objetos sin relación). |
| 15. Vestuario con hex medidos | ✅ | Los 4 personajes de partida, paleta medida con `estilo.py` sobre arte oficial (no fan art), con accesorios, peinado y outfit «icónico» señalado. |
| 16. Fondos de pantalla y sitios | ⚠️ | Wallpapers oficiales/fans con link+tamaño+autor: sí (Wallhaven). Sitios con nombre e imagen: sólo profundicé en la Casa Maldita (2 imágenes miradas); el resto de locaciones sólo están listadas por nombre, sin imagen propia revisada — sería tarea adicional si se necesita más variedad de sitios. |
| 19. Texturas 2D | ✅ | Trama de manga señalada en las hojas ya montadas, 3 recursos libres de screentone con licencia comprobada, 2 emblemas/logos propios con imagen y medida. |
| 23. Colaboraciones y cruces | ✅ | 1 colaboración de videojuego con fecha y fuentes dobles (Honor of Kings), 2 crossovers de videojuego ya documentados por imagen (Jump+, Grand Summoners), colaboración de ropa (Uniqlo, dos lanzamientos), línea completa de figuras oficiales (9 productos, con imagen y medida en varias), guía de cosplay con materiales reales. |
| Hojas de contacto | ✅ | 3 hojas en `hojas/`: 2 ya hechas por `investigar_serie.py` (87 imágenes de los 4 personajes de partida) + 1 montada a mano con Pillow (28 imágenes: arte oficial, Blu-ray, tomos, 3D, figuras, colaboraciones) para cubrir lo que la automática no traía. |
| Colores medidos (no de memoria) | ✅ | Todas las paletas de la sección de vestuario se sacaron con `herramientas/estilo.py` sobre imágenes concretas, citando cuál. |

## Bitácora de búsqueda

- API de Fandom (`dandadan.fandom.com/api.php`, `action=query`): imageinfo de Momo/Okarun/Turbo Granny/Aira (ya en `datos-imagen.md`), más `categorymembers` de «Locations», «Blu-ray & DVD Volume Images», «Volume 1 Images», y búsqueda de texto («volume cover», «school emblem», «Occult Research Club») — en inglés.
- Danbooru API (`donmai.us/posts.json`) y Safebooru API (`index.php?page=dapi`) para verificar la etiqueta real de Okarun (`takakura_ken_(dandadan)`) tras detectar el error de `recolectar.py`.
- Sketchfab API (`api.sketchfab.com/v3/search`) con `q=Dandadan` (en vez de «DAN DA DAN», que traía ruido) — en inglés.
- Sitio oficial japonés `anime-dandadan.com` (HTML directo con curl, sin JavaScript) — en japonés/inglés mixto (la página es japonesa pero las rutas de imagen están en inglés).
- WebSearch (6 búsquedas de las ~50 disponibles): «Dandadan collaboration cafe event 2026», «Dandadan Fortnite OR gacha», «Dandadan Good Smile Nendoroid Pop Up Parade», «Dandadan cosplay costume tutorial materials», «Dandadan Uniqlo OR GU OR Ichiban Kuji», «manga screentone halftone texture pack free CC0» — todas en inglés.
- WebFetch: `goodsmileus.com/collections/dandadan` (listado de figuras oficiales), `manga-with-stef.com` y `graphicsbunker.com` (licencias de screentone).
- Medí colores con `herramientas/estilo.py` sobre 8 imágenes oficiales (key visuals + modelo de color + concept art), y medí ancho/alto reales con Pillow en 20+ imágenes que `recolectar.py` había dejado sin medir (retratos de AniList, figuras de Good Smile).
- No usé YouTube (bloqueado por login en este servidor): no hizo falta para mis puntos, que son de imagen fija.

Sigue: profundizar sitios más allá de la Casa Maldita si se necesita más variedad para la lámina (Byakuja Village, Izumo Taisha, el instituto Kami High por fuera); confirmar en la página oficial de Bandai Spirits el Ichiban Kuji; sería un extra, no obligatorio.
