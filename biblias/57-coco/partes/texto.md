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

(pendiente)

### Punto 11 — Videojuegos de la franquicia

(pendiente)

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
