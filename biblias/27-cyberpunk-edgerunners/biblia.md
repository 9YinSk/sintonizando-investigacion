---
tags: [biblia, serie, laminas]
serie: "Cyberpunk: Edgerunners (サイバーパンク エッジランナーズ)"
canal: "#a-que-juegas"
fecha: 2026-09-24
---

# Biblia · Cyberpunk: Edgerunners — para #a-que-juegas

> [!important] Cómo se hizo, y sus límites
> - **Primera mitad de la sesión, con la red cerrada** (Fandom, Doblaje
>   Wiki, Wikipedia, YouTube, Reddit… bloqueados): búsqueda web en
>   español, inglés, japonés, chino y coreano, y GitHub.
> - **Después se abrió la red** y usé todo lo que pide el encargo:
>   - `herramientas/investigar_serie.py` sobre la wiki `cyberpunk`
>     (10 páginas: Lucy, David, Rebecca, Maine, Kiwi, Falco, Dorio,
>     Pilar, Faraday y la serie): **128 imágenes grandes, 3 hojas**
>     (citadas como **W1-W128**, en `hojas/`).
>   - La **API de Doblaje Wiki** para el reparto latino, cruzado con
>     ANMTV, TV Tropes y una **entrevista en vídeo al elenco latino**.
>   - La **API de la wiki** para fichas de personaje (edad, ropa, pasado).
>   - **yt-dlp** para metadatos, capítulos y subtítulos de vídeos
>     oficiales y de clips del doblaje latino (con minuto). Algunos vídeos
>     pedían «confirmar que no eres un robot»: ahí sólo tengo título y
>     duración.
>   - **Reddit** por el archivo de Arctic Shift, la **API de Sketchfab**
>     (licencias reales), la de **Poly Haven** y la de **ambientCG**.
> - De GitHub saqué lo más útil: **los subtítulos de Netflix de los 10
>   episodios, en japonés y en inglés, con sus tiempos**
>   ([kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Cyberpunk.%20Edgerunners)).
>   Los japoneses son **para sordos**: dicen **quién habla**
>   (「（レベッカ）」) y **qué suena** (「（雨の音）」, lluvia). Con ellos doy
>   **el minuto de cada escena**. La traducción al español es mía, salvo
>   donde digo «doblaje latino». El minuto puede moverse uno o dos
>   segundos en Netflix.
> - Ojo: la pista inglesa del **episodio 3** de ese archivo está mal
>   transcrita. Para el ep. 3 me fío de la japonesa.
> - También en GitHub: 3 hojas extra (**G01-G72**) con imágenes que fans
>   subieron (renders, fotogramas, capturas del juego), y las **letras**
>   de [google/fonts](https://github.com/google/fonts), comprobadas con
>   fontTools (á é í ó ú ñ ¿ ¡).
> - **Colores**: los hex con ✅ los **medí** en las imágenes (mediana de
>   píxeles, ±5 por canal).
> - **Cómo cito**: «ep. 4, 21:29» = episodio 4, minuto 21:29. La serie
>   tiene **10 episodios** (2022). «W26» = número de la hoja de la wiki.
> - ✅ **confirmado**: dos fuentes, o el subtítulo o vídeo con su minuto.
>   ⚠️ **dudoso**: una sola fuente, o de memoria. **Lo que se VE** en un
>   fotograma que no está en las hojas lo describo de memoria ⚠️.
>
> - **Segunda pasada (repaso del 25-sep-2026, red abierta, equipo de 4
>   investigadores + redactor).** Se miraron de verdad **7 episodios
>   completos** de Internet Archive y el **tráiler** de Dailymotion con
>   `fotogramas.py` (YouTube pedía iniciar sesión); se midieron colores en
>   esos fotogramas con Pillow; se cruzó el doblaje secundario con
>   **aniSearch** y **Anime-Planet**; se leyó el wikitexto de la wiki
>   `cyberpunk` con sus citas al *Cyberpunk: Edgerunners Mission Kit*
>   (manual oficial del juego de rol); se añadieron los puntos 18 a 25 del
>   encargo y la tabla «Cumplimiento del encargo». Lo que antes era «de
>   memoria» y ya se vio en vídeo, lo digo en cada sección.

---

## Segunda pasada · qué cambió

**Corregido (antes → ahora)**

- Carteles amarillos W26-W32: «¿error de la wiki con Kaneko?» → **no es
  error**: Yuto Kaneko diseñó a Rebecca y Dorio; Yoshiyuki Kaneko hizo el
  arte del opening y estos carteles (§3).
- Emblema verde de la chaqueta de David: «¿es el logo de la serie?» → es el
  logo de la **XBD «Edgerunners» de Jimmy Kurosaki**, un programa de
  braindance *dentro* de la ficción; Lucy se lo proyectó en la chaqueta y
  David lo pintó (§16 y punto 25).
- «I Really Want to Stay at Your House»: «ep. 2, hacia 20:00-21:28 ⚠️» →
  **ep. 2, 19:30-21:30**, visto en fotogramas (§11).
- El opening «This Fffire» **no suena en los primeros 4:20 del ep. 1**: el
  ep. 1 entra directo con la pelea bajo la lluvia. El opening completo se
  vio en el ep. 3, 0:00-1:36 (§11).
- Clínica de Doc: «al norte del bloque de pisos ⚠️» → **Arroyo, Santo
  Domingo** ✅ (§5).
- Doblaje secundario (Dorio, Pilar, Falco, Tanaka, Katsuo, Jimmy Kurosaki,
  Julio, Profesora IA, Adam Smasher): una fuente ⚠️ → **dos fuentes ✅**
  (Doblaje Wiki + aniSearch/Anime-Planet) (§10).
- La muerte de Maine (ep. 6, 22:10-22:48): se describía por subtítulo → **se
  vio**: el visor se agrieta como cristal verde y violeta y estalla en un
  fogonazo blanco; **no se ve el disparo ni el cuerpo** (§2, §14).
- Datos de pasado de David, Rebecca, Maine, Kiwi y Falco: «sólo wiki ⚠️» →
  ✅, porque la wiki cita el *Mission Kit* oficial con página (§8).
- M PLUS Rounded 1c: «no comprobada ⚠️» → ✅ con fontTools (§6).
- Capítulos de los 4 análisis de YouTube: «no pude sacarlos ⚠️» → sacados
  con yt-dlp (§12).

**Añadido**

- Lo que **se ve** en 7 episodios y el tráiler, con minuto (§2, §15).
- Paleta medida en fotogramas propios: 8 hex nuevos (§5).
- Poses nuevas de Maine y Kiwi (llegan a 6 cada uno) (§15).
- Popularidad: **Kiwi es la favorita del director Imaishi**; **Rebecca la
  añadió Trigger** y es la favorita del guionista Rafał Jaki (§9).
- Qué NO hacer: la polémica de Rebecca con fuente, los tatuajes «PKDICK» y
  la calavera de cabra, el pasado de Kiwi fuera de las láminas (§14).
- Secciones nuevas de los **puntos 18 a 25** del encargo (técnica y cómo
  replicarla, texturas 2D, gustos, por qué la aman, fan dubs,
  colaboraciones, obras parecidas, el mundo y su jerga).
- Guía para IA ampliada con la chaqueta «que flota» de Lucy (cosplay de
  Yaya Han) y la jerga de la serie para la IA de texto (§18).
- Conceptos de lámina: mejoras con la pose de Lucy apoyada en la barra
  (figura de Prime 1 Studio) y los logos de corporación como pegatinas en
  la recreativa (§19).
- Tabla «Cumplimiento del encargo» y bitácora de la segunda pasada.
- `referencias.json`: de **38 a 231** referencias.

**⚠️: había 62, quedan __DESPUES__.** Los que quedan son sobre todo:
minutos que no se pudieron volver a ver (YouTube pide iniciar sesión en el
servidor), vistas de los fandubs, la lista vertical de opciones de diálogo
del juego, el programa exacto de producción de Trigger y el amarillo exacto
del logo.

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, categoría **✦ LA SALA ✦**):

> **ıı・🎮・a-que-juegas** (texto) · 0 fijados · 0 de personas en los
> últimos 15 — _Lo que estás jugando, capturas y quién se apunta a una
> partida._

Función según el encargo: **a qué juegas, capturas y armar partida con
la hora de cada país**. Ya hay una lámina que **le gustó** al dueño: este
dossier sirve para **ampliar referencias**, no para rehacerla desde cero.

Vecinos en LA SALA: #general, #memes, y (según otras biblias)
#que-estas-viendo y #que-estas-escuchando. El canal hermano de juegos es
**#ofertas-y-gratis** (NOTICIAS): «Juegos gratis y rebajas de Steam, Epic
y GOG, con el precio en soles».

### Por qué Edgerunners encaja en un canal de juegos

- Es **la serie de un videojuego**: sale de *Cyberpunk 2077* (CD Projekt
  RED) y del juego de rol de mesa *Cyberpunk* de Mike Pondsmith. Pasa en
  **Night City**, la misma ciudad que se juega.
- La historia es **armar un equipo para un trabajo** (en la serie,
  «crew» y «gig»). Es literalmente «quién se apunta a una partida».
- Maine reparte **a partes iguales** («Everybody gets a fair shake», ep.
  3, 18:02 ✅) y David lo repite al final («Equal share of the pot. That's
  my style», ep. 9, 23:19 ✅). Suena a **reparto del botín de una
  partida**.
- El juego se actualizó con cosas de la serie (**parche 1.6
  «Edgerunners»**, ver §13): quien juega a 2077 reconoce la chaqueta de
  David y la escopeta de Rebecca.

### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **A qué juegas** | nombre del canal |
| 2 | **Cuenta lo que estás jugando** | para qué es |
| 3 | **Sube tus capturas** | qué se comparte |
| 4 | **¿Quién se apunta a una partida?** | armar grupo |
| 5 | **Pon la hora de tu país** | la regla para quedar |
| 6 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

### Los textos de la lámina 2 (la hora de cada país)

«Armar partida con la hora de cada país» **no cabe** en la lámina 1 sin
saturarla. Propongo **lámina 2**: la **tabla de récords de la
recreativa** (como la de *Roach Race*, ver §13) o el **panel de horarios
del metro NCART**, con una fila por país (ver §19).

Horas **a 24-sep-2026** (✅ son reglas oficiales conocidas; las marco
⚠️ donde cambian con el verano):

| Zona | Países del servidor | Si en Lima son las **20:00** |
|---|---|---|
| UTC−6 | **México** (centro, sin horario de verano desde 2022), Centroamérica | 19:00 |
| UTC−5 | **Perú, Colombia, Ecuador**, Panamá | **20:00** |
| UTC−4 | **Venezuela** (desde 2016), Bolivia, R. Dominicana, Puerto Rico | 21:00 |
| UTC−3 | Argentina, Uruguay, Paraguay, **Chile en verano** ⚠️ (sep-abr) | 22:00 |
| UTC+2 | **España** peninsular en verano ⚠️ (UTC+1 en invierno) | 03:00 del día siguiente |
| UTC−7 | **Night City** (California) en verano ⚠️ (UTC−8 en invierno) | 18:00 |

Textos de la lámina 2, una idea cada uno:

| # | Texto |
|---|---|
| 1 | **¿Armas partida?** |
| 2 | **Di la hora y el país** |
| 3 | **México 19:00** |
| 4 | **Perú, Colombia y Ecuador 20:00** |
| 5 | **Venezuela 21:00** |
| 6 | **Argentina y Chile 22:00** |
| 7 | **España 03:00** |
| 8 | **O usa el reloj de Discord: cada uno ve su hora** |

El truco del 8 es real: en Discord, escribir `<t:1790000000:t>` (el
número es la hora en formato Unix) se ve **en la hora local de cada
persona** ✅ ([Zapier](https://zapier.com/blog/discord-timestamps/),
[HammerTime](https://hammertime.cyou/en), que genera el código). Para la
lámina basta con la frase.

La fila de **Night City** es un guiño: ponerla en el tablero hace que el
tablero parezca **de la serie** y no un cuadro de Excel.

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué Edgerunners encaja | Es **la serie de un videojuego** (*Cyberpunk 2077*): sus fondos se pintaron **sobre fotos del propio juego** (Inside Look #2, 2:05 ✅) y la serie **hizo volver a jugar** a un millón de personas al día ✅. Su historia es **armar un equipo para un encargo**: «Welcome to the crew» (ep. 3, 17:07) ✅. |
| El objeto | **La recreativa** es real en ese mundo: el parche **1.6 «Edgerunners»** metió recreativas jugables (*Roach Race*) con **tabla de récords** en Night City ✅. Bajo la lluvia de Kabuki (la lluvia abre la serie, ep. 1, 00:13 ✅). |
| El más querido | **Rebecca** ✅: 1.ª en la encuesta de fans de Ranker, «la favorita de todos» en la prensa, más votos en Reddit que Lucy, y manga propio. No hay encuesta oficial. |
| Quién habla | **Rebecca** (invita y anima: «¿Te apuntas o qué?»). Alternativas: **David** (pulgar hacia sí mismo, W26) o **Lucy** («¿Qué te parecería si jugamos juntos?», eco de su frase del tren en el doblaje latino). |
| Cuadro de diálogo propio | **No hay burbuja**: el **subtítulo del juego** (nombre coral `#FE6962`, texto cian `#59E6F0`, Rajdhani) ✅; la **holo-llamada** (en 9 de 10 episodios ✅); el **HUD rojo del ojo** (G41 ✅); la **pantalla de la recreativa** y su **tabla de récords** ✅. |
| Letras | **Rajdhani** (la del juego), **Anton** (rótulos de nombre lima), **VT323** (pantalla), Chakra Petch. Todas con tildes, ñ, ¿ y ¡ (comprobado). |
| Voz latina | Grande Studios, dirección **Jessica Ángeles** ✅. David **José Ángel Torres** ✅, Lucy **María José Moreno** ✅, Rebecca **Melissa Gedeón** ✅, Maine **Humberto Solórzano** ✅, Kiwi **Jocelyn Robles** ✅. |
| Tono | Noche, neón y negro casi puro; amarillo de la chaqueta de David, lima, magenta y cian. **Nada de colores alegres de día.** |
| Hora de cada país | **Lámina 2**: la **tabla de récords** de la recreativa con las horas (México 19:00, Perú-Colombia-Ecuador 20:00, Venezuela 21:00, Argentina-Chile 22:00, España 03:00 y Night City 18:00). |
| Ojo | *Edgerunners 2* se estrena el **20-oct-2026** con otro equipo: la lámina, con los de la primera. |
| Hojas | `hojas/hoja_01-03.jpg` = **W1-W128** (wiki). Extra en `herramientas/referencias/cyberpunk-edgerunners/github_hoja_0X.jpg` = G01-G72. |

---

## 2 · Las escenas que sirven para #a-que-juegas (con minuto)

Todas salen de los subtítulos de Netflix (japonés para sordos + inglés)
de
[kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Cyberpunk.%20Edgerunners):
**el texto, quién lo dice y el minuto están comprobados ✅**. La
traducción al español es mía. Lo que se VE: en la 2.ª pasada se miraron con fotogramas las escenas de §2.6; el resto sigue de memoria ⚠️.

### 2.1 Night City bajo la lluvia (el ambiente del objeto)

| Escena | Ep. y minuto | Qué pasa / qué se oye | Para qué sirve |
|---|---|---|---|
| Arranque de la serie | ep. 1, 00:13 | 「（雨の音）」: **lluvia** sobre la ciudad. Dos policías se quejan por holo-llamada: «It just had to fucking rain…» (00:58) | Luz y tono del objeto bajo la lluvia |
| La lavadora sin saldo | ep. 1, 04:15 | «Cycle suspended due to insufficient funds…»: la lavadora de David **se para por falta de dinero** | Las máquinas de Night City funcionan **con saldo**, como una recreativa |
| «Wash cycle complete…» | ep. 2, 06:16 | La lavadora termina; David, expulsado, está hundido | Máquina doméstica con pantalla |
| Parte del tiempo en la radio | ep. 6, 03:58 | 「（ラジオ：お天気キャスター）」: «lluvia fuerte en la costa, Santo Domingo y Westbrook, de medianoche al amanecer» | La lluvia es parte del mundo, con horario |
| Anuncio de radio | ep. 6, 02:17 | «Wanna know where all the legends of Night City play?» (ナイトシティの伝説がこぞって集まる場所を知ってるか？) | **La frase perfecta para #a-que-juegas** |
| La última pelea de Maine | ep. 6, 18:25 | 「（雨の音）」 Maine y Dorio rodeados, bajo la lluvia | Lluvia dramática (no para un canal alegre) |

### 2.2 Armar el equipo (el «quién se apunta»)

| Escena | Ep. y minuto | Qué se dice | Para qué sirve |
|---|---|---|---|
| Lucy recluta a David en el tren | ep. 2, 08:23 | «Crazy idea. How about we work together?» | Invitar a jugar |
| Se presentan | ep. 2, 09:31 | «Call me Lucy.» / «David.» | Presentarse |
| «Edgerunners?» | ep. 2, 17:01 | «It's another word for cyberpunk. It's who you wanna be, right?» | Saber qué quiere ser cada uno |
| «Seríamos un buen equipo» | ep. 2, 21:47 | Lucy: «I think we'd make a good team.» | Hacer grupo |
| David pide su oportunidad | ep. 3, 05:01 | «Just give me a chance.» «You take me out on a job.» | Pedir entrar en la partida |
| Maine acepta | ep. 3, 05:24 | «Okay, kid. You get one chance.» | El jefe de grupo dice sí |
| El grupo en la furgoneta | ep. 3, 08:15 | Maine: «This one here is Kiwi. And Dorio and Pilar, you've met.» | Presentar al equipo |
| El reparto justo | ep. 3, 18:02 | Maine: «Everybody gets a fair shake. Only way I operate.» | Reglas del grupo |
| «Bienvenido al equipo» | ep. 3, 17:07 | «Sure. Welcome to the crew.» | Dar la bienvenida |
| Rebecca se presenta | ep. 3, 21:24 | 「レベッカ」: «I'm Rebecca. I heard you're joining up on Maine's crew?» | Rebecca saluda al nuevo |
| Reunión de urgencia | ep. 9, 05:23 | Rebecca: 「ずいぶん急な招集じゃん」 («vaya convocatoria de repente») | Convocar partida |
| «El trabajo más grande» | ep. 9, 05:27 | David: «Faraday's come through. It's our biggest gig yet.» | Anunciar partida |
| «Huge risk, huge return» | ep. 9, 05:32 | David: «Turn back now if you're not ready to face the heat.» | Advertir antes de empezar |
| «Parte igual del botín» | ep. 9, 23:19 | David: 「分け前はフェアにやる それが俺の流儀だ」 «Equal share of the pot. That's my style.» Los dos (「（２人）フッフフフ」, se ríen) y contestan: «Alright, buddy. Onwards to hell.» 「つきあってやるよ 地獄までな」 (el subtítulo no dice cuál de los dos habla ⚠️) | **Apuntarse a la partida** |

### 2.3 La fiesta y el bar (después de la partida)

| Escena | Ep. y minuto | Qué pasa | Para qué sirve |
|---|---|---|---|
| Celebración tras el primer golpe | ep. 3, 20:38 | Maine: «We're celebrating tonight.» | Contar la partida después |
| Rebecca en la fiesta | ep. 3, 21:18 | «Oh, right. You were at the bar.» «You like my performance?» | Rebecca en su salsa |
| Rebecca saca a bailar | ep. 7, 09:06 | «Why the long face, David?! Stop flirting with the nagging hag and dance with me!» | Animar al grupo |
| Llamada al Afterlife | ep. 7, 11:27 | Kiwi: 「あんた アフターライフに今から来られる？」 («¿puedes venir al Afterlife ahora?») | El bar de los mercenarios: **donde se arma el trabajo** |
| Faraday en el Afterlife | ep. 7, 11:55 | «I am Faraday.» «Let me buy you a drink.» | El que reparte los encargos |
| Rebecca: «¿damos un paseo?» | ep. 8, 12:15 | «David!… Wanna take a walk?» 「なあ ちっと歩こうぜ」 | Invitar |

### 2.4 La luna (el sueño de Lucy)

| Escena | Ep. y minuto | Qué pasa | Para qué sirve |
|---|---|---|---|
| El BD de la luna | ep. 2, 19:24 | David: «Whoa! Check the resolution on this! I can feel the fucking sun!» | Emoción de estrenar un juego |
| «Primera vez que se lo enseño a alguien» | ep. 2, 21:28 | Lucy: «First time I've ever shown anyone this.» | Compartir captura |
| La promesa | ep. 4, 21:54 | David: 「俺が君を月に連れていくよ 約束する」 «I'll take you to the moon! I promise!» | Momento más citado |
| «Te recuerdan por cómo mueres» | ep. 4, 21:29 | Lucy: 「この世界で名を残す方法は どう生きるかじゃない どう死ぬかよ」 | Frase de la serie (no para este canal) |
| Las estrellas | ep. 7, 16:14 | David: «Whoa! Look at the stars!» Lucy: «The city looks like a cage made of lights from here.» (16:50) | Night City de noche desde fuera |
| 250.000 a la luna | ep. 8, 07:26 | David ve un anuncio: «250K to the Moon… cheaper than I thought.» | El precio del sueño |
| Final en la luna | ep. 10, 23:56 | 「ようこそ 月面散歩ツアーへ」 «Welcome to the tour of the moon!» Lucy sola. 24:29: «I can feel the fucking sun!» (eco del ep. 2) | Final. **No usar en la lámina**: es el golpe triste |

### 2.5 Las frases que todo el mundo conoce (con su minuto)

| Frase (inglés de Netflix) | Japonés | Quién | Ep. y minuto |
|---|---|---|---|
| «I want you to work hard, rise up, and get to the top floor of Arasaka Tower!» | — | Gloria (madre de David) | ep. 1, 11:43 (y eco en ep. 10, 07:35) |
| «It's high time I chromed up.» | — | David | ep. 1, 22:22 |
| «Edgerunners? It's another word for cyberpunk.» | — | Lucy | ep. 2, 17:01 |
| «You don't make a name as a cyberpunk by how you live. You're remembered by how you die.» | どう生きるかじゃない どう死ぬかよ | Lucy | ep. 4, 21:29 |
| «I'll take you to the moon! I promise!» | 俺が君を月に連れていくよ 約束する | David | ep. 4, 21:54 |
| «David… Tell me I can do it.» / «I believe in you, Lucy.» | — | Lucy / David | ep. 6, 06:36 y 07:12 |
| «Fast is what you do, remember? Keep running.» | — | Maine, al morir | ep. 6, 22:32 |
| «Puppy-dog eyes! Knew I'm a sucker for the vulnerable, didn't ya?!» | — | Rebecca | ep. 9, 07:49 |
| «You're the only one I watch that closely, you know.» | まっ あーしが そんだけ… | Rebecca | ep. 8, 13:03 |
| «Never trust a soul in Night City.» | ナイトシティでは人を信じるな | Kiwi (lo enseñó a Lucy; lo repite en ep. 8, 10:47 y ep. 9, 04:51) | ep. 9, 04:51 |
| «You could say I'm special.» / «Well so the fuck am I!» | — | Adam Smasher / David | ep. 10, 17:10 |
| «Sorry. Wish we could go to the moon together.» | 月 一緒に行けなくて ごめんな | David (a través de Falco) | ep. 10, 22:25 |

### 2.6 Segunda pasada · lo que se ve en el fotograma

Mirado con `fotogramas.py` sobre los episodios de
[Internet Archive](https://archive.org/details/cyberpunk_edgerunners_01_360)
(360p) y el [tráiler VOSE de Dailymotion](https://www.dailymotion.com/video/x8ct6i8).
Todo ✅ visto.

| Ep. y minuto | Qué se ve | Para qué sirve |
|---|---|---|
| ep. 1, 0:08-0:56 | Tras el logo de Netflix entra directo la **pelea bajo la lluvia**: ciberpsicópata con visor rojo golpea un coche de policía; sirenas rojo y azul; charcos que reflejan el neón; «BLAM» amarillas de las trazadoras (0:48-0:52) | **El ambiente de la recreativa bajo la lluvia** |
| ep. 1, 2:52-3:16 | Persecución con fondo verde tóxico y sangre roja a contraluz | Contraste de un solo acento |
| ep. 1, 3:16-3:58 | Aviso en un holo-teléfono azul: «ripperdoctors, cybercyphers don't rat» | Pantalla del mundo con texto |
| ep. 1, 4:04-4:16 | David despierta en su cuarto: plano cenital, tonos ocre | Interior de H4 |
| ep. 3, 0:00-1:36 | **El opening real**: paneles planos verde ácido, magenta, violeta y crema; créditos en sans condensada inclinada; un gólem verde gigante (0:56-1:04); «TRIGGER» (1:20) | Tipografía y color del opening (§6) |
| ep. 3, 4:55-8:20 | Interrogatorio y braindance con **filtro verde militar** y tinta roja para las heridas | Filtro de un solo tono (punto 18) |
| ep. 4, 21:20-21:58 | **La promesa de la luna** («I'll take you to the moon! I promise!», 21:54): filtro entero **verde de visión nocturna**; Lucy de perfil llorando (21:34-21:36); un fogonazo vertical blanco (21:48); Lucy con la mano en la cabeza | Escena triste: sirve la pose, no el filtro |
| ep. 4, 22:40-23:16 | **El ending** «Let You Down»: pasillo industrial verde oscuro, silueta de espaldas a contraluz, créditos blancos condensados sobre negro | Créditos y luz del ending |
| ep. 6, 22:10-22:48 | **La muerte de Maine**: su visor se agrieta como cristal verde y violeta; Maine y Dorio de espaldas en las Badlands (22:22); David con la capucha, ojos muy abiertos (22:26-22:36); fogonazo blanco y dorado (22:44) al oír «Fast is what you do, remember? Keep running» | Trigger **no muestra el golpe**, sólo el antes y el después |
| tráiler, 0:28-2:40 | Subtítulos en **español de España** incrustados: «Bienvenidos a Night City» (0:28), «Llévalo al límite» (0:48), «Ese cromo está a otro nivel» (1:28), «¡Dámela tú, rata!» (2:24), «Es que eres adorable» (2:40); logo amarillo neón (2:24) | Minutos del tráiler. **No es doblaje latino** |

---

## 3 · Arte oficial y referencias visuales

### 3.1 Las hojas de contacto

Hay **dos juegos de hojas**. Los números se citan así:

- **W** + número = hojas de la **wiki de Fandom** (`cyberpunk`), hechas con
  `herramientas/investigar_serie.py`. Son las **3 hojas de
  `hojas/`** (`hoja_01.jpg` = W1-W48, `hoja_02.jpg` = W49-W96,
  `hoja_03.jpg` = W97-W128). Tamaños reales medidos por la herramienta.
  Para bajar un original: `python herramientas/investigar_serie.py
  --bajar cyberpunk-edgerunners 26 47` (el índice con la URL de cada
  número está en `herramientas/referencias/cyberpunk-edgerunners/indice.json`;
  las mejores también en `referencias.json`).
- **G** + número = 3 hojas extra montadas con imágenes que fans subieron
  a **GitHub** (renders sobre negro, fotogramas, capturas del juego).
  Están en `herramientas/referencias/cyberpunk-edgerunners/github_hoja_0X.jpg`
  (G01-G72) con su índice `github_indice.json`. **No se suben** al
  repositorio: sirven en esta máquina y sus enlaces van en
  `referencias.json`.
- **Todo es sólo para mirar.** El arte es de CD PROJEKT RED, Studio
  Trigger y Netflix. Para la lámina: original en alta y `v3/integrar.py`.

### 3.2 Lo más útil de las hojas W (wiki)

| W | Qué es | Tamaño | Pose / uso |
|---|---|---|---|
| **W2** | Ilustración del **2.º aniversario** (13-sep-2024) de Yoshinari: todo el reparto corriendo en una nube, fondo verde lima | 3840×2160 | Grupo en acción. **La de «todos se apuntan»** |
| **W3** | «Summer Vibes»: Rebecca (con Guts al hombro), David y Lucy en bañador en una azotea de noche | 3840×2160 | Grupo relajado, luz cian |
| **W4-W7** | **Guía oficial de cosplay de Lucy** (cara, peinado, puerto de buceo en la nuca, cuerpo entero de frente y espalda, accesorios) | 3840×2160 | **La mejor hoja de modelo de Lucy** (ver §16) |
| W8 | Detalle del tatuaje del muslo de Rebecca | 2560×1440 | Vestuario |
| **W9** | Rebecca disparando **con dos armas** (Guts y pistola) | 2560×1440 | Acción, «celebrar a tiros» |
| W10 | Cartel de la serie con Lucy («Sept 13, Netflix») | 1500×2222 | Presentar |
| W11, W24 | **Arte conceptual de Rebecca** (giro de cuerpo; diseño de tatuajes) | 1448×2048 / 1634×1612 | Proporciones |
| **W12-W22, W94, W95, W110** | **Cartones de cuenta atrás** («XX days to go!»), cada uno de un artista distinto, del 13 al 0 | ~1430×2048 | Estilos muy variados: manga en blanco y negro (W21 Maine), **Rebecca como maqueta de plástico en su bebedero** (W21: «4 days»), Kiwi con una hiena (W18) |
| W23, W105 | Carteles de Trigger: Lucy y David sobre verde | 1383×2048 / 960×1200 | Key visual |
| W25, W33 | Kiwi de pie; **hoja de diseño de su máscara** | 1266×2048 / 1471×1451 | Kiwi |
| **W26-W32** | **Carteles de personaje sobre amarillo** (firmados «by Yoshiyuki Kaneko» en la wiki ✅: **son dos personas**; Yuto Kaneko diseñó a Rebecca y Dorio, Yoshiyuki Kaneko hizo arte del opening y estos carteles, ver [Sakugabooru](https://www.sakugabooru.com/post/show/204453) e [IMDb](https://www.imdb.com/name/nm5608331/)): David, Kiwi, Lucy, Maine, Rebecca, Dorio, Pilar | 1280×1811 | **Las poses más vivas**: ver §15 |
| W37 | Arte de los Juegos Olímpicos de 2024: el reparto nadando y corriendo | 1920×1080 | Humor, deporte |
| W39 | Arte del Blu-ray («coming in 2025»), David con el ciberesqueleto | 1920×1080 | — |
| W46 | **El equipo en fila** (tráiler, junio de 2022) | 1920×1080 | Presentar al grupo |
| **W47, W60, W76, W78, W80, W85, W87** | **Rótulos de nombre**: katakana arriba y el nombre en letras gruesas lima (DAVID, KIWI, LUCY, MAINE, REBECCA, DORIO, PILAR). Salen del vídeo *Inside Look #2* | 1920×1080 | **Tipografía propia** (ver §6) |
| W49 | BD de la luna: David y Lucy en el **rover lunar** (ep. 2) | 1920×1080 | «Probar un juego» |
| W52-W54 | Lucy de niña en Arasaka (ep. 7) | 1920×1080 | Pasado |
| W57 | Kiwi hackeando, cinta de datos verde | 1920×1080 | Interfaz |
| W65, W66, W79 | Rebecca con David (ep. 4): práctica de tiro, el paquete de brazos, guiño con la pistola | 1920×1080 | Rebecca simpática |
| W69-W71 | Tráiler NSFW: Rebecca con Guts | ~1900×1080 | Acción |
| **W75** | **El equipo en un reservado del bar**, con bebidas (vídeo de «Let You Down») | 1920×1080 | «Después de la partida» |
| W77 | Lucy con traje espacial en la luna (ep. 10) | 1920×1080 | Final; no usar |
| W91, W99 | El coche de Falco (Chevillon Emperor) | 1672×1080 | Objeto |
| W93 | **Arte conceptual de David**: giro de cuerpo y 6 versiones de la chaqueta | 1665×1022 | Vestuario |
| W101 | Dibujo de agradecimiento «おつかれさまでした» (buen trabajo a todos) de Chiharu Kataoka, 20-ene-2023 | 1004×1434 | Grupo, tono cariñoso |
| W103, W106, W108, W124-W126 | **Manga *Edgerunners MADNESS*** (Rebecca y Pilar de jóvenes), con globos y onomatopeyas | 900-1225 px | **El globo de manga oficial** (ver §7) |
| W104 | Vinilo de la banda sonora 1: Lucy sentada en el alféizar de un tren, luz violeta | 1123×1123 | Pose de «pensar» |
| W111 | Lucy con Songbird (cruce con *Phantom Liberty*) | 832×1200 | — |
| W115 | Rebecca con chicle, fondo amarillo (autor «Nirak» ⚠️, posible colaboración) | 1000×803 | Pose |
| **W116** | Arte de la **lotería online 2024**: David, Lucy y Rebecca **tirados en un sofá**, David con lata, Rebecca guiña y saluda; marco amarillo de interfaz | 1000×800 | **Pasar el rato: el tono exacto de #a-que-juegas** |
| **W117** | **El Afterlife** por dentro: barra con luz verde, Rebecca y Kiwi | 1225×605 | Sitio |
| W118 | «Slice of Life», lienzo oficial: calle de noche, neón «Blue Moon ブルームーン», David junto al coche | 1015×716 | Fondo |
| **W127** | Vinilo 2: **David con un radiocasete**, el equipo alrededor en picado | 733×731 | Presentar |

### 3.3 Lo útil de las hojas G (GitHub, no se suben)

| G | Qué es | Pose / uso |
|---|---|---|
| G01, G05, G09, G13, G16, G18, G20 | **Renders sobre negro** (David, Lucy, Rebecca, Maine, Kiwi, Falco, Pilar) | Recorte limpio. **Rebecca G09: manos en los bolsillos**, sonrisa |
| G06 | Lucy sobre magenta `#F246B3`, brazo arriba | Póster |
| G10 | **Rebecca sobre lima `#BAF812`, agachada, apunta al espectador** | **Retar, animar** |
| G25 = W46 | El equipo en fila, luz naranja de noche | Presentar |
| **G26** | **El equipo de espaldas**; la chaqueta de David con su emblema verde | «Nos vamos de partida» |
| G27 = W2 | Ilustración del aniversario | Grupo |
| G28, G48 | Key visual de junio de 2022 | — |
| G29-G32 | La luna y el beso | Romántico, no para este canal |
| G33 | **Rebecca con brazos de gorila, puños arriba, riendo** | **Celebrar** |
| G41 | Lucy escanea en el tren con su HUD rojo | Interfaz |
| G42 | BD de la luna: tumbados con la corona | «Estrenar juego» |
| G45 | El título EDGERUNNERS en letras rotas | Tipografía |
| G46 | AV del Trauma Team sobre un tren amarillo | Metro |
| G49-G55 | Barrios del **juego**: Arroyo, Japantown, Kabuki, Watson | Fondos |
| G56-G58 | Panorámicas de Night City | Fondos |

Fuentes GitHub: [AlexandreDresch/EdgeRunners](https://github.com/AlexandreDresch/EdgeRunners),
[JJaaGGo/PopArt-webPage…](https://github.com/JJaaGGo/PopArt-webPage-Cyberpunk-Edgerunners-Theme),
[juletopi/Pagina_Cyberpunk-Edgerunners](https://github.com/juletopi/Pagina_Cyberpunk-Edgerunners),
[melendezdev/cyberpunk-edgerunners-project](https://github.com/melendezdev/cyberpunk-edgerunners-project),
[Ludobico/Project-Rebecca](https://github.com/Ludobico/Project-Rebecca),
[LeahJKH/Cyberpunk-Edgerunners-API](https://github.com/LeahJKH/Cyberpunk-Edgerunners-API),
[SHREE167/cyberpunk-edgerunners-site](https://github.com/SHREE167/cyberpunk-edgerunners-site),
[Manadrah/…moon-lively-wallpaper](https://github.com/Manadrah/cyberpunk-edgerunners-moon-lively-wallpaper).

### 3.4 Otras piezas oficiales (fuera de las hojas)

| Qué | Dónde | Estado |
|---|---|---|
| **Key visual** de junio de 2022 | [Famitsu](https://www.famitsu.com/news/202206/09264322.html) + G28 | ✅ |
| Nueva key visual de David y Lucy por **Yoh Yoshinari** (吉成曜) | [Comic Natalie](https://natalie.mu/comic/news/480860) | ✅ |
| Ilustración del 2.º aniversario | [X de CD PROJEKT RED Japan](https://x.com/CDPRJP/status/1834532480126161225) + W2 | ✅ |
| **Litografía de aniversario** de Trigger (casi un metro de ancho) | [CD PROJEKT RED Gear Store](https://gear.cdprojektred.com/products/cyberpunk-edgerunners-anniversary-lithograph-by-studio-trigger) | ✅ ficha oficial revisitada en la 2.ª pasada, foto 600×900 |
| Vídeo: **Yoshinari dibujando a David y Lucy** (5:45, 10-oct-2022) | [Netflix Japan](https://www.youtube.com/watch?v=9lQamD4CfBU) | ✅ |
| Dibujo en directo de Yoshinari (17-oct-2022) | [GAME Watch](https://game.watch.impress.co.jp/docs/news/1447266.html) | ⚠️ |
| **Blu-ray BOX** japonés (28-may-2025) | [4Gamer](https://www.4gamer.net/games/189/G018964/20241213102/), [HMV](https://www.hmv.co.jp/news/article/241213145/) | ✅ |
| Blu-ray de EE. UU. (Aniplex, 28-oct-2025) | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Cyberpunk:_Edgerunners) | ⚠️ |
| Réplica oficial de **Guts** a la venta en la tienda de IGN (sep. 2026) | [r/Edgerunners](https://reddit.com/r/Edgerunners) (dos hilos, 149 y 128 votos) | ⚠️ |

### 3.5 El artbook (la mejor fuente de poses y sitios)

**THE ART OF CYBERPUNK: EDGERUNNERS** ✅
- 318 páginas a todo color. **Portada nueva de Yoh Yoshinari.**
- Bocetos, **diseños de personaje**, **fondos**, **objetos** (props),
  storyboards del opening y el ending, arte promocional.
- 10 capítulos, cada uno con un comentario del director **Hiroyuki
  Imaishi**. Bocetos de Imaishi, Yoshinari y Yuto Kaneko.
- Reimpresión: reserva del 22 de mayo al 4 de junio de 2026 (tienda de
  Trigger).
- Fuentes: [TRIGGER en X](https://x.com/trigger_inc/status/2061976216496926890),
  [CDJapan](https://www.cdjapan.co.jp/product/NEODAI-296187),
  [Denfaminicogamer](https://news.denfaminicogamer.jp/news/2602272m),
  [Artbook Collector](https://www.artbookcollector.com/post/animation-studio-trigger-announce-the-art-of-cyberpunk-edgerunners).

### 3.6 Lo que dijo el equipo sobre el diseño

- **Director**: Hiroyuki Imaishi (今石洋之). **Director creativo**:
  Hiromi Wakabayashi. **Personajes y jefe de animación**: Yoh Yoshinari.
  **Guion**: Yoshiki Usa y Masahiko Otsuka. **Música**: Akira Yamaoka.
  **Showrunner** (CD PROJEKT RED): Rafał Jaki ✅ (descripción oficial
  del vídeo [Inside Look](https://www.youtube.com/watch?v=zxapZWv4pNs) y
  [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Cyberpunk:_Edgerunners)).
- **Los fondos salen del propio juego**: Trigger pidió un archivo para
  **pasear libremente por la ciudad del juego**, hizo fotos de todos sus
  rincones y pintó los fondos encima. «Hay escenas que reconocerán los
  jugadores» ✅ ([Inside Look #2](https://www.youtube.com/watch?v=D6ia1wjO7sg),
  **2:05 a 2:39**). Para un canal de juegos, esto es oro: **un fondo de la
  serie es un sitio que se puede visitar jugando**.
- **David**: diseño «flexible», un chico normal que va cambiando con la
  violencia (Inside Look #2, **2:49-3:36**) ✅.
- **Lucy** fue lo más difícil: *femme fatale* pero **mona**, con encanto
  de anime (Inside Look #2, **3:47-4:10**) ✅.
- CD PROJEKT RED: «cada fotograma es una pintura»; «los tonos son los del
  juego, pero con **muchos más colores**» ([Inside Look](https://www.youtube.com/watch?v=zxapZWv4pNs),
  **3:07-3:28**) ✅. A Trigger le encantaron los **peces holográficos** del
  juego y salen igual en la serie (**2:51**) ✅.
- **Rebecca** la diseñaron Imaishi y Yuto Kaneko; desde el ep. 7 le dieron
  más peso en la historia ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Rebecca_(Cyberpunk:_Edgerunners))).
  Imaishi a Famitsu: Rebecca es **pequeña y distinta** para que se vea de
  un vistazo que **Lucy es la heroína**; CD PROJEKT temía que una chica
  tan «mona» rompiera el mundo; Trigger defendió que su ternura hacía
  **más fuerte la acción** ✅ ([Famitsu](https://www.famitsu.com/news/202210/15278443.html),
  [WebNewtype](https://webnewtype.com/report/staff/1104956.html)).
- Las **proporciones exageradas** (brazos de Pilar, cuerpos de Maine y
  Dorio) son a propósito, para distinguir a cada uno (Famitsu) ✅.
- Productores: [AUTOMATON](https://automaton-media.com/articles/interviewsjp/20220914-219010/),
  [GAME Watch](https://game.watch.impress.co.jp/docs/interview/1439037.html).
  Imaishi en un AMA de Reddit
  ([resumen](https://www.bubbleblabber.com/2022/12/reddit-ama-recap-hiroyuki-imaishi/)).
  Entrevista a Imaishi de julio de 2026 en
  [Tonari no Young Jump](https://tonarinoyj.jp/article/entry/2026/07/23/000000) ⚠️ no leída.

### 3.7 Lo que falta ⚠️
- No vi el **artbook** por dentro.
- **Fotogramas 1080p con minuto**: los minutos están en §2. En la 2.ª
  pasada se miraron en **360p** (Internet Archive, §2.6); la captura en
  1080p sigue pendiente en Netflix ⚠️.

### 3.8 Segunda pasada · arte oficial confirmado

- **El manga *Cyberpunk: Edgerunners MADNESS*** (hojas W103, W106, W108,
  W124-W126) es oficial ✅: sale en *Comic Alive+* de KADOKAWA desde el
  13-dic-2024, dibujo de **Asano** (de *BNA*) y guion de **Bartosz
  Sztybor** (CD PROJEKT RED); Dark Horse lo publica en inglés (tomo 1,
  feb-2026) ([Kadokawa Global](https://group.kadokawa.co.jp/global/information/promotional_topics/2024121301_en.html),
  [Anime News Network](https://www.animenewsnetwork.com/news/2024-12-13/cyberpunk-edgerunners-madness-manga-launches-dark-horse-to-release-in-print-in-english/.218983),
  [Dark Horse](https://www.darkhorse.com/books/3015-353/cyberpunk-edgerunners-madness-volume-1-tpb/)).
  Medidas por la API: W124 914×634, W125 702×816, W126 932×611.
- **Los dos Kaneko** ✅: Yuto Kaneko (diseño de Rebecca y Dorio) y
  Yoshiyuki Kaneko (arte del opening y carteles amarillos) son personas
  distintas ([Sakugabooru](https://www.sakugabooru.com/post/show/204453),
  [TheGamer](https://www.thegamer.com/cyberpunk-edgerunners-rebecca-age-character-design/)).
- **La litografía de aniversario** de Trigger, revisitada en la
  [tienda oficial](https://gear.cdprojektred.com/products/cyberpunk-edgerunners-anniversary-lithograph-by-studio-trigger):
  foto medida 600×900 ✅.
- El diseñador **Yoh Yoshinari** cuidó que Lucy **no se pareciera a Motoko
  Kusanagi** (*Ghost in the Shell*) ✅ ([wiki: Lucy](https://cyberpunk.fandom.com/wiki/Lucyna_Kushinada),
  cita el vídeo «Quick Draw» de Netflix Anime).

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 La recreativa en 3D (para Blender)

Licencias **comprobadas en la API de Sketchfab** (24-sep-2026). Todas
se pueden descargar. «CC Attribution» = CC BY: hay que poner el crédito.

| Modelo | Autor | Licencia | Caras | Por qué |
|---|---|---|---|---|
| **Rusty Japanese Arcade** | Hawtor Studio | CC BY ✅ | 4.206 | **La más Night City**: oxidada, sucia, luz violeta arriba y rótulo japonés. [Enlace](https://sketchfab.com/3d-models/none-2938ae13a77c46e8afabb41eba18e699) |
| **Old Arcade Cabinets** (varias máquinas gastadas) | Hrvoje Wächter | CC BY ✅ | 144.682 | Para una **fila de recreativas** en un callejón. [Enlace](https://sketchfab.com/3d-models/none-fc863ca4e3f94b4c8729f091e36238cf) |
| **arcade machine** (neón, rótulo «アーケード») | Logotyp | CC BY ✅ | 12.894 | Neón magenta y cian ya puesto. [Enlace](https://sketchfab.com/3d-models/none-a914bf3651e3496ea708dc0782eca212) |
| Cyberpunk Arcade Machine | Zlat | CC BY ✅ | 1.616 | Baja resolución; **su pantalla trae un juego de Nintendo**: cambiarla. [Enlace](https://sketchfab.com/3d-models/none-5a2ec1fb48be42efa91f44f4de90201e) |
| Arcade Cabinet .glb (v0.9) FREE Low Poly | Lady Lion Studios | CC BY ✅ | 8.050 | Sencilla, hecha en Blender. [Enlace](https://sketchfab.com/3d-models/arcade-cabinet-glb-v09-free-low-poly-5685d09900dc4393b245f6e924457fc7) |
| Racing Arcade .glb (v0.9) FREE Low Poly | Lady Lion Studios | CC BY ✅ | 16.364 | Máquina de carreras con asiento (para dos jugadores). [Enlace](https://sketchfab.com/3d-models/racing-arcade-glb-v09-free-low-poly-48f608d9414f43caa6599cbd94681087) |
| Arcade Game Machine (Low Poly) | game_travel | CC BY ✅ | 2.582 | [Enlace](https://sketchfab.com/3d-models/arcade-game-machine-low-poly-63a6cb852c5d4fe596b62847c66c2b17) |

**Evitar**: «Blade Runner Arcade Cabinet» (Glowbox 3D, CC BY, pero lleva
una marca ajena) y cualquier pantalla con juegos reales de otras marcas.

Crédito de ejemplo: «Rusty Japanese Arcade» by Hawtor Studio, licensed
under CC BY 4.0, sketchfab.com.

**Neón y rótulos** (CC BY ✅, API):
- [Cyberpunk animated japanese LED neon sign](https://sketchfab.com/3d-models/none-fab087c62fc3459a8b7664757d980c28)
  · YD Visual (rótulo vertical 居酒屋, cian con marco naranja).
- [Neon Signs](https://sketchfab.com/3d-models/none-307e887d740649f88fbc77b061f3a742)
  · Shalmon (pared entera de neones asiáticos; pesado, 355k caras).
- [Taiwan style Signboard (lowpoly)](https://sketchfab.com/3d-models/none-7eeac0582f7746ffafcdf1091f882a5d)
  · Solarliu.
- Fondo de edificios: [Low Poly Night City Building Skyline](https://sketchfab.com/3d-models/none-b0035b8713b048bb8ddf311ee67c28c8)
  y [Asian Themed Low Poly Night City Buildings](https://sketchfab.com/3d-models/none-9f0343aff4814b758dc6e905aba5b5e0)
  · 99.Miles (CC BY).
- «Cyberpunk Assets» de Amanda Vergara es **CC BY-SA** (obliga a
  compartir igual): mejor no.

### 4.2 Objetos de la serie hechos por fans (Sketchfab, API)

| Modelo | Autor | Licencia |
|---|---|---|
| [**Guts**, la escopeta de Rebecca](https://sketchfab.com/3d-models/guts-c047b8e543ba4323969cd72950c34f62) | charlloyd | **CC BY** ✅ (3.806 caras) |
| [David Martinez](https://sketchfab.com/3d-models/david-martinez-cyberpunk-edgerunners-0105aad132d04217ad2371da44b51f7a) | Marinammp | CC BY ✅ |
| [David Martinez](https://sketchfab.com/3d-models/david-martinez-4fbd003f3a1748fe89e30d6a2fef9047) | Xetirano | **CC BY-NC-SA** (no comercial) |
| [Rebecca](https://sketchfab.com/3d-models/rebecca-cyberpunk-edgerunners-5dd3f0470b014ee1bf6900d8a664652e) | tukuru_kunn | **sin licencia, no descargable** |
| [LowPoly Rebecca](https://sketchfab.com/3d-models/lowpoly-rebecca-cyberpunk-edgerunners-382c37b4f1c3435e8155b08d56222ce9) | KelpieBoye | CC BY ✅ |
| [Escopeta de Rebecca (STL)](https://www.printables.com/model/302035-rebeccas-shotgun-from-cyberpunk-edgerunners/related) | ReProps | ⚠️ |

Regla: **los personajes NO se meten en 3D** en la lámina (se recortan de
fotogramas con `v3/integrar.py`). Los modelos de personaje sirven para
probar luz o pose. La escopeta **Guts** sí puede ir en 3D, apoyada en la
recreativa (es un objeto).

Maqueta oficial de referencia: **Prime 1 Studio** hizo una figura que
recrea **el Afterlife** con personajes de la serie
([entrevista en Sculptors Lab](http://sculptors.jp/topics/25722)) ⚠️.

### 4.3 Luz y texturas libres (CC0)

- **HDRI de Poly Haven** (CC0, comprobado en su API): para iluminar la
  recreativa con luz de ciudad de noche:
  [Shanghai Bund](https://polyhaven.com/a/shanghai_bund) (neones y
  rascacielos), [Metro: Noord](https://polyhaven.com/a/metro_noord)
  (**estación de metro**, para una recreativa del NCART),
  [Modern Buildings Night](https://polyhaven.com/a/modern_buildings_night),
  [Street Lamp](https://polyhaven.com/a/street_lamp),
  [Night Bridge](https://polyhaven.com/a/night_bridge),
  [Rooftop Night](https://polyhaven.com/a/rooftop_night),
  [Warm Bar](https://polyhaven.com/a/warm_bar) (para el Afterlife).
- **Asfalto** (Poly Haven, CC0): [Asphalt 04](https://polyhaven.com/a/asphalt_04),
  [Asphalt 06](https://polyhaven.com/a/asphalt_06),
  [Road Damaged](https://polyhaven.com/a/road_damaged).
- **ambientCG** (CC0, API): asfalto con charcos **Asphalt025B / 025C**,
  **Asphalt024C**; chapa pintada **PaintedMetal004 / 006 / 016**; chapa
  ondulada **CorrugatedSteel005** (para el mueble de la recreativa y las
  persianas). Enlace tipo: `https://ambientcg.com/view?id=Asphalt025C`.

### 4.4 Fan art 2D (mirar, nunca pegar)

- **Reddit** (archivo de Arctic Shift): Rebecca arrasa también en fan
  art. En r/cyberpunkgame, sus hilos más votados de 2026: «GTA 6 Cover
  Rebecca (by @ttsuki_ocha)» (8.111 votos), «Rebecca Fanart Life Size
  Print…» (7.269), «Rebecca from Edgerunners ♡ @cvber01» (7.062).
  En r/Edgerunners: «Beach Day Rebecca» (2.028), «Rebecca's bakery by
  [滑铲式]» (1.294), «Rebecca vs. Adam Smasher (Sol-Sama_D2)» (1.030).
- **Pixiv**: enciclopedia de Rebecca en
  [dic.pixiv.net](https://dic.pixiv.net/en/a/Rebecca%20(Edgerunners)).
- **Know Your Meme**: galería de Rebecca con el fan art viral
  ([imágenes](https://knowyourmeme.com/memes/rebecca-edgerunners-character/photos));
  el más compartido la dibuja **con dos pistolas** y cara de «duende
  asesino».
- **Wallpaper Engine**: fondos animados 4K
  ([ejemplo](https://steamcommunity.com/sharedfiles/filedetails/?id=3421423611)).
- Webs de fondos (mezclan oficial y fan; **no son fuente final**):
  [Alpha Coders 4K](https://alphacoders.com/cyberpunk-edgerunners-4k-wallpapers),
  [4kwallpapers](https://4kwallpapers.com/cyberpunk:-edgerunners),
  [WallpaperFlare](https://www.wallpaperflare.com/search?wallpaper=Cyberpunk%3A+edgerunners).
- Fondo animado de la luna hecho por un fan, en GitHub:
  [Manadrah/…moon-lively-wallpaper](https://github.com/Manadrah/cyberpunk-edgerunners-moon-lively-wallpaper)
  (miniatura 3840×2160).

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie (y dónde están en el juego)

Trigger pintó los fondos **sobre fotos tomadas dentro del juego**
(Inside Look #2, 2:15 ✅). Así que casi todo sitio de la serie **existe en
*Cyberpunk 2077*** y un jugador lo reconoce.

| Sitio | En la serie | En el juego | Estado |
|---|---|---|---|
| **Megaedificio H4**, Arroyo (Santo Domingo) | Casa de David y Gloria; la lavadora sin saldo (ep. 1, 04:15) | Metro: Wollesen Street; en un callejón debajo hay **el símbolo de Edgerunners** | ✅ ([VULKK](https://vulkk.com/2022/09/17/all-locations-from-edgerunners-in-cyberpunk2077/), [wiki: David](https://cyberpunk.fandom.com/wiki/David_Martinez)) |
| **Piso de Lucy**, Kabuki (Watson) | Bañera de hielo para bucear en la red; BD de la luna (ep. 2, 19:24) | Viaje rápido a Sutter St., edificio de cristal | ✅ (VULKK, [thegamer](https://www.thegamer.com/cyberpunk-2077-edgerunners-references/)) |
| **Piso de Kiwi**, Kabuki | — | Sutter St., ascensor a la planta 13 | ⚠️ una fuente |
| **Tren del NCART** (metro elevado) | Lucy roba chips; conoce a David (ep. 2, 07:46) | Sale en Edgerunners según su ficha de la [wiki](https://cyberpunk.fandom.com/wiki/Night_City_Area_Rapid_Transit) (`appears_other = EDGE`). Lo del parche 2.1 es del juego, no de la serie | ✅ subtítulo + wiki |
| **Afterlife** (Little China, Watson): bar de mercenarios en una antigua morgue; sirve **bebidas con nombre de leyendas muertas** | Kiwi cita a David; aparece Faraday (ep. 7, 11:27-11:55) | Existe; tiene la bebida **«The David Martinez»** | ✅ ([wiki: Afterlife](https://cyberpunk.fandom.com/wiki/Afterlife), [Game8](https://game8.co/games/Cyberpunk-2077/archives/Edgerunners-Items)) |
| **Clínica de Doc** (ripperdoc) | Le pone el Sandevistan (ep. 2, 00:11) | En **Arroyo, Santo Domingo**, el mismo barrio que el H4 de David ([wiki: Doc](https://cyberpunk.fandom.com/wiki/Doc_(Edgerunners))) | ✅ |
| **Arasaka Academy / Arasaka Tower** (City Center) | Escuela de David; la torre del final (ep. 10, 14:30: «estoy en lo alto de la Torre Arasaka») | La torre existe | ✅ subtítulo |
| **Memorial Park** (Corpo Plaza) | Donde mueren David y Rebecca (ep. 10) | En los arbustos del anillo suroeste está **Guts** | ✅ (wiki Rebecca, Den of Geek) |
| **Tienda 2nd Amendment**, Megaedificio H10, Little China | Práctica de tiro de David con Rebecca (ep. 4 ⚠️, sólo por el nombre del archivo W65) | Ubicación confirmada en la [wiki](https://cyberpunk.fandom.com/wiki/2nd_Amendment) | ✅ el sitio · ⚠️ el episodio |
| **Las Badlands** (desierto) | El convoy del ep. 9 | Existe | ✅ subtítulo |

### 5.2 La luz (medida en las hojas)

| Momento | Luz | Paleta medida ✅ | Referencia |
|---|---|---|---|
| **Calle de noche con farolas** (el equipo caminando) | Naranja de sodio, negros profundos | `#8C5648` `#4D231F` `#D9B88C` `#030309` | W46, G26 |
| **Afterlife** | Verde menta de neón desde la barra | `#7CF6CC` `#A8EEC9` `#328264` `#122521` | W117 |
| **Bar / reservado** (vídeo del ending) | Azul marino con filos cian | `#193E6F` `#44687D` `#8BB2AE` `#0A0F23` | W75 |
| **Calle de neón azul** («Blue Moon») | Azul noche, magenta del neón | `#20467D` `#5C789F` `#372945` `#B6CDD0` | W118 |
| **Tren de día** / Kabuki | Crema quemado y verde agua | `#FAFDDA` `#84CCB9` `#F2E0B2` | W84 |
| **Promoción: lima** (aniversario) | Lima y menta, sin sombras duras | `#87F46C` `#67DD8E` `#D1FDEF` `#572A49` | W2 |
| **Promoción: sofá** (lotería 2024) | Verde azulado con marco amarillo | `#0A545F` `#3E9480` `#F7EC49` `#C1F0AE` | W116 |
| **Lluvia** | Ciudad mojada de noche (ep. 1, 00:13; ep. 6, 18:25) | ⚠️ sin medir (no hay fotograma en las hojas) | §2.1 |

Regla visual de la serie: **negro casi puro** en las sombras (no gris) y
**un solo color de neón fuerte** por escena. Las sombras son planas, de
dos tonos, como recortes (se ve en todas las hojas W).

### 5.3 La paleta de la franquicia (medida ✅)

| Color | Hex | Dónde |
|---|---|---|
| **Amarillo Cyberpunk** (logo) | `#F8EE08` (oficial citado `#FCEE09` ⚠️) | Logo, key visual (G28) |
| Amarillo de marco de interfaz | `#F7E31F` | W116 |
| **Amarillo de la chaqueta de David** | luz `#FDCB1D`, `#DCC007`; sombra naranja `#C26D03` | G01, G25 |
| Cian del forro del cuello de David | `#39CAF8` | G01 |
| **Lima del rótulo de nombre** (degradado) | arriba `#45FF7D` → abajo `#EBFF68` | W47 |
| Lima de fondo (Rebecca) | `#BAF812` | G10 |
| Magenta (Lucy) | `#F246B3` | G06 |
| Rojo del juego (subtítulo) | coral `#FE6962` | guía de cuadros (medido antes) |
| Cian del juego (subtítulo) | `#59E6F0` | guía de cuadros |
| Negro de fondo | `#030309` a `#0A0F23` | W46, W75 |

Colores de cada personaje: ver §16.

### 5.4 Texturas reales equivalentes

- **Asfalto mojado con charcos** que reflejan neón: ambientCG
  Asphalt025B/C (CC0) + un plano de agua con rugosidad baja.
- **Chapa pintada y rayada** para el mueble de la recreativa: ambientCG
  PaintedMetal004 / 016 (CC0).
- **Persiana metálica** y chapa ondulada detrás: CorrugatedSteel005.
- **Pegatinas y grafitis** en la recreativa: la serie está llena de
  pegatinas y carteles rotos en las esquinas (W118 ⚠️ de memoria el
  detalle); hacerlas con los logos **de la ficción** (Arasaka, Militech,
  NCART, Kiroshi, Trauma Team), nunca con marcas reales.
- **Pantalla CRT** de la recreativa: textura de líneas de barrido y leve
  curvatura. Night City mezcla lo muy nuevo con lo viejo.

### 5.5 Segunda pasada · paleta medida en fotogramas propios

Medida con Pillow sobre los fotogramas de la 2.ª pasada (episodios de
[Internet Archive](https://archive.org/details/cyberpunk_edgerunners_04_360),
recorte de 80×40 px, color más repetido). ✅ medido.

| Escena | Luz | Fondo | Acento |
|---|---|---|---|
| ep. 1, 0:32 · pelea, visor del ciberpsicópata | Sirenas sobre lluvia | `#3C6C9C` · `#3C6090` (azul) | `#906C84` (malva de la sirena) |
| ep. 1, 0:44 · calle bajo la lluvia | Noche muy oscura, un solo acento | `#000C24` · `#000018` (negro azulado) | `#243C54` (cian apagado) |
| ep. 4, 21:20-21:58 · promesa de la luna | Visión nocturna, sin negro puro | `#002400` (verde oscurísimo) | `#78B46C` (verde claro) |
| ep. 6, 22:32 · visor de Maine roto | HUD verde fracturado | `#001800` (verde casi negro) | `#0C5400` (verde HUD) |

**Qué se saca**: confirma la regla de §5.2 (negro casi puro y un solo
acento de neón). Y enseña un recurso nuevo: el **filtro verde entero**
(luna, visor de Maine, braindance del ep. 3). Para #a-que-juegas, si se
quiere verde, mejor el verde HUD `#0C5400` del visor (más «de juego») que
el de la luna (demasiado triste).

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

| Dónde | Cómo es | Letra libre más cercana | ¿á é í ó ú ñ ¿ ¡? |
|---|---|---|---|
| **Logo «CYBERPUNK»** | Letras a mano, inclinadas y rotas, amarillo `#F8EE08` | **No hay equivalente libre**: usar el logo como imagen o no usarlo | — |
| «EDGERUNNERS» bajo el logo | Palo seco condensado en una banda | **Rajdhani Bold** o **Saira Condensed** | ✅ las dos |
| **Rótulos de nombre** (W47 y siguientes) | Palo seco **muy condensado y grueso**, degradado lima `#45FF7D`→`#EBFF68`, sombra fina oscura; el nombre en katakana encima | **Anton** (la más parecida) o **Bebas Neue** | ✅ las dos (Bebas sólo mayúsculas) |
| **Interfaz del juego** (subtítulos, menús) | **Rajdhani** (la del juego) y **Orbitron** de secundaria ([Fonts In Use](https://fontsinuse.com/uses/60926/cyberpunk-2077-video-game)) | Rajdhani / Orbitron (Google Fonts) | ✅ las dos |
| Pantallas y hologramas dentro del mundo | «Blender» y otras | **Chakra Petch**, **Oxanium**, **Share Tech Mono** | ✅ las tres |
| Título del opening | «EDGE RUNNERS» en letras rotas, como mosaico (G45) | **Rubik Glitch** (aproximación) | ✅ |
| Pantalla de recreativa | Píxeles | **VT323** o **DotGothic16** (trae japonés) | ✅ las dos |
| Katakana de los rótulos | Gótica redonda gruesa | DotGothic16 no; mejor una redonda japonesa (M PLUS Rounded 1c) ✅ comprobada con fontTools en la 2.ª pasada | á é í ó ú ñ ¿ ¡ ✅ |

**Comprobado por mí con fontTools** (archivos de
[google/fonts](https://github.com/google/fonts)): Rajdhani, Orbitron,
Chakra Petch, Oxanium, Teko, Share Tech Mono, VT323, Bebas Neue, Barlow
Condensed, Anton, Saira Condensed, Russo One, Audiowide, Zen Dots, Rubik
Glitch, Bungee y DotGothic16 **traen todas á é í ó ú ñ Ñ ¿ ¡ ü**.
(Orbitron sólo tiene 207 glifos, pero incluye estos.)

### 6.2 Qué letra para qué texto de la lámina

- **Nombre del canal** («A qué juegas»): **Anton** con el degradado lima
  del rótulo de nombre, o Rajdhani Bold en amarillo `#F8EE08`.
- **Lo que dice el personaje**: **Rajdhani Medium/SemiBold** en cian
  `#59E6F0`, con **el nombre en coral `#FE6962`** delante (el subtítulo
  del juego, ver §7).
- **La pantalla de la recreativa** y la **tabla de horas** (lámina 2):
  **VT323** (píxel) o **Share Tech Mono**.
- **Carteles y pegatinas** del sitio: Chakra Petch / Oxanium.
- Nada de letras de cómic redondas (Comic Neue, Bangers): **no es un
  anime de globos**.

### 6.3 Segunda pasada · tipografía

- **M PLUS Rounded 1c** ✅ trae á é í ó ú ñ Ñ ¿ ¡ ü (fontTools sobre el
  archivo de [google/fonts](https://raw.githubusercontent.com/google/fonts/main/ofl/mplusrounded1c/MPLUSRounded1c-Regular.ttf)).
- **Créditos del opening**, vistos en el ep. 3 (0:00-1:36): sans **bold
  condensada e inclinada**, negro sobre crema o blanco sobre magenta
  («Screen story by BARTOSZ SZTYBOR», «Directed by HIROYUKI IMAISHI»).
  Para imitarla: Bebas Neue o Anton en cursiva falsa de 8-10°.
- **Créditos del ending** (ep. 4, 22:40): condensada blanca sobre negro.
- **Logo «CYBERPUNK»**: sigue sin letra libre equivalente (buscado en
  dafont y Fontsource, variantes «glitch» y «cyberpunk»). Usar el logo como
  imagen ⚠️ (no lo encontré; no digo que no exista).
- **Amarillo exacto del logo** (`#F8EE08` o `#FCEE09`): no se pudo medir en
  esta pasada (AnimeThemes caído con error 522 y la API de imágenes de
  Wikipedia limitó las peticiones) ⚠️.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

Es lo más importante: **aquí no hay burbuja blanca**. La franquicia habla
de estas maneras:

### 7.1 En la serie

1. **Holo-llamada**. Cuando alguien habla desde lejos, los subtítulos
   para sordos lo marcan como 「（ホロ通信：名前）」 («holo-llamada:
   nombre»). Sale **en 9 de los 10 episodios** ✅ (conté las marcas; el
   ep. 3 tiene otra pista de subtítulos, sin marcas):
   Gloria llama a Maine (ep. 1, 05:40), Kiwi a David (ep. 7, 11:26),
   Rebecca (ep. 9, 10:20), Kiwi deja el equipo por holo (ep. 9, 17:31).
   En imagen es **una ventanita con la cara** flotando junto a quien la
   recibe ⚠️ (de memoria; comprobar en el fotograma).
2. **La interfaz del ojo** (Kiroshi): cuando Lucy escanea a David en el
   tren, la pantalla se llena de **recuadros rojos con datos** (G41 ✅ se
   ve). Es como piensa un personaje con implantes: **datos**, no nubes.
3. **La cinta de datos** del netrunner: una **tira verde con texto** que
   pasa por la cara (Kiwi, W57/G43 ✅ se ve).
4. **La radio y los anuncios**: el DJ de la radio (ep. 6, 01:45: «Good
   morning, Night City!»), el parte del tiempo (ep. 6, 03:58), la
   **profesora IA** de la Academia (「（ＡＩ教師）」, ep. 1, 08:00) y el
   anuncio de la luna (ep. 10, 23:56). La ciudad **habla por altavoces**.
5. **Rótulos de nombre** (W47…): el nombre en letras gruesas lima con
   el katakana encima, para presentar a cada uno ✅ (vídeo Inside Look #2).
6. **Sin monólogos interiores**: la serie no tiene voz en off de
   pensamientos ✅ (en los 10 subtítulos no hay ninguna marca de
   pensamiento; todo es diálogo o sonido).

### 7.2 En el juego (*Cyberpunk 2077*)

- **Subtítulo sin caja**, abajo en el centro: **nombre en coral
  `#FE6962`**, dos puntos, **texto en cian `#59E6F0`**, en **Rajdhani** ✅
  (medido en la guía `biblias/_ya_hechas/_Cuadros de dialogo por
  franquicia`, §14).
- Rótulos de tiempo tipo «SOME TIME LATER» en mayúsculas cian con
  resplandor `#2DFEFE`, a la izquierda ✅ (misma guía).
- **Opciones de diálogo** en lista vertical a la derecha, con la elegida
  resaltada ⚠️ (de memoria; la Game UI Database pedía un reto de
  Cloudflare y no lo intenté saltar).
- **Holo-llamada** en la esquina superior izquierda con el retrato y el
  nombre ⚠️ (de memoria).
- **La recreativa**: la de *Roach Race* tiene **tabla de récords con
  nombres de jugador en mayúsculas** (Z1R343L, B4RBOSA, NCALGOD, SCHEMA,
  NWONG, KEPLER, NETMAN, J4CKI3W, PNEUMO, SILVERHAND) y avisa con
  mensajes de «CDP Arcades» ✅ ([wiki: Roach Race](https://cyberpunk.fandom.com/wiki/Roach_Race)).
  Cuando la yegua coge una zanahoria, sale en japonés **「にんじんゲット！」**
  («¡zanahoria conseguida!») ✅ (misma página).

### 7.3 En el manga

- *Cyberpunk: Edgerunners MADNESS* (manga de Rebecca y Pilar de jóvenes)
  usa **globos de manga normales y onomatopeyas en katakana** («ジャキ»,
  el ruido al cargar Guts) ✅ (W103, W124-W126 se ven).
- Es la única pieza oficial **con globos**. No es el tono de la serie.

### 7.4 Cómo se traduce a una lámina fija

**Propuesta principal: el subtítulo del juego.**
- Abajo, sin caja: `REBECCA:` en coral `#FE6962` y la frase en cian
  `#59E6F0`, Rajdhani SemiBold, con un leve resplandor.
- Si el fondo es claro o con mucho detalle: una **banda negra
  translúcida** (60 %) detrás, como el subtítulo de Netflix. Nunca una
  burbuja con cola.

**Alternativas según el concepto (§19):**
- **Ventana de holo-llamada**: recuadro con esquinas cortadas en
  diagonal, filete cian, la cara del personaje dentro (un fotograma) y
  el texto al lado. Sirve para «¿quién se apunta?».
- **Pantalla de la recreativa**: el texto es parte del juego (menú,
  «INSERT COIN», tabla de récords). La tinta sigue la curva del CRT.
- **HUD del ojo**: recuadros rojos finos con datos (para la lámina 2 de
  horas: cada país como un «objetivo escaneado»).

### 7.5 Cómo hablan (por el subtítulo)

- **Frases cortas, de calle**, con jerga propia: *choom* (colega),
  *gonk* (idiota), *preem* (genial), *nova* (guay), *eddies* (dinero),
  *chrome* (implantes), *gig* (encargo), *flatline* (matar) ✅ (todo
  sale en los subtítulos: «C'mon, choom» ep. 1, 15:14; «We're at school
  you gonk!» ep. 2, 03:01; «Preeem!» ep. 4, 05:35; «Nova!» ep. 1, 05:26).
- En el **doblaje latino**: *braindance* se dijo **«neurodanza»**, *kid*
  queda como **«mocoso»**, *Trauma Team* como **«equipo de trauma»**, y
  sale **«pana»** ⚠️ (subtítulos automáticos de clips latinos, ver §10).
- **Rebecca en japonés** habla como una macarra: usa **「あーし」** (un
  «yo» de chica de la calle) y suelta 「ブッころ！」 («¡te mato!», ep. 9,
  05:51), 「うっしゃ！」 («¡bien!», ep. 8, 12:33), 「イーハー！」 («¡yija!»,
  ep. 7, 03:45) ✅ subtítulo.

### 7.6 Qué NO hacer con el texto

- Burbuja blanca de cómic con cola. **Nunca.**
- Verde tipo Matrix cayendo en columnas.
- Letras «de ordenador» genéricas de los 90 si no es la pantalla de la
  recreativa.
- Signos «·» o «—» de relleno (regla del dueño).
- Poner el logo de *Cyberpunk* rehecho con una letra parecida: queda
  falso. O el logo original, o nada.

### 7.7 Segunda pasada · el cuadro, confirmado

- **Subtítulo del juego sin caja** ✅: en una captura real de *Cyberpunk
  2077* (NPC en el Afterlife) el texto va centrado abajo, **sin caja**,
  cian claro con contorno oscuro
  ([Interface In Game](https://interfaceingame.com/wp-content/uploads/cyberpunk-2077/cyberpunk-2077-dialogue.png),
  1920×1080). Es subtítulo de cinemática, por eso no lleva el nombre en
  coral de §7.2. Confirma la regla: **nada de burbuja**.
- **Opciones de diálogo**: se navegan arriba y abajo y se resaltan en
  amarillo o azul según el tipo ✅ ([Game8](https://game8.co/games/Cyberpunk-2077/archives/Dialogue-Options)).
  La captura limpia de la lista vertical sigue sin conseguirse ⚠️ (Game UI
  Database tras Cloudflare, sin copia en Wayback).
- **Manga *MADNESS***: además del globo, lleva **onomatopeyas dibujadas a
  mano** en katakana y letras latinas rotas («ミシッ», «CHK» repetido)
  pegadas al borde de la viñeta (visto en W124, `hojas/hoja_03.jpg`).
- **La jerga**: los subtítulos dicen *choom*, *gonk*, *preem*, *eddies*,
  *delta*. En la lámina dan el tono sin traducir mal (glosario en «Punto 25»).

---

## 8 · Los personajes (descripción profunda y cómo se expresan)

Fuentes de cada ficha: la **wiki `cyberpunk`** por su API (edad, ropa,
pasado) y los **subtítulos** (cómo hablan, con minuto). Lo que viene de
la wiki sola va con ⚠️ si no lo confirma la serie.

### David Martínez — el protagonista

- **Quién es**: chico latino de Santo Domingo, **17 años** (ep. 1-6) y
  **18** (ep. 7-10); nació en 2058 **en la parte de atrás de una
  ambulancia** ✅ (wiki, que cita el *Cyberpunk: Edgerunners Mission Kit*, pág. 6 y 35). Vive con su madre, **Gloria**, técnica de
  emergencias, en el megaedificio H4. Estudia becado en la **Academia
  Arasaka**, donde no encaja (ep. 1, 10:38: «no tienes ni idea de
  cuánto desentono»). Vende braindances ilegales (XBD) en la escuela.
- **Qué le pasa**: su madre muere; él se instala el **Sandevistan**
  (implante militar que acelera el tiempo) y entra en el equipo de
  Maine. Se llena de implantes, va perdiendo la cabeza
  (**ciberpsicosis**) y muere en el ep. 10 ante Adam Smasher.
- **Qué le importa**: cumplir el sueño que le dejaron otros («Mom and
  Maine… They all left me something to do», ep. 8, 18:58) y **llevar a
  Lucy a la luna** (ep. 4, 21:54).
- **Miedos**: no poder salvar a nadie (ep. 10, 18:51: «No pude salvar a
  mamá ni a Maine, pero quería salvarte a ti»).
- **Manías**: **no le gustan las bebidas con gas ni el tabaco** (ep. 2,
  16:34 ✅) y odia que le llamen «Davis» («David! Not Davis! David!»,
  ep. 4, 04:02 ✅). Se cree «especial» («I think… I'm built different»,
  ep. 5, 18:00).
- **Cómo habla**: directo, impulsivo, jerga de barrio (*choom*, *nova*).
  **Cómo se ríe**: una carcajada abierta cuando algo le fascina (el sol
  en el BD de la luna: «I can feel the fucking sun!», ep. 2, 19:27,
  「アハハッ」). **Cómo se enfada**: grita e insulta («Fuck off!», ep. 1,
  17:31). **Cómo explica**: con lógica rápida («Would you bring a
  bodyguard to tune up a fetish BD?», ep. 5, 05:02). **Cómo saluda**:
  seco, «Hey, Kiwi» (ep. 7, 11:36).
- **Cuerpo**: manos en los bolsillos de la chaqueta (W127, G25), se
  señala con el pulgar (W26), sonrisa torcida.
- **Con quién**: Lucy (amor), Rebecca (amiga que le quiere), Maine
  (maestro), Falco (su conductor fiel), Doc (su ripperdoc).

### Lucy (Lucyna Kushinada) — la heroína

- **Quién es**: netrunner (hacker que «bucea» en la red), **unos 20
  años**. Según la wiki nació en **Varsovia** de padre japonés y madre
  polaca ⚠️. De niña la entrenó Arasaka con otros 12 niños para bucear
  en la «Old Net»; **sólo ella escapó** (lo cuenta en el ep. 7, 17:24 a
  20:13 ✅).
- **Qué quiere**: **irse a la luna**. Night City le parece una cárcel
  («Sounds more like a prison than paradise», ep. 2, 17:34; «La ciudad
  parece una jaula hecha de luces», ep. 7, 16:50 ✅).
- **Miedos**: que Arasaka la encuentre («They're always watching us»,
  ep. 6, 06:46) y que David muera (ep. 4, 22:09: «I just don't want you
  to die»).
- **Cómo habla**: **frases cortas, órdenes**: 「来て」 «ven», 「座って」
  «siéntate», 「脱いで」 «quítatela» (ep. 2, 15:48-16:47). Da lecciones
  con sorna: «Lesson number one. Less judgment, more awareness» (ep. 2,
  08:56). Provoca: «Oh? A bad boy» (ep. 2, 08:44). **Cómo se ríe**: una
  risa corta por la nariz, 「フッ」 (ep. 2, 08:49). **Cómo se enfada**:
  se cierra y corta («Shut it, David!», ep. 6, 06:26). **Cómo pide
  algo**: «David… Tell me I can do it» (ep. 6, 06:36).
- **Voz latina** (María José Moreno): la directora le pidió **un tono
  más grave, serio y frío** que su voz real (entrevista ANISON USA,
  **19:49-20:15** ✅).
- **Cuerpo**: brazos cruzados o abrazándose las rodillas (W104), la
  cabeza ladeada con media sonrisa (G05), la chaqueta caída de los
  hombros.
- **Con quién**: David; **Kiwi**, que la metió en el equipo y fue su
  mentora (ep. 8, 10:47); Rebecca.

### Rebecca — la secundaria más querida (ver §9)

- **Quién es**: *solo* (la de las armas) del equipo, **unos 20 años**,
  **bajita**. Hermana pequeña de **Pilar** ✅ (subtítulo: 「バカアニキ」,
  «el idiota de mi hermano», ep. 7, 09:18). La wiki cuenta que su padre
  («Papa Sunrise») desapareció y los dos hermanos vivieron en un coche ✅ (wiki, cita el *Mission Kit*, pág. 40).
- **Qué le pasa**: pierde a Pilar en el ep. 4 («¡Sólo yo tenía derecho
  a matarle!», 「あいつを殺していいのはあたしだけだったのに！」, ep. 4,
  18:18 ✅). Se pone **brazos de gorila**. Está enamorada de David, pero
  le ayuda a volver con Lucy. Muere en el ep. 10 protegiendo al equipo.
- **Qué le importa**: **su equipo**. Es la primera en ver que David se
  está rompiendo: «Hoy no es la primera vez… Sólo te miro así de cerca
  a ti» (ep. 8, 12:49-13:03 ✅).
- **Cómo habla**: macarra, de calle. En japonés usa 「あーし」 y a veces
  「あたし」 (yo), 「ブッころ！」 («¡te mato!»), 「うっしゃ！」 («¡bien!»),
  「イーハー！」 («¡yija!»). Insulta con cariño: a Kiwi la llama
  «vieja» (「オバサン」, ep. 7, 09:07; en inglés «nagging hag») y a Falco y Kiwi
  «boomers» (ep. 8, 12:20). **Cómo saluda**: «Hey David! How've you
  been?» 「あー デイビッドじゃん 元気？」 (ep. 4, 05:11). **Cómo se ríe**:
  a carcajadas, 「うっひょー アハハハハハッ」 (ep. 10, 09:16). **Cómo se
  enfada**: explota («You fucking gonk! Why don't you ever listen?!»,
  ep. 9, 17:10). **Cómo anima**: «Don't worry. I've got your back!»
  (ep. 8, 13:32).
- **Cuerpo**: manos en los bolsillos o **detrás de la nuca** (G09, W46),
  agachada apuntando (G10), **dos pistolas a la vez** (W9), puños al
  cielo con los brazos de gorila (G33), guiño (W79, W116).
- **Con quién**: Pilar, David, Lucy, Kiwi (se pican), Falco.

### Maine — el jefe del equipo

- **Quién es**: líder del grupo, **cerca de 40 años**, enorme, rubio,
  visor y bufanda. Ex boxeador, ex portero de discoteca y ex soldado de las NUSA SpecOps ✅ (wiki, cita el *Mission Kit*). Pareja de
  **Dorio**.
- **Qué le importa**: **repartir justo** («Everybody gets a fair shake.
  Only way I operate», ep. 3, 18:02 ✅) y que cada uno se valga solo
  («Ain't no one in this world you can trust more than yourself», ep. 3,
  17:13 ✅).
- **Qué le pasa**: el exceso de cromo le lleva a la **ciberpsicosis**
  (ep. 6) y muere pidiéndole a David que siga corriendo: «Fast is what
  you do, remember? Keep running» (ep. 6, 22:32 ✅).
- **Cómo habla**: jefe bromista y bruto. Enseña con reglas de la calle:
  «Every day. You check for your wallet, your condom, and your gun»
  (ep. 4, 08:40). Se burla con cariño: 「あーあ 分っかりやすいやつだな！」
  («¡qué fácil eres de leer!», ep. 5, 02:49).
- **Cuerpo**: sonrisa enorme, brazo sobre el hombro de otro, hombreras
  (W29, G13).

### Kiwi — la netrunner veterana

- **Quién es**: alta y delgada, **abrigo rojo largo**, **máscara roja**
  que tapa la mandíbula (le falta), bob rubio claro ✅ (se ve en W25,
  W33; la historia de la mandíbula, ✅ wiki con cita del *Mission Kit*; no para láminas, ver §14). Mentora de Lucy.
- **Su frase**: «Never trust a soul in Night City» ✅ (ep. 9, 04:51; se
  lo había enseñado a Lucy, ep. 8, 10:47).
- **Qué le pasa**: **traiciona al equipo** con Faraday (ep. 8-9), luego
  traiciona a Faraday y **Arasaka la mata** (ep. 10, 12:37-12:51 ✅).
- **Cómo habla**: seca, irónica, con 「あんた」 («tú» de confianza).
  Cansada: 「あいつ 人使い荒いんだよ」 («ese explota a la gente», ep. 7,
  04:29). Casi no ríe.
- **Cuerpo**: brazos cruzados, una mano en la máscara (W25, W27).

### Los demás, en una línea

- **Pilar**: hermano de Rebecca, técnico, **brazos larguísimos**,
  payaso del grupo («Bro! … Preeem!», ep. 4, 05:22-05:35). Muere en el
  ep. 4.
- **Dorio**: grandona, rubia (W31, W46), pareja de Maine, la que le cuida
  («When's the last time you ate?», ep. 6, 02:27). Muere en el ep. 6.
- **Falco**: conductor nómada, bigote, ropa del oeste, acento sureño ✅
  (la [wiki](https://cyberpunk.fandom.com/wiki/Falco) lo dice con todas las letras: «a notable Southern drawl»; cuadra con su ropa y su camioneta). **Cumple su promesa** a David al final (ep. 10, 21:34-22:25).
  Rebecca se ríe de su bigote (ep. 9, 13:13).
- **Faraday**: el *fixer* (el que reparte los encargos). Frío y
  traidor: «I do not pay you to think» (ep. 3, 19:40).
- **Gloria**: madre de David: «Get to the top floor of Arasaka Tower!»
  (ep. 1, 11:45).
- **Doc**: el ripperdoc gruñón que al final le desea suerte: «Go be a
  legend» (ep. 8, 18:05).
- **Adam Smasher**: el villano, un cíborg total («All the same meat to
  me», ep. 10, 20:59). **No usarlo en una lámina amable.**

### Segunda pasada · lo nuevo de cada uno (wiki con cita al *Mission Kit*)

La wiki `cyberpunk` cita el **manual oficial *Cyberpunk: Edgerunners
Mission Kit*** (juego de rol) con su página. Por eso estos datos pasan a ✅.

- **David** ✅: nació **en la parte de atrás de una ambulancia**; Gloria
  acababa de suturar a un mercenario, y ese mismo merc cortó el cordón con
  las cuchillas mantis que ella le había arreglado (*Mission Kit*, pág. 6 y
  35; [wiki](https://cyberpunk.fandom.com/wiki/David_Martinez)). Apodos:
  «Dee» (Gloria), «Davey» (Doc).
- **Lucy** ✅: nació en **Varsovia**; sus padres, **Takeshi Kushinada** y
  **«Shimmer»**. Rafał Jaki le puso **el nombre de su propia madre**;
  «Lucyna» viene de *Lūcīna*, «la que trae a la luz», diosa romana de los
  partos ([wiki](https://cyberpunk.fandom.com/wiki/Lucyna_Kushinada), cita
  un post del creador). Encaja con su final: «da a luz» su libertad en la
  luna. Apodo: «Luce».
- **Rebecca** ✅: tras perder el piso por deudas de juego del padre («Papa
  Sunrise»), vivieron en su coche averiado; la ayudó **Wakako Okada**. Es
  **más tierna de lo que parece**: perdía encargos por pararse a abrazar
  un cachorro o por defender a una camarera, y una vez perdonó a un
  objetivo «porque tenía los ojos tristes, pobre gonk» (*Mission Kit*,
  pág. 40; [wiki](https://cyberpunk.fandom.com/wiki/Rebecca)).
- **Maine** ✅: nació en **Portland (estado de Maine)**: de ahí su nombre.
  Boxeador, luego portero de discoteca (lo echan por pegar a cinco tipos
  que eran de las NUSA SpecOps), y esas fuerzas lo reclutan al día
  siguiente; sirvió en Sudamérica con **Solomon Reed** (el de *Phantom
  Liberty*) y desertó. Fue reuniendo su «familia»: salvó a Dorio cuando a
  ella le fallaba un encargo; luego Falco, Pilar, Rebecca, Sasha y Kiwi
  ([wiki](https://cyberpunk.fandom.com/wiki/Maine_(Edgerunners))).
- **Kiwi** ✅ pero **no para láminas**: su pasado (vendida de niña, joytoy
  a la fuerza, un cliente le arrancó la mandíbula; de ahí la máscara) es
  canon y muy oscuro ([wiki](https://cyberpunk.fandom.com/wiki/Kiwi)). Su
  «Never trust a soul in Night City» (ep. 9, 04:51) nace de ahí.
- **Falco** ✅: «a notable Southern drawl», acento sureño marcado
  ([wiki](https://cyberpunk.fandom.com/wiki/Falco)).

---

## 9 · ¿Quién es el más querido?

**Rebecca**, sin duda, aunque Lucy es la heroína. ✅

- **Encuesta de fans (Ranker, «14 Best Cyberpunk: Edgerunners
  Characters»)**: **1.º Rebecca**, 2.º David, 3.º Lucy ✅
  ([Ranker](https://www.ranker.com/list/best-cyberpunk-edgerunners-characters/jay_kobayashi),
  citado también por [EpicStream](https://epicstream.com/article/cyberpunk-edgerunners-rebecca-everyones-favorite-character)).
- Prensa: «el personaje favorito de todos» ([EpicStream](https://epicstream.com/article/cyberpunk-edgerunners-rebecca-everyones-favorite-character)),
  «cómo Rebecca se volvió la favorita» ([CBR](https://www.cbr.com/cyberpunk-edgerunners-anime-rebecca-fan-favorite/)),
  «uno de los personajes más geniales de 2077 ni siquiera está en el
  juego» ([Screen Rant](https://screenrant.com/cyberpunk-2077-edgerunners-rebecca-best-character/)) ✅.
- **Corea**: Namuwiki dice que Rebecca **recibió tan buena acogida como
  Lucy, a veces más** que la heroína ✅ ([Namuwiki](https://namu.wiki/w/%EB%A0%88%EB%B2%A0%EC%B9%B4(%EC%82%AC%EC%9D%B4%EB%B2%84%ED%8E%91%ED%81%AC%20%EC%8B%9C%EB%A6%AC%EC%A6%88))).
- **China**: artículos y preguntas en Zhihu sobre «por qué Rebecca es
  tan popular» ([Zhihu](https://www.zhihu.com/question/553633303),
  [18183](https://www.18183.com/xinwen/202209/4157621.html)) ✅.
- **Reddit** (archivo Arctic Shift, r/cyberpunkgame, 13-sep a 31-dic de
  2022, los 100 primeros hilos con el nombre en el título): **Rebecca
  26.240 votos**, Lucy 14.637, Kiwi 8.873, David 7.327 ⚠️ (es una señal,
  no una encuesta). En 2026 sigue igual: los hilos de fan art más
  votados son de Rebecca (§4.4), y en julio de 2026 alguien preguntaba
  si la nueva **Talia** (temporada 2) podrá superar a «Lucy o Rebecca»
  (1.503 votos).
- **Oficial**: no hay encuesta de personajes oficial ⚠️ (no encontré
  ninguna, ni en japonés). Lo oficial es el premio a la serie:
  **Anime del Año** en los **Crunchyroll Anime Awards 2023** (primer
  anime basado en un videojuego que lo gana; 18 millones de votos) ✅
  ([Deadline](https://deadline.com/2023/03/anime-awards-2023-winners-list-1235278881/),
  [Animation Magazine](https://www.animationmagazine.net/2023/03/cyberpunk-edgerunners-wins-anime-of-the-year-at-crunchyroll-anime-awards/),
  [AWN](https://www.awn.com/news/cyberpunk-edgerunners-named-anime-year-2023-anime-awards)).
  También fue nominada a los **Annie** ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Cyberpunk:_Edgerunners), categoría) ⚠️.
- La propia CD PROJEKT le dio a Rebecca un **manga propio**
  (*Edgerunners MADNESS*) y una réplica oficial de su escopeta (2026) ✅.

**Para la lámina**: Rebecca es la apuesta segura para un canal de
«quién se apunta»: es la que invita, anima y dispara. Lucy funciona
para un tono más tranquilo (compartir capturas, «mira esto»). David,
para «me apunto».

**Segunda pasada · dos datos que lo matizan**

- **Rebecca no estaba en el guion original** de CD PROJEKT RED: la
  **añadió Trigger** y convenció con su diseño; el guionista **Rafał Jaki**
  dijo en X que es **su favorita** ✅ ([wiki: Rebecca](https://cyberpunk.fandom.com/wiki/Rebecca)).
- **El director Hiroyuki Imaishi dijo en un AMA de Reddit que su favorita
  es Kiwi** ✅ ([r/Edgerunners AMA](https://www.reddit.com/r/Edgerunners/comments/z9hre7/comment/iyh0ftw/),
  citado en la [wiki: Kiwi](https://cyberpunk.fandom.com/wiki/Kiwi)).
- Cariño medible: el vídeo «Cyberpunk Edgerunners but just Rebecca» de
  Kakuchopurei pasó **1,2 millones de vistas en 6 días** ✅
  ([KnowYourMeme](https://knowyourmeme.com/memes/rebecca-edgerunners-character)).

**Veredicto, igual que antes**: para el público, **Rebecca**. Kiwi queda
como dato curioso («la favorita del director»).

---

## 10 · Doblaje latino

### 10.1 Ficha (Doblaje Wiki por su API ✅)

- **Estudio**: **Grande Studios** (México). **Dirección y adaptación**:
  **Jessica Ángeles**. **Traducción**: **Amalia Bobadilla**. Guiones de
  Netflix (EE. UU.); algunos diálogos grabados en **Córdoba (Argentina)**
  (los de Sebastián Llapur). Estreno: **13-sep-2022** en Netflix.
  Segunda fuente del estudio, directora y traductora: ANMTV y Okami Sama
  TV (por el buscador) ✅.

### 10.2 Reparto (cada nombre, con sus fuentes)

| Personaje | Voz latina | Voz japonesa | Fuentes | Estado |
|---|---|---|---|---|
| **David Martínez** | **José Ángel Torres** | KENN | Doblaje Wiki + ANMTV + entrevista ANISON USA (se une en 4:20) | ✅ |
| **Lucy** | **María José Moreno** («Majo») | Aoi Yūki | Doblaje Wiki + ANMTV + ANISON USA (0:50) | ✅ |
| **Rebecca** | **Melissa Gedeón** («Meli G») | Tomoyo Kurosawa | Doblaje Wiki + TV Tropes + Heroes Wiki | ✅ |
| **Maine** | **Humberto Solórzano** | Hiroki Tōchi | Doblaje Wiki + ANMTV + TV Tropes | ✅ |
| **Kiwi** | **Jocelyn Robles** | Takako Honda | Doblaje Wiki + Okami Sama TV | ✅ |
| **Faraday** | **Raúl Anaya** | Kazuhiko Inoue | Doblaje Wiki + Okami Sama TV | ✅ |
| **Doc** (ripperdoc) | **Carlo Vázquez** | Kenjirō Tsuda | Doblaje Wiki + Okami Sama TV | ✅ |
| **Gloria Martínez** | **Analiz Sánchez** | Yurika Hino | Doblaje Wiki + Okami Sama TV | ✅ |
| Dorio | Kerygma Flores | Michiko Kaiden | Doblaje Wiki + aniSearch/Anime-Planet | ✅ |
| Pilar | Armando Guerrero | Wataru Takagi | Doblaje Wiki + aniSearch/Anime-Planet | ✅ |
| Falco | Edson Matus | Yasuyuki Kase | Doblaje Wiki + aniSearch/Anime-Planet | ✅ |
| Tanaka | Sebastián Llapur | Tetsuo Komura | Doblaje Wiki + aniSearch/Anime-Planet | ✅ |
| Katsuo Tanaka | Arturo Castañeda | Kaito Ishikawa | Doblaje Wiki + aniSearch/Anime-Planet | ✅ |
| Jimmy Kurosaki | Christian Strempler | Yoshito Yasuhara | Doblaje Wiki + aniSearch/Anime-Planet | ✅ |
| Julio | Alan Bravo | Sōma Saitō | Doblaje Wiki + aniSearch/Anime-Planet | ✅ |
| Profesora IA | Cony Madera | Atsuko Sakuraoka | Doblaje Wiki + aniSearch/Anime-Planet | ✅ |
| Adam Smasher | Idzi Dutkiewicz (actor polaco; la wiki lo pone también en latino) | Yukihiro Misono | Doblaje Wiki + [aniSearch](https://www.anisearch.com/character/111048,adam-smasher) | ✅ (dos fuentes; sigue siendo raro, oírlo) |

Inglés, por si hace falta: David **Zach Aguilar**, Lucy **Emi Lo**,
Rebecca **Alex Cazares**, Maine **William C. Stephens**, Faraday
**Giancarlo Esposito**, Falco **Matthew Mercer** ✅ (wiki `cyberpunk` +
[Behind The Voice Actors](https://www.behindthevoiceactors.com/tv-shows/Cyberpunk-Edgerunners/)).

### 10.3 Cómo suena en latino

- **Muy malhablado y muy mexicano**: la Doblaje Wiki apunta que tiene
  «una gran cantidad de groserías y modismos mexicanos que no están en
  el original» y hasta términos de España ✅. En la entrevista, la
  directora les dijo que **les dejaban decir ciertas palabras** y hubo
  «más libertad» (ANISON USA, **31:34-31:51**) ✅.
- **«David» se pronuncia como se lee** (no «Deivid»), aunque en algunos
  episodios se cuela «Deivid» ✅ (Doblaje Wiki).
- Error famoso: en el ep. 10 Smasher dice «Debiste buscar una mejor
  construcción» (*construct* es otra cosa en el universo Cyberpunk) ✅
  (Doblaje Wiki).
- El volumen de la música tapa a veces los diálogos ✅ (Doblaje Wiki).

### 10.4 Frases del doblaje latino (con su minuto en el clip)

Salen de **subtítulos automáticos** de clips con audio latino; la
transcripción puede tener fallos ⚠️. Sirven como tono, no como cita
exacta.

| Frase latina | Quién | Escena | Clip y minuto |
|---|---|---|---|
| «¿Qué te parecería si trabajamos juntos desde hoy?» | Lucy | Tren, ep. 2 | [Momentos divertidos](https://www.youtube.com/watch?v=2I4ONpf9W3k) 0:03-0:07 |
| «70-30 y te pagaré en cuanto termine el trabajo» | Lucy | ep. 2 | ídem 0:45 |
| «Eres tan adorable. Nos vemos luego, David» | Rebecca | El paquete de Pilar, ep. 4 | [Rebecca y el paquete de Pilar](https://www.youtube.com/watch?v=wVRgUMabzdY) 0:59-1:01 |
| «¿Por qué tan serio, David? Deja de coquetear y mejor vamos a bailar» | Rebecca | Fiesta, ep. 7 | Momentos divertidos 10:35 |
| «No voy a emborracharme con este par de boomers» | Rebecca | ep. 8 | ídem 11:06 |
| «Oye, ¿quieres dar un paseo?» | Rebecca | ep. 8 | ídem 11:14 |
| «No te preocupes, yo te cuido» | Rebecca | ep. 8 | ídem 11:40 |
| «Riesgo enorme, pero la plata es jugosa. Si no quieren arriesgarse, será mejor que se vayan» | David | Reunión, ep. 9 | ídem 8:51-8:59 |
| «Los ancianos decrépitos se pueden quedar sentados si quieren» | Rebecca | ep. 9 | ídem 9:01-9:06 |
| «Si no tuviera bigote, te tendría enamorada» | Rebecca a Falco | ep. 9 | ídem 10:09-10:13 |
| «¿Traerías a tu guardaespaldas para que vea cómo ajustan tu **neurodanza** X?» | David | ep. 5 | [Mejores momentos #3](https://www.youtube.com/watch?v=N8f3ZHBMrdQ) 1:48 |

Más: [tráiler doblado al latino](https://www.youtube.com/watch?v=3s4uuDJbqBs)
(1:11, 31-ago-2022) y la **entrevista de ANISON USA** a María José
Moreno y José Ángel Torres ([vídeo](https://www.youtube.com/watch?v=c8YBuJhIVJY),
1:01:26, 25-sep-2022): Majo entró **por llamado directo** de Jessica
Ángeles, sin prueba (2:10-2:20) ✅.

**Frase propuesta para la lámina** (en voz latina, sin inventar jerga
rara): «¿Qué te parecería si jugamos juntos?» (eco de Lucy) o «Oye,
¿te apuntas?» (tono Rebecca). Ver §19.

### 10.5 Segunda pasada · doblaje

- **Reparto principal** revisado otra vez contra
  [ANMTV](https://www.anmtvla.com/2022/09/cyberpunk-edgerunners-ya-esta.html):
  coincide letra por letra con Doblaje Wiki (Grande Estudios, Jessica
  Ángeles, Amalia Bobadilla y los 7 principales) ✅✅.
- **Secundarios**: la segunda fuente sale de **aniSearch** (fichas por
  personaje con bandera «es»): [Dorio](https://www.anisearch.com/character/111005,dorio),
  [Pilar](https://www.anisearch.com/character/111006,pilar),
  [Falco](https://www.anisearch.com/character/111038,falco),
  [Tanaka](https://www.anisearch.com/character/111033,tanaka),
  [Katsuo Tanaka](https://www.anisearch.com/character/111034,katsuo-tanaka),
  [Jimmy Kurosaki](https://www.anisearch.com/character/111041,jimmy-kurosaki),
  [Julio](https://www.anisearch.com/character/111043,julio) y
  [Adam Smasher](https://www.anisearch.com/character/111048,adam-smasher);
  la Profesora IA (Cony Madera), en la filmografía de la actriz en
  [Anime-Planet](https://www.anime-planet.com/people/cony-madera). ✅✅
- **Aviso de método**: el buscador con resumen de IA dijo que **Behind The
  Voice Actors** confirmaba a Armando Guerrero y a Christian Strempler.
  **Era falso**: BTVA sólo lista inglés y japonés para esta serie. Se
  descartó y se comprobó todo en la página real.
- Sin cambios en «Cómo suena en latino» ni en los datos de interés
  («Deivid», groserías, el error de «construcción»): coinciden con el
  wikitexto de Doblaje Wiki.
- **Tráiler de Dailymotion**: sus subtítulos son de **España**, no del
  doblaje latino (§2.6). No citarlo como latino.

---

## 11 · Música

| Tema | Quién | Dónde suena | Ambiente | Estado |
|---|---|---|---|---|
| **«This Fffire»** (opening) | **Franz Ferdinand** (versión de 2004 producida por Rich Costey, muy recortada) | Opening de cada episodio (ep. 3, 00:11 a 01:34 en el subtítulo) | Rock nervioso, fuego y velocidad | ✅ ([wiki](https://cyberpunk.fandom.com/wiki/Cyberpunk:_Edgerunners/Soundtrack), [Wikipedia](https://en.wikipedia.org/wiki/This_Fire_(Franz_Ferdinand_song))) |
| **«Let You Down»** (ending) | **Dawid Podsiadło** | Al final de cada episodio (ep. 3, 22:40; letra en ep. 3, 22:56-24:02: «Forgive me for letting you down») | Balada triste, despedida | ✅ ([vídeo oficial](https://www.youtube.com/watch?v=BnnbP7pCIvQ), 4:44, 57,7 millones de vistas) |
| **«I Really Want to Stay at Your House»** | **Rosa Walton** (de Let's Eat Grandma; en el juego, con Hallie Coggins) | El **BD de la luna del ep. 2** (**19:30-21:30**, visto con fotogramas en la 2.ª pasada; sin diálogo, sólo risas y el motor del rover; que Imaishi la eligió para el final del ep. 2 ✅ wiki) | Pop dulce y melancólico; **la canción de David y Lucy** | ✅ |
| Banda sonora original | **Akira Yamaoka** (el de *Silent Hill*), **Marcin Przybyłowicz** y **P.T. Adamczyk** (compositores del juego) | Toda la serie | Electrónica sucia, tensa | ✅ |

**La banda sonora** (27-oct-2023, 14 temas) ✅
([wiki](https://cyberpunk.fandom.com/wiki/Cyberpunk:_Edgerunners/Soundtrack),
[Apple Music](https://music.apple.com/us/album/cyberpunk-edgerunners-original-series-soundtrack/1711647903),
[Spotify](https://open.spotify.com/album/0j3Idieeln2mEJKdhfCzPb)):
This Fffire · Opening Credits · Modern Anthill · Sudden Skirmish · Like a
Boy · Cloudy Day · Whatever It Takes · Into the Fire · Consumer Cathedral
· Juiced Up · Lucky You · **Whatever Choom, Like I Give a Sh\*t** ·
Run to the Edge · Let You Down.

- «I Really Want to Stay at Your House» llegó al **n.º 1 del Viral 50 de
  Spotify** (EE. UU. y Reino Unido) y al **n.º 68** de las listas
  británicas ✅ ([Wikipedia](https://en.wikipedia.org/wiki/I_Really_Want_to_Stay_at_Your_House),
  [Soundtracks, Scores and More](https://soundtracksscoresandmore.com/2022/09/28/cyberpunk-2077-listen-to-the-viral-hit-song-i-really-want-to-stay-at-your-house-by-rosa-walton-with-lyrics/)).
  Su vídeo oficial en Netflix tiene **90,4 millones de vistas**
  ([vídeo](https://www.youtube.com/watch?v=KvMY1uzSC1E), 4:22) ✅.
- En *Cyberpunk 2077* suena en la **radio del juego** (álbum *Radio,
  Vol. 2*, 2020) ✅: un jugador puede ponerla dentro de Night City.

Para la lámina: el **ambiente** es el de «Let You Down» y «I Really Want
to Stay…», **noche, neón y melancolía**, no el de un arcade alegre.

**Segunda pasada · música vista en el vídeo**

- **Opening «This Fffire»**: completo en el ep. 3, 0:00-1:36 (título en
  pantalla a 1:04). En los **primeros 4:20 del ep. 1 no suena**: el ep. 1
  arranca directo con la pelea bajo la lluvia ✅ (visto).
- **Ending «Let You Down»**: ep. 4 desde 22:40; mismo montaje al final del
  ep. 6 ✅ (visto).
- **«I Really Want to Stay at Your House»**: la secuencia de la luna del
  ep. 2 va de **19:30 a 21:30** ✅ (visto). Ojo: **no es el opening**, es
  la canción de la escena (una parte de voz la llamó «opening» por error).
- Análisis con minuto: [The Canipa Effect](https://www.youtube.com/watch?v=3PTX0lO7tpU&t=808s)
  dedica **13:28-15:08** a esta canción.
- Los `.webm` de [AnimeThemes](https://animethemes.moe/) siguen caídos
  (error 522, dos intentos) ⚠️.

---

## 12 · Vídeos (con minuto)

**Oficiales** (títulos y duraciones sacados con yt-dlp ✅):

| Vídeo | Duración | Qué sirve (minuto) |
|---|---|---|
| [Official Teaser (Netflix)](https://www.youtube.com/watch?v=x4ztgjvfU60) | 1:18 | Primeras imágenes (junio 2022) |
| [Official Trailer (Studio Trigger Version)](https://www.youtube.com/watch?v=ax5YUmkWf_Y) | 3:00 | Montaje de Trigger |
| [Official NSFW Trailer](https://www.youtube.com/watch?v=JtqIas3bYhg) | 2:18 | Rebecca con Guts (W69-W71) |
| [**Inside Look**](https://www.youtube.com/watch?v=zxapZWv4pNs) (CD PROJEKT RED) | 11:23 | Capítulos: 0:27 *Behind the scenes*, **2:21 *Creating Night City***, 3:44 *David & Lucy*, 4:49 *Body mods*. Peces holográficos 2:51; «cada fotograma es una pintura» 3:07 |
| [**Inside Look #2**](https://www.youtube.com/watch?v=D6ia1wjO7sg) (Trigger) | 5:45 | **Fondos pintados sobre fotos del juego 2:05-2:39**; David 2:49; Lucy 3:47. De aquí salen los **rótulos de nombre** (W47…) |
| [Yoshinari dibuja a David y Lucy](https://www.youtube.com/watch?v=9lQamD4CfBU) (Netflix Japan) | 5:45 | Trazo y proporciones de Yoshinari |
| [Clip «Cyberpsycho VS the NCPD»](https://www.youtube.com/watch?v=YRL74JmhVgk) | 3:16 | Arranque del ep. 1 bajo la lluvia (8,7 M vistas) |
| [Clip «Walk Through Night City!»](https://www.youtube.com/watch?v=Fn9gKhU_2_Q) | 2:09 | **Paseo por la ciudad**: sirve de fondo |
| [Ending «Let You Down»](https://www.youtube.com/watch?v=BnnbP7pCIvQ) | 4:44 | El equipo en el bar (W75) |
| [«I Really Want to Stay at Your House» (vídeo)](https://www.youtube.com/watch?v=KvMY1uzSC1E) | 4:22 | Recopilación David y Lucy |
| [Edgerunners 2: teaser](https://www.youtube.com/watch?v=jjhRSNkquOc), [teaser #2](https://www.youtube.com/watch?v=QBlPg818lGI), [teaser #3](https://www.youtube.com/watch?v=SyeHKMfswHk), [fecha](https://www.youtube.com/watch?v=IBTK8PGe_Oo), [*sneak peek*](https://www.youtube.com/watch?v=1i5Db5GHw0I) | 1:04-1:44 | Temporada 2 (ver §13.4) |

**Doblaje latino**: [tráiler doblado](https://www.youtube.com/watch?v=3s4uuDJbqBs)
(1:11), [entrevista ANISON USA](https://www.youtube.com/watch?v=c8YBuJhIVJY)
(1:01:26), [Momentos divertidos, audio latino](https://www.youtube.com/watch?v=2I4ONpf9W3k)
(11:48, 1,9 M vistas), [Rebecca y el paquete de Pilar](https://www.youtube.com/watch?v=wVRgUMabzdY)
(1:12). Minutos de frases: §10.4.

**Análisis**: [Gigguk, «The Cyberpunk Anime is Actually Incredible»](https://www.youtube.com/watch?v=EWB7ylAVObY)
(11:29, 2,9 M vistas), [The Canipa Effect: animación](https://www.youtube.com/watch?v=3PTX0lO7tpU)
(15:08), [Swamp Jawn: «una historia en 6 segundos»](https://www.youtube.com/watch?v=Xv9MdoAt3gQ)
(9:33), [MankoMan: análisis de animación](https://www.youtube.com/watch?v=j2nHAPtCjBk)
(23:27). Capítulos sacados en la 2.ª pasada con yt-dlp: ver «Segunda pasada» al final de esta sección.

**TikTok**: la tendencia fue editar a **David y Lucy con «I Really Want
to Stay at Your House»** ✅ ([Wikipedia](https://en.wikipedia.org/wiki/I_Really_Want_to_Stay_at_Your_House),
[etiqueta](https://www.tiktok.com/tag/edgerunners?lang=en)). En español
circulan con subtítulos («#subtitulosenespañol», [ejemplo](https://www.tiktok.com/@donllama/video/7210438811875167494)).
Retos de doblaje de fans a la voz oficial de David
([SDV Servicios de Voz](https://www.tiktok.com/@sdv_serviciosdevoz/video/7152659901645360390?lang=es)).

**Segunda pasada · capítulos de los análisis** (yt-dlp, sin descargar) ✅

| Vídeo | Minutos útiles |
|---|---|
| [Gigguk](https://www.youtube.com/watch?v=EWB7ylAVObY&t=177s) (11:29) | Intro 0:00 · patrocinio 2:01 · **el análisis, 2:57-11:29** |
| [The Canipa Effect](https://www.youtube.com/watch?v=3PTX0lO7tpU&t=808s) (15:08) | Por tema musical; **«I Really Want to Stay at Your House», 13:28-15:08** |
| [Swamp Jawn](https://www.youtube.com/watch?v=Xv9MdoAt3gQ&t=142s) (9:33) | Anticipación 0:47 · **espaciado de fotogramas 2:22** · primer plano 3:42 · impacto 5:31 · secuela 8:15 |
| [MankoMan](https://www.youtube.com/watch?v=j2nHAPtCjBk&t=585s) (23:27) | Por qué funciona 2:11 · dirección de arte 5:37 · diseños 7:46 · **«estilo Kanada» 9:45** · desglose 11:10-21:58 |

Episodios completos mirados (360p): [ep. 1](https://archive.org/details/cyberpunk_edgerunners_01_360),
[ep. 2](https://archive.org/details/cyberpunk_edgerunners_02_360),
[ep. 3](https://archive.org/details/cyberpunk_edgerunners_03_360),
[ep. 4](https://archive.org/details/cyberpunk_edgerunners_04_360),
[ep. 6](https://archive.org/details/cyberpunk_edgerunners_06_360),
[ep. 7](https://archive.org/details/cyberpunk_edgerunners_07_360),
[ep. 9](https://archive.org/details/cyberpunk_edgerunners_09_360).
Tráiler oficial VOSE: [Dailymotion](https://www.dailymotion.com/video/x8ct6i8) (2:59).

---

## 13 · Videojuegos de la franquicia

### 13.1 *Cyberpunk 2077* y el parche «Edgerunners» (1.6)

El **6 de septiembre de 2022**, una semana antes de la serie, salió el
**parche 1.6 «Edgerunners Update»** ✅
([notas oficiales](https://www.cyberpunk.net/en/news/45280/edgerunners-update-patch-1-6-list-of-changes),
[wiki](https://cyberpunk.fandom.com/wiki/Edgerunners_Update), [Xbox Wire](https://news.xbox.com/de-de/2022/09/06/cyberpunk-2077-edgerunners-update/)):

- **Recreativa *Roach Race***: minijuego nuevo en **máquinas de arcade
  de Night City**, entre ellas las de los pisos de V en **Northside,
  Japantown y The Glen**. Con **tabla de récords** y premios ✅. Es un
  corredor 2D con **Sardinilla, la yegua de Geralt de *The Witcher***.
  Tiene versión gratis para móvil ✅ ([Game8](https://game8.co/games/Cyberpunk-2077/archives/Roach-Race-Arcade-Game-Location),
  [Gamer Guides](https://www.gamerguides.com/cyberpunk-2077/guide/edgerunners-patch-1-6/roach-race/how-to-find-and-win-the-roach-race-arcade-game)).
  **Esta es la conexión real entre Edgerunners y la recreativa.**
- Misión **«Over the Edge»**: da **la chaqueta de David** (la de Gloria)
  ✅ (Game8, Den of Geek).
- **Guts**, la escopeta de Rebecca (rosa y verde menta), escondida en los
  arbustos de **Memorial Park** ✅ ([Den of Geek](https://www.denofgeek.com/games/how-to-get-cyberpunk-edgerunners-equipment-2077/)).
- El traje de Lucy y otros objetos ✅ ([Attack of the Fanboy](https://attackofthefanboy.com/guides/all-edgerunners-items-weapons-and-easter-eggs-in-cyberpunk-2077-and-where-to-find-them/)).
- **Modo foto**: 10 **pegatinas** con imágenes de la serie y **fotos
  en vertical** (giro de 90°) ✅ (wiki + [VULKK](https://vulkk.com/2022/09/07/cyberpunk-2077-patch-1-6-everything-you-should-know-about-the-edgerunners-update/)).
  Para «sube tus capturas», es perfecto.
- En el Afterlife se puede pedir **«The David Martinez»** ✅.

**El efecto**: tras la serie y el parche, *2077* tuvo su **récord de
jugadores simultáneos en Steam desde el lanzamiento** (136.724 el 25 de
septiembre de 2022) y **1 millón de jugadores al día** ✅
([Engadget](https://www.engadget.com/cyberpunk-2077-edgerunners-popularity-spike-161756943.html),
[Forbes](https://www.forbes.com/sites/paultassi/2022/09/16/cyberpunk-2077s-playercount-is-up-nearly-300-thanks-to-edgerunners/),
[ComicBook](https://comicbook.com/gaming/news/cyberpunk-2077-edgerunners-anime-release-players/),
[80.lv](https://80.lv/articles/cyberpunk-2077-got-record-concurrent-players-on-steam-since-release)).
**Una serie que hizo volver a la gente a jugar**: por eso encaja en
#a-que-juegas.

### 13.2 Más recreativas en el juego (parche 2.0)

- ***Trauma Drama***: plataformas retro, eres del Trauma Team; máquina en
  la tienda de netrunners junto al viaje rápido del **mercado de Kabuki** ✅.
- ***Arasaka Tower 3D***: disparos al estilo *Doom*; máquina cerca del
  viaje rápido «Protein Farm» ✅.
  ([TheGamer](https://www.thegamer.com/cyberpunk-2077-patch-version-2-0-arcade-games-arasaka-tower-3d-trauma-drama/),
  [Charlie INTEL](https://www.charlieintel.com/cyberpunk-2077/cyberpunk-2077-2-0-how-to-find-trauma-drama-arasaka-tower-3d-arcade-games-275289/))
- Nombre para la lámina: una recreativa de **Arasaka Tower 3D** es un
  guiño doble (el final de la serie pasa en la Torre Arasaka).

### 13.3 La interfaz del juego (para el cuadro de diálogo)

- Subtítulo: nombre coral `#FE6962` + texto cian `#59E6F0`, Rajdhani ✅
  (§7.2).
- Menús: fondo negro, **filetes rojos o cian con esquinas cortadas a
  45°**, amarillo `#F8EE08` para lo importante ⚠️ (de memoria; Game UI
  Database no se dejó leer).
- **Tabla de récords** de *Roach Race* (§7.2) ✅.
- **Mensajes del teléfono** y holo-llamadas ⚠️.

### 13.4 Lo que viene: *Cyberpunk: Edgerunners 2* (20-oct-2026)

- Se estrena en Netflix el **20 de octubre de 2026** (dentro de un mes)
  ✅ ([Netflix Tudum](https://www.netflix.com/tudum/articles/cyberpunk-edgerunners-2-release-date-news),
  [Seat42F](https://seat42f.com/cyberpunk-edgerunners-2-trailer-netflix-premiere-date/),
  [GamesRadar](https://www.gamesradar.com/entertainment/anime-shows/cyberpunk-edgerunners-season-2-release-date-trailer-story/)).
- **Otra historia y otro equipo**: Román, Weak «King», D (netrunner de
  Snake Nation) y Talia (de Maelstrom). Dirige **Kai Ikarashi** (el del
  ep. 6 de la primera) ✅ (GamesRadar, [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Cyberpunk:_Edgerunners_II)).
  Doblaje latino ya en marcha (Weak = Jorge Badillo, Avida Yang = Rebeca
  Manríquez) ⚠️ una fuente.
- **Para la lámina**: la gente del servidor hablará de ella en octubre;
  pero **la lámina debe ser de la primera temporada** (los personajes
  conocidos). No mezclar equipos.

### 13.5 Segunda pasada · juegos

- **The Cutting Room Floor** tiene página de *Cyberpunk 2077*
  ([tcrf.net](https://tcrf.net/Cyberpunk_2077)): un modo en tercera persona
  descartado, el cambio de nombre del mapa (`01_nightcity` →
  `03_night_city`) y cambios regionales por censura. Nada de recreativas ni
  de Edgerunners. ⚠️ Visto sólo por el extracto del buscador: la página da
  403 (Cloudflare) y no hay copia en Wayback.
- **Cruces con otros juegos** (Overwatch, Apex Legends, Fortnite): ver
  «Punto 23».

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todos reconocen

- **La luna**: «I'll take you to the moon» y el final de Lucy sola en la
  luna. Es el golpe emocional de la serie.
- **La chaqueta amarilla de David** con el emblema verde a la espalda.
- **Rebecca**: su tamaño, sus dos pistolas, **Guts**, sus brazos de
  gorila, su lealtad. Es la **«duende asesina»** («murder goblin») del
  fandom ✅ ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/CyberpunkEdgerunnersTheCrew)).
- **«Welcome to the crew»** y el reparto a partes iguales.
- **La bebida «The David Martinez»** del Afterlife… que lleva **NiCola,
  un refresco con gas**, algo que David **odiaba** (ep. 2, 16:34): ni
  muerto tiene suerte ✅ ([TV Tropes YMMV](https://tvtropes.org/pmwiki/pmwiki.php/YMMV/CyberpunkEdgerunners)).
- La broma de que Edgerunners **tiene el mismo argumento que *La LEGO
  película*** (chico corriente, chica punk llamada Lucy con el pelo de
  colores, torre malvada) ✅ (TV Tropes).
- El chiste de «Davis» (ep. 4, 04:02) ✅ subtítulo.
- El «**Preeem!**» de Pilar y su «**Bro!**» ✅ subtítulo.
- La **tumba de Rebecca** que los jugadores buscan en *2077* («I found
  Rebecca's grave!», r/cyberpunkgame, 2.338 votos) ⚠️.

### 14.2 Qué NO hacer (lo que un fan notaría)

- **Infantilizar a Rebecca**. El fandom se enfada con los chistes de
  «es una niña»: **tiene unos 20 años** ✅ (TV Tropes YMMV; wiki).
  Dibujarla como adulta bajita, no como niña; nada de poses sexualizadas.
- **Poner a Adam Smasher simpático** o a Kiwi como amiga fiel sin más: el
  fan recuerda la traición.
- **Usar la escena de la muerte** de David, Rebecca o Maine para un
  canal alegre. Tampoco la luna del ep. 10.
- **Colores pastel alegres** o luz de día plana para Night City: la
  serie es **noche, neón y negro** (regla 6 del dueño: tono de la serie).
- **Mezclar la temporada 2** con la 1 (§13.4).
- **Burbuja blanca** o letras de cómic (§7.6).
- **Logos o juegos reales** de otras marcas en la pantalla de la
  recreativa (Nintendo, *Street Fighter*…). En Night City las
  recreativas son **Roach Race, Trauma Drama, Arasaka Tower 3D**.
- **Chaqueta de David amarilla limón plana**: es un amarillo de
  emergencias con sombra **naranja** `#C26D03` y forro cian.
- **Lucy con el pelo blanco liso**: lleva el **degradado pastel** en las
  puntas (§16).

### 14.3 Segunda pasada · más cosas que NO hacer

- **Rebecca, nunca infantilizada ni sexualizada**. Ahora con el origen de
  la polémica: tras el ep. 3 (13-sep-2022) el fandom discutió si su diseño
  era un cliché «loli»; el 16-sep el dibujante **@FracturedInn** publicó un
  cómic de 4 viñetas que llegó a **9.000 «me gusta» en 3 días** ✅
  ([KnowYourMeme](https://knowyourmeme.com/memes/rebecca-edgerunners-character)).
  Dibujarla adulta (unos 20 años), con volumen real.
- **No quitarle ni inventarle tatuajes a Rebecca**: lleva **«PKDICK»**
  (por Philip K. Dick) y una **calavera de cabra** (guiño a *Shadowrun*) ✅
  ([wiki: Rebecca](https://cyberpunk.fandom.com/wiki/Rebecca), Trivia).
- **No hacer chiste del pasado de Kiwi** (joytoy, la mandíbula). Si sale,
  con la máscara puesta y sin explicarlo.
- **No enseñar la violencia de frente**: en la muerte de Maine (ep. 6,
  22:10-22:48) Trigger no muestra el disparo ni el cuerpo; usa el visor
  que se rompe y un fogonazo. Si una lámina toca algo duro, elipsis.
- **No usar el filtro verde entero de la luna** (ep. 4, 21:20-21:58) en un
  canal alegre: es la escena más triste.
- **No pintar telas con estampado** (cuadros, camuflaje, pata de gallo): la
  ropa de la serie es de color plano con ribetes (ver «Punto 19»).

---

## 15 · Poses analizadas por personaje

Números W (wiki, en `hojas/`) y G (GitHub, en `herramientas/…`), o
episodio y minuto. Lo que describo de W y G **lo he visto** en las hojas
✅; lo de los episodios sin imagen, de memoria ⚠️.

### Rebecca

| Ref. | Postura | Manos | Mirada / gesto | Sirve para |
|---|---|---|---|---|
| G09 (render) | De pie, cadera de lado, sudadera gigante | **En los bolsillos** | Sonrisa de pilla, cabeza ladeada | **Presentar, saludar** |
| W46 / G25 | De pie en el grupo | **Detrás de la nuca** | Sonrisa relajada | **«Me apunto»** |
| W20 = G10 (cuenta atrás «11 days») | **Agachada**, pierna adelantada | Pistola **apuntando al espectador**, la otra mano abierta | Boca abierta, ojos enormes | **Animar, retar** («¿quién se apunta?») |
| W9 | De frente, en el aire | **Dos armas** (brazos de gorila) disparando | Grito | **Celebrar** a lo grande |
| G33 | Brazos de gorila **arriba**, puños cerrados | Puños | Risa con los ojos cerrados, fondo de día | **Celebrar** |
| W79 | Primer plano | Pistola rosa junto a la cara | **Guiño** | **Invitar, complicidad** |
| W65 | Subida a algo, brazo estirado | Pistola por encima de la cabeza de David | Ojos redondos; David se agacha | **Explicar** (enseña a disparar) |
| W66 | Sentada en la galería de tiro, cascos rosas | Pistola en las dos manos | Seria, concentrada | **Pensar / prepararse** |
| W30 (cartel amarillo) | Agachada | Una mano arriba | Mirada fija, cara seria | **Regañar** (mirada que juzga) |
| W116 | Sentada en el respaldo del sofá | Una mano saluda | **Guiño y lengua fuera** | **Pasar el rato** |

### Lucy

| Ref. | Postura | Manos | Mirada / gesto | Sirve para |
|---|---|---|---|---|
| G05 (render) | Medio cuerpo, hombros caídos | Ocultas | Cabeza ladeada, **media sonrisa** | **Presentar, invitar** |
| W28 (cartel amarillo) | Tres cuartos | **Pistola levantada** junto a la cabeza | Seria, mirada al espectador | **Regañar, advertir** |
| W17 (cuenta atrás «13») | Busto | Cigarro en la boca | Ojos entornados | Tono frío |
| W64 (ep. 4) | Apoyada en la barandilla de una azotea, **capucha puesta** | Brazos cruzados sobre la baranda | Mira la ciudad | **Pensar** |
| W104 (vinilo) | **Sentada abrazando las rodillas** en un alféizar | Sobre las rodillas | Media sonrisa hacia abajo | **Pensar, esperar** |
| W63 (ep. 7) | En la oscuridad | — | **Ojos rojos brillando** (hackeando) | Interfaz, tensión |
| G41 / W45 | En el tren, acercándose | — | Escanea con HUD rojo | **Explicar** (datos) |
| G42 / W49 (ep. 2) | Tumbada con la corona del BD; en el rover lunar | Al volante | Ríe (ep. 2, 21:18 「アハハハッ」) | **Celebrar suave** («mira este juego») |
| W116 | Sentada en el sofá | Bolsa de gofres | Guiña, sonríe | Pasar el rato |

### David

| Ref. | Postura | Manos | Mirada / gesto | Sirve para |
|---|---|---|---|---|
| W26 (cartel amarillo) | Tres cuartos, echado adelante | **Se señala con el pulgar** | **Sonrisa enorme, boca abierta** | **Presentar** («este soy yo»), **animar** |
| W127 (vinilo) | De pie, piernas abiertas | **Manos en los bolsillos**; radiocasete al lado | Mira abajo, seguro | **Presentar** |
| W46 / G25 | Caminando en el grupo | En los bolsillos | Sonrisa ladeada | **«Me apunto»** |
| G26 | **De espaldas**, el emblema verde a la vista | En los bolsillos | — | «Vamos» |
| W14 (cuenta atrás «12») | Disparando | Pistola, **«BLAM BLAM»** | Gritando | Acción |
| W15 (cuenta atrás «6») | Busto, cara verde con marcas rojas | — | Mirada dura | Tensión |
| W116 | Tirado en el sofá | **Lata en la mano** | Sonrisa de dientes | **Pasar el rato** |
| G01 (render) | Busto | — | Ceño serio | Presentar serio |

### Maine

| Ref. | Postura | Manos | Mirada / gesto | Sirve para |
|---|---|---|---|---|
| W29 (cartel amarillo) | Busto enorme, visor, capucha roja | — | **Sonrisa de lado con dientes**, desde arriba | **El jefe que te acepta** |
| G13 (render) | Busto de tres cuartos | — | Sonrisa torcida | Presentar |
| W46 | Caminando | Brazo sobre Dorio | Carcajada | «El equipo» |
| W75 (vídeo ending) | Sentado en el reservado del bar | Bebida | Relajado | Después de la partida |
| ep. 3, 18:00 ([IA](https://archive.org/details/cyberpunk_edgerunners_03_360)) | De espaldas en la barra del Afterlife, capucha roja con banda reflectante subida | Sobre la barra | Justo cuando dice «Everybody gets a fair shake. Only way I operate.» (18:02) ✅ | **Marcar las reglas, repartir** |
| ep. 6, 22:22-22:24 ([IA](https://archive.org/details/cyberpunk_edgerunners_06_360)) | De espaldas, caminando por las Badlands junto a Dorio; hombros anchos, paso firme | Sueltas | No se le ve la cara; la capucha lo delata ✅ | **Liderar, ir al frente** |

### Kiwi

| Ref. | Postura | Manos | Mirada / gesto | Sirve para |
|---|---|---|---|---|
| W27 (cartel amarillo) | Tres cuartos | Cigarro junto a la máscara, algo colgando de la otra mano | Ojos entornados | **Explicar con sorna** |
| W25 | De pie en un pasillo oscuro | Una mano a la altura de la cadera | Mira de reojo | Presentar |
| W18 (cuenta atrás «3») | Caminando con **una hiena con correa** | Sujeta la correa | De perfil | Humor raro |
| W33 | Hoja de diseño de la máscara | — | — | Detalle |
| ep. 7, 11:40 ([IA](https://archive.org/details/cyberpunk_edgerunners_07_360)) | De perfil en el Afterlife junto a Faraday, media máscara puesta | — | Seria; poco después de la llamada «KIWI» (11:25) ⚠️ reconocida por diseño, no por el audio | **Vigilar, presentar con cautela** |
| ep. 9, 5:39 ([IA](https://archive.org/details/cyberpunk_edgerunners_09_360)) | Sentada en un sofá, a punto de dormirse; David de pie la mira (5:42) | Caídas | Cara triste, agotada tras la muerte de Maine ✅ | **Bajón del grupo, vulnerabilidad** |

**Resumen por intención** (para elegir rápido):

| Intención | Mejor pose |
|---|---|
| **Presentar** | David W26 (pulgar) · Rebecca G09 (bolsillos) · Lucy G05 |
| **Explicar** | Lucy G41 (escaneo) · Rebecca W65 (enseñando) · Kiwi W27 |
| **Celebrar** | Rebecca G33 (puños) · Rebecca W9 (dos armas) |
| **Regañar** | Lucy W28 (pistola arriba) · Rebecca W30 (mirada fija) |
| **Pensar** | Lucy W64 (barandilla) · Lucy W104 (rodillas) |
| **Animar / invitar** | Rebecca W20 (apunta al espectador) · Rebecca W79 (guiño) · David W26 |

---

## 16 · Vestuario (colores medidos ✅ salvo aviso)

### David
- **La icónica**: la **chaqueta amarilla de técnica de emergencias** de
  su madre (cuello alto, forro **cian luminoso** `#39CAF8`, **emblema
  verde pintado en la espalda**: el logo de la XBD «Edgerunners» de Jimmy
  Kurosaki, un programa de braindance dentro de la ficción, no el logo de la
  serie; ver «Segunda pasada» abajo). Amarillo en luz `#FDCB1D`
  / `#DCC007`, sombra **naranja** `#C26D03` ✅ (G01, G25, G26; wiki).
- Debajo: camiseta negra, **dos cadenas de oro** (la de abajo con una
  cruz), pantalón de chándal gris corto con **dos tiras amarillas**,
  zapatillas blancas con tiras azules ✅ (wiki; W26 se ve la cadena).
- Pelo **castaño** `#824736` con tupé y **laterales rapados** ✅.
- Al principio: **uniforme de la Academia Arasaka** (ep. 1; W93 tiene el
  diseño). Al final: sin camiseta, más músculo e implantes.

### Lucy
- **Pelo**: blanco natural con **degradado pastel**: rosa-lila arriba
  `#FFE0FA`, lavanda azulada `#D5E7FA`, puntas **menta** `#C9FFD8` y
  **amarillo pálido** `#FEFBC5`; **media melena asimétrica**, más larga
  a la izquierda ✅ (medido en la **guía oficial de cosplay**, W4-W7).
- **Maquillaje**: triángulos **rojos** bajo los ojos y labios rojos
  `#E74C4C` ✅ (W4).
- Ropa: **chaqueta blanca corta** `#FEEDFB`, **malla negra de netrunner
  con ribetes rojos** (tono `#554B6C` con la luz), shorts blancos,
  medias grises, botas negras altas ✅ (wiki + W4-W6).
- **Puerto de buceo** en la nuca (lo tapa con piel sintética) y **tatuaje
  rosa** `#D4A8C9` en la espalda, como un corazón a lo largo de la
  columna ✅ (W5, W7). Arma: el **monofilamento** (cable cortante) ✅.
- De niña (W6): **mono gris oscuro** de Arasaka con ribetes rojos.

### Rebecca
- **Pelo turquesa-menta** `#BAFBDC` en **dos coletas** con diadema de
  dos pinzas ✅ (G09; wiki).
- **Chaqueta negra enorme de cuello alto** con **ribetes lima** `#ACDE41`
  (azul marino con luz `#34426B`), medio abierta; debajo, sujetador y
  braga negros; zapatillas a juego ✅.
- **Tres tatuajes rosas** `#F98AAA`: uno en el cuello, una **cabeza de
  cabra** en el vientre y en el muslo derecho uno que dice «PK DICK» ✅
  (W8, W24; wiki).
- **Ojos-implante** rosas y amarillos ✅ (G09, W79).
- Arma: **Guts**, escopeta **rosa y verde menta** ✅. Después, **brazos
  de gorila** rojo (derecho) y azul (izquierdo) ✅ (G33; wiki).
- Piel muy blanca con un toque azul ✅ (wiki; se ve en G09).

### Maine
- Abrigo **azul petróleo** `#102837` con **forro rojo** `#CD234D` y
  **hombreras amarillas** `#F9F92D`; capucha/bufanda roja o naranja;
  **visor**; cuerpo lleno de cromo ✅ (G13, W29).

### Kiwi
- **Abrigo rojo largo** (granate en sombra `#4A203F`), **máscara roja**
  sobre la mandíbula, **bob rubio claro** `#DCFEFA` con luz fría ✅ (G16,
  W25, W27; wiki).

### Falco, Pilar, Dorio (rápido)
- **Falco**: chaleco marrón, camisa blanca de cuello alto, un brazo
  cibernético plateado, cinturón de balas amarillo, bigote ✅ (wiki; G18).
- **Pilar**: brazos mecánicos plateados larguísimos, chaleco negro,
  gafas-visor, pelo negro de punta ✅ (G20, W32).
- **Dorio**: grandota, rubia, abrigo azul ✅ (W31).

### Lo que todos reconocen
La **chaqueta amarilla de David**, el **pelo arcoíris pastel de Lucy** y
las **coletas menta con la sudadera gigante de Rebecca**. Si sólo se ve
una silueta, que sea una de estas tres.

### Segunda pasada · el emblema y la chaqueta real

- **El emblema verde** de la espalda ✅: no es el logo de la serie, sino el
  de la **XBD «Edgerunners» de Jimmy Kurosaki** (32 episodios de
  braindance dentro de la ficción; sale en el ep. 5). Lucy se lo proyectó
  en la chaqueta, a David le gustó y lo pintó a mano
  ([wiki: David's Jacket](https://cyberpunk.fandom.com/wiki/David%27s_Jacket),
  [wiki: Jimmy Kurosaki](https://cyberpunk.fandom.com/wiki/Jimmy_Kurosaki)).
  Un guiño dentro del guiño: si la lámina lo usa, que sea sabiéndolo.
- **La chaqueta existe de verdad** ✅: réplica oficial de **Insert Coin**,
  100 % algodón, forro reflectante, 167,49 $
  ([Crunchyroll News](https://www.crunchyroll.com/news/latest/2025/4/25/cyberpunk-edgerunners-anime-insert-coin-david-jacket),
  [Insert Coin](https://www.insertcoinclothing.com/outerwear/david.html)).
  Sirve para ver costuras, cuello alto y forro de una prenda real.
- **Lucy con la chaqueta que «flota»**: el cosplay de **Yaya Han** la
  sostiene con **espuma EVA de 2 mm forrada** para que no caiga
  ([Yaya Han](https://www.yayahan.com/post/cosplaying-lucy-from-cyberpunk-edgerunners)).
  Ver «Punto 23».

---

## 17 · Paisajes y fondos de pantalla

### 17.1 Los sitios, con su luz y su hora

| Sitio | Hora | Luz | Ref. |
|---|---|---|---|
| Calles de Santo Domingo / Arroyo | Noche | Naranja de sodio y negro | W46, G26, G49 (juego) |
| Kabuki (Watson), piso de Lucy | Noche | Neón magenta y cian, bruma | G52-G55 (juego), W64 |
| **Estación y tren NCART** | Día y noche | De día crema y verde agua (W84); de noche cian | W84, G46 |
| **Afterlife** | Noche | **Verde menta** desde la barra | W117 |
| Bar / reservado del ending | Noche | Azul marino con filos cian | W75 |
| Azoteas | Noche | Azul frío, ciudad de fondo | W64, G58 |
| Calle con neón «Blue Moon» | Noche | Azul y magenta | W118 |
| Luna (BD y final) | — | Gris lunar, Tierra azul | W49, G29, G30 |
| Badlands | Día | Amarillo polvo | W91 |

### 17.2 Fondos de pantalla

- **Oficiales** (wiki, tamaño real): W2 aniversario **3840×2160**, W3
  «Summer Vibes» **3840×2160**, W1 cartel **2765×4101**, W118 lienzo
  «Slice of Life» 1015×716, W116 lotería 1000×800 ✅.
- **Fan**: fondo animado de la luna en GitHub (Manadrah, 3840×2160);
  Wallpaper Engine en Steam (4K); webs de fondos (§4.4).
- **Del juego**: capturas en modo foto (el parche 1.6 añadió fotos en
  vertical) y fondos de *2077* en [cyberpunk.net](https://www.cyberpunk.net/)
  ⚠️ no revisé cuáles.

---

## 18 · Guía para generar con IA (Firefly, Canva)

**Regla del dueño y del encargo**: los **personajes NO se generan con
IA**; salen de fotogramas o arte oficial y se integran con
`v3/integrar.py`. La IA sirve para **fondos, objetos y luz** coherentes
con la serie. (Además, Firefly rechaza personajes con marca.)

### 18.1 Lo que nunca cambia (para comprobar el resultado)

- **David**: chaqueta amarilla con sombra naranja y forro cian; pelo
  castaño en tupé con laterales rapados; dos cadenas de oro.
- **Lucy**: media melena asimétrica blanca con degradado pastel (rosa,
  lavanda, menta, amarillo); triángulos rojos bajo los ojos; chaqueta
  blanca corta sobre malla negra con ribetes rojos.
- **Rebecca**: bajita; dos coletas menta; sudadera negra gigante con
  ribetes lima; tatuajes rosas; ojos rosa y amarillo.
- **Maine**: enorme, rubio, visor, abrigo azul petróleo con forro rojo.
- **Kiwi**: alta, abrigo rojo largo, máscara roja en la mandíbula, bob
  rubio claro.

### 18.2 El estilo

- **Línea**: contorno negro limpio de grosor variable, más grueso por
  fuera; **sin** líneas de boceto.
- **Sombreado**: **cel de dos tonos**, sombras **planas y duras**, a
  veces una sombra de color (magenta o verde) en vez de gris.
- **Color**: negro casi puro `#030309` + **un** neón fuerte por escena
  (lima `#BAF812`, magenta `#F246B3`, cian `#39CAF8`, amarillo
  `#F8EE08`, menta `#7CF6CC`). Paleta de §5.
- **Luz**: de noche; farolas de sodio naranjas, neones, pantallas.
  Contraluz y **borde de luz de color** en los personajes.
- **Encuadre**: angulares exagerados, contrapicados, líneas de velocidad;
  Trigger deforma la perspectiva.
- **Detalles del mundo**: cables colgando, pantallas publicitarias
  gigantes, carteles en japonés e inglés, pegatinas, grafitis, charcos,
  vapor de alcantarillas, trenes elevados.

### 18.3 Palabras que ayudan

`2D anime background, Studio Trigger style, cel shading, flat hard
shadows, thick clean outlines, night, neon signs, rain, wet asphalt
reflections, narrow alley, elevated train track, hanging cables,
Japanese and English signage, lime green and magenta neon, near-black
shadows, dramatic low angle, wide-angle lens distortion, arcade
cabinet with CRT glow`

### 18.4 Palabras que lo estropean

`photorealistic`, `3D render`, `Unreal Engine`, `octane`, `hyper
detailed`, `soft painterly`, `watercolor`, `pastel kawaii`, `chibi`,
`bokeh everywhere`, `lens flare`, `sepia`, `daylight`, `sunny`, `Blade
Runner` (marca ajena), `Matrix code`, `speech bubble`, nombres de juegos
reales en la pantalla, `sexy` / `pin-up` (sobre todo con Rebecca).

### 18.5 Qué imágenes usar como referencia

- **Estilo de fondo**: W118 («Slice of Life»), W84 (ciudad de día con el
  tren), W117 (Afterlife), G56-G57 (panorámicas).
- **Estilo de personaje (para comprobar, no para generar)**: W26-W32
  (carteles amarillos), G01-G20 (renders).
- **Luz de grupo de noche**: W46 / G25-G26.
- **Composición «pasar el rato»**: W116, W75.
- **Paleta promocional**: W2 (lima), G06 (magenta), G10 (lima).

### 18.6 Segunda pasada · más pistas para la IA de imagen

- **La chaqueta de Lucy flota, no cae**: tiene cuerpo (en el cosplay de
  Yaya Han, espuma EVA de 2 mm forrada). Pedir `stiff cropped jacket
  standing away from the body`; evitar `flowing`, `draped`.
- **Aberración cromática y grano**, suaves: `subtle chromatic aberration
  on edges, light film grain`. Sólo en logo, pantallas y glitches, no en
  toda la imagen.
- **La velocidad se dibuja**: la Sandevistan son **copias de color del
  personaje**, fotograma a fotograma, no un desenfoque. Pedir `colored
  afterimages trailing, smear frames, Kanada-style effects animation`;
  evitar `motion blur`.
- **Un solo acento por plano** (medido en §5.5): `near-black blue night
  #000C24, single cyan accent`. Si hay verde, el del HUD `#0C5400`, no el
  de visión nocturna.
- **Ropa de color plano**, sin estampado: evitar `plaid`, `camo`,
  `pattern fabric`.
- **Carteles del fondo**: los logos de Arasaka, Militech, Kiroshi y Trauma
  Team (ver «Punto 19»), recreados, nunca pegados.
- **Referencia de pose relajada**: la figura de Lucy de Prime 1 Studio
  apoyada de espaldas en la barra del Afterlife
  ([Sideshow](https://www.sideshow.com/collectibles/cyberpunk-2077-lucy-prime-1-studio-914452)).

### 18.7 Guía para una IA de texto (escribir en su voz)

**Reglas de voz**

- **Frases cortas, de calle.** Nada de explicaciones largas: dicen una
  cosa y la rematan con jerga.
- **Jerga** (sin traducir): *choom*, *gonk*, *preem*, *nova*, *eddies*,
  *chrome*, *gig*, *delta*, *flatline* (glosario en «Punto 25»).
- **En latino**: «neurodanza» por *braindance*, «mocoso», «pana», «plata»
  para el dinero, groserías sin miedo pero sin relleno (§10).
- **Puntuación**: exclamaciones dobles en Rebecca (¡…!), puntos secos en
  Lucy y Kiwi, interrogaciones retadoras en David.
- **Onomatopeyas**: «BLAM» de las trazadoras (ep. 1, 0:48), «CHK» del
  manga, «ミシッ» (crujido); en español, «¡pum!», «¡clac!».
- **Emociones exageradas**: Rebecca se pasa de alegría y de rabia (「ブッころ！」
  «¡te mato!», ep. 9, 05:51); Lucy casi no sube la voz; David grita
  cuando se juega todo («Well so the fuck am I!», ep. 10, 17:10).

**Frases reales, por emoción** (subtítulo de Netflix o doblaje latino)

| Emoción | Frase | Quién, dónde |
|---|---|---|
| Alegre | «¡Preeem!» | Pilar, ep. 4, 05:35 |
| Alegre | «¿Por qué tan serio, David? Deja de coquetear y mejor vamos a bailar» | Rebecca, latino, [clip](https://www.youtube.com/watch?v=2I4ONpf9W3k) 10:35 |
| Alegre | 「イーハー！」 («¡yija!») | Rebecca, ep. 7, 03:45 |
| Enfadado | «Well so the fuck am I!» | David, ep. 10, 17:10 |
| Enfadado | 「ブッころ！」 («¡te mato!») | Rebecca, ep. 9, 05:51 |
| Explicando | «Edgerunners? It's another word for cyberpunk.» | Lucy, ep. 2, 17:01 |
| Explicando | «Riesgo enorme, pero la plata es jugosa. Si no quieren arriesgarse, será mejor que se vayan» | David, latino, [clip](https://www.youtube.com/watch?v=2I4ONpf9W3k) 8:51 |
| Explicando | «Everybody gets a fair shake. Only way I operate.» | Maine, ep. 3, 18:02 |
| Animando | «I believe in you, Lucy.» | David, ep. 6, 07:12 |
| Animando | «No te preocupes, yo te cuido» | Rebecca, latino, [clip](https://www.youtube.com/watch?v=2I4ONpf9W3k) 11:40 |
| Animando | «Fast is what you do, remember? Keep running.» | Maine, ep. 6, 22:32 |
| Triste | «Sorry. Wish we could go to the moon together.» | David, ep. 10, 22:25 |
| Triste | «You're remembered by how you die.» | Lucy, ep. 4, 21:29 |
| Frío | «Never trust a soul in Night City.» | Kiwi, ep. 9, 04:51 |

**Vocabulario de expresiones para la IA de imagen** (esta serie no usa
gotas de sudor ni *chibi*; su «idioma» de gestos es otro):

- **Ojos**: pupilas que **tartamudean y se duplican** en la cyberpsicosis
  (`glitching doubled eyes`); ojos muy abiertos de shock (David, ep. 6,
  22:26).
- **Fondos de emoción**: **filtro de un color entero** (verde de visión
  nocturna en la tristeza, ep. 4, 21:20; verde militar en la tensión,
  ep. 3, 4:55); fogonazo blanco en el golpe final (ep. 6, 22:44).
- **Glitch** y aberración cian/magenta cuando algo se rompe.
- **Sonrisa de lado con dientes** (Maine, Rebecca) para la chulería.
- **Nada de chibi, gotas ni venitas**: se sale del tono (§14).

---

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

*(Sección nueva de la segunda pasada. Los puntos 18 a 25 del encargo van
aquí seguidos, antes de los conceptos.)*

### 18.a Cómo lo hizo Trigger (según entrevistas)

- **2D nítido de trazo grueso con memoria de anime de los 70-90** ✅
  ([Animation World Network](https://www.awn.com/animationworld/cyberpunk-edgerunners-vibrant-ode-retro-anime),
  con citas de la entrevista de Netflix a Otsuka, Imaishi y Yoshinari).
- **La Sandevistan se anima a mano**: repartieron los fotogramas de la
  acción y rellenaron los huecos con **copias del personaje en colores
  distintos**. Yoshinari: «un estilo que existía en el anime japonés
  antiguo… lo desempolvamos» ✅ (AWN). Los análisis lo llaman **«estilo
  Kanada»** ([MankoMan, 9:45](https://www.youtube.com/watch?v=j2nHAPtCjBk&t=585s)) y
  explican el **espaciado de fotogramas** ([Swamp Jawn, 2:22](https://www.youtube.com/watch?v=Xv9MdoAt3gQ&t=142s)).
- **El buceo en la red** (netrunners) se dibujó con **referencias
  analógicas antiguas**, no copiando el juego (Imaishi) ✅ (AWN).
- **Fondos pintados encima de capturas de Night City** del juego (ya en
  §3, *Inside Look #2*, 2:05-2:39) ✅.
- **Programa exacto** (RETAS, Clip Studio, Toon Boom): **no lo encontré**
  en entrevistas en inglés ni japonés. Lo habitual en Trigger es 2D en
  RETAS o Clip Studio y 3D propio para vehículos; **no confirmado para
  esta serie** ⚠️.

### 18.b Lo que se ve

- **Línea**: gruesa; en escenas de neón se **tiñe de cian o magenta**; muy
  marcada en los primeros planos de acción ⚠️ (visto en las hojas, sin
  medir un fotograma nuevo).
- **Sombreado**: cel plano de 2-3 tonos; degradados sólo en neones y
  hologramas ✅.
- **Filtros**: **un color entero** en escenas clave (verde militar en el
  braindance, ep. 3, 4:55-8:20; verde de visión nocturna en la promesa de
  la luna, ep. 4, 21:20-21:58; HUD verde roto de Maine, ep. 6, 22:10) ✅
  visto. Grano suave y aberración cian/magenta en logo y glitches ⚠️ (una
  fuente, [playcyberpunk.com](https://www.playcyberpunk.com/cyberpunk_edgerunners_gif/)).

### 18.c Cómo reproducirlo en Photoshop

Capas, de arriba abajo:

1. **Línea** (Multiplicar), pincel duro de trazo grueso.
2. **Viñeta**.
3. **Aberración cromática**: duplicar, mover 2-3 px los canales R y B,
   modo Trama.
4. **Grano** (Superponer, 8-15 %).
5. **Neón** (Sobreexponer color o Trama): pincel blando, flujo bajo, varias
   pasadas ([Spoongraphics](https://blog.spoongraphics.co.uk/tutorials/how-to-apply-cyberpunk-style-color-grading-neon-effects-to-your-photos)).
6. **Sombra plana** (Multiplicar, 60-70 %).
7. **Color plano**.

Pinceles de glitch gratis: [Resource Boy](https://resourceboy.com/photoshop-brushes/glitch-brushes/)
(revisar la licencia de cada pack).

### 18.d Cómo reproducirlo en Blender

- **Contorno**: modificador **Solidify** con normales invertidas y
  material negro (grosor 0,01-0,03), o **Freestyle**. Para el contorno de
  color, material emisivo cian o magenta en el Solidify
  ([Artisticrender](https://artisticrender.com/cel-shading-in-blender/),
  [Blender Artists](https://blenderartists.org/t/the-ultimate-cel-shading-shader/1413344)).
- **Cel**: *Shader to RGB* + *Color Ramp* de 2-3 bandas duras en Eevee
  ([Medium, 4 métodos](https://medium.com/@josephclaytonhansen/four-different-methods-for-making-cel-shaders-in-blender-eevee-2-8-2-9-6d976ce2555d)).
- **Luz**: áreas de color (cian, magenta, amarillo) de lado; *Bloom*;
  niebla volumétrica baja para la lluvia.
- **Modelos libres** (fan-made, CC BY, crédito al autor; para pose, no
  para vender): [David](https://sketchfab.com/3d-models/none-0105aad132d04217ad2371da44b51f7a)
  (190.508 caras), [Rebecca](https://sketchfab.com/3d-models/none-c9a1a0795acc469bad9c0c47158e436b)
  (130.402), [Lucy](https://sketchfab.com/3d-models/none-7cc2f167a5e84a1aa0bc620ef9b5dcfd) ✅ (API de Sketchfab).
- **Texturas encima**: por UV, con ruido en la rugosidad para el «sucio»
  de Night City (texturas en «Punto 19»).

### 18.e Encuadres y composición

- **Contrapicado muy cerrado** en las peleas ⚠️ (visto en hojas).
- **Planos anchos y vacíos para la soledad**, primerísimos planos para la
  emoción fuerte ✅ (AWN y §2).
- **La cámara imita la Sandevistan**: paneos rápidos con estirones de
  fotograma (*smears*) en vez de interpolar limpio ✅ (AWN).
- **La muerte fuera de cuadro**: antes y después, nunca el golpe (ep. 6,
  22:10-22:48) ✅ visto.

---

## Punto 19 · Texturas 2D

Junto con §4 (3D y HDRI) y §5.4 (texturas reales), así no falta ninguna
capa.

- **Tramas del manga *MADNESS***: **rejilla fina** (no el punto clásico)
  en sombras de ropa y piel, **líneas de velocidad radiales** en la
  sorpresa, onomatopeyas a mano pegadas al borde (W124-W125, en
  `hojas/hoja_03.jpg`) ✅ visto. La otra parte del manga (W106, W108) va a
  color, sin trama, con cel de dos tonos y una viñeta de luz cálida.
  - Pinceles libres: [Manga Screentone Pack 1](https://assets.clip-studio.com/en-us/detail?id=2142037)
    (Clip Studio Assets, gratis) y el pack de
    [GraphicsBunker](https://www.graphicsbunker.com/brushes/free-comic-manga-screentone-brushes/)
    (Photoshop, Procreate, CSP) ⚠️ uso comercial sin aclarar.
- **Grano de papel**: [ambientCG Paper004](https://ambientcg.com/view?id=Paper004),
  **CC0**, hasta 2048×2048 ✅ (API). Hay Paper001-006 y Cardboard001-004
  para un grano más grueso o de revista vieja.
- **Pinceladas** (fondos pintados de Trigger): «My digital oil painting
  brushes (FREE)» de Martina Palazzese
  ([Behance](https://www.behance.net/gallery/71632077/My-digital-oil-painting-brushes-(FREE)-for-Photoshop)) ✅.
- **Glitch y aberración**: [Resource Boy](https://resourceboy.com/photoshop-brushes/glitch-brushes/) (ver Punto 18).
- **Emblemas y logos** (medidos por la API de la wiki; se ven pintados en
  las calles de la serie, hojas W46, W91, W99, W117) ✅. **Son de CD
  PROJEKT RED: sólo referencia; en la lámina se recrean**, no se pega el PNG.

| Logo | Tamaño | Enlace |
|---|---|---|
| Arasaka | 1920×1080 | [wiki](https://static.wikia.nocookie.net/cyberpunk/images/5/5f/Arasaka_Logo_CP2077.png) |
| Militech | 3840×582 | [wiki](https://static.wikia.nocookie.net/cyberpunk/images/6/67/Militech_Logo_CP2077.png) |
| Kiroshi | 502×116 | [wiki](https://static.wikia.nocookie.net/cyberpunk/images/a/ae/Kiroshi_Logo_CP2077.png) |
| Trauma Team | 3134×1064 | [wiki](https://static.wikia.nocookie.net/cyberpunk/images/c/c8/Trauma_Team_Logo_CP2077.png) |
| Maelstrom | 1389×675 | [wiki](https://static.wikia.nocookie.net/cyberpunk/images/1/19/Maelstrom_Logo_CP2077.png) |
| Tyger Claws | 1391×1059 | [wiki](https://static.wikia.nocookie.net/cyberpunk/images/4/4d/Tyger_Claws_Logo_CP2077.png) |
| Valentinos | 506×845 | [wiki](https://static.wikia.nocookie.net/cyberpunk/images/4/49/Valentinos_Logo_CP2077.png) |
| 6th Street | 1920×1080 | [wiki](https://static.wikia.nocookie.net/cyberpunk/images/c/c6/6th_Street_Logo_CP2077.png) |
| Kang Tao | 1920×407 | [wiki](https://static.wikia.nocookie.net/cyberpunk/images/5/5d/Kang_Tao_Logo_CP2077.png) |

- **Patrones de ropa**: **no hay**. Busqué camuflaje, cuadros y pata de
  gallo (en inglés) y la ropa es de **color plano con piezas y ribetes**.
  Es un dato: no inventar una tela estampada ⚠️ (comprobado que no sale,
  no es que no se buscara).

---

## Punto 20 · Gustos y detalles de cada personaje

No hay *databook* de fichas al estilo shonen: **no hay altura ni
cumpleaños oficiales** de nadie ⚠️ (buscado; las edades aproximadas las
dio el guionista en Reddit, §8). Lo que sigue sale de la
[wiki](https://cyberpunk.fandom.com/wiki/David_Martinez) (que cita el
*Mission Kit*) y de la serie.

| Personaje | Le gusta / le importa | Odia | Su objeto | Cómo se ve |
|---|---|---|---|---|
| **David** | Su madre; llegar alto (el sueño de Gloria) | Las bebidas con gas y el tabaco (ep. 2, 16:34); que le llamen «Davis» (ep. 4, 04:02) | El radiocasete de su madre (W127) y luego la Sandevistan | «Creo que estoy hecho diferente» (ep. 5, 18:00): se cree especial. Nació en 2058 |
| **Lucy** | Irse a la luna; **los gofres** (se la ve comiendo una bolsa en el sofá del grupo, W116) | Night City, «una jaula de luces» (ep. 7, 16:50) | El monowire | Introvertida, no habla de su pasado; apodo «Luce» |
| **Rebecca** | **Los perros** (llegó tarde a un encargo por abrazar un cachorro); su hermano Pilar | — | **«Guts»**, su escopeta Carnage modificada | Dura por fuera, compasiva por dentro («pobre gonk»); apodos Becca, Becs, «Lil' B» |
| **Maine** | Repartir a partes iguales; su «familia» de mercs; Dorio | — | Su visor y los brazos de cromo | El que reúne al equipo; ex boxeador y ex soldado |
| **Kiwi** | Sobrevivir; fue la mentora de Lucy | Confiar («Never trust a soul», ep. 9, 04:51) | La máscara de la mandíbula | Fría por necesidad |
| **Falco** | Su coche; cumplir su palabra (ep. 10) | — | Su camioneta | Nómada de acento sureño |

**Para la lámina**: la bolsa de gofres de Lucy o un cachorro de peluche
de Rebecca encima de la recreativa humanizan sin contar historias oscuras.

---

## Punto 21 · Por qué la gente la ama

**Las razones, con cifras**

- **Crítica y público**: **100 %** en Rotten Tomatoes (16 reseñas) y
  **95 %** del público (más de 2.500 valoraciones) ✅, leído en el JSON de
  la [página](https://www.rottentomatoes.com/tv/cyberpunk_edgerunners/s01).
- **Anime del Año** en los Crunchyroll Anime Awards 2023, 18 millones de
  votos ✅ (§9).
- **Devolvió la gente al juego**: el pico de jugadores de *Cyberpunk 2077*
  en Steam pasó de 10.000-15.000 a **más de 85.000 en 24 horas** tras el
  estreno ✅ ([PC Gamer](https://www.pcgamer.com/skyrocketing-cyberpunk-2077-player-counts-prove-the-netflix-boost-is-real/)).
  Otros medios hablan de «+300 %» y de volver a lo más vendido de Steam
  ⚠️ (Forbes dio captcha). **Es el dato perfecto para #a-que-juegas**:
  una serie que hizo que todos volvieran a jugar.
- **Con quién se identifica el público**: con **David**, el chico de la
  calle sin nada que perder que se lo juega todo por su familia elegida;
  y engancha el tema de **pagar un precio por mejorar el cuerpo** ⚠️ (una
  reseña de blog, Peter Joosten en Substack, más MyAnimeList).
- **Rebecca** como sorpresa (§9) y el **final sin trampas**: la broma de
  los foros es «disfruta tus nueve episodios de felicidad» ✅ (varias
  reseñas).

**Las escenas que hacen llorar**

| Escena | Ep. y minuto | Qué pasa | Por qué duele | Música y dibujo |
|---|---|---|---|---|
| **La luna del BD** | ep. 2, 19:30-21:30 | David y Lucy juegan en la luna con traje espacial y rover; ríen (21:18) | Es el único momento de paz, y el espectador sabe que es mentira | Suena **«I Really Want to Stay at Your House»**; sin diálogo |
| **La promesa** | ep. 4, 21:29-21:54 | «You're remembered by how you die» / «I'll take you to the moon! I promise!» | La promesa que no se cumple | **Filtro entero verde de visión nocturna**; Lucy de perfil llorando (21:34) ✅ visto |
| **Muere Maine** | ep. 6, 22:10-22:48 | «Fast is what you do, remember? Keep running.» | Se rompe la familia; David hereda el mando | Lluvia antes (18:25); visor que se agrieta, fogonazo blanco; **no se ve el disparo** ✅ visto |
| **El final** | ep. 10, 21:34-22:25 | Falco cumple la promesa; David, por boca de Falco: «Sorry. Wish we could go to the moon together.» | Mueren Rebecca y David; Lucy llega sola a la luna | Vuelve «I Really Want to Stay at Your House» (§11) |

**Las que hacen reír o gritar**: las pullas de Rebecca («Si no tuviera
bigote, te tendría enamorada», a Falco; «No voy a emborracharme con este
par de boomers») en el clip latino
[Momentos divertidos](https://www.youtube.com/watch?v=2I4ONpf9W3k)
(10:09 y 11:06, **1,9 M vistas**); y «Well so the fuck am I!» contra Adam
Smasher (ep. 10, 17:10).

**Cómo reaccionó la gente**: el hilo «I found Rebecca's grave!»
(r/cyberpunkgame, 2.338 votos, §14) y la tendencia de TikTok de David y
Lucy con la canción (§12). El hilo más votado sobre el final en
r/Edgerunners **no lo pude sacar** (Arctic Shift daba timeout) ⚠️.

---

## Punto 22 · Fan dubs y comunidad hispana

YouTube pide iniciar sesión desde el servidor: **las vistas y fechas de
los fandubs quedan sin confirmar** ⚠️. Los enlaces son reales.

**Fandubs en español latino**

| Vídeo | Escena | Enlace |
|---|---|---|
| Rebecca // Cyberpunk Edgerunners (Fandub Español Latino) | Rebecca | [YouTube](https://www.youtube.com/watch?v=-t0Hen4lR1U) ⚠️ vistas |
| La revancha de David contra Katsuo (Fandub Latino) | David vs Katsuo | [YouTube](https://www.youtube.com/watch?v=2tCe6MJt9kc) ⚠️ |
| David Martinez vs Adam Smasher (Demo de voz, Fandub) | Pelea final, ep. 10 | [YouTube](https://www.youtube.com/watch?v=rx3C3dUyjrA) ⚠️ |
| **Itsumoissho_Dubs**: «Los últimos minutos de Cyberpunk: Edgerunners», en dos partes | Final, ep. 10 | [TikTok](https://www.tiktok.com/@itsumoissho_dubs/video/7291039726017056006) ✅ existe |
| Retos de doblaje a la voz oficial de David | David | [SDV Servicios de Voz](https://www.tiktok.com/@sdv_serviciosdevoz/video/7152659901645360390?lang=es) (§12) |

**Covers en español**

- **«Let You Down» (ending)** en español, de **Cesar Powers** (2023) ✅
  ([Spotify](https://open.spotify.com/track/5Io7rX4u4LmLe45s1zKiHI),
  [Apple Music](https://music.apple.com/us/song/let-you-down-from-cyberpunk-edgerunners-spanish-cover/1668852365)).
- **«I Really Want to Stay at Your House»** (canción de la serie, no el
  opening) en español: [YouTube](https://www.youtube.com/watch?v=3OLCRvB6Chk) ⚠️ canal y vistas.
- *Lyric videos* traducidos en TikTok (p. ej. @kawaiirodri) y edits con
  «#subtitulosenespañol» (§12): más edición que doblaje ⚠️.

**Memes hispanos propios**: **no los encontré** (buscado «memes
Cyberpunk Edgerunners español latino reddit forocoches»). Circulan los
ingleses traducidos (Rebecca, §14). No digo que no existan.

**Para el servidor**: el clip oficial latino más visto,
[Momentos divertidos](https://www.youtube.com/watch?v=2I4ONpf9W3k)
(1,9 M), da escenas cortas y conocidas para un reto de fandub de Rebecca.

---

## Punto 23 · Colaboraciones, figuras y cosplay

**Videojuegos**

- **Overwatch × Edgerunners**: anunciado en BlizzCon 2026; David Martinez
  y Talia Yang llegan como aspectos en **2027**, con la temporada 2
  (20-oct-2026) ✅ ([MasGamers](https://www.masgamers.com/blizzard-y-cd-projekt-red-extienden-su-alianza-con-una-colaboracion-de-aspectos-de-cyberpunk-edgerunners-en-overwatch/),
  [PC Master Race LATAM](https://www.pcmrace.com/2026/09/13/cyberpunk-2077-edgerunners-2-battlenet/)).
- **Apex Legends × Edgerunners**: evento con aspectos y armas (julio) ⚠️
  una fuente ([CBR](https://www.cbr.com/apex-legends-cyberpunk-edgerunners-crossover/)).
- **Fortnite**: sólo una mención ⚠️
  ([MultiAnime](https://multianime.com.mx/2026/09/14/cyberpunk-edgerunners-ii-llegara-a-overwatch-y-fortnite-con-nuevas-colaboraciones-de-alto-voltaje-anime-cyberpunkedgerunners-games-crossovers/));
  sin nota de Epic.

**Ropa con licencia**

- **Insert Coin** (abril de 2025): chaqueta de David (167,49 $), camiseta
  de Lucy (27,91 $), camisa de Rebecca con iconografía rosa (33,49 $) ✅
  ([Crunchyroll News](https://www.crunchyroll.com/news/latest/2025/4/25/cyberpunk-edgerunners-anime-insert-coin-david-jacket),
  [tienda](https://www.insertcoinclothing.com/cyberpunk-edgerunners/)).
- **Nonsense** (Joey «The Anime Man», enero de 2024): camiseta «Netizen»
  amarillo neón, balaclava reflectante, y una **«Corporate Jacket»** con
  los logos de Arasaka, Militech y compañía ✅
  ([Tokyo Weekender](https://www.tokyoweekender.com/entertainment/entertainment-roundup-stylish-streetwear-with-cyberpunk-edgerunners-collaboration/)).
  Es la prueba de cómo quedan los logos del Punto 19 sobre algo real.
- **Atsuko**: aparece con línea de Edgerunners ⚠️ una fuente
  ([tienda](https://atsuko.com/collections/cyberpunk-edgerunners)).

**Merchandising oficial** ([CD PROJEKT RED Gear Store](https://gear.cdprojektred.com/collections/cyberpunk-edgerunners),
visto entero) ✅: réplica del **collar de David** (45 $), FigZero 1/6 de
David, figuras simples, **Funko Pop!** de David, Lucy (con monowire) y
Rebecca, peluches y vinilos de **Youtooz**, estatua de Lucy de
**Kotobukiya**, anorak de Adam Smasher de **ARK8**, lámpara y una
**caja-diorama del apartamento de David** (145 $). Pistas de qué objetos
ya son icónicos: el collar, el llavero de Guts.

**Figuras (su pose es referencia 3D)**

- **Prime 1 Studio**, 1/4 (unos 50 cm): David, Lucy y Rebecca ✅
  ([Toy People, Lucy](https://www.toy-people.com/en/?p=98572),
  [Toy People, Rebecca](https://www.toy-people.com/en/?p=100665),
  [MyFigureCollection](https://myfigurecollection.net/item/2423349)).
  **Lucy apoyada de espaldas en la barra del Afterlife**, base con las
  luces del bar; la deluxe trae el dron Wyvern y cabezas intercambiables
  ([Sideshow](https://www.sideshow.com/collectibles/cyberpunk-2077-lucy-prime-1-studio-914452)) ✅.
  **La mejor referencia de pose relajada, de «esperar a que se arme la
  partida».**
- **Good Smile**: «Hello! Good Smile» de David y Lucy (chibi, dirección de
  arte de Shigeto Koyama) y **BUZZmod. Rebecca** 1/12 ✅
  ([Good Smile](https://www.goodsmile.com/en/product/1140950),
  [Amazon](https://www.amazon.com/Good-Smile-Company-Figure-Cyberpunk/dp/B0G5YPC63P)).

**Cosplay bien hecho**

- **Yaya Han, Lucy**: **8 telas** (panal, espejo holográfico, elásticos
  de 4 vías, scuba hex); chaqueta del patrón McCall's M7733 modificado con
  **EVA de 2 mm forrada** para que se sostenga sola; peluca aerografiada
  (80 % alcohol, 20 % color) con tiza para el degradado; **90 horas** ✅
  ([blog](https://www.yayahan.com/post/cosplaying-lucy-from-cyberpunk-edgerunners)).
- Fotos con licencia libre (Openverse, en `referencias.json`): Rebecca en
  la Comic-Con de L.A. 2023 (CC BY-NC-ND, Howie Muzika), Lucy en Made In
  Asia 2023 y CWT63 (CC BY-SA, Wikimedia Commons), Anime Las Vegas 2025
  (CC BY-SA).

**No encontré**: café temático oficial en Japón (buscado en español e
inglés); no digo que no exista.

---

## Punto 24 · Obras parecidas y temas relacionados

- **Influencias que nombra el equipo**: *Akira*, *Ghost in the Shell* y
  *Blade Runner* ✅ ([AWN](https://www.awn.com/animationworld/cyberpunk-edgerunners-vibrant-ode-retro-anime)).
  Y a propósito **se evitó que Lucy recordara a Motoko Kusanagi** (§3.8).
- **La casa**: Imaishi dirigió *Gurren Lagann*, *Kill la Kill* y
  *Promare*; Yoshinari, *Little Witch Academia* y *BNA*; el guionista
  Yoshiki Usa, *SSSS.GRIDMAN* ✅ ([wiki de la serie](https://cyberpunk.fandom.com/wiki/Cyberpunk:_Edgerunners)).
  De ahí la línea gruesa y la acción exagerada.
- **Lo que recomienda el público** ([AniList](https://anilist.co/anime/120377)),
  de más a menos votos: *Akudama Drive*, *Ghost in the Shell*,
  *PSYCHO-PASS*, *Redline*, *Promare*, *Black Lagoon*, *Gurren Lagann*,
  *LAZARUS*, *Akira*, *Akame ga Kill!*, *Devilman Crybaby*, *Cowboy Bebop*,
  *Kill la Kill* ✅. Las más cercanas en tono: *Akudama Drive*,
  *PSYCHO-PASS* y *Black Lagoon*.
- **Láminas del servidor que se le parecen**: el encargo **114, *Cyberpunk
  2077* (el juego)**, es el mismo universo y aún no tiene canal. Si se
  hace, que use **personajes del juego** (V, Johnny Silverhand, Judy,
  Panam) y no la recreativa, para no repetir esta. No hay otro anime
  cyberpunk entre los encargos 01-127 ✅ (comprobado sobre los títulos de
  `encargos/`). *Cowboy Bebop* sí tiene lámina (el disco que le gustó al
  dueño): no repetir su sobriedad jazz; aquí manda el neón.

---

## Punto 25 · El mundo, la historia y sus símbolos

### Las reglas del mundo en cinco líneas

1. **Night City**, 2076: ciudad-estado de California donde mandan las
   corporaciones; la policía (NCPD, MaxTac) va detrás ✅
   ([wiki](https://cyberpunk.fandom.com/wiki/Cyberpunk:_Edgerunners), AniList).
2. **El chrome** (implantes) te mejora, pero cuanto más llevas, más cerca
   estás de la **cyberpsicosis** ✅ (ep. 1, el ciberpsicópata del
   arranque).
3. **Un edgerunner** es un mercenario que vive al filo: sin corporación
   que lo cubra, un error lo mata ✅.
4. **Arasaka y Militech** son el poder real ✅.
5. **Todo es barato y carísimo a la vez**: megaedificios como el H4 abajo,
   torres de cristal arriba; lluvia y neón siempre; hasta la lavadora
   funciona con saldo (ep. 1, 04:15) ✅.

### La historia por arcos

Duraciones de la [wiki](https://cyberpunk.fandom.com/wiki/Cyberpunk:_Edgerunners#Episodes) ✅.

**Arco 1 · De la calle a edgerunner (ep. 1-4)**
- ep. 1 «Let You Down» (24:14): David, hijo de Gloria, en H4; se pone la
  Sandevistan; muere su madre.
- ep. 2 «Like A Boy» (24:12): venganza en la Academia Arasaka; conoce a
  Lucy en el tren; la luna del BD (19:30).
- ep. 3 «Smooth Criminal» (24:20): entra en el equipo de Maine.
- ep. 4 «Lucky You» (24:12): Lucy lo entrena; la promesa de la luna (21:54).

**Arco 2 · El ascenso (ep. 5-7)**
- ep. 5 «All Eyez On Me» (23:30): David propone el plan; el objetivo es
  más peligroso de lo que parecía.
- ep. 6 «Girl on Fire» (25:48): la cyberpsicosis de Maine; su muerte
  (22:10-22:48).
- ep. 7 «Stronger» (24:14): David, ya líder y con más chrome; Faraday le
  ofrece el gran trabajo.

**Arco 3 · La caída (ep. 8-10)**
- ep. 8 «Stay» (24:16): Faraday entre Arasaka y Militech; Lucy y Rebecca
  le reprochan a David cuánto ha cambiado.
- ep. 9 «Humanity» (25:18): descubren el pasado de Lucy; el trabajo sale
  mal.
- ep. 10 «My Moon My Man» (26:54): David, al borde de la cyberpsicosis,
  va a por Lucy; Adam Smasher; Lucy llega sola a la luna.

### Emblemas y objetos icónicos

- **Logos de corpos y bandas**: tabla del Punto 19.
- **El emblema verde de David**: el logo de la XBD de Jimmy Kurosaki
  (§16).
- **La Sandevistan**, **el monowire** de Lucy, **Guts** (la escopeta de
  Rebecca), **la máscara de Kiwi**, **la luna**.
- **Para #a-que-juegas**: la **recreativa de *Roach Race*** (§13) sigue
  siendo el mejor objeto real.

### Jerga (la reconoce cualquier fan)

De la [wiki: Streetslang](https://cyberpunk.fandom.com/wiki/Streetslang) ✅,
cruzada con los subtítulos (§7.5).

| Palabra | Qué es |
|---|---|
| **Choom** / choomba | Amigo, colega |
| **Gonk** | Idiota; «gonk move», mala decisión |
| **Eddies** | Dinero (eurodólares) |
| **Preem** | Genial |
| **Nova** | Guay |
| **Delta** | Largarse |
| **Flatline** | Matar, morir |
| **Chrome** | Implantes |
| **Gig** | Encargo |
| **Edgerunner** / **merc** | Mercenario al filo |
| **ICE** | Defensas contra hackers |
| **Ripperdoc** | Cirujano clandestino |
| **Cyberpsicosis** | Perder la humanidad por el chrome |
| **Braindance (BD)** | Grabación sensorial; en latino, «neurodanza» |
| **Netrunner** | Hacker que entra en la red |
| **Sandevistan** | Implante que ralentiza el tiempo |

---

## 19 · Tres conceptos para la lámina de #a-que-juegas

Los tres respetan las reglas del dueño: **objeto real en sitio real**,
hecho en **Blender** cuando se puede; personajes **recortados de
fotogramas**; textos cortos en la voz de la serie; **lámina 2** para las
horas.

### Concepto A — «La recreativa de Kabuki» (el objeto del plan, mejorado)

**Por qué es fiel**: el parche **1.6 «Edgerunners»** del juego añadió
**recreativas jugables** (*Roach Race*) a Night City, con **tabla de
récords** ✅ (§13.1). No es una recreativa inventada: es la del mundo.

- **Objeto y sitio**: una **recreativa vieja y oxidada** bajo el toldo de
  un callejón de **Kabuki (Watson)**, de noche, **con lluvia** (la
  lluvia abre la serie, ep. 1, 00:13). Blender: «Rusty Japanese Arcade»
  (Hawtor Studio, CC BY) o «Old Arcade Cabinets» (Hrvoje Wächter, CC BY),
  HDRI **Shanghai Bund** o **Street Lamp** (Poly Haven), suelo **Asphalt025C**
  (ambientCG) con charcos. En la pantalla, un juego **de la ficción**:
  la portada de *Arasaka Tower 3D* o *Roach Race* estilizada.
- **Personaje**: **Rebecca** (la más querida, §9). Pose: **sentada
  encima de la recreativa saludando con guiño** (sale de W116) o, más
  segura para recortar, **agachada apuntando al espectador** (W20 =
  G10), subida al panel de mandos. Alternativa: **David** con el pulgar
  hacia sí mismo (W26) apoyado de lado.
- **Cómo habla**: **subtítulo del juego** abajo, sin caja: `REBECCA:`
  en coral `#FE6962`, texto en cian `#59E6F0`, Rajdhani SemiBold, con
  una banda negra al 60 % si hace falta. Frase: **«¿Te apuntas o qué?»**
  (tono de su «¿quieres dar un paseo?», ep. 8).
- **Dónde va cada texto**:
  - **Marquesina iluminada** de la máquina: **A QUÉ JUEGAS** en Anton con
    el degradado lima del rótulo de nombre (`#45FF7D`→`#EBFF68`).
  - **Pantalla CRT** (modo demostración, VT323, la tinta sigue la
    curva): «CUENTA LO QUE ESTÁS JUGANDO», «SUBE TUS CAPTURAS»,
    «¿QUIÉN SE APUNTA?» y abajo, parpadeando, «PULSA START».
  - **Pegatina** en el panel de mandos, junto al joystick: «Pon la hora
    de tu país».
  - Subtítulo de Rebecca abajo.
- **Que no quede plano**: gotas de lluvia **delante** de todo (capa
  desenfocada), **Guts** (modelo CC BY de charlloyd) apoyada en la
  máquina en primer término, el **reflejo verde y magenta** de la
  pantalla en el charco, un rótulo de neón vertical (YD Visual) cortado
  por el borde, vapor saliendo de una alcantarilla detrás.
- **Lámina 2**: la **misma máquina** mostrando la **TABLA DE RÉCORDS**
  (como la de *Roach Race*), pero con países y horas: `MÉXICO 19:00`,
  `PERÚ COLOMBIA ECUADOR 20:00`, `VENEZUELA 21:00`, `ARGENTINA CHILE
  22:00`, `ESPAÑA 03:00`, y en último lugar `NIGHT CITY 18:00` (guiño:
  en la tabla del juego el último es SILVERHAND). Encabezado: «¿ARMAS
  PARTIDA? DI LA HORA Y EL PAÍS». Pie en otra pegatina: «O usa el reloj
  de Discord: cada uno ve su hora». Rebecca, con otra pose (G33, puños
  arriba): `REBECCA: ¡Pon tu hora, que no adivino!`.

### Concepto B — «La carta del Afterlife» (el bar donde se arma el equipo)

**Por qué es fiel**: el **Afterlife** es el bar de los mercenarios donde
se reparten los encargos; sirve **bebidas con nombre de leyendas
muertas** y en el juego existe **«The David Martinez»** ✅ (§5.1). En el
ep. 7 Kiwi cita a David allí (11:27) y conoce a Faraday.

- **Objeto y sitio**: la **carta luminosa** de la barra (una caja de luz
  con frontal de metacrilato serigrafiado) en la pared del **Afterlife**,
  con la luz **verde menta** de W117 (`#7CF6CC`). Blender: caja con
  emisión detrás del metacrilato, botellas delante, HDRI **Warm Bar**
  cambiado a verde.
- **Personaje**: **Maine**, el jefe que acepta a los nuevos (W29, sonrisa
  de lado con dientes), acodado en la barra en primer plano. O el
  **grupo en el reservado** (W75) al fondo, pequeño, para que se lea
  «equipo».
- **Cómo habla**: una **ventana de holo-llamada** flotando (esquinas
  cortadas, filete cian, la cara de Kiwi dentro) con **«¿Puedes venir al
  Afterlife ahora?»** (ep. 7, 11:27), y el subtítulo de Maine abajo:
  `MAINE: Aquí todos reciben su parte.` (su «Everybody gets a fair
  shake», ep. 3, 18:02).
- **Dónde va cada texto** (cada «bebida» de la carta es una idea):
  - Cabecera de la carta: **A QUÉ JUEGAS**.
  - «**El Jugador**: cuenta a qué juegas».
  - «**La Captura**: sube tus capturas».
  - «**El Equipo**: ¿quién se apunta?».
  - «**La Hora**: di la de tu país».
  - Abajo, pequeño, el guiño: «The David Martinez: con gas» (a David no
    le gustaba el gas, ep. 2, 16:34).
- **Que no quede plano**: **vasos y botellas** en primer plano
  desenfocados, el brillo verde recortando el hombro de Maine, un poco
  de humo de cigarro (Kiwi) cruzando la carta, reflejos en la barra.
- **Lámina 2**: la **pizarra de encargos** del fixer junto a la barra
  (un tablero físico con notas sujetas con cinta), cada nota un país con
  su hora.

### Concepto C — «El panel del NCART» (donde Lucy y David se conocieron)

**Por qué es fiel**: Lucy y David se conocen **en el tren** (ep. 2,
07:46-09:34: «¿Qué te parecería si trabajamos juntos?» en el doblaje
latino ✅ clip). El tren elevado es un sitio que el jugador reconoce.

- **Objeto y sitio**: el **panel de próximas salidas** de una estación del
  **NCART** (tablero LED de puntos, Blender), andén de noche, tren
  amarillo entrando (G46). HDRI **Metro: Noord** (Poly Haven).
- **Personaje**: **Lucy**, de pie en el andén, mirando el panel con su
  **escaneo rojo** activado (sale de G41 / W45) o sentada como en W104.
- **Cómo habla**: su **HUD del ojo**: recuadros rojos finos que «escanean»
  cada línea del panel, y su subtítulo abajo: `LUCY: ¿Qué te parecería
  si jugamos juntos?` (eco directo de su frase del tren).
- **Dónde va cada texto**:
  - Cabecera del panel: **PRÓXIMAS PARTIDAS**.
  - Filas del panel (una idea por fila): «Cuenta lo que estás jugando»,
    «Sube tus capturas», «¿Quién se apunta?», «Pon la hora de tu país».
  - **Cartel publicitario** en la pared del andén (estilo anuncio de
    Night City): **A QUÉ JUEGAS**.
- **Que no quede plano**: el **tren pasando** desenfocado en primer
  plano (motion blur), la **línea amarilla del borde del andén** en
  diagonal, el panel iluminando la cara de Lucy en naranja LED, bruma
  al fondo.
- **Lámina 2**: el **mismo panel** con la tabla de horas por país
  (encaja de forma natural: es un horario).

### ¿Cuál primero?

**A**. Es el objeto que el plan ya proponía, ahora **justificado por el
juego** (recreativas del parche «Edgerunners»), lleva a **la más
querida** (Rebecca) y su lámina 2 (la **tabla de récords con las horas**)
resuelve «la hora de cada país» sin inventar un panel suelto.
**C** es la mejor segunda opción: el **horario del metro** es el objeto
más natural para las horas.

---

## 20 · Lo que no pude verificar ⚠️

**Sigue sin verificar**

- **La lámina actual** de #a-que-juegas que le gustó al dueño: no está
  en el repositorio; no sé qué personaje ni qué objeto usa.
- Las frases latinas de §10.4 salen de **subtítulos automáticos**.
- El **aspecto de la lista vertical de opciones de diálogo** del juego
  (Game UI Database pide un reto de Cloudflare; no lo salté).
- **No hay encuesta oficial de popularidad** de personajes.
- En qué episodio exacto sale la práctica de tiro de Rebecca y David en
  la tienda 2nd Amendment (W65-W66, «EP4» según el nombre del archivo).
- Fotogramas en **1080p**: en la 2.ª pasada sólo se pudo mirar en 360p.
- El **programa exacto de producción** de Trigger (RETAS, Clip Studio,
  Toon Boom): ninguna entrevista en abierto lo dice.
- **Vistas y fechas** de los fandubs en español (YouTube pide iniciar
  sesión), y **memes propios de la comunidad hispana** (sólo encontré los
  ingleses traducidos).
- El **amarillo exacto del logo** (`#F8EE08` o `#FCEE09`).
- La colaboración con **Fortnite** y la tienda **Atsuko** (una sola fuente
  cada una), y si hubo **café temático oficial** en Japón (no lo encontré).
- Kiwi en el ep. 7, 11:40: reconocida por el diseño, no por el audio.

**Resuelto en la segunda pasada** ✅

- Voces latinas de los secundarios y de Adam Smasher: dos fuentes (§10.5).
- Minuto de «I Really Want to Stay at Your House»: ep. 2, 19:30-21:30 (§11).
- Capítulos de los vídeos de análisis (§12).
- Autor de los carteles amarillos: los dos Kaneko existen (§3.8).
- Emblema verde de David: el logo de la XBD de Jimmy Kurosaki (§16).
- Clínica de Doc: Arroyo, Santo Domingo (§5).
---

## 21 · Bitácora de búsqueda

### 21.1 Estado de la red (24-sep-2026)

- **Primera mitad**: bloqueados por el proxy (curl y WebFetch, una
  prueba cada uno): cyberpunk.fandom.com, doblaje.fandom.com (y su copia
  *sandbox*), Wikipedia, ANMTV, okamisamatv.com.mx (no resolvía),
  eldoblaje.com, Facebook, web.archive.org, Sketchfab, Poly Haven,
  ambientCG, cyberpunk.net, Alpha Coders, WallpaperCave, Pinterest,
  Twitter, TV Tropes, Natalie, Famitsu, Game8, Namuwiki, Moegirl,
  Animate Times. Sólo respondía **GitHub**.
- **Segunda mitad** (aviso del coordinador: red abierta): respondieron
  la **API de Fandom** (wiki `cyberpunk` y Doblaje Wiki), **YouTube**
  por yt-dlp (con el cliente *web_embedded*; muchos vídeos pedían
  «confirmar que no eres un robot»), **Arctic Shift** (Reddit), la
  **API de Sketchfab**, **Poly Haven** y **ambientCG**. Siguieron
  bloqueados netflixlife.com y **Game UI Database** (reto de Cloudflare;
  no se intentó saltar).

### 21.2 Búsquedas web (41, con idioma)

| # | Búsqueda | Idioma | Qué saqué |
|---|---|---|---|
| 1 | Edgerunners doblaje latino reparto Lucy David Rebecca Maine | es | ANMTV: Grande Studios, Jessica Ángeles, Torres, Moreno, Solórzano |
| 2 | «Edgerunners» doblaje latinoamericano estudio director «David Martínez» | es | Amalia Bobadilla; retos de doblaje de David |
| 3 | «Melissa Gedeón» Rebecca | es/en | TV Tropes y Heroes Wiki: Rebecca = Meli G |
| 4 | «María José Moreno» Lucy | es | Ficha de Doblaje Wiki, TikTok |
| 5 | okamisamatv doblaje latino Kiwi Faraday Falco… | es | Robles, Anaya, Vázquez, Analiz Sánchez |
| 6 | Crunchyroll Anime Awards 2023 Edgerunners | en | Anime del Año (Deadline, AWN, Animation Magazine) |
| 7 | エッジランナーズ 人気投票 キャラ ランキング | ja | No hay encuesta oficial |
| 8 | Edgerunners Rebecca most popular character poll | en | Ranker 1.º Rebecca; EpicStream, CBR, Screen Rant |
| 9 | Edgerunners key visual Trigger Yoshinari | en | Artbook, litografía, key art de la temporada 2 |
| 10 | サイバーパンク エッジランナーズ 描き下ろし 吉成曜 | ja | 2.º aniversario, Natalie, Famitsu, Blu-ray BOX |
| 11 | Edgerunners 2 release date Kai Ikarashi | en | 20-oct-2026, nuevo equipo |
| 12 | «The Art of Cyberpunk: Edgerunners» artbook | en | 318 págs., 10 capítulos, reimpresión 2026 |
| 13 | 今石洋之 インタビュー エッジランナーズ | ja | Famitsu (Rebecca y Lucy), WebNewtype, AUTOMATON |
| 14 | Imaishi interview Rebecca design | en | Wikipedia Rebecca, AMA de Reddit |
| 15 | «Humberto Solórzano» Maine | es/en | TV Tropes |
| 16 | «Jocelyn Robles» Kiwi / «Raúl Anaya» Faraday | es | Fichas de Doblaje Wiki |
| 17 | エッジランナーズ キャスト KENN 悠木碧 | ja | Reparto japonés |
| 18 | Edgerunners English dub cast | en | Reparto inglés, Salami Studios ⚠️ |
| 19 | «I Really Want to Stay at Your House» charts | en | Viral 50 n.º 1, UK n.º 68 |
| 20 | Edgerunners official trailer / «This Fffire» | en | Tráileres, versión de Rich Costey |
| 21 | 2077 patch 1.6 Edgerunners items | en | Chaqueta, Guts, David Martinez (bebida), pegatinas |
| 22 | 2077 arcade Roach Race Trauma Drama Arasaka Tower 3D | en | Máquinas y sitios |
| 23 | «Roach Race» arcade 1.6 | en | Llegó con el parche Edgerunners |
| 24 | Edgerunners locations in 2077 | en | H4, pisos de Lucy y Kiwi, Afterlife |
| 25 | Edgerunners wallpapers 4K | en | Webs de fondos |
| 26 | sketchfab arcade cabinet CC BY | en | Primeras recreativas |
| 27 | sketchfab Edgerunners Guts / David | en | Modelos de fans |
| 28 | Poly Haven night HDRI / ambientCG | en | HDRI y asfalto CC0 |
| 29 | Edgerunners doblaje latino «choom» traducción | es | Sin datos del doblaje; *choom* y *gonk* explicados |
| 30 | Edgerunners Steam player count | en | Récord y 1 millón diario |
| 31 | TV Tropes Edgerunners characters | en | «Murder goblin», manga MADNESS |
| 32 | Edgerunners memes fandom | en | LEGO, NiCola, «no es una niña» |
| 33 | 赛博朋克 边缘行者 丽贝卡 人气 | zh | Zhihu, 18183, Moegirl |
| 34 | 사이버펑크 엣지러너 레베카 인기 | ko | Namuwiki |
| 35 | Edgerunners logo font | en | Logo propio, sin letra libre |
| 36 | Edgerunners color palette | en | Páginas flojas; medí yo los colores |
| 37 | Edgerunners español latino Falco Dorio Pilar Gloria | es | Gloria = Analiz Sánchez |
| 38 | Discord timestamp HammerTime | en | Hora local de cada uno ✅ |
| 39 | Edgerunners soundtrack tracklist | en | 14 temas, 27-oct-2023 |
| 40 | «I Really Want to Stay…» qué episodio | en | Elegida por Imaishi para el ep. 2 |
| 41 | Edgerunners TikTok trend | en | Edits de David y Lucy |

### 21.3 APIs y herramientas (sin cupo)

- **GitHub**: `Ajatt-Tools/kitsunekko-mirror` (subtítulos de Netflix
  ja+en de los 10 episodios, clon sparse), `google/fonts` (20 carpetas
  comprobadas con fontTools), búsqueda de repositorios «edgerunners» y
  12 repositorios de fans clonados (imágenes para las hojas G).
- **Wiki `cyberpunk` (API)**: 10 páginas para `investigar_serie.py`
  (128 imágenes); texto de Lucyna Kushinada, Rebecca, David Martinez,
  Maine, Kiwi, Falco, Pilar, Afterlife, Roach Race, Edgerunners Update,
  la banda sonora y «I Really Want to Stay at Your House».
- **Doblaje Wiki (API)**: «Cyberpunk: Edgerunners» y «Cyberpunk:
  Edgerunners II».
- **yt-dlp**: 20+ vídeos (títulos, duraciones, capítulos) y subtítulos
  de *Inside Look*, *Inside Look #2*, la entrevista de ANISON USA y 4
  clips del doblaje latino.
- **Arctic Shift**: r/Edgerunners y r/cyberpunkgame.
- **Sketchfab API**: 10 modelos comprobados y 6 búsquedas.
- **Poly Haven API** (HDRI de noche, asfaltos) y **ambientCG API**.
- **Pillow**: colores medidos (mediana por tono) en 20 imágenes.

### 21.4 Fuentes por tipo (más de 40)

- **Oficiales**: Netflix Tudum, cyberpunk.net (notas del parche 1.6),
  canal de YouTube de Netflix y de CD PROJEKT RED (*Inside Look* 1 y 2,
  tráileres, vídeo de Yoshinari), X de Trigger y de CD PROJEKT RED
  Japan, tienda Gear de CDPR, Xbox Wire.
- **Entrevistas y prensa**: Famitsu, WebNewtype, AUTOMATON, GAME Watch,
  Comic Natalie, 4Gamer, HMV, Denfaminicogamer, Tonari no Young Jump,
  Deadline, Animation Magazine, AWN, VGC, Engadget, Forbes, ComicBook,
  80.lv, GamesRadar, Seat42F, Bleeding Cool, Hypebeast.
- **En otros idiomas**: japonés (Famitsu, Natalie, WebNewtype, pixiv),
  chino (Zhihu, 18183, Moegirl), coreano (Namuwiki). Vistos sólo en
  resultados, sin abrir: note.com (ja), DC Inside (ko).
- **Wikis**: Cyberpunk Wiki (Fandom), Doblaje Wiki, Wikipedia, TV Tropes
  (personajes, YMMV, Funny), Heroes Wiki, pixiv百科事典.
- **Foros**: Reddit (r/Edgerunners, r/cyberpunkgame vía Arctic Shift),
  Steam Community.
- **Arte**: Pixiv, Know Your Meme, Steam Workshop, Alpha Coders,
  WallpaperFlare (sólo para encontrar el origen).
- **Vídeo**: YouTube (Gigguk, The Canipa Effect, Swamp Jawn, MankoMan,
  ANISON USA, clips latinos), TikTok.
- **Código y recursos**: GitHub (kitsunekko-mirror, google/fonts, 12
  repositorios de fans), Sketchfab, Poly Haven, ambientCG, Printables.
- **Doblaje latino**: Doblaje Wiki (API), ANMTV, Okami Sama TV, TV
  Tropes (fichas de actores), entrevista de ANISON USA, tráiler doblado,
  clips con audio latino.
- **The Cutting Room Floor**: no hay página útil de *Edgerunners* (es una
  serie, no un juego); para *2077* no la consulté ⚠️.

### 21.5 Lo que NO encontré

- Encuesta **oficial** de popularidad de personajes.
- Frases del doblaje latino **en una fuente escrita** (sólo en clips).
- La lámina ya hecha para este canal.
- Capturas medidas de la **interfaz de diálogo** del juego distintas de
  las de la guía de cuadros (Game UI Database bloqueada por Cloudflare).
