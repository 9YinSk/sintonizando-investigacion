# Voz y personajes · Pokémon (07-pok-mon)

Investigador de voz y personajes. Puntos de `ENCARGO.md`: **7** (popularidad),
**8** (doblaje latino), **12** (fandom y qué no hacer), **13** (carácter y
forma de hablar) — repaso y confirmación en dos fuentes — y **20, 21, 22**
(gustos, por qué la aman, fan dubs), nuevos.

Parto de `partes/datos-voz.md` (AniList, Doblaje Wiki, Dailymotion, Reddit) y
de las secciones 8, 9, 10 y 14 de `biblia.md` (ya escritas en la primera
pasada, con red cerrada). No repito lo que ya está ✅ ahí; confirmo lo ⚠️,
corrijo lo que encontré mal y añado lo nuevo.

Trabajo pesado (audios .ogg de Doblaje Wiki, transcripciones de `voz.py`) en
`/tmp/claude-0/trabajo/07-pok-mon-voz/`.

---

## 1 · Doblaje latino: nombres nuevos y confirmación en dos fuentes (puntos 7-8)

Corrí la API de Doblaje Wiki sobre la página principal **`Pokémon`** (no sólo
`Max (Pokémon)`, que es la que trajo `recolectar.py` y venía con la tabla de
reparto vacía): `https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Pok%C3%A9mon`.
Trae la ficha completa con temporada, episodios y **muestra de audio real**
por actor (archivos `.ogg` en `static.wikia.nocookie.net`).

| Personaje | Voz latina | Estado | Fuentes |
|---|---|---|---|
| **Delia Ketchum** (madre de Ash) | **Patricia Hannidez** (temp. 1-7, 12+; a veces reemplazada por Karina Altamirano o Rebeca Manríquez en *Crónicas Pokémon*, eps. 8 y 14) | ✅ nuevo | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon), [Doblaje Wiki (ficha propia)](https://doblaje.fandom.com/es/wiki/Delia_Ketchum), [X/Kenshiro97](https://x.com/97_kenshiro/status/1793283148702253274) |
| **Gary Oak** (el rival) | **Gerardo del Valle**, temp. 1-5 y primera película; volvió en el redoblaje de 2015 y en *Viajes Pokémon* (2022) | ✅ nuevo | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon), [Doblaje Wiki (ficha propia)](https://doblaje.fandom.com/es/wiki/Gerardo_del_Valle), [WikiDex](https://www.wikidex.net/wiki/Gerardo_del_Valle), [Pokémon Project](https://pokemon-project.com/anime-5/actores-de-doblaje-y-seiyuus/gerardo-del-valle) |
| **Giovanni** (jefe del Equipo Rocket) | **Alejandro Villeli** | ✅ nuevo | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon), [WikiDex](https://www.wikidex.net/wiki/Alejandro_Villeli), [TikTok (bio)](https://www.tiktok.com/@theraer17/video/7314397862006131974) |
| **Pikachu hablando** en *La película Pokémon: ¡Yo te elijo!* (2017) | **Ana Lobo**, actriz de Michoacán | ✅ (ya estaba en biblia.md como ⚠️, ahora con 2ª fuente) | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/La_pel%C3%ADcula_Pok%C3%A9mon:_%C2%A1Yo_te_elijo!), [mimorelia.com](https://mimorelia.com/noticias/nueva-voz-pikachu-michoacan-aqui-le-decimos-parte) |
| **Traductor y adaptador** de la serie original | **Bernardo López** | ✅ (pasa de ⚠️ a ✅: infobox de Doblaje Wiki + nota independiente) | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon), [Doblaje Wiki (ficha propia)](https://doblaje.fandom.com/es/wiki/Bernardo_L%C3%B3pez), [Azteca Jalisco](https://www.aztecajalisco.com/espectaculos/quien-hizo-el-doblaje-pokemon-en-espanol-latino-actores-estudios-y-datos-que-no) |
| **Estreno en Cartoon Network Latinoamérica**: 6 de septiembre de 1999 | — | ✅ (pasa de ⚠️ a ✅) | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon) («En Latinoamérica el 6 de septiembre de 1999 por el canal de cable Cartoon Network»), [Wikipedia ES](https://es.wikipedia.org/wiki/Pok%C3%A9mon_(serie_de_televisi%C3%B3n)) (confirma que se emitió en Cartoon Network desde esa fecha hasta el 20 de enero de 2004) |
| **Enfermera Joy**, episodio 2 (temp. 1) | Liliana Barba (luego reemplazada de forma estable por Mildred Barrera desde Ciudad Plateada) | ⚠️ una fuente (Doblaje Wiki, «Datos de interés») | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon) |
| **Pokédex** (voz del aparato), episodios de Totodile (temp. 3) | Rubén León (México) | ⚠️ una fuente — resuelve el «no encontrado» que dejó la primera pasada, aunque sólo para esos 3 episodios puntuales | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon) |

**Ojo, contradicción dentro de la propia Doblaje Wiki** (para que el redactor
no la use sin más): la tabla de reparto de la página `Pokémon` dice que en el
**episodio 17** de la temporada 1, el «voice-over» de Pikachu (cuando tiene
diálogos hablados) lo hizo **Ana Lobo**; pero la sección «Datos de interés» de
la misma página dice que ese mismo episodio 17 lo dobló **Claudia Motta**. No
lo pude comprobar oyendo el episodio (no está en Dailymotion ni en Internet
Archive con ese número exacto). Dejarlo como ⚠️ hasta que alguien lo escuche.

**Reparto ya confirmado en la primera pasada** (Oak-Hugo Navarrete, Ash-Gabriel
Ramos/Miguel Ángel Leal, Pikachu-Ikue Ōtani, Misty-Xóchitl Ugarte,
Brock-Gabriel Gama, Jessie-Diana Pérez, James-Pepe Toño Macías,
Meowth-Gerardo Vásquez): lo re-confirmé con la ficha de reparto de Doblaje
Wiki de la página `Pokémon` (con muestra de audio propia para cada uno, ver
sección 2) más las fuentes que ya tenía la biblia. Sigue ✅.

---

## 2 · Frases del doblaje latino, textuales y con minuto (punto 8)

Con `herramientas/voz.py` (Whisper local) sobre audio real: las muestras de
Doblaje Wiki (una por personaje, dan una frase suelta, sin minuto de episodio
porque son clips de muestra) y un tráiler oficial y un episodio completo de
Dailymotion/Internet Archive (con minuto exacto).

### Muestras de Doblaje Wiki (voz real de cada actor, transcritas)
Archivo en `static.wikia.nocookie.net/doblaje/...`, bajado y pasado por
`voz.py --idioma es`. Frase representativa de cada uno (revisado a oído,
Whisper se equivoca con nombres propios):

- **Ash** (Gabriel Ramos), *S01E07*: «Pikachu, ¿pero qué haces ahí? [...] ¿Qué
  estás diciendo, que no quieres pelear contra Misty? Creo que está bien que
  no quieras pelear contra una amiga» ✅ — [audio](https://static.wikia.nocookie.net/doblaje/images/3/38/POS_Ash_Ketchum_S01E07.ogg).
- **Pikachu** (Ikue Ōtani, japonés conservado), *S01E07*: sólo «¡Pika!»,
  «Chuuu», «Kaachu» — confirma que nunca dice palabras, sólo su nombre ✅.
- **Misty** (Xóchitl Ugarte), *S01E07*: «Soy entrenadora de Ciudad Celeste,
  también. Soy la cuarta hermana sensacional [...] si pelea con él, probaré
  que no soy una fracasada y que soy tan buena entrenadora como ustedes» ✅.
- **Brock** (Gabriel Gama), *S01E07*: «Yo también soy líder de gimnasio y
  sería una falta de respeto, ¿tú entiendes?» ✅.
- **Profesor Oak** (Hugo Navarrete): «Al que madruga Dios le ayuda, y en este
  caso gana el Pokémon [...] tengo que advertirte que hay un problema con
  este último» ✅ — la misma idea del «problema con este último» que ya
  estaba citada en la biblia desde la película de 2017 (00:04:01): Oak repite
  esta muletilla en distintas épocas del doblaje.
- **Gary Oak** (Gerardo del Valle), *S05E59*: «El torneo final será de 6
  contra 6 [...] ¡te voy a destrozar! ¡Te veré en la demolición!» ✅ — tono de
  rival fanfarrón.
- **Giovanni** (Alejandro Villeli), *S01E63*: «¿De qué están hablando,
  ineptos? [...] ¡Son unos incompetentes!» ✅ — grave y autoritario, coincide
  con «jefe rudo» de su ficha.
- **Delia Ketchum** (Patricia Hannidez), *S01E64*: «Ay... ya me estoy
  preocupando por Ash, espero que esté bien [...] tendré tu almuerzo listo en
  un minuto» ✅ — la madre siempre pendiente de que Ash coma.
- **Jessie** (Diana Pérez), *S01E07*, fragmento del lema: «...para proteger al
  mundo de la devastación, para denunciar los males de la verdad y el amor...
  ¡El Equipo Rocket viajando a la velocidad de la luz!» ✅.
- **James** (Pepe Toño Macías), *S01E07*: «Permítanos presentarnos, para unir
  a los pueblos dentro de nuestra nación, para extender nuestro reino hasta
  las estrellas [...] ríndanse ahora o prepárense para luchar» ✅ — con las
  dos mitades del lema (Jessie + James) se puede armar el lema completo con
  voz real, no de memoria.
- **Meowth** (Gerardo Vásquez), *S01E07*: «¡Porque yo sí sé cómo hacerlo! [...]
  ¡Y ahora ha llegado rápido!» ✅.

### Un tráiler oficial en Dailymotion, con minuto (`&t=`)
«Trailer Oficial La Película Pokémon ¡Yo te Elijo! Completo [Español Latino]
HD» (canal Rahiwalayu) — https://www.dailymotion.com/video/x69qn7q — pasado
por `voz.py`:
- [0:07] «...que madruga todo se le resuelve, y en este caso se queda con el
  Pokémon» — https://www.dailymotion.com/video/x69qn7q?t=7
- [0:18] **«Hola Pikachu, mi nombre es Ash y vamos a ser los mejores amigos»**
  — https://www.dailymotion.com/video/x69qn7q?t=18 (la misma frase que ya
  citaba la biblia del minuto 00:04:44 de la película completa, pero aquí
  con fuente y minuto propios del tráiler)
- [1:04] «No eres muy débil. Recuerda: la supremacía del más fuerte es la
  ley» (Gary/rival) — https://www.dailymotion.com/video/x69qn7q?t=64
- [1:20] «Mientras tenga a mi amigo, puedo ir a cualquier lugar» (Ash) —
  https://www.dailymotion.com/video/x69qn7q?t=80

### Un episodio completo en Internet Archive, con minuto
`https://archive.org/details/pokemon-capitulo-18-espanol-latino` — 23:10 min,
960×720, doblado. **Hallazgo importante**: por el diálogo («varados en
Portovista, esperando tres horas al siguiente ferry para volver a la tierra
principal») es el **capítulo 18, "Beauty and the Beach"**, el episodio con la
escena del concurso de bikinis que **4Kids no distribuyó fuera de Japón y
quedó excluido de los DVD** (confirmado por el propio Doblaje Wiki, sección
«Sobre la grabación», ver punto 5). La página de Doblaje Wiki dice que, según
**Diana Pérez** (voz de Jessie), el episodio **sí se dobló al español** en su
momento porque el elenco recibía los episodios japoneses originales antes de
que 4Kids decidiera no distribuirlo. Esta copia de Internet Archive parece ser
justo ese doblaje raro. Frase transcrita con `voz.py --desde 0 --hasta 150`:
- [1:42-2:03] (narrador) «Nubes blancas... y mar hasta donde alcanzas a ver.
  Ya que ese barco nos sacara de esta isla. Encontramos a nuestros héroes
  varados en Portovista, el único sitio en la isla con transporte a la tierra
  principal. Parece que nuestros amigos perdieron el barco y que pasarán tres
  largas horas hasta el siguiente ferry» — https://archive.org/details/pokemon-capitulo-18-espanol-latino?t=102
- ⚠️ No alcancé a mirar el resto del episodio (23 min) ni a confirmar el
  reparto de voces de este doblaje específico contra la ficha oficial: el
  redactor o quien retome esto debería oírlo entero, es una rareza de
  doblaje que interesa mucho a un servidor de doblaje.

---

## 3 · Cómo se expresan: voz medida, no de oído (punto 13)

`voz.py` mide registro (Hz), expresividad (semitonos) y velocidad
(palabras/s) sobre la muestra de Doblaje Wiki de cada uno. Sirve para la
«guía de voz» de cada personaje (ya lo pedía el punto 13: tono, cómo se ríe,
cómo se enfada, cómo explica):

| Personaje | Registro | Expresividad | Velocidad | Lectura |
|---|---|---|---|---|
| Ash (Gabriel Ramos) | agudo, 247 Hz | muy expresiva, 16.7 semitonos | rápida, 3.23 pal/s | niño enérgico, cambia de tono rápido |
| Pikachu (Ikue Ōtani) | muy agudo, 348 Hz | muy expresiva, 15.0 semitonos | lenta, 1.16 pal/s | ladridos cortos, no frases: cada «chu» es una unidad completa |
| Misty (Xóchitl Ugarte) | muy agudo, 335 Hz | muy expresiva, 16.3 semitonos | rápida, 3.83 pal/s | la más rápida del grupo: encaja con su carácter mandón |
| Brock (Gabriel Gama) | medio, 204 Hz | expresiva, 11.6 semitonos | rápida, 3.61 pal/s | el más «plano» en semitonos: voz calmada de hermano mayor |
| Jessie (Diana Pérez) | agudo, 295 Hz | muy expresiva, 22.6 semitonos | normal, 2.39 pal/s | el lema se declama, no se habla: por eso baja la velocidad y sube la expresividad |
| James (Pepe Toño Macías) | agudo, 225 Hz | muy expresiva, 20.0 semitonos | normal, 2.83 pal/s | parecido a Jessie en el lema (declamado) |
| Meowth (Gerardo Vásquez) | muy agudo, 327 Hz | la más expresiva de todas, 25.6 semitonos | rápida, 3.14 pal/s | el que más sube y baja el tono: es el «cómico» del trío |
| Profesor Oak (Hugo Navarrete) | medio, 149 Hz | expresiva, 12.1 semitonos | rápida, 3.01 pal/s | el más grave junto con Giovanni: autoridad calmada |
| Gary Oak (Gerardo del Valle) | medio, 204 Hz | muy expresiva, 20.4 semitonos | rápida, 3.27 pal/s | sube mucho al fanfarronear («¡te voy a destrozar!») |
| Giovanni (Alejandro Villeli) | grave, 139 Hz | expresiva, 17.2 semitonos | rápida, 3.42 pal/s | el registro más grave de todo el reparto: villano serio |
| Delia Ketchum (Patricia Hannidez) | agudo, 247 Hz | muy expresiva, 22.5 semitonos | normal, 2.76 pal/s | sube mucho al preocuparse por Ash |

✅ (medido directamente del audio con `voz.py`, no de oído ni de memoria).
Nota para la lámina: si se necesita elegir **quién suena más "de cómic"**
para un texto exagerado, Meowth y Jessie son los de más semitonos; para un
texto sereno (p. ej. una instrucción de #autoroles dicha por Oak), su
registro medio y su expresividad más baja encajan mejor que Ash o Misty.

---

## 4 · Detrás de cámaras del doblaje: curiosidades verificadas (punto 12)

Todo esto sale de la sección «Datos de interés» de la página `Pokémon` en
Doblaje Wiki (fuente primaria: entrevistas del propio director, Gerardo
Vásquez, en su canal de YouTube «Leyendas del doblaje» y en el podcast
«IDZI'S CUT»). Es interno a un solo sitio pero cita entrevistas concretas,
así que lo marco ✅ cuando la propia página cita la entrevista por su nombre,
y ⚠️ cuando es un comentario suelto sin more contexto.

- **Casting sin audición para varios**: Gerardo Vásquez asignó directamente
  (sin que hicieran prueba) a Gabriel Gama como Brock, y a Diana Pérez y José
  Antonio Macías como Jessie y James — aunque Diana había hecho audición para
  Misty y José Antonio para el narrador, y no quedaron ✅ (entrevista citada:
  Gerardo Vásquez con Georgina Sánchez, [Facebook](https://www.facebook.com/TorreADoblaje/videos/2529980197313586)).
- **Diana Pérez también hizo prueba para Delia Ketchum** (la madre de Ash) y
  no quedó: se la dieron a Patricia Hannidez ✅ (misma entrevista).
- **Ash casi lo dobla otro actor**: Gabriel Ramos contó en una entrevista de
  radio de anime que el papel de Ash **iba a ser de Víctor Ugarte** en un
  principio ⚠️ (una mención, sin la entrevista completa enlazada).
- **Renuncia por no poder improvisar**: José Antonio Macías (James) contó que
  quisieron dejar la serie —él y Gerardo Vásquez (Meowth/director)— cuando
  ya no los dejaron meter diálogos improvisados; después los recontactaron y
  les permitieron improvisar «de manera paulatina» ✅ (canal de YouTube
  Leyendas del doblaje).
- **Xóchitl Ugarte no supo que era su última grabación como Misty**: nadie,
  ni el director en turno, se lo avisó ⚠️ (comentario suelto de Xóchitl en el
  mismo programa).
- **El "voice-over" de Pikachu cuando habla**: técnica de doblaje donde la
  voz doblada se **sobrepone** a la original en vez de reemplazarla (se
  escuchan las dos, la doblada más alta) — así hablan Pikachu, Meowth y el
  resto de Pokémon parlantes en la versión hispanoamericana ✅. Ejemplo dado
  por la propia wiki: episodio 9 («La escuela de los golpes duros»), toda la
  voz de Pikachu en la versión internacional (y por tanto en la latina) es de
  la actriz estadounidense Rachael Lillis, no de Ikue Ōtani, salvo una línea
  ⚠️ (dato técnico, una sola fuente).
- **Tres episodios nunca doblados al español** (ni a ningún idioma fuera de
  Japón, por censura):
  - **Ep. 18, "Beauty and the Beach"** (temp. 1): escena de concurso de
    bikinis; se emitió como especial y luego se excluyó de DVD y del resto
    del mundo — pero, según Diana Pérez, **sí llegó a doblarse** en su
    momento porque el elenco recibía episodios japoneses antes del corte de
    4Kids (ver el hallazgo del punto 2) ✅.
  - **Ep. 35, "La leyenda de Dratini"** (temp. 1): censurado por uso
    excesivo de armas ✅.
  - **Ep. 38, "El guerrero de computadora Porygon"** (temp. 1): el episodio
    que provocó ataques epilépticos a más de 700 niños en Japón en 1997 por
    los destellos rojo/azul del Impactrueno de Pikachu; nunca se distribuyó
    ni dobló fuera de Japón, por petición de Nintendo ✅ (dato ya conocido
    mundialmente, coincide con lo que dice Doblaje Wiki).
- **Karaoke de "Pokémon Karaokémon"**: al inicio de la temporada 3 en Cartoon
  Network, estos segmentos se emitían en inglés (letra en inglés incluida);
  luego se doblaron al español pero **sin subtítulos de karaoke**, perdiendo
  el sentido del segmento ⚠️ (una fuente).

**Para «Lo que ama el fandom» (sección 14 de la biblia)**: estas anécdotas de
casting (el actor que casi fue Ash, la renuncia por no poder improvisar, el
"voice-over" de Pikachu) son justo el tipo de dato de doblaje que un servidor
de doblaje disfruta — mejor material que un meme genérico para un canal de
#autoroles si algún día se hace una lámina 2 sobre el doblaje.

---

## 5 · Punto 20 — Gustos y detalles de cada personaje

De Bulbapedia (ficha e Trivia, en inglés, la wiki con más detalle verificado
para el anime) y de la Pokédex oficial en español ya citada en la biblia.

**Ash Ketchum**
- Altura: **alrededor de 4'7" (140 cm)** ✅ ([Bulbapedia, cita la web oficial
  japonesa de Pokémon Day, tip #65, archivada](https://web.archive.org/web/20210219050737/https://pokemonday.pokemon.co.jp/tips/065/)).
- Diseñado por **Atsuko Nishida** (la misma diseñadora de Pikachu) ✅
  ([Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Ash_Ketchum), cita un
  comunicado de prensa de "Hometown Story").
- Su movimiento favorito es **Impactrueno (Thunderbolt)**, lo dice él mismo
  en el episodio *Climbing the Walls!* (XY025) ✅.
- Sabe **dibujar** (dibujó un Dewgong en DP089) y es buen **trepador** ✅.
- Quería empezar con **Squirtle**, pero Oak le dijo que se lo había llevado
  «un entrenador que no llegó tarde» (Gary) ✅ — ya estaba en la biblia con
  otra fuente (la película), ahora con Bulbapedia como 2ª fuente indirecta.
- Nunca envejece «de canon»: sigue teniendo 10 años en material promocional
  reciente aunque han pasado años narrativos ✅ (esto es más del punto 25,
  mundo, lo dejo apuntado para quien lo escriba).
- ⚠️ **No encontré** cumpleaños, comida favorita ni color favorito oficiales
  para Ash: a diferencia de personajes de otras franquicias (con databooks
  fijos), el anime de Pokémon no publica una ficha de ese tipo para los
  humanos. Un resultado de búsqueda decía «22 de mayo, 1.65 m, 54 kg, verde
  oscuro, básquetbol» pero **no lo pude verificar en Bulbapedia ni en ninguna
  fuente primaria** (el 22 de mayo coincide, sospechosamente, con el
  cumpleaños real de la actriz Patricia Hannidez, así que probablemente es un
  error de una IA de búsqueda mezclando datos). **No lo uses.**

**Misty**
- Su título de Líder de Gimnasio en japonés es **「おてんば人魚」** («La sirena
  traviesa/marimacha») ✅ ([Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Misty)).
- En los juegos (Amarillo) su frase de combate en japonés es su propia
  muletilla del anime: **«¡Vamos, mi constancia!»** (いくわよ！マーイステディ！)
  ✅ — un guiño directo del videojuego al anime.
- Le teme a los Pokémon tipo Bicho (ya estaba en biblia, lo confirmo: es dato
  constante en toda la serie, TV Tropes y Bulbapedia coinciden ✅).
- Aficiones: coleccionar Pokémon de agua, la pesca; su sueño es ser la mejor
  Maestra Pokémon de tipo Agua ✅ (ficha de AniList en `datos-voz.md` +
  Bulbapedia).
- ⚠️ No encontré cumpleaños oficial ni color favorito verificable.

**Brock**
- Aficiones reales, de su propia ficha: **buscar fósiles en el Monte Moon,
  cocinar** (para gente y para Pokémon), **pescar, coser y limpiar** ✅
  ([Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Brock_(anime))).
- Quiere ser **Criador Pokémon** (Pokémon Breeder), no entrenador de gimnasio
  — se lo dice a Ash desde el capítulo 1 ✅.
- Manía reconocida: **se enamora a primera vista** de casi toda mujer que
  conoce, y Misty (y luego otros compañeros) lo arrastran de la oreja para
  cortarlo ✅ (rasgo constante, TV Tropes, Bulbapedia).
- ⚠️ No encontré comida favorita propia (cocina de todo) ni cumpleaños oficial.

**Jessie**
- Le encantan los Pokémon **tipo veneno y con forma de serpiente**: tuvo un
  Arbok y luego un Seviper ✅ ([Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Jessie)).
- Es **vanidosa**: se enfurece si alguien le daña el pelo o la cara, y
  **odia que la llamen vieja** (en el ep. *The Battling Eevee Brothers*,
  Misty la llama «vieja bruja» / *oba-san* y Jessie explota) ✅.
- Sueño (en distintos arcos): ser una **Coordinadora Pokémon** de primer
  nivel — le sale mejor que robar Pokémon ✅.
- Rivalidad de toda la vida con **Cassidy**, otra agente del Equipo Rocket ✅.

**James**
- **Colecciona tapas de botella (bottle caps)** raras desde niño ✅
  ([Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/James)).
- Viene de una **familia rica**; se unió al Equipo Rocket para escapar de un
  matrimonio arreglado con **Jessebelle** ✅.
- **Odia que lo llamen viejo**, igual que Jessie ✅.
- Manía recurrente: **lo estafa siempre el mismo vendedor de Magikarp**, pese
  a que ya desconfía de él ✅.
- Le gustan las bebidas gaseosas: en un episodio se dice que «ha tomado
  suficiente refresco como para hacer flotar un portaaviones» ✅ (trivia
  literal de Bulbapedia).
- Se disfraza mucho: imita a la Enfermera Joy, la Oficial Jenny, al propio
  Profesor Oak y a otros personajes famosos de la serie ✅.

**Meowth**
- Es el **único Meowth (de los suyos) que aprendió a hablar y a caminar en
  dos patas**, imitando a los humanos para impresionar a una Meowth de la
  que se enamoró de joven ✅ (origen ya conocido, Bulbapedia/Pokémon Wiki).
- Fue elegido para el papel **sin audición**, directamente por Gerardo
  Vásquez, quien también lo dobla ✅ (punto 4).

**Profesor Oak**
- **Escribe senryū** (poesía japonesa corta) sobre Pokémon y las recita al
  cerrar sus lecciones; llegó a publicar un libro de poemas en el anime — ya
  estaba en la biblia, lo confirmo con Bulbapedia y TV Tropes ✅ (dos
  fuentes ya citadas).
- Cómo se ve a sí mismo: se describe como «demasiado viejo» para completar su
  sueño de la guía Pokédex completa, y recuerda con nostalgia cuando era «un
  buen entrenador» — ya citado con fuente de juego, lo confirmo ✅.

**Pikachu (el de Ash)**
- Le encanta el **kétchup** (ya en biblia) ✅.
- **Rechazó evolucionar** a Raichu con la Piedra Trueno porque quería demostrar
  su fuerza sin ayuda — sigue con **una fuente** (TV Tropes): busqué una
  segunda fuente en Bulbapedia y en Pokémon Wiki, y ambas repiten el mismo
  hecho sin nueva fuente primaria citada, así que **sigue ⚠️** aunque es un
  hecho muy repetido en el fandom.
- Duerme sobre el hombro o la cabeza de Ash y odia la Pokébola — ya ✅.

---

## 6 · Punto 21 — Por qué la gente ama la serie

**Encuestas y datos de ventas/premios**
- **Encuesta oficial *Pokémon of the Year 2020* (mundial)**: ya está en la
  biblia (sección 9) con Greninja 1.º, Charizard 4.º y Pikachu 19.º ✅. La
  reutilizo aquí sólo para la lectura de «por qué la aman»: **el favorito
  mundial no es Pikachu ni Ash**, es un Pokémon de una generación posterior,
  lo que confirma que el cariño al elenco original **es nostalgia
  específicamente latina/hispana**, no un dato universal.
- **Pokémon favorito por país en Latinoamérica** (estudio de búsquedas en
  Google, The Toy Zone con datos de Ahrefs, recogido por prensa
  especializada): **Chikorita** es el más buscado en México, El Salvador y
  Perú; **Vaporeon** en Argentina, Colombia y Uruguay; **Abra** en Bolivia,
  Ecuador, Panamá y Guatemala ⚠️ (metodología de una sola fuente, con eco en
  dos medios) — [3DJuegos LATAM](https://www.3djuegos.lat/nintendo-switch/chikorita-pokemon-favorito-mexico-pikachu-popular-mundo-este-estudio-revela-popularidad-pokemon-todo-planeta),
  [SensaCine México](https://www.sensacine.com.mx/album/album-1000104421/).
  Esto **llena parcialmente** el hueco de «no hay encuesta latinoamericana»
  que dejó la primera pasada (sección 9): sigue sin haber una encuesta oficial
  de **personajes humanos** en Latinoamérica, pero sí hay una de Pokémon por
  país, y confirma que el gusto regional **no** sigue al ranking mundial.
- **Fans latinos agradeciendo en masa a Gabo Ramos** cuando dejó de doblar a
  Ash en 2009 y de nuevo cuando *Viajes Pokémon* cerró la historia del
  personaje en 2023: ya estaba apuntado en biblia (sección 14) con Infobae;
  confirmo con una segunda fuente ✅ ([La República](https://larepublica.pe/animes/2022/11/14/pokemon-por-que-gabo-ramos-dejo-de-doblar-al-personaje-del-anime-actor-aclaro-misterio)).
- **26 años de vigencia**: la franquicia sigue gustando por su música, el
  salto fiel del videojuego a la animación y el diseño «adorable pero con
  chispa» de Pikachu, según análisis de prensa especializada en español ⚠️
  (una fuente, [Nintenderos](https://www.nintenderos.com/2023/02/saga-de-pokemon-26-anos-despues/)).

**Con qué personaje se identifica el público**
- El propio Ash es el personaje de identificación «oficial» (protagonista),
  pero la prensa y el fandom coinciden en que el cariño real y sostenido va
  también a **Gabo Ramos como actor** (la voz, no sólo el personaje): la
  gente llora la salida del actor casi como la del personaje mismo ✅ (Infobae,
  La República — mismas fuentes de arriba). Esto es un dato **específico de
  doblaje** que otras biblias del servidor no van a tener: vale la pena
  destacarlo para #autoroles si se usa la voz de Ash o de Oak en el texto.

**Escenas que hacen llorar (capítulo, qué pasa, por qué duele)**
- **"Pikachu's Goodbye"** (EP039, temporada 1, Indigo League; estrenado en
  Japón el 16-abr-1998, en EE.UU. el 20-nov-1998) ✅. Ash cree que Pikachu
  estaría mejor con una manada de Pikachu salvajes que encuentran en el
  bosque; tras rescatarlos del Equipo Rocket, Ash deja que Pikachu decida
  quedarse con los suyos — Pikachu, llorando, elige volver con Ash. Aparece
  en casi todos los rankings de «momentos más tristes» de la serie: SYFY,
  MovieWeb, CBR, Ranker, WatchMojo, TheTopTens la citan entre las primeras
  posiciones ✅ ([SYFY](https://www.syfy.com/syfy-wire/the-10-saddest-moments-in-pokemon-history-ranked),
  [CBR](https://www.cbr.com/saddest-pokemon-episodes-worse-as-adult/)). Tiene
  su propia canción, **"The Time Has Come (Pikachu's Goodbye)"**, usada en el
  montaje final de despedida (dato para quien escriba el punto 9, música).
  ⚠️ No la vi en video (no está en Dailymotion ni Internet Archive con audio
  latino que encontrara); el resumen sale de Bulbapedia y de las listas de
  prensa, no de haberla mirado.
- **La despedida de Butterfree** (temporada 1: Ash libera a su Butterfree
  para que se vaya con una bandada y una Butterfree rosa de la que se
  enamora): otro de los momentos más citados como «el que me hizo llorar de
  niño» en Reddit y en listas de prensa ✅ (varias listas de arriba la
  incluyen; hilos de Reddit r/pokemon con comisiones de arte y hasta un
  pastel de cumpleaños dedicados a «el Charmander abandonado» y a escenas
  tristes del anime, ver bitácora).
- **Reddit r/pokemon, hilos reales** (vía Arctic Shift, ya que reddit.com
  puede fallar): pregunta «*what is the saddest pokemon episode you've ever
  seen?*» y variantes tienen **años de respuestas activas**; el hilo
  «*Probably the saddest episode*» tiene **513 votos** y «*Episode 18 is the
  saddest*» tiene **195 votos** ✅ (aunque ese «episodio 18» es un número de
  temporada distinto al EP018 clásico — no es el mismo que "Beauty and the
  Beach" del punto 2 — no confirmé a cuál se refiere exactamente, lo dejo
  como referencia de que el tema genera mucha conversación, no como cita de
  un capítulo concreto) — [hilo 513 votos](https://reddit.com/r/pokemon/comments/nvc3vu/probably_the_saddest_episode/),
  [hilo 195 votos](https://reddit.com/r/pokemon/comments/fjo027/episode_18_is_the_saddest/).

---

## 7 · Punto 22 — Fan dubs y comunidad hispana

**Fandubs de aperturas (openings) en español**
- Varios canales de YouTube/Dailymotion suben covers/fandubs de los openings
  latinos: *"Pokemon XY & Z Opening Fandub Español Latino"* (Homero Lezama y
  Yeke, con instrumental en SoundCloud) y *"Pokemon XY Opening 1 (Español
  Latino Fandub)"* (canal V Volt) ✅ — [SoundCloud](https://soundcloud.com/lezzamamusic/pokemon-xy-z-opening-instrumental-cover-by-katz-yeke),
  [YouTube](https://www.youtube.com/watch?v=A_MfEZ3COBc).
- En Dailymotion (`datos-voz.md`) hay openings oficiales resubidos en calidad
  HD por fans (feRz28: OP1 "Atrápalos Ya", OP2 "Liga Naranja", OP18) y
  fandubs propiamente dichos de escenas de películas ("Pokémon: Detective
  Pikachu - Tráiler español", FilmAffinity, 769 vistas).

**Fandub de una escena completa (parodia), verificado con `voz.py`**
- *"Pikamon (Pokémon Parody) [Spanish Fandub]"* (canal Allred Nicole,
  Dailymotion) — https://www.dailymotion.com/video/x381tx0. Transcribí el
  audio: es una **parodia para adultos** (lenguaje explícito, chistes
  sexuales sobre Ash y Pikachu) ⚠️ **contenido no apto para la lámina**, pero
  real y es exactamente el tipo de «parodia hispana» que pide el punto 22.
  **Aviso para el dueño**: existe este tipo de fandub, pero no debería
  citarse ni enlazarse en la lámina pública de #autoroles por su contenido.
- Otros fandubs de escenas encontrados (no revisados con `voz.py` por tiempo):
  *"Pokémon PARECIDOS a Humanos Fandub Español Latino"* (BrokenMOJO),
  *"Pokémon First Movie Fandub"* (carmen1994able), *"Pokemon CASTIGADA!
  Fandub Latino"* — todos en YouTube, sin ver contenido, ⚠️.

**Memes y comparación de doblajes (España vs. Latinoamérica)**
- El lema del Equipo Rocket es el tema más repetido en TikTok hispano: hay
  compilados de «Mejores frases del Equipo Rocket» y homenajes a los actores
  con miles de reproducciones (canal *Doblaje a la Mexicana*, ya citado en
  biblia) ✅.
- Encontré un TikTok que confirma el **reparto español (de España, no
  latino)** del Equipo Rocket para comparar: **Amparo Valencia** (Jessie),
  **Iván Jara** (James) y **José Escobosa** (Meowth) en el doblaje castellano
  ✅ ([TikTok](https://www.tiktok.com/@lavozdetuvida/video/7181873459322965254))
  — coincide con la columna «Voz Spanish» de AniList en `datos-voz.md` que ya
  traía esos mismos nombres para España. Útil para la sección de la biblia
  que compara «Pokébola» (latino) contra «Poké Ball» (España): el reparto
  también es distinto, no sólo el vocabulario.

---

## 8 · Popularidad: lo nuevo (punto 7)

Ya cubierto en profundidad por la sección 9 de la biblia (Pokémon of the
Year, encuesta japonesa, Corea, iniciales). Lo que aporto aquí es **específico
de Latinoamérica** (el hueco que la propia biblia marcaba en su punto 20 «Lo
que no pude verificar»):
- **Pokémon favorito por país en Latinoamérica** (ver punto 6 arriba): llena
  parte del hueco, aunque es sobre especies de Pokémon, no sobre los
  personajes humanos (Ash, Misty, Brock...) ⚠️.
- Sigo **sin encontrar** una encuesta oficial o de fans, amplia, sobre
  personajes humanos específicamente en Latinoamérica (Ash vs. Misty vs.
  Brock vs. Team Rocket). Busqué en español «encuesta popularidad personajes
  Pokémon Latinoamérica», «quién es el personaje favorito de Pokémon en
  México/Argentina», sin resultado directo. Lo que sí hay, y es fuerte, es el
  cariño **al actor de doblaje** más que al personaje en abstracto (ver
  punto 6): eso puede sustituir a una encuesta que no existe.

---

## Lo mejor para la lámina

1. **La voz de Oak repite su propia muletilla en dos doblajes distintos, 20
   años aparte**: «hay un problema con este último» (muestra de Doblaje Wiki)
   y «debo avisarte de que hay un problema con este último» (película 2017).
   Si Oak habla en la lámina, esta frase es su firma real, no inventada.
2. **El tráiler oficial de "¡Yo te elijo!" en Dailymotion da, con minuto y
   enlace, la frase más icónica** («vamos a ser los mejores amigos») sin
   depender de YouTube.
3. **El hallazgo del capítulo 18 doblado** (el episodio prohibido) es un dato
   único para un servidor de doblaje: nadie más lo va a tener en su
   documentación de fan.
4. **Meowth es, medido, el personaje que más sube y baja de tono** (25.6
   semitonos): si se necesita un personaje "cómico" hablando en un cuadro de
   diálogo, su registro es el más expresivo de todo el reparto.
5. El **cariño real en Latinoamérica es al actor, no sólo al personaje**
   (Gabo Ramos): un texto de agradecimiento a "quien nos prestó su voz" pega
   más con el espíritu del servidor que una frase genérica del personaje.

---

## No encontré

- ⚠️ Cumpleaños, comida y color favoritos **oficiales** de Ash, Misty y Brock
  como personajes de anime (no existen en Bulbapedia ni en fuente primaria;
  un resultado de búsqueda que los daba no se pudo verificar y probablemente
  mezcla datos de otra persona — ver punto 5). Busqué: «Ash Ketchum ficha
  cumpleaños altura Bulbapedia», «Misty altura cumpleaños signo», «Brock
  edad aficiones comida favorita».
- ⚠️ Quién dobla la voz de la Pokédex y de «¿Quién es ese Pokémon?» en la
  mayoría de temporadas (sólo until encontré a Rubén León para 3 episodios
  puntuales de la temporada 3, no para el resto). Ya estaba como «no
  encontrado» en la primera pasada; sigue sin aparecer.
- ⚠️ Encuesta de popularidad de **personajes humanos** específica de
  Latinoamérica: no existe o no la indexan los buscadores (ver punto 8).
  Esto **no es obligatorio del encargo** (pide «encuestas oficiales y de
  fans», y sí las hay, sólo que mundiales/japonesas, ya cubiertas en la
  biblia): lo marco como extra que no se pudo profundizar más, no como algo
  pendiente.
- ⚠️ Vistas exactas y canal verificado de varios fandubs de TikTok/YouTube
  (punto 22): la red cerrada a YouTube por login impide sacar el contador de
  vistas real; Dailymotion sí da vistas (ya puestas en `datos-voz.md`), pero
  ahí los fandubs propiamente hispanos son pocos comparado con YouTube.
- ⚠️ Resolución de la contradicción Ana Lobo/Claudia Motta en el episodio 17
  (punto 2): necesita oír el episodio, que no encontré en Dailymotion ni
  Internet Archive.
- ⚠️ El «episodio 18» de los hilos de Reddit con más votos (punto 6): no es
  seguro que sea el mismo "Beauty and the Beach" del punto 2 (los hilos no
  traen selftext claro sobre a qué numeración se refieren). No lo presento
  como el mismo hecho.

---

## Bitácora de búsqueda

**API directas (sin gastar cupo de buscador)**
- Doblaje Wiki, API `action=parse&prop=wikitext` sobre la página **`Pokémon`**
  (no sólo `Max (Pokémon)`, que había traído `recolectar.py`): ficha completa
  de reparto con muestras de audio, y sección «Datos de interés» con
  entrevistas citadas. Español.
- Doblaje Wiki, API sobre `imageinfo` para sacar la URL real de 11 archivos
  `.ogg` de muestra (`static.wikia.nocookie.net`), descargados y
  transcritos con `herramientas/voz.py --idioma es`.
- Bulbapedia, API `action=parse&prop=wikitext` (por secciones, con
  `prop=sections` primero) sobre `Ash_Ketchum`, `Misty`, `Brock`, `Jessie`,
  `James` — inglés, «Character» y «Trivia» de cada uno.
- Bulbapedia, `EP018` y `EP039` (`Pikachu's Goodbye`) para fechas y sinopsis.
- Wikipedia en español, API `action=query&list=search` y `action=parse` —
  confirmar fecha de estreno en Cartoon Network Latinoamérica (con `curl -G
  --data-urlencode` porque los acentos rompían la URL directa; luego di con
  rate limit y no insistí más de dos veces, según la regla de AYUDANTE.md).
- Dailymotion, API `videos?search=...` para encontrar clips con diálogo real
  (no sólo openings): encontré el tráiler oficial y el post-créditos de
  *¡Yo te elijo!*.
- Internet Archive, `advancedsearch.php?q=title:(pokemon) AND language:(spa)`
  — encontré el capítulo 18 doblado (punto 2).
- Arctic Shift (`arctic-shift.photon-reddit.com/api/posts/search`) sobre
  r/pokemon con `title=saddest episode`: 10 resultados reales con score y
  permalink. Un segundo intento (para leer el `selftext`) dio **rate limit**
  ("Timeout. Maybe slow down a bit") dos veces seguidas; no insistí más,
  según la regla de "no más de dos intentos" de AYUDANTE.md.

**Buscador web** (de un cupo de ~50; usé 13 en total para este rol)
- Español: «Gerardo del Valle Gary Oak Pokémon doblaje voz», «Giovanni
  Pokémon doblaje latino actor de voz Alejandro Villeli», «Patricia Hannidez
  Delia Ketchum Pokémon doblaje», «Bernardo López traductor Pokémon doblaje
  mexicano», «Ana Lobo Pikachu Yo te elijo voz película doblaje», «encuesta
  popularidad personaje favorito Pokémon Latinoamérica fans», «Pokémon
  estreno Cartoon Network Latinoamérica 6 de septiembre de 1999», «¡a la
  carga! Ash Ketchum frase doblaje Pokémon Gabo Ramos», «fandub español
  latino Pokémon opening cover youtube canal», «meme Pokémon latino a la
  carga Equipo Rocket doblaje viral tiktok», «por qué la gente ama Pokémon
  anime reseñas encuestas ventas premios».
- Inglés: «Ash Ketchum ficha cumpleaños altura color favorito comida
  Bulbapedia databook» (mixto es/en), «Misty Kasumi altura cumpleaños signo
  color favorito ficha Bulbapedia», «Brock Takeshi ficha edad altura
  aficiones comida favorita Bulbapedia», «Pokémon escena que hizo llorar a
  todos Butterfree despedida capítulo reddit», «"Pikachu's Goodbye" saddest
  Pokemon episode ranked list».
- No busqué en japonés ni coreano/chino para este rol: los puntos 20-22 son
  específicamente sobre el público hispano y el doblaje latino; el carácter
  y las voces originales japonesas ya estaban cubiertos en la primera pasada
  (biblia, secciones 8 y 10) citando Bulbapedia y TV Tropes.

Sigue: nada obligatorio pendiente de mis puntos (7, 8, 12, 13 confirmados en
dos fuentes donde se pudo, con lo dudoso marcado; 20, 21 y 22 con hallazgos
nuevos y fuentes). Lo que falta son extras ya listados en «No encontré», no
huecos del encargo.
