---
tags: [biblia, serie, laminas, biblioteca]
serie: "Naruto (NARUTO -ナルト- y NARUTO -ナルト- 疾風伝 / Shippuden)"
canal: "sin canal: propuesta #reto-de-la-semana (y #general-doblaje de reserva)"
fecha: 2026-09-24
---

# Biblia · Naruto — para la biblioteca (y su canal propuesto)

> [!important] Cómo se hizo, y sus límites
> - **Dos fases**. Al principio la red estaba cerrada (Fandom, Wikipedia,
>   dafont, vidaextra daban 403) y trabajé con **búsqueda web** y
>   **GitHub**. A media tarea **se abrió la red** y completé con:
>   - `herramientas/investigar_serie.py` sobre **Narutopedia**
>     (`naruto.fandom.com`): **555 imágenes** de personajes y sitios y
>     **41 de objetos**, en 13 hojas numeradas. **Las miré todas**. Copio
>     3 a `hojas/` (ver §3.0). Los tamaños que doy son **los reales** que
>     devuelve la API.
>   - **Doblaje Wiki por su API** (`action=parse`): reparto, estudio,
>     director y «Datos de interés» de *Naruto* y *Naruto Shippuden*.
>   - **Narutopedia por su API**: encuestas oficiales, la prueba de los
>     cascabeles, el campo 3, la piedra de los caídos, Ichiraku, la música.
>   - **yt-dlp** (cliente `mweb`, porque YouTube pedía «no soy un robot»):
>     títulos, duración, fecha, visitas, capítulos y descripción. **Sin
>     subtítulos** (los vídeos consultados no tenían).
>   - **API de Sketchfab** (licencias), **Poly Haven** y **ambientCG**
>     (CC0), **Arctic Shift** (Reddit) y **Wayback Machine** (The Cutting
>     Room Floor).
>   - Colores **medidos con Pillow** en fotogramas de la wiki y en una
>     captura del juego *Storm*.
> - **Siguió cerrado**: TV Tropes y The Cutting Room Floor directos (403,
>   Cloudflare), Game UI Database (reto de Cloudflare) y los subtítulos de
>   YouTube.
> - La lista de búsquedas, con su idioma, está en la **bitácora** (§21).
> - **GitHub** dio lo más valioso:
>   - Los **subtítulos japoneses de Hulu, con sus tiempos**, de **los 220
>     episodios de Naruto** y **los 500 de Shippuden**, del repositorio
>     [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv).
>     Los pasé a texto y los busqué con `grep`. Con ellos doy **el minuto
>     exacto** y la frase japonesa. **La traducción al español es mía**, no
>     la del doblaje latino (esa no está en ningún subtítulo abierto).
>   - La letra **Ninja Naruto** (la del logo), que encontré dentro de tres
>     juegos de fans en GitHub, y **50 letras de Google Fonts**. Comprobé una
>     a una, con fontTools, si traen á é í ó ú ñ ¿ ¡.
> - **Cómo leo los episodios**: «N005» es **Naruto**, episodio 5. «S133» es
>   **Shippuden**, episodio 133. La numeración de Hulu coincide con la
>   japonesa y con la de Netflix Latinoamérica. El minuto es el del archivo
>   de Hulu: en otra plataforma puede moverse **uno o dos minutos** (Netflix
>   corta a veces el resumen del principio).
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su minuto.
>   ⚠️ **dudoso**: una sola fuente, o lo describo de memoria. Lo de memoria
>   siempre va marcado. **Lo que se VE** en una escena (la pose, la luz) lo
>   describo de memoria ⚠️: mira el fotograma antes de usarlo.
> - **Segunda pasada (25-sep-2026), con la red abierta y un equipo de
>   cuatro investigadores** (imagen, vídeo, voz y texto). Se usó:
>   `herramientas/fotogramas.py` sobre **episodios completos del doblaje
>   latino en Internet Archive** (N001, N005, N025, N086; Shippuden 86 y
>   135) y clips de **Dailymotion**; colores **medidos** con
>   `herramientas/estilo.py` y Pillow; **Doblaje Wiki por su API** con
>   segunda fuente (AniList, ANMTV, Fandoblaje Wiki); **Narutopedia por su
>   API** (databooks, Akatsuki, Jinchūriki, bandana); **API de Sketchfab**
>   (rigs con licencia); **Arctic Shift** (Reddit); **Jikan** (MyAnimeList).
>   Siguió cerrado: YouTube desde el servidor («no soy un robot»), TV Tropes
>   y TCRF directos (403), AnimeThemes (error 522).

## Segunda pasada · qué cambió

**Corregido (antes → ahora)**, todo mirado en fotograma o medido:

- **Naruto acepta la 10.ª pregunta** (N025): «golpea la mesa y se levanta»
  → **sentado en su pupitre, brazo derecho en alto con el puño cerrado,
  sudando, ceño fruncido**, 00:10:45-00:10:54
  ([fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20025.mp4?t=648)) (§2, §15).
- **«¡Aprobados!» de Kakashi** (N005, 19:54): «luz de mediodía, se inclina
  hacia ellos» → **de noche, cielo morado con nubes**; Kakashi **salta en
  el aire con los brazos cruzados**, Naruto sigue **atado al tocón,
  riendo** ([fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20005.mp4?t=1194)) (§2, §5, §15).
- **Vendas de Sasuke** (Parte I): «en los brazos» → **en las piernas y
  tobillos**; jersey `#06406C` medido (§16).
- **Vestido de Sakura**: `#C8283C` ⚠️ de memoria → **`#85223F`** medido
  (rojo vino); en el fotograma de N005 a contraluz de atardecer da `#9C2A38` (§5, §16).
- **Nube de Akatsuki**: «rojo puro `#C0282E`» → **`#58262D` / `#9B3E35`**
  según la luz, borde hueso `#CFC3B7`; la tela no es negro puro, es
  `#2A2B33` (§5, §16).
- **Chaleco de Iruka**: ⚠️ → **`#8F9B7B`**, sombra `#3F4843` (§16).
- **«Never Ending Spirit»** (Dailymotion): **no es un ending oficial**, es
  un AMV de fan con marca «AnimeYT.tv». No se cita como oficial (§11).
- **«Sadness and Sorrow»**: autor dudoso → **Yasuharu Takanashi** (dos
  fuentes); shakuhachi, shamisen, piano y violín (§11).
- **Doblaje**: pasan a ✅ con segunda fuente Gaara, Tsunade, Rock Lee,
  Pain, Shikamaru, Minato (Edson Matus desde 2021), Iruka en Shippuden e
  Ibiki (§10).

**Añadido**:

- Caras de Naruto y Tsunade por emoción con fotograma (§8).
- Tendencia de TikTok del **«hand seal dance»** con «Silhouette» (§12).
- Secciones nuevas de los **puntos 18 a 25**: técnica y cómo
  replicarla, texturas 2D, gustos (databooks), por qué la aman y qué
  escenas hacen llorar, fan dubs, colaboraciones y figuras, obras
  parecidas, el mundo y sus símbolos.
- Tabla **«Cumplimiento del encargo»** y bitácora de la segunda pasada.
- `referencias.json` ampliado con las referencias de las cuatro partes.

**⚠️**: había **84**; se resuelven unos 20 (colores, pose, voces, música,
bandana rayada). Los que quedan se explican donde están y en la tabla de
cumplimiento.

---

## 0 · Naruto no tiene canal: dónde encaja mejor

El encargo dice que Naruto está en la **biblioteca**: es el anime clave del
doblaje latino, pero todavía no tiene canal. Miré los 45 canales de
`servidor/inventario.md` y los que ya tienen serie en `encargos/01` a `29`.

### La propuesta: **ıı・🎯・reto-de-la-semana** ✅ (libre)

Ningún encargo tiene este canal asignado (lo comprobé con `grep` en
`encargos/`). Del inventario, sección **EL ESTUDIO**:

> **ıı・🎯・reto-de-la-semana** (foro) · 2 hilos · etiquetas: Reto activo,
> Cerrado, Doblaje, Canto, Locución, Para empezar, Con trampa, Libre — _Un
> reto por semana: una línea, una escena, un tono. Se entrega dentro del
> hilo del reto. No se gana nada y esa es la gracia: es para grabar _
> - 📌 📌 De qué va esto (0 msj) · adj: reto-de-la-semana.png
> - EJEMPLO · Reto 1 · La misma frase, tres edades (0 msj) · adj: —

(La descripción del canal viene **cortada** en el inventario: termina en
«es para grabar». Hay que leerla entera en Discord antes de escribir la
lámina. Ya existe un `reto-de-la-semana.png` en el hilo fijado: esta
propuesta lo sustituiría, o sería su lámina 2.)

**Por qué Naruto y no otra serie** (todo con minuto, ver §2):

| Lo que pide el canal | Lo que pasa en Naruto |
|---|---|
| **Un reto** que se entrega | La serie **está hecha de pruebas**: el examen de la Academia (N001), **los cascabeles de Kakashi** (N004-N005), el **examen chūnin** (N020-N080), el **Rasengan en tres fases** (N086-N090) |
| Etiqueta **Con trampa** | **Los cascabeles**: hay **dos** cascabeles para **tres** alumnos. Es una prueba **hecha a propósito para que se peleen**; la respuesta es **trabajar en equipo** (N005, 00:13:49 a 00:14:03 ✅). Y la **10.ª pregunta** del examen escrito **no existe**: la pregunta era atreverse (N025, 00:12:52 ✅) |
| Etiqueta **Para empezar** | Las **misiones de rango D**: buscar un gato perdido, hacer de niñera, cosechar papas. Iruka: «**Todo el mundo empieza por las misiones fáciles**» (N006, 00:03:53 ✅) |
| «**No se gana nada y esa es la gracia**» | Kakashi no busca al que coge el cascabel, busca al que **comparte la comida**. Aprueban **perdiendo** (N005, 00:19:54 ✅) |
| Una **línea**, una **escena**, un **tono** | Naruto es **la** serie de las frases dobladas en Latinoamérica: «**¡De veras!**», «**Yo soy el más perrón aquí**» ✅. La cuenta SDV ya hace «**Reto de doblaje**» con escenas de **Kakashi** (n.º 1041) e **Itachi** (n.º 252), retando a sus voces oficiales ✅ (§10.5) |

### De reserva: **ıı・💬・general-doblaje** ⚠️ (lo lleva el encargo 29)

El encargo 29 busca serie para seis canales, entre ellos #general-doblaje
(«Del oficio: micros, voces, técnica y dudas de novato»). Naruto es **el
anime del doblaje latino** por excelencia: Isabel Martiñón lleva **20 años**
con el personaje ✅. El sitio sería **el puesto de ramen Ichiraku**, donde
Iruka escucha a Naruto (Concepto C, §19). Si el coordinador prefiere no
pisar el encargo 29, el Concepto C sirve igual para **🍟・General** (voz) o
para la sala **🔊・Aula**.

### Los textos de la lámina 1 (qué es #reto-de-la-semana)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Reto de la semana** | nombre del canal |
| 2 | **Un reto por semana** | ritmo |
| 3 | **Una línea, una escena, un tono** | qué es un reto |
| 4 | **Se entrega dentro del hilo del reto** | dónde |
| 5 | **No se gana nada** | la regla |
| 6 | **Esa es la gracia** | el tono |
| 7 | (el final de la descripción, «es para grabar…», cuando se lea entero) | para qué |
| 8 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

### Los textos de la lámina 2 (las ocho etiquetas)

Ocho etiquetas no caben bien en la lámina 1. Propongo **lámina 2** como **el
tablón de misiones** de la oficina del Hokage (N006 ✅), con **tres grupos**:

| Grupo | Etiquetas | En el mundo de Naruto |
|---|---|---|
| **Estado** | Reto activo · Cerrado | sello rojo de «en curso» o «cumplida» en el pergamino de la misión |
| **Disciplina** | Doblaje · Canto · Locución | tres pergaminos de colores |
| **Dificultad** | Para empezar · Con trampa · Libre | rango **D** (para empezar), **los cascabeles** (con trampa), misión **libre** |

(En la lámina, cada etiqueta va en su propio sitio: sin «·».)

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Qué es | Manga de **Masashi Kishimoto** (Weekly Shōnen Jump, 1999-2014, **72 tomos**) ✅. Anime de **Studio Pierrot**: *Naruto* (2002-2007, **220 episodios**) y *Naruto Shippuden* (2007-2017, **500 episodios**) ✅ (los cuento en los subtítulos). |
| Por qué encaja en #reto-de-la-semana | Es una serie de **exámenes y entrenamientos**. **Los cascabeles de Kakashi** son un reto con trampa: gana el que comparte (N005 ✅). |
| El objeto | **Los dos cascabeles** plateados colgados de un **cordel rojo** (obj 13 ✅), **el despertador** puesto a las 12 y **los tres tocones** del campo de entrenamiento 3, junto a la **piedra de los caídos** con forma de kunai (N004-N005 ✅, Narutopedia ✅). Todo se hace en Blender en una tarde: hay despertador y tocones **CC0** en Poly Haven (§4.2). |
| El más querido | En la encuesta mundial oficial **NARUTOP99** (2023, **4,6 millones de votos**): **1.º Minato**, **2.º Itachi**, **3.º Sakura**, 4.º Shisui, **5.º Kakashi**, 6.º Naruto, 8.º Sasuke ✅. En las 7 encuestas de la Jump, **Kakashi ganó 2** (la 1.ª y la 3.ª) y fue 2.º o 3.º en las demás; **Iruka, el profe, salió en el top 5 en seis de siete** ✅ (Narutopedia). Ver §9. |
| Quién habla en la lámina | **Kakashi** (el que pone la prueba; 5.º, y el más reconocible como «profe»), con **Naruto** atado al poste como contrapunto cómico. De reserva: **Itachi** (2.º) para un reto «con trampa», o **Jiraiya** para textos. Ver §19. |
| Cuadro de diálogo propio | **No es una burbuja blanca**. Naruto «habla» en **pergaminos** (makimono), en el **tablón de misiones**, en el **examen escrito** de Ibiki, en el **libro de Jiraiya**, en los **pensamientos entre 《 》** del subtítulo oficial y, en el juego *Storm*, en una **banda oscura translúcida con filete de bronce** (`#9A804A`, medido) y el nombre en una pestaña a la izquierda. Ver §7. |
| Letras | **Ninja Naruto** (la del logo, gratis, **sin tildes ni ñ**: sólo para «RETO DE LA SEMANA»), **Yuji Syuku / Yuji Boku** (pincel japonés), **Shojumaru** (latín con aire japonés), **Potta One** / **Reggae One** (rótulos). Las de Google Fonts traen á é í ó ú ñ ¿ ¡: comprobado en el archivo. |
| Voz latina | Naruto **Isabel Martiñón** ✅, Sasuke **Víctor Ugarte** ✅, Sakura **Christine Byrd** (Naruto y Shippuden 1-5) y **Montserrat Aguilar** (Shippuden 6-22) ✅, Kakashi **Alfonso Obregón** (y **Óscar López** en los ep. 440-500 de Shippuden) ✅, Itachi **Héctor Emmanuel Gómez** ✅, Jiraiya **Paco Mauri** ✅, Iruka **José Antonio Macías** ✅. Estudio **Art Sound México** (Naruto, 2006-2010) y **Labo** (Shippuden 6-22, 2023-2024); dirección y adaptación de **Eduardo Garza** ✅. Ver §10. |
| Tono | **Cálido y de esfuerzo**, con momentos tristes. Naranja de Naruto, verde de Konoha, cielo azul, madera. Nada de neón ni de estética «oscura» genérica: la tristeza de Naruto es **lluvia y atardecer**, no sangre. |
| Juegos | **Ultimate Ninja Storm** (CyberConnect2): banda de diálogo **oscura translúcida** a todo lo ancho, **filete de bronce** arriba y pestaña con el nombre ✅ (captura medida). Tiene un minijuego escondido de **trepar árboles con tres niveles** ✅ (The Cutting Room Floor). **Storm Connections** (2023) ✅. Ver §13. |

---

## 2 · Las escenas que sirven (con minuto)

Todas salen de los **subtítulos japoneses de Hulu** en
[kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/NARUTO):
el texto y el minuto están comprobados ✅. La traducción es mía.

### 2.1 Los cascabeles de Kakashi (el reto con trampa)

N004 se llama «**¡Prueba! Ejercicio de supervivencia**» (試練サバイバル演習)
y N005 «**Fracasados: la conclusión de Kakashi**» (失格カカシの結論).

| Escena | Minuto | Qué pasa / qué se dice | Para qué sirve |
|---|---|---|---|
| N004 | 00:03:17 | En la azotea: «**Primero, preséntense**». Naruto: le gusta **el ramen de Ichiraku que le invita Iruka** (00:04:12) y su sueño es «**superar al Hokage**» (00:04:23) | Presentar al equipo 7 |
| N004 | 00:07:23 a 00:07:59 | «Mañana, en el campo de entrenamiento, decido si aprueban. **A las 5 de la mañana**». «**No desayunen. Vomitarán**» | El anuncio del reto |
| N004 | 00:08:42 a 00:08:47 | Llega tarde: «**Es que se me cruzó un gato negro**» | Kakashi siempre llega tarde |
| N004 | 00:08:58 | «**Listo, las 12 en punto**» (pone el **despertador**) | **El despertador**: objeto |
| N004 | 00:09:05 a 00:09:13 | «**La tarea de hoy: quitarme estos cascabeles antes del mediodía**. El que no lo logre, **se queda sin almuerzo**» | **El enunciado del reto** |
| N004 | 00:09:26 a 00:09:34 | Sakura: «¿Por qué **sólo dos** cascabeles?». «Porque al menos uno **acabará atado al poste**» | La trampa |
| N004 | 00:09:47 | «**Vengan con la intención de matarme**, o no los conseguirán» | El reto va en serio |
| N004 | 00:10:25 a 00:10:50 | Frena a Naruto en un parpadeo: «No te apures, **aún no dije “empiecen”**». «Creo que **por fin empiezan a caerme bien**» | Kakashi calmado, con ironía |
| N004 | 00:10:56 | «**Preparados… ¡Ya!**» (よーい…スタート！) | **Cartela de inicio** |
| N005 | 00:05:54 | Kakashi, pensando: «**No me da tiempo a leer *Icha Icha Paradise***» | El libro en la mano |
| N005 | 00:13:11 a 00:13:19 | «¿Saben qué significa **un equipo de tres**? **Trabajo en equipo**» | La respuesta del reto |
| N005 | 00:13:51 a 00:14:03 | «**Es una prueba hecha a propósito para que se peleen**. Busco a los que pongan al equipo por delante de su propio interés» | **La trampa, explicada** |
| N005 | 00:15:15 a 00:16:09 | Les muestra **la piedra de los caídos** (慰霊碑): «Aquí está grabado **el nombre de mi mejor amigo**». A 16:07, **de espaldas, mano en el bolsillo**, luz de atardecer naranja entre los árboles ([fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20005.mp4?t=967)) ✅ | Momento serio |
| N005 | 00:16:53 | «**Aquí, la regla soy yo**» (ここでは 俺がルールだ) | **Frase para la lámina** |
| N005 | 00:17:40 a 00:18:51 | Sasuke y Sakura **le dan de comer a Naruto**, que está atado al poste, aunque estaba prohibido | Compartir |
| N005 | 00:19:54 a 00:20:00 | «**¡A-pro-ba-dos!**» (ごうかっく！). **De noche, cielo morado con nubes**: Kakashi salta en el aire con los brazos cruzados, Sakura a su lado, Naruto **todavía atado al tocón, riendo** ([fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20005.mp4?t=1194)) ✅ | **Celebrar** |
| N005 | 00:20:16 | «**Un ninja debe ver lo que hay debajo de lo de debajo**» (裏の裏を読むべし) | El lema de «Con trampa» |
| N005 | 00:20:19 a 00:20:27 | «En el mundo ninja, **el que rompe las reglas es escoria. Pero el que abandona a sus compañeros es peor que escoria**» | **La frase más famosa de Kakashi** ✅ |
| N005 | 00:20:46 | «**El equipo 7 empieza sus misiones mañana**» | Cierre |
| N005 | 00:21:15 | Naruto, todavía atado: «**¡Desátenme!**» | El chiste final |

### 2.2 El examen chūnin: la 10.ª pregunta (la otra trampa)

| Escena | Minuto | Qué pasa / qué se dice | Para qué sirve |
|---|---|---|---|
| N024 | 00:01:35 | «**Primera prueba del examen chūnin. Soy el examinador, Ibiki Morino**» | El examinador |
| N024 | 00:03:51 a 00:04:17 | «Hay **reglas importantes**». «**Diez preguntas**, un punto cada una. **Se resta**» | Reglas numeradas: idea para lámina 2 |
| N024 | 00:10:20 a 00:10:30 | Sakura entiende: «**No era un examen de conocimientos**» | La trampa |
| N025 | 00:05:03 | «Primero van a **elegir si hacen o no la 10.ª pregunta**» | El dilema |
| N025 | 00:06:22 | «**Este año, la regla soy yo**» (今年はこの俺がルールだ) | Eco de Kakashi |
| N025 | 00:10:45 a 00:11:03 | Naruto, **sentado en su pupitre**, alza el brazo derecho con **el puño cerrado**, sudando y con el ceño fruncido ([fotograma 10:48](https://archive.org/download/naruto-completo/Naruto%20-%20025.mp4?t=648), corregido en la segunda pasada: no golpea la mesa ni se levanta): «**¡No me subestimes! ¡Yo no huyo! La haré**. Aunque me quede de genin toda la vida, **seré Hokage igual**» | **Pose de reto aceptado** |
| N025 | 00:11:41 a 00:11:44 | «**No me retracto de mis palabras. Ese es mi camino ninja**» (まっすぐ自分の言葉を曲げねえ 俺の忍道だ) | **El lema de Naruto** ✅ |
| N025 | 00:12:33 | «**¡Todos los que quedan, aprobados!**» | Celebrar |
| N025 | 00:12:52 a 00:12:55 | «**Esa pregunta nunca existió.** La elección **era** la 10.ª pregunta» | La trampa revelada |

### 2.3 Misiones y entrenamientos (retos «para empezar»)

| Escena | Minuto | Qué pasa / qué se dice | Para qué sirve |
|---|---|---|---|
| N006 | 00:02:37 | «**Misión: capturar a Tora, la gata perdida. Cumplida**» | La misión rango D por excelencia |
| N006 | 00:03:23 a 00:03:34 | El Hokage lee el listado: «Cuidar al hijo de un noble, un recado al pueblo vecino, **ayudar a cosechar papas**…». Naruto: «**¡No, gracias!**» | El tablón de misiones |
| N006 | 00:03:50 a 00:03:57 | Iruka: «**Todo el mundo empieza por misiones fáciles y sube con la experiencia**» | Etiqueta **Para empezar** |
| N006 | 00:04:24 a 00:04:29 | «Los encargos se ordenan **por dificultad: A, B, C y D**» | Rangos = dificultad |
| N006 | 00:05:09 | Iruka, distraído: «Ayer comí **tonkotsu**, hoy tocará **miso**» | Iruka y el ramen |
| N010 | 00:13:17 a 00:13:57 | Kakashi: «**Treparán árboles. Sin usar las manos**». Sube caminando por el tronco | Reto de control |
| N010 | 00:14:12 a 00:14:28 | «El objetivo es llevar **la chakra justa al sitio justo**» | «Una línea, un tono»: precisión |
| N086 | 00:20:15 a 00:20:47 | Jiraiya: «Fase 1 del Rasengan: **reventar un globo de agua** haciendo girar el agua con chakra» | Reto por fases |
| N087 | 00:05:58 y 00:13:55 | «**Esto es sólo la fase 1**». Fase 2: «**¿Una pelota de goma?**» | Subir de nivel |

### 2.4 Las frases que todo el mundo conoce (con minuto)

| Frase (traducción mía) | Japonés | Dónde |
|---|---|---|
| «¡De veras!» (su muletilla) | だってばよ | **993 veces** en los subtítulos de Naruto (las conté) ✅ |
| «Superaré a todos los Hokage» | 先代の どの火影をも超えてやるんだ | N001, 00:05:09 ✅ |
| «Te voy a enseñar mi técnica sexy» | お色気の術 | N001, 00:03:28 ✅ |
| «¡Técnica de los clones de sombra!» | 影分身の術 | N001, 00:18:56 ✅ |
| «Felicidades… te graduaste» (Iruka le da su bandana) | 卒業… おめでとう | N001, 00:20:41 ✅ (el fotograma es un **primer plano de la bandana ya puesta**, [archivo](https://archive.org/download/naruto-completo/Naruto%20-%20001.mp4?t=1241)) |
| «No me retracto de mis palabras. Ese es mi camino ninja» | まっすぐ自分の言葉を曲げねえ 俺の忍道だ | N025, 00:11:41; N044, 00:09:21 ✅ |
| «¡Shannaro!» (la Sakura interior) | しゃーんなろ！ | N001, 00:02:42; N003, 00:03:49 ✅ |
| «Qué fastidio» (Shikamaru) | めんどくせえ | N001, 00:03:01; N023, 00:04:53 ✅ |
| «El que abandona a sus compañeros es peor que escoria» | 仲間を大切にしないやつは それ以上のクズだ | N005, 00:20:27 ✅ |
| «Perdóname, Sasuke. Otra vez será» (Itachi, toque en la frente) | 許せ サスケ また今度だ | N084, 00:03:17; S135, 00:01:10 ✅ |
| «Perdóname, Sasuke. Esta es la última vez» | 許せ サスケ / これで 最後だ | S141, 00:20:09 a 00:20:11 ✅ |
| «Pase lo que pase, **siempre te querré**» (Itachi se despide) | お前がこれからどうなろうと 俺はお前をずっと愛している | S339, 00:20:49 a 00:20:55 ✅ |
| «No es que al Hokage lo reconozcan todos. **Al que reconocen todos, ese llega a Hokage**» | 皆から認められた者が 火影になるんだ | S478, 00:15:32 a 00:15:36 ✅ |
| «Sasuke… **eres mi amigo**» | 友達だ | N133, 00:02:09; S478, 00:08:50 ✅ |
| «Nos vemos, **Iruka-sensei**. El ramen, **te lo pago cuando sea importante**» | ラーメン代は… 出世払いね！ | N220, 00:19:51 a 00:19:53 ✅ |

### 2.5 Jiraiya y su libro (la escritura dentro de Naruto)

Jiraiya **escribe novelas**. Naruto **se llama como el protagonista** de su
primer libro, *La leyenda del ninja muy valiente* (ド根性忍伝, literalmente
«Leyenda del ninja con agallas»).

| Escena | Minuto | Qué pasa / qué se dice |
|---|---|---|
| N053 | 00:02:06 a 00:02:09 | Su presentación, en pose de kabuki sobre un sapo: «**¡Bien preguntado! Espíritu sapo del monte Myōboku, el Sabio de los Sapos!**» |
| N053 | 00:02:19 | Naruto le pone el mote: «**¡Ero-sennin!**» (el Sabio Pervertido) |
| N177 | 00:04:36 | Anda «**con prisas por el último tomo de *Icha Icha Violence***» |
| S128 | 00:19:17 | «¿Lees mi *Leyenda del ninja valiente*?» |
| S133 | 00:14:51 a 00:15:22 | Minato: «**El protagonista no se rinde nunca**. ¿Podemos **ponerle su nombre a nuestro hijo**?». Jiraiya: «¡Es un nombre que se me ocurrió **comiendo ramen**!». «**Naruto**» |
| S133 | 00:16:52 a 00:16:57 | Recuerda a Naruto: «Lo más importante de un ninja no es cuántas técnicas sabe. **Es no rendirse**» |
| S133 | 00:19:15 a 00:19:31 | Muere pensando: «**Es hora de dejar la pluma**… ¿Qué título le pongo a **la continuación**? **La historia de Naruto Uzumaki**» |
| S174 | 00:17:21 a 00:17:36 | Naruto a Pain: «Yo no sé escribir libros como mi maestro. **La continuación es mi propia vida**» |

---

## 3 · Arte oficial y referencias visuales

La wiki de Fandom estaba cerrada, así que no hay hojas de contacto. Esto es
lo que existe, con su enlace, para buscarlo a mano.

### 3.0 Las hojas de contacto (lo que vi en Narutopedia) ✅

Corrí `investigar_serie.py` dos veces sobre `naruto.fandom.com`. Las hojas
completas están en `herramientas/referencias/naruto/` (**555 imágenes, 12
hojas**) y `herramientas/referencias/naruto-objetos/` (**41 imágenes, 1
hoja**), cada una con su `indice.json`. Copié **3 hojas** a `hojas/`:

| Hoja en `hojas/` | Índice de origen | Qué trae |
|---|---|---|
| `objetos_01.jpg` | `naruto-objetos` n.º 1-41 | **Los objetos y sitios**: cascabeles, libros *Icha Icha*, pergaminos, bandana, kunai, Ichiraku, campo 3, piedra de los caídos, Academia |
| `personajes_10.jpg` | `naruto` n.º 433-480 | Jiraiya, **Kakashi leyendo *Icha Icha***, **el aula del examen chūnin**, parte 1 |
| `personajes_11.jpg` | `naruto` n.º 481-528 | **Primeros planos de la parte 1** (Naruto, Sakura, Kakashi, Itachi, Minato), **Ichiraku al atardecer**, **la foto del equipo 7**, *renders* de Jiraiya, Iruka e Itachi |

**Las 30 mejores, por número** (tamaño real; enlace al original):

| N.º | Qué es | Tamaño | Para qué |
|---|---|---|---|
| obj 13 | **Kakashi enseña los dos cascabeles** colgando de un cordel rojo, bosque detrás | 1916×1080 | **Pose de presentar el reto** ([original](https://static.wikia.nocookie.net/naruto/images/9/97/Bell_Test_new.png)) |
| obj 15 | **El campo 3 desde arriba**: claro verde, río y bosque | 1913×1080 | Fondo del Concepto A ([original](https://static.wikia.nocookie.net/naruto/images/7/7f/Third_Training_Ground.png)) |
| obj 39 | El campo 3 **al atardecer** | 800×600 | Luz alternativa ([original](https://static.wikia.nocookie.net/naruto/images/6/61/Third_Training_Ground.PNG)) |
| obj 36 | **La piedra de los caídos** (en el anime: negra, **con forma de kunai**) | 1280×716 | Objeto serio ([original](https://static.wikia.nocookie.net/naruto/images/8/8f/Konoha%27s_Memorial_Stone.png)) |
| obj 40 | La piedra **en el manga**: losa con nombres | 657×402 | ([original](https://static.wikia.nocookie.net/naruto/images/9/91/Konoha_Monument.jpg)) |
| obj 11 | **Los tres libros *Icha Icha***: *Paradise* (naranja), *Violence* (rojo), *Tactics* (verde azulado), títulos a mano en katakana | 1920×1080 | **El libro de Kakashi** ([original](https://static.wikia.nocookie.net/naruto/images/9/97/Three_Icha_Icha_Books.png)) |
| obj 30 | **Pergaminos del Cielo (天, claro) y la Tierra (地, azul oscuro)** | 1429×1080 | **El pergamino como cuadro de diálogo** ([original](https://static.wikia.nocookie.net/naruto/images/8/83/Scrolls.png)) |
| obj 37 | Naruto carga el **Pergamino Sellado**, enorme | 907×979 | Pergamino gigante ([original](https://static.wikia.nocookie.net/naruto/images/b/b9/Scroll_of_Seals.png)) |
| obj 21 | **Bandana de Konoha** sobre madera (chapa y tela azul) | 1440×1080 | Objeto ([original](https://static.wikia.nocookie.net/naruto/images/f/fc/Forehead_Protector.png)) |
| obj 23 | **Ichiraku** original al atardecer, letrero «ラーメン 一楽» | 1440×1080 | Concepto C ([original](https://static.wikia.nocookie.net/naruto/images/b/be/Ichiraku_ramen.png)) |
| obj 38 | Ichiraku nuevo, de día | 1048×652 | ([original](https://static.wikia.nocookie.net/naruto/images/9/9b/Ichiraku_Ramen.png)) |
| obj 8 | **Despacho del Hokage**: mesa, papeles, kanji 影 | 1920×1080 | Mesa de misiones ([original](https://static.wikia.nocookie.net/naruto/images/4/42/Hokage%27s_office.png)) |
| obj 1 | **La Academia** en 4K | 3840×2152 | Fondo ([original](https://static.wikia.nocookie.net/naruto/images/a/ae/The_Academy.png)) |
| obj 5 | Portada de *Ultimate Ninja Storm* (PS3) | 1387×1600 | Juego ([original](https://static.wikia.nocookie.net/naruto/images/2/2e/NinjaStorm.jpg)) |
| 470 | **Naruto en el aula del examen**, pupitres en gradas («no me rindo») | 1440×1080 | **Concepto B** ([original](https://static.wikia.nocookie.net/naruto/images/3/34/Naruto_refuses_to_give_up.png)) |
| 481 | Sakura en el examen, sentada, con los demás aspirantes | 1440×1080 | Concepto B ([original](https://static.wikia.nocookie.net/naruto/images/6/61/Sakura_tries_to_give_up_test.png)) |
| 461 | **Kakashi lee *Icha Icha*** con rayos de luz, emocionado | 1440×1080 | Kakashi cómico ([original](https://static.wikia.nocookie.net/naruto/images/f/fa/Kakashi_Icha_Icha.png)) |
| 522 | **La foto del equipo 7**: Kakashi con las manos en las cabezas de Naruto y Sasuke, Sakura sonríe | 1124×923 | **Presentar al equipo** ([original](https://static.wikia.nocookie.net/naruto/images/5/50/Team_Kakashi.png)) |
| 389 | La foto del **equipo Minato** (la misma pose, generación anterior) | 1912×1080 | Eco de la foto ([original](https://static.wikia.nocookie.net/naruto/images/f/fd/Team_Minato.png)) |
| 278 | **Primera reunión del equipo 7** en la azotea, de espaldas, Konoha delante | 1920×1080 | Fondo con personajes ([original](https://static.wikia.nocookie.net/naruto/images/5/57/Team_7_first_meeting.png)) |
| 492 | **Naruto parte 1**, primer plano sonriente | 1440×1076 | Cara y colores ([original](https://static.wikia.nocookie.net/naruto/images/d/d6/Naruto_Part_I.png)) |
| 498 | **Kakashi** parte 1, primer plano | 1439×1076 | Cara ([original](https://static.wikia.nocookie.net/naruto/images/2/27/Kakashi_Hatake.png)) |
| 495 | **Sakura** parte 1, primer plano | 1440×1076 | Cara ([original](https://static.wikia.nocookie.net/naruto/images/6/64/Sakura_Part_1.png)) |
| 458 | **Jiraiya**, primer plano con la chapa «油» | 1440×1080 | Cara ([original](https://static.wikia.nocookie.net/naruto/images/2/21/Profile_Jiraiya.PNG)) |
| 399 | **Jiraiya en su pose de kabuki**, mano abierta hacia delante | 1916×1076 | **Presentarse a lo grande** ([original](https://static.wikia.nocookie.net/naruto/images/d/d7/Jiraiya_Posing.png)) |
| 518 | *Render* de Jiraiya de cuerpo entero, pose de kabuki | 837×1275 | Recorte ([original](https://static.wikia.nocookie.net/naruto/images/5/5a/Jiraiya_full2.png)) |
| 525 | *Render* de **Iruka** de cuerpo entero, con **carpeta en la mano** | 636×1600 | **Iruka en la mesa de misiones** ([original](https://static.wikia.nocookie.net/naruto/images/b/bf/Iruka_full.png)) |
| 526 | *Render* de **Itachi** (resucitado) con capa | 870×1168 | Recorte ([original](https://static.wikia.nocookie.net/naruto/images/5/55/Edo_Itachi_NXB.png)) |
| 265 | **Itachi toca la frente de Sasuke** niño | 1920×1080 | «Otro día será» ([original](https://static.wikia.nocookie.net/naruto/images/c/c5/Itachi_pokes_Sasuke.png)) |
| 232 | **La Sakura interior**: silueta de línea blanca sobre negro, ojos brillantes, puño | 1920×1080 | Pensamiento gritado ([original](https://static.wikia.nocookie.net/naruto/images/a/aa/Inner_Sakura.png)) |
| 155 | **Foto de registro ninja de Naruto**, con la cara pintada | 1920×1080 | Chiste de ficha ([original](https://static.wikia.nocookie.net/naruto/images/1/1e/Naruto%27s_Ninja_Registration_Photo.png)) |
| 156 | **Naruto con el pulgar arriba**, fondo blanco | 1920×1080 | **Celebrar / animar** ([original](https://static.wikia.nocookie.net/naruto/images/4/42/Naruto%27s_Promise.png)) |
| 329 | **Naruto sale de Konoha**, puño adelante, camino | 1920×1077 | **Animar / empezar** ([original](https://static.wikia.nocookie.net/naruto/images/c/ca/Naruto_Departing_Konoha.png)) |
| 105 | **Naruto y Sakura en Ichiraku**, barra | 1927×1080 | Concepto C ([original](https://static.wikia.nocookie.net/naruto/images/3/35/Sakura_and_Naruto_Ramen.png)) |
| 108 | **El mensaje cifrado de Jiraiya** («9.31.8 / 106.7 / 207.15») en la espalda de un sapo | 1920×1080 | Texto escrito en el mundo ([original](https://static.wikia.nocookie.net/naruto/images/e/e7/Dying_Message.png)) |
| 13 | **La Roca de los Hokage** en 4K (época Boruto, 7 caras) | 3840×2152 | Fondo ([original](https://static.wikia.nocookie.net/naruto/images/c/cf/Hokage_Rock.png)) |
| 551 | **Logo de Shippuden** (NARUTO naranja-amarillo, ナルト y 疾風伝 en rojo) | 1250×600 | Tipografía ([original](https://static.wikia.nocookie.net/naruto/images/4/48/Naruto_Shipp%C5%ABden_Logo.png)) |
| 544 | **Portada del tomo 3** (Kakashi arriba, Naruto delante) | 761×1200 | Portada de manga ([original](https://static.wikia.nocookie.net/naruto/images/e/e1/Vol3.png)) |
| 1 | *Render* de **Naruto niño y adulto** juntos | 2785×4255 | Recorte grande ([original](https://static.wikia.nocookie.net/naruto/images/c/cd/Naruto_both_parts.png)) |

Muchas de las 555 son de **Boruto** o de peleas de la guerra: **no sirven**
para este canal.

### 3.1 De la web oficial (naruto-official.com)

| Qué | Enlace | Para qué |
|---|---|---|
| **ANIME GALLERY** oficial | [naruto-official.com/special/anime-gallery](https://naruto-official.com/special/anime-gallery) | Ilustraciones del anime, ordenadas. **Lo primero que hay que mirar** ⚠️ (no pude abrirla) |
| Especial **20 aniversario** del anime (2022) | [naruto-official.com/en/special/20th](https://naruto-official.com/en/special/20th) | Arte de aniversario, vídeos |
| **NARUTOP99**, resultados | [narutop99.naruto-official.com/en](https://narutop99.naruto-official.com/en/) y [el archivo](https://narutop99.naruto-official.com/en/archive/) | **Kishimoto dibujó a los 22 primeros** en una ilustración nueva ✅ ([Natalie](https://natalie.mu/comic/news/520749), [web oficial](https://naruto-official.com/en/news/01_1468)) |
| Ilustración nueva de **Tetsuya Nishio** para la caja DVD 16 de Boruto | [naruto-official.com/news/01_1486](https://naruto-official.com/news/01_1486) | Estilo del diseñador del anime |
| **Cuatro episodios nuevos** del 20 aniversario: su imagen teaser (2023) | [Animate Times](https://www.animatetimes.com/news/details.php?id=1690034607) | Naruto niño **redibujado en 2023** (los episodios se aplazaron ⚠️) |
| Web antigua de TV Tokyo | [naruto.com/j/](http://www.naruto.com/j/) | Fondos de pantalla antiguos ⚠️ |

### 3.2 Los libros de arte de Kishimoto

| Libro | Qué trae | Fuente |
|---|---|---|
| ***The Art of Naruto: Uzumaki*** (1.º) | Ilustraciones a color de **1999 a mediados de 2004**. **Las 20 primeras portadas de la Jump** con Naruto, **una entrevista larga** y **el paso a paso de una ilustración** | ✅ [Narutopedia](https://naruto.fandom.com/wiki/Art_Collection:_Uzumaki), [VIZ Shop](https://shop.viz.com/products/the-art-of-naruto-uzumaki), [Simon & Schuster](https://www.simonandschuster.com/books/The-Art-of-Naruto-Uzumaki/Masashi-Kishimoto/The-Art-of-Naruto-Uzumaki/9781421514079) |
| ***Paint Jump: Art of Naruto*** (2.º) | La etapa de Shippuden ⚠️ (de memoria) | — |
| ***Uzumaki Naruto: Illustrations*** (3.º) | **El final del manga**, con **20 páginas de notas del autor** sobre cada imagen y un póster | ✅ [Amazon](https://www.amazon.com/Uzumaki-Naruto-Illustrations-Masashi-Kishimoto/dp/1421584395), [Simon & Schuster](https://www.simonandschuster.com/books/Uzumaki-Naruto-Illustrations/Masashi-Kishimoto/Uzumaki-Naruto-Illustrations/9781421584393) |
| ***NARUTO THE ANIMATION CHRONICLE 天＆地*** | Libro «premium» del anime, de Shueisha | [jcs.shueisha.co.jp](http://jcs.shueisha.co.jp/narutochronicle/_sp/ten.html) |
| ***Tetsuya Nishio Art Book*** (西尾鉄也画集) | Dibujos del diseñador del anime | [Anime Style](http://animestyle.jp/shop/archives/954) |

### 3.3 Portadas de los tomos (poses vivas) ⚠️ de memoria

Las portadas de Kishimoto son **fondos blancos o de color plano** con el
personaje **en acción**, casi nunca de pie quieto:

| Tomo | Qué se ve | Pose útil |
|---|---|---|
| 1 | Naruto **agachado** con el pulgar y una sonrisa de pillo, remolino detrás | Presentar |
| 3 | **Kakashi arriba**, Naruto delante gritando ✅ (lo vi: n.º 544 de la hoja) | Maestro y alumnos |
| 4 | Naruto con **la bandana en la mano** ⚠️ | Orgullo |
| 27 | Naruto y Jiraiya **de viaje** (portada del fin de la parte 1) ⚠️ | Marcharse |
| 72 | **Naruto y Sasuke**, adultos, mano con mano ⚠️ | Final |

(Compruébalas en la lista de tomos de VIZ o en la wiki: las describo de
memoria.)

### 3.4 Vídeo oficial con fotogramas nuevos en alta: «ROAD OF NARUTO»

El mejor sitio para sacar **fotogramas limpios en 4K**: el vídeo del 20
aniversario **rehace las escenas famosas con el dibujo de hoy** ✅.

- [«完全新作PV “ROAD OF NARUTO”», canal oficial スタジオぴえろ【公式】](https://www.youtube.com/watch?v=yKELA1qBAKA) ✅: **9:57**, subido el **3 de octubre de 2022**, **30,4 millones** de visitas (yt-dlp, 24-sep-2026). Lema de la descripción: «**¡Seré Hokage sí o sí, de veras!**» (絶対、火影になってやるんだってばよ！！).
- Ojo: la versión «4K Remastered» [yvOYf6cMpEE](https://www.youtube.com/watch?v=yvOYf6cMpEE) **no es oficial**: la subió el canal de fans «Devilizer» (oEmbed) ⚠️.
- Pierrot anunció también **un libro con los dibujos originales** del PV: [aviso de 31 s](https://www.youtube.com/watch?v=okzWxkX0lK4) ✅.
- Versión de VIZ: [YouTube](https://www.youtube.com/watch?v=QczGoCmX-pI) ✅.
- Dura **unos 10 minutos**. Trae **Naruto contra Neji**, **la muerte de
  Jiraiya** y **Pain destruyendo Konoha**, con los openings **«GO!!!»**,
  **«Blue Bird»** y **«Silhouette»** ✅ ([AniTrendz](https://anitrendz.net/news/2022/10/03/road-of-naruto-20th-anniversary-video-features-modern-reproduction-of-famous-naruto-scenes/)).
- Equipo: dirección **Yoshifumi Sasahara**, jefe de animación **Tetsuya
  Nishio**, director de arte **Hiromasa Ogura** ✅ (AniTrendz).
- Publicado el **3 de octubre de 2022** ✅.

### 3.5 Lo que falta ⚠️

- **Hojas de modelo** oficiales del anime (vistas de frente, perfil y
  espalda): la wiki no las tiene.
- **Fotogramas de la escena de los cascabeles** más allá del obj 13: los
  minutos de §2.1 son el camino para sacarlos de Netflix o Crunchyroll.

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D de la serie en Sketchfab (licencia comprobada por la API) ✅

Ojo: la **licencia CC** cubre el modelo, **no el diseño**, que es de
Shueisha y Pierrot. Sirven para **mirar formas y medidas**; en la lámina,
mejor modelar lo propio. «BY» = hay que dar crédito; «NC» = **no
comercial**. Todos los datos salen de `api.sketchfab.com/v3/models/<uid>`.

| Modelo | Autor (año) | Licencia | Enlace |
|---|---|---|---|
| Bandana de Konoha | **Rimacc** (2018) | CC BY | [sketchfab](https://sketchfab.com/3d-models/7779469bf90e4a0fb3647c51e9260270) |
| Bandanas de todas las aldeas | **DarvinAbraham** (2017) | CC BY | [sketchfab](https://sketchfab.com/3d-models/8f5fea1a77b145dd833c0b6c0f24d360) |
| «The Oath of Pain»: bandana con un **kunai clavado en una roca** | **Calfan** (2022) | CC BY-NC | [sketchfab](https://sketchfab.com/3d-models/5e3e2fc3715a4d099dbc435ac965aafc) |
| Bandana de Konoha | **Calfan** (2020) | CC BY-NC | [sketchfab](https://sketchfab.com/3d-models/ff1d4d15eddd403ea4ba7716212a2899) |
| Kunai | **Yanez Designs** (2018) | CC BY | [sketchfab](https://sketchfab.com/3d-models/4692daa67ec445348dbf81302bb5de0c) |
| Kunai | **kaiqueroque** (2017) | CC BY | [sketchfab](https://sketchfab.com/3d-models/a2375f70a0e840d4968c5f634f718a7d) |
| **Libro *Icha Icha Tactics*** (イチャイチャタクティクス) | **AnaCi** | CC BY | [sketchfab](https://sketchfab.com/3d-models/044b0b94815d458980ccde530a217dc9) |
| **Pergamino** («Naruto Water Scroll») | **DMI** | CC BY | [sketchfab](https://sketchfab.com/3d-models/a1107381d0a94e77bf0b4f8fbe4be5c1) |
| **Despacho del Hokage** («Hokage Room Naruto») | **Jp André** | CC BY | [sketchfab](https://sketchfab.com/3d-models/1485ceeb0acd4afba3d7b5a4544fe2c9) |
| Despacho del Hokage («Hokage Office») | **elre** | CC BY | [sketchfab](https://sketchfab.com/3d-models/07512299acb64f40a4b36d63286de7cf) |
| Roca de los Hokage (seis caras) | **jmartinez20592** | CC BY | [sketchfab](https://sketchfab.com/3d-models/c9cc3357a6ee46c2bff49c94e409fa99) |
| **Ichiraku Ramen** | **Doverlock** (2019) | CC BY-NC | [sketchfab](https://sketchfab.com/3d-models/c57a7c0bdca4446aade5241cc621f56e) |
| **Ichiraku Ramen** | **JojoInMess** (2017) | CC BY-NC | [sketchfab](https://sketchfab.com/3d-models/872aaeab34084ba1a8ff9377ce29f623) |
| Ichiraku, diorama | **meraliny** (2024) | **sin descarga** | [sketchfab](https://sketchfab.com/3d-models/80e6ef525c5e48aab647d581937717f3) |
| Ichiraku, diorama (JAMA Jam, julio de 2024) | **Jon Gilleland** | **sin descarga** | [sketchfab](https://sketchfab.com/3d-models/75839d92e3e3479f8eaa60771561630d) |

**Objetos genéricos útiles (no de Naruto), CC BY**:

| Para qué | Modelo | Autor | Enlace |
|---|---|---|---|
| Campanillas (forma de cascabel japonés) | «Furin», campanilla de viento | **seirogan** | [sketchfab](https://sketchfab.com/3d-models/a323143ea1ec46689c12e8b02b5ef19c) |
| Poste de entrenamiento | «combat training post» | **lachiebear117** | [sketchfab](https://sketchfab.com/3d-models/756477e8314d4eb7a035cf36f27aa84d) |
| Muñeco de madera | «Wooden Training Dummy» | **Jimmy** | [sketchfab](https://sketchfab.com/3d-models/3b4054d8c3814c99a2cca8332d08e6fe) |
| **Noren** (cortinita de Ichiraku) | «Noren (Low Poly)» | **game_travel** | [sketchfab](https://sketchfab.com/3d-models/ddbab39e8bf5464fbf18c94572ae34dc) |
| Cuenco de ramen | «Ramen bowl» | **Jungle Jim** | [sketchfab](https://sketchfab.com/3d-models/374aba41259447e792b13ca99747a281) |

### 4.2 Modelos libres (CC0) para los objetos de la lámina ✅

Comprobados por la **API de Poly Haven** (sí respondía). **Licencia CC0**:
no hace falta dar crédito, pero lo pongo.

| Para qué | Modelo | Autor | Enlace |
|---|---|---|---|
| **El despertador de Kakashi** | **Alarm Clock 01** (despertador de dos campanas, metal gastado; se puede animar) | Yann Kervran, James Ray Cock | [polyhaven.com/a/alarm_clock_01](https://polyhaven.com/a/alarm_clock_01) |
| **Los tocones y postes** del campo 3 | **Tree Stump 01** y **02** | Rob Tuytel | [01](https://polyhaven.com/a/tree_stump_01), [02](https://polyhaven.com/a/tree_stump_02) |
| Tronco caído | **Dead Tree Trunk** | Rob Tuytel | [polyhaven.com/a/dead_tree_trunk](https://polyhaven.com/a/dead_tree_trunk) |
| **La piedra de los caídos** | **Boulder 01**, **Rock Moss Set 01/02** | Rico Cilliers; Kless Gyzen | [boulder_01](https://polyhaven.com/a/boulder_01), [rock_moss_set_01](https://polyhaven.com/a/rock_moss_set_01) |
| Musgo y suelo | **Moss 01** | Rob Tuytel | [moss_01](https://polyhaven.com/a/moss_01) |
| **El aula del examen** | **School Desk 01**, **Standing Chalkboard 01** | Ethan Place; ParzivalCG | [desk](https://polyhaven.com/a/SchoolDesk_01), [pizarra](https://polyhaven.com/a/standing_chalkboard_01) |
| **Ichiraku** | **Wooden Stool 01/02**, **Wooden Bowl 01**, **Wooden Spoon**, **Tea Set 01** | Kuutti Siitonen; Oliver Harries; Ronnie Barter; James Ray Cock y otros | [stool](https://polyhaven.com/a/wooden_stool_01), [bowl](https://polyhaven.com/a/wooden_bowl_01) |
| Farol | **Wooden Lantern 01** | James Ray Cock | [wooden_lantern_01](https://polyhaven.com/a/wooden_lantern_01) |

### 4.3 Fan art 2D (mirar, nunca pegar)

| Obra | Autor | Enlace |
|---|---|---|
| «Naruto team7 team Kakashi» | **pung lonewolf** | [ArtStation](https://pungpp.artstation.com/store/art_posters/1qa3/naruto-team7-team-kakashi) |
| «[ TEAM 7 ] Fan-Art» | **Davide Rossini** | [ArtStation](https://www.artstation.com/artwork/vqa46) |
| «Kakashi Team 7» (chibi, Procreate) | **solisandluna** | [DeviantArt](https://www.deviantart.com/solisandluna/art/Kakashi-Team-7-873178656) |
| Render del equipo 7 | **ShiroChan92** | [DeviantArt](https://www.deviantart.com/shirochan92/art/Render-Team-7-Kakashi-Sasuke-Sakura-Naruto-483376260) |
| **Aldea inspirada en Konoha** (paisaje 3D) | **Christoffer Radsby** | [ArtStation](https://www.artstation.com/artwork/rR0Be) |

### 4.4 Código y datos en GitHub

| Repositorio | Qué es | Para qué |
|---|---|---|
| [ben-tiki/naruto-handsign-dataset](https://github.com/ben-tiki/naruto-handsign-dataset) | Fotos de **manos reales haciendo los sellos** | Referencia de **manos** para los sellos |
| [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/NARUTO) | Subtítulos japoneses con tiempos | Todos los minutos de este documento |
| [animecannonhunter-hash/anime-filler-list-data](https://github.com/animecannonhunter-hash/anime-filler-list-data) | Qué episodios son **relleno** (CC BY 4.0) | Evitar escenas de relleno |

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

| Sitio | Qué es | Escenas |
|---|---|---|
| **Campo de entrenamiento 3** | Claro del bosque con **tres tocones en fila** (donde Kakashi y el Tercero ataban a sus alumnos), un **río ancho y hondo**, montañas al fondo, y debajo **la piedra de los caídos**, pulida y **con forma de kunai** en el anime (una losa en el manga) | N004-N005 ✅; [Narutopedia: Third Training Ground](https://naruto.fandom.com/wiki/Third_Training_Ground), [Memorial Stone](https://naruto.fandom.com/wiki/Memorial_Stone) ✅ |
| **La Academia** | Aula con pupitres en gradas; examen de graduación | N001 ✅ |
| **Oficina de misiones** | Mesa larga con el Hokage e Iruka, y el **listado de misiones** | N006 ✅ |
| **Aula del examen escrito** | Gradas con 153 aspirantes, Ibiki delante de la pizarra ✅ (el número, en Narutopedia; en la segunda pasada) | N024-N025 ✅ |
| **La Torre del Bosque de la Muerte** | Sala con el **lema del chūnin escrito en la pared** con huecos | N037, 00:06:02 a 00:06:55 ✅ |
| **Ichiraku Ramen** | Puesto de ramen con **barra, taburetes y cortinita** (noren) | N001, N037, N055 ✅ |
| **Roca de los Hokage** | Montaña con **las caras** de los Hokage. Parodia del **monte Rushmore** ✅ ([ScreenRant](https://screenrant.com/naruto-konoha-leaf-village-facts-trivia-secrets/)) | N001 (Naruto la pinta) |
| **Valle del Fin** | Cascada entre **dos estatuas gigantes** (Hashirama y Madara), con lluvia | N133-N134, S476-S478 ✅ |

**Konoha se inspira en el pueblo de Kishimoto** (Nagi, distrito de Katsuta,
Okayama) ⚠️ ([ScreenRant](https://screenrant.com/naruto-konoha-leaf-village-facts-trivia-secrets/), una fuente; en la segunda pasada se buscó también en japonés, «岸本斉史 出身 ナルト 木ノ葉隠れ 元ネタ», sin segunda fuente).

### 5.2 Luz (el campo 3, mirado en fotograma en la segunda pasada ✅; lo demás ⚠️ de memoria)

| Sitio | Hora | Luz |
|---|---|---|
| Campo 3, los cascabeles | **De madrugada a mediodía en el reto** (citados a las 5, el reloj suena a las 12 ✅); **de noche en la resolución** | Durante el reto: sol, verde intenso. **El cierre («¡Aprobados!», N005 19:54) es de noche, cielo morado tormentoso con nubes** ✅ ([fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20005.mp4?t=1194)). Ante la piedra de los caídos (16:07), **atardecer naranja entre los árboles** ✅ ([fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20005.mp4?t=967)) |
| Ichiraku | Noche o tarde | **Luz cálida** de la bombilla bajo el toldo, calle en penumbra azul |
| Aula del examen | Día, interior | Luz blanca y plana, ambiente tenso |
| Valle del Fin (N133) | Tormenta | **Gris azulado**, lluvia, contraluz de los rayos |
| Roca de los Hokage | Atardecer | **Naranja** sobre la piedra, Konoha en sombra |

### 5.3 Paleta (medida ✅ o de memoria ⚠️)

**Medida por mí** con Pillow (mediana de 9 píxeles) en los fotogramas de
Narutopedia de §3.0. Margen: ±5 por canal. Lo que no pude medir va con ⚠️.

| Qué | Hex | De dónde |
|---|---|---|
| **Pelo de Naruto** (parte 1, luz) | `#E1E11F` | medido en 492 ✅ (es **amarillo limón**, no dorado) |
| **Naranja del cuello del traje** | `#FE7A35` | medido en 492 ✅ |
| **Azul del traje** (parte 1) | `#093C7D` | medido en 492 ✅ |
| Tela de la bandana (parte 1) | `#083B7A` | medido en 492 ✅; en obj 21 `#0A2449` |
| Chapa de la bandana | `#B2B7C3` | medido en 492 ✅ (Itachi `#B6B7C2`) |
| Piel de Naruto | `#F6B498` | medido en 492 ✅ |
| Ojos de Naruto | `#5B8ABA` | medido en 492 ✅ |
| **Pelo de Kakashi** | `#D3D6DE` | medido en 498 ✅ |
| Máscara de Kakashi | `#232526` | medido en 498 ✅ |
| **Chaleco de jōnin** (verde grisáceo) | `#778372` | medido en 498 ✅ |
| Chaleco de chūnin de Iruka | `#8F9B7B`, sombra `#3F4843` | medido en `Iruka_full.png` ✅ (segunda pasada) |
| Jersey de Sasuke (parte 1) | `#06406C`, sombra `#262E38` | medido en `Sasuke_Part_I.png` ✅ (segunda pasada) |
| **Pelo de Sakura** | `#EBB8BE` | medido en 495 ✅ |
| Piel de Sakura | `#F4E0D2` | medido en 495 ✅ |
| Vestido de Sakura | **`#85223F`** (rojo vino) | medido con `estilo.py` en la ficha de la wiki ✅ (segunda pasada; antes `#C8283C` de memoria). En el fotograma de N005 16:07, a contraluz de atardecer, da `#9C2A38` |
| **Haori de Jiraiya** | `#902D43` | medido en 458 ✅ (rojo vino, no rojo puro) |
| Pelo de Jiraiya | `#F5F5F5` | color dominante en 458 ✅ |
| Capa de Akatsuki (Itachi) | Tela `#2A2B33` (azul-negro, no negro puro); **nube `#58262D` / `#9B3E35`** según la luz; borde de la nube hueso `#CFC3B7` / `#DCCFC8` | medido en dos imágenes de la wiki (`Edo_Itachi_NXB.png`, `Itachi_Akatsuki_Mobile.png`) y en un fotograma de Shippuden 86, 15:00 ([archivo](https://archive.org/download/naruto-shippuden-lat/Naruto%20shippuden%20Lat%2086.mp4?t=900)), donde en penumbra la nube baja a `#431C29` ✅ (antes `#1A1A1F`/`#C0282E` de memoria) |
| **Cielo de Konoha** (detrás de Itachi) | `#609DE1` | medido en 486 ✅ |
| **Bosque** del campo 3 | `#48832F` | medido en obj 13 ✅ |
| **Césped** del campo 3 | `#7DBF4E` | medido en obj 13 ✅; desde arriba `#82C36B` (obj 15) |
| ***Icha Icha Paradise*** (naranja) | `#EB9D77` | medido en obj 11 ✅ |
| ***Icha Icha Violence*** (rojo) | `#A94D53` | medido en obj 11 ✅ |
| ***Icha Icha Tactics*** (verde azulado) | `#1F8480` | color dominante en obj 11 ✅ |
| **Papel del pergamino del Cielo** | `#FBFDB8` (con el brillo) | medido en obj 30 ✅ |
| Tinta del kanji | `#252221` | medido en obj 30 ✅ |
| **Filete de bronce** de la caja de diálogo de *Storm* | `#9A804A` | medido en una captura del juego ✅ (§7.3) |
| Atardecer en Ichiraku | `#BB704F` | color dominante en obj 23 ✅ |

**Lo que se aprende de medir**: el anime de la parte 1 es **más saturado y
más frío** de lo que se recuerda. El pelo es **limón**, el traje es **azul
marino fuerte** (no negro) y el chaleco jōnin es **verde grisáceo**, no
verde militar.

### 5.4 Texturas reales equivalentes (CC0) ✅

Comprobadas por las **APIs de Poly Haven y ambientCG** (las dos respondían).
Todas **CC0**.

| Para qué | Textura | De dónde |
|---|---|---|
| **Pergamino y papel de misión** | **Paper001** a **Paper006** | [ambientCG](https://ambientcg.com/list?q=paper) |
| **Cordel de los cascabeles** | **Rope001**, **Rope002**, **Rope003** | [ambientCG](https://ambientcg.com/list?q=rope) |
| Corteza de los tocones | **Bark Brown 01** (Rob Tuytel) | [Poly Haven](https://polyhaven.com/a/bark_brown_01) |
| Tablones (mesa de misiones, Ichiraku) | **Brown Planks 05** (Rob Tuytel) | [Poly Haven](https://polyhaven.com/a/brown_planks_05) |
| Suelo del bosque | **Forest Ground 04**, **Forest Leaves 02** | [Poly Haven](https://polyhaven.com/textures) |
| Tela (noren, vendas) | **Rough Linen** | [Poly Haven](https://polyhaven.com/a/rough_linen) |
| Tatami (interiores) | **Tatami Mat** | [Poly Haven](https://polyhaven.com/a/tatami_mat) |
| Tejado de paja (Ichiraku) | **Reed Roof 03**, **Thatch Roof Angled** | [Poly Haven](https://polyhaven.com/textures) |
| Bambú | **Bamboo Wall** (Amal Kumar) | [Poly Haven](https://polyhaven.com/a/bamboo_wall) |
| **Cielo y luz de mediodía** (HDRI) | **Kloofendal 48d Partly Cloudy (Pure Sky)** (Greg Zaal, Jarod Guest) | [Poly Haven](https://polyhaven.com/a/kloofendal_48d_partly_cloudy_puresky) |
| **Claro del bosque** (HDRI) | **Forest Grove** (Dimitrios Savva, Jarod Guest), **Hochsal Forest** (Adrian Kubasa) | [Poly Haven](https://polyhaven.com/a/forest_grove) |
| Atardecer (HDRI) | **Evening Meadow** (Alexander Scholten) | [Poly Haven](https://polyhaven.com/a/evening_meadow) |

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

| Dónde | Qué letra | Estado |
|---|---|---|
| **Logo** «NARUTO» | Rotulación propia, de pincel, en **degradado naranja a amarillo** con **contorno rojo** y otro negro; debajo, «ナルト» en rojo. En Shippuden se añade **疾風伝** en pincel rojo oscuro (lo vi: n.º 551, 1250×600). La letra de fans **Ninja Naruto** (sk89q, 2004) lo imita | ✅ ([dafont](https://www.dafont.com/ninja-naruto.font), [1001 Fonts](https://www.1001fonts.com/ninja-naruto-font.html), [logo en la wiki](https://static.wikia.nocookie.net/naruto/images/4/48/Naruto_Shipp%C5%ABden_Logo.png)) |
| Logo japonés | «NARUTO -ナルト-» con el katakana debajo | ✅ (el título del subtítulo lo escribe así) |
| **Globos del manga** (VIZ, inglés) | Letra de cómic en mayúsculas: los rotulistas de manga en inglés usan **CC Wild Words** (Comicraft) para el diálogo y **Anime Ace** (Blambot) para el aire de shōnen de los 2000 ([FontGet](https://www.fontget.com/font/anime-ace-family/), [mangafonts.carrd.co](https://mangafonts.carrd.co/)) | ⚠️ (listas de rotulistas, no un crédito de VIZ). Anime Ace sólo es gratis para cómics sin ánimo de lucro ([Quora](https://www.quora.com/What-free-commercial-font-can-replace-anime-Ace-and-Digital-Strip)): usa **Bangers** |
| **Globos del manga** (Panini, México) | La traducción es de **Daruma S.L.** (España), no de un estudio mexicano ([mangamexico.blogspot.com](https://mangamexico.blogspot.com/2015/10/mangas-de-panini-comics.html)); la letra de rotulado **no la encontré** | ⚠️ |
| **Pergaminos y rótulos** dentro de la serie | **Pincel japonés** (kanji a mano) | ⚠️ de memoria |
| **Títulos de los episodios** | Kanji de pincel sobre fondo ⚠️ | ⚠️ |

### 6.2 Letras libres comprobadas por mí

Las bajé y abrí **con fontTools**, una a una, buscando **á é í ó ú Á É Í Ó
Ú ñ Ñ ¿ ¡ ü**. También miré si traen **kanji** (火影忍者木ノ葉).

| Letra | Para qué | Licencia | ¿Tildes, ñ, ¿ ¡? | ¿Kanji? |
|---|---|---|---|---|
| **Ninja Naruto** (sk89q) | **Sólo el título**, como el logo | Gratis, uso personal y comercial, **prohibido modificarla** (lo dice el propio archivo) | **NO**: le faltan **todas** las tildes, ñ, ¿ y ¡ | no |
| **Yuji Syuku** | **Pincel japonés** para pergaminos y sellos | OFL (Google Fonts) | **sí, todas** | **sí** |
| **Yuji Boku** | Pincel más grueso, **rótulos de misión** | OFL | sí | sí |
| **Yuji Mai** | Pincel fino, **cartas y el libro de Jiraiya** | OFL | sí | sí |
| **Shojumaru** | Latín **con aire japonés**, para títulos en español | OFL | sí | no |
| **Potta One** | Rótulo de pincel redondo, **cartelas** | OFL | sí | sí |
| **Reggae One** | Rótulo grueso, **gritos** | OFL | sí | sí |
| **Dela Gothic One** | Onomatopeyas enormes | OFL | sí | sí |
| **Zen Antique** | Texto de libro antiguo (**Jiraiya**) | OFL | sí | sí |
| **Shippori Mincho** | Texto serio (la piedra de los caídos) | OFL | sí | sí |
| **Klee One** | **Letra a mano** de alumno (el examen) | OFL | sí | sí |
| **Bangers** | Globos de cómic en mayúsculas | OFL | sí | no |
| **Permanent Marker** | Notas a rotulador | Apache | sí | no |
| **Caveat** / **Kalam** | Letra a mano en español | OFL | sí | no |
| **Kosugi Maru** | ✗ No sirve | Apache | **NO** (le faltan todas) | sí |
| **Nanum Brush Script** | ✗ No sirve | OFL | **NO** | no |

**Combinación propuesta**: título en **Ninja Naruto** sólo si no lleva
tildes («RETO DE LA SEMANA» no lleva ninguna ✅). El resto, en **Yuji
Syuku** (pincel) y **Shojumaru** (títulos). Los textos largos, en **Klee
One**. Nada de Comic Sans ni Arial.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

**Lo más importante: en Naruto el texto casi nunca va en una burbuja
blanca.** Va **escrito en objetos del mundo ninja**.

### 7.1 Lo que la serie pone en pantalla

| Soporte | Cómo es | Estado |
|---|---|---|
| **Pergamino** (makimono) | Papel claro enrollado, con **un kanji grande de pincel** en la cara exterior. Es como llegan las misiones, las técnicas prohibidas (**el Pergamino Sellado**, N001, enorme: obj 37) y los contratos de invocación | ✅ N001, N037; aspecto visto en obj 30 y obj 37 ✅ |
| **Los pergaminos del Cielo y la Tierra** (天の書・地の書) | Dos rollos, **uno claro con 天 y otro azul oscuro con 地** (obj 30), uno por equipo. **No se pueden abrir** antes de llegar a la torre: dentro está el kanji **人** («persona») y **sale Iruka invocado** | ✅ N027, 00:06:45; N037, 00:02:41 a 00:03:41 |
| **El lema en la pared** de la torre | Texto de pincel **con huecos** («虫食い文字», letras comidas por la polilla) que Iruka explica: «**Si te falta el Cielo, aprende**…» | ✅ N037, 00:06:02 a 00:06:45 |
| **El examen escrito** | Hoja con **10 preguntas**, reglas leídas en voz alta por Ibiki | ✅ N024 |
| **El listado de misiones** | Lo lee el Hokage en la mesa: rangos **A, B, C, D** | ✅ N006 |
| **La piedra de los caídos** | Nombres **grabados** en piedra negra pulida | ✅ N005, 00:15:16; obj 36 |
| **El libro de Jiraiya** | Novela con su título y su «continuación» | ✅ S133, S174 |
| **La bandana** | La hoja de Konoha grabada en metal. **Una raya horizontal sobre el símbolo** = ha renunciado a su aldea (así la llevan los de Akatsuki). En la 4.ª Guerra, las **Fuerzas Aliadas** llevan el kanji **忍** («shinobi») en vez del símbolo de su aldea | ✅ [Narutopedia, «Forehead Protector»](https://naruto.fandom.com/wiki/Forehead_Protector) + ScreenRant (segunda pasada) |

### 7.2 Cómo piensan (el subtítulo oficial)

En los subtítulos japoneses de Hulu, **los pensamientos van entre 《 》**
(dobles comillas angulares): hay **4.932 líneas así** en Naruto ✅.
Ejemplo: «《しゃーんなろ！》», la Sakura interior (N001, 00:02:42). El
narrador de la leyenda del zorro va entre **⟨ ⟩** (N001, 00:00:04) ✅.

**Para la lámina**: el pensamiento de un personaje puede ir **entre « »
dobles y en otra letra** (más fina, Yuji Mai), sin globo. Es fiel a la
serie y no es una burbuja blanca.

**La Sakura interior** (内なるサクラ): en el manga aparece como **una
segunda Sakura en blanco, gritando «¡Shannaro!»** con el kanji **内**
(«dentro») en la frente ⚠️ (de memoria). En latino grita «**¡Cha!**» ✅
(guía de cuadros de diálogo del repositorio, sacada de Doblaje Wiki).

### 7.3 En los videojuegos

**La caja de *Ultimate Ninja Storm* (2008), medida** ✅. Saqué la miniatura
en alta (1280×720) del vídeo [«All Villagers Dialogue after Main
Story»](https://www.youtube.com/watch?v=kkVhqfzWWIE) (RuNix, 7:53, versión
remasterizada de PC). La miniatura muestra **a Anko** hablando con
Naruto; su capítulo empieza en **2:42**. Otros: Jiraiya **4:15**, Sakura
**3:19**, Hinata **6:52** (capítulos del vídeo, por yt-dlp):

- **Banda oscura translúcida** a todo lo ancho, en el tercio inferior. Deja
  ver el suelo detrás (se mide `#64644C` sobre la arena y `#21261F` sobre
  la sombra).
- **Filete doble arriba**: una línea **bronce** `#9A804A` (medida entre
  `#8F763D` y `#9D8352`) y otra más clara encima.
- **Pestaña con el nombre** a la izquierda, **encima** de la banda, con el
  extremo derecho redondeado, del mismo gris translúcido. El nombre, en
  blanco.
- **Texto blanco**, alineado a la izquierda, letra redondeada y **muy
  espaciada**.
- En la esquina de arriba, **la cara de Naruto en un círculo** con su
  barra de vida cian; abajo a la derecha, **un mapa redondo** como una
  brújula.

| Juego | Cómo cuenta la historia | Estado |
|---|---|---|
| ***Naruto: Ultimate Ninja*** (PS2) | Diálogos **en formato manga** | ✅ (Wikipedia, por resumen) |
| ***Ultimate Ninja Storm*** (2008) | La banda descrita arriba en la aldea; escenas animadas en los combates | ✅ medido |
| ***Storm*** (versión de depuración de Steam) | Trae modos escondidos: una **carrera de trepar árboles** («Kinobori Race») con **tres niveles, «Newbie», «Medium» y «Superior Training»**, y **un escenario de prueba llamado «AREA_TEST_TRAINING»**. Uno de los escenarios de combate es el **«Survival Exercise Ground»** (el campo de los cascabeles) | ✅ [The Cutting Room Floor, vía Wayback](https://web.archive.org/web/2024/https://tcrf.net/Naruto:_Ultimate_Ninja_Storm) |
| ***Storm Connections*** (2023), **Modo Historia** | **Diapositivas fijas con frases dobladas** y los jefes de los juegos anteriores | ✅ ([MP1st](https://mp1st.com/reviews/naruto-x-boruto-ultimate-ninja-storm-connections-review-visiting-the-past), [TheGamer](https://www.thegamer.com/naruto-x-boruto-ultimate-ninja-storm-connections-review/)) |
| ***Naruto Mobile*** (Tencent, China) | **Cada arco de la historia es un pergamino** (卷轴) que se abre | ✅ ([GameRes](https://www.gameres.com/492012.html), [18touch](https://www.18touch.com/hyrz10221.html)) |
| *Storm 4*, rediseño de interfaz | Portafolio de **Grégory Cohen** en Behance | [Behance](https://www.behance.net/gallery/177904985/Naruto-Shippuden-ultimate-ninja-storm-4-UXUI-Design) (no lo abrí) |

**Conclusión**: Naruto tiene **dos «cuadros» propios**. En la serie, **el
pergamino** (misiones, exámenes, invocaciones; el móvil de Tencent ordena la
historia en pergaminos). En el juego más famoso, **la banda translúcida con
filete de bronce y pestaña de nombre**. Los dos sirven; ninguno es una
burbuja blanca.

### 7.4 Cómo se traduce a una lámina fija

- **El texto informativo** va en **un pergamino** colgado del poste, o en
  **una tablilla de madera** (como las del Ichiraku), con **pincel**.
- **La frase del personaje** va **escrita a pincel** en una tira de papel
  (como un sello o talismán) pegada al objeto, o sin globo, **junto a su
  cara, entre « »**.
- **El número del reto** va como **rango de misión**: una letra grande
  (D, C, B, A, S) en un sello rojo.

### 7.5 Qué NO hacer con el texto

- **Nada de burbuja blanca redonda** flotando.
- **Nada de kanji inventados**: si se pone japonés, que sea **una palabra
  de la serie** con su sentido (鈴 cascabel, 任務 misión, 合格 aprobado, 忍
  ninja, 木ノ葉 Konoha). Un fan japonés o latino **nota el kanji falso**.
- **No escribir «Believe it!»**: en latino es «**¡De veras!**» ✅.
- **No usar Ninja Naruto con tildes**: no las tiene y saldría «RETO DE LA
  SEMANA» bien, pero «¡Así se entrega!» saldría roto.

---

## 8 · Los personajes

Orden: primero los del encargo, luego los secundarios que más quiere el
público. Lo que no lleva ✅ con minuto, imagen o fuente es **de memoria** ⚠️.
Los colores, en §5.3 (medidos).

### Naruto Uzumaki — el protagonista (6.º en NARUTOP99)

- **Aspecto**: pelo **amarillo limón en pinchos**, ojos azules, **tres
  marcas de bigote** en cada mejilla, bandana de Konoha. **Chándal naranja
  con hombros azul marino** y cuello blanco (parte 1); en Shippuden,
  naranja y **negro** ✅ (hojas, n.º 492 y 1).
- **Historia**: huérfano. Lleva **sellado dentro al zorro de nueve colas**
  (la leyenda abre el N001, 00:00:04 ✅). El pueblo lo evita: hay **una
  norma que nadie le cuenta** (N001, 00:11:58 a 00:12:17 ✅).
- **Qué le importa**: que **lo reconozcan**. «**Voy a superar al Hokage y
  a hacer que todo el pueblo reconozca que existo**» (N004, 00:04:23 a
  00:04:27 ✅).
- **Qué le gusta**: «**El ramen de Ichiraku que me invita Iruka-sensei**».
  Afición: **comparar sopas instantáneas** (N004, 00:04:12 a 00:04:20 ✅).
- **Cómo habla**: termina las frases en «**dattebayo**» (だってばよ, **993
  veces** en los subtítulos ✅) → en latino «**¡De veras!**» ✅. Grita,
  presume («**el que será Hokage**», いずれ木ノ葉隠れの火影になる男, N008,
  00:12:46 ✅), se ríe de pillo ⚠️. Se presenta a gritos con **su nombre
  completo** (N025, 00:08:57 ✅).
- **Cómo se enfada**: aprieta los puños y **no se rinde**: «¡No me
  subestimes! ¡Yo no huyo!» (N025, 00:10:45-00:11:03 ✅), **sentado, con
  el puño en alto y sudando**, no de pie ([fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20025.mp4?t=648)).
- **Cuerpo**: **pulgar arriba** (n.º 156 ✅), **puño adelante** (n.º 329
  ✅), **manos cruzadas en el sello de los clones** (N001, 00:18:56 ✅),
  **correr con los brazos atrás** («Naruto run», meme ✅ §14). Las manos
  detrás de la cabeza ⚠️.
- **Con quién**: Iruka (el primero que lo reconoce), Sasuke (rival y
  hermano), Sakura, Kakashi, Jiraiya.

### Sasuke Uchiha — el rival (8.º en NARUTOP99; 1.º en dos encuestas de la Jump)

- **Aspecto**: pelo negro azulado en punta atrás, **camiseta azul oscura
  de cuello alto** con el **abanico Uchiha** en la espalda, pantalón claro
  (parte 1) ✅ (n.º 512, 522). En Shippuden, **camisa blanca abierta** y
  **cuerda morada** a la cintura ✅ (n.º 2, 511).
- **Historia**: el último de su clan. **Su hermano Itachi mató a todos**.
- **Se presenta así**: «Me llamo Sasuke Uchiha. **No hay nada que me
  guste**. Tengo una ambición: **restaurar mi clan y matar a cierto
  hombre**» (N004, 00:05:12 a 00:05:32 ✅).
- **Cómo habla**: poco. «Hmph» (フン). A Naruto lo llama
  «**usuratonkachi**» (ウスラトンカチ, 18 veces en Naruto ✅) → en latino
  sobre todo «**cabeza hueca**», también «perdedor» o «inútil» ✅ (Doblaje
  Wiki).
- **Lo que se olvida**: en la prueba de los cascabeles **es el primero que
  comparte su comida** con Naruto (N005, 00:17:40 ✅). En Reddit, «**qué
  amable era Sasuke de genin**» tiene **2.506 votos** (r/Naruto, 25 de
  octubre de 2025) ✅.
- **Cuerpo**: manos en los bolsillos, mirada de lado ⚠️; **codos en las
  rodillas y manos juntas delante de la boca** en la azotea ⚠️.

### Sakura Haruno — la compañera (3.º en NARUTOP99)

- **Aspecto**: **pelo rosa** (`#EBB8BE` medido), **ojos verdes**, frente
  ancha, **vestido rojo** tipo qipao con el círculo blanco del clan en la
  espalda ✅ (n.º 495, 57).
- **Carácter**: lista y estudiosa: en el examen **sabe que acertaría la
  10.ª** (N025, 00:07:45 ✅). Enamorada de Sasuke: dice «**Sasuke-kun**»
  **191 veces** en Naruto ✅.
- **Se presenta así**: lo que le gusta… **mira a Sasuke y chilla**. Lo que
  no le gusta: «**Naruto**» (N004, 00:04:42 a 00:05:02 ✅).
- **La Sakura interior**: la que grita lo que ella calla: «**¡Shannaro!**»
  (しゃーんなろ！) ✅ → en latino «**¡Cha!**» ✅. Se dibuja como **una
  silueta de línea blanca sobre negro**, con ojos brillantes y el puño en
  alto ✅ (n.º 232).
- **Después**: ninja médica y **fuerza bestial** ⚠️ (de memoria). Es la
  mujer mejor situada en NARUTOP99 ✅.

### Kakashi Hatake — el maestro (5.º en NARUTOP99; 1.º en la 1.ª y la 3.ª de la Jump)

- **Aspecto**: **pelo plateado** (`#D3D6DE`) de punta hacia un lado,
  **máscara** que tapa media cara, **bandana caída sobre el ojo izquierdo**
  (el del Sharingan), **chaleco verde grisáceo** (`#778372`) ✅ (n.º 498).
- **Se presenta así**: «Me llamo Kakashi Hatake. **No tengo ganas de
  contarles lo que me gusta** ni lo que no. ¿Mi sueño? Pues… Aficiones,
  varias». Sakura: «**Al final sólo sabemos su nombre**» (N004, 00:03:40 a
  00:03:58 ✅).
- **Manías**:
  - **Llega tarde** con excusas absurdas: «**Se me cruzó un gato negro**»
    (N004, 00:08:47 ✅), «**Hoy me perdí**» (N020, 00:03:46 ✅), «**Hoy me
    perdí un poco en el camino de la vida**» (N021, 00:08:19 ✅).
  - **Lee *Icha Icha Paradise*** en cualquier momento (N005, 00:05:54 ✅;
    n.º 461 ✅). Es su novela favorita ✅ ([Narutopedia](https://naruto.fandom.com/wiki/Icha_Icha)).
  - Empieza frases con «**Bueno…**» (まっ, 695 veces en los subtítulos de
    Naruto, aunque no todas son suyas ✅).
- **Qué le importa**: **los compañeros**. Pasa horas ante la piedra donde
  está el nombre de **su mejor amigo** (N005, 00:16:09 ✅; Obito, según
  [Narutopedia](https://naruto.fandom.com/wiki/Memorial_Stone) ✅).
- **Cómo enseña**: pone una trampa y **deja que se equivoquen** antes de
  explicar (N005 entero ✅). Luego lo dice claro y serio.
- **Su voz latina** (Alfonso Obregón) **no quería hacer la prueba**
  porque no le gusta el anime; **esa apatía fue la razón** de que lo
  eligieran ✅ (Doblaje Wiki, «Datos de interés»).
- **Final**: **Sexto Hokage** (S479, 00:07:56 ✅; n.º 49, 52). Su cara sin
  máscara se ve en S469 ✅ (n.º 37).

### Jiraiya — el maestro pervertido y escritor

- **Aspecto**: **pelo blanco larguísimo en pinchos**, líneas rojas bajo los
  ojos, chapa con el kanji **油** («aceite») y cuernos, **haori rojo vino**
  (`#902D43`) con círculos, sandalias de madera altas ✅ (n.º 458, 518).
- **Se presenta** con una **pose de kabuki** sobre un sapo: «**¡Bien
  preguntado! El espíritu sapo del monte Myōboku… el Sabio de los
  Sapos!**» (N053, 00:02:06 a 00:02:09 ✅; n.º 399 ✅).
- **Es escritor**: la saga *Icha Icha* ✅ y su primer libro, el que dio
  nombre a Naruto ✅ (§2.5). «Investiga» **espiando baños** ✅
  ([Narutopedia](https://naruto.fandom.com/wiki/Icha_Icha); n.º 113).
- **Como maestro**: enseña el **Rasengan por fases** (N086-N087 ✅).
- **Muere** luchando contra Pain y deja **un mensaje cifrado** en la
  espalda de un sapo (S133 ✅; n.º 108). Sus últimos pensamientos son **el
  título de la continuación de su libro** (S133, 00:19:20 a 00:19:31 ✅).
- En Reddit, **«¿Quién es mejor padre para Naruto: Iruka, Jiraiya o
  Kakashi?»** tiene **1.532 votos** (31 de julio de 2026) ✅.

### Itachi Uchiha — el hermano (2.º en NARUTOP99)

- **Aspecto**: pelo negro largo atado, **ojeras marcadas**, **capa negra
  de Akatsuki con nubes rojas**, bandana **tachada** ✅ (n.º 486, 526).
- **Gesto que todo el mundo conoce**: **toca la frente de Sasuke con dos
  dedos**: «**Perdóname, Sasuke. Otro día será**» (許せ サスケ また今度だ,
  N084, 00:03:17; S135, 00:01:10 ✅; n.º 265 ✅). ⚠️ En la copia latina de
  Internet Archive, S135 a 00:01:10 muestra a **Sasuke niño llorando en el
  bosque**: el minuto puede moverse en otras copias. En latino, «**otro día
  será**» u «**otra vez será**» ✅ (Doblaje Wiki).
- Lo que dice como villano: «**Hermanito estúpido**» (愚かなる弟よ, N084,
  00:10:31 ✅), «**Ódiame**» (恨め 憎め, N084, 00:14:41 ✅).
- **La verdad** sale en S141 ✅ y se despide en S339: «**Pase lo que pase,
  siempre te querré**» (00:20:49 a 00:20:55 ✅).
- **Cuidado**: es un personaje **trágico y serio**. No sirve para chistes
  ni para un tono alegre.

### Iruka Umino — el profe de la Academia (el secundario escondido)

- **Top 5 en seis de las siete encuestas de la Jump** ✅
  ([Narutopedia](https://naruto.fandom.com/wiki/Naruto_Character_Popularity_Polls)).
- **Aspecto**: coleta alta, **cicatriz sobre la nariz**, chaleco de chūnin
  verde grisáceo `#8F9B7B` ✅ (medido en la segunda pasada); *render* de cuerpo entero **con una carpeta** ✅ (n.º 525).
- Es **el primero que reconoce a Naruto**: le da **su propia bandana**
  (N001, 00:20:41 ✅) y lo invita a ramen.
- En la **mesa de misiones** reparte encargos y regaña (N006, 00:03:50 ✅).
- En latino grita «**¡Tatatá!**», como el Profesor Jirafales (ep. 88) ✅
  (Doblaje Wiki).

### La cara en cada emoción, con fotograma (segunda pasada)

Mirado con `fotogramas.py --cortes` en dos clips de Dailymotion (YouTube
pedía iniciar sesión). El minuto es el del clip.

| Quién | Emoción | Cómo es la cara | Dónde |
|---|---|---|---|
| Naruto | **Alegría pilla, presunción** | Se ríe de pillo, **señala con el dedo**, orgulloso de su broma | [«Naruto doing sexy no jutsu!»](https://www.dailymotion.com/video/xsn027), 0:19-0:21 ✅ |
| Naruto | **Rabia contenida**, a punto de llorar | Primer plano: **ojos muy abiertos, cejas apretadas** | [«Jiraiya is dead»](https://www.dailymotion.com/video/x2f7ri8), 1:14 ✅ |
| Naruto | **Tristeza que se vuelve grito** | **Boca abierta, cejas caídas hacia dentro**: «¡¿Por qué dejaste que hiciera algo tan arriesgado?!» | mismo clip, 1:17-1:24 ✅ |
| Naruto | Duelo a solas | Llora con Iruka | mismo clip, 2:38 ✅ |
| Tsunade | **Tristeza contenida** | **Labios apretados, mirada baja, manos entrelazadas tapando la boca** | mismo clip, 0:24 y 1:20 ✅ |
| Naruto | **Reto aceptado** | Sentado, **puño en alto**, sudor, ceño fruncido | N025, 00:10:48 ([fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20025.mp4?t=648)) ✅ |
| Sasuke, Sakura, Kakashi | Serio «hmph», la Sakura interior, ojo caído aburrido | ver arriba | hojas n.º 232, 461, 498 ✅ |

**Falta** ⚠️: el **miedo** y la **vergüenza** de Naruto con fotograma
propio, y las caras de Itachi y Jiraiya en escena (búsquedas «naruto
miedo», «naruto avergonzado» en Dailymotion, sin un primer plano claro).

### Los secundarios que conviene tener a mano

| Personaje | Por qué | Dato |
|---|---|---|
| **Minato Namikaze** | **1.º en NARUTOP99**, con 792.257 votos ✅ | Padre de Naruto; eligió su nombre del libro de Jiraiya (S133 ✅) |
| **Shikamaru Nara** | Top 5 en tres encuestas de la Jump ✅ | «**Qué fastidio**» (めんどくせえ) ✅ |
| **Rock Lee y Gai** | El esfuerzo | «¡La **juventud**!» (青春, N022, 00:14:18 ✅) |
| **Gaara** | En latino lo dobla **el director, Eduardo Garza** ✅ (Doblaje Wiki) | |
| **Hinata Hyūga** | 10.ª en NARUTOP99 ✅ | «Naruto-kun» (N001, 00:03:12 ✅) |
| **Teuchi** (Ichiraku) | El cocinero del ramen | En latino, Alfonso Mellado y luego Alejandro Villeli ✅ (Doblaje Wiki) |
| **Ibiki Morino** | El examinador del chūnin | «**Este año, la regla soy yo**» (N025, 00:06:22 ✅); en latino **Carlos Segundo** ✅ (Doblaje Wiki) |

---

## 9 · ¿Quién es el más querido?

### 9.1 La encuesta mundial oficial NARUTOP99 (2022-2023) ✅

Del 17 de diciembre de 2022 al 31 de enero de 2023; **unos 4,6 millones
de votos**; **Kishimoto dibujó a los 22 primeros** y un **manga corto de
Minato** ✅ ([web oficial](https://naruto-official.com/en/news/01_1468),
[Oricon](https://www.oricon.co.jp/news/2275377/full/),
[Mantan](https://mantan-web.jp/article/20230413dog00m200039000c.html),
[Hypebeast Corea](https://hypebeast.kr/2023/4/results-announcement-for-narutop99-worldwide-character-popularity-vote)).

| Puesto | Personaje |
|---|---|
| 1 | **Minato Namikaze** (792.257 votos, 1.º en todas las regiones y edades) |
| 2 | **Itachi Uchiha** |
| 3 | **Sakura Haruno** (subida de última hora) |
| 4 | Shisui Uchiha |
| 5 | **Kakashi Hatake** |
| 6 | Naruto Uzumaki |
| 7 | Sakumo Hatake ⚠️ (una fuente) |
| 8 | Sasuke Uchiha |
| 9 | Madara Uchiha |
| 10 | Hinata Hyūga |

### 9.2 Las encuestas de la Weekly Shōnen Jump

Según [Narutopedia](https://naruto.fandom.com/wiki/Naruto_Character_Popularity_Polls)
(una fuente para el detalle ⚠️). La 7.ª (Naruto 6.880 votos, Sasuke 5.791,
Kakashi 4.828) la confirma también [Setochan](https://setochan.net/blog-20211013/) ✅:

| Encuesta | 1.º | 2.º | 3.º | 4.º | 5.º |
|---|---|---|---|---|---|
| 1.ª | **Kakashi** | Naruto | Sasuke | **Iruka** | Sakura |
| 2.ª | Naruto | Kakashi | **Iruka** | Sasuke | Rock Lee |
| 3.ª | **Kakashi** | Naruto | **Iruka** | Sasuke | Shikamaru |
| 4.ª | Naruto | Kakashi | Sasuke | Shikamaru | **Iruka** |
| 5.ª | Sasuke | Naruto | Kakashi | **Iruka** | Shikamaru |
| 6.ª | Sasuke | Kakashi | Deidara | Naruto | **Iruka** |
| 7.ª (2011) | Naruto | Sasuke | Kakashi | Gaara | Itachi |

### 9.3 Lo que sale de todo esto

- **Kakashi** es el único que está **siempre** entre los cinco primeros:
  en la Jump (1.º dos veces) y en NARUTOP99 (5.º). **Es la apuesta más
  segura** para una lámina.
- **Iruka**, el profe, fue **top 5 en seis encuestas**: el público quiere
  al maestro que cree en el alumno. Encaja con un canal donde la gente
  **aprende y entrega**.
- **Itachi y Minato** ganan hoy, pero son **trágicos**: sirven para un
  tono serio, no para un canal de retos alegre.
- **Naruto** nunca baja del top 6, pero **no es el más votado**.

---

## 10 · Doblaje latino

### 10.1 La producción ✅

| Dato | *Naruto* (2002, 220 ep.) | *Shippuden* temporadas 1-5 (ep. 1-112) | *Shippuden* temporadas 6-22 (ep. 113-500) |
|---|---|---|---|
| Estudio | **Art Sound México** | **Art Sound México** | **Labo** |
| Dirección | **Eduardo Garza** | Eduardo Garza | Eduardo Garza; **Jorge Roig Jr.** (ep. 298-500, con Garza en la dirección creativa); sustitutos **Pepe Vilchis** y **Alfonso Obregón** en algunos episodios |
| Traducción y adaptación | Eduardo Garza | Eduardo Garza | Eduardo Garza; **Jennifer Medel** (ep. 298-500) |
| Grabación | **4 de enero de 2006 a 25 de junio de 2010** | agosto de 2013 y julio de 2014 a febrero de 2015 | **2023-2024** |
| Estreno | **Cartoon Network, 1 de enero de 2007** | 2015 | **Netflix, desde el 1 de octubre de 2024**; completo en **febrero de 2026** |
| Base | Guiones de **VIZ Media** (inglés) | original japonés | guiones de VIZ |

Fuentes: Doblaje Wiki por su API ([Naruto](https://doblaje.fandom.com/es/wiki/Naruto),
[Naruto Shippuden](https://doblaje.fandom.com/es/wiki/Naruto_Shippuden)),
[ANMTV (2024)](https://www.anmtvla.com/2024/09/naruto-shippuden-primera-tanda-de.html),
[ANMTV (febrero de 2026)](https://www.anmtvla.com/2026/02/naruto-shippuden-netflix-dispone.html),
[El Comercio](https://elcomercio.pe/saltar-intro/netflix/series/naruto-shippuden-doblaje-nuevos-episodios-llegan-a-netflix-en-ano-nuevo-noticia/),
[FUNiAnime](https://funianime.com/lo-que-debes-saber-sobre-el-regreso-del-doblaje-de-naruto-shippuden/).
Ojo: un artículo de ANMTV de 2021 dice que **todo** se dobló en Labo; la
ficha técnica de Doblaje Wiki lo separa como arriba ⚠️.

### 10.2 Las voces (cada nombre con dos fuentes) ✅

| Personaje | Voz latina | Fuentes |
|---|---|---|
| **Naruto** | **Isabel Martiñón** (todas las etapas; también su «técnica sexy») | Doblaje Wiki; [Senpai](https://senpai.com.mx/noticias/anime/naruto-quienes-hacen-doblaje-latino-serie/); [El Retake](https://www.youtube.com/watch?v=LO5_NaIYYhc) |
| **Sasuke** | **Víctor Ugarte** | Doblaje Wiki; [ANMTV (2021)](https://www.anmtvla.com/2021/12/naruto-shippuden-revelados-mas-actores.html); [El Comercio](https://elcomercio.pe/saltar-intro/netflix/series/naruto-shippuden-doblaje-nuevos-episodios-llegan-a-netflix-en-ano-nuevo-noticia/) |
| **Sakura** | **Christine Byrd** (Naruto y Shippuden 1-5); **Montserrat Aguilar** (Shippuden 6-22), porque Byrd **se retiró en 2016** | Doblaje Wiki; [3DJuegos](https://www.3djuegos.lat/anime/naruto-que-paso-christine-byrd-actriz-que-hizo-primer-doblaje-sakura-latinoamerica) |
| **Kakashi** | **Alfonso Obregón** (hasta el ep. 433 de Shippuden); **Óscar López** (ep. 440-500) | Doblaje Wiki; [SDV, TikTok «Reto de doblaje n.º 1041»](https://www.tiktok.com/@sdv_serviciosdevoz/video/7266928255179951365); [Mangaka Store](https://mangakastore.cl/blog/audio-de-naruto-shippuden-en-latino) |
| **Jiraiya** | **Paco Mauri** | Doblaje Wiki; [Cracken Shop, TikTok](https://www.tiktok.com/@crackenshopmex/video/7364625591934487828); [La Mole](https://lamole.com.mx/expositores/paco-mauri/) |
| **Itachi** | **Héctor Emmanuel Gómez** | Doblaje Wiki; [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Creator/HectorEmmanuelGomez); [SDV «Reto n.º 252»](https://www.tiktok.com/@sdv_serviciosdevoz/video/7080604336459418886) |
| **Iruka** | **José Antonio Macías** (Naruto); **Arturo Cataño** (Shippuden, desde el ep. 1) | Doblaje Wiki; [Fandoblaje Wiki](https://fandoblaje.fandom.com/es/wiki/Arturo_Cata%C3%B1o) ✅ (Cataño; Macías sigue con una fuente ⚠️) |
| **Hinata** | **Alondra Hidalgo** | Doblaje Wiki; ANMTV (2021) |
| **Gaara** | **Eduardo Garza** (el director) | Doblaje Wiki; [AniList](https://anilist.co/anime/20/Naruto/characters) ✅ |
| **Minato** | **Edson Matus** (desde 2021; en *Ultimate Ninja Storm 4* fue Gabriel Ortiz) | Doblaje Wiki; [ANMTV (6-dic-2021)](https://www.anmtvla.com/2021/12/naruto-shippuden-revelados-mas-actores.html) ✅ |
| **Tsunade** | **Dulce Guerrero** | Doblaje Wiki; [AniList](https://anilist.co/anime/20/Naruto/characters) ✅ |
| **Shikamaru** | **Javier Olguín** (hizo dos rondas de casting) | Doblaje Wiki; [AniList](https://anilist.co/anime/20/Naruto/characters) ✅ (en AniList su fila sale junto a Jorge Saudinós, la voz de Neji) |
| **Rock Lee** | **Carlos Díaz** | Doblaje Wiki; [AniList](https://anilist.co/anime/20/Naruto/characters) ✅ |
| **Ibiki** | **Carlos Segundo** (Naruto, Shippuden y Boruto) | Doblaje Wiki; [daddyjim.ai](https://daddyjim.ai/naruto/voice-actor/carlos-segundo) ✅ |
| **Pain** | **Arturo Mercado Jr.** | Doblaje Wiki; [AniList](https://anilist.co/anime/20/Naruto/characters) ✅ |

### 10.3 Cómo se eligió cada voz (Doblaje Wiki, «Datos de interés») ✅

- Garza lo contó en el foro **Pikaflash** el **20 de noviembre de 2005**.
  La grabación empezó el **28 de noviembre de 2005**.
- **VIZ eligió a Isabel Martiñón el 8 de diciembre de 2005**, tras
  **probar a 18 actores y actrices**. Fue la voz **más parecida a Maile
  Flanagan** (la voz inglesa). Rossy Aguirre también hizo prueba.
- Isabel pasó **tres pruebas**. En la primera dijo: «**Dame tu mejor
  golpe, tonto, y yo te lo devolveré multiplicado por mil**» y «**Si te
  atreves a ponerle una mano a mi sensei, te mato**». Le pidieron **más
  energía** y luego **mejor risa**.
- **Alfonso Obregón** hizo la prueba de Kakashi **sin ganas**, y por eso lo
  eligieron.
- Para **Akatsuki**, Garza pidió a los fans que propusieran voces en redes
  ✅ ([ANMTV, 2009](https://www.anmtvla.com/2009/09/doblaje-de-naruto-se-anuncian-las-voces.html)).

### 10.4 Las frases propias del doblaje latino ✅

| Original | Latino | Fuente |
|---|---|---|
| だってばよ (*dattebayo*), Naruto | «**¡De veras!**». Garza lo había adaptado como «**¡Créelo!**» (del *Believe it!* inglés) y **se grabaron capítulos así**. Luego **un niño que le vendía algo en la calle le dijo «de veras»**, le dio unos 5 pesos y se quedó con la frase | Doblaje Wiki; [Entrevistadoz, «Lalo Garza: el origen del “de veras”»](https://www.youtube.com/watch?v=dWhSVlugklo) (2:01, 13-mar-2026); [El Siglo de Torreón](https://www.elsiglodetorreon.com.mx/noticia/2022/es-un-gusto-estar-en-la-laguna-de-veras-isabel-martinon-voz-de-naruto-en-su-visita-a-el-siglo.html) |
| しゃーんなろ, Sakura | «**¡Cha!**» (como en inglés) | Doblaje Wiki; guía de cuadros de diálogo del repositorio |
| めんどくせえ, Shikamaru | «**Qué fastidio**» o «**Qué molestia**» | Doblaje Wiki |
| ウスラトンカチ, Sasuke a Naruto | «**Cabeza hueca**», «perdedor», «inútil» | Doblaje Wiki |
| また今度だ, Itachi | «**Otro día será**» u «**otra vez será**» | Doblaje Wiki; TV Tropes («Perdóname, Sasuke») |
| (ep. 44, Naruto a Kiba) | «**Puedes olvidarte de ser Hokage, porque soy el más perrón aquí**». Del inglés *«I'm the top dog around here»*. Isabel lo dice en las convenciones | Doblaje Wiki; [Xataka México](https://www.xataka.com.mx/anime/frases-polemicas-queridas-doblaje-naruto-pocos-saben-que-decidieron-usarla) |
| 裏の裏を読むべし, Kakashi (ep. 5) | «**Un ninja debe ver a través de la decepción**». **Es un error**: el inglés decía *deception* («engaño») | Doblaje Wiki («Errores») ✅ |
| (ep. 88, Iruka) | «**¡Tatatá!**», guiño al Profesor Jirafales | Doblaje Wiki |
| (Sakura a Naruto) | «**¡Por favor, devuélveme a mi Sasuke!**» | Doblaje Wiki |
| (ep. 5, Kakashi) | «Quienes rompen las reglas son escoria, pero quienes abandonan a sus compañeros son peor que escoria» | ⚠️ versión que citan los fans ([Erikstore](https://blog.erikstore.com/frases-naruto-naruto-shippuden/)); **no la comprobé con el audio** |

**Otros detalles**: el doblaje **conserva «-sensei»** pero no «-kun» ni
«-chan»; «-sama» se traduce como «Lord» o «Lady» ✅. En la tele, los
**openings eran los de la versión de EE. UU.**; en Netflix, Max y Prime
Video están **los japoneses** ✅ (Doblaje Wiki).

### 10.5 Dónde ver y oír a los actores

| Vídeo | Qué es | Datos (yt-dlp) |
|---|---|---|
| [Isabel Martiñón en «El Retake» ep. 36](https://www.youtube.com/watch?v=LO5_NaIYYhc) | Entrevista larga: Naruto, Gumball, Ben 10, Marceline | **1:06:22**, 5-abr-2026, 56.298 visitas. Sin capítulos ni subtítulos: minuto sin comprobar ⚠️ |
| [Lalo Garza en «El Retake» ep. 35](https://www.youtube.com/watch?v=rHn4YzZIico) | El director | **1:23:05** |
| [«Lalo Garza: el origen del “de veras”»](https://www.youtube.com/watch?v=dWhSVlugklo) | **El corte que interesa**, en 2 minutos | **2:01**, 13-mar-2026 |
| [«La voz de Jiraiya»](https://www.youtube.com/watch?v=1ZraSF4wk2E) | Datos Geek | — |
| [«Entrevista a los actores de doblaje de Naruto», TeleGeek, parte 4](https://www.youtube.com/watch?v=n-UKuw84350) | Reparto | 7:49 |
| SDV «**Reto de doblaje**» [n.º 1041, Kakashi](https://www.tiktok.com/@sdv_serviciosdevoz/video/7266928255179951365) y [n.º 252, Itachi](https://www.tiktok.com/@sdv_serviciosdevoz/video/7080604336459418886) | Una cuenta de voces **reta a los fans a doblar la escena y compararse con la voz oficial** | **El formato exacto de #reto-de-la-semana** |

---

## 11 · Música

### 11.1 Openings y endings (lista de [Narutopedia](https://naruto.fandom.com/wiki/Music)) ✅

**Naruto** (openings japoneses): 1 «R★O★C★K★S» (Hound Dog, ep. 1-25) ·
2 «**Haruka Kanata**» (Asian Kung-Fu Generation, 26-53) · 3 «Kanashimi o
Yasashisa ni» (little by little, 54-77) · 4 «**GO!!!**» (FLOW, 78-103) ·
5 «Seishun Kyōsōkyoku» (Sambomaster, 104-128) · 6 «No Boy, No Cry» (Stance
Punks) · 7 «Namikaze Satellite» (Snorkel) · 8 «Re:member» (FLOW) · 9
«Yurayura» (Hearts Grow, 203-220).

**En la tele latina**, el primer opening **no fue «ROCKS»**: fue el de
EE. UU., «**Rise**» (Jeremy Sweet e Ian Nickus, ep. 1-52) ✅ (Narutopedia,
versión inglesa + Doblaje Wiki: la tele usó los temas de EE. UU.). Si se
quiere tocar la **nostalgia latina** de 2007, es ese. **Sonó cantado, en
inglés**, como en EE. UU.; su versión instrumental era el ending ✅
(segunda pasada: [Wikipedia, temporada 2](https://en.wikipedia.org/wiki/Naruto_season_2) y Doblaje Wiki).

**Endings de Naruto** que se recuerdan: 1 «**Wind**» (Akeboshi) · 13
«Yellow Moon» (Akeboshi) · 3 «Viva★Rock» (Orange Range) ✅. Ningún
ending está mirado en fotograma: el único clip largo que salía como
«ending», **«Naruto - Never Ending Spirit»** ([Dailymotion](https://www.dailymotion.com/video/x1fsiw), 5:28),
**es un AMV de fan** con marca «AnimeYT.tv» y el rótulo
「オープニングアニメーション」 pegado encima. **No lo cites como oficial.**

**Shippuden** (openings): 1 «Hero's Come Back!!» (nobodyknows+) · 3
«**Blue Bird**» (Ikimono-gakari, ep. 54-77) · 6 «Sign» (FLOW) · 16
«**Silhouette**» (KANA-BOON, 380-405) · 20 «Kara no Kokoro» (Anly, 480-500)
✅.

### 11.2 La banda sonora

- **Toshio Masuda** compuso la música de *Naruto*: «Naruto Main Theme»,
  «**The Raising Fighting Spirit**» ✅ ([Looper](https://www.looper.com/1233948/narutos-composer-was-careful-not-to-spoil-the-story-with-the-music/),
  [Wikipedia](https://en.wikipedia.org/wiki/Toshio_Masuda_(composer))).
- «**Sadness and Sorrow**» sale en los discos de Masuda, pero **lo
  escribió Yasuharu Takanashi**, que debutó ahí (lo hizo en dos horas y
  luego lo retocó) ✅ ([Japan Nakama](https://www.japannakama.co.uk/creativity/music/who-composed-sadness-and-sorrow-naruto/) + Wikipedia).
  Mezcla **shakuhachi y shamisen** con **piano y violín**. Takanashi compuso luego **toda la música de Shippuden** ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Yasuharu_Takanashi),
  [ANN, entrevista de 2021](https://www.animenewsnetwork.com/interview/2021-11-24/naruto-series-composer-yasuharu-takanashi/.179101)).
  Ganó el **premio internacional de JASRAC cinco veces** por Shippuden ✅.
- **El ambiente**: «**Sasuke's Theme**» usa **bajo, taiko, shakuhachi,
  platillos, claves, guitarra eléctrica y cascabeles** ✅
  ([Narutopedia ES](https://naruto.fandom.com/es/wiki/Sasuke's_Theme),
  [Anexo de Wikipedia](https://es.wikipedia.org/wiki/Anexo:Banda_sonora_de_Naruto)).
  Takanashi (Shippuden) tira de orquesta, coros e instrumentos japoneses;
  Masuda, más de sintetizador ⚠️ ([dodmagazine.es](https://www.dodmagazine.es/bandas-sonoras-naruto/), una fuente). «The Raising Fighting Spirit» es **el
  tema de «ahora va en serio»**; «Sadness and Sorrow», el de la tristeza.

### 11.3 Qué música pega a cada lámina

| Lámina | Tema |
|---|---|
| Reto (cascabeles, examen) | «**The Raising Fighting Spirit**» (tensión con humor) |
| Ramen, charla | «Naruto Main Theme» ⚠️ |
| Jiraiya, libro | «Jiraiya no Theme» (2:43) ⚠️: el título existe en el [Anexo de Wikipedia](https://es.wikipedia.org/wiki/Anexo:Banda_sonora_de_Naruto), pero no en las 21 pistas del OST vol. I de MusicBrainz |
| Algo triste, despedida | «**Sadness and Sorrow**» |
| Tensión seria, rival | «**Sasuke's Theme**» |

---

## 12 · Vídeos

| Vídeo | Canal | Datos (yt-dlp u oEmbed) | Qué sirve |
|---|---|---|---|
| [**«ROAD OF NARUTO»**, PV del 20 aniversario](https://www.youtube.com/watch?v=yKELA1qBAKA) | スタジオぴえろ【公式】 | 9:57 · 3-oct-2022 · **30,4 millones** de visitas | **Fotogramas nuevos en alta** de las escenas famosas, con el equipo que dibuja hoy |
| [«ROAD OF NARUTO», tráiler de VIZ](https://www.youtube.com/watch?v=QczGoCmX-pI) | vizmedia | oEmbed | Versión occidental |
| [Aviso del libro de dibujos originales del PV](https://www.youtube.com/watch?v=okzWxkX0lK4) | スタジオぴえろ【公式】 | 0:31 | Existe un **artbook de ROAD OF NARUTO** |
| [«KAKASHI pone a prueba al EQUIPO 7», latino](https://www.youtube.com/watch?v=Yd08oqnpsKY) | Tu Rincón Del Hobby (fan) | 10:26 | **La escena de los cascabeles doblada** (subida por un fan ⚠️) |
| [«KAKASHI conoce al equipo 7», latino](https://www.youtube.com/watch?v=7A0yY9_OSWs) | Tu Rincón Del Hobby (fan) | 2:52 | La azotea (N004) |
| [*Storm*: diálogos de todos los aldeanos](https://www.youtube.com/watch?v=kkVhqfzWWIE) | RuNix | 7:53, con capítulos | **La caja de diálogo del juego** (§7.3) |
| [Isabel Martiñón en El Retake](https://www.youtube.com/watch?v=LO5_NaIYYhc) | El Retake | 1:06:22 | La voz de Naruto |
| [Lalo Garza, el origen del «de veras»](https://www.youtube.com/watch?v=dWhSVlugklo) | Entrevistadoz | 2:01 | La frase |

### 12.1 Mirado con fotogramas en la segunda pasada

| Vídeo | Minuto | Qué se ve | Sirve para |
|---|---|---|---|
| [Opening de Shippuden (Dailymotion, FILMSTARTS)](https://www.dailymotion.com/video/x88r3bd) | 0:08 | Siluetas del equipo 7 antes del amanecer | Encuadre de grupo a contraluz |
| ídem | **0:16** | **Logo «NARUTO -ナルト-»** en naranja y rosa | Color del logo en movimiento |
| ídem | 0:24 | Sakura y Sasuke ante la Roca Hokage | Fondo |
| ídem | 0:32 | Primer plano de Kakashi | Presentar |
| ídem | 1:12-1:28 | El equipo camina hacia un atardecer enorme | Cierre, paleta cálida |
| [«Naruto Tráiler VO» (Sensacine)](https://www.dailymotion.com/video/x8bc8i2) | 1:57 | Tráiler de cine en España de **una película**, sin identificar | ⚠️ no mirado a fondo |
| [«Never Ending Spirit»](https://www.dailymotion.com/video/x1fsiw) | 5:28 | **AMV de fan**, no ending oficial | Descartado |

⚠️ El opening de Dailymotion no dice cuál es (el título del que lo sube no
lo precisa).

### 12.2 Tendencia de TikTok: el «hand seal dance»

El **baile de sellos de mano** se hizo viral con «**Silhouette**»
(KANA-BOON, opening 16 de Shippuden, ep. 380-405). La propia banda lanzó
**#silhouettetogether** pidiendo covers y el tema llegó a lo más alto de
las listas de TikTok Japón; hay versiones con efecto de **clon de sombra** ✅
([TikTok](https://www.tiktok.com/@lento.lento/video/7538352262771395846),
[Wikipedia, «Silhouette»](https://en.wikipedia.org/wiki/Silhouette_(Kana-Boon_song))).
No hay una cifra fiable de vídeos ni vistas ⚠️. **Para #reto-de-la-semana
o un canal de canto es la mejor pieza nueva.**

**Por qué hay pocos minutos exactos de YouTube**: los vídeos consultados
**no tenían subtítulos** y YouTube bloqueaba las descargas («no soy un
robot»). **Los minutos exactos de las escenas están en §2**, sacados de los
subtítulos de los episodios.

---

## 13 · Videojuegos de la franquicia

| Juego | Año | Estudio | Para la lámina |
|---|---|---|---|
| *Naruto: Ultimate Ninja* (PS2) | 2003 | CyberConnect2 | Historia **en viñetas de manga** ✅ |
| ***Naruto: Ultimate Ninja Storm*** | 2008 | CyberConnect2 / Bandai Namco | **La caja de diálogo medida** (§7.3). Escenario «**Survival Exercise Ground**» (el de los cascabeles) y minijuego de **trepar árboles en tres niveles** ✅ (TCRF) |
| *Storm 2, 3, Revolution, 4* | 2010-2016 | CyberConnect2 | TCRF tiene páginas de [Storm 3](https://tcrf.net/Naruto_Shippuden:_Ultimate_Ninja_Storm_3) y [Storm 4](https://tcrf.net/Naruto_Shippuden:_Ultimate_Ninja_Storm_4) (no las abrí) |
| *Storm* en **Apple Arcade** | — | Bandai Namco | Versión móvil oficial ✅ ([web oficial](https://naruto-official.com/en/news/01_2472)) |
| ***Naruto x Boruto: Storm Connections*** | 2023 | CyberConnect2 | Modo Historia en **diapositivas con voces** ✅ |
| ***Naruto Mobile*** (火影忍者手游) | 2016 ⚠️ | Tencent | **Historia ordenada en pergaminos** ✅ |

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todos reconocen

| Qué | Por qué lo reconocen | Fuente |
|---|---|---|
| «**¡De veras!**» | La muletilla latina; Isabel la usa en cada convención | Doblaje Wiki ✅; [El Siglo](https://www.elsiglodedurango.com.mx/noticia/2022/es-un-gusto-estar-en-la-laguna-de-veras-isabel-martinon-voz-de-naruto-en-su-visita-a-el-siglo.html) ✅ |
| «**Yo soy el más perrón aquí**» | Frase latina del ep. 44; meme en TikTok | Doblaje Wiki ✅; [TikTok](https://www.tiktok.com/discover/naruto-diciendo-soy-el-m%C3%A1s-perr%C3%B3n-aqu%C3%AD) ✅ |
| **«Naruto run»** | Correr con los brazos atrás. El evento de broma del **Área 51** (2019) pedía correr así «para ir más rápido que las balas» | [Know Your Meme](https://amp.knowyourmeme.com/memes/naruto-run) ✅ |
| «**¡Sasukeee!**» / «**¡Narutooo!**» | Los gritos alargados del Valle del Fin; compilaciones en TikTok | [TikTok](https://www.tiktok.com/discover/narutooo-sasukeee-funny) ✅ |
| **El relleno** | Se burlan de los arcos de relleno (hay un meme propio) | [Know Your Meme, «Naruto Fillers»](https://knowyourmeme.com/memes/naruto-fillers) ✅ |
| **Kakashi leyendo *Icha Icha*** | El libro naranja en la mano en plena pelea | N005 ✅; n.º 461 ✅ |
| **El toque en la frente de Itachi** | Gesto de hermano mayor | N084 ✅; n.º 265 ✅ |
| **El sello de los clones** (dedos en cruz) | Todo el mundo lo imita | N001 ✅ |
| **La foto del equipo 7** | Kakashi sonriendo detrás, Naruto y Sasuke enfadados, Sakura feliz | n.º 522 ✅ |
| **El ramen de Ichiraku** | Naruto pide siempre lo mismo; Iruka paga | N001, N006 ✅ |
| **«Sasuke era amable de genin»** | Reddit lo celebra en 2025 (2.506 votos) | [r/Naruto](https://reddit.com/r/Naruto/comments/1ofvauk/rereading_part_1_and_realizing_how_kind_genin/) ✅ |
| **Kakashi casi usa una técnica gorda con los niños** en los cascabeles | Chiste de Reddit (3.015 votos, octubre de 2025) | [r/Naruto](https://reddit.com/r/Naruto/comments/1nysify/kakashi_in_the_anime_was_lowkey_about_to_drop/) ✅ |

### 14.2 Qué NO hacer (lo que un fan notaría)

- **Bandana con otro símbolo**: la de Konoha es **una hoja con espiral**
  (no un remolino suelto ni un kanji). Tachada = **renegado** (Itachi).
- **Kakashi sin máscara** en una lámina cualquiera: su cara sólo se ve en
  un episodio de broma (S469). Con máscara siempre.
- **Kakashi con los dos ojos iguales**: el izquierdo va **tapado por la
  bandana** (parte 1) ✅ (n.º 498).
- **Sharingan de Sasuke en la parte 1 con más de tres aspas**: el
  «caleidoscopio» es de Shippuden ⚠️.
- **Naruto en naranja y negro** si la escena es de la parte 1: entonces
  era **naranja y azul marino** (`#093C7D`, medido).
- **Pelo de Naruto dorado cálido**: en el anime de la parte 1 es **amarillo
  limón** (`#E1E11F`, medido).
- **Sakura vestida de Shippuden** en una escena del examen chūnin.
- **Clones idénticos copiados y pegados**: el equipo del anime cuenta que
  **cada clon mira hacia un lado distinto** ⚠️ ([GetNews, entrevista al
  staff](https://getnews.jp/archives/3378334)).
- **«Believe it!»** o «**¡Créelo!**» en vez de «**¡De veras!**» (el
  «Créelo» existió, pero se cambió en seguida ✅).
- **Itachi o Minato de broma**: son los más votados **porque son
  trágicos**.
- **Kanji inventados** o sellos de manos sin sentido.
- **Colores «oscuros» de moda** (negro y neón): Naruto es **cálido, verde y
  naranja**.

---

## 15 · Poses analizadas por personaje

«Minuto» = la frase está comprobada en el subtítulo; **la pose que se ve**
en ese minuto la describo de memoria ⚠️, salvo las que llevan enlace
`archive.org`: esas se **miraron en el fotograma** en la segunda pasada ✅. «N.º» = la imagen **la vi** en la
hoja ✅.

### Kakashi

| Dónde | Qué hace | Sirve para |
|---|---|---|
| **obj 13** ✅ | De pie, **levanta el puño derecho** con el cordel rojo y **dos cascabeles** colgando; mirada tranquila, bosque detrás | **Presentar el reto** |
| **n.º 461** ✅ | Sentado, **lee *Icha Icha*** con los ojos brillando, rayos de luz saliendo del libro | **Chiste**, «no se gana nada» |
| **n.º 413** ✅ | **Sostiene un papel arrugado delante de la cara**, ojos de aburrido, cielo azul | **Explicar** (con el papel en la mano) |
| **n.º 522** ✅ | Detrás del equipo, **las dos manos en las cabezas** de Naruto y Sasuke, ojo cerrado sonriendo | **Presentar al grupo** |
| **n.º 129** ✅ | De pie junto a Sasuke, hojas volando | Llegar |
| N004, 00:08:42 | «**Hola, chicos, buenos días**» (llega tarde, saluda con la mano ⚠️) | **Saludar** |
| N005, 00:13:07 | Regaña: «¿Tienen **pulpa de tofu** en el cerebro?» (お前らの脳みそは オカラか？; brazos cruzados ⚠️) | **Regañar** |
| N005, 00:19:54 | «**¡A-pro-ba-dos!**»: **salta en el aire con los brazos cruzados** sobre el pecho, Sakura a su lado; **de noche, cielo morado** ([fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20005.mp4?t=1194)) ✅ | **Celebrar** |
| N005, 00:16:07 | Ante la piedra, **de espaldas, mano en el bolsillo**, atardecer naranja entre los árboles ([fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20005.mp4?t=967)) ✅ | **Pensar**, tono serio |

### Naruto

| Dónde | Qué hace | Sirve para |
|---|---|---|
| **n.º 156** ✅ | **Pulgar arriba**, sonrisa enorme con los ojos cerrados, fondo blanco luminoso | **Animar**, «¡tú puedes!» |
| **n.º 329** ✅ | **Puño adelante** hacia la cámara, sonrisa decidida, camino de tierra | **Empezar el reto** |
| **n.º 155** ✅ | **Palma abierta hacia la cámara** con el sello en espiral, cara pintada de kabuki | Chiste, **presentarse** |
| **n.º 492** ✅ | Primer plano, **sonrisa de medio lado**, bandana brillante | Cara de «acepto» |
| **n.º 470** ✅ | En el aula del examen, entre pupitres en gradas | **El examen** (Concepto B) |
| **n.º 105** ✅ | En la barra de Ichiraku, **palillos en la mano** | **Charlar** (Concepto C) |
| N025, 00:10:45-00:10:54 | **Sentado en su pupitre, brazo derecho en alto con el puño cerrado, sudando, ceño fruncido**: «¡Yo no huyo!» ([fotograma 10:48](https://archive.org/download/naruto-completo/Naruto%20-%20025.mp4?t=648)) ✅. No golpea la mesa ni se levanta | **Aceptar el reto sentado** (mesa de trabajo, pupitre) |
| N005, 00:21:15 | **Atado al tocón**, pataleando: «¡Desátenme!» | **Chiste**, primer plano |
| N001, 00:18:56 | **Dedos en cruz**, cientos de clones | **Celebrar / llenar** |

### Sakura

| Dónde | Qué hace | Sirve para |
|---|---|---|
| **n.º 57** ✅ | *Render*: **corre con un kunai** en la mano derecha, vestido rojo al viento | Acción |
| **n.º 495** ✅ | Primer plano, sonrisa amable | **Explicar**, cercana |
| **n.º 232** ✅ | **Su «yo interior»** en línea blanca sobre negro, puño en alto | **El pensamiento que grita** |
| **n.º 481** ✅ | En el examen, sentada, con el lápiz | **Pensar** |
| N004, 00:04:56 | Mira a Sasuke y **chilla** («¡Kyaa!») | Chiste |
| N005, 00:18:43 | Le da de comer a Naruto: «**Sólo por esta vez, ¿eh?**» | **Compartir**, regañar con cariño |

### Jiraiya

| Dónde | Qué hace | Sirve para |
|---|---|---|
| **n.º 399** ✅ | **Las dos manos abiertas** hacia delante, sonrisa enorme, campo gris | **Presentarse a lo grande** |
| **n.º 518** ✅ | *Render* de kabuki: **rodillas dobladas, un brazo estirado con la palma abierta**, pelo al viento | Recorte para una lámina |
| **n.º 458** ✅ | Primer plano, sonrisa pícara, chapa «油» | Cara |
| **n.º 113** ✅ | **Huye corriendo** tras espiar | Chiste |
| N053, 00:02:09 | Pose de kabuki **sobre un sapo** ⚠️ | Presentar |
| N086, 00:20:10-00:20:15 | Enseña el **globo de agua** en la palma hacia 20:10-20:13 ⚠️; a 20:15 es **un primer plano de su cara con el rasguño rojo, mirada de lado**, bosque detrás, sin manos ([fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20086.mp4?t=1215)) ✅ | **Explicar un ejercicio** |

### Itachi

| Dónde | Qué hace | Sirve para |
|---|---|---|
| **n.º 265** ✅ | **Dos dedos en la frente** de Sasuke niño, sonrisa suave | **Despedirse** («otro día será») |
| **n.º 486** ✅ | Primer plano ante el mar, mirada seria | Serio |
| **n.º 526** ✅ | *Render*: brazo extendido, túnica abierta | Recorte |
| N084, 00:10:31 | «Hermanito estúpido», de pie, inmóvil ⚠️ | Amenazar |
| S339, 00:20:49 | Se despide con la frente pegada a la de Sasuke ⚠️ | Emoción |

### Iruka

| Dónde | Qué hace | Sirve para |
|---|---|---|
| **n.º 525** ✅ | *Render*: **levanta un papelito** con la mano derecha y **sujeta una carpeta verde** con la izquierda | **Anunciar el reto** |
| N001, 00:20:40-00:20:41 | Le pone su bandana a Naruto (el gesto, un segundo antes); a 20:41, **primer plano de la bandana ya puesta** ([fotograma](https://archive.org/download/naruto-completo/Naruto%20-%20001.mp4?t=1241)) ✅ | **Felicitar** |
| N006, 00:03:49 | Grita «¡Idiota!» desde la mesa de misiones ⚠️ | **Regañar** |

### Resumen: qué pose para qué

| Para… | Mejor pose |
|---|---|
| **Presentar** | Kakashi con los cascabeles (obj 13) o Jiraiya en kabuki (n.º 399) |
| **Explicar** | Kakashi con el papel (n.º 413) o Iruka con la carpeta (n.º 525) |
| **Celebrar** | «¡Aprobados!» (N005, 00:19:54, Kakashi en el aire, de noche) o Naruto con el pulgar (n.º 156) |
| **Aceptar un reto** | Naruto sentado con el puño en alto (N025, 00:10:48) |
| **Regañar** | Kakashi, N005, 00:13:07; Iruka, N006 |
| **Pensar** | Kakashi ante la piedra (N005, 00:16:07) |
| **Animar** | Naruto puño adelante (n.º 329) |

---

## 16 · Vestuario

| Personaje | Traje icónico | Colores (medidos ✅ o ⚠️) | Accesorios |
|---|---|---|---|
| **Naruto** (parte 1) | **Chándal naranja** con hombros azul marino y cuello blanco; remolino en el hombro | naranja `#FE7A35`, azul `#093C7D` ✅ | Bandana azul, **gafas verdes** en la primera escena ⚠️, portakunais en el muslo |
| **Naruto** (Shippuden) | Chaqueta **naranja y negra** | negro ⚠️ | Bandana de tela **negra** ⚠️; **capa roja de sabio** en el arco de Pain (n.º 529 ✅) |
| **Naruto** (adulto) | **Capa de Hokage** blanca con llamas rojas y «七代目火影» | ✅ n.º 134, 554 | |
| **Sasuke** (parte 1) | Jersey **azul marino de cuello alto**, mangas remangadas, con el abanico Uchiha; pantalón corto blanco grisáceo | `#06406C`, sombra `#262E38` ✅ (medido en `Sasuke_Part_I.png`) | **Vendas blancas en las piernas y tobillos** (no en los brazos), sandalias azul marino, bandana de tela azul marino |
| **Sasuke** (Shippuden) | **Camisa blanca abierta**, **cuerda morada** gruesa a la cintura | ✅ n.º 2, 511 | Espada a la espalda |
| **Sakura** (parte 1) | **Vestido rojo** tipo qipao corto con cremallera, pantalón corto | vestido **`#85223F`** ✅ medido (antes `#C8283C` de memoria); a contraluz de atardecer `#9C2A38` (N005 16:07); pelo `#EBB8BE` / `#EABABE` ✅ | Bandana **como diadema** en el pelo |
| **Sakura** (adulta) | Kimono largo **rojo vino**, cuello alto con ribete gris, pelo corto | `#85223F` ✅ | Ojo: la wiki llama a ese archivo «Sakura_Part_1.png», pero el diseño es de adulta |
| **Kakashi** | Traje azul marino con **chaleco verde grisáceo** de jōnin | `#778372` ✅ | **Máscara**, bandana sobre el ojo izquierdo, *Icha Icha* |
| **Kakashi** (Hokage) | Sombrero y capa de Hokage «六代目火影» | ✅ n.º 49, 52 | |
| **Jiraiya** | Kimono corto verde, **haori rojo vino** con círculos | `#902D43` ✅ | Chapa «油» con cuernos, **pergamino enorme a la espalda**, geta |
| **Itachi** | **Capa de Akatsuki**: tela azul-negra con **nubes rojas** de borde hueso | tela `#2A2B33`; nube **`#58262D` / `#9B3E35`** según la luz; borde `#CFC3B7` ✅ medido en dos imágenes | Bandana con la raya, collar, anillo 朱 en el anular derecho ✅; uñas pintadas ⚠️ |
| **Iruka** | Chaleco de chūnin **verde grisáceo**, más claro que el de jōnin | `#8F9B7B`, sombra `#3F4843` ✅ medido | Coleta, cicatriz, carpeta |

**Lo icónico que todos reconocen**: el **chándal naranja** de Naruto, la
**máscara** de Kakashi, la **capa de Akatsuki**, el **haori rojo** de
Jiraiya y la **bandana** con la hoja.

---

## 17 · Paisajes y fondos de pantalla

### 17.1 Los sitios, con su luz (vistos en las hojas ✅)

| Sitio | Imagen | Luz y color |
|---|---|---|
| **Campo 3** desde arriba | obj 15 (1913×1080) | Mediodía, verde intenso (`#82C36B`), sombras cortas |
| **Campo 3** en «¡Aprobados!» | [fotograma N005 19:54](https://archive.org/download/naruto-completo/Naruto%20-%20005.mp4?t=1194) (1280×966) | **Noche, cielo morado con nubes** ✅ |
| **Campo 3** al atardecer | obj 39 (800×600) | Sol naranja bajo tras el bosque |
| **Piedra de los caídos** | obj 36 (1280×716) | Piedra negra pulida, luz filtrada de bosque |
| **Ichiraku** | obj 23 (1440×1080) | **Atardecer** naranja y malva, letrero blanco, farolillos |
| **Ichiraku nuevo** | obj 38 (1048×652) | Día, cielo azul, cables de luz |
| **Konoha** en panorámica | n.º 392 (1916×1077), n.º 414 | Tejados rojos y verdes, Roca de los Hokage detrás |
| **La Academia** | obj 1 (3840×2152) | Día, edificio rojo y crema, columpio ⚠️ |
| **Despacho del Hokage** | obj 8 (1920×1080) | Interior claro, pilas de papeles |
| **Valle del Fin** | n.º 437 (1915×1072) | Cascada entre dos estatuas, verde oscuro |
| **Roca de los Hokage** | n.º 13 (3840×2152) | 4K, época Boruto ⚠️ (siete caras) |

### 17.2 Fondos de pantalla

- **Oficiales**: la [ANIME GALLERY](https://naruto-official.com/special/anime-gallery)
  de la web oficial y la web del [20 aniversario](https://naruto-official.com/en/special/20th).
  La galería trae **20 key visuals** (2002-2017) pero **sólo en vista web,
  sin descarga ni tamaños** ✅ (comprobado en la segunda pasada).
- **Fotogramas 4K** de Narutopedia: n.º 13 (Roca, 3840×2152), obj 1
  (Academia, 3840×2152), obj 2 (bandana, 3821×2155), obj 3 (kunai,
  3826×2152) ✅ (tamaño de la API).
- **De fans**: el paisaje 3D **«Konoha Inspired Village»** de
  **Christoffer Radsby** en [ArtStation](https://www.artstation.com/artwork/rR0Be) ⚠️
  (tamaño sin comprobar).
- **De fans en Wallhaven** (tamaños de su API ✅): «Kyuubi/Madara»,
  **3840×2251**, ♥330, de *whendungeonarise*; **logo Uchiha minimalista**,
  1920×1080, ♥269, de *MegaRepoio21* (mejor como emblema que como
  paisaje); Sakura e Ino, **5684×3768**, ♥205, origen
  [x.com/limgae2726](https://x.com/limgae2726/status/1322580348769689600), pero es de la era Boruto ⚠️.
- **HDRI libres** para la luz: §5.4. No hay HDRI de «aldea ninja»: se usan
  los de naturaleza.

---

## 18 · Guía para generar con IA (Firefly, Canva)

**Regla del dueño**: «que no parezca hecho por IA». Por eso: **los
personajes, nunca con IA**. Se recortan de fotogramas reales (§3.0 y §15)
con `v3/integrar.py`. La IA sólo para **rellenar fondo o atrezo** que no
exista en ningún fotograma (un trozo de bosque, un tocón, papel).

### 18.1 Lo que no cambia nunca

- **Línea**: negra, **fina y limpia**, de grosor casi constante (anime de
  TV de 2002-2007, Studio Pierrot).
- **Sombreado**: **cel** de **dos tonos** (luz y una sombra de borde duro),
  sin degradados en la piel ni en la ropa.
- **Fondos**: **pintados a mano**, tipo gouache, **más suaves** que los
  personajes; bosques de manchas verdes, cielos limpios con nubes
  redondas.
- **Paleta**: la de §5.3 (medida). Verde de bosque `#48832F`, césped
  `#7DBF4E`, cielo `#609DE1`, naranja `#FE7A35`, azul marino `#093C7D`.
- **Luz**: **mediodía claro** en los exteriores del campo 3 durante el
  reto; **noche de cielo morado** en el «¡Aprobados!» (N005 19:54, mirado
  en fotograma); **atardecer naranja y malva** en Konoha e Ichiraku.

### 18.2 Palabras que ayudan (en inglés, que las entiende mejor)

`2000s TV anime background, hand-painted gouache, flat colors, soft
painted forest clearing, bright midday, clear blue sky with round white
clouds, Japanese wooden village, cel animation, clean thin lineart, Studio
Pierrot style background art`

### 18.3 Palabras que lo estropean

`photorealistic`, `3D render`, `octane`, `hyperdetailed`, `cinematic
lighting`, `neon`, `dark fantasy`, `glossy`, `bokeh` (el desenfoque se hace
luego, a mano), `ninja` a secas (sale un ninja genérico de película, no
Konoha).

### 18.4 Qué imágenes darle como referencia de estilo

| Para | Imagen |
|---|---|
| Bosque y claro del campo 3 | obj 15, obj 13 (el fondo detrás de Kakashi) |
| Atardecer | obj 39, obj 23 |
| Interior del aula | n.º 470, n.º 481 |
| Konoha | n.º 392, n.º 414 |

### 18.5 Encuadre

- **Plano medio** para hablar, **contrapicado suave** para presentar (el
  héroe «más alto»), **primer plano** del objeto en el borde del cuadro
  para dar profundidad.
- Nada de bustos cortados en recto flotando (regla del dueño): el
  personaje **toca** algo del escenario (el cordel, el pupitre, la barra).

### 18.6 Rasgos que la IA suele romper (y cómo pedirlos)

| Personaje | Nunca cambia | Palabras |
|---|---|---|
| Naruto (parte 1) | Pelo **amarillo limón** `#E1E11F` en pinchos, **tres marcas** por mejilla, chándal naranja `#FE7A35` con hombros azul marino `#093C7D` | `lemon yellow spiky hair, three whisker marks on each cheek, orange tracksuit with navy shoulders` |
| Sasuke (parte 1) | Jersey azul marino `#06406C` de cuello alto, **vendas en las piernas**, abanico Uchiha en la espalda | `navy high-collar shirt, white bandages on legs` |
| Sakura (parte 1) | Pelo rosa `#EBB8BE`, frente ancha, vestido qipao rojo `#85223F` | `pink hair, wide forehead, red qipao dress` |
| Kakashi | Máscara hasta la nariz, bandana sobre el ojo izquierdo, chaleco `#778372` | `face mask, headband over left eye, grey-green flak vest` |
| Akatsuki | Tela `#2A2B33`, **nubes rojas apagadas** `#9B3E35` con borde hueso | `muted maroon clouds with off-white outline`, nunca `bright red` |

La IA no puede con los **emblemas** (hoja de Konoha, abanico Uchiha,
remolino): se dibujan a mano encima (Punto 19).

### 18.7 Para una IA de texto: cómo escribir en su voz

**Reglas de estilo**:

- **Naruto**: frases cortas, exclamaciones, **«¡de veras!»** al final (en
  japonés *dattebayo*, 993 veces). Grita su nombre completo, promete
  («¡Seré Hokage!»), no se retracta. Nada de palabras técnicas.
- **Kakashi**: tranquilo, irónico, empieza con «**Bueno…**» (まっ), pone
  excusas absurdas, y **luego** dice lo importante en serio.
- **Sasuke**: muy poco, «**Hmph**», llama a Naruto «**cabeza hueca**».
- **Sakura**: educada por fuera; la **Sakura interior** grita «**¡Cha!**».
- **Jiraiya**: se presenta a lo grande, teatral, «**el Sabio de los
  Sapos**».
- **Itachi**: serio, pocas palabras, nunca chistes.
- **Puntuación**: «¡…!» abundante en Naruto; puntos suspensivos en Kakashi;
  frases secas con punto en Sasuke e Itachi.

**Frases reales por emoción** (del doblaje latino cuando se sabe; si no,
traducción de los subtítulos japoneses con su minuto, §2):

| Emoción | Frase | Quién, dónde |
|---|---|---|
| **Alegre / presumido** | «**Puedes olvidarte de ser Hokage, porque soy el más perrón aquí**» | Naruto, ep. 44, doblaje latino ✅ |
| Alegre | «**¡Todos los que quedan, aprobados!**» | Ibiki, N025 00:12:33 |
| Alegre | «**¡A-pro-ba-dos!**» | Kakashi, N005 00:19:54 |
| **Enfadado** | «**¡No me subestimes! ¡Yo no huyo! La haré**» | Naruto, N025 00:10:55 |
| Enfadado | «¿Tienen **pulpa de tofu** en el cerebro?» | Kakashi, N005 00:13:07 |
| Enfadado | «¡¿Por qué dejaste que hiciera algo tan arriesgado?!» | Naruto a Tsunade, S133 (clip, 1:17) |
| **Explicando** | «**La tarea de hoy: quitarme estos cascabeles antes del mediodía**. El que no lo logre, se queda sin almuerzo» | Kakashi, N004 00:09:05 |
| Explicando | «Los encargos se ordenan **por dificultad: A, B, C y D**» | N006 00:04:24 |
| Explicando | «**Esa pregunta nunca existió.** La elección era la 10.ª pregunta» | Ibiki, N025 00:12:52 |
| **Animando** | «**No me retracto de mis palabras. Ese es mi camino ninja**» | Naruto, N025 00:11:41 |
| Animando | «**Todo el mundo empieza por misiones fáciles y sube con la experiencia**» | Iruka, N006 00:03:50 |
| Animando | «Quienes rompen las reglas son escoria, pero quienes abandonan a sus compañeros son peor que escoria» | Kakashi, N005 00:20:19 |
| **Triste** | «**Perdóname, Sasuke. Otro día será**» | Itachi, N084 00:03:17 (latino «otro día será» ✅) |
| Triste | «**Pase lo que pase, siempre te querré**» | Itachi, S339 00:20:49 |
| Triste | «Aquí está grabado **el nombre de mi mejor amigo**» | Kakashi, N005 00:15:15 |

**Vocabulario de expresiones** (para que la IA de imagen entienda el
gesto): **gota de sudor** en la sien (vergüenza, «¿en serio?»), **vena**
en la frente (enfado cómico), **ojos en arco** (ojo sonriente de Kakashi),
**ojos en blanco con boca enorme** (grito cómico de Naruto), **la Sakura
interior** (silueta de línea blanca sobre negro con el puño en alto),
**versión *chibi*** con cabeza enorme para los chistes, **fondo de rayas
de velocidad** para gritos y sorpresas, **Sharingan** (ojos rojos con
comas) para el tono serio.

---

## 19 · Tres conceptos de lámina

**Canal propuesto**: **ıı・🎯・reto-de-la-semana** (§0). Los conceptos A y
B son para ese canal (se puede elegir uno; el otro sirve de lámina 2). El C
es para **#general-doblaje** (o la sala de voz 🍟 General), si el
coordinador del encargo 29 lo quiere.

Las frases «en la voz de la serie» son **traducción o adaptación mía** de
la frase japonesa del subtítulo (con su minuto), salvo las que marco como
**latinas** (comprobadas en Doblaje Wiki). Recortes siempre por
`v3/integrar.py` y comprobados a 1:1.

### Concepto A — «Los cascabeles de Kakashi» (#reto-de-la-semana)

- **Objeto y sitio**: **el campo de entrenamiento 3 a mediodía**. En primer
  plano, **los tres tocones en fila**; en el del medio, **un pergamino**
  clavado con un kunai. Sobre el tocón de la izquierda, **el despertador**
  marcando las 12. **Dos cascabeles plateados** cuelgan de un **cordel
  rojo** que cruza la imagen. Al fondo, desenfocada, **la piedra de los
  caídos** con forma de kunai.
  - En Blender: **Tree Stump 01/02** y **Alarm Clock 01** de Poly Haven
    (CC0), cordel con **Rope002** de ambientCG, papel con **Paper003**,
    cielo **Kloofendal 48d Partly Cloudy (Pure Sky)** y bosque de fondo
    pintado. Cascabeles: una esfera con ranura (o la forma del «Furin» de
    seirogan, CC BY).
- **Personaje**: **Kakashi**, el único que siempre está en el top 5 (§9).
  Pose: **obj 13** ✅, el **puño en alto con los cascabeles colgando**.
  El cordel de la foto **continúa** en el cordel 3D (así «toca» la escena).
  Detrás, pequeño y cómico, **Naruto atado al tocón** gritando «¡Desátenme!»
  (fotograma de N005, 00:21:15) ⚠️ opcional.
- **Cómo habla**: **sin globo**. Su frase va en **una tira de papel** (como
  un talismán) atada al cordel, a pincel (**Yuji Syuku**):
  **«Aquí, la regla soy yo»** (N005, 00:16:53 ✅, traducción mía).
- **Dónde va cada texto**:
  - **Pergamino**, arriba, en **Ninja Naruto** (no lleva tildes ✅):
    **RETO DE LA SEMANA**.
  - **Pergamino**, cuerpo, en **Shojumaru**, una idea por línea:
    **Un reto por semana** · **Una línea, una escena, un tono** · **Se
    entrega dentro del hilo del reto** (en la lámina, cada una en su
    renglón, sin «·»).
  - **Cascabel 1**, en una etiqueta colgante: **No se gana nada**.
  - **Cascabel 2**: **Esa es la gracia**. (Dos cascabeles, dos ideas: el
    fan lo entiende al instante.)
  - **Último renglón del pergamino**: el final de la descripción («es para
    grabar…») cuando se lea entero en Discord.
  - **El despertador, sin texto**: ya dice «hay un plazo».
- **Para que no quede plano**: **cascabeles grandes y nítidos en primer
  plano** con un brillo de sol; el **cordel cruza por delante** del brazo
  de Kakashi; **hojas cayendo** delante (como en el n.º 129); tocones con
  **sombras cortas y duras** de mediodía; piedra y bosque **desenfocados**
  al fondo.
- **Lámina 2 (las 8 etiquetas)**: **la mesa de misiones** del despacho del
  Hokage (obj 8 ✅; modelo «Hokage Room» de Jp André, CC BY). **Iruka**
  detrás, con la carpeta (n.º 525 ✅), dice en una tira de papel:
  **«Todo el mundo empieza por lo fácil»** (N006, 00:03:53 ✅). Sobre la
  mesa, **ocho pergaminos de misión** con un **sello de rango** cada uno:
  - **Reto activo** (sello rojo «en curso») y **Cerrado** (sello gris).
  - **Doblaje**, **Canto**, **Locución** (pergaminos de tres colores).
  - **Para empezar** = sello **D**; **Con trampa** = un pergamino con **un
    cascabel** atado; **Libre** = pergamino abierto sin sello.

### Concepto B — «La décima pregunta» (#reto-de-la-semana)

- **Objeto y sitio**: **la hoja del examen escrito** del chūnin, sobre **un
  pupitre de madera** del aula en gradas (n.º 470 y 481 ✅). Diez preguntas
  numeradas; **la 10.ª está en blanco**. Detrás, **la pizarra** con las
  reglas a tiza. Un lápiz, una goma y virutas.
  - En Blender: **School Desk 01** y **Standing Chalkboard 01** (Poly
    Haven, CC0), papel **Paper001** de ambientCG. La tinta y el lápiz
    **siguen las ondas** del papel.
- **Personaje**: **Naruto**, en la pose de **golpear la mesa y levantarse**
  («¡Yo no huyo!», N025, 00:10:55 ✅; fotograma a sacar). Alternativa con
  imagen ya vista: **Sakura pensando** con el lápiz (n.º 481 ✅).
- **Cómo habla**: su frase va **escrita a lápiz en el margen** de la hoja,
  con letra torcida (**Klee One**): **«No me retracto. Ese es mi camino
  ninja»** (N025, 00:11:41 ✅, traducción mía).
- **Dónde va cada texto**:
  - **Cabecera impresa** de la hoja (**Shippori Mincho**): **Reto de la
    semana**.
  - **Reglas 1 a 4** (impresas, una por renglón, sin «·»): **Un reto por
    semana**, **Una línea, una escena, un tono**, **Se entrega dentro del
    hilo del reto**, **No se gana nada**.
  - **Pregunta 10**, en grande: **¿Te atreves?** Y en la casilla de la
    respuesta, a lápiz: **Esa es la gracia**. (Es el chiste de la serie:
    la 10.ª pregunta **no existía**, la respuesta era atreverse ✅.)
  - **Pizarra** (lámina 2): las **8 etiquetas** a tiza, en tres columnas.
- **Para que no quede plano**: **lápiz desenfocado** en primer plano; la
  **mano de Naruto** golpeando el borde del pupitre levanta la hoja; filas
  de pupitres que se alejan; **luz lateral** de ventana.

### Concepto C — «La barra de Ichiraku» (#general-doblaje)

- **Objeto y sitio**: **el puesto de ramen Ichiraku al atardecer** (obj 23
  ✅). La **cortinita (noren)** con «一楽» y, en la pared, **las tablillas
  de madera del menú**. Dos cuencos humeando en la barra.
  - En Blender: «Noren (Low Poly)» de game_travel (CC BY), **Wooden Stool
    01/02** y **Wooden Bowl 01** (Poly Haven, CC0), tablones **Brown Planks
    05**, tejado **Reed Roof 03**. HDRI de atardecer **Evening Meadow**.
- **Personaje**: **Naruto comiendo** (n.º 105 ✅) y **Iruka** a su lado,
  escuchando. Es **el dúo del «profe que escucha dudas de novato»**, y
  Naruto es **la voz más famosa del doblaje latino** (Isabel Martiñón,
  20 años ✅).
- **Cómo habla**: **latino de verdad**. Una tablilla del menú, escrita a
  pincel (**Yuji Boku**): **«¡De veras!»** ✅ (la frase del doblaje).
  Y en un papelito pegado a la barra, la de Iruka en letra fina:
  **«Pregunta sin miedo»** (adaptación mía).
- **Dónde va cada texto** (descripción real del canal: «Del oficio: micros,
  voces, técnica y dudas de novato. Tu voz grabada va a demos; los papeles,
  a castings»):
  - **Noren**: **General doblaje**.
  - **Cuatro tablillas del menú**, una palabra en cada una: **Micros**,
    **Voces**, **Técnica**, **Dudas de novato**.
  - **Dos carteles de papel** en el poste, como los de «agotado»: **Tu voz
    grabada va a demos** y **Los papeles, a castings**.
- **Para que no quede plano**: **vapor** de los cuencos delante de las
  caras; **bombilla cálida** bajo el toldo y calle **azul de atardecer**
  detrás; el **noren tapa en parte** a los personajes por arriba.

### ¿Cuál primero?

1. **Concepto A**: es el más fiel (la prueba más famosa de la serie **es**
   un reto con trampa donde no se gana nada), el objeto se hace en Blender
   con modelos CC0 y **Kakashi** es la apuesta segura de popularidad.
2. **Concepto B** como **lámina 2** del mismo canal, o como alternativa si
   se quiere a **Naruto** de protagonista.
3. **Concepto C** sólo si el encargo 29 elige Naruto para #general-doblaje.

**Idea suelta** para un canal de escritura (#textos o #poemas, ya con
serie): **el libro de Jiraiya** y su «continuación» (S133, 00:19:20; S174,
00:17:27 ✅): «**La continuación es mi propia vida**».

---

## 20 · Lo que no pude verificar

- **La descripción completa de #reto-de-la-semana** (en el inventario sale
  cortada en «es para grabar»).
- **Frases del doblaje latino línea por línea** (no hay subtítulos latinos
  abiertos). Las que doy como latinas salen de Doblaje Wiki.
- **Minutos exactos en YouTube**: los vídeos no tenían subtítulos y el
  bloqueo de YouTube impidió más.
- **Game UI Database** (reto de Cloudflare), **TV Tropes** y **The Cutting
  Room Floor** directos (403): TCRF lo leí por Wayback.
- **Hojas de modelo oficiales** del anime.
- **Si «Rise» sonaba cantado** en Cartoon Network Latinoamérica.
- **Qué letra usan los globos** del manga de Panini México y de VIZ.
- **Tamaño real** de los fondos oficiales de naruto-official.com.

---

## 21 · Bitácora de búsqueda

### 21.1 Comprobación de red

- **Fase 1** (24-sep-2026, mañana): curl y WebFetch **bloqueados** en
  doblaje.fandom.com, naruto.fandom.com, es.wikipedia.org, dafont,
  1001fonts, vidaextra, tcrf.net, gameuidatabase.com, naruto-official.com,
  behance.net, web.archive.org. **GitHub** y **las API de Poly Haven y
  ambientCG** sí respondían.
- **Fase 2** (tras el aviso del coordinador): **abiertos** Fandom (API),
  Doblaje Wiki (API), Sketchfab (API), Arctic Shift, Wayback Machine,
  YouTube (sólo con `yt-dlp` cliente `mweb` y oEmbed). **Siguen cerrados**
  tcrf.net y tvtropes.org directos (403) y Game UI Database (Cloudflare).

### 21.2 Búsquedas web (33 hechas)

| # | Idioma | Búsqueda |
|---|---|---|
| 1 | ES | Naruto doblaje latino reparto Isabel Martiñón Sasuke Sakura Kakashi Jiraiya Itachi |
| 2 | ES | Naruto doblaje latino estudio Dubbing House director Eduardo Garza «Créelo» «De veras» |
| 3 | ES | Naruto Shippuden doblaje latino Netflix 2024 2025 estudio director reparto |
| 4 | ES | «de veras» Naruto origen dattebayo «créelo» Isabel Martiñón entrevista |
| 5 | ES | frases icónicas Naruto doblaje latino «otro día será» «más perrón» memes |
| 6 | ES | Itachi doblaje latino «Perdóname Sasuke» «otro día será» Héctor Emmanuel Gómez |
| 7 | EN | Naruto official character popularity poll results, NARUTOP99 |
| 8 | JA | NARUTO 人気投票 歴代 結果 カカシ 1位 イタチ NARUTOP99 |
| 9 | EN | «ROAD OF NARUTO» 20th anniversary official video Studio Pierrot |
| 10 | EN | Naruto logo font name, «Ninja Naruto», manga lettering |
| 11 | EN | Ultimate Ninja Storm story mode dialogue box UI, Game UI Database |
| 12 | EN | tcrf.net Naruto Ultimate Ninja Storm unused text, Storm Connections |
| 13 | EN | Naruto soundtrack Toshio Masuda, Takanashi, openings |
| 14 | ES | Naruto estreno Latinoamérica Cartoon Network 2007, historia del doblaje |
| 15 | ES | «Christine Byrd» Sakura, «Paco Mauri» Jiraiya, «Alfonso Obregón» Kakashi |
| 16 | ES | Jiraiya voz en español latino |
| 17 | JA | 西尾鉄也 NARUTO キャラクターデザイン インタビュー |
| 18 | EN | Kishimoto interview orange jumpsuit, Konoha inspiration |
| 19 | EN | Naruto artbook «UZUMAKI», «PAINT JUMP», illustrations |
| 20 | JA | NARUTO 公式 描き下ろし イラスト 2025 2026 キービジュアル |
| 21 | EN | sketchfab Naruto headband kunai scroll «CC Attribution» |
| 22 | EN | sketchfab Ichiraku ramen, Hokage mountain, Konoha |
| 23 | EN | polyhaven alarm clock, tree stump, bell CC0 |
| 24 | EN | Naruto fan art ArtStation, Pixiv, Team 7 |
| 25 | ES | Naruto memes fandom latino, Naruto run, Sasukeee, TikTok 2025-2026 |
| 26 | EN | Know Your Meme Naruto memes |
| 27 | EN | Naruto live-action movie 2026 news, Destin Daniel Cretton |
| 28 | ES | «peor que basura» Kakashi frase español latino |
| 29 | EN | «Ultimate Ninja Storm Connections» review story mode |
| 30 | ZH | 火影忍者手游 剧情模式 对话框 界面 卷轴 UI |
| 31 | KO | 나루토 캐릭터 인기투표 결과 카카시 이타치 순위 |
| 32 | JA | ナルト 公式人気投票 歴代1位 第1回~第6回 |
| 33 | ES | reto de doblaje Naruto TikTok, actores retan a fans |
Por idioma: **ES 12 · EN 15 · JA 4 · ZH 1 · KO 1** = **33**.

Además, **5 búsquedas en YouTube con yt-dlp** (`ytsearch6:`): «ROAD OF
NARUTO studio pierrot official», «Kakashi prueba de los cascabeles doblaje
latino», «Naruto Shippuden Netflix doblaje latino tráiler oficial»,
«Eduardo Garza de veras Naruto entrevista», «Naruto Ultimate Ninja Storm
story mode dialogue».

### 21.3 Sin cupo de búsqueda (API, git, descargas)

- **GitHub**: subtítulos de Hulu de **Naruto (220)** y **Shippuden (500)**
  en [kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror);
  **50 letras** de [google/fonts](https://github.com/google/fonts); la letra
  **Ninja Naruto** desde [Thitas-DEV/NarutoCardGame](https://github.com/Thitas-DEV/NarutoCardGame).
- **Narutopedia** (API): 30 páginas para las hojas; *Bell Test*, *Third
  Training Ground*, *Memorial Stone*, *Icha Icha*, *Ramen Ichiraku*,
  *Naruto Character Popularity Polls*, *Music*.
- **Doblaje Wiki** (API): *Naruto*, *Naruto Shippuden*, *Naruto
  (franquicia)*.
- **Sketchfab** (API): 10 fichas y 10 búsquedas.
- **Poly Haven** (API: 521 modelos, 862 texturas, 997 HDRI) y
  **ambientCG** (API).
- **Arctic Shift**: r/Naruto, consultas «bell test» e «Iruka».
- **Wayback Machine**: The Cutting Room Floor, *Naruto: Ultimate Ninja
  Storm*.
- **YouTube** (oEmbed y yt-dlp): 12 vídeos.

### 21.4 Fuentes consultadas por tipo (más de 60)

- **Oficiales**: naruto-official.com (noticias 01_1468, 01_1486, 01_1726,
  01_2320, 01_2472; especial 20th; ANIME GALLERY; NARUTOP99), canal
  スタジオぴえろ【公式】, VIZ (YouTube y tienda), Shueisha (Animation
  Chronicle), Tencent (hyrz.qq.com).
- **Entrevistas y staff**: ANN (Takanashi, 2021), GetNews / Otajo (staff
  del anime), Number Web (Nishio), Anime Style, ComicBook.com y ScreenRant
  (Kishimoto y el naranja).
- **Otros idiomas**: japonés (Oricon, Mantan, Animate Times, Natalie,
  Anime Hack), coreano (Hypebeast Corea, Namu Wiki, theqoo), chino
  (GameRes, 18touch, Tencent).
- **Wikis**: Narutopedia (API), Doblaje Wiki (API), Wikipedia (por
  resumen), Know Your Meme, TV Tropes (por resumen), Todo Anime Wiki.
- **Foros**: Reddit r/Naruto (Arctic Shift), ResetEra (por resumen).
- **Arte**: ArtStation (pung lonewolf, Davide Rossini, Christoffer Radsby),
  DeviantArt (solisandluna, ShiroChan92), Pinterest (sólo para localizar).
- **Vídeo**: YouTube (Pierrot, VIZ, El Retake, Entrevistadoz, Datos Geek,
  TeleGeek, RuNix, Tu Rincón Del Hobby), TikTok (SDV, Cracken Shop, Isabel
  Martiñón).
- **Juegos**: The Cutting Room Floor (Wayback), MP1st, TheGamer, Behance.
- **Código y recursos**: GitHub (kitsunekko-mirror, google/fonts,
  NarutoCardGame, naruto-handsign-dataset, anime-filler-list-data),
  Sketchfab, Poly Haven, ambientCG.
- **Doblaje latino**: Doblaje Wiki, ANMTV (2009, 2021, 2024, 2025, 2026),
  El Comercio, FUNiAnime, Senpai, 3DJuegos, Xataka México, El Siglo de
  Torreón y de Durango, Mangaka Store, La Mole, Cine Premiere, Código
  Espagueti, Bubbleblabber LATAM.
- **Noticias 2026**: Variety y Empire (la película de imagen real busca
  a sus tres protagonistas en todo el mundo, julio de 2026) ✅.

### 21.5 Lo que NO encontré

- La **descripción completa** del canal (cortada en el inventario).
- **Subtítulos latinos** con tiempos.
- Capturas de **Game UI Database**.
- La letra de los **globos del manga** en español.
- **Hojas de modelo** del anime.
