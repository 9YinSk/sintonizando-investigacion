# Investigador de voz y personajes · My Hero Academia

Repaso de una biblia ya escrita con **red cerrada** (no pudo abrir Fandom,
Doblaje Wiki ni YouTube). Mis puntos (EQUIPO.md): **7, 8, 12, 13, 20, 21, 22**.
Empecé por `partes/datos-voz.md` (AniList, Doblaje Wiki en crudo, Danbooru,
Dailymotion, Reddit) y por `seccion.py --avisos`: no repito esas consultas.
Ahora la red está abierta: confirmo con la **API de Doblaje Wiki** (wikitext
completo, no sólo el resumen que dio `recolectar.py`), la **wiki en inglés**
de Fandom (perfiles oficiales de los *databooks*, tomo 1 y 2) y **vídeos reales
en Dailymotion con audio del doblaje latino** (procesados con `voz.py` y
`fotogramas.py`, mirados con Read).

## Punto 7 · Personajes: popularidad oficial y de fans

- **Encuestas oficiales de Shonen Jump (todas, 1.ª a 9.ª + la mundial)**,
  sacadas del wikitext de la wiki en inglés (`Popularity_Polls`), con voto
  real, no resumen ✅ (https://myheroacademia.fandom.com/wiki/Popularity_Polls):
  - 1.ª encuesta (2015, 11 125 votos): 1. **Izuku** (2314) · 2. Todoroki (1987)
    · 3. Bakugo (1764) · 4. Uraraka (652) · 5. All Might (627) · 9. **Aizawa** (378).
  - 9.ª encuesta (2023-24, votos reexaminados tras un error, [Chapter 403/419/425]):
    1. **Bakugo** (23 441) · 2. Deku (18 488) · 3. Todoroki (13 478) · 13. Aizawa
    (2745) · 15. All Might (2499). **Corrijo el dato que ya tenía la biblia**: no es
    «Jump n.º 19», es la **9.ª encuesta** de la revista (la wiki en inglés la nombra
    así con las mismas cifras) ✅.
  - **Total acumulado de las 9** («Overall»): 1. **Bakugo** (1 647 611) · 2. Deku
    (1 217 357) · 3. Todoroki (630 398) · 4. **Aizawa** (259 715) · 5. Kirishima
    (247 533) · 12. All Might (107 060) ✅.
  - Bakugo pasa a 1.º **a partir de la 2.ª encuesta** y no la suelta ✅ (coincide
    con lo que ya decía la biblia por fuentes chinas).
- **World Best Hero (mundial, Crunchyroll, 6,12 M votos, ya en la biblia)**:
  añado el **desglose regional** que faltaba, del mismo wikitext ✅:
  - **Latinoamérica y el Caribe**: 1. **Bakugo** · 2. Deku · **3. Kirishima**
    (¡el público latino lo sube más que el resto del mundo: es 5.º en el
    total global!) · 4. Todoroki · 5. **Aizawa** · 6. Dabi · 7. Hawks.
  - **Europa**: 1. **Deku** · 2. Bakugo · 3. Todoroki (la única región donde
    Deku gana, ya lo decía la biblia; ahora con la wiki como 2.ª fuente).
  - Dato para la lámina de este canal (profesores): **Aizawa entra en el
    top 5 en Latinoamérica y en el top 4 del acumulado histórico**, muy por
    encima de All Might en ambos casos ✅.
- Lo de Danbooru (más dibujado por fans) **ya está confirmado en
  `datos-voz.md`**, no lo repito: Deku 8508, Bakugo 7781, Uraraka 5933,
  Todoroki 2893, Aizawa 806, All Might 806.

## Punto 8 · Doblaje latino (el más pesado: dos fuentes por nombre)

Fuente base para todo esto: el **wikitext completo** de
`https://doblaje.fandom.com/es/wiki/My_Hero_Academia` (la API con
`action=parse&prop=wikitext`, no la web). Es una sola wiki, así que para
✅ busco **una segunda fuente fuera de Doblaje Wiki** (ANMTV, IMDb, Behind
The Voice Actors, o un audio que yo mismo transcribí).

### Nombres que la biblia tenía en ⚠️ y ahora subo a ✅

| Personaje | Actor/actriz | 2.ª fuente (además de la ficha de Doblaje Wiki) | Estado |
|---|---|---|---|
| Ochaco Uraraka (T1-6 ep.1) | **Andrea Valentina Villaverde** | [Behind The Voice Actors](https://www.behindthevoiceactors.com/tv-shows/My-Hero-Academia/Uravity-Ochaco-Uraraka/) la lista igual (la web da 403 al abrirla; cito el resultado del buscador) | ✅ |
| Tenya Iida | **Luis Geraldo Carreño Pinango** | tuit de ANMTV (ya la tenía la biblia) + la propia ficha, que cita un vídeo de YouTube de Luis Carreño hablando del doblaje | ✅ |
| Burnin | **Gigliola Mariangel** («Gigliola P. Mariangel» en créditos; el tuit de ANMTV la abrevia «Gigliola MC») | tuit de ANMTV + ficha (coincide personaje y fechas T5-8) | ✅ |
| Hanta Sero | **Braulio Hernández** (T1-5) → **Mauricio Del Valle** (T6-8, se retira Braulio) | la wikitext lo cuenta como historia completa (ver «Sobre el reparto» abajo), + ya estaba en `datos-voz.md` | ✅ |
| Yuga Aoyama | **Hernán Andrio Chavarro** (T1-7) → **Ignacio Ortuondo** (T8) | ficha (columna de actor, no sólo el resumen) | ✅ |
| Katsuki Bakugo | **Rómulo A. Bernal** | la ficha lo pone en la **columna de actor directamente** (antes sólo se deducía de que @Dr0mz fuera Bakugo y director) | ✅, ya no es deducción |

### El misterio de Aizawa en la T1: resuelto (no es «José Arenas»)

La biblia decía «un resumen dijo José Arenas, no lo pude confirmar». **Ese
nombre no aparece en ningún sitio del wikitext.** Lo que sí dice la wiki,
con pelos y señales, en «Sobre el reparto» ✅:
- **Shota Aizawa Y Tomura Shigaraki** los interpretó primero **Eduardo
  Wasveiler** en la T1. Por la pandemia, viajes y motivos personales no
  pudo grabar presencial el resto de temporadas (no estaba permitido
  grabar a distancia todavía), así que lo sustituyeron: **Ernesto Daniel
  Rumbaut** en Aizawa y **Rómulo A. Bernal** en Shigaraki, **redoblando**
  todo lo que había grabado Eduardo.
- Fue una urgencia: el cliente pedía no cambiar la voz de ningún
  personaje importante. Rómulo dijo que, con más tiempo, habría buscado a
  alguien con un registro parecido al de Eduardo para Shigaraki.
- Al estrenarse la serie **se conservaron algunos loops y gestos** de
  Eduardo como Aizawa; meses después **también esos se regrabaron** con
  Rumbaut y se reemplazaron en Funimation.
- Eduardo Wasveiler **volvió** a la serie en la T3, con otros personajes.
- **Lo mismo le pasó a Kurogiri**: primero **Odin Subero** (T1, por salud
  no pudo seguir) → **Héctor José Pernia Almenara** desde la T2 (redobló
  todo, aunque quedaron algunos gestos de Odin).

### El equipo de dirección (de la ficha técnica de la wiki, con su propia cita a un vídeo de YouTube)

| Puesto | Quién | Temporadas |
|---|---|---|
| Dirección de doblaje | **Rómulo A. Bernal** | 1-2, 4-8 |
| | Judith Noguera | 2-4 |
| | Georgina Sánchez | 4 |
| | **Samuel Lazcano** | 8 (**sólo eps. 166-170**, colaboró con Rómulo; lo confirma también la ficha propia de la 8.ª temporada y aparece independiente en un resultado de búsqueda sobre su biografía) |
| Dirección de casting | Rómulo A. Bernal (5-8) · Judith Noguera (5) | |
| Traducción | Jesús Mercado (1-6) · **Gigliola P. Mariangel** (7-8, la misma actriz de Burnin) | |
| Adaptación | Judith Noguera (2-5) · **Georgina Sánchez (4-5)** · Katya Ojeda (4) · Gigliola Mariangel (5-8) | |

⚠️ **Corrijo con cautela, sin borrarlo**: la biblia decía, citando a
3DJuegos, que la película 4 (*Ahora es tu turno*) la dirigió «Gina
Sánchez». En la ficha de Doblaje Wiki, **Georgina Sánchez** sólo figura
como **adaptadora** de la T4-5 de la serie, nunca como directora, ni de la
serie ni de la película. Puede que 3DJuegos confundiera el rol; dejo las
dos versiones con su fuente, sin quedarme con ninguna.

**La T8 (final) sí se dobló y confirma fechas exactas** (ficha propia,
`My_Hero_Academia/8ª_temporada`): grabación del 10-10-2025 al 13-1-2026,
estreno en Latinoamérica el 8-11-2025, fin el 17-1-2026 en Crunchyroll ✅.

### Frases textuales del doblaje latino — encontradas oyendo clips reales (antes era «no encontré»)

Saqué estos clips de la lista de Dailymotion de `datos-voz.md`/nuevas
búsquedas en la API de Dailymotion, con audio del **doblaje latino de
Funimation** (marca de agua «FUNIMATION» visible), transcritos con
`voz.py` (Whisper: **revisado a oído**, marco con ⚠️ lo que no cuadra del
todo) y mirados con `fotogramas.py` + Read para confirmar la escena:

- **«¡Yo he venido!»** — All Might llega a salvar a Izuku del Villano
  Limo (escena de origen) ✅ (oído y visto: minuto 0:10,
  https://www.dailymotion.com/video/x618t31?t=10 — frame con All Might en
  forma musculosa, subtítulo en inglés «I am here!» quemado en el vídeo,
  audio en español).
- **«¡Ya estoy aquí!»** — la MISMA frase, en **otro montaje** (recopilación
  de la escena del callejón) ✅ (minuto 0:41,
  https://www.dailymotion.com/video/x7xktih?t=41). **Las dos frases
  existen** en distintos montajes/temporadas del doblaje; no puedo asegurar
  cuál es la de la primera emisión del episodio 1 sin ver el capítulo
  entero (⚠️), pero ambas están dichas con la voz de Orlando Noguera.
- **«Puedes ser un héroe.»** — la frase que cambia la vida de Izuku, dicha
  por All Might flaco en el callejón al atardecer ✅ (oído **y** visto:
  minuto 2:43, https://www.dailymotion.com/video/x7xktih?t=163 — miré el
  fotograma: silueta a contraluz, cielo naranja, cerezos). **Ojo**: la
  biblia decía «Tú puedes ser un héroe» (de memoria); el audio real dice
  **«Puedes ser un héroe»**, sin el «Tú». Corrijo con el fotograma+audio
  como prueba.
- **Los insultos de Bakugo a Deku** (misma escena, después de que Deku
  intente ayudarlo con el Villano Limo), minuto 0:14 a 0:22 del mismo
  vídeo, ✅: «**Eres un fracasado sin don, sin juicio**» · «**¡No me
  menosprecies!**» · «**¡Respeta, perdedor!**». (Antes la biblia decía
  «no encontré los insultos exactos»).
- **Kota y Mandalay (arco del campamento, Deku vs. Muscular, ep. 13
  aprox.)**, del clip «Deku vs Muscular» ya listado en `datos-voz.md`
  (https://www.dailymotion.com/video/x7xksc8), oído con `voz.py` ✅:
  - 0:26-0:27: «¡Tienes que salvarlo! ¡Debes recordar tu origen!»
  - 3:54-3:57: «Alguien que arriesgará su vida por ti. Alguien que será
    un héroe.» — la frase que cierra el arco de Kota (aprender a confiar
    de nuevo en los héroes).
- **Rei Todoroki, el recuerdo del agua hirviendo** (arco de Todoroki),
  encontrado con la misma técnica en
  https://www.dailymotion.com/video/x7xkvbk, oído y **visto** (el
  fotograma del minuto 0:20 la muestra de espaldas junto a la tetera) ✅:
  «Mamá, me estoy volviendo loca… Los niños se parecen más a él cada
  día… Shoto, el lado izquierdo… a veces me parece tan espantoso… ya no
  puedo criarlo, siento que no debo hacerlo.» Es el instante justo antes
  de que le eche el agua hirviendo a Shoto: la escena que explica su
  cicatriz.

### Cómo adapta el doblaje (directo del wikitext, sección «Sobre la adaptación»)

- 個性 (*kosei*) = **«Don»** ✅ (coincide con lo que ya decía la biblia,
  ahora con la cita exacta de la wiki, no un resumen).
- **U.A.** se pronuncia como se lee en español, no «yuei» ✅.
- **«Kacchan»** se deja sin traducir aunque el «-chan» no exista en
  español ✅.
- **Ningún alias de héroe o villano se traduce**, salvo **Trece** y
  **Tigre** (porque esos dos ya nacen en japonés en el original; el resto
  nace en inglés) ✅. Dato nuevo, útil para el punto 6/18 del redactor.
- Nejire Hado: su alias «Nejire-chan» se adapta a secas, **«Nejire»**
  (el doblaje no usa honoríficos japoneses) ✅.
- Dones y técnicas se traducen **excepto** One For All, All For One,
  Chronostasis y Overhaul (coinciden con el alias de quien los tiene) ✅.
- Los **«Smash»** de All Might/Deku y los **«Recipro»** de Tenya **no se
  traducen** ✅.
- **All Might mete palabras en inglés en japonés; en el doblaje TODO va
  traducido** ✅ (confirma lo que ya sospechaba la biblia, ahora con la
  wiki citada literal, no un resumen).
- **«One For All: Full Cowl» → «One For All: A todo motor»** en la serie,
  pero **en la película *Dos héroes* se adaptó distinto: «One For All:
  Flujo total»** ✅. Dato nuevo: la biblia sólo tenía el de la serie.
- «Howitzer Impact» (Bakugo) → «**Impacto Howitzer**» ✅.
- El equipo de villanos **«Reservoir Dogs»** se adaptó como **«Perros de
  la calle»**, conservando el guiño a la película de Tarantino ✅.
- La técnica de Mirio **«Phantom Menace»** → **«Amenaza fantasma»**,
  conservando el guiño a *Star Wars* Episodio I ✅.
- **Gentle Criminal habla con acento marcado de España** en el doblaje: se
  contrató primero a un actor de Barcelona (rechazó por temas de sindicato,
  igual que otros tres actores españoles contactados, entre ellos Claudio
  Serrano); al final lo hizo **Alejandro Graue desde Argentina**, imitando
  el acento ✅. Anécdota rara, sirve para el punto 12 (curiosidad de fans).
- Mirko dice **«¿Qué hay de nuevo, viejo?»** (chiste de Bugs Bunny) en el
  ep. 114 porque su don es de conejo; **pasa lo mismo en el doblaje en
  inglés** ✅ (ya lo tenía la biblia con otra fuente; ahora esto lo
  confirma con cita literal).
- «Shie Hassaikai» se deja sin traducir **toda la serie, salvo el capítulo
  75**, donde los subtítulos de Netflix lo tradujeron una vez como «Las 8
  varas del hassai» ✅. Sirve para el punto 12 «qué no hacer»: no lo
  traduzcas, y si lo haces, hazlo siempre igual (aquí ni el propio doblaje
  fue consistente).

### Curiosidades del reparto (para el punto 12/22, no sólo el 8)

- **Hawks es el único del elenco principal doblado siempre por actores
  mexicanos** en las 4 producciones latinas (2 películas, la serie y la
  versión niño) ✅.
- **Actores que también hicieron un fandub de la serie**: en 2018,
  **Judith Noguera** (voz oficial de Toru Hagakure, Mei Hatsume, Nana
  Shimura) y **Eder La Barrera** (2.ª voz de Yosetsu Awase) participaron
  en un *fandub* interpretando a **Mina Ashido** y **Tenya Iida**
  respectivamente ✅. En 2020, **Pato Hitch** y **Sofía Baltazar** (2.ª
  voz de Uraraka) hicieron el *fandub* de la primera película: él como
  Izuku, ella como Melissa Shield, Momo y Tsuyu ✅. **Esto es oro para el
  punto 22**: la comunidad de fans y el elenco oficial se mezclan.
- Antes de que Funimation eligiera The Kitchen, hubo **demos de casting**
  en Venezuela (Caja de Ruidos/VSI), México (dos estudios), Argentina y
  Chile, con otros repartos completos ✅ (ya resumido en `datos-voz.md`).

## Punto 12 · Lo que ama el fandom, y qué NO hacer

Confirmo/amplío lo que ya tenía la sección 14 de la biblia (8 ⚠️: la
mayoría son correctos, sólo les faltaba una 2.ª fuente o el fotograma).

- **Deku confunde su propio don**: en el ep. 5 lo llama por error **«All
  For One»** en vez de «One For All» (el nombre del villano principal) ✅
  (Doblaje Wiki, «Datos de interés», directo de la wikitext). Chiste que
  el fandom conoce y que un fan notaría si lo usas mal en un texto.
- El error de traducción de «Shie Hassaikai» (capítulo 75 en Netflix, ver
  arriba) es justo el tipo de cosa que **un fan de doblaje notaría**: la
  regla es «no lo traduzcas nunca», y hasta el propio doblaje se saltó su
  regla una vez ✅.
- **Qué NO hacer, confirmado con 2.ª fuente**:
  - **Quirk = Don** ✅ (antes ⚠️, ahora con la wikitext literal).
  - **U.A. se lee «u-a», no «yuei»** ✅ (antes ⚠️, ídem).
  - **Kacchan no se traduce** ✅ (antes ⚠️, ídem).
  - Los alias de héroe/villano casi nunca se traducen (excepción: Trece y
    Tigre) — dato nuevo para no inventar una traducción de un nombre de
    héroe que no la tiene.
- La cicatriz de Todoroki y la traición de la madre (ver el clip de
  arriba) son territorio muy sensible para el fandom: **no lo conviertas
  en chiste** ⚠️ (de mi lectura del fandom, no tengo una fuente única que
  lo diga así explícitamente, pero el tono de los hilos de Reddit sobre
  la familia Todoroki en `datos-voz.md` apoya esto).
- Sigue en pie del repaso anterior (ya con ✅, no lo repito entero):
  Todoroki al revés (pelo blanco a la derecha), All Might sin sombras de
  cómic, Bakugo sonriendo dulce, Deku sin zapatillas rojas, Aizawa
  enérgico, mezclar los dos doblajes latinos (serie vs. películas 1-2),
  llamar «Kacchan» a Bakugo mismo.

## Punto 13 · Los personajes, a fondo (carácter, cómo se expresan, su cara en cada emoción)

Además de lo que ya tenía la sección 8 de la biblia (que está bien, sólo
le faltaba profundidad y fotogramas reales), añado:

### Perfil oficial (*databook*, tomo 1-2, vía la wiki en inglés — antes la biblia sólo tenía AniList)

- **Izuku**: «tímido, educado, reacciona con expresiones exageradas»;
  **diseñado a propósito para verse “plano”** (el propio Horikoshi lo dice
  en su perfil del tomo 1) ✅. Va madurando tras entrar a U.A. y enfrentar
  a Katsuki.
- **All Might**: sonríe siempre porque su mentora, **Nana Shimura, le
  enseñó que “los que sonríen son los más fuertes”** ✅ — explica por qué
  la sonrisa es su gesto obligatorio, no un tic cualquiera. Al volver a su
  forma real se pone serio y evita la atención: es todo lo contrario del
  héroe.
- **Bakugo**: iba a ser un personaje **amable** en el primer boceto;
  Horikoshi lo cambió a «desagradable» porque le pareció aburrido ✅.
- **Todoroki**: su ficha *Ultra Analysis* lo describe como **«un idiota
  frío y caliente» (cool and hot airhead)** ✅ — frase literal, sirve para
  el punto 17 (vocabulario para IA de texto).
- **Uraraka**: sus reacciones son «exageradas y graciosas, se ríe y trata
  de contenerlo»; Horikoshi la describe como **«honesta»** ✅.
- **Aizawa**: su ficha *Ultra Analysis* lo llama **«en el fondo, muy
  consentidor» (actually kind of doting)** una vez decide cuidar de
  alguien ✅. Dato extra: es **bebedor social y se pone “dormilón”
  cuando bebe** (confunde objetos con personas) ✅ — demasiado para la
  lámina, pero útil para diálogos de IA de texto en tono informal.

### Cara y cuerpo en cada emoción — con fotograma y minuto REALES (visto con Read, no de memoria)

| Personaje | Emoción | Escena | Minuto y enlace | Qué se ve |
|---|---|---|---|---|
| **Izuku** | **Miedo** | Villano Muscular ataca en el campamento | [0:08](https://www.dailymotion.com/video/x7xksc8?t=8) | Ojos muy abiertos, boca abierta, junto a Kota, girado hacia el peligro |
| **Izuku** | **Rabia / fuera de control** | El mismo combate, tras activar su don al límite | [0:56](https://www.dailymotion.com/video/x7xksc8?t=56) | Sonrisa torcida, **ojo derecho inyectado en rojo/rosa**, mirada de loco: es el «Deku berserker» que tanto cita el fandom |
| **All Might** (musculoso) | **Alivio / calidez** al salvar a Izuku | Villano Limo, origen | [0:12](https://www.dailymotion.com/video/x618t31?t=12) | Sonrisa enorme, luz de cerezos detrás, pecho hacia adelante |
| **All Might** (flaco) | **Ternura / consejo** | «Puedes ser un héroe», callejón | [2:43](https://www.dailymotion.com/video/x7xktih?t=163) | A contraluz del atardecer, silueta, mano en el hombro de Izuku (se intuye) |
| **Rei Todoroki** | **Angustia / colapso** | Recuerdo antes de quemar a Shoto | [0:20](https://www.dailymotion.com/video/x7xkvbk?t=20) | De espaldas junto a la tetera, pelo blanco suelto, hombros caídos |
| **Bakugo** | **Rabia pura** | Discusión con Deku tras el Villano Limo | [0:17](https://www.dailymotion.com/video/x7xktih?t=17) | Primer plano muy cerrado, un ojo en sombra, boca abierta enseñando los dientes, luz amarilla a contraluz: **la cara de Bakugo más repetida por el fandom** en memes |
| **Shoto Todoroki** (niño) | **Rabia / esfuerzo** | Entrenando con su don a la fuerza | [1:00](https://www.dailymotion.com/video/x7xkvbk?t=60) | Dientes apretados, cejas bajas, primer plano cerrado |
| **Shoto Todoroki** | **Determinación** | Usa el fuego por primera vez ante Bakugo (Festival Deportivo) | [2:40](https://www.dailymotion.com/video/x7xkvbk?t=160) | Mitad de la cara iluminada por el fuego, ceja fruncida, mirada fija; dice «**Yo también quiero ser un héroe**» ([min. 2:36-2:42](https://www.dailymotion.com/video/x7xkvbk?t=156), doblaje latino, oído con `voz.py`) |

(De los 6 personajes del encargo, me quedaron **Uraraka y Aizawa sin un
fotograma nuevo mirado por mí** en esta tanda —los clips de Dailymotion
que encontré no los muestran de cerca—; siguen con la descripción «de
memoria ⚠️» que ya tenía la sección 8 de la biblia. Tampoco cubrí
tristeza ni vergüenza en ningún personaje: son las emociones menos
representadas en escenas de acción/doblaje cortas.)

## Punto 20 · Gustos y detalles de cada personaje (de fichas oficiales)

Todo de los perfiles **oficiales de los tomos 1 y 2** (sección *Omake* del
manga, citados en la wiki en inglés con la referencia al tomo exacto) ✅,
cruzado con AniList (que ya tenía `datos-voz.md` para altura/cumpleaños):

| Personaje | Comida favorita | Afición / le gusta | Cumpleaños | Altura | Sangre | Cómo se ve a sí mismo / detalle |
|---|---|---|---|---|---|---|
| **Izuku Midoriya** | **Katsudon** ✅ | anotar todo en cuadernos | 15 de julio | 166 cm | O | diseñado a propósito «plano»; alumno n.º 18 de 1-A |
| **Katsuki Bakugo** | **Cualquier cosa picante** ✅ | **escalar montañas** ✅ | 20 de abril | 172 cm | A | alumno n.º 17; 1.º en el examen de ingreso |
| **Shoto Todoroki** | **Soba fría (zaru soba)** ✅ | — | 11 de enero | 176 cm | O | alumno n.º 15; el más nominado del Festival Deportivo |
| **Ochaco Uraraka** | **Comida japonesa, sobre todo mochi** ✅ | mirar el cielo estrellado ✅ | 27 de diciembre | 156 cm | B | Horikoshi: «orgulloso del nombre que le puso» |
| **Shota Aizawa** | — | **le gustan los gatos** ✅ (ya lo tenía la biblia) | 8 de noviembre | 183 cm | B | bebedor social, «dormilón» borracho; cuarto vacío = su apatía |
| **All Might / Toshinori Yagi** | — | **películas y los cedros de Yakushima** ✅ | 10 de junio | 220 cm | A | el tono del móvil es un juego con su propia frase |

**Para la lámina**: el dato más usable es el de **Deku y el Katsudon**
(el mismo plato que come Naruto-tipo protagonistas shonen: buen gancho de
comida en un cuaderno o pizarra) y **Bakugo escalador** (poco conocido,
rompe el estereotipo de que sólo pelea).

## Punto 21 · Por qué la gente la ama

- **+100 millones de copias del manga vendidas en el mundo** ✅
  ([Kotaku ES, 2025](https://es.kotaku.com/un-record-para-la-eternidad-my-hero-academia-es-oficialmente-el-anime-mas-grande-del-mundo-en-2025-2000034070)).
- **Premios**: 7 premios en los **2.ª Crunchyroll Anime Awards** ✅; **Anime
  del Año** en la **10.ª edición (2026)** ✅
  ([Akibastation](https://www.akibastation.es/2026/05/ganadores-crunchyroll-anime-awards-2026.html),
  [Vandal](https://vandal.elespanol.com/random/my-hero-academia-conquista-los-anime-awards-2026-arrasa-como-mejor-serie-del-ano-y-solo-leveling-no-decepciona/42235.html));
  **Mejor manga que los extranjeros deberían leer**, Sugoi Japan Awards
  2017 ⚠️ (un resumen de búsqueda, no vi la fuente original).
- **Con qué personaje se identifica el público latino, con datos reales**:
  el desglose regional del World Best Hero (punto 7) pone a **Kirishima en
  3.er lugar en Latinoamérica**, dos puestos por delante de su posición
  mundial (5.º) ✅. Es un dato concreto y propio de esta región: el
  público latino valora más de lo normal a un secundario «buena onda, sin
  dobleces», justo lo opuesto al antihéroe.
- **Razones generales que dan los fans** (resumen de varias listas de
  «por qué lo aman», [Talk with Donuts](https://talkwithdonuts.com/14-reasons-why-fans-love-my-hero-academia-boku-no-hero-academia-part-1/)
  y otras) ⚠️ (fuente única, artículo de fans, no oficial): el mensaje de
  que **no hace falta un don para ayudar a alguien**; el elenco enorme
  tratado con el mismo cariño; identificarse con Izuku por ser «el que no
  tiene poder» al principio; el sistema de dones **con límites y
  contras**, no un solo protagonista que resuelve todo.

### Escenas que hacen llorar (capítulo, minuto, por qué, cómo está filmada)

| Escena | Dónde | Por qué duele | Cómo está filmada | Fuente |
|---|---|---|---|---|
| **«Puedes ser un héroe»** | Arco de origen (ep. 1-2) | Es la frase que decide toda la vida de Izuku: el único adulto que le dice que sí puede | Contraluz de atardecer, silueta, cerezos, plano bajo mirando hacia arriba a All Might | vista y oída, [min. 2:43](https://www.dailymotion.com/video/x7xktih?t=163) ✅ |
| **El colapso de Rei Todoroki** | Arco de Todoroki (flashback) | Explica la cicatriz y el trauma familiar de Shoto: una madre que se rompe y no puede más | Vista de espaldas en la cocina, luz fría, ella sola en el encuadre | vista y oída, [min. 0:20](https://www.dailymotion.com/video/x7xkvbk?t=20) ✅ |
| **Kota y «alguien que será un héroe»** | Arco del campamento (Deku vs. Muscular) | Cierra el arco de un niño que odiaba a los héroes por la muerte de sus padres | Voz en off sobre el combate, tono grave y lento | oída, [min. 3:54](https://www.dailymotion.com/video/x7xksc8?t=234) ✅ |
| **«Papa All Might» y el bento en el suelo** | Un panel del manga (no identifiqué el capítulo exacto) | All Might cuidando a Izuku como un padre | Es una imagen fija (panel), no supe ubicar el capítulo | Reddit, 1279 votos, 44 comentarios, ya en `datos-voz.md` ⚠️ (no confirmé el capítulo) |

**La música de estas escenas concretas**: no encontré el nombre de un
tema de fondo específico para ninguna de las tres primeras (son escenas
con diálogo/voz en off, no un tema instrumental identificable a oído) ⚠️.
Lo que sí está confirmado (sección 11 de la biblia, no es mi punto pero lo
cito): **«You Say Run»** es el tema del esfuerzo al límite, y las T1/T8
comparten banda para el opening (Porno Graffitti) como un cierre de
círculo.

## Punto 22 · Fan dubs y comunidad hispana

- **Canales dedicados a fandub en español**: **«My Hero Academia Fandub
  Castellano»** (canal propio en YouTube) y **«EL MEJOR FANDUB LATINO DE
  BOKU NO HERO ACADEMIA»** ⚠️ (los vi en resultados de búsqueda, no pude
  abrir YouTube para ver vistas/suscriptores por el bloqueo de este
  servidor).
- **Fandubs de escenas concretas** (todos en YouTube, sólo el título, sin
  poder ver métricas por el bloqueo) ⚠️: *Two Heroes* (llegada a la
  fiesta), Deku vs. Shinso, personaje Tsuyu Asui, personaje Jiro Kyoka,
  tráiler de *World Heroes Mission*, capítulo 1 completo.
- **Lo mejor encontrado — actores OFICIALES metidos en fandubs** (ver
  arriba, punto 8): Judith Noguera + Eder La Barrera (2018, fandub de la
  serie) y Pato Hitch + Sofía Baltazar (2020, fandub de la primera
  película) ✅ (Doblaje Wiki, sección «Curiosidades»). Es un puente único
  entre el doblaje oficial y el fandom: para un servidor de doblaje como
  Sintonizando, es el dato más útil de todo mi punto 22.
- **Covers de los openings/endings en español latino** (YouTube, títulos
  vistos en el buscador, mismo bloqueo) ⚠️:
  - «THE DAY» (opening 1) y varios más, recopilados en una lista:
    [playlist «Boku no Hero Academia Openings & Endings (Español
    Latino)»](https://www.youtube.com/playlist?list=PL4yrZkKNACAePPw06zjJrXz1KMPram_L0).
  - **David Delgado** tiene varios covers propios: «Hitamuki» (OP10),
    «Bokurano» (OP11), «No.1» (OP8).
  - «Kekka Orai» (opening de *Vigilantes*) por **@0uter**.
- **Parodias y memes en TikTok, en español**: cuentas con contenido de
  humor/ediciones de MHA como **@konamysan** y **@yerastian** ⚠️ (fuente
  única, sin vistas ni fecha: sólo aparecen en el buscador, no pude abrir
  TikTok para confirmar).
- El engagement de Reddit (hilos «best scene», votos y comentarios) **ya
  está en `datos-voz.md`**, no lo repito aquí.

## Lo mejor para la lámina

- **«Puedes ser un héroe»**, con la silueta a contraluz del atardecer
  (min. 2:43 del clip citado): es la frase y la imagen que de verdad
  cambia a Izuku, perfecta para un cuaderno o pizarra del canal.
- **Aizawa es el profesor más querido de verdad** (4.º histórico, top 5
  en Latinoamérica, muy por delante de All Might): la lámina de
  #material-de-clase gana más pegándose a él que a All Might.
- **Bakugo profesor invitado + Deku profesor** siguen siendo la pareja
  más fuerte: Bakugo es el 1.º en TODAS las encuestas desde la 2.ª, y en
  Latinoamérica specifically el n.º 1 regional.
- El dato de **Kirishima 3.º en Latinoamérica** (vs. 5.º mundial) es un
  gancho de identificación regional que ninguna otra biblia de esta serie
  va a tener si no se usa aquí.
- **Judith Noguera y Sofía Baltazar haciendo fandub** con la comunidad:
  para un servidor de doblaje, es el ejemplo perfecto de «los actores de
  verdad también son fans».

## No encontré

- ⚠️ Vistas/suscriptores de los canales de fandub y covers en español: **YouTube
  pide iniciar sesión** en este servidor (lo dice el aviso de arranque);
  probé `yt-dlp` directo y dio «Sign in to confirm you're not a bot» /
  429. Quedan como enlaces de texto de la búsqueda, sin métricas.
- ⚠️ El capítulo exacto del panel «Papa All Might con el bento en el
  suelo» (Reddit, 1279 votos): es una imagen suelta, no un vídeo con
  minuto; busqué «Papa All Might bento» y variantes, no until un capítulo.
- ⚠️ Metrics de las cuentas de TikTok de parodias (@konamysan,
  @yerastian): TikTok no se pudo abrir directamente; sólo tengo el
  nombre por el resultado del buscador.
- ⚠️ Nombre de un tema musical específico para las 3 escenas que hacen
  llorar de mi tabla del punto 21 (son diálogo/voz en off, no un tema
  instrumental reconocible a oído).
- Esto **no es un extra que falte por hacer**: son huecos reales del
  bloqueo del servidor o de que la fuente simplemente no da más (imagen
  suelta de Reddit sin metadatos de capítulo).

## Bitácora de búsqueda (esta pasada)

- Doblaje Wiki, API `action=parse&prop=wikitext`, página `My_Hero_Academia`
  completa (114 268 caracteres) y `My_Hero_Academia/8ª_temporada`
  (45 581 caracteres): leídas enteras con Python, no de memoria.
- Fandom en inglés (`myheroacademia.fandom.com`), API wikitext, páginas
  completas de Izuku Midoriya, Toshinori Yagi, Katsuki Bakugo, Shoto
  Todoroki, Ochaco Uraraka y Shota Aizawa (secciones Infobox y Trivia), y
  la página `Popularity_Polls` completa (102 464 caracteres).
- Dailymotion: API de búsqueda (`api.dailymotion.com/videos?search=…`) en
  español, «My Hero Academia All Might latino», «My Hero Academia Bakugo
  latino doblaje»; 4 vídeos procesados con `voz.py` (transcripción) y
  `fotogramas.py` (hojas de contacto, miradas con Read):
  `x618t31` (All Might, Villano Limo), `x7xktih` («Puedes ser un héroe» +
  pelea Deku/Bakugo + cara de rabia de Bakugo), `x7xksc8` (Deku vs.
  Muscular, ya en datos), `x7xkvbk` (Rei Todoroki + Shoto usando el fuego
  por primera vez, con su frase «Yo también quiero ser un héroe»). Borré
  los `video.mp4` de las 4 carpetas después de sacar las hojas (disco
  compartido).
- Reddit vía Arctic Shift (`arctic-shift.photon-reddit.com`), búsqueda
  «Papa All Might» en r/BokuNoHeroAcademia.
- Buscador web (en español e inglés, cupo usado: 6 de ~50): fandub español
  latino MHA, cover opening MHA español latino, doblaje T8 Samuel Lazcano
  ANMTV, por qué la gente ama MHA, ventas/premios MHA, Andrea Villaverde
  Uraraka IMDb/BTVA, parodias/memes MHA tiktok español.
- `behindthevoiceactors.com`: **403** al abrir directo (2 intentos);
  usado el resultado del buscador como cita, tal como indica AYUDANTE.md.
- YouTube directo (`yt-dlp`): **bloqueado** («sign in to confirm you're
  not a bot», 429), como avisa el mensaje de arranque. Todo el vídeo real
  lo saqué de Dailymotion en su lugar.
