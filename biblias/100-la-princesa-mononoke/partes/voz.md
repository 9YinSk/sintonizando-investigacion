# Voz y personajes — La princesa Mononoke (encargo 100)

Investigador de voz y personajes. Puntos 7, 8, 12, 13, 20, 21 y 22 de `ENCARGO.md`.
Parte de `partes/datos-voz.md` (AniList, Doblaje Wiki, Danbooru, Dailymotion, Reddit):
esas consultas no se repiten aquí. Personajes de partida marcados por el encargo:
**San, Ashitaka, Moro**.

**Aviso importante sobre `datos-voz.md` (corregido aquí)**: la tabla «Reparto
latino» de ese archivo y la ficha de personajes (Zashiki Warashi, Umibozu,
Noppera-bo…) son de **otra obra**: *Mononoke* (モノノ怪, 2007, la serie de
anime de Kenji Nakamura sobre el Boticario) — el recolector automático buscó
mal en Doblaje Wiki («Mononoke» en vez de «La princesa Mononoke»). El reparto
correcto de la PELÍCULA de Miyazaki está abajo (punto 8), sacado de la ficha
real: https://doblaje.fandom.com/es/wiki/La_princesa_Mononoke (bajada
completa con `action=parse&prop=wikitext`). El resto de `datos-voz.md`
(AniList, Danbooru, Dailymotion, Reddit, las fichas «Personality» de San/Moro
en inglés) sí es de esta película y se usa tal cual.

## 7. Personajes principales y secundarios: popularidad

### Tres fuentes de favoritos/popularidad, más fan art (mismo grupo de personajes)

| Personaje | AniList favoritos (datos-voz.md) | MyAnimeList favoritos | ranking.net Japón (orden 1-18) | Danbooru fan art (datos-voz.md, tag mixto Ghibli) |
|---|---|---|---|---|
| Ashitaka | 1485 | **2197** | **#1** | 272 |
| San | **2471** | **3546** | #2 | 786 |
| Moro | 320 | 227 | #3 | — |
| Yakul (elk) | 250 | 253 | #4 | — |
| Cachorros de Moro | — | — | #5 | — |
| Toki | 62 | 17 | #6 | — |
| Kodama | 225 | 311 | #7 | 192 |
| Eboshi | 318 | 339 | #8 | — |
| Kaya | 9 | 3 | #9 | — |
| Nago | — | 2 | #10 | — |
| Okkoto | 20 | 16 | #11 | — |
| Kohroku | 3 | 1 | #12 | — |
| Shishigami (Espíritu del Bosque) | 98 | 116 | #13 | — |
| Gonza | 3 | 1 | #14 | — |
| Jigo/Jiko-bō | 20 | 17 | #15 | — |
| Hii-sama | 3 | 1 | #16 | — |
| Daidarabocchi | — | — | #17 | — |

Fuentes: AniList (ya en `datos-voz.md`, https://anilist.co/anime/164) ·
MyAnimeList, extraído con `curl` de
https://myanimelist.net/anime/164/Mononoke_Hime/characters (campo
`js-anime-character-favorites` de cada personaje, HTML propio, sin necesitar
la API caída de Jikan) · ranking.net Japón,
https://ranking.net/rankings/best-mononokehime-characters (orden de las 18
cabeceras `<h3>`, cada una «Nº位<Personaje>»; el sitio no expone el número de
votos en el HTML estático, sólo el orden final, así que el orden en sí es
✅ pero el conteo de votos por debajo queda ⚠️) · Danbooru (ya en
`datos-voz.md`, tag `mononoke_hime`, que mezcla toda la obra con otros
títulos de Ghibli en el mismo tag padre).

- **San es la favorita en las bases de datos occidentales** (AniList y MAL,
  las dos coinciden en el mismo orden: San > Ashitaka > el resto) · ✅ (dos
  fuentes independientes, mismo orden).
- **Pero en la encuesta japonesa (ranking.net) gana Ashitaka**, no San · ✅
  (fuente japonesa, orden claro) — y esto **coincide** con una encuesta de
  medios: ねとらぼ (Nlab/ITmedia) hizo en mayo-junio de 2022 un ranking de
  «personajes chico/joven más populares de Ghibli» y Ashitaka salió **#1**
  · https://nlab.itmedia.co.jp/research/articles/765102/ («1位は「アシタカ
  （もののけ姫）」【2022年最新投票結果】») · ⚠️ (una fuente, sólo el titular
  confirmado por búsqueda, no se abrió el artículo completo — pero coincide
  en dirección con ranking.net, así que el patrón «Ashitaka gana en Japón»
  se sostiene con dos fuentes japonesas distintas).
- **Los secundarios que sí compiten con los protagonistas**: Moro, Yakul,
  Kodama y Eboshi están todos muy cerca entre sí en las tres fuentes
  (rango 200-340 favoritos/puestos 3-8) — ninguno domina, pero los cuatro
  claramente le importan al fandom más que el resto del reparto secundario
  · ✅ (AniList + MAL + ranking.net, mismo grupo en las tres).
- **Kodama es el secundario más «memeable»**: pese a favoritos moderados
  (225-311), tiene 192 dibujos de fans sólo por su propio tag y aparece
  en el trivia de «Ugly Cute» (ver punto 12) — su cariño es más viral que
  numérico · ✅.
- El Espíritu del Bosque (Shishigami) es querido pero no arrasador: #13 en
  Japón, favoritos medios en Occidente — su diseño intriga más de lo que
  «enamora» al fandom, a diferencia de Howl en *El castillo ambulante*
  (referencia cruzada con `biblias/99-el-castillo-ambulante/partes/voz.md`)
  · ✅.
- No existe una encuesta de popularidad hecha por el propio Studio Ghibli
  (igual que en *El castillo ambulante*): se buscó explícitamente y no
  publican rankings oficiales de personajes, sólo aparecen en encuestas de
  medios/fans como las de arriba.

## 8. Doblaje latino: reparto verificado y frases textuales

Fuente principal, la ficha REAL de la película en Doblaje Wiki (bajada
completa con la API):
https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=La%20princesa%20Mononoke

### Hay TRES doblajes latinos (nunca dos)

| | **Buena Vista / Miramax** (2001, VHS) | **Zima Entertainment** (2010, DVD) | **Wild Bunch / Netflix** (2020, streaming) |
|---|---|---|---|
| Estudio | Musitrón S.A. de C.V. | Estudio Tokio | Sysdub |
| Ciudad | Monterrey, Nuevo León (única peli de Ghibli doblada ahí) | Ciudad de México | Ciudad de México |
| Dirección | Juan Carlos García Amaro | Juan Alfonso Carralero | Alan Prieto |
| Traducción/adaptación | — | — | Doralí Sanginés |
| Gerente creativo | Raúl Aldana | — | — |
| Mezcla | — | — | Aaron Cedeño |
| Productor | — | — | Joaquín Alpízar |
| Grabado | 2000 | 2010 | enero de 2020 |
| Dónde se ve | VHS México/Argentina 2001 | DVD «Rincón Ghibli» 15-abr-2010; TV: Código Animé (Chile, 29-nov-2017), Canal 22 (México, 30-abr-2014), Señal Colombia (16-dic-2015), RCN (5-mar-2022) | Netflix Latinoamérica desde 1-mar-2020 |
| Es la versión que dobla... | ...la edición al INGLÉS de Miramax (diálogos distintos/añadidos) | ...directo del japonés | ...directo del japonés, «la única íntegra y más fiel», único que usa el término correcto «Tatarigami» |

Los tres doblajes están espaciados por exactamente 10 años entre sí · ✅
(fecha en la propia ficha de Doblaje Wiki).

### Reparto por personaje (los 3 doblajes)

| Personaje | Seiyū (JP) | Buena Vista 2001 | Zima 2010 | Wild Bunch 2020 |
|---|---|---|---|---|
| Ashitaka | Yōji Matsuda | **sin identificar** (Doblaje Wiki: «¿?») | **Carlos Enrique Bonilla** | **Luis Leonardo Suárez** |
| San | Yuriko Ishida | **Angélica Rodríguez Ovalle** | **Jahel Morga** | **Harumi Nishizawa** |
| Dama Eboshi | Yūko Tanaka | **Nancy López Montemayor** | **Alejandra de la Rosa** | **Adriana Casas** |
| Jigo (Jiko-bō) | Kaoru Kobayashi | **Francisco López Montemayor** | sin identificar | **Héctor Lee** |
| Moro | Akihiro Miwa | **Tere Salazar de Quintanilla** | **Salvador Reyes** | **Maru Guzmán** |
| Gonza | Tsunehiko Kamijō | Isidro Villarreal Pérez | Isidro Villareal Pérez (+Erick Salinas, 1 loop) | Víctor Hugo Aguilar |
| Toki | Sumi Shimamoto | Lucero Garza | Diana Pérez | Pamela Cruz |
| Kohroku | Masahiko Nishimura | sin identificar | Ricardo Rocha (+Erick Salinas, 1 loop) | Daniel Lacy |
| Okkoto | Hisaya Morishige | Mario Agrediano Brambila | Arturo Acosta | Jorge Santos |
| Hii-sama / Vieja sabia | Mitsuko Mori | Debi Derryberry(en)→Tere Salazar de Quintanilla | Love Santini | Olga Hnidey |
| Kaya | Yuriko Ishida | Angélica Rodríguez Ovalle (misma que San) | Jahel Morga (misma que San) | Amellalli Guevara |
| Narración | — | Mario Agrediano Brambila | Marcos Patiño | (no aparece como rol separado en la ficha) |

**Verificación en dos fuentes** para el núcleo del reparto (San, Ashitaka,
Eboshi, Jigo, Moro de Wild Bunch, y San/Ashitaka/Eboshi/Moro de Zima):
cruzado con `dubdb.fandom.com` (wiki DISTINTA a Doblaje Wiki), páginas
«La princesa Mononoke (Latin American Spanish, Sysdub)» y «...(Latin American
Spanish, Estudio Tokio)» — coincide nombre por nombre en las dos versiones
· ✅ aunque con matiz honesto: dubdb cita a su vez a Doblaje Wiki como
referencia, así que no es una fuente 100% externa (mismo límite que se
documentó en *El castillo ambulante*). Para Buena Vista/Miramax **no se
encontró una segunda fuente** fuera de Doblaje Wiki (ni el propio Doblaje
Wiki identifica al actor de Ashitaka en esa versión) · ⚠️.

### Datos de interés del doblaje (de la propia ficha)

- Moro la interpreta en japonés Akihiro Miwa, actor especializado en *drag*,
  buscando un tono de voz andrógino; en español eso **no se logra** en
  Miramax ni en Wild Bunch (la hace una actriz), sólo en Zima la hace un
  actor (Salvador Reyes) — es la versión que más se acerca al matiz de
  género ambiguo original · ✅.
- Jahel Morga dobla a San Y a Kaya en Zima porque comparten seiyū japonesa
  (Yuriko Ishida); el mismo patrón se repite en Buena Vista con Angélica
  Rodríguez Ovalle, aunque en el doblaje inglés de base las hacen actrices
  distintas (Claire Danes y Tara Strong) — decisión propia del casting en
  español, no una copia del inglés · ✅.
- Paco Mauri participa en los dos doblajes hechos en Ciudad de México (Zima
  y Wild Bunch) con personajes distintos cada vez · ✅.
- «Mononoke» no es un nombre: es una palabra que aquí se traduce como
  «espíritu vengador»; en los tres doblajes se deja sin traducir · ✅.
- Errores documentados: en Wild Bunch, en la primera escena Ashitaka llama
  por error «Lady Ji» a Lady Hii (mala pronunciación) · en Zima, varios
  *loops* quedan mudos (2 de Gonza, 1 de Eboshi, 1 de Jigo, 2 de voces
  adicionales) y hay una escena donde Toki y otra mujer intercambian sus
  voces, corregido 5 segundos después · ✅ (nota explícita de la ficha).
- El estudio donde se grabó Zima no era una casa de doblaje propiamente,
  sino un estudio de grabación/edición musical de la Ciudad de México
  (llamado «Tokio», como la calle donde está) · ✅.

### Frases textuales (transcritas con Whisper de las muestras OFICIALES de
Doblaje Wiki — `herramientas/voz.py`, revisadas a oído; audios en
`/tmp/claude-0/trabajo/100-la-princesa-mononoke-voz/audio/`)

**San (Wild Bunch, Harumi Nishizawa)** · fuente:
https://static.wikia.nocookie.net/doblaje/images/4/41/Mononokebtisan.ogg
- «Déjalo. Él es mi presa.» [0:00]
- «Te encuentras mal herido. Vas a morir.» [0:02]
- «Te cortaré la garganta y no podrás seguir diciendo tonterías.» [0:08]
- «¡Silencio! Yo no recibo órdenes de humanos.» [0:11-0:12]
- Voz: registro muy agudo (325 Hz), muy expresiva (16.2 semitonos), rápida
  (3.34 palabras/s) — hostil y cortante, nunca titubea · medido con
  `voz.py` ✅.

**San (Buena Vista, Angélica Rodríguez Ovalle)** · fuente:
https://static.wikia.nocookie.net/doblaje/images/8/8c/MononokeDisneySan.ogg
- «¡No temo a la muerte! ¡Haré lo que sea para sacar a los humanos del
  bosque!» [0:09-0:11]
- «Lady Evoshi es una mujer malvada y nadie evitará que yo la mate.»
  [0:17-0:19] (Whisper transcribe «Evoshi»: revisar de oído, es «Eboshi»)
- Voz: casi igual de aguda que Wild Bunch (323 Hz) pero con MENOS rango
  emocional (12.9 semitonos frente a 16.2) y aún más rápida (3.52
  palabras/s) — dos actrices distintas llegan a un registro parecido, pero
  la interpretación de 2020 suena más quebrada/emotiva · medido con
  `voz.py` ✅.

**Ashitaka (Wild Bunch, Luis Leonardo Suárez)** · fuente:
https://static.wikia.nocookie.net/doblaje/images/7/74/Mononokebtiashitaka.ogg
- «Por favor, controla tu ira.» [0:03]
- «¡Detente! ¡No destruyas nuestra aldea! ¡Basta! ¡Detente tu ira!»
  [0:10-0:14]
- Voz: registro agudo (231 Hz), muy expresiva (20.1 semitonos) — de las MÁS
  expresivas de todo el reparto medido, rápida (3.36 palabras/s): nada de
  «héroe de voz plana», suplica y ordena con urgencia real · medido con
  `voz.py` ✅.

**Moro (Wild Bunch, Maru Guzmán)** · fuente:
https://static.wikia.nocookie.net/doblaje/images/b/b4/Mononokebtimoro.ogg
- «Ella es mi hija, San. Hay humanos en todos lados.» [0:00]
- «El dios siervo otorga vida y quita vida.» [0:06]
- «San, ya he vivido una larga vida. El dios siervo con gusto tomará mi
  vida antes que curarme herida.» [0:24-0:26]
- Voz: registro medio (165 Hz), la MENOS expresiva de todo el reparto
  medido (sólo 8.6 semitonos de rango) — nunca «grita» ni en sus líneas más
  violentas, suena grave y resignada: una diosa vieja que ya aceptó su
  propia muerte · medido con `voz.py` ✅.

**Dama Eboshi (Wild Bunch, Adriana Casas)** · fuente:
https://static.wikia.nocookie.net/doblaje/images/c/cc/Mononokebtieboshi.ogg
- «¡Vamos! ¡Ya falta muy poco! ¡Manténganse alerta!» [0:00]
- «Es una diosa, no murió. No morirá tan fácilmente.» [0:07]
- «Muchos están convencidos de que eres un espía de los samuráis o de los
  monstruos.» [0:16] (Whisper dice «amurais»: es «samuráis», revisado de
  oído)
- Voz: registro medio (193 Hz), muy expresiva (14.9 semitonos), rápida
  (3.18 palabras/s) — autoritaria con energía, no con frialdad · medido con
  `voz.py` ✅.

**Jigo / Jiko-bō (Wild Bunch, Héctor Lee)** · fuente:
https://static.wikia.nocookie.net/doblaje/images/1/1a/Mononokebtijikobo.ogg
- «Qué horror, esto sabe a agua caliente.» [0:00]
- «Es una pepita enorme de oro. Si son monedas lo que quieres, te las daré
  a cambio de esto.» [0:06-0:12]
- «Yo creo que esto vale un saco de arroz... más bien, tres sacos.»
  [0:16-0:20]
- Voz: registro medio (219 Hz), expresiva (16.0 semitonos), pero el ritmo
  MÁS PAUSADO de todo el reparto medido («velocidad normal», 2.28
  palabras/s, frente a «rápida» en los demás) — habla despacio y
  calculador, nunca apresurado: encaja con un personaje que siempre
  controla la conversación · medido con `voz.py` ✅.

**Para el canal: hay TRES doblajes con reparto distinto** (ver tabla
arriba) — cualquier frase citada debe decir cuál (Buena Vista/Miramax 2001,
Zima 2010 o Wild Bunch/Netflix 2020), igual que se advirtió en *El castillo
ambulante*.

## 12. Lo que el fandom ama, y qué NO hacer

Fuentes: Tropedia (mirror en Fandom de TV Tropes, API `action=parse` —
funciona aunque tvtropes.org de frente esté bloqueado), páginas
`Princess Mononoke/YMMV`, `/Funny`, `/Heartwarming`, `/Tear Jerker`,
`/Trivia`; y búsquedas directas en Reddit vía `arctic-shift.photon-reddit.com`
sobre r/ghibli (orden por puntuación).

### Momentos/chistes internos que todo fan reconoce

- **«¡Odio a los humanos!»** (la línea de San): es la frase más citada como
  reacción/meme ante cualquier acción de alguien sin corazón — «Memetic
  Mutation» en la propia página YMMV · Tropedia ✅. En Reddit hay un post
  dedicado sólo a esa línea, con 79 votos, en r/ghibli
  (https://reddit.com/r/ghibli/comments/1wa6rlo/i_hate_humans/) · ✅ (dos
  fuentes independientes, TV Tropes y Reddit, señalan la misma frase).
- **San da de comer a Ashitaka boca a boca** (carne seca masticada, porque
  él está demasiado débil): al no entender el significado humano del gesto
  —fue criada por lobos—, Ashitaka llora de la ternura · confirmado en TV
  Tropes (vía búsqueda), Nausicaa.net (sinopsis oficial del fandom) y un
  post de Tumblr dedicado a esa escena
  (https://www.tumblr.com/dodonzone/110166536192) · ✅ (tres fuentes
  describen la misma escena) — es de los momentos más citados como
  «ternura inesperada» de toda la película.
- **Los Kodama** (espíritus del bosque): entrada propia en «Ugly Cute» de
  YMMV por sus caras haniwa y el traqueteo de cabeza — «raros pero
  entrañables» · Tropedia ✅. Un post de «Kodamas 3D Fan Art» tiene 69
  votos en r/ghibli · ✅ (coincide con el puesto #7 de popularidad del
  punto 7 pese a tener pocos favoritos numéricos: el cariño es más viral
  que estadístico).
- **El cosplay del fandom es serio, no de broma**: un cosplay hecho a mano
  de San tiene 1797 votos en r/ghibli, el post con más puntuación de toda
  la búsqueda («My handmade Princess Mononoke Cosplay!»,
  https://reddit.com/r/ghibli/comments/1w7kcjx/) · ✅ — dato para el
  investigador de imagen/vestuario, pero también mide qué tan en serio se
  toma el fandom a este personaje.
- **«FOREST SPIRIT! WE GIVE YOU BACK YOUR HEAD! TAKE IT!»** y «¡MI
  BRAAAZO!»: citados en la propia YMMV como «Narm» (momentos tan intensos
  que rozan lo involuntariamente gracioso) — el brazo de un samurái
  arrancado de un flechazo se recuerda con humor, no sólo con horror ·
  Tropedia ✅.
- **Jigo murmurando «un pequeño problema y todos entran en pánico»** en
  medio del clímax (el bosque muriéndose) es el chiste interno favorito de
  la página «Funny» · Tropedia ✅.
- **Miyazaki mandó una katana con la nota «No cuts» (sin cortes)** al
  estudio que adaptaba la película al inglés, para que no la editaran —
  anécdota real citada en la página de Trivia · Tropedia ✅ — dato de
  producción que el fandom repite como prueba de que la película se
  respetó íntegra en Occidente.

### Qué NO hacer (para no romper la ilusión del fandom)

- **No dibujar a San «linda y dócil»**: su primera aparición en pantalla es
  con sangre ajena en la cara, chupando una herida de bala de un lobo; su
  frase de bienvenida a Ashitaka es «vete» · Ghibli Wiki + blog de reseña
  (ver punto 21) ✅. Mostrarla siempre «bonita» sin su lado salvaje
  traiciona al personaje.
- **No hacer de Eboshi una villana simple**: cuida leprosos y compra la
  libertad de mujeres explotadas, pero también sacrifica a su propia gente
  como carnada y mata dioses sin dudarlo — el propio Miyazaki la llama un
  personaje «gris», y estuvo a punto de matarla en el guion original antes
  de decidir que «matarla es demasiado, pero tiene que ser castigada» ·
  Ghibli Wiki (Controversies + Trivia, cita directa de Miyazaki) ✅.
- **No usar un globo de diálogo blanco genérico**: el mundo es Japón rural
  del período Muromachi (1336-1573) con dioses-animales y una fundición de
  hierro — texturas de madera vieja, piedra, sangre, musgo y metal forjado
  encajan; un globo de cómic occidental no · confirmado por el tono visto
  en los fotogramas reales (punto 13) y por ser instrucción explícita de
  `ENCARGO.md`.
- **Cuidado con qué doblaje se cita**: hay TRES doblajes latinos con
  reparto distinto (ver punto 8) — decir siempre cuál.
- **No suavizar la violencia real de la película**: brazos y cabezas
  vuelan de un flechazo, San aparece cubierta de sangre, Eboshi dispara a
  matar — la propia YMMV lo señala como «Narm»/intenso a propósito, no
  como censura pendiente; el dueño del servidor ya avisó que rechaza
  láminas «que no se empapan del tema» (`ENCARGO.md`).
- **«Mononoke» no se traduce ni se usa como nombre propio suelto**: es
  «espíritu vengador» en este contexto (ver punto 8) — un cuadro de diálogo
  que diga «yo soy Mononoke» como si fuera su nombre sería un error de
  guion que cualquier fan notaría.

## 13. Descripción profunda de cada personaje

Fuentes: Ghibli Wiki (fandom), wikitext completo bajado con la API
`action=parse&prop=wikitext` para San, Ashitaka, Moro, Eboshi y Jigo (no la
página renderizada, el texto fuente, en
`/tmp/claude-0/trabajo/100-la-princesa-mononoke-voz/*_full.txt`). Caras
vistas en fotogramas HD reales de la película (no un tráiler: son capturas
del propio metraje, con segundo exacto en el nombre de archivo, ya sacadas
por el investigador de vídeo de este mismo encargo con `fotogramas.py` —
carpeta compartida `/tmp/claude-0/trabajo/100-la-princesa-mononoke-video/hd/`,
miradas aquí directamente con Read).

### San (Princesa Mononoke)

- **Quién es**: hija de la diosa loba Moro, aunque nació humana — sus
  padres la arrojaron a los pies de Moro huyendo, y Moro la crio como
  propia en vez de comérsela · Ghibli Wiki (San) ✅ (coincide con AniList,
  ya en `datos-voz.md`).
- **Su lucha interna**: rechaza su propia humanidad, se considera loba;
  tiene intentos repetidos de matar a Eboshi para acabar con Irontown y
  devolver el bosque a los animales — sólo el cariño de Ashitaka la hace
  reconciliarse poco a poco con su lado humano · Ghibli Wiki ✅.
- **Carácter**: testaruda, fiera, de mal genio, sin miedo, agresiva, muy
  protectora del bosque y de los animales con los que vive · Ghibli Wiki
  Appearance/Personality ✅.
- **Su escena que la define**: le da de comer a Ashitaka carne seca que
  ella misma masticó, boca a boca, cuando él está demasiado débil para
  masticarla — criada por lobos, no conoce el significado humano de ese
  gesto; Ashitaka llora de la ternura (ver punto 12) · TV Tropes +
  Nausicaa.net + Tumblr ✅.
- **Momentos clave / arco**: ataca Irontown sola y sobrevive a un disparo
  en la cara; después de la batalla por la cabeza del Espíritu del Bosque
  le dice a Ashitaka que le importa mucho, pero que no puede perdonar a
  los humanos y vuelve al bosque — Ashitaka promete visitarla siempre que
  pueda · Ghibli Wiki (Role in the film) ✅.
- **Con quién se relaciona**: Moro (madre adoptiva), la manada de Moro
  (hermanos adoptivos), Ashitaka (amigo, amor implícito) · Ghibli Wiki
  Relationships ✅.
- **Su cara en cada emoción, con fotograma y minuto real** (película
  completa, no tráiler):
  - Cautela/evaluando: fotograma `san_carga_ashitaka_1570.jpg`, **26:10**
    — con su capucha-máscara de lobo puesta, mira de reojo a Ashitaka
    mientras él la carga por el bosque, boca entreabierta, cejas alzadas:
    lo está evaluando, no confía todavía del todo · visto directamente
    (Read) ✅.
  - Alarma protectora: fotograma `san_lobo_defensa_4225.jpg`, **1:10:25**
    — pintura de guerra roja en la cara, boca abierta, mirada de
    sobresalto, de pie junto a uno de sus hermanos lobo que gruñe con los
    colmillos totalmente expuestos · visto directamente ✅.
- **Lenguaje corporal**: se mueve casi siempre agachada o a cuatro patas
  como un lobo, nunca con porte «elegante»; corre y salta como un animal,
  no como una princesa de cuento · Ghibli Wiki Appearance ⚠️ (descriptivo,
  sin minuto puntual).
- **Su miedo**: perder del todo el bosque y a su familia loba — no le teme
  a morir ella misma («¡no temo a la muerte!», ver punto 8), le teme a
  quedarse sin nada que proteger; por eso ataca Irontown aunque sepa que
  puede morir en el intento · Ghibli Wiki (Role in the film) + frase
  textual del doblaje (punto 8) ✅.
- **Cómo habla (doblaje)**: la San más aguda de las dos versiones oídas
  (325 Hz en Wild Bunch, 323 Hz en Buena Vista, casi idénticas pese a ser
  actrices distintas), pero Wild Bunch bastante MÁS expresiva en rango
  (16.2 frente a 12.9 semitonos) — la interpretación de 2020 suena más
  quebrada emocionalmente · medido con `voz.py` ✅ (detalle completo en el
  punto 8).

### Ashitaka

- **Quién es**: (ex)príncipe de la aldea Emishi; se maldice al matar con
  su arco a Nago, un dios jabalí corrompido en demonio, para salvar su
  pueblo · Ghibli Wiki ✅ (coincide con la sinopsis de Wikipedia en
  español).
- **Su maldición**: la marca se le extiende del brazo a todo el cuerpo
  hasta matarlo; en momentos de odio le da fuerza sobrehumana a cambio de
  expandirse más rápido — literalmente el precio de dejarse llevar por la
  ira · Ghibli Wiki + Wikipedia ES ✅.
- **Carácter**: firme y decidido, no deja que los contratiempos lo
  detengan; muy curioso (quiere entender quién es San después de verla
  succionar veneno de un lobo herido); bajo su carácter duro es muy
  amable, no quiere que ningún bando derrame sangre · Ghibli Wiki
  Personality ✅.
- **Su forma de resolver conflictos, en la práctica**: se interpone en la
  pelea entre San y Eboshi, primero intenta razonar, y cuando ambas lo
  atacan las neutraliza SIN matarlas — su regla es evitar la violencia
  letal siempre que pueda · Ghibli Wiki Personality ✅ (ejemplo concreto en
  pantalla).
- **Su habilidad con el arco**: puede decapitar a un hombre y arrancarle
  los brazos a otro de un solo flechazo cada uno — citado en TV Tropes
  como «Narm» (tan intenso que roza lo surrealista) · Tropedia ✅. Su edad,
  17 años, viene de una fuente de producción real: *Colección de
  Storyboards de La princesa Mononoke #11* (Tokuma Shoten, 2002, ISBN
  9784198614751), citada en Ghibli Wiki · ✅ (fuente de artbook/producción,
  no una wiki de fans).
- **Con quién se relaciona**: San (amiga, amor implícito), Kaya (su
  hermana/prometida antes del destierro, según el diseño original de
  Miyazaki) · Ghibli Wiki ✅.
- **Su miedo**: convertirse él mismo en un monstruo antes de encontrar una
  cura — la maldición avanza cada vez que se deja llevar por la ira, así
  que su verdadero enemigo es su propio odio, no San ni Eboshi · Ghibli
  Wiki (curse/Appearance) ✅.
- **Su cara en la emoción que lo define**: fotograma
  `ashitaka_arco_0260.jpg`, **4:20** — de pie sobre un tronco caído, arco
  totalmente tensado apuntando fuera de cuadro, ceño fruncido, concentración
  absoluta: el instante justo antes de matar al jabalí-demonio Nago para
  salvar su aldea · visto directamente ✅.
- **Cómo habla (doblaje, Wild Bunch, Luis Leonardo Suárez)**: registro
  agudo (231 Hz) y muy expresivo (20.1 semitonos) — de los MÁS expresivos
  de todo el reparto medido; habla rápido (3.36 palabras/s) cuando ordena
  detener la violencia, nada de «héroe de voz plana» · medido con `voz.py`
  ✅.

### Moro

- **Quién es**: diosa loba de 300 años, madre adoptiva de San, líder de su
  manada; entiende y habla el idioma humano · Ghibli Wiki ✅.
- **Carácter**: inteligente, fuerte, profundo odio a los humanos (sueña
  con «triturar la cabeza» de Eboshi) pero, sobre todo, muy maternal y
  protectora — recogió a San cuando sus padres humanos la abandonaron en
  vez de comérsela · Ghibli Wiki Personality ✅.
- **Apariencia**: pelaje blanco largo, ojos color oliva con la esclerótica
  roja (posiblemente por estar inyectados en sangre), y **dos colas**, un
  rasgo único suyo que ningún otro lobo de la manada tiene — un detalle de
  diseño deliberado para distinguirla · Ghibli Wiki Appearance ✅.
- **Su muerte**: herida por un disparo de Eboshi, acepta morir con calma;
  cuando el Espíritu del Bosque le quita la vida, su cabeza cortada sigue
  viva un instante y muerde el brazo derecho de Eboshi antes de apagarse
  del todo — venganza cumplida más allá de la propia muerte · Ghibli Wiki
  (Background/History) ✅.
- **Dato poco citado**: según una nota de prensa japonesa que la propia
  wiki cita como referencia, Okkoto (el dios jabalí) fue su antiguo amante
  · Ghibli Wiki, cita a news.biglobe.ne.jp ⚠️ (una fuente japonesa de
  segunda mano, no verificada de forma independiente).
- **Su miedo**: ninguno para sí misma (acepta su propia muerte con calma
  absoluta, ver arriba); su miedo es por San — qué será de ella si Moro ya
  no está para protegerla del odio a los humanos o de los propios humanos
  · Ghibli Wiki (Background/History) ✅.
- **Su cara**: fotograma `moro_colmillos_4860.jpg`, **1:21:00** — primer
  plano nocturno, colmillos totalmente expuestos, ojos entrecerrados con
  la mirada fija, orejas hacia atrás: advertencia y furia pura, sin nada
  de la ternura maternal que muestra con San · visto directamente ✅.
- **Cómo habla (doblaje, Wild Bunch, Maru Guzmán)**: la voz MENOS
  expresiva de todo el reparto medido (165 Hz, sólo 8.6 semitonos de
  rango) — nunca «grita» aunque hable de matar; suena grave y resignada
  incluso en sus líneas más violentas, coherente con una diosa vieja que
  ya aceptó su propia muerte · medido con `voz.py` ✅ — contraste directo
  con San (16.2 semitonos) y Ashitaka (20.1): Moro es la voz más
  «contenida» del reparto principal, el mismo patrón que tuvo Suliman en
  *El castillo ambulante*.

### Dama Eboshi

- **Quién es**: fundadora y señora de Irontown (Tatara Ba); antagonista
  «gris», no villana simple · Ghibli Wiki ✅.
- **Su lado bueno**: compra la libertad de mujeres obligadas a
  prostituirse y las pone a dirigir la fragua; acoge y cuida a los
  leprosos (los limpia, los alimenta, les da trabajo fabricando los
  rifles) — los habitantes de Irontown la adoran por eso · Ghibli Wiki
  Personality ✅.
- **Su lado cruel**: ve a los espíritus como «criaturas tontas», no le
  importa usar a sus propios subordinados como carnada para los jabalíes
  a sabiendas de que morirán, y esconde bombas bajo tierra para una
  matanza masiva · Ghibli Wiki Controversies ✅.
- **Miyazaki sobre ella**: en el folleto oficial de la película se dice
  que su ataque final por los samuráis es «un karma» para ella y para
  Irontown, en línea con la frase de Ashitaka de que ella «provoca nuevos
  odios y rencores» · Ghibli Wiki (cita el folleto oficial) ✅. Miyazaki
  planeaba originalmente matarla, pero decidió que «matarla es demasiado,
  aunque tiene que ser castigada» · Ghibli Wiki Trivia ✅.
- **Su pasado**: fue *shirabyōshi* (artista/bailarina), luego rehén de
  piratas y esposa forzada de su líder; conspiró con Gonza para matarlo y
  escapar, y con armas chinas (Ishibiya) que consiguió después conquistó
  el Bosque de Cedros donde fundó Irontown · Ghibli Wiki (Past) ✅.
- **Su plan real**: su «Kunikuzushi» (destructora de naciones) no es sólo
  matar dioses — es romper el monopolio samurái sobre el hierro haciendo
  que mujeres y leprosos fabriquen armas, cambiando el reparto de poder
  del país · Ghibli Wiki Controversies ✅.
- **Su miedo**: que Irontown se derrumbe sin ella — por eso nunca se
  detiene ni admite dudas en público, incluso cuando sus propias
  decisiones (usar civiles como carnada) la acercan a esa misma caída ·
  Ghibli Wiki Controversies (análisis de Ichizawa citado en la wiki) ✅.
- **Cómo habla (doblaje, Wild Bunch, Adriana Casas)**: registro medio
  (193 Hz), muy expresiva (14.9 semitonos), ritmo rápido (3.18
  palabras/s) — autoritaria con energía, nunca fría o monótona · medido
  con `voz.py` ✅.
- No se localizó un fotograma propio de su cara en el material del
  fotogramas.py ya reunido por el investigador de vídeo (la carpeta `hd`
  compartida no tiene ninguno con ella de cerca) — queda como pendiente
  si el equipo de vídeo suma uno más adelante.

### Jigo (Jiko-bō)

- **Quién es**: monje itinerante que parece aliado de Ashitaka, pero es el
  antagonista oculto: quiere la cabeza del Espíritu del Bosque para
  dársela al Emperador a cambio de una recompensa (se dice que da
  juventud eterna) · Ghibli Wiki ✅.
- Es el líder del Karakasa-Ren («Alianza del Paraguas»), un grupo bajo el
  Shishō-Ren, sociedad secreta al servicio del Emperador y la corte real
  · Ghibli Wiki ✅.
- **Su doble cara**: finge ser un monje sabio y pesimista que ayuda a
  Ashitaka con información sobre el Espíritu del Bosque, mientras en
  secreto ya tiene tropas de tiradores y cazadores trabajando para él ·
  Ghibli Wiki ✅.
- **Comic relief pese a ser el villano**: cuando el bosque agoniza y todos
  huyen en pánico, Jigo sólo murmura «un pequeño problema y todos entran
  en pánico» · Tropedia (Funny) ✅.
- **Indicios de que era un noble encubierto**: tenía menaje de cocina de
  lujo, le ofreció miso a Ashitaka sin dudarlo (carísimo en la época),
  sabía leer y conocía la cultura Emishi y el ciervo rojo de memoria —
  detalles que sólo alguien con acceso a «literatura antigua» reservada a
  pocos podía saber · Ghibli Wiki Trivia (cita un análisis de fans en
  japonés en X/Twitter) ⚠️ (una fuente, análisis de aficionados, no
  oficial).
- **Su miedo**: quedar atrapado en la destrucción que él mismo provoca —
  cuando el bosque enloquece por la cabeza robada, intenta huir con ella
  en vez de enfrentar las consecuencias, y sólo la entrega cuando no le
  queda otra salida · Ghibli Wiki (plot) ✅.
- **Cómo habla (doblaje, Wild Bunch, Héctor Lee)**: registro medio (219
  Hz) y expresivo (16.0 semitonos), pero el ritmo MÁS PAUSADO de todo el
  reparto medido (2.28 palabras/s, «velocidad normal» frente a «rápida» en
  los demás) — habla despacio y calculador, nunca apresurado, como quien
  siempre controla la conversación · medido con `voz.py` ✅.

### Kodama (secundario más querido tras Moro/Eboshi, ver punto 7)

- **Qué son**: espíritus de los árboles viejos, hijos del bosque —
  cabezas blancas con ojos y boca de tres puntos negros/grises que
  traquetean; su presencia es la señal de que un bosque está sano · Ghibli
  Wiki (Kodama) ✅.
- **Su arco silencioso, sin diálogo**: aparecen observando desde los
  árboles cuando Ashitaka ayuda a Kohroku, y otra vez cuando San lo lleva
  al Espíritu del Bosque; cuando Eboshi corta la cabeza del Espíritu del
  Bosque, los Kodama empiezan a morir junto con el bosque (ver «Tear
  Jerker» del punto 21); al final, cuando la tierra sana, reaparece UNO
  solo — la señal visual de que el bosque vuelve a la vida · Ghibli Wiki
  (Plot) ✅.
- **Dato de producción real**: Miyazaki comentó a los animadores, como
  teoría personal (no necesariamente canónica), que el Kodama solitario
  del final es un Totoro joven — aunque esto choca con lo que se sabe del
  origen de Totoro en otras películas, así que se cuenta como anécdota, no
  como dato confirmado · Ghibli Wiki Trivia (cita un tuit) ⚠️ (una fuente,
  y la propia wiki aclara que no es canon).
- **Por qué el fandom los adora**: entrada propia en «Ugly Cute» de la
  YMMV (ver punto 12) — «raros pero entrañables»; son el secundario con
  más peso emocional pese a no hablar ni una sola línea en toda la
  película.

### Yakul (el elk rojo de Ashitaka)

- **Quién es**: el serau gigante («elk rojo», アカシシ) que monta Ashitaka
  desde el inicio de la película — su compañero más leal, ya aparecía
  antes en *El viaje de Shuna*, la obra previa de Miyazaki de la que nace
  este diseño · Ghibli Wiki (Yakul) ✅.
- **Momento que lo define**: paralizado de miedo frente al jabalí-demonio,
  Ashitaka le dispara una flecha al poste de madera junto a él —el susto
  lo saca del pánico— y entonces sí corre; a partir de ahí nunca lo
  abandona, ni herido, ni en terreno sagrado, ni amenazado por la manada
  de lobos · Ghibli Wiki (Story) ✅.
- **Por qué importa para el punto 7**: pese a no tener ni una línea de
  diálogo, es el CUARTO personaje más popular en las tres fuentes de
  popularidad (AniList, MAL y ranking.net coinciden en ese puesto) — la
  lealtad silenciosa pesa tanto como el diálogo para este fandom, igual
  que pasó con Cabeza de Nabo en *El castillo ambulante*.

### La dinámica San/Ashitaka, para láminas en grupo

- Fotograma `abrazo_final_6960.jpg`, **1:56:00**: los dos de espaldas,
  abrazados en la oscuridad, la marca de la maldición ya casi borrada del
  brazo de Ashitaka — el abrazo de despedida tras la muerte de Moro y la
  restauración del bosque · visto directamente ✅. Coincide con el
  «Cooldown Hug» citado en la página Heartwarming de Tropedia (ver punto
  21) — es la imagen que mejor resume su vínculo sin ser una escena de
  romance convencional (ninguno de los dos se besa ni promete quedarse
  con el otro).

## 20. Gustos y detalles de cada personaje

Aviso honesto (igual que en *El castillo ambulante*): Studio Ghibli **no
publica fichas tipo databook** con cumpleaños/altura/comida favorita como
las series de manga shonen. Se buscó explícitamente en AniList, MyAnimeList,
Ghibli Wiki y Doblaje Wiki: ninguna de las cuatro trae esas fichas para esta
película. Lo que sigue es lo que SÍ está documentado, con fuente:

- **Ashitaka**: edad **17 años**, la única edad de todo el reparto con una
  fuente de producción real (no una wiki de fans): *Colección de
  Storyboards de La princesa Mononoke #11*, Tokuma Shoten, 2002, ISBN
  9784198614751 · ✅. Pelo castaño oscuro, ojos gris oscuro/azulado ·
  Ghibli Wiki (infobox) ✅. **Objeto que siempre lleva**: su arco y flechas
  (arma tradicional Emishi) y, hasta que se la regala a San, la daga de
  cristal de Kaya · Ghibli Wiki ✅. **Cómo se ve a sí mismo**: como alguien
  ya condenado a morir por la maldición — por eso arriesga todo en el
  viaje, no teme perder la vida · Ghibli Wiki (Appearance/curse) ✅. **Lo
  que odia**: la violencia sin sentido y el odio que ciega a la gente de
  cualquier bando · Ghibli Wiki Personality ✅.
- **San**: edad «desconocida (circa 15-17 años)» según el propio infobox
  de Ghibli Wiki · ⚠️ (la wiki lo marca como aproximado, no oficial). Pelo
  castaño chocolate, ojos azul real · Ghibli Wiki ✅. **Cómo se ve a sí
  misma**: como loba, no como humana — rechaza activamente su propia
  especie · Ghibli Wiki Personality ✅. **Objeto que siempre lleva**: la
  máscara de arcilla roja con dos orejas blancas (su rasgo más icónico) y
  el collar con colmillos de lobo · Ghibli Wiki Appearance ✅. **Comida**:
  carne cruda o seca de caza, compartida «a la manera de los lobos» —
  boca a boca, sin entender el significado humano del gesto (ver punto
  13) · TV Tropes + Nausicaa.net + Tumblr ✅.
- **Moro**: 300 años (fallecida) · Ghibli Wiki (infobox) ✅. **Rasgo que la
  define**: sus dos colas, únicas en toda la manada · Ghibli Wiki ✅. **Lo
  que ama**: a San, por encima incluso de su odio a los humanos · Ghibli
  Wiki Personality ✅. **Lo que odia**: a Eboshi en concreto, no a los
  humanos en abstracto — es personal, por haberla dejado inválida de un
  disparo · Ghibli Wiki (Background) ✅.
- **Dama Eboshi**: edad no especificada en ninguna fuente consultada.
  **Le encanta**: el hierro y la tecnología — su proyecto «Kunikuzushi» es
  literalmente su obsesión de vida · Ghibli Wiki ✅. **Objeto que la
  define**: su rifle Ishibiya y su capa negra con el gorro rojo «eboshi»
  que le da su nombre · Ghibli Wiki ✅. **Detalle único**: es la única
  mujer de toda la película que usa lápiz labial · Ghibli Wiki Appearance
  ⚠️ (dato visual/de diseño, no una cita textual).
- **Jigo**: mediana edad («Middle age» en el infobox) · Ghibli Wiki ✅. **Le
  encanta**: la comida y el dinero fácil — se queja de que el agua está
  demasiado caliente y de inmediato intenta cambiar una pepita de oro por
  sacos de arroz (ver frases del punto 8) · ✅ (frase textual + infobox).
  Su menaje de cocina de lujo y que ofrezca miso sin dudar (carísimo en la
  época) delatan que es de más alto estatus del que aparenta · Ghibli Wiki
  Trivia ⚠️ (una fuente).
- Ninguno de los personajes tiene **cumpleaños exacto ni altura oficial
  publicada** — se buscó en AniList, MyAnimeList, Ghibli Wiki y Doblaje
  Wiki; ninguna de las cuatro lo tiene. Esto se anota, no se inventa.

## 21. Por qué la gente la ama

- **Taquilla**: recaudó cerca de **152 millones de dólares** sólo en Japón,
  convirtiéndose en la película más taquillera de la historia de Japón
  hasta ese momento (superó a *E.T.*), y siguió siendo la más taquillera
  del país hasta que *Titanic* la superó meses después, en noviembre de
  1997 — mantuvo el récord de películas JAPONESAS hasta *El viaje de
  Chihiro* (2001) · Wikipedia ES (https://es.wikipedia.org/wiki/La_princesa_Mononoke)
  + búsqueda web (Variety/Collider) ✅ (dos fuentes, mismo orden de
  magnitud).
- **Premios**: ganó el **Japan Academy Prize a Mejor Película de 1997**,
  la PRIMERA película animada en ganar ese premio en Japón; además, Premio
  Especial a Yoshikazu Mera por cantar el tema principal ·
  https://variety.com/1998/digital/features/mononoke-wins-japan-s-best-pic-1117468558/
  + https://en.wikipedia.org/wiki/Japan_Academy_Film_Prize_for_Animation_of_the_Year
  ✅ (dos fuentes).
- **NO fue nominada al Óscar** (mito común): Japón la presentó para Mejor
  Película de Habla No Inglesa en los Premios de la Academia número 70,
  pero no logró la nominación · https://en.wikipedia.org/wiki/Princess_Mononoke
  (sección Accolades) ✅ — dato importante para no repetir el error si el
  redactor u otra parte asume que sí fue nominada.
- **Crítica**: 93% en Rotten Tomatoes (119 críticos, nota media 8/10,
  consenso: «con su historia épica y sus visuales impresionantes, La
  princesa Mononoke es un hito en el mundo de la animación»), 76/100 en
  Metacritic (29 críticos, «generalmente favorable») · Wikipedia EN
  (Reception) ✅. Roger Ebert la llamó un gran logro y «una de las mejores
  películas del año»; antes de su estreno en Chicago dijo «si algún anime
  puede ganarse al público estadounidense, es este» · rogerebert.com
  (búsqueda web) ✅.
- **Por qué conecta, según los académicos**: la investigadora Susan Napier
  escribe que el tema del conflicto y la coexistencia con la naturaleza y
  el mundo espiritual «resonó fuertemente con el público japonés»; varios
  académicos comentaron que el público joven encontró los temas
  identificables con sus propias luchas personales y se sintió acompañado
  por sus motivos de esperanza · Wikipedia EN (Reception/Legacy) ✅.
- **Por qué conecta, según una reseña de fan (ejemplo concreto, no
  genérico)**: 5 razones citadas en un blog de reseña — (1) no hay villano
  claro, la ambigüedad moral refleja la vida real; (2) hasta los
  personajes secundarios sin nombre se sienten reales con pocos gestos;
  (3) los dioses-animales (Moro, Okkoto, el Espíritu del Bosque)
  sorprenden en vez de ser genéricos; (4) mujeres fuertes en todos los
  bandos (San, Eboshi, las trabajadoras de Irontown) sin que sean
  «damiselas»; (5) la relación San/Ashitaka nunca cae en un subargumento
  romántico manido · https://www.joyvspicer.com/joy-blog/2019/4/27/5-reasons-i-love-princess-mononoke
  ⚠️ (una fuente de opinión personal, pero coincide con lo que dicen otras
  reseñas de crítica profesional).
- **Con qué personaje se identifica el público, y por qué NO hay una única
  respuesta**: en Occidente (AniList, MAL) San es la favorita; en Japón
  (ranking.net, encuesta de ねとらぼ/Nlab) gana Ashitaka — ver punto 7. No
  es casualidad: San encarna la rabia hacia la destrucción del entorno (un
  tema que conecta con la preocupación ambiental actual en Occidente),
  mientras Ashitaka encarna el ideal japonés de mediar entre bandos sin
  perder la propia humanidad · cruce de los datos del punto 7 con el
  análisis de Napier arriba, ⚠️ (interpretación propia a partir de fuentes
  verificadas, no una única fuente que lo diga con estas palabras).
- **Escenas que hacen llorar** (capítulo/minuto: al ser película, se da el
  momento de metraje o el nombre de la escena, con la fuente que describe
  QUÉ pasa y POR QUÉ duele — página «Tear Jerker» de Tropedia):
  - **El final**: mientras suena «Ashitaka and San», de Joe Hisaishi, y
    aparece un Kodama en el bosque arrasado pero ya reverdeciendo, se ve
    a una de las leprosas de Eboshi —cubierta de vendas, antes
    condenada a morir— asombrada de estar viva y sana: la lepra era
    sentencia de muerte en la época, así que verla curada es, según
    Tropedia, lo que «hace llorar sin poder controlarlo» a la mayoría de
    espectadores · Tropedia (Tear Jerker) ✅.
  - **La partida de Kaya**, a los 10 minutos de película: cuando Ashitaka
    es desterrado de su aldea para siempre, Kaya rompe las reglas y sale a
    darle su daga de cristal para que no la olvide · Tropedia ✅.
  - **La muerte de Moro y Okkoto**, mientras suena «Adagio of Life and
    Death» de Hisaishi: Ashitaka corre desesperado a salvar a San entre
    los dos — descrito como la pieza más «desgarradoramente hermosa» de
    toda la banda sonora, con tristeza Y esperanza a la vez · Tropedia ✅.
  - **Los Kodama cayendo de los árboles**, apagándose uno a uno mientras
    el bosque muere — criaturas inocentes, ajenas a la guerra entre
    humanos y dioses, muriendo como moscas · Tropedia ✅.
  - **La muerte confundida de Okkoto**: cojeando tras perder la batalla
    contra Irontown, confunde a los hombres cubiertos de piel con sus
    propios guerreros e intenta liderarlos de vuelta al combate — sólo
    para ser envenenado y convertido en un monstruo sin sentido; su
    esperanza ciega y desesperación se describen como «terriblemente
    triste» · Tropedia ✅.

## 22. Fan dubs y comunidad hispana

- **Fandub de San para DUBTOBER 2023** (canal/proyecto VocesalViento, con
  ayuda de una actriz para Lady Eboshi), con las etiquetas
  `#DUBTOBER2023 #FANDUB #DOBLAJECASTELLANO #PRINCESAMONONOKE` ·
  confirmado por búsqueda web (TikTok) ⚠️ (no se localizó la URL directa
  del video ni sus vistas — YouTube pide iniciar sesión desde este
  servidor, ver Bitácora).
- **Vídeo de comparación de los TRES doblajes latinos**: «La Princesa
  Mononoke [1997] Comparación del Doblaje Original y 2 Redoblajes
  [Español Latino]», https://www.youtube.com/watch?v=lOzeMGLkM8E — un
  video dedicado exactamente al tema del punto 8 (qué tanto le interesa al
  público hispano comparar los redoblajes) · ⚠️ (URL real confirmada por
  búsqueda web, pero no se pudieron leer vistas/fecha: `yt-dlp` fue
  bloqueado por YouTube con «Sign in to confirm you're not a bot», error
  429, igual que advierte `AYUDANTE.md`).
- **TikTok con actividad de comunidad hispana**: existen páginas de
  descubrimiento activas «La Princesa Mononoke Castellano» y «La Princesa
  Mononoke San» en TikTok · ⚠️ (confirmado que existen por búsqueda web,
  pero TikTok no da acceso a contenido individual sin sesión desde este
  servidor, así que sólo cuenta como indicio de actividad, no como fuente
  citable por separado — mismo límite que en *El castillo ambulante*).
- **Preservación fan de los doblajes originales**: un usuario de Internet
  Archive («SphinxAnime») subió «La Princesa Mononoke (1997) - Doblaje
  Latino Original + Extras», que junta el doblaje latino original, el
  redoblaje de Zima, el doblaje de España y el audio japonés, con la
  descripción «aquí está la *magnum opus* de Miyazaki (a opinión
  personal)» · https://archive.org/details/la-princesa-mononoke-1997-doblaje-latino-original-extras
  · ✅ (metadata real verificada: 141 archivos, fecha y descripción
  confirmadas con `archive.org/metadata`) — muestra que la comunidad
  hispana se organiza para no perder doblajes que streaming ya no ofrece
  (el doblaje Buena Vista/Miramax original de 2001 no está en ningún
  servicio activo).
- **No se encontró un cover en español del tema principal** «Ashitaka
  Sekki» (アシタカせっき, de Joe Hisaishi) — se buscó explícitamente
  («cover español Mononoke Hime canción tema Ashitaka Sekki») y sólo
  aparecieron versiones instrumentales/piano sin letra y traducciones de
  la letra japonesa, ninguna versión cantada en español · esto se anota
  como «no encontré», no como «no existe».
- **Dailymotion no tiene fandubs relevantes**: se probó directamente con
  la API (`api.dailymotion.com/videos?search=mononoke+fandub` y
  `...cover+cancion`) y sólo aparecieron un fandub en ITALIANO (no
  hispano) y tráilers oficiales ya listados en `datos-voz.md` — la
  comunidad de fandub en español de esta película vive en YouTube/TikTok,
  no en Dailymotion.

## Lo mejor para la lámina

1. San gana en Occidente (AniList/MAL) pero **Ashitaka gana en Japón**
   (ranking.net + encuesta de medios Nlab 2022) — ninguno de los dos es
   una apuesta «segura» por sí solo; usar a los dos juntos (o el abrazo
   final) cubre ambas lecturas del fandom.
2. Hay TRES doblajes latinos, no dos: Buena Vista/Miramax (2001,
   Monterrey), Zima (2010, CDMX) y Wild Bunch/Netflix (2020, CDMX) —
   cualquier frase citada en el canal debe decir cuál.
3. La escena de San dándole de comer a Ashitaka boca a boca es el momento
   de «ternura inesperada» más citado por el fandom (TV Tropes + Tumblr) —
   mejor referencia de tono que una pose genérica de acción.
4. El mundo es Japón rural del período Muromachi con dioses-animales y una
   fundición de hierro: texturas de madera, piedra, musgo, sangre y metal
   forjado, nunca un globo de cómic blanco genérico.
5. El servidor es de doblaje/locución — el ángulo de «tres doblajes
   distintos del mismo personaje» (punto 8) encaja de forma natural con un
   canal de castings o de comparación de voces, más que sólo mostrar arte.

## No encontré

- ⚠️ Encuesta de popularidad hecha por el propio Studio Ghibli (no
  publican rankings oficiales de personajes; sólo hay encuestas de
  medios/fans, ya citadas en el punto 7).
- ⚠️ Databook o ficha oficial con cumpleaños exacto o altura de los
  personajes (se buscó en AniList, MyAnimeList, Ghibli Wiki y Doblaje
  Wiki; ninguna de las cuatro lo tiene para esta película).
- ⚠️ Segunda fuente, fuera de Doblaje Wiki, para el actor de Ashitaka en
  el doblaje Buena Vista/Miramax 2001 (ni la propia Doblaje Wiki lo
  identifica: aparece como «¿?»).
- ⚠️ Vistas/fecha exactas de los fandubs y el video de comparación de
  doblajes en YouTube (VocesalViento DUBTOBER 2023, comparación de los 3
  doblajes): `yt-dlp` fue bloqueado por YouTube con «Sign in to confirm
  you're not a bot» (HTTP 429) al intentar leer sólo los metadatos, tal
  como advierte `AYUDANTE.md`. No se insistió más de un intento.
- ⚠️ Conteo de votos exacto detrás del orden de ranking.net (el sitio
  carga los puntajes por JavaScript; el HTML estático sólo trae el orden
  final 1-18, no el número de votos de cada uno).
- No se encontró un cover en español (Latinoamérica o España) del tema
  «Ashitaka Sekki» — búsqueda explícita sin resultado, distinto de «no
  existe» (ver `AYUDANTE.md`).
- No se encontraron memes o parodias hispanas dedicadas (tipo «versión
  chusca») más allá de los fandubs/covers ya citados en el punto 22 — se
  buscó explícitamente y no apareció nada dedicado.
- No se profundizó en un fotograma propio de la cara de Eboshi ni de Jigo
  (el material `hd/` ya reunido por el investigador de vídeo no tiene
  ninguno de cerca de ellos) — sus perfiles del punto 13 se apoyan en
  wikitext y en las frases del doblaje (punto 8), no en un fotograma
  directo.

## Bitácora de búsqueda

**Fuentes usadas directamente (API/descarga), sin buscador**:
- Doblaje Wiki, API `action=parse&prop=wikitext` sobre «La princesa
  Mononoke» (corrigiendo el error del recolector automático, que había
  bajado la ficha de la serie *Mononoke* de 2007).
- Ghibli Wiki (fandom), API `action=parse&prop=wikitext` sobre San,
  Ashitaka, Moro, Eboshi y Jigo (5 fichas completas).
- Tropedia (mirror en Fandom de TV Tropes), API `action=parse` sobre
  `Princess Mononoke/YMMV`, `/Funny`, `/Heartwarming`, `/Trivia`,
  `/Awesome`, `/Tear Jerker` (con `action=query&list=search` primero para
  encontrar el título exacto de cada subpágina).
- dubdb.fandom.com, API `action=parse` sobre las fichas «Sysdub» y
  «Estudio Tokio» de la película (segunda fuente para el reparto Wild
  Bunch y Zima).
- Audio oficial de Doblaje Wiki (`static.wikia.nocookie.net`): 6 muestras
  `.ogg` descargadas (API `imageinfo` para la URL real) y transcritas con
  `herramientas/voz.py` (Whisper, en español) — San (Wild Bunch y Buena
  Vista), Ashitaka, Moro, Eboshi y Jigo (Wild Bunch).
- `herramientas/fotogramas.py`, material YA reunido por el investigador de
  vídeo de este mismo encargo (`/tmp/claude-0/trabajo/100-la-princesa-mononoke-video/hd/`),
  mirado aquí directamente con Read: 5 fotogramas de metraje real (no
  tráiler) con segundo exacto en el nombre de archivo.
- MyAnimeList: HTML de `.../characters` bajado con `curl` (favoritos por
  personaje, sin depender de la API Jikan, que estaba caída/504).
- ranking.net Japón (`best-mononokehime-characters`): HTML bajado con
  `curl`, orden 1-18 extraído de las cabeceras `<h3>`.
- Reddit vía `arctic-shift.photon-reddit.com` sobre r/ghibli y
  r/PrincessMononoke (varias consultas, con reintentos espaciados por los
  timeouts del servicio).
- `api.dailymotion.com` (búsqueda directa, no buscador) para fandub/cover.
- `archive.org/metadata` para confirmar el archivo de preservación de
  doblajes.
- Wikipedia en español (`es.wikipedia.org/w/api.php`, extracto de texto) y
  en inglés (`en.wikipedia.org/w/api.php`, con reintento tras un 429 de
  «too many requests» compartido con otros ayudantes en el mismo
  contenedor).
- `yt-dlp --skip-download` sobre un video de YouTube: bloqueado por
  YouTube (ver «No encontré»), no se insistió.

**Buscador web (idioma entre paréntesis), de un cupo de ~50**:
1. Princess Mononoke box office Japan Academy Prize awards (en)
2. Princess Mononoke Rotten Tomatoes Roger Ebert review (en)
3. La Princesa Mononoke fandub español latino YouTube San Ashitaka (es)
4. cover español "Mononoke Hime" canción tema Ashitaka Sekki (es)
5. VocesalViento DUBTOBER 2023 San Mononoke fandub (es)
6. Princess Mononoke identify character why people love reddit essay (en)
7. もののけ姫 人気投票 サン アシタカ キャラクター ランキング (ja)
8. VocesalViento cover doblaje fandub (es)
9. ANMTV La princesa Mononoke redoblaje Netflix reparto actores 2020 (es)
10. comparación doblaje La Princesa Mononoke Zima Wild Bunch Disney youtube (es)
11. Princesa Mononoke cosplay San doblaje latino actriz voz entrevista (es)
12. Princess Mononoke San feeds Ashitaka meat mouth scene (en)
13. Princess Mononoke 5 reasons I love it blog (en, por lectura directa)

Todo lo pesado (audios, JSON de wikis, HTML de rankings, fotogramas
compartidos con vídeo) quedó en
`/tmp/claude-0/trabajo/100-la-princesa-mononoke-voz/`, fuera del repo.
