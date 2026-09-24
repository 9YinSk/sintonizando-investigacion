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

