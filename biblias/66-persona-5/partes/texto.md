# Persona 5 — parte de TEXTO, JUEGOS Y TÉCNICA (puntos 5, 6, 11, 18, 24, 25)

Investigador de texto. Libreta de datos: un dato por línea, con fuente y ✅/⚠️.

## 5 · Tipografía

Persona 5 tiene tipografía **oficial documentada por la propia fundición** (Fontworks/Monotype, Japón) además de análisis de fans para la versión occidental. Cada letra libre de abajo la comprobé yo con `fontTools` (á, ñ, ¿, ¡).

- **Fuente japonesa del texto del juego**: **スランプ (Slump)**, de Fontworks, «usada en el texto del juego» · ✅ ficha oficial del fabricante ([fontworks.co.jp/case/3471](https://fontworks.co.jp/case/3471/)) — plataforma PS3/PS4, fecha de salida 15-sep-2016.
- **Fuentes de Persona 5 Tactica** (2023): **ラグランパンチ (Raglan Punch), 花風テクノ (Kafu Techno), UD丸ゴ_ラージ (UD Marugo Large), ユールカ (Yurka) y ロダン (Rodin)**, para «texto del juego, UI» · ✅ ficha oficial ([fontworks.co.jp/case/15692](https://fontworks.co.jp/case/15692/)).
- **Rodin** (Fontworks) se usa además para menús, tiempos y acciones en la versión japonesa de Persona 5 Royal · ⚠️ (recopilación de fans, un hilo).
- **Fuente de los globos/diálogo en la versión occidental**: identificada por la comunidad como **Charisma / KoreanKRSM**, de la fundición surcoreana AsiaFont (Atlus modificó el apóstrofo, las comillas y el acento grave por versiones en forma de coma) · ⚠️ (un hilo detallado y verificado por dos usuarios independientes en [WhatFontIs](https://www.whatfontis.com/post-38011.html), pero sin confirmación oficial de Atlus).
- **La interfaz en inglés NO usa Slump** (la fuente japonesa oficial): existe un mod llamado **«Slumpy English»** que sustituye la fuente inglesa por Slump, lo que confirma que son distintas · ✅ dos fuentes ([GameBanana](https://gamebanana.com/mods/613348), recopilación de fans que cita Charisma/Slump/Optima Nova Black/Arsenal/P5 Hatty como las fuentes mezcladas del UI).
- **Logo «PERSONA 5»**: analizado por fans como **Futura Std Bold** inclinada unos 33°, con el «5» en **Manufacturer JNL Oblique** · ⚠️ (hilo de dafont con 2 aportes independientes, [dafont.com/forum](https://www.dafont.com/forum/read/291180/what-font-is-this-persona-5-logo-font)); ninguna es de licencia libre.
- **P5 Hatty**: fuente hecha por fans (Hatty Mikune) que imita el estilo urbano/graffiti del juego · ⚠️ «gratis sólo para uso personal» (no es de licencia libre plena para uso comercial).

### Una letra libre por uso (comprobadas con fontTools)

| Uso | Letra libre elegida | Fuente/licencia | á/ñ/¿/¡ |
|---|---|---|---|
| Logo o título | **Jost** (Google Fonts) — geométrica, mismo espíritu que la Futura del logo real | Google Fonts, gratis | ✅ todas presentes |
| Globo normal (manga) | **Anime Ace 2.0 BB** (Blambot) — estándar del lettering de manga en inglés, la usan DB y Naruto en esta misma biblioteca de series | Blambot, gratis sólo uso personal | ⚠️ no pude descargar el archivo para comprobarla yo (dafont y las réplicas la bloquean a curl); Blambot la anuncia con juego de caracteres occidental completo |
| Grito | **Bangers** (Google Fonts) — ya usada para Spider-Verse en esta biblioteca | Google Fonts, gratis | ✅ todas presentes |
| Pensamiento | **Caveat** (Google Fonts) — trazo manuscrito, para el tono más íntimo/interior | Google Fonts, gratis | ✅ todas presentes |
| Onomatopeya | **Anton** (Google Fonts) — muy negra y de impacto | Google Fonts, gratis | ✅ todas presentes |
| Cartel del mundo (calling card / carteles del Metaverso) | **Earwig Factory** (Typodermic, dafont) — letras sueltas de nota de rescate sobre fichas irregulares, el mismo look de la calling card | dafont, gratis (Typodermic Desktop License) | ✅ todas presentes (comprobado con fontTools: á, ñ, ¿, ¡, é, ü) |
| Interfaz de juego | **Oswald** (Google Fonts) — condensada y muy negra, el mismo espíritu que Rodin/Slump en los menús reales | Google Fonts, gratis | ✅ todas presentes |
| Subtítulos o créditos | **Archivo** (Google Fonts) — grotesca limpia, legible en tamaño pequeño | Google Fonts, gratis | ✅ todas presentes |

## 6 · Cuadros de diálogo, cartelas y cómo hablan en pantalla

Miré capturas oficiales reales (Steam, 1920×1080) de Persona 5 Royal y Strikers para describir el cuadro de diálogo con exactitud, no de memoria.

- **El cuadro de diálogo del juego**: un **cuadrilátero blanco irregular** (ningún lado recto ni paralelo) con **borde negro grueso** y una **cola en punta angulosa** (no curva) que señala al busto de quien habla · ✅ visto en 2 capturas distintas de P5 Royal ([captura 1](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1687950/ss_663171dc3afce8fe987e57e8659f91b69faa39bc.1920x1080.jpg), [captura 2](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1687950/ss_c665872b4c5cb3a4e4fd3a4abde97ee60fe51e33.1920x1080.jpg)).
- **El nombre de quien habla** va en una **cinta/ribete negro inclinado** encima del cuadro, con el texto en blanco o gris claro y ligeramente cursivo (ej. «Maruki», «Kasumi», «Shadow Kamoshida») · ✅ visto en 3 capturas.
- El **texto del diálogo va en negro, alineado a la izquierda**, sobre el blanco del cuadro.
- **El retrato (bust) de quien habla** aparece recortado, apoyado en la esquina inferior izquierda de la pantalla, superpuesto sobre el cuadro de diálogo, no dentro de él.
- Abajo a la derecha del cuadro, **tres iconos de control**: «FFWD» (avance rápido), «Auto» y «Log» (historial) · ✅ visibles en todas las capturas con diálogo.
- **El calendario/reloj** (arriba a la izquierda, fuera del diálogo): una **placa negra irregular** con la fecha en números grandes, el día de la semana y un icono de sol/luna, todo en blanco · ✅ (mismo look en 3 capturas de fechas distintas).
- **Coincide con lo ya documentado en esta biblioteca de series** (`_ya_hechas/_Cuadros de dialogo por franquicia`, §34): cuadrilátero negro torcido con borde blanco grueso y cola en triángulo, nombre en tira blanca inclinada — la diferencia que veo yo en las capturas 2024-2025 es que el cuadro es de **fondo blanco con borde negro** (no al revés); puede haber variado entre versiones o zonas de la UI (menú vs. combate vs. historia). Lo marco como comprobado con capturas propias ✅ y dejo la referencia previa como variante ⚠️.
- **Cartelas de estilo cómic (pantallas de "Baton Pass"/rango de confidente)**: página estilo panel de cómic con **tramas de puntos (halftone)**, bordes con motivo floral, y un titular en **letras recortadas tipo nota de rescate** («Beauty is Devotion», sobre Ann/Carmen) · ✅ visto directamente en captura oficial de P5 Royal ([captura](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1687950/ss_63d2164bf39a43905e9602381f43a9ad4ab46dea.1920x1080.jpg)).
- **La calling card** (tarjeta de aviso de robo a los Palace rulers): fondo negro, texto blanco recortado tipo «nota de rescate» con letras sueltas en fichas irregulares y alguna letra invertida — documentado ya en esta biblioteca (§34.1) y confirmado por un generador de fans que replica el formato exacto: [Persona 5 Calling Card Maker](https://skyventuree.github.io/p5cc/) ✅ (dos fuentes independientes).
- **En el manga** (Hisato Murasaki, ATLUS): usa el lenguaje visual estándar de manga occidentalizado: globo ovalado de contorno negro para habla normal, nube de círculos pequeños para pensamiento — no encontré capturas oficiales en alta del interior del tomo en inglés (Udon) para confirmar la fuente exacta de letra; el estudio de licencia no publica esos datos ⚠️.
- **Videojuegos de la franquicia (punto 11), interfaz y HUD**:
  - **The Game UI Database** cataloga Persona 5 y Persona 5 Royal con las categorías: *Dialogue & Speech, Dialogue Choice, Modal: Option & Menu, Modal: Item Get, Cutscenes & Story, Stage Intro, Results Screen, Ability List, Equipping, Area Map, Codex & Journal* · ✅ [ficha P5](https://www.gameuidatabase.com/gameData.php?id=72), [ficha P5 Royal](https://www.gameuidatabase.com/gameData.php?id=618).
  - **Persona 5 Strikers** (acción en tiempo real): HUD de combate con menú de comandos rojo diagonal **PERSONA / ATTACK / SUPPORT / GUN**, contador de «Actions», iconos de personajes arriba a la izquierda con barras de HP/SP · ✅ visto en captura oficial ([captura](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1382330/ss_dcf8139ee8becf74ebbcda5d818ea4d9f16dc64f.1920x1080.jpg)).
  - **Persona5: The Phantom X** (gacha móvil/PC, 2025) mantiene la misma familia visual: diálogo con retrato y cinta de nombre, paleta roja/negra · ✅ visto en captura oficial de Steam.
  - **Persona 5 Tactica** (táctico) usa el mismo lenguaje de calendario y diálogo pero con la paleta morada de los Marukis/nuevo enemigo, y añade iconos de cobertura y turnos propios del género táctico · ✅ visto en captura oficial.
- **Hojas de contacto propias**: `/tmp/claude-0/trabajo/66-persona-5-texto/screenshots/contacto1.jpg` y `contacto2.jpg` (8 capturas oficiales de Steam, miradas directamente).

## 11 · Videojuegos de la franquicia

- **Persona 5** (PS3/PS4, 15-sep-2016) y **Persona 5 Royal** (2019/2022) · fuente japonesa oficial del texto: **Slump** (Fontworks) ✅.
- **Persona 5 Strikers** (acción, 2020/2021): HUD de combate en tiempo real con menú de comandos diagonal rojo **PERSONA / ATTACK / SUPPORT / GUN**, contador de «Actions» y barras de HP/SP por personaje arriba a la izquierda ✅ (captura oficial Steam).
- **Persona 5 Tactica** (táctico, 2023): fuentes oficiales **Raglan Punch, Kafu Techno, UD Marugo Large, Yurka y Rodin** ✅ (ficha Fontworks); añade iconos de cobertura y turno propios del género, sobre la misma paleta roja/negra.
- **Persona5: The Phantom X** (gacha para PC/móvil, 2025): mantiene el mismo lenguaje visual — diálogo con retrato, cinta de nombre, calendario de fecha ✅ (captura oficial Steam).
- **Idiomas con interfaz y texto**: la tabla completa de idiomas de cada versión está en `datos-texto.md` (recolectada de Steam); en japonés, coreano y chino la interfaz y los diálogos están totalmente localizados en Royal, Strikers y Tactica — útil si la lámina necesita texto de fondo en esos alfabetos.
- **The Game UI Database** (base de datos especializada en UI de videojuegos) cataloga Persona 5 y Royal con capturas propias por categoría (título, diálogo, modales, combate, inventario, mapa) ✅ [P5](https://www.gameuidatabase.com/gameData.php?id=72) · [P5 Royal](https://www.gameuidatabase.com/gameData.php?id=618).
- **No encontré** una wiki de datamining o TCRF específica de Persona 5 con contenido descartado: TCRF (`tcrf.net/Persona_5`) está protegido por un desafío anti-bot de Cloudflare que ni `curl` ni `navegar.py` consiguen pasar (403 en ambos, dos intentos cada uno) ⚠️.

## 18 · Estilo de dibujo y técnica, y cómo replicarlo (rigs y tramas: ver puntos 3 y 19)

Fuente principal: la charla oficial de Atlus en **CEDEC+KYUSHU 2017** (recogida por Famitsu), con los propios diseñadores de la UI. Es un *making of* real, no un análisis de fans.

### Cómo lo hizo el estudio (fuente primaria)
- Ponentes: **Kazuhisa Wada** (productor de la saga Persona) y **Masayoshi Suto** (director de arte y líder de diseño de UI de Persona 5, primer diseñador de UI dedicado que tuvo Atlus) · ✅ [Famitsu, CEDEC+KYUSHU 2017](https://www.famitsu.com/news/201711/13145540.html).
- **Herramientas**: **Photoshop, Illustrator y After Effects** — las mismas que usa Suto desde hace 18 años, el flujo de trabajo apenas cambió ✅.
- **Concepto de diseño**: «**pop punk**» — *pop* (de masas, accesible) + *punk* (anti-sistema) ✅.
- **Proceso de color**: primero se decide el **color principal** (P5 = rojo; P3 = azul; P4 = amarillo; Catherine = rosa fucsia), y en el mismo momento ya está resuelto el **logo del título** y la **tipografía clave**. Persona 5 evita casi todo color secundario a propósito, para que el rojo destaque solo (sólo HP/MP llevan otro color) ✅.
- **Guía de la vista**: una **línea blanca central** en los menús dirige la mirada del jugador; al bajar de nivel en un menú **cambian el ángulo y el layout** para que se note el cambio de jerarquía; el **brillo** sube en la información más importante y baja en la secundaria ✅.
- **Los modelos 3D que se mueven en los menús** se hicieron con una herramienta propia: primero el *layout* en Photoshop, luego un diseñador de movimiento crea la pose, se coloca con la herramienta interna, y al final se dibuja una ilustración 2D «de remate» (*kime cut*) que coincide con la pose 3D final ✅.
- **La pose del protagonista al confirmar** (mano extendida hacia la cámara) está inspirada en el gesto de una estrella de Hollywood tapando la cámara a los paparazzi ✅.
- **Implementación**: cada sección (batalla, historia…) tenía su propio programador de UI; los diseñadores entregaban «hojas de coordenadas» (más de 1000 páginas en papel) y ajustaban «un píxel, un fotograma» junto al programador ✅.
- **Optimización**: texturas empaquetadas «como Tetris» para ahorrar espacio; como PS3 y PS4 tienen resoluciones distintas, se hicieron los gráficos en **rutas vectoriales** (no mapa de bits) para escalar sin perder calidad; contrataron temporales sólo para generar esas rutas ✅.

### El anime (Persona 5 the Animation, CloverWorks, 2018)
- Estudio: **CloverWorks**; director: **Masashi Ishihama** (fan declarado del estilo del juego, contratado en parte por eso) · ✅ dos fuentes ([All the Anime](https://blog.alltheanime.com/adapting-persona5/), [Wikipedia](https://en.wikipedia.org/wiki/Persona_5:_The_Animation)).
- **Diseñadora de personajes de la animación: Tomomi Ishikawa**, adaptando el diseño original de **Shigenori Soejima**; el estudio dice que «hay muy pocos animadores en la industria que sepan dibujar en el estilo de Soejima» y que Ishikawa fue la que mejor lo logró mientras lo animaba ✅.
- Los animadores de efectos estudiaron el videojuego «hasta que se les pusieron los ojos rojos» para replicar sus detalles (partículas, destellos, cortes de cómic) ✅.
- **Graphinica** (estudio de CG) importó los modelos 3D de los jefes (Shadows) del propio videojuego a la animación, con más detalle y animaciones nuevas ✅.
- El equipo **empezó a animar mientras el juego aún se hacía**, trabajando codo a codo con Atlus, y retrasaron el inicio de producción un mes para que todo el equipo se jugara el juego antes de adaptarlo ✅.
- **La apertura (OP) «Wake Up, Get Up, Get Out There»**: animación de **Production I.G** (no CloverWorks), dirección de storyboard y animación de **Sayo Yamamoto** (directora también de *Yuri!!! on Ice*), supervisor de animación **Kōichi Arai**, CGI por el estudio **sublimation**, dirección de arte de fondos **Seiki Tamura** · ✅ créditos oficiales completos en [Art of the Title](https://www.artofthetitle.com/title/persona-5/).
- **Ishihama no empieza a hacer el storyboard de una apertura hasta que puede cantar la canción entera**, para sincronizar cada corte con la letra ✅ (All the Anime).

### El manga (Hisato Murasaki, Shogakukan, 2016-)
- Entrevista propia en español (Manga Barcelona, vía Ramen Para Dos): Murasaki dice que su método es **decidir qué es «lo principal» de la historia del juego (100 horas) y descartar lo que no entra**, para que el manga no se alargue demasiado; reconoce que muchos personajes secundarios quedan poco desarrollados por esta poda · ✅ [entrevista completa](https://ramenparados.com/entrevista-a-hisato-murasaki-autor-del-manga-persona-5/).
- No dio detalles técnicos de programas o pinceles en esta entrevista ⚠️.

### Tipo de línea, sombreado y filtros (visto en las capturas oficiales)
- **Línea de contorno negra gruesa y constante** en personajes 3D y en las ilustraciones 2D «kime cut», sin variación de grosor por luz (contorno tipo cómic, no acuarela) ✅.
- **Sombreado plano por bandas** (cel-shading de 2 o 3 tonos) en los personajes 3D de las cinemáticas de combate, con un tono de sombra rojo/morado saturado, no gris neutro ✅ (visto en capturas).
- **Tramas de medio tono (halftone/screentone)** en las pantallas de cómic (rango de confidente, «Beauty is Devotion») y en fondos de menú — puntos regulares, no degradado suave ✅ (visto directamente).
- **Destellos de luz tipo lente (flare) y rayas de velocidad** en las transiciones de combate y en la pantalla de grupo con alfombra roja ✅ (visto directamente).
- **Encuadres y composición**: los `kime cuts` (ilustraciones de remate) usan **ángulos bajos y diagonales muy marcadas**, con el personaje cortando la composición en dos triángulos — mismo lenguaje que un splash page de cómic. Los diálogos usan **plano medio con el retrato en la esquina inferior**, nunca centrado. Las escenas de "Todos por uno" (*All-Out Attack*) usan un **fondo rojo saturado con figuras en silueta** desde un ángulo bajo, como una portada de disco de punk.

### Cómo replicarlo en Photoshop
1. **Línea**: pincel de entintado con los ajustes «Assorted Brushes → Ink pen» o un pincel duro al 100% opacidad, grosor constante (2-3 px a 1080p), color **negro puro** (no gris), en su propia capa «Línea» con modo Multiplicar.
2. **Color plano**: capas «Base» por zona (piel, pelo, ropa) rellenas con el cubo de pintura, sin degradado; el rojo principal debe ser el más saturado de la imagen y casi ningún otro color debe competir con él (regla de la sub-color casi nula que usó Suto).
3. **Sombra**: una capa nueva en modo Multiplicar, pincel duro, 1-2 tonos de sombra por zona (no más), en un rojo/morado oscuro en vez de gris — así se ve el cel-shading real del juego.
4. **Trama (halftone)**: filtro `Filtro > Pixelar > Trama de color` a un solo canal, o un patrón de puntos importado como superposición en modo Multiplicar al 30-50% de opacidad, sólo en las zonas de sombra o en cartelas de cómic.
5. **Cartelas y calling card**: forma de polígono irregular (herramienta Lazo poligonal) en blanco o negro, borde de 6-10 px, y texto cortado en fichas sueltas superpuestas con pequeñas rotaciones (2°-8°) para el efecto «nota de rescate».
6. **Filtro de luz**: capa de destello (`Filtro > Render > Destello`) en modo Trama o Color añadir, muy sutil, sólo en los momentos de impacto.
7. **Grano**: una capa de ruido monocromo (`Filtro > Ruido > Añadir ruido`, 3-5%, monocromático) en modo Superponer sobre todo el compuesto, para el look ligeramente sucio de las cinemáticas.

### Cómo replicarlo en Blender
1. **Contorno**: activar **Freestyle** (Render Properties → Freestyle) con grosor de línea 2-3 px y color negro puro; alternativa más rápida: modificador **Solidify** con normales invertidas y material *shadeless* negro (mismo truco que usan mods de otros juegos toon).
2. ***Shader***: **Shader to RGB** + nodo **Color Ramp** con 2-3 escalones duros (no degradado) conectado a un Principled BSDF con Roughness alto y sin specular fuerte, para imitar el cel-shading de 2-3 bandas visto en las cinemáticas.
3. **Luz**: una luz de área principal dura (sin sombras suaves) más una luz de relleno roja tenue desde abajo, para el ambiente del Metaverso.
4. **Render**: Eevee (más rápido, ideal para previews) con *Bloom* activado a baja intensidad para los destellos; para el render final, Cycles con muestras bajas (32-64) porque el estilo no necesita ray-tracing realista.
5. **Texturas encima**: pintar una textura de trama de puntos en un canal aparte y mezclarla sólo en las zonas de sombra con un nodo Mix por máscara, igual que el paso 4 de Photoshop.
6. **Rigs y tramas**: ver puntos 3 y 19 (los trae el investigador de imagen).

