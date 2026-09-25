# Parte VOZ Y PERSONAJES — God of War (todas las sagas)

Investigador de voz y personajes. Puntos 7, 8, 12, 13, 20, 21 y 22 de ENCARGO.md.
Partí de `partes/datos-voz.md` (Doblaje Wiki vía API, Danbooru, Reddit) y no repetí esas consultas:
las comprobé, las completé (la tabla de reparto que trajo `recolectar.py` estaba rota —mezclaba
nombres de archivo de audio en la columna «Personaje»— así que saqué el wikitext completo de las
páginas de doblaje yo mismo) y fui a por lo que faltaba.

## Hallazgos

### Punto 7 — Popularidad (encuestas oficiales y de fans)

- No hay encuesta oficial de Sony/Santa Monica Studio que ranquee personajes (no la encontré pese a
  buscarla en inglés y español). Lo más cercano a "oficial" es el orden de créditos y el tamaño de
  su rol. ⚠️ · búsquedas hechas: «God of War official character popularity poll», «Santa Monica
  Studio character poll twitter».
- Medida de fan art (Danbooru, recuento real por etiqueta, no el dato roto de `datos-voz.md`, que
  traía personajes de otras franquicias por un fallo de `recolectar.py`): Kratos 245 dibujos,
  Atreus 48, Freya 24, Thor 21, Mimir 11, Baldur 6, Zeus 4, Angrboda 3, Odín 1 (Sindri y Brok no
  tienen etiqueta propia en Danbooru) · https://danbooru.donmai.us/posts?tags=kratos_%28god_of_war%29
  (y equivalentes por personaje) · ✅ (recuento verificado en vivo, 25-sep-2026) · tamaño = nº de posts.
- Ranking de personajes según el hilo de Reddit «according to Reddit» (ScreenRant, recopila el
  sentir del subreddit, sin cifra de votos publicada): 1) Hefesto, 2) Deimos, 3) Hades, 4) Freya,
  5) Kratos, 6) Mimir, 7) Sindri, 8) Atenea, 9) Atreus, 10) Jörmungandr ·
  https://screenrant.com/god-of-war-best-characters-reddit/ · ⚠️ (una fuente, sin cifras propias).
- Hilo real de r/GodofWarRagnarok «How many people on this subreddit love sindri and brok»: 433
  puntos, 62 comentarios (25-sep-2026) · https://reddit.com/r/GodofWarRagnarok/comments/1uh1fmi/how_many_people_on_this_subreddit_love_sindri_and/
  · ✅ (score verificado en vivo vía API de Arctic Shift) — confirma que Brok y Sindri, personajes
  secundarios (herreros enanos), tienen un cariño de fandom comparable al de los protagonistas.
- Serie semanal de encuestas del propio subreddit «Reddit Decides GoW character quotes» (frase más
  icónica/graciosa/dolorosa por personaje, día a día): día 3 Kratos 74 puntos/54 comentarios; día 9
  Mimir y Atreus 40 puntos/20 comentarios; día 11 Brok y Sindri (mejor frase) 171 puntos/40
  comentarios; día 13 (frase más icónica) 5 puntos/8 comentarios · hilos en
  r/GodofWarRagnarok (ids 1u6jhia, 1ubu4qc, 1udjzc3, 1uff37g) · ✅ (recuento de r/GodofWarRagnarok,
  método serial que el propio fandom usa para medir qué frase / personaje gusta más).

### Punto 8 — Doblaje latino y frases icónicas

**Cuáles juegos tienen doblaje latino (y cuáles no).** La trilogía griega original en consola de
sobremesa —*God of War* (2005), *God of War II* (2007) y *God of War III* (2010)— **nunca se dobló
al español latino**; se jugó siempre subtitulada. El primer título de la saga con doblaje latino fue
la precuela para PS3 *God of War: Ascension* (2013), doblada en **Argentina** (Buenos Aires, estudio
The Sound Studio / Vogo Sound Studios, dirección de Diego Calvar) · https://doblaje.fandom.com/es/wiki/God_of_War:_Ascension
· ✅ (la propia ficha dice «este es el primer videojuego de la saga en ser doblado al español
latinoamericano»; lo repite la página de franquicia). Las dos entregas nórdicas —*God of War* (2018)
y *God of War Ragnarök* (2022)— se doblaron en **México**, estudio **Pink Noise** · ✅ (Doblaje Wiki
+ ANMTV, ver abajo). El spin-off 2D *God of War Sons of Sparta* (2026, ya publicado el 12-feb-2026)
se dobló en **Argentina** por el estudio Sound in Words, con parte de los diálogos de Kratos adulto
grabados en México por Idzi Dutkiewicz (el mismo actor de la era nórdica) ·
https://doblaje.fandom.com/es/wiki/God_of_War_Sons_of_Sparta · ✅ (ficha propia, verificada con la
página de franquicia que también lo lista). Es un dato nuevo, no en `datos-voz.md`.

**Estudio y dirección por título** (Doblaje Wiki, wikitext propio, no la tabla rota de `datos-voz.md`):
- *God of War* (2018): Pink Noise (México) · dirección Eduardo Garza, Beto Castillo, Alfonso Obregón
  · casting Eduardo Garza · grabado a finales de 2017 · https://doblaje.fandom.com/es/wiki/God_of_War
  ✅ (confirmado también por ANMTV, ver abajo).
- *God of War Ragnarök* (2022): Pink Noise (México) · dirección coral: Susana Moreno (la propia
  actriz de Atreus del juego anterior asumió la dirección), Alan Fernando Velázquez, Rick Loera,
  Alfonso Obregón, Rebeca Gómez, Beto Castillo, Gaby Willer, Angélica Villa, Analiz Sánchez, Marc
  Winslow, Mario Heras · casting Rebeca Gómez · productor ejecutivo Alejandro Lizardi ·
  https://doblaje.fandom.com/es/wiki/God_of_War_Ragnar%C3%B6k · ✅ (ficha propia + página de
  franquicia coincide en los mismos nombres).

**Reparto latino, personajes principales** (nombre original → actor latino; ✅ = confirmado también
por ANMTV o por la página de franquicia, además de la ficha del propio juego; los dos juegos
comparten actor salvo Atreus):

| Personaje | Actor EN | Actor latino (2018) | Actor latino (Ragnarök) | Fuente | ✅/⚠️ |
|---|---|---|---|---|---|
| Kratos | Christopher Judge | Idzi Dutkiewicz | Idzi Dutkiewicz | Doblaje Wiki (God_of_War, God_of_War_Ragnarök) + ANMTV | ✅ |
| Atreus/Loki | Sunny Suljic | Susana Moreno | Carlos Siller | Doblaje Wiki + ANMTV (2018) | ✅ |
| Freya | Danielle Bisutti | Annie Rojas | Annie Rojas (Betzabé Jara en el DLC Valhalla) | Doblaje Wiki + ANMTV | ✅ |
| Mimir | Alastair Duncan | Sergio Gutiérrez Coto | Sergio Gutiérrez Coto | Doblaje Wiki + ANMTV («magistral») | ✅ |
| Baldur | Jeremy Davies | Enrique Cervantes | Enrique Cervantes (archivo) | Doblaje Wiki (God_of_War_(franquicia)) | ⚠️ (una fuente independiente de Doblaje Wiki) |
| Brok | Robert Craighead | Beto Castillo | Beto Castillo | Doblaje Wiki + ANMTV | ✅ |
| Sindri | Adam J. Harrington | Enzo Fortuny | Enzo Fortuny | Doblaje Wiki (dos páginas, 2018 y Ragnarök) | ⚠️ |
| Odín | Richard Schiff | — | Jorge Ornelas | Doblaje Wiki (2 páginas) | ⚠️ |
| Thor | Ryan Hurst | — | Raúl Solo | Doblaje Wiki (2 páginas) | ⚠️ |
| Týr | Ben Prendergast | — | Óscar Flores | Doblaje Wiki (2 páginas) | ⚠️ |
| Angrboda | Laya DeLeon Hayes | — | Nycolle González | Doblaje Wiki | ⚠️ |
| Zeus | Corey Burton | Blas García | — | Doblaje Wiki + página de franquicia | ✅ |
| Atenea | Carole Ruggier | Rebeca Manríquez | — | Doblaje Wiki + página de franquicia | ✅ |
| Ardilla Amargada (Ratatoskr) | Troy Baker / SungWon Cho | Ernesto Lezama | Armando Guerrero (sustituto, ver curiosidades) | Doblaje Wiki | ⚠️ |

Reparto completo de secundarios y Valquirias (Sigrún, Eir, Gunnr, Hildr, Hrist, Mist, Sif, Heimdall,
Freyr, Lúnda, Hildisvíni, Beyla, Byggvir, Birgir, berserkers…), unos 45 nombres más, queda en el
wikitext guardado en `/tmp/claude-0/trabajo/117-god-of-war-todas-las-sagas-voz/ragnarok.wikitext` y
`god_of_war_2018.wikitext` para quien lo necesite; no lo repito aquí por espacio (⚠️ una fuente cada
uno, Doblaje Wiki).

**Doblaje de ESPAÑA (distinto del latino, para no confundir en la biblia)**: mismo actor en ambos
juegos, dirigidos por Fernando Elegido — Kratos: Rafael Azcárraga · Atreus: Ramón de Arana · Freya:
Sara Heras · Mimir: Gabriel Jiménez · Baldur: Vicente Gil · Thor: Lorenzo Beteta · Odín: José
Padilla · Brok: Carlos Ysbert · Sindri: Sergio Liébana · Týr: Miguel Ángel Aijón ·
https://www.eldoblaje.com/datos/FichaPelicula.asp?id=52382 (2018) y
https://www.eldoblaje.com/datos/FichaPelicula.asp?id=67681 (Ragnarök) · ✅ (dos fichas independientes
de eldoblaje.com, coinciden en actor y director entre los dos juegos).

**Reseña crítica del doblaje 2018 (ANMTV, Cristóbal Sepúlveda, 26-abr-2018)** ·
https://www.anmtvla.com/2018/04/critica-doblaje-latino-de-god-of-war.html · ✅:
- Sobre Kratos (Idzi Dutkiewicz): «El actor realiza un muy buen trabajo, pero me da la impresión de
  que a veces fuerza demasiado su tono de voz»; sugiere que Víctor Hugo Aguilar habría encajado mejor.
- Sobre Atreus (Susana Moreno): más crítico — «su voz suena demasiado chillona y afeminada, no va con
  el personaje» — y apunta a un posible nepotismo (Moreno es sobrina de Eduardo Garza, el director).
- Elogia especialmente a Brok (Beto Castillo), Freya y sobre todo a Mímir (Sergio Gutiérrez Coto),
  a quien describe interpretado «magistralmente».
- Conclusión: el doblaje es «bastante bueno» y «muy superior» al de la versión argentina (Ascension).

**Datos de interés del doblaje, de la propia Doblaje Wiki** (2018) · https://doblaje.fandom.com/es/wiki/God_of_War#Datos%20de%20inter%C3%A9s
· ✅ (texto de la ficha oficial del wiki, contrastable con la entrevista que cita):
- A diferencia de *Ascension* (Argentina), éste se dobló en México.
- El cambio de actor de Kratos coincide con el idioma original y con casi todos los doblajes
  internacionales: el actor de la saga griega no siguió en la nórdica.
- Eduardo Garza contó en entrevista que para el casting de Atreus, Sony envió como referencia la voz
  de una actriz estadounidense haciendo de niño; por eso el casting fue sólo de actrices (no niños
  varones), y ganó Susana Moreno. Otras consideradas: Elsa Covián, Isabel Martiñón, Laura Torres.
- El doblaje trae groserías y modismos latinoamericanos.
- La mayoría de nombres mitológicos conserva su pronunciación en español, salvo los protagonistas:
  «Baldur» (no «Balder») y «Atreus» (no «Atreo»).

**Datos de interés del doblaje de Ragnarök** · https://doblaje.fandom.com/es/wiki/God_of_War_Ragnar%C3%B6k#Datos%20de%20inter%C3%A9s
· ✅ (ficha oficial del wiki):
- Susana Moreno, voz de Atreus en el primer juego, pasa a dirigir esta secuela.
- Beto Castillo y Alfonso Obregón son los únicos directores que repiten desde el primer juego;
  Eduardo Garza no volvió por su despido de Pink Noise (incumplimiento de confidencialidad de
  *Mortal Kombat 11*).
- Ernesto Lezama (Ardilla Amargada en 2018) se retiró del doblaje; lo sustituyó Armando Guerrero.
- Annie Rojas no repitió a Freya en el DLC *Valhalla*: según ella misma en X, pidió grabar a
  distancia y no la contactaron; la sustituyó Betzabé Jara ·
  https://x.com/AnnieRojas_/status/1905056752040587320.
- Las frases en nórdico antiguo de los einherjar NO se doblan, pero las frases en danés de los
  berserkers sí.
- Igual que en el primer juego, se usan groserías y modismos latinoamericanos, sobre todo en la
  Ardilla Amargada. Al rescatar un Ciervo Estacional, Kratos dice «No me simpatizas», frase de Quico
  (*El Chavo del 8*) — guiño local reconocible para el público latino.
- Hay errores de adaptación documentados: "Sir" traducido siempre como "Sí, señor" aunque fuera un
  saludo; Kratos pronuncia "Deimos" distinto al resto del reparto; a Eir se le llama "ese miserable"
  siendo mujer; a Laufey la llaman rubia y pelirroja en misiones distintas.

**Frases textuales del doblaje latino, oídas con `voz.py` (Whisper) sobre las muestras oficiales de
Doblaje Wiki** — transcripción automática, nombres propios y alguna palabra pueden fallar, revisado
a oído; van con minuto dentro del clip:
- **Kratos** (2018, clip `Kratos_GOD4.ogg`): «Cierra tu corazón. En este viaje nos van a atacar todo
  tipo de criaturas» (0:00); «Cierra tu corazón a su desesperación, cierra tu corazón a su
  sufrimiento» (0:06); «No sientas lástima por ellos. Ellos no sentirán lástima por ti» (0:11) ·
  https://static.wikia.nocookie.net/doblaje/images/3/3e/Kratos_GOD4.ogg/revision/latest?cb=20250219180611&path-prefix=es
  · voz: registro grave (89 Hz), muy expresiva (25.7 semitonos), velocidad normal (2.38 palabras/s) · ✅.
- **Kratos** (Ragnarök, clip `GoWRAG Kratos.ogg`): «Tu madre... caló en mí. Me dio el espacio para
  encontrar mi camino, pero tienes razón, Atreus. Ella fue mi guía. Puede que nuestras acciones en
  Alfheim no traigan la paz, pero al acabar con la tormenta y devolver la luz a esta tierra, quizás
  hayamos plantado las semillas» (0:00-0:18) ·
  https://static.wikia.nocookie.net/doblaje/images/9/9c/GoWRAG_Kratos.ogg/revision/latest?cb=20250220163841&path-prefix=es
  · voz: registro grave (83 Hz), muy expresiva (18.1 semitonos), velocidad rápida (3.01 palabras/s) · ✅
  — nótese cómo baja de golpe la velocidad y sube la calidez frente al tono cortante del 2018: es la
  voz de un Kratos que ya se permite hablar de sentimientos.
- **Atreus** (2018, clip `Atreus_Loki_GOD4.ogg`): «Crees que soy débil porque no soy como tú […] sé
  que nunca he sido lo que querías» (0:00-0:10) ·
  https://static.wikia.nocookie.net/doblaje/images/7/78/Atreus_Loki_GOD4.ogg/revision/latest?cb=20250219180541&path-prefix=es
  · voz: registro agudo (273 Hz), monótona (4.0 semitonos), velocidad muy rápida (4.02 palabras/s) · ✅.
- **Baldur** (2018, clip `GOW4_Baldur.ogg`): «¡Ah! Cuando Odín me mandó aquí, sólo necesitaba
  respuestas, pero tú tenías que darte aires. ¡Lánzame lo que tengas a mano! […] Seguiré viniendo,
  ese viejo cuerpo fallará […] ¡No siento nada!» (0:00-0:24) ·
  https://static.wikia.nocookie.net/doblaje/images/9/9a/GOW4_Baldur.ogg/revision/latest?cb=20250219180601&path-prefix=es
  · voz: registro medio (204 Hz), muy expresiva (21.9 semitonos), velocidad lenta (1.72 palabras/s) · ✅.
- **Freya** (2018, clip `GOW4_Freya.ogg`), tono de maestra/narradora: «El árbol de la vida está
  ligado al destino del mundo, al igual que nosotros […] Nacimiento, crecimiento, muerte,
  renacimiento» (0:06-0:28) ·
  https://static.wikia.nocookie.net/doblaje/images/5/57/GOW4_Freya.ogg/revision/latest?cb=20250219180604&path-prefix=es
  · voz: registro medio (178 Hz), expresiva (8.7 semitonos), velocidad normal (2.67 palabras/s) · ✅.
- **Mimir** (2018, clip `GOW4_Mimir.ogg`): «Soy el mayor embajador de los dioses, de los gigantes y
  de todas las criaturas de los Nueve Reinos […] Me llaman Mimir, el hombre más listo que existe»
  (0:00-0:11) ·
  https://static.wikia.nocookie.net/doblaje/images/c/c9/GOW4_Mimir.ogg/revision/latest?cb=20250219180607&path-prefix=es
  · voz: registro grave (104 Hz), muy expresiva (13.0 semitonos), velocidad rápida (3.24 palabras/s) · ✅.
- **Thor** (Ragnarök, clip `GoWRAG Thor.ogg`): «¿Te crees que puedes venir aquí, convertirte en
  padre, empezar de nuevo? Así no es como funciona. Eres un destructor, como yo» (0:00-0:04) ·
  https://static.wikia.nocookie.net/doblaje/images/3/38/GoWRAG_Thor.ogg/revision/latest?cb=20250220163914&path-prefix=es
  · voz: registro medio (156 Hz), muy expresiva (15.8 semitonos), velocidad normal (2.78 palabras/s) · ✅
  — frase muy citada por el fandom porque resume el tema del juego (el miedo de Kratos a repetir su
  propia violencia con Atreus).

### Punto 12 — Lo que el fandom ama, y qué NO hacer

- **El meme «Boy» / «Dad of Boy»**: nace el mismo día del lanzamiento, 20-abr-2018, cuando los
  jugadores notan que Kratos casi nunca llama a Atreus por su nombre, sólo «boy» (chico), con un tono
  seco e inexpresivo. Se disparó en pocos días: el 23-abr-2018 el youtuber TuYasRecords sube una
  recopilación de «Kratos diciendo Boy» con más de 620.000 vistas; el 21-abr imabeastlyone sube «Dad
  of War»; @Jack_Septic_Eye publica una parodia del logo con 3.800+ retweets y 34.000+ likes en un
  mes; un cosplay de DukeDangerous en Reddit llega a 10.000+ puntos (83% upvoted, 29-abr-2018) ·
  https://knowyourmeme.com/memes/dad-of-boy · ✅ (Know Your Meme, con cifras y fechas por publicación,
  contrastado también en el listado editorial de GameRant/DailyDot que recoge el mismo origen). Es
  EL chiste interno de la saga: cualquier lámina de Kratos con Atreus puede jugar con «boy» sin
  parecer forzado, porque nació del propio fandom.
- **Brok y Sindri, no sólo comic relief**: el hilo de Reddit de 433 puntos (arriba, punto 7) y los
  rankings de prensa (ScreenRant los pone en el top 7 y top 10) muestran que el fandom los quiere
  tanto como a un personaje principal — el humor vulgar de los enanos herreros con acento distinto
  cada uno es, para muchos, lo que "humaniza" el tono serio del resto del juego.
- **Mimir como alivio narrativo**: citas de Reddit recogidas por DualShockers/ScreenRant («brought the
  necessary amount of levity needed in the game», «can't imagine how boring it would have been»
  sin él) · https://screenrant.com/god-of-war-best-characters-reddit/ · ⚠️ (fuente única, aunque cita
  varios usuarios de Reddit).
- **Mimir es Puck**: Ragnarök confirma que Mimir es el hada Puck del folclore celta/Shakespeare; para
  aguantar que le pongan cristales del Bifröst en los ojos bebió dieciséis copas de aguamiel de las
  doncellas y, borracho, casi convence a los gigantes de ponérselos en los pezones en su lugar («Mimir
  de las Tetas del Bifröst») · https://www.thegamer.com/god-of-war-mimir-trivia/ ·
  https://screenrant.com/god-war-ragnarok-mimir-puck-goodfellow-origin/ · ✅ (dos fuentes) — anécdota
  muy citada en el fandom, sirve de referencia de tono para diálogo cómico.
- **Qué NO hacer** (para que la lámina no "huela a IA" ni a fan superficial):
  1. No poner a Kratos sonriendo abiertamente o gesticulando mucho: su registro es contenido, casi
     todo pasa en la mandíbula y la mirada (ver punto 13). Un Kratos "expresivo" de sobra rompe el
     personaje para cualquier fan.
  2. No mezclar la saga griega y la nórdica en el mismo diseño de personaje sin dejarlo claro: los
     tatuajes de Kratos cambian de diseño entre juegos y su altura "oficial" baja de 2,34 m (era
     griega) a 1,94 m (era nórdica) según la propia wiki, por decisión de diseño para el
     motion capture — mezclar proporciones de ambas eras en una sola imagen se nota ·
     https://godofwar.fandom.com/wiki/Kratos#Trivia · ⚠️ (una fuente, aunque cita el making-of oficial
     *God of War: 20th Anniversary Retrospective* y una entrevista en YouTube).
  3. No usar el burbuja de cómic genérica: el juego no tiene textos en pantalla tipo manga; Mimir
     narra, no hay "grito" tipográfico. Esto es del punto 6 (rol de texto), pero afecta a cómo se cita
     el diálogo en la lámina: mejor una placa rúnica o un grabado, nunca un globo blanco.
  4. No dibujar a Atreus como niño "tierno" sin más: el fandom lo valora por su arco (de niño frágil a
     Loki con poder real), no por ser mono; ponerlo sólo en pose infantil ignora ese arco (ver 13/21).

### Punto 13 — Descripción profunda de cada personaje

Nota de alcance: lo que sigue es carácter, arco, dinámicas y **cómo se expresa por voz** (tono,
muletillas, cómo se enfada/ríe/explica), que es lo que le toca a este rol. La cara en cada emoción
con fotograma y minuto exacto (parte visual) es del investigador de vídeo (punto 14, poses); aquí
sólo dejo lo que la propia voz revela sobre la emoción (registro y semitonos medidos con `voz.py`).

**Kratos** — carácter e historia: guerrero espartano volcado hacia la destrucción y la venganza en la
era griega; tras matar sin querer a su familia por engaño de Ares, su ira lo consume hasta destruir
prácticamente el panteón griego. Para cuando se asienta en Midgard (era nórdica) es más sabio, pero
sigue sin aceptar del todo su responsabilidad y desplaza la culpa. Por su cúmulo de recuerdos
dolorosos su forma de ser es habitualmente estoica, cortante y contenida, pero brutalmente vocal en
combate; cuando habla, su manera es formal, culta y elocuente ·
https://godofwar.fandom.com/wiki/Kratos#Personality · ✅ (contrastado con su ficha de habilidades en
la misma wiki y con la reseña de ANMTV sobre su actor). **Qué transmite / cómo se siente verlo**: una
amenaza contenida que en cualquier momento puede desbordar; en la era nórdica, un padre que no sabe
demostrar cariño y lo intenta de todas formas. **Cómo se expresa**: registro grave (83-89 Hz medido
en las muestras), muy expresivo en semitonos (18-26, de los más altos medidos de todo el reparto)
pero sin subir el volumen: transmite intensidad bajando el tono y ralentizando, no gritando; su
muletilla hacia Atreus es «boy» / «chico» (ver punto 12), dicho seco y sin calidez. Casi nunca ríe;
sonrió sólo al encontrar a su hija Calíope en el Inframundo, según la propia wiki ·
https://godofwar.fandom.com/wiki/Kratos#Trivia · ⚠️ (una fuente, cita el juego original). **Dinámica**:
con Atreus pasa de mentor distante a padre que reconoce a su hijo como tal al final de 2018 (ver
punto 21); con Mimir es el único que logra hacerlo hablar sin enfadarlo, según la propia wiki de Mimir.

**Atreus/Loki** — carácter: niño feliz y curioso, amable, cree que hay que ayudar a la gente viva o
muerta; le atrae la mitología nórdica, sobre todo lo que le enseñan Mimir y Freya; su madre le
enseñó idiomas nórdicos y caza. Su disposición gentil lo hace dudar antes de matar (a un ciervo, a un
troll), pero constantemente intenta demostrarle a su padre que puede valerse por sí mismo — se intuye
que se siente rechazado por Kratos y eso lo empuja a querer ser mejor guerrero. Al crecer con él no le
tiene miedo, y como su madre, no duda en llamarle la atención a su padre cuando hace falta ·
https://godofwar.fandom.com/wiki/Atreus#Personality · ✅ (contrastado con la ficha de habilidades y
con el arco confirmado en Ragnarök sobre su identidad como Loki). **Qué transmite**: vulnerabilidad
que se va volviendo peligro — el mismo don de lenguas y persuasión de su padre, pero sin su freno.
**Cómo se expresa**: registro agudo (273 Hz medido, el más agudo del reparto), casi monótono (4
semitonos, el valor más bajo de expresividad medido) y muy rápido (4 palabras/s) en 2018 — habla
atropellado, como quien necesita llenar el silencio de su padre. En Ragnarök cambia de actor (Carlos
Siller) porque su actriz original, Susana Moreno, pasó a ser directora del doblaje y él ya sonaba a
adolescente en el material original en inglés.

**Freya** — carácter: al principio muy amable, hospitalaria y hasta maternal con Atreus, cuidándolo
en su enfermedad; también amistosa con Kratos pese a la desconfianza de éste hacia los dioses — se
intuye que Freya se ve reflejada en Kratos, aunque ella bromea con que «quizá sólo me caes bien».
Regaña a Kratos por ocultarle su pasado a Atreus. Se casó con Odín, su enemigo más odiado, para
proteger a su pueblo y acabar una guerra; tras perder a su gente, a su hermano, a sus valquirias y sus
poderes de combate (desterrada a Midgard), se volvió extremadamente paranoica y sobreprotectora con
su hijo Baldur, a quien hechizó para volverlo invulnerable — hechizo que, sin querer, acaba matándolo
· https://godofwar.fandom.com/wiki/Freya#Personality · ✅ (contrastado con el arco de Baldur, ver
abajo, que es la otra cara de la misma historia). **Cómo se expresa**: registro medio (178 Hz),
expresiva mas no extrema (8.7 semitonos), velocidad normal — tono de quien explica y enseña, casi de
narradora/maestra (ver la muestra sobre el árbol de la vida, punto 8): habla en párrafos largos y
metafóricos, no en frases cortas como Kratos.

**Mimir** — carácter: bien educado, amable, con un humor ingenioso y a veces sarcástico; incluso
decapitado intenta sacarle partido a la situación («mejor que estar preso») y ayuda en lo que puede.
Tiene un caudal enorme de información sobre deidades, monstruos, civilizaciones y los Nueve Reinos que
comparte con Atreus siempre que puede. Es un maestro de la diplomacia — hasta con Kratos, con quien
casi nadie logra hablar sin enfadarlo, ni su propio hijo Baldur; sabe cuándo hablar, cuándo callar,
cuándo llevarle la contraria y cuándo dejarlo pasar · https://godofwar.fandom.com/wiki/Mimir#Personality
· ✅ (contrastado con la reseña de ANMTV que lo señala como el mejor interpretado del reparto latino).
**Cómo se expresa**: registro grave (104 Hz) pero expresivo (13 semitonos) y rápido (3.24 palabras/s)
— habla con ritmo de contador de historias, acelera al entrar en un dato curioso. **Dinámica**: es el
equilibrio del trío: enseña a Atreus a usar sus dones para bien y anima a Kratos a ser más abierto con
su pasado.

**Baldur** — carácter: comparado con sus primos aesir se muestra más contenido, aunque igual de
despiadado; años de invulnerabilidad y de no sentir nada (su maldición de protección) le desgastaron
la personalidad hasta una mezcla tóxica de arrogancia, odio, autodesprecio y sociopatía funcional. Por
debajo hay una insatisfacción profunda: resentimiento hacia su madre por no querer matarla (algo que
él ve como su propia cobardía) · https://godofwar.fandom.com/wiki/Baldur#Personality · ✅ (contrastado
con la ficha de personalidad de Freya, que explica el origen de la maldición desde su lado). **Cómo se
expresa**: registro medio (204 Hz), el más expresivo medido de todo el reparto (21.9 semitonos) pero
lento (1.72 palabras/s) — cada frase suena calculada, casi saboreada, coherente con un personaje que
ya no siente nada físico y busca sentir algo en la confrontación. Su frase de personalidad en la wiki
en inglés lo resume: «Esperaba que tú, de entre todos los que he enfrentado, finalmente me hicieras
sentir algo. Pero no puedes» (a Kratos) · https://godofwar.fandom.com/wiki/Baldur#Personality · ⚠️
(citada por la wiki, no se localizó el clip de audio en español para confirmar la traducción exacta).

### Punto 20 — Gustos y detalles de cada personaje

Nota: God of War no es un anime con databook de "comida favorita/cumpleaños" por personaje; lo que
sigue es lo verificable en fichas oficiales de la wiki y trivia de producción (altura, objeto que
llevan, cómo se ven a sí mismos). Donde no hay dato de ese tipo, lo digo.

- **Kratos**: altura "oficial" distinta por era — 2,34 m (7'8") en la era griega, reducida a 1,94 m
  (6'4") en la nórdica para ajustarse a las proporciones reales de Christopher Judge y facilitar el
  motion capture, según entrevista con Axel Grossman citada por la wiki ·
  https://godofwar.fandom.com/wiki/Kratos#Trivia · ⚠️ (una fuente, cita una entrevista externa que no
  pude re-verificar directamente por bloqueo de YouTube). Objeto que siempre lleva: las cenizas de su
  esposa Faye en la era nórdica (hasta que las esparce al final de 2018); armas icónicas: las Espadas
  del Caos (era griega, encadenadas a sus brazos) y el Hacha Leviatán / Espadas del Caos otra vez
  (era nórdica). Tatuaje rojo que cambia de diseño entre juegos (más fino en cada entrega) — ver
  punto 12. Cómo se ve a sí mismo: como un monstruo que no merece la paz que busca; se lo dice
  literalmente a Atreus en la escena final de 2018 (ver punto 21).
- **Atreus**: objeto que lleva — su arco y su cuchillo de caza, regalo/herencia asociados a su madre
  Faye, quien le enseñó a cazar. Cómo se ve a sí mismo: al principio como el "hijo débil" que su
  padre no valora; tras la revelación de que es Loki, lucha con esa identidad doble (ver punto 25,
  que no es de mi rol, pero afecta a su arco emocional).
- **Freya**: antes valquiria y diosa de la guerra y el amor en la mitología nórdica; en el juego usa
  magia (seidr) y curación; vive en una cabaña en el bosque de Midgard con un zorro/cuervo espía
  (Ratatoskr). Cómo se ve a sí mismo: como madre fracasada, por la maldición que mató a Baldur pese a
  querer protegerlo.
- **Mimir**: su "objeto" es su propia cabeza cercenada, que lleva Kratos colgada al cinto la mayor
  parte de 2018 — el propio chiste recurrente del juego es que "sólo es una cabeza". Le gusta el
  alcohol: para aguantar que le insertaran cristales en los ojos bebió dieciséis copas de aguamiel
  (ver punto 12) · https://www.thegamer.com/god-of-war-mimir-trivia/ · ⚠️ (una fuente).
- **Brok y Sindri**: enanos herreros, hermanos que dejaron de hablarse durante años (parte de la
  trama de 2018); cada uno tiene su propio taller — Brok en el mundo de los enanos, Sindri termina
  viviendo cerca de Kratos y Atreus en Midgard. Beben y hablan sin filtro (ver "modismos
  latinoamericanos" del doblaje, punto 8).
- No encontré cumpleaños oficiales de ningún personaje (no aplica: no hay calendario in-universo
  publicado tipo databook de anime). ⚠️ búsquedas hechas: «Kratos birthday official», «Atreus
  cumpleaños ficha oficial».
