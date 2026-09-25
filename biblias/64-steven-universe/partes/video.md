# Parte de VÍDEO · Steven Universe (encargo 64)

Puntos de ENCARGO.md: 2 (fotogramas de escenas icónicas), 4 (fondos y sitios: luz, paleta,
texturas), 9 (música y sonido), 10 (vídeos: tráilers, escenas, análisis, tendencias),
14 (poses analizadas por personaje, con capítulo y minuto).
Libreta de datos: `- dato · fuente(s) · ✅/⚠️ · minuto o tamaño si aplica`.

`datos-video.md` sólo trajo clips cortos de Dailymotion (la mayoría, avances de guía de TV de
canales franceses, no escenas reales) y una lista de items de Internet Archive sin comprobar.
YouTube pedía iniciar sesión desde este servidor, así que todo el vídeo de abajo se vio en
**Internet Archive** (episodios y clips completos, comprobados uno a uno con su metadata antes
de bajarlos) — plan B de AYUDANTE.md. Se bajaron a
`/tmp/claude-0/trabajo/64-steven-universe-video/` (fuera del repo) y se borran al terminar.

## Vídeos mirados de verdad (con fotogramas.py, no reseñas)

| Vídeo | Fuente | Duración | Confirmado como |
|---|---|---|---|
| **"Gem Glow"** (S1E1, piloto) | archive.org/details/steven-universe-s-01-e-01-gem-glow | 11:30 | episodio completo real (créditos de Cartoon Network Studios al final) |
| **"Stronger Than You"** (clímax de "Jail Break", S1E52) | archive.org/details/Steven_Universe_Garnets_Fusion_Song_Stronger_Than_You_ | 4:11 | escena real de la pelea Garnet vs. Jasper |
| **"The Answer" — Animatic oficial** | archive.org/details/steven-universe-the-answer-animatic | 11:26 | storyboard/animatic **oficial de Cartoon Network** (créditos «STEVEN UNIVERSE EPISODE 075, Cartoon Network», sin publicar en TV) — plan C de AYUDANTE.md |
| **Tráiler Toonami de la película** | archive.org/details/steven-universe-the-movie-toonami-trailer | 2:00 | tráiler oficial (cartela «STEVEN UNIVERSE THE MOVIE — Monday September 2nd 6:00P», logo Cartoon Network) |
| **"1 Second From Every Steven Universe Episode"** | archive.org/details/1-second-from-every-steven-universe-episode | 2:55 | vídeo de fan (análisis/tendencia, no oficial) |
| **"Steven Universe Tik Toks"** | archive.org/details/steven-universe-tik-toks | 4:59 | recopilación de fan de TikToks reales (cosplay, speedpaint, roleplay) |

Todas verificadas con `archive.org/metadata/<id>` antes de bajar (título, descripción, tamaño de
archivo real) para no gastar ancho de banda en algo falso — así se descartaron los「blind
reactions」y los .rar de la serie completa (8.4 GB, un solo archivo, inútil para sacar
fotogramas).

## Punto 2 · Fotogramas de escenas icónicas (capítulo y minuto)

### Escena 1 — "Gem Glow" (S1E1), episodio piloto completo
Primer episodio: presenta la Casa Playa, el Templo de Cristal, el Big Donut y a las 4 Gemas
peleando contra un Centipeetle (gema corrupta). Visto entero cada 10 s (70 fotogramas).
- 0:00-0:20 — cold open: Steven corriendo con Pearl por un puente hacia un acantilado ·
  archive.org/download/steven-universe-s-01-e-01-gem-glow/…mkv#t=10 · ✅ (visto)
- 1:00-1:50 — interior del **Big Donut** (la tienda de Sadie y Lars) · #t=70 · ✅
- 2:00-2:50 — interior del **Templo de Cristal**, pasillo de cristales rosas y azules
  triangulares · #t=130 · ✅
- 8:20-8:50 — el Centipeetle (gema corrupta, forma de gusano/dragón verde) ataca en el
  acantilado; Garnet, Amatista y Perla pelean juntas · #t=510-530 · ✅
- 10:40-11:10 — cierre: las 4 gemas + Steven sentados en la playa al atardecer, tras la
  victoria · #t=660 · ✅ (paleta medida abajo, punto 4)

### Escena 2 — "Stronger Than You" (canción del clímax de "Jail Break", S1E52)
Garnet (recién fusionada nuevamente de Ruby+Sapphire) canta y pelea contra Jasper a bordo de la
nave gema. Es LA escena más citada por el fandom de toda la serie (ver punto 21 de voz/personajes).
- 0:00 — Garnet sentada, calmada, Steven pequeño a su lado tras el reencuentro · #t=0 · ✅
- 0:54-0:57 — Steven mirando con ojos-estrella, sorprendido · #t=54 · ✅
- 2:42-2:45 — Garnet de pie, chasqueando los dedos con confianza (gesto icónico) · #t=162 · ✅
- 3:00-3:33 — pelea cuerpo a cuerpo, Garnet esquiva y golpea a Jasper · #t=180-213 · ✅
- 4:09 — Jasper derrotada, atrapada en burbuja rosa · #t=249 · ✅

### Escena 3 — "The Answer" (animatic oficial, origen de Garnet)
Storyboard oficial de Cartoon Network (nunca emitido así, sólo animatic) de cómo Ruby salvó a
Sapphire y se fusionaron por primera vez, formando a Garnet. Es el origen narrado por Garnet a
Steven.
- 8:56-9:12 — Ruby y Sapphire se toman de la mano por primera vez, decidiendo fusionarse ·
  archive.org/download/steven-universe-the-answer-animatic/…mp4#t=536 · ✅
- 11:04-11:20 — la fusión: ambas brillan y se funden en una sola silueta (nace Garnet) ·
  #t=664-680 · ✅

**Nota sobre «ending»:** Steven Universe (a diferencia de un anime) no tiene un tema de cierre
distinto por episodio: tras la escena final pasa directo a los créditos con música instrumental
de fondo (confirmado viendo el final de "Gem Glow", 11:10-11:30) · ✅ (visto).

## Punto 4 · Fondos y sitios: luz, paleta (hex medidos) y texturas

Paletas sacadas con `herramientas/estilo.py` sobre fotogramas propios de "Gem Glow" (1280×714,
recorte de letterbox de un mkv 1080p original) — no de arte promocional (eso es del investigador
de imagen). Cada hex es el color medido, no aproximado a ojo.

### Acantilado y playa de Beach City (exterior, luz de día)
- Fotograma 0:10 (`archive.org/download/steven-universe-s-01-e-01-gem-glow/…mkv#t=10`) · cielo
  y mar en tonos fríos claros · paleta: `#CBFDF5` 32% `#F9FBF9` 26% `#ACFCEF` 17% `#BCDCCB` 15%
  `#58AAA8` 7% `#4C2433` 3% · brillo 93%, saturación 20% (luz de día muy lavada, casi pastel) ·
  ✅ (medido)
- Textura real equivalente: cielo despejado con niebla costera — sin textura de material (es
  luz/cielo, no superficie).

### Big Donut (interior, tienda)
- Fotograma 1:10 · paleta: `#D1B797` 23% `#A5847E` 19% `#EFE8C8` 18% `#F2DB9B` 16% `#FCFCEC`
  14% `#443B3B` 10% · sombreado degradado/pintado (vitrinas y mostrador con luz cálida de
  interior) · ✅ (medido)
- Textura real equivalente para el mostrador de madera clara: **Wood095** (CC0) ·
  https://ambientcg.com/view?id=Wood095 · ✅ (comprobado en la API `ambientcg.com/api/v2/full_json?type=Material&q=wood`)

### Templo de Cristal (interior, pasillo de cristales)
- Fotograma 2:10 · paleta: `#522F42` 22% (morado oscuro) `#AA827C` 19% `#D3DEDA` 16%
  `#726670` 16% `#F8F6F8` 14% `#BFAEA5` 13% · sombreado mixto, luz interior tenue con brillo de
  cristal · ✅ (medido) · el «Templo de Cristal» es su nombre oficial en la wiki (página
  `Crystal Temple`, confirmada) · https://steven-universe.fandom.com/wiki/Crystal_Temple · ✅

### Cocina de la Casa Playa (interior)
- Fotograma 3:30 · paleta: `#7A5C74` 22% `#CEA7B0` 21% `#F4DACF` 19% `#090306` 17% (sombra)
  `#5B1D37` 13% `#F7ECFC` 8% · saturación 35%, brillo 61% (luz cálida de tarde entrando por
  ventana) · ✅ (medido) · «Beach House» es su nombre oficial en la wiki, confirmado ·
  https://steven-universe.fandom.com/wiki/Beach_House · ✅

### Playa al atardecer (cierre de "Gem Glow")
- Fotograma 11:00 · paleta: `#17251E` 29% (verde muy oscuro, silueta de acantilado) `#F7F6CE`
  23% (cielo claro) `#ECD2A3` 18% (arena/luz cálida) `#445651` 13% `#CD8891` 11% (rosa de
  atardecer) `#946463` 6% · saturación 35%, brillo 61% · ✅ (medido) — paleta de atardecer muy
  usable para una lámina (cielo cálido + silueta oscura + una figura con luz de borde).
- Textura real equivalente para la arena: **Ground054** (CC0) ·
  https://ambientcg.com/view?id=Ground054 · ✅ (comprobado en la API, `q=sand`)

### Templo (textura de cristal/roca)
- Textura real equivalente para las paredes rocosas del Templo de Cristal: **Rock064** (CC0) ·
  https://ambientcg.com/view?id=Rock064 · ✅ (comprobado en la API, `q=stone`) — el color de las
  paredes en sí es el hex medido arriba (`#522F42`/`#AA827C`); esta textura es sólo para el
  relieve de roca, no el tono.

### Otro sitio de referencia (del clip de "Stronger Than You")
- La **Nave Gema** (Gem Warship) donde pelean Garnet y Jasper: interior verde fosforescente con
  paredes orgánicas (parecen zarcillos), muy distinto a la Tierra — confirma que Homeworld/las
  naves gema usan una paleta verde-veneno reconocible, útil para distinguir escenas "de gemas"
  de escenas "de la Tierra" en una lámina · visto en `stronger_than_you/hoja_02.jpg` 2:48-3:24 ·
  ✅ (visto, sin medir hex porque es del investigador de imagen si se necesita el hex exacto).

## Punto 9 · Música y sonido

### Tema de apertura
- **«We Are the Crystal Gems»**: compuesto por Rebecca Sugar y Aivi & Surasshu; versión corta
  (0:36) cantada por Zach Callison (Steven) desde el piloto, versión completa (2:23) con Estelle
  (Garnet), Michaela Dietz (Amatista) y Deedee Magno Hall (Perla) · Fandom (wikitext de la
  página «We Are the Crystal Gems») + confirmado escuchándolo en el minuto 0:00-0:36 de "Gem
  Glow" · ✅ (dos fuentes: wiki + visto/oído en el episodio)
- No hay un tema de **cierre** distinto (ver nota en el punto 2): la serie corta a créditos con
  música instrumental de fondo, no una canción de cierre cantada como en un anime · ✅ (visto).

### Canciones en escenas emotivas (letra, compositor y contexto confirmados en Fandom)
- **«Stronger Than You»** (S1E52 "Jail Break") — escrita por Rebecca Sugar, cantada por Estelle
  (voz de Garnet); Garnet la canta peleando contra Jasper tras reformarse; 2:52 · tema de
  triunfo/confianza, el más citado del fandom · https://steven-universe.fandom.com/wiki/Stronger_Than_You
  · ✅ (wiki + visto en el clip)
- **«It's Over, Isn't It»** (S3E16 "Mr. Greg") — escrita por Rebecca Sugar, cantada por Deedee
  Magno-Hall (voz de Perla); Perla canta su duelo porque Rose Quartz (Rosa) eligió a Greg;
  2:20 · tema de tristeza/duelo, de los que más hace llorar al fandom (ver punto 21, del
  investigador de voz) · https://steven-universe.fandom.com/wiki/It%27s_Over_Isn%27t_It · ✅
  (wiki; sólo hay versión de audio official en Internet Archive, sin vídeo — item
  `StevenUniverseItsOverIsntItHD`, formatos mp3/ogg, comprobado)
- **«Love Like You»** — tema de créditos de cierre de la serie (suena en los créditos finales de
  cada episodio, cantado por Rebecca Sugar), pista 37 del álbum oficial · confirmado en el
  tracklist oficial (ver abajo) · ✅

### Álbum oficial (fuente primaria: tracklist de Fandom, con referencias a iTunes/Billboard)
- **Soundtrack: Volume 1** (2 jun 2017) — 37 canciones, compositores Aivi & Surasshu, Hellen Jo,
  Ben Levin, Jeff Liu y Rebecca Sugar; llegó a #1 en iTunes y a la lista *Billboard 200* ·
  https://steven-universe.fandom.com/wiki/Soundtrack:_Volume_1 (wikitext con cita a Billboard e
  iTunes) · ✅
- Tracklist completo confirmado (37 títulos): incluye "We Are the Crystal Gems", "Giant Woman",
  "On the Run", "Full Disclosure", "Mr. Greg", "Here Comes a Thought", "What's the Use of
  Feeling (Blue)?" y "Love Like You (End Credits)" entre otras · misma fuente · ✅
- **Soundtrack: Volume 2** y el álbum de **Steven Universe: The Movie** también existen (ver
  `datos-video.md`, MusicBrainz) · ✅ (dos fuentes: MusicBrainz + mención en la página de "We Are
  the Crystal Gems" como álbum de la versión de "Change Your Mind")

### Bandas sonoras de videojuegos de la franquicia (ambiente, no diegéticas)
- **Steven Universe: Attack the Light — Full OST** y **Save the Light — Full OST**, ambas
  subidas completas en Internet Archive · archive.org/details/steven-universe-attack-the-light-full-ost
  y archive.org/details/steven-universe-save-the-light-full-ost · ⚠️ (existencia confirmada, no
  se escucharon: es trabajo del investigador de voz/sonido detallar pistas si hace falta más).

### Efectos de sonido y onomatopeyas reconocibles
- **«Poof»**: cuando una gema recibe daño, su forma física se disuelve en una nube de humo y se
  retira a su gema (no «muere»); es el término que usa el propio fandom y los videojuegos de la
  franquicia (la barra de vida de "Attack the Light" se llama «harmony» y al llegar a 0 la gema
  «se retira a su piedra», ver `partes/texto.md` punto 11) · visto en pantalla en "Gem Glow" con
  el Centipeetle (8:50-9:00, aunque en el piloto no llega a poof, sólo queda herido) y es el
  mismo verbo que usa la wiki para las gemas corruptas en general · ⚠️ (una sola fuente directa
  de terminología — no encontré una página dedicada «Sound Effects»; sí lo confirma indirectamente
  `partes/texto.md` con el juego oficial)
- Sonido de invocación de arma (el «shing»/destello al sacar la lanza de Perla o los guanteletes
  de Garnet): visible como un flash geométrico con líneas de brillo alrededor de las manos, en
  "Gem Glow" 3:30 (Perla) y 6:00-6:10 (Garnet) · ✅ (visto, sin clip de audio aislado para citar
  el sonido en sí — pendiente si el investigador de voz tiene el archivo con audio limpio).
- No encontré una página dedicada de la wiki a «efectos de sonido»: busqué `onomatopoeia`,
  `sound effect` (texto e inglés) y sólo salieron páginas de personajes/episodios que las
  mencionan de paso. Ver «No encontré» al final.

## Punto 10 · Vídeos: tráilers, escenas, análisis y tendencias (con minuto)

### Tráiler oficial
- **Tráiler Toonami de "Steven Universe: The Movie"** (Cartoon Network) — mezcla tomas de la
  película con metraje de la serie; termina con cartela «STEVEN UNIVERSE THE MOVIE — Monday
  September 2nd 6:00P» y el logo de Cartoon Network · minuto 1:36-1:48 muestra una fusión de 4
  brazos morada (probablemente Sugilite, Garnet+Amatista) y a Lion; 1:52-1:54 la cartela oficial
  · archive.org/download/steven-universe-the-movie-toonami-trailer/…mp4#t=96 · ✅ (visto entero,
  120 s)

### Vídeos de análisis (reseñas/ensayos, con creador)
- **«Steven Universe VS Social Norms | A Video Essay»** — de **Saberspark** (creador conocido de
  ensayos de animación en YouTube), 14:45 min, patrocinado por Steven Universe Amino · analiza
  cómo la serie rompe normas de género en dibujos animados infantiles · archive.org/details/youtube-oHkd2QERNy8
  · ✅ (metadata comprobada: creador y duración)
- **«Steven Universe Review - Is it good or bad?»** — de **PhantomStrider**, 5:13 min: elogia
  personajes carismáticos, animación y — cita textual de la descripción del propio archivo —
  «beautiful animation, nice [...]» · archive.org/details/steven-universe-review-is-it-good-or-bad
  · ⚠️ (sólo metadata leída, no se escuchó el análisis completo por presupuesto de tiempo)
- **«The Secret Origin of STEVEN UNIVERSE w Chris McDonnell»** (episodio de pódcast, con el
  autor del libro *Steven Universe: Art & Origins*) — fuente indirecta sobre producción, para
  cruzar con el investigador de texto/técnica · archive.org/details/98fc287479a22cb81f0e3dcd9ff72b8e
  · ⚠️ (sólo el título; no se escuchó)

### Tendencias de TikTok/YouTube del fandom (con minuto, del recopilatorio de fans)
Del ítem `steven-universe-tik-toks` (Internet Archive, 4:59 min, recopilación de TikToks reales
hecha por un fan con KineMaster) — visto entero cada 3 s:
- 2:33-2:57 — **cosplay dúo Steven+Rose/Perla** en la calle, cuenta «PorkCutlett» · #t=153 · ✅
- 2:57-3:15 — **speedpaints** de fan art de Steven (varias cuentas: incluye una llamada «Smiley
  Trash Bag») · #t=177 · ✅
- 3:18-3:33 — **TikTok interactivo tipo «elige tu aventura»**: «You meet a Jasper… Fuse with me?
  Yes/No», roleplay con botones simulados de sí/no, tendencia de formato muy popular en 2021-22
  · #t=198-213 · ✅
- 3:48-4:03 — **cosplay de Spinel** bailando al aire libre · #t=228 · ✅
- 4:33-4:45 — **reenactment/cosplay corriendo** (figura rosa corriendo por una acera, estilo
  Spinel) · #t=273 · ✅

Del ítem `1-second-from-every-steven-universe-episode` (2:55 min, un fan reúne 1 segundo de cada
episodio, con subtítulos de título de episodio activables) — visto entero cada 2 s: sirve como
**resumen visual cronológico** de toda la serie, útil para ver de un vistazo qué escenas/POSES
se repiten más (Steven corriendo, Garnet señalando, Perla con su lanza) ·
archive.org/details/1-second-from-every-steven-universe-episode · ✅ (visto)

### Clips en Dailymotion de `datos-video.md`: comprobados y descartados
La mayoría de los resultados de Dailymotion en `datos-video.md` (Tele-Loisirs.fr,
TV-programme.com, Télé 7 Jours, 0:21-0:33 s) son **avisos de programación de TV francesa**, no
escenas de la serie — se comprobó por el nombre del canal y la duración (demasiado corta para
ser un clip real). Se descartaron sin gastar fotogramas.py en ellos. El único con contenido real
potencial, «- Steven Universe - Pilot -» de «New All New» (1:56), queda de menor calidad que el
episodio completo ya conseguido en Internet Archive, así que no se usó.

## Punto 14 · Poses analizadas por personaje (capítulo, minuto, qué hace)

Todas de vídeos vistos con `fotogramas.py` (no de memoria). Enlaces con `#t=` a los archivos de
Internet Archive; el minuto es el que aparece en la hoja de contacto. Los 4 personajes son los
que pide `encargos/64-steven-universe.md` para empezar.

### Steven Universe
1. **"Gem Glow" 0:50** — alarmado, brazos arriba, protegiendo la caja de rosquillas · postura:
   inclinado hacia atrás, manos abiertas · sirve para **reaccionar/sorpresa** ·
   …mkv#t=50 · ✅
2. **"Gem Glow" 1:20** — abrazando la caja de Cookie Cat contra el pecho, sonrisa enorme ·
   sirve para **celebrar** · #t=80 · ✅
3. **"Gem Glow" 1:30** — señalando con el dedo índice un símbolo en la pared (el warp pad) ·
   sirve para **presentar/explicar un descubrimiento** · #t=90 · ✅
4. **"Gem Glow" 3:20** — abrazándose a sí mismo, mirada de lado, hablando con Perla · postura
   tímida/pensativa · sirve para **pensar/preguntar** · #t=200 · ✅
5. **"Gem Glow" 5:30** — brazo extendido señalando hacia delante con decisión, hablando con
   Amatista · sirve para **animar (a que le sigan)** · #t=330 · ✅
6. **"Gem Glow" 8:20** — brazos totalmente abiertos, cara de alarma, de espaldas al monstruo ·
   sirve para **advertir/reaccionar** · #t=500 · ✅
7. **"Gem Glow" 9:30** — sosteniendo dos Cookie Cats, cara de preocupación/oferta · sirve para
   **pedir ayuda/ofrecer** · #t=570 · ✅
8. **"Stronger Than You" 0:54-0:57** — ojos en forma de estrella, boquiabierto mirando a Garnet
   pelear · sirve para **admirar/reaccionar con asombro** · #t=54-57 · ✅

### Garnet
1. **"Gem Glow" 2:40** — de pie, brazos cruzados, expresión seria tras las gafas · sirve para
   **vigilar/autoridad silenciosa** · #t=160 · ✅
2. **"Gem Glow" 6:00-6:10** — guanteletes invocados con destello, lista para pelear · sirve para
   **actuar/prepararse** · #t=360-370 · ✅
3. **"Gem Glow" 9:40-10:00** — disparando un rayo de energía junto a Perla y Amatista contra el
   Centipeetle · sirve para **pelear en equipo** · #t=580-600 · ✅
4. **"Gem Glow" 10:20** — de pie en el centro, manos en la cadera, con Amatista y Perla tras la
   victoria · sirve para **celebrar/triunfo** · #t=620 · ✅
5. **"Stronger Than You" 0:00** — sentada con las piernas cruzadas, calmada, Steven pequeño al
   lado · sirve para **explicar con calma** · #t=0 · ✅
6. **"Stronger Than You" 2:42-2:45** — de pie, chasqueando los dedos, sonrisa confiada (gesto
   icónico de Garnet) · sirve para **presentar/mostrar seguridad** · #t=162-165 · ✅
7. **"Stronger Than You" 3:09-3:15** — puñetazo en pleno vuelo contra Jasper, acción dinámica ·
   sirve para **enfrentar una amenaza (regañar con los puños)** · #t=189-195 · ✅
8. **"The Answer" (animatic) 8:56-9:12** — Ruby y Sapphire se dan la mano por primera vez,
   decidiendo fusionarse · sirve para **animar/unir** (pose de origen, muy citada por el
   fandom) · #t=536-552 · ✅
9. **"The Answer" (animatic) 11:04-11:20** — el brillo de la primera fusión, naciendo Garnet ·
   sirve para **transformación/celebración emocional** · #t=664-680 · ✅

### Amatista
1. **"Gem Glow" 4:00-4:10** — comiendo un Cookie Cat feliz, sosteniendo la envoltura · sirve
   para **celebrar/disfrutar** · #t=240-250 · ✅
2. **"Gem Glow" 5:40** — ofreciendo un Cookie Cat a Steven, postura relajada/encorvada · sirve
   para **compartir/ofrecer** · #t=340 · ✅
3. **"Gem Glow" 6:30** — señalando mientras habla con Steven en la cocina · sirve para
   **explicar** · #t=390 · ✅
4. **"Gem Glow" 8:40-8:50** — corriendo por el acantilado junto a Garnet y Perla, alerta ·
   sirve para **animar/actuar en equipo** · #t=520-530 · ✅
5. **"Gem Glow" 10:40** — cavando en la arena junto a Steven, gesto juguetón · sirve para
   **jugar/relajarse** · #t=640 · ✅
6. **"Gem Glow" 10:50** — agachada junto a Steven en la playa, postura desenfadada · sirve para
   **acompañar** · #t=650 · ✅

### Perla
1. **"Gem Glow" 2:20** — manos cerca de la cara, ojos muy abiertos, mirando al monstruo ·
   sirve para **reaccionar con miedo/sorpresa** · #t=140 · ✅
2. **"Gem Glow" 3:30** — invocando su lanza con círculos de magia brillante alrededor de las
   manos · sirve para **presentar poder/invocar arma** · #t=210 · ✅
3. **"Gem Glow" 4:30** — tapándose la cara con las manos, exasperada · sirve para **regañar
   (frustración silenciosa)** · #t=270 · ✅
4. **"Gem Glow" 7:10-7:40** — regañando a Steven de cerca sobre las normas de la casa · sirve
   para **regañar** · #t=430-460 · ✅
5. **"Gem Glow" 8:00** — brazos cruzados, mirada de desaprobación en la cocina · sirve para
   **vigilar/desaprobar** · #t=480 · ✅
6. **"Gem Glow" 10:10** — lanza en alto, brillando, en plena pelea, determinada · sirve para
   **pelear/decidir** · #t=610 · ✅

### Mapa rápido de categorías (para el redactor)
| Categoría | Steven | Garnet | Amatista | Perla |
|---|---|---|---|---|
| presentar | #3 (1:30) | #6 (2:42) | #3 (6:30) | #2 (3:30) |
| explicar | #4 (3:20) | #5 (0:00) | #3 (6:30) | #4 (7:10) |
| celebrar | #2 (1:20) | #4 (10:20) | #1 (4:00) | — |
| regañar | #6 (8:20)* | #7 (3:09)* | — | #4 (7:10) |
| pensar | #4 (3:20) | — | — | #3 (4:30) |
| animar | #5 (5:30) | #8 (8:56) | #4 (8:40) | — |
(*Steven y Garnet no «regañan» en sentido literal en estas escenas; son las poses más cercanas
— confrontación/advertencia — se anota para que el redactor decida si encajan.)

## Lo mejor para la lámina

- El chasquido de dedos confiado de Garnet en "Stronger Than You" (2:42) — pose de seguridad
  total, perfecta para un canal de «logros» o confianza.
- La paleta de atardecer del final de "Gem Glow" (11:00): `#17251E` `#F7F6CE` `#ECD2A3`
  `#445651` `#CD8891` — cálida, con silueta oscura, lista para usar de fondo con un personaje
  delante.
- El gesto de invocar arma de Perla (círculos de magia en las manos, 3:30 de "Gem Glow") — muy
  «vivo», con objeto, tal como pide el dueño (nunca de pie sin más).
- El origen de Garnet en el animatic oficial de "The Answer" (8:56-11:20): dos manos que se
  tocan y se funden en luz — muy fuerte para un canal sobre «fusión»/equipo/colaboración.
- El interior verde-veneno de la Nave Gema (Homeworld) como contraste de paleta frente al calor
  de la Casa Playa — útil si el canal necesita distinguir «hogar» de «amenaza».

## No encontré

- Una página dedicada de la wiki a «efectos de sonido/onomatopeyas» de la serie: busqué
  `onomatopoeia`, `sound effect`, `"poof" retreat gem` (inglés) en el buscador de texto de
  Fandom y sólo salieron páginas de personajes/episodios que las mencionan de paso, no una ficha
  central. Lo que hay (el «poof») queda anotado con ⚠️ en el punto 9.
- Un «ending» (tema de cierre) distinto del opening: confirmado que NO existe (no es que no lo
  encontré, es que la serie no lo tiene — ver nota del punto 2).
- Clips oficiales de escenas dobladas en español latino con buena resolución en Dailymotion o
  Internet Archive: lo que hay en `datos-video.md` son avisos de programación de TV francesa, no
  clips reales (ver punto 10). El doblaje latino en sí (actores, frases) es punto del
  investigador de voz, no mío.
- ⚠️ No pude entrar a YouTube directamente (pide iniciar sesión desde este servidor, según lo
  esperado) para comprobar los storyboards internos de YouTube (plan C); usé en su lugar el
  animatic oficial ya público en Internet Archive, que cumple el mismo propósito (material de
  producción con marcas de tiempo).
- ⚠️ No escuché completos los vídeos de análisis de Saberspark (14:45) ni de PhantomStrider
  (5:13) por presupuesto de tiempo: sólo se comprobó su metadata (creador, duración, tema) —
  quedan citados con ⚠️ para quien quiera profundizar.

## Bitácora de búsqueda

- **Internet Archive, advancedsearch.php** (inglés): `title:(steven universe) AND
  mediatype:(movies)` → 100 resultados; de ahí se identificaron y comprobaron con
  `/metadata/<id>` los 6 vídeos usados (piloto, Stronger Than You, animatic de The Answer,
  tráiler de la película, 1 segundo por episodio, recopilación de TikToks) y se descartaron
  el .rar de 8.4 GB de la serie completa y varias «blind reactions» (no aportan fotogramas
  propios).
- **Internet Archive** (inglés): búsqueda específica `title:("The Answer" OR "Reunited" OR
  "Jail Break" OR "Full Disclosure") AND steven universe` → encontró el animatic oficial de
  "The Answer" y confirmó que "It's Over Isn't It" sólo existe como audio (mp3/ogg) en ese
  repositorio, no como vídeo.
- **Fandom steven-universe.fandom.com/api.php** (inglés), `action=query&list=search`: `list of
  songs`, `Main Title Theme`, `Beach House`, `Temple warp pad`, `Crystal Temple`, `onomatopoeia
  sound effect`, `"poof" retreat gem` — para confirmar nombres oficiales de sitios y canciones.
- **Fandom steven-universe.fandom.com/api.php**, `action=parse&prop=wikitext`: páginas «We Are
  the Crystal Gems», «Stronger Than You», «It's Over Isn't It», «Soundtrack: Volume 1» — para
  compositores, cantantes, duración y tracklist oficial con letras.
- **Vídeo mirado de verdad** (obligatorio de AYUDANTE.md): "Gem Glow" completo (11:30, cada
  10 s), "Stronger Than You" completo (4:11, cada 3 s), animatic de "The Answer" completo
  (11:26, cada 8 s), tráiler de la película completo (2:00, cada 2 s), recopilación de 1
  segundo por episodio completa (2:55, cada 2 s) y recopilación de TikToks completa (4:59, cada
  3 s) — 6 hojas de contacto revisadas con Read, más 2 fotogramas sueltos extra para medir
  paleta de sitios.
- **Colores medidos** con `herramientas/estilo.py` sobre 5 fotogramas propios (acantilado, Big
  Donut, Templo, cocina, playa al atardecer) — no de arte de fans.
