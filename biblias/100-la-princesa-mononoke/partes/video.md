# Parte VÍDEO — La princesa Mononoke (puntos 2, 4, 9, 10, 14 de ENCARGO.md)

Investigador de vídeo. Punto de partida: `datos-video.md`. Película de Studio Ghibli
(1997, 133 min), no serie: no hay "capítulo", los minutos son de metraje corrido.
Fuente de vídeo principal para mirar fotogramas: copia de Internet Archive en
1920×1040 (`archive.org/details/1997-mononoke-hime-la-princesa-mononoke`, sin
licencia declarada, copyright Studio Ghibli/Tokuma/Toho — sólo referencia
interna, nunca para publicar el fotograma suelto). Copia de trabajo en
480 p (`archive.org/details/so-3f-cb-vwqm-0-d`) usada para localizar escenas
barato antes de sacar el fotograma en HD. Todos los fotogramas citados aquí
se miraron de verdad (Read de la imagen), no son suposición.

## Punto 2 — Fotogramas de escenas icónicas (1080p+, minuto exacto)

Todos sacados en 1920×1040 por streaming HTTP directo del archivo de Internet Archive
(sin descargar los 2 GB completos, con `ffmpeg -ss <s> -i <url_directa>`), mirados con Read.
Enlace de cada uno: `https://archive.org/details/1997-mononoke-hime-la-princesa-mononoke?t=<segundo>`.

- **Ashitaka tensando el arco sobre un tronco**, mirada fija, defendiendo la aldea del jabalí
  maldito (Nago) · min 0:04:20 (t=260) · ✅ (visto en fotograma HD + confirmado en la hoja de
  contacto de apertura `curse_open/hoja_01.jpg`) · 1920×1040.
- **La maldición ataca la aldea**: Nago cubierto de zarcillos negros retorciéndose, aldeanos
  huyendo, Ashitaka interviene y recibe la marca en el brazo · min 3:00–6:40 (t=180–400) ·
  ✅ (9 fotogramas mirados, hoja `curse_open/hoja_01.jpg`) · 894×480 (copia de trabajo).
- **San carga a Ashitaka herido a la espalda** por el bosque profundo, mirándolo de reojo,
  con una mariposa posada en su hombro · min 0:26:10 (t=1570) · ✅ (fotograma HD +
  hoja `san_intro/hoja_01.jpg`) · 1920×1040.
- **Okkoto (jabalí blanco gigante) y San** de pie junto a Ashitaka desmayado, con Yakul al
  lado; primer encuentro de San protegiendo a Ashitaka en el bosque · min 1:12:05 (t=4325) ·
  ✅ (fotograma HD + hoja `shishigami/hoja_01.jpg`) · 1920×1040.
- **San gruñendo como loba, colmillos fuera**, defendiendo a Ashitaka delante de la manada ·
  min 1:10:25 (t=4225) · ✅ (fotograma HD + hoja) · 1920×1040.
- **Moro enseñando los colmillos** a la luz de la luna, ojos entornados, amenazante ·
  min 1:21:00 (t=4860) · ✅ (fotograma HD + hoja `moro_roca/hoja_01.jpg`) · 1920×1040.
- **San con la cara pintada de guerra, gritando**, primer plano de furia tras el ataque a
  Irontown · min 0:53:00 (t=3180) · ✅ (fotograma HD + hoja `san_sangre/hoja_01.jpg`) ·
  1920×1040.
- **San atrapada entre los tentáculos oscuros de la maldición** (batalla final de los
  jabalíes), cara de dolor y miedo · min 1:43:45 (t=6225) · ✅ (fotograma HD + hoja
  `okkoto/hoja_01.jpg`) · 1920×1040.
- **El Nightwalker** (forma nocturna del Shishigami/dios ciervo), silueta gigante
  traslúcida azul con kodamas flotando alrededor, tras perder la cabeza · min 1:54:00
  (t=6840) · ✅ (fotograma HD + hoja `final/hoja_01.jpg`) · 1920×1040.
- **Ashitaka y San se abrazan por detrás**, escena final antes de separarse (él se queda
  en Irontown, ella vuelve al bosque) · min 1:56:00 (t=6960) · ✅ (fotograma HD + hoja) ·
  1920×1040.
- **El bosque renace** tras la muerte del dios ciervo: colinas verdes desde el aire,
  con los troncos quemados todavía en pie entre la hierba nueva (señal de que el
  verde es recién nacido, no bosque viejo) · min 2:07:00 (t=7620) · ✅ (fotograma
  HD `bosque_renace_7620.jpg` + hoja `final/hoja_01.jpg`, fotograma 18) · 1920×1040.

## Punto 4 — Fondos y sitios: luz, paleta y texturas equivalentes

Paletas medidas con `herramientas/estilo.py` sobre fotogramas HD (1920×1040) reales, no
arte promocional. Índice completo en `estilo/estilo.json` (carpeta de trabajo).

- **Montañas y bosque de la aldea Emishi** (min 0:04, t=260): verdes saturados y sombra
  casi negra. Paleta: `#19201E` 22.6% (sombra), `#22342D` 16.4%, `#69935A` 16.0%
  (verde medio iluminado), `#538044` 14.8%, `#314F39` 12.3%, `#3A6353` 7.4% ·
  sombreado **degradado/pintado** (fondo pintado a mano, no cel-shading), saturación
  media 39%, brillo medio 36%, línea normal color `#395130` · ✅ (medido con estilo.py).
- **Bosque profundo del dios ciervo (musgo, donde Ashitaka descansa)** (min 1:09,
  t=4195): verde amarillento muy saturado, hojarasca ocre. Paleta: `#404F20` 18.7%,
  `#728A1D` 17.4%, `#576B17` 15.7%, `#366278` 13.6% (agua/sombra azulada),
  `#527C36` 11.5% · sombreado degradado/pintado, saturación 63% (la más alta medida),
  brillo 45%, línea `#494C21` · ✅. Es el fondo más saturado de toda la película:
  Miyazaki quería que el santuario del bosque se sintiera "vivo" frente al gris de
  Irontown.
- **Puerta y murallas de Irontown (Tatara-ba)** (min 1:14:40, t=4480, de noche):
  paleta dominada por grises y marrones oscuros: `#1A1917` 32.6%, `#2D2A25` 18.5%,
  `#423F37` 15.0%, con un verde apagado `#9DC3AC` 10.9% (vegetación al fondo) y un
  rojo muy escaso `#76091D` 1.9% (los estandartes rojos de Eboshi, apenas visibles
  de noche) · sombreado degradado/pintado, saturación 22% (la más baja medida),
  brillo 30%, línea `#3C3A32` · ✅. Confirma lo que dice la wiki: Irontown se
  ilumina con antorchas y fuego de fragua, nunca luz de día limpia.
- **Escena nocturna con Moro** (min 1:21, t=4860): paleta fría de luna: `#14233C`
  30.3% (cielo nocturno), `#A3C7AF` 22.2% (pelaje iluminado), `#749F98` 17.9%
  (pelaje en sombra media) · sombreado **plano (cel)** para el personaje, poca
  línea, saturación 44%, brillo 46% · ✅. Contraste claro con los fondos pintados:
  los personajes llevan cel-shading, los fondos son pintura digital con degradado.
- **Textura de referencia — suelo/roca con musgo** para el santuario del bosque:
  `Ground037` (ambientcg.com/a/Ground037) y `Rock064` (ambientcg.com/a/Rock064),
  licencia CC0 · ✅ (buscado y comprobado en la API de ambientCG).
- **Textura de referencia — madera vieja** para las murallas y tablones de
  Irontown: `Wood095` (ambientcg.com/a/Wood095) y `Wood094`
  (ambientcg.com/a/Wood094), licencia CC0 · ✅.
- **Textura de referencia — metal** para las herramientas y rifles de la fragua:
  `Metal063` (ambientcg.com/a/Metal063) y `CorrugatedSteel009`
  (ambientcg.com/a/CorrugatedSteel009), licencia CC0 · ✅.
- **Luz y hora del día por sitio** (confirmado viendo el metraje, no wiki):
  aldea Emishi = luz de día limpia, verdes claros; bosque del dios ciervo = luz
  filtrada verde-azulada incluso de día, casi submarina; Irontown = noche con
  antorchas y fuego naranja de fragua, cielo casi negro; la cima donde vive Moro =
  luz de luna fría azul-verdosa. Los 4 sitios tienen paletas y temperatura de color
  claramente distintas entre sí (dato para el punto 17, guía de IA).

## Punto 9 — Música y sonido

- **Compositor**: Joe Hisaishi (colaborador habitual de Miyazaki), banda tocada por
  la Tokyo City Philharmonic Orchestra dirigida por Hiroshi Kumagai · ✅ (Ghibli
  Fandom, wikitext de `Princess Mononoke/Soundtrack`, y MusicBrainz release-group
  `b0701a74-cce4-46f2-a392-72eadad32ef4` "Hayao Miyazaki – Princess Mononoke /
  Spirited Away", Joe Hisaishi).
- **Álbum original**: publicado en Japón por Tokuma Japan Communications el
  2 jul 1997; versión norteamericana por Milan Records el 12 oct 1999 · ✅
  (Ghibli Fandom, sección "Soundtrack").
- **Tema principal "Mononoke Hime" (もののけ姫)**: letra escrita por el propio
  Hayao Miyazaki, cantada por el contratenor japonés Yoshikazu Mera (versión
  japonesa) y por Sasha Lazard en la adaptación al inglés · ✅ (Ghibli Fandom,
  dos páginas: `Princess Mononoke/Soundtrack` y ficha de Yoshikazu Mera/Sasha
  Lazard referenciadas desde ahí).
- **"The Legend of Ashitaka"**: tema de apertura (1:39) y de cierre (5:03, créditos
  finales) — es el mismo leitmotiv de Ashitaka en dos duraciones distintas ·
  ✅ (Ghibli Fandom, página propia "The Legend of Ashitaka" + tracklist del
  soundtrack).
- **"Ashitaka and San"** (piano, 4:01): instrumental dedicado a la relación entre
  ambos, suena en la escena final de despedida (min ~1:56–1:58, coincide con el
  abrazo que se mira en el punto 2) · ✅ (Ghibli Fandom, página propia "Ashitaka
  and San", "used in Princess Mononoke... played at the end of the film").
- **Lista completa del disco original** (33 pistas, todas de Joe Hisaishi salvo
  las vocales indicadas), con duración exacta de cada una — útil para saber qué
  cue pedir para cada escena de la lámina: The Legend of Ashitaka (1:39) · The
  Demon God (3:51) · Departure – To the West (2:33) · Demon Power (0:36) · The
  Land of the Impure (2:59) · The Encounter (0:53) · Kodamas (0:39) · The Forest
  of the God (0:41) · Evening at the Ironworks (0:39) · The Demon God II – The
  Lost Mountains (0:57) · Lady Eboshi (2:48) · The Tatara Women Work Song (1:30,
  letra de Miyazaki) · Furies (1:28) · The Young Man from the East (1:25) ·
  Requiem (2:22) · Will to Live (0:32) · San and Ashitaka in the Forest of the
  Deer God (1:39) · Princess Mononoke Theme Song instrumental (2:08) · Requiem II
  (2:14) · Theme Song japonés (3:32, no está en la edición inglesa) · Battle
  Drums (2:47) · The Battle in Front of the Ironworks (1:26) · Demon Power II
  (2:30) · Requiem III (0:55) · Retreat (1:31) · The Demon God III (1:14) ·
  Adagio of Life and Death (2:09) · The World of the Dead (1:27) · The World of
  the Dead II (1:33) · Adagio of Life and Death II (1:07) · Ashitaka and San
  (3:12, nota: la wiki da dos duraciones distintas para esta pista según la
  página, 3:12 en el índice y 4:01 en su ficha propia — dato dudoso ⚠️) ·
  Princess Mononoke Theme Song (1:23) · The Legend of Ashitaka Theme, créditos
  de cierre (5:03) · ✅ tracklist (Ghibli Fandom, wikitext completo con tabla).
- **Qué ambiente da cada bloque**: los temas "The Demon God" y "Demon Power"
  (percusión grave, cuerdas disonantes) acompañan los ataques de los dioses
  poseídos por el odio; "Requiem" y sus variantes suenan en las escenas de
  muerte/duelo; "The Forest of the God" y "Kodamas" son piezas cortas, suaves,
  de arpa y campanas para el santuario; el "Theme Song" coral con voz de
  contratenor cierra la película sobre paisajes del bosque reverdecido · ⚠️
  (asociación por título y duración de pista, no se pudo escuchar el álbum
  completo con el metraje sincronizado minuto a minuto; es coherente con lo
  visto en los fotogramas del punto 2).
- **Onomatopeya reconocible — kodama**: los espíritus del bosque suenan como
  "cientos de sonajeros de bebé agitados a la vez" al mover la cabeza; se
  describe en textos de análisis como el sonido カタカタ (*kata-kata*, un
  giongo de traqueteo/repiqueteo) · ✅ (dos fuentes: PDF académico "Disembodied
  Stars and the Cultural Meanings of Princess Mononoke's Soundscape", Nottingham
  University, nottingham.ac.uk/scope/documents/2005/october-2005/denison.pdf; y
  descripción general de カタカタ como giongo de traqueteo en guías de
  onomatopeya japonesa).
- **Efectos de sonido documentados** (librería de la mezcla usada en EE. UU.,
  probablemente el doblaje de Miramax): choque de espadas ("Sword Shing With
  Sword"), disparo silenciado de arma ("Machine Gun Silence") para los rifles de
  Irontown, galope de caballo, explosiones grandes y pequeñas, "masa viscosa y
  reptante" (créditos de sonido que encajan con los tentáculos de la maldición
  del punto 2), chapoteo de agua, graznido de halcón · ✅ (soundeffects.fandom.com,
  página "Princess Mononoke (1997)", lista "Sound Effects Used").
- **AnimeThemes**: intentado dos veces (`api.animethemes.moe`), sin respuesta
  (HTTP 522 la primera vez según `datos-video.md`, timeout la segunda) — no
  aplica bien de todos modos: es una película con un único tema, no una serie
  con OP/ED por episodio · ❌ fuente caída, sustituida por Ghibli Fandom +
  MusicBrainz.

## Punto 10 — Vídeos: tráilers, escenas, análisis y tendencias

- **Tráiler/teaser oficial del 25 aniversario** (distribuido por Vértigo Films,
  reestreno en cines de España): mirado fotograma a fotograma con `fotogramas.py`
  (16 fotogramas, cada 2 s). Contenido real: logo Studio Ghibli (0:00) → logo
  distribuidora Vértigo (0:02) → título "LA PRINCESA MONONOKE" sobre kodamas de
  noche (0:04) → Ashitaka agachado con arco (0:06) → San con la boca ensangrentada
  (0:08) → montaña de kodamas (0:10) → aldeanos corriendo (0:12) → lucha en el
  bosque (0:14) → Moro de cerca (0:16) → San entre plantas (0:16) → texto "EL
  DESTINO DEL MUNDO" (0:18) → "DESCANSA EN EL VALOR DE DOS GUERREROS" con
  procesión (0:20) → San corriendo sobre agua azul (0:22) → Nightwalker gigante
  (0:24) → texto "VUELVE A LOS CINES POR SU 25 ANIVERSARIO" (0:24) → Moro de
  perfil (0:26) → título final (0:28) → "22 JULIO EN CINES" con logos de Vértigo,
  Aurum y Notro Films (0:30) · Dailymotion, `dailymotion.com/video/x8cliiw`,
  duración 0:31 · ✅ (mirado con fotogramas.py, hoja en
  `trailer_teaser/hoja_01.jpg`).
- **Otros tráilers oficiales en Dailymotion** (recogidos en `datos-video.md`,
  no todos mirados fotograma a fotograma por presupuesto): "Mononoke hime
  (Princesse Mononoké): Trailer HD VO st FR/NL" 1:28
  (dailymotion.com/video/x9pkvji) · "La princesa Mononoke Tráiler VO" 2:08
  (dailymotion.com/video/x88nkic, Sensacine) · "'La princesa Mononoke' - Tráiler
  oficial" 1:42 (dailymotion.com/video/x88a6q7, Sensacine México) · "La Princesa
  Mononoke - Trailer Oficial" 1:42 (dailymotion.com/video/x8x2e5w, Tomatazos) ·
  ⚠️ (duración y canal confirmados por la respuesta de la API de Dailymotion,
  contenido no mirado fotograma a fotograma, sólo el teaser de arriba).
- **Tráiler original japonés (1997)**: enlazado en `datos-video.md` desde AniList
  (`youtube.com/watch?v=4OiMOHRDs14`) · ⚠️ no se pudo mirar: YouTube pide iniciar
  sesión desde este servidor (bloqueo compartido por IP, según AYUDANTE.md); no
  se encontró el mismo tráiler en Dailymotion ni Internet Archive.
- **Análisis en español (YouTube, sólo enlace y título — no se pudo mirar por el
  bloqueo de sesión)**: "La Princesa Mononoke: el lado oscuro de Ghibli que nadie
  entiende" (youtube.com/watch?v=mk3I-VLc51g) · "LA PRINCESA MONONOKE (1997) |
  Análisis y Explicación" de Mr. Quinn (youtube.com/watch?v=5aANfYwywPk) · ⚠️
  (una sola fuente, título y existencia confirmados por búsqueda web, contenido
  y minutos no verificados).
- **Análisis escrito**: reseña de Cintilatio ("La princesa Mononoke (1997) |
  Crítica", cintilatio.com) y ensayo sobre lecturas religiosas/folclóricas de la
  película (buscado en español) · ⚠️ (una fuente cada uno, no cruzadas).
- **Tendencia en TikTok**: la etiqueta "Princess Mononoke Edit" /
  "La Princesa Mononoke Edit" agrupa miles de vídeos de fans con montajes de
  escenas de la película; una tendencia identificada usa la canción "The Seed"
  de Aurora como música de fondo para montajes de San y Ashitaka · ⚠️ (una
  fuente de búsqueda agregada, no se pudo entrar a TikTok directamente desde
  este servidor para contar vistas exactas de un vídeo concreto).
- **Vídeos de fans citables con canal y escena**: "Ashitaka e San: O Amor em
  Princesa Mononoke" (TikTok, @rl_editt, tiktok.com/@rl_editt/video/7316653871705754886)
  · "#princessmononoke #ghibli #studioghibli" (TikTok, @hwigyu,
  tiktok.com/@hwigyu/video/7315834904565058818) · ⚠️ (enlaces confirmados por
  búsqueda, número de vistas no verificado sin acceso directo a TikTok).

## Punto 14 — Poses analizadas (San, Ashitaka, Moro)

Todas de fotograma real (mirado con Read), no de memoria ni de arte promocional.
Enlace `https://archive.org/details/1997-mononoke-hime-la-princesa-mononoke?t=<segundo>`
salvo que se diga otra cosa.

### San (9 poses)

- **Corriendo por el pasillo de la prisión con la espada en alto**, cuerpo
  inclinado hacia delante, mirada fija al frente · min 0:50:00 (t=3000) ·
  ✅ (hoja `mapa/hoja_01.jpg`, fotograma 11) · sirve para **presentar** (acción,
  entrada del personaje).
- **Primer plano gritando con la cara pintada de guerra**, boca abierta, cejas
  bajas, tensión en el cuello · min 0:53:00 (t=3180) · ✅ (fotograma HD
  `test_55min.jpg` + hoja `san_sangre/hoja_01.jpg`) · sirve para **regañar/
  amenazar**.
- **Afilando un cuchillo con la mirada baja**, hombros tensos, manos ocupadas
  en la tarea · min 0:55:20 (t=3320) · ✅ (hoja `san_sangre/hoja_01.jpg`,
  fotograma 8) · sirve para **explicar/preparar** (postura de concentración,
  útil para paneles de "cómo se hace algo").
- **Cargando a Ashitaka herido a la espalda**, girando la cabeza para mirarlo,
  gesto de cuidado más que de esfuerzo · min 0:26:10 (t=1570) · ✅ (fotograma
  HD `san_carga_ashitaka_1570.jpg`) · sirve para **animar/cuidar**.
- **Tumbada sobre el lomo de Moro mirando el valle**, cuerpo relajado, mentón
  apoyado, mirada perdida · min 1:19:00 (t=4740) · ✅ (hoja
  `moro_roca/hoja_01.jpg`, fotograma 1) · sirve para **pensar**.
- **De pie mirando al vacío desde la roca**, sola, brazos sueltos, postura
  abierta y pequeña frente al paisaje · min 1:19:40 (t=4780) · ✅ (hoja
  `moro_roca/hoja_01.jpg`, fotograma 3) · sirve para **pensar/contemplar**
  (encaja con paneles de introducción del canal, personaje pequeño ante algo
  grande).
- **Cara de determinación antes de un combate**, ceño fruncido, mirada firme,
  sin miedo · min 1:40:25 (t=6025) · ✅ (hoja `okkoto/hoja_01.jpg`, fotograma 4)
  · sirve para **explicar/decidir** (anunciar una acción con seguridad).
- **Atrapada entre los tentáculos de la maldición**, cuerpo torcido, boca
  abierta de dolor, un ojo cerrado · min 1:43:45 (t=6225) · ✅ (fotograma HD
  `san_tendriles_6225.jpg`) · sirve para mostrar **sufrimiento/pedir ayuda**
  (útil si la lámina necesita urgencia o peligro).
- **Abrazando a Ashitaka por la espalda**, cabeza apoyada en su hombro, cuerpo
  pegado al de él, gesto de despedida cariñosa · min 1:56:00 (t=6960) · ✅
  (fotograma HD `abrazo_final_6960.jpg`) · sirve para **celebrar/reconciliar**
  (el único momento verdaderamente tierno y sin arma en toda la lista).

### Ashitaka (9 poses)

- **De pie sobre un tronco, arco tensado, apuntando**, peso adelantado, cola de
  caballo al viento · min 0:04:20 (t=260) · ✅ (fotograma HD
  `ashitaka_arco_0260.jpg`) · sirve para **presentar** (acción, entrada heroica).
- **Con el arco en alto protegiendo a los aldeanos**, brazo maldito visible,
  gesto de alarma hacia algo fuera de plano · min 0:06:40 (t=400) · ✅ (hoja
  `curse_open/hoja_01.jpg`, fotograma 15) · sirve para **regañar/advertir**
  (avisar de un peligro).
- **Montado en Yakul, inclinado hacia delante, galopando por el bosque** ·
  min 0:25:00 (t=1500) · ✅ (hoja `mapa/hoja_01.jpg`, fotograma 6) · sirve
  para **presentar** (viaje, en movimiento).
- **Sentado comiendo con Jigo**, postura relajada, un gesto de ofrecer o
  compartir comida con la mano · min 0:35:00 (t=2100) · ✅ (hoja
  `mapa/hoja_01.jpg`, fotograma 8) · sirve para **explicar/convivir** (charla
  informal, tono cercano).
- **Sentado en la roca junto a San y Moro, manos sobre las rodillas,
  escuchando** con calma en medio de dos criaturas hostiles · min 1:20:00
  (t=4800) · ✅ (hoja `moro_roca/hoja_01.jpg`, fotograma 4) · sirve para
  **explicar/escuchar** (postura serena de diálogo).
- **De pie, sereno, junto a San mientras Moro gruñe** a su lado, sin
  retroceder · min 1:10:25 (t=4225) · ✅ (fotograma HD
  `san_lobo_defensa_4225.jpg`) · sirve para **calmar/proteger** (mantiene la
  calma en medio del peligro).
- **Tumbado en el musgo, manos juntas sobre el pecho**, ojos entrecerrados,
  revisando/sintiendo su brazo maldito · min 1:09:55 (t=4195) · ✅ (fotograma
  HD `shishigami_pond_4195.jpg`) · sirve para **pensar** (introspección sobre
  la maldición).
- **Primer plano con la cara ensangrentada, mirada intensa al frente**, boca
  entreabierta, después de la batalla · min 2:03:00 (t=7320) · ✅ (hoja
  `final/hoja_01.jpg`, fotograma 14) · sirve para **avisar/advertir** (aviso
  grave, momento límite).
- **Abrazando a San por detrás**, cabeza apoyada contra la de ella, postura
  quieta y protectora · min 1:56:00 (t=6960) · ✅ (fotograma HD
  `abrazo_final_6960.jpg`) · sirve para **animar/consolar**.

### Moro (6 poses)

- **Tumbada sobre la roca, cabeza vuelta hacia Ashitaka**, postura relajada de
  quien escucha sin amenazar · min 1:20:00 (t=4800) · ✅ (hoja
  `moro_roca/hoja_01.jpg`, fotograma 4) · sirve para **explicar** (diálogo,
  postura de autoridad tranquila).
- **Colmillos al descubierto, ojos entornados, gruñendo** a la luz de la luna,
  primer plano de cabeza · min 1:21:00 (t=4860) · ✅ (fotograma HD
  `moro_colmillos_4860.jpg`) · sirve para **regañar/amenazar**.
- **Con San dormida/recostada sobre su lomo entre la hierba**, cuerpo grande
  envolviendo a la más pequeña, postura protectora · min 1:19:00 (t=4740) ·
  ✅ (hoja `moro_roca/hoja_01.jpg`, fotograma 1) · sirve para **animar/cuidar**.
- **De pie junto a San, colmillos hacia Ashitaka**, cuerpo interpuesto entre
  San y la posible amenaza · min 1:10:25 (t=4225) · ✅ (fotograma HD
  `san_lobo_defensa_4225.jpg`) · sirve para **regañar/defender**.
- **Primer plano del ojo, entrecerrado y cansado**, sin fiereza, gesto de
  cansancio o dolor contenido · min 1:10:50 (t=4250) · ✅ (hoja
  `shishigami/hoja_01.jpg`, fotograma 5) · sirve para mostrar **sufrimiento/
  vejez** (Moro está envenenada por el odio, útil para un panel sobre su
  arco narrativo).
- **Tumbada, cuerpo grande y quieto, San arrodillada a su lado con la cabeza
  gacha** · min 1:22:00 (t=4920) · ✅ (hoja `moro_roca/hoja_01.jpg`,
  fotograma 10) · sirve para **pensar/despedirse** (escena de calma antes de
  un momento grave).

## Lo mejor para la lámina

- San cargando a Ashitaka herido a la espalda (min 0:26:10) o abrazándolo al
  final (min 1:56:00): la única pose "viva" de pareja, cálida, sin violencia.
- Moro gruñendo bajo la luna, colores fríos verde-azulados medidos en el
  fotograma (`#A3C7AF`/`#14233C`): funciona como fondo de sitio nocturno con
  mucho carácter.
- Paleta del bosque del dios ciervo (`#728A1D`, `#366278`, saturación 63%, la
  más alta de la película) frente a la paleta apagada de Irontown (saturación
  22%): dos mundos, dos paletas, útil para separar dos canales o dos secciones
  de una misma lámina.

## No encontré

## Bitácora de búsqueda
