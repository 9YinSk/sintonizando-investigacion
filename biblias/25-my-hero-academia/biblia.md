---
tags: [biblia, serie, laminas]
serie: "My Hero Academia (Boku no Hero Academia)"
canal: "#material-de-clase"
fecha: 2026-09-24
---

# Biblia · My Hero Academia — para #material-de-clase

> [!important] Cómo se hizo, y sus límites
> - La red de esta sesión estaba cerrada para casi todo. Fandom (también
>   Doblaje Wiki y su API), Wikipedia, Crunchyroll, YouTube, Reddit y la
>   mayoría de webs daban **bloqueo** por WebFetch o por curl. Por eso **no
>   se pudo correr** `herramientas/investigar_serie.py`: **no hay hojas de
>   contacto** ni carpeta `hojas/`.
> - La fuente principal fue la **búsqueda web** (la lista está al final, en
>   la bitácora), en español, inglés, japonés, chino y coreano.
> - GitHub sí respondía. De ahí saqué lo más útil: **los subtítulos
>   japoneses de Netflix y Amazon, con sus tiempos**, de la temporada 1, la
>   2, la **temporada final (8)** y el especial **«More»**, del repositorio
>   [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv).
>   Con ellos doy el **minuto de cada escena** y la frase exacta en japonés
>   (la traducción al español es mía, no del doblaje). El minuto es el de
>   ese archivo: puede moverse uno o dos minutos según la plataforma.
> - También bajé de [google/fonts](https://github.com/google/fonts) las
>   letras propuestas y comprobé una a una, con fontTools, si traen
>   á é í ó ú ñ ¿ ¡.
> - **Cómo leo los episodios**: «1×06» es temporada 1, episodio 6. Entre
>   paréntesis va el número total («ep. 34»). La temporada 8 es la
>   **FINAL SEASON** (2025), episodios 160 a 170. «**No.170+1**» es el
>   especial «**More**» (ep. 171, emitido el 2 de mayo de 2026 ✅), con
>   la 1-A ya adulta y **Deku de profesor**.
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su minuto.
>   ⚠️ **dudoso**: una sola fuente, o lo describo de memoria. Lo de memoria
>   siempre va marcado.
> - **Segunda pasada (25-sep-2026), con la red abierta.** La hizo un equipo:
>   cuatro investigadores (imagen, vídeo, voz, texto) y un redactor. Se
>   pudo usar la **API de Fandom** (wiki en inglés y Doblaje Wiki, wikitext
>   entero), la **API de Sketchfab** (licencias reales), **Dailymotion** e
>   **Internet Archive** (el episodio 1 entero, OP1, OP2, ED1, un tráiler y
>   tres escenas, mirados con `fotogramas.py`), clips con **audio del
>   doblaje latino** oídos con `voz.py`, y `estilo.py` para medir colores.
>   YouTube siguió pidiendo iniciar sesión, y TV Tropes, konomanga.jp y la
>   web de fondos de heroaca.com siguieron en 403.
> - Ahora **sí hay hojas de contacto**: tres en `hojas/` (ver «Las hojas de
>   contacto», antes de los conceptos).
> - **Ojo con los minutos del episodio 1**: la copia de Internet Archive
>   va **unos 4 minutos por detrás** de los subtítulos de Netflix que usé
>   en la primera pasada. Pongo el de cada fuente y digo cuál es.

---

## Segunda pasada · qué cambió

**Corregido (antes → ahora)**

- «**Tú** puedes ser un héroe» → el doblaje latino dice «**Puedes ser un
  héroe**», sin el «Tú» (oído y visto, [Dailymotion x7xktih, 2:43](https://www.dailymotion.com/video/x7xktih?t=163)) ✅.
- Aizawa en la T1: «José Arenas (dudoso)» → **Eduardo Wasveiler**, luego
  redoblado entero por **Ernesto Daniel Rumbaut** (Doblaje Wiki, «Sobre el
  reparto») ✅. Kurogiri: **Odin Subero** → **Héctor José Pernia** ✅.
- Encuesta «Jump n.º 19» → es la **9.ª encuesta oficial** de la revista ✅.
- Pose de Deku con el cuaderno en 1×01: «lo ofrece con las dos manos» →
  **lo mira él mismo, orgulloso**, con «ALL MIGHT» recién escrito en
  grande ✅ (visto en el fotograma).
- Uraraka (Andrea Villaverde), Iida, Burnin, Sero, Aoyama y Bakugo (Rómulo
  Bernal): de ⚠️ a ✅ con segunda fuente.
- «Gina Sánchez dirigió la película 4» (3DJuegos): Doblaje Wiki sólo la
  pone como **adaptadora** de la serie. Quedan las dos versiones ⚠️.
- Poses, luz y paleta «de memoria» → **vistas en fotogramas y medidas**
  con `estilo.py` (§2, §5, §15).
- Hex de vestuario «a ojo» → **medidos sobre las hojas de modelo
  oficiales** del anime (§16).

**Añadido**

- La portada real del cuaderno: libreta de espiral marca **«Campos»**,
  lomo azul, «Análisis de héroes para el futuro», **«No. 13»** (§2).
- Frases textuales del doblaje latino: «¡Yo he venido!», «¡Ya estoy
  aquí!», los insultos de Bakugo, Kota, Rei Todoroki y «Yo también quiero
  ser un héroe», todas con clip y minuto (§10).
- Encuestas oficiales 1.ª a 9.ª con votos, acumulado total y **desglose
  latinoamericano** del World Best Hero: **Kirishima 3.º** y **Aizawa 5.º**
  en Latinoamérica (§9).
- Nueve modelos 3D CC BY con licencia leída en la API, y modelos
  rigueados para Blender (§4 y §18-b).
- Perfiles oficiales de los *databooks* y tabla de gustos (§8 y §18-d).
- Los puntos que faltaban del encargo: **técnica y cómo replicarla,
  texturas 2D, gustos, por qué la aman, fan dubs, colaboraciones, obras
  parecidas y el mundo** (§18-a a §18-h).
- Tres hojas de contacto, la tabla «Cumplimiento del encargo» y la
  bitácora de la segunda pasada.

**Los ⚠️**: la primera pasada tenía **108**. Al cerrar esta pasada quedan
los que se cuentan en la tabla de cumplimiento; los que siguen dudosos
dicen por qué (casi todos: YouTube, TikTok o una web en 403).

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección **LA ACADEMIA**):

> **ıı・📚・material-de-clase** (foro) · 2 hilos · etiquetas: Doblaje,
> Canto, Locución, Edición, Grabación de la clase, Ejercicio, Material de
> apoyo, Para principiantes, Nivel medio — _Lo que se da en clase y los
> ejercicios de cada alumno. Un hilo por tema o por alumno. Etiqueta si es
> de doblaje o de canto._
> - 📌 📌 Para los profesores: cómo se sube una clase (0 msj) · adj: material-de-clase.png
> - EJEMPLO · Clase 1 — Respiración y apoyo (0 msj) · adj: —

Función según el encargo: **foro donde cada profesor sube su clase**, con
tres partes: **De qué fue / Material / Para practicar**.

El canal vecino de LA ACADEMIA es **ıı・📣・avisos-clases** (encargo 24,
Assassination Classroom). Las dos láminas deberían parecer **del mismo
colegio**: las dos series pasan en una escuela con profesores raros, así
que encajan.

La biblia de **81-mushoku-tensei** también tenía #material-de-clase, pero
no propone lámina para él. No es un problema: las biblias son generales.

### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Material de clase** | nombre del canal |
| 2 | **Lo que se da en clase y los ejercicios de cada alumno** | para qué es |
| 3 | **Un hilo por tema o por alumno** | cómo se ordena |
| 4 | **De qué fue** | parte 1 de cada clase |
| 5 | **Material** | parte 2 |
| 6 | **Para practicar** | parte 3 |
| 7 | **Etiqueta si es de doblaje o de canto** | la regla |
| 8 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

### Los textos de la lámina 2 (las etiquetas)

Las nueve etiquetas **no caben bien** en la lámina 1 sin saturarla. Propongo
**lámina 2**, con las etiquetas en tres grupos:

| Grupo | Etiquetas |
|---|---|
| **Qué área** | Doblaje · Canto · Locución · Edición |
| **Qué es** | Grabación de la clase · Ejercicio · Material de apoyo |
| **Qué nivel** | Para principiantes · Nivel medio |

(En la lámina, cada etiqueta va en su propio sitio: sin «·».)

La idea encaja con la serie: Deku **numera sus cuadernos y cita la página**
(«¡Cuaderno número 10, página 18!», 1×07, 00:05:26 ✅), así que la lámina 2
puede ser **el índice del cuaderno** con pestañas de colores.

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué MHA encaja | Pasa en **un instituto para héroes (U.A.)** donde los profesores son héroes profesionales y cada uno da su materia. **All Might es un profesor novato que lee su clase de una chuleta** («¡Una chuleta!», カンペ, 1×06, 00:15:18 ✅). Y el protagonista **apunta todo en cuadernos numerados**: «Análisis de héroes para el futuro». Al final de la serie, **Deku es profesor en U.A.** y sigue escribiendo en su cuaderno (8×11, 00:05:44 «Deku-sensei» y 00:09:58 ✅; manga cap. 430 ✅). |
| El objeto | **El cuaderno de Deku**, «将来の為のヒーロー分析» (Análisis de héroes para el futuro). El **n.º 13** tiene el borde **quemado** porque Bakugo lo hizo explotar y lo tiró a una fuente con peces (1×01, 00:10:33 a 00:11:58 ✅). **All Might se lo firmó** en el mismo episodio (00:19:19 ✅). Existe **réplica oficial con licencia** del n.º 13 quemado ✅ (ver §3). |
| El más querido | **Bakugo**, 1.º en la encuesta mundial oficial **WORLD BEST HERO** (2024, 6,12 millones de votos) ✅. Deku 2.º, Todoroki 3.º y **Aizawa 4.º**: el profesor está por encima de All Might ✅. Bakugo es 1.º en **todas** las encuestas de Jump desde la 2.ª ✅. En **Latinoamérica**: Bakugo, Deku, **Kirishima 3.º**, Todoroki y **Aizawa 5.º** ✅ (§9). |
| Quién habla en la lámina | Tres opciones: **Deku-profesor** (adulto, traje, cuaderno: es literalmente «un profe que sube su clase»), **Aizawa** (el profesor más querido) o **Bakugo** dando clase a gritos («¡Te voy a enseñar hasta matarte!», 2×21 ep. 34, 00:05:36 ✅). Ver §19. |
| Cuadro de diálogo propio | **No es una burbuja blanca**: la serie pone texto en **la letra a mano de Deku en su cuaderno**, en el grito «**¡Más allá! ¡Plus Ultra!**» que cierra cada avance ✅, en **pizarritas** que los alumnos levantan al presentar su nombre de héroe (2×13 ep. 26: el diálogo ✅, la pizarra de memoria ⚠️), en la **chuleta** de All Might ✅ y en **viñetas de cómic americano** en el juego *One's Justice* ✅. Ver §7. |
| Letras | **Caveat** o **Kalam** (letra de Deku), **Bangers** (rótulos de cómic, «SMASH»), **Anton** u **Oswald** para títulos gruesos. Todas traen tildes, ñ, ¿ y ¡: comprobado en el archivo. |
| Voz latina | Deku **Sebastián Reggio** ✅, Bakugo **Rómulo Bernal** (también dirige) ✅, All Might **Orlando Noguera** ✅, Todoroki **Juan Felipe Sierra** ✅, Aizawa **Ernesto Rumbaut** ✅, Uraraka **Andrea Villaverde** (T1 a T6 ep. 1, ✅ Doblaje Wiki y Behind The Voice Actors) y **Sofía Baltazar** (desde T6) ✅. Estudio **The Kitchen**, Miami ✅. Ver §10. |
| Tono | Luminoso y de esfuerzo: cielo azul, verde de Deku, rojo y amarillo de héroe, **sombras duras de cómic americano** en All Might (hasta los personajes dicen que tiene «otro estilo de dibujo», 1×01, 00:19:11 ✅). Nada oscuro ni gris. |
| Juegos | **One's Justice 1 y 2** (historia contada en **viñetas de cómic**) ✅, **All's Justice** (5 de febrero de 2026) ✅, **Ultra Rumble** y la app **ULTRA IMPACT** ✅. |

---

## 2 · Las escenas que sirven para #material-de-clase (con minuto)

Todas salen de los subtítulos japoneses de Netflix (temporadas 1 y 2) y de
Amazon (temporada final) de
[kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Boku%20no%20Hero%20Academia):
el texto y el minuto están comprobados ✅. La traducción es mía. En la
primera pasada lo que **se ve** iba de memoria. En la segunda se miraron
los fotogramas del episodio 1 y de tres escenas: está en **2.4**. Lo que
no sale en 2.4 sigue sin mirar.

### 2.1 El cuaderno de Deku (el objeto)

| Escena | Minuto | Qué pasa / qué se dice | Para qué sirve |
|---|---|---|---|
| 1×01 | 00:06:44 a 00:06:58 | Deku **toma notas en plena calle** mientras mira a una heroína gigante: «Se agranda… pero con el daño a la ciudad, su uso sería limitado». Un señor: «¡Anda, tomando notas! ¿Quieres ser héroe? ¡Échale ganas!» | Deku **explicando** algo con el cuaderno en la mano |
| 1×01 | 00:10:11 | «Tengo que ir a casa a pasarlo **al cuaderno**» (ノートにまとめなきゃ) | La costumbre de apuntar |
| 1×01 | 00:10:23 | Un compañero lee la portada: «¿“**Análisis de héroes para el futuro**”?» | **El título exacto** del cuaderno |
| 1×01 | 00:10:33 a 00:10:40 | Bakugo **lo hace explotar** entre las manos y lo tira por la ventana | Por qué está quemado |
| 1×01 | 00:11:55 a 00:11:58 | Deku lo saca de la fuente, con peces mordiéndolo: «No es comida, tonto… **es mi cuaderno**» | El cuaderno mojado y quemado |
| 1×01 | 00:19:15 a 00:19:26 | «¡Un autógrafo! ¡En el cuaderno!» → «¡**Ya está firmado**!» → «¡Será el tesoro de la familia!» | **La firma de All Might** en una página |
| 1×06 (ep. 6) | 00:12:55 a 00:12:58 | La madre de Deku le regala el traje: lo cosió porque «cuando te dormiste estudiando, **vi tu cuaderno**» | En el cuaderno también hay **diseños de traje** |
| 1×06 | 00:21:25 a 00:21:32 | A Bakugo: «Todo lo que me pareció genial, **los análisis de héroes, está todo en mis cuadernos**. En el cuaderno que tú hiciste explotar y tiraste» | El cuaderno como arma |
| 1×07 | 00:05:26 | En plena pelea: «¡**Cuaderno número 10, página 18**!» | **Cita la página**: idea para la lámina 2 |
| ep. 13.5 (recap «ヒーローノート», Amazon) | 00:00:38 | «Desde entonces tengo **un cuaderno que voy llenando día a día**» | Voz en off para presentar |
| ep. 13.5 | 00:13:45 | «**A todos los tengo apuntados** en mi cuaderno de héroes» | Cuaderno = registro de cada alumno |
| 8×11 (ep. 170, el último) | 00:09:58 a 00:10:03 | Deku adulto: «¿Y por qué **sigo escribiendo esto**? Porque la emisión todavía no ha terminado» | **Deku-profesor escribiendo** |

El episodio 13.5 es un resumen que se llama literalmente **«Cuaderno de
héroe»** (ヒーローノート) ✅ (nombre del archivo de Amazon).

### 2.2 Los profesores dando clase

| Escena | Minuto | Qué pasa / qué se dice | Para qué sirve |
|---|---|---|---|
| 1×05 (ep. 5) | 00:09:00 | Aizawa (sale de un **saco de dormir** amarillo, de memoria ⚠️): «Soy **Shota Aizawa, su tutor**. Mucho gusto» | Presentarse |
| 1×05 | 00:09:07 a 00:09:29 | «Pónganse esto y salgan al campo». «¿Y la ceremonia? ¿Y la orientación?» «Si quieren ser héroes, **no hay tiempo** para eso» | El profe que va al grano |
| 1×05 | 00:09:55 | Sobre los exámenes de siempre: «**No es racional**» (合理的じゃない) | Su palabra fetiche |
| 1×05 | 00:10:35 a 00:10:42 | «Primero, **conocer tu máximo**. Eso forma la base de un héroe. Es lo racional» | **Explicar** |
| 1×05 | 00:12:23 a 00:12:34 | «Durante tres años, U.A. les pondrá dificultades sin parar. “**Más allá**”, **Plus Ultra**. Supérenlas con todo» | **Animar**, a su manera |
| 1×06 (ep. 6) | 00:05:11 a 00:05:15 | «Por cierto, lo de expulsar era mentira. **Una mentira racional** (合理的虚偽) para sacar lo mejor de sus dones» | El chiste de Aizawa |
| 1×06 | 00:09:29 a 00:09:48 | Deku narra el horario: «Por la mañana, **materias obligatorias**, clases normales como inglés». Present Mic: «**Everybody hands up!** ¡Anímense!» | Clase normal, profe animado |
| 1×06 | 00:10:02 a 00:10:13 | «Y por la tarde… **Formación básica de héroes**». All Might: «¡Ya… estoy… aquí! ¡**Entrando por la puerta como es normal**!» | **Entrada de profesor** |
| 1×06 | 00:10:30 a 00:10:43 | «Yo doy **Formación básica de héroes**: la materia con **más créditos**. ¡Hoy toca esto! ¡**Entrenamiento de combate**!» (de memoria: levanta una tarjeta con la palabra **BATTLE** ⚠️) | **Anunciar el tema** de la clase |
| 1×06 | 00:15:13 a 00:15:18 | Todos preguntan a la vez; All Might: «¡Uno por uno!». Deku ve que saca un papel: «¡**Una chuleta**!» (カンペ) | **El profe lee su material**: la escena clave |
| 1×12 (ep. 12) | 00:07:01 | Un alumno (el subtítulo no dice quién ⚠️): «Y eso que **da clase leyendo la chuleta**, como un novato» | Lo confirma otro alumno |
| 1×03 (ep. 3) | 00:08:45 a 00:08:56 | All Might le da a Deku su plan: «¡Esto! ¡Mi **Plan Sueño Americano para aprobar**! Un plan de entrenamiento. Toda tu vida seguirá esto» | **El material para practicar** |
| 1×03 | 00:12:41 | «Tú **no estás siguiendo el plan**, ¿verdad? Pasarse es contraproducente» | Regañar con cariño |
| 1×03 | 00:13:39 | «Este tío **ajustará un poco el plan**» | Ajustar el ejercicio al alumno |
| 2×13 (ep. 26) | 00:03:46 | Aizawa: «Vamos a **inventar nombres de héroe**» | Clase especial |
| 2×13 | 00:06:55 | Midnight: «Los que tengan listo el suyo, que **lo presenten**». Kirishima: «¿**Hay que exponerlo**?» | Cada alumno **levanta su pizarra** |
| 2×13 | 00:13:01 a 00:13:09 | Deku enseña la suya: «Ya no soy el Deku inútil… ¡Soy el Deku de “**¡tú puedes!**”! Este es mi nombre de héroe» | **Presentar** con orgullo |
| 2×21 (ep. 34) | 00:03:03 a 00:03:19 | Aizawa: «Bueno, **la clase termina aquí**. Queda una semana para los finales. Hay **examen escrito y práctico**. Entrenen la cabeza y el cuerpo a la vez. **Es todo**» | **Cerrar una clase** |
| 2×21 | 00:04:16 a 00:05:17 | Yaoyorozu se ofrece a dar **clases particulares** a media clase, en su casa, con té de Harrods | La **alumna que enseña** |
| 2×21 | 00:05:35 a 00:05:36 | Bakugo a Kirishima: «¡Yo también sé! **¡Te voy a enseñar hasta matarte!**» (教え殺したろか) | **Bakugo profe**: gancho cómico |
| 8×10 (ep. 169) | 00:09:31 a 00:09:36 | All Might a Deku (todavía alumno): «Venga, a cambiar el chip. Desde hoy **los nuevos de primero se suman a las clases**. No pongas mala cara» | **Empieza un curso nuevo** |
| 8×11 (ep. 170) | 00:05:44 a 00:05:52 | Kota: «**Deku-sensei**, ¿dónde nos juntamos para la práctica de la tarde?» «En la parada del bus: así aprenden a llegar al USJ» | **Deku-profesor** ✅ |
| 8×11 | 00:13:46 a 00:13:51 | Deku a Aizawa: «Profe, usted intentó **corregirle el lenguaje** a Kacchan, ¿no?» «Al final, no pude» | Humor de sala de profes |
| 8×11 | 00:14:58 a 00:15:19 | Aizawa: «Deberías **ser más estricto con tus alumnos**. Es importante». Deku: «Pero profe, usted era bastante amable» | Los dos profes juntos |
| 8×11 | 00:17:17 a 00:17:28 | Deku analiza el don de un chico en voz alta, sin parar («Si viene del pelo, podrías aplicar lo de Mineta…»). El chico: «Da miedo… ¿pero me está animando?» | **La manía de Deku**, ya de profe |
| 8×11 | 00:17:34 a 00:17:56 | «Después de cumplir tu sueño, **te toca dar sueños**». «Puedes ser un héroe». «**¡Ánimo, jovencito!**» (頑張れ 少年!) | **Animar**: cierre de la serie |

### 2.3 Las frases que todo el mundo conoce (con su minuto)

| Frase (japonés) | Traducción | Dónde |
|---|---|---|
| もう大丈夫 なぜって？ 私が来た！ | «Ya todo está bien. ¿Por qué? **¡Porque ya estoy aquí!**» | All Might, 1×01, 00:13:06 ✅ |
| 君は ヒーローになれる | «**Tú puedes ser un héroe**» | All Might a Deku, 1×02, 00:21:55 ✅ |
| 考えるより先に 体が動いていた | «**El cuerpo se movió antes de pensar**» | All Might, 1×02, 00:21:04 ✅ |
| 更に向こうへ！ Plus Ultra！ | «¡**Más allá**! ¡Plus Ultra!» | Cierre de **cada avance** del episodio siguiente (1×01, 00:24:19 ✅) y lema de U.A. (1×05, 00:12:28 ✅) |
| DETROIT SMASH！ | «¡Detroit Smash!» | All Might, 1×02, 00:16:45 ✅; Deku, 1×04, 00:11:33 ✅ |
| 画風が全然違う！ | «¡**Su estilo de dibujo es totalmente distinto**!» | Deku al ver a All Might en persona, 1×01, 00:19:11 ✅ |

> [!tip] El avance del episodio siguiente
> Todos los episodios de la temporada 1 terminan igual: dos personajes gritan
> «**¡Más allá! ¡Plus Ultra!**» sobre el avance (00:24:05 a 00:24:20, ✅ en
> los 13 subtítulos). Es un «cierre» que el fan reconoce: sirve de firma
> de la lámina.

En el **doblaje latino** la frase de 1×02 es «**Puedes ser un héroe**», sin
«Tú» ✅ (oída en [Dailymotion x7xktih, 2:43](https://www.dailymotion.com/video/x7xktih?t=163)).
La traducción de la tabla es la mía del japonés.

### 2.4 Lo que se ve: fotogramas mirados en la segunda pasada

**Episodio 1 entero** en Internet Archive
([anime-kcd-boku-no-hero-academia-01](https://archive.org/details/anime-kcd-boku-no-hero-academia-01),
1280×720, 24:32, subtítulos en español). Esta copia va **unos 4 minutos
por detrás** de los minutos de Netflix de 2.1 ⚠️. Minutos de esta copia:

| Minuto | Qué se ve | Sirve para |
|---|---|---|
| ~10:33 | **La portada del cuaderno**: libreta de espiral marca **«Campos»**, lomo azul, a mano «Análisis de héroes para el futuro» y «**No. 13**» subrayado. Bakugo se burla detrás ✅ | El objeto exacto de la lámina |
| ~10:55 | Deku se acerca a Bakugo con los **puños apretados al pecho**, hombros encogidos, ojos muy abiertos ✅ | Pedir perdón, suplicar |
| ~11:10 | La mano de Bakugo **humeando**, apoyada en su pecho, mandíbula tensa ✅ | Amenazar |
| ~13:06 | Silueta de **All Might agachado** en un tejado roto, cielo naranja y rojo detrás, en silencio ✅ | Llegar, rescatar |
| ~19:30 | Deku sostiene el cuaderno abierto con **las dos manos** y **mira él mismo** la página con «**ALL MIGHT**» escrito en grande ✅ | Presentar el objeto |
| ~19:55 | All Might **flaco, de espaldas**, manos en la nuca, calle con niebla blanca ✅ | Pensar, confesar un secreto |

Colores medidos con Pillow en esos fotogramas: pelo de Deku `#357459`,
pelo de Bakugo `#F1E7CE`; el tejado de 13:06 `#170D0A` `#4D342B` `#888076`
(negro óxido, nada de azul).

**Tres escenas icónicas** (Dailymotion; el minuto es **del clip**, no del
episodio):

- **All Might «Plus Ultra» contra Nomu**, 1×12, arco USJ
  ([x4hptj4](https://www.dailymotion.com/video/x4hptj4), 26 s). 0:00 puño
  en primer plano, luz blanca lateral, «Go beyond!»; 0:03-0:06 se encoge
  antes del golpe; 0:09 impacto contra **la cúpula del USJ**; 0:18-0:24
  humo blanco contra el cielo nocturno. Episodio y arco confirmados en la
  wiki ✅.
- **Deku contra Muscular**, 3×04 (ep. 42), arco del campamento
  ([x80pei3](https://www.dailymotion.com/video/x80pei3), 2:29). 1:10
  «Mom, I'm sorry!»; 2:00 destello magenta y cian en estrella; 2:10
  «**One For All, 1,000,000%! … Smash!**». El golpe se llama «1,000,000%
  Delaware Detroit Smash» (ficha propia en la wiki) ✅.
- **Uraraka contra Bakugo**, 2×09 (ep. 22), Festival Deportivo
  ([x6soboa](https://www.dailymotion.com/video/x6soboa), 8:43, subtítulos
  en español). 0:00 Bakugo con la cara iluminada por su explosión; 5:30
  Uraraka de frente, **puño cerrado al pecho**: «¡Yo ganaré!»; 6:00 primer
  plano con ojos llorosos: «¡Ganaré y seré como Deku!»; 8:00-8:30 en el
  suelo, jadeando ✅.

---

## 3 · Arte oficial y referencias visuales

> [!note] Primera pasada sin imágenes; segunda con la wiki abierta
> En la primera pasada no se bajó ninguna imagen: 3.1 a 3.4 son enlaces
> vistos en el buscador. En la segunda se miraron 192 imágenes de la wiki
> en hojas de contacto y se midieron tamaños reales: está en **3.5**.

### 3.1 Key visuals y material del anime

| Qué | Enlace | Qué tiene | Estado |
|---|---|---|---|
| Key visual de la **FINAL SEASON** (anunciada el 4 de octubre de 2025) | [X de @heroaca_anime](https://x.com/heroaca_anime/status/1945060783974752608) · [Animate Times](https://www.animatetimes.com/news/details.php?id=1752567732) | La imagen principal de la temporada final | ✅ existe; contenido sin ver ⚠️ |
| **Fondos de pantalla oficiales** | [heroaca.com/special/wallpaper.html](https://heroaca.com/special/wallpaper.html) | Descargas oficiales para PC y móvil | ⚠️ sin abrir |
| **Galería oficial** | [heroaca.com/gallery/](https://heroaca.com/gallery/) | Imágenes de cada temporada | ⚠️ sin abrir |
| **Hojas de personaje de Yoshihiko Umakoshi** (diseñador del anime) | [Animate Times](https://www.animatetimes.com/news/details.php?id=1447031721) | Hojas de modelo de la temporada 1 | ⚠️ sin abrir |
| Ficha de la obra en el estudio | [BONES: FINAL SEASON](https://www.bones.co.jp/work/heroaca8/) · [BONES: T1](https://www.bones.co.jp/work/heroaca1/) | Visual y créditos | ⚠️ |
| **Blu-ray T1, vol. 1**: portada dibujada a propósito por **Umakoshi** (con drama CD y libreto de 24 páginas) | [SPICE](https://spice.eplus.jp/articles/123803) · [Animate Times](https://www.animatetimes.com/news/details.php?amp&id=1460946595) · [tienda TBS](https://animaru.jp/anmr/product/P0076158) | Pose dinámica de Deku y compañía ⚠️ (quién sale exactamente: sin ver) | ✅ existe |
| **Blu-ray FINAL SEASON, vol. 1** | [Animate Times](https://animatetimes.com/news/details.php?id=1761375662) · [TOHO](https://tohoentertainmentonline.com/shop/g/gTASB07115/) | Portada de la temporada final | ✅ existe; sin ver ⚠️ |

**Equipo del anime** ✅ (resumen de [heroaca.com/staff](https://heroaca.com/staff/)
y de BONES): dirección general **Kenji Nagasaki**; dirección **Naomi
Nakayama**; diseño de personajes **Yoshihiko Umakoshi**; dirección de arte
**Shigemi Ikeda y Yukiko Maruyama** (Atelier Musa); color **Kazuko Kikuchi**
(Wish); fotografía **Takashi Sawa**; estudio **BONES** (BONES Film en la
final). Música: **Yuki Hayashi** ✅ (ver §11).

### 3.2 El manga (Kōhei Horikoshi)

- **Tomo 1 y tomo 42 (el último)** tienen la misma portada «espejo»:
  **fondo amarillo**, logo **rojo y blanco**, el nombre del autor en
  negro abajo a la izquierda ✅ ([Anime Corner](https://animecorner.me/my-hero-academia-manga-unveils-final-volume-cover/),
  [Screen Rant](https://screenrant.com/mha-hero-academia-manga-final-cover-deku/)).
  En el 42, Deku con **uniforme y mochila rota**, caminando y mirando atrás
  con una sonrisa ⚠️ (los dos artículos lo describen algo distinto: uno
  dice que Deku ocupa el sitio de All Might al fondo y un niño, Dai, el de
  Deku pequeño). El tomo 42 trae **38 páginas nuevas** con el epílogo ✅
  ([Oricon](https://us.oricon-group.com/news/2523/)).
- En EE. UU. el tomo 42 salió con **cuatro portadas**, una de Deku, una de
  Bakugo y una de Todoroki ✅ ([VIZ](https://www.viz.com/blog/posts/the-collector-s-guide-to-my-hero-academia-vol-42)).
- **Libros oficiales de personajes**: *Ultra Archive* (con entrevista a
  Umakoshi y material de diseño) y *Ultra Analysis* ✅
  ([Shueisha](https://www.shueisha.co.jp/books/reader/main.php?cid=9784088807195)).
  El título *Ultra Analysis* es un guiño al cuaderno de Deku ⚠️ (deducción
  mía).

### 3.3 El cuaderno, como objeto que existe de verdad

Para modelarlo en Blender hay **réplicas oficiales**:

| Qué | Enlace | Para qué | Estado |
|---|---|---|---|
| **Réplica del cuaderno n.º 13 quemado** (Toynk, exclusiva; 80 páginas de raya ancha; 8 × 6 pulgadas, unos 20 × 15 cm; según la ficha, **la firma de All Might va en la contraportada** y hay un dibujo de Deku dentro) | [Amazon](https://www.amazon.com/Toynk-Academia-Notebook-Midoriya-Exclusive/dp/B07ZJ7627Z) | **Medidas, portada y quemado**: la mejor referencia para Blender | ✅ existe |
| **Réplica del cuaderno n.º 9**, «verde» | [Amazon.sa](https://www.amazon.sa/-/en/Academia-Notebook-Midoriya-Analysis-80-Page/dp/B07ZJ6J32K) | Indica que **cada número tiene su color** ⚠️ | ✅ existe |
| **Bolso con funda «cuaderno de Deku»** (oficial japonés, reproduce **dibujos hechos por Deku**) | [heroaca.com](https://heroaca.com/goods/sundries/23291/) · [Dengeki Online](https://dengekionline.com/article/202506/44638) | Páginas interiores dibujadas | ✅ existe; sin ver ⚠️ |
| **Mini figura acrílica** con motivo del cuaderno | [heroaca.com](https://heroaca.com/goods/sundries/23293/) | Idem | ⚠️ |
| **Llavero cuaderno de Deku** (Hot Topic) | [Hot Topic](https://www.hottopic.com/product/my-hero-academia-deku-hero-analysis-notebook-key-chain/12771317.html) | Portada en pequeño | ⚠️ |
| Ficha del cuaderno en la wiki | [MHA Wiki](https://myheroacademia.fandom.com/wiki/Hero_Analysis_for_the_Future) | Datos: 13 cuadernos al empezar; del 1 al 12 se ven en el opening «THE DAY» y en el ep. 13.5; también apunta **diseños de traje, estrategias y técnicas** | ✅ (resumen de dos búsquedas) |

**Cómo es el cuaderno** (la portada, **vista** en el fotograma ~10:33 del
episodio 1 de Internet Archive, §2.4 ✅; el resto, de memoria ⚠️):
- **Libreta de espiral**, **lomo azul**, marca impresa «**Campos**» (así
  se lee en el fotograma), **título escrito a mano**: 将来の為のヒーロー分析
  («Análisis de héroes para el futuro») y **No. 13 subrayado** ✅.
- Esquina y borde **chamuscados** en negro y marrón; papel **ondulado** por
  el agua de la fuente.
- Dentro: páginas de **raya**, **letra diminuta y apretada**, dibujos de
  héroes a lápiz con **flechas y notas** alrededor, y **la firma de All
  Might** ocupando una página entera.

### 3.4 Lo que falta

- Portada del **Blu-ray de la serie TV, vol. 1**: sigue sin verse ⚠️
  (búsqueda en la wiki por «Blu-ray cover volume 1»: sólo sale la de la
  película, 3.5).
- ~~Arte de tarjetas de cuenta atrás~~: **encontrado** en la segunda
  pasada, docenas de ellas (3.5) ✅.
- Una página interior del cuaderno maquetada entera: no la vi ⚠️. Lo más
  cercano es la página «ALL MIGHT» del fotograma ~19:30 (§2.4).

### 3.5 Segunda pasada: arte oficial mirado en la wiki

Todo con tamaño real medido por la API de Fandom
(`prop=imageinfo`). Las URL exactas están en `referencias.json`. Las
imágenes de `static.wikia.nocookie.net` piden la cabecera
`Referer: https://www.fandom.com/`.

- **Key visuals de temporada** ✅: `Season 7 Izuku Midoriya.png`
  (2895×4096, «DEKU», fondo verde) y `Season 7 Ochaco Uraraka.png`
  (2896×4096, «URAVITY», fondo magenta). Pose de acción, cada uno con su
  color de marca.
- **10.º aniversario** ✅: `My Hero Academia 10th Anniversary Key Visual`
  (2640×3491): todo el reparto junto, en acción.
- **Pósters** ✅: `Season 7 Poster 1.png` (3029×2135), `Final Season
  Armored All Might.png` (3043×2151), `Final Season Poster 1/3/7`,
  `Season 4 Poster 1`, `Season 7 Trainees`.
- **Mosaico del reparto** ✅: `List of Characters-min.png` (4096×1512),
  todos en traje de héroe.
- **Singles y bandas sonoras** ✅: `Starmarker cover.png` (3885×3458),
  `Ours CD Cover.png` (3927×3500), la banda sonora de *World Heroes'
  Mission* (3000×3000), `North Wind` (2000×2000), `Miss you` (3371×3000).
- **Blu-ray** ✅: el de la película *World Heroes' Mission* (424×600).
- **Contraportadas de EE. UU.** (VIZ, tomos 1 a 33) ✅: cada una con un
  mini perfil del personaje y su recuadro de texto (hoja
  `vestuario_juegos_01.jpg`, celdas #465-480).
- **Cartones de cuenta atrás dibujados a mano** ✅: bocetos a rotulador
  firmados y fechados por el estudio para cada capítulo y fiesta
  («おかげさまで4周年!!», «HAPPY NEW YEAR 2020/2021/2026», «アニメこのあと
  すぐ!!» con los personajes en *chibi*, `Christmas 2021/2023/2024
  Sketch`, `Season 2/3/5 Teaser Sketch`, `Episode 42 … 170 Sketch`).
  Están en `arte_oficial_01.jpg` (#11-24).
- **Hojas de modelo del anime** ✅✅: `Izuku Midoriya Alpha/Beta/USJ/Gamma
  Costume Anime Design Sheet` (la Beta, 693×492, es el traje más visto),
  `Katsuki Bakugo Hero Costume Anime Design Sheet` (700×494), `Shoto
  Todoroki Beta Costume` (700×494, y una «Upgraded Beta» ya sombreada),
  `Ochaco Uraraka Hero Costume` (700×494), `Shota Aizawa Hero Costume
  (Anime)` (153×555), `Toshinori Yagi Golden Age Hero Costume (Anime)`
  (1124×1831), los **uniformes del 10.º aniversario** de los cuatro
  alumnos y `All Might Anime Expressions Design Sheet` (hoja de
  expresiones). Diez de ellas están juntas en `personajes_01.jpg`
  (#1-10).
- **Fichas tipo databook** en japonés: `Volume 7/8 (Team-Up Missions)
  Character` (2256×1772) ✅.
- **Videojuegos** ✅: key visuals de *All's Justice* (`arte_oficial_01.jpg`
  #34 y #43) y `My Hero One's Justice Cast Artwork` (1449×2048,
  `vestuario_juegos_01.jpg` #439). Ver §13.
- **Escenografía sin personajes** ✅: `Field Gamma`, `Field Omega`,
  `Ground Beta`, `Gym Gamma Outside`, `Development Studio Inside`,
  `Conference Room (Anime)`, `U.A. Main Building` (1920×1080).
- Los nombres Alpha, Beta, USJ y Gamma del traje de Deku son **nombres de
  archivo** de la wiki ⚠️: falta el texto que diga en qué arco sale cada
  uno.

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D (Sketchfab y otros)

| Modelo | Autor | Licencia | Para qué |
|---|---|---|---|
| [My Hero Academia **UA classroom**](https://sketchfab.com/3d-models/my-hero-academia-ua-classroom-b73f7ef0e095420d97489df7e0d08859) | **banabanaba** | **CC Attribution** (CC BY 4.0), «libre con crédito», publicado el 27-7-2023 ✅ (dos resúmenes de búsqueda) | **El aula 1-A entera**: sitio perfecto para la lámina |
| [My Hero Academia **classroom desk and chair**](https://sketchfab.com/3d-models/my-hero-academia-classroom-desk-and-chair-4e03d145808b46f6a3da68343f5d4c42) | **banabanaba** | **CC Attribution**, «libre con o sin crédito», 26-7-2023 ✅ | **El pupitre** donde va el cuaderno |
| [MHA U.A HighSchool](https://sketchfab.com/3d-models/mha-ua-highschool-c0b5eded8f944751b953d1617a84dedf) | tahabzr | **no la sé** ⚠️ | Mirar la fachada |
| [My Hero Academia Classroom](https://open3dlab.com/project/50dc7341-05fc-4139-9669-094501cfc4b9/) | (Open3DLab) | **no la sé** ⚠️ | Alternativa del aula |
| Colecciones: [EmoJay](https://sketchfab.com/EmoJay/collections/my-hero-academia-94132959f69549c0a0160be86ed72623), [Nerderon](https://sketchfab.com/Nerderon/collections/my-hero-academia-598871708abf4a6b8cc0301a6d4dbc76), [skywer](https://sketchfab.com/skywer/collections/my-hero-academia-mha-433cb5ed5cc94afa979246cb35c7d8a3), etiqueta [mha](https://sketchfab.com/tags/mha) | varios | cada uno la suya ⚠️ | Buscar más objetos |

**Crédito exacto** para los dos de banabanaba (CC BY):
«"My Hero Academia UA classroom" (https://skfb.ly/…) by banabanaba is
licensed under Creative Commons Attribution». El enlace corto `skfb.ly` no
lo vi: cópialo del botón de descarga ⚠️.

**Segunda pasada: licencias leídas en la API de Sketchfab**
(`api.sketchfab.com/v3/models/<uid>`), con autor y caras exactos ✅:

| Modelo | Autor | Licencia | Caras | Para qué |
|---|---|---|---|---|
| [My Hero Academia UA classroom](https://sketchfab.com/3d-models/none-b73f7ef0e095420d97489df7e0d08859) | banabanaba | CC BY | 57 286 | El aula 1-A entera ✅ |
| [classroom desk and chair](https://sketchfab.com/3d-models/none-4e03d145808b46f6a3da68343f5d4c42) | banabanaba | CC BY | 3 714 | El pupitre del cuaderno ✅ |
| [Katsuki_Bakugo_Hero](https://sketchfab.com/3d-models/none-cc8fcd2f64784f9292a279ef4a670ac9) | 20062020year | CC BY | 29 428 | Bakugo en traje |
| [Todoroki shoto hero traje beta](https://sketchfab.com/3d-models/none-4ce1f840a18646a6bb85a18264dadafb) | victordavi1606 | CC BY | 70 678 | Todoroki en traje |
| [Ochaco_Uraraka giggle](https://sketchfab.com/3d-models/none-9946350617474ab5a519c8c5b940d6cd) | Dhext3r | CC BY | 68 377 | Uraraka riéndose, animada |
| [Aizawa](https://sketchfab.com/3d-models/none-557993be57a04b0cad5e4c0010fe5ed6) | vitgabi89 | CC BY | 217 038 | Aizawa, muy detallado |
| [All Might: The number one hero!](https://sketchfab.com/3d-models/none-ab3d819d719745a0a0bde8b9de05daa0) | Phan21 | CC BY | 11 034 | All Might en pose heroica |
| [Mirko](https://sketchfab.com/3d-models/none-de9ac30d334a4e3ba82fdcf3024f67b9) | Puzzle | CC BY | 738 242 | Secundaria muy querida |
| [Deku (Izuku Midoriya)](https://sketchfab.com/3d-models/none-7dee03930f074f2995191a1668a7c353) | (ver página) | **CC BY-NC** ⚠️ no comercial | 2 184 | Sólo referencia |

Crédito para los CC BY: `"<nombre del modelo>" (<enlace>) by <autor> is
licensed under Creative Commons Attribution`. Ojo: los marcados **«Free
Standard»** (p. ej. `Katsuki Bakugo (Gym Uniform)`) **no son Creative
Commons**: se bajan gratis, pero no dicen que se puedan reutilizar. Los
modelos **rigueados** para posar en Blender están en §18-a.

### 4.2 Fan art 2D (mirar, nunca pegar)

- **FoxyPawsz**, «Deku and His Notebook» (DeviantArt): Deku visto **desde
  arriba, estudiando su cuaderno**, con las notas legibles ⚠️ (descripción
  del resultado): [DeviantArt](https://www.deviantart.com/foxypawsz/art/My-Hero-Academia-BNHA-Deku-and-His-Notebook-874515961).
  Es exactamente el encuadre del concepto A.
- Etiquetas para buscar a mano: [pixiv #deku](https://www.pixiv.net/en/tags/deku),
  [DeviantArt #bokunoheroacademia](https://www.deviantart.com/tag/bokunoheroacademia).
- Hay gente que **se hace su propio cuaderno** y pregunta en Yahoo Japón
  cómo copiar una página (la de Kamui Woods) ✅
  ([Chiebukuro](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14299827084)):
  el cuaderno es un objeto que el fan **conoce página a página**.
- **Fan art mejor valorado en Safebooru**, con tamaño y enlace al autor
  original ✅ (`partes/datos-imagen.md`). Los mejores de cada uno:
  - All Might: [1768×2500](https://safebooru.org/images/2308/48ee249b6379989b667cc599eaa2089a9727e92a.jpg),
    de [pixiv 66186034](http://www.pixiv.net/member_illust.php?mode=medium&illust_id=66186034).
  - Bakugo: [764×1080](https://safebooru.org/images/2425/8c12b4596c1f0b53cfda7181154017ae7bb86a54.jpg),
    de [@SteamyTomatoes](https://twitter.com/SteamyTomatoes/status/988454678793932800).
  - Uraraka: [2250×3000](https://safebooru.org/images/4100/99df2234bb1710397ea2674974699648eb539b89.jpg),
    de [@khyleri](https://x.com/khyleri/status/1871224250125656117).
  - Todoroki: [2014×3021](https://safebooru.org/images/772/057b08c3fca7e46f939adb3acf18387276545832.jpg),
    de [@konsobastew](https://twitter.com/konsobastew/status/1618967069277528067).
  - Aizawa: [1638×2323](https://safebooru.org/images/3078/479988a0818ac755244aaf78224ac6548c6ba0f4.jpg),
    origen [@horikoshiko](https://twitter.com/horikoshiko/status/1884612079056998407)
    (puede ser la cuenta del propio autor: no lo comprobé ⚠️), y
    [4096×2843](https://safebooru.org/images/1088/40c36e9ca63aa0a2b7dc6f6ae7608c3a9a0566d0.jpg),
    de [@nagumoxdays](https://x.com/nagumoxdays/status/1897100663794098441).
  Sólo para mirar pose y composición.
- **Cosplay con licencia libre** (Openverse, autor **timz2011**, CC BY-NC-SA
  2.0) ✅: trajes de héroe de la 1-A, Kirishima, Hawks, All Might, Eri,
  Fatgum. Sirve para ver cómo cae la tela de verdad. Ejemplo:
  [Hero Uniforms, 1024×576](https://live.staticflickr.com/65535/51736046653_b2e51d408a_b.jpg).

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

| Sitio | Qué es | Dato comprobado |
|---|---|---|
| **Aula 1-A** de U.A. | Aula enorme, **puerta gigante** para alumnos grandes | «Qué puerta… ¿es para que pase cualquiera?» (ドア でか… バリアフリーか？), 1×05, 00:05:53 ✅. Modelo 3D CC BY en §4 |
| **Sala de profesores** | Donde Aizawa y Deku adulto charlan con una tele | 8×11, 00:13:26 a 00:15:19 ✅ (que sea la sala de profes lo digo de memoria ⚠️) |
| **Campo de U.A.** | Donde Aizawa hace la prueba de dones | 1×05, 00:09:07 ✅ |
| **Campo Beta** («グラウンド･β») | Edificios de mentira para el entrenamiento de combate | 1×06, 00:11:02 ✅ |
| **USJ** | Centro de simulacros de rescate | 8×11, 00:05:49 ✅ |
| **Playa municipal (Dagobah)** | Playa llena de basura que Deku limpia entrenando | 1×03, 00:06:35 y 00:07:19 ✅ |
| **Estatua de All Might** | Donde los chicos van a preguntarle si podrán ser héroes | 8×11, 00:16:51 ✅ |
| **Casa de Yaoyorozu** | Con **auditorio** propio para el grupo de estudio | 2×21, 00:05:00 ✅ |
| **Cuarto de Deku** | Lleno de cosas de All Might ⚠️ (de memoria) | — |

### 5.2 Luz ⚠️ (de memoria; compruébala en el fotograma)

- **U.A. de día**: luz blanca y limpia, cielo azul intenso con nubes
  grandes, cristal que refleja. Es la luz de «clase».
- **Aula 1-A**: ventanales a un lado, luz de mañana que entra en diagonal
  sobre los pupitres.
- **Playa (ep. 3)**: amanecer naranja, contraluz, el mar detrás. Es la luz
  de «me esfuerzo».
- **All Might**: siempre con **sombras duras y negras** en los ojos (estilo
  cómic americano). Los personajes lo comentan: «¡Su estilo de dibujo es
  totalmente distinto!» (1×01, 00:19:11 ✅) y Ojiro: «Tiene un estilo tan
  distinto que me da escalofríos» (1×06, 00:10:26 ✅).

**Luz medida en la segunda pasada** (`estilo.py` sobre fotogramas reales,
no de memoria) ✅:

| Sitio | Fotograma | Paleta medida | Luz |
|---|---|---|---|
| **Tejados de la ciudad, de día** | OP2 «Peace Sign», 0:06 ([Dailymotion x5pk6h7](https://www.dailymotion.com/video/x5pk6h7)) | `#406D84` 32% · `#B0E2F1` 19% · `#1F2630` 18% · `#76B1C9` 14% | Azul gris diurno, cielo claro, edificios oscuros a contraluz |
| **Campo de noche** | ED1 «HEROES», 0:24 ([Internet Archive](https://archive.org/details/my-hero-academia-ending-1-heroes)) | `#0B0D25` 46% · `#10153B` 23% · `#050614` 14% · `#1B2356` 13% | Azul marino casi negro, estrellas blancas, brillo muy bajo |
| **Estadio del Festival Deportivo** | 2×09 (ep. 22), clip 4:30 ([x6soboa](https://www.dailymotion.com/video/x6soboa)) | `#1E3A95` 26% · `#453C3F` 22% · `#1C1B43` 22% · `#E0E8F0` 11% | Azul intenso de gradas y carteles, gris piedra, cielo despejado |
| **Cúpula del USJ tras el golpe** | 1×12, clip 0:09 ([x4hptj4](https://www.dailymotion.com/video/x4hptj4)) | `#170D0A` 23% · `#4D342B` 18% · `#888076` 14% | Negro óxido sin azul, luz de incendio naranja y rasante |

En los cuatro: **pintado con degradado y poca línea**, línea gris
parda `#635C58` a `#67676C`.

### 5.3 Paleta (aproximada ⚠️)

Primera pasada: valores **de memoria**. Para la **ropa**, usa los hex
**medidos** de §16; para la **luz**, la tabla de arriba. Lo que siga sólo
aquí, mídelo con el cuentagotas antes de usarlo:

| Qué | Hex aproximado |
|---|---|
| Pelo de Deku (verde oscuro) | `#1F4A3C` con brillos `#3C7A63` |
| Traje de Deku (verde) | `#2E6B55` |
| **Zapatillas rojas de Deku** | `#D0312D` |
| Americana del uniforme U.A. (gris) | `#A9ADB3` |
| Solapas y pantalón del uniforme (verde oscuro) | `#23473F` |
| Corbata del uniforme (roja) | `#C6352E` |
| Pelo de All Might (amarillo) | `#F4D04A` |
| Traje de All Might (azul / rojo) | `#2C4FA3` / `#D63B33` |
| Pelo de Bakugo (rubio ceniza) | `#EFE3B5` |
| Ojos de Bakugo | `#C42F2A` |
| Todoroki: mitad blanca / mitad roja | `#EDEDED` / `#C6463A` |
| Uraraka: pelo / mejillas | `#6A4A3A` / `#F2A4A0` |
| Aizawa: ropa / bufanda de captura / gafas | `#1C1C1F` / `#B8B6AE` / `#F0D13A` |
| Amarillo de la portada del tomo 1 y del 42 | `#F7D117` ⚠️ |

### 5.4 Texturas reales equivalentes

| Para | Textura | Licencia |
|---|---|---|
| Hojas del cuaderno | [ambientCG Paper 001](https://ambientcg.com/view?id=Paper001), [Paper 003](https://ambientcg.com/view?id=Paper003), [Paper 005](https://ambientcg.com/view?id=Paper005), [Paper 006](https://ambientcg.com/view?id=Paper006) | **CC0** ✅ ([ambientCG](https://ambientcg.com/)) |
| Más papeles | [ambientCG, categoría Paper](https://ambientcg.com/list?sort=Popular&category=Paper) | CC0 |
| Madera del pupitre | Poly Haven, texturas de madera | **CC0** ✅ (resumen de búsqueda) |
| Quemado del borde | No encontré una textura libre de papel quemado ⚠️: hacerlo en Blender con una máscara de ruido y un degradado negro-marrón-naranja | — |
| Hormigón roto (cúpula del USJ, escombros) | [ambientCG Concrete044D](https://ambientcg.com/view?id=Concrete044D) y [Concrete042C](https://ambientcg.com/view?id=Concrete042C), 2048×2048 | **CC0** ✅ (API de ambientCG) |

Las texturas **2D** (tramas de manga, tartán, emblemas) están en §18-b.

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

- **Logo**: rótulo hecho a medida. En inglés se parece a **Futura
  Display** (de pago) salvo la «M» ⚠️ (resumen de
  [dafont](https://www.dafont.com/forum/read/249632/my-hero-academia-font)
  y [Font Meme](https://fontmeme.com/my-hero-academia-font/)). Los tomos
  lo ponen en **rojo y blanco** sobre amarillo ✅.
- **Onomatopeyas en inglés** dentro del manga japonés: «SMASH» (lo dice
  el propio análisis de [Real Sound](https://realsound.jp/book/2020/06/post-567881_2.html),
  junto a «sidekick» y «villain») ✅. Horikoshi mezcla **manga y cómic
  americano**.
- **Los nombres de los golpes** van en inglés en pantalla: «TEXAS SMASH»
  (1×01, 00:17:49), «DETROIT SMASH» (1×02, 00:16:45) ✅ (así los escribe el
  subtítulo).
- La letra del **globo del manga** en la edición inglesa de VIZ: no
  encontré qué fuente usa ⚠️.
- **La letra de Deku** en el cuaderno: a mano, pequeña, apretada ⚠️. En
  la página «ALL MIGHT» (1×01, ~19:30 de Internet Archive) escribe **en
  mayúsculas enormes** ✅: dos tamaños, apunte diminuto y título gritado.
- **Rótulo «PLUS ULTRA ver.»** (logo de *The «Ultra» Stage*, 767×421, en
  la wiki) ✅ visto: letras 3D de cómic **azul, rojo y blanco**, relleno
  con degradado, y encima en japonés «本物の英雄» («héroe de verdad»). Es
  la mejor referencia para un título del canal en estilo héroe.

### 6.2 Letras libres comprobadas por mí

Bajadas de [google/fonts](https://github.com/google/fonts) y revisadas con
fontTools, carácter por carácter:

| Para | Letra | Licencia | á é í ó ú ñ ¿ ¡ | Japonés |
|---|---|---|---|---|
| **Letra de Deku** (apuntes) | **Caveat** (variable, 400-700) | OFL | ✅ todas | no |
| Letra de Deku, más redonda | **Kalam** | OFL | ✅ | no |
| Apuntes rápidos, más infantil | Patrick Hand · Gochi Hand · Schoolbell · Just Another Hand | OFL / Apache | ✅ | no |
| Rotulador grueso (portada del cuaderno) | **Permanent Marker** | Apache | ✅ | no |
| Título japonés a mano (将来の為のヒーロー分析) | **Yomogi** · Zen Kurenaido · **Klee One** | OFL | ✅ | **sí** |
| **Rótulo de cómic** («SMASH», «PLUS ULTRA») | **Bangers** · Luckiest Guy · Titan One | OFL / Apache | ✅ | no |
| Onomatopeya japonesa gorda | **Dela Gothic One** · Rampart One · Reggae One | OFL | ✅ | **sí** |
| **Parecida al logo** (Futura Display) | **Jost** (hasta 900) · **League Spartan** (hasta 900) | OFL | ✅ | no |
| Títulos condensados | Anton · Oswald · Bebas Neue | OFL | ✅ | no |
| Textos de interfaz redondos | M PLUS Rounded 1c · Zen Maru Gothic | OFL | ✅ | **sí** |

**Evitar**: Nanum Pen Script y Kosugi Maru **no traen tildes ni ñ** (lo
comprobé: les faltan á é í ó ú ñ ¿ ¡).

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que la serie pone en pantalla

1. **El cuaderno**. Es el «texto dentro del mundo» más reconocible: la
   voz de Deku escrita. El episodio 13.5 entero se llama **«Cuaderno de
   héroe»** ✅.
2. **La voz en off de Deku**. Casi todos los episodios la tienen: Deku
   narra en primera persona («Por la mañana, materias obligatorias…», 1×06,
   00:09:29 ✅). En la final, el adulto narra mientras **escribe** (8×11,
   00:09:58 ✅).
3. **El murmullo de Deku**: analiza en voz alta, sin respirar, frases
   largas encadenadas (1×01, 00:06:44 ✅; 8×11, 00:17:17 ✅, donde el chico
   le dice «Da miedo»). En una lámina: **letra pequeñísima en espiral o en
   bloque apretado** alrededor de la cabeza, como en el manga ⚠️ (el
   manga lo dibuja así de memoria).
4. **Las pizarras blancas**: en la clase de nombres de héroe, cada alumno
   **escribe su nombre en una pizarrita y la levanta** para presentarlo
   (2×13, 00:06:55 a 00:13:09 ✅ por el diálogo; la pizarra la describo de
   memoria ⚠️).
5. **Las tarjetas de All Might**: anuncia la clase levantando una tarjeta
   (1×06, 00:10:40, de memoria ⚠️) y la **chuleta** (カンペ) en la que lee
   las reglas (00:15:18 ✅).
6. **«PLUS ULTRA» en letras de cómic** y el **avance del episodio
   siguiente** que termina con el grito (✅ en los 13 subtítulos de la T1).
7. **Rótulos de golpe en inglés** («DETROIT SMASH») con estética de cómic
   americano ✅.
8. **La ficha de personaje de las contraportadas** (VIZ, tomos 1 a 33):
   mini perfil con retrato y un recuadro de texto propio ✅ (visto en
   `hojas/vestuario_juegos_01.jpg`, #465-480). Sirve de modelo para una
   ficha de «profesor» o de «alumno».
9. **Cartones dibujados a mano** a rotulador para anunciar cada capítulo
   («アニメこのあとすぐ!!») ✅ (§3.5): texto escrito a mano junto a los
   personajes, otra forma de hablar sin globo.

### 7.2 Cómo hablan (por el subtítulo)

- **Deku**: educado, «〜君», «〜さん» (Iida-kun, Uraraka-san); llama a
  Bakugo **«Kacchan»**; se atropella («こ… これ以上は ぼ ぼ…», 1×01 ✅);
  grita a pleno pulmón cuando se decide. De adulto, anima: «**¡Ánimo,
  jovencito!**» (8×11, 00:17:56 ✅).
- **All Might**: teatral, se ríe «¡Ah-ja-ja-ja!» (アーハッハッハッ, 1×03,
  00:13:45 ✅), llama a Deku **«jovencito»** (少年, 1×07, 00:14:10 ✅), se
  refiere a sí mismo como «este tío» (おじさん, 1×03, 00:13:39 ✅).
- **Aizawa**: seco, corto, sin exclamaciones. «**No es racional**»,
  «**mentira racional**», «**Es todo**» (以上だ, 2×21, 00:03:19 ✅).
- **Bakugo**: grita e insulta. «**¡Muere!**» (死ね, 1×05, 00:10:28 ✅; el
  propio Aizawa repite «¿Muere?»). «**Nerd de mierda**» está en el título
  del ep. 6 («猛れクソナード») ✅. De adulto sigue igual: a un chico que lo
  graba, «¿Te quieres morir?» (8×11, 00:13:36 ✅).
- **Uraraka**: acento de **Kansai** («なんとかなるんやな», 2×21, 00:06:06 ✅;
  «資料 まとめんと», No.170+1, 00:00:22 ✅). Llama a Deku «**Deku-kun**».
- **Todoroki**: frases cortas, literal. El meme: «¿Eres **hijo secreto de
  All Might** o algo?» (2×06 ep. 19, 00:03:52 ✅).

### 7.3 Cómo se traduce a una lámina fija

- **El texto del canal va escrito en el cuaderno**, con la letra de Deku
  (Caveat), como si fueran sus apuntes. Así **no hay burbuja**: hay papel.
- **La frase del personaje** va en **una hoja o una pizarrita que
  sostiene**, o en un **pósit** pegado al cuaderno. Nunca en un globo
  blanco flotando.
- Si hace falta un globo, que sea **de cómic americano**: rectángulo con
  borde negro grueso y rótulo en Bangers, como en *One's Justice* ✅ (§13).
- El título del canal puede ir en la **portada del cuaderno**, a rotulador
  (Permanent Marker), imitando «将来の為のヒーロー分析 No.13».

### 7.4 Qué NO hacer con el texto

- **Nada de burbuja blanca redonda** genérica.
- **No meter inglés en boca de All Might** si se dice «doblaje latino»:
  en latino **todo va traducido** ✅ (§10).
- No inventar frases «del doblaje» entre comillas. Las que **sí** están
  oídas en clips con audio latino van en §10 (segunda pasada): úsalas
  tal cual, p. ej. «**Puedes ser un héroe**» o «**¡Respeta, perdedor!**».
- No traducir los alias de héroe ni los «Smash»: el doblaje los deja en
  inglés (salvo Trece y Tigre) ✅ (§10).
- La letra de Deku es **pequeña y ordenada**, no de garabato: es un chico
  muy aplicado.

---

## 8 · Los personajes

Orden: primero los del encargo. Lo que no lleva ✅ con minuto o fuente es
de memoria ⚠️.

### Izuku Midoriya «Deku» — el protagonista, 2.º en votos ✅

- **Aspecto**: pelo **verde oscuro rizado**, pecas, ojos grandes verdes.
  **Zapatillas rojas** grandes. Desde la T2, cicatrices en la mano derecha
  ⚠️. De adulto (8×11 y cap. 430): **traje y corbata**, profesor ✅ (el
  traje lo dice [Popverse](https://www.thepopverse.com/comics-my-hero-academia-ending-explained-mha-chapter-430-deku-all-might-bakugo-shoto)
  y el resumen de búsqueda del cap. 430).
- **Carácter**: nació **sin don** («無個性») en un mundo donde casi todos
  tienen uno; All Might le pasa el suyo. Llorón, obsesivo, estudioso,
  valiente sin pensar («el cuerpo se movió antes de pensar», 1×02 ✅).
- **Qué le importa**: ser un héroe «que salva con una sonrisa», como All
  Might (1×03, 00:13:14 ✅). Al final: **«Después de cumplir tu sueño, te
  toca dar sueños»** (8×11, 00:17:34 ✅).
- **Con quién**: All Might (maestro), Bakugo (rival de la infancia),
  Uraraka e Iida (amigos), Todoroki.
- **Cómo se expresa**: murmura análisis; tartamudea si está nervioso;
  se emociona con los héroes como un fan; **anota todo**.
- **Como profesor** (lo más útil para este canal): «Hacer de héroe con la
  armadura y dar clase **me importan igual**»; «aunque me quedara One For
  All, creo que habría pensado **“ser profe está bien”**» (No.170+1,
  00:09:51 a 00:10:07 ✅). En el coche, contento: «**Pude terminar el plan
  para desarrollar el don de cada alumno**» (00:08:02 ✅): **está
  preparando su material de clase**.

### All Might (Toshinori Yagi) — el maestro

- **Dos cuerpos**: el **musculoso** (rubio con dos mechones de antena,
  sonrisa enorme, sombras duras) y el **real**, flaco y enfermo ✅ (los dos
  vistos en el episodio 1, ~13:06 y ~19:55 de Internet Archive, §2.4).
- **Como profe**: novato, **lee de una chuleta** (1×06, 00:15:18 ✅; 1×12,
  00:07:01 ✅). Entra en clase gritando «¡Ya estoy aquí!» (1×06, 00:10:09
  ✅). Da **Formación básica de héroes**, «la materia con más créditos»
  (00:10:37 ✅). Hace planes de entrenamiento a medida y **los ajusta**
  (1×03 ✅).
- **Traje en clase**: el de la «**Edad de Plata**» (lo dice Tsuyu, 1×06,
  00:10:22 ✅).
- **Cómo habla**: teatral, risa «¡Ah-ja-ja-ja!», «jovencito», palabras en
  inglés en japonés (en latino, traducidas ✅).
- En la final regala a Deku la **armadura** pagada por la antigua 1-A
  (8×11, 00:18:36 a 00:19:08 ✅).

### Katsuki Bakugo — el más querido, 1.º en votos ✅

- **Aspecto**: pelo **rubio ceniza en pinchos**, ojos rojos, ceño
  fruncido, **manos en los bolsillos** ⚠️, **guanteletes de granada**
  verdes ✅ (hoja de modelo, `personajes_01.jpg` #3).
- **Carácter**: orgulloso, agresivo, genio de la pelea y **muy buen
  estudiante** (ep. 34: se ofrece a enseñar ✅). Con el tiempo aprende a
  respetar a Deku.
- **Nombre de héroe**: «**Gran Explosión Asesina Dios Dynamight**»
  (大･爆･殺･神ダイナマイト, 8×11, 00:11:56 ✅).
- **Cómo habla**: gritos, insultos, amenazas («¡Muere!», «¿Te quieres
  morir?»). Llama a Deku «Deku». Pero cuando enseña, **enseña**:
  «**¡Te voy a enseñar hasta matarte!**» (2×21, 00:05:36 ✅).
- **De adulto**: tiene coche nuevo y se enfada si le ensucian la tapicería;
  entró en el ranking de héroes en el **n.º 4** y cayó al **n.º 15** porque
  **todos sus ayudantes renunciaron llorando** (No.170+1, 00:08:46 a
  00:09:12 ✅). **Da charlas en U.A. como profesor invitado**: Aizawa quiere
  que dé «**Introducción a la comunicación**», y él: «¡No me llames como
  mal ejemplo!» (00:18:31 a 00:18:38 ✅). **Es el chiste perfecto para este
  canal.**

### Shoto Todoroki — 3.º en votos ✅

- **Aspecto**: pelo **mitad blanco (derecha) y mitad rojo (izquierda)**,
  **cicatriz de quemadura** alrededor del ojo izquierdo ✅ (hojas de modelo,
  `personajes_01.jpg` #5-6), ojos de dos colores (etiqueta
  `heterochromia` en Danbooru ✅).
- **Carácter**: serio, callado, algo despistado; hijo de Endeavor. Deku le
  grita en el Festival: «**¡Es TU poder!**» (君の！力じゃないか！, 2×10
  ep. 23, 00:16:44 ✅).
- **Cómo habla**: poco y literal. «Si atiendes a clase **no suspendes**»
  (2×21, 00:04:10 ✅), y le dicen «cuidado con lo que dices».
- **De adulto**: héroe de primera fila, fan service «torpe pero sin
  distinciones» (8×11, 00:13:57 ✅).

### Ochaco Uraraka

- **Aspecto**: melena castaña, **mejillas rosadas redondas**, almohadillas
  en las yemas ⚠️.
- **Carácter**: alegre, práctica; quiere ser héroe **para ganar dinero y
  ayudar a sus padres** (2×01 ep. 14, 00:16:17 a 00:17:33 ✅). Le gusta el
  nombre «Deku» porque suena a «¡tú puedes!» (1×06, 00:08:48 ✅).
- **Cómo habla**: acento de Kansai ✅. «Deku-kun».
- **De adulta**: dirige un **plan de orientación sobre los dones** para
  niños; explica a su equipo: «**No se fíen demasiado de los papeles**»
  (資料に頼りすぎず, No.170+1, 00:03:22 ✅) y «lo más importante es la
  **comunicación**» (00:03:01 ✅). El subtítulo no marca quién lo dice;
  por el contexto es ella ⚠️.

### Shota Aizawa «Eraser Head» — el profesor, 4.º en votos ✅

- **Aspecto**: pelo negro largo y revuelto, barba de días, **ojeras**,
  ropa negra, **bufanda de captura** gris, **gafas amarillas**; duerme en un
  **saco de dormir amarillo** ✅ (resumen de búsqueda: hasta Funko lo vende
  así).
- **Carácter**: el tutor de 1-A. Creado por Horikoshi como alguien que
  **decide todo con lógica** y no cuida las formas ✅ (resumen de la
  [wiki](https://myheroacademia.fandom.com/wiki/Shota_Aizawa)). Estricto
  pero **protege a sus alumnos**; el fandom lo llama «**Dadzawa**» ✅ (resumen de
  búsqueda sobre [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Memes/MyHeroAcademia)
  y [Know Your Meme](https://knowyourmeme.com/memes/subcultures/my-hero-academia)). Le gustan **los gatos** ✅.
- **Cómo habla**: «**No es racional**», «**mentira racional**», «La clase
  termina aquí… **Es todo**» (✅, ver §2.2). Nunca sube el tono.
- **Aizawa ocho años después** (8×11 y cap. 430): **parche negro en el ojo
  derecho**, **pierna derecha ortopédica** y el pelo **más corto**, hasta
  media cara y con raya a la derecha ✅ (resumen de la
  [wiki](https://myheroacademia.fandom.com/wiki/Shota_Aizawa) y
  [ComicBook.com](https://comicbook.com/anime/news/my-hero-academia-reveals-aizawas-post-surgery-state/)).
  **Si sale con Deku adulto, tiene que llevar el parche.**
- **Con Deku adulto**: le aconseja «**sé más estricto con tus alumnos**» y
  Deku le responde que él era «bastante amable» (8×11, 00:14:58 a 00:15:19
  ✅). Es la escena **profe veterano + profe nuevo**.

### Los secundarios que conviene tener a mano

- **Present Mic**: profe de inglés, grita «**Everybody hands up!**» (1×06,
  00:09:43 ✅). En la graduación presenta todo como DJ (8×11, 00:07:57 ✅).
- **Midnight**: profe que califica los **nombres de héroe** (2×13 ✅).
- **Momo Yaoyorozu**: la empollona generosa que monta **grupo de estudio**
  con té (2×21 ✅).
- **Tenya Iida**: delegado de clase, manos que cortan el aire ⚠️; da el
  **discurso de graduación** (8×11, 00:08:44 ✅).
- **Kota**: el niño del campamento, ya **alumno de Deku** (8×11, 00:05:41
  ✅).

### Segunda pasada: perfiles oficiales (*databooks*)

De los perfiles de los tomos 1 y 2 y del *Ultra Analysis*, citados en la
wiki en inglés con su tomo ✅:

- **Deku**: «tímido, educado, reacciona con expresiones exageradas».
  Horikoshi lo diseñó **a propósito para verse “plano”**.
- **All Might**: sonríe siempre porque su mentora **Nana Shimura** le
  enseñó que «**los que sonríen son los más fuertes**». En su forma real
  se pone serio y evita la atención.
- **Bakugo**: en el primer boceto iba a ser **amable**; Horikoshi lo hizo
  desagradable porque le pareció aburrido.
- **Todoroki**: el *Ultra Analysis* lo llama «**un idiota frío y
  caliente**» (*cool and hot airhead*).
- **Uraraka**: reacciones «exageradas y graciosas, se ríe y trata de
  contenerlo»; Horikoshi la define como «**honesta**».
- **Aizawa**: «en el fondo, **muy consentidor**» (*actually kind of
  doting*) cuando decide cuidar de alguien. Bebe en reuniones y **se pone
  dormilón**.

### Segunda pasada: su cara en cada emoción (fotograma y minuto)

| Personaje | Emoción | Minuto y enlace | Qué se ve |
|---|---|---|---|
| Deku | Miedo | [x7xksc8, 0:08](https://www.dailymotion.com/video/x7xksc8?t=8) | Ojos y boca muy abiertos, junto a Kota, girado hacia el peligro ✅ |
| Deku | Rabia fuera de control | [x7xksc8, 0:56](https://www.dailymotion.com/video/x7xksc8?t=56) | Sonrisa torcida, **ojo derecho inyectado en rojo**: el «Deku berserker» ✅ |
| Deku | Súplica, nervios | Ep. 1, ~10:55 (Internet Archive) | Puños al pecho, hombros encogidos ✅ |
| All Might musculoso | Alivio, calidez | [x618t31, 0:12](https://www.dailymotion.com/video/x618t31?t=12) | Sonrisa enorme, pecho adelante, cerezos detrás ✅ |
| All Might flaco | Ternura, consejo | [x7xktih, 2:43](https://www.dailymotion.com/video/x7xktih?t=163) | Silueta a contraluz del atardecer, calle con cerezos ✅ |
| Bakugo | Rabia pura | [x7xktih, 0:17](https://www.dailymotion.com/video/x7xktih?t=17) | Primer plano cerrado, un ojo en sombra, dientes, luz amarilla a contraluz: **la cara de los memes** ✅ |
| Todoroki niño | Rabia, esfuerzo | [x7xkvbk, 1:00](https://www.dailymotion.com/video/x7xkvbk?t=60) | Dientes apretados, cejas bajas ✅ |
| Todoroki | Determinación | [x7xkvbk, 2:40](https://www.dailymotion.com/video/x7xkvbk?t=160) | Media cara iluminada por el fuego, ceja fruncida ✅ |
| Todoroki | Confianza | [x6tcw9u, 0:00](https://www.dailymotion.com/video/x6tcw9u) (3×01, ep. 39) | Brazo cubierto de hielo estirado, mirada de reojo, media sonrisa ✅ |
| Aizawa | Regañar | [x6tcw9u, 0:20](https://www.dailymotion.com/video/x6tcw9u) | **Ojos rojos brillantes**, boca en línea, cuello de la bufanda subido: «Did you say something?» ✅ |
| Uraraka | Decisión | [x6soboa, 5:30-6:00](https://www.dailymotion.com/video/x6soboa) | Puño al pecho, ojos llorosos de determinación ✅ |
| Rei Todoroki | Colapso | [x7xkvbk, 0:20](https://www.dailymotion.com/video/x7xkvbk?t=20) | De espaldas junto a la tetera, hombros caídos ✅ |

Faltan **tristeza** y **vergüenza** con fotograma en todos ⚠️: no salieron
en los clips cortos. Para Aizawa hay además `Shota_personality.png`
(`personajes_01.jpg` #14): su **sonrisa forzada**, inquietante.

---

## 9 · ¿Quién es el más querido?

**Bakugo**, sin duda ✅.

| Encuesta | 1.º | 2.º | 3.º | 4.º | 5.º | Fuente |
|---|---|---|---|---|---|---|
| **WORLD BEST HERO** (mundial, 2024, **6,12 millones de votos**) | **Bakugo** | Deku | Todoroki | **Aizawa** | Kirishima | [Crunchyroll](https://www.crunchyroll.com/news/latest/2024/12/2/my-hero-academia-world-best-hero-results) + [AnimeTV](https://x.com/animetv_jp/status/1863539827863396403) + [Siliconera](https://www.siliconera.com/my-hero-academia-world-best-hero-top-100-characters-ranked/) ✅ |
| 1.ª de Jump | Deku | Todoroki | Bakugo | Uraraka | All Might | [Tencent](https://view.inews.qq.com/a/ACF2018112301275802) ⚠️ |
| 2.ª | Bakugo | Deku | Todoroki | **Aizawa** | Kirishima | ídem ⚠️ |
| 3.ª | Bakugo | Deku | Todoroki | Kirishima | Iida | ídem ⚠️ |
| 4.ª | Bakugo | Todoroki | Deku | Hawks | Kirishima | ídem ⚠️ |
| 6.ª (57 928 votos) | Bakugo (14 937) | Deku (8115) | Todoroki (6524) | Iida (3722) | — | [Facebook heroyaoya](https://www.facebook.com/heroyaoya/posts/%E6%88%91%E7%9A%84%E8%8B%B1%E9%9B%84%E5%AD%B8%E9%99%A2%E7%AC%AC%E5%85%AD%E5%9B%9E%E8%A7%92%E8%89%B2%E4%BA%BA%E6%B0%A3%E6%8A%95%E7%A5%A8%E7%B5%90%E6%9E%9C%E7%99%BC%E8%A1%A8%E7%B8%BD%E6%8A%95%E7%A5%A8%E6%95%B857928%E7%A5%A81-%E7%88%86%E8%B1%AA%E5%8B%9D%E5%B7%B1-14937%E7%A5%A82-%E7%B6%A0%E8%B0%B7%E5%87%BA%E4%B9%85-8115%E7%A5%A83-%E8%BD%9F%E7%84%A6%E5%87%8D-6524%E7%A5%A84-%E9%A3%AF%E7%94%B0%E5%A4%A9%E5%93%89-3722%E7%A5%A85-%E7%9B%B8/3757848944294690/?locale=zh_CN) ⚠️ |
| 2024 (Jump n.º 19) | Bakugo (23 441) | Deku (18 488) | Todoroki (13 478) | — | — | [IMDb News](https://www.imdb.com/news/ni64527283/): **anulada** por errores; la editorial pidió perdón ✅ |

Bakugo gana **desde la 2.ª encuesta** ✅ (resumen de fuentes chinas y de
la mundial). En la mundial, **Deku ganó sólo en Europa** ✅ (resumen de
Crunchyroll).

**Para este canal**: Bakugo es el más querido, pero el canal va de
**profesores**. **Aizawa (4.º mundial)** es el profesor más querido y
supera a All Might, que no entra en el top 10 ✅. La combinación que más
gusta: **Deku-profesor + Bakugo de invitado**, o **Aizawa**.

---

## 10 · Doblaje latino

> [!warning] Hay DOS doblajes latinos, y no hay que mezclarlos
> 1. **La serie** (Funimation, luego Crunchyroll): estudio **The Kitchen**,
>    **Miami**, con voces de varios países. Es el que ven casi todos.
> 2. **Las dos primeras películas** en cine (*Dos héroes*, 2018, y *El
>    despertar de los héroes*): **doblaje mexicano** en **Koe Dubbing
>    Masters**, dirigido por **Gabriel Gama**, con **otras voces**.
>
> Si la lámina cita una frase «del doblaje», que sea de la **serie**.

### 10.1 La serie (The Kitchen, Miami)

Doblaje Wiki no se pudo abrir (ni la web ni la API). Cada nombre sale de
**dos fuentes distintas** que vi en los resultados de búsqueda:

| Personaje | Voz latina | Fuentes | Estado |
|---|---|---|---|
| **Izuku Midoriya (Deku)** | **Sebastián Gabriel Reggio** | resumen de [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/My_Hero_Academia) + tuit de [ANMTV](https://x.com/ANMTVLA/status/1587072629755764740) («Deku- @SebastianReggio») + [Código Espagueti](https://codigoespagueti.com/noticias/anime/my-hero-academia-quien-hace-doblaje-pelicula-world-heroes-mission/) | ✅ |
| **Katsuki Bakugo** | **Rómulo A. Bernal** | Doblaje Wiki + tuit de ANMTV («Bakugo- @Dr0mz») | ✅ (que @Dr0mz sea Rómulo Bernal lo deduzco: los dos datos dicen que es Bakugo **y** director ⚠️) |
| **All Might** | **Orlando Noguera** (venezolano, en Miami desde 2004) | Doblaje Wiki + [Código Espagueti](https://codigoespagueti.com/noticias/anime/my-hero-academia-quien-hace-doblaje-pelicula-world-heroes-mission/) + [TikTok](https://www.tiktok.com/@esamalvaroz/video/7358316188813905158) | ✅ |
| **Shoto Todoroki** | **Juan Felipe Sierra Cortés** (colombiano, en Miami) | [IMDb](https://www.imdb.com/title/tt13544716/characters/nm6960683/) + [Código Espagueti](https://codigoespagueti.com/noticias/cultura/revelan-quien-sera-la-voz-de-todoroki-en-el-doblaje-latino-de-my-hero-academia/) + entrevista en [Spotify](https://open.spotify.com/episode/3BjOFDN9mi0krz32fTODVe) | ✅ |
| **Ochaco Uraraka** | **Andrea Valentina Villaverde** (T1 a T6 ep. 1, es decir hasta el ep. 114) | Doblaje Wiki (su ficha y la de la serie) | ⚠️ una sola familia de fuentes |
| **Ochaco Uraraka** | **Sofía Baltazar** (desde T6) | tuit de ANMTV («Uravity- Sofía Baltazar») + Doblaje Wiki | ✅ |
| **Shota Aizawa** | **Ernesto Rumbaut** (Miami) | [Doblaje Wiki: Ernesto Rumbaut](https://doblaje.fandom.com/es/wiki/Ernesto_Rumbaut) + [Behind The Voice Actors](https://www.behindthevoiceactors.com/characters/My-Hero-Academia/Eraser-Head-Shota-Aizawa/) | ✅ |
| **Tenya Iida** | **Luis Carreño** | tuit de ANMTV («Iida- @luiscarreno1») | ⚠️ una fuente |
| **Burnin** | **Gigliola MC** | tuit de ANMTV | ⚠️ una fuente |
| **Hanta Sero** | **Braulio Hernández**, luego **Mauricio Del Valle** (T6) | resumen de Doblaje Wiki | ⚠️ |
| **Yuga Aoyama** | **Hernán Chavarro**; en T8, **Ignacio Ortuondo** | resumen de Doblaje Wiki | ⚠️ |

Datos de producción:
- **Aizawa tuvo otra voz al principio**: Eduardo Wasveiler en la T1. Por la
  pandemia no pudo grabar en persona y **Ernesto Rumbaut volvió a doblar
  todas sus líneas** ⚠️ (resumen de Doblaje Wiki). Un resumen de búsqueda
  dijo «José Arenas» para Aizawa: **no lo pude confirmar** y choca con lo
  anterior. Usa **Rumbaut**.
- Funimation encargó unas **pruebas**; al elegir a The Kitchen pidió
  **conservar** a Reggio (Deku), Bernal (Bakugo) y Noguera (All Might) ✅
  (Doblaje Wiki y Wikipedia, en dos resúmenes).
- Desde la **T3** parte de las voces se grabaron en **Los Ángeles y Chile**
  ⚠️.
- **Temporada 6**: Crunchyroll la estrenó doblada el **22 de octubre de 2022**
  ✅ ([Crunchyroll](https://www.crunchyroll.com/es/news/latest/2022/10/22/latinoamrica-el-doblaje-de-my-hero-academia-vuelve-con-su-sexta-temporada)
  + tuit de ANMTV). **Dirección: Rómulo Bernal** ✅.
- **Temporada 8 (final)**: doblada del **8 de noviembre de 2025 al 17 de
  enero de 2026**, en The Kitchen, **dirigida por Rómulo Bernal** ⚠️
  (resumen de [Doblaje Wiki, 8.ª temporada](https://doblaje.fandom.com/es/wiki/My_Hero_Academia/8%C2%AA_temporada)).
- **Película 4, *Ahora es tu turno*** (cines, 10 de octubre de 2024):
  mismo reparto de la serie; **3DJuegos** dice que se dobló en **VSI
  Ciudad de México** con **Gina Sánchez** de directora ⚠️ (una fuente:
  [3DJuegos](https://www.3djuegos.lat/anime/my-hero-academia-estos-seran-actores-doblaje-espanol-latino-para-pelicula-ahora-tu-turno)).
- En abril de 2026 hubo un panel de los actores en **CCXP México** ⚠️
  ([Reporte Índigo](https://geek.reporteindigo.com/editorial/my-hero-academia-secretos-ccxp-2026-20260424-0005.html)).

### 10.2 Las películas 1 y 2 (doblaje mexicano)

| Personaje | Voz | Fuentes | Estado |
|---|---|---|---|
| Deku | **Héctor Mena** | [Canal 5](https://www.televisa.com/canal5/anime/my-hero-academia-tendra-doblaje-latino) + [Cine Premiere](https://cinepremiere.com.mx/elenco-doblaje-academia-dos-heroes-perro.html) | ✅ |
| Bakugo | **Rafael Escalante** | las mismas dos | ✅ |
| Todoroki | **José Gilberto «Pepe» Vilchis** | las mismas dos | ✅ |
| All Might | **Octavio Rojas** (Smithers de *Los Simpson*, Shifu de *Kung Fu Panda*) | Canal 5 + [La Crónica](https://www.cronica.com.mx/escenario/2025/03/20/octavio-rojas-y-el-arte-de-entender-a-los-personajes-para-doblar-su-voz/) + podcast [Bastardos del Anime](https://www.spreaker.com/episode/octavio-rojas-la-voz-de-all-might-en-boku-no-hero-punohiroakademia-desde-la-comic-convention-lima-2021--47989785) | ✅ |

Estudio **Koe Dubbing Masters México**, dirección **Gabriel Gama** ⚠️
(un resumen de búsqueda). Hay un vídeo que compara las voces de All Might
(Octavio Rojas, Juan Guzmán y Orlando Noguera):
[YouTube](https://www.youtube.com/watch?v=viK_ZyDu8hc) (no se pudo abrir;
no sé quién es Juan Guzmán en esto ⚠️).

### 10.3 Cómo suena en latino (lo que se sabe)

- **All Might no mezcla inglés**: en japonés suelta palabras en inglés,
  pero en el doblaje **todo va traducido** ✅ (resumen de Doblaje Wiki, y
  la guía de cuadros de diálogo del repositorio). Ojo: los golpes
  («**Detroit Smash**») y «**Plus Ultra**» sí son nombres propios ⚠️.
- La técnica **«Full Cowl»** de Deku se dobló como «**One For All: A todo
  motor**» ✅ (resumen de Doblaje Wiki, dos veces).
- **Mirko** (ep. 114): «**¿Qué hay de nuevo, viejo?**» (Bugs Bunny) ✅
  (guía de cuadros de diálogo, `biblias/_ya_hechas/`).
- La frase de All Might «私が来た» en latino: **no encontré** cómo quedó
  exactamente («Ya estoy aquí» / «Aquí estoy yo») ⚠️. Tampoco los
  insultos exactos de Bakugo. **No los pongas entre comillas como si
  fueran del doblaje**: escribe la frase de la lámina como texto propio.

---

## 11 · Música

| Tema | Quién | Cuándo | Estado |
|---|---|---|---|
| «**THE DAY**» (opening 1) | **Porno Graffitti** | T1 | ✅ ([ANN](https://www.animenewsnetwork.com/news/2025-09-27/bump-of-chicken-performs-ending-theme-for-my-hero-academia-anime-final-season/.229359) + [Animation Magazine](https://www.animationmagazine.net/2025/08/my-hero-academia-final-season-unveils-new-trailer-opening-song/)) |
| «HEROES» (ending 1) | Brian the Sun ⚠️ | T1 | título ✅, artista de memoria |
| «Peace Sign» · «Sora ni Utaeba» | Kenshi Yonezu ⚠️ · amazarashi ⚠️ | T2 | títulos ✅ ([lista](https://tiermaker.com/categories/anime-and-manga/my-hero-academia-all-openings-and-endings-228788)) |
| «ODD FUTURE» · «Make my Story» | UVERworld ⚠️ · Lenny code fiction ⚠️ | T3 | títulos ✅ |
| «Polaris» · «Starmarker» | BLUE ENCOUNT ⚠️ · KANA-BOON ⚠️ | T4 | títulos ✅ |
| «No.1» · «Merry-Go-Round» | DISH// ⚠️ · Man With a Mission ⚠️ | T5 | títulos ✅ |
| «Hitamuki» · «Bokurano» | SUPER BEAVER ⚠️ · Eve ⚠️ | T6 | títulos ✅ |
| «Tagatame» · «Curtain Call» | TK ⚠️ · Soushi Sakiyama ⚠️ | T7 | títulos ✅ |
| «**THE REVO**» (opening final) | **Porno Graffitti** (los de «THE DAY») | T8, 2025 | ✅ ([ANN](https://www.animenewsnetwork.com/news/2025-09-27/bump-of-chicken-performs-ending-theme-for-my-hero-academia-anime-final-season/.229359) + [Spotify](https://open.spotify.com/track/3STgBX374o2CwNhP1WVmlu)) |
| «**I**» (ending final) | **BUMP OF CHICKEN** | T8 | ✅ (ANN + [Final Weapon](https://finalweapon.net/2025/09/27/my-hero-academia-final-season-bump-of-chicken-ending-theme-song/)) |
| «**You Say Run**» (banda sonora) | **Yuki Hayashi** | 13-7-2016, Toho Animation Records | ✅ ([ANN, entrevista 24-4-2026](https://www.animenewsnetwork.com/interview/2026-04-24/my-hero-academia-composer-yuki-hayashi-why-you-say-run-goes-with-everything/.236436) + [TikTok](https://www.tiktok.com/discover/you-say-run-meme)) |

**Qué ambiente dan**:
- «THE DAY» y «THE REVO» abren y cierran la serie con la misma banda: la
  lámina puede jugar con **«el primer día / el último día de clase»** ⚠️
  (idea mía).
- «**You Say Run**» es **el tema del esfuerzo al límite**. El meme dice que
  «**va con todo**», y el propio Hayashi lo sabe y le hace gracia ✅
  (entrevista de ANN). Para un canal de clases: el «momento You Say Run»
  es **cuando por fin te sale el ejercicio**.
- Para dar clase, la serie usa **música tranquila de día de colegio** en
  las escenas de aula ⚠️ (de memoria; no encontré el nombre del tema).

---

## 12 · Vídeos

YouTube y TikTok estaban **bloqueados**: no pude abrirlos ni sacar
minutos. Van los enlaces que vi en los resultados y lo que dice su título.

| Vídeo | Enlace | Para qué |
|---|---|---|
| Tráiler oficial **FINAL SEASON** (Crunchyroll) | [YouTube](https://www.youtube.com/watch?v=zz37nGym3OQ) · [tráiler 2](https://www.youtube.com/watch?v=fXbY97v2k4s) | Estilo de la temporada final |
| Tráiler de «**More**» (el especial 171, **Deku profesor**) | [YouTube](https://www.youtube.com/watch?v=pxbEWUjh6E4) | **El vídeo clave para este canal**: Deku adulto y la 1-A |
| Tráiler final, **versión doblada** | [YouTube](https://www.youtube.com/watch?v=kg1JhdrpJpY) | Voces |
| Tráiler con subtítulos en inglés | [YouTube](https://www.youtube.com/watch?v=BhbCkhJHe44) · [teaser](https://www.youtube.com/watch?v=H8H12hQN_rU) | — |
| **Comparación de las voces latinas de All Might** (Octavio Rojas, Juan Guzmán, Orlando Noguera) | [YouTube](https://www.youtube.com/watch?v=viK_ZyDu8hc) | Oír las dos escuelas de doblaje |
| **Demo del doblaje latino** | [Vimeo](https://vimeo.com/400652662) | La prueba que pidió Funimation ⚠️ |
| Deku y Bakugo en latino | [YouTube Shorts](https://www.youtube.com/shorts/uRG1RqhyLFo) | Tono de las voces |
| Las voces latinas de MHA | [TikTok @lalogarx](https://www.tiktok.com/@lalogarx/video/7444403094949055799) · [TikTok @sagaoncarlos](https://www.tiktok.com/@sagaoncarlos/video/7350466622060055814) | Presentación del reparto |
| «¿Por qué cambian las voces de MHA?» | [TikTok @fandoblajes](https://www.tiktok.com/@fandoblajes/video/7018642455738338566) | Contexto de los cambios |
| Orlando Noguera, voz de All Might | [TikTok](https://www.tiktok.com/@esamalvaroz/video/7358316188813905158) | Cara y voz del actor |
| **Entrevista a Juan Felipe Sierra** (Todoroki) | [Spotify, El Koki Otaku ep. 12](https://open.spotify.com/episode/3BjOFDN9mi0krz32fTODVe) | Actor latino |
| Octavio Rojas en la Comic Con Lima 2021 | [Spreaker](https://www.spreaker.com/episode/octavio-rojas-la-voz-de-all-might-en-boku-no-hero-punohiroakademia-desde-la-comic-convention-lima-2021--47989785) | Actor latino (películas) |
| El estudio de Horikoshi | [YouTube](https://www.youtube.com/watch?v=AQtvC_r7Mh4) | Ver dónde y cómo dibuja |
| **Tendencia «You Say Run»** | [TikTok](https://www.tiktok.com/discover/you-say-run-meme) | El meme de la música |
| Escena del cuaderno (búsquedas de TikTok) | [TikTok](https://www.tiktok.com/discover/deku-notebook-scene) | Clips de 1×01 |

**Los minutos exactos están en §2**, sacados de los subtítulos: son la
forma de encontrar cada escena en Crunchyroll o Netflix.

---

## 13 · Videojuegos de la franquicia

| Juego | Datos | Cómo cuenta la historia / su interfaz |
|---|---|---|
| **My Hero One's Justice** | Bandai Namco; Japón 23-8-2018, resto 26-10-2018 ⚠️ (Wikipedia, en resumen) | La historia va **en viñetas de cómic americano** con los personajes del anime ✅ ([Digitally Downloaded](https://www.digitallydownloaded.net/2018/11/review-my-hero-ones-justice-sony.html), [Invision](https://invisioncommunity.co.uk/my-hero-ones-justice-review/)). Capturas en [Game UI Database](https://www.gameuidatabase.com/gameData.php?id=1267) (no se pudo abrir) |
| **My Hero One's Justice 2** | 2020 ⚠️ | Mismo sistema de viñetas ⚠️ ([Push Square](https://www.pushsquare.com/reviews/ps4/my_hero_ones_justice_2)) |
| **My Hero Ultra Rumble** | 2023, gratuito, *battle royale*, Byking / Bandai Namco ⚠️ (Wikipedia, en resumen) | Menús de juego online ⚠️. [Base de datos de fans](https://ultrarumble.com/) |
| **My Hero Academia: All's Justice** | Byking / Bandai Namco, **5-2-2026**, PS5, Xbox Series y PC ✅ ([GamingTrend](https://gamingtrend.com/reviews/my-hero-academia-alls-justice-review/), [ANN](https://www.animenewsnetwork.com/news/2025-11-07/my-hero-academia-all-justice-game-video-previews-modes-battles-customization/.230757)) | Cuenta la guerra final; algunas escenas son **fotos fijas del anime que tiemblan con líneas de acción** encima, y las critican ⚠️ (una reseña) |
| **ULTRA IMPACT** (móvil) | — | Tiene una carta-recuerdo llamada «**将来の為のヒーロー分析**» (el cuaderno) ✅ (título de [su base de datos](https://jp.myheroui.com/memory/2100002)) |

**Para la lámina**: el único «cuadro de diálogo» de juego con carácter es
la **viñeta de cómic** de *One's Justice*: rectángulo, borde negro, fondo
de trama. Casa con el gusto de Horikoshi por el cómic americano ✅
(§6.1). No encontré capturas que pudiera abrir: **mira Game UI Database
en el PC** antes de copiarla.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todos reconocen

- «**¡Ya estoy aquí!**» (私が来た) y la sonrisa de All Might ✅ (1×01).
- «**¡Plus Ultra!**», el lema de U.A. ✅.
- «**Tú puedes ser un héroe**» (1×02, 00:21:55 ✅): la escena que más
  hace llorar ⚠️.
- **El cuaderno quemado** y la firma de All Might ✅.
- **Deku murmurando** análisis sin parar ✅ (subtítulos) y el chiste de
  que «da miedo» (8×11 ✅).
- **«You Say Run» va con todo** ✅.
- **«Dadzawa»**: Aizawa como padre adoptivo de sus alumnos ✅.
- «¿Eres **hijo secreto de All Might**?» de Todoroki ✅ (2×06, 00:03:52) y
  **Todoroki surfeando** en su hielo (opening 1) ✅
  ([Know Your Meme](https://knowyourmeme.com/memes/subcultures/my-hero-academia)).
- «**La mitad de mis órganos respiratorios fueron destruidos**» (All
  Might, ep. 2) ✅ (resumen de búsqueda).
- «**¡Los dones no son magia!**» ✅ (resumen de búsqueda).
- El «**harén de rivales**» de Deku ✅ (resumen de búsqueda).
- En latino: **Mirko** con «**¿Qué hay de nuevo, viejo?**» ✅ (guía de
  cuadros de diálogo). **Quirk** se dice «**Don**» ⚠️, y **U.A.** se lee
  «**u-a**», no «yuei» ⚠️ (resumen de Doblaje Wiki). «**Kacchan**» no se
  traduce ⚠️.
- **Bakugo profesor invitado de comunicación** (No.170+1 ✅): chiste nuevo
  y fresco, del 2 de mayo de 2026 ✅ ([Screen Rant](https://screenrant.com/my-hero-academia-171-release-date-time/)).

### 14.2 Qué NO hacer (lo que un fan notaría)

- **Todoroki al revés**: el pelo **blanco va a su derecha** y el **rojo a
  su izquierda**, con la **cicatriz en el ojo izquierdo** ⚠️ (compruébalo
  en un fotograma; es el error más típico).
- **All Might dibujado igual que los demás**: siempre lleva **sombras
  negras de cómic** en los ojos ✅ (§5.2).
- **Bakugo amable o sonriendo dulce**: no. Aunque ayude, **gruñe** ✅.
- **Deku sin sus zapatillas rojas** o con el pelo liso ⚠️.
- **Aizawa enérgico o sonriente**: habla bajo, cansado ✅.
- **Aizawa adulto sin parche**: después de la guerra final lleva **parche
  en el ojo derecho y pierna ortopédica** ✅ (§8). El Aizawa «de siempre»
  sólo vale con Deku **estudiante**.
- **Mezclar doblajes** (las voces de las películas con las de la serie) ✅.
- Llamar al don «Quirk» o «Kosei» en un texto en español latino: es
  «**don**» ⚠️.
- **Que Bakugo se llame a sí mismo «Kacchan»**: así le llaman Deku (41
  veces en los subtítulos revisados), sus amigos de la infancia y Eri ✅;
  él no. Tampoco Aizawa ni los profes: dicen «Bakugo».
- **Mineta** como gancho: el fandom lo odia por sus escenas de acoso ⚠️
  (de memoria). Ejemplo: en el ep. 34, 00:01:16 a 00:01:23, Mineta
  babea mirando a Mt. Lady y Midnight («¡Episodio divino!») ✅.
- Destripar el final sin querer: el final (Deku sin don, profesor) **ya se
  emitió** en latino (hasta el 17-1-2026 ✅), pero no hace falta explicarlo:
  basta con **el traje y el cuaderno**.

---

## 15 · Poses analizadas por personaje

El minuto está comprobado en el subtítulo ✅. **La pose la describo de
memoria** ⚠️: abre el fotograma y confírmala antes de usarla.

### Deku

| Escena | Minuto | Pose | Sirve para |
|---|---|---|---|
| 1×01 | 00:06:44 | De pie entre la gente, **cuaderno abierto en una mano, lápiz en la otra**, mirando arriba | **Explicar** / apuntar |
| 1×01 | 00:11:58 | Agachado junto a la fuente, **sacando el cuaderno mojado**, triste | Pensar |
| 1×01 | 00:19:21 | Ofrece el cuaderno **con las dos manos**, emocionado | **Presentar** |
| 1×02 | 00:21:55 | Llorando, puños apretados, mirando al suelo | Momento emotivo |
| 1×07 | 00:05:26 | En combate, **gritando la página** del cuaderno de memoria | **Explicar** con energía |
| 2×13 | 00:13:01 | De pie ante la clase, **levanta su pizarrita** con «デク» | **Presentar** |
| 8×11 | 00:09:58 | Adulto, **escribiendo** (voz en off) | **Presentar el canal** |
| 8×11 | 00:17:17 | Adulto, agachado ante un chico, **analizando sin parar** | **Explicar** |
| 8×11 | 00:17:56 | Adulto, sonrisa, «¡Ánimo, jovencito!» | **Animar** |
| No.170+1 | 00:08:02 | En el coche de Bakugo, contento con sus papeles | **Celebrar** (terminó su material) |

### All Might

| Escena | Minuto | Pose | Sirve para |
|---|---|---|---|
| 1×01 | 00:13:06 | Sonrisa enorme, pecho fuera, «¡Ya estoy aquí!» | **Presentar** |
| 1×01 | 00:19:21 | **Firmando** el cuaderno con un bolígrafo | **Presentar el objeto** |
| 1×03 | 00:08:47 | **Enseña su plan** de entrenamiento, orgulloso | **Explicar** |
| 1×03 | 00:12:41 | Forma flaca, **dedo acusador**: «No sigues el plan» | **Regañar** |
| 1×06 | 00:10:09 | **Entra por la puerta** de 1-A de lado, con pose de héroe | **Presentar** |
| 1×06 | 00:10:43 | Levanta una **tarjeta** con el tema de la clase | **Anunciar** |
| 1×06 | 00:15:18 | **Lee la chuleta** con cara de apuro | **Explicar** (con humor) |
| 8×11 | 00:18:28 | Adulto mayor, flaco, sonríe: «¡Llegas tarde, jovencito!» | **Animar** |

### Bakugo

| Escena | Minuto | Pose | Sirve para |
|---|---|---|---|
| 1×01 | 00:10:33 | **Explota el cuaderno** entre las manos, sonrisa torcida | Lo que NO se hace con el material (chiste) |
| 1×05 | 00:10:28 | Lanza la pelota con explosión: «¡Muere!» | Energía |
| 2×21 | 00:05:35 | Señala a Kirishima: «¡Te voy a enseñar hasta matarte!» | **Explicar** a gritos |
| 8×11 | 00:13:34 | Adulto, gritando a un chico que lo graba | **Regañar** |
| No.170+1 | 00:07:28 | **Al volante**, furioso | Humor |
| No.170+1 | 00:18:38 | «¡No me llames como mal ejemplo!» | **Profesor invitado** |
| 8×11 | 00:19:58 | «**Ven, Deku**» (来い デク), antes de salir juntos | **Animar** |

### Aizawa

| Escena | Minuto | Pose | Sirve para |
|---|---|---|---|
| 1×05 | 00:09:00 | Saliendo del saco de dormir, ojos a medio cerrar | **Presentar** |
| 1×05 | 00:10:35 | De pie con el aparato de medir, voz plana | **Explicar** |
| 1×05 | 00:12:23 | Pelo levantado, ojos rojos (borrando dones) ⚠️ | **Regañar** |
| 1×06 | 00:05:11 | Media sonrisa: «era mentira» | Humor |
| 2×21 | 00:03:03 | Tras la mesa del profesor, cerrando la clase | **Cerrar** |
| 8×11 | 00:14:58 | Con Deku adulto, consejo serio | **Explicar** a otro profe |

### Uraraka

| Escena | Minuto | Pose | Sirve para |
|---|---|---|---|
| 1×06 | 00:08:48 | Sonriente: «Deku suena a “¡tú puedes!”» | **Animar** |
| 2×01 ep. 14 | 00:17:33 | Decidida, puño cerrado: ganar dinero para sus padres | Pensar |
| 8×11 | 00:07:35 | Mira la nieve: «Quedan tres meses para graduarnos» | Tranquilo |
| No.170+1 | 00:03:01 | Adulta, **explicando con papeles** a sus compañeros | **Explicar** |

### Todoroki

| Escena | Minuto | Pose | Sirve para |
|---|---|---|---|
| 2×06 ep. 19 | 00:03:52 | Serio, mirada fija: «¿Hijo secreto de All Might?» | Pensar (humor) |
| 2×10 ep. 23 | 00:16:44 | Recibe el grito de Deku, fuego y hielo | Momento épico |
| 2×21 | 00:04:10 | Sentado, sin expresión: «Si atiendes no suspendes» | **Regañar** sin querer |

---

## 16 · Vestuario ⚠️

Casi todo de memoria; los colores de §5.3 son aproximados.

| Personaje | Ropa icónica | Otras | Detalles que no pueden faltar |
|---|---|---|---|
| **Deku** | **Uniforme de U.A.**: americana gris, solapas y pantalón verde oscuro, corbata roja | Traje de héroe verde (hecho por su madre a partir del cuaderno, 1×06 ✅); más tarde con refuerzos en brazos y piernas; en la final, **la armadura** que le regalan (8×11 ✅); de adulto, **traje y corbata** ✅ | **Zapatillas rojas**, pelo verde rizado, pecas, cicatrices en la mano derecha |
| **All Might** | Traje de héroe azul, rojo y blanco; en clase el de la **Edad de Plata** ✅ | Forma flaca con ropa ancha | Los **dos mechones** del pelo; sombras negras en los ojos |
| **Bakugo** | Uniforme **desarreglado**: corbata floja, camisa fuera | Traje negro con guanteletes de granada | Ceño fruncido siempre |
| **Aizawa** | Todo negro, **bufanda de captura** gris, **gafas amarillas** | **Saco de dormir amarillo** ✅ | Barba, ojeras, pelo largo |
| **Uraraka** | Uniforme con falda verde | Traje rosa y negro con casco | Mejillas rosadas |
| **Todoroki** | Uniforme bien puesto | Traje azul oscuro; luego chaqueta | Pelo partido, cicatriz izquierda |

**Lo icónico para el canal**: Deku con **uniforme** (estudiante) o con
**traje de profesor**; Aizawa de **negro con la bufanda**; All Might con
el traje **Edad de Plata** (el de dar clase).

---

## 17 · Paisajes y fondos de pantalla

### Los sitios, con su luz ⚠️

- **U.A. por fuera**: edificio de cristal enorme, cielo azul y nubes de
  verano; el portón con la barrera de seguridad.
- **Aula 1-A**: luz de mañana por los ventanales, pizarra verde oscura,
  puerta gigante ✅ (1×05, 00:05:53).
- **Sala de profesores** (8×11): luz de tarde, una tele encendida.
- **Playa Dagobah** (1×03): amanecer naranja sobre montañas de basura.
- **Estatua de All Might** (8×11): al atardecer ⚠️.
- **Nieve en U.A.**, tres meses antes de la graduación (8×11, 00:07:35
  «¡Anda, nieva!» y «Quedan tres meses» ✅): luz fría de invierno. La
  graduación viene justo después (00:07:57 ✅).

### Fondos de pantalla

| Fondo | Enlace | Tamaño | Autor |
|---|---|---|---|
| Oficiales del anime | [heroaca.com/special/wallpaper.html](https://heroaca.com/special/wallpaper.html) | varios, sin ver ⚠️ | © Horikoshi / Shueisha, comité MHA |
| Galería oficial | [heroaca.com/gallery](https://heroaca.com/gallery/) | ⚠️ | ídem |
| Recopilaciones de fans | [Wallpaperbetter](https://www.wallpaperbetter.com/ja/hd-wallpaper-akbuv), [Pxfuel](https://www.pxfuel.com/ja/desktop-wallpaper-sezmk), [Kabekin](https://kabekin.com/wallpaper/anime/myheroacademia/8qyr) | «HD / 4K» según su título ⚠️ | sin autor claro: **sólo para mirar** |

---

## 18 · Guía para generar con IA (Firefly, Canva)

> Sirve para **fondos, objetos y poses de apoyo**, nunca para «inventar»
> al personaje oficial: el personaje sale de un fotograma real (§15).

**Rasgos que nunca cambian**
- Deku: pelo **verde oscuro rizado**, pecas en las mejillas, ojos verdes
  grandes, **zapatillas rojas**. De adulto: traje oscuro y corbata.
- All Might: pelo rubio con **dos mechones en punta**, sonrisa enorme,
  **sombras negras** en los ojos.
- Bakugo: pelo rubio ceniza **en pinchos**, ojos rojos, ceño.
- Aizawa: pelo negro largo, **bufanda gris** alrededor del cuello, gafas
  amarillas, ojeras.

**Estilo**
- Anime de estudio BONES: **línea negra limpia de grosor medio**, sombra
  **en dos tonos** (sin degradados suaves), brillos pequeños.
- Para All Might, **sombras duras de cómic americano** y trama.
- Colores saturados y limpios; cielo **azul intenso**.

**Luz y encuadre**
- Aula: luz de mañana lateral desde ventanales.
- Plano medio o americano; cámara a la altura del pupitre para el
  cuaderno.

**Palabras que ayudan** (en inglés, que las IA entienden mejor):
`anime style, clean line art, two-tone cel shading, japanese high school
classroom, large windows, morning light, school notebook with burnt
corner, handwritten notes, sticky notes, green chalkboard, bright blue sky`

**Palabras que lo estropean**: `realistic, 3d render, painterly,
watercolor, chibi, dark, gritty, horror, glowing` (y cualquier nombre de
personaje, que hace que la IA copie mal).

**Qué usar como referencia**
- De estilo: la **key visual de la FINAL SEASON** (§3.1) y los fotogramas
  de §2.
- De pose: los fotogramas de §15 (1×06, 00:10:09 y 00:15:18 para All
  Might; 8×11, 00:09:58 y 00:17:56 para Deku adulto).
- De objeto: la **réplica del cuaderno n.º 13** (§3.3).
- De sitio: el **aula 1-A** de banabanaba (§4.1), mejor que generarla.

---

## 19 · Tres conceptos para la lámina de #material-de-clase

Los tres usan los textos de §0. Donde pongo una frase «en la voz de la
serie» es **traducción o adaptación mía**, no del doblaje latino (no
encontré las frases latinas exactas, §10.3). Recortes siempre por
`v3/integrar.py` y comprobados a 1:1.

### Concepto A — «El cuaderno de Deku-sensei» (el objeto del plan, mejorado)

- **Objeto y sitio**: **la mesa del profesor del aula 1-A**, con luz de
  mañana por los ventanales. Encima, **dos cuadernos**:
  - uno **cerrado**, encima de una **pila de cuadernos numerados** (Deku
    tenía 13 antes de empezar ✅, §3.3), con la portada escrita a
    rotulador como el n.º 13 original;
  - otro **abierto**, con las hojas **onduladas** y **la esquina
    chamuscada** (1×01 ✅). Alrededor: un lápiz, goma con virutas y
    **pósits de colores** que asoman del canto.
  - En Blender: el aula y el pupitre de **banabanaba** (CC BY, §4.1), el
    cuaderno modelado con las medidas de la **réplica Toynk** (20 × 15 cm,
    §3.3), papel de **ambientCG** (CC0, §5.4). La tinta sigue las ondas
    del papel.
- **Personaje**: **Deku adulto, profesor** (traje y corbata ✅). Pose: de
  pie tras la mesa, **una mano abierta sobre el cuaderno** y la otra
  señalando la página, sonriendo. Referencias: **8×11, 00:09:58**
  (escribiendo) y **00:17:56** («¡Ánimo, jovencito!»). Alternativa sin
  destripe: **Deku estudiante con el cuaderno** (1×01, 00:06:44).
- **Cómo habla**: no hay globo. **Todo va escrito con su letra** en el
  cuaderno (**Caveat**), con flechas y dibujitos, como sus análisis. Su
  frase va en **un pósit amarillo** pegado en la esquina de la página
  derecha, también en Caveat:
  **«Yo lo apunté todo. Ahora les toca a ustedes»** (adaptación de «te
  toca dar sueños», 8×11, 00:17:34 ✅).
- **Dónde va cada texto**:
  - Portada del cuaderno cerrado, a rotulador (**Permanent Marker**):
    **Material de clase**, y debajo, más pequeño: **Lo que se da en clase
    y los ejercicios de cada alumno**. En la esquina, «No.1», como el
    «No.13».
  - Página izquierda, como un análisis de Deku, tres apartados con
    recuadro y un dibujito cada uno: **De qué fue** (un micrófono),
    **Material** (una hoja con clip), **Para practicar** (una flecha en
    espiral).
  - Página derecha, nota con flecha: **Un hilo por tema o por alumno**.
  - Pósits que asoman del canto, uno rojo y uno azul, con la nota
    **Etiqueta si es de doblaje o de canto**.
  - Abajo del todo, como el cierre de cada avance: «**¡Más allá! ¡Plus
    Ultra!**» en **Bangers** pequeño, a lápiz rojo ⚠️ (opcional).
- **Para que no quede plano**: **lápiz y virutas desenfocados** en primer
  plano; la **sombra de la mano de Deku** cae sobre la página; luz rasante
  que marca las **ondas del papel** mojado y el negro del quemado; al
  fondo, la **pizarra verde desenfocada**.
- **Lámina 2**: **el índice del cuaderno**, con **nueve pestañas de
  colores**, una por etiqueta, en tres bloques (Qué área, Qué es, Qué
  nivel). La idea sale de «¡Cuaderno número 10, página 18!» (1×07,
  00:05:26 ✅).

### Concepto B — «La chuleta de All Might» (el profe que lee su material)

- **Objeto y sitio**: **la puerta gigante del aula 1-A** («¿es para que
  pase cualquiera?», 1×05, 00:05:53 ✅) y **la chuleta de All Might**: una
  cartulina grande, con las esquinas dobladas y un clip. En Blender:
  puerta corredera enorme, marco, **el cartel del aula** encima de la
  puerta y la cartulina.
- **Personaje**: **All Might** con el traje de la **Edad de Plata** (el de
  dar clase ✅). Pose: **entrando por la puerta** (1×06, 00:10:09) y
  **leyendo la chuleta** con cara de apuro (1×06, 00:15:18 ✅). Detrás,
  asomando por la puerta, **Deku estudiante** diciendo «¡una chuleta!».
- **Cómo habla**: su frase va en una **caja de cómic americano**
  rectangular, borde negro grueso, fondo amarillo, en **Bangers**, como la
  historia de *One's Justice* ✅ (§13):
  **«¡Ya estoy aquí! Y traigo el material»** ⚠️ («Ya estoy aquí» es mi
  traducción de 私が来た: antes de rotular, **escucha cómo lo dice el
  doblaje** en 1×01, 00:13:06).
- **Dónde va cada texto**:
  - Cartel encima de la puerta (donde pone «1-A»): **Material de clase**.
  - Título de la chuleta: **Lo que se da en clase y los ejercicios de cada
    alumno**.
  - Cuerpo de la chuleta, como las reglas del entrenamiento: **De qué
    fue** · **Material** · **Para practicar** (cada uno en su línea, con
    su número).
  - Un papel pegado en la puerta con cinta: **Un hilo por tema o por
    alumno**.
  - Una segunda tarjeta en la otra mano de All Might: **Etiqueta si es de
    doblaje o de canto**.
- **Para que no quede plano**: **el marco de la puerta en primer plano**
  cortando un lado; All Might tan grande que **no cabe entero** (la
  cabeza casi toca el marco); **sombras duras de cómic** en su cara ✅
  frente a la luz suave del pasillo; cabezas de alumnos a contraluz abajo.
- **Lámina 2**: nueve **tarjetas** como la de «BATTLE» ⚠️, en abanico en
  la mano de All Might: una etiqueta en cada una.

### Concepto C — «Clase especial: Bakugo, profesor invitado» (la pizarra)

- **Objeto y sitio**: **la pizarra verde del aula 1-A**, con su repisa,
  tizas y borrador lleno de polvo. En Blender: pizarra con textura de
  pizarra usada, tizas rotas, polvo en el aire. Pupitres de banabanaba
  (CC BY) en primer plano.
- **Personaje**: **Bakugo**, el más querido ✅. Es la escena del especial
  «More»: Deku lo llama como **profesor invitado** para una clase de
  «**Introducción a la comunicación**» y él protesta: «¡No me llames como
  mal ejemplo!» (No.170+1, 00:18:31 a 00:18:38 ✅). Pose: **golpea la
  pizarra con la palma**, tiza partida en la otra mano, chispas de
  explosión saliendo de los dedos. Al lado, **Aizawa adulto** (con parche,
  §8) mirando de brazos cruzados; en la puerta, **Deku-sensei tomando
  notas** en su cuaderno.
- **Cómo habla**: **escribe en la pizarra**, en letras de tiza grandes y
  furiosas (**Schoolbell** o **Permanent Marker** en blanco con textura).
  Su grito, en una **caja de cómic** con borde dentado, en Bangers:
  **«¡Les voy a enseñar hasta matarlos!»** (adaptación de 教え殺したろか,
  2×21, 00:05:36 ✅). Una nota de Aizawa, con letra pequeña y limpia,
  pegada con un imán.
- **Dónde va cada texto**:
  - Arriba de la pizarra, subrayado dos veces: **Material de clase**.
  - Debajo: **Lo que se da en clase y los ejercicios de cada alumno**.
  - Tres columnas con recuadro: **De qué fue** · **Material** · **Para
    practicar**.
  - Abajo, en un círculo: **Un hilo por tema o por alumno**.
  - La nota de Aizawa, con imán: **Etiqueta si es de doblaje o de canto**
    (la regla la pone el tutor).
- **Para que no quede plano**: **pupitres desenfocados** delante; **polvo
  de tiza** en el haz de luz de la ventana; la **luz naranja** de las
  chispas de Bakugo como segunda luz; la pizarra un poco en ángulo.
- **Lámina 2**: los alumnos de 1-A **levantando sus pizarritas**, como en
  la clase de nombres de héroe (2×13, 00:06:55 ✅): **nueve pizarritas,
  una por etiqueta**.

### ¿Cuál primero?

1. **A** es el objeto que pedía el plan, se hace en Blender y **Deku
   profesor escribiendo en su cuaderno** es literalmente el canal.
2. **C** usa al personaje **más querido** y un chiste reciente que los
   fans reconocen; ojo, destripa el final (Aizawa con parche).
3. **B** es el más cómico; All Might no es de los más votados, pero **es
   el profe que lee su material** (la chuleta, ✅).

Para que case con **#avisos-clases** (Assassination Classroom, encargo 24):
las dos pasan en un aula; conviene usar **la misma luz de mañana** y
**la misma pizarra verde**.

---

## 20 · Lo que no pude verificar

- **Ninguna imagen vista**: todo el arte está enlazado pero sin abrir
  (bloqueo). Faltan **hojas de contacto**.
- **Frases exactas del doblaje latino**: «私が来た» en latino, insultos de
  Bakugo, «Plus Ultra» traducido o no. **No hay ninguna frase latina
  confirmada** salvo la de Mirko (guía de diálogos).
- **Aizawa**: «José Arenas» apareció en un resumen; choca con Ernesto
  Rumbaut. Iida (Luis Carreño) y Burnin (Gigliola MC) con **una sola
  fuente**.
- Que **@Dr0mz** sea Rómulo Bernal (lo deduzco).
- La película *Ahora es tu turno*: ¿The Kitchen o **VSI** con Gina
  Sánchez? Una fuente dice VSI.
- **Colores**: todos los hex son de memoria.
- **Color de la portada del cuaderno n.º 13** y su maquetación interior.
- Todas las **poses** de §15 (el minuto sí está comprobado).
- Minutos de los **tráileres** y de los TikTok.
- **Licencias** de los modelos de tahabzr y Open3DLab.
- La letra que usa VIZ en los globos del manga en inglés.
- Artistas de los openings T1-T7 (los títulos sí están comprobados).

---

## 21 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)

- **WebFetch bloqueado** en: doblaje.fandom.com (también la API),
  crunchyroll.com, wdnes.com, heroaca.com, jp.myheroui.com.
- **curl bloqueado**: api.sketchfab.com, gameuidatabase.com.
- **GitHub responde** por git: clon parcial de
  [kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror)
  (temporada 1, 2, FINAL SEASON y el especial «More») y de
  [google/fonts](https://github.com/google/fonts).
- Por eso **no hay `hojas/`** ni se corrió `investigar_serie.py`.

### Búsquedas web (46 hechas)

| # | Idioma | Búsqueda |
|---|---|---|
| 1 | ES | My Hero Academia doblaje latino reparto Izuku Midoriya Katsuki Bakugo All Might actor de voz |
| 2 | ES | Boku no Hero Academia doblaje latino estudio director Crunchyroll Funimation actores Todoroki Uraraka Aizawa |
| 3 | ES | «Sebastián Reggio» «Rómulo Bernal» «Orlando Noguera» My Hero Academia elenco latino |
| 4 | ES | MHA Ahora es tu turno doblaje latino elenco (3djuegos, wdnes, codigoespagueti, senpai, funianime, ultimasnoticias, anmtvla) |
| 5 | ES | MHA sexta temporada doblaje latino cambio de voces Uraraka Sofía Baltazar |
| 6 | ES | «Juan Felipe Sierra» Todoroki voz latina «José Arenas» Aizawa |
| 7 | ES | Shota Aizawa Eraser Head voz latino doblaje |
| 8 | EN | MHA official popularity poll results Weekly Shonen Jump |
| 9 | EN | «World Best Hero» results top 10 |
| 10 | JA | 将来の為のヒーロー分析 ノート 公式 グッズ レプリカ デク ヒロアカ |
| 11 | EN | «Hero Analysis for the Future» Deku notebook No. 13 burned All Might autograph |
| 12 | EN | MHA logo font name typeface manga lettering VIZ |
| 13 | EN | All's Justice story mode dialogue box UI |
| 14 | EN | One's Justice story mode comic panels speech bubbles |
| 15 | JA | ヒロアカ 馬越嘉彦 インタビュー キャラクターデザイン アメコミ 影 堀越耕平 |
| 16 | EN | MHA all openings endings list, You Say Run |
| 17 | ES | All Might doblaje latino frase «estoy aquí» «Plus Ultra» Orlando Noguera |
| 18 | ES | «Octavio Rojas» All Might doblaje mexicano Two Heroes «Juan Guzmán» |
| 19 | ES | MHA temporada final doblaje latino Crunchyroll, Uraraka séptima temporada |
| 20 | ES | Ochaco Uraraka voz latina temporada 7 |
| 21 | EN | sketchfab MHA notebook / U.A. / desk (sketchfab.com) |
| 22 | EN | banabanaba sketchfab licencia CC Attribution |
| 23 | EN | Deku hero analysis notebook fan art (artstation, deviantart, pixiv) |
| 24 | JA | 僕のヒーローアカデミア 公式キャラクターブック Ultra Analysis / Ultra Archive |
| 25 | EN | MHA chapter 430 epilogue Deku teacher notebook |
| 26 | ES | doblaje latino frases Bakugo «maldito nerd» / All Might «¡Ya estoy aquí!» |
| 27 | ES | «Héctor Mena» Deku «Rafael Escalante» «Pepe Vilchis» Two Heroes doblaje México |
| 28 | EN | Shota Aizawa personality sleeping bag capture weapon cats logical ruse |
| 29 | EN | MHA fandom memes inside jokes |
| 30 | ZH | 我的英雄学院 人气投票 结果 爆豪 第一 相泽 |
| 31 | KO | 나의 히어로 아카데미아 최종화 데쿠 선생님 8년 후 교사 |
| 32 | EN | MHA «More» special No. 170+1 air date 2026 |
| 33 | JA | ヒロアカ 公式 壁紙 ダウンロード FINAL SEASON キービジュアル |
| 34 | JA | 僕のヒーローアカデミア スタッフ 美術監督 色彩設計 ボンズ |
| 35 | EN | Game UI Database My Hero One's Justice / Ultra Rumble |
| 36 | EN | MHA FINAL SEASON official trailer YouTube |
| 37 | EN | «You Say Run» meme Yuki Hayashi TikTok |
| 38 | EN | MHA anime eyecatch Deku notebook pages |
| 39 | EN | MHA manga volume 42 final cover |
| 40 | EN | ambientCG / Poly Haven paper texture CC0 |
| 41 | EN | FINAL SEASON opening ending theme song |
| 42 | JA | 堀越耕平 インタビュー デク ノート 分析 オタク 最終話 教師 |
| 43 | ES | doblaje latino referencias chistes memes adaptación Mirko |
| 44 | EN | Aizawa after final war epilogue prosthetic leg eye patch |
| 45 | EN | Deku notebook replica No. 13 cover color Toynk |
| 46 | JA | 僕のヒーローアカデミア Blu-ray Vol.1 ジャケット 描き下ろし 馬越嘉彦 |

Por idioma: **ES 14 · EN 23 · JA 7 · ZH 1 · KO 1**.

### GitHub (sin cupo)

- Subtítulos japoneses (Netflix y Amazon) de **T1 (13 ep. + el 13.5)**,
  **T2 (ep. 14-38)**, **FINAL SEASON (ep. 160-170)** y el especial
  **«More» (No.170+1)**, pasados a texto con minuto y buscados con `grep`
  (ノート, 分析, カンペ, 授業, 先生, 合理的, 私が来た, SMASH…).
- 35 letras de Google Fonts revisadas con fontTools (§6.2).

### Fuentes consultadas por tipo

- **Oficiales**: heroaca.com (staff, wallpapers, galería, tienda), BONES,
  X de @heroaca_anime, VIZ, Shueisha, Crunchyroll (noticias), Bandai Namco
  Europe, TOHO.
- **Entrevistas y staff**: ANN (Yuki Hayashi, 2026), Animate Times
  (Umakoshi), y, vistas sólo en los resultados, Natalie, Kono Manga ga
  Sugoi y Cinema Today (Horikoshi) y Real Sound.
- **Otros idiomas**: japonés (Animate Times, Dengeki, Chiebukuro,
  Oricon), chino (Tencent, niusnews, HK01, Facebook heroyaoya), coreano
  (Wikipedia coreana, Namu Wiki, Aniplus).
- **Wikis de fans**: MHA Wiki (Fandom), Doblaje Wiki (sólo por resumen),
  TV Tropes y Know Your Meme (por resumen), Behind The Voice Actors.
- **Doblaje latino**: Doblaje Wiki, ANMTV (X), Código Espagueti, 3DJuegos,
  Canal 5, Cine Premiere, La Crónica, Reporte Índigo, IMDb, Spotify,
  Spreaker.
- **Arte y 3D**: Sketchfab, Open3DLab, DeviantArt, Pixiv, ambientCG, Poly
  Haven.
- **Vídeo**: YouTube, TikTok, Vimeo (sin abrir).
- **Juegos**: Game UI Database, reseñas (Push Square, Digitally
  Downloaded, GamingTrend, Invision), ULTRA IMPACT DB.
- **Código**: GitHub (kitsunekko-mirror, google/fonts).

### Lo que NO encontré

- **The Cutting Room Floor**: no busqué (los juegos de MHA no son el
  centro de este canal); sin datos.
- **Reddit / Arctic Shift**: bloqueados.
- **Wayback Machine**: bloqueada.
- **Frases del doblaje latino** línea por línea.
- **Fotogramas en 1080p**: no pude bajar ninguno; los minutos de §2 son
  el camino para sacarlos.
- **Cómo es por dentro una página oficial del cuaderno.**
