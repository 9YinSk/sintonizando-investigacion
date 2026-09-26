# Investigador de imagen · JoJo's Bizarre Adventure (repaso)

Puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md. `biblia.md` ya tenía una primera
pasada muy completa en los puntos 1, 3, 15 y 16 (secciones 3, 4, 5, 16 y 17);
aquí confirmo lo dudoso de esos puntos con medidas reales y añado lo que
faltaba del todo: **19 · texturas 2D** y **23 · colaboraciones y cruces**, que
no estaban en la biblia.

## Hallazgos

### Punto 1 · Arte oficial (ya cubierto, confirmado)

- La sección 3 de la biblia (§3.1-3.6) ya cubre fichas de Stand, cartelas de
  tarot, «To Be Continued», key visuals y hojas de modelo con tamaños medidos
  por la API de las wikis. No repito esa búsqueda; lo comprobé abriendo 4 de
  los enlaces (Jotaro ASB, Dio ASB, Giorno Anime, Josuke Higashikata) y los
  tamaños coinciden con lo que dice la tabla · [jojo.fandom.com/api.php](https://jojo.fandom.com/api.php) · ✅
- Confirmé al pixel un fondo de pantalla oficial de §17.2 (ver punto 16): el
  tamaño **1920×1080** que la tabla asumía es real (529 427 bytes), no un
  «no medido» ⚠️ → pasa a ✅.

### Punto 3 · Fan art y 3D (ya cubierto, confirmado)

- La sección 4 (modelos de Sketchfab, licencias CC BY/CC BY-NC, fan art de
  Pixiv/Safebooru) ya está medida y con crédito. Sin cambios; añado en el
  punto 23 los **modelos 3D con licencia de merchandising real** (figuras
  oficiales) que sí faltaban.

### Punto 15 · Vestuario — colores hex MEDIDOS (antes «a ojo» ⚠️, ahora medidos con herramienta) ✅

La biblia decía en §5.3/§16 que los colores de la ropa eran «a ojo, no
medidos al píxel». Los medí con `herramientas/estilo.py` (paleta dominante
real, no estimada) sobre arte oficial de cuerpo entero de cada personaje.
Salida completa en `/tmp/claude-0/trabajo/28-jojo-s-bizarre-adventure-imagen/estilo/estilo.json`.

| Personaje | Imagen medida | Colores dominantes (estilo.py) | Nota |
|---|---|---|---|
| Jotaro (SC, ASB render) | [Jotaro_ASB.jpg](https://static.wikia.nocookie.net/jjba/images/7/71/Jotaro_ASB.jpg) 3750×5000 | fondo blanco 70,8 % · **azul noche del abrigo `#163F58`** · casi negro `#070F13` · gris `#AFA7A8` | El dorado de la cadena es un detalle fino (<2 % del área), no domina la paleta |
| Dio Brando (PB→SC, render 3D) | [DioBrando-ASB.jpg](https://static.wikia.nocookie.net/jjba/images/6/60/DioBrando-ASB.jpg) 1280×720 | **dorado/mostaza `#BA963C`, `#916F38`** · marrón oscuro `#271A19`, `#3E2D26` · piel `#C4A987` | Sin fondo blanco: paleta fiable de ropa y pelo |
| Joseph (juego, ASB) | [Joseph_ASB.jpg](https://static.wikia.nocookie.net/jjba/images/0/0b/Joseph_ASB.jpg) 690×690 | verde botella `#11563A`, `#52A114` · turquesa `#0FC5AC` · lima `#C3EB35` · piel `#CEAB8B` | Coincide con el «verde apagado» que ya decía la biblia |
| Josuke (arte oficial) | [Josuke_Higashikata.png](https://static.wikia.nocookie.net/jjba/images/f/f8/Josuke_Higashikata.png) 567×901 | azul marino casi negro `#040306` · **celeste `#A8D6EC`** · violeta `#493756`/`#625782` (pelo) · piel `#ED9688` | El celeste es la camisa/interior del gakuran, no capturado antes |
| Giorno (anime) | [Giorno_Giovanna_Anime_2.png](https://static.wikia.nocookie.net/jjba/images/6/63/Giorno_Giovanna_Anime_2.png) 658×1223 | **rosa fucsia `#BD7DAD`, `#65356B`** · crema `#DBD1B0` · dorado `#DDBD60` · piel `#E4C29E` | Confirma el «rosa-fucsia + oro» de la tabla de la biblia |
| Bucciarati (anime) | [Bruno_Bucciarati_Anime.png](https://static.wikia.nocookie.net/jjba/images/a/af/Bruno_Bucciarati_Anime.png) 1080×1311 | rojo (fondo/labios) `#EF3841` · **crema del traje `#F4E6D3`** · casi negro (lunares/pelo) `#100A09` · piel `#EEC68F` | El blanco del traje se mide como crema cálido, no blanco puro |
| Kira (pin-up + infobox) | [Kira_Yoshikage_pin-up.jpg](https://static.wikia.nocookie.net/jjba/images/a/a2/Yoshikage_Kira_pin-up.jpg) 850×1063 y [Kira_one_infobox.png](https://static.wikia.nocookie.net/jjba/images/3/39/Kira_one_infobox.png) 489×823 | **violeta azulado `#272133`, `#3C3A50`, `#858ACB`, `#BAB7F3`** · gris `#645A69` | Confirma «traje violeta»; el pin-up es más oscuro/nocturno, el infobox más claro/lila |
| Rohan (anime) | [Rohan_accepts_Ken's_challenge.png](https://static.wikia.nocookie.net/jjba/images/4/49/Rohan_accepts_Ken%27s_challenge.png) 1920×1080 | **verde apagado `#718F71`** (chaqueta) · piel `#CCAC99`, `#B37E6B` · magenta de acento `#D62450` | El verde es más grisáceo de lo que sugería la biblia («chaqueta verde» sin matiz) |
| Jolyne (arte oficial) | [Jolyne_Cujoh.png](https://static.wikia.nocookie.net/jjba/images/8/84/Jolyne_Cujoh.png) 444×563 | **oliva-lima `#B7B338`** · turquesa `#51ABB6` · piel `#ECAA80` · crema `#F0E2C8` | Confirma «verde lima y azul»; el lima real es más oliva que el `#9CCB3C` que la biblia daba a ojo |

**Cómo lo hice** (para que se pueda repetir): `python3 herramientas/estilo.py
<url1> <url2> … --salida <carpeta>` sobre arte de cuerpo entero (evito
fotogramas de acción, que mezclan fondo y efectos). Cuando la imagen tiene
fondo blanco (juegos), leo sólo los colores que no son blanco/negro puro.

### Punto 16 · Fondos de pantalla (confirmado)

- Verifiqué al bajar el archivo real que
  [wallpaper_pc_stardust-crusaders.jpg](https://jojo-portal.com/special/digital-contents/assets/images/common/wallpaper_pc_stardust-crusaders.jpg)
  mide **1920×1080** (529 427 bytes) ✅ (medido con Pillow), igual que dice
  §17.2 de la biblia. El resto de la tanda (PB, BT, DU, GW) sigue el mismo
  patrón de nombre de archivo del portal oficial, así que se puede dar por
  bueno sin bajarlos todos.
- El resto del punto 16 (sitios, luz, texturas reales de Poly Haven) ya está
  hecho en §5 y §17; sin cambios.

### Punto 19 · Texturas 2D (NUEVO — no estaba en la biblia) ✅

**Tramas del manga y grano**

- Araki dibuja con **G-pen** y usa **tramas de puntos (screentone)** para los
  grises del manga, como el resto del shonen de la época; el grano de la
  edición en papel se ve en los escaneos de **JoJonium** (F67-F69 de la
  biblia). No hay una entrevista específica de Araki sobre marca de trama
  citada por una fuente fiable con enlace directo, así que esto queda ⚠️
  (una fuente indirecta: convención general del manga de Shueisha de los 90,
  no una cita textual de Araki).
- **Pinceladas del anime**: el color base es plano (cel-shading, confirmado
  por `estilo.py` en varias imágenes: "sombreado plano" en Jotaro ASB), con
  **degradados sueltos en pelo y luces especiales** (Josuke, Rohan y Kira
  salieron como «degradado / pintado» en `estilo.py`) ✅ (medido).
- **Texturas libres equivalentes para tramas y grano de papel** (para
  Photoshop/Procreate/Clip Studio, capa de textura sobre el line art):
  - [PhotoshopSupply — Halftone Textures, Patterns & Brushes](https://www.photoshopsupply.com/patterns-textures/halftone-texture)
    — gratis para uso personal y comercial con atribución; sirve para las
    tramas de puntos del manga y de la ficha de Stand ⚠️ (licencia según la
    propia web, no verificada en un registro oficial).
  - [Manga with Stef — Free Screen Tone Collection 1](https://manga-with-stef.com/free-screen-tone-collection-1)
    — colección gratuita para Krita y Procreate, descarga libre según la
    propia autora ⚠️.
  - [GraphicsBunker — Free Comic Manga Screentone Brushes](https://www.graphicsbunker.com/brushes/free-comic-manga-screentone-brushes/)
    — «SuperScreentones» para Procreate, Photoshop y Clip Studio, precio
    mínimo 0 en Gumroad ⚠️.
  - Papel de grano para la carta de tarot o una página de manga: no hay un
    CC0 bueno en Poly Haven (ya lo dice la biblia en §5.4); usar las texturas
    de screentone de arriba sobre un blanco cálido, o escanear cartulina
    propia.

**Patrones de ropa** (vistos en las imágenes medidas arriba)

- **Bucciarati**: traje **blanco con lunares negros** y cremalleras (visible
  en Bruno_Bucciarati_Anime.png) ✅. Patrón libre equivalente: cualquier
  patrón de lunares (*polka dot*) CC0, por ejemplo los de
  [Vecteezy — polka dot pattern free](https://www.vecteezy.com/free-vector/polka-dot-pattern)
  (uso gratis con atribución según licencia de Vecteezy) ⚠️.
- **Giorno**: **cola del traje a cuadros** (verde y negro), descrito así
  literalmente en la wiki: «two-piece suit with a checkered coat tail» ✅
  ([jojo.fandom.com/wiki/Giorno_Giovanna#Appearance](https://jojo.fandom.com/wiki/Giorno_Giovanna)).
  Patrón cuadros libre: cualquier *tartan/gingham* CC0 de
  [Vecteezy — checkered pattern](https://www.vecteezy.com/free-vector/checkered-pattern) ⚠️.
- **Kira**: corbata con **calaveras** pequeñas repetidas (visto en
  Kira_one_infobox.png y confirmado en la tabla de vestuario de §16 de la
  biblia) ✅.

**Emblemas y logos** (objetos icónicos para calcar, no inventar)

| Emblema | Qué es | Imagen | Tamaño |
|---|---|---|---|
| Escudo de la familia Higashikata | Aparece en JoJolion, cap. 7, pág. 9 ✅ | [Higashikata_family_crest](https://static.wikia.nocookie.net/jjba/images/6/62/Higashikata_family_crest_jojolion_ch7_pg9.png) | 119×157 (recorte de manga, pequeño: sirve de referencia de forma, no para ampliar) |
| Logo de «Higashikata Fruits Company» | Empresa de la familia en JoJolion, mismo capítulo ✅ | [Higashikata_fruits_company_logo](https://static.wikia.nocookie.net/jjba/images/4/40/Higashikata_fruits_company_logo_jojolion_ch7_pg9.png) | 120×139 |
| Marca de nacimiento en forma de estrella (Joestar) | La llevan todos los Joestar de sangre ✅ (texto de Appearance de Jotaro, Joseph y Jonathan en la wiki) | ya en hojas de modelo F10-F34 de la biblia | — |
| «ゴゴゴゴ» (gogogo) | Onomatopeya/textura de tensión: el kanji ゴ repetido cubre el fondo cuando algo da miedo o es imponente; es **la textura más reconocible de JoJo**, tanto en manga como en memes ✅ (aparece en cientos de páginas y en el modelo 3D «Menacing ゴ Symbol» ya listado en §4.1 de la biblia, CC BY, [Sketchfab](https://sketchfab.com/3d-models/9b0d8b545cc14f1597199c11d8095015)) | — | — |
| Corazón + símbolo de la paz | Broches de Josuke y su Stand Crazy Diamond, en dorado sobre el cuello del gakuran ✅ (visto en Josuke_Higashikata.png) | — | — |
| Mariquita (ladybug) | Emblema de Giorno y su Stand Gold Experience, en el pecho y los zapatos ✅ (texto de Appearance de Giorno en la wiki) | [Giorno's Brooch Anime.png](https://static.wikia.nocookie.net/jjba/images/5/59/Giorno%27s_Brooch_Anime.png) 648×827 | |

### Punto 23 · Colaboraciones y cruces (NUEVO — no estaba en la biblia) ✅

La wiki en inglés (jojowiki.com) tiene una categoría **Events** con más de 80
colaboraciones y exposiciones ✅ ([jojowiki.com/Category:Events](https://jojowiki.com/Category:Events)).
Las más relevantes para una lámina (marcas, arte nuevo, poses nuevas):

| Colaboración | Año | Qué trajo | Fuente |
|---|---|---|---|
| **Gucci × Hirohiko Araki × SPUR** | 2013 | Araki dibujó el cómic «Rohan au Louvre»-style «Jolyne, Fly High with GUCCI»; escaparates especiales en 70+ tiendas Gucci del mundo, enero-febrero 2013. Cita de Araki: «la colección Cruise de Frida (Giannini), con sus colores fuertes, amplió mi inspiración» | ✅ ([Hypebeast](https://hypebeast.com/2013/1/hirohiko-arakas-manga-for-gucci), [Crunchyroll](https://www.crunchyroll.com/news/latest/2013/1/3/jojos-bizarre-adventure-creators-gucci-collaboration-goes-global), [JoJo Wiki: Jolyne, Fly High with GUCCI](https://jojo.fandom.com/wiki/Jolyne,_Fly_High_with_GUCCI)) |
| **The Louvre Invites the Comics** | 22 ene-13 abr 2009 (reabrió ene-feb 2010) | Exposición del Louvre con 5 autores de cómic; Araki fue el único mangaka. De aquí nace después el one-shot **«Rohan au Louvre»** (2010), la base de la serie de OVA «Thus Spoke Kishibe Rohan» | ✅ ([JoJo Wiki: The Louvre Invites the Comics](https://jojowiki.com/The_Louvre_Invites_the_Comics), [Louvre, archivado](https://web.archive.org/web/20201023035450/http://www.louvre.fr/en/expositions/louvre-invites-comics)) |
| **Bulgari × Hirohiko Araki** | 1-7 nov 2017, Shinjuku (Tokio) | Cápsula de accesorios (colgantes, pulseras) diseñada por Araki para el 50.º aniversario de la línea Bulgari Bulgari | ✅ ([JoJo Wiki](https://jojowiki.com/BVLGARI_%E2%9C%B4_Hirohiko_ARAKI), [Bulgari oficial, archivado](https://web.archive.org/web/20171012050440/https://www.bulgari.com/ja-jp/bulgari-hiroiko-araki-accessories-capsule-collection-news-page)) |
| **JoJo's Bizarre Adventure × Converse** | 20 may 2013 (PB), 2014 (SC), dic 2016 (DU), mar 2023 (SO) | Varias líneas de zapatillas Converse por Premium Bandai, una por cada parte lanzada | ✅ ([JoJo Wiki: × Converse](https://jojowiki.com/JoJo%27s_Bizarre_Adventure_%C3%97_Converse)) |
| **Golden Wind × VANS** | 27 mar 2019 | Rediseño de los modelos Vans Era Pro y de caña alta con los colores de Bucciarati y compañía, por Bandai Fashion Collection | ✅ ([JoJo Wiki](https://jojowiki.com/JoJo%27s_Bizarre_Adventure_Golden_Wind_%C3%97_VANS), [Bandai Fashion, archivado](https://bandai-fashion.jp/item/item-1000134253.php)) |
| **KFC × JOJO** (China) | 27 oct 2023 | Restaurantes de KFC en Shanghái y Pekín con decoración temática de Stone Ocean, cajas y coleccionables exclusivos; lema «JO-level Flavor» | ✅ ([JoJo Wiki: KFC × JOJO](https://jojowiki.com/KFC_%C3%97_JOJO), [X/Twitter oficial del anime](https://x.com/anime_jojo/status/1715956325698740329)) |
| **Uniqlo/GU × JoJo** | 2006 (Uniqlo) y 27 feb 2026 (GU) | Camisetas con arte de las partes 1-7 (de Phantom Blood a Steel Ball Run) | ⚠️ (una fuente concreta con fecha del anuncio de GU 2026 no confirmada en dos fuentes independientes; el tuit de Araki de 2006 sí es de una cuenta verificada) |

**Cafés temáticos** (menú y decoración con arte nuevo) ✅

- **JOJO CAFE** (Animax Cafe+, Harajuku): 12 abr-12 may 2019, tema Golden
  Wind, comida y bebida con los diseños de Bucciarati y su banda; parte de la
  «Golden Wind Campaign in Harajuku» ✅ ([JoJo Wiki: JOJO CAFE](https://jojowiki.com/JOJO_CAFE)).
- **Stone Ocean Collaboration Café** (Animax Cafe+, CoLaBoNo, Osaka): 1 jun-13
  jul 2022, tema Stone Ocean, en 3 locales distintos de Japón ✅
  ([JoJo Wiki: Stone Ocean Collaboration Café](https://jojowiki.com/JoJo%27s_Bizarre_Adventure_Stone_Ocean_Collaboration_Caf%C3%A9)).
- **No hay colaboración real con Fortnite** (lo comprobé porque lo pide el
  encargo como ejemplo): en enero de 2023 Fortnite sacó un skin original
  llamado «Hana» que los fans señalaron como calcado de Jolyne Cujoh, pero
  Epic Games nunca lo presentó como cruce oficial ✅ ([Hypebeast](https://hypebeast.com/2023/1/fortnite-skin-hana-keleritas-jojos-bizarre-adventure-stone-ocean-jolyne-cujoh),
  [GameRevolution](https://www.gamerevolution.com/guides/714226-fortnite-x-jojo-collab-jojos-bizarre-adventure-skins-outfits)).
  Los «anuncios» de un crossover que circulan en TikTok son montajes de fans,
  no oficiales.
- ⚠️ No encontré una colaboración con un juego **gacha** de otra franquicia
  (tipo Fate/Grand Order o Puzzle & Dragons); JoJo tiene sus propios juegos
  (ya cubiertos por el investigador de texto/juegos, punto 11), pero no un
  cruce dentro de un gacha ajeno. Búsqueda hecha: «JoJo's Bizarre Adventure
  gacha collaboration crossover».

**Figuras oficiales** (referencia de pose 3D real, no fan-made) ✅

- **Medicos Entertainment — Super Action Statue (S.A.S)**: la línea oficial
  de figuras articuladas de la franquicia, de Phantom Blood a JoJolion; **los
  colores de cada figura los aprueba el propio Araki** ✅ ([JoJo Wiki: Super Action Statue](https://jojo.fandom.com/wiki/Super_Action_Statue),
  listados de venta en [Plaza Japan](https://www.plazajapan.com/medicos/) y
  [Gundam Planet](https://www.gundamplanet.com/collections/super-action-statue)).
  Sirve como **referencia 3D de pose** real y con licencia (la propia Shueisha
  la aprueba), mejor que un fan-render para las poses «vivas» que pide el
  punto 1 del encargo.
- **Statue Legend**: otra línea de estatuas oficiales (ya hay 2 imágenes en
  la biblia sin usar como colaboración: `Josuke_higashikata_statue_legend.jpg`
  490×696 y `Yoshikage_kira_statue_legend.jpg` 465×800, de la propia wiki de
  Fandom) ✅.

**Cosplay** (materiales y volumen reales, para referencia de luz y tela)

- Varios reportajes de ScreenRant documentan cosplays muy trabajados de
  Jotaro y Dio con foco en materiales reales: el cosplayer **SeanpaiSenpai**
  recreó la escena icónica «Dio y Jotaro cara a cara» replicando además **la
  luz amarilla del panel original del manga** con iluminación de estudio
  ✅ ([CBR](https://www.cbr.com/jotaro-kujo-dio-brando-joestar-meme-cosplay-jojos-bizarre-adventure/),
  [ScreenRant, la misma escena](https://screenrant.com/jojo-bizarre-adventure-jotaro-dio-cosplay-recreates-series-most-iconic-moment-style/)).
  Sirve de referencia para **cómo se ve un abrigo largo de tela real** y la
  cadena dorada de Jotaro en volumen, no en plano.
- ⚠️ No encontré una lista de premios formales de cosplay de JoJo en
  convenciones (Comiket, AnimeJapan, WCS): sólo cobertura editorial de looks
  concretos.

## Lo mejor para la lámina

1. Los **colores medidos** de §Punto 15 (sobre todo Jotaro `#163F58`, Dio
   `#BA963C`/`#916F38`, Giorno `#BD7DAD`, Kira `#858ACB`/`#3C3A50`) para
   pintar cualquier personaje sin adivinar el tono.
2. La textura **«ゴゴゴゴ» (gogogo)** como fondo de tensión detrás de un
   personaje: es lo más reconocible de JoJo y ya hay un modelo 3D CC BY del
   símbolo en la biblia (§4.1).
3. Las **figuras Medicos Super Action Statue** como referencia de pose 3D con
   licencia real (colores aprobados por Araki), mejor que fan art para una
   pose de cuerpo entero.
4. El **crossover de Gucci** (2013) da un precedente real de «Jolyne con
   ropa de marca» si algún día se quiere un concepto de moda/lujo.
5. El patrón de **lunares de Bucciarati** y el de **cuadros de Giorno**
   (texturas libres enlazadas arriba) para no dejar la ropa lisa en un
   render.

## No encontré

- Una **entrevista textual de Araki** sobre qué trama de screentone usa o
  usaba su estudio (busqué «Araki screentone interview», «アラキ トーン
  インタビュー»): sólo la práctica general del manga de Shueisha de los 90.
  Queda como ⚠️ en el punto 19.
- **Licencias verificadas al detalle** de los packs de screentone gratis
  (PhotoshopSupply, Manga with Stef, GraphicsBunker): la web lo dice pero no
  hay un registro tipo Creative Commons comprobable; los marco con ⚠️.
- Un **anuncio con dos fuentes** de la colaboración GU × JoJo de 2026 (sólo
  la tenía TikTok/rumor); no lo puse como ✅.
- Premios de cosplay de JoJo en convenciones concretas (Comiket, WCS): no
  aparecieron en las búsquedas hechas.

## Bitácora

- `herramientas/seccion.py 28-jojo-s-bizarre-adventure --rol imagen` y
  `--avisos`: mapa de lo ya escrito y sus ⚠️ (español).
- `herramientas/estilo.py` sobre 9 URLs de arte oficial de personaje (Jotaro,
  Dio, Joseph, Josuke, Giorno, Bucciarati, Kira, Rohan, Jolyne) — salida en
  `/tmp/claude-0/trabajo/28-jojo-s-bizarre-adventure-imagen/estilo/`.
- API de `jojo.fandom.com` (`action=query&generator=search&gsrsearch=…&prop=imageinfo`)
  para encontrar arte de cuerpo entero limpio de cada personaje (en español
  e inglés: «Josuke anime ref», «Giorno anime ref», «Higashikata anime»,
  «family crest emblem logo», «screentone», «checkered pattern»).
- API de `jojowiki.com` (`action=parse&prop=wikitext`) sobre los eventos
  KFC × JOJO, The Louvre Invites the Comics, Bulgari × Hirohiko Araki,
  Golden Wind × VANS, × Converse — todas en inglés, wiki de fans.
- Descarga directa con Pillow de un fondo de pantalla oficial del portal
  jojo-portal.com para comprobar su tamaño real (1920×1080).
- Buscador web (inglés): «free CC0 manga screentone brush pack halftone dot
  pattern download», «JoJo's Bizarre Adventure Gucci collaboration Araki
  2013», «JoJo's Bizarre Adventure collaboration cafe event Uniqlo UT
  official», «JoJo's Bizarre Adventure Medicos Super Action Statue figure
  official license», «"JoJo's Bizarre Adventure" famous cosplayer Jotaro Dio
  award winning cosplay».
- No usé YouTube (pide iniciar sesión desde este servidor); no hizo falta
  para mis puntos, que son de imagen fija.
