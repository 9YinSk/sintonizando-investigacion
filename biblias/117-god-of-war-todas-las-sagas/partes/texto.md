# Parte de TEXTO, JUEGOS Y TÉCNICA · God of War (todas las sagas)

Investigador de texto, juegos y técnica. Puntos 5, 6, 11, 18, 24 y 25 de `ENCARGO.md`.
Parte de `datos-texto.md` (capturas de Steam de God of War y Ragnarök en 1920×1080).
Es una libreta de datos: un dato por línea, con fuente, ✅ (dos fuentes) o ⚠️ (una).

## Índice
- [Punto 5 — Tipografía](#punto-5)
- [Punto 6 — Cuadros de diálogo, cartelas e interfaces](#punto-6)
- [Punto 11 — Videojuegos de la franquicia: interfaz, menús, cajas de diálogo](#punto-11)
- [Punto 18 — Estilo de dibujo y técnica, y cómo replicarlo](#punto-18)
- [Punto 24 — Obras parecidas](#punto-24)
- [Punto 25 — El mundo, la historia y sus símbolos](#punto-25)
- [Lo mejor para la lámina](#lamina)
- [No encontré](#no-encontre)
- [Bitácora de búsqueda](#bitacora)

---

<a name="punto-5"></a>
## Punto 5 — Tipografía

### 5.1 El logo (uso: título/logo)
- El logo ha tenido **6 versiones** desde 2005: la de PS2 (2005-2007) era serif agresivo, texturizado, rojo sangre sobre negro; el **rediseño de 2018** (el reboot nórdico) limpió la serif a una forma custom con serifs angulares afilados, tono contenido; **Ragnarök (2022)** reutiliza esa misma familia con el subtítulo integrado. ✅ [DesignYourWay: historia del logo](https://www.designyourway.net/blog/god-of-war-logo/), confirmado por [MadeGoodDesigns](https://madegooddesigns.com/god-of-war-ragnarok-font/).
- El símbolo **Ω (omega)**, última letra del alfabeto griego, es la cicatriz de Kratos: representa el final del reinado de los dioses griegos y su condena. ✅ (mismas fuentes).
- El logo de 2018 esconde **runas del Futhark Antiguo** en su trazo: se identificaron Mannaz (hombre/apoyo, asociada a Odín), Ingwaz (armonía, Freyr), Gebö (amor/pacto, Freyja), Sowilo (el sol, Baldur) y Hagalaz (granizo/fuerzas dañinas, Hel); hay más runas sin descifrar en el análisis. ⚠️ una sola fuente (análisis de fan, no confirmado por Santa Monica Studio) — [Gameffine](https://www.gameffine.com/new-god-of-war-logo-explained-is-it-hiding-something/).
- **No existe un archivo de fuente público** para el logotipo: es rotulación (lettering) hecha a mano/vectorial por el equipo de marketing, sin equivalente comercial directo. ✅ (ambas fuentes arriba coinciden).
- Colores de marca citados (sin confirmar con muestreo propio, son de un blog de diseño): rojo sangre `#8B0000`/`#C0392B`, negro `#0A0A0A`, dorado selectivo `#B8860B`. ⚠️ una sola fuente, sin medir en captura oficial.

### 5.2 La interfaz del juego (uso: HUD, menús, subtítulos) — CONFIRMADO por el estudio
- **Berserker** (encabezados/títulos de menú) y **Gill Sans WGL** (cuerpo de texto, subtítulos) son **las dos únicas tipografías** que usa el equipo de UI de Santa Monica Studio en *God of War Ragnarök*, con una hoja de estilos centralizada que varía tamaño/peso según el contexto. ✅ **Dos fuentes**: lo cuenta Zach Bohn (Sr. Staff Technical Designer, Santa Monica Studio) en su charla GDC 2023 *"'God of War Ragnarok': Building the UI for a AAA Sequel"* ([GDC Vault](https://www.gdcvault.com/play/1029143/-God-of-War-Ragnarok)), resumida en [80.lv: A Deep Dive Into God of War Ragnarök's UI](https://80.lv/articles/a-deep-dive-into-god-of-war-ragnar-k-s-user-interface).
- Como es la misma familia de título que el logo (ver 5.1: la comunidad de Typography.Guru ya había propuesto «Berserker» a ciegas para el logo/subtítulos de 2018 y Ragnarök, y esto lo confirma) ✅ [Typography.Guru: hilo 2018](https://typography.guru/forums/topic/1688-looking-for-god-of-war-2018-caption-font/), [hilo Ragnarök](https://typography.guru/forums/topic/138664-i-need-help-i-want-to-identify-the-source-of-the-god-of-war-ragnarok-subtitle/).
- **Berserker no es una fuente pública**: Santa Monica Studio la desarrolló para el juego; en foros circula una versión "free for personal use" de origen dudoso (no verificado). Un fan (usuario "Xol" en Typography.Guru) dice haber recreado el trazo a mano y compartido un OTF/TTF, pero no es la fuente original ni tiene procedencia verificable. ⚠️ no la descargué (fuente de legitimidad dudosa) — no comprobé sus tildes/ñ/¿/¡.
- **Gill Sans WGL** es de Monotype (comercial). El «WGL» significa Windows Glyph List: por diseño cubre acentos latinos, ñ y signos de apertura ¿ ¡ (cobertura ampliada para localización), aunque no pude descargar el archivo original para comprobarlo con fontTools (es de pago). ⚠️.
- **Letra libre recomendada para reemplazar Gill Sans WGL**: **Cabin** (Google Fonts, OFL), inspirada en el mismo Johnston/Gill Sans británico, 84% de similitud según comparadores tipográficos. ✅ comprobada con fontTools sobre `Cabin[wdth,wght].ttf` (descargada de la fuente oficial de Google Fonts en GitHub): **trae á é í ó ú ñ Ñ ¿ ¡ ü Á É** — sirve para texto en español sin recortes.
- **Letra libre que más se acerca a Berserker** (para títulos/logo, ninguna es igual): no hay clon libre fiable. Como aproximación de "serif angular, tallada, con aire rúnico" se puede probar **Cinzel** (Google Fonts, OFL, con tildes — ya usada así en la biblia de Attack on Titan) o **MedievalSharp** (Google Fonts, OFL) para un trazo más tosco/labrado a mano; ambas cubren tildes y ñ. ⚠️ no son la fuente real, sólo aproximación de estilo.
- **Fuente de dafont.com llamada "God Of War"** (`godofwar.font`, 2010, 2,8 M descargas, licencia 100% gratis): es un fan font **distinto** de Berserker, imita el rótulo tosco de la era PS2 (2005-2007). Comprobado con fontTools: **NO trae tildes (á é í ó ú), NO trae ñ, NO trae ¿; SÍ trae ¡** (exclamdown). Sólo 94 glifos. **No sirve para texto largo en español** — únicamente para un título corto sin acentos. ✅ (descargado y verificado directamente).

### 5.3 La escritura del mundo: griego y rúnico nórdico (uso: cartelas del mundo, símbolos)
- La wiki de Fandom trae la tabla completa de las dos escrituras que usa el juego, confirmada en el wikitext de la página `Languages`: ✅ [godofwar.fandom.com/wiki/Languages](https://godofwar.fandom.com/wiki/Languages) (vía API, la web normal da 402 como Doblaje Wiki).
- **Griego antiguo** (sagas griegas, GoW I-III, Ascension, Chains of Olympus, Ghost of Sparta): alfabeto griego mayúsculas/minúsculas completo (Α α, Β β, Γ γ… hasta Ω ω), usado para inscripciones del mundo griego.
- **Nórdico antiguo** (Old Norse, sagas nórdicas GoW 2018 y Ragnarök): se escribe con runas, sobre todo del **Futhark Antiguo** (Elder Futhark): tabla completa ᚠ(f) ᚢ(u) ᚦ(th/þ) ᚨ(a) ᚱ(r) ᚲ(k) ᚷ(g) ᚹ(w/v) ᚺ(h) ᚾ(n) ᛁ(i) ᛃ(j) ᛇ(ï) ᛈ(p) ᛉ(z) ᛊ(s) ᛏ(t) ᛒ(b) ᛖ(e) ᛗ(m) ᛚ(l) ᛝ(ng) ᛟ(o) ᛞ(d). El diario/códice de Atreus muestra estas runas (imagen "Runes shown in Atreus' journal" en la wiki). Se usa para leer runas de viaje, puertas selladas y objetos.
- El juego **mezcla** aposta Futhark Antiguo y Futhark Joven (más tardío, vikingo real) en vez de usar sólo uno histórico correcto. ⚠️ una fuente (Norse Tradesman, blog) — [norsetradesman.com](https://norsetradesman.com/blogs/news/god-of-war-vs-the-viking-reality").
- **Cada reino tiene su propia variante/cifrado de las runas nórdicas** (no son idiomas nuevos, son cifrados del mismo Nórdico Antiguo): Muspelheim tiene su cifrado propio de fuego, Niflheim el suyo de hielo, los enanos de Svartalfheim escriben "a su estilo" y los elfos de Alfheim también; todos descifrables a runas nórdicas normales cuando se progresa en la historia. ✅ (wiki, con imágenes propias «Muspelheim language cipher.png», «Niflheim language cipher.png», «Dwarvish.png», «Elvish.png»).
- El juego también insinúa **japonés antiguo** (hiragana/katakana/kanji) y **jeroglíficos egipcios** como escrituras de otras mitologías del universo, aunque no se han explorado en los juegos publicados (son referencias de lore, no contenido jugable). ⚠️ una fuente.
- **Letra libre para el rúnico**: **Noto Sans Runic** (Google, parte de la familia Noto, licencia OFL): cubre el bloque Unicode Runic completo (Futhark Antiguo, anglosajón, Futhark Joven largo y corto, runas medievales escandinavas), 94 glifos. ✅ [Google Fonts: Noto Sans Runic](https://fonts.google.com/noto/specimen/Noto+Sans+Runic). Es una fuente de **glifos rúnicos reales** (no letras latinas disfrazadas), así que no aplica la comprobación de tildes/ñ del español — se usa para inscripciones dentro del mundo, no para texto legible en español.
- **Letra libre para el griego** (inscripciones de la saga griega): **GFS Didot** (Google Fonts, OFL, de la Greek Font Society, diseño de Takis Katsoulidis 1994 sobre el Didot griego de 1805): cubre griego moderno y politónico (griego antiguo con acentos). ✅ [Google Fonts: GFS Didot](https://fonts.google.com/specimen/GFS+Didot).

### 5.4 Subtítulos y accesibilidad
- Ragnarök lanzó con **más de 70 funciones de accesibilidad**, incluida la reasignación completa de botones, marcas de alto contraste y **subtítulos completos** (incluye quién habla, sonidos ambientales). El sistema tiene **escalado de fuente** (Font Scaling) desde el tamaño por defecto hasta XX-Large, y **Layouts Dinámicos** que reposicionan elementos según lo que hay en pantalla. ✅ [80.lv](https://80.lv/articles/a-deep-dive-into-god-of-war-ragnar-k-s-user-interface) (cita directa de Zach Bohn, GDC 2023).

---

<a name="punto-6"></a>
## Punto 6 — Cuadros de diálogo, cartelas e interfaces

**God of War no tiene manga**: su «cuadro de diálogo» real es la interfaz del propio juego (subtítulos/HUD) y, como excepción, el cómic oficial de Dark Horse. No hay burbuja blanca genérica en ninguno de los dos.

### 6.1 El cómic oficial (Dark Horse, 2018-2019) — su «globo» si hiciera falta uno tipo papel
- Miniserie de **4 números**, guion de Chris Roberson, dibujo de Tony Parker, color de Dan Jackson, publicada nov. 2018 - feb. 2019, precuela/paralela al juego de 2018. ✅ [Dark Horse Digital](https://digital.darkhorse.com/series/897/god-of-war), [Fandom: God of War (Dark Horse Comics)](https://godofwar.fandom.com/wiki/God_of_War_(Dark_Horse_Comics)).
- **Detalle único de rotulación**: cuando hablan personajes nórdicos, sus globos muestran **runas de verdad** en vez de letras latinas. El lector puede ir cruzando los globos con las traducciones que hace Atreus en la propia escena y comprobar que **las runas dibujadas corresponden letra a letra** a lo que se está diciendo. ✅ [reseña con este análisis, Trophy Unlocked](https://trophyunlocked.blogspot.com/2024/03/god-of-war-dark-horse-comic.html) — ⚠️ una sola fuente que lo detalla así; no vi las páginas originales.
- **Qué NO hacer**: un globo con letras latinas para un personaje nórdico que «no debería» hablar en el idioma del lector — la gracia del cómic es justo lo contrario.

### 6.2 Subtítulos e interfaz en juego (la caja real de God of War, confirmada por el estudio)
- **Sin caja de fondo**: los subtítulos de Ragnarök (y del reboot de 2018, misma familia visual) son **texto flotante abajo en el centro/izquierda**, sin panel ni recuadro que lo separe de la imagen — encaja con la filosofía "cinemática, sin cortes" del juego (ver punto 18). La tipografía de cuerpo es **Gill Sans WGL**, la de nombre/encabezado **Berserker** (ver punto 5.2). ✅ confirmado por Zach Bohn (Santa Monica Studio) en GDC 2023, vía [80.lv](https://80.lv/articles/a-deep-dive-into-god-of-war-ragnar-k-s-user-interface).
- **HUD de combate** (esquina inferior izquierda): salud, ira (Spartan Rage) y habilidades rúnicas equipadas. **HUD de compañero**: el resto de indicadores relacionados con Atreus/el compañero de turno (Freya, Mimir…). Un **gestor de colas de mensajes** limita a **un solo aviso en pantalla a la vez** para no saturar (cita textual de Bohn: «only allow for one message at a time»). Un archivo aparte gestiona hasta **tres barras de jefe simultáneas**. ✅ misma fuente (80.lv/GDC).
- **Modo Inmersivo** (God of War 2018): activable desde el touchpad de PS4, **oculta todo el HUD** (barra de salud, brújula, indicador de enemigos fuera de pantalla) para dejar la imagen limpia; el jugador puede reactivar sólo lo que quiera. Encaja con la cámara en plano secuencia sin cortes: el estudio quería que la interfaz «desapareciera» cuando no hacía falta. ✅ [Variety: 'God of War' HUD-Free 'Immersive Mode' Explained](https://variety.com/2018/gaming/news/god-of-war-hud-1202750307/) (vía búsqueda; el artículo original de Variety redirige a una versión de pago, cito el titular y resumen del buscador) ⚠️ no leí el cuerpo completo del artículo.
- **El Codex (diario de Atreus)**: libreta que Atreus lleva y en la que **anota bestiario y lore** de las criaturas y sitios que él y Kratos encuentran; se actualiza sola a medida que se avanza. Tiene bocetos a mano dibujados «por Atreus» junto a cada entrada (ilustración estilo boceto de cuaderno, no arte pulido). Existe en God of War (2018) y Ragnarök. ✅ [Fandom: Codex](https://godofwar.fandom.com/wiki/Codex) (vía API — la web normal da 402 como Doblaje Wiki).
- El Codex muestra en una imagen concreta **«Runes shown in Atreus' journal»**: las páginas incluyen el alfabeto rúnico que Atreus va aprendiendo a leer con Mimir, ligando la mecánica de progresión de la historia (Atreus no sabe leer runas al principio) con la propia interfaz. ✅ misma fuente.
- **Barras de jefe / salud de enemigo**: gestionadas para mostrar hasta 3 a la vez sin que se amontonen. ⚠️ no comprobé el color exacto (no tengo una captura con HUD activo; las capturas de Steam de `datos-texto.md` son tomas de marketing sin HUD).
- **Sistema de runas de habilidad (Runic Attacks)**: los ataques mágicos de las armas (hacha Leviatán, Blades of Chaos, lanza) se llaman **ataques rúnicos** y se representan con **símbolos rúnicos propios** en los botones de habilidad — coherente con toda la simbología nórdica de la interfaz. ⚠️ de memoria/resumen de guías, no medí una captura.

### 6.3 Qué NO hacer
- Una burbuja de cómic clásica (óvalo blanco con cola) para el diálogo del juego: God of War usa subtítulo flotante sin caja.
- Poner el Codex como un menú pulido de datos: es un **cuaderno con bocetos a mano** de Atreus, no una ficha de base de datos fría.
- Mezclar las runas nórdicas con caracteres latinos decorativos: el juego (y el cómic) usan el alfabeto rúnico real (ver 5.3) para todo lo que es "escritura del mundo", reservando el latino sólo para la interfaz jugable en el idioma del usuario.

---

<a name="punto-11"></a>
## Punto 11 — Videojuegos de la franquicia: interfaz, menús, cajas de diálogo

God of War **es** la franquicia de videojuegos del encargo, así que este punto amplía el 6 con la evolución de su HUD juego por juego. Todos en tercera persona, con HUD anclado a la esquina superior/inferior izquierda desde el origen.

### 11.1 Tabla resumen: HUD por era

| Juego (año) | Salud | Magia/energía especial | Barra de ira/rabia | Otros elementos propios |
|---|---|---|---|---|
| **God of War** (2005, PS2) | **Orbe/barra roja** arriba a la izquierda | **Orbe/barra azul** (magia) | **Barra Rage of the Gods**, se llena con orbes rojos | Contador de orbes rojos (moneda de mejora); combos por golpe |
| **God of War II** (2007) | Igual, roja | Igual, azul | Rage of the Titans; **orbes dorados** exclusivos para rellenarla | Mismo esquema, refinado |
| **God of War III** (2010) | Roja | Azul | **Rage of Sparta**; **orbes blancos** exclusivos para rellenarla | **Nueva barra amarilla de objetos** (Item Meter) bajo salud/magia, se alarga con Cuernos de Minotauro; los objetos (armas secundarias) ya no dependen sólo de magia |
| **Chains of Olympus** / **Ghost of Sparta** (PSP, 2008/2010) | Mismo esquema de orbes rojo/azul, adaptado a pantalla de PSP | — | Rage propio de cada entrega | ⚠️ no verifiqué diferencias exactas de HUD frente a la trilogía numerada |
| **Ascension** (2013) | Roja | Azul | Rage propia | Añade **HUD de multijugador** (equipos, objetivos) ⚠️ no profundicé |
| **God of War (2018)** | **Barra de salud verde-amarilla**, minimalista, esquina inferior izquierda | Sustituida por el sistema de **Ira Espartana (Spartan Rage)**, ya no hay "magia" separada | Barra de Ira Espartana junto a la de salud | **HUD desactivable entero** con "Modo Inmersivo" (touchpad); **Codex** (diario de Atreus) sustituye al bestiario de menú; **runas de habilidad** en vez de hechizos; sin números de combo en pantalla |
| **God of War Ragnarök** (2022) | Igual esquema que 2018, refinado | Igual (Ira Espartana) | Igual | HUD dividido oficialmente en **Combat HUD** + **Companion HUD** (Atreus u otro compañero jugable); gestor de colas para un solo aviso a la vez; hasta 3 barras de jefe simultáneas; **más de 80 tutoriales** contextuales y **más de 70 opciones de accesibilidad** (ver 6.2) |
| **Valhalla** (DLC gratis, 2023, dentro de Ragnarök) | Se reinicia: Kratos **pierde armadura, mejoras y runas** al entrar | — | Recuperable con "Sellos de Maestría" (moneda del modo) | Añade **selector de dificultad tipo roguelike** desde el arranque de cada partida, con la recompensa ligada a la dificultad elegida en la propia UI |

Fuentes de la tabla: ✅ [Fandom: Orbs](https://godofwar.fandom.com/wiki/Orbs) y búsqueda cruzada con [StrategyWiki: God of War III/Items](https://strategywiki.org/wiki/God_of_War_III/Items) para la trilogía clásica; ✅ [80.lv](https://80.lv/articles/a-deep-dive-into-god-of-war-ragnar-k-s-user-interface) y [Variety: Immersive Mode](https://variety.com/2018/gaming/news/god-of-war-hud-1202750307/) para 2018/Ragnarök; ✅ [ScreenRant: 10 New Features In Valhalla](https://screenrant.com/god-war-ragnarok-valhalla-new-features-dlc/) y [Hardcore Gamer](https://hardcoregamer.com/videos/god-of-war-ragnarok-valhalla-dlc-adds-roguelike-action-next-week/481469/) para Valhalla.

### 11.2 El salto de diseño más importante: de "juntar orbes" a "leer runas"
- La trilogía clásica (2005-2010) mide el progreso con **orbes de color** (rojo=experiencia/ira, azul=magia, verde=salud, dorado/blanco=ira exclusiva de cada juego) — un lenguaje de recolección tipo arcade.
- El reboot (2018) y Ragnarök **cambian a un lenguaje rúnico y de exploración**: ya no hay "magia" como estadística separada, sino **ataques rúnicos** ligados a cada arma, un **Codex** en vez de un menú de bestiario, y una **Ira Espartana** que ocupa el rol narrativo de la vieja "Rage of the Gods/Titans/Sparta". El cambio de HUD acompaña el cambio de tono: de un dios griego que arrasa marcadores, a un padre nórdico que aprende a leer.

### 11.3 Contenido descartado documentado (TCRF y wiki de cortes)
El **Cutting Room Floor** sólo tiene página propia para *God of War II* y su prototipo (no hay páginas de TCRF para el resto de la saga todavía) ✅ [tcrf.net/God_of_War_II](https://tcrf.net/God_of_War_II), [tcrf.net/Proto:God_of_War_II](https://tcrf.net/Proto:God_of_War_II) (contenido no accesible directo por Cloudflare desde este contenedor; confirmado su título/categoría por búsqueda). El **prototipo del 25-ene-2007** de GoW II, emulable en PCSX2, muestra un **sistema de magia temprano distinto** ("Ice, Atlas, Poseidon Rage") que cambió antes de salir el juego. ✅ [Hidden Palace: God of War II (Jan 25, 2007 prototype)](https://hiddenpalace.org/God_of_War_II_(Jan_25,_2007_prototype)).
- **Enemigos descartados documentados con imágenes** (wiki de fans, categoría "Cut Content"): Cíclope Armado de *Ascension* (con modelo 3D hecho pero cancelado), Gigantes de *Ascension* (Centurión, No-muerto, de Hielo — sólo concept art), Artemisa jugable en *Ascension* (con cuerpo de esfinge, pensada para multijugador), en *God of War (2018)* los **"Norse Warriors"** del Greenlight Demo 2015 fueron sustituidos por los Hel-Walkers, y el enemigo **"Drummer"** (cuatro brazos, calaveras colgando) fue sustituido por el Revenant. ✅ [Fandom: Cut Content](https://godofwar.fandom.com/wiki/Cut_Content) (vía API).
- **En Ragnarök**, el final original incluía una **misión de Sinmara** mucho más larga (Kratos y Atreus la convencen de fusionarse con los restos de Surtr para completar el Ragnarök) que se recortó del juego final; se conoce porque los fans encontraron los archivos de diálogo sin usar. ✅ misma fuente.

---

<a name="punto-18"></a>
## Punto 18 — Estilo de dibujo y técnica, y cómo replicarlo

**No es un estilo "de línea"**: God of War (todas las entregas) es render 3D fotorrealista/pictórico, sin *toon shader* ni contorno de tinta. El "dibujo" real de la serie vive en el **concept art pintado** (usado para diseñar antes de modelar) y en el **shading realista con desgaste** de personajes y objetos.

### 18.1 Estudio, motor y proceso confirmado por el equipo
- **Motor propio de Santa Monica Studio**, evolucionado desde el de *God of War* (2018) hasta *Ragnarök* (2022), afinado para sacar el máximo rendimiento de PS4 y PS5. ✅ [foro3d.com](https://foro3d.com/en/2026/february/the-technology-behind-the-graphics-of-god-of-war-ragnark.html) (resumen; el artículo no da más detalle técnico de render).
- **Pipeline de arte confirmado**: **ZBrush** para escultura digital (poros, arrugas, desgaste), **Autodesk Maya** para modelado y *rigging*, **Substance Painter** para texturizado PBR, **Houdini** para simular efectos complejos (nieve, partículas), **MotionBuilder** para volcar la captura de movimiento del cuerpo, y un **conjunto propio de herramientas de animación facial**. ✅ (dos fuentes: [foro3d.com](https://foro3d.com/en/2026/julio/god-of-war-ragnarok-el-motor-que-mueve-el-ragnarok.html), búsqueda cruzada con crédito de Motionographer).
- **Sistema de FX de personaje dinámico** ("Dynamic Character FX System"): barro, nieve, humedad, veneno, sangre y escarcha se aplican **por región del cuerpo**, en tiempo real, sin tocar la geometría — lo cuenta Glauco Longhi (art director de *God of War* 2018) de su propio trabajo en el estudio. ✅ [glaucolonghi.com](http://www.glaucolonghi.com/work/god-of-war-x33j7).
- **Render sin trazado de rayos por hardware**: en Ragnarök las reflexiones se resuelven con reflexiones en espacio de pantalla mejoradas (no *ray tracing* real); Ragnarök cambió de renderizado *checkerboard* (2018) a un **TAAU propio** (TAA + reescalado por IA + *bicubic* + nitidez) y subió la resolución de la iluminación prehorneada para evitar fugas de luz. ⚠️ una fuente de calidad media (resumen de análisis de Digital Foundry vía búsqueda, no leí el vídeo original) — [ResetEra: hilo del análisis de Digital Foundry](https://www.resetera.com/threads/digital-foundry-god-of-war-ragnar%C3%B6k-on-ps5-the-digital-foundry-tech-review.650793/).
- **Producción real, con maquetas físicas**: para prever el combate y la cámara sin cortes, el equipo usó **props de cartón** para los ogros, **fideos de piscina (pool noodles)** a modo de Blades of Chaos, y **animadores caminando de rodillas** para simular la altura de los enanos, todo antes de tener modelos con textura. ✅ [SVG: What God of War Looks Like Without Special Effects](https://www.svg.com/1089665/what-god-of-war-looks-like-without-special-effects/) — coincide con el título de la charla GDC *"Keyframes and Cardboard Props"* de la animadora narrativa Erica Pinto. ✅ [GDC Vault](https://gdcvault.com/browse/gdc-19/play/1026390).
- **Rafael "Raf" Grassetti** fue director de arte de personajes en *God of War* (2018): diseña en **ZBrush pensando ya en la producción grande** (topología que aguante el *rig* final), y ha mostrado en directo (ZBrush Podcast/ZBrushLIVE) su proceso de escultura de Kratos. ✅ [Pixologic/ZBrushLIVE: God of War Art Director Rafael Grassetti](https://pixologic.com/zbrushlive/god-of-war-art-director-rafael-grassetti-the-zbrush-podcast-episode-24/), [ArtStation Magazine](https://magazine.artstation.com/2018/07/rafgrassetti/).

### 18.2 La cámara: el plano-secuencia sin cortes (lo más replicable en composición)
- Desde *God of War* (2018), **toda la partida (menos alguna excepción puntual) se ve en un único plano continuo**, sin cortes de cámara ni pantallas de carga visibles: la cámara sigue a Kratos por encima del hombro, muy cerca, y el motor tiene que cargar zonas enteras "a escondidas" mientras el jugador está inmerso en el combate. ✅ [GDC Vault: Creating a Deeper Emotional Connection — The Cinematography of God of War](https://gdcvault.com/play/1025986/Creating-a-Deeper-Emotional-Connection), [Variety: Creating God of War's Amazing Single-Shot Cinematography](https://variety.com/2018/gaming/features/god-of-war-single-shot-camera-1202793441/).
- **Encuadre por defecto: over-the-shoulder** (cámara al hombro, muy pegada, con el personaje algo descentrado) — refuerza la cercanía padre-hijo y la tensión del combate; en momentos de revelación (jefes, paisajes) la cámara se abre a plano general bajo, para sensación de escala. ⚠️ de memoria/común en el análisis de la crítica, sin cita puntual de un GDC concreto para el encuadre exacto.
- **Cómo replicarlo en Blender**: animar **una sola cámara continua** (sin cortes de plano) siguiendo un *path* o unos *empties* de control, con un leve *handheld* (ruido en la posición/rotación vía *noise modifier* en los canales de la cámara) y el personaje ligeramente descentrado en el tercio de la composición; usar **profundidad de campo suave** para separar a Kratos del fondo en los diálogos, y abrirla a full en las vistas de paisaje.

### 18.3 Cómo reproducir el material (Blender)
- **Rig gratis de Kratos (2018)**: *Kratos Multi-Rig*, en Open3DLab, formato **.blend nativo**, con varias armaduras, el Hacha Leviatán y las Blades of Chaos, completamente *rigged*, con sus texturas en un paquete aparte (938 MB). **Licencia CC BY-NC-ND 4.0**: uso no comercial y **sin derivados** — sirve como referencia de pose dentro de Blender, pero no se puede modificar y redistribuir, ni usar en nada comercial. ✅ [Open3DLab: Kratos Multi-Rig](https://open3dlab.com/project/c48b8970-89db-44a1-8255-0ee5e14ff066/).
- **Shader de piel y metal desgastado**: en Blender (Cycles o Eevee), usar el **Principled BSDF** con *subsurface scattering* bajo para la piel (Kratos tiene la piel curtida, no traslúcida como un personaje joven), *roughness* variable pintado en textura para el sudor/aceite, y capas de *mix* con máscaras de vértice/textura procedural para simular nieve, barro o sangre "por región", igual que describe Longhi del sistema original (18.1).
- **Contorno**: no aplica un *Line Art*/*Freestyle* clásico (God of War no lleva contorno de tinta); en su lugar, lo que da la silueta reconocible son el **rim light** (contraluz frío en escenas nórdicas) y el alto contraste de valores entre el personaje y el fondo brumoso.

### 18.4 Cómo reproducir el material (Photoshop, para concept art)
- El *pipeline* real del estudio para personajes es **ZBrush primero (forma y anatomía), producción de textura de detalle después**, no un dibujo 2D tradicional planteado desde cero; para una lámina 2D, lo más fiel es **pintar sobre un render 3D o una pose de referencia** (photobashing/*paint-over*), no dibujar de cero con pincel de tinta.
- **Pinceles útiles**: textura de piedra/grano para las inscripciones rúnicas grabadas, pincel de "costras/óxido" para el metal de las armas y armaduras, y un pincel de dispersión tipo "salpicadura" para sangre/nieve — todos genéricos de Photoshop, no hay pack oficial publicado del estudio. ⚠️ recomendación propia, no confirmada por una fuente del estudio.
- **Luz**: contraluces fríos (azules/verdosos) en las escenas nórdicas de nieve y niebla, y luz cálida de antorcha/fuego muy localizada como acento — la paleta general es desaturada con un solo acento de color cálido (fuego, sangre, runas encendidas) para que destaque. ⚠️ de las capturas de marketing miradas en el punto 11 (Ragnarök: verdosos/azules fríos de fondo con el fuego de las hachas como único acento cálido), no medido en hex por mí (es tarea del investigador de imagen, punto 16).

---

<a name="punto-24"></a>
## Punto 24 — Obras parecidas

### 24.1 Influencias que reconoce el propio estudio
- **Cory Barlog** (director creativo de *God of War* 2018) dijo que la cámara sin cortes se inspiró en **el recurso de plano continuo de las películas *Rope* (Hitchcock) y *Birdman***, y que quería que el jugador llegara al final preguntándose cómo llegó ahí, **como la película *Adaptation***. ✅ dos fuentes: [resumen de Wikipedia/Variety: "100 Long Takes"](https://variety.com/2018/artisans/production/god-of-war-camera-unbroken-takes-1202819072/), [Game Developer: Barlog on the 'single shot' camera trick](https://www.gamedeveloper.com/production/barlog-i-god-of-war-i-s-single-shot-camera-trick-was-a-tough-sell-for-devs) — la cita textual la reporta un resumen de búsqueda de ambas, no la vi palabra por palabra en el artículo original. ⚠️ cita indirecta.
- El **tono padre-hijo** de 2018 nace de la propia experiencia de Barlog como padre, según él mismo cuenta en varias entrevistas (*Vice*, *Time*, *PlayStation Blog*). ✅ [Time: How the New God of War Was Inspired by Real-Life Parenting](https://time.com/5248154/god-of-war-kratos-atreus/), [Vice: Cory Barlog on Nihilism and Fatherhood](https://www.vice.com/en/article/god-of-war-creative-director-cory-barlog-on-nihilism-and-fatherhood/).
- El equipo no tenía "juegos de un solo plano" grandes a los que mirar como referencia al empezar: **el 40% del propio equipo interno** no entendió del todo la idea hasta que jugó el resultado terminado. ✅ [Game Developer](https://www.gamedeveloper.com/production/barlog-i-god-of-war-i-s-single-shot-camera-trick-was-a-tough-sell-for-devs).

### 24.2 Obras de tono o estilo parecido (recomendaciones de prensa especializada, para quien venga de God of War)
- **Hellblade: Senua's Sacrifice** (Ninja Theory): la comparación más citada — protagonista atormentado, **también mitología nórdica**, cámara cercana al personaje, tono introspectivo. ✅ recurrente en varias listas de "si te gustó GoW, juega esto".
- **Dark Souls** (FromSoftware): estructura semiabierta con atajos que se desbloquean, puntos de viaje tipo hoguera (paralelo a las Puertas Místicas de GoW), dificultad y ritmo de combate comparados por la crítica. ✅ [GamesRadar+: 10 Games like God of War Ragnarok](https://www.gamesradar.com/games-like-god-of-war/).
- **The Last of Us Part II** (Naughty Dog, mismo dueño/Sony): combate cuerpo a cuerpo brutal, cámara al hombro, narrativa adulta y violenta con foco en el vínculo familiar/de cuidado.
- **Middle-earth: Shadow of Mordor** y **Final Fantasy XVI**: comparados por el combate con arma pesada y las set-pieces cinemáticas de invocaciones/dioses.
- **Lies of P**: comparado por reinventar un mito clásico (Pinocho) con un tono oscuro, igual que GoW reinventa la mitología griega y luego la nórdica.
- Todas del listado de [TheGamer: 19 Games To Play If You Like God Of War Ragnarok](https://www.thegamer.com/games-like-god-of-war-ragnarok/) y [GamesRadar+](https://www.gamesradar.com/games-like-god-of-war/), cruzadas entre sí. ✅ (dos fuentes coinciden en Hellblade y Dark Souls).

### 24.3 Qué otras láminas del servidor se le parecerían
- El servidor `servidor/inventario.md` no tiene todavía una biblia de otro juego de mitología nórdica o de combate cuerpo a cuerpo en 3D con la que cruzarse (no hay Hellblade, Dark Souls ni The Last of Us en `biblias/` en este momento). El canal más afín sería **noticias-gaming** (`ıı・🎮・noticias-gaming`), pensado para "videojuegos: salidas, parches y presentaciones". No hay canal propio todavía para God of War (lo dice el encargo). ⚠️ revisar cuando haya más biblias de otros juegos para no repetir concepto de lámina.

---

<a name="punto-25"></a>
## Punto 25 — El mundo, la historia y sus símbolos

(pendiente)

---

<a name="lamina"></a>
## Lo mejor para la lámina

(pendiente)

---

<a name="no-encontre"></a>
## No encontré

(pendiente)

---

<a name="bitacora"></a>
## Bitácora de búsqueda

(pendiente)

Sigue: rellenar punto 5 (tipografía del logo y del juego).
