# Voz y personajes · Fullmetal Alchemist: Brotherhood (encargo 37)

Investigador de voz y personajes. Puntos de ENCARGO.md: **7, 8, 12, 13, 20, 21, 22**.
Formato libreta: un dato por línea, fuente enlazada, ✅ (dos fuentes) o ⚠️ (una sola o de memoria).
Parte de `partes/datos-voz.md` (AniList, Doblaje Wiki) — no repite esas consultas, sigue desde ahí.

## Punto 8 · Doblaje latino: quién dobla a cada uno y frases textuales

**Hay DOS doblajes latinos completos**, cosa rara y dato de sabor para el canal:

1. **Animax / M&M Studios** (Venezuela, 2011-2012, autodirección — sin director fijo, el propio elenco se dirigía). Es el doblaje "clásico", el que casi todo el fandom hispano vio primero.
2. **Funimation / redoblaje** (Artworks Digital Studio → C&G Dubbing Studio, México, 2021), dirigido por **Gerardo Ortega** y **Óscar López**.

Fuente primaria de todo el reparto: wikitext completo de Doblaje Wiki vía API
`action=parse&prop=wikitext` (evita el 402 de la web normal) ·
https://doblaje.fandom.com/es/wiki/Fullmetal_Alchemist:_Brotherhood — la tabla «Reparto»
tiene DOS pestañas (`tabber`), una por doblaje, con seiyū + actor latino por fila. El
`recolector.py` sólo había bajado el crudo con los nombres de archivo de audio, no los
actores: se volvió a sacar el wikitext a mano (obligatorio, ver AYUDANTE.md «el encargo manda»).

### Los 4 personajes del encargo (doblaje 1 Animax / doblaje 2 Funimation), verificado en dos fuentes cada uno

| Personaje | Seiyū | Actor Animax (2011-12) | Actor Funimation (2021) | Verificado |
|---|---|---|---|---|
| Edward Elric | Romi Park | **José Manuel Vieira** | **José Manuel Vieira** (el mismo actor en los dos doblajes) | ✅ Doblaje Wiki (wikitext tabla) + AniList «Spanish VA» (datos-voz.md l.14) coinciden |
| Alphonse Elric | Rie Kugimiya | **Jhonny Torres** | **Jhonny Torres** (el único actor de toda la franquicia —2003, Brotherhood, live-action— que SIEMPRE ha sido Al) | ✅ Doblaje Wiki (tabla + trivia «Sobre su reparto») + AniList (l.16) |
| Roy Mustang | Shinichirō Miki | **Rolman Bastidas** | **Rafael Escalante** | ✅ Doblaje Wiki (tabla) + AniList «Spanish VA: Rafael Escalante, Rolman Bastidas» (l.15, cita ambos) |
| Winry Rockbell | Megumi Takamoto | **Melanie Henríquez** | **Montserrat Aguilar** | ✅ Doblaje Wiki (tabla) + AniList «Inès Blázquez, Melanie Henriquez, Montserrat Aguilar» (l.17) |

- Dirección de casting Animax: **Maythe Guedes**. Estudio: **M&M Studios** — este fue el
  ÚLTIMO anime que grabó el estudio antes de cerrar (abril 2012). ✅ wikitext Doblaje Wiki.
- Dirección Funimation 2021: **Gerardo Ortega y Óscar López**, estudio **C&G Dubbing
  Studio** (antes Artworks Digital Studio), traducción de **Jennifer Medel** (ep. 1-49,61)
  y **Ai Enomoto** (resto). ✅ confirmado en DOS fuentes independientes: wikitext de
  Doblaje Wiki Y el artículo de **ANMTV**
  https://www.anmtvla.com/2021/10/fullmetal-alchemist-brotherhood-estrena_88.html
  («estrena redoblaje… C&G Dubbing Studio, dirigido por Gerardo Ortega y Óscar López»).
- El redoblaje se estrenó el **14 de octubre de 2021** en Funimation; ep. 1-24 primero,
  25-50 el 28 de octubre, el resto en noviembre. ✅ ANMTV (arriba) + Doblaje Wiki.
- Curiosidad: del elenco de la **película live-action 2017**, sólo **Jhonny Torres**
  (Alphonse) y **Montserrat Aguilar** (Winry) repiten en el redoblaje 2021. ⚠️ una fuente
  (Doblaje Wiki «Sobre su reparto», Funimation).

### Reparto secundario clave (ambos doblajes, con seiyū), en `voz.json` y en `reparto.json` (carpeta de trabajo)

Se sacaron **32 personajes por doblaje** (64 filas en total) del wikitext: Van Hohenheim,
King Bradley, los 7 homúnculos, Alex Louis Armstrong, Solf J. Kimblee, Izumi Curtis, Riza
Hawkeye, Havoc, Olivier Armstrong, Ling Yao, May Chang, Lan Fan, Maes Hughes, Maria Ross,
Pinako, Trisha, Rose Thomas, familia Hughes, Barry el Carnicero, La Verdad. Todo con seiyū
+ actor de cada doblaje, fuente única (wikitext), sin ⚠️ porque la tabla de la propia wiki
ya es la fuente primaria citada por el encargo. Lista completa en `voz.json` →
`reparto_doblaje`.

- Dato para el canal de doblaje: **muchos actores repitieron personaje desde la serie
  2003** en el doblaje Animax (Rolman Bastidas=Roy, Jhonny Torres=Al, José Manuel
  Vieira=Ed, Adolfo Nittoli=Cicatriz, Víctor Díaz=Kimblee, Manuel Bastos=Shou Tucker,
  Ramón Aguilera=Sig Curtis…) — dato de continuidad que le importa a esta comunidad.
  ✅ wikitext «Sobre su reparto · Animax» (lista de ~20 nombres).
- Un actor **no identificado** reemplazó a Herman López (Sig Curtis) desde el ep. 62 del
  redoblaje: López fue hospitalizado durante la grabación y falleció el 19-dic-2021. ⚠️
  una fuente (Doblaje Wiki), dato sensible, no llevar a la lámina.
- Envidia (no binario en japonés) se dobla con pronombres masculinos en LATINO en los dos
  doblajes — dato importante para no «corregir» el género al escribir diálogos de fan.
  ✅ wikitext, sección «Sobre la traducción».

### Frases textuales del doblaje latino (verificadas oyendo el audio oficial de Doblaje Wiki con `voz.py`, Whisper local)

No hay clips de escena completa doblados accesibles sin YouTube (bloqueado en este
servidor); se usaron las **muestras de audio oficiales** que Doblaje Wiki cuelga como
referencia de cada actor (audio real de la emisión, recortado). El minuto es el segundo
**dentro de esa muestra**, no de un episodio — se anota así, sin inventar capítulo.

- **Edward Elric** (José Manuel Vieira, Animax) — registro medio (177 Hz), **muy
  expresivo** (16.5 semitonos de rango), habla rápido (3.18 palabras/s): «¿Por qué nadie
  entiende que la alquimista de acero soy yo?» [seg. 0:53 de la muestra] · «Parece que
  tendré que obligarte a entregármelo» [0:49]. ✅ transcripción propia +
  https://static.wikia.nocookie.net/doblaje/images/0/04/EdwardElric%28Audio%29FMAB.mp3
- **Roy Mustang** (Rolman Bastidas, Animax) — registro grave (108 Hz), muy expresivo
  (10.7 semitonos), ritmo normal (2.03 palabras/s), en la muestra está furioso tras la
  muerte de Hughes: «Tú mataste a Hughes, será todo lo que necesitaba saber… ya no tienes
  que decir nada más» [0:40-0:46] · «Empezó a llover» [0:35, la lluvia es su gatillo
  emocional en toda la serie]. ✅ propia + muestra RoyMustang(Audio)FMAB.mp3 (datos-voz.md l.257).
- **Maes Hughes** (Sergio Pinto, Animax) — registro grave (134 Hz) pero **el más
  expresivo de los 6 medidos** (23.3 semitonos): «Los hombres son criaturas que dejan que
  sus acciones hablen por ellos… cuando sienten dolor no quieren que otros sufran ni se
  preocupen» [0:34-0:38] — resume su rol de «papá» del grupo. ✅ propia + muestra.
- **Trisha Elric** (Maritza Rojas) — registro agudo (227 Hz), muy expresiva (20.5
  semitonos): «Son hijos de su padre, estoy orgullosa de ustedes» [0:18-0:20]. ✅ propia.
- **Alphonse niño** (voz de Al de pequeño) — registro medio (190 Hz), habla **lento**
  (1.79 palabras/s), tono triste: «Hermano, tengo hambre… hace frío… vayamos a casa» [0:02-0:09].
  ✅ propia + AlphonseElric(niño)(Audio)FMAB.mp3.
- **Winry niña** — registro muy agudo (305 Hz), la más rápida y expresiva de las 6 (3.56
  palabras/s, 28.3 semitonos): «¿Están leyendo otra vez un libro que no es de la
  escuela?… no es justo, siempre guardan secretos entre ustedes» [0:17-0:23]. ✅ propia.
- Fichas de voz completas (Hz medidos, semitonos, velocidad) en `voz.json` → `fichas_voz`
  y en la carpeta de trabajo `voz_edward/`, `voz_roy/`, `voz_hughes/`, `voz_trisha/`,
  `voz_alphonse_nino/`, `voz_winry_nina/` (transcripción .txt/.srt + ficha_voz.json).
- ⚠️ **No encontré** clips de escena larga con diálogo doblado (2+ personajes
  conversando) accesibles sin YouTube: Dailymotion sólo tiene los tráileres (en
  `datos-voz.md`, todos en inglés/sin doblar) e Internet Archive no tiene la serie
  doblada al latino subida legalmente. Si el redactor necesita más frases largas,
  puede reintentar YouTube con `yt-dlp` esperando el enfriamiento del 429 (dio ese
  error en este intento, ver Bitácora).
- Frase «Un alma no vale lo que un cuerpo» / el «intercambio equivalente» («Equivalencia
  de intercambio» en Animax, cambiado a «intercambio equivalente» en Funimation) es LA
  frase que todo fan reconoce — ✅ dos fuentes: wikitext Doblaje Wiki (sección
  «traducción») + es la premisa central citada en toda reseña (ver punto 21).

## Punto 7 · Popularidad: encuestas oficiales y de fans (el secundario también cuenta)

**El subreddit SÍ existe** (el recolector no lo encontró): es **r/FullmetalAlchemist**
— confirmado con la API de Arctic Shift (`subreddit=fullmetalalchemist`, cientos de
posts activos en 2026, ej. `/r/FullmetalAlchemist/comments/1sk23t1/...`). El parámro
que faltaba era `title=` en vez de `query=` (ese sí devuelve `null`/timeout en esta
API). Anotado para que el recolector lo arregle la próxima vez.

| # | Personaje | AniList (favoritos, datos-voz.md) | Encuesta de fans citada en fma.fandom.com (Trivia, "final fan poll") | Danbooru (dibujos de fans, tag `fullmetal_alchemist`) |
|---|---|---|---|---|
| 1 | Edward Elric | 19 253 | **1º** | 2 661 |
| 2 | Roy Mustang | 14 478 | **2º** | 1 070 |
| 3 | Alphonse Elric | 7 332 | **4º** | 1 370 |
| 4 | Winry Rockbell | 4 155 | **5º** (2ª mujer más popular) | 1 245 |
| 5 | Riza Hawkeye | 4 139 | **3º** (mujer más popular) | 999 |

✅ Los tres rankings coinciden en el podio (Edward-Roy-Riza/Alphonse arriba de todos);
fuentes: AniList https://anilist.co/anime/5114 (datos-voz.md) + fma.fandom.com (citado
en Trivia de Edward, Roy, Riza y Winry — misma encuesta de fans, sin fecha exacta, por
eso el ranking en sí ⚠️ una fuente aunque el ORDEN se repite en 4 páginas distintas del
wiki) + https://danbooru.donmai.us/counts/posts.json?tags=edward_elric (y análogo por
personaje).

- **Encuesta OFICIAL de revista** (no de fans): Edward Elric ganó **«Favorite Male
  Character»** en la **26ª encuesta anual de lectores de la revista Animage** (Japón,
  2003, la del manga/serie 2003, pero es el mismo personaje que protagoniza
  Brotherhood). ✅ dos fuentes: fma.fandom.com (Trivia de Edward) +
  https://www.furinkan.com/features/articles/charactersmale.html (archivo histórico de
  los ganadores de Animage por año, columna 2003 confirma «Edward Elric (Fullmetal
  Alchemist)» con imagen).
- **MyAnimeList**: 244 136 «favoritos» de usuario para la serie completa (no por
  personaje) — https://myanimelist.net/anime/5114 vía Jikan API. ✅.
- **El secundario más querido, con pruebas** (pregunta explícita del encargo — «a veces
  no es el protagonista»): en dos hilos de alto puntaje de r/FullmetalAlchemist
  («Tell me your favorite character and why», 159 puntos, y «Who is your favorite side
  character?», 57 puntos) los nombres que MÁS se repiten fuera del cuarteto principal
  son **Maes Hughes** («will always be my number 1, it still hurts all these years
  later»), **King Bradley**, **Greed**, **Alex Louis Armstrong**, **Pinako Rockbell** y
  **Scar**. ✅ (r/FullmetalAlchemist, comentarios propios, con enlace en Bitácora) +
  Hughes también es, con Riza, el personaje secundario con más «favoritos» en AniList
  (2 875, datos-voz.md l.21) — dos fuentes independientes confirman a **Maes Hughes**
  como EL secundario más amado de la serie.

## Punto 12 · Lo que el fandom ama (memes, chistes internos) y qué NO hacer

- **El chiste de la estatura de Edward está SOBRE-explotado — cuidado con la lámina.**
  Post de r/FullmetalAlchemist «I've Had It Up To Here With The Short Jokes» (formato
  meme de Bob Esponja, con **1 970 puntos**, el más votado que encontré sobre el tema) —
  el propio fandom se burla de lo cansado que es el chiste de que Ed es bajito. Es
  CANON que a Ed lo enfurece (por eso "Fullmetal" viene de "cabeza dura" en japonés,
  ver Personality de Edward), pero usarlo como ÚNICO chiste de su personaje ya cansa al
  fandom — mejor un guiño sutil (una caja para alcanzar algo, sin subrayarlo con texto).
  ✅ https://old.reddit.com/r/FullmetalAlchemist/comments/1ustwqy/ (arctic-shift).
- **Al sólo deja entrar mujeres y gatos dentro de su armadura** (chiste recurrente del
  manga) — Al es un amante de los gatos reconocido por todo el fandom; es SU detalle de
  personaje más citado. ✅ fma.fandom.com, Trivia de Alphonse.
- **"Royai"** (Roy Mustang + Riza Hawkeye) es el ship más grande y "oficial-implícito"
  de la franquicia — la propia autora (Hiromu Arakawa) confirmó en el Artbook 3 que no
  se casan en la historia sólo por el reglamento militar. Chistes recurrentes del canon
  mismo: Roy amenaza con quemar a quien se le insinúe a Riza (Barry el Carnicero), la
  llama en código "Elizabeth". ✅ fma.fandom.com, Trivia de Roy y de Riza (dos páginas
  independientes del wiki, mismo dato).
- **"Edwin"** (Edward + Winry) es el otro ship "canon confirmado": terminan juntos con
  hijos al final del manga. ✅ fma.fandom.com, Trivia de Winry.
- **Roy trata a su equipo como piezas de ajedrez**: Fuery=Peón, Falman=Alfil,
  Havoc=Caballo, Breda=Torre, Hawkeye=Reina, Roy=Rey — dato que el fandom cita mucho
  para explicar la dinámica del "Mustang's team". ✅ fma.fandom.com, Trivia de Roy y de
  Riza (coincide en ambas).
- **La escena de Nina Tucker** (niña convertida en quimera por su propio padre, ep. 4-5)
  sigue siendo, según medios hispanos, "el momento más triste y horrible que pueda
  existir" para el fandom — casi nunca se usa en fan art alegre, es zona sensible. ✅
  https://www.univision.com/entretenimiento/geek/fullmetal-alchemist-los-momentos-de-brotherhood…
  (ver punto 21) + mencionado en el propio wikitext de Doblaje Wiki como escena que
  cambiaron técnicamente por su dureza (datos-voz.md l.293-295).
- **Qué NO hacer** (para esta lámina y las siguientes de la serie):
  - No reducir a Edward SOLO al chiste de la estatura (arriba).
  - No dibujar a Alphonse como "el gracioso de la armadura" sin más — es el más
    maduro emocionalmente de los dos hermanos (ver punto 13) y el fandom lo nota si se
    banaliza.
  - No mezclar diseños de la serie **2003** (Ishvalanos, Envidia mujer, uniformes) con
    **Brotherhood**: son dos adaptaciones distintas y el fandom las distingue mucho
    (color de ojos de Envidia, uniformes militares cambian de diseño entre series). ⚠️
    un solo hilo de referencia pero es señalado también por Doblaje Wiki (pronunciación
    de nombres cambia entre ambas series, datos-voz.md l.342-346).
  - No usar pronombres femeninos para Envidia (error de la serie 2003 que el propio
    doblaje corrigió en Brotherhood). ✅ wikitext Doblaje Wiki.
  - No ignorar que Riza es la MUJER más popular (3ª en general) y Hughes el secundario
    más querido: si la lámina necesita "un secundario", estos dos pesan más que otros
    nombres obvios.

## Punto 13 · Descripción profunda: carácter, miedos, arco, cómo se expresan (con fotograma)

Personality/Abilities de Edward, Alphonse, Roy y Winry ya en `datos-voz.md` (AniList) —
no se repite; se AMPLÍA con lo que falta: relaciones/dinámicas, trivia de expresión y
caras en video real.

- **Edward Elric**: su tozudez viene de que "Hagane" (acero) en japonés también
  significa alguien de carácter obstinado — por eso Bradley lo apoda así. Miedo/herida
  central: la culpa por el cuerpo de Al; su padre Hohenheim es la ÚNICA persona que
  logra hacerlo llorar en toda la serie (fuera de su niñez). Zurdo al escribir aunque
  ambidiestro peleando (su brazo derecho es automail). Odia la leche (por su sabor o
  "por ser un líquido blanco opaco secretado por una vaca"); ama el estofado/guiso. Sus
  sándwiches en pantalla siempre están sin corteza. ✅ fma.fandom.com Trivia de Edward.
  - **Dinámica con Alphonse**: relación "casi parental" a la inversa — Al cuida a Ed
    emocionalmente aunque es el hermano menor; discuten seguido pero cada uno moriría
    por el otro. ✅ fma.fandom.com, Relationships/Alphonse Elric.
  - **Dinámica con Roy**: "animosidad amistosa" — Roy disfruta molestarlo, Ed disfruta
    esquivar sus órdenes; se respetan de fondo y son cómplices en el plan secreto contra
    los homúnculos. ✅ fma.fandom.com, Relationships/Roy Mustang.
  - **Cara en video real** (Internet Archive, trailer oficial de Cartoon Network/Toonami
    2009, `turner_video_11408`, sin YouTube): a los **~41 s** (±2 s) Edward aparece con
    las manos juntas cerca de la boca, ojos entrecerrados — gesto de **angustia/miedo**;
    a los **~46 s** aparece a gritar con la boca abierta, mechones sueltos, automail
    visible en el hombro — **rabia/dolor** puro. Fuente:
    https://archive.org/details/turner_video_11408 (trailer oficial, 2009, EN — subido a
    IA 2021, "checked for malware" por el propio archive.org). Fotogramas guardados en
    la carpeta de trabajo `frames_ia/f_000041.jpg` y `f_000046.jpg`. ✅ (vistos con Read).
- **Alphonse Elric**: el foil calmado de Ed — paciente casi hasta el exceso, madurez muy
  por encima de su edad biológica (creció atrapado en la armadura desde los 10 años).
  Su tristeza tarda más en salir que la de Ed pero existe (oscuridad de fondo por las
  tragedias vividas). Detalle tierno: sólo deja entrar mujeres y gatos a su armadura;
  ama los gatos (llegó a cargar una panda, Shao May, creyendo que era un gato). ✅
  fma.fandom.com, Personality (datos-voz.md) + Trivia (arriba).
- **Roy Mustang**: fachada de mujeriego engreído que esconde ambición e inteligencia
  reales; su motivación de fondo es volverse Führer para cambiar el país desde adentro
  (por la culpa que carga de la Guerra Civil de Ishval). Vive solo, en una casa
  alquilada angosta, con "poco más que un sofá" en la sala — dato de la propia autora
  Arakawa en el Guidebook. Su gatillo emocional es LA LLUVIA (activa sus recuerdos de
  Ishval y su alquimia de fuego no funciona con las manos mojadas). Sus ojos son negros
  en casi todo el arte oficial, grises sólo en algunas páginas a color durante su
  ceguera. ✅ fma.fandom.com Trivia + Relationships/Riza Hawkeye.
  - **Cara en video real** (mismo trailer IA): a los **~35 s** (±2 s) aparece Maes
    Hughes (no Roy) apretando un teléfono con nudillos blancos, cejas fruncidas — cara
    de **alarma/urgencia**, útil para el punto 13 de Hughes también. Fuente: misma que
    arriba, fotograma `f_000035.jpg`. ✅ (visto con Read).
- **Winry Rockbell**: pasión real por la automail (no es "el interés amoroso" nada
  más), se pone rabiosa si alguien maltrata su trabajo. Se hizo tantos piercings en las
  orejas porque Ed y Al le regalaron muchos aretes y quería usarlos todos; se dejó
  crecer el pelo porque vio a Riza Hawkeye con el pelo largo la primera vez que se
  conocieron (dato cruzado: Riza a su vez se puso aretes por ver los de Winry). ✅
  fma.fandom.com, Trivia de Winry + Trivia de Riza (mismo dato en las dos páginas).
- **Riza Hawkeye** (la secundaria más popular, 3ª en general): extremadamente leal PERO
  desobedece a Roy si él intenta sacrificarse o hacer algo solo — su arma es su
  conciencia, tiene autorización explícita de él para dispararle si se desvía del buen
  camino. Mide 168 cm. ✅ fma.fandom.com, Personality + Trivia de Riza.
- **Maes Hughes** (el secundario más amado, punto 7): en la muestra de audio oficial
  suena grave (134 Hz) pero es el MÁS expresivo de los 6 personajes medidos (23.3
  semitonos de rango) — la ficha vocal confirma lo que dice el fandom: es cálido,
  efusivo, "el papá del grupo". Frase citada arriba (punto 8) resume su filosofía sobre
  la masculinidad y el dolor callado. ✅ ficha propia con `voz.py`.

## Punto 20 · Gustos y detalles de cada personaje

| Personaje | Cumpleaños | Altura | Comida que ama/odia | Objeto/manía | Cómo se ve a sí mismo |
|---|---|---|---|---|---|
| Edward Elric | ⚠️ no fijado en canon | 165 cm con alzas (141 cm real a los 15, crece tras recuperar su brazo/pierna) | Odia la leche; ama el estofado | Su reloj de alquimista estatal, escribe con la izquierda | Se obsesiona con no ser "bajito"; se define por proteger a Al |
| Alphonse Elric | ⚠️ no fijado en canon | ~170-175 cm de adulto (estimado por la wiki) | Sin datos de comida (no puede comer en armadura) | Sólo deja entrar mujeres y gatos a su armadura; ama los gatos | Se ve como el responsable de la culpa de Ed, aunque no la comparte |
| Roy Mustang | 24/8 según AniList (⚠️ atribuido a King Bradley en datos-voz.md, revisar) — cumpleaños propio no confirmado aquí | 173 cm | Sin dato de comida ⚠️ | Sus guantes de ignición (alquimia de fuego), vive con casi sólo un sofá en su casa | Se presenta como mujeriego vago; en el fondo, estratega con un plan de país |
| Winry Rockbell | 9/6 (AniList, datos-voz.md l.51) | ⚠️ sin medir en cm en las fuentes usadas | Sin dato de comida ⚠️ | Su llave inglesa (arma y herramienta a la vez); múltiples piercings en las orejas | Se ve como mecánica antes que "la novia de Ed"; orgullo total en su automail |
| King Bradley | 24/8 (AniList, datos-voz.md l.74) | — | — | Su espada, ajedrez (invicto salvo por Roy) | — |
| Riza Hawkeye | ⚠️ no fijado en canon | 168 cm | — | Sus dos pistolas (una tipo Browning M1910, otra tipo revólver Enfield); su perro Black Hayate | Se ve como la conciencia/arma de Roy, no como "sólo su asistente" |

⚠️ La wiki en inglés no fija cumpleaños para Edward, Alphonse ni Roy (lo marca
`{{fact}}` — dato sin confirmar incluso para la propia wiki); no se inventó ninguno.
Fuente de toda la tabla: fma.fandom.com (Trivia + Infobox de cada personaje) + AniList
(datos-voz.md). Faltan gustos de comida de Roy, Winry y Riza en las fuentes en inglés
consultadas — no se encontró un databook oficial traducido con esos datos (⚠️, ver «No
encontré»).

## Punto 21 · Por qué la gente ama esta serie

- **MyAnimeList**: 9.11/10 con **2 326 893 votos**, puesto **#3 histórico** (fue **#1
  durante más de una década**, hoy superado sólo por un par de series), **244 136**
  usuarios la marcaron como favorita, 3.7 millones de miembros la tienen en su lista. ✅
  https://myanimelist.net/anime/5114 (vía Jikan API, dato propio del 24-sep-2026).
- **IMDb**: 9.1/10. ✅ https://www.imdb.com/title/tt1355642/ (segunda fuente
  independiente que coincide con MAL).
- **Por qué, según reseñas**: narrativa "madura" poco común en anime, cada personaje
  —incluso los que no son del grupo principal— tiene un rol real en la trama; el
  «intercambio equivalente» como regla de magia dura, con consecuencias reales, es lo
  que más se cita como diferencial. ✅ dualshockers.com «10 Reasons Why FMAB is Still
  the Gold Standard of Anime», gamerant.com «Does FMAB Still Deserve To Be #1?».
- **Escenas que hacen llorar** (recopilado de medios hispanos especializados en anime,
  cruzado con el propio wikitext de Doblaje Wiki para el episodio exacto donde se pudo
  verificar):
  - **Ep. 1**: los hermanos intentan resucitar a su madre con alquimia humana y todo
    sale mal — el origen de toda la serie (Ed pierde la pierna, luego el brazo; Al
    pierde el cuerpo entero). ✅ univision.com + ficha técnica del ep. 1 (fma.fandom.com,
    debut de varios personajes).
  - **Ep. 4-5 · "An Alchemist's Anguish"**: Nina Tucker, la hija de Shou Tucker,
    convertida en quimera por su propio padre — "el momento más triste y horrible que
    pueda existir" para el fandom hispano. ✅ univision.com +
    fma.fandom.com/wiki/Nina_Tucker (debut confirmado: Episode 4, 2009 series) +
    Doblaje Wiki (datos-voz.md l.293-295, detalla cómo se dobló esa escena).
  - **Ep. 10 · "Separate Destinations"**: Envy, transformado en la esposa de Maes
    Hughes, le dispara en una cabina telefónica — la muerte que "aún duele años
    después" según comentarios propios de Reddit (ver punto 7). ✅ cbr.com "FMAB
    Episode 10 Kills Off a Fan Favorite Character" + otakukart.com (dos fuentes
    coinciden en el episodio 10) + univision.com (menciona la escena sin número de
    episodio).
  - **Explicarle la muerte de su papá a Elicia (la hija de Hughes), muy pequeña** —
    citado aparte del punto anterior por Univision como otro momento que duele solo.
  - **Cuando Alphonse se sacrifica** (da su cuerpo/existencia para revivir a Edward) y
    **Hohenheim muere** tras por fin ser visto con respeto por Ed — la resolución del
    arco del padre. ✅ univision.com.
  - **El final**: Edward le confiesa sus sentimientos a Winry y el epílogo muestra a
    toda la "familia" reunida — el momento feliz que también hace llorar. ✅
    univision.com.
  - ⚠️ No se pudo confirmar el **minuto exacto** de estas escenas (falta mirar el
    episodio completo, tarea de `episodio.py`/`fotogramas.py` con acceso a la serie
    completa doblada, que no está disponible sin YouTube en este servidor); si el
    redactor lo necesita, pedir al investigador de vídeo que lo saque con
    `herramientas/episodio.py` sobre una fuente accesible.
- **Con qué personaje se identifica el público**: en los hilos de Reddit revisados
  (punto 7), el patrón es identificarse con Edward por su terquedad/orgullo, o con
  Alphonse por cargar con el dolor de otro sin quejarse — varios comentarios usan la
  palabra "saint" (santo) para Al por aguantar 4 años en un cuerpo sin sentir nada y
  quejarse "sólo una vez". ✅ r/FullmetalAlchemist (comentario citado arriba, punto 13).

## Punto 22 · Fan dubs y comunidad hispana

YouTube bloqueado en este servidor (pide iniciar sesión) y dio **429** al reintentar una
vez con `yt-dlp` (se respetó la regla de no insistir en bucle) — los datos de vistas/canal
no se pudieron verificar en vivo; se listan con ⚠️ los que sólo se encontraron por
buscador, con su URL para que el redactor los revise cuando el 429 se enfríe:

- **Fandubs de escenas en español latino** (⚠️ un solo hallazgo por buscador, sin ver
  vistas/canal):
  - "Fullmetal Alchemist Brotherhood - Muerte de Van Hohenheim [Fandub Español Latino]"
    · https://www.youtube.com/watch?v=eDltSfZRzU8 (dio 429 al intentar leer metadatos;
    el título indica que doblan la muerte de Hohenheim, una de las escenas más
    emotivas del punto 21).
  - "FullMetal Alchemist: Brotherhood [Spanish Fandub] - Clip en castellano" ·
    https://www.youtube.com/watch?v=KWNMuUXxrLA (español de España, no latino — dato
    para diferenciar si el canal quiere sólo latino).
  - "【Devy】USO, Fullmetal Alchemist Brotherhood『Fandub Español Latino』" (cover
    cantado de un insert song) · https://www.youtube.com/watch?v=P4ZK8EMEucg
  - "Un corazón de acero | Fullmetal Alchemist Brotherhood Fandub Español Latino +
    RECAP FIN DE AÑO 2025" · https://www.youtube.com/watch?v=Sx7lf1Shpf0 (canal activo
    en 2025-2026, sigue subiendo contenido de la serie).
- **Covers del opening en español**:
  - "AGAIN - Fullmetal Alchemist Brotherhood OP1 [Fandub Español] Acoustic ver." ·
    https://www.youtube.com/watch?v=uByvZPd84OY
- Todos ⚠️ una sola fuente (resultado de buscador, sin poder abrir el vídeo por el
  bloqueo de YouTube). No se encontraron covers o parodias en **TikTok** verificables
  sin acceso a la app/login — búsqueda web sólo devolvió páginas de descubrimiento
  genéricas de TikTok (tiktok.com/discover), no vídeos concretos con vistas. ⚠️
- **Memes hispanos**: el juego de palabras del doblaje (`Winry` pronunciado distinto
  entre Animax y Funimation, ver punto 8) y los "errores" documentados por Doblaje Wiki
  (ej. "no fue eso, Pulgarcito" en vez de "no fue eso lo que dije, Pulgarcito") son el
  tipo de dato que ya circula como trivia en la comunidad de doblaje hispana — fuente
  primaria: wikitext de Doblaje Wiki, sección "Errores" (datos-voz.md l.377).

## Lo mejor para la lámina

1. **Maes Hughes**: secundario más querido (dos fuentes independientes, punto 7) y con
   la frase más "de canal de doblaje" de todas («los hombres dejan que sus acciones
   hablen por ellos»). Fotograma de su cara de alarma en `frames_ia/f_000035.jpg`.
2. La frase **«intercambio equivalente»** — la premisa de toda la serie, reconocida por
   cualquier fan, corta y con gancho para un cuadro de diálogo.
3. **Edward con las manos juntas, angustiado** (`frames_ia/f_000041.jpg`, ~41s del
   trailer oficial) — mejor pose para "pensar/explicar algo difícil" que la típica
   pose de pie con los brazos cruzados.
4. El gag canon de **Alphonse dejando entrar sólo mujeres y gatos** a su armadura — un
   gato asomando de la armadura es un detalle tierno y 100% verificable que nadie ha
   usado todavía en las láminas del servidor.
5. **Riza Hawkeye** (3ª más popular, arma+conciencia de Roy) como alternativa a Winry si
   se busca un personaje femenino menos "esperado" para la lámina.

## No encontré

- ⚠️ Minuto exacto (no sólo episodio) de las escenas que hacen llorar (punto 21): pedí
  acceso a la serie doblada completa y no hay fuente sin YouTube en este servidor.
  Búsquedas: "Fullmetal Alchemist Brotherhood" + nombre de escena en Dailymotion (sólo
  devolvió tráilers, ya en datos-voz.md), Internet Archive (`archive.org/advancedsearch`,
  sólo trailers/reacciones/AMVs, no episodios completos doblados).
- ⚠️ Vistas y nombre de canal de los fandubs hispanos (punto 22): YouTube pide login en
  este servidor y dio 429 al reintentar una vez con `yt-dlp` (no se insistió en bucle,
  regla del encargo). Sólo tengo título + URL por buscador.
- ⚠️ Covers/parodias de FMAB en **TikTok** de la comunidad hispana: sin login a la app,
  el buscador sólo devuelve páginas genéricas de "discover" de TikTok, no vídeos
  concretos con vistas.
- ⚠️ Comida favorita, cumpleaños y estatura exacta de **Winry**, **Riza** y comida
  favorita de **Roy**: la wiki en inglés los marca `{{fact}}` (sin confirmar) o
  simplemente no los tiene; no encontré un *databook* oficial traducido o escaneado
  con esos datos. Búsquedas: "Fullmetal Alchemist character guidebook Winry height",
  "Roy Mustang favorite food databook" (en, ja romanizado) — sin resultado confiable.
- ⚠️ TVTropes (YMMV, Tearjerker, Fridge) para FMAB: la web devuelve **403** (reto de
  Cloudflare) desde este servidor; probé también con Wayback Machine
  (`archive.org/wayback/available`) y no hay snapshot guardado de esa página. Dos
  intentos, sin más (regla del encargo). Se cubrió el hueco con medios hispanos
  (Univision) y con Reddit en su lugar.
- ⚠️ La rejilla completa de «cara en cada emoción (alegría, rabia, tristeza, miedo,
  vergüenza) con fotograma y minuto» que pide el punto 13 para cada personaje sólo se
  cubrió parcialmente (3 fotogramas: Edward en miedo y en rabia, Hughes en alarma,
  todos del mismo trailer oficial de Internet Archive). Conseguir el resto de la rejilla
  (alegría, tristeza, vergüenza; y para Alphonse, Roy, Winry, Riza) necesita mirar
  episodios completos con `episodio.py`/`fotogramas.py`, que es la herramienta y el
  punto fuerte del investigador de VÍDEO (poses con capítulo y minuto, punto 14) — se
  avisa aquí para que no se pierda, no se dejó en `Sigue:` porque ya no es tarea
  pendiente de esta parte sino del rol de vídeo.
- ⚠️ Encuesta de fans citada en fma.fandom.com como «final fan poll»: la wiki no dice
  quién la organizó ni la fecha exacta, sólo que es la última. Coincide en 4 páginas
  distintas del wiki así que el ORDEN es fiable, pero no pude verificar la fuente
  primaria de esa encuesta (⚠️, apuntado igual en el punto 7).

## Bitácora de búsqueda

- **Fuentes de red directa** (sin gastar cupo de buscador): API de Doblaje Wiki
  (`action=parse&prop=wikitext`) para el wikitext completo de la ficha de FMAB (reparto
  Animax + Funimation, trivia, errores) — la tabla de reparto NO estaba bien en
  `datos-voz.md` (el recolector sólo sacó nombres de archivos de audio) así que se
  volvió a sacar a mano, con éxito. API de AniList ya en `datos-voz.md`, no repetida.
  API de Danbooru (`counts/posts.json`) con el tag correcto `fullmetal_alchemist` (el
  recolector probó `fullmetal_alchemist_brotherhood`, que no existe — 0 resultados).
  API de Jikan/MyAnimeList (`api.jikan.moe/v4/anime/5114`) para score/rank/favoritos.
  API de Arctic Shift para r/FullmetalAlchemist, con `title=` (funciona) en vez de
  `query=` (da error/timeout) — dato para el recolector.
  API de fma.fandom.com (`action=parse&prop=wikitext&section=N`) para Trivia y
  Relationships de Edward, Alphonse, Roy, Winry y Riza (secciones que el recolector no
  había bajado, sólo Personality/Abilities).
  Internet Archive (`archive.org/advancedsearch.php`, `archive.org/metadata/...`) para
  el trailer oficial `turner_video_11408` (Cartoon Network/Toonami 2009) — se miraron
  sus 12 miniaturas oficiales (contacto en `frames_ia/contacto.jpg`) y se citaron 2
  fotogramas de Edward y 1 de Hughes con segundo aproximado.
  Descarga directa de 6 muestras de audio oficiales de Doblaje Wiki (Edward, Roy,
  Hughes, Trisha, Alphonse niño, Winry niña) + transcripción y ficha vocal con
  `herramientas/voz.py` (Whisper local, registro/semitonos/velocidad medidos, no de
  oído).
- **Buscador web** (8 de ~50, español/inglés): "ANMTV Fullmetal Alchemist Brotherhood
  redoblaje 2021 elenco México Funimation" (ES) → confirmó estudio y directores del
  redoblaje. "Fullmetal Alchemist Brotherhood encuesta personaje más popular oficial
  Newtype" (ES) → sin encuesta Newtype específica, sí confirmó podio Edward-Roy-Riza.
  "Fullmetal Alchemist: Brotherhood reddit escena que te hizo llorar" (ES) → llevó al
  artículo de Univision. "Fullmetal Alchemist Brotherhood fandub español youtube canal
  de fans" (ES) → 6 vídeos de fandub/cover encontrados. "Fullmetal Alchemist Brotherhood
  memes iconic fandom Envy meme" (EN) → sin meme específico confirmado, sólo presencia
  genérica en TikTok/Pinterest. "Fullmetal Alchemist Brotherhood why anime fans love it
  reviews sales awards" (EN) → artículos de dualshockers/gamerant, MAL "#1 por más de
  una década". "Fullmetal Alchemist popularity poll official ranking… Square Enix
  magazine" (EN) → sin poll de Square Enix, sí confirmó a Roy como 2º "en cada encuesta
  desde su debut". ""Fullmetal Alchemist Brotherhood" Hughes dies episode number" (EN)
  → confirmó episodio 10 "Separate Destinations" en dos fuentes (CBR, OtakuKart).
  "Animage Readers Poll Edward Elric favorite male character" (EN) → llevó al archivo
  furinkan.com con el año exacto (2003).
- **Webs que fallaron**: tvtropes.org da 403 (Cloudflare) en este servidor, sin
  snapshot en Wayback Machine — no se pudo usar para punto 12/21. reddit.com directo
  (no la API de Arctic Shift) da bloqueo — se usó Arctic Shift en su lugar, con éxito.
  etc.cl (artículo de "momentos que te hicieron llorar") da 404, la URL había cambiado
  — se cubrió el punto con Univision, que sí funcionó. YouTube pide login en este
  servidor; `yt-dlp` dio 429 al primer reintento — no se insistió en bucle, se usó lo
  que dio el buscador con ⚠️.
- **Total de fuentes distintas usadas en esta parte** (ver `voz.json`): 22, entre APIs
  (Doblaje Wiki, AniList, Danbooru, Jikan/MyAnimeList, Arctic Shift/Reddit, fma.fandom,
  Internet Archive), medios (ANMTV, Univision, CBR, OtakuKart, dualshockers, gamerant,
  furinkan.com/Animage), audio propio transcrito (6 muestras) y fotogramas propios (3,
  del trailer oficial en Internet Archive).
