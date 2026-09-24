# Investigación de VÍDEO · Pokémon (07-pok-mon)

Rol de `EQUIPO.md`: puntos **2, 4, 9, 10 y 14** de `ENCARGO.md` (fotogramas de
escenas icónicas, sitios/luz/paleta, música, vídeos con minuto, y poses por
personaje). La biblia ya traía estos puntos escritos (primera pasada, red
cerrada): las escenas venían de un **subtítulo no oficial** de la película
*¡Yo te elijo!* (2017) y el capítulo 1 real **no se había mirado**. Parto de
`partes/datos-video.md` (Dailymotion, Internet Archive, MusicBrainz) y no
repito esas consultas: busco lo que falta, miro los vídeos de verdad y
confirmo o corrijo cada ⚠️.

**YouTube pidió iniciar sesión** en este contenedor (varios ayudantes con la
misma IP), así que todo lo de abajo es de **Dailymotion** e **Internet
Archive**, tal como permite `AYUDANTE.md`.

**Hallazgo principal**: en Internet Archive está el **episodio 1 real y
completo** en inglés, doblaje oficial de 4Kids
(`archive.org/details/pokemon-indigo-league-season-1-1998`, archivo
`[AnimeRG] Pokémon - 0001 - Pokémon, I Choose You [Di [480p] [x265] [pseudo].mp4`,
1342 s). Usé el truco de **recortar por rango HTTP con ffmpeg** (`-ss` antes
de `-i` sobre la URL directa) para sacar sólo los minutos que hacían falta,
sin bajar los 97 MB del episodio completo (dos recortes, 6 min y 4 min, 24 s
y 17 s de red cada uno). Sobre esos recortes locales corrí
`fotogramas.py --cortes` (un fotograma por plano) y miré las hojas. Esto da
**minutos reales, verificados por mí viendo el episodio**, no un subtítulo de
fans de la película. La numeración de "minuto real" de esta sección es
`90 + segundo del recorte` (recorte 1: laboratorio) y `960 + segundo del
recorte` (recorte 2: Spearow/Ho-Oh) sobre el metraje del episodio 1 en inglés
(4Kids). El doblaje latino puede tener cortes de 2-5 s distintos (créditos,
"la Pokébola cuenta la historia" en España/LatAm quita/pone segundos): lo dejo
marcado como **episodio 1, minuto aproximado del tramo**, no al segundo exacto
del doblaje latino (verificar el minuto latino exacto es del rol de voz).

---

## 2 · Fotogramas de escenas icónicas, con capítulo y minuto (mirados)

### 2.1 Escena 1 · El laboratorio de Oak — Episodio 1, real (inglés, 4Kids) ✅
Mirado fotograma a fotograma con `fotogramas.py --cortes` sobre el recorte de
Internet Archive (90–450 s del episodio). Corrige y AMPLÍA lo que la biblia
tenía de un subtítulo no oficial de la película:

| Minuto real (ep. 1, inglés) | Qué pasa | Fuente |
|---|---|---|
| **≈4:00** | Ash duerme con un **reloj Voltorb con un Pidgey de cuco**; lo rompe dormido, sin querer, poco después de las 4 AM | visto + ✅ [Bulbapedia EP001, Trivia](https://bulbapedia.bulbagarden.net/wiki/EP001): «Ash has a Voltorb clock with a cuckoo Pidgey in it... he ends up breaking it in his sleep» |
| **≈4:42** | Ash llega tarde: otros niños ya se van del laboratorio con su Pokémon (uno de ellos es **Gary**, medallón *yin-yang*, puño en alto, presumiendo) | visto (fotograma en grande, ver abajo) |
| **≈5:56** | **Tres Pokébolas sobre soportes en TRIÁNGULO, con un hueco vacío en el centro** (confirma la descripción ya escrita en la biblia, esta vez vista en el episodio real, no en la película remake) | visto, fotograma en grande |
| **≈6:03–6:24** | Oak abre las Pokébolas una a una: **vacías** (Squirtle, Bulbasaur, Charmander ya se los llevaron) | visto |
| **≈6:48–6:52** | La Pokébola del centro (con **un rayo pintado**, se ve en detalle) se abre con un **flash dorado** | visto |
| **≈6:58** | Sale **Pikachu**, algo arisco, apoyado en la mesa | visto, fotograma en grande (ver `estilo_pikachu2`) |
| **≈7:04–7:12** | Pikachu descarga a Ash cuando lo toca | visto |
| **≈7:18** | Ash abraza a Pikachu, **los dos chamuscados y echando humo**, Oak los mira serio de fondo | visto, fotograma en grande |
| ⚠️ orden exacto Squirtle→Bulbasaur→Charmander | Confirmado por Bulbapedia (no por mí viendo el orden letra por letra, las pokébolas vacías se ven muy rápido) | ✅ [Bulbapedia EP001](https://bulbapedia.bulbagarden.net/wiki/EP001): «Squirtle first, Bulbasaur second, and Charmander last» |
| ✅ **Es el único capítulo donde se ve a Pikachu dentro de su Pokébola** | la biblia ya lo decía con ⚠️ (una fuente); ahora **dos fuentes** | ✅ [Bulbapedia EP001, Trivia](https://bulbapedia.bulbagarden.net/wiki/EP001) + WikiDex (ya citada) |
| Dato nuevo: la apertura del episodio (combate Gengar/Nidorino/Onix que Ash ve por TV) **imita el intro de Pokémon Rojo/Verde** (mismo combate Gengar vs Nidorino de la demo del juego) | ✅ [Bulbapedia EP001, Trivia](https://bulbapedia.bulbagarden.net/wiki/EP001) |

Fotogramas en grande (mirados con Read, no sólo la hoja de contacto):
`/tmp/claude-0/trabajo/07-pok-mon-video/ep1_frames/fotograma_00266.jpg` (las
tres Pokébolas), `fotograma_00328.jpg` (Pikachu), `fotograma_00348.jpg`
(el abrazo con Oak de fondo), `fotograma_00219.jpg` (Gary presumiendo).
⚠️ Cada Pokébola lleva una etiqueta en **katakana grabada en el plástico**
(se ve en `fotograma_00266.jpg`); a la resolución del archivo (480p, vídeo de
1997) está borrosa y **no la pude leer con certeza** — no invento el texto.

### 2.2 Escena 2 · Los Spearow y Ho-Oh — mismo episodio 1, real ✅
Segundo recorte (960–1200 s) con el mismo método. Es **la escena más citada
de todo el anime** y no estaba en la biblia:

| Minuto real | Qué pasa |
|---|---|
| ≈16:02 | Ash conoce a **Misty**, pescando en un río |
| ≈16:57 | Pikachu va **dormido en la cesta de la bici** de Misty (que Ash toma prestada) |
| ≈17:16–17:19 | Una bandada de **Spearow** ataca; Pikachu los repele con un rayo, pero un Spearow le devuelve el golpe y lo hiere |
| ≈17:37–17:52 | Ash intenta meter a Pikachu (herido) en su Pokébola para protegerlo; Pikachu **se niega otra vez** |
| ≈18:03–18:23 | Ash corre bajo la lluvia cargando a Pikachu; al final **se para y abre los brazos** de cara a la bandada, para protegerlo con su cuerpo (pose de sacrificio/entrega, útil para "proteger, animar") |
| ≈18:28–19:39 | Aparece una silueta gigante entre el aguacero (dorada/marrón por el contraluz) que ahuyenta a los Spearow; sale un **arcoíris** y el ave se aleja volando por encima de él |
| ≈19:58 | Ash y Pikachu, ya a salvo, se miran contentos: nace la amistad |

- ✅ **El ave es Ho-Oh**, confirmado por fuente primaria:
  [Bulbapedia EP001](https://bulbapedia.bulbagarden.net/wiki/EP001) lo lista
  en "Pokémon debuts": «Ho-Oh (anime)». Es la **primera aparición de Ho-Oh en
  cualquier medio Pokémon** (antes de Oro/Plata, que lo revelarían como
  mascota de esa generación) ⚠️ (dato de trivia muy repetido en la comunidad,
  sólo una fuente primaria abierta esta vez: Bulbapedia no da fecha
  comparativa con el lanzamiento del juego en su extracto).
- Fotogramas en grande: `ep1_hoOh/fotograma_00143.jpg` (Ash de espaldas,
  brazos abiertos, bandada encima) y `fotograma_00219.jpg` (Ho-Oh bajo el
  arcoíris).
- Hoja completa de planos (76 fotogramas, un fotograma por plano):
  `/tmp/claude-0/trabajo/07-pok-mon-video/ep1_spearow/hoja_01.jpg` y `hoja_02.jpg`.

### 2.3 Escena 3 · El lema del Equipo Rocket (compilación, Dailymotion) ✅
[`Lema Team Rocket`](https://www.dailymotion.com/video/xs14pe), 35 s. Mirado
completo con `fotogramas.py --cortes` (8 planos). Pose fija que se repite
capítulo tras capítulo: **Jessie y James de pie en silueta contra un fondo
que gira** (remolino de estrellas), brazo en alto, luego primer plano de cada
cara con gesto exagerado, cierre con **Meowth riendo a cámara**. Útil para
"presentar en grupo" y para la tipografía del logo "R" en el uniforme (ya en
`partes/texto.md`, punto 6).
⚠️ No identifiqué el idioma exacto del doblaje de este clip en concreto (sin
diálogo con texto en pantalla que lo confirme); verificar el actor/frase con
el rol de voz.

### 2.4 Otras escenas ya en la biblia (repaso)
- **Ash se da la vuelta la gorra**: seguí sin encontrar un clip limpio.
  Probé `yt-dlp` sobre el enlace de TikTok de la biblia
  (`fandamncollectibles/video/7318016739621571882`): **falla la extracción**
  (TikTok pide "impersonation", no disponible aquí). Probé también la API de
  búsqueda de Dailymotion ("ash cap backwards pokemon"): sin resultado
  limpio. Sigue con ⚠️, como ya estaba.
- **El final de Ash (2023, JN147)**: no hay clip oficial accesible sin
  YouTube; se deja como estaba (enlace a Bulbapedia).

---

## 4 · Sitios, luz y paleta — colores medidos sobre fotograma real (nuevo)

La biblia ya tenía la paleta de Pueblo Paleta y el laboratorio **medida del
código** de los juegos (`pret/pokered`) y del arte oficial (PokéAPI). Lo que
faltaba —y es lo que pide `AYUDANTE.md`— es medir sobre **un fotograma del
anime realmente visto**, para comparar:

- **Pikachu, medido con `estilo.py` sobre el fotograma 00328 del episodio 1**
  (recorte de sólo el cuerpo, sin fondo): paleta dominante **`#CAA62D`**
  (54%, amarillo cuerpo) · `#C8A527` (línea/sombra) · `#9C502A` (mejillas y
  la franja del lomo, un marrón rojizo más apagado que el "rojo" de las
  mejillas del arte oficial) · contorno `#322822`. Sombreado: **plano (cel)**,
  saturación 69%, brillo 70% ✅ (medido por mí,
  `/tmp/claude-0/trabajo/07-pok-mon-video/estilo_pikachu2/estilo.json`).
  Es **más apagado y amarronado** que el amarillo `#FEE200` del render HOME
  ya medido en la biblia (5.3): la cinta de 1997/VHS y la compresión del
  archivo bajan saturación; para la lámina, el HOME sigue siendo la
  referencia (más parecida al anime actual), y este tono es la referencia
  "anime clásico, cinta vieja" si se quiere ese aire retro.
- **La tormenta de los Spearow, medida sobre el fotograma 00143 (Ash de
  espaldas, brazos abiertos)**: paleta de noche-tormenta, azules oscuros
  `#222D35` · `#27363F` · `#2C424F` · `#324B65`, con un verde-azulado
  `#3F6E6E` de acento (los árboles a contraluz) ✅ (medido,
  `estilo_ash_escudo/estilo.json`). Sombreado degradado/pintado (fondo
  pintado a mano, no cel), saturación 43%, brillo 32%: es la escena más
  oscura y "pintada" de las que miré, útil si la lámina quiere un momento
  dramático de lluvia en vez de la luz de día de costumbre.
- **Confirmación visual del laboratorio (punto 5.2 de la biblia)**: en el
  episodio real se ve la sala circular con las Pokébolas en soportes y luz
  azulada de laboratorio (no cálida) entrando por una claraboya — coincide
  con "luz de día, fluorescentes" que la biblia ya marcaba con ⚠️ (de
  memoria); ahora es ✅ **visto**, aunque sigue sin verse el molino de viento
  exterior en los planos de este episodio en concreto (los planos del
  exterior son del camino de subida, no de la fachada) — el molino queda
  ⚠️ (una fuente, Bulbapedia/Pallet Town Wiki, no lo vi en este episodio).
- **Gary y su grupo de porristas**, fotograma 00219: colores del uniforme de
  Gary en el episodio 1 — jersey/camisa **azul marino** `#2E3A8C`-ish (no
  medido con la herramienta, a ojo sobre el fotograma) con medallón
  yin-yang verde/amarillo; el uniforme verde con corbata amarilla del niño a
  su lado (uno de los otros 3 entrenadores). Dato nuevo para vestuario de
  personajes secundarios del episodio 1 (no estaba en la biblia).

---

## 9 · Música — confirmaciones nuevas (Doblaje Wiki, fuente primaria)

La biblia daba **Óscar Roa** como cantante latino de "¡Atrápalos ya!" con
⚠️ (una fuente débil, artículos de prensa). Lo busqué en la página propia del
actor en Doblaje Wiki (API, wikitext) y en la ficha musical de la serie:

- ✅ **Óscar Roa** (tenor lírico mexicano, Tehuacán, Puebla) **sí** cantó el
  tema de apertura en el doblaje latino de Pokémon
  ([Doblaje Wiki, ficha de Óscar Roa](https://doblaje.fandom.com/es/wiki/%C3%93scar_Roa):
  «interpretó algunos temas en el doblaje de Pokémon, entre ellos la
  conocida primera apertura Pokémon Theme»), confirmado también en
  ([Doblaje Wiki, Pokémon/Música](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon/M%C3%BAsica),
  tabla de aperturas: Óscar Roa, temporada 1.ª, episodios 1-83). **Sube a
  ✅** (dos fuentes de Doblaje Wiki + la prensa que ya tenía la biblia).
- **Letrista/adaptador y dirección musical del doblaje latino**: **Adolfo
  Aguirre Gamboa** y **Jorge Roig** ✅ ([Doblaje Wiki, Pokémon/Música](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon/M%C3%BAsica)).
  Estudio de grabación de las canciones: **Audiomaster 3000** ✅ (misma
  fuente).
- **Segunda apertura latina, "Mundo Pokémon"** (episodios 84-116): cantante
  original en inglés Russell Velázquez, versión latina cantada por
  **Rodrigo Zea** ✅ (misma fuente, tabla de aperturas). Dato nuevo, no
  estaba en la biblia.
- **Letra completa verificada de "¡Atrápalos ya!" en español** (para citar
  textual en la lámina o en futuras piezas, tildes y ¿¡ comprobados
  visualmente en el wikitext): *"Tengo que ser siempre el mejor, / mejor que
  nadie más... / Atraparlos mi prueba es, / entrenarlos mi ideal... [...]
  ¡Pokémon! / Atrápalos ya, / ¡Atrápalos ya! / ¡Pokémon!"* ✅
  ([Doblaje Wiki, Pokémon/Música](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon/M%C3%BAsica)).
- **Los cierres (endings) casi nunca se doblaron al español**: la propia
  Doblaje Wiki lo dice de frente: *"Generalmente los cierres no son doblados
  al inglés y por ende tampoco al español"* ✅ (misma fuente). Esto explica
  por qué el único clip de ending que encontré con texto en español
  (`x3urahi`) es un **vídeo de fans con la letra traducida sobre ilustraciones
  fijas**, no la animación oficial doblada — lo dejo anotado en el punto 10
  para que no se use como si fuera dub oficial.
- **Segmentos musicales post-episodio** (dato nuevo, no estaba en la
  biblia): además del **Pokérap** (150 Pokémon repartidos en 5 versiones,
  emitido tras los primeros 52 episodios) estaba **"La Rockola de Pikachu"**
  (Pikachu's Jukebox), fragmentos de canciones del álbum *¡Para ser un
  Maestro!*, y en la 3.ª temporada **"Pokémon Karaokémon"**, videoclips de un
  minuto con las canciones de *The Johto Journeys* ✅
  ([Doblaje Wiki, Pokémon/Música](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon/M%C3%BAsica)).
  Sirve como referencia de "cápsula musical corta" si el servidor quiere un
  formato parecido para anuncios del canal.
- El resto del punto 9 (Junichi Masuda, Shinji Miyazaki, arreglo de Ray
  Chen) ya estaba bien y con fuente: no lo repito aquí, sigue en la biblia.

---

## 10 · Vídeos mirados, con minuto (opening, ending, tráiler)

| Vídeo | Sitio | Duración | Qué se ve | Minuto de lo que sirve |
|---|---|---|---|---|
| [**Opening**, «Pokémon - Opening»](https://www.dailymotion.com/video/x88osgb) | Dailymotion (canal Sensacine) | 61 s | Etapa **Kanto-Johto** (el vídeo no dice cuál apertura exacta): planeta y galaxia, Ash de perfil, Growlithe corriendo con un niño, Charmander bebé, Raichu saltando junto a Pikachu, una mano abriendo una Pokébola con un flash, Ash y Misty con mochila viendo Pokémon pequeños a lo lejos, Charizard volando, Pikachu haciendo un salto con chispas, logo "Pokémon" en amarillo con contorno azul | mirado completo, 21 fotogramas cada 3 s |
| [**Ending**, «Friends to the End»](https://www.dailymotion.com/video/x2sqtay) | Dailymotion | 3:50 | Éste sí es **animación oficial de TV** (no un vídeo de fans): Ash con la **gorra de la Liga Pokémon** (visera verde, distinta a la roja de siempre), primeros planos de Ash y Pikachu, el profesor Oak, un combate con Onix/Poliwrath-tipo y Weezing/Grimer, el estadio de la Liga Índigo | mirado completo, 29 fotogramas cada 8 s; usar minutos 0:56-1:28 para poses de Ash con Pikachu en brazos |
| ⚠️ «Peace Smile», con subs español | [Dailymotion](https://www.dailymotion.com/video/x3urahi) | 4:08 | **No es la animación oficial**: es un vídeo de fans (créditos "Cristy P.R." al final) con **ilustraciones fijas** (algunas parecen arte oficial de XY&Z, otras son fan art) sobre la canción, letra en rōmaji + traducción al español. Sirve para la **letra traducida**, no como referencia de animación de un ending real | mirado completo, 25 fotogramas cada 10 s |
| [**Tráiler**, «Pokémon Rojo / Pokémon Azul»](https://www.dailymotion.com/video/x84bzwf) | Dailymotion (canal 3djuegos) | 2:23 | Tráiler oficial en **español de España** de los juegos de Game Boy: pantallas reales del juego dentro de un marco promocional. Dice **"¡Hola a todos! ¡Bienvenidos al mundo de POKéMON!"** (0:12), Oak: **"¡Ven conmigo!"** (0:18) y **"se quedan 3. Te daré uno. ¿Cuál..."** (0:24). El combate de ejemplo usa **"ASH"** como nombre del jugador y **PIKACHU** como su primer Pokémon (1:00) — encaja directo con el tema de #autoroles (elegir tu inicial) | mirado completo, 24 fotogramas cada 6 s |
| [«Lema Team Rocket»](https://www.dailymotion.com/video/xs14pe) | Dailymotion | 35 s | Ver punto 2.3 | mirado completo, 8 planos |
| Episodio 1 completo (inglés, 4Kids) | [Internet Archive](https://archive.org/details/pokemon-indigo-league-season-1-1998) | 22:23 | Ver puntos 2.1 y 2.2 | recortes 1:30-7:30 y 16:00-20:00 mirados fotograma a fotograma |

**Tendencia de TikTok** ("¿qué inicial eliges?"): sigue igual que en la
biblia, no encontré nada nuevo que verificar con vídeo directo (TikTok no se
deja extraer aquí, ver 2.4).

---

## 14 · Poses analizadas — con capítulo, minuto real y fotograma (nuevo/ampliado)

Todo lo de abajo es del **episodio 1, doblaje inglés, Internet Archive**
(minuto real = mirado por mí, no de un subtítulo). Añade a la tabla de poses
que ya tenía la biblia (que usaba minutos de la película remake, sin
verificar):

### Profesor Oak
| # | Minuto real (ep. 1) | Qué hace | Sirve para |
|---|---|---|---|
| 1 | ≈6:09-6:31 | de pie junto a Ash, bata blanca, corbata roja, explicando con gesto de mano | **explicar** |
| 2 | ≈7:18 | serio, brazos cruzados/quieto, mirando a Ash y Pikachu chamuscados de fondo | **regañar sin palabras** (cara de "te lo dije") — fotograma en grande: `ep1_frames/fotograma_00348.jpg` |

### Ash
| # | Minuto real (ep. 1) | Qué hace | Sirve para |
|---|---|---|---|
| 1 | ≈6:58-7:12 | sorprendido, luego adolorido (Pikachu lo descarga) | **sorpresa/dolor cómico** |
| 2 | ≈7:18 | abraza a Pikachu, pelo chamuscado, ojos en blanco de humo | **celebrar a pesar de todo**, humor |
| 3 | ≈18:23 | **de espaldas, brazos totalmente abiertos**, bajo la lluvia, protegiendo a Pikachu de la bandada de Spearow | **proteger/entregarse** — la pose más fuerte que vi, útil para un concepto de lámina "el mentor cubre a su aprendiz" — fotograma en grande: `ep1_hoOh/fotograma_00143.jpg` |
| 4 | ≈19:58 | de pie, sonriendo, mirando a Pikachu ya a salvo | **alegría tranquila**, cierre de escena |

### Pikachu
| # | Minuto real (ep. 1) | Qué hace | Sirve para |
|---|---|---|---|
| 1 | ≈6:58 | de pie sobre la mesa del laboratorio, algo arisco, mejillas con chispas | **presentarse**, desconfianza — fotograma en grande: `ep1_frames/fotograma_00328.jpg` |
| 2 | ≈16:57 | dormido, hecho bolita en la cesta de la bici | **descansar/acompañar** |
| 3 | ≈17:16-17:19 | de pie, mejillas brillando, lanza un rayo contra los Spearow | **defender**, acción |
| 4 | ≈17:37-17:52 | herido, tumbado, se resiste a la Pokébola con la pata | **negarse, terquedad** (ya estaba apuntado en la biblia con la escena de la película; ahora hay una segunda escena, distinta, que confirma que es un rasgo repetido del personaje) |

### Gary Oak (secundario; no estaba en la tabla de poses de la biblia)
| # | Minuto real (ep. 1) | Qué hace | Sirve para |
|---|---|---|---|
| 1 | ≈5:09 | puño en alto, sonrisa amplia, medallón yin-yang al cuello, sus porristas detrás | **presumir/celebrar** — fotograma en grande: `ep1_frames/fotograma_00219.jpg`. Dato para el dueño: Gary es el rival "de fábrica" del juego (su nombre por defecto en Rojo/Azul es **GARY**, visto también en el tráiler del punto 10) — si el canal #autoroles quiere un segundo personaje además de Ash/Oak, Gary es una opción con arte e imagen propios. |

---

## Lo mejor para la lámina

1. **Ash con los brazos abiertos bajo la lluvia protegiendo a Pikachu**
   (ep. 1, ≈18:23) es la pose más fuerte y menos usada de todo lo que se
   suele ver de Pokémon: mentor/entrenador que se sacrifica por su
   compañero. Muy distinta a la típica "Ash con el puño en alto".
2. El **tráiler oficial de Rojo/Azul en español** ya usa **"ASH" y
   "PIKACHU"** como nombre de jugador/inicial en su propia demo (minuto
   1:00): es la prueba más directa de que el vínculo Ash-Pikachu-inicial es
   oficial y no sólo del anime, perfecto para el "elige tu inicial" de
   #autoroles.
3. Las **tres Pokébolas en soporte triangular con hueco en el centro**,
   vistas en el episodio real (≈5:56), confirman de forma independiente el
   concepto ya propuesto en la biblia (la mesa del laboratorio con las
   Pokébolas = elegir tu rol).

## No encontré
- ⚠️ **El gesto de Ash girándose la gorra** en un clip limpio: TikTok no se
  deja extraer aquí (ver 2.4) y Dailymotion no tiene un clip dedicado. Sigue
  como en la biblia, con las mismas fuentes de antes.
- ⚠️ **El molino de viento del laboratorio** no aparece en los planos
  exteriores del episodio 1 que miré (sólo se ve el camino de subida). Sigue
  con la fuente de la wiki (Bulbapedia/Pallet Town Wiki), no confirmado por
  vídeo.
- ⚠️ **Fondos de pantalla oficiales en alta** de Pueblo Paleta/laboratorio:
  seguí sin encontrarlos (mismo resultado que la primera pasada).
- El texto grabado en katakana sobre cada Pokébola del laboratorio (episodio
  1, ≈5:56): visible pero **demasiado borroso para leerlo** con certeza; no
  lo transcribo para no inventar.

## Bitácora de búsqueda (vídeo, esta pasada)
- **Internet Archive, por su API de metadatos** (`archive.org/metadata/…`):
  confirmé el archivo de vídeo real del episodio 1 dentro de la colección ya
  lista en `datos-video.md`.
- **HTTP Range + ffmpeg** (truco de otro repaso): `curl -sI` confirmó
  `accept-ranges: bytes`; extraje dos recortes (`-ss` antes de `-i`, 6 min y
  4 min) en 24 s y 17 s de red respectivamente, sin bajar los 97 MB
  completos. Los `.mp4` de recorte y los `video.mp4` que bajó
  `fotogramas.py` para cada clip de Dailymotion quedan en
  `/tmp/claude-0/trabajo/07-pok-mon-video/` (fuera del repositorio); los
  borro al terminar esta tanda.
- **`fotogramas.py --cortes`** (detección de plano) sobre los dos recortes
  del episodio 1: 94 y 76 fotogramas. **`fotogramas.py --cada N`** sobre
  cuatro clips de Dailymotion (opening, ending oficial, ending de fans,
  tráiler) y **`--cortes`** sobre el lema del Rocket.
- **`estilo.py`**: paleta y tipo de sombreado en 4 fotogramas (Pikachu
  recortado, Pikachu completo, Ash bajo la lluvia, Ash+Oak del abrazo).
- **Dailymotion, por su API pública** (`api.dailymotion.com/videos?search=`,
  no gasta cupo de buscador): «team rocket lema pokemon» (encontró el clip
  usado), «ash cap backwards pokemon» (sin resultado útil), y confirmé con
  `yt-dlp -j` el título/duración exacta de cada clip antes de procesarlo.
- **`yt-dlp` sobre TikTok** (el enlace ya citado en la biblia): falla la
  extracción («Unexpected response», impersonation no disponible). Un solo
  intento, como marca el límite de `AYUDANTE.md`; no insistí más.
- **AnimeThemes** (`api.animethemes.moe`): sigue caída, error 522, igual que
  cuando la corrió `recolectar.py` (ya anotado en `datos-video.md`). No hay
  `.webm` de openings/endings disponible por ahí en esta tanda.
- **Bulbapedia, por su API** (`action=query&prop=extracts`, sin curl directo
  a la web normal): funcionó sin bloqueo esta vez (`EP001` — ficha completa
  del episodio 1, con blurb, lista de debuts y trivia). Esto **contradice**
  lo que la primera pasada de `texto.md` anotó ("Bulbapedia da 403 todo el
  repaso"): puede que el bloqueo sea intermitente o por endpoint (la API con
  `format=json` sí respondió, la web normal no la probé). Aviso para el
  siguiente investigador que la necesite: probar la API antes de descartarla.
- **Doblaje Wiki, por su API** (`action=parse&prop=wikitext`): páginas
  `Óscar_Roa` y `Pokémon/Música` completas, ambas con datos nuevos no
  usados en la primera pasada.
- **No usé buscador web (WebSearch)** en esta tanda: todo salió de APIs
  directas (Dailymotion, Internet Archive, Bulbapedia, Doblaje Wiki) y de
  mirar los vídeos. Cupo de ~50 búsquedas sin tocar, disponible para quien
  siga.

Sigue: nada obligatorio pendiente de los puntos 2, 4, 9, 10 y 14. Si hay
tiempo/tanda extra: reintentar el gesto de la gorra de Ash con otra fuente
(Internet Archive tiene episodios de Kanto sueltos por si aparece en uno con
la escena completa), y buscar el molino de viento del laboratorio en otro
episodio con exterior más amplio.
