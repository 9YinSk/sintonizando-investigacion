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
> _(se rellena al terminar el repaso)_

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

> [!warning] Sin imágenes descargadas
> Todas las webs de imágenes estaban cerradas. Aquí van **las piezas que
> existen y dónde están**. Antes de dibujar, hay que abrirlas desde un PC
> con red normal y guardarlas en `referencias/hora-de-aventura/`.

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
  (no vi la imagen).
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
| **Marceline Canta: Timeless Songs (Versión en español)** | **Disco oficial en español** con **10 canciones de Marceline** | Hay también **versión en portugués**. La wiki dice **2019** ⚠️ (el número de Apple Music apunta más bien a 2020) | [Spotify](https://open.spotify.com/album/6x28Z0ItbmOHSpPUtExumt), [Deezer](https://www.deezer.com/us/album/153622342), [Hora de Aventura Wiki](https://horadeaventura.fandom.com/es/wiki/Marceline_Canta:_Timeless_Songs), [Apple Music](https://music.apple.com/us/album/marceline-canta-timeless-songs/1515397280) |

**Lista del disco en español** (según la wiki; el episodio va entre
paréntesis tal como lo da) ⚠️:
1. ¿Qué soy para ti? («Lo que estaba perdido»)
2. Soy tu problema («Lo que estaba perdido»)
3. Pequeña mujer («Muchachito malo»)
4. Recordándote («Te recuerdo»)
5. Ya no lo puedo soportar / Siento fuego dentro de mí («Incendio»)
6. Canción de las papas («Llegó de la Nocheósfera»)
7. Todo se queda («Todo se queda / La nube oscura»)
8. Cadena alimenticia («Cadena alimenticia»)
9. Siempre entonces se podrá volver («¡Ven conmigo!»)
10. Acompáñame («¡Ven conmigo!»)

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

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D del bajo-hacha (Sketchfab)

Sketchfab no abría (ni la web ni su API), así que **no pude leer la
licencia de casi ninguno**. Los que en el título dicen «Download Free»
son descargables, y en Sketchfab eso **suele** ser Creative Commons ⚠️.
**Comprueba la licencia en la ficha antes de usar.**

| Modelo | Autor | Licencia | Nota |
|---|---|---|---|
| [Marceline's Ax Bass](https://sketchfab.com/3d-models/marcelines-ax-bass-2224d0a363a24ba883614f209761454c) | **Yogensia** | **CC BY-NC-SA 4.0** ✅ (lo dice su ficha, según la búsqueda) | Descargable. Crédito: «Marceline's Ax Bass» by Yogensia, CC BY-NC-SA 4.0. **Sin uso comercial**: vale para el Discord si no se vende nada |
| [Marceline's Ax Bass](https://sketchfab.com/3d-models/marcelines-ax-bass-417178d709774642b0d5b5a02181caa2) | Haxis | descargable, licencia sin ver ⚠️ | |
| [Low Poly Marceline's Ax Bass](https://sketchfab.com/3d-models/low-poly-marcelines-ax-bass-adventure-time-101d7036f35b411295e6a500c86e952b) | Roberto Cuxil (@cuxilrodas) | descargable, sin ver ⚠️ | **Texturas pintadas en Blender con aspecto de dibujo animado**: la más fiel al estilo |
| [Marceline's Axe Bass](https://sketchfab.com/3d-models/marcelines-axe-bass-477b56a2db134065947b2c931c52b3aa) | denizin | descargable, sin ver ⚠️ | textura iridiscente (se aleja del estilo plano) |
| [Marceline axe bass guitar](https://sketchfab.com/3d-models/marceline-axe-bass-guitar-adventure-time-9bc622d77287423391e4e5451c05ca77) | Z3bbz | sin ver ⚠️ | |
| [Marceline Bass Axe](https://sketchfab.com/3d-models/marceline-bass-axe-b6f6f74eb92f4bbfbcbd2d4d01f3b8df) | Froes | sin ver ⚠️ | 16,5 mil triángulos |
| [(SGP) Marceline's Bass Axe](https://sketchfab.com/3d-models/sgp-adventure-time-marcelines-bass-axe-6e72178681c44722a0cb5226deff7e8e) | TravisEvashkevich | sin ver ⚠️ | |
| [Marceline's Bass Guitar](https://sketchfab.com/3d-models/marcelines-bass-guitar-4d89b7121de54b4e9410f4472fa1bab6) | deadlygeek | sin ver ⚠️ | |
| [Marceline's guitar bass](https://sketchfab.com/3d-models/marcelines-guitar-bass-c003bed4b97244d1b705626dd5bb5e69) | Hoho (@hoho03) | sin ver ⚠️ | trae versión alta y baja en polígonos |
| [Marceline's Axe Bass](https://sketchfab.com/3d-models/marcelines-axe-bass-e111ddfd74f9426dab13a70fce789d44) | 10958533 | sin ver ⚠️ | |
| [Axe bass – Marceline](https://www.artstation.com/artwork/BmZxOm) (ArtStation) | Victor Cavalcante Vk | sólo para mirar | render 3D |

> Recomendación: usar **el de Yogensia** (licencia conocida) o modelarlo
> desde cero siguiendo §3.5. Es un objeto sencillo: dos hojas de hacha,
> un mástil y una pala. **Ojo**: un render 3D realista del bajo **no
> encaja** junto a un personaje plano; hay que darle material plano con
> contorno (ver §18).

### 4.2 Fan art 2D (mirar, nunca pegar)

- [Marceline playing bass](https://www.deviantart.com/ajscanvas/art/Marceline-playing-bass-292387926), AJsCanvas: **redibuja la pose de «What Was Missing»** (3×10). Útil para ver la postura al tocar.
- [Marceline and her ax bass](https://www.deviantart.com/queenjazmine/art/Marceline-and-her-ax-bass-419453602), queenjazmine.
- [Marceline Plays the Bass](https://www.deviantart.com/disneyponyfan/art/Marceline-Plays-the-Bass-924284143), Disneyponyfan.
- [Marceline Bass](https://www.deviantart.com/minty-kitty-art/art/Marceline-Bass-510877467), Minty-Kitty-Art (se vendió como lámina).
- Diseños del bajo solo: [DavaDs](https://www.deviantart.com/davads/art/Marceline-s-Axe-Bass-382362695), [TheBreakfastUnicorn](https://www.deviantart.com/thebreakfastunicorn/art/Marcelines-axe-bass-3-304673345).

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
- **La casa del árbol** de Finn y Jake: donde vive BMO ✅ (serie entera).
- **El Reino de Cristal** («Obsidian»): escenario con telones, un
  **horno** donde está encerrado el dragón y un pueblo de cristal ✅.

### 5.2 Luz ⚠️ (de memoria)

- Cueva: luz **fría, azul violeta**, con puntos cálidos de **velas**;
  reflejos de la laguna.
- La casa por dentro: **cálida**, lámparas y velas.
- Escenario del cementerio: **noche**, niebla verde azulada y un foco.
- Casa del árbol: **luz de tarde dorada** entrando por ventanas redondas.

### 5.3 Paleta ⚠️ (aproximada, de memoria: **muestrear en un fotograma** antes de usar)

| Qué | Hex aproximado |
|---|---|
| Piel de Marceline (gris azulado pálido) | `#A9B8C2` |
| Pelo de Marceline (negro azulado) | `#1C1B2B` |
| Camiseta gris de tirantes | `#8C8C8C` |
| Vaqueros azules | `#3E5C9A` |
| Botas rojas | `#B3262B` |
| Bajo-hacha: filos rojos | `#C22B2F` |
| Bajo-hacha: madera del mástil | `#6B4226` |
| Casa de Marceline (rosa) | `#E7A1B0` |
| Tejado marrón | `#6E4A36` |
| Fondo de la cueva (morado oscuro) | `#2A2440` |
| Finn: camiseta celeste | `#35A9E0` |
| Finn: pantalón azul | `#1F4E9B` |
| Finn: mochila verde | `#5FAE44` |
| Jake: amarillo naranja | `#F2B133` |
| Dulce Princesa: piel rosa | `#F6A9C8` |
| Dulce Princesa: pelo chicle | `#E0569A` |
| BMO: carcasa turquesa | `#6CC3B3` |
| BMO: pantalla verde claro | `#CFEFD9` |
| Papel viejo de las cartelas | `#E8DCBC` |
| Vinilo «Glassboy Blue» | azul claro translúcido, sin ver |

### 5.4 Texturas reales equivalentes (CC0, sin crédito obligatorio)

- Roca de la cueva: [Rock Wall 05 (Poly Haven, 8K)](https://polyhaven.com/a/rock_wall_05) y [Rock Wall 13 (16K)](https://polyhaven.com/a/rock_wall_13) ✅ CC0.
- Luz de cueva real para Blender: [Cave Wall HDRI (Poly Haven)](https://polyhaven.com/a/cave_wall) ✅ CC0 (cueva con río y vegetación, luz suave).
- Cartón de la funda del disco, papel de la nota, madera del mástil:
  **ambientCG** (CC0) o la [sección de texturas de Poly Haven](https://polyhaven.com/textures) ✅. No busqué la textura concreta.
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
- Hay una **fuente de fans, «Adventure Time Logo»**, gratis en
  [Font Meme](https://fontmeme.com/fonts/adventure-time-font/) y
  [font.download](https://font.download/font/adventure-time-logo) ✅.
  **No pude bajarla** para ver si trae tildes y ñ ⚠️. Las fuentes de fans
  de logos casi nunca las traen: **compruébalo antes**.
- **Las cartelas de título**: cada una **rotulada a mano** por el pintor,
  distinta en cada episodio, sobre papel viejo ✅ (ver §3.2).
- **Los cómics de BOOM!**: globos con letra de cómic a mano ⚠️ (de
  memoria; no busqué el rotulista).

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

> **No** usar Comic Sans ni fuentes «de anime». **No** usar la fuente
> de fans del logo para frases largas: sólo para una o dos palabras.

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
4. **La pantalla de BMO** ⚠️ (de memoria): su cara es una pantalla;
   a veces muestra imágenes o texto de videojuego.
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

### 7.3 En los videojuegos ⚠️

- Hay muchos: **«Hey Ice King! Why'd You Steal Our Garbage?!!»**
  (WayForward, DS y 3DS, 2012; Pendleton Ward ayudó con la historia),
  **«The Secret of the Nameless Kingdom»** (2014), **«Pirates of the
  Enchiridion»** (2018) ✅
  ([Gaming Nexus](https://www.gamingnexus.com/Article/Adventure-Time-Hey-Ice-King!--Whyd-you-steal-our-garbage!!/Item3804.aspx),
  [Destructoid](https://www.destructoid.com/reviews/review-adventure-time-pirates-of-the-enchiridion/),
  [IMDb](https://www.imdb.com/title/tt9863808/)).
- **No encontré cómo son sus cajas de diálogo** (Game UI Database tiene
  reto de Cloudflare y no sale en búsquedas). Creo recordar que el de DS
  usa **retratos de los personajes junto a una caja de texto** ⚠️, pero
  **no lo pude comprobar**: no lo uses sin ver una captura.

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

### Dulce Princesa (Princess Bubblegum, Bonnibel)

- **Quién es**: la **gobernante del Dulce Reino** y **científica** ✅
  (wikis). Tiene cientos de años ⚠️.
- **En la música**: quiere **dirigir**: «For our next attempt, **I
  wanna be the lead**» y da órdenes técnicas («triplet quavers in
  mixolydian mode») que nadie entiende (3×10) ✅. Toca a BMO como
  instrumento ✅. En el final descubre que **la armonía es el arma**
  («It's the harmony!») ✅.
- **Cómo habla**: correcta, algo mandona, muy segura. Con Marceline,
  **juguetona**: «Ooooo, so mysterious all the time. Just like your
  song» («Obsidian») ✅.
- **Cuerpo**: postura recta, manos juntas o señalando, bata de
  laboratorio en ciencia ⚠️.

### BMO

- **Quién es**: una **consola de videojuegos viva** que vive con Finn y
  Jake ✅ (wikis).
- **En la música**: canta «**Time Adventure**» en el final, con Jake en
  brazos, y grita «**My art is a weapon!**» (10×13, ≈35:55-37:00) ✅.
  Tiene **disco propio**: «BMO's Mixtape» (§3.4) ✅. La Princesa le hace
  sonar «Sound Structure Alpha» (3×10) ✅.
- **Cómo habla**: como un niño pequeño muy seguro de sí mismo; habla de
  sí en tercera persona a veces ⚠️.

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

---

## 9 · ¿Quién es el más querido?

- **No encontré una encuesta oficial** de Cartoon Network ni de la
  productora.
- Lo que sí hay:
  - La editorial **BOOM!** llamó a Marceline «**fan-favorite**» en la nota
    de prensa de «Marceline and the Scream Queens» ⚠️ (lo cita
    [Wikipedia](https://en.wikipedia.org/wiki/Marceline_the_Vampire_Queen),
    según el resumen de la búsqueda).
  - «Evicted!» (su primer episodio) **disparó su popularidad** ⚠️ (misma
    fuente).
  - Tuvo **su propia miniserie** («Estacas», 2015) y **su propio
    especial** («Obsidian», 2020) ✅
    ([Wikipedia: Stakes](https://en.wikipedia.org/wiki/Stakes_(miniseries)),
    [Wikipedia: Distant Lands](https://en.wikipedia.org/wiki/Adventure_Time:_Distant_Lands)).
    Sólo ella y la Princesa (y BMO, con su especial) tienen eso.
  - Tiene **dos discos propios** («Marceline Canta» en español y
    portugués) ✅.
  - Listas de fans: [Ranker](https://www.ranker.com/list/best-adventure-time-characters/cerberus)
    (1.958 votantes a septiembre de 2026; no vi su orden),
    [Looper](https://www.looper.com/803890/15-most-popular-adventure-time-characters-ranked-worst-to-best/),
    [Screen Rant](https://screenrant.com/best-adventure-time-characters-ranked/)
    ⚠️ (no pude abrirlas).
  - Japón: «マーセリンはアドベンチャー・タイムの人気キャラクターの一人»
    (es uno de los personajes populares) ⚠️
    ([ciatr](https://ciatr.jp/topics/74459)).
- **Conclusión**: para un canal de música, **Marceline no es sólo la
  más querida: es la única música de verdad del reparto**. Finn y Jake
  sirven de acompañantes (beatbox y viola), y **BMO** es el secundario
  más tierno con disco propio.

---

## 10 · Doblaje latino

> Doblaje Wiki y la Wiki de Hora de Aventura no abrían (ni por su API).
> Los datos salen de **resúmenes de búsqueda** de esas páginas, cruzados
> con noticias, TikTok y Facebook de convenciones.

### 10.1 El doblaje de la serie ✅

- Estreno en Latinoamérica: **8 de agosto de 2010** (en EE. UU., 5 de
  abril de 2010) ⚠️ (una fuente: [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Hora_de_aventura) por búsqueda).
- **Estudio**: **Sensaciones Sónicas** (México) desde el principio
  **hasta la temporada 5**; desde el episodio «**El traje de Jake**»,
  **SDI Media de México** ✅
  ([Hora de Aventura Wiki: Sensaciones Sónicas](https://horadeaventura.fandom.com/es/wiki/Sensaciones_S%C3%B3nicas),
  [Milenio](https://www.milenio.com/espectaculos/television/cambio-voz-jake-perro-hora-aventura)
  habla de SDI México).
- **Dirección**: empezó a **principios de 2010** con **Óscar Flores**
  (que además es el Rey Helado); desde la temporada 3 cambió varias veces:
  Rafael Pacheco, Juan Antonio Edwards, Circe Luna, Elsa Covián y Carlos
  Hugo Hidalgo ⚠️ (una fuente).

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
| **Dulce Princesa** | **Karla Falcón** (temp. 1-2 y **vuelve desde la 4 a petición de los fans**) | ✅ | [Doblaje Wiki: Dulce Princesa](https://doblaje.fandom.com/es/wiki/Dulce_Princesa), [TikTok, entrevista en Festigame 2024](https://www.tiktok.com/@eldiariodelalquimista/video/7440244073505623352) |
| Dulce Princesa (suplente, temp. 3 hasta el ep. 94) | Claudia Urbán | ⚠️ | Doblaje Wiki (por búsqueda) |
| **Rey Helado** | **Óscar Flores** (toda la serie y «Misiones Secundarias») | ✅ | [Doblaje Wiki: Rey Helado](https://doblaje.fandom.com/es/wiki/Rey_Helado), noticias de «Misiones Secundarias» |
| **BMO** | **Gustavo Melgarejo** (hasta la temp. 5, en Sensaciones Sónicas) | ⚠️ | Hora de Aventura Wiki (por búsqueda) |

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
| «**¡Oh, por Glob!**» | en inglés «Oh my Glob». Según la búsqueda, en latino **a veces se cambió por «¡Oh, por Dios!»**, y «¡Oh por Glob!» quedó como muletilla de la **Princesa Grumosa** | ⚠️ (dato confuso) |
| «**Soy tu problema**», «**Canción de las papas**», «**Todo se queda**», «**¡Oh, Dulce Princesa!**» | títulos latinos de canciones | ✅ |
| «**Marceline la Reina Vampiro**» | título latino oficial de 7×06 («Estacas», parte 1) | ✅ ([HBO Max](https://www.hbomax.com/bo/es/shows/hora-de-aventura/s7/fff09eaf-17c3-446b-be32-8a0d47e4ccf1/e6-marceline-la-reina-vampiro/73c26176-7919-4bfe-8b77-db471f43719d), [Hora de Aventura Wiki](https://horadeaventura.fandom.com/es/wiki/Marceline_la_Reina_Vampiro)) |

**Intro latina** ⚠️ (letras de fans; el orden varía entre páginas):
«Hora de aventura, llama a tus amigos, vamos a tierras muy lejanas, con
Jake el perro y Finn el humano, y diversión siempre tendrás, ¡es hora
de aventura!»
([La Cuerda](https://chords.lacuerda.net/musica_de_tv/hora_de_aventura__intro),
[musica.com](https://www.musica.com/letras.asp?letra=2056436),
[Hora de Aventura Wiki: secuencia de apertura](https://horadeaventura.fandom.com/es/wiki/Secuencia_de_apertura)).

> **No encontré** cómo dice Marceline en latino «Thanks for helping me
> record», «I'm Marceline the Vampire Queen» ni la frase del Hoyo Musical.
> Las frases que propongo para la lámina son **traducción mía**.

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

### 11.2 Los temas que dan ambiente

| Tema | Dónde | Ambiente |
|---|---|---|
| Intro «Hora de aventura» | cada episodio | ukelele y voz aniñada, alegre y casera ⚠️ |
| **«Island Song (Come Along With Me)»**, de **Ashley Eriksson** | cierre de cada episodio y final de la serie | dulce, melancólico, de despedida ✅ |
| «Fry Song» / «Canción de las papas» | 2×01 | bajo solo y voz, **íntimo, de grabación casera** ✅ |
| «I'm Just Your Problem» / «Soy tu problema» | 3×10 | rock con rabia contenida, **con banda** ✅ |
| «Remember You» / «Recordándote» | 4×25 | teclado (omnichord) y voz, **para llorar** ✅ |
| «Slow Dance With You» | 10×07 | **concierto en directo** ✅ |
| «Everything Stays» / «Todo se queda» | 7×07 | nana, triste y cálida ✅ |
| «Woke Up», «Monster», «See Through», «Eternity With You» | «Obsidian» | **punk** («Woke Up»), **balada** («Monster»), dúo final ✅ |
| «Time Adventure» | 10×13 | BMO, **canción de cuna que vence al caos** ✅ |
| «Bacon Pancakes» | 4×16 | tontería pegadiza de Jake; meme ✅ |

> Para #musica-nueva, el ambiente es **el del estreno casero**: bajo,
> voz y ritmo hecho con la boca. No una superproducción.

---

## 12 · Vídeos

> YouTube y TikTok estaban cerrados: **no pude ver los vídeos ni dar el
> minuto dentro de ellos**. Van con su enlace, tal como salieron en la
> búsqueda. Los minutos de las escenas están en §2 (del episodio).

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

- «**Everything Stays**» es **viral en TikTok**: versiones, mezclas con
  «Drift Away» de Steven Universe y dúos de hermanos ✅
  ([búsqueda de TikTok](https://www.tiktok.com/discover/everything-stays-adventure-time-full)).
- **Rebecca Sugar** tiene TikTok y subió «Everything Stays»:
  [vídeo](https://www.tiktok.com/@rebeccasugar/video/7380076323168996650) ✅.
- **Evanescence (Amy Lee)** hizo su versión:
  [vídeo](https://www.tiktok.com/@evanescence/video/7008939931548568837) ✅.
- Isabel Martiñón en la Expomac de Veracruz:
  [vídeo](https://www.tiktok.com/@rebecavirgen/video/7434952138339536184).
- Entrevista a Karla Falcón (Dulce Princesa) en Festigame 2024:
  [vídeo](https://www.tiktok.com/@eldiariodelalquimista/video/7440244073505623352).
- «¿Por qué cambió la voz de Jake?»:
  [vídeo](https://www.tiktok.com/@acubick/video/7206541052713438469).

### 12.4 Análisis

- [«Marceline's Best Tunes, Ranked»](https://medium.com/the-dot-and-line/marceline-songs-adventure-time-ranked-f0e904443f9a) (Medium).
- [«Six Degrees of Rebecca Sugar: The Long Road to Bubbline»](https://www.thefandomentals.com/six-degrees-of-rebecca-sugar-the-long-road-to-bubbline-and-beyond/).
- [«Adventure Scrape: text mining on Adventure Time transcripts»](https://medium.com/towards-data-science/adventure-scrape-text-mining-on-adventure-time-transcripts-8a50d09c2b6d).
- Clip «Behind the Music» de la serie en [Internet Archive](https://archive.org/details/bliptv-20131014-143325-Cbr-AdventureTimeClip176) ⚠️ (archive.org cerrado).

---

## 13 · Videojuegos de la franquicia ⚠️

Ver §7.3. Lo único confirmado: existen (WayForward 2012, 2014, Climax
2018) y el de 2012 tiene **más de 50 personajes** de las temporadas 1-3
y lugares como el Dulce Reino, el Reino Helado, el Espacio Grumoso y la
casa del árbol ✅ ([Gaming Nexus](https://www.gamingnexus.com/Article/Adventure-Time-Hey-Ice-King!--Whyd-you-steal-our-garbage!!/Item3804.aspx),
[Mash Those Buttons](https://mashthosebuttons.com/review/adventure-time-hey-ice-king-whyd-you-steal-our-garbage-review/)).
**No sé cómo son sus cajas de diálogo.** No los propongo como cuadro.
También existe **Card Wars** (el juego de cartas del episodio, hecho
juego real) ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Card_Wars)).

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todos reconocen

- «**¿Qué hora es? ¡Hora de aventura!**» ⚠️ (la frase del opening).
- «**¡Matemático!**» y «**¡Algebraico!**» ✅.
- «**Bacon Pancakes**» de Jake ✅ (4×16).
- «**Papi, ¿por qué te comiste mis papas?**»: la **Canción de las papas**
  ✅ (título latino confirmado; la letra exacta en latino ⚠️).
- **«I Remember You»**: el episodio que hace llorar; Marceline y Simón ✅.
- **«Bubbline»**: la pareja Marceline y Dulce Princesa, **hecha oficial**
  con el beso del final (10×13, ≈33:30) ✅.
- **Jake con modismos mexicanos** y la polémica del cambio de voz ✅ (§10.3).
- **«Everything Stays»** en TikTok ✅.
- El **bajo-hacha**: los fans lo **construyen de verdad** y lo modelan en
  3D ✅ (§3.5, §4.1).
- **«Oh my Glob»** (Princesa Grumosa) ⚠️ en latino.

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

---

## 15 · Poses analizadas por personaje

> Sin fotogramas descargados. Las poses salen de las **acotaciones de las
> transcripciones** ✅ (qué hace) con **minuto estimado** ⚠️ (dónde
> mirar). La mano, la mirada y el gesto que añado son **descripción mía
> de memoria** ⚠️: comprobar en el fotograma.

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

**La mejor para presentar el canal**: la 10 (escenario) o la 6
(grabando). **Para la regla «nada de vida personal»**: la 4 (guiño
burlón) o la 11 (desgana).

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
  «Power Animal»…) ✅.
- Otra muy popular: **chaqueta corta rosa y morada, pantalón corto
  magenta y botas altas rosas**, a veces con **camiseta de rock** ⚠️ (una
  fuente la llama «la más icónica»).
- **De día**: **sombrero de sol y guantes** ✅ (3×10).
- «Obsidian»: **ropa de motorista**, en moto con la Princesa detrás ✅
  («full biker gear», ≈11:49).
- De niña: camiseta de tirantes verde, pantalón marrón morado, botas
  moradas oscuras; o camiseta rosa y peto azul ✅ (wiki, por búsqueda).
- **Pelo**: **negro, lisísimo y larguísimo**, hasta las rodillas o más ⚠️.
- **Fijo**: piel gris azulada, **orejas puntiagudas**, **dos marcas de
  mordida en el cuello** ⚠️ (de memoria).

### Finn ⚠️ (de memoria)
Gorro blanco con **orejas de oso**, camiseta celeste, pantalón corto azul
oscuro, calcetines blancos altos, zapatos negros, **mochila verde**.

### Jake ⚠️
Sin ropa; amarillo anaranjado, **orejas caídas**, hocico claro.

### Dulce Princesa ⚠️
Piel y pelo rosa chicle, **corona dorada** con gema azul, vestido rosa;
bata de laboratorio y gafas cuando hace ciencia.

### BMO ⚠️
Consola turquesa, **pantalla con cara**, cruceta amarilla, botones de
colores, piernas y brazos finitos.

---

## 17 · Paisajes y fondos de pantalla

- **No bajé ni medí ninguno** (red cerrada). Lo que existe y conviene
  buscar desde un PC con red:
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
- La hora del día: **noche o cueva** para Marceline; **tarde dorada**
  para la casa del árbol ⚠️ (§5.2).

---

## A · Estilo de dibujo y técnica, y cómo replicarlo (punto 18)

_(pendiente)_

---

## B · Texturas 2D (punto 19)

_(pendiente)_

---

## C · Gustos y detalles de cada personaje (punto 20)

_(pendiente)_

---

## D · Por qué la gente la ama (punto 21)

_(pendiente)_

---

## E · Fan dubs y comunidad hispana (punto 22)

_(pendiente)_

---

## F · Colaboraciones, figuras y cosplay (punto 23)

_(pendiente)_

---

## G · Obras parecidas y temas relacionados (punto 24)

_(pendiente)_

---

## H · El mundo, la historia y sus símbolos (punto 25)

_(pendiente)_

---

## 18 · Guía para generar con IA (Firefly, Canva)

> La IA sólo para **fondos, poses de apoyo o bocetos**. El personaje
> final, mejor redibujado o sacado de un fotograma real. Y todo lo que
> salga de la IA se compara con las referencias de §3 y §15.

### 18.1 El estilo en pocas palabras (lo que nunca cambia)

- **Línea**: contorno **fino, uniforme, oscuro** (no negro puro:
  marrón o morado muy oscuro en los personajes) ⚠️; sin variación de
  grosor tipo pincel.
- **Color**: **plano**, casi sin sombras; cuando hay sombra, **una sola
  mancha de sombra dura** ⚠️.
- **Formas**: círculos, óvalos y triángulos; **brazos y piernas de
  fideo** «al dente» sin codos ✅ ([notas de Pendleton Ward, Acclaim](https://acclaimmag.com/culture/learn-draw-adventure-time-creator-pendleton-wards-detailed-occasionally-bizarre-notes/)).
- **Caras**: **ojos de punto negro** y **boca de una línea** o una
  curva ✅ (mismas fuentes).
- **Fondos**: **pintados**, con más textura y detalle que los
  personajes, y colores más suaves ⚠️.

### 18.2 Marceline, rasgos fijos

- Piel **gris azulada pálida**, **pelo negro lisísimo** hasta más abajo
  de la cintura, flequillo partido ⚠️, **orejas puntiagudas**, colmillos
  pequeños, **dos puntos de mordida en el cuello** ⚠️.
- **Flota**. Cuerpo largo y delgado.
- Ropa por defecto: **camiseta gris de tirantes, vaqueros, botas rojas**
  ✅.
- **El bajo-hacha**: hacha de doble filo **roja**, mástil de madera,
  **cuatro cuerdas**, **dos clavijas a cada lado** de la pala ✅.

### 18.3 Palabras que ayudan

`flat 2D cartoon, thin uniform outline, flat colors, simple dot eyes,
noodle limbs, whimsical post-apocalyptic fantasy, painted background,
gouache background, soft pastel palette, Cartoon Network 2010s style`
y, para el sitio: `cave with stalactites, small pink suburban house
inside a cave, lagoon, candles, night`.

Para el título: `vintage paper border, halftone dithering, pulp
paperback cover, hand-lettered title` (el estilo de las cartelas, §3.2).

### 18.4 Palabras que lo estropean

`anime, manga, big eyes, detailed shading, cel shading with gradients,
realistic, 3D render, glossy, Pixar`, `vampire blood, gore` (Marceline
**no** es de sangre), `electric guitar` (sale una guitarra normal: pedir
**`double-bladed battle axe shaped bass guitar, 4 strings`**).

### 18.5 Qué referencias usar

- **De estilo**: el arte de los discos oficiales (§3.4) y las cartelas
  (§3.2).
- **De pose**: los momentos de §15 (sobre todo Marceline 6, 8 y 10).
- **Del objeto**: el modelo 3D de Yogensia (§4.1) y las fotos de
  réplicas reales (§3.5).
- **De luz para Blender**: el [HDRI Cave Wall](https://polyhaven.com/a/cave_wall) (§5.4).

---

## 19 · Tres conceptos para la lámina de #musica-nueva

Los tres usan los textos de §0. Las frases «en la voz de la serie» son
**traducción mía**, no del doblaje (no la encontré). Recortes siempre por
`v3/integrar.py` y comprobados a 1:1.

### Concepto A — «El estreno en la caja» (Marceline en su casa)

- **Objeto y sitio**: sobre **el sofá de la casa de Marceline**, dentro
  de la cueva (§5.1), **una caja de discos abierta**, inspirada en la
  **caja real de Mondo** (§3.4): dentro, **un LP de 12"**, **un 10"**,
  **un single de 7"** y **un casete**. **El bajo-hacha** apoyado en el
  brazo del sofá. Velas en la pared. Por la ventana, la **laguna** con
  reflejos azules.
  - En Blender: caja de cartón con tapa, vinilos de colores (amarillo,
    azul oscuro y rosa, como los de Mondo), casete, el bajo (modelo de
    Yogensia o hecho a mano), sofá sencillo. Cartón y madera de
    ambientCG/Poly Haven (§5.4).
- **Personaje**: **Marceline flotando** encima de la caja, **tumbada en
  el aire boca abajo**, con un disco en la mano (pose de §15 n.º 2-3:
  relajada, burlona). Referencia de pose: «Evicted!» ≈2:31 y «Marceline's
  Closet» ≈8:41 (flota sobre la cama).
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
  ventana del otro; un vinilo **medio fuera de la funda** proyectando
  sombra.
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
  ≈18:47) para «lo siguiente».
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
  con el bajo, para que la protagonista siga en la lámina.
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
  primer plano; **luz de tarde dorada** por la ventana redonda; la
  pantalla de BMO **ilumina** la cara de Finn.

### ¿Cuál primero?

- **A** es el más fiel al plan (bajo + discos) y el que mejor explica
  «disco, single, EP» con **objetos reales de la franquicia**.
- **B** es el más espectacular y el que más dice «estreno»: un concierto.
- **C** es el más tierno y el que menos depende de Marceline; útil si la
  lámina de otro canal ya la usa.

---

## 20 · Lo que no pude verificar

- **Ninguna imagen vista.** Todo lo visual (key art, portadas de discos,
  cartelas) está descrito por texto de tiendas y noticias.
- **Los minutos** son estimados por la posición en la transcripción (±1
  minuto).
- **Frases latinas de Marceline**: no encontré ninguna frase textual suya
  en el doblaje (sólo títulos de canciones y del episodio). Tampoco la
  del Hoyo Musical.
- **Quién canta** a Marceline en cada temporada (Claudia Urbán, Patty
  Urbán, Carla Cerda): una sola fuente (Doblaje Wiki).
- **BMO latino** (Gustavo Melgarejo) y los directores de doblaje: una
  sola fuente.
- **Estudio de «Misiones Secundarias»** (Iyuno México, Miguel Ángel
  Leal): una sola fuente.
- **Fecha del disco «Marceline Canta»**: 2019 según la wiki; puede ser 2020.
- **Encuesta oficial de popularidad**: no existe o no la encontré.
- **Las licencias** de los modelos 3D, salvo el de Yogensia.
- **Las cajas de diálogo** de los videojuegos.
- **Colores**: todos los hex son aproximados.
- **«El sicario»** = «Hitman» (3×04): deducción mía.
- La **fuente de fans «Adventure Time Logo»**: no sé si trae tildes.

---

## Cumplimiento del encargo

_(pendiente)_

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
