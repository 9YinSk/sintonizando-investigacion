# Parte del investigador de TEXTO, JUEGOS Y TÉCNICA · Jujutsu Kaisen

Repaso corto (24-sep-2026): la biblia ya tiene los puntos 5, 6 y 11 de
`ENCARGO.md` (tipografía, cómo hablan en pantalla, videojuegos). Este
archivo cubre **sólo los 3 puntos nuevos, que no están en la biblia**:
**18** (estilo de dibujo y técnica, y cómo replicarlo), **24** (obras
parecidas) y **25** (el mundo, la historia y sus símbolos). Parte de
`partes/datos-texto.md` (AniList, staff, Steam) sin repetir sus consultas.

## Hallazgos

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Software y técnica del estudio (MAPPA)**

- MAPPA usa una mezcla de dibujo 2D y CG 3D, "sin que se note cuál es cuál" · [CGWORLD, seminario CGWORLD JAM Vol.3](https://cgworld.jp/feature/202108-cgwjam03-mappa.html) (ja) ✅ (confirmado también en el artículo de JJK0 abajo) · sin minuto (artículo)
- El director 3DCG de la serie es **Kentarō Kimura (木村謙太郎)** (también en el staff de `datos-texto.md`); en escenas de calle con multitud, **el primer plano se dibuja en 2D y el fondo se hace en 3D** para ahorrar trabajo de animadores · [CGWORLD](https://cgworld.jp/feature/202108-cgwjam03-mappa.html) (ja) ✅
- Para los bosques del arco de Kioto: modelos 3D completos con árboles, ajustados en cantidad y espaciado "según referencias artísticas para mantener coherencia visual" (Kimura) · misma fuente ⚠️ (una fuente, resumen del seminario)
- En la película **JJK 0**: la técnica **camera mapping** (proyectar el dibujo 2D sobre geometría 3D simplificada) para poder mover la cámara libremente sin perder el aspecto dibujado a mano. El objetivo declarado: "acercar la CGI al dibujo" ("作画に近づける") · [CGWORLD, JJK0 3DBG](https://cgworld.jp/article/202203-jujutsukaisen.html) (ja) ✅
  - Flujo de trabajo: layout 2D del animador → modelado base (estudio **Easter** hizo Kioto y Shinjuku) → proyección de la textura dibujada sobre el modelo → capas de sombra/luz añadidas **en After Effects** · misma fuente ✅
  - Software mencionado: **Blender** (para el layout 3D previo, hecho por los propios animadores de dibujo), **Maya** y herramientas internas (modelado/rigging), **After Effects** (composición) · misma fuente ✅
- Los espíritus malditos en 3D de JJK0 (el ciempiés y los peces) se hicieron en **3ds Max**, con **tyFlow** para las simulaciones de partículas de los peces; el ciempiés lo modelaron/riggearon en **Yostar Pictures** y lo animó **Larks Entertainment**, con "muchas repeticiones para acercar la animación al movimiento dibujado a mano" (Kimura) · [CGWORLD, JJK0 3D呪霊篇](https://cgworld.jp/article/202203-jujutsukaisen02.html) (ja) ✅
- Diseño de personajes y dirección de animación: **Tadashi Hiramatsu (平松禎史)** (T1 y T2); en la T2 se sumó **Sayaka Koiso**, y el diseño se hizo "más moderno y flexible": menos líneas de músculo y menos arrugas de ropa que en la T1 · [Real Sound, sobre el cambio de staff en la T2](https://realsound.jp/movie/2023/07/post-1368255_2.html) (ja) ✅ (coincide con el punto siguiente)
- Cambio de estilo T1→T2: la T1 (dir. **Sunghoo Park**) tiene un "estilo gráfico pesado y robusto", líneas marcadas y sombreado detallado; la T2 (dir. **Shōta Gotō**) simplifica el diseño para poder animar más rápido las peleas de Shibuya, prioriza composición y sensación de movimiento con cámaras dinámicas · [noteapex.conohawing.com, análisis del cambio de artwork T1/T2](https://noteapex.conohawing.com/958/) (ja) ⚠️ (una fuente, blog de análisis, pero coincide con Real Sound en la simplificación) · el ep. 41 recibió "correcciones masivas" en el Blu-ray
- Software habitual de los estudios japoneses grandes (contexto, no específico de MAPPA en esta fuente): **RETAS** fue el estándar durante años (lo usaron estudios grandes como ufotable y MAPPA) y se sustituye cada vez más por **Clip Studio Paint EX**, que ya tiene funciones de producción de anime · [Wikipedia, «RETAS»](https://en.wikipedia.org/wiki/RETAS) ⚠️ y [CLIP STUDIO ASK, «CSP EX and animation industry»](https://ask.clip-studio.com/en-us/detail?id=57247) ⚠️ (contexto de industria, no cita a MAPPA por nombre) · **Toon Boom Harmony** y **After Effects** también se citan como parte habitual del stack de MAPPA · [Dark Skies Film, «Decoding MAPPA's Animation Arsenal»](https://darkskiesfilm.com/what-animation-software-does-mappa-use/) ⚠️ (una fuente, blog, sin citar entrevista directa del estudio)

**Encuadre y composición** (para «planos, ángulos y cómo se enmarca cada emoción»)

- La T1 se inspira en cine de acción en imagen real: comparaciones directas con *The Raid* y *John Wick* (planos de persecución, montaje) e *Inception* (ángulos imposibles); "el ángulo de la cabeza, la dirección de la luz, la distancia entre personajes" transmiten el significado sin diálogo · [Anime Lore Hub, «The Cinematic Camera Work of Jujutsu Kaisen»](https://animelorehub.blogspot.com/2025/10/when-frame-speaks-louder-than-words.html) ⚠️ (una fuente, blog, no cita entrevista directa)
- El montaje sigue el estado mental del personaje: cortes rápidos en pánico, zooms lentos en el duelo/tristeza; planos aéreos tipo dron para dar escala en batallas grandes · misma fuente ⚠️
- Ya confirmado por el propio director en coreano (ver §18 de la biblia, `biblia.md` l. 1442-1449): Sunghoo Park probó "distintas formas desde el storyboard" para que "el miedo se sienta real" · [Xportsnews](https://www.xportsnews.com/article/1540502) (ko) — cita ya en la biblia, no se repite aquí.

**Cómo replicarlo en Photoshop** (capas y pinceles concretos)

- Flujo estándar de *cel shading* aplicable al estilo de JJK (línea fina + sombra de dos tonos con borde duro, ya medido en la biblia §18): 1) línea/boceto limpio en su propia capa, 2) **colores planos** rellenados con el cubo o lazo y "Lock Transparent Pixels" activado para no salirse del contorno, 3) capa de sombra en **modo Multiply** (no gradientes: formas sólidas, pensando en planos como la parte de abajo de la barbilla o el lado opuesto a la luz), 4) *drop shadow* para las zonas más oscuras · [Adobe, «Cel Shading — A Comprehensive Expert Guide»](https://www.adobe.com/uk/creativecloud/animation/discover/cel-shading.html) ✅ (fuente oficial de Adobe) + [Concept Art Empire, tutoriales de cel shading](https://conceptartempire.com/cel-shading-tutorials/) ⚠️ (lista de vídeos, no un paso a paso propio)
- Para el grano y el brillo/aberración cromática del anime: se añaden como **capas de ajuste encima de todo** (ruido monocromo a baja opacidad para el grano; un desenfoque + desplazamiento de los canales R/B para la aberración cromática; una capa Screen u Overlay suave para el brillo de contraluces) — técnica estándar de posproducción de vídeo, no específica de JJK; ⚠️ sin una fuente que la aplique a JJK en concreto, se deja como método general.
- Herramienta específica de Clip Studio para *cel shading*: pincel de tinta + capa de "Tono" (screentone) automático para tramas; guía paso a paso con capturas · [CLIP STUDIO TIPS, «Tips for Cel Shading» de LizStaley](https://tips.clip-studio.com/en-us/articles/10901) ⚠️ (una fuente, tutorial genérico de la comunidad, no específico de JJK)

**Cómo replicarlo en Blender** (contorno, rigs libres, texturas)

- Contorno de línea en Blender: dos caminos que cita el propio `ENCARGO.md` y que confirman los tutoriales — **Line Art** (modificador de grease pencil que traza el contorno desde geometría 3D, integrado en Blender 2.93+) o el método clásico con una segunda malla con shader de **Emission** + **Backface Culling** + modificador **Solidify** hacia fuera para el trazo (o **Freestyle**, el motor de render por líneas de Blender) · [Blender Artists, «The Ultimate Cel-Shading Shader»](https://blenderartists.org/t/the-ultimate-cel-shading-shader/1413344) ✅ (hilo técnico con capturas) + confirmado en un tutorial rápido de YouTube · [«How to make an Anime Cell Shader in 2 MINUTES in Blender»](https://www.youtube.com/watch?v=LJJkCI5u7Rw) ✅
- Shader de sombreado plano: nodo **Diffuse BSDF → Shader to RGB → ColorRamp** con el modo del ColorRamp puesto en **Constant** (no Linear) para que el degradado se corte en dos tonos duros, igual que la sombra de dos tonos medida en la biblia (§18) · [Blender Artists](https://blenderartists.org/t/the-ultimate-cel-shading-shader/1413344) ✅
- **Fan art 3D de la propia serie hecho en Blender**, útil como referencia de estilo (no para calcar): animación fan de **Sukuna vs. Mahoraga** por el animador **FrameFiend** (canal de YouTube @FrameFiend), con el complemento **Autosmear** para los *smears* (estelas de movimiento) con color y *mesh trails*, imitando el dibujo a mano de las peleas rápidas · [80 Level, «JJK's Sukuna vs Mahoraga Fan Animation in Blender»](https://80.lv/articles/jjk-s-sukuna-vs-mahoraga-fan-animation-in-blender) ✅
- **Modelo/rig gratuito de referencia de estilo**: el artista 3D **DAL** hizo una recreación de **Yuta Okkotsu** con shading anime en Blender y publicó el desglose técnico (Patreon/Gumroad, de pago) · [80 Level, «Artist Shares a Tutorial on Shading Anime-Style Character Model»](https://80.lv/articles/artist-shares-tips-on-shading-anime-style-character-model) ⚠️ (confirma que el tutorial existe, pero los pasos detallados están detrás del muro de pago; no se pudo verificar el contenido completo)
- Guía de dibujo de cara (aplica igual al boceto base antes de pasar a 3D o al *line art* en Photoshop): 12 pasos para la cara de Yuta Okkotsu, con código de color (rojo = paso actual, negro = líneas ya hechas, gris = boceto base); ojos grandes y redondos, cejas finas algo arqueadas, barbilla puntiaguda suave · [Sketchok, «Yuta Okkotsu Face Drawing Tutorial – JJK Style in 12 Steps»](https://sketchok.com/anime/jujutsu-kaisen/yuta-okkotsu-face-drawing-tutorial-jjk-style-in-12-steps/) ⚠️ (una fuente, tutorial de fan)
- Para el contorno de la wiki de animación japonesa sobre Hiramatsu y el estilo de JJK (ficha con enlaces a cortes de animación por escena, útil para comparar «quién dibujó qué»): [作画@wiki, «平松禎史»](https://w.atwiki.jp/sakuga/pages/213.html) (ja) ⚠️ (wiki editada por fans del *sakuga*, sin firma; consultada como índice, no como cita textual)

### Punto 24 · Obras parecidas y temas relacionados

(pendiente)

### Punto 25 · El mundo, la historia y sus símbolos

(pendiente)

## Lo mejor para la lámina

(pendiente)

## No encontré

(pendiente)

## Bitácora

(pendiente)

Sigue: falta todo (18, 24, 25). Empezando por 18 (técnica y cómo replicarlo).
