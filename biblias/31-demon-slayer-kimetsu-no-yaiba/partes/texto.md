# Parte de TEXTO — puntos 18, 24 y 25 (repaso corto) · Demon Slayer (Kimetsu no Yaiba)

La biblia ya está completa en 22 secciones (1-20 + resumen + cumplimiento):
tipografía (5), cuadro de diálogo (6), videojuegos (11) y obras parecidas de
AniList ya están cubiertas y **no se tocan**. Este repaso investiga **sólo
los puntos 18 (estilo de dibujo y técnica, y cómo replicarlo), 24 (obras
parecidas y temas relacionados) y 25 (el mundo, la historia y sus símbolos)**
de `ENCARGO.md`, nuevos y ausentes en `biblia.md` (comprobado con
`seccion.py --indice`: no hay sección 18/24/25 propia). Parto de
`datos-texto.md` (no repito esas consultas: AniList staff, obras parecidas,
capturas de Steam). Las fuentes de abajo se comprueban contra la bitácora ya
citada (52 fuentes + las nuevas de `imagen.md`) para no repetir dominio.

## Hallazgos

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

#### 18.1 Qué software usó ufotable (entrevistas técnicas, no fan-made)

- **3ds Max es el software 3D principal**, con estos plugins: **V-Ray**
  (render), **PhoenixFD** (fluidos: fuego y agua de las respiraciones),
  **tyFlow** (partículas: hilos de araña, viento, cuervos), **ForestPack**
  (vegetación), **RailClone** (estructuras repetidas del Castillo
  Infinito), **GrowFX** (crecimiento orgánico), **HairFarm** (pelo) y
  **Pencil+** (estilización 2D sobre 3D) · ✅ [entrevista de Autodesk AREA
  JAPAN a ufotable, parte 1](https://area.autodesk.jp/case/animation/kimetsu-01/)
  (texto: «los cortes CG de Kimetsu prácticamente se realizaron con 3ds
  Max y plugins») + confirmado en la [parte
  2](https://area.autodesk.jp/case/animation/kimetsu-02/) y en el
  [reportaje de CGWORLD sobre el equipo de vídeo digital de ufotable con
  NVIDIA](https://cgworld.jp/special-feature/202410-nvidia-hp-ufotable.html)
  (también usan **Blender y Houdini** para colaboraciones externas,
  **EmberGen** para fluidos rápidos, **After Effects** para compositing y
  **DaVinci Resolve** para edición).
- **Quién habla**: la entrevista de CGWORLD/NVIDIA es con **Yuichi Terao**
  (寺尾優一, jefe del Departamento de Imagen Digital y director de
  fotografía, 20+ años en la industria), **Takeshi Okuya** (奥屋武志, líder
  del equipo de artistas técnicos) y **Reiji Amano** (天野礼治, artista
  técnico, ex modelador de personajes) ✅.
- **Cómo se reparte el trabajo 2D/3D** (Autodesk, parte 1): se hacen
  **maquetas 3D previas** para dar a los dibujantes 2D una referencia de
  perspectiva y composición antes de animar; fondos arquitectónicos y
  criaturas complejas se generan enteramente en 3D; los personajes
  principales siguen siendo dibujo tradicional; un **supervisor 3D
  participa en las reuniones de dirección** antes de que empiece la
  animación 2D ✅.
- **La Respiración del Agua** se diseñó investigando estéticamente los
  grabados *ukiyo-e*, con múltiples iteraciones en 3ds Max antes de fijar
  la dirección de arte ✅ (Autodesk, parte 1).
- **El Castillo Infinito** se modeló entero en 3ds Max, con **~30
  versiones de la estructura por escena** para mantener la sensación de
  geometría imposible ✅ (Autodesk, parte 1); en la
  [entrevista de Terao con Popverse sobre la película](https://www.thepopverse.com/movies-demon-slayer-kimetsu-no-yaiba-yuichi-terao-interview-making-the-infinity-castle-feel-infinite)
  cuenta la evolución: en el episodio 26 (T1) sólo podían renderizar
  ~100×100 m; en el arco de los Herreros (ep. 45), 2 km² procesables; en
  la película, **10 veces más rápido** de render ✅ (dos fuentes: Autodesk
  + Popverse, ambas citando al mismo equipo desde ángulos distintos).
- **Gotouge dibuja el manga a mano, en analógico**: la
  [exposición de dibujos originales «原画展»](https://discoverjapan-web.com/article/74084)
  (Discover Japan, prensa oficial de la exposición, 2024-25) confirma que
  son «直筆原画» (dibujos manuscritos originales) ⚠️ (una fuente de prensa;
  no da marca de plumilla ni si retoca en digital). La
  [entrevista al primer editor, Tatsuhiko Katayama](https://news.livedoor.com/article/detail/17760339/)
  (livedoor News, prensa) describe el flujo real: Gotouge mandaba los
  *nomes* (bocetos) **por fax** desde una zona rural y los corregía **por
  teléfono** con el editor ✅ (confirma un proceso tradicional, no un
  estudio digital en la redacción).

#### 18.2 Sombreado, línea y composición (fuentes de análisis técnico)

- **Sombreado**: cel-shading plano en los personajes, compositado sobre
  fondos y efectos 3D **deliberadamente más fotorrealistas** para crear
  contraste — es la firma de ufotable: «fotorrealismo en CGI que
  contrasta deliberadamente con arte de personajes audaz» ✅ [Sakuga
  Blog — The Power of Ufotable's
  Harmony](https://blog.sakugabooru.com/2019/08/15/kimetsu-no-yaiba-the-power-of-ufotables-harmony/)
  (blog de análisis de animación, en inglés, cita a animadores por
  nombre).
- **Línea variable**: **Akira Matsushima** (directora de animación /
  diseño de personajes) usa un grosor de línea que **cambia con el
  movimiento del personaje** («variable lineweight») ✅ (Sakuga Blog,
  misma fuente).
- **Animadores clave citados** (para buscar sus cortes en YouTube/Twitter
  si se quiere estudiar el trazo a mano): **Masayuki Kunihiro** (poses
  «sobrehumanas», anticipación larga antes del golpe: anima a Inosuke),
  **Mitsuru Obunai** (timing «ágil», dibujos muy espaciados para dar
  sensación de fuerza) y **Nozomu Abe** (efectos 2D, siluetas de
  personaje en los fotogramas de impacto) ✅ (Sakuga Blog).
- **Encuadres y composición** (para «cómo se enmarca cada emoción», ✅
  [The Visual Design of Demon Slayer's Combats — jb
  siraudin](https://jbsiraudin.github.io/blog/demon-slayer-visual-grammar/),
  ensayo técnico de análisis visual, en inglés, con ejemplos de combate):
  - la acción se **comprime al centro del cuadro** para que el ojo no
    tenga que moverse: menos fatiga visual en escenas intensas;
  - la **cámara tiembla a 24 fps mientras la animación va a 12 fps**
    (desenfoque de movimiento superpuesto), y la cámara **se mueve en la
    dirección del golpe** para reforzar el impacto;
  - **la luz avisa el ataque antes del contacto**: brillo azul en las
    espadas, tonos morados para enemigos, chispas doradas; cada golpe se
    anuncia con un color antes de llegar;
  - **fotogramas de impacto**: un frame de alto contraste (a veces sólo
    silueta) en el instante del choque, para dar peso;
  - **ritmo**: preparación larga → ataque instantáneo → relajación larga,
    como respiraderos entre secuencias frenéticas (coincide con el propio
    tema de «respiración» de la serie, §0 de la biblia).
  - En el mismo sentido, Sakuga Blog analiza el **episodio 19** («Cumbre
    de Armonía», storyboard de **Toshiyuki Shirai**): la sensación de
    peligro se transmite por el *storyboard*, no sólo por el guion, con
    composiciones que acentúan la amenaza sin perder legibilidad ✅.

#### 18.3 Cómo replicarlo en Blender

- **Contorno**: **Freestyle** (Render Properties → Freestyle) es la vía
  más simple para una línea negra tipo anime; **Grease Pencil** da más
  control línea a línea (grosor variable, como Matsushima) ⚠️ (una guía
  técnica: [StraySpark — How to Get an Anime / Toon Look in Blender
  (2026)](https://www.strayspark.studio/blog/how-to-get-anime-toon-look-blender)),
  corroborado por [Instructables — Custom Toon Shader in
  Blender](https://www.instructables.com/Custom-Toon-Shader-in-Blender/)
  ✅ (dos fuentes independientes, ambas explican Freestyle como método).
- **Sombreado tipo cel**: nodo **Shader to RGB → Color Ramp** en modo
  *Constant* — **dos paradas de color = anime clásico a dos tonos**, tres
  paradas añaden un medio-tono (Eevee) ✅ [Yarsa DevBlog — Toon Shading
  Effect in Blender
  Tutorial](https://blog.yarsalabs.com/basic-toon-shader-in-blender/) +
  tutoriales en vídeo: [«New Anime Cel/Toon Shader for Blender 4.2+
  [EEVEE]»](https://www.youtube.com/watch?v=uCplB3zvQks) y [«ANIME in
  BLENDER! - Toon Shading
  Tutorial»](https://www.youtube.com/watch?v=WcVwszxkUuA).
- **Modelos y *rigs* libres del personaje** (con licencia, para posar y
  renderizar, no para vender): el artista de Sketchfab **Light.k** subió
  una serie completa de personajes de Demon Slayer **totalmente
  *rigueados*** bajo **CC Attribution 4.0** y descargables: [Tanjiro
  Kamado](https://sketchfab.com/3d-models/none-0ab5b317b7654fd29255d22182537ded)
  (33.764 caras), [Akaza (Superior
  3)](https://sketchfab.com/3d-models/none-327741c265db45c1b92ca9f1aeb57e99)
  (45.629 caras), [Rengoku](https://sketchfab.com/3d-models/none-91a0c5978dd74ca5a0d4747c89270f99)
  (59.528 caras), además de Nezuko, Inosuke, Giyu y Rui (mismo autor,
  mismo buscador) ✅ (comprobado con la API de Sketchfab: `license.label
  = "CC Attribution"`, `isDownloadable = true`). También **AikoX** subió
  un [Nezuko *rigged*](https://sketchfab.com/3d-models/none-c57b6393ddee4c86b28a26c26d7a7a8f)
  (122.561 caras, CC Attribution, con *shapekeys* pensado para Maya/Eevee)
  y **K-** dos versiones de Tanjiro ([Kagura del
  Hinokami](https://sketchfab.com/3d-models/none-dfebaddf7ec442cc8cf81f561fcb465b),
  [uniforme de la Selección
  Final](https://sketchfab.com/3d-models/none-50ba553d376e45e596eace02e9779c38),
  con el `.blend` original enlazado a Google Drive) ✅. Ninguno de estos
  9 enlaces se repite con los 15 ya citados en la biblia (todos IDs de
  Sketchfab distintos, comprobado con `grep`).
- **Texturas encima del render**: para que el 3D no se vea «demasiado
  limpio», una capa de **grano de papel o pincelada** en modo *Overlay*
  (baja opacidad) sobre el render final rompe el aspecto sintético; las
  texturas CC0 concretas (papel, tela, madera) ya las buscó el
  investigador de imagen en el punto 4 de la biblia (§5, ambientCG): no
  se repiten aquí, sólo se indica **dónde va la capa** en el flujo de
  Blender → Photoshop (render de Blender como capa base, textura encima
  en *Overlay* u *Soft Light*, línea de Freestyle como capa superior en
  *Multiply*).
- **Luz y render**: Freestyle/Grease Pencil para el contorno + un *world*
  con luz plana de área (evitar sombras duras) reproduce el look de
  ufotable mejor que un render PBR normal, según la misma guía de
  StraySpark (⚠️ receta de tercero, no del estudio real: el estudio usa
  V-Ray con render fotorrealista para fondos, no toon-shading — ver
  18.1). Para un objeto de lámina (ver ENCARGO, «un objeto real en un
  sitio real»), lo fiel al estudio real es: **fondo/objeto con render
  realista** (V-Ray-like: Cycles con luz de área e IES) y **personaje en
  capa aparte con toon-shading**, tal y como hace ufotable en pantalla.

#### 18.4 Cómo replicarlo en Photoshop

- **Pinceles de línea manga/anime, gratis, formato .abr (Photoshop
  nativo)**: [Manga Brush Line — for Photoshop, por Pearlpencil
  (DeviantArt)](https://www.deviantart.com/pearlpencil/art/Manga-Brush-Line-for-Photoshop-268440777)
  ✅ (gratis, dice explícitamente «for Photoshop»); [Manga Ink — 496
  pinceles gratis en
  Brusheezy](https://www.brusheezy.com/free/manga-ink) ✅ (licencia
  variable por pincel, revisar cada uno). Para el trazo grueso/fino que
  varía con la presión (como Matsushima en el anime), usar un pincel de
  **tinta con sensibilidad a la presión** y **estabilización de trazo**
  activada en Photoshop.
- **Tutorial de cel-shading en Photoshop paso a paso**: [Creative Bloq —
  Create manga-style
  artworks](https://www.creativebloq.com/animation/create-manga-style-artworks-2118703)
  ⚠️ (una fuente, tutorial genérico no específico de Demon Slayer, pero
  explica el método de capas de sombra plana + *multiply* que sí coincide
  con el cel-shading de la serie).
- **Tramas y grano de papel**: ya resueltos por el investigador de
  imagen en el punto 19 (Clip Studio Assets, GraphicsBunker); no se
  repite aquí. Para el **pincel de tinta de Clip Studio** (si se usa CSP
  en vez de Photoshop): [Manga Line Brush — Clip Studio
  Assets](https://assets.clip-studio.com/en-us/detail?id=1707223) y [15
  Free Clip Studio Paint Brushes for Manga-Style, por artwithrod
  (DeviantArt)](https://www.deviantart.com/artwithrod/art/15-Free-Clip-Studio-Paint-Brushes-for-Manga-Style-1019425750)
  ✅ (dos fuentes de pinceles gratis, formatos distintos a los ya citados
  en `imagen.md`, que sólo cubrió tramas, no línea).

#### 18.5 Resumen: rasgos que no cambian nunca (para la guía de IA, §18 ya
existente en la biblia como «Guía para generar con IA» del punto 17 —
esto es material nuevo de técnica, no lo repite)

- Personaje = **línea limpia + cel-shading plano de 2-3 tonos**; fondo y
  efectos = **3D con luz fotorrealista** (agua, fuego, humo) que
  contrasta a propósito con el personaje plano; nunca lo inverso.
- Cámara con **temblor** en los golpes, encuadre **centrado**, luz de
  color que **anuncia** el ataque antes del impacto.

### Punto 24 · Obras parecidas y temas relacionados

#### 24.1 Series de tono o estilo parecido (más allá de `datos-texto.md`)

`datos-texto.md` ya trae las 15 recomendaciones de usuarios de AniList
(Jujutsu Kaisen, Dororo, Bleach, MHA T4, Black Clover, Hell's Paradise,
Rurouni Kenshin, HxH, FMAB, Akame ga Kill, Naruto, InuYasha, Seraph of the
End…): no se repite esa lista aquí. Lo nuevo:

- Todas comparten el molde **shōnen de Shūeisha con acción por
  «respiraciones»/técnicas con nombre y niveles de poder crecientes**;
  por tono visual (ukiyo-e, época histórica, sangre estilizada), la más
  cercana en este servidor es **Jujutsu Kaisen** (mismo tipo de marca en
  el cuerpo — la del punto 25 —, mismo formato de «técnicas con nombre»).

#### 24.2 Influencias que el propio autor reconoce (con fuente directa,
no fandom)

- **JoJo's Bizarre Adventure, Bleach y Naruto**: Gotouge las nombró como
  sus **«tres mayores influencias de manga»** en una entrevista por
  *twitcast* del 31-oct-2016 (recogida por la wiki japonesa de la
  serie) ✅ (dos fuentes: [ScreenRant — Demon Slayer's Creator Confirms
  Their One Surprising Manga
  Influence](https://screenrant.com/demon-slayer-jojos-bizarre-adventure-surprising-influence/),
  que cita el `twitcast` original, + la [entrevista al editor Tatsuhiko
  Katayama en livedoor News](https://news.livedoor.com/article/detail/17760339/),
  que por separado confirma: «先生は『ジョジョの奇妙な冒険』はファンだと
  おっしゃっています» — el editor dice que la autora es fan de JoJo, y
  que la **técnica de la Respiración Total** recuerda a la **Onda /
  Hamon** de JoJo, la energía solar que activan con la respiración en las
  partes 1-2). La página original del *twitcast*
  (`w.atwiki.jp/kimetsunoyaiba/pages/64.html`) dio **403** en directo y
  su copia en Wayback **cortó la conexión dos veces** (máximo de
  intentos de AYUDANTE.md): queda citada sólo por las dos fuentes de
  prensa de arriba, no vista de primera mano ⚠️.
- **Gintama**: el mismo editor cuenta que «先生は『銀魂』が大好き» (la
  autora adora Gintama), y que de ahí sale **el humor y los gags
  cómicos** que rompen la tensión en Kimetsu (los momentos chibi, las
  peleas de Inosuke) ✅ (livedoor; una sola fuente directa, pero es
  declaración de primera mano del editor, no especulación de fans) ⚠️
  (marcado ⚠️ por venir de una sola fuente, aunque es primaria).
- **Hunter x Hunter**: no es que Gotouge lo citara directamente, pero el
  propio editor explica que **Tanjiro se diseñó como un «personaje
  corriente» (普通の人)** rodeado de compañeros excepcionales, idea que un
  colega editorial le sugirió comparando con **Gon** de HxH ✅ (livedoor,
  misma entrevista) ⚠️ (una fuente).
- **Cambios de diseño reales, contados por el editor** (dato de técnica y
  de mundo a la vez): **Tomioka Giyu** iba a llevar un **kimono
  tradicional**; el editor pidió «más ambiente Taisho» y así salió el
  uniforme con **cuello mandarín** actual. **Rengoku** no tenía máscara
  de tengu al principio; cuando el editor dijo que «le faltaba impacto
  visual», Gotouge respondió «pensé que podría usar una máscara» y nació
  su diseño icónico ✅ (livedoor, entrevista directa al editor original,
  fuente única pero de primera mano — ⚠️ por ser una sola fuente).
- **Tanjiro empezó como personaje secundario** en el concepto original
  de la autora; **Nezuko con el bambú en la boca** sí fue idea propia de
  Gotouge desde el principio, no sugerencia editorial ✅ (livedoor) ⚠️.

#### 24.3 Qué otras láminas ya hechas en este servidor se parecen (para
no repetir ideas — comparado con `biblias/*/biblia.md`, sección 0 y 19 de
cada una)

| Serie ya hecha | Canal que propuso | Por qué se parece a Demon Slayer | Cómo evitar repetir |
|---|---|---|---|
| **Jujutsu Kaisen** (32) | ➕ CREAR SALA («Clase extra») y 🍟 General | mismo shōnen de Shūeisha, técnicas con nombre, marca en el cuerpo (Marca de Cazademonios ≈ Dominio/Técnica) | Demon Slayer usa **Aula** (voz), no «Crear Sala»: son canales distintos, pero **evitar el mismo gag de «clase extra»**: el ángulo de Demon Slayer es la **respiración física real** (aguante de aire), no una clase de técnica de combate |
| **Naruto** (30) | ıı・🎯・reto-de-la-semana y #general-doblaje («La barra de Ichiraku») | ambos con «técnicas por aliento/chakra» y un elenco de personajes con apodos | Demon Slayer no compite por el mismo canal; si se usa #general-doblaje alguna vez, **no repetir el formato «barra/mostrador con personaje sirviendo»**: usar el **escenario con telón rojo** (ya propuesto en la biblia, §0) en su lugar |
| **Fullmetal Alchemist: Brotherhood** (37) | #general-doblaje («El círculo de tiza»), 🎚️ Mesa de Trabajo, #staff | ambas obras con un **símbolo dibujado en el suelo/objeto** como icono central (círculo de transmutación ≈ tablilla del Secreto Taisho) | si Demon Slayer usara #general-doblaje, **no dibujar un símbolo en el suelo como en FMAB**: usar el **telón** o la **tablilla de madera**, que ya son el objeto propio de la serie (§0 y §7 de la biblia) |
| **Attack on Titan** (2) | **#📜・reglas** («Reglamento del cuartel», Levi limpiando) | ambas con **una organización militar con rangos y disciplina estricta** (Cuerpo de Cazadores ≈ Cuerpo de Exploración) | el ángulo del Aula de Demon Slayer es **entrenamiento físico de respiración**, no reglamento ni disciplina militar: no usar un «reglamento pegado en la pared» como en AoT |
| **My Hero Academia** (25) | #material-de-clase | ambas tienen una **escuela/academia con instructores** (Mansión Mariposa ≈ U.A. High) | el propio canal **#avisos-clases** ya usa como ejemplo «Clase 1 — Respiración y apoyo»: si se hace la lámina 2 del Aula, **usar el horario del Entrenamiento de los Pilares** (cada Hashira enseña una cosa, en orden), no un aula con pizarra como en MHA |

**Conclusión para el redactor**: el concepto ya propuesto en la biblia
(§0: **Aula** con Shinobu entrenando la respiración, y
**#que-estas-escuchando** con Zenitsu) **no repite ningún concepto visual
ya usado** en las 5 series de arriba: ninguna otra lámina usa un
**escenario de telón rojo**, una **tablilla de madera vertical**, ni un
**instrumento tocado de oído** (el *shamisen* de Zenko). Es el hueco que
queda libre.

#### 24.4 Temas relacionados (más allá de «obras parecidas»)

- El tema del **duelo y la familia perdida** conecta con **Violet
  Evergarden** (22, ya en este servidor) y **Frieren** (33): las tres
  tratan la pérdida y el paso del tiempo con un tono contemplativo, pese
  a que Demon Slayer es mucho más de acción.
- El tema de la **respiración como técnica de combate y de vida**
  (§0 de la biblia) no tiene equivalente directo en las demás láminas
  del servidor: es el ángulo más seguro para no chocar con nada ya hecho.

### Punto 25 · El mundo, la historia y sus símbolos

#### 25.1 Las reglas del mundo, en cinco líneas

1. Japón, **era Taishō** (1912-1926): trenes de vapor, quimonos y ya
   algo de ropa occidental conviviendo ✅ [Britannica —
   Demon Slayer](https://www.britannica.com/topic/Demon-Slayer) + wiki.
2. Los **demonios** (鬼, *oni*) fueron humanos corrompidos por la sangre
   de **Muzan Kibutsuji**; se regeneran de casi todo, necesitan comer
   personas para sobrevivir y hacerse fuertes, y **el sol los desintegra**
   ✅ [CBR — Demon Slayer's Nichirin Swords,
   Explained](https://www.cbr.com/demon-slayer-nichirin-swords-explained/)
   + wiki.
3. La única forma de matarlos del todo (aparte del sol) es **decapitarlos
   con una espada Nichirin** (日輪刀, «espada del disco solar»): forjada
   con **Arena de Hierro Escarlata** y **Mineral Escarlata**
   (猩猩緋砂鐵 / 猩猩緋鑛石) de la **Montaña de la Luz Solar** (陽光山),
   que absorbe sol todo el año; corta a nivel celular, así que el
   demonio no se regenera ✅ (dos fuentes: CBR + [wikitexto de la ficha
   «Nichirin Sword»](https://kimetsu-no-yaiba.fandom.com/wiki/Nichirin_Sword),
   `action=parse`). La espada **cambia de color al desenvainarla por
   primera vez** según cada dueño (de ahí «espada de color cambiante»),
   pero sólo si el dueño tiene suficiente nivel; si no, se queda negra.
4. Para pelear con ellos, los cazadores entrenan la **Respiración Total**
   (全集中の呼吸): respirar profundo constantemente multiplica su fuerza,
   velocidad y percepción; cada escuela de respiración tiene **Formas**
   (型) numeradas, todas derivadas de la **Respiración de la Danza del
   Dios del Fuego / Sol** (ヒノカミ神楽, la original) ✅ wiki + CBR.
5. El **Cuerpo de Cazadores de Demonios** (鬼殺隊, *Kisatsutai*) es una
   organización **no reconocida por el gobierno**, activa «desde tiempos
   antiguos»; la cita oficial de la wiki (voz de Urokodaki a Tanjiro):
   «*The Demon Slayer Corps. We number in the hundreds. An organization
   completely unrecognized by the government. Since ancient times, we
   have existed to hunt down demons*» ✅ (wikitexto, `action=parse`,
   página «Demon Slayer Corps»).

#### 25.2 La historia por arcos, con sus momentos clave

Fuente: [CBR — Every Demon Slayer Arc, In Order](https://www.cbr.com/demon-slayer-arcs-chronological-order/)
✅, cruzado con la wiki para capítulos/episodios exactos.

| # | Arco | Capítulos / episodios | Qué pasa | Momento clave |
|---|---|---|---|---|
| 1 | **Selección Final** | cap. 1-9 · ep. 1-5 | Muzan mata a la familia de Tanjiro; Nezuko sobrevive vuelta demonio; Tanjiro entra al Cuerpo | el examen de Urokodaki en la montaña de los lobos |
| 2 | **La Ciénaga del Secuestrador** | cap. 10-13 · ep. 6-7 | primera misión oficial de Tanjiro, contra el Demonio del Pantano | primer combate real fuera del entrenamiento |
| 3 | **Asakusa** | cap. 14-19 · ep. 8-10 | Tanjiro se cruza con Muzan en Tokio sin saberlo; conoce a Tamayo, una demonio que no ataca humanos | primer contacto (fallido) con el villano principal |
| 4 | **Mansión del Tambor** (*Tsuzumi*) | cap. 20-27 · ep. 11-14 | se unen **Zenitsu** e **Inosuke** al grupo | Zenitsu despierta su poder real dormido |
| 5 | **Monte Natagumo** | cap. 28-44 · ep. 15-21 | la Familia Araña; **Rui**, el primer miembro de los Doce Kizuki que aparece | Tanjiro despierta la **Danza del Dios del Fuego** (Hinokami Kagura) |
| 6 | **Entrenamiento de Rehabilitación** | cap. 45-53 · ep. 22-26 | presentación formal de los **Hashira** y de **Ubuyashiki**; se curan en la Mansión Mariposa | primera reunión de todos los Pilares |
| 7 | ***Mugen Train*** (película, 2020) | cap. 54-66 · ep. 27-34 | **Rengoku** se enfrenta a **Akaza** (Superior 3) | muerte del Pilar de la Llama |
| 8 | **Distrito de Entretenimiento** | cap. 67-97 · ep. 34-44 | se presenta **Tengen Uzui** (Pilar del Sonido) y sus 3 esposas; combate contra **Daki y Gyutaro** | primera victoria del grupo contra un Superior |
| 9 | **Aldea de los Herreros** | cap. 98-127 · ep. 45-55 | se revela que **Nezuko puede resistir el sol** | punto de giro para toda la trama del sol |
| 10 | **Entrenamiento de los Pilares** | cap. 128-136 · ep. 56-63 | calma antes de la tormenta: cada Hashira entrena a los demás en su especialidad | el «horario de clases» de los Pilares (§0 de la biblia) |
| 11 | **Castillo Infinito** | vol. 16-21 · cap. 137-183 | invasión final al castillo de Muzan; batallas contra varios Superiores | se revelan los orígenes trágicos de varios villanos |
| 12 | **Cuenta atrás hasta el amanecer** | vol. 21-23 · cap. 184-205 | batalla final contra Muzan antes de que salga el sol; Tanjiro se convierte brevemente en demonio y recupera su humanidad | final del trío principal; epílogo con sus descendientes en el siglo XXI |

#### 25.3 Emblemas, logos y objetos icónicos (nuevos, sin repetir los ya
medidos en `imagen.md` §19.2: insignia de glicinia, Marca de Cazador,
*tsuba*)

- **Jerarquía y vocabulario de rango** (para etiquetas o carteles de
  lámina 2), confirmado en el wikitexto de la ficha «Demon Slayer
  Corps» (`action=parse`, sección «Positions») ✅:
  - **Oyakata** (お館様, «Amo»): el líder, siempre de la familia
    Ubuyashiki.
  - **Cazadores de Demonios** (鬼狩り, *Oni-kari*): el grueso del Cuerpo.
  - **Hashira** (柱, «Pilares»): los más fuertes, cada uno maestro de una
    Respiración; su aprendiz se llama **Tsuguko** (継子).
  - **Cultivador** (育手, *Ikushu*): quien entrena a los aspirantes antes
    de la Selección Final (Urokodaki es uno).
  - **Kakushi** (隠, «los ocultos»): apoyo sin espada — curan, limpian el
    campo de batalla y **cosen los uniformes** de los cazadores.
  - **Herreros** (刀鍛冶, *Katanakaji*): forjan las espadas Nichirin, en
    la Aldea de los Herreros, escondida.
- **Los Doce Kizuki** (十二鬼月, *Jūni Kizuki*, «Doce Lunas Demonio»): los
  demonios más fuertes al mando directo de Muzan, cada uno con más
  sangre de Muzan que el resto; se dividen en **6 Superiores** (上弦,
  *Jōgen*) y **6 Inferiores** (下弦, *Kagen*), numerados 1 (más fuerte) a
  6; los Superiores llevan **el kanji de su rango tatuado en el ojo
  derecho y el número en el izquierdo** ✅ (dos fuentes:
  [kimetsu-no-yaiba.fandom.com/wiki/Twelve_Kizuki](https://kimetsu-no-yaiba.fandom.com/wiki/Twelve_Kizuki)
  + resumen cruzado en la búsqueda web con
  [GamesRadar+](https://www.gamesradar.com/entertainment/anime-movies/demon-slayer-upper-moons-twelve-kizuki-ranks/)).
- **El cuervo mensajero** (鎹鴉) y la **Piedra afiladora** ya están en la
  biblia (§7); no se repiten.
- **Vocabulario que un fan reconoce al instante** (para textos cortos de
  la lámina, en su idioma original con romanización):
  - **全集中の呼吸** (*Zenshū Chū no Kokyū*) — Respiración Total (Concentración).
  - **型** (*Kata*) — Forma/técnica (p. ej. «Agua, Primera Forma»).
  - **鬼殺隊** (*Kisatsutai*) — Cuerpo de Cazadores de Demonios.
  - **柱** (*Hashira*) — Pilar.
  - **痣** (*Aza*) — la Marca del Cazador de Demonios (ya en `imagen.md`).
  - **日輪刀** (*Nichirin Tō*) — espada del disco solar.
  - **鬼** (*Oni*) — demonio.

#### 25.4 Lo que ya cubrió `imagen.md` (no se repite aquí)

Insignia de glicinia del Cuerpo, la Marca del Cazador, la *tsuba* grabada
por Hashira, y los patrones textiles (*ichimatsu*, *asanoha*, *uroko*) ya
están medidos y con equivalente libre en `partes/imagen.md` §19.1-19.2.

## Lo mejor para la lámina

1. **Regla de oro para el objeto 3D de la lámina**: personaje en
   cel-shading plano (Freestyle/Grease Pencil + Color Ramp de 2-3 tonos)
   sobre un **fondo u objeto con render realista** (luz de área, sombras
   suaves) — así es como ufotable compone de verdad (18.1-18.3), no un
   render 100% toon.
2. Hay **9 modelos 3D *rigueados* y descargables** (Tanjiro, Akaza,
   Rengoku, Nezuko, Inosuke, Giyu…) en Sketchfab, CC Attribution, listos
   para posar en Blender (18.3): ahorra modelar desde cero.
3. La luz **anuncia el ataque con color** (azul = espada, morado =
   enemigo, dorado = chispa) antes del golpe (18.2): útil para iluminar
   al personaje de la lámina según lo que esté diciendo.
4. El **Entrenamiento de los Pilares** (arco 10, §25.2) es literalmente
   «cada Hashira enseña una cosa, en orden»: encaja de forma directa con
   la lámina 2 del Aula/#avisos-clases ya propuesta en §0 de la biblia.
5. Ningún canal ya hecho en el servidor usa un **telón rojo de teatro**
   ni una **tablilla de madera vertical**: es el hueco visual libre
   (24.3) para que el Aula no se parezca a ninguna lámina anterior.

## No encontré

- ⚠️ **Filtros específicos de la animación** (grano, aberración
  cromática, *bloom*): ninguna de las entrevistas técnicas leídas
  (Autodesk AREA JAPAN, CGWORLD/NVIDIA, Sakuga Blog) los menciona por su
  nombre; busqué «ufotable film grain chromatic aberration compositing»
  y «鬼滅の刃 撮影 グレイン フィルター» sin resultado técnico (sólo
  reseñas que dicen «se ve cinematográfico», sin detalle).
- ⚠️ **Qué plumilla o tableta usa Gotouge exactamente**: confirmé que
  dibuja el manga a mano/analógico (18.1, exposición de originales +
  entrevista al editor sobre fax/teléfono), pero no encontré marca de
  plumilla ni si usa una tableta para retoques; busqué «吾峠呼世晴 Gペン»
  y «吾峠呼世晴 使用画材» sin una fuente que lo confirme.
- ⚠️ La página original del *twitcast* del 31-oct-2016
  (`w.atwiki.jp/kimetsunoyaiba/pages/64.html`) donde Gotouge nombra sus
  tres influencias dio **403** en directo, y su copia en Wayback
  **cortó la conexión dos veces** (máximo de intentos): la cita queda
  con dos fuentes de prensa que la reproducen (ScreenRant + livedoor),
  no con el texto original.
- ⚠️ **Segunda fuente independiente** para lo que dice el editor
  Katayama sobre Gintama, Hunter x Hunter y los cambios de diseño de
  Giyu/Rengoku: es una sola entrevista (livedoor News); busqué «鬼滅の刃
  編集 片山 銀魂 影響» y «Kimetsu no Yaiba editor Gintama influence
  interview» sin una segunda fuente que repita esos detalles concretos
  (sí hay muchas que repiten sólo lo de JoJo).
- ⚠️ **TV Tropes**, página de «Similar Works» o «Influences»: sigue
  bloqueada (403) como ya constaba en la bitácora principal; no reintenté
  (ya se había gastado el máximo de dos intentos con Wayback en la
  biblia principal).
- ⚠️ No encontré un *making of* en vídeo (oficial, con subtítulos) donde
  el equipo de arte hable de encuadres específicos por emoción; lo de
  18.2 sale de un ensayo de análisis (jb siraudin) y de Sakuga Blog, no
  de una entrevista del propio estudio sobre composición.

## Bitácora

### Red

- **Funcionó**: WebSearch (16 búsquedas), WebFetch (10 páginas), API de
  Sketchfab (curl directo, 2 consultas), API de Kimetsu no Yaiba Wiki
  (`action=parse` con `curl`, 3 consultas, sin repetir las de
  `datos-texto.md`).
- **Bloqueado**: `w.atwiki.jp` (403 en directo; su copia en Wayback
  cortó la conexión dos veces, sin insistir más — máximo de intentos de
  AYUDANTE.md); WebFetch no puede leer `web.archive.org` directamente
  (error propio de la herramienta, no del sitio).

### Búsquedas web (16 del cupo de ~50, todas nuevas, no repiten
`datos-texto.md`)

| # | Idioma | Búsqueda | Qué dio |
|---|---|---|---|
| 1 | en | ufotable Demon Slayer animation technique 2D 3D CGI interview | blog jb siraudin, Popverse, Sakuga-adyacentes |
| 2 | ja | CGWORLD 鬼滅の刃 ufotable 制作 インタビュー | Autodesk AREA JAPAN (2 partes), CGWORLD/NVIDIA |
| 3 | ja | 吾峠呼世晴 漫画 使用画材 ペン インタビュー | nada específico de plumilla (⚠️) |
| 4 | en | Demon Slayer style toon shader Blender tutorial anime cel shading Freestyle | Yarsa DevBlog, Instructables, StraySpark |
| 5 | en | "Demon Slayer" Tanjiro rig free Blender download character model | Sketchfab (K-, Light.k, AbaKat) |
| 6 | en | sakugabooru OR "sakuga blog" Demon Slayer animation analysis key animator | Sakuga Blog 2019, animadores nombrados |
| 7 | en | Gotouge Koyoharu analog hand-drawn manga no digital interview Weekly Shonen Jump | nada directo (⚠️) |
| 8 | ja | 鬼滅の刃 吾峠呼世晴 アナログ 原稿 手描き 編集者 | discoverjapan-web.com (原画展), livedoor News (entrevista al editor) |
| 9 | en | Demon Slayer manga line art brush "Clip Studio" free download ufotable ink style | Clip Studio Assets (Manga Line Brush), DeviantArt |
| 10 | en | Gotouge Koyoharu influences manga inspirations interview | resultados genéricos, sin la cita concreta |
| 11 | en | Demon Slayer Total Concentration Breathing inspired by JoJo Hamon Ripple influence Gotouge | ScreenRant (confirma JoJo/Bleach/Naruto) |
| 12 | en | Photoshop anime manga line art brush free download inking cel shading tutorial | DeviantArt (Pearlpencil), Brusheezy, Creative Bloq |
| 13 | en | Demon Slayer story arcs in order list Final Selection … Infinity Castle | CBR (lista completa con capítulos) |
| 14 | en | Demon Slayer glossary terms Nichirin blade Twelve Kizuki Upper Lower Moon Total Concentration explained | CBR, GamesRadar+, wiki |
| 15 | en | Demon Slayer world rules explained Taisho era demons sunlight regeneration Nichirin sword ore | resumen cruzado con CBR |
| 16 | ja | 鬼滅の刃 影響を受けた漫画 吾峠 *(no llegó a lanzarse: cubierta por #11)* | — |

### Sin cupo (API, curl directo)

- API de Sketchfab: `search?type=models&q=Tanjiro%20rig&downloadable=true`
  y `q=demon%20slayer%20rigged` (2 consultas) + `GET /v3/models/<uid>`
  para 4 modelos (licencia, caras, autor).
- Kimetsu no Yaiba Wiki, `action=parse&prop=wikitext`: «Demon Slayer
  Corps» (2 veces, secciones distintas) y «Nichirin Sword» — 3 llamadas,
  ninguna repetida de `datos-texto.md` (que sólo trajo AniList y Steam).
- `action=query&list=search`: 2 consultas de comprobación (no aportaron
  página nueva, descartadas).

### Fuentes consultadas (32 enlaces distintos, en 21 dominios; 17 de esos
dominios son nuevos, ninguno de los 52 de la bitácora principal ni de los
~14 que sumó `imagen.md` — comprobado con `grep -o` sobre los tres
archivos)

**Entrevistas técnicas oficiales/de industria (5)**:
[Autodesk AREA JAPAN, parte 1](https://area.autodesk.jp/case/animation/kimetsu-01/) ·
[Autodesk AREA JAPAN, parte 2](https://area.autodesk.jp/case/animation/kimetsu-02/) ·
[CGWORLD × NVIDIA, ufotable](https://cgworld.jp/special-feature/202410-nvidia-hp-ufotable.html) ·
[Popverse — entrevista a Yuichi Terao](https://www.thepopverse.com/movies-demon-slayer-kimetsu-no-yaiba-yuichi-terao-interview-making-the-infinity-castle-feel-infinite) ·
[livedoor News — entrevista al editor Tatsuhiko Katayama](https://news.livedoor.com/article/detail/17760339/).

**Prensa sobre el autor (1)**: [Discover Japan — exposición de originales
de Gotouge](https://discoverjapan-web.com/article/74084).

**Análisis técnico de animación (2)**: [Sakuga Blog — The Power of
Ufotable's Harmony](https://blog.sakugabooru.com/2019/08/15/kimetsu-no-yaiba-the-power-of-ufotables-harmony/) ·
[jb siraudin — The Visual Design of Demon Slayer's
Combats](https://jbsiraudin.github.io/blog/demon-slayer-visual-grammar/).

**Cómo replicar en Blender (4)**: [Yarsa DevBlog — Toon Shading Effect in
Blender](https://blog.yarsalabs.com/basic-toon-shader-in-blender/) ·
[Instructables — Custom Toon Shader in
Blender](https://www.instructables.com/Custom-Toon-Shader-in-Blender/) ·
[StraySpark — How to Get an Anime / Toon Look in Blender
(2026)](https://www.strayspark.studio/blog/how-to-get-anime-toon-look-blender) ·
2 tutoriales en YouTube (Comfee, «ANIME in BLENDER!»).

**Modelos 3D con licencia (Sketchfab, 6 perfiles/modelos nuevos,
distintos de los 15 ya citados)**: Light.k (Tanjiro, Akaza, Rengoku,
Inosuke, Giyu, Nezuko, Teoni — serie completa) · AikoX (Nezuko) · K-
(Tanjiro ×2) · AbaKat (Tanjiro con *shapekeys*).

**Cómo replicar en Photoshop / Clip Studio (4)**: [DeviantArt — Manga
Brush Line for Photoshop (Pearlpencil)](https://www.deviantart.com/pearlpencil/art/Manga-Brush-Line-for-Photoshop-268440777) ·
[Brusheezy — Manga Ink](https://www.brusheezy.com/free/manga-ink) ·
[Creative Bloq — Create manga-style
artworks](https://www.creativebloq.com/animation/create-manga-style-artworks-2118703) ·
[Clip Studio Assets — Manga Line
Brush](https://assets.clip-studio.com/en-us/detail?id=1707223).

**Historia, mundo y glosario (3)**: [CBR — Every Demon Slayer Arc, In
Order](https://www.cbr.com/demon-slayer-arcs-chronological-order/) ·
[CBR — Demon Slayer's Nichirin Swords,
Explained](https://www.cbr.com/demon-slayer-nichirin-swords-explained/) ·
[GamesRadar+ — Upper Moons /Twelve
Kizuki](https://www.gamesradar.com/entertainment/anime-movies/demon-slayer-upper-moons-twelve-kizuki-ranks/).

**Obras parecidas (1)**: [ScreenRant — Demon Slayer's Creator Confirms
Their One Surprising Manga
Influence](https://screenrant.com/demon-slayer-jojos-bizarre-adventure-surprising-influence/).

**Wiki de la serie, páginas nuevas (2, mismo dominio ya citado pero
páginas distintas)**: [Nichirin
Sword](https://kimetsu-no-yaiba.fandom.com/wiki/Nichirin_Sword) ·
[Twelve Kizuki](https://kimetsu-no-yaiba.fandom.com/wiki/Twelve_Kizuki) ·
[Demon Slayer
Corps](https://kimetsu-no-yaiba.fandom.com/wiki/Demon_Slayer_Corps) ·
[Britannica —
Demon Slayer](https://www.britannica.com/topic/Demon-Slayer).

Sigue: investigar punto 18 (técnica del estudio, cómo replicar en Photoshop/Blender, encuadres), punto 24 (obras parecidas más allá de AniList, influencias del autor, comparación con otras láminas del servidor) y punto 25 (mundo, arcos de la historia, símbolos) — todo con fuentes nuevas, distintas de las 52+ ya citadas.
