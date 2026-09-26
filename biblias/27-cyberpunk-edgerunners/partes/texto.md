# Parte de TEXTO, JUEGOS Y TÉCNICA · Cyberpunk: Edgerunners (repaso)

Puntos 5, 6, 11, 18, 24 y 25 de `ENCARGO.md`. La biblia ya tiene secciones
para 5 (§6 Tipografía, l.575-611), 6 (§7 Cuadro de diálogo, l.612-713) y 11
(§13 Videojuegos, l.1061-1135), bastante completas: aquí confirmo lo dudoso
y sumo lo nuevo. Los puntos **18, 24 y 25 no tenían sección**: van enteros,
para que el redactor los añada.

## 5 · Tipografía (confirma §6 de la biblia)

- **M PLUS Rounded 1c confirmada con fontTools**: sí trae á é í ó ú ñ Ñ ¿ ¡ ü
  (probé `MPLUSRounded1c-Regular.ttf` de
  [google/fonts](https://raw.githubusercontent.com/google/fonts/main/ofl/mplusrounded1c/MPLUSRounded1c-Regular.ttf))
  · ✅ (antes ⚠️ «no comprobada» en la biblia: **pásalo a ✅**). Es la letra
  libre para el katakana redondo de los rótulos de nombre.
- El resto de §6 (Rajdhani, Orbitron, Anton, Bebas Neue, VT323, Chakra Petch,
  Oxanium, Share Tech Mono) ya estaba comprobado por el investigador
  anterior con fontTools: no lo repito, lo doy por bueno.
- **Logo «CYBERPUNK»**: sigue sin equivalente libre real. Busqué en dafont
  y Fontsource variantes "glitch"/"cyberpunk" (en) y ninguna reproduce el
  trazo roto a mano; mejor usar el logo como imagen, tal y como dice la
  biblia · ⚠️ (confirmado que no hay letra libre, no que "no existe": busqué
  a fondo).

## 6 · Cómo hablan y piensan en pantalla (confirma §7)

- **Subtítulo del juego sin caja**: lo vi en una captura real de
  *Cyberpunk 2077* (no de Edgerunners, es diálogo de personaje NPC en el
  Afterlife) — texto centrado abajo, **sin caja**, en un tono azul/cian
  claro con contorno oscuro para legibilidad ✅ (captura de
  [Interface In Game](https://interfaceingame.com/wp-content/uploads/cyberpunk-2077/cyberpunk-2077-dialogue.png),
  1920×1080). No mostraba el nombre en coral delante porque es un
  subtítulo de cinemática, no una línea de diálogo con opciones; **confirma
  el estilo "sin burbuja"** que ya tenía la biblia, no contradice el color
  coral+cian de §7.2 (ese lo midieron en la guía de cuadros).
- **Opciones de diálogo en lista vertical**: sigue como ⚠️ de memoria. Probé
  Game UI Database (bloqueada por Cloudflare, reto que no salté, dos
  intentos: `curl` y `WebFetch`) y busqué capturas alternativas; sólo
  confirmé por texto (Game8, gamepressure) que se navegan con arriba/abajo
  del d-pad y se resaltan en amarillo/azul según el tipo de elección ✅
  ([Game8](https://game8.co/games/Cyberpunk-2077/archives/Dialogue-Options)),
  pero no encontré una captura clara de la lista completa: **queda ⚠️**.
- Todo lo demás de §7 (holo-llamada, HUD del ojo, cinta de datos del
  netrunner, radio, rótulos de nombre, ausencia de monólogos, manga
  MADNESS) ya lo dejó bien el investigador anterior con fuente y ✅: no
  repetido.

## 11 · Videojuegos de la franquicia (confirma §13)

- **The Cutting Room Floor sí tiene página de *Cyberpunk 2077***
  (`tcrf.net/Cyberpunk_2077`): existe y documenta un modo en tercera
  persona descartado, el cambio de nombre del mapa (`01_nightcity` →
  `03_night_city`) y diferencias regionales por censura ✅ (confirmado por
  los resultados de búsqueda de Google, con extractos de la página). **No
  pude abrirla directo**: Cloudflare la bloquea (403 con `curl` y con
  `WebFetch`, dos intentos cada uno) y tampoco hay copia en Wayback
  Machine. No documenta nada de las recreativas ni del contenido de
  Edgerunners en concreto (es del juego base, previo al parche 1.6) · ⚠️
  contenido visto sólo por snippet de búsqueda, no por la página.
- El resto de §13 (parche 1.6 «Edgerunners Update», *Roach Race*, *Trauma
  Drama*, *Arasaka Tower 3D*, la interfaz del juego, *Edgerunners 2*) ya
  estaba muy completo y con fuentes: no repetido.

## 18 · Estilo de dibujo y técnica, y cómo replicarlo (sección nueva)

### 18.1 Cómo lo hizo Studio Trigger (de entrevistas, no de memoria)

- **2D moderno con memoria de anime retro**: el estudio mezcló animación
  2D "crujiente" (nítida, de trazo grueso) con guiños visuales a los años
  70-90 ✅ ([Animation World Network](https://www.awn.com/animationworld/cyberpunk-edgerunners-vibrant-ode-retro-anime)).
- **El "bullet-time" del Sandevistan es una técnica de animación real, no
  sólo un efecto de cámara**: el equipo *"spread out all the frames that
  would have gone into that particular animation, [broke] it down, and
  fill[ed] in the gaps"* con variaciones de color en cada fotograma
  (efecto psicodélico de multiplicado/afterimage) ✅. Yoshinari (diseñador
  de personajes) dijo que es *"a style that actually existed in Japanese
  anime from older days... we dusted it off and brought it back to modern
  animation"* ✅ (misma fuente, AWN, citando la entrevista de Netflix con
  Otsuka, Imaishi y Yoshinari).
- **Las escenas de "buceo" en la red** (netrunners hackeando) se hicieron
  con referencias **analógicas antiguas**, no replicando el pixel del
  videojuego: *"we drew reference from old-school analogs. It looks very
  different from the original game"* (Imaishi) ✅ (misma fuente AWN).
- **Influencias que el propio equipo nombra**: *Akira*, *Ghost in the
  Shell* y *Blade Runner*, combinadas con animación 2D moderna ✅ (AWN). Es
  la fuente directa para el punto 24 (obras parecidas por influencia, no
  sólo por parecido de catálogo).
- **Fondos pintados sobre capturas del propio videojuego** (ya lo tenía la
  biblia en §3, referencia al *Inside Look #2*): Trigger partió de
  renders/fotos de Night City de *Cyberpunk 2077* y pintó encima para
  darles el acabado 2D ✅ (ya citado en referencias.json, minuto 2:05-2:39
  del vídeo).
- **Programa de producción exacto** (Retas, Clip Studio, Toon Boom...): no
  lo dice ninguna entrevista en abierto que encontré (probé en inglés y
  japonés); Trigger viene de Gainax/Trigger, que tradicionalmente trabaja
  con **RETAS/Clip Studio Paint para el 2D** y **CG 3D propio para
  vehículos y algunos efectos** (dato de la industria, no específico de
  Edgerunners) · ⚠️ no confirmado para esta serie en concreto, dilo así en
  la biblia.

### 18.2 Lo que se ve (línea, sombreado, filtros) — de fotogramas y hojas

- **Línea**: gruesa y de color (no siempre negra: en las escenas de neón la
  línea de contorno se tiñe de cian o magenta), muy marcada en los
  primeros planos de acción — coherente con el estilo "Trigger" ya
  conocido en *Kill la Kill*/*Promare* ⚠️ (visual, de las hojas G y W ya
  citadas en la biblia; no medí un fotograma nuevo por presupuesto).
- **Sombreado**: cel-shading plano de 2-3 tonos en personajes, con
  degradados sólo en luces de neón y hologramas (ya lo dice §5 de la
  biblia sobre los rótulos con degradado lima) ✅.
- **Filtros de la animación**: grano sutil y aberración cromática
  (duplicado cian/magenta) en el logo y en los glitches de cyberpsicosis,
  donde los ojos del personaje "tartamudean" y se duplican — descrito en
  fuentes de análisis de estilo (⚠️ una fuente de menor calidad,
  [playcyberpunk.com](https://www.playcyberpunk.com/cyberpunk_edgerunners_gif/);
  visualmente coherente con lo que se ve en los GIF y en el logo oficial,
  pero no lo confirmé en un fotograma propio) · ⚠️.

### 18.3 Cómo reproducirlo en Photoshop

- **Pinceles**: de trazo grueso con bordes duros para el contorno; capa de
  grano de película con blend "Overlay" al 8-15%; capa de aberración
  cromática (duplicar la capa, desplazar 2-3 px los canales R y B, modo
  "Screen"). Pinceles de **glitch gratuitos** (más de 200, licencia libre
  para uso personal/comercial con atribución según el pack) en
  [Resource Boy](https://resourceboy.com/photoshop-brushes/glitch-brushes/).
- **Neón**: capa nueva, pincel blando, flujo bajo, modo "Color Dodge",
  varias pasadas para el halo — método explicado paso a paso en
  [Spoongraphics](https://blog.spoongraphics.co.uk/tutorials/how-to-apply-cyberpunk-style-color-grading-neon-effects-to-your-photos)
  (grano y aberración cromática incluidos en el mismo tutorial).
- **Capas típicas** para un personaje al estilo Edgerunners: línea (arriba,
  modo Multiplicar), color plano, sombra plana (Multiplicar, 60-70%),
  luces de neón (Color Dodge/Screen), grano (Overlay, opacidad baja),
  aberración cromática (Screen, desplazada), viñeta.

### 18.4 Cómo reproducirlo en Blender

- **Contorno**: dos caminos habituales — el modificador **Solidify** (caras
  invertidas hacia adentro, material negro, grosor 0.01-0.03) o el motor
  **Freestyle** (Render Properties → Freestyle, línea gruesa configurable
  por objeto); ambos explicados con pasos en
  [Artisticrender](https://artisticrender.com/cel-shading-in-blender/) y en
  el hilo de [Blender Artists](https://blenderartists.org/t/the-ultimate-cel-shading-shader/1413344).
  Para el contorno de color (cian/magenta en vez de negro, como en el logo)
  se cambia el material del Solidify por uno emisivo de ese color.
- **Sombreado tipo cel**: nodo *Shader to RGB* + una rampa de color (2-3
  bandas duras) en vez del degradado normal del Principled BSDF; es el
  método más citado para imitar el sombreado plano del anime en Eevee
  ([Artisticrender](https://artisticrender.com/cel-shading-in-blender/),
  [Medium — 4 métodos de cel-shading en Eevee](https://medium.com/@josephclaytonhansen/four-different-methods-for-making-cel-shaders-in-blender-eevee-2-8-2-9-6d976ce2555d)).
- **Luz y render**: luces de área de color (cian/magenta/amarillo) desde
  los lados para el efecto neón de Night City; *Bloom* del compositor de
  Eevee para los brillos; niebla/volumétricos bajos para la lluvia y el
  ambiente húmedo de la ciudad (visto en casi todas las escenas nocturnas).
- **Modelos y rigs libres del personaje** (Sketchfab, comprobados por su
  API):
  - **David Martinez** — modelo con **190.508 caras**, licencia
    **CC Attribution** ✅ ([Sketchfab](https://sketchfab.com/3d-models/none-0105aad132d04217ad2371da44b51f7a)).
  - **Rebecca** — modelo con **130.402 caras**, licencia **CC Attribution**
    ✅ ([Sketchfab](https://sketchfab.com/3d-models/none-c9a1a0795acc469bad9c0c47158e436b)).
  - **Lucy** — modelo "Sketchfab Broke", licencia **CC Attribution** ✅
    ([Sketchfab](https://sketchfab.com/3d-models/none-7cc2f167a5e84a1aa0bc620ef9b5dcfd)).
  - Todos piden crédito al autor original (no son oficiales, son fan-made);
    válidos como base de pose/rig, no para vender.
- **Texturas encima**: remite al punto 19 (rol imagen) para tramas y
  patrones; aquí sólo el procedimiento — proyectar la textura con UV
  y añadir una capa de ruido en el mapa de rugosidad para el aspecto
  "sucio" de Night City.

### 18.5 Encuadres y composición típicos

- **Contrapicados muy cerrados** en las peleas (cámara baja, personaje
  ocupando el cuadro) para dar sensación de poder — visible en los
  fotogramas ya citados de las hojas G y W de la biblia (§2, §14) ⚠️
  (observación visual, sin medir un fotograma nuevo).
- **Planos muy anchos y vacíos** para la soledad (David solo en su
  apartamento, Lucy en la azotea) contra **primerísimos planos** para la
  emoción fuerte (llanto, rabia) — mismo patrón que describen las reseñas
  de estilo consultadas (AWN) y que ya recoge la biblia en las escenas
  icónicas (§2) ✅.
- **La cámara imita la Sandevistan**: paneos rápidos con motion blur
  direccional y "smear frames" (fotogramas de estirado) en vez de
  interpolación limpia, según la misma entrevista de Yoshinari (§18.1) ✅.

## 24 · Obras parecidas y temas relacionados (sección nueva)

### 24.1 Influencias que el propio equipo reconoce

- *Akira*, *Ghost in the Shell* y *Blade Runner* — citadas directamente por
  el equipo de Trigger como referencia visual ✅ ([AWN](https://www.awn.com/animationworld/cyberpunk-edgerunners-vibrant-ode-retro-anime)).
- El director **Hiroyuki Imaishi** también dirigió *Gurren Lagann*, *Kill la
  Kill* y *Promare*; el diseñador de personajes **Yoh Yoshinari**, *Little
  Witch Academia* y *BNA: Brand New Animal*; el guionista **Yoshiki Usa**,
  *SSSS.GRIDMAN* ✅ (créditos de la [wiki de Cyberpunk](https://cyberpunk.fandom.com/wiki/Cyberpunk:_Edgerunners),
  sección «Production»). Todo el estilo de línea gruesa y acción exagerada
  de Edgerunners viene de esa casa (Trigger/ex-Gainax).

### 24.2 Recomendaciones de catálogo (AniList, ya en `datos-texto.md`)

De más votadas a menos: *Akudama Drive*, *Ghost in the Shell* (película),
*PSYCHO-PASS*, *Redline*, *Promare*, *Black Lagoon*, *Gurren Lagann*,
*LAZARUS*, *Akira*, *Akame ga Kill!*, *Devilman Crybaby*, *Cowboy Bebop*,
*Kill la Kill* ✅ ([AniList](https://anilist.co/anime/120377)). Las más
cercanas en tono (acción callejera, mercenarios, distopía) son *Akudama
Drive*, *PSYCHO-PASS* y *Black Lagoon*.

### 24.3 Qué otras láminas del servidor se le parecen

- **Choque directo de universo**: el encargo **114 — Cyberpunk 2077
  (juego)** es la misma IP (Night City, corpos, chrome) pero sin canal
  todavía y con otros personajes (V, Johnny Silverhand, Judy, Panam) ⚠️
  aviso de una línea, no un problema: si se hace más adelante, que use
  personajes y escenas *del juego*, no de la serie, para no repetir la
  lámina de #a-que-juegas.
- Sin más choques de tono cyberpunk/distópico entre los encargos ya
  revisados (comprobado con `grep -il` sobre los títulos de `encargos/`;
  no hay otro anime cyberpunk en la lista 01-127) ✅.

## 25 · El mundo, la historia y sus símbolos (sección nueva)

### 25.1 Las reglas del mundo en cinco líneas

1. **Night City** es una ciudad-estado corporativa de California en 2076,
   sin ley real fuera del control de las corporaciones y la policía
   (NCPD/MaxTac) ✅ ([wiki](https://cyberpunk.fandom.com/wiki/Cyberpunk:_Edgerunners), sección «Locations»; [AniList](https://anilist.co/anime/120377)).
2. **El chrome (cyberware)** mejora el cuerpo pero pasa factura: cuanto más
   implante llevas, más cerca estás de la **cyberpsicosis** (perder la
   humanidad y volverte una máquina violenta) ✅ (tags de AniList:
   «Cyborg», «Body Modification»; ya descrito en la biblia con Norris,
   ep. 1).
3. **Un edgerunner** es un mercenario fuera de la ley que vive "al filo":
   sin corporación que lo proteja, un solo error lo mata ✅ (glosario de
   la wiki, ver 25.3).
4. **Las corporaciones (Arasaka, Militech...) mandan de verdad**: la
   policía y el gobierno son secundarios frente a su poder económico y
   militar ✅ (páginas de facciones, 25.2).
5. **Todo es desechable y a la vez carísimo**: la gente vive apretada en
   megaedificios (H4) mientras los corpo viven en torres de cristal; la
   lluvia constante y el neón son el fondo de todo ✅ (visual, ya descrito
   en §5 de la biblia).

### 25.2 La historia por arcos (con los 10 episodios y su minuto de estreno)

Fuente: ficha de episodios de la [wiki de Cyberpunk](https://cyberpunk.fandom.com/wiki/Cyberpunk:_Edgerunners#Episodes)
(duración exacta de cada uno) y las líneas de «Descripción» de cada página
de episodio ✅ (dos fuentes: la tabla de la wiki y la página propia de cada
episodio).

**Arco 1 · De la calle a edgerunner (ep. 1-4)**
- Ep.1 «Let You Down» (24m14s): David ve una braindance ilegal, vive con
  su madre en un apartamento pobre de H4.
- Ep.2 «Like A Boy» (24m12s): con su cuerpo recién potenciado, busca
  venganza en la Academia Arasaka; conoce a Lucy.
- Ep.3 «Smooth Criminal» (24m20s): pide unirse al equipo de edgerunners de
  Maine, mientras Arasaka intenta recuperarlo.
- Ep.4 «Lucky You» (24m12s): Maine pone a Lucy a entrenarlo.
- **Momento clave**: la muerte de Gloria (madre de David) y su primer
  trabajo con el equipo, el punto de no retorno.

**Arco 2 · El ascenso (ep. 5-7)**
- Ep.5 «All Eyez On Me» (23m30s): David propone una estrategia; el
  objetivo resulta ser más peligroso de lo pensado.
- Ep.6 «Girl on Fire» (25m48s): Maine empieza a comportarse raro (avance
  de su cyberpsicosis) mientras el equipo interroga a un prisionero.
- Ep.7 «Stronger» (24m14s): David, ya una estrella del gremio con más
  implantes, lidera una misión nueva; un viejo contacto le ofrece un
  trabajo grande (Faraday).
- **Momento clave**: la caída de Maine (cyberpsicosis) — el giro que
  empuja a David a liderar el equipo.

**Arco 3 · La caída (ep. 8-10)**
- Ep.8 «Stay» (24m16s): Faraday, atrapado entre Arasaka y Militech; Lucy y
  Rebecca confrontan a David por cómo ha cambiado.
- Ep.9 «Humanity» (25m18s): los captores de Lucy descubren su pasado y su
  misión secreta; el trabajo de Faraday sale mal.
- Ep.10 «My Moon My Man» (26m54s): David, al borde de la cyberpsicosis,
  entra a Night City a salvar a Lucy mientras Arasaka despliega su arma
  letal (Adam Smasher).
- **Momento clave**: el final agridulce, con la canción **«I Really Want
  to Stay at Your House»** sonando sobre la Luna (ya citado en la biblia,
  §11).

### 25.3 Emblemas, logos y objetos icónicos

- **Logos de las corporaciones y bandas**, con su imagen y tamaño
  (medidos con Pillow, todas de la wiki oficial vía API con
  `Referer: https://www.fandom.com/`):
  - **Arasaka**: rojo, tipografía angular con un árbol/raíz dentro de un
    círculo — 1920×1080 ✅ ([wiki](https://static.wikia.nocookie.net/cyberpunk/images/5/5f/Arasaka_Logo_CP2077.png)).
  - **Militech**: azul/gris, letras industriales anchas — 3840×582 ✅
    ([wiki](https://static.wikia.nocookie.net/cyberpunk/images/6/67/Militech_Logo_CP2077.png)).
  - **Maelstrom**: rojo agresivo, símbolo de calavera/máquina — 1389×675 ✅
    ([wiki](https://static.wikia.nocookie.net/cyberpunk/images/1/19/Maelstrom_Logo_CP2077.png)).
  - **Tyger Claws**: naranja/negro, garra estilizada — 1391×1059 ✅
    ([wiki](https://static.wikia.nocookie.net/cyberpunk/images/4/4d/Tyger_Claws_Logo_CP2077.png)).
  - **Valentinos**: 506×845 ✅, **6th Street**: 1920×1080 ✅, **Kang Tao**:
    1920×407 ✅ (mismas fuentes, wiki de Cyberpunk). Ninguna de estas
    bandas/corpos sale con protagonismo en Edgerunners salvo Arasaka y
    Militech (Faraday, ep. 8) y Maelstrom (mencionada en el juego); útiles
    para carteles de fondo en la lámina, no para el centro.
- **El emblema de la chaqueta de David** (runa verde en la espalda): **no
  es un logo inventado**, es el logo de la serie de braindance «Edgerunners»
  del editor **Jimmy Kurosaki** (32 episodios de XBD) que aparece en el
  ep. 5; Lucy lo probó proyectado en la tela y David acabó pintándolo a
  mano ✅ **confirmado en dos páginas de la wiki**:
  [David's Jacket](https://cyberpunk.fandom.com/wiki/David%27s_Jacket) y
  [Jimmy Kurosaki](https://cyberpunk.fandom.com/wiki/Jimmy_Kurosaki). Esto
  **resuelve la duda ⚠️ que dejó la biblia** («si el emblema verde... es
  el logo de la serie»): sí lo es, y además tiene una historia propia
  dentro de la ficción (no es sólo "el logo de Edgerunners"), es un guiño
  dentro del guiño.
- **Objeto icónico para #a-que-juegas**: la recreativa de **Roach Race**
  (ya la tiene la biblia en §13, con tabla de récords) sigue siendo la
  mejor opción real: es un objeto físico, del propio juego, con lluvia y
  neón alrededor.

### 25.4 Vocabulario propio (glosario del universo)

De la página oficial de jerga de la franquicia ✅
([Cyberpunk Wiki — Streetslang](https://cyberpunk.fandom.com/wiki/Streetslang)),
cruzado con los subtítulos ya citados en la biblia (§2, donde se oyen
varias de estas palabras):

| Palabra | Qué significa |
|---|---|
| **Choom** / choomba | Amigo, compañero |
| **Gonk** | Idiota, torpe (o «gonk move» = mala decisión) |
| **Eddies** | Dinero (eurodólares) |
| **Preem** | Genial, de primera |
| **Delta** | Irse, largarse |
| **Flatline** | Matar / morir |
| **Chrome** / chromed | Cyberware / tener implantes |
| **Edgerunner** | Mercenario que vive al filo de la ley |
| **ICE** | Programas de seguridad contra hackers |
| **Merc** | Mercenario |
| **Ripperdoc** | Cirujano clandestino de implantes |
| **Cyberpsicosis** | Perder la humanidad por exceso de chrome |
| **Braindance (BD)** | Grabación sensorial de una experiencia ajena |
| **Netrunner** | Hacker que entra en la red directamente |
| **Sandevistan** | Implante que ralentiza el tiempo (el de David) |

Todas usadas o mencionadas en la serie (choom y gonk ya salían citadas en
la bitácora anterior de la biblia; el resto lo confirmo yo con la página
de jerga).

## Lo mejor para la lámina

- El logo de la chaqueta de David **no es un adorno**: es el logo de la
  XBD *Edgerunners* de Jimmy Kurosaki, con su propia historia — un detalle
  perfecto para "hablar en el idioma" de la serie en la lámina.
- La técnica real del Sandevistan (fotogramas de color repetidos, no un
  filtro) explica por qué cualquier efecto de "velocidad" en la lámina
  debe verse **dibujado**, no como un blur de Photoshop plano.
- Vocabulario listo para el texto del canal: *choom*, *preem*, *gonk*,
  *eddies* dan sabor sin traducir mal el tono.
- Blender: Solidify o Freestyle + *Shader to RGB* con rampa dura es la
  combinación más simple para un render fiel al cel-shading de la serie.
- Rigs libres de David, Lucy y Rebecca en Sketchfab (CC BY) listos para
  posar en Blender sin partir de cero.

## No encontré

- El **software exacto de producción** de Trigger para Edgerunners
  (Retas/Clip Studio/Toon Boom): sin entrevista técnica en abierto, en
  inglés ni japonés. ⚠️ No es obligatorio para el punto 18 (que pide "según
  entrevistas", y ya cito las que sí hablan de técnica), pero lo dejo
  anotado como extra que falta.
- Captura clara y medida de la **lista vertical de opciones de diálogo**
  del juego (Game UI Database bloqueada por Cloudflare, sin snapshot en
  Wayback). ⚠️ extra, ya está el resto del punto 6 confirmado.
- Acceso directo a **The Cutting Room Floor** para *Cyberpunk 2077*
  (Cloudflare, dos intentos); confirmé por búsqueda que la página existe y
  qué contiene a grandes rasgos, pero no el detalle completo. ⚠️ extra.

## Bitácora de búsqueda (esta tanda)

- Fandom API (`cyberpunk.fandom.com/api.php`): wikitext de Streetslang,
  Cyberpunk: Edgerunners (principal + episodios), Jimmy Kurosaki, David's
  Jacket; `imageinfo` de logos de Arasaka, Militech, Maelstrom, Tyger
  Claws, Valentinos, 6th Street, Kang Tao y de la chaqueta de David.
- GitHub `raw.githubusercontent.com/google/fonts`: descarga y comprobación
  con fontTools de M PLUS Rounded 1c.
- Sketchfab API: búsqueda de modelos de David Martinez, Rebecca y Lucy
  (licencias y caras).
- WebSearch (en): «Cyberpunk Edgerunners animation style interview
  Imaishi», «line art shading chromatic aberration film grain visual
  style», «Retas Clip Studio Paint compositing software», «Blender toon
  shader Line Art Freestyle Solidify», «Photoshop cyberpunk brushes neon
  grain chromatic aberration», «Cyberpunk 2077 dialogue choice menu
  screenshot UI», «site:tcrf.net Cyberpunk 2077».
- WebFetch: artículo de Animation World Network (citas de la entrevista de
  Netflix con Otsuka/Imaishi/Yoshinari); interfaceingame.com (captura de
  diálogo); tcrf.net (403, Cloudflare).
- Wayback Machine (`archive.org/wayback/available`): comprobado
  gameuidatabase.com y tcrf.net, sin snapshot útil.
- No usé más buscador web del necesario: 7 búsquedas de las ~50 del cupo.

Los 6 puntos (5, 6, 11, 18, 24, 25) están cubiertos con lo obligatorio. Lo
que falta (software exacto de producción, captura de opciones de diálogo,
TCRF completo) son extras, ya anotados en «No encontré», no pendientes.
