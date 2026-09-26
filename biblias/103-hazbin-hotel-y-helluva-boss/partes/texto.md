# Texto, juegos y técnica · Hazbin Hotel y Helluva Boss

Investigador de texto (puntos 5, 6, 11, 18, 24, 25 de ENCARGO.md). Serie hermana 55-hazbin-hotel
todavía no tiene carpeta en `biblias/` (se comprobó, no existe: no hay nada que leer de ella).
`datos-texto.md` casi no trajo nada (la obra es occidental, la mayoría de recolectores de anime
fallan): la investigación de este archivo es casi toda de mano, con la API de Fandom
(`hazbinhotel.fandom.com`, que cubre las dos series) y búsquedas propias.

## 5 · Tipografía (logo, globos, interfaz, letra libre comprobada con fontTools)

Ni manga ni videojuego: son series animadas de streaming, así que «letra según cada uso» se adapta
a rótulos, chyrons de TV, pantallas de móvil y subtítulos. Todas las letras libres de abajo se
descargaron de Fontsource y se comprobaron con `fontTools` (`TTFont(f).getBestCmap()`) para á/é/í/ó/ú,
ñ/Ñ, ¿ y ¡.

- **Logo/título de Hazbin Hotel**: letra de estilo *art déco* de los años 20-30 (el hotel es un
  homenaje al glamour decadente). La comunidad la identifica como **Mr Darcy** (Insigne Design),
  con retoques propios del estudio · [hilo de Hellaverse Wiki citado en búsqueda](https://hazbinhotel.fandom.com/f/p/4400000000000089255) · ⚠️ (una fuente, no confirmada por VivziePop). Mr Darcy es gratis sólo para uso personal, no sirve para nada que se publique.
- **Letra libre gemela para el logo** (déco, con tildes/ñ/¿/¡): **Cinzel Decorative** (Google
  Fonts/Fontsource, OFL) ✅ comprobada con fontTools: á/é/í/ó/ú/ñ/Ñ/¿/¡ = todo `True` · descargada de
  `cdn.jsdelivr.net/fontsource/fonts/cinzel-decorative@latest`. Alternativa más fina: **Poiret One**
  (mismo resultado, todo `True`).
- **Logo de Helluva Boss**: letra **propia y no comercial**, garabateada, con un doble trazo rojo
  sangre debajo del blanco y letras concretas con dibujo propio (la «B» de Boss, etc.); no es una
  tipografía instalable ✅ (dos fuentes independientes coinciden en que es dibujo a mano, no
  tipografía de catálogo: [pixelframe.design](https://pixelframe.design/helluva-boss-logo-font-generator/), [dafont forum «Helluva Boss - Season 2»](https://www.dafont.com/forum/read/514789/helluva-boss-season-2)).
- **Letra libre gemela para Helluva Boss** (grunge, con sangre/rasguño): **Nosifer** (Google
  Fonts, OFL, horror-splatter) ✅ fontTools: todo `True`, incluida latin-ext. Para el rótulo de
  **I.M.P.** (letras más romas, industriales): **Butcherman** ✅ fontTools: todo `True` **excepto ¿**
  (`False`) — si se necesita «¿», usar Nosifer en su lugar.
- **Globo/diálogo normal y subtítulos**: la serie no tiene globos de cómic en pantalla (es
  animación, no manga); los subtítulos oficiales de Prime Video van en un sans-serif limpio
  estándar de plataforma, no pude identificar el nombre exacto ⚠️ (sin confirmar; Prime Video no
  publica su hoja de estilos). Letra libre recomendada para textos largos/subtítulos de lámina:
  **Oswald** (Google Fonts, OFL, condensada, muy legible en pantalla) ✅ fontTools: todo `True`.
- **Grito** (letras de énfasis, gritos de Blitzo o Angel Dust): **Bangers** (Google Fonts, cómic,
  OFL) ✅ fontTools: todo `True`.
- **Pensamiento** (poco usado; la serie prefiere monólogo hablado a texto de pensamiento): si hace
  falta, **Caveat** (manuscrita, Google Fonts, OFL) ✅ fontTools: todo `True`.
- **Onomatopeya** (disparos, golpes; aparecen poco en pantalla, casi todo es sonido, no letra
  dibujada — comprobado mirando fotogramas de peleas de Helluva Boss): si se necesita una,
  **Permanent Marker** (Google Fonts, OFL, trazo de marcador) ✅ fontTools: todo `True`.
- **Cartel del mundo** (letreros de neón de Pentagram City, el cartel del hotel, el ticker de
  «666 News»): **Monoton** (Google Fonts, OFL, imita tubos de neón) ✅ fontTools: todo `True`, ideal
  para carteles de casino/club nocturno del Pride Ring. Para el ticker de noticias tipo tabloide,
  **Special Elite** (máquina de escribir, Google Fonts, OFL) ✅ fontTools: todo `True`.
- **Interfaz de juego**: no hay videojuego oficial con interfaz propia (ver punto 11); el «mapa» del
  móvil de Blitzo (imagen `Mapapp.jpg`, 2500×2500 px) usa una letra sans genérica de app, sin rasgo
  distintivo ⚠️.
- Todas las letras libres arriba se enlazan también en `texto.json` con su licencia (OFL en todos
  los casos, uso comercial libre).

## 6 · Cómo hablan y piensan en pantalla (cuadros de diálogo, cartelas, interfaces)

Es el punto más importante del encargo: nada de burbuja blanca genérica. Hazbin Hotel/Helluva Boss
no usan globos de cómic; cada personaje con un «filtro» tiene su propio marco visual, muy
reconocible por el fandom.

- **Alastor habla con ESTÁTICA DE RADIO, no con un globo**: su voz en pantalla trae textura de
  interferencia (líneas horizontales, grano, el símbolo de «señal de radio» ondulando), y su marco
  de cámara imita un dial antiguo cuando transmite ✅ (dos fuentes citadas en la guía interna del
  equipo `_Cuadros de dialogo por franquicia.md`: [Hazbin Hotel Wiki, Mario Vargas](https://hazbinhotel.fandom.com/es/wiki/Mario_Vargas), [Doblaje Wiki, Hotel Hazbin](https://doblaje.fandom.com/es/wiki/Hotel_Hazbin)). Dato de sabor: **en el doblaje latino (Chile, Caja de Ruidos) se olvidaron de quitar el filtro de radio de Alastor en el final de la T1** cuando le rompen el bastón — error real, queda grabado ✅.
- **666 News (VoxTek) usa cartela de noticiero real**: banda inferior roja con el logo de VoxTek,
  ticker de texto corriendo abajo, nombre y cargo del presentador en caja blanca, todo dentro de un
  «marco de televisor» con viñeteado, exactamente como un canal de cable de los 2000 ✅ (imagen
  `666 News main series.png`, 1920×1080, wiki oficial: [666 News](https://hazbinhotel.fandom.com/wiki/666_News); coincide con el lema «Murder! Sex! Weather!» repetido en redes oficiales) · sirve de referencia directa de «cartela del mundo».
- **VoxTek (marca del Overlord Vox/Valentino) tiene su propio logo corporativo**, año de fundación
  1952 en el lore, usado en anuncios, coches y merchandising dentro del mundo ✅ (imagen `VoxTek
  Logo.png`, 1920×1080, [wiki VoxTek](https://hazbinhotel.fandom.com/wiki/VoxTek); confirmado también en merchandising real de BoxLunch). Sirve de plantilla para cualquier «anuncio dentro del mundo» de la lámina.
- **El móvil de Blitzo (Helluva Boss) usa una app de mapa** con las siete anillas de Hell marcadas,
  interfaz tipo GPS genérico (fondo oscuro, pines de colores) ✅ (imagen `Mapapp.jpg`, 2500×2500,
  [wiki Rings of Hell](https://hazbinhotel.fandom.com/wiki/Rings_of_Hell)) — es la referencia más concreta de «interfaz de móvil» del mundo.
- **No hay manga oficial** de Hazbin Hotel/Helluva Boss (nació como piloto de YouTube y serie
  animada, no como cómic seriado); sólo hay **merchandising con paneles tipo cómic** (variant covers,
  pósters) hechos por artistas del estudio para eventos — no encontré un cómic narrativo licenciado
  con globos propios ⚠️ (búsqueda «Hazbin Hotel comic official issue» sin resultado fiable).
- **Pensamientos**: la serie casi no usa cajas de texto de pensamiento; los personajes cantan o
  hablan en voz alta lo que piensan (recurso de musical) — nada que fotografiar como «cuadro de
  pensamiento» ⚠️ propio de la obra, es una decisión de guion, no de arte.
- **Subtítulos oficiales**: sans blanco con borde negro fino, estándar de Prime Video, centrados
  abajo; no cambian de tipografía por personaje (ni siquiera para Alastor) ⚠️ (visto en clips
  oficiales de Prime Video en Dailymotion, sin acceso a archivo de subtítulos original para medir el
  tipo exacto).

## 11 · Videojuegos de la franquicia

- **No existe ningún videojuego oficial** de Hazbin Hotel ni de Helluva Boss a fecha de hoy
  (26-sep-2026) ✅ — comprobado en TCRF (`tcrf.net`, búsqueda «Hazbin» y «Helluva»: cero páginas) y
  en búsqueda directa de anuncios de publisher; lo único con ese nombre en fandoms son wikis de
  «ideas de fans» (`gameideas.fandom.com`, `audreyworks.fandom.com`) con fechas de 2026-2029 que
  se leen como ficción de fans, no como anuncios reales (el propio texto lo admite: «homebrew»,
  «Game Ideas Wiki») — **no lo cuento como real**, aviso explícito para no confundirlo.
- **Lo único oficial jugable es un juego de mesa**: *Immediate Murder Professionals: A Helluva Boss
  Official Game* (Creatist Games, con licencia de VivziePop/Spindlehorse) ✅ (dos fuentes:
  [Kickstarter](https://www.kickstarter.com/projects/creatistgames/immediate-murder-professionals-a-helluva-boss-official-game-0), [Gamefound](https://gamefound.com/en/projects/creatist-games/helluvabossgame), reseñado también en [thelatenightplayers.com](https://www.thelatenightplayers.com/news/helluva-boss-board-game-launches-on-kickstarter)). 4 personajes jugables (Blitzo, Millie, Moxxie, Loona), rueda de juego, 56 cartas base, standees de cartón; edición «Grimoire» con
  caja con forma del grimorio de Stolas y peones de cristal acrílico · recaudó más de $204,701 en
  Kickstarter ✅.
- No hay interfaz de videojuego que mirar (ni menús, ni cajas de diálogo de juego): el punto no
  aplica más allá del juego de mesa de arriba. Si el redactor necesita una interfaz de «juego»
  para la lámina, la referencia más cercana dentro del mundo ficticio es el móvil de Blitzo (ver
  punto 6) o las máquinas tragamonedas de los casinos del Pride Ring (visibles en fondos de la
  serie, sin interfaz jugable real).

## 18 · Estilo de dibujo y técnica, y cómo replicarlo (rigs y tramas: ver puntos 3 y 19)

Software y equipo confirmados en entrevistas; el resto es guía propia de cómo llegar a ese look
en Photoshop y Blender, con marcas y licencias reales.

**Cómo se hizo (con fuentes)**
- **Toon Boom Harmony** es el programa central de animación 2D, con tabletas **Wacom Cintiq**, y
  Adobe (Photoshop, Premiere) en postproducción ✅ (dos fuentes: [VFX Voice, «Checking Into Hazbin
  Hotel to Check Out the Animation»](https://vfxvoice.com/checking-into-hazbin-hotel-to-check-out-the-animation/), resumen coincidente de Animation Magazine sobre el pipeline Spindlehorse/Bento Box/A24).
- **Casi todo es 2D**: los efectos de fuego, humo y explosiones son dibujados a mano, no 3D; el 3D
  se usa muy poco ✅ (VFX Voice).
- **Línea y proporción**: nada de hoja de modelo rígida — la directora de animación **Skye
  Henwood** lo resume: «as long as it looks cool or appealing, that's it», así que los personajes
  se estiran y exageran cuando ayuda a la toma ✅ (VFX Voice, cita textual).
- **Color, el reto real**: el director de arte **Sam Miller** dijo que lo más difícil es «a lot of
  red characters on numerous red backgrounds» — Hell vive en rojo/negro saturado, y el Cielo usa
  paleta pastel para que el contraste se note de inmediato al cambiar de escenario ✅ (VFX Voice,
  cita textual de Vivienne Medrano sobre Sam Miller).
- **Regla de diseño fija**: **Vox nunca se dibuja de perfil**, porque su cabeza es una pantalla de
  TV y de perfil se rompe el gag visual ⚠️ (una fuente, VFX Voice, pero es coherente con lo que se
  ve en el material de la wiki).
- **Influencias declaradas**: Bruce Timm (el diseño de las Overlord femeninas viene de ahí), Tim
  Burton (proporciones espigadas, «rayas» decorativas — «a Tim Burtonism», cita de Medrano), el
  Renacimiento Disney (estructura de musical), Looney Tunes (comedia física) y, sobre todo,
  **Jhonen Vasquez / Invader Zim**, que Medrano recomienda activamente a sus fans ✅ (dos fuentes:
  [VFX Voice](https://vfxvoice.com/checking-into-hazbin-hotel-to-check-out-the-animation/), búsqueda cruzada con TV Tropes/SVA sobre las influencias de Medrano).

**Cómo reproducirlo en Photoshop**
1. Boceto en una capa al 30-40% de opacidad; encima, capa de **línea limpia** con un pincel de
   punta dura sin textura (100% opacidad, sin difuminado): así sale el contorno grueso y sin
   grano que da Toon Boom al exportar vectorial. Pinceles libres que sirven: los paquetes de
   *ink/line art* de [BrushWarriors](https://brushwarriors.com/lineart-brushes-photoshop/) o
   [123FreeBrushes](https://www.123freebrushes.com/line-art/) (gratis, uso personal).
2. Color base en una capa debajo de la línea, un tono por zona (piel, ropa, pelo) sin degradado.
3. Sombra en una capa **Multiplicar** encima del color, recortada (clipping mask) al color base,
   rellena con el lazo poligonal (bordes duros, no aerógrafo) — así se consigue el sombreado
   **plano de dos valores** que se ve en la serie, nunca un degradado suave.
4. Brillos/neón (fuego de Alastor, magia, letreros) en una capa **Trama** o **Más claro** en
   blanco o en el color del neón, con desenfoque gaussiano sólo en esa capa para el «glow».
5. Grano y viñeta al final, en una capa de ajuste (Ruido + Viñeta suave) para imitar la
   compresión y el grano de streaming que se ve en los fotogramas.
6. Paleta: swatches fijos rojo/negro para escenas de Hell, pastel para Heaven — cambiar de paleta
   entera, no sólo aclarar/oscurecer el mismo rojo.

**Cómo reproducirlo en Blender** (para el objeto u escena 3D de la lámina, no para el personaje
completo — eso es el punto 3/19 de imagen):
1. Contorno: **Freestyle** activado, grosor 3-5 px, color negro puro, ángulo de arista (crease
   angle) bajo para que también marque las costuras de ropa y no sólo la silueta exterior.
   Alternativa más ligera en Eevee: modificador **Solidify** con normales invertidas y material
   negro sin sombra («casco invertido»), más rápido de previsualizar.
2. Shader plano: nodo **Diffuse BSDF → Shader to RGB → ColorRamp** con 2-3 paradas SIN
   interpolación (Constante) para que la sombra caiga en un solo salto duro, igual que el
   sombreado plano de la serie, en vez del degradado suave por defecto.
3. Luz: una luz de área como clave, y una luz de relleno de color de neón contrastante (cian o
   verde) para las escenas de casino/club nocturno del Pride Ring — sin iluminación global
   difusa, que aplana el efecto de dos-tonos.
4. Render en **Eevee** (rápido, no exige la GPU como Cycles — cumple la regla del dueño de no
   saturar el PC, `servidor/reglas_del_dueno.md`, punto 9).
5. Textura encima: una textura de grano de papel o película en modo de fusión **Superponer** con
   opacidad baja, para el filtro sucio típico de la serie. CC0 en [ambientCG](https://ambientcg.com/api/v2/full_json?type=Material&q=paper) (buscar «Paper» o «Grunge»).

## 24 · Obras parecidas y temas relacionados

- **Invader Zim** (Jhonen Vasquez, Nickelodeon 2001): la propia Medrano lo recomienda a sus fans y
  hay un cameo directo (Tallest Rojo y Tallest Púrpura aparecen en la canción de Charlie) ✅ (dos
  fuentes: [Dexerto, «5 shows to watch if you like Hazbin Hotel»](https://www.dexerto.com/tv-movies/shows-to-watch-if-you-like-hazbin-hotel-2533898/), [TV Tropes ReferencedBy/InvaderZim](https://tvtropes.org/pmwiki/pmwiki.php/ReferencedBy/InvaderZim)). Comparte la estética espigada, ojos grandes y humor gótico-pop.
- **Murder Drones** (Glitch Productions): nació también como animación independiente en YouTube,
  comparte actores de doblaje con Hazbin Hotel (Michael Kovach, Elsie Lovelock) y tono de
  comedia-horror distópica ✅ (dos fuentes: Dexerto, búsqueda cruzada confirmando el reparto
  compartido).
- **Panty & Stocking with Garterbelt** (Gainax, 2010): comparación habitual de la crítica por el
  tono vulgar + ángeles/demonios en tensión, aunque los críticos dicen que P&S lo hace «con más
  propósito» ✅ ([ScreenRant, «Panty and Stocking is Far More Vulgar than Hazbin Hotel»](https://screenrant.com/panty-and-stocking-beat-hazbin-hotel-viral-anime/)) — útil para explicar el género «comedia-demoníaca-musical-vulgar» a quien no conoce ninguna de las dos.
- **The Good Place** (serie live-action): mismo tema de Cielo/Infierno/redención con comedia, citada
  como recomendación directa para quien viene de Hazbin Hotel ✅ (Dexerto).
- **The Owl House**: comparada por el mundo de fantasía demoníaca y el foco en personajes queer ✅
  (Dexerto).
- **Influencias de estilo** (ver punto 18): Bruce Timm/DC Animated Universe, Tim Burton, Disney
  Renaissance, Looney Tunes — mismas fuentes que el punto 18.
- **Ya hechas en el servidor, no repetir la idea**: **Steven Universe** (104, sin canal aún,
  propone #arte/#reto-de-la-semana/#demos-canto — tono opuesto, familiar y pastel, sirve de
  contraste, no de gemelo), **Arcane** (17, #proyectos y #arte — animación madura pero pintada,
  no plana), **Rick and Morty** (13, #noticias-series — comedia adulta animada, pero ciencia
  ficción, no musical-demoníaco). Ninguna comparte el ángulo «musical + radio demoníaca» que pide
  este encargo, así que el concepto de lámina no choca con ellas.

## 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo en cinco líneas** (Hazbin Hotel Wiki, `Rings of Hell`, `Sinners`, `Overlords`,
`Extermination` — todas ✅ con wikitext oficial citado arriba):
1. El Infierno tiene **siete Anillos apilados**, uno por cada Pecado Capital (Pride, Greed, Wrath,
   Lust, Sloth, Gluttony, Envy); los Sinners (humanos condenados) no pueden salir de su Anillo,
   sólo los demonios «Hellborn» y la familia real se mueven libremente entre ellos.
2. Los **Sinners** son almas humanas condenadas; están por debajo de los Hellborn (imps, hellhounds,
   súcubos) en la jerarquía, pese a ser el grueso de la población.
3. Los **Overlords** (Alastor, los Vees, Carmilla Carmine, Zestial, Rosie, Zeezi…) son la clase de
   poder que controla territorio, medios y negocios de la Pentagram City.
4. Los **Seven Deadly Sins** (Lucifer, Satán, Beelzebub, Mammón, Asmodeo, Leviatán, Belfegor) son la
   realeza que gobierna por encima de los Overlords.
5. Una vez al año (antes bianual) llega la **Extermination**: exorcistas armados con **armas
   angelicales** bajan a matar Sinners para controlar la superpoblación — el conflicto que mueve
   toda la trama del hotel.

**Historia por arcos** (Hazbin Hotel Wiki, página de la serie ✅):
- **Piloto** («That's Entertainment», 28-oct-2019, YouTube de Vivienne): presenta el Happy Hotel,
  a Charlie y el concepto de redención, gratis en el canal de la autora.
- **Recogida por A24** (7-ago-2020) y estreno oficial en **Prime Video el 19-ene-2024**: serie
  principal, 8 episodios en temporada 1 — arco de fundación del hotel, llegada de Angel Dust,
  Sir Pentious y el ataque de la Extermination al final de temporada.
- **Temporada 2** (estreno 29-oct-2025, 8 episodios): arco de guerra de Vox contra el hotel
  («Vox's War Path»), consolidación de las Vees como antagonistas centrales.
- **Temporadas 3, 4 y 5**: confirmadas y en producción a la fecha de este informe (26-sep-2026) ✅
  (wiki + cobertura de prensa especializada).
- **Helluva Boss** corre en paralelo, mismo universo, desde 2019/2020 (creada también por Medrano
  con Brandon Rogers); se centra en I.M.P. (Immediate Murder Professionals), la empresa de
  sicarios de Blitzo que trabaja **desde el Infierno hacia el mundo humano** — perspectiva opuesta
  a Hazbin Hotel, que se queda dentro del Infierno ✅ (wikitext de Helluva Boss).

**Emblemas, logos y objetos icónicos**:
- **VoxTek** — logo corporativo de Vox/Valentino, fundada (en el lore) en 1952, dueña de 666 News,
  electrónica, vehículos y comida dentro de Pentagram City ✅ (wiki + merchandising real de
  BoxLunch citando el año).
- **666 News** — el noticiero de Pentagram City, lema «Murder! Sex! Weather!», cartela roja de
  VoxTek con ticker (ver punto 6) ✅.
- **I.M.P. (Immediate Murder Professionals)** — logo/marca de la empresa de sicarios de Blitzo en
  Helluva Boss, con su propio jingle y vídeo de entrenamiento en la wiki ✅ (páginas «I.M.P Jingle»,
  «IMP Training Video»).
- **Armas angelicales** — objeto icónico del conflicto Cielo/Infierno: mercado negro dominado por
  Carmine Industries ✅.
- El **Pentagrama** en sí (silueta de Pentagram City vista desde arriba) es el símbolo geográfico
  central de toda la franquicia — aparece en el propio nombre de la ciudad ✅.

## Lo mejor para la lámina

- El **filtro de radio de Alastor** (estática + dial) como «cuadro de diálogo» propio: mucho más
  fiel que cualquier globo.
- La **cartela de 666 News** (banda roja VoxTek + ticker) y el **logo VoxTek** como plantilla de
  «marca/aviso dentro del mundo» para los textos del canal.
- **Cinzel Decorative** para títulos/logo (deco, libre, con ñ/¿/¡) y **Nosifer** para lo tipo
  Helluva Boss (sangre/grunge, libre).
- El **sombreado plano de dos valores** (sombra dura, sin degradado) + rojo/negro saturado en Hell
  vs. pastel en Heaven: la clave de color para cualquier render, en Photoshop o Blender
  (ColorRamp constante, ver punto 18).
- El **Pentagrama de Pentagram City**: símbolo geográfico que cualquier fan reconoce al instante,
  útil como sello o marca de agua del canal.

## No encontré

- Confirmación directa de VivziePop sobre el nombre exacto del tipo del logo de Hazbin Hotel
  (búsqueda «vivziepop twitter font hazbin hotel logo», en inglés: sólo fan art, sin tuit fuente).
- El nombre del tipo de letra de subtítulos/créditos oficiales de Prime Video (no hay archivo de
  subtítulos original descargable sin sesión).
- Un cómic o manga oficial con cuadros de diálogo propios de la franquicia (búsqueda «Hazbin Hotel
  official comic issue», en inglés: nada más que merchandising suelto).
- Videojuego oficial (confirmado que no existe, ver punto 11; búsquedas «Hazbin Hotel video game
  official 2026», «Helluva Boss I.M.P. app», en inglés, en tcrf.net directamente).
- No pude leer el artículo de Animation Magazine (403 al fetch directo y también por Wayback,
  conexión cortada) para cruzar una segunda fuente de las citas de Sam Miller/Skye Henwood: quedan
  con una sola fuente (VFX Voice) ⚠️, aunque VFX Voice es medio especializado y cita nombre y cargo
  exactos, no anónimo.
- Fuentes originales **en japonés** o **coreano/chino** no aplican: Hazbin Hotel y Helluva Boss son
  producciones estadounidenses (Spindlehorse/A24/Bento Box/Amazon), sin staff ni prensa en esos
  idiomas que buscar — se dejó constancia en vez de forzar una búsqueda vacía.
- Entrevista directa de VivziePop sobre software de Blender/3D (no usan Blender en producción real,
  es 2D; la guía de Blender del punto 18 es propuesta propia para la lámina, no técnica original
  del estudio — lo digo explícito para no confundir «cómo lo hicieron» con «cómo replicarlo»).

## Bitácora

- Fandom API (`hazbinhotel.fandom.com/api.php`, inglés): `allpages`, `search` y `parse&prop=wikitext`
  para Rings of Hell, Overlords, Extermination, Seven Deadly Sins, Pentagram City, Hazbin Hotel
  (series), Hazbin Hotel (location), 666 News, VoxTek — todas abiertas y leídas.
- `tcrf.net` (inglés): búsqueda de texto completo «Hazbin» y «Helluva» → sin resultados, confirma
  que no hay contenido descartado de un juego que no existe.
- WebSearch (inglés): «Hazbin Hotel logo font typeface identify», «Helluva Boss logo font typeface
  identify», «"Mr Darcy" font dafont free download license», «Hazbin Hotel font free alternative
  Google Fonts dafont art deco», «TCRF Hazbin Hotel OR Helluva Boss», «Hazbin Hotel official video
  game mobile app 2024 2025», «Helluva Boss video game I.M.P. app», «"Hazbin Hotel" game announced
  2026 publisher official», «vivziepop twitter font hazbin hotel logo», «Hazbin Hotel end credits
  font typeface style title cards».
- Fontsource (`api.fontsource.org/v1/fonts`, descarga directa de `cdn.jsdelivr.net`): Cinzel
  Decorative, Poiret One, Nosifer, Butcherman, Creepster, Bangers, Monoton, Special Elite, Oswald,
  Permanent Marker, Caveat — comprobadas todas con `fontTools` (`getBestCmap`) para
  á/é/í/ó/ú/ñ/Ñ/¿/¡.
- WebFetch: `pixelframe.design` (Helluva Boss font), `audreyworks.fandom.com` (Five Nights at
  Hazbin Hotel, confirmado fan-made), `thelatenightplayers.com` (juego de mesa I.M.P.),
  `gamefound.com` y Kickstarter (bloqueados por 403, se usó la reseña de thelatenightplayers.com en
  su lugar, con Gamefound/Kickstarter como enlaces directos del producto), `vfxvoice.com` (técnica
  de animación, punto 18), `dexerto.com` (obras parecidas, punto 24).
- WebSearch (inglés) puntos 18/24/25: «Hazbin Hotel Helluva Boss animation software Toon Boom
  pipeline interview Vivienne Medrano», «Hazbin Hotel art style line art shading cel shading
  outline color interview», «Vivienne Medrano influences Cats Don't Dance Bruce Timm Tim Burton
  animation style hazbin», «Blender Freestyle toon shader flat cel shading tutorial free node
  setup 2D cartoon outline», «free Photoshop ink brush clean line art cartoon vector brush
  download», «Hazbin Hotel compared Panty and Stocking OR Invader Zim OR Murder Drones similar
  style review».
- Fandom API, wikitext adicional para el punto 25: `Sinners`, `Angelic Weapon`, `Helluva Boss`
  (serie), búsqueda de `I.M.P` (jingle y vídeo de entrenamiento).
- Comparación con biblias ya hechas del servidor (punto 24): se miró `canal:` de
  `biblias/104-steven-universe/biblia.md`, `biblias/17-arcane/biblia.md` y
  `biblias/13-rick-and-morty/biblia.md` (sólo la cabecera, no se leyeron enteras: no son mi rol).
