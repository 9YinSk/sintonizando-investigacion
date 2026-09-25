# Parte de TEXTO, JUEGOS Y TÉCNICA · Kakegurui (repaso)

Repaso del 25-sep-2026. La biblia ya tenía bien cubiertos los puntos 5
(Tipografía, §6), 6 (Cómo hablan, §7) y 11 (Videojuegos, §13) — los comprobé
con `seccion.py --rol texto` y no hacía falta rehacerlos. Lo que **faltaba
entero** eran los puntos 18, 24 y 25 (añadidos el 24-sep): no existían como
sección. Este archivo trae los datos para que el redactor los meta.

## Hallazgos

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Lo que dice el propio equipo (entrevistas):**

- El director **Yuichiro Hayashi** (林祐一郎) explica que pensó cada escena
  «como si fuera cine en imagen real» («if this is live-action how would I
  film it?») para huir de las expresiones «genéricas» del anime, y que buscó
  dar **tridimensionalidad al encuadre** («a frame and a scene that has
  emotional gravitas and energy, and three-dimensionality») y **jugar con la
  luz** («evening light, and moonlight, and different kinds of light», algo
  que no puede dar el manga en blanco y negro) ✅
  ([easternkicks.com](https://www.easternkicks.com/features/yuichiro-hayashi-interview/),
  [All the Anime](https://blog.alltheanime.com/interview-yuichiro-hayashi/)).
- El **diseñador de personajes Manabu Akita** (秋田学) explica el truco de
  las caras: **las normales las cuida más** para que sean «simples y monas»
  («通常時はシンプルで可愛くなるように心がけています» / «逆に通常時の方が気を
  使って描いているつもりです»), precisamente para que el contraste con el
  «顔芸» (kaogei, cara exagerada de cuando ganan o pierden) golpee más fuerte
  («通常時のキャラの表情と、顔芸と言われている激しい表情の時で差が出るように»)
  ✅ ([MANTANWEB](https://mantan-web.jp/article/20190309dog00m200005000c.html),
  confirma lo de §7 sacado de [4Gamer](https://www.4gamer.net/games/338/G033856/20170809048/)).
- **Cambio de filtro entre temporadas**, dicho por Hayashi: la 1.ª es
  «oscura, sucia (gritty) y realista»; la 2.ª es «más colorida, más vibrante»
  («the first season is quite dark, gritty… the second season is a bit more
  colourful, it's more vibrant») ✅ (misma entrevista de easternkicks, citada
  también por [Anime UK News](https://animeuknews.net/2019/08/interview-kakegurui-director-yuichiro-hayashi/)).
- **Manos y cartas en 3DCG**: la ficha técnica trae un **CG Director** en
  cada temporada (Jae-Hun Sin/신재훈, T1; Motoi Okuno/奥納基, ××) ✅
  ([AniList](https://anilist.co/anime/98314/staff), ya en `datos-texto.md`).
  Una entrevista de Comic Natalie con Hayashi (河本ほむら×小沢一敬×林祐一郎)
  dice que en set usaban fichas, cartas y pistolas de attrezzo y que el
  volteo de cartas se llevaba a la animación con esos movimientos reales; un
  resumen de búsqueda añade que las manos y las cartas pequeñas se resuelven
  con **CG 3D** dentro del dibujo 2D (técnica híbrida) ⚠️ **no pude abrir la
  página original** ([natalie.mu/comic/pp/kakegurui_anime01](https://natalie.mu/comic/pp/kakegurui_anime01)
  da 403 directo y por Wayback también; queda como ⚠️ una fuente indirecta,
  mejor que el «no pude abrir nada» de la vuelta anterior).

**Línea, sombra y luz (ya apuntado en §18 de la biblia, aquí con más detalle
para ampliarlo)**:
- Línea fina, limpia, de color oscuro casi negro (no marrón suave como Ghibli).
- Sombreado **plano en bloques** (2 tonos: piel/sombra), no degradado; el
  bloque de sombra en la cara se vuelve **duro y anguloso** en los primeros
  planos de tensión (mandíbula, párpado inferior) — coherente con el kaogei
  de Akita.
- Brillo especular **redondo y doble** en el iris (dos puntos blancos) y en
  labios húmedos.
- Luz de escena: una fuente cálida (tarde/lámpara) más un **contraluz de
  color** (rojo cuando gana/se emociona, azul si hay agua/acuario cerca) —
  exactamente lo que describe Hayashi de «evening light… different kinds of
  light» ✅.

**Cómo replicarlo en Photoshop:**
1. Línea: pincel duro de borde limpio (tipo «Kyle's Real Basic», libre en
   [Kyle T. Webster gratis para suscriptores Adobe]) a 2-3 px sobre lienzo
   2000 px; sin textura de papel encima (la serie no tiene grano visible de
   entintado).
2. Color base en una capa, sombra en **una sola capa de recorte** («clipping
   mask») en modo Multiplicar, pintada con formas duras (lazo poligonal, no
   pincel suave): así sale el bloque de sombra sin degradado.
3. Capa de contraluz en modo Trama de color o Aclarar, sólo en el borde del
   pelo/hombro, roja o azul según la escena (ver §18 de la biblia, paleta ya
   medida).
4. Brillo de ojos: dos elipses blancas pequeñas + una capa de degradado sutil
   encima del iris en modo Superponer.
5. Cara «kaogei»: exagera **sólo** boca, cejas y pupilas (achícalas o hazlas
   puntos); dejando el resto de la cara con el mismo dibujo base de Akita, no
   redibujando todo.

**Cómo replicarlo en Blender:**
1. **Sombreado tipo cel** con nodos: `Shader to RGB` → `Color Ramp` de 2-3
   bandas duras (sin interpolar) → `Emission`/`Diffuse`, para el bloque de
   sombra plano que describí arriba (funciona con Eevee).
2. **Contorno**: `Solidify` (normales invertidas, material negro sólido, 0.01-
   0.02 de grosor) para el trazo limpio de la serie; o `Freestyle` con grosor
   fino (1-1.5 px) y color casi negro si se quiere afinar por ángulo de
   cámara — ambas son las técnicas estándar para este acabado, no algo que
   use el estudio (no hay entrevista sobre el proceso 3D del estudio en
   Blender: MAPPA no usa Blender para el show).
3. **Luz**: dos puntos, uno cálido de key (temperatura ~3200K) y un **rim
   light** de color rojo o azul detrás del personaje, tal como pide Hayashi;
   sin luz de relleno frontal para no perder el bloque duro de sombra.
4. **Modelos y rigs libres** (comprobados en la API de Sketchfab):

| Modelo | Enlace | Licencia | Caras/vértices |
|---|---|---|---|
| Runa Yomozuki (con rig, `.blend`/FBX) | [Sketchfab](https://sketchfab.com/3d-models/runa-yomozuki-kakegurui-70dafed89bcd4dd3b9f5654f90ebeef3) por Gustav_Johansson00 | CC BY-NC (crédito, no comercial) | 40 434 caras · 22 040 vértices |
| Kakegurui Runa (alta densidad, sin rig) | [Sketchfab](https://sketchfab.com/3d-models/kakegurui-runa-b015aaa7272c4191a543722ead37a316) por claener | **CC BY** (crédito, uso comercial permitido) | 2 459 421 caras |

   No hay Yumeko, Mary ni Kirari con licencia libre y descargable en
   Sketchfab a día de hoy ⚠️ (comprobado con la API, `q=kakegurui yumeko`,
   `q=kakegurui mary`, `q=kakegurui kirari`, sin resultados descargables). El
   tapete verde y las fichas de póquer sí tienen textura y modelo libres (ver
   §18-19 de la biblia, ya puestos por imagen).
5. **Textura encima**: pinta el grano de tela del blazer rojo con una textura
   de sarga fina a baja opacidad (modo Multiplicar), y añade una **aberración
   cromática muy leve** sólo en los bordes de alto contraste del contraluz
   rojo, para imitar el look «gritty» de la 1.ª temporada que menciona
   Hayashi.
6. **Grano**: una capa de ruido fino (2-3%, modo Superponer) sobre toda la
   imagen ayuda a igualar el aspecto «gritty» de la temporada 1; para la
   temporada 2 (más vibrante, según la misma entrevista) hay que bajarlo o
   quitarlo y subir un poco la saturación. No encontré ninguna entrevista que
   diga el filtro exacto que usa el estudio en fotografía (撮影): esto es una
   receta para llegar al mismo resultado visual, no una copia de su proceso.

**Qué programas usó el estudio**: no encontré ninguna entrevista que nombre
el software de animación digital (Clip Studio Paint, RETAS, Toon Boom…) que
usó MAPPA en Kakegurui ⚠️ — sólo confirmé que hay un CG Director en cada
temporada (arriba) y la cita sobre cámara/luz de Hayashi. Busqué en japonés e
inglés («撮影 賭ケグルイ», «Kakegurui RETAS OR Toon Boom OR Clip Studio») sin
resultado; lo dejo en «No encontré» en vez de inventar un programa.

**Encuadres y composición** (a partir de lo que ya está mirado en fotogramas,
§2 y §18 de la biblia, más la idea de Hayashi de «pensar en cine»):
- Plano medio con la **mesa de juego en primer término**, algo desenfocada,
  y la cámara **un poco baja** (mirando ligeramente hacia arriba al
  personaje): ya lo dice la Guía IA de la biblia (§18) y coincide con el
  objetivo de Hayashi de dar peso y tridimensionalidad al plano.
- Para el «kaogei»: primer plano muy cerrado, cámara al mismo nivel de los
  ojos, fondo que se apaga a negro o a un color sólido (nunca el fondo del
  aula): así el gesto de la cara es lo único que se lee.
- Diálogo tranquilo (Kirari, el consejo): plano medio-largo, simétrico,
  personaje centrado tras el escritorio — el opuesto de la cámara inclinada
  de las escenas de apuesta.

### Punto 24 · Obras parecidas y temas relacionados

**Series de tono o estilo parecido** (de las recomendaciones de usuarios de
AniList, ya en `datos-texto.md`, no repito la consulta): *No Game No Life*,
*Classroom of the Elite*, *Death Parade*, *Kaiji*, *Death Note*, *Prison
School*, *Akagi*, *Tomodachi Game*, *Talentless Nana* — todas comparten
«juegos psicológicos con mucho en juego» ✅.

**Influencia que la propia autora reconoce** (entrevista directa, en
japonés, la fuente más fuerte que hay para este punto):
- **Homura Kawamoto** (河本ほむら, guionista) dice que al leer *Kaiji* de
  Nobuyuki Fukumoto pensó **«¡Existe un manga así!»** («『カイジ』（福本伸行）
  ですね。「こんな漫画があるんだ！」と思いました») — es la influencia de manga
  de apuestas que ella misma cita ⚠️ (una entrevista, no repetida en otra
  fuente que encontrara, pero es su propia voz)
  ([Big Comic BROS.NET, parte 2](https://bigcomicbros.net/8281/)).
- También cita como influencias, **fuera del género de apuestas**: la novela
  de misterio *El caso de los crímenes del zodíaco* (『占星術殺人事件』, Sōji
  Shimada), *Satsuriku ni Itaru Yamai* (Takemaru Abiko) y el videojuego de
  novela visual **Kamaitachi no Yoru** ⚠️ (misma entrevista).
- Su filosofía de diseño, en su propia frase: **«se dibuja a la persona que
  está jugando, no el juego»** («ギャンブルをやっている《人》を描くんだ») — por
  eso Kakegurui se centra en la cara y no en las reglas del juego; útil para
  la guía de IA de texto (§17, la hace el redactor) ⚠️ (misma entrevista).
- El proceso con el dibujante **Tooru Naomura** (尚村透) es de ida y vuelta:
  Kawamoto cuenta que la escena en la que Sayaka acaricia la silla de la
  presidenta fue **idea de Naomura**, y que esa imagen le hizo profundizar en
  la devoción del personaje ⚠️ (misma entrevista,
  [Big Comic BROS.NET, parte 2](https://bigcomicbros.net/8281/)).

**Qué otras láminas del servidor se le parecen** (para no repetir ideas):
- **Death Note** (`biblias/18-death-note/`, ya terminada): comparte el
  género de «juego psicológico de altos vuelos», pero sus 3 conceptos de
  lámina usan **un cuaderno** y **una pantalla de televisor** — nada de mesa
  de casino, cartas ni fichas, así que no hay choque con los conceptos de
  Kakegurui (mesa de piedra-papel-tijera, escritorio del consejo, tablón de
  avisos) ✅ (comprobado leyendo `biblias/18-death-note/biblia.md`, líneas
  1034-1140).
- **No Game No Life** (`encargos/84-no-game-no-life.md`): tiene encargo pero
  **su biblia todavía no existe** (carpeta vacía). Es la recomendación más
  votada junto a Kakegurui en AniList y comparte «la vida como un juego»: si
  se hace en el futuro, avisar a su investigador de texto para que no repita
  la idea de «mesa con cartas y fichas» como objeto central ⚠️ (aviso para el
  dueño, no un hallazgo cerrado).
- No encontré ninguna otra biblia terminada en `biblias/` con casino, apuestas
  o consejo estudiantil como eje (revisé los encabezados de
  `biblias/24-assassination-classroom/` —colegio, pero sin apuestas— y
  `biblias/45-mob-psycho-100` no tiene biblia aún).

### Punto 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo, en cinco líneas** (de la wiki, wikitext comprobado):
1. La academia Hyakkaou (私立百花王学園, fundada hace 122 años) no evalúa por
   notas ni deporte: **el que gana apostando manda** ✅
   ([Fandom, Hyakkaou Private Academy](https://kakegurui.fandom.com/wiki/Hyakkaou_Private_Academy)).
2. El **consejo estudiantil** cobra «donaciones» —en teoría voluntarias, en
   la práctica obligatorias— y con eso controla todo el juego del colegio, y
   por extensión negocios y política fuera de él ✅ (misma fuente).
3. Quien queda entre los **últimos 100 de 3000 alumnos** por donación se
   vuelve **«housepet»** (家畜): chicos «Pochi» (perro), chicas «Mike»
   (gata) —en el doblaje inglés «Fido»/«Mittens»—, con una placa al cuello,
   sin derechos, y sólo puede librarse ganando un «combate oficial» o
   pagando un millón de yenes ✅
   ([Fandom, Housepet](https://kakegurui.fandom.com/wiki/Housepet)).
4. Los alumnos con **deudas impagables** reciben un «Plan de Vida» (人生計画
   表, un cuadernillo que dicta trabajo y matrimonio tras graduarse); el
   consejo usa sus contactos familiares para que se cumpla al pie de la letra
   ✅ (misma fuente).
5. Detrás de todo está el **clan Momobami** (百喰一族, «las cien familias
   devoradoras»): ramas emparentadas y hostiles entre sí, cada apellido
   termina en «-bami» («que devora») y controla un negocio distinto (juego,
   venenos, medicinas, resolución de conflictos); Kirari es su líder desde
   los siete años ✅
   ([Fandom, The Hundred Devouring Families](https://kakegurui.fandom.com/wiki/The_Hundred_Devouring_Families)).

**La historia por arcos** (wikitext de
[Fandom, Story Arcs](https://kakegurui.fandom.com/wiki/Story_Arcs), cruzado
con los capítulos de anime que ya cita la biblia en §0):

*Temporada 1 — «Student Council Saga»* (ep. 1-12):
- **Arco de introducción**: Yumeko llega, Mary intenta hacerla «housepet»
  con el voto a piedra-papel-tijera (ver §2 de la biblia, 1×01).
- **Arco de canje de deudas**: Yumeko cae a housepet, la ponen a jugar
  póquer indio.
- **Arco del juego ESP**: Midari la reta a un juego de vida o muerte con
  Suzui de por medio.
- **Guerra total contra el consejo**: gana a Yumemi (ídolo del colegio) y a
  Kaede (contable del consejo).
- **Torre de las Puertas**: duelo final contra Sayaka, la secretaria.

*Temporada 2 — «Presidential Election Saga»* (ep. 13-24, «Kakegurui ××»):
- **Guillotina de dedos**: Erimi arrastra a Yumeko y Midari a un juego donde
  se puede perder más que dinero o votos.
- **Nim Type Zero**: dos hermanas del clan Momobami les tienden una trampa
  de cartas.
- **El juego del bien común**: Yumeko contra Miroslava e Ibara (clan
  Momobami) e Itsuki y Kaede, por un montón de votos.
- **Concurso de actuación**, con la ídolo Yumemi.
- **Subasta de cien votos** (arco original del anime, no del manga).
- Cierra con el arco de la elección: Ririka con máscara y sus «100 votos»
  (ver §2 de la biblia, 2×03) y la reelección de Kirari.
- El manga sigue después del episodio 24 con más arcos (Guerra, Gran Torneo)
  que **todavía no tienen anime** ✅ (misma fuente wiki).

**Momentos clave con minuto** (algunos ya en §2 de la biblia, aquí puestos en
orden de la historia):
- 1×02, 00:03:51-00:04:59: se explica el sistema housepet completo (el
  «porqué» del mundo).
- 1×01, 00:22:32: Yumeko se declara «a gambling freak… a compulsive
  gambler» — el título de la serie dicho en voz alta.
- 2×03, 00:07:31: Ririka y los «100 votos», el clímax de la elección.
- 2×05, 00:07:01: Kirari dice «オールイン» (all in) dos veces, antes del
  cierre de temporada.

**Emblemas, logos y objetos icónicos** (medidos en la wiki):

| Objeto | Qué es | Imagen | Tamaño |
|---|---|---|---|
| Placas de housepet | Chapa con forma de pata para el cuello, una para «gato» y otra para «perro» | [Kakegurui_collar.jpg](https://static.wikia.nocookie.net/kakegurui/images/c/c3/Kakegurui_collar.jpg/revision/latest?cb=20201225202413) | 749×807 ✅ (medido con la API) |
| Placas sobre la mesa (varias juntas) | Cómo se ven en grupo, útil para una lámina 2 de economía | [Housepet_tags_drama.jpg](https://static.wikia.nocookie.net/kakegurui/images/e/e3/Housepet_tags_drama.jpg/revision/latest?cb=20190714181215) | 1000×667 ✅ |
| Cuadro del sistema de mascotas (manga) | Explica el sistema con dibujos, sirve de referencia de cómo lo dibuja el propio manga | [Volume_1_Pet_System...PNG](https://static.wikia.nocookie.net/kakegurui/images/6/65/Volume_1_Pet_System_explanation_image.PNG/revision/latest?cb=20170630200326) | 881×343 ✅ |
| Escudo/edificio de la academia | Fachada del edificio (occidental, tras la reforma de Kirari) | [HyakkaoAcademy.jpg](https://static.wikia.nocookie.net/kakegurui/images/7/78/HyakkaoAcademy.jpg/revision/latest?cb=20190809132405) | 669×435 ✅ |
| Emblema del clan Momobami | Ilustración del árbol/clan usada en la wiki | [Clan.jpg](https://static.wikia.nocookie.net/kakegurui/images/a/a1/Clan.jpg/revision/latest?cb=20190206092249) | 1880×947 ✅ |

Nota: la wiki no tiene un «logo oficial del consejo estudiantil» aparte del
sello rojo que ya se ve en los papeles (§7 de la biblia); no encontré un
escudo de tela o metal distinto del edificio ⚠️.

**Vocabulario propio** (comprobado en el wikitext, útil para cartelas y para
la guía de IA de texto del redactor):
- **賭ケグルイ** (kakegurui): la palabra real es «賭博狂い» (compulsión al
  juego); el título la escribe medio en katakana para que se vea más
  agresiva — es el género de la serie hecho palabra ✅.
- **家畜** (kachiku, «ganado/mascota»): el estatus de los últimos del ranking.
- **ポチ/ミケ** (Pochi/Mike): nombres genéricos de perro/gata que usan de
  mote para los housepets; el doblaje inglés de Netflix los cambia por
  «Fido»/«Mittens» (ya en §7 de la biblia) ✅.
- **生徒会** (seitokai, consejo estudiantil) y **公式戦** (kōshiki-sen,
  «combate oficial»): el único derecho que tiene un housepet, retar a
  cualquiera a una apuesta que no se puede rechazar ✅.
- **人生計画表** (jinsei keikakuhyō, «plan de vida»): el cuadernillo-condena
  de quien no puede pagar (ya en §7 de la biblia como objeto de mesa) ✅.
- **百喰一族** (Momobami-ichizoku, «las cien familias devoradoras»): el clan
  detrás de todo; cada apellido de rama termina en «-bami» ✅.
- **顔芸** (kaogei, «arte de la cara»): la palabra que usa la prensa y el
  fandom (japonés y chino, ver §7 de la biblia) para las caras exageradas; es
  el término que hay que usar al pedirle a una IA de imagen ese gesto, mejor
  que «anime face».

## Lo mejor para la lámina

- La cita de Kawamoto **«se dibuja a la persona que juega, no el juego»**
  explica por qué la cara manda sobre la mecánica: en el objeto de la lámina,
  el personaje siempre debe estar reaccionando, no sólo sosteniendo cartas.
- El contraste **cara normal cuidada / kaogei exagerado** de Akita es la
  clave técnica para no hacer un dibujo «plano»: dos capas de expresión, no
  una intermedia.
- El **rig libre de Runa** (Sketchfab, CC BY-NC) es el único personaje
  principal con modelo 3D listo para posar en Blender; para las demás, sólo
  quedan fotogramas y arte oficial como referencia de pose.
- El vocabulario **家畜 / ポチ / ミケ / plan de vida / 100 votos** da nombres
  reales para las cartelas de la lámina 2 de economía, en vez de inventar
  términos genéricos de «casino».
- El emblema del clan Momobami (`Clan.jpg`) y las placas de housepet dan dos
  símbolos gráficos listos para grabar en la caja o el tablón del concepto A/C.

## No encontré

⚠️ **TV Tropes** (`tvtropes.org/pmwiki/pmwiki.php/Anime/Kakegurui`): da 403
en curl directo y en WebFetch; dos intentos, no insistí más (regla de
AYUDANTE.md).
⚠️ **The Cutting Room Floor**: Cloudflare bloquea la API (`tcrf.net`) incluso
para una búsqueda simple; no hay entrada de Kakegurui indexada en los
resultados de Google tampoco, y son juegos de navegador/móvil sin beta
conocida — probable que TCRF no tenga nada de esta franquicia.
⚠️ Confirmación de segunda fuente para «las cartas y manos se animan en
3DCG»: sólo tengo el resumen de una búsqueda sobre la entrevista de Comic
Natalie (la página da 403 en directo y en Wayback). Dejo los nombres de los
CG Directors (verificables en AniList) para que quien tenga acceso pueda
abrir la entrevista original si hace falta subir esto a ✅.
⚠️ Un «logo» o escudo textil propio del consejo estudiantil, aparte del
sello rojo de los documentos.
⚠️ Modelos 3D libres de Yumeko, Mary o Kirari en Sketchfab (sólo hay de Runa).

## Bitácora de búsqueda (esta tanda)

- `seccion.py 12-kakegurui --rol texto` y `--avisos`: confirman que §6, §7 y
  §13 (puntos 5, 6, 11) ya estaban hechos; no repetí esas consultas.
- Fandom API (`kakegurui.fandom.com/api.php`), en español no hace falta
  (wiki en inglés): `list=search` para «House Pet system», «Momobami Clan
  crest», «Guild members»; `list=allpages` para localizar «Story Arcs»,
  «Basic Vocabulary», «The Hundred Devouring Families»; `action=parse` sobre
  «Hyakkaou Private Academy», «Housepet», «Student Council», «The Hundred
  Devouring Families», «Story Arcs», «Kakegurui (Animated)», «Kakegurui -
  Compulsive Gambler», «Basic Vocabulary» (wikitext completo).
- `action=query&prop=imageinfo&iiprop=url|size` sobre 5 imágenes de la wiki
  para medir tamaño real (Clan.jpg, Kakegurui collar.jpg, HyakkaoAcademy.jpg,
  Housepet tags drama.jpg, Volume 1 Pet System...PNG).
- Sketchfab API (`api.sketchfab.com/v3/search?type=models&q=kakegurui`,
  variantes con «yumeko», «mary», «kirari», todas con `downloadable=true`):
  sólo Runa tiene resultados descargables.
- WebSearch (contadas: 9 de las ~50 del cupo, en japonés e inglés):
  «賭ケグルイ アニメ カード 3DCG 撮影 制作», «Kakegurui anime production MAPPA
  making of interview art style», «"賭ケグルイ" 林祐一郎 インタビュー 手 カード
  作画», «Kakegurui season 2 art style change more colorful vibrant Hayashi
  interview», «"賭ケグルイ" アニメ 監督 カードさばき CG 表現», «秋田学 賭ケグルイ
  キャラクターデザイン インタビュー 顔芸 デフォルメ», «賭ケグルイ 美術監督 野村
  正信 OR 松田春香 背景 インタビュー», «河本ほむら 賭ケグルイ 影響を受けた作品
  インタビュー 福本伸行», «河本ほむら "カイジ" 影響 賭ケグルイ インタビュー».
- WebFetch: `blog.alltheanime.com/interview-yuichiro-hayashi`,
  `easternkicks.com/features/yuichiro-hayashi-interview`,
  `mantan-web.jp/article/20190309dog00m200005000c.html`,
  `bigcomicbros.net/8280` y `/8281` (entrevista completa a Kawamoto, en dos
  partes). Fallaron (403, dos intentos cada uno): `natalie.mu/comic/pp/…`
  (directo y por Wayback), `w.atwiki.jp/sakuga/pages/2206.html`,
  `tvtropes.org/…/Anime/Kakegurui`, `tcrf.net` (Cloudflare).
- Comparé cabeceras de secciones y conceptos de lámina de
  `biblias/18-death-note/biblia.md` (líneas 1020-1140) contra los de
  Kakegurui para el punto 24, y comprobé que `biblias/84-no-game-no-life/`
  está vacía (sólo el encargo).

Sigue: nada obligatorio pendiente de los puntos 18, 24 y 25. Si hay tiempo
extra: intentar de nuevo `natalie.mu` (quizá por otro espejo) para subir a
✅ el dato de las cartas en 3DCG, y repasar los ⚠️ que ya traían §6/§7/§13
(letra del logo, diseño real de la placa y el tablón) — no son obligatorios
de mi reparto pero ayudarían a la tabla de cumplimiento del redactor.
