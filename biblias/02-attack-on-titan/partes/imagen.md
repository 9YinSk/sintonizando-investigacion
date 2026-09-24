# Parte de IMAGEN · Attack on Titan — repaso corto (puntos 19 y 23 de ENCARGO.md)

La biblia de esta carpeta ya tiene los puntos 1, 3, 4, 15 y 16 hechos a fondo
(arte oficial, fan art y 3D con licencia, texturas 3D reales de Poly Haven,
vestuario con hex y fondos de pantalla — ver §2 a §5 y §17 de `biblia.md`). Los
puntos **19 (texturas 2D)** y **23 (colaboraciones y cruces)** son nuevos en
`ENCARGO.md` desde el 24-sep-2026 y no estaban: no aparecen en la tabla
«Cumplimiento del encargo» (línea 1565 y siguientes). Este archivo los cubre
enteros, sin repetir lo que ya está en §2-§5.

Parto de `partes/datos-imagen.md` (ya recolectado: AniList, Fandom, Danbooru,
Safebooru, Wallhaven, Sketchfab, Openverse) sin repetir esas consultas: ahí no
hay nada de texturas 2D ni de colaboraciones/cosplay/figuras, así que todo lo
de abajo es búsqueda nueva de hoy. `hojas/` ya tiene sus 3 JPEG (el máximo);
no hago hojas nuevas, pero sí bajé y **miré** dos páginas de manga sueltas de
la wiki (no estaban en ninguna hoja) para el punto 19.

## Punto 19 · Texturas 2D

### 19.1 Trama del manga y pinceladas (las miré, no las supongo)

Bajé y miré dos imágenes de manga de la wiki que no estaban en `datos-imagen.md`
ni en las hojas de `hojas/`:

- **`Manga_Wall_Maria_operation.png`** (946×643, [Fandom](https://static.wikia.nocookie.net/shingekinokyojin/images/9/9c/Manga_Wall_Maria_operation.png)):
  Erwin a caballo con la espada en alto, cargando. Se ve bien el entintado de
  Isayama: **rayado a mano (hatching) muy denso** en el cuerpo del caballo y
  las sombras de la ropa (líneas finas, paralelas, más juntas donde hay más
  sombra — no puntos mecánicos ahí), y una **trama de puntos/degradado
  mecánico** en el fondo (cielo/hierba, gris uniforme con textura de retícula
  fina, típica de un screentone tipo Deleter/IC pegado, no dibujado a mano).
  Las líneas de fondo detrás de Erwin son **líneas de velocidad** gruesas,
  totalmente negras. · ✅ (la vi yo mismo; el estilo "mucho rayado a mano +
  tono mecánico en fondos" coincide con lo que ya midió `estilo.py` en la
  biblia §7 sobre la ficha «Información pública», que habla de "mucha línea").
- **`AoT_Manga_final_panel.png`** (843×460, [Fandom](https://static.wikia.nocookie.net/shingekinokyojin/images/2/29/AoT_Manga_final_panel.png)):
  el **boceto a lápiz sin entintar** que Isayama dibujó en directo para el
  documental *Jōnetsu Tairiku* (MBS, 18-nov-2018) mostrando el layout del
  panel final del manga (una figura adulta cargando a un bebé, globo «お前は
  自由だ» / «tú eres libre»). Confirmado real por el propio programa, no un
  filtrado: [Anime News Network](https://www.animenewsnetwork.com/news/2018-11-18/attack-on-titan-manga-final-panel-previewed-on-tv/.139667)
  y [ComicBook.com](https://comicbook.com/anime/news/attack-on-titan-manga-final-panel-finale-spoilers/)
  · ✅ (dos fuentes, y la imagen del boceto la miré yo mismo: líneas sueltas,
  múltiples pasadas de lápiz sin limpiar, nada de tinta ni trama — es la
  **pincelada cruda** antes del entintado final, útil para un pincel de lápiz
  en Photoshop más que uno de tinta).

### 19.2 Grano de papel

- El papel de la **ficha «Información pública»** ya está medido en la biblia
  §5: `#F2F2F2` (gris neutro, 2.ª pasada) y `#F3F3F3`/`#F4EEEF` en la 1.ª
  medida (F·1-17). Es el papel base del cuadro de diálogo propio de la serie
  (§7); no lo remido, lo cito.
- **Textura libre equivalente (CC0)**: `Paper001` de ambientcg (papel blanco
  liso, sin trama), comprobada hoy por su API — sirve de base antes de poner
  encima el gris medido de la ficha: https://ambientcg.com/view?id=Paper001

### 19.3 Patrones de ropa (revisé si hay estampado, no lo hay)

Miré los 4 visuales grandes de personaje (P·5, P·6, hoja `personajes_01.jpg`)
y el texto de *Appearance* de cada uno en `datos-imagen.md`: **ninguna prenda
de la Legión, la Policía Militar o la Guarnición lleva estampado repetido**.
Son colores planos (verde oliva de la capa, gris del uniforme, marrón de las
correas) con el emblema bordado sólo en la espalda de la capa — no hay una
"tela con patrón" que texturizar, sólo el tejido liso y el cuero de las
correas del equipo de maniobras. Lo digo así (no como «no existe» sin más):
busqué también «uniform pattern/fabric» en el texto de la wiki y en japonés
«制服 柄» sin resultado de un estampado textil.

- **Texturas libres equivalentes (CC0, ambientcg, comprobadas hoy)**:
  - `Fabric019` (lana tejida, blanco, apta para teñir del verde de la capa
    `#1E261F`-`#3C4E3A` ya medido en biblia §5): https://ambientcg.com/view?id=Fabric019
  - `Leather037` (cuero marrón liso, para las correas del equipo de
    maniobras y las botas): https://ambientcg.com/view?id=Leather037

### 19.4 Emblemas y logos

Los 4 emblemas de facción ya están en la biblia con tamaño real (F·19-22,
§2) y uno con hex medido: **Alas de la Libertad** (Legión), azul `#162873` +
blanco `#E3E3E5` + escudo gris `#AFADAB` (§5). No los remido; los uso como
base para el equivalente libre:

- **Vector libre equivalente** (para reconstruir la silueta sin copiar el
  emblema con derechos): colecciones de alas y coronas de laurel en
  [Noun Project](https://thenounproject.com/browse/icons/term/laurel-wreath/)
  (licencia **CC BY** gratis con atribución, o de pago sin atribución) y
  [Vecteezy "Military Wings"](https://www.vecteezy.com/free-vector/military-wings)
  (licencia Vecteezy gratuita con atribución) · ⚠️ ninguno es CC0 puro, los
  dos piden atribución o cuenta de pago para quitarla — decidir cuál usar
  según si el canal puede poner el crédito.
- **Cruce con el punto 23**: el "Regiment Cloak Back Bling" de la colaboración
  de *Fortnite* (abril de 2023, ver 23.1) deja elegir entre **los mismos 4
  emblemas de facción** (Cadetes, Guarnición, Policía Militar o Legión) como
  parche de la capa — confirma que estos 4 logos son los que el propio
  licenciante trata como "el set completo" para merchandising. Fuente:
  [Siliconera](https://www.siliconera.com/fortnite-attack-on-titan-collab-adds-eren-levi-mikasa-and-odm-gear/) · ✅

### Tabla-resumen: texturas y pinceles libres para las 4 capas del punto 19

| Capa | Qué es en la serie | Textura/pincel libre | Licencia |
|---|---|---|---|
| Trama de fondo (manga) | tono mecánico de puntos en fondos, ejemplo en `Manga_Wall_Maria_operation.png` | 34 pinceles "Screentone Halftone" (.abr) en [Brusheezy](https://www.brusheezy.com/brushes/50379-mabecman-s-screentones-halftone-brushes) | ⚠️ gratis para descargar; la página de licencia detallada no cargó el texto completo hoy — revisarla antes de un uso comercial |
| Rayado a mano (sombra) | hatching denso en cuerpos y ropa | pinceles de tinta/rayado del mismo pack de Brusheezy, o dibujar a mano en Photoshop con un pincel de lápiz duro | igual que arriba |
| Pincelada cruda (boceto) | lápiz sin entintar, `AoT_Manga_final_panel.png` | cualquier pincel de lápiz por defecto de Photoshop/CSP (no hace falta descarga) | — |
| Papel | ficha «Información pública», `#F2F2F2` | `Paper001` (ambientcg) | **CC0** |
| Tela de uniforme | capa verde lisa, camisa gris | `Fabric019` (ambientcg) | **CC0** |
| Cuero de correas | equipo de maniobras, botas | `Leather037` (ambientcg) | **CC0** |
| Emblemas/logos | 4 emblemas de facción, F·19-22 | alas/coronas en Noun Project o Vecteezy | CC BY (atribución) |

## Punto 23 · Colaboraciones y cruces

### 23.1 Videojuegos y gacha (poses y ropa nuevas)

- ***Fortnite* × Attack on Titan** (Epic Games, oficial): lanzada el **11 de
  abril de 2023** (Capítulo 4, Temporada 2). Trae a **Eren** (pase de batalla),
  **Levi** y **Mikasa** (tienda), con equipo de maniobras y lanzas de rayo
  jugables, la mochila "Regiment Cloak" personalizable con los 4 emblemas
  (ver 19.4) y una pantalla de carga oficial "A World Without Walls" con arte
  nuevo. ✅ (dos fuentes: [Siliconera](https://www.siliconera.com/fortnite-attack-on-titan-collab-adds-eren-levi-mikasa-and-odm-gear/),
  [The Loadout](https://www.theloadout.com/fortnite/attack-on-titan-mikasa-levi-ackerman-skins)).
- ***Puzzle & Dragons* × Attack on Titan** (GungHo, Japón): colaboración
  repetida; la 2.ª se anunció junto al estreno de la película *Kuinaki Sentaku*
  (otoño de 2015), con Annie y Reiner en su forma titán como evoluciones
  definitivas. ✅ ([QooApp](https://news.qoo-app.com/en/post/10805/qoo-news-puzzle-dragons-x-attack-on-titan-second-collaboration-announced),
  [Anime News Network](https://www.animenewsnetwork.com/news/2015-05-31/puzzle-and-dragons-mobile-game-collaborates-with-attack-on-titan-ghost-in-the-shell-duel-masters/.88749)).
- ***Monster Strike* × Attack on Titan** (Mixi, Japón), **2.ª colaboración
  desde el 1 de mayo de 2023**: trae **10 personajes** nuevos y repetidos,
  entre ellos «Long-Time Comrades-in-Arms» **Hange Zoë y el capitán Levi**,
  y un **Erwin Smith ★6 evolucionado** como personaje exclusivo del pack. Son
  justo 2 de los 5 personajes del encargo con arte nuevo de pose en pareja.
  ✅ ([QooApp](https://news.qoo-app.com/en/post/165419/monster-strike-x-attack-on-titan-2),
  [Pocket Gamer](https://www.pocketgamer.com/monster-strike/attack-on-titan-crossover/)).
- ***Ninjala* × Attack on Titan** (GungHo/Ninjala, Japón): evento de
  colaboración anunciado en la web oficial del juego · ⚠️ una sola fuente
  ([Ninjala oficial](https://ninjalathegame.com/en/news/info/collab-shingeki.html)),
  no comprobé personajes ni fecha exacta por ahorrar tiempo — queda para quien
  amplíe este punto.

### 23.2 Marca de ropa

- **UNIQLO UT × Attack on Titan** (Kodansha): colección lanzada el **30 de
  marzo de 2023** en EE. UU. (fechas distintas por región), **8 diseños**
  para celebrar *The Final Season - The Final Chapters Part 1*. Las
  camisetas recrean **viñetas del manga** (composición y encuadre, no sólo el
  personaje suelto) centradas en Eren y sus 5 compañeros de generación,
  con frases icónicas de la serie. ✅ ([butwhytho](https://butwhytho.net/2023/03/attack-on-titan-uniqlo-collection/),
  [Anitrendz](https://anitrendz.net/news/2023/03/13/uniqlo-to-release-attack-on-titan-ut-collection-on-march-30-in-the-united-states/),
  [Kodansha US](https://kodansha.us/2023/04/14/get-attack-on-titan-gear-at-uniqlo/)).
- **No encontré** una colaboración de la marca de vaqueros *Levi's* con el
  personaje Levi Ackerman (busqué el juego de palabras evidente, en inglés y
  español) · ⚠️ no existe tal colaboración documentada, o no se hizo pública;
  no lo doy por inexistente sin más, pero dos búsquedas no dieron nada.

### 23.3 Cafés temáticos y eventos (con poses y arte nuevo)

- **Tower Records Cafe Omotesando** (Tokio): pop-up del **21-jun al
  9-jul-2019**, con menú temático y una **experiencia VR de 5 minutos** para
  usar el equipo de maniobras y pelear contra un titán (600 yenes aparte). ✅
  ([grape Japan](https://grapejapan.com/116858), confirmado en
  [Geeky Travels & Fandoms](https://geekytravelsfandoms.com/2019/04/30/attack-on-titan-shingeki-no-kyojin-x-animate-cafe/)
  para la cafetería hermana de Animate).
- **Animate Cafe** (Shinjuku e Ikebukuro, 2019): colaboración con menú e
  ilustraciones propias del café · ⚠️ una fuente ([Geeky Travels & Fandoms](https://geekytravelsfandoms.com/2019/04/30/attack-on-titan-shingeki-no-kyojin-x-animate-cafe/)).
- **«Attack on Titan Café: Adolescence Dinner»** (Tokio, BOX cafe&space
  Lumine Est Shinjuku 2), **3-sep al 12-oct-2026** (activo ahora mismo):
  **ilustraciones nuevas de WIT Studio** de los 5 personajes del encargo más
  Armin, con concepto de «última cena antes de la batalla»; llavero acrílico
  aleatorio y mini figuras acrílicas (6 diseños). ✅ ([Anime Corner](https://animecorner.me/attack-on-titan-cafe-opens-in-tokyo-with-new-wit-studio-illustrations/),
  listado en [Japan Pop Now](https://www.japan-pop-now.com/calendar)).
- **Atracción XR «Attack on Titan» en Universal Studios Japan**: *Universal
  Cool Japan 2020* (21-ene al 28-jun-2020), primera atracción XR de la serie
  por el 10.º aniversario del manga; combina raíles físicos y visor de
  realidad virtual («Race For Survival»), con Eren, Mikasa, Armin, Levi,
  Hange y Sasha. Además hubo un restaurante temático, el «Survey Corps Mess
  Hall», con figuras a tamaño real de Levi y Hange. ✅ ([Anime News Network](https://www.animenewsnetwork.com/interest/2020-01-20/oricon-news-gives-inside-look-at-attack-on-titan-xr-ride/.155571),
  [ComicBook.com](https://comicbook.com/anime/news/attack-on-titan-behind-the-scenes-universal-studios-japan-ride-attraction-xr/)).
- **Exposición itinerante «進撃の巨人展FINAL»** (Attack on Titan Exhibition
  FINAL): versión ampliada de la expo de 2014-2015 que recorrió Japón (más de
  450 000 visitantes); la versión FINAL recorrió Asia en 2023, incluida
  **Seúl del 15-jul al 15-oct-2023**. ✅ ([Japan Kuru](https://www.japankuru.com/en/event-calendar/e185/),
  [Pia Corporation (JA)](https://corporate.pia.jp/news/detail_final.html)).
- **Real Escape Game × Attack on Titan** (SCRAP): al menos 5 ediciones desde
  2014 («Escape From a Certain Fortress Town», 2014; «Escape From the Walled
  City», Yokohama→Tokio→Osaka→Singapur→San Francisco→Los Ángeles→Nueva York;
  «Escape From the Amusement Park Surrounded by Titans», Hirakata Park/Tokyo
  Dome City; «Escape From the 5 Titans», 25-feb-2021, temática de *The Final
  Season*). ✅ ([Anime News Network](https://www.animenewsnetwork.com/interest/2016-08-06/latest-attack-on-titan-real-escape-game-story-traps-players-in-a-castle/.104884),
  [CBR](https://www.cbr.com/attack-on-titan-scores-a-second-real-escape-game/),
  [Real Escape Game US](https://realescapegame.com/aotus/)).

### 23.4 Figuras oficiales (su pose es una referencia 3D directa)

Good Smile Company tiene Nendoroid **y** figma de los 5 personajes del
encargo — cada uno con varias caras/expresiones y accesorios que ya son, en
sí, un storyboard de poses en 3D:

| Personaje | Figura | Accesorios / expresiones | Fuente |
|---|---|---|---|
| Levi | Nendoroid n.º 390 | 3 caras (estándar, combate, desdén); equipo de maniobras, doble espada en agarre invertido (su firma) | [goodsmile.info](https://www.goodsmile.info/en/product/4167/Nendoroid+Levi.html) ✅ |
| Levi | figma | 3 caras (estándar, apretando dientes, fría); espadas de acero ultraduro, equipo de maniobras, piezas de mano para el agarre invertido | [goodsmile.info](https://www.goodsmile.info/en/product/4164/figma+Levi.html) ✅ |
| Erwin | Nendoroid | 3 caras (estándar, gritando, sonriendo); equipo de maniobras, doble espada, efectos de vuelo | [goodsmile.info](https://www.goodsmile.info/en/product/6468/Nendoroid+Erwin+Smith.html) + reseña en [Kahotan's Blog](https://mikatan.goodsmile.info/en/2017/05/26/nendoroid-erwin-smith-attack-on-titan/) ✅ |
| Erwin | figma | 3 caras (fulminante, gritando, dientes apretados); espadas, equipo de maniobras, **su caballo incluido**, y su capa de la Legión | [goodsmile.info](https://www.goodsmile.info/en/product/8651/figma+Erwin+Smith.html) ✅ |
| Hange | Nendoroid (relanzada 2023) | 3 caras (estándar, sonriente en batalla, entusiasmada); gafas y hoja de informe de titanes (no sólo combate); **capa con escultura nueva** para más poses de acción | [goodsmile.info](https://www.goodsmile.info/en/product/8251/Nendoroid+Hange+Zoe.html) + [Kahotan's Blog](https://mikatan.goodsmile.info/en/2019/04/16/nendoroid-hange-zoe-attack-on-titan/) ✅ |
| Eren | Nendoroid (versión Titán de Ataque) | caras estándar y de combate; edificio miniatura y una mini-figura de Reiner para recrear la pelea de Trost | [goodsmile.info](https://www.goodsmile.info/en/product/4095/Nendoroid+Eren+Yeager.html) ✅ |
| Eren | figma | 3 caras (decidido, enfadado, en shock); doble espada, equipo de maniobras, efectos de humo | [goodsmile.info](https://www.goodsmile.info/en/product/4089/figma+Eren+Yeager.html) ✅ |
| Mikasa | Nendoroid | 3 caras (estándar, gritando, aturdida); equipo de maniobras, doble espada, efectos de vuelo y **efectos de sangre** para las hojas | [goodsmile.info](https://www.goodsmile.info/en/product/4048/Nendoroid+Mikasa+Ackerman.html) ✅ |

Sirven de referencia 3D directa: cada "cara" es una emoción ya resuelta en
volumen (cruza con el punto 14 de poses y el 13 de caras por emoción, que
hace el investigador de voz).

### 23.5 Cosplay bien hecho (materiales y volumen reales)

- **Titán Acorazado (Reiner Braun) por Hartigan Cosplay** (belga): **381
  horas** de trabajo con **espuma de tapicería, látex prevulcanizado,
  FlexFoam-iT III y resina de poliuretano**; cabeza y manos esculpidas en
  Monsterclay y vaciadas en látex; mandíbula mecánica que se mueve con la
  suya propia y **suelta humo** al abrirse, ojos que brillan. Ganó el 1.er
  puesto en la categoría FX de **Twitchcon Ámsterdam 2022**. Es el ejemplo
  más completo de "materiales y volumen reales" que pide el punto 23: no es
  tela plana, tiene bulto de músculo esculpido y mecanismos que funcionan.
  ✅ ([ScreenRant](https://screenrant.com/attack-on-titan-cosplay-armored-titan/),
  [CBR](https://www.cbr.com/attack-on-titans-armored-titan-awe-inspiring-cosplay/),
  el propio [TikTok de la autora](https://www.tiktok.com/@hartigan_cosplay/video/7124349359692516614) con el detalle técnico completo).
- **Cosplay con licencia libre ya en `datos-imagen.md`** (Openverse, no lo
  repito entero): destaca el grupo de fotos de **Mangoe** como Mikasa en
  Katsucon 2014 (CC BY-NC-ND 2.0) y las de **Xubaet** y **esby.photo** en
  convenciones europeas (CC BY 2.0 y CC BY-NC-SA 2.0) — buena variedad de
  materiales de tela real (bufanda, capa) aunque sin la escala del titán de
  Hartigan.

## Lo mejor para la lámina

1. **Los 4 emblemas de facción** (F·19-22, hex ya medidos) son también el
   "set" que usa el propio licenciante en *Fortnite* — la prueba de que son
   el símbolo más reutilizable de la serie para cualquier objeto (sello,
   parche, cartel) del canal de reglas.
2. **El boceto a lápiz del panel final de Isayama** (`AoT_Manga_final_panel.png`):
   una pincelada cruda, real y con fuente doble, perfecta para una capa de
   "boceto" en una lámina que quiera verse dibujada a mano, no generada.
3. **Figuras oficiales de Good Smile**: cada personaje del encargo tiene ya
   3 expresiones resueltas en 3D (Levi, Erwin, Hange, Eren, Mikasa) — es un
   atajo directo para decidir la cara y la pose sin inventar nada.
4. **El café «Adolescence Dinner» (2026, activo ahora)**: arte nuevo de WIT
   Studio de los 5 personajes juntos, concepto de "última cena" — encaja con
   una lámina de grupo si el canal quisiera una versión 2.
5. **El Titán Acorazado de Hartigan**: referencia de volumen y materiales
   reales si el servidor quisiera un texto sobre "cómo se ve un titán bien
   hecho" en carne (para el investigador de voz o de texto, si les sirve).

## No encontré

- ⚠️ Colaboración de la marca *Levi's* (vaqueros) con el personaje Levi
  Ackerman: busqué en español e inglés, no hay nada documentado. No lo doy
  por inexistente, sólo no lo encontré.
- ⚠️ Fecha y personajes exactos de la colaboración con *Ninjala*: sólo una
  fuente (la web oficial del juego), no la amplié más por ahorrar tiempo del
  repaso corto.
- ⚠️ Texto completo de la licencia de los pinceles de Brusheezy (screentone):
  la página de "License Info" no cargó el detalle hoy; antes de un uso
  comercial habría que abrirla directamente.
- ⚠️ No hice hojas de contacto nuevas para el punto 19/23: `hojas/` ya
  tiene el máximo de 3 JPEG del encargo; las dos páginas de manga y las
  figuras oficiales las describo con su URL directa en vez de montar una
  hoja nueva.

## Bitácora de búsqueda (imagen · repaso corto, 24-sep-2026)

- **`partes/datos-imagen.md`**: revisado, sin repetir sus consultas (no traía
  nada de texturas 2D ni colaboraciones).
- **API de Fandom** (`attackontitan.fandom.com/api.php`), hoy: `list=search`
  con `srnamespace=6` para encontrar páginas de manga sueltas («manga page
  chapter», «insource manga»); `list=allimages` con prefijo «Manga»;
  `imageinfo` con `iiprop=url|size` para medir las 2 imágenes de manga.
  Idioma: inglés (la wiki está en inglés).
- **Bajé y miré con Read** (no de memoria): `Manga_Wall_Maria_operation.png`
  (946×643) y `AoT_Manga_final_panel.png` (843×460), guardados en
  `/tmp/claude-0/trabajo/02-imagen/` (no se sube, es sólo lo pesado).
- **API de ambientcg** (`/api/v2/full_json`), hoy: `type=Material&q=wool`,
  `q=leather`, `q=paper`, `q=canvas` — elegí `Paper001`, `Fabric019` y
  `Leather037` (CC0, comprobado por la propia API del sitio).
- **WebSearch** (14 de las ~50 del cupo, en inglés y español): «Attack on
  Titan Fortnite collaboration skin Eren Mikasa»; «colaboración videojuego
  gacha Puzzle Dragons Monster Strike»; «"Attack on Titan" themed cafe
  collaboration Animate Cafe Tower Records»; «Levi's jeans Attack on Titan
  Levi Ackerman collaboration»; «Good Smile Company Nendoroid Figma Levi
  Mikasa Erwin»; «cosplay ODM gear build materials»; «manga screentone
  Deleter trama Isayama sombreado»; «free CC0 halftone screentone brush
  download license manga»; «Universal Studios Japan attraction XR ride
  exhibition Isayama»; «Uniqlo UT Vans collaboration merchandise»; «goodsmile
  Erwin Smith Nendoroid Figma»; «cosplay "World Cosplay Summit" Levi Mikasa
  armor real»; «Hartigan Cosplay Armored Titan Reiner Braun latex foam»;
  «Monster Strike Attack on Titan collaboration 2023 characters gacha event
  date»; «goodsmile Hange Zoe / Eren Yeager Nendoroid figma pose» (2 más).
- **WebFetch** (4): artículo de ScreenRant (cosplay del Titán Acorazado),
  Siliconera (detalle del collab de Fortnite), Anime Corner (café 2026),
  Brusheezy (licencia de los pinceles de screentone, incompleta).
- **404/403 de hoy**: ninguno; todo respondió a la primera o segunda consulta.
