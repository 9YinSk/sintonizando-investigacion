---
tags: [biblia, serie, laminas, biblioteca]
serie: "Vinland Saga (ヴィンランド・サガ)"
canal: "sin canal: propuesta #proyectos (reservas: #textos lámina 2 y 🎭 Escenario, ver §0)"
fecha: 2026-09-24
---

# Biblia · Vinland Saga — para la biblioteca

> [!important] Cómo se hizo, y sus límites
> - La escribió el **redactor** con las cuatro partes del equipo
>   (`partes/imagen.md`, `video.md`, `voz.md`, `texto.md`) y los datos del
>   recolector (`partes/datos-*.md`, `datos.json`). Nada nuevo sin fuente.
>   Lo que el redactor miró en las 3 hojas de `hojas/` lo dice como
>   «visto en la hoja».
> - **YouTube no dejó bajar vídeo** (403 y «confirma que no eres un bot»).
>   El opening 1 y el tráiler de la temporada 2 se miraron enteros en
>   **Dailymotion a 1280×720**. El ending 1 y los clips de escenas, por
>   **storyboard de YouTube** (160×90, minuto ±2 s). AnimeThemes, caído
>   (HTTP 522) todo el día.
> - **Frases del doblaje latino**: salen de **3 clips oficiales doblados
>   (Netflix)** que sube la página «Vinland Saga Latinoamérica» en
>   Facebook, transcritos con `voz.py`. Doblaje Wiki no trae muestras de
>   audio para esta serie.
> - Hay **dos doblajes latinos** (Netflix y Crunchyroll). Cada frase dice
>   de cuál sale.
> - ✅ = dos fuentes o visto por el equipo. ⚠️ = una sola fuente,
>   storyboard, o minuto dentro de un clip recortado. Lo que no se
>   encontró está en §28 y en la tabla final.

## Índice

Entre corchetes, el punto de `ENCARGO.md` que cubre cada sección.

0. Vinland Saga no tiene canal: dónde encaja mejor
1. Resumen para quien tenga prisa
2. Las escenas que sirven, con minuto [2]
3. Arte oficial y hojas de contacto [1]
4. Fan art y 3D, sólo como referencia [3]
5. Sitios, luz, paleta y texturas reales [4]
6. Tipografía: una letra para cada uso [5]
7. Cómo hablan y piensan en pantalla: el cuadro de diálogo [6]
8. Los personajes: qué transmiten, su cara en cada emoción y sus dinámicas [7, 13]
9. ¿Quién es el más querido? [7]
10. Doblaje latino y frases textuales [8]
11. Música y sonido [9]
12. Vídeos y tendencias [10]
13. Videojuegos de la franquicia [11]
14. Lo que ama el fandom, y qué NO hacer [12]
15. Poses analizadas por personaje [14]
16. Vestuario, con hex medidos [15]
17. Paisajes y fondos de pantalla [16]
18. Guía para generar con IA: imagen y texto [17]
19. Estilo de dibujo, técnica, Blender y encuadres [18]
20. Texturas 2D [19]
21. Gustos y detalles de cada personaje [20]
22. Por qué la gente la ama, y las escenas que hacen llorar o gritar [21]
23. Fan dubs y comunidad hispana [22]
24. Colaboraciones, figuras y cosplay [23]
25. Obras parecidas y láminas vecinas [24]
26. El mundo, la historia por arcos y sus símbolos [25]
27. Tres conceptos de lámina
28. Lo que no pude verificar
- Cumplimiento del encargo
29. Bitácora de búsqueda

---

## 0 · Vinland Saga no tiene canal: dónde encaja mejor

La serie en una línea: un chico vikingo del siglo XI pasa de la venganza a
la paz, y su meta es fundar **Vinlandia**, «una tierra sin guerra ni
esclavos» ([wiki: Vinland](https://vinlandsaga.fandom.com/wiki/Vinland)).
Su tema es «**nadie tiene enemigos**». El tono es sombrío y crudo: nada de
colores alegres (regla 6 del dueño).

Casi todos los canales de texto ya tienen serie (mirado en `encargos/` y en
el `canal:` de cada biblia). Estos tres son los que mejor le van:

| Canal (de `servidor/inventario.md`) | Por qué encaja | Con quién choca |
|---|---|---|
| **ıı・📂・proyectos** (foro, EL ESTUDIO): «Un hilo por proyecto: equipo, avance, entregas.» Etiquetas: Buscando gente, En traducción, En grabación, En edición, En revisión, Estrenado, En pausa, Cancelado, Oficial del servidor, De la comunidad | **Vinlandia es un proyecto**: Thorfinn busca gente, lo financia con la expedición al este, cruza el mar y lo funda (§26). **Askeladd** dirige una banda que acepta encargos y planea campañas: hay un mapa del manga con «Askeladd's landing» (hoja `fondos_01.jpg` #4). Caben el protagonista y el más querido | **Arcane (encargo 17)** tiene «#proyectos y #arte». Dos salidas: Arcane se queda #arte y Vinland Saga #proyectos, o Vinland Saga hace la **lámina 2 de #proyectos** (las 10 etiquetas como ruta del viaje) |
| **ıı・📖・textos**, lámina 2 (foro de guiones; etiquetas Monólogo, Diálogo, Escena de anime, Comercial, Narración, Original, Libre para usar, Pide crédito, Para dos voces) | El hilo de ejemplo del foro es «**Monólogo — hombre adulto, 40 segundos, tono contenido**»: es Askeladd tal cual (voz grave, nunca grita; su monólogo de Artorius dura de 2:52 a 3:43 en el clip). Y Thors con Thorfinn niño es un diálogo «para dos voces» con clip doblado | **Death Note (encargo 18)** tiene #textos: sería su lámina 2 de etiquetas |
| **🎭・Escenario** (EN VIVO): «Charlas, entrevistas y directos. Sube quien invita el anfitrion.» | La saga contada en voz alta junto al fuego de la casa larga, con Askeladd de anfitrión que decide quién sube | Está dentro del **encargo 29** (seis canales sin serie y las salas de voz) |

**Propuesta: #proyectos.** El propio título (Vinland) es la meta de un
proyecto, hay objetos reales para contarlo (mapas, el tocón de la granja,
el barco) y caben Thorfinn y Askeladd. Los conceptos 1 y 2 de §27 son
para #proyectos; el 3, para #textos lámina 2.

> [!question] Para el dueño
> ¿#proyectos se lo queda Vinland Saga (y Arcane sólo #arte), o Vinland
> Saga hace la lámina 2 de #proyectos? Si no, la reserva es la lámina 2
> de #textos.

---

## 1 · Resumen para quien tenga prisa

- **Qué es**: manga de **Makoto Yukimura** (Kodansha, revista Afternoon),
  de abril de 2005 al **25 de julio de 2025** ✅
  ([wiki: Makoto Yukimura](https://vinlandsaga.fandom.com/wiki/Makoto_Yukimura)).
  Anime: temporada 1 de **WIT Studio** (2019, 24 episodios) y temporada 2
  de **MAPPA** (2023, 24 más; 48 en total), con el mismo director
  (Shūhei Yabuta) y el mismo diseñador (Takahiko Abiru) ✅.
- **Tono**: la crudeza vikinga y una paz que cuesta más que cualquier
  batalla. Islandia nevada, Inglaterra verde en guerra, la granja de
  esclavos, el mar de noche con aurora, y Vinlandia.
- **El más querido: Askeladd, el secundario.** Es el antagonista y a la
  vez mentor de Thorfinn.
  - Gana la encuesta de fans japonesa más reciente: rancolle 4.ª
    edición, **Askeladd 39 votos, Thorfinn 7** ⚠️ (pocos votos, una
    fuente) ([rancolle](https://rancolle.com/ranking/uid21_1739280400)).
  - TV Tropes lo pone como «**Ensemble Darkhorse**»: el secundario que se
    roba el cariño del público ✅
    ([TV Tropes YMMV](https://tvtropes.org/pmwiki/pmwiki.php/YMMV/VinlandSaga)).
  - Muere en el **episodio 24** (fin de la temporada 1) y aun así tiene
    **16 588 favoritos en AniList, el 74 % de los de Thorfinn**
    (22 329) ✅ ([AniList](https://anilist.co/anime/101348)).
  - Satoru Noda, autor de *Golden Kamuy*, dice que admira sobre todo a
    Askeladd ✅.
  - Thorfinn gana en AniList y en dibujos de fans (Danbooru 266 contra
    190), pero es «divisivo»: parte del fandom no aceptó su giro
    pacifista. Tercero: **Thorkell** (3744 favoritos).
  - **Por eso Askeladd protagoniza el concepto 1 de §27.**
- **Cuadro de diálogo propio**: en el anime **no hay globos**. Se habla
  con **subtítulo blanco sin caja** o con **cartela negra y letra serif
  blanca** (tráiler T2, 0:03 y 0:21). En el manga japonés, el número de
  capítulo va en una **cartela roja con texto blanco**. El manga en
  inglés usa globos ovalados blancos (§7), pero para la lámina toca
  **texto tallado o pintado en madera, cuero o pergamino**, como el
  mapa de Vinlandia del opening.
- **Letras libres** (todas con á é í ó ú ñ ¿ ¡, comprobado con fontTools):
  **Eater** (logo), **Pirata One** (runas), **Playfair Display**
  (cartelas), **MedievalSharp** (mapa), **Noto Sans** (subtítulos),
  **Anton** (grito).
- **Frase**: «**No tienes enemigos... Nadie tiene enemigos. Nadie en este
  mundo merece ser herido.**» (Thors, doblaje Netflix, ep. 2, clip 1:05).
  Y «**Un verdadero guerrero no necesita espada**» (Thors, capítulo 15).
- **Paleta medida**: noche con aurora `#131E35`→`#34BAC6`, nieve
  `#F1F1EA`/`#9DB1D0`, fuego y sombra `#241B0D`/`#694630`, trigal
  `#E8E74D`, caqui de Thorfinn granjero `#BAA16E`.
- **Doblaje latino, dos versiones**: Netflix (Audiomaster Candiani, dir.
  Eduardo Garza): Thorfinn **Lalo Garza**, Askeladd **Dafnis
  Fernández**, Canute **Diego Becerril**, Einar **Diego Estrada**.
  Crunchyroll T2 (Haymillian, dir. Alejandro Eguiza y Julio Gómez):
  **Víctor Tabarez**, **Aldo Ramírez**, **Luba Flores**, **Jonathan
  Miranda**.
- **No hay videojuego oficial** (confirmado). «Dead in Vinland» es otro
  juego, sin relación.
- **Tres láminas** (§27): 1) Askeladd sobre su mapa de campaña, en la casa
  larga con fuego (#proyectos). 2) Thorfinn y Einar en el campo que
  desbrozan, con el mapa de Vinlandia pintado en una tabla (#proyectos o
  su lámina 2). 3) Thors y Thorfinn niño en el muelle nevado, «para dos
  voces» (#textos lámina 2).

---

## 2 · Las escenas que sirven, con minuto

El minuto es **el del vídeo enlazado**. Si es un clip recortado, no es el
minuto del episodio (lo digo en cada caso).

### Las cuatro escenas icónicas

| Escena | Episodio | Dónde se miró | Qué se ve | Estado |
|---|---|---|---|---|
| **Rendición y muerte de Thors** | ep. 4 «A True Warrior» | clip de YouTube [LPnQ74j1dqY](https://www.youtube.com/watch?v=LPnQ74j1dqY) (41 s, storyboard 160×90) | Askeladd con la espada en alto y **sonrisa cruel**. Thors **arrodillado**, espada bajada, mano en la empuñadura, sin atacar. **Thorfinn niño con los ojos muy abiertos de horror.** La sangre se extiende por la túnica gris de Thors | ✅ episodio (ficha de Thors + [sinopsis del ep. 4](https://vinlandsaga.fandom.com/wiki/Episode_4)); ⚠️ minuto dentro del clip |
| **Muerte de Askeladd** | ep. 24 «End of the Prologue» | clip **oficial de Crunchyroll** [PF2NTT_mnps](https://www.youtube.com/watch?v=PF2NTT_mnps) (180 s, storyboard; marca de agua de Crunchyroll) | Askeladd con la **banda roja en la cabeza** y el ojo marcado, tendido y ensangrentado. Un joven rubio llorando lo sostiene. Guardias con antorchas, celda de piedra. Subtítulos en inglés: «Is this the first time you've stabbed someone, prince?», «Hey, Askeladd», «You did well», «This part is important», «Don't waste it» | ✅ episodio ([ep. 24](https://vinlandsaga.fandom.com/wiki/Episode_24)); ⚠️ a 160×90 no se distingue si el que llora es Thorfinn o Canute |
| **Discurso de Canute ante su ejército** | sin confirmar | clip **oficial de Netflix Anime** [Zt85YuG0-_Y](https://www.youtube.com/watch?v=Zt85YuG0-_Y) (184 s, storyboard) | Canute con **capa roja real**, ante su ejército al atardecer sobre el mar. Cortes a un **tapiz tipo Bayeux** (caballería bordada). Primeros planos de su cara fría y decidida: el príncipe débil se vuelve rey | ⚠️ episodio sin localizar (el ep. 44 «Pain» no es) |
| **«Nadie tiene enemigos»** | ep. 2 | clip doblado (Netflix) en [Facebook, Vinland Saga Latinoamérica](https://www.facebook.com/VinlandSagaLatam/videos/nadie-tiene-enemigos-vinland-saga-espa%C3%B1ol-latino/542457653772935/?t=65) (2:14) | 0:04-0:18 Thorfinn niño mira **fascinado una daga**. 0:37-0:45 Thors: «¿a quién quieres matar?». 0:53-1:52 primeros planos de los ojos de Thors, serio. 1:05-1:25 «No tienes enemigos». 1:58-2:04 Thors **arrodillado** se despide de Ylva (vestido rojo). 2:10-2:13 **mascarón de proa** tallado contra el cielo y Thorfinn niño **solo en el muelle nevado** mirando el mar | ✅ (episodio confirmado en la [votación oficial de escenas](https://vinlandsaga.jp/special/best-scene/); plano a plano con `fotogramas.py --cortes`, 31 planos) |

### Otras escenas con minuto

- **Askeladd cuenta la leyenda de Artorius** (ep. 22, doblaje Netflix):
  monólogo de 2:52 a 3:43 del [clip de Facebook](https://www.facebook.com/VinlandSagaLatam/videos/la-infancia-de-askeladd-y-la-leyenda-de-artorius-vinland-saga-t1ep22-doblaje-lat/1012395204836119/?t=172) ✅.
- **Reencuentro de Thorfinn y Einar** (T2 ep. 1, doblaje Netflix): casi
  sin diálogo, sólo música, hasta que Thorfinn grita «¡Ven!» en el 2:36
  del [clip](https://www.facebook.com/VinlandSagaLatam/videos/vinland-saga-ha-regresado-thorfinn-y-einar-se-encuentran-ep1-temporada-2/5631142283607789/?t=156) ✅.
- **Einar llega como esclavo a la granja de Ketil** (clip oficial de
  Netflix Anime [Zk4Iy5PBsOw](https://www.youtube.com/watch?v=Zk4Iy5PBsOw),
  99 s): 0:00-0:03 «—¿Cómo te llamas? —Einar.» (subtítulo automático en
  español); lágrima hacia el 0:31 con «¿En el campo?» ✅.
- **Opening 1 «MUKANJYO»** (Dailymotion, 1280×720, [x8bcl5n](https://www.dailymotion.com/video/x8bcl5n)):
  0:03-0:09 logo rojo sangre sobre mar tormentoso; 0:27 Thorfinn niño con
  miedo; 0:45 mirada fija con dientes apretados; 0:51 corre en la nieve
  hacia una casa con techo de paja; 1:00 aurora sobre el mar de noche;
  1:15 **Thors en contrapicado heroico**, con cicatrices y sangre en la
  túnica; 1:24 **campo de cadáveres bajo la Vía Láctea** ✅.
- **Tráiler oficial T2** (Dailymotion, 1280×720, [x8h1n5b](https://www.dailymotion.com/video/x8h1n5b),
  subtítulos en español): 0:19 Einar a contraluz entre humo y fuego («Yo
  era un guerrero»); 0:39 niño llorando en una aldea en llamas; 0:58 chica
  rubia envuelta en una manta; 1:10 hombre rubio discute con su padre
  (Canute con Sweyn, por contexto ⚠️); 1:17 **puerto vikingo desde el
  aire**; 1:31 brazos tiran de una cuerda para arrancar un **tocón**; 1:42
  Thorfinn recibe un puñetazo **sin devolverlo**; 2:02 castillo con
  relámpagos y tropas en fila; 2:16 cartela «VINLAND SAGA SEASON 2» ✅.

### Lo que falta

- ⚠️ **Nada en 1080p**: YouTube bloqueó la descarga y los mismos clips no
  están en Dailymotion ni en Internet Archive (buscados por título
  exacto). Lo mejor visto es 1280×720.
- En Internet Archive hay **episodios completos subidos por usuarios**
  (p. ej. «[DB] Vinland Saga S1 (Dual Audio) BD 1080p», 15 872 descargas;
  «Vinland Saga Latino», 52 118) según `datos-video.md`. No tienen licencia
  clara y **el equipo no los usó**.

---

## 3 · Arte oficial y hojas de contacto

### Lo oficial, en cantidad

- **Key visuals de la temporada 1** (3, a 750×1058) ✅ (Fandom +
  ComicBook.com): [KV1](https://static.wikia.nocookie.net/vinlandsaga/images/4/48/Vinland_Saga_Key_Visual_1.jpg),
  [KV2](https://static.wikia.nocookie.net/vinlandsaga/images/0/01/Vinland_Saga_Key_Visual_2.jpg),
  [KV3](https://static.wikia.nocookie.net/vinlandsaga/images/5/52/Vinland_Saga_Key_Visual_3.jpg).
- **Key visuals de la temporada 2** (2, a 750×1058), del animador **Raita
  Kazama** ✅ (Fandom + Facebook oficial):
  [S2 KV1](https://static.wikia.nocookie.net/vinlandsaga/images/1/10/Vinland_Saga_S2_Key_Visual_1.png),
  [S2 KV2](https://static.wikia.nocookie.net/vinlandsaga/images/7/7b/Vinland_Saga_S2_Key_Visual_2.png).
- **Portadas de tomo** (Kodansha, Afternoon KC): tomo 1 (840×1200),
  10 (610×880), 20 (1011×1440), 27 (1055×1500) ✅
  ([tomo 1](https://static.wikia.nocookie.net/vinlandsaga/images/b/b1/Volume_1.jpg)).
- **Portada del capítulo 1** (1607×1200) y **revista Afternoon** de
  agosto de 2019, que anuncia el anime (1080×1551) ✅
  ([cap. 1](https://static.wikia.nocookie.net/vinlandsaga/images/c/cc/Chapter_001.jpg),
  [Afternoon 2019-08](https://static.wikia.nocookie.net/vinlandsaga/images/d/d0/Afternoon_2019-08.jpg)).
- **Artbook oficial «Vinland Saga Animation Works»** (WIT Studio, 2020,
  272 páginas, sólo en japonés) ✅. Portada 1390×1964
  ([enlace](https://static.wikia.nocookie.net/vinlandsaga/images/0/04/VinlandSagaWITAnimationWorksCover.png)).
  Tres páginas de muestra, 1500×1059 cada una, **miradas en grande**:
  - **Hoja de diseño de color de Thorfinn granjero** (arco de Vinlandia):
    de frente, de espalda, cuerpo entero, **12 expresiones** y detalle
    del ojo ([enlace](https://static.wikia.nocookie.net/vinlandsaga/images/9/94/AnimationWorksPreview_Thorfinn.png)).
    La mejor referencia de pose y color de todo el dossier.
  - **Hoja de diseño de Askeladd**: vuelta completa con la coraza de cuero
    sin mangas y hombreras de metal, versión «con flechas clavadas» del
    final del arco de Inglaterra, y dos juegos de expresiones. Línea gris,
    sin color ([enlace](https://static.wikia.nocookie.net/vinlandsaga/images/c/c7/AnimationWorksPreview_Askeladd.png)).
  - **Correcciones de Takahiko Abiru** sobre Thorfinn adolescente en el
    arco de la guerra: hacha, daga, gestos de furia
    ([enlace](https://static.wikia.nocookie.net/vinlandsaga/images/c/cb/AnimationWorksPreview_Thorfinn2.png)).
- **AniList**: portada (460×650), banner (1600×900) y **15 retratos
  oficiales** (Thorfinn, Askeladd, Thorkell, Canute, Thors, Leif, Bjorn,
  Ylva, Willibald, Helga, Ragnar, Anne, Halfdan, Mimi…) ✅
  ([portada](https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx101348-2fhDFPCuMNiz.jpg)).
- **Figura oficial figma Thorfinn** (Good Smile Company, n.º 608, unos
  145 mm, ropa de tela, caras y dagas intercambiables; anunciada el
  30-may-2023, salió en feb-2024) ✅
  ([goodsmile.com](https://www.goodsmile.com/en/product/12106/figma+Thorfinn)).
- **Edición española**: el recolector encontró en Openverse 17 miniaturas
  de sobrecubiertas subidas por Salva_Navarro (CC BY-SA 2.0), una con el
  ISBN 9788416051816 en el nombre. Son de 158×229: sólo sirven para saber
  que existen ⚠️ (editorial sin comprobar).
- ⚠️ **No encontré portadas de Blu-ray ni DVD** (búsqueda en los archivos
  de la wiki, sin resultado).

### Las 3 hojas de contacto (`hojas/`), miradas número a número

**`personajes_01.jpg`** (17 imágenes de la wiki):

| # | Qué es (tamaño) | Para qué sirve |
|---|---|---|
| 1 | Cartel de la exposición 40 años de Afternoon (1920×1080) | Nada para la lámina: mezcla muchas series |
| 2 | **Canute T1 en el anime**, pelo rubio largo, capa roja con piel, boca abierta de sorpresa («Moe canute», 1920×1080) | Cara de sorpresa o grito de Canute niño |
| 3 | Retrato de manga en blanco y negro, archivo «Askeladd.png» (1239×1270) | Trazo de manga, rayado de sombras |
| 4 | Viñeta de manga, abrazo con capucha (1056×1132) | Tramas de ropa y pelo |
| 5 | **Viñeta del manga en inglés**: Canute rey con diadema y cicatriz, a caballo entre cabezas en picas; **globos ovalados blancos** (1134×888) | Cómo son los globos del manga (§7) y cómo habla Canute rey |
| 6 | Fotograma del anime, hombre de pelo oscuro en penumbra («Vinland-Saga-24-59», página de Einar, 1280×720) | Luz de interior oscura |
| 7-9 | Viñetas de manga con globos (anciano llorando, Thorfinn adulto frente a otro hombre, dos hombres con cicatrices) | Tramas y globos |
| 10 | **Thorfinn de frente, serio**, manga (1018-1019, 875×875) | Cara neutra adulta |
| 11 | **Thorfinn adulto, arco de Vinlandia**, pelo hacia atrás (873×868) | Cómo se ve al final |
| 12 | **Canute T1 en el bosque**, calmado, capa roja con piel (1080×608) | Pose serena de Canute joven |
| 13-14 | Thorfinn en 1021 y en el arco de esclavitud, manga | Evolución de la cara |
| 15 | **Thorfinn niño con gota de sudor y dientes apretados**, manga (1020×536) | Cara de tensión o rabia infantil |
| 16 | Fotograma: hombre rubio de barba corta con capa roja («Canute's second appearance in Season 2», 736×735) | Canute rey en color |
| 17 | **Diseño del anime de Askeladd, cuerpo entero** (598×854): coraza negra sin mangas, faldón beige, botas marrones, **espada al hombro** | **La pose de presentar de Askeladd** y su ropa |

**`arte_01.jpg`** (15 portadas y key visuals; descrito por el redactor
mirando la hoja):

| # | Qué es | Para qué sirve |
|---|---|---|
| 1 | KV1 T1: **barco entre témpanos** y nieve, logo rojo | Frío, escala, logo |
| 2 | KV2 T1: **noche estrellada**, mástil con farol, logo naranja fuego | Luz de noche con un solo foco cálido |
| 3, 6, 14 | KV3 T1 (y sus versiones de 1000×1411 y de AniList): **el grupo de Askeladd con Thorfinn niño, salpicado de rojo sangre** | Pose de grupo; la mancha roja como textura |
| 4 | S2 KV1: figura entre nubes, «SEASON 2» | Tono más claro de la T2 |
| 5 | S2 KV2: **muchos personajes y una explosión de sol en el centro** | Luz de contraluz dorada |
| 7 | **Portada del artbook**: rojo con ornamento dorado y 6 medallones azules | Marco decorativo, cenefa |
| 8 | Tomo 1: Thorfinn con daga y piel, **vela de rayas rojas y blancas** detrás | Pose con su arma |
| 9-11 | Tomos 10, 20 y 27 (el 27, con **colonos y nativos** del arco de Vinlandia) | Ropa de granjero y de Vinlandia |
| 12 | Capítulo 1: logo rojo con una espada en la «I» | Logo original (§6) |
| 13 | Revista Afternoon 2019-08, amarilla y roja, «TVアニメ 7/7» | Rotulación japonesa |
| 15 | Banner de AniList (recorte del KV1) | Fondo apaisado |

**`fondos_01.jpg`** (15 fondos, mapas y paisajes):

| # | Qué es | Para qué sirve |
|---|---|---|
| 1 | **Islandia en el anime**: montañas nevadas, costa y mar azul (1024×488) | Fondo frío de día |
| 2 | Manga: **barco entre olas** junto a acantilados de Islandia (1000×703) | Barco en blanco y negro |
| 3 | Manga: montaña de Gales (1584×1304) | Paisaje de Inglaterra |
| 4 | **Mapa de manga del cruce a Gales**: «Kingdom of Morgannwg», «Askeladd's landing», «Thorkell's men», Bristol, Wessex (1160×754) | **El mapa de campaña del concepto 1** |
| 5-6 | Manga, capítulos 130 y 138: **Jomsborg** con casas largas y muralla | Arquitectura vikinga |
| 7 | Manga, capítulo 146: **Jomsborg circular de noche** con la onomatopeya **ゴオォォ** a pincel y una franja negra con texto en mayúsculas | Onomatopeya y cartela de narrador (§7) |
| 8 | Artbook, «Environment»: **bocetos a lápiz** de sitios | Composición de fondos |
| 9 | Artbook, «Scenery»: **tableros de color**: interior de casa larga de madera con fuego, fiordo nevado, **aurora sobre el mar**, acantilado verde con playa, **casa larga nevada** | **Los sitios reales de la lámina** |
| 10 | Artbook, «Ship»: **vuelta completa del barco** (perfil, popa, proa) | Barco en Blender |
| 11 | Fondo de fans (3840×2160, mushit): **brazo encadenado que sujeta una espada**, gris | Motivo de la esclavitud |
| 12 | Fondo de fans: **ruinas de noche con luna** (1920×1080) | Paleta nocturna medida (§5) |
| 13 | Fondo de fans: **Thorfinn con capa mirando el paisaje al amanecer** (1920×1080) | Pose de espaldas, pensar |
| 14 | Fondo de fans: lago con reflejo al atardecer (1920×1080) | Calma |
| 15 | Fondo de fans: dos figuras junto a una **columna romana en ruinas**, colinas de otoño (1920×1080) | Inglaterra con restos romanos |

> [!warning] Corrección del redactor
> En `partes/imagen.md` y `imagen.json` las tres páginas del artbook
> tenían los nombres cruzados. Según los nombres de archivo de la hoja:
> **Environment** = bocetos a lápiz, **Scenery** = tableros de color
> (casa larga, aurora, acantilado), **Ship** = vuelta del barco. El
> **brazo encadenado** no es del artbook: es el fondo de fans
> wallhaven-6d5zgl. También los KV de la T1: el KV2 es el barco de
> noche y el KV3 es el grupo de Askeladd salpicado de sangre.
> `referencias.json` ya va corregido.

---

## 4 · Fan art y 3D, sólo como referencia

Nunca para pegar. Sirven para ver cómo lo dibuja el fandom y para
volumen.

### Fan art (Safebooru, con autor)

| Personaje | Tamaño | Imagen | Autor u origen |
|---|---|---|---|
| Thorfinn | 2663×4096 | [safebooru](https://safebooru.org/images/1607/9ad014051e207e675e1892a16b01552687451625.jpg) | [x.com/icebuko](https://x.com/icebuko/status/2076979563817836965) ⚠️ |
| Thorfinn | 2560×1440 | [safebooru](https://safebooru.org/images/825/e7495f75df0ffd099b797c5b4012c31880a17126.jpg) | [x.com/velupium](https://x.com/velupium/status/2041344911346139581) |
| Askeladd | 609×750 (4 pts) | [safebooru](https://safebooru.org/images/550/128a6882491efac98f651f809fcc759d4e88a65a.jpg) | pixiv chicken79 |
| Askeladd | 2000×1304 | [safebooru](https://safebooru.org/images/3161/297310384b1ef589bc4065126b16a7f414fc71ad.jpg) | [pixiv 81185819](https://i.pximg.net/img-original/img/2020/04/30/23/18/41/81185819_p0.jpg) |
| Askeladd | 1390×2048 | [safebooru](https://safebooru.org/images/4220/0df71349ddac17f10ac71b2b69436df0841a4d05.jpg) | [twitter.com/kakuzta](https://twitter.com/kakuzta/status/1670353505109045248) |
| Askeladd | 1200×1534 | [safebooru](https://safebooru.org/images/4058/ffc4f8adf5a76c3d244fc48f9e83084997b1c552.png) | twitter.com/frkdlsch_draws |
| Askeladd y Canute | 792×1224 | [safebooru](https://safebooru.org/images/4213/c9cf9c2cae74926c7158dd7b52dd88167de34af4.jpg) | pixiv 108973137 |
| Canute | 1105×1600 (3 pts) | [safebooru](https://safebooru.org/images/103/3233183b9add3e1d8afae558fb730f6c38a1534a.jpeg) | sin origen |
| Canute | 1748×2481 | [safebooru](https://safebooru.org/images/2837/d684858f2038ca181a07ca05b3dcb3eddeb03d2d.png) | [i.redd.it](https://i.redd.it/3qqdyejwls041.png) |
| Einar | 1073×1266 | [safebooru](https://safebooru.org/images/4616/b2f301cef5c919058ae683d03fc74ce8112c9c12.png) | [4chan /a/](https://i.4cdn.org/a/1740795508976049.png) |
| Einar en el trigo | 900×558 | [safebooru](https://safebooru.org/images/622/261c7c12f13c956b254ffa8c6f83047219997582.jpg) | [DeviantArt karaii, «Vinland Saga Wheat»](http://karaii.deviantart.com/art/Vinland-Saga-Wheat-194965245) |

> [!warning] Datos contaminados
> En `datos-imagen.md` y `datos-voz.md`, parte de las listas de Danbooru y
> Safebooru traen personajes de **otras series** (hatsune_miku,
> artoria_pendragon, yakumo_yukari, inubashiri_momiji, raiden_shogun…).
> No son de Vinland Saga: se ignoran y no pasan a `referencias.json`.

### Modelos 3D con licencia libre (Sketchfab, todos CC BY: exigen crédito)

Crédito exacto: «*Título*» de *Autor*, CC BY 4.0, con el enlace.

| Modelo | Autor | Enlace |
|---|---|---|
| Thorfinn's Knives From Vinland Saga (♥15) | SILVER KEY | [sketchfab](https://sketchfab.com/3d-models/none-10ec8a60e33b43449e835ee6e3e1d6f0) |
| Thorfinn's Knife (♥15) | Elliott_Lowes | [sketchfab](https://sketchfab.com/3d-models/none-3ac2763a9fb741b7a024b2b7b0bc4a0e) |
| Thorfinn's Dagger (Vinland Saga), 852 caras (♥8) | SMich017 (Samantha Michelson) | [sketchfab](https://sketchfab.com/3d-models/thorfinns-dagger-vinland-saga-0f430617c66142d283d13029bac42de4) |
| Thorfinn's Dagger (♥12) | luacha2000 | [sketchfab](https://sketchfab.com/3d-models/none-081115bd0e9a4c3a93f5907a4000a68c) |
| Thorfinn Dagger (Battle damage) | Vomitor | [sketchfab](https://sketchfab.com/3d-models/none-477206d1732a4810be30195b55d81577) |
| Snake Sword - Vinland Saga (♥12) | obamazz | [sketchfab](https://sketchfab.com/3d-models/none-448c5654adcf4097822473f85846ac88) |
| Thors From Vinland Saga Lowpoly (490 783 caras, según la API) | FramelessGamesGuy | [sketchfab](https://sketchfab.com/3d-models/thors-from-vinland-saga-lowpoly-cb76da08bda048aab6cc35bb52ae0e43) |
| Lowpoly Model Askeladd Bonavera (♥0) | Sebastian Bonavera | [sketchfab](https://sketchfab.com/3d-models/none-8b98182fd8db45788399aa01e5129163) |
| Thors Death Inktober Day15 Legend (♥42) | muppe5 | [sketchfab](https://sketchfab.com/3d-models/none-42ceb96d7b51456aa723561aeb0c3c29) |
| Arm Guard (♥21) | J.R.Ramos | [sketchfab](https://sketchfab.com/3d-models/none-6736a700c527415da6ff529e7f6966ed) |

**Genéricos vikingos** (no son de la serie, sirven para el sitio):

- Viking Longship (♥285), de massive-graphisme: [sketchfab](https://sketchfab.com/3d-models/none-3d649f8373514860b69ff6f874c0efb5).
- Barco con el uid `ecc03f0875e34a0cb2e66c40b22383e5` (♥324, 14 813 caras):
  [sketchfab](https://sketchfab.com/3d-models/viking-longship-ecc03f0875e34a0cb2e66c40b22383e5).
  ⚠️ `imagen.md` lo da como «Longboat» de **kreinin** y `texto.md` como
  «Viking Longship» de **FoxxAssets**: comprobar el autor en la página
  antes de poner el crédito.
- Viking shaman hut (♥153), de JulienSchoots: [sketchfab](https://sketchfab.com/3d-models/none-eb98d1aef0fa4e01ab5584fff0c23742).
- Medieval viking house (♥25), de vlad_design228: [sketchfab](https://sketchfab.com/3d-models/none-1a720687cb1f4747ade741508cd505bc).

⚠️ No hay modelo libre de cuerpo entero de Thorfinn, Canute ni Einar. Para
volumen, usar la **figma de Thorfinn** (§24) y el cosplay.

---

## 5 · Sitios, luz, paleta y texturas reales

Todos los hex salen de `herramientas/estilo.py` sobre fotogramas propios
(1280×720 salvo que se diga), con el vídeo y el segundo.

| Sitio | Vídeo y minuto | Paleta medida | Luz |
|---|---|---|---|
| **Aurora sobre el mar, de noche** | OP1, [1:00](https://www.dailymotion.com/video/x8bcl5n?t=60) | `#131E35` `#16244A` `#1A3064` `#1B3F7B` `#20578F` `#2373A3` `#2895B6` `#34BAC6` | Saturación 73 %, brillo 45 %; degradado, casi sin línea. La imagen más repetida de la serie (también en el ED1) |
| **Campo de cadáveres bajo la Vía Láctea** | OP1, [1:24](https://www.dailymotion.com/video/x8bcl5n?t=84) | `#1B1C1D` `#131314` `#252628` `#2B3140` `#3C4257` `#4A4F6F` `#6A5F76` `#8B7C9E` | Brillo 30 %, saturación 23 %. Un guerrero solo en la cima, lanzas clavadas, cielo violeta y rosa |
| **Islandia nevada, casas con techo de paja** | OP1, [0:51](https://www.dailymotion.com/video/x8bcl5n?t=51) | `#F1F1EA` (41 %) `#CED1D9` `#9DB1D0` `#7B94B9` `#48658B` `#C5B096` | Brillo 81 %, saturación 16 %: blanco frío de invierno, sombras azul gris |
| **Praderas de Inglaterra** (con créditos encima) | OP1, [0:27](https://www.dailymotion.com/video/x8bcl5n?t=27) | `#DBD3C3` `#E6E7E4` `#C1BCB1` `#CFC288` `#ACA593` `#9C8F71` | Brillo 73 %, saturación 17 %; el verde real es algo más vivo (el texto pesa en la media) |
| **Puerto vikingo desde el aire** | Tráiler T2, [1:17](https://www.dailymotion.com/video/x8h1n5b?t=77) | `#9E8F66` `#B4A684` `#D1C6A7` `#7F7152` `#60533C` `#41616A` `#2E413E` `#658490` | Brillo 53 %, saturación 33 %: agua verde azulada turbia, madera tostada |
| **Bosque de la granja** (tirando del tocón) | Tráiler T2, [1:31](https://www.dailymotion.com/video/x8h1n5b?t=91) | `#263020` `#1B2616` `#363D27` `#554E2D` `#816541` `#A07758` `#BC9875` `#EAC7A1` | Brillo 44 %, saturación 40 %: sol de mediodía sobre la piel, fondo verde oscuro |
| **Castillo con relámpagos y tropas** | Tráiler T2, [2:02](https://www.dailymotion.com/video/x8h1n5b?t=122) | `#0B0907` `#241B0D` `#462D1B` `#694630` `#8F654A` `#B68C6E` `#DCBD9C` `#F9F7F1` | Mucho contraste: silueta negra contra luz blanca; línea más marcada |
| **Fiordo nevado, barco al atardecer** | ED1 «Torches», [storyboard](https://www.youtube.com/watch?v=rlb942EnOF0) | `#F8F9F5` `#E7E9E3` `#CFD4CC` `#B2BCB5` `#909C96` `#70776F` | Brillo 75 %, saturación 13 % |
| **Aurora y antorcha en la tormenta** | ED1, segunda mitad | `#090D10` `#1F2829` `#40433F` `#6A635D` `#928F83` `#329D5B` (verde aurora) | Brillo 35 %, saturación 38 % |
| **Trigal dorado con flores** | ED1, tramo final | `#F3E9D7` `#EFE68F` `#E8E74D` `#BDAB4B` `#6C6957` `#2B3531` | Brillo 64 %, saturación 34 %: lo más cálido de toda la serie |
| **Ruinas de noche con luna** (fondo de fans) | [wallhaven-q6oor5](https://w.wallhaven.cc/full/q6/wallhaven-q6oor5.png) | `#1C394B` `#152429` `#448AA1` `#65C5D9` | Azul noche desaturado, cian en el cielo |
| **Paisaje al amanecer** (fondo de fans) | [wallhaven-lmddyq](https://w.wallhaven.cc/full/lm/wallhaven-lmddyq.png) | `#1A3B4A` `#2B5B70` `#4A7EA7` `#97B1DA` | Misma familia azul verdosa, más clara |

**Lo que dicen las paletas juntas**: casi todo es **frío y poco saturado**
(noche, nieve, mar). El **fuego es la única luz cálida** en interiores
(§19). El trigal del ED1 es la excepción cálida: la calma después de la
violencia.

**Interiores**: el tablero «Scenery» del artbook (hoja `fondos_01.jpg` #9)
muestra la **casa larga de madera oscura con el fuego como único foco**,
y la **casa larga nevada** por fuera ✅ (visto en la hoja).

### Texturas reales libres (CC0, ambientCG)

| Capa | Textura | Enlace |
|---|---|---|
| Papel, pergamino | Paper001 | [ambientcg](https://ambientcg.com/view?id=Paper001) |
| Lana y lino de túnicas | Fabric081C, Fabric061 | [Fabric081C](https://ambientcg.com/view?id=Fabric081C), [Fabric061](https://ambientcg.com/view?id=Fabric061) |
| Cuero (coraza de Askeladd, cinturones) | Leather037, Leather030 | [Leather037](https://ambientcg.com/view?id=Leather037) |
| Metal (hombreras, hebillas, hachas) | Metal063, Metal049A | [Metal063](https://ambientcg.com/view?id=Metal063) |
| Tablón de barco y casa | WoodFloor051, Planks030A | [WoodFloor051](https://ambientcg.com/view?id=WoodFloor051), [API](https://ambientcg.com/api/v2/full_json?type=Material&q=wood+plank) |

⚠️ **Faltan nieve, paja de techo y piedra**: nadie llegó a buscarlas. La
consulta está lista: `https://ambientcg.com/api/v2/full_json?type=Material&q=snow`
(y `thatch`, `stone`).

---

## 6 · Tipografía: una letra para cada uso

Cada letra libre se **descargó y se abrió con fontTools**: todas traen
á é í ó ú ñ Ñ ¿ ¡ ✅. Enlaces directos al `.ttf` de Fontsource (licencia
OFL, uso libre).

| Uso | Cómo es en la serie (visto) | Letra libre | Estado |
|---|---|---|---|
| **Logo o título** | Portada del capítulo 1: «VINLAND SAGA» en **rojo, trazo desgarrado de pincel o filo de espada**, contorno blanco y sombra oscura; encima ヴィンランド・サガ en caligrafía gruesa ([Chapter 001](https://vinlandsaga.fandom.com/wiki/File:Chapter_001.jpg)). En la hoja `arte_01.jpg` #12 la «I» es una espada | [**Eater**](https://cdn.jsdelivr.net/fontsource/fonts/eater@latest/latin-400-normal.ttf) | ✅ visto; ⚠️ es aproximación de estilo (no está en Fonts In Use) |
| **Carteles «rúnicos»** | Tomo 1 de Kodansha USA: «VINLAND SAGA» **blanco, tallado**, con **nudos nórdicos** a los lados y una **cenefa de falsas runas** arriba ([Book1](https://vinlandsaga.fandom.com/wiki/File:Book1.png)) | [**Pirata One**](https://cdn.jsdelivr.net/fontsource/fonts/pirata-one@latest/latin-400-normal.ttf) | ✅; ⚠️ no se sabe si las runas del borde dicen algo |
| **Cartela de cita y créditos** | Tráiler T2: pantalla negra, **serif blanca de alto contraste**, centrada, sin caja: «Obra Original / Makoto Yukimura» (0:03), «Producción MAPPA» (0:07), «Los crímenes de un monstruo» (0:21) | [**Playfair Display**](https://cdn.jsdelivr.net/fontsource/fonts/playfair-display@latest/latin-700-normal.ttf) | ✅ visto con minuto |
| **Subtítulos** | Tráiler T2, 0:47: «Hay gente prejuiciosa en todas partes, pero no todos lo son.» **Sans blanca**, contorno oscuro fino, dos líneas centradas abajo, sin caja | [**Noto Sans**](https://cdn.jsdelivr.net/fontsource/fonts/noto-sans@latest/latin-400-normal.ttf) | ✅ visto con minuto |
| **Cartel del mundo, mapas** | Opening: «Vinland» **escrito a pluma en tinta roja marrón**, caligrafía irregular, sobre un mapa color pergamino con vetas de madera ([mapa del OP](https://vinlandsaga.fandom.com/wiki/File:Anime_op_vinland_map.jpg), 1280×720) | [**MedievalSharp**](https://cdn.jsdelivr.net/fontsource/fonts/medievalsharp@latest/latin-400-normal.ttf) | ✅ visto |
| **Globo normal** (manga) | Edición inglesa: **mayúsculas de cómic, centradas**, en globo ovalado (hoja `personajes_01.jpg` #5) | **Anime Ace 2.0 BB** (Blambot, con tildes según la guía de `_ya_hechas`) | ⚠️ no se vio una página japonesa |
| **Grito** | No visto en un panel | [**Anton**](https://cdn.jsdelivr.net/fontsource/fonts/anton@latest/latin-400-normal.ttf) (condensada de impacto) | ⚠️ propuesta |
| **Pensamiento** | En el anime **no hay nube**: lo interior va en **voz en off** con subtítulo sobre la imagen (Einar, tráiler 0:19, «Yo era un guerrero») | Noto Sans, como el subtítulo | ✅ visto |
| **Onomatopeya** | Manga, cap. 146: **ゴオォォ en katakana a pincel negro con borde blanco**, torcida, encima del paisaje (hoja `fondos_01.jpg` #7) | Dibujarla a mano con pincel; si hace falta letra, Eater (mismo trazo roto que el logo) | ⚠️ una sola viñeta; la letra es propuesta del redactor |
| **Narrador del manga** | Cap. 146 en inglés: **franja negra con mayúsculas condensadas blancas** («THE FIRST NIGHT AFTER THE OPENING SALVO OF THE JOMSBORG WAR.», hoja `fondos_01.jpg` #7) | Anton | ⚠️ una viñeta, edición inglesa; letra propuesta del redactor |
| **Interfaz de juego** | No aplica: **no hay videojuego oficial** (§13) | — | ✅ |

**Logo vectorial**: Wikimedia Commons tiene
[«Vinland Saga simplified logo.svg»](https://upload.wikimedia.org/wikipedia/commons/7/7f/Vinland_Saga_simplified_logo.svg)
(686×553), trazado a curvas: sirve de silueta, no dice la fuente. Posible
marca registrada: sólo referencia.

---

## 7 · Cómo hablan y piensan en pantalla: el cuadro de diálogo

**Lo más importante: en el anime nadie habla con una burbuja.** ✅ (mirado
en el tráiler T2 y el OP1, con minuto).

### En el anime

- **Subtítulo sin caja**: sans blanca, contorno fino, dos líneas centradas
  abajo (tráiler, 0:47). Es el formato de la plataforma.
- **Cartela negra con serif blanca**, centrada, sin marco: citas y
  créditos (0:03, 0:07, 0:21).
- **Voz en off sobre imagen**: lo que el personaje piensa o recuerda se
  oye mientras se ve otra cosa (Einar a contraluz, 0:19).
- **Silencio**: el reencuentro de Thorfinn y Einar (T2 ep. 1) va **casi
  sin palabras**, sólo música, hasta el «¡Ven!» del 2:36. La emoción no
  necesita texto.
- **Texto pintado dentro del mundo**: «Vinland» a pluma en el mapa del
  opening.

### En el manga

- **Cartela roja rectangular con texto blanco**: el número de capítulo
  («第1話») en la portada del capítulo 1. Sin adornos ✅ (visto). Es el
  único «cuadro» limpio y geométrico de la obra.
- **Globos** (edición inglesa de Kodansha USA, visto por el redactor en la
  hoja `personajes_01.jpg` #5, 7, 8, 9 y 13): **óvalos blancos**, línea
  negra fina, **cola corta en punta**, texto en **mayúsculas de cómic
  centradas**. Ejemplo textual (#5, Canute rey): «YOU SPEAK AS THOUGH THIS
  WAS AN ACT OF NATURE, GUNNAR.» / «WE DID THIS.» ⚠️ (edición inglesa; no
  se vio una página japonesa).
- **Narrador**: franja negra con mayúsculas blancas condensadas, en
  vertical al borde de la viñeta (hoja `fondos_01.jpg` #7) ⚠️.
- **Onomatopeya**: katakana a pincel, grande, torcida (#7) ⚠️.
- **Títulos de capítulo con fecha y lugar**: «Inglaterra, 1013 d.C.»,
  «Inglaterra, 1008 d.C.» (capítulos 17 y 18,
  [Story Arcs](https://vinlandsaga.fandom.com/wiki/Story_Arcs)) ✅. ⚠️ No
  se comprobó si el anime pone esta cartela en pantalla.

### Qué cuadro usar en la lámina

1. **Para el texto del canal**: tallado o pintado **sobre un objeto del
   mundo** (tabla de madera, pergamino, cuero), con MedievalSharp o
   Pirata One. La tinta sigue la veta y las arrugas.
2. **Para el nombre de quien habla o el título**: la **cartela roja
   rectangular con texto blanco** del manga.
3. **Para la frase del personaje**: **cartela negra con serif blanca**
   (Playfair Display), como en los tráileres, o **subtítulo sin caja**
   (Noto Sans) abajo, como en el anime.
4. **Nunca**: burbuja blanca con cola, nube de pensamiento, globo de
   colores. Aunque el manga inglés use óvalos blancos, en una lámina se
   leen como «burbuja blanca rara».

El rojo de la cartela **no se midió** ⚠️: sacarlo con `estilo.py` de
[Chapter_001.jpg](https://static.wikia.nocookie.net/vinlandsaga/images/c/cc/Chapter_001.jpg).
Como apoyo, el rojo medido de la túnica de Canute T1 es `#9C403B`.

---

## 8 · Los personajes: qué transmiten, su cara en cada emoción y sus dinámicas

Textos de la wiki (secciones Personality, History, Abilities, Trivia) ✅
salvo que se diga. Caras con el minuto del vídeo enlazado.

### Askeladd (Lucius Artorius Castus) · el secundario más querido

- **Quién es**: hijo ilegítimo de **Lydia**, noble galesa esclavizada, y
  del vikingo **Olaf**. De niño no tenía nombre: iba cubierto de ceniza y
  estiércol de sus trabajos para mantener a su madre, de ahí «Askeladd»,
  **el Muchacho Ceniciento** ([wiki](https://vinlandsaga.fandom.com/wiki/Askeladd)).
  A los 11 años se enfrentó con una espada a Olaf para defender a su
  madre; perdió, pero Olaf lo reconoció. Años después lo mató y se quedó
  con sus hombres.
- **Carácter**: astuto, manipulador, carismático. Su mayor arma es la
  cabeza: **sabe qué clase de persona es alguien sólo con mirarle la
  cara**. Gran espadachín, también con hachas y cuchillos arrojadizos.
- **Qué le importa**: no cree que el héroe Artorius vuelva a salvar a su
  pueblo («¿por qué querría volver a un mundo como éste?»). Aun así, al
  final **se sacrifica** ante el rey Sweyn para que Canute reine y los
  britanos tengan una oportunidad (manga cap. 90-91, anime ep. 24).
- **Qué transmite**: respeto incómodo. Das miedo y confianza a la vez; es
  el mentor cínico que no quieres admirar y admiras.
- **Cómo habla**: **nunca grita**. Amenaza con calma. Explica **con
  historias o acertijos** antes de llegar al punto (el monólogo de
  Artorius). Su voz latina (Dafnis Fernández) mide **104 Hz, grave**, con
  **27,7 semitonos de rango: muy expresiva** y a **2,55 palabras por
  segundo** ✅ (medido con `voz.py`).
- **Cuerpo**: postura **relajada, casi lánguida**, incluso peleando.
  **Sonrisa ladeada** que tapa lo que piensa.
- **Su cara**:

| Emoción | Dónde | Qué hace |
|---|---|---|
| Cruel, burlón | ep. 4, [clip](https://www.youtube.com/watch?v=LPnQ74j1dqY) | Espada en alto, sonrisa |
| Explicando, gruñón | ep. 24, [clip Crunchyroll](https://www.youtube.com/watch?v=PF2NTT_mnps) | Banda roja, ojo entrecerrado: «this part is important» |
| Sereno ante la muerte | ep. 24, mismo clip | Tendido, ensangrentado, cara relajada |
| Miedo, dolor (de joven) | [clip 1nRt6tiU20g](https://www.youtube.com/watch?v=1nRt6tiU20g) | Un solo ojo muy abierto en la oscuridad; cara con sangre, gritando ⚠️ escena sin identificar |
| Alegría, tristeza, vergüenza | — | ⚠️ sin fotograma |

### Thorfinn (Thorfinn Karlsefni, hijo de Thors) · el protagonista

- **Historia**: de niño, curioso y cariñoso; le encantan las historias de
  aventuras de Leif. Ve morir a su padre a manos de Askeladd (ep. 4) y se
  une a la banda de su asesino sólo para retarlo en duelo. Pasa **unos 10
  años frío e impulsivo**, sin empatía: cuando la banda mata o viola, él
  «simplemente se aleja». Muerto Askeladd, se queda sin propósito, lo
  venden como esclavo a la granja de Ketil y allí, con Einar, entiende por
  fin a su padre: «no tienes enemigos». Su meta pasa a ser **fundar
  Vinlandia** ([wiki](https://vinlandsaga.fandom.com/wiki/Thorfinn)).
- **Miedo**: volverse lo que odia, un asesino como Askeladd.
- **Qué le importa**: la memoria de su padre; después, no repetir la
  violencia con los suyos (Einar, Gudrid, sus hijos).
- **Qué transmite**: en el arco de la guerra, **tensión y frialdad que
  incomodan**. Desde la esclavitud, **alivio y esperanza**.
- **Cómo habla**: de niño, voz aguda y entusiasta. En la venganza,
  **frases cortas y secas**, casi sin entonación. De adulto explica
  **despacio, con pausas largas**.
- **Los ojos** (lo que más comenta el fandom, ✅ TV Tropes + fotogramas):
  niño, **grandes, redondos, curiosos**; en la venganza, **entrecerrados
  y «muertos», sin brillo**, ceño fruncido, hombros tensos; tras la
  esclavitud, **grandes otra vez**, postura suelta, manos abiertas.
- **Aspecto fijo**: pelo corto despeinado, ropa vieja, **dos cuchillos**,
  **bajo de estatura** (se lo dicen varios personajes).
- **Su cara**:

| Emoción | Dónde | Qué hace |
|---|---|---|
| Alegría, fascinación (niño) | clip ep. 2, [0:04-0:18](https://www.facebook.com/VinlandSagaLatam/videos/nadie-tiene-enemigos-vinland-saga-espa%C3%B1ol-latino/542457653772935/?t=4) | Ojos redondos muy abiertos mirando una daga |
| Miedo | OP1, [0:27](https://www.dailymotion.com/video/x8bcl5n?t=27) | Ojos muy abiertos, envuelto en piel oscura, viento en el pelo |
| Rabia contenida, decisión | OP1, [0:45](https://www.dailymotion.com/video/x8bcl5n?t=45) | Mirada fija a cámara, dientes apretados |
| Tensión o rabia infantil | manga, hoja `personajes_01.jpg` #15 | Gota de sudor, dientes apretados |
| Horror, tristeza | ep. 4, [clip](https://www.youtube.com/watch?v=LPnQ74j1dqY) | Niño, ojos muy abiertos, boca entreabierta, mirando arriba |
| Llanto, culpa | ep. 24, [clip](https://www.youtube.com/watch?v=PF2NTT_mnps) | Joven rubio llorando, manos temblorosas ⚠️ puede ser Canute |
| Vergüenza | — | ⚠️ sin fotograma |

### Canute (Canuto) · el príncipe que se vuelve rey

- **Historia**: príncipe danés, tímido, **con cara casi de chica** (algunos
  hombres creen que es la diosa Freyja); no hace nada sin su consejero
  **Ragnar** y los vikingos se burlan de él, también por su fe cristiana.
  Su padre Sweyn quiere matarlo; Askeladd hace matar a Ragnar para
  obligarlo a madurar. Se vuelve **un rey frío, manipulador y cristiano
  devoto** que quiere «un paraíso en la Tierra» y elimina a quien estorba
  (hasta envenena a su hermano) ([wiki](https://vinlandsaga.fandom.com/wiki/Canute)).
  De joven odiaba las armas; luego aprende a pelear. Según tuits de
  Yukimura, **está casado y tiene hijos, pero el autor «olvidó
  dibujarlos»** ✅.
- **Qué transmite**: primero, lástima; después, **frialdad que impone**.
- **Cómo habla**: de niño, voz temblorosa y frases cortadas. De rey,
  **pausado y absoluto**: «Yo crearé un paraíso en esta Tierra» (en la wiki inglesa: «I will create a worldly paradise in this land...»).
- **Su cara**:

| Emoción | Dónde | Qué hace |
|---|---|---|
| Sorpresa, grito | hoja `personajes_01.jpg` #2 | Boca abierta, cejas arriba, capa roja con piel |
| Calma | hoja `personajes_01.jpg` #12 | Serio en el bosque |
| Angustia, compasión | [clip rsZc66_fisM](https://www.youtube.com/watch?v=rsZc66_fisM) | Ojos muy abiertos mirando a un hombre caído |
| Frialdad, dureza | [clip del discurso](https://www.youtube.com/watch?v=Zt85YuG0-_Y) | Ceño fruncido, cara girada |
| Tensión, confrontar | tráiler T2, [1:10](https://www.dailymotion.com/video/x8h1n5b?t=70) | Puño cerrado ante su padre ⚠️ por contexto |
| Alegría, vergüenza | — | ⚠️ sin fotograma |

### Einar · el amigo de la granja

- **Historia**: del norte de Inglaterra. De niño pierde a su padre en un
  ataque inglés; de joven, los daneses arrasan su aldea, matan a su madre
  **Emma** y a su hermana **Lotta**, y lo venden como esclavo hasta la
  granja de Ketil. Allí lo ponen a **talar un bosque con Thorfinn** para
  ganar la libertad. No se hacen amigos enseguida; cuando entiende el
  pasado de Thorfinn, **lo adopta como hermano**. Se enamora de
  **Arnheid**; tras su muerte, los dos van a por Vinlandia
  ([wiki](https://vinlandsaga.fandom.com/wiki/Einar)).
- **Carácter**: directo, emocional, franco; **se sonroja** cuando Arnheid
  lo elogia. No sabe pelear, pero es grande y fuerte y sabe de campo.
- **Qué transmite**: **calidez y humanidad** en medio de la granja de
  esclavos: la voz que recuerda que se puede vivir sin violencia.
- **Su cara**:

| Emoción | Dónde | Qué hace |
|---|---|---|
| Cautela | [clip Netflix](https://www.youtube.com/watch?v=Zk4Iy5PBsOw), ~0:14 | Mira hacia arriba a Ketil, serio, cejas algo fruncidas |
| Tristeza contenida | mismo clip, ~0:31 | **Una lágrima**, mirada de reojo, mandíbula tensa |
| Sorpresa | mismo clip, ~1:16 | Ojos muy abiertos, cejas arriba, jadeando |
| Llanto (niño) | tráiler T2, [0:39](https://www.dailymotion.com/video/x8h1n5b?t=39) | Llora a gritos en la aldea en llamas |
| Rabia | clip de fans [Nu6G6dy1C88](https://www.youtube.com/watch?v=Nu6G6dy1C88) | Grita de rabia con la aldea ardiendo detrás ⚠️ canal no oficial |
| Vergüenza | wiki | Se sonroja con Arnheid ⚠️ sin fotograma |

### Otros secundarios queridos

- **Thorkell «el Alto»** (3.º en AniList): tío de Thorfinn, general
  jomsvikingo de **230 cm**. Casi siempre **sonriendo**; sólo se enfurruña
  si lleva tiempo sin pelear. **Nunca ataca a quien no puede
  defenderse**: hasta le da un arma a un enemigo desarmado. Frase (manga
  cap. 140): «Yo... sólo... quiero... pelear.» Quiere un duelo a muerte
  con Thorfinn que **nunca se completa** (3 intentos) ✅. TV Tropes: «Crazy
  Awesome».
- **Thors** (5.º en AniList): padre de Thorfinn, «**el Troll de Jom**»,
  180 cm. Se cansó de la guerra, fingió su muerte y se hizo **granjero
  pacifista**. Se le considera el mejor luchador de la serie ✅ (AniList).
  Habla con **calma de padre que regaña sin gritar** (primeros planos de
  sus ojos, clip ep. 2, 0:53-1:52).
- **Gudrid**: exploradora que no acepta los papeles de mujer de su época;
  la **compañera de Thorfinn** en el arco de Vinlandia ✅.
- **Snake (Serpiente)**: compasivo con esclavos y libres, pero ve la
  esclavitud como normal; sólo pierde la calma si matan a su gente ✅.
- **Ylva**: hermana mayor de Thorfinn, de carácter firme; cuida la casa y
  a su madre Helga cuando él se va ✅.
- **Leif Erikson**: el explorador que cuenta historias de Vinlandia y
  **busca a Thorfinn más de una década**; figura de padre sustituto ✅.
- **Bjorn**: segundo de Askeladd, **berserker** que entra en furia comiendo
  ciertas setas (AniList).
- **Willibald**: fraile de 23 años que acompaña a Canute; le gusta el
  alcohol y **busca el amor verdadero** (AniList).
- **Ragnar**: consejero de Canute; calvo con pelo negro largo y rizado a
  los lados, cejas muy gruesas, arrugas hondas, barba espesa (AniList).

### Dinámicas (para láminas en grupo)

| Pareja | Cómo es | Sirve para |
|---|---|---|
| Thorfinn y Askeladd | Odio y aprendizaje: Askeladd se burla de Thors para que Thorfinn pierda los duelos, y a la vez lo aconseja | Tensión, «el que sabe y el que aprende» |
| Thorfinn y Einar | **Hermanos** de la granja; Einar es el franco | Trabajo en equipo, calidez |
| Thorfinn y Canute | Rivales en la guerra, luego aliados distantes | Dos caminos distintos |
| Canute y Ragnar | Padre sustituto; su muerte lo cambia | Pérdida |
| Askeladd y Canute | Askeladd lo empuja a madurar y muere por él | Mentor y rey |
| Thorkell y Thorfinn | Tío y sobrino; el duelo que nunca termina | Humor bruto y acción |
| Einar y Arnheid | Amor en la granja, acaba en tragedia | La escena que hace llorar |

La página «Vinland Saga Latinoamérica» hizo una imagen con **«el dúo de
cada arco»**: Thorfinn y Canute (guerra), Thorfinn y Einar (esclavo),
Thorfinn y Sigurd (Báltico), Thorfinn y Pulmuk (Vinlandia) ✅
([Facebook](https://www.facebook.com/VinlandSagaLatam/photos/a.100291368282103/388514229459814/)).

---

## 9 · ¿Quién es el más querido?

**Askeladd.** El secundario le gana en cariño al protagonista si se mira
por encuesta y por tiempo en pantalla.

| Medida | 1.º | 2.º | 3.º | Fuente |
|---|---|---|---|---|
| Encuesta de fans japonesa, 4.ª edición (la última) | **Askeladd** (39 votos) | Thorfinn (7) | Thorkell (4) | [rancolle](https://rancolle.com/ranking/uid21_1739280400) ⚠️ pocos votos |
| TV Tropes (YMMV) | **Askeladd = «Ensemble Darkhorse»** | Thorfinn «divisivo» | Thorkell «Crazy Awesome» | [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/YMMV/VinlandSaga) ✅ |
| Favoritos de AniList | Thorfinn (22 329) | **Askeladd (16 588)** | Thorkell (3744) | [AniList](https://anilist.co/anime/101348) ✅ |
| Dibujos de fans (Danbooru, 510 de la serie) | Thorfinn (266) | **Askeladd (190)** | Bjorn y Canute (62) | [Danbooru](https://danbooru.donmai.us/posts?tags=vinland_saga) ✅ |
| Otros autores | Satoru Noda (*Golden Kamuy*) admira sobre todo a **Askeladd** | | | [entrevista traducida](https://threadreaderapp.com/thread/1147322332450394112.html) ✅ |
| Premios | Thorfinn, nominado a **Mejor Personaje Principal** en los Crunchyroll Anime Awards 2024 | | | [Wikipedia](https://en.wikipedia.org/wiki/4th_Crunchyroll_Anime_Awards) ✅ |

**Cómo leerlo**:

- Askeladd **muere en el episodio 24**, al final de la temporada 1, y aun
  así junta **el 74 % de los favoritos de Thorfinn**, que sale en los 48
  episodios. Gana la encuesta japonesa más reciente y TV Tropes lo nombra
  el secundario que se roba la serie.
- Thorfinn es el más dibujado y el más votado en AniList, pero **divide**:
  una parte del fandom lo prefería vengador y no aceptó su giro pacifista.
- Thorkell es el tercero fijo en todas las medidas.
- ⚠️ No hay **encuesta oficial de personajes** de Kodansha con resultados
  publicados. Sí hay una **votación oficial de mejores escenas** (2022,
  [vinlandsaga.jp](https://vinlandsaga.jp/special/best-scene/)).
- ⚠️ No se encontró encuesta hispana de personajes.

**Para la lámina**: Askeladd es la apuesta más segura como personaje
(concepto 1). Thorfinn cuenta el tema (concepto 2). Thorkell es la
alternativa si hace falta humor bruto o acción.

---

## 10 · Doblaje latino y frases textuales

**Hay dos doblajes latinos distintos.** El fandom los compara todo el
tiempo: cualquier frase de la lámina tiene que decir de cuál sale.

### Ficha de producción

| | **Netflix** (T1 y T2) | **Crunchyroll** (sólo T2) |
|---|---|---|
| Estudio | **Audiomaster Candiani**, Ciudad de México (parte grabada en Mérida, Canadá y Córdoba, Argentina) | **Haymillian México** (TransPerfect Media México), Cuernavaca |
| Dirección | **Eduardo Garza** | **Alejandro Eguiza** y **Julio Gómez** |
| Traducción y adaptación | Axel Contreras (T1), Edson Gutiérrez (T2); adapta Jaime Chaparro; control de calidad Rodolfo Olivares | Adapta Elizabeth Hernández; mezcla Claudia Álvarez |
| Estreno | 2021-2023 en Latinoamérica | En simultáneo con Japón desde el 30-ene-2023 |
| Fuente | [Doblaje Wiki (API)](https://doblaje.fandom.com/es/wiki/Vinland_Saga) ✅ | Doblaje Wiki + [ANMTV](https://x.com/ANMTVLA/status/1620231139788034048) ✅ |

- Doblaje Wiki la pone en la categoría **«Doblaje con groserías»**: el
  doblaje mexicano no suaviza el lenguaje del original ✅.
- ⚠️ **Prime Video la tiene con un doblaje hecho con inteligencia
  artificial**, sin actores (Doblaje Wiki). El dueño no quiere nada que
  «parezca hecho por IA»: **no usar ese audio**.
- Dato de Doblaje Wiki: **Lalo Garza lloró con los finales de las dos
  temporadas** ⚠️ (una fuente).

### Reparto (cada nombre en dos fuentes)

| Personaje | Seiyū | Netflix | Crunchyroll T2 | Estado |
|---|---|---|---|---|
| **Thorfinn** | Yūto Uemura | **Eduardo «Lalo» Garza** (T1 y T2) | **Víctor Tabarez** | ✅ Garza: Doblaje Wiki + su [short de YouTube](https://www.youtube.com/shorts/CPGyL1I3KAU). Tabarez: [su ficha](https://doblaje.fandom.com/es/wiki/V%C3%ADctor_Tabarez) + [YouTube](https://www.youtube.com/watch?v=8NMEImNq69M) |
| Thorfinn niño | Shizuka Ishigami | **Desireé González** (T1), Israel Salazar (T2) | — | ✅ Doblaje Wiki + AniList (González) |
| **Askeladd** | Naoya Uchida | **Dafnis Fernández** (T1 y T2) | **Aldo Ramírez** | ✅ Fernández: Doblaje Wiki + AniList. Ramírez: Doblaje Wiki + [ANN](https://www.animenewsnetwork.com/encyclopedia/people.php?id=200711) |
| Askeladd joven | Maki Kawase | Liliana Barba (ep. 17 y 22) | — | ✅ Doblaje Wiki |
| **Canute** | Kenshō Ono | **Diego Becerril** (T1 y T2) | **Luba Flores** | ✅ Becerril: Doblaje Wiki + AniList. Flores: tabla y «Datos de interés» de Doblaje Wiki |
| **Einar** | Shunsuke Takeuchi | **Diego Estrada** | **Jonathan Miranda** (@Locutor_MX) | ✅ Estrada: Doblaje Wiki + su ficha. Miranda: Doblaje Wiki + ANMTV |
| Thorkell | Akio Ōtsuka | Idzi Dutkiewicz (T1), Bernardo Rodríguez (T2) | — | ✅ Doblaje Wiki + AniList |
| Thors (y el Narrador en T2) | Kenichirō Matsuda | Dan Osorio (T1), Bismarck Martínez (T2) | — | ✅ |
| Ylva | Hitomi Nabatame | Rebeca Gómez (T1), Karen Hernández (T2) | — | ✅ |
| Leif | Yōji Ueda | José Luis Orozco (T1), Lenin Venosa (T2) | — | ✅ |
| Ragnar | Jin Urayama | Óscar Rangel (T1), Luis Eduardo Fink (T2) | — | ✅ |
| Willibald | Satoshi Hino | Yamil Atala | — | ✅ |
| Rey Sweyn | Takayuki Sugō | **Humberto Vélez** (T1, la voz latina de Homero Simpson), Mario Hernández (T2) | — | ✅ |
| Arnheid | Mayumi Sako | Danann Huicochea | Valeria Tavera | ⚠️ sólo Doblaje Wiki |

- **Canute en Crunchyroll** lo dobla **Luba Flores**, mujer trans, igual
  que en inglés (Jessie James Grelle). Doblaje Wiki lo cuenta como dato
  positivo, **no es un chiste** ✅.
- Otros nombres sólo en AniList (que mezcla España y Latinoamérica) ⚠️:
  Bjorn Ulises Zavala, Helga Cony Madera, Halfdan Carlos Segundo, Mimi
  Sergio Morel, Floki Humberto Solórzano, Ari José Antonio Macías, Asgeir
  Armando Coria, Atli Roberto Mendiola, Torgrim Héctor Estrada,
  Gratianus Gerardo Vásquez.
- Sólo en Doblaje Wiki (T2, Crunchyroll) ⚠️: Emma Laura Becerril, Lotta
  Denisse Leguizamo, Eadric Víctor Covarrubias, hijo de Eadric Emiliano
  Venosa.

### Frases textuales del doblaje latino (Netflix)

Transcritas con `voz.py` (Whisper) y revisadas a oído. Whisper escribe
«Dorfin»: es «Thorfinn».

| Quién | Frase | Clip y minuto |
|---|---|---|
| **Thors** a Thorfinn niño (ep. 2) | «**Pon atención, Thorfinn. No tienes enemigos... Nadie tiene enemigos. Nadie en este mundo merece ser herido.**» | [«Nadie tiene enemigos»](https://www.facebook.com/VinlandSagaLatam/videos/nadie-tiene-enemigos-vinland-saga-espa%C3%B1ol-latino/542457653772935/?t=65), 1:05-1:25 ✅ |
| **Thors** (ep. 2) | «**Quieres una espada, Thorfinn... son para matar personas. Piénsalo bien: ¿a quién quieres matar?**» | mismo clip, [0:37-0:45](https://www.facebook.com/VinlandSagaLatam/videos/nadie-tiene-enemigos-vinland-saga-espa%C3%B1ol-latino/542457653772935/?t=37) ✅ |
| **Askeladd** a Thorfinn niño (ep. 22) | «**Es un paraíso donde nadie envejece ni muere, la tierra prometida... Si existe ese ancestro y vive en un lugar así, ¿por qué querría volver a un mundo como éste?**» | [«La infancia de Askeladd y la leyenda de Artorius»](https://www.facebook.com/VinlandSagaLatam/videos/la-infancia-de-askeladd-y-la-leyenda-de-artorius-vinland-saga-t1ep22-doblaje-lat/1012395204836119/?t=172), 2:52-3:43 ✅ |
| **Thorfinn** (T2 ep. 1) | «**¡Ven!**» (tras una escena muda, sólo música) | [«Thorfinn y Einar se encuentran»](https://www.facebook.com/VinlandSagaLatam/videos/vinland-saga-ha-regresado-thorfinn-y-einar-se-encuentran-ep1-temporada-2/5631142283607789/?t=156), 2:36 ✅ |

**Frases en subtítulo español** (no doblaje), del tráiler T2 en Dailymotion:

- Einar: «Eran bestias, monstruos con aspecto humano» / «Esta vez
  protegeré a mis hijos de la tormenta que son los adultos»
  ([0:39](https://www.dailymotion.com/video/x8h1n5b?t=39)).
- «No pasaré el resto de mi vida en el fin del mundo»
  ([0:58](https://www.dailymotion.com/video/x8h1n5b?t=58)).
- «Estoy buscando al hijo de un amigo al que convirtieron en esclavo»
  (Sverkel buscando a Thorfinn ⚠️ por trama, 1:20).
- «Necesitarás más cadáveres para llegar a lo más alto»
  ([2:02](https://www.dailymotion.com/video/x8h1n5b?t=122)).

### Cómo suenan (medido con `voz.py`, Whisper + Praat)

- **Askeladd (Dafnis Fernández)**: 104 Hz de media (**grave**), rango de
  27,7 semitonos (**muy expresivo**), 2,55 palabras por segundo
  (normal). Calmado, nunca grita, con inflexiones para intimidar o para
  el sarcasmo ✅.
- **Thors y Thorfinn niño (Dan Osorio, Desireé González)**: 186 Hz de
  media, 30 semitonos, **1,31 palabras por segundo**: lento, con silencios
  largos, solemne ⚠️ (mezcla las dos voces).

### Lo que falta

- ⚠️ **No hay clips oficiales doblados en YouTube** descargables desde
  aquí: los tres salen de la página de Facebook «Vinland Saga
  Latinoamérica», que sube clips del doblaje de Netflix.
- ⚠️ **Ninguna frase del doblaje de Crunchyroll** transcrita.
- ⚠️ Doblaje Wiki **no tiene muestras de audio** de esta serie.

---

## 11 · Música y sonido

### Openings y endings (cada uno en dos fuentes)

| Tema | Artista | Episodios | Estreno | Estado |
|---|---|---|---|---|
| OP1 **«MUKANJYO»** (無感情) | Survive Said The Prophet | 1-12 | 21-ago-2019 | ✅ [wiki](https://vinlandsaga.fandom.com/wiki/MUKANJYO) + **mirado entero** (90 s; el título sale en pantalla en el 0:33) |
| OP2 **«Dark Crow»** | MAN WITH A MISSION | 13-24 | 23-oct-2019 | ✅ [wiki](https://vinlandsaga.fandom.com/wiki/Dark_Crow) |
| OP3 **«River»** | Anonymouz | 25 en adelante (T2) | 15-feb-2023 | ✅ [wiki](https://vinlandsaga.fandom.com/wiki/River) |
| ED1 **«Torches»** | Aimer | 1-12 | 14-ago-2019 | ✅ [wiki](https://vinlandsaga.fandom.com/wiki/Torches) + **mirado entero** por storyboard |
| ED2 **«Drown»** | milet | 13-24 | 4-nov-2019 | ✅ [wiki](https://vinlandsaga.fandom.com/wiki/Drown) |
| ED3 **«Without Love»** | LMYK | 25 en adelante | 1-mar-2023 | ✅ [wiki](https://vinlandsaga.fandom.com/wiki/Without_Love) |

**Qué ambiente dan**:

- **MUKANJYO** (rock duro): mar en tormenta y el logo rojo sangre
  (0:03-0:09), barcos en la niebla, la infancia en Islandia, la banda de
  mercenarios y el campo de cadáveres bajo las estrellas (1:24). La
  escala épica y cruda en minuto y medio.
- **Torches** (Aimer, calmado): un barco entre fiordos nevados al
  atardecer con un niño rubio mirando; aurora verde sobre el mar; una
  silueta de niño con una **antorcha** subiendo una montaña en tormenta;
  al final, luz blanca y **un trigal dorado**. De la crudeza a un recuerdo
  cálido y de esperanza.

### Banda sonora y equipo de sonido

- **Compositor: Yutaka Yamada** (やまだ豊) ✅ (wiki del anime + ficha de
  equipo de AniList en `datos-texto.md`). Siguió en la T2 según la wiki.
- **Director de sonido**: Shouji Hata. **Efectos de sonido**: Takuya
  Hasegawa (AniList) ✅.
- Álbum de la banda sonora publicado el **19-feb-2020**
  ([Wikipedia: Music of Vinland Saga](https://en.wikipedia.org/wiki/Music_of_Vinland_Saga)).
- **Qué suena en las escenas emotivas** ⚠️: los fans llaman «Thors vs
  Askeladd fight theme» al tema del duelo de Thors, y la T2 tiene un
  «Thorfinn's Theme» para sus momentos de redención. Son nombres de fans,
  no del disco.
- El **reencuentro con Einar** va con **música orquestal y casi sin
  palabras** ✅ (clip mirado).

### Efectos y onomatopeyas

- **Manga**: onomatopeya **ゴオォォ** («gooo», un rugido) a pincel sobre
  Jomsborg de noche, cap. 146 (hoja `fondos_01.jpg` #7) ⚠️ una viñeta.
- ❌ **Anime**: no se encontró ninguna lista de efectos de sonido que el
  público reconozca (la wiki no tiene página; búsquedas «sound effect» y
  «onomatopoeia» sin resultado).

---

## 12 · Vídeos y tendencias

| Vídeo | Qué es | Minuto útil | Estado |
|---|---|---|---|
| [Tráiler oficial T2](https://www.dailymotion.com/video/x8h1n5b) (FilmAffinity, 2:20, subtítulos en español; igual que [el de 3djuegos](https://www.dailymotion.com/video/x8p41mq)) | Mirado entero, 97 planos | 0:03 cartela del autor; 0:19 Einar a contraluz; 0:39 aldea en llamas; 1:17 puerto; 1:31 tocón; 1:42 puñetazo; 2:02 castillo; 2:16 cartela final | ✅ |
| [OP1 «MUKANJYO»](https://www.dailymotion.com/video/x8bcl5n) (repost de MGG Spain, 1280×720) | Mirado entero, 31 fotogramas | 0:27, 0:45, 0:51, 1:00, 1:15, 1:24 | ✅ |
| [ED1 «Torches»](https://www.youtube.com/watch?v=rlb942EnOF0) (sin créditos, 90 s) | Storyboard completo | ver §11 | ✅ ⚠️ baja resolución |
| [Muerte de Askeladd](https://www.youtube.com/watch?v=PF2NTT_mnps) (Crunchyroll, 180 s) | Clip oficial | ver §2 | ✅ |
| [Discurso de Canute](https://www.youtube.com/watch?v=Zt85YuG0-_Y) (Netflix Anime, 184 s) | Clip oficial | ver §2 | ✅ |
| [Einar llega a la granja](https://www.youtube.com/watch?v=Zk4Iy5PBsOw) (Netflix Anime, 99 s) | Clip oficial, con subtítulo automático en español | 0:00-0:03, ~0:31, ~1:16 | ✅ |
| [Canute despierta](https://www.youtube.com/watch?v=rsZc66_fisM) (170 s) | Clip de terceros: Canute en la nieve con capa roja, subtítulo «Isn't there any way to end the suffering from your punishment other than death?» | todo el clip | ⚠️ |
| [PV5, tráiler japonés oficial](https://www.youtube.com/watch?v=5xqEp7R9SYM) (105 s) | Enlazado desde AniList | — | ⚠️ **no se pudo mirar** (403) |
| [Edit vertical tipo TikTok](https://www.dailymotion.com/video/x8rnpp0) (Toxic-dj, 52 s) | Primeros planos muy cerrados, cortes al ritmo, subtítulos en inglés | todo | ⚠️ no se encontró el TikTok original |
| [Lalo Garza: «¿Qué opino sobre Vinland Saga?»](https://www.youtube.com/shorts/CPGyL1I3KAU) (2025) | El actor de Thorfinn en Netflix habla de la serie | — | ✅ |
| [@fandoblajes en TikTok](https://www.tiktok.com/@fandoblajes/video/7291264804713450758) | Compara el doblaje de Netflix y el de Crunchyroll: «¿Cuál es el mejor doblaje?» | — | ✅ |

**Tendencias** (de los títulos de hilos de
[r/VinlandSaga](https://www.reddit.com/r/VinlandSaga/comments/1anap1l/this_is_why_i_love_gigguk_i_knew_he_would_have/)):
el youtuber **Gigguk** puso la T2 como su número 1 del año; y un hilo
entero sobre cómo **Yukimura pone el énfasis en los ojos** de los
personajes.

**Otros en Dailymotion** (del recolector, sin mirar ⚠️): tráiler de la T2
de Vidaextra (51 793 vistas, [x8llc9a](https://www.dailymotion.com/video/x8llc9a)),
tráiler alemán de MeinMMO, tráileres en inglés de BetaSeries, «la fin du
manga Vinland Saga !» (Nasspassion) y «L'opening Incroyable de Vinland
Saga» (Berserk3r, 0:54).

⚠️ **Making of en vídeo**: no apareció en Dailymotion ni Internet Archive
(búsquedas «Vinland Saga making of», «staff interview video»). El making
of escrito está en §19.

---

## 13 · Videojuegos de la franquicia

- **No existe ningún videojuego oficial** de Vinland Saga, en ninguna
  plataforma ✅ (dos fuentes: búsqueda web específica, que sólo da juegos
  de fans en Roblox, un proyecto en GitHub y una demo en Unity Play, sin
  licencia; y Steam, vacío en `datos-texto.md`).
- **No confundir**: «Dead in Vinland» es un juego francés de gestión, de
  otro estudio, **sin relación** con esta obra.
- **No usar los juegos de fans** como referencia de interfaz.
- Lo más cercano: el **cómic cruzado con *Assassin's Creed Valhalla***,
  dibujado por el propio Yukimura (§24).
- Aparte: existe un **juego de mesa «Vinland Saga 01»** de Millennium
  Games ⚠️ (no investigado a fondo)
  ([tienda](https://shop.millenniumgames.com/products/vinland-saga-01)).
- AniList enlaza también un ONA llamado **«Ponkotsuland Saga»** como obra
  relacionada ⚠️ (no investigado).
- **Si la lámina necesita una caja «de juego»**, hay que inventarla
  coherente con §7: cartela negra con serif blanca o texto sobre madera.
  No copiar un juego de fans.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### Lo que ama

- **«Un verdadero guerrero no necesita espada»** (Thors, cap. 15): la
  frase más citada. Está en camisetas
  ([Redbubble](https://www.redbubble.com/i/t-shirt/Copia-de-Vinland-Saga-True-Warrior-Needs-no-Sword-by-GambaShop/155713482.FB110)),
  tuits fijados y es la filosofía que Thorfinn tarda toda la serie en
  entender ✅.
- **«No tienes enemigos» / «Nadie tiene enemigos»**: la otra frase-símbolo.
  En el fandom hispano hay hasta un fandub titulado así (§23) ✅.
- **Los ojos de Thorfinn**: grandes de niño, muertos en la venganza,
  grandes otra vez al final. Miles de posts «Thorfinn eyes» en Pinterest
  y TikTok ✅
  ([TV Tropes, personaje](https://tvtropes.org/pmwiki/pmwiki.php/Characters/VinlandSagaThorfinn)).
- **Askeladd**: el fandom lo prefiere muchas veces a Thorfinn. Su final
  ante el rey (ep. 24) es de lo más compartido.
- **El dúo de cada arco** (Facebook hispano, §8).
- En Reddit: «Heroes and Villains has same origin story but different
  ways to handle» (42 votos): Thorfinn y Askeladd salen del mismo dolor y
  eligen distinto ([hilo](https://www.reddit.com/r/VinlandSaga/comments/14mwg8u/heroes_and_villains_has_same_origin_story_but/)).
- ⚠️ No hay un meme o chiste interno **propio del fandom hispano** más allá
  de comparar los dos doblajes.

### Qué NO hacer (lo que a un fan le parecería falso)

1. **No dibujar a Thorfinn con ojos grandes y brillantes en una escena del
   arco de la venganza.** Ahí tiene la mirada entrecerrada y vacía. Es el
   error visual más notorio ⚠️ (deducido del motivo, no hay una regla
   escrita).
2. **Nada de paleta alegre ni estética *chibi* o cómica.** Es un seinen
   histórico, violento y realista. El encargo pide «Inglaterra del siglo
   XI, paisajes y crudeza».
3. **No confundir los dos doblajes**: Lalo Garza (Netflix) y Víctor
   Tabarez (Crunchyroll) son personas distintas.
4. **No tratar la voz de Canute en Crunchyroll como chiste** (Luba
   Flores, mujer trans).
5. **No meter acción donde la T2 es lenta a propósito.** La T2 (granja)
   decepcionó al principio a quien quería batallas, pero la crítica y los
   lectores la defienden como la mejor parte ✅
   ([Epicdope](https://www.epicdope.com/is-vinland-saga-season-2-bad-why-are-fans-displeased/)).
6. **No usar globo blanco de cómic** (§7).
7. **No confundirla con «Dead in Vinland»** ni con otros juegos
   vikingos.
8. **No usar el doblaje con IA de Prime Video.**
9. **No repetir la lámina de Attack on Titan** (papel sucio con cinta
   roja, §25).

---

## 15 · Poses analizadas por personaje

Salen de lo mirado (OP1 y tráiler en 1280×720; clips por storyboard) y de
las hojas. «Sirve para» usa los verbos del encargo.

### Askeladd (6 + 1 de la hoja)

| # | Dónde | Postura, manos, mirada, gesto | Sirve para |
|---|---|---|---|
| 1 | hoja `personajes_01.jpg` #17 (diseño oficial) | De pie, **espada apoyada en el hombro**, cuerpo entero, peso en una pierna | **Presentar** |
| 2 | ep. 24, [clip](https://www.youtube.com/watch?v=PF2NTT_mnps) | Banda roja en la frente, ojo entrecerrado, gesto gruñón mientras dice «this part is important» | **Explicar**, instruir |
| 3 | tráiler T2, [1:21](https://www.dailymotion.com/video/x8h1n5b?t=81) | En primera fila de un grupo de mercenarios, espada en alto, mirada al frente | **Presentar** a un líder ⚠️ puede no ser él |
| 4 | ep. 24, mismo clip | Tendido, ensangrentado, sostenido por otro; cara relajada | Despedida, sacrificio |
| 5 | [clip 1nRt6tiU20g](https://www.youtube.com/watch?v=1nRt6tiU20g) | Cara y pelo con sangre, bandana torcida, ojos muy abiertos, gritando | Horror, dolor ⚠️ escena sin identificar |
| 6 | mismo clip | Un solo ojo muy abierto en la oscuridad | Miedo antes de actuar |
| 7 | mismo clip | Boca abajo, cara de perfil con sangre, junto a una figura pequeña tendida | Escena dura ⚠️ contexto sin confirmar |

### Thorfinn (7)

| # | Dónde | Postura, manos, mirada, gesto | Sirve para |
|---|---|---|---|
| 1 | OP1, [0:27](https://www.dailymotion.com/video/x8bcl5n?t=27) | Primer plano de niño, ojos muy abiertos, manto de piel oscura, viento en el pelo | Reaccionar con miedo |
| 2 | OP1, [0:45](https://www.dailymotion.com/video/x8bcl5n?t=45) | Primer plano cerrado, mirada fija a cámara, dientes apretados | **Pensar**, decidirse |
| 3 | OP1, [0:51](https://www.dailymotion.com/video/x8bcl5n?t=51) | De espaldas, corriendo por la nieve hacia una casa, brazos en movimiento | **Animar** (dinamismo) |
| 4 | tráiler T2, [1:42](https://www.dailymotion.com/video/x8h1n5b?t=102) | Recibe un puñetazo sin devolverlo, cuerpo hacia atrás, brazo cruzado sobre la cara | **Explicar** su pacifismo |
| 5 | tráiler T2, [1:31](https://www.dailymotion.com/video/x8h1n5b?t=91) | Tira de una cuerda atada a un tocón, músculos tensos, cabeza gacha | Trabajar, perseverar ⚠️ puede ser Einar |
| 6 | ep. 4, [clip](https://www.youtube.com/watch?v=LPnQ74j1dqY) | Niño, ojos muy abiertos, boca entreabierta, mirando arriba con horror | La escena que hace llorar |
| 7 | ep. 24, [clip](https://www.youtube.com/watch?v=PF2NTT_mnps) | Joven rubio llorando, manos temblorosas sosteniendo a Askeladd | Culpa ⚠️ puede ser Canute |

Además: la **hoja de diseño de color de Thorfinn granjero** (artbook) da
de frente, de espalda y 12 caras; el fondo de fans **wallhaven-lmddyq**
lo muestra **de espaldas con capa mirando el amanecer** (pensar).

### Canute (6)

| # | Dónde | Postura, manos, mirada, gesto | Sirve para |
|---|---|---|---|
| 1 | [discurso](https://www.youtube.com/watch?v=Zt85YuG0-_Y) | De pie, capa roja real, viento en el pelo corto, mirando el horizonte sobre el mar al atardecer | **Presentar** con autoridad |
| 2 | mismo clip | Primer plano, cara girada, fría, ceño fruncido | **Regañar**, imponerse |
| 3 | tráiler T2, [1:10](https://www.dailymotion.com/video/x8h1n5b?t=70) | Cara a cara con un hombre mayor, puño cerrado | Explicar, confrontar |
| 4 | [clip rsZc66_fisM](https://www.youtube.com/watch?v=rsZc66_fisM) | De pie en la nieve, capa roja, mirando a un hombre mayor de barba gris | Pedir compasión, cuestionar una orden |
| 5 | mismo clip | Primer plano, ojos muy abiertos, boca entreabierta, mirando abajo a un hombre herido | Angustia |
| 6 | mismo clip | Solo, de espaldas en un campo nevado con árboles secos, pelo largo sobre la capa | **Pensar**, estar a solas |

### Einar (6)

| # | Dónde | Postura, manos, mirada, gesto | Sirve para |
|---|---|---|---|
| 1 | tráiler T2, [0:19](https://www.dailymotion.com/video/x8h1n5b?t=19) | Silueta a contraluz entre humo y fuego rojo, un brazo alzado | Narrar su pasado (voz en off) |
| 2 | tráiler T2, [0:39](https://www.dailymotion.com/video/x8h1n5b?t=39) | Niño llorando a gritos en la aldea en llamas | La escena que hace llorar |
| 3 | tráiler T2, [1:31](https://www.dailymotion.com/video/x8h1n5b?t=91) | De espaldas, tirando de la cuerda | Trabajar ⚠️ puede ser Thorfinn |
| 4 | [clip Netflix](https://www.youtube.com/watch?v=Zk4Iy5PBsOw), ~0:14 | Primer plano, mira arriba, boca cerrada, cejas fruncidas | Cautela ante alguien nuevo |
| 5 | mismo clip, ~0:31 | Lágrima, mirada de reojo, mandíbula tensa | Tristeza silenciosa |
| 6 | mismo clip, ~1:16 | Ojos muy abiertos, cejas arriba, boca entreabierta | Sorpresa |

### Thors (2)

- OP1, [1:15](https://www.dailymotion.com/video/x8bcl5n?t=75): **contrapicado
  heroico**, cicatrices, sangre en la túnica → **presentar**.
- Clip ep. 2, 1:58-2:04: **arrodillado a la altura de una niña** (Ylva)
  para despedirse → **explicar** con calma a alguien pequeño.

### Resumen: qué pose para qué

| Para… | La mejor |
|---|---|
| **Presentar** | Askeladd con la espada al hombro (#17 de la hoja); Canute en el discurso; Thors en contrapicado (OP1 1:15) |
| **Explicar** | Askeladd, «this part is important» (ep. 24); Thors arrodillado (ep. 2) |
| **Celebrar** | ⚠️ **ninguna**: la serie casi no celebra. Lo más cercano: Thorkell riéndose al frenar un ejército (ep. 9-10, sin fotograma) |
| **Regañar** | Canute frío (discurso); Thors serio (ep. 2, 0:53-1:52) |
| **Pensar** | Canute solo en la nieve; Thorfinn de espaldas al amanecer; Thorfinn OP1 0:45 |
| **Animar** | Thorfinn niño corriendo (OP1 0:51); el «¡Ven!» del reencuentro (T2 ep. 1, 2:36) |

---

## 16 · Vestuario, con hex medidos

Hex de `estilo.py --colores 6` sobre hojas de diseño oficiales (no fan
art). Si el fondo pesa en la medida, lo aviso.

| Personaje | Ropa por arco | Hex medidos | Fuente |
|---|---|---|---|
| **Thorfinn** | **Guerra** (niño soldado, 1013-1014): capa con capucha y **ribete de piel oscura**, cuero ajustado. **Esclavo**: ropa sencilla. **Vinlandia** (27 años): **túnica con capucha caqui**, polainas envueltas, cinturón con funda de daga. Siempre **dos cuchillos**. Pelo corto y despeinado; se lo peina hacia atrás antes de ir a Vinlandia | `#BAA16E` capucha caqui, `#E4CCAD` luces crema, `#7E6A46` sombra, `#443A2D` línea | [hoja de color del artbook](https://static.wikia.nocookie.net/vinlandsaga/images/9/94/AnimationWorksPreview_Thorfinn.png) + [wiki, Appearance](https://vinlandsaga.fandom.com/wiki/Thorfinn#Appearance) ✅ |
| **Askeladd** | Niño: ropa raída, descalzo, cubierto de ceniza. Adulto: **coraza de cuero sin mangas con hombreras de metal** sobre túnica de manga larga; en el diseño del anime, **coraza negra, faldón beige y botas marrones** (hoja #17). Pelo **rubio ondulado a la altura del mentón**, **perilla**. Al final, **banda roja en la frente** (ep. 24) | `#6D5B42`, `#D9C08D` (túnica) ⚠️ fondo negro en la medida | [hoja del artbook](https://static.wikia.nocookie.net/vinlandsaga/images/c/c7/AnimationWorksPreview_Askeladd.png) + wiki ✅ |
| **Canute** | T1: **pelo rubio largo**, capa roja con piel. T2 (rey): **pelo corto tipo melena corta**, perilla, **cicatriz bajo el ojo izquierdo** (se la hizo Thorfinn), capa y **diadema** casi siempre | T1 `#9C403B` (túnica rojiza), T2 `#B46746` (capa terracota) | [diseño T1](https://static.wikia.nocookie.net/vinlandsaga/images/a/a6/Canute_anime_design.png), [diseño T2](https://static.wikia.nocookie.net/vinlandsaga/images/d/db/Canute_S2_anime_design.png) ✅ |
| **Einar** | Alto, **pelo castaño rojizo**, ojos marrones en el manga y **azules en el anime**, **lunar a la izquierda del puente de la nariz**, musculoso. **Camisa verde** | `#7A7646` (camisa verde) | [diseño T2](https://static.wikia.nocookie.net/vinlandsaga/images/7/74/Einar_S2_anime_design.png) + [wiki](https://vinlandsaga.fandom.com/wiki/Einar#Appearance) ✅ |
| **Jomsvikings** | **Capa blanca**, **escudo rojo y amarillo**, **hacha de un filo con un ojo grabado** | — | [wiki: Jomsvikings](https://vinlandsaga.fandom.com/wiki/Jomsvikings) ✅ |
| **Thorkell** | ⚠️ no se midió su armadura | — | — |

**La ropa «icónica»** que todo fan reconoce: la **capucha caqui de
granjero de Thorfinn** y **sus dos cuchillos** (key visual de la T2 y
portada del artbook) ✅.

**Etiquetas que más se repiten al dibujarlos** (Danbooru, vocabulario de
las IA de imagen, `datos-imagen.md`):

- Thorfinn: blonde_hair, short_hair, brown_eyes, knife, dagger,
  **dual_wielding**, **reverse_grip**, fur_trim, capelet, hood, tunic,
  viking.
- Askeladd: blonde_hair, short_hair, beard, **goatee**, blue_eyes,
  mature_male, sword, armor, smile, **aquiline_nose**, viking.
- Canute: blonde_hair, blue_eyes, long_hair, **androgynous**, scar,
  scar_on_face, fur_trim, headband, cloak.
- Einar: brown_hair, short_hair, **thick_eyebrows**, **green_shirt**,
  blue_eyes, muscular, blush.

**Cosplay de Thorfinn** (guía de [Carbon Costume](https://carboncostume.com/thorfinn-from-vinland-saga/)
⚠️): peluca rubia despeinada, ribete de piel marrón, túnica beige,
cinturón con hebilla plateada, daga de utilería.

---

## 17 · Paisajes y fondos de pantalla

### Los sitios de la serie

| Sitio | Luz y hora | Referencia |
|---|---|---|
| **Islandia** (infancia) | Invierno, blanco frío de día; aurora de noche | [Iceland](https://static.wikia.nocookie.net/vinlandsaga/images/f/f2/Iceland%282%29.jpg) (1024×488), OP1 0:51 y 1:00 |
| **Inglaterra y Gales** (guerra) | Praderas verdes de día; castillos con fuego y relámpagos de noche | mapas de [Gales](https://static.wikia.nocookie.net/vinlandsaga/images/d/d9/Wales.png) (1584×1304), OP1 0:27, tráiler 2:02 |
| **Granja de Ketil** (esclavitud) | Mediodía en el bosque, verde oscuro y piel al sol | tráiler 1:31 ⚠️ la página de la wiki **no tiene ninguna imagen** |
| **Jomsborg** (base jomsvikinga) | Fuerte circular junto al agua; de noche con fuegos | manga, caps. 130, 138 y 146 ([cap. 130](https://static.wikia.nocookie.net/vinlandsaga/images/a/a4/Chapter_130_Screenshot.PNG), 1115×808) |
| **El mar** | Tormenta (OP1), atardecer entre fiordos (ED1), aurora de noche | OP1 y ED1 |
| **Casa larga** | Interior de madera oscura con el fuego como único foco; por fuera, nevada | artbook «Scenery» (hoja `fondos_01.jpg` #9) |
| **Puerto vikingo** | Día nublado, agua turbia, muelles de madera | tráiler 1:17 |
| **Vinlandia** (Isla del Príncipe Eduardo, «Epekwitk» en mi'kmaq) | Bosque, colonos y nativos | tomo 27; mapa del opening |
| **Markland** | — | un mapa en la wiki |

Categoría de lugares de la wiki: Iceland, Jomsborg, Markland, Vinland,
Wales, Arnheid Village ([Category:Locations](https://vinlandsaga.fandom.com/wiki/Category:Locations)) ✅.

### Fondos de pantalla (Wallhaven, aptos, 1920×1080 o más)

| Tamaño | ♥ | Qué es | Autor | Enlace |
|---|---|---|---|---|
| 3840×2160 | 143 | Brazo encadenado con espada, gris | mushit | [6d5zgl](https://w.wallhaven.cc/full/6d/wallhaven-6d5zgl.jpg) |
| 1920×1080 | 101 | Espada, blanco y negro de manga | nidko8 | [poj76e](https://w.wallhaven.cc/full/po/wallhaven-poj76e.png) |
| 4096×2340 | 54 | Thorfinn con globo en inglés, manga | theflyboy667 | [1pzgl1](https://w.wallhaven.cc/full/1p/wallhaven-1pzgl1.png) |
| 1920×1080 | 51 | Ruinas de noche con luna | Nemr0d | [q6oor5](https://w.wallhaven.cc/full/q6/wallhaven-q6oor5.png) |
| 1920×1080 | 50 | Reflejo en el agua, cielo | TankerNejla | [1pgjzg](https://w.wallhaven.cc/full/1p/wallhaven-1pgjzg.png) |
| 1920×1080 | 38 | Ruinas, colinas, mañana (columna romana) | Nemr0d | [dgdd8j](https://w.wallhaven.cc/full/dg/wallhaven-dgdd8j.png) |
| 4096×2160 | 38 | Thorfinn con cuchillo, fondo liso | kazro | [w5dgr7](https://w.wallhaven.cc/full/w5/wallhaven-w5dgr7.jpg) |
| 1920×1080 | 37 | Thorfinn de espaldas al amanecer, Inglaterra | Nemr0d | [lmddyq](https://w.wallhaven.cc/full/lm/wallhaven-lmddyq.png) |
| 3000×2000 | 35 | Thorfinn, fondo liso | AlexisGt123 | [r26w8q](https://w.wallhaven.cc/full/r2/wallhaven-r26w8q.jpg) |
| 1920×1080 | 32 | Ruinas al amanecer | Nemr0d | [zm99pv](https://w.wallhaven.cc/full/zm/wallhaven-zm99pv.png) |
| 1920×1080 | 24 | Thorfinn con capucha y daga, fondo oscuro | DrPlaga049 | [2yjm2m](https://w.wallhaven.cc/full/2y/wallhaven-2yjm2m.png) |

**Lo que muestran**: los fondos más guardados son de **noche o
amanecer**, paleta fría y poco saturada, o **blanco y negro de manga**.

⚠️ **No se encontraron fondos de pantalla oficiales** del estudio o la
editorial (sólo de fans).

---

## 18 · Guía para generar con IA: imagen y texto

La escribe el redactor con los datos de §3 a §17. La IA **no inventa
referencias**: sirve para probar poses, fondos o luces, siempre partiendo
de las imágenes reales que se citan aquí.

### A. Para una IA de imagen (Firefly, Canva)

**1. Rasgos que nunca cambian**

| Personaje | Siempre | Nunca |
|---|---|---|
| **Askeladd** | Hombre maduro (33-44 años), **pelo rubio ondulado a la altura del mentón**, **perilla y barba corta**, **nariz aguileña**, ojos azules claros, **cejas gruesas con las puntas hacia arriba**, **sonrisa ladeada**; coraza de cuero oscura sin mangas con hombreras de metal, túnica de manga larga, espada | Gritando con la boca muy abierta (salvo de joven), armadura brillante de fantasía, pelo largo |
| **Thorfinn** (guerra, 16-18 años) | Rubio, **pelo corto y despeinado**, ojos marrones **entrecerrados, sin brillo**, ceño fruncido, **bajo de estatura**, capa corta con **ribete de piel oscura**, **dos dagas agarradas al revés** | Ojos grandes y brillantes, sonrisa, ropa limpia |
| **Thorfinn** (Vinlandia, adulto) | Rubio, **pelo peinado hacia atrás**, ojos abiertos y tranquilos, **túnica con capucha caqui** `#BAA16E`, polainas envueltas, cinturón con funda de daga | Armas en la mano, cara de rabia |
| **Thorfinn** (niño, 6-7 años) | Cara redonda, **ojos grandes y curiosos**, pelo bien peinado, ropa campesina de Islandia, manto de piel | Ojos muertos |
| **Canute** (T1) | **Pelo rubio largo y liso**, ojos azules grandes, **cara andrógina**, labios carnosos («pouty lips», wiki), **capa roja con ribete de piel** `#9C403B` | Barba, pose firme |
| **Canute** (rey, T2) | Pelo rubio **corto**, perilla, **cicatriz bajo el ojo izquierdo**, **diadema**, capa terracota `#B46746`, mirada fría | Sonrisa, lágrimas |
| **Einar** | Alto y musculoso, **pelo castaño rojizo corto**, **cejas gruesas**, ojos azules (anime), **lunar a la izquierda del puente de la nariz**, **camisa verde** `#7A7646` | Armas, armadura |

**2. Paleta** (medida, §5 y §16)

- Noche y aurora: `#131E35` `#1B3F7B` `#2895B6` `#34BAC6`; aurora verde `#329D5B`.
- Nieve de Islandia: `#F1F1EA` `#CED1D9` `#9DB1D0` `#48658B`.
- Interior con fuego y castillos: `#0B0907` `#241B0D` `#694630` `#B68C6E` `#DCBD9C`.
- Bosque de la granja: `#1B2616` `#263020` `#816541` `#EAC7A1`.
- Trigal (la única escena cálida): `#E8E74D` `#EFE68F` `#BDAB4B`.
- Regla: **frío y poco saturado** (saturación 13-40 %); el **fuego es la
  única luz cálida**.

**3. Línea, sombreado y luz** (§19)

- Línea **de grosor variable, como tinta a pincel**, oscura; en los
  paisajes casi no hay línea (degradado).
- Sombreado **pictórico**: 2-3 bandas suaves y degradados, no *cel-shading*
  plano y brillante.
- Luz **direccional y realista**: cielo nublado de día, luna o aurora de
  noche, fuego en interiores.

**4. Encuadre**

- **Planos generales muy abiertos** para la escala (barco entre témpanos,
  campo de cadáveres, fiordos).
- **Primeros planos muy cerrados** de cara y ojos para la emoción.
- **Contrapicado** para presentar a alguien imponente (Thors, OP1 1:15).
- **De espaldas mirando el paisaje** para pensar (Thorfinn al amanecer,
  Canute en la nieve).

**5. Palabras que ayudan** (en inglés, que es como mejor responden):

> Vinland Saga anime style, WIT Studio, 11th century Viking Age,
> historical seinen, muted earthy palette, painterly background art,
> realistic proportions, variable ink line weight, overcast Nordic light,
> snowy fjord, longhouse interior lit only by a hearth fire, fur-trimmed
> capelet, wool tunic, leather cuirass, dual daggers reverse grip,
> aurora over a dark sea, close-up on the eyes

Etiquetas tipo Danbooru que entienden bien: `viking`, `fur_trim`,
`capelet`, `tunic`, `dual_wielding`, `reverse_grip`, `goatee`,
`aquiline_nose`, `androgynous`, `scar_on_face`, `thick_eyebrows`,
`green_shirt`.

**6. Palabras que lo estropean**

> chibi, kawaii, moe, sparkles, glossy cel shading, neon, pastel candy
> colors, big shiny eyes (en el arco de la venganza), horned fantasy
> armor, speech bubble, comic balloon, clean vector outline

**7. Qué imágenes usar de referencia**

| Para | Imagen |
|---|---|
| Estilo y color de personaje | [Hoja de color de Thorfinn](https://static.wikia.nocookie.net/vinlandsaga/images/9/94/AnimationWorksPreview_Thorfinn.png) (artbook) |
| Pose de Askeladd | [Diseño del anime](https://static.wikia.nocookie.net/vinlandsaga/images/9/9b/Askeladd_anime_design.png) (hoja `personajes_01.jpg` #17) y [hoja del artbook](https://static.wikia.nocookie.net/vinlandsaga/images/c/c7/AnimationWorksPreview_Askeladd.png) |
| Grupo | KV3 T1 (hoja `arte_01.jpg` #3) |
| Fondos | Tableros «Scenery» del artbook (hoja `fondos_01.jpg` #9); OP1 1:00 y 1:24 |
| Barco | Vuelta del barco del artbook (hoja `fondos_01.jpg` #10) |
| Volumen 3D | figma Thorfinn; modelos de §4 |

El fan art (§4) **nunca** como referencia de estilo final: sólo para ver
cómo lo interpreta el fandom.

### B. Para una IA de texto (diálogos en su voz)

**1. Cómo habla cada uno**

| Personaje | Tono | Muletillas y forma | Puntuación |
|---|---|---|---|
| **Askeladd** | Calmado, irónico, grave. **Nunca grita** | Cuenta una historia o hace una pregunta antes de ir al grano. Se burla con suavidad. Habla de la gente como si la leyera por la cara | Frases medias, puntos; alguna pregunta retórica. **Sin exclamaciones** |
| **Thorfinn** (venganza) | Seco, cortante | Frases de dos a cinco palabras. No explica nada | Puntos. Alguna exclamación de rabia |
| **Thorfinn** (adulto) | Lento, pausado, sereno | Explica despacio, con pausas | **Puntos suspensivos**, frases cortas |
| **Thors** | Calma de padre, solemne | Preguntas que obligan a pensar: «Piénsalo bien» | Pausas largas (1,31 palabras por segundo) |
| **Canute** (rey) | Absoluto, frío | Habla en primera persona de su destino y de Dios | Frases firmes, sin dudas |
| **Canute** (príncipe) | Tembloroso | Frases cortadas | Puntos suspensivos |
| **Einar** | Directo, emocional, cálido | Dice lo que piensa sin filtro | Exclamaciones sinceras |
| **Thorkell** | Jovial, bruto | Se ríe; sólo quiere pelear | «Yo... sólo... quiero... pelear.» |

**Cómo exageran las emociones**: casi no las exageran. La serie **baja
el volumen**: la emoción fuerte va en **silencio y mirada** (el
reencuentro del T2 ep. 1 es mudo hasta el «¡Ven!»). Los gritos son para
la batalla. El doblaje de Netflix **usa groserías** («Doblaje con
groserías»); en la lámina, mejor sin ellas.

**2. Frases reales por emoción** (la fuente entre paréntesis)

- **Explicando**: «Pon atención, Thorfinn. No tienes enemigos... Nadie
  tiene enemigos. Nadie en este mundo merece ser herido.» (Thors,
  doblaje Netflix, ep. 2, 1:05). «Quieres una espada... son para matar
  personas. Piénsalo bien: ¿a quién quieres matar?» (Thors, ep. 2, 0:37).
  «Es un paraíso donde nadie envejece ni muere, la tierra prometida...»
  (Askeladd, ep. 22, 2:52).
- **Triste**: «Eran bestias, monstruos con aspecto humano.» / «Esta vez
  protegeré a mis hijos de la tormenta que son los adultos.» (Einar,
  subtítulo del tráiler T2, 0:39). «No pasaré el resto de mi vida en el
  fin del mundo.» (tráiler, 0:58).
- **Animando o alegre**: «¡Ven!» (Thorfinn, doblaje Netflix, T2 ep. 1,
  2:36). Últimas palabras de Askeladd: «You did well» / «Don't waste
  it» (subtítulo inglés del clip de Crunchyroll, ep. 24) ⚠️ sin versión
  latina transcrita.
- **Enfadado o duro**: «Necesitarás más cadáveres para llegar a lo más
  alto.» (tráiler, 2:02). «We did this.» / «You speak as though this was
  an act of nature, Gunnar.» (Canute rey, manga en inglés, hoja
  `personajes_01.jpg` #5) ⚠️ edición inglesa.
- **Presentarse**: «—¿Cómo te llamas? —Einar.» (subtítulo automático en
  español del clip de Netflix Anime, 0:00).
- **La frase-símbolo**: «Un verdadero guerrero no necesita espada.»
  (Thors, manga cap. 15, página 5). «No tengo enemigos, ninguno.»
  (Thorfinn adulto, arco final ⚠️ capítulo sin precisar).

**3. Vocabulario de la serie**

- **Vinlandia** (Vinland), **jomsvikingo**, **skræling** (así llaman los
  nórdicos a los nativos de Vinlandia), **«la maldición de la corona»**,
  **berserker**, «**el Troll de Jom**» (Thors), «**Cadena de Hierro**»
  (Halfdan), **Askeladd** = «el Muchacho Ceniciento», **Artorius**.
- Fechas como cartela: «Inglaterra, 1013 d.C.».

**4. Vocabulario de expresiones para la IA de imagen**

| Gesto | Cómo se dibuja en Vinland Saga |
|---|---|
| Inocencia | Ojos grandes, redondos, con brillo (Thorfinn niño) |
| Vacío, rencor | **Ojos entrecerrados sin brillo**, ceño fruncido («dead eyes») |
| Tensión | **Gota de sudor** y dientes apretados (manga, hoja #15) |
| Furia (T2) | **Líneas negras que cruzan la cara** (recurso de MAPPA) ⚠️ una fuente |
| Vergüenza | Sonrojo (`blush`, Einar con Arnheid) |
| Tristeza | Una sola lágrima, mandíbula tensa, mirada de reojo (Einar) |
| Emoción grande | No hay fondos de emoción de colores: la emoción la ponen **la luz y el paisaje** (aurora, trigal, lluvia de sangre roja del KV3) |
| *Chibi* | **No existe en la serie**: no usar |

---

## 19 · Estilo de dibujo, técnica, Blender y encuadres

### Quién la hizo

- **Anime** (AniList, `datos-texto.md`): director **Shūhei Yabuta**,
  guion **Hiroshi Seko**, diseño de personajes y director de animación
  jefe **Takahiko Abiru**, dirección de arte **Yūsuke Takeda**, diseño de
  color **Satoshi Hashimoto**, props **Tatsumori Imoto**, fotografía
  **Yūki Kawashita**, dirección de CG **Mayu Takehana**; diseñador 2D
  **Hirofumi Araki** (del artbook) ✅.
- **WIT Studio** hizo la T1 (2019) y **MAPPA** la T2 (2023), pero **se
  quedó el mismo equipo clave** para no romper el estilo ✅
  ([ComicBook.com](https://comicbook.com/anime/news/vinland-saga-season-2-mappa-wit-studio/),
  [GameRant](https://gamerant.com/vinland-saga-season-2-mappa-studio/)).
- MAPPA añadió **líneas negras que cruzan la cara** cuando alguien está
  furioso ⚠️ ([Sportskeeda](https://sportskeeda.com/anime/mappa-s-animation-vinland-saga-season-2-displeases-attack-titan-fans)).

### Lo que dicen ellos (making of)

- Entrevista a Yabuta y Abiru ([AnimaniA](https://animania.de/vinland-saga-anime-staff-interview-mit-shuhei-yabuta-und-takahiko-abiru/),
  en alemán) ✅:
  - El manga tiene **demasiadas líneas para animarlo igual**: simplificaron
    el trazo y cuidaron los detalles en cada escena.
  - Yabuta viene del **CGI 3D**: **planea la cámara en 3D junto con la
    animación** para dar profundidad a la acción y los fondos. AniList le
    da a la serie la etiqueta «CGI» con un 39 %.
  - **Las caras primero**: «las emociones no se pueden escenificar bien
    sin controlar bien las caras».
- **Artbook «Animation Works»** (WIT, 25-sep-2020, 272 páginas, B5, sólo
  japonés): diseño de color y de props, tableros con comentarios de
  Takeda, diseños de Araki y Abiru y entrevista ✅
  ([wiki](https://vinlandsaga.fandom.com/wiki/Vinland_Saga_Animation_Works)).
- **Yukimura se documenta viajando**: Noruega, Dinamarca, Islandia,
  Francia, Inglaterra y Canadá ✅.
- **Del papel al ordenador**: dibujaba con tinta y escaneaba; con la
  pandemia (hacia los **capítulos 168-169**) pasó a entintar en digital ⚠️
  ([Comic Natalie, charla con Isayama](https://natalie.mu/comic/pp/vinlandsaga),
  resumen del buscador; la página dio 403). ⚠️ **El programa no se
  confirmó** (¿Clip Studio Paint?).
- Yukimura: para contar **el odio a la violencia**, el mundo tiene que
  **estar lleno de violencia** ⚠️ ([manga-kuroyan](https://manga-kuroyan.com/5216.html)).
- Satoru Noda admira cómo Yukimura dibuja **la nieve distinta si la pisa
  un pie o la corta un hacha** ✅.

### Cómo se ve

- **Paleta** térrea y apagada; **el fuego es la única luz cálida** en los
  interiores (§5) ✅.
- **Línea**: en personajes, tinta de grosor variable; en paisajes, muy
  poca (el OP1 mide «poca línea» en aurora y bosque; «normal» en el
  castillo).
- **Sombreado**: pictórico, degradados suaves, luz realista. Varias
  reseñas lo comparan con *La princesa Mononoke*.
- **Manga**: tramas de **puntos finos** para sombras de piedra y nieve,
  **líneas paralelas** para el agua (hojas `fondos_01.jpg` #2, #5-7) ✅.

### Cómo reproducirlo (propuesta del equipo, no cita)

**Photoshop**

1. Pincel de **tinta con presión** (grueso al apoyar, fino al final). Nada
   de contorno vectorial uniforme.
2. Sombras en **2-3 capas** en modo Multiplicar con degradado suave.
3. Una capa de **luz de rebote naranja** (modo Trama o Luz suave) en
   interiores, desde el fuego.
4. Paisaje: pintura sin línea, degradados de cielo (paletas de §5).
5. Textura de **papel** (Paper001) en Multiplicar al 10-20 % para quitar
   el brillo digital.

**Blender**

1. Contorno con **Line Art (Grease Pencil)** o **Freestyle**, con grosor
   que cambie con la distancia a la cámara. **Solidify no**: da un
   grosor igual y se aleja del trazo de Yukimura.
2. Shader *toon* de **2-3 bandas suaves** (Shader to RGB + ColorRamp en
   Ease), más una luz de rebote cálida en interiores.
3. Luz: un sol frío y bajo de día; de noche, luna azul y el fuego como
   Point Light naranja.
4. Modelos libres (CC BY, con crédito): dagas de Thorfinn, Thors lowpoly,
   barco vikingo (§4). Tablones: WoodFloor051 o Planks030A (CC0).
5. Render y después **`v3/integrar.py`** para que el personaje encaje
   (regla 3 del dueño).

### Encuadres y composición

| Para… | Encuadre |
|---|---|
| Escala, épica | Plano general muy abierto, horizonte bajo (barco entre témpanos, campo de cadáveres) |
| Emoción | **Primer plano muy cerrado** de ojos (clip ep. 2, 0:53-1:52) |
| Poder | Contrapicado (Thors, OP1 1:15; Canute ante el ejército) |
| Soledad, pensar | De espaldas, figura pequeña ante el paisaje (Thorfinn en el muelle, 2:10; al amanecer) |
| Violencia | Silueta negra contra luz blanca (castillo, tráiler 2:02) |
| Calma | Luz dorada en campo abierto (trigal del ED1) |

---

## 20 · Texturas 2D

| Capa | Qué hay en la serie | Equivalente libre |
|---|---|---|
| **Trama de manga** | Puntos finos en piedra y nieve; líneas paralelas en agua (caps. 130, 138, 146) | [Brusheezy, 34 pinceles de trama](https://www.brusheezy.com/brushes/50379-mabecman-s-screentones-halftone-brushes) (gratis); [Photoshop Supply, +35 texturas de trama](https://www.photoshopsupply.com/patterns-textures/halftone-texture) (gratis, con atribución) ✅ |
| **Grano de papel** | Portadas y pergamino del mapa | [Paper001](https://ambientcg.com/view?id=Paper001) (CC0) |
| **Tela de túnica** | Lana y lino | [Fabric081C](https://ambientcg.com/view?id=Fabric081C), [Fabric061](https://ambientcg.com/view?id=Fabric061) (CC0) |
| **Cuero** | Coraza de Askeladd, cinturones | [Leather037](https://ambientcg.com/view?id=Leather037), Leather030 (CC0) |
| **Metal** | Hombreras, hachas | [Metal063](https://ambientcg.com/view?id=Metal063), Metal049A (CC0) |
| **Madera** | Barcos, casas largas, tablas | [WoodFloor051](https://ambientcg.com/view?id=WoodFloor051), Planks030A (CC0) |
| **Salpicadura roja** | Lluvia de sangre del KV3 T1 (hoja `arte_01.jpg` #3) | Pintarla con pincel de salpicadura; o `v3/sangre.py` del proyecto |
| **Emblemas** | **Jomsvikings**: hacha de un filo con ojo grabado, capa blanca, escudo rojo y amarillo. **Nudos nórdicos y cenefa de falsas runas** del logo de Kodansha USA. **Ornamento dorado sobre rojo** de la portada del artbook | Dibujarlos a partir de las referencias |

- ⚠️ No hay **heráldica propia** de la banda de Askeladd ni del ejército
  de Canute (búsquedas «emblem», «symbol», «banner» en la wiki): sólo
  motivos vikingos históricos.
- Junto con §4 (3D) y §5 (texturas reales), las capas de la lámina
  quedan cubiertas salvo **nieve, paja y piedra** ⚠️.

---

## 21 · Gustos y detalles de cada personaje

| Personaje | Cumpleaños y edad | Altura | Objeto | Gustos y odios | Fuente |
|---|---|---|---|---|---|
| **Thorfinn** | **3 de febrero** (Yukimura lo fijó en Twitter en 2021; antes decía que no tenía); nacido en 996 | 100 cm (6-7 años), 153 cm (16-18), 155 cm (19) | **Las dos dagas** de su padre | Niño: las historias de Leif. Adulto: el campo, la paz. Teme volverse un asesino | AniList + wiki ✅ |
| **Askeladd** | Nacido en 969, muere en 1014 con 44 años | — | Espada; su arma de verdad es **leer caras** | ⚠️ comida y aficiones no documentadas | Epicstream ⚠️; AniList da edad 33-44 |
| **Canute** | **12 de julio**; nacido en 996 | 170 cm | Capa y diadema (rey) | De joven **odia las armas** y le dan miedo; **cocina** (escena del cap. 15 en la votación oficial: «¿Qué ave será? Aún no he hecho ave», cocinando para Ragnar ⚠️); fe cristiana: reza, lleva cruces, cita a Dios | AniList ✅; cocina ⚠️ |
| **Einar** | 20 años al aparecer (1015); cumpleaños no documentado | — | Herramientas de campo | Hijo de granjeros; sabe labrar. Su meta: fundar Vinlandia | wiki ✅ |
| **Thorkell** | — | **230 cm** | Hacha (prop con diseño propio en el artbook) | **Pelear** con alguien de su nivel; se irrita si pasa tiempo sin combate | AniList ✅ |
| **Thors** | — | 180 cm | Su espada (prop del artbook) | Harto de la guerra, granjero pacifista | AniList ✅ |
| **Leif** | Nacido en 965 | 152 cm | Sus historias de Vinlandia | Busca a Thorfinn más de 10 años | AniList ✅ |
| **Willibald** | 23 años | — | — | El alcohol; busca el amor verdadero | AniList ⚠️ |
| **Bjorn** | — | — | Setas del berserker | La pelea | AniList ⚠️ |
| **Mimi** | — | — | Su oído | Necesita silencio total; la nieve le apaga el sonido | AniList ⚠️ |
| **Halfdan** | — | — | **Cadena de hierro** | Encadenar a los demás es su filosofía | AniList ⚠️ |

- **Cómo se ven a sí mismos**: Thorfinn, como alguien que no debe repetir
  la violencia; Askeladd, como un hombre que ya no espera que el héroe
  vuelva; Canute, como el que carga con la «maldición de la corona».
- ⚠️ No hay *databook* traducido con fichas de «le gusta / no le gusta»:
  es un seinen histórico, no un shōnen. La *Official Guidebook*
  (Kodansha, 2019, 256 páginas) existe en japonés, francés e italiano,
  no en español ni inglés ([wiki](https://vinlandsaga.fandom.com/wiki/Vinland_Saga_Official_Guidebook)).

---

## 22 · Por qué la gente la ama, y las escenas que hacen llorar o gritar

### Razones concretas

- **Un pacifismo raro en el género**: Yukimura es pacifista declarado. La
  serie muestra la violencia vikinga más cruda y luego dice que la paz
  cuesta más que cualquier batalla, **sin vender el trauma como
  «desarrollo»**. Varias reseñas independientes lo dan como la razón
  número uno ✅.
- **Identificación**: los lectores se ven en **la culpa y el duelo de
  Thorfinn**; la describen como una lectura que empuja a la empatía en
  vez de la rabia.
- **Dos personajes, el mismo origen**: Thorfinn y Askeladd salen del mismo
  dolor y eligen distinto (hilo de Reddit, 42 votos).
- **Premios del manga**: **Gran Premio de manga de los Japan Media Arts
  Awards** (2008), **36.º Premio Kodansha de Manga**, categoría general
  (2012); nominado al Manga Taisho 2008; **más de 1,2 millones de copias
  sólo de los 5 primeros tomos** (2008) ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Vinland_Saga_(manga))).
- **Premios del anime**: ganó **Mejor Drama** en una edición de los
  Crunchyroll Anime Awards; 16 nominaciones en total; la T2 compitió en
  2024 por Anime del Año, Mejor Personaje Principal (Thorfinn), Mejor
  Cinematografía, Mejor Drama y Mejor Serie Continuada. **Perdió Anime
  del Año** y los fans protestaron en Reddit ✅.
- **AniList**: nota media 87, popularidad 548 003 ✅.

### Las escenas que hacen llorar

| Escena | Dónde | Qué pasa y por qué duele | Cómo está hecha | Cómo reaccionó la gente |
|---|---|---|---|---|
| **Muerte de Thors** | manga cap. 4-5, **anime ep. 4** | Thors vence a los hombres de Askeladd y a Askeladd mismo, pero **se rinde para salvar a su hijo** y lo matan por la espalda, delante de Thorfinn | Thors arrodillado, espada baja; Askeladd con sonrisa cruel; primer plano de los ojos del niño; la sangre se extiende por la túnica gris ([clip](https://www.youtube.com/watch?v=LPnQ74j1dqY)). Música: el tema que los fans llaman «Thors vs Askeladd» ⚠️ | Es la **escena n.º 4 de la votación oficial** («第4話 トールズの死») con la cita «本当の戦士には、剣などいらぬ». En MyAnimeList cuentan que lloraron «con orgullo» ✅ |
| **Muerte de Askeladd** | manga cap. 90-91, **anime ep. 24** | Se enfrenta solo al rey Sweyn para que **Canute reine**; antes revela que desciende de Artorius | Celda de piedra, antorchas, banda roja, «Don't waste it» ([clip Crunchyroll](https://www.youtube.com/watch?v=PF2NTT_mnps)) | Escena n.º 24 de la votación oficial; de lo más compartido del fandom |
| **Muerte de Arnheid** | **T2, ep. 20** | La pareja de Einar muere tras la violencia y la desesperanza; Thorfinn le dedica unas palabras al despedirla | ⚠️ no se miró el vídeo | Un usuario de Reddit «sollozó sin control»; según Sportskeeda, «encarna el mensaje de toda la T2» ✅ ([Sportskeeda](https://sportskeeda.com/anime/vinland-saga-season-2-episode-20-arnheid-einar-s-love-story-ends-thorfinn-goes-c)) |
| **«Nadie tiene enemigos»** | manga cap. 2, **anime ep. 2** | Thors le explica al niño que no tiene enemigos. Es la semilla de toda la serie | Primeros planos de los ojos de Thors, pausas largas; termina con el niño **solo en el muelle nevado** mirando irse el barco (2:10-2:13) | En la votación oficial: «第2話「お前に敵などいない誰にも敵などいないんだ」» ✅ |
| **Reencuentro de Thorfinn y Einar** | **T2, ep. 1** | Se reconocen sin palabras | **Sólo música orquestal** hasta el «¡Ven!» del 2:36 | ✅ (clip mirado) |

### Las que hacen gritar de emoción

- **Thorkell frena solo un ejército riéndose** (manga cap. 9-10, anime
  ep. 9-10): el momento de acción más compartido como «hype». Está en la
  votación oficial («第9話「必殺！！竜骨砕き！！」») ✅.

⚠️ El **minuto dentro del episodio completo** no se tiene: sólo el del
clip recortado.

---

## 23 · Fan dubs y comunidad hispana

| Qué | Canal | Escena | Vistas | Enlace |
|---|---|---|---|---|
| Fandub **«Tú no tienes enemigos»** | Mend VA Dubs (Facebook) | Thors y Thorfinn, ep. 2 | 2477 ✅ | [Facebook](https://www.facebook.com/100063024169377/videos/tu-no-tienes-enemigos-vinland-saga-fandub-espa%C3%B1ol-latino/1024247659028271/) |
| Fandub **«La muerte de Askeladd»** | RodriFD (YouTube) | ep. 24 (5:03) | 740 ✅ | [YouTube](https://www.youtube.com/watch?v=AqaUzBNYoms) |
| **Cover del OP1 «MUKANJYO» en español latino** | James Mart | Opening 1 | **32 184** ✅ (el más visto) | [YouTube](https://www.youtube.com/watch?v=zPXwYoFYDgU) |
| «MUKANJYO Full Español Latino ft. Jhair & Tricker» | — | Opening 1 | ⚠️ sin vistas | — |
| Cover del OP3 «RIVER» | André - A! | Opening 3 | ⚠️ sin vistas | — |

- **Vinland Saga Latinoamérica** (Facebook): la comunidad hispana más
  activa. Sube **los clips oficiales doblados episodio a episodio**, hace
  memes, «duelos de arco» y **encuestas sobre qué actor pondrían a cada
  personaje** ✅ ([página](https://www.facebook.com/VinlandSagaLatam)).
- **TikTok**: [@fandoblajes](https://www.tiktok.com/@fandoblajes/video/7291264804713450758)
  compara Netflix y Crunchyroll; **@lalogarx** (el propio Lalo Garza)
  cuenta cómo dobló a Thorfinn ✅.
- **Lo que más se discute en español**: **cuál doblaje es mejor**. Para un
  servidor de doblaje es oro: una lámina 2 o un reto puede poner la misma
  frase en las dos versiones.
- ⚠️ No se encontró un meme hispano propio.

---

## 24 · Colaboraciones, figuras y cosplay

| Qué | Cuándo | Qué trae | Fuentes |
|---|---|---|---|
| **Cómic «Assassin's Creed Valhalla × Vinland Saga»**, dibujado y escrito por **Yukimura** | 23-oct-2020, web de Ubisoft Japón | Una entrega, arte nuevo del autor | [ComicBook.com](https://comicbook.com/anime/news/assassins-creed-vinland-saga-manga-crossover/) + [wiki de Assassin's Creed](https://assassinscreed.fandom.com/es/wiki/Assassin's_Creed:_Valhalla_x_Vinland_Saga) ✅ |
| **Película *The Northman* (2022) × anime** | enero de 2023 | Vídeo con los seiyū de Thorfinn (Yūto Uemura) y Canute (Kenshō Ono) | [ANN](https://www.animenewsnetwork.com/interest/2023-01-05/vinland-saga-the-northman-come-together-for-the-ultimate-viking-crossover/.193451) + [Código Espagueti](https://codigoespagueti.com/noticias/anime/vinland-saga-the-northman-tienen-genial-colaboracion-oficial/) ✅ |
| **Zombieland Saga × Vinland Saga** | estreno del anime (2019) | Ilustración de la cuenta oficial de Zombieland Saga | [AnmoSugoi](https://www.anmosugoi.com/de-interes/zombieland-saga-estrena-una-ilustracion-crossover-con-vinland-saga/) ⚠️ una fuente |
| **Prefectura de Saga («Sagaprise!»)** | 3-18 oct 2019, Akihabara | «Búsqueda de Vinlandia»: rally de sellos; exposición con diseños, dibujos originales y fondos | [ANN](https://www.animenewsnetwork.com/interest/2019-09-17/vinland-saga-vikings-enjoy-saga-prefecture-bounty/.151221) + [Anime Anime Global](https://animeanime.global/2019/09/24/48410.html) ✅ |
| **Figura figma Thorfinn** (Good Smile, n.º 608) | anunciada 30-may-2023, salió feb-2024 | ~145 mm, ropa de tela, caras y dagas intercambiables: **referencia 3D de pose y volumen** | [goodsmile.com](https://www.goodsmile.com/en/product/12106/figma+Thorfinn) + [Hobby Genki](https://hobby-genki.com/en/figma/18144-figma-thorfinn-vinland-saga-action-figure-limited-edition-4545784068939.html) ✅ |
| **Cosplay de Askeladd** | — | Foto real, materiales y volumen (819×1024, CC BY-NC 2.0, plumvs-photo) | [Flickr](https://live.staticflickr.com/65535/52593952796_33fbe2f334_b.jpg) ✅ |
| **Guía de cosplay de Thorfinn** | — | Peluca, piel, túnica beige, cinturón, daga | [Carbon Costume](https://carboncostume.com/thorfinn-from-vinland-saga/) ⚠️ |

- ⚠️ No hay **cafés temáticos** ni colaboraciones con **gachas o
  Fortnite** en lo buscado. Tampoco videojuegos (§13).

---

## 25 · Obras parecidas y láminas vecinas

### Lo que recomienda el público (AniList, votos)

Attack on Titan (2876), **Berserk** (1066), Dororo (546), *Orb: On the
Movements of the Earth* (413), *To Your Eternity* (142), Rurouni Kenshin
2023 (128), **Golden Kamuy** (123), Kingdom (92), *Jaadugar* (80),
Claymore (65), *Ranking of Kings* (59), Drifters (53) ✅.

### Influencias y parientes que reconoce el autor

- **El Puño de la Estrella del Norte**: Yukimura pasó unos **20 años
  dándole vueltas a los capítulos 2 y 3**, incómodo con que Kenshiro no
  arreglara el problema de raíz («¿por qué no llevaste el grano de vuelta
  al pueblo?»). Esa pregunta es el tema de Vinland Saga: construir la paz,
  no sólo vencer ✅ ([Anime Corner](https://animecorner.me/interview-vinland-saga-creator-makoto-yukimura/)).
- **Vicky el Vikingo**, la serie que vio de niño, el origen remoto de su
  interés por los vikingos ⚠️ (una fuente).
- **Golden Kamuy** (Satoru Noda): admiración mutua, los dos investigan
  viajando; Noda admira a Askeladd ✅.
- **Attack on Titan** (Hajime Isayama): charla a solas entre los dos en
  Comic Natalie; Isayama elogia su estructura en tres actos ✅.
- **Planetes**, la obra anterior de Yukimura (1999-2004, Premio Seiun
  2002): ciencia ficción realista, antecedente del realismo histórico de
  Vinland Saga ✅.

### Láminas del servidor que se le parecen (para no repetir)

| Lámina vecina | Qué usa | Cómo se diferencia Vinland Saga |
|---|---|---|
| **Attack on Titan** (#reglas) | Cartela de **papel sucio con cinta de pincel rojo sangre** | Madera tallada, cuero, pergamino de mapa; sangre sólo como salpicadura |
| **Arcane** (#proyectos y #arte) | Si se queda #proyectos, choca | Vinland Saga: mapas y madera, mundo medieval, luz de fuego |
| **Death Note** (#textos) | Si Vinland Saga hace su lámina 2 | Muelle nevado y tabla tallada, no cuaderno |
| **Violet Evergarden** (#poemas) | Cartas y máquina de escribir | Evitar «carta escrita»: en Vinland Saga, mapa y tallado |

---

## 26 · El mundo, la historia por arcos y sus símbolos

### Las reglas del mundo en cinco líneas

1. **Europa vikinga de principios del siglo XI** con hechos reales
   (batalla de Maldon en 991, conquista danesa de Inglaterra), pero con
   licencias: la wiki avisa que no es una cronología exacta ✅
   ([Timeline](https://vinlandsaga.fandom.com/wiki/Timeline)).
2. **La esclavitud es legal y corriente**; un esclavo puede **comprar su
   libertad trabajando** ✅.
3. **El poder se decide por la espada y el linaje**: Sweyn Forkbeard,
   Canute, Ethelred II y Edmund Ironside son reyes reales ✅.
4. **Los jomsvikingos** son una hermandad de élite con reglas propias:
   capa blanca, disciplina militar y **funeral en el mar** (el cuerpo arde
   en un barco mientras suenan flautas) ✅
   ([Jomsvikings](https://vinlandsaga.fandom.com/wiki/Jomsvikings)).
5. **Vinlandia es real**: la serie la sitúa en la **Isla del Príncipe
   Eduardo** (Canadá), «Epekwitk» en mi'kmaq; lo confirma Yukimura en el
   tomo 26. Allí Thorfinn quiere fundar **«una tierra sin guerra ni
   esclavos»** (1022, junto a la tribu de Kitpui) ✅.

### La historia por arcos

Yukimura confirmó en Twitter (2019) que son 4 partes ✅
([Story Arcs](https://vinlandsaga.fandom.com/wiki/Story_Arcs)).

| Arco | Capítulos | Tomos | Anime | Qué pasa | Momentos clave |
|---|---|---|---|---|---|
| **De la guerra** | 1-54 | 1-8 | **T1**, ep. 1-24 | Infancia en Islandia; Thorfinn sigue a Askeladd para vengarse; guerra por la corona de Inglaterra | Muerte de Thors (ep. 4); Thorkell frena un ejército (ep. 9-10); Canute despierta; muerte de Askeladd (ep. 24) |
| **De la esclavitud** | 55-99 | 8-14 | **T2**, ep. 25-48 | Thorfinn, esclavo en la granja de Ketil, desbroza un bosque con Einar; Canute rey y su «paraíso en la tierra» | Reencuentro con Einar (T2 ep. 1); ataque a la granja; muerte de Arnheid (T2 ep. 20) |
| **Expedición al este** | 100-166 | 14-24 | — | Vuelve a Islandia; viaja al este (Bizancio) para pagar el sueño de Vinlandia; guerra civil de los jomsvikingos | Jomsborg de noche (cap. 146) |
| **De Vinlandia** | 167-final | 24-final | — | Fundación de la colonia | Thorfinn con Gudrid; contacto con los nativos |

La serie **terminó el 25 de julio de 2025**, tras 20 años ✅.

### Objetos icónicos y símbolos

- **Las dos dagas de Thorfinn**, **la espada de Thors**, **la espada de
  Askeladd** y **el hacha de Thorkell**: los cuatro props con diseño de
  color propio en el artbook oficial ✅.
- **Los jomsvikingos**: **hacha de un filo con un ojo grabado**, **capa
  blanca**, **escudo rojo y amarillo** ✅.
- **El barco vikingo** (drakkar o knarr, vuelta completa en el artbook) y
  el **mascarón de proa tallado** (clip ep. 2, 2:10).
- **El mapa de Vinlandia** pintado a pluma (opening).
- **La vela de rayas rojas y blancas** (portada del tomo 1).
- **La banda roja** de Askeladd en su final.
- **La diadema** de Canute rey.
- **La cartela roja** del número de capítulo.

### Vocabulario que un fan reconoce al instante

- «**Un verdadero guerrero no necesita espada**» (Thors, cap. 15, pág. 5;
  la repiten Askeladd y Thorkell) ✅
  ([wiki: Thors](https://vinlandsaga.fandom.com/wiki/Thors_Snorresson)).
- «**No tienes enemigos**» / «**No tengo enemigos, ninguno**» ✅.
- «**Crearé un paraíso en esta tierra**» (Canute) ✅.
- «**Sigue adelante, Thorfinn**»: últimas palabras de Askeladd, que le
  pide no pasarse la vida aferrado a la venganza (en la wiki inglesa:
  «Move on, Thorfinn. Don't hang on to this petty bullshit your entire
  life») ✅.
- **Vinland**, **jomsvikingo**, **skræling**, **«la maldición de la
  corona»**, **Artorius**, **Troll de Jom**, **berserker**.

---

## 27 · Tres conceptos de lámina

Canal propuesto: **#proyectos** (conceptos 1 y 2); reserva, **#textos
lámina 2** (concepto 3). Ver §0.

Lo que dice el canal según `servidor/inventario.md`:

- **#proyectos**: «Un hilo por proyecto: equipo, avance, entregas.»
  Etiquetas: Buscando gente, En traducción, En grabación, En edición, En
  revisión, Estrenado, En pausa, Cancelado, Oficial del servidor, De la
  comunidad. Hilos fijados: «📌 De qué va esto» y «EJEMPLO · Proyecto en
  marcha, para ver el formato».
- **#textos**: «Guiones para practicar: monólogos, diálogos, escenas y
  narraciones. Un hilo por guion, y di si se puede usar libre o hay que
  pedir permiso.» Etiquetas: Monólogo, Diálogo, Escena de anime,
  Comercial, Narración, Original, Libre para usar, Pide crédito, Para dos
  voces.

Las frases de los personajes en la lámina son **propuestas del
redactor** en su voz (§18), no citas, salvo donde se dice.

### Concepto 1 · «El mapa de campaña de Askeladd» (#proyectos) · recomendado

- **El objeto y el sitio**: una **mesa de tablones** dentro de la **casa
  larga**, de noche, con el **hogar encendido** como única luz (tablero
  «Scenery» del artbook, hoja `fondos_01.jpg` #9). Sobre la mesa, un
  **mapa de campaña de pergamino**, dibujado a pluma como el **mapa del
  cruce a Gales** del manga («Askeladd's landing», «Thorkell's men»,
  Bristol, hoja `fondos_01.jpg` #4). **En Blender**: plano con Paper001,
  simulación de tela para las arrugas y bordes enrollados, tinta que
  sigue las arrugas; unas **fichas de madera** y **una daga clavada** en
  el punto donde «vamos».
- **El personaje**: **Askeladd**, el más querido (§9). De pie,
  **inclinado sobre la mesa**, una mano apoyada con el brazo entero a la
  vista (regla 7 del dueño) y la otra señalando el mapa con la daga.
  **Sonrisa ladeada**, ojo algo entrecerrado.
  - Cuerpo y ropa: diseño del anime (hoja `personajes_01.jpg` #17) y
    [hoja del artbook](https://static.wikia.nocookie.net/vinlandsaga/images/c/c7/AnimationWorksPreview_Askeladd.png).
  - Gesto de explicar: el «this part is important» del ep. 24
    ([clip](https://www.youtube.com/watch?v=PF2NTT_mnps)).
  - Paleta: coraza `#6D5B42`, túnica `#D9C08D`, pelo rubio con luz de
    fuego.
- **Cómo habla**: su nombre en la **cartela roja rectangular** del manga
  (texto blanco); su frase en **cartela negra con serif blanca**
  (Playfair Display), como en los tráileres, abajo. Calmado, sin
  exclamaciones:
  - «Un hilo por proyecto. Dime quién va, hasta dónde llegaste y qué
    entregas.»
  - «Esta parte es importante: marca en qué punto estás.» (eco de su
    frase del ep. 24)
  - «¿Quieres ver cómo se hace? Abre el hilo de ejemplo.»
- **Dónde va cada texto**:
  - Arriba a la izquierda, **«PROYECTOS»** en rojo con trazo roto
    (Eater), como el logo.
  - En el mapa, a pluma (MedievalSharp), **tres zonas**: «Equipo» junto
    a un grupo de fichas, «Avance» sobre la flecha de la ruta,
    «Entregas» en el destino.
  - En el margen del mapa, una **leyenda** con las 10 etiquetas (Pirata
    One pequeña), cada una con su marca.
  - Abajo, la cartela negra con la frase de Askeladd.
- **Para que no quede plano**:
  - Delante, **desenfocadas**, las espaldas de dos hombres de su banda
    (como el grupo del KV3, hoja `arte_01.jpg` #3) y el borde del fuego.
  - El fuego a un lado: **luz naranja de rebote** en la cara y el pelo,
    el otro lado en sombra `#241B0D`.
  - Humo y vigas de la casa larga detrás; la daga clavada proyecta
    sombra sobre el mapa.

### Concepto 2 · «La tabla de Vinlandia» (#proyectos, o su lámina 2 de etiquetas)

- **El objeto y el sitio**: el **campo que Thorfinn y Einar desbrozan**
  en la granja de Ketil, a mediodía; bosque verde oscuro detrás (tráiler
  T2, [1:31](https://www.dailymotion.com/video/x8h1n5b?t=91), paleta
  `#263020` `#1B2616` `#816541`). Apoyada en el **tocón a medio
  arrancar**, una **tabla de madera** con **el mapa de Vinlandia pintado a
  pluma en tinta roja marrón**, como el del opening
  ([mapa](https://vinlandsaga.fandom.com/wiki/File:Anime_op_vinland_map.jpg)).
  **En Blender**: tabla con WoodFloor051, la tinta sigue la veta; el
  tocón con raíces y la cuerda tensa.
- **Los personajes**:
  - **Thorfinn adulto** con la **túnica con capucha caqui** `#BAA16E`
    ([hoja de color del artbook](https://static.wikia.nocookie.net/vinlandsaga/images/9/94/AnimationWorksPreview_Thorfinn.png)),
    **ojos abiertos y tranquilos**, en cuclillas junto a la tabla,
    señalando la ruta con la mano abierta.
  - **Einar** de pie detrás, **camisa verde** `#7A7646`, apoyado en la
    herramienta, sonrisa franca ([diseño T2](https://static.wikia.nocookie.net/vinlandsaga/images/7/74/Einar_S2_anime_design.png)).
  - El dúo del arco de la esclavitud, el que el fandom hispano asocia a
    esta parte (§8).
- **Cómo habla**: **subtítulo sin caja** (Noto Sans blanca con contorno
  fino), como en el anime; el nombre de cada uno en cartela roja.
  - Thorfinn, despacio: «Un proyecto se cruza como el mar... paso a
    paso.»
  - Einar, directo: «¡Y ponle la etiqueta, que si no, nadie sabe dónde
    vas!»
- **Dónde va cada texto**:
  - La **ruta** del mapa, de Islandia a Vinlandia, lleva las etiquetas
    como paradas, a pluma (MedievalSharp): «Buscando gente» en el puerto
    de salida; «En traducción», «En grabación», «En edición» y «En
    revisión» en la travesía; **«Estrenado» en Vinlandia**.
  - «En pausa» en un barco **fondeado**; «Cancelado» en un **barco
    hundido**.
  - «Oficial del servidor» y «De la comunidad» como **dos banderas** en
    la esquina de la tabla.
  - Arriba, «PROYECTOS» y la función del canal en una línea.
- **Para que no quede plano**:
  - En primer plano, **las raíces del tocón y la cuerda** cruzando,
    desenfocadas.
  - **Sol de mediodía** sobre la piel (`#EAC7A1`) y la tabla, con sombras
    de hojas.
  - Bosque profundo detrás, **polvo de tierra** en el aire.

### Concepto 3 · «Para dos voces en el muelle» (#textos, lámina 2)

- **El objeto y el sitio**: el **muelle nevado de Islandia**, el día que
  Thors se va a la guerra (clip ep. 2, 2:10-2:13: el **mascarón de proa**
  tallado contra el cielo y Thorfinn solo en el muelle). Un **poste o
  tablón del muelle** con las 9 etiquetas de #textos **talladas**, con
  nieve dentro de los surcos. **En Blender**: tallado con desplazamiento
  sobre Planks030A, nieve en partículas, el barco de la vuelta del
  artbook (hoja `fondos_01.jpg` #10) atracado al lado.
- **Los personajes**:
  - **Thors arrodillado** a la altura del niño, como cuando se despide de
    Ylva (clip ep. 2, 1:58-2:04), serio y tranquilo.
  - **Thorfinn niño** con los **ojos grandes y curiosos** (clip ep. 2,
    0:04-0:18).
- **Cómo habla**: en **formato de guion para dos voces**. Cada línea con
  el nombre en **cartela roja** («THORS», «THORFINN») y el texto en
  **cartela negra con serif blanca** (Playfair Display). Así la lámina
  enseña el formato del foro. Arriba, como lema, la cita real del
  doblaje de Netflix: «**Nadie tiene enemigos.**» (Thors, ep. 2, 1:05).
  - Thors: «Un guion se ensaya con calma. Piénsalo bien antes de subirlo.»
  - Thorfinn: «¿Y cómo sé si lo puedo usar?»
  - Thors: «Míralo en la etiqueta: libre, o pide crédito.»
- **Dónde va cada texto**:
  - Arriba, «TEXTOS» (Eater) y la función del canal en una línea.
  - El diálogo de tres líneas, a la izquierda, en formato de guion.
  - Las **9 etiquetas talladas** en el poste del muelle, a la derecha.
- **Para que no quede plano**:
  - **El mascarón de proa** entra en primer plano por un lado.
  - **Nieve cayendo** delante de los personajes.
  - Fiordo con niebla detrás (paleta `#F8F9F5` `#CFD4CC` `#909C96`) y un
    **farol cálido** en el barco, como el del KV2 (hoja `arte_01.jpg` #2),
    único punto de luz caliente.

### Ideas para láminas 2 y extras

- **Reto de doblaje**: la misma frase en las **dos versiones latinas**
  (Netflix y Crunchyroll), para comparar, como hace el fandom hispano
  (§23).
- **#eventos**: el rally de sellos «Búsqueda de Vinlandia» que hizo la
  prefectura de Saga en 2019 (§24) sirve de modelo para un evento por
  etapas con sello en cada una.
- **Lámina 2 de etiquetas** de cualquier foro: la leyenda del mapa del
  concepto 1.

---
