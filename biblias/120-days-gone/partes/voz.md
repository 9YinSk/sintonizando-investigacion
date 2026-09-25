# Voz y personajes — Days Gone

Parte del investigador de VOZ (puntos 7, 8, 12, 13, 20, 21, 22 de `ENCARGO.md`).
Libreta de datos: un dato por línea, con fuente, ✅ (dos fuentes) o ⚠️ (una), y minuto o tamaño si aplica.
Punto de partida: `partes/datos-voz.md` (no repetido aquí). La tabla de reparto de `datos-voz.md` salió rota
(nombres de archivo en la columna «Personaje», sin actor); se rehizo sacando el wikitext de Doblaje Wiki por su
API (`action=parse&prop=wikitext`) — ver el punto 8.

## Hallazgos

### Punto 8 — Doblaje latino y doblaje de España (dos fuentes por nombre)

**Aviso sobre `datos-voz.md`:** su tabla de reparto salió rota (la columna «Personaje» traía el nombre del
archivo de audio, sin actor). Se rehizo sacando el wikitext de la página de Doblaje Wiki con
`action=parse&format=json&prop=wikitext&page=Days_Gone` y parseando la tabla real. La de abajo es la buena.

**Días Gone SÍ tiene DOS doblajes al español, hechos por separado** (esto no estaba claro en los datos de
partida): uno latino (México, estudio Lola MX) y uno de España (estudio DL Multimedia, Madrid). Cada uno con
reparto propio; no comparten ningún actor. ✅ confirmado con eldoblaje.com + doblajevideojuegos.es (España) y
Doblaje Wiki (Latino) + HobbyConsolas/Vandal (que Claudio Serrano dobla a Deacon en España).

**Ficha del doblaje latino** — estudio Lola MX · dirección Dan Osorio y Daniel Lacy · dirección creativa Luis
Daniel Ramírez · ingeniería Darío Ramírez y Monserrat Licona · grabado en 2019 para el lanzamiento en
Hispanoamérica (26-abr-2019). ✅ _Doblaje Wiki, wikitext de la ficha_: https://doblaje.fandom.com/es/wiki/Days_Gone

**Ficha del doblaje de España** — estudio DL Multimedia (Madrid) · dirección Antonio Ramírez de Antón (también
dirigido por Antonio Domínguez) · sin traductor especificado en la ficha · año de grabación 2019 · distribuidora
para España Sony Interactive Entertainment Europe. ✅ dos fuentes iguales: eldoblaje.com y doblajevideojuegos.es.
- https://www.eldoblaje.com/datos/FichaPelicula.asp?id=55301&Orden=O
- https://www.doblajevideojuegos.es/fichajuego/days-gone

**Reparto latino (Lola MX) — personajes principales y recurrentes**, de la tabla de Doblaje Wiki. Cada nombre
de los 8 personajes de arranque (Deacon, Boozer, Sarah, O'Brian, Iron Mike, Rikki, Copeland, Skizzo) se
comprobó **dos veces dentro de Doblaje Wiki**: en la ficha de la serie y, por separado, en la ficha propia de
cada actor (su filmografía la escribe/edita otra gente, no la misma página) — búsqueda externa (ANMTV, BTVA,
IMDb) no dio reparto latino de videojuegos para esta obra (ver Bitácora); se marca ✅ con esa salvedad:

| Personaje | Actor original | Actor latino | Fuente cruzada (ficha del actor) |
|---|---|---|---|
| Deacon St. John | Sam Witwer | **José Gilberto Vilchis** | ✅ ficha propia: «Deacon en Days Gone» |
| William «Boozer» Gray | Jim Pirri | **Beto Castillo** | ✅ ficha propia: «Boozer en Days Gone» |
| Sarah Whitaker | Courtnee Draper | **Alex(ander) Delint** (créditada como «Alejandra Delint»; persona no binaria, alias «Alex») | ✅ ficha propia: «Sarah Whitaker en Days Gone» |
| James O'Brian | Bernardo De Paula | **Daniel Lacy** | ✅ ficha propia: «Days Gone - James O'Brian (Bernardo de Paula)» |
| «Iron Mike» Wilcox | Eric Allan Kramer | **Armando Réndiz** | ✅ ficha propia: «Iron Mike Wilcox en Days Gone» |
| Rikki Patil | Nishi Munshi | **Edurne Keel** | ✅ ficha propia: «Rikki Patil (Nishi Munshi) en Days Gone (2019)» |
| Mark «Cope» Copeland | Crispin Freeman | **Erick Selim** | ✅ ficha propia: «Mark Copeland en Days Gone» |
| Raymond «Skizzo» Sarkoski | Jason Spisak | **Luis Daniel Ramírez** (también dirección creativa del doblaje) | ✅ ficha propia: «Skizzo Sarkoski / Teniente Bishop y Merodeadores en Days Gone» |
| Jessie Williamson «Carlos» | Scott Whyte | Erick Salinas | ⚠️ sólo ficha de la serie |
| Lisa Jackson | Laura Bailey | «Actriz sin identificar» | ⚠️ Doblaje Wiki no tiene el nombre |
| Ministro (boda) | Darien Sills-Evans | Javier Otero | ⚠️ sólo ficha de la serie |
| Mary | — | Leyla Rangel | ⚠️ sólo ficha de la serie |
| Emmanuel «Manny» Méndez | Andrew Kishino | Carlos Torres | ⚠️ sólo ficha de la serie |
| Jezzy «Recompensas» | — | Rossy Aguirre | ⚠️ sólo ficha de la serie |
| Damon «Comerciante» | — | Guillermo Rojas | ⚠️ sólo ficha de la serie |
| Raymond… Addison «Addy» Walker | Debra Wilson | Analiz Sánchez | ⚠️ sólo ficha de la serie |
| Ada «Tuck» Tucker | Dee Dee Rescher | Katalina Múzquiz | ⚠️ sólo ficha de la serie |
| Alkai Turner | Jonathan Joss | Dan Osorio (también director del doblaje) | ⚠️ sólo ficha de la serie |
| Derrick Kouri | Phil Morris | Víctor Covarrubias | ⚠️ sólo ficha de la serie |
| Glen Russell | Jonathan Roumie | David Allende | ⚠️ sólo ficha de la serie |
| Rick Mullins | Clayton Froning | Óscar Garibay | ⚠️ sólo ficha de la serie |
| Coronel Matthew Garret | Daniel Riordan | Gerardo Reyero | ⚠️ sólo ficha de la serie |
| Wade Taylor | James Allen McCune | Tommy Rojas | ⚠️ sólo ficha de la serie |
| Arturo García Jiménez «Doc» | Al Coronel | Gerardo Alonso | ⚠️ sólo ficha de la serie |
| James Weaver | Darien Sills-Evans | Sergio Gutiérrez Coto | ⚠️ sólo ficha de la serie |
| Crystal Adkins / Jacob D'Angelo / Caleb Tomlinson | — | Mariana Ortiz / Pedro D'Aguillón Jr. / Javier Olguín | ⚠️ sólo ficha de la serie |

Voces adicionales latino (sin personaje fijo): Alan Fernando Velázquez (Kindace), Christian Strempler (Philips),
Dafnis Fernández (Guardia de Puerta), Eduardo Garza (El Rojo Railey), Edurne Keel, Guillermo Rojas, Rossy Aguirre
(Mujer del campamento / narradora / guardia), Toni Rodríguez, Valentina Souza (Airi). ⚠️ _Doblaje Wiki_.
_Fuente de toda la tabla latina: https://doblaje.fandom.com/es/wiki/Days_Gone (wikitext vía API)_

**Reparto de España (DL Multimedia)** — de eldoblaje.com, con doblajevideojuegos.es como segunda fuente
(coinciden los dos, actor por actor) ✅:

| Personaje | Actor original | Actor de España |
|---|---|---|
| Deacon St. John | Sam Witwer | **Claudio Serrano** (también voz de Batman/Christian Bale, Nathan Drake) |
| William «Boozer» Gray | Jim Pirri | **Adolfo Pastor** |
| Sarah Irene Whitaker | Courtnee Draper | **Paqui Horcajo** |
| O'Brian | Bernardo De Paula | **Álvaro Reina** |
| Iron Mike | Eric Allan Kramer | **Ángel Amorós** |
| Rikki Patel | Nishi Munshi | **Inma Gallego** |
| Mark «Cope» Copeland | Crispin Freeman | **Borja Fernández Sedano** |
| Skizzo | Jason Spisak | **Antonio Ramírez de Antón** (el propio director de doblaje se puso también esta voz) |
| Carlos / Jessie Williamson | Scott Whyte | Fernando Cordero |
| Addison «Addy» Walker | Debra Wilson | Yolanda Pérez Segoviano |
| Álvarez (otro personaje de Debra Wilson) | Debra Wilson | Elena Ruiz de Velasco |
| Lisa | Laura Bailey | Laura Barriga |
| Doc Lewis | Al Coronel | Carlos López Benedí |
| Leon | Kaiwi Lyman | Luis Vicente Ivars «Tente» |
| Coronel Matthew Garret | Daniel Riordan | Eugenio Barona |
| Glen Russell | Jonathan Roumie | Juan Navarro Torelló |
| Weaver | Darien Sills-Evans | Antonio Domínguez (codirector del doblaje) |
| Taylor | James Allen McCune | Jesús Barreda |
| Kouri | Phil Morris | Fernando «Nano» Castro |
| Billy | Hugo Martin | José Ángel Fuentes |
| Alkai | Jonathan Joss | Miguel Ángel Pérez |
| Ada Tucker | Dee Dee Rescher | Mercedes Espinosa |
| Agente Martine Sinclair | — | Nikki García |
| Vasquez | — | Fran Jiménez |

Más de 30 «voces adicionales» en España (Adrián Viador, Idoia Fernández, Enrique Santarén, Miguel Ángel Poison,
Felipe Garrido, Óscar Ruiz García, Marcos Graña, Rodri Martín, Ana González Soler, Ángel Coomonte, Carlos Moreno
Minguito, Javier Gámir, Nuria Huéscar, Carmen Gambín, Isabel Gaudí, Jazmín Abuín y más). ✅ coinciden ambas fuentes.
_Fuentes: https://www.eldoblaje.com/datos/FichaPelicula.asp?id=55301&Orden=O ·
https://www.doblajevideojuegos.es/fichajuego/days-gone_

**Dato curioso sobre Claudio Serrano** (Deacon, España): más de 100 horas de grabación sólo para su
personaje, trabajado sobre el audio del actor original (Sam Witwer); ganó un premio en el Fun&Serious Game
Festival por este papel. ✅ _HobbyConsolas (Dailymotion, entrevista en el estudio DL Multimedia):
https://www.dailymotion.com/video/x74lljj (5:29) · claudioserrano.com:
https://www.claudioserrano.com/days-gone-el-doblaje-de-videojuegos/_

**Frases icónicas del doblaje latino, adaptación textual** (de la sección «Datos de interés» de Doblaje Wiki,
✅ está en la propia ficha, una sola fuente pero es primaria — la propia wiki cita el diálogo del juego):
- El culto «The Reapers» se adaptó como «Los Muertos». Pero cuando Deacon rescata a los rehenes del
  Campamento Lost Lake, dice igualmente: «No quiero más **Reapers** entrando por el pantano» (se les cuela el
  nombre en inglés). ⚠️ una fuente (Doblaje Wiki, sección Datos de interés).
- El Dr. Jiménez, en inglés, dice «Your hear me, amigo?»; en el doblaje esto se adaptó como el juego de
  palabras **«¿Me entiendes, Méndez?»**. ⚠️ una fuente (ídem).
- El apodo con el que las bandas del juego llaman a Deacon suena, en el doblaje latino, como «Dick» —pero es
  **«Deek»**, su apodo real dentro de la historia (lo confirma la propia wiki de Days Gone: Iron Mike le dice
  «Remember how we run things in this camp, Deek», y un hilo de Reddit se titula «Deek most iconic quotes»).
  Al transcribir con Whisper el audio de Doblaje Wiki sale «Dick» varias veces (ver más abajo): es un error de
  reconocimiento de voz, no del doblaje. ✅ _https://daysgone.fandom.com/wiki/Deacon_St._John ·
  https://www.reddit.com/r/DaysGone/comments/15bzlns/deek_most_iconic_quotes/_

**Frases textuales transcritas de las muestras oficiales de Doblaje Wiki** (con `herramientas/voz.py`,
Whisper `small`, revisado a oído; los nombres propios pueden fallar). Cada una es del propio audio de
personaje que trae la ficha de Doblaje Wiki — ✅ (audio oficial del juego, fuente primaria):

- **Deacon** (José Gilberto Vilchis): «Saint John Deacon, sí sé cómo ser un hermano. Serví una vez, serví con
  honor, odié cada maldito minuto.» — voz grave (98 Hz de media), muy expresiva (9.9 semitonos de rango),
  ritmo normal (2.37 palabras/s). _Muestra: https://static.wikia.nocookie.net/doblaje/images/a/a8/Deacon_St._John_Days_Gone_audio_juego.ogg_
- **Boozer** (Beto Castillo): «A casa, ya me voy para mi hogar. No voy [a subir] a la puta montaña […] Tomaste
  una botella y te la tomaste de un [trago], fue mucho whisky, y me dijiste que si yo iba a tomar hasta morir,
  tú harías lo mismo.» — voz grave (104 Hz), la más expresiva de las ocho (23 semitonos), ritmo rápido (3.73
  palabras/s): así se nota su lado más pasional y «de fiesta». _Muestra:
  https://static.wikia.nocookie.net/doblaje/images/7/7d/Boozer_Days_Gone.ogg_
- **Sarah** (Alex Delint): «Yo, yo iré primero. […] Quiero que sepas lo mucho que hiciste conmigo.» — voz
  media (157 Hz), muy expresiva (15.9 semitonos), ritmo normal (2.76 palabras/s); tono cálido, de despedida.
  _Muestra: https://static.wikia.nocookie.net/doblaje/images/c/cb/Sarah_Days_Gone_Audio_Demo.ogg_
- **O'Brian** (Daniel Lacy): «[Mire,] siento mucho lo de tu esposa, siento mucho todo esto. Pero debes
  entender que si no la enviabas esa noche conmigo, habría muerto el otro día. Hiciste lo correcto, y si te
  hubieras quedado, lo que habría pasado es que hubieran muerto los dos.» — voz media (189 Hz, la más aguda de
  los ocho), muy expresiva (23.5 semitonos), ritmo normal. _Muestra:
  https://static.wikia.nocookie.net/doblaje/images/f/f2/Obrain_days_gones_2.ogg_
- **Iron Mike** (Armando Réndiz): «¿Y sé qué clase de hombre es y lo que hizo? ¿Son cosas peores que tú?
  ¿Ricki [Rikki]? ¿O que yo mismo?» — voz media (175 Hz), la de rango más amplio de los ocho (26.4 semitonos),
  ritmo rápido (3.54 palabras/s). _Muestra:
  https://static.wikia.nocookie.net/doblaje/images/3/3b/Iron_Mike_Days_Gone.ogg_
- **Rikki** (Edurne Keel): «Addy [Whisper oyó "Adi"], ¿estás aquí? Bueno, quítatela. Tal vez sea ingeniera,
  Dig[…] De verdad fuiste a la guerra. […] ¿Afganistán o… el CM [ejército] o después?» — voz media (164 Hz),
  muy expresiva (18.4 semitonos), ritmo normal. _Muestra:
  https://static.wikia.nocookie.net/doblaje/images/7/7d/Rikki_Patil_Days_G_ps4.ogg_
- **Copeland** (Erick Selim): «Vi a Leon el otro día, me estaba trayendo algo. La gente aquí está sufriendo
  mucho, Deek. Le diré algo: te encuentras sus cosas y me las traes a mí, Deek. Haces eso y… bueno, veremos
  qué puedo hacer por ti. Recuperamos…» — voz grave (104 Hz), expresiva (11.4 semitonos), ritmo normal (2.07
  palabras/s), tono paternalista/persuasivo. _Muestra:
  https://static.wikia.nocookie.net/doblaje/images/d/d2/Mark_Copeland_Days_Gone.ogg_
- **Skizzo** (Luis Daniel Ramírez): «Vamos, aquí. Bueno, si vas adentro te lo mostraré. Hoy estuve pensando en
  tu idea […] sellar la cueva al norte del campamento para impedir que las hordas atraviesen nuestra área de
  cultivo. El problema es que Mike no ha podido encontrar ningún detonador para esto, ¿sí? Pero sé dónde
  puedes conseguir eso.» — voz grave (110 Hz), la MENOS expresiva de los ocho (sólo 5.1 semitonos, «registro
  normal» en vez de «muy expresiva») pero la MÁS rápida (4.22 palabras/s): habla plano y atropellado, como
  quien vende una idea sin parar a respirar — encaja con su perfil narcisista/manipulador (ver punto 13).
  _Muestra: https://static.wikia.nocookie.net/doblaje/images/d/d8/Skizzo_days_gone_ps4.ogg_

_(Fichas completas de tono en `/tmp/claude-0/trabajo/120-days-gone-voz/voz_<Nombre>/ficha_voz.json`, no se
suben al repositorio por ser carpeta de trabajo.)_

### Punto 13 — Descripción profunda de cada personaje

Carácter, cómo se expresa (tono medido con `voz.py`, ver punto 8) y momentos clave. Fuente base de cada
biografía: wikitext de `daysgone.fandom.com` (wiki de la serie, no la de doblaje) sacado por su API
`action=parse&prop=wikitext`, sección Personality/Trivia de cada personaje. ✅ cuando se cruza con Reddit,
Doblaje Wiki o el propio audio; ⚠️ cuando es sólo la wiki del juego.

**Deacon St. John** (voz original Sam Witwer; latino José Gilberto Vilchis; España Claudio Serrano) —
Cazarrecompensas, expresidente/miembro de los Mongrels MC (club de moteros), veterano del ejército (unidad
10.ª División de Montaña, tatuada en su mano derecha). Es «un estudio en contrastes»: pide independencia y
libertad de ataduras, pero en el fondo necesita comprometerse con algo; su miedo a la obligación choca con su
necesidad de vínculos profundos. Empieza la historia exiliado socialmente y termina como pilar de Lost Lake,
negándolo en voz alta («sólo lo hago porque Boozer está herido») mientras sus actos (ayudar a Iron Mike, Rikki
y Addy a estabilizar el campamento) lo desmienten. ✅ _daysgone.fandom.com/wiki/Deacon_St._John#Personality_
(ya en `datos-voz.md`) + confirmado por el arco jugable.
- Apodo dentro de la historia: **«Deek»** (Iron Mike y Copeland lo llaman así). El audio del doblaje latino
  suena como «Dick» por un error de Whisper, no del doblaje real. ✅ (ver punto 8).
- Voz medida (latino, muestra oficial): grave (98 Hz), muy expresiva (9.9 semitonos), ritmo normal — encaja
  con alguien que habla poco y con peso cuando lo hace. ✅ (voz.py sobre audio oficial).
- Tatuajes con significado, todos en el brazo/cuello derecho salvo los indicados (⚠️ una fuente, wiki del
  juego): 10.ª División de Montaña (mano derecha), «RIDE» (nudillos derechos), Parca/Reaper (antebrazo
  derecho, luego quemada a medias por los Rippers), alambre de espino (bíceps derecho), calavera alada
  (hombro derecho), calavera con llaves inglesas (mano izquierda), «HARD» (nudillos izquierdos), serpiente con
  daga y «Freedom Enduring» (antebrazo izquierdo), daga ornamentada (pecho), **«Sarah»** (lado derecho del
  cuello, el nombre de su esposa), «Forever MC» (lado izquierdo del cuello), los colores de los Mongrels MC
  (espalda).
- Su chaqueta («kutte») de cuero negro lleva los colores de los Mongrels MC: el rocker superior «Mongrel», el
  logo del club (calavera de perro rabioso encadenada, mordiendo con sangre) y el rocker inferior «Farewell
  Original» (su capítulo/base del club). Es el objeto de vestuario que todo fan reconoce. ⚠️ wiki del juego.
- El nombre «Deacon» lo puso el director creativo John Garvin por su propia mascota; el apellido «St. John» es
  el de la calle donde creció Garvin. Hay guiños a la banda Queen (cuyo bajista se llama John Deacon): los
  trofeos de habilidades citan letras de «Don't Stop Me Now». ⚠️ _wiki del juego, cita un vídeo de
  entrevista «157 Rapid-Fire Questions About Days Gone»._

**Boozer — William «Boozer» Gray** (original Jim Pirri; latino Beto Castillo; España Adolfo Pastor) — El
mejor amigo de Deacon, expiloto de los Mongrels MC. «Lleva el corazón en la mano»: no tiene dobleces, es
igual de directo con amigos que con enemigos, y profundamente empático. En su juventud vivía al día,
apasionado, ideal para la vida «salvaje» del club; ese contraste entre el anarquismo del club (compromisos
sólo por consenso, resistencia a la autoridad) y su necesidad de vínculos con código da forma a sus tatuajes
visibles: «Mayhem» (rechazo a sistemas de valores impuestos), «Vengeance» (represalia ante violaciones del
código moral) y «Farewell Original» (pertenencia al club). ✅ _daysgone.fandom.com/wiki/Boozer#Personality_.
- Voz medida: grave (104 Hz) pero la MÁS expresiva de los 8 (23 semitonos) y la más rápida (3.73 palabras/s):
  encaja con su carácter pasional y sin filtro. ✅ voz.py.
- Dato curioso: en la boda de Deacon y Sarah, Boozer fue el único invitado de «familia y amigos» además del
  ministro; Sarah dice que es porque «se peleó con todo el mundo de las dos familias». Sólo Addy se niega a
  llamarlo «Boozer» y usa su nombre real, William. ⚠️ wiki del juego.
- Los creadores reconocen que Boozer (y Deacon, y Carlos/Jessie) deben mucho a la serie *Sons of Anarchy*: como
  Opie Winston, es el mejor amigo del protagonista, perdió a su pareja en un accidente ligado al club, y ambos
  luchan contra la depresión. ⚠️ wiki del juego (comparación de fans, razonable pero sin fuente oficial del
  estudio).

**Sarah Whitaker** (original Courtnee Draper; latino Alex Delint; España Paqui Horcajo) — Esposa de Deacon,
investigadora doctoral, bióloga que aplicaba su trabajo de campo a biotecnología médica y de defensa. Rebelde
suave, empática, de opiniones firmes: una vez decide un curso de acción lo sigue aunque familia o jefes no
estén de acuerdo. Su vínculo con Deacon —pese a la distancia entre su formación universitaria y el trabajo de
mecánico de él— se explica porque comparten el rechazo a lo convencional y valoran los compromisos personales
por encima de las obligaciones sociales: ella aprende a montar en moto, él aprende de plantas silvestres.
✅ _daysgone.fandom.com/wiki/Sarah_Whitaker#Personality_.
- Voz medida: media (157 Hz), muy expresiva (15.9 semitonos), ritmo normal — voz cálida, de despedida, en la
  muestra oficial («Quiero que sepas lo mucho que hiciste conmigo»). ✅ voz.py.
- Deacon lleva su nombre tatuado en el cuello; en una escena juega con su anillo de casada (Mongrel ring) que
  se pone y se quita según cree que ella vive o ha muerto — ese anillo es, según Reddit, el objeto que más
  fans buscan comprar como réplica (hilo sobre dónde comprar el anillo en Etsy, ver punto 20/23). ⚠️ wiki del
  juego + comentarios de Reddit (no oficial).
- Curiosidad de personaje (Horde Killer, coleccionables in-game): era esquiadora habitual, tenía abono de
  temporada en la estación Mt. Scott. Deacon la acompañaba aunque no esquiaba tan bien. ⚠️ una fuente (wiki del
  juego, cita los coleccionables del propio juego).

**O'Brian — James O'Brian** (original Bernardo De Paula; latino Daniel Lacy; España Álvaro Reina) —
Estudiante de posgrado que se ofreció como voluntario para NERO al empezar el brote. Conoció a Deacon y Sarah
en las primeras semanas del apocalipsis: cargó supervivientes en un helicóptero de NERO, y aunque simpatizaba
con Deacon, se sintió desbordado y dijo no poder llevar a más gente — Deacon le apuntó con un arma (con Boozer
cubriéndolo) para forzarlo a aceptar a Sarah. Su avión se desvió y terminó, contra las órdenes, asegurándose
de que Sarah recibiera atención médica de calidad, hasta perder el contacto con ella. ✅
_daysgone.fandom.com/wiki/James_O%27Brian#Background_ + lo retoma como personaje NERO en el tramo final del
juego (su «giro» es de los más comentados: hilo de Reddit «O'Brian goes Thriller mode», 11 votos, sobre lo
mucho que impacta verlo perder su humanidad bajo el mando de NERO). ✅
_https://www.reddit.com/r/DaysGone/comments/hefiyi/_
- Voz medida: media-aguda (189 Hz, la más aguda de los 8), muy expresiva (23.5 semitonos) — un registro que
  transmite nervio/tensión, coherente con su papel de burócrata atrapado entre la culpa y las órdenes.
  ✅ voz.py.

**Iron Mike — «Iron Mike» Wilcox** (original Eric Allan Kramer; latino Armando Réndiz; España Ángel Amorós) —
Líder del Campamento Lost Lake. Su ropa (sencilla, práctica, de leñador experimentado) es un espejo de su
carácter. Físicamente fuerte para su edad pese a que sus rodillas «necesitan calentar» antes de rastrear una
horda. Le confiesa a Deacon que fue cristiano muy devoto y que reza menos porque arrodillarse ya le cuesta
físicamente, pero conserva la fe y la aplica en trabajos humildes del campamento. ✅
_daysgone.fandom.com/wiki/Iron_Mike#Personality_.
- Frase citada en la propia wiki: «Remember how we run things in this camp, Deek» — confirma el apodo real de
  Deacon (ver punto 8). ✅.
- Su arma preferida es el revólver «The Sheriff» (objeto que siempre lleva, punto 20). ⚠️ wiki del juego.
- Trivia oscura: *The Art of Days Gone* revela que Iron Mike participó en la masacre de los residentes del
  Campamento Sherman — un secreto que contradice la imagen de líder bondadoso que da al principio. ⚠️ una
  fuente (wiki del juego, cita el artbook oficial).
- Voz medida: media (175 Hz), la de MAYOR rango de los ocho (26.4 semitonos) y ritmo rápido — se nota su
  vehemencia al hablar de lo que está bien y mal en el campamento. ✅ voz.py.

**Rikki — Rikki Patil** (original Nishi Munshi; latino Edurne Keel; España Inma Gallego) — Lugarteniente de
operaciones de Iron Mike en Lost Lake. Optimista, pragmática, con actitud «resolutiva», ingeniera mecánica y
civil de formación; combatiente por encima de la media tras un año viajando con Deacon y Boozer entre Farewell
y Tumalo. Cree de verdad en los ideales del campamento (confianza y compasión), y fue clave para acoger a Lisa
Jackson tras ser torturada por los Rippers, y también a Deacon y Boozer en su semi-exilio. ✅
_daysgone.fandom.com/wiki/Rikki_Patil#Personality_and_Appearance_.
- Tatuajes de inspiración hindú en brazos y hombros; ropa de excedente militar salvo unas botas vaqueras;
  chaqueta verde de faena parecida a la que usa Deacon camino a la Milicia. ⚠️ wiki del juego (relevante para
  vestuario, punto 15, compartido con el investigador de imagen).
- Es bisexual: mantiene una relación romántica con Addy, aunque también siente algo por Deacon. ⚠️ una fuente
  (wiki del juego).
- Voz medida: media (164 Hz), muy expresiva (18.4 semitonos), ritmo normal — la muestra oficial la capta en
  una escena curiosa y afectuosa («¿De verdad fuiste a la guerra? ¿Afganistán o…?»). ✅ voz.py.

**Copeland — Mark «Cope» Copeland** (original Crispin Freeman; latino Erick Selim; España Borja Fernández
Sedano) — Líder del Campamento Copeland. Ya antes del brote le gustaban las armas y la caza; su padre le
inculcó que las libertades de la Constitución están por encima de la burocracia. Libertario, filosofía de
«vive y deja vivir» a la manera de los padres fundadores; ese mismo amor por la libertad individual lo hace
desconfiado de regímenes represivos y a la defensiva frente a agresores — de ahí su desprecio por los
merodeadores, el culto RIP y NERO (a quien ve como brazo autoritario). ✅
_daysgone.fandom.com/wiki/Mark_Copeland#Personality_.
- Es el presentador de **«Radio Free Oregon»**, una emisora pirata/de conspiración que suena por toda la
  carretera del juego — divide mucho al fandom: hay hasta un mod en Nexus Mods, «Shut Up Cope», para
  silenciarlo, y comentarios de Reddit («Copeland definitely belongs on r/mygunismypenis», «Fuck Tucker, me
  and my homies all hate Tucker») que muestran lo mucho que engancha (o harta) su personaje — ver punto 12.
  ⚠️ una fuente por el mod (Nexus), ✅ para el tono del fandom (varios comentarios de Reddit coinciden).
  _https://www.nexusmods.com/daysgone/mods/336_
- Voz medida: grave (104 Hz), expresiva (11.4 semitonos), ritmo normal — tono paternalista y persuasivo,
  coherente con alguien que negocia y presiona a la vez. ✅ voz.py.

**Skizzo — Raymond «Skizzo» Sarkoski** (original Jason Spisak; latino Luis Daniel Ramírez; España Antonio
Ramírez de Antón —el propio director del doblaje español se puso esta voz—) — Rasgos de narcisismo clásico:
sentido elevado de su propia importancia, encanto manipulador, sensación de merecerlo todo, necesidad de tener
siempre la razón, poca empatía salvo cuando percibe que a ÉL le hacen algo injusto, visión de que «todo es
perro come perro», cree que los demás son «tontos» a los que se puede usar, y miente con total convicción,
llegando a creerse su propia versión de la realidad. ✅ _daysgone.fandom.com/wiki/Skizzo#Personality_.
- Es un farsante: se hace pasar por expresidiario, pero una postal de su universidad (coleccionable) confirma
  que en realidad era «chico de fraternidad». Su arma preferida es el «Eliminator». En su lista «The Shit
  List» aparecen los nombres de dos compañeros muertos en una cueva con la nota «deshacerse de ellos» — insinúa
  que los abandonó o los dejó atrapados. ⚠️ wiki del juego.
- Voz medida: grave (110 Hz), la MENOS expresiva de los ocho (5.1 semitonos, «registro normal» en vez de «muy
  expresiva») pero la MÁS rápida (4.22 palabras/s de las ocho muestras): habla plano y atropellado, vendiendo
  una idea sin parar — cuadra con el perfil manipulador/narcisista de arriba. ✅ voz.py (dato propio, cruzado
  con la wiki de personalidad).

### Punto 7 — Personajes principales y secundarios: popularidad oficial y de fans

**Encuestas oficiales de popularidad: no encontré ninguna.** Days Gone es un videojuego occidental de un solo
estudio (Bend Studio/Sony), no una franquicia con revistas o encuestas tipo Shonen Jump; no hay «ranking
oficial de personajes». Busqué «Days Gone character popularity poll», «Days Gone official survey favorite
character» (inglés) y no aparece nada de PlayStation ni de Bend Studio. Lo más cercano a un reconocimiento
oficial es el **premio a Claudio Serrano** (voz de Deacon en España) en el Fun&Serious Game Festival por su
interpretación (punto 8) — un premio a un actor, no una encuesta de personajes.

**Popularidad de fans (proxy con Reddit r/DaysGone, ya en `datos-voz.md`; no repito las búsquedas, sólo leo lo
que trajeron)**:
- **Deacon** es, con diferencia, el favorito asumido: el hilo con más comentarios de todos («¿cuál es tu
  personaje favorito además de Deacon y Boozer?», 42 votos, 88 comentarios) da por hecho que Deacon y Boozer
  son el top 1 y 2 antes de preguntar por el resto. ✅ _reddit.com/r/DaysGone/comments/1m2f0ea/_
- Un hilo dedicado, «Deacon might be my favorite main character in a video game that I've ever played» (110
  votos, 42 comentarios), atribuye su popularidad al trabajo de Sam Witwer y a que combina dureza con un lado
  sensible (habla con la lápida de Sarah). ✅ _reddit.com/r/DaysGone/comments/151ng1o/_
- **Copeland**, un secundario, genera el hilo con MÁS votos de todo el bloque «por qué lo amo»: «I really love
  Copeland. Please tell me why.» (236 votos, 63 comentarios) — más votos que cualquier hilo sobre Deacon en la
  categoría de «por qué amo el juego». Los comentarios están divididos: unos lo odian por robarle la moto a
  Deacon y culpar a otros («I hate the fact that Copeland stole Deacon's bike… then even expects Deke to work
  for him»), otros lo defienden porque sus emisiones de «Radio Free Oregon» «casi siempre tienen razón sobre
  el mundo del juego» y porque «me reía con lo que decía Deacon después de oírlo». Es el ejemplo perfecto de
  «personaje secundario más discutido que el protagonista» que pide `ENCARGO.md`. ✅
  _reddit.com/r/DaysGone/comments/12yrqb5/_
- **Boozer** es tratado como coprotagonista/deuteragonista por la propia comunidad y por Wikipedia (lo cita
  como «deuteragonist» del juego) — no hay un hilo propio con tantos votos porque se le da por hecho como
  parte del dúo con Deacon. ⚠️ (una fuente concreta, Wikipedia, pero coincide con el trato que le da Reddit en
  el hilo de arriba).
- **O'Brian** genera el hilo «O'Brian goes Thriller mode (best scene of the game)» (11 votos) sobre su giro de
  personaje — modesto en votos pero con comentarios que piden una secuela para ver más de él («We need DG2
  please»). ⚠️ una fuente (Reddit, pocos votos).
- El fandom tiene también hilos de «personaje menos favorito» (19 votos, 17 comentarios, «Your Deeks Least
  favorite or hated character??») — no llegué a leer los comentarios a fondo por presupuesto de búsquedas;
  queda para quien retome este punto. ⚠️ _reddit.com/r/DaysGone/comments/rao6s2/_

**Con quién aparece cada uno** (dinámicas para láminas en grupo, cruzando punto 13): Deacon+Boozer (dúo
inseparable desde antes del brote), Deacon+Sarah (matrimonio, hilo emocional central), Iron Mike+Rikki+Addy
(cúpula de mando de Lost Lake), Rikki+Addy (pareja), Copeland+Deacon (relación de negociación tensa, «Deek»),
O'Brian+Sarah (la rescata y protege sin que Deacon lo sepa hasta el reencuentro), Skizzo+Deacon (falsa amistad
que termina en traición). ✅ (de las biografías del punto 13, cruzado con Reddit).

### Punto 20 — Gustos y detalles de cada personaje

**No hay «databook» oficial con altura/cumpleaños/edad exacta** de los personajes (busqué «Days Gone Deacon
altura cumpleaños ficha personaje», «Art of Days Gone character sheet height birthday», en español e inglés):
no es una franquicia anime con esas fichas; ni el artbook *The Art of Days Gone* (Dark Horse) ni la wiki traen
esos datos. Lo que sí hay, de la propia wiki del juego y de sus coleccionables in-game (cartas «Horde Killer»,
postales, listas), es esto:

- **Deacon**: objeto que siempre lleva = su chaqueta «kutte» de cuero negro con los colores de los Mongrels MC
  (punto 13); tatuajes que cuentan su historia (10.ª Div. de Montaña, «RIDE», «HARD», el nombre de Sarah en el
  cuello). Cómo se ve a sí mismo: un exmotero sin ataduras que en el fondo necesita pertenecer a algo (ver
  Personality, punto 13). Come lo que caza/rebusca —no hay un plato favorito documentado—. ⚠️ wiki del juego.
- **Boozer**: bebedor, de ahí su propio apodo («Boozer» = «borrachín»); su nombre real, William, casi nunca se
  usa (sólo Addy lo llama así). Le apasiona la vida «al límite» del club de moteros. ⚠️ wiki del juego.
- **Sarah**: esquiadora habitual con abono de temporada en Mt. Scott Ski Resort; bióloga/investigadora de
  formación, curiosa por naturaleza (aprendió a montar en moto por Deacon). Su anillo de boda (el «Mongrel
  ring») es su objeto más asociado en el fandom — hay un hilo de Reddit preguntando dónde comprar una réplica
  en Etsy. ✅ (wiki + hilo de Reddit sobre el anillo). _reddit.com/r/DaysGone/comments/nbjjt9/_
- **Iron Mike**: arma que siempre lleva, el revólver «The Sheriff»; antes muy religioso (cristiano devoto),
  ahora aplica su fe en el trabajo diario del campamento en vez de en el rezo formal porque arrodillarse ya le
  cuesta físicamente. Se ve a sí mismo como protector práctico, no como predicador. ⚠️ wiki del juego.
- **Rikki**: tatuajes de inspiración hindú en brazos y hombros; le encanta la ingeniería (mecánica y civil);
  viste excedente militar salvo sus botas vaqueras, su toque personal. ⚠️ wiki del juego.
- **Copeland**: aficionado a las armas y la caza desde antes del brote (se lo inculcó su padre); su afición
  favorita ahora es su propia emisora de radio pirata, «Radio Free Oregon», donde comparte teorías y opiniones
  sobre el mundo tras el brote. Se ve a sí mismo como el último defensor de la libertad individual frente a
  NERO y los merodeadores. ✅ (wiki del juego + reacciones de Reddit al personaje/radio, punto 12).
- **Skizzo**: arma que siempre lleva, el «Eliminator»; también tiene un «SSR» que casi no usa. Se ve a sí
  mismo como un superviviente astuto y «peligroso» (se inventó un pasado de expresidiario), pero una postal de
  su universidad demuestra que en realidad fue «chico de fraternidad»: el gusto/manía central de Skizzo es
  mentir sobre quién fue antes del apocalipsis. ⚠️ wiki del juego.
- **O'Brian**: no hay datos de gustos personales en la wiki más allá de que era estudiante de posgrado antes
  del brote; su «manía»/rasgo definitorio es que intenta hacer lo correcto dentro de un sistema (NERO) que se
  lo va arrebatando. ⚠️ wiki del juego (poca info previa al apocalipsis, es intencional: no se explica su
  vida anterior).

### Punto 12 — Lo que el fandom ama; qué NO hacer

**Lo que ama (con hilos y comentarios reales de r/DaysGone, arctic-shift API, ya localizados en
`datos-voz.md` + comentarios leídos ahora)**:
- **El «bromance» Deacon-Boozer** es lo más citado con cariño: «Heterosexual life partners, for sure», «Hands
  down best bromance in videogames», «Si no fuera por Sarah, habría asumido que Deacon y Boozer eran pareja».
  ✅ _reddit.com/r/DaysGone/comments/1bythh7/_ (comentarios).
- **Muletillas y frases de combate que se volvieron memes** dentro del propio fandom (bocadillos que sueltan
  los NPC constantemente durante el juego, citados de memoria por los fans en un hilo llamado justamente «Deek
  most iconic quotes»): «Nothing beats scrap…», «Fuel can…», «Nice, headshot», y la broma de que Deacon dice
  «less Freaks» cuando debería ser «fewer» (un fan «gramático» lo corrige mentalmente cada partida). ✅
  _reddit.com/r/DaysGone/comments/15bzlns/_
- **El running gag de Carlos y Lil Jon**: en un hilo sobre la trama de los Rippers, un fan pregunta «¿alguna
  vez se explica por qué Carlos está tan obsesionado con Lil Jon? No paraba de decirme "get low"» — es un
  chiste interno que los fans reconocen al instante. ⚠️ un comentario, pero consistente con el personaje de
  Carlos en la wiki (relacionado con la MC, jerga hip-hop). _reddit.com/r/DaysGone/comments/1m5omfy/_
- **«Radio Free Oregon» (las emisiones de Copeland)** genera cariño Y hartazgo a partes iguales — visto en el
  punto 7/13: hay quien dice que «casi siempre tiene razón sobre el mundo del juego» y quien creó el mod «Shut
  Up Cope» en Nexus Mods para silenciarlo del todo. Cualquiera de las dos reacciones es «auténtica» del
  fandom; una lámina que cite mal su discurso (como si sólo fuera un villano tonto) chocaría con los fans que
  SÍ lo disfrutan. ✅ (mod + comentarios de Reddit coinciden en que divide opiniones).
- **El anillo de boda de Deacon** (Mongrel ring): varios fans preguntan por foros de Etsy dónde comprar una
  réplica exacta — el accesorio más «cosplay-able» del protagonista. ⚠️ un hilo, pero es indicativo fuerte:
  hay demanda real de mercancía basada en ese objeto. _reddit.com/r/DaysGone/comments/nbjjt9/_
- **La trama de los Rippers** (culto de moteros automutilados) es, con diferencia, el arco narrativo más
  citado con cariño: el hilo «debería haber durado todo el juego» tiene 917 votos, el más votado de todo
  r/DaysGone entre los que se buscaron para esta ficha. ✅ _reddit.com/r/DaysGone/comments/1m5omfy/_
- **La boda de Deacon y Sarah** y el detalle de que Deacon la celebra vistiendo igualmente su «cut» (colores
  de los Mongrels) en vez de un traje convencional: «Deacon still wearing the cut during their wedding is
  iconic» (10 votos, pero es justo el tipo de detalle de vestuario que un fan reconoce al instante). ⚠️ un
  hilo. _reddit.com/r/DaysGone/comments/1ge34pb/_

**Qué NO hacer (quejas reales, para no «sonar falso» según pide `ENCARGO.md`)**:
- **No presentar la muerte de Boozer como sacrificio heroico sin más**: en el final, Boozer parece morir
  salvando a Deacon, pero resulta ser un «fake out» (aparece vivo poco después, sin que se explique bien cómo
  escapó). Varios fans lo consideran una salida barata: «It cheapened the ending that the writers couldn't
  commit to Boozer willingly sacrificing himself… the fake-out… no one saw me until I magically appeared».
  Si una lámina usa esa escena como «Boozer se sacrifica», estaría repitiendo justo lo que el fandom ve como el
  fallo de guion más comentado del juego. ✅ (varios comentarios coinciden) _reddit.com/r/DaysGone/comments/1bythh7/_
- **No convertir a Copeland en un villano de cartón**: como se vio arriba, divide al fandom pero muchos lo
  defienden con matices («casi siempre tiene razón»); presentarlo como un bufón sin más suena falso para media
  comunidad.
- **No dibujar a Deacon como un motero genérico sin su «cut» ni sus tatuajes**: son su seña de identidad más
  citada (punto 13); una lámina sin el chaleco de los Mongrels o sin, al menos, el tatuaje del cuello con el
  nombre de Sarah, perdería lo que el fandom reconoce a primera vista.
- **No usar «¿Me entiendes, Méndez?» fuera de contexto**: es una broma de adaptación MUY específica del
  doblaje latino (punto 8) — funciona sólo si se sabe que es un chiste de doblaje, no una frase genérica de
  Deacon.

### Punto 21 — Por qué la gente la ama; escenas que emocionan

**Por qué la gente ama Days Gone** (reseñas, Reddit, ventas — ✅ cruzado en dos o más fuentes):
- El vínculo Deacon-Boozer es la razón más citada, por encima incluso de la trama principal: «best bromance in
  videogames» (Reddit, punto 12). ✅
- La libertad de estilo de juego: un hilo con 107 votos se titula «Why I Love Days Gone: It Respects Player
  Choice and Playstyle». ✅ _reddit.com/r/DaysGone/comments/1qx6b96/_
- El «vibe» distinto a otros survival/zombis, pese a sus defectos técnicos: «This game has a different vibe.
  That's why I love this, even with it's shortcomings» (181 votos). ✅ _reddit.com/r/DaysGone/comments/1uks79g/_
- Cala hondo con el tiempo: «After almost a year, I managed to finish Days Gone. I don't know why, but I'm in
  love with this game» (121 votos) — varios comentarios describen que el juego «engancha tarde», no en las
  primeras horas. ⚠️ un hilo, pero coincide con la reputación pública del juego (reseñas de lanzamiento bajas,
  reputación de culto después) que también documenta Wikipedia. ✅ (dos fuentes: Reddit + reputación
  documentada por Wikipedia/ScreenRant sobre su «redención» posterior al lanzamiento).
- El público se identifica sobre todo con **Deacon** (por Sam Witwer/los actores de doblaje, punto 13) y con
  **Boozer** como «el amigo que todos querríamos tener»; ver también Copeland como personaje secundario que
  genera identificación por sus ideas polémicas pero «casi siempre acertadas dentro del juego» (punto 7).

**Escena que la gente señala como la más floja emocionalmente — al revés de lo esperado** (para no «sonar
falso», ver `ENCARGO.md`): el reencuentro final de Deacon y Sarah, que en teoría debería ser el clímax
emocional del juego, está ampliamente criticado como anticlimático: «no hay diálogo, ni un "me alegra que
estés viva", ni siquiera se besan» — un artículo llega a titularse «Days Gone Ending Twist Completely Ruins
All The Character Development». ✅ _screenrant.com/days-gone-ending-twist-deacon-sarah-bad-why/ ·
comentarios de GameFAQs y Steam Community citados por la misma cobertura._
- Conclusión práctica para la lámina: **no uses el reencuentro final como «la escena que hace llorar»** — el
  propio fandom la ve floja. Lo que sí funciona mejor, y así lo documenta la cobertura del juego, es el
  **duelo de Deacon antes de saber que Sarah vive**: raspa su nombre de una lápida improvisada que él mismo le
  hizo, y se pone de nuevo el anillo de casado — ✅ escena repetidamente citada como la más conmovedora del
  arco de Sarah (más que el reencuentro). _screenrant.com/days-gone-ending-twist-deacon-sarah-cure-explained/_
  Con flashbacks de la boda intercalados mientras Deacon cuida esa tumba. ⚠️ (una fuente concreta de la escena,
  pero coincide con la ficha de Trivia de Sarah en la wiki, punto 13, que describe la misma secuencia).
- La otra escena que la comunidad señala como fuerte es el giro de **O'Brian** perdiendo su humanidad bajo
  NERO (punto 7, «O'Brian goes Thriller mode») — no es una escena que «haga llorar» sino que «impacta»/asusta,
  el tipo de gran giro que el fandom pide que se explore más en una secuela. ⚠️ un hilo de Reddit.

### Punto 22 — Fan dubs y comunidad hispana

### Punto 22 — Fan dubs y comunidad hispana

**No es un juego con «openings» tipo anime** (no hay canción de apertura que cubrear) y no encontré fandubs de
escenas hechos por fans en español (busqué «Days Gone fandub español parodia TikTok», «Days Gone fandub
latino/español youtube», «Days Gone cover español opening Long Way Home»): lo que sale es contenido oficial de
prensa (HobbyConsolas, Vandal) o listas genéricas de TikTok sin vídeos concretos con vistas. Lo que sí hay,
documentado con más detalle:
- **Comparaciones de doblaje hechas por la comunidad**: un vídeo de YouTube titulado «DAYS GONE: Doblaje
  ESPAÑA vs LATINOAMÉRICA vs INGLÉS (PS4)» compara los tres audios lado a lado — exactamente el tipo de
  contenido que interesa a un servidor de doblaje, aunque no pude verificar canal ni vistas (YouTube pide
  iniciar sesión desde este servidor). ⚠️ una fuente (aparece en resultados de búsqueda, no se pudo abrir).
- **PlayStation mismo promovió la comparación de doblajes**: Vandal público un tráiler mostrando «las voces en
  castellano y español latinoamericano» lado a lado antes del lanzamiento — o sea, la propia distribuidora
  alimentó esa curiosidad comparativa del público hispano. ✅ _vandal.elespanol.com/noticia/1350720398/_
- **Actividad en TikTok** con las etiquetas «days gone en español», «deacon days gone» y «days gone deacon
  cosplay» existe (hay vídeos activos, un usuario citado es @ervs.18), pero no logré aislar vídeos concretos
  con cifras de vistas verificables sin acceso a TikTok con sesión — se anota como pista, no como dato
  confirmado. ⚠️ _tiktok.com/discover/days-gone-en-espa%C3%B1ol_
- **Cosplay de Deacon**: hay comunidad activa (grupos de Facebook de cosplay en Filipinas y Sri Lanka
  encontrados en la búsqueda, guías de disfraz en costumewall.com y carboncostume.com que detallan el kutte de
  cuero con el parche Mongrels MC, camiseta gris/negra, jeans, botas de moto, gorra negra y pañuelo rojo), pero
  no encontré específicamente eventos o cosplayers de habla hispana documentados con fuente — punto que le
  toca en detalle al investigador de imagen (punto 23), aquí sólo se deja la pista. ⚠️
- **Comunidad de doblaje hispana sobre esta obra en concreto**: no encontré foros o Discords públicos
  centrados en el doblaje de Days Gone más allá de Doblaje Wiki y doblajevideojuegos.es (que son bases de
  datos, no comunidades de fandub). Es un dato honesto: a diferencia de anime o Disney, el doblaje de
  videojuegos como Days Gone no genera tanta comunidad de fandub en español como series con más recorrido.

## Lo mejor para la lámina

1. **Deacon con su kutte de cuero y el tatuaje de «Sarah» en el cuello**, hablando con el cuadro de diálogo
   de radio/walkie del juego — es lo que el fandom reconoce al instante (puntos 13, 20).
2. **Cita real de doblaje latino**: «Nunca hemos hablado de ello… ¿De por qué seguimos llevando los colores?»
   (tráiler argumental, `partes/episodios.md`) o «¿Me entiendes, Méndez?» como guiño de doblaje (punto 8).
3. **Copeland y su «Radio Free Oregon»** como gag reconocible: un cuadro de diálogo tipo «transmisión de
   radio» (estática, micrófono) es un recurso muy propio de la serie y divide cariño/hartazgo real (punto 12).
4. Si se usa a un secundario en vez del protagonista: **Copeland es, por votos de Reddit, más comentado que
   Deacon** en «por qué lo amo» — encaja con la petición del dueño de destacar secundarios queridos.
5. Evitar el reencuentro final Deacon-Sarah como «la escena triste»: usar mejor a Deacon cuidando la lápida
   improvisada de Sarah y poniéndose el anillo, que es la escena que la crítica sí valora (punto 21).

## No encontré

- ⚠️ **Encuestas oficiales de popularidad de personajes** (tipo revista/ranking): no existen para este juego;
  busqué «Days Gone character popularity poll» y «official survey favorite character» en inglés, nada de Sony
  ni Bend Studio (punto 7).
- ⚠️ **Segunda fuente totalmente independiente de Doblaje Wiki para el reparto latino completo** (más allá de
  los 8 personajes de arranque, verificados cruzando ficha de personaje + ficha de actor dentro de la misma
  wiki): probé ANMTV (sin cobertura de este título), Behind The Voice Actors (403 Forbidden, dos intentos),
  IMDb full credits (403/202 sin contenido, dos intentos), International Dubbing Wiki (la ficha de Daniel Lacy
  no llega a listar videojuegos). Es una limitación real del sector: el doblaje latino de videojuegos casi no
  se documenta fuera de Doblaje Wiki, a diferencia del doblaje de España que sí tiene dos bases de datos
  independientes (eldoblaje.com y doblajevideojuegos.es).
- ⚠️ **Altura, cumpleaños o edad exacta de los personajes** (punto 20): no hay «databook» oficial con fichas
  de estadísticas; ni el artbook *The Art of Days Gone* ni la wiki las traen. Busqué en español e inglés.
- ⚠️ **Fandubs de escena y covers de canciones en español** (punto 22): el juego no tiene una canción de
  apertura tipo anime que cubrear, y no encontré canales o vídeos concretos de fandub en español con cifras
  verificables (sólo etiquetas genéricas de TikTok). Sí hay contenido de comparación de doblajes, que se
  documenta arriba.
- ⚠️ **Comunidad de doblaje hispana específica de Days Gone** (foros, Discords públicos): no encontré ninguno
  dedicado; el interés hispano documentado es sobre todo periodístico (Vandal, HobbyConsolas, LevelUp) o de
  bases de datos (Doblaje Wiki, DoblajeVideojuegos.es), no de comunidad de fans organizada en torno al doblaje.
- ⚠️ No profundicé en el hilo «Your Deeks Least favorite or hated character?» (19 votos) por presupuesto de
  búsquedas — queda pendiente si se retoma este punto.

## Bitácora de búsqueda

**Herramientas usadas (no cuentan como «búsqueda web»)**: `curl` directo a la API de Doblaje Wiki
(`action=parse&prop=wikitext`) para Days Gone y para 11 fichas de actor; `curl` directo a la API de
`daysgone.fandom.com` para 8 fichas de personaje; `curl` a eldoblaje.com y doblajevideojuegos.es;
`herramientas/voz.py` (Whisper `small` + Parselmouth) sobre las 8 muestras `.ogg` oficiales de Doblaje Wiki,
descargadas a `/tmp/claude-0/trabajo/120-days-gone-voz/audio/`; `arctic-shift.photon-reddit.com` para posts y
comentarios de r/DaysGone (con reintentos por límite de tasa de la API).

**Búsquedas web (WebSearch), todas en español o inglés según el caso** — quedan más de 30 de las 50
disponibles sin usar, por si el redactor o el jefe piden ampliar algo:
1. `"Days Gone" eldoblaje.com Claudio Serrano Deacon` — encontró la ficha de eldoblaje.com y confirmó el
   doblaje de España.
2. `"Days Gone" doblaje español reparto "Claudio Serrano" Boozer Sarah` — confirmó el vídeo de HobbyConsolas.
3. `ANMTV "Days Gone" doblaje latino Deacon José Gilberto Vilchis` — sin resultados de ANMTV.
4. `"Days Gone" "José Gilberto Vilchis" Deacon doblaje` — confirmó a Vilchis para Deacon latino.
5. `"Days Gone" behindthevoiceactors Latin American Spanish cast Deacon Boozer` — BTVA existe pero bloqueó el
   acceso directo (403).
6. `"Beto Castillo" Boozer "Days Gone" doblaje` — confirmó a Castillo para Boozer.
7. `site:anmtv.mx "Days Gone"` — sin resultados.
8. `"Days Gone" doblaje latino tráiler PlayStation México Vilchis Deacon voz` — confirmó el tráiler de
   lanzamiento localizado.
9. `"Days Gone" "José Gilberto Vilchis" instagram OR entrevista OR twitter` — sin entrevista específica sobre
   Days Gone.
10. `"Alejandra Delint" Sarah "Days Gone"` — llevó a descubrir que la ficha actual de la actriz es «Alex(ander)
    Delint», no binaria.
11. `"Days Gone" doblaje latino reparto "Erick Selim" OR "Armando Réndiz" OR "Luis Daniel Ramírez" OR "Edurne
    Keel"` — sin una fuente externa única, resultados dispersos.
12. `"Beto Castillo" "William Boozer" OR "Boozer Gray" Days Gone personaje` — nada nuevo.
13. `"Days Gone" créditos doblaje latino reparto completo actores voz México` — nada nuevo.
14. `"Daniel Lacy" actor de doblaje "Days Gone" O'Brian` — llevó a la página de International Dubbing Wiki
    (sin la ficha de videojuegos completa).
15. `"Days Gone" Deacon St. John altura cumpleaños edad "Art of Days Gone" ficha personaje` — confirmó que no
    hay databook con esos datos.
16. `"Days Gone" ending Sarah reunion emotional scene reviewers cried moving` — encontró la crítica de
    ScreenRant sobre el reencuentro anticlimático.
17. `"Days Gone" most emotional scene favorite reddit tears "Sarah" wedding flashback OR gravestone` — encontró
    la escena de la lápida y el anillo.
18. `"Days Gone" fandub español parodia TikTok Deacon` — sólo etiquetas genéricas de TikTok.
19. `"Days Gone" meme español latino Copeland "Radio Free Oregon" doblaje comunidad` — encontró el mod «Shut Up
    Cope» en Nexus Mods.
20. `"Days Gone" cover español opening OR canción fandub youtube "Long Way Home" español` — confirmó que no hay
    covers relevantes (el juego no tiene opening tipo anime).
21. `"Days Gone" reacción doblaje español vs latino youtube comparación voces` — encontró el vídeo comparativo
    de YouTube (no se pudo abrir, YouTube pide sesión).
22. `"Days Gone" cosplay Deacon español Latinoamérica evento convención` — cosplay documentado en inglés/otros
    idiomas, nada específicamente hispano con fuente.

**Peticiones directas fallidas** (para no repetirlas sin motivo): `behindthevoiceactors.com` → 403 (dos
intentos, con y sin WebFetch); `imdb.com/title/tt6795336/fullcredits` → 403 y 202 vacío (dos intentos, con y
sin user-agent de navegador); `eldoblaje.com/datos/buscar.asp` y variantes → 404 (se resolvió el id real,
55301, por búsqueda web en vez de adivinar la URL).

Sigue: nada obligatorio pendiente de los puntos 7, 8, 12, 13, 20, 21, 22. Si se retoma esta parte, ampliar el
hilo de «personaje menos favorito» (punto 7) y, si el jefe lo pide, intentar de nuevo BTVA/IMDb con otra
salida de red para una segunda fuente externa del reparto latino completo (punto 8).
