---
tags: [biblia, serie, laminas]
serie: "Adventure Time (Hora de aventura)"
canal: "#musica-nueva"
fecha: 2026-09-24
---

# Biblia · Hora de aventura — para #musica-nueva

> [!important] Cómo se hizo, y sus límites
> - **Segunda pasada (25-26 sep 2026, red abierta)**: un equipo de cuatro
>   investigadores (imagen, vídeo, voz, texto) y un redactor. Se pudo usar:
>   la API de la wiki en inglés (**`adventuretime.fandom.com`**: el
>   subdominio del encargo redirige ahí), la de **Doblaje Wiki** (con
>   `curl -A "Mozilla/5.0"`) y la de Hora de Aventura Wiki en español;
>   **1188 imágenes de la wiki en 13 hojas de contacto** (3 en `hojas/`,
>   §3.0); **7 clips reales en Dailymotion** (opening latino, créditos,
>   «Fry Song», «I'm Just Your Problem», «I Remember You», tráiler de
>   «Obsidian» y el piloto) mirados con `fotogramas.py`; `estilo.py` y
>   Pillow para **medir colores**; **6 muestras de audio del doblaje**
>   oídas con `voz.py`; APIs de Sketchfab, Wallhaven, ambientCG,
>   MusicBrainz, TikTok (oEmbed) y Arctic Shift (Reddit); fontTools.
> - **Lo que no se pudo en la segunda pasada**: YouTube pidió iniciar
>   sesión todo el día (los enlaces de YouTube de abajo son de la primera
>   pasada, sin mirar). TCRF dio 403, la Wayback Machine cortó la conexión,
>   Ranker dio 401 y TikTok no deja contar vistas. Los clips de
>   Dailymotion son de **720p** casi todos (sólo el opening y el tráiler
>   de «Obsidian» llegan a 1080p). Crunchyroll no se usa.
> - Los minutos **vistos** en vídeo llevan el enlace `?t=` o dicen «visto»;
>   los de la primera pasada siguen como «≈» (calculados por la
>   transcripción).
>
> **Primera pasada (24 sep 2026)**:
> - **La red estaba cerrada.** Fandom (las tres wikis: inglés, Hora de
>   Aventura y Doblaje Wiki), Discogs, Mondo, iam8bit, Flickr, Sketchfab
>   (web y API), OpenSubtitles, Subtitle Cat, Art of the Title,
>   cartoonnetwork.com e i.ibb.co daban error por curl. Wikipedia,
>   YouTube, Reddit y TV Tropes ya se sabían cerrados y no los reintenté.
>   WebFetch probó dos webs de noticias y Spotify: las tres,
>   **bloqueadas**. Por eso **no se pudo correr**
>   `herramientas/investigar_serie.py`: **no hay hojas de contacto** ni
>   carpeta `hojas/`, y **no medí colores** en capturas (los hex van
>   marcados como aproximados).
> - Hice **50 búsquedas web** (español, inglés y una en japonés). La lista
>   está al final, en la bitácora.
> - GitHub sí respondía, y de ahí salió lo más útil:
>   **las transcripciones de 239 episodios**, con acotaciones de escena
>   («Marceline flota», «toca el bajo», «sisea»), del repositorio
>   [guiszk/adventuretime-transcripts](https://github.com/guiszk/adventuretime-transcripts)
>   (sacadas de la wiki en inglés). Con ellas cito frases exactas y
>   describo poses.
> - **Los minutos son estimados.** No encontré subtítulos con tiempos
>   (ni en GitHub ni en sitios abiertos). El minuto «≈2:11» lo calculo por
>   la posición de la línea dentro de la transcripción, sobre 11 minutos
>   por episodio (44 en los especiales). **Puede fallar ±1 minuto**:
>   compruébalo en el vídeo antes de sacar el fotograma.
> - Bajé de [google/fonts](https://github.com/google/fonts) las letras
>   propuestas y comprobé con fontTools que traen á é í ó ú ñ ¿ ¡ ü.
> - Cómo leo los episodios: «3×10» es temporada 3, episodio 10. Título
>   en inglés y, si lo encontré, el latino.
> - ✅ **confirmado**: dos fuentes, o lo dice la transcripción.
>   ⚠️ **dudoso**: una sola fuente, o lo digo de memoria. Lo de memoria
>   siempre va marcado.

> [!note] Segunda pasada · qué cambió
> **Corregido (antes → ahora)**
> - **Piel de Marceline**: `#A9B8C2`, «gris azulado», de memoria →
>   **`#D8E7E7`**, casi blanca con un toque menta, medida dos veces en el
>   *model sheet* oficial y en una captura (§5.3, §16). El `#657471` que
>   da un fotograma es la piel **en sombra**, no su color.
> - **Pelo**: «negro azulado» `#1C1B2B` → **negro puro `#000000`** en el
>   color plano (en escena, `#150209`).
> - **Finn**: «camiseta celeste» `#35A9E0` → **`#018BCB`**; piel `#FDE5DA`.
> - **Licencias 3D**: «sin ver» → leídas en la API: el bajo de **Haxis es
>   CC BY**; el «Low Poly» de cuxilrodas **no es Creative Commons**
>   («Free Standard») (§4.1).
> - **«¡Oh por Glob!»**: «dato confuso» → **muletilla latina de la
>   Princesa Grumosa**, confirmada (§10.4).
> - **Karla Falcón**: «vuelve desde la 4» → vuelve en el **ep. 96, «Rey
>   Gusano»**, tras **una campaña de los fans** (§10.2, §E). Claudia Urbán
>   la suplió en los eps. 58-94.
> - **BMO latino**: una fuente → **Gustavo Melgarejo** (T1-5) y **Héctor
>   Emmanuel Gómez** (desde «El traje de Jake»), con dos fuentes.
> - **Disco en español**: fecha dudosa → **25-oct-2019**; pistas 3 y 6 con
>   su nombre de MusicBrainz y duración (§3.4).
> - **«I Remember You»**: sólo notas → también **una Polaroid** de Marcy
>   niña (visto, §2.4).
> - **«I'm Just Your Problem»**: luz de cueva → **tarde despejada** sobre la
>   puerta de los círculos dorados; y lleva **sombrero mostaza** (nuevo).
> - **Fuente de fans del logo**: «no sé si trae tildes» → las tiene sólo
>   en Mac Roman; **no sirve para español** en Windows (§6.1).
> - **Letrista de BOOM!**: de memoria → **Steve Wands**, dos fuentes.
>
> **Añadido**
> - **Hojas de contacto** (§3.0) y arte de producción visto (§3.7).
> - **Escenas y poses vistas en vídeo** con minuto y `?t=` (§2, §12.0,
>   §15.0); **caras por emoción** (§8.2).
> - **Colores medidos** de la casa, el Reino de Cristal y los trajes
>   (§5.3, §16).
> - **Doblaje leído en la API**: directores por temporada, traductores,
>   Arturo Castañeda, y **6 frases textuales oídas** (§10).
> - Personajes a fondo, **Rey Helado/Simon** con ficha propia y voces
>   medidas (§8.1-8.4); popularidad con fuentes (§9).
> - Retratos del juego de DS y menú de Card Wars (§7.3, §13).
> - Los puntos nuevos del encargo: estilo y técnica (§A), texturas 2D
>   (§B), gustos (§C), por qué la aman (§D), fan dubs (§E),
>   colaboraciones (§F), obras parecidas (§G) y el mundo (§H).
> - Guía de IA **de texto** con frases por emoción (§18.7); tabla
>   «Cumplimiento del encargo»; **157 referencias** (antes 36).
> - Conceptos: los tres siguen, con imágenes vistas; **A pasa a ser el
>   recomendado** (todo su sitio está visto y medido).
>
> **Los ⚠️**: había **84**; ahora hay **164**, porque las secciones nuevas
> marcan una a una lo dudoso. De los viejos se resolvieron los de
> colores, licencias, doblaje, poses de Marceline, fuente del logo y
> fecha del disco. Lo que queda está en §20.2 y en la tabla de
> cumplimiento.

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección 📡 NOTICIAS):

> **ıı・🎵・musica-nueva** (texto) · 0 fijados · 0 de personas en los
> últimos 15 — _Solo cuando un artista saca disco, single o EP. Nada de
> vida personal. Para pedir un artista: sugerencias._

Función según el encargo: **estrenos musicales**.

### Lo que el canal pide (tres reglas)

1. **Sólo estrenos**: disco, single o EP.
2. **Nada de vida personal** del artista.
3. **Para pedir un artista**, se va a **#sugerencias** (foro con
   etiquetas Nueva, En estudio, Aprobada, Rechazada, Hecha).

### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Música nueva** | nombre del canal |
| 2 | **Aquí sólo entran estrenos** | para qué es |
| 3 | **Disco** | formato 1 |
| 4 | **Single** | formato 2 |
| 5 | **EP** | formato 3 |
| 6 | **Nada de vida personal** | lo que no va |
| 7 | **¿Quieres un artista? Pídelo en sugerencias** | a dónde ir |
| 8 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

Los tres formatos encajan con objetos reales de la franquicia (ver §3.4):
un **LP de 12"** (disco), el **single «Monster»** (digital; en la
lámina, un vinilo de 7") y un **10"** o un **casete** (EP). La caja
oficial de Mondo trae justo LP de 12", un 10", un casete y un CD ✅.

### ¿Hace falta lámina 2?

Con ocho textos cabe en una. Si el dueño quiere explicar **cómo se
publica un estreno** (qué poner: artista, título, tipo, fecha, enlace),
propongo **lámina 2**: la **contraportada del disco** con esos cinco
campos como si fuera la lista de canciones (ver §19, concepto A).

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué encaja con #musica-nueva | En la serie **se graban discos**. Marceline graba la «Canción de las papas» con Finn haciendo beatbox («Thanks for helping me record, Finn», 2×01, ≈0:07) ✅. En «Marceline's Closet» (3×21, ≈6:05) enciende su equipo de grabación y dice: «Toma uno para mi **nuevo álbum conceptual**, basado en quinientos años de mi diario» ✅. Y la serie **termina con un estreno**: el Hoyo Musical dice «he estado trabajando en **una canción nueva**. ¿Quieren oírla?» y suena el tema final (10×13, ≈43:04) ✅. |
| El objeto | **El bajo-hacha de Marceline**, que era **el hacha de la familia** («Is this the family ax? Did you turn it into some kind of lute?», dice su padre en 2×01, ≈2:15) ✅. Y los **discos oficiales que existen de verdad**: la **caja de Mondo** con tres LP de 12", un 10", un CD y un casete (2019) ✅, el LP «Come Along With Me» ✅, el doble LP de «Obsidian» ✅ y «BMO's Mixtape» ✅. Hay **seis modelos 3D del bajo en Sketchfab** con licencia leída en su API; el de **Haxis** es **CC BY** (deja uso comercial con crédito) ✅ (§4). |
| Cuadro de diálogo propio | **No hay globos.** La serie pone el texto en **papeles escritos a mano**: la nota de Finn («MARCY, PLEASE COME TO THE TREEHOUSE—IT'S AN AMERGENCY!», 3×21) ✅, las **notas de Simón que Marceline canta** en «I Remember You» (4×25, ≈8:49) ✅ y **el cuaderno de letras** de Marceline (3×21, ≈6:36) ✅. Y las **cartelas de título**, pintadas sobre **papel antiguo escaneado** y con **tramado de cómic viejo** ✅. |
| Personaje | **Marceline**, sin duda: es la música de la serie. Es la favorita de mucha gente: BOOM! la llamó «fan-favorite» en su nota de prensa ✅, Cartoon Network UK la hizo «Character of the Week» (24-ene-2012) ✅ y *The Guardian* la llamó lo mejor de la serie ✅; tuvo su miniserie «Estacas» y su especial «Obsidian» ✅. **No encontré una encuesta oficial** con números. Secundarios que suman: el **Rey Helado/Simon** (*Vulture*: «el mejor personaje») ✅, **BMO** (el favorito del creador, Pendleton Ward) ✅, **Finn** (beatbox), **Jake** (viola) y la **Dulce Princesa** (§9). |
| Voz latina de Marceline | **Isabel Martiñón** (habla), en **toda** la serie: su voz y la de Finn nunca cambiaron ✅ (Doblaje Wiki + dos entrevistas). Frase real oída: «No puedes estar aquí. Ash no quiere que salga con mortales» (§10.4). Sus canciones las cantaron otras: **Claudia Urbán** (temporadas 1-2), **Patty Urbán** (3-4) y **Carla Cerda** (5 en adelante, «Estacas», «Tierras lejanas») ⚠️. |
| Voces latinas del resto | Finn **José Antonio Toledano** ✅, Jake **José Arenas** ✅, Dulce Princesa **Karla Falcón** ✅, Rey Helado **Óscar Flores** ✅. Estudio **Sensaciones Sónicas** (hasta media temporada 5) y luego **SDI Media de México** ✅. |
| Noticia que viene justo | **«Hora de aventura: Misiones Secundarias»** llega a **Cartoon Network y HBO Max en Latinoamérica el 5 de octubre de 2026**, doblada, con **José Arenas** otra vez como Jake ✅. |
| Letras | Títulos: **Chewy** o **Luckiest Guy** (redondas y gorditas, como el logo). Letra de Marceline a mano: **Rock Salt** o **Permanent Marker**. Pantalla de BMO: **VT323**. Todas con tildes, ñ, ¿ y ¡: **comprobado en el archivo**. |
| Tono | Colores vivos y **planos**, **línea fina y uniforme**, **brazos de fideo** sin codos, **ojos de punto**. Las escenas de Marceline van de **su casa rosa por dentro** (`#F8AEC5`, medido) a la **noche** y a los **violetas del Reino de Cristal** (`#422D6B`, medido en «Obsidian»). Divertido, pero con un fondo melancólico. |

---

## 2 · Las escenas que sirven para #musica-nueva

Todas salen de las transcripciones de
[guiszk/adventuretime-transcripts](https://github.com/guiszk/adventuretime-transcripts).
El texto entre comillas es **el inglés original**; la traducción es mía,
salvo donde digo que es del doblaje. **Minutos estimados** (ver arriba).

**Segunda pasada: vistas en vídeo real.** Cuatro de estas escenas se
miraron fotograma a fotograma con `fotogramas.py` en clips de Dailymotion
(YouTube pedía iniciar sesión). Donde pone **«visto»**, el minuto es el
**del clip**, no el del episodio, con su enlace `?t=`. Las escenas 2.2,
2.5 y 2.8 no tienen clip real: siguen con el minuto estimado ⚠️.

### 2.1 Marceline graba una canción (2×01 «It Came from the Nightosphere», latino «Llegó de la Nocheósfera») ✅

- **≈0:00**: «en la cueva de Marceline, justo fuera de su casa. Finn hace
  beatbox y Marceline rasguea su bajo-hacha».
- **≈0:07**: Marceline: «Thanks for helping me record, Finn» (gracias por
  ayudarme a grabar).
- **≈0:10**: «Now, I'm gonna sing something really personal, so don't
  laugh at me» (voy a cantar algo muy personal, no te rías).
- **≈0:18**: «Start a slow beat, and keep it steady» (empieza un ritmo
  lento y mantenlo).
- **≈0:25**: canta la **Canción de las papas** («Fry Song»). En latino se
  llama «**Canción de las Papas**» ✅
  ([Hora de Aventura Wiki](https://horadeaventura.fandom.com/es/wiki/Canci%C3%B3n_de_las_Papas));
  en el disco oficial en español la pista 6 se llama «**Papi, te
  comiste mis papas**» (1:43) ✅ (MusicBrainz + el vídeo de la página
  latina de la serie en Facebook).
- **≈2:15**: su padre, Hunson Abadeer, ve el bajo: «Whoa! **Is this the
  family ax?** Did you turn it into some kind of lute?» (¿es el hacha de
  la familia? ¿la convertiste en una especie de laúd?). Y se lo lleva.
- **≈2:23**: Marceline: «**My bass!**» (¡mi bajo!).
- **≈9:17**: Finn saca **un walkman** y pone **la canción que grabaron**
  para distraer al padre. El disco que grabaron al principio **salva el
  episodio**.

**Visto en vídeo** ([«Marceline Sing-a-Long Fry Song»](https://www.dailymotion.com/video/x51arca),
52 s, 1280×720; es el montaje «Toon Tunes» de Cartoon Network con la letra
en pantalla, en inglés):
- **0:00**: Finn hace beatbox de pie; **Marceline flota bocabajo tocando
  el bajo-hacha**, en un cuarto de paredes **rosa** con sillones rojos y
  puerta doble azul ✅ ([`?t=0`](https://www.dailymotion.com/video/x51arca?t=0)).
- **0:12**: primer plano de **una grabadora amarilla** sobre la mesa, con
  el cable enchufado: el objeto que graba la canción ✅
  ([`?t=12`](https://www.dailymotion.com/video/x51arca?t=12)).
- **0:28-0:36**: **primer plano de Marceline cantando triste**, ojos
  entornados y boca abierta: «But you ate them, yeah, you ate my fries…
  and I cried» ✅ ([`?t=28`](https://www.dailymotion.com/video/x51arca?t=28)).
- **0:40-0:44**: Finn con **audífonos**, levanta la grabadora ✅
  ([`?t=40`](https://www.dailymotion.com/video/x51arca?t=40)).
- **0:48**: «Daddy, there were tears there», con la mirada baja ✅.
- Ojo: el fondo del montaje puede ser un decorado simplificado para el
  vídeo musical; coincide en color con la casa de Marceline (§5).

> Para la lámina: esta es la escena del **estreno casero**. Un bajo, un
> micro, un amigo haciendo ritmo y una grabadora amarilla.

### 2.2 El álbum conceptual secreto (3×21 «Marceline's Closet») ✅

- **≈4:28**: deja un mensaje en el contestador de Finn y Jake: «It's jam
  time, so, like, call me, 'kay?» (es hora de tocar, llámame).
- **≈6:05**: sola en su cuarto: «Welp... they're not gonna show up, then
  I'll just work on my own stuff». **Toca el bajo y enciende el equipo de
  grabación**: «Take one for **new concept album** based on five hundred
  years of my journal entries» (toma uno del nuevo álbum conceptual, sobre
  quinientos años de mi diario).
- «I wanna make this the most emotional album ever. So private and
  secret, that I'll never let anyone hear» (quiero que sea el disco más
  emotivo de la historia; tan secreto que nadie lo oirá).
- **≈6:36**: «**abre su cuaderno**. Suena una batería de fondo. Marceline
  canta la **Canción del diario**» («Journal Song»).
- Antes (≈5:00), Finn escribe con lápiz, **usando la espalda de Jake de
  mesa**, una nota: «MARCY, PLEASE COME TO THE TREEHOUSE—IT'S AN
  AMERGENCY! Love, FINN + JAKE» (con la falta de ortografía, así en el
  guion). La dobla en **avión de papel**.

> Para la lámina: **el cuaderno de letras** y **la nota de papel** son el
> «cuadro de diálogo» natural de la serie (ver §7).

### 2.3 La banda (3×10 «What Was Missing», latino «Lo que estaba perdido») ✅

- Finn, Jake, Marceline, la Dulce Princesa y BMO **forman una banda** para
  abrir la puerta del Señor de las Puertas, que sólo se abre con música.
- **≈4:36**: «**Jake empieza a tocar su viola y Finn hace beatbox**».
  Marceline canta **«I'm Just Your Problem»** (≈4:41); en latino, «**Soy tu
  problema**» ✅ ([Hora de Aventura Wiki](https://horadeaventura.fandom.com/es/wiki/Soy_tu_Problema),
  [Spotify: «Soy tu Problema», Hora de Aventura Latino](https://open.spotify.com/intl-es/track/3LADlDmcmlWu24MU5VnxMA)).
- **≈4:25**: «la Dulce Princesa **toca a BMO como si fuera un
  instrumento**, BMO se ríe».
- **≈6:25**: se pone el sol; Marceline **se quita el sombrero de sol y
  los guantes**.
- **≈6:52**: la Princesa dirige: «BMO, execute Sound Structure Alpha.
  Marceline, begin playing **triplet quavers in mixolydian mode**».
  Marceline: «Alright, fine. [toca el bajo] **Wait, what's a quaver?**»
  (¿qué es una corchea?).
- **≈6:42**: Jake vuelve **vestido de punk**: «I came back for the music».
- **≈8:41**: Finn canta «My Best Friends in the World» y **reúne otra vez
  a la banda**.

**Visto en vídeo** ([«I'm Just Your Problem», canal oficial de Cartoon
Network en Dailymotion](https://www.dailymotion.com/video/x537pqr), 2:07,
1280×720):
- **0:00**: la Dulce Princesa sostiene **un aparato verde tipo Game Boy**
  (control de sonido) junto a BMO ✅.
- **0:04-0:08**: **Jake corre tocando la viola** ✅
  ([`?t=4`](https://www.dailymotion.com/video/x537pqr?t=4)).
- **0:12-0:24**: **Marceline entra volando con el bajo por delante**
  (filos rojos) hacia la **puerta de piedra en arco con círculos dorados**
  del Señor de las Puertas y toca sobre ella ✅
  ([`?t=12`](https://www.dailymotion.com/video/x537pqr?t=12)).
- **0:24-1:00**: lleva un **sombrero de ala ancha mostaza con cinta
  azul** (medido: `#BBAB4C`, cinta `#4A7AA2`); primeros planos cantando,
  ceño fruncido y **colmillos a la vista** ✅
  ([`?t=52`](https://www.dailymotion.com/video/x537pqr?t=52)).
- **1:32**: con el sombrero, **toca apoyada en la puerta** mientras cae
  la tarde ✅ ([`?t=92`](https://www.dailymotion.com/video/x537pqr?t=92)).
- La luz es de **tarde con cielo despejado**, no de cueva.

> Para la lámina: la única escena con **los cinco tocando juntos**. Sirve
> para un concepto de grupo. Fotograma de la wiki: hoja 9, **#393**
> («S3e10 Marceline singing», 1920×1080).

### 2.4 Canciones escritas en notas (4×25 «I Remember You», latino «Te recuerdo») ✅

- **≈1:57**: «Marceline rasguea su bajo-hacha» en su cueva y ve entrar al
  Rey Helado por la ventana.
- **≈4:45**: el Rey Helado canta su canción de princesas; en latino es
  «**¡Oh, Dulce Princesa!**» ✅
  ([Hora de Aventura Wiki](https://horadeaventura.fandom.com/es/wiki/%C2%A1Oh,_Dulce_Princesa!),
  [Spotify](https://open.spotify.com/intl-es/track/5oZTIVKk1gMDLl2Y6g3wVZ)).
- **≈6:29**: Marceline, frustrada, **se deja caer sentada delante de la
  nevera** y hace rodar una manzana.
- **≈8:39**: el Rey Helado monta su **omnichord**: «Sing out, sister!».
- **≈8:49 a 10:29**: Marceline **canta leyendo las notas** que Simón le
  escribió hace mil años («Singing and reading note»). La letra de
  «**Remember You**» sale de esos papeles. En latino, «**Recordándote**»
  ✅ (Doblaje Wiki + MusicBrainz: pista 4 del disco en español, 2:19).

**Visto en vídeo** ([«Marceline & Ice King — I Remember You»](https://www.dailymotion.com/video/xzt1l7),
1:58, 1280×720; grabación de la emisión de Cartoon Network HD **en
francés**: vale para la imagen, no para frases):
- **0:00-0:12**: el Rey Helado toca un teclado; Marceline entra por la
  puerta de su casa (paredes rosa, suelo verde azulado) **con un papel en
  la mano** ✅.
- **0:18-0:30**: **primer plano de Marceline con una mano en la cabeza**,
  cara de angustia ✅ ([`?t=18`](https://www.dailymotion.com/video/xzt1l7?t=18)).
- **0:42-1:06**: el Rey Helado toca **una batería verde con un «#1» en el
  bombo**; Marceline, sentada, **toca el bajo con cara seria** ✅
  ([`?t=42`](https://www.dailymotion.com/video/xzt1l7?t=42)).
- **≈1:18**: **una sola lágrima**, la cabeza hacia atrás, dientes
  apretados, cantando a dúo con Simon ([`?t=78`](https://www.dailymotion.com/video/xzt1l7?t=78)).
  ⚠️ Las dos partes no coinciden en este segundo: la de voz ve aquí la
  lágrima; la de vídeo ve en 1:18 a **Finn y Jake escuchando por la
  ventana** (con antifaces de dormir en la cabeza). Están a pocos
  segundos: mirar de 1:12 a 1:24.
- **1:36**: primer plano de **una foto Polaroid** de Marceline niña.
  **Corrección**: además de las notas de Simón, en la escena hay **una
  foto** ✅ ([`?t=96`](https://www.dailymotion.com/video/xzt1l7?t=96)).
- **1:42-1:54**: flashback: **Marceline niña con un osito rojo (Hambo)**
  entre ruinas, se acerca a Simon ✅.
- Fotogramas de la wiki: hoja 9, **#396** (tocan juntos), **#403**
  (Marceline con el omnichord), **#404** (la lágrima) y **#408** (la nota
  de Simón: «Marceline, is it just you & me in the wreckage of the
  world?…»), todos 1920×1080.

> Para la lámina: **la letra de una canción escrita en un papel viejo**.
> Es la escena que más lloran los fans (ver §14 y §D).

### 2.5 El concierto en el cementerio (10×07 «Marcy & Hunson») ✅

- **≈6:21**: Jake: «Aren't you giving a concert tonight? At the **Ghost
  Amphitheater**?» (¿no das un concierto esta noche en el Anfiteatro
  Fantasma?).
- **≈7:00**: «Hello, **Hamburger Hills Cemetery**!» (¡hola, cementerio
  de Hamburger Hills!). «Marceline **aparece entre la niebla en el
  escenario** y el público aplaude».
- Hunson: «Marceline! You're doing great, baby!». Ella: «**I haven't
  started yet**» (todavía no empiezo). Canta **«Slow Dance With You»**.
- Hunson: «This is my daughter! **I am proud of my punk daughter!**»
  (¡estoy orgulloso de mi hija punk!).

> Para la lámina: **escenario, niebla y público de fantasmas**. Es el
> «estreno en directo» de la serie. ⚠️ **Sin clip real**: se buscó en
> Dailymotion por canción y por escena («Slow Dance With You Marceline
> concert Hunson») y no salió nada; el minuto sigue estimado.

### 2.6 «Obsidian», el especial de Marceline y la Dulce Princesa (2020) ✅

(«Hora de aventura: Tierras lejanas», episodio 2; 44 minutos.)
- **≈4:41**: en **su casa compartida**, Marceline en forma de murciélago
  monta un mueble con un martillo; luego trae **dos tazas humeantes**.
- **≈6:28**: en la casa, «Marceline **toca el bajo** y la Princesa lee un
  libro»; **≈6:57**, las dos en el sofá mientras ella toca.
- **≈15:25**: «**se apoya en su bajo-hacha** con cara de desgana».
- **≈18:47**: «Next up, [**se echa el bajo al hombro**] taking care of
  that dragon».
- **≈20:17**: toca «**Woke Up**» ante el pueblo de cristal, que se emociona.
- Para el Reino de Cristal, Marceline es una **santa**: «Brave
  St. Marceline… with her silver shovel and **a holy song**» (con su
  pala de plata y una canción sagrada, ≈1:39).
- **≈33:37**: le rompen el bajo: «[Eyes turn red] My bass. **MY BASS!**».
- **≈35:55**: la Princesa: «**your new song must be extra angry and
  sad**» (tu canción nueva tiene que ser extra enojada y triste).
- **≈38:45**: Marceline canta «**Monster**» a la Princesa con una
  **guitarra hecha de caja** que lleva Glassboy a la espalda. Y de niña
  (≈30:51), en el búnker, canta «Red Light» a **cajas y latas con caras
  dibujadas**.
- Glassboy es **fan** de Marceline: tiene **una muñeca suya**. Simón le
  dice: «big Marcy fan, huh?».

**Visto en el tráiler oficial** ([«Adventure Time Distant Lands Trailer —
Obsidian»](https://www.dailymotion.com/video/x7xejon), 1:30, **1920×1080**,
termina con el logo de HBO Max):
- **0:16**: Marceline y la Princesa **en la cocina** (suelo turquesa,
  armarios verdes), **cada una con una taza humeante** ✅
  ([`?t=16`](https://www.dailymotion.com/video/x7xejon?t=16)).
- **0:20**: Marceline, en camiseta gris, **toca el bajo sentada** mientras
  la Princesa cocina detrás ✅ ([`?t=20`](https://www.dailymotion.com/video/x7xejon?t=20)).
- **0:36**: **flota tocando el bajo** sobre un camino de piedra hacia el
  Reino de Cristal, con **picos morados y una torre de cristal** al fondo ✅
  ([`?t=36`](https://www.dailymotion.com/video/x7xejon?t=36)).
- **0:44-1:00**: convertida en **monstruo alado de ojos rojos**, pelea;
  luego vuelve a flotar tocando entre picos morados y turquesa ✅.
- **1:08**: de pie, **bajo al hombro**, junto a la Princesa y dos figuras
  de cristal, luz cálida de atardecer ✅ ([`?t=68`](https://www.dailymotion.com/video/x7xejon?t=68)).
- **1:12**: las dos **en una motocicleta**, entrando en la ciudad de
  cristal ✅.
- **1:24**: primer plano de **Marceline asustada**, fondo oscuro
  estrellado ✅ ([`?t=84`](https://www.dailymotion.com/video/x7xejon?t=84)).

### 2.7 El estreno con que termina la serie (10×13 «Come Along With Me», latino «¡Ven conmigo!») ✅

- **≈35:55**: BMO canta «**Time Adventure**» con Jake en brazos: «You
  and I will always be back then».
- **≈36:57**: Marceline: «Oh man! **He hates music!**». La Princesa:
  «GOLB is discord. **It's the harmony!** Harmony hurts them!». BMO: «**My
  art is a weapon!**». Todo Ooo canta a la vez.
- **≈42:39**: Jake: «Music is powerful, man. It speaks to a primal pit in
  our brains».
- **≈43:04**: el **Hoyo Musical**: «A good song can really wrap people up
  in a mood, better than any words alone could. Actually, **I've been
  working on a new song myself**… Would you like to hear it?». Finn y
  Jake: «Sure!» «Yeah!». Suena el tema final.

> Es, literalmente, **un estreno musical**. La frase del Hoyo Musical
> cabe en la lámina como gancho (traducción mía: «Tengo una canción
> nueva. ¿Quieren oírla?»). **No encontré cómo se dijo en el doblaje.**

### 2.8 Marceline, contratada para tocar (1×22 «Henchman») ✅

- **≈6:35**: Finn avisa en el castillo del Duque de las Nueces de que
  llega «su ama con un ejército de no muertos»… y era **el público**.
  Marceline entra volando: «**I wrote this next song about a
  fisherman**» (esta canción la escribí sobre un pescador) y canta.
- El Duque: «You're late, Marceline! My son has been **dying to hear your
  undead music**!». Una invitada: «**Marceline is playing tonight!**»
  (¡esta noche toca Marceline!).
- **≈6:49**: «Marceline **toca el bajo**. Todo el mundo se pone a
  bailar». En este episodio los filos del bajo aún son **plateados**.

> Para la lámina: Marceline ya era **una artista con conciertos
> anunciados** desde la temporada 1. ⚠️ **Sin clip real** (buscado en
> Dailymotion: «Henchman Marceline plays bass party»); minuto estimado.

### 2.9 El opening y los créditos, vistos ✅

- **Opening doblado al latino** ([Dailymotion, «'Hora de Aventuras'
  intro», Espinof](https://www.dailymotion.com/video/x8p2dsj), 0:29,
  **1920×1080**), 10 fotogramas: laguna helada con montañas, el castillo
  del Dulce Reino con personajes, valle verde, la casa del árbol por
  dentro con Finn, Jake y un perrito caliente gigante, Jake tocándose las
  orejas, Finn y Jake corriendo por una cresta bajo nubes de tormenta, y
  el logo «ADVENTURE TIME — Created by Pendleton Ward» ✅.
- **Créditos finales en inglés** ([Dailymotion](https://www.dailymotion.com/video/x4fakxm),
  0:33, 1280×720), 12 fotogramas: **fondo verde lima plano** con abejas y
  mariposas animadas y los nombres reales del staff («Supervising
  Director Larry Leichliter», «Lead Character & Prop Designer Phil
  Rynda», «Character & Prop Designers Natasha Allegri, Tom Herpich»…);
  cierran los logos de **Frederator Studios** y **Cartoon Network
  Studios** ✅.

---

## 3 · Arte oficial y referencias visuales

> [!note] Segunda pasada: ahora sí hay imágenes vistas
> En la primera pasada las webs de imágenes estaban cerradas. En la
> segunda se bajaron y **se miraron** las de la wiki (1188, en 13 hojas),
> los *model sheets* de producción y el arte del especial «Obsidian».
> Lo que sigue sin ver lleva ⚠️.

### 3.0 Las hojas de contacto ✅

`herramientas/investigar_serie.py --wiki adventuretime` con las páginas
de Marceline, Finn, Jake, Dulce Princesa, el bajo-hacha y BMO indexó
**1188 imágenes** de la wiki en **13 hojas** de 48. Se quedan **3** en
`hojas/` (vistas). El número de cada imagen es el de la hoja; el
original, con su tamaño, está en `referencias.json`.

**`hojas/personajes_01.jpg` (1-48): arte de producción y vestuario.**
- **#1** «Stock Night» (5100×3300): Marceline caminando en 4 poses, gris,
  sin color final. Para **proporciones**.
- **#2-4**: bocetos a lápiz de Marceline murciélago («Bat Marceline
  Rough — Phil»), 3600×3000.
- **#5** el **bajo-hacha solo**, *model sheet* con las llantas del mástil
  (4104×2454). **La mejor referencia del objeto.**
- **#9-10** «New Costume #1» (4079×2421): vestido camisero azul grisáceo y
  zapatos granate, de frente y de espaldas. **Colores medidos aquí** (§16).
- **#15** grito (pose especial, ojos rojos) y **#16** a punto de llorar:
  caras oficiales para rabia y tristeza.
- **#20** traje con **sombrero de ala ancha, guantes y botas** contra el
  sol (el de «I'm Just Your Problem»).
- **#25** «S2e1 Drama bomb» (2880×1620): de noche con el bajo rojo.
- **#35** Simon y Marcy niña **en moto** (5×14). **#36** «S7e7 Marceline
  playing ax bass» (2880×1620): **de pie, en un huerto, tocando de
  verdad, un ojo guiñado**. **La mejor «con su instrumento».**
- **#43** Dulce Princesa (2880×1618), **#45** *model sheet* de Jake
  (1700×2455), **#48** *model sheet* de Finn (1467×2385).

**`hojas/personajes_02.jpg` (49-96): el bajo y la Dulce Princesa.**
- **#49** el **bajo-hacha solo sobre fondo verde** (1471×2227), en color:
  filos rojos, mástil y clavijas.
- **#51** «Marceline Presentation» (1382×2136): **cuerpo entero sobre
  blanco**, camiseta gris, vaqueros y botas rojas. **La mejor para la IA
  y para recortar la silueta.**
- **#52-63**: Marshmaline (la versión de «Fionna & Cake») y BMO
  transformándose, sobre el rosa del Dulce Reino.
- **#67-93**: la Dulce Princesa en muchos episodios (1920×1200); **#86-87**
  sentada **con una taza de té**, en su palacio rojo.
- **#94** Finn, la Princesa y Marceline **con su paraguas negro** en la
  playa («Islands»).

**`hojas/escenas_09.jpg` (385-432): la historia de Marceline y Simon.**
- **#385** Marceline presenta a sus fantasmas **en su casa rosa**
  (1920×1080); **#386** asusta a Finn y Jake en el **sofá rojo**.
- **#391-392** con la Princesa y el **sombrero de sol**; **#393**
  **cantando sobre la puerta de los círculos dorados** (3×10).
- **#396-397** tocando con el Rey Helado en la batería; **#403** con el
  **omnichord**; **#404** la **lágrima**; **#408** **la nota de Simón**
  escrita a mano (4×25).
- **#407, #409-411, #417-423**: Marcy niña con Simon (5×14, 5×29), con
  **Hambo**, el osito rojo.
- **#432** Betty, Gunter, Marceline, Finn y Jake (5×48).

Las otras 10 hojas quedan fuera del repositorio, en
`herramientas/referencias/adventure-time-hora-de-aventura/` (git las
ignora), por si hace falta más.

### 3.1 Libros de arte oficiales

- **«Adventure Time: The Art of Ooo»**, de Chris McDonnell, prólogo de
  Guillermo del Toro. Abrams, **14 de octubre de 2014**, **352 páginas**.
  Bocetos, guiones gráficos, fondos pintados y páginas de la «biblia» de
  la serie ✅ ([Amazon](https://www.amazon.com/Adventure-Time-Art-Chris-McDonnell/dp/1419704508),
  [Goodreads](https://www.goodreads.com/book/show/20701976-adventure-time)).
  Es **la mejor fuente de fondos y bocetos de Marceline** ⚠️ (no pude
  ver qué páginas trae de ella).
- **«Adventure Time: The Original Cartoon Title Cards»** (Titan Books):
  las cartelas de título, con bocetos, versiones y comentarios de Pendleton
  Ward, Pat McHale, Nick Jennings, Phil Rynda y Paul Linsley ✅
  ([Penguin Random House](https://www.penguinrandomhouse.ca/books/240090/adventure-time-the-original-cartoon-title-cards-vol-1-by-pendleton-ward/9781783292875),
  [The Mary Sue](https://www.themarysue.com/adventure-time-title-cards/)).
- Álbumes de Flickr con **todas las cartelas de título** por temporada
  ([temporada 1](https://www.flickr.com/photos/84568447@N00/albums/72157623600706180/),
  [temporada 5](https://www.flickr.com/photos/84568447@N00/albums/72157631970017303/)) ⚠️
  (no sé de quién es la cuenta; no abría).

### 3.2 Las cartelas de título (cómo se hacen) ✅

- **Phil Rynda** las diseña, **Paul Linsley** las pinta y el director de
  arte **Nick Jennings** les da la última pasada: cambia colores y añade
  un **tramado (dithering) que imita la impresión de los cómics viejos**
  ([Art of the Title](https://www.artofthetitle.com/title/adventure-time/),
  [Nerdist](https://archive.nerdist.com/exclusive-never-before-seen-art-from-adventure-time-the-original-cartoon-title-cards/)).
- **Jennings coleccionaba papel antiguo** y lo escaneaba para usarlo como
  **borde** de las cartelas ✅ (mismas fuentes).
- Influencias que citan: portadas de novela pulp y romántica,
  ilustraciones de Dungeons & Dragons, Frank Frazetta, cine de artes
  marciales de los 70 y hasta paisajes de Thomas Kinkade ✅.

> Esto importa para la lámina: el **papel viejo con tramado** es la
> textura «oficial» de la serie para poner un título.

### 3.3 Key art de los especiales

- **«Obsidian»** (Tierras lejanas): el primer póster salió en la
  Comic-Con virtual del **24 de julio de 2020**; tráiler y key art
  después, para el estreno del **19 de noviembre de 2020** ✅
  ([Bleeding Cool](https://bleedingcool.com/tv/adventure-time-distant-lands-obsidian-releases-trailer-key-art/),
  [MovieWeb](https://movieweb.com/adventure-time-distant-lands-obsidian-hbo-max/),
  [TVLine, primera imagen](https://www.tvline.com/news/adventure-time-distant-lands-obsidian-first-look-bubblegum-marceline-2904814/)).
  Marceline y la Princesa juntas: la mejor pose de pareja oficial ⚠️
  (el póster no se bajó; sí se vio el **tráiler** en 1080p, §2.6).
- **Otro key art de «Obsidian»** con el adelanto de una canción
  ([Bleeding Cool](https://bleedingcool.com/tv/adventure-time-distant-lands-previews-obsidian-song-new-key-art/)).

### 3.4 Los discos oficiales (el objeto real para #musica-nueva) ✅

Todos existen y se venden. Son la referencia perfecta para modelar en
Blender: **funda, galleta, color del vinilo, librito**.

| Disco | Qué es | Detalles para modelar | Fuentes |
|---|---|---|---|
| **Adventure Time: The Complete Series Soundtrack** (Mondo, 2019) | **Caja** con **3 LP de 12"** (amarillo, azul oscuro y rosa), **1 LP de 10"**, **1 CD** y **1 casete** con 15 maquetas | Arte de **JJ Harrison**. Dentro de la caja: **Prismo y el Búho Cósmico en la Sala del Tiempo**; en el librito, Finn y Jake fuera de esa sala. Producida por el compositor **Tim Kiefer**. Más de 200 canciones | [Mondo (producto)](https://mondoshop.com/products/adventure-time-the-complete-series-box-set), [Mondo (blog)](https://mondoshop.com/blogs/news/music-weekly-adventure-time-the-complete-series-soundtrack-box-set), [Discogs](https://www.discogs.com/release/13812325-Adventure-Time-Adventure-Time-The-Complete-Series-Soundtrack) |
| **Come Along With Me** (Mondo, 2019) | LP de la música del final | **180 g**, vinilo partido **azul y amarillo** («Finn y Jake»), **carpeta desplegable** y **librito de 8 páginas**. Arte de **Jesse Balmer**. Trae «Island Song» completa de Ashley Eriksson y una canción nueva de Rebecca Sugar | [Mondo](https://mondoshop.com/products/adventure-time-come-along-with-me-original-soundtrack-lp), [Turntable Lab](https://www.turntablelab.com/products/adventure-time-come-along-with-me-180g-vinyl-lp), [Mondo: final + pins](https://mondoshop.com/blogs/news/adventure-time-final-episode-soundtrack-enamel-pins) |
| **Distant Lands – Obsidian** (iam8bit / WaterTower) | **Doble LP**, 32 canciones | Vinilo **«Glassboy Blue»**. Arte de **Maya Petersen**. **La letra de «Monster» va grabada en la cara 4** del disco, diseñada por Half Shy | [iam8bit](https://www.iam8bit.com/products/adventure-time-distant-lands-obsidian-original-soundtrack-2xlp), [Plastic Stone](https://plasticstone.net/products/amanda-jones-adventure-time-distant-lands-obsidian-original-soundtrack-2xlp-glassboy-blue-vinyl), [WaterTower](https://www.watertower-music.com/release/adventure-time-distant-lands-obsidian-original-soundtrack-deluxe-edition/) |
| **BMO's Mixtape (Gilligan Moss Mix)** (iam8bit) | LP de **11 remezclas** («Robot Cowboy», «Bacon Pancakes», «Eternity With You»…) | Vinilo **«Groovy Cosmic Splatter»** (salpicado), funda con **barniz brillante en zonas**. Arte nuevo de **Jesse Balmer**, **con BMO** | [iam8bit](https://www.iam8bit.com/products/adventure-time-distant-lands-bmos-mixtape-gilligan-moss-mix-vinyl-soundtrack), [Gamers Heroes](https://www.gamersheroes.com/gaming-news/iam8bit-adventure-time-distant-lands-vinyl-and-cd-soundtracks-pre-orders-live/) |
| **Monster** (single) | **Single digital** con **King Princess** | Portada: sin ver ⚠️ | [Spotify](https://open.spotify.com/album/1F9JG1CnaKLmYqsDHdOxey), [Bleeding Cool](https://bleedingcool.com/tv/adventure-time-distant-lands-obsidian-king-princess-sings-monster/) |
| **Marceline Canta: Timeless Songs (Versión en español)** | **Disco oficial en español** con **10 canciones de Marceline** | Hay también **versión en portugués**. Fecha **25-oct-2019** ✅ (la wiki dice 2019 y MusicBrainz da el día exacto; el número de Apple Music apuntaba a 2020) | [MusicBrainz](https://musicbrainz.org/release-group/1f39e3d6-9a3b-4838-bae0-3e59b37e69eb), [Spotify](https://open.spotify.com/album/6x28Z0ItbmOHSpPUtExumt), [Deezer](https://www.deezer.com/us/album/153622342), [Hora de Aventura Wiki](https://horadeaventura.fandom.com/es/wiki/Marceline_Canta:_Timeless_Songs), [Apple Music](https://music.apple.com/us/album/marceline-canta-timeless-songs/1515397280) |

**Lista del disco en español**, con la **duración real** de cada pista
(MusicBrainz) y el episodio entre paréntesis (Hora de Aventura Wiki) ✅:
1. ¿Qué soy para ti? — 2:41 («Lo que estaba perdido»)
2. Soy tu problema — 2:00 («Lo que estaba perdido»)
3. **Niño malvado** — 1:54 («Muchachito malo»). La wiki la llamaba
   «Pequeña mujer»; MusicBrainz, «Niño malvado» ⚠️ (no coinciden).
4. Recordándote — 2:19 («Te recuerdo»)
5. Ya no lo puedo soportar / Hay un fuego dentro de mí — 1:29 («Incendio»)
6. **Papi, te comiste mis papas** — 1:43 («Llegó de la Nocheósfera»; la
   wiki la llamaba «Canción de las papas»)
7. Todo se queda — 2:26 («Todo se queda / La nube oscura»)
8. Cadena alimenticia — 1:32 («Cadena alimenticia»)
9. Siempre entonces se podrá volver — 2:10 («¡Ven conmigo!»)
10. **Acompáñame** — 1:49 («¡Ven conmigo!»): es «**Come Along With Me**»,
    el tema de cierre de la serie.

> **Idea fuerte**: los tres formatos del canal existen en la franquicia.
> **Disco** = el LP de 12". **Single** = «Monster». **EP** = el 10" de
> la caja de Mondo. Y **el casete** de la misma caja sirve de guiño.
> «¿Esto es un disco, un single o un EP?» se explica con objetos que un
> fan reconoce.

### 3.5 El bajo-hacha (el objeto del plan) ✅

- **Qué es**: un **hacha de guerra de doble filo**, herencia de la
  familia Abadeer, que Marceline convirtió en **bajo de cuatro cuerdas**
  ✅ (transcripción de 2×01; [Adventure Time Wiki: Ax Bass](https://adventuretime.fandom.com/wiki/Ax_Bass),
  [Marceline's instruments](https://adventuretime.fandom.com/wiki/Marceline's_instruments)).
- **Cómo es** (según la wiki, por el resumen de búsqueda) ✅: pala con
  **dos clavijas a cada lado**, **mástil tallado con unos 20 trastes**,
  **dos pastillas de bobina simple**, **puente fijo**, perillas de
  **volumen y tono** y botones para la correa.
- **Color de los filos**: en «Henchman» (1×22) eran **plateados**; desde
  «It Came from the Nightosphere» (2×01) son **rojos** ✅. Para la
  lámina, **rojos**: es el que todo el mundo recuerda.
- **Lo que le pasa**: su padre se lo roba y **lo usa de broche** (2×01);
  en «Ocarina» (6×12) aparece un **bajo nuevo de cuatro mástiles** ✅
  (transcripción: «plays her new four-necked bass»); en «Obsidian» se lo
  **rompen** (≈33:37). En «Betty» (5×48) Finn le pregunta «¿por qué
  sostienes el bajo tan alto?» ✅.
- **Hay réplicas físicas tocables hechas por fans** (DeviantArt:
  [kazesamurai1000](https://kazesamurai1000.deviantart.com/art/Working-Playable-Marceline-s-Axe-Bass-525394489),
  [BeastlyBrains](https://www.deviantart.com/beastlybrains/art/Marceline-s-axe-bass-323235952))
  y un **objeto de Steam Workshop** ([Ax Bass](https://steamcommunity.com/sharedfiles/filedetails/?id=309894021)).
  Sirven para ver **el bajo con luz real**.

### 3.5b El bajo-hacha en arte oficial (visto) ✅

- ***Model sheet* «axbass withrims»**: el bajo solo, con las llantas del
  mástil marcadas ([4104×2454](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/5/58/Modelsheet_axbass_withrims.png)),
  hoja 1 **#5**. Sin color (gris de producción).
- **En color, sobre fondo verde** ([«Qr.png», 1471×2227](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/e/e5/Qr.png)),
  hoja 2 **#49**.
- **Tocándolo de pie**, en un huerto, luz de tarde
  ([«S7e7 Marceline playing ax bass», 2880×1620](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/3/33/S7e7_Marceline_playing_ax_bass.png)),
  hoja 1 **#36**.
- Filos en color de escena: rojo saturado entre `#9E1B1E` y `#C22B2F` ⚠️
  (no se aisló un píxel limpio por el brillo de la escena).

### 3.6 Cómics oficiales

- **«Marceline and the Scream Queens»** (BOOM! Studios, **6 números,
  julio a diciembre de 2012**), de **Meredith Gran**: **la banda de rock
  de Marceline se va de gira por Ooo** y la Dulce Princesa se une ✅
  ([Bleeding Cool](https://bleedingcool.com/2012/04/15/boom-spins-off-adventure-time-comic-marceline-scream-queens),
  [ComicsAlliance](https://comicsalliance.com/adventure-time-marceline-and-the-scream-queens-boom-studios/),
  [Autostraddle](https://www.autostraddle.com/marceline-and-the-scream-queens-is-punk-rock-and-precious-227669/)).
  Portadas alternativas del n.º 1 de **JAB, Chynna Clugston, Lucy
  Knisley, Ming Doyle y Colleen Coover** ✅. Es **la mejor fuente de
  Marceline en gira, con banda y en escenario** ⚠️ (no vi las portadas).
- En España los cómics se editaron como «Hora de Aventuras», con tomos
  como la «**Edición Matemática**» ✅ ([Amazon.es](https://www.amazon.es/HORA-AVENTURAS-EDICION-MATEMATICA-COLECCION/dp/8467918675)).
- El rotulista de los cómics de BOOM! es **Steve Wands** ✅
  ([Adventure Time Wiki](https://adventuretime.fandom.com/wiki/Steve_Wands),
  [League of Comic Geeks, n.º 41](https://leagueofcomicgeeks.com/comic/3374523/adventure-time-41)).

### 3.7 Arte de producción, visto (segunda pasada) ✅

Cada *model sheet* trae el sello **© Cartoon Network Studios** y una
ficha con episodio e id.
- **«Marceline - New Costume #1»**, ep. **057**, id `C057s011_472`,
  2011: de frente y de espaldas, **vestido camisero azul grisáceo** y
  **zapatos granate** ([4079×2421](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/3/34/Modelsheet_Marceline_-_New_Costume_-1.png)).
  Es el que se usó para medir su ropa y su piel (§16).
- **«Marceline Stock Night»**: caminata en 4 poses, gris
  ([5100×3300](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/0/0b/Modelsheet_marceline_stocknight.jpg)). Para
  proporciones, no para color.
- **«Marceline Bat» 1 y 2**: bocetos a lápiz de su forma de murciélago,
  firmados «Bat Marceline Rough — Phil»
  ([3600×3000](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/9/9b/Modelsheet-MarcelineBat1.jpg)).
- **«Original Finn»** y **«Jakesalad»**: *model sheets* a color de Finn y
  Jake ([1467×2385](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/f/f3/Original_Finn.png),
  [1700×2455](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/3/3b/Jakesalad.png)).
- **«Modelsheet princessbubblegumtiedup»** (1478×1494) y los **bocetos de
  vestuario de Marceline para el final**, de **Tom Herpich** (1280×1673).
- **Concept art de «Obsidian»** (galería de 15 en la wiki, subida el
  30-ene-2021): **#9** bocetos a lápiz rojo de los «Shards», la gente del
  Reino de Cristal, con capucha puntiaguda y manoplas
  ([1002×810](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/9/9e/Obsidian-concept-9.png)); **#1** la
  montaña-criatura de tinta negra con dientes y garras
  ([1280×989](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/3/38/Obsidian-concept-1.png)).
- **Logo oficial** de la serie ([1069×519](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/thumb/b/bd/Adventure_Time_logo.png)).

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D con licencia (Sketchfab, leída en su API) ✅

En la primera pasada Sketchfab no abría y casi todo iba «sin ver». En la
segunda, **la licencia se leyó en la API de Sketchfab**
(`api.sketchfab.com/v3/search`), que es quien la certifica.

**El bajo-hacha**

| Modelo | Autor | Licencia (API) | Nota |
|---|---|---|---|
| [Marceline's Ax Bass](https://sketchfab.com/3d-models/none-417178d709774642b0d5b5a02181caa2) | **Haxis** | **CC BY** ✅ | **El más libre**: deja uso comercial con crédito. ♥ 61. Crédito: «Marceline's Ax Bass» by Haxis, CC BY |
| [Marceline's Ax Bass](https://sketchfab.com/3d-models/none-2224d0a363a24ba883614f209761454c) | **Yogensia** | **CC BY-NC-SA 4.0** ✅ | sin uso comercial; vale para el Discord si no se vende nada |
| [Marceline's Axe/Guitar](https://sketchfab.com/3d-models/none-412c96ee288a4bcdb01a7433dff90fa7) | ScoobSter_ | CC BY ✅ | |
| [Marceline`s Bass guitar](https://sketchfab.com/3d-models/none-bac567bac05b46039f0e5510bf0c3062) | coffe0wolf | CC BY-NC ✅ | |
| [Marceline's Axe Bass](https://sketchfab.com/3d-models/none-477b56a2db134065947b2c931c52b3aa) | denizin | CC BY-NC ✅ | textura iridiscente (se aleja del estilo plano) |
| [Low Poly Marceline's Ax Bass](https://sketchfab.com/3d-models/none-101d7036f35b411295e6a500c86e952b) | cuxilrodas | **«Free Standard»** ⚠️ | **Corrección**: no es Creative Commons, es la licencia por defecto de Sketchfab (se baja gratis, sin permiso claro para reusar). Tiene las texturas más «de dibujo animado»: **pedir permiso al autor** antes de usarla |
| [Marceline axe bass guitar](https://sketchfab.com/3d-models/marceline-axe-bass-guitar-adventure-time-9bc622d77287423391e4e5451c05ca77) · [Marceline Bass Axe](https://sketchfab.com/3d-models/marceline-bass-axe-b6f6f74eb92f4bbfbcbd2d4d01f3b8df) · [(SGP) Bass Axe](https://sketchfab.com/3d-models/sgp-adventure-time-marcelines-bass-axe-6e72178681c44722a0cb5226deff7e8e) · [Bass Guitar](https://sketchfab.com/3d-models/marcelines-bass-guitar-4d89b7121de54b4e9410f4472fa1bab6) · [guitar bass](https://sketchfab.com/3d-models/marcelines-guitar-bass-c003bed4b97244d1b705626dd5bb5e69) · [Axe Bass](https://sketchfab.com/3d-models/marcelines-axe-bass-e111ddfd74f9426dab13a70fce789d44) | Z3bbz, Froes, TravisEvashkevich, deadlygeek, Hoho, 10958533 | ⚠️ | la API los da como descargables pero **sin campo de licencia** en la consulta: mirar la ficha uno a uno |
| [Axe bass – Marceline](https://www.artstation.com/artwork/BmZxOm) (ArtStation) | Victor Cavalcante Vk | sólo para mirar | render 3D |

**Personajes y sitios**

| Modelo | Autor | Licencia (API) | Para qué |
|---|---|---|---|
| [Marceline the vampire queen](https://sketchfab.com/3d-models/none-f520806111dc454ba3455947e51b04de) | coffe0wolf | CC BY ✅ | **maniquí de proporciones** de Marceline entera |
| [Finn - (Adventure Time)](https://sketchfab.com/3d-models/finn-adventure-time-309e158598764644a5c6068e0cfdc898) | Agu.3D | CC BY ✅ | Finn, 64 992 caras |
| [Finn Adventure Time](https://sketchfab.com/3d-models/none-19255b56148247eaa213bff7974304a4) | Nico Caraballo (theniloart) | CC BY ✅ | Finn ligero, 1 548 caras, para pruebas |
| [Finn - Adventure Time](https://sketchfab.com/3d-models/none-b3c5b1d5e4274eb0ba7f42ea00ed0ad2) · [Finn's Demon Blood Sword](https://sketchfab.com/3d-models/none-7f919633863140a49e6d51a8f0d87aab) | RenataDiFlorio · Haxis | CC BY ✅ | Finn y su espada |
| [Jake](https://sketchfab.com/3d-models/jake-6326c036c6f14d09bf0708ca4289d699) · [Jake el Perro Toon](https://sketchfab.com/3d-models/none-6fd2e3f4ef614842add5cec885cec2f2) | Mormont · Luis Angel | CC BY ✅ | Jake |
| [Bmo - Adventure Time](https://sketchfab.com/3d-models/none-ffeb3e9ab97e4e3dbed4ddc0650d8b9b) · [Adventure Time BMO](https://sketchfab.com/3d-models/none-57a8b359d2ad41a3bacc41facfc77531) · [BMO / Hora de Aventura](https://sketchfab.com/3d-models/none-c746c7382fe748759b7f11eda14b8b9a) | featbear · ezgibakim · Jzero_95 | CC BY ✅ | BMO (concepto C) |
| **[The Treehouse](https://sketchfab.com/3d-models/none-0131dc63d8894892b0c87dc852f23984)** · [Finn and Jake's Treehouse](https://sketchfab.com/3d-models/none-a390d3c9873c4c219959d0b930aabe52) | gleksono | **CC BY** ✅ | **la casa del árbol entera**, el sitio del concepto C |

> Recomendación: el bajo de **Haxis** (CC BY) para la lámina; el de
> **Yogensia** si no se vende nada. Marceline de **coffe0wolf** como
> maniquí. **Ojo**: un render 3D realista **no encaja** junto a un
> personaje plano; hay que darle material plano con contorno (§A).

### 4.2 Fan art 2D (mirar, nunca pegar)

- [Marceline playing bass](https://www.deviantart.com/ajscanvas/art/Marceline-playing-bass-292387926), AJsCanvas: **redibuja la pose de «What Was Missing»** (3×10). Útil para ver la postura al tocar.
- [Marceline and her ax bass](https://www.deviantart.com/queenjazmine/art/Marceline-and-her-ax-bass-419453602), queenjazmine.
- [Marceline Plays the Bass](https://www.deviantart.com/disneyponyfan/art/Marceline-Plays-the-Bass-924284143), Disneyponyfan.
- [Marceline Bass](https://www.deviantart.com/minty-kitty-art/art/Marceline-Bass-510877467), Minty-Kitty-Art (se vendió como lámina).
- Diseños del bajo solo: [DavaDs](https://www.deviantart.com/davads/art/Marceline-s-Axe-Bass-382362695), [TheBreakfastUnicorn](https://www.deviantart.com/thebreakfastunicorn/art/Marcelines-axe-bass-3-304673345).
- Fondos de fans con autor y tamaño (Wallhaven): ver §17.
- **Fotos con licencia libre** (Openverse): disfraces caseros de
  Halloween de «Violently Japy» (Flickr, CC BY-NC 2.0) y 8 fotos
  tituladas «Marceline» de **Peu Pundik Fotografia** (Flickr, **CC BY-SA
  2.0**, 683×1024, p. ej.
  [esta](https://live.staticflickr.com/5520/10413902646_377f68940e_b.jpg))
  ⚠️ (las trajo el recolector; nadie las miró una a una).
  Para cosplay con materiales de verdad, ver §F.

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios que sirven

- **La cueva de Marceline** ✅ ([Adventure Time Wiki](https://adventuretime.fandom.com/wiki/Marceline%27s_cave)):
  oscura y húmeda, con **estalactitas y estalagmitas**. Una entrada está
  **bajo una autopista vieja, de antes de la Guerra de los Champiñones**,
  con una roca que **parece una cara de demonio**.
- **La casa de Marceline** ✅ ([Adventure Time Wiki](https://adventuretime.fandom.com/wiki/Marceline's_house)):
  dentro de la cueva, con **un porche grande sobre una laguna**. Es
  **rosa con tejado marrón**, **valla blanca**, **una canasta de
  baloncesto** y **tres cúpulas**: parece una casa de las afueras, algo
  raro en Ooo. Dentro: un **sofá incómodo** (ella flota, no lo usa) con
  **velas en la pared** a los dos lados. En «Obsidian» vive allí con la
  Dulce Princesa y hay **fotos de las dos** en las paredes.
  - Detalles de las transcripciones ✅: **un contestador automático**
    (3×21), **su cuaderno**, **equipo de grabación** en el cuarto, una
    **escalera al dormitorio**, **la nevera** (4×25), **ventana** por
    donde entra el Rey Helado.
- **El Anfiteatro Fantasma** del **cementerio de Hamburger Hills**
  (10×07): escenario con **niebla** y público de fantasmas ✅.
- **La casa del árbol** de Finn y Jake: donde vive BMO ✅ (serie entera). Hay
  **modelo 3D entero con licencia CC BY** (gleksono, §4.1).
- **El Reino de Cristal** («Obsidian»): escenario con telones, un
  **horno** donde está encerrado el dragón y un pueblo de cristal ✅.
  En el tráiler (visto): **camino de piedra** hacia **picos morados y
  turquesa** y **una torre de cristal**; una **ciudad de cristal** a la
  que llegan en moto ✅.
- **La puerta del Señor de las Puertas** (3×10): **arco de piedra con
  botones circulares dorados** (visto en el clip oficial, y hoja 9
  **#393**) ✅.
- **La cocina de la casa** («Obsidian»): suelo turquesa, armarios verdes,
  dos tazas humeantes (visto, 0:16) ✅. Por dentro la casa es **rosa**
  (dos clips) ✅; fotogramas de la wiki: hoja 9 **#385**, **#386**, **#400**.

### 5.2 Luz (vista en vídeo en la segunda pasada) ✅

- **Casa de Marceline por dentro**: luz **plana y cálida**, rebotada en
  las paredes rosa, **sin sombras marcadas** ✅ (visto en «Fry Song» y en
  la cocina del tráiler de «Obsidian»: dos clips distintos).
- **La puerta del Señor de las Puertas** («I'm Just Your Problem»):
  **tarde con cielo despejado**, nubes blancas; cae la noche con fondo
  rojizo al final ✅. **Corrección**: no es la cueva; la primera pasada
  mezclaba las dos localizaciones.
- **Reino de Cristal** («Obsidian»): **violeta y magenta frío** con
  acentos cian, aire nocturno y mágico; el camino está **pintado con
  degradado**, más pictórico que el resto de la serie ✅ (3 fotogramas,
  `estilo.py`).
- **Créditos finales**: **verde lima plano**, sin degradado, con abejas y
  mariposas sueltas ✅.
- **La cueva** (luz fría azul violeta con velas) y **el escenario del
  cementerio** (noche, niebla y foco): **siguen de memoria** ⚠️; no hubo
  clip real de ninguno de los dos.
- Casa del árbol: luz de tarde dorada por ventanas redondas ⚠️ (de
  memoria; el opening la muestra por dentro, sin medir).

### 5.3 Paleta medida ✅ (con Pillow y `estilo.py`; dice de dónde sale cada una)

**Casa de Marceline** («Fry Song» 0:16 y tráiler de «Obsidian» 0:16)

| Qué | Hex | De dónde |
|---|---|---|
| Pared rosa | **`#F8AEC5`** | «Fry Song» 0:16, 37 % del cuadro |
| Techo, pared clara | `#FBE0E8` | «Fry Song» 0:16 |
| Sillón rojo | `#D94344` | «Fry Song» 0:00, píxel puntual |
| Zócalo y marco de ventana gris azulado | `#7A8A96` ⚠️ | a ojo en el fotograma; el agrupado automático no lo separó |
| Cocina: rojo vino de fondo | `#4D252C` | «Obsidian» 0:16 |
| Cocina: turquesa de los aparatos | `#5B8890` | «Obsidian» 0:16 |
| Cocina: rosa de la pared en sombra | `#B04E5E` | «Obsidian» 0:16 |

**Reino de Cristal** (tráiler de «Obsidian», 0:00, 0:16, 0:44, 1:00)

| Qué | Hex |
|---|---|
| Camino y cielo violeta oscuro (0:44, 36 %) | **`#422D6B`** |
| Violeta medio | `#6A53A0` |
| Rosa pálido de la luz | `#E7D1D9` |
| Magenta de acento | `#8F3F6E` |
| Cian pálido del cristal (0:00, 53 %) | **`#E1F7F9`** |
| Azul cielo claro | `#BDE0F5` |
| Picos de cristal, violeta | `#9055C3` y `#D3A0E8` |

**Cielo de «I'm Just Your Problem»** (0:52): `#EFEFFF` y `#A5B9F6`.

**Personajes** (el detalle, prenda por prenda, en §16)

| Qué | Hex medido | De dónde |
|---|---|---|
| Piel de Marceline, **color plano** | **`#D8E7E7`** (blanco menta muy pálido) | *model sheet* oficial ep. 057 y «Drama bomb», dos veces ✅ |
| Piel de Marceline **en escena con sombra** | `#657471` | fotograma 0:52 de «I'm Just Your Problem», 12 puntos ✅ |
| Pelo de Marceline, plano | `#000000` | *model sheet* y captura ✅ |
| Pelo en escena | `#150209` y `#24080E` | «I'm Just Your Problem» 0:52 y «Fry Song» 0:16 ✅ |
| Finn: camiseta / mochila / piel | `#018BCB` / `#7BBB59` / `#FDE5DA` | *model sheet* «Original Finn» ✅ |
| Jake | `#FEB925` | *model sheet* «Jakesalad», 40 % de la imagen ✅ |
| Dulce Princesa: rosa y rosa en luz | `#ED8ACE` y `#F3BBFB` | «Princess Bubblegum Duct Tape» ✅ |
| BMO: carcasa turquesa | `#6CC3B3` ⚠️ | de memoria: el rosa del fondo tapaba la muestra |
| Papel viejo de las cartelas | `#E8DCBC` ⚠️ | de memoria |

> **Corrección importante (piel de Marceline)**: la primera pasada puso
> `#A9B8C2`, «gris azulado», de memoria. **Medido, el color plano es
> `#D8E7E7`**: casi blanco, con un toque menta. El `#657471` sólo sale
> cuando la escena la oscurece; **para dibujarla se usa `#D8E7E7`** y se
> sombrea encima. Y el pelo es **negro puro**, no «negro azulado»
> (`#1C1B2B` era de memoria).
>
> Quedan **de memoria** ⚠️ (no se midieron): vaqueros `#3E5C9A`, madera
> del mástil `#6B4226`, casa por fuera `#E7A1B0` con tejado `#6E4A36`,
> fondo de la cueva `#2A2440`, pantalón de Finn `#1F4E9B`, pelo chicle
> de la Princesa `#E0569A` y pantalla de BMO `#CFEFD9`. El vinilo
> «Glassboy Blue», sin ver.

### 5.4 Texturas reales equivalentes (CC0, sin crédito obligatorio)

- Roca de la cueva: [Rock Wall 05 (Poly Haven, 8K)](https://polyhaven.com/a/rock_wall_05) y [Rock Wall 13 (16K)](https://polyhaven.com/a/rock_wall_13) ✅ CC0.
- Luz de cueva real para Blender: [Cave Wall HDRI (Poly Haven)](https://polyhaven.com/a/cave_wall) ✅ CC0 (cueva con río y vegetación, luz suave).
- Cartón de la funda del disco, papel de la nota, madera del mástil,
  cuero de las botas y tela: **ambientCG** (CC0), nombres leídos en su
  API ✅: papel **Paper001-006**, cartón **Cardboard001-004**, madera
  **Wood092, 094, 095**, cuero **Leather026, 030, 037, 038**, tela
  **Fabric081C, 061, 066** ([ambientCG](https://ambientcg.com/list?type=Material&q=paper)).
- **Papel viejo de las cartelas**: escanear papel real amarillento
  (como hacía Jennings) o una textura de papel de ambientCG.

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

- **El logo** «Adventure Time» **no es una fuente**: es un rótulo
  dibujado a mano, de letras **gorditas, redondas y un poco
  temblorosas**, con proporciones desiguales ✅
  ([madegooddesigns](https://madegooddesigns.com/adventure-time-font/),
  [BetterStudio](https://betterstudio.com/fonts/adventure-time-font/)).
- Hay una **fuente de fans, «Adventure Time»**, que imita el logo
  ([dafont](https://www.dafont.com/adventure-time.font); también en
  [Font Meme](https://fontmeme.com/fonts/adventure-time-font/) y
  [font.download](https://font.download/font/adventure-time-logo)).
  **En la segunda pasada se bajó y se abrió con fontTools** ✅: tiene
  dibujadas á é í ó ú ñ ¿ ¡ ü, **pero sólo en la tabla Mac Roman**; **no
  tiene tabla Unicode de Windows** (sólo una «Symbol» en 0xF000+). En
  Photoshop sobre Windows, al teclear ñ o ¿ **lo más probable es que no
  salga la letra**. **Úsala sólo para «Adventure Time» en inglés**, nunca
  para texto en español.
- **Las cartelas de título**: cada una **rotulada a mano** por el pintor,
  distinta en cada episodio, sobre papel viejo ✅ (ver §3.2).
- **Los cómics de BOOM!**: globos con letra de cómic; el rotulista es
  **Steve Wands** ✅ ([Adventure Time Wiki](https://adventuretime.fandom.com/wiki/Steve_Wands),
  [League of Comic Geeks](https://leagueofcomicgeeks.com/comic/3374523/adventure-time-41)).
  Cómo es su letra, sin ver una página ⚠️.
- **Los créditos finales** (vistos, §2.9): letras claras sobre verde lima;
  la fuente exacta no se identificó ⚠️.
- **El menú de «Card Wars»** (visto, §7.3): botón «BATTLE!» con **letra
  blanca gruesa de cartel**, del estilo de Chewy o Luckiest Guy.

### 6.2 Letras libres comprobadas por mí

Bajadas de [google/fonts](https://github.com/google/fonts) y revisadas
con fontTools: **todas traen á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü** ✅.

| Uso en la lámina | Letra | Por qué | Licencia |
|---|---|---|---|
| Título «Música nueva» (como el logo) | **Chewy** | la más parecida al logo: gordita, redonda, de dibujo animado | Apache 2.0 |
| Título, alternativa | **Luckiest Guy** | más pesada, de cartel | Apache 2.0 |
| Rótulos bonitos y redondos | **Baloo 2**, **Fredoka**, **Sniglet ExtraBold** | redondas y amables, como las letras de los carteles de Ooo | OFL |
| Letra de Marceline (cuaderno, lista de canciones) | **Rock Salt** | rotulador rápido, punk | Apache 2.0 |
| Letra de Marceline, más legible | **Permanent Marker** o **Caveat Brush** | rotulador grueso | Apache 2.0 / OFL |
| Nota de Finn (lápiz, letra de niño) | **Gochi Hand**, **Patrick Hand** o **Short Stack** | letra de mano sencilla | OFL |
| Texto de relleno legible | **Mali** (SemiBold) | redonda, de mano, muy clara en el móvil | OFL |
| Pantalla de BMO | **VT323** o **Press Start 2P** | píxel, de consola vieja | OFL |
| Guiño «de vampira» (sólo una palabra) | **Creepster** o **Eater** | letra que gotea | OFL |
| Cartel de concierto punk | **Bungee** o **Rubik Doodle Shadow** | bloque, de póster | OFL |

Segunda comprobación (texto, 25-sep): **VT323, Press Start 2P, Creepster,
Eater, Rubik Doodle Shadow y Bungee** se volvieron a bajar (el `.woff2`
de Fontsource) y a abrir con fontTools: las seis traen todo ✅.
**Ojo al bajar de Fontsource**: hay que coger el subconjunto **«latin»**,
no «latin-ext». Las tildes españolas están en «latin»; con «latin-ext»
faltaban las 15 letras (comprobado con VT323).

**Una letra para cada uso** (propuesta con las letras de arriba):

| Uso | Letra |
|---|---|
| Logo o título | Chewy (o la fuente de fans, sólo «Adventure Time» en inglés) |
| Texto normal que «dice» un personaje | Mali SemiBold, o la letra de mano de quien escribe |
| Grito | Luckiest Guy en mayúsculas |
| Pensamiento o nota íntima de Marceline | Rock Salt o Caveat Brush |
| Onomatopeya | Bungee; la serie casi no las rotula en pantalla (es animación americana), sólo los cómics ⚠️ |
| Cartel del mundo (concierto, tienda) | Bungee o Rubik Doodle Shadow |
| Interfaz de juego y pantalla de BMO | VT323 o Press Start 2P |
| Subtítulos o créditos | Mali; la de los créditos reales no se identificó ⚠️ |

> **No** usar Comic Sans ni fuentes «de anime». **No** usar la fuente
> de fans del logo para frases largas ni en español.

---

## 7 · Cómo hablan en pantalla (el cuadro de diálogo)

### 7.1 Lo que la serie pone en pantalla

**Hora de aventura no usa globos.** Es animación: la gente habla y ya.
Cuando **aparece texto**, sale en **objetos**:

1. **Notas en papel escritas a mano** ✅
   - La nota de Finn en «Marceline's Closet» (3×21, ≈5:00), **a lápiz**,
     apoyada en la espalda de Jake: «MARCY, PLEASE COME TO THE
     TREEHOUSE—IT'S AN AMERGENCY! Love, FINN + JAKE». Luego la **dobla en
     avión**.
   - **Las notas de Simón** que Marceline canta en «I Remember You»
     (4×25, ≈8:49): papeles viejos con fotos. **La letra de la canción
     sale de las notas**.
2. **El cuaderno de Marceline** ✅: lo abre para cantar la «Canción del
   diario» (3×21, ≈6:36). Y su álbum sale de **quinientos años de
   diario**.
3. **Las cartelas de título** ✅: ilustración pintada con el título
   rotulado a mano, **papel viejo escaneado de borde** y **tramado de
   cómic** (§3.2). Es lo más parecido a una «caja de texto oficial».
4. **La pantalla de BMO**: su cara es una pantalla. Está diseñado como
   **parodia de las consolas portátiles de Nintendo** tipo Game Boy ✅
   (dos fuentes: un mod real que convierte un Game Boy Color en BMO,
   [Instructables](https://www.instructables.com/Adventure-Times-BMO-Roommate-GBC-Mod/),
   y la web interactiva de Active Theory para «Tierras lejanas: BMO», que
   usa su cara como menú, [Medium](https://medium.com/active-theory/adventure-time-distant-lands-bmo-5997687372b7)).
   Qué texto sale en su pantalla dentro de un episodio: sin fotograma ⚠️.
   En una ficha de DVD su «edad» es **«VER. 2600»** y su especie **«110
   VOLT-60 HERTZ SYSTEM»**, un guiño a la Atari 2600 ✅ (§C).
5. **Los discos** ✅: la **letra de «Monster» va grabada en el vinilo**
   de «Obsidian» (§3.4). Un disco oficial usa el propio objeto para
   poner texto.

### 7.2 Cómo se traduce a una lámina fija

- **Nada de burbuja blanca.** El texto va **escrito en algo**:
  - la **funda o la galleta de un disco**,
  - **la hoja de letras** de Marceline (papel de cuaderno, rotulador),
  - **una nota a lápiz** de Finn pegada con cinta,
  - **la pantalla de BMO**,
  - **una cartela** con papel viejo y tramado, para el título.
- Si hace falta que un personaje «diga» algo, que lo **diga en un papel
  que sostiene** o en **una hoja pegada a su lado**, con su letra (ver
  §6.2).
- En los cómics sí hay globos (BOOM!), redondos y de línea negra fina
  ⚠️. Si al final se usa un globo, que sea **de cómic de BOOM!**, con
  cola curva y letra de mano, **nunca** una burbuja blanca lisa genérica.

### 7.3 En los videojuegos (a medias ⚠️)

- Hay muchos: **«Hey Ice King! Why'd You Steal Our Garbage?!!»**
  (WayForward, DS y 3DS, 2012; Pendleton Ward ayudó con la historia),
  **«The Secret of the Nameless Kingdom»** (2014), **«Pirates of the
  Enchiridion»** (2018) ✅
  ([Gaming Nexus](https://www.gamingnexus.com/Article/Adventure-Time-Hey-Ice-King!--Whyd-you-steal-our-garbage!!/Item3804.aspx),
  [Destructoid](https://www.destructoid.com/reviews/review-adventure-time-pirates-of-the-enchiridion/),
  [IMDb](https://www.imdb.com/title/tt9863808/)).
- **«Hey Ice King!» (DS), visto** ✅: la hoja de *sprites* «Mugshots»
  ([Spriters Resource](https://www.spriters-resource.com/ds_dsi/adventuretimehicwysog/asset/54668/),
  759×673) trae **retratos de cuerpo entero, simplificados, de unos 28
  personajes** (Finn, Jake, BMO, Dulce Princesa, Flama Princesa, Rey
  Helado, Marceline, Lady Arcoíris, Gunter…), hechos para ir **junto a la
  caja de texto** del diálogo. La caja en sí, sin captura ⚠️.
- **«Card Wars» (móvil, 2014-2019), visto** ✅: captura del menú en
  2560×1440 ([imagen](https://i.imgur.com/cXUolY0.jpg), del puerto a PC
  archivado en [GitHub](https://github.com/shishkabob27/CardWars)):
  **marcos metálicos biselados azul grisáceo**, barra de vida y XP con
  retrato arriba a la izquierda, monedas y gemas arriba a la derecha,
  tapete de batalla **hexagonal** de madera y piedra, **botón rojo
  redondeado «BATTLE!»** con letra blanca gruesa.
- **No encontré la caja de diálogo** de «The Secret of the Nameless
  Kingdom» ni de «Pirates of the Enchiridion» ⚠️ (la API de Steam dio
  `success:false` para 298890 y 353200; TrueAchievements y Steam
  Community no abrieron). Más juegos en §13.

### 7.4 Qué NO hacer con el texto

- Burbuja blanca lisa con cola recta.
- Letra de ordenador perfecta para lo que «escribe» un personaje: aquí
  todo está **hecho a mano**.
- Mayúsculas de anime o efectos de «manga»: esto es **dibujo animado
  americano**.
- Nombres de España («Hora de Aventuras», con **s**): el servidor es
  latino, se dice **Hora de aventura** ✅ (en España el título lleva «s»:
  [wiki de España](https://adventuretimespain.fandom.com/es/wiki/Tema_de_Apertura)).

---

## 8 · Los personajes (quién es quién y cómo se expresa)

Lo que cito entre comillas sale de las transcripciones ✅. Lo demás que
marco ⚠️ es de memoria o de una sola fuente.

### Marceline Abadeer, «la Reina Vampiro» — la elegida

- **Quién es**: vampira de **más de mil años**, hija de **Hunson
  Abadeer**, el señor de la **Nocheósfera** (latino ✅), y de una madre
  humana, Elise ⚠️. De niña, tras la Guerra de los Champiñones, la cuidó
  **Simón Petrikov**, el hombre que luego se volvió el **Rey Helado**
  ✅ (4×25; 5×14 «Simon & Marcy»).
- **Qué come**: **no chupa sangre, chupa el color rojo**: «It's not the
  blood that I like. It's the color. **I eat shades of red**» y le quita
  el rojo a una fresa (1×12, ≈2:40) ✅.
- **Qué le importa**: **la música**, Simón, la Dulce Princesa (Bonnie,
  «Peebs»), su osito **Hambo** («Goodbye, Hambo», 5×48) ✅.
- **Miedos**: que la gente que quiere **la olvide o la deje**: Simón
  pierde la memoria por la corona (4×25), su madre la dejó sola
  («Obsidian», ≈30:51) ✅. En el final: «I was so afraid something bad
  would happen to you, and I wouldn't be there» (10×13, ≈33:06) ✅.
- **Cómo habla**: burlona y relajada. Llama «**weenies**» a Finn y Jake
  («Calm down, weenies», 1×12) ✅. Presume sin despeinarse: «I've seen
  some stuff that would really make you say "like what?"» ✅. Cuando se
  pone seria, habla bajito y va al grano.
- **Cómo se ríe**: a carcajadas y **cacarea** cuando gasta una broma
  («[Cackles]», 1×22) ✅; **guiña el ojo** después de asustar («You know I
  eat the color red sometimes. [Winks]», 1×22, ≈4:35) ✅.
- **Cómo se enfada**: **sisea** («[Hisses]», en casi cada episodio) ✅,
  **se le ponen los ojos rojos** y **se transforma en monstruo**
  (murciélago, lobo) ✅ («[Eyes turn red]… taking on a demonic bat form»,
  «Obsidian» ≈33:37).
- **Cómo saluda**: aparece **de golpe, colgada del techo**, sisea y se
  presenta: «Hey, guys. What's up? **I'm Marceline the Vampire Queen**»
  (1×12, ≈2:18) ✅. En el escenario: «Hello, Hamburger Hills Cemetery!»
  (10×07) ✅.
- **Cuerpo**: **flota** en vez de caminar, se tumba en el aire, duerme
  flotando sobre la cama (3×21, ≈8:41) ✅. Toca el bajo **muy
  tranquila**, a veces con desgana (se apoya en él, «Obsidian» ≈15:25) ✅.
- **Con quién aparece**: la **Dulce Princesa** (pareja: se besan en el
  final, 10×13 ≈33:30 ✅), **Finn** (su amigo pequeño, al que chincha),
  **Simón/Rey Helado** (padre adoptivo), **Hunson** (padre pesado pero
  orgulloso: «I am proud of my punk daughter!») ✅.
- **Voces**: inglés **Olivia Olson** ✅; latino **Isabel Martiñón** ✅
  (ver §10).
- **Carácter, a fondo** (segunda pasada, wikitext de
  [Adventure Time Wiki: Marceline](https://adventuretime.fandom.com/wiki/Marceline)) ✅: independiente y
  traviesa; empieza de **antagonista** («Evicted!», 1×12) hasta que Finn
  ve que es «a radical dame who likes to play games». Debajo de la
  fachada dura es **muy sentimental**: rompió con su ex **Ash** porque él
  vendió a Hambo. **Le cuesta decir lo que siente si no es cantando**
  («Fry Song», «I'm Just Your Problem»).
- **Arco** ✅: villana traviesa (T1) → amiga cercana que acepta su
  inmortalidad («The Dark Cloud») → en «Obsidian», años después, **mucho
  más madura sin perder lo juguetona**.
- **El miedo de verdad** ✅: no sólo que la olviden; es **el peso de la
  inmortalidad**, ver morir a todos los que quiere. En «Estacas» su arco
  gira en torno a «Magia, Locura y Tristeza».
- **Cómo se ve a sí misma**: «No soy mala. Tengo mil años y perdí de
  vista mi código moral» ⚠️ (traducción del inglés; la línea doblada no
  se encontró).
- **Qué transmite**: la amiga mayor, *cool* y un poco peligrosa que
  esconde una tristeza enorme. Verla cantar es ver cómo se le cae la
  armadura.

### Finn el humano

- **Quién es**: el último humano (que se sepa al principio), un niño
  héroe que vive en la casa del árbol con Jake. Empieza con **12 años** ⚠️.
- **Muletillas**: «**Mathematical!**» → latino «**¡Matemático!**» ✅
  ([Hora de Aventura Wiki](https://horadeaventura.fandom.com/es/wiki/Mathematical!),
  [vídeo «¡¡Matemático!!»](https://www.youtube.com/watch?v=AAFA1hvHu8U)).
  «**¡Algebraico!**» ✅ (guía de cuadros del proyecto).
- **Cómo habla**: con entusiasmo total, gritando; caballeroso a su manera
  («I would never dream of it... **m'lady**», 2×01) ✅.
- **En la música**: **hace beatbox** (2×01, 3×10) ✅ y compone canciones
  tontas («A Song About Noodles», 3×10) ✅.
- **Cuerpo**: brazos de fideo, **pulgar arriba** cuando algo sale bien
  («Finn gives Jake a thumbs up», 3×21) ✅; se sonroja con facilidad ✅.
- **Carácter, a fondo** ✅ ([Adventure Time Wiki: Finn](https://adventuretime.fandom.com/wiki/Finn)):
  impulsivo y a veces de mal genio, pero **bondadoso, valiente y con un
  código moral casi absoluto**: le cuesta hasta robar en una misión
  («City of Thieves»). Hace de «sheriff moral» de Ooo.
- **Arco** ✅: al saber que su padre humano es un criminal egoísta
  («Wake Up», «The Tower») casi cae en la venganza; la Dulce Princesa le
  ayuda a controlarla. Madura en lo romántico: vomita de vergüenza en «Go
  With Me», besa a la Princesa en «Too Young», sale con Flama Princesa.
- **Cómo llora**: **casi nunca**, sólo en lo devastador (muerte, corazón
  roto), según «Dad's Dungeon» ✅. Usa las palabras de matemáticas
  («mathematical», «rhombus», «algebraic») **también para no decir
  groserías** ✅.
- **Qué transmite**: el niño que crece delante de ti; *Entertainment
  Weekly* lo compara con los niños que crecieron con Harry Potter ✅
  (§D).

### Jake el perro

- **Quién es**: perro mágico que **se estira y cambia de forma**; el
  hermano adoptivo de Finn ✅ (serie).
- **En la música**: **toca la viola** (1×09, 1×12, 3×10…) ✅, **canta
  «Bacon Pancakes»** mientras cocina (4×16, ≈7:51) ✅, hace beatbox ✅, y
  en el final dice «Music is powerful, man. It speaks to a primal pit in
  our brains… **Boompa-boompa-boom**» ✅.
- **Cómo habla (en latino)**: el doblaje le metió **modismos
  mexicanos** e improvisaciones ✅ ([Milenio](https://www.milenio.com/espectaculos/television/cambio-voz-jake-perro-hora-aventura),
  Doblaje Wiki por búsqueda). Ver §10.
- **Cuerpo**: tumbado, relajado; se transforma en cosas (en el final,
  **en megáfono**, 10×13 ≈37:15) ✅.
- **Carácter, a fondo** ✅ ([Adventure Time Wiki: Jake](https://adventuretime.fandom.com/wiki/Jake)):
  relajado, nada preocupado; se apoya en sus poderes (o en Finn) para
  salir de líos. Hace de **mentor sabio** con consejos que van de
  brillantes a absurdos. A veces **irresponsable**, deja a Finn peleando
  solo, pero **siempre llega cuando hace falta**. La wiki apunta que
  **quizá es disléxico** y con **rasgos de TDAH** ⚠️ (lo dice como
  «posible», no es oficial).
- **Qué transmite**: el hermano mayor que te dice «todo estará bien» y
  te lleva de compras (frase real del doblaje, §10.4).

### Dulce Princesa (Princess Bubblegum, Bonnibel)

- **Quién es**: la **gobernante del Dulce Reino** y **científica** ✅
  (wikis). Tiene **827 años** según *Explore the Dungeon Because I DON'T
  KNOW!*, y es **más joven que Marceline** según *The Art of Ooo* ✅
  ([Adventure Time Wiki: Princess Bubblegum](https://adventuretime.fandom.com/wiki/Princess_Bubblegum)).
- **En la música**: quiere **dirigir**: «For our next attempt, **I
  wanna be the lead**» y da órdenes técnicas («triplet quavers in
  mixolydian mode») que nadie entiende (3×10) ✅. Toca a BMO como
  instrumento ✅. En el final descubre que **la armonía es el arma**
  («It's the harmony!») ✅.
- **Cómo habla**: correcta, algo mandona, muy segura. Con Marceline,
  **juguetona**: «Ooooo, so mysterious all the time. Just like your
  song» («Obsidian») ✅.
- **Cuerpo**: postura recta, manos juntas o señalando, bata de
  laboratorio en ciencia ⚠️. Visto: **manos juntas contra el pecho**
  cuando se preocupa (§8.2) ✅; **taza en la mano** con Marceline
  («Obsidian», 0:16) ✅.
- **Carácter, a fondo** ✅: amable y educada, pero con un lado **frío y
  algo macabro**: corta y vuelve a pegar extremidades de criaturitas «sin
  dolor» para experimentar («The Lich»), bromea con venenos («The Other
  Tarts»). **Muy racional**: «all magic is science». **Come de más**
  cuando el estrés la supera. Es el personaje con **más vestuarios** de
  toda la serie.
- **Qué transmite**: la que lo controla todo y lo arregla todo, y que
  con Marceline por fin se deja llevar.

### BMO

- **Quién es**: una **consola de videojuegos viva** que vive con Finn y
  Jake ✅ (wikis).
- **En la música**: canta «**Time Adventure**» en el final, con Jake en
  brazos, y grita «**My art is a weapon!**» (10×13, ≈35:55-37:00) ✅.
  Tiene **disco propio**: «BMO's Mixtape» (§3.4) ✅. La Princesa le hace
  sonar «Sound Structure Alpha» (3×10) ✅.
- **Cómo habla**: como un niño pequeño muy seguro de sí mismo; habla de
  sí en tercera persona a veces ✅ ([Adventure Time Wiki: BMO](https://adventuretime.fandom.com/wiki/BMO)).
- **Carácter, a fondo** ✅: dice «I am incapable of emotion», **pero llora,
  se enfada y se pone celoso**. Muy protector: «If anyone tries to hurt
  Finn, I will kill them». **Hace de mediador** cuando Finn y Jake se
  pelean (en «Video Makers» edita su película para arreglarlo).
- **Es el personaje favorito del creador**, Pendleton Ward (entrevista con
  Hot Topic) ✅.

### Los secundarios musicales

- **Rey Helado / Simón**: canta mal y con ganas; toca el **omnichord**
  ✅ (4×25); en «Obsidian» canta «Remember You» en una taberna: «This is
  going out to a little girl named Marceline» ✅.
- **Hunson Abadeer**: el padre; canta cancioncitas tontas («Walk, walk,
  walk, not suck, suck, suck», 10×07) ✅ y arruina el concierto de su
  hija por orgullo ✅.
- **El Hoyo Musical** («Music Hole»): el personaje que **estrena una
  canción nueva** al final de la serie (10×13) ✅. Poco conocido, pero su
  frase es perfecta para el canal.
- **Glassboy** («Obsidian»): **fan de Marceline**, con muñeca suya ✅.

### 8.1 Rey Helado / Simon Petrikov (el secundario más querido)

- **Como Simon** ✅: inteligente, cariñoso, capaz de un **sacrificio
  enorme**: cuidó a Marceline niña en el apocalipsis mientras la corona
  le quitaba la cordura. Sus cartas (4×25) muestran que **temía
  abandonarla** ([Adventure Time Wiki: Ice King](https://adventuretime.fandom.com/wiki/Ice_King)).
- **Como Rey Helado** ✅: al principio, villano pesado «al estilo
  Gargamel»; desde la T3, **trágico y solo**: quiere casarse con una
  princesa **sin recordar por qué** (el eco de **Betty**, su prometida).
- **Cómo se expresa** ✅: optimista hasta en lo peor; en el final
  consuela a Finn: nadie elige cómo morir, pero al menos estaban juntos.
- **Con Marceline** ✅: padre e hija adoptivos. Ella (y Betty) son las
  únicas que lo llaman «Simon»; a Marceline se lo acepta.
- **Voces**: latino **Óscar Flores**, toda la serie ✅ (§10).
- **Qué transmite**: risa y pena a la vez. *Vulture* lo llamó «el mejor
  personaje» de la serie y lee su arco como una metáfora del
  **Alzheimer** ✅ (§9, §D).
- Detalle de trivia: un **tatuaje de pingüino** en el glúteo derecho
  («Prisoners of Love») ⚠️ (sin fotograma).

### 8.2 Su cara en cada emoción (vista en vídeo, con minuto)

| Personaje | Emoción | Cómo es la cara | Clip y minuto |
|---|---|---|---|
| Marceline | tristeza | ojos entornados, boca abierta, cantando | [«Fry Song» 0:32](https://www.dailymotion.com/video/x51arca?t=32) ✅ |
| Marceline | tristeza (llanto) | cabeza atrás, dientes apretados en mueca triangular, **una sola lágrima** de un ojo cerrado | [«I Remember You» ≈1:18](https://www.dailymotion.com/video/xzt1l7?t=78) ⚠️ (ver §2.4) |
| Marceline | angustia, pensar | **una mano en la cabeza** | [«I Remember You» 0:24](https://www.dailymotion.com/video/xzt1l7?t=24) ✅ |
| Marceline | rabia | **ceño fruncido, colmillos a la vista**, canta con fuerza | [«I'm Just Your Problem» 0:52](https://www.dailymotion.com/video/x537pqr?t=52) ✅ |
| Marceline | miedo | shock, ojos abiertos, fondo oscuro estrellado | [tráiler «Obsidian» 1:24](https://www.dailymotion.com/video/x7xejon?t=84) ✅ |
| Marceline | rabia extrema y llanto | *model sheets* oficiales: grito con ojos rojos y «a punto de llorar» | hoja 1 **#15** y **#16** ✅ |
| Finn | vergüenza | óvalo rosa en las mejillas, boca en rayita, ojos de punto muy abiertos y descentrados | [piloto 6:00](https://www.dailymotion.com/video/x84oaz2?t=360) ✅ |
| Rey Helado | fastidio cómico | cejas caídas, ojos entrecerrados, boca en zigzag; dice «Eso... es estúpido» con Finn agarrándolo | [piloto 4:05](https://www.dailymotion.com/video/x84oaz2?t=245) ✅ |
| Jake | alegría, orgullo | ojos enormes casi blancos con franja negra abajo, **sonrisa ancha de dientes cuadrados** (piel azulada por la luz nocturna) | [«Jake the Starchild» 1:39](https://www.dailymotion.com/video/x6gkz32?t=99) ✅ |
| Dulce Princesa | preocupación, miedo | ojos muy redondos con brillo blanco, boquita entreabierta, **manos juntas contra el pecho** | [«Slumber Party Panic» 2:12](https://www.dailymotion.com/video/x8ghhnc?t=132) ✅ |
| BMO | calma, contento | ojos cerrados en dos curvas, boca en curva suave | [«The More You Moe…» 2:36](https://www.dailymotion.com/video/x3q931u?t=156) ✅ |

**Cuentas**: de las **25 combinaciones** (Marceline, Finn, Jake, Princesa
y BMO × alegría, rabia, tristeza, miedo y vergüenza) hay **7 vistas en
vídeo** (Marceline 3, los demás 1), más la del Rey Helado. **Faltan** ⚠️:
alegría y vergüenza de Marceline; alegría, rabia, tristeza y miedo de
Finn; rabia, tristeza, miedo y vergüenza de Jake; alegría, rabia,
tristeza y vergüenza de la Princesa; rabia, tristeza, miedo y vergüenza
de BMO. Los clips de Dailymotion no daban más y YouTube pedía iniciar
sesión.

### 8.3 Dinámicas (para láminas en grupo) ✅

- **Marceline y la Dulce Princesa**: de la tensión con humor a pareja
  oficial (beso en 10×13; en «Obsidian» ríen juntas).
- **Marceline y Simon**: padre e hija adoptivos (arriba).
- **Finn y Jake**: el impulsivo con código moral y el hermano sabio pero
  disperso; el contraste es la base cómica del dúo.
- **BMO media** cuando Finn y Jake discuten.
- **Marceline y Finn**: ella lo chincha y él la admira (§8, arriba).

### 8.4 Cómo suenan en latino (medido con `voz.py`) ✅

Sobre las 6 muestras oficiales de Doblaje Wiki (§10.4):

| Personaje | Registro | Expresividad | Velocidad |
|---|---|---|---|
| Marceline (Isabel Martiñón) | agudo, 295 Hz | **muy expresiva**, 17,3 semitonos | normal, 2,86 palabras/s |
| Finn (José Antonio Toledano) | medio, 164 Hz | muy expresiva, 16,0 | **rápida**, 3,49 |
| Jake (José Arenas, tono nuevo) | medio, 214 Hz | muy expresiva, 14,8 | normal, 2,43 |
| Dulce Princesa (Karla Falcón) | **muy agudo**, 397 Hz | — | rápida, 3,36 |
| Rey Helado (Óscar Flores) | agudo, 266 Hz | muy expresiva, 15,8 | — |
| BMO | **muy agudo**, 465 Hz | — | **lenta**, 1,36 |

---

## 9 · ¿Quién es el más querido?

- **No encontré una encuesta oficial** de Cartoon Network ni de la
  productora.
- Lo que sí hay:
  - La editorial **BOOM!** llamó a Marceline «**fan-favorite**» en la nota
    de prensa de «Marceline and the Scream Queens» ✅
    ([Wikipedia](https://en.wikipedia.org/wiki/Marceline_the_Vampire_Queen)
    y [Adventure Time Wiki](https://adventuretime.fandom.com/wiki/Marceline), leídas en la segunda pasada).
  - Según **Pendleton Ward**, su popularidad **«creció enormemente»**
    después de «Evicted!» (1×12), su primer episodio ✅ (mismas fuentes).
  - **Cartoon Network UK** la nombró **«Character of the Week»** el **24
    de enero de 2012** ✅ (Wikipedia + Adventure Time Wiki). Es lo más
    parecido a un reconocimiento oficial que hay.
  - ***The Guardian*** la llamó **lo mejor de la serie** en una reseña
    del DVD: «responsable de algunas de las mejores canciones del show» ✅.
  - **WhatCulture** (2016) la puso **#4** de los mejores personajes: «el
    personaje más cool de la serie» ⚠️ (una fuente).
  - **El Rey Helado/Simon**: **Eric Thurm** (*Vulture*) lo llamó
    «**Adventure Time's Best Character**» ✅
    ([Wikipedia: Ice King](https://en.wikipedia.org/wiki/Ice_King) +
    [Adventure Time Wiki](https://adventuretime.fandom.com/wiki/Ice_King)). Para mucha gente, el más querido.
  - **BMO es el personaje favorito del propio Pendleton Ward** (entrevista
    con Hot Topic) ✅ ([Adventure Time Wiki: BMO](https://adventuretime.fandom.com/wiki/BMO)). El creador
    prefiere a un secundario.
  - Otros secundarios con peso propio: la **Princesa Grumosa** (memes,
    «¡Oh por Glob!») y **Fionna**, que tuvo serie propia («Fionna & Cake»,
    2023-2024) ✅.
  - Tuvo **su propia miniserie** («Estacas», 2015) y **su propio
    especial** («Obsidian», 2020) ✅
    ([Wikipedia: Stakes](https://en.wikipedia.org/wiki/Stakes_(miniseries)),
    [Wikipedia: Distant Lands](https://en.wikipedia.org/wiki/Adventure_Time:_Distant_Lands)).
    Sólo ella y la Princesa (y BMO, con su especial) tienen eso.
  - Tiene **dos discos propios** («Marceline Canta» en español y
    portugués) ✅.
  - Listas de fans: [Ranker](https://www.ranker.com/list/best-adventure-time-characters/cerberus)
    (1.958 votantes a septiembre de 2026; **da 401**, no se pudo ver su
    orden ⚠️),
    [Looper](https://www.looper.com/803890/15-most-popular-adventure-time-characters-ranked-worst-to-best/),
    [Screen Rant](https://screenrant.com/best-adventure-time-characters-ranked/)
    ⚠️ (no pude abrirlas).
  - Japón: «マーセリンはアドベンチャー・タイムの人気キャラクターの一人»
    (es uno de los personajes populares) ⚠️
    ([ciatr](https://ciatr.jp/topics/74459)).
- **Conclusión**: no hay encuesta oficial con números. La crítica se
  reparte entre **Marceline** (BOOM!, CN UK, *The Guardian*) y **el Rey
  Helado** (*Vulture*); el creador prefiere a **BMO**. Para un canal de
  música, **Marceline no es sólo de las más queridas: es la única música
  de verdad del reparto**. Finn y Jake acompañan (beatbox y viola), BMO
  es el secundario tierno con disco propio y **Simon** el que hace
  llorar (§D).

---

## 10 · Doblaje latino

> **Segunda pasada**: la página de la serie en Doblaje Wiki **sí se leyó
> entera por su API** ([`Hora de aventura`](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Hora_de_aventura),
> 87 135 caracteres, con `curl -A "Mozilla/5.0"`). Es la primera fuente
> de cada nombre; la segunda va en la tabla. En la primera pasada todo
> salía de resúmenes de búsqueda.

### 10.1 El doblaje de la serie ✅

- Estreno en Latinoamérica: **8 de agosto de 2010** (en EE. UU., 5 de
  abril de 2010). Terminó en EE. UU. el **3 de septiembre de 2018** (283
  episodios, 10 temporadas) y en Latinoamérica el **23 de septiembre de
  2018** ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Hora_de_aventura)
  + [Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time)).
- **Estudio**: **Sensaciones Sónicas** (México) desde el principio
  **hasta la temporada 5**; desde el episodio «**El traje de Jake**»,
  **SDI Media de México** ✅
  ([Hora de Aventura Wiki: Sensaciones Sónicas](https://horadeaventura.fandom.com/es/wiki/Sensaciones_S%C3%B3nicas),
  [Milenio](https://www.milenio.com/espectaculos/television/cambio-voz-jake-perro-hora-aventura)
  habla de SDI México). Algunos promocionales se doblaron en **Candiani
  Dubbing Studios** ✅ (Doblaje Wiki, tabla de estudios).
- **Dirección**, tabla exacta de Doblaje Wiki ✅:

  | Director | Temporadas |
  |---|---|
  | **Óscar Flores** (también el Rey Helado) | 1-2, 4 (eps. 96-101), 5 (desde el 131) |
  | Rafael Pacheco | 3, 8 episodios |
  | Circe Luna | 3 y 4, algunos |
  | Elsa Covián | 4, algunos |
  | Carlos Hugo Hidalgo | 4, algunos (retake de sonido) |
  | Juan Antonio Edwards | 3, algunos |
  | *(sin datos en la wiki)* | 5, hasta el ep. 130 |
  | **Arturo Castañeda** | **6 a 9** |

- **Arturo Castañeda** (director de la T6 a la T9): nació el 3-oct-1988
  en Ciudad de México, **hijo de Mario Castañeda (la voz de Goku) y Rommy
  Mendoza**; de niño dobló a Harry Potter en *La piedra filosofal* ✅
  ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Arturo_Casta%C3%B1eda),
  [Comic Fest Juárez](https://www.facebook.com/comicfestjuarez/posts/arturo-casta%C3%B1eda-doblajeactor-y-director-de-doblaje-mexicano-hijo-de-los-tambi%C3%A9n/811605114317097/)).
- **Productor ejecutivo** (T5.2-6): **Mario Castañeda** ⚠️ (sólo Doblaje
  Wiki). Ingeniero de grabación: Antonio Hernández. Gerentes de
  producción: Gerardo Suárez (T1-5) y Gabriela Garay (T5.2-9) ✅.
- **Traductores** ✅: Carlos Hugo Hidalgo (la mayoría), Janet León, Luis
  Leonardo Suárez (desde el 131), Circe Luna y David Bueno (ep. 279).
- **Las voces de Finn y Marceline nunca cambiaron** en toda la serie,
  cosa rara: casi todos los demás tuvieron cambios ✅ (Doblaje Wiki,
  curiosidades).
- **Canal 2 (El Salvador) y Canal 5 (México)** la emiten **sin las
  censuras** de Cartoon Network y Netflix Latinoamérica ✅ (Doblaje Wiki).

### 10.2 Reparto

| Personaje | Voz latina | Estado | Fuentes |
|---|---|---|---|
| **Marceline** (habla) | **Isabel Martiñón**, en toda la serie y las miniseries | ✅ | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Marceline_Abadeer), [TikTok Expomac Veracruz](https://www.tiktok.com/@rebecavirgen/video/7434952138339536184), [Facebook Starcon](https://www.facebook.com/starconmx/videos/isabel-marti%C3%B1on-actriz-de-doblaje-que-dio-voz-a-marceline-en-hora-de-aventura-be/1609015216591153/) |
| Marceline (canciones, temp. 1-2) | **Claudia Urbán** | ⚠️ | Doblaje Wiki (por búsqueda), [Hora de Aventura Wiki](https://horadeaventura.fandom.com/es/wiki/Claudia_Urb%C3%A1n) |
| Marceline (canciones, temp. 3-4) | **Patty Urbán** | ⚠️ | Doblaje Wiki (por búsqueda) |
| Marceline (canciones desde la temp. 5, «Estacas» con «Todo se queda», «Tierras lejanas») | **Carla Cerda** | ⚠️ | [Doblaje Wiki: Marceline](https://doblaje.fandom.com/es/wiki/Marceline_Abadeer), [Doblaje Wiki: Carla Cerda](https://doblaje.fandom.com/es/wiki/Carla_Cerda) (mismo wiki) |
| Marceline (una canción de la temp. 6) | Romina Marroquín Payró | ⚠️ | Doblaje Wiki (por búsqueda) |
| **Finn** | **José Antonio Toledano**, **toda la serie** (de los pocos que no cambió) y «Misiones Secundarias» | ✅ | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Hora_de_aventura), [GeekZilla](https://geekzilla.tech/hora-de-aventura-misiones-secundarias-llega-a-hbo-max/), [The Project Arcade](https://theprojectarcade.com/hora-de-aventura-misiones-secundarias-revive-al-jake-clasico-hbo-max-revela-su-doblaje-latino/) |
| **Jake** | **José Arenas** | ✅ | [Doblaje Wiki: Jake](https://doblaje.fandom.com/es/wiki/Jake_el_perro), [Milenio](https://www.milenio.com/espectaculos/television/cambio-voz-jake-perro-hora-aventura), [TVLaint](https://www.tvlaint.com/2026/09/jose-arenas-regresa-como-jake-en-hora.html) |
| **Dulce Princesa** | **Karla Falcón** (temp. 1-2; **vuelve en la 4, ep. 96, «Rey Gusano»**, hasta el final, **tras una campaña de los fans**, §E) | ✅ | [Doblaje Wiki: Dulce Princesa](https://doblaje.fandom.com/es/wiki/Dulce_Princesa), [TikTok, entrevista en Festigame 2024](https://www.tiktok.com/@eldiariodelalquimista/video/7440244073505623352) (también es Tori en *Victorious* y Jinx en *Arcane*) |
| Dulce Princesa (suplente, **eps. 58-94**, temp. 3-4) | **Claudia Urbán**; se retiró del doblaje en **noviembre de 2012** para llevar su empresa con su esposo, Gerardo Suárez | ✅ | Doblaje Wiki (tabla y ficha propia) |
| **Rey Helado** | **Óscar Flores** (toda la serie y «Misiones Secundarias») | ✅ | [Doblaje Wiki: Rey Helado](https://doblaje.fandom.com/es/wiki/Rey_Helado), noticias de «Misiones Secundarias» |
| **BMO** | **Gustavo Melgarejo** (T1-5) → **Héctor Emmanuel Gómez** (T5.2-9, desde «El traje de Jake») | ✅ | Doblaje Wiki (API), [Hora de Aventura Wiki: Héctor Emmanuel Gómez](https://horadeaventura.fandom.com/es/wiki/H%C3%A9ctor_Emmanuel_G%C3%B3mez) |
| **Princesa Grumosa** | **Alfonso Obregón**, casi toda la serie | ✅ | Doblaje Wiki (API), [Hora-de wiki](https://hora-de.fandom.com/es/wiki/Princesa_Grumosa) |
| Jake (2 loops sueltos) | Víctor Ugarte (ep. 202) y Tommy Rojas (ep. 279, «Diamantes y limones») | ⚠️ | sólo Doblaje Wiki |
| Rey Helado (eps. 59-60) | Rafael Pacheco | ⚠️ | sólo Doblaje Wiki |
| Marceline alterna («Fionna & Cake») | Ángela Villanueva (T5) → vuelve Isabel Martiñón (T7) | ⚠️ | sólo Doblaje Wiki |
| Hunson Abadeer | José Luis Orozco (T2) → Rafael Pacheco (T3) → Julián Lavat (T4) → Enrique Cervantes (T9) | ⚠️ | sólo Doblaje Wiki |

Voz original de Marceline: **Olivia Olson**, que **canta ella misma** sus
canciones ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Olivia_Olson),
[SciFiNow](https://www.scifinow.co.uk/interviews/adventure-times-olivia-olson-on-marceline-stakes-and-songs/)).

### 10.3 El caso de la voz de Jake ✅

- En las primeras temporadas, Jake hablaba con **modismos mexicanos** y
  los actores **improvisaban**; eso creó chistes que **no existen en
  inglés** ✅ ([Milenio](https://www.milenio.com/espectaculos/television/cambio-voz-jake-perro-hora-aventura),
  [Comunidad HDA Latino](http://comunidadhdalatino.blogspot.com/2015/02/cambio-de-la-voz-de-jake.html)).
- **Desde mitad de la temporada 5**, Cartoon Network Latinoamérica pidió
  «**no más mexicanismos**» y Arenas tuvo que hacerlo **neutro**. A casi
  todos los fans les pareció aburrido ✅ (mismas fuentes y
  [TikTok](https://www.tiktok.com/@acubick/video/7206541052713438469)).
- En «**Misiones Secundarias**» (2026) **vuelven los modismos** y Arenas
  recupera el tono de las primeras temporadas ✅ (búsquedas 4 y 27).

### 10.4 Frases del doblaje latino

| Frase | Quién, dónde | Estado |
|---|---|---|
| «**¡Matemático!**» | Finn | ✅ |
| «**¡Algebraico!**» | Finn, «Pánico en la fiesta del palacio» | ✅ (guía de cuadros) |
| «**No le creas, compadre, así le dijeron a mi hermana y ahora estoy lleno de sobrinos**» | Jake, «El sicario». Por el título y la escena creo que es **3×04 «Hitman»**, cuando el Rey Helado les jura que no los va a matar de verdad ⚠️ (deducción mía) | ⚠️ (Doblaje Wiki, dos búsquedas) |
| «**¡Ay, Jojutla!**» | Jake, «Poder animal» | ⚠️ |
| «**Nunca me hagan eso**» (de Clavillazo) | Jake | ✅ (guía de cuadros y búsqueda 27) |
| «**¡Ay, mamachita!**», «**¿Qué pasó, qué pasó? Vamos, ¡ay!**» | Jake | ✅ (guía de cuadros) |
| «**Los amigos se ayudan siempre, ¡SIEMPRE!**» | Finn | ⚠️ |
| «**¡Oh por Glob!**» | **Princesa Grumosa**; es su muletilla latina, de «Oh my Glob». **Corrección**: no se cambió por «Oh por Dios»; lleva «Glob» en latino | ✅ (Doblaje Wiki + [Hora-de wiki](https://hora-de.fandom.com/es/wiki/Princesa_Grumosa)) |
| «**Soy tu problema**», «**Canción de las papas**», «**Todo se queda**», «**¡Oh, Dulce Princesa!**» | títulos latinos de canciones | ✅ |
| «**Marceline la Reina Vampiro**» | título latino oficial de 7×06 («Estacas», parte 1) | ✅ ([HBO Max](https://www.hbomax.com/bo/es/shows/hora-de-aventura/s7/fff09eaf-17c3-446b-be32-8a0d47e4ccf1/e6-marceline-la-reina-vampiro/73c26176-7919-4bfe-8b77-db471f43719d), [Hora de Aventura Wiki](https://horadeaventura.fandom.com/es/wiki/Marceline_la_Reina_Vampiro)) |

**Intro latina** ⚠️ (letras de fans; el orden varía entre páginas):
«Hora de aventura, llama a tus amigos, vamos a tierras muy lejanas, con
Jake el perro y Finn el humano, y diversión siempre tendrás, ¡es hora
de aventura!»
([La Cuerda](https://chords.lacuerda.net/musica_de_tv/hora_de_aventura__intro),
[musica.com](https://www.musica.com/letras.asp?letra=2056436),
[Hora de Aventura Wiki: secuencia de apertura](https://horadeaventura.fandom.com/es/wiki/Secuencia_de_apertura)).

**Frases oídas de verdad** (segunda pasada): Doblaje Wiki sube una
muestra de audio de cada actor. Se bajaron **6** y se transcribieron con
`voz.py` (Whisper local). **Son diálogo real doblado** ✅; **de qué
episodio sale cada una, no lo dice la wiki** ⚠️, y Whisper puede fallar
en algún nombre (marcado).

| Personaje | Frase textual | Audio |
|---|---|---|
| **Marceline** (Isabel Martiñón) | «¿Vía⚠️? ¿Qué estás haciendo? No puedes estar aquí. **Ash no quiere que salga con mortales**» | [.ogg](https://static.wikia.nocookie.net/doblaje/images/a/a6/Isabel_Marti%C3%B1on_como_Marceline.ogg) |
| **Finn** (José Antonio Toledano, T5) | «Tienes razón, sólo hay una forma de salir. Uno de nosotros será sacrificado para que los otros vivan. […] No traten de convencerme. Estoy seguro de que... esto es lo que significa ser un...» | [.ogg](https://static.wikia.nocookie.net/doblaje/images/5/57/Jose_Toledano_-_Finn_5ta_Temporada.ogg) |
| **Jake** (José Arenas, tono nuevo) | «Estoy para ti, hermano. Pero, Finn, te diré algo gentilmente. Necesitas otra espada. Ellos iban a acabarte. Todo estará bien. **Vayamos de compras**» | [.ogg](https://static.wikia.nocookie.net/doblaje/images/5/51/Jose_Arenas_-_Jake_Nuevo_Tono.ogg) |
| **Dulce Princesa** (Karla Falcón) | «**¡Los veo en el dulce reino! ¡Esta noche!**» | [.ogg](https://static.wikia.nocookie.net/doblaje/images/4/40/Karla_Falcon_como_la_Dulce_Princesa.ogg) |
| **Rey Helado** (Óscar Flores) | «¡La hora es suya, pero el día será mío! ¡Como tú, princesa mía!» | [.ogg](https://static.wikia.nocookie.net/doblaje/images/7/7a/Oscar_Flores_como_el_Rey_Helado.ogg) |
| **BMO** | «¡Jajajajajaja! ¡Juguemos⚠️ a policías y⚠️ ladrones!» (Whisper oyó «Cukemos... iradrones»; reconstruido de oído) | [.ogg](https://static.wikia.nocookie.net/doblaje/images/7/70/BMO.ogg) |

Cómo suena cada voz (registro, expresividad, velocidad): §8.4.

- El **título latino del final** en Doblaje Wiki es **«Ven Conmigo»**
  ✅; la primera pasada lo daba como «¡Ven conmigo!» (así sale en otras
  páginas) ⚠️.
- **No hay clips oficiales doblados** en Dailymotion (sólo tráileres y
  cajitas felices) y YouTube pide iniciar sesión: por eso las frases
  salen de las muestras de la wiki.

> **No encontré** cómo dice Marceline en latino «Thanks for helping me
> record», «I'm Marceline the Vampire Queen» ni la frase del Hoyo Musical.
> Las frases que propongo para la lámina son **traducción mía**, salvo
> las de la tabla de arriba.

### 10.5 Lo nuevo: «Hora de aventura: Misiones Secundarias» ✅

- Serie nueva sobre **Finn y Jake de pequeños**, episodios sueltos como
  las primeras temporadas. Showrunner **Nate Cash** (Cartoon Network
  Studios) ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time:_Side_Quests),
  [Gizmodo](https://gizmodo.com/adventure-time-side-quests-returns-in-ooo-ctober-2000805659)).
- En EE. UU. salió el **29 de junio de 2026** (Disney+ y Hulu); la
  temporada 2, el **2 de octubre de 2026**. En Latinoamérica llega por
  **Cartoon Network y HBO Max el 5 de octubre de 2026, doblada desde el
  primer día** ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time:_Side_Quests),
  [GeekZilla](https://geekzilla.tech/hora-de-aventura-misiones-secundarias-llega-a-hbo-max/),
  [BSCKids](https://www.bsckids.com/2026/09/adventure-time-side-quests-sets-october-return-for-season-2/)).
- Doblaje: **Iyuno México**, dirección de **Miguel Ángel Leal** ⚠️
  (una sola fuente, por búsqueda). Vuelven **Toledano, Arenas y Flores** ✅.
- En inglés, **Olivia Olson** sigue siendo Marceline ✅.

---

## 11 · Música

### 11.1 Quién la hace ✅

- **Casey James Basichis** (el compositor original) y **Tim Kiefer**.
  Estudiaron en **CalArts** con Pendleton Ward. Antes eran un dúo de
  **ukelele y Game Boy** que vendía CD con fundas de tela peluda pintada
  con spray
  ([VICE](https://www.vice.com/en/article/talking-to-the-musical-masterminds-behind-adventure-time/),
  [AV Club](https://www.avclub.com/read-this-the-men-behind-the-music-on-adventure-time-1798279451),
  [JeanBookNerd, entrevista a Kiefer](https://www.jeanbooknerd.com/2018/05/adventure-time-tim-kiefer-interview.html)).
- Basichis hacía el «esqueleto» de la música **en la ducha, con la voz y
  un ukelele, grabando con el teléfono** ⚠️ (una fuente).
- Las canciones de Marceline las escribieron sobre todo **storyboarders**,
  y la más famosa, **Rebecca Sugar** (luego creadora de «Steven
  Universe»): «Fry Song», «I'm Just Your Problem», «Remember You» y, ya
  fuera de la serie, «**Everything Stays**» para «Estacas» ✅
  ([Wikipedia: It Came from the Nightosphere](https://en.wikipedia.org/wiki/It_Came_from_the_Nightosphere),
  [What Was Missing](https://en.wikipedia.org/wiki/What_Was_Missing),
  [I Remember You](https://en.wikipedia.org/wiki/I_Remember_You_(Adventure_Time)),
  [Stakes](https://en.wikipedia.org/wiki/Stakes_(miniseries))).
- «Everything Stays» se presentó en la **Comic-Con de San Diego de
  2015** con Olivia Olson y Rebecca Sugar ✅ (Wikipedia y
  [The Mary Sue](https://www.themarysue.com/olivia-olson-talks-marceline/), por búsqueda).
- **De qué trata de verdad «Everything Stays»**: lo dice la propia
  Rebecca Sugar en su TikTok (texto leído con la API oEmbed de TikTok):
  «I wrote this song for Adventure Time after I'd left to create Steven
  Universe… I was so touched to be asked to write a song for **Marcy's
  mom**». Es **la canción de la madre de Marceline**, no una despedida
  cualquiera. La graba con Jeff (@Jeffthatnoise) al violín ✅ (fuente
  primaria: [@rebeccasugar](https://www.tiktok.com/@rebeccasugar/video/7380076323168996650)).
- **El disco oficial en español** tiene 10 pistas con su duración real
  (lista en §3.4); «**Acompáñame**» es «Come Along With Me» ✅.
- **La intro cambia en cada miniserie**: hay versiones para «Stakes»,
  «Islands», «Food Chain» y «Fionna & Cake», de 24-26 s cada una
  ([Islands](https://www.dailymotion.com/video/x5whnwn),
  [Stakes](https://www.dailymotion.com/video/x5whnw2),
  [Food Chain](https://www.dailymotion.com/video/x5whp1h)) ✅ que existen
  y cuánto duran; ⚠️ no se miraron fotograma a fotograma.

### 11.2 Los temas que dan ambiente

| Tema | Dónde | Ambiente |
|---|---|---|
| Intro «Hora de aventura» | cada episodio | ukelele y voz aniñada, alegre y casera ⚠️ (el sonido no se midió; la imagen sí se vio, §2.9) |
| **«Island Song (Come Along With Me)»**, de **Ashley Eriksson** | cierre de cada episodio y final de la serie | dulce, melancólico, de despedida ✅ |
| «Fry Song» / «Canción de las papas» | 2×01 | bajo solo y voz, **íntimo, de grabación casera** ✅ |
| «I'm Just Your Problem» / «Soy tu problema» | 3×10 | rock con rabia contenida, **con banda** ✅ |
| «Remember You» / «Recordándote» | 4×25 | teclado (omnichord) y voz, **para llorar** ✅ |
| «Slow Dance With You» | 10×07 | **concierto en directo** ✅ |
| «Everything Stays» / «Todo se queda» | 7×07 | nana, triste y cálida; **es la canción de la madre de Marceline** ✅ |
| «Woke Up», «Monster», «See Through», «Eternity With You» | «Obsidian» | **punk** («Woke Up»), **balada** («Monster»), dúo final ✅ |
| «Time Adventure» | 10×13 | BMO, **canción de cuna que vence al caos** ✅ |
| «Bacon Pancakes» | 4×16 | tontería pegadiza de Jake; meme ✅ |

> Para #musica-nueva, el ambiente es **el del estreno casero**: bajo,
> voz y ritmo hecho con la boca. No una superproducción.

**Efectos de sonido**: es animación americana; **no hay onomatopeyas
rotuladas** en pantalla como en el manga. Los sonidos que todos
reconocen son de voz: el **siseo** de Marceline, el **beatbox** de Finn,
el «**Boompa-boompa-boom**» de Jake (10×13) y la **risa** de BMO (§10.4).
No se buscó un efecto de sonido concreto ⚠️.

---

## 12 · Vídeos

> **Segunda pasada**: YouTube sigue pidiendo iniciar sesión, así que los
> enlaces de YouTube de abajo (12.1-12.2) **siguen sin mirar** ⚠️. Los que
> sí se vieron, con minuto, son los de Dailymotion (12.0). Los TikTok se
> comprobaron con la API oEmbed (título y autor reales).

### 12.0 Vistos de verdad, con minuto (Dailymotion) ✅

| Clip | Dura | Canal | Qué sirve, con minuto |
|---|---|---|---|
| [Opening doblado al latino](https://www.dailymotion.com/video/x8p2dsj) | 0:29 | Espinof (medio de cine) | la intro entera, 1080p (§2.9) |
| [«I'm Just Your Problem»](https://www.dailymotion.com/video/x537pqr) | 2:07 | **Cartoon Network** (oficial) | [0:12 entra volando con el bajo](https://www.dailymotion.com/video/x537pqr?t=12), [0:52 canta con rabia](https://www.dailymotion.com/video/x537pqr?t=52), [1:32 apoyada en la puerta](https://www.dailymotion.com/video/x537pqr?t=92) |
| [«Fry Song» Sing-a-Long](https://www.dailymotion.com/video/x51arca) | 0:52 | resubido de «Toon Tunes» de CN | [0:00 flota bocabajo](https://www.dailymotion.com/video/x51arca?t=0), [0:12 la grabadora](https://www.dailymotion.com/video/x51arca?t=12), [0:32 canta triste](https://www.dailymotion.com/video/x51arca?t=32) |
| [«I Remember You»](https://www.dailymotion.com/video/xzt1l7) | 1:58 | emisión de CN HD, audio francés | [0:24 mano en la cabeza](https://www.dailymotion.com/video/xzt1l7?t=24), [0:42 dúo bajo y batería](https://www.dailymotion.com/video/xzt1l7?t=42), [1:36 la Polaroid](https://www.dailymotion.com/video/xzt1l7?t=96) |
| [Tráiler «Obsidian»](https://www.dailymotion.com/video/x7xejon) | 1:30 | resubido, logo HBO Max | [0:16 las tazas](https://www.dailymotion.com/video/x7xejon?t=16), [0:36 flota tocando al Reino de Cristal](https://www.dailymotion.com/video/x7xejon?t=36), [1:08 bajo al hombro](https://www.dailymotion.com/video/x7xejon?t=68) |
| [Créditos finales](https://www.dailymotion.com/video/x4fakxm) | 0:33 | resubido, logos reales | staff y fondo verde lima (§2.9) |
| [Tráiler de «BMO» (Tierras lejanas), en español](https://www.dailymotion.com/video/x7vjn4d) | 1:54 | HobbyConsolas | tráiler oficial doblado ⚠️ (identificado, sin mirar a fondo) |
| [Tráiler de «Fionna & Cake»](https://www.dailymotion.com/video/x8nce5e) | 2:05 | HobbyConsolas | 720p; no sale la Marceline clásica |
| [Piloto subtitulado](https://www.dailymotion.com/video/x84oaz2) | 7:30 | Capra TV | [4:05 Rey Helado](https://www.dailymotion.com/video/x84oaz2?t=245), [6:00 Finn avergonzado](https://www.dailymotion.com/video/x84oaz2?t=360) |
| Clips de la parte de voz | — | con logo de CN | [«Jake the Starchild» 1:39](https://www.dailymotion.com/video/x6gkz32?t=99), [«Slumber Party Panic» 2:12](https://www.dailymotion.com/video/x8ghhnc?t=132), [«The More You Moe…» 2:36](https://www.dailymotion.com/video/x3q931u?t=156) |

### 12.1 Oficiales (Cartoon Network)

- [«I'm Just Your Problem» | Adventure Time | Cartoon Network](https://www.youtube.com/watch?v=h28xpNvW9Yw) — la escena de la banda (3×10).
- [«I'm Just Your Problem» – Sing Along (Cartoon Network UK)](https://www.youtube.com/watch?v=QikaN4522yI) — **con la letra en pantalla**: referencia de cómo CN pone texto de canción.
- [«Fries Song» – Toon Tunes (Cartoon Network UK)](https://www.youtube.com/watch?v=fpmDtouxwlI) — la grabación casera (2×01).
- [Marceline Sings «Monster» | Distant Lands – Obsidian](https://www.youtube.com/watch?v=g--_zGaKPYI).
- [Olivia Olson Performing «Monster» | Cartoon Network](https://www.youtube.com/watch?v=inkx3joKxl8) — la actriz cantando en directo.
- [Canal «Hora de Aventura LA»](https://www.youtube.com/@HoradeAventuraLA) ⚠️ (no sé si es oficial).

### 12.2 En español latino

- [«Soy tu Problema» – Marceline (Español Latino)](https://www.youtube.com/watch?v=uvLY4KHNVIs).
- [«Soy Tu Problema» con letra](https://www.youtube.com/watch?v=9Q-i-QhHd2Q).
- [«Todo Se Queda» completa con letra](https://www.youtube.com/watch?v=jqUPSd2oWeo).
- [«¡¡Matemático!!»](https://www.youtube.com/watch?v=AAFA1hvHu8U).
- [Las voces de Hora de Aventura (Draquio)](https://www.youtube.com/watch?v=13waXilj5io) y [su vídeo de la Dulce Princesa](https://www.youtube.com/watch?v=m1RRisrV06s).
- [«¡TODAS las VOCES principales de Hora de Aventura!»](https://www.youtube.com/watch?v=G9Pq4X3YCSs).
- Listas: [Doblaje de Hora de Aventura](https://www.youtube.com/playlist?list=PLvuQzcKA3UUcD3F3hlaeCmhooSpQYbS49), [Marceline sings: Timeless songs](https://www.youtube.com/playlist?list=PLHo7CmBqY-EJ36VOk1q7SbRKr7rFTbalv).
- Facebook de la serie en latino: [«Marceline: Papi, te comiste mis papas»](https://www.facebook.com/HoradeaventuraCNLAT/videos/marceline-papi-te-comiste-mis-papas/458523794162928/).
- Facebook de HBO Max México: [«No hay doblaje más icónico que el de Hora de Aventura…»](https://www.facebook.com/HBOMaxMX/posts/no-hay-doblaje-m%C3%A1s-ic%C3%B3nico-que-el-de-hora-de-aventura-y-se-sabe-/854395177305162/).

### 12.3 TikTok (tendencias y actores)

Los cuatro con enlace de abajo se comprobaron en la **API oEmbed de
TikTok** (título y autor reales) ✅. Las vistas no se pueden contar
desde aquí ⚠️.

- «**Everything Stays**» es **viral en TikTok**: versiones, mezclas con
  «Drift Away» de Steven Universe y dúos de hermanos ✅
  ([búsqueda de TikTok](https://www.tiktok.com/discover/everything-stays-adventure-time-full)).
- **Rebecca Sugar** tiene TikTok y subió «Everything Stays»:
  [vídeo](https://www.tiktok.com/@rebeccasugar/video/7380076323168996650) ✅.
- **Evanescence (Amy Lee)** hizo su versión:
  [vídeo](https://www.tiktok.com/@evanescence/video/7008939931548568837)
  ✅ («One of my favorite #adventuretime songs ❤️❤️❤️ #everythingstays
  #marceline»).
- Isabel Martiñón en la Expomac de Veracruz:
  [vídeo](https://www.tiktok.com/@rebecavirgen/video/7434952138339536184).
- Entrevista a Karla Falcón (Dulce Princesa) en Festigame 2024:
  [vídeo](https://www.tiktok.com/@eldiariodelalquimista/video/7440244073505623352).
- «¿Por qué cambió la voz de Jake?»:
  [vídeo](https://www.tiktok.com/@acubick/video/7206541052713438469)
  («Por qué Jake el perro cambio de voz en las últimas temporadas de
  #horadeaventura? doblaje: José Arenas») ✅.

### 12.4 Análisis

- [«Marceline's Best Tunes, Ranked»](https://medium.com/the-dot-and-line/marceline-songs-adventure-time-ranked-f0e904443f9a) (Medium).
- [«Six Degrees of Rebecca Sugar: The Long Road to Bubbline»](https://www.thefandomentals.com/six-degrees-of-rebecca-sugar-the-long-road-to-bubbline-and-beyond/).
- [«Adventure Scrape: text mining on Adventure Time transcripts»](https://medium.com/towards-data-science/adventure-scrape-text-mining-on-adventure-time-transcripts-8a50d09c2b6d).
- Clip «Behind the Music» de la serie en [Internet Archive](https://archive.org/details/bliptv-20131014-143325-Cbr-AdventureTimeClip176) ⚠️ (archive.org cerrado).

---

## 13 · Videojuegos de la franquicia

Interfaz y retratos: ver §7.3 (la hoja «Mugshots» de DS y el menú de
«Card Wars», vistos). Lista (segunda pasada):

| Juego | Estudio, año, consola | Cómo se juega | Estado |
|---|---|---|---|
| **Hey Ice King! Why'd You Steal Our Garbage?!!** | WayForward (D3/Bandai Namco), **20-nov-2012**, DS y 3DS | historia escrita por **Pendleton Ward** con WayForward; mapa desde arriba y mazmorras de lado, como *Zelda II*; Finn y Jake a la vez (Jake en la mochila saca objetos); 4 zonas: Grass Lands, Candy Kingdom, Red Rock Pass, Ice Kingdom | ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time:_Hey_Ice_King!_Why%27d_You_Steal_Our_Garbage%3F!!), [Giant Bomb](https://giantbomb.com/wiki/Games/Adventure_Time_Hey_Ice_King_Whyd_you_steal_our_garbage), [Nintendo Life](https://www.nintendolife.com/reviews/ds/adventure_time_hey_ice_king_whyd_you_steal_our_garbage)) |
| **Explore the Dungeon Because I Don't Know!** | WayForward, 2013, PS3, Xbox 360, Wii U, 3DS | mazmorras en cooperativo, hasta 4 | ⚠️ ([Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time:_Explore_the_Dungeon_Because_I_Don%27t_Know!)) |
| **The Secret of the Nameless Kingdom** | WayForward, 2014 | tipo Zelda | ✅ |
| **Pirates of the Enchiridion** | Climax Studios, 2018 | aventura | ✅ |
| **Card Wars** | Kung Fu Factory / CN, 2014, iOS y Android; retirado en dic-2019 | cartas; Finn, Jake, BMO, Princesa, Marceline y Flama Princesa jugables | ✅ ([Adventure Time Wiki](https://adventuretime.fandom.com/wiki/Card_Wars_(application))) |
| **Card Wars Kingdom** | secuela móvil | cartas | ⚠️ (sólo tiendas de APK) |
| Apariciones en otros juegos | Fortnite, MultiVersus, LEGO Dimensions, Minecraft, Brawlhalla | ver §F | ✅ |

Lo de la primera pasada: el de 2012 tiene **más de 50 personajes** de las temporadas 1-3
y lugares como el Dulce Reino, el Reino Helado, el Espacio Grumoso y la
casa del árbol ✅ ([Gaming Nexus](https://www.gamingnexus.com/Article/Adventure-Time-Hey-Ice-King!--Whyd-you-steal-our-garbage!!/Item3804.aspx),
[Mash Those Buttons](https://mashthosebuttons.com/review/adventure-time-hey-ice-king-whyd-you-steal-our-garbage-review/)).
**La caja de diálogo** de los juegos sigue sin captura ⚠️ (sí los
retratos de DS y el menú de Card Wars). No los propongo como cuadro.
También existe **Card Wars** (el juego de cartas del episodio, hecho
juego real) ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Card_Wars)).

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todos reconocen

- «**¿Qué hora es? ¡Hora de aventura!**» ⚠️ (es la letra del opening, no
  un diálogo; no se encontró como frase exacta de un capítulo doblado).
- «**¡Matemático!**» y «**¡Algebraico!**» ✅.
- «**Bacon Pancakes**» de Jake ✅ (4×16).
- «**Papi, te comiste mis papas**»: la **Canción de las papas** ✅ (así se
  llama la pista 6 del disco en español, MusicBrainz + Facebook de CN
  Latinoamérica; la letra entera en latino ⚠️).
- **«I Remember You»**: el episodio que hace llorar; Marceline y Simón ✅.
- **«Bubbline»**: la pareja Marceline y Dulce Princesa, **hecha oficial**
  con el beso del final (10×13, ≈33:30) ✅.
- **Jake con modismos mexicanos** y la polémica del cambio de voz ✅ (§10.3).
- **«Everything Stays»** en TikTok ✅.
- El **bajo-hacha**: los fans lo **construyen de verdad** y lo modelan en
  3D ✅ (§3.5, §4.1).
- «**¡Oh por Glob!**» de la **Princesa Grumosa**: así se dice en latino ✅
  (§10.4).
- **La campaña por Karla Falcón**: los fans firmaron peticiones, hicieron
  un grupo de Facebook y se quejaron en foros hasta que **volvió a doblar
  a la Dulce Princesa** (T4, ep. 96) ✅ (§E). Para un servidor de doblaje,
  es el dato de oro: **el público latino defendió a su actriz**.
- **Bubbline, reconocida**: «Obsidian» fue **nominado a un GLAAD Media
  Award** ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Marceline_the_Vampire_Queen)).
  Es el hito de representación LGBTQ+ más citado de la serie.
- **BMO es el favorito del creador** ✅ (§9).
- La serie **sin censura** en Canal 2 (El Salvador) y Canal 5 (México):
  los fans comparan versiones ✅ (Doblaje Wiki).

### 14.2 Qué NO hacer (lo que un fan notaría)

- **El bajo sin forma de hacha**, con seis cuerdas o de guitarra normal:
  es un **hacha de doble filo con cuatro cuerdas y dos clavijas a cada
  lado** ✅.
- **Filos plateados** fuera de la temporada 1: desde la 2 son **rojos** ✅.
- Marceline **chupando sangre** o con colmillos de película: chupa **el
  color rojo** ✅, y sus colmillos son pequeños ⚠️. **Dos puntitos de
  mordida en el cuello** ⚠️ (de memoria).
- Marceline **caminando con los pies en el suelo** todo el rato: **flota** ✅.
- **Ojos grandes de anime**, sombras suaves, pelo con mechones
  realistas: la serie usa **ojos de punto**, línea fina y colores planos
  ✅ (§18).
- **Codos y rodillas marcados**: son **brazos de fideo** ✅.
- **Finn sin su gorro** (sólo se lo quita en momentos muy especiales) ⚠️.
- Nombres de España: «Princesa Chicle», «Rey Hielo», «Hora de Aventuras»
  ⚠️ (de memoria; el latino es **Dulce Princesa**, **Rey Helado**,
  **Hora de aventura** ✅).
- Poner a Marceline **alegre de colorines** en pleno día sin sombrero:
  **de día lleva sombrero de sol y guantes** ✅ (3×10).
- **Burbuja blanca genérica** (§7).
- Frases del doblaje **inventadas y presentadas como reales**: si la
  frase es mía, no se atribuye al doblaje.
- **Piel de Marceline gris oscuro** o azulada: en el color plano es casi
  blanca, **`#D8E7E7`** ✅ (§5.3). Y el **pelo negro puro**, no azulado.
- **Cambiar la voz o el nombre latino** de un personaje: el fandom se
  organizó para recuperar una voz (§E); con Finn y Marceline, que nunca
  cambiaron, es aún más sensible.
- Usar la **fuente de fans del logo** para texto en español: no trae
  bien ñ ni ¿ en Windows (§6.1).

---

## 15 · Poses analizadas por personaje

> **Segunda pasada**: primero van las poses **vistas en vídeo** (15.0),
> con minuto exacto y enlace. Las tablas de debajo son de la primera
> pasada: salen de las **acotaciones de las transcripciones** ✅ (qué
> hace) con **minuto estimado** ⚠️; la mano, la mirada y el gesto son de
> memoria ⚠️. Las de «Henchman», «Marceline's Closet» y «Slow Dance With
> You» **no tienen clip real** (buscadas en Dailymotion).

### 15.0 Vistas en vídeo, con minuto exacto ✅

**Marceline** (12 poses, 4 clips):

| # | Clip | Minuto | Qué hace | Sirve para |
|---|---|---|---|---|
| V1 | «Fry Song» | [0:00](https://www.dailymotion.com/video/x51arca?t=0) | flota **bocabajo tocando el bajo**, de espaldas a cámara | presentar el «estreno casero» |
| V2 | «Fry Song» | [0:32](https://www.dailymotion.com/video/x51arca?t=32) | primer plano, **ojos entornados, boca abierta**, canta triste | emocionar |
| V3 | «I'm Just Your Problem» | [0:16](https://www.dailymotion.com/video/x537pqr?t=16) | vuela hacia la puerta con **el bajo por delante** y sombrero | **anunciar**, entrar en escena |
| V4 | «I'm Just Your Problem» | [0:52](https://www.dailymotion.com/video/x537pqr?t=52) | **ceño fruncido, colmillos**, canta con fuerza | **regañar** |
| V5 | «I'm Just Your Problem» | [1:32](https://www.dailymotion.com/video/x537pqr?t=92) | apoyada en la puerta, **toca relajada** con el sombrero | pensar, calma |
| V6 | «I Remember You» | [0:24](https://www.dailymotion.com/video/xzt1l7?t=24) | de pie, **mano en la cabeza**, angustia | **pensar**, dolor |
| V7 | «I Remember You» | [1:00](https://www.dailymotion.com/video/xzt1l7?t=60) | sentada, **toca el bajo seria** con el Rey Helado en la batería | tocar en dúo |
| V8 | tráiler «Obsidian» | [0:16](https://www.dailymotion.com/video/x7xejon?t=16) | sentada en la cocina, **taza humeante** con la Princesa | conversar |
| V9 | tráiler «Obsidian» | [0:20](https://www.dailymotion.com/video/x7xejon?t=20) | sentada, **toca el bajo**, la Princesa cocina detrás | tocar en casa, **explicar** |
| V10 | tráiler «Obsidian» | [0:36](https://www.dailymotion.com/video/x7xejon?t=36) | **flota tocando** sobre un camino de piedra al Reino de Cristal | **avanzar**, presentar (la mejor nueva) |
| V11 | tráiler «Obsidian» | [1:08](https://www.dailymotion.com/video/x7xejon?t=68) | de pie, **bajo al hombro**, con la Princesa y dos figuras de cristal | **celebrar**, grupo |
| V12 | tráiler «Obsidian» | [1:24](https://www.dailymotion.com/video/x7xejon?t=84) | primer plano, **shock** | susto |

Y en arte oficial (hoja 1): **#36** de pie tocando en el huerto, **un
ojo guiñado** (la mejor «con su instrumento»); **#20** con sombrero,
guantes y botas; **#1** caminando en 4 poses.

**Los demás** (vistos):

| Personaje | Clip · minuto | Qué hace |
|---|---|---|
| Finn | «Fry Song» · [0:40](https://www.dailymotion.com/video/x51arca?t=40) | de pie, **audífonos**, levanta la grabadora |
| Finn | piloto · [6:00](https://www.dailymotion.com/video/x84oaz2?t=360) | vergüenza, mejillas rosas |
| Jake | «I'm Just Your Problem» · [0:04](https://www.dailymotion.com/video/x537pqr?t=4) | **corre tocando la viola** |
| Jake | «Jake the Starchild» · [1:39](https://www.dailymotion.com/video/x6gkz32?t=99) | sonrisa enorme de orgullo |
| Dulce Princesa | tráiler «Obsidian» · [0:16](https://www.dailymotion.com/video/x7xejon?t=16) | **taza humeante**, sentada a la mesa |
| Dulce Princesa | tráiler «Obsidian» · 1:12 | **conduce una moto** con Marceline detrás |
| Dulce Princesa | «I'm Just Your Problem» · [0:00](https://www.dailymotion.com/video/x537pqr?t=0) | sostiene el **aparato verde** de sonido junto a BMO |
| Rey Helado | «I Remember You» · [0:42](https://www.dailymotion.com/video/xzt1l7?t=42) | toca **la batería verde con «#1»** |
| BMO | «The More You Moe…» · [2:36](https://www.dailymotion.com/video/x3q931u?t=156) | contento, en brazos de su creador |

**Cuántas por personaje**: Marceline tiene **12 vistas** (más 13 de
transcripción); Finn, Jake y la Princesa **2-3 vistas** cada uno, BMO
**1**. Para ellos, el resto son las tablas de abajo, con minuto estimado
⚠️.

### Marceline

| # | Escena | Qué hace | Sirve para |
|---|---|---|---|
| 1 | 1×12 «Evicted!», ≈2:11 | **cuelga del techo** y sisea; ≈2:18 se presenta: «I'm Marceline the Vampire Queen» | **presentar** (su entrada más famosa) |
| 2 | 1×12, ≈2:31 | ríe («Calm down, weenies») y **enciende velas** | presentar con calma |
| 3 | 1×12, ≈2:40 | **chupa el rojo de una fresa** y se la da a Finn | gesto de marca |
| 4 | 1×22 «Henchman», ≈4:35 | «You know I eat the color red sometimes» y **guiña** | **regañar en broma** |
| 5 | 1×22, ≈6:49 | **toca el bajo en la fiesta**, la gente baila | **celebrar** |
| 6 | 2×01, ≈0:07-0:25 | **graba** la Canción de las papas con Finn | **explicar** el canal (estreno) |
| 7 | 3×10, ≈7:04 | toca el bajo y pregunta «what's a quaver?» | **pensar** / duda graciosa |
| 8 | 3×21, ≈6:05-6:36 | **en la cama**, toca el bajo, **enciende la grabadora**, **abre el cuaderno** y canta | **explicar**, íntimo |
| 9 | 4×25, ≈8:49 | canta **leyendo una nota** de Simón | **emocionar** |
| 10 | 10×07, ≈7:00 | **aparece entre niebla en el escenario**: «Hello, Hamburger Hills Cemetery!» | **anunciar un estreno** |
| 11 | «Obsidian», ≈15:25 | **apoyada en el bajo** con desgana | **esperar** / «aquí no» |
| 12 | «Obsidian», ≈18:47 | **se echa el bajo al hombro**: «Next up…» | **animar**, pasar a lo siguiente |
| 13 | «Obsidian», ≈33:37 | ojos rojos, **se vuelve murciélago**: «MY BASS!» | **regañar fuerte** (usar poco) |

**La mejor para presentar el canal**: la **V10** (flota tocando, vista en
1080p), la 10 (escenario, sin clip) o la 6 (grabando; vista como V1).
**Para la regla «nada de vida personal»**: la 4 (guiño burlón) o la 11
(desgana). **Para regañar**: V4. **Para pensar**: V6.

### Finn

| # | Escena | Qué hace | Sirve para |
|---|---|---|---|
| 1 | 2×01, ≈0:00 | **beatbox** para Marceline | acompañar, animar |
| 2 | 2×01, ≈9:17 | saca **un walkman** con la canción grabada | **enseñar un estreno** |
| 3 | 3×21, ≈5:00 | escribe **la nota** apoyado en Jake | **explicar** (escribe la regla) |
| 4 | 3×21, ≈7:41 | **pulgar arriba** a Jake | **aprobar** |
| 5 | 3×10, ≈8:41 | canta «My Best Friends in the World» y **reúne a la banda** | **celebrar** |
| 6 | 10×13, ≈42:39 | escucha al Hoyo Musical: «Yeah!» | **escuchar lo nuevo** |

### Jake

| # | Escena | Qué hace | Sirve para |
|---|---|---|---|
| 1 | 1×12, ≈5:56 | **toca la viola** y canta «home is where your heart is» | explicar con cariño |
| 2 | 3×10, ≈4:36 | viola en la banda | acompañar |
| 3 | 3×10, ≈6:42 | vuelve **vestido de punk**: «I came back for the music» | **presentar** con actitud |
| 4 | 4×16, ≈7:51 | canta **«Bacon Pancakes»** cocinando | chiste, relajar |
| 5 | 10×13, ≈37:15 | **se convierte en megáfono** | **anunciar** |
| 6 | 10×13, ≈42:39 | «Music is powerful, man» | **explicar** por qué importa la música |

### Dulce Princesa

| # | Escena | Qué hace | Sirve para |
|---|---|---|---|
| 1 | 3×10, ≈4:25 | **toca a BMO** como instrumento | explicar |
| 2 | 3×10, ≈6:52 | **dirige** con órdenes técnicas | **explicar reglas** (mandona) |
| 3 | 3×10, ≈6:35 | «I wanna be the lead» | tomar el mando |
| 4 | «Obsidian», ≈5:06 | ríe con Marceline, toma **la taza negra** | escena de pareja |
| 5 | «Obsidian», ≈35:55 | «your new song must be extra angry and sad» | **pedir algo nuevo** |
| 6 | 10×13, ≈37:00 | anuncia desde el cielo: «**Everyone! I need you all to harmonize**» | **anunciar a todos** |

### BMO

| # | Escena | Qué hace | Sirve para |
|---|---|---|---|
| 1 | 3×10, ≈6:52 | ejecuta «Sound Structure Alpha» (suena música) | **reproducir un estreno** |
| 2 | 3×10, ≈7:40 | **se incendia** (Marceline le había enchufado un hornillo) | chiste de «no hagas esto» |
| 3 | 10×13, ≈35:55 | **canta con Jake en brazos** | ternura |
| 4 | 10×13, ≈37:00 | «**My art is a weapon!**» | **celebrar** |

---

## 16 · Vestuario

### Marceline ✅ (salvo lo marcado)

- **Cambia de ropa en casi cada episodio**. Pendleton Ward lo explicó:
  «**girls own more than one outfit**» ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Marceline_the_Vampire_Queen),
  [Adventure Time Wiki: Outfits](https://adventuretime.fandom.com/wiki/Marceline/Outfits)).
- **La que más lleva** (la que todos reconocen): **camiseta gris de
  tirantes, vaqueros azules y botas rojas** («Evicted!», «The Duke»,
  «Power Animal»…) ✅. Vista entera en hoja 2 **#51** («Marceline
  Presentation», 1382×2136). En el tráiler de «Obsidian» vuelve la
  **camiseta gris** (0:20) ✅.

**Tres trajes medidos en la segunda pasada** (Pillow y `estilo.py`):

| Traje | Hex medido | De dónde |
|---|---|---|
| **«New Costume #1»**: vestido camisero azul grisáceo, sin mangas | tela **`#83A5BC`**, zapatos granate **`#8C284F`**, piel `#D8E7E7`, pelo `#000000` | [*model sheet* oficial, ep. 057]({W}3/34/Modelsheet_Marceline_-_New_Costume_-1.png) (hoja 1 **#9**). **El más fiable**: sin luz de escena |
| **Suéter a rayas rojo y oscuro**, cuello alto, manga larga | de noche: `#5F120D` y `#090B25`, piel `#D8E0E8` ([«S2e1 Drama bomb»]({W}8/85/S2e1_Drama_bomb.png)); en «Fry Song» 0:16: `#630515` y `#2C080C` | dos fuentes; los dos fotogramas están oscurecidos por la escena, de día sería más vivo |
| **Top rojo y sombrero de ala ancha** («I'm Just Your Problem») | top `#8C000C`-`#90000A`, sombrero **`#BBAB4C`** (luz) y `#75691D` (sombra), cinta `#4A7AA2` | fotograma 0:52 del clip oficial; el sombrero es **dato nuevo** (hoja 1 **#20**, hoja 9 **#391-392**) |
| Chaqueta gris oliva sobre camiseta, tocando | sin hex (no se separó la tela del fondo) ⚠️ | [«S7e7 Marceline playing ax bass»]({W}3/33/S7e7_Marceline_playing_ax_bass.png) |

- **Corrección**: la «más icónica» no es sólo la camiseta gris; el
  **suéter a rayas** con cuello alto también se repite mucho ✅ (imagen).
- Otra muy popular: **chaqueta corta rosa y morada, pantalón corto
  magenta y botas altas rosas**, a veces con **camiseta de rock** ⚠️ (una
  fuente la llama «la más icónica»).
- **De día**: **sombrero de sol y guantes** ✅ (3×10; visto en el clip
  oficial y en el *model sheet* «with sun resistant gloves, boots, hat»,
  hoja 1 **#20**). Siempre lleva **algo rojo** «por si acaso» (§C).
- «Obsidian»: **ropa de motorista**, en moto con la Princesa detrás ✅
  («full biker gear», ≈11:49).
- De niña: camiseta de tirantes verde, pantalón marrón morado, botas
  moradas oscuras; o camiseta rosa y peto azul ✅ (wiki, por búsqueda).
- **Pelo**: **negro puro** (`#000000`, medido dos veces) ✅, **lisísimo y
  larguísimo**, hasta las rodillas o más (visto en los *model sheets*,
  hoja 1 **#1**, **#9**) ✅.
- **Fijo**: **piel casi blanca con un toque menta, `#D8E7E7`** ✅
  (**corrige** el «gris azulado» `#A9B8C2` de la primera pasada),
  **orejas puntiagudas** ✅ (vistas en los *model sheets*), **dos marcas
  de mordida en el cuello** ⚠️ (de memoria).
- Bocetos de vestuario para el final, de **Tom Herpich** (1280×1673, en
  la wiki) ✅.

### Finn ✅ (medido en el *model sheet*)
Gorro blanco con **orejas de oso**, **camiseta azul `#018BCB`**, pantalón
corto azul oscuro, calcetines blancos altos, zapatos negros, **mochila
verde `#7BBB59`**, **piel durazno pálido `#FDE5DA`** ✅
([«Original Finn», 1467×2385](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/f/f3/Original_Finn.png), hoja 1 **#48**).
**Corrige** la «camiseta celeste» `#35A9E0` de memoria. Pantalón y
zapatos, sin medir ⚠️.

### Jake ✅ (medido)
Sin ropa; **amarillo anaranjado `#FEB925`** (40 % de la imagen),
**orejas caídas**, hocico claro ([«Jakesalad», 1700×2455](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/3/3b/Jakesalad.png),
hoja 1 **#45**). Coincide con lo que se decía de memoria.

### Dulce Princesa (medida a medias)
Piel y pelo **rosa chicle en dos tonos, `#ED8ACE` y `#F3BBFB`** (zonas de
luz) ✅ ([«Princess Bubblegum Duct Tape», 2880×1618](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/f/f5/Princess_Bubblegum_Duct_Tape.png),
hoja 1 **#43**). **Corona dorada** con gema azul ⚠️ (no se aisló un
píxel limpio). Vestido rosa; bata de laboratorio y gafas cuando hace
ciencia ⚠️. Es el personaje con **más vestuarios** de la serie ✅ (wiki);
muchos en hoja 2 **#67-93** (1920×1200).

### BMO ⚠️
Consola turquesa (`#6CC3B3`, de memoria: el rosa del fondo tapaba la
muestra), **pantalla con cara**, cruceta amarilla, botones de colores,
piernas y brazos finitos. Hoja 2 **#62** (BMO transformándose).

---

## 17 · Paisajes y fondos de pantalla

### 17.1 Fondos de pantalla de fans, con tamaño y autor (Wallhaven) ✅

Leídos en la API de Wallhaven (`purity=sfw`). **Son fan art**, no
oficiales: para mirar, no para pegar.

| Enlace | Tamaño | Autor | Favoritos | Qué es |
|---|---|---|---|---|
| [zxo8vg](https://wallhaven.cc/w/zxo8vg) | **3600×2400** | RaidMath | 40 | todo el elenco (Marceline, Princesa, Jake, Rey Helado, BMO, Lady Arcoíris) sobre fondo de Cartoon Network: **el mejor de conjunto** |
| [0wy167](https://wallhaven.cc/w/0wy167) | 1800×1000 | Oniofash | 52 | collage de Marceline, Simon y la Princesa |
| [45zpo5](https://wallhaven.cc/w/45zpo5) | 1639×1165 | Linez | 34 | Jake, Finn, la Princesa y Marceline juntos |
| [0wxpgp](https://wallhaven.cc/w/0wxpgp) | 1920×1036 | 8bitcartoon | 57 | Finn y Jake en **pixel art**: paleta reducida |

**Fondos oficiales** en alta, pensados como fondo de pantalla: **no
encontré** una página de descargas de Cartoon Network ⚠️. Lo oficial más
grande son el arte de los discos (§3.4), los *model sheets* (§3.7) y las
capturas de la wiki en 2880×1620 (§3.0).

**Paisajes con su luz y su hora** (vistos, §5.2): la casa de Marceline
por dentro (luz plana y cálida, rosa); la puerta de los círculos dorados
(tarde despejada); el Reino de Cristal (noche violeta y cian); el opening
(laguna helada, valle verde, cresta bajo tormenta). La casa del árbol en
3D con licencia CC BY: §4.1.

### 17.2 Lo de la primera pasada

- Lo que existe y conviene buscar desde un PC con red:
  - **Arte de los discos** (§3.4): la caja de Mondo (JJ Harrison), «Come
    Along With Me» y «BMO's Mixtape» (Jesse Balmer), «Obsidian» (Maya
    Petersen). Son **ilustraciones oficiales grandes y nuevas**.
  - **Key art de «Obsidian»** (§3.3).
  - **Cartelas de título** en Flickr (§3.1).
  - **Fondos pintados** en «The Art of Ooo» (§3.1).
  - Galerías de fans de la casa y la cueva: tableros de Pinterest
    [«Marceline's House»](https://www.pinterest.com/ideas/marceline's-house-adventure-time/950434038146/)
    (sólo para llegar a la fuente original, nunca como fuente final).
  - Una idea de fans para **LEGO de la casa-cueva de Marceline**:
    [LEGO Ideas](https://ideas.lego.com/product-ideas/8238723e-457a-45b2-894c-a13fca85eeda)
    (sirve para ver la casa en 3D) ⚠️.
- La hora del día: **noche o cueva** para Marceline ⚠️ (en vídeo también
  sale de tarde y en su casa rosa, §5.2); **tarde dorada** para la casa
  del árbol ⚠️.

---

## A · Estilo de dibujo y técnica, y cómo replicarlo (punto 18)

### A.1 Cómo se hacía de verdad

- **Dibujo a mano en papel**, luego **compuesto y pintado en digital**
  («hand-drawn on paper, which was then digitally composited and painted
  with digital ink and paint») ✅
  ([Wikipedia, «Animation»](https://en.wikipedia.org/wiki/Adventure_Time)).
- La **preproducción** (objetos, personajes, fondos) se hacía **sobre todo
  en Photoshop**, según **Phil Rynda**, diseñador principal ⚠️ (el dato de
  Photoshop sólo lo da Wikipedia citando una entrevista que no se
  encontró; que Rynda es el diseñador principal sí está en dos fuentes:
  Wikipedia y su [ficha de la wiki](https://adventuretime.fandom.com/wiki/Phil_Rynda),
  y sale en los créditos vistos, §2.9).
- La **animación** se hacía en **Corea del Sur** (**Rough Draft Korea** o
  **Saerom Animation**); el diseño y el color final, en **Cartoon Network
  Studios**, Burbank ⚠️ (una fuente).
- **Nick Jennings**, director de arte, dirigía el departamento y pintó
  muchas cartelas ✅ ([ficha](https://adventuretime.fandom.com/wiki/Nick_Jennings)).
  Fondos de la T1: **Ghostshrimp** y **Santino Lascano**; pintura: **Sue
  Mondt** y **Martin Ansolabehere** ⚠️ (una fuente).
- **Fred Seibert**, productor ejecutivo, comparó el estilo con **Felix
  the Cat** y los dibujos de **Max Fleischer** ⚠️ (una fuente).
- Las **cartelas de título**: papel viejo escaneado y **tramado de cómic
  viejo** (§3.2) ✅.

### A.2 Línea, color y sombra

- **Contorno negro limpio**, con un **ligero temblor de mano** (más grueso
  en las primeras temporadas) ⚠️ (análisis de fans que coinciden, no un
  *making of*).
- **Colores planos y saturados**, casi sin degradados: sombra de **1-2
  tonos** como mucho ✅ (visto: la casa de Marceline tiene luz plana sin
  sombras marcadas, §5.2).
- **Excepción**: en «Tierras lejanas» los fondos van **pintados con
  degradado** (el camino al Reino de Cristal, medido con `estilo.py`) ✅.
- **Formas simples y geométricas**: el cuerpo de Finn es casi una
  habichuela; **brazos de fideo** sin codos; **ojos de punto** ✅ (notas de
  dibujo de Ward, §18.1).
- **Filtros**: no se encontró ningún dato de grano, brillo o aberración
  en la serie (búsqueda «film grain post-production Adventure Time») ⚠️.
  El grano y el tramado que sí están documentados son los de las
  **cartelas** ✅ (§3.2).

### A.3 Encuadres y composición (lo visto en los clips)

No hay entrevista sobre planos y ángulos ⚠️. Lo que sí se vio:
- **Tristeza**: primerísimo primer plano de la cara, cantando («Fry Song»
  0:32; la lágrima de «I Remember You»).
- **Rabia**: primer plano, ceño y colmillos («I'm Just Your Problem» 0:52).
- **Pensar o dudar**: plano medio, **mano en la cabeza** («I Remember
  You» 0:24).
- **Viajar o avanzar**: plano general, el personaje **pequeño en el
  paisaje** (tráiler de «Obsidian» 0:36).
- **Celebrar o presentar en grupo**: plano medio largo, de pie, con el
  bajo al hombro (tráiler de «Obsidian» 1:08).
- **Un objeto clave**: plano detalle aislado (la **grabadora amarilla**
  en «Fry Song» 0:12; la **Polaroid** en «I Remember You» 1:36).

### A.4 Cómo reproducirlo en Photoshop

Propuesta práctica, coherente con el flujo real (papel → tinta digital →
color plano):
- Capa de **línea** aparte: pincel de tinta duro, opacidad 100 %, sin
  textura, **3-4 px** en un lienzo de 1500 px de ancho.
- **Color base debajo** de la línea, con el cubo de relleno (bordes
  duros, sin degradado). Colores de §5.3.
- **Sombra en una sola capa «Multiplicar»**, un solo tono, sin aerógrafo.
- Para una **cartela**: textura de **papel viejo** en «Multiplicar» o
  «Superponer», a baja opacidad, y un **tramado** encima (§B).

### A.5 Cómo reproducirlo en Blender

- **Contorno**: modificador **Solidify** con normales invertidas y grosor
  0,01-0,02 («casco invertido», funciona en Eevee), o **Freestyle** para
  línea automática ✅ (técnica documentada:
  [Blender Studio, Toon Character Workflow](https://studio.blender.org/training/toon-character-workflow/5859a5da1f47427e3fe82330/),
  [BlenderNation](https://www.blendernation.com/2020/02/06/how-to-make-a-toon-shader-with-dynamic-outlines/);
  genérica, no del estudio).
- **Sombreado**: un *toon shader*, o **Diffuse + ColorRamp** cortando la
  sombra en 1-2 tonos duros.
- **Luz**: una luz suave principal y poco más: la serie casi no tiene
  sombras proyectadas. En el Reino de Cristal, luz violeta con rebote cian
  (§5.3).
- **Modelos y rigs libres** con licencia leída en la API de Sketchfab
  (§4.1): el **bajo de Haxis** (CC BY), **Marceline de coffe0wolf** (CC
  BY, maniquí), **Finn de Agu.3D** (CC BY, 64 992 caras) o de **Nico
  Caraballo** (1 548 caras), **Jake de Mormont** (CC BY) y **la casa del
  árbol de gleksono** (CC BY).
- **Texturas encima**: sólo en objetos «reales» del mundo (cartón de la
  funda, papel), con material plano; ver §B.

---

## B · Texturas 2D (punto 19)

No es manga: **no hay tramas japonesas**. Sus equivalentes son:
- El **tramado (*dithering*) de las cartelas** sobre **papel viejo
  escaneado** (Phil Rynda, Paul Linsley, Nick Jennings) ✅ (§3.2).
- El **punteado de cómic** de los tebeos de BOOM!: color plano con sombra
  en trama, como el cómic americano de la época ⚠️ (descripción, sin
  página medida).
- **Patrones de ropa**: las **rayas** del suéter de Marceline (§16) y el
  **gorro de oso** de Finn. **Emblemas**: el logo de la serie
  ([1069×519](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/thumb/b/bd/Adventure_Time_logo.png)) ✅.

**Tramas y *halftone* libres**:

| Qué | Dónde | Licencia |
|---|---|---|
| 12 texturas de *halftone* desgastado | [Spoon Graphics](https://blog.spoongraphics.co.uk/freebies/free-pack-of-12-distressed-halftone-pattern-textures) | descarga gratis, sin registro ✅ |
| +35 texturas y patrones de *halftone* | [PhotoshopSupply](https://www.photoshopsupply.com/patterns-textures/halftone-texture) | gratis ✅ |
| Pinceles de *halftone* | [Brusheezy](https://www.brusheezy.com/free/halftone-texture) | **cambia de un pincel a otro** ⚠️: mirar cada uno |

**Papel, cartón, tela, madera y cuero reales** (ambientCG, **CC0**, sin
crédito obligatorio; licencia leída en su API) ✅:

| Uso | Textura |
|---|---|
| Papel viejo de cartelas, librito del disco, nota de Finn | [Paper001-006](https://ambientcg.com/list?type=Material&q=paper) |
| Funda de cartón del vinilo | [Cardboard001-004](https://ambientcg.com/list?type=Material&q=cardboard) |
| Tela de ropa (Finn, Marceline) | [Fabric081C, 061, 066](https://ambientcg.com/list?type=Material&q=fabric) |
| Mástil del bajo, muebles | [Wood092, 094, 095](https://ambientcg.com/list?type=Material&q=wood) |
| Botas de Marceline y Finn | [Leather026, 030, 037, 038](https://ambientcg.com/list?type=Material&q=leather) |

Con esto las tres capas están: **tramado** (arriba), **materiales
reales** (ambientCG, Poly Haven en §5.4) y **3D con licencia**
(Sketchfab, §4.1).

---

## C · Gustos y detalles de cada personaje (punto 20)

Todo sale de las fichas y curiosidades de la
[Adventure Time Wiki](https://adventuretime.fandom.com/wiki/Marceline) (wikitext leído por su API), con el
episodio que lo confirma. **Ninguna ficha trae altura** en cm: no se
inventa. *The Adventure Time Encyclopædia* (Martin Olson, 2013) tiene
fichas en la voz de cada personaje, pero **no se pudo leer** (la copia
de Scribd no cargó) ⚠️.

| | Marceline | Finn | Jake | Dulce Princesa | BMO | Rey Helado / Simon |
|---|---|---|---|---|---|---|
| **Comida** | **no bebe sangre: come el color rojo**; los **tomates** le dan sueños lúcidos («Marceline's Closet») ✅ | **pastel de carne** (*meatloaf*), en tres episodios ✅ | pay, hamburguesas, helado; **el chocolate lo mataría** ✅ | **espagueti** (se enfada si se le cae) ✅ | — | — |
| **Aficiones** | música (bajo-hacha), **baloncesto** («Simon & Marcy») ✅ | ser héroe; la nana de su madre adoptiva, que se sabe de memoria ✅ | **cocinar** (bacon pancakes, café, «Everything Burrito»), viola, beatbox ✅ | ciencia; toca la **trompeta** («Bad Timing») ✅ | sus juegos (es una consola, con juegos «clones» de Atari) ✅ | videojuegos y dibujos torpes de princesas en una computadora vieja ✅ |
| **Color favorito** | no consta; **siempre lleva algo rojo** «por si acaso» (para comérselo), salvo en «Red Starved» ✅ | **azul bebé** «de niño» («The Silent King») ✅ | — | **rosa** («The Real You») ✅ | — | — |
| **Lo que odia o le cuesta** | que la olviden; la inmortalidad (§8) | las escenas románticas (vomita, «Go With Me»); es **daltónico rojo-verde** («Red Starved») ✅ | — | bajo estrés **come de más** ✅ | llora si Finn se afeita la cabeza («Davey») ✅ | no recuerda por qué quiere una princesa |
| **Objeto que siempre lleva** | el **bajo-hacha** ✅; su osito **Hambo** | su **espada** (varias) y la **mochila**; la cajita de música de su madre adoptiva ✅ | — | su pájaro veloz **Morrow** para moverse ✅ | **su mando**, «BMO's prized possession» («What Was Missing») ✅ | la **corona** (poder y locura) ✅ |
| **Mascota** | **Schwabl**, un caniche zombi ✅ | — | — | — | — | — |
| **Cumpleaños / edad** | **27 de junio** ✅ (ficha); «mil años» | empieza con 12 ⚠️ | — | **827 años** ✅ | «VER. 2600», especie «110 VOLT-60 HERTZ SYSTEM» (ficha de un DVD, guiño a Atari) ✅ | — |
| **Cómo se ve** | «No soy mala; perdí de vista mi código moral» ⚠️ (traducción) | el «sheriff moral» de Ooo; sufre si no puede ayudar ✅ | el mentor sabio, aunque sabe que sus consejos no siempre sirven ✅ | la que todo lo sabe: «all magic is science» ✅ | «incapable of emotion» (no es verdad) ✅ | Simon: responsable de Marceline; el Rey: sólo sabe que «quiere una princesa» ✅ |
| **Detalle raro** | protector solar **FPS 10 000 000** («Marceline the Vampire Queen») ✅ | — | quizá disléxico ⚠️ | en situaciones límite **se come a gente-dulce** para «reponer biomasa» (lo confirmó el showrunner Adam Muto) ✅ | — | **tatuaje de pingüino** en el glúteo ⚠️ |
| **Altura** | «alta y delgada», más que la Princesa ⚠️ sin cifra | sin cifra ⚠️ | sin cifra ⚠️ | sin cifra ⚠️ | sin cifra ⚠️ | sin cifra ⚠️ |

Las casillas con «—» son datos que **no se encontraron** en las fichas.

---

## D · Por qué la gente la ama (punto 21)

### D.1 Premios ✅

**8 Primetime Emmy**, **1 Peabody**, **3 Annie**, **2 British Academy
Children's Awards**, un Motion Picture Sound Editors Award y un premio
*Kerrang!* ([Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time)).
«**Simon & Marcy**» (5×14) fue nominado al Emmy en 2013; el final, «**Come
Along With Me**», al Emmy Creative Arts en 2019
([Wikipedia: Ice King](https://en.wikipedia.org/wiki/Ice_King),
[Come Along with Me](https://en.wikipedia.org/wiki/Come_Along_with_Me_(Adventure_Time))).
«**Obsidian**», nominado al **GLAAD Media Award** ✅.

### D.2 Por qué conecta (la crítica) ✅

- **Crecer de verdad**: *Vox* (Emily VanDerWerff) la llamó «la mejor
  historia de crecimiento de esta era»; Finn pasa «de niño a casi
  hombre». *Comic Book Resources*: de «niño amable» a «joven noble».
- **Salud mental**: *Vulture* lee el arco del Rey Helado como una
  metáfora del **Alzheimer** y la soledad. *Teen Vogue* destaca a
  Marceline por venir de una **familia no tradicional** con emociones que
  «a veces reflejaban depresión».
- **Representación LGBTQ+**: la revista *Them* llamó a Marceline «uno de
  los mejores retratos de angustia bisexual» de la animación; su relación
  con la Dulce Princesa, canon en el final y ampliada en «Obsidian», es
  el ejemplo más citado de su época.
- **Imaginación pura**: humor fácil con temas serios (guerra nuclear,
  muerte, identidad); «una de las caricaturas más distintivas».

### D.3 Con quién se identifica el público ✅

- **Finn**: crece con su público; *Entertainment Weekly* lo compara con
  los niños que crecieron con Harry Potter. Hubo **una carroza de Finn en
  el desfile de Macy's de 2013**; Finn y Jake están entre los disfraces más
  vistos (*The Daily Beast*, 2019).
- **Simon / Rey Helado**: tragedia enorme más torpeza de todos los días;
  por eso es «el favorito de mucha gente» (*Vulture*).
- **Marceline**: adolescentes y jóvenes que se ven en su lado punk y en
  la tristeza bajo la fachada dura; y el público LGBTQ+, por su relación
  con la Princesa.

### D.4 Las escenas que hacen llorar

| Escena | Qué pasa y por qué duele | Música | Cómo está dibujada | Cómo reaccionó la gente |
|---|---|---|---|---|
| **«I Remember You»** (4×25, ≈8:49 en el episodio) | Marceline le canta a Simon **la carta que él le escribió** cuando aún era humano y se volvía loco por la corona. Él no la recuerda | «Remember You» / «Recordándote»: **omnichord y batería** del Rey Helado, bajo de ella | visto en el clip: **casa rosa, luz plana**; primer plano con **una lágrima**; plano detalle de una **Polaroid** de ella niña; **flashback entre ruinas** con Hambo ([clip](https://www.dailymotion.com/video/xzt1l7?t=96)) ✅ | *io9*: «una de las cosas más intensas que he visto en años»; se tiene por el giro de la serie en salud mental ✅ |
| **«Simon & Marcy»** (5×14, como lo numeran la wiki y §8; la parte de voz lo daba como 4×24 ⚠️) | Simon cuida a Marcy niña en el apocalipsis mientras pierde la cabeza | ⚠️ no consta | hoja 9 **#417-422** (ruinas, puente) y hoja 1 **#35** (moto) | nominado al Emmy; en los «10 mejores episodios» de *Geek.com* ✅ |
| **«Come Along With Me» / «Ven Conmigo»** (10×13) | el final: despedida de todo Ooo | «Come Along With Me» (Ashley Eriksson); «Time Adventure» | ⚠️ sin clip | crítica: «desgarrador», «extraño y triste y tonto y divertido». Reddit, r/adventuretime: «**I definitely cried on the last episode and my mom thought I was faking**» (**1186 puntos**) y «Just cried when finishing the last episode» (167) ✅ ([Arctic Shift](https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=adventuretime&title=cried&limit=15&sort=desc)) |
| **«Obsidian»** (2020) | Marceline y la Princesa, por fin juntas y felices; ella canta «Monster» | «Monster» | tráiler visto: violetas y cian, luz de atardecer al final ✅ | nominación GLAAD; «por fin, felices juntas» ✅ |

**Las que hacen reír**: «Bacon Pancakes» (4×16), el siseo y el guiño de
Marceline, «¡Oh por Glob!», Jake con modismos mexicanos (§14.1).
**Las que hacen gritar de emoción**: el beso del final (10×13) y el
«I am proud of my punk daughter!» de Hunson (10×07). Vídeos de reacción
con votos: no se pudieron ver (YouTube) ⚠️.

---

## E · Fan dubs y comunidad hispana (punto 22)

YouTube pide iniciar sesión desde el servidor y TikTok no da datos sin
JavaScript: **existen, pero las vistas y fechas no se pudieron
comprobar** ⚠️. Se citan con lo que sí se vio (título, canal, tema).

- **La campaña por Karla Falcón** ✅, el ejemplo más fuerte de la
  comunidad hispana: cuando cambiaron su voz de la Dulce Princesa por la
  de Claudia Urbán, los fans hicieron **peticiones firmadas** (en
  peticionpublica.es), un **grupo de Facebook** («Evitemos que cambien las
  voces…»), una queja en la wiki en español y un hilo en **McAnime**. Falcón
  **volvió en la T4, ep. 96, «Rey Gusano»** (Doblaje Wiki enlaza las
  fuentes).
- **Fandubs en YouTube** ⚠️ (vistas sin comprobar): «Hora De Aventura -
  Chico Malo (Fandub Español Latino)», «Hora de aventura "Parodia"
  (Fandub español latino)», «Hora De Aventura Demasiado Joven (Fandub
  Español Latino) Clip», «Muchachito malo | Hora de Aventura | Español
  latino - Fandub» y la serie **«Cómics de Hora de aventura (Fandub
  español)»**, del #2 al #7 al menos, la última de **septiembre de 2024**.
- **Fandub en TikTok** ⚠️: **@angelon_2002_fandubs**, escena de
  «**Estacas**» con el **Hierofante Vampiro** doblado por «Artista
  Galáctico», con #fandubcomunidad #fandoblaje #horadeaventura.
- **Comparar doblajes** ⚠️: **@whiderlin_hot** compara «**Soy tu
  problema**» en latino y en castellano (#horadeaventuralatino
  #horadeaventurascastellano).
- **Actores latinos en convenciones** ✅: Isabel Martiñón en la Expomac de
  Veracruz y en Starcon; Karla Falcón en Festigame 2024 (§10.2). José
  Arenas vuelve como Jake en «Misiones Secundarias» (2026).
- **Letras traducidas por fans** ✅: LyricsTranslate, Letras.com y Cifra
  Club traen «I Remember You» y «Everything Stays» en español.
- **La versión oficial cantada en español** existe (disco «Marceline
  Canta», 2019, §3.4): es la base sobre la que se hacen los covers ✅.
- **Memes hispanos**: los **modismos mexicanos de Jake** («¡Ay, Jojutla!»,
  «Nunca me hagan eso», §10.4) y la polémica de su cambio de voz ✅ (§10.3).
- **No encontré** un canal de fandub en español con cifras grandes y
  comprobables ⚠️. Quien tenga YouTube sin bloqueo: buscar «Hora de
  aventura fandub capítulo completo».

---

## F · Colaboraciones, figuras y cosplay (punto 23)

Fuente principal: la página **«References in other media»** de la wiki,
leída entera por su API, contrastada con prensa para fechas y precios.

### F.1 Videojuegos con personajes o pieles oficiales

- **Fortnite** ✅: Finn, Jake, Dulce Princesa y Marceline como **skins**
  (1500 V-Bucks cada uno, 3800 el lote), actualización **v34.30, abril de
  2025** ([ScreenRant](https://screenrant.com/fortnite-adventure-time-skins/),
  [Sportskeeda](https://www.sportskeeda.com/fortnite/how-get-finn-jake-princess-bubblegum-marceline-adventure-time-skins-fortnite)).
  **Toca el objeto del plan**: el **«Marcy's Ax Bass»** es pico **y
  también instrumento tocable en Fortnite Festival** («A family heirloom
  converted into a wicked bass guitar»), junto a un *keytar* de la
  Princesa y el «Candy Axe» ([Fortnite.gg](https://fortnite.gg/cosmetics?id=17683)).
  Mochilas: Chicle Espacial, BMO, Hambo. Segunda tanda (Fionna, Cake,
  Conde Limongrab, Rey Helado) el **15-ene-2026** ✅.
- **MultiVersus** ✅: Finn, Jake y un Guardia Banana jugables desde 2024;
  **Marceline** llegó el **20-dic-2024** (temporada 4)
  ([GameRant](https://gamerant.com/multiversus-marceline-adventure-time-release-date-price/)).
  El mapa «Tree Fort» es la casa del árbol. **Cerró sus servidores el
  30-may-2025** ⚠️ (sólo quedan vídeos).
- **LEGO Dimensions** (2016) ✅: *Level Pack* con Finn, *Team Pack* con
  Jake y la Princesa Grumosa (27-sep-2016) y ***Fun Pack* con Marceline**
  (18-nov-2016).
- **Minecraft** ✅: el logro «**Adventuring Time!**» (visitar todos los
  biomas) y el **«Adventure Time Mash-up Pack»** (mapa de Ooo, texturas y
  skins, **30-may-2017**); ese julio, el episodio cruzado «Diamonds and
  Lemons».
- **Brawlhalla** ✅: Finn, Jake y la Princesa como skins, más mapa y efecto
  de K.O. ([nota oficial](https://www.brawlhalla.com/news/what-time-is-it-adventure-time-in-valhalla-patch-3-44/)).
- **Xbox Live** (2012) ✅: 30 prendas para el avatar, con la corona del Rey
  Helado y **el bajo-hacha de Marceline**, de 1 a 4 dólares
  ([Polygon](https://www.polygon.com/2012/10/9/3480640/adventure-time-avatar-items-xbox-live)).
- Guiños ⚠️ (sólo la wiki): el baile de **Jinx** en *League of Legends*
  copia el que Jake le enseña a un escarabajo («Power Animal»); la skin
  «Galaxy Slayer Zed» cita casi igual al Lich; en *Skullgirls*, **Filia**
  recuerda a **Fionna**.

### F.2 Figuras oficiales (su pose es referencia 3D) ✅

- **Funko Pop! Marceline #31** (botas marrones) y **#301 con guitarra**
  (exclusivo de Hot Topic): **la referencia 3D más directa de Marceline
  tocando** ([#31](https://www.tcgplayer.com/product/135801/funko-pop-vinyl-adventure-time-marceline),
  [#301](https://www.tcgplayer.com/product/135786/funko-pop-vinyl-adventure-time-marceline-with-guitar)).
- **Funko Adventure Time × Minecraft**, Marceline, ligada al mash-up
  ([BoxLunch](https://www.boxlunch.com/product/funko-pop-adventure-time-x-minecraft-marceline-vinyl-figure/11442336.html)).
- LEGO Dimensions *Fun Pack* de Marceline (arriba).

### F.3 Cosplay y réplicas con materiales reales ✅

Para dar **volumen de verdad** al bajo en Blender:
- **MDF de ¼" y espuma aislante de ½"** a los dos lados, pegada con
  espray y lijada ([2StoryProps](http://2storyprops.blogspot.com/2013/03/marcelines-axe-bass-adventure-time.html)).
- Cuerpo de **pino** cortado con plantilla y mástil de **dos tablas de
  2×3"** atornilladas, paso a paso en
  [The RPF](https://www.therpf.com/forums/threads/marcelines-axe-bass-build-from-adventure-time.221761/),
  el foro de referencia de réplicas.
- Versión ligera, no tocable: **cartón piedra y goma EVA**, cuerdas de
  alambre de colgar cuadros ([Nerd Caliber](https://www.nerdcaliber.com/making-good-cosplay-great-marcelines-guitar-a-tutorial/),
  [Cosplay Sass](https://cosplaysass.wordpress.com/2019/02/20/marceline-axe/)).
- Réplica **tocable** en DeviantArt (kazesamurai1000, §3.5).

### F.4 Otros cruces ✅

- ***MAD Magazine* #520**: portada con Finn como Alfred E. Neuman.
- **Gaia Online** (2012): objetos virtuales y un evento en vivo con
  Pendleton Ward (22-mar-2012).
- Cameos en ***Steven Universe*** («Sadie's Song», un peluche que parece
  Gunter) y ***OK K.O.!*** (Finn y Jake en «Crossover Nexus»).
- **Cómic «Marceline and the Scream Queens»**: la banda de gira (§3.6).
- **Moda**: **no encontré** una colaboración de diseño con Vans, OPI o
  Uniqlo; sólo ropa con licencia en Hot Topic ⚠️. No se da por
  colaboración.
- Cafés temáticos o eventos en Latinoamérica: **no se buscaron** ⚠️.

---

## G · Obras parecidas y temas relacionados (punto 24)

### G.1 La familia de *Flapjack* ✅

**The Marvelous Misadventures of Flapjack** (Cartoon Network, 2008-2010)
es el semillero: Pendleton Ward fue guionista y *storyboarder* allí antes
de crear Hora de aventura ([SlashFilm](https://www.slashfilm.com/1581694/flapjack-cartoon-network-disney-nickelodeon-descendants/),
[Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time)). Del mismo
equipo salieron series de tono parecido (fantasía, humor y emoción):
- **Gravity Falls** (Alex Hirsch, *storyboarder* en Flapjack).
- **Over the Garden Wall** (Patrick McHale, *storyboarder* en Flapjack y
  **director creativo de Hora de aventura hasta la T2**).
- **Steven Universe** (Rebecca Sugar, *storyboarder* en Flapjack y luego
  guionista aquí; autora de las canciones de Marceline, §11).
- **Regular Show** (J. G. Quintel, director creativo de las 2 primeras
  temporadas).

### G.2 Influencias que reconoce Ward

- **Dungeons & Dragons**: «Writing for the show is a lot like playing
  DnD... I get all my dungeon crawls out in writing the show» ⚠️ (una
  fuente, cita directa: [The Mary Sue](https://www.themarysue.com/pendleton-ward-interview/)).
- **Hayao Miyazaki / *Mi vecino Totoro*** para los momentos bonitos en
  medio del humor; ***Home Movies*** y ***Dr. Katz*** por el diálogo
  relajado ⚠️ (Wikipedia, sin la entrevista original).
- Fred Seibert: **Felix the Cat** y **Max Fleischer** (§A.1) ⚠️.
- Las cartelas: novela *pulp*, D&D, Frank Frazetta, cine de artes
  marciales de los 70 (§3.2) ✅.

### G.3 Otras láminas del servidor que se le parecen

- **64 · Steven Universe**: misma autora de canciones y mismo aire;
  sólo tiene `partes/` por ahora. **No repetir** «personaje cantando con
  su instrumento» si su lámina va por ahí.
- **13 · Rick y Morty**: su biblia ya avisa de no repetir el «personaje
  dentro de una pantalla» del concepto C de esta (BMO).
- **57 · Coco**: también de música; marca #musica-nueva como **tomado por
  Hora de aventura** y usa otro canal.
- **09 · Mafalda**: su lámina de #sugerencias manda las peticiones de
  artistas a #musica-nueva. Si las dos se hacen, que el texto
  «pídelo en sugerencias» de aquí (§0) y el suyo casen.

---

## H · El mundo, la historia y sus símbolos (punto 25)

### H.1 Las reglas de Ooo, en cinco líneas ✅

(Wikitext de la wiki: [Mushroom War](https://adventuretime.fandom.com/wiki/Mushroom_War), [Land of Ooo](https://adventuretime.fandom.com/wiki/Land_of_Ooo).)
1. Ooo es **la Tierra, unos mil años después de la Guerra de los
   Champiñones**, un intercambio nuclear de finales del siglo XX o
   principios del XXI.
2. La bomba mutagénica que cayó sobre lo que fue Norteamérica **despertó
   al Lich** y **trajo de vuelta la magia**.
3. La humanidad casi desapareció; de las tribus que quedaron y de la
   mutación nacieron las razas nuevas (gente-dulce, elementales…).
4. Ooo se reparte en reinos: **Reino Helado, Dulce Reino, Condado de
   Limongrab, Reino Wildberry, Reino de Fuego, Reino de las Nubes**, y
   zonas sin reino como el Bosque Maligno. El **Espacio Grumoso** es otra
   dimensión.
5. Frederator publicó **dos mapas oficiales** con el documento de
   presentación: uno en blanco y negro de Ghostshrimp (más fiel a la
   pantalla) y otro a color.

### H.2 La historia por arcos

- **T1-5**: episodios sueltos, con pistas sobre el pasado del Rey Helado
  y el origen de Marceline ✅. Marceline aparece en «Evicted!» (1×12) ✅.
- **T6**: Finn busca a su padre humano ✅.
- **T7, «Estacas»** (8 episodios): el pasado vampiro de Marceline; hace
  las paces con lo que es ✅. Aquí suena «Everything Stays».
- **T8, «Islands»**: Finn, Jake, BMO y Susan cruzan el mar; Finn conoce a
  su madre ✅.
- **T9, «Elements»**: la magia elemental vuelve Ooo una distopía ✅.
- **T10, final**: la Princesa contra su tío Gumbald; Betty le quita la
  corona a Simon; beso de Marceline y la Princesa; «Come Along With Me» ✅.
- **Después**: «Tierras lejanas» (2020-2021, con «Obsidian» y «BMO»),
  «Fionna & Cake» (2023-2024) y «**Misiones Secundarias**» (2026) ✅.
- Fuente del detalle por temporada:
  [Wikipedia, temporadas 6-10](https://en.wikipedia.org/wiki/Adventure_Time_season_6)
  ⚠️ (una fuente para cada arco; los arcos sueltos también están en la
  wiki).

### H.3 Objetos y emblemas que un fan reconoce al instante

- **El bajo-hacha** de Marceline: el hacha de la familia Abadeer (§3.5) ✅.
- **El Enchiridion**: el manual del héroe, casi sagrado; del griego
  *encheiridion*, «lo que se lleva en la mano» ✅
  ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/WesternAnimation/AdventureTime),
  [Wikipedia](https://en.wikipedia.org/wiki/The_Enchiridion!)).
- **La corona del Rey Helado**: la hizo Urgence Evergreen; llevarla
  siglos **volvió loco a Simon** ✅ ([wiki](https://adventuretime.fandom.com/wiki/Ice_King%27s_crown)).
- **La Espada de Hierba** de Finn, y luego su brazo-espada: dos «eras» de
  Finn ✅ ([wiki](https://adventuretime.fandom.com/wiki/Grass_Sword)).
- **Hambo**, el osito rojo de Marceline, regalo de Simon ✅ (§2.4).
- **Card Wars**: el juego de cartas del episodio que se hizo juego real
  (§13) ✅.
- **BMO**: una consola viva que parodia al Game Boy (§7.1) ✅.

### H.4 Vocabulario propio

- **Ooo**; **Glob** (como «Dios»: «¡Oh por Glob!») ✅; **Nocheósfera**
  (*Nightosphere*, el inframundo de Hunson Abadeer) ✅
  ([wiki](https://adventuretime.fandom.com/wiki/Nightosphere)); **Espacio Grumoso**.
- «**¿Qué hora es? ¡Hora de aventura!**» (el opening) ⚠️.
- «**¡Matemático!**», «**¡Algebraico!**»: las muletillas del piloto y
  la T1, que luego se usaron menos ⚠️ (TV Tropes).
- **Dulce Princesa**, **Rey Helado**, **Hora de aventura** (en latino,
  sin «s»); no los nombres de España ✅ (§7.4).

---

## 18 · Guía para generar con IA (Firefly, Canva) — punto 17

> La IA sólo para **fondos, poses de apoyo o bocetos**. El personaje
> final, mejor redibujado o sacado de un fotograma real. Y todo lo que
> salga de la IA se compara con las referencias de §3.0 y §15.0.

### 18.1 El estilo en pocas palabras (lo que nunca cambia)

- **Línea**: contorno **fino y uniforme**, sin variación de grosor tipo
  pincel, con un leve temblor de mano ✅ (§A.2). Su color: la primera
  pasada decía «marrón o morado muy oscuro»; la parte de técnica dice
  «negro limpio» ⚠️ (ninguna lo midió). En la duda, **casi negro**.
- **Color**: **plano y saturado**; cuando hay sombra, **una sola mancha
  dura** (1-2 tonos) ✅ (§A.2, visto en la casa de Marceline).
- **Formas**: círculos, óvalos y triángulos; **brazos y piernas de
  fideo** «al dente», sin codos ✅ ([notas de Pendleton Ward, Acclaim](https://acclaimmag.com/culture/learn-draw-adventure-time-creator-pendleton-wards-detailed-occasionally-bizarre-notes/)).
- **Caras**: **ojos de punto negro** y **boca de una línea** o una
  curva ✅ (visto en el piloto, §8.2).
- **Fondos**: más detalle que los personajes; en «Tierras lejanas»,
  **pintados con degradado** ✅ (§5.2).
- **Luz**: plana y cálida en interiores; violeta y cian en el Reino de
  Cristal; tarde despejada en exteriores (§5.2).
- **Encuadre**: primer plano para tristeza y rabia; plano general con el
  personaje pequeño para viajar; plano detalle para un objeto (§A.3).

### 18.2 Marceline, rasgos fijos

- **Piel casi blanca con un toque menta, `#D8E7E7`** ✅ (medida; **no**
  gris: el `#A9B8C2` de antes era de memoria). **Pelo negro puro
  `#000000`**, lisísimo, hasta las rodillas ✅; flequillo partido ⚠️;
  **orejas puntiagudas** ✅; colmillos pequeños; **dos puntos de mordida
  en el cuello** ⚠️.
- **Flota**. Cuerpo largo y delgado (*model sheet* «Stock Night», hoja 1
  **#1**).
- Ropa por defecto: **camiseta gris de tirantes, vaqueros, botas rojas**
  ✅ (hoja 2 **#51**). Alternativa medida: vestido camisero **`#83A5BC`** y
  zapatos **`#8C284F`** (hoja 1 **#9**). De día, **sombrero mostaza
  `#BBAB4C`** con cinta `#4A7AA2` y guantes (hoja 1 **#20**).
- Siempre **algo rojo** en la ropa (§C).
- **El bajo-hacha**: hacha de doble filo **roja** (`#9E1B1E`-`#C22B2F`
  ⚠️), mástil de madera, **cuatro cuerdas**, **dos clavijas a cada lado**
  de la pala ✅ (hoja 1 **#5**, hoja 2 **#49**).

**Paleta para el *prompt*** (medida, §5.3): pared rosa `#F8AEC5`, techo
`#FBE0E8`, sillón `#D94344`; Reino de Cristal `#422D6B`, `#6A53A0`,
`#E1F7F9`, `#9055C3`; Finn `#018BCB`/`#7BBB59`/`#FDE5DA`; Jake
`#FEB925`; Princesa `#ED8ACE`/`#F3BBFB`.

### 18.3 Palabras que ayudan

`flat 2D cartoon, thin uniform outline, flat colors, simple dot eyes,
noodle limbs, whimsical post-apocalyptic fantasy, painted background,
gouache background, soft pastel palette, Cartoon Network 2010s style`
y, para el sitio: `small pink suburban house inside a cave, pink walls,
red armchair, flat warm light` (la casa por dentro, vista) o `purple
crystal peaks, cyan crystal tower, stone path, violet night` (el Reino
de Cristal, visto). La cueva: `cave with stalactites, lagoon, candles,
night` ⚠️ (de memoria).

Para Marceline: `pale mint-white skin, pure black very long straight
hair, pointed ears, floating in the air, playing a double-bladed battle
axe shaped bass guitar, 4 strings, red blades`.

Para el título: `vintage paper border, halftone dithering, pulp
paperback cover, hand-lettered title` (el estilo de las cartelas, §3.2).

### 18.4 Palabras que lo estropean

`anime, manga, big eyes, detailed shading, cel shading with gradients,
realistic, 3D render, glossy, Pixar`, `vampire blood, gore` (Marceline
**no** es de sangre), `grey skin, blue skin` (sale gris), `electric
guitar` (sale una guitarra normal: pedir **`double-bladed battle axe
shaped bass guitar, 4 strings`**), `speech bubble` (la serie no usa
globos, §7).

### 18.5 Qué referencias usar

- **De estilo**: los *model sheets* oficiales (hoja 1 **#1**, **#9**,
  **#48**, **#45**), el arte de los discos (§3.4) y las cartelas (§3.2).
- **De pose**: hoja 1 **#36** (tocando de pie, guiño), hoja 2 **#51**
  (cuerpo entero sobre blanco), hoja 9 **#393** (cantando sobre la
  puerta) y **#396** (dúo); en vídeo, las **V1, V3, V10 y V11** de §15.0.
- **Del objeto**: hoja 1 **#5** y hoja 2 **#49**; en 3D, el bajo de
  **Haxis** (CC BY) o el de Yogensia (§4.1); réplicas reales (§F.3).
- **De luz para Blender**: el [HDRI Cave Wall](https://polyhaven.com/a/cave_wall)
  (§5.4) y la paleta medida (§5.3).

### 18.6 Vocabulario de gestos (para la IA de imagen)

No es anime: **no hay gotas de sudor, venas ni fondos de emoción** de
manga. Lo que usa la serie (visto, §8.2):
- **Vergüenza**: óvalo **rosa en las mejillas**, boca en rayita, ojos de
  punto muy abiertos (Finn, piloto 6:00).
- **Llanto**: cabeza atrás, dientes apretados en **mueca triangular**,
  **una sola lágrima** (Marceline, «I Remember You»).
- **Rabia**: ceño fruncido, **colmillos**; en extremo, **ojos rojos** y
  forma de **murciélago o monstruo** (hoja 1 **#15**, §8).
- **Miedo o nervios**: ojos muy redondos con brillo blanco, **manos juntas
  contra el pecho** (la Princesa, 2:12).
- **Alegría**: ojos enormes, sonrisa ancha de **dientes cuadrados** (Jake,
  1:39); **ojos cerrados en dos curvas** (BMO, 2:36).
- **Burla**: **guiño** (Marceline, hoja 1 **#36**; «[Winks]», 1×22).
- **«Chibi»**: la versión simplificada existe en los retratos del juego
  de DS (§7.3).

### 18.7 Para una IA de texto: cómo escribir en su voz

**Marceline**: burlona, tranquila, frases cortas; llama «**weenies**» a
Finn y Jake; presume sin esfuerzo; **sisea** cuando se enfada; cuando se
pone seria, baja la voz y va al grano. Grita poco: cuando se enfada de
verdad, **sisea y se transforma**.
**Finn**: todo con **¡!**; «**¡Matemático!**», «**¡Algebraico!**»;
caballeroso («m'lady»); heroico y rápido (3,49 palabras/s, §8.4).
**Jake**: relajado, consejero, **modismos mexicanos** en el doblaje
clásico («¡Ay, Jojutla!», «Nunca me hagan eso»); «hermano».
**Dulce Princesa**: correcta, mandona, técnica («triplet quavers in
mixolydian mode»); juguetona sólo con Marceline.
**BMO**: niño seguro de sí mismo, a veces **en tercera persona**, risa
larga («¡Jajajajajaja!»).
**Princesa Grumosa**: «**¡Oh por Glob!**».

**Frases reales por emoción** (en latino, oídas en las muestras de
Doblaje Wiki, §10.4, ✅; en inglés, de las transcripciones, con mi
traducción):

| Emoción | Frase | Quién, fuente |
|---|---|---|
| Alegre | «**¡Los veo en el dulce reino! ¡Esta noche!**» | Dulce Princesa, muestra de Doblaje Wiki ✅ |
| Alegre | «¡Jajajajajaja! ¡Juguemos a policías y ladrones!» | BMO, muestra ⚠️ (dos palabras reconstruidas) |
| Alegre | «**¡Matemático!**» | Finn ✅ |
| Enfadada | «¿Qué estás haciendo? No puedes estar aquí. **Ash no quiere que salga con mortales**» | Marceline, muestra ✅ |
| Enfadada | «[Eyes turn red] My bass. **MY BASS!**» («¡Mi bajo!») | Marceline, «Obsidian» ≈33:37, transcripción |
| Enfadado (villano) | «¡La hora es suya, pero el día será mío!» | Rey Helado, muestra ✅ |
| Explicando | «Tienes razón, sólo hay una forma de salir. […] No traten de convencerme» | Finn, muestra ✅ |
| Explicando | «Music is powerful, man. It speaks to a primal pit in our brains» («La música es poderosa, viejo») | Jake, 10×13 ≈42:39, transcripción |
| Explicando | «I wrote this next song about a fisherman» («Esta canción la escribí sobre un pescador») | Marceline, 1×22 ≈6:35, transcripción |
| Animando | «**Estoy para ti, hermano.** […] **Todo estará bien. Vayamos de compras**» | Jake, muestra ✅ |
| Animando | «Los amigos se ayudan siempre, ¡SIEMPRE!» | Finn ⚠️ (una fuente) |
| Animando | «I've been working on a new song myself… Would you like to hear it?» («Tengo una canción nueva. ¿Quieren oírla?») | el Hoyo Musical, 10×13 ≈43:04, transcripción |
| Triste | «But you ate them, yeah, you ate my fries… and I cried» | Marceline, subtítulo del clip «Fry Song» 0:28 ✅ (inglés) |
| Triste | «I was so afraid something bad would happen to you, and I wouldn't be there» | Marceline, 10×13 ≈33:06, transcripción |

**Cómo exagera**: Marceline con **siseo y transformación** más que
con gritos; Finn con **mayúsculas y ¡!**; Jake con **modismos y risas**; la
Princesa con **palabras técnicas**. **Puntuación latina**: ¿? y ¡!
siempre, y «Hora de aventura» sin «s».

---

## 19 · Tres conceptos para la lámina de #musica-nueva

Los tres usan los textos de §0. Las frases «en la voz de la serie» son
**traducción mía**, no del doblaje (no la encontré). Recortes siempre por
`v3/integrar.py` y comprobados a 1:1.

> **Segunda pasada**: los tres conceptos se mantienen, pero ahora con
> **imágenes vistas** (número de hoja y minuto de vídeo), **colores
> medidos** y **modelos 3D con licencia leída**. Lo que cambió va marcado
> «Nuevo».

### Concepto A — «El estreno en la caja» (Marceline en su casa)

- **Objeto y sitio**: sobre **el sofá de la casa de Marceline**, dentro
  de la cueva (§5.1), **una caja de discos abierta**, inspirada en la
  **caja real de Mondo** (§3.4): dentro, **un LP de 12"**, **un 10"**,
  **un single de 7"** y **un casete**. **El bajo-hacha** apoyado en el
  brazo del sofá. Velas en la pared. Por la ventana, la **laguna** con
  reflejos azules.
  - En Blender: caja de cartón con tapa, vinilos de colores (amarillo,
    azul oscuro y rosa, como los de Mondo), casete, el bajo (**Nuevo**:
    modelo de **Haxis, CC BY**, o el de Yogensia, §4.1), sofá sencillo.
    Cartón **Cardboard001-004** y madera **Wood092** de ambientCG (§B).
  - **Nuevo**: junto a la caja, **la grabadora amarilla** con el cable
    enchufado, la de «Fry Song» (visto, 0:12): el objeto con el que ella
    graba sus estrenos.
  - **Nuevo, colores medidos**: pared **`#F8AEC5`**, techo `#FBE0E8`,
    sofá rojo **`#D94344`** (§5.3). Fotogramas del sitio: hoja 9 **#385**
    y **#386** (el sofá rojo).
- **Personaje**: **Marceline flotando** encima de la caja, **tumbada en
  el aire boca abajo**, con un disco en la mano (pose de §15 n.º 2-3:
  relajada, burlona). Referencia de pose: «Evicted!» ≈2:31 y «Marceline's
  Closet» ≈8:41 (flota sobre la cama). **Nuevo, vista en vídeo**: la
  **V1** de §15.0 («Fry Song» [0:00](https://www.dailymotion.com/video/x51arca?t=0),
  flota bocabajo tocando) y el **guiño** de hoja 1 **#36**. Piel
  **`#D8E7E7`**, pelo negro puro, camiseta gris (hoja 2 **#51**).
- **Cómo habla**: **no hay globo**. Su frase va **escrita con rotulador
  en la hoja de letras** que asoma de la caja, con **Rock Salt**:
  «**Sólo lo que acaba de salir. Lo demás, pa' otro lado.**» (mía).
- **Dónde va cada texto**:
  - **Tapa de la caja**, con letras gorditas (**Chewy**): **Música nueva**.
  - **Pegatina redonda** en el plástico de la caja: **Aquí sólo entran estrenos**.
  - **Galletas** (el centro de cada disco): **Disco** (LP de 12"),
    **EP** (10"), **Single** (7"). El casete, sin texto o con «demo».
  - **Pegatina de advertencia** en una esquina, como «Parental
    Advisory» pero hecha a mano: **Nada de vida personal**.
  - **Nota de Finn a lápiz** pegada con cinta en la tapa (**Gochi
    Hand**), como la del 3×21: **¿Quieres un artista? Pídelo en sugerencias**.
- **Para que no quede plano**: **vela desenfocada** en primer plano;
  el **mástil del bajo cruza la imagen** por delante de la caja; luz
  **cálida de vela** desde un lado y **luz fría de la laguna** por la
  ventana del otro (la laguna, de memoria ⚠️); un vinilo **medio fuera de
  la funda** proyectando sombra. Dentro de la casa la luz de la serie es
  **plana y cálida** (visto): que la vela sea el único acento.
- **Lámina 2** (si se quiere explicar cómo publicar): la **contraportada
  de la caja**, con los campos del mensaje como si fuera la **lista de
  canciones** (artista, título, tipo, fecha, enlace). **Los campos los
  tiene que confirmar el dueño**: no están en el inventario.

### Concepto B — «Esta noche toca Marceline» (el concierto del cementerio)

- **Objeto y sitio**: el **escenario del Anfiteatro Fantasma** del
  cementerio de Hamburger Hills (10×07, §2.5). En el suelo del
  escenario, **la lista de canciones pegada con cinta** (setlist en
  papel, escrita con rotulador) y **un pedal y un amplificador**. Detrás,
  **niebla** y lápidas. Delante, **siluetas de fantasmas** del público.
  - En Blender: tablas del escenario, amplificador (caja con rejilla),
    papel arrugado con cinta, niebla volumétrica y un foco.
- **Personaje**: **Marceline apareciendo entre la niebla** con el bajo
  colgado (pose de §15 n.º 10, 10×07 ≈7:00), un brazo arriba saludando al
  público. Alternativa: **echándose el bajo al hombro** («Obsidian»
  ≈18:47) para «lo siguiente». **Nuevo, vistas en vídeo**: **V3** (entra
  volando con el bajo por delante, [0:16](https://www.dailymotion.com/video/x537pqr?t=16))
  y **V11** (de pie, bajo al hombro, [1:08](https://www.dailymotion.com/video/x7xejon?t=68));
  para cantar con fuerza, **V4** (0:52). ⚠️ El escenario del cementerio
  **no tiene clip real**: niebla, foco y lápidas son de la transcripción.
- **Nuevo, variante con sitio visto**: el mismo concierto **sobre la
  puerta de los círculos dorados** (3×10, hoja 9 **#393**, luz de tarde),
  o **flotando hacia el Reino de Cristal** (V10, paleta `#422D6B`,
  `#E1F7F9`, `#9055C3` medida).
- **Cómo habla**: su saludo va **en el cartel del concierto** pegado a
  una lápida (cartel punk, **Bungee**), y la frase del personaje, **en la
  setlist**, con su letra (**Permanent Marker**): «**¡Hola, cementerio!
  Esta noche, sólo temas nuevos.**» (mía, sobre «Hello, Hamburger Hills
  Cemetery!»).
- **Dónde va cada texto**:
  - **Cartel del concierto** (en la lápida): **Música nueva** (grande) y
    debajo **Aquí sólo entran estrenos**.
  - **Setlist en el suelo**: tres líneas numeradas **1. Disco 2. Single
    3. EP**.
  - **Pegatina en el amplificador**: **Nada de vida personal**.
  - **Entrada de concierto** que sostiene un fantasma en primer plano:
    **¿Quieres un artista? Pídelo en sugerencias**.
- **Para que no quede plano**: **cabezas de fantasmas** de espaldas en
  primer plano, desenfocadas; **contraluz del foco** atravesando la
  niebla; el **mástil del bajo** sale del encuadre hacia el espectador.
- **Tono**: noche, verdes y morados, pero **divertido**, no de terror
  (el público son fantasmas simpáticos y Hunson aplaude).

### Concepto C — «La mixtape de BMO» (la casa del árbol)

- **Objeto y sitio**: **BMO** sobre la mesa de la **casa del árbol** de
  Finn y Jake, con **un casete saliendo de su ranura** y **un vinilo
  apoyado** al lado, como la portada real de «**BMO's Mixtape**» (§3.4).
  BMO es un objeto que se puede modelar en Blender (una caja con
  pantalla y botones).
- **Personajes**: **BMO** en la mesa; **Finn** haciendo beatbox y
  **Jake con su viola** detrás (poses de §15: Finn 1, Jake 2), escuchando
  como al final de la serie («Would you like to hear it?» «Sure!»
  «Yeah!», 10×13 ≈43:04). Marceline puede asomar flotando por la ventana
  con el bajo, para que la protagonista siga en la lámina. **Nuevo, vistas
  en vídeo**: Finn **con audífonos levantando la grabadora** («Fry Song»
  [0:40](https://www.dailymotion.com/video/x51arca?t=40)) y Jake
  **corriendo con la viola** («I'm Just Your Problem» [0:04](https://www.dailymotion.com/video/x537pqr?t=4)).
  Colores medidos: Finn `#018BCB`/`#7BBB59`, Jake `#FEB925`.
- **Nuevo, en 3D con licencia CC BY** (§4.1): **la casa del árbol entera**
  (gleksono), **BMO** (featbear o ezgibakim), **Finn** (Agu.3D) y **Jake**
  (Mormont). BMO: **parodia de Game Boy** (§7.1), su «edad» «VER. 2600».
- **Cómo habla**: **en la pantalla de BMO**, con letra de píxel
  (**VT323**): «**¿QUIEREN OÍRLA? ES NUEVA.**» (mía, sobre la frase del
  Hoyo Musical).
- **Dónde va cada texto**:
  - **Pantalla de BMO**: **Música nueva** y, debajo, su frase.
  - **Etiquetas del casete y de los discos**, escritas a mano:
    **Disco**, **Single**, **EP**.
  - **Nota de Finn** pegada en la pared: **Aquí sólo entran estrenos**.
  - **Nota de Jake** debajo, con otra letra: **Nada de vida personal**.
  - **Flecha pintada** en una tabla hacia la puerta: **¿Quieres un
    artista? Pídelo en sugerencias**.
- **Para que no quede plano**: la **voluta de la viola** de Jake en
  primer plano; **luz de tarde dorada** por la ventana redonda (de
  memoria ⚠️); la pantalla de BMO **ilumina** la cara de Finn.
- **Ojo** (§G.3): Rick y Morty ya evita repetir «un personaje dentro de
  una pantalla» por este concepto; aquí la pantalla **es** el personaje
  (BMO), así que no choca.

### ¿Cuál primero?

- **A** es el más fiel al plan (bajo + discos) y el que mejor explica
  «disco, single, EP» con **objetos reales de la franquicia**.
- **B** es el más espectacular y el que más dice «estreno»: un concierto.
- **C** es el más tierno y el que menos depende de Marceline; útil si la
  lámina de otro canal ya la usa. Ahora es el que tiene **más 3D con
  licencia** (casa del árbol, BMO, Finn y Jake).
- Recomendación tras la segunda pasada: **A**, porque todos sus sitios,
  colores y poses ya están **vistos y medidos**; B tiene el escenario sin
  fotograma.

---

## 20 · Lo que no pude verificar

### 20.1 Lo que se resolvió en la segunda pasada (antes → ahora)

- «Ninguna imagen vista» → **1188 imágenes en 13 hojas**, 3 aquí, miradas
  (§3.0); *model sheets* y concept art de «Obsidian» vistos (§3.7).
- «Minutos estimados» → **4 escenas, el opening y los créditos vistos**
  con minuto exacto (§2, §12.0, §15.0).
- «Ninguna frase latina de Marceline» → **una frase real oída** en la
  muestra de Doblaje Wiki, y otras 5 de Finn, Jake, la Princesa, el Rey
  Helado y BMO (§10.4).
- BMO latino y directores: **Doblaje Wiki leída por su API** más segunda
  fuente (§10.1, §10.2).
- Fecha del disco «Marceline Canta»: **25-oct-2019** (MusicBrainz).
- Licencias 3D: **leídas en la API de Sketchfab** (§4.1).
- Colores: **medidos** en *model sheets* y fotogramas (§5.3, §16).
- Fuente de fans del logo: **abierta con fontTools** (sólo Mac Roman,
  §6.1).
- «¡Oh por Glob!»: **confirmado** de la Princesa Grumosa (§10.4).

### 20.2 Lo que sigue sin verificar ⚠️

- **Encuesta oficial de popularidad** con números: no la encontré (ni en
  español ni en inglés); Ranker da 401.
- **Quién canta** a Marceline en cada temporada (Claudia Urbán, Patty
  Urbán, Carla Cerda): una sola fuente (Doblaje Wiki); la parte de voz no
  lo repasó.
- **Frase latina** de «Thanks for helping me record», «I'm Marceline the
  Vampire Queen» y la del Hoyo Musical; **episodio** de cada una de las 6
  muestras de audio.
- **Estudio de «Misiones Secundarias»** (Iyuno México, Miguel Ángel
  Leal): una sola fuente.
- **La cueva de Marceline** y **el Anfiteatro Fantasma** (10×07): sin
  clip real; su luz y su paleta siguen de memoria. Tampoco «Henchman» ni
  «Marceline's Closet».
- **La lágrima de «I Remember You»**: las partes no coinciden en el
  segundo (≈1:18, §2.4).
- **Colores sin medir**: turquesa de BMO, corona de la Princesa, filos
  del bajo en luz de día, vaqueros, casa por fuera, cueva.
- **Las cajas de diálogo** de los videojuegos (sí los retratos de DS y el
  menú de Card Wars).
- **6 modelos 3D del bajo** sin campo de licencia en la API; el de
  cuxilrodas es «Free Standard» (no CC).
- **Vistas y fechas** de fandubs de YouTube y TikTok.
- **Caras por emoción**: 7 de 25 combinaciones vistas (§8.2).
- **«El sicario»** = «Hitman» (3×04): deducción mía.
- «Simon & Marcy»: 5×14 (wiki) o 4×24 (parte de voz).
- La entrevista original de **Phil Rynda** sobre Photoshop; *The
  Adventure Time Encyclopædia* (no cargó).
- **Las 3 intros de miniserie** (Islands, Stakes, Food Chain): existen y
  se sabe su duración; no se miraron.

---

## Cumplimiento del encargo

✅ hecho · ⚠️ a medias (se dice qué falta) · ❌ no hecho. Estado tras la
segunda pasada del equipo (25-26 sep 2026).

| Punto de ENCARGO.md | Dónde | Estado | Por qué |
|---|---|---|---|
| 1 · Arte oficial variado | §3, §3.0, §3.7 | ✅ | 1188 imágenes de la wiki en 13 hojas (3 aquí, miradas y numeradas); *model sheets* con ficha de producción, bocetos de Tom Herpich y concept art de «Obsidian» vistos; discos, libros y cómics con fuente. El póster de «Obsidian» y las portadas de «Scream Queens», sin ver. |
| 2 · Fotogramas de escenas icónicas | §2, §2.9, §12.0 | ⚠️ | 4 escenas, el opening y los créditos vistos con minuto exacto y `?t=`. Sólo el opening y el tráiler de «Obsidian» están en **1080p**; el resto en 720p (Dailymotion; YouTube pide iniciar sesión). El concierto del cementerio, «Henchman» y «Marceline's Closet», sin clip. Los fotogramas 1920×1080 de la wiki no traen minuto. |
| 3 · Fan art y 3D con licencia | §4, §17.1 | ✅ | 18 modelos de Sketchfab con licencia leída en su API (el bajo de Haxis es CC BY; el de cuxilrodas no es CC); casa del árbol en 3D; fan art con autor. Otros 6 bajos sin campo de licencia (dicho). |
| 4 · Sitios, luz, paleta y texturas | §5 | ⚠️ | Casa de Marceline por dentro y Reino de Cristal con hex **medidos** en fotogramas; luz vista; texturas CC0 con nombre. **La cueva y el Anfiteatro Fantasma siguen de memoria** (sin clip). |
| 5 · Tipografía por uso | §6 | ✅ | Tabla de una letra por uso; la fuente de fans del logo abierta con fontTools (sólo Mac Roman: no para español) y 6 letras libres comprobadas otra vez; letrista de BOOM! con dos fuentes. La letra de los créditos no se identificó. |
| 6 · Cómo hablan en pantalla | §7 | ✅ | Sin globos: papel escrito a mano (la nota de Simón vista, hoja 9 #408), cuaderno, cartelas con tramado, pantalla de BMO (parodia de Game Boy, dos fuentes) y la letra grabada en el vinilo. Los globos de BOOM!, sin ver una página. |
| 7 · Personajes y popularidad | §8, §9 | ⚠️ | Marceline: BOOM!, CN UK «Character of the Week», *The Guardian*; Rey Helado: *Vulture*; BMO: favorito de Ward. **No hay encuesta con números**: la oficial no la encontré y Ranker dio 401. |
| 8 · Doblaje latino y frases | §10 | ⚠️ | Reparto, estudios, directores y traductores leídos en la API de Doblaje Wiki, los principales con segunda fuente. **6 frases textuales oídas** en audios oficiales de la wiki, pero **sin episodio ni minuto**: no hay clips oficiales doblados en Dailymotion y YouTube bloquea. Cantantes de Marceline, una fuente. |
| 9 · Música y sonido | §11 | ⚠️ | Compositores, autora de las canciones, disco en español con duraciones (MusicBrainz), de qué trata «Everything Stays» (fuente primaria), variantes de la intro. No se buscó un efecto de sonido concreto; la serie no rotula onomatopeyas. |
| 10 · Vídeos y tendencias con minuto | §12 | ⚠️ | 9 clips de Dailymotion vistos con minuto y 4 TikTok comprobados por oEmbed. Los vídeos de YouTube (análisis y clips latinos) **siguen sin mirar**; vistas de TikTok sin contar. |
| 11 · Videojuegos | §7.3, §13 | ⚠️ | 7 juegos con estudio y año; retratos de DS y menú de Card Wars vistos y medidos; 5 juegos con cruce (§F). **La caja de diálogo** de ninguno se vio. |
| 12 · Lo que ama el fandom y qué no hacer | §14 | ✅ | Memes, «¡Oh por Glob!» confirmado, campaña por Karla Falcón, GLAAD; lista de errores ampliada con lo medido (piel, pelo, fuente del logo). |
| 13 · Descripción profunda y caras por emoción | §8, §8.1-8.4 | ⚠️ | Carácter, arco, miedos, cómo se ve, qué transmite y dinámicas de 6 personajes; voz medida con `voz.py`. **Caras con minuto: 7 de 25** combinaciones (más el Rey Helado); faltan casi todas las de Finn, Jake, la Princesa y BMO. |
| 14 · Poses con minuto | §15, §15.0 | ⚠️ | Marceline: **12 poses vistas** en vídeo con minuto, más 13 de transcripción y 3 de arte oficial. Finn, Jake y la Princesa: 2-3 vistas cada uno; BMO: 1. El resto, con minuto estimado. |
| 15 · Vestuario con hex | §16 | ✅ | Tres trajes de Marceline, Finn, Jake y la Princesa **medidos** en *model sheets* y capturas; piel de Marceline corregida a `#D8E7E7`; sombrero nuevo. Sin medir: BMO, corona, vaqueros. |
| 16 · Ciudades y fondos de pantalla | §17, §5.2 | ✅ | 4 fondos de fans con tamaño, autor y favoritos (Wallhaven); sitios con su luz y hora vistos. **Fondos oficiales** de descarga, no encontrados (dicho). |
| 17 · Guía para IA de imagen y de texto | §18 | ✅ | Rasgos fijos con hex medidos, línea y sombra, luz, encuadre, palabras que ayudan y que estropean, referencias por número de hoja y minuto, vocabulario de gestos visto, forma de hablar de cada uno y 14 frases por emoción (6 oídas en latino). |
| 18 · Estilo, técnica y cómo replicarlo | §A | ✅ | Papel y tinta digital, Photoshop en preproducción (una fuente), animación en Corea; recetas de Photoshop y Blender; encuadres por emoción sacados de los clips vistos. No hay entrevista sobre encuadres. |
| 19 · Texturas 2D | §B | ✅ | Tramado de cartelas, *halftone* gratis, papel, cartón, tela, madera y cuero CC0 con nombre. Brusheezy, licencia variable (dicho). |
| 20 · Gustos y detalles | §C | ⚠️ | Comida, aficiones, objeto, mascota y cómo se ven, con episodio, para 6. **Ninguna altura** en las fichas; cumpleaños sólo de Marceline; la *Encyclopædia* no cargó. |
| 21 · Por qué la aman | §D | ⚠️ | Premios, crítica, con quién se identifican y Reddit con votos (1186). «I Remember You» completa (minuto, música, dibujo, reacción); el final y «Simon & Marcy», **sin ver cómo están dibujadas**; vídeos de reacción no vistos. |
| 22 · Fan dubs y comunidad hispana | §E | ⚠️ | La campaña por Karla Falcón (documentada), 5 fandubs de YouTube, 2 TikTok, letras de fans, disco oficial en español. **Sin vistas ni fechas** (YouTube y TikTok bloquean). |
| 23 · Colaboraciones, figuras y cosplay | §F | ✅ | Fortnite (con el bajo tocable), MultiVersus, LEGO Dimensions, Minecraft, Brawlhalla, Xbox; Funko con guitarra; 4 construcciones reales del bajo con materiales. Cafés y eventos en Latinoamérica, no buscados. |
| 24 · Obras parecidas | §G | ✅ | La familia de *Flapjack* con dos fuentes, influencias de Ward, y 4 biblias del servidor que se le cruzan (Steven Universe, Rick y Morty, Coco, Mafalda). |
| 25 · El mundo y sus símbolos | §H | ✅ | Reglas en cinco líneas, arcos por temporada, 7 objetos y el vocabulario propio con fuente. |
| 3 conceptos de lámina | §19 | ✅ | Caja de discos en casa de Marceline (A, recomendado), concierto (B) y mixtape de BMO (C), con número de hoja, minuto, letra, sitio de cada texto y profundidad; actualizados con lo visto. |
| 40 fuentes distintas | todo | ✅ | Más de 100 webs distintas enlazadas (lo cuenta `revisar.py`). |
| Tipos de fuente | bitácora §21 | ⚠️ | Oficiales, wikis (API), foros (Reddit, RPF), arte, vídeo, código (GitHub), 3D y doblaje: sí. **TCRF dio 403 y la Wayback Machine se cortó.** En japonés sólo una fuente (primera pasada); coreano y chino, no (serie estadounidense). |
| Hojas de contacto | `hojas/`, §3.0 | ✅ | 3 hojas (personajes 1-48, personajes 49-96, escenas 385-432), menos de 1 MB cada una, miradas y citadas por número. |
| `referencias.json` | archivo | ✅ | **157** referencias (antes 36): todas las útiles de las partes y del recolector, las mejores primero; 63 con ancho y alto medidos. Fuera quedan dos falsos positivos de Openverse. |

**⚠️ antes → después**: la primera pasada tenía **84**; ahora hay más
(ver «Segunda pasada · qué cambió»), porque las secciones nuevas (A-H,
caras, gustos, fandubs) marcan una a una lo dudoso. De los viejos se
resolvieron los de colores, licencias 3D, doblaje, «Oh por Glob», fecha
del disco, fuente del logo, letrista de BOOM!, poses de Marceline y el
«no hay imágenes».

---

## 21 · Bitácora de búsqueda

### 21.1 Comprobación de red (24-sep-2026)

- **curl**: doblaje.fandom.com (API), adventuretime.fandom.com (API),
  horadeaventura.fandom.com (API), cartoonnetwork.com, mondoshop.com,
  opensubtitles.org, subtitlecat.com, flickr.com, artofthetitle.com,
  iam8bit.com, discogs.com, api.sketchfab.com, huggingface.co,
  cdn.jsdelivr.net, i.ibb.co → **sin conexión** (código 000).
- **WebFetch**: theprojectarcade.com, tvlaint.com, open.spotify.com →
  **bloqueados por el proxy**.
- **Funcionan**: raw.githubusercontent.com, git clone de GitHub, PyPI.

### 21.2 Búsquedas web (50)

| # | Idioma | Búsqueda (resumida) | Qué salió |
|---|---|---|---|
| 1 | es | reparto doblaje latino Finn Jake Marceline Dulce Princesa | Doblaje Wiki, Misiones Secundarias |
| 2 | es | Marceline voz latina y canciones | Isabel Martiñón; cantantes por temporada |
| 3 | es | Sensaciones Sónicas, dirección, Rey Helado, BMO | estudio, Óscar Flores, Melgarejo |
| 4 | es | Misiones Secundarias doblaje latino | Iyuno, Leal, 5 de octubre de 2026 |
| 5 | es | voz latina de la Dulce Princesa | Karla Falcón, Claudia Urbán |
| 6 | es | cambio de voz de Jake | Milenio, blog, TikTok |
| 7 | en | Marceline axe bass heirloom | wiki Ax Bass, diseño |
| 8 | en | Adventure Time vinyl Mondo | caja completa 2019 |
| 9 | en | Obsidian soundtrack vinyl | iam8bit, Maya Petersen |
| 10 | en | canciones de Marceline, Rebecca Sugar | Fry Song, Problem, Remember You, Everything Stays |
| 11 | es | canciones latinas de Marceline | Soy tu problema, Canción de las papas |
| 12 | en | BMO's Mixtape iam8bit | Jesse Balmer, vinilo salpicado |
| 13 | es | «Marceline Canta» álbum | lista de 10 canciones |
| 14 | en | «Marceline Sings: Timeless Songs» | Apple Music, versión portuguesa |
| 15 | en | transcripciones en GitHub | guiszk, MrGeislinger, amrosnik |
| 16 | en | encuesta de popularidad | sólo listas de fans |
| 17 | en | subtítulos .srt en GitHub | sólo OpenSubtitles (cerrado) |
| 18 | en | site:github.com srt | nada con tiempos |
| 19 | en | fuente del logo | rótulo a mano; fuente de fans |
| 20 | en | cartelas de título, Nick Jennings | papel viejo, tramado |
| 21 | en | cajas de diálogo de los juegos | nada concreto |
| 22 | en | Sketchfab bajo de Marceline | 10 modelos |
| 23 | en | licencias de esos modelos | Yogensia CC BY-NC-SA |
| 24 | en | ropa de Marceline | camiseta gris, vaqueros, botas rojas |
| 25 | en | casa y cueva de Marceline | casa rosa, laguna, velas |
| 26 | es | frases icónicas, «matemático», intro | «El sicario», «Los amigos se ayudan» |
| 27 | es | modismos mexicanos de Jake | «Ay Jojutla», Clavillazo, orden de CN |
| 28 | es | «¡Matemático!» | wiki y vídeo |
| 29 | es | letra de la intro latina | La Cuerda, musica.com |
| 30 | es | encuesta de personaje favorito | nada oficial |
| 31 | en | Marceline «most popular» | «fan-favorite», Olivia Olson |
| 32 | en | Marceline and the Scream Queens | Meredith Gran, 2012 |
| 33 | en | «Monster», Obsidian | single con King Princess |
| 34 | en | reglas del estilo, brazos de fideo | notas de Ward |
| 35 | en | «The Art of Ooo» | Abrams 2014, 352 páginas |
| 36 | en | Game UI Database | nada de Adventure Time |
| 37 | en | «Hey Ice King!» cajas de texto | reseñas, sin capturas |
| 38 | en | «Everything Stays» en TikTok | viral, Rebecca Sugar, Evanescence |
| 39 | en | clips oficiales de CN | «I'm Just Your Problem», «Fries Song» |
| 40 | en | «Adventure Time: Side Quests» | fechas y reparto |
| 41 | es | «Oh por Glob» en latino | dato confuso |
| 42 | en | LP «Come Along With Me» | Jesse Balmer, 180 g |
| 43 | en | fan art del bajo | DeviantArt, ArtStation |
| 44 | en | key art de Obsidian | Comic-Con 24-jul-2020 |
| 45 | en | compositores Kiefer y Basichis | VICE, AV Club |
| 46 | es | Marceline frases latinas, «Reina Vampiro» | título latino de 7×06 |
| 47 | en | API de Adventure Time en GitHub | imágenes en i.ibb.co (cerrado) |
| 48 | en | texturas CC0 Poly Haven | Rock Wall 05/13, Cave Wall |
| 49 | ja | マーセリン 人気 吹き替え | voz japonesa 冠野智美 ⚠️, «personaje popular» |
| 50 | es | Carla Cerda / Patty Urbán canciones | mismo dato de Doblaje Wiki |

No busqué en **coreano ni chino**: la serie es estadounidense y las
entrevistas originales están en inglés.

### 21.3 GitHub (sin cupo)

- [guiszk/adventuretime-transcripts](https://github.com/guiszk/adventuretime-transcripts):
  **239 transcripciones** (temporadas 1-10 y «Tierras lejanas» 1-2). Base
  de §2, §8 y §15.
- [google/fonts](https://github.com/google/fonts): 31 familias revisadas
  con fontTools (§6.2).
- [LuisFernandoLG/adventure-time-api](https://github.com/LuisFernandoLG/adventure-time-api):
  datos de 14 personajes; sus imágenes están en i.ibb.co (cerrado).
- Probados sin éxito para paletas: `Ryo-N7/tvthemes`,
  `EmilHvitfeldt/r-color-palettes` (no traen Hora de aventura).

### 21.4 Fuentes consultadas por tipo

- **Oficiales**: Mondo, iam8bit, WaterTower Music, Spotify, Apple Music,
  Deezer, HBO Max, canales de Cartoon Network en YouTube, TikTok de
  Rebecca Sugar, libros de Abrams y Titan.
- **Entrevistas al staff**: VICE y AV Club (compositores), JeanBookNerd
  (Kiefer), Art of the Title y Nerdist (cartelas), Acclaim (notas de
  Ward), SciFiNow, The Mary Sue y Bubbleblabber (Olivia Olson).
- **Wikis**: Adventure Time Wiki, Hora de Aventura Wiki, Doblaje Wiki,
  wiki de España, Wikipedia (todas por resumen de búsqueda).
- **Foros y comunidades**: blog Comunidad HDA Latino, Medium, The
  Fandomentals, Autostraddle, Ranker.
- **Arte**: DeviantArt, ArtStation, Pinterest (sólo como pista), LEGO
  Ideas, Steam Workshop.
- **3D y texturas**: Sketchfab, Poly Haven.
- **Doblaje**: Doblaje Wiki, Milenio, GeekZilla, TVLaint, The Project
  Arcade, TikTok y Facebook de convenciones (Expomac, Starcon, Festigame).
- **Otros idiomas**: ciatr (japonés).
- **Sin consultar**: The Cutting Room Floor (no me quedó cupo y los
  juegos no entran en los conceptos); TV Tropes, Reddit y Arctic Shift
  estaban cerrados.

### 21.5 Lo que NO encontré

- Subtítulos con tiempos (para dar minutos exactos).
- Ninguna imagen descargable: **no hay hojas de contacto**.
- Frases textuales de Marceline en el doblaje latino.
- Una encuesta oficial de popularidad.
- Capturas de las cajas de diálogo de los videojuegos.
- Las licencias de 9 de los 10 modelos 3D del bajo.
- El minuto exacto dentro de los vídeos de YouTube y TikTok.

### 21.6 Segunda pasada (25-26 sep 2026, red abierta)

Juntado de las bitácoras de las cuatro partes (`partes/imagen.md`,
`video.md`, `voz.md`, `texto.md`); allí está cada consulta con detalle.

**Comprobación de red**
- **Funcionaban**: API de Fandom (`adventuretime.fandom.com`: el
  subdominio del encargo, `adventuretimewithfinnandjake`, **redirige** ahí;
  comprobado con `meta=siteinfo`), Doblaje Wiki (sólo con `curl -A
  "Mozilla/5.0"`; sin cabecera, 403), Hora de Aventura Wiki en español,
  `static.wikia.nocookie.net` (con `Referer: https://www.fandom.com/`),
  Dailymotion (API y `yt-dlp`), TikTok oEmbed, MusicBrainz, Sketchfab,
  Wallhaven, ambientCG, Arctic Shift, dafont, Fontsource (jsDelivr),
  Spriters Resource, imgur, Wikipedia, GitHub.
- **No funcionaban**: YouTube (pide iniciar sesión: `yt-dlp` y WebFetch
  dan CAPTCHA), TCRF (403), Wayback Machine (conexión cortada, un
  intento), Ranker (401), Medium y la web de Active Theory (403),
  industriaanimacion.com (503), Scribd (no cargó), TikTok sin JavaScript
  (sin vistas), la API de Steam para los appid 298890 y 353200
  (`success:false`), `raw.githubusercontent.com` para repos no vinculados.

**Herramientas**
- `investigar_serie.py`: 1 corrida, 6 páginas, **1188 imágenes, 13 hojas**.
- `fotogramas.py`: **7 clips** (opening latino, créditos, «Fry Song», «I'm
  Just Your Problem», «I Remember You», tráiler de «Obsidian», piloto) más
  4 clips para caras (voz) y 4 fotogramas grandes para medir.
- `estilo.py` y Pillow: 11 imágenes de arte oficial y 5 fotogramas.
- `voz.py` (Whisper): **6 muestras** `.ogg` de Doblaje Wiki.
- fontTools: la fuente de fans de dafont y 6 letras de Fontsource.

**APIs (sin gastar búsquedas)**
- Fandom: `siteinfo`; `list=search` (Lego Dimensions, MultiVersus,
  crossover, Mushroom War, BMO screen, corona); `parse` de «References in
  other media», «LEGO Dimensions», Marceline, Finn, Jake, Princess
  Bubblegum, BMO, Ice King, Mushroom War, Land of Ooo, Ice King's crown,
  Grass Sword, Nightosphere, Steve Wands; `imageinfo` para tamaños.
- Doblaje Wiki: `parse` de «Hora de aventura» (87 135 caracteres).
- Sketchfab: 6 búsquedas (Ax Bass, Finn, Jake, BMO, Marceline house,
  treehouse, Marceline guitar). Wallhaven: 2 búsquedas y 6 fichas.
  ambientCG: 7 (paper, fabric, denim, knit, vinyl record, cardboard,
  wood, leather). Dailymotion: 12 búsquedas por canción y escena (tabla
  en `partes/video.md`), más 2 de fandub. TikTok oEmbed: 4 vídeos.
  MusicBrainz: *release group* del disco en español. Arctic Shift:
  `subreddit=adventuretime&title=cried` (**r/adventuretime sí existe**;
  el recolector no lo encontró).

**Búsquedas web** (unas 40 entre las cuatro partes; inglés y español; no
se buscó en japonés ni coreano: la serie es estadounidense y sus
entrevistas están en inglés)
- Imagen (6, en): colaboraciones de moda, MultiVersus, Funko, cosplay del
  bajo, key art de «Obsidian», texturas de *halftone*.
- Voz (16, es y en): Óscar Flores director; Héctor Emmanuel Gómez BMO;
  encuestas de popularidad (3); fandub y covers en español (4); «Oh por
  Glob»; recepción del final; Arturo Castañeda; *Encyclopædia*; *The
  Guardian*; *Vulture*; premios.
- Texto (18, en): Toon Boom/Photoshop; influencias de Ward; Nick
  Jennings; caja de diálogo de «Hey Ice King!»; series parecidas; Steve
  Wands; rigs de Sketchfab; estilo de línea; símbolos en TV Tropes;
  contorno en Blender; Card Wars (2); arcos por temporada; alumnos de
  Flapjack; Rynda y Photoshop; BMO y Nintendo; grano; fuente de dafont.
- Vídeo: sólo APIs (Dailymotion, TikTok, MusicBrainz).

**Fuentes nuevas por tipo**
- **Oficiales**: canal de Cartoon Network en Dailymotion, tráiler de HBO
  Max, TikTok de Rebecca Sugar, notas de Brawlhalla, *model sheets* con
  sello de Cartoon Network Studios.
- **Wikis**: Adventure Time Wiki y Doblaje Wiki por su API; Hora-de wiki;
  TV Tropes; Wikipedia (serie, personajes, temporadas, juegos).
- **Foros**: Reddit por Arctic Shift, The RPF.
- **Arte y 3D**: Sketchfab (API), Wallhaven, Spriters Resource, ambientCG,
  Openverse, Spoon Graphics, PhotoshopSupply, Brusheezy.
- **Vídeo**: Dailymotion (Cartoon Network, Espinof, HobbyConsolas, Capra
  TV), TikTok.
- **Código**: GitHub (`shishkabob27/CardWars`), Instructables.
- **Doblaje**: Doblaje Wiki (API y audios), La República, Milenio,
  TVLaint, Comic Fest Juárez.
- **Prensa y crítica**: ScreenRant, Sportskeeda, GameRant, Polygon,
  SlashFilm, The Mary Sue, Giant Bomb, Nintendo Life, League of Comic
  Geeks, Fortnite.gg, TCGplayer, BoxLunch.
- **Sin usar**: TCRF (403) y Wayback Machine (cortada). Fuentes en
  japonés, coreano o chino: sólo la de la primera pasada (ciatr).

**Lo que NO encontré en la segunda pasada**: encuesta oficial con
números; clips reales de la cueva, del Anfiteatro Fantasma, «Henchman» y
«Marceline's Closet»; cajas de diálogo de «Nameless Kingdom» y «Pirates
of the Enchiridion»; vistas de fandubs; turquesa de BMO medido; colaboración
de moda; fondos de pantalla oficiales; altura de los personajes; la
entrevista original de Rynda; entrevista sobre encuadres.
