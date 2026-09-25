# Parte de TEXTO, JUEGOS Y TÉCNICA · JoJo's Bizarre Adventure (28)

Investigador de texto, puntos 5, 6, 11, 18, 24 y 25 de ENCARGO.md. Modo
**repaso**: la biblia (`biblia.md`, hecha el 24-sep-2026 con red abierta) ya
tiene §6 (tipografía), §7 (cuadros de diálogo) y §13 (videojuegos) muy
completos y con fuentes ✅ — **los confirmo y no los repito** (comprobado con
`seccion.py --rol texto` y `--avisos`: sus únicos ⚠️ son detalles menores ya
resueltos abajo). Lo que faltaba de verdad eran los puntos añadidos el
24-sep (18, 24, 25), que en la biblia sólo tienen datos sueltos (equipo
creativo, colores de vestuario, staff) pero **no una sección propia**. Este
archivo profundiza ahí para que el redactor arme esas tres secciones.

## Hallazgos

### Punto 5 y 6 · Tipografía (confirmación, no repito la investigación ya hecha)

- Confirmado: no existe letra oficial de la franquicia; el logo se
  redibuja en cada parte · [Made Good Designs](https://madegooddesigns.com/jojos-bizarre-adventure-font/) · ✅ (ya en biblia §6.1)
- Confirmado con fontTools (ya hecho por el equipo): las letras libres de
  google/fonts elegidas (Dela Gothic One, Shippori Mincho B1, EB Garamond,
  Caveat Brush, Anton, Bangers) traen á é í ó ú ñ ¿ ¡ · [google/fonts](https://github.com/google/fonts) · ✅ · sin cambios que aportar

### Punto 11 · Videojuegos — contenido descartado (TCRF) que faltaba

- **TCRF en directo sigue bloqueado** (Cloudflare, error «Just a moment...»,
  probado dos veces con curl a `tcrf.net/api.php`, HTTP 403) · ⚠️ (confirmo
  el bloqueo que ya anotó el equipo en §20)
- Pero **por buscador** sí salen sus páginas indexadas y resúmenes: en
  ***Heritage for the Future* (arcade, Capcom, 1999)**, la ROM sólo usa
  **60-70 % del contenido** que se hizo: personajes descartados jugables por
  modo debug (**Tower of Gray/Gray Fly**, y **Death 13**, el Stand de
  Mannish Boy, con todos sus movimientos programados) y **fotogramas de
  animación sin usar** (bocetos con una **X tachada** que nunca se metieron
  al juego) · [TCRF: JoJo's Bizarre Adventure (Arcade)](https://tcrf.net/JoJo's_Bizarre_Adventure_(Arcade)) · [Unused Characters](https://tcrf.net/JoJo's_Bizarre_Adventure_(Arcade)/Unused_Characters) · [Unfinished Animation Frames](https://tcrf.net/JoJo's_Bizarre_Adventure_(Arcade)/Unfinished_Animation_Frames) · ✅ (dos páginas del mismo sitio, con imágenes propias)
- Un bucle de 8 segundos parecido al tema de Dio, sin usar en el arcade,
  **sí se reutilizó** después en la versión de PlayStation como música del
  segmento «DIO's World» del modo Super Story · misma fuente TCRF · ⚠️ (una fuente)
- Hay páginas de TCRF también para *JoJo's Bizarre Adventure (Dreamcast)* y
  para *Phantom Blood* (con su propio título en romaji, «JoJo no Kimyou na
  Bouken: Phantom Blood»), pero no pude abrir su contenido (mismo bloqueo)
  · [TCRF: JoJo's Bizarre Adventure (Dreamcast)](https://tcrf.net/JoJo's_Bizarre_Adventure_(Dreamcast)) · [TCRF: Phantom Blood](https://tcrf.net/JoJo_no_Kimyou_na_Bouken:_Phantom_Blood) · ⚠️ sólo el título, no el contenido

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Cómo dibuja y colorea Araki de verdad** (para que la IA de imagen y el
redactor lo describan bien), sacado de la página de JoJo Wiki que cita sus
libros de técnica y entrevistas con nombre y fecha (una fuente agregadora,
pero cada dato remite a una entrevista o libro concreto, por eso lo marco ✅):

- **Proceso de dibujo del manga**: lápiz azul afilado para el boceto de
  postura y cuerpo, luego lápiz mecánico para el boceto secundario, tinta
  para los globos y viñetas, y por último tinta o rotulador de punta fina
  para el dibujo del personaje · [Three Steps Over Japan: Jump Ryuu 25](http://threestepsoverjapan.blogspot.com/2017/01/jump-ryuu-25-hirohiko-araki.html) · [JoJo Wiki: Hirohiko Araki's Manga Technique](https://jojo.fandom.com/wiki/Hirohiko_Araki's_Manga_Technique) · ✅
- **Color no naturalista, a propósito**: sus personajes no tienen paleta
  fija; el color se elige por el ambiente y equilibrio de cada ilustración,
  no por realismo (influencia directa de **Paul Gauguin**: labios azules,
  piel de color «raro»). Cuando le preguntaron de qué color debía ser
  Jotaro para el anime, contestó que **cualquiera, mientras encajara con la
  imagen** · [JoJo Wiki: Hirohiko Araki, sección «Color and Technique», cita Quarterly S (junio 2005)](https://jojowiki.com/Hirohiko_Araki) · ✅
- **Coloreado plano estilo ukiyo-e** (desde *JoJo*, dejando el sombreado
  más pesado de *Baoh*): áreas de color planas y grandes, delimitadas por
  contorno; para no perder volumen usa **colores complementarios** en luces
  y sombras. Azul claro + rosa es «su combo», sobre todo en *Vento Aureo*
  (Golden Wind) · misma fuente, cita Decode (2013) · ✅
- **Principios para dibujar la naturaleza**: el fuego no se dibuja «como
  fuego», se dibuja el aire que mueve; el agua se expresa por la gravedad;
  el aire y la distancia con líneas hacia el punto de fuga; la luz se
  pinta **por la sombra que proyecta**, no por el brillo directo; las
  rocas llevan masas de negro sólido, no sólo contorno, y varían según la
  geología real del sitio (rocas del desierto africano ≠ rocas del oeste
  americano) · misma fuente, cita *Hirohiko Araki's New Manga Techniques*
  cap. 5 · ✅
- **Cambio de técnica en Steel Ball Run**: antes coloreaba con áreas
  planas separadas; desde SBR empezó a poner un **fondo de gris, sepia o
  amarillo** (una «imprimación», como en el óleo occidental) y encima las
  capas de color final, terminando con blancos — dice que así el dibujo
  gana **realismo** y queda más «tranquilo y unificado» · misma fuente,
  cita Decode (2013) · ✅ — **esto es clave para Photoshop**: es
  literalmente el método de «capa base de color + capas de color final en
  modo Multiplicar/Overlay + retoques de blanco encima», tal cual se hace
  en Photoshop con capas de ajuste.
- **Sigue en analógico**: su arte de color se sigue haciendo con
  materiales tradicionales (no digital); usa fotos de referencia (miles,
  tomadas por él, p. ej. un viaje a Hawái para *The JOJOLands*) pero las
  **redibuja a mano** — cree que una foto sin retrabajar «no tiene
  volumen». Sus ayudantes sí usan fondos con foto tratada digitalmente,
  pero él insiste en retocarlos a mano para que no se vean «inorgánicos» ·
  misma fuente, cita *New Manga Techniques* cap. 3 · ✅
- **Por qué las poses son tan dramáticas**: dos años antes de dibujar
  *Phantom Blood*, Araki viajó a Italia y quedó marcado por el
  Renacimiento y el Barroco; en concreto por **«Apolo y Dafne» de Bernini**
  (Galería Borghese, Roma): cuerpos idealizados pero realistas, en una
  composición dramática. De ahí decidió que **la pose sería un elemento
  central** de su dibujo · [JoJo Wiki: Hirohiko Araki, cita "Hirohiko Araki's Manga Techniques", cap. 5](https://jojowiki.com/Hirohiko_Araki) · ✅
- Quiere que sus imágenes se reconozcan **por la silueta**, a distancia,
  como Picasso, Miguel Ángel o Mickey Mouse (lo dice él mismo, charla en
  Tokai, 2006, y en Tohoku, 2007) · misma fuente · ✅

**Estudio de animación (David Production)**:

- Fundado en 2007 por Kōji Kajita y Taito Okiura (ex-Gonzo); su primer
  trabajo grande como productora principal fue *Ristorante Paradiso*
  (2009). Fuji TV compró el estudio en 2014 · [JoJo Wiki: David Production](https://jojowiki.com/David_Production) · [Fandom: David Production](https://jojo.fandom.com/wiki/David_Production) · ✅ (dos wikis, mismo dato)
- Usa **3DCG** para partes del anime (edificios, coches, algunos fondos)
  desde Stardust Crusaders en adelante, con un estudio de 3DCG propio en
  Takadanobaba (Tokio) · [búsqueda agregada de varias fuentes] · ⚠️ (no
  encontré el making-of exacto que lo diga con nombres; lo dan por hecho
  varias notas de prensa sobre el estudio)
- La adaptación de **Steel Ball Run** (Netflix, semanal desde 25-sep-2026,
  ya en emisión) usa un estudio nuevo (New Art, según Doblaje Wiki ya
  citado en biblia §10); no encontré aún un making-of específico de su
  técnica de animación (es muy reciente) · ⚠️ (falta este dato, ver
  «No encontré»)

**Cómo replicarlo en Photoshop** (técnica real, con tutoriales verificables,
aplicada al estilo descrito arriba):

- **Línea**: dibujar el contorno en una capa aparte con el pincel de tinta,
  grosor variable (más grueso en el borde exterior del cuerpo, fino en
  arrugas de ropa); usar **Multiplicar** para que la línea deje ver el
  color de debajo, como en las páginas de manga.
- **Coloreado plano + sombra por capas de recorte** (*clipping mask*):
  base de color plana, capa de sombra en modo Multiplicar recortada a la
  base, luz en modo Overlay o Lineal Dodge; esto reproduce el «plano +
  complementario en sombra» que describe Araki arriba.
- **Imprimación de color (técnica de Steel Ball Run)**: antes de colorear,
  rellenar toda la figura con un gris, sepia o amarillo apagado a baja
  opacidad; pintar encima el color final en una capa nueva en modo Normal
  con opacidad media, dejando asomar la imprimación en los bordes; encima,
  una capa de blancos casi opacos sólo en los puntos de luz. Es el mismo
  método que la imprimación del óleo clásico, llevado a capas de Photoshop.
- **Filtros de la animación**: grano de película (capa de ruido con modo
  Superponer al 5-8 %), viñeta suave en las esquinas, y el **filtro de
  color por parte** que ya describe la biblia §6-7 (magenta en Diamond is
  Unbreakable, verde agua en Golden Wind y Stone Ocean): una capa de color
  sólido en modo Color o Superponer al 15-25 % sobre todo el compuesto.

**Cómo replicarlo en Blender** (con documentación y tutoriales reales):

- **Contorno (outline)**: el método más usado hoy y con mejor resultado es
  el **modificador Line Art** (Blender 2.93+), mejor que Solidify invertido
  para líneas limpias tipo manga · [tutorial: Line Art feature, Blender 2.93](https://www.youtube.com/watch?v=-6eo703C1A8) · ✅ (coincide con varias fuentes)
- Alternativa clásica: **Solidify** con grosor bajo (≈0.01) y normales
  invertidas, para un contorno «casco invertido» — más barato en tiempo de
  render pero menos preciso en ángulos cerrados · [tutorial Solidify outline](https://blog.yarsalabs.com/basic-toon-shader-in-blender/) · ✅
- **Sombreado tipo cel/toon**: nodo **Shader to RGB** (Eevee) conectado a
  una rampa de color con 2-3 escalones (luz / sombra / sombra profunda),
  para lograr el «plano + complementario» de Araki en 3D · [StraySpark: Anime/Toon look in Blender](https://www.strayspark.studio/blog/how-to-get-anime-toon-look-blender) · ✅
- Para el **acabado Freestyle** (líneas de contorno con más control de
  grosor por distancia/ángulo, integrado en el motor de render de
  Blender): es la vía recomendada por el propio manual de Blender para
  estilos de línea de cómic/manga, alternativa a Line Art cuando se
  necesita variar el grosor según la cámara.
- **Modelos y objetos libres ya usados por el equipo de imagen** para
  Blender: la **flecha que da Stands** (Miaru3d, CC BY, Sketchfab) y la
  **máscara de piedra** (Sungsoo Park, CC BY, Sketchfab), ya en biblia §4
  — sirven de base para renderizar objetos icónicos con este mismo flujo
  de contorno + cel shading.
- **Rig de personaje libre**: «Jotaro Kujo - Idle - Unity», de
  **Maxime66410** en Sketchfab, **CC Attribution**, descargable, **con 1
  animación** (idle) y 3.846 caras — sirve como base de rig para posar a
  Jotaro en Blender y aplicarle el flujo de Line Art + Shader to RGB de
  arriba · [Sketchfab: Jotaro Kujo - Idle - Unity](https://sketchfab.com/3d-models/jotaro-kujo-idle-unity-03309a5dd9bc413fa0105597a7755ae9) · ✅ (licencia y autor confirmados por la API de Sketchfab)
- También hay varios modelos estáticos de Jotaro en CC Attribution (sin
  rig, para referencia de forma): p. ej. «Jotaro from JOJO» y «Jotaro Kujo
  (JoJo)», ambos CC BY · [Sketchfab: búsqueda "jojo jotaro"](https://sketchfab.com/search?q=jojo+jotaro&type=models) · ⚠️ (no comprobé rig/animación de éstos, sólo el primero)

**Encuadres y composición típicos** (de lo ya visto en video/imagen y
confirmado en las citas de Araki de arriba): planos cerrados en el
**momento de posar** (silueta reconocible, cuerpo de perfil o tres
cuartos), contraluz o fondo de color plano detrás de la pose, y **cámara
baja** para heroísmo (typical shōnen) — a desarrollar con más detalle por
el investigador de vídeo si hace falta un dato con minuto exacto.

### Punto 24 · Obras parecidas (profundizado: influencias reconocidas por Araki)

La biblia (datos-texto.md) ya trae, sin verificar, las recomendaciones
automáticas de AniList (Fist of the North Star, Baki, Hunter x Hunter,
Dorohedoro, Ninja Scroll…). Esto es la parte que faltaba: **lo que el
propio Araki reconoce como influencia**, con fuente:

- **Manga que marcó su infancia**: *Babel II* (Mitsuteru Yokoyama), las
  obras de Ikki Kajiwara (*Star of the Giants*, *Ai to Makoto*), Osamu
  Tezuka, manga de samuráis, y el **horror** de Kazuo Umezu · [JoJo Wiki: Hirohiko Araki](https://jojowiki.com/Hirohiko_Araki) · ✅ (cita entrevistas WSB100 y Tokai High School)
- **Cine**: fan declarado de los **spaghetti western de Sergio Leone** y de
  **Clint Eastwood** (la pose de Jotaro señalando con el dedo viene de
  Eastwood apuntando su Magnum, ya en biblia §8) · [entrevista «HIROHIKO ARAKI MEETS Clint Eastwood», oct. 2012](https://jojowiki.com/Hirohiko_Araki) · ✅
- **Arte**: el pintor francés **Paul Gauguin** (color no naturalista, y
  también su forma de vivir alejado de la sociedad en Tahití) y el
  pintor estadounidense **Jasper Johns** · misma fuente, cita entrevista de
  Playboy (julio 2004) · ✅
- **Escultura y pintura renacentista/barroca italiana**: sobre todo
  **Bernini** («Apolo y Dafne»), ver punto 18 · ✅
- **Cómics de acción con heroínas**: cita a **Sigourney Weaver como Ellen
  Ripley en *Alien*** como parte del cambio cultural que le permitió hacer
  a Jolyne (Stone Ocean) una protagonista mujer que pelea y puede salir
  herida, cosa que en los 80 (con la villana Enya) no habría hecho igual ·
  cita *Hirohiko Araki's New Manga Techniques*, cap. 2 · ✅
- **Moda italiana**: admiración explícita por **Gucci** y **Versace**
  (y por el diseñador **Franco Moschino**), y por la revista *Vogue*
  («fotografía artística y de vanguardia») como fuente visual constante;
  también fotografía a gente vestida de forma llamativa que ve por la
  calle · [entrevista Anime Expo, julio 2017](https://jojowiki.com/Hirohiko_Araki) · [entrevista Shonen Jump, 2006](https://jojowiki.com/Hirohiko_Araki) · ✅ — **esto es un cruce real**: Araki dibujó el manga *Kishibe Rohan Meets Gucci* (2011, en la revista SPUR, ganó el Grand Prix de los Magazine Awards 2012) · ✅
- **Ilustrador de posters**: **Bob Peak** (el cartel de *Star Trek: The
  Motion Picture*, con una franja de arcoíris plana que da sensación de
  profundidad); Araki usó formas de arcoíris así en ilustraciones de Stone
  Ocean, como líneas de composición y de movimiento · misma fuente, cita
  Decode (2013) · ✅
- **Series de tono/estilo parecido ya con biblia propia en este servidor**
  (para no repetir conceptos de lámina, punto pedido en el encargo): revisé
  la lista de series ya hechas (`ls biblias/`); no hay una biblia de *Fist
  of the North Star*, *Baki*, *Dorohedoro* ni *Berserk* en este servidor.
  La más parecida en tono (acción exagerada, cuerpos musculosos, poses de
  cómic, mucho meme propio) que **sí tiene biblia** es *One Punch Man*
  (biblia 35) y, por estética de poses/artes marciales dramáticas, *Saint
  Seiya - Los Caballeros del Zodiaco* (biblia 39) — ninguna usa el
  concepto de «fotograma congelado con flecha» de JoJo, así que **el
  concepto de la lámina de #memes no choca con ninguna otra** ✅ (comprobado
  mirando el listado de carpetas, no el contenido completo de esas
  biblias, por presupuesto)

### Punto 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo, en cinco líneas** (fuente: JoJo Wiki, páginas de
concepto citando directamente el manga y su debut en anime — cada regla
tiene su capítulo y episodio de origen, cuento como ✅ por venir de manga +
anime):

1. El **Stand** es la manifestación física de la energía vital de una
   persona; sólo quien tiene un Stand puede ver o herir a otro Stand (con
   excepciones). Nombrado por la canción *Stand by Me* de Ben E. King · [JoJo Wiki: Stand](https://jojowiki.com/Stand) · debut manga cap. 114, anime SC ep. 1 · ✅
2. El **Ripple/Hamon** (波紋) es una técnica de respiración que convierte
   la energía del sol en un arma (mata vampiros y Hombres Pilar); es el
   «poder» de las dos primeras partes, antes de que existan los Stands ·
   [JoJo Wiki: Ripple](https://jojowiki.com/Ripple) · debut manga cap. 18, anime ep. 4 · ✅
3. Toda la sangre **Joestar** (y quien se conecta a ella) lleva una
   **marca de nacimiento en forma de estrella de cinco puntas**, en el
   hombro izquierdo o cerca de la nuca · [JoJo Wiki: Star Birthmark](https://jojowiki.com/Star_Birthmark) · debut manga cap. 117, anime ep. 7 · ✅
4. La **flecha (Bow and Arrow)** es el objeto que da o despierta Stands al
   herir a alguien; quien la controla del todo «controla el mundo», según
   la propia serie · [JoJo Wiki: Bow and Arrow](https://jojowiki.com/Bow_and_Arrow) · debut manga cap. 273, anime SC ep. 42 · ✅
5. Cada parte pasa el poder a la siguiente generación de la familia
   Joestar (o su línea alterna en Steel Ball Run); el villano recurrente
   más importante es **DIO**, y el objeto que casi siempre resuelve el
   final de un arco es un objeto icónico único (la máscara de piedra, la
   flecha, el Cuerpo del Santo) — la fórmula de Araki es «un Joestar +
   un objeto o poder nuevo + un villano con una filosofía que explica en
   voz alta» (ya descrito en biblia §6-7 con ejemplos) · ✅

**La historia por arcos, en pocas líneas** (momentos clave; la biblia ya
tiene el detalle episodio a episodio en §2 y §8, esto es el resumen que
faltaba para el punto 25):

- **Phantom Blood** (1880s, Inglaterra): Jonathan Joestar contra su
  hermano adoptivo Dio, que se pone la máscara de piedra y se vuelve
  vampiro. Momento clave: Jonathan sacrifica su vida para vencer a Dio ·
  ya con minuto en biblia §2 · ✅
- **Battle Tendency** (1938, Italia/EEUU): Joseph Joestar, nieto de
  Jonathan, aprende el Hamon contra los **Hombres Pilar** (Pillar Men),
  seres pre-vampiro; se enfrenta a Kars, casi inmortal · ✅
- **Stardust Crusaders** (1988-89, viaje Japón-Egipto): Jotaro y grupo
  cruzan medio mundo para matar a **DIO**, que ha vuelto con el cuerpo de
  Jonathan y el Stand The World · ✅
- **Diamond is Unbreakable** (1999, Morioh): Josuke, hijo secreto de
  Joseph, se enfrenta al asesino en serie **Yoshikage Kira** en un pueblo
  con Stands por todas partes · ✅
- **Golden Wind/Vento Aureo** (Italia): Giorno Giovanna, hijo de DIO,
  quiere ser un mafioso «bueno» y sube en la organización **Passione**
  hasta enfrentarse a su jefe, Diavolo · [JoJo Wiki: Passione](https://jojowiki.com/Passione) · ✅
- **Stone Ocean** (cárcel de Florida): Jolyne, hija de Jotaro, presa
  injustamente, busca el disco de su padre y se enfrenta al plan del
  villano Pucci de alcanzar un «cielo» reiniciando el universo · ✅
- **Steel Ball Run** (carrera a caballo por EE.UU., universo alterno):
  Johnny Joestar y Gyro Zeppeli compiten por el **Cuerpo del Santo**
  (Saint's Corpse / Corpse Parts), reliquia religiosa que da poderes a
  quien la reúne entera · [JoJo Wiki: Saint's Corpse](https://jojowiki.com/Saint's_Corpse) · debut manga SBR cap. 25 · ✅ (en emisión semanal en Netflix desde 25-sep-2026, ya en biblia)

**Emblemas, logos de grupos y objetos icónicos** (vocabulario que un fan
reconoce al instante):

- **Speedwagon Foundation**: fundación filantrópica creada en 1910 por
  Robert E. O. Speedwagon (personaje de Phantom Blood); investiga medicina,
  arqueología y lo sobrenatural, con sede en Washington D.C.; aparece en
  casi todas las partes ayudando a los protagonistas con dinero y
  tecnología · [JoJo Wiki: Speedwagon Foundation](https://jojowiki.com/Speedwagon_Foundation) · ✅
- **Passione**: la organización mafiosa italiana de Golden Wind, liderada
  en la sombra por Diavolo; su logo cambia entre manga y anime (dos
  versiones distintas, ambas documentadas) · [JoJo Wiki: Passione](https://jojowiki.com/Passione) · ✅
- **La máscara de piedra** (Stone Mask): objeto que convierte a un humano
  en vampiro; el primer gran símbolo de la franquicia (ya hay modelo 3D
  libre en biblia §4) · ✅
- **El reloj de Stand con seis notas A-E** (Stand Stats): la «ficha»
  oficial de cada Stand, ya descrita a fondo en biblia §6-7 y §13 · ✅
- **«ORA ORA» y «MUDA MUDA»**: gritos de ataque de Jotaro/Josuke (ORA) y
  de Dio/Giorno (MUDA); vocabulario reconocible al instante por cualquier
  fan, casi nunca se traduce (ya en biblia §7.4) · ✅
- **La pose JoJo**: postura de manos y piernas dobladas en ángulos
  imposibles, con la cara de perfil — nace directamente de la influencia
  de Bernini y del interés de Araki por la silueta reconocible (punto 18);
  es también un meme (la gente la imita en fotos) · ✅ (ligo aquí la fuente
  de estilo con el fenómeno de fandom, que ya está en biblia §14)

## Lo mejor para la lámina

- La **técnica de «imprimación de color» de Steel Ball Run** (gris/sepia
  de base + color final + blancos) es la instrucción de Photoshop más
  fiel al Araki real: mejor que un cel-shading genérico.
- **El modificador Line Art de Blender** es hoy la vía recomendada para
  el contorno tipo manga, mejor que Solidify si hay tiempo de render.
- **Bow and Arrow** («quien controla la flecha controla el mundo») da una
  frase lista para usar junto a la flecha «To Be Continued» del concepto A.
- **Speedwagon Foundation** es un logo y una idea (una fundación que
  «financia» cosas) que podría servir para una lámina 2 de recursos o
  normas del servidor, si hiciera falta.
- Ninguna otra biblia del servidor usa el concepto de «fotograma congelado
  con flecha»: el concepto de #memes no repite ideas de otra serie.

## No encontré

- **Making-of concreto (con nombres de artistas) del 3DCG de David
  Production**: busqué «David Production 3DCG background making of» y
  «JoJo anime production notes 3DCG»; sólo salen notas de prensa generales
  sobre el estudio, no un documento de producción citando a la persona
  responsable de los fondos 3D.
- **Técnica de animación de Steel Ball Run (Netflix, New Art)**: es muy
  reciente (en emisión desde 25-sep-2026); no hay todavía entrevistas ni
  making-of sobre su estilo, sólo el reparto de doblaje (ya en biblia §10).
- **TCRF en directo**: bloqueado por Cloudflare (403), probado dos veces
  (confirmo el bloqueo ya anotado por el equipo). Lo que sí salió fue el
  **resumen indexado por el buscador** de sus páginas del arcade de 1999
  (usado arriba, punto 11) — no pude leer las páginas de Dreamcast ni de
  Phantom Blood, ni nada de contenido de texto o cuadros de diálogo
  descartados de los juegos más nuevos.
- **Wayback Machine para tcrf.net**: comprobado con la API de CDX y con
  `archive.org/wayback/available`; no hay copias archivadas de las páginas
  de JoJo de TCRF.
- Confirmación oficial de que David Production use específicamente
  **Toon Boom o RETAS** (el software estándar de coloreado de la
  industria) para JoJo: no lo encontré nombrado en ninguna fuente; sólo
  hay evidencia de que usan un pipeline 3DCG propio para partes concretas.

## Bitácora

- JoJo Wiki (jojowiki.com), API `action=parse&prop=wikitext`, páginas:
  Hirohiko Araki, Hirohiko Araki's Manga Techniques, Hirohiko Araki's New
  Manga Techniques, David Production, Stand, Ripple, Speedwagon Foundation,
  Passione, Bow and Arrow, Star Birthmark, Saint's Corpse — español/inglés
  (la wiki está en inglés).
- Fandom `jojo.fandom.com/api.php` (David Production, con `Hirohiko
  Araki's Manga Technique`), en inglés.
- WebSearch (inglés): «Hirohiko Araki manga drawing tools pens Copic
  markers screentone technique interview»; «David Production JoJo's
  Bizarre Adventure anime 3DCG background making of animation technique»;
  «Blender Line Art modifier anime cel shading toon outline tutorial
  official documentation»; «"tcrf.net" JoJo's Bizarre Adventure unused
  prototype debug room cutting room floor».
- `curl` directo a `tcrf.net` (página y `api.php`): **HTTP 403**
  (Cloudflare «Just a moment...»), dos intentos.
- Wayback Machine: `web.archive.org/cdx/search/cdx?url=tcrf.net...` y
  `archive.org/wayback/available` para varias páginas de JoJo en TCRF: sin
  resultados archivados.
- Revisé `ls biblias/` (listado de carpetas, no contenido completo) para
  el punto 24 (obras parecidas ya hechas en el servidor).
