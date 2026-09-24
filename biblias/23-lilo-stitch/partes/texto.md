# Parte · Investigador de TEXTO, JUEGOS Y TÉCNICA · Lilo & Stitch (23-lilo-stitch)

Puntos de `ENCARGO.md`: **5** (tipografía), **6** (cuadros de diálogo), **11**
(videojuegos), **18** (estilo de dibujo y técnica, cómo replicarlo), **24**
(obras parecidas) y **25** (mundo y símbolos).

Parto de `partes/datos-texto.md` (casi vacío: la película no es serie de
AniList ni tiene etiqueta en Danbooru, así que `recolectar.py` no trajo casi
nada) y de `biblia.md` ya existente (hecha con la red cerrada, sin ver
ninguna imagen ni vídeo — lo dice su propio recuadro «Cómo se hizo»). Mi
trabajo de hoy es con la **red abierta**: miré cómics reales, capturas de
videojuego, modelos 3D y letras, cosa que la pasada anterior no pudo hacer.
No repito lo que la biblia ya tiene confirmado (§6 tipografía, §7 diálogo,
§13 videojuegos); lo amplío, lo verifico con imágenes y **añado los puntos
18, 24 y 25, que en la biblia actual no existen todavía** (se saltó, porque
esta biblia es de antes del 24-sep-2026, cuando se añadieron esos 3 puntos
al encargo).

Formato: un dato por línea, fuente enlazada, ✅ (dos fuentes) o ⚠️ (una).

---

## Punto 5 · Tipografía

### 5.1 El logo oficial (confirmado con imagen)

- Logo oficial «Lilo & Stitch»: rótulo a mano, letras redondas muy gruesas,
  algo infladas, bailando sobre la línea, en rojo con contorno blanco ✅
  (imagen oficial medida por su API: **800×620 → en realidad 800×310 px**,
  [Fandom disney, `File:Lilo & Stitch Logo.png`](https://static.wikia.nocookie.net/disney/images/9/9d/Lilo_%26_Stitch_Logo.png/revision/latest?cb=20160630120430),
  necesita `Referer: https://www.fandom.com/`). La vi directamente.
- La copia que circula en internet con ese look se llama **«Buka Bird»**, de
  Steve Ferrera, **gratis sólo para uso personal** ✅ (ya confirmado en
  `biblia.md` §6 con 3 fuentes: FontMeme, FontBolt, Fontspace.io). No pude
  bajarla hoy tampoco (no está en Google Fonts ni GitHub) para comprobar
  tildes con fontTools ⚠️: si el dueño la quiere, hay que comprar la
  licencia comercial o pedir permiso a Ferrera.
- **Variante del logo en el videojuego de Game Boy Advance** (2002,
  Digital Eclipse): el mismo rótulo rojo-con-blanco pero **metido dentro de
  una tabla de surf**, con un borde verde de florecitas blancas alrededor
  («Disney's» arriba en letra fina). La vi yo mismo en la pantalla de
  título ✅ (captura propia, ver `gba/s12.png` en la carpeta de trabajo;
  fuente [archive.org/details/stitch_gba](https://archive.org/details/stitch_gba),
  480×320 px, el tamaño real del hardware). Es una **variante de logo lista
  para usar en un objeto físico** (una tabla de surf, un cartel de playa):
  útil si la lámina quiere un guiño al merchandising sin copiar el logo
  principal 1:1.
- **Variante del logo en el manga japonés** *Tono-sama to Stitch* / *Stitch
  & the Samurai* (2020-2021, ver §24): la portada usa un título distinto,
  en trazo de pincel más anguloso y con sangre/tinta roja, estilo cartel de
  samurái — nada que ver con el redondeado de Disney. La vi yo mismo
  (portada, 432×648 px, [TOKYOPOP](https://tokyopop.com/collections/disneymanga/products/9781427868961_disney-manga-stitch-and-the-samurai-volume-1))
  ✅. Sirve para mostrar que la franquicia **cambia de letra según el
  contexto cultural**; no la recomiendo para #fotos (es demasiado alejada
  del tono Disney/Hawái del canal).

### 5.2 Ocho letras libres, una por uso (comprobadas hoy con fontTools)

Bajé cada letra directa de `fonts.gstatic.com` (la URL real que da la API
`css2` de Google Fonts) y comprobé con `fontTools.ttLib` si el cmap trae
**á é í ó ú ñ Ñ ¿ ¡**. Las 8 están completas ✅ (verificación propia, hoy).
Las 4 primeras ya estaban en la biblia (las revalidé); las 4 últimas son
**nuevas**, para los usos que la biblia todavía no cubría (globo de cómic,
grito, cartel del mundo, interfaz):

| Uso (punto 5 del encargo) | Letra | Diseñador/fundición | Licencia | Tildes ñ ¿¡ |
|---|---|---|---|---|
| **Logo o título** | Lilita One | Juan Montoreano | OFL | ✅ completa |
| **Pensamiento** (burbuja de nube, blanda) | Baloo 2 | Ek Type | OFL | ✅ completa |
| **Onomatopeya** (fuerte, de cómic clásico) | Luckiest Guy | Astigmatic | OFL | ✅ completa |
| **Créditos / pie de foto a mano** | Gochi Hand | HT Fonts | OFL | ✅ completa (ya en biblia) |
| **Globo normal de cómic** ⭐ nuevo | **Comic Neue** (Bold) | Craig Rozynski | OFL | ✅ completa |
| **Grito / exclamación** ⭐ nuevo | **Bangers** | Vernon Adams | OFL | ✅ completa |
| **Cartel del mundo** (tiki, surf, luau) ⭐ nuevo | **Trade Winds** | Sideshow | OFL | ✅ completa |
| **Interfaz de juego / HUD** ⭐ nuevo | **Actor** | Sorkin Type Co. | OFL | ✅ completa |
| **Subtítulos o créditos de vídeo** ⭐ nuevo | **Quicksand** | Andrew Paglinawan | OFL | ✅ completa |

- **Comic Neue** está diseñada explícitamente como «un Comic Sans mejor
  para cómics»: encaja perfecto con el globo normal que vi en el cómic real
  (§6.1) ✅ [Google Fonts](https://fonts.google.com/specimen/Comic+Neue).
- **Trade Winds** tiene look de cartel de tiki-bar / luau de los años 50:
  la recomiendo para un letrero dentro del mundo (un cartel de tienda de
  surf, no para el título del canal) ✅ [Google Fonts](https://fonts.google.com/specimen/Trade+Winds).
- **Actor** es una sans condensada de aire «pantalla de nave espacial»,
  coherente con la tecnología de Jumba y la Federación Galáctica (§25) ✅
  [Google Fonts](https://fonts.google.com/specimen/Actor).
- Recomendación final para #fotos: **Lilita One** para «Fotos» (el título
  del canal), **Gochi Hand** para los pies de foto a mano de Lilo, y si se
  usa un bocadillo de cómic, **Comic Neue Bold**.

---

## Punto 6 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

**Esto es lo más importante del encargo** («la lámina NO lleva una burbuja
blanca genérica»). La biblia ya tiene bien cubierta la película (no hay
globos, todo es voz en off, con la lista de escenas y minutos en su §7). Lo
que yo aporto hoy es lo que la red cerrada no pudo dar: **cómics reales de
la franquicia, vistos con mis propios ojos**, que sí tienen bocadillo.

### 6.1 El bocadillo real de la franquicia (visto directamente)

Miré 3 páginas del cómic **Dynamite Entertainment, *Disney's Lilo & Stitch*
#1** (2024, guion Greg Pak, dibujo Giulia Giacomino), bajadas de la
[preview de DuckTalks](https://ducktalks.com/2024/01/03/dynamite-comics-lilo-stitch-1-preview/)
(1988×3057 px cada página, medidas por mí) ✅:

- **Bocadillo normal**: óvalo blanco, borde negro de 3-4 px, cola recta
  hacia quien habla. Letra en **mayúsculas, sans-serif redondeada y
  gruesa** (muy parecida a Comic Neue Bold), con palabras clave en
  **cursiva y más gruesas** para dar énfasis («*BLOW* up», «*responsible*
  older sister», «*'OHANA*»). No hay línea fina de cómic clásico
  americano: es una letra más suave, a juego con lo redondeado de los
  personajes.
- **Cartela de flashback/aparte**: rectángulo con esquinas redondeadas,
  fondo **azul pálido** (no blanco), mismo tipo de letra, para el «Look,
  you can't... you can't just blow things up!» de Nani en modo recuerdo.
- **No hay bocadillo de pensamiento ni onomatopeyas** en las páginas que vi
  (⚠️ dato de sólo 3 páginas de 1 cómic; puede haber en otros números).
- **Frase encontrada, en el propio cómic**: «**'OHANA MEANS FAMILY. AND
  FAMILY MEANS NO ONE GETS LEFT BEHIND OR FORGOTTEN, RIGHT?**» — «**RIGHT.**»
  (David a Nani, cómic #1, 2024) ✅. Es la **misma frase icónica** de la
  película (ahí sale de Lilo a Stitch), reescrita en el cómic: **doble
  fuente independiente** para la frase más citada de toda la franquicia.
- **Vocabulario hawaiano metido tal cual en el globo, en cursiva**:
  «**'Ohana**», «**Kuleana**» (responsabilidad — cuidar de los demás y del
  entorno) y «**Mālama 'āina**» (cuidar la tierra) ✅ (vistas en la página;
  significado confirmado en 2 fuentes: [Ko Olina](https://koolina.com/destination/kuleana/),
  [NOAA Sanctuaries](https://sanctuaries.noaa.gov/magazine/6/kuleana.html)).
  Es vocabulario real del mundo (ver también §25): útil para un texto corto
  tipo «Kuleana: sube lo que hiciste tú» en el canal.
- **Conclusión para la lámina**: si hace falta un bocadillo, que sea **el
  óvalo blanco de borde grueso con letra Comic Neue Bold en mayúsculas**,
  nunca la burbuja plana estilo chat/messenger. Esto confirma y afina lo
  que ya decía la biblia en su §7.5 («qué NO hacer»).

### 6.2 Cómics de la franquicia (mapa completo)

- **Disney Adventures *Comic Zone*** (2002-2007): tiras cortas en la
  revista infantil; compiladas en *Comic Zone Volume 1: Disney's Lilo &
  Stitch* (2006) ✅ ([Disney Wiki](https://disney.fandom.com/wiki/Comic_Zone_Volume_1:_Disney%27s_Lilo_%26_Stitch),
  [Lilo & Stitch Wiki](https://liloandstitch.fandom.com/wiki/Comic_Zone_Volume_1:_Disney%27s_Lilo_%26_Stitch)).
- Dato curioso de participación: en mayo de 2006 Disney Adventures publicó
  **«Stitch's Movie Mix-Up»**, una versión de la tira **con los bocadillos
  vacíos** para que los niños escribieran su propio diálogo y lo mandaran a
  la revista ✅ (2 fuentes: [Lilo & Stitch Wiki](https://liloandstitch.fandom.com/wiki/Comic_Zone_Volume_1:_Disney%27s_Lilo_%26_Stitch),
  reflejado también en [TV Tropes, *Comic Zone: Lilo & Stitch*](https://tvtropes.org/pmwiki/pmwiki.php/ComicStrip/ComicZoneLiloAndStitch)
  vía buscador, la web en sí me dio 403 hoy). Es la prueba de que el
  bocadillo vacío **ya se usó de verdad** con esta franquicia como juego
  participativo — una idea reutilizable para el foro de #fotos («escribe
  tú el pie de foto»).
- **Dynamite Entertainment, *Lilo & Stitch*** (2024-en curso), guion Greg
  Pak: la serie activa ahora mismo, la que vi en 6.1 ✅.
- **Manga *Tono-sama to Stitch* / *Stitch & the Samurai*** (2020-2021,
  Japón): ver §24, no pude ver páginas interiores (sólo la portada) ⚠️.

### 6.3 En los videojuegos

Ningún juego de la franquicia tiene una caja de diálogo tan icónica como la
de Pokémon o Undertale (confirmado en biblia §7.4 y ampliado en mi §11): no
la uses como referencia central.

---

## Punto 11 · Videojuegos de la franquicia

### 11.1 Lista completa (más larga que la de la biblia, que sólo tenía TCRF)

Saqué la lista completa del wikitext de la ficha de franquicia ✅
([Disney Wiki, *Lilo & Stitch (franchise)*](https://disney.fandom.com/wiki/Lilo_%26_Stitch_(franchise)),
contrastada con [Wikipedia](https://en.wikipedia.org/wiki/Lilo_%26_Stitch_(franchise))):

| Juego | Año | Plataforma | Nota |
|---|---|---|---|
| *Lilo & Stitch* | 2002 | GBA (Digital Eclipse) | Plataformas; **vi la pantalla de título yo mismo**, ver 11.2 |
| *Lilo & Stitch Pinball* | 2002 | PC | — |
| *Lilo & Stitch: Trouble in Paradise* | 2002 | PS1/PC (Blitz Games) | Plataformas; prototipo y código fuente filtrados en 2023 (ya en biblia §13) |
| *Lilo & Stitch: Hawaiian Adventure* | 2002 | PC | Minijuegos de cultura hawaiana (ya en biblia §13) |
| *Disney's Stitch: Experiment 626* | 2002 | PS2 | Stitch en el espacio (ya en biblia §13) |
| *Lilo & Stitch 2: Hämsterviel Havoc* | 2005 | GBA/PC | Secuela del de 2002 |
| *Stitch Jam* | — | móvil/flash | — |
| **Motto! Stitch! DS** ⭐ | 2008 | Nintendo DS | **Sólo salió en Japón** — no lo tenía la biblia |
| *Kingdom Hearts II* | 2005 | PS2 | Stitch invocación |
| *Kingdom Hearts: Birth by Sleep* | 2010 | PSP | Mundo Deep Space (ya en biblia §13); aquí debuta **Sparky/Experimento 221** como personaje jugable de apoyo |
| *Disney Magical World* / *2* | 2013/2017 | 3DS | Stitch como vecino |
| *Disney Infinity* / *2.0* | 2013/2014 | multi | Figura de Stitch |
| *Disney Heroes: Battle Mode* | 2018 | móvil | — |
| *Disney Dreamlight Valley* | 2022 | multi | Ya en biblia §13, con fuente ampliada abajo |
| *Disney Speedstorm* | 2023 | multi | Carreras, Stitch como piloto |

- **Cruce con otra franquicia Disney**: el **Experimento 619 «Splodyhead»**
  (uno de los «primos» de Stitch) aparece como personaje secundario en la
  película ***Big Hero 6*** (2014) ✅ ([Disney Wiki, franquicia](https://disney.fandom.com/wiki/Lilo_%26_Stitch_(franchise))).
  **Aviso para el redactor**: el servidor ya tiene una biblia de Big Hero 6
  (`biblias/08-big-hero-6-grandes-h-roes/`); vale la pena decirlo ahí
  también si se hace un repaso, son el mismo universo compartido de Disney.
- El **Experimento 221 «Sparky»** en *Kingdom Hearts: Birth by Sleep* fue
  el primer caso de un personaje introducido en una serie de TV de Disney
  (no en el cine) que llegó a un *Kingdom Hearts* ✅ (misma fuente).

### 11.2 Lo que vi con mis propios ojos

- **Pantalla de título del GBA (2002)**, capturas propias medidas: 480×320
  px, bajadas de [archive.org/details/stitch_gba](https://archive.org/details/stitch_gba)
  ✅. El logo va dentro de una tabla de surf (ver §5.1); «PRESS START» en
  amarillo con contorno negro, letra de bloque pixelada. **No encontré
  capturas de una escena de juego real ni de un cuadro de diálogo** en el
  volcado de Internet Archive (sólo grabó la introducción/título, ⚠️ lo
  intenté 2 veces con distintos números de captura, 01-06 y 12-27, y salió
  siempre la misma pantalla). MobyGames y TCRF, que sí tienen capturas de
  niveles, me dieron **403** (Cloudflare) — lo anoto y no insisto más.
- **Disney Dreamlight Valley**: la caja de diálogo del juego **no la pude
  ver** hoy tampoco (Steam necesita el juego instalado; no hay clips
  cortos con capturas claras en las fuentes que revisé) ⚠️, sigue igual que
  en la biblia §13.

### 11.3 Conclusión (igual que la biblia, reforzada)

Ningún juego de la franquicia dejó una caja de diálogo reconocible al
instante (nada tipo Pokémon). **No la uses** como referencia central de la
lámina de #fotos; usa el bocadillo de cómic del punto 6.

---

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Esto no existía en la biblia** (es uno de los 3 puntos añadidos el
24-sep-2026). Encontré entrevistas de producción muy concretas — de hecho
es el hallazgo más fuerte de toda mi parte.

### 18.1 Cómo se hizo de verdad (con nombres y citas)

- **La película usa fondos de ACUARELA, no gouache**: es la primera
  película Disney en volver a la acuarela desde los años 40 (*Dumbo* fue
  la última) — *La Sirenita*, *Aladdín*, *El Rey León* y *La Bella y la
  Bestia* se pintaron en gouache opaco ✅ (2 fuentes independientes:
  [AVClub](https://www.avclub.com/read-this-lilo-stitch-disney-watercolor-animation-1849681724),
  [Animation Obsessive](https://animationobsessive.substack.com/p/the-shape-and-color-of-lilo-and-stitch)).
- El **director de arte Ric Sluiter** propuso la acuarela; tuvieron que
  «redescubrirla» porque los pigmentos y papeles de los años 40 ya no
  existían. **7 meses de talleres de acuarela**, pintando al aire libre casi
  a diario para dominarla ✅ (AVClub).
- Sólo **un artista de fondos de 8-9, Peter Moehrle, ya sabía acuarela**;
  entrenó al resto ✅ (AVClub).
- Consultaron a **Maurice Noble**, veterano de Disney de los años 40-50 (ya
  con más de 80 años): el truco de la **sal marina de grano grueso**
  espolvoreada sobre la pintura húmeda, para la textura de las rocas de
  lava ✅ (2 fuentes: [Animation Obsessive](https://animationobsessive.substack.com/p/the-shape-and-color-of-lilo-and-stitch),
  [AVClub](https://www.avclub.com/read-this-lilo-stitch-disney-watercolor-animation-1849681724)).
- Técnica del pintor **David Wang**: mezclar el pigmento con **mucha agua
  en un platito aparte**, no en la paleta — así el pigmento grueso se posa
  en el fondo del papel y crea grano natural ✅ (Animation Obsessive).
- **Regla clave de color, cita textual de Ric Sluiter**: «*We didn't use
  any white paint, which tends to kill a color, and instead we allowed the
  white of the paper to act as a light*» — no pintaban blanco puro; dejaban
  el blanco del papel como si fuera la luz ✅ (Animation Obsessive).
- **Diseño de personaje, cita de Sluiter**: «*We chose soft, rounded
  shapes, suggestive of little loaves of home-baked bread. Elements were
  slightly inflated, or what we called chubbed up*» ✅ (Animation
  Obsessive). El animador **Byron Howard** lo resume: «*no hard edges, no
  straight lines*» — todo son curvas ✅ (misma fuente).
- La artista **Sue Nichols**: cada pose se construye con **una sola forma
  general** por personaje, «weighted to the earth» (más pesada hacia los
  pies) ✅ (Animation Obsessive).
- El diseñador de producción **Paul Felix** se centró en «mood and basic
  shapes», evitando «texturing, elaborate lighting, or an overabundance of
  stuff» — **restricción deliberada**: el detalle va en el fondo pintado,
  no en el personaje ✅ (Animation Obsessive).
- Estudio: **Walt Disney Feature Animation en Orlando (Florida)**, equipo
  de unos **350 animadores y pintores de fondos**; entre ellos, fondistas
  **William Silvers** y **Barry Kooser** ✅ (2 fuentes: [AVClub](https://www.avclub.com/read-this-lilo-stitch-disney-watercolor-animation-1849681724),
  [Wikipedia, William Silvers](https://en.wikipedia.org/wiki/William_Silvers)).
- **Storyboard muy detallado**, con luz y encuadre ya decididos ahí (como
  en cine real): cita del codirector **Dean DeBlois**, «*composition and
  lighting are vital in storytelling*», y los tableros pasaban «casi
  exactamente» a la pantalla, sin apenas discusión de layout después ✅
  ([AWN, Lilo & Stitch Revisited Part I](https://www.awn.com/animationworld/lilo-stitch-revisited-part-i)).
- Tras el **11-S**, el clímax se mantuvo casi intacto pero se retocó
  digitalmente: los rascacielos de la persecución final se cambiaron por
  **cañones de montaña** y el avión 747 por una **nave espacial** ✅
  (misma fuente AWN).
- **Influencia declarada por los directores**: *Mi vecino Totoro* de
  Miyazaki, por cómo crea relaciones familiares creíbles mezcladas con
  fantasía sin forzarla — cita de DeBlois: «*You've got these fantastic
  elements and yet you feel like you watched a story that really existed
  between a family*» ✅ ([AWN, «Lilo, Toothless and Totoro Too»](https://www.awn.com/animationworld/lilo-toothless-and-totoro-too),
  reforzado por [Wikipedia](https://en.wikipedia.org/wiki/Lilo_%26_Stitch)).
  Chris Sanders (voz y diseño de Stitch) miraba revistas de fauna salvaje —
  **nutrias marinas** en concreto — para las proporciones y gestos de
  Stitch ✅ (AWN).
- ⚠️ **Lo que no encontré**: el nombre exacto del software de tinta y color
  digital que usaron en 2002 (CAPS ya estaba descontinuándose en Disney por
  entonces). Las fuentes hablan de «coloreado digitalmente» pero no dan el
  nombre del programa.

### 18.2 Cómo replicarlo en Photoshop

1. **Nunca pintes blanco puro como luz.** Deja capas de «papel» (un color
   crema muy claro, no #FFFFFF) y usa máscaras para *revelar* el papel en
   vez de pintar blanco encima — así se ve como una acuarela real.
2. **Pinceles de acuarela con «wet edges»** (los que trae Photoshop, marca
   Kyle T. Webster, incluidos gratis con la suscripción CC) para el
   pigmento que se acumula en el borde.
3. **El truco de la sal**: usa un pincel con textura granulada fuerte, o
   una textura real de sal/roca (CC0, en [ambientCG](https://ambientcg.com/api/v2/full_json?type=Material&q=rock))
   en modo Multiplicar, sólo en zonas de roca o lava.
4. **Capa de grano de papel** por debajo de la línea, en Multiplicar u
   Overlay muy suave, para que no se vea «digital limpio».
5. **La línea del personaje**: pincel de tinta con un poco de temblor,
   nunca vectorial perfecta; siluetas **redondas e infladas** («chubbed
   up»), sin ángulos rectos.
6. **No detalles en el personaje**: el color va plano por dentro (regla de
   Paul Felix); el detalle y la textura los lleva el FONDO, no el
   personaje. Esto es clave para que la lámina no quede «genérica de IA».
7. **Grano final**: una capa de ruido muy suave + un pelín de aberración
   cromática (1-2 px) sobre todo el compuesto, para el aire de copia de
   cine de 2002 (no un render digital limpio).

### 18.3 Cómo replicarlo en Blender

1. **Contorno**: Freestyle sobre formas redondeadas, o Solidify con
   normales invertidas; línea de grosor bastante uniforme y un pelín suave
   (no afilada), para que combine con la tinta a mano.
2. **Sombreado**: shader de 2-3 escalones (Shader to RGB → ColorRamp),
   plano, sin especular elaborado — Paul Felix decía «nada de luces
   complicadas» en el personaje.
3. **El fondo lleva la textura**: usa imágenes pintadas al estilo acuarela
   como *texture* de los materiales del set (no proceduralmente
   «perfectas»); para roca de lava, un mapa de bump con ruido Voronoi
   grueso simulando el grano de sal.
4. **Rigs libres encontrados hoy** (todos con licencia CC Attribution,
   comprobada por su API), miré las miniaturas de los 4 (1920×1080 px):
   - [**Stitch (626) Rigged**](https://sketchfab.com/3d-models/stitch-626-from-lilo-and-stitch-rigged-5ae4cd66c67d42c49202f2003fe7f559),
     autor werasik2aa1, 35 464 caras, CC Attribution ✅.
   - [**Stitch (KH3) Rig**](https://sketchfab.com/3d-models/stitch-kh3-rig-d1c674e7c0424687935d1839a2a55843),
     autor guinavarro.al, 34 782 caras, CC Attribution ✅.
   - [**Pleakley**](https://sketchfab.com/3d-models/pleakley-lilo-stitch-3a4305debb52451a8ba5ccb8a174e7ef),
     autor ArbitraryCanary, 260 220 caras (muy pesado, cuidado con el punto
     9 de `reglas_del_dueno.md` — no saturar el PC), CC Attribution ✅.
   - [**Nani**](https://sketchfab.com/3d-models/nani-from-lilo-and-stitch-8ed9ce5f0f944c7182fc150cf9d4c10b),
     autor werasik2aa1, 2 758 caras (ligero), CC Attribution ✅.
   - No encontré rig libre de **Lilo** ni de **Jumba** con licencia CC
     descargable (sólo modelos sin rig o con licencia más restrictiva) ⚠️.
5. **Tutoriales libres de la técnica** (genéricos, no son de Lilo &
   Stitch, pero enseñan el método): [Blender Toon/Cel Shader Tutorial —
   TipTut](https://www.youtube.com/watch?v=rHeMWkfMpME) y [Grease Pencil
   Beginner Tutorial — Kevandram](https://www.classcentral.com/course/youtube-blender-grease-pencil-beginner-tutorial-2d-3d-toon-shaded-scene-part-2-2-133917) ✅.

### 18.4 Encuadres y composición

- Todo se decidía **en el storyboard**, con luz y encuadre ya pensados
  (cita de DeBlois en 18.1): para una lámina, eso significa **encajar
  primero en miniatura** dónde va cada cosa (personaje, texto, luz) antes
  de pintar detalle.
- Regla de contraste: **personaje limpio y plano, fondo con toda la
  textura**. Si la lámina pone a Lilo o Stitch delante de un fondo
  detallado, el personaje debe quedar gráficamente simple para no competir
  con el fondo — es justo la regla que pide `reglas_del_dueno.md` punto 1
  («un objeto real en un sitio real», con el personaje reconocible encima).

---

## Punto 24 · Obras parecidas

**Tampoco existía en la biblia.**

### 24.1 Influencias declaradas por los propios autores

- ***Mi vecino Totoro*** (Miyazaki, 1988): citado por Sanders y DeBlois
  como influencia directa en cómo dibujar una familia creíble con fantasía
  mezclada sin forzar (ver cita completa en §18.1) ✅.
- Chris Sanders puso su propia voz a Stitch con un **«croac» a lo E.T.**
  para molestar a sus animadores, según él mismo ✅ ([Wikipedia, Stitch (Lilo & Stitch)](https://en.wikipedia.org/wiki/Stitch_(Lilo_%26_Stitch))).
  El paralelo con ***E.T. el extraterrestre*** (alien escondido, adoptado
  por un niño/a solitario) es el más citado por la crítica, aunque como
  comparación de género más que cita directa del director ⚠️ (una fuente
  clara con la cita de Sanders, el paralelo con E.T. es interpretación de
  varios medios, no cita textual del director).

### 24.2 La propia franquicia se reinventa en otras culturas (dato fuerte)

La franquicia es **más popular en Asia que en Occidente desde 2006** ✅
([Disney Wiki, franquicia](https://disney.fandom.com/wiki/Lilo_%26_Stitch_(franchise))),
y eso generó **relecturas del mismo argumento en otro país**, sin Lilo:

- ***Stitch!*** (anime japonés, Madhouse, 2008-2015): Stitch cae en
  **Izayoi**, una isla ficticia inspirada en **Okinawa**; su nueva amiga es
  la niña **Yuna Kamihara**; aparecen personajes de folclore okinawense
  como la abuela **Obaa** y los espíritus del árbol **kijimuna** ✅ (2
  fuentes en japonés: [Ryukyu Shimpo](https://ryukyushimpo.jp/culture/entry-3182982.html),
  [castel.jp](https://castel.jp/p/6965), contrastadas con [Wikipedia japonés](https://ja.wikipedia.org/wiki/%E3%82%B9%E3%83%86%E3%82%A3%E3%83%83%E3%83%81!)).
- ***Stitch & Ai*** (China, 2017): Stitch llega a la China rural moderna y
  hace amistad con la niña **Wang Ai Ling** ✅ ([Disney Wiki, franquicia](https://disney.fandom.com/wiki/Lilo_%26_Stitch_(franchise))).
- ***Tono-sama to Stitch / Stitch & the Samurai*** (manga, Kodansha
  *Comic Days*, 2020; en español no publicado, en inglés por Tokyopop,
  2021, 3 tomos): Stitch amerriza en el **Japón feudal (era Sengoku)** y lo
  encuentra el señor de la guerra **Yamato** ✅ (2 fuentes: [Disney Wiki](https://disney.fandom.com/wiki/Stitch_%26_the_Samurai),
  [Anime News Network](https://www.animenewsnetwork.com/news/2020-01-13/disney-character-stitch-gets-manga-set-in-feudal-japan/.155297)).
  Su autor, **Hiroto Wada**, murió en julio de 2021, meses después de
  terminar la serie ✅ (misma fuente ANN, dato de respeto, no morboso).
  Vi la portada del tomo 1 (432×648 px): línea de manga shonen normal,
  título en pincel rojo agresivo, muy distinto al logo redondeado
  occidental (ver §5.1) ⚠️ no vi páginas interiores (Tokyopop no publica
  muestra online; lo intenté en su ficha de producto y no la tenía).
- **Por qué importa para la lámina**: son la prueba de que «Stitch +
  niña/o solitario + cultura local» es una fórmula que la propia Disney ya
  repite. Si el servidor quisiera una lámina 2 del estilo «Stitch en
  Okinawa», ya hay una obra real de referencia con su propio arte.

### 24.3 Qué otras láminas del servidor se le parecen (aviso al redactor)

Miré las 3 biblias de Disney/temática parecida que ya están hechas en el
servidor, sus **conceptos de lámina** exactos, para no repetir ideas:

- **Big Hero 6** (`08-big-hero-6-grandes-h-roes`): Disney, familia
  encontrada tras una pérdida, compañero no-humano (Baymax). Su concepto A
  usa una **tabla de dolor plastificada en un laboratorio**. Además
  **comparten universo de verdad**: el Experimento 619 de Lilo & Stitch
  aparece en *Big Hero 6* (§11.1). Nada que se pise en el objeto elegido,
  pero el redactor puede mencionar el cruce como dato curioso.
- **Doraemon** (`19-doraemon`): el paralelo más fuerte que encontré — un
  **ser no-humano de origen fantástico que un niño/a adopta y que causa
  caos doméstico**, con "gadgets"/poderes propios. **Aviso**: si la lámina
  de #fotos se apoya en «Stitch desordena la casa», se parece demasiado al
  motor de Doraemon. Mejor centrar el objeto en algo **exclusivo de
  Lilo**: que ella hace fotos (es la actividad que Doraemon no tiene).
- **Scooby-Doo** (`26-scooby-doo`): también «familia encontrada» + humor,
  concepto A con un **tablero de corcho** de pistas. No se pisa con nada
  de lo mío.
- No encontré ninguna biblia ya hecha centrada en Hawái, fotografía o
  álbumes de fotos: el ángulo del objeto (el álbum de Lilo) sigue siendo
  único en el servidor ✅ (repasé el listado de `biblias/` y sus índices).

---

## Punto 25 · El mundo, la historia y sus símbolos

**Tampoco existía en la biblia.**

### 25.1 Las reglas del mundo, en 5 líneas

1. Hay un gobierno espacial, la **Federación Galáctica Unida** («United
   Galactic Federation»), con sede en el planeta **Turo** y liderada por la
   **Gran Consejera** («Grand Councilwoman») ✅ ([Disney Wiki, Grand Councilwoman](https://disney.fandom.com/wiki/Grand_Councilwoman)).
2. El Dr. **Jumba Jookiba** crea **626 experimentos genéticos ilegales**
   numerados; Stitch es el **626**, el último y más peligroso. A los que
   sobreviven, la Federación los llama informalmente **«trogs»** o
   **«abominaciones»** ✅ ([Disney Wiki, Experiments](https://disney.fandom.com/wiki/Experiments)).
3. La Tierra está declarada **reserva de vida salvaje protegida** por ley
   de la Federación (dato ya confirmado en `biblia.md` §7.1, con subtítulo
   de la película en 00:07:23): por eso los alienígenas tienen que
   camuflarse entre los humanos.
4. El concepto hawaiano de **'ohana** («familia», en sentido extendido:
   «nadie se queda atrás ni se olvida») es la regla emocional central: es
   lo que convierte a un arma biológica en un miembro de familia ✅ (frase
   confirmada en DOS sitios independientes: la propia película y el
   cómic Dynamite 2024, ver §6.1).
5. **Kuleana** (responsabilidad) y **mālama 'āina** (cuidar la tierra) son
   la versión «adulta» de 'ohana: cuidar no sólo de la familia, sino de la
   comunidad y el entorno — así lo explica el personaje de David en el
   cómic (§6.1) ✅.

### 25.2 La historia por arcos, con momentos clave

- **Arco 1 — La película (2002)**: juicio y exilio del 626; cae en Hawái;
  Lilo lo adopta pensando que es un perro; Nani lucha por quedarse con la
  custodia de Lilo; Cobra Bubbles vigila a la familia; final: Stitch entra
  de verdad en la 'ohana Pelekai ✅ (ya narrado con minutos en `biblia.md`).
- **Arco 2 — La caza de los «primos» (2003-2006)**: *Stitch! The Movie*
  (2003, presenta a **Gantu** y al experimento 625 **Reuben**) → *Lilo &
  Stitch: The Series* (2003-2006, Lilo y Stitch cazan y **rehabilitan** los
  demás experimentos, «cambiarlos de malos a buenos y encontrar dónde
  pertenecen de verdad») → *Lilo & Stitch 2: Stitch Has a Glitch* (2005,
  un fallo de fábrica hace que Stitch vuelva a su programación
  destructiva) → *Leroy & Stitch* (2006, cierre de la serie: capturados
  los 624 experimentos, Hämsterviel libera a Gantu y crea un clon malvado,
  **Leroy**, con un ejército de copias) ✅ ([Disney Wiki, franquicia](https://disney.fandom.com/wiki/Lilo_%26_Stitch_(franchise))).
- **Arco 3 — Relecturas culturales, sin Lilo (2008-2020s)**: la franquicia
  se hace más grande en Asia que en Occidente; nacen *Stitch!* (Japón/
  Okinawa), *Stitch & Ai* (China) y el manga *Tono-sama to Stitch* (Japón
  feudal) — ver §24.2 para el detalle de cada una ✅.
- **Arco 4 — Vuelta a imagen real (2025-)**: remake de imagen real/CGI en
  2025 con Maia Kealoha de Lilo; segunda parte anunciada para 2028 ✅
  ([Disney Wiki, franquicia](https://disney.fandom.com/wiki/Lilo_%26_Stitch_(franchise))).

### 25.3 Emblemas, objetos icónicos y vocabulario que un fan reconoce

- **El número 626**: de designación de arma a nombre propio («Stitch») —
  es el símbolo central de aceptarse a uno mismo tal y como es ✅.
- **Scrump**: la muñeca de trapo que Lilo se hizo ella misma a mano, antes
  de conocer a Stitch. Su inspiración de diseño oficial: **muñeco vudú y
  el monstruo de Frankenstein** ✅ ([Disney Wiki, Scrump](https://disney.fandom.com/wiki/Scrump),
  imagen oficial medida, 1806×1080 px,
  [`Lilo & Stitch - Lilo holding Scrump.png`](https://static.wikia.nocookie.net/disney/images/9/9d/Lilo_%26_Stitch_-_Lilo_holding_Scrump.png/revision/latest?cb=20230820215155)).
  Es un símbolo perfecto para el canal de fotos: **la propia Lilo ya
  fabrica cosas caseras y las quiere**, igual que alguien que edita sus
  fotos con lo que tiene a mano.
- **El libro de El Patito Feo**: el que Stitch lee y que Lilo le explica.
  El patito llora «I'm lost!» y en la página siguiente vuelve con su
  familia; ese es el espejo de la historia de Stitch y de Lilo, los dos
  «patitos feos» que hacen las cosas mal pero quieren encajar ✅ (2
  fuentes: [ScreenRant](https://screenrant.com/lilo-and-stitch-ugly-ducking-im-lost-scene-left-out/),
  [Disney Wiki, Ugly Duckling](https://disney.fandom.com/wiki/The_Ugly_Duckling_(character))).
- **Vocabulario propio del mundo** (glosario corto, para el bot o etiquetas
  del canal): *'ohana* (familia extendida), *kuleana* (responsabilidad),
  *mālama 'āina* (cuidar la tierra), *626* (Stitch, «experimento»),
  *Federación Galáctica* / *Gran Consejera* (la ley del espacio), *primos*
  (como Stitch llama a los otros experimentos) ✅ (todas confirmadas
  arriba, con 2 fuentes cada una salvo donde se marca ⚠️).

---

## Lo mejor para la lámina (mi parte)

- El bocadillo real del cómic Dynamite (§6.1): óvalo blanco, borde grueso,
  letra Comic Neue Bold en mayúsculas — el reemplazo perfecto de «la
  burbuja blanca genérica» que el dueño rechaza.
- La frase «'Ohana means family. Family means nobody gets left behind or
  forgotten» confirmada en DOS fuentes independientes (película + cómic
  2024): es EL cuadro de diálogo de la franquicia.
- Scrump, la muñeca casera de Lilo (inspirada en vudú/Frankenstein): encaja
  perfecto con un canal de fotos hechas a mano, sin pulir.
- Técnica real de producción: acuarela + «el blanco del papel es la luz» +
  sal marina en las rocas — una receta concreta y citada para Photoshop.
- 4 rigs 3D libres (CC Attribution) de Stitch, Pleakley y Nani, listos para
  Blender, con su cara-count medido.

## No encontré (⚠️ extras, no obligatorios)

- La letra **Buka Bird** (el logo comercial): no está en Google Fonts ni
  GitHub, no la pude bajar para comprobar tildes con fontTools. Búsquedas:
  «Buka Bird font download», «Buka Bird font ñ tildes» (sin resultado
  descargable).
- **Páginas interiores** del manga *Tono-sama to Stitch*: sólo vi la
  portada; Tokyopop no publica muestra online. Búsqueda: «Tono to Stitch
  ページ», «Stitch and the Samurai manga preview pages».
- **Capturas de juego reales** (no de título) del GBA de 2002: el volcado
  de Internet Archive sólo grabó la intro; MobyGames y TCRF dieron 403.
- **Caja de diálogo** de Disney Dreamlight Valley: no encontré una captura
  clara y con licencia abierta. Búsqueda: «Disney Dreamlight Valley Stitch
  quest dialogue box UI screenshot».
- **Software exacto** de tinta y color digital usado en la película de
  2002 (¿sucesor de CAPS?): las fuentes dicen «coloreado digitalmente» sin
  nombrar el programa.
- **Rig libre de Lilo o Jumba** con licencia CC descargable en Sketchfab:
  sólo encontré de Stitch, Pleakley y Nani.
- **Un emblema o logo visual de la Federación Galáctica**: no encontré una
  imagen oficial de un escudo o insignia (sólo el nombre y el cargo de la
  Gran Consejera). Búsqueda: «Galactic Federation Lilo Stitch emblem logo
  insignia».
- **TV Tropes** de la página general de la serie (`WesternAnimation/LiloAndStitch`):
  dio 403 (Cloudflare) en el único intento; usé TV Tropes de la tira de
  cómic (esa sí cargó) y me quedé con las fuentes que sí respondieron.

## Bitácora de búsqueda (mi parte, hoy)

- **Español**: ninguna búsqueda web en español dio resultados mejores que
  el inglés para estos 6 puntos técnicos; usé español sólo para leer
  fuentes ya en español (Doblaje Wiki no aplica a mi parte).
- **Inglés** (WebSearch, ~11 búsquedas): «Lilo & Stitch Deep Canvas
  technique background art interview», «Lilo & Stitch watercolor gouache
  backgrounds art director making of», «Chris Sanders Lilo Stitch
  influences Totoro E.T. interview», «Lilo Stitch comic IDW Disney panel
  dialogue lettering», «"Lilo & Stitch" "Ohana means family" exact quote
  script», «Lilo Stitch "Ugly Duckling" book symbolism script», «Sketchfab
  Stitch Lilo model CC license downloadable», «gameuidatabase.com Kingdom
  Hearts dialogue box screenshot», «"Lilo & Stitch" Game Boy Advance 2002
  screenshot HUD dialogue box», «Disney Dreamlight Valley Stitch quest
  dialogue box UI screenshot», «Lilo Stitch Blender rig free grease pencil
  toon shader tutorial replicate 2D style», «DeBlois Sanders "Totoro"
  influence Lilo Stitch family relationships interview quote», «"Kuleana"
  meaning Hawaiian responsibility "Mālama ʻāina" translation», «"Stitch and
  the Samurai" manga preview pages Tokyopop read».
- **Japonés** (WebSearch, 2 búsquedas): «スティッチ! アニメ 沖縄 設定 世界観», «Tono to
  Stitch 殿とスティッチ 漫画 comic days ページ».
- **Red directa** (sin buscador, `curl`/Python): API de Fandom disney
  (`action=parse&prop=wikitext` en *Grand Councilwoman*, *Experiments*,
  *Scrump*, *Lilo & Stitch (franchise)*, *Stitch & the Samurai*;
  `action=query&list=search` para Ohana, Deep Canvas, Aumākua, Galactic
  Federation, Scrump, Stitch & the Samurai; `imageinfo` para 2 imágenes),
  API de Sketchfab (`v3/search`, `v3/models/<uid>`), API de
  `fonts.googleapis.com/css2` + `raw.githubusercontent.com/google/fonts`
  (8 letras), `archive.org/metadata` y descarga de capturas de
  `stitch_gba` y del cómic Dynamite (`ducktalks.com`), portada de manga
  (`tokyopop.com`).
- **Webs que dieron 403/402 hoy** (2 intentos cada una, no más): TCRF
  (`api.php` y la página directa), MobyGames, TV Tropes (página general de
  la serie), Disney Wiki normal (la página de Comic Zone, 402 — usé la API
  en su lugar para el resto).
- Herramientas: `fontTools.ttLib` (8 letras comprobadas hoy), Pillow
  (medir imágenes descargadas y montar hojas de contacto de la GBA), `Read`
  (miré 3 páginas de cómic, 2 hojas de contacto de la GBA y la portada del
  manga con mis propios ojos).