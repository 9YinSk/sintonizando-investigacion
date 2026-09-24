# Parte · texto — One Piece (puntos 5, 6, 11, 18, 24 y 25)

> Investigador de texto, juegos y técnica (equipo de 4, repaso). Parto de
> `partes/datos-texto.md` (no repito esas consultas), de `biblia.md` §7, §8 y
> §13 (puntos 5, 6 y 11: ya tuvieron una segunda pasada muy completa) y de dos
> archivos que dejó un piloto anterior (equipo de 8) sin terminar de escribir
> pero con trabajo de campo ya hecho: `partes/dialogos.md` (puntos 5, 6 y 11;
> su punto 11 está muy avanzado, lo resumo y añado, no lo repito) y
> `partes/tecnica-mundo.md` (puntos 18, 24 y 25: los títulos estaban puestos
> pero vacíos). Ese piloto además dejó **trabajo pesado sin escribir** en
> `/tmp/claude-0/trabajo/01-tecnica-mundo/`: 360 imágenes de la One Piece Wiki
> ya bajadas y medidas por época (manga y anime) con un script propio. Lo
> aproveché entero para el punto 18 en vez de volver a bajarlo.
> Formato: `- dato · fuente(s) · ✅ (dos fuentes o medido) / ⚠️ (una) · minuto o tamaño si aplica`

## Hallazgos

### Punto 5 · Tipografía (ya resuelto en `biblia.md` §7 — confirmo y cierro)

`biblia.md` §7 ya tiene el logo, las cartelas y ocho letras libres comprobadas
con `fontTools` (á é í ó ú ñ ¿ ¡). No hay nada flojo que rehacer; sólo quedaba
un ⚠️ abierto:

- **Letra de Panini México (manga en español) y de Planeta (España):** volví a
  buscar («Panini México One Piece tipografía letra globos») y no hay ficha
  pública de ninguna editorial que diga qué letra usan para los globos ⚠️
  (dos intentos, como pide `AYUDANTE.md`; sigue sin encontrarse). Recomiendo
  **Comic Neue Bold** (ya propuesta en §7): es la que más se parece a ojo a las
  ediciones en español de Shueisha/VIZ que sí tienen letra pública.

**No toco nada más de §7**: está completo y con las fuentes bien puestas.

### Punto 6 · Cómo hablan y piensan en pantalla (ya resuelto en `biblia.md` §8 — una pieza nueva)

`biblia.md` §8 ya cubre el globo ancho de Oda, el ドン!!, el cartel de SE BUSCA,
los *eyecatchers*, la carta del opening y la caja de *Odyssey*. Añado un dato
nuevo que salió de una entrevista de prensa japonesa (no estaba en la biblia):

- **El «ドン!!» cambia de sonido en Wano: se convierte en «べべん!!».** El
  director de serie desde el arco de Wano, **Nagamine Tatsuya** (長峯達也), lo
  cuenta así: «leyendo el original vi que el efecto de sonido había cambiado de
  "ドン!" a "べべん!", así que le pregunté a Oda qué sonido era exactamente»
  ✅ ([entrevista en 超！アニメディア](https://cho-animedia.jp/article/2019/06/30/12998.html),
  copia guardada en `/tmp/claude-0/trabajo/01-tecnica-mundo/animedia.html`,
  japonés, 30-jun-2019). Es la única onomatopeya de la serie que se sabe que
  **la cambió el propio Oda a propósito** para un arco concreto (el sonido de
  un tambor/gong de kabuki, no elタイコ de siempre). Para la lámina: si se
  hace algo ambientado en Wano, «べべん!!» es más fiel que «ドン!!».
- Confirma además que la caja de texto **no es fija en toda la serie**: cada
  arco puede tener su propio efecto de golpe, filtro de imagen y hasta plantilla
  de color de fondo (ver punto 18, mismo staff).

### Punto 11 · Videojuegos: interfaz, menús y cajas (gran parte ya en `partes/dialogos.md`)

`partes/dialogos.md` (piloto anterior) ya hizo el trabajo grande de este punto:
**59 capturas de Steam** (7 juegos) + **29 de la App Store** (México y Japón) +
el tráiler de *Grand Gourmet* en Dailymotion, todo **mirado** y con colores
medidos con `estilo.py`. No lo repito; lo resumo para que quede todo en un
sitio y añado lo que faltaba (TCRF, bloqueado para ellos con 403).

**Resumen de lo que ya está mirado y confirmado** (detalle completo en
`dialogos.md`, sección «Punto 11»):
- Qué juegos hay en español de Hispanoamérica de verdad: *Bounty Rush*,
  *Odyssey*, *World Seeker* y el próximo *Grand Gourmet* (23-oct-2026,
  Kairosoft); *Pirate Warriors 3/4* y *Burning Blood* sólo en español de España;
  *Treasure Cruise* no tiene español.
- La caja de *Odyssey* (banda translúcida verde azulada `#466164` + pestaña
  turquesa `#38909C`) y que **es translúcida de verdad** (cambia de color según
  el fondo: `#2E4646` en otra captura).
- *Grand Gourmet* tiene **la caja «de barco» más clara de la franquicia**: crema
  con filete dorado y café, un ancla de «siguiente» en vez de flecha.
- ***Treasure Cruise* cuenta sus escenas famosas con viñetas de manga y un
  globo de manga de verdad** (blanco, borde negro grueso, texto japonés
  vertical): es la prueba de que un juego oficial también usa el globo del
  manga, no sólo una caja traducida.
- *Bounty Rush* tiene un «DOOM!!» rojo con borde blanco (la versión en inglés
  del ドン!!) y fichas de personaje con Birthday/Height/Bounty/VA.
- *Burning Blood* escribe los golpes en **katakana gigante dentro del
  escenario 3D** (ズドォン!!!, バチッ), como en el manga.
- La app oficial **ONE PIECE BASE** convierte tu foto en un cartel de SE BUSCA
  con tu propio nombre y lo pone de foto de perfil; el reverso es una ficha con
  Nickname/Bounty/Devil Fruits/Haki/Affiliations — un modelo perfecto para el
  paso «preséntate» del canal.

**Lo nuevo que añado (The Cutting Room Floor, contenido descartado):** la web
sigue en 403 (Cloudflare) desde este contenedor —lo comprobé de nuevo,
`curl` y con cabecera de navegador, mismo resultado; dos intentos, no
insisto más— pero el buscador sí indexa el texto de sus páginas:
- **One Piece Ambition** (móvil/Vita): quedó un **modelo sin usar de
  Axe-Hand Morgan** con mucho más detalle que el de la versión final, y unas
  imágenes de relleno del mecanismo «Will Crystal» ⚠️ (una fuente, TCRF vía
  resultado de búsqueda, no pude abrir la página para comprobar capítulo o capturas).
- **One Piece: Grand Battle!** (PlayStation, 1999): una versión sin terminar
  del mapa «Syrup Village», con diferencias gráficas y de obstáculos frente al
  final ⚠️ (una fuente, igual).
- **One Piece: Grand Battle** (PlayStation 2): la versión occidental de 4Kids
  y Bandai **recortó mucho contenido a propósito**, para no revelar spoilers a
  la audiencia occidental del anime (que iba muy por detrás del japonés) ⚠️
  (una fuente).
  ([resultados de búsqueda sobre tcrf.net](https://tcrf.net/Category:One_Piece_series), en_)

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo (nuevo, todo mío)

#### 18.1 · Las herramientas físicas de Oda (manga en papel)

Un blog que documentó la reproducción de la mesa de trabajo de Oda en la
exposición **ONE PIECE展 2012-2013** (Osaka, Tempozan) enumera cada objeto real
expuesto ⚠️ (una fuente, pero describe objetos físicamente expuestos por la
propia exposición oficial, no una opinión):
([canrevb.com](https://canrevb.com/archives/254), japonés, 19-ene-2013;
copia en `/tmp/claude-0/trabajo/01-tecnica-mundo/t.html`).

- **Plumilla G (Gペン)** en un mango de madera **BRAUSE 1614** (gastado de uso).
- Lápiz **Mitsubishi B**, tinta **Pilot**, corrector **Mannon (ミスノン)**.
- Rotulador técnico de tinta al agua **Pigma Graphic** (para las rayas rectas
  de fondo/viñeta).
- **Copic** (marcadores de alcohol): 3 cajas de 72 colores + 1 de 36, para las
  ilustraciones a color (los *color spreads* del punto 18.2).
- Goma de **migas de pan** (練り消しゴム), para no ensuciar el papel.
- 3 pinceles de grosor distinto (龍, リセーブル面相短峰, KOLINSKY SABLE PICABIA)
  y un rotulador-pincel **Pentel FP6L** para negros sólidos (pelo, sombras).
- Cuadernos **Kokuyo Campus**: los de ideas llevan escrito a mano «Wano»,
  «Isla Gyojin», «técnica», «personaje» — la libreta de ideas real de Oda.

**Para replicarlo en Photoshop:** un pincel de entintado con presión variable
(grosor 2-6 px a 300 dpi, como el Gペン) + un pincel plano de bordes duros para
rellenos negros (como el Pentel) + una paleta de marcador plano (no
degradado) de ~30 tonos para las ilustraciones a color, en vez de pintura
digital con muchos matices.

#### 18.2 · Tres «capas» de estilo, medidas con un script propio (n=356 imágenes)

El piloto anterior bajó y midió con su propio script (basado en el método de
`estilo.py`: saturación, brillo, % de zona plana, % de degradado, densidad de
línea, color de la línea, grano de textura y viñeteado) **9 grupos de imágenes
al azar de la One Piece Wiki** (categorías `Chapter_Images`,
`Color_Spread_Images`, `Colored_Chapter_Images` y `Season_N_Episode_Images`,
40 por grupo salvo el de Oda, 16): manga en blanco y negro, los *color spreads*
que pinta el propio Oda, el manga coloreado digitalmente por el estudio, y
seis épocas del anime (1999 East Blue → 2001 Alabasta/Skypiea → 2010s HD →
Wano → Egghead → Elbaph, el arco que se está emitiendo ahora). Datos y
contactos en `/tmp/claude-0/trabajo/01-tecnica-mundo/` (`resumen_estilo.json`,
`extra.json`, `grosor.json`, hojas `hoja_1…9_*.jpg`); **los miré** (hojas 1 y 9
comparadas abajo). ✅ (medido, n=356 en total).

| Grupo | n | Línea (% de píxeles) | Color de la línea | Sombreado | Saturación | Paleta cerrada (top-12 colores) | Viñeta (esquina/centro) |
|---|---|---|---|---|---|---|---|
| Manga B/N (`Chapter_Images`) | 40 | **16,2 %** (la más densa: tramas y rayado) | `#585858` | mixto (37/40) | 0 (sin color) | 96 % | 0,99 (plana) |
| *Color spread* de Oda (acuarela/Copic) | 16 | 15,3 % | `#614F40` | mixto/degradado | 30,5 | **32 %** (la paleta más ancha: pintura real) | 1,54 (más clara en las esquinas) |
| Manga coloreado digital (estudio) | 40 | 10,5 % | `#5D4C41` | mixto, algo cel | 31,0 | 45 % | 1,22 |
| Anime 1999 (East Blue) | 40 | 8,4 % | `#867B73` | degradado 36/40 | 29,0 | **74 %** (paleta muy cerrada: cel-shading clásico) | 0,80 |
| Anime 2001 (Alabasta/Skypiea) | 40 | 7,7 % | `#7C6E67` | degradado 32/40 | 29,0 | 45 % | 1,01 |
| Anime 2010s HD | 40 | 8,3 % | `#776E64` | degradado 32/40 | 29,0 | 55 % | 0,69 |
| Anime Wano | 40 | 6,8 % | `#635951` | degradado 39/40 | **49,5** (la más saturada) | 71 % | 0,66 |
| Anime Egghead | 40 | 9,9 % | `#695854` | degradado 36/40 | 41,0 | 44 % | 0,88 |
| Anime Elbaph (actual) | 40 | 7,3 % | `#5B4C5B` | degradado 34/40 | 36,0 | **31 %** (la paleta más ancha de todo el anime) | **0,42** (la más viñeteada: bordes muy oscuros) |

**Qué dice esta tabla, en cristiano:**
- El manga impreso usa **mucha más línea** que cualquier anime (16 % contra
  6-10 %): Oda rellena con tramas y rayado en vez de degradados. El anime
  compensa con **degradado pintado** (32-39 de 40 imágenes en todas las épocas).
- El color se ha ido **saturando con los arcos nuevos** hasta Wano (49,5,
  el pico) y ha bajado un poco desde (Egghead 41, Elbaph 36), pero sigue muy
  por encima de 1999-2010 (29 en los tres).
- La **paleta se ha ido abriendo**: 1999 usaba sólo 12 colores para cubrir el
  74 % de cada imagen (cel clásico, pocos tonos); Elbaph necesita 3 veces más
  colores para cubrir sólo el 31 % (más gradientes, más luces de color).
- El **viñeteado (esquinas más oscuras que el centro) ha ido subiendo** de
  época en época: casi nulo en 1999 (0,80) hasta muy marcado en Elbaph (0,42,
  cuanto más bajo el número más oscuras las esquinas). Es un filtro de cámara
  digital (ver 18.3), no del dibujo.
- El grano (textura de alta frecuencia fuera de los bordes, en `extra.json`)
  es **mucho mayor en el manga escaneado** (5,6-8,8) que en el anime digital
  (0,9-2,1 en todas las épocas): el papel real tiene grano; el máster digital
  del anime, casi nada — así que «grano de papel» sólo hace falta simularlo
  para las páginas de manga, no para las escenas de anime.

**Mirado (no sólo medido):** comparé la hoja 1 (manga B/N, 20 páginas al azar)
con la hoja 9 (Elbaph, 20 fotogramas al azar). El manga tiene **tramas de
puntos, rayado de velocidad y grandes manchas negras de contraste** (estilo
*gekiga*, dramático); Elbaph es **pintura digital de fondos muy saturada**
(arcoíris, fuego, bosque mágico) con líneas de personaje finas y limpias sobre
fondos casi ilustrados. Es el salto de «cómic de acción» a «anime de
aventura pictórico» del que habla la prensa (18.3).

#### 18.3 · Qué dicen el estudio y la prensa japonesa del cambio de estilo

- **El grosor de línea bajó de Wano a Egghead a propósito**, según un análisis
  de prensa: «el dibujo, que en el arco de Wano tenía una pincelada ruda y
  *gekiga*, cambió: el trazo se hizo más fino en general y el ambiente se
  volvió más gráfico», para separar visualmente el Japón feudal de Wano de la
  tecnología de Egghead ✅ ([Real Sound](https://realsound.jp/movie/2024/09/post-1780386.html),
  japonés, 15-sep-2024; copia en `realsound.html`). El *storyboard* y la
  dirección del opening de Egghead fueron de **Ishitani Megumi** (石谷恵) y la
  dirección de animación de **Mori Keisuke** (森佳祐), buscando ese aire «pop y
  artístico». El episodio 1072 («Gear 5» de Luffy) tuvo la participación del
  animador legendario **Ohira Shingo** (大平晋也); el episodio 1112 (Shanks vs.
  Kid) contó con **Ota Akihiro** (太田晃博, el mismo animador de la pelea de
  *Kitarō Tanjō*) y dirección de animación de **Tu Yongce** y **He Ziwei**.
- **El estudio de «撮影» (fotografía/composición digital) cambió al empezar
  Wano**, y con él **los filtros y efectos de pantalla**: el director de serie
  **Nagamine Tatsuya** dice en la misma entrevista de Animedia: «las batallas
  van a ser más como las de *Dragon Ball*, más vistosas — vamos a hacer que la
  pantalla brille más, y cuando el color general vaya a quedar apagado, vamos
  a mostrar el Haoshoku Haki, el Kenbunshoku Haki o los efectos de las Frutas
  del Diablo con una luz de color muy vistosa» y «como el equipo de fotografía
  cambia desde Wano, el ambiente de los filtros y efectos también va a
  cambiar» ✅ (misma fuente, `animedia.html`). Esto es justo el «撮影» del que
  habla el punto 18 del encargo: la etapa de post-producción en 2D (equivalente
  a componer capas de ajuste en After Effects/Photoshop) que en el anime
  japonés se hace en un estudio aparte del de animación.
- Para las Frutas del Diablo, el Haki y los golpes especiales: **luces de
  color plano superpuestas en modo Trama/Luz** (no relleno) sobre el dibujo,
  con un resplandor difuminado alrededor (glow), es la técnica que describen.

#### 18.4 · Cómo replicarlo, paso a paso

**En Photoshop (una viñeta o pose ya recortada):**
1. Capa de **línea**: entintado a pincel con grosor variable (2-4 px a 1000 px
   de ancho de personaje, según la línea medida arriba), color no puro negro
   sino un gris-marrón oscuro (`#5D4C41` a `#776E64` según la época que se
   quiera imitar) — nunca `#000000` puro.
2. Capa de **color base plano** (Multiplicar o normal debajo de la línea),
   paleta de **10-15 tonos por personaje** (paleta cerrada, como midió el
   script: 44-74 % del área en pocos colores).
3. Capa de **sombra**: una sola forma con los bordes duros (ajustar a "sombra
   de anime clásica") si se imita 1999-2010, o con el borde **difuminado 8-15
   px** (Gaussiano) si se imita Wano/Egghead/Elbaph — la tabla de arriba
   muestra que el degradado gana en casi todas las épocas modernas.
4. Capa de **luz/Haki/Fruta del Diablo** (si aplica): modo *Trama* o *Luz
   suave*, color saturado (rojo `#D00303`-como del punto 6, dorado, morado),
   con **Desenfoque gaussiano 10-20 px** para el resplandor, encima de todo.
5. Capa de **viñeta**: una forma ovalada negra al 10-20 % de opacidad en las
   esquinas (más fuerte cuanto más reciente sea el arco que se imite: casi
   nada para 1999, bastante marcada para Elbaph).
6. Si se quiere imitar el papel del manga: capa de **grano** (Filtro > Ruido >
   Añadir ruido, monocromático, 3-5 %) sólo si el marco es «página de manga»;
   no hace falta para un marco de anime (el grano medido ahí es casi nulo).

**En Blender (si el objeto de la lámina lleva un elemento 3D, p. ej. un barril
o un cofre con la escena pintada encima):** usar un *material* con un
**Toon Shader / Shader to RGB** para que las sombras salgan en dos tonos
planos (no degradado PBR), un **Freestyle** o *Solidify* invertido para el
contorno de tinta (grosor ~2-3 % del tamaño del objeto en pantalla, como la
línea medida), y añadir el resplandor de Haki/Fruta como un **Emission**
sobrepuesto con *Glare* en composición, igual que el punto 3 (glow) de arriba.

### Punto 24 · Obras parecidas y temas relacionados (nuevo, todo mío)

#### 24.1 · Lo que el propio Oda reconoce como influencia

- **Akira Toriyama y *Dragon Ball* son, con diferencia, su influencia más
  grande.** Palabras suyas: «la influencia de *Dragon Ball* es sin duda la
  más grande. Copié una y otra vez el dibujo de Toriyama, y esa costumbre se
  me quedó para siempre» ✅ ([ComicBook](https://comicbook.com/anime/news/one-piece-creator-talks-his-history-with-dragon-ball-the-influence-of-toriyama-is-by-far-the-greatest/) +
  cita original japonesa recogida en varios blogs de fans que remiten a una
  entrevista/diálogo con Toriyama). En una charla publicada en el primer
  *Color Walk* (2001), Oda le confesó a Toriyama que lo que más le impactó de
  *Dragon Ball* de niño fueron, curiosamente, **las manos y las axilas** de
  los personajes ✅ ([ScreenRant](https://screenrant.com/one-piece-oda-compliment-toriyama-dragon-ball-art/)).
  Oda y Toriyama hicieron juntos el especial ***Cross Epoch*** (2006, para el
  38 aniversario de *Shonen Jump*), un cruce con personajes de las dos series
  ✅ (ambas fuentes).
- **Kinnikuman** (de Yudetamago) es, junto a *Dragon Ball*, el otro manga que
  Oda dice que más le gusta ✅ (cita en japonés recogida en varios blogs que
  citan la misma entrevista; ⚠️ no encontré la entrevista original, sólo
  citas de segunda mano coincidentes en varias webs).
- ***Vicke el vikingo*** (*Chiisana Viking Bicke*, la serie de animación
  japonesa de 1974 basada en los libros suecos de Runer Jonsson) es, según
  Oda, **el origen de que le gusten los piratas**: «me gustan desde siempre,
  empezando por Bicke. Creo que a todo el mundo le gustan los piratas» ✅
  ([SlashFilm](https://www.slashfilm.com/881423/the-forgotten-anime-classic-that-inspired-one-piece/) +
  cita japonesa recogida en blogs); la serie le hizo darse cuenta de que **«los
  vikingos también son un tipo de pirata»**.

#### 24.2 · Obras de tono o estructura parecida (según la comunidad)

De la lista de «recomendaciones si te gustó» de AniList (votos de usuarios,
ya en `datos-texto.md`, no la repito entera): las más votadas son *Hunter x
Hunter* (2011, 2188 votos), *Naruto* (1015), *Naruto Shippuden* (674),
*Black Clover* (454) y *Dragon Ball*/*Dragon Ball Z* (394+249) ⚠️ (una
fuente, votos de comunidad, no un dato oficial). Comparten con One Piece la
estructura de *shonen* de aventura por arcos, el «equipo de amigos poco a
poco más fuerte» y (salvo *Naruto*) el humor exagerado mezclado con drama
real. **Diferencia clave para la lámina:** One Piece es el único de esos
títulos ambientado **en el mar**, así que el objeto/escenario (barco, cartel
de pirata, carta náutica) no se solapa con ninguno de ellos.

#### 24.3 · Qué otras láminas del servidor se parecen (para no repetir ideas)

Repasé los conceptos de lámina de las biblias ya hechas más parecidas en tono
(*shonen* de acción/aventura: Naruto 30, Hunter x Hunter 36, Jujutsu Kaisen 32,
My Hero Academia 25, Demon Slayer 31, JoJo 28) y dos más con objeto 3D fuerte
(Pokémon 07, Solo Leveling 03) — no las 36 biblias completas, por tiempo; el
resto son de géneros muy distintos (sitcom, terror psicológico, cocina…) donde
el choque de objeto es poco probable. Lo más
parecido a los tres conceptos de One Piece (muro de carteles de SE BUSCA,
carta náutica de Nami, barril) es:

- **Solo Leveling (03)** usa en su concepto B un **«tablón con papeles y
  chinchetas»** (un panel de anuncios del gremio de cazadores) — es la idea
  más cercana a un «muro con papeles clavados» que hay en el servidor ✅ (leído
  en `biblias/03-solo-leveling/biblia.md`). **Para que el de One Piece no se
  confunda con ése:** que el muro sea claramente **madera de barco vieja y
  clavos de hierro**, papel envejecido y roto en los bordes (como las hojas
  O3-O9 de la biblia), nunca un tablón de corcho ni una pizarra de gremio.
- **My Hero Academia (25)** usa un **cuaderno** que el fandom copia página a
  página como objeto reconocible ✅ (leído en su biblia, §concepto). No es el
  mismo objeto que la carta náutica de Nami, pero comparte la idea de «un
  objeto de papel que el fan ya conoce de memoria»: en la biblia de One Piece
  esa función la cumple **el propio cartel de SE BUSCA**, que es aún más
  reconocible fuera del fandom que un cuaderno.
- **JoJo's Bizarre Adventure (28)** y **Naruto (30)** no comparten objeto
  (usan una flecha de «To Be Continued» y un rollo/aula, respectivamente):
  sin solape.
- **Pokémon (07)** usa una Pokébola 3D como objeto principal: sin solape de
  objeto ni de escenario.

**Conclusión para el redactor:** los tres conceptos de One Piece (cartel de
SE BUSCA, carta náutica, barril) siguen siendo **distintos** de todo lo ya
hecho en el servidor; el único cuidado real es que el muro de carteles no se
vea como el tablón de Solo Leveling (ver arriba).

### Punto 25 · El mundo y sus símbolos (nuevo, todo mío)

#### 25.1 · Las reglas del mundo, en cinco líneas

Todo verificado en el wikitexto de la One Piece Wiki, que a su vez cita el
capítulo/episodio exacto donde se establece cada regla (`action=parse`,
`prop=wikitext`, sección 0 de cada página) ✅:

1. El mundo es un planeta con un océano gigante partido por una línea de
   tierra continua, la **Red Line**, y cruzado de polo a polo por la
   **Grand Line**, una ruta «cementerio de piratas» con fenómenos que no
   existen en ningún otro mar ([One Piece Wiki: Grand Line](https://onepiece.fandom.com/wiki/Grand_Line)).
2. Un cinturón de mar sin viento ni corrientes, el **Calm Belt**, separa la
   Grand Line de los cuatro mares «normales» (East/West/North/South Blue) y
   está lleno de Reyes Marinos gigantes ([Calm Belt](https://onepiece.fandom.com/wiki/Calm_Belt)).
3. Gobierna casi todo el mundo el **Gobierno Mundial**, una federación de más
   de 170 países con sede en **Mary Geoise**, dirigida de hecho por **Imu**
   (el rey oculto) y de derecho por los **Cinco Ancianos**, con los
   **Nobles Mundiales** como clase privilegiada ([World Government](https://onepiece.fandom.com/wiki/World_Government)).
4. El equilibrio de poder lo sostienen los **Tres Grandes Poderes**: la
   Marina (brazo militar del Gobierno Mundial), los **Cuatro Emperadores**
   (piratas) y (hasta que se abolieron) los **Siete Corsarios**
   ([Three Great Powers](https://onepiece.fandom.com/wiki/Three_Great_Powers)).
5. Comer una **Fruta del Diablo** da un poder único a cambio de no volver a
   nadar nunca; sólo puede haber una persona con cada poder a la vez, y el
   poder «renace» en otra fruta cuando su dueño muere
   ([Devil Fruit](https://onepiece.fandom.com/wiki/Devil_Fruit)).

#### 25.2 · Emblemas y objetos icónicos (con imagen)

- **El Jolly Roger (bandera pirata) es distinto para cada tripulación**: hay
  «cientos, si no miles» de variantes documentadas en la wiki, cada una con su
  propia página ([Jolly Roger](https://onepiece.fandom.com/wiki/Jolly_Roger)) ✅.
  El de los **Sombrero de Paja** es una calavera sonriente con el sombrero de
  Luffy y dos tibias cruzadas, dibujada por Luffy en el ep./cap. donde nace el
  grupo ([imagen oficial, 1432×1029](https://static.wikia.nocookie.net/onepiece/images/8/87/Straw_Hat_Pirates%27_Jolly_Roger.png)) ✅.
  Es la insignia que un fan reconoce **al instante**, más que ninguna otra de
  la serie.
- **El Log Pose y el Eternal Pose**: la brújula normal no sirve en la Grand
  Line (los minerales de cada isla confunden el imán); el Log Pose graba el
  magnetismo de la isla donde estás y apunta a la siguiente, un Eternal Pose
  siempre apunta a una isla fija ([Log Pose](https://onepiece.fandom.com/wiki/Log_Pose)) ✅.
  Es el objeto de «brújula de aventura» más reconocible de la serie —una
  esfera de cristal con una aguja, llevada en la muñeca (Nami la lleva así,
  ya en la biblia §9).
- **La Vivre Card**: un papel especial hecho en el New World que arde despacio
  y siempre señala hacia la persona a la que pertenece, incluso a distancia
  ([Vivre Card](https://onepiece.fandom.com/wiki/Vivre_Card)) ✅. Sirve de
  «carta de presentación mágica»: un posible objeto para el paso «preséntate»
  del canal.
- **El Berry (฿)**, moneda del mundo: el símbolo es una B mayúscula con dos
  rayas, como el signo del dólar pero con B ([Belly](https://onepiece.fandom.com/wiki/Belly)) ✅.
- **El Poneglyph**: bloques de piedra indestructibles con historia escrita en
  una escritura antigua, repartidos por el mundo, hechos por el clan Kozuki
  ([Poneglyph](https://onepiece.fandom.com/wiki/Poneglyph)) ✅. Vocabulario
  perfecto para una lámina de «lore»: son literalmente «piedras con reglas
  escritas», el mismo papel que cumpliría un cartel de reglas del servidor.
- **El Den Den Mushi**: un caracol telepático que hace de teléfono/cámara del
  mundo, con variantes según la señal que transmite ([Den Den Mushi](https://onepiece.fandom.com/wiki/Den_Den_Mushi)) ✅.
  Un Den Den Mushi puede ser el «icono de aviso» de un canal de anuncios.

#### 25.3 · Vocabulario propio que un fan reconoce al instante

`Grand Line` · `New World` (Nuevo Mundo) · `Paradise` (Paraíso, la primera
mitad de la Grand Line) · `Calm Belt` (Cinturón de Calma) · `Red Line`
(Línea Roja) · `nakama` (compañero de tripulación, con un matiz de familia
elegida que la propia serie usa mucho más que «amigo») · `Yonkou`/Four
Emperors (Cuatro Emperadores) · `Shichibukai`/Seven Warlords (Siete
Corsarios, ya abolidos en la trama) · `Marine` (Marina) · `Cipher Pol`
(espías del Gobierno Mundial) · `World Noble` (Noble Mundial) ·
`Devil Fruit` con sus tres familias **Paramecia**, **Zoan** y **Logia**
([Devil Fruit](https://onepiece.fandom.com/wiki/Devil_Fruit)) ✅ ·
`Haki` (覇気), con sus tres tipos: **Kenbunshoku** (observación),
**Busoshoku** (armadura) y **Haoshoku** (el de los reyes, rarísimo)
([Haki](https://onepiece.fandom.com/wiki/Haki)) ✅ · `Will of D.`
(«La Voluntad de la D.»): el misterio de los personajes con una «D.» en su
nombre, opuestos en el fondo a los Nobles Mundiales
([Will of D.](https://onepiece.fandom.com/wiki/Will_of_D.)) ✅ ·
`Pirate King` (Rey de los Piratas) · `One Piece` (el tesoro; también el
nombre de la serie) · `Laugh Tale` (la última isla).

