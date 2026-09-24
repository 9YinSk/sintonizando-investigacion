# Investigador de VÍDEO · Solo Leveling: el Sistema y las sombras

Puntos de ENCARGO.md: **2** (fotogramas de escenas icónicas), **4** (fondos y sitios), **9** (música y
sonido), **10** (vídeos), **14** (poses analizadas). Foco especial pedido por el encargo: cómo se
anima/renderiza la interfaz del Sistema y los efectos visuales de invocación de sombras.

YouTube pidió «inicia sesión» para descargar (bloqueo intermitente, confirmado varias veces). Funcionó en
cambio: **storyboards de YouTube sin login** (hojas de contacto oficiales, ±2 s, técnica nueva de esta
tanda — ver Bitácora), clips reales del anime re-subidos en **Dailymotion** (mirados enteros con
`fotogramas.py --cortes`), y un mirror del tráiler oficial en **Internet Archive**. AnimeThemes
(`api.animethemes.moe`) seguía caído (conexión TLS que cuelga hasta timeout, igual que el 522 avisado) tras
reintentarlo: usé la wiki (openings/endings con su ID de YouTube) + storyboards en su lugar.

## Hallazgos

### Punto 9 · Música y sonido

**Lista completa de openings, endings y OST**, sacada del wikitexto de `Template:Music_Navigation`
(solo-leveling.fandom.com) ✅:

- **Opening 1 · «LEveL»** — SawanoHiroyuki[nZk] : TOMORROW X TOGETHER, compuesta por Hiroyuki Sawano.
  Empieza en el [Episodio 1], termina en el [Episodio 12] (la cambian justo cuando Jinwoo se convierte en
  Monarca de las Sombras). Vídeo oficial YouTube `XqD0oCHLIF8` (Crunchyroll). ✅ (wiki + storyboard propio,
  ver Punto 10).
- **Opening 2 · «ReawakeR»** — LiSA ft. Felix (Stray Kids), letra de Benjamin/cAnON, música de Sawano.
  Empieza en el [Episodio 13] (arranque de la Temporada 2). ✅ (wiki, un solo dato — no encontré vídeo
  accesible para mirarlo, YouTube bloqueado en el intento; ⚠️ sin fotograma propio).
- **Ending 1 · «request»** — krage (compuesta y escrita por ella misma). Empieza en el [Episodio 2] (la
  wiki dice explícitamente: «the first time we get to see the ending "request"» es también la primera vez
  que aparecen los **cuadros del Sistema** en pantalla, mismo episodio). Vídeo oficial `CRZsOOOvg1I`. ✅.
- **Ending 2 · «UN-APEX»** — TK from Ling tosite sigure (吉田一郎不可触世界). Empieza en el [Episodio 13].
  Letra en japonés e inglés confirmada en la wiki (dos versiones, TV y completa). ✅.
- **OST 1 · «DARK ARIA»** (Sawano + vocalista XAI) — suena en el [Episodio 6] y el [Episodio 23]; la
  galería de la wiki la titula **«Kill or Be Killed»**. Reversión «DARK ARIA -ARISE-» con XAI y Laco. ✅.
- **OST 2 · «4eVR»** (Sawano, voces Laco/Benjamin/mpi) — suena en el [Episodio 10]; escena de la wiki
  **«Grinding XP»** (montaje de entrenamiento/subida de nivel). ✅.
- **OST 3 · «SHADOWBORN»** (Sawano, voces Benjamin/mpi) — Temporada 2, suena en los [Episodio 13],
  [Episodio 18] y [Episodio 25]; escena de la wiki **«Jinwoo vs All the Ice Bears»**. ✅.
- **OST 4 · «REVIVER»** (Sawano, voz SennaRin) — Temporada 2, [Episodio 21], escena **«It Was All Worth
  It»**: Jinwoo lleva el Elixir de Vida a su madre enferma en el hospital, la cura, y le piden que se una a
  la incursión de Jeju. Es el tema de la escena que más hace llorar según la propia wiki (nombre de la
  escena en la galería). ✅ (wikitexto del episodio + de la canción, dos páginas).
- **OST 6 · «HØWL»** (Sawano, voz Aimee Blackschleger) — [Episodio 24], escena **«Sung Jinwoo vs The Ant
  King»**: el clímax con Beru antes de que se una a las sombras (Beru debuta un episodio después, el 25).
  ✅.
- Los vídeos «MV» de estas OST en el canal de Sawano son **actuaciones en directo** (banda, piano, cello),
  no fotogramas del anime: los miré (storyboard, ver Bitácora) para confirmar el ambiente — luces rojas y
  cian cruzadas para DARK ARIA (urgencia), noir rojo/negro para SHADOWBORN (más orquestal-rock, sube la
  tensión), azul frío + piano/cello para REVIVER (la balada emotiva, encaja con la escena de la madre). ✅
  ambiente confirmado por mí viendo el vídeo; el encaje narrativo (qué escena) sale de la wiki.
- **Efectos de sonido de la interfaz**: en los tres clips reales que miré entero (ver Punto 10), cada caja
  «NOTIFICATION» entra con un **tintineo electrónico corto y agudo**, distinto del sonido grave de impacto
  de los golpes; no encontré una fuente escrita que lo confirme con nombre propio, así que queda ⚠️ (lo oí
  yo mismo en los tres clips, un solo tipo de fuente: mi propia escucha).
- No hay una **onomatopeya de texto** en pantalla para el sonido del Sistema (a diferencia de los golpes,
  que sí llevan letras coreanas/japonesas superpuestas en el manhwa, punto que cubre mejor el investigador
  de texto). ⚠️ dicho por descarte, no lo vi en ningún fotograma propio.

### Punto 10 · Vídeos (con minuto exacto)

**Tráiler oficial** — «Solo Leveling | OFFICIAL TRAILER 3» (Crunchyroll), mirror en Internet Archive
`youtube-n24l9gvM3XM` (13,2 MB, 854×480 medido), mirado ENTERO con `fotogramas.py --cortes` (87 planos,
0:00-2:20) y las hojas abiertas con Read:
- 0:00-0:16 créditos: «Original: CHUGONG · Original Illustration: DUBU · Written by: H-GOON», logo
  «SOLO LEVELING» tipografía angular con resplandor azul sobre fondo de circuito. ✅.
- 0:18-0:31 «weakest hunter of all mankind»: Jinwoo con gafas, uniforme escolar, discute con su amiga
  Song-yi sobre dejar de ser cazador («Don't tell me you're too stubborn to quit being a hunter»). ✅.
- 0:41-1:02 la Doble Mazmorra: «That huge stone statue... it was looking at us», explosión, Jinwoo
  ensangrentado en el suelo, ojo herido en primer plano, ruego «If I have another chance...!», puño con
  venas brillando en azul (min 1:00) — es el instante del «segundo despertar». ✅.
- **1:11-1:13 primera aparición en pantalla de una caja del Sistema dentro de material promocional**: en
  la habitación del hospital aparece un panel azul translúcido con la cabecera «NOTIFICATION» flotando
  junto a la mano de Jinwoo («No one else can see this but me?!»); toca el texto brillante con el dedo.
  Confirma que el Sistema es invisible para todos menos para el jugador. ✅ (mirado directamente en el
  fotograma, dos veces en el tráiler: 1:11 y 1:13).
- 1:32-1:45 «THIS WINTER» (cartela de campaña) + primer plano de un ojo azul con grietas de energía —
  mismo lenguaje visual de «grieta que brilla» que usa el Sistema para transformar sombras (ver Punto 2).
  ✅.
- `https://archive.org/details/youtube-n24l9gvM3XM` (vídeo completo descargado, 13,2 MB, 854×480; el
  archivo original en YouTube es `HkIKAnwLZCw`, que en el momento de mirar pedía login).
- También localicé, sin abrir por presupuesto de tiempo, el **tráiler oficial en doblaje hindi de
  Crunchyroll India** para la Temporada 2 «Arise from the Shadow» (mirror en Internet Archive,
  `solo-leveling-season-2-arise-from-the-shadow-official-hindi-dub-trailer-crunchyroll-india-1080p`, 64,9
  MB) — ⚠️ existencia confirmada (metadatos leídos), contenido no mirado fotograma a fotograma.
- **Tendencia en TikTok**: la escena «Arise» (Episodio 12, ver Punto 2) es un edit viral recurrente —
  decenas de cuentas usan el audio/clip bajo las etiquetas `#sololevelingarise`, `#sololevelingedits`
  («relive the toughest moments of Sung Jinwoo in ARISE»). ✅ (buscado en inglés, resultados de
  tiktok.com/discover consistentes en varias cuentas distintas).

**Escena icónica 1 — pelea contra Igris (Episodio 11 → 12, arco «Job Change»)**: clip real del episodio,
re-subido en Dailymotion, «Sung Jin Woo vs Igris (Full Fight) — Solo Leveling Ep 11»
(`dailymotion.com/video/x8xqany`, 2:43, 512×288 medido), mirado ENTERO con `--cortes` (91 planos):
- 0:06 cartela «KNIGHT COMMANDER IGRIS THE BLOODRED» en letra azul angular sobre la espada — presentación
  de jefe. ✅.
- 0:38-1:31 combate cuerpo a cuerpo: Jinwoo esquiva agachado, bloquea con las dos dagas en cruz, cae y
  rueda; texto en pantalla («Still no good!», «I guess you're being chivalrous, huh?») en subtítulo
  blanco simple (no es una caja del Sistema, es diálogo). ✅.
- **2:33 — caja «NOTIFICATION» del Sistema tras ganar**: panel azul traslúcido de bordes redondeados,
  icono de exclamación circulado arriba a la izquierda, texto «You have defeated [Knight Commander] Igris
  the Bloodred», fondo casi negro con veta azul. Coincide en diseño con la de 1:11 del tráiler y con la
  del Episodio 12 (ver abajo): confirma que ésta es la caja «de evento» estándar de toda la serie. ✅✅
  (tres apariciones independientes, mismo diseño).
- Medido con `estilo.py` sobre el fotograma de la sala del trono (roja): paleta dominante **#F46B7D**
  (18,7 %), **#C95460** (15,7 %), **#973D48** (12 %), acentos rosa vivo **#FB88A0**; sombreado en
  degradado/pintado, poca línea, línea de contorno **#76343C**, saturación 55 %, brillo 63 %. Luz cálida
  de candelabro dorado, ambiente de sala-trono gótica.

**Escena icónica 2 — «Arise», Episodio 12 (el Sistema entero, de principio a fin)**: clip real,
«Solo leveling First ARISE scenes» (`dailymotion.com/video/xb7cnoi`, 1:42, 512×288 medido), mirado
ENTERO con `--cortes` (43 planos). Es la secuencia clave para el encargo (interfaz + invocación):
- 0:00 «NOTIFICATION — Your job has changed [necromancer] ▼ [shadow monarch]»: el nombre de la clase
  vieja en blanco-cian, una flecha doble apuntando abajo, el nombre nuevo **en verde brillante** (medido
  **#02DE58**) — es el único texto verde de toda la secuencia, resalta el cambio bueno/logro.
- 0:08 «NOTIFICATION — Please designate a command word for [Skill: Shadow Extraction]» con un campo de
  texto vacío y cursor parpadeante debajo — el jugador tiene que escribir la palabra de mando.
- 0:14-0:24: silueta negra tipo sombra chino con **grietas de luz cian/blanca en zigzag** (como cristal
  rajado) recorriendo el cuerpo del caballero mientras se reconstruye — es la animación concreta de
  «extraer» una sombra: no es un contorno que se rellena, es luz agrietándose sobre negro sólido, con la
  capa roja de Igris como único color cálido en medio del azul.
- **0:52 — «Number of extractions possible: 1/3»**: NO es una caja, es una **cinta horizontal** (banda
  larga con doble filete azul, sin fondo sólido) con el texto en **rosa/carmesí** (medido **#E70D41**),
  no en cian — la serie usa el rosa para avisos de límite/riesgo, reservando el azul para información
  neutra y el verde para logros. Superpuesta sobre el efecto de extracción (fondo rojo sangre).
- 1:18 «NOTIFICATION — [Skill: Shadow Extraction] is successful.» (caja azul estándar) → 1:19 «LV.7
  Knight Rank. You may bestow a name.» con campo de texto → 1:22 el jugador escribe «Igris» — así nace el
  nombre del general en pantalla, letra por letra.
- 1:27-1:41: el cuerpo de Igris se termina de formar con las grietas cian sobre negro, cierra con el
  primer plano de los ojos de Jinwoo llorando y la frase «You're with me now.»
- Medido con `estilo.py` sobre el fotograma 0 (la caja de cambio de clase): paleta dominante en azul
  marino **#071331** (34 %), **#071949** (26 %), **#08256A** (13 %), acentos cian **#2A9EDA** (5 %) y
  **#81D9EC** (2,4 %); sombreado degradado, línea normal color **#0B275B**, saturación 87 %, brillo 38 %.
  Fondo casi negro-azul con marco y letras en cian, coherente con las otras dos cajas «NOTIFICATION».
- **Cómo cruza con lo que ya midió el investigador de texto** (`partes/texto.md`, imagen fija
  `Anime_System.png`, pantalla de ESTADO no de NOTIFICATION): violeta-magenta **#D259FF** para el marco
  tipo «circuito» de la ventana de ESTADO, y avisa que las ventanas «de novato» (Temporada 1 temprana) son
  **azules** (`#4C8CFD`), no violetas. Eso encaja exactamente con lo que vi en vídeo: **el color del marco
  no es fijo, depende del TIPO de ventana** — «NOTIFICATION» (aviso de evento, la que más sale) es
  siempre azul/cian en toda la serie (medido tres veces, min 1:11 tráiler / 2:33 ep. 11 / 0:00 y 1:18 ep.
  12); «STATUS» (ficha de personaje a demanda) es violeta neón; dentro de cualquier caja, el **verde**
  marca lo bueno (subida, recompensa) y el **rosa/carmesí** marca límite o coste. ✅✅ (dos investigadores,
  fuentes independientes, mismo patrón).

**Escena icónica 3 (apoyo, con reserva) — Beru y el Rey Hormiga (Episodio 24-25)**: no encontré el
episodio real re-subido entero en Dailymotion/Internet Archive dentro del tiempo de esta tanda (búsquedas
en Bitácora). Sí vi dos vídeos que tocan la escena y los diferencio con cuidado:
- «Sung Jinwoo vs The Ant King Beru | Cinematic Short» (`dailymotion.com/video/x9vvdrc`, 2:11) trae en su
  PRIMER fotograma su propio aviso: *"The following video is: Fan-made, not affiliated with Solo Leveling
  or Crunchyroll"* — es una animación 3D hecha por fans (parece usar asset del juego «Solo Leveling:
  ARISE», no el anime). Aun así reproduce la MISMA caja azul «NOTIFICATION» (min 0:00 y 2:01, «You have
  defeated the enemy. Leveled up!») y añade una tercera variante que no vi en el anime real: un panel
  «SKILLS» y un aviso de mejora de habilidad en **rosa-violeta con borde en pixel/glitch** (min 1:36,
  «[Skill: Fatal Strike] has been upgraded... [Skill: Mutilation]») — lo marco ⚠️ porque no pude confirmar
  si ese estilo glitch es del anime o sólo del juego que imita el fan.
- «Sung jin woo vs ant king (Beru) — Solo Leveling season 2» (`dailymotion.com/video/x9d28g8`, 3:08) es en
  realidad una **animación del manhwa** (viñetas con bocadillo, «ARISE.» dentro de un globo redondo
  azul, onomatopeyas coreanas superpuestas) mezclada con capturas de un juego 3D — NO es la interfaz de
  la serie de TV. La cito sólo como referencia del cómic, nunca para «cómo se ve la interfaz del anime».
- La escena real (Episodio 24, HØWL de fondo) queda confirmada por la wiki (galería de la canción, nombre
  «Sung Jinwoo vs The Ant King») pero **sin fotograma propio del anime real** — ⚠️, lo dejo en Sigue.

### Punto 2 · Fotogramas de escenas icónicas (resumen con capítulo y minuto)

| Escena | Episodio | Minuto | Fuente mirada entera | Qué muestra |
|---|---|---|---|---|
| Duelo con Igris | 11 | 0:06-2:43 | Dailymotion x8xqany | combate + caja de victoria |
| «Arise», cambio de clase | 12 | 0:00-1:42 | Dailymotion xb7cnoi | el Sistema completo, extracción de Igris |
| Tráiler: doble mazmorra/despertar | — (resumen) | 0:41-1:13 | Internet Archive (mirror oficial) | origen del Sistema, primera caja |
| Ant King / Beru | 24-25 | — | ⚠️ sólo fan-made / manhwa | ver reserva arriba |

### Punto 4 · Fondos y sitios (luz y paleta medida)

- **Sala del trono / mazmorra de Igris** (Doble Mazmorra, interior tipo templo gótico): columnas y
  candelabros dorados, luz cálida rojo-rosa. Medido con `estilo.py`: **#F46B7D / #C95460 / #973D48**
  dominantes, acento **#FB88A0**. Sombreado en degradado, poca línea. Fuente: fotograma propio, min 0:16
  del clip x8xqany. ✅ (visto en dos escenas del mismo set: min 0:06 y 1:53-1:59).
- **Portal/energía de sombra** (efectos de invocación sobre azotea nocturna, del opening): violeta-magenta
  vivo, medido sobre la hoja de storyboard del opening (fotograma M1, fila 2): **#C330E0** (el pixel más
  saturado de la zona del portal). Contrasta con el azul-cian de la interfaz del Sistema: el juego de
  colores de la serie separa «magia de sombra» (violeta/magenta) de «interfaz/datos» (azul/cian). ✅.
- **Skyline de Seúl de noche** (opening, min ~0:16-0:20 del vídeo de 100 s): edificios altos iluminados,
  puente peatonal con verja de cadena, parque con árboles — paleta medida sobre la hoja completa (M1):
  dominante casi negro **#0F0F19** (30 %), azul **#1A3251/#376590**, cian **#60BCD2**, magenta apagado
  **#572230**. Ciudad nocturna azul fría con acentos cálidos en la piel/ropa de personajes. ✅.
- **Ending «request» — espacios líminales** (habitación con TV de tubo, pasillo de casilleros de
  instituto, pasillo con puertas): paleta teal/cian desaturada muy oscura, con un giro a **rojo-naranja
  fuego** en el tramo final (cuenta atrás digital en pantalla, figura envuelta en llamas). Es un estilo
  totalmente distinto al de la serie: fotografía de imagen fija, grano, cámara "casera"/found-footage,
  muy alejado del 2D limpio del resto del anime — un vídeo musical conceptual, no una recreación de
  ninguna localización real de la trama. ✅ (mirado con storyboard, hojas 0 y 2 de 4).
- **Cueva/nido de insectos** (mazmorra de Jeju, escenario del Rey Hormiga): sólo visible en el clip
  fan-made (ver aviso arriba) — rocas grises, niebla, luces rojas (ojos/aguijón) y cian (poder de Jinwoo);
  ⚠️ no pude medir un hex de confianza porque el único material que encontré no es del anime oficial.

### Punto 14 · Poses analizadas (con capítulo y minuto)

**Sung Jinwoo** (dagas gemelas, arco «Job Change», ep. 11-12):
- **Guardia baja**, dagas invertidas, rodillas flexionadas — min 0:03 (x8xqany). Sirve para «alerta,
  a punto de pelear».
- **Bloqueo en cruz** sobre la cabeza, dientes apretados — min 0:37. Sirve para «resistir/aguantar».
- **Arrodillado, agotado**, puños ensangrentados apoyados en el suelo, cabeza baja — min 1:54-1:55.
  Sirve para «al límite, pensar» (encaja con el punto 14 del encargo, «pensar»).
- **Sentado contra una columna tras ganar**, brazos caídos, mirada al frente — min 2:39-2:42 («One
  screwup, and I'd probably be dead»). Sirve para «reflexionar/explicar en voz baja».
- **Puño cerrado con venas brillando en azul** (despertar), cámara muy cerca — min 1:00 del tráiler.
  Sirve para «decisión/determinación», es la pose que usa el propio tráiler como clímax de campaña.
- **Corriendo con la daga en alto**, capa/sudadera ondeando — min 0:23 del tráiler. Sirve para «avanzar,
  atacar».
- **De pie con los brazos en cruz sobre el pecho**, ligeramente agachado, viendo elevarse a Igris ya
  reconstruido — min 1:41 (xb7cnoi). Sirve para «presentar a alguien / dar una orden» (encaja con
  «presentar» del punto 14).

**Igris** (rasgo de personalidad confirmado por la wiki, no visto en vídeo propio esta tanda): se
arrodilla ante Jinwoo al terminar cada batalla, gesto recurrente de lealtad («running gag» que la propia
wiki describe, con Iron imitándolo). ⚠️ un solo tipo de fuente (texto de la wiki), lo dejo apuntado para
que quien escriba la biblia lo cruce con una imagen si aparece en las partes de imagen/voz.

## Lo mejor para la lámina

1. La caja **«NOTIFICATION»** (fondo azul casi negro, borde cian fino, icono de exclamación circulado,
   texto en mayúsculas) es el elemento MÁS reconocible y más repetido de toda la serie: confirmada en tres
   escenas distintas y por otro investigador desde una imagen fija — es el candidato obvio para «cuadro de
   diálogo propio de la serie» que pide el encargo, en vez de una burbuja blanca genérica.
2. El código de color por función (azul=aviso normal, verde=lo bueno, rosa/carmesí=límite o coste, violeta
   magenta=ficha de estado) da una paleta lista para cualquier panel de interfaz que se dibuje para el
   servidor (nº de mensajes, roles ganados, etc.), con el mismo lenguaje visual que usa la serie.
3. La animación de invocar una sombra (grietas cian en zigzag sobre silueta negra, capa/color propio del
   personaje asomando entre las grietas) es un efecto muy concreto y replicable: no es una nube de humo
   genérica, es «cristal que se rompe hacia dentro» con luz.
4. Pose de «sentado agotado contra la piedra tras ganar» (min 2:39 del duelo con Igris) es más honesta y
   menos genérica que un busto de pie; encaja con lo que pide `reglas_del_dueno.md` de personajes con pose
   y cara que casen con lo que dicen.
5. El opening (LEveL) separa visualmente violeta/magenta = sombras del protagonista, azul/cian =
   interfaz/datos del Sistema — dos familias de color que no se pisan y sirven para diferenciar zonas de
   una lámina (texto del canal vs. decoración).

## No encontré

- ⚠️ Vídeo del opening 2 «ReawakeR» y del ending 2 «UN-APEX» propios (sólo datos de wiki, sin
  storyboard ni fotograma propio) — YouTube bloqueaba justo en esos intentos; es extra sobre el mínimo (ya
  cubrí un opening y un ending completos), lo anoto para quien continúe.
- ⚠️ Fotograma real del anime (no fan-made, no manhwa) para la pelea con el Rey Hormiga / primera aparición
  de Beru (Episodio 24-25): busqué en Dailymotion e Internet Archive (bitácora abajo) y sólo aparecieron
  ediciones de fans o el manhwa animado. El archivo completo del episodio existe en Internet Archive
  (`solo-leveling-s-2-e-11-1920x-1080`, ~1,9 GB) pero descargarlo/recortarlo por streaming HTTP tardaba
  más de un minuto por fotograma (probado: 42 s un solo fotograma sobre un `.mkv` de 1,5 GB en otro ítem) —
  no encajaba en el presupuesto de esta tanda.
- Tráiler doblado al hindi de Crunchyroll India (Temporada 2): sólo confirmé que existe, no lo miré.
  Extra, no obligatorio (ya hay un tráiler mirado entero).
- No encontré un nombre propio para el sonido de la caja del Sistema (tintineo que sí se oye en los tres
  clips) — ⚠️ una sola fuente, mi propia escucha.

## Bitácora de búsqueda

- **AnimeThemes** (`api.animethemes.moe`): reintentado al empezar la tanda — la conexión TLS se cuelga
  hasta agotar el tiempo (mismo síntoma que el 522 avisado). Descartado, usé la wiki + storyboards.
- **Fandom `solo-leveling.fandom.com/api.php`** (inglés): `action=query&list=search` para `opening theme
  song`, `Shadow Army Arise`, `System window interface`, `Double Dungeon`, `Cartenon Temple`, `Demon
  Castle`; `action=parse&prop=wikitext` sobre `Solo Leveling (anime)`, `4eVR`, `UN-APEX`, `LEveL`,
  `ReawakeR`, `Request`, `DARK ARIA`, `DARK ARIA -ARISE-`, `SHADOWBORN`, `REVIVER`, `HØWL`,
  `Template:Music_Navigation`, `System`, `Shadow Authority`, `Shadow Extraction`, `Igris`, `Beru`,
  `Episode 2`, `Episode 12`, `Episode 21`.
- **api.dailymotion.com** (inglés/francés): búsquedas `Solo Leveling Arise Igris`, `Solo Leveling opening
  LEveL`, `Solo Leveling Ant King Jinwoo`, `Solo Leveling Beru`, `Solo Leveling System window`, `Solo
  Leveling Season 2 opening ReawakeR`, `Solo Leveling Episode 12 Arise scene`, `Solo Leveling mother elixir
  hospital`, `Solo Leveling Episode 24 Ant King anime`, `Solo Leveling Jinwoo cries mother` — de ahí salieron
  los clips reales x8xqany y xb7cnoi (los dos mirados enteros) y los descartados por ser fan-made/manhwa.
- **archive.org** `advancedsearch.php`: `solo leveling opening`, `"solo leveling"` — encontré el mirror del
  tráiler oficial (`youtube-n24l9gvM3XM`), el ítem con episodios de la Temporada 1 doblados en latino
  (`solo-leveling-09-1080p-lat-cast-jap-subs`, no usado por peso/velocidad), el ítem con episodios de la
  Temporada 2 (`solo-leveling-s-2-e-11-1920x-1080`) y el audio oficial de OP/ED (`krage-request-solo-
  leveling-ed`, mp3 sin vídeo).
- **YouTube vía yt-dlp**: `-F`/`-j` (listar formatos e info) funcionó siempre; la descarga del vídeo dio
  403 o «Sign in to confirm you're not a bot» de forma intermitente (a veces sí, a veces no, con la misma
  IP compartida) — cuando fallaba, usé el **storyboard** (`yt-dlp -f sb0`, formato `mhtml`; la extracción
  con el módulo `email` de Python corrompía el JPEG, así que bajé cada hoja directo por su URL
  `i.ytimg.com/sb/<id>/…`, sin login, sin descargar el vídeo). Storyboards conseguidos: `XqD0oCHLIF8`
  (LEveL, 4 hojas), `CRZsOOOvg1I` (request, 4 hojas), `ZGXOWPZ64DA`/`qUFRPDHs1Q8`/`1LJnOQOBGp4` (MV en
  directo de DARK ARIA/SHADOWBORN/REVIVER, 3 hojas cada uno). Fallaron por login: `GThtBqztnJc` (HØWL) y
  `HkIKAnwLZCw` (tráiler AniList) — sustituido este último por el mirror de Internet Archive.
- **WebSearch** (1 búsqueda usada de ~50): `Solo Leveling "Arise" scene TikTok viral trend edit 2024` →
  confirma la tendencia (tiktok.com/discover, varias cuentas).
- **Herramientas**: `fotogramas.py --cortes` sobre 4 vídeos completos (Igris 91 planos, Arise-ep12 43
  planos, Ant King fan-made 77 planos, tráiler 87 planos); `estilo.py` sobre 3 fotogramas propios para
  paleta y tipo de sombreado; medición manual con Pillow (`getcolors`, escaneo de píxel más saturado) para
  los hex de la interfaz y el portal violeta.
- Cruce de datos con `partes/texto.md` (mismo equipo, punto 5/6/11): sus colores medidos sobre
  `Anime_System.png` (imagen fija) y los míos (vídeo en movimiento) coinciden en la lógica de colores por
  tipo de ventana — going citado arriba.

Sigue: fotograma real del anime (episodio 24-25, Rey Hormiga/Beru) si aparece un mirror completo más
ligero; storyboard de ReawakeR/UN-APEX si YouTube deja de bloquear.
