# Parte de VOZ Y PERSONAJES · Saint Seiya (Los Caballeros del Zodiaco)

Puntos de ENCARGO.md: 7 (popularidad), 8 (doblaje latino y frases textuales),
12 (fandom y qué no hacer), 13 (descripción profunda de cada personaje, con
cara en cada emoción), 20 (gustos y detalles), 21 (por qué la gente la ama y
escenas que hacen llorar) y 22 (fan dubs y comunidad hispana). Parte de
`partes/datos-voz.md` (AniList, Doblaje Wiki, Danbooru, Dailymotion, Reddit)
— esas consultas no se repiten aquí.

YouTube pidió iniciar sesión desde este servidor (bloqueo compartido de IP):
todo lo de vídeo se miró en **Dailymotion** e **Internet Archive** (con
`fotogramas.py`, reaprovechando también las hojas ya sacadas por el
investigador de vídeo en `/tmp/claude-0/trabajo/39-saint-seiya-video/`), y el
doblaje se oyó con **muestras de audio reales de Doblaje Wiki** (`.ogg`,
procesadas con `voz.py`, Whisper + medida de tono). Trabajo pesado en
`/tmp/claude-0/trabajo/39-saint-seiya-voz/`.

## Hallazgos

### Punto 7 — Popularidad (encuestas oficiales y de fans)

- **Animage 1986** (revista japonesa, encuesta de lectores): Saint Seiya quedó
  9º entre los mejores anime del año; en el ranking de personajes masculinos,
  **Shun 10º, Shiryu 11º, Hyoga 15º** — el único anime de ese año con tres
  personajes en el top 20 · https://en.wikipedia.org/wiki/Saint_Seiya_(TV_series) ·
  https://www.ssnextdimension.com/el-anime/saint-seiya-clasico/su-exito-en-japon/
  · ✅ (dos fuentes).
- Saint Seiya ganó el **Anime Grand Prix de Animage 1987** (mejor anime del
  año, voto de lectores); en 1988 quedó 4º de la historia, en 1989 y 1990, 3º
  · misma fuente (ssnextdimension.com, con cifras de Animage) · ⚠️ (una fuente
  agregadora; no vimos la revista original).
- En Japón, **Shiryu es el más popular de los 5 Santos de Bronce** en la
  encuesta de personajes principales (según Wikipedia, que cita Animage) ·
  https://en.wikipedia.org/wiki/Dragon_Shiry%C5%AB · ⚠️ (una fuente; no se
  encontró el año exacto de esa encuesta puntual).
- Encuesta de **Netorabo** (portal japonés), 6-19 marzo 2021, 18 690 votos de
  fans de Saint Seiya · mencionada en varias páginas de repaso · ⚠️ (no se
  encontró el resultado exacto —quién ganó— sólo la existencia y el número de
  votos).
- **AniList (favoritos de usuarios, medida global de fans)**, de
  `datos-voz.md`: Ikki 379, Shun 323, Seiya 319, Shiryu 317, Hyoga 245, Saori
  92 (de los 6 personajes del encargo) · https://anilist.co/anime/1254 · ✅
  (cifra propia de la web, verificable). Aquí **Ikki gana a Seiya**, el
  protagonista — coincide con el aviso del dueño de que «un secundario puede
  ser más querido».
- **Danbooru (dibujos de fans, cariño visual)**, de `datos-voz.md`: entre los
  6, el más dibujado es **Saori/Athena** (185 + 127 = 312 contando
  `kido_saori` y `athena_(saint_seiya)` por separado), luego Seiya (155),
  Shiryu (67); Hyoga, Shun e Ikki no entran en el top 20 de la serie ·
  https://danbooru.donmai.us/posts?tags=saint_seiya · ✅.
- Reddit r/SaintSeiya, hilo «Who is your favorite character and why?» (164
  votos, 42 comentarios, 2025) y «besides the Gold Saints?» (101 votos, 60
  comentarios) — de `datos-voz.md`, sin ganador único claro en los títulos (se
  necesitaría leer comentarios) · ⚠️.

### Punto 8 — Doblaje latino (dos fuentes por nombre) y frases textuales

Hay **tres doblajes latinos** distintos de Seiya y compañía (Doblaje Wiki, API
directa, `action=parse&prop=wikitext`, además de Fandom con la wiki en inglés
que reusa los mismos créditos para el Blu-ray/streaming — datos-voz.md ya trae
la ficha de la 2ª temporada del redoblaje 2022-24):

**1. Serie clásica (1986, doblada en México 1992-95, estudio Producciones
Salgado, dirigida por el propio Jesús Barrero)** ·
https://doblaje.fandom.com/es/wiki/Los_Caballeros_del_Zodiaco ·
✅ (Doblaje Wiki + AniList trae los mismos 6 nombres en su columna «Spanish»):
- Seiya de Pegaso → **Jesús Barrero** (las 3 temporadas; también dirigió el
  doblaje) · ✅.
- Shiryu de Dragón → **Ricardo Mendoza** (voz principal 1ª-3ª; Roberto
  Mendiola lo dobló en el ep. 2 y Daniel Abundis en 7-8, antes de fijarse el
  reparto) · ✅.
- Hyoga de Cisne → **René García** (las 3 temporadas) · ✅.
- Shun de Andrómeda → **José Gilberto Vilchis** (1ª-3ª; Javier Rivero en
  64-65) · ✅.
- Ikki de Fénix → **Marcos Patiño** (1ª-3ª) · ✅.
- Saori Kido/Athena → **Cristina Camargo** (1ª, eps. 1-26), reemplazada por
  **María Fernanda Morales** (resto de 1ª y 2ª) y por **Haydeé Unda** (3ª) ·
  Doblaje Wiki cuenta el cambio: Camargo dejó el personaje y Morales, que ya
  hacía a «Miho» y «Akira», tampoco siguió con esos dos · ✅.

**2. Netflix «Knights of the Zodiac» 2019 (CG, 1ª temporada, 12 eps., doblado
del inglés, estudio Labo, dirección Arturo Castañeda)** ·
https://doblaje.fandom.com/es/wiki/SAINT_SEIYA%3A_Los_Caballeros_del_Zodiaco ·
✅ (ficha propia + muestras de audio oficiales `.ogg` de la misma wiki, oídas
con `voz.py`):
- Seiya → **Darío Yazbek Bernal** (actor de cine mexicano, «startalent»; según
  datos-voz.md este mismo estudio hizo pruebas para la voz de Seiya de la
  temporada 2 antes de que Netflix decidiera usar un startalent en la 1ª) ·
  ✅.
- Shiryu → **Ricardo Mendoza** (se mantiene desde la serie clásica) · ✅.
- Hyoga → **Alfonso Herrera** (actor/cantante, ex-RBD) · ✅.
- «Shaun» de Andrómeda → **Isabel Martiñón** — **en esta versión (guion
  original en inglés) el personaje de Shun es una MUJER**, «Shaun»: se oye en
  la propia muestra de audio («no estoy segura», «siempre he sido reacia»,
  «mi hermano mayor, Iggy, me enseñó a pelear») y lo confirma la ficha de
  Doblaje Wiki (`Shaun de Andrómeda`, actriz mujer) · ✅ (audio + ficha). Dato
  importante para no dibujarla/dibujarlo mal: en el resto de versiones
  (clásica y redoblaje 2022) Shun es varón.
- Ikki → **Marcos Patiño** (se mantiene desde la serie clásica) · ✅.
- Saori/Athena → **María Fernanda Morales** (se mantiene) · ✅.

**3. Netflix «Knights of the Zodiac - Battle for Sanctuary -» 2022-24 (2ª
temporada, doblado del japonés, estudio Audiomaster Candiani, dirección
Octavio Campos)** — ficha completa ya en `datos-voz.md` (no se repite aquí);
resumen: **Seiya recastado a Carlo Vázquez** (Yazbek no continuó), **Shiryu a
Óscar López** (Mendoza no volvió «por diferencias económicas», grabó el ep.1
y lo cambiaron), **Hyoga se mantiene con René García** (repite de la serie
clásica pese al cambio de estudio), **Ikki y Shun con actores nuevos**
(Máscara de Muerte y Kiki recastados por bajas del actor original) · ✅ (ya
verificado en datos-voz.md con Doblaje Wiki).

**Frases textuales (Netflix 2019, muestras oficiales `.ogg` de Doblaje Wiki,
transcritas con Whisper vía `voz.py`; nombres propios revisados a oído)**:
- Seiya (Darío Yazbek Bernal): *«Hagan lo que quieran. Yo me quedaré. Voy a
  luchar.» «Cuando era niño, Grada atacó a mi hermana y trató de matarme. No
  pude detenerlo entonces, pero ahora sí puedo.» «¡Meteoro!»* (grito de
  ataque, Whisper lo oyó como «mete oro») · voz: registro grave (137 Hz), MUY
  expresiva (23.7 semitonos), velocidad normal (2.65 palabras/s) ·
  https://static.wikia.nocookie.net/doblaje/images/7/7b/DarioYazbekSeiya01.ogg
  · ✅ (oído entero).
- Shiryu (Ricardo Mendoza): *«Mi maestro Dohko sugirió que participara en el
  torneo... lo respeto mucho y algún día quiero ser un gran hombre como él.»
  «¡Ya vieron el escudo indestructible! ¡Ahora contemplen! ¡La furia del
  dragón!»* · voz: grave (106 Hz), muy expresiva (20.9 semitonos), **la más
  rápida de los 4** (3.39 palabras/s) ·
  https://static.wikia.nocookie.net/doblaje/images/2/2f/ShiryuSaintSeiya2019.ogg
  · ✅.
- Hyoga (Alfonso Herrera): *«Seiya tuvo el valor de arriesgar su vida para
  salvarla... Yo creí conocer el resultado, pero aún hay mucho que no
  entiendo.»* · voz: la más grave de los 4 (93 Hz) y la **menos expresiva con
  diferencia** (7.0 semitonos, «normal» según la herramienta, frente a
  ~19-24 de los demás) — coincide con su fama de frío/contenido · velocidad
  normal (2.79 palabras/s) ·
  https://static.wikia.nocookie.net/doblaje/images/d/de/HyogaAlfonsoHerrera01.ogg
  · ✅.
- Ikki (Marcos Patiño): *«Vienen por mí o vienen por la armadura dorada, no
  importa, no debieron venir. Patéticos... hoy es el peor día de tu vida:
  estás a punto de revivir tu peor recuerdo una y otra vez, hasta que quedes
  hecho pedazos.»* · voz: grave (116 Hz), muy expresiva (19.2 semitonos),
  amenazante ·
  https://static.wikia.nocookie.net/doblaje/images/5/56/IkkifenixSaintSeiya2019.ogg
  · ✅.
- Saori/Athena (María Fernanda Morales): *«Cuando reencarné como Atena, nací
  con una profecía... Ellos no decidirán quién soy y lo que hago. Nunca he
  querido destruir a la humanidad y nunca lo querré.»* · voz: media (200 Hz,
  la más aguda de los 5), muy expresiva (19.6 semitonos) ·
  https://static.wikia.nocookie.net/doblaje/images/b/b5/AthenaSaintSeiya2019.ogg
  · ✅.
- «Shaun»/Shun (Isabel Martiñón): *«No estoy segura. Podría decirse que
  siempre he sido reacia a la pelea. Solía ser muy inmadura para mi edad...
  mi hermano mayor, Iggy, me enseñó a pelear, pero en vez de enseñarme a
  atacar, me enseñó a protegerme sin lastimar a otros.»* · voz: media (153
  Hz), muy expresiva (18.3 semitonos) ·
  https://static.wikia.nocookie.net/doblaje/images/7/79/ShunIsabelMArti%C3%B1on01.ogg
  · ✅.
- Escena «Final de las Doce Casas» (fandub/edición de fan sobre la serie
  CLÁSICA doblada, con subtítulos incrustados que reproducen el guion latino
  real de los 90): se lee en pantalla «¡Me las vas a pagar!» (0:18),
  «¿Dónde está Athena?» (1:30, gritado por Seiya), «¡El Sol! ¡Se está
  ocultando!» (1:36), «¡Ya es demasiado tarde!» (3:24) ·
  https://www.dailymotion.com/video/x3iigt0 · ✅ (visto fotograma a
  fotograma).

### Punto 12 — Lo que ama el fandom, y qué NO hacer

- **Chistes internos / memes reconocibles**: los Santos de Bronce siempre se
  levantan más fuertes después de cada golpe casi mortal («nunca mueren
  del todo»); el grito del nombre de la técnica antes de usarla (Meteoro de
  Pegaso, Cólera del Dragón, Polvo de Diamante, Cadena de Andrómeda, Ave
  Fénix); el «128% de tu poder» y superar límites imposibles con el Cosmo;
  el poder de la amistad como arma literal contra villanos que se burlan de
  ella y acaban perdiendo · visto en las propias escenas dobladas (Dailymotion,
  clip Doce Casas) y descrito también por reseñas de fans (ssnextdimension.com)
  · ✅.
- **Shun es a menudo confundido con una chica dentro del propio fandom** (por
  su cara delicada y su cloth rosa/blanca) — y en el redoblaje de Netflix
  2019 literalmente lo escribieron como mujer (`Shaun`, ver punto 8): es un
  tema real de la serie, no un error de quien dibuje, pero **no conviene
  dibujarlo como mujer sin avisar** si la lámina se basa en la serie
  clásica/manga, donde es varón · ✅ (con fuente propia, no de memoria).
- **Qué NO hacer** (para no sonar hecho sin ver la serie):
  - No poner una burbuja de diálogo blanca genérica: la propia serie usa
    cartelas con texturas y estilo (ver `partes/texto.md`, punto 6, del
    investigador de texto).
  - No dibujar a Seiya con la Cloth de Pegaso dorada por defecto: su armadura
    icónica es **blanca y roja** (bronce); la dorada es un arco puntual
    (Sagitario, Saint Seiya Omega) — confundirlo es un error típico que el
    fandom nota enseguida.
  - No hacer que Ikki sonría fácil o hable mucho: su gancho es la frialdad y
    las frases cortas y amenazantes (ver frase textual arriba) — si aparece
    alegre sin motivo, no se siente «su» Ikki.
  - No perder de vista que **Athena/Saori es una diosa con autoridad**, no
    sólo una princesa a rescatar: en su frase textual (arriba) ella decide
    por sí misma, no la deciden por ella.
  - No confundir actores de doblaje entre versiones: Ricardo Mendoza (Shiryu)
    e Ikki con Marcos Patiño se repiten en dos versiones distintas (clásica y
    Netflix 2019), pero NO en la tercera (2022); citarlos bien importa mucho
    en un server de doblaje.

### Punto 13 — Descripción profunda de cada personaje (los 6 del encargo)

Formato por personaje: carácter/historia · qué transmite · cómo se expresa ·
dinámicas · **cara en cada emoción** (fotograma/minuto o imagen, con fuente).

**Seiya de Pegaso**
- Carácter: impulsivo, generoso, ardiente y sincero; parece insolente pero es
  de los Santos más nobles y compasivos, incluso con enemigos; terco pero
  fiel a lo que siente · https://saintseiya.fandom.com/wiki/Pegasus_Seiya#Personality
  (de `datos-voz.md`) · ✅.
- Historia/arco: huérfano entrenado en Grecia para ser Santo de Atena;
  motivado por proteger a su hermana Seika y a Saori; en el redoblaje 2019 se
  añade que de niño «Grada» atacó a su hermana y casi lo mata a él (frase
  textual arriba) · ✅.
- Qué transmite: energía y esperanza contra todo pronóstico — es el que nunca
  se rinde aunque esté perdiendo; ver a Seiya da ánimo, no miedo.
- Cómo se expresa: grita el nombre de su técnica («¡Meteoro de Pegaso!»);
  voz grave y muy expresiva (23.7 semitonos, la 2ª más expresiva de los 4
  varones, ver punto 8); tutea a todos, hasta a sus maestros; no usa
  muletillas raras, habla directo y con frases cortas cuando pelea.
- Dinámicas: Shiryu lo calma cuando se precipita; discute con Shaina/villanos
  desafiándolos verbalmente antes de pelear; protege activamente a Saori y a
  su hermana Seika.
- Cara en cada emoción:
  - Alegría → sonríe con los ojos cerrados, mirando sus propias manos
    brillar (poderes recién descubiertos), min. 2:45,
    https://archive.org/download/knights-of-the-zodiac-saint-seiya-episode-12/Knights%20of%20the%20Zodiac%20Saint%20Seiya%20Episode%201.mp4?t=165
    · ✅ (visto en hoja).
  - Rabia → primer plano gritando «¿Dónde está Athena?», dientes apretados,
    min. 1:30, https://www.dailymotion.com/video/x3iigt0?t=90 · ✅.
  - Tristeza → llorando, restregándose la cara con la manga, min. 7:56,
    https://archive.org/download/knights-of-the-zodiac-saint-seiya-episode-12/Knights%20of%20the%20Zodiac%20Saint%20Seiya%20Episode%201.mp4?t=476
    · ✅.
  - Miedo → ojos muy abiertos mirando sus propias manos brillar sin entender
    qué le pasa, min. 6:39, mismo vídeo `?t=399` · ✅.
  - Vergüenza → ⚠️ no encontramos un fotograma claro con minuto (Seiya casi
    no se avergüenza en pantalla: su registro es más ira/orgullo herido que
    vergüenza). Búsquedas: Dailymotion «Seiya avergonzado», «Seiya
    sonrojado», wiki en inglés/es (`srsearch=Seiya blushes/embarrassed`) sin
    resultado claro. Se deja pendiente.

**Shiryu de Dragón**
- Carácter: el más calmado y sereno de los 5; fuerza física enorme (gana
  peleas incluso sin su Cloth); entrenado en los Cinco Picos de Rozan (China)
  por el maestro Dohko · https://anilist.co/character/5922 (de
  `datos-voz.md`) · ✅.
- Historia/arco: pierde la vista defendiendo su Cloth de un ataque de Shura
  (Caballero de Capricornio) y sigue peleando ciego; su maestro Dohko se
  sacrifica/rejuvenece para ayudarlo · ✅ (visto en clip «Dohko rejuvenece»).
- Qué transmite: estabilidad y sacrificio silencioso — el que aguanta el
  golpe para que otros no tengan que hacerlo.
- Cómo se expresa: es el que más rápido habla de los 4 (3.39 palabras/s,
  frente a 2.4-2.8 de los demás) pese a fama de tranquilo — se acelera al
  anunciar su técnica («¡Ahora contemplen! ¡La furia del dragón!»); voz
  grave (106 Hz) y muy expresiva (20.9 semitonos) · fuente: punto 8.
- Dinámicas: hermano mayor sustituto de Shunrei (huérfana a su cuidado);
  rivalidad y respeto con Shura tras la pelea que lo deja ciego; calma a
  Seiya en sus arrebatos.
- Cara en cada emoción:
  - Alegría → torso al descubierto, brazo alzado, boca abierta gritando de
    alegría al ver a su maestro Dohko con vida/rejuvenecido, min. 2:48,
    https://www.dailymotion.com/video/x8x2zig?t=168 · ✅.
  - Tristeza/emoción contenida → primer plano, ojos llorosos, mirando a su
    maestro, min. 2:42, `?t=162` mismo vídeo · ✅.
  - Rabia → viñeta de manga, dientes apretados y mirada fija liberando el
    «Rozan Sho Ryu Ha» (Excalibur) · «Dragon Excalibur.jpg», wiki,
    https://static.wikia.nocookie.net/saintseiya/images/../Dragon_Excalibur.jpg
    (enlace exacto en `partes/video.md`, punto 14) · ⚠️ (imagen fija de wiki,
    sin minuto de vídeo).
  - Miedo → ⚠️ no encontramos un fotograma propio. Es un personaje que
    canónicamente «nunca demuestra miedo por sí mismo» (sí por Shunrei);
    búsquedas: Dailymotion «Shiryu miedo Shunrei», wiki (`srsearch=Shiryu
    afraid`) sin imagen clara.
  - Vergüenza → ⚠️ no encontrado (mismas búsquedas que Seiya, sin resultado).

**Hyoga de Cisne**
- Carácter: frío, calmado, controlado en apariencia; por dentro apasionado y
  devoto a sus ideales; su madre murió ahogada de joven y eso lo marca de
  por vida · https://saintseiya.fandom.com/wiki/Cygnus_Hyoga#Personality (de
  `datos-voz.md`) · ✅.
- Historia/arco: entrena en Siberia bajo Camus de Acuario; su motivación
  secreta es que el poder de Santo le permitiría «visitar» los restos de su
  madre en el fondo del mar; Camus le advierte que esa motivación «egoísta»
  puede matarlo · ✅.
- Qué transmite: contención — parece que no siente nada, y cuando se le
  quiebra la voz (por su madre) es cuando más golpea emocionalmente.
- Cómo se expresa: la voz **menos expresiva de los 4 por lejos** (7.0
  semitonos frente a 19-24 de sus compañeros) y la más grave (93 Hz) — la
  propia medida de `voz.py` confirma con números lo que dice el texto de la
  wiki («calm, collected, unemotional») · fuente: punto 8. No usa muletillas;
  frases más largas y reflexivas que sus compañeros («creí conocer el
  resultado, pero aún hay mucho que no entiendo»).
- Dinámicas: hermano de entrenamiento de Isaak (Kraken); discípulo de Camus;
  el que más rara vez discute, pero el que más rencor guarda cuando alguien
  amenaza su recuerdo de su madre.
- Cara en cada emoción:
  - Rabia → primer plano en pleno combate, ojos entrecerrados, boca abierta
    gritando el ataque, min. 0:51, https://www.dailymotion.com/video/x7v5mmz?t=51
    (clip «Hyoga de Cisne vence a Ichi de Hidra con el Polvo de Diamantes»)
    · ✅.
  - Tristeza → primer plano con el ceño fruncido, mirando el mar, justo
    antes de la escena de su madre ahogada (a la que sostiene en brazos,
    pálida, ojos cerrados), min. 0:24 y 0:48,
    https://www.dailymotion.com/video/x52rr67?t=24 y `?t=48` · ✅.
  - Alegría, miedo y vergüenza → ⚠️ no encontramos fotograma propio para
    ninguna de las tres. Esto **es también un dato real de personaje**: ni la
    ficha de personalidad ni los clips vistos lo muestran sonriendo,
    asustado o avergonzado — su registro emocional en pantalla es
    deliberadamente plano salvo la ira/dolor de la técnica y el recuerdo de
    su madre (confirmado por la propia medida de expresividad de voz, la más
    baja de los 6). Búsquedas: Dailymotion «Hyoga sonríe», «Hyoga feliz»,
    wiki (`srsearch=Hyoga smiles/afraid`), sin imagen ni clip claro.

**Shun de Andrómeda**
- Carácter: pacifista, el más reacio a pelear de los 5; bondadoso por
  naturaleza; su paciencia es enorme pero cuando se agota se vuelve un
  luchador letal y hábil · https://saintseiya.fandom.com/wiki/Andromeda_Shun#Personality
  (de `datos-voz.md`) · ✅. En el redoblaje Netflix 2019 (voz femenina, ver
  punto 8) se añade en su propia voz: «solía ser muy inmadura para mi edad;
  me quejaba y lloraba cuando las cosas no salían a mi manera... los niños me
  molestaban pero no me defendía» — hasta que su hermano Ikki le enseña a
  pelear defensivamente, «sin lastimar a otros» · ✅ (audio propio).
- Historia/arco: hermano menor de Ikki; su Cloth (cadenas de Andrómeda) es
  defensiva, no ofensiva por diseño; en el arco de Hades es poseído y se
  convierte en un alter-ego oscuro.
- Qué transmite: ternura y vulnerabilidad — da ganas de proteger, no de
  temer, salvo en su versión poseída.
- Cómo se expresa: voz media (153 Hz) y muy expresiva (18.3 semitonos, en la
  versión con actriz mujer); en la versión con actor varón (clásica) su
  frase típica es negarse a pelear hasta el último momento; no grita sus
  ataques con la agresividad de los demás, más bien los explica.
- Dinámicas: sobreprotegido por su hermano Ikki (con quien discute más:
  Ikki quiere que huya, Shun se queda a ayudar a sus amigos); el que más
  fácil hace reír o llorar de ternura al grupo.
- Cara en cada emoción:
  - Miedo → primer plano, ojos muy abiertos, boca entreabierta, mirando algo
    fuera de cuadro con alarma, min. 4:07,
    https://archive.org/download/knights-of-the-zodiac-saint-seiya-episode-12/Knights%20of%20the%20Zodiac%20Saint%20Seiya%20Episode%206.mp4?t=247
    · ✅.
  - Tristeza → primer plano con lágrimas, min. 4:44, mismo vídeo `?t=284` ·
    ✅; refuerzo con imagen fija de la wiki «Shun crying.jpg» ·
    https://static.wikia.nocookie.net/saintseiya/images/.../Shun_crying.jpg
    (buscar por nombre exacto en Special:Search de la wiki) · ⚠️ (no se
    resolvió la URL exacta de esta segunda imagen, sólo el nombre de
    archivo).
  - Rabia → su «yo» poseído por Hades alza un báculo con expresión oscura —
    pero ES su alter-ego, no su carácter normal: «Saint Seiya Hades
    Arc-Hades Shun lifts a staff.png», wiki (citada también en
    `partes/video.md`, punto 14) · ⚠️ (hay que aclarar en la lámina que es
    su versión poseída, no él).
  - Alegría → primer plano, ojos muy abiertos y sonrisa suave mirando hacia
    arriba (justo cuando se revela el cofre dorado de Sagitario sobre un
    pedestal), min. 8:21,
    https://archive.org/download/knights-of-the-zodiac-saint-seiya-episode-12/Knights%20of%20the%20Zodiac%20Saint%20Seiya%20Episode%204.mp4?t=501
    · ✅ (hoja 147 de `ep04a`, identificado por el color de su Cloth
    rosa/blanca de Andrómeda, igual que en la ficha de imágenes de
    saintseiya.fandom.com).
  - Vergüenza → ⚠️ seguimos sin fotograma propio con minuto tras ver también
    el ep.1 completo, el ep.2 completo y los primeros 15 min del ep.4.
    Búsquedas: Dailymotion «Shun sonríe», «Shun feliz», wiki
    (`srsearch=Shun smiling/embarrassed`) sin resultado claro.

**Ikki de Fénix**
- Carácter: el más fuerte de los Santos de Bronce en potencia base; conocido
  desde niño como el más duro de los 100 huérfanos; frío, cortante, casi sin
  paciencia para explicarse · https://anilist.co/character/5923 (de
  `datos-voz.md`) · ✅.
- Historia/arco: entrenado en solitario en la Isla de la Reina Muerte; amó a
  Esmeralda, muerta en un incendio que él no pudo evitar — guarda un
  recuerdo dorado de ella (visto en la escena, ver abajo); protector
  obsesivo de su hermano menor Shun.
- Qué transmite: intimidación y lealtad feroz — el que da miedo hasta que se
  ve por quién pelea.
- Cómo se expresa: frases cortas, amenazantes, sin relleno («patéticos...
  hoy es el peor día de tu vida»); voz grave (116 Hz) y muy expresiva (19.2
  semitonos) pero SIN calidez — la expresividad es de amenaza, no de
  emoción positiva (fuente: punto 8, comparar con el tono de Seiya en el
  mismo rango de semitonos pero en frases de aliento, no de amenaza).
- Dinámicas: choca con Shun (quiere alejarlo del peligro, Shun se resiste);
  es el Santo de Bronce que menos convive con el grupo (llega y se va solo).
- Cara en cada emoción:
  - Tristeza → sostiene un objeto pequeño y dorado en la palma (recuerdo de
    Esmeralda), torso desnudo, mirada baja, min. 3:53,
    https://archive.org/download/knights-of-the-zodiac-saint-seiya-episode-12/Knights%20of%20the%20Zodiac%20Saint%20Seiya%20Episode%206.mp4?t=233
    · ✅.
  - Rabia → puño en alto envuelto en aura de fuego con forma de alas,
    dientes apretados, min. 4:54-4:57, mismo vídeo `?t=294`; también primer
    plano de ojo con reflejo de fuego, min. 3:58, `?t=238` · ✅.
  - Alegría, miedo y vergüenza → ⚠️ no encontramos fotograma propio para
    ninguna. Coincide con su ficha de personaje (AniList, `datos-voz.md`):
    lo describen sólo por dureza y fuerza, nunca por sonreír o asustarse.
    Búsquedas: Dailymotion «Ikki sonríe», «Ikki feliz», «Ikki asustado»,
    wiki (`srsearch=Ikki smiles/afraid`), sin imagen ni clip claro — parece
    un rasgo real de personaje (casi nunca se le ve reír ni temer en
    pantalla) más que un hueco de búsqueda.

**Saori Kido / Athena**
- Carácter: seria, cumplidora, serena, muy compasiva; de niña fue una
  heredera consentida que trataba mal a los huérfanos a su cargo, hasta que
  descubre quién es realmente · https://saintseiya.fandom.com/wiki/Saori_Kido#Personality
  (de `datos-voz.md`) · ✅.
- Historia/arco: nieta y heredera de Mitsumasa Kido; reencarnación de la
  diosa Atena; en el redoblaje 2019 dice de sí misma: «nací con una
  profecía... ellos no decidirán quién soy y lo que hago» — deja claro que
  es ella quien manda en su propio destino, no sus enemigos (frase textual,
  punto 8) · ✅.
- Qué transmite: autoridad serena — no es una damisela, es quien decide ir a
  la guerra por amor a la Tierra aunque odie las armas.
- Cómo se expresa: voz media-aguda (200 Hz, la más aguda de los 5 medidos) y
  muy expresiva (19.6 semitonos); habla en primera persona con determinación
  («probaré que la profecía se equivoca»), sin muletillas.
- Dinámicas: Seiya es quien más la protege y quien menos la trata como
  «ama»; para los Santos de Bronce es a la vez jefa y amiga de infancia.
- Cara en cada emoción:
  - Tristeza → desvanecida/muriendo, ojos cerrados, cabeza inclinada, con el
    subtítulo en pantalla «Sollozando», min. 1:42,
    https://www.dailymotion.com/video/x3iigt0?t=102 · ✅.
  - Miedo → primer plano, ojos muy abiertos, mirando hacia un ataque fuera
    de cuadro, min. 2:17, https://archive.org/download/knights-of-the-zodiac-saint-seiya-episode-12/Knights%20of%20the%20Zodiac%20Saint%20Seiya%20Episode%206.mp4?t=137
    · ✅.
  - Alegría → primer plano, sonrisa suave, ojos entornados mirando hacia
    arriba con un brillo dorado alrededor (avance de la 2ª temporada
    insertado tras los créditos, se repite igual en los ep. 1 y 6), min.
    22:56,
    https://archive.org/download/knights-of-the-zodiac-saint-seiya-episode-12/Knights%20of%20the%20Zodiac%20Saint%20Seiya%20Episode%206.mp4?t=1376
    · ✅ (hoja 244 de `ep06_final`, visto fotograma a fotograma; la misma
    toma aparece también en el ep.1 al mismo minuto).
  - Rabia y vergüenza → ⚠️ seguimos sin fotograma propio con minuto para
    ninguna de las dos, tras ver también los 8-23 min finales de los
    episodios 1 y 6 completos (antes sólo se habían visto los primeros 7-8
    min de cada uno) y el episodio 2 completo. Encaja con su ficha: Athena
    «odia las armas» y es «extremadamente compasiva» — en todo lo visto su
    registro es solitud/autoridad/tristeza/alegría serena, no ira. Búsquedas:
    Dailymotion «Saori sonríe», «Athena feliz», «Saori enojada», wiki
    (`srsearch=Saori/Athena angry/happy`), hojas completas de ep01, ep02 y
    ep06 (Internet Archive), sin imagen ni clip claro de rabia o vergüenza.

### Punto 20 — Gustos y detalles de cada personaje

- Seiya: edad 13, cumpleaños 1 de diciembre, tipo de sangre B ·
  https://anilist.co/character/2285 (de `datos-voz.md`) · ✅. Objeto/símbolo
  que siempre lo define: la Cloth de Pegaso blanca/roja (bronce), no la
  dorada de Sagitario (arco puntual) · ✅ (visto en fotogramas).
- Shiryu: edad 14, cumpleaños 4 de octubre · https://anilist.co/character/5922
  · ✅. Marca corporal propia: tatuaje/marca de dragón rojo en la espalda,
  ligado a su cosmo (no es un tatuaje literal según el manga) · «Shiryu
  Tattoo.png», wiki (visto en `/tmp/…/wiki_extra/shiryu_tattoo.jpg`) · ✅.
- Hyoga: edad 14, cumpleaños 23 de enero, altura 173 cm ·
  https://anilist.co/character/5921 · ✅. Objeto que siempre lo acompaña (en
  espíritu): el recuerdo del cuerpo de su madre bajo el hielo, que visita
  buceando — su motivación secreta para ser Santo · ✅ (ficha + clip
  `x52rr67`).
- Shun: edad 13, cumpleaños 9 de septiembre · https://anilist.co/character/2440
  · ✅. Objeto propio: la cadena de Andrómeda (arma-armadura defensiva,
  parte de su Cloth, no un accesorio aparte) · ✅.
- Ikki: edad 15, cumpleaños 15 de agosto · https://anilist.co/character/5923
  · ✅. Objeto que siempre lleva: un pequeño recuerdo dorado de Esmeralda que
  guarda en la palma de la mano (visto en fotograma, punto 13) · ✅ (visto
  directamente, no sólo de ficha).
- Saori: edad 13, cumpleaños 1 de septiembre · https://anilist.co/character/5628
  · ✅. Antes de saber que era Atena: empresaria exitosa, aficiones equitación
  y piano · https://saintseiya.fandom.com/wiki/Saori_Kido#Abilities (de
  `datos-voz.md`) · ✅. Objeto que siempre la define: el báculo dorado de
  Niké (diosa de la victoria) que porta como Atena · ✅ (visto en fotogramas
  y en fichas de `partes/video.md`).

### Punto 21 — Por qué la gente la ama

- Razón repetida en reseñas de fans (ssnextdimension.com, en español): Saint
  Seiya introdujo en Latinoamérica el concepto del «poder de la amistad» y el
  «superar tu propio límite» de forma muy física y emotiva, con una banda
  sonora orquestal muy reconocible · https://www.ssnextdimension.com/el-anime/saint-seiya-clasico/su-exito-en-japon/
  · ⚠️ (una fuente, tono de opinión más que dato duro).
- El doblaje clásico en sí es un motivo de cariño aparte: **Jesús Barrero
  (voz de Seiya) fue también el director de doblaje** de la serie clásica —
  el fandom hispano lo trata como el «dueño» de la voz de Seiya; tras su
  muerte en 2015 se hicen tributos (ver punto 22, fandub «Tenkai Hen
  Overture», dedicado a él) · Doblaje Wiki (ficha) + hallazgo del fandub ·
  ✅.
- **Escena que hace llorar** (clip real visto, doblaje latino clásico): la
  «muerte de Athena»/final de las Doce Casas — Seiya llega a la cámara del
  Patriarca justo cuando Saori se desvanece («Sollozando» en pantalla, min.
  1:42) tras haberse clavado la flecha de Sagitario para demostrar que es la
  diosa; música orquestal dramática de fondo, planos cerrados de su cara
  pálida y el pelo suelto · https://www.dailymotion.com/video/x3iigt0?t=102
  · ✅ (visto fotograma a fotograma, con el propio texto en pantalla del
  doblaje).
- Con qué personaje se identifica el público (según los votos de AniList y
  Danbooru del punto 7): más con **Ikki** (el secundario duro que no es el
  protagonista) y con **Saori/Athena** en el arte de fans — el dueño del
  server acertó al avisar que a veces el secundario gana al protagonista.

### Punto 22 — Fan dubs y comunidad hispana

- **Fandub de audio latino, «Saint Seiya Tenkai Hen Overture» (2017)**,
  descrito como tributo a Jesús Barrero (voz/director de Seiya en la serie
  clásica, fallecido en 2015) · https://www.youtube.com/watch?v=iRJBQJDfLBE
  (hallado por WebSearch; no se pudo bajar el vídeo por el bloqueo de
  YouTube en este servidor, pero el título y la descripción del propio canal
  lo confirman) · ⚠️ (un solo dato, sin verlo directamente).
- **Cover metal de «Pegasus Fantasy» con Mauren** (cantante que participó en
  el doblaje musical de la serie clásica en México, según la ficha de
  Doblaje Wiki: «adaptador_music = Mauren Mendo») — cover publicado en 2017,
  con la propia voz original latina de la canción · https://www.youtube.com/watch?v=9CO6Ta3xfUA
  · ✅ (coincide el nombre de la cantante con el crédito real del doblaje).
- **Clips de la serie doblada resubidos por fans latinoamericanos en
  Dailymotion** (canal «Tomatazos»: «La muerte de Athena», «Dohko
  rejuvenece»; canal «Rapsta A.K.A. Otro Gamer Loquendero Mas»: openings y
  endings de Azteca 7 2022) — de `datos-voz.md`, usados también en el punto
  13 arriba · ✅ (vistos con `fotogramas.py`).
- Podcasts de fans en español sobre la serie, en Internet Archive: «Otacast
  #12a/b - Saint Seiya (CDZ)», «Universo Saint Seiya» (varios episodios),
  «MexidÃ£o Cast #5 - Especial Saint Seiya» — de `datos-video.md` · ✅
  (existencia confirmada; no se transcribieron por tiempo).

## Lo mejor para la lámina

- La frase real de Saori/Athena del redoblaje 2019 («Ellos no decidirán
  quién soy y lo que hago») es perfecta para un canal de escritura o de
  autoafirmación: es Atena hablando con su propia autoridad, no una
  princesa pasiva.
- El dato de que **Ikki gana a Seiya en favoritos de fans** (AniList) apoya
  usar a Ikki (con su gesto de guardar el recuerdo dorado de Esmeralda,
  min. 3:53 del ep.6) como personaje secundario protagonista de una lámina,
  tal como pidió el dueño.
- Hyoga es el personaje con la voz medida más «plana» de los 6 (7.0
  semitonos frente a 18-24 de los demás): útil para un canal de doblaje que
  quiera explicar «actuar con la voz contenida también es actuar».

## No encontré

- ⚠️ El **resultado exacto** de la encuesta Netorabo 2021 (quién quedó 1º):
  se confirmó que existió (18 690 votos) pero no su tabla de resultados.
  Búsquedas: «Saint Seiya Netorabo encuesta 2021 resultado», «Saint Seiya
  character poll Netlab 2021» (WebSearch, español e inglés).
- ⚠️ Caras de **vergüenza** con fotograma y minuto propio para los 6
  personajes: no se encontraron para ninguno de los 6 (ver detalle en punto
  13 de cada uno). Es la emoción menos representada en las escenas de acción
  que están disponibles fuera de YouTube (Dailymotion/Internet Archive); se
  necesitaría un episodio completo de comedia/relleno, que no se pudo bajar
  con el bloqueo de YouTube en este servidor.
- ⚠️ Cara de **miedo** propia para Shiryu e Ikki, y de **alegría** propia para
  Hyoga e Ikki: no se encontraron con minuto pese a ver también el ep.1 y el
  ep.6 completos, el ep.2 completo y los primeros 15 min del ep.4 (ver
  detalle arriba); en Hyoga e Ikki parece un rasgo real de personaje (casi no
  se les ve reír ni temer en los clips vistos), no sólo un hueco de búsqueda.
  (La alegría de Saori y de Shun sí se encontraron en esta tanda, ver punto
  13 arriba.)
- ⚠️ Transcripción completa de los podcasts en español de Internet Archive
  (Otacast, Universo Saint Seiya): se confirmó que existen y de qué tratan,
  pero no se transcribieron por el tiempo que llevaría cada uno (varias
  decenas de minutos cada episodio).

## Bitácora de búsqueda

- Doblaje Wiki, API directa (`action=parse&prop=wikitext`), en español:
  página «Los Caballeros del Zodiaco» (ficha + reparto clásico completo) y
  «SAINT SEIYA: Los Caballeros del Zodiaco» (ficha + reparto Netflix 2019,
  con enlaces a muestras `.ogg`) — ambas nuevas respecto a `datos-voz.md`,
  que sólo traía la ficha de la 2ª temporada del redoblaje.
- `saintseiya.fandom.com/api.php`, `list=search&srwhat=text` y
  `prop=images`, en inglés: búsqueda de imágenes con nombre de archivo que
  contenga «crying», «smiling», «angry», «scared», «blushing», «laughing»,
  «afraid», «furious» en las páginas de los 6 personajes y en todo el
  namespace de archivos — sólo dio resultado claro para «Shun crying.jpg».
- Dailymotion API (`api.dailymotion.com/videos?search=…`), en español:
  «Hyoga Cisne doblaje», «Hyoga llora Camus», «Shiryu Shura ciego furioso» —
  se usaron 2 clips reales (Hyoga vs Ichi de Hidra, Camus hunde el barco de
  la madre de Hyoga) y se descartó uno (Shura vs Shiryu, resultó ser un
  tráiler de videojuego sin primeros planos de cara).
- `fotogramas.py` ×4 sobre clips nuevos de Dailymotion (Hyoga ×2, Shiryu vs
  Shura descartado) — hojas en `/tmp/claude-0/trabajo/39-saint-seiya-voz/`.
- `voz.py` ×6 sobre muestras de audio oficiales `.ogg` de Doblaje Wiki
  (Seiya, Shiryu, Hyoga, Shun, Ikki, Saori/Athena, todas de la versión
  Netflix 2019) — primera vez que se usan muestras de audio reales para este
  encargo; permitió sacar frases textuales Y medir tono/expresividad/
  velocidad con datos, no de oído.
- WebSearch (2 búsquedas, en español): «Saint Seiya encuesta oficial
  personaje más popular Shueisha Animage ranking» → Animage 1986 (Shun
  10º, Shiryu 11º, Hyoga 15º), Netorabo 2021; «"Saint Seiya" fan dub
  español latino cover opening YouTube parodia hispana» → fandub tributo a
  Jesús Barrero, cover de Mauren.
- Hojas de contacto reaprovechadas del investigador de vídeo (sin volver a
  bajar los vídeos): `ep01/hojas` (×4), `ep06/hojas` (×2), `escena3_12casas`,
  `escena2_dohko`, `opening`, `trailer` (descartado: es del live-action de
  Sony, no del anime) — todas en
  `/tmp/claude-0/trabajo/39-saint-seiya-video/`.
- **Segunda tanda (esta sesión)**: con `fotogramas.py --cortes` sobre los
  mismos vídeos de Internet Archive, se completó lo que faltaba de ver de
  los episodios 1 y 6 (min 7:50/7:40 hasta el final, ~23:00 — antes sólo se
  habían mirado los primeros 7-8 min de cada uno) y se miró **por primera
  vez** el episodio 2 completo (torneo Galaxian Wars) y los primeros 15 min
  del episodio 4 («Nebula Chain», el episodio centrado en Shun) — hojas en
  `/tmp/claude-0/trabajo/39-saint-seiya-voz/ep01_final`, `ep06_final`,
  `ep02` y `ep04a`. De ahí salió la alegría de Saori (avance de temporada 2
  insertado tras los créditos, se repite igual en ep.1 y ep.6) y la de Shun
  (ep.4, min 8:21). Se revisó también `saintseiya.fandom.com` (wikitext de
  «Saint Seiya: Knights of the Zodiac») para los nombres/colores de Cloth en
  inglés de esta versión (Long=Shiryu, Magnus=Hyoga, Nero=Ikki,
  Shaun=Shun, Sienna=Saori) y así no confundir personajes secundarios del
  torneo con los 6 del encargo.
- Se miró también la pelea de entrenamiento con un rival de larga cabellera
  oscura y túnica morada en el ep.2 (min 18:15-20:00, hojas 7-8 de `ep02`) y
  una escena de niños burlándose de un dibujo de Seiya en el ep.1 (min
  5:42-5:53, hoja 3 de `ep01_final`) como posibles candidatas a
  Shiryu-rabia (con minuto) y Seiya-vergüenza: en ambos casos la expresión es
  ambigua (podría leerse como enfado/dolor, no claramente vergüenza o un
  Shiryu identificable con certeza) y se decidió NO forzarlas — se dejan
  fuera para no inventar.

Sigue: puntos 7, 8, 12, 20, 21 y 22 están completos. Del punto 13 (obligatorio)
van 16 de 30 casillas con fotograma+minuto propio (antes 14; esta tanda sumó
Saori-alegría y Shun-alegría). Faltan, con sus búsquedas ya hechas (ver
arriba, marcadas ⚠️): Seiya-vergüenza; Shiryu-rabia (sólo imagen fija de
wiki, sin minuto), miedo y vergüenza; Hyoga-alegría, miedo y vergüenza;
Shun-vergüenza (su rabia sigue sólo con la imagen de su alter-ego poseído);
Ikki-alegría, miedo y vergüenza; Saori-rabia y vergüenza. Vía sugerida si se
retoma: de la colección `archive.org/details/knights-of-the-zodiac-saint-seiya-episode-12`
faltan por mirar el resto del ep.4 (15-23 min) y los episodios 3, 5 y 7-12
completos (con `fotogramas.py --cortes`, igual que esta tanda) — el ep.3
(«Enter the Dragon», debut de Shiryu) y el ep.5 («The Black Knights», grupo
completo) son los más prometedores para Shiryu e Ikki; para vergüenza en
concreto no ha aparecido en ninguno de los 4 episodios ya vistos por
completo o en parte (1, 2, 4 parcial, 6), así que puede necesitar
directamente escenas de comedia/vida diaria fuera de las peleas (el «avance
de temporada 2» sí dio alegría pero no vergüenza) más que más episodios de
la misma serie de acción.
