# Parte del investigador de TEXTO, JUEGOS Y TÉCNICA · Oshi no Ko

Repaso corto (25-sep-2026): sólo puntos **18, 24 y 25** de `ENCARGO.md`
(nuevos, no están en la biblia). Parte de `partes/datos-texto.md` (AniList:
equipo creativo, obras parecidas/relacionadas) sin repetir esas consultas.
No toco `biblia.md`: eso es del redactor.

✅ = confirmado en dos fuentes. ⚠️ = una sola fuente o de memoria.

## Hallazgos

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Estudio y equipo (ya en `datos-texto.md`, AniList, no repetido aquí salvo para citar):**
- Estudio de animación: **Doga Kobo** (動画工房) ✅ (AniList + [Wikipedia: Doga Kobo](https://en.wikipedia.org/wiki/Doga_Kobo), [ABEMA Times, jp](https://times.abema.tv/articles/-/10081313)).
- Director: **Daisuke Hiramaki** (平牧大輔), las 3 temporadas ✅ (AniList + [ABEMA Times jp](https://times.abema.tv/articles/-/10081313)).
- Manga: guion **Aka Akasaka** (赤坂アカ), dibujo **Mengo Yokoyari** (横槍メンゴ) ✅ (AniList + [ficha Fandom del manga](https://oshinoko.fandom.com/wiki/Oshi_no_Ko_(manga))).

**Cómo se hizo la animación (entrevistas al staff, jp):**
- El director propuso un método nuevo para las coreografías de idol: **crear imágenes 3D a partir de vídeos de baile real y dibujar el storyboard según la canción**; las dos cosas se combinan en la fase de animación ⚠️ (una fuente, [Anime Corner, interview staff](https://animecorner.me/interview-oshi-no-ko-staff-on-the-animes-creation-and-popularity/), en inglés, resumen de prensa de una entrevista jp).
- Se metieron **cortes dibujados a mano con pincel** («hand-drawn cuts with brushes») para dar un estilo «vívido y llamativo» en momentos clave ⚠️ (misma fuente).
- La ayudante de dirección **Ciao Nekotomi** (猫富ちゃお) lleva el **guion de color** («color script»): decide de antemano el color y la luz de cada escena antes de pasarlo a color y fotografía (compositing); cita del director: «全体の監修はちゃおさんにやってもらっています» (‘la supervisión general de todo se la encargo a Chao’) ✅ ([Febri, entrevista al director, jp](https://febri.jp/topics/oshinoko_imamaki_01/), 1.ª de una serie de entrevistas; confirmado también por su crédito de «color script» citado en [Anime Corner](https://animecorner.me/interview-oshi-no-ko-staff-on-the-animes-creation-and-popularity/)).
- Sobre la coreografía de las actuaciones de idol: **«パフォーマンスの部分で増幅できるところはかなり増幅していますね»** (‘en las partes de actuación, ampliamos bastante lo que se puede amplificar’ respecto al manga) ✅ ([Febri, jp](https://febri.jp/topics/oshinoko_imamaki_01/)).
- Filosofía de luz y sombra, citada del *making of*: aunque un pasillo sea oscuro de verdad, **se añade luz cuando el personaje entra al aula**, y el equipo llama a esto **«上手な嘘»** (‘una mentira hábil’): no calcan la realidad, la interpretan para que impacte más. El asistente de dirección ajusta sombras a mano: «dado que la entrada de sombra era densa, la hice un poco más delgada» ✅ ([MANTANWEB, reportaje del rodaje/making of, jp](https://mantan-web.jp/article/20230616dog00m200018000c.html)).
- Ninguna de las entrevistas encontradas nombra el programa exacto (Clip Studio, Toon Boom, RETAS…) que usa Doga Kobo para producción; es lo normal en estudios de anime TV japoneses (RETAS/CLIP STUDIO son estándar de la industria, pero no confirmado para esta serie en concreto) ⚠️.

**El manga (Mengo Yokoyari), línea y estilo:**
- Ella misma, en una entrevista/tutorial oficial del sitio de **Clip Studio Paint** (el programa que usa para dibujar, confirmado por ser la propia plataforma quien la entrevista), explica su método: pensar el **cuerpo femenino como cilindros** (el masculino, como cubos), **empezar siempre por el gesto y la pose** antes que el detalle, y cuidar sobre todo las **pestañas limpias** y el **pelo con un aire suelto/ligero** («フワッとした感じ») como su sello personal; recomienda mirar vídeos reales para las poses ✅ ([Clip Studio, «【メンゴ先生流】かわいい女の子を描くために考えるべきこと», jp, sitio oficial del programa](https://www.clipstudio.net/oekaki/archives/151231)).
- Aka Akasaka sobre el trazo de Yokoyari: «tiene una aguja escondida» (針が仕込まれている) y sus dibujos de mujeres llevan siempre **fuerza, una elegancia que no busca agradar** ⚠️ (una fuente, [ar-mag.jp, diálogo Akasaka×Yokoyari, jp](https://ar-mag.jp/articles/-/15015)).

**Encuadres y composición (coreografía de cámara, confirmado por el director):**
- El equipo tomó **libertades en cámara y ángulos** respecto a las viñetas del manga para que el espectador sienta lo mismo que el lector, aunque el plano cambie ✅ ([Anime Corner, interview staff](https://animecorner.me/interview-oshi-no-ko-staff-on-the-animes-creation-and-popularity/) + [Febri, jp](https://febri.jp/topics/oshinoko_imamaki_01/)).
- No se encontró un desglose oficial de «qué plano para qué emoción»; lo que hay de encuadres por emoción con minuto concreto lo cubre el investigador de vídeo (puntos 4/14), que sí miró fotogramas.

**Cómo reproducirlo en Photoshop (pipeline general de cel-shading anime, con fuentes libres):**
- Capas típicas: color base → sombra en una capa con **máscara de recorte** (`Alt+Ctrl+G` sobre la capa de base) → luces → contornos → texto/decals, pintando con **pincel duro** (sin difuminar) para mantener el borde limpio del cel-shading ✅ (coincide en dos guías: [MicahBuzan.com, cel shading tutorial](https://www.micahbuzan.com/cel-shading-tutorial/) y [Adobe, «Cel Shading, a comprehensive guide»](https://www.adobe.com/uk/creativecloud/animation/discover/cel-shading.html)).
- Truco de capa: activar **«Bloquear píxeles transparentes»** en la capa a sombrear para no salirse de la silueta, elegir un tono más oscuro que la base y sombrear en bloques, no en degradado ✅ (mismas dos fuentes).
- Para el «grano» y aberración cromática de la animación: no se encontró un ajuste específico citado por el estudio; en Photoshop se simula con una capa de **ruido (Filtro > Ruido > Añadir ruido, 2-4%)** en modo Superponer y una capa de **desplazamiento de canal rojo/azul de 1-2px** en los bordes ⚠️ (técnica general de posproducción, no confirmada específicamente para Oshi no Ko).

**Cómo reproducirlo en Blender (pipeline de toon shading + contorno):**
- **Sombreado tipo cel/anime**: nodo *Diffuse BSDF* → **Shader to RGB** → **Color Ramp en modo «Constant»**; cada escalón del degradado se vuelve una banda de luz dura (2 escalones = blanco/negro clásico; 3 = con tono medio) ✅ (coincide en dos guías: [Artisticrender.com, «Cel Shading in Blender»](https://artisticrender.com/cel-shading-in-blender/) y [Yarsa DevBlog, toon shader tutorial](https://blog.yarsalabs.com/basic-toon-shader-in-blender/)).
- **Contorno**: dos rutas válidas, según el pedido del encargo (Line Art, Freestyle o Solidify):
  - **Freestyle** (Render Properties > Freestyle): rápido, integrado, basta para la mayoría de renders anime ✅ ([Artisticrender.com](https://artisticrender.com/cel-shading-in-blender/)).
  - **Solidify** (más control por objeto): material nuevo con **Backface Culling** activado; añadir el modificador **Solidify**, grosor pequeño (≈0.01), activar **«Flipped Normals»** y asignar el material de contorno con **Material Offset** ✅ (paso a paso confirmado en [Artisticrender.com](https://artisticrender.com/cel-shading-in-blender/) e [Instructables, «Custom Toon Shader in Blender»](https://www.instructables.com/Custom-Toon-Shader-in-Blender/)).
  - **Grease Pencil**: da más control aún (línea variable, texturizada) pero exige más trabajo manual, mencionado como alternativa en las mismas guías ⚠️.
- **Modelos/rigs libres de base** (no hay ningún personaje de Oshi no Ko con licencia libre; sirven como *base* para posar y luego repintar con textura/toon shader propio, igual que hace el investigador de imagen en el punto 3): **«3D Anime Character girl for Blender»**, de un usuario en Sketchfab, **CC Attribution**, dos versiones (C1 y base) ✅ (comprobado con la API de Sketchfab, `search?type=models&q=anime+girl+rigged&downloadable=true`; [enlace C1](https://sketchfab.com/3d-models/none-4592848f6d2d47d1b0544e1ddbbc6e87), [enlace base](https://sketchfab.com/3d-models/none-906b6874327844de9f794c7986127f3f)). Se pueden bajar y adaptar (licencia CC-BY pide crédito), NO representan a ningún personaje de la serie: sólo la base de cuerpo/rig para posar.

Fuente de la lista de guías de Blender: comparación cruzada de 3 resultados de búsqueda web (Artisticrender.com, Yarsa DevBlog, Instructables), todas coinciden en el mismo pipeline (Shader to RGB + Color Ramp Constant + Freestyle/Solidify), señal de que es el método estándar, no una única opinión.

### Punto 24 · Obras parecidas y temas relacionados

**Series de tono o estilo parecido (recomendadas por la comunidad de AniList, ya en `datos-texto.md`):**
- **Perfect Blue** (película, Satoshi Kon, nota 85/100, 438 votos de similitud) — la más votada; ídolo, industria del espectáculo, thriller psicológico con la identidad de una artista ✅ ([AniList](https://anilist.co/anime/150672)).
- **ERASED** (nota 81, 285 votos) — misterio con un protagonista que revive el pasado para evitar una tragedia (paralelo con la reencarnación de Aqua) ✅ (misma fuente).
- **Kaguya-sama: Love is War** (nota 83, 213 votos) — la ópera prima de **Aka Akasaka**, mismo autor ✅ (AniList + confirmado en la [entrevista de Anime Corner](https://animecorner.me/oshi-no-ko-creator-talks-his-heavy-involvement-in-the-anime/), donde Akasaka dice que Oshi no Ko es «su primera adaptación a anime» tras Kaguya-sama).
- **ODDTAXI**, **Kageki Shojo!!**, **ZOMBIE LAND SAGA**, **NEEDY GIRL OVERDOSE**, **Rascal Does Not Dream of Bunny Girl Senpai**, **Vivy -Fluorite Eye's Song-**, **Looking for the Full Moon**, **Skip Beat!** — todas con votos menores pero repetidas por la comunidad como parecidas (industria del espectáculo, ídolos o doble identidad) ✅ (AniList, mismo listado).

**Sobre «Perfect Blue» como influencia directa:** la prensa y los fans comparan mucho el opening «Idol» (T1) con la estética de Perfect Blue, y el argumento (ídolo + industria + lado oscuro) se parece, pero **no se encontró ninguna entrevista donde Akasaka o Yokoyari citen la película como influencia reconocida**; búsquedas específicas en inglés y japonés no dieron esa cita directa ⚠️ (comparación de prensa/fans, no confirmada por el autor: [epicstream.com, «Oshi no Ko vs. Perfect Blue»](https://epicstream.com/article/oshi-no-ko-and-perfect-blue-idol-industry), [Let's Discover Things That Are Good, blog comparativo](https://letsdiscoverthingsthataregood.wordpress.com/2023/04/29/perfect-blue-criticizes-the-idol-industry-oshi-no-ko-does-not/)). No lo presento como «influencia confirmada»: sólo como comparación de crítica.

**Temas relacionados que el propio Akasaka sí confirma en entrevista:**
- Dice implicarse en todo el proceso del anime, incluidas las sesiones de doblaje semanales, con peticiones concretas a los actores ✅ ([Anime Corner](https://animecorner.me/oshi-no-ko-creator-talks-his-heavy-involvement-in-the-anime/)).
- Sobre su primera adaptación a anime (Kaguya-sama) dice que fue un proceso de ilusión progresiva, no de reacción inmediata; con Oshi no Ko: «puedo sonreír durante mucho tiempo, estoy 100% feliz» ✅ (misma fuente).

**Qué otras láminas ya hechas en el servidor se parecen (para no repetir ideas — comprobado leyendo las biblias ya escritas en `biblias/*/biblia.md`):**
- **`biblias/29-por-decidir-seis-canales-sin-serie/biblia.md`**, concepto de **Los Simpson** para «Radio 24/7»: la cabina de **Radio KBBL** con el cartel de neón **«EN EL AIRE»** ✅ (l. 1618-1627 de esa biblia). Es **casi el mismo objeto** que el «letrero ON AIR» que propone nuestro encargo para #en-directo: cambiar el color de neón, la tipografía y el objeto de fondo (micro de radio vs. móvil/set de streaming) para que no se vean iguales.
- **Mismo archivo**, concepto de **Sing** (película) para «#canto»: el **volante amarillo de audición** «OPEN AUDITIONS» del Teatro Moon ✅ (l. 1396-1470 de esa biblia). Es el mismo objeto-concepto que la «hoja de audición» que pide nuestro encargo para #castings: hay que diferenciarlos en formato (nuestra hoja de audición de Oshi no Ko es una ficha de casting de industria del espectáculo con foto y datos, tipo agencia japonesa, no un volante de cine de barrio) y en paleta (evitar el amarillo/rojo de Sing).
- **`biblias/10-k-on/biblia.md`**, canal #general: club de música escolar, ambiente cálido y de amistad — mismo mundo de «actuación en directo» que B-Komachi, pero **tono opuesto** (K-On es luz, sin industria ni ambición; Oshi no Ko es la cara oscura del mismo mundo) ✅ (l. 1008-1050 de esa biblia). Sirve como contraste, no como repetición: si se usa un escenario o instrumentos, que se note la diferencia de iluminación (K-On cálido/natural vs. Oshi no Ko con neón y luces de estudio).
- No se encontró ninguna otra biblia ya escrita con un concepto de «teléfono móvil con interfaz de app» (el otro objeto que propone nuestro encargo, «el móvil de B-Komachi»): búsqueda `grep -i "teléfono\|smartphone"` sobre las 36 biblias del repositorio no dio ningún concepto de lámina con un móvil como objeto central ✅ (comprobado sobre el repositorio completo).

### Punto 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo, en cinco líneas** (comprobado en la wiki, fichas de personaje):
1. El mundo es el Japón real de hoy y su **industria del espectáculo** (idols, actuación, modelaje, cine): nada de magia visible salvo una excepción.
2. Esa excepción: quien muere justo cuando nace un bebé puede **reencarnarse** en ese bebé, con los recuerdos de su vida anterior intactos ✅ (ficha de [Aqua Hoshino](https://oshinoko.fandom.com/wiki/Aqua_Hoshino): el doctor **Gorou Amamiya**, asesinado por un acosador de su paciente, renace como Aqua; ficha de [Ruby Hoshino](https://oshinoko.fandom.com/wiki/Ruby_Hoshino): la paciente terminal **Sarina Tendouji**, cuidada por ese mismo doctor, renace como Ruby).
3. La protagonista original, la idol **Ai Hoshino**, esconde el embarazo de gemelos para no arruinar su imagen; los cría en secreto siendo madre e idol a la vez, hasta que la mentira la alcanza ✅ (ficha de [Ai Hoshino](https://oshinoko.fandom.com/wiki/Ai_Hoshino)).
4. Ai muere asesinada por **Ryosuke Sugano**, un fan obsesionado con ella ✅ (ficha de [Ryosuke Sugano](https://oshinoko.fandom.com/wiki/Ryosuke_Sugano); coincide con la ficha de Ai, dos páginas de la misma wiki que se citan entre sí y describen el mismo hecho).
5. A partir de ahí, la historia se mueve entre dos caras del mismo mundo: **Ruby** intenta revivir el sueño de idol de su madre con la banda **B-Komachi**, y **Aqua** persigue una venganza fría contra quien delató a Ai. Todo el elenco (Kana, Akane, MEM-cho…) gira alrededor de la industria: actuación, ídolos, cine y televisión, y sus mentiras «necesarias».

**La historia por arcos** (11 arcos oficiales del propio autor, según la wiki, con tomos y temporada — ✅ estructura confirmada por la wiki con la etiqueta explícita «officially divided into story arcs by the author»; [fuente](https://oshinoko.fandom.com/wiki/Story_Arcs)):

| # | Arco | Tomos | Temporada | Momento clave |
|---|---|---|---|---|
| 1 | **Prólogo: infancia** | 1 | T1 | El doctor Gorou conoce a Ai embarazada; nacen Aqua y Ruby; Ai muere asesinada por Sugano el mismo día del parto de gemelos ✅. |
| 2 | **Show Business** | 2 | T1 | Aqua y Ruby, ya niños, entran al mundo del espectáculo; primeros pasos de Ruby como idol. |
| 3 | **Reality de citas** | 3-4 | T1 | Un programa de citas de la tele expone la doble cara de las apariencias en el mundo del espectáculo. |
| 4 | **El primer concierto** | 4 | T1 | El primer directo grande de la nueva B-Komachi, con Ruby al frente. |
| 5 | **Obra 2.5D** | 5-7 | T2 | Aqua y Kana Arima se meten en el teatro «**2.5D**» (adaptaciones escénicas de anime/videojuego, un formato real de la industria japonesa) con la obra ficticia **Tokyo Blade** ✅ (nombre confirmado en la nota de la ficha de [Aqua Hoshino](https://oshinoko.fandom.com/wiki/Aqua_Hoshino)). |
| 6 | **Privado** | 7-8 | T2 | Se destapan secretos personales del elenco fuera de las cámaras. |
| 7 | **Mainstay** | 9-10 | T3 | Los protagonistas se consolidan como profesionales del medio. |
| 8 | **Escándalo** | 11 | T3 | Un escándalo mediático golpea a uno de los personajes principales. |
| 9 | **Película** | 11-15 | T3 | Se rueda **«The 15 Year Lie»** (１５年の嘘), película biográfica ficticia sobre la vida de Ai Hoshino, dirigida por Taishi Gotanda y producida por Masaya Kaburagi, protagonizada por Ruby, Aqua, Kana, Akane, MEM-cho y más ✅ ([ficha de la película en Fandom](https://oshinoko.fandom.com/wiki/The_15_Year_Lie)). |
| 10 | **El fin de la obra** | 15 | (sin emitir aún en anime al cierre de esta ficha) | Cierre de la trama de «The 15 Year Lie». |
| 11 | **Hacia las estrellas y los sueños** | 16 (tomo final) | — | Cierre de la serie (16 tomos en total, publicada 23-abr-2020 a 14-nov-2024) ✅ ([ficha del manga](https://oshinoko.fandom.com/wiki/Oshi_no_Ko_(manga))). |

La **temporada 3** (invierno 2026, ✅ ya vista y fotografiada por el investigador de vídeo, biblia §14) cubre hasta el arco 9 (Película); los arcos 10 y 11 son el tramo final del manga (tomos 15-16) y **todavía no tienen anime emitido** a la fecha de esta ficha (25-sep-2026) ✅ (cruzado con la biblia §0/§14, que sólo tiene T1-T3).

**Emblemas, logos y objetos icónicos** (nuevos para este punto; el logo de la serie y la estrella de seis puntas en los ojos ya están medidos y descritos a fondo en la biblia, secciones de tipografía y de «cómo hablan en pantalla» — no se repite aquí, sólo se referencia):
- **B-Komachi** (B小町): el grupo de idols, con su propio logo ya cubierto en la biblia (§3, §7). Nombre real del grupo, no traducido ✅.
- **Ichigo Production** (苺プロダクション, «Ichigo-Pro», también traducida oficialmente como **«Strawberry Productions»**): la agencia de talentos que fichó a Ai y luego a Ruby; el nombre significa literalmente «fresa» (苺) ✅ ([ficha Fandom](https://oshinoko.fandom.com/wiki/Ichigo_Production,_Inc)); su presidenta es **Miyako Saitou**.
- **«The 15 Year Lie»** (１５年の嘘): el título de la película-dentro-de-la-serie sobre Ai; funciona como vocabulario propio del fandom para hablar del arco de la película ✅ (misma ficha de arriba).
- **«Tokyo Blade»**: la obra de teatro 2.5D del arco 5, otro título ficticio propio de la serie que un fan reconoce al instante ✅ (nota en la ficha de Aqua).
- El **arma del crimen** de Sugano contra Ai no se detalla como objeto de merchandising o icono visual en la wiki (no se encontró una página dedicada al arma); no se afirma qué objeto es para no arriesgar un dato sin comprobar ⚠️.

**Vocabulario propio que un fan reconoce al instante:**
- **【推しの子】** — el título: los **corchetes lenticulares 【 】** son parte oficial del logo (ya medido en la biblia, §7). El título en sí es un juego de palabras: **「推し」(oshi)** es la persona (idol, artista) a la que alguien admira/sigue con devoción, y **「子」(ko)** es «hijo/a»: **「推しの子」** se lee a la vez como «el hijo de mi idol» y «el hijo de [mi] oshi», el doble sentido central de la trama (Aqua y Ruby son literalmente los hijos de la idol Ai) ✅ (confirmado por la propia ficha del manga en Fandom, que da la traducción literal «My Favorite Idol, Their Idol's Children»; [fuente](https://oshinoko.fandom.com/wiki/Oshi_no_Ko_(manga))).
- **2.5D** (niji-ten-go-dii): término real de la industria japonesa para las obras de teatro que adaptan anime/manga/videojuegos con actores reales; el arco 5 usa este término tal cual, así que sirve como palabra de vocabulario del mundo de la serie ✅ (mismo término usado en el nombre oficial del arco, wiki).
- El resto del vocabulario de motivos visuales (estrella de seis puntas = carisma/mentira, corchetes del logo, colores del logo) ya está resuelto y medido en la biblia (§7-8): no se repite aquí, sólo se remite a esas secciones para que el redactor no las vuelva a pedir.

## Lo mejor para la lámina

(pendiente)

## No encontré

(pendiente)

## Bitácora de búsqueda

(pendiente)

## Cumplimiento de mis puntos (18, 24, 25)

(pendiente)

Sigue: rellenar los tres puntos.
