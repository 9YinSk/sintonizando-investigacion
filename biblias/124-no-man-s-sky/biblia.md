# No Man's Sky — biblia (encargo 124)

Obra: **No Man's Sky**, videojuego de **Hello Games** (Guildford, Reino Unido). Salió el 12-ago-2016 en PS4 y PC; después Xbox, PS5 (con soporte de PS5 Pro) y realidad virtual (*Beyond*, 2019). Switch ⚠️: no aparece en las partes. Desde entonces lleva más de 18 actualizaciones grandes gratis.
Enfoque del encargo: **planetas de colores y portadas de ciencia ficción retro**. Personaje de partida: **el Viajero** (*the Traveller*).
Escrita por el redactor el 25-sep-2026 con las partes de imagen, vídeo, voz y texto (`partes/`). Lo que no está en las partes lleva ⚠️ o ❌ y se dice.
Continuada el 26-sep-2026 (modo «seguir»): la primera redacción se cortó tras §0. Ahora van los 25 puntos, las hojas, los conceptos, la tabla y la bitácora. El redactor además leyó el texto de 10 capturas de diálogo de la wiki y midió sus cajas con `estilo.py`.

Leyenda: ✅ = dos fuentes, o visto o medido · ⚠️ = una fuente, deducido o a medias · ❌ = no hecho.

## Segunda pasada · qué cambió

- **Antes**: sólo índice y §0. **Ahora**: §1-25, hojas, correcciones, 3 conceptos, tabla y bitácora.
- **Añadido por el redactor**: frases reales leídas en 10 capturas de diálogo (Polo, Nada, Artemis, Apollo, -null-, el Atlas, un Viajero NPC). Y los colores medidos de las cajas: la caja es translúcida y cambia de tono con el fondo (§6).
- **Corregido** (detalle en «Correcciones del redactor»): la narración del Viajero es en primera persona, no en tercera. Sí hay onomatopeya escrita: la estática «kzzkt». Los Autophage llegan con *Echoes* (2023), no con *Desolation*. En `referencias.json`, Polo es Gek, no Korvax.
- **⚠️**: había 1 en la biblia. Los que quedan se ven en la tabla, cada uno con su porqué.

## Índice

- Segunda pasada · qué cambió
- 0 · En una pantalla
- 1 · Arte oficial
- 2 · Fotogramas de escenas icónicas
- 3 · Fan art y 3D con licencia
- 4 · Sitios, luz, paleta y texturas reales
- 5 · Tipografía
- 6 · Cómo hablan y piensan en pantalla
- 7 · Personajes y popularidad
- 8 · Doblaje: no hay latino (y lo que sí hay)
- 9 · Música y sonido
- 10 · Vídeos y tendencias
- 11 · El videojuego: interfaz y menús
- 12 · Lo que ama el fandom y qué NO hacer
- 13 · Personajes a fondo
- 14 · Poses analizadas
- 15 · Vestuario con hex medidos
- 16 · Paisajes y fondos de pantalla
- 17 · Guía para IA de imagen y de texto
- 18 · Estilo y técnica, y cómo replicarlo
- 19 · Texturas 2D
- 20 · Gustos y detalles
- 21 · Por qué la aman
- 22 · Fan dubs y comunidad hispana
- 23 · Colaboraciones, figuras y cosplay
- 24 · Obras parecidas y láminas vecinas
- 25 · El mundo, la historia y sus símbolos
- Hojas de contacto
- Correcciones del redactor
- 3 conceptos de lámina
- Cumplimiento del encargo
- Bitácora de búsqueda

## 0 · En una pantalla

- **Qué es**: un universo que se genera solo con matemáticas: **18 trillones de planetas** (18×10¹⁸), cada uno distinto. El jugador es **el Viajero**, alguien dentro de un **Exotraje** (*Exosuit*) al que nunca se le ve la cara. Mina, sobrevive al frío, al calor o a la radiación, arregla su nave y viaja hacia el centro de la galaxia. Por encima de todo está **el Atlas**, la entidad que para los alienígenas creó el universo (y que resulta ser el ordenador que lo simula).
- **El tono**: asombro y soledad a la vez. «La belleza que te deja sin aire y la soledad inquietante del espacio profundo» ([TouchArcade](https://toucharcade.com/2024/07/29/no-mans-sky-2024-review/)). Aquí **sí van colores vivos** (regla 6 del dueño: el tono de la obra manda), pero no alegres de dibujo infantil: son colores de **portada de libro de ciencia ficción de los 70**, con niebla y contraluz.
- **La regla de oro del estilo**: **nada de negro puro**. El director de arte, Grant Duncan, quería evitar «los campos de estrellas negros y las naves grises» ([GamesBeat](https://gamesbeat.com/unraveling-the-mysteries-of-no-mans-skys-18-quintillion-planets/)). Todas las sombras medidas llevan tinte: verde, vino o azul.
- **La paleta**, medida con `estilo.py` en fotogramas y capturas: planeta del anuncio al atardecer `#630F31`, sabana tóxica `#CCBC54` y cielo `#C1E8B3`, hierba roja de *Echoes* `#A00B0A` con cielo `#609FDB`, fondo del cartel *Cosmos* `#49C0A9` y `#3B7872` con planeta `#85514C`, Exotraje por defecto `#0A2334` con luces `#02DBF0` y óxido `#D17359`, capa de Nada `#24264C` con forro `#5C2C31`, caja de diálogo `#2E2B29`.
- **El más querido**: **no hay encuesta oficial** (buscada). No es un juego de reparto fijo: lo que la gente ama es **el propio juego y su remontada**. Entre las especies, los **Gek** son «los adorables» del hilo con más votos sobre el tema (131 votos) ⚠️ sin ganador claro. Los personajes con nombre más recordados: **Nada y Polo** (la pareja de la Anomalía Espacial) y **Artemis** (la historia que emociona).
- **El cuadro de diálogo propio**: **nunca un globo**. Es una **barra oscura translúcida** (`#2E2B29` sobre fondo cálido; toma el tono de lo que hay detrás, ver §6) con un **filete blanco punteado** arriba y abajo, **texto blanco sin serifa** y, a la derecha, **opciones numeradas** `[1] [2] [3] [4]`; las bloqueadas, en gris con la condición entre paréntesis. El Viajero «habla» en **primera persona, narrando** («*Nada's paranoia is infectious. I find myself…*»). Los Viajeros NPC usan una **caja azul** (`#153457`) con su nombre en una pestaña arriba.
- **Voz**: **no hay doblaje latino** (ni texto en español latino). Steam sólo trae **español de España**, con audio sólo para la voz del traje. Los alienígenas no tienen actores: su voz la sintetiza un programa, **VocAlien**, de Paul Weir.
- **Canal propuesto** (el encargo no trae canal): A **#a-que-juegas** «El portal de la sabana» (recomendada), B **#proyectos** «El Nexo de la Anomalía», C **#eventos** «El parche de la Expedición». Las biblias son generales: el canal es sólo una idea.


## 1 · Arte oficial

**La idea que manda.** Hello Games quería que el juego pareciera «una portada de libro de ciencia ficción cobrando vida» ([blog oficial](https://www.nomanssky.com/2016/04/art-of-no-mans-sky/), repetido por Sean Murray a IGN y citado por [TweakTown](https://www.tweaktown.com/news/52987/mans-sky-art-reimagined-sci-fi-book-covers/index.html)) ✅.

- **Quién lo dibuja.** Grant Duncan, cofundador y director de arte. Al principio era el único artista del estudio ([wiki](https://nomanssky.fandom.com/wiki/Grant_Duncan)) ✅.
- **Sus influencias.** Chris Foss (portadas de los libros de Asimov), Ralph McQuarrie (*Star Wars*), John Harris, Mœbius y las películas de Ray Harryhausen ([GamesBeat](https://gamesbeat.com/unraveling-the-mysteries-of-no-mans-skys-18-quintillion-planets/) y [Wikipedia](https://en.wikipedia.org/wiki/Development_of_No_Man%27s_Sky), misma cita) ✅.
- **Su frase sobre Foss**: «he created this kind of art when everyone else was creating black starfields, grey dull monolithic spacecrafts» ✅. Por eso aquí no hay negro puro ni naves grises.
- **Su referencia de color**: fotos de la NASA, como los «Pilares de la Creación» del Hubble, en vez de un fondo de estrellas negro ✅.
- **Artbook oficial**: *The Art of No Man's Sky*, Dark Horse Books, 2016, tapa dura, 48 páginas. Venía en la Limited Edition de PS4 con el cómic *Adventures in No Man's Sky* ([ficha](https://www.thevideogamelibrary.org/book/the-art-of-no-man-s-sky)) ✅. Está **escaneado entero** en [Internet Archive](https://archive.org/details/art-of-no-mans-sky-book-scan) (PDF y EPUB). Es la mejor fuente de arte conceptual pintado a mano: naves, criaturas y planetas antes de pasar al programa ✅.
- **Arte conceptual del blog**: nave y planeta con dos soles, 1280×720 ([imagen](https://www.nomanssky.com/media/me2doobw/art-nms-1.png)) ⚠️: sólo se pudo sacar esta imagen del artículo.
- **El cartel más reciente**: el de *Cosmos* (10.º aniversario, ago-2026), en el [minuto 1:52 del tráiler](https://archive.org/details/youtube--sK7EGiJSDk?t=112). El Viajero lleva traje blanco y rojo con visera dorada, entre dos compañeros alienígenas. Detrás, un planeta rojo enorme y el rombo rojo del Atlas; el fondo es verde azulado. Visto en la hoja 3, n.º 10 ✅.
- **Fondo oficial del estudio**: planeta cian de Kuldar Leement, 2280×1280, con origen en hellogames.org ([Wallhaven](https://w.wallhaven.cc/full/2k/wallhaven-2kzwg9.jpg)) ✅.
- **Arte promocional en alta**: 8250×4672, rosa y turquesa, con origen en no-mans-sky.com. Lo subió GameVogue (♥ 72) ([imagen](https://w.wallhaven.cc/full/4x/wallhaven-4xvdxo.jpg)) ⚠️: el origen sólo lo dice Wallhaven.
- **Portadas retro de un fan**, ichtyander, que imitan libros de bolsillo de los 70. Grant Duncan las compartió el 12-jul-2016: «Wow, this is one of the coolest NMS fan-made things I've seen yet!» ([Push Square](https://www.pushsquare.com/news/2016/07/these_alternate_no_mans_sky_ps4_covers_look_just_like_classic_sci-fi_books)) ⚠️: una fuente, pero es la cita del director de arte.
- **Poses vivas del arte de la wiki** (con su número de hoja):
  - hoja 1, n.º 1: el Exotraje de pie junto a su nave, sobre un aro de luz cian (3840×2160);
  - hoja 1, n.º 29: el Viajero en el pasillo de un carguero;
  - hoja 2, n.º 59: dos Viajeros hablando, uno con una tablet;
  - hoja 1, n.º 31: una multiherramienta dañada;
  - hoja 2, n.º 69: una nave en vuelo rasante sobre el agua;
  - hoja 1, n.º 15: una corbeta aterrizando.
- **No encontré** quién firma cada pieza de *key art*, más allá de Duncan como responsable ⚠️. «Malcolm Smith» fue una pista falsa: es un ilustrador *pulp* de los años 30-60 sin relación con el estudio.

## 2 · Fotogramas de escenas icónicas

Es un videojuego: no hay capítulos. Aquí el «capítulo» es el **tráiler** o la **actualización**. Todos los fotogramas los sacó el investigador de vídeo con `fotogramas.py`. Están en la hoja 3 ✅.

| Hoja 3 | Tráiler | Minuto | Qué se ve |
|---|---|---|---|
| — | Anuncio (VGX, 2014) | [0:24](https://archive.org/details/youtube-aCgWabJssVI?t=24) | Arrecife de coral con peces |
| 1 | Anuncio 2014 | [0:40](https://archive.org/details/youtube-aCgWabJssVI?t=40) | Playa de hierba roja, bruma marina verde, letrero «NEW PIDU» |
| 2 | Anuncio 2014 | [1:40](https://archive.org/details/youtube-aCgWabJssVI?t=100) | Logo «NO MAN'S SKY» sobre un planeta rojo a contraluz |
| 3 | E3 2015 (JeuxVideo.com) | [3:40](https://www.dailymotion.com/video/x89lilx?t=220) | Sabana tóxica amarilla vista desde la cabina |
| 4 | E3 2015 | [4:00](https://www.dailymotion.com/video/x89lilx?t=240) | Bosque de árboles rojos sobre hierba amarilla, a pie |
| 5 | *Echoes* (2023, Vidaextra) | [0:00](https://www.dailymotion.com/video/x8nggcs?t=0) | Hierba roja, setas gigantes y los Autophage |
| 6 | *Echoes* | [0:42](https://www.dailymotion.com/video/x8nggcs?t=42) | Combate espacial con láseres rojos entre planetas azul, verde y violeta. video.md lo da de 0:36 a 1:12; la hoja pone 0:06 ⚠️ |
| 7 | *Prisms* | [0:16](https://www.dailymotion.com/video/x89nujz?t=16) | Cueva con luz de colores; rótulo «Volumetric Lighting» |
| 8 | *Prisms* | [0:24](https://www.dailymotion.com/video/x89nujz?t=24) | El Viajero de espaldas en una ladera verde, con compañeros |
| — | 10.º aniversario | [0:24](https://archive.org/details/youtube--sK7EGiJSDk?t=24) | Repaso de «Year 1» a «Year 10» con los nombres de cada actualización |
| 9 | 10.º aniversario | [1:20](https://archive.org/details/youtube--sK7EGiJSDk?t=80) | En primera persona, apuntando a una criatura mecánica entre niebla verde |
| 10 | 10.º aniversario | [1:52](https://archive.org/details/youtube--sK7EGiJSDk?t=112) | Cartel «NO MAN'S SKY COSMOS» |

- YouTube pedía «confirma que no eres un bot». Por eso se usaron copias del vídeo oficial en Internet Archive y Dailymotion ✅.
- **Las escenas de historia** (Artemis, el Atlas muriendo) no tienen minuto de vídeo. Sólo hay capturas de la wiki (§21) ⚠️.

## 3 · Fan art y 3D con licencia

**Modelos 3D** (comprobados con la API de Sketchfab, todos descargables; los ♥ son del recolector) ✅:

| Modelo | Autor | Licencia | ♥ | Para qué |
|---|---|---|---|---|
| [No Man's Sky Portal](https://sketchfab.com/3d-models/none-c30efda62567455d9f0644f55abc06f7) | locopixel | CC BY-NC | 168 | El portal de glifos (concepto A) |
| [Radiant Pillar BC1](https://sketchfab.com/3d-models/none-97e9276d86454c92af42c50aefa8d405) | locopixel | CC BY-NC | 240 | Nave (la más votada) |
| [Golden Vector](https://sketchfab.com/3d-models/none-ccb55b1309434d51875cbe2860d78e2f) | locopixel | CC BY-NC | 207 | Nave dorada |
| [No Man's Sky Atlas](https://sketchfab.com/3d-models/none-10618c9fb65b459886c591e043852692) | locopixel | CC BY-NC | — | El monumento del Atlas |
| [Sentinel Drone](https://sketchfab.com/3d-models/none-64e8761b44aa4eb99fb936887e576965) | locopixel | CC BY-NC | — | Dron Centinela |
| [Sentinel Summoner Drone](https://sketchfab.com/3d-models/none-68f2c0d1d0ee4ba7b6f3fe2c798bc2bc) | locopixel | CC BY-NC | — | Dron que llama a otros |
| [No Man's sky Fan art](https://sketchfab.com/3d-models/none-cfe751694fc94bdfae9aae3a4aaed999) | Rasmus.Eist | CC BY | — | Nave; la licencia más abierta |
| [NMS Starship](https://sketchfab.com/3d-models/none-25e26f50065c433f8120c5257d683250) | cmzw | CC BY | 101 | Nave |
| [Spaceship Fighter](https://sketchfab.com/3d-models/none-99c1d15965c74f3aa7b5999e2d4e42e1) | valterjherson1 | CC BY | 233 | Genérica, no es de NMS ⚠️ |
| [Cartoon spaceship](https://sketchfab.com/3d-models/none-a377d653202f45a68d441a987aa6dbda) | pinguinoconpulgares | CC BY | 118 | Genérica ⚠️ |

- **Crédito exacto** que se pone en la lámina o en su mensaje: «"No Man's Sky Portal" by locopixel, CC BY-NC 4.0, sketchfab.com». CC BY-NC permite un servidor sin ánimo de lucro, pero no vender la imagen.
- **Rigs del Viajero**: no hay ninguno libre ⚠️. Nadie buscó un modelo del Exotraje con licencia; en la lámina el traje entra como recorte de fotograma.

**Fan art como referencia** (enlace y autor, nunca para pegar):
- ArtStation: [Alexander Kovyazin](https://www.artstation.com/artwork/5Wkxg), [Emanuele Mattia Nava](https://www.artstation.com/artwork/qA0d6P), [Thomas Corvée](https://www.artstation.com/artwork/18lGzo) (un paisaje rehecho en Unreal) y [Artby Tessab](https://www.artstation.com/artwork/EL0mK8) ⚠️: cada uno es su propia página.
- «My Sky» de JoeyJazz, un mundo anillo en 2560×1440 ([DeviantArt](https://www.deviantart.com/joeyjazz/art/My-Sky-805137026), ♥ 47 en Wallhaven) ✅.
- Una acuarela de un jugador con su personaje en su planeta favorito, 681 votos ([Reddit](https://www.reddit.com/r/NoMansSkyTheGame/comments/1nyn5g4/watercolor_of_my_character_on_my_favorite_home/)) ✅. Es la prueba de que el fandom pinta **a su propio Viajero**.
- El cruce con *Rick and Morty* de kasqay: dos fondos, ♥ 85 y ♥ 66 ([1](https://w.wallhaven.cc/full/od/wallhaven-odlkd7.jpg), [2](https://w.wallhaven.cc/full/5d/wallhaven-5dzxw5.jpg)) ✅.
- En [Pixiv](https://www.pixiv.net/en/tags/No_Man's_Sky) casi no hay nada: el fan art japonés es escaso ⚠️ (dato negativo, comprobado).
- **Fotos reales con licencia CC BY 2.0** en Flickr, vía Openverse (autor blakespot). Son objetos reales que sirven para Blender:
  - la caja de la *Explorer's Edition* ([foto](https://live.staticflickr.com/657/32249960286_ba98c61326_b.jpg));
  - una lámina enmarcada en una pared ([foto](https://live.staticflickr.com/321/31644262184_6a24884310_b.jpg));
  - un **cuaderno de bitácora hecho por un fan** ([foto](https://live.staticflickr.com/65535/49846043101_c7470159f9_b.jpg)) ✅.

## 4 · Sitios, luz, paleta y texturas reales

Todos los hex están medidos con `estilo.py` sobre fotogramas y capturas, no de memoria ✅.

| Sitio | Luz y hora | Paleta medida | De dónde |
|---|---|---|---|
| Planeta del cierre del anuncio | Atardecer, luz rasante naranja-vino | `#630F31` 65 %, `#79273B`, `#2A0A1C` | [1:40](https://archive.org/details/youtube-aCgWabJssVI?t=100) |
| Playa de hierba roja | Día despejado, sombra suave | `#5E1120` hierba, `#E0EB99` arena, `#C9CFAD` cielo | [0:40](https://archive.org/details/youtube-aCgWabJssVI?t=40) |
| Sabana tóxica desde la cabina | Día con niebla verdosa, brillo alto | `#CCBC54` 35 %, `#C1E8B3` 25 %, `#B27957`; luego `#C7B653` y `#452F3D` | [3:40](https://www.dailymotion.com/video/x89lilx?t=220) |
| Hierba roja y setas (*Echoes*) | Mediodía, rojo contra azul | `#270E1E`, `#A00B0A`, `#609FDB`, `#B3D9F1` | [0:00](https://www.dailymotion.com/video/x8nggcs?t=0) |
| Cueva bioluminiscente (*Prisms*) | Casi negra, focos puros; brillo 8 % | `#070202` 66 %, `#200F09`, brasa `#741410`, luz `#586A6A` | [0:16](https://www.dailymotion.com/video/x89nujz?t=16) |
| Ladera sobre un lago (*Prisms*) | Nublado, poco contraste | `#535B5D`, `#3E462F`, `#232819` | [0:24](https://www.dailymotion.com/video/x89nujz?t=24) |
| Combate en niebla verde | Niebla muy saturada, sol quemado | `#999F5F`, `#C0E083`, `#75553D` | [1:20](https://archive.org/details/youtube--sK7EGiJSDk?t=80) |
| Fondo del cartel *Cosmos* | Espacio verde azulado y planeta rojo | `#49C0A9` 28 %, `#3B7872` 29 %, planeta `#85514C` | [1:52](https://archive.org/details/youtube--sK7EGiJSDk?t=112) |
| Bosque verde con niebla | Mediodía brumoso, brillo 24 % | `#130F0F`, `#1C322D`, jade `#528A75` | [captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/5/5d/20221009190548_1.jpg) 2560×1440 |
| Planeta óxido con plantas turquesa | Contraste cálido y frío | `#7D140A`, `#789D8A` | [captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/5/5c/20221014115848_1.jpg) |
| Desierto dorado | Anochecer, brillo 18 % | `#877140`, `#C7A45D`, `#EFE3BD` | [captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/0/03/20200222010737_1.jpg) |
| Corbeta sobre el agua | Reflejos duros en el casco | `#23233B`, `#215767`, agua `#A6CABE` | [captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/2/2c/Corvettelanding03tweak.jpg) |

- **La regla de todo el juego**: ninguna sombra midió negro puro. Siempre tienen tinte verde, vino o azul ✅. La excepción es la cueva de *Prisms*, que va casi negra a propósito (luz volumétrica).
- **Pareja de color típica**: cálido contra frío (rojo tierra con verde agua, rojo con verde azulado).
- **Texturas reales equivalentes**, todas CC0 de ambientCG:
  - [Ground054](https://ambientcg.com/a/Ground054): arena y barro de playa, 2048×2048, para desiertos y playas;
  - [Rock061](https://ambientcg.com/a/Rock061): roca de acantilado y cueva ⚠️ (tamaño sin medir);
  - [Corrugated Steel 009](https://ambientcg.com/view?id=CorrugatedSteel009): chapa ondulada para cascos de nave;
  - [Metal 063](https://ambientcg.com/view?id=Metal063): metal gastado para el Exotraje;
  - [Solar Panel 003](https://ambientcg.com/view?id=SolarPanel003): rejilla, como las velas de las naves.
