# Parte · voz — One Piece (puntos 7, 8, 12, 13, 20, 21 y 22)

> Investigador de voz y personajes (repaso corto, EQUIPO.md). **No repito lo que ya está.**
> Antes de mí hubo un piloto del «equipo de 8» que dejó `partes/doblaje.md` (puntos 8 y 22) y
> `partes/personajes.md` + `personajes.json` (puntos 7, 12, 13, 20 y 21) muy completos: los leí
> enteros y sigo desde ahí. También parto de `partes/datos-voz.md` (reparto latino y las 20
> muestras `.mp3` de Doblaje Wiki) y de §2, §9, §10 y §14 de `biblia.md`. Aquí sólo va:
> 1) las muestras de audio que quedaron **sin medir** con `herramientas/voz.py` (doblaje.md
> marcaba su §8.4 «en curso»); 2) dos correcciones de reparto que esas muestras destaparon,
> con segunda fuente; 3) una confirmación importante para el objeto que propone el encargo
> (los carteles de SE BUSCA); 4) los cierres de sección (Lo mejor, No encontré, Bitácora) que
> `doblaje.md` y `personajes.md` dejaron «(pendiente)».
> Formato: `- dato · fuente(s) · ✅ (dos fuentes) / ⚠️ (una) · minuto/segundo si aplica`

## Hallazgos

### Punto 8 · Doblaje latino — las muestras que faltaban por medir

`datos-voz.md` trae 20 muestras `.mp3` de Doblaje Wiki. `personajes.md` ya midió con
`herramientas/voz.py` (Whisper *medium* + Praat) las 15 de los personajes adultos
principales. Quedaban **las 5 versiones «niño»/joven**, que mido aquí, más **4 muestras de
secundarios** que estaban bajadas en la carpeta de trabajo del piloto de doblaje
(`/tmp/claude-0/trabajo/01-doblaje/muestras/`) pero sin medir. Con esto **se cierran las 20
muestras** que doblaje.md daba como «en curso» en su §8.4.

#### Las 5 versiones «niño» (register infantil o joven, con su frase textual)

| Muestra | Quién dobla | Frase textual (Whisper *medium*) | Tono medio | Rango | Velocidad | Qué dice de la voz |
|---|---|---|---|---|---|---|
| **Luffy niño.mp3** | **Mireya Mendoza**, la misma actriz de «Luffy 1/2» (temp. 1ª, DW) | «No importa cuántos secuaces los sigan o qué tan fuertes parezcan, ustedes no se portaron como hombres ni como piratas. ¡Ya olvídalo!» | **435 Hz, muy agudo** | 16,6 st | normal (2,93 p/s) | **Sube casi 200 Hz sobre su Luffy adulto** (237-257 Hz en «Luffy 1/2», tabla de personajes.md): la misma actriz agudiza mucho la voz para el Luffy niño de los flashbacks. |
| **Zoro niño.mp3** | **Jared Mendoza** (actor infantil aparte; Megumi Urawa en japonés) | «…desafiar su dōjō, quiero que salga a pelear el más fuerte de aquí. Oye, no me subestimes por ser un niño… nunca me puedo permitir perder contra una niña.» | **388 Hz, muy agudo** | 22,9 st | normal (2,97 p/s) | Nada que ver con el Zoro adulto de Dafnis Fernández (116 Hz, grave, 14 st): es otro actor, y se nota — mucho más agudo y más expresivo. Es la escena de la promesa a Kuina. |
| **Nami niña.mp3** | **Georgina (Gina) Sánchez**, la misma actriz de «Nami» (temp. 1ª) | «…en la aldea dicen que el clima es benévolo con la isla, así que puedes conseguir mandarinas en cualquier huerto… mi plan es usar mis habilidades como navegante para viajar por todos los océanos y, después de haberlo visto todo, voy a trazar un mapa mundial.» | 393 Hz, muy agudo | 19,5 st | **rápida (3,18 p/s)** | Muy cerca del registro de su Nami adulta (410 Hz): la misma actriz no cambia mucho el tono para la niña. **Frase nueva y muy útil**: es Nami de pequeña explicando su sueño (el mapa del mundo), textual. |
| **Sanji 1.2.mp3** | **Oliver Díaz** (actor infantil aparte; Ikue Ōtani en japonés) | «…tu porción es tres veces más grande que la mía… anciano decrépito, aunque vea un barco no pienso decírselo. Estaré bien, me quedan cinco días de comida… lo dividiré para que me dure 20 días. En 20 días tiene que pasar un barco.» | 294 Hz, agudo | **25,5 st, muy expresiva** | normal (2,85 p/s) | Nada que ver con el Sanji adulto de Noé Velázquez (111 Hz, el más grave del reparto): otro actor, mucho más agudo. **Es el monólogo de los 85 días varado en la roca con Zeff** (el origen de por qué Sanji nunca deja tirar comida, ya contado en `personajes.md` punto 13): esta muestra da la **frase textual exacta** de esa historia, que antes no estaba citada. |
| **Ussop niño.mp3** | **Alejandro Orozco**, el mismo actor de «Usopp 1/2» (DW: ep. 17) | «¡Pirata se acerca, es mejor…! Dicen que existe una medicina milagrosa que puede curar cualquier enfermedad… me gusta imaginar, porque yo soy el hijo de un auténtico pirata.» | 381 Hz, muy agudo | 25,0 st | **lenta (1,35 p/s), la más lenta de todas las muestras medidas** | Mismo actor que el Usopp adulto (194-286 Hz), pero aquí mucho más lento: **la pausa de quien cuenta una fantasía despacio**, no el atropello del Usopp mayor contando mentiras. |

- Todas ✅ (frase y actor confirmados por dos fuentes: la propia muestra de audio de
  [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/One_Piece) medida con `voz.py` +
  la tabla de reparto de la misma wiki en `datos-voz.md`, que ya cruza cada actor con su
  temporada). El **actor infantil** (cuándo es el mismo adulto y cuándo es otro) sólo constaba
  en la tabla de reparto sin comentar; aquí queda explicado con la voz oída.
- **Para la lámina y el bot** (amplía la nota de `personajes.md` §13): si se usa una escena de
  **flashback o infancia** de Luffy, Nami, Sanji o Zoro, la voz que hay que imitar en el texto
  **no es la misma** que la del personaje adulto — es más aguda y, en Zoro y Sanji, de otro
  actor por completo.

#### 4 muestras de secundarios sin medir (bajadas por el piloto de doblaje, sin usar)

| Muestra | Personaje | Voz latina | Frase textual | Tono | Rango | Qué dice |
|---|---|---|---|---|---|---|
| **DoflamingoOP1.mp3** | Donquixote Doflamingo | **Alfredo Gabriel Basurto** (ver corrección abajo) | «Sólo me divierto… ¿qué puedo decir? Por supuesto… los negocios van tan bien en la isla que empezaba a aburrirme… Ya estás demasiado viejo para buscar pelea. Estás manchando el nombre de Buda, almirante Sengoku.» | 136 Hz, **grave** | **28,2 st, la más expresiva de las 4** | Voz calmada y burlona con Sengoku, muy marcada en el tono — coincide con el Doflamingo «que juega con todos» de su ficha. |
| **Mihawk-OP.mp3** | Dracule Mihawk | **Esteban Desco** (confirmado, ver abajo) | «Eso significa la derrota. Su espíritu es inquebrantable. Prefiere morir a ser derrotado. Lo recordaré. Hace mucho que no veía un espíritu así. Por eso… te ganaste el favor de una espada [Yoru]. Te enviaré al fondo del mar con la espada negra más fuerte del mundo.» | 163 Hz, medio | 16,5 st | **rápida (3,27 p/s)**: sereno pero sin pausas largas — el elogio a Zoro tras vencerlo en el East Blue. |
| **Barbanegra_Trujo.mp3** | Marshall D. Teach / Barbanegra | **Rubén Trujillo** (su primera voz; ver corrección abajo) | «Ya que no tienen nada mejor que hacer, ¿qué les parece una buena lucha hasta la muerte, donde yo mismo seré su juez? Quien quede con vida podrá ver el mundo exterior otra vez y navegar en las dulces aguas de la libertad de mi tripulación. ¡Jajajaja…! Llévatelos, pero deja ese. Así que sigues con vida, ¿eh? El hombre al que llaman el heredero del diablo.» | 315 Hz, agudo | 24,9 st | Risa grande y frase larga y teatral: encaja con el villano showman que arenga a su tripulación en Impel Down. |
| **TashigiOP2.mp3** | Tashigi | **Ivett Toriz** (2.ª voz del personaje; ver abajo) | «Los carteles de **Se Busca** acaban de llegar, ¡lo lamento!» | 401 Hz, muy agudo | 11,5 st, la menos expresiva de las 4 | Frase corta y de disculpa — el tono más ajustado de las cuatro (poco rango). **Sirve para el punto 8 y para el objeto del encargo: ver más abajo.** |

- Fuente de cada `.mp3`: [Doblaje Wiki, API, `imageinfo`](https://doblaje.fandom.com/es/api.php?action=query&titles=Archivo:TashigiOP2.mp3&prop=imageinfo&iiprop=url&format=json) sobre las tablas de reparto de
  [One Piece/6ª temporada](https://doblaje.fandom.com/es/wiki/One_Piece/6%C2%AA_temporada) y
  [One Piece/9ª temporada](https://doblaje.fandom.com/es/wiki/One_Piece/9%C2%AA_temporada) (wikitext, leídas por la API) · ✅ (actor + frase, por la propia muestra medida).

#### Dos correcciones de reparto que salieron al medir estas muestras

- **Doflamingo tuvo DOS actores latinos, no uno.** `doblaje.md` §8.3 sólo daba «Christian
  Strempler», con fuente DW + ANMTV (Dressrosa). Ahora, con la muestra `DoflamingoOP1.mp3`
  (tabla de la **6.ª temporada**, su primera aparición como Shichibukai, antes de Dressrosa):
  la voz es **Alfredo Gabriel Basurto**. Christian Strempler lo dobla **desde el ep. 207** (su
  segunda aparición) y se queda con el papel — la propia comunidad explica por qué Basurto no
  volvió: para entonces ya era la voz de Zoro y no iban a repetirlo en dos personajes de peso ·
  [Doblaje Wiki, One Piece/6ª temporada](https://doblaje.fandom.com/es/wiki/One_Piece/6%C2%AA_temporada)
  (wikitext) + [X, One Piece Doblaje Latino News](https://x.com/onepiecedoblat/status/1708248955539112316):
  «¡Donquixote Doflamingo sigue siendo interpretado por Christian Strempler! Recordemos que ya
  le había dado voz en el episodio 207 (su segunda aparición). Sé que a muchos nos encantó la
  voz de Basurto, pero al ser él la voz actual de Zoro, no regresará a doblar a Doflamingo.» · **✅**
- **Marshall D. Teach / Barbanegra no estaba en `doblaje.md` y también tuvo dos voces.**
  Primera aparición (temporada 6, Jaya): **Rubén Trujillo** · confirmado también por
  [X, One Piece Doblaje Latino News](https://x.com/onepiecedoblat/status/1505810635732488192):
  «¡Barbanegra (Marshall D. Teach) en Español Latino! Actor de Voz: Rubén Trujillo». Desde la
  serie de Marineford (temporada 14) pasa a **Carlos Segundo** («2.ª voz» de Teach según su
  [ficha en Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Carlos_Segundo)) · DW (dos
  temporadas) + X + ficha del actor · **✅**. Barbanegra es un villano importante (mata a
  Barbablanca) que no tenía ni una línea en `doblaje.md`: queda cerrado.
- **Mihawk, de ⚠️ a ✅.** `personajes.md` daba «Esteban Desco (muestra Mihawk-OP) ⚠️ una
  fuente». Segunda fuente: [X, One Piece Doblaje Latino News, arco 3D2Y](https://x.com/onepiecedoblat/status/1775390134113849587):
  «Zoro le pide a Mihawk que lo entrene. Mihawk: Esteban Desco». **✅**
- **Tashigi tuvo TRES actrices, no una.** `doblaje.md` sólo apuntaba «Liliana Barba» con ⚠️.
  La ficha de Tashigi en Doblaje Wiki da: **Liliana Barba** (temporada 1ª en adelante, la voz
  «titular»), **Ivett Toriz** (temporada 9ª — la de la muestra «TashigiOP2», la que dice la
  frase de los carteles) y **Rosalinda Márquez** (un solo capítulo, el 336) ·
  [Doblaje Wiki, ficha de Tashigi](https://doblaje.fandom.com/es/wiki/Tashigi) (wikitext,
  tabla «Ficha por actriz de doblaje») + la propia tabla de la 9.ª temporada · **✅**

#### La frase de Tashigi y el objeto que propone el encargo

**«Los carteles de Se Busca acaban de llegar, ¡lo lamento!»** (Tashigi, «TashigiOP2.mp3»,
0:01-0:04, doblaje latino, temp. 9ª, voz de Ivett Toriz).

Esto importa para #bienvenidas. La biblia (§14 y §16) sólo tenía «SE BUSCA» como una palabra
de la **emisión española** del ep. 45 (hoja O2), y avisaba de no mezclarla con el estilo
americano (WANTED / DEAD OR ALIVE / MARINE) del anime. **Esta muestra es del doblaje
LATINOAMERICANO** (confirmado: la tabla de reparto de la 9.ª temporada la pone en la columna
de México, con Ivett Toriz) y **usa literalmente «carteles de Se Busca»**. Es decir: **«Se
Busca» no es sólo cosa de España — el doblaje latino también lo dice**, al menos en esta
escena. Sigue sin encontrarse un cartel dibujado en pantalla que diga «SE BUSCA» en la versión
latina (sólo hay imagen de eso en la española, hoja O2): el término se oye, pero no está
comprobado que se vea escrito así en el anime latino. **Para el concepto del encargo (carteles
de SE BUSCA clavados en la madera del barco): usar «SE BUSCA» en el texto es fiel al doblaje
que se oye en Latinoamérica, aunque la imagen de referencia del cartel escrito sea la
española.** · Doblaje Wiki (muestra + tabla de reparto) · ⚠️ (una frase oída, no una imagen
del cartel en la versión latina — pero es la propia voz del doblaje, la fuente más directa
que hay).

### Punto 13 · Cómo suena la voz de niño frente a la de adulto (para textos del bot)

Con las 5 muestras «niño» medidas arriba, la tabla de `personajes.md` §13 («Cómo suena cada
voz latina») queda así de completa para quien escriba texto de personaje-niño en el bot o en
láminas de flashback:

| Personaje | Adulto (ya en personajes.md) | Niño/joven | Mismo actor? |
|---|---|---|---|
| Luffy | 237-257 Hz (Mireya Mendoza) | **435 Hz** | Sí, misma actriz, mucho más aguda |
| Zoro | 116 Hz (Dafnis Fernández) | **388 Hz** | No — otro actor (Jared Mendoza) |
| Nami | 410 Hz (Gina Sánchez) | 393 Hz | Sí, casi el mismo tono |
| Sanji | 111 Hz (Noé Velázquez) | **294 Hz** | No — otro actor (Oliver Díaz) |
| Usopp | 194-286 Hz (Alejandro Orozco) | 381 Hz, mucho más lento | Sí, mismo actor, otro ritmo |

**Lectura para la lámina:** si el bot o una lámina 2 usa una viñeta de infancia (el sueño de
Nami con el mapa, la promesa de Zoro a Kuina, los 85 días de Sanji en la roca), el texto tiene
que sonar más agudo y, en Zoro y Sanji, distinto del habla adulta ya fijada en la biblia.

## Lo mejor para la lámina

- **La frase de Tashigi resuelve una duda real del encargo**: «Se Busca» sí se oye en el
  doblaje latino (no sólo en la emisión española), así que el cartel de #bienvenidas puede
  decir «SE BUSCA» sin sonar a traducción ajena al doblaje que conoce el servidor.
- **El monólogo de Sanji niño** («me quedan cinco días de comida… en 20 días tiene que pasar
  un barco») es la frase textual que faltaba para la historia de los 85 días que ya se cuenta
  en `personajes.md`: sirve para un texto del bot sobre «nunca tires la comida».
- **Nami niña explicando su sueño** («voy a trazar un mapa mundial») es una frase corta y
  perfecta para un texto de bienvenida sobre «cuál es tu sueño en el servidor», en la voz real
  de la navegante desde pequeña.
- Doflamingo y Barbanegra dejan de ser villanos sin voz latina documentada: si alguna lámina
  de otro canal (avisos, eventos) los usa, ya hay actor y frase con fuente.
- **Aviso de ahorro:** las 9 muestras nuevas están en
  `/tmp/claude-0/trabajo/01-voz/voz_medium/<nombre>/` (`ficha_voz.json`, `transcripcion.txt`,
  `voz.wav`); no hace falta volver a bajarlas ni medirlas.

## No encontré

- **Por qué Zoro y Sanji ganan justo en Latinoamérica** (y no Luffy): busqué en español
  («por qué Zoro es tan popular en Latinoamérica encuesta One Piece») y sólo salieron notas
  que repiten el resultado de la encuesta (Cinepremiere, Ramen Para Dos, ETC.cl — este último,
  fuente nueva que confirma otra vez el top de 2021 con Nami y Zoro), pero ninguna da una
  razón cultural o de doblaje. `personajes.md` ya lo marcaba como pendiente; sigue sin
  resolverse con fuente.
- **Por qué Carrot (coneja *mink*) es tan votada en Latinoamérica** (9.ª en 2026, 5.ª en
  2021): no encontré ninguna nota que lo explique; ni siquiera tiene doblaje latino propio
  confirmado con nombre de actriz en Doblaje Wiki (no tiene página).
- **Imagen de un cartel «SE BUSCA» dentro del anime en la versión latina** (con la letra en
  pantalla, no sólo oído): no la encontré; sólo existe la de la emisión española (hoja O2 de
  la biblia). Puede que no exista — en el doblaje latino los carteles suelen dejarse en inglés
  y sólo se traduce lo que se dice en voz alta.
- **Segunda fuente para «por qué se fue Dafnis Fernández de Zoro»**: sigue sólo en Doblaje
  Wiki; su entrevista en El Heraldo (ya citada en `doblaje.md`) habla del personaje pero no de
  su salida.

## Bitácora

- **Doblaje Wiki, API** (`action=parse&prop=wikitext`): páginas `One Piece/6ª temporada` y
  `One Piece/9ª temporada` (para rastrear el reparto exacto de las muestras `DoflamingoOP1`,
  `Mihawk-OP`, `Barbanegra_Trujo` y `TashigiOP2`), ficha de `Tashigi` (sus tres actrices) y
  `Hideyuki Tanaka` (seiyū de Doflamingo, sin dato útil nuevo). Español.
- **Doblaje Wiki, API `imageinfo`**: URL directa de `Archivo:TashigiOP2.mp3` para citar la
  fuente exacta del audio.
- **`herramientas/voz.py`** (Whisper *medium* + Praat), 9 corridas: `Luffy_niño`, `Nami_niña`,
  `Sanji_1.2`, `Ussop_niño`, `Zoro_niño` (de `/tmp/claude-0/trabajo/01-personajes/audio/`, ya
  bajados por el piloto anterior) y `Barbanegra_Trujo`, `Mihawk-OP`, `DoflamingoOP1`,
  `TashigiOP2` (de `/tmp/claude-0/trabajo/01-doblaje/muestras/`, también ya bajados). No hizo
  falta bajar nada nuevo.
- **WebSearch** (español): `"Carlos Segundo" Barbanegra One Piece doblaje latino` →
  confirmó la 2.ª voz de Barbanegra y su ficha en Doblaje Wiki.
  `"Christian Strempler" Doflamingo One Piece Marineford ANMTV` → dio el tuit de **One Piece
  Doblaje Latino News** que fija el episodio 207 como el cambio de Basurto a Strempler.
  `Esteban Desco Mihawk One Piece doblaje entrevista` → dio el tuit del arco 3D2Y que confirma
  a Desco como Mihawk (2.ª fuente).
  `por qué Zoro es tan popular en Latinoamérica encuesta One Piece` → sin razón nueva (ver «No
  encontré»); salió ETC.cl como fuente adicional del resultado de 2021.
- **onepiece.fandom.com, API `pageimages`**: retratos de Tashigi y de Marshall D. Teach
  (dimensiones reales) para `voz.json`, ya que estos dos personajes se quedaban sin ninguna
  imagen propia en `personajes.json`.
- No usé YouTube (pide iniciar sesión en este servidor, como avisa el encargo); todo el audio
  ya estaba bajado de Doblaje Wiki por el piloto anterior.

## Segunda pasada · lo que pedía el «Sigue» anterior

> Relanzamiento de esta parte (misma investigadora de voz). Sólo dos tareas quedaban pendientes:
> medir con `voz.py` las muestras de Doblaje Wiki de Crocodile, Smoker, Vivi, Sabo, Katakuri (y
> Jinbe si había muestra), y buscar una tercera fuente del motivo de la salida de Dafnis
> Fernández de Zoro. Añado sin tocar lo de arriba.

### Punto 8 · las muestras de los cinco personajes pedidos (y Jinbe)

**Se pudo medir Crocodile y Vivi** (ésta con dos muestras). **Smoker, Sabo, Katakuri y Jinbe NO
tienen ninguna muestra de audio en Doblaje Wiki**: comprobado con `action=parse&prop=wikitext`
sobre sus páginas de personaje (`Crocodile`, `Smoker`, `Nefertari_Vivi`, `Sabo`; Katakuri no
tiene página propia, sólo fila en `One_Piece/19ª_temporada`), sobre las páginas de sus actores
(`Dan_Osorio`, `Erick_Selim`, `Luis_Leonardo_Suárez` — la redirección de «Luigi Suárez» — y
`Lourdes_Arruti`) y con `action=query&list=search&srnamespace=6` (archivos) para cada nombre:
ningún resultado termina en `.mp3` salvo los de Crocodile y Vivi de abajo. Probé además
`prop=imageinfo` sobre `Archivo:Smoker-OP.mp3`, `Archivo:Smoker 1.mp3`, `Archivo:Sabo-OP.mp3`,
`Archivo:Sabo niño.mp3`, `Archivo:Katakuri-OP.mp3`, `Archivo:Jinbe-OP.mp3` y `Archivo:Jinbe 1.mp3`:
todas «missing». En la tabla de la 1ª temporada, la fila de Smoker tiene la columna «Audio»
vacía (igual que Crocodile y Vivi en la 2ª temporada) — Doblaje Wiki no llegó a subir esas
muestras. ⚠️→confirmado con búsqueda exhaustiva, no es que faltara mirar.

| Muestra | Personaje | Voz latina (ya en `doblaje.md` §8.3) | Frase textual (Whisper *medium*) | Tono medio | Rango | Velocidad | Qué dice de la voz |
|---|---|---|---|---|---|---|---|
| **Crocodile-OP.mp3** | Sir Crocodile / Sr. 0 | Sebastián Llapur | «Pueden llamarme como quieran, miradas veo que les interesa causar estragos en este país, no permito que alguien que se burla de mí, siga con vida después de faltarme al respeto, deja de jugar maldito me acaso[o].» | **113 Hz, grave** | 27,7 st, **muy expresiva** | normal (2,21 p/s) | Voz grave y teatral, con mucho rango — encaja con el villano frío y sarcástico de Alabasta; Whisper tropieza con la última frase («me acaso» = «mocoso», revisar de oído). |
| **Vivi (Niña) Ep de Alabasta Latino.mp3** | Nefertari Vivi (de niña, en el especial *One Piece: Episodio de Alabasta*) | **Lourdes Arruti** (misma actriz que la Vivi adulta: ver corrección abajo) | «Pregunta, ¿por qué entrenas todos los días? Oye, pero ¿contra quién pelearás? ¿Son diferentes? Oh, qué raro. Líder, te lo prometo.» | 368 Hz, **muy agudo** | 15,4 st | normal (2,57 p/s) | Frases cortas y curiosas de una niña — nada que ver con el registro más adulto de abajo; es la Vivi pequeña hablando con su padre o Igaram. |
| **Vivi LourdesArruti.mp3** | Nefertari Vivi / Srta. Miércoles | **Lourdes Arruti** | «Muy bien, es hora de mostrarles tu velocidad superior a la de un leopardo. Es un reino con costumbres magníficas y lleno de paso, o al menos lo verá. Llegó la hora de la seducción. Es exactamente lo que intento evitar. Los rebeldes, el ejército real y toda la gente de este reino no tienen la culpa. **Entonces, explícame por qué tienen que morir.**» | 282 Hz, agudo | **28,0 st, muy expresiva** | normal (2,92 p/s) | La frase final es el reclamo de Vivi a Crocodile por los inocentes que van a morir en la guerra civil de Alabasta (arco Alabasta, hacia el final) — una de sus líneas más citadas por el fandom. |

- Fuente de los tres `.mp3`: [Doblaje Wiki, API `imageinfo`](https://doblaje.fandom.com/es/api.php?action=query&format=json&titles=Archivo:Crocodile-OP.mp3&prop=imageinfo&iiprop=url) · ✅ (audio + reparto de `datos-voz.md`/`doblaje.md`, que ya daban el actor con una fuente; ahora hay frase real que lo confirma).

#### Corrección de reparto: Vivi niña y Vivi adulta las hace LA MISMA actriz (segunda fuente)

`doblaje.md` §8.3 sólo daba «Vivi: Lourdes Arruti (también traduce) · DW · ⚠️ (misma wiki)».
Con la muestra de la Vivi niña salió una duda (¿otra actriz, como pasa con Luffy/Zoro/Sanji
niños?) y se resolvió que **no**: en el wikitext de
[One Piece: Episodio de Alabasta](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=One_Piece%3A_Episodio_de_Alabasta)
la fila de «Nefertari Vivi / Srta. Miércoles» (adulta) y la de «Nefertari Vivi (niña)» comparten
`rowspan="2"` con el mismo nombre: **Lourdes Arruti** (créditada «Lulú Arruti»). Segunda fuente
independiente: el wikitext de la [ficha de la propia actriz](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Lourdes_Arruti),
que trae `Vivi LourdesArruti.mp3` como uno de sus 5 demos y la lista en su currículum como
«Vivi Nefertari en One Piece (2020-presente/LA)» y también en «One Piece: Episodio de Alabasta
(2022)». **Vivi pasa de ⚠️ a ✅.**

### Tercera fuente del motivo de salida de Dafnis Fernández — sigue sin encontrarse

Busqué en profundidad (11 búsquedas web + 4 páginas leídas) una fuente distinta de Doblaje Wiki
que explique **por qué** Dafnis Fernández dejó a Zoro («diferencias con la empresa» + no poder
ir siempre al estudio, según DW). **No encontré ninguna que dé el motivo.** Sí encontré **dos
fuentes independientes que confirman que el cambio ocurrió** (el hecho, no la razón), que sirven
para no depender sólo de DW en eso:
- [ANMTV, «One Piece: Netflix estrena…»](https://www.anmtvla.com/2023/07/one-piece-netflix-estrena-nueva-tanda.html):
  «Zoro pasa a ser interpretado nuevamente por Gabriel Basurto, quien fuera su primera voz para
  el doblaje de 4Kids, en sustitución de Dafnis Fernández» — sin motivo.
- [Cine PREMIERE, «One Piece llega a Netflix con nuevo doblaje latino»](https://cinepremiere.com.mx/one-piece-netflix-nuevo-doblaje-latino.html):
  confirma a Dafnis Fernández como Zoro en el primer doblaje latino, tampoco explica el cambio.
- Revisé también las fichas de Doblaje Wiki de [Alfredo Gabriel Basurto](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Alfredo_Gabriel_Basurto)
  y de [Dafnis Fernández](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Dafnis_Fern%C3%A1ndez)
  (ambas con su sección «Curiosidades»), la entrevista completa de
  [El Heraldo (2025)](https://www.elheraldo.co/cultura/cine/2025/07/06/tyrion-lannister-es-un-parteaguas-en-mi-carrera-dafnis-fernandez-actor-de-doblaje/)
  y un hilo del foro de Pirate-King: ninguno menciona el motivo.
- **Conclusión: el motivo de la salida sigue teniendo una sola fuente (Doblaje Wiki)**; lo que
  ahora tiene dos fuentes es sólo el hecho de que Dafnis dejó el papel y Basurto lo retomó. No
  bajo el ⚠️ de `doblaje.md` en ese dato concreto — sería inventar una fuente que no está.

## Lo mejor para la lámina (añadido)

- **La frase de Vivi a Crocodile** («Entonces, explícame por qué tienen que morir») es de las
  líneas más citadas del arco Alabasta: sirve para un texto sobre injusticia o sobre defender a
  los tuyos.
- **Vivi niña y adulta, misma actriz** (Lourdes Arruti): útil si el bot usa un flashback de Vivi
  pequeña con Igaram o su padre — no hace falta «envejecer» el texto, es la misma voz real.
- **Crocodile grave y muy expresivo** (113 Hz, 27,7 semitonos) es el villano con el rango más
  amplio medido hasta ahora en esta parte, por encima de Barbanegra y Doflamingo.

## No encontré (añadido)

- **Muestra de audio de Smoker, Sabo, Katakuri y Jinbe en Doblaje Wiki**: no existen — comprobado
  con wikitext de sus páginas/tablas de temporada, páginas de sus actores y búsqueda de archivos
  `.mp3` por nombre (namespace 6). No es que falte buscar: la propia wiki no las subió (columna
  «Audio» vacía en sus tablas).
- **Tercera fuente del motivo real de la salida de Dafnis Fernández de Zoro**: sigue sin
  aparecer tras 11 búsquedas y 4 páginas leídas a fondo (ver arriba). Sólo Doblaje Wiki explica
  el porqué; otras dos fuentes (ANMTV, Cine PREMIERE) sólo confirman que el cambio pasó.

## Bitácora (añadido)

- **Doblaje Wiki, API** (`action=parse&prop=wikitext`): páginas de personaje `Crocodile`,
  `Smoker`, `Nefertari_Vivi`, `Sabo`, tablas `One_Piece/1ª_temporada`, `One_Piece/2ª_temporada`,
  `One_Piece/19ª_temporada`, `One_Piece:_Episodio_de_Alabasta`, y fichas de actor `Dan_Osorio`,
  `Erick_Selim`, `Luis_Leonardo_Suárez`, `Lourdes_Arruti`, `Alfredo_Gabriel_Basurto`,
  `Dafnis_Fernández`. Español.
- **Doblaje Wiki, API** `list=search&srnamespace=6` (archivos) por «Crocodile», «Smoker», «Vivi»,
  «Sabo», «Katakuri», «Jinbe» (hasta `srlimit=500`), para confirmar qué personajes tienen o no
  `.mp3` subido.
- **Doblaje Wiki, API `imageinfo`** sobre nombres de archivo probados a mano (`Smoker-OP.mp3`,
  `Sabo-OP.mp3`, `Sabo niño.mp3`, `Katakuri-OP.mp3`, `Jinbe-OP.mp3`, `Jinbe 1.mp3`, etc.): todas
  «missing»; `Crocodile-OP.mp3` y los dos de Vivi sí existen.
- **`herramientas/voz.py`** (Whisper *medium* + Praat), 3 corridas nuevas: `Crocodile-OP`,
  `Vivi_nina` (la del especial de Alabasta) y `Vivi_LourdesArruti`. Archivos en
  `/tmp/claude-0/trabajo/01-voz/<nombre>/`.
- **WebSearch** (español, 11 búsquedas): variantes de `"Dafnis Fernández" Zoro salió / dejó /
  reemplazado / diferencias / empresa / motivo / entrevista / podcast / Colombia / Reddit /
  tuit Basurto` → ninguna dio el motivo; sólo confirmaron el hecho del cambio (ANMTV, Cine
  PREMIERE) o repitieron el texto de Doblaje Wiki sin fuente nueva.
- **WebFetch**: artículo completo de El Heraldo (2025), artículo de ANMTV, artículo de Cine
  PREMIERE, hilo de Pirate-King («One Piece vuelve a Latinoamérica»). Ninguno menciona el motivo
  de la salida de Dafnis.
- **onepiece.fandom.com, API `pageimages`**: retratos de Crocodile y Nefertari Vivi para
  `voz.json`.
