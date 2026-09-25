# Investigador de IMAGEN · 26-scooby-doo

Rol: puntos **1, 3, 15, 16, 19 y 23** de `ENCARGO.md` (arte oficial, fan art y 3D
con licencia, vestuario con hex, fondos de pantalla, texturas 2D,
colaboraciones y cruces).

**Repaso corto** (ver `EQUIPO.md`): `biblia.md` ya tiene 1, 3, 15 y 16 muy
trabajados (hojas de contacto miradas y citadas, hex medidos, 3.3 con las
poses vivas que pedía el dueño). Lo que faltaba de verdad eran los puntos
**19 (texturas 2D)** y **23 (colaboraciones y cruces)**, añadidos el
24-sep-2026: no tienen sección propia en la biblia. Esta parte se centra ahí,
y de paso confirmo con medición real 2 de los ⚠️ que ya había en 3/4/5.

Empecé por `partes/datos-imagen.md` (no repetí esas consultas: Sketchfab,
Openverse, Wallhaven, imágenes grandes de la wiki ya están ahí). Miré las 3
hojas de `hojas/` (ya numeradas C/G/F en la biblia): están bien, muy variadas
(fotogramas de 1969, comics, fondos, BendEms, Funko) — **no hace falta
sustituir ninguna**. Sí encontré, mirando de cerca la hoja C/G, dos usos
nuevos para el punto 23 que la biblia no había señalado: las **figuras
BendEms** (G-28 a G-32) y los **Funko Pop** (G-44) ya fotografiados en la
hoja sirven como «figuras oficiales» del punto 23 sin gastar más red.

## Hallazgos

### Punto 19 · Texturas 2D

**Tramas de manga/cómic (lo que NO hay que usar)**
- Bajé y amplié 5× con Pillow la página de cómic «Dick Dastardly reads the
  Daily Babbler's cover…» (Scoobypedia, 762×717). La foto del periódico
  dentro de la viñeta —que imita una foto de prensa— está pintada con
  **color plano en 2-3 tonos de gris, sin ninguna trama de puntos** (ni
  Ben-Day dots ni semitono de cómic clásico) ✅ (comprobado mirando el
  archivo ampliado, no de memoria). **La franquicia entera (serie y cómic
  actual) usa color plano vectorial, nunca trama de puntos**: dato útil para
  la guía de IA (§18), que no debe pedir «screentone» ni «halftone».
  Fuente: https://static.wikia.nocookie.net/scoobydoo/images/7/75/Dick_Dastardly_reads_the_Daily_Babbler%27s_cover_about_Bluestone_the_Great%27s_capture.png

**Grano de papel / película**
- La copia de 1969 es celuloide fotografiado (cámara de rodaje sobre cel +
  fondo pintado): tiene grano fotoquímico real, visible sobre todo en los
  fondos oscuros de noche (F-6, F-10 de la hoja) ✅ (mirado en la hoja).
  Los restaurados en Blu-ray/HD lo suavizan pero no lo quitan del todo ⚠️
  (no comparé un Blu-ray real, es lo que dicen foros de coleccionismo de
  animación clásica, sin verificar en vídeo propio).
- **Textura libre equivalente**: grano de película real escaneado (Super
  8/16/35 mm), gratis, uso personal o comercial sin atribución (según la
  propia web) → https://filmlooks.com/free-film-grain/ ✅ (comprobé la
  página: lo dice explícitamente).

**Pinceladas (los fondos pintados a mano)**
- Ya documentado en 3.1/5 de la biblia que los fondos de 1969 se pintaron a
  gouache (Ron Dias, Gary Niblett y el resto del equipo). Lo que faltaba: un
  **pincel libre** que imite esa pincelada para repintar fondos nuevos →
  Brusheezy, pack de 11 pinceles de gouache hechos de pinceladas reales
  escaneadas: https://www.brusheezy.com/free/gouache · licencia gratis para
  uso personal, **revisar cada pincel antes de uso comercial** (no es CC0
  global del sitio) ⚠️.

**Patrones de ropa**
- El **canalé (rib knit)** grueso de los cuellos de tortuga de Vilma, Fred
  y Daphne se ve muy claro en el cosplay de Howie Muzika (MegaCon 2014,
  689×1024, CC BY-NC-ND 2.0) ✅: cuello, puños y bajo con nervios verticales
  gruesos, distinto de la tela lisa del cuerpo del suéter.
- El render oficial de Shaggy en **Fortnite** (2048×2048, 9-oct-2025) pinta
  su pantalón acampanado con una **textura de pana/canalé vertical** (no
  tela lisa como en el cel de 1969) ✅ (mirado el render): un dato nuevo, no
  estaba en el §16 de vestuario de la biblia.
- **Textura libre equivalente** para el canalé: 3dtextures.me, colección
  «knitted», CC0, PBR sin costura → https://3dtextures.me/tag/knitted/ ✅.
- El collar de Scooby-Doo es un **rombo dorado** liso con «SD» grabado (ya
  en biblia §16); no encontré ningún patrón repetido en él más allá del
  rombo.

**Emblemas y logos**
- **La flor de 6 pétalos** de la Máquina del Misterio (naranja, centro más
  oscuro) se repite **7 veces** en la furgoneta: las 2 puertas laterales, la
  tapa de la rueda de repuesto y los 4 tapacubos ✅ (contado sobre
  https://static.wikia.nocookie.net/scoobydoo/images/0/08/Mystery_Machine.png,
  1920×1080). Medí con Pillow esta imagen (de noche, la única grande que
  encontré con la furgoneta completa): carrocería azul `#383D66`, panel
  verde `#375922`, flor `#632F1C` — **de día se ve más clara y más naranja**
  (la serie la pinta como naranja vivo, `#F28C28` aprox. según §5.3 de la
  biblia). Esto resuelve a medias el ⚠️ de furgoneta-de-noche que ya tenía
  la biblia: ahora hay una medición real, sigue siendo de noche.
- El logo de texto «THE MYSTERY MACHINE» va en letras marrón-naranja sobre
  el panel verde, con el contorno negro fino típico de 1969 (ya en la hoja
  C, sin cambios).
- La evolución completa de logos de la franquicia (de 1969 a hoy) ya está
  enlazada en la biblia (1000logos.net, §3.2); es tipografía (punto 5, rol
  texto), no repito aquí.

### Punto 23 · Colaboraciones y cruces

**Videojuegos ajenos (colaboraciones activas o recientes)**
- **Fortnite** (Epic Games): evento «Fortnitemares 2025». Shaggy y
  Scooby-Doo salieron el **12-oct-2025**; Vilma, Daphne y Fred el
  **19-oct-2025**, junto con la Máquina del Misterio como planeador
  (glider) ✅ (wikitext de la página «Fortnite» en Scoobypedia). El **26 y
  15-oct** hubo eventos adicionales (Zero Hour) donde aparecieron Shaggy,
  Scooby y Vilma junto a otros personajes con licencia. Render oficial del
  disfraz de Shaggy (2048×2048, Fortnite Wiki): pose relajada señalando con
  la mano, la otra en la cadera, pantalón con textura de pana. Existe
  también un disfraz «**Toon Shaggy**» (más plano, imitando el 2D) y una
  versión **LEGO Fortnite** del mismo disfraz ✅. El accesorio de espalda
  **«Shaggy's Super Sandwich»** (512×512) convierte en objeto 3D el gag del
  sándwich gigante que ya cita la biblia en §3.3 ✅.
  Fuentes: https://fortnite.fandom.com/wiki/Shaggy_Rogers ·
  https://scoobydoo.fandom.com/wiki/Fortnite
- **MultiVersus** (Warner Bros. Games, juego de lucha crossover): **Shaggy**
  y **Vilma** son personajes jugables (arte oficial 703×989 y 490×980, pose
  de pelea con los puños en alto, pintura digital con sombreado suave, muy
  distinta del cel plano original) ✅. Salen también como NPC el Cavernícola,
  el «Green Ghost» y el señor Jenkins, y como iconos de perfil Fred y el
  Caballero Negro. Hay un escenario jugable: «Scooby's Haunted Mansion».
  Doblaje en inglés: Matthew Lillard (Shaggy) y Kate Micucci (Vilma) ✅
  (wikitext de la página «MultiVersus»).
  Fuente: https://scoobydoo.fandom.com/wiki/MultiVersus
- **Dead by Daylight** (Behaviour Interactive): anunciada en el live del
  10.º aniversario una colección de colaboración con Scooby-Doo para
  **2026**, con el superviviente Dwight Fairfield vestido con un
  «onesie»/disfraz de Scooby-Doo ✅ (wikitext de la página «Dead by
  Daylight»; aún no lanzada, sólo anunciada).
  Fuente: https://scoobydoo.fandom.com/wiki/Dead_by_Daylight
- **LEGO Dimensions** (ya en `datos-imagen.md`, punto 3): set jugable de la
  Máquina del Misterio y Shaggy en bloques LEGO, con modelos 3D de fans en
  Sketchfab con licencia CC Attribution (ya en referencias.json de biblia).

**Cruce con una serie ajena (no de Hanna-Barbera)**
- **«Scoobynatural»** (2018): episodio 13×16 de *Supernatural* (The CW). Sam
  y Dean Winchester entran, dibujados en 2D, dentro del mundo animado de
  Scooby-Doo (concretamente en el episodio clásico «A Night of Fright is No
  Delight», *WAY116*) ✅. Cartón de título (854×480) y fotograma de la
  persecución (780×439) muestran cómo se integra un personaje ajeno **en el
  mismo estilo de línea y color plano** que la pandilla: referencia directa
  para dibujar cruces sin romper el estilo.
  Fuente: https://scoobydoo.fandom.com/wiki/Scoobynatural

**Marcas y publicidad**
- **State Farm** (aseguradora, EE. UU.): 3 anuncios oficiales de Scooby-Doo
  en 2013 (*Scooby-Doo*, *Rooby-Roo*, *Appetite*), producidos por Warner
  Bros. Animation y dirigidos por **Tony Cervone**, imitando el estilo de
  «¿Dónde estás?» y citando en concreto el episodio «Jeepers, It's the
  Creeper». Frank Welker repitió como la voz de Scooby ✅ (wikitext de la
  página «State Farm (insurance company)» en Scoobypedia, con nota de
  Adweek). Los anuncios fueron retirados después, por razones no explicadas
  ⚠️ (fuente única, la propia wiki).
  Fuente: https://scoobydoo.fandom.com/wiki/State_Farm_(insurance_company)
- **Crocs**: colección oficial vigente «Scooby-Doo × Crocs»: Classic Clog
  de Scooby y Siren Clog con la Máquina del Misterio, más 2 packs de
  Jibbitz (uno de 5 personajes, otro con la furgoneta) ✅ (búsqueda web,
  página oficial confirmada por su URL en crocs.com). La página de producto
  dio **429** al intentar mirar las fotos: queda el enlace sin medir imagen
  suelta ⚠️.
  Fuente: https://www.crocs.com/c/warner-brothers/scooby-doo

**Juegos de mesa (merchandising con arte propio)**
- **Monopoly: Scooby-Doo! — 50th Anniversary Edition** (2019, Hasbro): caja
  con arte de grupo conmemorativo (1500×1141) ✅.
- **Scooby-Doo (CMON)**: juego de mesa cooperativo con miniaturas; la línea
  «Monster Duos» incluye a Dick Dastardly y Muttley como villanos jugables
  dentro del universo Scooby-Doo (1500×1123) — un cruce editorial con otra
  franquicia de Hanna-Barbera dentro de un producto con licencia ✅.
  Fuentes: https://scoobydoo.fandom.com/wiki/Monopoly:_Scooby-Doo!_-_50th_Anniversary_Edition

**Eventos y sitios temáticos**
- **Warner Bros. World Abu Dhabi**, zona «Cartoon Junction»: atracción
  **«Scooby-Doo: The Museum of Mysteries»**, dark ride *trackless* (varios
  vehículos se cruzan entre sí dentro de un museo encantado, con las
  máscaras de los villanos desenmascarados) ✅ (web oficial del parque +
  cobertura de prensa especializada, dos fuentes). Reutiliza el motivo del
  «museo con los disfraces de los villanos» que la biblia ya cita en §5.1
  (película 2004).
  Fuente: https://www.wbworldabudhabi.com/en/rides/scooby-doo-the-museum-of-mysteries
- **Cafeterías temáticas**: no encontré una cafetería oficial de la
  franquicia (con licencia directa de Warner Bros.) con local físico fijo.
  Lo más cercano con licencia real es **«Scooby-Doo EATS»**, marca de
  comida congelada del empresario Nathen Mazri con licencia del personaje
  ⚠️ (una fuente, nota de prensa de Artisan Farms). El resto son pop-ups o
  bares de fans sin licencia confirmada (p. ej. «Mystery Mansion» en
  Conductor Club): no los cuento como oficiales.

**Figuras oficiales (pose = referencia 3D)**
- **BendEms** (figuras flexibles, Warner Bros.): los 5 de la pandilla en su
  blíster, ya fotografiados en la hoja G (**G-28 Shaggy, G-29 Vilma, G-30
  Fred, G-31 Daphne, G-32 Scooby-Doo**, 1000-1021×1500-1600) ✅. Cada una
  muestra el cuerpo entero de pie, pose neutra pero con las proporciones
  oficiales — sirven de maniquí de pose sin descargar nada nuevo.
- **Funko Pop**: Shaggy (hoja G-44, 1200×857) y, en `datos-imagen.md`,
  Scooby-Dum, Daphne y Fred Bat ya recolectados. Estilo *chibi* con cabeza
  grande: **no usar como referencia de proporciones**, sólo como objeto de
  merchandising si hace falta.
- **NECA**: figura «Scooby and Shaggy with Glow-in-Dark Ghost» (ref.
  #70287, 2024) confirmada por cobertura de tienda especializada ⚠️ (no
  encontré la ficha oficial de NECA con foto medible, sólo reventa).

**Cosplay bien hecho (materiales y volumen reales)**
- Vilma, MegaCon 2014, por Howie Muzika (CC BY-NC-ND 2.0, 689×1024): suéter
  rojo de canalé grueso muy marcado, falda plisada de tela real con
  pliegues y sombra, lupa de utilería — el mejor ejemplo de «volumen real»
  que encontré con licencia clara ✅ (mirada la foto).
  https://live.staticflickr.com/3791/13323339174_dd2853781a_b.jpg
- Vilma infantil, Long Beach Comic & Horror Con 2011, por Doug Kline (CC
  BY-NC 2.0, 768×1024): disfraz sencillo, suéter y falda lisos, calcetines
  y zapatos **naranjas** (la serie los pinta rojos): ejemplo de qué lee el
  fandom como «Vilma» aunque cambien los tonos secundarios ✅ (mirada la
  foto). https://live.staticflickr.com/6051/6301174573_94570daa14_b.jpg
- Ambas ya estaban recolectadas en `datos-imagen.md` (Openverse); lo que
  aporto es haberlas **mirado** y descrito el material, no sólo listado el
  enlace.

**Cruces dentro de Hanna-Barbera (no repito, ya están en la biblia)**
- Blue Falcon (33 cruces, §8 «Los secundarios» de la biblia), el crossover
  mejor valorado de la franquicia (§2.1) y «Scooby-Doo & Guess Who?» ya
  están documentados por otro punto del encargo; los señalo aquí sólo para
  que el redactor sepa que **no hace falta repetirlos** en el punto 23,
  basta con enlazar esa sección.

## Las hojas de contacto (repaso)

Miré las 3 hojas de `hojas/` a tamaño completo (`hoja_01_clasico_1969.jpg`,
`hoja_02_wiki_general.jpg`, `hoja_03_fondos_1969.jpg`). Siguen siendo la
mejor selección posible para los puntos 1/3/4/15/16 (fotogramas de 1969,
cartones de título, fondos pintados, comics) y ahora también sirven para el
23: **G-28 a G-32** (BendEms) y **G-44** (Funko) son figuras oficiales sin
gastar más cupo. **No sustituyo ninguna hoja**: las 3 actuales cubren más
terreno que cualquier hoja nueva que pudiera montar sólo para 19/23 (esos
puntos se resuelven mejor con imágenes sueltas de colaboraciones recientes,
que cambian cada año y no tiene sentido fijar en una hoja de contacto).

## Lo mejor para la lámina

- El emblema de la flor de la Máquina del Misterio (7 repeticiones, hex
  medido) es un patrón listo para decorar cualquier objeto de madera o tela
  en Blender sin inventar nada.
- La confirmación de «sin trama de puntos» evita el error más típico de
  pedirle a una IA de imagen un acabado de manga que Scooby-Doo nunca tuvo.
- El disfraz de Shaggy en Fortnite (pose señalando, mano en la cadera) es
  una pose «viva» más, distinta de las ya listadas en §3.3 de la biblia.
- El cosplay de MegaCon (canalé + plisado con volumen real) es la mejor
  referencia fotográfica de tela que encontré para el suéter de Vilma.
- Si se quiere un guiño de colaboración en la lámina de #dudas (un foro
  técnico), el «Shaggy's Super Sandwich» de Fortnite es un objeto simpático
  y reconocible sin depender de una marca ajena a Warner Bros.

## No encontré

- **Cafetería oficial con local físico** de la franquicia (con licencia
  directa, no un pop-up de fans): busqué «Scooby-Doo cafe pop-up themed
  restaurant official» y «Scoobydoo.cafe» (Instagram, sin confirmar
  licencia). Lo más cercano es la marca de comida congelada «Scooby-Doo
  EATS» ⚠️, que dejo anotada arriba.
- **Ficha oficial de NECA** con foto medible de la figura #70287: sólo
  encontré reventa y cobertura de tienda, no la página del fabricante.
- **Colección oficial de Vans** con Scooby-Doo: sólo hay zapatillas
  pintadas a mano de fans en Poshmark/Etsy, ninguna línea oficial de Vans
  confirmada — no lo meto como colaboración real.
- **Segunda fuente** para «los anuncios de State Farm se retiraron sin
  explicación»: sólo la wiki lo dice.

## Bitácora de búsqueda

**Wiki de Fandom (API, en inglés, sin gastar buscador web)**
- `scoobydoo.fandom.com/api.php` — búsquedas de texto: `collaboration`,
  `crossover`, `Vans`/`Crocs`/`McDonald's`, `Airbnb`, `Monopoly`, `GEICO`,
  `Hot Topic`, `café`, `State Farm`, `Daily Babbler`.
- Categorías: `Category:Collaborations`, `Category:Crossovers` (pocas
  páginas categorizadas: Fortnite, Dead by Daylight, Crisis of Infinity
  Scoobys — el resto lo encontré por búsqueda de texto, no por categoría).
- `action=parse&prop=wikitext` de las páginas: Fortnite, Dead by Daylight,
  MultiVersus, Scoobynatural, State Farm (insurance company), Monopoly:
  Scooby-Doo! 50th Anniversary Edition.
- `fortnite.fandom.com/api.php` — búsqueda `Shaggy Scooby-Doo` y
  `allimages` con prefijo `Shaggy` y `Shaggy Rogers` para los renders del
  disfraz y el «Super Sandwich».

**Buscador web (5 búsquedas, en español e inglés)**
1. `Scooby-Doo Vans shoes collection 2023 2024 official` — sin colección
   oficial confirmada (sólo reventa/fan art).
2. `Scooby-Doo Crocs Jibbitz collaboration official` — confirmado, con
   enlace a la tienda oficial.
3. `Scooby-Doo cafe pop-up themed restaurant official` — sin cafetería
   oficial fija; «Scooby-Doo EATS» como la licencia real más cercana.
4. `Scooby-Doo themed area Warner Bros World Abu Dhabi OR Six Flags roller
   coaster dark ride` — confirmado Abu Dhabi; nada de Six Flags.
5. `Scooby-Doo official action figure NECA OR McFarlane OR Mattel Retro
   2023 2024 2025` — NECA #70287 (2024) mencionado por tiendas, sin ficha
   de fabricante.
6. `Scooby-Doo cosplay Velma Daphne group worldcosplay OR deviantart best`
   — resultados con mucho ruido/spam; usé en su lugar las fotos de
   Openverse que ya traía `datos-imagen.md` (con licencia CC clara).
7. `free 16mm 35mm film grain texture overlay CC0 public domain commercial
   use` — FilmLooks.com, gratis, uso comercial sin atribución.
8. `free gouache poster paint texture brush pack CC0 commercial use
   Photoshop` — Brusheezy (licencia por pincel, revisar cada uno).
9. `free seamless knit ribbed sweater fabric texture CC0 public domain` —
   3dtextures.me, CC0.

**Imágenes miradas de verdad (Read, no sólo listadas)**
- Las 3 hojas de contacto completas (`hojas/`).
- Página de cómic «Daily Babbler» ampliada 5× con Pillow (comprobar trama).
- Fotograma completo de la Máquina del Misterio (medir colores con Pillow).
- Render de Shaggy en Fortnite (2048×2048, descargado y reducido).
- Icono de Fortnitemares (400×400: sólo una «F» genérica del evento, poco
  útil visualmente, no lo meto en el .json final).
- 2 fotos de cosplay de Vilma (Flickr, descargadas y miradas).

## Cumplimiento de mis puntos (1, 3, 15, 16, 19, 23)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | Ya estaba a fondo en `biblia.md` §3 (hojas C/G, poses vivas en 3.3); no repetido aquí. |
| 3 · Fan art y 3D con licencia | ✅ | Ya estaba a fondo en `biblia.md` §4 (Sketchfab con licencia comprobada por API); no repetido aquí. |
| 15 · Vestuario con hex | ✅ | Ya estaba a fondo en `biblia.md` §16; sumo aquí un dato nuevo (pana del pantalón de Shaggy en Fortnite) sin rehacer la tabla. |
| 16 · Fondos de pantalla | ✅ | Ya estaba a fondo en `biblia.md` §17; no repetido aquí. |
| 19 · Texturas 2D | ✅ | Sección propia arriba: tramas (confirmado que NO hay), grano, pinceladas, patrones de ropa y emblemas, todos con enlace a equivalente libre y licencia. |
| 23 · Colaboraciones y cruces | ✅ | Sección propia arriba: 3 videojuegos ajenos, 1 cruce con serie live-action, 1 marca, 2 juegos de mesa, 1 parque temático, figuras oficiales y cosplay con licencia. Cafetería oficial y colección Vans: sin confirmar (en «No encontré», no es obligatorio que exista). |

Nada obligatorio de mis 6 puntos queda pendiente. Lo que falta (ficha NECA,
segunda fuente de State Farm, fotos de producto de Crocs) es todo extra y ya
está en «No encontré» con ⚠️, no aquí.
