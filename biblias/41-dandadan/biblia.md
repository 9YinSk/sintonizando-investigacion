---
tags: [biblia, serie, laminas, biblioteca]
serie: "Dandadan (ダンダダン, DAN DA DAN)"
canal: "sin canal: propuesta 📻 RADIO EN VIVO (alternativas #log-mod y 🍿 Cine, ver §0)"
fecha: 2026-09-25
---

# Biblia · Dandadan — para la biblioteca

> [!important] Cómo se hizo, y sus límites
> - La escribió el **redactor** sólo con las partes del equipo
>   (`partes/imagen.md`, `video.md`, `voz.md`, `texto.md`,
>   `episodios.md` y, para completar, los `datos-*.md` y los `.json`).
>   Nada nuevo sin fuente.
> - **YouTube pidió iniciar sesión** y **AnimeThemes estaba caído**
>   (HTTP 522). Los vídeos se miraron en **Internet Archive** (episodios
>   1 a 8 de la T1, a 720p) y **Dailymotion** (tráileres, a 512×288).
>   Los fotogramas en 1920×1080 son los de la wiki, sin minuto.
> - **Frases del doblaje latino**: 2 oídas con `voz.py` en el episodio 1
>   con audio latino de Crunchyroll, más 12 que cita Doblaje Wiki con su
>   episodio (§10).
> - El redactor **miró las 3 hojas de `hojas/` número a número** y las
>   hojas de fotogramas de la parte de vídeo. Corrigió cosas de las
>   partes: la «forma humana de Turbo Granny» del ep. 5 es **Seiko**, la
>   abuela de Momo; la figura «TENITOL Momo» es **Okarun**; dos frases
>   latinas son de Netflix, no de Crunchyroll (§28).
> - **Punto 13 incompleto**: el investigador de voz agotó sus 2 tandas.
>   Falta la vergüenza y la tristeza de Aira despierta, y a Turbo Granny
>   le faltan alegría, tristeza, miedo y vergüenza (§8.6).
> - ✅ = dos fuentes o visto por nosotros. ⚠️ = una sola fuente, o algo
>   que hay que comprobar. Lo que falta está en §28 y en la tabla final.

## Índice

Entre corchetes, el punto de `ENCARGO.md` que cubre cada sección.

0. Dandadan no tiene canal: dónde encaja mejor
1. Resumen para quien tenga prisa
2. Las escenas que sirven, con minuto [2]
3. Arte oficial y hojas de contacto [1]
4. Fan art y 3D, sólo como referencia [3]
5. Sitios, luz, paleta y texturas reales [4]
6. Tipografía: una letra para cada uso [5]
7. Cómo hablan en pantalla: el globo y el color [6]
8. Los personajes: qué transmiten, su cara y sus dinámicas [13]
9. ¿Quién es el más querido? [7]
10. Doblaje latino y frases textuales [8]
11. Música y sonido [9]
12. Vídeos y tendencias [10]
13. Videojuegos de la franquicia [11]
14. Lo que ama el fandom, y qué NO hacer [12]
15. Poses analizadas por personaje [14]
16. Vestuario, con hex medidos [15]
17. Paisajes y fondos de pantalla [16]
18. Guía para generar con IA: imagen y texto [17]
19. Estilo de dibujo, técnica, Blender y encuadres [18]
20. Texturas 2D [19]
21. Gustos y detalles de cada personaje [20]
22. Por qué la gente la ama, y las escenas que hacen llorar [21]
23. Fan dubs y comunidad hispana [22]
24. Colaboraciones, figuras y cosplay [23]
25. Obras parecidas y láminas vecinas [24]
26. El mundo, la historia por arcos y sus símbolos [25]
27. Tres conceptos de lámina
28. Lo que no pude verificar, y lo que corregí de las partes
- Cumplimiento del encargo
29. Bitácora de búsqueda

---

## 0 · Dandadan no tiene canal: dónde encaja mejor

El encargo dice por qué está: **fenómeno reciente**. Las partes lo
confirman: 4.º en el Top 10 global de Netflix (no inglés), 1.º de la
temporada en Niconico, 22 nominaciones y 2 premios en los Crunchyroll
Anime Awards (§22). Y para un servidor de doblaje tiene algo único:
**dos doblajes latinos a la vez**, Netflix y Crunchyroll, con nombres
distintos para los mismos personajes (§10).

Miré los textos reales de `servidor/inventario.md`, lo que proponen las
otras biblias (`grep '^canal:' biblias/*/biblia.md`), los tres ejemplos
de `_ya_hechas/` y los avisos de `lotes/D.md`. En 37-40 ya chocan
**#general-doblaje, #destacados, 🎲 Juegos, #eventos, 🎭 Escenario,
🎚️ Mesa de Trabajo, 🎙️ Grabación, #staff, #postulaciones,
#que-estas-escuchando, 🍟 General y #config-bots**. Ninguna de mis tres
propuestas está en esa lista.

El único canal público **que nadie pide** es **📻 RADIO EN VIVO**.
#demos-canto parecía libre, pero es de Bocchi (`_ya_hechas/`, y ya
tiene su lámina 2 con el teclado).

### 0.1 La propuesta

| Orden | Canal o sala | Texto real del inventario | Por qué Dandadan | Choca con |
|---|---|---|---|---|
| **1 (recomendado)** | **📻・RADIO EN VIVO** (EN VIVO, escenario) | «La radio de la casa. Pides por comandos y suena aquí.» | Okarun **llamó al cielo desde niño y nadie vino** (ep. 1, 15:00-15:47, con su revista ocultista abierta en «cómo llamar a…»). Aquí sí: lo pides y suena. Okarun es el **1.º de la encuesta oficial** (§9) | **nadie** |
| 2 | **ıı・🧾・log-mod** (REGISTRO, privado) | «Cada sanción, quién y por qué.» | **Turbo Granny acabó sellada** en un gato de la suerte con un talismán «contra el mal» pegado (ep. 5, 16:05-17:16). La sancionada explica las sanciones. Es la **3.ª de la encuesta** | nadie la pide. Attack on Titan (02) la nombra dentro de su lámina de #reglas (el libro de actas). Es privado: sirve si los privados llevan lámina |
| 3 | **🍿・Cine** (EN VIVO, voz) | sin descripción en el inventario: la sala para ver algo juntos | Momo pasa **2 horas al día al teléfono con su amiga Kei viendo pelis de Ken Takakura** (*Daizukan*, §21). Ver pelis en llamada es justo esa sala | Los Simpson (29, el sillón). **Ninguna de 37-40** |

**Mi recomendación: la 1.** Es la única libre del todo, su personaje es
el más votado en Japón, el objeto (una revista) se hace en Blender con
papel curvo y brillo real, y la frase que la sostiene está en el
capítulo 1 con su minuto.

### 0.2 Los canales que miré y descarté

| Canal | Por qué encajaba | Por qué no |
|---|---|---|
| #general-doblaje | **el mejor tema**: dos doblajes latinos a la vez, «Turbo Abuela» contra «Turbo Ruca» (§10) | lo piden 29, 37 y 39, y 38 de reserva. No sumo un quinto choque. Queda como idea de lámina 2 para quien se lo quede |
| #reto-de-la-semana | la carrera contra Turbo Granny, que hace trampa al contar (§8.3) | es de Dragon Ball (`_ya_hechas`) y lo piden Naruto (30), Haikyuu (34) y One Punch Man (35) de reserva |
| #demos-canto | Crunchyroll dobló las canciones al español y Netflix no (§11) | es de Bocchi (`_ya_hechas`) |
| #memes | «¿Te parece que somos ricos?» y «¡Cállense, cállense que me desesperan!» son memes del doblaje (§10) | es de JoJo (28) |
| #que-estas-viendo | Tatsu fue asistente de Fujimoto; comparte público con Chainsaw Man (§25) | es de Chainsaw Man (11) |
| 🍟 General (voz) | Okarun **habla mejor por teléfono** que en persona (ep. 1, 10:00-10:30) | lo piden Digimon (40) y Jujutsu Kaisen (32) de segunda opción |
| 🎶 Karaoke, 🎙️ Grabación | Okarun canta «Tímido» de Flans en el doblaje de Crunchyroll (§11) | 29 los da a Sing y a Monsters, Inc.; Sailor Moon (38) pide Grabación de reserva |
| #en-directo, #castings, #redes-y-novedades | — | son de Oshi no Ko (05); #en-directo también lo pide One Punch Man (35) |
| #presentaciones | las dos caras de Aira, la dulce y la de verdad (§8.4) | es de Spy x Family (06) |
| #config-bots | el reparto de comandos de la radio | lo pide Digimon (40, concepto C) |

---

## 1 · Resumen para quien tenga prisa

- **Qué es.** Manga de **Yukinobu Tatsu** (Shueisha, Jump+) y anime de
  **Science SARU** (2024, 12 episodios la T1; T2 en 2025). Una chica
  que cree en fantasmas (Momo) y un chico que cree en extraterrestres
  (Okarun) se retan, y **los dos tienen razón** ([AniList](https://anilist.co/anime/171018) ✅).
- **El tono.** Terror de verdad, chiste verde y romance torpe, todo a
  la vez. La serie **no baja el tono** cuando da miedo ni se pone seria
  cuando hace un chiste (§26).
- **El más querido.** En Japón, **Okarun** (1.º de la encuesta oficial,
  38.699 votos). Fuera de Japón, **Momo** (1.ª en AniList y la más
  dibujada). **Turbo Granny** es 3.ª en la encuesta, por delante de Aira
  (§9).
- **El cuadro de diálogo propio.** No hay juego propio ni caja propia.
  Lo que es de Dandadan es el **código de color por bando**: rojo para
  Turbo Granny y los yokai, azul frío para los extraterrestres Serpo,
  turquesa para los poderes psíquicos (lo dice el director, §7). Encima,
  el **globo del manga**: óvalo fino con colita puntiaguda.
- **El doblaje latino.** Dos a la vez: **Netflix** (New Art, dirige
  Irwin Daayán) y **Crunchyroll** (Audiomaster Candiani, dirige Gerardo
  Márquez). Momo es Azucena Estrada o Alicia Vélez; Okarun, José Luis
  Piedra o Iván Bastidas; Turbo Granny, Rebeca Patiño o Magda Giner
  (§10).
- **La frase que todos reconocen.** El robo de las «bolas doradas» de
  Okarun. En Crunchyroll, los extraterrestres: **«Nos va a tener que dar
  su banana»** (ep. 1, 14:59, oída) (§10).
- **La regla de color.** Lo cotidiano va **cálido y apagado** (25-27 %
  de saturación); lo sobrenatural, **frío o mixto y muy saturado**
  (49-87 %). Medido en 6 fotogramas (§5).
- **Lo que un fan nota al momento.** Mezclar los dos doblajes («Turbo
  Abuela» es Netflix, «Turbo Ruca» es Crunchyroll), dibujar a Turbo
  Granny tierna o a Aira como una chica tonta (§14).
- **La lámina recomendada.** **📻 RADIO EN VIVO**: la revista ocultista
  de Okarun abierta en «cómo llamar a…», en el aula de su infancia.
  «Llamé al cielo toda mi vida. Aquí lo pides y suena.» (§0, §27 A).

---

## 2 · Las escenas que sirven, con minuto

Vistas de verdad con `episodio.py` y `fotogramas.py` sobre Internet
Archive (sub. inglés, 720p) y Dailymotion. Las frases van como las dice
el subtítulo inglés del vídeo o la transcripción japonesa de
`episodios.md`. **No son el doblaje latino** (ése está en §10).

### 2.1 Episodio 1 · «それって恋のはじまりじゃんよ» ✅ visto entero

[Internet Archive](https://archive.org/details/english-sub-s-01.-e-01-op-join).
Es el mejor capítulo para las láminas: salen los cuatro del encargo y
casi todas las caras.

| Minuto | Qué pasa | Para qué sirve |
|---|---|---|
| [1:00-2:30](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=60) | Momo corta con su novio por teléfono. Con sus amigas: le gustaba porque se parecía a **Ken Takakura**; le gustan «los hombres duros» que dicen «**自分、不器用なんで**» («soy un tipo torpe») | la semilla del apodo de Okarun y de su frase del final |
| [4:00-4:30](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=240) | Okarun le enseña a Momo su **revista ocultista**: «No es OVNI, es **UAP**, fenómeno aéreo no identificado». Momo: «うるせーな» («cállate») | Okarun explicando; la revista (§27 A) |
| [5:00](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=300) | Momo: no cree en extraterrestres pero sí en fantasmas; su abuela es **médium** | la premisa |
| [8:00-10:30](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=480) | hablan por teléfono mientras cada uno va a su sitio maldito. Momo le cuenta lo de su abuela. Y le dice: «**por teléfono hablas con soltura**» (電話ごしだとシャキシャキ喋るね) | Okarun y la voz; §0.2 |
| [10:49-11:26](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=649) | **Turbo Granny** persigue a Okarun por el túnel: primero sólo sus **ojos amarillos** en la oscuridad (10:55), luego su silueta | presentar la amenaza |
| [12:00-13:00](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=720) | los **Serpo** tienen a Momo en su OVNI: «somos amistosos», «queremos vuestra banana» | el gag central |
| [13:16-14:10](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=796) | **despierta el poder psíquico de Momo**: todo se vuelve cian | la escena que arranca la serie |
| [14:27-14:46](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=867) | Okarun, **poseído por Turbo Granny**: «Turbo Granny has cursed me!», «Please help! I can't control myself!». Con la voz de ella: «Lemme gobble that weenie!». Un Serpo: «¡Entrar con un **smartphone**! Ni nosotros tenemos esa tecnología» (14:34) | la maldición |
| [15:43-16:02](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=943) | recuerdo: Okarun niño con su revista (titular «…人の呼び方», «cómo llamar a…»), mirando al cielo, con el cielo reflejado en los lentes: «**No matter how much I called for you, you never showed up!**». Luego, en clase, Momo le defiende. **Ojos llorosos**: «She actually stood up for me» (16:02) | el corazón de §27 A |
| [16:12-16:16](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=972) | «**If it's for her sake, I'll even become a monster!**» | Okarun protegiendo |
| [16:50-17:30](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=1010) | recuerdo de Momo niña con **Seiko**: «mete fuerza bajo el ombligo y saca el *ki* por la coronilla». Momo: «perdón, abuela, entonces sólo me daba vergüenza» | la técnica de Momo (y de cualquier cantante) |
| [17:45-18:10](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=1065) | Momo, **aura con dibujo geométrico** en los puños. «La abuela era médium de verdad. Gracias, abuela» | presentar el poder |
| [18:24-19:41](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=1104) | combate final con la forma yokai de Turbo Granny. Ella: «si lo quieres de vuelta, **ven al túnel**» | la villana |
| [21:00-21:54](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=1260) | Okarun: «自分、不器用なんで» (la frase de Ken Takakura). Momo se sobresalta. Él se presenta: «Takakura Ken». Ella **se ríe** con la cabeza hacia atrás (21:54) | el apodo; la risa de Momo |

### 2.2 Episodios 2 a 8 ✅ vistos (fotogramas cada 15 s)

| Episodio | Minuto | Qué pasa |
|---|---|---|
| 2 · [«それって宇宙人じゃね»](https://archive.org/details/english-sub-s-01.-e-02-11-10) | [21:15-21:30](https://archive.org/details/english-sub-s-01.-e-02-11-10?t=1275) | tras el Flatwoods Monster, sentados sin aliento: «I really thought I was gonna die!»; Momo: «What? You change your hairdo?» |
| 3 · [«ババアとババアが激突じゃんか»](https://archive.org/details/english-sub-s-01.-e-03) | [14:15-14:30](https://archive.org/details/english-sub-s-01.-e-03?t=855) | Okarun, cabeza gacha: «So please don't be disappointed with me» |
| 4 · [«ターボババアをぶっ飛ばそう»](https://archive.org/details/english-sub-s-01.-e-04) | casi entero | la carrera contra Turbo Granny, en pantalla roja de «modo maldición» |
| 5 · [«タマはどこじゃんよ»](https://archive.org/details/english-sub-s-01.-e-05) | [11:36-14:04](https://archive.org/details/english-sub-s-01.-e-05?t=696) | **debut de Aira**: choca con Okarun («I'm sorry, are you okay?», 11:49) y luego se burla con sus amigas («That otaku had such a dumb look on his face», 12:44) |
| 5 | [14:11-14:56](https://archive.org/details/english-sub-s-01.-e-05?t=851) | Momo se disculpa **ruborizada**: «I'm not embarrassed about being friendly to you, Okarun» (14:26). Okarun: «I'm very happy that I could make amends with you» (14:34) |
| 5 | [15:12](https://archive.org/details/english-sub-s-01.-e-05?t=912) | Momo **llora de risa** porque a Okarun le faltan las bolas |
| 5 | [15:17-17:23](https://archive.org/details/english-sub-s-01.-e-05?t=917) | **Seiko** examina a Okarun en el tatami, pide un muñeco y le pega un **talismán** al gato de la suerte (16:05): «家内安全 / 厄除» («familia en paz, contra el mal», 17:16) |
| 6 · [«ヤベー女がきた»](https://archive.org/details/english-sub-s-01.-e-06-.compressed) | [6:30-7:00](https://archive.org/details/english-sub-s-01.-e-06-.compressed?t=390) | Aira: «Momo Ayase. She's definitely a demon!» y «I mean, I'm all too pretty!» |
| 7 · [«優しい世界へ»](https://archive.org/details/s-01.-e-07_202411) | ~17:00-20:00 | la historia de Acrobatic Silky; Aira la abraza; **Momo llora** (18:45) |
| 8 · [«なんかモヤモヤするじゃんよ»](https://archive.org/details/s-01.-e-08_202411) | 13:00-17:45 | arco de Kinta y el monstruo tipo dinosaurio. **Aira no sale** |

### 2.3 Tráileres ✅ vistos (Dailymotion, 512×288)

| Vídeo | Minuto | Qué se ve |
|---|---|---|
| [Tráiler oficial japonés](https://www.dailymotion.com/video/x8u8yoq) (0:58) | [0:15](https://www.dailymotion.com/video/x8u8yoq?start=15), [0:16](https://www.dailymotion.com/video/x8u8yoq?start=16), [0:25](https://www.dailymotion.com/video/x8u8yoq?start=25) | Aira decidida; Okarun ajustándose los lentes; Momo de perfil. Créditos del staff 0:01-0:24; logo rojo 0:32 |
| [Tráiler 2](https://www.dailymotion.com/video/x96npto) (1:40) | [0:12](https://www.dailymotion.com/video/x96npto?start=12) | los Serpo: «Please give us your banana» |
| [Tráiler de «Evil Eye»](https://www.dailymotion.com/video/x9khv6a) (0:47, ADN) | [0:30](https://www.dailymotion.com/video/x9khv6a?start=30), [0:34](https://www.dailymotion.com/video/x9khv6a?start=34) | Momo agachada con la mano brillando; Okarun con el ojo encendido: «Momo, utilise ton super-pouvoir!». En cines el 7 y 8 de junio (0:45) |
| [Tráiler T2 con subtítulos en español](https://www.dailymotion.com/video/x9puf5e) (1:45) | [0:23](https://www.dailymotion.com/video/x9puf5e?start=23), [0:44](https://www.dailymotion.com/video/x9puf5e?start=44), [0:55](https://www.dailymotion.com/video/x9puf5e?start=55) | Kinta y su «bola dorada»; el **kaiju** en la ciudad («宇宙怪獣 出現!»); un chico de pelo morado: «¿Quieres palmarla?» |

⚠️ **Resolución.** Los capítulos están a 720p y los tráileres a 512×288.
En 1080p sólo hay fotogramas sueltos de la wiki, **sin minuto**
(«Momo's compassion», «Psychic Grip», «Episode 7»…, §3).

---

## 3 · Arte oficial y hojas de contacto

### 3.1 Las tres hojas (miradas enteras por el redactor)

Están en `hojas/`. Los números son los que usan las partes.

**`personajes_01_wiki.jpg`** (48 imágenes, de la [wiki de Fandom](https://dandadan.fandom.com/wiki/Momo_Ayase)):

| N.º | Qué es | Tamaño | Para qué |
|---|---|---|---|
| 1 | Momo de cuerpo entero, anime, en la calle | 1852×4833 | ropa icónica y proporciones |
| 2 | Momo de camarera | 1920×4551 | otra ropa |
| 3 | Aira con el uniforme del arco Acrobatic Silky, en el pasillo, con su bolso | 1920×4247 | Aira de pie; el bolso (§27 C, alternativa) |
| 4-9 | **obra de teatro**: Aira, el gato de Turbo Granny, Turbo Granny yokai, Momo, Okarun (mano en los lentes), Okarun transformado; fotos sobre fondos de arcoíris | 2520-2756 | volumen real de pelucas y trajes |
| 10 | Momo con ropa de médium | 1600×2992 | vestuario ritual |
| 11 | Okarun derrota a Acrobatic Silky (magenta) | 3341×1080 | panorámica de acción |
| 12-17 | páginas del manga en blanco y negro (Moe Moe Tri-Beam, Pirouette Noble Drill, Okarun esquivando…) | 2160×1578 | trama y línea (§19, §20) |
| 18 | Acrobatic Silky sube al cielo: tres siluetas a contraluz | 1920×1080 | la escena que hace llorar (§22) |
| 21 | Aira sonriendo, primer plano (ep. 5) | 1920×1080 | su cara pública |
| 22 | niebla blanca: Aira y una niña caminando (ep. 7) | 1920×1080 | el final del arco de Aira |
| 25 | **Momo con los ojos cerrados, sonriendo y haciendo la V** | 1920×1080 | alegría (sin minuto ⚠️) |
| 27-30 | Momo con su poder: todo turquesa y cian, manos verdes gigantes | 1920×1080 | el color de lo psíquico |
| 31-36 | el cangrejo espíritu, posesión, Turbo Granny en rojo total | 1920×1080 | el color de Turbo Granny |
| 37 | Momo saltando, página a color del tomo 20 | 1128×1772 | pose de portada |
| 39 | Momo de sirvienta, página a color del tomo 21 | 1080×1702 | otra ropa |
| 40 | el gato de Turbo Granny, cara de fastidio | 1125×1528 | su expresión en el gato |
| 42 | Momo niña, enfadada | 1490×1080 | infancia |
| 47 | concept art de Okarun | 692×2055 | hoja de modelo |
| 48 | Momo con gafas | 1272×1080 | otra cara |

**`personajes_02_wiki.jpg`** (39 imágenes, del 49 al 87):

| N.º | Qué es | Tamaño | Para qué |
|---|---|---|---|
| 49 | concept art de Momo | 685×1990 | hoja de modelo |
| 50 | Momo con psicoquinesis (manga) | 1353×1006 | pose de poder |
| 51 | logo del anime | 1320×975 | §6 |
| 52, 54 | Okarun en *chibi* (Jump+ Jumble Rush), normal y transformado | 883-1024 px | la versión *chibi* oficial |
| 56-61 | *Grand Summoners*: Aira con fuego, Momo con agua, Okarun con rayo verde, normales y «Super Awakening» | 1024×1024 | poses de acción (§24) |
| 63 | Aira con chaqueta marrón y cuello alto | 942×1076 | ropa de calle |
| 64 | página a color estilo cómic americano, archivo «Dandadan (Marvel Comics)» | 750×1334 | ⚠️ ninguna parte dice qué es |
| 66 | concept art de Aira | 590×1570 | hoja de modelo |
| 68-69 | *Honor of Kings*: Momo y Okarun | 1200×738 | la colaboración de 2026 (§24) |
| 70, 73 | páginas del manga con **globos vacíos** | ~1015×800 | la forma del globo (§7) |
| 75 | **concept art de Turbo Granny yokai** | 647×1224 | hoja de modelo |
| 77 | **Okarun de secundaria leyendo su revista** en el pupitre | 897×825 | §27 A |
| 79 | concept art del gato de Turbo Granny | 618×1075 | §27 B |
| 80 | **Okarun niño leyendo su revista** | 897×738 | §27 A |
| 81 | Turbo Granny y el cangrejo, en rojo | 789×770 | color de Turbo Granny |
| 84 | página del manga: puntos de trama sobre negro | 763×752 | lo sobrenatural (§7) |
| 85 | el gato de Turbo Granny (infobox del anime) | 728×766 | §27 B |
| 86 | Okarun ajustándose los lentes (infobox) | 707×782 | su gesto |
| 87 | Okarun con su *kintama* (manga) | 645×786 | el objeto del chiste |

**`personajes_03_oficial_colab.jpg`** (28 imágenes, montada por la parte
de imagen):

| N.º | Qué es | Tamaño | Para qué |
|---|---|---|---|
| 1-6 | **key visuals del [sitio oficial](https://anime-dandadan.com/)**: Momo, Okarun, el gato de Turbo Granny, Turbo Granny yokai, Aira y Seiko (con bate y chaqueta bordada) | 984×1570; Turbo Granny yokai 1290×2055 | **la mejor referencia de cuerpo entero** |
| 7 | modelo de color de Momo | 274×601 | hex del uniforme (§16) |
| 8 | logo del anime | 1320×975 | §6 |
| 9-11 | portadas de Blu-ray 1, 5 y 8 (arte apaisado dentro de marco blanco) | 800×1081-1087 | arte de acción |
| 12-13 | tomo 1 del manga, Japón y Viz | 764×1200, 1400×2100 | portada con el logo |
| 14 | una **casa japonesa antigua en sepia, con nieve** | 1920×1080 | ⚠️ la parte la llama «fachada nocturna de la Casa Maldita»; en la hoja se ve de día y en sepia |
| 15 | un **pasillo moderno** con plantas; Momo (cazadora roja y blanca), Okarun y un chico pelirrojo de espaldas | 1920×1080 | ⚠️ la parte lo llama «interior con luz de linterna»; se ve de día |
| 16 | Aira con el bolso en el pasillo | 1920×4247 | = hoja 1 n.º 3 |
| 17 | el gato de Turbo Granny | 1125×1528 | = hoja 1 n.º 40 |
| 18-22 | miniaturas de Sketchfab | **64×36** | ❌ no sirven: abrir los enlaces de §4 |
| 23-24 | **figura TENITOL de FuRyu: Okarun transformado**, agachado sobre escombros, dos vistas | 900×1200 | pose 3D. ⚠️ **La 24 no es Momo**: la parte la llamó «TENITOL Momo» |
| 25 | figura 1/7 de **Seiko** con bate (FuRyu F:NEX) | 750×1000 | pose de Seiko |
| 26 | **el gato de Turbo Granny a tamaño real, vinilo** (FuRyu F:NEX) | 750×1000 | **volumen real para Blender** (§27 B) |
| 27 | peluche de Turbo Granny, cara gritando | 1500×2000 | expresión |
| 28 | Noodle Stopper: el gato tumbado, **ojos cerrados y una lágrima** | 2550×2550 | ⚠️ única «tristeza» de Turbo Granny, y es un producto (§8.6) |

### 3.2 Fuera de las hojas

- **Portada y banner** de [AniList](https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx171018-60q1B6GK2Ghb.jpg): 460×650 y 1900×400 ✅.
- **Ilustración de la 1.ª encuesta** de Tatsu con los 10 más votados:
  [2560×1652](https://static.wikia.nocookie.net/dandadan/images/0/01/Results_First_popularity_poll_of_the_DandaDan_characters.png) ✅ (§9).
- **Retratos de AniList** (230×345, medidos): Momo, Aira, Okarun, Seiko,
  Jiji, Turbo Granny, Serpo y 8 secundarios más (`referencias.json`).
- 25 tomos del manga catalogados en la wiki; 8 volúmenes de Blu-ray.
- ⚠️ **No hay artbook** oficial (buscado en inglés y japonés, 画集
  ダンダダン). Lo más parecido es el *Dandadan Daizukan* (databook,
  agosto 2025, §21).

---

## 4 · Fan art y 3D, sólo como referencia

### 4.1 Modelos 3D con licencia libre (Sketchfab) ✅

Buscados con «Dandadan» (con «DAN DA DAN» salían muebles franceses e
instrumentos vietnamitas). Todos **CC Attribution**: se cita al autor de
Sketchfab. Son de fans, no oficiales: para pose y volumen.

| Modelo | Autor | ♥ | Enlace |
|---|---|---|---|
| Momo Ayase + DL | higuys920 | 261 | [sketchfab](https://sketchfab.com/3d-models/none-6ac6c3476a1f4b8da1c7de7e98a7c83c) |
| Okarun con Turbo Granny + DL | higuys920 | 116 | [sketchfab](https://sketchfab.com/3d-models/none-994932a4c4464439983f936d1cf5784e) |
| Aira (Acrobatic Silky) DL | higuys920 | 35 | [sketchfab](https://sketchfab.com/3d-models/none-e59d90ffd0c0494eadc8e6a1a9a702e0) |
| okarun dandadan (194.579 caras, CC-BY 4.0) | bakhats110 | 11 | [sketchfab](https://sketchfab.com/3d-models/okarun-dandadan-8452d63687324ec58b595dcc2b829fcc) |
| Turbo Granny y Okarun (*Arena of Valor*) | carinhaqualquer123 | 21 | [sketchfab](https://sketchfab.com/3d-models/none-f2702def0cf74dd69ff1a4b05942acf9) |
| Serpo Dandadan | elmachosexy | 2 | [sketchfab](https://sketchfab.com/3d-models/none-086349c159e34bcf9d911887fe755c73) ⚠️ la parte de imagen lo llama «planeta o nave», la de texto «el alien»: abrirlo antes |
| TURBO GRANY (el gato) | Turbo-Granny-Cat | 1 | [sketchfab](https://sketchfab.com/3d-models/none-c2c8305c6341481ca18fcf33087684a3) ⚠️ una fuente |

Para el gato de Turbo Granny, **mejor la figura oficial a tamaño real**
(hoja 3 n.º 26) que cualquier modelo de fan.

### 4.2 Fotos libres (Openverse) ⚠️ sin mirar

- [Tienda Muse Land de Taipéi con la camiseta blanca de Dan Da Dan](https://upload.wikimedia.org/wikipedia/commons/e/e7/Taipei_City_Mall_Store%2C_Muse_Land_and_Dan_Da_Dan_white_T-shirt_20260425.jpg),
  5336×4002, Solomon203, **CC BY-SA 4.0**.
- [Pier-2 y Dan Da Dan](https://upload.wikimedia.org/wikipedia/commons/a/a0/Pier-2_and_Dan_Da_Dan-20250403.jpg),
  4080×3072, Allervous, **CC BY-SA 4.0**.
- El resto de Openverse (un bar llamado «Dan da dan», catedrales…) no es
  de la serie.

### 4.3 Fan art (sólo para mirar, nunca para pegar)

Mejor valorados en [Safebooru](https://safebooru.org/index.php?page=post&s=list&tags=dandadan), con su autor:

- **Momo y Okarun** haciendo ejercicio, 3085×4096, de
  [Yuqi_non](https://twitter.com/Yuqi_non/status/1963251057158393937).
- **Okarun**, 3000×4444, de [Pixiv](https://i.pximg.net/img-original/img/2025/03/03/13/24/18/127820524_p0.png).
- **Turbo Granny**, 3867×2972, de [Yuqi_non](https://twitter.com/Yuqi_non/status/1952403415667183758);
  1688×2048 de [syooooyoooo](https://twitter.com/syooooyoooo/status/1944190745105018906).
- **Aira**, 2894×4093, de [toniai_29Q](https://twitter.com/toniai_29Q/status/1871212606943576335).
- **Momo**, 2520×2608, de [Pluvion_](https://twitter.com/Pluvion_/status/1857167125070393504);
  2344×3001 de [masoq095](https://twitter.com/masoq095/status/1849907033379639673).
- ⚠️ El recolector repitió el fan art de Momo bajo la etiqueta de
  Okarun. La etiqueta buena es **`takakura_ken_(dandadan)`** (lo
  corrigió la parte de imagen).
- En Reddit: «[Dandadan in Iconic Movie Posters](https://www.reddit.com/r/Dandadan/comments/1haypgj/dandadan_in_iconic_movie_posters_art_by_me/)» (2067 votos) e
  «[I did Okarun in that iconic Sonic pose](https://www.reddit.com/r/Dandadan/comments/1pc4txi/i_did_okarun_in_that_iconic_sonic_pose/)» (205).

### 4.4 Cómo etiqueta el fandom a cada uno ([Danbooru](https://danbooru.donmai.us/posts?tags=dandadan)) ✅

- **Momo**: `brown_hair`, `earrings`, `black_choker`, `crossed_bangs`,
  `pink_sweater`, `red_bowtie`, `white_shirt`, `blue_skirt`,
  `school_uniform`.
- **Okarun**: `glasses`, `round_eyewear`, `gakuran`, `black_hair`,
  `brown_eyes`; transformado: `white_hair`, `red_eyes`, `mouth_mask`,
  `facial_mark`, `torn_clothes`, `black_nails`.
- **Aira**: `pink_hair`, `short_hair`, `pink_eyes`, `hair_between_eyes`,
  `kami_high_school_uniform`, `red_bowtie`, `pleated_skirt`.
- ⚠️ Las etiquetas de `turbo_granny_(dandadan)` salen mezcladas con las
  de Momo y Okarun (gafas, pelo castaño): casi siempre la dibujan con
  ellos. No sirven para describirla sola.

---

## 5 · Sitios, luz, paleta y texturas reales

### 5.1 Medidos en fotogramas del anime (`estilo.py`) ✅

| Sitio | Dónde | Colores dominantes | Saturación | Luz |
|---|---|---|---|---|
| Túnel de Turbo Granny, linterna | ep. 1, 10:55 | dorado **#F5C752** (42 %), negro **#130B06** (25 %), naranja **#E4A73D** | alta | un punto de luz muy cálido contra negro total |
| Dentro del OVNI, despertar de Momo | ep. 1, 13:20 | cian **#94EDF4**, azul **#1696EB**, **#5BD5EA** | brillo 87 % | fría y saturada, la más luminosa |
| Transformación de Okarun | ep. 1, 14:50 | cian claro **#BFF8F9**, carmín **#C02343**, violeta **#362353** | 49 % | frío y rojo, «enfermizo» |
| Pasillo de Kami High, tarde | ep. 5, 11:55 | marrón **#24211F**, **#564646**, piel **#D4A98D** | 25 % | normal, apagada |
| Casa de Seiko, tatami, tarde | ep. 5, 15:00 | rosado-marrón **#584446**, **#8C6E68**, crema **#EAD4CD**; línea **#7C655E** | 27 % | cálida, más línea visible |
| Casa maldita, «Evil Eye» | tráiler, 0:21-0:41 | violeta **#8B5CF6** y rojo sangre sobre negro | — | ⚠️ a ojo, no medido (vídeo de 512×288) |

**La regla** ✅ (5 fotogramas de 2 capítulos): lo cotidiano es cálido y
poco saturado (25-27 %); lo sobrenatural, frío o mixto y muy saturado
(49-87 %). Una lámina «normal» va apagada; una «paranormal», encendida.

### 5.2 Fotogramas de la wiki en 1920×1080 ✅ (sin minuto)

- [Fachada de Kami High](https://static.wikia.nocookie.net/dandadan/images/7/72/High_School_%28Anime%29.png):
  edificio moderno de varios pisos, muro de ladrillo, reja verde
  azulada, cielo despejado.
- [Daija Town](https://static.wikia.nocookie.net/dandadan/images/f/fb/Daija_Town_%28Anime%29.png):
  gran escalinata de piedra, casas tradicionales y modernas, montañas
  verdes, de día.
- [Casa japonesa antigua en sepia](https://static.wikia.nocookie.net/dandadan/images/4/47/Cursed_House_Facade_1.png)
  y [pasillo moderno](https://static.wikia.nocookie.net/dandadan/images/a/a0/Cursed_House_interior_2.png),
  archivados como «Casa Maldita» (ver §3.1, n.º 14 y 15).
- Nombres de sitios sin imagen mirada ⚠️: Izumo Taisha, Danmara,
  Futakori Barbershop, Abandoned Warehouse.

### 5.3 Sitios reales detrás de la serie ✅ ([fun-japan.jp](https://www.fun-japan.jp/en/articles/14048))

- **Kamigoe** está basada en **Kawagoe** (Saitama).
- El instituto, en el **Takushoku University First** (Musashimurayama).
- El túnel de Turbo Granny, en el **túnel de Hata**.
- El balneario «Orochi Onsen», en **Ikaho** (Gunma).

### 5.4 Texturas reales equivalentes ⚠️

**Las partes no buscaron texturas reales** (papel, tatami, madera). Lo
que hace falta para los conceptos de §27, por buscar en ambientCG (CC0):
papel satinado de revista, **tatami**, madera de mesa baja, papel
*washi* para el talismán, cerámica blanca brillante para el gato.
El director de secuencia del opening pide lo contrario del filtro:
**recortes y lápiz de verdad** (§19).

---

## 6 · Tipografía: una letra para cada uso

### 6.1 El logo ✅

- **ダンダダン no es una fuente: es rotulado a mano.** Katakana enorme en
  **rojo sangre**, con **cortes diagonales** en cada trazo, como
  rasgado. Visto en la [portadilla del capítulo 1](https://static.wikia.nocookie.net/dandadan/images/6/66/Chapter_1.png)
  (1481×1079), sobre una foto industrial gris de tuberías.
- Logo del anime: [1320×975](https://static.wikia.nocookie.net/dandadan/images/3/3d/Dandadan_Logo_%28Anime%29.png),
  rojo, anguloso, con grano. Diseño del logo del anime: **Youhei
  Okashita** ([AniList, staff](https://anilist.co/anime/171018/staff)).
- En el foro de dafont dicen que se parece a **Babarun** (de pago), pero
  que «probablemente es rotulado a mano»
  ([hilo 1](https://www.dafont.com/forum/read/573074/dandadan),
  [hilo 2](https://www.dafont.com/forum/read/583537/dandadan-looking-font)) ✅.
- En el logo inglés del tomo 1 (hoja 3 n.º 13) pone «DAN DA DAN» en
  rojo, en diagonal.

### 6.2 La letra libre para cada uso ✅ (tildes, ñ, ¿ y ¡ comprobados con fontTools)

| Uso | Letra libre | ¿Trae á é í ó ú ñ ¿ ¡? | Nota |
|---|---|---|---|
| Logo o título | **[Rubik Glitch](https://fonts.google.com/specimen/Rubik+Glitch)** (OFL) | sí | la más parecida a los cortes diagonales, comparada renderizando «DANDADAN» contra Bungee, Rubik Distressed y Chokokutai |
| Logo, alternativa | Rubik Distressed (OFL) | sí | textura castigada en vez de cortes |
| Título secundario, cartel de tienda | Chokokutai (OFL) | sí | más caligráfica |
| Globo normal | **Anime Ace 2.0 BB** ([dafont](https://www.dafont.com/anime-ace-bb.font), gratis no comercial) | **tildes y ñ sí; ¿ y ¡ NO** en sus 3 estilos | copiar ¿ y ¡ de Bangers, o usar Kalam |
| Grito (globo dentado) | **[Bangers](https://fonts.google.com/specimen/Bangers)** (OFL) | sí | letras infladas y desiguales |
| Pensamiento | **[Caveat](https://fonts.google.com/specimen/Caveat)** (OFL) | sí | cursiva fina |
| Onomatopeya | **[Rampart One](https://fonts.google.com/specimen/Rampart+One)** (OFL) | sí | Dela Gothic One ya la usan One Piece y JoJo: ésta distingue a Dandadan |
| Cartel del mundo (tiendas, señales) | **[Zen Kaku Gothic New](https://fonts.google.com/specimen/Zen+Kaku+Gothic+New)** o M PLUS 1p (OFL) | sí | gótica japonesa de señalética |
| Interfaz de juego | [Rajdhani](https://fonts.google.com/specimen/Rajdhani) (OFL) | sí | no hay juego propio: sólo si hace falta una pantalla |
| Subtítulos y créditos | ⚠️ Noto Sans JP | — | Netflix y Crunchyroll usan su letra de plataforma; los créditos del tráiler son una sans fina blanca sobre negro (de memoria de la parte, sin comprobar) |

> [!warning] Anime Ace 2.0 BB no trae ¿ ni ¡
> Comprobado por la parte de texto abriendo los 3 archivos con fontTools.
> Es la letra de globo que usan casi todas las biblias. En español hay
> que añadir esos dos signos a mano. (Es el mismo problema que
> Haikyuu en `DECISIONES.md`.)

### 6.3 Lo que no se encontró ⚠️

- La letra del opening y del ending (DeviantArt y Behance dieron 403).
- Una onomatopeya del manga vista de cerca: las páginas de la wiki
  vienen sin rotular. Se sabe que el título ダンダダン es una
  onomatopeya de redoble (§11).

---

## 7 · Cómo hablan en pantalla: el globo y el color

Dandadan **no tiene caja de diálogo propia** (no hay juego, §13). Su
lenguaje propio son tres cosas: el globo del manga, los puntos de trama
para lo sobrenatural y el **color por bando** del anime.

### 7.1 El globo del manga ✅ (visto)

- **Óvalo limpio, trazo fino, colita pequeña y puntiaguda** hacia quien
  habla. Sin relleno de color ni sombra
  ([«Turbo Granny's farewell»](https://static.wikia.nocookie.net/dandadan/images/6/62/Turbo_Granny%27s_farewell.png),
  1013×525; hoja 2 n.º 70 y 73).
- Las páginas de acción: **trama de puntos muy densa** en la ropa de los
  yokai, **pinceladas negras gruesas** para el movimiento, **esquirlas**
  alrededor del golpe
  ([«Acrobatic Silky attacks Momo»](https://static.wikia.nocookie.net/dandadan/images/b/b3/Acrobatic_Silky_attacks_Momo.png), 1356×1048).
- **Lo sobrenatural que se deshace** no lleva línea: una **nube de
  puntos de trama** que se dispersa como purpurina sobre negro
  ([«Acrobatic Silky goes to heaven»](https://static.wikia.nocookie.net/dandadan/images/e/eb/Acrobatic_Silky_goes_to_heaven.png),
  2879×2104; hoja 2 n.º 84).
- ⚠️ No se encontró un **globo de pensamiento** propio. En vez de la
  nube de burbujitas, usar esa **nube de puntos de trama**: es el
  recurso que la serie ya usa para lo que no se toca.

### 7.2 El color por bando del anime ✅ (lo dice el director)

El director **Fūga Yamashiro** da a cada bando su color, para que se
sepa «de qué mundo es» cada cosa sin decir nada
([entrevista en Mantan-Web](https://en.mantan-web.jp/e_article/20241017dog00m200033000c.html),
confirmado por las [notas de producción de Sakuga Blog](https://blog.sakugabooru.com/2024/10/03/dandadan-production-notes-01/)):

| Bando | Color | Medido en |
|---|---|---|
| Turbo Granny y los yokai | **rojo** (guiño a Ultraman: Okarun transformado se queda «rojo» como un héroe *tokusatsu*) | carmín **#C02343** (ep. 1, 14:50) |
| Extraterrestres Serpo | **azul frío** | azul **#1696EB** (ep. 1, 13:20) |
| Poderes psíquicos | **turquesa** | cian **#94EDF4**, **#5BD5EA** (ep. 1, 13:20) |

- Hasta la luna avisa: la **luna amarilla** es real; la **luna azul
  pálida** es un OVNI disfrazado (Mantan-Web).
- Los **extraterrestres son 3D** (fríos, geométricos) y los **yokai son
  2D a mano** (cálidos, orgánicos)
  ([ScreenRant](https://screenrant.com/dandadan-anime-episode-2-director-unique-animation-color-ghost-alien/)) ✅.
- Los *color scripts* los hace **Sophie Li** (Sakuga Blog).

### 7.3 Los títulos hablan como Momo ✅

Los títulos de los capítulos terminan con la muletilla de Momo,
**じゃん(よ)** («¿no?», «¿a que sí?»): «それって恋のはじまりじゃんよ»
(ep. 1), «ババアとババアが激突じゃんか» (ep. 3), «タマはどこじゃんよ»
(ep. 5), «なんかモヤモヤするじゃんよ» (ep. 8)
([Internet Archive](https://archive.org/details/english-sub-s-01.-e-03)).
Un cartel de lámina puede terminar igual en español: «…¿a poco no?».

### 7.4 La receta para la lámina

1. **Globo**: óvalo blanco, trazo negro fino (más fino que la línea
   del personaje), colita corta y puntiaguda. Letra: Anime Ace 2.0 BB con ¿ y ¡
   de Bangers.
2. **Borde o acento de color según quién habla**: rojo **#C02343** si
   habla Turbo Granny o un yokai; azul **#1696EB** si habla un Serpo;
   turquesa **#94EDF4** cuando Momo usa su poder. Okarun y Momo normales
   van en negro.
3. **Grito**: globo dentado con Bangers, rojo si es de Turbo Granny.
4. **Pensamiento o algo sobrenatural**: sin globo; texto en Caveat sobre
   una **nube de puntos de trama** blancos sobre negro.
5. **Rótulo de título**: Rubik Glitch en rojo, con los cortes en
   diagonal.

### 7.5 Qué NO hacer

- ❌ Una burbuja blanca redonda con sombra y colita curva de cómic
  genérico.
- ❌ Inventar «la interfaz del juego de Dandadan»: no existe.
- ❌ Cambiar el color de un bando: Turbo Granny en azul o los Serpo en
  rojo es un error que el director evita a propósito.

---
