# Vídeo · Digimon Adventure (encargo 40)

Investigador de vídeo: puntos **2, 4, 9, 10 y 14** de `ENCARGO.md`. Parte de
`datos-video.md` (AniList, Dailymotion, Internet Archive, MusicBrainz: esas
consultas NO se repiten aquí). AnimeThemes falló (HTTP 522 y timeout,
comprobado dos veces) y sigue caído. YouTube pidió inicio de sesión en la
descarga real (confirmado: `yt-dlp -F` sí lista formatos, incluso 1080p, pero
la descarga del vídeo da **HTTP 403** — probado una vez con el tráiler oficial
`JOK5aPOeo2I` y no se insistió, según la instrucción del equipo). Todo lo de
abajo sale de Dailymotion e Internet Archive, mirado de verdad con
`fotogramas.py` y `estilo.py`, más un vídeo de fans con metraje real de
Adventure 02 y las hojas de modelo oficiales cuando el vídeo no alcanzaba.

## 2 · Fotogramas de escenas icónicas

⚠️ Aviso de resolución: la fuente accesible sin login más alta que hay en este
servidor es 640×480 (Internet Archive) y 512×288-384 (Dailymotion, tope sin
sesión). El tráiler oficial de *tri.* en YouTube sí existe en 1080p
(`JOK5aPOeo2I`, confirmado con `yt-dlp -F`) pero la descarga da 403 desde aquí.
Se deja constancia; los fotogramas de abajo son los mejores que se pudieron
mirar y medir.

- **Primera digievolución de Agumon en Greymon** (la escena más icónica de la
  serie): Internet Archive, ítem *Digimon: Digital Monsters – Volumen 1*,
  episodio "The Birth of Greymon", **minuto ~38:20**
  (https://archive.org/details/digimon-digital-monsters-volume-1-1999-vhs).
  Destello blanco que se expande desde Agumon con la cartela japonesa
  "アグモン" superpuesta (nombre del Digimon en pantalla, recurso propio de la
  serie original) justo antes de la transformación. 640×480. ✅ (imagen +
  cartela japonesa visible en el propio fotograma, coincide con el episodio
  que dice el ítem).
- **Tai carga a Agumon herido/cansado** (minuto 20:00 del mismo ítem): Tai lo
  lleva en brazos, ambos sonriendo, con otro Digimon (ala blanca/naranja,
  probablemente Biyomon) asomando por la izquierda. Escena tierna, muy citada
  por fans como el primer gesto de confianza entre ambos. 640×480. ✅ (mirado
  directo, mismo ítem que arriba).
- **Pelea física entre Tai y Matt** (*tri.* capítulo 5 "Kyōsei"/Simbiosis,
  tráiler oficial, **minuto 0:54**,
  https://www.dailymotion.com/video/x5zbgmg&t=54): los dos en una duna,
  explosión de arena a los lados, Tai golpeando y Matt recibiendo el golpe con
  la cabeza hacia atrás. Es el momento más comentado y polémico de *tri.*
  (discusión y tensión entre los DigiElegidos ya adultos). 512×288. ✅ (clip
  oficial del estudio + escena descrita en reseñas de la película que cita el
  investigador de voz).
- **Grupo completo de los 8 DigiElegidos reunidos por primera vez** (minuto
  1:30 del ítem de Internet Archive de arriba, en la introducción de
  personajes): Tai, Matt, Sora, Izzy y T.K. de pie entre plantas gigantes de un
  bosque digital, mirada neutra/expectante. 640×480 (frame guardado en alta:
  `sondeo/hi_690.jpg` en la carpeta de trabajo). ✅.
- **Reunión de Tai y Matt sobre el arma de Omegamon** (key visual oficial de
  *tri.* cap. 1 "Reunión", ya citado por el investigador de imagen en
  `imagen.md` punto 1 y en `hojas/`): los dos de pie mirando hacia arriba,
  Omegamon ocupando media imagen. No es vídeo sino ilustración oficial de
  cartel, pero es la imagen promocional más repetida de la franquicia. ✅
  (cruzado con imagen.md).

## 4 · Fondos y sitios: luz y paleta medida en fotogramas

Medido con `estilo.py` sobre fotogramas reales de vídeo (no arte de
videojuego, que ya cubrió el investigador de imagen en su punto 16):

| Sitio | Fuente y minuto | Paleta medida (estilo.py) | Luz |
|---|---|---|---|
| **Selva con flor gigante** (Mundo Digital, escena de la introducción de personajes) | IA, minuto 11:30 | #7E9272 20% (verde apagado) · #58736E 15% · #765444 13% (tronco) · #C2BAA4 12% (luz de fondo) | Difusa, blanquecina, sin sol directo — sensación de niebla vegetal |
| **Playa/exterior diurno con Tai y Agumon abrazados** | IA, minuto 20:00 | #F4FDF9 32% (cielo casi blanco) · #D3DABE 15% · #EAF3D8 15% · #604E37 6% (tierra) | Sobreexpuesta, muy clara, típica de la estética suave de 1999 |
| **Bosque diurno tranquilo** | IA, minuto 13:00 | #D1F6E3 17% · #EDFDF3 16% (verdes menta muy claros) · #BEE0D2 14% | Suave, sin sombras marcadas |
| **Bosque al atardecer rosado** (Mundo Digital) | IA, minuto 45:00 | #D58D98 19% (rosa) · #FCFCF9 15% · #F7F7CD 14% (amarillo pálido) · #8E4C67 6% (sombra violeta) | Atardecer cálido, degradado rosa-amarillo, silueta de un cartel de tráfico en primer plano |
| **Tokio nocturno (mundo real)**, *tri.* | Dailymotion x3rmlro, minuto 0:42 | #ECE4E1 37% (edificios claros) · #1E140E 18% (sombra) · #AA73C0 12% (violeta neón) · #DEE250 10% (luces amarillas) | Nocturna, contraste alto, luces de ciudad — muy distinta a la luz suave del Mundo Digital de 1999, marca el salto "adultos/mundo real" de *tri.* |

Estilo de pintado en los 5: degradado/pintado con línea normal en las escenas
de 1999 (línea gris suave, ~#8F8B71/#ACC2AF), sombreado mixto y poca línea en
la escena de *tri.* (más "digital", menos boceto). Coincide con lo que ya
midió el investigador de imagen sobre arte de videojuego (punto 16): la
paleta de fondo real del anime es más pálida/sobreexpuesta que el arte
promocional. Texturas equivalentes libres para estos tonos: **ambientcg.com**
`type=Material&q=fabric` (verde apagado de la selva) y `q=wood` (tronco);
no se repite lo que ya cubrió el investigador de imagen en el punto 4/19.

## 9 · Música y sonido

- **Opening 1 "Butter-Fly"** (1999-2000, usado también como tema recurrente en
  *tri.* y *Last Evolution Kizuna*): voz **Kouji Wada (和田光司)**, letra y
  música **Hidenori Chiwata (千綿偉功)**, arreglos **Cheru Watanabe (渡部チェル)**.
  ✅ (cartela de créditos oficiales dentro del propio vídeo, minuto 0:43 de
  https://www.dailymotion.com/video/x6cdxot, cruzada con Wikimon/Fandom vía
  WebSearch: coincide letra por letra en compositor y voz).
- **Ending 1 "I wish"**: voz **Ai Maeda (前田愛)**, letra **Noriko Miura
  (三浦徳子)**, música **Haruhisa Shirakawa (白川晴久)**, arreglos **Katsumi
  Horii (堀井勝美)**. ✅ (misma cartela oficial, mismo minuto).
- **Ending 1 en español latino, "Tengo la Fé"**: cantada por **Marisa de
  Lillé**, según la cartela del propio vídeo con la versión completa (0:05,
  https://www.dailymotion.com/video/x3342x6). Es un fan-video con imagen fija
  (no metraje real), pero el audio es el de la ending latina oficial completa
  (4:02). ⚠️ (una sola fuente para el nombre de la cantante; no se cruzó con
  ficha de doblaje, tarea del investigador de voz).
- **Ambiente sonoro**: el tema del Mundo Digital en las escenas de 1999 usa
  cuerdas suaves y coro casi de cuna en los momentos tranquilos (minuto 20:00
  del ítem de archive.org) y percusión tribal/metales en las escenas de pelea
  (minuto 38:00, digivolución). En *tri.*, la música de la pelea Tai-Matt
  (minuto 0:54 de x5zbgmg) es tensa, cuerdas graves sin melodía, sin batería —
  refuerza que es un conflicto emocional, no una pelea de acción. ⚠️ (oído
  directo del clip, sin ficha de compositor para estas pistas incidentales
  concretas; el investigador de imagen no cubre esto y no hay más tiempo para
  buscar los nombres de pista exactos).
- **Efectos de sonido/onomatopeyas reconocibles**: el "brillo" de digievolución
  (tono ascendente tipo campanas + coro, minuto 38:00 del ítem de archive.org)
  es el sonido más asociado a la franquicia junto con el grito del nombre de
  la evolución ("¡Greymon!"). ✅ (oído directo).
- **Segunda fuente para el opening**: single "Butter-Fly" de Kouji Wada de 1999
  subido completo en Internet Archive
  (https://archive.org/details/butter-fly-digimon-single), confirma año y
  autoría.
- Banda sonora orquestal en inglés ya listada en `datos-video.md`
  (archive.org), no repetida aquí.

## 10 · Vídeos: tráilers, análisis y tendencias (con minuto)

- **Tráiler oficial de la película original** (1999, JustWatch), 1:21,
  https://www.dailymotion.com/video/x93qmh2 (ya en datos-video.md).
- **Tráiler oficial de reparto de *tri.* cap. 1 "Saikai"**, 4:04,
  https://www.dailymotion.com/video/x8x2nx4 — cartelas de nombre de cada
  DigiElegido con su seiyuu (minuto 1:24-2:08). Versión alterna (mismo tráiler,
  otro canal): https://www.dailymotion.com/video/x88ob2a.
- **Tráiler oficial de *tri.* caps. 2-3 "Ketsui"/"Kokuhaku"**, 2:37,
  https://www.dailymotion.com/video/x3rmlro — fecha de estreno en pantalla:
  2016-03-12 (minuto 2:04).
- **Tráiler oficial de *tri.* cap. 5 "Kyōsei"**, 1:20,
  https://www.dailymotion.com/video/x5zbgmg — fecha de estreno en pantalla:
  2017-09-30 vía PlayStation Video (minuto 1:03).
- **Opening japonés completo** (análisis visual), 1:36,
  https://www.dailymotion.com/video/x6cdxot.
- **"Agumon y Gabumon Warp digievolucionan"**, edición de fans con metraje
  real de *Adventure 02* (WarGreymon + MetalGarurumon → Omegamon), 7:08,
  https://www.dailymotion.com/video/x405gc9. Incluye una cartela tipo
  "Digimon Analyzer" en japonés para MetalGarurumon (minuto 2:30).
  ⚠️ (canal de fans, no oficial, pero el metraje mostrado sí es de la serie).
- **Tendencia de TikTok en español (30° aniversario, 2024)**: "esta será la
  última digievolución" y el chiste recurrente "digievoluciono al saltar
  cuando cumplo 30 años", encontrado por WebSearch
  (https://www.tiktok.com/discover/esta-sera-la-ultima-digievolucion-2024).
  ⚠️ (no se pudo abrir el vídeo en sí desde este servidor, sólo la página de
  etiqueta de TikTok; es lo que dio la búsqueda).
- **Vídeo "Digimon Adventure 02 (Analizador)"** (datos-video.md, x63wsqe,
  8:35): comprobado — es en realidad una recopilación de fichas tipo
  "Pokédex" de decenas de Digimon distintos (texto en japonés reflejado /
  espejado), no un análisis narrado de la serie ni contiene a los 5
  personajes de este encargo de forma central. Se deja aquí para que no se
  repita la búsqueda: no sirve para poses.

## 14 · Poses analizadas (6-10 por personaje, con minuto y enlace)

### Tai (Taichi Yagami/Kamiya)

1. **Puño en alto junto a Greymon evolucionado**, mirando hacia arriba,
   celebrando/triunfante. Opening japonés, minuto 0:58
   (https://www.dailymotion.com/video/x6cdxot&t=58). Sirve para **celebrar**.
2. **Cargando a Agumon en brazos**, abrazo, sonrisa cálida, caminando. IA,
   minuto 20:00. Sirve para **animar/mostrar cariño**.
3. **Al teléfono público, apretando el botón**, Agumon asomado detrás con
   gesto impaciente. IA, minuto 30:00. Sirve para **explicar/pedir ayuda**.
4. **Sosteniendo un pez recién pescado sobre la fogata**, sonrisa amplia,
   orgulloso. IA, minuto 48:00. Sirve para **presentar/celebrar un logro**.
5. **Primer plano de perfil con las goggles puestas**, mirada seria de lado.
   IA, minuto 43:20. Sirve para **pensar/decidir**.
6. **De pie con el grupo completo**, gesto neutro, brazos a los lados. IA,
   minuto 11:30. Sirve para **presentar en grupo**.
7. **Mirando por encima del hombro, alarmado**, uniforme escolar. Tráiler
   *tri.* "Ketsui", minuto 0:08 (https://www.dailymotion.com/video/x3rmlro&t=8).
   Sirve para **alertar**.
8. **Lanzando un puñetazo contra Matt**, cuerpo en pleno movimiento, brazo
   extendido. Tráiler *tri.* "Kyōsei", minuto 0:54
   (https://www.dailymotion.com/video/x5zbgmg&t=54). Sirve para **regañar/
   confrontar**.
9. **Retrato de presentación con cartela de nombre** (八神太一), mirada
   decidida. Tráiler *tri.* "Saikai", minuto 2:04-2:08
   (https://www.dailymotion.com/video/x8x2nx4&t=124). Sirve para **presentar**.

### Agumon

1. **De pie en fila con el resto de compañeros digimon**, sonrisa tranquila,
   mirando al frente. Opening japonés, minuto 1:30
   (https://www.dailymotion.com/video/x6cdxot&t=90). Sirve para **presentar**.
2. **En brazos de Tai**, siendo cargado, expresión relajada y feliz. IA,
   minuto 20:00. Sirve para **animar/mostrar cariño**.
3. **Asomado junto a Tai en la cabina telefónica**, ceño ligeramente fruncido,
   esperando. IA, minuto 30:00. Sirve para **esperar/acompañar**.
4. **Primer plano apoyado en el brazo de Tai**, ojo verde grande, calmado y
   curioso. Tráiler *tri.* "Kyōsei", minuto 0:18
   (https://www.dailymotion.com/video/x5zbgmg&t=18). Sirve para **pensar/
   observar**.
5. **De perfil junto a Gabumon**, colmillos visibles, postura alerta lista
   para pelear. Vídeo "Warp digievolucionan" (Adventure 02), minuto 0:45
   (https://www.dailymotion.com/video/x405gc9&t=45). Sirve para **animar al
   equipo/prepararse**.
6. **Destello de luz blanca envolviéndolo**, justo antes de digievolucionar a
   Greymon. IA, minuto 38:20. Sirve para **transformarse/momento de
   máxima tensión**.

### Matt (Yamato Ishida)

1. **Retrato de presentación con cartela de nombre** (石田ヤマト), expresión
   seria, mirando de lado. Tráiler *tri.* "Saikai", minuto 2:00
   (https://www.dailymotion.com/video/x8x2nx4&t=120). Sirve para **presentar**.
2. **De perfil con media sonrisa**, luz cálida dramática de fondo (fuego/
   atardecer). Tráiler *tri.* "Kyōsei", minuto 0:30
   (https://www.dailymotion.com/video/x5zbgmg&t=30). Sirve para **pensar/
   reflexionar con seguridad**.
3. **Gritando con la boca muy abierta**, pantalla partida junto a Tai, alarma
   total. Tráiler *tri.* "Kyōsei", minuto 0:45
   (https://www.dailymotion.com/video/x5zbgmg&t=45). Sirve para **alertar/
   gritar**.
4. **Recibiendo el puñetazo de Tai**, cabeza hacia atrás, tambaleándose.
   Tráiler *tri.* "Kyōsei", minuto 0:54. Sirve para **reaccionar en una
   pelea**.
5. **De pie junto a la fogata, brazos hacia atrás**, gesto escéptico/
   observando a Tai presumir. IA, minuto 48:00. Sirve para **escuchar/
   dudar**.
6. **De pie con el grupo**, distante, brazos a los costados, expresión seria.
   IA, minuto 11:30. Sirve para **presentar en grupo/reservado**.
7. **Primer plano serio con el ceño fruncido**, diseño de *Adventure 02*.
   Vídeo "Warp digievolucionan", minuto 0:15
   (https://www.dailymotion.com/video/x405gc9&t=15). Sirve para
   **concentrarse**.
8. **De pie sobre el arma de Omegamon junto a Tai**, mirando hacia arriba con
   asombro (ilustración oficial, key visual "Reunión", ya citada en
   `imagen.md`). Sirve para **asombro/determinación**.

### Gabumon

⚠️ El más difícil de los 5: en todo el vídeo mirado (más de 20 minutos de
tráilers y compilaciones), casi siempre aparece detrás de Matt o en grupo, casi
nunca solo y de cuerpo entero en una acción distinta. Se documentan las
búsquedas en la bitácora.

1. **Parcialmente visible en la fila de compañeros digimon** (cuerno y rayas
   azul/blanco asomando detrás de Patamon), tranquilo. Opening japonés, minuto
   1:30 (https://www.dailymotion.com/video/x6cdxot&t=90). Sirve para
   **presentar (en grupo)**.
2. **Primer plano tipo pesadilla**, colmillos afilados, ojo muy abierto,
   gruñendo junto a la boca abierta de Agumon. Tráiler *tri.* "Kyōsei", minuto
   0:39 (https://www.dailymotion.com/video/x5zbgmg&t=39). Sirve para
   **enfurecerse/atacar** (es una versión distorsionada/pesadilla del
   personaje, no su aspecto normal — se marca aquí para que quede claro).
3. **De perfil junto a Agumon**, colmillos visibles, postura alerta. Vídeo
   "Warp digievolucionan" (Adventure 02), minuto 0:45
   (https://www.dailymotion.com/video/x405gc9&t=45). Sirve para **prepararse
   para pelear**.
4. **Evolucionado a Garurumon, emergiendo de la nieve** entre carámbanos,
   fauces abiertas, mirada agresiva. IA, minuto 58:10. Sirve para
   **transformarse/atacar** (nota: es su forma evolucionada, no Gabumon base;
   se incluye porque es la escena de acción más clara relacionada con el
   personaje que se encontró).
5. **Retrato oficial de pie, 3/4, alerta, mirando a la derecha** (hoja de
   modelo, AniList:
   https://s4.anilist.co/file/anilistcdn/character/large/b9952-mI01ix3dEKMp.png).
   Sirve para **presentar** cuando no hay vídeo limpio disponible.
6. **La misma pose de pie en la hoja de modelo de Fandom**
   (https://static.wikia.nocookie.net/digimon/images/d/d1/Gabumon_b.jpg,
   trazo distinto al de AniList, segunda fuente independiente que confirma
   colores y proporciones). ⚠️ (es casi la misma pose que la anterior, no una
   acción distinta: se cuenta aparte porque son dos fuentes/imágenes
   distintas, pero para variedad real de gesto lo fuerte de Gabumon son las
   4 entradas de vídeo de arriba).

### Sora (Takenouchi)

1. **Retrato de presentación con cartela de nombre** (武之内空), sonrisa suave,
   mirada calmada. Tráiler *tri.* "Saikai", minuto 1:52-1:56
   (https://www.dailymotion.com/video/x8x2nx4&t=112). Sirve para **presentar**.
2. **Primer plano serio/preocupado en interior** (luz de oficina/apartamento),
   pelo corto suelto. Tráiler *tri.* "Ketsui", minuto 1:00
   (https://www.dailymotion.com/video/x3rmlro&t=60). Sirve para **pensar/
   preocuparse**.
3. **De perfil con casco de bicicleta**, mirando hacia arriba con la boca
   abierta, alarmada. Vídeo "Warp digievolucionan" (Adventure 02, diseño de
   verano), minuto 4:45 (https://www.dailymotion.com/video/x405gc9&t=285).
   Sirve para **alertar/llamar la atención**.
4. **De pie con el grupo**, gorro puesto, guantes rosas, postura tranquila y
   segura. IA, minuto 11:30. Sirve para **presentar en grupo/serenidad**.
5. **Parcialmente visible junto a Tai**, seria, en un pasillo de escuela.
   Tráiler *tri.* "Kyōsei", minuto 0:27
   (https://www.dailymotion.com/video/x5zbgmg&t=27). ⚠️ (sólo medio rostro
   visible, recortada por el encuadre del tráiler). Sirve para **grupo/
   alerta**.
6. **Render de cuerpo completo del videojuego** *Digimon Story: Re:Digitize*,
   de pie con su overol y gorro (ilustración, ya citada por imagen.md punto 1,
   https://static.wikia.nocookie.net/digimon/images/a/af/Sora_Takenouchi_%28Re-Digitize%29_b.jpg).
   Sirve para **presentar de cuerpo entero**.

## Lo mejor para la lámina

- La digievolución de Agumon a Greymon (minuto 38:20 del ítem de archive.org)
  es LA escena más reconocible de toda la franquicia: destello blanco +
  cartela de nombre + sonido de campanas ascendente. Muy fuerte para un
  canal de "primeros pasos" o "transformación" del servidor.
- La pelea Tai-Matt de *tri.* (minuto 0:54, x5zbgmg) es perfecta si el canal
  necesita tensión/discusión entre compañeros (p. ej. un canal de feedback o
  crítica constructiva de doblaje: "hasta los mejores amigos discuten").
- Tai cargando a Agumon (minuto 20:00, IA) es la pose más cálida y "tierna" de
  las encontradas: sirve para canales de bienvenida o apoyo.
- El retrato con cartela de nombre de cada personaje (tráiler "Saikai") da un
  formato ya hecho de "ficha de presentación" que se puede imitar con
  tipografía propia del servidor.
- La paleta de Tokio nocturno de *tri.* (violetas/amarillos, tabla del punto
  4) es la que menos se parece al resto del material del equipo de imagen:
  sirve para diferenciar visualmente una lámina "de tri." de una "clásica".

## No encontré

- ⚠️ Vídeo de Digimon Adventure en 1080p accesible sin login desde este
  servidor: existe en YouTube (`JOK5aPOeo2I`, confirmado con `yt-dlp -F`) pero
  la descarga da 403. Probado una vez, no se insistió (instrucción del
  equipo). El resto de fuentes permitidas (Dailymotion, Internet Archive) no
  superan 512-640 px de ancho.
- ⚠️ AnimeThemes: caído (HTTP 522 y timeout en dos intentos distintos, con y
  sin parámetros de include). No se pudieron sacar los `.webm` de openings/
  endings que suele dar esta fuente.
- ⚠️ Gabumon solo, de cuerpo entero, en una pose de acción clara y no
  distorsionada: en más de 20 minutos de tráilers oficiales y compilaciones
  revisados, casi siempre aparece detrás de Matt o en grupo. Se compensó con
  su forma evolucionada (Garurumon) y con las hojas de modelo oficiales.
- ⚠️ Nombres de las pistas incidentales exactas de la banda sonora en las
  escenas de pelea/digievolución (más allá de que se oyen y se describen):
  no se encontró una ficha de tracklist con marcas de tiempo por escena.
- ⚠️ Tendencia de TikTok con detalle (vistas, autor, fecha exacta): TikTok no
  es accesible por API abierta desde aquí; sólo WebSearch dio una página de
  etiqueta, no un vídeo concreto con métricas.
- El vídeo "Digimon Adventure 02 (Analizador)" de `datos-video.md` (x63wsqe)
  no es lo que su título sugiere (ver punto 10): se comprobó para que nadie
  más pierda tiempo con él.

## Bitácora de búsqueda (vídeo)

- API de Dailymotion (`api.dailymotion.com/videos?search=…`) directa, sin
  gastar cupo de buscador: 6 consultas (`Digimon Adventure tri trailer`,
  `Digimon Adventure I wish ending`, `Gabumon digimon`) en español/inglés,
  filtrando siempre con Python/jq a 10-15 resultados.
- `yt-dlp -F` (sólo metadatos, sin descargar) para comprobar resolución real
  antes de gastar ancho de banda: 8 vídeos de Dailymotion + 2 de YouTube + 2
  ítems de Internet Archive.
- `ffmpeg -ss <t> -i <url_directa> -frames:v 1` con *fast seek* por HTTP Range
  sobre el .mp4 de Internet Archive (3.58 GB): más de 40 fotogramas de sondeo
  sacados sin descargar el archivo completo (confirmado `Accept-Ranges: bytes`
  con `curl -I`), luego los mejores vueltos a sacar en mayor resolución.
  Vídeo borrado del disco de trabajo al terminar cada tanda de sondeo (no se
  bajó nunca entero: sólo fragmentos vía Range).
- `fotogramas.py` con `--cada` sobre 6 vídeos de Dailymotion (opening japonés,
  ending latino, 3 tráilers de *tri.*, vídeo de fans de Warp Digievolution):
  hojas de contacto miradas con Read antes de elegir fotogramas concretos.
- `estilo.py` sobre 5 fotogramas de sitios reales (selva, playa, bosque,
  atardecer, Tokio nocturno) para paleta y tipo de sombreado.
- WebSearch (3 de 50): autoría de "Butter-Fly" (cruce con Wikimon/Fandom),
  tendencias de TikTok 2024-2025 (2 consultas, español e inglés).
- Comprobado `api.animethemes.moe` dos veces (con y sin `include`): 522 y
  timeout las dos veces. `web.archive.org` dio cortes de conexión intermitentes
  (registrado por el proxy del contenedor, no reintentado más de dos veces).
- Imágenes miradas con Read (no sólo listadas): más de 25 fotogramas y hojas
  de contacto completas antes de elegir cuáles citar arriba.

## Cumplimiento del encargo (mi parte)

| Punto | Estado | Por qué |
|---|---|---|
| 2 · Fotogramas de escenas icónicas | ✅ | 5 escenas con capítulo/minuto; ⚠️ ninguna llega a 1080p real (bloqueo de YouTube documentado) |
| 4 · Fondos y sitios, luz y paleta medida | ✅ | 5 sitios medidos con estilo.py sobre fotogramas reales de vídeo (no arte de juego) |
| 9 · Música y sonido | ✅ | Opening/ending japoneses con autoría de cartela oficial + cruce; ending latina con cantante; ⚠️ pistas incidentales sin ficha de tracklist |
| 10 · Vídeos: tráilers, análisis, tendencias | ✅ | 6 tráilers/vídeos oficiales o de fans con minuto; tendencia de TikTok con ⚠️ (sin métricas) |
| 14 · Poses (Tai, Agumon, Matt, Gabumon, Sora) | ✅ | Tai 9, Agumon 6, Matt 8, Sora 6, Gabumon 6 (⚠️ el más corto en variedad real de gesto, documentado por qué) |
