# Investigador de VOZ Y PERSONAJES · Rick and Morty (repaso, 25-sep-2026)

Puntos de ENCARGO.md: **7** (principales/secundarios y popularidad), **8** (doblaje
latino), **12** (fandom y qué no hacer), **13** (personajes a fondo), **20**
(gustos), **21** (por qué la aman), **22** (fan dubs). Parto de
`partes/datos-voz.md` y de las secciones que ya tiene `biblia.md` (leídas con
`seccion.py --rol voz` y `--avisos`). **No reescribo lo que ya está bien**: aquí
dejo sólo correcciones a los ⚠️ existentes y lo que faltaba del todo (20, 21, 22
no tenían sección en la biblia). El redactor decide cómo fusionarlo.

Formato: `- dato · fuente(s) · ✅/⚠️ · minuto o nota`.

---

## 8 · Doblaje latino — los 10 ⚠️ de la biblia, revisados

Fuente base para todo este bloque:
`https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Rick_y_Morty`
(wikitext completo, secciones «Historia del doblaje», «Reparto» y «Datos de
interés» — más completas que lo que sacó `recolectar.py`, que sólo trajo
nombres de archivo de audio, no la tabla de actores).

- **Director de doblaje T1-T2: Ángel Balam** (autodirección desde la T3) ·
  [Doblaje Wiki, «Historia del doblaje» de la serie](https://doblaje.fandom.com/es/wiki/Rick_y_Morty#Historia_del_doblaje)
  y [ficha propia de Ángel Balam, sección «Dirección de doblaje»](https://doblaje.fandom.com/es/wiki/Angel_Balam)
  (páginas distintas de la misma wiki, mantenidas por separado) · ✅ (dos
  páginas) — **esto resuelve el «no lo encontré» de la biblia** (sección 10,
  «Lo importante»/«Lo que no pude verificar»).
- **Estudio, corregido**: Turner encargó el doblaje a Sonoclips (hoy IDS), pero
  Sonoclips **subcontrató** a **Dvinxi Studios** para grabar las temporadas
  1-2 (dirigidas por Ángel Balam); la T3 la grabó **AGP Producciones**; desde
  la T4, **IDS graba en su propio estudio** (por la pandemia y porque vio el
  éxito de la serie, puso cláusula de grabación presencial) · [Doblaje Wiki,
  «Historia del doblaje»](https://doblaje.fandom.com/es/wiki/Rick_y_Morty#Historia_del_doblaje) ·
  ⚠️ (un sitio, pero es la wiki especializada en esto; no encontré una segunda
  fuente que entre en el detalle de la subcontratación) — **la biblia decía
  sólo «Sonoclips, hoy IDS» como si hubiera doblado todo desde el principio:
  es impreciso, corregir**.
- **Sr. Meeseeks: Ángel Lugo** · ✅ **dos fuentes independientes**:
  [tabla de reparto del episodio 1×05 «Meeseeks destructores» en Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Rick_y_Morty/1.%C2%AA_temporada)
  y [ficha de Ángel Lugo en Fandoblaje Wiki](https://fandoblaje.fandom.com/es/wiki/%C3%81ngel_Lugo)
  (wiki distinta a Doblaje Wiki). Antes la biblia lo daba con una sola fuente.
- **Beth Smith, las tres voces, confirmadas**:
  - **Rebeca Aponte** (T1-6) · ✅ [Doblaje Wiki, tabla de reparto](https://doblaje.fandom.com/es/wiki/Rick_y_Morty)
    y [ficha de Rebeca Aponte en Fandoblaje Wiki](https://fandoblaje.fandom.com/es/wiki/Rebeca_Aponte)
    («Beth Smith - Rick y Morty»).
  - **Carmen Lugo** (T7-8; Rebeca se mudó a España en 2023) · ✅ [Doblaje Wiki,
    tabla de reparto](https://doblaje.fandom.com/es/wiki/Rick_y_Morty) y
    [ficha propia de Carmen Lugo en Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Carmen_Lugo)
    («Beth Smith (2ª voz) / Voces adicionales, 2013-presente»).
  - **Arlet Matute** (T9-, porque Carmen se mudó a España en 2025) · dato
    **nuevo, no estaba en la biblia** · ✅ [Doblaje Wiki, «Historia del
    doblaje»](https://doblaje.fandom.com/es/wiki/Rick_y_Morty#Historia_del_doblaje)
    y [World Dubbing News en X, 2026](https://x.com/WDN_Topic/status/2058748920721768777)
    («La actriz Arlet Matute se une al elenco de la novena temporada de
    #RickandMorty interpretando a Beth Smith»).
- **Mr. Poopybutthole / Sr. Pantalones de Popó**: no tenía actor en la biblia
  («Ooh-wee! ⚠️» sin nombre). **Reinaldo Rojas** (T2-3) → **Nayip Rodríguez**
  (T4-6, hasta que dejó IDS) → **Jaime de Abreu** (T7-) · [Doblaje Wiki,
  «Sobre el reparto»](https://doblaje.fandom.com/es/wiki/Rick_y_Morty#Sobre_el_reparto) ·
  ⚠️ (una sola fuente; no encontré una ficha de actor independiente que lo
  confirme — sí lo busqué en Fandoblaje, ninguno de los tres nombres tiene
  página ahí).
- **Rick y Morty: El anime (2024), reparto confirmado con segunda fuente**:
  **Rick: Gerardo Reyero. Morty: Miguel Ángel Leal. Summer: Constanza de la
  Rosa. Beth: Elena Díaz Toledo. Jerry: Héctor Indriago. Elle (personaje
  nuevo): Abigaly Claro** · ✅ [ANMTV, 11-jul-2024, «Max revela cambios en el
  reparto del doblaje latino»](https://www.anmtvla.com/2024/07/rick-y-morty-el-anime-max-revela.html)
  (por Albert Cardozo, cita textual del elenco) y [Doblaje Wiki, «Rick y
  Morty: El anime»](https://doblaje.fandom.com/es/wiki/Rick_y_Morty:_El_anime).
  Antes la biblia sólo confirmaba Rick y Morty (Doblaje Wiki+ANMTV+TVLaint) y
  dejaba Summer y Beth con ⚠️: **ya quedan ✅**.
- **Por qué cambiaron el elenco del anime**: fue decisión de la propia Max/IDS
  «como parte de una medida global, para dar un grado de diferencia» respecto
  a la serie original (venezolana) — no fue porque las pruebas venezolanas
  fallaran, como decía la biblia; ANMTV no dice eso · [ANMTV](https://www.anmtvla.com/2024/07/rick-y-morty-el-anime-max-revela.html) ·
  ✅ — **corregir esa frase en la sección 10** (dice «porque a Warner no le
  convencieron las pruebas venezolanas», eso no está en las fuentes).
- **Crossover no oficial con Los Simpson**: las primeras voces oficiales de
  Rick y Morty en español fueron en México, en el gag del sofá del episodio
  «Hazaña matemática» (2015, Los Simpson T26), un año antes de que Rick y
  Morty tuviera doblaje propio: **Ismael Castro** (Rick) y **Bruno Coronel**
  (Morty) · ✅ ya estaba en la biblia (tabla del capítulo). Dato nuevo: en
  2020, **Juan Guzmán y Eder La Barrera regrabaron esas escenas de manera no
  oficial** para un canal de YouTube (DALEHHOR STUDIOS) · [Doblaje Wiki,
  «Sobre el reparto»](https://doblaje.fandom.com/es/wiki/Rick_y_Morty#Sobre_el_reparto),
  [vídeo](https://youtu.be/QaQdbhepkH8) · ⚠️ (una fuente).

**Cumplimiento del punto 8**: de los 10 ⚠️ que marcaba `seccion.py --avisos`
en la sección 10, quedan resueltos con dos fuentes: director, Sr. Meeseeks,
Beth Smith (las tres voces) y el reparto del anime. Sigue con una sola fuente
(dejar el ⚠️): el estudio subcontratado exacto por temporada, y el actor de
Mr. Poopybutthole.

---

## 7 · Quién es el más querido (aporte a la sección 9, ya existente)

- El hilo de Reddit **«Which character do you identify with most?»** (833
  votos, 475 comentarios) sirve también para popularidad real, no sólo
  encuestas de prensa: los comentarios con más apoyo son para **Morty**,
  **Beth**, **Summer**, **Rick** y **Jerry**, en ese orden de aparición (ver
  citas exactas en el punto 21) · [Reddit](https://www.reddit.com/r/rickandmorty/comments/1r2zhxh/which_character_do_you_identify_with_most/) ·
  ✅ (hilo público, con recuento de votos verificable).
- Sr. Meeseeks tiene un hueco curioso de reconocimiento fuera del fandom: el
  bot de Discord **MEE6** tomó su nombre y parte de su imagen de Mr. Meeseeks
  · [wiki en inglés, sección Trivia](https://rickandmorty.fandom.com/wiki/Mr._Meeseeks#Trivia) ·
  ⚠️ (una fuente, dato curioso pero verificable por cualquiera que abra
  Discord y compare el logo) — **dato con gancho para un servidor de
  Discord como Sintonizando**: la lámina de #noticias-series podría jugar con
  que «hasta los bots de Discord se visten de Meeseeks».

---

## 13 · Los personajes a fondo (miedos, manías, cómo se ven a sí mismos)

Todo de la wiki en inglés (`rickandmorty.fandom.com`, secciones Trivia y
Relationships de cada personaje), comprobado con el wikitext completo
(`action=parse&prop=wikitext`), no de memoria.

### Rick Sánchez

- **Miedo real y con fuente** (no «la soledad» de memoria, como decía la
  biblia con ⚠️): **Rick le tiene miedo a los piratas** · ✅ dos episodios lo
  confirman, [«Anatomy Park»](https://rickandmorty.fandom.com/wiki/Anatomy_Park_(episode))
  y [«Unmortricken»](https://rickandmorty.fandom.com/wiki/Unmortricken)
  (citados en la propia ficha de Rick, sección Trivia).
- Lo de «llora en secreto por Morty» sí tiene fuente concreta (la biblia lo
  daba de memoria en la sección 8): en **«Close Rick-Counters of the Rick
  Kind»** Rick empieza a llorar al ver recuerdos de Morty y lo disimula
  diciendo que es «alérgico a los idiotas»; en **«A Rickle in Time»** está
  dispuesto a sacrificarse por Morty · ✅ [wiki, ficha de Rick, Trivia](https://rickandmorty.fandom.com/wiki/Rick_Sanchez#Trivia).
  Es la prueba de que si le importa, aunque lo niegue: útil para el punto 13
  («qué transmite»).
- **Cómo se ve a sí mismo**: se llama «the hardest working liver in the
  galaxy» (el hígado más trabajador de la galaxia, por lo que bebe) en
  [«Look Who's Purging Now»](https://rickandmorty.fandom.com/wiki/Look_Who%27s_Purging_Now)
  y, desde la T3, «the smartest man/being in the universe» · ✅ (wiki,
  Trivia).
- **Manías**: sostiene bebidas, dispara y toca el bajo con la mano
  **izquierda** (aunque escribe con la derecha: es ambidiestro) · ⚠️ (una
  fuente, wiki Trivia, con fotos de referencia enlazadas en la propia wiki).
  Tiene «fetiche por los planetas» ([«Childrick of Mort»](https://rickandmorty.fandom.com/wiki/Childrick_of_Mort)) ⚠️.
- **Origen hispano confirmado dentro de la ficción**: en el comentario de
  audio del episodio «Auto Erotic Assimilation», los creadores confirman que
  Rick es de origen hispano (probablemente mexicano, por el chiste del
  sombrero y bigote postizo en esa escena) · ⚠️ (una fuente, comentario de
  Blu-ray citado por la wiki, no lo pude oír yo mismo). Dato con cuidado: es
  un chiste de la serie sobre sí misma, no una biografía seria.
- **Toca el bajo y la guitarra**: fue el bajista de una banda real dentro de
  la serie, **The Flesh Curtains**, con Squanchy y Birdperson (aparece en una
  foto en la pared de Birdperson en «Get Schwifty», y en un flashback tocando
  en vivo en «Rickternal Friendshine of the Spotless Mort») · ✅ (wiki,
  Trivia, dos episodios distintos). Sirve para un concepto de lámina con
  instrumento (el plan del encargo propone «con su instrumento»).
- **Grupo sanguíneo B-Negativo** · ⚠️ (una fuente, wiki Trivia).

### Morty Smith

- **Manías/gustos**: fetiche por los pies (revelado en «Mortynight Run»);
  masturbación frecuente, tema recurrente de la serie («Something Ricked
  This Way Comes», «Total Rickall», «The Ricks Must Be Crazy») · ✅ wiki,
  varios episodios — dato **no apto para la lámina de Discord**, pero sirve
  para no escribirle diálogos «demasiado inocentes».
- **Es agnóstico** (dato explícito, no de memoria) · ⚠️ (una fuente, wiki
  Trivia).
- Bajo la Federación Galáctica su «edad legal» pasó a ser 35 años (en
  «The Rickshank Rickdemption») — es un chiste de la serie, no su edad real
  (14-17 años en la Tierra) · ✅ wiki.
- **Con quién se relaciona (para dinámicas en grupo, punto 13)**: su interés
  romántico principal es **Jessica**, su compañera de clase, desde el primer
  episodio y a lo largo de toda la serie · ✅ (aparece en múltiples
  episodios, confirmado por la wiki en la ficha de Morty y en la de Jessica).

### Summer Smith

- **Nació el 23 de noviembre de 1996** (dentro de la ficción: la wiki lo
  calcula porque, sumándole 17 años, da 2013, el año en que se estrenó la
  serie) · ⚠️ (una fuente, cálculo de la propia wiki, no un dato dicho
  directamente en pantalla).
- **Gustos confirmados en pantalla**: disfruta las versiones postapocalípticas
  de la Tierra («Rickmancing the Stone»); **odia la película «The Purge»**;
  es bastante atlética (voleibol y trofeos en su cuarto); probablemente le
  gusta el anime y la cultura japonesa (implícito, no dicho directo) · ⚠️
  (wiki, un solo sitio, aunque son hechos mostrados en pantalla).
- **Frase que la define para el canal de debate**: dice «boo-yah» (con
  variantes: «boob-yah», «boo-nah») según la situación · ✅ (wiki, varios
  episodios citados).
- **Confirmada bisexual** en «The Old Man and the Seat» (sale con hombres y
  mujeres) · ✅ wiki. Es un dato de representación que puede interesar al
  servidor (Sintonizando tiene canal de escritura y personajes).
- Es probablemente la hija favorita de Beth, según un recuerdo en «Morty's
  Mind Blowers» · ⚠️ (una fuente).
- El hábito de «orinarse cuando está en apuros, pero dice que es a
  propósito» (confirmado en tres episodios) matiza el carácter «superficial»
  que ya tenía la biblia: es orgullosa incluso cuando pierde el control · ⚠️
  (wiki, un sitio).

### Sr. Meeseeks

- **Prohibido en casi todos los universos** según Rick C-130 (cómic oficial,
  «Rick and Morty Issue 58») · ⚠️ (una fuente, y es material derivado —
  cómic con licencia oficial de Oni Press, no la serie).
- **Nombre igual en casi todos los idiomas** salvo en francés («Moniseur
  Larbin», de «sirviente») e italiano («Mr. Miguardi», de «guardi mi» —
  «mírenme» al revés) · ⚠️ (una fuente) — dato curioso, comparable con la
  adaptación latina («Sr. Meeseeks», sin cambio de nombre, según Doblaje
  Wiki en la sección 8).
- Los Meeseeks aparecen incluso en un cameo dentro del videojuego dentro de
  la serie, **Blips and Chitz**, dando consejos («Mortynight Run») · ✅ wiki.

---

## 20 · Gustos y detalles de cada personaje (sección NUEVA — no existía en la biblia)

`ENCARGO.md` punto 20 pide comida, aficiones, lo que ama y odia, cumpleaños,
altura, el objeto que siempre lleva y cómo se ve a sí mismo. Rick y Morty
**no tiene un databook/artbook oficial con fichas físicas tipo altura o
cumpleaños del elenco principal** (busqué el «Rick and Morty Character
Guide» de Dark Horse, 2020: es un libro de personajes secundarios y del
multiverso narrado como informe de un gromflomita, no trae estos datos del
elenco principal) · ⚠️ [Fandom, «Rick and Morty Character Guide»](https://rickandmorty.fandom.com/wiki/Rick_and_Morty_Character_Guide).
La wiki sólo confirma altura/cumpleaños/sangre para **Mullet Rick** y su
Morty (versiones alternativas, en el episodio «Fighting Mother»), y avisa
expresamente que **no está confirmado que apliquen al Rick y Morty
principales** · ✅ (wikitext de ambas fichas, sección Trivia, final).

| Personaje | Objeto que siempre lleva | Le encanta | Odia / le da miedo | Cómo se ve a sí mismo | Fuente |
|---|---|---|---|---|---|
| **Rick** | La pistola de portales; una petaca o vaso en la mano izquierda | Tocar el bajo/guitarra; los planetas (fetiche) | Los piratas; la rutina (quemó su propia tienda antes que llevar una rutina, en «Something Ricked This Way Comes») | «El hígado más trabajador de la galaxia»; «el hombre más inteligente del universo» | ✅/⚠️ wiki, Trivia (ver arriba) |
| **Morty** | — (depende del capítulo; a veces las botas de gancho de «Intergalactic Customs») | Jessica; los videojuegos de Blips and Chitz | El caos que trae Rick; se avergüenza fácil | Se ve «normal», pero la serie lo trata como más listo y valiente de lo que él cree (rescata Anatomy Park, se niega a matar en «Raising Gazorpazorp») | ✅/⚠️ wiki |
| **Summer** | El móvil (al inicio); el voleibol en su cuarto | Los mundos postapocalípticos; el anime (implícito) | La película «The Purge»; que la traten de niña | Al principio se preocupa por su estatus social; luego se ve como parte activa de las aventuras, compitiendo con Morty por la atención de Rick | ⚠️ wiki |
| **Sr. Meeseeks** | La caja de Meeseeks de la que sale | Cumplir la tarea y desaparecer («Existence is pain», lo contrario es su infierno) | Que le den una tarea imposible (le provoca crisis existencial) | Se ve como una herramienta de ayuda, feliz mientras dura, nunca como un ser con derecho a existir más allá de la tarea | ✅ (ya en la biblia, con fuente de subtítulos) |
| **Pepinillo Rick** | El traje de ratas cosidas (su única forma de tener «brazos») | Presumir lo que hizo («Boom, big reveal») | Ir a terapia familiar (por eso se convirtió en pepinillo) | Se ve invencible («I'm Pickle Rick!»), aunque literalmente sólo tiene ojos y boca funcionales | ✅ ya en la biblia |

---

## 21 · Por qué la gente la ama (sección NUEVA)

### Reconocimiento oficial y crítica

- **2 premios Emmy a Mejor Programa Animado**: 2018, por el episodio «Pickle
  Rick»; 2020, por «The Vat of Acid Episode» (T4) · ✅ dos fuentes:
  [Deadline, 2020](https://deadline.com/2020/09/rick-and-morty-outstanding-animated-program-1234580001/)
  y [IMDb/IndieWire, 2020](https://www.indiewire.com/awards/industry/rick-and-morty-wins-emmy-outstanding-animated-program-1234585898/).
  Nominado de nuevo en 2022 (no ganó) · ✅ [Nerds and Beyond](https://www.nerdsandbeyond.com/2022/07/12/rick-and-morty-nominated-for-outstanding-animated-program-at-the-2022-emmys/).
- **Rotten Tomatoes**: la temporada 1 tiene 97% de crítica; la 3 y la 4, 96%;
  la **temporada 9 (2026) debutó con 100% de crítica y 89% de audiencia**,
  el mejor arranque de la era post-Roiland · ✅ [CBR, sep-2026](https://www.cbr.com/rick-and-morty-season-9-rotten-tomatoes-score/)
  y [ScreenRant, sep-2026](https://screenrant.com/rick-morty-season-9-audience-rotten-tomatoes-score-debut/).
- **Éxito en streaming en 2026**: nº2 en el top 10 global de HBO Max (detrás
  de Euphoria) y nº1 en el top 10 de Apple TV · ✅ [CBR, «Global Streaming
  Hit»](https://www.cbr.com/rick-and-morty-season-9-instant-success/).

### Con qué personaje se identifica el público (y por qué, con sus propias palabras)

Hilo de Reddit **«Which character do you identify with most?»** (833 votos,
475 comentarios) · [enlace](https://www.reddit.com/r/rickandmorty/comments/1r2zhxh/which_character_do_you_identify_with_most/) · ✅ (citas literales, comprobadas con la API de Arctic Shift):

- Con **Beth**: *«I relate to Beth too the most for all the reasons you
  listed (including the weed coping habit) (…) I grew up without my dad
  around»* — el vacío del padre ausente y el potencial que sienten no haber
  cumplido.
- Con **Jerry**: *«Jerry 100%. I need a job»* — la inseguridad laboral,
  dicha con humor.
- Con **Summer**: *«Summer 10000000%»* (la respuesta con más apoyo después de
  Beth) — no explican por qué, pero es la segunda más repetida.
- Con **Morty**: *«Nah I know that on my best days I'm Morty. I'm generally a
  Jerry lol»* — Morty representa el «yo ideal», Jerry el «yo real».
- Con **Rick**: menos citado espontáneamente, más como aspiración («Rick or
  summer»).

**Para la lámina**: la gente no sólo ama a Rick por listo; se identifica con
Beth y Jerry por sus inseguridades, y con Summer como aspiración de
personalidad fuerte. Sirve para justificar que Summer sea la voz del canal de
debate (ya lo proponía la sección 9 de la biblia, por otra razón: aquí hay un
respaldo extra).

### Las escenas que hacen llorar (con capítulo, qué pasa y por qué duele)

1. **«A Rickconvenient Mort»** (T5E3, 4-jul-2021): Morty se enamora de
   **Planetina** (parodia de Capitán Planeta), su primera relación seria;
   ella se vuelve violenta defendiendo el medioambiente y Morty termina la
   relación. La escena final: Morty llora en los brazos de **Beth**, mientras
   suena **«I Am the Antichrist to You» de Kishi Bashi** (la misma canción
   sonó antes, en un montaje feliz de la pareja, y vuelve para la ruptura:
   el contraste es lo que duele) · ✅ dos fuentes: [Newsweek](https://www.newsweek.com/rick-morty-season-5-episode-3-morty-planetina-relationship-explained-1606826)
   y [ComicBook.com, sobre el videoclip musical oficial que Adult Swim
   publicó de esta escena](https://comicbook.com/anime/news/rick-and-morty-season-5-morty-planetina-break-up-flowers-music-video-adult-swim/) —
   que Adult Swim sacara un vídeo musical aparte confirma lo mucho que pegó
   la escena en el público. **Reddit** también la señala: el hilo «What is
   the saddest episode?» (403 votos) menciona Planetina como de las más
   citadas · [Reddit](https://www.reddit.com/r/rickandmorty/comments/1mde14b/what_is_the_saddest_episode_of_rick_and_morty/).
2. **«That's Amorte»** (T7E4, 5-nov-2023): la familia descubre que los
   espaguetis que comen vienen de un planeta donde la gente que se suicida se
   convierte en pasta («Morty's Suicide Spaghetti»); un anciano cuenta, en
   flashback, que fue «el último en quitarse la vida» en su planeta, lo que
   lo humaniza de golpe. Adult Swim puso **aviso de contenido** al inicio: es
   la serie hablando directo de salud mental y suicidio · ✅ [Variety,
   entrevista a Dan Harmon sobre el episodio](https://variety.com/2023/tv/news/dan-harmon-rick-and-morty-season-7-episode-4-spaghetti-interview-1235779646/)
   y [Wikipedia/IMDb, resumen y recepción](https://en.wikipedia.org/wiki/That%27s_Amorte).
   En Reddit, un comentario del hilo de las escenas más tristes: *«the
   flashback from the old man who was last to kill himself just hit me. It
   humanizes him»* (403 votos el hilo) · [Reddit](https://www.reddit.com/r/rickandmorty/comments/1mde14b/what_is_the_saddest_episode_of_rick_and_morty/).
3. Hilo de Reddit **«What is your saddest scene?»** (625 votos, 137
   comentarios) y **«Is this the saddest scene in the entire show?»** (2004
   votos, 118 comentarios) confirman que estas dos (Planetina y el spaghetti)
   son las más repetidas por los fans, con la parte final de la temporada 8
   también mencionada · ⚠️ (no llegué a identificar el episodio exacto de esa
   mención de la T8; queda para quien mire el capítulo final de esa
   temporada).

---

## 22 · Fan dubs y comunidad hispana (sección NUEVA)

Fuente para todo: búsqueda web + metadatos reales bajados con `yt-dlp
--skip-download` (no de memoria: canal, fecha y vistas confirmados uno por
uno).

| Fandub | Canal | Fecha | Vistas | Enlace |
|---|---|---|---|---|
| Escena de Pickle Rick, doblada por fans | **zeusupchuck** | 08-ago-2017 | 17 820 | ✅ [YouTube](https://www.youtube.com/watch?v=54KRtXDG1jU) |
| «Rick & Morty - Allahu Akbar» (escena cómica doblada) | **Kitsumaur** | 03-may-2017 | 6 037 | ✅ [YouTube](https://www.youtube.com/watch?v=nKvcKRyR_fY) |
| «Rick and Morty Señor Mezeeks Fandub» (un solo actor dobla a todos, primer trabajo del canal) | **Moises Aldana** | 13-jul-2018 | 81 | ✅ [YouTube](https://www.youtube.com/watch?v=RKui4ah87xY) |
| «RICK Y MORTY ROBAN EL OMNITRIX» (crossover fandub con Ben 10) | **Kicker Professional** | sin confirmar (YouTube no respondió a tiempo) | sin confirmar | ⚠️ [YouTube](https://www.youtube.com/watch?v=UL5uk05WVCg) |
| «EL FUTURO DE RICK Y MORTY» (Short) | **CHUCKLEBONE** | sin confirmar | sin confirmar | ⚠️ [YouTube shorts](https://www.youtube.com/shorts/vugSeeML1nQ) |

- **No hay covers de opening cantado**: Rick and Morty no tiene una canción de
  entrada con letra (el «tema» es un riff de guitarra de Ryan Elder sobre la
  animación del título) · ⚠️ (no encontré covers musicales del tema por esto
  mismo; sí hay muchos fandubs de escenas y memes, que es lo que se cita
  arriba).
- **Memes y parodias hispanas**: colecciones activas en
  [Memedroid, «Rick Y Morty en español»](https://es.memedroid.com/memes/tag/rick+y+morty)
  y audios de TikTok en español (categoría [«Audios De Rick Y Morty En
  Español»](https://www.tiktok.com/discover/audios-de-rick-y-morty-en-espa%C3%B1ol)) ·
  ⚠️ (categorías activas, no conteo exacto de vistas por vídeo individual).
- **Comunidad hispana de doblaje comentando el propio doblaje oficial**: hay
  vídeos de doblaje profesional hispano (canal «estrelladoblaje» en TikTok)
  hablando específicamente del cambio de voz de Beth · ⚠️ (una fuente,
  [TikTok](https://www.tiktok.com/@estrelladoblaje/video/6994486723602386182)) —
  dato interesante para un servidor de doblaje: la comunidad de actores de
  voz hispanos sigue de cerca los cambios de reparto de esta serie en
  particular.

---

## Lo mejor para la lámina (voz y personajes)

1. **Ángel Balam como director T1-2** y el detalle de que **Sonoclips
   subcontrató** el doblaje en vez de hacerlo en su propio estudio hasta la
   T4: da contexto real para un texto de «ficha del doblaje» en el canal.
2. La canción **«I Am the Antichrist to You»** y el quiebre de Morty con
   Planetina (T5E3): si el canal alguna vez habla de «momentos que
   destrozan», es la referencia con más respaldo (Reddit + vídeo musical
   oficial de Adult Swim).
3. El hilo de Reddit de identificación (833 votos): confirma que **Summer**
   funciona como personaje de «opinar fuerte» (ya lo decía la biblia) y que
   **Beth** y **Jerry** son con quienes más se identifica la gente por sus
   inseguridades — un ángulo humano para textos del canal, más allá del
   chiste fácil.
4. El **Sr. Meeseeks y el bot MEE6 de Discord**: gancho literal para un
   servidor de Discord (el propio Discord ya «citó» a Meeseeks sin saberlo).
5. Tres fandubs reales de canales hispanoamericanos con vistas confirmadas,
   por si el canal quiere destacar doblaje de fans en algún evento.

---

## No encontré (búsquedas hechas, no es que no exista)

- ⚠️ **Encuesta oficial de popularidad** de Adult Swim: ya la biblia decía que
  no existe (sección 9); confirmo que tampoco la encontré yo, buscando en
  inglés («Rick and Morty official character poll», «Adult Swim fan
  favorite character survey») y en español.
- ⚠️ **Altura, cumpleaños y comida favorita reales** de Rick, Morty y Summer
  (personajes principales, no versiones alternativas): busqué en el
  «Rick and Morty Character Guide» (Dark Horse, 2020) y en la wiki; sólo hay
  estos datos para **Mullet Rick** y su Morty (versión alterna), con aviso
  expreso de que no se sabe si aplican a los protagonistas. No es que la
  wiki lo esconda: literalmente no está resuelto en el canon.
- ⚠️ **Actor de doblaje latino confirmado con dos fuentes independientes**
  para Mr. Poopybutthole (me quedé con Doblaje Wiki sola: Reinaldo Rojas →
  Nayip Rodríguez → Jaime de Abreu). Busqué los tres nombres en Fandoblaje
  Wiki y no tienen ficha ahí.
- ⚠️ **Vistas de «Kicker Professional» y «CHUCKLEBONE»** (fandubs): `yt-dlp`
  no devolvió datos a tiempo en esta tanda (puede ser el bloqueo por ratos
  que avisa AYUDANTE.md); los enlaces quedan puestos igual, sin cifra.
- ⚠️ **Segunda fuente para «Rick es ambidiestro»** y el «fetiche por los
  planetas»: son datos de Trivia de la wiki en inglés con capturas de pantalla
  como referencia, pero no encontré un artículo de prensa que los repita.
- No encontré **cover de opening cantado en español**: expliqué por qué
  (la serie no tiene tema cantado) en el punto 22, no es una búsqueda floja.
- ⚠️ **«Su cara en cada emoción» (alegría, rabia, tristeza, miedo, vergüenza)
  con fotograma y minuto, para los 5 personajes** (punto 13, pedido completo):
  la sección 8 de la biblia ya reutiliza fotogramas numerados por el
  investigador de imagen para **rabia** (fotograma 1, Rick; fotograma 3,
  Summer) y **duda/temor leve** (fotograma 2, Morty). Me faltó cubrir
  **alegría, tristeza y vergüenza** de cada uno: no tengo acceso directo a
  los fotogramas numerados (son del investigador de imagen, vía
  `investigar_serie.py`) ni corrí `fotogramas.py` sobre escenas nuevas en
  esta tanda (herramienta pensada para el rol de vídeo). Sí dejé, en el
  punto 21, dos escenas con minuto de sobra para sacar esos fotogramas
  después: Morty llorando en «A Rickconvenient Mort» (T5E3, tristeza) y el
  Sr. Meeseeks gritando «Existence is pain» (1×05, min. 00:16:42, ya citado
  en la biblia, entre rabia y desesperación).

---

## Bitácora de búsqueda (segunda pasada, red abierta)

| # | Idioma | Búsqueda / fuente |
|---|---|---|
| 1 | ES | API de Doblaje Wiki, wikitext completo de «Rick y Morty» (secciones Historia del doblaje, Reparto, Datos de interés) |
| 2 | ES | API de Doblaje Wiki, wikitext de «Rick y Morty/1.ª temporada» (tabla de reparto del episodio 1×05, Meeseeks) |
| 3 | ES | API de Fandoblaje Wiki: Ángel Lugo, Rebeca Aponte, Carmen Lugo (missingtitle), Angel Balam (missingtitle), Arlet Matute (missingtitle), Jaime De Abreu (missingtitle) |
| 4 | ES | API de Doblaje Wiki: Carmen Lugo (ficha propia), Angel Balam (ficha propia) |
| 5 | ES | WebSearch: «ANMTV Rick and Morty doblaje latino temporada 9 elenco voces» → artículo de ANMTV sobre «Rick y Morty: El anime» |
| 6 | ES | Descarga y lectura de `https://www.anmtvla.com/2024/07/rick-y-morty-el-anime-max-revela.html` con curl + limpieza de HTML |
| 7 | ES | WebSearch: «"Arlet Matute" Beth Smith Rick y Morty doblaje» → World Dubbing News en X |
| 8 | ES | WebSearch: «"Jaime de Abreu" "Pantalones de Popó" OR "Poopybutthole" doblaje» → sin segunda fuente |
| 9 | EN | API de Fandom (rickandmorty.fandom.com), wikitext completo de Rick Sanchez, Morty Smith, Summer Smith, Mr. Meeseeks (secciones Trivia, Relationships) |
| 10 | EN | WebSearch: «"Rick and Morty" character guide birthday height favorite food databook» |
| 11 | EN | WebSearch: «Rick and Morty Emmy Awards won Outstanding Animated Program list» |
| 12 | EN | WebSearch: «Rick and Morty Rotten Tomatoes score most streamed Adult Swim ratings record» |
| 13 | EN | WebSearch: «"which Rick and Morty character do you relate to" reddit identify» |
| 14 | EN | API de Arctic Shift: `posts/search?subreddit=rickandmorty&title=identify` → hilo de 833 votos |
| 15 | EN | API de Arctic Shift: `comments/search?link_id=1r2zhxh` → citas de fans sobre identificación |
| 16 | EN | API de Arctic Shift: `posts/search?subreddit=rickandmorty&title=saddest` → 8 hilos con votos |
| 17 | EN | API de Arctic Shift: `comments/search?link_id=1mde14b` → citas sobre Planetina y el spaghetti |
| 18 | EN | WebSearch: «Rick and Morty Planetina episode which season "environmental superhero"» |
| 19 | EN | WebSearch: «Rick and Morty season 7 episode 4 spaghetti people suicide sad ending» |
| 20 | EN | WebSearch: «"A Rickconvenient Mort" Planetina ending song heartbreak Morty» → Kishi Bashi, vídeo musical oficial |
| 21 | ES | WebSearch: «Rick y Morty cover opening español latino YouTube parodia meme hispano» |
| 22 | — | `yt-dlp --skip-download --print` sobre 5 vídeos de fandub (3 con datos, 2 sin respuesta a tiempo) |
| 23 | — | Intento fallido de `arctic-shift posts/search?...&q=cried` (parámetro equivocado, corregido a `title=`) |

**Terminado** por esta tanda: los 7 puntos (7, 8, 12, 13, 20, 21, 22) tienen
contenido obligatorio con fuente. Lo que queda son extras anotados en «No
encontré» (segunda fuente de Mr. Poopybutthole, vistas de 2 fandubs, databook
de altura/cumpleaños que no existe para el elenco principal, fotogramas de
alegría/tristeza/vergüenza para completar el punto 13).
