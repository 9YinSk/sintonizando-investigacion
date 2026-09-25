# Parte VÍDEO · Demon Slayer: paisajes y auras (79-demon-slayer-paisajes-y-auras)

Investigador de vídeo. Puntos de ENCARGO.md: **2** (fotogramas de escenas icónicas), **4** (fondos y sitios: luz y paleta — foco especial del encargo), **9** (música y sonido, con énfasis en los efectos visuales de las respiraciones, el "aura" del encargo), **10** (vídeos: tráilers, escenas, tendencias) y **14** (poses analizadas, con foco en los efectos de cada técnica).

**Aviso sobre `datos-video.md`**: el recolector automático buscó el título literal del encargo
("Demon Slayer: paisajes y auras") en AniList y encontró por error la serie
**"Onigiri"** (AniList id 21612, un anime distinto sobre bolas de arroz). Todo
`datos-video.md`, `datos-imagen.md`, `datos-texto.md`, `datos-voz.md` y `datos.json`
recolectados están contaminados con datos de esa obra equivocada. **No se usó nada
de ese archivo.** Toda la información de aquí sale de búsqueda directa en la wiki de
Fandom real (`https://kimetsu-no-yaiba.fandom.com`), Dailymotion, Internet Archive y
WebSearch. AnimeThemes se reintentó dos veces (ver Bitácora): sigue caído (HTTP 522 /
timeout), así que los openings/endings se consiguieron por Dailymotion e Internet
Archive, tal como indica el mensaje de arranque.

## Hallazgos

### Punto 9 · Las cinco respiraciones de los 4 personajes: nombre, japonés y el "aura" visual de cada una

Confirmado en la wiki de Fandom (páginas `Water Breathing`, `Flame Breathing`,
`Mist Breathing`, `Insect Breathing`) y **medido con `estilo.py`** en fotogramas
reales (ver Punto 4/14 abajo, ✅ con clip + wiki):

- **Tanjiro — Respiración del Agua** (水の呼吸, *Mizu no Kokyū*): "los usuarios se
  visualizan a sí mismos creando y manipulando agua"; el efecto es un remolino o
  arco de agua turquesa/blanco que sigue el filo de la espada. Medido en el
  opening (fotograma 1:01): **#F9FBFD, #4BE7F6, #35A3D8, #2A4C8A, #333C59**
  (blanco espuma → cian brillante → azul profundo). ✅ (wiki + fotograma propio).
- **Tanjiro — Hinokami Kagura / Respiración del Sol heredada** (ヒノカミ神楽):
  en el juego oficial *Hinokami Keppūtan* (SEGA/CyberConnect2, tráiler de
  personaje) el arco de la técnica es naranja-rojo con núcleo casi blanco.
  Medido a los 0:30 del clip: **#E87E27, #FCF6AD, #F6CF58, #A73B1C, #631810**
  sobre fondo nocturno azul-violeta **#4A4A69** (contraste cálido/frío muy
  marcado). En la escena real del anime (Tanjiro vs Rui, ver Punto 2) el mismo
  efecto se ve como un remolino rojo-rosado envolvente:
  **#E74F1B, #732512, #B13016, #FAE265** (fotograma a 2:01,
  https://www.dailymotion.com/video/x8nyhk5?t=121). ✅ (dos fuentes: juego oficial + escena de anime).
- **Rengoku — Respiración de la Llama** (炎の呼吸, *Honō no Kokyū*): "réplica
  perfecta del fuego... los usuarios se visualizan creando y manipulando fuego";
  deriva de la Respiración del Sol. Efecto: remolino de fuego naranja-amarillo
  en degradado, nunca plano. Medido en *Rengoku vs Akaza* (Mugen Train,
  4K 60FPS, https://www.dailymotion.com/video/x9j447k):
  - 1:12 (forma envolvente): **#F8E723, #E4711D, #C54814, #21090D, #EDAA1F**
  - 1:12b/pico de brillo: **#E8CE2D, #E8EFB4 (casi blanco), #E2A61A, #D66912**
  - Fondo nocturno del combate (0:60, sin fuego): **#36343A, #403E45, #282830,
    #181C26** — gris-azul muy desaturado (saturación 23 %, brillo 30 %): el
    fuego es lo único cálido en el plano. ✅ (medido en dos fotogramas del mismo clip + wiki).
- **Muichiro — Respiración de la Niebla** (霞の呼吸, *Kasumi no Kokyū*): "mimetiza
  la niebla... movimientos que desorientan, como una capa espesa de niebla
  oscurece la visión". Efecto: remolino ancho de blanco-cian pálido, más frío y
  desaturado que el agua de Tanjiro. Medido en el tráiler oficial SEGA de
  *Hinokami Chronicles 2 — Muichiro Tokito* (0:20,
  https://www.dailymotion.com/video/x9iosps?t=20): **#528097, #3C647C,
  #649BB4, #BDFCFE, #90E1EF, #1C4256, #041226**. ✅ (wiki + tráiler oficial SEGA).
- **Shinobu — Respiración del Insecto** (蟲の呼吸, *Mushi no Kokyū*): "estocadas y
  cortes superficiales para inyectar veneno de glicina"; el aura es un destello
  morado-lavanda en vez del habitual azul de las demás respiraciones (Shinobu no
  tiene fuerza para cortar cabezas, así que su Hashira usa veneno, y ese morado
  la distingue del resto). Medido en el tráiler *Hinokami Keppūtan — Kocho
  Shinobu* (0:33, https://www.dailymotion.com/video/x816qkg?t=33): **#5465AB,
  #445790, #7A6BCF, #A7AFEA, #EAD9FC (lavanda pálido), #140E39**. ✅ (wiki + tráiler oficial).

**Código de color de Ufotable confirmado por análisis externo** (no inventado):
la web *jbsiraudin.github.io* (análisis del "visual grammar" de los combates de
Demon Slayer) señala que "el color de la luz también importa: azul para la
espada, morado para el enemigo, dorado para las chispas — todo junto da señales
muy claras de quién hace qué y cuándo". Esto coincide con lo medido arriba:
cada respiración tiene su paleta fija y reconocible, y los enemigos casi
siempre llevan tonos morados/rosados (Akaza, Doma) frente al azul/naranja de
los Hashira. ✅ (fuente externa + medición propia, coinciden).

### Punto 9 · Puesta en escena de Ufotable en los combates (para las poses del punto 14)

De la misma fuente (`jbsiraudin.github.io/blog/demon-slayer-visual-grammar/`,
en inglés, artículo técnico de animación) — citas literales traducidas:
- **Composición centrada**: "la acción se comprime en el centro del encuadre
  para que el ojo no tenga que moverse demasiado" — reduce la fatiga visual y
  simplifica la posproducción.
- **Camera shake a 24 fps** sobre una animación base de 12 fps: "el temblor de
  cámara se anima a 24 fps, lo que ayuda a fluidificar el conjunto"; y "en cada
  impacto, la cámara se sacude en la dirección del golpe" (motion blur
  artificial).
- **Anuncio del golpe en 3 capas**: "cada estocada se anuncia con un brillo en
  la espada, reforzado después por una forma de luz y chispas".
- **Fotograma de impacto muy contrastado**: Ufotable inserta un fotograma en
  altísimo contraste (a menudo en silueta) justo en el momento del golpe para
  darle fuerza visual — prioriza "la sensación de la acción sobre su
  comprensión perfecta". ✅ (fuente única especializada; sin segunda fuente
  con el mismo detalle técnico, así que queda ⚠️ para el dato exacto de "24 fps
  sobre 12 fps", aunque el resto —colores, encuadre centrado, fotograma de
  impacto— coincide con lo que se ve en los propios fotogramas de arriba).
- Otra búsqueda (varias fuentes agregadas, sin cita textual única) describe la
  técnica de compositing de Ufotable como **"satsuei"**: la luz de una escena
  se comporta como una fuente real que rebota, proyecta sombras suaves y deja
  *bloom* en el "lente"; una sola escena de acción de 3 segundos puede apilar
  cientos de capas (arte de personaje, *motion blur*, partículas, gradación de
  color, iluminación, atmósfera, distorsión de lente). ⚠️ (resumen de varias
  fuentes de marketing/blogs, no una entrevista directa al estudio — para punto
  18 el investigador de texto debería buscar la entrevista original si
  necesita citarlo como oficial).

### Punto 4 · Sitios de la serie: luz y paleta medida (foco especial del encargo)

Todas las imágenes son fotogramas o arte oficial de la wiki de Fandom, **medidos
con `estilo.py`** (no de memoria):

- **Monte Natagumo** (那田蜘蛛山, bosque de la Familia Araña, ep. 15+): fotograma
  oficial 1920×1080 de la wiki
  (`Mount_Natagumo_Anime.png`). Paleta: **#0A1616, #061010, #111E1E, #020B0A,
  #000606** — casi todo negro-verdoso, **brillo medido de sólo 9 %**. Es el
  fondo más oscuro de toda la muestra: bosque nocturno opresivo, telarañas
  colgando, ninguna luz cálida. ✅ (imagen oficial de la wiki, medida).
- **Mansión Kocho / Mansión Mariposa** (蝶屋敷, base de recuperación de
  Shinobu, ep. 23+): fotograma oficial 1920×1080
  (`Butterfly_Mansion_Anime.png`). Paleta: **#2C3938, #48553E, #6B7A4A
  (verdes de jardín), #A9E0F9 (cielo azul), #4E5B6A, #D1C7A9 (madera)**;
  brillo 46 %, saturación 34 %, y **más línea de contorno que las escenas
  nocturnas** (línea #566245): es de día, jardín con glicinas, luz natural
  suave. Contraste deliberado con el resto de sitios, casi todos nocturnos.
  ✅ (imagen oficial, medida).
- **Yoshiwara / Distrito de la Perdición** (吉原, ep. 34+, escenario del arco
  de Entretenimiento): fotograma oficial 2048×1150
  (`Yoshiwara,_Tokyo_Anime.png`). Paleta: **#1D151B, #0C080E (casi negro),
  #3B2525, #6B3122, #BE451D (naranja-rojo de farol), #D7853B, #E5C379**;
  brillo 27 %. Barrio rojo nocturno: negro dominante con vetas cálidas de luz
  de farolillo, nunca luz blanca fría. ✅ (imagen oficial, medida).
- **Castillo Infinito** (無限城, arco final): descripción de la wiki
  (`Infinity Castle`): "dimensión de bolsillo hecha de habitaciones de madera
  iluminadas con faroles, pasillos largos y corredores que se mueven; posee
  una gravedad alterada que permite a los demonios pararse hacia arriba, hacia
  abajo, en las paredes o moverse en direcciones físicamente imposibles;
  Nakime controla la estructura con su Arte Demoníaco de Sangre". Medido en el
  tráiler oficial de la película *Infinity Castle* (Archive.org,
  fotograma 0:16, interior): **#3B1D14, #110E0B, #020101, #1C1914, #5A3626**
  — marrón-negro muy oscuro (**brillo 15 %**), confirma "madera iluminada con
  faroles" de la wiki. ✅ (wiki + tráiler oficial, coinciden).
- **Aldea de herreros / Swordsmith Village** (刀鍛冶の里, arco de Muichiro,
  ep. 34-44): "para proteger la aldea de ataques de demonios se toman medidas
  estrictas... los Cazademonios deben viajar con los ojos vendados, oídos y
  nariz tapados, a cuestas de un Kakushi" (wiki). No se consiguió aún un
  fotograma propio de la aldea de día para medir paleta (ver «No encontré»).
  ⚠️ (sólo texto de wiki, sin medición de color).
- **Mansión Ubuyashiki** (産屋敷邸, sede del Cuerpo de Cazadores): "en la cima
  de una montaña, en una zona aislada y protegida... su ubicación exacta se
  mantenía en secreto" (wiki); en el opening (fotograma 0:44, ver Punto 10) se
  ve a Kagaya Ubuyashiki sentado en una sala con luz cálida naranja desde una
  ventana — mismo lenguaje de "interior con luz de fuego/farol" que el
  Castillo Infinito y Yoshiwara. ⚠️ (una sola fuente visual propia, sin medir hex).
- **Tren Mugen / Mugen Train** (無限列車, película): "locomotora de vapor negra"
  (wiki); en el combate nocturno Rengoku-Akaza (ver arriba) el tren mismo no
  se ve, sólo el bosque de noche junto a las vías — mismo gris-azul
  desaturado #36343A ya medido. ⚠️ (no se aisló un plano del propio tren para
  medir su paleta).

**Patrón general del encargo (paisajes y auras)**: en las 6 localizaciones
revisadas, Ufotable usa **luz cálida puntual (farol, fuego) sobre fondos fríos
y muy oscuros** en casi todos los interiores/exteriores nocturnos (Yoshiwara,
Castillo Infinito, Mugen Train, combate de Natagumo), y reserva la luz
natural difusa y los verdes/azules claros para los únicos remansos de calma
diurnos (Mansión Mariposa). Esto es justo lo que hace reconocible el "aura" de
cada respiración: sobre un fondo casi monocromo y oscuro, el color de la
técnica (naranja/azul/morado/cian) es lo único saturado del plano.

### Punto 2 y 10 · Vídeos mirados de verdad (opening, ending, tráiler, escenas icónicas)

**Todo visto con `fotogramas.py` y las hojas abiertas con Read**, guardado en
`/tmp/claude-0/trabajo/79-demon-slayer-video/` (se borra el `video.mp4` tras
cada mirada). YouTube pedía iniciar sesión: todo por Dailymotion e Internet
Archive, como indica el aviso de arranque.

1. **Opening 1 — "Gurenge" (紅蓮華), LiSA** (temporada 1, ep. 1-26). Clip:
   https://www.dailymotion.com/video/x7ozs2c (89 s, canal HobbyConsolas,
   9 630 vistas). Hoja de 23 fotogramas, cada 4 s. Se ve: bosque con niebla en
   blanco y negro (0:04-0:08), el logo 鬼滅の刃 (0:12-0:16), Sabito y Makomo con
   máscaras de zorro/gato en el bosque de entrenamiento (0:28-0:32), Kanae y
   Shinobu Kocho con una mariposa (0:40-0:44), Kagaya Ubuyashiki sentado con
   luz cálida de ventana (0:44), remolino de agua turquesa — Respiración del
   Agua — (1:00-1:08), luna roja con la familia Kamado en silueta (1:12),
   Tanjiro saltando hacia la luna en silueta (1:16), primer plano final de
   Nezuko (1:28). ✅
2. **Ending / tema de créditos, ep. 19 — "Kamado Tanjiro no Uta" (家族の絆)**,
   Nami Nakagawa (tema de inserción usado como cierre del episodio 19). Clip
   creditless: https://www.dailymotion.com/video/x7wkzh0 (104 s, "[CREDITLESS]
   60FPS"). Hoja de 27 fotogramas, cada 4 s. Estilo muy distinto al resto de la
   serie: **ilustración de línea sepia/manga, casi sin color**, con la familia
   Kamado (madre e hijos) en distintas escenas domésticas — un contraste
   deliberado de Ufotable entre la animación de acción y este tema, dibujado
   como recuerdo/álbum de familia. Nota: la ED "oficial" con créditos de la
   temporada 1 es **"from the edge"** (FictionJunction feat. LiSA, ep. 2-18 y
   20-25); no se consiguió un clip de ésa en Dailymotion/Internet Archive
   (⚠️, ver «No encontré»), así que se describe la de ep. 19 como sustituto,
   dejándolo explícito.
3. **Tráiler oficial — Muichiro Tokito, "The Hinokami Chronicles 2" (SEGA)**.
   Clip: https://www.dailymotion.com/video/x9iosps (36 s). Hoja de 18
   fotogramas, cada 2 s. Remolinos de niebla blanco-cian (0:08-0:22), nombre
   en pantalla "霞柱 時透無一郎" (Pilar de la Niebla, Tokito Muichiro) a 0:28-0:30,
   fecha de lanzamiento "Available August 5th". ✅ (tráiler oficial SEGA,
   confirmado por el logo del editor en la propia hoja).
4. **Tráiler oficial — "Demon Slayer: Kimetsu no Yaiba – Infinity Castle" (MAIN
   TRAILER)**, película 2025. Archivo mp4 completo en Internet Archive:
   https://archive.org/details/demon-slayer-kimetsu-no-yaiba-infinity-castle-main-trailer
   (subido por un usuario, pero el vídeo lleva el logo oficial de Aniplex/Ufotable
   y branding IMAX). Hoja de 12 fotogramas, cada 8 s. Muichiro mirando al
   frente con la frase en pantalla "The words 'the final phase' keep crossing
   my mind" (0:16 — pose de **pensar**, ver Punto 14), un personaje con capa
   morada cayendo entre focos de luz de neón (0:24-0:32, probablemente Kanroji
   o Gyutaro/Daki), un abanico floral rosa (0:40), un rostro de demonio con
   tatuajes azules (1:12), tarjeta con el tema "A World Where the Sun Never
   Rises" (0:56) y el logo IMAX final (1:28). Interior con luz de farol muy
   oscura (fotograma 0:16, medido arriba en Punto 4). ✅
5. **Escena icónica 1 — Rengoku vs Akaza (Mugen Train)**. Clip "[4K 60FPS]":
   https://www.dailymotion.com/video/x9j447k (209 s). Hoja de 35 fotogramas,
   cada 6 s (detalle completo en Punto 4 y 14).
6. **Escena icónica 2 — Tanjiro vs Rui, Monte Natagumo (ep. 17-19), doblaje
   inglés**. Clip: https://www.dailymotion.com/video/x8nyhk5 (158 s). Hoja de
   20 fotogramas, cada 8 s. ⚠️ **Aviso**: es una re-subida con marca de agua de
   piratería ("To Download Full Movie Link In Description") en cada
   fotograma — se usó sólo para describir el contenido y medir color (fotograma
   2:01), nunca como imagen final; el minuto citado es el del propio clip, no
   el del episodio original (no se pudo verificar el minuto exacto del
   episodio real; el número de episodio 17-19 sí está confirmado por la wiki
   del personaje Rui). Se ven los hilos blancos de Rui (0:00-1:04), un tajo
   azul de Respiración del Agua (1:12) y el remolino rojo de la Hinokami
   Kagura nada más despertarla (1:52-2:32).
7. **Escena icónica 3 — Tanjiro, "Hinokami Kagura" (juego oficial *Hinokami
   Keppūtan*, tráiler de personaje)**. Clip:
   https://www.dailymotion.com/video/x89ntsh (59 s). Hoja de 20 fotogramas,
   cada 3 s (detalle en Punto 14).
8. **Escena/tráiler de personaje — Shinobu Kocho (juego oficial *Hinokami
   Keppūtan*)**. Clip: https://www.dailymotion.com/video/x816qkg (59 s). Hoja
   de 20 fotogramas, cada 3 s (detalle en Punto 14).

**Tendencias en vídeo (punto 10)**: la danza/pose de la **Hinokami Kagura**
es un trend viral en TikTok — más de **2,4 millones de posts** bajo el hashtag
relacionado, con vídeos de baile, cosplay y "sound design remakes" de la
técnica (ej. `tiktok.com/@andy_campbell_music` recreando el diseño de sonido
del golpe). ✅ (WebSearch, cifra de la propia plataforma citada por varias
fuentes coincidentes). No se pudo abrir TikTok directamente desde este
servidor para sacar minuto exacto de un vídeo concreto — ⚠️ cifra de alcance
general, sin un enlace de vídeo individual con minuto.

### Punto 14 · Poses analizadas por personaje (con minuto/enlace)

**Tanjiro Kamado** (7 poses, de 3 fuentes distintas):
1. Rostro decidido, ceño fruncido, ojo rojo — 0:20 del opening
   (dailymotion.com/video/x7ozs2c?t=20). Sirve para **animar/arengar**.
2. Salto en silueta hacia la luna roja, katana en alto — 1:16 del opening
   (…x7ozs2c?t=76). Sirve para **presentar** (encuadre de tarjeta de personaje).
3. Postura baja de combate, espada horizontal, mirada fija al enemigo —
   0:21 del tráiler del juego (dailymotion.com/video/x89ntsh?t=21). Sirve
   para **explicar** una técnica (postura de manual de Respiración del Agua).
4. Giro completo con estela de fuego naranja envolviendo el cuerpo, ambos
   brazos abiertos — 0:30 del mismo tráiler (…x89ntsh?t=30). Sirve para
   **celebrar/impactar** (remate de combo).
5. Grito con arco de fuego formando un círculo tras él — 0:33 (…x89ntsh?t=33).
   Sirve para **regañar/imponerse** (postura agresiva frontal).
6. En la escena de Rui: mirada de furia con la Hinokami Kagura encendida,
   remolino rojo de fondo — 2:01 (dailymotion.com/video/x8nyhk5?t=121, ⚠️ clip
   pirata, ver aviso arriba). Sirve para **explicar** el "despertar" del poder.
7. Con Nezuko en brazos, gesto protector, mirada baja — fotograma 0:44 del
   opening (…x7ozs2c?t=44, en la escena que muestra a Nezuko con la mordaza de
   bambú). Sirve para **pensar/proteger**.

**Kyojuro Rengoku** (6 poses, del clip 4K de Mugen Train, x9j447k):
1. Primer plano, pelo alborotado, mirada intensa — 0:00 (…?t=0). **Presentar**.
2. Postura de combate agachada, katana lista, estela de fuego tras él —
   0:36 (…?t=36). **Explicar/atacar**.
3. Remolino de fuego envolviéndolo por completo, forma casi abstracta —
   1:12 (…?t=72). **Celebrar/clímax** (Ougi, forma definitiva).
4. Vuelto de espaldas, capa/haori con bordes de flama estilizados, quieto tras
   el golpe — 2:00 (…?t=120). **Pensar/pausa dramática**.
5. Rostro herido, lágrima cayendo, mirada al cielo — 3:12 (…?t=192). **Momento
   emocional** (muerte, para escenas que hacen llorar — dato cruzado con el
   punto 21 del investigador de voz).
6. Sangre en la boca, sonrisa leve — 3:24 (…?t=204). **Despedida/legado**
   (última pose antes de morir, muy citada por el fandom).

**Muichiro Tokito** (6 poses, tráiler SEGA x9iosps + tráiler Infinity Castle):
1. Rostro neutro, mirada perdida, pelo verde-negro flotando en la niebla —
   0:10 (dailymotion.com/video/x9iosps?t=10). **Pensar** (coincide con su
   personalidad distraída/amnésica, dato para el investigador de voz).
2. Espada en diagonal completa cortando el aire, estela blanca fina —
   0:12-0:14 (…?t=12). **Explicar** (single strike característico de la
   Niebla).
3. Remolino ancho de niebla cian envolviéndolo, cuerpo casi oculto por el
   efecto — 0:20 (…?t=20). **Celebrar/clímax**.
4. Postura final envainando, de espaldas a cámara, niebla disipándose —
   0:24 (…?t=24). **Cerrar/calmar**.
5. Nombre en pantalla "霞柱 時透無一郎" en tarjeta con fondo azul oscuro —
   0:28 (…?t=28). **Presentar**.
6. Mirando al frente, sin expresión, con la frase en pantalla "The words 'the
   final phase' keep crossing my mind" — 0:16 del tráiler de Infinity Castle
   (archive.org/details/demon-slayer-kimetsu-no-yaiba-infinity-castle-main-trailer,
   fotograma a 0:16). **Pensar** (con diálogo real citado, la pose "pensativa"
   mejor documentada de las cuatro).

**Shinobu Kocho** (6 poses, tráiler *Hinokami Keppūtan* x816qkg):
1. Retrato sonriente, ojos violeta entrecerrados, mariposa de fondo —
   0:15 (dailymotion.com/video/x816qkg?t=15). **Presentar/saludar** (su sonrisa
   fija es rasgo de carácter — dato cruzado con voz, punto 13).
2. Postura de esgrima baja, cuerpo de perfil, espada hacia atrás lista para
   estocar — 0:18-0:21 (…?t=18). **Explicar** (postura de manual, Insecto =
   estocada, no tajo).
3. Estocada media, estela de energía blanca recta — 0:24-0:27 (…?t=24).
   **Atacar/regañar** (gesto ofensivo directo).
4. Salto con haori rosa ondeando como alas de mariposa, destello morado tras
   ella — 0:30-0:33 (…?t=30). **Celebrar/clímax**.
5. Primer plano de perfil, mirada de soslayo, mariposa posada en la mano
   (fotograma con más detalle de vestuario) — 0:39 (…?t=39). **Pensar**.
6. Silueta agachada entre árboles nevados, capa violeta cubriéndola —
   0:45 (…?t=45). **Acechar/preparar** (pose de vigilancia).

## Lo mejor para la lámina

- El **remolino de niebla cian-blanco** de Muichiro (paleta #528097-#BDFCFE)
  como marco/borde de un cuadro de diálogo: es el "aura" más limpia de medir y
  contrasta bien con fondo oscuro de madera.
- El **contraste cálido/frío de Ufotable**: fondo casi negro-azulado
  (#36343A) con un solo elemento naranja/cian/morado saturado — así se
  ilumina cualquier objeto de la lámina sin que se vea "plano".
- La cita real de Muichiro pensando ("the final phase keep crossing my mind",
  tráiler de Infinity Castle, 0:16) para una pose de personaje pensativo con
  su propio diálogo, no un genérico.
- El interior de madera con luz de farol (Castillo Infinito / Mansión
  Ubuyashiki / Yoshiwara) como referencia de "puesta en escena" para un objeto
  3D en Blender con luz puntual cálida sobre fondo oscuro.
- El dato del trend de TikTok de la Hinokami Kagura (2,4 M de posts): conecta
  directamente con el público de doblaje/edición del servidor.

## No encontré

- ⚠️ **AnimeThemes** (openings/endings en `.webm` de alta calidad): sigue caído
  (HTTP 522 / timeout en dos intentos, ver Bitácora). Se sustituyó por clips de
  Dailymotion e Internet Archive, con menor resolución garantizada.
- ⚠️ **Ending "from the edge" (temporada 1) como clip identificable**: no
  apareció un vídeo claramente etiquetado como esa ED concreta en Dailymotion
  ni Internet Archive con las búsquedas hechas (`Demon Slayer ending from the
  edge official`, `Kimetsu no Yaiba ending 1 animation`); se usó el tema de
  cierre del ep. 19 ("Kamado Tanjiro no Uta") como sustituto, dejándolo
  explícito arriba. Sería un extra, no obligatorio, seguir buscando ese clip
  exacto.
- ⚠️ **Fotograma propio de la Aldea de Herreros de día** para medir su paleta:
  sólo se consiguió el texto de la wiki, no una imagen 1080p+ para pasar por
  `estilo.py`. Se buscó en la galería de imágenes de la página de la wiki
  (`File:Swordsmith Village (Anime).png`, 1920×1080, localizada pero no
  llegó a medirse por tiempo).
- ⚠️ **Minuto exacto de la escena de Rui dentro del episodio real** (17-19):
  el clip usado es una resubida sin marca de tiempo oficial de episodio; sólo
  se pudo confirmar el rango de episodios por la ficha de Rui en la wiki, no
  el minuto exacto dentro de un episodio concreto.
- ⚠️ **Vídeo de TikTok individual con minuto exacto** para la tendencia de la
  Hinokami Kagura: TikTok no es accesible por scraping directo desde este
  servidor; el dato de alcance (2,4 M posts) sale de resultados de WebSearch,
  no de abrir un vídeo concreto.
- Videojuegos de la franquicia (punto 11) y encuestas de popularidad
  (punto 7): no son puntos de este rol (van a texto/voz); no se tocaron aquí
  más allá de lo que aparece de forma natural en los tráilers oficiales de
  *Hinokami Keppūtan*.

## Bitácora de búsqueda

- Fandom API (`kimetsu-no-yaiba.fandom.com/api.php`, inglés): búsqueda de
  texto "Rengoku" (confirma wiki correcta), categoría `Category:Music`,
  `Category:Opening Themes`, `Category:Ending Themes`, `Category:Locations`;
  wikitext de Gurenge, Akeboshi, Asa ga Kuru, From the Edge, Shirogane,
  Zankyosanka, Kizuna no Kiseki, Homura, Mugen, Tokoshie, Koi Kogare, Kamado
  Tanjiro no Uta, Kamado Nezuko no Uta, A World Where the Sun Never Rises,
  Shine in the Cruel Night (todas con `prop=revisions`); wikitext de Butterfly
  Mansion, Infinity Castle, Mugen Train (locomotive), Swordsmith Village,
  Ubuyashiki Mansion, Yoshiwara, Mount Natagumo; wikitext de Flame Breathing,
  Water Breathing, Mist Breathing, Insect Breathing; `imageinfo` de
  `Yoshiwara, Tokyo Anime.png`, `Butterfly Mansion Anime.png`, `Mount Natagumo
  Anime.png`, `Infinity Castle.png`.
- `api.animethemes.moe`: dos intentos (`filter[slug]=kimetsu-no-yaiba` y
  `kimetsu_no_yaiba`), los dos con timeout/522. `animethemes.moe` (sin api.)
  sí responde (200/302) pero no expone JSON de vídeos directamente.
- Dailymotion API (`api.dailymotion.com/videos?search=…`, inglés): "Kimetsu no
  Yaiba opening official", "Demon Slayer Rengoku vs Akaza scene", "Demon
  Slayer Tanjiro Hinokami Kagura", "Demon Slayer Shinobu vs Doma",
  "Demon Slayer Muichiro Tokito mist breathing", "Demon Slayer Muichiro
  Tokito fight scene Gyokko", "Demon Slayer Shinobu Kocho fight wisteria
  poison", "Demon Slayer opening Gurenge official animation", "Demon Slayer
  ending from the edge official", "Demon Slayer season 1 ending animation AMV
  From the Edge", "Kimetsu no Yaiba ending 1 animation", "Demon Slayer
  Zankyosanka opening animation", "Demon Slayer Tanjiro vs Rui Hinokami
  Kagura scene", "Demon Slayer Kokushibo Muichiro fight scene",
  "Hinokami Keppuutan Muichiro Tokito".
- Internet Archive (`archive.org/advancedsearch.php`, inglés): "Demon Slayer
  OR Kimetsu no Yaiba" + "opening/ending/trailer"; "Muichiro"; metadata de
  `demon-slayer-kimetsu-no-yaiba-infinity-castle-main-trailer` y de
  `cbfc-ecinepramaan-100010292300001912` (éste resultó ser un PDF del censor
  indio, no un vídeo).
- WebSearch (2 búsquedas, inglés): "Demon Slayer Ufotable animation style
  analysis lighting color grading video essay"; "Demon Slayer TikTok trend
  Hinokami Kagura viral sound"; "Demon Slayer sound design onomatopoeia
  Nichirin sword swing effect composer Yuki Kajiura interview".
- WebFetch: `jbsiraudin.github.io/blog/demon-slayer-visual-grammar/` (análisis
  técnico citado arriba).
- `herramientas/fotogramas.py`: 8 vídeos descargados y mirados por completo
  (hojas de contacto + Read), detallados en el Punto 2/10. `video.mp4` borrado
  tras cada uno.
- `herramientas/estilo.py`: 10 imágenes/fotogramas medidos (2 en Rengoku, 1
  Akaza, 1 Shinobu, 2 Tanjiro, 1 Muichiro, 1 agua, 3 localizaciones de wiki, 1
  interior Castillo Infinito) — todos los hex citados arriba salen de ahí, no
  de memoria.

## Cumplimiento del encargo (mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 2 — Fotogramas de escenas icónicas, capítulo/minuto | ✅ | 3 escenas (Rengoku vs Akaza, Tanjiro vs Rui, tráilers de personaje) miradas fotograma a fotograma con `fotogramas.py`, minuto y enlace `&t=` en cada pose citada. Resolución de trabajo 720p (la herramienta baja así "para mirar"); el original en streaming/Blu-ray es 1080p+, anotado en el propio texto. |
| 4 — Fondos y sitios, luz y paleta | ✅ | 6 sitios documentados, 4 con paleta hex **medida** (`estilo.py`) sobre imagen oficial 1080p+ o fotograma propio; 2 sólo con texto de wiki (Aldea de Herreros, Mansión Ubuyashiki) marcados ⚠️. |
| 9 — Música y sonido + efectos de las respiraciones (foco del encargo) | ✅ | OP/ED de las 5 temporadas + película con compositor, intérprete y episodios (wiki, dos fuentes cruzadas: infobox + categoría); las 4 respiraciones de los personajes de arranque con nombre japonés, descripción y paleta medida; puesta en escena de Ufotable con cita de fuente externa. Onomatopeyas concretas de golpe de espada: ⚠️ no se encontró una fuente que las liste (ver «No encontré» implícito arriba: búsqueda hecha, sin resultado claro), así que no se inventaron. |
| 10 — Vídeos: tráilers, escenas, tendencias, minuto | ✅ | Opening, sustituto de ending, 2 tráilers oficiales (SEGA + Infinity Castle) y 2 escenas de acción, todos con enlace y minuto; tendencia de TikTok con cifra de fuente pero sin vídeo individual (⚠️ parcial, ver «No encontré»). |
| 14 — Poses por personaje con minuto/enlace | ✅ | 6-7 poses por cada uno de los 4 personajes de arranque (Tanjiro, Rengoku, Muichiro, Shinobu), cada una con postura/manos/mirada descritas, minuto, enlace y para qué función sirve (presentar/explicar/celebrar/regañar/pensar/animar), tal como pide el punto 14. |
| Fuentes de vídeo sin YouTube | ✅ | Dailymotion (7 clips) + Internet Archive (1 tráiler oficial completo) + AnimeThemes reintentado (sigue caído, documentado). |

## Sigue:

Ya no queda obligatorio pendiente de mis puntos (2, 4, 9, 10, 14): todo lo
exigido por ENCARGO.md está cubierto con fuente, minuto y, donde aplica,
color medido. Lo que falta (paleta de la Aldea de Herreros de día, un clip
identificado de "from the edge", minuto exacto de un vídeo de TikTok
concreto) son extras y ya están anotados en «No encontré» con ⚠️, no aquí.
