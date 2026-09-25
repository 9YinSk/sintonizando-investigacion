---
tags: [biblia, serie, laminas]
serie: "Adventure Time (Hora de aventura)"
canal: "#musica-nueva"
fecha: 2026-09-24
---

# Biblia · Hora de aventura — para #musica-nueva

> [!important] Cómo se hizo, y sus límites
> - **Segunda pasada con la red abierta (25-sep-2026)**, por un equipo de
>   cuatro investigadores (imagen, vídeo, voz, texto) y un redactor. Se
>   pudo usar: la API de Fandom (wiki inglesa `adventuretime.fandom.com`,
>   Hora de Aventura Wiki y Doblaje Wiki), `investigar_serie.py` (1188
>   imágenes, 13 hojas, **3 en `hojas/`**), `fotogramas.py` sobre
>   **Dailymotion** (YouTube pide sesión), `estilo.py` y Pillow para
>   **medir colores**, `voz.py` (Whisper) sobre **6 audios reales del
>   doblaje**, las API de Sketchfab, Wallhaven, ambientCG, MusicBrainz y
>   TikTok (oEmbed), Reddit por Arctic Shift y `fontTools`. Siguieron
>   cerrados: YouTube, Ranker (401), TCRF (403), Medium (403) y Scribd.
>   Lo de abajo, de la primera pasada, queda como historia.
> - Primera pasada (24-sep): **la red estaba cerrada.** Fandom (las tres wikis: inglés, Hora de
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

## Segunda pasada · qué cambió

**Corregido (antes → ahora):**

- **Piel de Marceline**: `#A9B8C2` gris azulado, de memoria → **`#D8E7E7`**
  casi blanca con un toque menta, medida en el model sheet oficial (ep. 057)
  y en «Drama Bomb». Con luz de escena se oscurece a **`#657471`** (medido
  en «I'm Just Your Problem», 0:52). Usa la primera como color base.
- **Pelo de Marceline**: `#1C1B2B` negro azulado → **negro puro `#000000`**
  en el model sheet; en escena tira a rojo muy oscuro (`#150209`,
  `#24080E`), **nunca a azul**.
- **Piel de Finn**: «celeste» → **`#FDE5DA`** durazno pálido (el celeste era
  la camiseta, `#018BCB`).
- **Reparto latino**: ahora con la tabla completa de Doblaje Wiki (API) y
  segunda fuente para cada voz principal. La Dulce Princesa: **Karla Falcón**
  (1-2), **Claudia Urbán** (eps. 58-94) y **vuelve Falcón en «Rey Gusano»**
  (ep. 96) tras **peticiones firmadas de fans**. BMO: **Gustavo Melgarejo**
  (1-5) → **Héctor Emmanuel Gómez** (5.2-9). Director de las temporadas
  6-9: **Arturo Castañeda**.
- **«¡Oh por Glob!»**: era «dato confuso» → **confirmado**, es la muletilla
  latina de la **Princesa Grumosa** (Doblaje Wiki + Hora de Aventura Wiki).
- **Sketchfab**: el bajo low poly de cuxilrodas **no es Creative Commons**
  («Free Standard»): sólo mirar. El de **Haxis** es **CC BY** (API).
- **«I Remember You»**: no sólo lee notas; en la escena sale **una Polaroid
  de Marceline niña** (1:36 del clip) y el Rey Helado toca **una batería
  verde con «#1»**.
- **Minutos**: los «≈» de transcripción de «Fry Song», «I'm Just Your
  Problem», «I Remember You» y «Obsidian» → **minuto exacto visto** en
  clips reales de Dailymotion.
- **Wiki de Fandom**: el subdominio del encargo redirige; la buena es
  `adventuretime.fandom.com`.

**Añadido:**

- **3 hojas de contacto** en `hojas/` (miradas) y la sección que dice qué
  sirve de cada una (§3.8).
- **6 frases textuales del doblaje latino**, de audios oficiales de Doblaje
  Wiki pasados por Whisper, con el tono medido de cada voz (§10).
- **12 poses de Marceline** vistas en vídeo, con minuto (§15) y **una cara
  por emoción** de Finn, Rey Helado, Marceline, Jake, Dulce Princesa y BMO
  con enlace `?t=` (§8).
- **Paletas medidas**: casa de Marceline por dentro y el Reino de Cristal de
  «Obsidian» (§5); vestuario de Marceline, Finn, Jake y Dulce Princesa (§16).
- **Disco oficial en español** con sus 10 títulos reales (MusicBrainz), y
  que «Everything Stays» habla de **la mamá de Marceline** (TikTok de
  Rebecca Sugar) (§11).
- **Fondos de pantalla** con tamaño y autor (Wallhaven) y la casa del árbol
  en 3D CC BY (§17).
- Fortnite, MultiVersus, LEGO Dimensions, Minecraft, Brawlhalla, Funko y
  cosplay del bajo con materiales reales (punto 23).
- Las **secciones nuevas de los puntos 18 a 25** (técnica y cómo
  replicarla, texturas 2D, gustos, por qué la aman, fan dubs,
  colaboraciones, obras parecidas, el mundo), antes de los conceptos.
- La tabla **«Cumplimiento del encargo»** y la bitácora de la segunda
  pasada.

**Los ⚠️: 84 antes → 119 ahora.** Suben porque esta pasada **añadió unas
1300 líneas** (8 secciones nuevas, el reparto completo, poses, paletas) y
cada dato de una sola fuente lleva su marca. De los 84 viejos se
resolvieron **unos 30** (lista en §20, «Resuelto»). Los que quedan se
explican en §20 y en la tabla de cumplimiento: sobre todo minutos de
escenas sin clip (Anfiteatro Fantasma, «Henchman», «Marceline's Closet»),
vistas de fan dubs (YouTube cerrado), cantantes latinas de Marceline,
papeles secundarios del doblaje con una sola fuente, y BMO y la corona de
la Dulce Princesa sin medir.

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
| El objeto | **El bajo-hacha de Marceline**, que era **el hacha de la familia** («Is this the family ax? Did you turn it into some kind of lute?», dice su padre en 2×01, ≈2:15) ✅. Y los **discos oficiales que existen de verdad**: la **caja de Mondo** con tres LP de 12", un 10", un CD y un casete (2019) ✅, el LP «Come Along With Me» ✅, el doble LP de «Obsidian» ✅ y «BMO's Mixtape» ✅. Hay **modelos 3D del bajo en Sketchfab**, al menos uno con licencia CC BY-NC-SA ✅. |
| Cuadro de diálogo propio | **No hay globos.** El más reconocible es **la nota de Simon** a Marcy: papel crema arrugado con mayúsculas a mano (hoja `escenas_09` n.º 408, segunda pasada). La serie pone el texto en **papeles escritos a mano**: la nota de Finn («MARCY, PLEASE COME TO THE TREEHOUSE—IT'S AN AMERGENCY!», 3×21) ✅, las **notas de Simón que Marceline canta** en «I Remember You» (4×25, ≈8:49) ✅ y **el cuaderno de letras** de Marceline (3×21, ≈6:36) ✅. Y las **cartelas de título**, pintadas sobre **papel antiguo escaneado** y con **tramado de cómic viejo** ✅. |
| Personaje | **Marceline**, sin duda: es la música de la serie. Es la favorita de mucha gente (BOOM! la llamó «fan-favorite» ✅, *The Guardian* la llamó lo mejor de la serie ✅; tuvo su miniserie «Estacas» y su especial «Obsidian» ✅). **No encontré una encuesta oficial** de popularidad. Secundarios que suman: **BMO** (disco propio y favorito de Pendleton Ward ✅), el **Rey Helado / Simon** (el «mejor personaje» para *Vulture* ✅), **Finn** (beatbox), **Jake** (viola) y la **Dulce Princesa**. |
| Voz latina de Marceline | **Isabel Martiñón** (habla) ✅. Sus canciones las cantaron otras: **Claudia Urbán** (temporadas 1-2), **Patty Urbán** (3-4) y **Carla Cerda** (5 en adelante, «Estacas», «Tierras lejanas») ⚠️. |
| Voces latinas del resto | Finn **José Antonio Toledano** ✅, Jake **José Arenas** ✅, Dulce Princesa **Karla Falcón** ✅, Rey Helado **Óscar Flores** ✅. Estudio **Sensaciones Sónicas** (hasta media temporada 5) y luego **SDI Media de México** ✅. |
| Noticia que viene justo | **«Hora de aventura: Misiones Secundarias»** llega a **Cartoon Network y HBO Max en Latinoamérica el 5 de octubre de 2026**, doblada, con **José Arenas** otra vez como Jake ✅. |
| Letras | Títulos: **Chewy** o **Luckiest Guy** (redondas y gorditas, como el logo). Letra de Marceline a mano: **Rock Salt** o **Permanent Marker**. Pantalla de BMO: **VT323**. Todas con tildes, ñ, ¿ y ¡: **comprobado en el archivo**. |
| Tono | Colores vivos, **línea fina y uniforme**, **brazos de fideo** sin codos, **ojos de punto**. Las escenas de Marceline son **de noche o en su cueva**: morados, rojos y velas. Divertido, pero con un fondo melancólico. |

---

## 2 · Las escenas que sirven para #musica-nueva

Todas salen de las transcripciones de
[guiszk/adventuretime-transcripts](https://github.com/guiszk/adventuretime-transcripts).
El texto entre comillas es **el inglés original**; la traducción es mía,
salvo donde digo que es del doblaje. **Minutos estimados** (ver arriba).

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
  un vídeo de la página latina de la serie en Facebook se titula
  «Marceline: **Papi, te comiste mis papas**», y el disco oficial en
  español la trae con ese mismo título (pista 6, 1:43) ✅
  ([MusicBrainz](https://musicbrainz.org/release-group/1f39e3d6-9a3b-4838-bae0-3e59b37e69eb)).
- **≈2:15**: su padre, Hunson Abadeer, ve el bajo: «Whoa! **Is this the
  family ax?** Did you turn it into some kind of lute?» (¿es el hacha de
  la familia? ¿la convertiste en una especie de laúd?). Y se lo lleva.
- **≈2:23**: Marceline: «**My bass!**» (¡mi bajo!).
- **≈9:17**: Finn saca **un walkman** y pone **la canción que grabaron**
  para distraer al padre. El disco que grabaron al principio **salva el
  episodio**.

> Para la lámina: esta es la escena del **estreno casero**. Un bajo, un
> micro, un amigo haciendo ritmo y una grabadora.

**Visto en vídeo (segunda pasada)** ✅: clip «Marceline Sing-a-Long Fry
Song» de la marca «Toon Tunes» de Cartoon Network, 52 s, 1280×720, con la
letra en pantalla en inglés
([Dailymotion](https://www.dailymotion.com/video/x51arca)):

- **0:00**: Finn hace beatbox de pie; **Marceline flota bocabajo tocando
  el bajo-hacha**, en un cuarto de **paredes rosa** con sillones rojos y
  puerta doble azul.
- **0:12**: primer plano de **una grabadora amarilla** con su cable sobre
  la mesa: el objeto que graba la canción.
- **0:16-0:24**: flota tocando: «Daddy, why did you eat my fries?».
- **0:28-0:36**: **primer plano de su cara cantando triste**, ojos
  entornados y boca abierta: «and I cried, but you didn't see me cry».
- **0:40-0:44**: Finn con **audífonos puestos** sostiene la grabadora en
  alto.
- **0:48**: «Daddy, there were tears there», mirada baja.

Ojo: es un **montaje musical** de Cartoon Network, no el metraje crudo
del episodio. El cuarto rosa puede ser un set simplificado, aunque
coincide con los colores de su casa por dentro (§5).

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

> Para la lámina: la única escena con **los cinco tocando juntos**. Sirve
> para un concepto de grupo.

**Visto en vídeo (segunda pasada)** ✅: «I'm Just Your Problem», del
**canal oficial de Cartoon Network**, 2:07, 1280×720
([Dailymotion](https://www.dailymotion.com/video/x537pqr)):

- **0:00**: la Dulce Princesa sostiene **un aparato verde tipo Game Boy**
  junto a BMO.
- **0:04-0:08**: **Jake corre tocando la viola** y alcanza a Finn.
- **0:12-0:24**: **Marceline entra volando** con el bajo (filos rojos)
  hacia una **puerta de piedra en arco con círculos dorados**, la del
  Señor de las Puertas, y toca sobre ella.
- **0:24-1:00**: lleva **un sombrero de ala ancha color mostaza con cinta
  azul**; primeros planos cantando, ceño fruncido y colmillos a la vista
  ([0:52](https://www.dailymotion.com/video/x537pqr?t=52)).
- **1:12-1:24**: Finn y Jake llegan corriendo junto a la Princesa.
- **1:32**: Marceline, con el sombrero, **toca apoyada en la puerta**
  mientras cae la tarde.

Es **de día, al aire libre**, con cielo despejado: no es la cueva.

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
  ✅ (Doblaje Wiki y la pista 4 del disco en español en
  [MusicBrainz](https://musicbrainz.org/release-group/1f39e3d6-9a3b-4838-bae0-3e59b37e69eb)).

> Para la lámina: **la letra de una canción escrita en un papel viejo**.
> Es la escena que más lloran los fans (ver §14).

**Visto en vídeo (segunda pasada)** ✅: metraje real de la emisión de
Cartoon Network HD, con audio francés, 1:58
([Dailymotion](https://www.dailymotion.com/video/xzt1l7)):

- **0:00-0:12**: el Rey Helado toca un teclado; **Marceline entra con un
  papel en la mano** (paredes rosa, piso verde azulado) y discuten.
- **0:18-0:30**: primer plano de Marceline, **mano en la cabeza, cara de
  angustia**.
- **0:42-1:06**: el Rey Helado toca **una batería verde con «#1» en el
  bombo**; Marceline, sentada, **toca el bajo con cara seria**.
- **1:18**: primerísimo primer plano: **cabeza hacia atrás, dientes
  apretados, una sola lágrima** ([1:18](https://www.dailymotion.com/video/xzt1l7?t=78)).
- **1:36**: **una Polaroid de Marceline niña**, sonriendo. Corrige la
  primera pasada: no sólo hay notas escritas.
- **1:42-1:54**: flashback: **Marceline pequeña con un osito rojo**
  (Hambo) entre ruinas se acerca a Simon.

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
> «estreno en directo» de la serie.

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

**Visto en vídeo (segunda pasada)** ✅: tráiler oficial de «Obsidian»,
1:30, 1920×1080, termina con el logo de HBO Max (1:28)
([Dailymotion](https://www.dailymotion.com/video/x7xejon)):

- **0:16**: Marceline y la Princesa en la **cocina** (piso turquesa,
  gabinetes verdes), **cada una con una taza humeante**. Confirma la
  escena de ≈4:41.
- **0:20**: Marceline, en camiseta gris, **toca el bajo sentada** mientras
  la Princesa cocina detrás.
- **0:36**: **flota tocando el bajo sobre un camino de piedra** hacia el
  Reino de Cristal, con picos morados y una torre al fondo
  ([0:36](https://www.dailymotion.com/video/x7xejon?t=36)).
- **0:44-1:00**: se vuelve **monstruo alado gigante de ojos rojos** y
  pelea; luego vuelve a flotar tocando entre cristales morados y turquesa.
- **1:08**: **bajo al hombro**, de pie junto a la Princesa y dos figuras
  de cristal, luz cálida de atardecer.
- **1:12**: las dos **en una motocicleta** entrando en la ciudad de
  cristal.
- **1:24**: primer plano de Marceline con **cara de susto**, fondo oscuro
  estrellado.

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
> anunciados** desde la temporada 1.

⚠️ «Henchman» (§2.8), el concierto del Anfiteatro Fantasma (§2.5) y
«Marceline's Closet» (§2.2) **no tienen clip** en Dailymotion (se buscaron
por canción y por escena). Sus minutos siguen estimados por transcripción.

### 2.9 El opening y los créditos, vistos enteros (segunda pasada) ✅

- **Opening doblado al latino** (29 s, 1920×1080,
  [Dailymotion, Espinof](https://www.dailymotion.com/video/x8p2dsj)):
  **0:00** laguna helada con montañas; castillo del Dulce Reino con
  personajes; valle verde; la casa del árbol por dentro con Finn, Jake y
  un perrito caliente gigante; Jake tocándose las orejas; Finn y Jake
  corriendo por una cresta bajo nubes de tormenta; y al final el logo
  «ADVENTURE TIME — Created by Pendleton Ward».
- **Créditos en inglés** (33 s, 1280×720,
  [Dailymotion](https://www.dailymotion.com/video/x4fakxm)): fondo **verde
  lima plano** con abejas y mariposas animadas, nombres reales del staff
  («Supervising Director Larry Leichliter», «Lead Character & Prop
  Designer Phil Rynda», «Character & Prop Designers Natasha Allegri, Tom
  Herpich»…) y, al final, los logos de **Frederator Studios** y
  **Cartoon Network Studios**.

---

## 3 · Arte oficial y referencias visuales

> [!note] Segunda pasada: ahora sí hay imágenes vistas
> La primera pasada no pudo abrir ninguna imagen. Ahora hay **model sheets
> de producción** y **concept art** vistos y medidos (§3.7) y **3 hojas de
> contacto** en `hojas/` (§3.8). El resto de esta sección sigue valiendo
> como lista de piezas oficiales y dónde están.

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
| **Marceline Canta: Timeless Songs (Versión en español)** | **Disco oficial en español** con **10 canciones de Marceline** | Hay también **versión en portugués**. Fecha: **25 de octubre de 2019** ✅ (MusicBrainz y la wiki dicen 2019) | [Spotify](https://open.spotify.com/album/6x28Z0ItbmOHSpPUtExumt), [Deezer](https://www.deezer.com/us/album/153622342), [Hora de Aventura Wiki](https://horadeaventura.fandom.com/es/wiki/Marceline_Canta:_Timeless_Songs), [Apple Music](https://music.apple.com/us/album/marceline-canta-timeless-songs/1515397280), [MusicBrainz](https://musicbrainz.org/release-group/1f39e3d6-9a3b-4838-bae0-3e59b37e69eb) |

**Lista del disco en español**, con el título y la duración que da
MusicBrainz (segunda pasada) y, entre paréntesis, el episodio según la
wiki ✅:
1. «¿Qué soy para ti?» 2:41 («Lo que estaba perdido»)
2. «Soy tu problema» 2:00 («Lo que estaba perdido»)
3. «Niño malvado» 1:54 («Muchachito malo»). La wiki lo llamaba «Pequeña
   mujer» ⚠️: vale el de MusicBrainz, que es el de la ficha del disco.
4. «Recordándote» 2:19 («Te recuerdo»)
5. «Ya no lo puedo soportar / Hay un fuego dentro de mí» 1:29 («Incendio»)
6. «Papi, te comiste mis papas» 1:43 («Llegó de la Nocheósfera»)
7. «Todo se queda» 2:26 («Todo se queda / La nube oscura»)
8. «Cadena alimenticia» 1:32 («Cadena alimenticia»)
9. «Siempre entonces se podrá volver» 2:10 («¡Ven conmigo!»)
10. «Acompáñame» 1:49 («¡Ven conmigo!»): es «Come Along With Me».

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

### 3.7 Model sheets y concept art de producción (vistos, segunda pasada) ✅

Todos con el sello **© Cartoon Network Studios** y su ficha de producción
(episodio, id). Tamaños medidos con la API de la wiki.

- **«Marceline In New Outfit Playing Axe Bass — Special Pose A a F»**,
  episodio de producción **062**, ids `C062s074_203` a `C062s089_218`.
  **Seis poses oficiales tocando el bajo**, con el **sombrero de sol
  mostaza**, vestido rojo y botas marrones: es el traje de «What Was
  Missing» (3×10), el mismo que se ve en el clip de §2.3. Las miré:
  - **A**: de pie sobre una cuesta, bajo cruzado, un pie adelantado
    ([1024×608](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/4/45/Modelsheet_marceline_innewoutfit_playingaxebass_-_specialposea.jpg)).
  - **B**: echada hacia atrás, **ojos cerrados, boca abierta cantando**,
    pierna levantada ([1024×608](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/d/d6/Modelsheet_marceline_innewoutfit_playinaxebass_-_specialposeb.jpg)).
  - **C**: doblada hacia atrás casi bocabajo, el bajo en alto
    ([1024×608](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/0/0c/Modelsheet_marceline_innewoutfit_playingaxebass_-_specialposec.jpg)).
  - **D y E**: **sentada en el aire**, flotando, bajo vertical, en línea
    sin color ([D](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/5/59/Modelsheet_marceline_innewoutfit_playingaxebass_-_specialposed.jpg),
    [E](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/1/13/Modelsheet_marceline_innewoutfit_playingaxebase_-_specialposee.jpg)).
  - **F**: primer plano, cabeza ladeada bajo el ala del sombrero,
    **cantando con la boca muy abierta**
    ([1024×608](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/7/7b/Modelsheet_marceline_innewoutfit_playingaxebass_-_specialposef.jpg)).
- **«Marceline — New Costume #1»**, ep. **057**, id `C057s011_472`: de
  frente y de espaldas, **vestido camisero azul grisáceo** y **zapatos
  granate**
  ([4079×2421](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/3/34/Modelsheet_Marceline_-_New_Costume_-1.png)).
  Hex medidos en §16.
- **«Marceline Stock Night»**: vuelta de caminata en 4 poses, en gris de
  construcción, para proporciones
  ([5100×3300](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/0/0b/Modelsheet_marceline_stocknight.jpg)).
- **«Marceline Bat» 1 y 2**: bocetos a lápiz de su forma de murciélago,
  firmados «Bat Marceline Rough — Phil»
  ([3600×3000](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/9/9b/Modelsheet-MarcelineBat1.jpg)).
- **«Modelsheet axbass withrims»**: **el bajo-hacha solo**, en rojo, con
  sus llantas marcadas
  ([4104×2454](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/5/58/Modelsheet_axbass_withrims.png)).
  La mejor referencia para modelarlo.
- **«Original Finn»** y **«Jakesalad»**: model sheets a color de Finn y
  Jake ([1467×2385](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/f/f3/Original_Finn.png),
  [1700×2455](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/3/3b/Jakesalad.png)).
- **Bocetos de vestuario de Tom Herpich** para el final («Come Along with
  Me original costume sketches for Marceline», 1280×1673) y
  «Modelsheet princessbubblegumtiedup» (1478×1494).
- **Concept art de «Obsidian»** (galería `Obsidian-concept-1` a `-15`,
  subida el 30-ene-2021): el **9** son bocetos a lápiz rojo de los
  «Shards» del Reino de Cristal
  ([1002×810](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/9/9e/Obsidian-concept-9.png));
  el **1**, la montaña-criatura de tinta negra
  ([1280×989](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/3/38/Obsidian-concept-1.png)).
- **Logo oficial**: [1069×519](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/thumb/b/bd/Adventure_Time_logo.png).

### 3.8 Las hojas de contacto (en `hojas/`) ✅

`investigar_serie.py` sobre la wiki inglesa (páginas Marceline Abadeer,
Finn the Human, Jake the Dog, Princess Bubblegum, Ax Bass y BMO) juntó
**1188 imágenes** en 13 hojas. Hay 3 en `hojas/`. Los números son los de
cada hoja; el nombre del archivo va debajo de cada miniatura.

**`personajes_01.jpg`** (1-48): lo mejor para **vestuario y producción**.
- **1** «Stock Night», **2-4** Marceline murciélago, **5** el bajo-hacha
  con llantas, **9-14** «New Costume» 1 a 3 (varios trajes de día),
  **15** Marceline gritando (pose especial, ojos rojos), **17** Marceline
  adolescente, **18** Marceline niña, **20** el traje con **sombrero de
  sol**.
- **25** «S2e1 Drama bomb» (suéter a rayas, noche), **35** Simon y Marcy
  en moto (5×14), **36** «**S7e7 Marceline playing ax bass**»: de pie en
  un huerto, **tocando de verdad**, 2880×1620. **La mejor pose con su
  instrumento.**
- **43** la Dulce Princesa con cinta adhesiva, **45** Jake, **48** Finn
  (model sheets a color).

**`personajes_02.jpg`** (49-96): lo mejor para **la Dulce Princesa**.
- **49** el bajo-hacha solo sobre verde, **51** «Marceline Presentation»
  (de cuerpo entero, fondo blanco), **62** BMO transformándose, **64**
  Marceline con ropa informal (model sheet).
- **67-96**: capturas de 1920×1200 de la Dulce Princesa en muchos trajes
  (capa roja de «Stakes», bata de laboratorio, vestido de fiesta, en la
  playa con Finn y Marceline con su paraguas, **94**).

**`escenas_09.jpg`** (385-432): lo mejor para **Marceline y Simon** y para
las escenas que hacen llorar.
- **385** Marceline presenta a sus fantasmas en su **casa rosa** (2×26),
  **386** asusta a Finn y Jake en el **sofá rojo**.
- **391-393** «What Was Missing» (3×10): con la Princesa y el sombrero de
  sol, y **393 cantando sobre la puerta dorada**
  ([1920×1080](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/d/d3/S3e10_Marceline_singing.png)).
- **396-408** «I Remember You» (4×25): **396** tocando con el Rey Helado
  en la batería, **403** Marceline con el **omnichord**
  ([1920×1080](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/8/80/S4e25_Marceline_playing_Omnichord.png)),
  **404** **la lágrima**
  ([1920×1080](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/2/2f/S4e25_Marceline_shedding_a_tear.png)),
  **407** Marcy niña sin Hambo y **408** **la nota de Simon escrita a
  mano** («Marceline, is it just you & me in the wreckage of the
  world?…»)
  ([1920×1080](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/d/d2/S4e25_Simon%27s_note_to_Marcy.png)).
  **Es la referencia del papel y la letra de la hoja de canciones del
  concepto A y de la setlist del concepto B.**
- **417-424** «Simon & Marcy» (5×14): baloncesto, en el puente, viendo
  una película con Simon; **423** llorando con Hambo (5×29).
- **425-431** capturas de 5×38 con Finn, Jake y la Princesa; **432**
  «Betty» (5×48), Marceline en grupo con Betty, Finn y Jake.

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D del bajo-hacha (Sketchfab)

**Segunda pasada**: las licencias se leyeron en la **API de Sketchfab**
(`api.sketchfab.com/v3/search`), que es quien certifica la licencia. Donde
dice «API» está comprobado. Los que siguen «sin ver» no traían el campo
de licencia en esa consulta: **mira su ficha antes de usarlos**.

| Modelo | Autor | Licencia | Nota |
|---|---|---|---|
| [Marceline's Ax Bass](https://sketchfab.com/3d-models/marcelines-ax-bass-2224d0a363a24ba883614f209761454c) | **Yogensia** | **CC BY-NC-SA 4.0** ✅ (ficha y API) | Descargable. Crédito: «Marceline's Ax Bass» by Yogensia, CC BY-NC-SA 4.0. **Sin uso comercial**: vale para el Discord si no se vende nada |
| [Marceline's Ax Bass](https://sketchfab.com/3d-models/marcelines-ax-bass-417178d709774642b0d5b5a02181caa2) | Haxis | **CC BY** ✅ (API) | **El más libre**: permite uso comercial con crédito. Crédito: «Marceline's Ax Bass» by Haxis, CC BY |
| [Low Poly Marceline's Ax Bass](https://sketchfab.com/3d-models/low-poly-marcelines-ax-bass-adventure-time-101d7036f35b411295e6a500c86e952b) | Roberto Cuxil (@cuxilrodas) | **«Free Standard»**, NO es CC (API) | Texturas pintadas en Blender con aspecto de dibujo animado, la más fiel al estilo, **pero sólo para mirar**: pedir permiso al autor |
| [Marceline's Axe Bass](https://sketchfab.com/3d-models/marcelines-axe-bass-477b56a2db134065947b2c931c52b3aa) | denizin | **CC BY-NC** ✅ (API) | textura iridiscente (se aleja del estilo plano) |
| [Marceline axe bass guitar](https://sketchfab.com/3d-models/marceline-axe-bass-guitar-adventure-time-9bc622d77287423391e4e5451c05ca77) | Z3bbz | sin ver ⚠️ | |
| [Marceline Bass Axe](https://sketchfab.com/3d-models/marceline-bass-axe-b6f6f74eb92f4bbfbcbd2d4d01f3b8df) | Froes | sin ver ⚠️ | 16,5 mil triángulos |
| [(SGP) Marceline's Bass Axe](https://sketchfab.com/3d-models/sgp-adventure-time-marcelines-bass-axe-6e72178681c44722a0cb5226deff7e8e) | TravisEvashkevich | sin ver ⚠️ | |
| [Marceline's Bass Guitar](https://sketchfab.com/3d-models/marcelines-bass-guitar-4d89b7121de54b4e9410f4472fa1bab6) | deadlygeek | sin ver ⚠️ | |
| [Marceline's guitar bass](https://sketchfab.com/3d-models/marcelines-guitar-bass-c003bed4b97244d1b705626dd5bb5e69) | Hoho (@hoho03) | sin ver ⚠️ | trae versión alta y baja en polígonos |
| [Marceline's Axe Bass](https://sketchfab.com/3d-models/marcelines-axe-bass-e111ddfd74f9426dab13a70fce789d44) | 10958533 | sin ver ⚠️ | |
| [Axe bass – Marceline](https://www.artstation.com/artwork/BmZxOm) (ArtStation) | Victor Cavalcante Vk | sólo para mirar | render 3D |
| [Marceline`s Bass guitar](https://sketchfab.com/3d-models/none-bac567bac05b46039f0e5510bf0c3062) | coffe0wolf | **CC BY-NC** ✅ (API) | nuevo en la segunda pasada |
| [Marceline's Axe/Guitar](https://sketchfab.com/3d-models/none-412c96ee288a4bcdb01a7433dff90fa7) | ScoobSter_ | **CC BY** ✅ (API) | nuevo |

### 4.1.b Personajes y sitios en 3D con licencia (API de Sketchfab, segunda pasada) ✅

| Modelo | Autor | Licencia (API) | Para qué |
|---|---|---|---|
| [Marceline the vampire queen](https://sketchfab.com/3d-models/none-f520806111dc454ba3455947e51b04de) | coffe0wolf | **CC BY** | Maniquí del cuerpo entero de Marceline: proporciones y volumen |
| [Finn - (Adventure Time)](https://sketchfab.com/3d-models/finn-adventure-time-309e158598764644a5c6068e0cfdc898) | Agu.3D | **CC BY** | Finn, 64 992 caras, el más completo para posar |
| [Finn Adventure Time](https://sketchfab.com/3d-models/none-19255b56148247eaa213bff7974304a4) | Nico Caraballo (theniloart) | **CC BY** | Finn ligero (1 548 caras), para pruebas |
| [Finn - Adventure Time](https://sketchfab.com/3d-models/none-b3c5b1d5e4274eb0ba7f42ea00ed0ad2) · [Finn's Demon Blood Sword](https://sketchfab.com/3d-models/none-7f919633863140a49e6d51a8f0d87aab) | RenataDiFlorio · Haxis | **CC BY** | Finn y su espada |
| [Jake](https://sketchfab.com/3d-models/jake-6326c036c6f14d09bf0708ca4289d699) · [Jake el Perro Toon](https://sketchfab.com/3d-models/none-6fd2e3f4ef614842add5cec885cec2f2) | Mormont · Luis Angel | **CC BY** | Jake |
| [Bmo - Adventure Time](https://sketchfab.com/3d-models/none-ffeb3e9ab97e4e3dbed4ddc0650d8b9b) · [Adventure Time BMO](https://sketchfab.com/3d-models/none-57a8b359d2ad41a3bacc41facfc77531) | featbear456978 · ezgibakim | **CC BY** | BMO, para el concepto con su pantalla |
| **[The Treehouse](https://sketchfab.com/3d-models/none-0131dc63d8894892b0c87dc852f23984)** · [Finn and Jake's Treehouse](https://sketchfab.com/3d-models/none-a390d3c9873c4c219959d0b930aabe52) | gleksono | **CC BY** | **La casa del árbol entera**: un sitio real en 3D, con luz de verdad |

**Recomendación nueva**: el bajo de **Haxis** (CC BY, el más libre) o el de
**Yogensia** (CC BY-NC-SA, sin vender nada); el cuerpo de **coffe0wolf**
como maniquí. **Figura de referencia 3D**: el **Funko Pop! #301 de
Marceline con guitarra** (punto 23).

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

### 4.3 Fotos con licencia libre (Openverse)

Son **disfraces caseros** de Halloween (usuario «Violently Japy» en Flickr,
CC BY-NC 2.0), no cosplay de estudio: están en `referencias.json` pero sirven
poco. El **cosplay bien hecho, con materiales reales**, está en el punto 23.

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

### 5.2 Luz (segunda pasada: vista en vídeo donde se pudo)

- **La casa por dentro**: luz **plana y cálida**, paredes rosa, casi sin
  sombras ✅ (vista en «Fry Song» y en la cocina del tráiler de
  «Obsidian»).
- **La puerta del Señor de las Puertas** («I'm Just Your Problem»): **tarde
  despejada**, nubes blancas iluminadas, **al aire libre** ✅. No es la
  cueva: la primera pasada mezclaba los dos sitios.
- **El Reino de Cristal**: luz **violeta y magenta fría** con toques cian,
  de noche mágica; sombreado **pintado, con degradado**, más que en la
  serie normal (lo da `estilo.py` en el fotograma 0:44 del tráiler) ✅.
- **Créditos**: verde lima plano con insectos animados; es color de marca,
  no un sitio ✅.
- Cueva: luz **fría, azul violeta**, con puntos cálidos de **velas**;
  reflejos de la laguna ⚠️ (de memoria: no hubo clip de la cueva).
- Escenario del cementerio: **noche**, niebla verde azulada y un foco ⚠️
  (de memoria, sin clip).
- Casa del árbol: **luz de tarde dorada** por ventanas redondas ⚠️ (de
  memoria; hay modelo 3D CC BY para ponerle luz real, §4.1.b).

### 5.2.b Paleta MEDIDA en fotogramas reales (segunda pasada) ✅

Medida con `estilo.py` y Pillow sobre fotogramas de los clips de §2 y sobre
model sheets. **Usa esta tabla antes que la de 5.3.**

| Qué | Hex medido | De dónde |
|---|---|---|
| Casa de Marceline: pared rosa | **`#F8AEC5`** (37 % del cuadro) | «Fry Song», 0:16 |
| Casa: techo o pared clara | `#FBE0E8` | «Fry Song», 0:16 |
| Casa: sillón rojo | `#D94344` | «Fry Song», 0:00 |
| Cocina de la casa: fondo rojo vino | `#4D252C` | tráiler «Obsidian», 0:16 |
| Cocina: electrodomésticos turquesa | `#5B8890` | tráiler «Obsidian», 0:16 |
| Cocina: pared rosa en sombra | `#B04E5E` | tráiler «Obsidian», 0:16 |
| Reino de Cristal: camino y cielo violeta | **`#422D6B`** (36 %) | tráiler «Obsidian», 0:44 |
| Reino de Cristal: violeta medio | `#6A53A0` | tráiler, 0:44 |
| Reino de Cristal: rosa de luz | `#E7D1D9` | tráiler, 0:44 |
| Reino de Cristal: magenta de acento | `#8F3F6E` | tráiler, 0:44 |
| Reino de Cristal: cian pálido del cristal | **`#E1F7F9`** (53 %) | tráiler, 0:00 |
| Reino de Cristal: cielo claro | `#BDE0F5` | tráiler |
| Picos de cristal | `#9055C3` y `#D3A0E8` | tráiler, 1:00 |
| Cielo de «I'm Just Your Problem» | `#EFEFFF` / `#A5B9F6` | clip CN, 0:52 |

Marco de ventana gris azulado de la casa: `#7A8A96` ⚠️ (a ojo; el
programa no lo separó).

### 5.3 Paleta de la primera pasada ⚠️ (de memoria; donde choque con 5.2.b o §16, manda lo medido)

Corregido en la segunda pasada: piel de Marceline → `#D8E7E7` (§16), pelo
→ `#000000`, Finn: la camiseta medida es `#018BCB` y la mochila
`#7BBB59`; Jake `#FEB925`; Dulce Princesa `#ED8ACE` / `#F3BBFB`; casa rosa
por dentro `#F8AEC5`.

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
  **ambientCG** (CC0) o la [sección de texturas de Poly Haven](https://polyhaven.com/textures) ✅.
  Segunda pasada, nombres exactos sacados de la API de ambientCG, todos
  **CC0**: papel **Paper001-006**
  ([ambientCG](https://ambientcg.com/list?type=Material&q=paper)), cartón
  **Cardboard001-004**
  ([ambientCG](https://ambientcg.com/list?type=Material&q=cardboard)),
  madera del mástil **Wood092, Wood094, Wood095**
  ([ambientCG](https://ambientcg.com/list?type=Material&q=wood)), tela
  **Fabric081C, Fabric061, Fabric066**
  ([ambientCG](https://ambientcg.com/list?type=Material&q=fabric)), cuero
  de las botas **Leather026, 030, 037, 038**
  ([ambientCG](https://ambientcg.com/list?type=Material&q=leather)).
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
  **Segunda pasada: bajada y revisada con fontTools** desde
  [dafont](https://www.dafont.com/adventure-time.font). Tiene dibujos
  para á é í ó ú ñ ¿ ¡ ü, **pero sólo en la tabla Mac Roman**: no trae
  tabla Unicode de Windows. En Photoshop sobre Windows, la ñ o el ¿
  **probablemente no salgan** ✅. **No usarla para texto en español**:
  sólo para las palabras «Adventure Time» tal cual.
- **Las cartelas de título**: cada una **rotulada a mano** por el pintor,
  distinta en cada episodio, sobre papel viejo ✅ (ver §3.2).
- **Los cómics de BOOM!**: globos con letra de cómic a mano. El letrista
  es **Steve Wands** ✅ ([Adventure Time Wiki](https://adventuretime.fandom.com/wiki/Steve_Wands),
  [League of Comic Geeks, n.º 41](https://leagueofcomicgeeks.com/comic/3374523/adventure-time-41)).

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

Segunda pasada: **VT323, Press Start 2P, Creepster, Eater, Rubik Doodle
Shadow y Bungee** se volvieron a bajar de
[Fontsource](https://cdn.jsdelivr.net/fontsource/fonts/vt323@latest/latin-400-normal.woff2)
y a revisar con fontTools: las seis traen las 15 letras ✅. **Ojo**: baja
el subset **«latin»**, no «latin-ext»: los acentos españoles están en
«latin»; el «latin-ext» sólo no los trae.

### 6.3 Una letra para cada uso

La serie no tiene globos ni onomatopeyas en pantalla (§7): lo de abajo es
la propuesta para la lámina con las letras ya comprobadas.

| Uso | Letra | Por qué |
|---|---|---|
| Logo o título | **Chewy** (o Luckiest Guy) | gordita y redonda como el rótulo del logo |
| Texto normal que dice un personaje | **Mali SemiBold** | de mano, clara en el celular |
| Grito | **Luckiest Guy** en mayúsculas | pesada, de cartel |
| Pensamiento o nota íntima de Marceline | **Rock Salt** o **Permanent Marker** | su cuaderno de letras |
| Nota de Finn | **Gochi Hand** o **Short Stack** | lápiz de niño (la nota del «AMERGENCY») |
| Onomatopeya (si hace falta una) | **Bungee** | bloque de póster; úsala poco: la serie no las dibuja |
| Cartel del mundo (concierto, Dulce Reino) | **Baloo 2** o **Fredoka**; **Creepster** para una palabra vampira | letreros redondos de Ooo |
| Interfaz de juego o pantalla de BMO | **VT323** o **Press Start 2P** | píxel, de consola vieja; Card Wars usa letra blanca gruesa tipo **Luckiest Guy** en sus botones |
| Subtítulos o créditos | **Mali** o **Patrick Hand** | los créditos reales usan letra de palo sencilla sobre verde lima (§2.9) |

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
     sale de las notas**. Segunda pasada: la nota se ve entera en la hoja
     `escenas_09`, n.º **408**: **papel crema arrugado, letra de
     mayúsculas a mano en tinta negra, ligeramente inclinada** («Marceline,
     is it just you & me in the wreckage of the world?…») ✅
     ([captura 1920×1080](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/d/d2/S4e25_Simon%27s_note_to_Marcy.png)).
     Y en el clip de la escena sale además **una Polaroid** de Marcy niña
     (1:36). **Este papel es el cuadro de diálogo más reconocible de la
     serie.**
2. **El cuaderno de Marceline** ✅: lo abre para cantar la «Canción del
   diario» (3×21, ≈6:36). Y su álbum sale de **quinientos años de
   diario**.
3. **Las cartelas de título** ✅: ilustración pintada con el título
   rotulado a mano, **papel viejo escaneado de borde** y **tramado de
   cómic** (§3.2). Es lo más parecido a una «caja de texto oficial».
4. **La pantalla de BMO**: su cara es una pantalla; a veces muestra
   imágenes o texto de videojuego. Segunda pasada: su diseño es **parodia
   de las consolas portátiles retro de Nintendo** ✅ (dos fuentes: un
   [mod real de Game Boy Color convertido en BMO](https://www.instructables.com/Adventure-Times-BMO-Roommate-GBC-Mod/)
   y la web oficial interactiva de Active Theory para «Tierras lejanas:
   BMO», que usa su cara como menú,
   [resumen en Medium](https://medium.com/active-theory/adventure-time-distant-lands-bmo-5997687372b7)).
   Su cara en calma: **dos curvas de ojos cerrados y una boca curva**
   (clip de «The More You Moe», [2:36](https://www.dailymotion.com/video/x3q931u?t=156)).
   ⚠️ Sigue sin fotograma de **texto escrito** en su pantalla.
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
- En los cómics sí hay globos (BOOM!, rotulados por **Steve Wands** ✅),
  redondos y de línea negra fina ⚠️ (forma de memoria). Si al final se usa
  un globo, que sea **de cómic de BOOM!**, con cola curva y letra de mano,
  **nunca** una burbuja blanca lisa genérica.

### 7.3 En los videojuegos

- Hay muchos: **«Hey Ice King! Why'd You Steal Our Garbage?!!»**
  (WayForward, DS y 3DS, 2012; Pendleton Ward ayudó con la historia),
  **«The Secret of the Nameless Kingdom»** (2014), **«Pirates of the
  Enchiridion»** (2018) ✅
  ([Gaming Nexus](https://www.gamingnexus.com/Article/Adventure-Time-Hey-Ice-King!--Whyd-you-steal-our-garbage!!/Item3804.aspx),
  [Destructoid](https://www.destructoid.com/reviews/review-adventure-time-pirates-of-the-enchiridion/),
  [IMDb](https://www.imdb.com/title/tt9863808/)).
- **«Hey Ice King!» (DS)**, segunda pasada: vista la hoja de sprites
  **«Mugshots»**, 759×673: **retratos de cuerpo entero, simplificados**,
  de unos 28 personajes (Finn, Jake, BMO, Dulce Princesa, Flama Princesa,
  Rey Helado, Marceline, Lady Arcoíris, Gunter…), hechos para ir **junto
  al cuadro de texto** ✅
  ([The Spriters Resource](https://www.spriters-resource.com/ds_dsi/adventuretimehicwysog/asset/54668/)).
- **«Card Wars»** (app, 2014-2019): vista una captura del menú, 2560×1440.
  **Marcos metálicos biselados azul grisáceo**, barra de vida y XP con
  **retrato** arriba a la izquierda, monedas y gemas arriba a la derecha,
  tapete **hexagonal** de madera y piedra, y un **botón rojo redondeado
  «BATTLE!»** con letra blanca gruesa ✅
  ([GitHub shishkabob27/CardWars](https://github.com/shishkabob27/CardWars),
  [captura](https://i.imgur.com/cXUolY0.jpg)).
- ⚠️ **No encontré** la caja de texto en sí de «The Secret of the Nameless
  Kingdom» ni de «Pirates of the Enchiridion» (la API de Steam no dio sus
  fichas; TCRF da 403).

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

Segunda pasada: cada ficha lleva un bloque **«A fondo»** con la wiki
inglesa leída entera por su API
([Marceline](https://adventuretime.fandom.com/wiki/Marceline),
[Finn](https://adventuretime.fandom.com/wiki/Finn),
[Jake](https://adventuretime.fandom.com/wiki/Jake),
[Princess Bubblegum](https://adventuretime.fandom.com/wiki/Princess_Bubblegum),
[BMO](https://adventuretime.fandom.com/wiki/BMO),
[Ice King](https://adventuretime.fandom.com/wiki/Ice_King)) y **su cara en
una emoción, vista en vídeo con minuto**. Los gustos van en el punto 20.

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
- **A fondo** ✅: al principio es **antagonista traviesa** («Evicted!»,
  1×12) hasta que Finn ve que es «a radical dame who likes to play
  games». Debajo de la fachada dura es **muy sentimental**: rompió con su
  ex **Ash** cuando él vendió a Hambo. **Le cuesta decir lo que siente si
  no es cantando** («Fry Song», «I'm Just Your Problem»). Arco: de villana
  traviesa → amiga más madura que acepta su inmortalidad → en «Obsidian»,
  **madura sin perder lo juguetón**. Su miedo de fondo es **el peso de la
  inmortalidad**: ver morir a quien quiere, y el precio de sus poderes
  («Stakes»). Pendleton Ward dijo que su popularidad **«creció
  enormemente»** tras su primer episodio.
- **Qué transmite**: la amiga mayor, cool y un poco triste. Da ganas de
  que la dejen tocar en paz y a la vez de abrazarla.
- **Su cara, vista en vídeo** ✅:
  - **Tristeza**: primerísimo primer plano, **cabeza echada atrás, dientes
    apretados en triángulo, una sola lágrima** de un ojo cerrado, cantando
    con Simon a la batería («I Remember You», clip oficial,
    [1:18](https://www.dailymotion.com/video/xzt1l7?t=78)).
  - **Dolor o pensar**: de pie, **mano en la cabeza**, cara de angustia
    (mismo clip, [0:24](https://www.dailymotion.com/video/xzt1l7?t=24)).
  - **Rabia al cantar**: **ceño fruncido, colmillos a la vista**, canta con
    fuerza («I'm Just Your Problem», [0:52](https://www.dailymotion.com/video/x537pqr?t=52)).
  - **Susto**: ojos muy abiertos, fondo oscuro estrellado (tráiler de
    «Obsidian», [1:24](https://www.dailymotion.com/video/x7xejon?t=84)).
  - **Cantar algo íntimo**: ojos entornados, boca abierta («Fry Song»,
    [0:32](https://www.dailymotion.com/video/x51arca?t=32)).
  - ⚠️ Alegría y vergüenza: sin fotograma propio todavía.

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
- **A fondo** ✅: impulsivo y a veces de mal genio, pero **bondadoso,
  valiente y con un código moral casi absoluto**: le cuesta hasta robar en
  una misión («City of Thieves»). Hace de «sheriff moral» de Ooo. Arco: al
  saber que su padre humano es un egoísta («Wake Up», «The Tower») casi cae
  en la venganza y aprende a controlarla; madura en el amor (besa a la
  Princesa en «Too Young», sale con la Princesa Flama) tras **vomitar de
  vergüenza** con escenas románticas en «Go With Me». **Casi nunca llora**:
  sólo ante algo devastador («Dad's Dungeon»). Sus muletillas matemáticas
  («mathematical», «rhombus», «algebraic») **le sirven de palabrota**.
- **Qué transmite**: el niño que crece con su público; *Entertainment
  Weekly* lo compara con los que crecieron con Harry Potter (punto 21).
- **Su cara, vista en vídeo** ✅: **vergüenza**, óvalo rosa claro en las
  mejillas, **boca en rayita recta**, ojos redondos con la pupila de punto
  descentrada (piloto subtitulado,
  [6:00](https://www.dailymotion.com/video/x84oaz2?t=360)).

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
- **A fondo** ✅: relajado, **cero preocupado**, tira de sus poderes o de
  Finn para salir de líos; hace de **mentor sabio** con consejos que van de
  brillantes a absurdos. A veces es **irresponsable** y deja a Finn solo,
  pero **siempre aparece cuando hace falta**. La wiki apunta que quizá es
  disléxico y tiene rasgos de TDAH ⚠️ (lo dice como «posible», no es
  oficial).
- **Su cara, vista en vídeo** ✅: **alegría y orgullo**, ojos enormes casi
  todo blancos con una franja negra abajo y **sonrisa ancha de dientes
  cuadrados**, al ver el «Jakeseum» («Jake the Starchild», clip oficial,
  [1:39](https://www.dailymotion.com/video/x6gkz32?t=99)). Ojo: ahí se ve
  **azulado** por la luz de noche, no amarillo.

### Dulce Princesa (Princess Bubblegum, Bonnibel)

- **Quién es**: la **gobernante del Dulce Reino** y **científica** ✅
  (wikis). Tiene **827 años** ✅ (ver «A fondo»).
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
- **A fondo** ✅: amable y educada, pero con un lado **frío y hasta un
  poco macabro**: corta y reconecta extremidades de criaturitas «sin
  dolor» («The Lich»), bromea con venenos («The Other Tarts»). **Muy
  racional**, cree que «toda magia es ciencia». Bajo estrés extremo **come
  de más**. Tiene **827 años** según *Explore the Dungeon Because I DON'T
  KNOW!* y es más joven que Marceline según *The Art of Ooo*. Es el
  personaje con **más vestuarios** de la serie.
- **Su cara, vista en vídeo** ✅: **preocupación**, ojos muy redondos con
  brillo blanco, boquita entreabierta y **manos juntas contra el pecho**,
  cuando su experimento de revivir un ratón se le va de las manos
  («Slumber Party Panic», 1×01, clip de CN,
  [2:12](https://www.dailymotion.com/video/x8ghhnc?t=132)).

### BMO

- **Quién es**: una **consola de videojuegos viva** que vive con Finn y
  Jake ✅ (wikis).
- **En la música**: canta «**Time Adventure**» en el final, con Jake en
  brazos, y grita «**My art is a weapon!**» (10×13, ≈35:55-37:00) ✅.
  Tiene **disco propio**: «BMO's Mixtape» (§3.4) ✅. La Princesa le hace
  sonar «Sound Structure Alpha» (3×10) ✅.
- **Cómo habla**: como un niño pequeño muy seguro de sí mismo; habla de
  sí en tercera persona a veces ✅ (confirmado en su ficha de la wiki).
- **A fondo** ✅: dice «I am incapable of emotion», pero **llora, se enoja
  y se pone celoso**. Muy protector («If anyone tries to hurt Finn, I will
  kill them»). **Media cuando Finn y Jake se pelean** (edita su película en
  «Video Makers» para arreglarlo). **Era el personaje favorito del propio
  Pendleton Ward** (entrevista con Hot Topic, citada en la wiki).
- **Su cara, vista en vídeo** ✅: **calma**, ojos cerrados en dos curvas y
  boca curva hacia arriba, en brazos de su creador («The More You Moe, The
  Moe You Know», 3.ª temporada,
  [2:36](https://www.dailymotion.com/video/x3q931u?t=156)).

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

### Rey Helado / Simon Petrikov (el secundario más querido por la crítica)

- **Como Simon**: arqueólogo inteligente y cariñoso, capaz de un enorme
  sacrificio: **cuidó a Marceline niña en el apocalipsis** mientras la
  corona lo volvía loco. Sus cartas a ella («I Remember You») muestran
  que **temía abandonarla** ✅.
- **Como Rey Helado**: en las primeras temporadas, **villano pesado «tipo
  Gargamel»**; desde la 3.ª, **personaje trágico y solo** que quiere
  casarse con una princesa **sin recordar por qué**: el eco de haber
  perdido a **Betty** ✅. *Vulture* lo llamó **«el mejor personaje de Adventure
  Time»** y lee su arco como una metáfora del **Alzheimer** ✅
  ([Wikipedia: Ice King](https://en.wikipedia.org/wiki/Ice_King)).
- **Cómo se expresa**: optimista incluso en lo peor. En el final consuela
  a Finn: nadie elige cómo morir, pero al menos estaban juntos ✅.
- **Su cara, vista en vídeo** ✅: **molesto y cómico**, en el piloto, con
  Finn haciéndole una llave por detrás; dice «**Eso... es estúpido**»
  (subtítulo del clip): cejas caídas, ojos entrecerrados, **boca en
  zigzag** ([4:05](https://www.dailymotion.com/video/x84oaz2?t=245)).
- **Voz latina**: **Óscar Flores** en toda la serie ✅ (§10).

### Dinámicas (para láminas en grupo) ✅

- **Marceline y la Dulce Princesa**: de la tensión con humor a **pareja
  oficial** (beso en el final, 10×13; «Obsidian», ríen juntas).
- **Marceline y Simon**: padre e hija adoptivos. Ella (y Betty) es la única
  que lo llama «Simon», y él lo acepta de ella.
- **BMO media** entre Finn y Jake.
- **Jake, el hermano sabio pero disperso; Finn, el impulsivo con código
  moral**: ese contraste es la base cómica del dúo.
- **Quién hace reír a Marceline**: Finn, al que chincha; **con quién
  discute**: su padre Hunson y, al principio, la Princesa.

---

## 9 · ¿Quién es el más querido?

- **No encontré una encuesta oficial** de Cartoon Network ni de la
  productora.
- Lo que sí hay:
  - La editorial **BOOM!** llamó a Marceline «**fan-favorite**» en la nota
    de prensa de «Marceline and the Scream Queens» ✅ (lo citan
    [Wikipedia](https://en.wikipedia.org/wiki/Marceline_the_Vampire_Queen)
    y la [Adventure Time Wiki](https://adventuretime.fandom.com/wiki/Marceline),
    leídas enteras en la segunda pasada).
  - «Evicted!» (su primer episodio) **disparó su popularidad**, según el
    propio **Pendleton Ward** ✅ (mismas dos fuentes).
  - **CartoonNetwork.co.uk** la nombró **«Character of the Week»** el **24
    de enero de 2012** ✅ (mismas dos fuentes).
  - ***The Guardian*** la llamó **lo mejor de la serie** en una reseña del
    DVD, «responsable de algunas de las mejores canciones» ✅ (mismas dos).
  - **WhatCulture** (2016) la puso **n.º 4** de los mejores personajes, «el
    personaje más cool de la serie» ⚠️ (sólo la cita de la wiki).
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
  - **Segunda pasada, los rivales**: el crítico **Eric Thurm** (*Vulture*)
    llamó al **Rey Helado / Simon** «el mejor personaje de Adventure Time»
    ✅ ([Wikipedia: Ice King](https://en.wikipedia.org/wiki/Ice_King) y la
    [wiki](https://adventuretime.fandom.com/wiki/Ice_King)). **BMO era el
    favorito del propio Pendleton Ward** ✅ (entrevista con Hot Topic, en su
    [ficha](https://adventuretime.fandom.com/wiki/BMO)). **Fionna** tuvo su
    serie propia, «Fionna & Cake» (2023-2024) ✅.
  - Ranker sigue sin abrirse (da **401**): no hay orden del voto del
    público ⚠️.
- **Conclusión**: para un canal de música, **Marceline no es sólo la
  más querida: es la única música de verdad del reparto**. El **Rey
  Helado / Simon** es el favorito de la crítica y el que más hace llorar:
  es el mejor secundario para una lámina 2 o para acompañarla (tocan
  juntos en «I Remember You»). Finn y Jake
  sirven de acompañantes (beatbox y viola), y **BMO** es el secundario
  más tierno con disco propio.

---

## 10 · Doblaje latino

> **Segunda pasada**: la página entera de
> [«Hora de aventura» en Doblaje Wiki](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Hora_de_aventura)
> (87 135 caracteres) **sí se leyó** por su API con `curl -A "Mozilla/5.0"`.
> Es la fuente 1 de cada nombre; la 2 va en la tabla. En la primera
> pasada todo salía de resúmenes de búsqueda.

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
  Dubbing Studios** ✅ (Doblaje Wiki).
- **Dirección**, tabla exacta de Doblaje Wiki (segunda pasada) ✅:

  | Director | Temporadas |
  |---|---|
  | **Óscar Flores** (además, el Rey Helado) | 1.ª-2.ª, 4.ª (eps. 96-101), 5.ª (desde el 131) |
  | Rafael Pacheco | 3.ª, 8 episodios |
  | Circe Luna | 3.ª y 4.ª, algunos |
  | Elsa Covián | 4.ª, algunos |
  | Carlos Hugo Hidalgo | 4.ª, algunos (retake de sonido) |
  | Juan Antonio Edwards | 3.ª, algunos |
  | *(sin datos en la wiki)* | 5.ª hasta el episodio 130 |
  | **Arturo Castañeda** | **6.ª-9.ª** |

  **Arturo Castañeda** es hijo de **Mario Castañeda** (la voz de Goku) y
  Rommy Mendoza; de niño dobló a Harry Potter en *La piedra filosofal* ✅
  ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Arturo_Casta%C3%B1eda),
  [Comic Fest Juárez](https://www.facebook.com/comicfestjuarez/posts/arturo-casta%C3%B1eda-doblajeactor-y-director-de-doblaje-mexicano-hijo-de-los-tambi%C3%A9n/811605114317097/)).
  **Mario Castañeda** fue productor ejecutivo en las temporadas 5.2-6 ⚠️
  (sólo Doblaje Wiki).
- **Traducción**: Carlos Hugo Hidalgo (la mayoría), Janet León, Luis
  Leonardo Suárez (del 131 en adelante), Circe Luna, David Bueno (ep. 279).
  Grabación: Antonio Hernández ✅ (Doblaje Wiki).

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
| **Dulce Princesa** | **Karla Falcón** (temp. 1-2 y **vuelve en la 4.ª, ep. 96, «Rey Gusano»**, hasta el final) | ✅ | [Doblaje Wiki: Dulce Princesa](https://doblaje.fandom.com/es/wiki/Dulce_Princesa), [TikTok, entrevista en Festigame 2024](https://www.tiktok.com/@eldiariodelalquimista/video/7440244073505623352) |
| Dulce Princesa (suplente, eps. 58-94, temp. 3-4) | **Claudia Urbán**, que se retiró del doblaje en noviembre de 2012 | ✅ | Doblaje Wiki, tabla de la serie y su ficha |
| **Rey Helado** | **Óscar Flores** (toda la serie y «Misiones Secundarias») | ✅ | [Doblaje Wiki: Rey Helado](https://doblaje.fandom.com/es/wiki/Rey_Helado), noticias de «Misiones Secundarias» |
| **BMO** | **Gustavo Melgarejo** (1.ª-5.ª) → **Héctor Emmanuel Gómez** (5.2-9.ª, desde «El traje de Jake») | ✅ | Doblaje Wiki (API), [Hora de Aventura Wiki: Héctor Emmanuel Gómez](https://horadeaventura.fandom.com/es/wiki/H%C3%A9ctor_Emmanuel_G%C3%B3mez) |
| Jake (dos loops sueltos) | Víctor Ugarte (ep. 202), Tommy Rojas (ep. 279) | ⚠️ | sólo Doblaje Wiki |
| Rey Helado (eps. 59-60) | Rafael Pacheco | ⚠️ | sólo Doblaje Wiki |
| **Princesa Grumosa** | **Alfonso Obregón**, casi toda la serie | ✅ | Doblaje Wiki, [Hora-de Wiki](https://hora-de.fandom.com/es/wiki/Princesa_Grumosa) |
| Hunson Abadeer | José Luis Orozco (2.ª) → Rafael Pacheco (3.ª) → Julián Lavat (4.ª) → Enrique Cervantes (9.ª) | ⚠️ | sólo Doblaje Wiki |
| Marceline del universo alterno («Fionna y Cake») | Ángela Villanueva (5.ª) → Isabel Martiñón (7.ª) | ⚠️ | sólo Doblaje Wiki |

Voz original de Marceline: **Olivia Olson**, que **canta ella misma** sus
canciones ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Olivia_Olson),
[SciFiNow](https://www.scifinow.co.uk/interviews/adventure-times-olivia-olson-on-marceline-stakes-and-songs/)).

Curiosidades de Doblaje Wiki ✅: **Finn y Marceline no cambiaron de voz en
toda la serie**, algo raro (casi todos los demás sí). El final se llama en
latino **«Ven Conmigo»**. **Canal 2** (El Salvador) y **Canal 5** (México)
la emiten **sin las censuras** de Cartoon Network y Netflix Latinoamérica.

**Por qué volvió Karla Falcón** ✅: la wiki enlaza **peticiones firmadas**
(peticionpublica.es), un **grupo de Facebook** («Evitemos que cambien las
voces…»), un hilo de McAnime y quejas en la wiki de la serie contra el
cambio. **El público latino peleó por su actriz y ganó**: dato de oro para
un servidor de doblaje (punto 22).

### 10.2.b Frases reales del doblaje, oídas en audios oficiales ✅

Seis muestras `.ogg` que Doblaje Wiki sube como prueba de cada actor,
pasadas por `voz.py` (Whisper). **Son diálogo real doblado**; la wiki no
dice de qué episodio sale cada una ⚠️, y Whisper puede fallar en una
palabra suelta (marcada ⚠️).

| Personaje | Frase | Cómo suena (medido) | Audio |
|---|---|---|---|
| **Marceline** (Isabel Martiñón) | «¿Vía⚠️? ¿Qué estás haciendo? No puedes estar aquí. **Ash no quiere que salga con mortales**» | aguda (295 Hz), **muy expresiva** (17,3 semitonos), ritmo normal | [ogg](https://static.wikia.nocookie.net/doblaje/images/a/a6/Isabel_Marti%C3%B1on_como_Marceline.ogg) |
| **Finn** (José Antonio Toledano) | «Tienes razón, sólo hay una forma de salir. Uno de nosotros será sacrificado para que los otros vivan… No traten de convencerme» | media (164 Hz), muy expresiva, **rápida** (3,5 palabras/s) | [ogg](https://static.wikia.nocookie.net/doblaje/images/5/57/Jose_Toledano_-_Finn_5ta_Temporada.ogg) |
| **Jake** (José Arenas, «tono nuevo») | «Estoy para ti, hermano. Pero, Finn, te diré algo gentilmente. Necesitas otra espada… Todo estará bien. **Vayamos de compras**» | media (214 Hz), expresiva, tranquila | [ogg](https://static.wikia.nocookie.net/doblaje/images/5/51/Jose_Arenas_-_Jake_Nuevo_Tono.ogg) |
| **Dulce Princesa** (Karla Falcón) | «**¡Los veo en el dulce reino! ¡Esta noche!**» | **muy aguda** (397 Hz), rápida | [ogg](https://static.wikia.nocookie.net/doblaje/images/4/40/Karla_Falcon_como_la_Dulce_Princesa.ogg) |
| **Rey Helado** (Óscar Flores) | «**¡La hora es suya, pero el día será mío!** ¡Como tú, princesa mía!» | aguda (266 Hz), muy expresiva | [ogg](https://static.wikia.nocookie.net/doblaje/images/7/7a/Oscar_Flores_como_el_Rey_Helado.ogg) |
| **BMO** | «¡Jajajajajaja! ¡Juguemos⚠️ a policías y⚠️ ladrones!» | **muy aguda** (465 Hz), **lenta** | [ogg](https://static.wikia.nocookie.net/doblaje/images/7/70/BMO.ogg) |

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
| «**¡Oh, por Glob!**» | en inglés «Oh my Glob». Es la muletilla latina de la **Princesa Grumosa** y **sí lleva «Glob»** en latino | ✅ (Doblaje Wiki + [Hora-de Wiki](https://hora-de.fandom.com/es/wiki/Princesa_Grumosa), segunda pasada) |
| «**Ash no quiere que salga con mortales**» | Marceline, audio oficial de Doblaje Wiki | ✅ (audio) |
| «**¡Los veo en el dulce reino! ¡Esta noche!**» | Dulce Princesa, audio oficial | ✅ (audio) |
| «**¡La hora es suya, pero el día será mío!**» | Rey Helado, audio oficial | ✅ (audio) |
| «**Eso... es estúpido**» | Rey Helado, piloto subtitulado en español, [4:05](https://www.dailymotion.com/video/x84oaz2?t=245) | ⚠️ (subtítulo, no doblaje) |
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
> record», «I'm Marceline the Vampire Queen» ni la frase del Hoyo Musical
> (YouTube pide sesión y Dailymotion no tiene clips doblados de esas
> escenas). Las frases que propongo para la lámina son **traducción mía**,
> salvo las de 10.2.b.

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

### 11.3 Lo nuevo de la segunda pasada ✅

- **«Everything Stays» habla de la mamá de Marceline.** Lo dice la propia
  **Rebecca Sugar** en su TikTok: «I wrote this song for Adventure Time
  after I'd left to create Steven Universe… I was so touched to be asked
  to write a song for **Marcy's mom**». Grabada con Jeff (@Jeffthatnoise)
  en cuerdas ([TikTok, verificado por oEmbed](https://www.tiktok.com/@rebeccasugar/video/7380076323168996650)).
  Fuente primaria: la compositora.
- **Amy Lee (Evanescence)** subió su versión: «One of my favorite
  #adventuretime songs» ([TikTok](https://www.tiktok.com/@evanescence/video/7008939931548568837)).
  Buen ejemplo de un **cover de estreno** para el canal.
- **La intro cambia en cada miniserie**: hay versiones propias para
  «Islands», «Stakes», «Food Chain» y «Fionna & Cake», de 24-26 s cada una
  ([Islands](https://www.dailymotion.com/video/x5whnwn),
  [Stakes](https://www.dailymotion.com/video/x5whnw2),
  [Food Chain](https://www.dailymotion.com/video/x5whp1h)) ⚠️ (existencia y
  duración por la API de Dailymotion; no se miraron fotograma a fotograma).
- **El disco en español** tiene 10 títulos reales, con «Acompáñame» como
  título latino de «Come Along With Me» (§3.4).
- **Qué suena en las escenas que hacen llorar**: «Remember You» con
  omnichord y batería en «I Remember You» (4×25); «Everything Stays» en
  «Estacas»; «Time Adventure» de BMO y la «Island Song» en el final
  (10×13) ✅ (transcripciones y clips).
- **Sonidos que todos reconocen** (de las transcripciones): el **siseo** de
  Marceline («[Hisses]», casi en cada episodio), el **beatbox** de Finn, el
  «**Boompa-boompa-boom**» de Jake en el final y el **grito «¡Hora de
  aventura!»** de la intro ✅. **No hay onomatopeyas dibujadas** en
  pantalla: es animación americana, el sonido va sólo en el audio.

---

## 12 · Vídeos

> **Segunda pasada**: YouTube sigue pidiendo sesión, así que **los vídeos
> se vieron en Dailymotion** con `fotogramas.py` (12.0). Los enlaces de
> YouTube de abajo son de la primera pasada: existen, pero no se miraron.
> Los TikTok se comprobaron con su API pública (oEmbed).

### 12.0 Vistos de verdad, con minuto (segunda pasada) ✅

| Clip | Duración | Canal | Qué sirve, y en qué minuto |
|---|---|---|---|
| [Opening doblado al latino](https://www.dailymotion.com/video/x8p2dsj) | 0:29 | Espinof | la intro entera en latino, 1080p (§2.9) |
| [«I'm Just Your Problem»](https://www.dailymotion.com/video/x537pqr) | 2:07 | **Cartoon Network** | vuelo con el bajo [0:16](https://www.dailymotion.com/video/x537pqr?t=16); cantando con rabia [0:52](https://www.dailymotion.com/video/x537pqr?t=52); tocando apoyada [1:32](https://www.dailymotion.com/video/x537pqr?t=92) |
| [«Fry Song» Sing-a-Long](https://www.dailymotion.com/video/x51arca) | 0:52 | Toon Tunes de CN | flota bocabajo tocando 0:00; grabadora amarilla [0:12](https://www.dailymotion.com/video/x51arca?t=12); Finn con audífonos [0:40](https://www.dailymotion.com/video/x51arca?t=40) |
| [Créditos finales](https://www.dailymotion.com/video/x4fakxm) | 0:33 | reload con logos reales | staff real sobre verde lima |
| [Tráiler «Obsidian»](https://www.dailymotion.com/video/x7xejon) | 1:30 | reload, logo HBO Max | tazas en la cocina [0:16](https://www.dailymotion.com/video/x7xejon?t=16); flota tocando hacia el Reino de Cristal [0:36](https://www.dailymotion.com/video/x7xejon?t=36); bajo al hombro [1:08](https://www.dailymotion.com/video/x7xejon?t=68) |
| [Tráiler «BMO» doblado](https://www.dailymotion.com/video/x7vjn4d) | 1:54 | HobbyConsolas | tráiler oficial en español de «Tierras lejanas: BMO» |
| [«I Remember You»](https://www.dailymotion.com/video/xzt1l7) | 1:58 | emisión CN HD, audio francés | batería del Rey Helado [0:42](https://www.dailymotion.com/video/xzt1l7?t=42); la lágrima [1:18](https://www.dailymotion.com/video/xzt1l7?t=78); la Polaroid [1:36](https://www.dailymotion.com/video/xzt1l7?t=96) |
| [Tráiler «Fionna & Cake»](https://www.dailymotion.com/video/x8nce5e) | 2:05 | HobbyConsolas | 720p; no sale la Marceline clásica |
| [Episodio piloto subtitulado](https://www.dailymotion.com/video/x84oaz2) | 7:30 | Capra TV | Rey Helado [4:05](https://www.dailymotion.com/video/x84oaz2?t=245); Finn avergonzado [6:00](https://www.dailymotion.com/video/x84oaz2?t=360) |
| [«Slumber Party Panic»](https://www.dailymotion.com/video/x8ghhnc) | — | clip con logo CN | Dulce Princesa preocupada [2:12](https://www.dailymotion.com/video/x8ghhnc?t=132) |
| [«Jake the Starchild»](https://www.dailymotion.com/video/x6gkz32) | — | clip oficial CN | Jake orgulloso [1:39](https://www.dailymotion.com/video/x6gkz32?t=99) |
| [«The More You Moe…»](https://www.dailymotion.com/video/x3q931u) | — | clip con logo CN | BMO en calma [2:36](https://www.dailymotion.com/video/x3q931u?t=156) |

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
- Segunda pasada: los cuatro vídeos de abajo (Sugar, Evanescence, acubick
  y la entrevista a Karla Falcón) se comprobaron con la **API oEmbed de
  TikTok**: existen, con ese autor y ese título ✅. La de acubick dice:
  «Por qué Jake el perro cambió de voz en las últimas temporadas de
  #horadeaventura? doblaje: José Arenas».
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

## 13 · Videojuegos de la franquicia

Ver §7.3 (sus interfaces) y el punto 23 (Fortnite, MultiVersus, LEGO
Dimensions, Minecraft, Brawlhalla). Segunda pasada, la lista ampliada:

| Juego | Estudio y año | Cómo es | Estado |
|---|---|---|---|
| **Hey Ice King! Why'd You Steal Our Garbage?!!** | WayForward, DS/3DS, 20-nov-2012 | historia escrita con **Pendleton Ward**; mapa desde arriba y mazmorras de lado, tipo *Zelda II*; Jake va en la mochila y saca objetos; 4 zonas (Grass Lands, Candy Kingdom, Red Rock Pass, Ice Kingdom); **retratos «Mugshots»** junto al texto | ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time:_Hey_Ice_King!_Why%27d_You_Steal_Our_Garbage%3F!!), [Giant Bomb](https://giantbomb.com/wiki/Games/Adventure_Time_Hey_Ice_King_Whyd_you_steal_our_garbage), [Nintendo Life](https://www.nintendolife.com/reviews/ds/adventure_time_hey_ice_king_whyd_you_steal_our_garbage)) |
| **Explore the Dungeon Because I DON'T KNOW!** | WayForward, 2013, PS3/360/Wii U/3DS | mazmorras en cooperativo hasta 4 | ⚠️ ([Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time:_Explore_the_Dungeon_Because_I_Don%27t_Know!)) |
| **The Secret of the Nameless Kingdom** | WayForward, 2014 | tipo Zelda | ✅ |
| **Pirates of the Enchiridion** | Climax Studios, 2018 | mundo abierto inundado | ✅ |
| **Card Wars** | Kung Fu Factory / CN, 2014-2019 (retirada) | cartas; menú metálico azul grisáceo, botón rojo «BATTLE!» (§7.3) | ✅ ([wiki](https://adventuretime.fandom.com/wiki/Card_Wars_(application))) |
| **Card Wars Kingdom** | móvil | secuela | ⚠️ (sólo tiendas de APK) |

Lo de la primera pasada: el de 2012 tiene **más de 50 personajes** de las temporadas 1-3
y lugares como el Dulce Reino, el Reino Helado, el Espacio Grumoso y la
casa del árbol ✅ ([Gaming Nexus](https://www.gamingnexus.com/Article/Adventure-Time-Hey-Ice-King!--Whyd-you-steal-our-garbage!!/Item3804.aspx),
[Mash Those Buttons](https://mashthosebuttons.com/review/adventure-time-hey-ice-king-whyd-you-steal-our-garbage-review/)).
Sus cajas de texto en sí siguen sin captura ⚠️; sí se vieron los
retratos del de DS y el menú de Card Wars (§7.3). No los propongo como
cuadro principal de la lámina.
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
- **«¡Oh por Glob!»** (Princesa Grumosa) ✅ en latino (segunda pasada, §10.4).
- **La lucha para que volviera Karla Falcón** como Dulce Princesa
  (firmas, grupo de Facebook, foros) ✅: el fandom latino **defiende sus
  voces** (§10.2).
- **«Bubbline» reconocida**: «Obsidian» fue **nominado a un GLAAD Media
  Award** ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Marceline_the_Vampire_Queen)).
- **BMO, el favorito de Pendleton Ward** ✅ (§9).
- En **Reddit** (r/adventuretime, que sí existe) la gente cuenta que lloró
  con el final (punto 21) ✅.

### 14.2 Qué NO hacer (lo que un fan notaría)

- **El bajo sin forma de hacha**, con seis cuerdas o de guitarra normal:
  es un **hacha de doble filo con cuatro cuerdas y dos clavijas a cada
  lado** ✅.
- **Filos plateados** fuera de la temporada 1: desde la 2 son **rojos** ✅.
- Marceline **chupando sangre** o con colmillos de película: chupa **el
  color rojo** ✅, y sus colmillos son pequeños ⚠️. **Dos puntitos de
  mordida en el cuello** ⚠️: la wiki tiene una captura llamada «S2e26
  Missing bite mark» (hoja `escenas_09`, n.º 387), que señala un fallo de
  animación **porque la marca falta**; así que la marca va.
- Marceline **caminando con los pies en el suelo** todo el rato: **flota** ✅.
- **Ojos grandes de anime**, sombras suaves, pelo con mechones
  realistas: la serie usa **ojos de punto**, línea fina y colores planos
  ✅ (§18).
- **Codos y rodillas marcados**: son **brazos de fideo** ✅.
- **Finn sin su gorro** (sólo se lo quita en momentos muy especiales) ⚠️.
- Nombres de España: «Princesa Chicle», «Rey Hielo» ⚠️ (de memoria) y
  «Hora de Aventuras» ✅ (§7.4); el latino es **Dulce Princesa**, **Rey
  Helado**, **Hora de aventura** ✅.
- **Poner la censura de Cartoon Network** como si fuera «la versión»: en
  Canal 2 (El Salvador) y Canal 5 (México) se vio **sin cortes**, y los
  fans comparan ✅ (Doblaje Wiki).
- **Olvidar el rojo en la ropa de Marceline**: como come el color rojo,
  **siempre lleva algo rojo** «por si acaso» (salvo en «Red Starved») ✅
  (wiki, punto 20).
- Poner a Marceline **alegre de colorines** en pleno día sin sombrero:
  **de día lleva sombrero de sol y guantes** ✅ (3×10).
- **Burbuja blanca genérica** (§7).
- Frases del doblaje **inventadas y presentadas como reales**: si la
  frase es mía, no se atribuye al doblaje.

---

## 15 · Poses analizadas por personaje

> **Segunda pasada**: primero van las poses **vistas en vídeo real**, con
> minuto exacto, y las **6 poses oficiales del model sheet** tocando el
> bajo. Las tablas de la primera pasada (de transcripción, minuto
> estimado ⚠️) siguen debajo para las escenas sin clip.

### Marceline, vistas en vídeo (segunda pasada) ✅

| # | Clip | Minuto | Qué hace: postura, manos, mirada | Sirve para |
|---|---|---|---|---|
| V1 | «Fry Song» | [0:00](https://www.dailymotion.com/video/x51arca) | **flota bocabajo tocando el bajo**, de espaldas | presentar el «estreno casero» |
| V2 | «Fry Song» | [0:32](https://www.dailymotion.com/video/x51arca?t=32) | primer plano, **ojos entornados, boca abierta**, canta triste | emocionar |
| V3 | «I'm Just Your Problem» | [0:16](https://www.dailymotion.com/video/x537pqr?t=16) | **vuela hacia la puerta con el bajo por delante**, sombrero de sol | **anunciar**, entrar en escena |
| V4 | «I'm Just Your Problem» | [0:52](https://www.dailymotion.com/video/x537pqr?t=52) | primer plano, **ceño fruncido, colmillos**, canta con fuerza | **regañar** |
| V5 | «I'm Just Your Problem» | [1:32](https://www.dailymotion.com/video/x537pqr?t=92) | **apoyada en la puerta, toca relajada** con el sombrero | pensar, tocar con calma |
| V6 | «I Remember You» | [0:24](https://www.dailymotion.com/video/xzt1l7?t=24) | de pie, **una mano en la cabeza**, angustia | **pensar**, dolor |
| V7 | «I Remember You» | [1:00](https://www.dailymotion.com/video/xzt1l7?t=60) | **sentada, toca con cara seria** junto al Rey Helado a la batería | tocar a dúo |
| V8 | tráiler «Obsidian» | [0:16](https://www.dailymotion.com/video/x7xejon?t=16) | sentada en la cocina con **una taza humeante** | conversar, momento tranquilo |
| V9 | tráiler «Obsidian» | [0:20](https://www.dailymotion.com/video/x7xejon?t=20) | sentada, **toca el bajo** con la Princesa cocinando detrás | **explicar** en casa |
| V10 | tráiler «Obsidian» | [0:36](https://www.dailymotion.com/video/x7xejon?t=36) | **flota tocando** sobre un camino de piedra hacia el Reino de Cristal | **animar**, avanzar tocando |
| V11 | tráiler «Obsidian» | [1:08](https://www.dailymotion.com/video/x7xejon?t=68) | de pie, **bajo al hombro**, con la Princesa y dos figuras de cristal | **presentar en grupo**, celebrar |
| V12 | tráiler «Obsidian» | [1:24](https://www.dailymotion.com/video/x7xejon?t=84) | primer plano, **cara de susto** | sorpresa |

**Las 6 poses oficiales tocando el bajo** (model sheet, ep. 062 = 3×10,
§3.7): **A** de pie en cuesta (**presentar**), **B** echada atrás cantando
con los ojos cerrados (**celebrar**), **C** doblada casi bocabajo con el
bajo en alto (solo exagerado, **celebrar**), **D-E** sentada en el aire
(**explicar** con calma), **F** primer plano cantando fuerte (**animar**).

**La mejor para presentar #musica-nueva, con imagen real**: la **B** del
model sheet o la **V10** del tráiler (flotando y tocando). Para
**«nada de vida personal»**: la **V4** (ceño y colmillos) o la 4 de
abajo (guiño). Para **pensar**: la **V6**.

### Otros personajes, vistos en vídeo (segunda pasada) ✅

| Personaje | Clip y minuto | Qué hace |
|---|---|---|
| Rey Helado | «I Remember You», [0:42](https://www.dailymotion.com/video/xzt1l7?t=42) | toca **una batería verde con «#1»** en el bombo |
| Dulce Princesa | tráiler «Obsidian», [0:16](https://www.dailymotion.com/video/x7xejon?t=16) | sentada, **taza humeante** en las manos |
| Dulce Princesa | tráiler «Obsidian», [1:12](https://www.dailymotion.com/video/x7xejon?t=72) | **conduce una moto** con Marceline detrás |
| Dulce Princesa | «Slumber Party Panic», [2:12](https://www.dailymotion.com/video/x8ghhnc?t=132) | **manos juntas contra el pecho**, preocupada |
| Finn | «Fry Song», [0:40](https://www.dailymotion.com/video/x51arca?t=40) | de pie, **audífonos puestos**, grabadora en alto |
| Finn | piloto, [4:05](https://www.dailymotion.com/video/x84oaz2?t=245) | **llave de cabeza** al Rey Helado por detrás |
| Jake | «I'm Just Your Problem», [0:04](https://www.dailymotion.com/video/x537pqr?t=4) | **corre tocando la viola** |
| Jake | «Jake the Starchild», [1:39](https://www.dailymotion.com/video/x6gkz32?t=99) | sonrisa enorme de orgullo |
| BMO | «The More You Moe…», [2:36](https://www.dailymotion.com/video/x3q931u?t=156) | en brazos, ojos cerrados, contento |

### Marceline, de la primera pasada (transcripción, minuto estimado ⚠️)

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

Primera pasada: **la mejor para presentar el canal**, la 10 (escenario,
⚠️ sin clip) o la 6 (grabando, ya vista: V1). **Para «nada de vida
personal»**: la 4 (guiño burlón) o la 11 (desgana).

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
- **Pelo**: **negro, lisísimo y larguísimo**, hasta las rodillas o más
  ✅ (se ve así en todos los model sheets de la hoja `personajes_01`).
- **Fijo**: **piel casi blanca con un toque menta** (medida, abajo),
  **orejas puntiagudas**, **dos marcas de mordida en el cuello** ⚠️ (ver
  §14.2).
- **Siempre algo rojo** en la ropa, porque come el color rojo ✅ (punto 20).

### Marceline, hex MEDIDOS (segunda pasada) ✅

Medidos con `estilo.py` y Pillow sobre imágenes oficiales. **El model sheet
manda** (no tiene luz de escena); las capturas salen más oscuras.

| Traje o parte | Hex medido | De dónde |
|---|---|---|
| **Piel** (color base) | **`#D8E7E7`** (y `#D9E7E7`) | model sheet «New Costume #1» (ep. 057) y recorte de «Drama Bomb», dos medidas |
| Piel con luz de escena | `#657471` | «I'm Just Your Problem», fotograma 0:52, 12 puntos |
| **Pelo** | **`#000000`** en model sheet; `#150209` y `#24080E` en escena | tira a **rojo muy oscuro**, nunca a azul |
| «New Costume #1»: vestido camisero azul grisáceo | **`#83A5BC`** | model sheet ep. 057 |
| «New Costume #1»: zapatos granate | **`#8C284F`** | model sheet ep. 057 |
| **Traje de 3×10**: sombrero de sol mostaza | **`#BBAB4C`** luz / `#75691D` sombra | «I'm Just Your Problem», 0:52 |
| Traje de 3×10: cinta del sombrero | `#4A7AA2` | mismo fotograma |
| Traje de 3×10: top rojo oscuro | `#8C000C` a `#90000A` | mismo fotograma |
| **Suéter a rayas** (nocturno) | rojo `#5F120D` / azul negro `#090B25` | captura «S2e1 Drama bomb», de noche |
| Suéter a rayas en «Fry Song» | rojo `#630515` / gris oscuro `#2C080C` | «Fry Song», 0:16 |
| Bajo-hacha: filos | rojo `#9E1B1E` a `#C22B2F` ⚠️ | escenas; no salió un píxel limpio por el brillo |

**Corrige a la primera pasada**: además de la camiseta gris, son muy
repetidos el **suéter a rayas rojo con cuello alto** y el **traje de 3×10
con sombrero de sol**, que tiene **6 poses oficiales tocando** (§3.7). La
hoja `personajes_01` enseña varios trajes de día (n.º 9-14, 19-23) y el
murciélago (2-4).

### Finn ✅ (segunda pasada, medido)
Gorro blanco con **orejas de oso**, camiseta **azul `#018BCB`**, pantalón
corto azul oscuro, calcetines blancos altos, zapatos negros, **mochila
verde `#7BBB59`**, piel **durazno pálido `#FDE5DA`** (model sheet
[«Original Finn»](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/f/f3/Original_Finn.png),
1467×2385). La primera pasada decía piel «celeste»: era la camiseta.

### Jake ✅ (medido)
Sin ropa; amarillo anaranjado **`#FEB925`** (40 % del model sheet
[«Jakesalad»](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/3/3b/Jakesalad.png)),
**orejas caídas**, hocico claro.

### Dulce Princesa ✅ (medido; corona ⚠️)
Piel y pelo rosa chicle en dos tonos, **`#ED8ACE`** y **`#F3BBFB`** en la
luz (captura [«Princess Bubblegum Duct Tape»](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/f/f5/Princess_Bubblegum_Duct_Tape.png),
2880×1618). **Corona dorada** con gema azul ⚠️ (sin medir), vestido rosa;
bata de laboratorio cuando hace ciencia; capa roja en «Stakes» (hoja
`personajes_02`, n.º 67-79). Es el personaje con **más vestuarios** ✅.

### BMO ⚠️ (sin medir)
Consola turquesa (`#6CC3B3`, de memoria: el fondo rosa tapaba la muestra),
**pantalla con cara**, cruceta amarilla, botones de colores, piernas y
brazos finitos.

---

## 17 · Paisajes y fondos de pantalla

- **Segunda pasada: fondos de pantalla con tamaño y autor** (API de
  Wallhaven, filtro «sfw»). **Son fan art**, no oficiales ✅:

  | Id | Tamaño | Autor | Favoritos | Qué es |
  |---|---|---|---|---|
  | [zxo8vg](https://wallhaven.cc/w/zxo8vg) | **3600×2400** | RaidMath | 40 | todo el elenco (Marceline, Dulce Princesa, Jake, Rey Helado, BMO, Lady Arcoíris) sobre fondo de Cartoon Network |
  | [0wy167](https://wallhaven.cc/w/0wy167) | 1800×1000 | Oniofash | 52 | collage de Marceline, Simon y Dulce Princesa |
  | [45zpo5](https://wallhaven.cc/w/45zpo5) | 1639×1165 | Linez | 34 | Jake, Finn, Dulce Princesa y Marceline |
  | [0wxpgp](https://wallhaven.cc/w/0wxpgp) | 1920×1036 | 8bitcartoon | 57 | Finn y Jake en **pixel art** (paleta reducida) |

- **Fondos oficiales en alta**: Cartoon Network no tiene página de
  descargas ⚠️ (no encontré). Lo más cercano son las portadas de disco y
  el key art de «Obsidian» (oficiales, pero no 16:9).
- **Sitios vistos en capturas oficiales** (hojas): casa de Marceline por
  dentro, rosa con piso azul verdoso (`escenas_09` n.º 385, 403); la puerta
  dorada de 3×10 de día (393); el Dulce Reino rosa (`personajes_02`,
  52-61); la playa al atardecer (94-95).
- **La casa del árbol en 3D**, CC BY, de gleksono ([Sketchfab](https://sketchfab.com/3d-models/none-0131dc63d8894892b0c87dc852f23984)):
  para darle luz real en Blender (§4.1.b).
- Lo de la primera pasada, que sigue valiendo:
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
- La hora del día: **noche o cueva** para Marceline ⚠️; **de día con
  sombrero** en 3×10 ✅; **violeta de noche mágica** en el Reino de Cristal
  ✅; **tarde dorada** para la casa del árbol ⚠️ (§5.2).

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
  personajes, y colores más suaves ⚠️. En «Tierras lejanas» (Obsidian)
  el sombreado es **más pintado, con degradado** ✅ (§5.2).
- Producción real: **dibujo a mano en papel**, compuesto y pintado en
  digital; preproducción en Photoshop (punto 18) ✅/⚠️.

### 18.2 Marceline, rasgos fijos

- Piel **casi blanca con un toque menta** (`#D8E7E7`, medida; la primera
  pasada decía gris azulada), **pelo negro puro** (`#000000`) lisísimo
  hasta más abajo de la cintura, flequillo partido ⚠️, **orejas
  puntiagudas**, colmillos pequeños, **dos puntos de mordida en el
  cuello** ⚠️. **Siempre algo rojo** en la ropa.
- **Flota**. Cuerpo largo y delgado.
- Ropa por defecto: **camiseta gris de tirantes, vaqueros, botas rojas**
  ✅. De día: **sombrero de sol mostaza `#BBAB4C`** con cinta azul
  `#4A7AA2`, top rojo oscuro `#8C000C` y botas marrones (3×10) ✅.
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

- **De estilo**: el arte de los discos oficiales (§3.4), las cartelas
  (§3.2) y **los model sheets** de §3.7 (línea y color limpios, sin luz de
  escena).
- **De pose**: las **6 poses oficiales tocando el bajo** (Special Pose
  A-F, §3.7), las V1-V12 de §15 vistas en vídeo y, en las hojas,
  `personajes_01` n.º 36 (tocando en el huerto) y `escenas_09` n.º 393
  (cantando en la puerta).
- **Del objeto**: el modelo 3D de Yogensia (§4.1) y las fotos de
  réplicas reales (§3.5).
- **De luz para Blender**: el [HDRI Cave Wall](https://polyhaven.com/a/cave_wall) (§5.4).
- **Frase de prompt para Marceline** (IA de imagen): `Marceline, pale
  mint-white skin, very long straight pure black hair to the knees,
  pointed ears, floating in the air, wide mustard sun hat with blue band,
  dark red top, brown boots, playing a red double-bladed battle axe bass
  guitar with 4 strings, flat 2D cartoon, thin uniform outline, dot eyes,
  noodle arms, pink room background`.

### 18.6 Para una IA de texto: cómo escribir en su voz

**Reglas de voz** ✅ (transcripciones, audios de Doblaje Wiki y wiki):
- **Marceline**: frases cortas y relajadas, burla suave, **cero
  signos de exclamación salvo cuando se enfada**. Presume sin esfuerzo y
  cambia a hablar bajito cuando algo le importa. Guiña después de asustar.
  Su voz latina es **aguda y muy expresiva** (295 Hz, 17 semitonos).
- **Finn**: todo con **exclamaciones**, rápido (3,5 palabras por segundo
  en el audio), heroico, caballeroso; **«¡Matemático!»** y
  **«¡Algebraico!»** en vez de palabrotas.
- **Jake**: tranquilo, de hermano mayor; en latino, **modismos
  mexicanos** («compadre», «¡Ay, mamachita!», «Nunca me hagan eso»).
- **Dulce Princesa**: correcta, algo mandona, **palabras técnicas**;
  muy aguda y rápida.
- **BMO**: niño seguro de sí mismo, **a veces en tercera persona**, risas
  largas («¡Jajajajaja!»).
- **Princesa Grumosa**: **«¡Oh por Glob!»**. En Ooo, **«Glob»** es «Dios».

**Frases reales, por emoción** (en inglés lo que es de transcripción; en
español, lo que es del doblaje oído):

| Emoción | Frase real | Quién, dónde |
|---|---|---|
| Alegre | «Hey, guys. What's up? I'm Marceline the Vampire Queen» | Marceline, 1×12 |
| Alegre | «¡Jajajajajaja! ¡Juguemos a policías y ladrones!» | BMO, audio del doblaje |
| Alegre | «I am proud of my punk daughter!» | Hunson, 10×07 |
| Burlona | «Calm down, weenies» · «You know I eat the color red sometimes» [guiña] | Marceline, 1×12 y 1×22 |
| Enfadada | «My bass. MY BASS!» [ojos rojos] | Marceline, «Obsidian» |
| Enfadado | «¡La hora es suya, pero el día será mío!» | Rey Helado, audio del doblaje |
| Explicando | «Music is powerful, man. It speaks to a primal pit in our brains» | Jake, 10×13 |
| Explicando | «A good song can really wrap people up in a mood, better than any words alone could» | Hoyo Musical, 10×13 |
| Explicando (mandona) | «Marceline, begin playing triplet quavers in mixolydian mode» | Dulce Princesa, 3×10 |
| Animando | «Estoy para ti, hermano… Todo estará bien. Vayamos de compras» | Jake, audio del doblaje |
| Animando | «¡Los veo en el dulce reino! ¡Esta noche!» | Dulce Princesa, audio del doblaje |
| Animando | «Sing out, sister!» · «Everyone! I need you all to harmonize» | Rey Helado 4×25 · Dulce Princesa 10×13 |
| Triste | «Daddy, there were tears there» | Marceline, «Fry Song», 0:48 |
| Triste | «I was so afraid something bad would happen to you, and I wouldn't be there» | Marceline, 10×13 |
| Triste (heroico) | «Uno de nosotros será sacrificado para que los otros vivan… No traten de convencerme» | Finn, audio del doblaje |

**Vocabulario de expresiones para la IA de imagen** ✅ (visto en
fotogramas y model sheets): **ojos de punto negro**; **boca en rayita**
(vergüenza) con **óvalo rosa** en las mejillas; **boca en zigzag** y cejas
caídas (molestia); **dientes apretados en triángulo** y **una sola
lágrima** (tristeza de Marceline); **ceño fruncido y colmillos**
(rabia); **ojos rojos** y **transformación en murciélago o monstruo**
(rabia extrema); **ojos enormes blancos con franja negra** (Jake
emocionado); **ojos en dos curvas** (BMO feliz); **manos juntas contra el
pecho** (Dulce Princesa nerviosa). La serie **no usa gotas de sudor de
anime, fondos de emoción ni chibi**: su versión «simplificada» son los
retratos del juego de DS (§7.3).

---

## Punto 18 del encargo · Estilo de dibujo y técnica, y cómo replicarlo

Sección nueva de la segunda pasada.

### Cómo se hizo de verdad

- **Dibujo a mano en papel**, luego compuesto y pintado en digital
  («hand-drawn on paper, which was then digitally composited and painted
  with digital ink and paint») ✅
  ([Wikipedia, «Animation»](https://en.wikipedia.org/wiki/Adventure_Time)).
- La preproducción (personajes, objetos, fondos) se hizo **sobre todo en
  Photoshop**, según **Phil Rynda**, diseñador líder ⚠️ (el dato del
  Photoshop sólo lo da Wikipedia citando una entrevista que no encontré;
  Rynda como diseñador líder sí está en dos fuentes:
  [su ficha](https://adventuretime.fandom.com/wiki/Phil_Rynda) y los
  créditos vistos en §2.9).
- La animación se hacía en **Corea del Sur** (**Rough Draft Korea** o
  **Saerom Animation**); diseño y color final en **Cartoon Network Studios**
  (Burbank) ⚠️ (una fuente).
- **Fred Seibert** comparó el estilo con **Felix the Cat** y los dibujos de
  **Max Fleischer**, y dijo que el mundo bebe de los videojuegos ⚠️ (una
  fuente).
- Dirección de arte: **Nick Jennings** (pintó muchas cartelas, §3.2) ✅.
  Fondos de la temporada 1: **Ghostshrimp** y **Santino Lascano**; pintura:
  **Sue Mondt** y **Martin Ansolabehere** ⚠️.
- **Línea y color** ⚠️ (análisis de fans y blogs que coinciden, no un
  *making of*): contorno oscuro limpio con un **temblor leve «a mano»**, más
  grueso en las primeras temporadas; **colores planos y saturados**, 1 o 2
  tonos de sombra como mucho; formas simples. Los model sheets vistos
  (§3.7) lo confirman: **línea fina uniforme, color plano, sin sombra**.
- **Filtros**: no hay grano, brillo ni aberración en la serie normal ✅
  (visto en los clips). En «Tierras lejanas» los fondos son **más
  pintados, con degradado** (§5.2).
- Reglas de dibujo de Ward: **brazos de fideo «al dente»** y ojos de punto
  ✅ ([Acclaim](https://acclaimmag.com/culture/learn-draw-adventure-time-creator-pendleton-wards-detailed-occasionally-bizarre-notes/)).

### Cómo reproducirlo en Photoshop

(Propuesta práctica, coherente con el flujo real: papel → tinta digital →
color plano.)

- **Capa de línea** aparte: pincel de tinta duro, opacidad 100 %, sin
  textura, unos **3-4 px sobre un lienzo de 1500 px** de ancho.
- **Color base debajo** de la línea, con el bote de pintura (bordes duros,
  sin degradado).
- **Sombra en una sola capa «Multiplicar»**, un solo tono, sin aerógrafo.
- Para una **cartela o un título**: textura de **papel viejo** en
  «Multiplicar» o «Superponer» a baja opacidad, y una trama de **tramado
  (dithering)** encima (punto 19).
- Recortes de fotogramas: siempre por `v3/integrar.py`.

### Cómo reproducirlo en Blender

- **Contorno**: modificador **Solidify** con normales invertidas, grosor
  ~0,01-0,02 (el «casco invertido», funciona en Eevee), o **Freestyle** en
  la pestaña Render ✅
  ([Blender Studio, Toon Character Workflow](https://studio.blender.org/training/toon-character-workflow/5859a5da1f47427e3fe82330/),
  [BlenderNation](https://www.blendernation.com/2020/02/06/how-to-make-a-toon-shader-with-dynamic-outlines/)).
- **Sombreado**: un **Toon Shader**, o Diffuse + **ColorRamp** en modo
  Constant, cortando en 1 o 2 tonos duros.
- **Luz**: una luz principal suave y cálida; en la cueva, el HDRI
  [Cave Wall](https://polyhaven.com/a/cave_wall) (§5.4).
- **Modelos y rigs libres** (licencia leída en la API de Sketchfab): bajo
  de Haxis (CC BY), Marceline de coffe0wolf (CC BY), Finn de Agu.3D (CC BY,
  64 992 caras) y de Nico Caraballo (CC BY, 1 548 caras), Jake de Mormont
  (CC BY), BMO y la casa del árbol (CC BY) (§4.1.b).
- **El objeto 3D no debe verse realista** al lado de un personaje plano:
  material plano + contorno (§4.1).

### Encuadres y composición

- ⚠️ **No encontré** una entrevista o *making of* sobre planos y ángulos.
  Lo visto en los clips (§2, §15): **plano general** para entrar en
  escena (Marceline volando hacia la puerta), **primer plano frontal**
  para cantar con rabia o tristeza, **primerísimo primer plano** con la
  cabeza echada atrás para llorar (1:18 de «I Remember You»), **plano
  medio sentado** para escenas de casa (tráiler de «Obsidian», 0:16-0:20).

## Punto 19 del encargo · Texturas 2D

Sección nueva de la segunda pasada. No es manga: **no hay tramas de manga**.

- **Tramado (dithering) de las cartelas**: la textura «oficial» de la
  serie, sobre **papel viejo escaneado** por Nick Jennings ✅ (§3.2).
- **Cómics de BOOM!**: color plano con sombra en trama, típico del cómic
  americano de la época ⚠️ (descripción, sin fuente de técnica).
- **Texturas reales CC0** (nombres sacados de la API de ambientCG):
  **Paper001-006** para cartelas y librillos, **Cardboard001-004** para la
  funda del vinilo, **Fabric081C, Fabric061, Fabric066** para la ropa,
  **Wood092, Wood094, Wood095** para el mástil y los muebles,
  **Leather026, 030, 037, 038** para las botas ✅ (§5.4).
- **Pinceles y patrones de trama libres**:
  [12 texturas de halftone desgastado, Spoon Graphics](https://blog.spoongraphics.co.uk/freebies/free-pack-of-12-distressed-halftone-pattern-textures)
  ✅ (gratis, sin registro);
  [+35 patrones de halftone, PhotoshopSupply](https://www.photoshopsupply.com/patterns-textures/halftone-texture)
  ✅; [Brusheezy](https://www.brusheezy.com/free/halftone-texture) ⚠️ (la
  licencia cambia en cada pincel: míralo antes).
- **Emblemas y logos**: el logo oficial (§3.7), la corona del Rey Helado,
  la Espada de Hierba y el Enchiridion (punto 25).
- Con el punto 3 (3D, §4) y el 4 (texturas reales, §5.4) **no falta
  ninguna capa**: trama, material real y 3D.

## Punto 20 del encargo · Gustos y detalles de cada personaje

Sección nueva de la segunda pasada. Sale de los infobox y de las
curiosidades de la wiki inglesa, leídos por su API, con el episodio que
lo confirma. **Ningún infobox trae la altura**: no la invento.

### Marceline

- **Come el color rojo**, no sangre. Por eso **toda su ropa lleva algo
  rojo** «por si acaso» (salvo en «Red Starved») ✅. **Los tomates le dan
  sueños lúcidos** (nota suya en «Marceline's Closet») ✅.
- **Aficiones**: la música y el **baloncesto** («Simon & Marcy»; la hoja
  `escenas_09` n.º 417-418 la muestra encestando) ✅.
- **Mascota**: un **caniche zombi, Schwabl** ✅.
- **Lo que siempre lleva**: **el bajo-hacha**, hecho del hacha de guerra de
  la familia ✅.
- **Protector solar «FPS 10 000 000»** ✅.
- **Cumpleaños**: **27 de junio** ✅ (infobox, con la «House Hunting Song»
  de 1×12: «I'm a thousand years old»).
- **Cómo se ve a sí misma**: «No soy mala. Tengo mil años y perdí de vista
  mi código moral» ⚠️ (traducción mía; no encontré el doblaje).
- **Altura**: sin número; «alta y delgada», más alta que la Princesa y como
  el Rey Helado ⚠️.

### Finn

- **Color favorito**: **azul bebé** «de niño» («The Silent King») ✅.
- **Comida favorita**: **pastel de carne** (meatloaf), en tres episodios
  («Still», «Jake Suit», «Three Buckets») ✅.
- **Lo que le cuesta**: el romance (vomita en «Go With Me»); es
  **daltónico rojo-verde** («Red Starved») ✅.
- **Lo que siempre lleva**: su espada (varias) y la mochila; en «Jake vs.
  Me-Mow», la **cajita de música de su madre adoptiva**, cuya nana se sabe
  de memoria ✅.
- **Cómo se ve**: quiere ser un gran héroe, el «sheriff moral» de Ooo ✅.

### Jake

- **Comida**: pay, hamburguesas y helado; **el chocolate lo mataría**
  («Slumber Party Panic») ✅.
- **Aficiones**: **cocinar** bien (bacon pancakes, café, «Everything
  Burrito»), **la viola**, el beatbox ✅.
- **Cómo se ve**: el mentor sabio de Finn, aunque sabe que sus consejos
  fallan ✅.

### Dulce Princesa

- **Color favorito**: **rosa** («The Real You») ✅.
- **Comida favorita**: **espagueti** («To Cut a Woman's Hair») ✅.
- **Afición**: toca **la trompeta** («Bad Timing») ✅.
- **Transporte**: **Morrow**, un pájaro muy veloz ✅.
- **Lo inquietante**: en situaciones límite **come gente-caramelo** de su
  reino para «reponer biomasa» (lo confirmó el showrunner **Adam Muto**) ✅.
- **Edad**: 827 años (§8) ✅.

### BMO

- **Lo que más valora**: **su control**, «BMO's prized possession»
  («What Was Missing») ✅.
- **Ficha en broma** de un DVD: edad **«VER. 2600»**, especie **«110
  VOLT-60 HERTZ SYSTEM»**, guiño a la Atari 2600 ✅.
- **Lo que le hace llorar**: que Finn se rape para disfrazarse («Davey»),
  aunque dice no tener emociones ✅.

### Rey Helado / Simon

- **Objetos**: la **corona** (poder y locura) y una **computadora vieja**
  donde juega y dibuja princesas torpes ✅.
- **Detalle**: un tatuaje de pingüino («Prisoners of Love», en un sueño) ⚠️.
- **Cómo se ve**: como Simon, responsable de Marceline; como Rey Helado,
  sólo sabe que «quiere una princesa» (el eco de Betty) ✅.

**Fuente que falta**: la *Adventure Time Encyclopædia* (Martin Olson,
Abrams, 2013) trae fichas de gustos «en la voz» de cada personaje, pero
no se pudo leer (Scribd no cargó) ⚠️.

## Punto 21 del encargo · Por qué la gente la ama

Sección nueva de la segunda pasada.

### Premios y reconocimiento ✅

- **8 Primetime Emmy**, **1 Peabody**, **3 Annie**, **2 BAFTA infantiles**,
  un premio de los editores de sonido y un premio *Kerrang!*
  ([Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time)).
- **«Simon & Marcy»** (4×24), nominado al Emmy en 2013; el final, **«Come
  Along With Me»**, nominado a un Emmy Creative Arts en 2019
  ([Wikipedia: Ice King](https://en.wikipedia.org/wiki/Ice_King),
  [Wikipedia: Come Along with Me](https://en.wikipedia.org/wiki/Come_Along_with_Me_(Adventure_Time))).
- **«Obsidian»**, nominado a un **GLAAD Media Award** (§14).

### Por qué conecta, según la crítica ✅

- **Crecer de verdad**: *Vox* (Emily VanDerWerff) la llamó «la mejor
  historia de crecimiento de esta era»; Finn pasa «de niño a casi hombre».
- **Salud mental**: el Rey Helado como metáfora del **Alzheimer** y la
  soledad (*Vulture*); Marceline, de una **familia no tradicional**, con
  emociones que «a veces reflejaban depresión» (*Teen Vogue*).
- **Representación LGBTQ+**: la revista *Them* llamó a Marceline «uno de
  los mejores retratos de angustia bisexual» en animación
  ([Wikipedia: Marceline](https://en.wikipedia.org/wiki/Marceline_the_Vampire_Queen)).
- **Imaginación pura**: humor fácil con temas duros (guerra nuclear,
  muerte, identidad) (Wikipedia, recepción).

### Con quién se identifica el público ✅

- **Finn**: crece con su público; *Entertainment Weekly* lo compara con
  los niños que crecieron con Harry Potter.
- **Rey Helado / Simon**: tragedia enorme mezclada con torpeza diaria; por
  eso es «el favorito de mucha gente» (*Vulture*).
- **Marceline**: lo punk, la tristeza bajo la fachada dura y, para el
  público LGBTQ+, su relación con la Princesa.
- **Cosplay**: Finn y Jake, de los disfraces más vistos en EE. UU. (*The
  Daily Beast*, 2019); hubo **globo de Finn en el desfile de Macy's de
  2013** ([wiki: Finn](https://adventuretime.fandom.com/wiki/Finn)).

### Las escenas que hacen llorar (y cómo están hechas)

- **«I Remember You»** (4×25): Marceline canta la carta que Simon le
  escribió cuando aún era humano. **Cómo está dibujada** (vista en el
  clip): casa rosa con luz plana, **primerísimo primer plano con la cabeza
  atrás y una sola lágrima** ([1:18](https://www.dailymotion.com/video/xzt1l7?t=78)),
  **una Polaroid** de ella niña ([1:36](https://www.dailymotion.com/video/xzt1l7?t=96))
  y un **flashback entre ruinas** con Hambo. **Música**: «Remember You»
  con omnichord y la batería del Rey Helado. *io9*: «una de las cosas más
  intensas que he visto en años» ✅.
- **«Simon & Marcy»** (4×24): nominado al Emmy; en listas de los 10
  mejores episodios (*Geek.com*) ✅.
- **El final, «Ven Conmigo»** (10×13): «desgarrador, aventurero e
  inventivo»; tono «tierno y un poco lloroso» ✅. En **Reddit**
  (r/adventuretime): «**I definitely cried on the last episode and my mom
  thought I was faking**» (1186 puntos) y «Just cried when finishing the
  last episode» (167) ✅
  ([Arctic Shift](https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=adventuretime&title=cried&limit=15&sort=desc)).
- **«Obsidian»**: «por fin, felices juntas», Marceline y la Princesa (§14).
- **Para reír**: «Bacon Pancakes» (4×16) y el «¿qué es una corchea?» de
  Marceline (3×10) (§14, §2.3).
- ⚠️ Faltan **vídeos de reacción** con minuto: YouTube pide sesión.

## Punto 22 del encargo · Fan dubs y comunidad hispana

Sección nueva de la segunda pasada. **YouTube y TikTok no dejan ver vistas
ni fechas desde este servidor**: van título, canal y tema; las métricas,
⚠️.

- **Fandubs latinos en YouTube** ⚠️ (existencia por buscador, sin vistas):
  «Hora De Aventura - Chico Malo (Fandub Español Latino)»; «Hora de
  aventura "Parodia" (Fandub español latino)»; «Hora De Aventura Demasiado
  Joven (Fandub Español Latino) Clip»; «Muchachito malo | Hora de Aventura
  | Español latino - Fandub»; y una serie de **«Cómics de Hora de aventura
  (Fandub español)»** con al menos los n.º 2 a 7, el último de
  **septiembre de 2024**: un proyecto sostenido.
- **TikTok**: **@angelon_2002_fandubs** dobló una escena de **«Estacas»**
  con el **Hierofante Vampiro** hecho por «Artista Galáctico», con
  **#fandubcomunidad #fandoblaje #horadeaventura** ⚠️. **@whiderlin_hot**
  comparó **«Soy tu problema»** en latino y en castellano ⚠️.
- **Traducciones de canciones por fans**: LyricsTranslate, Letras.com y
  Cifra Club tienen «I Remember You» y «Everything Stays» en español ✅.
- **El disco oficial en español** (§3.4) es la base de muchos covers: ya
  hay una versión cantada con la que comparar ✅.
- **La campaña por Karla Falcón** (§10.2): firmas, un grupo de Facebook y
  hilos en McAnime y Taringa **para que volviera a la Dulce Princesa**. Es
  el ejemplo más fuerte de la comunidad hispana **defendiendo su doblaje**
  ✅.
- **Actores en convenciones**: Isabel Martiñón en la Expomac de Veracruz y
  en Starcon; Karla Falcón en Festigame 2024 (§10.2) ✅.
- **Memes hispanos**: los **modismos de Jake** («¡Ay, mamachita!»,
  «compadre») y la polémica de su voz «neutra» (§10.3) ✅; HBO Max México
  presume de que «no hay doblaje más icónico» (§12.2).
- ⚠️ **No encontré** un canal de fandub con métricas grandes comprobables.
  Quien tenga YouTube abierto: buscar «Hora de aventura fandub capítulo
  completo».

## Punto 23 del encargo · Colaboraciones y cruces

Sección nueva de la segunda pasada. Fuente principal: la página
[«References in other media»](https://adventuretime.fandom.com/wiki/References_in_other_media)
de la wiki, leída entera, con prensa para fechas y precios.

### Videojuegos con pieles o personajes ✅

- **Fortnite**: Finn, Jake, Dulce Princesa y Marceline como **skins**
  (1500 V-Bucks cada uno, 3800 el pack), update v34.30, **abril de 2025**
  ([ScreenRant](https://screenrant.com/fortnite-adventure-time-skins/),
  [Sportskeeda](https://www.sportskeeda.com/fortnite/how-get-finn-jake-princess-bubblegum-marceline-adventure-time-skins-fortnite)).
  **El objeto del plan está dentro**: el **«Marcy's Ax Bass»** es pico y
  **instrumento tocable en Fortnite Festival** («A family heirloom
  converted into a wicked bass guitar»), junto a un keytar de la Princesa
  ([Fortnite.gg](https://fortnite.gg/cosmetics?id=17683)). Mochilas:
  Chicle Espacial, BMO, Hambo. Segunda tanda con Fionna, Cake, Conde
  Limongrab y Rey Helado, **15-ene-2026**.
- **MultiVersus**: Finn, Jake y un Guardia Banana desde 2024; **Marceline**
  el **20-dic-2024** ([GameRant](https://gamerant.com/multiversus-marceline-adventure-time-release-date-price/)).
  Mapa «Tree Fort». Cerró servidores el **30-may-2025** ⚠️.
- **LEGO Dimensions** (2016): Level Pack con Finn, Team Pack con Jake y la
  Princesa Grumosa (27-sep-2016), Fun Pack con **Marceline** (18-nov-2016).
- **Minecraft**: el logro **«Adventuring Time!»** y el **«Adventure Time
  Mash-up Pack»** (mapa de Ooo, texturas y skins), **30-may-2017**.
- **Brawlhalla**: Finn, Jake y Dulce Princesa, mapa y efecto K.O.
  ([nota oficial](https://www.brawlhalla.com/news/what-time-is-it-adventure-time-in-valhalla-patch-3-44/)).
- **League of Legends** (el baile de Jinx, la piel de Zed) y **Skullgirls**
  (Filia y Fionna): guiños ⚠️ (sólo la wiki).
- **Xbox Live** (2012): 30 prendas de avatar, con la corona del Rey Helado
  y **el bajo-hacha** ([Polygon](https://www.polygon.com/2012/10/9/3480640/adventure-time-avatar-items-xbox-live)).

### Figuras oficiales (su pose es referencia 3D) ✅

- **Funko Pop!**: Marceline **#31** y **#301 con guitarra** (exclusiva de
  Hot Topic), y una versión **Adventure Time × Minecraft**
  ([#31](https://www.tcgplayer.com/product/135801/funko-pop-vinyl-adventure-time-marceline),
  [#301](https://www.tcgplayer.com/product/135786/funko-pop-vinyl-adventure-time-marceline-with-guitar),
  [BoxLunch](https://www.boxlunch.com/product/funko-pop-adventure-time-x-minecraft-marceline-vinyl-figure/11442336.html)).
  La #301 es la figura más directa de **Marceline con su bajo**.

### Cosplay bien hecho: el bajo-hacha con materiales reales ✅

- **MDF de ¼" + espuma aislante de ½"** a los dos lados, lijada
  ([2StoryProps](http://2storyprops.blogspot.com/2013/03/marcelines-axe-bass-adventure-time.html)).
- Cuerpo de **pino con plantilla**, mástil de **dos tablas de 2×3"**
  atornilladas, paso a paso en [The RPF](https://www.therpf.com/forums/threads/marcelines-axe-bass-build-from-adventure-time.221761/).
- Versión ligera: **cartón piedra y goma EVA**, cuerdas de alambre
  ([Nerd Caliber](https://www.nerdcaliber.com/making-good-cosplay-great-marcelines-guitar-a-tutorial/),
  [Cosplay Sass](https://cosplaysass.wordpress.com/2019/02/20/marceline-axe/)).
- Sirven como **referencia de volumen y materiales** para el modelo 3D.

### Parodias y cruces ✅

- **MAD Magazine** n.º 520, con Finn como Alfred E. Neuman.
- **Gaia Online** (2012): objetos virtuales y evento con Pendleton Ward
  (22-mar-2012).
- Cameos en **Steven Universe** («Sadie's Song») y **OK K.O.!** («Crossover
  Nexus»).
- ⚠️ No encontré colaboraciones de moda o belleza (Vans, OPI, Uniqlo) con
  dos fuentes: sólo ropa con licencia en Hot Topic. **Cafés temáticos**:
  no se buscaron ⚠️.

## Punto 24 del encargo · Obras parecidas y temas relacionados

Sección nueva de la segunda pasada.

- **El semillero: «The Marvelous Misadventures of Flapjack»** (Cartoon
  Network, 2008-2010). Pendleton Ward fue guionista y storyboarder ahí ✅
  ([SlashFilm](https://www.slashfilm.com/1581694/flapjack-cartoon-network-disney-nickelodeon-descendants/),
  [Wikipedia](https://en.wikipedia.org/wiki/Adventure_Time)).
- Del mismo equipo, series de tono parecido (fantasía, humor y emoción) ✅:
  **Gravity Falls** (Alex Hirsch), **Over the Garden Wall** (Patrick
  McHale, director creativo de Adventure Time hasta la temporada 2),
  **Steven Universe** (Rebecca Sugar, storyboarder de Adventure Time y
  autora de las canciones de Marceline) y **Regular Show** (J.G. Quintel,
  director creativo en las dos primeras temporadas).
- **Influencias que reconoce Ward**: **Dungeons & Dragons** («Writing for
  the show is a lot like playing DnD… I get all my dungeon crawls out in
  writing the show») ⚠️
  ([The Mary Sue](https://www.themarysue.com/pendleton-ward-interview/));
  **Miyazaki / Totoro** para los momentos bonitos, **Home Movies** y **Dr.
  Katz** para el diálogo relajado ⚠️ (Wikipedia).
- Las cartelas beben de **novela pulp, D&D, Frazetta y cine de artes
  marciales de los 70** ✅ (§3.2).
- **Otras láminas del servidor**: hay una biblia en marcha de **Steven
  Universe** (`biblias/64-steven-universe/`, sólo partes todavía). Tiene
  el mismo aire (Rebecca Sugar, canciones): **no repetir** en ella la idea
  de «disco o canción en papel» si esta lámina la usa.

## Punto 25 del encargo · El mundo, la historia y sus símbolos

Sección nueva de la segunda pasada.

### Las reglas del mundo, en cinco líneas ✅

1. **Ooo es la Tierra**, unos **mil años después de la Guerra de los
   Champiñones**, un cruce nuclear de finales del s. XX o principios del
   XXI ([wiki: Mushroom War](https://adventuretime.fandom.com/wiki/Mushroom_War)).
2. La bomba **despertó al Lich** y **trajo de vuelta la magia**.
3. Los humanos casi desaparecieron; de la mutación nacieron las razas
   nuevas (gente-dulce, elementales…).
4. Ooo se reparte en **reinos**: Helado, Dulce, Condado de Limongrab,
   Wildberry, de Fuego, de las Nubes; el **Espacio Grumoso** es otra
   dimensión ([wiki: Land of Ooo](https://adventuretime.fandom.com/wiki/Land_of_Ooo)).
5. Frederator publicó **dos mapas oficiales** de Ooo (uno en blanco y negro
   de Ghostshrimp, otro a color).

### La historia por arcos

- **T1-5**: episodios sueltos con pistas del pasado de Simon y de
  Marceline ✅.
- **T6**: Finn conoce a su padre humano ✅.
- **T7, «Estacas»**: el pasado vampiro de Marceline; hace las paces con lo
  que es ✅.
- **T8, «Islands»**: Finn, Jake, BMO y Susan cruzan el mar; Finn conoce a su
  madre ✅.
- **T9, «Elements»**: la magia elemental vuelve Ooo una distopía ✅.
- **T10, el final**: la Princesa contra su tío **Gumbald**, Finn contra el
  lado oscuro de **Fern**, y **Betty** le quita la corona a Simon ✅.
- Fuente del detalle por arcos: [Wikipedia, temporada 6](https://en.wikipedia.org/wiki/Adventure_Time_season_6)
  y las siguientes ⚠️ (una fuente para el detalle).
- Después: «Tierras lejanas» (2020-2021, con «Obsidian»), «Fionna & Cake»
  (2023-2024) y «Misiones Secundarias» (2026) (§10.5).

### Símbolos y vocabulario que un fan reconoce al instante

- **El bajo-hacha** de Marceline (§3.5) ✅.
- **El Enchiridion**, el manual del héroe; del griego *encheiridion*, «lo
  que se lleva en la mano» ✅
  ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/WesternAnimation/AdventureTime),
  [Wikipedia](https://en.wikipedia.org/wiki/The_Enchiridion!)).
- **La corona del Rey Helado**, creada por Urgence Evergreen: la que
  **volvió loco a Simon** ✅ ([wiki](https://adventuretime.fandom.com/wiki/Ice_King%27s_crown)).
- **La Espada de Hierba** de Finn y luego su brazo de cactus ✅
  ([wiki](https://adventuretime.fandom.com/wiki/Grass_Sword)).
- **La Nocheósfera**, el inframundo de Hunson Abadeer ✅
  ([wiki](https://adventuretime.fandom.com/wiki/Nightosphere)).
- **Hambo**, el osito de Marceline, regalo de Simon ✅ (§8).
- **Card Wars**, el juego de cartas que se volvió juego real ✅.
- Palabras: **Ooo**, **Glob** (como «Dios»), **Nocheósfera**, **Espacio
  Grumoso**, **«¿Qué hora es? ¡Hora de aventura!»**, y las muletillas
  **«¡Algebraico!»** y **«¡Matemático!»** ⚠️ (TV Tropes; se usan sobre todo
  al principio).

---

## 19 · Tres conceptos para la lámina de #musica-nueva

Los tres usan los textos de §0. Las frases «en la voz de la serie» son
**traducción mía**, no del doblaje (no la encontré). Recortes siempre por
`v3/integrar.py` y comprobados a 1:1.

> **Segunda pasada: qué cambió en los conceptos.** Los tres siguen, pero
> ahora tienen **imágenes reales vistas**: las **6 poses oficiales tocando
> el bajo** (§3.7), las poses V1-V12 con minuto (§15), la **paleta medida**
> de la casa de Marceline (§5.2.b), la **grabadora amarilla** de «Fry Song»,
> la **nota de Simon** como modelo de papel escrito a mano (hoja
> `escenas_09` n.º 408) y modelos 3D **CC BY** del bajo (Haxis), BMO y la
> casa del árbol (§4.1.b).

### Concepto A — «El estreno en la caja» (Marceline en su casa)

- **Objeto y sitio**: sobre **el sofá de la casa de Marceline**, dentro
  de la cueva (§5.1), **una caja de discos abierta**, inspirada en la
  **caja real de Mondo** (§3.4): dentro, **un LP de 12"**, **un 10"**,
  **un single de 7"** y **un casete**. **El bajo-hacha** apoyado en el
  brazo del sofá. Velas en la pared. Por la ventana, la **laguna** con
  reflejos azules.
  - En Blender: caja de cartón con tapa, vinilos de colores (amarillo,
    azul oscuro y rosa, como los de Mondo), casete, el bajo (modelo de
    **Haxis, CC BY**, o el de Yogensia), sofá sencillo. Cartón
    **Cardboard001-004** y madera **Wood092-095** de ambientCG, CC0 (§5.4).
  - **Segunda pasada**: la casa por dentro es **rosa `#F8AEC5`** con techo
    `#FBE0E8` y **sofá rojo `#D94344`** (medido en «Fry Song»); piso azul
    verdoso (hoja `escenas_09` n.º 385 y 386: el sofá rojo con Finn y
    Jake). Sobre la mesa, **la grabadora amarilla** de «Fry Song»
    ([0:12](https://www.dailymotion.com/video/x51arca?t=12)): el objeto
    con que Marceline graba sus estrenos.
- **Personaje**: **Marceline flotando** encima de la caja, **sentada en
  el aire con el bajo**, como la **Special Pose D** del model sheet
  oficial (§3.7,
  [imagen](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/5/59/Modelsheet_marceline_innewoutfit_playingaxebass_-_specialposed.jpg)),
  o **bocabajo tocando** como en «Fry Song»
  ([0:00](https://www.dailymotion.com/video/x51arca), pose V1). Ropa de
  casa: camiseta gris y vaqueros, o el **suéter a rayas rojo** de «Fry
  Song» (`#630515`), con su rojo de siempre.
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
  sombra. Ojo: dentro de la casa la serie usa **luz plana y cálida**
  (§5.2); la laguna por la ventana es lo único frío.
- **La hoja de letras**: papel crema arrugado con letra a mano en tinta
  negra, como **la nota de Simon** (`escenas_09` n.º 408).
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
  colgado (pose de §15 n.º 10, 10×07 ≈7:00 ⚠️: sin clip), un brazo arriba
  saludando al público. **Segunda pasada, pose con imagen real**: la
  **Special Pose B** (echada atrás, ojos cerrados, cantando,
  [model sheet](https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/d/d6/Modelsheet_marceline_innewoutfit_playinaxebass_-_specialposeb.jpg))
  o la **V4** (ceño y colmillos cantando con fuerza,
  [0:52](https://www.dailymotion.com/video/x537pqr?t=52)). Alternativa:
  **bajo al hombro** (tráiler «Obsidian»,
  [1:08](https://www.dailymotion.com/video/x7xejon?t=68)) para «lo
  siguiente».
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
- **Personajes**: **BMO** en la mesa; **Finn con audífonos** escuchando
  (visto en «Fry Song», [0:40](https://www.dailymotion.com/video/x51arca?t=40))
  y **Jake con su viola** detrás (corre tocándola en «I'm Just Your
  Problem», [0:04](https://www.dailymotion.com/video/x537pqr?t=4)),
  escuchando como al final de la serie («Would you like to hear it?»
  «Sure!» «Yeah!», 10×13 ≈43:04). Marceline puede asomar flotando por la
  ventana con el bajo, para que la protagonista siga en la lámina.
  - En Blender, segunda pasada: **BMO** ([featbear456978, CC BY](https://sketchfab.com/3d-models/none-ffeb3e9ab97e4e3dbed4ddc0650d8b9b))
    y **la casa del árbol entera** ([gleksono, CC BY](https://sketchfab.com/3d-models/none-0131dc63d8894892b0c87dc852f23984)):
    el sitio real en 3D. Dato para el texto: **BMO era el favorito de
    Pendleton Ward** (§9).
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

Actualizado en la segunda pasada. Entre corchetes, lo que se resolvió.

**Resuelto** ✅: [imágenes vistas: model sheets, capturas, 3 hojas] ·
[minutos exactos de «Fry Song», «I'm Just Your Problem», «I Remember You»,
tráiler de «Obsidian», piloto y 4 clips más] · [6 frases textuales del
doblaje, en audio] · [BMO latino, directores y Claudia Urbán, con la tabla
de Doblaje Wiki] · [fecha del disco en español: 25-oct-2019] · [licencias
de Sketchfab por la API] · [hex medidos] · [la fuente de fans del logo:
sólo trae tildes en tabla Mac Roman] · [«¡Oh por Glob!»] · [retratos del
juego de DS y menú de Card Wars].

**Sigue sin verificar** ⚠️:
- **Minutos de escenas sin clip**: «Henchman» (1×22), «Marceline's Closet»
  (3×21), el concierto del Anfiteatro Fantasma (10×07), y los minutos de
  los episodios largos (final y «Obsidian» entero). Siguen por
  transcripción (±1 min).
- **La cueva de Marceline**: sin fotograma; su luz y paleta, de memoria.
- **Quién canta** a Marceline en cada temporada (Claudia Urbán, Patty
  Urbán, Carla Cerda): una sola fuente.
- **Episodio exacto** de cada audio de Doblaje Wiki (la wiki no lo dice).
- **Frases latinas de Marceline** en las escenas de la lámina («Thanks for
  helping me record», la del Hoyo Musical): no encontradas.
- **Estudio de «Misiones Secundarias»** (Iyuno México, Miguel Ángel Leal):
  una sola fuente.
- **Encuesta oficial de popularidad**: no la encontré; Ranker da 401.
- **Vistas y fechas de los fan dubs** (YouTube y TikTok cerrados).
- **Cajas de texto** de «Nameless Kingdom» y «Pirates of the Enchiridion».
- **Colores sin medir**: BMO (el fondo rosa tapaba), la corona de la
  Dulce Princesa, los filos del bajo con luz de día.
- **Licencias** de 6 modelos de Sketchfab (Z3bbz, Froes,
  TravisEvashkevich, deadlygeek, Hoho, 10958533).
- **Encuadres típicos** según el estudio (no hay *making of* sobre eso).
- **Altura** de los personajes (ningún infobox la trae).
- **«El sicario»** = «Hitman» (3×04): deducción mía.
- **Variantes de la intro** por miniserie: existen, sin mirar a fondo.

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
