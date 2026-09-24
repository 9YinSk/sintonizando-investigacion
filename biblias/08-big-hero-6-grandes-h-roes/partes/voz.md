# Voz y personajes · Big Hero 6 (Grandes Héroes) (08-big-hero-6-grandes-h-roes)

Investigador de voz y personajes. Puntos de `ENCARGO.md`: **7** (popularidad),
**8** (doblaje latino), **12** (fandom y qué no hacer), **13** (carácter y
forma de hablar) — repaso y confirmación en dos fuentes — y **20, 21, 22**
(gustos, por qué la aman, fan dubs), nuevos.

Parto de `partes/datos-voz.md` (Doblaje Wiki, texto de personalidad de la
wiki de Disney, Dailymotion) y de las secciones 2, 9, 10 y 14 de `biblia.md`
(ya escritas en la primera pasada, con red cerrada, sin vídeos mirados). No
repito lo que ya está ✅ ahí; confirmo lo ⚠️, corrijo lo que encontré mal (los
actores de Fred, GoGo y Wasabi **sí estaban** en Doblaje Wiki, la primera
pasada no los vio) y añado lo nuevo.

Trabajo pesado (wikitext, HTML y transcripciones de `voz.py`) en
`/tmp/claude-0/trabajo/08-voz/`.

---

## 1 · Doblaje latino: los que faltaban, y estudio/dirección en dos fuentes más (punto 8)

La primera pasada (red cerrada) dijo «Fred, GoGo, Wasabi: no lo encontré» y
dejó estudio/dirección con «sólo Doblaje Wiki». **Sí estaban**: el wikitext
completo de la página `Grandes_héroes` de Doblaje Wiki (tabla «Reparto») los
trae; sólo que la tabla de `recolectar.py` no capturó esas columnas porque el
wikitext usa `colspan` distinto por fila. Lo comprobé de nuevo pidiendo el
wikitext entero
(`https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Grandes_h%C3%A9roes`)
y además encontré **dos fuentes independientes más** que traen el reparto
completo con crédito de estudio y dirección: **The Dubbing Database** (wiki
hermana, en inglés, no es Fandom de doblaje) y **CHARGUIGOU / Disney
International Dubbings** (archivo de un aficionado con los créditos exactos
de Disney Character Voices International).

| Personaje | Voz latina | Confirmado en |
|---|---|---|
| Hiro Hamada | **Memo Aponte** (Guillermo Aponte Mille) | ✅ Doblaje Wiki, PRODU (entrevista), Radio Disney MX, [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) |
| Baymax | **Alan Prieto** | ✅ Doblaje Wiki, SoundCloud, TikTok SDV, dubdb, CHARGUIGOU |
| Tadashi Hamada | **Alexis Ortega** (1989-2026) | ✅ Doblaje Wiki, El Imparcial, El Informador, LatinUS, dubdb, CHARGUIGOU |
| **Fred Frederickson** | **Noé Velázquez Pedroza** | ✅ nuevo — Doblaje Wiki (wikitext, no la tabla resumida) + [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes) + [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) |
| **GoGo Tomago** | **Erika Ugalde** | ✅ nuevo — mismas tres fuentes |
| **Wasabi** | **Alan Bravo** | ✅ nuevo — mismas tres fuentes |
| Honey Lemon | **Génesis Rodríguez** (se autodobla) | ✅ Doblaje Wiki, dubdb (nota de «Trivia»: repitió su papel del inglés), CHARGUIGOU |
| Robert Callaghan / Yokai | **Humberto Vélez** | ✅ Doblaje Wiki, dubdb, CHARGUIGOU |
| Alistair Krei | **Idzi Dutkiewicz** | ✅ Doblaje Wiki, dubdb, CHARGUIGOU |
| **Tía Cass** | **Patricia Palestino** | ✅ ya no es «una fuente»: dubdb y CHARGUIGOU la confirman también |
| Abigail Callaghan | **Yadira Aedo** | ✅ Doblaje Wiki, dubdb, CHARGUIGOU |
| Padre de Fred | **Jesse Conde** | ✅ Doblaje Wiki, dubdb, CHARGUIGOU |
| Heathcliff (mayordomo de Krei) | **Arturo Mercado Chacón** | ✅ Doblaje Wiki, CHARGUIGOU (dubdb no lo lista) |
| Yama | Octavio Rojas | ✅ Doblaje Wiki, CHARGUIGOU |
| General | Paco Mauri | ✅ Doblaje Wiki, dubdb, CHARGUIGOU |
| Oficial Gerson | Germán Fabregat | ✅ Doblaje Wiki, CHARGUIGOU («Sargento») |
| Réferi | Gabriela Guzmán | ✅ Doblaje Wiki, CHARGUIGOU |
| Reportero | Agustín L. Lezama (López Lezama) | ✅ Doblaje Wiki, CHARGUIGOU |

- **Estudio y equipo, en dos fuentes más** (antes «sólo Doblaje Wiki, dos
  páginas»): **Taller Acústico, S.C.**, dirección **Ricardo Tejedo**,
  traducción Katya Ojeda Iturbide y el propio Tejedo, dirección de casting
  **Luis Daniel Ramírez**, gerencia de producción Erika Sánchez Santarelli,
  producción Yeri Casanova, edición **Diseño en Audio «DNA»**, mezcla
  **Shepperton International** (Reino Unido), ejecutivo creativo Raúl Aldana,
  versión en español producida por Disney Character Voices International ✅
  ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes),
  [dubdb, ficha de crew](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes),
  [CHARGUIGOU, lista de crew completa](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html)).
- **Voces adicionales** (elenco de relleno) listadas sólo por CHARGUIGOU, 33
  nombres: Adriana Casas Basilio, Ana Luisa Pérez Compeán, Berenice Vega,
  César Filio, César Garduza, Salvador «Chava» Reyes, Daniel Lacy, Diego
  Armando Ángeles Ramírez, Emmanuel Bernal, Erick Salinas, Erika Dubka
  Sánchez, Esteban Desco, Gabriela Guzmán, Gerardo Alonso, Gisella Ramírez,
  Gwendolyne Flores, Herman López, Jahel Morga Vera, Jesse Conde, José Luis
  Miranda B., Joss Waleska, Luis Navarro, Luna Arjona, Magda Tenorio, Mark
  Pokora, Marysol Cantú, Mauricio Pérez Castillo, Orlando Rivas, Pedro
  D'Aguillón Jr., Raúl Solo, Raymundo Armijo Ugalde, Ricardo Tejedo, Roberto
  Velázquez, Sofía Huerta, Valentina Souza, Yeri Insunza Casanova ⚠️ (una sola
  fuente; no sé qué papel exacto tuvo cada uno) ([CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html)).
- **No hay muestras de audio en la ficha de Doblaje Wiki** de esta película
  (comprobado en el wikitext: cero etiquetas `<sm2>`), así que las frases
  textuales con minuto de abajo salen de clips doblados reales, no de
  muestras sueltas.

## 2 · Frases del doblaje latino, textuales y con minuto (punto 8)

Como Doblaje Wiki no tiene muestras de audio para esta película, oí clips
**doblados reales** en Dailymotion con `herramientas/voz.py` (Whisper en
local). **Ojo: Whisper confunde nombres propios** (oye «Baymax» como
«Deimax», «Hiro» como «Giro/Max/Vocé») — lo dejo anotado en cada frase; el
resto de la frase se oye bien y coincide con lo que ya circulaba de memoria en
la biblia (o lo corrige).

### Tráiler oficial en español latino (Dailymotion, voz real de Alan Prieto y Memo Aponte)
_Fuente: [Dailymotion, «'Grandes Héroes' - Tráiler oficial en español latino»](https://www.dailymotion.com/video/x889whz), 2:31 · transcrito con `voz.py --idioma es`_

| Minuto | Frase (limpia de errores de Whisper) | Quién |
|---|---|---|
| [0:11](https://www.dailymotion.com/video/x889whz?t=11) | «Él es mi hermano mayor, Tadashi.» | Hiro ✅ |
| [0:18](https://www.dailymotion.com/video/x889whz?t=18) y [0:37](https://www.dailymotion.com/video/x889whz?t=37) | «Hola, yo soy Baymax.» | Baymax ✅ (Whisper oyó «Deimax») |
| [0:52](https://www.dailymotion.com/video/x889whz?t=52) | «Quiero ayudarte.» | Baymax ✅ |
| [0:59](https://www.dailymotion.com/video/x889whz?t=59) | «Estoy abrazando un... malvavisco.» (frase cortada en el tráiler) | Hiro ⚠️ (se pierde una palabra en el corte del tráiler) |
| [1:25](https://www.dailymotion.com/video/x889whz?t=85) | «¡Somos nerds!» | Fred ✅ |
| [1:37](https://www.dailymotion.com/video/x889whz?t=97) | «¿Por qué la ropa interior de fibra de carbono?» | GoGo o Wasabi ⚠️ (no distingo la voz con certeza en el tráiler) |
| [2:16](https://www.dailymotion.com/video/x889whz?t=136) | «¡Es solo una expresión!» | Wasabi ✅ (coincide con la frase de más abajo, oída también en otro clip) |

### Escena real de la película, doblada (Dailymotion, fragmento subido por un usuario)
_Fuente: [Dailymotion, «6 Grandes Héroes Español Latino Parte 2»](https://www.dailymotion.com/video/x2hry42), 3:59 · transcrito con `voz.py --idioma es`. Es la escena inicial (pelea robótica y regaño de la tía Cass) y la del «Nerd Lab» donde Hiro conoce a GoGo, Wasabi y Fred._

| Minuto | Frase | Quién |
|---|---|---|
| [0:00](https://www.dailymotion.com/video/x2hry42?t=0) | «Las peleas robóticas son ilegales. ¿Quieres que te arresten por esto?» | Tía Cass ✅ |
| [0:04](https://www.dailymotion.com/video/x2hry42?t=4)-[0:09](https://www.dailymotion.com/video/x2hry42?t=9) | «Las peleas robóticas no son ilegales. Apostar en peleas robóticas, eso es ilegal, pero lucrativo.» | Hiro ✅ — confirma de oído la frase que sólo se sabía de memoria (biblia, punto 20 de «lo no verificado») |
| [1:26](https://www.dailymotion.com/video/x2hry42?t=86) | «¿Hasta cuándo harás algo de valor con esa mente brillante?» | Tadashi ✅ |
| [1:37](https://www.dailymotion.com/video/x2hry42?t=97)-[1:40](https://www.dailymotion.com/video/x2hry42?t=100) | «¿Qué dirían mamá y papá ahora? No lo sé, ya no están. Tenía tres años cuando murieron.» | Tadashi e Hiro ✅ |
| [1:49](https://www.dailymotion.com/video/x2hry42?t=109) | «Quizá no evite que vayas, pero no voy a dejarte ir solo.» | Tadashi ✅ |
| [2:11](https://www.dailymotion.com/video/x2hry42?t=131) | «¡Qué lindo! Conoceré tu nerd lab.» | Hiro ✅ |
| [2:45](https://www.dailymotion.com/video/x2hry42?t=165) | «Bienvenida a la tierra de los nerds.» | Hiro ✅ |
| [3:29](https://www.dailymotion.com/video/x2hry42?t=209) | «Cada objeto tiene un lugar y un lugar cada objeto.» | Wasabi ✅ — su manía del orden, con frase textual |
| [3:34](https://www.dailymotion.com/video/x2hry42?t=214) | «¡La sociedad tiene reglas!» | Wasabi ✅ |

### Otra escena real, doblada (Dailymotion, «pain scale» y presentación de Krei)
_Fuente: [Dailymotion, «Big hero 6 pelicula completa en español latino Parte 1 part 2/2»](https://www.dailymotion.com/video/x5hvz3y), 4:23 · transcrito con `voz.py --idioma es`. Es la escena en que Baymax escanea a Hiro tras la pelea con Yama y la de la presentación del proyecto «Silent Sparrow» de Alistair Krei._

| Minuto | Frase | Quién |
|---|---|---|
| [0:39](https://www.dailymotion.com/video/x5hvz3y?t=39) | «Sólo es una expresión.» | Hiro ✅ (corrige/confirma la de la biblia) |
| [0:52](https://www.dailymotion.com/video/x5hvz3y?t=52) | «Tu estado emocional ha mejorado.» | Baymax ✅ (dato nuevo) |
| [0:55](https://www.dailymotion.com/video/x5hvz3y?t=55) | **«Puedo desactivarme si dices que estás satisfecho con tu cuidado.»** | Baymax ✅ — **corrige** la frase de audiofrases.com que traía la biblia («No pueden desactivarme hasta que digas...»): la versión real del doblaje es más corta y usa **«tu cuidado»**, no «mi cuidado» |
| [1:00](https://www.dailymotion.com/video/x5hvz3y?t=60) | «No, no quiero que te desactives.» | Hiro ✅ |
| [3:01](https://www.dailymotion.com/video/x5hvz3y?t=181) | «Fred, no me hagas callarte con mi láser.» | GoGo ✅ |
| [2:44](https://www.dailymotion.com/video/x5hvz3y?t=164) | «El líder Fred, los ángeles de Fred» (Fred se imagina jefe del equipo) | Fred/Hiro ✅ |
| [4:14](https://www.dailymotion.com/video/x5hvz3y?t=254) | «Amigos, les presento el proyecto Silent Sparrow.» | Alistair Krei ✅ |

**Con esto se cierran o corrigen varias ⚠️ que traía la biblia de la primera
pasada** (punto 10 de `biblia.md`): la frase de «satisfecho con tu cuidado» sí
tiene fuente textual con minuto y corrige la versión que circulaba; «Sólo es
una expresión» se confirma tal cual; y la manía de Wasabi («cada objeto tiene
un lugar») ahora tiene minuto propio. Sigue sin confirmarse de oído la frase
final «Estoy satisfecho con mi cuidado» de Hiro (no encontré ese tramo —el
clímax— doblado en Dailymotion ni Internet Archive): queda ✅ por dos fuentes
de texto (audiofrases, TikTok) pero ⚠️ de oído.

## 3 · Cómo se expresan: voz medida, no de oído (punto 13)

Medido con `herramientas/voz.py` sobre los mismos clips doblados de arriba
(registro en Hz, expresividad en semitonos, velocidad en palabras/segundo).
Sirve para que el redactor no describa las voces «de memoria»:

| Personaje | Clip · minuto | Registro | Expresividad | Velocidad | Lectura |
|---|---|---|---|---|---|
| **Baymax** | [x5hvz3y, 0:52-0:55](https://www.dailymotion.com/video/x5hvz3y?t=52) | medio, 150 Hz | 13,3 semitonos (la más baja medida) | normal, 2,42 pal/s | ✅ confirma «voz plana y suave»: es el personaje **menos expresivo** de los tres medidos, coherente con su carácter de robot educado y sin prisa |
| **Hiro** | [x2hry42, 0:04-0:11](https://www.dailymotion.com/video/x2hry42?t=4) | agudo, 268 Hz | 24,3 semitonos | normal, 2,45 pal/s | ✅ voz aguda de adolescente, bastante expresiva: encaja con el «listo, algo burlón» que ya decía la biblia (Memo Aponte, ya adulto, dobla con un timbre juvenil) |
| **Wasabi** | [x2hry42, 3:29-3:35](https://www.dailymotion.com/video/x2hry42?t=209) | medio, 186 Hz | 22,8 semitonos | **muy rápida, 4,1 pal/s** — la más rápida de las tres | ✅ nuevo: Wasabi habla atropellado cuando defiende su manía del orden, coherente con su lado ansioso |
| (la escena completa, con varias voces) | [x889whz, tráiler](https://www.dailymotion.com/video/x889whz) | medio, 164 Hz | 30,7 semitonos | normal, 2,74 pal/s | ⚠️ promedio de todo el tráiler (varias voces mezcladas), no de un solo personaje — sirve sólo como referencia general del tono del doblaje, muy expresivo de punta a punta |

- **Tadashi** (Alexis Ortega): en los clips oídos habla pausado y cálido con
  Hiro («¿Hasta cuándo harás algo de valor con esa mente brillante?», minuto
  1:26 de x2hry42) — tono de hermano mayor paciente, sin medir su registro
  aislado (se mezcla con la respuesta de Hiro en el mismo segundo).
- **GoGo** (Erika Ugalde): frase cortante «Fred, no me hagas callarte con mi
  láser» (minuto 3:01 de x5hvz3y), dicha rápido y seca — encaja con «la
  seria» que ya decía la biblia, aunque no se midió su registro por separado
  (se solapa con la réplica de Fred).
- Esto **confirma con oído real** lo que la biblia describía de memoria en el
  punto 9 (Baymax «voz plana y suave», Hiro «rápido, listo»): pasa de ⚠️ a ✅.

## 4 · Popularidad: números frescos, abiertos de verdad (punto 7)

La primera pasada citó la encuesta japonesa **みんなのランキング** («ranking.net»)
de memoria, «vista por el buscador, sin abrir la página» (quedó ⚠️). La abrí
entera hoy (24-sep-2026; la página se actualiza sola y dice
«última actualización: 2026/09/21»):

| Puesto | Personaje | Puntos | Evaluadores | Seiyū (JP) |
|---|---|---|---|---|
| 1.º | **Baymax** | 97,4 | 99 | 川島得愛 |
| 2.º | Hiro | 90,9 | 70 | 本城雄太郎 |
| 3.º | **GoGo** | 80,2 | 44 | 浅野真澄 |
| 4.º | Tadashi | 79,5 | 47 | 小泉孝太郎 |
| 5.º | **Mochi (el gato)** | 79,4 | 25 | — |

✅ (abierto directamente, no de resumen) [ranking.net](https://ranking.net/rankings/best-baymax-characters).
Los números cambiaron un poco frente a lo que decía la primera pasada
(97,9/86 votos para Baymax; ahora 97,4/99): es normal, la web sigue recibiendo
votos. **Confirma lo mismo que ya decía la biblia: Baymax gana con claridad**,
y añade un dato curioso para el punto 12 (fandom): **hasta el gato Mochi
queda mejor valorado que varios humanos** del reparto.

- La encuesta de Fanpop que ponía a Honey Lemon primero sigue siendo la
  opinión de un solo usuario, no una encuesta con votos ([Fanpop](https://www.fanpop.com/clubs/big-hero-6/articles/252355/title/review-big-hero-6-characters)):
  ⚠️ confirmado que sigue siendo así (no hay conteo de votos en esa página).
- No hay encuesta oficial de Disney por personajes: repetí la búsqueda
  («Big Hero 6 official character popularity poll Disney», «ビッグヒーロー6
  人気投票 公式») y sigue sin aparecer ninguna. Se mantiene el «no encontré».

## 5 · Fandom y qué NO hacer: confirmado (punto 12)

La sección 14 de `biblia.md` ya estaba sin ⚠️ (fue de las mejor confirmadas en
la primera pasada). Repasé sus fuentes:

- La cita de TV Tropes (Memes y Funny) sigue viva:
  [Memes/BigHero6](https://tvtropes.org/pmwiki/pmwiki.php/Memes/BigHero6),
  [Funny/BigHero6](https://tvtropes.org/pmwiki/pmwiki.php/Funny/BigHero6) ✅.
- El TearJerker de TV Tropes (que la biblia no había citado) añade el
  «no hacer» que falta: **no aligerar el funeral de Tadashi** ni la escena en
  que Hiro ve los vídeos del taller de su hermano y dice «supongo que no soy
  como mi hermano» — es uno de los momentos más citados como tearjerker ✅
  ([TearJerker/BigHero6](https://tvtropes.org/pmwiki/pmwiki.php/TearJerker/BigHero6),
  visto por buscador: TV Tropes bloqueó el acceso directo, 403, dos intentos).
- Nuevo para «qué NO hacer»: **el chiste bilingüe de Fred** («Bienvenidos a
  my house») sólo funciona en español — doblarlo *todo* en inglés (como
  hicieron en España, «Bienvenidos a mi casa» sin mezcla) le quita la gracia
  ✅ (confirmado de oído en el punto 2, y por el wikitext de Doblaje Wiki:
  «en su versión doblada se podría decir que fue al revés»).
- La tabla del dolor sigue con pines y mercancía real: reconfirmado sin
  cambios ([Hot Topic](https://www.hottopic.com/product/disney-big-hero-6-baymax-pain-scale-3-pin/10396449.html)).

## 6 · Punto 20 — Gustos y detalles de cada personaje

De las fichas de infobox de `bighero6.fandom.com` (cada una cita como fuente
el **blog oficial de Disney en Tumblr**, `disneysbighero6-bh6.tumblr.com`,
publicado en 2014 para promocionar la película: comprobé que el dominio sigue
vivo y redirige a la ficha real de cada personaje, aunque el contenido está
detrás de JavaScript y no se puede leer con `curl` — cuenta como fuente
oficial + la wiki que la cita, dos fuentes). Añado la sección «Trivia» de
cada wiki, que trae más gustos sueltos.

### Hiro Hamada
- **Altura:** 1,52 m (5'0"). **Edad:** 14 (nace hacia 2017-18 si la película
  pasa en 2031, dato de las fechas que se ven en pantalla) ✅ ([wiki de BH6](https://bighero6.fandom.com/wiki/Hiro_Hamada)).
- **Le gusta:** peleas de robots, los robots, la emoción, la libertad, ositos
  de goma, inventar, alitas picantes, paletas heladas.
- **Le odia:** el fracaso, que lo regañen, **los cacahuates (es alérgico:** lo
  detectó el primer escaneo de Baymax), que lo molesten, las restricciones,
  los supervillanos.
- **Su color menos favorito es el rosa** — dato irónico, porque el rosa es el
  color de Honey Lemon (según la página de ella en el «Diario de Hiro», un
  material promocional) ⚠️ (una fuente, la wiki; no vi el diario original).
- **Manía:** saca la lengua para sujetar el popote antes de beber, señal de
  quien se chupó el dedo de niño; tiene un huequito entre los dientes
  (diastema) por lo mismo ✅ ([wiki de BH6](https://bighero6.fandom.com/wiki/Hiro_Hamada)).
- **Cómo se ve a sí mismo:** orgulloso de saberlo todo por su cuenta; cree que
  ya sabe lo que la universidad podría enseñarle (biblia, punto 9).
- **En el doblaje coreano lo renombraron «Hero Armada»** ⚠️ (una fuente, wiki).

### Baymax
- **Altura:** 1,88 m (6'2") — bastante alto para lo achaparrado que se ve
  inflado ✅ ([wiki de BH6](https://bighero6.fandom.com/wiki/Baymax), cita el
  Tumblr oficial).
- **Le gusta:** ayudar a los demás, la felicidad y salud de sus pacientes y
  amigos, las flores, los gatos, el ajedrez, las pelotas de fútbol, las
  mariposas, los abrazos, los besos, volar, bailar.
- **Le odia:** que sus amigos estén en peligro, la mala salud, quedarse
  desinflado, lastimar a otros o causarles angustia.
- Robots reales que lo inspiraron, además del brazo de Carnegie Mellon: ASIMO
  y **Pepper** (el robot que también da abrazos y choca los puños) ✅
  ([wiki de BH6](https://bighero6.fandom.com/wiki/Baymax)).
- Es el **único personaje que sale en todos los episodios** de toda la
  franquicia, salvo un corto de *Big Chibi 6* ⚠️ (una fuente).

### Tadashi Hamada
- **Altura:** 1,82 m (6'0"). **Edad oficial:** 18 según los libros de Disney
  (*Big Hero 6: Hiro's San Fransokyo Files*), aunque medios japoneses dijeron
  21 y el propio actor de voz original, Daniel Henney, dijo en una entrevista
  que Tadashi tendría 19 o 20 — **hay tres versiones de su edad, todas
  citadas**: ⚠️ (contradicción real entre fuentes, no error mío).
- **Le gusta:** ayudar a los demás, la robótica, las artes marciales, su
  familia y amigos, Baymax, la inteligencia.
- **Le odia:** las peleas de robots, el crimen, la ilegalidad, que Hiro
  desperdicie su talento, que la gente se moleste.
- **En el doblaje coreano lo renombraron «Teddy Armada»** ⚠️ (una fuente).
- En el manga *Big Hero 6* (Baymax) hay una escena eliminada donde Tadashi
  presenta a Baymax junto con Fred en la feria de ciencias ⚠️ (una fuente).

### Honey Lemon
- **Altura:** 1,77 m (5'10"; 1,88 m con tacones) ✅ ([wiki de BH6](https://bighero6.fandom.com/wiki/Honey_Lemon), Tumblr oficial).
- **Le gusta:** química, diseño de modas, explosiones, té verde, el peligro,
  música latina, manga, grabar vídeos de ciencia, karaoke, «fiestas de
  stickers», música pesada.
- **Le odia:** confrontaciones entre amigos, que la gente salga herida, los
  hipopótamos, el pesimismo, el crimen, que le digan «alta».
- **Tiene su propia tienda en línea** (boutique de ropa) ✅.
- Es de **ascendencia hispana**, según su propia actriz de doblaje original
  (Génesis Rodríguez) y una publicación oficial de Disney Television Animation
  ✅ ([wiki de BH6](https://bighero6.fandom.com/wiki/Honey_Lemon), cita un post
  de `@DisneyTVA` en Twitter/X). Encaja con que ella misma se dobló al español
  latino.
- «Honey Lemon» es un apodo que le puso Fred; su nombre real nunca se dice
  (salvo que aparece como «Honey Lemon» de nombre oficial en su credencial
  escolar, en un capítulo de la serie) ⚠️.

### Fred Frederickson
- **Altura:** 1,82 m (6'0") ✅ ([wiki de BH6](https://bighero6.fandom.com/wiki/Fred)).
- **Le gusta:** acción, aventura, caridad, voluntariado, comida chatarra,
  coleccionables, cómics, tacos de fideos, ponerle apodos a la gente, el
  webtoon *Big Chibi 6*.
- **Le odia:** los supervillanos, las arañas, robar.
- Su apellido «Frederickson» no aparece hasta el episodio «Baymax Regresa» de
  la serie (antes sólo se sabía su inicial, «L.», en una carta de
  recomendación firmada por «R. Richards» — un guiño a Mr. Fantástico de
  Marvel) ✅.
- **Toca la guitarra y el sitar.** Le hacen cosquillas. El kanji de su
  playera es «kaiju» (怪獣, monstruo gigante) ✅ ([wiki de BH6](https://bighero6.fandom.com/wiki/Fred)).
- **Color propio: azul** (el traje de kaiju).

### Wasabi
- **Altura:** 1,93 m (6'4"), el más alto del equipo. **Edad:** 21 (su pastel
  de cumpleaños en «Steamer's Revenge» tiene 21 velas) ✅ ([wiki de BH6](https://bighero6.fandom.com/wiki/Wasabi)).
- **Cumpleaños:** no dicho con fecha exacta, pero una escena («muro de
  cumpleaños») muestra un calendario que sugiere que es **el día 15** de
  abril, junio, septiembre o noviembre (el único mes que no se puede descartar
  por el patrón del calendario) ⚠️ (dato deducido por fans a partir de una
  imagen, no confirmado por Disney).
- **Le gusta:** el color verde, tejer, planchar, trenes miniatura, el orden,
  la jardinería sustentable, el tai-chi, sándwiches, pay, láseres, la
  higiene, máquinas de escribir antiguas.
- **Le odia:** el desorden, el polen, los perros (alergia), los gérmenes,
  **las alturas** (acrofobia — la línea del tráiler «me aterran las alturas,
  por eso no la amo», sí es suya), el exceso de velocidad, la imprudencia,
  los chistes malos.
- **«Wasabi» es sólo un apodo**; su verdadero nombre nunca se dice en ninguna
  parte, ni en su expediente ✅.
- **Tiene glosofobia** (miedo a hablar en público) que supera en un capítulo
  de la serie; es supersticioso aunque lo niega ⚠️ (un capítulo, wiki).
- **Color propio: verde** (por el condimento wasabi).

### GoGo Tomago
- **Altura:** 1,62 m (5'4") ✅ ([wiki de BH6](https://bighero6.fandom.com/wiki/Go_Go_Tomago)).
- **Le gusta:** sus amigos, mascar chicle, ingeniería, ensalada de kale,
  kickboxing, punk rock, gatitos.
- **Le odia:** la cobardía, lo «tierno» (a veces), la prudencia excesiva, el
  exceso de payasadas, la soledad.
- **Manía:** pega un chicle mascado a sus vehículos por buena suerte —
  homenaje a la película *The Rocketeer* ✅.
- Es el **primer personaje coreano de Disney** ✅. Su nombre real nunca se
  dice (en los cómics es Leiko Tanaka, japonesa; en la versión Disney es
  coreana); los fans la apodan «Ethel» por sugerencia de su actriz original,
  Jamie Chung ⚠️ (una fuente, tuit archivado).
- **Color propio: amarillo.**

### Tía Cass
- **Le gusta:** hornear, cocinar, su familia, la poesía, ver películas,
  gatos, karaoke, hacer ejercicio.
- **Le odia:** el peligro para su familia, comer por estrés, que Hiro esté
  triste, que insulten su comida, que sus sobrinos se metan en líos.
- Cocina «alitas de pollo con esa salsa picante» (ya en la biblia) y tiene
  gusto por la poesía, algo que casi no se ve en pantalla ✅ ([wiki de BH6](https://bighero6.fandom.com/wiki/Aunt_Cass)).
- **Dato curioso:** en versiones tempranas del guion, Cass iba a ser la madre
  de Hiro y Tadashi (más cerca del cómic original), no su tía ⚠️ (un vídeo de
  2013 de Rotoscopers, una fuente).

### Mochi (el gato)
- Gato bobtail japonés con patrón **calicó de tres colores** (blanco, naranja
  y negro): genéticamente eso es casi siempre hembra, pero Mochi es
  oficialmente macho, por eso Hiro dice «¡sí que está loco ese gato!» — un
  dato de interés textual de Doblaje Wiki, que la biblia ya tenía ✅.

## 7 · Punto 21 — Por qué la gente la ama

### Razones concretas (crítica, premios, ventas)
- **Taquilla:** 222,5 millones de dólares en Norteamérica y 435,3 millones en
  el resto del mundo, **657,8 millones en total** — la animada más taquillera
  de 2014 en todo el mundo ✅ ([Wikipedia, ficha de la película](https://en.wikipedia.org/wiki/Big_Hero_6_(film)),
  contrastado con [Box Office Mojo](https://www.boxofficemojo.com/release/rl2708621313/), citado en la propia Wikipedia).
- **Japón** aportó 76 millones de dólares de esa cifra — uno de los mercados
  más fuertes fuera de EE. UU., algo llamativo para una peli «occidental» ✅
  (mismo artículo de Wikipedia).
- **Crítica:** 90% en Rotten Tomatoes (229 reseñas, nota media 7,4/10), 74/100
  en Metacritic (38 reseñas, «favorable en general»), «A» en CinemaScore
  (encuesta a público de estreno) ✅ (Wikipedia, que cita Rotten Tomatoes y
  Metacritic directamente).
- **Premios:** ganó el **Óscar a Mejor Película Animada** (87.ª entrega);
  7 nominaciones a los Annie Awards (ganó 1); nominada al Globo de Oro; y
  Kids' Choice Award 2015 a «Película animada favorita» ✅ (Wikipedia +
  wikitext de Doblaje Wiki, que menciona el Óscar y el Kids' Choice de forma
  independiente).
- **Reseña citada:** Michael O'Sullivan (*The Washington Post*, 3,5/4
  estrellas): «El verdadero atractivo de Big Hero 6 no es la acción. Es el
  corazón del personaje central» (traducción propia) ✅ (recogida en
  Wikipedia).

### Con qué personaje se identifica el público, y por qué
- **Con Hiro**, por el duelo: perder a un hermano de golpe y no saber qué
  hacer con la rabia es universal; varias reseñas señalan que la película
  «engaña» al espectador (empieza como comedia de robots y se vuelve una
  historia de duelo) — es el motivo más citado de que enganche a tanta gente,
  no sólo a niños ✅ (Washington Post, arriba; TV Tropes, ver abajo).
- **Con Baymax**, por el consuelo: la gente proyecta en él el cuidador ideal
  que nunca juzga y siempre quiere ayudar — de ahí que gane por goleada la
  encuesta de personajes (punto 4) y que en China lo llamen «大众情人», «el
  amor de todos» (biblia, punto 2).

### Las escenas que hacen llorar (o reír de emoción)
**No encontré el minuto exacto de la película para estas escenas** (busqué
guiones con marca de tiempo, la wiki de CinemaSins —que numera «pecados», no
minutos reales— y clips doblados en Dailymotion e Internet Archive con la
escena del incendio: no aparece ninguno; YouTube pide inicio de sesión en
este servidor). Quedan con la escena descrita y ⚠️ de minuto.

- **El incendio y la muerte de Tadashi** (acto 1): Tadashi vuelve corriendo al
  edificio en llamas por salvar al profesor Callaghan; la explosión pasa
  fuera de cámara, se ve sólo el estallido desde donde está Hiro. Duele
  porque es repentino y no se recrea con morbo ✅ (descrito en
  [Wikipedia, la trama](https://en.wikipedia.org/wiki/Big_Hero_6_(film)),
  [wiki de BH6, Tadashi](https://bighero6.fandom.com/wiki/Tadashi_Hamada)).
- **El funeral de Tadashi**, con lluvia: todos los amigos están destrozados,
  intentan consolar a la tía Cass, e Hiro se queda solo, sentado arriba de
  las escaleras, sin hablar con nadie — la lluvia y el silencio hacen el
  golpe ✅ ([TearJerker/BigHero6, TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/TearJerker/BigHero6);
  visto por buscador, la web da 403 directo).
- **Los vídeos del taller de Tadashi**: Hiro los ve solo y dice en voz baja
  «Supongo que no soy como mi hermano» — momento silencioso, sin música
  grandilocuente, que muestra que de verdad lo admiraba ✅ (misma fuente).
- **El sacrificio de Baymax** (clímax): Baymax va a autodesactivarse para
  impulsar a Hiro de vuelta a un portal y le dice, con su voz de siempre,
  que no puede desactivarse hasta que Hiro esté satisfecho con su cuidado.
  Es el momento más citado como el que más hace llorar: Hiro se despide de
  Baymax como se despidió de Tadashi, porque Baymax lleva el «chip» que
  Tadashi programó — es literalmente perder a su hermano dos veces ✅ (muy
  citado en foros y notas de reseña; frase confirmada de oído con minuto en
  el punto 2 de esta parte, aunque en un clip distinto al de la escena
  completa del clímax, que no encontré doblado).
- **Reacciones del público:** no encontré un hilo de Reddit con votos altos
  específico de esta escena (`r/disney`, `r/MadeMeCry`: los que aparecieron
  con la búsqueda por Arctic Shift no hablaban de la película, o la API dio
  «Timeout» varias veces al repetir la búsqueda) ni un vídeo de reacción
  concreto (hay decenas en YouTube, pero esa plataforma pide iniciar sesión
  desde este servidor). Sirve como pista para quien continúe: buscar
  «Big Hero 6 reaction Tadashi» directo en YouTube con sesión iniciada.

## 8 · Punto 22 — Fan dubs y comunidad hispana

- **Parodias fandub en español latino, en YouTube** (con oEmbed comprobado,
  sin necesitar sesión):
  - **«6 Grandes Heroes - Parodia Fandub a La Chilena - Español Latino»**,
    canal **RobertMan FANDUBS** ✅ ([YouTube](https://www.youtube.com/watch?v=pBPMBFzKmQ8),
    confirmado con [oEmbed](https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=pBPMBFzKmQ8&format=json):
    título y canal reales).
  - **«Big Hero Sweet - Parodia Grandes Heroes【Fandub Latino】»**, canal
    **Ken Asakura** ✅ (mismo método de verificación,
    [vídeo](https://www.youtube.com/watch?v=jo8Gk5Gt128)).
  - No pude ver las vistas ni la fecha exacta de ninguno de los dos (oEmbed no
    las da, y YouTube pide sesión desde este servidor para la página normal):
    ⚠️ en ese dato puntual.
- **TikTok, doblaje y memes**: hay una etiqueta activa **«Grandes Héroes
  Doblaje Latino»** con varios clips de fans imitando o comentando el
  doblaje ✅ ([TikTok, discover](https://www.tiktok.com/discover/grandes-h%C3%A9roes-doblaje-latino)).
  Un ejemplo puntual: **«Saludo de Baymax en Español Latino - Grandes
  Héroes»**, de la usuaria `@paulaalegriat` ✅ ([TikTok](https://www.tiktok.com/@paulaalegriat/video/6854733516253433093)).
- **El meme de la casa de Fred**: la revelación de que Fred es multimillonario
  y vive en una mansión («Bienvenidos a mi casa» / «Welcome to mi casa», el
  chiste bilingüe del punto 5) se volvió formato de meme hispano en TikTok,
  con chistes tipo «Creí que vivías bajo un puente» ✅ ([TikTok, «Welcome to
  mi casa Big Hero 6»](https://www.tiktok.com/discover/welcome-to-mi-casa-big-hero-6)).
- **Memedroid en español** tiene una etiqueta «Big Hero 6» con memes de
  fans hispanohablantes ⚠️ (la página bloqueó el acceso directo, 403; visto
  sólo por resumen del buscador, con el título «Top memes de Big Hero 6 en
  español»).
- **No hay covers de opening/ending en español**: a diferencia de un anime,
  *Big Hero 6* es una película sin tema de apertura cantado; lo más cercano
  es «Immortals» de Fall Out Boy (usada en el tráiler), y no encontré ningún
  cover en español de esa canción ligado a la película (busqué «Immortals
  Fall Out Boy cover español Big Hero 6», «Immortals versión latina») — punto
  que **no aplica** tal cual lo pide el encargo, aclarado en vez de forzarlo.
- **No encontré doblajes de fans completos (audio propio) en YouTube ni
  Dailymotion**, sólo las dos parodias de arriba y clips de imitación de voz
  sueltos en TikTok. Puede haber más en YouTube que este servidor no deja ver
  sin sesión: queda como pendiente para quien tenga acceso.

