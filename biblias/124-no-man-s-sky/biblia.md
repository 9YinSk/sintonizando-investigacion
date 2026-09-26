# No Man's Sky — biblia (encargo 124)

Obra: **No Man's Sky**, videojuego de **Hello Games** (Guildford, Reino Unido). Salió el 12-ago-2016 en PS4 y PC; después Xbox, PS5 (con soporte de PS5 Pro) y realidad virtual (*Beyond*, 2019). Switch ⚠️: no aparece en las partes. Desde entonces lleva más de 18 actualizaciones grandes gratis.
Enfoque del encargo: **planetas de colores y portadas de ciencia ficción retro**. Personaje de partida: **el Viajero** (*the Traveller*).
Escrita por el redactor el 25-sep-2026 con las partes de imagen, vídeo, voz y texto (`partes/`). Lo que no está en las partes lleva ⚠️ o ❌ y se dice.
Continuada el 26-sep-2026 (modo «seguir»): la primera redacción se cortó tras §0. Ahora van los 25 puntos, las hojas, los conceptos, la tabla y la bitácora. El redactor además leyó el texto de 11 capturas de diálogo de la wiki y midió sus cajas con `estilo.py`.

Leyenda: ✅ = dos fuentes, o visto o medido · ⚠️ = una fuente, deducido o a medias · ❌ = no hecho.

## Segunda pasada · qué cambió

- **Antes**: sólo índice y §0. **Ahora**: §1-25, hojas, correcciones, 3 conceptos, tabla y bitácora.
- **Añadido por el redactor**: frases reales leídas en 11 capturas de diálogo (Polo, Nada, Artemis, Apollo, -null-, el Atlas, un Viajero NPC). Y los colores medidos de las cajas: la caja es translúcida y cambia de tono con el fondo (§6).
- **Corregido** (detalle en «Correcciones del redactor»): la narración del Viajero es en primera persona, no en tercera. Sí hay onomatopeya escrita: la estática «kzzkt». Los Autophage llegan con *Echoes* (2023), no con *Desolation*. En `referencias.json`, Polo es Gek, no Korvax.
- **⚠️**: antes había 1; ahora hay 77 en el texto (contando éste), casi todos datos de una sola fuente o cosas que no existen (comprobado). En la tabla quedan 20 ✅, 10 ⚠️ y ningún ❌, cada uno con su porqué.

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

## 5 · Tipografía

Las tildes, la ñ y los signos ¿¡ se comprobaron con `fontTools` en los archivos reales ✅.

| Uso | Letra del juego | Letra libre | Tildes, ñ, ¿¡ |
|---|---|---|---|
| Logo o título | «Geo NMS», retoque de Geo Sans Light (Manfred Klein, 2003) ([fontmeme](https://fontmeme.com/no-mans-sky-font/) y NMSCD) ✅ | **NMSGeoSans_Kerned** ([NMSCD](https://github.com/NMSCD/No-Mans-Sky-Universal-Font), OFL 1.1), o **[Jost](https://fonts.google.com/specimen/Jost)** (OFL) | ✅ las dos |
| Caja de diálogo actual (desde *NEXT*, 2018) | Roboto (lo dicen por separado 3 mods de [Nexus Mods](https://www.nexusmods.com/nomanssky/mods/1)) ✅ | **[Roboto](https://fonts.google.com/specimen/Roboto)** | ✅ |
| Caja de diálogo de 2016 | Sans fina de letras **muy separadas**, de la familia Geo Sans (visto en capturas de Polo y Nada) ⚠️ lo vio el redactor | NMSGeoSans con el espaciado a +150 | ✅ |
| Nombre de quien habla | Actual: Roboto pequeño en una pestaña. 2016: Geo Sans grande con una línea debajo en Roboto («Current Gek standing: Partner») | Roboto / NMSGeoSans | ✅ |
| Grito | **No hay**: nadie grita en texto. La emoción va en «...» y en la estática | — | — |
| Pensamiento | **No hay globo**: el Viajero narra en primera persona dentro de la misma caja | Roboto | ✅ |
| Onomatopeya | «kzzkt» y «kzzkkt», la estática de radio de los Viajeros, en la **misma letra** que el texto (visto en capturas de Artemis y -null-) | Roboto | ✅ |
| Cartel del mundo | Alfabeto alienígena: cambia cada letra latina por un glifo ([Alphabet](https://nomanssky.fandom.com/wiki/Alphabet), [Language](https://nomanssky.fandom.com/wiki/Language)) ✅ | «NMS Alphabet» de [Expedition Alphabet](https://github.com/NMSCD/Expedition-Alphabet) ([web](https://alphabet.nmscd.com/)), licencia FontStruct | ❌ **sin tildes, ñ ni ¿¡**: escribir sin ellas |
| Interfaz de juego | Clásica (2016-2018): NMSGeoSansLight y una Futura Pro. Actual: Roboto | **NMSFuturaProBook_Kerned** (NMSCD, OFL) o Roboto | ✅ |
| Subtítulos y créditos | Roboto, blanco, sin caja propia | Roboto | ✅ |
| Japonés, coreano, chino | Roboto no trae esos glifos. La comunidad pone Noto Sans CJK ([mod](https://www.nexusmods.com/nomanssky/mods/3117); [guía en japonés](https://steamcommunity.com/sharedfiles/filedetails/?id=1827579867)) ✅ | Noto Sans CJK | — |

- **Para la lámina**: título en Jost o NMSGeoSans, en mayúsculas y con aire entre letras. Texto de la caja en Roboto Regular, blanco. Glifos alienígenas sólo de adorno, nunca con información.
- **El cómic** *Adventures in No Man's Sky* (historia «Cargo», dibujada por Dave Gibbons, el de *Watchmen*) es la única pieza con globos ([wiki](https://nomanssky.fandom.com/wiki/Adventures_in_No_Man%27s_Sky)) ✅. La letra de sus globos no se pudo ver: no está escaneado en abierto ⚠️.

## 6 · Cómo hablan y piensan en pantalla

**Nunca hay burbuja blanca.** El diálogo es una **caja azul oscura translúcida** en la parte de abajo de la pantalla. Hay tres versiones, las tres vistas en capturas de la wiki.

**A. La caja actual (desde *NEXT* y *Beyond*)**. Vista y medida por el redactor en 6 capturas: [Polo](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/8/81/Polo-PL.jpg), [-null-](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/9/95/Nullsad-PL.jpg), [Artemis](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/0/0e/Art-PL.jpg), [el Atlas](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/8/88/Atlas-PL.jpg), [Apollo](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/f/f1/Apollo-PL.jpg) y un [Viajero NPC](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/f/f5/Hub_Traveler_Reference_2.jpg) ✅.
- **Forma**: rectángulo ancho, esquinas apenas redondeadas, centrado abajo. Ocupa unos 2/3 del ancho.
- **Textura**: una trama fina de **hexágonos** dentro del azul.
- **Arriba**, en el centro, un **arco de puntos blancos**, como el borde de un visor.
- **Pestaña del nombre**: una píldora oscura `#0E191F` arriba a la izquierda, con el nombre en blanco `#E7EFF2` («Specialist Polo», «-null-», «Traveller Nogiga»).
- **Texto**: blanco, Roboto, centrado, de 1 a 4 líneas.
- **Abajo en el centro**, un botón ⊗ con una flecha ⌄ («siguiente»). **Abajo a la derecha**, un círculo con un punto: el cursor.
- **Color**: es translúcida y **toma el tono del fondo**. Mide `#193D5D` sobre fondo claro, `#1C3A57` sobre dorado y `#222E3C` sobre rojo. Sobre naranja se ve marrón, `#2E2B29` (lo midió texto.md en la captura del Autophage).
- **Opciones** a la derecha, fuera de la caja: barras oscuras con una **rayita blanca vertical** a la izquierda y el texto en gris claro («Goodbye», «Comfort the Atlas»).

**B. La narración del Viajero** (captura del [Autophage](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/1/1f/Speaking_with_an_Autophage.png), 2522×1138; hoja 3, n.º 13) ✅:
- sin pestaña de nombre, texto alineado a la izquierda y **filete punteado** arriba y abajo;
- el Viajero cuenta lo que ve en **primera persona y en presente**: «*Construct Uahattrai, rebuilt and returned, turns to face me.*»;
- a la derecha, **opciones numeradas** con la tecla en un cuadrito: «[1] Offer assistance (Insufficient Standing)», «[2] Present a gift (1 Spool of Nano Cables)», «[3] Practice language», «[4] Leave». Las bloqueadas van en gris, con la condición entre paréntesis.

**C. La caja de 2016** (capturas de [Polo](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/7/7d/Polo_pur1.jpg) y [Nada](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/b/b2/NadaNoAtlas.jpg); hoja 2, n.º 52-54 y 60-61) ✅:
- el texto flota sobre una franja oscura, con letras finas **muy separadas**;
- abajo, una **barra azul a todo el ancho** (`#102230`) con el nombre grande («Specialist Polo») y el trato debajo («Current Gek standing: Partner»);
- las opciones van a la derecha, con el precio entre paréntesis: «Purchase Ship Tech (20000 UNITS)».

**D. Los Viajeros NPC encierran su frase entre signos**: «-{{ If so, you'll love the Rentocniijk Expanse! Our capital, Drogradur NO425, is throneworld to our thriving community of interdimensional anomalies. }}-» (visto de cerca por el redactor; hoja 3, n.º 11) ⚠️: una sola captura.

**E. El idioma alienígena se entiende a trozos** ([Language](https://nomanssky.fandom.com/wiki/Language)) ✅:
- hay 5 idiomas: Gek, Korvax, Vy'keen, Autophage y el del Atlas;
- se aprenden 3.813 palabras: 921 Gek, 858 Korvax, 930 Vy'keen, 889 Autophage y 222 del Atlas;
- en pantalla, las palabras aprendidas salen legibles y el resto no;
- se aprende con las **Knowledge Stones** o con el implante [Automatic translation device](https://nomanssky.fandom.com/wiki/Automatic_translation_device) (hasta 7 palabras más de golpe).

**F. Pantallas dentro del mundo** ([Overseer](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/e/eb/Overseer_NPC.png); hoja 3, n.º 16) ✅:
- hologramas de planos técnicos: fondo `#0A1110`, cian `#3D8DB3` y `#8AC5D0`, línea `#F2F4F3`, acento verde `#36E27C`;
- sin texto grande, sólo iconos de línea.

**G. Carteles**: glifos con el inglés debajo. En un carguero se lee «In case of gravity or pressure loss follow emergency procedures» ([foto](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/4/4a/Freighter_writing.jpg)) ✅.

**H. El traje también habla**: Telamon, la IA del Exotraje, da los avisos de peligro y de salud con una voz sintética. Es la única voz de diálogo real del juego ([wiki](https://nomanssky.fandom.com/wiki/Telamon)) ✅. El aspecto del aviso en pantalla no se midió ⚠️.

**Pensamiento**: no hay monólogo interior aparte ⚠️. Lo que «piensa» el Viajero es la narración de B.

## 7 · Personajes y popularidad

**No hay encuesta oficial de personajes**, y se buscó: el juego no tiene reparto fijo ⚠️. Lo más parecido:
- **La especie favorita**: el hilo «What's your favorite Alien race in the game and why?» tiene 131 votos y 137 comentarios ([Reddit](https://redd.it/1msvwup), leído por Arctic Shift) ✅.
  - A los **Gek** los llaman «adorable» y «super cute».
  - Los **Korvax** gustan «por lo técnico».
  - Los **Autophage** tienen su broma: «Autophage: Am I a joke to you?».
  - No hay un ganador claro ⚠️.
- **El personaje más dibujado es el propio Viajero de cada jugador**: la acuarela con más votos del recolector (681) es «my character» ([Reddit](https://www.reddit.com/r/NoMansSkyTheGame/comments/1nyn5g4/watercolor_of_my_character_on_my_favorite_home/)) ✅. Hay más hilos «My favorite character» (95 y 74 votos), sin saber de quién ⚠️.
- **Los personajes con nombre más recordados** son Nada y Polo (la pareja de la Anomalía) y Artemis (la historia que emociona) ⚠️: sale de lo que cuentan las partes, no de una votación.

**Quién va en la lámina**:
- **El Viajero** es el que pide el encargo y el que todo jugador reconoce: el casco con visera y la mochila con luces.
- **Polo** (Gek) es el secundario amable para **explicar** cosas.
- **Nada** (Korvax) es para lo **misterioso** o lo serio.
- **Con quién aparecen**: Nada y Polo siempre juntos en la Anomalía Espacial. El Viajero, solo ante un paisaje, o con compañeros en el cartel de *Cosmos*.

## 8 · Doblaje: no hay latino (y lo que sí hay)

- **No existe versión en español latino**, ni de texto ni de voz. La lista oficial de Steam sólo trae «Español de España», con el asterisco de audio ([API de Steam](https://store.steampowered.com/api/appdetails?appids=275850)) ✅. Lo confirma un hilo de jugadores de jul-2018: al ponerlo, «sale en español de España» ([Steam Community](https://steamcommunity.com/app/275850/discussions/0/1762481957308442405/)) ✅.
- **Doblaje Wiki no tiene página del juego**. Se probaron tres títulos por la API `action=parse` y una búsqueda; todos dan «missingtitle» ([API](https://doblaje.fandom.com/es/api.php)) ✅.
- **Por qué no hay doblaje clásico**: los alienígenas no tienen actores. Su voz la crea **Paul Weir** con **VocAlien**, un programa que imita una garganta y se toca como un instrumento con MIDI. Por eso suena igual en todos los idiomas ([Behind The Voice Actors](https://www.behindthevoiceactors.com/video-games/No-Mans-Sky/): «Aliens — voiced by Paul Weir», el único actor de la ficha; y la entrevista en [Audiokinetic](https://www.audiokinetic.com/en/blog/behind-the-sound-of-no-mans-sky-a-qa-with-paul-weir-on-procedural-audio/)) ✅.
- **La única voz con texto es Telamon**, la IA del traje. Da avisos cortos «con tono cibernético» y sólo está en español de España ✅.
- **Un tráiler con actor famoso**: «I've Seen Things», con **Rutger Hauer**, presentado en la Paris Games Week (oct-2015). Recita su monólogo de *Blade Runner* adaptado al juego ([PCGamesN](https://www.pcgamesn.com/no-mans-sky/no-mans-sky-trailer-reveals-june-release-date-also-rutger-hauers-voice) y [Nerdbot](https://nerdbot.com/2022/02/17/no-mans-sky-trailer-features-rutger-hauers-likely-last-voice-over/), que dice que quizá fue su última grabación) ✅.
  - Oído con `voz.py` en el [minuto 0:02](https://www.dailymotion.com/video/x443lhp?t=2) ✅:
    - voz grave, 110 Hz;
    - muy expresiva, 33 semitonos de rango;
    - muy lenta, 0,54 palabras por segundo.
- **No hay frases del doblaje latino que citar**, porque no existe. Para la lámina, el texto se escribe en **español neutro** en la voz del juego (§17), y se dice así en el mensaje del canal.
- **ANMTV** está bloqueado en este contenedor (probado con curl y `navegar.py`) ⚠️. Es poco probable que tenga el juego.

## 9 · Música y sonido

- **La banda sonora**: *No Man's Sky: Music for an Infinite Universe*, de la banda de *math-rock* **65daysofstatic**. Salió el 5-ago-2016 con 10 temas ([wiki](https://nomanssky.fandom.com/wiki/Music_for_an_Infinite_Universe) y [MusicBrainz](https://musicbrainz.org/release-group/b0fb336e-dfc0-4049-be04-bf4c903b46b9)) ✅. Los temas: Monolith, Supermoon, Asimov, Heliosphere, Blueprint For a Slow Machine, Pillars of Frost, Escape Velocity, Red Parallax, Hypersleep y End of the World Sun.
- **El tema que todo fan reconoce**: «**Supermoon**», que sonó en los tráileres de 2014 a 2016 ✅. En la primera presentación, en 2013, sonó «Debutante», de la misma banda.
- **Cómo nació**: Sean Murray y Paul Wolinski (de 65daysofstatic) llegaron a la primera reunión queriendo proponer lo mismo ([MusicRadar](https://www.musicradar.com/news/guitars/how-65daysofstatic-built-the-soundtrack-to-no-mans-skys-infinite-universe-641184)) ✅.
- **La música nunca suena igual**: un sistema propio, **Pulse**, mezcla en directo «un par de horas» de material: 24 paisajes sonoros y 60 variaciones de base ([A Sound Effect](https://www.asoundeffect.com/no-mans-sky-sound-procedural-audio/)) ✅. Joe Shrewsbury, de la banda, lo resume así: «As a musician, it forces you to give up on being precious about anything» ⚠️ (una fuente).
- **El ambiente que da**: guitarras en capas y electrónica. Asombro y soledad, como el tono del juego.
- **Las criaturas**: sus voces las fabrica en tiempo real el sintetizador **VocAlien**, de Paul Weir y Sandy White. Se explica en la charla del GDC «[The Sound of No Man's Sky](https://www.gdcvault.com/play/1024067/The-Sound-of-No-Man)» ✅.
- **Efectos con historia** (A Sound Effect, una fuente) ⚠️:
  - el buggy suena con el coche de Paul Weir, grabado con micrófonos de contacto;
  - el aerodeslizador mezcla un ventilador de mesa y un aire acondicionado;
  - la lluvia sale de bombas de agua, máquinas expendedoras y motores de garaje.
- **Más discos**: *Journeys: Original Soundtrack* (2025) y *Vostok / The Journey* (2025), también de 65daysofstatic con Paul Weir ([MusicBrainz](https://musicbrainz.org/release-group/33a46a1b-3513-475a-935f-1331d3bc7688)) ✅.
- **La onomatopeya escrita**: «kzzkt», la estática de radio en las frases de los Viajeros (§5 y §6) ✅.
- **Qué tema suena en la escena más emotiva**: no se pudo confirmar ⚠️. La música se genera en directo y ninguna fuente ata un tema a una escena.

## 10 · Vídeos y tendencias

**Tráileres oficiales**:
- Anuncio (VGX 2014), 1:58 ([Internet Archive](https://archive.org/details/youtube-aCgWabJssVI)) ✅.
- E3 2015, 5:32, en la conferencia de PlayStation ([Dailymotion](https://www.dailymotion.com/video/x89lilx)) ✅.
- «I've Seen Things», con Rutger Hauer ([Dailymotion](https://www.dailymotion.com/video/x443lhp)) ✅.
- *Prisms*, de 1:49 a 1:50 ([Dailymotion](https://www.dailymotion.com/video/x89nujz)) ✅.
- *Echoes*, 1:29 ([Dailymotion](https://www.dailymotion.com/video/x8nggcs)) ✅.
- 10.º aniversario y anuncio de *Cosmos*, 2:07, ago-2026 ([Internet Archive](https://archive.org/details/youtube--sK7EGiJSDk); lo describe igual [Shacknews](https://www.shacknews.com/article/150314/no-mans-sky-10th-anniversary-cosmos-teaser)) ✅.

**Análisis**:
- «The Redemption Of No Man's Sky», de GameSpot: 14:39, 46 687 vistas, 1-ago-2018. Repasa cómo se rehízo el juego ([YouTube](https://www.youtube.com/watch?v=3TpTSuaElVQ)) ✅.
- «The Engoodening of No Man's Sky», de Internet Historian: unos 53:50, 9-ene-2020. Es la historia de la redención más vista ([YouTube](https://www.youtube.com/watch?v=O5BJVO3PDeQ); nota 8,9 en [IMDb](https://www.imdb.com/title/tt12681108/)) ✅.
- En español: «De ESTAFA a OBRA MAESTRA: No Man's Sky» (may-2026) ([YouTube](https://www.youtube.com/watch?v=EXLFqQKsRZw)) ⚠️: no se pudo abrir.

**Tendencias**:
- En 2016, los memes «One Man's Lie» sobre las promesas que no se cumplieron, sobre todo el multijugador, y la ola de reembolsos ([Know Your Meme](https://knowyourmeme.com/memes/subcultures/no-mans-sky)) ⚠️.
- **Luego la remontada**: en Steam pasó de «Mostly Negative» (2016) a «Very Positive» ✅. Ganó **Mejor Juego en Curso** en The Game Awards 2020 y 2025 ✅.
- En TikTok, un vídeo de @thepoddaddy sobre los «80 cuadrillones de planetas» tiene 271 800 me gusta ([TikTok](https://www.tiktok.com/@thepoddaddy/video/7488369729720093983)) ⚠️: las cifras cambian.
- También se repiten los vídeos «cómo cambió el juego en X años» ([TikTok](https://www.tiktok.com/discover/no-mans-sky)) ⚠️. No encontré un reto o *hashtag* propio que se hiciera viral.
- **Tráileres de la prensa española** en Dailymotion (del recolector, sin mirar) ⚠️:
  - [*Omega*, de Vandal](https://www.dailymotion.com/video/x8ssute), 1:32, 10 939 vistas;
  - [«Combate», de Meristation](https://www.dailymotion.com/video/x4l05y0), 1:08;
  - [*Aquarius*, de HobbyConsolas](https://www.dailymotion.com/video/x955kj4), 1:10.

## 11 · El videojuego: interfaz y menús

**Es un solo juego**, sin secuelas. Lo que hay son 18 o más **actualizaciones gratis**, cada una con su nombre ([registro oficial](https://www.nomanssky.com/release-log/), [Wikipedia](https://en.wikipedia.org/wiki/No_Man%27s_Sky)) ✅. *Light No Fire*, el próximo juego del estudio, no es de esta franquicia.

- **Catálogo de la interfaz** en [Game UI Database](https://www.gameuidatabase.com/gameData.php?id=293) ✅: fabricación, editor de personaje, misiones, mapa, diario de descubrimientos, modo foto, constantes vitales, brújula, marcadores y registro de combate.
  - Esa web **prohíbe usar sus capturas en IA**: sólo sirve para mirar.
- **Inventario del Exotraje (2016)**: rejilla de casillas cuadradas ([captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/e/e4/NmsExosuit_Panel.jpg); hoja 3, n.º 17) ✅.
  - Cada recurso lleva su **símbolo químico en una etiqueta de color**: C naranja (carbono), Si turquesa (silicio), S amarillo (azufre), Pu morado (plutonio).
  - Arriba, pestañas en mayúsculas: `SUIT | WEAPON | SHIP | DISCOVERIES | OPTIONS`.
  - El dinero va en una placa roja: «10,000 U».
- **Inventario actual (*NEXT*)**: el traje en 3D en el centro y la rejilla a los lados, sobre azul (hoja 1, n.º 2-5 y 30-32) ✅.
- **Ficha de tecnología**: tarjeta oscura con título en mayúsculas y datos en dos columnas, como «VESPER SAIL · Advanced Engine Technology» (hoja 2, n.º 55) ✅.
- **Indicador del arma** en el HUD: «99% Personal Forcefield», «81 / 1428 Boltcaster», «Switch», con marco verde (hoja 2, n.º 68) ✅.
- **Menú rápido**: círculos oscuros translúcidos con icono blanco y el nombre encima («Exocraft Miner») ([captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/e/e5/QuickMenu02.jpeg); hoja 3, n.º 18) ✅. Abajo, la ayuda de teclas: «Q/E Navigate», «F Charge», «C Close». En la esquina, el planeta y su temperatura: «Anzhensky Noydeni 19.0°C».
- **Mapa de la galaxia**: fondo `#03131D`, `#051B28`, `#020E16` y `#092433` ([captura](https://nomanssky.fandom.com/wiki/File:NMS1dot3GalaxyMap.jpg); hoja 3, n.º 15) ✅.
  - La estrella elegida lleva una etiqueta fina con la distancia: «Distance: 4004 LY».
  - Abajo, una ficha con icono y texto por fila: especie, economía y conflicto.
- **Modo Foto**: los «filtros de la animación» del juego (§18) ✅.
- **Mods y extractores**: [MBINCompiler](https://github.com/monkeyman192/MBINCompiler) abre los archivos del juego. En Nexus Mods hay cambios de letra y un mod que quita la aberración y el viñeteado ✅.

## 12 · Lo que ama el fandom y qué NO hacer

**El gran chiste interno es su propio lanzamiento y su remontada.**
- En ago-2016 faltaba lo prometido: el multijugador y las criaturas gigantes.
- Hubo reembolsos incluso en PS4: Sony rompió su norma.
- La ASA británica investigó la publicidad y en 2017 falló a favor de Hello Games ([IBTimes](https://www.ibtimes.com/no-mans-sky-devs-did-not-mislead-players-asa-says-ruling-hello-games-valve-case-2453084), [TechRadar](https://www.techradar.com/news/no-mans-sky-didnt-mislead-consumers-rules-the-asa)) ✅.
- Hoy «to pull a No Man's Sky» es jerga de la industria: salir roto y redimirse con años de parches gratis ([Eurogamer en X](https://x.com/eurogamer/status/2086817804225819003)) ⚠️.

**Lo que celebra en los posts con más votos** (Reddit, del recolector) ✅:
- las tormentas: «Why do the storms in this game look so damn good», 3064 votos ([hilo](https://www.reddit.com/r/NoMansSkyTheGame/comments/1l879sc/why_do_the_storms_in_this_game_look_so_damn_good/));
- las naves y las corbetas: «I still prefer to fly my starship over my corvette», 5382 votos y 775 comentarios; «My squadron will beat up your squadron», 794 votos;
- aterrizar en un planeta nuevo: «man I love exploring new planets», 333 votos;
- las Expediciones, porque «te cruzas con mucha más gente», 104 votos;
- el debate eterno: «Paradise Planets are Overrated», 350 votos;
- los guiños de ciencia ficción: el casco «Kappa» homenajea a Capa, de *Sunshine* (30 votos) ⚠️.

**Campaña de cada diciembre**: votarlo al «Labour of Love» de los Steam Awards, al que está nominado desde 2018 sin ganar nunca ([hilo 1](https://steamcommunity.com/app/275850/discussions/0/694248493352507893/), [hilo 2](https://steamcommunity.com/app/275850/discussions/0/691994126364810870/)) ✅.

**Qué NO hacer** (a un fan le parecería falso):
- **Globo blanco de cómic**: el juego usa cajas azules translúcidas (§6).
- **Negro puro o naves grises**: va contra la idea del director de arte (§1).
- **Una cara fija para el Viajero** como si fuera la oficial: es un traje sin rostro y cada jugador lo personaliza.
- **Alienígenas que hablan en frases enteras y claras**: se les entiende a trozos, con palabras sueltas.
- **Presentar el juego de 2016 como si ya lo tuviera todo**, o reírse de Sean Murray con el tono cruel de 2016. Hoy el fandom lo trata con cariño.
- **Dibujar una colaboración con Palworld como si existiera**: sólo es un coqueteo en redes (§23).
- **Contorno negro grueso o *cel-shading*** de anime: el juego es degradado y pintado (§18).
- **Escribir con tildes en la letra de glifos**: no las tiene (§5).
- **Hablar de un «doblaje latino oficial»**: no existe (§8).

## 13 · Personajes a fondo

**Cara en cada emoción: no aplica, y está comprobado** ✅. Nadie tiene gestos de cara por emoción: el Viajero no tiene rostro, y los Viajeros NPC y las especies son modelos que no cambian de cara. Se buscó en la wiki por la API (archivos «Nada angry/happy/sad», imágenes «Korvax») y no hay ninguna.
**En este juego la emoción va en cuatro cosas**: el texto, la **luz** (el rojo del Atlas es peligro y destino), la **postura** y la **estática** «kzzkt» en la voz de los Viajeros.

**El Viajero** (el jugador):
- **Quién es**: un Exotraje que se estrella en un planeta y encuentra su nave destruida. No se le ve nunca la cara ([Exosuit](https://nomanssky.fandom.com/wiki/Exosuit)) ✅.
- **Qué transmite**: asombro y soledad, y la calma del que tiene toda la galaxia por delante.
- **Cómo se expresa**: sólo narrando, en primera persona y en presente («*… turns to face me*», «*Nada's paranoia is infectious. I find myself…*»).
- **Lenguaje corporal**: brazos sueltos al contemplar, arma al frente al combatir y cabeza baja al examinar algo (§14).
- **Su arco**: llegar al centro de la galaxia, seguir la señal de Artemis y descubrir qué es el Atlas.

**Nada** (Entidad Sacerdote, Korvax) ([wiki](https://nomanssky.fandom.com/wiki/Priest_Entity_Nada)) ✅:
- **Quién es**: una Korvax que se sale de la norma. La Convergencia, la mente colmena Korvax, quiere recuperar su cuerpo y «borrarla». Por eso **va siendo más paranoica** a lo largo de la partida.
- **Qué transmite**: misterio e inquietud, y algo de ternura con Polo.
- **Cómo habla**: **telegráfico, a base de preguntas cortas**. En una [captura de 2016](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/b/b2/NadaNoAtlas.jpg): «Red orbs. Dominant, hostile. Creators or their relics? Singularities are key. Peripatetic path to galactic core. Path message from creator? Or sloppy workmanship?» ✅.
- **Su objeto**: la capa azul noche y roja, con tres naves y el símbolo del Atlas bordados.

**Polo** (Especialista, Gek) ([wiki](https://nomanssky.fandom.com/wiki/Specialist_Polo)) ✅:
- **Quién es**: un traductor enviado a un puesto remoto como castigo por su conducta. Curioso por naturaleza.
- **Qué transmite**: calidez y un humor pícaro. Es el «adorable».
- **Cómo habla**: frases cortas y repetidas, con «friend» y «oh yes», y cambia de idea a media frase. En sus [capturas de 2016](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/e/e9/SpecialistPolo.jpg) ✅:
  - «You, friend, visit the worst places you can find. Stay alive. No good to me dead, are you? Can't learn much from a corpse. Although... No, never mind, stay alive.»
  - «Always more to do, oh yes, but not just now, friend. Go, be free, see the stars.»
  - Hoy, más tierno: «A whole galaxy for you, just for you. You must see it all.»
- **Su objeto**: una tablet cian (visto; hoja 1, n.º 26-28).

**La pareja Nada y Polo**: en otro universo, cuando los Centinelas habían borrado toda la vida, Nada salvó a Polo. Viajaron juntos hacia el centro, perseguidos. Antes de morir, ese Polo le prometió que se volverían a ver en otro universo. Ahora están juntos en la Anomalía sin saberlo del todo ✅.
- Un mensaje de aquel Polo, en una [captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/e/e4/Backstory-PL.jpg): «I told Nada to leave. I told them what we already know, all of us, in our hearts... we are not alone. Even if I die, even if all that is left of me are these words, Nada will find me again in another universe.» ✅.

**Artemis** (Viajero, de *Atlas Rises* en adelante) ([wiki](https://nomanssky.fandom.com/wiki/Artemis)) ✅:
- **Quién es**: el jugador la oye por radio y la ayuda a encontrar su posición. Esa posición «no existe»: Artemis ya está muerta. El jugador decide si sube su mente a una simulación o la deja descansar.
- **Su aspecto**: un «gris» clásico, con tonos arena y dorado.
- **Cómo habla**: poética y rota por la estática. En una [captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/0/0e/Art-PL.jpg): «The noises... the sound of kzzkt – it's the sound of waking. It's the sound of everything falling apart. It's the final gasp. The death of the Atlas will not begin in sixteen minutes. It began a long time ago.» ✅.

**Apollo** ([wiki](https://nomanssky.fandom.com/wiki/Apollo)) ✅:
- **Quién es**: tenía cuerpo de carne y hoy es casi todo máquina. Frío, sólo le importan las unidades: «el dinero es lo único que importa en la vida».
- **Cómo habla**: seco y escéptico. En una [captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/f/f1/Apollo-PL.jpg): «Or perhaps it was nothing, a ghost in the machine...».

**-null-** ([wiki](https://nomanssky.fandom.com/wiki/-null-)) ✅:
- **Quién es**: un Viajero de otro universo que vivió una eternidad catalogando cada mundo. El Atlas le dijo que era «uno más entre infinitos viajeros» y dejó de hablarle. Ahora tiene celos del jugador.
- **Qué transmite**: amargura, y la tristeza del que lo dio todo.
- **Cómo habla**: «I was born to travel, to see these worlds, to catalogue them, to give a name to every creature, every planet. The skies... they were mine.». Y en una [captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/9/95/Nullsad-PL.jpg): «Why won't it speak to me? Why – kzzkkt – aren't I enough?».

**El Atlas** ([wiki](https://nomanssky.fandom.com/wiki/The_Atlas)) ✅:
- **Quién es**: el «creador» al que adoran los Korvax y los Gek. En realidad es el ordenador que simula el universo.
- **Su imagen**: una esfera roja facetada dentro de un rombo rojo de neón.
- **Cómo habla**: a trozos, con mayúsculas irregulares, como una terminal. En una [captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/8/88/Atlas-PL.jpg), el Viajero narra: «It is dying. The Atlas is dying... It cries out at me, afraid...», con la opción «Comfort the Atlas».

**Telamon**: la IA que el Atlas mete en el traje ([wiki](https://nomanssky.fandom.com/wiki/Telamon)) ✅. Es analítica y melancólica: habla de que «nos están cazando» y de un «mundo de cristal» bajo la realidad.

**Las especies**:
- **Gek** ([wiki](https://nomanssky.fandom.com/wiki/Gek)) ✅:
  - anfibios comerciantes, con ojos y pico de ave;
  - sus antepasados, los First Spawn, fueron un imperio genocida;
  - hablan también con olores (el GekNip).
- **Korvax** ([wiki](https://nomanssky.fandom.com/wiki/Korvax)) ✅:
  - máquinas muy intelectuales que adoran al Atlas;
  - el casco cambia según su papel en la Convergencia;
  - **siempre llevan una tablet**.
- **Vy'keen** ([wiki](https://nomanssky.fandom.com/wiki/Vy%27keen)) ✅:
  - reptiles guerreros, encorvados y de mandíbula grande;
  - tienen un código de honor, y para su profeta Hirk el Atlas es un dios falso.
- **Autophage**: robots que se desmontan y se rehacen, y que llegan con *Echoes* (2023) ✅ (vídeo y voz coinciden).
- **Centinelas**: drones policía de origen oscuro, el enemigo de siempre ([wiki](https://nomanssky.fandom.com/wiki/Sentinel)) ✅.

**Dinámicas para láminas en grupo**:
- Polo hace de guía amable y Nada de voz inquieta.
- Apollo es el cínico frente a Artemis, la soñadora.
- -null- tiene celos del Viajero.
- Los Gek regatean y los Vy'keen presumen de honor.

## 14 · Poses analizadas

El Viajero no tiene escenas con guion propias: sus poses salen de los **tráileres** y de las capturas de la wiki ✅.

| # | Pose | Dónde | Postura, manos, mirada | Sirve para |
|---|---|---|---|---|
| 1 | De perfil ante una planta que brilla | *Prisms* [0:16](https://www.dailymotion.com/video/x89nujz?t=16); hoja 3, n.º 7 | Erguido, casco con visera oscura, luces verdes de la mochila encendidas, mirada baja | **Pensar**, examinar |
| 2 | De espaldas en lo alto de una ladera | *Prisms* [0:24](https://www.dailymotion.com/video/x89nujz?t=24); hoja 3, n.º 8 | Brazos sueltos. A su lado, una criatura verde flotante y un robot con luces | **Animar**, contemplar |
| 3 | Apuntando con la multiherramienta | 10.º aniversario [1:20](https://archive.org/details/youtube--sK7EGiJSDk?t=80); hoja 3, n.º 9 | Primera persona, brazos al frente, mira sobre una criatura mecánica gigante | Acción, **regañar** con humor (apuntar al que rompe las normas) |
| 4 | Erguido entre dos compañeros | *Cosmos* [1:52](https://archive.org/details/youtube--sK7EGiJSDk?t=112); hoja 3, n.º 10 | Cámara al pecho, visera dorada. Los compañeros, con los brazos cruzados | **Presentar**, **celebrar** |
| 5 | Viajero NPC a media frase | [captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/f/f5/Hub_Traveler_Reference_2.jpg); hoja 3, n.º 11 | Primer plano, cabeza ladeada hacia la cámara, boca entreabierta, caja de diálogo abierta | **Explicar** |
| 6 | Dos Viajeros hablando | [captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/5/57/TwoTravellers.png); hoja 2, n.º 59 | Uno con una tablet, gesticula con la mano libre; el otro escucha con los brazos caídos | **Explicar** en pareja |
| 7 | Andando por un pasillo | [captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/d/d4/TravellerInFreighter.jpg); hoja 1, n.º 29 | Pequeño en el encuadre, hacia la cámara, luces azules detrás | Entrada, bienvenida |
| 8 | Hojas de cascos | [Heads](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/e/e1/Traveller_-_Heads.png) y [Heads 2](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/f/fc/Traveller_-_Heads_2.png); hoja 1, n.º 8 y 20 | Cascos y cabezas desde varios ángulos | Diseño, no pose |
| 9 | Polo de brazos cruzados ante su tablet | [Polo](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/8/81/Polo-PL.jpg); hoja 1, n.º 26-28 | Cuerpo girado, tablet cian en la mano | Explicar con cariño |
| 10 | Nada de pie con la capa | [Nada Cape](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/9/9e/Nada_Cape.jpg); hoja 1, n.º 25 | De espaldas y quieta; la capa cae recta con el emblema | Solemne, misterio |

- **Regañar**: el Viajero no tiene ninguna pose de enfado ✅ (buscado). Lo más cercano es **el texto de Polo** («Stay alive. No good to me dead, are you?»), dicho con pose tranquila.
- Las filas 5, 6, 7 y 9 son de una sola captura de la wiki cada una ⚠️.

## 15 · Vestuario con hex medidos

**El traje ES el personaje**: el Exotraje da inventario, protección y un salto con mochila. Su color se cambia en los «Appearance Modifiers» de las estaciones ([wiki](https://nomanssky.fandom.com/wiki/Exosuit)) ✅. No hay un traje único oficial: en la lámina, mejor el de serie.

| Pieza | Colores medidos | Imagen |
|---|---|---|
| Exotraje y nave por defecto (*NEXT*) | Fondo de nave `#020608` y `#0A2334`, luces turquesa `#02DBF0`, acento óxido `#D17359`. Línea fina `#1E343E`, saturación 63 %, brillo 27 % | [3840×2160](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/3/3a/NmsNext_Default_Exosuit_Starship.jpg); hoja 1, n.º 1 |
| Multiherramienta estándar (rifle IAAF) | Metal azulado `#A6D9FA`, gris verdoso `#6A7E7E`, azul marino `#13223C`, rojo `#974C4A`, dorado `#E0A62D` | [1600×900](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/c/c7/Standard_IAAF_Rifle.png); hoja 2, n.º 56 |
| Capa de Nada | Azul noche `#24264C` y `#191B35`, forro vino `#5C2C31` | [1080×1920](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/9/9e/Nada_Cape.jpg) |
| Artemis | Arena `#C9B883`, dorado `#F3C952`, verde azulado técnico `#55717A` | [468×1080](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/6/63/Artemis_Front.jpg); hoja 2, n.º 70 |
| Traje del cartel *Cosmos* | Blanco y rojo, con visera dorada (visto; hoja 3, n.º 10) | Sin medir ⚠️ |
| Polo | Chaleco y bufanda de colores, con tablet cian (visto; hoja 1, n.º 26-28) | Sin medir ⚠️ |

- **La multiherramienta de serie** es la Waveform Focuser N56-P ([wiki](https://nomanssky.fandom.com/wiki/Multi-Tool); hoja 1, n.º 5) ✅.
- **Lo icónico que todos reconocen**: el casco redondo con visera, la **mochila con luces** y la multiherramienta en la mano.
- **Peinado y temporadas**: no aplican ⚠️. Nunca se ve el pelo, y el traje no cambia por arcos: cambia porque el jugador lo tiñe.
- **Las 22 especies de Viajero** varían mucho: rasgos de gato, de insecto o de anfibio, cabezas robóticas. -null- está hecho de cables ✅.

## 16 · Paisajes y fondos de pantalla

**No hay ciudades fijas.** El sitio fijo es la **Anomalía Espacial**: una estación «fuera del tiempo y del espacio» a la que se llega desde cualquier sistema. Allí viven Nada y Polo y está **el Nexo**, el tablón de misiones en grupo ([wiki](https://nomanssky.fandom.com/wiki/Space_Anomaly)) ✅.
- Otros sitios que se repiten: la **cabina** de la nave (hoja 1, n.º 16, 37, 38, 40, 42-44 y 47), el **hangar del carguero** (n.º 29), la **interfaz del Atlas** (hoja 3, n.º 14) y las **bases de asentamiento** con hologramas (n.º 16).
- **Hora del día**: cualquier planeta puede verse a cualquier hora, así que se elige según el canal ⚠️. Las capturas medidas van del mediodía brumoso al anochecer (§4).

**Fondos de pantalla en alta** (Wallhaven; los ♥ son del recolector) ✅:

| Tamaño | ♥ | Autor o subida | Qué es | Enlace |
|---|---|---|---|---|
| 8250×4672 | 72 | GameVogue; origen no-mans-sky.com | Arte promocional rosa y turquesa | [imagen](https://w.wallhaven.cc/full/4x/wallhaven-4xvdxo.jpg) |
| 3840×2160 | 122 | yaxe | *NEXT*: astronauta y planeta (el más guardado) | [imagen](https://w.wallhaven.cc/full/r2/wallhaven-r2779q.jpg) |
| 3840×2160 | 71 | rootkit; origen «Dimensional warping» de u/the_sonnie | Nave en un agujero de gusano | [imagen](https://w.wallhaven.cc/full/dg/wallhaven-dgoz3m.png) |
| 3840×2160 | 52 | arg81 | Planeta | [imagen](https://w.wallhaven.cc/full/p2/wallhaven-p2kx6p.jpg) |
| 2560×1440 | 49 | viennesecinnamon | Buceo espacial | [imagen](https://w.wallhaven.cc/full/y8/wallhaven-y8xwox.jpg) |
| 2560×1440 | 47 | JoeyJazz | Mundo anillo con árboles | [imagen](https://w.wallhaven.cc/full/kw/wallhaven-kw21r7.jpg) |
| 2280×1280 | 49 | Kuldar Leement; origen hellogames.org | **Oficial**, planeta cian. Medido: `#AEC5B8`, `#66AAA7`, vino `#72343F` | [imagen](https://w.wallhaven.cc/full/2k/wallhaven-2kzwg9.jpg) |
| 2048×1228 | 55 | yaxe; origen un tuit | Nave, traje y nubes | [imagen](https://w.wallhaven.cc/full/96/wallhaven-9655vd.jpg) |
| 1920×1080 | 109 | cuenta borrada | Arte de PS4, cielo | [imagen](https://w.wallhaven.cc/full/n6/wallhaven-n611mw.jpg) |
| 1920×1080 | 73 | kejsirajbek | *Pixel art* de agua y espacio | [imagen](https://w.wallhaven.cc/full/2k/wallhaven-2kggx9.png) |
| 1920×1080 | 71 | bfoxwell | Cielo | [imagen](https://w.wallhaven.cc/full/nm/wallhaven-nmdgmy.jpg) |
| 1920×1080 | 60 | OganjKaramel | *NEXT* | [imagen](https://w.wallhaven.cc/full/wq/wallhaven-wq5xm7.jpg) |
| 1920×1080 | 48 | cuenta borrada | Arte conceptual colorido | [imagen](https://w.wallhaven.cc/full/01/wallhaven-01eqog.png) |

- **Capturas de jugadores con licencia CC BY 2.0** (Flickr, Stefans0), en 1024×576: «[Staring Into The Sun](https://live.staticflickr.com/4546/38624740696_0b1e765272_b.jpg)», «[Downed at Dawn](https://live.staticflickr.com/4343/36840764471_b1f1a646f0_b.jpg)» y «[Crashed](https://live.staticflickr.com/4439/36946556991_198f9a71e6_b.jpg)» ✅.
- **Capturas oficiales de Steam** en 1920×1080: planos muy abiertos y naves en diagonal ([tienda](https://store.steampowered.com/app/275850)) ✅.

## 17 · Guía para IA de imagen y de texto

### Para una IA de imagen (Firefly, Canva)

**Rasgos del Viajero que nunca cambian**:
- un traje espacial acolchado, con **casco redondo y visera opaca**: nunca se le ve la cara;
- una **mochila con luces** turquesa (`#02DBF0`) o verdes;
- una multiherramienta retrofuturista en la mano, entre pistola y rifle;
- siempre **pequeño frente a un paisaje enorme**.

**Paleta**: una pareja cálida y fría de §4, **sin negro**. Las sombras llevan tinte verde, vino o azul. Tres juegos listos:
- *sabana tóxica*: `#CCBC54`, `#C1E8B3`, `#B27957`;
- *cartel Cosmos*: `#49C0A9`, `#3B7872`, `#85514C`;
- *atardecer vino*: `#630F31`, `#79273B`, `#2A0A1C`.

**Línea y sombreado**: sin contorno de tinta. Sombreado degradado, como pintado. Parece un 3D estilizado con brillo suave (*bloom*).

**Luz**: contraluz con sol bajo. Niebla de color y partículas en el aire. Dos luces, una cálida y otra fría.

**Encuadre**:
- plano muy abierto, con el horizonte bajo: el cielo ocupa más de la mitad;
- un planeta enorme en el cielo y naves cruzando en diagonal;
- para **explicar**, un primer plano del personaje un poco de lado, con la caja de diálogo abajo.

**Palabras que ayudan** (en inglés, que Firefly entiende mejor): *1970s science fiction paperback cover, Chris Foss spaceship, Moebius alien landscape, retro-futurism, hazy colored atmosphere, pastel toxic sky, giant ringed planet on the horizon, painterly 3D render, volumetric colored fog, soft bloom, tinted shadows, no black, astronaut with opaque visor and glowing backpack, tiny figure in vast landscape*.

**Palabras que lo estropean**: *anime, cel shading, black space background, starfield, grey spaceship, realistic NASA astronaut, visible face, photorealistic, gritty, grimdark, neon cyberpunk city, speech bubble, comic panel*.
- El nombre «No Man's Sky» puede bloquearse por ser una marca ⚠️: mejor describir el estilo sin nombrarlo.

**Qué imágenes usar como referencia**:
- **de estilo**: hoja 3, n.º 1, 3, 5 y 10; el [fondo oficial de Kuldar Leement](https://w.wallhaven.cc/full/2k/wallhaven-2kzwg9.jpg); el [artbook escaneado](https://archive.org/details/art-of-no-mans-sky-book-scan);
- **de pose**: hoja 3, n.º 7, 8 y 10, y hoja 2, n.º 59;
- **nunca** capturas de Game UI Database: su web lo prohíbe (§11).

**Vocabulario de expresión** (el equivalente a los ojos o las gotas de sudor del anime):
- aquí **no hay** ojos grandes, gotas de sudor, fondos de emoción ni *chibi*;
- la emoción se pide con **luz y lugar**:
  - calma: el visor reflejando el paisaje;
  - peligro: una tormenta, el rojo del Atlas;
  - misterio: la cueva de *Prisms*, casi negra con focos;
  - asombro: el planeta gigante al fondo.
- El único *chibi* oficial es la figura Youtooz del Gek (§23).

### Para una IA de texto

**La voz del juego**:
- frases **cortas, en presente**, sin exclamaciones de anime;
- **puntos suspensivos** cuando dudan;
- la estática «–kzzkt–» entre guiones, sólo en los Viajeros;
- el Viajero **no habla**: narra en primera persona lo que ve.

**Las opciones**: numeradas y cortas, en imperativo («[3] Practicar el idioma»).
- Lo bloqueado va en gris, con la condición entre paréntesis. **Ojo**: la regla 4 del dueño pide no usar paréntesis de relleno, así que como mucho **uno**, y que sea la broma del juego.

**Por personaje**:
- **Polo** llama «amigo» (*friend*), repite «oh, sí» y se corrige a media frase.
- **Nada** habla telegráfico, con preguntas cortas.
- **-null-** hace preguntas amargas.
- **Apollo** es seco y cínico.
- **El Atlas** habla a trozos, como una terminal (no hay frase textual suya en las partes ⚠️).

**Frases reales por emoción** (inglés original, leídas en capturas del juego o en sus fuentes) ✅:

| Emoción | Frase real | Quién |
|---|---|---|
| Alegre | «A whole galaxy for you, just for you. You must see it all.» | Polo |
| Alegre | «-{{ If so, you'll love the Rentocniijk Expanse! Our capital, Drogradur NO425, is throneworld to our thriving community of interdimensional anomalies. }}-» | Viajero Nogiga |
| Enfadado, amargo | «Why won't it speak to me? Why – kzzkkt – aren't I enough?» | -null- |
| Regañando | «You, friend, visit the worst places you can find. Stay alive. No good to me dead, are you?» | Polo |
| Explicando | «Red orbs. Dominant, hostile. Creators or their relics? Singularities are key.» | Nada |
| Explicando | «In case of gravity or pressure loss follow emergency procedures» | Cartel de un carguero |
| Narrando | «Construct Uahattrai, rebuilt and returned, turns to face me.» | El Viajero |
| Animando | «Always more to do, oh yes, but not just now, friend. Go, be free, see the stars.» | Polo |
| Animando | «…we are not alone. Even if I die, even if all that is left of me are these words, Nada will find me again in another universe.» | Polo, en otro universo |
| Triste | «The death of the Atlas will not begin in sixteen minutes. It began a long time ago.» | Artemis |
| Triste | «I was born to travel, to see these worlds, to catalogue them… The skies... they were mine.» | -null- |
| Miedo | «It is dying. The Atlas is dying... It cries out at me, afraid...» | El Viajero ante el Atlas |
| Duda | «Or perhaps it was nothing, a ghost in the machine...» | Apollo |
| Épico | «I've seen things you people wouldn't believe…» | Rutger Hauer, tráiler de 2015 |

- **No hay texto oficial en español latino** (§8). Para el servidor, **se traduce en español neutro** con esta misma voz. Ejemplo del redactor, no oficial: «Una galaxia entera para ti, sólo para ti. Tienes que verla toda.»
- **Vocabulario del juego** para los textos: *Units*, *Nanites*, *Exosuit*, *Multi-Tool*, *Freighter*, *Anomaly*, *Nexus*, *Portal*, glifos, *Sentinels*, Atlas y *Expedition* (§25). La traducción oficial de España no está en las partes ⚠️: para el servidor, pasarlos al español de forma literal («unidades», «Exotraje», «multiherramienta»).

## 18 · Estilo y técnica, y cómo replicarlo

**Cómo lo hace el estudio**:
- **Motor propio**, no Unreal ni Unity. Empezó como afición de Sean Murray ✅.
- **El terreno se hace con voxels**: capas de ruido marcan la forma, luego se convierten en polígonos y se texturizan ([charla del GDC «Continuous World Generation in No Man's Sky»](https://www.gdcvault.com/play/1024265/Continuous-World-Generation-in-No); [wiki de modding](https://nomsmodding.fandom.com/wiki/Terrain_Generation)) ✅.
- **Su filosofía**, en palabras de Murray a IGN: «cuando miro un planeta, no veo las montañas, veo las matemáticas» ✅. Lo pintado a mano es el arte conceptual previo (§1).
- **Los «filtros» del juego están en el Modo Foto** ([wiki](https://nomanssky.fandom.com/wiki/Photo_Mode)) ✅:
  - Vignette, Bloom, Fog Density y Cloud Level, cada uno de 0 a 100 %;
  - profundidad de campo: Off, Light, Full o Macro, con un campo de visión de 50° a 150°;
  - **filtros de color con nombre**: Default, Vintage, Collapse, Emral, Chrono, Vapour, Soft Pulse, Synth, Revisti, Mosaic, Frost, Aliora, Hyper, Xeno, Deepend, Simulation, Pikisi, Unsleep, Haze, Phono, Scream, Oil Rain, Inverse, Lattice y Shimmer.
- **Aberración cromática y viñeteado**: el juego los trae puestos, se pueden apagar y desaparecen en el Modo Foto (un mod de Nexus y varios hilos de Steam) ✅.
- **Medido**: «sombreado degradado, línea normal», nunca plano ✅.

**Cómo reproducirlo en Blender** ⚠️ (receta a partir de lo medido; no es la técnica del estudio):
- **Terreno**: materiales de nodos. Noise o Voronoi Texture con un Color Ramp de 2-3 colores de §4, igual que el juego apila ruido.
- **Aire**: Volume Scatter **con tinte de color**, nunca gris. Niebla densa cerca del horizonte.
- **Luz**: dos soles de color opuesto, uno cálido y otro frío, y un planeta grande de fondo como luz de relleno.
- **Contorno**: **no uses Freestyle ni Line Art negro**. Si hay que separar la silueta, usa un Solidify muy fino con el color de la superficie o una luz de borde de color.
- **Compositor**: Glare (tipo Fog Glow) suave, y como mucho una aberración cromática leve.
- **Modelos**: los de Sketchfab de §3 se importan en `.glb` o `.fbx`.
- Tutoriales de partida, que no son de NMS: [Toon Style Planets](https://ryankingart.gumroad.com/l/toon-planets) y [Stylised Sky shader](https://www.blendernation.com/2021/06/21/stylised-sky-shader/).

**Cómo reproducirlo en Photoshop**:
- **Base**: *matte painting* con formas planas de color y degradados suaves, como una portada de Chris Foss.
- **Sombras**: un **Mapa de degradado** de 2-3 colores saturados sobre la capa de sombras, para que ninguna quede negra.
- **Metal**: las texturas CC0 de §4 en modo **Superponer**, al 15-30 %.
- **Encima de todo**: una capa de niebla de color con máscara de degradado desde el horizonte.

**Encuadres y composición** (vistos en las 6 capturas oficiales de Steam y en las hojas) ✅:
- **Asombro**: plano general enorme, figura pequeña y horizonte bajo.
- **Viaje**: naves en diagonal y un planeta gigante en el cielo.
- **Diálogo**: primer plano de medio cuerpo, ligero contrapicado y la caja abajo (Polo, Nogiga, -null-).
- **Tensión**: primera persona con el arma al frente (hoja 3, n.º 9).
- **Misterio**: casi negro con un solo foco de color (hoja 3, n.º 7 y 14).

## 19 · Texturas 2D

- **El alfabeto alienígena**:
  - [tabla completa](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/4/49/Alphabet.png), 1847×831 ✅;
  - aplicado en el [casco de un carguero](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/4/4a/Freighter_writing.jpg) ✅;
  - la fuente libre está en §5, **sin tildes**.
- **El logo**: letras con una estrella de rayas sobre la «S» ([SVG en Wikimedia](https://commons.wikimedia.org/wiki/File:No_Man%E2%80%99s_Sky_%E2%80%93_Text_logo.svg)) ⚠️. Es marca registrada: sirve para imitar el estilo, no para pegarlo.
- **La trama de hexágonos** de la caja de diálogo (vista por el redactor, §6) ✅. Se hace en Photoshop con un patrón hexagonal al 5-10 % sobre el azul.
- **Los parches de Expedición** ([índice](https://nomanssky.fandom.com/wiki/Expedition_Patches)) ✅: insignias como de tela cosida, cada una con su forma.
  - Uno es [Milestone 5](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/0/08/PATCH.MILESTONE.5.png): óvalo azul noche con estrellas verde lima `#BECF7A` y una nave rosa.
  - Otro es [Spooky Stage 3](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/3/31/PATCH.SPOOKY.STAGE.3.png): triángulo verde con gusanos naranja `#C84924` y borde crema `#E7E4DC`.
- **Iconos planos de naves**, sacados de las diapositivas de una charla de Hello Games: caza, carguero, explorador y transbordador (hoja 2, n.º 63) ✅.
- **Las etiquetas de elementos** del inventario de 2016: C, Si, S y Pu en cuadros de color (§11) ✅.
- **Las texturas de metal** CC0 de ambientCG están en §4 ✅.
- **Tramas de manga y pincelada**: no aplican ⚠️. El juego es 3D y su terreno no está pintado a mano. Tampoco hay un pack de texturas oficial.

## 20 · Gustos y detalles

Fichas oficiales o *databooks* de personajes no hay ⚠️: todo sale de la wiki.

| Quién | Lo que ama | Lo que odia o teme | Objeto que lleva | Cómo se ve a sí mismo |
|---|---|---|---|---|
| El Viajero | Explorar | — | Multiherramienta (Waveform Focuser N56-P) y Exotraje | — (no habla) |
| Nada | Buscar la verdad del Atlas | La Convergencia, que quiere borrarla | La capa con el símbolo del Atlas | Cada vez más paranoica |
| Polo | Aprender, los datos, la curiosidad | Que el Viajero muera: «Can't learn much from a corpse» | Una tablet cian | Un exiliado castigado |
| Apollo | Las unidades, el dinero | La sentimentalidad | — | Una máquina de negociar |
| -null- | Catalogar y nombrar cada criatura y cada planeta | Que el Atlas no le hable | — | Alguien que hizo lo correcto, en vano |
| Gek | El dinero y el comercio | — | El GekNip, un aditivo de la planta NipNip que cambia el humor con el olor | Mercaderes |
| Korvax | El saber y la aprobación del Atlas | — | La tablet táctil | Parte de la Convergencia |
| Vy'keen | El combate y el honor | Al Atlas, un dios falso | — | Guerreros del Alto Mando |

- **La altura de los Vy'keen**, «6 pies 5 pulgadas» (1,96 m), la marca la propia wiki con «cita necesaria» ⚠️. No se da por segura.
- **Cumpleaños, comida favorita y alturas**: no existen para estos personajes ⚠️ (buscado en la wiki).

## 21 · Por qué la aman

- **«La mayor remontada de la historia de los videojuegos»**, como titula [Pocket Tactics](https://www.pockettactics.com/no-mans-sky/review). [TouchArcade](https://toucharcade.com/2024/07/29/no-mans-sky-2024-review/) lo llama «uno de los mejores juegos que se pueden jugar en 2024» ✅.
- **Steam**: pasó a **«Muy positiva»** en 2024, tras tres años en «Mayormente positiva» ([reseñas](https://steamcommunity.com/app/275850/reviews/)) ⚠️. Lo cuenta TweakTown, que no se pudo leer entero (403).
- **Premios**: Mejor Juego en Curso en The Game Awards 2020 y 2025 ✅. La campaña de cada año por el «Labour of Love» de Steam (§12) ✅.
- **Con sus palabras** ✅:
  - «Why I Love No Man's Sky. Thank you Hello Games for a lovely game» (107 votos, [hilo](https://www.reddit.com/r/NoMansSkyTheGame/comments/1gu06lk/why_i_love_no_mans_sky_thank_you_hello_games_for/));
  - «man I love exploring new planets» (333 votos).
- **Con qué se identifica el público**: con la mezcla de asombro y soledad, más que con un personaje. «Captures both the breathtaking beauty and the haunting loneliness of deep space» (TouchArcade) ✅. Y con la sensación de «me quedé y valió la pena», que se repite en las reseñas ✅.

**Las escenas que duelen** (no tienen minuto de vídeo: son capturas de la wiki) ⚠️:
- **La ruta de Artemis** («Alone Amidst the Stars», «A Leap in the Dark», «The First Traveller»):
  - **Qué pasa**: hablas por radio con alguien que ya está muerto. Al final decides si subes su mente a una simulación o la dejas descansar.
  - **Por qué duele**: porque la ayudaste creyendo que podías salvarla.
  - **Cómo se ve**: la caja azul sobre la consola roja de la nave, con «The death of the Atlas will not begin in sixteen minutes. It began a long time ago.» ([captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/0/0e/Art-PL.jpg)).
- **El Atlas muriendo**: una sala oscura con la esfera y la única opción «Comfort the Atlas» ([captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/8/88/Atlas-PL.jpg)).
- **El mensaje de Polo desde otro universo**: «Nada will find me again in another universe» ([captura](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/e/e4/Backstory-PL.jpg)).
- **Lo que no encontré**: la música de esas escenas (se genera en directo, §9) ni comentarios de Reddit con muchos votos que digan «lloré». El buscador de Arctic Shift no devuelve nada con palabras sueltas ⚠️.

**Las que hacen reír o gritar**: las tormentas (3064 votos), la barra de vida sobre la cabeza «wait why is there a health bar above my head» (333 votos) y la pelea de escuadrones (794 votos) ✅.

## 22 · Fan dubs y comunidad hispana

- **No hay fandubs del juego**, y se buscó: «No Man's Sky fandub español», «fandub latino», el tráiler de Rutger Hauer con «lágrimas en la lluvia» y Dailymotion ✅. La razón: casi no hay diálogo hablado que redoblar (§8).
- **Lo que sí hace la comunidad hispana**:
  - **Series de *gameplay* comentado** por temporadas, como «NO MAN'S SKY 2022 GAMEPLAY ESPAÑOL T2 #7 · COMUNICACIÓN CON ARTEMIS» ([YouTube](https://www.youtube.com/watch?v=yvb-G382E2s)) ⚠️: no se pudo abrir.
  - **Análisis de la remontada**: «De ESTAFA a OBRA MAESTRA» (§10) ⚠️.
  - **Podcasts en español en Internet Archive**, del recolector y sin escuchar ⚠️: [«Podcast #42: Crónicas del algoritmo procedural»](https://archive.org/details/Podcast42_201608) y [«La Casa De Mi Hermano 4x01»](https://archive.org/details/LaCasaDeMiHermano4x01NoMansSkyEliteDangerousUnSenorDeNoruega....YMas).
  - **La prensa de España**: Vandal, Meristation, Vidaextra y HobbyConsolas suben los tráileres a Dailymotion (§10).
- **Dato para un servidor de doblaje**: la comunidad hispana juega en inglés o en español de España, nunca en latino. **Hacer el primer fandub latino** del tráiler de Rutger Hauer o de la ruta de Artemis sería algo nuevo (propuesta del redactor, para un evento).

## 23 · Colaboraciones, figuras y cosplay

- **Mass Effect** (7-nov-2024): vuelve la **Normandy SR1** en una Expedición de dos semanas; al terminarla, te quedas la nave ([blog oficial](https://www.nomanssky.com/2024/11/cross-save-ps5-pro-normandy/), [Gematsu](https://www.gematsu.com/2024/11/no-mans-sky-cross-save-ps5-pro-support-and-mass-effect-collaboration-now-available)) ✅.
  - La [miniatura oficial](https://www.nomanssky.com/media/g2zdsn1b/No-Mans-Sky-Cross-Save-Trailer-Thumbnail.jpg) es de 1280×720.
- **Youtooz** (9-ago-2025, por el 9.º aniversario): figuras y peluches oficiales. La primera es un **Gek** ([Happy Gamer](https://happygamer.com/no-mans-sky-fans-go-wild-over-new-youtooz-merch-drop-128147/), [tienda](https://youtooz.com/collections/no-mans-sky)) ✅. Es la figura oficial que sirve de referencia 3D, y también el único «*chibi*». Se celebró en el [blog](https://www.nomanssky.com/2025/08/celebrating-our-ninth-anniversary/).
- **Palworld**: sólo un **coqueteo público** entre Sean Murray y John Buckley en X durante 2025 ([PC Gamer](https://www.pcgamer.com/games/survival-crafting/palworld-and-no-mans-sky-are-intensifying-their-months-long-flirtation-and-if-those-two-dont-just-kiss-already-im-going-to-lose-my-mind/), [GamesRadar+](https://www.gamesradar.com/games/survival/palworld-would-collab-with-ark-no-mans-sky-and-enshrouded-tomorrow-if-we-could-make-it-make-sense-says-publishing-chief/)) ⚠️. **No existe todavía**: no dibujarla.
- **Tienda oficial** del estudio ([merch](https://www.nomanssky.com/merch/)) ✅.
- **Ropa con licencia** de Insert Coin ([tienda](https://www.insertcoinclothing.com/no-mans-sky/)) ⚠️: una fuente.
- **Ediciones físicas**: la caja de la *Explorer's Edition* y una lámina oficial enmarcada, en fotos CC BY 2.0 de blakespot (§3) ✅.
- **Cosplay bien hecho**: no encontré ninguno ⚠️. Se buscó en inglés en DeviantArt, Instagram y Reddit. Como el Viajero no tiene cara ni cuerpo fijos, no hay un disfraz «reconocible».
- **Cafés temáticos o eventos físicos**: no hay ⚠️ (buscado). Es un estudio pequeño, sin ese tipo de marketing.

## 24 · Obras parecidas y láminas vecinas

- **Los juegos que reconoce Sean Murray**: *Elite* (1984), *Star Control II* y *Freelancer*, todos procedurales. «Es casi como si hubiéramos vuelto a esos juegos» ([Inverse](https://www.inverse.com/article/7327-the-movies-books-and-video-games-that-influenced-no-man-s-sky), Wikipedia) ✅.
- **Los libros**: Asimov, Arthur C. Clarke y Heinlein. Sus historias le parecen «vibrantes, emocionantes, lo no explorado» ✅.
- **El arte**: Chris Foss, Mœbius, Ralph McQuarrie, John Harris y Ray Harryhausen (§1) ✅.
- **El cine**: *Blade Runner*, por el tráiler de Rutger Hauer (§8) ✅, y *Sunshine*, por el casco «Kappa» (§12) ⚠️.
- **Con qué lo compara la prensa** (tres artículos coinciden) ✅:
  - *Elite Dangerous*: sin bajar a pie a los planetas;
  - *Star Citizen*: escala parecida, todavía en desarrollo;
  - *Outer Wilds*: más de historia y puzles;
  - *Subnautica*: mapa hecho a mano;
  - *Spore*: comparación floja.
- **Del mismo estudio**: *Light No Fire*, de fantasía, que comparte tecnología desde *Worlds* ✅.
- **Láminas del servidor que se le parecen**: ninguna es de exploración espacial procedural ✅. Lo más cercano es **127-honkai-star-rail** (espacio, pero estilo anime de gacha) y **65-the-legend-of-zelda** (mundo abierto, pero fantasía). Ninguna usa la paleta de portada *pulp* sin negro. Si Honkai coge el tema «espacio», NMS se distingue por el paisaje enorme y la caja azul translúcida.

## 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo en cinco líneas** ✅:
1. El universo se genera con matemáticas: **18 trillones de planetas** (18×10¹⁸), todos distintos.
2. Para sobrevivir, se minan recursos (carbono, silicio, ferrita…). Con ellos se recargan el Exotraje, la nave y la multiherramienta, o mueres de frío, calor, radiación o falta de aire.
3. Hay tres especies con cultura propia: **Gek** (comerciantes), **Korvax** (máquinas que adoran al Atlas) y **Vy'keen** (guerreros). Desde *Echoes* se suman los **Autophage**.
4. Los **Viajeros** (Nada, Polo, Artemis, Apollo, -null-) no son otra especie: son identidades simuladas dentro del **Atlas**, el ordenador que crea el universo.
5. Los **Centinelas** vigilan cada planeta como jardineros armados: atacan si dañas el ecosistema o minas lo prohibido.

**La historia por arcos**: son las actualizaciones gratis, que hacen de «capítulos» ([registro oficial](https://www.nomanssky.com/release-log/) y Wikipedia) ✅.
- **2016**: lanzamiento (12-ago) y *Foundation* (28-nov), las primeras bases.
- **2017**: *Pathfinder* (8-mar), con vehículos y Modo Foto. *Atlas Rises* (11-ago) reescribe la historia y trae a Artemis.
- **2018**: *NEXT* (jul), con multijugador real, tercera persona y un gran cambio visual. Aquí cambia la letra de la interfaz.
- **2019**: *Beyond* (ago), con realidad virtual. La Anomalía se vuelve el punto de encuentro.
- **2020**: *Origins* (sep): montañas hasta 4 veces más grandes, gusanos de arena y sistemas de dos y tres soles.
- **2021**: *Frontiers* (1-sep, 5.º aniversario): pueblos donde el jugador puede ser *Overseer* ([PlayStation Blog](https://blog.playstation.com/) y [Xbox Wire](https://news.xbox.com/) lo anunciaron a la vez).
- **2022 en adelante**: *Sentinel*, *Desolation*, *Interceptor*, *Singularity*, *Fractal*, *Orbital*, *Adrift*, *Echoes* (con los Autophage), *Omega* y *Worlds* (Part I y II).
- **2026**: el 10.º aniversario y *Cosmos* (§10).

**El hilo principal, la ruta de Artemis** ✅:
- Te estrellas y encuentras una baliza con la identidad de Artemis.
- Con un Signal Booster la localizas, y descubres que su sitio no existe.
- Artemis pasa la identidad de Apollo antes de desaparecer («Alone Amidst the Stars»).
- Encuentras su tumba («A Leap in the Dark»).
- -null- te da el plano del **Mind Arc** para guardar su alma en el Holo-Terminus («The First Traveller»).

**Emblemas y objetos icónicos** ✅:
- **El símbolo del Atlas**: una **esfera roja facetada** dentro de un **rombo de neón rojo**, en una sala oscura ([captura](https://nomanssky.fandom.com/wiki/File:NMSAtlasInterface.jpg); hoja 3, n.º 14; y [NMSAtlas](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/8/8e/NMSAtlas.jpg), hoja 1, n.º 11). Sale en el cartel de *Cosmos*.
- **Los parches de Expedición** (§19).
- **El portal**, con su dirección de 12 glifos.
- **La multiherramienta**, el Exotraje y la nave.

**Vocabulario que un fan reconoce al instante** ✅:
- **dinero**: *Units* (la moneda, símbolo «U») y *Nanites*;
- **viaje**: *Warp Cell* / *Hyperdrive*, *Portal*;
- **el equipo**: *Exosuit*, *Multi-Tool*, *Starship*, *Freighter*;
- **sitios**: *Anomaly*, *Nexus*;
- **la historia**: *Signal Booster*, *Distress Beacon*, *Knowledge Stone*, *Sentinel*, *Atlas*.

## Hojas de contacto

Las tres están en `hojas/`, todas en JPEG de menos de 1 MB. Las **miró el redactor**. Los originales de la wiki están enlazados en `referencias.json` y en esta biblia.

**Hoja 1 · `naves_interfaz_01.jpg`** (n.º 1-48, imágenes de la wiki con su tamaño):
- **Exotraje e inventario**: n.º 1 (traje y nave de serie, 3840×2160), n.º 2-5 y 30-32 (inventario *NEXT*).
- **Multiherramientas**: n.º 5, 6 y 31.
- **Retratos**: n.º 8 y 20 (cabezas de Viajero), n.º 25 (**capa de Nada**), n.º 26-28 (**Polo** con su tablet y su caja de diálogo), n.º 29 (Viajero en el carguero).
- **Historia**: n.º 11 (el Atlas), n.º 21-23 (**cajas de diálogo** de Artemis, del Atlas y de Polo en otro universo).
- **Paisajes**: n.º 12-15 (los cuatro medidos en §4).
- **Cabinas**: n.º 16, 37, 38, 40, 42-44 y 47.
- **Naves**: n.º 17-19, 33-36, 39, 41, 45 y 48.

**Hoja 2 · `personajes_naves_02.jpg`** (n.º 49-70):
- **Diálogos de 2016**: n.º 52-54 (Polo), n.º 60-61 (Nada).
- **Retratos**: n.º 57 (Nada), n.º 58 (Polo), n.º 59 (**dos Viajeros hablando**), n.º 62 (Nogiga), n.º 70 (Artemis de frente).
- **Interfaz**: n.º 55 (ficha de tecnología), n.º 68 (indicador del arma).
- **Iconos de naves**: n.º 63.
- **Multiherramienta estándar**: n.º 56.
- **Nave sobre el agua**: n.º 69.

**Hoja 3 · `escenas_dialogo_03.jpg`** (n.º 1-20, fotogramas de tráiler con su minuto y capturas clave):
- **Paisajes de color**: n.º 1-5 (el encargo pide planetas de colores: aquí están).
- **Poses del Viajero**: n.º 7-10. El n.º 10 es el **cartel de *Cosmos***, la mejor pose de grupo.
- **Las dos cajas de diálogo**: n.º 11 (azul, con nombre) y n.º 13 (narración con opciones [1]-[4]).
- **Sitios y símbolos**: n.º 14 (Atlas), n.º 15 (mapa), n.º 16 (hologramas), n.º 17 (inventario de 2016), n.º 18 (menú rápido), n.º 19 (**parches de Expedición**), n.º 20 (pasillo del carguero).

## Correcciones del redactor

- **texto.md dice que la narración es «en tercera persona»**: es en **primera persona**. «*…turns to face me*» y «*I find myself…*» los dice el Viajero, que describe al otro.
- **texto.md dice que «no hay onomatopeyas de texto»**: **sí hay una**. La estática de radio se escribe dentro de la frase, «kzzkt» y «kzzkkt» (capturas de Artemis y de -null-).
- **texto.md pone a los Autophage en *Desolation* (2022)**: vídeo y voz los ponen en ***Echoes* (2023)**, y el tráiler de *Echoes* abre con ellos. Se queda *Echoes*.
- **La caja `#2E2B29` no es «el» color**: la caja es translúcida. Sobre fondo claro mide `#193D5D`, sobre dorado `#1C3A57` y sobre rojo `#222E3C` (medido por el redactor). Para la lámina conviene un azul `#1C3A57` al 80-85 % de opacidad.
- **§0 citaba `#153457`** para la caja de los Viajeros NPC. Medido ahora, va de `#123556` a `#204565`: cuadra.
- **video.md habla de un «casco dorado»** en el cartel de *Cosmos*: el traje es **blanco y rojo** y lo dorado es la **visera** (visto en la hoja 3, n.º 10).
- **En `referencias.json`, Polo figuraba como Korvax**: es **Gek** (corregido).
- **§0 decía «Switch y PS VR»**: no está en las partes. Queda la realidad virtual de *Beyond*, y Switch lleva ⚠️.

## 3 conceptos de lámina

El encargo no trae canal. Propongo tres, todos de `servidor/inventario.md`. Es sólo una idea: las biblias son generales. Si otra serie pide el mismo canal, no pasa nada.

### A · «El portal de la sabana» → **#a-que-juegas** (recomendada)
Texto del canal: «Lo que estás jugando, capturas y quién se apunta a una partida.»

- **Objeto y sitio**: un **Portal** de glifos, el anillo de piedra que lleva a otros mundos, en la **sabana tóxica** del E3 2015.
  - El sitio sale de la hoja 3, n.º 3 y 4 ([3:40](https://www.dailymotion.com/video/x89lilx?t=220) y [4:00](https://www.dailymotion.com/video/x89lilx?t=240)).
  - En Blender: el [modelo del Portal](https://sketchfab.com/3d-models/none-c30efda62567455d9f0644f55abc06f7) (locopixel, CC BY-NC, con crédito) sobre un terreno de nodos Noise y Color Ramp (`#CCBC54`, `#B27957`).
  - Niebla de Volume Scatter en `#C1E8B3`.
- **Personaje**: **el Viajero**, en la pose de *Cosmos* ([1:52](https://archive.org/details/youtube--sK7EGiJSDk?t=112); hoja 3, n.º 10), con sus dos compañeros. Los compañeros son «quién se apunta».
  - Se recorta con `v3/integrar.py` y se le da la luz rasante de la sabana.
- **Cómo habla**: la **narración del Viajero** (§6 B), con Roboto blanco sobre azul translúcido `#1C3A57`. Sobre el dorado de la sabana, el azul se verá como en el juego.
  - Arriba, el filete punteado.
  - Narración: «El portal se enciende. Al otro lado alguien busca con quién jugar.»
  - Opciones numeradas, en cuadritos como teclas:
    - «[1] Contar a qué juegas»
    - «[2] Subir tus capturas»
    - «[3] Buscar quién se apunta»
    - «[4] Seguir explorando»
- **Dónde va cada texto**:
  - el nombre del canal, arriba a la izquierda, en Jost mayúsculas con aire entre letras, como el logo;
  - en el anillo del portal, los glifos dicen «JUEGA» con la fuente NMS Alphabet, sin tildes y sólo de adorno;
  - la caja de narración, abajo a la izquierda;
  - las opciones, a la derecha.
- **Para que no quede plano**:
  - delante, hierba alta amarilla y un árbol rojo desenfocado (hoja 3, n.º 4);
  - entre los planos, niebla verdosa;
  - el portal brilla y da luz de rebote al traje;
  - arriba, una nave en diagonal y un planeta gigante en el cielo.

### B · «El Nexo de la Anomalía» → **#proyectos** (foro)
Texto del canal: «Un hilo por proyecto: equipo, avance, entregas.»

- **Objeto y sitio**: la **terminal del Nexo**, el tablón de misiones en grupo, en la **Anomalía Espacial** (§16). Es una consola con tarjetas de holograma, una por proyecto.
  - En Blender: planos emisivos cian `#3D8DB3` y `#8AC5D0` con línea `#F2F4F3` sobre `#0A1110`, como los hologramas del Overseer (hoja 3, n.º 16).
  - El texto va en los hologramas y la luz cae sobre la consola.
- **Personaje**: **Polo**, el Gek «adorable» y el que explica, de pie con su tablet cian ([Polo-PL](https://static.wikia.nocookie.net/nomanssky_gamepedia/images/8/81/Polo-PL.jpg); hoja 1, n.º 26).
  - Al fondo, **Nada** con su capa (hoja 1, n.º 25). Son la pareja de la Anomalía.
- **Cómo habla**: la **caja azul actual** (§6 A), con la pestaña «Especialista Polo» y el texto centrado en Roboto.
  - Primera caja: «Un hilo por proyecto, amigo. Oh, sí.»
  - Tras la flecha ⌄: «Cuenta quién está, cómo va y qué entregas.»
  - Opciones a la derecha, con la rayita blanca: «Abrir un hilo», «Ver las etiquetas», «Adiós».
- **Dónde va cada texto**:
  - el nombre del canal, arriba, sobre el arco de luces de la estación;
  - en el tablón, tres tarjetas de ejemplo: «Equipo», «Avance» y «Entregas»;
  - la caja de Polo, abajo en el centro.
- **Lámina 2 (las 10 etiquetas)**: el tablón del Nexo en grande.
  - El avance va como una ruta de misión: Buscando gente → En traducción → En grabación → En edición → En revisión → Estrenado.
  - «En pausa» y «Cancelado» van en gris, como las opciones bloqueadas.
  - «Oficial del servidor» y «De la comunidad» van como el trato de 2016 («Current Gek standing»): «Origen: oficial del servidor».
- **Para que no quede plano**:
  - la tablet de Polo, delante, le tiñe la cara de cian;
  - los hologramas son semitransparentes y quedan por delante de Nada;
  - al fondo, las luces de la estación desenfocadas.

### C · «El parche de la Expedición» → **#eventos**
Texto del canal: «Lo que se viene. Se convoca con /create y cada uno lo ve en su hora.»

- **Objeto y sitio**: un **parche de Expedición de tela cosida**, como los de §19, clavado en una caja del **hangar del carguero** (hoja 1, n.º 29, luces azules). Por la compuerta abierta se ve el planeta rojo sobre el espacio verde azulado de *Cosmos* (`#49C0A9`, `#3B7872`, `#85514C`).
  - En Blender: un plano con el relieve del bordado, el borde de puntada crema `#E7E4DC` y la textura del hilo.
  - Es el tipo de objeto que le gustó al dueño: la luz del hangar marca las puntadas.
- **Personaje**: **el Viajero con visera dorada y sus dos compañeros**, en la pose de *Cosmos* para **celebrar** (hoja 3, n.º 10), a media distancia.
  - La otra opción es el Viajero solo en el pasillo, hacia la cámara, como bienvenida (pose 7).
- **Cómo habla**: la **narración del Viajero** (§6 B), con opciones numeradas.
  - Narración: «Llega una Expedición. Cada uno la vive a su hora.»
  - Opciones:
    - «[1] Ver lo que se viene»
    - «[2] Convocar con /create»
    - «[3] Mirarlo en tu hora»
  - `/create` va en la opción [2], con el número en su cuadrito como una tecla.
- **Dónde va cada texto**:
  - «EVENTOS», bordado en el parche, grande y en primer plano;
  - un reloj pequeño arriba a la derecha, como el nombre y la temperatura del menú rápido («19.0°C» → «Tu hora»);
  - la caja, abajo.
- **Para que no quede plano**:
  - el parche va delante, con relieve y algo desenfocado;
  - la luz de la compuerta entra en rayos volumétricos de color;
  - las naves cruzan fuera, en diagonal.
- **⚠️ No documentado**: cómo es en pantalla la cuenta atrás de las Expediciones. Si hace falta, se mira antes de hacer la lámina.

## Cumplimiento del encargo

| Punto | Qué pide | Estado | Por qué |
|---|---|---|---|
| 1 | Arte oficial variado | ✅ | Artbook escaneado entero, blog oficial, cartel de *Cosmos*, fondo oficial y poses vivas numeradas en las hojas. Falta el artista de cada *key art* |
| 2 | Fotogramas con minuto | ✅ | 12 fotogramas de 5 tráileres, con minuto y enlace `t=`. Las escenas de historia sólo tienen capturas de la wiki |
| 3 | Fan art y 3D con licencia | ✅ | 10 modelos de Sketchfab con licencia y crédito, 4 de ArtStation, DeviantArt, Reddit y fotos CC BY. No hay un *rig* libre del Viajero |
| 4 | Sitios, luz, paleta y texturas reales | ✅ | 12 paletas medidas con `estilo.py` y 5 texturas CC0 |
| 5 | Una letra por uso, con tildes | ✅ | Comprobadas con `fontTools`. La letra de glifos no tiene tildes (dicho). La del cómic no se vio |
| 6 | Cómo hablan en pantalla | ✅ | Tres cajas de diálogo vistas y medidas por el redactor. La caja es translúcida |
| 7 | Principales y secundarios, popularidad | ⚠️ | No hay encuesta oficial (buscada). Se usan un hilo de Reddit (131 votos) y los posts con más votos |
| 8 | Doblaje latino verificado | ⚠️ | **No existe**, comprobado en la API de Steam, en Doblaje Wiki por su API y en un hilo de Steam. ANMTV está bloqueado |
| 9 | Música, sonido y onomatopeyas | ⚠️ | Banda sonora, Pulse, VocAlien y «kzzkt» con dos fuentes. No se confirmó el tema de la escena más emotiva |
| 10 | Vídeos y tendencias con minuto | ✅ | 6 tráileres, 2 análisis con duración y vistas, tendencias de 2016 y de TikTok. No hay un reto viral propio |
| 11 | Videojuegos: interfaz, menús y cajas | ✅ | Un solo juego. Inventario, mapa, menú rápido, HUD, Modo Foto y Game UI Database |
| 12 | Lo que ama el fandom y qué NO hacer | ✅ | La remontada, los posts con más votos y una lista de 9 «no» |
| 13 | Personajes a fondo, cara por emoción | ⚠️ | 13 fichas con frases reales leídas en capturas. La cara por emoción **no existe**, comprobado por la API de la wiki |
| 14 | Poses en varias escenas | ⚠️ | 10 poses; 4 del Viajero con minuto. «Regañar» no existe (buscado). Nada y Polo tienen pocas poses |
| 15 | Vestuario con hex | ✅ | Exotraje, multiherramienta, capa de Nada y Artemis medidos. El traje de *Cosmos* y Polo, sin medir |
| 16 | Sitios y fondos de pantalla en alta | ✅ | La Anomalía y 13 fondos con tamaño, ♥ y autor, uno oficial |
| 17 | Guía para IA de imagen y de texto | ✅ | Rasgos, paleta, luz, encuadre, palabras que ayudan y que estropean, referencias, y 14 frases reales por emoción |
| 18 | Técnica y cómo replicarla | ✅ | Motor, voxels (GDC), Modo Foto con sus valores, y receta para Blender y Photoshop. La receta es del redactor, no del estudio |
| 19 | Texturas 2D | ✅ | Alfabeto, logo, trama hexagonal, parches con hex, iconos de naves y CC0. No hay tramas de manga (no aplica) |
| 20 | Gustos y detalles | ⚠️ | Tabla de 8 personajes sacada de la wiki. No hay *databooks*; cumpleaños y alturas no existen |
| 21 | Por qué la aman, escenas que duelen | ⚠️ | Reseñas, premios y Steam con dos fuentes. Las escenas de Artemis no tienen minuto de vídeo ni comentarios con votos |
| 22 | Fan dubs y comunidad hispana | ⚠️ | No hay fandubs (buscado). Series de *gameplay*, análisis y podcasts en español, sin abrir |
| 23 | Colaboraciones, figuras y cosplay | ⚠️ | Mass Effect, Youtooz y Palworld (sin confirmar). No se encontró cosplay bien hecho ni cafés temáticos |
| 24 | Obras parecidas y láminas vecinas | ✅ | Influencias con dos fuentes, comparativas de prensa y las biblias 127 y 65 |
| 25 | Mundo, historia y símbolos | ✅ | 5 reglas, arcos por año, la ruta de Artemis, el Atlas, los parches y el vocabulario |
| Conceptos | Los 3 conceptos de lámina | ✅ | Portal, Nexo y parche. Distintos entre sí, con objeto, personaje, caja, textos y profundidad. Hay lámina 2 para las etiquetas de #proyectos |
| Fuentes | 40 webs distintas | ✅ | 59 dominios enlazados en el texto |
| Tipos de fuente | Los de «Profundidad exigida» | ⚠️ | Hay oficiales, wikis, foros, arte, vídeo, código y doblaje. The Cutting Room Floor y Wayback están bloqueados por la red del contenedor. TV Tropes no se consultó. En japonés sólo una guía de Steam y Pixiv; coreano y chino no aplican (estudio británico) |
| Hojas | 3 hojas de contacto | ✅ | 3 JPEG de menos de 1 MB, miradas y descritas número a número |
| Referencias | `referencias.json` | ✅ | 120 referencias, con Polo corregido |

## Bitácora de búsqueda

**Del redactor (26-sep-2026)**:
- `juntar_referencias.py` dejó 120 referencias y `juntar_bitacora.py` juntó las bitácoras de los cuatro roles, que van debajo.
- Bajé de la wiki, con cabecera `Referer`, 11 capturas de diálogo: Polo ×3, Nada ×2, Artemis, el Atlas, Apollo, -null-, el mensaje de Polo desde otro universo y el Viajero Nogiga. Leí su texto con Read y medí sus cajas con `estilo.py`. De ahí salen las frases reales de §13 y §17 y los colores de §6.
- **Lo confirmado** lleva dos fuentes o está visto o medido (✅). **Lo dudoso** lleva ⚠️.
- **No encontré**: cómo es en pantalla la cuenta atrás de las Expediciones, frases textuales del Atlas y el tema musical de la escena más emotiva.
- No hice búsquedas web nuevas: la cuota compartida de la sesión estaba agotada (lo dice texto.md).

## Bitácora

### Bitácora de imagen

- `recolectar.py` (previo, no repetido): Fandom (8 páginas), Wallhaven, Sketchfab, Openverse → `datos-imagen.md`.
- `investigar_serie.py --serie "No Man's Sky" --wiki nomanssky --paginas Traveller "Priest Entity Nada" "Specialist Polo" Artemis "The Atlas" Multi-Tool Starship Exosuit`: falló primero con `--wiki nomanssky_gamepedia` (subdominio equivocado, error SSL); funcionó con `--wiki nomanssky` → 171 imágenes enlazadas, 70 grandes, 2 hojas de contacto en `herramientas/referencias/no-man-s-sky/` (miradas con Read, copiadas a `hojas/`).
- `herramientas/estilo.py` (paleta + estilo, con Pillow/numpy/opencv en local, no busca en la red): 9 imágenes — Exosuit/nave por defecto, Multiherramienta estándar, capa de Nada, traje de Artemis, 4 paisajes de planeta de la wiki, 1 fondo de pantalla oficial de Wallhaven.
- Web search (inglés): «No Man's Sky key art cover retro sci-fi pulp inspiration artist», «No Man's Sky box art 70s science fiction book cover style», «No Man's Sky cover art artist Malcolm Smith Innerspace retro poster design» (pista falsa), «No Man's Sky official merchandise collaboration figure Numskull Fangamer Youtooz», «No Man's Sky crossover collaboration PlayStation exclusive content event», «No Man's Sky Palworld collaboration 2025 official confirmed launched», «No Man's Sky alien language font Korvax Gek Vy'keen glyphs symbol alphabet», «No Man's Sky official wallpapers download nomanssky.com media», «Grant Duncan No Man's Sky art director Chris Foss interview influence», «No Man's Sky fan art ArtStation traveler exosuit illustration», «No Man's Sky logo meaning starburst symbol design», «Art of No Man's Sky official artbook book print», «No Man's Sky cosplay exosuit official recognition photo».
- Web search (japonés): «No Man's Sky pixiv イラスト ファンアート» → presencia escasa en Pixiv, confirmado.
- Páginas leídas directamente (curl, filtrando con Python/regex, nunca la respuesta entera): nomanssky.com (blog del arte, crossover con Mass Effect, aniversario, tienda), Wikipedia API (`Development of No Man's Sky`, extracto), GamesBeat (entrevista a Grant Duncan), Push Square (portadas retro de fans), Gematsu (crossover Mass Effect), Insert Coin Clothing, thevideogamelibrary.org (ficha del artbook), archive.org (metadata del escaneo del artbook), Youtooz (tienda oficial).
- Fandom API (`api.php`, sin bloqueo): `Traveller`, `Exosuit`, `Multi-Tool`, `Space Anomaly`, `Language`, `Alphabet` (extractos de texto) + `imageinfo` de `Alphabet.png` y `Freighter writing.jpg`.
- Sketchfab API (`v3/search`, `q=No Man's Sky`, `downloadable=true`): 8 modelos con licencia, autor y miniatura confirmados.
- ambientCG API (`full_json`, ojo: sólo acepta una palabra en `q`, no frases): `metal`, `rust`, `panel`, `paper`, `fabric` → 3 texturas CC0 elegidas (Corrugated Steel 009, Metal 063, Solar Panel 003).
- Bloqueados: time.com (403 a curl), highdefdigest.com (403, Cloudflare), tweaktown.com (403); `navegar.py` no pudo abrir ninguno (falta el ejecutable de Chromium en este contenedor: «BrowserType.launch: Executable doesn't exist»). No insistí más de dos intentos en cada uno, según la regla.

### Bitácora de video

- Miré con `fotogramas.py`: tráiler de anuncio (archive.org, mirror de YouTube aCgWabJssVI), tráiler E3 2015 (Dailymotion x89lilx), tráiler «Echoes» (Dailymotion x8nggcs), tráiler «Prisms» (Dailymotion x89nujz) y tráiler del 10.º aniversario (archive.org, mirror de YouTube -sK7EGiJSDk). Todos los clips venían ya localizados en `datos-video.md` salvo el del 10.º aniversario, que busqué porque es el más reciente (ago-2026) y encaja con «planetas de colores» del encargo.
- Probé `fotogramas.py` directo contra YouTube dos veces (aCgWabJssVI y -sK7EGiJSDk): ambas dieron «Sign in to confirm you're not a bot» (bloqueo de este servidor). Plan B que funcionó: el mismo vídeo mirrorado en `archive.org/details/youtube-<id>`, tal y como indica AYUDANTE.md.
- Intenté `yt-dlp` para sacar metadatos (duración/vistas) de dos vídeos de análisis en YouTube: uno dio 429 en el primer intento y funcionó al repetir («The Redemption Of No Man's Sky», GameSpot); el otro («The Engoodening», Internet Historian) siguió bloqueado, así que usé IMDb + Lemmy.World para la duración.
- Medí color y estilo con `herramientas/estilo.py` sobre 10 fotogramas propios (no descargué arte de terceros para esto).
- Búsquedas web (inglés, ~10 de mi cupo de 50): «65daysofstatic No Man's Sky soundtrack interview», «Paul Weir procedural audio No Man's Sky interview», «No Man's Sky TikTok viral trend meme», «No Man's Sky redemption documentary Noclip», «The Engoodening video essay», «No Man's Sky TikTok millions views», «No Man's Sky 10th anniversary trailer 2026 update», «No Man's Sky launch controversy meme lying Sean Murray». No hice búsquedas en japonés/coreano: el estudio (Hello Games) es británico y la obra no viene de Asia, así que no aplica ese requisito de ENCARGO.md.
- Wiki de Fandom (`nomanssky.fandom.com`) por su API: wikitext de «Music for an Infinite Universe» (lista de pistas verificada) e imágenes ya recolectadas del Viajero (descargadas con cabecera `Referer` para poder mirarlas).
- ambientCG (`api/v2/full_json`): texturas de arena/tierra («Ground054») y roca («Rock061»), ambas CC0, para las «texturas reales equivalentes» del punto 4.
- No until usé `navegar.py`: no hizo falta, ninguna web relevante bloqueó curl directamente (TikTok y Dailymotion respondieron bien por API).

### Bitácora de voz

- Doblaje Wiki API (`doblaje.fandom.com/es/api.php`): 3 variantes de título +
  1 búsqueda de texto libre → sin página de la obra (español).
- Fandom `nomanssky.fandom.com/api.php`: wikitext de Nada→Priest Entity Nada,
  Polo→Specialist Polo, Gek, Korvax, Vy'keen, The Atlas, Sentinel, Artemis,
  Apollo, -null-, Telamon; `imageinfo` de 8 imágenes para medir tamaño real
  (inglés).
- WebSearch (inglés y español): doblaje/voces NMS, voice actor narrator
  credits, Paul Weir alien language, Rutger Hauer trailer, meme Sean Murray
  redemption arc, Steam Awards Labour of Love, review 2024/2025 comeback,
  fandub español, lágrimas en la lluvia homenaje, gameplay comentado latino.
- `behindthevoiceactors.com` vía `navegar.py` (Cloudflare bloquea curl
  directo) → ficha de reparto.
- Steam Store API `appdetails` (oficial) → tabla de idiomas.
- `navegar.py` sobre Steam Community (discusión doblaje) y Steam Store
  (tabla de idiomas) → funcionó bien, sin bloqueo.
- `herramientas/voz.py` sobre el tráiler de Rutger Hauer (mirror Dailymotion
  x443lhp) → transcripción + análisis de voz.
- Arctic Shift (Reddit, inglés): `posts/search` con `title=` (nota: el
  parámetro `sort` sólo acepta `asc`/`desc`, no `sort_type`; búsquedas de una
  sola palabra como «cry», «chills», «beautiful», «masterpiece» devuelven 0
  resultados aunque el hilo exista — el buscador de título parece exigir
  coincidencias más largas o exactas — mientras que frases de 2-3 palabras sí
  funcionan) y `comments/search` con `body=Artemis`.
- ANMTV bloqueado por política de proxy del contenedor (`connect_rejected`),
  probado por curl y por `navegar.py`.
- Wikipedia API: `Development of No Man's Sky` (extracto, confirma a Paul
  Weir y 65daysofstatic) funcionó; una segunda consulta a `No Man's Sky` dio
  «too many requests» (límite de tasa) y no reintenté para no gastar cupo.

### Bitácora de texto

- `datos-texto.md` (recolectado antes): sólo 6 capturas de Steam de interfaz 1920×1080 — miradas en contacto propio (`contacto_steam.jpg`), sin diálogo visible en ninguna (son capturas de marketing sin HUD).
- Leído primero `imagen.md` y `video.md` (ya escritos por los otros investigadores) para no repetir: el alfabeto alien, el logo, las 4 paletas de planeta y los modelos Sketchfab ya estaban ahí — aquí sólo se referencian, no se repiten.
- GitHub: `add_repo` + clon superficial de `NMSCD/No-Mans-Sky-Universal-Font` (con `GIT_LFS_SKIP_SMUDGE=1`) para bajar los 4 `.ttf` reales y comprobarlos con fontTools (`TTFont(f).getBestCmap()`, chequeo de á é í ó ú ñ Ñ ¿ ¡ ü) — los cuatro dieron `True` en todo.
- Google Fonts / Fontsource: `api.fontsource.org/v1/fonts?family=Jost` (licencia OFL, subsets latin+latin-ext) y descarga directa de `fonts.gstatic.com` para Jost y Roboto, comprobadas igual con fontTools.
- Fandom API (`nomanssky.fandom.com/api.php`, sin bloqueo): páginas `Language`, `Alphabet`, `NPC conversation` (obsoleta), `Automatic translation device`, `Adventures in No Man's Sky`, `Artemis`, `The Atlas`, `Sentinel`, `Expedition Patches`, `Inventory`, `Quick Menu`, `Overseer (NPC)`, `Discoveries` — texto (`prop=wikitext`) e imágenes (`prop=pageimages` / `allimages`).
- Imágenes propias miradas con Read (no sólo citadas): `dialogue.jpg` (cuadro de diálogo real, 2522×1138), `contacto_ui.jpg` (inventario 2016 + menú rápido), `overseer.jpg` (hologramas), `patches.jpg` (2 parches de expedición), `contacto_steam.jpg` (6 capturas oficiales de Steam) — todas medidas en hex con `herramientas/estilo.py`.
- Steam: `store.steampowered.com/api/appdetails?appids=275850` (lista completa de 189 capturas, sólo usadas las ya citadas).
- `python3 herramientas/navegar.py` (sin ventana, con Chromium): funcionó para `gameuidatabase.com` (pasó el reto de Cloudflare) pero **no** para `tcrf.net` (403 duro, no es el mismo tipo de verificación).
- `WebSearch` (11 búsquedas antes de agotarse la cuota compartida de la sesión, en inglés): fuente UI/HUD, fuente del logo, mecánica de diálogo alienígena, cómic "Adventures in No Man's Sky", lista de expediciones, cita "playable painting" (sin resultado), filtros de post-proceso, juegos parecidos, tutorial de Blender estilo NMS, fuente CJK, inspiración de Sean Murray en "Elite".
- Bloqueados: `tcrf.net` (403 Cloudflare, con y sin navegar.py) y `web.archive.org` (confirmado esta tanda como **bloqueo de política de egress del contenedor**, no de la fuente ni de Cloudflare: `curl` por `http://` devolvió el texto literal "Blocked by egress policy") — repetido en esta tanda de relanzo por las tres vías posibles, sin éxito; no se insiste más, es un límite de infraestructura, no de investigación.
- Verificación propia del repositorio: `ls biblias/` para comparar con otras láminas del servidor (punto 24), sin necesidad de fuente externa.
- **Segunda pasada (relanzo, 25-sep-2026)**: se cerraron los 4 huecos ⚠️ que quedaban como extra — (1) fuente real del alfabeto alien descargada del bundle JS de `alphabet.nmscd.com` (`raw.githubusercontent.com/NMSCD/Expedition-Alphabet/.../nms-alphabet.ttf`) y comprobada con fontTools (NO trae tildes/ñ/¿¡, dato ahora confirmado en vez de dudoso); (2) captura propia del Galactic Map (`nomanssky.fandom.com`, imagen oficial 1920×1080) mirada y medida con `estilo.py`; (3) segunda imagen oficial de una Atlas Interface (`NMSAtlasInterface.jpg`) mirada directamente para confirmar la forma del símbolo del Atlas, antes sólo descrita en texto; (4) TCRF/Wayback reintentado por 3 vías, confirmado bloqueo de política de red del contenedor (no de la fuente, no hace falta reintentar). `texto.json` pasó de 12 a 15 referencias.
