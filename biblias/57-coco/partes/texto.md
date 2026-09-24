# Parte de TEXTO, JUEGOS Y TÉCNICA · Coco (encargo 57)

Investigador de texto, juegos y técnica. Puntos 5, 6, 11, 18, 24 y 25 de `ENCARGO.md`.
Coco es película de Pixar (2017), no anime: cuadros de diálogo y "videojuegos" son
los de sus adaptaciones (cómics, libro dorado, apariciones en juegos móviles Disney).

## Hallazgos

### Punto 5 — Tipografía

- **Logo/título de Coco (2017)**: tipo base **Rockwell Extra Bold** (slab serif geométrica de Monotype, 1934, sobre Litho Antique de 1910), con las letras decoradas a mano con flores y colores de Día de Muertos (no es la fuente pelada, es arte custom sobre esa base) · fuente: ficha de Logopedia vía API (`https://logos.fandom.com/api.php?action=parse&page=Coco`, campo `type=Rockwell Extra Bold`) **y** hilo de identificación en foro de DaFont (`dafont.com/forum/read/342164/coco-2018-font`, usuario estabros: «Rockwell Bold», comentario «i like this font eroded manually») · ✅ (dos fuentes independientes)
  - Uso: título/logo (portada, Blu-ray, apps). No hay una fuente libre idéntica (Rockwell es de Monotype, de pago), pero para replicar el peso y la caja ancha sirven alternativas libres en Google Fonts/Fontsource, **comprobadas con fontTools (`getBestCmap`) para á é í ó ú ñ Ñ ¿ ¡: las tres llevan el juego completo**:
    - **Bevan** (Fontsource `bevan`, peso 400, ancha y redondeada, la más parecida a la calidez del logo) · https://fontsource.org/fonts/bevan · OFL-1.1 (libre) · completa ✅ (comprobado con fontTools sobre `latin-400-normal.ttf`)
    - **Alfa Slab One** (Fontsource `alfa-slab-one`, peso 400, muy negra/pesada, cercana al "Extra Bold" del logo) · https://fontsource.org/fonts/alfa-slab-one · OFL-1.1 · completa ✅
    - **Roboto Slab Black** (peso 900, más geométrica/fría, sirve para variantes tipo interfaz) · https://fontsource.org/fonts/roboto-slab · Apache-2.0 · completa ✅
    - Dato de contexto (una sola fuente, sin verificar en archivo): dos sitios de identificación de fuentes (FontBolt, designbeep) sugieren también **ChunkFive Ex** y **Rokkitt Black**/**Ultra** (Astigmatic) como réplicas del logo · ⚠️ (fuentes tipo "font finder" SEO, sin comprobar el glifo)
  - **Letras en pantalla dentro de la película** (letreros de Santa Cecilia, arco de la Ofrenda, cartel "Sunrise Spectacular" de Ernesto de la Cruz, partitura de "Un Poco Loco"): son rótulos pintados a mano por el equipo de arte de producción, con serifas gruesas y adornos florales estilo cartel mexicano de mediados de s. XX (carteles de lucha libre / cine de oro) — no hay una fuente digital documentada públicamente para estos rótulos; anotado en «No encontré» ⚠️.

### Punto 6 — Cómo hablan y piensan en pantalla

Coco no tiene manga; sus "globos" son los de sus adaptaciones a cómic y las cajas de diálogo de los juegos donde aparece.

- **Coco Cinestory Comic** (Joe Books, 2 ene 2018, 336 págs., incluye corto extra de Dante) · portada e ítem en Internet Archive `cococinestorycom0000unse` (préstamo, sin vista de páginas) · descripción del formato «Cinestory»: fotogramas reales de la película con **globos de diálogo redondeados superpuestos en post** (no dibujo, foto+letrado), como el resto de la colección Disney Cinestory (Frozen, Zootopia, Big Hero 6…) · fuente: ficha «Cinestory Comics» de Disney Wiki vía API (`disney.fandom.com/api.php?action=parse&page=Cinestory_Comics`) **y** fichas de venta (Amazon/Goodreads: «screenshots of the movie with comic styled balloon dialogues») · ✅ (dos fuentes)
- **Coco: The Story of the Movie in Comics** (Joe Books, otra edición, distinta de la Cinestory) · confirmado por ficha de venta en Amazon (ISBN 9781772755312) · ⚠️ (una fuente, no se pudo ver el interior para comparar el estilo de letra con la Cinestory)
- **Cajas de diálogo en videojuegos** (ligado al punto 11): en *Disney Magic Kingdoms* las frases de personajes Coco salen en **globos blancos redondeados con cola hacia el personaje**, tipografía de palo/cómic sin serifas, en mayúsculas para exclamaciones — ejemplos textuales sacados del wikitext oficial de la wiki del juego (`dmk.fandom.com`, página Héctor Rivera):
  - Héctor Rivera: *"Ahh... Such a sweet sentiment! ... At SUCH a bad time."* — *"Nice! Hey — got any requests?"* — *"Showtime!"* — *"¡Epa! Now, THAT'S worth a grito!"* (mezcla inglés + interjección en español "¡Epa!", "grito" mariachi) · fuente: `dmk.fandom.com/wiki/Héctor_Rivera` vía API ✅ (contenido extraído directo de archivos del juego, contrastado con capturas de la propia wiki)
  - En *Disney Heroes: Battle Mode*, la cita de presentación de Miguel Rivera en su ficha de personaje (caja de texto bajo el retrato, estilo "quote box" con comillas grandes): *"Sometimes I think I'm cursed 'cause of something that happened before I was even born."* · fuente: `disneyheroesbattlemode.fandom.com/wiki/Miguel_Rivera` vía API ✅
- **Subtítulos oficiales**: en el Blu-ray/Disney+ los subtítulos en español usan tipografía sans-serif blanca con borde negro fino (estándar de Disney, sin fuente pública documentada) · no se encontró una ficha técnica pública del tipo exacto → anotado en «No encontré» ⚠️.

### Punto 11 — Videojuegos de la franquicia

Coco no tuvo un videojuego propio dedicado (a diferencia de Cars o Toy Story); aparece como contenido dentro de juegos móviles/servicio de Disney, y **desde ago-2026 se anunció en Kingdom Hearts IV**.

- **Disney Magic Kingdoms** (móvil, gacha de construcción) — evento limitado «Coco» lanzado **15 oct 2019** («The Bride Update», parche 4.4.0), ambientado después de la película: personajes jugables **Miguel Rivera, Héctor Rivera, Dante, Abuelita, Mamá Coco, Ernesto de la Cruz y Mamá Imelda**; atracciones: Land of the Dead, Musical Celebration, Rivera Familia Home, Santa Cecilia Market Shop · fuente: TV Tropes «Characters/DisneyMagicKingdomsEventCharactersPartFour» **y** wikitext oficial de `dmk.fandom.com/wiki/Héctor_Rivera` (fecha de update, coste, bundle 2019/11/01) ✅ (dos fuentes)
- **Disney Heroes: Battle Mode** (móvil, RPG de combate, **cerrado el 31 may 2026**) — Miguel Rivera, personaje de rol **"Support"** (posición trasera, equipo Amarillo), habilidad "Crescendo": en vez de atacar pone Notas de curación sobre aliados y no puede ser hechizado; se desbloqueaba con 10 "Miguel Rivera Chips" · fuente: wikitext de `disneyheroesbattlemode.fandom.com/wiki/Miguel_Rivera` **y** búsqueda que confirma el cierre del juego (mayo 2026) ✅
- **Disney Speedstorm** (F2P de carreras, Gameloft) — **Temporada 22 "Bridge of Marigolds"**, lanzada **hoy mismo, 24-sep-2026**: nuevos corredores **Miguel Rivera** (Speedster, rareza Épica), **Héctor Rivera** (Trickster, Rara) y **Ernesto de la Cruz** (Brawler, Común); pista nueva ambientada en la Tierra de los Muertos; eventos "Tale" por personaje (Miguel 30 sep-6 oct, Héctor 15-21 oct, Ernesto 5-11 nov) · fuente: parche oficial `disneyspeedstorm.com/news/disney-speedstorm-patch-notes-season-22` **y** cobertura en GoNintendo ✅ (dos fuentes, la más reciente de todo el dossier)
- **Kingdom Hearts IV** (Square Enix, ventana **finales de 2027**) — en el D23 de agosto 2026 se reveló que el **mundo de Coco** llega al juego: Sora combate Heartless junto a **Miguel y Héctor** en la Tierra de los Muertos durante el Día de Muertos; Miguel y Héctor confirmados como miembros del grupo de Sora en ese mundo · fuente: Game Informer («Kingdom Hearts IV Gets 2027 Launch Window, Coco World Reveal») **y** cuenta oficial de Pixar en X («the world of Coco will be coming to KINGDOM HEARTS IV, launching in late 2027») ✅ — dato "si aplica" del encargo: **sí aplica**, es una revelación muy reciente.
- **No encontrado / no aplica**: sin juego propio de consola/PC dedicado a Coco (ni de Avalanche, Behaviour ni Disney Interactive); sin presencia confirmada en Disney Dreamlight Valley (búsqueda específica no encontró realm de Coco, sólo Alice in Wonderland y otros anunciados) ⚠️; no se encontró página de Coco en **The Cutting Room Floor** (TCRF) — buscado directamente en tcrf.net, sin resultados, coherente con que no hay un juego "propio" que minar.

### Punto 18 — Estilo de dibujo/técnica y cómo replicarlo

(pendiente)

### Punto 24 — Obras parecidas

(pendiente)

### Punto 25 — El mundo, la historia y sus símbolos

(pendiente)

## Lo mejor para la lámina

(pendiente)

## No encontré

(pendiente)

## Bitácora

(pendiente)

Sigue: empezar por punto 5 (tipografía del logo y rótulos).
