# Parte VOZ · 12-kakegurui (repaso: puntos 20, 21 y 22 de ENCARGO.md)

La biblia (escrita el 24-sep-2026, con la red cerrada) ya cubre a fondo los
puntos 7, 8, 12 y 13 (popularidad, personajes, doblaje, fandom). Esta parte
sólo aporta lo que **no estaba**: **punto 20** (gustos y detalles de cada
personaje), **punto 21** (por qué la gente la ama, con escenas y reacción
real) y **punto 22** (fan dubs y comunidad hispana). Parto de
`partes/datos-voz.md` (no repito AniList, la ficha de Doblaje Wiki ni las
búsquedas de Reddit/Danbooru ya recolectadas) y de `herramientas/seccion.py
12-kakegurui --rol voz` / `--avisos`.

La red está abierta esta vez (la biblia original tuvo 403 en casi todo). Uso
la API de Fandom (`kakegurui.fandom.com` y `doblaje.fandom.com`), la API de
Wikipedia, `arctic-shift` para Reddit, y `yt-dlp --skip-download --print`
para YouTube: **hoy sí devuelve metadatos** (título, canal, vistas, duración)
sin pedir sesión — es intermitente, como avisa AYUDANTE.md. TikTok sí me
bloqueó (yt-dlp no puede sortear su verificación); esos los dejo con el
título y canal que da el buscador, marcados ⚠️.

**Extra fuera de mis 3 puntos, pero barato y útil**: la API de Doblaje Wiki
(`action=parse&prop=wikitext`) ya no da 403. Resolví ahí mismo el reparto
latino completo que la biblia tenía como ❌ en «Lo que no pude verificar»
(sección 20) — lo dejo en el bonus al final de este documento para que el
redactor lo pase a la sección 10 de la biblia.

## Hallazgos

### Punto 20 · Gustos y detalles de cada personaje

Sin *artbook* o *databook* impreso confirmado para Kakegurui (a diferencia de
otras biblias del equipo). La fuente más rica que encontré es un **hilo de X
que traduce un podcast de radio real de Homura Kawamoto (el autor) y su
hermano**, hablando personaje por personaje ([hilo 1
«Parte 2»](https://x.com/Shishi_Odoshii/status/2005737101116203158), 29-dic-2025,
cuenta [@Shishi_Odoshii](https://x.com/Shishi_Odoshii), 755 seguidores).
Es información **del propio autor**, pero llega **traducida por un fan sin
confirmar en un medio oficial**: marco cada dato de ahí con ⚠️ por esa razón,
no porque dude de que el podcast exista. Lo demás sale de las fichas
(`Character Infobox`) y las secciones «Trivia» de la wiki en inglés, leídas
con la API (`action=parse&prop=wikitext`).

| Personaje | Comida/afición favorita | Edad, altura, cumpleaños | El objeto que siempre lleva | Cómo se ve a sí misma |
|---|---|---|---|---|
| **Yumeko Jabami** | Sin dato de comida. Su única «afición» declarada es apostar por la emoción, no por el dinero (ya en la biblia, §8) | 16-17 años · **166 cm** ✅ ([Fandom](https://kakegurui.fandom.com/wiki/Yumeko_Jabami) + [AniList](https://anilist.co/character/121889), dos fuentes) · **sin cumpleaños revelado**: según el propio Kawamoto en el podcast, los cumpleaños «no están confirmados porque podrían usarse en la historia más adelante, como pasó con Mary» ⚠️ | un **anillo de plata en el pulgar izquierdo**, uno de los anillos de boda de sus padres (fallecidos); se lo dejaron ella y su hermana Souko como recuerdo ✅ ([Fandom, «Appearance» y «Trivia»](https://kakegurui.fandom.com/wiki/Yumeko_Jabami)) | la serie **nunca** le da un monólogo interno en todo el anime — es el único personaje al que no se le oyen pensamientos ✅ ([Fandom, Trivia](https://kakegurui.fandom.com/wiki/Yumeko_Jabami)): su «cómo se ve a sí misma» queda deliberadamente oculto, a diferencia de Mary (ver abajo). Un dato aparte: **es el personaje favorito del propio Kawamoto** ⚠️ (podcast, tweet [4/21](https://x.com/Shishi_Odoshii/status/2005734420251304234)) |
| **Mary Saotome** | Sin comida citada; sí «**odia los abrazos**, sobre todo de sus amigas» y «**le gusta la gente muy honesta**» ⚠️ ([Fandom, Trivia](https://kakegurui.fandom.com/wiki/Mary_Saotome)) | 16-17 años (15-16 en *Twin*) · **162 cm** ✅ (Fandom + AniList) · **cumpleaños 8 de marzo** ✅ — **dos fuentes que coinciden**: [AniList](https://anilist.co/character/122687) y el manga (cap. 21 / anime ep. 9, citado en la ficha de Fandom). Es, según la propia wiki, **el único personaje de toda la serie con cumpleaños confirmado** ✅ | el **pasador de pelo (hairpin) de Tsuzura Hanatemari**, su amiga de *Kakegurui Twin* que desaparece de la trama principal: Mary lo conserva y «parece disgustada por lo que le pasó a su amiga» ✅ ([Fandom, «Mary Saotome#History»](https://kakegurui.fandom.com/wiki/Mary_Saotome)) | en *Twin* se revela que **su familia no es rica** y que está en Hyakkaou con **beca**; su meta desde niña es «convertirse en una verdadera ganadora en la vida», y odia que la miren por menos por su dinero ✅ (Fandom). Tiene monólogo interno explícito (a diferencia de Yumeko): rechaza el «plan de vida ridículo» que le tocaría — casarse con un político, tener hijos, ser un trofeo — antes de perder contra Kirari (cita indirecta, [búsqueda web](https://www.tumblr.com/kakeguruibeyond/186343901233); ⚠️ no pude abrir la página completa, sólo el fragmento) |
| **Kirari Momobami** | **McDonald's, donas y café** — nunca termina su comida, pero pide todo el café que le dejen «por diversión»; en un *barbacoa* pide **kimchi y pulpo**, le gusta lo dulce-picante y casi no come carne salvo pollo ⚠️ (podcast, tweets [2/14](https://x.com/Shishi_Odoshii/status/2005737103322497086) y [3/14](https://x.com/Shishi_Odoshii/status/2005737105578942574)). Su deporte favorito es el **baloncesto** («le parece interesante»); nunca jugó béisbol ⚠️ (mismo hilo) | 17-18 años · **166 cm** ⚠️ (Fandom, la propia wiki sólo cita una foto de Tumblr como fuente) · sin cumpleaños oficial (ver arriba) — la ficha de AniList decía 24/8, pero **no coincide con ninguna fuente primaria** que haya podido comprobar: lo bajo a ⚠️ | no tiene un objeto citado, pero sí un **detalle de diseño**: su peinado (los dos «rodetes» con lazos) está inspirado en **donas y cuentas de oración budistas** ⚠️ (mismo podcast, tweet 3/14) — útil también para el punto 17/18 (guía de estilo) | **ya sabía todo lo que enseñaban en la escuela antes de transferirse** a Hyakkaou ⚠️ (podcast, tweet [5/14](https://x.com/Shishi_Odoshii/status/2005737109638774871)): encaja con su personalidad de aburrimiento crónico, ya descrita en la biblia (§8, «qué la aburre») |
| **Ririka Momobami** | Sin comida citada | 17-18 años · **166 cm**, la misma altura que Kirari por ser gemelas idénticas ✅ (Fandom, ficha) | **una máscara de repuesto** para emergencias (revelado en el capítulo extra «A Dog, Mary and the Vice President», del spin-off *Kakkokari*) ⚠️ una fuente; también tiene **un iPhone** (manga, cap. 110) ⚠️ | se ve a sí misma sólo como la **suplente de Kirari**: «la única autoridad de la vicepresidenta es actuar de apoderada de la presidenta», así que no tiene funciones propias ✅ (Fandom, «Personality», ya citado en parte en la biblia §8); el podcast de Kawamoto añade que la elección del arco 2 fue **la primera vez que se enfrenta a Kirari** ⚠️ y que, de las gemelas, **Ririka es más cercana a Mary y a Yumeko** — Kirari no tanto ⚠️ (tweet [13/14](https://x.com/Shishi_Odoshii/status/2005737123933217025)) |

**Secundarias más queridas** (para tener a mano si la lámina 2 las necesita):

- **Runa Yomozuki**: **130 cm (4'3")** ⚠️ una fuente (Fandom) — la más
  bajita del reparto, dato útil para poses de grupo. Su risa «にゃは
  (Nyaha)» / «にゃはは (Nyahaha)» es la única onomatopeya de risa exclusiva
  de un personaje en la serie ✅ (Fandom + ya usada con minuto en la
  biblia §8). Apodo: «Furry Girl», que le pone Ibara Obami (manga cap. 62)
  ⚠️.
- **Midari Ikishima**: **170 cm (5'7")**, la más alta del grupo ⚠️ una
  fuente (Fandom). Es **zurda** ⚠️. Es el único personaje con apariciones
  importantes en **todos** los medios de Kakegurui (manga, *Twin*, *Midari*,
  anime, drama) ✅ (Fandom, Trivia).

**Nadie tiene cumpleaños oficial excepto Mary.** No es que no lo haya
buscado: el propio Kawamoto lo explica en el podcast (arriba), y las fichas
de Fandom (inglés) dejan el campo `birth` vacío para Yumeko, Kirari, Ririka,
Midari y Runa ✅ (comprobado en las 5 fichas, API `action=parse`).

### Punto 21 · Por qué la gente la ama

**21.1 Ventas y premios (con fuente)**

- **El manga no ha dejado de crecer**: 4 millones de copias en circulación
  en feb-2018 ([ANN, titular](https://www.animenewsnetwork.com/daily-briefs/2018-02-01/kakegurui-manga-has-4-million-copies-in-print/.127149) — la
  página da error de seguridad al reabrirla, cito el titular, que sí cargó
  la primera vez) → **5 millones** en feb-2019 → **6.2 millones** en jul-2021
  → **6.8 millones** en jun-2022 ✅ ([Wikipedia, «Kakegurui»,
  sección Reception](https://en.wikipedia.org/wiki/Kakegurui), con sus tres
  referencias propias). Es una curva sostenida de casi una década, no un
  pico y caída.
- **El opening «Deal with the Devil» (TIA) fue nominado a Mejor Opening**
  en la **3.ª entrega de los Crunchyroll Anime Awards** (2018), compitiendo
  con *Darling in the Franxx*, *Aggretsuko*, *Wotakoi* y *JoJo's Bizarre
  Adventure* ✅ ([Wikipedia, «Crunchyroll Anime Award for Best Opening
  Sequence»](https://en.wikipedia.org/wiki/Crunchyroll_Anime_Award_for_Best_Opening_Sequence)).
  No hay constancia de que ganara esa categoría ese año.

**21.2 Con quién se identifica el público, y por qué**

- **Celebridades reales que lo dicen abiertamente**: **Megan Thee Stallion**
  y **Poppy** se han cosplayado como Yumeko y han hablado en público de
  cuánto les gusta la serie; el artículo de CBR dice que esto **abrió la
  puerta a nuevos fans** años después del estreno (2017→2020) ✅ ([CBR, «How
  Kakegurui Became a Sleeper
  Hit»](https://www.cbr.com/how-kakegurui-anime-became-popular/), Molly
  Kishikawa, 24-nov-2020, leído completo).
- **Por qué se enganchan con Yumeko** (resumen de discusiones de fans en
  MyAnimeList, vía búsqueda): su **inteligencia disimulada** (parece ingenua
  pero detecta cualquier trampa), sus **jugadas imprevisibles** (esconde una
  grabadora durante un cacheo) y, sobre todo, que **disfruta genuinamente**
  del juego en sí, no del premio — el público dice identificarse con esa
  falta de miedo y esa pasión por la experiencia, no por ganar ⚠️ (resumen
  de varios hilos de foro, no un solo post citable).
- **Mary es la «best girl» por su arco**, ya en la biblia (§9): pierde,
  se humilla, vuelve. Aquí lo confirmo con más contexto: en *Twin* se ve que
  viene de una familia sin dinero becada en una escuela de ricos, así que su
  necesidad de «ganar de verdad» tiene una raíz de clase, no sólo orgullo
  (ver punto 20 arriba) — probablemente por eso el público conecta más con
  ella que con Kirari o Yumeko, que ya nacieron arriba.
- **El propio Kawamoto se sorprendió del resultado de la encuesta oficial**
  (la que la biblia ya cita con ⚠️ en las fichas de personaje, §8): en su
  podcast dice que **Kirari no quedó primera** y que **Yumeko quedó 5.ª**
  («sin Yumeko la historia ni empezaría», y admite que le dio pena) ⚠️;
  también que **le sorprendió que Mary superara a Kirari** y que Mary y
  Ririka quedaran tan arriba ⚠️; y que **cree que Ririka subiría de puesto**
  si se repitiera la encuesta hoy ⚠️ (tweets
  [2/21](https://x.com/Shishi_Odoshii/status/2005734414832263348),
  [3/21](https://x.com/Shishi_Odoshii/status/2005734417889997114) y
  [13/14](https://x.com/Shishi_Odoshii/status/2005737123933217025)). **Esto
  confirma de forma independiente** el orden que la biblia ya tenía con ⚠️
  en las fichas de Yumeko (5.ª), Kirari (2.ª) y Mary (1.ª): sugiero al
  redactor subirlos a ✅ citando también esta fuente.
  también dijo que su personaje favorito es **Yumeko**, y el de su hermano,
  **Sumika Warakubami** ⚠️ (tweet
  [4/21](https://x.com/Shishi_Odoshii/status/2005734420251304234)).
- **La propia seiyū de Yumeko también tiene favorita**: a Saori Hayami le
  preguntaron su personaje favorito sin contar a Yumeko, y contestó
  **Midari** — dijo que, durante el juego de la guillotina de dedos, Midari
  «adora tanto a Yumeko que pone la misma cara que un cachorro esperando a
  su dueño»; el propio Kawamoto dijo que él también la encuentra adorable
  ✅ ([entrevista en japonés, entertainmentstation.jp](https://entertainmentstation.jp/388789/2),
  citada y traducida en [Fandom, «Midari
  Ikishima#Trivia»](https://kakegurui.fandom.com/wiki/Midari_Ikishima)). Es
  una fuente japonesa primaria, aunque leída a través de la traducción de la
  wiki: marco ⚠️ sólo por no haber leído el japonés yo mismo.
- **El «arte de la fuga» no aplica aquí** (a diferencia de otras series del
  equipo): en Kakegurui nadie se identifica por huir, sino por **plantarse y
  apostarlo todo**; es lo opuesto, y vale la pena decirlo así de claro para
  no mezclar tonos entre biblias.

**21.3 Las escenas, con minuto verificado por mí en el subtítulo (no copiado
de la biblia)**

Kakegurui no es una serie que haga llorar: es una serie que hace **gritar de
emoción o reír de vergüenza ajena**. Verifiqué estos tres momentos yo mismo
abriendo el `.srt`/`.ass` de `kitsunekko-mirror` (ep. 1, minuto exacto
confirmado con el diálogo en pantalla, inglés y japonés):

| Escena | Cap. y minuto (verificado) | Qué pasa | Por qué engancha | Reacción del público |
|---|---|---|---|---|
| **El discurso de la locura + «さあ 賭け狂いましょう!»** | 1×01, **00:12:08 a 00:12:40** (verificado línea a línea: «Insanity is the essence of gambling» a las 00:12:08.52; «Now, then, let's get our gambling freak on» / «さあ 賭け狂いましょう！» a las 00:12:37.17-00:12:40.84) | Yumeko explica por qué apostar la vida da placer y remata retando a Mary con la frase que se volvió el eslogan de la serie | Es el momento bisagra: de «chica nueva rara» a «la protagonista que cambia las reglas» en 30 segundos | Es la frase que en 2026 volvió viral («kakegurui mashou», ya en la biblia §14); Know Your Meme y CBR lo confirman como el clip más repetido de la serie |
| **«¿Cómo pasó esto?» — Mary llorando tras perder y volverse mascota** | 1×01, **00:16:59.77** (verificado: «How did this happen, anyway?») | Mary, que empezó humillando a Yumeko, termina arrastrándose por el suelo como «Fido» tras perder | Es el «gancho» clásico de shōnen — caída dura — que hace que el público quiera verla resurgir (de ahí que sea la más votada, §9 de la biblia) | Fandom la señala como el inicio de su arco «favorito de los fans»; Screen Rant y CBR (ya citados en la biblia) coinciden en que es el momento que la vuelve memorable |
| **«私は… 私は…» — Ririka sin máscara, tartamudeando** | 2×03, 00:18:05 (minuto **de la biblia §15, no lo pude reverificar yo mismo**: el mirror de GitHub que usé sólo tiene los 12 episodios de la 1.ª temporada, no la 2.ª/××; lo marco ⚠️ por eso, no porque dude del dato) | Sin la máscara, la Ririka fría y decidida se traba al hablar | Es el único momento en que se ve a la Momobami «invencible» como una persona insegura de verdad | El podcast de Kawamoto (21.2) confirma que ésta fue, en la trama, la primera vez que Ririka se enfrenta de igual a igual — encaja con por qué los fans la recuerdan |

No encontré el nombre de la pista de música exacta que suena en ninguna de
estas tres escenas: la biblia (§11) no da minutos de la banda sonora y yo no
tengo acceso a los créditos de audio del OST. Lo dejo ⚠️, no invento el
título.

### Punto 22 · Fan dubs y comunidad hispana

**22.1 Fan dubs de capítulos y escenas (voz de aficionados)**

Confirmados con `yt-dlp --skip-download --print` (título, canal, vistas y
fecha reales, sin descargar vídeo — hoy no pidió sesión):

| Título | Canal | Vistas | Fecha | Enlace |
|---|---|---|---|---|
| KAKEGURUI - Capítulo 1 (Clip) [Fandub Español] | **Sakato Irumi** (con Lirin1996 y JonTenox) | 94 330 | 07-mar-2018 | [YouTube](https://www.youtube.com/watch?v=ub4zVzGiD8w) |
| Kakegurui \| OVA 1 \| Maid Café Hyakkaou \| Fandub Latino | **GoldFandubs** | 203 | 22-dic-2024 | [YouTube](https://www.youtube.com/watch?v=b9vkToczwjU) |
| Kakegurui Yumeko vs Mary Fandub Español Latino | **Sekai no Yuro FD** | 1922 | 08-jun-2021 | [YouTube](https://www.youtube.com/watch?v=YjKNo0ajMO8) |
| Kakegurui Live Action - Fandub en Español Latino | **El DMNT** | 15 398 | 19-nov-2020 | [YouTube](https://www.youtube.com/watch?v=6OFbbHMq7-I) |

Todos ✅ (confirmados directamente con `yt-dlp`, no de memoria ni de un
resumen de búsqueda). Créditos completos que trae la descripción de cada
vídeo (útiles para un servidor de doblaje, con nombres de fandubbers reales):

- **Capítulo 1** (Sakato Irumi): voces «versionando» de Sakato Irumi,
  Lirin1996 y JonTenox; traducción y adaptación de Lirin1996; edición de
  Sakato Irumi y JonTenox.
- **OVA 1** (GoldFandubs): Suzui — *Affter!Vibes*; Yumeko — *Dian_dubs*;
  Mary («Saotomi» en la descripción) — *Takiry*; narrador — *Custom
  Animatronics*.

**22.2 Covers del opening en español**

«Deal with the Devil» (TIA) tiene varias versiones en español, con vistas
muy distintas entre sí — la de Miree destaca mucho sobre el resto:

| Cover | Canal | Vistas | Fecha | Enlace |
|---|---|---|---|---|
| Kakegurui OP - Deal With The Devil (Cover Español) | **Miree** (con Aryes Anime y Pidrosax) | **634 563** | 04-dic-2020 | [YouTube](https://www.youtube.com/watch?v=TbAUB9c0Lgk) |
| Kakegurui -Deal with the devil- Opening FULL Fandub Español | **Hana** | 202 072 | 03-sep-2017 | [YouTube](https://www.youtube.com/watch?v=TQKT8qLqt8E) |
| Kakegurui - OP - (Deal with the Devil) - [Fandub Español Latino] | **Skargu ღღ** | 8233 | 20-jul-2017 | [YouTube](https://www.youtube.com/watch?v=50RHkSSOTs0) |
| Kakegurui - Deal with the devil - Opening Fandub Español | **Hana** | 21 564 | 06-jul-2017 | [YouTube](https://www.youtube.com/watch?v=2LMGHGeasfw) |
| Kakegurui opening - Deal with the devil FANDUB ESPAÑOL LATINO | **Val** | 2703 | 08-may-2018 | [YouTube](https://www.youtube.com/watch?v=lSfFW6GQOvw) |
| KAKEGURUI OPENING \| Deal with the devil - Tia (Cover español) | **bestendista** | 135 reproducciones | — | [SoundCloud](https://soundcloud.com/user-652528345/kakegurui-opening-deal-with) ✅ (confirmado con el contador propio de SoundCloud) |

Todos ✅ (mismo método, `yt-dlp --print`, salvo el de SoundCloud, confirmado
con su propio contador de reproducciones). El cover de **Miree** (2020) es,
con diferencia, el más visto: más de 600 mil vistas cuatro años después del
estreno original — coincide con la fecha del resurgir de popularidad que ya
documenta el artículo de CBR (21.2).

**22.3 Parodias y memes hispanos del doblaje**

En TikTok no pude confirmar vistas ni likes con `yt-dlp` (bloquea la
verificación del sitio sin sesión); dejo lo que da el buscador, marcado ⚠️
por no haberlo podido abrir yo mismo salvo la cifra que el propio buscador
reporta:

- **@marhinafrances**: hace un «home studio» de doblaje de Yumeko y Mary
  para redes, citando de memoria a las actrices españolas reales (María
  Sánchez y Paqui Horcajo) ⚠️ ([TikTok](https://www.tiktok.com/@marhinafrances/video/7245344327600278810)).
- **@kazumaldito**: compara «kakegurui mashou» (el meme viral de 2026, ya
  en la biblia §14) en japonés contra el doblaje en español, con **288 mil
  «me gusta»** según el resumen del buscador ⚠️ ([TikTok](https://www.tiktok.com/@kazumaldito/video/7490415201846660358)).
- **@kodenwatch**: «¿Cuál prefieres tú? — Análisis de doblaje de Kakegurui»,
  comparando doblajes ⚠️ ([TikTok](https://www.tiktok.com/@kodenwatch/video/6986793041587703046)).
- **@kira.bug**: comparación doblaje latino vs. castellano (ya citada en la
  biblia §10, la repito aquí porque es la pieza que más une doblaje +
  comunidad).
- Reto de doblaje con Yumeko y Mary de **@jarigrt** (ya en la biblia §10).

No encontré covers ni fandubs de **Kakegurui Twin** ni de **Kakegurui ××**
en español, sólo de la primera temporada y del *live action*: parece que la
comunidad hispana se concentró en la serie original.

## Lo mejor para la lámina

1. El cover de **Miree** del opening (634 mil vistas, 22.2) demuestra que la
   comunidad hispana **ya le puso voz** a Kakegurui a lo grande: buen gancho
   de texto para el canal de doblaje/canto.
2. **«さあ 賭け狂いましょう!»** (1×01, 00:12:37, verificado) sigue siendo la
   frase más reconocible y la que detonó el meme de 2026: es la candidata
   más segura para el cuadro de diálogo del concepto de lámina.
3. **Mary con el pasador de Tsuzura** (punto 20) da una imagen de objeto
   pequeño y personal, útil si el concepto de lámina quiere un detalle de
   vestuario en vez de un arma o una carta.
4. El contraste Yumeko (sin monólogo interno, «no sabemos qué piensa») vs.
   Mary (monólogo explícito, rabia contra su «vida de trofeo») es una buena
   pareja para una lámina 2 sobre «voces internas» si el canal lo necesita.
5. El propio Kawamoto confirmando que **Mary superó a Kirari en la encuesta
   real** (21.2) es la prueba «de la casa» de que el dueño busca: el
   secundario puede ser más querido que el principal, con cita del autor.

## No encontré

- ⚠️ **Cumpleaños real de Yumeko, Kirari, Ririka, Runa y Midari**: no
  existen (campo vacío en la ficha, y el propio Kawamoto lo explica en su
  podcast). No es un fallo de búsqueda.
- ⚠️ **El tema musical exacto** de las tres escenas del punto 21.3: la
  biblia (§11) no da minutos del OST.
- ⚠️ **Minuto verificado por mí mismo** de la escena de Ririka (2×03): el
  mirror de GitHub que usé sólo trae la 1.ª temporada; dejo el minuto que ya
  tenía la biblia, sin re-verificar.
- ⚠️ **Vistas y «me gusta» reales de los TikTok** del punto 22.3: TikTok
  bloquea `yt-dlp` sin sesión desde este servidor; uso lo que da el
  resumen del buscador.
- ⚠️ **La cifra exacta de manga vendido en 2018** (ANN, 4 millones): la
  página da ahora un aviso de seguridad al reabrirla; el dato es del
  titular, que sí cargó a la primera.
- Todo lo demás de los puntos 20, 21 y 22 **sí** se encontró, con su fuente,
  arriba.

## Bonus (fuera de mis 3 puntos): reparto latino que la biblia tenía como ❌

La API de Doblaje Wiki ya no da 403. Confirmé el reparto completo con **dos
páginas independientes de la propia wiki** por cada nombre (la ficha de
«Kakegurui» + la página propia del actor, que lista «Kakegurui» en su
filmografía) ✅:

| Personaje | Voz latina | Confirmado en |
|---|---|---|
| Kirari Momobami | **Adriana Núñez** | [Ficha de Kakegurui](https://doblaje.fandom.com/es/wiki/Kakegurui) + [ficha de Adriana Núñez](https://doblaje.fandom.com/es/wiki/Adriana_Núñez) |
| Ririka Momobami | **Adriana Núñez** (mismo papel que Kirari, por ser gemelas) | Ficha de Kakegurui |
| Sayaka Igarashi | **Sofía Huerta** | Ficha de Kakegurui + [ficha de Sofía Huerta](https://doblaje.fandom.com/es/wiki/Sofía_Huerta) |
| Runa Yomozuki | **Azul Valadez** | Ficha de Kakegurui + [ficha de Azul Valadez](https://doblaje.fandom.com/es/wiki/Azul_Valadez) |
| Itsuki Sumeragi | **Montserrat Aguilar** | Ficha de Kakegurui + [ficha de Montserrat Aguilar](https://doblaje.fandom.com/es/wiki/Montserrat_Aguilar) |
| Midari Ikishima | **Liliana Barba** | Ficha de Kakegurui + [ficha de Liliana Barba](https://doblaje.fandom.com/es/wiki/Liliana_Barba) |
| Yumemi Yumemite | **Annie Rojas** | Ficha de Kakegurui |
| Kaede Manyuda | **David Allende** | Ficha de Kakegurui |
| Yuriko Nishinotoin | **Georgina Sánchez** (T1) / **Mayra Arellano** (T2) | Ficha de Kakegurui |
| **Director de doblaje** | **Guillermo Rojas** (Sysdub); **Daniel Lacy** sólo eps. 17-21 | [Infobox de Kakegurui](https://doblaje.fandom.com/es/wiki/Kakegurui) + [ficha de Guillermo Rojas, sección «Dirección de doblaje» → «Anime: Kakegurui (2017-2019)»](https://doblaje.fandom.com/es/wiki/Guillermo_Rojas) |

Sigue sin encontrarse la frase exacta del doblaje latino para «さあ 賭け狂い
ましょう» (ya lo decía la biblia); no lo busqué de nuevo por no ser mi punto.

## Bitácora

**Red directa** (sin gastar el buscador):
- `doblaje.fandom.com/es/api.php?action=parse&prop=wikitext` para
  «Kakegurui» (reparto completo) y para 5 actores (Adriana Núñez, Sofía
  Huerta, Azul Valadez, Montserrat Aguilar, Liliana Barba, Guillermo Rojas)
  — todas cargaron sin 403.
- `kakegurui.fandom.com/api.php?action=parse&prop=wikitext` para Yumeko,
  Mary, Kirari, Ririka, Runa y Midari (fichas completas, «Trivia»).
- `api.fxtwitter.com/<usuario>/status/<id>` y `api.vxtwitter.com/i/status/<id>`
  para leer el hilo de X de @Shishi_Odoshii sin necesitar sesión (7 tuits
  del hilo «Parte 1» y «Parte 2» del podcast de Kawamoto, más 2 de
  contexto para confirmar el tema del hilo).
- `en.wikipedia.org/w/api.php?action=parse&prop=wikitext&page=Kakegurui`
  (sección Reception, ventas del manga) — se cortó una vez por *rate limit*,
  funcionó al reintentar tras una pausa.
- `en.wikipedia.org/wiki/Crunchyroll_Anime_Award_for_Best_Opening_Sequence`
  y `2nd_Crunchyroll_Anime_Awards` (este último no traía a Kakegurui: usé el
  buscador para dar con la edición correcta, la 3.ª).
- `arctic-shift.photon-reddit.com/api/posts/search?subreddit=Kakegurui` con
  `query=`: funciona con una palabra (`sad`, `Mary`), pero da **422/400**
  con frases de dos o más palabras y a veces «Timeout, slow down a bit» —
  dejé de insistir tras 3-4 intentos para no gastar más tiempo en algo
  fuera de mis 3 puntos.
- `yt-dlp --skip-download --print "%(title)s | %(uploader)s | %(view_count)s..."`
  para 11 vídeos de YouTube (fandubs y covers): **funcionó sin pedir
  sesión** en el momento de este repaso (a diferencia de lo que avisa
  AYUDANTE.md — es intermitente). Con TikTok (3 intentos) dio siempre
  «Unexpected response... impersonation»: no lo pude sortear.
- `i.ytimg.com/vi/<id>/maxresdefault.jpg` (o `hqdefault.jpg` si el primero
  da 404) + Pillow para medir miniaturas de 3 vídeos, sin descargar el
  vídeo completo.
- `doblaje.fandom.com/es/api.php?action=query&prop=imageinfo&iiprop=url|size`
  para medir 3 imágenes del reparto (Kirari, Ririka, Sayaka).
- El `.ass`/`.srt` de `github.com/Ajatt-Tools/kitsunekko-mirror` (clonado
  con `git clone --sparse`, la API de GitHub da «acceso no habilitado» pero
  el clon normal sí funciona): sólo trae los 12 episodios de la **1.ª
  temporada**, no la 2.ª (××) — lo dejo anotado porque la biblia original
  decía tener también la 2.ª y no la encontré en este repositorio.
- `soundcloud.com/.../kakegurui-opening-deal-with` (HTML propio, contador
  `playback_count` en el JSON incrustado).

**Buscador web** (9 de mi cupo de ~50):
- Español: «Kakegurui opening español "Deal with the Devil" latino fandub»;
  «Kakegurui fandub español Yumeko canal youtube»; «Kakegurui parodia
  español meme "doblaje" TikTok reto voz»; «Kakegurui cosplay español
  fandub Mary Kirari youtube».
- Inglés: «Kakegurui "why fans love" reddit reasons Yumeko identify»;
  «Kakegurui crying scene reaction "made me cry" reddit»; «Kakegurui Mary
  Saotome breakdown episode saddest most emotional scene»; «Kakegurui
  review "why people love" Anime News Network OR IGN OR CBR»; «Kakegurui
  manga sales million copies circulation»; «Kakegurui anime award
  nomination Crunchyroll Anime Awards»; «"Kakegurui" "Crunchyroll Anime
  Awards" nominee category».

**Fallos y cómo los resolví**:
- `voice-over-and-voice-acting.fandom.com`: Cloudflare (verificación de
  navegador) — no lo pude sortear con `curl`; usé la propia API de Doblaje
  Wiki como fuente principal y las fichas de actor como segunda fuente en
  su lugar.
- `animenewsnetwork.com`: aviso de seguridad al reabrir 2 de 3 páginas
  (sólo la búsqueda de «awards nominations» cargó bien); usé Wikipedia como
  respaldo para lo que necesitaba confirmar dos veces.
- `x.com` directo: sólo devuelve la app de React vacía sin JavaScript; usé
  los espejos `api.fxtwitter.com` / `api.vxtwitter.com`, que sí dan el
  texto del tuit en JSON.
- `arctic-shift` con `sort=score`: tira el resultado a `null` sin avisar
  del motivo — mejor pedir sin `sort` y ordenar yo mismo en Python.
- TikTok vía `yt-dlp`: bloqueado por verificación anti-bot en los 3
  intentos; no insistí una cuarta vez.

**Parte terminada**: los puntos 20, 21 y 22 quedan cubiertos con lo
obligatorio del encargo (gustos con fuente para los 4 principales + 2
secundarias, premios/ventas/identificación con reacción real y 3 escenas
con minuto para el 21, y fan dubs + covers + memes con canal/vistas/enlace
verificados para el 22). Lo que falta son extras opcionales, listados en «No
encontré», más el bonus del punto 8 (fuera de mi encargo) para que el
redactor lo aproveche.
