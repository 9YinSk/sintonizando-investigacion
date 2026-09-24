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
