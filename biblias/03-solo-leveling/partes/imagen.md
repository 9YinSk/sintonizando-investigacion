# Investigador de imagen · Solo Leveling — repaso corto (puntos 19 y 23)

Repaso corto (24-sep-2026): la biblia ya está hecha (dos pasadas); sólo faltan
los puntos **19 (Texturas 2D)** y **23 (Colaboraciones y cruces)** de
`ENCARGO.md`, nuevos en el encargo. No repito nada de `datos-imagen.md` ni de
lo que ya está en `biblia.md` (arte oficial §10, vestuario §8, modelos 3D
§11 — eso lo cubrió la primera/segunda pasada, puntos 1, 3, 15, 16). No toco
`biblia.md`: eso es del redactor.

## Hallazgos · Punto 19 — Texturas 2D

**Cómo está pintado el manhwa (para saber qué textura buscarle equivalente)**
- El webtoon **no usa tramas de manga tradicionales** (no es como un manga en
  blanco y negro): DUBU (Jang Sung-rak, REDICE Studio) colorea con
  **degradados digitales saturados**, pensados para pantalla, no para papel.
  Los efectos de textura son **aberración cromática** (poderes psíquicos),
  **motion blur** (velocidad) y **líneas de velocidad radiales** con
  fragmentos de humo/escombros, no puntos de trama. · fuente:
  [canmom.art — análisis del manhwa](https://canmom.art/crit/comics/solo-leveling)
  (leído entero) · ⚠️ una sola fuente propia leída a fondo, aunque coincide
  con lo que resumen otras reseñas (asianmoviepulse.com, comicbookyeti.com)
  que no abrí completas.
- Line art: líneas limpias y definidas, muy estudiadas en el plegado de la
  ropa y la anatomía muscular; en el anime (A-1 Pictures) se añade grano y
  brillo de postproducción (eso ya lo cubre el punto 18, del equipo de texto).

**Emblemas y logos del mundo (para calcarlos o vectorizarlos)**
- **Ahjin Guild** (阿진, el gremio de Jinwoo): símbolo circular morado con un
  triángulo/aguijón dorado, 700×700 · `File:Ahjin.png` ·
  https://static.wikia.nocookie.net/solo-leveling/images/8/88/Ahjin.png/revision/latest?cb=20210529014242
  · medido con Pillow · fuente: [wiki, API imageinfo](https://solo-leveling.fandom.com/wiki/File:Ahjin.png)
  · ⚠️ un solo sitio (la wiki), aunque hay dos versiones/archivos que coinciden
  en el diseño.
- **Ahjin Guild**, versión del logo que aparece en el capítulo 141 del
  webtoon, 725×803 · `File:Ah-Jin Logo Ch.141.PNG` ·
  https://static.wikia.nocookie.net/solo-leveling/images/c/ca/Ah-Jin_Logo_Ch.141.PNG/revision/latest?cb=20210904095011
  · medido con Pillow.
- **Hunters Guild** (el gremio más grande de Corea, de Choi Jong-In): insignia
  circular dorada, 480×480 · `File:Insignia Hunters.png` ·
  https://static.wikia.nocookie.net/solo-leveling/images/8/89/Insignia_Hunters.png/revision/latest?cb=20200209102559
  · medido con Pillow · fuente: [wiki](https://solo-leveling.fandom.com/wiki/Hunters_Guild)
  · ⚠️ un solo sitio. Nota: son diseños **con derechos** (Chugong/DUBU vía
  D&C Media); sirven de **referencia visual**, no para calcar y vender.
- El **Scavenger Guild** (EE.UU., de Thomas Andre) tiene página en la wiki
  pero **sin símbolo propio** listado (`Symbol=` vacío en su ficha) · ⚠️
  comprobado en el wikitext, no lo encontré en ningún lado más.

**Patrones y grabados (armaduras, telas)**
- La armadura de **Igris** y de **Beru** está descrita como grabada
  («jet-black armor», con adornos) en `datos-imagen.md`; el patrón real de
  grabado en metal no lo da la wiki en texto, se mide en las imágenes
  grandes ya recolectadas (485 y 25 imágenes respectivamente).

**Texturas y pinceles libres equivalentes (con licencia)**
- **Tramas de manga (screentone):** «[FREE] Manga Screentone Pack 1»,
  gratis (precio $0, comprobado) para Clip Studio Paint desde la versión
  1.10.10 · https://assets.clip-studio.com/en-us/detail?id=2142037 ·
  licencia: gratis en CLIP STUDIO ASSETS (uso dentro del programa) · ✅
  comprobado el precio con curl.
- **Líneas de velocidad** (las que sí usa Solo Leveling, en vez de tramas):
  «Manga Speedlines», 20 pinceles .ABR gratis, licencia **Free for
  Commercial Use (Attribution)**, compatible con Procreate, Affinity Photo,
  GIMP y Krita · https://myphotoshopbrushes.com/resources/3816/manga-speedlines
  · ✅ comprobada la licencia exacta en la página (JSON-LD del sitio).
- **Grabado en metal** (para Igris, Beru, las armaduras): «Metal Armor
  Pattern 001», CC0, resolución 4K · https://3dtextures.me/2026/01/28/metal-armor-pattern-001/
  · ✅ comprobado «cc0» y «4K resolution» en la página.
- **Grano de papel** (para el manhwa impreso o efectos de viñeta): CC0
  Textures, categoría papel, sin registro ·
  https://cc0-textures.com/c/paper · ⚠️ una fuente, no bajé un archivo
  concreto (complementa el punto 4, que ya usó Poly Haven/ambientCG para
  texturas reales de sitios).
- **Encuadres/aberración cromática y grano de anime:** ese estilo de
  postproducción no es una «textura 2D» descargable; se replica con ajustes
  de capa (Chromatic Aberration, Film Grain) en Photoshop — apunte para el
  punto 18 (equipo de texto/técnica), no una fuente nueva.

## Hallazgos · Punto 23 — Colaboraciones y cruces

**Videojuegos (crossovers, cada uno trae poses/ropa nueva)**
- **Fortnite × Solo Leveling: ARISE**: 3 skins oficiales — Sung Jin-Woo,
  Cha Hae-In y **«Blood-Red Commander Igris»** — en la tienda del 20-feb-2026
  al 2-mar-2026 (evento previo: «Solo Leveling: Arise Cup», 19-20 feb). El
  traje de Jin-Woo es «reactivo»: cambia de aspecto según eliminas rivales en
  la partida (referencia directa a su transformación de Monarca de las
  Sombras). Basado en el videojuego ARISE, no en el anime. · páginas
  oficiales: https://www.fortnite.com/item-shop/offers/sung-jinwoo-ed689683
  y https://www.fortnite.com/item-shop/offers/solo-levelingarise-bundle-bf68c9e7
  (la tienda ya cerró, pero la URL sigue documentada) · ✅ dos fuentes:
  [Anime News Network / ScreenRant vía búsqueda](https://www.videogamer.com/news/fortnite-solo-leveling-crossover-sung-jinwoo/)
  y [ExitLag](https://www.exitlag.com/news/solo-leveling-in-fortnite/).
- **Solo Leveling: ARISE × Frieren: Beyond Journey's End** (oct-2025):
  colaboración con 3 nuevas unidades SSR jugables (Frieren, Fern, Stark) y
  misión especial · imagen oficial 1280×720 ·
  https://cdn5.idcgames.com/storage/image/1577/frieren-collaboration-update-pv/default.jpg
  (medida con Pillow) · fuente:
  [idcgames.com (portal oficial del juego)](https://idcgames.com/en/solo-levelingarise/news/frieren-joins-solo-leveling-arise-in-an-epic-collaboration-with-beyond-journey%E2%80%99s-end-2025-10-23-11-00-11653)
  · ✅ confirmado también por [Inven Global](https://www.invenglobal.com/articles/19808/solo-leveling-arise-announces-collaboration-with-frieren-beyond-journeys-end).
- **Solo Leveling: ARISE × (G)I-DLE** (K-pop): primer crossover del juego con
  un grupo real; MIYEON y SHUHUA como Hunters jugables · ⚠️ una fuente
  (Game8) — interesa mucho al servidor (es de canto e ídolos).
- **Solo Leveling: ARISE × OVERDRIVE**: promoción cruzada con código canjeable
  entre los dos juegos · ⚠️ una fuente (dotgg.gg).
- **Grand Summoners × Solo Leveling** (anime RPG, en vivo desde el
  12-jun-2026): Jinwoo, Choi Jong-In, Cha Hae-In e Igris jugables, con sus
  armas (Espada del Monarca Demonio, montante de Igris) como equipo
  invocable; recrea movimientos del anime · ✅ dos fuentes:
  [Anime News Network (nota de prensa)](https://www.animenewsnetwork.com/press-release/2026-06-12/grand-summoners-x-solo-leveling-now-available-in-many-territories-worldwide/.238449)
  y [CBR](https://www.cbr.com/solo-leveling-grand-summoners-game-crossover-collaboration/)
  («Solo Leveling se une a One Punch Man» en el roster de crossovers del
  juego).
- **Seven Knights Re:BIRTH × Solo Leveling**: primer crossover de ese juego
  con la serie · ⚠️ una fuente (gamefragger.com), no verificada en una
  segunda web.

**Eventos, cafés y exposiciones**
- **Exposición inmersiva «Solo Leveling»** (la primera del mundo dedicada a
  la serie): 22-nov-2025 al 1-mar-2026, DUEX Hongdae Exhibition Hall 1,
  Mapo-gu, Seúl. Zonas temáticas (Templo Cartenon, Isla Jeju, mazmorra de la
  estación de Hongdae), estación interactiva para invocar sombras gritando
  «Arise», **figuras a tamaño real de Jinwoo, Igris y el Rey Hormiga**,
  vídeos de batalla panorámicos, exhibición de armas, **café temático**, zona
  de fotos y tienda (con IDs de cazador de mentira) · imagen oficial
  1107×622 · https://static.animecorner.me/2025/09/1759182098-938fb7693a9c38ba777e1cf5b0a4bc41.png
  (medida con Pillow) · ✅ dos fuentes:
  [Anime Corner](https://animecorner.me/solo-leveling-gets-first-visual-for-immersive-new-exhibition-in-korea/)
  y [The Korea Herald](https://www.koreaherald.com/article/10589225).
- **Café «ARISE × ANIPLUS»**: café-colaboración anterior del videojuego, del
  22-ago al 6-oct-2024, en Hapjeong, Seúl · ⚠️ una fuente (world.nol.com,
  la propia web de reservas del café).
- **«System Sync»: pop-up de Solo Leveling × Omniscient Reader's Viewpoint**
  (el otro gran fantástico coreano; ambos comparten editorial en inglés,
  Ize Press): 14-30 ago-2026, 238 E 6th St, Manhattan, coincidiendo con
  Anime NYC (20-23 ago). Ropa exclusiva que brilla en la oscuridad, importado
  de Corea, «stamp rally» con Ize Press en Anime NYC · ✅ tres fuentes:
  [Anime News Network](https://www.animenewsnetwork.com/news/2026-07-17/solo-leveling-omniscient-reader-viewpoint-pop-up-store-to-open-in-new-york-in-august/.239721),
  [Yen Press (oficial)](https://yenpress.com/news/system-sync) y
  [CBR](https://www.cbr.com/solo-leveling-omniscient-readers-viewpoint-system-sync/).

**Figuras oficiales**
- **Nendoroid Sung Jinwoo** (#2597), Good Smile Arts Shanghai / Good Smile
  Company: ¥7.200, ~100 mm, escultor Semi/Title, con 3 caras intercambiables
  (mando, batalla, chibi) y piezas opcionales (Knight Killer, un soldado de
  sombra, el panel del Sistema). Salió abril-2025; relanzamiento marzo-2027
  · imagen oficial del producto, 750×1000 ·
  https://www.goodsmile.com/gsc-webrevo-sdk-storage-prd/product/image/34792/u5732DjFSANprK9bicHCL4kxQ0RzWZUm.jpg
  (medida con Pillow) · ✅ dos fuentes:
  [Good Smile Company (oficial)](https://www.goodsmile.com/en/product/34792)
  y [CBR (concept art reveal)](https://www.cbr.com/solo-leveling-sung-jinwoo-good-smile-company-nendoroid-concept-art-reveal/).
  Su pose (de pie, con Knight Killer al hombro) sirve de **referencia 3D**
  para una escultura o render del personaje.
- Además hubo un **peluche de Sung Jinwoo** de Good Smile que se agotó antes
  de que todos los fans pudieran comprarlo · ⚠️ una fuente (ScreenRant).

**Cosplay bien hecho (materiales y volumen reales, no telas planas)**
- **Esil Radiru**, armadura roja y dorada hecha a mano (foam/resina, con
  volumen real en hombreras, peto y grebas; pintura metalizada) ·
  4096×2731 · https://i.redd.it/i917f5bdst6h1.jpg (medida con Pillow) ·
  autora: u/_Mikomihokina_ (fotografía firmada «Mikomihokina Photo») ·
  publicado en [r/SoloLeveling](https://www.reddit.com/r/sololeveling/comments/1u3r1le/)
  (vía Arctic Shift, `gallery_data`) · **la miré**: hombreras, peto y guantes
  con relieve real, no estampado · ✅ imagen vista + post con autora
  identificada (falta una segunda fuente fuera de Reddit).
- **Igris** sin casco, armadura roja/dorada de placas superpuestas con capa,
  casco aparte sobre un pie de exhibición · 4016×6016 ·
  https://i.redd.it/mv4qi4hnqjcg1.jpg (medida con Pillow) · autora: u/Halfangel66
  · publicado en [r/SoloLeveling](https://www.reddit.com/r/sololeveling/comments/1q980kq/)
  (vía Arctic Shift) · **la miré**: piezas de armadura con espesor real
  (EVA foam o worbla, no cartón plano), espada de utilería con vendas en el
  mango · ⚠️ una fuente (Reddit).
- Otros cosplays de Igris con más apoyo del fandom (por puntuación en
  r/SoloLeveling, sin abrir la imagen): «Igris Cosplay» (5.925 puntos,
  vídeo) y «Peak Igris Cosplay» (1.635 puntos) — quedan anotados para que el
  redactor elija si hacen falta más ejemplos.
- Cosplay de **Cha Hae-In** encontrado en Reddit (i.redd.it/ge5zuhif42eg1.jpeg,
  1080×1579): es un look casual con peluca rubia corta, **no** la armadura
  roja icónica — no lo recomiendo como ejemplo de «materiales y volumen
  reales» del punto 23; lo anoto pero con esta salvedad.
- Un post viral («Perfect cosplay of Jinwoo», 5.598 puntos) no es disfraz:
  es un jugador coreano que se parece a Jinwoo enmarcando su cara con una
  copa de vino para imitar el corte de pelo del anime — meme del fandom, no
  cosplay con vestuario; lo dejo fuera del punto 23 pero podría servir para
  el punto 12 («lo que ama el fandom»), que no es mío.

## Lo mejor para la lámina

1. Los emblemas de **Ahjin Guild** (700×700) y **Hunters Guild** (480×480) dan
   un escudo/sello grabable en madera o metal para la puerta o el mostrador
   de un hilo del foro (encaja con el objeto que propone el encargo: la
   ventana del Sistema sobre un sitio real).
2. El **Nendoroid de Jinwoo** (foto oficial 750×1000) es la mejor referencia
   3D de una pose «de pie, con su arma al hombro» con licencia clara de uso
   como referencia (no para calcar el diseño, sí para mirar el volumen).
3. La armadura roja y dorada de **Igris** en cosplay real (4016×6016) enseña
   cómo se ve el grabado del metal con luz de estudio: sirve para el
   sombreado del emblema si se decide una versión «con armadura» de un
   hilo.
4. El **grabado en metal CC0 4K** (3dtextures.me) y el **pack de líneas de
   velocidad libres** (Free for Commercial Use) son las dos texturas/pinceles
   con licencia más directamente usables para replicar el estilo sin
   IA de imagen que «invente» una trama.
5. La **exposición de Seúl** (figuras a tamaño real + «Arise» interactivo)
   es la mejor prueba de que el gesto de invocar sombras es el momento más
   reconocible de la serie para el público — coincide con la idea del
   objeto del encargo (la ventana del Sistema en un sitio real).

## No encontré

- ⚠️ Una entrevista directa a DUBU o a REDICE Studio sobre software/pinceles
  exactos del manhwa (Clip Studio vs. Photoshop): busqué «Solo Leveling
  manhwa coloring technique interview», «DUBU REDICE Studio art style
  interview» (inglés) y no apareció una entrevista técnica citable, sólo
  reseñas. Lo dejo para el punto 18 (equipo de texto), que puede tenerlo
  cubierto con el *making of* del anime.
- ⚠️ Un símbolo propio para la **Korean Hunters Association** (el organismo
  oficial, distinto de los gremios privados): busqué en la wiki
  («Hunters Association emblem seal», «Korean Hunters Association») y sólo
  salió el logo del *Hunters Guild* (gremio privado). Puede que la
  Asociación oficial sólo use texto/sello de tinta roja en el anime, sin un
  logo gráfico fijo: no lo encontré, no digo que no exista.
- ⚠️ Patrón textil propio (tejido, no color plano) en la ropa de Jinwoo o
  Cha Hae-In: la wiki describe colores y cortes, no tramas de tela; no
  parece un dato que la wiki documente. Compensado con la referencia CC0 de
  grabado en metal para las armaduras (Igris/Beru), que sí tienen relieve
  visible en las imágenes grandes.
- Colaboración con marca de moda o bebidas (tipo Uniqlo, 7-Eleven Corea) no
  la encontré con las búsquedas hechas («Solo Leveling brand collaboration
  fashion», «Solo Leveling 7-Eleven»); lo que sí hay y está confirmado son
  las de videojuegos, el café/exposición y el pop-up con Ize Press.

## Bitácora de búsqueda

- Wiki de Fandom (API, inglés): `srsearch=collaboration`, `emblem OR logo`,
  `Ahjin Guild`, `Hunters Association emblem seal`, `magic circle`,
  `hunter license card` — imageinfo para `Ahjin.png`, `Ah-Jin Logo
  Ch.141.PNG`, `Insignia Hunters.png` (tamaños reales por API).
- WebSearch (inglés, 11 búsquedas): estilo de dibujo/DUBU/REDICE, técnica de
  coloreado, pinceles libres de halftone/screentone, texturas de papel CC0,
  Clip Studio Assets screentone gratis, pinceles de líneas de velocidad,
  texturas de grabado en metal CC0, colaboraciones 2026, café/exposición
  Corea, Fortnite oficial, ARISE crossovers, cosplay oficial.
- WebFetch: `canmom.art/crit/comics/solo-leveling` (análisis completo,
  citado), `korealore.com` (perfil del webtoon, sin datos técnicos nuevos),
  `animenewsnetwork.com` (403, no se pudo leer directo — se usó el resumen
  de la búsqueda en su lugar), `goodsmile.com/en/product/34792` (specs de
  la figura), `idcgames.com` (colaboración Frieren), `animecorner.me`
  (exposición de Seúl).
- Arctic Shift (Reddit, `r/SoloLeveling`): búsqueda `title=cosplay`
  (15 resultados) y `posts/ids` para sacar `gallery_data`/`media_metadata`
  de dos posts (Esil Radiru y Igris) con tamaño real sin necesidad de
  bajarlos primero.
- Verificado con curl + Pillow (tamaño real medido): emblemas de la wiki,
  imagen de la exposición de Seúl, imagen de la colaboración con Frieren,
  foto del Nendoroid de Jinwoo, las dos fotos de cosplay (Esil Radiru,
  Igris), licencia exacta del pack de líneas de velocidad (JSON-LD de la
  propia página) y el precio ($0) del pack de tramas de Clip Studio Assets.
- No se necesitó YouTube en este repaso (los puntos 19 y 23 no piden mirar
  vídeo, salvo los tráilers de los crossovers de videojuegos, que están
  descritos por las notas de prensa oficiales citadas arriba).

Sigue: nada pendiente de los puntos 19 y 23 (obligatorio cubierto). Quedan
sólo los ⚠️ de «No encontré», que son extras, no obligatorios.
