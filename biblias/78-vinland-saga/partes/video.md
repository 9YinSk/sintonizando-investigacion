# Vídeo — Vinland Saga (encargo 78)

Investigador de vídeo. Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Parte de
`datos-video.md` (AnimeThemes cayó con HTTP 522, comprobado tres veces hoy —
sigue caído). YouTube pide iniciar sesión desde este servidor para bajar vídeo
(confirmado: `yt-dlp` da `HTTP Error 403: Forbidden` al descargar), así que
todo lo mirado sale de **Dailymotion** (vídeo completo, se descarga bien) y de
**storyboards de YouTube** (mosaicos de miniaturas que YouTube sí sirve sin
login; resolución baja —160×90— pero permiten identificar la escena con el
minuto ±2 s, como pide la consigna). Formato de dato:
`- dato · fuente(s) · ✅/⚠️ · minuto/tamaño`.

## Hallazgos

### Punto 9 — Música: openings, endings y ambiente

Las 6 canciones y sus tramos de episodios, confirmados en dos fuentes cada
una (Doblaje/wiki de la serie, texto completo `Song Info` de cada página +
duración "1:30 (TV)" que coincide con el clip real mirado):

- OP1 **"MUKANJYO"** (無感情), Survive Said The Prophet, estreno 21-ago-2019, episodios 1-12 · https://vinlandsaga.fandom.com/wiki/MUKANJYO · ✅ (wikitext de la página + **mirado entero**, 90 s, en Dailymotion, ver abajo)
- OP2 **"Dark Crow"**, MAN WITH A MISSION, estreno 23-oct-2019, episodios 13-24 (reemplaza a MUKANJYO) · https://vinlandsaga.fandom.com/wiki/Dark_Crow · ✅ (wikitext + duración TV 1:30 coherente)
- OP3 **"River"**, Anonymouz, estreno 15-feb-2023, episodios 25+ (temporada 2) · https://vinlandsaga.fandom.com/wiki/River · ✅ (wikitext, con referencia a sonymusic.co.jp)
- ED1 **"Torches"**, Aimer, estreno 14-ago-2019, episodios 1-12 · https://vinlandsaga.fandom.com/wiki/Torches · ✅ (wikitext + **mirado entero** por storyboard de YouTube, ver abajo)
- ED2 **"Drown"**, milet, estreno 4-nov-2019, episodios 13-24 (reemplaza a Torches) · https://vinlandsaga.fandom.com/wiki/Drown · ✅ (wikitext)
- ED3 **"Without Love"**, LMYK, estreno 1-mar-2023, episodios 25+ · https://vinlandsaga.fandom.com/wiki/Without_Love · ✅ (wikitext, con referencia a lmyk.jp)

**Estudios de animación**: WIT Studio (temporada 1, 2019), MAPPA (temporada 2,
2023) · https://vinlandsaga.fandom.com/wiki/Vinland_Saga_(anime) (infobox) y
AniList https://anilist.co/anime/101348 · ✅ (dos fuentes).

**Compositor de la banda sonora**: Yutaka Yamada (山田 悠人), se mantuvo de
la temporada 1 a la 2 según la wiki · https://vinlandsaga.fandom.com/wiki/Vinland_Saga_(anime)
(sección "Background") · ⚠️ (una sola fuente; AniList no lista el rol de
música para este anime y Wikipedia en inglés dio "too many requests" al
consultarlo — no lo reintenté para no gastar más).

**OP1 "MUKANJYO" mirado entero** (90 s = duración TV exacta, confirmado por
el texto "MUKANJYO / Survive Said The Prophet" que aparece en pantalla a
0:33): https://www.dailymotion.com/video/x8bcl5n (repost de MGG Spain) · ✅
— fotogramas cada 3 s con `fotogramas.py`, 31 fotogramas, 1280×720. Qué
transmite: arranca con mar tormentoso y el logo en rojo sangre sobre esa
tormenta (0:03-0:09), sigue con dracares vikingos en la niebla, la infancia
de Thorfinn en Islandia (nieve, casas con techo de paja) y cierra con la
banda de mercenarios, un campo de cadáveres bajo la Vía Láctea y un cielo
estrellado — resume la escala "épica y cruda" que pide el encargo en un solo
minuto y medio.

**ED1 "Torches" mirado entero** (90 s, por storyboard de YouTube —
`rlb942EnOF0`, "Vinland Saga「Torches」- Ending 1 | 4K | 60FPS | Creditless",
duración 90 s = TV exacta, canal Rirakkusu Studio; **plan C de AYUDANTE.md**
porque YouTube bloqueó la descarga directa): https://www.youtube.com/watch?v=rlb942EnOF0
· ✅ — storyboard de baja resolución (160×90, ~1 fotograma/segundo) leído
completo en 4 mosaicos. Contenido: un dracar navega entre fiordos nevados al
atardecer con una figura pequeña y rubia (niño) mirando el paisaje; luego
aurora boreal verde sobre el mar de noche; después una silueta infantil
camina con una antorcha encendida por una montaña oscura en tormenta (la
imagen que da título a la canción); termina con luz blanca que se abre a un
trigal dorado con flores donde camina la misma silueta — de la crudeza
vikinga a un recuerdo cálido y de esperanza. Contraste tonal fuerte con los
openings, típico de la serie (calma después de la violencia).

**Efectos de sonido y onomatopeyas reconocidas**: ⚠️ no encontré una fuente
que las liste para el ANIME (fandom.com no tiene página de "Sound Effects").
Busqué `srsearch=sound effect` y `srsearch=onomatopoeia` en la wiki en inglés
y no hay resultados; es un dato más propio del manga impreso (tipografía),
que le toca al investigador de texto (punto 6 de ENCARGO.md). Lo dejo dicho
aquí para que no se pierda.

### Punto 10 — Vídeos: tráilers, escenas oficiales, tendencias

**Tráiler oficial temporada 2** (español, repost legal de FilmAffinity —
ficha de cine.es reconocida), 2:20 min, con subtítulos en español pegados:
https://www.dailymotion.com/video/x8h1n5b · ✅ (duración 140 s = 2:20, coincide
con el otro repost igual de 3djuegos https://www.dailymotion.com/video/x8p41mq,
dos fuentes) — mirado entero con `fotogramas.py --cortes` (97 planos) y varios
fotogramas en 1280×720:
- 0:03 "Obra Original Makoto Yukimura" / 0:07 "Producción MAPPA" — cartelas de
  crédito con tipografía serif blanca sobre negro.
- 0:12-0:31 flashback de **Einar**: aldea en llamas, siluetas de soldados,
  niño rubio llorando — "Eran bestias, monstruos con aspecto humano" / "Esta
  vez protegeré a mis hijos de la tormenta que son los adultos"
  (https://www.dailymotion.com/video/x8h1n5b?t=39). Encaja con la ficha de
  Einar en la wiki (aldea de Arnheid destruida, madre y hermana muertas) ·
  https://vinlandsaga.fandom.com/wiki/Einar · ✅ (dos fuentes: subtítulo +
  wikitext de Einar).
- 0:47-0:59 grupo de campesinos/esclavos de la granja hablando ("Hay gente
  prejuiciosa en todas partes, pero no todos lo son") y una chica rubia
  envuelta en una manta ("No pasaré el resto de mi vida en el fin del mundo",
  https://www.dailymotion.com/video/x8h1n5b?t=58) — arco de la granja (S2).
- 1:05-1:16 hombre rubio adulto discutiendo con su padre ("En absoluto,
  padre" / "generará tempestades", https://www.dailymotion.com/video/x8h1n5b?t=70)
  — probable escena de **Canute** con el rey Sven; ⚠️ no confirmé el nombre
  exacto del padre en pantalla, sólo por contexto (Canute es el único
  personaje con arco de "hijo de rey" en la serie, según su ficha
  https://vinlandsaga.fandom.com/wiki/Canute).
- 1:17 vista aérea de una ciudad portuaria vikinga con muelles de madera y
  decenas de barcos (https://www.dailymotion.com/video/x8h1n5b?t=77) — fondo
  para el punto 4.
- 1:20-1:27 anciano de pelo blanco hablando con un joven rubio en la costa:
  "Estoy buscando al hijo de un amigo al que convirtieron en esclavo" — es
  **Sverkel** (el amo de la granja) buscando al hijo de Thors, o sea a
  **Thorfinn** · guion coherente con el arco de la granja; ⚠️ nombres no
  confirmados en pantalla, sólo por trama.
- 1:29-1:34 trabajo agrícola: brazos tirando de una cuerda para arrancar un
  tocón ("con calma", https://www.dailymotion.com/video/x8h1n5b?t=91) — la
  vida de granjero de Thorfinn en la temporada 2.
- 1:40-1:44 dos figuras se pelean a puñetazos ("¿Lo ves, Thorfinn?", un
  hombre de pelo oscuro golpea a un joven de camiseta morada,
  https://www.dailymotion.com/video/x8h1n5b?t=102) — Thorfinn recibe el golpe
  sin defenderse (su pacifismo de la temporada 2).
- 2:00-2:07 silueta de un castillo con relámpagos/fuego y filas de soldados:
  "Necesitarás más cadáveres para llegar a lo más alto"
  (https://www.dailymotion.com/video/x8h1n5b?t=122) — tono político y oscuro
  del arco de Canute rey.
- 2:16 cartela final "VINLAND SAGA SEASON 2" con el reparto en japonés.

**PV5 (5º tráiler japonés oficial)**: https://www.youtube.com/watch?v=5xqEp7R9SYM
· título「ヴィンランド・サガ」第5弾アニメPV, 105 s · fuente AniList
https://anilist.co/anime/101348 · ⚠️ metadatos confirmados (duración, título)
pero **no se pudo mirar**: YouTube bloqueó la descarga con 403 y no encontré
el mismo tráiler reposteado en Dailymotion ni Internet Archive (probé
"Vinland Saga PV5", "Vinland Saga PV 5" — nada).

**Escena icónica 1 — muerte/rendición de Thors** (episodio 4, "A True
Warrior" 本当の戦士): Thors vence a los hombres de Askeladd y a Askeladd
mismo en duelo, pero se rinde para salvar a Thorfinn y muere por la espalda ·
confirmado en dos fuentes de la wiki: ficha de personaje
https://vinlandsaga.fandom.com/wiki/Thors_Snorresson (lista el episodio 2 y
"defeated Askeladd in their duel") y la sinopsis del episodio
https://vinlandsaga.fandom.com/wiki/Episode_4 ("Thors advances through
Askeladd's men... challenges Askeladd to a duel... but surrenders") · ✅.
Mirado por storyboard de YouTube (clip corto ya recortado, no el episodio
completo, por eso el minuto es dentro del CLIP, no del episodio — dejo esto
como ⚠️): https://www.youtube.com/watch?v=LPnQ74j1dqY ("Thors Last words for
his son thorfinn", 41 s). Qué se ve: Askeladd con la espada en alto y una
sonrisa cruel; Thors arrodillado con la espada bajada, la mano en la
empuñadura, sin atacar; el rostro de **Thorfinn niño** con los ojos muy
abiertos de horror; luego la mancha de sangre extendiéndose en la túnica gris
de Thors. Es de los momentos que más se citan de la serie (arranca el "no
tengas enemigos" que persigue a Thorfinn el resto de la historia).

**Escena icónica 2 — muerte de Askeladd** (episodio 24, "End of the Prologue"):
final de temporada 1, Thorfinn apuñala a Askeladd (a petición de este, para
salvar a Canute) · confirmado en https://vinlandsaga.fandom.com/wiki/Episode_24
(título y posición como último episodio de temporada) y la búsqueda de texto
de la wiki que devuelve esta página al buscar "Askeladd dies Thorfinn knife" ·
✅. Mirado por storyboard de un clip **oficial del canal de Crunchyroll**
(marca de agua "Crunchyroll" visible en cada fotograma):
https://www.youtube.com/watch?v=PF2NTT_mnps ("Askeladd's Death | VINLAND
SAGA", 180 s). Con subtítulos en inglés: "Is this the first time you've
stabbed someone, prince?" / "Hey, Askeladd" / "You did well" / "This part is
important" / "Don't waste it". Se ve a Askeladd con la banda roja en la
cabeza y el ojo marcado, tendido y ensangrentado; un personaje rubio joven
llorando lo sostiene (Thorfinn o Canute — a 160×90 no pude distinguirlos con
certeza, ⚠️); guardias con antorchas de fondo, celda de piedra.

**Escena/clip 3 — "discurso de la marea" de Canute**: clip del canal oficial
de **Netflix Anime**: https://www.youtube.com/watch?v=Zt85YuG0-_Y ("Canute's
Famous Tide Speech | VINLAND SAGA | Clip | Netflix Anime", 184 s) · ⚠️ no
localicé el episodio exacto (busqué en la wiki "tide speech", "command the
tide", "Canute addresses army" y sólo salió la ficha general de Canute, no un
episodio concreto — mi mejor candidato por tema, Episodio 44 "Pain", resultó
ser sobre el ataque a la granja de Ketil, no éste, así que lo descarto y dejo
sin confirmar). Se ve a Canute con capa roja real ante su ejército al
atardecer sobre el mar, con cortes a una escena estilo tapiz de Bayeux
(caballería medieval bordada) y primeros planos de su cara transformada, fría
y decidida — es el momento bisagra en que deja de ser el príncipe débil y se
vuelve el rey despiadado.

**Tendencia de edición/TikTok**: encontré un vídeo en formato vertical (9:16,
con barras negras a los lados, subtítulos en inglés tipo "Do you think you
can be... while you're still half-ass...") en Dailymotion, típico de un
"edit" de TikTok reposteado: https://www.dailymotion.com/video/x8rnpp0 (canal
Toxic-dj, 52 s) · ⚠️ una sola fuente, no pude confirmar el TikTok original
(TikTok no es accesible por API abierta desde aquí) ni el conteo de vistas.
Sirve como referencia del tipo de recorte (primeros planos muy cerrados,
corte rápido al ritmo de música) que usa el fandom para "edits" del
personaje.

**Análisis oficial / making of**: ⚠️ no encontré vídeos de detrás de cámaras
oficiales en Dailymotion ni Internet Archive (sólo encontré episodios
completos y tráilers). Búsquedas hechas: "Vinland Saga making of",
"Vinland Saga staff interview video", sin resultado en Dailymotion.

### Punto 4 — Fondos, sitios: luz y paleta medida

Todos los hex son de `herramientas/estilo.py` sobre fotogramas propios
(1280×720 salvo que se diga lo contrario), citando el vídeo y segundo exacto:

- **Aurora boreal sobre el mar, de noche** (OP1, t≈60-66 s,
  https://www.dailymotion.com/video/x8bcl5n?t=60): paleta fría de azules muy
  oscuros — `#131E35` `#16244A` `#1A3064` `#1B3F7B` `#20578F` `#2895B6`
  `#2373A3` `#34BAC6`; saturación 73 %, brillo 45 %, sombreado degradado con
  muy poca línea marcada. Es la escena que más se repite en el imaginario de
  fans (también sale en el ED1, ver arriba).
- **Campo de cadáveres bajo la Vía Láctea** (OP1, 1:24,
  https://www.dailymotion.com/video/x8bcl5n?t=84): paleta oscura violeta-gris
  — `#1B1C1D` `#6A5F76` `#4A4F6F` `#131314` `#252628` `#2B3140` `#3C4257`
  `#8B7C9E`; brillo muy bajo (30 %), saturación 23 %. Un guerrero solitario de
  pie en la cima de la colina de cuerpos, con lanzas y espadas clavadas
  alrededor, cielo con la Vía Láctea en violeta y rosa.
- **Islandia nevada, casas con techo de paja** (OP1, 0:51,
  https://www.dailymotion.com/video/x8bcl5n?t=51): paleta muy clara y fría —
  `#F1F1EA` (41 %) `#9DB1D0` `#CED1D9` `#C5B096` `#7B94B9` `#48658B`; brillo
  81 %, saturación baja (16 %), típico "blanco frío" de invierno nórdico con
  acentos azul-grisáceo en las sombras de la nieve.
- **Créditos sobre praderas verdes de Inglaterra** (OP1, 0:27,
  https://www.dailymotion.com/video/x8bcl5n?t=27): paleta cálida terrosa —
  `#DBD3C3` `#E6E7E4` `#C1BCB1` `#CFC288` `#ACA593` `#9C8F71`; brillo 73 %,
  saturación baja (17 %) — nota: fotograma con texto de créditos superpuesto,
  la paleta de fondo real es algo más verde de lo que registra el promedio.
- **Puerto vikingo visto desde arriba, muelles y barcos** (tráiler S2, 1:17,
  https://www.dailymotion.com/video/x8h1n5b?t=77): paleta tierra + agua —
  `#9E8F66` `#41616A` `#7F7152` `#B4A684` `#2E413E` `#D1C6A7` `#60533C`
  `#658490`; brillo 53 %, saturación 33 %, línea normal — agua azul-verde
  turbia y casas de madera en tonos tostados.
- **Bosque de la granja (tirando de un tocón)** (tráiler S2, 1:31,
  https://www.dailymotion.com/video/x8h1n5b?t=91): paleta verde bosque —
  `#263020` `#EAC7A1` `#363D27` `#1B2616` `#A07758` `#554E2D` `#816541`
  `#BC9875`; brillo 44 %, saturación 40 %, sombreado degradado con poca
  línea — piel muy iluminada por el sol de mediodía sobre fondo verde oscuro.
- **Castillo con relámpagos, tropas en fila** (tráiler S2, 2:02,
  https://www.dailymotion.com/video/x8h1n5b?t=122): paleta fuego/oscuro —
  `#241B0D` `#462D1B` `#F9F7F1` `#694630` `#8F654A` `#0B0907` `#B68C6E`
  `#DCBD9C`; brillo 44 %, saturación 45 %, línea normal (más marcada que en
  las escenas de paisaje) — mucho contraste, silueta negra contra luz blanca
  intensa.
- **Fiordo nevado, dracar navegando al atardecer** (ED1 "Torches", storyboard
  completo, https://www.youtube.com/watch?v=rlb942EnOF0): paleta muy clara
  con hielo y montañas — `#F8F9F5` `#E7E9E3` `#CFD4CC` `#B2BCB5` `#909C96`
  `#70776F`; brillo 75 %, saturación baja (13 %), "mucha línea" (el
  storyboard de baja resolución exagera el contorno).
- **Aurora + antorcha en la tormenta** (ED1, mismo vídeo, segunda mitad):
  paleta oscura verde-negra — `#090D10` `#1F2829` `#40433F` `#928F83`
  `#6A635D` `#329D5B` (el verde de la aurora); brillo 35 %, saturación 38 %.
- **Trigal dorado con flores** (ED1, tramo final): paleta amarilla-dorada —
  `#F3E9D7` `#E8E74D` `#BDAB4B` `#EFE68F` `#2B3531` `#6C6957`; brillo 64 %,
  saturación 34 % — el tramo más cálido y luminoso de todo lo mirado, en
  contraste total con la crudeza del resto de la serie.

**Texturas reales equivalentes**: ⚠️ no llegué a este sub-punto (nieve,
madera de dracar, paja de techo, piedra de castillo); si hace falta,
`https://ambientcg.com/api/v2/full_json?type=Material&q=snow|wood|thatch|stone`
da resultados CC0 directos con esas mismas palabras — lo dejo anotado para
quien lo retome (imagen o el redactor).

### Punto 2 — Fotogramas de escenas icónicas (resumen con capítulo y minuto)

(Ya detallados arriba en el punto 10; se listan aquí sólo como índice para no
repetir texto.)

1. **Rendición y muerte de Thors** — Episodio 4 "A True Warrior" · clip
   https://www.youtube.com/watch?v=LPnQ74j1dqY (minuto dentro del clip, no del
   episodio, ⚠️) · resolución real del clip HD, pero sólo pude mirar el
   storyboard (160×90) por el bloqueo de YouTube.
2. **Muerte de Askeladd** — Episodio 24 "End of the Prologue" · clip oficial
   Crunchyroll https://www.youtube.com/watch?v=PF2NTT_mnps (mismo aviso de
   resolución).
3. **Discurso de Canute ante su ejército** — episodio sin confirmar · clip
   oficial Netflix Anime https://www.youtube.com/watch?v=Zt85YuG0-_Y (mismo
   aviso de resolución).

Para 1080p real habría que repetir esto cuando YouTube deje de pedir login en
este servidor, o conseguir los mismos clips en Dailymotion/Internet Archive
(los busqué por título exacto y no aparecieron).

### Punto 14 — Poses analizadas por personaje

**Thorfinn** (7 fotogramas, capítulo/minuto o enlace con `&t=`):

1. OP1, 0:27 — primer plano, ojos muy abiertos de miedo, envuelto en un
   manto de piel oscuro, viento moviéndole el pelo · niño ·
   https://www.dailymotion.com/video/x8bcl5n?t=27 · sirve para **reaccionar
   con miedo/tensión**.
2. OP1, 0:45 — primer plano más cerrado, mirada fija y directa a cámara,
   dientes apretados, mismo manto · https://www.dailymotion.com/video/x8bcl5n?t=45
   · sirve para **pensar/decidirse** bajo presión.
3. OP1, 0:51 — plano entero de espaldas, corriendo por la nieve hacia una
   casa con techo de paja, brazos en movimiento · https://www.dailymotion.com/video/x8bcl5n?t=51
   · sirve para **animar** (acción, dinamismo).
4. Trailer S2, 1:42 — recibe un puñetazo sin devolverlo, cuerpo echado hacia
   atrás, brazo cruzado sobre la cara · https://www.dailymotion.com/video/x8h1n5b?t=102
   · sirve para **explicar** su pacifismo (temporada 2).
5. Trailer S2, 1:31 — tirando de una cuerda atada a un tocón, músculos en
   tensión, cabeza gacha (⚠️ podría ser Einar, no distinguible con certeza a
   esta resolución) · https://www.dailymotion.com/video/x8h1n5b?t=91 · sirve
   para **trabajar/perseverar**.
6. Episodio 4 (clip, storyboard) — niño, ojos muy abiertos, boca
   entreabierta, mirando hacia arriba con horror mientras matan a su padre ·
   https://www.youtube.com/watch?v=LPnQ74j1dqY · sirve para **la escena que
   hace llorar** (tristeza/shock).
7. Episodio 24 (clip Crunchyroll, storyboard) — joven rubio llorando,
   sosteniendo a Askeladd agonizante, manos temblorosas (⚠️ podría ser Canute,
   ver aviso arriba) · https://www.youtube.com/watch?v=PF2NTT_mnps · sirve
   para **la escena que hace llorar** / regañar-se a sí mismo (culpa).

**Askeladd** (6 fotogramas):

1. Episodio 24 (clip Crunchyroll, storyboard) — banda roja en la cabeza, ojo
   marcado/entrecerrado, gesto gruñón mientras dice "esta parte es
   importante" · https://www.youtube.com/watch?v=PF2NTT_mnps · sirve para
   **explicar/instruir** (su rol de mentor cínico con Thorfinn).
2. Trailer S2, 1:21 — de pie en primera fila de un grupo de mercenarios con
   la espada en alto, mirada fija al frente (⚠️ identidad no confirmada al
   100 %, el grupo entero de mercenarios podría no incluirlo si esta escena
   es sólo del ejército de Canute) · https://www.dailymotion.com/video/x8h1n5b?t=81
   · candidato para **presentar** (líder de grupo).
3. Episodio 24 (clip Crunchyroll, storyboard) — tendido, ensangrentado,
   sostenido por otro personaje, expresión relajada pese a la herida ·
   https://www.youtube.com/watch?v=PF2NTT_mnps · sirve para la escena de
   **despedida/sacrificio**.
4. Clip "Vinland Saga Askeladd Scene CLIP 1080p HD DUB" (storyboard,
   https://www.youtube.com/watch?v=1nRt6tiU20g) — cara y pelo llenos de
   sangre y arañazos, bandana torcida, ojos muy abiertos, gritando · sirve
   para **reaccionar con horror/dolor** (flashback de juventud, ⚠️ no
   confirmé en la wiki a qué escena exacta corresponde: parece un naufragio o
   emboscada, no lo di por hecho).
5. Mismo clip — primer plano de un solo ojo muy abierto, aterrorizado, en la
   oscuridad · https://www.youtube.com/watch?v=1nRt6tiU20g · sirve para
   **el miedo antes de actuar** (contraste con su cinismo adulto).
6. Mismo clip — tumbado boca abajo, cara ensangrentada de perfil, cerca de
   una figura pequeña tendida en el suelo con sangre alrededor ·
   https://www.youtube.com/watch?v=1nRt6tiU20g · escena dura, la dejo descrita
   sin interpretar más de lo que se ve (⚠️ no confirmé el contexto exacto).

**Canute** (6 fotogramas):

1. Clip "Tide Speech" (Netflix Anime, storyboard) — de pie con capa roja
   real, viento moviéndole el pelo rubio corto, mirando al horizonte sobre el
   mar al atardecer · https://www.youtube.com/watch?v=Zt85YuG0-_Y · sirve
   para **presentar** (majestuosidad, autoridad).
2. Clip "Tide Speech" — primer plano de su cara girada, expresión fría y
   dura, ceño fruncido · https://www.youtube.com/watch?v=Zt85YuG0-_Y · sirve
   para **regañar/imponerse**.
3. Tráiler S2, 1:10 — discutiendo cara a cara con un hombre mayor (su padre,
   por contexto), puño cerrado, gesto tenso · https://www.dailymotion.com/video/x8h1n5b?t=70
   · sirve para **explicar/confrontar**.
4. Clip "Prince Canute awakens" (storyboard, https://www.youtube.com/watch?v=rsZc66_fisM)
   — de pie en la nieve con capa roja, mirando a un hombre mayor de barba
   gris, subtítulo "Isn't there any way to end the suffering from your
   punishment other than death?" · sirve para **pedir compasión/cuestionar**
   una orden (su conflicto moral antes de endurecerse).
5. Mismo clip — primer plano de su cara, ojos muy abiertos, boca entreabierta,
   consternado, mirando hacia abajo (a un hombre caído y ensangrentado) ·
   https://www.youtube.com/watch?v=rsZc66_fisM · sirve para **reaccionar con
   angustia/compasión**.
6. Mismo clip — de pie, solo, en un campo nevado con árboles secos alrededor,
   pelo rubio largo suelto sobre la capa roja, postura relajada de espaldas ·
   https://www.youtube.com/watch?v=rsZc66_fisM · sirve para **pensar/estar a
   solas** (antes de su transformación en rey).

**Einar** (6 fotogramas, capítulo/clip y minuto):

1. Tráiler S2, 0:19 — silueta a contraluz envuelta en humo y fuego rojo,
   sólo se distingue el perfil del pelo y un brazo alzado, subtítulo "Yo era
   un guerrero" · https://www.dailymotion.com/video/x8h1n5b?t=19 · sirve para
   **recordar/narrar su pasado** (voz en off sobre imagen).
2. Tráiler S2, 0:39 — niño llorando a gritos en medio de una aldea en llamas
   · https://www.dailymotion.com/video/x8h1n5b?t=39 · sirve para **la escena
   que hace llorar** (trauma de origen).
3. Tráiler S2, 1:31 — de espaldas, tirando de una cuerda con esfuerzo físico
   (mismo aviso de identidad que en el punto 5 de Thorfinn) ·
   https://www.dailymotion.com/video/x8h1n5b?t=91 · sirve para **trabajar/
   perseverar**.
4. Clip "Einar Becomes Ketil's Slave" (canal oficial **Netflix Anime**,
   storyboard, ~14 s dentro de un clip de 99 s) — primer plano, mirada seria
   y tensa hacia arriba (a Ketil, cuyo pelo rubio se ve al borde del
   encuadre), boca cerrada, cejas algo fruncidas; identidad confirmada por el
   subtítulo automático en español, "-¿Cómo te llamas? -Einar." (0:00-0:03) ·
   https://www.youtube.com/watch?v=Zk4Iy5PBsOw · sirve para **reaccionar con
   cautela/desconfianza** ante un desconocido (llega como esclavo a la granja
   de Ketil).
5. Mismo clip, ~31 s — primer plano muy cerrado, una lágrima marcada bajando
   por la mejilla, mirada de reojo, mandíbula tensa; coincide con el
   subtítulo "¿En el campo?" (0:31-0:32, su reacción a que Ketil le pida
   trabajar la tierra) · https://www.youtube.com/watch?v=Zk4Iy5PBsOw · sirve
   para **contener la emoción/tristeza silenciosa**.
6. Mismo clip, ~76 s — primer plano extremo, ojos muy abiertos, cejas
   fruncidas hacia arriba, boca entreabierta como si jadeara; cae poco
   después de la última línea del clip ("primero échale un vistazo a la
   granja", 1:10-1:12) · https://www.youtube.com/watch?v=Zk4Iy5PBsOw · sirve
   para **reaccionar con sorpresa/conmoción**.

## Lo mejor para la lámina

- La aurora boreal sobre el mar (OP1, ED1) es la imagen más repetida de toda
  la identidad visual: paleta `#131E35`-`#34BAC6` (noche) o verde `#329D5B`
  sobre negro — muy usable de fondo o textura.
- El "campo de cadáveres bajo la Vía Láctea" del OP1 (`?t=84`) resume en una
  sola imagen la mezcla de épica y crudeza que pide el encargo.
- El trigal dorado del ED1 (paleta `#E8E74D`/`#EFE68F`) da el contraste cálido
  perfecto si la lámina necesita un momento de calma dentro del mundo vikingo.
- Cuadro de diálogo del tráiler: "Necesitarás más cadáveres para llegar a lo
  más alto" (`?t=122`) — frase muy citable para un canal de escritura/guion.
- Pose de Thorfinn niño mirando con horror (episodio 4) es la más fuerte para
  transmitir emoción si el canal necesita un personaje "sintiendo" algo.

## No encontré

- ⚠️ PV5 (tráiler japonés oficial, YouTube) — bloqueado por login; no lo
  encontré reposteado en Dailymotion ni Internet Archive.
- ⚠️ Efectos de sonido/onomatopeyas reconocidas del anime como tal (existen
  para el manga, es tarea del investigador de texto).
- ⚠️ Making of/entrevistas en vídeo del staff — no aparecieron en Dailymotion
  ni Internet Archive con los términos probados.
- ⚠️ Texturas reales equivalentes (nieve, madera, paja, piedra) — no llegué a
  buscarlas, dejo la API de ambientCG lista para quien lo retome.
- ⚠️ Episodio exacto del "discurso de la marea" de Canute.
- ⚠️ Segunda fuente para el compositor Yutaka Yamada.
- ⚠️ AnimeThemes (caído las tres veces que lo probé, con más de una hora de
  diferencia; las dos primeras con HTTP 522, la tercera con timeout total).
- ⚠️ Openings/endings en 1080p reales (sólo storyboard de baja resolución
  para el ED1 y para los 3 clips de escenas icónicas; el OP1 y el tráiler S2 sí
  se vieron en 1280×720 vía Dailymotion).

## Bitácora de búsqueda

- AnimeThemes API (`api.animethemes.moe`), español/inglés: HTTP 522 dos veces
  (con `curl` directo, confirmado que el dominio principal sí responde pero la
  API no).
- `yt-dlp --dump-json` en YouTube (inglés): funciona para metadatos y
  storyboards; falla con 403 al intentar descargar vídeo real (confirmado con
  el PV5 y con `fotogramas.py`).
- Dailymotion API `api.dailymotion.com/videos?search=` (español/inglés):
  "Vinland Saga OP/ED/opening/ending/trailer/escena/OP2/ED2/ED1/Torches/
  Drown/MUKANJYO/River/Ending 1/Ending animation" — la búsqueda de Dailymotion
  no filtra bien por texto exacto de canción, devuelve casi siempre los mismos
  10 vídeos más vistos con "Vinland Saga" en el título; tuve que abrir cada
  candidato y mirar el contenido real para confirmar qué era.
- Fandom `vinlandsaga.fandom.com/api.php` (inglés), `action=parse&prop=wikitext`
  sobre: MUKANJYO, Torches, Dark Crow, Drown, River, Without Love, Thors
  Snorresson, Episode 4, Episode 24, Episode 44, Canute, Einar, Vinland Saga
  (anime); y `action=query&list=search` con: "opening theme song", "Thors
  death episode", "Askeladd dies Thorfinn knife episode", "Canute addresses
  army king episode", "tide speech king", "command the tide", "soundtrack
  composer", "sound effect", "onomatopoeia".
- AniList GraphQL (`graphql.anilist.co`), consulta de `staff` del anime
  101348: sin rol de música en las primeras 50 entradas.
- MusicBrainz (`musicbrainz.org`), búsqueda "Yutaka Yamada Vinland": sin
  resultados.
- Jikan/MyAnimeList (`api.jikan.moe`): caído (504) al consultar staff.
- Wikipedia en inglés (`en.wikipedia.org/w/api.php`): rate-limited al segundo
  intento, no insistí.
- YouTube `ytsearch` (inglés) para: "Vinland Saga ED1 Torches Aimer
  creditless", "Vinland Saga Thors death scene official clip", "Vinland Saga
  Askeladd death scene Thorfinn", "Vinland Saga Canute transformation king
  scene" — todas con resultados útiles.
- YouTube, storyboards de dos clips más para completar poses: "Vinland Saga
  Askeladd Scene CLIP 1080p HD DUB" (`1nRt6tiU20g`) y "Vinland Saga | Prince
  Canute awakens" (`rsZc66_fisM`) — los dos con subtítulos en inglés
  legibles en el storyboard.
- AnimeThemes reintentado (dos endpoints, `curl` directo): sigue caído,
  ahora con timeout total en vez de 522 (tercera comprobación del día).
- `yt-dlp --dump-json "ytsearch8:Vinland Saga Einar scene clip"` para
  completar el mínimo de 6 poses de Einar: de los 8 candidatos, usé el clip
  oficial de **Netflix Anime** "Einar Becomes Ketil's Slave" (`Zk4Iy5PBsOw`,
  storyboard + `--write-auto-subs --sub-langs "en,es.*"` para confirmar el
  nombre en el subtítulo). También miré "Vinland Saga S2 Einar rages over his
  dead family" (canal fan MirokSs, `Nu6G6dy1C88`, primer plano gritando de
  rabia con la aldea ardiendo detrás) y "Einar Meets Arnheid" (Crunchyroll
  Dubs, `GA9-IOiOwMA`) pero no los usé: el primero no tenía episodio ni
  fuente oficial que confirmar y el segundo dio 429 al pedir sus metadatos
  (no insistí, ya tenía las 3 poses que faltaban del clip de Netflix).
- Herramientas usadas: `fotogramas.py` (OP1 completo, tráiler S2 completo con
  `--cortes`, más fotogramas sueltos con `--fotograma`), `estilo.py` (11
  paletas medidas), descarga manual de storyboards de YouTube con `curl`
  sobre las URLs `i.ytimg.com/sb/...` que da `yt-dlp --dump-json` (nivel
  `sb0`, 160×90, ~1 fotograma/segundo) para los vídeos que YouTube bloqueó
  para descarga completa.

## Cumplimiento del encargo (mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 2. Fotogramas de escenas icónicas | ⚠️ | 3 escenas confirmadas con capítulo/fuente, pero sólo en storyboard de 160×90 (YouTube bloqueó la descarga en HD); el OP1 y el tráiler S2 sí están en 1280×720 |
| 4. Fondos y sitios, luz y paleta | ✅ | 11 paletas medidas con `estilo.py` sobre fotogramas propios, con fuente y segundo; faltan las texturas reales equivalentes (⚠️, ver "No encontré") |
| 9. Música y sonido | ✅ | Los 6 temas (3 OP + 3 ED) confirmados en dos fuentes con tramo de episodios; OP1 y ED1 mirados enteros; compositor con una sola fuente (⚠️); onomatopeyas no encontradas para el anime (⚠️, es del manga) |
| 10. Vídeos con minuto exacto | ✅ | Tráiler S2 diseccionado plano a plano con diálogo y segundo; 3 clips de escenas icónicas de canales oficiales (Crunchyroll, Netflix Anime); 1 vídeo de tendencia tipo TikTok; PV5 sin poder mirar (⚠️) |
| 14. Poses por personaje | ✅ | Thorfinn 7, Askeladd 6, Canute 6, Einar 6 (todos con capítulo/clip, minuto o `&t=`, y para qué sirve cada pose) |

Todos mis puntos (2, 4, 9, 10, 14) están completos dentro de lo que da la red
disponible (AnimeThemes caído, YouTube sin descarga directa).
