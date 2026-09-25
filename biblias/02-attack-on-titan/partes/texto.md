# Parte de TEXTO · repaso corto (puntos 18, 24, 25 y lo nuevo del 5) · Attack on Titan

Escrito por el investigador de texto del repaso. Parto de `partes/datos-texto.md` (no repito
esas consultas) y de lo que ya tiene `biblia.md` (miré `seccion.py --rol texto` y la tabla de
«Cumplimiento del encargo»: los puntos 18, 24 y 25 **no estaban** en esa tabla — es justo lo
que falta). El redactor decide dónde y cómo meter esto en `biblia.md`; aquí dejo los datos
comprobados, con fuente y ✅/⚠️.

---

## Hallazgos

### Punto 5 (nuevo) · Una letra según cada uso

El punto 6 de `biblia.md` (letras) ya cubre: **logo/título** (a mano; Ditty/Linotext, no
imitar), **cartel del mundo** (ficha «Información pública» → Shippori Mincho B1; sentencias →
IM Fell English) y **subtítulos/créditos** (Cormorant Garamond / Cinzel). Faltaban 5 usos:
**globo normal, grito, pensamiento, onomatopeya e interfaz**. Los busqué y comprobé letra a
letra con fontTools (script en `/tmp/claude-0/trabajo/02-texto/fonts/`, descargado de
`raw.githubusercontent.com/google/fonts`).

- **Pensamiento (monólogo interior)**: en el manga japonés, un lector identificó la fuente
  exacta del monólogo de Shingeki no Kyojin como **「じゅん34」(Jun 34) de Morisawa**, una
  gótica redondeada (*maru gothic*) — ✅ pregunta y respuesta aceptada en
  [Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q12276462092)
  (el autor de la pregunta confirmó la solución). Jun 34 es de pago. Probé su prima libre más
  cercana, **Kosugi Maru** (Google Fonts): con fontTools, **le faltan tildes, ñ, ¿ y ¡** en
  sus subsets `latin` y `latin-ext` de Fontsource (comprobado bajando el `.woff2` de
  `cdn.jsdelivr.net/fontsource/fonts/kosugi-maru@latest/`). Por eso uso **Zen Maru Gothic**
  ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/zenmarugothic/METADATA.pb),
  OFL): misma familia redondeada, y con fontTools **trae completos** á é í ó ú Á É Í Ó Ú ñ Ñ
  ¿ ¡ ü Ü. Uso: texto sin bocadillo, pegado al fondo, para el monólogo interior de un
  personaje (así lo hace el manga: nada de burbuja, según los foros de manga consultados
  — ⚠️ un solo hilo, ninguna fuente oficial lo confirma en AoT en concreto).
- **Globo normal (diálogo)**: la rotulación del manga en inglés es de Steve Wands (Kodansha
  USA) y no identifiqué su fuente exacta (ya en §20 de `biblia.md`, sigue sin resolver: la
  ficha de biblioteca no la nombra). Como letra libre para un globo de diálogo corriente,
  legible y no genérica (nada de Comic Sans real), uso **Comic Neue**
  ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/comicneue/METADATA.pb),
  OFL; completa con fontTools: sin faltantes en tildes, ñ, ¿, ¡).
- **Grito**: letra libre **Bangers** ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/bangers/METADATA.pb),
  OFL; completa con fontTools), la clásica de cómic para mayúsculas gritadas, gruesa e
  inclinada por las esquinas.
- **Onomatopeya**: letra libre **Bungee** ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/bungee/METADATA.pb),
  OFL; completa con fontTools), de trazo grueso y geométrico, para clavar sobre la
  ilustración como los efectos de sonido en katakana del manga (ver punto 18 más abajo:
  Isayama usa juegos de palabras en sus onomatopeyas — [ANN, EN](https://www.animenewsnetwork.com/interest/2019-09-21/attack-on-titan-japanese-sound-effects-are-full-of-goofy-puns/.151195) ·
  estudio académico sobre las 99 onomatopeyas del tomo 1, con su categorización, en
  [JLA/UGM](https://journal.ugm.ac.id/jla/article/view/92270)). ✅ (dos fuentes).
- **Interfaz**: en `biblia.md` §12 ya está medido que los menús de *Attack on Titan 3* usan
  una **«sans humanista cursiva, en blanco roto»**. La letra libre más parecida y completa es
  **Jost, en su estilo Italic**
  ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/jost/METADATA.pb), OFL;
  descargué `Jost-Italic[wght].ttf` y con fontTools **no le falta nada**: tildes, ñ, ¿, ¡).
- **Tabla resumen para pegar en `biblia.md` §6**:

| Uso | Real (fuente) | Letra libre | Licencia | Tildes/ñ/¿/¡ (fontTools) |
|---|---|---|---|---|
| Globo normal | rotulación EN de Steve Wands, fuente sin identificar | Comic Neue | OFL | completas |
| Grito | mayúsculas gruesas del manga (visual, sin fuente digital) | Bangers | OFL | completas |
| Pensamiento | Jun 34 (Morisawa), de pago — confirmado por un lector en Yahoo Chiebukuro | Zen Maru Gothic (Kosugi Maru descartada: le faltan) | OFL | completas |
| Onomatopeya | katakana con juegos de palabras (Isayama) | Bungee | OFL | completas |
| Interfaz (*AoT 3*) | sans humanista cursiva, blanco roto (medido en demo, §12) | Jost Italic | OFL | completas |

---

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**18.1 Isayama, a mano y «feo a propósito» (entrevista traducida, primaria)** ✅

En una entrevista de 2014 (traducida al inglés,
[mangabrog](https://mangabrog.wordpress.com/2014/12/24/interview-with-hajime-isayama-creator-of-attack-on-titan-better-to-have-memorable-art-even-memorably-bad-art-and-stand-out/)),
Isayama dice que dibuja **totalmente a mano, en analógico**: «I get the feeling that I
wouldn't be able to get my art right if I were to do it digitally». Su original **es
literalmente tridimensional**, de tanto rascar el papel grueso y ponerle corrector líquido
encima («digging into the thick paper and slathering on white-out»). Dice que de niño ya
dibujaba «cosas feas» y que prefiere «memorable, incluso memorablemente malo» a genérico.
Confirma influencias directas: el manga *Parasyte* de **Hitoshi Iwaaki** (su «estilo
idiosincrásico»), *Hell Teacher Nube* (diseño de monstruos), el cine kaiju (Godzilla, Gamera),
*Muv-Luv Alternative* y, en animación, **Hideaki Anno** (*Evangelion*) por cómo dirige los
rayos láser y «el placer de la expresión animada». Segunda fuente sobre su línea:
[FIHEROE](https://www.fiheroe.com/blogs/anime-drawing-all-things-animation/attack-on-titan-manga-art-techniques-hajime-isayama)
y [Where Creativity Works](https://wherecreativityworks.com/illustrator-study-hajime-isayama/)
coinciden en que usa **muchísimo cross-hatching** (tramado a pluma cruzado) para las sombras y
la tensión emocional de las caras, con línea **irregular a propósito** para que el mundo se
sienta inestable. En una entrevista de ClipStudio ([clipstudio.net](https://www.clipstudio.net/oekaki/archives/152645))
Isayama cuenta que se entrenó copiando página completa (**模写**, *mosha*) de George Morikawa
y Seio Seio antes de serializar: no hay mención de qué programa usa hoy (⚠️, sin resolver;
Clip Studio Paint lo usó como imagen de portada de un libro de consejos para mangakas, pero
eso no confirma que sea su programa — [búsqueda EN sin fuente concluyente]).

**18.2 WIT Studio (T1-T3): 2D + 3DCG, capa de «maquillaje digital»**

- El director **Tetsurō Araki** (T1-T3) dirigió después *Death Note* y *Spy×Family*; en una
  entrevista sobre color y cinematografía ([fullfrontal.moe](https://fullfrontal.moe/tetsuro-araki/))
  dice que la belleza «surge de cómo se enfrentan la luz y la sombra», que usa mucho **destello
  de lente** (*lens flare*) por influencia del cineasta Shunji Iwai, y que **integrar fondos en
  3DCG con personajes en 2D es una técnica que él ayudó a estandarizar en la industria
  empezando en *Attack on Titan***. Usa *storyboard* en 3D (Storyboard Pro) para las escenas
  de acción. Su paleta en AoT es «pesada e intensa», y se volvió más colorida después (en Spy
  x Family). ✅ (coincide con lo ya medido en `biblia.md` §5: paleta apagada, verdes y ocres).
- El director de fotografía fue **Kazuhiro Yamada** ([ANN](https://www.animenewsnetwork.com/encyclopedia/people.php?id=25502));
  no hallé una entrevista suya sobre grano o aberración cromática en concreto (⚠️, sin
  resolver).
- El **3DCG lo hizo el estudio MADBOX** dentro de WIT, con **Shūhei Yabuta** como director de
  CG (ya en `partes/datos-texto.md`, AniList); se usó desde el principio para el **equipo de
  maniobras (ODM), la cámara siguiendo el vuelo y los caballos** —
  [SlashFilm](https://www.slashfilm.com/834201/the-anime-that-inspired-attack-on-titans-shift-to-cgi/) ·
  [UK Anime Network, entrevista a WIT](https://uk-anime.net/articles/titans_of_animation_-_the_wit_studio_interview.html).
  El director de *Final Season* parte 1, Yuichirō Hayashi, dijo a *Japan Forward* que se
  inspiró en el uso de CGI de *Dorohedoro*, en la que trabajaba justo antes.
- **Técnica de «maquillaje digital»** (temporada 2): un grupo de artistas digitales
  retocaba el *inbetweening* para dar textura de ilustración — sobre todo en primeros planos
  de pelaje y ojos de titanes —, técnica bautizada «Special Effects For Living Beings»,
  liderada por Chie Yamazaki y heredada de su prueba en *Kabaneri* —
  [Sakuga Blog](https://blog.sakugabooru.com/2017/04/13/attack-on-titan-season-2-production-notes-1-2/)
  (blog especializado en animación japonesa, fuente técnica de referencia). Los caballos casi
  siempre van en 3DCG «porque son la pesadilla de los animadores».

**18.3 MAPPA (temporada final): más CG, más fiel al manga, polémica**

- Con el cambio de estudio, **WIT hacía parte a mano y parte en CGI; MAPPA hace más en CG**
  ([Gamerant](https://gamerant.com/attack-on-titan-who-did-it-better-wit-studio-vs-mappa/) ·
  [AnimeIgnite](https://animeignite.com/wit-to-mappa-aot-final-season/)). MAPPA sigue **más de
  cerca las proporciones del manga** (WIT las había cambiado un poco), con un estilo descrito
  como «más realista», que dividió al fandom (episodios con dibujo irregular fueron muy
  comentados). WIT destacaba en la acción del ODM; MAPPA, en el peso de los combates de
  titanes y el *rotoscoping* — [CBR](https://www.cbr.com/attack-on-titan-season-4-premiere-maapa-wit-animation-differences/) ·
  [Twinfinite](https://twinfinite.net/features/mappa-didnt-deserve-the-hate-for-attack-on-titans-final-season/).
  ✅ (tres fuentes coinciden en «más CG, más fiel al manga, discutido»).

**18.4 Sombreado y filtros (lo medido en `biblia.md` + esto)**

Ya en `biblia.md` §18 (guía IA): «sombra en dos tonos, dura, poco brillo» y «contorno negro
fino con muchas líneas de tensión». Encaja con el cross-hatching de Isayama (18.1) trasladado
a cel-shading duro en el anime. No encontré una entrevista específica sobre grano de película
o aberración cromática en AoT (⚠️); son efectos estándar de posproducción de anime de 2013
(viñeteado suave, grano fino, algo de *bloom* en luces de antorcha y linternas — ya medido en
hex en `biblia.md` §5, p.ej. `#D29258` de antorcha).

**18.5 Cómo reproducirlo en Photoshop**

- **Capas**: línea (Multiplicar, negro `#0D0D0D`–`#1A1A1A`) sobre color plano; una capa de
  sombra dura recortada (*clipping mask*) al 100 % opacidad, sin difuminar el borde (para el
  «dos tonos» de §18.4); una capa de textura de papel/grano al 8-12 % en modo Superponer; una
  capa de viñeta sutil.
- **Pinceles**: uno de tinta dura (sin presión en el borde) para el contorno; uno de trama
  cruzada (*cross-hatch*) a mano o el patrón de medios tonos de Photoshop (Filtro > Trama de
  medios tonos) para tramas de manga, imitando lo de 18.1.
- **Ajustes**: Curvas para subir el contraste de la sombra (banda dura, no degradado), Balance
  de color hacia verde-ocre en las sombras (la paleta apagada de §5), y una capa de grano
  (Filtro > Ruido > Añadir ruido, 2-4 %, monocromático) para el look de anime de 2013.

**18.6 Cómo reproducirlo en Blender**

- **Shader tipo cel/toon** (nodos, método estándar y libre, sin add-ons de pago): Diffuse BSDF
  → **Shader to RGB** (sólo en Eevee) → **Color Ramp en modo Constante** (dos paradas para
  el clásico anime de dos tonos, tal como está medido en AoT) → multiplicar sobre el color
  base. Para que la sombra no quede sucia, los tutoriales recomiendan virar el tono de sombra
  hacia **azul o morado** en vez de sólo oscurecerlo — guía completa en
  [StraySpark Studio](https://www.strayspark.studio/blog/how-to-get-anime-toon-look-blender).
  Blender también trae un nodo nativo **Toon BSDF** (tamaño y suavizado del brillo) —
  [manual oficial de Blender](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/toon.html).
- **Contorno** (tres formas, todas gratis y nativas de Blender):
  1. **Line Art** (modificador de rejilla, desde Blender 2.93): contorno vectorial limpio,
     grosor constante en píxeles, el más parecido al manga —
     [tutorial](https://www.classcentral.com/course/youtube-easy-real-time-toon-shader-outlines-with-new-blender-2-93-line-art-feature-222968).
  2. **Freestyle** (motor de render de líneas, nativo): más lento, pero permite variar grosor
     por ángulo de cámara (bueno para las líneas de tensión de Isayama).
  3. **Solidify invertido**: modificador Solidify con grosor negativo, normales invertidas y
     un material negro con «Backface Culling»; la envoltura negra sólo se ve en el borde de
     la silueta. Limitación: el grosor es en unidades del mundo, no en píxeles, así que varía
     con la distancia a cámara.
- **Luz y render**: una sola luz Sol fuerte, para un borde de sombra limpio (igual que la
  «sombra dura» ya medida); cambiar **Color Management > View Transform** de AgX (el nuevo
  valor por defecto de Blender) a **Estándar**, porque AgX aplana los colores planos y
  saturados que pide el estilo anime — mismo tutorial de StraySpark.
- **Modelos y *rigs* libres** (comprobados por la API de Sketchfab, 24-sep-2026, todos **CC
  Attribution** y descargables):

| Modelo | Autor | Caras | Tiene esqueleto | Enlace |
|---|---|---|---|---|
| **Levi Ackerman rig** | ianadrielbravo | 29 423 | ✅ (lo dice el nombre y la ficha) | [01ffa989…](https://sketchfab.com/3d-models/01ffa989559941ef807cc07b3fed40b8) |
| Eren - attack on titan | AZlZ | 9 409 | por comprobar al descargar | [e249261e…](https://sketchfab.com/3d-models/e249261e7d4a4bb48ffbd0a7f84001a0) |
| Aot Smiling Titan rig | ianadrielbravo | 18 196 | ✅ | [d697d485…](https://sketchfab.com/3d-models/d697d4856d724144beccfd7471d9f5c9) |
| Aot female_titan | ianadrielbravo | 14 902 | por comprobar | [05aec839…](https://sketchfab.com/3d-models/05aec8398757451fb9ceed7b304f4ab1) |
| Beast Titan rig | ianadrielbravo | 24 306 | ✅ | [fa271e04…](https://sketchfab.com/3d-models/fa271e0452394ca6bece9fdefd5287d7) |
| Aotwa_armin_arlelt rig | ianadrielbravo | 26 531 | ✅ | [eb79c080…](https://sketchfab.com/3d-models/eb79c080ba4645df8246bcf81ae8c759) |
| Aot sasha braus rig | ianadrielbravo | 18 117 | ✅ | [625e1d01…](https://sketchfab.com/3d-models/625e1d017086400481faba3019da8e77) |

  Se descargan en glTF/FBX/OBJ desde Sketchfab (formatos que Blender importa con el
  esqueleto si el archivo lo trae; hay que revisarlo al bajarlo). Son de un mismo autor
  (ianadrielbravo), con **licencia CC BY**: hay que dar crédito exacto a «ianadrielbravo en
  Sketchfab» si se usan como base de pose, nunca para publicar el modelo tal cual (regla del
  punto 3 del encargo: fan art en 3D, sólo referencia). Sirven de referencia de pose y
  proporción; para la lámina final conviene retexturizar con la paleta medida en `biblia.md`
  §5, no dejarlos con su textura original.
- **Texturas encima**: reusar las de Poly Haven ya listadas en `biblia.md` §4.2
  (`castle_brick_07`, `rough_plaster_brick`, `sandstone_blocks_08`) sobre los modelos, y una
  capa de grano/viñeta en compositing (nodo Grano de película o una textura de ruido
  multiplicada) para igualar el filtro de 18.4.

**18.7 Encuadre y composición**

- **Plano contrapicado (desde abajo) para los titanes**, para exagerar su escala y la
  vulnerabilidad humana: es la lectura estándar del cómic y se repite en el anime — así lo
  describe el análisis de
  [RedQStudios](https://www.redqstudios.com/p/attack-on-titan-shingeki-no-kyojin_3.html), que
  además señala que la serie **respeta la regla de los 180°** salvo en las persecuciones de
  acción del ODM (donde se rompe a propósito para dar sensación de vértigo), usa **paneos**
  en las peleas y **fotogramas congelados** para marcar un instante clave.
- Ya medido en `biblia.md` §18 (guía IA): «plano medio desde abajo, capa al viento, algo
  delante del personaje» — coincide con lo anterior. Añado por emoción, de lo visto en los
  *storyboards* ya citados en `biblia.md` (§10, §11): calma/explicar = plano medio frontal,
  luz plana (ficha del tribunal, E·1-E·3); tensión/pelea = contrapicado + paneo rápido +
  destello de lente (ver 18.2, Araki); duelo/discurso = primer plano de ojos, luz lateral dura
  (antorchas, `#D29258`); revelación = composición **simétrica**, personaje centrado y
  pequeño contra un fondo enorme (el tribunal, E·3: juez arriba, acusado abajo, ya en `biblia.md`).

---

### Punto 24 · Obras parecidas

**24.1 Recomendaciones cuantificadas (AniList, ya en `datos-texto.md`, con votos)** ✅

De más votada a menos (usuarios que la recomiendan tras ver AoT):
*Vinland Saga* (2876 votos), *The Promised Neverland* (699), *86 Eighty-Six* (366),
*Kabaneri of the Iron Fortress* (365), *Seraph of the End* (210), *Kaiju No. 8* (170),
*Fullmetal Alchemist: Brotherhood* (116), *Parasyte -the maxim-* (101), *Chainsaw Man* (89),
*Claymore* (68), *Code Geass* (59), *Jujutsu Kaisen* (45). Fuente:
[AniList, página de Attack on Titan](https://anilist.co/anime/16498).

**24.2 Influencias que el propio Isayama reconoce (entrevista primaria)** ✅✅

Confirmado en 18.1: **Parasyte** (Hitoshi Iwaaki, coincide con la recomendación de AniList:
¡el propio autor cita a un manga que su público también asocia con AoT!), *Hell Teacher Nube*,
cine kaiju (Godzilla, Gamera), *Muv-Luv Alternative*, y en animación **Neon Genesis
Evangelion** (Hideaki Anno) — fuente:
[mangabrog, entrevista traducida](https://mangabrog.wordpress.com/2014/12/24/interview-with-hajime-isayama-creator-of-attack-on-titan-better-to-have-memorable-art-even-memorably-bad-art-and-stand-out/).
Segunda fuente que además liga a Mikasa con **Casca de Berserk** (Kentarō Miura) como
influencia declarada de Isayama para ese personaje:
[IMDb/ScreenRant](https://www.imdb.com/news/ni64720057/). El propio Isayama cita también,
entre sus influencias gráficas generales, a Hideki Arai, George Morikawa, Koji Seo, Ryōji
Minagawa y Makoto Yukimura (agregador de biografía,
[Lambiek Comiclopedia](https://www.lambiek.net/artists/i/isayama_hajime.htm); ⚠️ una sola
fuente agregadora para esa lista concreta, no es la entrevista directa).

**24.3 Qué otras láminas del servidor se le parecen (para no repetir ideas)**

Miré qué encargos de `biblias/` (fuera de mi carpeta, sólo para leer, no toqué nada) ya tienen
sus «Tres conceptos de lámina» hechos y coinciden en tono oscuro/militar con AoT:
- **`16-neon-genesis-evangelion`** (canal `#demos`): es la **influencia directa** que el
  propio Isayama reconoce (24.2). Sus 3 conceptos («La ficha del Instituto Marduk», «SOUND
  ONLY», «el chelo de Shinji») son para un canal distinto (#reglas ≠ #demos), así que no hay
  choque directo, pero comparten el recurso de «ficha/documento oficial dentro del mundo» —
  vigilar no repetir el mismo objeto si se hace una lámina 2 de Evangelion.
- **`11-chainsaw-man`** (canal `#que-estas-viendo`): también recomendado por AniList tras AoT
  (24.1). Sus conceptos usan un cine y un café, objetos muy distintos a la estela/tablón de
  AoT: sin choque.
- **`03-solo-leveling`**: mismo género (acción/supervivencia militar), conceptos sobre un
  mostrador de gremio y un tablón de misiones — el «tablón» se parece de lejos al Concepto A
  de AoT (tablón de roble con normas clavadas); si el dueño hace ambas láminas, conviene que
  el tablón de AoT sea claramente el de un **cuartel militar** (roble oscuro, clavos de
  hierro, ficha del anime) y no un tablón genérico de gremio de fantasía.
- No encontré (ni busqué más allá de esto, por presupuesto del repaso) una comparación
  explícita hecha por el propio servidor; es una lectura mía de las bibliai ya escritas.

---

### Punto 25 · El mundo, la historia por arcos y sus símbolos

**25.1 Las reglas del mundo, en cinco líneas** ✅ (Fandom, dos páginas)

1. La humanidad sobrevive encerrada tras **tres murallas concéntricas** (María, Rosa y Sina)
   porque fuera hay **Titanes** que devoran personas sin necesitarlas como alimento.
2. Los Titanes son en realidad personas transformadas —los **«Súbditos de Ymir»**— convertidas
   por el poder del **Titán Fundador** o del **Titán Bestia**, que pueden crear titanes
   gritando (ni falta que el grito sea fuerte) —
   [Fandom, «Founding Titan»](https://attackontitan.fandom.com/wiki/Founding_Titan).
3. Hay **nueve Titanes** con poderes únicos que pasan de portador a portador (al morir uno o
   comerlo otro); quien controla al **Fundador** (con sangre real Reiss/Fritz) puede ordenar a
   todos los demás Titanes a la vez.
4. Todo el que recibe el poder de un Titán muere en un plazo fijo si no lo transmite antes:
   la **«maldición de Ymir»** —
   [Fandom, «Power of the Titans»](https://attackontitan.fandom.com/wiki/Power_of_the_Titans)
   (la página «Curse of Ymir» redirige aquí, confirmado por su API).
5. Fuera de las murallas existe **Marley**, la nación que también usa Titanes como arma y que
   persigue a **Eldia** (el pueblo de origen de los Titanes) por lo que hicieron hace siglos.

**25.2 La historia por arcos, con sus momentos clave** ✅ (estructura oficial de Fandom)

La propia wiki organiza el manga en **9 arcos**, agrupados en dos «series»: *Muros* (arcos 1-7)
y *Marley* (arcos 8-9) — fuente:
[Fandom, «Story Arcs»](https://attackontitan.fandom.com/wiki/Story_Arcs) (wikitext leído por
su API `action=parse`, incluye el enlace al portal oficial como referencia para esa
división). Momentos clave añadidos de lo ya visto y medido en el resto de la biblia
(fotogramas y minutos de `biblia.md` §3, §10, §11):

| # | Arco | Manga / Anime | Momento clave |
|---|---|---|---|
| 1 | **Prólogo / Caída de Shiganshina** | vol. 1 · eps. 1-2 | El Titán Colosal rompe el Muro María; Eren ve morir a su madre. |
| 2 | **Sellado del Muro / Lucha por Trost** | vol. 1-4 · eps. 3-9 | El Titán Colosal vuelve a Trost; Eren descubre su poder de Titán defendiendo la muralla. |
| 3 | **104.º Cuerpo de Entrenamiento** | vol. 4 · eps. 10-11 | Entrenamiento militar; se forman las amistades y rivalidades del escuadrón 104. |
| 4 | **El Titán Femenina** | vol. 5-8 · eps. 12-25 | 57.ª expedición; Levi y su escuadrón mueren cazando al Titán Femenina; Annie Leonhart, expuesta y encerrada en cristal en Stohess. |
| 5 | **Choque de Titanes** | vol. 9-12 | Titanes irrumpen dentro del Muro Rosa; se revela que **Reiner es el Acorazado y Bertolt el Colosal**; Ymir se revela Titán y protege a Historia. |
| 6 | **Gobierno Real** | vol. 13-17 | Golpe de Erwin contra el gobierno; Kenny el Destripador; Historia se convierte en reina. |
| 7 | **Regreso a Shiganshina** | vol. 18-22 | Se retoma Shiganshina; **el sótano de Eren**: descubren la verdad del mundo exterior y de Marley. |
| 8 | **Marley** | vol. 23-26 | Ataque a Liberio durante la ceremonia; Eren captura al Titán Bestia (Zeke) y revela el plan del Retumbar. |
| 9 | **Guerra por Paradis** (final) | vol. 27-34 | Eren desata **el Retumbar**; guerra final entre antiguos aliados; Mikasa acaba con Eren; epílogo de paz frágil. |

**25.3 Emblemas, objetos y vocabulario que un fan reconoce al instante**

- **Emblemas** (ya medidos y con hex en `biblia.md` §2.0, hoja F·19-22): **Alas de la
  Libertad** (azul `#162873` y blanco) = Legión/Cuerpo de Reconocimiento; **unicornio** =
  Policía Militar; **rosas** = Guarnición; **espadas cruzadas** = cadetes del 104.º. El
  doblaje latino dice **«Legión de Exploración»** (biblia.md §9.3, ⚠️ sin texto oficial que lo
  escriba, sólo cuatro voces en las muestras de Doblaje Wiki).
- **Objetos icónicos**: el **equipo de maniobras tridimensional (ODM/3DMG)**, las **espadas**
  que se gastan y cambian, la **llave del sótano** que Eren guarda al cuello (el objeto que
  desata el arco 7), la **bufanda granate** de Mikasa (se la anuda Eren en el cap. 1: símbolo
  de «hogar»), la **taza que Levi coge por el borde** (ya en `biblia.md` §14, gesto de
  limpieza/control).
- **Vocabulario propio**: *Titán* (个別: Colosal, Acorazado, Femenina, Bestia, Mandíbulas,
  Carro, Martillo de Guerra, Fundador, Ataque — los nueve, 25.1), *Eldia* / *Marley*,
  *el Retumbar*, *Ackerman* (apellido con fuerza de guerrero despierta), *Súbditos de Ymir*,
  *la maldición de Ymir* (25.1), *Muro María / Rosa / Sina*, *«ese día»* (frase recurrente
  para el trauma del prólogo), y el saludo militar (puño derecho al pecho, ya en `biblia.md`
  §7.3 y §14).
- No repito aquí los emblemas con hex y enlace: ya están completos en `biblia.md` (F·19-22);
  el redactor puede enlazar esta tabla de arcos justo antes o después de esa sección.

---

## Lo mejor para la lámina

1. **Punto 18 → Blender**: el «Levi Ackerman rig» de ianadrielbravo (CC BY, con esqueleto,
   [enlace](https://sketchfab.com/3d-models/01ffa989559941ef807cc07b3fed40b8)) es la base 3D
   más directa para posar a Levi sin dibujar desde cero.
2. **Punto 18 → contorno**: usar el modificador **Line Art** de Blender (nativo, gratis) antes
   que Freestyle o Solidify: es el más parecido al contorno limpio y de grosor constante del
   manga/anime.
3. **Punto 5 → pensamiento**: **Zen Maru Gothic** para cualquier texto de monólogo interior
   sin bocadillo (la fuente real, Jun 34, es de pago y su prima libre Kosugi Maru falla en
   tildes).
4. **Punto 24**: el propio Isayama reconoce *Evangelion* como influencia — y ya hay una biblia
   de Evangelion en el servidor (`16-neon-genesis-evangelion`): se puede citar ese vínculo
   real en un texto de lámina 2 sobre «series parecidas».
5. **Punto 25**: la tabla de 9 arcos con su momento clave sirve para una lámina cronológica o
   para el foro `#🗺️・guia` (que ya tiene el hilo «Lo que hay que leer», según §1 de `biblia.md`).

---

## No encontré

- **Qué programa digital usa Isayama hoy** (más allá de la confirmación de 2014 de que dibuja
  a mano/analógico): busqué en japonés y en la web de ClipStudio, que lo tiene como imagen de
  un libro de consejos, pero no dice que sea su programa. **Sin fuente que lo diga**, así que
  no lo afirmo.
- **Grano de película o aberración cromática, con nombre de la técnica o del responsable**: es
  visible en el anime (ya medido en hex en `biblia.md`), pero no até una entrevista concreta
  sobre esos filtros de posproducción; lo dejo como técnica genérica de anime de 2013, ⚠️.
- **Fuente exacta de la rotulación del manga en inglés** (Steve Wands): sigue sin resolver
  desde la pasada anterior (`biblia.md` §20); tampoco la encontré yo.
- **Un segundo `.blend` o rig ya armado y verificado dentro de Blender** (los de Sketchfab se
  bajan en glTF/FBX/OBJ; no comprobé la importación real en Blender por no tener el programa
  en este contenedor: lo dejo dicho para que el redactor o el dueño lo verifiquen al bajarlo).
- **Una fuente que compare explícitamente AoT con otras láminas ya hechas en el servidor**:
  no existe (es lógico, el servidor no publica eso); 24.3 es mi propia lectura cruzada de las
  bibliai ya escritas, y lo digo así.

---

## Bitácora de búsqueda

**Buscador web** (11 búsquedas de las ~50 del cupo del rol; todo lo demás fue red directa:
Fandom API, Sketchfab API, GitHub raw, Fontsource API, jsdelivr):

1. EN · `Hajime Isayama backgrounds traced photos interview drawing style` → sin resultado
   directo sobre calco de fotos; sí sobre línea irregular a propósito.
2. EN · `Wit Studio Attack on Titan animation production 3DCG ODM gear technique interview` →
   SlashFilm, UK Anime Network, CBR, Sakuga Blog.
3. EN · `MAPPA Attack on Titan Final Season art style change animation technique` → Gamerant,
   AnimeIgnite, CBR, Twinfinite.
4. JA · `諫山創 作画 背景 写真 トレース インタビュー` → sin resultado técnico concreto;
   sí la entrevista de ClipStudio (18.1).
5. EN · `Hajime Isayama influences Blame Tsutomu Nihei Berserk interview inspiration` → IMDb
   (Casca/Mikasa), Lambiek.
6. EN · `Attack on Titan story arcs list Fandom manga arcs` → confirmó la página de Fandom,
   leída después por su API.
7. EN · `Blender toon shader Line Art modifier anime style outline tutorial free` →
   StraySpark, BlenderNation, manual de Blender.
8. EN · `Hajime Isayama Clip Studio Paint software manga tools digital` → sin confirmación.
9. EN · `Attack on Titan manga onomatopoeia sound effects lettering katakana style` → ANN,
   estudio académico JLA/UGM.
10. JA · `進撃の巨人 漫画 モノローグ 心の声 ふきだし なし` → llevó a la pregunta de Yahoo
    Chiebukuro con la fuente Jun 34.
11. EN · `Attack on Titan cinematography low angle framing composition analysis titans scale`
    → RedQStudios (regla de los 180°, paneos, contrapicados).
12. EN · `Attack on Titan anime color grading grain film effect photography director Kazuhiro
    Yamada` → llevó a la entrevista de Araki en fullfrontal.moe (sin dato de grano, pero sí de
    luz/sombra y 3DCG).

**Red directa** (sin gastar cupo de buscador):
- `attackontitan.fandom.com/api.php` (`action=parse`, `prop=wikitext`): páginas «Story Arcs»
  y «Founding Titan»; `action=query&list=search` para «Curse of Ymir».
- `api.sketchfab.com/v3/search` y `/v3/models/<uid>`: rigs de ianadrielbravo (licencia,
  descargable, miniatura 1920×1080) y ficha completa del «Levi Ackerman VR/Game Ready».
- `raw.githubusercontent.com/google/fonts`: METADATA y `.ttf` de Comic Neue, Bangers, Zen
  Maru Gothic, Jost (+ Jost Italic), Bungee; comprobados letra a letra con fontTools
  (`TTFont(f).getBestCmap()`) para á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü Ü.
- `api.fontsource.org/v1/fonts` y `cdn.jsdelivr.net/fontsource`: Kosugi Maru (subsets `latin`
  y `latin-ext`), descartada por faltarle tildes/ñ/¿/¡.
- Lectura de `biblias/*/biblia.md` de otros encargos (sólo lectura, sin tocar nada) para 24.3.

**Fuentes nuevas de esta parte** (para sumar a las ~67 ya contadas en `biblia.md`): mangabrog,
FIHEROE, Where Creativity Works, clipstudio.net, fullfrontal.moe, Sakuga Blog, RedQStudios,
Gamerant, AnimeIgnite, CBR (2 artículos), Twinfinite, SlashFilm, UK Anime Network, ANN
(onomatopeyas), journal.ugm.ac.id (JLA), Yahoo!知恵袋, Lambiek Comiclopedia, IMDb/ScreenRant,
StraySpark Studio, docs.blender.org, ClassCentral, api.sketchfab.com, api.fontsource.org,
cdn.jsdelivr.net — **23 fuentes nuevas**, todas enlazadas arriba.

**Repasado contra `ENCARGO.md`** (puntos 5-nuevo, 18, 24 y 25): todo lo obligatorio de cada uno
está cubierto y enlazado arriba. Lo que falta son extras ya anotados con ⚠️ en «No encontré»
(programa digital de Isayama, grano/aberración cromática con fuente nombrada, fuente del manga
en inglés, verificación del rig ya importado en Blender). Tanda cerrada: no hace falta relanzar
este rol para estos puntos.
