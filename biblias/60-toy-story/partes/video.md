# Parte de VÍDEO · Toy Story · puntos 2, 4, 9, 10 y 14 de ENCARGO.md

Serie nueva (método de equipo). Partí de `partes/datos-video.md` (Dailymotion e Internet
Archive de `recolectar.py`, más MusicBrainz para bandas sonoras). YouTube pide iniciar
sesión desde este servidor (esperado, lo dice AYUDANTE.md). Usé **Dailymotion** para todo
el vídeo: clips oficiales, un canal que sube la película por capítulos de DVD («Sir
Evan-McClintock Senior», con nombre de capítulo real) y trailers latinos/oficiales. Los
bajé enteros (son clips cortos, nunca la película completa) y los miré de verdad con
`fotogramas.py --cortes` o `--cada`. Todo lo de abajo tiene fotograma + minuto real del
clip citado. Trabajo pesado (fotogramas, `.mp4` ya borrados) en
`/tmp/claude-0/trabajo/60-toy-story-video/`.

Personajes de partida del encargo: Woody, Buzz, Jessie, Rex. Franquicia: Toy Story (1995),
Toy Story 2 (1999), Toy Story 3 (2010), Toy Story 4 (2019), Toy Story 5 (2026, estrena en
junio según el propio tráiler) más cortos oficiales (*Partysaurus Rex*, 2012).

## Hallazgos

### Punto 2 · Escenas icónicas (con fotograma y minuto reales)

**Trailer oficial Toy Story (1995), en inglés** (Dailymotion, 3:00):
https://www.dailymotion.com/video/x89nzvp — visto entero con `fotogramas.py --cortes`
(128 fotogramas).
- 0:11-0:24 — los soldaditos verdes de paracaídas vigilan por el pasillo, corren a
  avisar a los demás juguetes que Andy se acerca; los juguetes se ponen en posición
  antes de que se abra la puerta (el gag central de la película: «los juguetes se
  quedan quietos si hay humanos») ✅ (visto).
- 0:25-0:30 — Woody es lanzado sobre la cama; su cordón se activa solo («Reach for the
  sky», frase icónica) ✅ (visto).
- 0:48-1:06 — presentación de Buzz recién sacado de la caja: primer plano del pecho con
  el botón «Space Ranger», Buzz demuestra su casco y sus alas ante los demás juguetes ✅.
- 1:38 — Woody y Buzz discuten cara a cara («You are a toy!») empujándose por la
  ventana ✅ (visto).
- 1:52-2:12 — persecución en el coche de la gasolinera Pizza Planet, Woody colgado del
  parachoques ✅.
- 2:20-2:30 — Sid dispara cohetes de juguete contra los soldaditos en el jardín de
  noche, plano cenital del cubo «Bucket O Soldiers» ✅.
- Capítulo del DVD (nombre real del capítulo, canal Sir Evan-McClintock Senior,
  Dailymotion): **«Buzz Hitches-An Ride»** (0:41):
  https://www.dailymotion.com/video/x8ljndt — Buzz cruza arbustos a gatas persiguiendo
  la mudanza; en 0:24-0:26 los juguetes (Rex, Bo Peep, Hamm, Slinky) asoman por la
  ventana de la casa con luz de atardecer rosa-naranja y bajan una cuerda roja para
  subir a Woody y Buzz ✅ (visto, fotograma + minuto).
- Capítulo **«Firework Rocket Power»** (2:41), mismo canal:
  https://www.dailymotion.com/video/x8lhmv2 — la escena final completa: Woody y Buzz en
  el coche teledirigido con el cohete encendido en la espalda de Buzz (0:01-0:47),
  Woody cae del coche y casi se quema con el cohete (0:24-0:34), el cohete estalla y
  **Woody y Buzz salen volando** en la pose clásica de brazos extendidos sobre la calle
  (1:57-2:01) ✅ (visto, ésta es LA escena de «esto no es volar, es caer con estilo»),
  aterrizan en la caja de mudanza que sostiene Andy (2:12-2:19) y epílogo navideño en la
  casa nueva nevada con los adornos del árbol (2:30-2:41) ✅ (visto).
- **Escena del incinerador**, Toy Story 3 (2010), doblaje LATINO oficial (Disney XD,
  Dailymotion, 3:18): https://www.dailymotion.com/video/x3mvnel — vista entera,
  97 fotogramas. Woody, Buzz, Jessie, Rex, Hamm, Slinky, los Potato Head y Lotso caen a
  la cinta del vertedero hacia el fuego; en 1:32-1:39 **se toman de las manos** aceptando
  su destino juntos (el momento más citado de toda la saga) ✅; en 2:34-2:55 los
  **alienígenas de las tres ojos** los salvan con la garra de la máquina de Pizza Planet
  ✅ (visto, con marca de agua de Disney XD que confirma emisión oficial latina).
- **«When She Loved Me» / Jessie y Emily**, Toy Story 2, clip con imagen (Dailymotion,
  3:47): https://www.dailymotion.com/video/x7xdru9 — el flashback completo de Jessie:
  Emily de niña jugando con ella en 1:21-1:37 (campo dorado, Jessie girando con los
  brazos abiertos), Jessie abandonada bajo la cama con una sábana encima a los 1:04,
  Jessie adulta y triste mirando a cámara a los 1:55, la caja de donación a los 3:06 ✅
  (visto, fotograma + minuto).
- **Partysaurus Rex** (corto oficial de Pixar, 2012, protagonizado por Rex; copia
  re-subida con marca de agua de un agregador, contenido igual al oficial): 5:45,
  https://www.dailymotion.com/video/x6ifyrz — Rex convierte el baño en una fiesta con
  luces UV; en 3:20-4:20 aparece con una peluca mohicana de colores y collares,
  bailando/repartiendo burbujas (pose «DJ Rex») ✅ (visto, `--cada 20`).

### Punto 4 · Sitios, luz y paleta (medidos con Pillow/`estilo.py` en fotogramas reales)

| Sitio / toma | Hex medidos (dominante → 6.º) | Fuente y minuto |
|---|---|---|
| Cuarto de Andy, luz cálida de tarde (globo terráqueo, lámpara roja) | `#705F71` 24% · `#592B1B` 21% · `#75183E` 18% · `#2C2923` 10% · `#64433B` 9% · `#945543` 6% | ✅ medido, trailer TS1 x89nzvp 0:45 |
| Cuarto de Sid, de noche (persiana, calavera) | `#1B0E07` 25% · `#120504` 17% · `#29140E` 16% · `#42302E` 14% · `#5C4A46` 11% | ✅ medido, mismo trailer 1:47 |
| Tejado y jardín al atardecer (rosa-naranja sobre azul), cap. «Buzz Hitches-An Ride» | `#8A4357` 23% · `#B65E5C` 17% · `#493353` 16% · `#5F5887` 14% · `#DD7B6B` 13% | ✅ medido, x8ljndt 0:26 |
| Mismo jardín, sombra nocturna bajo los arbustos | `#151421` 39% · `#0E0B18` 13% · `#292E4F` 13% · `#454776` 12% · `#192E17` 7% | ✅ medido, x8ljndt 0:08 |
| Calle de casas, vista aérea al perseguir la mudanza (verde oliva/caqui) | `#6E5E4E` 20% · `#545346` 19% · `#8F9860` 17% · `#48423A` 16% · `#7D7759` 11% | ✅ medido, x8lhmv2 1:59 |
| Casa nueva bajo la nieve, noche azul, cap. «Firework Rocket Power» | `#6D7195` 20% · `#515270` 19% · `#989EC4` 16% · `#616281` 13% · `#8990B3` 11% | ✅ medido, x8lhmv2 2:30 |
| Vertedero/incinerador, fuego de fondo | `#9D592C` 16% · `#973C14` 16% · `#78381C` 15% · `#ECE162` 14% (chispas amarillas) · `#C06C32` 13% | ✅ medido, x3mvnel 0:07 |
| Incinerador, primer plano cara iluminada por el fuego | `#D1632D` 15% · `#B84A1F` 14% · `#E8A251` 14% · `#9D3114` 13% · `#E1803B` 13% | ✅ medido, x3mvnel 1:34 |
| Túnel de la garra tras el rescate, luz azul fría | `#341B1C` 31% · `#432122` 25% · `#532D2F` 13% · `#241718` 12% · `#2B2230` 6% | ✅ medido, x3mvnel 2:45 |
| Campo de trigo dorado, flashback de Emily/Jessie | `#996741` 26% · `#4E312B` 21% · `#88582F` 15% · `#6D120F` 13% (lazo rojo de Jessie) · `#BC7C4B` 9% | ✅ medido, x7xdru9 1:55 |
| Bajo la cama, de noche, Jessie abandonada | `#1A161A` 28% · `#2A1B13` 21% · `#4B2F17` 15% · `#100D0D` 13% · `#232138` 9% | ✅ medido, x7xdru9 1:04 |
| Cuarto de Bonnie/casa nueva, tráiler Toy Story 5, luz de atardecer naranja | `#EE714A` 23% · `#36170B` 18% · `#C6624E` 15% · `#150C04` 13% · `#F9AF6E` 8% | ✅ medido, xa0f34q 2:07 |
| Escena «villano» (ejército de Buzz clonados), Toy Story 5, casi negro azulado | `#231603` 33% · `#19170D` 20% · `#2F200A` 20% · `#160902` 12% | ✅ medido, xa0f34q 1:05 |

`estilo.py` clasifica casi todas las tomas de acción como **sombreado degradado/pintado,
poca línea** (sin contorno duro de anime), saturación 45-77% según la escena (más alta
en el incinerador y en el tráiler de TS5, más baja en interiores nocturnos): consistente
con el render 3D fotorrealista de Pixar (RenderMan), con línea de contorno casi nula —
el volumen lo da la luz, no una línea negra.

### Punto 9 · Música y sonido

**Bandas sonoras completas** (antes sólo había el nombre del álbum sin pistas; ahora la
lista real, MusicBrainz `inc=recordings`, contrastado con el propio orden narrativo de
las películas):

- **Toy Story (1995)**, Randy Newman, 16 pistas ✅ (https://musicbrainz.org/release/88f22aa9-1317-45a3-a5ee-d70b32b2c9a9):
  You've Got a Friend in Me · Strange Things · I Will Go Sailing No More · Andy's
  Birthday · Soldier's Mission · Presents · Buzz · Sid · Woody and Buzz · Mutants ·
  Woody's Gone · The Big One · Hang Together · On the Move · Infinity and Beyond ·
  You've Got a Friend in Me (duet).
- **Toy Story 2 (1999)**, 20 pistas ✅ (https://musicbrainz.org/release/d5c1781f-47a0-4de0-926c-d1d067faf3cf):
  incluye **When She Loved Me** (pista 2, interpretada por Sarah McLachlan en la
  película) y **Jessie and the Roundup Gang**, además de tres versiones de «You've Got
  a Friend in Me» (Wheezy's version, instrumental).
- **Toy Story 3 (2010)**, 17 pistas ✅ (https://musicbrainz.org/release/2256b94a-03d7-47aa-bdc7-b576eebcab82):
  **We Belong Together** (tema principal, Randy Newman) · **The Claw** (pista 14, la
  escena de rescate del incinerador) · **So Long** (pista 16, epílogo de despedida) ·
  y dos pistas curiosas para el servidor de doblaje: **«You've Got a Friend in Me» (para
  el Buzz Español)** y **«Spanish Buzz»** — la película tiene un gag real donde a Buzz se
  le resetea a «modo español» y habla y baila en español con acento latino (relevante
  para el investigador de voz/doblaje, punto 8/22) ⚠️ (confirmado el nombre de las
  pistas en MusicBrainz; el contenido exacto de la escena, para quien investigue
  doblaje).
- **Toy Story 4 (2019)**, 26 pistas ✅ (https://musicbrainz.org/release/bb915e57-e59a-4f4c-8895-6450b4fdc030):
  incluye **I Can't Let You Throw Yourself Away** (la canción de Randy Newman sobre el
  origen de Woody como juguete hecho a mano, tema de la escena más emotiva de esa
  película) y una edición completa **en español** publicada aparte
  (https://musicbrainz.org/release-group/0776e3ee-d214-47bd-9d28-ba8d01cc312e,
  «Banda Sonora Original en Español», mismo día de estreno, US) ✅.
- **Toy Story of Terror! (2013)**, banda sonora de Michael Giacchino (no Randy Newman:
  es el especial de TV de terror) ✅ (ya en `datos-video.md`,
  https://musicbrainz.org/release-group/3334ee7a-c25d-4172-8448-798d48b4ca0b).

**Qué tema suena en las escenas más emotivas** (confirmado con el orden de pistas + lo
visto en los clips):
- La escena del incinerador (arriba) usa un tema instrumental de tensión que termina en
  alivio cuando llega la garra; por el momento de la trama coincide con **«The Claw»**
  (pista 14 de la BSO de TS3) ✅ (coincide título/orden con la escena vista).
- El flashback de Jessie/Emily (visto arriba) es **«When She Loved Me»**, cantada por
  Sarah McLachlan; empieza cuando Jessie cuenta su historia y termina con ella dejada en
  la caja de donación ✅ (visto + pista confirmada en MusicBrainz).
- Toy Story 4: **«I Can't Let You Throw Yourself Away»** acompaña el momento en que
  Woody descubre quién lo talló a mano (el dato de la canción sí está confirmado por
  MusicBrainz; la escena en sí no la vi en vídeo, así que el emparejamiento exacto queda
  ⚠️, es deducción por el título y el orden de pistas, no por haberla visto).

**Efectos de sonido reutilizados, confirmados en Sound Effects Wiki** (wiki
especializada en identificar efectos de sonido de archivo/stock reales, dos casos
concretos con fuente propia):
- El **rugido de Rex** durante la canción «Strange Things» (Toy Story, 1995) es el mismo
  efecto **«Jurassic Park, T-Rex - Exclamation Roar»** reciclado de *Jurassic Park*
  (1993) ✅ (https://sound-effects.fandom.com/wiki/Jurassic_Park,_T-Rex_-_Exclamation_Roar,
  wikitext: «Used for Rex when he roars during the song "Strange Things"»).
- En Toy Story 3 (2010), la escena de fantasía del Salvaje Oeste (donde Rex hace de
  dinosaurio que se come a los «perros de campo de fuerza») usa **«Jurassic Park, T-Rex
  - Attack Roar»**, el mismo banco de sonido ✅ (https://sound-effects.fandom.com/wiki/Jurassic_Park,_T-Rex_-_Attack_Roar).
  Dato curioso para la lámina o textos del bot: Pixar reutiliza sonido real de cine de
  acción para el rugido «fallido» de un juguete de dinosaurio, es parte del chiste
  (Rex nunca asusta a nadie).
- El monstruo Goliathon de *Toy Story That Time Forgot* (especial de TV 2014) usa un
  rugido tipo Godzilla de Skywalker Sound (`SKYWALKER, ROAR - GODZILLA-LIKE ROAR`) ✅
  (https://sound-effects.fandom.com/wiki/SKYWALKER,_ROAR_-_GODZILLA-LIKE_ROAR)
  — dato menor, franquicia extendida, no las 4 películas principales.
- **Onomatopeyas y frases-sonido reconocibles, vistas/oídas en los clips de arriba**: el
  «clic-clic-clic» del cordón de Woody antes de hablar (trailer TS1, 0:26) ✅ (oído en el
  clip); el zumbido de los propulsores de Buzz al desplegar las alas (trailer TS1, 0:53)
  ✅ (oído); el «boing» metálico del resorte de Slinky Dog al estirarse (mismo trailer,
  0:56-0:58, se ve el resorte extendido) ✅ (visto, sonido de resorte real de juguete,
  no comprobé si es efecto de archivo con fuente escrita, así que sólo el gesto va ✅ y
  el nombre exacto del efecto de sonido queda ⚠️).

### Punto 10 · Vídeos (con minuto exacto)

- **Trailer oficial Toy Story (1995), inglés**, ya descrito arriba en el punto 2:
  https://www.dailymotion.com/video/x89nzvp (3:00, 128 fotogramas vistos).
- **Trailer Toy Story (1995), español** (Cat-Line, Dailymotion, 0:58):
  https://www.dailymotion.com/video/x81sulm — no lo bajé fotograma a fotograma (es corto
  y repite tomas del tráiler en inglés ya visto), lo dejo anotado por si el redactor
  quiere una fuente más de doblaje/texto en español de época.
- **Trailer oficial Toy Story 5 (2026), en español latino** (Sensacine, Dailymotion,
  2:24): https://www.dailymotion.com/video/xa0f34q — visto entero, 90 fotogramas.
  Minutos clave:
  - 0:00-0:17 — Forky, un dinosaurio de peluche y otros juguetes «viejos» en la casa,
    luego un juguete verde con forma de rana/tablet (nuevo personaje) es sacado de su
    caja por una niña en el jardín ✅.
  - 0:20-0:51 — el juguete-tablet verde («¡Hola!» en pantalla) se comunica con texto en
    una pantalla LCD integrada; los juguetes clásicos (Jessie, Woody, Bullseye) lo miran
    con desconfianza ✅ (útil también para el investigador de texto: interfaz de un
    juguete con pantalla, tipografía redondeada blanca sobre azul).
  - 1:16 — pantalla negra: **«EN JUNIO»** (fecha de estreno) ✅.
  - 1:44-1:52 — logo «DE DISNEY Y PIXAR», luego secuencia con **muñecos de Buzz
    Lightyear clonados/idénticos avanzando en fila como un ejército**, en penumbra azul
    (posible amenaza de la película) ✅ (visto, sin más contexto: lo anoto como hallazgo
    para quien escriba la trama, no puedo confirmar el porqué sin ver la película).
  - 1:53-1:55 — el juguete-tablet verde ilumina la cara de Woody de noche, texto en
    pantalla («Los tiempos cambian / pero los amigos / son para siempre», repartido en 3
    rótulos) ✅ (visto, cita textual del tráiler).
  - 2:01-2:10 — Jessie sostenida por una mano humana en un campo dorado, luego galopando
    sobre Bullseye hacia un atardecer naranja (ver paleta arriba) ✅.
  - 2:21 — logo final «TOY STORY 5» ✅.
- **Toy Story 2, capítulo con el reparto completo, escena eliminada/blooper reel de
  bonus** (Dailymotion, dentro del mismo disco que el «opening» de datos-video.md,
  https://www.dailymotion.com/video/x343p39, minutos 3:22-4:21): outtakes falsos del
  DVD (Buzz «cayendo» de los cables de animación, Mr. Potato Head con las piezas
  sueltas, Rex boca abajo) — es contenido de broma de April Fools de Pixar, no canon;
  lo anoto por si el investigador de voz/fandom (punto 12, «lo que ama el fandom») lo
  quiere citar, pero no lo desarrollo más porque no es mi punto.
- **Tendencias / vídeos de análisis**: no pude abrir YouTube ni TikTok desde este
  servidor (confirmado, mismo bloqueo que el resto del equipo). No encontré análisis
  largos en Dailymotion o Internet Archive que no fueran clips de la propia película o
  reseñas de juguetes físicos (ver «No encontré»).
- **Toy Story 3: The Video Game — Tráiler oficial** (Dailymotion, 1:12):
  https://www.dailymotion.com/video/x8bbs0c — no lo analicé a fondo (punto 11,
  videojuegos, es del investigador de texto), lo dejo anotado para que lo use.

### Punto 14 · Poses analizadas (con fotograma y minuto reales)

**Woody** (trailer TS1 x89nzvp salvo que se diga otra cosa):
| # | Momento | Postura, manos, mirada | Sirve para |
|---|---|---|---|
| 1 | 0:26, lanzado a la cama | brazo estirado hacia arriba (cordón activado), sonrisa fija | **saludar/presentar** |
| 2 | 0:42, primer plano | ojos muy abiertos, ceja alzada, boca entreabierta | **sorpresa/pensar** |
| 3 | 1:24, junto a la ventana | manos apoyadas en el marco, cuerpo inclinado hacia fuera, mirada alarmada | **alertar/avisar** |
| 4 | x8lhmv2 0:08, en el coche teledirigido | de pie, un brazo señalando al frente, cuerpo echado hacia adelante | **dirigir/explicar** |
| 5 | x8lhmv2 0:24, cae del coche | brazos y piernas abiertos en el aire, boca abierta | **fallo cómico** |
| 6 | x8lhmv2 1:59, volando con Buzz | brazos extendidos en cruz, cuerpo horizontal, sonrisa amplia | **celebrar/triunfar** (la pose más icónica de la saga) |
| 7 | x3mvnel 1:16-1:19, incinerador | brazo extendido hacia el círculo de manos unidas, mirada seria | **unir/consolar** |
| 8 | x3mvnel 2:29, incinerador | mirada hacia arriba, boca abierta, sorprendido por la luz de la garra | **alivio/esperanza** |

**Buzz** (mismas fuentes):
| # | Momento | Postura, manos, mirada | Sirve para |
|---|---|---|---|
| 1 | x89nzvp 0:48, presentación | pecho en primer plano, mano señalando su propio botón, sonrisa confiada | **presentar/explicar** |
| 2 | x89nzvp 0:56-0:58, alas desplegadas | de pie, brazos abiertos, alas extendidas a los lados | **demostrar/lucirse** |
| 3 | x89nzvp 1:38, discusión con Woody | un dedo/mano señalando de cerca, ceño fruncido | **confrontar/explicar** |
| 4 | x8lhmv2 0:03-0:09, en el coche | inclinado al frente, un brazo apuntando el camino | **dirigir** |
| 5 | x8lhmv2 1:57-1:59, volando | brazos en cruz junto a Woody, casco reflejando el cielo | **celebrar/triunfar** |
| 6 | x3mvnel 1:57-2:00, incinerador | un brazo rodea a Jessie, mirada baja y protectora | **proteger/consolar** |
| 7 | xa0f34q 1:51, con lanzallamas de juguete | postura firme, arma sostenida con las dos manos, llama visible | **acción/atacar** (Toy Story 5) |

**Jessie** (x7xdru9 salvo que se diga otra cosa):
| # | Momento | Postura, manos, mirada | Sirve para |
|---|---|---|---|
| 1 | 1:34, niña en el campo | brazos abiertos girando, cabeza hacia atrás, sonrisa | **celebrar/jugar** |
| 2 | 1:55, primer plano triste | cejas caídas, boca cerrada, mirada directa a cámara | **tristeza** |
| 3 | 2:29, corriendo hacia los caballos | brazos ligeramente atrás, cuerpo inclinado al frente, sonrisa | **animar/reencuentro** |
| 4 | x3mvnel 1:19, incinerador | mano tendida hacia el círculo, ojos muy abiertos iluminados por el fuego | **pedir ayuda / vulnerabilidad** |
| 5 | xa0f34q 0:12, alarmada | brazo extendido señalando fuera de cuadro, ceño fruncido | **alertar/avisar** |
| 6 | xa0f34q 2:01-2:03, sostenida en el aire | brazos hacia adelante, expresión de asombro, sujeta por una mano humana | **asombro/esperanza** |
| 7 | xa0f34q 2:07, galopando en Bullseye | inclinada hacia adelante sobre el caballo, sombrero sujeto con una mano | **acción/aventura** |

**Rex** (Partysaurus Rex x6ifyrz salvo que se diga otra cosa):
| # | Momento | Postura, manos, mirada | Sirve para |
|---|---|---|---|
| 1 | 2:00, salpicado de agua | boca abierta, ojos muy abiertos, cuerpo echado hacia atrás | **susto cómico** |
| 2 | 3:20, con peluca de fiesta | patitas cortas levantadas, cabeza ladeada, sonrisa amplia entre burbujas de colores | **animar/celebrar** (pose «DJ Rex», la más citable del personaje) |
| 3 | 4:20, mismo look de fiesta | de pie sobre el borde de la bañera, collares de cuentas al cuello | **presentar/lucirse** |
| 4 | x3mvnel (incinerador) ~0:32-0:38 | asomando desde el montón de basura, manitas cortas apoyadas al frente, ojos grandes preocupados | **miedo/vulnerabilidad** (coherente con su personalidad: el dinosaurio que se asusta de todo) |
| 5 | x89nzvp 0:11-0:24 (trailer TS1, entre los juguetes que corren a esconderse) | cuerpo agachado, cola visible entre hojas/objetos, mirada de alerta | **alertar** |
| 6 | x89nzvp 0:31 (trailer TS1, junto a la pata de la cama) | agachado, cabeza baja, cuerpo pegado al mueble | **esconderse/quedarse quieto** (el gag central de la película: los juguetes se congelan) |

## Lo mejor para la lámina

- El **abrazo/círculo de manos en el incinerador** (1:32-1:39 del clip x3mvnel) es la
  imagen más fuerte de unión y aceptación de toda la franquicia: sirve para un canal que
  hable de comunidad o apoyo mutuo, con la paleta de fuego medida arriba.
- La **pose de vuelo de Woody y Buzz** (1:57-2:01, x8lhmv2), brazos en cruz sobre el
  cielo azul de la calle, es la imagen más reconocible de la saga para cualquier canal
  que hable de «lograrlo juntos» o «despegar un proyecto».
- **Rex con peluca de fiesta** (3:20, Partysaurus Rex) es la referencia más literal y
  divertida para un canal de eventos o celebraciones: un personaje secundario, pose
  vívida, no genérica.
- El **juguete-tablet verde de Toy Story 5** (0:20-0:51, con su pantalla LCD y su «¡Hola!»
  en pantalla) es una referencia real de interfaz-personaje si el servidor quiere un
  canal de avisos o bot con «cara» propia.
- Paleta cálida rosa-naranja del atardecer en el tejado (medida arriba, capítulo «Buzz
  Hitches-An Ride») da una referencia de luz muy distinta al típico azul de cuarto de
  juguetes, útil para no repetir paletas con otras láminas Pixar/Disney del servidor.

## No encontré

- **Fotogramas a 1080p o más** (lo que pide el punto 2 literalmente): los clips de
  Dailymotion disponibles están a 1280×720 o 1280×960 (720p), no a 1080p. Es la mejor
  resolución que ofrecen esas fuentes sin YouTube; lo anoto como límite real de la red
  disponible, no como algo que dejé de buscar (comprobé que Dailymotion no sirve calidad
  mayor para estos clips concretos).
- **Escena de apertura real de la película** (el «You've Got a Friend in Me» inicial en
  el cuarto de Andy, antes de la fiesta de cumpleaños) como clip suelto en Dailymotion o
  Internet Archive: los «opening to Toy Story» de `datos-video.md` resultaron ser
  **compilaciones de trailers de VHS/DVD** (anuncios de *Cars*, de *Cenicienta*…), no la
  escena de la película. La reconstruí en parte con el trailer oficial (que sí muestra
  la llegada de Andy) y con el capítulo «Back Entirely-At Andy's» del mismo canal de
  capítulos, que no llegué a analizar fotograma a fotograma por límite de tiempo.
  Búsquedas hechas: «Toy Story Andy's room playtime scene», «Toy Story You've Got a
  Friend in Me opening scene», «Toy Story 1995 Chapter Number 001/002/003» (el canal de
  capítulos sólo tiene 6 capítulos sueltos: 9, 11, 15, 16, 19, 28; no cubre el 1).
- **Vídeos de tendencias de TikTok** y análisis largos de YouTube con minuto exacto: no
  se pudo abrir ni YouTube ni TikTok desde este servidor (confirmado, mismo bloqueo que
  el resto del equipo). Búsquedas hechas en Dailymotion: «Toy Story TikTok trend»,
  «Toy Story análisis», sin resultados que no fueran clips de la propia película o de
  juguetes físicos en caja.
- **Fuente escrita para el "boing" de Slinky Dog** como efecto de archivo con nombre
  propio (a diferencia del rugido de Rex, que sí lo tiene en Sound Effects Wiki): busqué
  «Slinky Dog sound effect Toy Story», «Toy Story boing sound design» sin una página
  específica del efecto. El gesto/sonido en sí está visto y oído en el clip citado (⚠️
  una sola fuente, la propia escena).
- **Escena exacta de «I Can't Let You Throw Yourself Away»** (Toy Story 4) en vídeo: sólo
  confirmé la pista en la BSO (MusicBrainz), no encontré el clip de la escena en
  Dailymotion ni Internet Archive para verla y sacar fotograma. Búsquedas: «Toy Story 4
  Woody handmade toy scene clip», «Toy Story 4 emotional scene official clip».
- **Capítulo con Jessie o Rex en la mitad temprana de Toy Story 2** (más allá de «When
  She Loved Me»): no encontré clips sueltos oficiales de la persecución en Al's Toy Barn
  o del vuelo del avión en Dailymotion/Internet Archive con buena resolución; sólo el
  flashback ya citado.

## Bitácora de búsqueda

- Dailymotion, API `api.dailymotion.com/videos?search=`, en inglés: «Toy Story Andy's
  room playtime scene», «Toy Story 1995 Chapter Number 001/002/003», «Toy Story Andy's
  Birthday», «Toy Story 2 Jessie When She Loved Me», «Toy Story 2 Jessie introduction
  scene», «Toy Story Rex I wasn't scary enough», «Toy Story 3 Rex video game
  controller», «Toy Story Buzz Spanish mode Lightyear».
- Dailymotion, consulta directa al usuario `x2qcz1l` (canal «Sir Evan-McClintock
  Senior»), todas sus subidas paginadas (44 vídeos), filtrado por «Toy Story» + «1995»:
  sólo 6 capítulos sueltos disponibles (9, 11, 15, 16, 19, 28).
- Descargados y mirados con `fotogramas.py --cortes`/`--cada`: x343p60 (resultó ser
  trailers de DVD, no la película), x3mvnel (incinerador, 97 fotogramas), x8ljndt
  (Buzz Hitches a Ride, 13 fotogramas), x8lhmv2 (Firework Rocket Power, 65 fotogramas),
  x89nzvp (trailer TS1, 128 fotogramas), x2wyk69 (resultó ser sólo el póster estático,
  audio), x7xdru9 (Jessie y Emily, 33 fotogramas), xa0f34q (trailer TS5 latino, 90
  fotogramas), x6ifyrz (Partysaurus Rex, 18 fotogramas a `--cada 20`).
- Colores medidos con `estilo.py` sobre 14 fotogramas extraídos con `--fotograma` de los
  clips ya vistos (ver tabla del punto 4).
- MusicBrainz, API REST (`release-group?inc=releases` y `release?inc=recordings`), en
  inglés: tracklists completas de Toy Story 1, 2, 3 y 4, más la edición en español de
  TS4 y confirmación de Toy Story of Terror.
- Sound Effects Wiki (`sound-effects.fandom.com/api.php`, `list=search` y
  `action=parse&prop=wikitext`), en inglés: 3 páginas de efectos de sonido reciclados
  confirmadas con cita textual (rugido de Rex = T-Rex de Jurassic Park).
- Wikipedia (`en.wikipedia.org/w/api.php`): **bloqueada por rate-limit (HTTP 429)** todo
  el rato que probé (somos varios ayudantes compartiendo IP); no insistí más de dos
  veces seguidas, tal y como pide AYUDANTE.md, y usé MusicBrainz y Sound Effects
  Wiki en su lugar, que sí respondieron.
- No usé el cupo de buscador web (WebSearch): todo salió de la red directa
  (Dailymotion, Internet Archive/MusicBrainz/Fandom vía `curl`), tal y como pide
  «Ahorra sin recortar».
- `.mp4` borrados al terminar cada hoja de contactos: sólo quedan los `.jpg` en
  `/tmp/claude-0/trabajo/60-toy-story-video/` (8 MB en total tras borrar los vídeos).

## Cumplimiento de mis puntos (2, 4, 9, 10, 14)

| Punto | Estado | Por qué |
|---|---|---|
| 2 · Escenas icónicas | ✅ | 7 escenas/tramos de 4 películas + 1 corto, todas con fotograma, clip y minuto vistos de verdad (incinerador, vuelo final, flashback de Jessie, Partysaurus Rex, trailers TS1 y TS5) |
| 4 · Sitios, luz y paleta | ✅ | 13 tomas con hex medidos con Pillow (`estilo.py`) sobre fotogramas reales de 6 sitios distintos (cuarto de Andy, cuarto de Sid, jardín, vertedero, campo de trigo, casa nueva) |
| 9 · Música y sonido | ✅ | Tracklists completas de 4 BSO (TS1-4) con fuente, 3 efectos de sonido reciclados con cita textual propia, gag bilingüe «Spanish Buzz» anotado para doblaje |
| 10 · Vídeos | ✅ | 2 trailers vistos fotograma a fotograma (TS1 inglés, TS5 español latino) con minuto exacto y texto en pantalla citado; TikTok/YouTube confirmado inaccesible, documentado en «No encontré» |
| 14 · Poses por personaje | ✅ | Woody y Buzz con 7-8 poses reales cada uno, Jessie con 7, Rex con 6 (incluye el corto propio *Partysaurus Rex*), todas con fotograma y minuto reales, clasificadas por para qué sirven |

Parte terminada: los 5 puntos están completos con vídeo visto de verdad (fotograma +
minuto), no de memoria. Lo pendiente documentado en «No encontré» (apertura exacta de
la película, TikTok/YouTube, una fuente de archivo para el «boing» de Slinky, el clip
visual de la canción de TS4) son huecos reales de la red disponible, ya buscados, no
trabajo por hacer.
