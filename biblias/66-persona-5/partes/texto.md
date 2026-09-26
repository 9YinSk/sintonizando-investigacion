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

