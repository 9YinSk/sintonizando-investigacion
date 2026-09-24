---
tags: [biblia, serie, laminas, biblioteca]
serie: "Demon Slayer: Kimetsu no Yaiba (鬼滅の刃)"
canal: "sin canal: propuesta 🔊 Aula (LA ACADEMIA) y #que-estas-escuchando (libre)"
fecha: 2026-09-24
---

# Biblia · Demon Slayer (Kimetsu no Yaiba) — para la biblioteca

> [!important] Cómo se hizo, y sus límites
> - **Red abierta**. `herramientas/investigar_serie.py` sobre **Kimetsu no
>   Yaiba Wiki**: **4.314 + 257 imágenes** en 96 hojas; miré las más grandes
>   y busqué el resto por título. Tres hojas propias en `hojas/` (§3).
> - **Subtítulos japoneses de Netflix** de los 63 episodios y las dos
>   películas (GitHub, kitsunekko-mirror): **todos los minutos** de §2 salen
>   de ahí. La traducción es mía, no la del doblaje.
> - **Doblaje Wiki por su API** + ANMTV y SensaCine: cada voz principal en
>   dos fuentes (§10).
> - **Vídeos mirados**: YouTube no deja bajar vídeo ni subtítulos desde
>   aquí, así que miré sus **storyboards** (miniaturas cada 1-2 s) del
>   opening, el ending, el tráiler latino, dos clips oficiales, dos escenas,
>   un minijuego y una entrevista al staff (§12). Minuto ±1-2 s.
> - **Colores medidos con Pillow** en fotogramas y arte oficial (§5).
> - **Letras comprobadas con fontTools** (§6).
> - ✅ = dos fuentes, o lo dice el subtítulo con su minuto, o lo vi en un
>   fotograma. ⚠️ = una fuente o de memoria.
> - **Episodios**: «T1-25» = temporada 1, ep. 25; «TM», Tren Mugen; «DR»,
>   Distrito Rojo; «AH», Aldea de los Herreros; «EP», Entrenamiento de los
>   Pilares; «MT» y «CI», las películas (tabla en §2).

## Índice

0. Demon Slayer no tiene canal: dónde encaja mejor
1. Resumen para quien tenga prisa
2. Las escenas que sirven (con minuto)
3. Arte oficial y hojas de contacto
4. Fan art y 3D (sólo como referencia)
5. Sitios, luz, paleta y texturas
6. Tipografía
7. Cómo hablan y piensan en pantalla (el cuadro de diálogo)
8. Los personajes
9. ¿Quién es el más querido?
10. Doblaje latino
11. Música
12. Vídeos
13. Videojuegos de la franquicia
14. Lo que ama el fandom, y qué NO hacer
15. Poses analizadas por personaje
16. Vestuario
17. Paisajes y fondos de pantalla
18. Guía para generar con IA: imagen y texto
19. Estilo de dibujo, técnica, Blender y encuadres
20. Texturas 2D
21. Gustos y detalles de cada personaje
22. Por qué la gente la ama, y las escenas que hacen llorar o gritar
23. Fan dubs y comunidad hispana
24. Colaboraciones, figuras y cosplay
25. Obras parecidas y láminas vecinas
26. El mundo, la historia por arcos y sus símbolos
27. Tres conceptos de lámina
28. Lo que no pude verificar
- Cumplimiento del encargo
29. Bitácora de búsqueda

(Arriba del índice, «Segunda pasada · qué cambió»: el repaso del
24-sep-2026 que añadió las secciones 19-26.)

---

## 0 · Demon Slayer no tiene canal: dónde encaja mejor

El encargo dice que Demon Slayer está en la **biblioteca**: es de lo más
visto en Latinoamérica (§10.1: *Castillo Infinito* es **el anime más
taquillero de la historia en México y en casi toda la región**), pero no
tiene canal. Miré los canales de `servidor/inventario.md` y los que ya
proponen las biblias 01-30 (`grep '^canal:' biblias/*/biblia.md`).

**La clave de Demon Slayer para este servidor**: todo su poder es
**la respiración** (呼吸). Los cazadores entrenan **los pulmones**,
**aguantan el aire**, respiran **hasta dormidos** y rompen una calabaza
**soplando** (T1-25, 00:04:29 ✅). Es, literalmente, lo que se hace en una
clase de **doblaje y canto**. Y tiene un segundo tema muy fuerte: **el
oído** (Zenitsu oye «el sonido» de cada persona y toca de oído el
shamisen; Tengen es el **Pilar del Sonido** y lee al enemigo como una
**partitura**, §2.2).

### La propuesta, de un vistazo

| # | Canal | Por qué | Personaje | Estado del canal |
|---|---|---|---|---|
| **1** | **🔊・Aula ⋆ ˚** (LA ACADEMIA, sala de voz) | la clase de **respiración** de la Mansión Mariposa: la calabaza, las tazas, el dojo | **Shinobu** (5.ª en la encuesta oficial) con Tanjiro de alumno | la biblia 29 la dejó a medias (Monsters University **o** Assassination Classroom). Demon Slayer encaja mejor: su tema **es** entrenar la respiración |
| **2** | **ıı・🎧・que-estas-escuchando** (LA SALA) | **Zenitsu toca de oído** cualquier canción; el juego *Hinokami 2* tiene un **minijuego de shamisen** con la barra de notas en forma de mástil | **Zenitsu** (**1.º** en la 2.ª encuesta oficial) | **libre** ✅: ningún encargo ni biblia lo propone |
| 3 | **lámina 2 del Aula** (o de #avisos-clases): el **escenario con telón rojo** donde Tanjiro cuenta los Secretos de la era Taisho; en tablillas, «cómo va una clase». Otra idea para #avisos-clases: el **Entrenamiento de los Pilares** es un **horario de clases** (cada Pilar enseña una cosa, en orden, EP-1 00:36:43 ✅) | **Tanjiro** con **Mitsuri** | #avisos-clases lo propone Assassination Classroom (encargo 24) |

Del inventario (textos reales):

> **🔊・Aula ⋆ ˚** (voz), sección **LA ACADEMIA**. **No tiene descripción**
> en el inventario. Sus vecinos sí:
> **#avisos-clases**: «_Cuándo hay clase y de qué. Clases de doblaje y de
> canto. Activa el aviso que te interese en Canales y roles._»
> **#material-de-clase** (foro): «_Lo que se da en clase y los ejercicios de
> cada alumno. Un hilo por tema o por alumno. Etiqueta si es de doblaje o
> de canto._» Su hilo de ejemplo se llama, justamente, «**EJEMPLO · Clase
> 1 — Respiración y apoyo**».
> **#dudas** (foro): «_Pregunta sin miedo, por tonta que te parezca._»

> **ıı・🎧・que-estas-escuchando** (texto), sección **LA SALA**: «_La
> canción que llevas en bucle. Pega el enlace y di por qué._»

### Los textos de la lámina del Aula (propuesta: el Aula no tiene descripción)

Una idea cada uno, sin «·», «—» ni paréntesis. **Confírmalos con el dueño**
antes de dibujar: salen de los canales vecinos, no de una descripción del
Aula.

| # | Texto | Idea |
|---|---|---|
| 1 | **Aula** | nombre |
| 2 | **Aquí se da la clase, en vivo** | qué es |
| 3 | **Doblaje y canto** | de qué |
| 4 | **El horario está en avisos-clases** | cuándo |
| 5 | **Activa el aviso en Canales y roles** | cómo enterarse |
| 6 | **Lo de cada clase queda en material-de-clase** | después |
| 7 | **¿Te quedó una duda? Pregunta en dudas** | dudas |
| 8 | Frase del personaje, en su voz (§7 y §27) | gancho |

### Lámina 2 del Aula (si se quiere explicar cómo va una clase)

El entrenamiento de recuperación de la Mansión Mariposa tiene **tres
partes** (T1-24, 00:07:00 a 00:07:36 ✅) que se parecen mucho a una clase
de voz. Es **una idea para adaptar** a cómo den la clase de verdad:

| En la serie | En la clase | Quién lo dice |
|---|---|---|
| **Estiramientos** en el futón (Sumi, Kiyo y Naho) | calentar el cuerpo y la voz | las tres niñas: «¡Ánimo!» |
| **Reflejos con tazas de té medicinal** (Aoi y Kanao) | ejercicio rápido, leer en frío | Aoi, seria |
| **Pilla-pilla** por todo el dojo | escena completa, de principio a fin | Kanao, en silencio |
| **La calabaza** (reto aparte, T1-25) | aguante de aire y apoyo | Shinobu: «Cuento contigo» |

### Los textos de #que-estas-escuchando (concepto C)

| # | Texto | Idea |
|---|---|---|
| 1 | **Qué estás escuchando** | nombre |
| 2 | **La canción que llevas en bucle** | qué va aquí |
| 3 | **Pega el enlace** | cómo |
| 4 | **Y di por qué** | lo que se pide |
| 5 | Frase de Zenitsu (§27, concepto C) | gancho |

(Cuatro textos caben de sobra: aquí **no** hace falta lámina 2.)

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Qué es | Manga de **Koyoharu Gotōge** (*Weekly Shōnen Jump*, **15-feb-2016 a 18-may-2020**, **205 capítulos**, 23 tomos) ✅ fechas y capítulos en la [ficha del manga](https://kimetsu-no-yaiba.fandom.com/wiki/Kimetsu_no_Yaiba_(Manga)); los 23 tomos ⚠️ de memoria. Anime de **ufotable**, dirigido por **Haruo Sotozaki**, música de **Yuki Kajiura y Go Shiina** ✅ (Kimetsu Wiki). **63 episodios** en 5 arcos (§2) y las películas *Mugen Train* (2020) y *Castillo Infinito* (2025) ✅ (Doblaje Wiki, wiki) |
| Tono | **Era Taishō** (Japón, 1912-1926): kimonos, farolillos, trenes de vapor, madera. **Oscuro y triste** en los combates (sangre, noche, demonios), **cómico y tierno** en los descansos (caras deformadas, Zenitsu gritando, los Secretos de la era Taisho). La lámina puede ser **cálida**: la Mansión Mariposa es de día, con glicinias y mariposas |
| Por qué encaja en el Aula | Todo su sistema de poder es **respirar**. La escena de **Tanjiro reventando la calabaza de un soplido** (T1-25) es una clase de apoyo diafragmático con otro nombre |
| El objeto | **La calabaza** (瓢箪, *hyōtan*), marrón `#853920`, con cordón rojo, y **la mesa de tazas de té medicinal** del dojo de la Mansión Mariposa. Las dos se hacen en Blender en una tarde (hay calabazas CC BY en Sketchfab, §4) |
| El más querido | Encuesta oficial 1 (2017): **1.º Tanjiro**, 2.º Zenitsu, 3.º Nezuko. Encuesta oficial 2 (2020, **130.316 votos**): **1.º Zenitsu**, 2.º Giyu, 3.º Muichiro, 4.º Tanjiro, **5.º Shinobu**, 6.º Inosuke, 7.º Rengoku ✅ (Kimetsu Wiki + animatetimes + GAME Watch). En Latinoamérica, **Rengoku** es el fenómeno de las pelis («¡Sabroso!»). Ver §9 |
| Quién habla en la lámina | Aula: **Shinobu** (la profe que explica sonriendo y pica a los alumnos), con Tanjiro soplando la calabaza. #que-estas-escuchando: **Zenitsu** vestido de «Zenko» con el shamisen |
| Cuadro de diálogo propio | **No es un globo blanco**. Demon Slayer habla con: la **cartela de nombre vertical a pincel** (negra sobre el fotograma, T1-20), el **Secreto de la era Taisho** (el logo en círculo rojo sobre una **ola ukiyo-e**, o una **tablilla de madera** «その1», y en el arco de los Pilares un **escenario con telón rojo** `#B91F2A`), la cartela **«つづく» (Continuará)** en franjas de colores, el **«予告» (Avance) dibujado a lápiz**, el **marco de cumpleaños** con nudo *mizuhiki* y nombre vertical, y en el juego la **barra-mástil de shamisen**. Ver §7 |
| Letras | La web oficial usa **Zen Old Mincho** y **Noto Serif JP** (comprobado en su CSS) ✅. El «DEMON SLAYER» del logo occidental es **Blood Crow Condensed** (Iconian, gratis no comercial, **trae tildes, ñ, ¿ y ¡**) ⚠️. Para el pincel: **Yuji Syuku / Yuji Boku**. Todas con tildes comprobadas con fontTools (§6) |
| Voz latina | Tanjiro **Iván Bastidas**, Nezuko **Annie Rojas**, Zenitsu **José Luis Piedra**, Inosuke **Uraz Huerta**, Rengoku **Irwin Daayán**, Shinobu **Cristina Hernández**, Giyu **Marc Winslow** (también director) ✅. Estudios Universal Cinergía, SIGE e Iyuno México. Ver §10 |
| Juegos | *The Hinokami Chronicles* (2021) y *Hinokami Chronicles 2* (2025), de CyberConnect2. El 2 trae el minijuego de **Zenko y el shamisen**. En Steam España se llama «**Guardianes de la Noche** – Las Crónicas de Hinokami»; el texto en español es de España, sin voces latinas ✅ (API de Steam). Ver §13 |

---

## 2 · Las escenas que sirven (con minuto)

**De dónde sale el minuto** ✅: los **subtítulos japoneses para sordos de
Netflix** (`ja[cc]`, con el nombre de quien habla entre paréntesis) de
**toda la serie y las dos películas**, del repositorio
[Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv)
(carpetas `Kimetsu no Yaiba`, `…Mugen Ressha-hen (TV)`, `…Yuukaku-hen`,
`…Katanakaji no Sato-hen`, `…Hashira Geiko-hen` y `anime_movie/…`). Los pasé
a un solo texto de **25.876 líneas** y los busqué con `grep`. **La
traducción al español es mía**: la frase del doblaje latino puede ser otra.

**Cómo leo los episodios** (así numera Netflix Latinoamérica, por arco):

| Código | Arco | Episodios (numeración total) |
|---|---|---|
| **T1-nn** | Temporada 1 («Hermanos Kamado») | 1-26 |
| **TM-n** | Tren Mugen (versión TV) | 27-33 |
| **DR-nn** | Distrito Rojo (Entertainment District / Yūkaku) | 34-44 |
| **AH-nn** | Aldea de los Herreros | 45-55 |
| **EP-n** | Entrenamiento de los Pilares (Hashira Geiko) | 56-63 |
| **MT** / **CI** | películas *Mugen Train* (2020) y *Castillo Infinito* (2025) | — |

El minuto es el del archivo de Netflix; en Crunchyroll puede moverse
**uno o dos minutos**. El subtítulo de *Castillo Infinito* es una
**transcripción automática** (Whisper): sus frases llevan ⚠️.

### 2.1 Respirar: la técnica del mundo de Demon Slayer (el corazón del canal propuesto)

Todo el poder de la serie es **la respiración** (呼吸, *kokyū*). Para un
servidor de **voz y canto**, es la coincidencia más fuerte que hay.

| Escena | Minuto | Qué pasa / qué se dice | Para qué sirve |
|---|---|---|---|
| T1-02 | 00:13:39 | Urokodaki le da un golpe: «**¡Juzgas muy lento!**» (判断が遅い) | El maestro exigente; meme |
| T1-03 | 00:10:39 | Urokodaki: «**Si cortas esta roca, te dejo ir a la Selección Final**» | El examen del maestro |
| T1-03 | 00:18:13 a 00:18:43 | Makomo le explica la respiración: «Acelera **la sangre y el latido**… **haz grandes los pulmones**… mete **muchísimo aire** en la sangre… cuando la sangre **se asusta**, huesos y músculos se calientan». Tanjiro: «**No entiendo nada…**» | **Explicar**: la clase de respiración |
| T1-24 | 00:07:00 a 00:07:36 | Aoi explica el entrenamiento de recuperación: **estiramientos**, **reflejos con tazas de té medicinal** y «**pilla-pilla**» | Tres ejercicios, como una clase |
| T1-25 | 00:00:01 a 00:00:34 | Tanjiro pide a Naho, Kiyo y Sumi que **le peguen con el sacudidor de futones** si deja de respirar dormido. «**¡Tanjiro se esfuerza!**» | La constancia |
| T1-25 | 00:04:29 a 00:04:50 | **Sopla la calabaza pequeña hasta romperla**: «**¡Se rompió!**». Las tres: «**¡Ánimo! ¡Ánimo! ¡Ánimo!**» (頑張れ). Naho: «**Ya sólo falta esta calabaza grande**» | **El objeto: la calabaza (瓢箪, *hyōtan*)** |
| T1-25 | 00:05:20 a 00:05:23 | Zenitsu: «**Esforzarme no es lo mío. Ir poco a poco, constante, es lo más duro**» | La voz del alumno que se rinde |
| T1-25 | 00:06:17 a 00:06:28 | Shinobu: «Lo que Tanjiro quiere aprender se llama **Concentración total: constante**. Respirar así **todo el día** sube la resistencia muchísimo» | **Explicar** (Shinobu) |
| T1-25 | 00:06:54 a 00:07:06 | Tanjiro explica fatal: «**Los pulmones, así, grandes… la sangre se asusta y los huesos hacen ¡BUON! ¡BUON!**… y luego, **entrenar a muerte**» | Chiste: el alumno que explica mal |
| T1-25 | 00:07:14 a 00:07:47 | Shinobu pica a Inosuke: «Es una técnica básica… **lo normal es poder**… ¿**no puedes**? Qué se le va a hacer» | **Regañar** con sonrisa |
| T1-25 | 00:07:58 a 00:08:03 | Shinobu: «**¡Ánimo, Zenitsu! Eres al que más apoyo**». Zenitsu, derretido: «**¡Sííí!**» | **Animar** |
| T1-25 | 00:19:32 | Shinobu a Tanjiro: «**Cuento contigo**» (期待していますね) | Cierre cálido |
| T1-25 | 00:23:12 a 00:23:18 | «Secreto de la era Taisho»: el **té medicinal** de las tazas, echado al baño, cura el cansancio | La cartela propia de la serie (§7) |
| TM-6 | 00:08:50 a 00:08:57 | Rengoku: «**¡Ya haces la concentración constante! ¡Admirable!** Es **el primer paso para ser Pilar**» | **Celebrar** (Rengoku) |
| EP-1 | 00:36:43 a 00:37:09 | Tengen recita **el orden de las clases**: Tokito (**velocidad**), Kanroji (**flexibilidad «del infierno»**), Iguro (**corregir el trazo de la espada**), Shinazugawa (**combate sin fin**), Himejima (**fuerza**) | **Un horario de clases** |
| EP-6 | 00:00:30 | Himejima: «Por último, **empujar esta roca** una distancia de un *chō* (≈ 109 m)» | La prueba final |

### 2.2 Oír: Zenitsu y Tengen (para un canal de música)

| Escena | Minuto | Qué pasa / qué se dice | Para qué sirve |
|---|---|---|---|
| T1-13 | 00:17:35 a 00:18:02 | Zenitsu: «El sonido de un demonio es distinto… pero **de Tanjiro sale un sonido tan amable que dan ganas de llorar**. Los seres vivos **no paran de sonar**: la respiración, el latido, la sangre…» | **Zenitsu oye lo que eres** |
| DR-2 | 00:13:29 a 00:14:10 | Zenitsu, disfrazado de «**Zenko**», **toca el shamisen** con furia en la casa Kyōgoku. Las chicas: «**Qué bien toca**… **tiene buen oído**… dicen que **oye algo una vez y ya lo toca, en shamisen o en koto**» | **La canción que llevas en bucle** |
| DR-3 | 00:03:57 | Se burlan: «¿De qué sirve **mejorar en shamisen y koto**?» | Chiste |
| DR-10 | 00:15:08 a 00:15:27 | Tengen: «**¡La partitura está completa!**». Canta notas (壱、三、七、五、為、巾, nombres de cuerdas del **koto**): «**Ya me sé tu canción asquerosa**» | Tengen, el **Pilar del Sonido** |
| DR-2 | 00:01:11 | Tengen: «Soy el dios de lo **llamativo**… **el dios de las fiestas**» (派手を司る神… 祭りの神だ) | **Presentar** (Tengen) |

### 2.3 Rengoku y el Tren Mugen

| Escena | Minuto | Qué pasa / qué se dice | Para qué sirve |
|---|---|---|---|
| MT | 00:05:45 a 00:06:05 | Rengoku come bentos: «**¡Umai! ¡Umai!**» (¡Rico!; en latino, «**¡Sabroso!**», §10) | El gag más querido |
| TM-1 | 00:01:15 | Otra vez «¡Umai!» (episodio original de TV) | — |
| TM-7 | 00:14:02 a 00:14:21 | «**Creo en tu hermana. La reconozco como miembro del Cuerpo**» | Momento serio |
| TM-7 | 00:14:26 | «**Vive con la frente en alto**» (胸を張って生きろ) | **Animar** |
| TM-7 | 00:14:40 a 00:14:44 | «**Enciende tu corazón**» (心を燃やせ). «**Aprieta los dientes y mira adelante**» | **La frase de Rengoku** |
| MT | 01:44:37 a 01:44:51 | Las mismas frases, en la película | — |

### 2.4 Las frases que todo el mundo conoce (con minuto)

| Frase (traducción mía) | Japonés | Dónde |
|---|---|---|
| «**¡No dejes tu vida en manos de otro!**» (Giyu) | 生殺与奪の権を他人に握らせるな | T1-01, 00:14:52 ✅ |
| «**¡Juzgas muy lento!**» (Urokodaki) | 判断が遅い | T1-02, 00:13:39 ✅ |
| «**Aguanté porque soy el hermano mayor**» (Tanjiro) | 俺は長男だから我慢できたけど | T1-12, 00:19:27 ✅ |
| «**¡Ánimo, Tanjiro, ánimo!**» (se lo dice a sí mismo) | 頑張れ炭治郎 頑張れ | T1-12, 00:21:04 y 00:23:04 ✅ |
| «**¡Embestida de jabalí!**» (Inosuke) | 猪突猛進 | T1-11, 00:20:23 ✅ (y 10 veces más) |
| «**Respiración del Trueno, primera postura: Relámpago**» (Zenitsu) | 雷の呼吸 壱ノ型 霹靂一閃 | T1-12, 00:09:51 ✅ |
| «**A mí no me odia nadie**» (Giyu) | 俺は嫌われてない | T1-21, 00:12:43 ✅ |
| «**¡Orden! ¡Orden! ¡Caw!**» (el cuervo mensajero) | 伝令！伝令！カア〜！ | T1-21, 00:17:32 ✅ |
| «**Si todos, humanos y demonios, nos lleváramos bien…**» (Shinobu) | 人も鬼も みんな 仲良くすればいいのに | T1-15, 00:13:51 ✅ |
| «**Ay, ay… adiós**» (Shinobu, «あらあら») | あらあら… さようなら | T1-24, 00:05:12 ✅ |
| «**Hermano, tú puedes**» (Nezuko, dormida) | お兄ちゃんなら大丈夫 | T1-25, 00:20:54 ✅ |
| «**Aquí, un Secreto de la era Taisho**» | ここで“大正コソコソ噂話” | T1-02, 00:23:17 (y casi cada episodio) ✅ |
| «**¿Lo que escribí…?**» (Kyōgai, el demonio del tambor, que era escritor) | 小生の書いた物は… | T1-13, 00:11:23 ✅ |

### 2.5 El cuervo, el gorrión y los mensajes

| Escena | Minuto | Qué pasa |
|---|---|---|
| T1-05 | «Secreto» del final | El cuervo de Tanjiro **no se presenta**: le da picotazos y amenaza con picotear **al público** si se pierde el capítulo (Kimetsu Wiki, *Taisho Secret*) |
| T1-11 | 00:00:36 a 00:09:07 | **Chuntarō**, el gorrión de Zenitsu, «habla» con Tanjiro (チュン) |
| T1-25 | 00:05:26 a 00:05:51 | Zenitsu le habla al gorrión: «¿Me dijiste “**esfuérzate más**”?» |

---

## 3 · Arte oficial y hojas de contacto

### 3.0 Lo que bajé y miré ✅

- `herramientas/investigar_serie.py` sobre **Kimetsu no Yaiba Wiki**
  (`kimetsu-no-yaiba.fandom.com`), con 12 personajes (Tanjiro, Nezuko,
  Zenitsu, Inosuke, Rengoku, Shinobu, Giyu, Tengen, Mitsuri, Kanao,
  Urokodaki, Muichiro) y 14 páginas de sitios y objetos: **4.314 imágenes**
  grandes en **90 hojas** (`herramientas/referencias/ds-personajes/`) y
  **257** en **6 hojas** (`…/ds-sitios/`). Las ordena de mayor a menor:
  **miré las 6 primeras** de personajes (las 288 más grandes: arte
  oficial) y **las 6 de sitios**, y del resto **busqué por título** en
  `indice.json`. Bajé **unas 110** en alta a mi carpeta de trabajo.
- **Vídeos mirados de verdad** (fotogramas con su minuto; YouTube no deja
  bajar el vídeo desde este contenedor, así que usé su **storyboard**, las
  miniaturas cada 1-2 s que da `yt-dlp -f sb0`; el minuto puede moverse
  **±1-2 s**): opening, ending 1, tráiler latino de *Castillo Infinito*,
  dos clips oficiales de Crunchyroll en Español, dos escenas y un minijuego.
  Todo en §12.
- **Capturas oficiales** del juego (web japonesa y API de Steam): §13.

### 3.1 Las tres hojas de esta carpeta (`hojas/`) — míralas con el número

**`personajes_01.jpg`** (30 imágenes, poses vivas):

| N.º | Qué es | Para qué |
|---|---|---|
| 1 | [Shinobu se presenta](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/a/aa/Shinobu_introducing_herself.png) (2355×2279), espada al hombro entre mariposas | **presentar** (Aula) |
| 2-3 | Shinobu **dedo índice arriba** y luego **palma abierta**, fondo blanco con viñeta (clip CR «¡TODOS necesitamos una Shinobu…», 0:17 y 0:24) | **explicar** |
| 4 | Shinobu con su **cartela de nombre vertical** «蟲柱 胡蝶しのぶ» (T1-20) | el cuadro de nombre (§7) |
| 5 | [Shinobu sonríe a Kanao](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/e/ee/Shinobu_smiling_at_Kanao.png) (2880×1618) | sonrisa tranquila |
| 6 | [Cumpleaños de Shinobu 2025](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/2/2f/Shinobu%27s_birthday_illustration_%282025%29.png) (4096×2898): marco de bento dorado, nudo *mizuhiki*, nombre vertical | el marco oficial (§7) |
| 7 | [Tanjiro, arte del juego](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/a/ad/Tanjiro_visual_Hinokami_Chronicles.png) con el agua | acción |
| 8 | [Tanjiro sopla la calabaza](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/c/ce/Tanjiro_blowing_up_the_gourd.png) (1920×1080), fondo de «impacto» naranja | **el objeto del Aula** |
| 9 | Tanjiro feliz en **ropa de paciente** verde menta (T1-25) | alumno contento |
| 10 | Tanjiro **susurrando con la mano en la boca**, fondo amarillo (clip CR de Rengoku, 0:23): la pose del **Secreto de la era Taisho** («kosokoso» = cuchicheo) | contar un secreto |
| 11 | Tanjiro con el **puño cerrado** delante del telón rojo (1:49) | **animar** |
| 12 | [Tanjiro chibi con megáfono](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/8/84/Tanjiro_Beach_House_Event_2024.png) (2013×2672) | anunciar (chibi) |
| 13 | [Zenitsu de «Zenko», arte del juego](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/e/e0/Zenitsu_Entertainment_District_visual_Hinokami_Chronicles.png) | #que-estas-escuchando |
| 14-15 | **Zenko toca el shamisen** en la casa Kyōgoku (DR-2): de cuerpo entero con rayos verdes, y la cara furiosa con colorete (clip de fan, 0:02 y 0:23) | **la escena del concepto C** |
| 16 | [Cumpleaños de Zenitsu 2024](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/d/dc/Zenitsu%27s_birthday_illustration_%282024%29.png) con Chuntaro | marco de cumpleaños |
| 17 | [Zenitsu lee la carta de Chuntaro](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/5/54/Zenitsu_looks_at_Chuntaro%27s_letter_for_him.png) | mensajes |
| 18 | [Zenitsu, juego 2](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/c/cb/Zenitsu_%28Infinity_Castle%29_visual_Hinokami_Chronicles_2.png) (4088×3685) | acción grande |
| 19 | [Rengoku, arte del juego](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/8/89/Kyojuro_visual_Hinokami_Chronicles.png) entre llamas | celebrar |
| 20 | [Rengoku explica (manga)](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/3/34/Kyojuro_explains_the_beauty_of_humanity.png) | explicar |
| 21 | [Cumpleaños de Rengoku 2024](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/c/cb/Kyojuro%27s_Birthday_Illustration_%282024%29.png), brazos cruzados sobre un pastel | marco |
| 22 | Mitsuri **manos en las mejillas**, colorada (clip CR, 0:48) | emoción |
| 23 | [Mitsuri da clase de cintas](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/2/22/Mitsuri_leads_the_trainees_in_ribbon_dancing.png) en un dojo | **una clase** |
| 24 | [Tengen de paisano](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/2/24/Tengen%27s_undercover_appearance.png) | Tengen sin maquillaje |
| 25 | [Kanao gana en el juego de las tazas](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/2/2a/Kanao_beating_Tanjiro_in_the_water_cup_game.png) | reflejos |
| 26 | [Aoi regaña a Zenitsu](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/0/09/Aoi_scolding_Zenitsu.png) | **regañar** |
| 27-30 | Urokodaki, Nezuko, Inosuke y Giyu, arte del juego *Hinokami* | fichas de acción |

**`objetos_01.jpg`** (30: objetos, cartelas y cuadros):

| N.º | Qué es | Para qué |
|---|---|---|
| 1-3 | **La calabaza**: Tanjiro soplando; las pequeñas en el *engawa*; Kanao y la grande (T1-25) | objeto del Aula |
| 4 | **La mesa de tazas de té medicinal** del dojo (T1-24) | objeto del Aula |
| 5 | [Cartela del Secreto de la era Taisho](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/3/3f/Taisho_Secrets.png) (1940×1090): logo en círculo rojo sobre **ola ukiyo-e** | cuadro propio |
| 6-7 | Secretos de los Herreros y los Pilares: una **tablilla de madera «その1»** | cuadro-objeto |
| 8 | El **telón rojo** del Secreto en el arco de los Pilares | escenario |
| 9 | La cartela **«つづく»** (Continuará) sobre franjas de colores con mariposas | cierre |
| 10 | La cartela **«予告»** (Avance) **dibujada a lápiz** (la Mansión Mariposa) | cartela |
| 11 | [Cuenta atrás de Mugen Train: Rengoku](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/3/36/Mugen_Train_Countdown_%28Kyojuro%29.png) (1200×630): cuadros *ichimatsu*, texto vertical a pincel, «1日» | tipografía |
| 12 | Cartela de nombre vertical de Shinobu | cuadro de nombre |
| 13 | Marco de cumpleaños (bento + *mizuhiki*) | marco |
| 14 | [Diagrama de las respiraciones](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/4/46/Kyojuro_explaining_Breath_Styles_to_Tanjiro.png) del manga (炎 水 雷 岩 風 → 霞, con colores) | **explicar con un esquema** |
| 15 | [Página del manga: la respiración](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/7/7c/Total_Concentration_Breathing_Manga.png) (1116×842) | pulmones dibujados |
| 16-18 | *Hinokami 2*: minijuego del shamisen, «**BEGIN!**» dorado y pantalla «**Success**» con rango S | **UI del concepto C** |
| 19-21 | Cuervos Kasugai, Matsuemon y **Chuntarō con una carta atada** | mensajeros |
| 22-25 | *Tsuba* (guardas) de Tanjiro, Rengoku, Shinobu y Zenitsu | detalles, iconos |
| 26 | [Los tambores de Kyōgai](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/0/06/Kyogai_drumming.png) | sonido |
| 27-28 | Tráiler latino: «**LA FASE FINAL**» y «**Aimer / LiSA**» | letras del tráiler |
| 29 | Opening: el **logo sobre blanco y negro** | logo |
| 30 | [Banner de los Pilares](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/6/66/Hashira_Banner.png) (1500×500) | los nueve kanji |

**`fondos_01.jpg`** (24 sitios; detalle en §5 y §17): 1-5 Mansión
Mariposa (exterior, dojo, *engawa*, tejado de noche, sala abierta al
jardín); 6-8 monte Sagiri (la roca, el bosque, el bambú dorado); 9-10
glicinias y Selección Final; 11-13 Yoshiwara y la casa Kyōgoku; 14 Aldea
de los Herreros; 15 Reunión de los Pilares; 16-17 bosques del
entrenamiento; 18-19 Castillo Infinito; 20-21 ending 1 (ventana ukiyo-e,
*higanbana*); 22 cuadros *ichimatsu*; 23 telón rojo; 24 ola ukiyo-e.

### 3.2 Arte oficial grande, para la pose (no para pegar)

| Imagen | Tamaño | Qué muestra |
|---|---|---|
| [Mugen Train Key Visual 2](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/c/c0/Mugen_Train_Key_Visual_2.jpeg) | 2898×4096 | los cinco con el tren al fondo |
| [Castillo Infinito, key visual IMAX](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/4/48/Infinity_Castle_Trilogy_IMAX_Key_Visual.png) | 2898×4096 | Tanjiro cayendo con el agua |
| [Key visual del arco de los Pilares](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/e/e2/Kimetsu_no_Yaiba_Season_4_Key_Visual.png) | 2300×2168 | todos los Pilares |
| [Key visual «柱、集結» (Reunión de Pilares y Mansión Mariposa)](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/d/d5/Kimetsu_no_Yaiba_Rehabilitation_Training_Arc_Key_Visual.png) | 1448×2048 | los nueve Pilares; en el wiki se llama «Rehabilitation Training Arc Key Visual» |
| [Blu-ray Pilares vol. 3](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/7/72/BD%26DVD_Hashira_Training_Arc_-_Volume_3.png) | 1898×2580 | Mitsuri, Obanai y Gyomei |
| [Blu-ray vol. 5](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/9/9f/BD%26DVD_Volume_5.png) | 1888×2621 | Zenitsu con rayos |
| [Blu-ray vol. 6](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/8/80/BD%26DVD_Volume_6.png) | 1985×2665 | Inosuke en guardia |
| [Cumpleaños de Tengen 2025](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/d/d6/Tengen%27s_birthday_illustration_%282025%29.png) | 4096×2908 | el marco con globos |
| [Cuenta atrás del Castillo: Kanao](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/5/5a/Infinity_Castle_Kanao_Countdown_Visual.png) | 1200×1698 | cartel vertical |
| [Rengoku, evento de otoño 2025](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/c/c7/Kyojuro_Fruitful_Autumn_Festival_Event_2025.png) | 1810×2568 | chibi comiendo boniato |

**Las ilustraciones de cumpleaños** son una serie oficial fija (2020-2026):
formato apaisado 4096×2900, **nombre vertical a pincel** a la derecha,
**fecha vertical** («二月二十四日 生誕») a la izquierda, un **nudo
*mizuhiki*** rojo y blanco, el logo abajo a la derecha y el personaje en
chibi dentro de una **caja de bento** o sobre un **pastel**. Es un recurso
«de la casa» que se puede imitar para una lámina de cumpleaños.

### 3.3 Qué NO usar como arte

- Las fotos de **la obra de teatro** (*Kimetsu no Yaiba The Stage*, en las
  hojas 1-2 de personajes: «profile (Stage Play)»): son **actores reales**.
- Los **fotogramas «2880×1620»** del arco de los Pilares y el Castillo son
  probablemente **reescalados** de 1080p ⚠️ (no lo comprobé): sirven de
  referencia, no para imprimir a ese tamaño.

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D en Sketchfab (licencia leída en la API) ✅

Búsqueda con `api.sketchfab.com/v3/search?type=models&downloadable=true`.
**Ojo**: lo que es de la serie (espadas, la caja de Nezuko) es **fan art en
3D**: la licencia CC cubre el modelo, **no** el diseño de Gotōge. Para una
lámina del servidor, mejor los objetos **genéricos** (calabaza, shamisen,
farol, glicinia).

| Modelo | Autor (Sketchfab) | Licencia | Para qué |
|---|---|---|---|
| [Hyotan Stylized](https://sketchfab.com/3d-models/14210cb7192d484d959e8fa39a36dcdd) | ArtFusion3D | **CC BY** | **la calabaza del Aula**, ya estilizada (7.878 caras) |
| [Sake Gourd 酒 瓢箪](https://sketchfab.com/3d-models/5a09351edc4d48408c086d9c91bf1473) | Pranav_1603 | **CC BY** | calabaza con cordón |
| [Gourd Bottle](https://sketchfab.com/3d-models/fc5c13c5194241339121d8c2e99ae1c7) | akio_illu | **CC BY** | otra calabaza |
| [Gourds! (CC0 en el título)](https://sketchfab.com/3d-models/84186afb78ba4f37b4768afe063f3260) | crufro | la API dice **CC BY** ⚠️ (el título dice CC0: da crédito por si acaso) | calabazas de huerto |
| [Japanese Instrument Shamisen](https://sketchfab.com/3d-models/b7308ba21fb147cb85134ccd001fcd28) | yuleeeee | **CC BY** | shamisen ligero (765 caras) |
| [Shamisen](https://sketchfab.com/3d-models/a67f95529b804e01a1c97f8c8b7935cf) | niarax | **CC BY** | shamisen detallado (18.514 caras) |
| [Shamisen](https://sketchfab.com/3d-models/2a0bc0a696c24d88bd7dae3bb737244a) | lejean | **CC BY-SA** | alternativa (obliga a compartir igual) |
| [Japanese Lantern](https://sketchfab.com/3d-models/5b183cae6d1043f2acddfa177653abae) | afx_cgmotion | **CC BY** | farolillo |
| [Indoor Japanese Lantern](https://sketchfab.com/3d-models/0c233fa266e94686af4f01cab1bdaa96) | xiamilisite | **CC BY** | *andon* de interior |
| [CC0 フジ Japanese Wisteria](https://sketchfab.com/3d-models/b1d89a4c913c4ca192533bbca8a4d448) | ffishAsia-and-floraZia | **CC0** | **glicinia** real (1 M caras: pesada) |
| [Stylized Traditional Japanese House](https://sketchfab.com/3d-models/af3cea94b81a4479a054153a53f7bd57) | White3d | **CC BY** | casa con *engawa* |
| [Nezuko Box](https://sketchfab.com/3d-models/7628220ddf354ea591349e3dd2eca6d6) | OPREXT | **CC BY** (fan) | la caja de Nezuko |
| [Tanjiro's Katana](https://sketchfab.com/3d-models/a611ef5a2829487cbffc3703cec55e80) | Astrien | **CC BY** (fan) | espada de Tanjiro |
| [Rengoku's nichirin sword](https://sketchfab.com/3d-models/2e27e3ea47594d338d78905eb09514d5) | Joschuer | **CC BY** (fan) | espada de Rengoku (3.268 caras) |
| [Shinobu Kochou - Nichirin Blade](https://sketchfab.com/3d-models/2c1e043a55ec48e3a5b363a9858b84f7) | Doverlock | **CC BY-NC** (fan, no comercial) | espada de Shinobu |

Crédito exacto para CC BY: «*Hyotan Stylized* de ArtFusion3D
(sketchfab.com), CC BY 4.0».

### 4.2 Modelos y texturas CC0 (sin crédito obligatorio) ✅

| Recurso | Dónde | Autor | Para qué |
|---|---|---|---|
| [Tea Set 01](https://polyhaven.com/a/tea_set_01) | Poly Haven | Rico Cilliers (modelo), James Ray Cock (textura) | **las tazas del entrenamiento de reflejos** |
| [Sweet Potato](https://polyhaven.com/a/sweet_potato) | Poly Haven | Jan Martens | el **boniato** (la sopa favorita de Rengoku: miso con boniato ✅ Kimetsu Wiki) |
| [Dark Wooden Planks](https://polyhaven.com/a/dark_wooden_planks) | Poly Haven | Amal Kumar | suelo del dojo |
| [Bamboo Wall](https://polyhaven.com/a/bamboo_wall) | Poly Haven | Amal Kumar | la valla de bambú del jardín |
| [Clay Roof Tiles](https://polyhaven.com/a/clay_roof_tiles) | Poly Haven | — | tejado |
| [Tatami 001-006](https://ambientcg.com/view?id=Tatami001) | ambientCG | ambientCG | tatami de la casa Kyōgoku |
| [Paper 001-006](https://ambientcg.com/view?id=Paper005) | ambientCG | ambientCG | papel de la tablilla o de la cartela |
| [Bamboo 001](https://ambientcg.com/view?id=Bamboo001A) | ambientCG | ambientCG | bambú del monte Sagiri |
| [Rope 001](https://ambientcg.com/view?id=Rope001) | ambientCG | ambientCG | el **cordón rojo de la calabaza** (teñir) |

### 4.3 Fan art 2D (mirar, nunca pegar)

| Obra | Autor | Dónde | Para qué |
|---|---|---|---|
| [Fan art de Rengoku tras ver la película](https://i.redd.it/zvt52ie1agw61.jpg) ([hilo](https://reddit.com/r/KimetsuNoYaiba/comments/n2id9u/)) | u/andres1984 | r/KimetsuNoYaiba, 1-may-2021, **3.203 votos** | cuánto mueve Rengoku |
| [Shinobu Kocho](https://www.artstation.com/artwork/aRzDBz) | Fan Yang (jiuge) | ArtStation | pose y color de Shinobu |
| [Shinobu Kocho fan-art](https://www.artstation.com/artwork/xYeLQr) | Anna April | ArtStation («unas 17 horas») | acabado pintado |
| [Shinobu Kocho (escultura para imprimir)](https://www.artstation.com/artwork/AZZyNz) | Mihail Mahmutov para Bulkamancer Sculpts | ArtStation | Shinobu en 3D, volumen |
| [Shinobu Kochō // Fan Art](https://www.artstation.com/artwork/OG320w) | — | ArtStation, 12-jul-2023 | otra pose |

Pixiv y DeviantArt: no los busqué a fondo (se agotaba el cupo de
búsquedas) ⚠️. Pinterest: no usado.

### 4.4 Código y datos en GitHub

| Repositorio | Qué saqué |
|---|---|
| [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv) | **subtítulos japoneses de Netflix** de los 63 episodios y las dos películas: todos los minutos de §2 |
| [google/fonts](https://github.com/google/fonts) | 25 letras bajadas y comprobadas con fontTools (§6) |

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

| Sitio | Dónde sale | Luz y ambiente (lo que vi) |
|---|---|---|
| **Mansión Mariposa** (蝶屋敷) | T1-23 a T1-26; DR-1; EP | De **día**: tejado de dos alturas, pino, farol de piedra, cielo celeste (fondos n.º 1). Dentro, **dojo de madera oscura** con ventanas de papel (n.º 2) y un *engawa* (galería de madera) que da a un **patio de tierra con valla de bambú** (n.º 3). De noche, Tanjiro medita en **el tejado bajo la luna** (n.º 4) |
| **Monte Sagiri** (狭霧山) | T1-02, T1-03 | Niebla, nieve y **la roca** gigante atada con cuerda sagrada (n.º 6). En el opening, bambú **dorado** (0:22) |
| **Monte Fujikasane** (Selección Final) | T1-04 | **Glicinias** moradas que brillan de noche (n.º 9) |
| **Asakusa** | T1-07 | La ciudad moderna de la era Taishō, con luz eléctrica (⚠️ no lo miré en fotograma) |
| **Mansión del tambor** (Tsuzumi) | T1-11 a T1-13 | Madera y **tambores** en un cuarto que gira (objetos n.º 26) |
| **Tren Mugen** | TM, película | Locomotora negra, vagones de madera, noche |
| **Yoshiwara** (Distrito Rojo) | DR | **Noche** con miles de faroles naranjas (n.º 11); la casa **Kyōgoku** con tatami y un **biombo con un pino** pintado (n.º 13) |
| **Aldea de los Herreros** | AH | **Otoño**, luz de atardecer, casas de madera en la ladera (n.º 14) |
| **Jardín de los Ubuyashiki** | T1-21/22; EP-8 | Jardín cuidado, arena rastrillada: aquí es **la Reunión de los Pilares** (n.º 15) |
| **Bosques del entrenamiento** | EP | Bosque, rocas, cascada (n.º 16-17) |
| **Castillo Infinito** (la «fortaleza infinita» en el doblaje) | CI | **Ámbar** y madera, pasillos en todas direcciones, faroles (n.º 18-19) |

### 5.2 Paleta medida con Pillow ✅

(«n.º» = hoja; «clip» = fotograma del storyboard, con su minuto; margen ±5 por canal)

| Qué | Hex | De dónde |
|---|---|---|
| Mansión Mariposa, cielo | `#BEE0E4` | fondos n.º 1 (`Butterfly Mansion Anime.png`) |
| Mansión Mariposa, verde del jardín | `#5F6E54` / `#314541` | fondos n.º 1 |
| Dojo: madera oscura | `#4F3F37` / `#866954`; papel `#C8B5A6` | fondos n.º 2 |
| *Engawa* con las calabazas: tierra y madera | `#C8C08E` / `#9A8C6F`; sombra `#302724` | clip de la calabaza, 0:17 |
| **La calabaza** | `#853920` (sombra), `#B0886A` (luz) | personajes n.º 8 |
| Noche del tejado | `#101923` / `#41515A` | fondos n.º 4 |
| Glicinias | `#AD85EF`, `#664EC2`, `#3A216A`, `#CFADF2` | fondos n.º 9 |
| Yoshiwara de noche | `#1C1116` fondo, **`#C68146`** farol, `#783A2A` | fondos n.º 11 |
| Aldea de los Herreros | `#AE8955`, `#DDC687`, `#7F5233` | fondos n.º 14 |
| Castillo Infinito | `#19110A`, `#3E271A`, `#693D29` | tráiler, 0:01 |
| **Telón rojo del Secreto Taisho** | **`#B91F2A`**, `#860614`, `#5F020C` | clip Shinobu, 0:04 |
| Cartela «つづく»: franjas | `#B3DBD4` menta, `#CF99AA` rosa, `#773A87` morado, `#3D2449` | clip Shinobu, 0:57 |
| Secreto Taisho, la ola | `#3A4B73`, `#74B0D0`, `#D5ECF5`, blanco | objetos n.º 5 |
| Cuenta atrás de Rengoku | `#522924`, `#A47C64`, `#DACBAA` (cuadros *ichimatsu*) | objetos n.º 11 |
| Minijuego del shamisen: mástil | `#93815D`, `#6D583C`, `#C8C7B6` | clip del juego, 0:23 |
| Ending 1: ventana ukiyo-e | `#0B0F47`, `#5A538A`, `#DEC8B5` | clip ED1, 0:11 |
| Ending 1: *higanbana* | `#830D14` sobre negro | clip ED1, 0:01 |

### 5.3 Texturas reales equivalentes

- **Madera oscura** del dojo y el *engawa* → *Dark Wooden Planks* (Poly Haven, CC0).
- **Papel de *shōji*** y de la cartela → *Paper 005* (ambientCG, CC0).
- **Tatami** de la casa Kyōgoku → *Tatami 001* (ambientCG, CC0).
- **Bambú** de la valla y del monte Sagiri → *Bamboo Wall* (Poly Haven) y *Bamboo 001* (ambientCG).
- **La calabaza**: piel lisa y cerosa, marrón rojizo; en Blender, un
  *principled* con rugosidad 0,4 y un poco de *subsurface* ⚠️ (propuesta mía).
- **La cuerda** roja de la calabaza → *Rope 001* (ambientCG), teñida `#A8262A` ⚠️ a ojo.

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

| Dónde | Letra | Estado |
|---|---|---|
| **Logo japonés** 鬼滅の刃 | **caligrafía a pincel propia**, negra, dentro de un **círculo blanco con aro rojo** (como un sello) y furigana «きめつのやいば» encima. No se vende | ✅ visto en el opening (0:11-0:15) y las cartelas; ✅ [dafontonline](https://dafontonline.com/demon-slayer-font/) dice «custom» |
| **Logo occidental** «DEMON SLAYER» | **Blood Crow Condensed**, de Iconian Fonts (Daniel Zadorozny) | ✅ [FontBolt](https://www.fontbolt.com/font/demon-slayer-font/) + [dafontonline](https://dafontonline.com/demon-slayer-font/) |
| «MUGEN TRAIN» en rojo | sans gruesa parecida a **Impact** o **Ignite** | ⚠️ una fuente (FontBolt) |
| **Web oficial del anime** (kimetsu.com/anime, arco de los Pilares, película del Castillo, demonslayer-anime.com) | **Zen Old Mincho** (Google Fonts) y **Noto Serif JP**, con **YakuHanMP** para la puntuación | ✅ **leído en su CSS** |
| **Web del juego *Hinokami*** | **Cinzel** (títulos latinos) y **Noto Serif JP** | ✅ leído en su HTML |
| Cartelas del **tráiler latino** («LA FASE FINAL», «COMIENZA LA BATALLA FINAL», «CANCIONES») | serif clásica en versales, blanca o dorada sobre humo rojo oscuro | ✅ visto (tráiler, 0:09 y 0:53); la letra exacta no la identifiqué ⚠️ (se parece a **Cinzel**) |
| **Cartela de nombre** del anime (蟲柱 胡蝶しのぶ) | **pincel vertical**, negro, con furigana pequeño | ✅ visto (personajes n.º 4) |
| Cuenta atrás de *Mugen Train* | texto vertical a pincel blanco con borde negro, y el número «1日» enorme | ✅ visto (objetos n.º 11) |
| Cartela «**つづく**» | letras redondas a mano, negras con borde blanco | ✅ visto (clip Shinobu, 0:57) |
| Juego *Hinokami 2* | «BEGIN!» y «Success» en **letra de pincel dorada**; números del combo en colores | ✅ visto (clip del minijuego) |
| Globos del manga japonés | la «antigua» (アンチック体): kanji en gótica, kana en mincho, como casi toda la Jump | ⚠️ de memoria |
| Manga en Latinoamérica | Panini México lo edita como *Demon Slayer: Kimetsu no Yaiba*; Ivrea (Argentina) como *Guardianes de la Noche* | ⚠️ de memoria: no comprobé la letra de sus globos |

### 6.2 Letras libres comprobadas por mí con fontTools ✅

Bajé cada archivo (Google Fonts desde su GitHub, Blood Crow desde dafont) y
miré si trae **á é í ó ú ñ Á É Í Ó Ú Ñ ¿ ¡ ü**. **Todas las de la tabla
las traen.**

| Letra | Licencia | ¿Kanji? | Para qué en Demon Slayer |
|---|---|---|---|
| **Blood Crow Condensed** (Iconian) | gratis **sólo no comercial** | no | el «DEMON SLAYER» o un título corto en inglés/español (trae tildes y ñ) |
| **Zen Old Mincho** Black | OFL | sí | **la letra de la web oficial**: textos de la lámina en español con aire de la serie |
| **Noto Serif JP** | OFL | sí | texto largo, sobrio |
| **Shippori Mincho** ExtraBold | OFL | sí | títulos serios (como la cuenta atrás) |
| **Yuji Syuku** | OFL | sí | **pincel**: nombres verticales, cartelas |
| **Yuji Boku** | OFL | sí | pincel más grueso, tipo sello |
| **Yuji Mai** | OFL | sí | pincel fino, elegante (Shinobu) |
| **Kaisei Decol** Bold | OFL | sí | cartel de época Taishō |
| **Zen Antique** | OFL | sí | carteles antiguos, tablilla de madera |
| **Dela Gothic One** | OFL | sí | onomatopeyas y gritos gordos |
| **Rampart One** / **Reggae One** | OFL | sí | rótulos de efecto |
| **Hachi Maru Pop** / **Mochiy Pop One** | OFL | sí | la cartela «つづく» y los chistes chibi |
| **Klee One** | OFL | — | no bajó (enlace roto): no comprobada ⚠️ |
| **Cinzel** | OFL | no | cartelas del tráiler; títulos del juego |
| **Shojumaru** | OFL | no | latín con aire japonés |

### 6.3 Qué letra para qué

- **Nombre del canal** («Aula», «Qué estás escuchando»): **Yuji Boku**, en
  vertical si cabe, como las cartelas de nombre.
- **Texto que dice el personaje**: **Zen Old Mincho** (la de la web
  oficial) en negro sobre papel, o en blanco sobre madera oscura.
- **Etiquetas o números**: **Kaisei Decol** o **Zen Antique** sobre una
  tablilla de madera (el «その1» del Secreto Taisho).
- **Nunca** Blood Crow para frases largas: es un logo, y es no comercial.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

Lo más importante: **Demon Slayer no habla con globos blancos**. En el
anime casi no hay texto sobre la imagen; cuando lo hay, es **caligrafía,
madera, papel o un escenario**. Todo lo de esta sección lo **vi** (hoja,
fotograma o clip con su minuto) salvo lo que lleva ⚠️.

### 7.1 Lo que la serie pone en pantalla

| Recurso | Cómo es | Dónde lo vi |
|---|---|---|
| **Cartela de nombre** (al presentar a un Pilar o a un demonio) | nombre en **pincel vertical negro** sobre el fotograma, con el rango encima en pequeño (蟲柱, «Pilar del Insecto») y el furigana | personajes n.º 4 (T1-20) ✅ |
| **Secreto de la era Taisho** (大正コソコソ噂話, «rumores cuchicheados») | Al final de casi cada episodio. **Temporada 1**: el logo en su círculo rojo sobre una **gran ola ukiyo-e** azul, con Tanjiro y Nezuko en chibi haciendo la «V» (objetos n.º 5). **Herreros y Pilares**: los personajes sujetan una **tablilla de madera «その1»** (n.º 6-7). **Pilares (versión de Crunchyroll)**: un **escenario con telón rojo** `#B91F2A`, luces de teatro y bambalinas; Tanjiro **cuchichea con la mano en la boca** sobre un fondo amarillo (clip de Rengoku, 0:19-0:31) | ✅ vistos |
| Cartela «**つづく**» (Continuará) | letras redondas negras con borde blanco sobre **franjas verticales** de colores con **mariposas** (la de Shinobu: menta, rosa, morado) | clip Shinobu, 0:57 ✅ |
| Cartela «**予告**» (Avance) | el sitio del próximo capítulo **dibujado a lápiz**, en gris, con dos kanji enormes a pincel | objetos n.º 10 (T1-22) ✅ |
| **El cuervo mensajero** (鎹鴉) | grita órdenes: «¡Orden! ¡Orden! ¡Caw!». En los subtítulos japoneses **su voz va en katakana** y con gramática de telegrama («本部ヨリ伝令アリ», «連レ帰レ»): el cuervo habla como un **telegrama** | T1-21, 00:17:32 a 00:17:46 ✅ |
| **Cartas** | Chuntarō, el gorrión, trae **una carta atada a la pata**; los cuervos llevan mensajes | objetos n.º 21 ✅ |
| **El kanji 滅** | bordado en blanco en **la espalda del uniforme** del Cuerpo | fondos n.º 1 ✅ |
| **Grabado de la espada** | los Pilares llevan grabado **惡鬼滅殺** (*akki messatsu*, «destruir a los demonios malvados») en la hoja | ✅ Kimetsu Wiki, fichas de Giyu y Rengoku |
| **Marco de cumpleaños** (serie oficial) | caja de **bento** dorada o pastel, nudo **mizuhiki** rojo y blanco, **nombre y fecha en vertical** | objetos n.º 13 ✅ |
| **Cuenta atrás** (*Mugen Train*) | fondo de **cuadros *ichimatsu***, frase vertical a pincel, «公開まで あと 1日» | objetos n.º 11 ✅ |
| **Diagrama del manga** | Rengoku explica las respiraciones con **un esquema dibujado a mano**: kanji en manchas (炎 水 雷 岩 風 → 霞) con flechas y colores | objetos n.º 14 ✅ |

### 7.2 Cómo piensan

- En el anime, los pensamientos de Tanjiro **se oyen** (voz en off), no se
  escriben. En los subtítulos de Netflix van entre paréntesis con su
  nombre: «（炭治郎） 全集中の呼吸を 長くできるようになれば…» (T1-25,
  00:03:07) ✅.
- **Zenitsu piensa a gritos**: sus monólogos en la cama (T1-25, 00:05:13 a
  00:05:53) son quejas en voz alta al gorrión ✅.
- En el manga, Tanjiro piensa **muchísimo en texto**, en recuadros de
  narración ⚠️ (de memoria; no revisé páginas).

### 7.3 En los videojuegos

- *Hinokami 2*, **minijuego del shamisen de Zenko** (vídeo de STORM MASTER,
  [0:03](https://www.youtube.com/watch?v=VUMxmU9ksIU&t=3) y
  [0:23](https://www.youtube.com/watch?v=VUMxmU9ksIU&t=23)): la barra de
  notas **es el mástil de un shamisen** tumbado (madera `#93815D`, cuerdas
  claras), con la cejuela a la izquierda; las notas son los botones del mando
  en círculos; el combo va en números grandes de colores; «**BEGIN!**» en
  **pincel dorado**; al acabar, «**Success**» dorado, «Total Score» y un
  rango **S** ([0:58](https://www.youtube.com/watch?v=VUMxmU9ksIU&t=58)).
  Detrás, un **biombo con un pino** y dos *geishas*. ✅ visto.
- *Hinokami* (2021): en el modo historia se explora con «**Examinar /
  Hablar**» y se **rastrea el olor** con el gatillo derecho (el olfato de
  Tanjiro) ✅ (manual oficial). En combate, «**el hilo del hueco**» (隙の糸)
  marca el momento de atacar ✅ (manual). **La caja de diálogo del modo
  historia no la vi**: las capturas oficiales vienen sin interfaz ⚠️.

### 7.4 Cómo se traduce a una lámina fija

| Si la lámina necesita… | Usa… |
|---|---|
| que el personaje **se presente** | la **cartela de nombre vertical** a pincel, al lado de su cara |
| que **explique** algo | un **papel o una tablilla** con el esquema dibujado a mano, como el diagrama de Rengoku; o el **fondo blanco con viñeta** de las escenas cómicas (clip Shinobu, 0:17) |
| contar **un dato curioso o una regla** | **el Secreto de la era Taisho**: Tanjiro con la mano en la boca y el texto en la **tablilla de madera** |
| **cerrar** o mandar a otro canal | la cartela **«つづく» / «Continuará»** en franjas de los colores del personaje |
| un **aviso** | **el cuervo**: frase corta, en versales, como un telegrama |
| un canal de **música** | la **barra-mástil de shamisen** del juego, con el texto donde van las notas |

### 7.5 Qué NO hacer con el texto

- **Globo blanco redondo con cola** «de cómic»: en el anime no existe.
- **Letras de terror** (sangre goteando) para todo: el logo occidental lo
  tiene, pero la serie dentro de pantalla es **caligrafía limpia**.
- Poner **kanji inventados** o mal escritos (la gente lee japonés): copia los
  reales de esta biblia (蟲柱, 滅, つづく, 予告).
- Llamarlo «Castillo Infinito» **dentro** del diálogo latino: los personajes
  dicen «**la fortaleza infinita**» (§10.3). «Castillo Infinito» es el título
  de la película.
- «Hashira»: en el doblaje latino son «**Pilares**».

---

## 8 · Los personajes

Carácter: de las fichas de **Kimetsu no Yaiba Wiki** ✅ (secciones
*Personality* y *Trivia*). Forma de hablar: de los **subtítulos japoneses**
(con minuto) ✅ y de lo que vi en los clips. La voz latina, en §10.

### Shinobu Kocho — la Pilar del Insecto (5.ª en la 2.ª encuesta) · la propuesta para el Aula

- **Quién es**: Pilar del Insecto, médica del Cuerpo. **No tiene fuerza
  para cortar cuellos**: mata con **veneno de glicinia** en la punta de su
  espada fina. Dirige la **Mansión Mariposa**, donde se curan y entrenan los
  heridos. Hermana de Kanae (muerta a manos de Doma); hermana mayor
  adoptiva de Kanao.
- **Carácter**: **siempre sonríe**, habla con **cortesía exquisita** y
  **pica** a los demás (sobre todo a Giyu). Esa calma es **una máscara**:
  por dentro arde de rabia contra los demonios (Tanjiro lo **huele**).
  Persuasiva: convence a Inosuke **picándole el orgullo** y a Zenitsu
  **con encanto** (T1-25, 00:07:14 a 00:08:03 ✅). Estricta cuando hace
  falta: regaña a Inosuke por romper una ventana. Quemó los uniformes
  indecentes del sastre Maeda **delante de él** (✅ wiki; fotograma
  [*Shinobu about to burn the uniform*](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/4/41/Shinobu_about_to_burn_the_unform_Masao_gave_her.png), 2880×1622).
- **Cómo habla**: *keigo* suave, frases que empiezan con «あらあら» («ay,
  ay») (T1-24, 00:05:12); explica con **el dedo índice arriba** y luego la
  **palma abierta** (clip CR, 0:17 y 0:24); remata con una puya dulce:
  «**lo normal es poder… ¿no puedes?**». Se ríe bajito («うふふ»).
- **Cómo se enfada**: no sube la voz; **sonríe más** y la vena se le marca
  en la frente ⚠️ (de memoria; la vena sale en los memes).
- **Con quién**: Kanao y Aoi (su casa), las tres niñas, Giyu (su víctima
  favorita), Mitsuri (la otra Pilar mujer: le enseña cocina occidental ✅
  wiki), Tanjiro (le confía su sueño de «llevarse bien con los demonios»).
- **Qué le importa**: que su hermana muera vengada; que Kanao viva.

### Tanjiro Kamado — el protagonista (1.º en la 1.ª encuesta, 4.º en la 2.ª)

- **Quién es**: hijo mayor de una familia que vendía carbón. Su familia
  muere a manos de Muzan; su hermana **Nezuko** se vuelve demonio. Lleva a
  Nezuko en **una caja de madera a la espalda**. Tiene **olfato
  sobrehumano**: huele las emociones.
- **Carácter**: **amable hasta con los demonios** que mata; honesto (no sabe
  mentir: la cara se le deforma); cabezota; **pide ayuda** sin vergüenza.
  Por dentro, **rabia** contra Muzan.
- **Cómo habla**: respetuoso, con «**です/ます**» a los mayores; se
  **anima a sí mismo** en voz alta: «**¡Ánimo, Tanjiro, ánimo!**» y «**soy
  el hermano mayor, aguanto**» (T1-12, 00:19:27 y 00:21:04 ✅). **Explica
  fatal**: «los huesos hacen ¡BUON! ¡BUON!» (T1-25, 00:06:54 ✅). En los
  Secretos Taisho **cuchichea** con la mano en la boca.
- **Lenguaje corporal**: espalda recta, **puño cerrado** delante del
  pecho, ojos muy abiertos; cuando sonríe, **cierra los ojos** del todo
  (personajes n.º 9).
- **Con quién**: Nezuko, Zenitsu, Inosuke; Urokodaki (su maestro); Giyu;
  Rengoku (su modelo); Kanao.

### Nezuko Kamado — la hermana (3.ª en la 1.ª encuesta)

- **Quién es**: demonio que **no come humanos**; duerme para recuperarse;
  lleva un **bozal de bambú** y viaja en la caja. Se hace pequeña o grande.
- **Cómo «habla»**: casi no habla: **gruñidos y «mm»** tras el bambú.
  Cuando habla, pocas palabras y muy dulces: «**Hermano, tú puedes**»
  (dormida, T1-25, 00:20:54 ✅).
- **Lenguaje corporal**: pasos cortos, **da palmaditas en la cabeza** a
  los demás como a sus hermanos (⚠️ de memoria), patadas en combate.

### Zenitsu Agatsuma — el cobarde con talento (2.º en la 1.ª, **1.º en la 2.ª encuesta**)

- **Quién es**: huérfano, alumno del expilar del Trueno Jigoro Kuwajima. Un
  rayo le volvió **el pelo amarillo**. Sólo domina **la primera postura**
  de la Respiración del Trueno, **perfeccionada hasta el extremo**; pelea
  **dormido**. Tiene **un oído prodigioso**: oye el latido y «**el sonido**»
  de cada persona; **toca de oído** el shamisen y el koto tras oír una
  canción **una sola vez** (DR-2, 00:14:10 ✅; manga cap. 72 ✅ wiki).
- **Carácter**: miedoso, pesimista, **llorón**, se cree inútil; **ligón
  desesperado** (pide matrimonio a desconocidas, T1-10/11 ✅); pero
  cuando importa, es valiente. Adora a **Nezuko**.
- **Cómo habla**: **gritando**. Quejas largas, histéricas; insulta cuando
  le da celos («¡Siéntense en seiza!», T1-24, 00:08:10 ✅); habla con su
  gorrión. Dormido, **habla poco y serio**.
- **Con quién**: Tanjiro (el que «suena amable»), Inosuke, Nezuko,
  Chuntarō (su gorrión mensajero), el abuelo Jigoro, Kaigaku (su rival).

### Inosuke Hashibira — el jabalí (5.º en la 1.ª, 6.º en la 2.ª)

- **Quién es**: criado por jabalíes en la montaña; lleva **una cabeza de
  jabalí** como máscara (debajo, cara de chica guapa); **dos espadas
  melladas a pedradas**; torso desnudo.
- **Cómo habla**: a gritos y **sin respetar a nadie**; **no se aprende los
  nombres**: a Tanjiro le llama «**Kamaboko Gonpachirō**» (T1-14, 00:12:25
  ✅; en latino, «**Gonpachipro Kamaboko**», §10) y a Zenitsu «Monitsu»
  (T1-25, 00:06:14 ✅). Su grito: «**¡Embestida de jabalí!**» (猪突猛進,
  11 veces en los subtítulos ✅). Cuando Shinobu le pica: «**¡Claro que
  puedo! ¡No me subestimes!**» (T1-25, 00:07:49 ✅).
- **Con quién**: Tanjiro (le fastidia su amabilidad), Zenitsu, Nezuko (la
  trata como a una madre ✅ wiki), Aoi (le da de comer).

### Kyojuro Rengoku — el Pilar de la Llama (7.º en las dos encuestas; el ídolo de las películas)

- **Quién es**: Pilar de la Llama; protagoniza *Mugen Train*.
- **Carácter**: **entusiasta, ruidoso, puro**. Cree que «el que nace fuerte
  tiene el deber de proteger al débil» (enseñanza de su madre ✅ wiki).
  Muy buen maestro: **ve el talento** en los demás. Come muchísimo; su
  plato favorito es la **sopa de miso con boniato** ✅ wiki.
- **Cómo habla**: **muy alto**, frases cortas y rotundas; «**¡Umai!**»
  (¡Rico!; «**¡Sabroso!**» en latino) comiendo bentos (MT, 00:05:45 ✅);
  «**Umu**» (うむ) para asentir; «**¡Yomoya yomoya da!**» («¡Quién lo
  habría dicho!») ✅; llama a los chicos **por apodo**: «**joven
  Kamado**», «**el chico amarillo**», «**el chico cabeza de jabalí**» (MT,
  01:45:31 ✅). Sus frases: «**Vive con la frente en alto**» y «**Enciende
  tu corazón**» (TM-7, 00:14:26 y 00:14:40 ✅).
- **Lenguaje corporal**: **brazos cruzados**, piernas abiertas, **ojos
  muy abiertos y fijos** (no parpadea), sonrisa enorme (personajes n.º 21).

### Giyu Tomioka — el Pilar del Agua (4.º en la 1.ª, **2.º en la 2.ª**)

- **Quién es**: el primero que encuentra a Tanjiro y le perdona la vida a
  Nezuko. Viste un *haori* **partido en dos**: granate liso y el dibujo
  geométrico de su amigo muerto Sabito.
- **Cómo habla**: **poco, seco, mal**. Grita una vez en toda la serie: «**¡No
  dejes tu vida en manos de otro!**» (T1-01, 00:14:52 ✅). Su meme: «**A mí
  no me odia nadie**» (T1-21, 00:12:43 ✅), cuando todos los demás Pilares
  lo tienen por antipático.

### Kanao, Aoi y las tres niñas — la Mansión Mariposa

- **Kanao Tsuyuri** (8.ª y 10.ª): alumna de Shinobu; **no decide nada**
  sin **lanzar una moneda** (se la dio Kanae); sonríe sin hablar. Es la que
  **revienta la calabaza grande** y gana en las tazas (T1-24/25).
- **Aoi Kanzaki**: la **seria**, organiza la casa y el entrenamiento;
  regaña (personajes n.º 26).
- **Sumi, Kiyo y Naho**: las tres niñas enfermeras; animan a coro «**¡Ánimo!
  ¡Ánimo! ¡Ánimo!**» y pegan a Tanjiro con el **sacudidor de futones** si
  deja de respirar dormido (T1-25 ✅).

### Los otros que salen en la lámina

- **Tengen Uzui**, Pilar del Sonido (13.º): exninja, **tres esposas**,
  joyas en la cabeza, maquillaje. Todo es «**派手**» (*hade*, llamativo): la
  palabra sale **42 veces** en los subtítulos ✅. Se presenta como «**el dios
  de las fiestas**» (DR-2, 00:01:11 ✅). Pelea leyendo **una partitura**.
- **Mitsuri Kanroji**, Pilar del Amor (12.º): pelo rosa y verde (de comer
  *sakuramochi* ✅ wiki), **todo le emociona**, se sonroja, corazones
  alrededor (clip CR, 0:11-0:17). Da **la clase de flexibilidad** con
  **cintas de gimnasia** (personajes n.º 23).
- **Muichiro Tokito**, Pilar de la Niebla (**3.º en la 2.ª encuesta**):
  distraído, frío, mira las nubes; **velocidad** en el entrenamiento.
- **Sakonji Urokodaki**: maestro de Tanjiro, **máscara de tengu roja**
  (la lleva porque su cara es «demasiado amable» ✅ Secreto T1-03). «**¡Juzgas
  muy lento!**» (T1-02).

---

## 9 · ¿Quién es el más querido?

### 9.1 Las encuestas oficiales de la *Weekly Shōnen Jump* ✅

Dos fuentes que coinciden en los números: **Kimetsu no Yaiba Wiki** (ficha
de cada personaje) y **animatetimes**
([resumen 2026](https://www.animatetimes.com/news/details.php?id=1783587640)),
más [GAME Watch](https://game.watch.impress.co.jp/docs/news/1285358.html)
para la 2.ª.

| Puesto | 1.ª encuesta (2017, 18.979 votos) | 2.ª encuesta (2020, 130.316 votos según GAME Watch; «más de 127.000» según animatetimes) |
|---|---|---|
| 1 | **Tanjiro** 6.742 | **Zenitsu** 17.451 |
| 2 | Zenitsu 4.299 | **Giyu** 13.281 |
| 3 | Nezuko 3.319 | **Muichiro** 11.948 |
| 4 | Giyu 2.190 | Tanjiro 9.045 |
| 5 | Inosuke 1.977 | **Shinobu** 8.787 |
| 6 | Shinobu 1.813 | Inosuke 8.750 |
| 7 | Rengoku 1.021 | Rengoku 8.000 |
| 8 | Kanao 712 | Obanai 6.204 |
| 9 | la autora, Gotōge 331 | Sanemi 5.716 |
| 10 | Makomo 294 | Kanao 5.305 |

Otros de la 2.ª: Nezuko 11.ª (5.000), Mitsuri 12.ª (3.714), Tengen 13.º
(3.436), Kokushibo 14.º, Genya 15.º, Enmu 16.º, Akaza 17.º ✅ wiki.
**No hubo tercera encuesta oficial** (animatetimes, 2026).

### 9.2 Lo que dice el público latino y de internet

- **Rengoku** es el fenómeno de las películas: *Mugen Train* fue la
  película de anime más taquillera del mundo hasta que la superó
  *Castillo Infinito* ✅ (Xataka, LOS40). Crunchyroll en Español titula su
  clip «**¡Siempre vivirás en nuestros corazones, Rengoku! 🥹**» (719 mil
  visitas). En Reddit, el fan art de Rengoku «tras ver la película» tiene
  **3.203 votos** (§4.3), y el 21-sep-2026 aún se abren hilos «¿por qué
  quiero tanto a Rengoku?» (Arctic Shift) ✅.
- **Shinobu** tiene el clip latino más visto de los que miré: «**¡TODOS
  necesitamos una Shinobu en nuestras vidas!**», **1,33 millones** de
  visitas ✅.
- **Giyu** vive del meme «**A mí no me odia nadie**» (693 mil visitas en un
  clip de fan latino) ✅.
- **Zenitsu** gana la encuesta grande y es el más memeado por sus gritos.

### 9.3 Qué sale de todo esto

| Para qué canal | Quién | Por qué |
|---|---|---|
| **🔊 Aula** | **Shinobu** | 5.ª en la encuesta grande, **1,3 M** en el clip latino, y **es la profe** de la Mansión Mariposa. Tanjiro (el protagonista) hace de alumno |
| **#que-estas-escuchando** | **Zenitsu** | **1.º** en la encuesta grande y **el del oído**. Un secundario más votado que el protagonista, como pide el dueño |
| Reserva para cualquiera | **Rengoku** | el más querido en Latinoamérica por las películas; sirve para **celebrar** y **animar** |

---

## 10 · Doblaje latino

### 10.1 La producción ✅

| Dato | Valor | Fuente |
|---|---|---|
| ¿Hay doblaje latino? | **Sí**, de toda la serie (63 episodios, 4 temporadas en el recuento de Doblaje Wiki) y de las películas | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Demon_Slayer:_Kimetsu_no_Yaiba) (API) |
| Director (y casting, y adaptación musical) | **Marc Winslow**, que además es la voz de **Giyu** | Doblaje Wiki + [ANMTV 2021](https://www.anmtvla.com/2021/01/demon-slayer-kimetsu-no-yaiba-llega.html) ✅ |
| Estudios | **Universal Cinergía Dubbing** (temp. 1), **SIGE Produciendo** (temp. 2 y la película *Mugen Train*), **Iyuno México** (temp. 3-4 y *Castillo Infinito*). Siempre localizado por **Iyuno** para **Aniplex** | Doblaje Wiki; ANMTV confirma Universal Cinergía ✅ |
| Grabado en | Ciudad de México; **Mérida, Yucatán** (los diálogos de **Cristina Hernández**, Shinobu); **Chile** (los de **René Pinochet**, a distancia) | Doblaje Wiki ⚠️ (una fuente) |
| Cuándo | Temp. 1 grabada en **nov.-dic. de 2020** en **2 semanas y media**, sesiones de 4 horas. *Mugen Train* se grabó en **2 días** | Doblaje Wiki (palabras de Winslow y de Iván Bastidas) ⚠️ |
| Estreno | **Netflix EE. UU. 30-ene-2021**; Netflix Latinoamérica 1-abr-2021; Funimation México 25-mar-2021; Crunchyroll LA 4-oct-2021. En TV abierta, **Canal 5** (México) emitió los ep. 1-10 del **6 al 10 de octubre de 2025** | Doblaje Wiki; ANMTV (Netflix 30-ene) ✅ |
| Lema del director | «**Un proyecto de primera merece un doblaje de primera**» | ANMTV ⚠️ |
| Los libretos | Aniplex mandó guion en inglés **y** traducción del japonés; las adaptadoras mezclaron ambos, leyendo también el manga, para «**conservar el espíritu japonés**» | Doblaje Wiki (tuits de Clemen Larumbe) ⚠️ |

**Por qué importa aquí**: *Castillo Infinito* (estreno en cines el **11 de
septiembre de 2025**, con doblaje) es **la película de anime más taquillera
de la historia en México** (184 millones de pesos en su primer fin de
semana, unos 2,3 millones de espectadores) y en casi toda Latinoamérica,
Perú incluido ✅ ([Xataka México](https://www.xataka.com.mx/anime/demon-slayer-castillo-infinito-rompe-todos-records-mexico-supero-a-dragon-ball-mejor-debut-para-pelicula-anime),
[LOS40 México](https://los40.com.mx/2025/09/30/demon-slayer-kimetsu-no-yaiba-castillo-infinito-rompe-records-en-latinoamerica/?outputType=amp),
[Merca2.0](https://www.merca20.com/demon-slayer-castillo-infinito-rompe-record-y-se-convierte-en-la-pelicula-mas-taquillera-de-anime-en-la-historia-de-mexico/)).
Llega a Netflix, Prime Video y Disney+ Latinoamérica el **28-sep-2026** y a
HBO Max el 29-sep-2026 (Doblaje Wiki): **justo esta semana**.

### 10.2 Las voces (cada nombre con dos fuentes)

| Personaje | Voz latina | Voz japonesa | Estado |
|---|---|---|---|
| **Tanjiro Kamado** | **Iván Bastidas** (elegido directo, sin audición) | Natsuki Hanae | ✅ Doblaje Wiki + ANMTV + SensaCine |
| **Nezuko Kamado** | **Annie Rojas** | Akari Kitō | ✅ Doblaje Wiki + ANMTV |
| **Zenitsu Agatsuma** | **José Luis Piedra** | Hiro Shimono | ✅ Doblaje Wiki + ANMTV |
| **Inosuke Hashibira** | **Uraz Huerta** (José Ángel Torres fue la otra opción) | Yoshitsugu Matsuoka | ✅ Doblaje Wiki + ANMTV |
| **Kyojuro Rengoku** | **Irwin Daayán** | Satoshi Hino | ✅ Doblaje Wiki + ANMTV |
| **Shinobu Kocho** | **Cristina Hernández** (desde Mérida) | Saori Hayami | ✅ Doblaje Wiki + ANMTV |
| **Giyu Tomioka** | **Marc Winslow** | Takahiro Sakurai | ✅ Doblaje Wiki + ANMTV |
| **Tengen Uzui** | **Alfredo Gabriel Basurto** | Katsuyuki Konishi | ✅ Doblaje Wiki + ANMTV («Gabriel Basurto») |
| **Mitsuri Kanroji** | **Meli G** (Melissa Gedeón) | Kana Hanazawa | ✅ Doblaje Wiki + ANMTV |
| **Gyomei Himejima** | **Gerardo Reyero** (el Freezer latino) | Tomokazu Sugita | ✅ Doblaje Wiki + ANMTV |
| **Sakonji Urokodaki** | **Alejandro Villeli** | Hōchū Ōtsuka | ✅ Doblaje Wiki + ANMTV |
| **Kagaya Ubuyashiki** | **Idzi Dutkiewicz** | Toshiyuki Morikawa | ✅ Doblaje Wiki + ANMTV |
| **Kanao Tsuyuri** | **Montserrat Aguilar** | Reina Ueda | ✅ Doblaje Wiki + ANMTV |
| **Muzan Kibutsuji** | **Luis Leonardo Suárez** | Toshihiko Seki | ✅ Doblaje Wiki + ANMTV |
| **Muichiro Tokito** | **Armando Corona** | Kengo Kawanishi | ✅ Doblaje Wiki + resumen de Xataka/Geekmi |
| Obanai Iguro | Arturo Cataño | Kenichi Suzumura | ⚠️ sólo Doblaje Wiki |
| Sanemi Shinazugawa | Galo Balcázar | Tomokazu Seki | ⚠️ sólo Doblaje Wiki |
| Akaza | José Antonio Toledano | Akira Ishida | ⚠️ sólo Doblaje Wiki |
| Doma | Alan Fernando Velázquez | Mamoru Miyano | ⚠️ sólo Doblaje Wiki |
| Aoi Kanzaki | Miriam Aceves | Yuri Ehara | ⚠️ |
| Sumi / Kiyo / Naho | Rosa Obdulia / **Elizabeth Infante** (la Anya latina) / Jocelyn Meneses | — | ⚠️ |
| Kotetsu | Jorge Rafael | Ayumu Murase | ⚠️ |
| Hotaru Haganezuka | Manuel Pérez | Daisuke Namikawa | ⚠️ |
| Shinjuro Rengoku (el padre) | **Mario Castañeda** (el Goku latino) | Rikiya Koyama | ⚠️ sólo Doblaje Wiki |
| Enmu | Arturo Castañeda | Daisuke Hirakawa | ⚠️ |
| Kokushibo | Octavio Rojas | Ryōtarō Okiayu | ⚠️ |
| Genya | Osvaldo Trejo Rodríguez (temp. 1-2) → **Luis Fernando Orozco** (desde temp. 3, por el fallecimiento de Trejo) | Nobuhiko Okamoto | ⚠️ |

### 10.3 Datos de interés del doblaje (Doblaje Wiki, «Datos de interés»)

- Winslow tuvo que proponer **tres voces por personaje** al cliente.
- A Winslow le habían asignado primero a **Zenitsu**; no se vio en él y
  se quedó con Giyu (lo contó en el canal de YouTube **Pratz**).
- **Mario Castañeda y Rommy Mendoza** hacen de los padres de Rengoku en
  *Mugen Train*; en la vida real fueron marido y mujer.
- En *Mugen Train* se **reusaron los mismos «loops»** (voces de fondo) que
  en la película para el arco de TV.
- **«Hashira» se tradujo como «Pilar»** (el ep. 15 dice «Hashira» por error).
  Y «Mugen-jō» (無限城) se dice **«la fortaleza infinita»** en los diálogos,
  aunque el cartel latino diga «Castillo Infinito». En España, «La
  fortaleza infinita» en todo.
- El doblaje **tiene groserías** («Doblaje con groserías» en su ficha).
- Winslow **pidió al estudio que propusiera al cliente doblar el opening y el ending**, y ya tenía pensadas las voces. **No consta que se hiciera**: los clips oficiales suenan con *Gurenge* en japonés ⚠️.
- La única canción doblada que registra Doblaje Wiki es la **canción de cuna de Kie Kamado** (ep. 40), con intérprete sin identificar.
- Error famoso de créditos: a Tanjiro lo acreditan como «**Tanjito**».

### 10.4 Frases propias del doblaje latino

| Quién | Frase latina | Dónde | Estado |
|---|---|---|---|
| **Kotetsu** (Jorge Rafael) | «**¿Qué pashó, papu?**» | temp. 3, ep. 2 (Villa de los Herreros), cuando entrena a Tanjiro | ✅ Doblaje Wiki + la guía de cuadros (`_ya_hechas`) |
| **Rengoku** (Irwin Daayán) | «**¡Sabroso!**» por su «*¡Umai!*» (うまい) comiendo bentos en el tren | *Mugen Train* 00:05:45 en japonés; temp. 2 ep. 1 | ✅ dos vídeos de fans con ese título: [«SABROSO!»](https://www.youtube.com/watch?v=_RCI2nqPqDc) y [reacción «¡¡SABROSO!!»](https://www.youtube.com/watch?v=OU5BOAMBdxQ). No es fuente oficial |
| **Giyu** (Marc Winslow) | «**A mí no me odia nadie**» (俺は嫌われてない, «no es que me odien») | ep. 21, 00:12:43 en japonés | ⚠️ una fuente: clip de fan [«A mí no me odia nadie - Tomioka»](https://www.youtube.com/watch?v=GhFhePAHo3w) (693 mil visitas) |
| **Inosuke** | «**Pues Gonpachipro Kamaboko**» (el nombre mal dicho de Tanjiro, en el avance del ep. 16) | avance del ep. 16 | ✅ Doblaje Wiki (dato técnico) |
| Una dama de la casa Ogimoto | «**Me llamo Gaby, y soy de la casa Ogimoto**» (el nombre es el de su actriz, Gaby Willer) | ep. 35 | ⚠️ Doblaje Wiki |
| **Rengoku** | «**Enciende tu corazón**» (心を燃やせ) | temp. 2 ep. 7, 00:14:40; *Mugen Train* 01:44:51 en japonés | ⚠️ sólo el título de un vídeo de fan que compara idiomas ([Xoso](https://www.youtube.com/watch?v=Av8IyxCc_bM)); no sé si es el audio latino o el de España. **Escúchalo antes de usarlo** |

Títulos de clips oficiales de **Crunchyroll en Español** (comprobados con
`yt-dlp`; dan el tono del doblaje y de su comunidad):

| Clip | Duración | Visitas | Fecha |
|---|---|---|---|
| [«¡TODOS necesitamos una Shinobu en nuestras vidas!»](https://www.youtube.com/watch?v=OQ-S0SYxOGI) | 1:10 | 1,33 M | 8-jul-2024 |
| [«Nadie quiere a Mitsuri 💔»](https://www.youtube.com/watch?v=nKKm-7Y3UZw) (Herreros ep. 4) | 1:05 | 862 mil | 9-may-2023 |
| [«¡Siempre vivirás en nuestros corazones, Rengoku! 🥹»](https://www.youtube.com/watch?v=cTsMylsTCWA) | 2:05 | 719 mil | 26-ago-2024 |
| [«Mi compa casi no la contaba»](https://www.youtube.com/watch?v=xW8kvEcEVQA) (Pilares) | 0:50 | 343 mil | 5-ago-2024 |
| [«¡Te quiero mucho, Tokito! ✨♥»](https://www.youtube.com/watch?v=VlRmK1QnbK8) (Pilares) | 0:50 | 413 mil | 29-jul-2024 |
| [«¡No te merecemos, Gyomei! 😭»](https://www.youtube.com/watch?v=rEBmrpu0_g0) (Pilares) | 0:50 | 255 mil | 12-ago-2024 |
| [«¡Te presento a Filemón!»](https://www.youtube.com/watch?v=V-b9uoyTnYk) (Herreros ep. 7) | 1:05 | 51 mil | 13-jun-2023 |
| [Tráiler en español de *Castillo Infinito*](https://www.youtube.com/watch?v=SKQWT0As7oc) | 1:30 | 1,43 M | 1-sep-2025 |
| [Tráiler doblado, Sony Pictures México](https://www.youtube.com/watch?v=sqgSm8fWe1s) | 1:30 | 461 mil | 1-sep-2025 |

Ojo con «¡Te presento a Filemón!»: por el título, el doblaje le puso un
**nombre latino** a algo o a alguien del ep. 7 de los Herreros; **no lo pude
comprobar** sin ver el vídeo ⚠️.

### 10.5 Dónde oír a los actores contar su trabajo

| Vídeo | Duración | Para qué |
|---|---|---|
| [«Detrás de la voz de Inosuke», Uraz Huerta con Pratz y Kumaru](https://www.youtube.com/watch?v=ydYTmycYs2M) | 25:21 | cómo hace los gritos de Inosuke |
| [«Detrás de la voz de Tomioka», Marc Winslow con Pratz](https://www.youtube.com/watch?v=kMDucA2CdUs) | 27:10 | la dirección de toda la serie (306 mil visitas) |
| [Marc Winslow con Idzi Dutkiewicz: «No quería dirigir Demon Slayer»](https://www.youtube.com/watch?v=QvK7-cPWRbo) | 2:08:43 | 22-jun-2026; Idzi es la voz de Kagaya |
| [Iván Bastidas, Winslow, Piedra y Huerta en la Friki Feria (31-jul-2022)](https://www.youtube.com/watch?v=yibRjVzbJgU) | 1:02:11 | los cuatro juntos en un panel |
| [Iván Bastidas en Otakon 2026](https://www.youtube.com/watch?v=1eq-zSbcX3c) | 12:12 | la voz de Tanjiro, entrevista reciente |
| TikTok de Marc Winslow: [Irwin Daayán grabando a Rengoku](https://www.tiktok.com/@marcwinslow/video/7091738912200150278) | — | la cabina, de verdad |
| TikTok de SDV: [«Reto de doblaje n.º 874, Kyōjurō Rengoku»](https://www.tiktok.com/@sdv_serviciosdevoz/video/7212717526587870470), retando a Irwin Daayán | — | **ya existe el formato «reto» con Demon Slayer** |

No encontré subtítulos latinos descargables de ningún clip (YouTube pide
«no soy un robot»): las frases latinas salen de títulos y de Doblaje Wiki,
no del audio.

---

## 11 · Música

### 11.1 Openings, endings y canciones (lista de [Kimetsu no Yaiba Wiki](https://kimetsu-no-yaiba.fandom.com/wiki/Kimetsu_no_Yaiba_(Anime))) ✅

| Arco | Opening | Ending |
|---|---|---|
| Temporada 1 (1-26) | **«Gurenge»** (紅蓮華), **LiSA** | «from the edge», FictionJunction feat. LiSA |
| Tren Mugen TV (27-33) | «Akeboshi» (明け星), LiSA | «Shirogane» (白銀), LiSA; el ep. 33 cierra con **«Homura»** (炎) |
| Distrito Rojo (34-44) | «Zankyōsanka» (残響散歌), **Aimer** | «Asa ga Kuru» (朝が来る), Aimer |
| Aldea de los Herreros (45-55) | «Kizuna no Kiseki», MAN WITH A MISSION × milet | «Koi Kogare», los mismos |
| Pilares (56-63) | «Mugen» (夢幻), MY FIRST STORY × HYDE | «Tokoshie», los mismos |
| Película *Mugen Train* | **«Homura»**, LiSA | — |
| Película *Castillo Infinito* | «A World Where the Sun Never Rises» (太陽が昇らない世界), **Aimer** | «Shine in the Cruel Night» (残酷な夜に輝け), **LiSA** |

**Canciones dentro de la serie** ✅:
- **«Kamado Tanjirō no Uta»** (竈門炭治郎のうた), de **Go Shiina** con
  **Nami Nakagawa**: suena **en la pelea contra Rui** (ep. 19, «Hinokami»)
  y cierra el capítulo; dura 5:32. Es el momento musical más famoso de la
  serie ⚠️ (lo de «el más famoso» es opinión mía, por las visitas).
- «Kamado Nezuko no Uta», ep. 55.
- **La canción de cuna de Kie Kamado** (ep. 40): **la única doblada al
  español latino** que registra Doblaje Wiki.
- En la banda sonora del Distrito Rojo hay una pista llamada **«Zenitsu
  ~Shamisen Breathing~»** (vídeo [yVowrhZtFbE](https://www.youtube.com/watch?v=yVowrhZtFbE), 1:41) ⚠️ (una fuente).

### 11.2 Qué ambiente dan (lo que vi y oí de oídas)

- **Gurenge**: rock rápido. El opening (visto por fotogramas, §12) va del
  **blanco y negro con ojos rojos** al color: entrenamiento dorado,
  noche azul, agua en espiral.
- **from the edge**: lento, triste; *higanbana* rojas sobre negro y una
  **ventana redonda de estilo ukiyo-e** con nubes doradas (visto, §12).
- **Kajiura y Shiina**: coros, taiko, shamisen y cuerdas; lo japonés
  antiguo mezclado con orquesta ⚠️ (de oídas).

### 11.3 Qué música pega a cada lámina

| Lámina | Tema | Por qué |
|---|---|---|
| Aula (Mansión Mariposa) | la música tranquila del entrenamiento (T1-24/25) ⚠️ | día, esfuerzo, humor |
| #que-estas-escuchando | **«Gurenge»** (el más conocido en Latinoamérica) o la pista del shamisen | el canal es de canciones en bucle |
| Rengoku | **«Homura»** | cierra su historia |

---

## 12 · Vídeos

**Cómo los miré**: YouTube pide «no soy un robot» a este contenedor y no
deja bajar el vídeo ni los subtítulos (probé los clientes `web`, `mweb`,
`tv`, `android_vr`, `web_safari` y el `timedtext` directo: todos bloqueados
o sin formatos). Sí deja bajar **el storyboard** (`-f sb0`): miniaturas de
160×90 o 320×180 **cada 1-2 s** (cada 5 s en el vídeo largo). Las monté en
hojas con el minuto y **las miré una a una**. El minuto es aproximado
(**±1-2 s**). Los datos (título, duración, fecha, visitas) salen de
`yt-dlp -j`.

### 12.1 Los vídeos que miré (con minuto y enlace)

| Vídeo | Canal · duración · visitas | Qué vi, con minuto |
|---|---|---|
| [Opening 1, «Gurenge»](https://www.youtube.com/watch?v=pmanD_s7G3U) | animelab (distribuidora) · 1:29 · 168,8 M | [0:00](https://www.youtube.com/watch?v=pmanD_s7G3U&t=0) bosque nevado **en blanco y negro**, Tanjiro con la caja · [0:10](https://www.youtube.com/watch?v=pmanD_s7G3U&t=10) primer plano de **ojos rojos** en B/N · [0:11-0:15](https://www.youtube.com/watch?v=pmanD_s7G3U&t=11) **el logo** sobre Tanjiro · [0:18-0:24](https://www.youtube.com/watch?v=pmanD_s7G3U&t=18) entrenamiento con luz **dorada**; Urokodaki en el bambú · [0:26-0:30](https://www.youtube.com/watch?v=pmanD_s7G3U&t=26) Sabito y Makomo de noche, azul verdoso · [0:38](https://www.youtube.com/watch?v=pmanD_s7G3U&t=38) Kanao con una mariposa al atardecer · [1:03](https://www.youtube.com/watch?v=pmanD_s7G3U&t=63) Kyōgai y sus tambores · [1:08](https://www.youtube.com/watch?v=pmanD_s7G3U&t=68) **luna roja** con siluetas · [1:13-1:18](https://www.youtube.com/watch?v=pmanD_s7G3U&t=73) rayo amarillo de Zenitsu y **dragón de agua** · [1:20](https://www.youtube.com/watch?v=pmanD_s7G3U&t=80) Tanjiro y Nezuko **de la mano** |
| [Ending 1, «from the edge», sin créditos](https://www.youtube.com/watch?v=j1KxC7eaBVs) | AniPortFX (fan, reescalado) · 2:07 · 109 mil | [0:01](https://www.youtube.com/watch?v=j1KxC7eaBVs&t=1) ***higanbana*** rojas sobre negro · [0:05-0:15](https://www.youtube.com/watch?v=j1KxC7eaBVs&t=5) Nezuko flotando **boca abajo** con cintas rojas ante una **ventana redonda** morada con **nubes doradas** estilo ukiyo-e · [0:21-0:29](https://www.youtube.com/watch?v=j1KxC7eaBVs&t=21) la familia feliz, luz de día · [0:37-0:41](https://www.youtube.com/watch?v=j1KxC7eaBVs&t=37) fondos de **tinta sumi-e** salpicada · [0:43](https://www.youtube.com/watch?v=j1KxC7eaBVs&t=43) los hermanos de la mano bajo las estrellas |
| [«Asa ga Kuru», MV oficial del ending del Distrito Rojo](https://www.youtube.com/watch?v=QORbTrXHpsA) | Aimer · 4:51 · — | **no es anime**: actores, **sombrillas *wagasa* rojas**, pasillos de *shōji*, una **ventana redonda con glicinias** ([1:03](https://www.youtube.com/watch?v=QORbTrXHpsA&t=63)). Sirve sólo de ambiente |
| [Tráiler en español de *Castillo Infinito*](https://www.youtube.com/watch?v=SKQWT0As7oc) | Crunchyroll en Español · 1:30 · 1,43 M · 1-sep-2025 | [0:01](https://www.youtube.com/watch?v=SKQWT0As7oc&t=1) el castillo en **ámbar**, cientos de faroles · [0:09](https://www.youtube.com/watch?v=SKQWT0As7oc&t=9) cartela «**LA FASE FINAL**» en serif blanca sobre humo rojo · [0:18](https://www.youtube.com/watch?v=SKQWT0As7oc&t=18) «Producción de Animación ufotable» · [0:40-0:43](https://www.youtube.com/watch?v=SKQWT0As7oc&t=40) Shinobu frente al estanque de lotos de Doma · [0:47-0:50](https://www.youtube.com/watch?v=SKQWT0As7oc&t=47) **Zenitsu serio**, ojos en sombra · [0:53](https://www.youtube.com/watch?v=SKQWT0As7oc&t=53) «**COMIENZA LA BATALLA FINAL**» · [0:57](https://www.youtube.com/watch?v=SKQWT0As7oc&t=57) «**Aimer**» en azul, «**LiSA**» en rojo, con brillo |
| [Clip «¡TODOS necesitamos una Shinobu en nuestras vidas!»](https://www.youtube.com/watch?v=OQ-S0SYxOGI) | Crunchyroll en Español · 1:10 · 1,33 M | es **un Secreto de la era Taisho** del arco de los Pilares: [0:00-0:09](https://www.youtube.com/watch?v=OQ-S0SYxOGI&t=0) Tanjiro de pie ante un **telón rojo** · [0:17-0:23](https://www.youtube.com/watch?v=OQ-S0SYxOGI&t=17) Shinobu **dedo índice arriba** sobre fondo blanco con viñeta · [0:24-0:27](https://www.youtube.com/watch?v=OQ-S0SYxOGI&t=24) **palma abierta** · [0:28-0:33](https://www.youtube.com/watch?v=OQ-S0SYxOGI&t=28) Inosuke **colorado**, fondo amarillo con brillos · [0:39-0:48](https://www.youtube.com/watch?v=OQ-S0SYxOGI&t=39) Mitsuri con las **manos en las mejillas** y Shinobu sonriendo · [0:57](https://www.youtube.com/watch?v=OQ-S0SYxOGI&t=57) cartela «**つづく**» |
| [Clip «¡Siempre vivirás en nuestros corazones, Rengoku!»](https://www.youtube.com/watch?v=cTsMylsTCWA) | Crunchyroll en Español · 2:05 · 719 mil | otro Secreto: [0:01](https://www.youtube.com/watch?v=cTsMylsTCWA&t=1) telón rojo · [0:11-0:17](https://www.youtube.com/watch?v=cTsMylsTCWA&t=11) Mitsuri salta con **corazones** y rayitas amarillas · [0:19-0:31](https://www.youtube.com/watch?v=cTsMylsTCWA&t=19) **Tanjiro cuchichea con la mano en la boca** · [0:48-1:00](https://www.youtube.com/watch?v=cTsMylsTCWA&t=48) Mitsuri emocionada · [1:02](https://www.youtube.com/watch?v=cTsMylsTCWA&t=62) **brazos abiertos** · [1:08](https://www.youtube.com/watch?v=cTsMylsTCWA&t=68) dibujo de **Rengoku comiendo** con Mitsuri y Senjuro · [1:31-1:41](https://www.youtube.com/watch?v=cTsMylsTCWA&t=91) **las bambalinas** del teatro · [1:47-1:51](https://www.youtube.com/watch?v=cTsMylsTCWA&t=107) Tanjiro con **el puño** |
| [Tanjiro y las calabazas (Latino)](https://www.youtube.com/watch?v=Mi_vqp2GB-Y) | PikaMauri 64 (fan) · 0:29 | [0:00](https://www.youtube.com/watch?v=Mi_vqp2GB-Y&t=0) Tanjiro en **ropa de paciente** en el *engawa*, feliz · [0:04](https://www.youtube.com/watch?v=Mi_vqp2GB-Y&t=4) Kiyo y Sumi · [0:11](https://www.youtube.com/watch?v=Mi_vqp2GB-Y&t=11) cara cómica de susto · [0:12-0:24](https://www.youtube.com/watch?v=Mi_vqp2GB-Y&t=12) sentados en el *engawa* frente a **la valla de bambú**, con **las calabacitas en el suelo de madera** · [0:25](https://www.youtube.com/watch?v=Mi_vqp2GB-Y&t=25) Kanao de cerca |
| [Zenitsu toca rápido el shamisen](https://www.youtube.com/watch?v=l35HAO3U1gU) | PikaMauri 64 (fan) · 0:29 | [0:01-0:06](https://www.youtube.com/watch?v=l35HAO3U1gU&t=1) Zenko en un cuarto de **tatami** con **biombo de pino**, rodeado de chicas, con **rayos verdes** · [0:07-0:14](https://www.youtube.com/watch?v=l35HAO3U1gU&t=7) las chicas miran asombradas · [0:15-0:22](https://www.youtube.com/watch?v=l35HAO3U1gU&t=15) Zenitsu **de espaldas**, kimono naranja y *obi* granate · [0:23-0:28](https://www.youtube.com/watch?v=l35HAO3U1gU&t=23) cara **furiosa** con colorete rojo |
| [Minijuego «Zenko's Shamisen Jams» (*Hinokami 2*)](https://www.youtube.com/watch?v=VUMxmU9ksIU) | STORM MASTER · 3:23 | §7.3 y §13 |
| [ufotable explica la animación de *Castillo Infinito*](https://www.youtube.com/watch?v=FLB_sLTgbPk) | **Oscars** («Scene at the Academy») · 9:28 · 1,27 M · 11-ene-2026 | **entrevista al staff**, con subtítulos en inglés en la imagen: [0:29](https://www.youtube.com/watch?v=FLB_sLTgbPk&t=29) «ufotable sigue dibujando **cada fotograma a mano**» · [0:39](https://www.youtube.com/watch?v=FLB_sLTgbPk&t=39) «hay cosas que **sólo cierto artista** puede dibujar, y sólo en ese momento» · [1:39](https://www.youtube.com/watch?v=FLB_sLTgbPk&t=99) «los **23 tomos** del manga pasan de **200 millones** de copias» · [2:19](https://www.youtube.com/watch?v=FLB_sLTgbPk&t=139) «tienen en plantilla **cinco veces más** animadores 2D» · [2:24](https://www.youtube.com/watch?v=FLB_sLTgbPk&t=144) «**más de 2.200 planos** a mano» · [2:59](https://www.youtube.com/watch?v=FLB_sLTgbPk&t=179) **Hikaru Kondo** (presidente de ufotable) decidió «cuándo, dónde y quién hace qué» mientras escribía el guion · [3:09](https://www.youtube.com/watch?v=FLB_sLTgbPk&t=189) el director **Haruo Sotozaki** y el jefe de animación **Akira Matsushima** revisaron **todos los dibujos clave** · [4:44](https://www.youtube.com/watch?v=FLB_sLTgbPk&t=284) **Yuichi Terao** (fotografía): «el ordenador dijo que tardaría **10 años** en renderizar» el castillo · [5:43](https://www.youtube.com/watch?v=FLB_sLTgbPk&t=343) **Toshiyuki Shirai** (storyboard): un efecto de 3 s lleva **cientos de hojas** |

### 12.2 Otros vídeos útiles (sólo datos, no mirados fotograma a fotograma)

| Vídeo | Datos | Para qué |
|---|---|---|
| [PV 1 del arco de los Pilares](https://www.youtube.com/watch?v=Tf31dGdlWxE) | Aniplex · 1:38 · **5,5 M** | su descripción trae **el staff completo** ✅: dirección **Haruo Sotozaki**; diseño de personajes y jefe de animación **Akira Matsushima**; dirección de arte **Masaru Yanaka** y **Yuri Kabasawa**; supervisión de arte **Kōji Etō**; fotografía **Yuichi Terao**; 3D **Kazuki Nishiwaki**; color **Yūko Ōmae**; música **Yuki Kajiura y Go Shiina** |
| [Vídeo especial «Kamado Tanjirō no Uta»](https://www.youtube.com/watch?v=ckGTdMYV6Xg) | ufotable · 5:39 · 607 mil · 16-ago-2026 | reestreno del ep. 19 |
| [LiSA, «Gurenge» (MV)](https://www.youtube.com/watch?v=x1FV6IrjZCY) | LiSA Official · 3:55 · **31,3 M** | letra de LiSA, música de Kayoko Kusano ✅ |
| [LiSA, «Gurenge» en THE FIRST TAKE](https://www.youtube.com/watch?v=MpYy6wwqxoo) | 5:30 · **149 M** · 6-dic-2019 | la versión a piano: la **tendencia** más vista |
| [«The Secret Behind Demon Slayer's Animation»](https://www.youtube.com/watch?v=lEkLJX0q6gs) | Damon Billiot · 13:27 · 965 mil | capítulos: [2:33](https://www.youtube.com/watch?v=lEkLJX0q6gs&t=153) animación técnica, [5:22](https://www.youtube.com/watch?v=lEkLJX0q6gs&t=322) **composición y 3D**, [7:15](https://www.youtube.com/watch?v=lEkLJX0q6gs&t=435) *genga* |
| [Tráiler doblado de *Castillo Infinito*](https://www.youtube.com/watch?v=sqgSm8fWe1s) | Sony Pictures México · 1:30 · 461 mil | tráiler de cines |

### 12.3 Tendencias de TikTok

- **SDV (Servicios de Voz)** hace «**Reto de doblaje**» con escenas de la
  serie y reta a la voz oficial: el **n.º 874 es Rengoku**, retando a Irwin
  Daayán ([TikTok](https://www.tiktok.com/@sdv_serviciosdevoz/video/7212717526587870470)) ✅.
- **Marc Winslow** sube a su TikTok **grabaciones de cabina** (Irwin Daayán
  grabando a Rengoku) ✅.
- En YouTube hay fandubs latinos: «Reto de doblaje "Shinobu"» y «Shinobu
  anima a Zenitsu (Fandub Español Latino)» ✅ (títulos de `ytsearch`).
- No pude abrir TikTok para medir visitas ni minutos ⚠️.

---

## 13 · Videojuegos de la franquicia

| Juego | Datos | Lo que sirve para una lámina |
|---|---|---|
| ***The Hinokami Chronicles*** (鬼滅の刃 ヒノカミ血風譚) | CyberConnect2; Aniplex/Sega; **15-oct-2021** (Switch, 9-jun-2022) ✅ wiki + Steam | modo historia hasta *Mugen Train*; al explorar se pulsa «**Examinar / Hablar**» y se **rastrea el olor** con el gatillo; en combate, el **hilo del hueco** (隙の糸) ✅ [manual oficial](https://game.kimetsu.com/hinokami/manual/play.html). Su web usa **Cinzel** y **Noto Serif JP** ✅ |
| ***The Hinokami Chronicles 2*** | CyberConnect2 **y Arc System Works**; **5-ago-2025** (Japón, 1-ago) ✅ wiki + Steam | historia del Distrito Rojo, los Herreros y los Pilares; **minijuego «Zenko's Shamisen Jams»** (visto, §7.3) |
| En Steam, en español | «**Guardianes de la Noche** -Kimetsu no Yaiba- Las Crónicas de Hinokami» (1 y 2) | textos en **español de España**; voces sólo en japonés e inglés ✅ API de Steam |
| Otros (colaboraciones y móvil) | *Nichirin Battle Slash*, colaboraciones con *Puzzle & Dragons*, *Shironeko Project*, *Kotodaman* ✅ (páginas en la wiki) | no los miré ⚠️ |

**Lo que no encontré**: la **caja de diálogo del modo historia** (las
capturas oficiales y las de Steam vienen **sin interfaz**) ⚠️. **Game UI
Database** no la busqué (reto de Cloudflare, según la guía de cuadros).
**The Cutting Room Floor**: da **403 (Cloudflare)** en la búsqueda y en
su API (dos intentos); no pude saber si tiene página de estos juegos ⚠️.

**Capturas oficiales** (1920×1080), de la web japonesa del juego: 22
escenas del modo historia (`/hinokami/assets/img/gamemode/st_img1-22.jpg`),
por ejemplo [st_img6](https://game.kimetsu.com/hinokami/assets/img/gamemode/st_img6.jpg)
(Kanao entre glicinias) y
[st_img11](https://game.kimetsu.com/hinokami/assets/img/gamemode/st_img11.jpg)
(sala de tatami de Tamayo).

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todos reconocen

| Qué | Dónde | Estado |
|---|---|---|
| Rengoku comiendo: «**¡Umai! ¡Umai!**» → en latino «**¡Sabroso!**» | MT 00:05:45; TM-1 00:01:15 | ✅ subtítulo + 2 vídeos de fans |
| «**Enciende tu corazón**» (心を燃やせ) | TM-7 00:14:40 | ✅ japonés; la frase latina ⚠️ |
| Tanjiro gritándole a Akaza «**¡No huyas, cobarde!**» (逃げるな卑怯者) | MT 01:40:24; TM-7 00:10:03 | ✅ |
| Giyu: «**A mí no me odia nadie**» | T1-21 00:12:43 | ✅ |
| Kotetsu: «**¿Qué pashó, papu?**» (sólo en latino) | AH-2 | ✅ Doblaje Wiki |
| Tanjiro: «**Soy el hermano mayor, puedo aguantarlo**» | T1-12 00:19:27 | ✅ |
| **El cabezazo** de Tanjiro: le parte la frente a quien sea (su cabeza dura la heredó de su madre) | T1-14 00:07:28; DR-10 00:23:20 | ✅ |
| Inosuke llamando mal a todos («**Gonpachirō**», «**Monitsu**») | T1-14, T1-25 | ✅ |
| Zenitsu **gritando** y **pidiendo matrimonio** a desconocidas | T1-10/11 | ✅ |
| Zenitsu **dormido**, que es cuando pelea bien | T1-12 00:09:51 | ✅ |
| **Chuntarō**, el gorrión que no habla | T1-11 | ✅ |
| **La calabaza** (hay hasta una **palomitera de calabaza** de Tanjiro en Universal Studios Japan, según un hilo de Reddit) | T1-25 | ✅ serie; la palomitera ⚠️ (una fuente: [Reddit](https://reddit.com/r/KimetsuNoYaiba/comments/1jz4xop/)) |
| **Los Secretos de la era Taisho** | casi cada episodio | ✅ |
| El trío protagonista como «**escuadrón Kamaboko**» | — | ⚠️ de memoria (no sale en los subtítulos japoneses) |

### 14.2 Qué NO hacer (lo que un fan notaría)

- **Dibujar a Shinobu gritando o seria sin motivo**: sonríe siempre; su
  enfado es una sonrisa más tensa.
- **Poner a Rengoku callado o con los ojos entornados**: siempre **ojos
  muy abiertos** y voz alta.
- **Quitarle a Nezuko el bambú** en una lámina normal.
- **Invertir el *haori* de Giyu**: la mitad lisa granate va a **su
  derecha** ⚠️ (compruébalo con la ficha, personajes n.º 30).
- **Poner a Zenitsu tranquilo tocando el shamisen**: en la escena toca
  **furioso**, con venas y colorete (clip, 0:23).
- **Mezclar la Mansión Mariposa con el Castillo Infinito**: una es de día
  y cálida; el otro es la batalla final, ámbar y oscuro.
- **Globos blancos de cómic** o letras de terror para los textos (§7.5).
- **Decir «Hashira» o «Castillo Infinito» en boca de los personajes**: en
  latino es «**Pilar**» y «**la fortaleza infinita**».
- **Los pendientes de Tanjiro**: son cartas *hanafuda* con **un sol rojo
  sobre una montaña** ✅ wiki. En algunos países de Asia se cambiaron por
  parecerse a la bandera del sol naciente ⚠️ (de memoria): en una lámina
  para Latinoamérica, **déjalos como en el anime**, sin exagerar los rayos.
- **Spoilers del final** (quién muere en el Castillo): mucha gente del
  servidor sólo ha visto el anime.

---

## 15 · Poses analizadas por personaje

(«P n.º» = `hojas/personajes_01.jpg`; «clip» = vídeo de §12, con su minuto.)

### Shinobu

| Fuente | Postura | Manos | Mirada / gesto | Sirve para |
|---|---|---|---|---|
| P n.º 1 (arte oficial) | de pie, tres cuartos, cadera ladeada | **espada al hombro**, la otra mano recogida | sonrisa cerrada, ojos entornados | **presentar** |
| P n.º 2 (clip Shinobu, 0:17) | de medio cuerpo, un poco inclinada | **índice arriba** a la altura de la cara | ojos entornados hacia abajo, sonrisa | **explicar** |
| P n.º 3 (clip, 0:24) | igual | **palma abierta** hacia arriba, ofreciendo | sonrisa más abierta | **explicar**, «así se hace» |
| P n.º 4 (T1-20) | de medio cuerpo, erguida | fuera de plano | **ojos cerrados**, sonrisa serena | presentar con cartela |
| P n.º 5 (2880×1618) | de medio cuerpo, girada | — | sonrisa dulce hacia Kanao | **animar** |
| clip, 0:43-0:48 | arrodillada en *seiza* junto a Mitsuri | manos en el regazo | ojos cerrados, sonriendo | **pensar**, calma |
| T1-25, 00:07:14 a 00:07:44 | (sin fotograma: subtítulo) | — | le dice a Inosuke «¿no puedes?» sonriendo | **regañar** con dulzura |

### Tanjiro

| Fuente | Postura | Manos | Mirada / gesto | Sirve para |
|---|---|---|---|---|
| P n.º 8 (T1-25) | piernas abiertas, cuerpo tenso | **las dos manos sujetan la calabaza** contra la boca | mejillas hinchadas, cejas fruncidas | **el esfuerzo**, el reto |
| P n.º 9 (T1-25, 0:00) | sentado, ropa de paciente | manos juntas en el pecho | **ojos cerrados**, sonrisa enorme | **celebrar** |
| P n.º 10 (clip Rengoku, 0:19-0:31) | de medio cuerpo | **mano junto a la boca**, cuchicheando | mirada de lado, cómplice | **contar un secreto** |
| P n.º 11 (clip, 1:47-1:51) | de medio cuerpo, ante el telón | **puño cerrado** delante del pecho | ceño decidido | **animar** |
| P n.º 12 (chibi) | de pie | **megáfono** en una mano | boca abierta, feliz | **anunciar** |
| fondos n.º 4 (2552×1436) | sentado en el tejado, de espaldas, **meditando** | en las rodillas | hacia la luna | **pensar**, respirar |

### Zenitsu

| Fuente | Postura | Manos | Mirada / gesto | Sirve para |
|---|---|---|---|---|
| P n.º 14 (DR-2, clip 0:02) | arrodillado en el tatami, **shamisen** en el regazo | púa arriba, rasgueando | concentrado, **rayos verdes** alrededor | **tocar**, música |
| P n.º 15 (clip, 0:23) | primer plano | mano en las cuerdas | **dientes apretados**, venas, colorete | la pasión |
| clip, 0:15-0:22 | **de espaldas**, kimono naranja, *obi* granate | el mástil sobresale | — | plano con profundidad |
| P n.º 16 (cumpleaños) | chibi sentado en un bento | **brazos abiertos** | ojos cerrados, risa | **celebrar** |
| P n.º 17 | de medio cuerpo, con la carta | la carta en las manos | ojos llorosos | leer un mensaje |
| tráiler, 0:47 | de medio cuerpo | — | **ojos en sombra**, serio | la versión seria |

### Rengoku

| Fuente | Postura | Manos | Mirada / gesto | Sirve para |
|---|---|---|---|---|
| P n.º 19 (arte del juego) | en guardia, llamas en espiral | espada a dos manos | fija, sonrisa | acción |
| P n.º 21 (cumpleaños) | sentado en un pastel | **brazos cruzados** | ojos muy abiertos, sonrisa | **presentar**, orgullo |
| clip Rengoku, 1:08 | sentado a la mesa | **cuenco y palillos** | boca abierta: «¡Sabroso!» | **celebrar** |
| MT (película) | sentado en el tren con bentos apilados | palillos | «¡Umai!» | el gag |
| [En el tren](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/b/bc/Tanjiro_and_Zenitsu_running_into_Kyojuro_on_the_Train.png) (1920×1080) | sentado de lado en el asiento, luz cálida de lámparas | **caja de bento** en la izquierda, **palillos** en la derecha, comiendo | ojos muy abiertos y **fijos al frente**, boca llena; Tanjiro y Zenitsu detrás, pasmados | **celebrar**, el chiste |
| [Dormido en el tren](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/f/f5/Tanjiro_and_Kyojuro_asleep_on_the_train.png) (2048×1150) | sentado, **cabeza gacha** | — | ojos cerrados; Tanjiro dormido contra él | **pensar**, calma |
| [Key visual 1 de *Mugen Train*](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/a/ac/Mugen_Train_Key_Visual_1.png) (1332×1880) | **de frente**, piernas abiertas, *haori* ondeando, llamas detrás | **espada clavada vertical** delante; **la otra mano extendida hacia la cámara** | mirada al espectador, serio | **presentar** a lo grande |
| [Evento de otoño 2025](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/c/c7/Kyojuro_Fruitful_Autumn_Festival_Event_2025.png) (chibi, 1810×2568) | caminando, gorro de oso | **un boniato** en una mano, una rama en la otra | **guiño**, boca abierta | **animar**, lo tierno |

### Mitsuri, Kanao, Aoi, Tengen

| Fuente | Quién | Qué hace | Sirve para |
|---|---|---|---|
| P n.º 22 (clip, 0:48) | Mitsuri | **manos en las mejillas**, colorada | emocionarse |
| clip Rengoku, 1:02 | Mitsuri | **brazos abiertos** | dar la bienvenida |
| P n.º 23 | Mitsuri | clase de **cintas**, pierna en alto | **dar clase** |
| P n.º 25 | Kanao | le tira té a Tanjiro, rapidísima | el ejercicio |
| P n.º 26 | Aoi | brazos en jarra, regaña | **regañar** |
| P n.º 24 | Tengen | brazos cruzados, sonrisa pícara | presentar |

### Resumen: qué pose para qué

| Para… | Pose | Imagen |
|---|---|---|
| **presentar** | Shinobu con la espada al hombro; Rengoku brazos cruzados | P n.º 1; P n.º 21 |
| **explicar** | Shinobu índice arriba → palma abierta | P n.º 2 y 3 |
| **celebrar** | Tanjiro ojos cerrados y sonrisa; Rengoku «¡Sabroso!» | P n.º 9; clip 1:08 |
| **regañar** | Aoi brazos en jarra; Shinobu «¿no puedes?» | P n.º 26 |
| **pensar** | Tanjiro meditando en el tejado | fondos n.º 4 |
| **animar** | Tanjiro con el puño; las tres niñas «¡Ánimo!» | P n.º 11 |
| **contar un dato** | Tanjiro cuchicheando | P n.º 10 |

---

## 16 · Vestuario

Colores medidos (§5.2) o de la ficha del wiki ✅; «a ojo» ⚠️.

| Personaje | Traje icónico | Colores | Accesorios y peinado |
|---|---|---|---|
| **Tanjiro** | uniforme negro del Cuerpo + ***haori* a cuadros verde y negro** («biscay-green» según el wiki) | verde `#2E957F`-`#47A47E`, negro `#011826` (medido, T1-03) | **pendientes *hanafuda*** (sol rojo sobre montaña), **cicatriz** en la frente que se vuelve **marca de llama**, caja de madera a la espalda ✅ wiki |
| Tanjiro, entrenamiento | **ropa de paciente** verde menta muy clara (T1-24/25) | ⚠️ a ojo `#DDEDE5` | pelo suelto |
| **Nezuko** | kimono **rosa con dibujo *asanoha*** (hojas de cáñamo), *haori* marrón oscuro, lazo rosa | rosa `#EC1C56` (arte del juego) ⚠️ | **bozal de bambú** verde, pelo negro largo con puntas naranjas |
| **Zenitsu** | uniforme marrón dorado + ***haori* amarillo a naranja con triángulos blancos** ✅ wiki | amarillo `#D6AE75`/`#FFE9C9` (cumpleaños) | *kyahan* degradados con tres lazos blancos ✅ wiki |
| Zenitsu, «**Zenko**» | kimono **naranja** con *obi* granate, maquillaje blanco, colorete | naranja `#D4994B`/`#E7A84F`, granate `#791F2F` (medidos) | dos moñitos en el pelo |
| **Inosuke** | torso desnudo, pantalón con **piel de jabalí** | ⚠️ | **cabeza de jabalí**, dos espadas melladas |
| **Rengoku** | uniforme marrón oscuro + ***haori* blanco que acaba en llamas rojas** (era de su padre) ✅ wiki | ⚠️ `#F88D22` (llama, arte del juego) | pelo **amarillo con puntas rojas**, cejas partidas, *kyahan* rojos con llamas ✅ wiki |
| **Shinobu** | uniforme **morado oscuro** + ***haori* de alas de mariposa**: blanco que pasa a **turquesa y rosa** con bordes negros ✅ wiki | morado `#534452`, blanco `#ECE6E1` (medido, T1-20) | **horquilla de mariposa** blanca, pelo negro que acaba en **morado**, *kyahan* de mariposa ✅ wiki |
| **Giyu** | *haori* **partido**: granate liso y el geométrico verde-amarillo-naranja de Sabito | ⚠️ | pelo negro recogido bajo |
| **Kanao** | uniforme con capa blanca, falda | ⚠️ | **horquilla de mariposa**, coleta de lado |
| **Mitsuri** | uniforme con escote (se lo hizo el sastre Maeda; ella no lo quemó) ✅ wiki, *haori* blanco | ⚠️ | **trenzas rosas y verdes**, **medias a rayas verdes** (regalo de Obanai) ✅ wiki |
| **Tengen** | uniforme sin mangas | ⚠️ | **banda de joyas** en la frente, maquillaje rojo en el ojo |
| **Urokodaki** | ropa azul con **nubes** blancas | azul `#488595`/`#326171` (medido) | **máscara de *tengu* roja** |

**Lo icónico que todos reconocen**: los **cuadros de Tanjiro**, el **bambú
de Nezuko**, los **triángulos de Zenitsu**, la **cabeza de jabalí**, las
**llamas de Rengoku** y las **alas de mariposa de Shinobu**. Hay un **kanji
滅** en la espalda de todos los uniformes ✅ wiki.

---

## 17 · Paisajes y fondos de pantalla

### 17.1 Los sitios, con su luz (vistos en `hojas/fondos_01.jpg`)

| N.º | Sitio | Hora y luz |
|---|---|---|
| 1 | Mansión Mariposa, exterior | mediodía, cielo claro `#BEE0E4`, sombras suaves |
| 2 | Dojo de la Mansión | interior, luz de ventana lateral, madera oscura |
| 3 | *Engawa* | tarde, luz cálida sobre tierra `#C8C08E` |
| 4 | Tejado de noche | **luna creciente**, azul casi negro `#101923` |
| 5 | Sala abierta al jardín (opening, 1:06) | contraluz verde |
| 6-8 | Monte Sagiri | nieve y niebla; bambú **dorado** |
| 9-10 | Glicinias de la Selección Final | noche, morados que **brillan** |
| 11-13 | Yoshiwara y la casa Kyōgoku | noche, **faroles naranjas** `#C68146` |
| 14 | Aldea de los Herreros | atardecer de otoño |
| 15 | Jardín de la Reunión de Pilares | día, arena clara |
| 16-17 | Bosques del entrenamiento | día, verdes |
| 18-19 | Castillo Infinito | **ámbar** y negro, faroles |
| 20-21 | Ending 1 | ukiyo-e morado y *higanbana* roja |

### 17.2 Fondos de pantalla en alta

| Imagen | Tamaño | Autor | Nota |
|---|---|---|---|
| [Castillo Infinito, key visual IMAX](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/4/48/Infinity_Castle_Trilogy_IMAX_Key_Visual.png) | 2898×4096 | Aniplex/ufotable | vertical: **móvil** |
| [Mugen Train Key Visual 2](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/c/c0/Mugen_Train_Key_Visual_2.jpeg) | 2898×4096 | Aniplex/ufotable | vertical |
| [Cumpleaños de Shinobu 2025](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/2/2f/Shinobu%27s_birthday_illustration_%282025%29.png) (y todos los de la serie) | 4096×2898 | oficial | apaisado: **escritorio** |
| [Año Nuevo 2025](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/5/57/New_Year%27s_illustration_%282025%29.png) | 4031×2845 | oficial | el grupo en el *kotatsu* |
| [Wallhaven vp2qv3](https://wallhaven.cc/w/vp2qv3) | 1920×1080 | subido por un usuario | el único que devolvió la API de Wallhaven con «kimetsu no yaiba» ⚠️ |

Fondos de pantalla **de fans** en alta: la API de Wallhaven no devolvió
nada más con «demon slayer», «tanjiro» o «rengoku» ⚠️. No busqué en
DeviantArt ni Pixiv.

---

## 18 · Guía para generar con IA: imagen (Firefly, Canva) y texto

Sirve para **fondos, objetos y pruebas de pose**. Al personaje final se le
recorta de arte oficial (y se integra con `v3/integrar.py`, regla 3 del
dueño): la IA **no** debe inventar a Shinobu ni a Zenitsu.

### 18.1 Lo que no cambia nunca

- **Línea**: contorno fino y uniforme, **a veces de color** (en los dibujos
  clave de ufotable las sombras se marcan con **lápiz rojo, azul y verde**:
  vídeo de los Oscars, [0:29-0:44](https://www.youtube.com/watch?v=FLB_sLTgbPk&t=29)).
- **Sombra**: *cel shading* de 1-2 tonos, con **brillo de borde** en la
  acción; los efectos de las respiraciones (agua, rayo, llama) van
  **dibujados a lo ukiyo-e** (olas con rizos, como Hokusai) sobre un 3D
  suave.
- **Fondos**: pintados, casi fotográficos, con **profundidad de campo** y
  luz de «composición» (ufotable llama a su departamento de fotografía el
  que «termina» la imagen).
- **Época**: **Taishō** (1912-1926): madera, papel, kimonos, faroles,
  algún tren y luz eléctrica en la ciudad. **Nada moderno**.

### 18.2 Palabras que ayudan (en inglés)

`Taisho era Japan, 1910s`, `traditional Japanese mansion with engawa
veranda`, `wooden floorboards, shoji paper screens, bamboo fence`,
`afternoon sunlight, soft dappled light`, `hyotan gourds tied with red
cord`, `wisteria`, `anime background painting, ufotable style, cinematic
depth of field`, `ukiyo-e wave pattern`, `paper lanterns at night`,
`red theater curtain`, `shamisen on tatami, pine tree folding screen`.

### 18.3 Palabras que lo estropean

`chibi` (salvo que se quiera chibi), `neon`, `cyberpunk`, `modern city`,
`samurai armor` (no son samuráis), `katana glowing` (sólo brillan en los
efectos), `speech bubble`, `manga panel`, `blood` (para el Aula), `demon`
(saca monstruos occidentales), `kimono` sin más (saca kimonos de boda;
mejor `plain cotton kimono`).

### 18.4 Qué imágenes darle como referencia

| Para… | Imagen |
|---|---|
| estilo de fondo de día | fondos n.º 1 ([Butterfly Mansion Anime](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/9/99/Butterfly_Mansion_Anime.png)) |
| interior de madera | fondos n.º 2 ([Rehabilitation Training](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/d/dd/Rehabilitation_Training.png)) |
| noche con faroles | fondos n.º 11 ([Yoshiwara](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/2/28/Yoshiwara%2C_Tokyo_Anime.png)) |
| el objeto | objetos n.º 1 ([la calabaza](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/c/ce/Tanjiro_blowing_up_the_gourd.png)) |
| pose que explica | personajes n.º 2-3 (Shinobu, clip) |

### 18.5 Encuadre

- Apaisado 1200×800 (3:2); **el personaje a un lado** (tercio izquierdo o
  derecho) y el objeto con los textos en el otro.
- **Algo delante**, desenfocado (una calabaza, el mástil, una mariposa).
- Cámara **a la altura del *engawa*** (sentado), como en T1-25: así se ve
  el jardín detrás.
- **Técnica del estudio** (segunda pasada, §19): personaje **plano**
  (*cel* de 2-3 tonos) sobre fondo u objeto con **luz realista**. Nunca al
  revés. Si la IA da un personaje con volumen de 3D, no sirve.

### 18.6 Para una IA de texto: cómo escribir en su voz

Segunda pasada. Todo sale de §7, §8, §10.4 y §14 de esta biblia. Las
frases son **reales**, con su minuto. La traducción del japonés es de la
biblia, salvo las marcadas «latino».

**Reglas que no cambian**

- **Frases cortas y rotundas**. Una idea por frase.
- **Nada de globos**: el texto va en cartela vertical, tablilla, papel o
  telegrama de cuervo (§7.4).
- **Exclamaciones dobles** para Zenitsu, Inosuke y Rengoku («¡¡…!!»);
  Shinobu y Giyu **nunca** gritan (Giyu, una vez en toda la serie).
- **Vocabulario del doblaje latino**: «Pilar», no «Hashira»; «la
  fortaleza infinita», no «Castillo Infinito» (§7.5).
- **Onomatopeyas**: las de Tanjiro al explicar («¡BUON! ¡BUON!»,
  T1-25, 00:06:54); el «Umu» de Rengoku para asentir; los «mm» de Nezuko
  tras el bambú; la risa bajita de Shinobu («うふふ»); el «¡Caw!» del
  cuervo.

**Cómo habla cada uno** (para darle a la IA como instrucción)

| Personaje | Muletillas y forma | Puntuación |
|---|---|---|
| **Shinobu** | empieza con «Ay, ay» (あらあら, T1-24, 00:05:12); cortesía extrema; remata con una puya dulce | puntos suspensivos y pregunta final: «lo normal es poder… ¿no puedes?» |
| **Tanjiro** | «usted» a los mayores; se anima a sí mismo en voz alta; explica fatal | exclamaciones sueltas, onomatopeyas |
| **Zenitsu** | quejas largas, histéricas; piropos a desconocidas; dormido, serio y breve | «¡¡…!!» y lloriqueo; dormido, punto final seco |
| **Inosuke** | grita, no respeta a nadie, dice mal los nombres | todo en exclamación; «¡Embestida de jabalí!» |
| **Rengoku** | muy alto; llama «joven Kamado», «el chico amarillo», «el chico cabeza de jabalí» (MT, 01:45:31) | frases de 3-5 palabras con «¡!» |
| **Giyu** | poco, seco | punto final; nada de exclamaciones |
| **Nezuko** | casi muda | «Mm.» o dos palabras dulces |
| **El cuervo** | telegrama en mayúsculas | «¡ORDEN! ¡ORDEN!» |

**Frases reales por emoción**

| Emoción | Frase | Quién · dónde |
|---|---|---|
| **Alegre** | «¡Sabroso!» (latino; «¡Umai!») | Rengoku · MT 00:05:45 ✅ |
| **Alegre** | «¡Quién lo habría dicho!» («¡Yomoya yomoya da!») | Rengoku · §8 ✅ |
| **Enfadado** | «¡Claro que puedo! ¡No me subestimes!» | Inosuke · T1-25, 00:07:49 ✅ |
| **Enfadado** | «¡No huyas, cobarde!» | Tanjiro · MT 01:40:24 ✅ |
| **Enfadado** | «¡No dejes tu vida en manos de otro!» | Giyu · T1-01, 00:14:52 ✅ |
| **Enfadado** | «¡Siéntense en seiza!» | Zenitsu, celoso · T1-24, 00:08:10 ✅ |
| **Explicando** | «Lo normal es poder… ¿no puedes?» | Shinobu · §8 ✅ |
| **Explicando** | «Los huesos hacen ¡BUON! ¡BUON!» | Tanjiro · T1-25, 00:06:54 ✅ |
| **Explicando** | «Todo lo vivo suena» | Zenitsu · T1-13, 00:17:54 ✅ |
| **Animando** | «¡Ánimo, Tanjiro, ánimo!» | Tanjiro a sí mismo · T1-12, 00:19:27 ✅ |
| **Animando** | «Hermano, tú puedes» | Nezuko, dormida · T1-25, 00:20:54 ✅ |
| **Animando** | «Cuento contigo» | Shinobu · T1-25, 00:19:32 ✅ |
| **Animando** | «¡Ánimo! ¡Ánimo! ¡Ánimo!» | Sumi, Kiyo y Naho · T1-25 ✅ |
| **Animando** | «Enciende tu corazón» | Rengoku · TM-7, 00:14:40 ✅ japonés; el latino ⚠️ (§10.4) |
| **Triste** | «Soy el hermano mayor, puedo aguantarlo» | Tanjiro · T1-12, 00:19:27 ✅ |
| **Triste** | «Vive con la frente en alto» | Rengoku · TM-7, 00:14:26 ✅ |
| **Cómico** | «A mí no me odia nadie» | Giyu · T1-21, 00:12:43 ✅ |
| **Cómico** | «¿Qué pashó, papu?» (sólo latino) | Kotetsu · AH-2 ✅ |

**Vocabulario de expresiones** (para que la IA de imagen entienda el
gesto; lo que se vio en clips y hojas)

| Gesto | Cómo se ve en la serie | Dónde |
|---|---|---|
| **Sonrisa de Tanjiro** | ojos **cerrados del todo** | personajes n.º 9 |
| **Mentira de Tanjiro** | la cara **se le deforma** | §8 ✅ wiki |
| **Explicar** | fondo **blanco con viñeta**, dedo índice arriba | clip Shinobu, 0:17 |
| **Vergüenza** | Inosuke **colorado**, fondo **amarillo con brillos** | clip Shinobu, 0:28 |
| **Enamorada** | Mitsuri con **manos en las mejillas** y **corazones** | clip Rengoku, 0:11-0:17 |
| **Cuchicheo** | mano en la boca, fondo amarillo | clip Rengoku, 0:19 |
| **Chibi** | Secretos Taisho, cumpleaños, eventos: cabeza grande, «V» con los dedos | objetos n.º 5; personajes n.º 12 y 16 |
| **Furia de Zenitsu** | venas y colorete, rayos verdes | clip de Zenko, 0:23 |
| **Rabia de Shinobu** | sonrisa más tensa; la vena ⚠️ de memoria | §8 |
| **Gotas de sudor** | ❌ no documentadas en las partes | — |

---

## 19 · Estilo de dibujo, técnica, Blender y encuadres

Segunda pasada (punto 18 de `ENCARGO.md`). Sale de `partes/texto.md`:
entrevistas técnicas en japonés e inglés y guías de Blender.

### 19.1 Con qué lo hace ufotable

- **3ds Max** es el programa 3D principal, con **V-Ray** (render),
  **PhoenixFD** (fuego y agua de las respiraciones), **tyFlow** (hilos de
  araña, viento, cuervos), **ForestPack** (vegetación), **RailClone**
  (estructuras repetidas del Castillo), **GrowFX**, **HairFarm** (pelo) y
  **Pencil+** (línea 2D sobre 3D) ✅ [Autodesk AREA JAPAN, parte
  1](https://area.autodesk.jp/case/animation/kimetsu-01/) y [parte
  2](https://area.autodesk.jp/case/animation/kimetsu-02/) (ja).
- También **Blender y Houdini** (con estudios externos), **EmberGen**
  (fluidos rápidos), **After Effects** (composición) y **DaVinci
  Resolve** (edición) ✅ [CGWORLD × NVIDIA](https://cgworld.jp/special-feature/202410-nvidia-hp-ufotable.html)
  (ja). Hablan **Yuichi Terao** (jefe de imagen digital y director de
  fotografía), **Takeshi Okuya** y **Reiji Amano** (artistas técnicos).
- **Cómo se reparten 2D y 3D**: maquetas 3D previas para que los
  dibujantes tengan la perspectiva; fondos de edificios y criaturas
  complejas, en 3D; **los personajes principales, dibujados a mano**. Un
  supervisor 3D está en las reuniones de dirección ✅ (Autodesk, parte 1).
- **La Respiración del Agua** se diseñó estudiando los grabados
  **ukiyo-e**, con muchas pruebas en 3ds Max ✅ (Autodesk, parte 1).
- **El Castillo Infinito**: ~**30 versiones** de la estructura por escena.
  En el ep. 26 sólo podían renderizar ~100×100 m; en los Herreros
  (ep. 45), 2 km²; en la película, **10 veces más rápido** ✅ (Autodesk +
  [Popverse, entrevista a Terao](https://www.thepopverse.com/movies-demon-slayer-kimetsu-no-yaiba-yuichi-terao-interview-making-the-infinity-castle-feel-infinite)).
- **Gotouge dibuja el manga a mano**: la exposición de originales habla de
  «直筆原画» ⚠️ ([Discover Japan](https://discoverjapan-web.com/article/74084),
  una fuente). Mandaba los bocetos (*name*) **por fax** desde el campo y
  los corregía **por teléfono** con su editor ✅ ([livedoor News,
  entrevista al editor Tatsuhiko Katayama](https://news.livedoor.com/article/detail/17760339/), ja).
- **Qué plumilla o tableta usa**: no lo encontré ⚠️.

### 19.2 Línea, sombra y filtros

- **Personaje**: *cel shading* plano. **Fondos y efectos**: 3D mucho más
  **realista**, a propósito, para que contraste ✅ [Sakuga Blog](https://blog.sakugabooru.com/2019/08/15/kimetsu-no-yaiba-the-power-of-ufotables-harmony/).
- **Línea que cambia de grosor con el movimiento**: la usa **Akira
  Matsushima**, diseño de personajes y dirección de animación ✅ (Sakuga
  Blog). En los dibujos clave, sombras marcadas con **lápiz de color**
  (§18.1).
- **Animadores que conviene estudiar**: **Masayuki Kunihiro** (poses
  «sobrehumanas», anticipación larga; anima a Inosuke), **Mitsuru
  Obunai** (dibujos muy espaciados, sensación de fuerza) y **Nozomu Abe**
  (efectos 2D, siluetas en el impacto) ✅ (Sakuga Blog).
- **Pinceladas de fondo**: acuarela digital, con grano en cielo y agua
  (fondos n.º 1 y 9). Pincel libre que se le acerca: la acuarela por
  defecto de Krita ⚠️ (propuesta del investigador, sin *making of*).
- **Filtros** (grano, aberración, *bloom*): **no encontré** fuente que los
  nombre ⚠️. Sólo reseñas que dicen «cinematográfico».

### 19.3 Encuadres: cómo se enmarca cada emoción

Del ensayo [The Visual Design of Demon Slayer's Combats](https://jbsiraudin.github.io/blog/demon-slayer-visual-grammar/)
(jb siraudin, en) ✅ y de Sakuga Blog:

- **La acción, al centro del cuadro**: el ojo no tiene que moverse.
- **La cámara tiembla a 24 fps** sobre animación a 12 fps, y **se mueve
  hacia donde va el golpe**.
- **La luz avisa antes del golpe**: brillo **azul** en las espadas,
  **morado** en los enemigos, **chispas doradas**.
- **Fotograma de impacto**: uno de alto contraste, a veces sólo silueta.
- **Ritmo**: preparación larga → ataque instantáneo → pausa larga. Como
  una respiración.
- **Ep. 19** (*storyboard* de **Toshiyuki Shirai**): el peligro se cuenta
  con la composición, sin perder claridad ✅ (Sakuga Blog).
- **Encuadre por emoción fuera del combate** (explicar, animar, triste):
  no hay entrevista del estudio que lo diga ⚠️. Lo visto en pantalla, con
  minuto, está en §15 (pose por uso) y §18.5 (encuadre de la lámina).

### 19.4 Cómo replicarlo en Blender

| Capa | Cómo | Fuente |
|---|---|---|
| **Contorno** | **Freestyle** (Render Properties → Freestyle), lo más simple; **Grease Pencil** si se quiere grosor variable como Matsushima | ✅ [StraySpark](https://www.strayspark.studio/blog/how-to-get-anime-toon-look-blender) + [Instructables](https://www.instructables.com/Custom-Toon-Shader-in-Blender/) |
| **Sombra de personaje** | nodo **Shader to RGB → Color Ramp** en *Constant*: **2 paradas = anime a dos tonos**; 3 paradas, medio tono (Eevee) | ✅ [Yarsa DevBlog](https://blog.yarsalabs.com/basic-toon-shader-in-blender/) + vídeos [«New Anime Cel/Toon Shader for Blender 4.2+»](https://www.youtube.com/watch?v=uCplB3zvQks) y [«ANIME in BLENDER!»](https://www.youtube.com/watch?v=WcVwszxkUuA) |
| **Fondo y objeto** | render **realista** (Cycles, luz de área o IES), como el V-Ray de ufotable | ✅ §19.1 |
| **Personaje** | en **capa aparte**, con el *toon* de arriba | ✅ §19.1 |
| **Luz** | área plana, sin sombras duras, para el personaje | ⚠️ receta de StraySpark, no del estudio |
| **Textura encima** | grano de papel (*Paper 005*, ambientCG, CC0, §5) en *Overlay* o *Soft Light*, baja opacidad | ⚠️ receta del investigador |
| **Orden de capas** | render de Blender → textura en *Overlay* → línea de Freestyle en *Multiply* | ⚠️ receta |

**Modelos con *rig*, libres** (CC Attribution 4.0, descargables; licencia
comprobada con la API de Sketchfab ✅; crédito obligatorio al autor):

| Personaje | Autor | Caras | Enlace |
|---|---|---|---|
| Tanjiro | Light.k | 33.764 | [Sketchfab](https://sketchfab.com/3d-models/none-0ab5b317b7654fd29255d22182537ded) |
| Rengoku | Light.k | 59.528 | [Sketchfab](https://sketchfab.com/3d-models/none-91a0c5978dd74ca5a0d4747c89270f99) |
| Akaza | Light.k | 45.629 | [Sketchfab](https://sketchfab.com/3d-models/none-327741c265db45c1b92ca9f1aeb57e99) |
| Nezuko (con *shapekeys* de expresión) | AikoX | 122.561 | [Sketchfab](https://sketchfab.com/3d-models/none-c57b6393ddee4c86b28a26c26d7a7a8f) |
| Tanjiro, Danza del Dios del Fuego | K- | — | [Sketchfab](https://sketchfab.com/3d-models/none-dfebaddf7ec442cc8cf81f561fcb465b) |
| Tanjiro, uniforme de la Selección Final (con `.blend`) | K- | — | [Sketchfab](https://sketchfab.com/3d-models/none-50ba553d376e45e596eace02e9779c38) |
| Teoni | Light.k | — | [Sketchfab](https://sketchfab.com/3d-models/none-302c19719a83454b8a18eb4ef30b9678) |

Light.k tiene también **Inosuke, Giyu y Rui** (mismo autor, mismo
buscador) ⚠️ sin enlace propio en las partes. **No hay Shinobu con *rig***
entre los encontrados: para ella, recorte de arte oficial (§18).

### 19.5 Cómo replicarlo en Photoshop (o Clip Studio)

- **Línea**: pincel de tinta con **presión** y **estabilizador** activado.
  Libres: [Manga Brush Line for Photoshop (Pearlpencil,
  DeviantArt)](https://www.deviantart.com/pearlpencil/art/Manga-Brush-Line-for-Photoshop-268440777)
  ✅ y [Manga Ink, 496 pinceles (Brusheezy)](https://www.brusheezy.com/free/manga-ink)
  (licencia distinta en cada pincel ⚠️).
- **Clip Studio**: [Manga Line Brush](https://assets.clip-studio.com/en-us/detail?id=1707223)
  y [15 pinceles de artwithrod](https://www.deviantart.com/artwithrod/art/15-Free-Clip-Studio-Paint-Brushes-for-Manga-Style-1019425750) ✅.
- **Sombra**: una capa de sombra **plana** en *Multiply* por encima del
  color, sin degradado ⚠️ ([Creative Bloq](https://www.creativebloq.com/animation/create-manga-style-artworks-2118703),
  tutorial general, no de Demon Slayer).
- **Tramas y grano de papel**: §20.

### 19.6 Lo que nunca cambia (resumen para la lámina)

- Personaje = **línea limpia + 2-3 tonos planos**.
- Fondo y efectos = **3D con luz realista** (agua, fuego, humo).
- Nunca al revés.
- Golpes: **temblor**, encuadre **centrado**, **luz de color** antes del
  impacto.

---

## 20 · Texturas 2D

Segunda pasada (punto 19). Sale de `partes/imagen.md`. Con §4 (3D) y §5.3
(texturas reales), no falta ninguna capa.

### 20.1 Los patrones de la ropa, con su nombre japonés

Cada patrón, en el wikitexto de su ficha de [Kimetsu no Yaiba
Wiki](https://kimetsu-no-yaiba.fandom.com/wiki/Zenitsu_Agatsuma) y, los
de Tanjiro y Nezuko, también en [Fun! Japan](https://www.fun-japan.jp/en/articles/14279) ✅.
Contraste: [Tokyo Weekender](https://www.tokyoweekender.com/art_and_culture/history/wagara-japanese-patterns-and-what-they-mean/).

| Personaje | Patrón | Qué significa | Hex (§16) | Versión libre |
|---|---|---|---|---|
| **Tanjiro** | ***ichimatsu*** (市松模様): cuadros verde y negro | nombre de un actor de kabuki del s. XVIII; prosperidad, un lazo que no se corta ✅ | `#2E957F` / `#011826` | vectores de Vecteezy, gratis con atribución, **no CC0** ⚠️. Se dibuja fácil a mano |
| **Nezuko** | ***asanoha*** (麻の葉): hoja de cáñamo, hexágonos con rayos | ropa de bebé: el cáñamo crece rápido y protege del mal ✅ | `#EC1C56` ⚠️ | [Asanoha Kumiko Pattern.svg](https://upload.wikimedia.org/wikipedia/commons/e/e1/Asanoha_Kumiko_Pattern.svg), 512×494, **CC BY-SA 4.0** (crédito al autor de la página) |
| **Zenitsu** | triángulos blancos (tipo ***uroko***, escama) sobre degradado amarillo-naranja, en *haori* y polainas | ✅ wiki | `#D6AE75` / `#FFE9C9` | [Uroko.svg](https://upload.wikimedia.org/wikipedia/commons/d/d8/Uroko.svg), 800×831, **dominio público** |
| **Giyu** | mitad **rombos** verde, verde oscuro, naranja y amarillo (era de Sabito) + mitad **granate liso** (era de su hermana Tsutako) | ✅ wiki | no medido ⚠️ | no encontré un patrón libre igual ⚠️ |
| **Rengoku** | degradado blanco a amarillo con **llamas rojas** en el borde (heredado de su padre) | ✅ wiki | `#F88D22` | no es trama: es pintura |
| **Shinobu** | polainas con **alas de mariposa**, turquesa a rosa con borde negro | ✅ wiki | `#534452` / `#ECE6E1` | no encontré versión CC0 ⚠️ |
| **Mitsuri** | *haori* **blanco liso** (regalo de Rengoku) | ✅ wiki | ⚠️ | no hace falta |

### 20.2 Emblemas

| Emblema | Qué es | Imagen | Estado |
|---|---|---|---|
| **Insignia del Cuerpo** (鬼殺隊) | una rama de **glicinia** (藤) enroscada en el kanji «fuji». Una familia la hizo su escudo para dar las gracias al Cuerpo; desde entonces marca las **casas-refugio** que no cobran | [Demon_Slayer_Corps_Insignia.png](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/2/25/Demon_Slayer_Corps_Insignia.png), 559×553 medido | ✅ wiki «Wisteria» + [The Mary Sue](https://www.themarysue.com/demon-slayer-symbol-meaning-explained/) |
| **Marca del Cazador** (痣) | mancha que despierta en combate; casi siempre única, pero la de Tanjiro, Yoriichi y Kokushibo son **llamas** | wiki «Demon Slayer Mark» | ✅ |
| **Tsuba** de cada uno | guarda de la espada con su dibujo propio | Tanjiro 2578×1443, Zenitsu 1920×1080, Shinobu 1920×1080 (§3, `referencias.json`) | ✅ |
| **El kanji 滅** y **惡鬼滅殺** | espalda del uniforme; hoja de la espada de los Pilares | §7.1 | ✅ |

### 20.3 Tramas, papel y pinceladas

- **Tramas oficiales del manga**: no se pueden bajar. Shueisha no las
  libera ⚠️ (busqué en inglés y japonés, «鬼滅の刃 トーン素材»).
- **Tramas libres para imitarlas** (gratis, **no CC0**: leer la licencia):
  - [Manga Screentone Pack 1](https://assets.clip-studio.com/en-us/detail?id=2142037),
    de Clip Studio Assets.
  - [Comic Manga Screentone Brushes](https://www.graphicsbunker.com/brushes/free-comic-manga-screentone-brushes/),
    de GraphicsBunker (Photoshop y Clip Studio).
- **Grano de papel**: *Paper 005* de ambientCG (CC0, §5.3). Sirve para el
  papel del manga, las cartelas y el *shōji*.
- **Pinceladas de fondo**: ufotable pinta en acuarela digital con grano
  (fondos n.º 1 y 9). No hay pincel CC0 igual; la acuarela de Krita es lo
  más cercano ⚠️ (§19.2).

### 20.4 Para qué sirve en la lámina

- La **glicinia del Cuerpo**: sello **tallado** en un objeto de madera
  (una caja, un cartel).
- El ***asanoha***: para forrar o grabar un objeto de Nezuko sin medir a
  ojo.
- El ***uroko***: el más fácil de hacer en Blender como relieve repetido
  en la tela de Zenitsu (concepto C).

---

## 21 · Gustos y detalles de cada personaje

Segunda pasada (punto 20). Sale de `partes/voz.md`. Fuente: el **databook
oficial** (*Kimetsu no Yaiba Official Fanbook: Kisatsutai Kenbunroku*,
Shueisha, jul-2019, 216 pág., y el *Fanbook 2*), citado con nota en la
sección **Trivia** de cada ficha de [Kimetsu no Yaiba
Wiki](https://kimetsu-no-yaiba.fandom.com/wiki/Tanjiro_Kamado#Trivia).
Cumpleaños y altura, cruzados con **AniList** ✅. Portada del libro:
[Official Fanbook](https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/7/75/Kimetsu_no_Yaiba_Official_Fanbook.png) (1561×2465).

### 21.1 La ficha de cada uno

| | Cumpleaños · altura · peso | Comida favorita | Afición | Cómo se ve (o lo ven) | Estado |
|---|---|---|---|---|---|
| **Tanjiro** | 14 jul · 165 cm · 61 kg | **brotes de angélica** (*tara no me*): se le abren las fosas nasales aunque disimule | **limpiar** y **dar cabezazos** | no habla de sí; en el Entrenamiento de los Pilares lo apodan «**Mamá**»: cocina bien y cuida a todos | ✅ |
| **Nezuko** | 28 dic · 153 cm · 45 kg | ***konpeitō*** (caramelitos de azúcar) | **coser**: le arregla a Giyu el *haori* tras la batalla final | siempre le gana a Tanjiro a **piedra, papel o tijera**; su peinado es el único que él sabe hacerle bien | ✅ |
| **Zenitsu** | 3 sep · 164,5 cm · 58 kg | bolas de arroz de **salmón** (Secreto Taisho, ep. 18) | cartas ***hanafuda*** y ***sugoroku*** | se cree **inútil y cobarde**, pero escribió unas memorias de **79 tomos**, *La leyenda de Zenitsu*, donde es el héroe (y pinta feo a Giyu por celos) | ✅ databook |
| **Inosuke** | 22 abr · 164 cm · 63 kg | **no la encontré** ⚠️ | el juego *Kotoro-Kotoro*, que le enseñó Tanjiro | se cree **el más fuerte**; acierta el nombre de Tanjiro **una de cada siete veces** | ✅ |
| **Rengoku** | 10 may · 177 cm · 72 kg | **sopa de miso con boniato**; en caja, dorada a la parrilla con arroz de boniato | ver **Noh, kabuki y sumo** | se mide por su **deber de Pilar**: «el que nace fuerte tiene que proteger al débil» (§8) | ✅ |
| **Shinobu** | 24 feb · 151 cm · 37 kg | ***tsukudani* de jengibre** | **contar historias de fantasmas** | sabe que **no tiene fuerza** para cortar cuellos: se ve estratega, no guerrera; lo suple con veneno | ✅ |

### 21.2 Lo que aman y lo que odian

- **Tanjiro**: odia la grosería y la cobardía (§8); ama a su familia.
- **Nezuko**: ama a Tanjiro por encima de todo.
- **Zenitsu**: **evita a las chicas** desde que, con su oído, oyó lo que
  decían de él a sus espaldas ⚠️ (sólo el databook); ama a Nezuko a
  primera vista.
- **Inosuke**: odia perder; su único pasatiempo declarado es **pelear**.
- **Rengoku**: **nunca tuvo mascota**: su padre odiaba a los animales ⚠️
  (sólo el databook). Ama enseñar.
- **Shinobu**: según Giyu, **no soporta los animales peludos**, pero tiene
  un **pez de colores llamado Fugu** (como el pez globo venenoso) ⚠️
  (sólo el databook).

### 21.3 El objeto que siempre lleva

| Personaje | Objeto |
|---|---|
| Tanjiro | la **caja de madera** con Nezuko y los **pendientes *hanafuda*** |
| Nezuko | el **bozal de bambú** y el adorno del pelo |
| Zenitsu | sus **cartas *hanafuda*** y el shamisen (de Zenko) |
| Inosuke | la **cabeza de jabalí** |
| Rengoku | la **espada de la Llama**, con 惡鬼滅殺 grabado (§7.1) |
| Shinobu | la **espada aguijón** con veneno de glicinia |

### 21.4 En la Academia Kimetsu (el instituto de broma de los tomos)

Páginas extra oficiales de los tomos 2, 3 y 7 ✅ (Trivia de la wiki):

- **Tanjiro** incumple siempre el uniforme por sus pendientes.
- **Zenitsu** revisa uniformes, con miedo a los matones.
- **Shinobu** preside el club de **Farmacología** y el de **Esgrima**
  (ganó el campeonato).
- **Rengoku** es **profesor de historia** y organiza batallas de
  caballitos en clase.
- **Nezuko** muerde **baguettes** y se las deja en la boca, como el bambú.
- **Inosuke** sale en la tele por haberse criado entre jabalíes.

### 21.5 Para la lámina

- Un **dato curioso** corto en el Secreto Taisho (concepto B): «A Shinobu
  le encantan las historias de fantasmas», «Nezuko siempre gana a piedra,
  papel o tijera».
- **No usar** los gustos de blogs (mangashed, lifehaki): se contradicen
  con el databook (p. ej. «taiyaki» para Tanjiro) ⚠️.
- **Gustos de Giyu, Tengen, Mitsuri, Kanao y Muichiro**: no los revisé ⚠️.

---

## 22 · Por qué la gente la ama, y las escenas que hacen llorar o gritar

Segunda pasada (punto 21). Sale de `partes/voz.md`, con fuentes en
español, inglés, japonés y coreano. Las encuestas y el cariño del
público latino ya están en §9.

### 22.1 Los números

| Dato | Cifra | Fuente |
|---|---|---|
| Manga en el mundo (jul-2025, con digital) | **220 millones** (164 M en Japón); 4.º de Shueisha tras One Piece, Dragon Ball y Naruto | ✅ [Somos Kudasai](https://somoskudasai.com/noticias/demon-slayer-220-millones-copias-manga/) + [Inquirer](https://technology.inquirer.net/142563/demon-slayer-manga-tops-200-million-copies-sold-worldwide) |
| Manga al terminar (mayo-2020) | 120 millones | ⚠️ [nippon.com (ja)](https://www.nippon.com/ja/in-depth/d00667/) |
| *Mugen Train* en Japón (2020) | **32.400 millones de yenes**: le quitó el récord a *El viaje de Chihiro* | ⚠️ nippon.com |
| *Castillo Infinito* en Corea del Sur | **3 millones** de espectadores en **10 días**; 58 % hombres | ⚠️ [Daum / IZE (ko)](https://v.daum.net/v/20250901095116506) |
| Crunchyroll Anime Awards 2020 | **Anime del Año** (y 3 premios esa noche) | ✅ [Animation World Network](https://www.awn.com/news/demon-slayer-kimetsu-no-yaiba-and-mob-psycho-100-ii-take-top-crunchyroll-anime-award-honors) + Wikipedia |
| Newtype Anime Awards 2019 | Mejor Director (Haruo Sotozaki) | ⚠️ sólo un agregador (IMDb) |
| Crunchyroll Anime Awards 2026 | **7 premios** para *Castillo Infinito*: Película del Año, Mejor Banda Sonora (Yuki Kajiura y Go Shiina) y **Mejor Actuación de Voz en Español Latinoamericano: José Antonio Toledano, Akaza** | ✅ [El Financiero](https://www.elfinanciero.com.mx/entretenimiento/2026/05/22/crunchyroll-anime-awards-2026-lista-completa-de-ganadores/) + [TV Azteca](https://www.tvazteca.com/azteca7/planeta-anime/crunchyroll-anime-awards-2026-que-premio-gano-demon-slayer-kimetsu-no-yaiba/) |
| Crítica, temporada 1 | **100 %** crítica, **89 %** público | ✅ [Rotten Tomatoes](https://www.rottentomatoes.com/tv/demon_slayer_kimetsu_no_yaiba/s01) |
| Reseñas | IGN: «*stunning swordfights… a lot of heart, and even a fair amount of humor*»; The Verge: la animación y las voces mejoran **cada episodio**, no sólo los grandes | ⚠️ citas vistas en resultados de búsqueda |

### 22.2 Por qué conecta

- **Japón** ⚠️ ([nippon.com](https://www.nippon.com/ja/in-depth/d00667/)):
  llegó en plena **pandemia**, cuando la gente se preguntaba qué importa
  de verdad. Los muertos **siguen acompañando** a los vivos: «**los
  pensamientos se heredan**». Llegó a gente que no ve anime.
- **Corea del Sur** ⚠️ ([Daum / IZE](https://v.daum.net/v/20250901095116506)):
  triunfó pese a su identidad japonesa, algo delicado allí. Por los
  **fondos realistas**, el movimiento en 3D, el sonido, el pasado triste
  **también de los villanos** y el humor que corta la tensión.
- **Latinoamérica**: la muerte de Rengoku y el récord de taquilla de
  *Castillo Infinito* en México (§9.3 y §10.1) ✅.

### 22.3 Con quién se identifica el público

De [AnmoSugoi](https://anmosugoi.com/demon-slayer-10-personas-populares/) ⚠️ (una fuente, pero da un motivo por personaje):

| Personaje | Por qué |
|---|---|
| **Zenitsu** | vence el miedo **justo cuando importa** |
| **Inosuke** | de salvaje a buscar **amistad** |
| **Mitsuri** | la rechazaban por no encajar; su fuerza rompe lo que «se espera» de una chica |
| **Nezuko** | demonio que sigue siendo humana por dentro |
| **Tanjiro** | empatía; la fuerza de verdad incluye **perdonar** |
| **Giyu** | protege sin esperar órdenes |
| **Rengoku** | nobleza y sacrificio |
| **Muichiro** | la historia con su gemelo |

En Danbooru, los cinco más dibujados son **Giyu, Shinobu, Nezuko, Mitsuri
y Tanjiro** (`datos-voz.md`): cariño medido, no encuestado.

### 22.4 Las escenas que hacen llorar

**Ep. 19, «Hinokami»** (T1-19, Monte Natagumo):

- **Qué pasa**: Tanjiro contra Rui. Recuerda la **danza del fuego de su
  padre** y Nezuko usa por primera vez su **sangre que arde** para
  salvarlo.
- **Qué suena**: «**Kamado Tanjirō no Uta**», de Go Shiina con Nami
  Nakagawa (§11.1), no el ending de siempre ✅ (Wikipedia en español).
- **Por qué duele**: la autora lloró. «La animación, la dirección, la
  música… todo es tan increíble que yo misma terminé llorando
  desconsoladamente», dijo **Koyoharu Gotoge**; lo vio **unas 20 veces**
  ⚠️ ([SensaCine México](https://www.sensacine.com.mx/noticias/noticia-1000160582/), una fuente, cita textual).
- **Cómo está dibujada**: el *storyboard* es de Toshiyuki Shirai (§19.3).

**La muerte de Rengoku** (*Mugen Train*), la que más hace llorar en
Latinoamérica (§9.3):

- **Minuto**: de «¡No huyas, cobarde!» (**MT 01:40:24**) a «Enciende tu
  corazón» (**MT 01:44:51**) ✅ (§14.1 y §10.4).
- **Qué suena**: «**Homura**», de LiSA, cierra su historia (§11.3).
- **Ranking** de las 10 escenas más emotivas de la película ⚠️
  ([Cultture](https://www.cultture.com/demon-slayer-mugen-train-las-10-escenas-mas-emotivas-de-la-pelicula-clasificadas)):
  1.ª la muerte de Rengoku; 2.ª Tanjiro persigue a Akaza al amanecer;
  3.ª el Hinokami Kagura contra Enmu; 4.ª Tanjiro rompe la pesadilla,
  furioso por los insultos a su familia; y en 10.ª, su madre le dice a
  Rengoku que está orgullosa de él.

**Lo que dice el fandom**: en r/KimetsuNoYaiba, «¿en qué pelea
lloraste?» (126 votos, 72 comentarios) da **Tengen contra Gyutaro,
Tanjiro contra Rui, Shinobu contra Doma y Tanjiro y Giyu contra Akaza**
⚠️ ([hilo](https://www.reddit.com/r/KimetsuNoYaiba/comments/1rmp5y1/which_fight_did_you_cry_at_tengen_vs_gyutaro/)).

**Reacciones** a la muerte de Rengoku (medidas con `yt-dlp`):

| Vídeo | Canal | Vistas | Idioma |
|---|---|---|---|
| [36 reacciones en mosaico](https://www.youtube.com/watch?v=FeqILNQVpps) | REACTION MASHUPS | 1.274.635 | inglés |
| [«se EXTINGUIÓ la LLAMA! :(»](https://www.youtube.com/watch?v=AevGumyhtes) | Merce Gallardo | 403.731 | español |
| [«[GIRLS REACT] Rengoku's Death»](https://www.youtube.com/watch?v=pmI917UuFYE) | Otaku-sen 2.0 | 351.487 | inglés |

### 22.5 La que hace gritar de emoción

La publicación más votada de r/KimetsuNoYaiba en «la mejor escena» (3.169
votos, 120 comentarios, `datos-voz.md`): [«No words. No action. Just the
serious expression from a once coward
kid»](https://www.reddit.com/r/KimetsuNoYaiba/comments/1f2oh56/). Es
**Zenitsu**, por primera vez **serio**, sin gritar. Para el fandom, da
más escalofríos que cualquier golpe. Otro punto a favor de Zenitsu para
el concepto C.

### 22.6 Las que hacen reír

De [ScreenRant](https://screenrant.com/funniest-demon-slayer-moments-hilarious/) ⚠️:

- Inosuke **mella sus espadas nuevas a pedradas** delante del herrero.
- Giyu **ata a Inosuke a un árbol** tras rechazar su reto.
- Las tres esposas de Tengen le estropean su despedida «final», y
  Nezuko **lo prende fuego** al intentar curarlo.
- Zenitsu se entera de que Tengen tiene **tres esposas** y acaba noqueado.
- Tanjiro reta a Giyu a un **concurso de comer** para animarlo.

---

## 23 · Fan dubs y comunidad hispana

Segunda pasada (punto 22). Sale de `partes/voz.md`. Todo es **de
aficionados**; el doblaje oficial está en §10. Vistas y «me gusta»
medidos con `yt-dlp` ✅.

### 23.1 Fandubs en YouTube

| Vídeo | Canal | Vistas | Me gusta | Fecha |
|---|---|---|---|---|
| [«Día de Besos»](https://www.youtube.com/watch?v=6pL9T_-uZrw) (cómic dub) | Humbertory | 1.671.983 | 65.318 | 19-abr-2020 |
| [«Tanjiro va al cielo»](https://www.youtube.com/watch?v=zG4NuOy5iBw) (cómic dub) | Humbertory | 1.458.739 | 72.432 | 23-abr-2020 |
| [«La muerte de Genya»](https://www.youtube.com/watch?v=eTAhMWJDNww) | RodriFD | 1.093.956 | 36.440 | 4-jun-2022 |
| [«¡GONPACHIRO KAMABOKO!»](https://www.youtube.com/watch?v=LrfgPRt7IpE) | Qchao24 | 3.970 | 82 | 2-ago-2021 |

**Un fandub en grupo**: [«Kamaboko Gonpachiro», de
TanoshiDubs](https://www.facebook.com/TanoshiDubs-585825835438840/videos/demon-slayer-kamaboko-gonpachiro-fandub-latinocr%C3%A9ditostanjiro-kiyoshi-el%C3%ADas-vega/352977596067075/)
(Facebook), con reparto acreditado: **Elías Vega** (Tanjiro y Kiyoshi),
**Fermín Abraham** (Zenitsu), **Alexito Sas** (Inosuke y el cuervo) ✅
(créditos en la descripción). Vistas: Facebook no las da sin sesión ⚠️.

**En TikTok**: [@soysamsedano](https://www.tiktok.com/@soysamsedano/video/7406568369912106246)
dobla a Kanao y la escena de Shinobu con Kanao; [@haijime_0](https://www.tiktok.com/@haijime_0/video/7390162930618141957),
la misma escena. Etiquetas: **#fandublatino #fandubespañol
#kimetsunoyaiba**. Vistas: TikTok da 403 sin sesión ⚠️.

### 23.2 Covers de openings y endings en español

| Canción | Cover | Canal | Vistas |
|---|---|---|---|
| Gurenge (OP1) | [«GURENGE COVER ESPAÑOL»](https://www.youtube.com/watch?v=yVuJzF14amo) | ilonqueen | **7.606.133** |
| Akeboshi (OP2) | [«FULL COVER ESPAÑOL LATINO»](https://www.youtube.com/watch?v=54c-_tTNqxo) | Danie Green | 1.216.278 |
| Gurenge (OP1) | [«FULL COVER ESPAÑOL LATINO»](https://www.youtube.com/watch?v=V3-Nkt0-3yw) | Danie Green | 1.020.076 |
| Zankyou Sanka (OP3) | [«COVER ESPAÑOL»](https://www.youtube.com/watch?v=i02a5eO6wFw) | Luxe KO | 720.740 |
| Homura (*Mugen Train*) | [«FULL COVER ESPAÑOL LATINO»](https://www.youtube.com/watch?v=A9eCWmSinG4) | Danie Green | 358.940 |
| Asa ga Kuru (OP4) | [«COVER ESPAÑOL»](https://www.youtube.com/watch?v=UVdL7iKihek) | Danie Green | 221.496 |
| From the Edge (ED1) | [«Cover ESPAÑOL»](https://www.youtube.com/watch?v=YubFGjSW2yw) | Yara Paz | 6.106 |

**Danie Green** es el canal que más openings canta en español latino:
cuatro, todos con más de 200 mil vistas ✅.

### 23.3 Parodias y memes hispanos

| Qué | Canal | Dato |
|---|---|---|
| [«KIMETSU DEL BARRIO — PARODIA RESUMIDA»](https://www.youtube.com/watch?v=Wyh8aMGocLc) (T1) | Eddie FD | **5.550.642** vistas, 170.969 me gusta |
| [«KIMETSU DEL BARRIO 2 — EL MUGRE TREN»](https://www.youtube.com/watch?v=XmSduNPYwWI) | Eddie FD | 1.637.922 vistas |
| [«Si tuviera BUENOS DIÁLOGOS»](https://www.youtube.com/watch?v=YG3e6vpb5XY) (serie de 9+ redoblajes de broma) | AquamerYT | de 213.691 a 1.083.542 por vídeo |
| [«If the Pillars Went to School»](https://www.youtube.com/watch?v=k_66ggFKqzY) | Viruz 51 | 2.683.142 vistas |
| El meme **«Kamaboko Gonpachiro»** | YouTube, Facebook y TikTok (@yowaimo_san, @jsscmrcl_) | se repite en varias redes ⚠️ |

**«Kimetsu del Barrio»** es la comedia hispana más vista que se encontró:
más que casi cualquier clip oficial doblado de §10.4.

### 23.4 Para el servidor

- **Reto de doblaje**: la escena de Shinobu y Kanao ya la doblan fans en
  TikTok; el «Kamaboko Gonpachiro» es el gag que todos conocen.
- **Canto**: Danie Green es la referencia de covers en español.
- **Encuesta**: «¿En qué pelea lloraste?» (§22.4).

---

## 24 · Colaboraciones, figuras y cosplay

Segunda pasada (punto 23). Sale de `partes/imagen.md`. Las tres
colaboraciones de móvil de §13 (*Nichirin Battle Slash*, *Shironeko
Project*, *Kotodaman*) siguen **sin mirar** ⚠️.

### 24.1 Marcas, parques y eventos

| Colaboración | Qué trae | Fecha | Fuentes |
|---|---|---|---|
| **Universal Studios Japan**: atracción XR del arco de los Herreros y el restaurante **Hyottoko Dining Hall** | arte nuevo de los Herreros, comida de cada Pilar, figuras a tamaño real | jul-2024 a ene-2025; anunciada otra para el Entrenamiento de los Pilares | ✅ [SoraNews24](https://soranews24.com/2024/07/24/demon-slayer-kimetsu-no-yaiba-gets-new-roller-coaster-attractions-and-food-at-universal-studios-japan/) + [Japan Web Magazine](https://jw-webmagazine.com/demon-slayer-theme-restaurant-at-universal-studios-japan/) |
| **Lawson × USJ** | dos tiendas decoradas, productos exclusivos | desde 30-jun-2026 | ✅ [Lawson (ja)](https://www.lawson.co.jp/lab/entertainment/art/20260630_collabousj.html); [foto oficial](https://www.lawson.co.jp/lab/entertainment/art/__icsFiles/afieldfile/2026/06/29/20260630_collabo_usj_g_2.jpg), 800×450 |
| **UNIQLO UT** | **2021**: con GU, 22-jul. **2025**: 4 camisetas (Tanjiro y Nezuko; Zenitsu con rayo; Akaza; glicinias y Pilares de espaldas), 1.500 ¥ | 2021 y 2025 | ✅ [Uniqlo 2021 (ja)](https://www.uniqlo.com/jp/ja/contents/corp/press-release/2021/07/210706_21ss_kimetsu_ut.html) + [kimetsu.com, noticia 2025](https://kimetsu.com/anime/news/?id=67677) + [Aniplex](https://www.aniplex.co.jp/news/detail/?id=67677); [camiseta](https://image.uniqlo.com/UQ/ST3/AsianCommon/imagesgoods/481120/item/goods_00_481120_3x4.jpg), 1500×2000 |
| **Puzzle & Dragons** (GungHo) | arte nuevo: Akaza, «Giyu y Tanjiro», Doma; mazmorra «Descenso de Muzan» | 22-ago a 8-sep-2025 | ✅ [kimetsu.com](https://kimetsu.com/anime/news/?id=68473) + [pad.gungho.jp](https://pad.gungho.jp/member/collabo/kimetsu/2312/); [arte](https://pad.gungho.jp/member/collabo/kimetsu/2312/img/ogp.jpg?=231221), 1280×720 |
| **ufotable Cafe** (el café del propio estudio) | menú y mercancía con **arte nuevo** de escenas concretas, casi todo el año. En 2026, cuatro tandas «Lazos que unen» (p. ej. la 3.ª, 9-jun a 5-jul: el trío y la Academia Kimetsu) y una de Iguro y Kanroji (4-mar) | 2026 | ✅ [ufotable Cafe](https://www.ufotable.co.jp/cafe/collaboration/kimetu/) + [Japan Web Magazine](https://jw-webmagazine.com/tips/demon-slayer-kimetsu-no-yaiba-cafe-in-japan/); fechas también en [collabo-cafe.com](https://collabo-cafe.com/events/tag/ufotable-cafe/) |

**Fortnite: no hay colaboración oficial** (sep-2026). Sólo el rumor de un
filtrador (ShiinaBR); Epic no lo ha anunciado ([GameRant](https://gamerant.com/fortnite-leak-demon-slayer-collab-release/),
[ExitLag](https://www.exitlag.com/blog/demon-slayer-fortnite/)). **No
ponerlo en una lámina como real.**

### 24.2 Figuras oficiales (pose en 3D)

| Figura | Qué trae | Fuente |
|---|---|---|
| **S.H.Figuarts Nezuko** (Bandai Spirits) | 5 caras, mitad inferior **sentada**, manos para ir **de la mano con Tanjiro**; 8.250 ¥, venta 10-ago-2024 | ✅ [tamashiiweb 14759](https://tamashiiweb.com/item/14759/); [foto](https://tamashiiweb.com/storage/images/products/imported/item_0000014759_vVPMEchI_02.jpg), 560×560 |
| **S.H.Figuarts Tanjiro** | piezas para ir de la mano con Nezuko | ✅ [tamashiiweb 14758](https://tamashiiweb.com/item/14758/); [foto](https://tamashiiweb.com/storage/images/products/imported/item_0000014758_gIs5SJW4_02.jpg), 560×560 |
| **S.H.Figuarts Rengoku** y **Shinobu** | en el catálogo | ✅ [shfiguarts.com](https://www.shfiguarts.com/category/1/355/SHFiguarts/SHFiguarts-Demon-Slayer.html) |
| **Banpresto** (Vibration Stars, Figuarts ZERO) | premios baratos, poses de acción | ✅ catálogo de tamashiiweb |

La Nezuko **sentada con el bambú** da la pose con **volumen real** del
lazo y del *obi* a cuadros, desde varios ángulos: mejor que un fotograma
para calcarla en 3D.

### 24.3 Cosplay bien hecho

- **El *haori* de Tanjiro**: tela **ligera** (algodón o mezcla) para que
  se mueva; patrones de costura **Simplicity 5839** y **Folkwear #129**;
  la trama a cuadros se manda a imprimir (Spoonflower) ✅
  ([AniBladez](https://anibladez.com/blogs/news/the-ultimate-demon-slayer-cosplay-guide)).
  Tutorial en vídeo: [How to Make Tanjiro Kamado's
  Haori](https://www.youtube.com/watch?v=YeQJPdTqgSk) ⚠️ (leídos el
  título y la descripción, no el vídeo).
- **Consejos de convención**: [Popverse](https://www.thepopverse.com/demon-slayer-tanjiro-nezuko-cosplay-anime-convention-social-media).
- **Foto con volumen real**: [Zenitsu, Tanjiro y Nezuko en FanimeCon
  2023](https://upload.wikimedia.org/wikipedia/commons/c/ca/Cosplay_of_Zenitsu_Agatsuma%2C_Tanjiro_Kamado%2C_and_Nezuko_Kamado_from_Demon_Slayer_Kimetsu_no_Yaiba_at_FanimeCon_2023_%2853055055502%29.jpg),
  2048×1365, **CC BY-SA 2.0**, LX-Designs. Se ve cómo cae el *haori* a
  cuadros y el volumen del pelo de Nezuko.
- **Más fotos con licencia CC** (`datos.json`, Openverse/Flickr): 15 de
  **esby.ph** (Nezuko, Zenitsu, el trío; **CC BY-NC-SA 2.0**) y 2 de
  Rengoku de **timz201** (CC BY-NC-SA 2.0), todas en `referencias.json`
  ⚠️ (no miradas una a una).
- **Un cruce en el mundo real**: la [locomotora de vapor «SL Kimetsu no
  Yaiba» en la estación de Futsukaichi, 23-nov-2020](https://upload.wikimedia.org/wikipedia/commons/2/28/Steam_locomotive_Demon_Slayer_SL_Kimetsu_no_Yaiba_Futsukaichi_Station_20201123.jpg),
  3986×2809, **CC BY-SA 3.0**, autor Rsa (Wikimedia Commons, vía
  Openverse). Sólo el título y la foto: quién la organizó, no lo dicen las
  partes ⚠️. Sirve de referencia real para el tren de *Mugen Train*.

---

## 25 · Obras parecidas y láminas vecinas

Segunda pasada (punto 24). Sale de `partes/texto.md` y
`partes/datos-texto.md`.

### 25.1 Series de tono parecido

Las que más recomiendan los usuarios de [AniList](https://anilist.co/anime/101922)
✅ (votos): **Jujutsu Kaisen** (3.343), **Dororo** (1.945), Bleach (385),
My Hero Academia T4 (335), Black Clover (151), Hell's Paradise (148),
Rurouni Kenshin 2023 (107), Hunter x Hunter 2011 (103), Fullmetal
Alchemist: Brotherhood (101), Akame ga Kill! (101), Seraph of the End
(81), Naruto (80) e InuYasha (79).

Todas son *shōnen* de técnicas con nombre y poder que crece. Por tono
visual (ukiyo-e, época histórica, sangre estilizada), la más cercana del
servidor es **Jujutsu Kaisen**.

### 25.2 Lo que la autora reconoce como influencia

| Influencia | Qué dejó | Fuente | Estado |
|---|---|---|---|
| **JoJo, Bleach y Naruto** | sus «tres mayores influencias», en un *twitcast* del 31-oct-2016 | [ScreenRant](https://screenrant.com/demon-slayer-jojos-bizarre-adventure-surprising-influence/) + [livedoor, el editor Katayama](https://news.livedoor.com/article/detail/17760339/) (ja) | ✅ dos de prensa; el *twitcast* original dio 403 ⚠️ |
| **JoJo** en concreto | la **Respiración Total** recuerda a la **Onda (Hamon)** de JoJo, la energía solar que sale de respirar | livedoor: «先生は『ジョジョの奇妙な冒険』はファンだと» | ✅ |
| **Gintama** | la autora lo adora: de ahí el **humor** que corta la tensión (chibis, Inosuke) | livedoor | ⚠️ una fuente, pero de primera mano |
| **Hunter x Hunter** | Tanjiro como «**persona corriente**» (普通の人) entre compañeros excepcionales, idea que un colega del editor comparó con **Gon** | livedoor | ⚠️ una fuente |

**Cambios de diseño que contó el editor** (livedoor ⚠️ una fuente, de
primera mano):

- **Giyu** iba en **kimono**. El editor pidió «más ambiente Taishō» y
  salió el uniforme de **cuello mandarín**.
- **Rengoku** no tenía **máscara de tengu**. «Le falta impacto», dijo el
  editor; «pensé que podría usar una máscara», respondió Gotouge.
- **Tanjiro empezó como secundario**. **Nezuko con el bambú** fue idea de
  la autora desde el principio.

### 25.3 Láminas del servidor que se le parecen (para no repetir)

Comparado con la sección 0 y los conceptos de cada biblia ya hecha:

| Serie | Su canal | En qué se parece | Cómo no repetir |
|---|---|---|---|
| **Jujutsu Kaisen** (32) | ➕ CREAR SALA («Clase extra»), 🍟 General | *shōnen* de Shueisha, técnicas con nombre, marca en el cuerpo | no hacer otra «clase extra»: aquí es **respiración física**, aguante de aire |
| **Naruto** (30) | #reto-de-la-semana, #general-doblaje («La barra de Ichiraku») | técnicas por aliento o chakra; apodos | no repetir **barra con alguien sirviendo**: usar el **telón rojo** (concepto B) |
| **Fullmetal Alchemist** (37) | #general-doblaje («El círculo de tiza»), 🎚️ Mesa de Trabajo, #staff | un **símbolo dibujado** como icono central | no dibujar un símbolo en el suelo: usar la **tablilla de madera** |
| **Attack on Titan** (2) | #reglas («Reglamento del cuartel») | cuerpo militar con rangos | no poner un **reglamento en la pared**: el Aula es entrenamiento |
| **My Hero Academia** (25) | #material-de-clase | una escuela con instructores | lámina 2 del Aula: el **horario del Entrenamiento de los Pilares** (§26.2), no un aula con pizarra |

**Resultado**: los tres conceptos de §27 **no repiten** nada ya hecho.
Ninguna lámina usa un **telón rojo de teatro**, una **tablilla vertical
de madera** ni un **instrumento tocado de oído** (el shamisen de Zenko).

### 25.4 Temas que comparte

- **El duelo y la familia perdida**: con **Violet Evergarden** (22) y
  **Frieren** (33), aunque Demon Slayer tiene mucha más acción.
- **La respiración como técnica de combate y de vida**: ninguna otra
  lámina del servidor la tiene. Es el ángulo más seguro.

---

## 26 · El mundo, la historia por arcos y sus símbolos

Segunda pasada (punto 25). Sale de `partes/texto.md` y
`partes/imagen.md`.

### 26.1 Las reglas del mundo, en cinco líneas

1. **Japón, era Taishō** (1912-1926): trenes de vapor, kimonos y algo de
   ropa occidental ✅ ([Britannica](https://www.britannica.com/topic/Demon-Slayer) + wiki).
2. Los **demonios** (鬼) fueron humanos, corrompidos por la sangre de
   **Muzan Kibutsuji**. Se regeneran, comen personas y **el sol los
   deshace** ✅ ([CBR](https://www.cbr.com/demon-slayer-nichirin-swords-explained/) + wiki).
3. Sólo mueren del todo al sol o **decapitados con una espada Nichirin**
   (日輪刀), forjada con **arena y mineral de hierro escarlata** de la
   **Montaña de la Luz Solar**. La hoja **cambia de color** la primera
   vez que la desenvaina su dueño; si no tiene nivel, queda negra ✅ (CBR
   + [ficha «Nichirin Sword»](https://kimetsu-no-yaiba.fandom.com/wiki/Nichirin_Sword)).
4. Los cazadores usan la **Respiración Total** (全集中の呼吸): más fuerza,
   velocidad y percepción. Cada escuela tiene **Formas** (型) numeradas y
   todas vienen de la **Respiración del Sol** (la del Hinokami Kagura) ✅.
5. El **Cuerpo de Cazadores de Demonios** (鬼殺隊) **no lo reconoce el
   gobierno** y existe «desde tiempos antiguos» ✅ ([ficha «Demon Slayer
   Corps»](https://kimetsu-no-yaiba.fandom.com/wiki/Demon_Slayer_Corps)).

### 26.2 La historia por arcos

Fuente: [CBR, todos los arcos en orden](https://www.cbr.com/demon-slayer-arcs-chronological-order/)
✅. Capítulos del manga según CBR; episodios con la numeración de §2.

| # | Arco | Manga · anime | Qué pasa | Momento clave |
|---|---|---|---|---|
| 1 | **Selección Final** | cap. 1-9 · ep. 1-5 | Muzan mata a la familia; Nezuko, demonio; Tanjiro entra al Cuerpo | el entrenamiento de Urokodaki y el examen |
| 2 | **Demonio del Pantano** | cap. 10-13 · ep. 6-7 | primera misión | primer combate de verdad |
| 3 | **Asakusa** | cap. 14-19 · ep. 8-10 | Tanjiro ve a Muzan en Tokio; conoce a Tamayo | primer choque con el villano |
| 4 | **Mansión del Tambor** | cap. 20-27 · ep. 11-14 | llegan **Zenitsu** e **Inosuke** | Zenitsu dormido, en serio |
| 5 | **Monte Natagumo** | cap. 28-44 · ep. 15-21 | la familia araña; **Rui** | el **Hinokami Kagura** (ep. 19, §22.4) |
| 6 | **Entrenamiento de recuperación** | cap. 45-53 · ep. 22-26 | se presentan los **Pilares** y **Ubuyashiki**; curación en la **Mansión Mariposa** | la primera reunión de los Pilares; la calabaza (T1-25) |
| 7 | **Tren Mugen** | cap. 54-66 · ep. 27-33 y la película | **Rengoku** contra **Akaza** | muere el Pilar de la Llama |
| 8 | **Distrito Rojo** | cap. 67-97 · ep. 34-44 | **Tengen** y sus tres esposas contra **Daki y Gyutaro** | primera victoria sobre una Luna Superior |
| 9 | **Aldea de los Herreros** | cap. 98-127 · ep. 45-55 | **Nezuko resiste el sol** | giro de toda la trama |
| 10 | **Entrenamiento de los Pilares** | cap. 128-136 · ep. 56-63 | cada Pilar entrena a los demás **en su especialidad** | el «horario de clases» (lámina 2 del Aula) |
| 11 | **Castillo Infinito** | cap. 137-183 · película de 2025 | asalto al castillo de Muzan | el pasado triste de los villanos |
| 12 | **Hasta el amanecer** | cap. 184-205 | batalla final contra Muzan; Tanjiro es demonio un rato y vuelve | epílogo con sus descendientes en el siglo XXI |

(La parte de texto ponía el Tren Mugen en «ep. 27-34»; lo corregí a
**27-33** con la tabla de §2: el ep. 34 ya es del Distrito Rojo.)

### 26.3 Rangos y vocabulario del Cuerpo

Wikitexto de la ficha «Demon Slayer Corps», sección *Positions* ✅:

| Rango | Japonés | Qué es |
|---|---|---|
| **Oyakata** («el señor de la casa») | お館様 | el líder, siempre un **Ubuyashiki** |
| **Pilar** | 柱 (*Hashira*) | los más fuertes; su aprendiz es el **Tsuguko** (継子) |
| **Cazador** | 鬼狩り | el grueso del Cuerpo |
| **Instructor** | 育手 | entrena antes de la Selección (Urokodaki) |
| **Kakushi** | 隠 («los ocultos») | apoyo sin espada: curan, limpian y **cosen los uniformes** |
| **Herreros** | 刀鍛冶 | forjan las espadas en su aldea escondida |

**Los Doce Kizuki** (十二鬼月, «Doce Lunas Demoníacas»): los demonios más
fuertes de Muzan. **6 Superiores** (上弦) y **6 Inferiores** (下弦), del 1
al 6. Los Superiores llevan **el kanji del rango en un ojo y el número en
el otro** ✅ ([ficha «Twelve Kizuki»](https://kimetsu-no-yaiba.fandom.com/wiki/Twelve_Kizuki)
+ [GamesRadar+](https://www.gamesradar.com/entertainment/anime-movies/demon-slayer-upper-moons-twelve-kizuki-ranks/)).

### 26.4 Símbolos y objetos que un fan reconoce al instante

- La **glicinia** del Cuerpo y las casas-refugio (§20.2).
- El kanji **滅** en la espalda; **惡鬼滅殺** en la hoja (§7.1).
- La **Marca del Cazador** (痣) y las ***tsuba*** de cada uno (§20.2).
- Los **pendientes *hanafuda*** de Tanjiro: sol rojo sobre montaña (§14.2).
- La **caja de madera** de Nezuko y su **bambú**.
- El **cuervo mensajero** (鎹鴉) y Chuntarō (§7.1).
- La **máscara de tengu** de Urokodaki (§8).

**Palabras** (japonés, lectura, y cómo va en latino):

| Japonés | Lectura | Qué es |
|---|---|---|
| 全集中の呼吸 | *Zenshū Chū no Kokyū* | Respiración Total (Concentración Total) |
| 型 | *kata* | Forma («Agua, Primera Forma») |
| 鬼殺隊 | *Kisatsutai* | Cuerpo de Cazadores de Demonios |
| 柱 | *Hashira* | Pilar (así en latino, §7.5) |
| 痣 | *aza* | la Marca |
| 日輪刀 | *Nichirin tō* | espada Nichirin |
| 鬼 | *oni* | demonio |

---

## 27 · Tres conceptos de lámina

Los tres son **distintos**: sitio, objeto, personaje y cuadro de diálogo
cambian. A y B son para **LA ACADEMIA** (el Aula y su lámina 2); C es para
**#que-estas-escuchando**, que está **libre**.

### Concepto A — «La calabaza de la Mansión Mariposa» (🔊 Aula) ⭐ el recomendado

- **Objeto real en un sitio real**: **una fila de calabazas (瓢箪) de menor
  a mayor**, atadas con **cordón rojo**, sobre el **suelo de madera del
  *engawa*** de la Mansión Mariposa (T1-25, 00:04:29 a 00:04:50 ✅; fondos
  n.º 3). La más grande es **del tamaño de una silla**, como dice el wiki
  ✅. **Cada calabaza lleva una etiqueta de papel** (*washi*) colgada del
  cordón con un texto. **Se hace en Blender**: calabazas por torno
  (*Spin*) o el modelo CC BY *Hyotan Stylized* (§4.1); papel con la tinta
  que **sigue la curva**; tablones *Dark Wooden Planks* (CC0).
- **Personaje**: **Shinobu**, de pie en el *engawa*, **índice arriba**
  (personajes n.º 2), sonriendo con los ojos entornados. Detrás, en el
  patio, **Tanjiro** en ropa de paciente **soplando una calabaza**
  (personajes n.º 8) y las **tres niñas** animando.
- **Cómo habla**: **no hay globo**. Su nombre y el del canal van como la
  **cartela de nombre vertical a pincel** del anime (personajes n.º 4):
  «**Aula**» grande en **Yuji Boku**, y encima, pequeño, «LA ACADEMIA»
  (donde el anime pone «蟲柱»). Su frase va en **una tira de papel vertical
  (*tanzaku*)** clavada al pilar de madera junto a ella, en **Zen Old
  Mincho**: «**Aquí se entrena la voz. Cuento contigo**» («Cuento contigo»
  es su «期待していますね», T1-25, 00:19:32 ✅).
- **Dónde va cada texto**:
  - cartela vertical a la derecha: **Aula**
  - calabaza grande (delante): **Aquí se da la clase, en vivo**
  - calabaza 2: **Doblaje y canto**
  - calabaza 3: **El horario está en avisos-clases**
  - calabaza 4: **Activa el aviso en Canales y roles**
  - calabaza 5: **Lo de cada clase queda en material-de-clase**
  - calabaza pequeña: **¿Te quedó una duda? Pregunta en dudas**
  - tira de papel en el pilar: la frase de Shinobu
- **Que no quede plano**: la **calabaza grande en primer plano**, abajo a
  la izquierda, **desenfocada**; **mariposas** (su símbolo) cruzando por
  delante; **luz de tarde entre la valla de bambú** que raya el suelo;
  la cámara a la altura del *engawa* con el jardín al fondo.
- **Luz y paleta**: tarde cálida; madera `#866954`, tierra `#C8C08E`,
  calabaza `#853920`, cordón rojo, *haori* de Shinobu blanco-turquesa-rosa
  (§5 y §16).

### Concepto B — «El escenario del Secreto de la era Taisho» (lámina 2 del Aula o #avisos-clases)

- **Objeto real en un sitio real**: **el escenario con telón rojo**
  (`#B91F2A`) donde se cuentan los Secretos en el arco de los Pilares (clip
  Shinobu, 0:00; clip Rengoku, 1:31: se ven **bambalinas y focos**) y
  **cuatro tablillas de madera con mango** como la «その1» de los
  Secretos (objetos n.º 6-7). **Se hace en Blender**: telón con tela y
  pliegues, tablillas de madera con papel pegado.
- **Personaje**: **Tanjiro**, el que presenta los Secretos, **cuchicheando
  con la mano en la boca** (personajes n.º 10); a su lado **Mitsuri**
  con las **manos en las mejillas** y corazones (personajes n.º 22).
- **Cómo habla**: el **título del Secreto** arriba, como en el anime:
  «**Secretos de la era Taisho**» en **Kaisei Decol**, y la frase de
  Tanjiro abajo, en papel: «**Aquí va un secreto: así va una clase**».
  Cierra con la cartela **«Continuará»** en franjas de los colores de la
  Mansión Mariposa (menta `#B3DBD4`, rosa `#CF99AA`, morado `#773A87`, con
  mariposas), igual que la «つづく» del clip (0:57).
- **Dónde va cada texto** (una tablilla en cada mano de los personajes, o
  apoyadas en el borde del escenario, numeradas «**1**», «**2**», «**3**»,
  «**4**» como la «その1»):
  1. **Calentar el cuerpo y la voz** (los estiramientos)
  2. **Ejercicio rápido** (las tazas de té)
  3. **La escena completa** (el pilla-pilla)
  4. **El reto: aguantar el aire** (la calabaza)
  (Es una idea: hay que cambiar los textos por **cómo es la clase de
  verdad**.)
- **Que no quede plano**: el **borde del telón** entra por delante,
  desenfocado; **focos** con halo arriba; el suelo del escenario refleja la
  luz; los personajes proyectan sombra en el telón.

### Concepto C — «Zenko y el shamisen» (#que-estas-escuchando, libre)

- **Objeto real en un sitio real**: **un shamisen** tumbado en diagonal
  sobre el **tatami** de la **casa Kyōgoku**, con el **biombo del pino**
  detrás (clip de Zenko, 0:01 ✅; fondos n.º 13). Su **mástil hace de
  barra de notas**, como en el minijuego de *Hinokami 2* (objetos n.º 16).
  **Se hace en Blender**: shamisen CC BY (§4.1) o por cajas; tatami CC0.
- **Personaje**: **Zenitsu vestido de Zenko** (1.º en la encuesta grande),
  arrodillado, **rasgueando furioso** con **rayos verdes** alrededor
  (personajes n.º 14-15). Al fondo, dos chicas del local, desenfocadas,
  asombradas (clip, 0:07).
- **Cómo habla**: el título como el «**BEGIN!**» del juego: «**Qué estás
  escuchando**» en **pincel dorado** (Yuji Boku con degradado dorado) arriba.
  Los textos **son las «notas» que corren por el mástil**, cada uno en una
  pastilla redonda de madera. La frase de Zenitsu, en **cartela vertical a
  pincel** a un lado: «**Todo lo vivo suena**» (su «生き物からは とにかく音が
  している», T1-13, 00:17:54 ✅). Debajo, pequeño, lo que dicen las chicas:
  «**La oye una vez y ya la toca**» (DR-2, 00:14:10 ✅).
- **Dónde va cada texto**: arriba, el título dorado; en el mástil, de
  izquierda a derecha: **La canción que llevas en bucle** · **Pega el
  enlace** · **Y di por qué** (en la lámina, cada uno en su pastilla, sin
  «·»); la cartela vertical de Zenitsu a la derecha.
- **Que no quede plano**: **la punta del mástil** sale hacia la cámara,
  desenfocada; chispas verdes delante de todo; luz de **farol naranja**
  (`#C68146`) de un lado y noche azul del otro; el biombo del pino al fondo.

### ¿Cuál primero?

**A**. Es el que mejor junta lo que pide el dueño: un **objeto real que se
hace en Blender** (las calabazas con sus etiquetas), un **sitio real** de
la serie con luz de día, la **profe más querida** de la Mansión y una
**cartela de la propia serie** en vez de un globo. Y dice justo lo que es
el servidor: **aquí se entrena la voz**. **C** es la mejor si se prefiere un
canal **sin serie asignada**.

---

## 28 · Lo que no pude verificar

- **Frases latinas textuales sacadas de subtítulos**: YouTube bloquea desde
  este contenedor los subtítulos y los vídeos («no soy un robot», y el
  `timedtext` devuelve «We're sorry… automated queries»). Las frases
  latinas de §10.4 salen de **Doblaje Wiki** y de **títulos de vídeos**,
  no del audio. «**Enciende tu corazón**» (Rengoku) queda ⚠️: no sé si es
  la frase latina o la de España.
- **«¡Te presento a Filemón!»**: por el título, el doblaje latino le pone
  un nombre a algo del ep. 7 de los Herreros; no lo comprobé ⚠️.
- **La caja de diálogo del modo historia** de los juegos *Hinokami*: las
  capturas oficiales vienen sin interfaz ⚠️.
- **Obanai, Sanemi, Akaza, Doma** y otros secundarios: sus voces latinas
  sólo están en Doblaje Wiki (una fuente) ⚠️.
- **El «escuadrón Kamaboko»** como nombre de fans del trío: de memoria ⚠️.
- **Los pendientes de Tanjiro cambiados en Asia**: de memoria ⚠️.
- **La vena de Shinobu** cuando se enfada sonriendo: de memoria ⚠️.
- **Globos del manga y ediciones latinas** (Panini México, Ivrea): no
  revisé páginas ⚠️.
- **TikTok**: no se abre desde aquí; sólo títulos de búsqueda ⚠️.
- **Pixiv y DeviantArt**: sin búsqueda propia ⚠️.
- El minuto de los vídeos mirados por **storyboard** puede moverse ±1-2 s.
- El **Aula** no tiene descripción en el inventario: los textos de §0 son
  una **propuesta** y hay que confirmarlos con el dueño.

---

## Cumplimiento del encargo

| Punto de `ENCARGO.md` | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial en cantidad y variado | ✅ | 4.314 + 257 imágenes de la wiki en 96 hojas; miré las 12 más grandes y busqué por título; 3 hojas propias con 84 imágenes numeradas (§3) |
| 2 · Fotogramas de escenas icónicas con capítulo y minuto | ✅ | minutos de los subtítulos japoneses de Netflix (§2) y fotogramas de storyboard (§12) |
| 3 · Fan art, renders 3D y modelos libres | ✅ | 15 modelos de Sketchfab con licencia de la API, 9 recursos CC0 (§4) |
| 4 · Fondos y sitios, paleta y texturas | ✅ | 11 sitios, paleta medida con Pillow, texturas CC0 (§5) |
| 5 · Tipografía y letras libres con tildes | ✅ | letras de la web oficial leídas en su CSS; 25 archivos comprobados con fontTools (§6) |
| 6 · Cómo hablan y piensan en pantalla | ✅ | 11 recursos propios vistos (§7); falta la caja del juego ⚠️ |
| 7 · Personajes y encuestas | ✅ | las dos encuestas oficiales en dos fuentes (§9) |
| 8 · Frases del doblaje latino y reparto en dos fuentes | ⚠️ | reparto principal en Doblaje Wiki + ANMTV ✅; frases sin subtítulos (YouTube bloqueado): salen de Doblaje Wiki y títulos (§10.4) |
| 9 · Música | ✅ | los 10 temas y las canciones internas (§11) |
| 10 · Vídeos con minuto exacto | ✅ | 10 vídeos mirados por storyboard, con enlace `&t=` (§12); el minuto ±1-2 s |
| 11 · Videojuegos: interfaz y cajas | ⚠️ | minijuego del shamisen visto; caja del modo historia no (§13) |
| 12 · Lo que ama el fandom y qué NO hacer | ✅ | §14 |
| 13 · Descripción profunda de cada personaje | ✅ | 12 personajes, con cómo hablan y minuto (§8) |
| 14 · Poses analizadas (6-10 por personaje) | ✅ | Shinobu 7, Tanjiro 6, Zenitsu 6, Rengoku 8, más 6 de Mitsuri, Kanao, Aoi y Tengen (§15) |
| 15 · Vestuario con hex | ✅ | §16 (medidos o marcados ⚠️) |
| 16 · Paisajes y fondos de pantalla | ⚠️ | sitios con luz ✅; fondos de fans en alta casi no hay (Wallhaven dio 1) (§17) |
| 17 · Guía para IA | ✅ | §18 |
| 3 conceptos de lámina | ✅ | §19, con objeto, personaje, cuadro, textos y profundidad |
| 40 fuentes distintas | ✅ | 52 en la bitácora (§21) |
| Tipos: oficiales | ✅ | webs oficiales, CSS, manual del juego, Steam, PV de Aniplex, entrevista de ufotable en los Oscars |
| Tipos: otros idiomas | ⚠️ | japonés (subtítulos, animatetimes, GAME Watch, webs) ✅; chino: Bilibili dio 412 ❌; coreano no ❌ |
| Tipos: wikis, TV Tropes, TCRF, Wayback | ⚠️ | Fandom y Doblaje Wiki ✅; TV Tropes 403 y por Wayback sólo la portada; TCRF 403 (Cloudflare) |
| Tipos: foros y comunidades | ✅ | Reddit por Arctic Shift |
| Tipos: arte (Pixiv, ArtStation, DeviantArt) | ⚠️ | ArtStation y Reddit ✅; Pixiv y DeviantArt no |
| Tipos: vídeo | ✅ | §12 |
| Tipos: código y recursos | ✅ | GitHub (subtítulos, Google Fonts), Sketchfab, Poly Haven, ambientCG |
| Tipos: doblaje latino | ✅ | Doblaje Wiki, ANMTV, SensaCine, entrevistas en YouTube (§10.5) |
| Hojas de contacto (máx. 3, < 3 MB) | ✅ | `personajes_01.jpg` 0,98 MB, `objetos_01.jpg` 0,86 MB, `fondos_01.jpg` 0,66 MB |
| `referencias.json` (20-40, medidos, url = imagen) | ✅ | 36 entradas; 30 URL de imagen comprobadas (HTTP 200); 6 vídeos con `&t=` y el tamaño del fotograma medido |

---

## 29 · Bitácora de búsqueda

### 29.1 Red

- **Funcionó**: Kimetsu no Yaiba Wiki y Doblaje Wiki (API), GitHub (clon
  parcial), Google Fonts (GitHub raw), dafont, Sketchfab, Poly Haven,
  ambientCG, Arctic Shift, Wallhaven, API de Steam, webs oficiales
  japonesas, `yt-dlp` para datos y **storyboards**.
- **Bloqueado**: vídeos y subtítulos de YouTube («Sign in to confirm you're
  not a bot»; `timedtext` → «automated queries»); Wikipedia API (429);
  TV Tropes (403) y sus subpáginas por Wayback (se cortó la conexión dos
  veces); fontmeme y The Cutting Room Floor (Cloudflare, 403); betterstudio (no resuelve); Bilibili
  (412); sonica.mx (429 y página vacía).

### 29.2 Búsquedas web (9 del cupo de 50)

| # | Idioma | Búsqueda | Qué dio |
|---|---|---|---|
| 1 | es | Demon Slayer doblaje latino reparto Iván Bastidas… | ANMTV, SensaCine, nintenderos, Cine PREMIERE |
| 2 | es | Rengoku doblaje latino «enciende tu corazón» | TikTok de Winslow y de SDV; nada textual |
| 3 | es | Rengoku «sabroso» doblaje latino | vídeo de reacción «¡¡SABROSO!!»; Doblaje Wiki |
| 4 | en | Demon Slayer logo font dafont | Blood Crow Condensed (FontBolt, dafontonline) |
| 5 | es | Arco del Entrenamiento de los Pilares doblaje latino elenco | Armando Corona (Muichiro); Sanemi/Obanai no |
| 6 | es | Castillo Infinito taquilla México récord | Xataka, LOS40, Merca2.0, Infobae |
| 7 | ja | 鬼滅の刃 人気投票 結果 第2回 | animatetimes, GAME Watch, 130.316 votos |
| 8 | en | gameuidatabase Hinokami Chronicles dialogue | nada de Game UI Database |
| 9 | en | artstation Demon Slayer Shinobu fan art | 7 obras en ArtStation |

### 29.3 Sin cupo (API, git, descargas)

- `investigar_serie.py` (2 pasadas: personajes y sitios).
- Kimetsu Wiki `action=parse` de **58 páginas** (personajes, sitios,
  técnicas, *Taisho Secret*, *Rehabilitation Training*, juegos, canciones).
- Doblaje Wiki `action=parse`: serie, *Mugen Train*, *Castillo Infinito*,
  7 fichas de personaje y 6 de actores.
- `git clone --filter=blob:none` de kitsunekko-mirror y `git show` de **65
  archivos** de subtítulos (Netflix `ja[cc]` y el de la película del
  Castillo).
- `yt-dlp` (`ytsearch`, `-j`, `-f sb0`) sobre ~40 vídeos; 11 storyboards
  mirados en hojas.
- CSS de 5 webs oficiales; manual y modos de juego de *Hinokami*.
- API de Sketchfab (17 búsquedas), Poly Haven, ambientCG, Wallhaven,
  Steam; Arctic Shift (8 consultas).

### 29.4 Fuentes consultadas (52)

**Oficiales (15)**: [kimetsu.com/anime](https://kimetsu.com/anime/) ·
[kimetsu.com/anime/hashirageikohen](https://kimetsu.com/anime/hashirageikohen/) ·
[kimetsu.com/anime/mugenjyohen_movie](https://kimetsu.com/anime/mugenjyohen_movie/) ·
[demonslayer-anime.com](https://demonslayer-anime.com/) ·
[game.kimetsu.com/hinokami](https://game.kimetsu.com/hinokami/) (modos y manual) ·
[game.kimetsu.com/hinokami2](https://game.kimetsu.com/hinokami2/) ·
[asia.sega.com/kimetsu_hinokami2](https://asia.sega.com/kimetsu_hinokami2/en/) ·
[Steam 1490890](https://store.steampowered.com/app/1490890/) y [2928600](https://store.steampowered.com/app/2928600/) ·
[PV de Aniplex (staff)](https://www.youtube.com/watch?v=Tf31dGdlWxE) ·
[ufotable, vídeo especial](https://www.youtube.com/watch?v=ckGTdMYV6Xg) ·
[Oscars: el equipo de ufotable](https://www.youtube.com/watch?v=FLB_sLTgbPk) ·
[Crunchyroll en Español](https://www.youtube.com/watch?v=OQ-S0SYxOGI) (6 clips) ·
[Sony Pictures México](https://www.youtube.com/watch?v=sqgSm8fWe1s) ·
[LiSA Official](https://www.youtube.com/watch?v=x1FV6IrjZCY) ·
[Aimer Official](https://www.youtube.com/watch?v=QORbTrXHpsA).

**Wikis (4)**: [Kimetsu no Yaiba Wiki](https://kimetsu-no-yaiba.fandom.com/) ·
[Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Demon_Slayer:_Kimetsu_no_Yaiba) ·
[TV Tropes por Wayback](https://web.archive.org/web/2024/https://tvtropes.org/pmwiki/pmwiki.php/Manga/DemonSlayerKimetsuNoYaiba) (sólo portada) ·
[Wallhaven](https://wallhaven.cc/w/vp2qv3).

**Prensa y datos (12)**: [ANMTV](https://www.anmtvla.com/2021/01/demon-slayer-kimetsu-no-yaiba-llega.html) ·
[SensaCine México](https://www.sensacine.com.mx/noticias/noticia-1000041873/) ·
[Nintenderos](https://www.nintenderos.com/2023/09/demon-slayer-estos-son-los-actores-de-doblaje-en-latino-de-la-nueva-temporada-de-kimetsu-no-yaiba/) ·
[Xataka México](https://www.xataka.com.mx/anime/demon-slayer-castillo-infinito-rompe-todos-records-mexico-supero-a-dragon-ball-mejor-debut-para-pelicula-anime) ·
[LOS40 México](https://los40.com.mx/2025/09/30/demon-slayer-kimetsu-no-yaiba-castillo-infinito-rompe-records-en-latinoamerica/?outputType=amp) ·
[Merca2.0](https://www.merca20.com/demon-slayer-castillo-infinito-rompe-record-y-se-convierte-en-la-pelicula-mas-taquillera-de-anime-en-la-historia-de-mexico/) ·
[animatetimes (ja)](https://www.animatetimes.com/news/details.php?id=1783587640) ·
[GAME Watch (ja)](https://game.watch.impress.co.jp/docs/news/1285358.html) ·
[Xataka: Pilares en latino](https://www.xataka.com.mx/anime/demon-slayer-kimetsu-no-yaiba-hashira-training-arc-doblaje-latino-cuando-a-que-hora-sera-estreno-mexico) ·
[Geekmi](https://www.geekmi.news/series/Demon-Slayer-Arco-de-Entrenamiento-Pilar-confirma-doblaje-latino-y-fecha-de-llegada-a-Crunchyroll-20240625-0006.html) ·
[Cine PREMIERE](https://cinepremiere.com.mx/demon-slayer-doblaje-aniplex-netflix.html) (sólo en resultados) ·
[Infobae](https://www.infobae.com/estados-unidos/2025/09/16/demon-slayer-castillo-infinito-debuta-con-usd-70-millones-y-desplaza-a-la-secuela-de-el-conjuro-al-segundo-lugar/) (sólo en resultados).

**Letras (4)**: [FontBolt](https://www.fontbolt.com/font/demon-slayer-font/) ·
[dafontonline](https://dafontonline.com/demon-slayer-font/) ·
[dafont: Blood Crow](https://www.dafont.com/blood-crow.font) ·
[google/fonts](https://github.com/google/fonts).

**Código, 3D y texturas (4)**: [kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror) ·
[Sketchfab](https://sketchfab.com/) · [Poly Haven](https://polyhaven.com/) ·
[ambientCG](https://ambientcg.com/).

**Comunidad y arte (5)**: [Arctic Shift (Reddit)](https://arctic-shift.photon-reddit.com/) ·
[r/KimetsuNoYaiba](https://reddit.com/r/KimetsuNoYaiba/comments/n2id9u/) ·
[ArtStation: Fan Yang](https://www.artstation.com/artwork/aRzDBz) ·
[ArtStation: Anna April](https://www.artstation.com/artwork/xYeLQr) ·
[ArtStation: Bulkamancer](https://www.artstation.com/artwork/AZZyNz).

**Vídeo de fans y doblaje (8)**: [Pratz: Uraz Huerta](https://www.youtube.com/watch?v=ydYTmycYs2M) ·
[Pratz: Marc Winslow](https://www.youtube.com/watch?v=kMDucA2CdUs) ·
[Soy Idzi](https://www.youtube.com/watch?v=QvK7-cPWRbo) ·
[Friki Feria 2022](https://www.youtube.com/watch?v=yibRjVzbJgU) ·
[PikaMauri 64](https://www.youtube.com/watch?v=Mi_vqp2GB-Y) ·
[STORM MASTER](https://www.youtube.com/watch?v=VUMxmU9ksIU) ·
[Damon Billiot](https://www.youtube.com/watch?v=lEkLJX0q6gs) ·
[Khromaki](https://www.youtube.com/watch?v=GhFhePAHo3w).

### 29.5 Lo que NO encontré

- Subtítulos latinos de clips oficiales (bloqueados).
- La caja de diálogo del modo historia de *Hinokami*.
- Página de The Cutting Room Floor de los juegos (403 de Cloudflare: no sé si existe).
- Fuentes en **coreano o chino** (Bilibili dio 412; no busqué en Naver).
- Una tercera encuesta oficial (animatetimes confirma que no hubo).
- Fondos de pantalla de fans en alta resolución (Wallhaven sólo dio uno).

---
