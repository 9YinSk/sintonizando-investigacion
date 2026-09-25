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

## 8 · Los personajes: qué transmiten, su cara y sus dinámicas

Fuentes: la sección *Personality* de cada ficha de la
[wiki en inglés](https://dandadan.fandom.com/wiki/Momo_Ayase) (leída
entera por la parte de voz), el *Dandadan Daizukan* que cita la wiki,
[AniList](https://anilist.co/character/222594) y los fotogramas con
minuto de las partes. Las frases entre comillas son del subtítulo
inglés o de la transcripción japonesa, **no del doblaje latino** (ése,
en §10).

### 8.1 Momo Ayase — la que no deja pasar una injusticia

- **Carácter.** Audaz, segura, brusca. Casi nada la intimida. Pierde los
  estribos rápido, sobre todo si la desprecian o si sus amigos hacen
  tonterías; reacciona con violencia cómica y **se arrepiente si se
  pasa**. A la vez es cálida y alegre: **no puede mirar a otro lado**
  ante una injusticia. Por eso defiende a Okarun sin conocerlo (ep. 1,
  16:00) ✅.
- **Historia.** Vive con su abuela **Seiko**, médium, que la crió sola:
  «no tengo padres» (ep. 1, 8:00-10:00). De niña se avergonzó de los
  rituales de la abuela cuando el chico que le gustaba se burló; le dijo
  «falsa médium» y dejó de hablarle hasta hace poco ✅ (ep. 1, 9:00 y
  17:00).
- **Qué le importa, qué teme.** Su abuela y sus amigos. Que la llamen
  tonta o «de pueblo». Su primer amor (Jiji) la dejó desconfiada del
  romance ✅.
- **Qué transmite.** Fuerza con cariño. Da gusto verla ponerse delante
  de alguien. Es la gyaru que protege al raro de la clase.
- **Su arco.** No cree en extraterrestres → ve un OVNI, **despierta su
  poder** y se reconcilia con el legado de la abuela («gracias, abuela»,
  ep. 1, 18:00) → en el último arco pierde la memoria de todo lo vivido
  con Okarun (§26).
- **Cómo habla.** Dice **うち** («yo», de chica de barrio), マジ,
  超ウケる («qué risa»), うるせーな («cállate») y la muletilla **じゃん**
  (§7.3). Corta, directa, insulta sin pensarlo. En Crunchyroll, con
  modismos mexicanos; en Netflix, más neutra (§10).
- **Cómo se ríe.** Cabeza hacia atrás, ojos cerrados, mano en el pelo
  (ep. 1, 21:54); o **llora de risa** con la boca muy abierta (ep. 5,
  15:12).
- **Cómo se enfada.** Grita con la boca enorme (ep. 1, 4:45), roja de
  furia (ep. 5, 9:00).
- **Cómo explica.** Con una historia personal y sin rodeos: «mi abuela
  me crió sola, por eso creo en fantasmas» (ep. 1, 10:00).
- **Cómo saluda.** ⚠️ No está en las partes.
- **Cuerpo.** Manos en los bolsillos al caminar, hombros relajados;
  cuando pelea, puños cerrados y el cuerpo hacia delante (§15.1).
- **Su técnica.** La de la abuela: «**mete fuerza bajo el ombligo y
  saca el *ki* por la coronilla**» (ep. 1, 17:00). Es, casi palabra por
  palabra, el apoyo de un cantante.

### 8.2 Okarun (Ken Takakura) — el raro que se vuelve valiente

- **Carácter.** Se describe a sí mismo como torpe con la gente.
  Obsesionado con lo paranormal (OVNIs, críptidos) **desde niño, porque
  no tenía amigos**: intentaba contactar con extraterrestres para tener
  alguno. Complejo de inferioridad que no se le quita ni siendo amigo de
  Momo ✅ (wiki).
- **Historia.** Sufrió acoso. De niño llamaba al cielo con su revista
  en la mano: «**No matter how much I called for you, you never showed
  up!**» (ep. 1, 15:47). Momo es la primera que lo defiende (16:00).
- **Qué le importa, qué teme.** No encajar; que Momo prefiera a Jiji;
  **perder el control** de la maldición («Please help! I can't control
  myself!», ep. 1, 14:39).
- **Qué transmite.** Ternura. El que nunca tuvo a nadie y, cuando lo
  tiene, se juega todo: «**If it's for her sake, I'll even become a
  monster!**» (ep. 1, 16:12).
- **Su arco.** Maldito por Turbo Granny → gana su velocidad → hace
  amigos y se entrena (se le marcan los músculos) (§26).
- **Por qué «Okarun».** Se llama como el actor que idolatra Momo, **Ken
  Takakura**, y ella se niega a llamarlo así ([AniList](https://anilist.co/character/222593)) ✅.
  Encima suelta la frase más famosa del actor, «**自分、不器用なんで**»
  («soy un tipo torpe»), y Momo se sobresalta (ep. 1, 21:00-21:30).
- **Cómo habla.** Dice **自分** («yo», tieso, a la antigua) y trata a
  Momo de usted («Ayase-san»). **Tartamudea** cuando se pone nervioso
  («あ、あ、あやせさ», «倒ぼぼぼ倒しましたよね», ep. 5, 13:00-14:00).
  Pide perdón a cada rato («すいません», ep. 1, 20:00-21:00). Es
  **pedante**: «No es OVNI, es UAP» (ep. 1, 4:00). **Por teléfono
  habla con soltura** (ep. 1, 10:00). Una frase suya que lo resume:
  «¿Hace falta una razón para que te guste algo?» (好きなものに理由が
  必要なんですか?, ep. 1, 10:00).
- **Cuerpo.** **Dos dedos en el puente de los lentes** (tráiler, 0:16;
  ep. 5, 14:18-14:50; hoja 2 n.º 86). Se rasca la nuca cuando se
  avergüenza (ep. 1, 21:29). Encogido de hombros.
- ⚠️ La parte de voz dice que grita «¡Nyoron!» al transformarse. **No
  lo confirma ninguna fuente**, y «Nyoro~n» sale en la página de
  mantenimiento de AnimeThemes: probablemente es una confusión. No
  usarlo.

### 8.3 Turbo Granny (Turbo Babaa; «Turbo Abuela» en Netflix, «Turbo Ruca» en Crunchyroll)

- **Carácter.** Cruel, sádica y «**extremadamente malhablada**» (texto
  literal de la wiki). Vulgar: le ofrece a Okarun sus pechos a cambio
  de sus «joyas de la familia». **Orgullosa de su velocidad**: no
  soporta que la subestimen. **Hace trampa** si hace falta: en el juego
  de las traes contó mal a propósito ✅ (wiki).
- **Su lado oculto.** Según Seiko, solía ir a **consolar a los espíritus
  de niñas muertas trágicamente**; por eso se fundió con el cangrejo
  espíritu del túnel de Shono ✅ (wiki).
- **Historia y arco.** Leyenda urbana real: la vieja que persigue coches
  en los túneles ([fun-japan.jp](https://www.fun-japan.jp/en/articles/14048)) ✅.
  Villana del primer arco → le roba las «bolas» a Okarun y lo posee →
  la **sellan en un gato de la suerte** (maneki-neko) → vive en casa de
  Seiko, gruñendo, como aliada a regañadientes (§26).
- **Qué transmite.** Peligro y carcajada a la vez. El fandom la quiere
  **por grosera**, no por tierna (§14).
- **Cómo habla.** Dice **わし** («yo», de viejo), llama a Okarun
  **こぞう** («mocoso»), habla golpeado: «si lo quieres de vuelta, **ven
  al túnel**» (ep. 1, 19:00). Su dicho favorito, según el *Daizukan*:
  «**shiiit**». En el doblaje de Crunchyroll, Magda Giner le pone **el
  tono de Zim** (*Invasor Zim*) ✅ (Doblaje Wiki).
- **Cuerpo.** Encorvada, a cuatro patas cuando corre, brazos en alto con
  garras cuando ataca (§15.3). En el gato: cara de fastidio (hoja 1
  n.º 40).
- **Cuando posee a alguien**, su víctima se vuelve un reflejo de ella
  con una boca enorme ([AniList](https://anilist.co/character/239956)).
  Por eso su «cara de malicia» del ep. 1 (14:27-14:46) está en el
  **cuerpo de Okarun**: «Lemme gobble that weenie!» (14:46) es ella
  hablando por él.

### 8.4 Aira Shiratori — la reina del instituto que no es lo que parece

- **Carácter.** Por fuera, dulce, inocente y algo despistada. Por
  dentro, **vanidosa, arrogante e insensible** con quien no es de su
  círculo. Usa su belleza para burlarse de los chicos. Cuando pierde la
  popularidad se muestra tal cual: **orgullosa, seria, un poco
  mandona** (se autoproclama líder del grupo). Pero capaz de **empatía
  de verdad**: ayuda a Acrobatic Silky a alcanzar el nirvana, llora con
  la historia de Bamora, se derrite con lo tierno. Enamorada de Okarun
  sin disimular; celosa ✅ (wiki, texto entero).
- **Por qué es así.** Perdió a su madre de niña. Su padre le pidió que
  fuera una mujer de la que su madre «estuviera orgullosa», y ella lo
  entendió mal: ser popular a toda costa ✅ (wiki).
- **Qué le importa.** Su reputación; luego, su grupo. Se cree **«la
  elegida»** para proteger el mundo del mal, y decide que Momo es un
  demonio ([AniList](https://anilist.co/character/245466)) ✅.
- **Qué transmite.** Primero rabia, luego ternura. El ep. 7 hace llorar
  (§22).
- **Cómo habla.** Dos voces. En público: «すみません», «痛くなかった
  ですか» («¿no te hice daño?»), «本当にごめんなさい» (ep. 5, 11:00-12:00).
  En privado: «ese otaku puso una cara de tonto», «seguro que ya se
  enamoró de mí», «**es divertido hacer que los perdedores se enamoren
  de ti**» (カスを好きにさせるの), «le estoy regalando un sueño» (ep. 5,
  12:00-13:00). Y «**I mean, I'm all too pretty!**» (ep. 6, 7:00). Su
  lema: «**lo lindo es justicia**» (*Daizukan*).
- **Cuerpo.** En público, inclinada y con las manos juntas; en privado,
  de espaldas, haciendo la V con sus amigas (ep. 5, 12:53) (§15.4).

### 8.5 Seiko Ayase — la abuela médium (secundaria muy querida)

6.ª en la encuesta oficial y 4.ª en AniList (2200 favoritos) (§9).

- Pelo blanco recogido con una tela blanca, **lentes rojos**, camiseta
  de tirantes; en el key visual, **bate de béisbol** y chaqueta bordada
  (hoja 3 n.º 6 y 25). Aparenta mucha menos edad y es muy guapa
  ([AniList](https://anilist.co/character/234824)).
- En el ep. 5 (15:17-17:23): examina a Okarun, fuma (16:09), le pega
  con un abanico de papel, parodia al profesor Kinpachi («el kanji de
  *persona* son dos palos que se apoyan», 16:24) y da órdenes:
  «**Momo! Bring me a doll, I don't care what!**» (15:50), «The instant
  the aura changes colors, pull out that aura» (16:45).
- Su alias de médium en el doblaje: «**Santa Dodoria**» (Netflix) o
  «**Dodoria Santa**» (Crunchyroll), ep. 3 (Doblaje Wiki) ✅.

### 8.6 Su cara en cada emoción ⚠️ (13 de 20 con fotograma y minuto)

| | Alegría | Rabia | Tristeza | Miedo | Vergüenza |
|---|---|---|---|---|---|
| **Momo** | ✅ risa, cabeza atrás (ep. 1, 21:54); llora de risa (ep. 5, 15:12) | ✅ ceño y mirada fija (ep. 1, 2:00); boca enorme (4:45); roja (ep. 5, 9:00) | ✅ lágrimas grandes (ep. 7, 18:45) | ❌ **falta** | ✅ **rubor, mano en la cabeza, mirada abajo**: «I'm not embarrassed about being friendly to you» (ep. 5, 14:26); sonrisa ruborizada (14:43) |
| **Okarun** | ⚠️ «I'm very happy that I could make amends with you», levantándose los lentes (ep. 5, 14:34); el brillo de los lentes le tapa los ojos | ✅ mirada fija leyendo su revista (ep. 1, 4:15); puño cerrado (7:45) | ✅ **ojos llorosos tras los lentes**: «She actually stood up for me» (ep. 1, 16:02) | ✅ boca abierta, ojos como platos (ep. 1, 4:30); pálido con lágrimas (19:15) | ✅ cabeza baja (ep. 1, 21:30); «So please don't be disappointed with me» (ep. 3, 14:15) |
| **Turbo Granny** | ❌ falta | ✅ ojos amarillos en la oscuridad (ep. 1, 10:55); forma yokai atacando (18:41-18:59); su cara en Okarun poseído (14:46) | ❌ falta (sólo un producto: el Noodle Stopper con una lágrima, hoja 3 n.º 28) | ❌ falta | ❌ falta |
| **Aira** | ✅ sonrisa de suficiencia (ep. 6, 7:00); sonrisa halagadora (ep. 5, 12:15) | ✅ perfil serio, ceño (ep. 6, 6:30-6:45) | ❌ **falta** despierta | ✅ mirada tensa hacia atrás (ep. 6, 13:15); sorprendida (ep. 5, 13:36) | ❌ **falta** |

**Lo que dice la parte de voz** (agotó sus 2 tandas):

- Miró completos los episodios **1 a 8** (fotogramas cada 15 s) y el
  tráiler, más 15 fotogramas sueltos del ep. 3.
- **Vergüenza de Momo**: no la encontró en los eps. 1-7. **El redactor
  la vio** en la hoja de la parte de vídeo (ep. 5, n.º 243, 14:26):
  ese hueco queda cerrado.
- **Aira despierta, tristeza y vergüenza**: en el ep. 7 sólo sale
  inconsciente (0:30); **el ep. 8 no tiene a Aira**; los eps. 9-11 no
  se miraron. La wiki dice que se sonroja a menudo con Okarun y que
  llora con la historia de Bamora, **sin minuto**.
- **Turbo Granny**: en los eps. 1, 5-6 y 7 sólo sale amenazando. Su
  *Daizukan* tampoco describe esas caras. Su única cara segura es la de
  amenaza y burla.
- **Miedo de Momo**: ninguna parte lo tiene (el redactor lo nota; no
  está en la lista de la parte de voz).

**Pistas para la próxima tanda** (de `episodios.md`, sin mirar la cara):
Momo dice «perdón, abuela, entonces sólo me daba **vergüenza**» (ep. 1,
~17:10); Aira sale en la niebla con la niña en el ep. 7 (hoja 1 n.º 22,
«Episode 7.png», sin minuto); probar los eps. 9, 10 y 11 para Aira
([ep. 9](https://archive.org/details/s-01.-e-09_202411),
[ep. 10](https://archive.org/details/s-01.-e-10_202412),
[ep. 11](https://archive.org/details/s-01.-e-11_202412)). En el ep. 10
Turbo Ruca discute con Okarun mientras comen (Doblaje Wiki): quizá haya
más caras del gato.

### 8.7 Los secundarios más queridos (sólo ficha)

| Personaje | Encuesta oficial | AniList | Qué es | Voces latinas (Netflix / Crunchyroll) |
|---|---|---|---|---|
| **Jiji** (Jin Enjōji) | 4.º | 1782 fav. | amigo de la infancia y primer amor de Momo; hiperactivo, gestos dramáticos, **muletillas raras al final de las frases**, futbolero; noble debajo ([AniList](https://anilist.co/character/258506)) | Dalí González / Marc Winslow |
| **Seiko Ayase** | 6.ª | 2200 fav. | §8.5 | Karla Falcón / Xóchitl Ugarte |
| Zuma, Bamora, Rokuro Serpo, Kinta | 7.º-10.º | — | de la T2 en adelante | — |
| Penny Chinkosu (Dover Demon) | — | 242 fav. | trabaja para los Serpo para pagar las transfusiones de su hijo Chiquitita | Irwin Daayán (Netflix) |
| Acrobatic Silky | — | 114 fav. | mujer alta, pelo negro sedoso, sombrero y vestido rojos, sonrisa de pintalabios permanente | Rosalba Sotelo |

En Reddit, un hilo de 836 votos dice que **Jiji es su favorito**
([r/Dandadan](https://www.reddit.com/r/Dandadan/comments/1mm0tss/after_completing_the_recent_episode_jiji_is_by/)).

### 8.8 Dinámicas para láminas en grupo ✅

| Pareja | Cómo es | Escena |
|---|---|---|
| Momo y Okarun | discuten (fantasmas contra extraterrestres), se protegen, se piden perdón con vergüenza a la vez; **él la hace reír**, ella lo saca de su cascarón | ep. 1, 4:00-7:00; ep. 5, 14:11-15:12 |
| Momo y Aira | rivales («es un demonio») que acaban amigas; se insultan | ep. 6, 6:45 |
| Okarun y Aira | ella está enamorada y celosa; él no se entera | ep. 5, 11:49 |
| Okarun y Turbo Granny | ella lo posee; luego discuten comiendo | ep. 1, 14:27; ep. 10 (Doblaje Wiki) |
| Momo y Seiko | la abuela que la crió sola; Momo se avergonzó de ella y le pide perdón | ep. 1, 17:00-18:00 |
| Seiko y Okarun | la abuela lo examina y le pega; él aguanta en *seiza* | ep. 5, 15:17-16:45 |
| Okarun y Jiji | rivales por Momo sin decirlo; cantan juntos los temas de *Slam Dunk* | ep. 12 (§11) |

---

## 9 · ¿Quién es el más querido?

### 9.1 Los números

| Fuente | 1.º | 2.º | 3.º | 4.º | 5.º | Otros |
|---|---|---|---|---|---|---|
| **1.ª encuesta oficial** (Shueisha/Jump+, 16-dic-2024) ✅ | **Okarun** 38.699 | Momo 25.763 | **Turbo Granny** 22.920 | Jiji | Aira 14.271 | 6.ª Seiko, 7.º Zuma, 8.º Bamora, 9.º Rokuro Serpo, 10.º Kinta |
| Favoritos del autor (tuit de VIZ) ✅ | Momo | Okarun | Aira | — | — | Tatsu esperaba que ganara «el cangrejo de Hokkaido» |
| [AniList](https://anilist.co/anime/171018) (fandom internacional) ✅ | **Momo** 7357 | Aira 6137 | Okarun 4709 | Seiko 2200 | Jiji 1782 | Turbo Granny 871 (6.ª) |
| [Danbooru](https://danbooru.donmai.us/posts?tags=dandadan) (cuánto se dibuja) ✅ | **Momo** 4302 | Okarun 3220 (+1196 transformado) | Turbo Granny 1018 | Seiko 879 | Aira 824 (+159 transformada) | Jiji 553 |

Fuentes de la encuesta: [wiki, Popularity Polls](https://dandadan.fandom.com/wiki/Popularity_Polls),
[Game Rant](https://www.gamerant.com/dandadan-reveals-results-of-popularity-poll/) y
[Oricon](https://us.oricon-group.com/news/2823/). Favoritos del autor:
[tuit de VIZ Media](https://x.com/VIZMedia/status/1843003291971846296).

En Reddit ([r/Dandadan](https://www.reddit.com/r/Dandadan/)): «Unpopular
Opinion: Aira's the Most Beautiful Female Character» (2021 votos),
«Aira and Momo carry every time when it comes to fights» (1218), y el
hilo de Jiji (836) ✅.

### 9.2 Qué significa para la lámina

- **Los cuatro del encargo están en el top 5 oficial.** No hay un
  secundario escondido que gane al protagonista: Okarun gana en Japón y
  Momo fuera.
- **Turbo Granny es la secundaria más votada** (3.ª, por delante de
  Aira y Jiji). Merece su propia lámina (§27 B).
- **Aira se vota más de lo que se dibuja**: 2.ª en AniList y 5.ª en la
  encuesta, pero la última de los cuatro en Danbooru. El fan art no mide
  todo el cariño.
- Público latino: **ninguna encuesta latinoamericana** en las partes ⚠️.

---

## 10 · Doblaje latino y frases textuales

### 10.1 La ficha ✅

Hay **dos doblajes latinos**, los dos hechos en Ciudad de México
([Doblaje Wiki, por la API](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Dan_Da_Dan)):

| | **Netflix** | **Crunchyroll** |
|---|---|---|
| Estudio | New Art | Audiomaster Candiani |
| Dirección | **Irwin Daayán** | **Gerardo Márquez** (también dirección musical) |
| Traducción | Fernando Gurrea | Antonio Valdez (el traductor del manga de Panini) |
| Adaptación | — | Jaime Chaparro; adaptación musical, Luis Miguel Morales |
| Guion base | el guion internacional en inglés | los subtítulos de Crunchyroll |
| Estreno | 3-oct-2024, a la vez que Japón | 24-oct-2024, con 3 semanas de retraso |
| Estilo | groserías y vocabulario neutro, algo coloquial | **jerga mexicana**, anglicismos, cultura pop e internet |
| Nombres japoneses | pronunciación llana | pronunciación esdrújula |
| Canciones de la serie | **en japonés** | **dobladas al español** |

- El primer doblaje, en **Iyuno México**, iba avanzado y se perdió por
  la **filtración del 9-ago-2024**. Netflix lo rehízo en New Art sin
  nadie del equipo anterior ✅ (Doblaje Wiki).
- Gerardo Márquez **ya seguía el manga** y llevó **su colección de
  tomos** al estudio para enseñar las escenas a los actores ✅ (Doblaje
  Wiki).
- Anuncios oficiales: [ANMTV, Netflix](https://www.anmtvla.com/2024/10/dandadan-se-estrena-con-con-doblaje.html)
  y [ANMTV, Crunchyroll](https://www.anmtvla.com/2024/10/dandadan-recibe-un-segundo-doblaje.html) ✅.

### 10.2 Quién dobla a cada uno (dos fuentes por nombre) ✅

| Personaje | Seiyū | Netflix | Crunchyroll | Fuentes |
|---|---|---|---|---|
| Momo Ayase | Shion Wakayama | **Azucena Estrada** | **Alicia Vélez** | Doblaje Wiki + ANMTV (las dos) |
| Okarun | Natsuki Hanae | **José Luis Piedra** | **Iván Bastidas** | Doblaje Wiki + ANMTV |
| Turbo Granny | Mayumi Tanaka | **Rebeca Patiño** | **Magda Giner** | Doblaje Wiki + ANMTV |
| Aira Shiratori | Ayane Sakura | **Fernanda Gastélum** | **Elizabeth Infante** | Doblaje Wiki + [Anime Argentina](https://animeargentina.net/fernanda-gastelum-voz-de-aira-shiratori-en-dandadan/) / Instagram de @wdn.es y sonica.mx |
| Seiko Ayase | Nana Mizuki | Karla Falcón | Xóchitl Ugarte | Doblaje Wiki + ANMTV |
| Jiji | Kaito Ishikawa | Dalí González | Marc Winslow | Doblaje Wiki + AniList ⚠️ (Winslow, sólo Doblaje Wiki) |

**Lo que un fan del doblaje sabe** (Doblaje Wiki) ✅:

- Azucena Estrada y Alicia Vélez (las dos Momo) ya compartieron a
  **Gin Akutagawa** en *Bungo Stray Dogs*.
- José Luis Piedra e Iván Bastidas (los dos Okarun) son **Zenitsu y
  Tanjiro** en *Demon Slayer*.
- Magda Giner rechazó primero el papel en Netflix (pocos *loops* y
  presencial); meses después la llamó Crunchyroll para el mismo
  personaje.
- Marc Winslow es el único del reparto principal de Crunchyroll que sale
  también en Netflix (allí es Kinta).
- De niños, en Netflix: Sarah Mendoza (Momo), Ximena Frutos (Aira),
  Elian Garcés (Jiji). En Crunchyroll los hacen los mismos adultos.

### 10.3 Frases textuales, con su vídeo y minuto

**Oídas con `voz.py`** (Whisper) en el episodio 1 con **audio latino de
Crunchyroll** ([Internet Archive](https://archive.org/details/dan-da-dan-latino-01)):

| Frase | Quién | Minuto | Cómo suena |
|---|---|---|---|
| «**Nos va a tener que dar su banana**» | los Serpo | [14:59](https://archive.org/details/dan-da-dan-latino-01?t=899) ✅ | agudo (304 Hz), muy expresivo (29,6 semitonos), 2,84 palabras/s |
| «**Maldito ladrón de bananas**» | los Serpo | [15:13](https://archive.org/details/dan-da-dan-latino-01?t=913) ✅ | — |
| «no me jodas», «a la chingada» | la llamada del principio (Momo y su novio) | [1:31-2:28](https://archive.org/details/dan-da-dan-latino-01?t=91) ⚠️ | 214 Hz, 32,4 semitonos, 3,01 palabras/s. Whisper transcribe con ruido: revisar de oído |

**Citadas por Doblaje Wiki** con su episodio (⚠️ sin minuto; no las
oímos):

| Frase | Versión | Episodio | De dónde viene |
|---|---|---|---|
| «**Chico misterio**» (Momo a Okarun, antes de saber su nombre) | Netflix | 1 | — |
| «**Ocultista**» (lo mismo) | Crunchyroll | 1 | apodo de Manga Plus |
| «**Turbo Abuela**» | Netflix | todos | Manga Plus |
| «**Turbo Ruca**» | Crunchyroll | todos | el manga de Panini |
| «**Jaimito Maussan**» (así le decían a Okarun de niño) | Crunchyroll | 1 | Jaime Maussan, ufólogo mexicano |
| «**Santa Dodoria**» / «**Dodoria Santa**» (alias de Seiko) | Netflix / Crunchyroll | 3 | — |
| «**¿Te parece que somos ricos?**» (Turbo Ruca a Okarun, comiendo) | Crunchyroll | 10 | **Lois de *Malcolm***, también de Magda Giner. Meme |
| «a mi lado por siempre, **chiquita**» (Okarun, final del ending de *Slam Dunk*) | Crunchyroll | 12 | letra latina de 1998 de Loretta Santini, con una palabra cambiada |
| «**quiere unas pataditas en sus costillitas**» (Momo, pateando el cadáver de la Gran Serpiente) | Netflix | 14 | **Número 1** de *KND*; Azucena engrosa la voz en homenaje a Blas García |
| «**Jennifer López, Anaconda**» (técnica de Naki Kito) | Netflix | — | Yolanda Vidal dobló a J. Lo en *Anaconda* |
| «**Mega Rayo Ternuri**» (Moe Moe Kikoho) | Crunchyroll | 19 | en Netflix se deja «Moe Moe Kikoho», guiño a Ten Shin Han |
| «**Oye, despacio cerebrito**» (Momo a Okarun) | **Netflix** | penúltimo de la T2 | el Jefe Gorgory, *Los Simpson*. Meme |
| «**¡Cállense, cállense que me desesperan!**» (Momo) | **Netflix** | último de la T2 | **Quico**, *El Chavo del 8* |

⚠️ **Corrección**: la parte de voz pone las dos últimas en Crunchyroll.
En el wikitext de Doblaje Wiki están bajo «Versión Netflix».

**La actriz de Aira (Netflix), sobre grabar el ep. 7** ✅
([Anime Argentina, 24-ago-2025](https://animeargentina.net/fernanda-gastelum-voz-de-aira-shiratori-en-dandadan/)):
«Ese día yo llegué al estudio y tenía poco para grabar… me dieron ganas
de llorar y el director me dijo si necesitaba un momento y yo le dije
que no… el resultado fue maravilloso.» Y: «Me identifico mucho con
Aira… tengo TDAH, y si no tengo todo planeado me estreso mucho.»

**Errores del doblaje** (Doblaje Wiki, una fuente ⚠️): Netflix ep. 5,
6:10 (falta una línea de fondo); ep. 8, 1:25 (Aira dice «Takamura»);
ep. 9 (voces desfasadas en opening y ending, corregido en HBO Max);
ep. 20 (filtro de voz de Aira irregular). Crunchyroll ep. 3, 7:50 (eco
por error a Ayase, corregido).

⚠️ **No hay clips oficiales doblados** que se pudieran bajar (YouTube
pidió iniciar sesión). Las frases con audio salen del episodio completo
de Internet Archive.

---

## 11 · Música y sonido

### 11.1 Openings y endings ✅

Dos fuentes cada uno: [Wikipedia, lista de episodios](https://en.wikipedia.org/wiki/List_of_Dandadan_episodes)
(cita a Anime News Network) y los tráileres.

| Temporada | Opening | Ending |
|---|---|---|
| T1 (2024) | **«Otonoke»** (オトノケ), **Creepy Nuts** | **«Taidada»**, **Zutomayo** (ずっと真夜中でいいのに。) |
| T2 (2025) | **«Kakumei Dōchū»** (革命道中, «De camino»), **Aina the End** | **«Doukashiteru»** (どうかしてる), **WurtS** |

- «Otonoke» ganó **Mejor Secuencia de Apertura** en los 9.º Crunchyroll
  Anime Awards (mayo 2025) ([Wikipedia](https://en.wikipedia.org/wiki/9th_Crunchyroll_Anime_Awards)) ✅.
- Ese opening se hizo con **recortes de papel y lápiz de verdad**, no
  con un filtro: su director de secuencia, **Abel Góngora**, quería «ir
  en la dirección contraria a la IA»
  ([ComicBook.com](https://comicbook.com/anime/news/dandadan-director-ai-anime/)) ✅.
- ⚠️ **El opening no se miró** como vídeo propio (AnimeThemes caído,
  YouTube bloqueado). El ep. 1 de Internet Archive se llama «op-join» y
  sus minutos 22-23 tienen muchos cortes (31-35 planos por minuto en
  `episodios.md`): quizá sea el opening pegado. Sin comprobar.
- Cover de fans del OP2: «On the Way», Miura Jam, 2025-08-21
  ([MusicBrainz](https://musicbrainz.org/release-group/0806bfc8-4e82-498a-aa60-db7d149b54b1)) ⚠️.

### 11.2 La banda sonora ✅

- **Kensuke Ushio** (牛尾憲輔). Sale en el tráiler oficial («MUSIC / 音楽
  牛尾憲輔», 0:20) y en MusicBrainz: [banda sonora](https://musicbrainz.org/release-group/5ff86679-629c-4d56-82e4-32ef8f93aed5)
  (2024-12-06) y [*Lead Trax*](https://musicbrainz.org/release-group/7fb6a561-9cd0-457a-a709-2c5d41037555) (2024-11-08).
- Usa **Big Beat electrónico** y **graba sonidos falsos** para
  samplearlos, en vez de usar muestras con derechos
  ([Sakuga Blog](https://blog.sakugabooru.com/2024/10/03/dandadan-production-notes-01/)) ✅.
- Sonido: dirección **Eriko Kimura**, efectos **Shouta Yaso**, selección
  musical **Maiko Gouda** ([AniList](https://anilist.co/anime/171018/staff)).

### 11.3 Lo que suena en las escenas clave (visto en el ep. 1)

- **Persecución del túnel** (10:55-11:26): música tensa y rítmica,
  pegada a los golpes de la persecución.
- **Despertar de Momo** (13:16-14:10): la música sube con capas de
  sintetizador a la vez que todo se vuelve cian.
- **Ep. 7, la escena que hace llorar**: la música **baja a silencio** en
  los momentos clave (parte de voz).
- ⚠️ No hay lista de pistas con minutos: los nombres de las pistas no se
  saben. Se reconocen de oído con estos minutos.

### 11.4 Las canciones dentro de la serie (y el doblaje) ✅ Doblaje Wiki

| Ep. | Quién canta | Qué | Netflix | Crunchyroll |
|---|---|---|---|---|
| 1 | Okarun | «Too Shy Shy Boy!» (Alisa Mizuki) | José Luis Piedra **la canta en japonés** | la cambian por **«Tímido» de Flans** (sale del manga de Panini) |
| 8-9 | el Dover Demon | «Chiquitita» (ABBA) | en japonés | con **la letra en español del propio ABBA** |
| 12 | Okarun y Jiji | opening y ending de ***Slam Dunk*** | en japonés | en español, con **la letra latina de 1998 de Loretta Santini** («…a mi lado por siempre, chiquita») |
| 17 | Jiji | «Olvida la amargura» (*Ranma ½*) | japonés con subtítulos de Jorge Roig | cantada con la adaptación de Jorge Roig |
| 18 | la banda **Hayasii** (inspirada en X Japan) | «Hunting Soul» | en japonés | en español, **Nando Fortanell** |

- **Irwin Daayán** insistió en Netflix para doblar *Slam Dunk* y *Ranma*
  como gesto a los fans, y **dirigió a Dalí González cantándolas**,
  pero no entró en el resultado final ✅ (Doblaje Wiki).
- En el avance del ep. 10 de la T2 sí se dobló «Char ga kuru» (*Gundam*)
  que canta Kinta; en el episodio quedó en japonés.

### 11.5 Efectos y onomatopeyas

- **El título es una onomatopeya**: ダンダダン suena a redoble de tambor
  ✅.
- ⚠️ Según la [wiki de efectos de sonido](https://soundeffects.fandom.com/api.php?action=parse&page=DanDaDan&format=json&prop=wikitext)
  (una fuente, comunitaria): el rugido del **kaiju** es el del **T-Rex
  de *Jurassic Park*** mezclado con «Sharktopus Roar»; el puñetazo es
  «Sound Ideas, PUNCH, FACE - HARD FACE PUNCH 02»; la vaca del arco de
  la mutilación de ganado, «Sound Ideas, COW - SINGLE MOO».

---

## 12 · Vídeos y tendencias

### 12.1 Mirados de verdad ✅

Los tres tráileres de §2.3 (`fotogramas.py --cortes`: 29 fotogramas del
japonés, 59 del de la T2) y los **episodios 1 a 8** de §2.1-2.2 (el 1 y
el 5 enteros con `episodio.py`: 484 y 404 planos, con transcripción
japonesa; los demás, cada 15 s).

### 12.2 Otros útiles, sin mirar ⚠️

| Vídeo | Dónde | Vistas | Nota |
|---|---|---|---|
| Tráiler oficial | [YouTube](https://www.youtube.com/watch?v=rJo1MnsuxyY) | — | el de AniList; YouTube pidió iniciar sesión |
| «Dandadan - trailer» | [Dailymotion](https://www.dailymotion.com/video/x8uepus) | 88.781 | JeuxVideo.com |
| «Tráiler Dan Da Dan Temporada 2» | [Dailymotion](https://www.dailymotion.com/video/x9b3u3c) | 350.490 | 3DJuegos, 0:15 |
| 3.er PV (estreno 3-oct-2024) | [Internet Archive](https://archive.org/details/tv-anime-dan-da-dan-3rd-pv-24.10.3-broadcast-started) | — | — |
| Opening hecho por fans con «Ashura-chan» de Ado | [Internet Archive](https://archive.org/details/dandadan-fanmade-opening-ashura-chan) | 606 descargas | tendencia de fans |
| Entrevista «¡El anime caótico regresa!» con Azucena Estrada e Iván Bastidas | Doblaje Wiki, «Muestra multimedia» | — | las voces de Momo (Netflix) y Okarun (Crunchyroll) juntas |
| Pódcasts *Ani-Gamers* y *Baka! Baka! Baka!* 209 y 223 | [Internet Archive](https://archive.org/details/bbb-209-dan-da-dan) | — | reseñas en audio |

### 12.3 Tendencias ⚠️

- **Reddit**: «It was ICONIC that Okarun says his name & background
  goes KABOOM» (**3515 votos**) es plantilla de meme
  ([hilo](https://www.reddit.com/r/Dandadan/comments/1mu93jv/it_was_iconic_that_okarun_says_his_name/)) ✅.
- **TikTok**: no se pudo entrar sin sesión. Sin cifras.
- **Análisis en vídeo**: no se encontró ninguno descargable.

---

## 13 · Videojuegos de la franquicia

**Dandadan no tiene videojuego propio** ✅. Comprobado: la API de
[Steam](https://store.steampowered.com/api/storesearch/?term=dandadan)
da 0 resultados; The Cutting Room Floor no tiene página; en tiendas
móviles sólo hay juegos de fans (Roblox, itch.io). Vive en
**colaboraciones con juegos ajenos**:

| Juego | Cuándo | Qué trae | Fuentes |
|---|---|---|---|
| ***Monster Strike*** (XFLAG, móvil) | 1-14 oct 2025 | Momo, Okarun y Jiji de 6 estrellas **con sus seiyū**; Aira y Kinta de 5; Turbo Babaa y Hoshiko en el paquete de inicio. Enemigos: Mongolian Death Worm, Dover Demon, Kitou Naki, Flatwoods Monster, Serpo | [Animeworld](https://animeworld.info/2025/09/29/dandadan-x-monst-collaboration-begins-momo-okarun-jiji-more-join-limited-gacha-goods-also-available/) ⚠️ una fuente |
| ***Honor of Kings*** (Tencent) | 1-31 ago 2026 | aspectos: Okarun sobre Lam, Momo sobre Daji, Turbo Granny sobre Mozi; mapa temático y líneas de voz propias | [UNGEEK](https://www.ungeek.ph/2026/08/honor-of-kings-x-dandadan-collab-is-live-now-until-august-31/), [LapakGaming](https://www.lapakgaming.com/blog/en-my/honor-of-kings-x-dandadan/) ✅ |
| *Jump+ Jumble Rush* | — | Okarun en *chibi*, normal y transformado (hoja 2 n.º 52 y 54) | wiki ✅ |
| *Grand Summoners* | — | Momo (agua), Okarun (rayo verde), Aira (fuego), normales y «Super Awakening» (hoja 2 n.º 56-61) | wiki ✅; fecha sin confirmar |

- ⚠️ **Ninguna caja de diálogo de estas colaboraciones se vio**: no hay
  capturas de interfaz en las partes.
- **Qué NO hacer**: inventar «la pantalla del juego de Dandadan». Si una
  lámina necesita algo de juego, mejor el lenguaje del manga (§7).

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todo fan reconoce ✅

- **El robo de las «bolas doradas»** (*kintama*) de Okarun: el chiste que
  sostiene medio primer arco. El doblaje de Crunchyroll lo dice con
  **«banana»** («Nos va a tener que dar su banana», ep. 1, 14:59), y el
  tráiler también («Please give us your banana», 0:12).
- **Okarun diciendo su nombre y una explosión detrás** (Reddit, 3515
  votos).
- **Momo y Okarun** como pareja; el arco de Kinta que retrasa el romance
  divide («this arc was needed», 908 votos).
- **Aira y Momo cargan las peleas** (1218 votos).
- **El ep. 7** hace llorar: «Third time I've drowned in tears», «made a
  grown man shed a tear»
  ([Sportskeeda](https://www.sportskeeda.com/anime/dandadan-episode-7-review-science-saru-proves-perfect-blend-action-emotion), que cita los foros de MyAnimeList).
- **Los memes del doblaje latino**: «¿Te parece que somos ricos?»,
  «Oye, despacio cerebrito», «¡Cállense, cállense que me desesperan!»
  (§10.3).
- El **gato de la suerte** de Turbo Granny, con su 千万両.

### 14.2 Qué NO hacer ✅

- ❌ **Mezclar los doblajes.** «Turbo Abuela» y «Chico misterio» son
  **Netflix**; «Turbo Ruca» y «Ocultista» son **Crunchyroll**. Se elige
  uno y se sigue. El propio Doblaje Wiki lo anota como dato: el fandom
  se fija.
- ❌ **Turbo Granny tierna.** Es cruel y malhablada; su lado compasivo es
  un secreto de fondo, no su cara pública.
- ❌ **Aira como «chica tonta y linda».** Es vanidosa y calculadora, y
  pelea.
- ❌ **Quitar el chiste de las bolas.** Sin él se cae el arco. Para un
  servidor público, basta con el eufemismo del propio doblaje: la
  «banana».
- ❌ **Confundir a Seiko con Turbo Granny.** Las dos son ancianas de
  pelo blanco; Seiko lleva **lentes rojos** y Turbo Granny **ojos
  amarillos que miran a los lados**. (Hasta una parte se equivocó, §28.)
- ❌ **El pelo de Okarun castaño.** En el manga es castaño, **en el anime
  es negro** (wiki, *Appearance*).
- ❌ **Cambiar los colores de bando** (§7.2).
- ❌ **«¡Nyoron!»** como grito de Okarun: sin fuente (§8.2).
- ⚠️ No se encontró una lista hecha por fans de «lo que les parece
  falso»: esto sale de reseñas, la wiki y el audio.

---

## 15 · Poses analizadas por personaje

De la parte de vídeo (vistas en los eps. 1 y 5 y en las hojas de la
wiki), con dos correcciones del redactor (§28). Los enlaces llevan al
segundo exacto.

### 15.1 Momo (9) ✅

| # | Pose | Dónde | Qué hace | Sirve para |
|---|---|---|---|---|
| 1 | Furiosa, protectora | [ep. 1, 13:20](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=800) | ojos muy abiertos, pelo levantado por la energía, mandíbula tensa, de frente | **regañar** |
| 2 | Grito de rescate | [ep. 1, 13:43](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=823) | puños cerrados, cuerpo hacia delante, boca abierta | **animar** |
| 3 | Poder desatado | [ep. 1, 17:45](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=1065) | brazos cruzados ante el pecho, aura geométrica blanca en los puños | **presentar** |
| 4 | Aviso | [ep. 1, 18:11](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=1091) | primer plano, ojos entrecerrados, ceño | **regañar** |
| 5 | Agotada, cayendo | [ep. 1, 18:34](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=1114) | cuerpo flojo de espaldas | después del esfuerzo |
| 6 | Riendo | [ep. 1, 21:54](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=1314) | cabeza atrás, ojos cerrados, sonrisa amplia, mano en el pelo | **celebrar** |
| 7 | Caminando de noche | [ep. 1, 21:02-21:33](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=1262) | manos en los bolsillos, hombros sueltos | charla tranquila |
| 8 | Psicoquinesis | hoja 2 n.º 50 | en el aire, una pierna doblada, manos hacia abajo | **explicar** su poder |
| 9 | Salto de portada | hoja 1 n.º 37 | piernas encogidas, uniforme al viento, mira abajo | portada |

Extra, visto por el redactor: **disculpa ruborizada, mano en la
cabeza** ([ep. 5, 14:26](https://archive.org/details/english-sub-s-01.-e-05?t=866)) y
**llorando de risa** ([ep. 5, 15:12](https://archive.org/details/english-sub-s-01.-e-05?t=912)).

### 15.2 Okarun (7) ✅

| # | Pose | Dónde | Qué hace | Sirve para |
|---|---|---|---|---|
| 1 | Incómodo | [tráiler, 0:16](https://www.dailymotion.com/video/x8u8yoq?start=16) | mano en la sien ajustando los lentes, ceño, encogido | **pensar** |
| 2 | Aterrado | [ep. 1, 11:52-12:03](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=712) | manos abiertas empujando, cuerpo arqueado hacia atrás | miedo |
| 3 | Transformado, protector | [ep. 1, 14:27](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=867) (la frase «If it's for her sake…» llega a las 16:12) | agachado, garras hacia delante, ojo rojo | **animar** |
| 4 | Suplicando | [ep. 1, 14:39-14:46](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=879) | manos juntas al pecho, cabeza inclinada | pedir ayuda |
| 5 | Explicando avergonzado | [ep. 1, 21:29-21:39](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=1289) | mano en la nuca, mirada de lado | **explicar** |
| 6 | Dos dedos en los lentes | [ep. 5, 14:18-14:50](https://archive.org/details/english-sub-s-01.-e-05?t=858) | cabeza algo baja, cara seria | **pensar**, pausa antes de hablar |
| 7 | En guardia (*chibi*) | hoja 2 n.º 52 | de pie, puños arriba, ceño | **presentar** |

Extra: **niño leyendo su revista** en el pupitre ([ep. 1, 15:50-15:57](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=950);
hoja 2 n.º 77 y 80) y **mirando al cielo** (15:47). Son las de §27 A.

### 15.3 Turbo Granny (7) ✅ con corrección

| # | Pose | Dónde | Qué hace | Sirve para |
|---|---|---|---|---|
| 1 | Ojos en la oscuridad | [ep. 1, 10:55](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=655) | sólo dos ojos amarillos y colmillos | **presentar** la amenaza |
| 2 | Persiguiendo en silueta | [ep. 1, 11:10-11:23](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=670) | encorvada, corriendo, contra fondo rojo | velocidad |
| 3 | Forma yokai atacando | [ep. 1, 18:41-18:59](https://archive.org/details/english-sub-s-01.-e-01-op-join?t=1121) | de pie, brazos arriba con garras, melena blanca sobre media cara, boca abierta | **regañar**, amenazar |
| 4 | De pie, neutra | hoja 2 n.º 75 (concept art) | cuerpo entero, kimono rojo, pelo blanco a un lado, erguida | **presentar** |
| 5 | El gato con el talismán | [ep. 5, 16:05](https://archive.org/details/english-sub-s-01.-e-05?t=965) | el gato sentado, talismán pegado al costado | **explicar** (§27 B) |
| 6 | El gato con la pata alzada | [ep. 5, 16:51](https://archive.org/details/english-sub-s-01.-e-05?t=1011) | pata levantada, mirada de lado | **llamar**, saludar |
| 7 | El gato sobre la mesa baja | [ep. 5, 17:16](https://archive.org/details/english-sub-s-01.-e-05?t=1036) | de frente, talismán «家内安全 / 厄除» | la lámina B |

⚠️ La parte de vídeo tenía 3 poses más de «Turbo Granny en forma
humana» (ep. 5, 15:24-16:54). **Son de Seiko** (lentes rojos, fuma, da
órdenes con un abanico): las paso a §15.5.

### 15.4 Aira (7) ✅

| # | Pose | Dónde | Qué hace | Sirve para |
|---|---|---|---|---|
| 1 | Disculpándose | [ep. 5, 11:49-12:19](https://archive.org/details/english-sub-s-01.-e-05?t=709) | inclinada, manos junto al pecho, ojos grandes | **presentar** su cara amable |
| 2 | Sonrisa halagadora | [ep. 5, 12:15-12:19](https://archive.org/details/english-sub-s-01.-e-05?t=735) | cabeza ladeada, mano en el pelo | **celebrar**, coquetear |
| 3 | La V con sus amigas | [ep. 5, 12:53-13:06](https://archive.org/details/english-sub-s-01.-e-05?t=773) | de espaldas, dedos en V, en corro | **celebrar** en privado |
| 4 | Sorprendida de verdad | [ep. 5, 13:36-13:38](https://archive.org/details/english-sub-s-01.-e-05?t=816) | ojos muy abiertos, se gira hacia Momo que cae | preocupación real |
| 5 | Burlona | [ep. 5, 13:50](https://archive.org/details/english-sub-s-01.-e-05?t=830) | media sonrisa, ceja alzada, mirando de lado | **regañar** con sarcasmo |
| 6 | Patada alta | hoja 1 n.º 20 («Aira kicks Chorus giant», [1920×1080](https://static.wikia.nocookie.net/dandadan/images/5/5d/Aira_kicks_Chorus_giant.png)) | pierna arriba, brazos abiertos, pelo y falda al viento | **animar** |
| 7 | De pie (concept art) | hoja 2 n.º 66 | manos junto al cuerpo, mirada al frente | **presentar** |

### 15.5 Seiko (3, antes atribuidas a Turbo Granny)

| Pose | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| Examinando de cerca | [ep. 5, 15:54-16:01](https://archive.org/details/english-sub-s-01.-e-05?t=954) | cabeza adelante, ceño, lentes rojos: «There's something hiding inside him» | **pensar** |
| Fumando, dedos en alto | [ep. 5, 16:09](https://archive.org/details/english-sub-s-01.-e-05?t=969) | cigarro en la boca, mano levantada | explicar con calma |
| Dando órdenes con el abanico | [ep. 5, 16:45-16:54](https://archive.org/details/english-sub-s-01.-e-05?t=1005) | abanico de papel en la mano | **mandar** |

Y el key visual con el **bate al hombro** (hoja 3 n.º 6 y la figura n.º 25).

### 15.6 Qué pose para qué

| Para… | Momo | Okarun | Turbo Granny | Aira |
|---|---|---|---|---|
| presentar | 3 (aura) | 7 (guardia) | 1 (ojos) o 4 | 1 o 7 |
| explicar | 8 (psicoquinesis) | 5 (nuca) | 5 (gato y talismán) | — |
| celebrar | 6 (risa) | — ⚠️ | — ❌ | 2 o 3 |
| regañar | 1 o 4 | — | 3 (yokai) | 5 |
| pensar | — | 1 o 6 (lentes) | — | — |
| animar | 2 (grito) | 3 (protector) | — | 6 (patada) |

---

## 16 · Vestuario, con hex medidos

Colores con `estilo.py` sobre **arte oficial** (key visuals del sitio y
modelo de color), quitando el fondo.

### 16.1 La ropa icónica de cada uno ✅

- **Momo · uniforme de Kami High** (el que todos reconocen): **suéter
  rosa** de manga larga sobre camisa blanca, **lazo rojo** suelto, falda
  plisada **azul marino**, **calcetas blancas holgadas**, mocasines
  marrones. **Aretes redondos verdes** y **gargantilla negra** con
  adorno verde, que conserva con cualquier ropa. Pelo caoba medio, que
  enmarca **el lado derecho** de la cara; ojos carmesí. Estilo *kogal*
  de gyaru (wiki).
  - Key visual: rosa claro **#F5C6C1**, rosa sombra **#CC9694**, falda
    **#795566**.
  - Modelo de color: piel **#EDD5C7**, blanco cálido **#F9F2F1**, sombra
    **#433547**. Línea **#6F544C** / **#645552**.
  - Fuentes: [key visual](https://anime-dandadan.com/_assets/images/char/detail/momo_pc.png)
    y [modelo de color](https://static.wikia.nocookie.net/dandadan/images/d/da/Momo_Ayase_full_appearance_%28color_scheme%29.png) ✅.
- **Okarun · *gakuran* de Kami High**: chaqueta y pantalón **gris carbón
  casi negro**, cuello alto, **botones dorados redondos**, zapatillas
  blancas. **Lentes redondos** de montura fina. Pelo **negro en el
  anime** (castaño en el manga), antes en tazón, **despeinado** desde el
  Flatwoods Monster. Se le marcan los músculos con el entrenamiento.
  - Key visual: **#363838**, **#1E2020**, piel **#CEB9AD**. Línea
    **#5F5F5F** / **#5C544F**
    ([key visual](https://anime-dandadan.com/_assets/images/char/detail/ken_pc.png)) ✅.
  - **Transformado**: pelo blanco, ojos rojos, **máscara de dientes** en
    la boca, marcas rojas en la cara, uñas negras, ropa rota (etiquetas
    de Danbooru; figura TENITOL, hoja 3 n.º 23).
- **Turbo Granny · dos cuerpos**:
  - **El gato** (maneki-neko): porcelana blanca, orejas rojas por dentro,
    **collar rojo y verde con cascabel dorado**, **medallón dorado con
    千万両** («diez millones de *ryō*», amuleto de dinero). Medido en el
    [concept art](https://static.wikia.nocookie.net/dandadan/images/a/aa/Turbo_Granny_Anime_Concept_Art_Doll.png):
    crema **#F4F4F0**, negro **#0B0C0A**, rojo teja **#A2412E**, dorado
    arena **#C2B076** ✅.
  - **La yokai**: *haori* rojo con **damasco floral** rojo sobre rojo,
    mangas a rayas, pantalón corto azul verdoso, pelo blanco largo y
    desgreñado sobre media cara, piel rojiza arrugada, **ojos amarillos
    que miran a los lados**, descalza con garras
    ([key visual](https://anime-dandadan.com/_assets/images/char/detail/turbo-granny-changed_pc.png)) ✅.
- **Aira · uniforme del arco Acrobatic Silky**: blazer azul marino casi
  negro con **el escudo del colegio** en el pecho izquierdo, vivos
  granate y crema, **lazo rojo grande**, falda corta, calcetas altas
  blancas. Pelo **rosa claro corto** que enmarca **el lado izquierdo**
  (al revés que Momo); ojos rosa oscuro.
  - Key visual: blazer **#4A3F59**, piel **#EFD1C3**, malva **#B87C7F**
    ([key visual](https://anime-dandadan.com/_assets/images/char/detail/aira_pc.png)) ✅.
  - ⚠️ Los zapatos: la parte de imagen ve «mary jane grises»; la wiki
    dice «sandalias». Mirar el key visual antes de dibujarlos.

### 16.2 Otras ropas (vistas en las hojas) ✅

- Momo: de camarera (hoja 1 n.º 2), de sirvienta (n.º 39), con ropa de
  médium (n.º 10), con gafas (n.º 48). **En casa**, una **sudadera verde
  grande** con un dibujo (ep. 5, 17:08).
- Aira: chaqueta marrón con cuello alto blanco (hoja 2 n.º 63); ropa del
  arco del kaiju (n.º 62).
- Seiko: pelo blanco recogido con tela blanca, **lentes rojos**,
  camiseta de tirantes (ep. 5); chaqueta bordada y bate (key visual).
  ⚠️ Sin hex medido.
- ⚠️ No hay imagen suelta del **escudo de Kami High**: sólo el texto de
  la wiki.
- Bolso escolar tipo Boston (Aira, hoja 3 n.º 16) ⚠️ una imagen.

### 16.3 Cosplay como referencia de volumen ✅

[Carbon Costume](https://carboncostume.com/momo-ayase-from-dandadan/)
lista las piezas de Momo: peluca con flequillo cruzado, aretes
«alienígenas», lazo rojo, gargantilla negra, camisa blanca, suéter
rosa, falda plisada azul marino, calcetas blancas holgadas, zapatos
marrones. Coincide con lo medido.

---

## 17 · Paisajes y fondos de pantalla

### 17.1 Sitios con su luz y su hora ✅

| Sitio | Hora y luz | Dónde verlo |
|---|---|---|
| **Túnel** de Turbo Granny | noche, linterna dorada contra negro | ep. 1, 10:49-11:26 |
| **OVNI** de los Serpo | luz cian saturada | ep. 1, 12:00-14:10 |
| **Aula** de la infancia de Okarun | día; carteles de caligrafía **勇気** («valor») en la pared, pizarra, pupitre de madera | ep. 1, 15:50-15:57 |
| **Pasillo de Kami High** | tarde, marrones apagados | ep. 5, 11:36-14:04 |
| **Calle residencial al atardecer** | cielo rosa y lila, edificios bajos | ep. 5, 14:11-15:04 |
| **Casa de Seiko** | tarde; tatami, mesa baja de madera, puertas correderas, tele | ep. 5, 15:12-17:23 |
| **Fachada de Kami High** | día despejado | [wiki, 1920×1080](https://static.wikia.nocookie.net/dandadan/images/7/72/High_School_%28Anime%29.png) |
| **Daija Town** | día, montañas verdes, escalinata | [wiki, 1920×1080](https://static.wikia.nocookie.net/dandadan/images/f/fb/Daija_Town_%28Anime%29.png) |
| **Torre eléctrica y luna** | noche | [Wallhaven, captura del anime, 1920×1080](https://w.wallhaven.cc/full/kx/wallhaven-kxo3rq.png) |

### 17.2 Fondos de pantalla ✅ ([Wallhaven](https://wallhaven.cc/search?q=Dandadan), con tamaño y autor)

| Tamaño | Qué es | Subido por / origen |
|---|---|---|
| **8192×4096** | Momo en un interior de noche, sofá y lámpara | SagXD / [Pixiv 133070020](https://www.pixiv.net/artworks/133070020) |
| 4400×2200 | Momo | Elisban |
| 4400×2200 | Okarun | Elisban |
| 4078×3053 | Momo y Okarun de perfil | Ramces |
| 3840×2160 | Okarun y Momo | leoscau |
| 3840×2160 | pelo blanco y castaño (¿Okarun transformado?) ⚠️ | Elisban / [pinjirooo](https://x.com/pinjirooo/status/1860305772099604922) |
| 2666×1500 | Momo con el gato de la suerte | Elisban / [Pixiv 123208924](https://www.pixiv.net/en/artworks/123208924) |
| 2560×1440 | Momo gyaru | TheWitch |
| 1966×3000 | Momo y Turbo Granny, de Mirco Cabbia | jrmnt / [sciamano240](https://x.com/sciamano240/status/1870129953464815847) |
| 1920×1080 | Momo, primer plano violeta | MrPato |
| 1920×1080 | Seiko con gafas (captura) | MrPato |
| 1920×1080 | Okarun, naranja (captura) | MrPato |

- Para el celular: los **key visuals** del sitio oficial (984×1570, fondo
  transparente) con un fondo liso detrás.
- ⚠️ **No hay fondos oficiales para descargar** (ni en
  anime-dandadan.com ni en Crunchyroll: revisado el HTML).

---
