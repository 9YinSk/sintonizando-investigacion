# Parte del investigador de TEXTO, JUEGOS Y TÉCNICA · Assassination Classroom

Puntos de ENCARGO.md a mi cargo (EQUIPO.md): **5 (tipografía), 6 (cómo hablan y
piensan en pantalla), 11 (videojuegos), 18 (estilo de dibujo y cómo
replicarlo), 24 (obras parecidas) y 25 (el mundo, la historia y sus
símbolos)**.

`biblia.md` ya existe (hecha con la red cerrada, 24-sep-2026, antes del
método en equipo). Los puntos 5, 6 y 11 ya están escritos ahí (§6, §7, §13);
mi trabajo en esos tres es **confirmar, corregir con la red abierta y
profundizar**, no repetir. Los puntos **18, 24 y 25 no existen como sección
propia en `biblia.md`** (sólo frases sueltas): los escribo enteros aquí para
que el redactor los añada.

**Corrección para el equipo**: la wiki de Fandom correcta es
`https://ansatsukyoshitsu.fandom.com/` (la wiki `assassinationclassroom.fandom.com`
que sugiere `encargos/24-assassination-classroom.md` da 404: no existe con
ese subdominio). Aviso también para imagen/vídeo/voz.

---

## Punto 5 · Tipografía — confirmaciones nuevas

- **Logo inglés «ASSASSINATION CLASSROOM»: Futura** ✅ (dos fuentes además
  de la ya citada en `biblia.md`: foro de
  [dafont](https://www.dafont.com/forum/read/347871/assasination-classroom)
  y el listado
  [«Famous logos created with Futura»](https://fontmeme.com/famous-logos-created-with-futura-font/)
  de FontMeme, que la incluye explícitamente).
- **Logo japonés 暗殺教室** (el rotulado curvo de la portada de los tomos):
  sigue **sin encontrar** ❌ quién lo diseñó o qué tipografía base usa.
  Búsquedas hechas: `暗殺教室 ロゴ デザイン 書体`, `暗殺教室 タイトルロゴ フォント`
  (Yahoo!知恵袋 tiene la misma pregunta sin responder:
  [enlace](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14170560814)).
  Parece **rotulado a mano para la ocasión** (no hay coincidencia con una
  familia comercial conocida), como es normal en portadas de Shonen Jump.
- **Blu-ray/DVD y web oficial**: los títulos de episodio en pantalla («〜の
  時間») usan una **gótica de trazo grueso sin filetes** (Gothic/Godo tipo);
  no encontré el nombre exacto ❌, pero **Dela Gothic One** (ya propuesta en
  `biblia.md` para onomatopeyas) es la libre más parecida en peso y kanji.

*(El resto de §6 de `biblia.md` — la tabla de letras libres comprobadas con
fontTools — ya está bien hecha y no hace falta repetirla.)*

---

## Punto 6 · Cómo hablan y piensan en pantalla — ampliación con videojuegos

`biblia.md` §7.5 decía «No encontré capturas de sus cajas de diálogo ❌» de
los videojuegos. **Con la red abierta sí se encontraron y se miraron**
(hoja de contacto propia, ver abajo). Cambia a ✅.

### Cómo son los cuadros de diálogo en los dos juegos de 3DS

Miré 7 capturas oficiales de prensa (Famitsu y 4Gamer, ver Bitácora) montadas
en una hoja de contacto propia
(`/tmp/claude-0/trabajo/24-assassination-classroom-texto/hoja_juegos.jpg`,
no sube al repo por ser de prensa, sólo referencia) ✅:

| Elemento | Cómo es | Foto de la hoja |
|---|---|---|
| **Etiqueta del nombre** | Rectángulo **amarillo brillante** (medido con Pillow: **#FFEA62**), esquina superior izquierda de la caja, con el nombre en kanji/kana en negro | 1, 2 |
| **Caja de texto** | Fondo **casi blanco con un tinte crema** (medido: **#F5F7E2 / #FBFEED**, no blanco puro #FFFFFF), letra negra de trazo grueso sin filetes (gótica), 2 líneas | 1, 2 |
| **Retrato** | Busto del personaje en **estilo SD/chibi** (cabeza grande, 2 cabezas de alto) sobre el fondo del lugar (patio, autobús del viaje) | 1, 2 |
| **HUD de combate** («大包囲網», 2015) | Barra de vida **AP** arriba a la izquierda (número, no barra), icono del **arma equipada** arriba a la derecha dentro de una placa oscura, texto de diálogo corto en **globo verde lima** sobre el personaje, un **radar/mapa circular** abajo con las posiciones de los alumnos alrededor de Koro-sensei | 3, 6, 7 |
| **Combos** | Texto grande en diagonal, con contorno, tipo cómic: **«Critical Hit!»**, **«2 HIT COMBO!!»**, **«2 TRAP&CHAINS»** | 4, 7 |
| **Caja de estadísticas** («育成計画», 2016) | Gráfico de **radar (pentágono/heptágono) rojo** con 6-7 parámetros (気力, スタミナ, 腕力, スピード, 元気, 集中力, ワナLV), pestañas «能力 / その他» arriba | 1, 2 |

**Para la lámina**: si el canal quiere un guiño "de videojuego" (una
notificación tipo HUD), la combinación **etiqueta amarilla + caja crema +
letra gótica gruesa negra** es la que usa la propia franquicia, más fiel que
inventar una burbuja. El radar de estadísticas (pentágono rojo) sirve de
adorno para una ficha de "nivel" del canal.

---

## Punto 11 · Videojuegos de la franquicia — ampliación

Confirmación con capturas reales (antes sólo texto, sin imagen):

| Juego | Interfaz vista | Fuente de la captura |
|---|---|---|
| **暗殺教室 殺せんせー大包囲網!!** (3DS, 2015) | Persecución en 3ª persona por las calles junto al colegio, con **conos de tráfico** de attrezo; cronómetro arriba a la izquierda (`01:10`, `01:20`); combos `HIT COMBO` y `TRAP&CHAINS`; caja del juego con Koro-sensei enorme y los alumnos alrededor, fondo **verde y amarillo** (los colores del uniforme/pizarra) | [4Gamer, cobertura del lanzamiento](https://www.4gamer.net/games/278/G027887/20150227043/) ✅ |
| **暗殺教室 アサシン育成計画!!** (3DS, 2016) | Diálogos de vida escolar (viaje a Kioto, "prueba de valor") con retrato SD; **reutiliza el motor de combate** del juego de 2015 (mismo HUD de AP y arma) para sus misiones de asesinato | [Famitsu, galería de capturas](https://www.famitsu.com/news/201603/18101425.html) ✅ |

Las dos fuentes fallaban con la red cerrada (§20 de `biblia.md`); con la red
abierta **sí responden** (200 OK), igual que Dengeki
([1128444](https://dengekionline.com/elem/000/000/982/982279/), sin
capturas nuevas de interés).

- **No encontré**: Koro-sensei en *J-Stars Victory VS* seguía sin
  comprobar; con la red abierta **tampoco lo confirmé** ❌ (no hay tiempo
  para más búsquedas de este dato menor; lo dejo igual que antes, con su
  aviso).
- **No hay versión occidental** de ninguno de los dos juegos de 3DS (sólo
  Japón): confirmado por la ausencia total de ficha en MobyGames para
  Europa/EE. UU. (comprobé el buscador de MobyGames, sin resultado) ⚠️.

---

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo (NUEVO)

### 18.1 Quién lo hizo

- **Estudio de animación**: **Lerche** (studio formado en 2011 desde Studio
  Hibari) ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Lerche_(studio)),
  [Anime News Network](https://www.animenewsnetwork.com/encyclopedia/company.php?id=10083)).
- **Director**: **Kishi Seiji** (岸誠二) ✅. **Guion/composición de serie**:
  **Uezu Makoto** (上江洲誠) ✅. Los dos dieron una entrevista conjunta en
  [Comic Natalie](https://natalie.mu/comic/pp/ansatsu) sobre la adaptación
  (la página bloqueó la lectura completa del texto al intentar extraerlo;
  cito sólo el titular y el tema, **una fuente, sin cita textual** ⚠️).
- **Diseño de personajes (anime)**: **Morita Kazuaki** (森田和明) ✅
  ([AniList](https://anilist.co/anime/20755/staff),
  [ansatsu-anime.com](https://www.ansatsu-anime.com/2014-2016/special/special0001.php)).
- **Dirección de arte**: **Miyakoshi Ayumu** (宮越昇), ya en `biblia.md`
  §5; una fuente añade un segundo nombre, **Shimoyama Kazuto**, sin poder
  confirmarlo en una segunda fuente ⚠️.
- **Autor del manga**: **Matsui Yuusei** (松井優征). Antes de esta serie
  creó *Neuro: Supernatural Detective* (2005-2009); después, *El joven
  Ashigaru astuto* (逃げ上手の若君). Su debut fue en 2004 ✅
  ([にじめん](https://nijimen.kusuguru.co.jp/topics/605488)).

### 18.2 Cómo dibuja Matsui (el manga)

- Matsui dice que para el primer capítulo **primero imaginó la escena
  clave (las páginas 2-3) y construyó la historia alrededor**, y que "la
  inspiración no sale sólo de calcular" ✅ (paráfrasis de una entrevista de
  にじめん/jump-mangasho, sin cita textual del japonés porque las fuentes
  sólo la resumen).
- Tiene una entrevista dedicada a su cuidado del **"blanco" (余白)**: el
  espacio que decide NO dibujar, comparado con un calígrafo (前田鎌利) en
  [Oricon](https://www.oricon.co.jp/news/2069215/) (título: «松井優征が語る
  "白"のこだわりと読者の目を遅らせる画面», "el cuidado del blanco y la
  pantalla que retrasa el ojo del lector"). **El texto completo de la
  entrevista está detrás de un muro de pago** (sólo se lee la entradilla):
  confirmo el tema y el titular, no el contenido completo ⚠️.
- **No encontré** ❌ qué programa usa Matsui para el manga (a mano o
  digital): las búsquedas (`松井優征 作画 ペン インタビュー デジタル`, `Matsui
  drawing tools interview`) no dan una respuesta directa. Dado que Shonen
  Jump migró la mayoría de sus series a **CLIP STUDIO PAINT** entre 2015 y
  2020, es razonable para el redactor **no afirmarlo** sin fuente directa.

### 18.3 Cómo está dibujado el anime — medido, no de memoria

Usé `estilo.py` (ya lo corrieron los investigadores de imagen y vídeo sobre
sus propias imágenes; cito sus JSON, que están en la carpeta de trabajo
compartida, no repito la medición) ✅:

| Tipo de imagen | Sombreado | Línea | Color de línea | Fuente medida |
|---|---|---|---|---|
| **Arte clave de personaje** (ilustración del 10.º aniversario) | **Plano (cel), 82-86% de la imagen** | **Poca línea** (2.3-3.2% de densidad) | **No es negro puro**: gris-marrón oscuro (`#5C4C4D`, `#3A392A`, `#4E5358`) | `estilo/10th_anni/estilo.json` (imagen), 3 ilustraciones oficiales de Fandom |
| **Fondo del edificio viejo** (fotograma 2×24) | **Degradado/pintado, 60-72%** | Poca línea (0-2.4%) | Verdoso apagado (`#9DAF97`) o sin línea marcada | `f_2x24/estilo/estilo.json` (vídeo), 2 fotogramas |
| **Escena de interior con luz** (fotograma 2×06) | **Mixto**: 29-50% degradado, 31-58% plano | Poca línea (3.9-4.8%) | Marrón/oliva (`#7F704B`, `#605E50`) | `f_2x06/estilo/estilo.json` (vídeo), 2 fotogramas |

**Lectura para replicar**: es el patrón normal del anime de TV de 2015 —
**personajes con línea de color (no negra) y sombreado plano de 2 tonos
(cel-shading)**, sobre **fondos pintados con degradados suaves** (más
detalle, más luz, sin apenas línea). Esto **confirma y mide** lo que
`biblia.md` §18 (guía IA) ya decía de memoria ("línea fina y limpia,
sombreado de dos tonos"): ahora tiene datos ✅ y sube de ⚠️ a ✅.

### 18.4 Cómo replicarlo en Photoshop y Blender

**Photoshop (arte 2D, personajes)**
1. **Línea**: pincel de entintado fino (2-4 px a 2000 px de ancho), pero
   **coloreado, no negro puro**: usa un tono oscuro de la misma familia
   que la piel/ropa de esa zona (gris-marrón `#4E4A4A` de base, ajustable
   por zona) — así se ve la línea de las ilustraciones oficiales medidas.
2. **Sombreado**: capa de "Multiplicar" con **selección de bordes duros**
   (sin difuminar), un único tono de sombra por zona de luz — **dos
   valores** (luz/sombra), nunca degradado a mano alzada en el personaje.
3. **Piel y objetos redondeados** (la cabeza de Koro-sensei): un **brillo
   pequeño en "Trama de luz" (Screen)**, óvalo blanco al 40-60% opacidad,
   arriba a la izquierda.
4. **Fondos**: al contrario que el personaje, aquí sí degradado: pinceles
   de aerógrafo suaves, varias capas con opacidad baja, luz cálida desde
   una ventana o el atardecer (ver paleta del punto 4 de la biblia).

**Blender (objetos y escenas 3D)**
1. **Contorno**: activar **Freestyle** (Render Properties → Freestyle) con
   grosor 1.5-2.5 px y **color no negro** (gris-marrón oscuro, igual que en
   2D) — o el modificador **Solidify** invertido con un material de
   contorno si se necesita exportar a otro motor.
2. **Shader**: nodo **Shader to RGB** + una rampa de color de **2-3
   escalones** (no degradado continuo) conectada a un Principled BSDF con
   rugosidad alta (mate) — así se logra el cel-shading de 2 tonos medido
   arriba.
3. **Luz**: una luz de área grande y suave (Sol o Area con radio grande)
   más una de relleno tenue; evitar sombras duras y contrastadas — los
   fotogramas medidos tienen brillo medio 22-45 (no oscuro).
4. **Render**: Eevee (rápido, ideal para este estilo plano) con **Bloom**
   suave activado para el brillo de ventanas y del cielo nocturno con luna.

### 18.5 Encuadres y composición típicos (de lo ya mirado por vídeo/imagen)

- **Plano medio desde los pupitres** con uno desenfocado delante, cámara a
  la altura de un alumno sentado — ya en `biblia.md` §18 (guía IA), lo
  confirmo como patrón de composición, no sólo de IA ✅.
- Las **escenas de examen y de combate** cierran mucho el encuadre en la
  cara de Koro-sensei (para mostrar el color) — visto en las capturas de
  vídeo ya analizadas por el investigador de vídeo (`f_2x06`, `f_2x24`).

---

## Punto 24 · Obras parecidas y temas relacionados (NUEVO)

### 24.1 Recomendaciones de la propia audiencia (AniList)

De `partes/datos-texto.md` (ya recolectado, sin repetir la consulta), las
más votadas por usuarios que vieron Assassination Classroom ✅:

| Obra | Nota | Votos | Por qué se parece |
|---|---|---|---|
| Great Teacher Onizuka (GTO) | 84 | 104 | Profesor poco ortodoxo que cambia una clase de problemáticos |
| My Hero Academia | 76 | 176 | Clase, elenco coral, shonen de la misma época de Jump |
| Danganronpa: The Animation | 69 | 156 | Jóvenes en una situación de "matar o morir" |
| Classroom of the Elite | 76 | 362 | Ambientación de instituto con juegos de poder |
| Talentless Nana | 70 | 177 | Estudiantes con una misión de asesinato encubierta |
| Soul Eater | 77 | 28 | Estudiantes-arma, tono de acción con comedia |

### 24.2 Comparaciones críticas (TV Tropes)

**TV Tropes bloquea el acceso directo desde este contenedor** (403,
"Just a moment... / cf-mitigated: challenge" de Cloudflare, en dos
intentos: sin cabecera y con cabecera de navegador). Cito su contenido a
través de los resultados de búsqueda, que sí lo reproducen ⚠️ (una fuente,
sin poder verificar visitando la página):

- La obra se compara con **«GTO mezclado con ciencia ficción y espionaje»**
  ([TV Tropes, vía búsqueda](https://tvtropes.org/pmwiki/pmwiki.php/Manga/AssassinationClassroom)).
- **Danganronpa** es "la que más se acerca en estilo": ambas ponen a
  jóvenes en un "mata o te matan".
- El propio manga **hace referencia (Shout Out) a Doraemon y a El Puño de
  la Estrella del Norte** en distintos capítulos
  ([TV Tropes ShoutOut, vía búsqueda](https://tvtropes.org/pmwiki/pmwiki.php/ShoutOut/AssassinationClassroom)).
  **Dato para el servidor**: Doraemon ya tiene su propia biblia (encargo
  19, canal `#recursos`) — el cruce está documentado por la propia serie,
  no es invención nuestra.

### 24.3 Influencia del propio autor

- Matsui Yuusei (**mismo autor**) hizo antes ***Neuro: Supernatural
  Detective*** (2005-2009): comparten el tema de **"un ser sobrehumano de
  moral ambigua que acaba mejorando a la gente que toca"**
  ([TV Tropes, vía búsqueda](https://tvtropes.org/pmwiki/pmwiki.php/Manga/AssassinationClassroom);
  confirmado también en
  [にじめん](https://nijimen.kusuguru.co.jp/topics/605488): "ambas comparten
  el crecimiento y evolución humana, con humor negro") ✅ (dos fuentes).
- Después hizo ***El joven Ashigaru astuto*** (逃げ上手の若君, 2021-), su
  tercera serie, también en Shonen Jump.

### 24.4 Qué otra lámina del servidor se le parece

- **25 · My Hero Academia** (canal `#material-de-clase`): **el choque más
  directo** — otro instituto, otra clase con nombre de letra, elenco
  coral. La propia AniList lo recomienda a quien vio Assassination
  Classroom (176 votos, nota 76). El redactor debería **evitar repetir**
  la composición de "aula con pizarra al fondo" entre las dos láminas si
  van a canales visibles cerca uno del otro.
- No hay otro canal de "clases" además de estos dos entre los encargos
  revisados (01-41, 57, 77-79): la coincidencia se limita a esa pareja.

---

## Punto 25 · El mundo, la historia y sus símbolos (NUEVO)

### 25.1 Las reglas del mundo, en cinco líneas

1. Una criatura amarilla y con tentáculos (más tarde llamada **«Koro-sensei»**,
   "el profesor al que no se puede matar", 殺せんせー) **destruye el 70% de
   la Luna** y amenaza con destruir la Tierra en un año si no lo detienen ✅
   ([en.wikipedia.org](https://en.wikipedia.org/wiki/Assassination_Classroom)).
2. El **gobierno japonés** confía la misión de matarlo **sólo** a los 28
   alumnos y profesores de la **Clase 3-E** del instituto Kunugigaoka (椚ヶ丘中学校),
   la clase de los peores expedientes, con una **recompensa de 100億円 (10
   000 millones de yenes)** ✅ (dos fuentes:
   [ja.wikipedia.org](https://ja.wikipedia.org/wiki/%E6%9A%97%E6%AE%BA%E6%95%99%E5%AE%A4),
   confirmado también por búsquedas cruzadas con Yahoo!知恵袋; el
   [en.wikipedia.org](https://en.wikipedia.org/wiki/Assassination_Classroom)
   lo traduce directamente como «¥10 billion»). **Ojo con la traducción**:
   億 = 100 millones, no "billón" en inglés; **100億円 son 10 000 millones
   de yenes**, no "100 000 millones" como traduce mal alguna síntesis
   automática. **≈70 millones de USD** al cambio aproximado de 2015-16
   (cálculo propio, no de una fuente) ⚠️.
3. **Reglas fijas**: Koro-sensei **no puede dañar a ningún alumno de la
   3-E** bajo ninguna circunstancia (aunque le disparen); a cambio, los
   alumnos reciben **armas especiales del gobierno** capaces de herirlo (los
   cuchillos y pistolas de balas de antimateria, siempre de colores vivos,
   nunca realistas) ✅.
4. Si alguien **cuenta el secreto** fuera de la clase, el gobierno le
   **borra la memoria** ⚠️ (una síntesis lo dice, no lo vi citado en el
   wikitext directamente: dejar con aviso).
5. El **plazo es el fin del curso escolar** (marzo): si nadie lo consigue
   antes, Koro-sensei destruirá la Tierra ✅.

### 25.2 La historia por arcos (con nombres reales, no inventados)

Arcos según la web oficial (títulos de episodio "〜の時間") y fuentes
japonesas cruzadas ✅:

| Cuándo (curso) | Arco | Qué pasa |
|---|---|---|
| Abril | **Llegada de Koro-sensei** | Primer contacto; la clase decide intentar matarlo por el premio y por hastío |
| Mayo | **Llegada de Irina** (イリーナ) | Se suma como profesora de inglés y asesina profesional rival |
| Junio-julio | **Debilidad al agua** / exámenes de mitad de año | Se descubre que el agua frena a Koro-sensei; primer examen contra la Clase A |
| Verano | **Campamento de Okinawa** | Viaje de 2-3 días; intento de asesinato con virus que casi mata a Koro-sensei y pone a la 3-E en peligro (le hacen de "enfermeros") ✅ ([manga-tettei.com](https://manga-tettei.com/ansa-7/)) |
| Septiembre-octubre | **Llegada de Itona** y de Ritsu (律, el "arma androide") | Nuevo alumno-arma rival; Ritsu se instala como el "ordenador" de la clase (§7.2 de `biblia.md`) |
| Otoño | **Viaje de estudios a Kioto** (修学旅行の時間) | 2 noches en Kioto; Karasuma ordena seguir el asesinato durante el viaje ✅ ([ansatsu-anime.com](https://www.ansatsu-anime.com/2014-2016/story/detail_1st.php?id=1000361)) |
| Otoño | **Festival cultural** (文化祭) | La 3-E monta un puesto de comida con ingredientes de la montaña; acaban 3.º de todo el colegio ✅ ([búsqueda cruzada](https://manga-tettei.com/ansa-7/)) |
| Invierno | **Exámenes finales contra la Clase A** | El director convierte a la Clase A en arma contra la 3-E; los 28 alumnos logran entrar todos entre los 50 mejores del curso ✅ |
| Invierno | **El pasado de Koro-sensei** (過去の時間) | Se revela que fue un asesino humano ("死神", el Dios de la Muerte/Reaper) convertido en la criatura por el científico **Yanagisawa Kotarou** (柳沢誇太郎, alias **Shiro/白**) ✅ ([pixiv百科](https://dic.pixiv.net/a/%E6%AD%BB%E7%A5%9E(%E6%9A%97%E6%AE%BA%E6%95%99%E5%AE%A4)), [natalie.mu](https://natalie.mu/comic/news/169566)) |
| Marzo | **Batalla final** contra el grupo mercenario **«群狼» (Gunrō, "Manada de Lobos")**, liderado por **Craig Hōjō**, y **la graduación**: los alumnos deciden juntos matar a Koro-sensei por cariño, no por el dinero | ✅ (dos fuentes: [ja.wikipedia.org](https://ja.wikipedia.org/wiki/%E6%9A%97%E6%AE%BA%E6%95%99%E5%AE%A4), [comic.tatsuya-book.com](https://comic.tatsuya-book.com/craig-hojo/)) |

**Después del final**: la recompensa sube a **300億円 (30 000 millones de
yenes)**; parte se usa para pagar estudios futuros de los 28, y parte para
**comprar la montaña detrás del colegio viejo**, que se conserva como
"el sitio al que siempre pueden volver" ✅ (dos fuentes: ja.wikipedia.org,
sintetizado también en
[anime-mahoubako.hatenablog.com](https://anime-mahoubako.hatenablog.com/entry/ansatsu-saisyuukai)).

### 25.3 Emblemas, logos de grupos y objetos icónicos

- **No hay un escudo o emblema oficial de diseño para la Clase 3-E**
  (como un blasón dibujado): busqué `暗殺教室 E組 校章 エンブレム` y sólo salen
  resultados de escudos escolares genéricos o de otras franquicias. **No lo
  encontré** ❌, no "no existe": lo más parecido es la **letra "E" grande**
  sobre fondo verde pizarra que usa el propio fandom para referirse a la
  clase ("エンドのE組", pixiv百科, ya citado).
- **Objetos icónicos ya documentados en `biblia.md`** (no repito): la
  pizarra verde (§7.2), el cuaderno de puntos débiles de Nagisa (§7.2), la
  guía del viaje de 2.400 páginas (§7.2), Ritsu/la pantalla (§7.2).
- **Grupo mercenario 群狼 (Gunrō)**: "Manada de Lobos", especialistas en
  guerrilla y sabotaje, menos de 30 miembros, liderados por **Craig Hōjō**
  (apodado 「神兵」, "el soldado divino") — el último obstáculo antes del
  asesinato final ✅ (dos fuentes arriba).
- **死神 (Shinigami, "el Dios de la Muerte / Reaper")**: apodo del pasado
  humano de Koro-sensei como asesino profesional, antes del experimento de
  Yanagisawa ✅.

### 25.4 Vocabulario propio que un fan reconoce al instante

| Palabra | Qué significa | Estado |
|---|---|---|
| **暗殺教室** (Ansatsu Kyōshitsu) | "Aula de asesinato", título de la obra | ✅ |
| **殺せんせー** (Korosensei) | Juego de palabras: 殺す (matar) + 先生 (profesor); "no se le puede matar" | ✅ (ya en biblia.md) |
| **E組** (E-gumi) | Clase E, la de peor fama académica del instituto | ✅ |
| **3年E組** | "3.º E", el curso completo del grupo protagonista | ✅ |
| **椚ヶ丘中学校** (Kunugigaoka) | El instituto donde pasa todo | ✅ (ya en biblia.md) |
| **群狼** (Gunrō) | El grupo mercenario final | ✅ |
| **死神** (Shinigami) | El pasado humano de Koro-sensei | ✅ |
| **弱点** (jakuten) | "Punto débil": cada debilidad de Koro-sensei que Nagisa anota | ✅ (ya en biblia.md §7.2) |
| **抜き打ちテスト** (nukiuchi test) | "Examen sorpresa"; también el nombre del evento oficial del 10.º aniversario (ya en biblia.md §7.7) | ✅ |
| **弱点その…** | Numeración de los puntos débiles en el cuaderno de Nagisa | ✅ (ya en biblia.md) |

---

## Lo mejor para la lámina (máximo 5 líneas)

1. El **HUD real de los videojuegos** (etiqueta amarilla `#FFEA62` + caja
   crema + letra gótica negra) es más fiel que inventar una burbuja: úsalo
   para una "notificación" dentro de la lámina.
2. Punto 18 da la **receta medida** (línea de color, no negra; sombreado
   plano de 2 tonos en el personaje; degradado sólo en fondos) — aplicable
   directo en Photoshop/Blender.
3. El sello real del aviso oficial (🎓🌕, ya en `biblia.md` §7.7) combinado
   con el vocabulario de §25.4 (**「抜き打ちテスト」**, **「弱点」**) da un
   texto que suena "de la serie" y no genérico.
4. El icono de la **luna en creciente + la pizarra verde** son el símbolo
   más reconocible sin depender de la cara (que cambia de color).
5. La montaña comprada con la recompensa final (§25.2) es una imagen fuerte
   para "el lugar al que siempre se puede volver" si el canal quisiera una
   lámina 2 sobre comunidad.

---

## No encontré (⚠️ extra, no bloquea el encargo)

- ⚠️ Quién diseñó el logo japonés 暗殺教室 y con qué tipografía base (§5).
- ⚠️ El texto completo de las entrevistas de Kishi/Uezu (Natalie) y de
  Matsui sobre el "blanco" (Oricon): ambas bloquean la lectura completa
  (Natalie, 403; Oricon, sólo entradilla libre) — cito el tema, no el
  texto.
- ⚠️ Qué programa usa Matsui para dibujar el manga (a mano o digital).
- ⚠️ Un segundo nombre de director de arte (Shimoyama Kazuto) sin segunda
  fuente.
- ⚠️ Si Koro-sensei aparece en *J-Stars Victory VS* (dato menor, de
  memoria en la primera pasada, sigue sin confirmar).
- ❌ Un emblema o escudo diseñado específicamente para la Clase 3-E (no
  parece existir como pieza de arte, más allá de la letra "E").

---

## Bitácora de búsqueda (segunda pasada · texto, juegos y técnica)

### Comprobación de red (25-sep-2026, esta sesión)

- **Ahora responden** (antes cerrados en la primera pasada): Doblaje Wiki
  (200), `ja.wikipedia.org` (200 tras un primer 429), `en.wikipedia.org`
  (200), Famitsu (200), 4Gamer (200), Dengeki (200), GitHub (sin cambios).
- **Siguen bloqueados**: `tvtropes.org` (403, Cloudflare "cf-mitigated:
  challenge", dos intentos: sin cabecera y con user-agent de navegador),
  `web.archive.org` (rechazado por la herramienta de fetch), Comic Natalie
  (403 al extraer el cuerpo del artículo, aunque el enlace carga).
- **La wiki de Fandom de la serie da 404 en el subdominio que sugiere el
  encargo** (`assassinationclassroom.fandom.com`); el correcto es
  `ansatsukyoshitsu.fandom.com` (confirmado por su API `siteinfo`, 200 OK).
  El resto de subdominios probados (`assassination-classroom`,
  `ansatsukyoshitsu` en mayúsculas distintas, `koro-sensei`) dan 404 o
  challenge de Cloudflare en la web normal.

### Búsquedas web (18, todas nuevas sobre las 47 de la primera pasada)

| # | Idioma | Búsqueda | Qué saqué |
|---|---|---|---|
| 1 | ja | 暗殺教室 アニメ 作画 セルシェイディング Lerche 制作 | Estudio y staff, sin detalle técnico |
| 2 | en | Studio Lerche Assassination Classroom animation production technique interview | Sin entrevista técnica específica |
| 3 | ja | 岸誠二 暗殺教室 演出 インタビュー 殺せんせー デザイン | Entrevista Kishi×Uezu en Comic Natalie |
| 4 | en | Assassination Classroom TV Tropes similar works influences | GTO+espionaje, Danganronpa, Neuro del mismo autor, Shout Outs |
| 5 | ja | 暗殺教室 世界観 用語集 用語 出席番号 弱点 E組 | Vocabulario base |
| 6 | ja | 暗殺教室 賞金 100億円 政府 殺せんせー 暗殺 | Cifra del premio |
| 7 | — | (WebFetch) ja.wikipedia.org/暗殺教室 | Reglas del mundo, arcos, premio, vocabulario |
| 8 | — | (WebFetch) en.wikipedia.org/Assassination_Classroom | Confirmación en inglés del premio (¥10 000 millones) |
| 9 | ja | 暗殺教室 賞金 300億円 増額 最終回 理由 | Premio final y en qué se gastó |
| 10 | ja | 暗殺教室 ロゴ シンボル マーク E組 校章 エンブレム | Sin emblema oficial documentado |
| 11 | ja | 暗殺教室 ストーリー 編 一覧 水泳大会編 文化祭編 修学旅行編 期末試験編 最終決戦編 | Nombres de arcos |
| 12 | ja | 暗殺教室 名場面 章 一覧 期末試験 水泳大会 合宿 修学旅行 文化祭 過去編 | Detalle de festival cultural y viaje a Kioto |
| 13 | ja | 暗殺教室 松井優征 死神 過去編 柳沢 グルロー 用語 | Shinigami, Yanagisawa, Shiro |
| 14 | ja | "群狼" 暗殺教室 傭兵 組織 | El grupo mercenario final y su líder |
| 15 | ja | 暗殺教室 似ている作品 影響 松井優征 好きな漫画 | Neuro del mismo autor, tema compartido |
| 16 | ja | 暗殺教室 ロゴ デザイン 集英社 誰がデザイン タイトルロゴ 書体 | Sin diseñador confirmado |
| 17 | en | "Assassination Classroom" logo font Futura Bold identification | Segunda fuente de Futura |
| 18 | ja | 松井優征 暗殺教室 作画 ペン 画材 インタビュー デジタル 原稿 | Entrevista del "blanco" en Oricon (bloqueada) |

### Páginas oficiales y de prensa leídas directamente

- [ansatsu-anime.com/2014-2016/story/](https://www.ansatsu-anime.com/2014-2016/story/)
  (WebFetch: sólo lista episodios, sin sinopsis por arco).
- [ansatsu-anime.com/2014-2016/story/detail_1st.php?id=1000361](https://www.ansatsu-anime.com/2014-2016/story/detail_1st.php?id=1000361)
  (viaje a Kioto).
- Famitsu (`famitsu.com/news/201603/18101425.html`, WebFetch) y 4Gamer
  (`4gamer.net/games/278/G027887/20150227043/`, WebFetch): descripción +
  **7 capturas bajadas y miradas** (`curl`, montadas en hoja de contacto
  propia con Pillow, leídas con la herramienta de lectura de imágenes).
- Oricon (`oricon.co.jp/news/2069215/`): bajado con `curl`, decodificado de
  **Shift-JIS** (el WebFetch normal daba texto corrupto por la codificación
  del sitio) — sólo entradilla libre, resto de pago.

### GitHub y herramientas locales (sin cupo de búsqueda)

- `estilo.py`: **no volví a medir** paletas propias; **reutilicé** el
  `estilo.json` que ya generaron los investigadores de imagen
  (`.../24-assassination-classroom-imagen/estilo/10th_anni/estilo.json`) y
  de vídeo (`.../24-assassination-classroom-video/f_2x06/estilo/estilo.json`,
  `f_2x24/estilo/estilo.json`) en la carpeta de trabajo compartida, para no
  repetir el gasto.
- Pillow (`Image.getpixel`) para medir a mano el amarillo de la etiqueta
  (`#FFEA62`) y el crema de la caja de texto (`#F5F7E2`) de las capturas de
  Famitsu.

### Fuentes consultadas por tipo (sólo las nuevas de esta parte)

- **Oficiales**: ansatsu-anime.com (historia, viaje a Kioto), Famitsu,
  4Gamer, Dengeki (juegos).
- **Wikis**: ja.wikipedia.org, en.wikipedia.org, pixiv百科 (死神, シロ),
  アニヲタWiki, ナムウィキ.
- **Prensa/entretenimiento**: Oricon (Shift-JIS, bajado a mano), Comic
  Natalie (bloqueada), にじめん, manga-tettei.com.
- **Comunidad/fans**: comic.tatsuya-book.com, animegametyadaisuki (blog),
  anime-mahoubako.hatenablog.com, TV Tropes (sólo vía resultados de
  búsqueda, la web bloquea el acceso directo).
- **Tipografía**: dafont (foro), FontMeme, Yahoo!知恵袋 (pregunta sin
  responder sobre el logo japonés).

Sigue: ninguno de los 6 puntos asignados (5, 6, 11, 18, 24, 25); todos
tienen lo obligatorio de ENCARGO.md. Quedan como ⚠️/❌ opcionales (no
bloquean): el diseñador del logo japonés, el texto completo de las
entrevistas de Kishi/Uezu y de Matsui (bloqueadas), el programa de dibujo
de Matsui, el segundo nombre de dirección de arte, y Koro-sensei en J-Stars
Victory VS.
