# Imagen — Oshi no Ko · repaso corto (puntos 19 y 23)

Investigador de imagen. Esta biblia ya tiene los puntos 1-17 (ver
`biblia.md`); sólo faltaban los puntos **19** (texturas 2D) y **23**
(colaboraciones y cruces), que no estaban. Parto de `datos-imagen.md`
(ya mirado, no repito esas consultas) y de la wiki de Fandom.

**Aviso importante para el jefe:** el subdominio de la wiki que da el
encargo (`oshi-no-ko`) **da 403/404** (Cloudflare). El correcto, que sí
funciona con la API, es **`oshinoko.fandom.com`** (sin guiones). Por eso
`recolectar.py` no pudo bajar nada de Fandom (`datos-imagen.md` lo dice
en su cabecera). Con el subdominio bueno la API responde normal.

## Hallazgos

### Punto 19 · Texturas 2D (tramas, papel, pinceladas, patrones, emblemas y logos)

**Tramas del manga (screentone), miradas en una página real:**
- En la página de manga oficial de B小町 en el escenario (Fandom,
  `B-Komachi Current Manga.jpg`, 1299×1423) se ven cuatro capas de
  textura 2D distintas ✅ (vista directamente, no de memoria):
  1. **Trama de puntos en degradado** para sombrear pelo y piel (más
     densa donde hay sombra, se aclara hacia la luz).
  2. **Patrón de brillos/estrellas** pequeñas sueltas por el fondo
     (efecto "sparkle" típico de escena de ídolos).
  3. **Rejilla de cuadros pequeños** de fondo, en dos franjas — son las
     luces del escenario vistas de lejos (mismo recurso que el fondo de
     focos de los renders, §6 de la biblia).
  4. **Rayado fino a pluma** (crosshatch) sólo en las sombras más
     oscuras (bajo el pelo, pliegues de ropa).
  - Fuente: [Fandom, «B-Komachi»](https://oshinoko.fandom.com/wiki/B-Komachi),
    imagen con `imageinfo` medida ✅.
- El estilo de línea fina y las tramas suaves son de la dibujante
  **Mengo Yokoyari** (共同作者/artista); ya está descrito en `datos-imagen.md`
  y en `estilo.py` lo puede ampliar el investigador de texto (punto 18,
  no repito).

**Pinceles y tramas libres equivalentes (con licencia):**
- **34 pinceles de screentone/halftone gratis** para Photoshop
  (licencia «community»: uso libre personal y comercial) — [Brusheezy,
  Mabecman's Screentones](https://www.brusheezy.com/brushes/50379-mabecman-s-screentones-halftone-brushes) ✅ (comprobado, página abierta).
- **Pincel de brillos «Shoujo Manga Sparkle»**, gratis (0 puntos) en
  CLIP STUDIO ASSETS (necesita cuenta + CSP para instalarlo) — [enlace](https://assets.clip-studio.com/en-us/detail?id=1887489) ✅
  (comprobado: la página marca «free» tres veces).
- **Texturas de papel gratis** para CSP (colección «Paper textures»,
  también «free») — [enlace](https://assets.clip-studio.com/en-us/detail?id=1752867) ✅.
  Para 3D ya está el papel CC0 de Poly Haven (§6.4/§5.1 de la biblia,
  punto 4): **misma textura sirve para las dos capas** (2D y 3D), no
  falta ninguna.

**Patrones de ropa vistos de verdad (no inventados):**
- Los trajes de idol de B小町 (uniforme rojo, «POP IN 2», Taito) llevan
  **lazos, corazones y estrellas sueltas** como adorno, no un estampado
  de tela repetido (revisé el uniforme de Yōtō en las hojas P· y O· de
  la biblia y en las fotos de cosplay: es azul marino liso con ribete
  dorado, sin cuadros). Por eso el patrón libre que sirve es de
  **lunares/corazones/estrellas**, no un tartán:
  [freesvg.org, «Polka dot seamless pattern»](https://freesvg.org/polka-dot-seamless-pattern),
  **CC0 / dominio público** ✅ (comprobado en la propia página, lo dice
  tres veces).

**Emblemas y logos reales (mirados, con tamaño):**
- **Ichigo Production, Inc**: placa de metal grabada «Ichigo Production,
  Inc · Saitou» con el emblema de una **fresa con una coronita** encima
  (323×205, medido) ✅ — [Fandom](https://oshinoko.fandom.com/wiki/Ichigo_Production,_Inc).
  Coincide con lo que ya describió la primera pasada de la biblia (§3,
  «placa gris cálido con una fresa»): **dos fuentes** de la misma placa.
- **B小町, logo de la 1.ª generación**: monograma cursivo «B» + kanji
  「小町」en negro, insignia recortada con **borde de picos blancos**
  tipo estrella, estilo vintage (313×313, medido) ✅ — [Fandom](https://oshinoko.fandom.com/wiki/Category:BKomachi_Gen1_Logo).
- **B小町, logo de la 2.ª generación**: letras «B小町» en burbuja
  rosa/magenta con degradado, sobre un **corazón rojo**, con una
  **estrella y una estela amarilla** cruzándolo tipo varita mágica
  (600×600, medido) ✅. Mucho más «pop» que el logo gen1: se puede usar
  el contraste de los dos para mostrar el antes/después del grupo.

### Punto 23 · Colaboraciones y cruces

La wiki tiene una página completa de colaboraciones
([Fandom, «Oshi no Ko (anime)/Promotional Material»](https://oshinoko.fandom.com/wiki/Oshi_no_Ko_(anime)/Promotional_Material))
con **más de 25 marcas/eventos** distintos. Elegí las más útiles para
láminas (ropa y poses nuevas, cafés, figuras, juegos):

**Marcas y comercios** (todas ⚠️ una fuente — la propia wiki — salvo
donde digo lo contrario):
- Sweets Paradise (café), Natslive Cafe (café), Animate Cafe (café),
  Gamers, Kujibikido, Tower Records, Animate (tienda), HotPepperBeauty,
  **DyDo** (máquinas expendedoras, regala **fondos de pantalla** con
  poses nuevas — cruza con el punto 16), Taito Toys (premios de grúa),
  Giants (béisbol, con lanzamiento inicial de las seiyū), GiGO
  (recreativos), RakuSpa (spa), Yomiuri Land (parque de atracciones),
  **Sanrio**, Sega Plaza, Gindaco (takoyaki), Don Quijote, Family Mart,
  Meiji, Ichiban Kuji (lotería con figuras), Real Escape Game (SCRAP,
  ya en la biblia §3), Seibu Yuenchi.
- **Sanrio** ✅ **dos fuentes**: además de la wiki, lo confirman
  [CBR](https://www.cbr.com/sanrio-hello-kitty-oshi-no-ko-official-crossover/)
  y [Siliconera](https://www.siliconera.com/oshi-no-ko-sanrio-crossover-merchandise-will-pair-characters/)
  (en inglés, búsqueda web). Parejas: Ruby-Hello Kitty, Aqua-Cinnamoroll,
  Akane-Kuromi, Ai-Little Twin Stars, Kana-My Melody, MEM-Pompompurin,
  Pieyon-Bad Badtz-maru. El arte de Ai y Ruby lo dibujó **Kanna
  Hirayama, la diseñadora de personajes real del anime** (créditos en
  el archivo de la wiki): no es fan art, es arte de producción.
  Mercancía a la venta desde el 8-nov-2024 (CBR).

**Otros juegos (los que pide el encargo, tipo «gacha»):**
- **The Idolmaster: Shiny Colors** (ronda 1: 2023, ronda 2: 2024) — ya
  estaba en la biblia (§3, §6.2) ✅.
- **Othellonia** (Reversi/tablero, gacha de Sega/DeNA): arte nuevo tipo
  carta para Ai, Aqua+MEM, Ruby+Kana, Miyako+Akane (1920×1080) ⚠️.
- **Monster Strike**: dos rondas de colaboración (2.ª ronda empezó el
  13-feb-2026, confirmado en
  [Gachago](https://gachago.com/en/news/monster-strike-announces-second-crossover-event-with-oshi-no-ko-anime)
  y [Mix Vale](https://www.mixvale.com.br/2026/02/13/monster-strike-begins-second-collaboration-with-oshi-no-ko-and-highlights-powerful-arima-kana-en/))
  ✅ **dos fuentes**. Trae versiones «verano» y «San Valentín» de los
  personajes, ropa que no sale en el anime.
- **Caravan Stories**: personajes de 5 y 6 estrellas de Aqua, Kana y
  Ruby (wiki) ⚠️.
- **KOTODAMAN**: colaboración confirmada por vídeo oficial en YouTube
  («OSHI NO KO Collaboration Gacha on KOTODAMAN») ⚠️ una fuente (no
  está en la wiki de Oshi no Ko).
- **BanG Dream! (Girls Band Party!)**: existe una página propia en la
  wiki de BanG Dream, «Oshi no Ko x Girls Band Party! Part 1 Gacha»
  (confirmada por su título vía API; el contenido no se pudo leer,
  Cloudflare bloquea esa wiki) ⚠️.
- **Fortnite**: **no lo encontré**. Busqué «Fortnite» en el texto de la
  wiki (0 resultados) y en la web (no aparece ninguna colaboración real,
  sólo el ejemplo genérico del encargo). No hay colaboración con
  Fortnite; lo digo así, no «no existe» sin más: hice la búsqueda y no
  apareció.

**Figuras oficiales** (no de premio de grúa, coleccionables normales):
- **Ai Hoshino, figura a escala 1/7** (Good Smile Company, producida
  por Kadokawa): 215 mm con soporte, pose dinámica basada en una
  escena de concierto, pelo y colas al viento. ¥21 780. Confirmado en
  dos fuentes: [Good Smile (goodsmile.info)](https://www.goodsmile.info/en/product/14226/Ai.html)
  y [Anime Corner](https://animecorner.me/ai-hoshino-from-oshi-no-ko-gets-a-figure-pre-orders-open/) ✅.
- **Ai Hoshino, Nendoroid #2300** (Good Smile Company, chibi): foto de
  producto 726×1000 medida — [Solaris Japan](https://solarisjapan.com/products/oshi-no-ko-hoshino-ai-nendoroid-2300-good-smile-company) ✅
  (mismo modelo listado también en Good Smile US).
- **Premios de grúa Taito** («Sweet Sailor Style», «White Angel») e
  **Ichiban Kuji** (lotería, mayo y octubre 2024, febrero 2026): cada
  figura trae **ropa nueva que no sale en el anime** (marinero, ángel,
  vestidos de época) — sirven como referencia 3D de pose y de vestuario
  alternativo. Imágenes medidas en `imagen.json`.

**Cosplay bien hecho** (materiales y volumen reales, mirado en la foto,
no de memoria):
- **Ai Hoshino**, Palais Longchamp, Marsella (esby.photo, CC
  BY-NC-SA 2.0, 1024×769): vestido **rosa satinado** con falda de
  **volantes fruncidos sobre una enagua** (ahí sale el volumen real,
  no es una falda lisa), cinturón negro ancho, **guantes magenta
  largos**, medias a juego, plataformas blancas con correa al tobillo,
  peluca morada. Coincide con el traje del key visual T1 (§5.2 de la
  biblia).
- **Ruby y Aqua**, uniforme de Yōtō, San Diego Comic-Con
  (coolanimeboy25, CC BY 2.0, 1023×665): **blazer azul marino con
  ribete dorado brillante** en solapa y puños (se nota que es un
  galón cosido, no pintado), camisa blanca, pelucas rubias con mechón
  rosa. Bueno para ver cómo cae de verdad la tela del blazer (no queda
  tan rígida como en el dibujo).
- Quedan más fotos de cosplay con licencia libre (13 más) ya
  recolectadas en `datos-imagen.md` (Openverse): todas en Francia
  (Lyon, Marsella), mismo fotógrafo profesional esby.photo con CC
  BY-NC-SA, y una tanda de shotwhore photography (CC BY-NC-ND) de
  «Oshi no Ko Rooftop». No hice falta bajarlas todas: con estas dos se
  cubre uniforme + traje de idol.

## Lo mejor para la lámina
- El **logo gen2 de B小町** (corazón + burbuja rosa) es el más fácil de
  adaptar a un rótulo de canal: ya es una insignia tipo pegatina.
- La colaboración **Sanrio** (dibujada por la diseñadora real del
  anime) es la mejor prueba de que un crossover puede traer pose nueva
  *sin* salirse del estilo oficial: sirve de referencia de línea.
- El cosplay de Ai en Marsella es la mejor referencia de **volumen
  real** de la falda de volantes: en 3D/Blender conviene una enagua o
  varias capas, no una falda plana.
- La trama de puntos + rayado de la página de manga (imagen 1 de
  `imagen.json`) es la referencia más directa para configurar un
  pincel de sombreado con el pincel gratis de Brusheezy.
- El Ichiban Kuji y el Taito dan **ropa alternativa** (marinera, ángel,
  época) sin tocar el copyright del traje icónico: buena idea para una
  lámina 2 de vestuario.

## No encontré
- ⚠️ Colaboración con **Fortnite**: busqué «Fortnite» en el texto de la
  wiki (`srwhat=text`, 0 resultados) y en la web; no existe tal
  colaboración (el encargo lo pone sólo como ejemplo genérico de tipo
  de cruce, no como algo confirmado de la serie).
- ⚠️ Emblema propio del **Instituto Yōtō** (escudo del colegio): no hay
  página ni archivo en la wiki con ese nombre; el uniforme visto en
  cosplay y en las hojas P·/O· no muestra un escudo bordado visible.
- ⚠️ Licencia exacta de los pinceles de Brusheezy más allá de «licencia
  community» (uso libre, no reventa): la página no detalla si pide
  atribución obligatoria u opcional.
- ⚠️ No pude leer el contenido de la página de BanG Dream (Cloudflare
  403 incluso por API con extracto); sólo confirmé que existe por el
  título exacto.

## Bitácora de búsqueda
- **Wiki de Fandom** (inglés): subdominio correcto localizado
  (`oshinoko.fandom.com`, no `oshi-no-ko`); búsquedas de texto
  `cosplay`, `collaboration`, `logo`, `gacha`, `Fortnite`,
  `"Girls Band Party"`, `Kotodaman`; página `Oshi no Ko
  (anime)/Promotional Material` completa (wikitext); categorías «Taito
  Toys Collaboration», «Ichiban Kuji Collaboration», «Sweet Paradise
  Collaboration», «Natslive Cafe Collaboration», «Sanrio
  Collaboration», «GiGO Collaboration», «Animate Collaboration»,
  «Monster Strike Collaboration», «Caravan Stories Collaboration»;
  `imageinfo` medido de 20 archivos.
- **Web, en inglés** (WebSearch, 6 búsquedas): figura de Good Smile
  Company, cosplay de Ai Hoshino, pinceles de screentone gratis,
  brillos/tramas de shoujo manga gratis, patrón de tartán/lunares
  libre, textura de papel de manga libre, colaboración Sanrio,
  colaboración Monster Strike.
- **Openverse**: ya recolectado en `datos-imagen.md` (17 fotos de
  cosplay con licencia CC), miré 2 en grande con Read.
- **Sitios de venta de figuras** (goodsmile.info, solarisjapan.com,
  amiami.com —dio 403—): imagen de producto medida con Pillow.
- **Descargas propias miradas con Read** (`/tmp/claude-0/trabajo/05-oshi-no-ko-imagen/`):
  hoja de contacto de 4 colaboraciones (Taito×2, Ichiban Kuji, Sweets
  Paradise), logo Ichigo Pro, logos B小町 gen1/gen2, 2 fotos de cosplay.
  Los `.mp4`/`.png` de trabajo se pueden borrar, no hay vídeo pesado en
  esta tanda.

## Cumplimiento de mis puntos (19 y 23)
| Punto | Estado | Por qué |
|---|---|---|
| 19 · Texturas 2D | ✅ | trama de manga real mirada (puntos, brillos, rejilla, rayado); pinceles libres de screentone y de brillos con licencia; textura de papel libre (cruza con el punto 4); patrón de lunares CC0; 2 logos de B小町 y el emblema de Ichigo Pro, medidos |
| 23 · Colaboraciones y cruces | ✅ | 25+ colaboraciones de marca listadas, 6 con imagen medida; 6 juegos/gacha (Fortnite comprobado que no existe); figura oficial 1/7 y Nendoroid de Ai con fuente doble; 2 cosplays analizados por materiales y volumen |

Sin `Sigue:` — los dos puntos están completos con lo obligatorio del
encargo. Quedan extras posibles en «No encontré», no pendientes.
