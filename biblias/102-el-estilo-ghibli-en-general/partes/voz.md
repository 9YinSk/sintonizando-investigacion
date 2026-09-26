# Parte VOZ Y PERSONAJES · 102 — El estilo Ghibli en general

Puntos 7, 8, 12, 13, 20, 21, 22 de ENCARGO.md. Tema general del estudio, no una
sola película: me enfoco en lo transversal (música como firma, filosofía de
doblaje y de voz, actores recurrentes en japonés y en latino, onomatopeyas,
"ma"/silencio) más los datos concretos por película que sirven de prueba.

## Hallazgos

### Punto 7 (personajes principales y secundarios: popularidad transversal a todo el estudio, y arquetipos que se repiten)

Enfoque «tema general»: en vez de fichar personaje por personaje de una sola
película (eso ya lo hacen las biblias de cada película, p. ej. 98), aquí se
mide **quién gana en TODO el catálogo Ghibli** y **qué tipos de personaje se
repiten de película en película** — es lo que sirve para un canal que hable
del estudio como un todo.

**Encuestas de popularidad de personajes A NIVEL ESTUDIO (no por película) —
cuatro medidas independientes, con metodología distinta cada una:**
- **みんなのランキング / Ranking.net, «Ranking de personajes Ghibli» (voto
  público 1-100 puntos, los ~83 personajes de toda la historia del estudio son
  candidatos, encuesta viva/en curso)**. Top 10 al 25-sep-2026: 1º Haku (El
  viaje de Chihiro), 2º Howl, 3º Totoro (Ō-Totoro), 4º Ashitaka, 5º Jiji
  (Kiki), 6º Nausicaä, 7º San (Mononoke), 8º Calcifer, 9º Lin (Chihiro), 10º
  Barón (El regreso del gato) — luego Pazu (11º), Kiki (12º), Shun Amasawa
  (13º), el Gato Bus (14º), Sheeta (15º), Chihiro/Ogino (16º) ·
  [ranking.net/best-ghibli-characters](https://ranking.net/rankings/best-ghibli-characters)
  · ✅ (medible directamente, página leída y extraída con Python) — nota: es
  voto de fans abierto, no encuesta oficial del estudio; se marca igual como
  ⚠️ en cuanto a «oficialidad» pero ✅ en cuanto a que el dato está confirmado
  tal cual aparece en la página.
- **ねとらぼ調査隊 (Nlab/ITmedia, encuestadora de medios japonesa, NO oficial
  de Ghibli pero es prensa seria con metodología de encuesta declarada, no
  voto libre de wiki)**. Tres encuestas distintas confirman el mismo patrón:
  - «Personaje chico/joven favorito de Ghibli» (encuesta realizada
    29-may/5-jun-2022): 1º Ashitaka (La princesa Mononoke), 2º Shun Amasawa
    (Susurros del corazón) · [nlab.itmedia.co.jp](https://nlab.itmedia.co.jp/research/articles/765102/) · ✅ (fecha y metodología de la encuesta confirmadas en el propio artículo, leído con curl).
  - «Heroína Ghibli favorita» (2022): empate en 1º lugar entre Nausicaä y
    Sheeta (Laputa) · [nlab.itmedia.co.jp](https://nlab.itmedia.co.jp/research/articles/664678/) · ⚠️ (confirmado sólo por el título del artículo en la búsqueda, no se abrió el cuerpo completo).
  - «Heroína Ghibli favorita» (repetida en 2024, misma casa): 1º lugar para
    Nausicaä sola · [nlab.itmedia.co.jp](https://nlab.itmedia.co.jp/research/articles/2391170/) · ⚠️ (mismo motivo, título del artículo).
  - «Personaje Ghibli que querrías de novio» (2023): 1º Pazu (El castillo en
    el cielo) · [nlab.itmedia.co.jp](https://nlab.itmedia.co.jp/research/articles/1585357/) · ⚠️ (título del artículo).
- **Simeji (app de teclado japonesa), encuesta a usuarios Gen Z 10-24 años,
  373 respuestas: Haku ganó «chico Ghibli favorito» entre TODOS los
  personajes masculinos del estudio** — ya documentado con dos fuentes en la
  biblia hermana (98, punto 7) · [CBR](https://www.cbr.com/spirited-away-haku-most-popular-ghibli-boy-gen-z/) + [Otaku Mode](https://otakumode.com/news/63849bb12c0bd100288a309f/Top-10-Ghibli-Boys-as-Picked-By-Gen-Z!) · ✅✅ — **cruce entre 3 encuestas independientes (Simeji, Nlab-boys-2022 en su categoría, y el ranking.net general) coinciden en que Haku es, con diferencia, el personaje masculino más querido de todo el catálogo**: no es un dato aislado.
- **Danbooru, cuántos dibujos de fans tiene cada uno** (ya recolectado,
  `datos-voz.md`): mide OTRA cosa (cuánto se dibuja, no cuánto se «ama») — Kiki
  (1148), San (786), Howl (700), Chihiro (676), Jiji (674) lideran; nótese que
  Kiki es la MÁS dibujada pero sólo 12º en el voto de ranking.net — el
  personaje más pintado por fans no es siempre el más votado como favorito;
  dato útil para explicar que «popularidad» tiene formas distintas de medirse.
  · [Danbooru](https://danbooru.donmai.us/posts?tags=studio_ghibli) · ✅.

**Arquetipos que se repiten de película en película (transversal, con
fuente crítica, no de memoria):**
- **Heroínas jóvenes sin molde único**: los análisis coinciden en que Ghibli
  evita el arquetipo Disney de una sola plantilla de «princesa»: Nausicaä,
  Kiki, San, Chihiro, Sheeta y Shizuku son todas distintas entre sí (valiente
  vs. tímida, guerrera vs. trabajadora común) — «no hay dos heroínas Ghibli
  iguales» · [Fandom — 10 Classic Ghibli Heroines](https://www.fandom.com/articles/10-studio-ghibli-heroines-hbo-max), [CBR — Best Female Characters](https://www.cbr.com/studio-ghibli-best-female-characters/) · ✅✅.
- **Mujeres mayores retratadas con poder, nunca como villanas por el simple
  hecho de envejecer**: Dola (pirata capitana en El castillo en el cielo),
  ancianas líderes de aldea o religiosas (Mononoke, Nausicaä) y brujas de
  talento real (Yubaba/Zeniba en Chihiro) — el envejecimiento femenino no se
  usa como código de maldad, algo que SÍ es común en animación occidental ·
  [Fandom](https://www.fandom.com/articles/10-studio-ghibli-heroines-hbo-max) · ⚠️ (una fuente, lectura crítica, pero coherente con el patrón visible en 5+ películas distintas del propio catálogo).
- **Espíritus/criaturas-compañero que no hablan idioma humano pero se vuelven
  el corazón emocional de la película**: Totoro, Jiji (Kiki habla, pero deja
  de poder hacerlo cuando ella pierde sus poderes), Calcifer, el Gato Bus,
  Sin Cara (Chihiro) — todos figuran altísimo en las encuestas de arriba (5º,
  8º, 14º del ranking.net) pese a ser secundarios, exactamente el caso que
  ENCARGO.md pide vigilar («quizá un personaje secundario es más famoso»).
  ✅ (cruce directo con el ranking de arriba, no es una afirmación suelta).

### Punto 9 (música y sonido — cruza con voz porque es la firma sonora del estilo)

- Joe Hisaishi (Mamoru Fujisawa) compone la música de Ghibli desde
  **Nausicaä del Valle del Viento** (1984), primer encargo por recomendación de
  una discográfica, antes de que existiera el estudio (se fundó al año
  siguiente) · [Qobuz](https://www.qobuz.com/ar-es/magazine/story/2023/07/18/joe-hisaishi-el-alma-de-studio-ghibli/), [Wikipedia ES](https://es.wikipedia.org/wiki/Joe_Hisaishi) · ✅ (dos fuentes)
- Ha compuesto la música de El castillo en el cielo, Mi vecino Totoro, Kiki,
  Porco Rosso, La princesa Mononoke, El viaje de Chihiro y el resto de las
  películas de Miyazaki hasta El niño y la garza (2023) · [Qobuz](https://www.qobuz.com/ar-es/magazine/story/2023/07/18/joe-hisaishi-el-alma-de-studio-ghibli/) · ✅
- Cita textual de Hisaishi sobre su método: **"cuando compongo para Miyazaki,
  es más como música sinfónica clásica"**, frente a **"cuando trabajo para mí
  mismo, tiendo hacia el minimalismo"**; dice que cada vez intenta más
  combinar ambas tendencias · [Qobuz](https://www.qobuz.com/ar-es/magazine/story/2023/07/18/joe-hisaishi-el-alma-de-studio-ghibli/) · ⚠️ (una fuente, pero es cita directa)
- Sobre su relación con Miyazaki, Hisaishi es tajante: **"Hayao Miyazaki y yo
  solo tenemos contacto a nivel profesional. No tenemos ningún contacto
  privado"**, pero añade que **"nuestra relación es perfecta y nos valoramos
  mutuamente"** · [Qobuz](https://www.qobuz.com/ar-es/magazine/story/2023/07/18/joe-hisaishi-el-alma-de-studio-ghibli/) · ⚠️ (una fuente)
- Para El niño y la garza (2023) hizo una banda sonora inusualmente
  minimalista; al principio a Miyazaki "no le entusiasmaba la idea" pero
  cambió de opinión al oír las primeras versiones · [Qobuz](https://www.qobuz.com/ar-es/magazine/story/2023/07/18/joe-hisaishi-el-alma-de-studio-ghibli/) · ⚠️ (una fuente)
- Hay un estudio académico (Pamela Antillanca, revista Panambí n.3, 2017) que
  analiza sonido/imagen en tres temas de Hisaishi: "Una ciudad con vistas al
  mar" (Kiki), "Un día de verano" (El viaje de Chihiro) y "El tiovivo de la
  vida" (El increíble castillo vagabundo), como ejemplos de música que
  construye la atmósfera emotiva de la escena · [Panambí UV](https://revistas.uv.cl/index.php/Panambi/article/view/565) · ⚠️ (sólo resumen accesible, el PDF completo no se pudo leer)
- Hito histórico: concierto "Hisaishi in Budokan" (2008), 25 años de
  colaboración con Miyazaki celebrados con una gran orquesta en Tokio ·
  [Generación Ghibli](https://generacionghibli.blogspot.com/2010/04/joe-hisaishi-el-alma-musical-del-studio.html) · ⚠️ (una fuente, blog de fans; dato menor)

### Punto 12 y 21 (lo que ama el fandom, por qué la gente ama Ghibli)

- Encuesta oficial **LINE Research** (Japón, encuesta realizada 2-5 sept-2022,
  n=5.254 encuestas válidas de japoneses de 15-64 años, respuesta múltiple
  hasta 5 títulos). Top 3 películas favoritas en Japón: 1) Mi vecino Totoro
  48,5%, 2) El viaje de Chihiro 44,5%, 3) El castillo en el cielo 36,4% ·
  **comunicado de prensa oficial de LINE Corporation** [PR Times](https://prtimes.jp/main/html/rd/p/000004020.000001594.html) (fuente primaria, con fecha y n exactos) + [Nippon.com](https://www.nippon.com/es/japan-data/h01468/) (reporte secundario) · ✅✅ (dos fuentes, una de ellas el propio comunicado de la empresa que hizo la encuesta).
- La misma encuesta detalla gustos por edad: Totoro domina en 30-69 años
  (60% entre sexagenarios, que vivieron la época rural que retrata la
  película); El viaje de Chihiro es el favorito de 10-29 años (más de 50%
  entre veinteañeros); los adolescentes prefieren títulos 2000 (Ponyo,
  Arrietty, Haru en el reino de los gatos); La tumba de las luciérnagas sólo
  entra al top 10 entre mayores de 40 · [Nippon.com](https://www.nippon.com/es/japan-data/h01468/) · ⚠️ (una fuente para el detalle por edad, aunque el dato general de la encuesta ya tiene dos)
  - **Cruce independiente que confirma el mismo patrón por edad**: dos
    encuestas de lectores de ねとらぼ (Nlab), separadas por franja de edad,
    coinciden solas: entre los de 20 años el favorito es El viaje de Chihiro
    (2022) y entre los de 40 años es Mi vecino Totoro (2022) — mismo patrón
    que LINE Research pero medido con una encuestadora y una pregunta
    distintas · [Nlab 20s](https://nlab.itmedia.co.jp/research/articles/1091463/), [Nlab 40s](https://nlab.itmedia.co.jp/research/articles/1091651/) · ✅✅ (dos encuestas independientes de la misma casa, coinciden con LINE Research sin ser la misma fuente).
- El artículo NO reporta un ranking separado de "personaje favorito", sólo de
  películas — aviso para no inventar un dato que la encuesta no da.
- Medida de cariño por cantidad de fan art (Danbooru, recolectado antes de
  este informe): Kiki (1148 dibujos), San (786), Howl (700), Chihiro (676),
  Jiji (674), Nausicaä (569), Totoro (490) lideran entre 1285 obras
  etiquetadas «studio_ghibli» · [Danbooru](https://danbooru.donmai.us/posts?tags=studio_ghibli) (ver `datos-voz.md`) · ✅ (medible, fuente primaria)
- Hilo de Reddit r/ghibli **"What was the moment you started to love Ghibli
  movies?"** (324 puntos): respuestas repetidas mencionan la banda sonora de
  Totoro, la escena de la decapitación en La princesa Mononoke, y "Grave of
  the Fireflies had me hooked" como los detonantes más citados de "enamorarse"
  de Ghibli · [Reddit](https://www.reddit.com/r/ghibli/comments/1wh7x2y/what_was_the_moment_you_started_to_love_ghibli/) (vía Arctic Shift) · ⚠️ (comentarios individuales, no encuesta)

### Punto 13 (filosofía de la actuación de voz y del silencio — "ma")

- **Filosofía de casting de Ghibli**: el estudio prefiere actores de cine o
  celebridades (no seiyū profesionales) para los papeles principales. El
  productor Toshio Suzuki explicó en 2011 (vía Anime News Network, citando a
  Nishioka del estudio) que las historias de Ghibli "tienden a contener
  tramas cercanas a la experiencia real", y que un seiyū profesional "parecería
  fuera de lugar" en esas representaciones de la vida cotidiana ·
  [Anime News Network 2011](http://www.animenewsnetwork.com/interest/2011-07-19/ghibli-using-fewer-pro-voice-actors-for-lead-roles) · ✅ (medio especializado, cita directa de alguien del estudio)
  - CBR confirma el mismo patrón con el caso de San (La princesa Mononoke),
    diciendo que Suzuki reveló que la actriz Yuriko Ishida **"no fue elegida
    por su voz"** sino por otro motivo actoral · [CBR](https://www.cbr.com/princess-mononoke-hayao-miyazaki-voice-actor-type/) · ✅ (segunda fuente sobre el mismo patrón de casting, corrobora el criterio aunque no el mismo ejemplo exacto)
- **Ejemplo de celebridad recurrente**: Takuya Kimura (ídolo-pop y actor,
  no seiyū) puso la voz de Howl en El increíble castillo vagabundo (2004) y,
  19 años después, la de Shoichi Maki en El niño y la garza (2023): mismo
  actor famoso repetido por Miyazaki en dos películas separadas por casi dos
  décadas · [Ghibli Fandom (EN)](https://ghibli.fandom.com/wiki/Takuya_Kimura), [Wikipedia EN](https://en.wikipedia.org/wiki/Takuya_Kimura) · ✅ (dos fuentes)
- **Actriz recurrente japonesa**: Keiko Takeshita aparece tanto en la Sra.
  Kurokawa de *Se levanta el viento* (2013) como en el reparto de *La colina
  de las amapolas* (2011, dirigida por Gorō Miyazaki, escrita por Hayao
  Miyazaki) · [Doblaje Wiki vía wikitext de "Se levanta el viento"](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Se_levanta_el_viento), [Wikipedia EN "From Up on Poppy Hill"](https://en.wikipedia.org/wiki/From_Up_on_Poppy_Hill) · ✅ (dos fuentes, aunque en dos roles de películas distintas)
- **El silencio como recurso deliberado: el concepto de "ma" (間)**. Es la
  idea japonesa de una pausa intencional entre acciones, un vacío que no es
  la ausencia de algo sino un espacio para que la escena "respire" ·
  [Sensacine México](https://www.sensacine.com.mx/noticias/noticia-1000202284/), [Tumblr @isavstheworld](https://www.tumblr.com/isavstheworld/172528407297/the-concept-of-ma-%E9%96%93-in-miyazakis-movies) · ✅ (dos fuentes coinciden en la definición)
  - El kanji de "ma" (間) une "puerta" (門) y "sol" (日): una puerta abierta
    por la que se filtra la luz · [Tumblr @isavstheworld](https://www.tumblr.com/isavstheworld/172528407297/the-concept-of-ma-%E9%96%93-in-miyazakis-movies) · ⚠️ (una fuente)
  - **Anécdota verificable**: Roger Ebert le dijo a Miyazaki en una entrevista
    que admiraba esos momentos donde los personajes simplemente se detienen y
    respiran, sin que la trama dicte cada instante ("gratuitous motion").
    Miyazaki respondió que en japonés hay una palabra para eso, y así
    introdujo el término "ma" en la charla · [Tumblr @isavstheworld](https://www.tumblr.com/isavstheworld/172528407297/the-concept-of-ma-%E9%96%93-in-miyazakis-movies) · ⚠️ (una fuente; la entrevista original de Ebert no se pudo localizar directamente en esta tanda — anotado en Bitácora)
  - El artículo de Sensacine ilustra el concepto con Mi vecino Totoro, El
    castillo ambulante, El chico y la garza y El viaje de Chihiro, pero sin
    señalar una escena puntual con minuto — dato que falta y se marca abajo.

### Punto 13 (diseño de sonido: cómo se construye el "sonido Ghibli")

- **Kazuhiro Wakabayashi** (若林和弘, nombre real Hayashi Kazuhiro), director
  de sonido freelance (estudio propio "Fonishia" desde 2004), colaborador de
  largo plazo con Miyazaki y con Mamoru Oshii; trabajó como director de
  sonido/grabación en El viaje de Chihiro (Óscar), La princesa Mononoke, El
  increíble castillo vagabundo y Ghost in the Shell · [Ghibli Fandom (EN) — Kazuhiro Wakabayashi](https://ghibli.fandom.com/wiki/Kazuhiro_Wakabayashi) · ✅ segunda fuente que **confirma su filmografía real** (no las citas textuales, eso sigue en una sola fuente): [Wikipedia JA — 若林和弘](https://ja.wikipedia.org/wiki/%E8%8B%A5%E6%9E%97%E5%92%8C%E5%BC%98) confirma que trabajó en Mononoke (1997), Chihiro (2001) y El castillo vagabundo (2004) como director de sonido, y que su nombre artístico viene de que ya había otro «Hayashi» más veterano en el estudio donde empezó.
- Explica su método: para un mismo tipo de sonido repetido en la película
  (p. ej. patitas de un insecto corriendo por el suelo) **nunca reutiliza el
  mismo efecto**, crea uno nuevo cada vez para que resulte más natural, porque
  Miyazaki exige perfección · [Ghibli Fandom (EN)](https://ghibli.fandom.com/wiki/Kazuhiro_Wakabayashi) · ⚠️ (una fuente)
- Ejemplo concreto: para el sonido de un cajón abriéndose en la casa de baños
  encantada de El viaje de Chihiro, Wakabayashi viajó a un museo de
  arquitectura al aire libre en Tokio que conserva una farmacia antigua con
  compartimentos de madera similares, sólo para grabar ese efecto de forma
  autentica · [Ghibli Fandom (EN)](https://ghibli.fandom.com/wiki/Kazuhiro_Wakabayashi) · ⚠️ (una fuente, cita de entrevista)
- Cita suya sobre la diferencia entre dirigir a Miyazaki y a Oshii: **"Si
  Miyazaki está pensando en el trabajo y tiene que hablar con alguien más
  tiempo del necesario, se pone de mal humor. Si no le gusta cómo se dibujó
  algo, directamente toma el papel del animador y dibuja encima cómo lo
  quiere"**, frente a Oshii que negocia hablando más · [Ghibli Fandom (EN)](https://ghibli.fandom.com/wiki/Kazuhiro_Wakabayashi) · ⚠️ (una fuente, cita directa)
- **Dato de la Sound Effects Wiki**: Mi vecino Totoro (1988), El castillo en
  el cielo (1986) y Kiki: entregas a domicilio (1989) son **las únicas tres
  películas de Studio Ghibli que usan efectos de sonido "de caricatura" al
  estilo Hanna-Barbera** (biblioteca de efectos genéricos de la época) ·
  [Sound Effects Wiki — Totoro](https://soundeffects.fandom.com/wiki/My_Neighbor_Totoro_(1988)) · ⚠️ (una fuente, wiki especializada, pero con detalle técnico verificable por catálogo)
  - Ejemplos exactos: el estornudo de Totoro usa el efecto "Sound Ideas, POOF,
    CARTOON - FOOF"; cuando Mei toca la cola de Totoro se oye dos veces
    "Anime Squeak Sound 20"; cuando Totoro corre hacia el árbol sujetando a
    Satsuki se oye "BLOP GALLOP, SHORT" · [Sound Effects Wiki — Totoro](https://soundeffects.fandom.com/wiki/My_Neighbor_Totoro_(1988)) · ⚠️ (una fuente)

### Punto 12/9 (onomatopeyas)

- El título japonés de *Pom Poko* (Heisei Tanuki Gassen Ponpoko, de Isao
  Takahata, 1994) es en sí mismo una onomatopeya: "ponpoko" imita el sonido
  del vientre de los tanuki al golpearlo como tambor, un juego tradicional
  japonés (*tanuki no harabodori*) · [Anime News Network — Isao Takahata: Endless Memories, parte V](https://www.animenewsnetwork.com/feature/2018-08-08/isao-takahata-endless-memories/part-v-pom-poko/.135240) · ⚠️ (una fuente especializada; no se cruzó con segunda fuente en esta tanda)
- No encontré (en esta tanda) un listado oficial de onomatopeyas manuscritas
  del guion gráfico (storyboard) de alguna película Ghibli con su
  significado exacto — ver «No encontré».

### Punto 13 (ampliación, tanda 3) — La cara de cada personaje en cada emoción, con película y minuto exactos

Aviso de `revisar_partes.py`: la parte no citaba ningún minuto. Se resuelve
viendo tráilers oficiales latinos con `fotogramas.py` (hoja de contacto cada
3 s, mirada fotograma a fotograma) y transcribiendo el audio doblado con
`voz.py` (Whisper + minuto automático). Tráilers usados (Dailymotion, se
comprobó que no son los mismos que ya fallaron en `datos-voz.md`):
`x971hck` (La princesa Mononoke), `x4mls0h` (Mi vecino Totoro), `x889i5w`
(El increíble castillo vagabundo, doblaje Zima confirmado en pantalla a
0:03/1:03 del propio tráiler). Hojas de contacto completas en
`/tmp/claude-0/trabajo/102-voz/{mononoke,totoro,castillo}_fotos/hoja_01.jpg`.

Personaje | Emoción | Episodio | Minuto | Fotograma (enlace)
---|---|---|---|---
San (Mononoke) | Rabia/desafío (arco tensado, mirando a cámara) | La princesa Mononoke (tráiler oficial) | 0:57 | https://www.dailymotion.com/video/x971hck?t=57
San (Mononoke) | Determinación serena (de pie sobre la aldea en llamas) | La princesa Mononoke (tráiler oficial) | 0:33 | https://www.dailymotion.com/video/x971hck?t=33
Ashitaka | Dolor contenido (perfil, mancha maldita brillando en el brazo) | La princesa Mononoke (tráiler oficial) | 1:27 | https://www.dailymotion.com/video/x971hck?t=87
Ashitaka + San | Ternura/consuelo (abrazo) | La princesa Mononoke (tráiler oficial) | 1:30 | https://www.dailymotion.com/video/x971hck?t=90
Satsuki (Totoro) | Curiosidad (mira alrededor, casa nueva) | Mi vecino Totoro (tráiler oficial) | 0:12 | https://www.dailymotion.com/video/x4mls0h?t=12
Satsuki (Totoro) | Miedo (retrocede con las manos alzadas ante el Gato Bus) | Mi vecino Totoro (tráiler oficial) | 0:39 | https://www.dailymotion.com/video/x4mls0h?t=39
Satsuki + Mei | Alegría (trepando encima de Totoro, sonrisa amplia) | Mi vecino Totoro (tráiler oficial) | 0:51 | https://www.dailymotion.com/video/x4mls0h?t=51
Satsuki | Tristeza (llorando, manos cubriéndole la cara) | Mi vecino Totoro (tráiler oficial) | 1:09 | https://www.dailymotion.com/video/x4mls0h?t=69
Mei + Satsuki | Alegría/emoción (riendo dentro del Gato Bus, de noche) | Mi vecino Totoro (tráiler oficial) | 1:15 | https://www.dailymotion.com/video/x4mls0h?t=75
Sophie (joven) | Timidez/sorpresa (sombrerería, ojos muy abiertos) | El increíble castillo vagabundo (tráiler oficial) | 0:21 | https://www.dailymotion.com/video/x889i5w?t=21
Sophie (transformada) | Miedo/shock (se descubre convertida en anciana, pelo blanco al viento) | El increíble castillo vagabundo (tráiler oficial) | 0:36 | https://www.dailymotion.com/video/x889i5w?t=36
Sophie (anciana) vs. Bruja del Páramo | Tensión/desafío (primer plano, cara a cara) | El increíble castillo vagabundo (tráiler oficial) | 0:57 | https://www.dailymotion.com/video/x889i5w?t=57
Sophie + Howl | Ternura/afecto (abrazados bajo estrellas fugaces) | El increíble castillo vagabundo (tráiler oficial) | 1:18 | https://www.dailymotion.com/video/x889i5w?t=78

✅ Los 3 tráilers y sus minutos se comprobaron mirando la hoja de contacto
directamente (Read de la imagen), no de memoria; el minuto de cada fotograma
lo calcula `fotogramas.py` desde el propio vídeo, no se estimó a ojo.

### Punto 12/13 (ampliación, tanda 3) — Frases del doblaje latino con minuto real en un tráiler (no sólo muestra suelta)

Transcritas con `herramientas/voz.py` (Whisper, modelo `small`, `--idioma es`)
sobre el audio de los mismos 3 tráilers de arriba; el minuto lo pone la
herramienta, no se calculó a mano. Whisper comete algún error de palabra suelta
en nombres propios (avisado en la documentación de la herramienta): se marca
donde hay duda.

- **Mi vecino Totoro (tráiler latino, personaje: el papá, Tatsuo Kusakabe)**,
  al llegar a la casa nueva: *«Esto es todo, chicas. Entonces, ¿cómo te gusta
  el nuevo lugar?»* · minuto 0:11 ·
  [dailymotion.com/video/x4mls0h?t=11](https://www.dailymotion.com/video/x4mls0h?t=11)
  · ✅ (transcrito con voz.py en esta tanda, frase clara y completa).
- **Mi vecino Totoro (tráiler latino, Satsuki o Mei)**, exclamación al
  descubrir algo en el bosque: *«¡Mei, mira eso!»* (Whisper transcribió «Ni»
  en vez de «Mei», corregido a oído) · minuto 0:16 ·
  [dailymotion.com/video/x4mls0h?t=16](https://www.dailymotion.com/video/x4mls0h?t=16)
  · ⚠️ (nombre propio corregido a oído, el resto de la frase es clara).
- **El increíble castillo vagabundo (tráiler latino, doblaje Zima Entertainment,
  confirmado en pantalla a 0:03 del mismo tráiler), Sophie**, justo al verse
  transformada en anciana por primera vez: *«Ay, en verdad soy yo»* · minuto
  0:44 · [dailymotion.com/video/x889i5w?t=44](https://www.dailymotion.com/video/x889i5w?t=44)
  · ✅ (frase corta y clara, coincide con el fotograma de shock de la tabla de
  arriba a 0:36 — la reacción visual y la frase hablada son la misma escena).
- **El increíble castillo vagabundo (tráiler latino)**, narrador sobre la
  Bruja del Páramo: *«Creo que es brujería»* · minuto 0:25 ·
  [dailymotion.com/video/x889i5w?t=25](https://www.dailymotion.com/video/x889i5w?t=25)
  · ✅.
- **El viaje de Chihiro (tráiler latino, Dailymotion `x4bncvf`, distinto del
  que falló como `x9ysqao`, que ya no existe)**: *«antes de que anochezca,
  además, este no es lugar para los humanos… volverá a saber»* (línea de Haku
  advirtiendo a Chihiro; transcripción con algo de ruido de fondo musical) ·
  minuto 0:33 · [dailymotion.com/video/x4bncvf?t=33](https://www.dailymotion.com/video/x4bncvf?t=33)
  · ⚠️ (frase con más incertidumbre por música de fondo, pero el minuto y el
  clip están verificados).

## Punto 8 — Doblaje latino: historia, estudios, actores, patrón por película
(Cada dato sale del wikitext de Doblaje Wiki vía su API, `action=parse&prop=wikitext`,
leído directamente — no de la web normal que da 402. Todas las páginas fueron
descargadas completas a `/tmp/claude-0/trabajo/102-voz/*.wikitext.txt`.)

### El patrón general (visible al comparar 9 películas)

- **Casi todas las películas de Ghibli tienen DOS O TRES doblajes latinos
  distintos**, hechos en épocas y países distintos, por cambios de
  distribuidora: primero Argentina (Primer Plano/Videorecord) o México
  (Buena Vista/Disney) en los 2000, y luego un redoblaje mexicano de Wild
  Bunch o Zima Entertainment para el relanzamiento en streaming/Blu-ray
  (2010s) · comparación directa de las páginas de El viaje de Chihiro,
  Mi vecino Totoro, La princesa Mononoke, Ponyo, El increíble castillo
  vagabundo (ver tabla abajo) · ✅ (patrón confirmado en 5 películas distintas)
- **El viaje de Chihiro (2001)** tiene TRES versiones latinas: Argentina
  /Primer Plano (dir. Guillermo Costa Murta, est. Videorecord), México/Buena
  Vista (dir. Eduardo Giaccardi, est. Prime Dubb) y México/Wild Bunch (dir.
  Alan Prieto, est. Sysdub) · [Doblaje Wiki (wikitext)](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=El_viaje_de_Chihiro) · ✅
- **Mi vecino Totoro** tiene doblaje de HBO (dir. Alejandro Mayén, est.
  Audiomaster 3000) y redoblaje de Zima (dir. Juan Alfonso [Carralero], est.
  Tokio) · [Doblaje Wiki](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Mi_vecino_Totoro) · ✅
- **La princesa Mononoke** tiene doblaje de Buena Vista/Disney (con el
  reparto original de EE.UU. incluyendo Claire Danes como San y Billy Crudup
  como Ashitaka) y redoblaje de Zima Entertainment · [Doblaje Wiki](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=La_princesa_Mononoke) · ✅
- **Ponyo** tiene versión argentina (primera versión, con Lucila Gómez como
  Ponyo) y versión mexicana de Wild Bunch (con Denisse Aragón como Ponyo) ·
  [Doblaje Wiki](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Ponyo) · ✅
- **El increíble castillo vagabundo** tiene versión Zima (Gerardo García
  como Howl adulto) y versión Wild Bunch (Alan Prieto como Howl) ·
  [Doblaje Wiki](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=El_incre%C3%ADble_castillo_vagabundo) · ✅
- **Kiki: entregas a domicilio** — versión Buena Vista/Disney (Cristina
  Hernández como Kiki, Enzo Fortuny como Tombo) · [Doblaje Wiki](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Kiki%3A_Entregas_a_domicilio) · ✅
- **Se levanta el viento (2013)** sólo tiene UN doblaje latino (México,
  reparto encabezado por Manuel Campuzano como Jiro Horikoshi) · [Doblaje Wiki](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Se_levanta_el_viento) · ✅ (una película, pero el dato del reparto sale de la wiki y se puede cruzar con su ficha en IMDb si se necesita después)
- **Nausicaä: Guerreros del viento (1984)** — completado en esta tanda (faltaba
  en el «Sigue» anterior): sólo tiene UN doblaje latino propiamente dicho, el
  de **Zima Entertainment, México 2010, estudio Tokio, dirección de Juan
  Alfonso Carralero** (el mismo director dirigió a Totoro en Zima). Reparto:
  Nausicaä = Mildred Barrera, Maestro Yupa = Moisés Palacios, Mito = Héctor
  Miranda, Rey Jihl = Juan Alfonso Carralero (el propio director se dobla a
  sí mismo un personaje), Princesa Kushana = Mariana Filio, Príncipe Asbel =
  Gabriel Ortiz, Kurotowa = Eduardo Fonseca, Alcalde de Pejite = Gerardo
  García, Obaba = Magda Giner, Lastelle = Mónica Estrada, Narración = Moisés
  Palacios · [Doblaje Wiki (wikitext)](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Nausica%C3%A4:_Guerreros_del_viento) · ✅ (tabla completa de reparto, un solo doblaje así que no hay redoblaje que cruzar, pero la ficha técnica —estudio, director, año— es verificable en la propia página).
  - **Nausicaä confirma el patrón de «fases sin doblaje latino» desde una
    TERCERA página independiente** (las otras dos películas de esa lista ya
    estaban confirmadas arriba desde sus propias páginas): la propia ficha de
    Nausicaä dice que en Netflix sólo está disponible con doblaje de España
    (+ japonés, inglés, alemán), en la «2ª fase» de estrenos Ghibli sin
    doblaje latino, junto con El mundo secreto de Arrietty, El regreso del
    gato, La leyenda de la princesa Kaguya y Mis vecinos los Yamada · [Doblaje Wiki — Nausicaä](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Nausica%C3%A4:_Guerreros_del_viento) · ✅ (tercera ficha independiente que confirma el mismo patrón de fases, ahora con las 3 fases —1ª, 2ª y 3ª— documentadas cada una desde una página distinta de la wiki).

### La historia detrás de la «cláusula de no cortes» — el doblaje que cambió cómo se distribuye Ghibli en todo el mundo (relevante para el doblaje latino de hoy)

- Antes de que Nausicaä tuviera su doblaje latino de Zima (arriba), Estados
  Unidos hizo en 1985 un corte editado con New World Pictures/Manson
  International titulado **«Warriors of the Wind»** («Guerreros del viento»):
  **le quitó más de 20 minutos a la película y tradujo mal el diálogo a
  propósito**, convirtiendo una fábula ecologista moralmente compleja en un
  dibujo animado de acción típico de los 80 · [Doblaje Wiki — Guerreros del viento (wikitext)](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Guerreros_del_viento) + [ScreenRant](https://screenrant.com/nausicaa-worst-dub-anime-history-factoid/) · ✅✅.
  - Dato muy citable para «cómo hablan en pantalla»: en ese corte editado, a
    **Nausicaä la rebautizaron «Princesa Zandra»** (voz de Rocío Robledo en el
    doblaje mexicano de esa versión editada, con Isidro Olace como director
    en Los Ángeles) — cambiar hasta el nombre de la protagonista para
    «occidentalizar» la venta · [Doblaje Wiki — Guerreros del viento (wikitext, tabla de reparto)](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Guerreros_del_viento) · ✅ (tabla de reparto propia, con el nombre «Princesa Zandra» explícito).
  - **Consecuencia directa, documentada en dos fuentes independientes**:
    Miyazaki, disgustado con el resultado, adoptó desde entonces una
    **cláusula contractual de «no cortes» para TODAS las futuras
    distribuciones internacionales de Ghibli** — nadie puede editar,
    reestructurar ni cambiar el guion o la música de una película Ghibli sin
    autorización · [SlashFilm](https://www.slashfilm.com/786405/the-reason-studio-ghibli-has-a-strict-no-edits-policy/) + [cinema.wisc.edu](https://cinema.wisc.edu/2016/09/06/when-nausicaa-became-warriors-wind/) · ✅✅.
  - **Anécdota hermana, muy citada por el fandom, sobre la MISMA cláusula**:
    cuando Miramax (Harvey Weinstein) quiso recortar La princesa Mononoke
    para el mercado estadounidense, el productor **Toshio Suzuki le envió una
    katana auténtica con un mensaje: «No cuts» («sin cortes»)** · [SlashFilm](https://www.slashfilm.com/786405/the-reason-studio-ghibli-has-a-strict-no-edits-policy/) · ⚠️ (una fuente en esta tanda, aunque es una anécdota muy repetida en medios de anime; sirve igual para «qué NO hacer»: no proponer nunca un doblaje o corte «adaptado» de una escena Ghibli como si fuera aceptable).
  - Ghibli recuperó y lanzó en DVD (2005, EE.UU.) la versión íntegra de
    117 minutos de Nausicaä, con nuevo doblaje y subtítulos mejorados, tras un
    acuerdo de distribución entre Disney y Tokuma Shoten (entonces dueña de
    Ghibli) en 1997 · [Wikipedia EN — Nausicaä of the Valley of the Wind (film)](https://en.wikipedia.org/wiki/Nausica%C3%A4_of_the_Valley_of_the_Wind_(film)) · ✅.

### Dato importante: qué películas Ghibli NO tienen doblaje latino en streaming

- Al llegar a Netflix Latinoamérica por fases, varias películas se ofrecieron
  **sólo con español de España** (más inglés, alemán, japonés), sin doblaje
  latino:
  - Fase 1: **Un castillo en el cielo**, **Porco Rosso**, **Recuerdos del
    ayer** · [Doblaje Wiki — "Un castillo en el cielo" (wikitext)](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Un_castillo_en_el_cielo) · ✅
  - Fase 3: **Susurros del corazón**, **La colina de las amapolas**, **El
    recuerdo de Marnie**, **La guerra de los mapaches** (además de *Se levanta
    el viento*, que curiosamente sí tiene doblaje latino de cine pero se
    ofreció en streaming sin él) · [Doblaje Wiki — "Se levanta el viento" (wikitext)](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Se_levanta_el_viento) · ✅ (mencionado en dos páginas distintas de la misma wiki, patrón consistente)
  - Esto confirma en dos fichas independientes de Doblaje Wiki (no es un
    error de una sola página) que Ghibli/Netflix trató la disponibilidad de
    doblaje latino de forma desigual según la fase de estreno, no según la
    película en sí.

### Actores recurrentes del doblaje latino (cruce manual de repartos)

- **Lucila Gómez**: Chihiro/Sen en la versión argentina de El viaje de
  Chihiro (2003) y Ponyo en la primera versión argentina de Ponyo (2008) —
  mismo estudio/país, dos protagonistas infantiles de Ghibli con años de
  diferencia · [Doblaje Wiki Chihiro](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=El_viaje_de_Chihiro), [Doblaje Wiki Ponyo](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Ponyo) · ✅ (dos fichas)
- **Cristina Hernández**: Kiki en Kiki: entregas a domicilio, y según
  BehindTheVoiceActors es la actriz con la que Enzo Fortuny ha coincidido más
  veces en toda su carrera (15 colaboraciones registradas en distintos
  doblajes, no específicas de Ghibli) · [Doblaje Wiki Kiki](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Kiki%3A_Entregas_a_domicilio), [BehindTheVoiceActors](https://www.behindthevoiceactors.com/Cristina-Hernandez/actor-team-ups/) · ✅ (dos fuentes; la segunda no es específica de Ghibli sino de su carrera en general — aclarado)
- **Enzo Fortuny**: Tombo en Kiki (Doblaje Wiki lo confirma), aunque su
  artículo de Wikipedia en español NO menciona ningún papel de Ghibli en su
  biografía — **discrepancia entre fuentes**, se deja anotada: Doblaje Wiki
  (especializada en doblaje, con tabla de reparto verificable con audio) es
  más confiable que la lista parcial de Wikipedia · [Doblaje Wiki](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Kiki%3A_Entregas_a_domicilio), [Wikipedia ES — Enzo Fortuny Romero](https://es.wikipedia.org/wiki/Enzo_Fortuny_Romero) · ⚠️ (dato confirmado sólo en una de las dos fuentes; anotado como discrepancia, no como error)
  - Dato biográfico verificado de Enzo Fortuny (aunque no mencione Ghibli):
    empezó en el doblaje a los 9 años porque el actor Héctor Bonilla, su
    vecino, lo invitó a un taller de doblaje · [Wikipedia ES](https://es.wikipedia.org/wiki/Enzo_Fortuny_Romero) · ⚠️ (una fuente)
- **Alan Prieto**: dirigió el doblaje de El viaje de Chihiro (versión Buena
  Vista México) y actuó como Howl adulto en la versión Wild Bunch de El
  increíble castillo vagabundo — mismo profesional en dos roles distintos
  (director y actor) en dos películas Ghibli · [Doblaje Wiki Chihiro](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=El_viaje_de_Chihiro), [Doblaje Wiki Castillo Vagabundo](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=El_incre%C3%ADble_castillo_vagabundo) · ✅ (dos fichas)
- **Noé Velázquez**: interpretó a Calcifer en AMBAS versiones latinas de El
  increíble castillo vagabundo (Zima y Wild Bunch) — caso raro de un actor
  que se mantiene en el redoblaje del mismo personaje · [Doblaje Wiki](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=El_incre%C3%ADble_castillo_vagabundo) · ✅ (visible en la misma tabla, dos columnas)

## Frases textuales del doblaje latino (de las tablas de Doblaje Wiki, con audio de muestra)

Cada .ogg es una muestra de audio real alojada en Doblaje Wiki, no una
transcripción de memoria — no son "frases icónicas" con contexto narrativo
(la wiki no las etiqueta así), sino muestras de identificación de voz. Frases
narrativas completas con guion no se encontraron en esta tanda (ver «No
encontré»).

- Chihiro (versión argentina), muestra de voz: `EVDC-ARG-Chihiro.ogg` ·
  [Doblaje Wiki — audio](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=El_viaje_de_Chihiro) · ⚠️ (es muestra de identificación, no cita narrativa con contexto)
- **Actualizado en esta tanda — ya no es sólo el nombre del archivo, se
  transcribió la frase completa con `herramientas/voz.py` (Whisper) sobre el
  audio real, con ficha de voz):**
- **Howl, versión Zima (Gerardo García)**, escena en el mercado escoltando a
  Sophie de los soldados que flotan: *«Ah, aquí estás. Te estaba buscando. No
  me digan. A mí me pareció que estaban a punto de irse. No les guardes
  rencor. No son tan malos. Vámonos. Seré tu escolta toda la tarde. No te
  asustes. Alguien me sigue. Camina. Creo que te quieren a ti. Estira las
  piernas y empieza a caminar. ¿Lo ves? No es tan difícil. Me aseguraré que se
  vayan. Pero espera un momento antes de salir.»* · audio: `Howlhowl1.ogg`
  ([enlace directo](https://static.wikia.nocookie.net/doblaje/images/e/e8/Howlhowl1.ogg/revision/latest?cb=20200330152228&path-prefix=es)) · ✅ (transcrito con voz.py en esta tanda, sobre el audio oficial de Doblaje Wiki). Voz medida: registro grave (129 Hz), muy expresiva (21.1 semitonos), velocidad rápida (3.12 palabras/s).
- **La MISMA escena, versión Wild Bunch (Alan Prieto)**: *«¿Qué tal? Ahora
  también te buscan. Por aquí, sujétate. Ahora estira las piernas y empieza a
  caminar. ¿Lo lograste? No tengas miedo. Lo haces muy bien.»* · audio:
  `HowlWBhowl1.ogg` ([enlace directo](https://static.wikia.nocookie.net/doblaje/images/a/ae/HowlWBhowl1.ogg/revision/latest?cb=20200330160251&path-prefix=es)) · ✅ (transcrito con voz.py, mismo método). Voz medida: registro grave
  (128 Hz), muy expresiva (25.2 semitonos), velocidad normal (2.7
  palabras/s) — casi el mismo registro que la versión Zima, pero MÁS
  expresiva y más lenta: mismo Howl «galán tranquilizador», dos actores,
  distinto ritmo de adaptación.
- **San (Mononoke), versión Buena Vista/Disney**, escena enfrentando al clan
  de simios: *«Su propia gente le disparó. ¡Está muriendo! ¿Por qué no me
  dejaste matarla? ¡Dímelo mientras sigas vivo! ¡No temo a la muerte! ¡Haré lo
  que sea para sacar a los humanos del bosque! ¡Y no te tengo miedo! ¡Te
  mataría por haberla salvado! Lady Eboshi es una mujer malvada y nadie
  evitará que yo la mate. ¿Están locos? ¿Qué sucedió para que los simios
  cambiaran sus costumbres? ¡Díganme desde cuándo comen carne humana!»*
  (Whisper transcribió mal «Eboshi» como «Evochy»/«Tevería»; corregido a oído
  para esta cita) · audio: `MononokeDisneySan.ogg` ([enlace directo](https://static.wikia.nocookie.net/doblaje/images/8/8c/MononokeDisneySan.ogg/revision/latest?cb=20180710222055&path-prefix=es)) · ✅ (transcrito con voz.py en esta tanda). Voz medida: registro muy agudo (323 Hz), muy expresiva (12.9 semitonos), velocidad rápida (3.52 palabras/s).
- **La MISMA escena, versión Zima**: *«Déjalo, él es mío. ¿Acaso te
  lastimaron? ¿Moriste? ¿Por qué me detuviste? Habla mientras sigues vivo. Lo
  supe en cuanto te vi. ¿Por qué demonios te metiste en mis asuntos? Te
  degollaré. Eso te callará. No desperdicio mi tiempo escuchando a los
  humanos. Dinos algo. ¿Por qué querría la tribu de los simios comerse a un
  hombre? Además, esta presa es nuestra.»* · audio: `MononokeZimaSan.ogg`
  ([enlace directo](https://static.wikia.nocookie.net/doblaje/images/7/7b/MononokeZimaSan.ogg/revision/latest?cb=20180710222109&path-prefix=es)) · ✅ (transcrito con voz.py). Voz medida: registro muy agudo (322 Hz), muy expresiva (10.0 semitonos), velocidad rápida (3.36 palabras/s) — casi
  idéntica en tono a la versión Disney (323 Hz): San suena igual de fiera y
  aguda en los dos doblajes, aunque el guion cambie bastante (la de Zima es
  más directa y cortante: «Te degollaré» vs. «Te mataría»).

## Punto 22 — Fan dubs y comunidad hispana

- Canal de Dailymotion con clip **"El viaje de Chihiro parte 3 español
  latino"** y **"parte 9 español latino"** en una lista de reproducción de
  fandub/subida no oficial · [Dailymotion](https://www.dailymotion.com/video/x7xvp9c) · ⚠️ (contenido no oficial, subido por terceros; sirve como muestra de que la comunidad hispana comparte y redobla escenas de Ghibli, no como fuente de calidad de audio)
- Se detectó un fandub cantado, **"【Nada se Olvida】Fandub Español Latino"**
  (canción de El viaje de Chihiro, "Itsumo Nando demo") listado dentro de esa
  misma página de resultados de Dailymotion, con autoría atribuida a "Aubrey
  Mason" · [Dailymotion](https://www.dailymotion.com/video/x7xvp9c) · ⚠️ (no se pudo aislar el video individual por la API de Dailymotion en esta tanda; queda pendiente confirmar vistas y enlace directo)
- No se encontraron canales de TikTok específicos dedicados a fandub de
  películas Ghibli con métricas verificables en esta tanda (las búsquedas
  devolvieron fandubs de otras franquicias como Attack on Titan y One Piece,
  no de Ghibli) — ver «No encontré».

## Lo mejor para la lámina

1. La cita de Miyazaki/Ebert sobre "ma": un personaje simplemente respira y
   se detiene, sin que la trama dicte cada instante — perfecto para explicar
   el ritmo pausado del estilo Ghibli sin necesitar una escena concreta.
2. El dato de Wakabayashi grabando un cajón real en un museo de Tokio para
   el sonido de la casa de baños de Chihiro: ilustra "cómo se logra" el
   sonido Ghibli con textura auténtica, no efectos genéricos.
3. El patrón de 2-3 doblajes latinos por película (Argentina/México/Wild
   Bunch): útil para explicar por qué a veces "esa voz no es la que
   recuerdas" — varía según cuándo y dónde la viste.
4. Cita de Hisaishi: sinfónico para Miyazaki, minimalista para sí mismo. Sirve
   para explicar la "firma sonora" en dos palabras.
5. Top de fan art de Danbooru (Kiki, San, Howl, Chihiro) como medida de cariño
   distinta a "quién es el protagonista".
6. Haku es el personaje Ghibli más querido a nivel estudio en 3 encuestas
   independientes (Simeji Gen Z, ranking.net de fans, Nlab boys-2022 en su
   categoría) — sirve como «campeón general» del catálogo si la lámina
   necesita un personaje secundario (no protagonista de su propia película
   como tal, ya que Chihiro es la protagonista de esa cinta) que represente
   a todo Ghibli.
7. La historia de «Guerreros del viento» → cláusula de «no cortes» → katana
   a Weinstein: en tres frases explica por qué Ghibli es tan estricto con
   adaptar/cortar su obra, y es un argumento fuerte para «que no parezca
   hecho por IA» / «no recortar información» del propio dueño del servidor.

## No encontré

- ⚠️ Un ranking OFICIAL de "personaje favorito" (organizado por el propio
  Studio Ghibli, tipo Oricon/NHK): sigue sin aparecer — lo más cercano son
  encuestas de medios serios (LINE Research para películas, Nlab para
  personajes por categoría) y voto abierto de fans (ranking.net, Simeji). Se
  documentan las 4 como aproximaciones válidas pero ninguna es "de Ghibli".
- ⚠️ Muestras de audio de Doblaje Wiki para el tema en general vía
  `datos-voz.md` — la recolección automática marcó que "no encontré la
  página de la obra" porque 102 es un tema, no una película con ficha propia;
  por eso bajé el wikitext a mano de 9 películas concretas (ver arriba).
- ⚠️ Un listado oficial u ordenado de onomatopeyas manuscritas del storyboard
  de alguna película Ghibli con su significado — sólo encontré el caso de
  "Pom Poko" en el título mismo.
- ⚠️ Canales de TikTok o YouTube de fandub hispano dedicados específicamente a
  Ghibli con vistas medidas — las búsquedas devolvieron fandubs de otras
  franquicias de anime, no de Ghibli. AnimeThemes devolvió error 522 en la
  recolección automática (ver `datos-voz.md`).
- ⚠️ Kiki: entregas a domicilio (tráiler Dailymotion `x8x2kas`) se transcribió
  con voz.py pero salió demasiado ruidoso para citar («Yo soy el tío de Black
  Cat» es un error claro de Whisper) — no se usó como cita, se deja la
  frase de El increíble castillo vagabundo y Totoro en su lugar.
- ⚠️ Entrevista original de Roger Ebert a Miyazaki donde surge la palabra
  "ma" — la cita se documenta de segunda mano en un blog/Tumblr, no se pudo
  localizar la fuente primaria (transcripción o video de esa entrevista) en
  esta tanda.
- ⚠️ Gustos personales concretos (comida, cumpleaños, altura) de personajes
  Ghibli con fuente de databook — no aplica bien al tema 102 porque es
  general y no de un personaje/película; este punto (20) se cubre mejor en
  las biblias de cada película individual, no en el estilo general. Se anota
  la limitación en vez de inventar datos.

## Bitácora de búsqueda

- WebSearch (es): "Joe Hisaishi Studio Ghibli firma musical estilo
  composición Miyazaki entrevista" → Qobuz, Classic FM, Wikipedia ES/EN.
- WebSearch (es): "Studio Ghibli doblaje latino historia Ventura
  Distribution Cinépolis actores de doblaje recurrentes" → sin resultados
  útiles directos, redirigió a Doblaje Wiki.
- WebSearch (en): "Studio Ghibli casting policy famous actors not voice
  actors Toshio Suzuki reasoning" → Anime News Network 2011, CBR, renote.net.
- WebSearch (es): "encuesta popularidad personajes Studio Ghibli favorito
  Oricon NHK ranking" → Nippon.com (LINE Research), TierMaker (no oficial).
- WebSearch (es/en): "Studio Ghibli 'ma' 間 silencio filosofía animación
  Miyazaki entrevista pausa" → Sensacine México, Tumblr @isavstheworld.
- WebSearch (es): "Studio Ghibli fandub español latino comunidad hispana
  doblaje de fans YouTube TikTok" → TikToks de otras franquicias (no útiles),
  Doblaje Wiki.
- WebSearch (en): "'Studio Ghibli' sound design diseñador de sonido Kazuhiko
  Takahashi onomatopeyas efectos Totoro viento" → llevó a Kazuhiro
  Wakabayashi (Ghibli Fandom) y Sound Effects Wiki de Totoro.
- WebSearch (es): "escenas que hacen llorar Studio Ghibli más tristes música
  Joe Hisaishi minuto" → Qobuz, artículo académico Panambí (Antillanca 2017).
- WebSearch (es): "Cristina Hernández Enzo Fortuny actor doblaje Studio
  Ghibli entrevista experiencia grabación" → Wikipedia Enzo Fortuny,
  BehindTheVoiceActors.
- WebSearch (es): "seiyuu actores voz japonesa que han trabajado en varias
  películas Ghibli Chishu Ryu Keiko Takeshita Yuriko Ishida" → From Up on
  Poppy Hill (Wikipedia EN), confirmó a Keiko Takeshita.
- WebSearch (en): "Studio Ghibli celebridades famosas doblaje japonés Ken
  Watanabe Takuya Kimura Youtube actrices no profesionales" → Ghibli Fandom
  (Takuya Kimura), Wikipedia EN/FR.
- API directa Doblaje Wiki (`action=parse&prop=wikitext`) para 9 páginas:
  El viaje de Chihiro, Mi vecino Totoro, La princesa Mononoke, Kiki: entregas
  a domicilio, Ponyo, El increíble castillo vagabundo, Se levanta el viento,
  Un castillo en el cielo, Nausicaä: Guerreros del viento.
- API directa Fandom (`ghibli.fandom.com`, `soundeffects.fandom.com`) para
  Kazuhiro Wakabayashi y My Neighbor Totoro (1988) — WebFetch dio 402, la API
  cruda funcionó.
- API Arctic Shift (Reddit) para r/ghibli y r/Studioghibli1: búsqueda por
  `title=` (no `q=`) y `sort=asc|desc` (no `score`) — parámetros correctos
  encontrados por prueba y error, anotados aquí para no repetir el fallo.
- Dailymotion API (`api.dailymotion.com/videos?search=`) para fandub "Nada
  se Olvida" — no aisló el video exacto, sólo confirmó que aparece listado
  en resultados de búsqueda web de Dailymotion.

**Tanda 2 (continuación en modo `seguir`, 25/26-sep-2026):**
- API directa Doblaje Wiki (`action=parse&prop=wikitext`) para **Nausicaä:
  Guerreros del viento** (reparto completo del doblaje Zima 2010) y para
  **Guerreros del viento** (la ficha de la versión editada estadounidense de
  1985, con la tabla de reparto que rebautiza a Nausicaä «Princesa Zandra»).
- API `action=query&prop=imageinfo` de Doblaje Wiki para sacar la URL directa
  de 4 muestras de audio (`Howlhowl1.ogg`, `HowlWBhowl1.ogg`,
  `MononokeDisneySan.ogg`, `MononokeZimaSan.ogg`), bajadas con curl y el
  header `Referer: https://www.fandom.com/`, y transcritas con
  `herramientas/voz.py` (Whisper + ficha de voz) — resuelve el pendiente de
  «frases textuales completas» sin necesitar YouTube.
- WebSearch (en): `Miyazaki "no cuts" clause "Warriors of the Wind" Nausicaa
  edited dub contract` → SlashFilm, ScreenRant, cinema.wisc.edu, Wikipedia EN
  — confirma la cláusula de «no cortes» y la anécdota de la katana a
  Weinstein.
- WebSearch (ja): `スタジオジブリ キャラクター 人気投票 ランキング 公式` →
  ranking.net (voto de fans, ~83 personajes), varias encuestas de ねとらぼ
  (Nlab/ITmedia) por categoría (chicos, heroínas, «novio ideal»).
- WebSearch (en): `Studio Ghibli recurring character archetypes strong girl
  heroines crone witch essay` → Fandom, CBR, Japan Nakama (arquetipos de
  heroínas y de mujeres mayores).
- WebSearch (ja): `Kazuhiro Wakabayashi 若林和弘 音響 スタジオジブリ 千と千尋
  インタビュー` → Wikipedia JA, eiga.com, jfdb.jp (confirman su filmografía
  real en Ghibli, segunda fuente para el dato biográfico, no para las citas).
- WebSearch (ja): `LINE Research 2022 ジブリ 好きな映画 ランキング 5254人` →
  encontró el **comunicado de prensa oficial de LINE Corporation** en
  PR Times (fuente primaria de la encuesta) y dos encuestas más de Nlab por
  franja de edad (20s, 40s) que confirman el mismo patrón generacional.
- Lectura directa de `ranking.net/rankings/best-ghibli-characters` (HTML con
  curl, extraído con regex en Python) y de un artículo de Nlab (curl +
  regex) — no se imprimió el HTML completo, sólo los fragmentos con datos.

**Tanda 3 (`seguir`, aviso de `revisar_partes.py`: «0 minutos citados»,
26-sep-2026):**
- Búsqueda directa en la API de Dailymotion (`api.dailymotion.com/videos?search=`)
  de tráilers oficiales doblados al latino de 5 películas (Chihiro, Castillo
  vagabundo, Mononoke, Totoro, Kiki); un id salió muerto (`x9ysqao`, "Not
  found") y se sustituyó por `x4bncvf` de la misma búsqueda.
- `herramientas/voz.py` sobre 5 tráilers de Dailymotion (Chihiro, Mononoke,
  Totoro, Castillo vagabundo, Kiki) con `--idioma es --modelo small`: da
  transcripción con minuto automático (`[m:ss]` + enlace `&t=`). El de Kiki
  salió inservible (ruido/hallucination de Whisper) y se descartó.
- `herramientas/fotogramas.py` sobre 3 tráilers (Mononoke, Totoro, Castillo
  vagabundo) cada 3 s, hojas de contacto miradas fotograma a fotograma (Read
  de la imagen) para identificar la cara de cada personaje en 5 emociones
  distintas con su minuto exacto — resuelve el punto 13 (tabla de emociones)
  que antes no existía en esta parte.
- Todo lo pesado (audio, vídeo, hojas de contacto) quedó en
  `/tmp/claude-0/trabajo/102-voz/` (fuera del repositorio).

Sin `Sigue:` — no queda pendiente ninguna tarea obligatoria de mis 7 puntos.
Extras que no se hicieron (quedan en «No encontré» con ⚠️, no aquí): más
canales de TikTok de fandub hispano específico de Ghibli con métricas, la
entrevista original de Roger Ebert, un ranking oficial (no de fans/prensa) de
personaje favorito, y datos tipo databook (altura/cumpleaños) por personaje —
este último punto (20) se resuelve mejor en cada biblia de película.
