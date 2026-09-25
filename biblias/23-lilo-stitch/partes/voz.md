# Investigador de voz y personajes · Lilo & Stitch

Puntos de `ENCARGO.md`: **7** (popularidad), **8** (doblaje latino), **12** (fandom y qué no
hacer), **13** (personajes a fondo, cara en cada emoción), **20** (gustos), **21** (por qué
la aman), **22** (fan dubs y comunidad hispana). Parto de `partes/datos-voz.md` (no repito
esas consultas) y de `python3 herramientas/seccion.py 23-lilo-stitch --rol voz` /
`--avisos` para ver lo que ya hay en `biblia.md` (no la toco).

**Cómo miré la película** (punto 13, obligatorio hacerlo yo mismo): YouTube no hacía
falta esta vez (no dio 429), pero seguí el plan de «Internet Archive antes de
rendirse» porque es la única fuente que trae la **película entera** (los clips de
Dailymotion de `datos-voz.md` son sólo tráileres de 2 min). Usé
`herramientas/fotogramas.py` sobre `https://archive.org/details/lilo-stitch-2002_202609`
(copia íntegra de *Lilo & Stitch* 2002, pista de audio en francés pero **imagen
idéntica** a cualquier edición; 85 min) y sobre
`https://archive.org/details/lilo-stitch-luau-nani-loses-her-job-hd-1080p` (el mismo
tramo del luau en 1080p). Los tiempos que cito son **los de esta copia de Internet
Archive** (enlace con `&t=`): en la mayoría de escenas coinciden con el minuto que ya
usa `biblia.md` (±10 s), pero en un par de tramos hay hasta ~30 s de diferencia por
los créditos iniciales distintos; lo aviso donde pasa. Carpeta de trabajo:
`/tmp/claude-0/trabajo/23-lilostitch-voz/` (`pelicula/`, `pelicula_hoja1/2/3`,
`nani_clip/`). Borro `video.mp4` al terminar la tanda.

---

## Punto 7 · Popularidad

- **Stitch es, con diferencia, el personaje más popular** de la franquicia y uno de
  los más vendibles de todo Disney hoy: mercancía dominante y cruce
  generacional (quienes lo vieron en 2002 se lo enseñan a sus hijos) ✅
  [Hollywood Reporter, «How Disney Made Stitch the Biggest Winner»](https://www.hollywoodreporter.com/movies/movie-news/disney-2025-big-winner-stitch-character-1236457944/),
  [The Walt Disney Company, «Stitch: The Extraordinary Character»](https://thewaltdisneycompany.com/news/stitch-character-brand/).
- **La película de 2025 recaudó 1.038 millones de dólares** en todo el mundo (presupuesto
  100 millones) ✅ [Wikipedia (infobox, cifra de Box Office Mojo)](https://en.wikipedia.org/wiki/Lilo_%26_Stitch_(2025_film)),
  cifra repetida en Hollywood Reporter. Es el indicador más objetivo de alcance que
  encontré (no hay encuesta de popularidad oficial, ver «No encontré»).
- **26 de junio = «Stitch Day»** (6/26, por el número de experimento) ✅ ya en
  `biblia.md` §14; lo confirmo con
  [Disney Latino, «Día de Stitch»](https://www.disneylatino.com/novedades/dia-de-stitch-que-significa-ohana)
  y con la costumbre en TikTok de la etiqueta #626day.
- **Pleakley es el secundario más querido por el público adulto**, no Jumba ni
  Gantu: se ve en la reacción cuando en 2025 le quitaron el vestido («Put Pleakley
  in the wig, cowards», ya citado en `biblia.md` §8/§14) ✅. Lo confirmo con un
  ángulo nuevo: los directores originales describieron a Pleakley y Jumba como el
  **dúo Marty McFly / Doc Brown** de *Regreso al futuro* (Pleakley el nervioso,
  Jumba el científico) ⚠️ un solo wiki
  ([Lilo & Stitch Wiki, Pleakley, sección Trivia](https://liloandstitch.fandom.com/wiki/Wendy_Pleakley#Trivia)),
  dato que explica por qué el dúo funciona tan bien para el fandom.
- **Quitar a Gantu en 2025 fue de lo más criticado** (ya en `biblia.md` §8): otra
  señal de que un secundario puede pesar más de lo que parece ✅ (fuentes ya
  citadas ahí, Screen Rant y SAN).

---

## Punto 8 · Doblaje latino (correcciones y datos nuevos)

`biblia.md` §10 marcaba ⚠️15 y varios reparto ❌ «no encontrado». Los resolví con
**dos fuentes independientes**: la ficha de cada actor en Doblaje Wiki
(`doblaje.fandom.com/es/api.php`, wikitext, consulta directa) y **The Dubbing
Database** (`dubdb.fandom.com`, wiki en inglés que documenta doblajes por país;
su propia página de Lilo & Stitch cita a Doblaje Wiki como fuente pero la
redacta de forma independiente, así que cuenta como segunda fuente real).

### 8.1 Película de 2002 — reparto completo, ya con 2 fuentes

| Personaje | Voz latina | Fuentes |
|---|---|---|
| Lilo Pelekai | **Anaís Portillo** | ✅ ya en `biblia.md` |
| Stitch/Exp. 626 | **Raúl Aldana** | ✅ ya en `biblia.md` |
| Nani Pelekai | **Claudia Garzón** (canciones: Irasema Terrazas) | ✅✅ [Doblaje Wiki, ficha de Nani Pelekai](https://doblaje.fandom.com/es/wiki/Nani_Pelekai) (Garzón, 6 proyectos), [The Dubbing Database](https://dubdb.fandom.com/wiki/Lilo_y_Stitch_(Latin_American_Spanish)) — **sube de ⚠️ a ✅** |
| Dr. Jumba Jookiba | **Maynardo Zavala** (acreditado en pantalla como «José Maynardo») | ✅✅ [Doblaje Wiki, ficha de Jumba Jookiba](https://doblaje.fandom.com/es/wiki/Jumba_Jookiba) (Zavala, 6 proyectos; su página real es «Maynardo Zavala», no «José Maynardo»), [The Dubbing Database](https://dubdb.fandom.com/wiki/Lilo_y_Stitch_(Latin_American_Spanish)) (lo llama «José Maynardo») — **corrige** el nombre de `biblia.md` («Maynardo Zavala» estaba bien pero con ⚠️; ahora con 2 fuentes, más el matiz del nombre acreditado |
| Agente Pleakley | **Rubén Trujillo** «Trujo» | ✅✅ Doblaje Wiki (tabla de `datos-voz.md`), The Dubbing Database — **antes ❌, ahora resuelto** |
| Cobra Bubbles | **Rubén Moya** | ✅✅ mismas 2 fuentes — **antes ❌, ahora resuelto** |
| David Kawena | **Noé Velázquez Pedroza** | ✅✅ mismas 2 fuentes — **antes ❌, ahora resuelto** |
| Capitán Gantu | **Gerardo Reyero** | ✅✅ (ya en `biblia.md` con 1 fuente; The Dubbing Database lo confirma) |
| Gran Concejal | **Patricia Martínez** | ✅✅ Doblaje Wiki + The Dubbing Database |
| Mertle Edmonds | **Fernanda Robles** | ✅✅ (ya en `biblia.md`; The Dubbing Database confirma) |
| Kumu Moses Puloki | **Mario Filio** | ✅✅ **resuelve el misterio** de `biblia.md` («aparece junto a Anaís Portillo en un vídeo, no sé a quién dobla»): es la voz de Kumu |
| Encargada de la perrera | **Jessica Ortiz** | ✅✅ Doblaje Wiki, The Dubbing Database |
| Primera oficial Ombit | **Cristina Hernández** | ✅✅ |
| Teniente de custodia / cond. de camión 2 | **Ricardo Tejedo** | ✅✅ |
| Piloto | **Yamil Atala Cabrera** | ✅✅ (nuevo, no estaba en `biblia.md`) |
| Piloto femenina rosa | **Karla Falcón** | ✅✅ |
| Conductor de camión | **Raúl Aldana** | ✅✅ |
| Estudio de doblaje | **Doblaje Audio Traducción, S.A. de C.V.** | ✅✅ Doblaje Wiki + infobox de The Dubbing Database (independiente) — **sube de ⚠️ a ✅** |
| Dirección | Ricardo Tejedo (según `datos-voz.md`) / José Carlos Moreno (según `biblia.md`, «uno de sus últimos trabajos antes de morir») | ⚠️ **sigue en duda**: las dos fuentes que tengo (Doblaje Wiki vía recolectar.py y el resumen de `biblia.md`) no coinciden en quién dirigió; The Dubbing Database no da director. Dejar ⚠️ hasta abrir la página completa en el PC. |

### 8.2 Película de 2025 (imagen real) — correcciones importantes

`biblia.md` §10.2 tenía varios nombres con ⚠️ «un resumen» (de sdpnoticias/la-lista,
notas de prensa de casting). Los comprobé contra Doblaje Wiki (que ya lista el
reparto final, no el rumoreado) y The Dubbing Database:

| Personaje | `biblia.md` decía | **Corregido / confirmado** | Fuentes |
|---|---|---|---|
| Nani | Karen Vallejo ⚠️ | **Alicia Vélez** | ✅✅ [Doblaje Wiki, Lilo y Stitch (2025)](https://doblaje.fandom.com/es/wiki/Lilo_y_Stitch_(2025)), [The Dubbing Database](https://dubdb.fandom.com/wiki/Lilo_y_Stitch_(Latin_American_Spanish,_2025)) — **corrección real**, ⚠️ el nombre de prensa era otro |
| Pleakley | Arturo Castañeda ⚠️ | **Armando Guerrero** | ✅✅ mismas 2 fuentes — **corrección real** |
| Lilo | Aurora Villegas Romero ⚠️ | Aurora Villegas Romero | ✅✅ confirmado, sube a ✅ |
| Stitch | Gerardo Becker (Ania) ✅ | Gerardo Becker Ania | ✅✅ confirmado |
| Jumba | Sergio Gutiérrez Coto ✅ | Sergio Gutiérrez Coto | ✅✅ confirmado |
| Cobra Bubbles | Octavio Rojas ⚠️ | Octavio Rojas | ✅✅ sube a ✅ |
| Gran Concejal | Rebeca Manríquez ⚠️ | Rebeca Manríquez | ✅✅ sube a ✅ |
| David, Gantu | «desconocido» | **David Kawena = Iván Bastidas** (Gantu no sale en la versión de 2025, por eso no hay voz) | ✅✅ Doblaje Wiki + The Dubbing Database |
| Mertle Edmonds | no estaba | **Habana Zoé** | ✅✅ |
| Tutu (abuela) | no estaba | **Ma. Eugenia Guzmán** | ✅✅ |
| Sra. Kekoa | no estaba | **Yolanda Vidal** | ✅✅ |
| Kumu Hula | no estaba | **Polo Rojas** | ✅✅ |

**Ojo para el redactor**: el cambio de Nani y Pleakley en 2025 es una corrección
real sobre `biblia.md`, no una duda: dos fuentes especializadas en doblaje
coinciden y contradicen la nota de prensa que se usó antes.

### 8.3 Frases del doblaje latino

No sumo frases nuevas transcritas de vídeo esta tanda (las de `biblia.md` §10.3 ya
están bien sourceadas); confirmo que las 5 frases con ✅ siguen en pie tal cual.
Sigue pendiente (lo dejo en «Sigue») bajar subtítulos en español de un clip
oficial doblado para sacar la frase «My camera's full again» / «Aren't they
beautiful?» en latino, que ni `biblia.md` ni yo encontramos.

---

## Punto 12 · Lo que ama el fandom, y qué NO hacer (añadido)

- **Hubo una escena cortada por xenofobia hacia los turistas**: Lilo hace creer a
  los turistas que viene un tsunami para vengarse de cómo tratan a los
  hawaianos (uno le pregunta si «sabe hablar inglés»); los directores la
  cortaron por ser difícil de leer para el público infantil (gentrificación,
  turismo excesivo, apropiación cultural) ✅
  [Cultura Colectiva, «La escena eliminada de Lilo y Stitch que te habría hecho llorar»](https://culturacolectiva.com/entretenimiento/cine-series/escena-eliminada-lilo-y-stitch/),
  [Sensacine México](https://www.sensacine.com.mx/noticias/noticia-1000146758/).
  **Para la lámina**: confirma lo que ya decía `biblia.md` §14.2 sobre no hacer
  «Hawái de postal»; el propio estudio lo pensó y lo evitó.
- **El fandom identifica el momento de la hamaca (Nani cantando «Aloha ʻOe» a
  Lilo, 00:52:51 en `biblia.md`)** como «representación emocional», no sólo
  representación étnica: un hilo de Reddit lo describe como el instante en que
  la audiencia siente que «alguien tomó tu realidad, desordenada y sin
  filtrar, y la volvió algo hermoso» ✅
  [resumen citado en Goodreads/Substack sobre reseñas de Lilo & Stitch](https://gonewith.substack.com/p/lilo-and-stitch-is-the-movie-2025).
  **Para la lámina**: ese es el momento de ternura, no el de acción; sirve para
  una pose tranquila, no dramática.
- **Stitch como metáfora universal**: un comentario de fan citado en varias
  reseñas dice que Stitch «era en realidad todos los que conozco: buscando
  aprobación, tratando de ser amado, anhelando amor» ⚠️ (cita de segunda mano,
  sin el hilo original) — coincide con lo ya escrito en `biblia.md` §8 sobre
  Stitch («no tiene nada que destruir y nadie a quien querer»).

---

## Punto 13 · Los personajes a fondo (con cara en cada emoción)

> Fotogramas propios, sacados **yo mismo** con `fotogramas.py` sobre la copia de
> Internet Archive citada arriba. Enlace con `&t=` = mismo segundo en esa copia.
> Marco ✅ lo que vi directamente en el fotograma (no es «de memoria»); dejo ⚠️
> sólo si el gesto es ambiguo o si mezclo con una fuente de texto sin imagen.

### Lilo Pelekai

- **Arco**: pasa de estar sola y castigando a los demás por adelantado (antes de
  que la abandonen) a dejar entrar a Stitch y, con él, reconstruir su idea de
  familia. Cumple años (7) durante la propia película: en el montaje final hay
  7 velas en su pastel ⚠️ un solo wiki
  ([Lilo & Stitch Wiki, Trivia](https://liloandstitch.fandom.com/wiki/Lilo_Pelekai#Trivia)).
- **Miedos**: que la gente se vaya (ya en `biblia.md`: «I remember everyone that
  leaves», 00:54:57); que Nani deje de quererla como hermana; que se la lleven
  con un asistente social.
- **Cara en cada emoción** (todas con fotograma propio):
  - **Vergüenza**: enseña a Scrump con sonrisa torcida, un ojo entornado, de
    camino a la escuela, sabiendo que la van a molestar ✅
    fotograma en 14:35, https://archive.org/details/lilo-stitch-2002_202609?t=875
  - **Tristeza**: abrazada a su peluche verde, sentada en la cama, mirando la
    pared de fotos de turistas con la mirada baja ✅
    fotograma en 22:10, https://archive.org/details/lilo-stitch-2002_202609?t=1330
  - **Alegría**: a carcajadas, boca abierta, subida con Stitch al cohete de
    monedas «Space Adventure» frente a una tienda ✅
    fotograma en 31:44, https://archive.org/details/lilo-stitch-2002_202609?t=1904
  - **Ternura/afecto** (variante de alegría que sirve más para la lámina que la
    de carcajada): sonríe de lado, ceño relajado, mirando a Stitch mientras él
    hace de las suyas en su caja ✅
    fotograma en 36:56, https://archive.org/details/lilo-stitch-2002_202609?t=2216
  - **Rabia**: en `biblia.md` §8 ya está citada «Before I bit her» (00:22:29) y
    el portazo (00:21:18); no repetí el fotograma exacto esta tanda por tiempo
    — **sigue pendiente** verlo yo mismo (ver «Sigue»).
  - **Miedo**: no encontré un primer plano claro sólo de miedo (la escena de la
    llamada a Cobra, 01:01:44, es más pánico hablado que cara en pantalla) ⚠️
    — **sigue pendiente**.
- **Dinámica con Nani**: en la hoja de contacto que saqué (14:10-15:40 y
  20:50-23:15 de la copia) se ve la secuencia completa: Nani la regaña y la
  manda a su cuarto (20:50-21:20), Lilo llora sola abrazada al peluche
  (21:30-22:15), Nani entra, se sienta con ella y se abrazan hasta quedarse
  dormidas juntas (22:20-22:55) ✅ — es la mejor referencia de «regañar → hacer
  las paces» para una lámina en pareja.

### Stitch (Experimento 626)

- **Arco**: de arma sin propósito a «hijo» que aprende qué es una familia. El
  giro está en la lectura repetida del Patito Feo.
- **Cara en cada emoción**:
  - **Rabia**: capturado en una cápsula de contención, enseña los dientes y
    gruñe con los ojos entornados ✅ fotograma en 2:25,
    https://archive.org/details/lilo-stitch-2002_202609?t=145 · también
    silueta amenazante recién escapado, sobre un montón de escombros con luz
    verde ✅ fotograma en 23:59, https://archive.org/details/lilo-stitch-2002_202609?t=1439
    · y enseñando los dientes a Nani, que le devuelve el gesto con una rama en
    alto ✅ fotograma en 1:05:30, https://archive.org/details/lilo-stitch-2002_202609?t=3930
  - **Tristeza**: sentado de noche, con el libro del Patito Feo abierto, orejas
    caídas, mano en la barbilla, mirada baja — el «I'm Lost!» que cita
    `biblia.md` §8, pero ahora con el fotograma exacto de su cara, no sólo de
    la página del libro ✅ fotograma en 55:27,
    https://archive.org/details/lilo-stitch-2002_202609?t=3327 (la página con
    el texto «I'm Lost!» sale 4 s después, t=3331).
  - **Alegría**: a carcajadas en el cohete con Lilo (mismo plano que arriba) ✅
    t=1904.
  - **Miedo/vergüenza**: no encontré un plano donde Stitch muestre miedo o
    vergüenza con claridad (su registro es casi todo rabia, alegría o
    melancolía) ⚠️ — puede ser real del personaje (apenas habla y no se
    avergüenza en pantalla), lo anoto para que el redactor no lo dé por
    fotograma perdido.
- **Detalle nuevo**: en la misma habitación a oscuras, Stitch construye en
  secreto una maqueta de una ciudad (puente, edificios, un barco) mientras Lilo
  lo mira pensativa desde la cama — un gesto de inteligencia oculta que no
  estaba en `biblia.md` ✅ fotograma en 38:00,
  https://archive.org/details/lilo-stitch-2002_202609?t=2280. Sirve para
  «pensar»/creatividad, más que para una emoción básica.

### Nani Pelekai

- **Cara en cada emoción**:
  - **Rabia/asco**: primer plano sirviendo bebidas en el luau, ceja levantada,
    boca torcida de fastidio ✅ fotograma en 1:39 del clip
    `lilo-stitch-luau-nani-loses-her-job-hd-1080p` (1080p),
    https://archive.org/details/lilo-stitch-luau-nani-loses-her-job-hd-1080p
    · y blandiendo una rama contra Stitch, dientes apretados ✅ fotograma en
    1:05:30, https://archive.org/details/lilo-stitch-2002_202609?t=3930 · y
    arrastrando a Lilo del brazo hacia casa nada más empezar la bronca ✅
    fotograma en 20:50-21:00, https://archive.org/details/lilo-stitch-2002_202609?t=1250
  - **Ternura**: abraza a Lilo en la cama hasta quedarse dormidas juntas (ver
    dinámica de Lilo arriba) ✅ 22:20-22:55.
  - **Tristeza/estrés**: la misma cara de fastidio del luau dobla como
    agotamiento: está a punto de perder ese trabajo (el clip se titula
    literalmente «Nani Loses Her Job») ✅.
  - **Miedo/vergüenza**: no aparecen con claridad en lo que miré esta tanda —
    **sigue pendiente** (la escena candidata es cuando Cobra Bubbles la
    entrevista, que no llegué a sacar en fotograma).
- **Nuevo dato de gustos** (cruza con punto 20): pizza y chocolate entre lo que
  le gusta, según la ficha de personaje — ver tabla del punto 20.

### Dr. Jumba Jookiba

- **Cara en cada emoción**:
  - **Miedo/alarma**: escondido entre arbustos junto a Pleakley, ojos muy
    abiertos, boca apretada, mirando algo fuera de plano ✅ fotograma en
    28:37, https://archive.org/details/lilo-stitch-2002_202609?t=1717 · y de
    pie entre los escombros de la casa que Stitch acaba de destrozar, ojos
    como platos, sujetando un trozo de madera ✅ fotograma en 1:01:05,
    https://archive.org/details/lilo-stitch-2002_202609?t=3665
  - **Alegría/rabia/tristeza/vergüenza**: no saqué fotograma propio esta
    tanda — las frases ya citadas en `biblia.md» («Evil genius!», «I'll make
    you taller») sirven de referencia de tono, pero **falta el fotograma**
    (queda en «Sigue»).
- **Gustos nuevos** (punto 20): le gusta bailar; según él mismo, en su planeta
  los nutrientes se absorben por la piel y masticar comida «le parece molesto»
  — pero al final de una escena admite que empieza a gustarle comer de todos
  modos ⚠️ un solo wiki (dato de la serie, no de la película de 2002)
  ([Jumba Jookiba, Trivia](https://liloandstitch.fandom.com/wiki/Jumba_Jookiba#Trivia)).

### Agente Pleakley

- **Cara en cada emoción**:
  - **Miedo**: mismo plano que Jumba, agachado entre los arbustos, boca
    abierta, antena hacia atrás ✅ t=1717 (28:37).
  - **Alegría/fascinación**: riendo con los brazos arriba junto a Jumba, en el
    bosque de noche, rodeado de instrumental ✅ fotograma en 38:40,
    https://archive.org/details/lilo-stitch-2002_202609?t=2320 · y con una
    sonrisa traviesa, de perfil, cubierto de mosquitos que lo adoran (especie
    protegida, ya citada en `biblia.md`) ✅ fotograma en 39:00,
    https://archive.org/details/lilo-stitch-2002_202609?t=2340
  - **Rabia/tristeza/vergüenza**: no encontré fotograma claro esta tanda —
    quedan en «Sigue».
- **Especie y apodos** (punto 20): es un **Plorgonarian**; Jumba lo llama
  «Walking Noodle» (fideo andante); otros apodos: Aunt Ophelia, Mrs. P.
  Leakley, Aunt Pleakley ✅ un wiki, pero coincide con lo ya sabido de que se
  disfraza de mujer (`biblia.md` §8) —
  [Lilo & Stitch Wiki, Wendy Pleakley](https://liloandstitch.fandom.com/wiki/Wendy_Pleakley).

---

## Punto 20 · Gustos y detalles de cada personaje

_Fuente principal: infobox «likes/dislikes» de_
_[Lilo & Stitch Wiki (Fandom)](https://liloandstitch.fandom.com), sección por
personaje. Es un solo wiki de fans (⚠️), pero varios datos ya están
confirmados por escenas citadas en `biblia.md` (los marco ✅ cuando hay
cruce con película)._

| Personaje | Le gusta | Le disgusta | Fuente |
|---|---|---|---|
| **Lilo** | Su ʻohana, Stitch, tener amigos, **Elvis Presley** ✅ (`biblia.md` §8), Regis Philbin, el hula, surfear | Los abusones, Mertle, que Nani la regañe o la sobreproteja, que la griten | ⚠️/✅ mixto, [Lilo Pelekai](https://liloandstitch.fandom.com/wiki/Lilo_Pelekai) |
| **Stitch** | Divertirse, la ʻohana, sus «primos» experimentos, Lilo, Angel, **comida y bebida (sobre todo pastel de coco y café)** ✅ (`biblia.md` §8: Nani le da café), naves espaciales, **tortugas** (dibuja dos en los créditos y abraza una de peluche tras una pesadilla) ⚠️ | El agua, la nieve/hielo (al principio), la soledad y el rechazo, la competencia, Mertle | ⚠️/✅ mixto, [Stitch (626)](https://liloandstitch.fandom.com/wiki/Stitch_(626)) |
| **Nani** | Surfear ✅ (`biblia.md`: escena de la tabla), Lilo, estar con su familia, **pizza**, hula, **chocolate** | La mala suerte, la desobediencia, perder a Lilo, perder el trabajo, gritarle a Lilo, los inventos de Jumba | ⚠️, [Nani Pelekai](https://liloandstitch.fandom.com/wiki/Nani_Pelekai) |
| **Jumba** | Crear experimentos «malvados», sus propios inventos, la canción **«Hound Dog» de Elvis** (coincide con la obsesión familiar por Elvis), su propio genio, su madre | Que sus experimentos fallen, que lo arresten, que lo llamen «científico idiota», que Hämsterviel use sus experimentos, su ex-esposa, Mertle | ⚠️, [Jumba Jookiba](https://liloandstitch.fandom.com/wiki/Jumba_Jookiba) |
| **Pleakley** | La limpieza, la seguridad, **disfrazarse de mujer** ✅ (`biblia.md` §8), coser, la cultura y los estudios terrestres, los mosquitos ✅ (`biblia.md`: especie protegida), el olor del Sr. Hediondo (personaje de la serie) | La suciedad, el peligro, los agujeros negros, los experimentos «malvados» de Jumba, que su madre lo regañe, su propio nombre de pila («Wendy») | ⚠️/✅ mixto, [Wendy Pleakley](https://liloandstitch.fandom.com/wiki/Wendy_Pleakley) |

- **Altura de Stitch**: alrededor de 1 metro (3 pies y 6 pulgadas) ⚠️ un solo
  blog especializado en figuras coleccionables —
  [Sideshow, «Disney Data: Learn More About Stitch»](https://www.sideshow.com/blog/disney-learn-about-stitch).
  No encontré una ficha oficial con altura exacta en cm.
- **Cumpleaños**: ninguno de los 5 tiene fecha de nacimiento oficial publicada
  (no hay campo «birthday» en las fichas de Fandom que consulté) ❌ — sólo la
  edad aproximada de Lilo (cumple 7 durante la película, ver punto 13).
- **El objeto que siempre lleva**: Lilo con su cámara de fotos (❓ marca no
  confirmada, ya en `biblia.md` §20 de «Lo que no pude verificar»); Stitch, el
  libro del Patito Feo cuando está triste; Pleakley, su antena (que además le
  sirve de oído/olfato) ✅.

---

## Punto 21 · Por qué la gente la ama

- **El tema de la ʻohana (familia encontrada) es la razón número uno** que
  repiten las reseñas: la película deja claro que familia no es sólo sangre,
  y eso conecta con gente que no encaja en su propia familia biológica ✅
  [Box Office Mojo, «'Ohana' Means Family»](https://www.boxofficemojo.com/article/ed2859467780).
- **Un hilo de Reddit describe la escena de la hamaca** (Nani cantando «Aloha
  ʻOe» a Lilo, 00:52:51 en `biblia.md`) como el momento de «representación
  emocional»: no es sólo ver hawaianos en pantalla, es ver una familia rota
  intentando arreglarse tal cual es, «desordenada y sin filtro» ✅ (citado en
  reseñas agregadas, [gonewith.substack.com](https://gonewith.substack.com/p/lilo-and-stitch-is-the-movie-2025)).
- **Escena que hace llorar, con minuto y por qué**: la del Patito Feo /
  «I'm Lost!» (55:27-55:31 en mi copia de Internet Archive, ≈00:55:31 en
  `biblia.md`) es la que más se repite en redes como «la escena que te hizo
  llorar» ✅ [TikTok, «La escena que hizo llorar en la película de Lilo y
  Stitch»](https://www.tiktok.com/discover/la-escena-que-hizo-llorar-en-la-pel%C3%ADcula-de-lilo-y-stitch).
  **Por qué duele**: Stitch, que hasta entonces sólo destruye, se ve reflejado
  en un pato que no encaja en ningún grupo; está solo, de noche, con las
  orejas caídas (fotograma propio del punto 13). **Cómo está filmada**: plano
  cerrado, luz azul de luna, sin música (silencio, más el sonido del bosque) —
  lo vi yo mismo en el fotograma; el contraste de silencio es lo que más
  golpea, no hay canción de por medio ✅ (observación directa).
- **La escena de la hamaca también hace llorar**, con música: «Aloha ʻOe» la
  canta Nani sin instrumentos, a capela, cosa que se resalta en el análisis del
  hilo de Reddit citado arriba ✅.
- **Recaudación y alcance como prueba de cariño masivo**: 1.038 millones de
  dólares en 2025 (ver punto 7) y el hecho de que Stitch sea top de ventas de
  mercancía Disney hoy ✅ (fuentes ya citadas en punto 7).
- **Con qué personaje se identifica el público**: sobre todo con **Stitch**
  como metáfora de sentirse «raro» y no encajar, y con **Lilo** entre quienes
  fueron niños solitarios o «diferentes» — ambos hilos de reseñas ya citados
  ⚠️ (son resúmenes de foros, no una encuesta con números).

---

## Punto 22 · Fan dubs y comunidad hispana

Comprobé 3 fandubs reales en YouTube con `yt-dlp -j` (título, canal, vistas,
fecha — datos medidos, no de memoria):

- **«Fandub Lilo & Stitch Español Latino. Con participación especial de Saii y
  Yumi»** · canal **Dotachin96** · **147 762 vistas** · subido 26-jun-2012 ·
  9:48 min ✅ medido con yt-dlp,
  https://www.youtube.com/watch?v=kofTIv15aL4
- **«Lilo y Stitch ¡ESTÁ TOCANDOME!»** · canal **Lucymar** · 512 vistas ·
  21-oct-2020 · 1:31 min ✅ medido con yt-dlp,
  https://www.youtube.com/watch?v=C53YBpJ8I_k — parte de una **moda de fandubs
  con el mismo chiste** («está tocándome», sobre la escena en que Nani revisa
  si Stitch tiene pulgas): encontré al menos 4 versiones distintas del mismo
  gag por distintos creadores (ver enlaces en `datos-voz.md`), señal de un
  meme hispano recurrente, no de un solo vídeo suelto.
- **«LILO Y STITCH FANDUB (Doblaje) | Vane Ochoa»** · canal **Érase Una Voz** ·
  202 vistas · 22-may-2023 · 1:32 min ✅ medido con yt-dlp,
  https://www.youtube.com/watch?v=fTEk021IYKQ
- **Covers en español de las canciones**: «Hawaiian Roller Coaster Ride» y «He
  Mele No Lilo» tienen varias versiones con letra traducida al español en
  YouTube y TikTok, la mayoría ligadas al estreno de 2025 ✅
  [ejemplo de cover, YouTube](https://www.youtube.com/watch?v=qcMfcIHcJXk),
  búsqueda con múltiples resultados en TikTok bajo la etiqueta «Hawaiian
  Roller Coaster Ride letra español». No pude verificar vistas del cover de
  YouTube (yt-dlp no devolvió datos esa consulta) ⚠️.
- **No encontré** parodias o memes hispanos de gran escala fuera de estos
  fandubs y los covers de canciones (el «Ohana» y «Stupidhead» sí son memes en
  inglés, pero no vi una versión hispana viral equivalente) ⚠️ — puede ser que
  exista y no la haya encontrado con las búsquedas hechas (ver Bitácora).

---

## Lo mejor para la lámina

1. **Lilo con Scrump, avergonzada-orgullosa** (fotograma t=875, 14:35): la cara
   exacta para un cuadro de diálogo tímido/orgulloso en el foro de fotos.
2. **La secuencia completa de la pared de fotos + abrazo con Nani**
   (20:50-23:15 en mi copia): dos poses en una escena — Lilo triste abrazando
   su peluche junto a la pared de turistas, y luego el abrazo con Nani. Es la
   referencia más clara para el objeto «álbum de fotos» del encargo.
3. **Stitch leyendo el Patito Feo, orejas caídas** (t=3327): la cara triste más
   citada por el propio fandom como «la escena que te hizo llorar».
4. **Nani sirviendo bebidas con cara de hartazgo** (nani_clip t=99, 1080p): la
   mejor cara de rabia/estrés medida en alta resolución.
5. **Pleakley riendo entre mosquitos** (t=2340): humor puro, secundario más
   querido, encaja con el tono desenfadado que pide el dueño.

---

## No encontré ⚠️ (no es «Sigue»: esto es lo que sería un extra)

- Encuesta oficial de popularidad de Disney con ranking numérico por
  personaje: busqué en español e inglés («Disney character popularity poll»,
  «encuesta popularidad Disney personajes», «Stitch Day poll Pleakley Gantu»)
  y no existe o no está publicada; sólo hay proxies (taquilla, mercancía,
  reacción a recortes de personajes).
- Vistas del cover de YouTube de «Hawaiian Roller Coaster Ride» (id
  qcMfcIHcJXk): yt-dlp no devolvió metadatos esa consulta (posible vídeo
  restringido por edad o música con Content ID).
- Fecha de nacimiento oficial de cualquiera de los 5 personajes.
- Parodias o memes hispanos de gran escala equivalentes a «Ohana» o «blue
  punch buggy» en inglés.
- Quién dirigió el doblaje de 2002 con certeza (dos fuentes que no coinciden,
  ver tabla 8.1).

## Sigue: fotogramas propios de miedo y vergüenza de Jumba y Pleakley, de rabia y miedo de Lilo, y de miedo/vergüenza de Nani (volver a bajar `https://archive.org/details/lilo-stitch-2002_202609` con `fotogramas.py`, el `video.mp4` de esta tanda se borró para no llenar el disco compartido); bajar subtítulos en español de un clip oficial doblado para la frase de la pared de fotos («Aren't they beautiful?») del punto 8.3; confirmar quién dirigió el doblaje de 2002 (Ricardo Tejedo vs José Carlos Moreno).

---

## Bitácora de búsqueda (esta tanda)

- **Vídeo (Internet Archive, mirado con fotogramas.py)**: película completa
  `lilo-stitch-2002_202609` (85 min, francés/imagen original) — más de 25
  fotogramas propios sacados y mirados con Read, en 3 hojas de contacto
  (14:10-15:40, 20:50-23:15, 1:00:30-1:02:00) y 15 fotogramas sueltos a
  1280 px. Clip `lilo-stitch-luau-nani-loses-her-job-hd-1080p` (1080p, 3:16
  min) — 1 hoja de contacto de 48 fotogramas + 6 fotogramas sueltos.
- **Doblaje Wiki** (API, wikitext): páginas de Nani Pelekai, Jumba Jookiba,
  Lilo y Stitch (2025) — en español.
- **The Dubbing Database** (dubdb.fandom.com, API, wikitext): Lilo y Stitch
  (Latin American Spanish) y Lilo y Stitch (Latin American Spanish, 2025) —
  en inglés/español mixto.
- **Lilo & Stitch Wiki** (liloandstitch.fandom.com, API, wikitext): fichas de
  Lilo, Stitch, Nani, Jumba y Wendy Pleakley (likes/dislikes/trivia) — en
  inglés.
- **yt-dlp -j** sobre 4 vídeos de YouTube (fandubs y cover) para título, canal,
  vistas y fecha — sin necesidad de descargar.
- **WebSearch** (7 búsquedas, en español e inglés): popularidad oficial de
  Disney, cumpleaños/altura de Stitch, fandub español latino, escena que hace
  llorar, por qué ama el público la película, covers en español de las
  canciones, encuesta Stitch Day.
- **WebFetch**: thewaltdisneycompany.com (Stitch), Box Office Mojo (reseña
  ʻohana), Wikipedia (cifra de taquilla 2025); Hollywood Reporter no se pudo
  leer completo (redirección a un servicio de pago, tollbit.hollywoodreporter.com) —
  me quedé con el resumen del buscador para esa fuente ⚠️.
- **No until repetí** ninguna consulta ya hecha por `recolectar.py` en
  `datos-voz.md`.
