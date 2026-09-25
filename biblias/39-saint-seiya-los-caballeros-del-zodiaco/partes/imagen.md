# Imagen · Saint Seiya (Los Caballeros del Zodiaco)

Investigador de imagen — puntos 1, 3, 15, 16, 19 y 23 de `ENCARGO.md`. Parte de
`partes/datos-imagen.md` (no repite esas consultas: AniList, wiki de Fandom por
personaje, Danbooru/Safebooru, Wallhaven, Sketchfab, Openverse). Formato:
libreta de datos, un dato por línea.

## Hallazgos

### Punto 1 — Arte oficial, en cantidad y variado

- Portada y banner oficiales de AniList (anime 1986): 225×298 y 1900×472 px
  (medidos con Pillow) · https://anilist.co/anime/1254 · ✅ (AniList + usada
  también por la wiki) · licencia: uso editorial/promocional, no libre.
- **Hoja `hojas/personajes_01.jpg`** (56 imágenes, wiki saintseiya.fandom.com,
  páginas de Seiya/Shiryu/Hyoga/Shun/Ikki/Saori y sus galerías): key visuals
  1920×1080 (wallpapers oficiales de Toei/Bandai), turnarounds técnicos a
  línea de las Cloths (Pegasus 1-5, Cygnus 1-3; #29-39), escaneos de manga
  (cap. 4.1; #18-20, 26-31), fotograma de la película *Legend of Sanctuary*
  (#14), póster *Heaven Chapter — Overture* 633×900 (#48), foto de producto
  *Pegasus Seiya (Myth Cloth CG)* 720×960 (#42). ✅ (imágenes + `imageinfo` de
  la API de Fandom, tamaños reales).
- **Hojas `hojas/vestuario_01.jpg` y `hojas/fondos_01.jpg`** (94 imágenes más,
  páginas de Aries Mu, Leo Aiolia, Virgo Shaka, Scorpio Milo, Sagittarius
  Aiolos, Pope Shion, Saga, Dohko y Athena's Sanctuary): arte oficial de los
  Santos Dorados en sus 3 versiones (Gold Cloth clásica, God Cloth de la saga
  Hades, Soul of Gold), armadura de Asgard (Odin Robe), turnarounds técnicos
  de Aries y Sagitario (#79-80), fotogramas de *The Lost Canvas* y capturas CG
  de la serie Netflix *Knights of the Zodiac* (2019). ✅.
- Tomo 1 del manga (Kurumada, Shonen Jump, 1986): portada con Seiya, 413×644 px
  · https://static.wikia.nocookie.net/saintseiya/images/0/00/Volume1.jpg ·
  ✅ (imagen de la wiki + confirmado por Wikipedia: «el primer tomo lleva a
  Pegasus Seiya en la portada»). Colección completa de tomos de Kurumada
  escaneada: https://archive.org/details/saint-seiya-manga-kurumada-works
  (Internet Archive) · ⚠️ (un origen, formato de colección sin catalogar
  tomo a tomo).
- Artbook «Saint Seiya Precious Artwork» + «Saint Seiya Hikari»:
  https://archive.org/details/artbooks-saint-seiya-precious-artwork · ⚠️
  (archivo .rar sin extraer aquí — pesado y sin visor directo; un solo
  origen). Se deja el enlace para quien continúe.
- Videojuego oficial *Saint Seiya: Soldiers' Soul* (Bandai Namco, PS3/PS4,
  2015) en Steam (appid 348710): carátula (`header.jpg`) 460×215,
  cápsula 231×87, capturas de menú/combate 1920×1080 · fuente:
  https://store.steampowered.com/app/348710 (API `appdetails`) · ✅ (Steam +
  Wikipedia lo confirma como parte de la trilogía Sanctuary
  Battle/Brave Soldiers/Soldiers' Soul).
- 40.º aniversario (2026-2027): «Saint Seiya 40th Anniversary Celebration
  Grand Original Art Exhibition», anunciada para 2027 en *Weekly Shōnen
  Champion*, más figura conmemorativa Saint Cloth Myth EX Pegasus Seiya
  [First Bronze Cloth] · fuentes: https://x.com/NekketsuHeroes/status/2054583260278132876
  y https://www.shfiguarts.com/news/2396/Saint-Seiya-40th-Anniversary.html ·
  ✅ (dos medios independientes sobre el mismo anuncio).
- Símbolo/constelación oficial de Pegaso (usado como marca de personaje en
  videojuegos y merchandising): `S.S Pegasus Constellation.png` 869×537 y
  `S.S Pegasus Star Pattern.jpg` 981×493 · wiki saintseiya.fandom.com · ⚠️ (un
  origen, pero material de producción, no fan art).

### Punto 3 — Fan art y renders 3D (referencia) + modelos con licencia libre

- Fan art mejor valorado por personaje ya está en `datos-imagen.md`
  (Safebooru, con enlace, tamaño y origen/autor cuando lo hay). Nombres de
  artista confirmados en el origen: `heiligershadowfax` (DeviantArt, Piscis
  Afrodita), `ladygt93` (DeviantArt), `RIO_AOI` (Twitter/X, Saori). El resto
  cita el enlace pixiv/artwork pero sin nombre de autor verificable ⚠️.
- **Modelos 3D con licencia libre** (Sketchfab, todos con `downloadable=true`;
  licencia y autor comprobados con la API `v3/models/<uid>`, no de memoria):
  - Estatua de Athena · Adriano.Fontoura.Fraga · CC Attribution (BY 4.0) · ♥104 ·
    https://sketchfab.com/3d-models/none-0390aa9da1f74214bfe5e7fcc4b9a4d6
  - Grande Arena (Coliseo/Palestra) · Adriano.Fontoura.Fraga · CC BY · ♥226 ·
    https://sketchfab.com/3d-models/none-9483831a03e7485b9dd83837c46f0721
  - Casa de Virgo y Casa de Cáncer (2 de las 12 Casas) · Adriano.Fontoura.Fraga
    · CC BY · ♥212 / ♥156 · https://sketchfab.com/3d-models/none-b85a291055c5436e8b4ec6bfa53af0aa
    y https://sketchfab.com/3d-models/none-86bd39f9c92b4aa4add8def2ae8a266a
  - Cloth Sagitario, Cloth Capricornio, Cloth Libra (armaduras doradas) ·
    GremorySaiyan · CC BY · ♥158/♥108/♥61 ·
    https://sketchfab.com/3d-models/none-8028c71014ae4c2498c8adcd2a8f6c93 ·
    https://sketchfab.com/3d-models/none-821113a5daf949bba5142211a964f6d9 ·
    https://sketchfab.com/3d-models/none-473d9e131eee42b8b88eaed7de39d271
  - Modelo Seiya y Seiya God Cloth · RaulV2 · CC BY · ♥196/♥94 ·
    https://sketchfab.com/3d-models/none-c835aca9be5b4081b4f6eb8b84df86e2 ·
    https://sketchfab.com/3d-models/none-a55f6698905b49c8b5ae0dcaf7089e82
  - Shiryu V4 ACE y Hyoga V4 ACE (versiones «Rebirth») · RaulV2 · CC BY ·
    ♥61/♥46 · https://sketchfab.com/3d-models/none-f947b6d968eb463e8ca3a9e1286d225e
    · https://sketchfab.com/3d-models/none-46a45943439a4be592141259a0cbccf7
  - Ikki Armadura Divina · RaulV2 · CC BY · ♥53 ·
    https://sketchfab.com/3d-models/none-a0f5b5b2eef84e9a873fec9e1348490e
  - Shun de Andromeda · Krlts · **CC BY-NC-ND** (no comercial, sin obra
    derivada) · ♥32 · https://sketchfab.com/3d-models/none-e84be0d61cd041b18415495ca71ce4ec
    — ⚠️ licencia más restrictiva que el resto, sólo referencia visual, no
    para render final.
  - Todos ✅ (licencia confirmada con la API oficial de Sketchfab, no con la
    ficha resumida del buscador).
- Fotos de cosplay y merchandising con licencia libre (Openverse/Flickr, CC
  BY-NC-ND y CC BY-SA, autor `animepapertoys` y `DocChewbacca`): ya listadas
  en `datos-imagen.md`, 19 fotos con tamaño y autor. ✅.

### Punto 15 — Vestuario: por arco, colores medidos, accesorios, ropa icónica

Colores medidos con `herramientas/estilo.py` sobre la imagen citada (no de
memoria); paleta completa y % de área en `imagen.json` → campo `paleta`.

- **Pegasus Cloth (bronce, Seiya)**, foto de producto *Myth Cloth CG* (720×960):
  cuerpo plata/hueso #C5C0BC y #EDEAE3 (el «bronce» se ve gris-plateado en las
  versiones CG/figura, no dorado), fondo #121021, acento granate #533633 ·
  ✅ (coincide con las 5 hojas técnicas de diseño de la Cloth, todas a línea
  sin color, que muestran el mismo perfil de placas).
- **Phoenix Cloth (Ikki)**, medida en 2 imágenes independientes → ✅: naranja-
  dorado #EDB045/#94662D (`Phoenix ikki final bronze cloth.jpg`, 800×600) y
  #CD864A/#784313 (`Phoenix Ikki Basic Pic.jpg`, 650×650). Es la Cloth de
  bronce con el tono más cálido/dorado de las 5, consistente en ambas fotos.
- **Dragon Cloth (Shiryu)**: verde azulado #45A89A/#9EF1DA sobre fondo de
  estudio blanco (`Bronze - Dragon Shiryu V1.jpg`, 447×800) · ⚠️ un origen,
  pero coincide con la descripción «green dragon cloth» de guías de fans en
  inglés.
- **Vestido de Athena (God Cloth)**: blanco #FCFBFB, dorado mostaza #D8C049,
  amarillo pálido #F5F28E, lila-gris #AEA4C5 en joyas/cetro (`Athena God
  Cloth.png`, 663×850) · ✅ (imagen + texto de la wiki: «white dress
  symbolizing divinity»).
- **Gold Cloth clásica** (grupo, saga Santuario): dorado-marrón #AC7623 y
  amarillo #DFC544 sobre fondo de batalla púrpura-gris (`Athena and the Gold
  Saints.PNG`, 1920×1080) · ✅.
- **God Cloth de los Santos Dorados** (mejora de la saga Hades): más cálida y
  «quemada» que la Gold Cloth base — #A4893D, #D9C53D, crema #F4EAB7, con
  mucha línea de contorno #A18C40 (`God Cloth Gold Saints.png`, 1920×1080) ·
  ✅ (contraste medido entre las dos versiones, mismo tipo de armadura).
- **Odin Robe** (armadura de la saga alterna de Asgard, ej. Aiolia): esquema
  de color totalmente distinto — azul marino #171C26/#294373/#4165A4 con
  acento mostaza #AEAA36, nada de dorado (`Aiolia (Odin Robe and
  Aiolos).png`, 1920×1080) · ✅ — dato útil: el mismo personaje cambia de
  paleta según el arco, no sólo de traje.
- **Soul of Gold** (resurrección de los Santos Dorados, serie 2015): mismo
  patrón de Gold Cloth con brillo/aura dorada más intensa en las capturas de
  animación (`Gold Saints (Soul of Gold).png`) · ⚠️ un origen de imagen, pero
  documentado también por Wikipedia (*Saint Seiya: Soul of Gold*, serie
  spin-off completa dedicada a esto).
- **Ropa civil**: Seiya con camiseta roja, jean claro, tenis blancos, banda
  roja en el brazo (texto «Appearance» de la wiki, ✅ combinando texto + las
  hojas donde aparece vestido de calle, p. ej. escenas de playa con Miho) —
  ⚠️ el hex exacto de la camiseta no se pudo aislar: las fotos disponibles
  del wiki con esa ropa están dominadas por el fondo de mar/atardecer al
  medir con `estilo.py`. Hyoga: camiseta azul sin mangas, pantalón negro,
  calentadores naranja, a veces abrigo café (texto wiki) · ⚠️ mismo problema,
  las fotos disponibles son nocturnas/oscuras (medido: negro >85% del
  cuadro). Queda para quien tenga un fotograma más limpio (rol de vídeo).
- **Shun (Andrómeda)**: cabello y ojos verdes en el anime clásico (texto
  oficial de la wiki + etiqueta Danbooru `green_hair`/`green_eyes`) · ✅ dos
  fuentes independientes. Armadura con tonos rosa/magenta según la etiqueta
  Danbooru `pink_armor` (ya en `datos-imagen.md`) · ⚠️ sólo tageo de fans; no
  se pudo medir en una imagen oficial limpia (las disponibles del wiki con
  esa armadura son wallpapers nocturnos, dominados por el fondo espacial
  morado, no por la armadura).
- **Peinados reconocibles** (silueta, de las hojas + texto «Appearance»):
  Seiya castaño de puntas hacia arriba; Shiryu negro largo con banda en la
  frente; Hyoga rubio liso; Shun castaño/verdoso con flequillo lacio; Ikki
  azul oscuro alborotado con cicatriz bajo el ojo. ✅ (imagen + texto).

### Punto 16 — Ciudades, paisajes y fondos de pantalla

Luz y hora del día medidas con `estilo.py` (no de memoria); es un
complemento a los fotogramas de vídeo del rol de vídeo (punto 4), aquí con
imágenes fijas y wallpapers.

- **Doce Casas / Santuario** (exterior en piedra): gris mármol #8D8D91 y
  #5C6269, cielo #94B5DB, luz diurna difusa, saturación baja (11-15%)
  (`LC Sanctuary Location2.jpg`, 2711×1080 y `Sanctuary of Athena.jpg`,
  600×337) · ✅ (2 imágenes distintas de la misma zona, mismo resultado).
- **Coliseo/Palestra** (arena de entrenamiento): beige-gris #E5E1DB/#D0CBC1,
  saturación muy baja (9%), luz de día nublada (`ColosseumTLC.jpg`,
  1204×692) · ✅ (coincide con el modelo 3D «Grande Arena» del punto 3, misma
  arquitectura circular).
- **Pradera / Star Hill** (saga *The Lost Canvas*, 1743): verde #98B967,
  cielo celeste #99B4DB, luz de mediodía, brillo alto (79 %) — el fondo más
  luminoso de toda la muestra (`LostCanvas.jpg`, 1280×1396) · ✅.
- **Templo del Zodiaco al atardecer**: tonos tierra cálidos #1F1B18/#433A35/
  #6B5D4D/#998765, brillo medio (43 %), clara luz de atardecer
  (`LC Zodiac.jpg`, 1280×1387) · ✅.
- **Mansión Kido al anochecer**: morados oscuros y azules fríos —
  `Saori Kido wallpaper.jpeg` (1920×1080, #030305/#181F37/#AFADBC) y
  `Andromeda Shun wallpaper.jpeg` (1920×1080, fondo espacial casi negro
  #020304 44,7 %) — ambas son wallpapers oficiales con estética de
  constelación nocturna, no fondos «de interior» realistas · ✅ (mismo patrón
  en 2 wallpapers oficiales de personajes distintos).
- **Fondos de pantalla oficiales/de fans en alta** (Wallhaven, ♥ = favoritos):
  la mayoría de los resultados con la etiqueta «Saint Seiya» son colages
  crossover con Dragon Ball/One Piece/Naruto (ya en `datos-imagen.md`); los
  que son **sólo** Saint Seiya: 5496×3000 «reflejo de ballena» (♥43, origen
  pixiv: https://www.pixiv.net/artworks/100255153); 1920×1200 «montañas,
  luna» (♥48, sin origen firmado); **hallazgo nuevo** 1500×1018, Mu de Aries,
  arte digital, autor `jNiederauer` (♥ visible en la ficha) ·
  https://wallhaven.cc/w/429e1y · ✅ (purity SFW confirmada con la API).

### Punto 19 — Texturas 2D

- **Trama de manga (screentone)**: escaneos del capítulo 4.1 en
  `hojas/personajes_01.jpg` (#18-20, 26-31) — tinta negra de línea gruesa +
  puntos de trama regular (halftone), blanco y negro puro, sin degradado de
  gris real; típico del shōnen de Shonen Jump de los 80 · ✅ (visto
  directamente en el escaneo).
- **Ilustraciones técnicas «Cloth design»**: hojas de despiece con flechas y
  numeración de piezas (Pegasus 1-5, Cygnus 1-3 en `personajes_01.jpg`
  #29-39; Aries y Sagitario en `vestuario_01.jpg`/`fondos_01.jpg` #79-80) —
  línea fina de plano técnico sobre fondo blanco, ideal para el contorno
  pieza a pieza de una armadura · ✅.
- **Emblema/constelación oficial**: patrón de estrellas de Pegaso usado como
  marca de personaje, `S.S Pegasus Constellation.png` (869×537) y
  `S.S Pegasus Star Pattern.jpg` (981×493), wiki saintseiya.fandom.com · ⚠️
  un solo origen (material de producción, sin segunda fuente que lo repita).
- **Patrones de tela vs. metal**: la túnica de Athena es blanco liso con
  ribete dorado (sin trama de tela visible); las armaduras son superficie
  metálica lisa con grabados curvos en relieve, no textura de tejido — visto
  en las mismas imágenes medidas en el punto 15.
- **Texturas libres equivalentes (con licencia)**:
  - Metal048A / Metal048B / Metal048C (ambientcg, **CC0**) — oro/bronce
    pulido para placas de armadura ·
    https://ambientcg.com/view?id=Metal048A
  - Fabric026 y Fabric080 (ambientcg, **CC0**) — tela para capas/túnicas ·
    https://ambientcg.com/view?id=Fabric026
  - «Retro Halftone Clouds» (Flickr vía Openverse, **CC BY**, 1024×768) —
    trama de puntos para simular impresión de manga ·
    https://live.staticflickr.com/3437/3801365993_fcae20a01a_b.jpg

### Punto 23 — Colaboraciones y cruces

- **Videojuego móvil "Saint Seiya Awakening: Knights of the Zodiac"**: hub
  activo de eventos y crossovers oficiales del propio estudio (no fan
  content) · https://x.com/SaintSeiyaKOTZ · crossover con «QQ Speed: Mobile»
  (abril 2021: pieles de auto basadas en las armaduras de Saori/Athena y los
  5 Bronze Saints) · fuente: https://www.jbox.com.br/2021/04/28/saint-seiya-awakening-armaduras-viram-carros-em-crossover-com-qq-speed-mobile/
  · ⚠️ un solo medio (prensa de fans brasileña), no lo repite un segundo
  medio.
- **Uniqlo UT** (ropa oficial licenciada): camisetas de Saint Seiya por el
  aniversario de Shonen Jump/Shueisha, dos tiendas licenciadas lo confirman
  como el mismo producto · https://jumpichiban.com/en-us/products/shueishas-100th-anniversary-x-uniqlo-fashion-collection-saint-seiya-vol-1
  y https://www.aitaikuji.com/shonen-jump-50th-anniversary-x-uniqlo-t-shirts-saint-seiya
  · ✅.
- **Fortnite: NO confirmado.** Hay vídeos de YouTube y un post de fan en X
  (`@PegasusFly_`, feb-2025) que anuncian una supuesta llegada a la
  Temporada 2 Cap. 5, pero no hay ningún ítem de Saint Seiya en la tienda
  oficial (revisado `fortnite.com/item-shop` y `epicgames.com`) ni anuncio en
  los canales oficiales de Epic Games · se deja como rumor/proyecto de fans,
  **no** como colaboración real (ver «No encontré»).
- **Figuras oficiales** (Bandai): línea *Saint Cloth Myth* / *Saint Cloth
  Myth EX* — foto de producto ya citada en el punto 1 (720×960) · catálogo
  vigente en el sitio oficial de Bandai: https://tamashiiweb.com/item_character/saint_seiya_series/?wovn=en
  · ✅ (imagen de producto + catálogo oficial, dos fuentes).
- **Cosplay premiado**: 2.º premio, Saint Seiya, World Cosplay Summit
  Barcelona 2019 (canal del evento «Misión Tokio», subido 2019-11-02,
  4445 vistas, verificado con `yt-dlp`) · https://www.youtube.com/watch?v=_ze5TsXkrMk
  · ⚠️ un solo origen (el vídeo del evento), no hay cobertura de prensa
  aparte que lo repita.
- **Café temático**: no encontré uno propio de Saint Seiya (a diferencia de
  franquicias como *Jujutsu Kaisen*, que sí tienen cafés dedicados en Tokio);
  ver «No encontré» con las búsquedas hechas.
- **Exposición 40 aniversario 2027**: ya citada en el punto 1 (dos medios) ·
  también aplica aquí como evento/colaboración con la propia editorial.

## Lo mejor para la lámina

1. El contraste de paleta entre Cloths por arco es el hallazgo más fuerte:
   Gold Cloth dorado-marrón vs. God Cloth dorado-quemado vs. Odin Robe azul
   marino — sirve para fechar visualmente cualquier escena sin texto.
2. `hojas/vestuario_01.jpg` (#61 *LostCanvas.jpg*, pradera a mediodía) y
   `hojas/fondos_01.jpg` (#62 *LC Zodiac.jpg*, templo al atardecer) dan dos
   fondos con luz opuesta y medida, listos para Blender (piedra + cielo).
3. La Estatua de Athena y la Grande Arena en Sketchfab (CC BY, descargables)
   son el objeto y el sitio reales que pide `reglas_del_dueno.md` (punto 1).
4. Ikki (Fénix) es el que más varía de paleta entre fuentes propias sin
   contradecirse (siempre naranja-dorado cálido): el más seguro para colores.
5. Ninguna colaboración de marca real (Fortnite no está confirmado): si se
   quiere «colaboración» para la lámina, usar Uniqlo/Shonen Jump o las
   figuras Bandai, no Fortnite.

## No encontré

- **Cartones/tarjetas de cuenta atrás** (eyecatch de comienzo/vuelta de
  publicidad) del anime de 1986: busqué «Saint Seiya eyecatch», «cuenta
  atrás tarjeta comercial Toei 1986» (español e inglés) y no aparecieron en
  la wiki ni en búsqueda web. ⚠️ no descarto que existan, sólo no los
  localicé con las fuentes a mano.
- **Café temático propio de Saint Seiya**: busqué «Saint Seiya café temático
  Ikebukuro/Shibuya 2024/2025» (español e inglés); sólo aparecen cafés de
  otras franquicias (Jujutsu Kaisen). No lo encontré, no digo que no exista.
- **Portada de videojuego con arte propio** para *Sanctuary Battle* y *Brave
  Soldiers* (más allá de *Soldiers' Soul* en Steam): busqué en MobyGames/
  DeviantArt; sólo hay un fan-scan en DeviantArt sin confirmar como el
  arte de caja real. ⚠️.
- **Hex exacto de la ropa civil** de Seiya (camiseta roja) y Hyoga (camiseta
  azul/calentadores naranja): las fotos disponibles del wiki con esa ropa
  están dominadas por fondo de mar/atardecer o por negro de escena nocturna
  al medir con `estilo.py`; sólo queda la descripción textual (⚠️, marcado
  arriba en el punto 15). Un fotograma más limpio lo puede sacar el rol de
  vídeo con `fotogramas.py` sobre un capítulo con esa ropa.

## Bitácora de búsqueda

- Español/inglés (directo, sin buscador): API de Fandom (`saintseiya.fandom.com/api.php`,
  `action=query&prop=images/imageinfo`, `list=search`, `list=categorymembers`
  para localizaciones: Category:Locations, Category:Earth, Category:God
  Temple, Category:Locations in Greece) · Sketchfab API v3 (`search` y
  `models/<uid>` para licencia) · ambientcg API v2 · Openverse API v1 ·
  Wallhaven API v1 (`search?q=saint+seiya`, ficha por id para tags/purity) ·
  Steam `storesearch` y `appdetails` (appid 348710) · Internet Archive
  `metadata` (dos colecciones de artbooks/manga) · `herramientas/estilo.py`
  sobre 15 imágenes de la wiki para paleta y luz medidas.
- `herramientas/investigar_serie.py` × 2: la primera corrida (recolector) con
  las 6 páginas de personajes → `hoja_01/02.jpg` (56 imgs); la mía, con
  `--serie "Saint Seiya vestuario y santuario"` (carpeta nueva para no pisar
  la anterior) y páginas de Santos Dorados + Santuario → 2 hojas más
  (94 imgs). Elegidas las 3 mejores para `hojas/`.
- Buscador web (en español e inglés, ~9 búsquedas de mi cupo de 50): «Saint
  Seiya Awakening colaboración crossover evento», «Saint Seiya colaboración
  Uniqlo Fortnite Line Friends café temático», «Saint Seiya 40th anniversary
  key visual artbook official», «Saint Seiya cosplay premiado World Cosplay
  Summit», «Fortnite Saint Seiya colaboración oficial confirmada Epic
  Games», «Saint Seiya café temático exposición Ikebukuro Shibuya 2024
  2025», «Saint Seiya manga tomo portada oficial Kurumada tankobon cover»,
  «Saint Seiya videojuego portada Soldiers Soul Sanctuary Battle Brave
  Soldiers cover art», «Saint Seiya eyecatch cuenta atrás tarjeta comercial
  Toei 1986».
- yt-dlp `--print` (sin descargar vídeo) para verificar autoría/fecha del
  vídeo de cosplay de World Cosplay Summit.

Sigue: nada obligatorio pendiente de mi parte (puntos 1, 3, 15, 16, 19, 23
cubiertos con fuentes, ✅/⚠️ marcados). Si se libera más cupo, se podría: (a)
extraer el artbook `.rar` del punto 1 para citar páginas concretas, (b)
pedir al rol de vídeo un fotograma limpio de Seiya/Hyoga en ropa civil para
medir el hex que aquí quedó en ⚠️.
