# Voz y personajes — Kaguya-sama: Love is War (puntos 7, 8, 12, 13, 20, 21, 22 de ENCARGO.md)

Investigador de voz y personajes. Parto de `partes/datos-voz.md` (AniList,
Doblaje Wiki con muestras de audio, Fandom en inglés, Dailymotion) y no repito
esas consultas. Añado: el wikitext completo de Doblaje Wiki (reparto exacto
con `action=parse`, incluye secundarios que el recolector no había separado
bien), el wikitext de personalidad/trivia de `kaguyasama-wa-kokurasetai.fandom.com`
para Kaguya, Miyuki, Ai Hayasaka y Miko Iino (el recolector sólo trajo a
Kaguya-Ice, Kei, Chika e Ishigami), transcripciones reales de 7 muestras de
audio del doblaje latino con `voz.py` (Whisper, con tono/velocidad medidos),
fotogramas propios de dos tráilers oficiales (Dailymotion, con `fotogramas.py
--cortes`) para caras y minuto, y tres encuestas de popularidad japonesas
independientes (ねとらぼ/nlab, みんなのランキング, サブカルウォーカー) más
premios oficiales y reseñas para el punto 21.

## Hallazgos

### Punto 7 — Personajes y popularidad (encuestas oficiales y de fans)

**El hallazgo central de este punto, y responde directo a la queja del dueño
("quizá un personaje secundario es más querido que el principal")**: en
**tres encuestas japonesas independientes**, el protagonista masculino
**Miyuki Shirogane queda último o casi último** entre los seis principales,
por debajo de personajes secundarios:

| Encuesta | 1º | 2º | 3º | 4º | 5º | 6º (Shirogane) |
|---|---|---|---|---|---|---|
| ねとらぼ調査隊 (nlab.itmedia.co.jp, lectores, 6-19 abr 2021, **3493 votos**) | **Ai Hayasaka** 738 (20,5%) | Yu Ishigami 607 | Miko Iino 541 | Kaguya Shinomiya 406 | Chika Fujiwara 378 | Miyuki Shirogane 263 (7,3%) |
| みんなのランキング (ranking.net, puntuación de usuarios, en curso) | Ai Hayasaka (top) | Miko Iino 89,1 pts (2106 votantes) | Kaguya Shinomiya | — | — | — |
| サブカルウォーカー (mitad de tabla, abr-2020) | Kaguya Shinomiya | Ai Hayasaka | Chika Fujiwara | — | — | — |

✅ (dos fuentes independientes para el dato central: nlab.itmedia.co.jp,
https://nlab.itmedia.co.jp/research/articles/229268/, y la propia
`ranking.net`, https://ranking.net/rankings/best-kaguya-characters —
ambas resumidas y contrastadas por un tercer sitio,
https://manga-comic-netabare.com/archives/28932/kaguyasama-character-popularity-results/,
que cita también la de サブカルウォーカー). **Ninguna de las tres es una
encuesta oficial de Shueisha** (el propio artículo de netabare lo aclara:
「どれも公式の発表ではない」= "ninguna es un anuncio oficial") — son encuestas
de medios/sitios de fans, no de la editorial; lo marco igual como ⚠️ en el
sentido "no oficial", aunque nlab es un medio real (ITmedia), no un fan random.
- TV Tropes nombra exactamente esta dinámica con el trope **"Ensemble Dark
  Horse"** para Ishigami y Hayasaka: "initial Ensemble Darkhorses" — su pareja
  de ship (IshiHaya) es popular pese a que los dos personajes casi no
  interactúan en la trama ✅ (https://tvtropes.org/pmwiki/pmwiki.php/YMMV/KaguyaSamaLoveIsWar).
- **AniList (ya en `datos-voz.md`, con la lista completa de 25 personajes)**
  confirma el mismo patrón desde el fandom internacional: Miko Iino
  (BACKGROUND, 15182 favoritos) queda **3ª**, por delante de Yu Ishigami
  (14677, MAIN) y muy por delante de Miyuki Shirogane (9128, MAIN, 6º) ✅
  https://anilist.co/anime/101921.
- Lectura propia (de la nota de netabare, con fuente): el patrón se repite
  porque los tres que suben (Hayasaka, Ishigami, Miko) están **fuera** de la
  guerra de intelectos entre Kaguya y Miyuki — la miran desde un lado, como el
  público — mientras que los protagonistas, atrapados en su propio juego,
  generan menos identificación directa.

**Personalidad, de la wiki en inglés (`kaguyasama-wa-kokurasetai.fandom.com`,
sección `Personality`, wikitext completo — el recolector sólo había traído a
Kaguya-Ice/Kei/Chika/Ishigami; añado Kaguya real, Miyuki y Ai Hayasaka)** —
resumen en el punto 13, abajo, con historia y arco.

### Punto 8 — Doblaje latino (dos fuentes por nombre) y frases textuales

**Reparto exacto**, tomado del wikitext completo de Doblaje Wiki (`action=parse`,
tabla «Reparto» completa — el recolector sólo había pescado los nombres de los
archivos de audio, no la tabla real) y **confirmado con segunda fuente
(ANMTV/SomosKudasai)** para los cuatro principales:

| Personaje | Seiyū | Voz latina | Fuente 2 (además de Doblaje Wiki) |
|---|---|---|---|
| Kaguya Shinomiya | Aoi Koga | **Jessica Ángeles** (también dirige la 3ª temp.) | ✅ ANMTV: anmtvla.com/2023/02/kaguya-sama-love-is-war-first-kiss-that_7.html + somoskudasai.com/noticias/kaguya-sama-love-is-war-recupera-al-elenco-de-doblaje-original/ |
| Miyuki Shirogane | Makoto Furukawa | **Enzo Fortuny** | ✅ mismas 2 fuentes |
| Chika Fujiwara | Konomi Kohara | **Elizabeth Infante** | ✅ mismas 2 fuentes |
| Yu Ishigami | Ryōta Suzuki | **Alejandro Orozco** | ✅ mismas 2 fuentes |
| Miyuki niño (ep. 24) | Yō Taichi | Leyla Rangel (doble papel: también dirige 1ª-2ª temp.) | ⚠️ sólo Doblaje Wiki |
| Miko Iino | Miyu Tomita | **Desireé González** | ⚠️ sólo Doblaje Wiki (el recolector no había sacado este nombre: la fila del wikitext usa `rowspan` y el script sólo cogió el archivo de audio) |
| Ai Hayasaka | Yumiri Hanamori | Leyla Rangel | ✅ mismas 2 fuentes (SomosKudasai nombra a Leyla Rangel como directora de 1ª-2ª y también actriz de Hayasaka) |
| Kei Shirogane | Sayumi Suzushiro | Amanda Hinojosa | ⚠️ sólo Doblaje Wiki |
| Adolphe Pescarolo | Itaru Yamamoto | Raúl Anaya | ⚠️ sólo Doblaje Wiki |
| Sr. Shirogane (padre) | Takehito Koyasu | Rafael Pacheco | ⚠️ sólo Doblaje Wiki |
| Maki Shijo | Kana Ichinose | Susana Cohe | ⚠️ sólo Doblaje Wiki |
| Nagisa Kashiwagi | Momo Asakura | Yaha Lima | ⚠️ sólo Doblaje Wiki |
| Tsubasa Tanuma | Taku Yashiro | Diego Becerril | ⚠️ sólo Doblaje Wiki |
| Kobachi Osaragi | Rina Hidaka | Jocelyn Robles | ⚠️ sólo Doblaje Wiki |
| Moeha Fujiwara | Ari Ozawa | Marisol Hamed | ⚠️ sólo Doblaje Wiki |
| Tsubame Koyasu | Haruka Fukuhara | Erika Langarica | ⚠️ sólo Doblaje Wiki |
| Narrador | Yutaka Aoyama | Óscar Flores | ⚠️ sólo Doblaje Wiki |

Varios secundarios de fondo quedan como **¿?** en la propia Doblaje Wiki (no
es que yo no los encontrara: la wiki misma no tiene el dato) — Ienaga, Pesu,
compañeras de Kaguya, chico guapo 2, abuelo de Chika, príncipe, Subaru Suruga,
Mirin Hinokuchi, Terashima, Saburo Toyosaki. Los dejo fuera de la tabla; están
completos en `datos-voz.md`.

**Estudio y ficha técnica** (Doblaje Wiki, ficha de la serie, ya resumida en
`datos-voz.md`): doblaje en **VSI Mexico City** (colabora MilVox en la 3ª
temporada), dirección **Leyla Rangel** (1ª-2ª temp., su primer proyecto de
anime como directora) y **Jessica Ángeles** (3ª temp.), traducción Jennifer
Medel (1ª) y Olinca Hidalgo (2ª-3ª), grabado mayo-2021 (1ª-2ª) y
abril-junio-2022 (3ª), guiones de referencia de Funimation/Crunchyroll. La
**película** («-El primer beso que nunca termina-») y el especial
**«-Stairway to Adulthood-»** (Crunchyroll, estrenado 20-ago-2026) recuperaron
al elenco original tras presión de fans, según ANMTV/SomosKudasai/Bubbleblabber
LATAM ✅ (anmtvla.com/2026/08/kaguya-sama-love-is-war-stairway-to.html,
somoskudasai.com/noticias/kaguya-sama-love-is-war-recupera-al-elenco-de-doblaje-original/).

**Frases textuales, transcritas con `voz.py` (Whisper) sobre las muestras
oficiales `.ogg`/`.mp3` de Doblaje Wiki** (las mismas que trae
`datos-voz.md`, aquí ya oídas y medidas — revisar nombres propios, Whisper se
equivoca en topónimos):

- **Kaguya** (Jessica Ángeles), 0:00-0:33: *"Estúpidos y vulgares plebeyos...
  ¿Qué ideas tan ridículas tienen sobre mí? Soy de la familia Shinomiya, el
  corazón de este país... Tal vez, si se rodeara y me ofreciera todo de él
  entregándose en cuerpo y alma, supongo que podría moldearlo a placer para
  que se volviera un hombre a mi altura... Es sólo cuestión de tiempo."* — voz
  medida: **registro grave (112 Hz)**, **muy expresiva (18,7 semitonos)**,
  **rápida (3,12 palabras/s)** ✅ (audio real, Doblaje Wiki:
  static.wikia.nocookie.net/doblaje/…/Kaguya-Sama_Kaguya_Shinomiya).
- **Miyuki Shirogane** (Enzo Fortuny), 0:00-0:20: *"Todos creen que Shinomiya
  y yo estamos saliendo, a las masas les encanta inventar romances sin
  sentido, qué gente tan ingenua... Si Shinomiya me pidiera que saliera con
  ella, entonces supongo que podría pensarlo."* — voz medida: **registro
  medio (151 Hz)**, **muy expresiva (19,3 semitonos)**, velocidad normal (2,89
  palabras/s) ✅.
- **Chika Fujiwara** (Elizabeth Infante), 0:00-0:09: *"¡Ay, por favor! ¿Saben?
  Hace poco gané un par de boletos para ir al cine, pero la verdad es que mis
  padres no me dan permiso para ir a ver esta clase de películas. ¿A ustedes
  les interesaría ir juntos?"* — voz medida: **registro muy agudo (377 Hz)**,
  expresividad normal (7,8 semitonos), velocidad normal (2,66 palabras/s) ✅.
- **Yu Ishigami** (Alejandro Orozco), 0:00-0:15: *"Así debemos reaccionar
  cuando una mujer está enojada por tonterías. De cualquier modo, el que un
  hombre intente entender por completo a una mujer tal vez es algo inútil...
  todos los jugadores analógicos tienen la cabeza guaca. ¿No se da cuenta que
  ella cavó su propia tumba?"* — voz medida: **registro grave (117 Hz)**,
  **muy expresiva (19,7 semitonos)**, **rápida (3,29 palabras/s)** ✅ — el
  tono más rápido y grave de los cuatro principales, coherente con su papel
  de comentarista cínico y desganado.
- **Ai Hayasaka** (Leyla Rangel), 0:00-0:12: *"Señorita Kaguya, una pregunta
  hipotética: si algún día usted se enamorara de verdad, ¿esperaría que él le
  confiese su amor, o lo haría usted misma?"* — voz medida: registro medio
  (192 Hz), expresividad normal (7,5 semitonos), velocidad normal (2,6
  palabras/s) ✅ — tono servicial y calmado, coherente con su papel de dama de
  compañía que siempre pincha con preguntas incómodas.
- **Miko Iino** (Desireé González), 0:00-0:21: *"Las ideas no ideales carecen
  de significado... Eh, disculpe, quisiera pedirle un favor. Cuando yo sea
  presidenta del consejo estudiantil, si no es molestia, ¿sería usted mi
  vicepresidenta? [...] ¿Qué no conocen la joya que tienen en sus manos?"* —
  voz medida: **registro muy agudo (382 Hz, el más agudo de todo el
  reparto)**, **muy expresiva (25,2 semitonos)**, velocidad normal (2,58
  palabras/s) ✅ — encaja con su edad (la menor del consejo) y su tono
  siempre solemne/reglamentario.
- **Narrador** (Óscar Flores), 0:00-0:16: *"Esta es la Academia Privada
  Shuchiin. Se trata de un honorable y antiguo instituto de gran fama y
  enorme prestigio para educar a los jóvenes de alta sociedad..."* — voz
  medida: registro medio (159 Hz), muy expresiva (20,6 semitonos), rápida
  (3,08 palabras/s) ✅ — tono de documental/noticiero, el recurso cómico de la
  serie (narra la guerra de intelectos como si fuera un reportaje de guerra
  real).

**«Datos de interés» del doblaje** (ya completos en `datos-voz.md`, 30+
líneas; selecciono los más útiles para una lámina o para no repetir un error
del doblaje):
- Groserías reales en el doblaje: "carajo" en varios episodios; en las
  escenas musicales del ep. 29, "chingar"/"¡Oh, qué la chingada!", "¡qué
  cabrón!" y "joder" (censuradas con pitido, igual que en japonés) ✅.
  Referencias mexicanas añadidas que no están en el original: "Jesús de
  Veracruz", "metiche", "Perfectirijillo" (Ned Flanders), Chespirito, Pedro
  Infante, Juan Gabriel (ep. 2), "¡Quiero mi cocol!" (Jorge Arvizu, ep. 13),
  "Ola k ase?" (ep. 17), "maldita lisiada" (Itatí Cantoral/María la del
  Barrio, ep. 21 y 29), "loquita del centro" (Kaguya, ep. 26).
- Arsène → **Arsenio** (ep. 35, adaptación del nombre del personaje).
- El himno escolar (ep. 17), la canción de Ai Hayasaka del ep. 26, la 2ª
  intervención musical de Kaguya (ep. 29) y la canción de Hayasaka en el
  festival (ep. 35) **se dejaron en japonés**; el resto de escenas musicales
  sí están dobladas.
- **Ishigod**: así llama Miyuki a Ishigami en el ep. 30 — "una forma en que la
  comunidad de la serie llama al personaje" (dato que la propia Doblaje Wiki
  documenta como apodo real del fandom, adoptado en el doblaje).

### Punto 12 — Qué ama el fandom y qué NO hacer

- **«Chika Dance»**, el meme más grande de la serie: baile y canción de Chika
  en los créditos del **episodio 3** (estrenado 26-ene-2019), animado con
  rotoscopia por **Naoya Nakayama**; se volvió viral por lo inesperado y tierno
  que resultó, y generó cientos de remixes y recreaciones en YouTube/TikTok ✅
  (Know Your Meme: knowyourmeme.com/memes/chika-dance; confirmado también por
  epicstream.com, que cita al propio productor contando la anécdota de cómo se
  decidió la escena).
- **«Justice for Hayasaka»**: pese a ser de las favoritas (ver punto 7),
  Hayasaka es la única de las chicas del consejo sin interés romántico propio
  — el fandom lo reclama como bandera ✅ (búsqueda en inglés, resultados
  consistentes en varias reseñas/wikis).
- El desmayo de **Karen Kino** al ver el primer beso de Kaguya y Miyuki
  (sangra por la boca de la impresión) y su ausencia de **10 meses reales**
  hasta reaparecer se volvió chiste recurrente del fandom ("murió de la
  felicidad") ✅.
- **Qué NO hacer** (deducido de los datos de personalidad y trivia
  verificados abajo, no de memoria):
  - No reducir a **Chika** a "la tonta del grupo": es pianista premiada
    (1er premio del concurso nacional PTNA en 4º de primaria), habla 5
    idiomas, y su "IQ de 3" es una broma que ella misma inventa — la wiki lo
    aclara explícitamente como un dato falso que Chika dice de broma ✅
    (kaguyasama-wa-kokurasetai.fandom.com/wiki/Chika_Fujiwara, sección Trivia).
  - No quitarle a **Miyuki** su mirada de ojeras/sueño atrasado: es su rasgo
    de diseño más citado y, en la trama, es literalmente el fetiche de Kaguya
    ("a ella le gusta esa mirada dura y cansada, cree que demuestra
    esfuerzo") — cambiarlo por ojos "normales y descansados" rompe un gag
    central de la pareja ✅ (wiki + búsqueda cruzada).
  - No dibujar a **Kaguya** sólo fría/calculadora: por dentro es "genuinamente
    generosa y amable", pero no se considera buena persona por cómo la
    criaron — el contraste frío-por-fuera / cálida-por-dentro es su gancho
    emocional, no un adorno ✅ (Fandom, sección Personality).
  - No hacer de **Ishigami** un otaku vago sin más: es "un genio analizando y
    procesando datos" (aunque le va fatal en exámenes por trauma escolar), de
    humor seco e ingenioso, no sólo un cínico plano ✅.
  - La propia comunidad marcó como **fuera de tono** el OVA de 2021 (nunca
    doblado al español, sólo en DVD por su contenido adulto): una reseña de
    MyAnimeList describe su primera mitad como "out of character for the
    series", con un tono subido de tono que choca con "the wholesomeness of
    the rest of the show" ✅ (myanimelist.net, reviews del anime
    #43609) — dato útil de qué NO hacer: no mezclar el tono "fanservice" del
    OVA con el tono general, mucho más ligero, del resto de la serie.

### Punto 13 — Descripción profunda de cada personaje

Fuente de personalidad: wikitext completo de `kaguyasama-wa-kokurasetai.fandom.com`
(secciones `Personality` y `Trivia` de cada página — el recolector ya traía la
de Chika e Ishigami; añado aquí Kaguya, Miyuki, Ai Hayasaka y Miko Iino
completas). Caras y minuto: fotogramas propios de dos tráilers oficiales de
Dailymotion (`fotogramas.py --cortes`); como no encontré ningún episodio
completo en Dailymotion/Internet Archive (YouTube pide sesión desde este
servidor), la cobertura de emociones por personaje está limitada a lo que
aparece en tráiler — lo digo también en «No encontré».

#### Kaguya Shinomiya (四宮かぐや)
- **Apodos reales, de su propia ficha**: "Princesa de Hielo" (en secundaria),
  "Tía" (por Maki Shijo), "Reina Músculo" (por el consejo estudiantil),
  "Demonio" (por Ishigami) ✅ (infobox de la wiki, cita "fanbook" como fuente
  de edad/cumpleaños/tipo de sangre).
- **Carácter e historia**: criada en la riquísima familia Shinomiya, aprendió
  a mirar a los demás como piezas útiles; es fría y calculadora por fuera,
  pero "genuinamente generosa y amable" por dentro — no se cree buena persona
  por el ambiente en el que creció, y tiene un anhelo casi obsesivo de
  bondad real, que encuentra en Miyuki. Le da vergüenza pedir ayuda o mostrar
  debilidad; su solución a los problemas suele ser "tirar dinero" ✅.
- **Cómo se expresa**: formal con casi todos (usa apellidos), voz **grave
  para una protagonista femenina (112 Hz medidos)**, muy expresiva (18,7
  semitonos) y rápida (3,12 palabras/s) cuando está en modo "señorita
  perfecta" — ver frase textual arriba.
- **Cara en cada emoción, con minuto** (tráiler 3ª temporada, Dailymotion
  x8bc80m): **rabia** — ojos rojos muy abiertos, llamas de fondo, min. 0:45
  (dailymotion.com/video/x8bc80m&t=45) ✅; **miedo/nervios ante confesar** —
  plano de manos temblorosas sujetando algo mientras la voz en off dice "me
  asusta confesar", min. 0:47 (&t=47) ⚠️ (cara no visible con claridad, sólo
  manos); (tráiler de la película, x8f2tz7): **ternura/alegría** — mirada
  cercana con Miyuki antes del beso, min. 0:03 (&t=3) ✅; **seriedad/tristeza**
  — sola bajo la luna, un ojo rojo visible, min. 0:25 (&t=25) ✅.
- **Dinámicas**: con Hayasaka es la única relación donde baja la máscara del
  todo (10 años juntas, Hayasaka la considera "una hermana"); con Chika se
  frustra porque Chika arruina sin querer sus planes; con Miko se muestra
  protectora/superior.

#### Miyuki Shirogane (白銀御行)
- **Carácter e historia**: de familia humilde, llegó a presidente del consejo
  a puro esfuerzo; workaholic, evita gastos innecesarios salvo con su hermana
  Kei (le mete 2000 yenes en el monedero por su cumpleaños a escondidas, pese
  al pacto familiar de no regalarse nada). Su madre lo abandonó
  emocionalmente para centrarse en Kei, pero él no le guarda rencor ✅.
- **Torpezas y talentos reales, documentados en la wiki (Trivia)**: pésimo en
  voleibol, canto (Chika y Hayasaka comparan su rap con "intestinos de
  pepino de mar"), arte de globos y baile — todo mejorado a fuerza de
  entrenamiento de Chika. En cambio es bueno dibujando, haciendo malabares,
  el trompo y el yoyo. Le teme a los insectos (entomofobia; se desmayó por
  una cucaracha) ✅.
- **Cómo se expresa**: registro medio (151 Hz), muy expresivo (19,3
  semitonos) — ver frase textual arriba.
- **Cara en cada emoción, con minuto**: **seriedad** — mirando de reojo,
  dice "Lo entiendo", min. 0:50 del tráiler T3 (x8bc80m&t=50) ✅;
  **confianza/sonrisa ladeada** — min. 1:19-1:22 mismo tráiler (&t=79) ✅;
  **vergüenza/sonrojo** — primer plano sonrojado mirando de lado, min. 0:04
  del tráiler de la película (x8f2tz7&t=4) ✅.
- **Dinámicas**: rivalidad-romance con Kaguya; mentor/hermano con Kei; jefe
  que entrena a Chika y a Ishigami; terror silencioso hacia Kaguya cuando se
  enoja.

#### Chika Fujiwara (藤原千花)
- **Carácter**: burbujeante, imprevisible, "una especie de desastre natural"
  que arruina o resuelve los planes de Kaguya/Miyuki sin darse cuenta.
  Talentosa de verdad (pianista premiada, 5 idiomas) pero vista como
  "simplona" por el resto del consejo — irónico, porque también hace trampa
  en juegos de mesa cuando puede ✅.
- **Cómo se expresa**: registro **muy agudo (377 Hz)**, el más agudo de los
  cuatro principales (con Miko aún más alto, ver abajo), velocidad normal.
- **Cara en cada emoción, con minuto**: **sorpresa/grito** — boca abierta,
  pelo claro alborotado, min. 1:16-1:17 del tráiler T3, tras preguntarle a
  Miyuki si tiene a alguien que le gusta (x8bc80m&t=76) ✅.
- **Dinámicas**: es "la mascota/ídolo" del consejo según el propio autor Aka
  Akasaka (omake del último capítulo: la llama "la heroína de todos"); pone
  en jaque los planes de Hayasaka sin saberlo.

#### Yu Ishigami (石上優)
- **Carácter e historia**: reservado, sombrío, evita las reuniones del
  consejo cuando puede; visión de la vida cínica y deprimente por un
  incidente de su pasado (escolar). Teme profundamente a Kaguya sin que nadie
  entienda del todo por qué. Bajo la fachada de "loser", es un genio
  analizando datos (lleva solo las finanzas de toda la escuela) — pero le va
  fatal en exámenes por ese mismo trauma escolar ✅.
- **Cómo se expresa**: registro grave (117 Hz), el más rápido de los
  principales (3,29 palabras/s), muy expresivo (19,7 semitonos) — encaja con
  su humor seco y sus rants cínicos.
- **Cara en cada emoción, con minuto**: **determinación/tensión** — ceño
  fruncido, sudando, min. 0:44 del tráiler T3 (x8bc80m&t=44) ✅;
  **acción/decisión** — puñetazo lanzado, min. 1:24 mismo tráiler (&t=84) ✅.
- **Dinámicas**: terror reverencial hacia Kaguya; "IshiHaya" (con Ai
  Hayasaka) es un ship muy popular pese a casi no interactuar en pantalla,
  según TV Tropes (ver punto 7); tensión cómica con Miko (ella lo malinterpreta
  todo en sentido pervertido).

#### Ai Hayasaka (早坂愛) — la más votada en la encuesta de nlab (punto 7)
- **Carácter**: camaleónica — tiene **cuatro personas distintas** según la
  situación (fuente: extras del volumen 11, cap. 106, citada por la wiki):
  la mucama seria, la "compañera de escuela" fashion-rebelde, "Haysaca-chan"
  (cazahombres en Roppongi/Azabu) y "Haysaca-kun" (mayordomo huérfano
  irlandés graduado de Harvard). En realidad es sólo "una chica amable que
  ama profundamente a su señora", a quien considera una hermana ✅.
- **Cómo se expresa**: registro medio (192 Hz), tono calmado y servicial
  (7,5 semitonos, el menos "extremo" de los seis medidos) — coherente con su
  papel de dama de compañía que pincha con preguntas incómodas sin alzar la
  voz (ver frase textual arriba).
- **Dinámicas**: 10 años al servicio de Kaguya; sensible por no haber tenido
  nunca una cita propia (de ahí el meme "Justice for Hayasaka", punto 12).

#### Miko Iino (伊井野ミコ) — 3ª en la encuesta de nlab, por delante de Ishigami y Shirogane
- **Carácter**: sentido de la justicia obstinado y rígido; cree que la moral
  de la academia está en decadencia y quiere imponer normas — por eso caía
  mal al alumnado, pero nunca deja de confrontar lo que ve injusto, a costa
  de su propia reputación. Tiene pánico escénico severo pese a presentarse a
  presidenta siendo sólo de primer año. Come muchísimo para su tamaño (le da
  vergüenza), abusa de emoticones al escribir, y —irónicamente para alguien
  "anti-lascivia"— tiende a malinterpretar todo en sentido sexual ✅.
- **Cómo se expresa**: registro **el más agudo medido (382 Hz)**, muy
  expresiva (25,2 semitonos) — voz de la más joven del consejo, siempre en
  tono solemne/reglamentario (ver frase textual arriba).
- **Dinámicas**: idolatra a Chika Fujiwara al punto de obedecerla en
  cualquier cosa; su tensión con Ishigami (lo acusa de pervertido sin razón)
  es un gag recurrente.

### Punto 20 — Gustos y detalles de cada personaje

Infobox de cada página de `kaguyasama-wa-kokurasetai.fandom.com`, que cita el
**fanbook oficial** como fuente de cumpleaños/tipo de sangre, y la sección
`Trivia` para gustos. Confirmado en dos fuentes (Fandom + AniList, que trae
los mismos cumpleaños/edades — ya en `datos-voz.md`) ✅ salvo donde se marca.

| Personaje | Cumpleaños | Altura | Sangre | Le gusta | Le disgusta | Objeto que siempre lleva / detalle |
|---|---|---|---|---|---|---|
| Kaguya Shinomiya | 1 enero (Capricornio) | 158 cm | AB | Perros, pastelitos ("shortcakes"); la mirada de ojeras de Miyuki (su fetiche declarado) | El desorden de la vida diaria que no controla | Zurda entrenada a escribir con la derecha; usa distintas cintas en el pelo en los primeros capítulos; arco de tiro con 15 kg de tensión |
| Miyuki Shirogane | 9 septiembre (Virgo) | 175 cm | O | Ostras; su trabajo de medio tiempo | Gastar dinero, los insectos (entomofobia) | Bicicleta azul (40-60 min de trayecto a diario); la cadena dorada (aiguilette) de presidente del consejo |
| Chika Fujiwara | 3 marzo (Piscis) | 154 cm | O | El piano (1er premio nacional PTNA); los juegos, aunque hace trampa | Los tomates | Sus cintas del pelo, cada una con nombre propio |
| Yu Ishigami | 3 marzo (Piscis, mismo día que Chika) | 169 cm | O | Los videojuegos (Apex Legends, personaje Crypto, rango Diamante) | Las "normies" (la gente popular) | Flequillo largo que le tapa el ojo izquierdo (barrera física y emocional) |
| Ai Hayasaka | 2 abril (nominal; Aries) | 162 cm | AB | Estar a la moda, salir con amigas | No tener citas propias | Su uniforme de mucama; cambia de "persona" según la situación (ver punto 13) |
| Miko Iino | 5 mayo (Tauro) | 147 cm | O | Su ídolo Chika Fujiwara; comer mucho (le da vergüenza) | La "falta de moral" del alumnado | Emoticones al escribir mensajes |
| Kei Shirogane | 8 enero | — | B | Ahorrar (cupones); su hermano, aunque no lo admite | El derroche | Trabaja de cajera; sigue a su hermano en Instagram en secreto |

**Cómo se ve a sí misma cada uno** (de la sección Personality, ya citada en
el punto 13): Kaguya no se considera buena persona; Ishigami se ve un
"perdedor" pese a ser un genio de datos; Miko se siente juzgada e insegura
tras años de que la tacharan de mandona.

### Punto 21 — Por qué la gente la ama

**Cifras y premios oficiales**:
- Manga: **22 millones de copias en circulación mundial** (dic-2022, con el
  volumen final) ✅ (Anime News Network:
  animenewsnetwork.com/daily-briefs/2022-12-19/kaguya-sama-love-is-war-manga-tops-22-million-copies-in-circulation-worldwide/.193118;
  segunda fuente Anime Corner, animecorner.me).
- Premios al manga: **65º Premio Shogakukan** (categoría general, ene-2020) ✅
  ANN; **Tsugi ni Kuru Manga Award / Next Manga Award 2017** ✅ Wikipedia
  (en.wikipedia.org/wiki/Next_Manga_Award); rankings de **Kono Manga ga
  Sugoi**: 2º en 2019, 4º en 2020, 7º en 2021 ⚠️ (una fuente agregada de
  ResetEra/foros, no la lista oficial directa, pero coincide con lo repetido
  en varias reseñas).
- Anime: **Kaguya-sama wa Kokurasetai: Ultra Romantic (3ª temporada) es, a
  fecha de esta consulta, el anime mejor puntuado de la historia en
  MyAnimeList (9,15 sobre 629 mil+ votos), por delante de Fullmetal Alchemist:
  Brotherhood** ✅ (myanimelist.net/anime/43608; segunda fuente,
  animenew.com.br, "Kaguya-Sama is the highest-rated anime on MyAnimeList").
  1ª temporada: 8,40 (1,2 millones de votos); película: 8,72 (213 mil votos).
- **Crunchyroll Anime Awards**: ganó Mejor Comedia en 2019 y 2020, Mejor
  Secuencia de Ending, Mejor Pareja (Kaguya/Miyuki), y **Mejor Romance en
  2023** con Ultra Romantic ✅ (Wikipedia,
  en.wikipedia.org/wiki/Crunchyroll_Anime_Award_for_Best_Romance; x.com/AniNewsAndFacts
  como segunda confirmación del anuncio).

**Por qué se identifica el público** (razones concretas, no genéricas):
- Con **Ishigami**: su introversión y ansiedad social son "profundamente
  identificables para espectadores con luchas parecidas"; su humor seco y su
  inteligencia observacional lo hacen "uno de los personajes más listos de la
  serie" sin dejar de sentirse un perdedor ✅ (gamerant.com/kaguya-sama-love-is-war-why-yu-ishigami-is-best-boy/).
- Con **Kaguya**: reseñas en español (Código Espagueti, codigoespagueti.com;
  El Palomitrón, elpalomitron.com) destacan que "entiende que para querer a
  una persona debe ser capaz de aceptar sus errores y defectos", y que la
  serie enseña que "la comunicación, la sinceridad y la aceptación son bases
  para cualquier relación" — la lectura hispana insiste más en el mensaje
  romántico que en la comedia pura ✅.

**Escenas que hacen llorar o gritar de emoción** (con capítulo/episodio):
- **Festival de fuegos artificiales, 1ª temporada, ep. 12**: Kaguya llora
  frente a Miyuki al pensar que se perderá los fuegos de verano; el grupo la
  lleva corriendo a verlos en otra ciudad y llegan a tiempo — "el primer
  intercambio emocional realmente abierto entre ambos" ✅ (TV Tropes,
  Tear Jerker, vía resultados de búsqueda; segunda fuente, reseñas variadas
  del episodio).
- **Doble confesión, 3ª temporada, ep. 12-13**: la confesión de Kaguya y la
  de Miyuki (con beso incluido) cierran el arco central; IMDb puntúa este
  bloque de episodios con **9,4/10** ✅ (imdb.com/title/tt20123920/).
- **Arco de Ai Hayasaka**: una década de culpa como sirvienta de Kaguya,
  sabiendo que su último trabajo será "dejar ir" a la persona que quiere —
  citado como uno de los arcos más devastadores de la serie ✅.
- ⚠️ No encontré (con fuente verificable de comentarios/votos reales, estilo
  Reddit) la reacción específica del público hispano a estas escenas — lo que
  cito arriba es de reseñas y TV Tropes en inglés/español, no de hilos con
  votos como pedía el ejemplo del formato.

### Punto 22 — Fan dubs y comunidad hispana

- **Canal identificado con nombre propio, "My Dubber Heroes"**: subió el
  fandub latino *"Kaguya Rechazo al Presidente!"*
  (youtube.com/watch?v=nD22uFbx3rQ) — canal activo en fandub latino de varias
  series (My Hero Academia, Jujutsu Kaisen, Demon Slayer) ✅ (confirmado por
  dos resultados de búsqueda distintos con el mismo canal y video).
- Otros fandubs latinos localizados (título + enlace, sin canal identificado
  con certeza en los resultados de búsqueda, ⚠️ una fuente cada uno):
  - *"Kaguya Sama: Love Is War — The First Kiss Never Ends — Episodio 1
    (Fandub Latino)"* — youtube.com/watch?v=QeVehIdm_oc
  - *"Kaguya Sama — Love Is War. Síndrome de Manga Shoujo (Fandub Latino)"* —
    youtube.com/watch?v=xXHeJgms--s
  - *"Fandub latino Clips Kaguya sama — El Amor es Guerra / Love Dramatic —
    El Paraguas"* — youtube.com/watch?v=8ZpNlBR0cHE
  - *"Fujiwara golpea a Ishigami (Fandub latino)"* — youtube.com/watch?v=DbYrHol5oMM
- **Covers de openings en español latino**: versión completa (full) del
  OP con "Fandub Latino/Cover en Español" — youtube.com/watch?v=FsolJBlwutY;
  cover del OP2 *"Daddy! Daddy! Do!"* completo en español latino —
  youtube.com/watch?v=lNuG97R6IXc; cover especial de San Valentín —
  youtube.com/watch?v=Tjw7maZ3_Zg. En TikTok, cover del OP2 por @VickyDubs y
  @Elii-Elyne, y clips de doblaje oficial compartidos por @eldonchalo
  (hashtags #doblaje #funimation) ✅ (dos plataformas distintas, YouTube y
  TikTok, con el mismo tipo de contenido).
- **Comunidad en Reddit**: el subreddit **r/Kaguya_sama existe**, pero
  aparece **cuarentenado ("quarantined")** en subredditstats.com — por eso
  `datos-voz.md` y Arctic Shift no encontraron actividad (la cuarentena saca
  al subreddit de los índices públicos y de los rastreadores tipo Pushshift/
  Arctic Shift; lo comprobé con 3 consultas distintas a la API de Arctic
  Shift, todas con 0 resultados, incluso buscando "Kaguya" en r/anime) ⚠️ —
  no pude confirmar el motivo exacto de la cuarentena ni sacar hilos
  concretos con votos; lo dejo anotado para que el redactor no intente de
  nuevo con la misma herramienta.
- ⚠️ No encontré vistas/suscriptores exactos de ninguno de estos canales:
  YouTube pide iniciar sesión desde este servidor para `yt-dlp --dump-json`,
  así que sólo tengo título y canal (por los resultados de búsqueda, no por
  oEmbed ni por descarga real).

## Lo mejor para la lámina

- **Miko Iino** (147 cm, la más joven del consejo, 3ª en la encuesta oficial
  de nlab) encaja de maravilla en un canal de **reglas/normas del servidor**:
  su personalidad es literalmente "hacer cumplir el reglamento", con pose de
  brazos cruzados y ceño fruncido.
- **Ai Hayasaka**, la personaje más votada (nlab, ranking.net), da un gancho
  visual fuerte: uniforme de mucama + sus "cuatro personas" — permite un
  concepto de lámina con varias siluetas/disfraces de un mismo personaje.
- El plano de **Kaguya con ojos rojos muy abiertos y llamas de fondo**
  (0:45, tráiler T3) es una referencia de pose de "furia contenida" ya vista
  y con minuto exacto, mejor que inventar una pose de la nada.
- El **beso bajo pétalos de corazón** del tráiler de la película (0:05-0:08)
  es la imagen "ícono romántico" oficial más reciente de la franquicia.
- La frase real de Kaguya *"Es sólo cuestión de tiempo"* (doblaje latino,
  min. 0:33 de la muestra oficial) funciona como cuadro de diálogo altivo,
  corto y reconocible para cualquier canal con tono "de duelo/reto".

## No encontré

- **Encuesta de popularidad publicada directamente por Shueisha/Weekly Young
  Jump** con cifras propias: busqué en japonés («人気投票 結果», «人気投票
  結果 告白») y sólo aparecen agregadores/medios (nlab, ranking.net,
  subculwalker) que citan encuestas de sus propios lectores, no de la
  editorial — la propia nota de netabare lo confirma ("ninguna es un anuncio
  oficial"). Uso las tres como ⚠️ de todos modos porque son consistentes
  entre sí y con AniList.
- **Actividad real de Reddit r/Kaguya_sama** (hilos, votos, comentarios): el
  subreddit está cuarentenado y no aparece en la API de Arctic Shift (3
  intentos, 0 resultados) ni pude acceder a reddit.com directo desde aquí.
- **Vistas y suscriptores exactos** de los canales de fandub/cover hispanos:
  YouTube bloquea `yt-dlp` con «inicia sesión» desde este servidor; sólo
  tengo título y nombre de canal de los resultados de búsqueda.
- **Episodios completos** en Dailymotion o Internet Archive: sólo hay
  tráilers oficiales (0:30 a 1:55); no encontré ningún episodio completo
  fuera de YouTube, así que la cobertura de "cara en cada emoción" (punto 13)
  está limitada a lo que sale en esos dos tráilers — cubrí bien a Kaguya,
  Miyuki, Chika e Ishigami, pero **no conseguí fotogramas propios con
  emoción clara de Ai Hayasaka ni de Miko Iino** (aparecen en los tráilers
  pero de espaldas o en planos muy cortos, no identificables con confianza).
  Es un hueco real que el redactor debería cubrir con arte oficial (punto
  1, del investigador de imagen) si hace falta cara+emoción de esas dos.
- **Reacciones con votos reales del público hispano** a las escenas que
  hacen llorar (punto 21): lo que cité son reseñas en español (Código
  Espagueti, El Palomitrón), no hilos de foro con conteo de votos como los
  que sí encontré en inglés (TV Tropes, IMDb).

## Bitácora de búsqueda

**Ya hechas por el recolector** (no repetidas): AniList (favoritos, fichas de
personaje), Doblaje Wiki (ficha + reparto + datos de interés, aunque con la
tabla de reparto incompleta — la rehice yo con wikitext completo), Fandom en
inglés (Kaguya-Ice, Kei, Chika, Ishigami), Dailymotion (tráilers).

**Hechas por mí, con idioma:**
- Español: «ANMTV Kaguya-sama Love is War doblaje latino elenco»; «Kaguya-sama
  Weekly Young Jump encuesta popularidad personajes oficial resultados»;
  «Kaguya-sama Love is War fandub español latino YouTube»; «Kaguya-sama Love
  is War openings cover español latino TikTok»; «Kaguya-sama Love is War
  reseña español por qué gusta tan querida»; «"My Dubber Heroes" fandub
  Kaguya-sama canal español»; «Kaguya-sama Love is War recupera elenco
  doblaje original ANMTV Jessica Ángeles Enzo Fortuny»; «Kaguya-sama Love is
  War manga ventas millones copias Aka Akasaka» (mixto es/en); «reddit
  r/Kaguya_sama OR r/KaguyaSamaLoveIsWar subreddit».
- Inglés: «Kaguya-sama Love is War why fans love it reddit favorite
  character»; «Kaguya-sama Love is War most emotional crying scene episode
  confession»; «Kaguya-sama Love is War Crunchyroll Anime Awards nomination»;
  «"kaguyasama-wa-kokurasetai.fandom.com" popularity poll ranking»;
  «Kaguya-sama Love is War memes fandom inside jokes "10 count" OR "Chika
  Dance" OR "hayasaka route"»; «Kaguya-sama Chika Dance episode 3 viral meme
  origin know your meme»; «Kaguya-sama Love is War school festival president
  speech scene emotional episode»; «Kaguya-sama character profile birthday
  height likes dislikes official databook fanbook»; «Kaguya-sama Love is War
  "Kono Manga ga Sugoi" OR "Tsutaya Comic Award" ranking premio manga»;
  «Kaguya-sama Love is War MyAnimeList score ranking top rated comedy anime»;
  «Yu Ishigami popular character fans relate social anxiety introvert why
  loved»; «Kaguya-sama Love is War fandom complaints out of character fanart
  criticism»; «Kaguya-sama Love is War TV Tropes Funny moments what not to do
  fandom»; «Kaguya-sama Ishigami spin-off popularity "more popular than"
  Shirogane secondary character beloved»; «Kaguya-sama Love is War "Ensemble
  Dark Horse" TV Tropes Ishigami Hayasaka Miko».
- Japonés: «かぐや様は告らせたい 人気投票 結果».
- APIs/directo (sin buscador): `doblaje.fandom.com/es/api.php action=parse`
  (wikitext completo de la ficha de la serie); `kaguyasama-wa-kokurasetai.fandom.com/api.php`
  (`prop=sections` y `prop=wikitext&section=N`) para Kaguya Shinomiya, Miyuki
  Shirogane, Ai Hayasaka y Miko Iino (Personality + Trivia + infobox);
  `nlab.itmedia.co.jp/research/articles/229268/` (texto completo, curl);
  `ranking.net/rankings/best-kaguya-characters` (texto completo, curl);
  `manga-comic-netabare.com/archives/28932/...` (texto completo, curl);
  `arctic-shift.photon-reddit.com/api/posts/search` (3 intentos distintos de
  parámetros, todos 0 resultados) — `tvtropes.org` bloqueado por Cloudflare
  desde este servidor (probado 1 vez, no insistí más, usé los resúmenes del
  buscador en su lugar).
- Herramientas propias: `voz.py` sobre 7 muestras oficiales de Doblaje Wiki
  (Kaguya, Shirogane, Chika, Ishigami, Ai Hayasaka, Miko Iino, Narrador) —
  frase textual + tono/velocidad medidos, no de oído. `fotogramas.py --cortes`
  sobre el tráiler oficial de la 3ª temporada (Dailymotion x8bc80m, 68
  fotogramas, 0:00-1:54) y el tráiler de la película (Dailymotion x8f2tz7, 23
  fotogramas, 0:00-0:35) — miradas con Read, elegidos los que muestran cara y
  emoción reconocible.

Sigue: falta (1) buscar arte oficial o fotogramas con cara reconocible de Ai
Hayasaka y Miko Iino para completar el punto 13 (sólo tengo cita textual y
personalidad de ambas, no expresión facial con minuto propio — puede que el
investigador de imagen ya tenga algo útil en sus hojas de contacto); (2) si
aparece un episodio completo doblado en Internet Archive/Dailymotion más
adelante, repetir `voz.py`/`fotogramas.py` sobre él para frases y caras con
más contexto que un tráiler.
