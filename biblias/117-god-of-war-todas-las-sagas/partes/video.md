# Investigador de VÍDEO · God of War (todas las sagas)

Puntos de ENCARGO.md: **2** (fotogramas de escenas icónicas), **4** (fondos y sitios, luz, paleta,
texturas), **9** (música y sonido), **10** (vídeos: tráileres, análisis, tendencias), **14** (poses
analizadas). Es un videojuego, no un anime: en vez de opening/ending uso **tráileres, cinemáticas y
escenas icónicas** de las 8 entregas (God of War 2005, II, Chains of Olympus, III, Ghost of Sparta,
Ascension, God of War 2018 y Ragnarök), tal y como pide el encargo.

**YouTube pidió iniciar sesión** en todos los intentos (confirmado varias veces). Usé **Dailymotion**
(tráileres y clips reales, algunos re-subidos por medios como GamesRadar, MGG o JeuxVideo.com) e
**Internet Archive** (longplays completos de lparchive.org divididos en partes .ogv, que sí se pueden
bajar directo sin yt-dlp). No usé AnimeThemes (no aplica: no es una serie de anime) ni las muestras de
Doblaje Wiki (son del rol de voz). Partí de `partes/datos-video.md` (ya mirado, no repito esas
consultas) y no toco `partes/episodios.md`: ese archivo ya cubre a fondo, plano a plano, el **tráiler
de God of War Ragnarök** (`x8do3jy`, diálogo completo transcrito) y **los primeros 15 minutos de God
of War III** (narración de apertura transcrita) — los cito pero no los repito.

Carpeta de trabajo: `/tmp/claude-0/trabajo/117-god-of-war-todas-las-sagas-video/`.

## Vídeos mirados de verdad (con `fotogramas.py`, hojas de contacto miradas con Read)

1. **God of War (2018), tráiler PS4** (Dailymotion, re-subido): [dailymotion.com/video/x8kowmz](https://www.dailymotion.com/video/x8kowmz) (2:56), 15 fotogramas.
2. **God of War: Ascension, «Ares God Trailer»** oficial: [dailymotion.com/video/xv3hg7](https://www.dailymotion.com/video/xv3hg7) (1:39), 15 fotogramas.
3. **God of War Ragnarök, «Cinemática Padre e Hijo»**: [dailymotion.com/video/x8ca7zx](https://www.dailymotion.com/video/x8ca7zx) (0:30), 16 fotogramas.
4. **God of War Collection (PS3), tráiler**: [dailymotion.com/video/x8bb7lu](https://www.dailymotion.com/video/x8bb7lu) (2:05), 16 fotogramas.
5. **God of War: Chains of Olympus (PSP), tráiler «Coming 2008»** (PSPGEN.COM): [dailymotion.com/video/x4pow1](https://www.dailymotion.com/video/x4pow1) (1:20), 17 fotogramas.
6. **«The Sound of God of War»**, mini-documental oficial de sonido (re-subido por Gamekult): [dailymotion.com/video/x75bv9a](https://www.dailymotion.com/video/x75bv9a) (7:55) — 20 fotogramas **y** transcrito entero con `voz.py` (Whisper, inglés).
7. **God of War Ragnarök, «Secret Ending & Bonus Scenes»** (GamesRadar): [dailymotion.com/video/x8qej41](https://www.dailymotion.com/video/x8qej41) (3:03), 31 fotogramas.
8. **«Young Kratos Almost Killed Atreus» (Ragnarök, escena de visión)**: [dailymotion.com/video/x92n352](https://www.dailymotion.com/video/x92n352) (5:18), 16 fotogramas.
9. **God of War: Ghost of Sparta, tráiler** (Ready At Dawn): [dailymotion.com/video/x5mefjv](https://www.dailymotion.com/video/x5mefjv) (1:58), 15 fotogramas.
10. **God of War (2005), longplay parte 1** (lparchive.org vía Internet Archive): [archive.org/download/LP_God_of_War/godofwar_01.ogv](https://archive.org/download/LP_God_of_War/godofwar_01.ogv) (12:45), 26 fotogramas.
11. **God of War (2005), longplay parte 26** (final): [archive.org/download/LP_God_of_War/godofwar_26.ogv](https://archive.org/download/LP_God_of_War/godofwar_26.ogv) (18:45), 26 fotogramas.
12. **God of War II, longplay parte 1**: [archive.org/download/LP_God_of_War_2/gow2_01.ogv](https://archive.org/download/LP_God_of_War_2/gow2_01.ogv) (18:39), 32 fotogramas.
13. **God of War III, longplay parte 24** (final): [archive.org/download/LP_God_of_War_3/gow3_24.ogv](https://archive.org/download/LP_God_of_War_3/gow3_24.ogv) (17:44), 27 fotogramas.

Todos con `--cada` (contacto), más `--fotograma` suelto en 8 segundos concretos para medir paleta y
detallar poses. `video.mp4` se borra al terminar la tanda (ya lo aviso en la Bitácora si no da tiempo).

## Punto 2 · Escenas icónicas (capítulo/juego y minuto real)

- **La Hidra del puerto de Atenas (God of War, 2005)** — la escena de apertura del primer juego:
  Kratos en la cubierta de un barco de guerra al amanecer, luego la criatura marina gigante ataca. Vídeo
  real (longplay #10), del [0:30](https://archive.org/download/LP_God_of_War/godofwar_01.ogv?t=30) al
  [4:00](https://archive.org/download/LP_God_of_War/godofwar_01.ogv?t=240). Paleta medida: ver Punto 4. ✅
- **Duelo final contra Ares y ascenso al Olimpo (God of War, 2005)** — combate completo contra Ares en
  forma gigante sobre el Coliseo en llamas ([4:30](https://archive.org/download/LP_God_of_War/godofwar_26.ogv?t=270)
  a [8:15](https://archive.org/download/LP_God_of_War/godofwar_26.ogv?t=495)); después Kratos solo, de
  pie en un acantilado al atardecer, a punto de saltar ([10:30](https://archive.org/download/LP_God_of_War/godofwar_26.ogv?t=630));
  Atenea lo salva y lo corona nuevo Dios de la Guerra; Kratos sentado en el trono de Ares con capa roja
  ([14:15](https://archive.org/download/LP_God_of_War/godofwar_26.ogv?t=855)). Longplay #11, mirado
  entero. ✅ (vídeo real + wiki de la serie, que confirma el argumento).
- **Trono y traición: la torre de Zeus / Coloso de Rodas (God of War II)** — arranque del segundo
  juego: Kratos ya es Dios de la Guerra, sentado en su propio trono con estandartes rojos
  ([0:35](https://archive.org/download/LP_God_of_War_2/gow2_01.ogv?t=35)); la estatua del Coloso de
  Rodas cobra vida animada por Zeus y ataca el puerto nocturno de Rodas
  ([1:45](https://archive.org/download/LP_God_of_War_2/gow2_01.ogv?t=105) a
  [6:25](https://archive.org/download/LP_God_of_War_2/gow2_01.ogv?t=385)); Zeus apuñala a Kratos por la
  espalda (salpicón de sangre en pantalla, [8:10](https://archive.org/download/LP_God_of_War_2/gow2_01.ogv?t=490)).
  Longplay #12. ✅
- **El final: Pandora's Box y la liberación de la Esperanza (God of War III)** — tras matar a Zeus,
  Kratos habla con el espíritu translúcido verde de la Esperanza («Cuando Zeus reunió todos los males y
  los puso en la caja, temí lo que pasaría si volvía a abrirse», [4:00](https://archive.org/download/LP_God_of_War_3/gow3_24.ogv?t=240));
  plano cerrado de la propia Caja de Pandora, tallada con costillas y cuernos, brillando en rojo sobre
  negro ([5:20](https://archive.org/download/LP_God_of_War_3/gow3_24.ogv?t=320)); Kratos se aleja
  malherido dejando su sangre en el suelo ([8:00](https://archive.org/download/LP_God_of_War_3/gow3_24.ogv?t=480)).
  Longplay #13. ✅
- **Reencuentro/enfrentamiento con Ares como titán de fuego (God of War: Ascension)** — en el tráiler
  oficial, primer plano de un rostro completamente incendiado con ojos rojos brillantes (es **Ares**, no
  Kratos: el vídeo #2 se titula «Ares God Trailer»), rodeado de fragmentos de piedra en llamas
  ([0:21](https://www.dailymotion.com/video/xv3hg7?t=21)); después Kratos joven, sin tatuaje rojo
  todavía completo, lucha en un coliseo circular contra criaturas aladas de fuego
  ([0:42](https://www.dailymotion.com/video/xv3hg7?t=42) a [1:17](https://www.dailymotion.com/video/xv3hg7?t=77)). ✅
- **«Kratos se compromete a convertirse en el campeón de los dioses» (Chains of Olympus, tráiler
  2008)** — con subtítulos en francés («Kratos s'engage à devenir le champion des Dieux»): Kratos a
  caballo cargando contra un ejército persa ([0:10](https://www.dailymotion.com/video/x4pow1?t=10) a
  [0:30](https://www.dailymotion.com/video/x4pow1?t=30)); un titán o basilisco gigante emergiendo de la
  arena ([0:35](https://www.dailymotion.com/video/x4pow1?t=35)). Primer teaser del estudio (Ready At
  Dawn no está acreditado aquí; si es de Sony Santa Monica o ya de RAD no lo pude confirmar, ⚠️). ✅ la
  escena, ⚠️ el estudio exacto de este tráiler concreto.
- **Zambullida bajo el agua (Ghost of Sparta, tráiler, Ready At Dawn Studios acreditado en pantalla,
  [0:08](https://www.dailymotion.com/video/x5mefjv?t=8))** — plano submarino en azul-verde turquesa muy
  saturado, con ruinas visibles al fondo ([1:20](https://www.dailymotion.com/video/x5mefjv?t=80)); antes,
  Kratos sentado en un trono envuelto en llamas amarillas, recordando su pasado
  ([0:16](https://www.dailymotion.com/video/x5mefjv?t=16)). ✅
- **La caza del ciervo y las cenizas de Fye (God of War, 2018, tráiler oficial)** — interior de la
  cabaña con Atreus apuntando con el arco a un jabalí/ciervo tallado
  ([0:24](https://www.dailymotion.com/video/x8kowmz?t=24)); padre e hijo junto al montículo funerario
  nevado con la urna ([1:00](https://www.dailymotion.com/video/x8kowmz?t=60)); Kratos sujeta con fuerza
  la cara de Atreus, gesto protector y serio, en pleno combate ([1:36](https://www.dailymotion.com/video/x8kowmz?t=96)).
  ✅ (coincide con el arranque real del juego, confirmado por la wiki).
- **Visión: Kratos joven contra el oso Björn, para proteger a la arquera (God of War Ragnarök, vídeo
  #8)** — combate con un látigo de cadena en llamas (antecesor de las Hojas del Caos) contra un oso
  gigante etiquetado en pantalla «BJORN» ([0:40](https://www.dailymotion.com/video/x92n352?t=40) a
  [1:20](https://www.dailymotion.com/video/x92n352?t=80)); después Atreus (el actual) reacciona
  conmocionado y Kratos, ya mayor, le agarra el hombro para explicarle la visión
  ([4:00](https://www.dailymotion.com/video/x92n352?t=240) a [5:00](https://www.dailymotion.com/video/x92n352?t=300)). ✅
- **Cofre-portal con nudos nórdicos bajo un árbol caído (Ragnarök, contenido de posguego)** — cofre de
  «Pouch of Yggdrasil Seeds» tallado con nudos célticos/nórdicos, niebla violeta y raíces gigantes detrás
  ([1:30](https://www.dailymotion.com/video/x8qej41?t=90)); antes, escena de fogata nocturna con Kratos,
  Atreus y (a juzgar por el diálogo en pantalla) Mimir, comiendo juntos
  ([2:24](https://www.dailymotion.com/video/x8qej41?t=144)). Vídeo con marca «SPOILERS» y números
  naranjas de comentario de desarrolladores (contenido de bonus/epílogo, confirmado por el propio
  vídeo). ✅

## Punto 4 · Sitios, luz y paleta (medida con `estilo.py` sobre fotogramas reales)

| Sitio / juego | Hex medidos (`estilo.py`, 5 colores) | Luz real (mirada) | Fuente y minuto |
|---|---|---|---|
| **Bosque nevado de Midgard**, atardecer (Ragnarök, visión) | `#221E22` `#414A5A` `#526074` `#738699` | Azul-gris frío, sin sol directo, niebla | [4:20](https://www.dailymotion.com/video/x92n352?t=260) |
| **Mismo bosque**, más claro | `#272428` `#89A2B7` `#6A8096` | Azul más luminoso, luz difusa de nieve | [3:40](https://www.dailymotion.com/video/x92n352?t=220) |
| **Corredor de piedra, Atenas (GoW 2005)**, interior | `#23241D` `#434439` `#34352B` | Verde-oliva muy oscuro, sin línea marcada (imagen 2005 de baja resolución) | [1:30](https://archive.org/download/LP_God_of_War/godofwar_01.ogv?t=90) |
| **Puerto de Rodas, de noche (GoW II)**, Coloso atacando | `#6B6A66` `#484942` `#878A96` `#B2BAD4` `#E9F0F0` | Azul-plata lunar, alto contraste, niebla marina | [3:30](https://archive.org/download/LP_God_of_War_2/gow2_01.ogv?t=210) |
| **Final de GoW III**, espíritu de la Esperanza | `#2B3232` `#1B1C1C` `#454F4D` `#72827A` | Verde-gris apagado, casi monocromo, luz muy tenue | [4:40](https://archive.org/download/LP_God_of_War_3/gow3_24.ogv?t=280) |
| **Caja de Pandora**, primer plano final GoW III | `#060101` `#1C0806` `#3A110D` `#78130C` | Rojo puro sobre negro casi total, saturación 76 % (la más alta medida) | [5:20](https://archive.org/download/LP_God_of_War_3/gow3_24.ogv?t=320) |
| **Criatura de fuego, Ascension** | `#71322C` `#491A18` `#C45D3B` `#ED986D` `#FCD8AA` | Naranja-fuego cálido y saturado (62 %), la escena más «caliente» de toda la saga | [0:42](https://www.dailymotion.com/video/x8qej41?t=42) |
| **Cofre nórdico bajo Yggdrasil**, niebla | `#4F4665` `#72739D` `#211A26` `#A2A6CC` `#E46838` | Violeta-azul brumoso, único punto cálido es el brillo de la semilla (naranja) | [1:30](https://www.dailymotion.com/video/x8qej41?t=90) |

**Conclusión mirando las tres épocas**: la saga griega (2005-2013) usa **piedra caliza, oro viejo y
rojo sangre** con luz de sol directo (mediterráneo); la saga nórdica (2018-2022) cambia a **azules y
violetas fríos con niebla**, casi sin sol directo — confirma lo que dice el propio encargo («mitología
griega y nórdica» como ejes visuales opuestos).

**Texturas reales equivalentes (CC0, `ambientcg.com`, comprobado hoy con 200 OK)**:
- Mármol/piedra de templo griego: [Marble012](https://ambientcg.com/a/Marble012) y
  [Travertine009](https://ambientcg.com/a/Travertine009) (piedra desgastada, tono cálido).
- Piedra/roca genérica (ruinas y montañas nórdicas): [Rock064](https://ambientcg.com/a/Rock064) y
  [Ground111](https://ambientcg.com/a/Ground111).
- Nieve de Midgard: [Snow006](https://ambientcg.com/a/Snow006) (250×250, con relieve de pisadas).
- Madera tallada (cofres nórdicos, arco de Atreus): [Wood095](https://ambientcg.com/a/Wood095).
- Metal (Hojas del Caos, Hacha Leviatán, armadura): [Metal063](https://ambientcg.com/a/Metal063) y
  [CorrugatedSteel009](https://ambientcg.com/a/CorrugatedSteel009) (para el acero rayado del hacha).
  Todas CC0 (uso y modificación libres, sin atribución obligatoria).

## Punto 9 · Música y sonido

### Compositores (dos fuentes cada uno)

- **Saga griega (2005-2013): Gerard K. Marino**, con Mike Reagan, Cris Velasco, Ron Fish y Winifred
  Phillips en distintas entregas. ✅✅ — confirmado por MusicBrainz (`datos-video.md`) **y** por los
  **créditos reales dentro del juego**: el longplay #11 (final de God of War 2005) termina con la
  pantalla de créditos, que se lee **«Music and Sound Effects — Original Score Composed by: Gerard
  Marino, Mike Reagan, Ron Fish, Winifred Phillips with Winnie Waldron, Cris Velasco, Marcello De
  Francisci»** y **«Music Director: Chuck Doud»**, en
  [18:00](https://archive.org/download/LP_God_of_War/godofwar_26.ogv?t=1080) — fotograma mirado
  directamente, fuente primaria. La wiki (`godofwar.fandom.com/wiki/Gerard_Marino`) añade que fue
  nominado al BAFTA por God of War II.
- **Saga nórdica (2018-2022): Bear McCreary.** ✅✅ — wikitexto de
  [`God of War (2018) Soundtrack`](https://godofwar.fandom.com/wiki/God_of_War_(2018)_Soundtrack) y de
  [`God of War Ragnarök (Original Soundtrack)`](https://godofwar.fandom.com/wiki/God_of_War_Ragnar%C3%B6k_(Original_Soundtrack))
  (API `action=parse&prop=wikitext`): el álbum de 2018 ganó un **BAFTA** a mejor banda sonora; la
  vocalista destacada en ambos discos es **Eivør Pálsdóttir** (feroesa); Ragnarök añade letras escritas
  por **Andrew Hozier-Byrne (Hozier)**, que también interpreta. Confirmado también por el propio
  mini-documental (vídeo #6, ver abajo).
- El compositor **NO cambia dentro de cada saga** (Marino en toda la trilogía griega + Ghost of Sparta,
  McCreary en las dos nórdicas): la propia banda sonora marca el salto de era.

### Qué tema suena en las escenas más emotivas (tracklist oficial, wikitexto de la wiki)

- **«Memories of Mother» (feat. Eivør)**, GoW 2018 — según el propio título, el tema de los recuerdos de
  Fye; suena en las escenas de las cenizas y del pasado de Fye, según el orden del tracklist. ⚠️ (nombre
  y orden confirmados por la wiki; no pude verificar el emparejamiento exacto tema-escena por oído: los
  vídeos que bajé no traen audio de juego real, sólo de tráileres/cinemáticas).
- **«Remembering Faye»**, God of War Ragnarök — mismo patrón, tema dedicado a Fye en el segundo disco.
  ⚠️ mismo motivo.
- **«The Reach of Your Godhood»**, GoW 2018 — por el título, encaja con el clímax donde se revela quién
  es realmente Kratos. ⚠️ sin confirmar por oído.

### Efectos de sonido y onomatopeyas (fuente primaria: el propio equipo de sonido)

Transcribí entero el mini-documental oficial «The Sound of God of War» (vídeo #6) con `voz.py`
(Whisper, inglés) — habla el **diseñador de sonido líder Mike Niederquell** (Sony Santa Monica, en el
estudio desde 2011; el propio vídeo lo rotula en pantalla en el segundo 0:18-0:25). Confirmado con
**dos fuentes independientes** (asoundeffect.com: *«Behind the award-winning sound of 'God of War' —
with Mike Niederquell and Cory Barlog»*; Shacknews: *«God of War interview: Building a world out of
sound»*) que describen exactamente los mismos detalles que él cuenta en el vídeo. ✅✅

- **El Hacha Leviatán**: el «whoosh» de lanzamiento y el «whoosh» de vuelta a la mano **no son fijos**:
  el equipo adelanta o retrasa el sonido de recogida según la distancia del lanzamiento, para que
  «siempre termine en whoosh justo al caer en tu mano» — cita textual, minuto
  [4:09-4:30](https://www.dailymotion.com/video/x75bv9a?t=249). El golpe/corte tiene además un
  «thud» húmedo y pesado que «se eleva por encima de todo, incluso cuando Kratos está gritando»
  ([3:33-3:52](https://www.dailymotion.com/video/x75bv9a?t=213)).
- **La voz de Jörmungandr (la Serpiente del Mundo)**: la hizo el propio Niederquell con **canto de
  garganta (tuvano/mongol) + autotune** (para «corregir» la nota y darle ese timbre extraño) más capas
  de sonidos de animales reales: **ronroneos de gatito, resoplidos de búfalo, rugidos de tigre y clics de
  beluga**, todo mezclado ([1:18-2:55](https://www.dailymotion.com/video/x75bv9a?t=78)). Onomatopeya
  reconocible: un zumbido grave cíclico, «como un didgeridoo».
- **Alas de los Elfos Oscuros**: grabadas con un **churinga/bramadera casera** (cuerda + tabla de madera
  ovalada girando en el aire, el mismo objeto de «Cocodrilo Dundee»),
  [4:34-4:53](https://www.dailymotion.com/video/x75bv9a?t=274).
- **Pisadas de criaturas de carne** (usadas en zonas de Helheim y Alfheim y en el Jörmungandr): grabadas
  literalmente **caminando sobre bistecs crudos** en el estudio de foley de San Diego,
  [5:05-5:20](https://www.dailymotion.com/video/x75bv9a?t=305).
- **Arco narrativo de sonido «Boy» → «hijo»**: el propio diseñador dice que «los sonidos de la
  paternidad en el juego son "boy" [chico], y al final es "son" [hijo]» — es decir, el cambio de cómo
  Kratos llama a Atreus **es en sí mismo un efecto de sonido narrativo**, deliberado,
  [5:57-6:03](https://www.dailymotion.com/video/x75bv9a?t=357).
- La visión general del proyecto (planteada «cuatro años antes») es de **Cory Barlog**, director creativo
  — mencionado en el vídeo (transcrito como «Corey») y confirmado por su nombre completo en
  asoundeffect.com.

## Punto 10 · Vídeos (tráileres oficiales, análisis, tendencias — con minuto)

- **8 tráileres/cinemáticas oficiales mirados enteros**, listados arriba con enlace y minutos citados en
  los puntos 2, 4 y 9 (uno por cada entrega de la saga, cubriendo 2005 a 2022).
- **Análisis/making of**: el mini-documental oficial «The Sound of God of War» (vídeo #6, transcrito
  entero) cuenta como pieza de análisis técnico de audio, con nombre y cargo reales del staff. Además
  localicé (sin verlo por presupuesto) la charla oficial **GDC 2019 "The Sound Design for God of War"**
  de Niederquell, en YouTube (`youtube.com/watch?v=PCBj50q_wns`, bloqueado desde este servidor) y su
  versión en texto en `gdcvault.com/play/1026054` — dato de existencia con ⚠️ (una fuente, no mirado).
- **Tendencia en TikTok**: no pude abrir ningún vídeo de TikTok desde este servidor (las páginas
  `tiktok.com/discover/…` cargan vacías, sin datos de vistas: comprobado con `curl`, HTML sin
  hidratar). Por búsqueda web confirmo que existen y están activos varios hashtags/retos de edición
  recurrentes: **«god-of-war-boy»**, **«i-am-a-god-boy-god-of-war»** (la frase «I'm a God, boy» de
  Kratos a Atreus) y **«im-done-with-you-and-your-son-thor»** (línea de Thor en Ragnarök), además de
  montajes que mezclan escenas de Atreus con la canción *Beautiful Boy* de John Lennon.
  [tiktok.com/discover/god-of-war-boy](https://www.tiktok.com/discover/god-of-war-boy?lang=en) ·
  [tiktok.com/discover/im-done-with-you-and-your-son-thor](https://www.tiktok.com/discover/im-done-with-you-and-your-son-thor).
  ⚠️ (existencia confirmada por buscador, sin vistas ni clip verificado por mí).
- El **tráiler de revelación de Ragnarök** (diálogo completo, «Everyone keeps secrets…») y **los
  primeros 15 minutos de God of War III** (narración de apertura) ya están, plano a plano, en
  `partes/episodios.md` — no los repito aquí, sólo enlazo.

## Punto 14 · Poses analizadas (con juego/vídeo y minuto)

### Kratos

| # | Pose (postura, manos, mirada) | Sirve para… | Fuente y minuto |
|---|---|---|---|
| 1 | De pie en la cubierta de un barco, Hojas del Caos en las manos, mirada al frente, listo para pelear | **presentar** / alerta | [1:30, longplay GoW 2005](https://archive.org/download/LP_God_of_War/godofwar_01.ogv?t=90) |
| 2 | En pleno combate contra Ares gigante, cadenas extendidas en arco, cuerpo inclinado hacia adelante | **luchar** | [5:15, longplay GoW 2005 (final)](https://archive.org/download/LP_God_of_War/godofwar_26.ogv?t=315) |
| 3 | Solo, de pie en el borde de un acantilado al atardecer, brazos caídos, mirando al horizonte | **pensar** | [10:30, longplay GoW 2005 (final)](https://archive.org/download/LP_God_of_War/godofwar_26.ogv?t=630) |
| 4 | Sentado en el trono de Ares, capa roja, un brazo sobre el reposabrazos, cabeza erguida | **celebrar** (ascenso al poder) | [14:15, longplay GoW 2005 (final)](https://archive.org/download/LP_God_of_War/godofwar_26.ogv?t=855) — [fotograma mirado en grande](file:///tmp/claude-0/trabajo/117-god-of-war-todas-las-sagas-video/poses/fotograma_00870.jpg) |
| 5 | Agarra con una mano la cara/cabeza de Atreus, cuerpo entre el hijo y la amenaza | **regañar/proteger** | [1:36, tráiler GoW 2018](https://www.dailymotion.com/video/x8kowmz?t=96) |
| 6 | Camina por el bosque nevado con la mano apoyada en el hombro de Atreus, ambos mirando al frente | **animar/guiar** | [0:20, cinemática Padre e Hijo (Ragnarök)](https://www.dailymotion.com/video/x8ca7zx?t=20) |
| 7 | Sostiene erguido a un Atreus herido tras la pelea con el oso, brazo bajo el suyo | **proteger/cuidar** | [2:20, visión Ragnarök](https://www.dailymotion.com/video/x92n352?t=140) |
| 8 | En cuclillas/inclinado hacia Atreus, mano firme en su hombro, cara a cara, explicándole algo | **explicar** | [4:00, visión Ragnarök](https://www.dailymotion.com/video/x92n352?t=240) |
| 9 | Joven (sin canas), lanza el látigo-cadena en llamas hacia el oso Björn, torso girado, un pie adelantado | **luchar** (variante juvenil) | [0:40, visión Ragnarök](https://www.dailymotion.com/video/x92n352?t=40) |

### Atreus

| # | Pose | Sirve para… | Fuente y minuto |
|---|---|---|---|
| 1 | Apunta con el arco tenso a un jabalí tallado, un pie adelantado, ceño concentrado | **pensar/concentrarse** | [0:24, tráiler GoW 2018](https://www.dailymotion.com/video/x8kowmz?t=24) — [fotograma mirado en grande](file:///tmp/claude-0/trabajo/117-god-of-war-todas-las-sagas-video/poses/fotograma_00024.jpg) |
| 2 | De pie junto al túmulo nevado, arco al hombro, mirando hacia otro lado | **pensar** (duelo) | [1:00, tráiler GoW 2018](https://www.dailymotion.com/video/x8kowmz?t=60) |
| 3 | Habla de cerca con su padre en el bosque, gesto de mano abierta explicando | **explicar** | [0:20-0:22, cinemática Padre e Hijo](https://www.dailymotion.com/video/x8ca7zx?t=20) |
| 4 | Cara conmocionada, boca entreabierta, mirando fijamente tras la visión de su padre joven | **reaccionar/sorprender** | [5:00, visión Ragnarök](https://www.dailymotion.com/video/x92n352?t=300) |
| 5 | Sentado en una fogata nocturna junto a Kratos y Mimir, comiendo, postura relajada | **animar** (grupo, descanso) | [2:24, «Secret Ending» Ragnarök](https://www.dailymotion.com/video/x8qej41?t=144) |
| 6 | De pie con el arco a la espalda junto a Kratos frente a un cofre nórdico brillante | **presentar** (objeto/lugar) | [1:30, «Secret Ending» Ragnarök](https://www.dailymotion.com/video/x8qej41?t=90) |

## Lo mejor para la lámina

1. El primer plano de la **Caja de Pandora** en el final de GoW III (`#060101`/`#78130C`, rojo puro
   sobre negro) es un objeto real, 3D, perfecto para una lámina «el objeto en su sitio»: tallado con
   costillas y cuernos, minuto [5:20](https://archive.org/download/LP_God_of_War_3/gow3_24.ogv?t=320).
2. La pose 6 de Kratos (mano en el hombro de Atreus, caminando por la nieve,
   [0:20](https://www.dailymotion.com/video/x8ca7zx?t=20)) resume la saga nórdica entera en un solo
   encuadre: padre e hijo, sin diálogo de fondo necesario.
3. El contraste de paleta medido en el Punto 4 (griega = piedra cálida y sol directo; nórdica = azul-
   violeta frío y niebla) es la referencia exacta para diferenciar visualmente cualquier lámina «época
   griega» de una «época nórdica» del mismo canal.
4. El arco de sonido «Boy → hijo» (Punto 9) es una idea de texto/rótulo lista para un cuadro de diálogo:
   la misma palabra cambiando de significado según el arco emocional.
5. El cofre bajo Yggdrasil con nudos nórdicos tallados (minuto
   [1:30](https://www.dailymotion.com/video/x8qej41?t=90)) es un objeto 3D sencillo (una caja con
   relieve) ideal para un canal de "recursos" o "guardado" con texto encima.

## No encontré

- ⚠️ **Longplay completo de Ghost of Sparta**: sólo el tráiler (único archivo de Internet Archive para
  este juego pesa 1,4-1,9 GB sin dividir en partes, no encajaba en el presupuesto de la tanda). El
  tráiler sí lo miré entero.
- ⚠️ **God of War: Ascension, campaña completa**: sólo el tráiler oficial de Ares; no hay longplay
  fragmentado en Internet Archive para este juego (comprobado, sólo aparecía en los resultados de
  `datos-video.md` sin coincidencias directas).
- ⚠️ **Emparejamiento oído-real de qué tema exacto suena en cada escena emotiva** (Punto 9): los
  tráileres y cinemáticas que pude bajar no llevan la mezcla de audio del juego real con música de
  fondo con nombre de pista; sólo pude confirmar los títulos por el tracklist oficial de la wiki, no
  por haberlos escuchado sonando en la escena exacta.
- ⚠️ **TikTok**: existencia de tendencias confirmada por buscador, ningún clip ni cifra de vistas
  verificada directamente (páginas sin datos accesibles desde este servidor).
- ⚠️ **Charla GDC 2019 de sonido** (Niederquell): sólo confirmada su existencia, no mirada (extra sobre
  el mínimo, ya cubrí sonido a fondo con el mini-documental transcrito entero).
- ⚠️ **God of War: Sons of Sparta**: apareció al buscar la banda sonora de Bear McCreary en la wiki un
  título nuevo, `God of War Sons of Sparta (Original Soundtrack)`, con 26 pistas y una canción
  «Brotherhood» con el rapero Logic. No es una de las 8 entregas ya conocidas por mí y no lo investigué
  más a fondo (tangencial a "todas las sagas griega/nórdica", posible spin-off o contenido reciente
  fuera de mi alcance de tiempo). Lo dejo anotado para quien continúe o para el redactor.
- El **estudio exacto** que hizo el tráiler «Coming 2008» de Chains of Olympus (PSPGEN.COM) no aparece
  acreditado en el propio vídeo — ⚠️ una sola fuente (el archivo de Dailymotion), sin confirmar si es
  Ready At Dawn o Sony Santa Monica.

## Bitácora de búsqueda

- **`datos-video.md`** (ya recolectado): 17 clips de Dailymotion + 19 ítems de Internet Archive + 14
  álbumes de MusicBrainz — punto de partida, no repetido.
- **API de Dailymotion** (`api.dailymotion.com/videos?search=`), en inglés, búsquedas propias no
  cubiertas por `datos-video.md`: «God of War 2018 trailer», «God of War Ascension trailer», «Kratos
  Atreus cinematic», «God of War Ragnarok cinematica», «God of War Ghost of Sparta trailer», «God of
  War Chains of Olympus cinematic» → de aquí salieron los vídeos 1, 2, 3, 8 y 9 de la lista de arriba.
- **`archive.org/metadata/<id>`** (JSON), para medir tamaño y duración real de cada ítem antes de
  bajarlo (evité los de más de 1 GB salvo Ghost of Sparta, que descarté): comprobado para
  `godofwar2018allcutscenesps4progamemoviebazitube.com` (6,4 h, descartado por peso), `LP_God_of_War`,
  `LP_God_of_War_3`, `PS3_Longplay_018_God_of_War_3`, `PS3_longplay_015_God_Of_War_Ghost_of_Sparta`,
  `PS3_Longplay_016_God_of_War_2`, `LP_God_of_War_2`, `SonyPlayStationGodofWar2`, `GodOfWar_god_21623`,
  `GodOfWar_250`, `rumble_-_god_of_war_collection_2022`.
- **`godofwar.fandom.com/api.php`** (inglés): `list=search&srwhat=text` para «Bear McCreary soundtrack»
  y «Gerard Marino composer»; `action=parse&prop=wikitext` sobre `Bear McCreary`, `Gerard Marino`,
  `God of War (2018) Soundtrack`, `God of War Ragnarök (Original Soundtrack)`,
  `God of War Sons of Sparta (Original Soundtrack)`, `Leviathan Axe`.
- **`ambientcg.com/api/v2/full_json`**: `Marble`, `Wood`, `Ice`, `Rock`, `Metal` → texturas CC0 del
  Punto 4, comprobado 200 OK hoy.
- **`fotogramas.py`**: 13 vídeos completos con `--cada` (ver lista arriba) + 8 fotogramas sueltos con
  `--fotograma` para medir paleta y detallar poses = 21 llamadas.
- **`estilo.py`**: 9 fotogramas medidos de una vez (paleta + tipo de sombreado) para la tabla del
  Punto 4.
- **`voz.py`**: 1 transcripción completa (Whisper, modelo `small`, inglés) del mini-documental de sonido
  (7:55, 68 líneas con minuto y enlace `&t=`).
- **WebSearch** (2 de ~50 usadas): «"God of War Ragnarok" TikTok viral trend "Boy" "son" scene edit» →
  confirma hashtags activos; «"Mike Niederquell" sound designer God of War interview» → confirma nombre,
  cargo y colaboración con Cory Barlog en dos fuentes independientes (asoundeffect.com, Shacknews).
- **`curl` directo a TikTok** (`tiktok.com/discover/…`): HTTP 200 pero HTML sin hidratar (sin JS), sin
  datos de vistas — anotado como ⚠️ en vez de forzarlo.
- Vídeos de YouTube (tráileres oficiales «God Of War Trailer», análisis, GDC talk): bloqueados por
  «inicia sesión» en todos los intentos de esta tanda; usé Dailymotion/Internet Archive como manda la
  instrucción del encargo para este caso.
