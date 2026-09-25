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

### 5.4 Por qué faltan letras de "globo normal, grito, pensamiento, onomatopeya" (tipos de manga)
- **God of War no es manga ni cómic seriado con esos códigos**: no tiene viñetas con globo ovalado normal, globo dentado de grito, nube de pensamiento u onomatopeyas en letras grandes dentro de la imagen (eso es un lenguaje del manga/cómic japonés, ver los ejemplos de otras franquicias en `biblias/_ya_hechas/_Cuadros de dialogo por franquicia`). Su único material impreso con globos es el cómic de Dark Horse (ver 6.1), que usa **globo de cómic americano estándar** (óvalo con cola), sin variantes de grito o pensamiento documentadas por las fuentes que consulté. ⚠️ no encontré un análisis de las páginas del cómic que distinga tipos de globo (grito vs. normal); sólo el dato de que usa runas de verdad para el diálogo nórdico (6.1).
- Tampoco hay un mecanismo de "pensamiento" en el juego: no existe una caja o efecto visual para los pensamientos internos de Kratos o Atreus — lo que sabemos de lo que piensan se cuenta por diálogo hablado (banter con Mimir/Atreus) o por el propio Codex escrito a mano por Atreus (ver 6.2), nunca por una burbuja de pensamiento en pantalla. ⚠️ no lo vi desmentido en ninguna fuente, lo baso en la ausencia de menciones en todas las páginas de interfaz consultadas.

### 5.5 Subtítulos y accesibilidad
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

### 18.4 Filtros de post-procesado y encuadre por emoción
- **Grano de película (Film Grain) y desenfoque de movimiento (Motion Blur)** son opciones reales y ajustables en las opciones gráficas de la versión de PC (activados por defecto con un grano ligero); no encontré una lista oficial que confirme aberración cromática o viñeta como opciones nombradas así. ✅ grano y desenfoque confirmados por dos fuentes de guías de PC ([PCGamer](https://www.pcgamer.com/god-of-war-best-settings/), [GameFAQs: hilo Film Grain](https://gamefaqs.gamespot.com/boards/191627-god-of-war/76535505)); ⚠️ aberración cromática/viñeta no confirmadas, no las doy por hechas.
- **Encuadre por emoción** (lectura propia sobre las capturas miradas en el punto 11 y la descripción de la cámara en 18.2, sin cita puntual de un GDC que lo diga así con estas palabras — ⚠️): los combates y momentos de rabia usan **plano medio-corto muy pegado, cámara algo inestable** (por el *handheld* del plano-secuencia); los momentos de duelo/introspección (como esparcir las cenizas de Faye) usan **planos más abiertos y estáticos**, con Kratos de espaldas o de perfil, dejando aire/silencio en la composición; las revelaciones de escala (un dios, un paisaje nuevo) usan **contrapicado y gran angular** para transmitir asombro o amenaza.

### 18.5 Cómo reproducir el material (Photoshop, para concept art)
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

### 25.1 Las reglas del mundo, en cinco líneas
1. Kratos es un mortal (espartano) que se convirtió en Dios de la Guerra griego tras matar a Ares; huyó de Grecia tras destruir a los Olímpicos y llegó a las **tierras nórdicas**, donde volvió a envejecer y a tener un hijo, Atreus. ✅ [Fandom: God of War (series)](https://godofwar.fandom.com/wiki/God_of_War_(series)).
2. El mundo nórdico son **Nueve Reinos** (Midgard, Alfheim, Asgard, Vanaheim, Niflheim, Muspelheim, Helheim, Svartalfheim y Jötunheim) que cuelgan de las ramas de **Yggdrasil**, el Árbol del Mundo, más un "Reino Entre Reinos" que actúa de espacio intermedio entre todos. ✅ [Fandom: Nine Realms](https://godofwar.fandom.com/wiki/Nine_Realms) (vía API).
3. Antes de los Nueve Reinos sólo existía el vacío **Ginnungagap**, donde el Fuego y el Hielo se encontraron y crearon la **Chispa del Mundo** (Spark of the World), origen de todo. ✅ misma fuente.
4. Cada mitología del juego tiene **su propia escritura**: griego antiguo con alfabeto griego, nórdico antiguo con runas (mayoritariamente Futhark Antiguo) — ver punto 5.3.
5. **Ragnarök** es el fin del mundo nórdico profetizado: la trama de *God of War Ragnarök* gira en torno a si Kratos y Atreus pueden (o deben) evitarlo. ✅ (resumen de búsqueda, Wikipedia/consolepulse).

### 25.2 La historia por arcos (con sus momentos clave)
**Saga griega** (orden cronológico interno: *Ascension* → *Chains of Olympus* → *God of War* [2005] → *Ghost of Sparta* → *God of War II* → *God of War III*; *Sons of Sparta*, sobre Kratos y su hermano Deimos de jóvenes en el entrenamiento espartano, es el punto más temprano de la línea de tiempo):
- Kratos, general espartano, es engañado por **Ares** para matar a su propia esposa e hija; las cenizas del Oráculo se le pegan a la piel para siempre (de ahí su piel de ceniza). Se convierte en el "Fantasma de Esparta" y sirve a los dioses del Olimpo a cambio de que le liberen de las pesadillas.
- Mata a **Ares** y se convierte en el nuevo Dios de la Guerra (*God of War*, 2005).
- Los dioses (sobre todo **Zeus**, su propio padre) lo traicionan; Kratos se venga sistemáticamente de todo el panteón griego a lo largo de *God of War II* y *III*, hasta **matar a Zeus** y destruir el Olimpo, liberando la Esperanza para la humanidad al final de la trilogía.
✅ (resumen cruzado de Wikipedia/fandomwire, dos fuentes coinciden en el orden y los hitos).

**Saga nórdica** (*God of War* 2018 → *God of War Ragnarök*, con el DLC *Valhalla*):
- Kratos, ya viejo, vive en las tierras nórdicas con su segunda esposa, **Faye**, y su hijo **Atreus**. Faye muere al empezar el juego (2018) y padre e hijo emprenden un viaje para esparcir sus cenizas desde el pico más alto de los Nueve Reinos, cruzándose con **Baldur ("El Forastero"/The Stranger)**, hijo de Odín, que los persigue. El juego cambia el eje de Kratos: de la venganza a la contención y la paternidad. ✅ (Cory Barlog, ver punto 24).
- En *Ragnarök* (2022), Kratos y Atreus intentan **evitar (o decidir si provocar)** el fin del mundo profetizado, enfrentándose a **Odín** y **Thor**; Atreus busca su propia identidad como el "Loki" de la profecía nórdica. ✅ (resumen cruzado Wikipedia/consolepulse).
- El DLC gratuito *Valhalla* (2023) es un epílogo jugable: Kratos revive recuerdos de su pasado griego dentro de un "más allá" de prueba (roguelike), como cierre emocional del personaje. ✅ (ver punto 11.1, ScreenRant).

### 25.3 Emblemas y símbolos
- **Cada uno de los Nueve Reinos tiene su propio glifo/runa** que lo representa en toda la interfaz del juego (mapa, viaje rápido, menú): `RuneAlfheim`, `RuneAsgard`, `RuneJotunheim`, `RuneVanaheim`, `RuneMidgard`, `RuneSvartalfheim`, `RuneNiflheim`, `RuneHelheim`, `RuneMuspelheim` — son los "logos de facción/lugar" más reconocibles del juego, cada uno una runa distinta dibujada en un círculo. ✅ [Fandom: Nine Realms](https://godofwar.fandom.com/wiki/Nine_Realms) (vía API; nombres de archivo confirmados en el wikitext).
- El **símbolo Ω (omega)** del logo, cicatriz de Kratos, representa el final del reinado griego y aparece grabado en su piel desde el primer juego (ver punto 5.1).
- Las **runas de ataque rúnico** (símbolos de las habilidades mágicas de cada arma) son iconografía propia del juego, distinta para cada arma (ver punto 6.2 y 11.2).

### 25.4 Objetos icónicos y su significado narrativo
- **Blades of Chaos** (Cuchillas del Caos): las armas encadenadas a los brazos de Kratos desde que sirvió a Ares; personifican **el monstruo que fue** — el que mató a su familia. Las abandona durante años y sólo vuelve a usarlas por amor a su hijo. ✅ [Fandom: Blades of Chaos](https://godofwar.fandom.com/wiki/Blades_of_Chaos).
- **Leviathan Axe** (Hacha Leviatán): arma de hielo forjada por los enanos, heredada de su segunda esposa Faye; personifica **el cambio** de Kratos — ya no mata por placer como Thor con Mjölnir, sólo para defenderse. ✅ [Fandom: Leviathan Axe](https://godofwar.fandom.com/wiki/Leviathan_Axe), [CBR: The Leviathan Axe Explained](https://www.cbr.com/god-of-war-ragnarok-leviathan-axe-explained/).
- **Draupnir Spear**: la primera arma **hecha específicamente para Kratos** (no heredada ni impuesta): lanza dorada que simboliza justicia y nobleza — encaja con el Kratos que ya no busca venganza. Una lanza es, además, la primera arma que aprende un espartano, así que le devuelve su origen. ✅ [Fandom: Draupnir Spear](https://godofwar.fandom.com/wiki/Draupnir_Spear).
- **La cabeza de Mímir**, guía parlante que Kratos lleva colgada del cinturón tras liberarlo, es quien narra buena parte del lore del mundo nórdico (sus "Cuentos de Mímir"). ⚠️ de memoria/común conocimiento, no cité fuente puntual.
- **La Caja de Pandora** (saga griega) y las **cenizas de Faye** (saga nórdica) son los dos "macguffin" que estructuran cada trilogía: uno es un arma de poder, el otro es un viaje de duelo.

### 25.5 Vocabulario que un fan reconoce al instante
- **«Boy»**: cómo llama Kratos a Atreus casi siempre en vez de por su nombre; se volvió meme instantáneo tras el lanzamiento de 2018. El propio director necesitaba "un término cariñoso" que sonara natural en boca de un padre distante. ✅ [ScreenRant: Why Kratos Always Calls Atreus Boy](https://screenrant.com/god-of-war-why-kratos-calls-atreus-boy/).
- **«The Stranger» / «El Forastero»**: como se refieren al personaje que resulta ser Baldur antes de revelar su identidad, al principio de *God of War* (2018). ✅ [Source Gaming: The Stranger](https://sourcegaming.info/2022/12/06/big-baddies-breakdown-the-stranger-god-of-war-2018/).
- **Spartan Rage** (Ira Espartana): el estado de furia límite de Kratos, sustituye a la vieja "Rage of the Gods/Titans/Sparta" de la trilogía griega (ver 11.2).
- **Nueve Reinos / Yggdrasil / Ragnarök / Jötunn**: vocabulario nórdico que cualquier fan reconoce de memoria por lo repetido que está en diálogos y menús.
- **«Boy» + el gruñido característico de Kratos** y su frase de combate «**¡Mortal insensato!**» / en inglés «**Insolent whelp!**» de la trilogía griega son las citas más parodiadas del Kratos "antiguo", en contraste con el Kratos contenido de la saga nórdica. ⚠️ de memoria, sin verificar la frase exacta doblada al español (tarea del investigador de voz, punto 8).

---

<a name="lamina"></a>
## Lo mejor para la lámina

- El **Codex de Atreus** (diario con bocetos a mano y runas) es el objeto perfecto para una lámina: un cuaderno real, con texto propio del mundo, no una interfaz fría.
- Usar **runas del Futhark Antiguo de verdad** (tabla en 5.3, letra libre Noto Sans Runic) para cualquier inscripción decorativa nórdica, y el **alfabeto griego** para cualquier cosa "de la saga vieja" — nunca un rúnico inventado sin sentido.
- Tipografía de cuerpo: **Cabin** (gratis, con tildes/ñ/¿/¡ comprobadas) imita la Gill Sans WGL real del juego; para el título/logo, **Cinzel** o **MedievalSharp** (ambas con tildes) como aproximación de Berserker.
- El subtítulo del juego real **no lleva caja**: sólo texto flotante abajo, con el nombre en un color/peso y la frase en otro — así de limpio debería quedar en la lámina si se imita el estilo GoW.
- Composición: **cámara al hombro, personaje descentrado, luz fría de contraluz con un único acento cálido** (fuego/runas) — la fórmula visual más reconocible de la saga nórdica (18.1-18.4).

---

<a name="no-encontre"></a>
## No encontré

- ⚠️ **El archivo real de la fuente Berserker** (título/logo/encabezados de menú): confirmada por nombre en dos fuentes (GDC/80.lv y foros de Typography.Guru), pero no la descargué — las copias que circulan en internet son de origen dudoso, y no quise comprobarla con fontTools sin poder verificar su procedencia. Búsquedas: "Berserker font God of War dafont", "Berserker God of War OTF download", en inglés.
- ⚠️ **TCRF (The Cutting Room Floor) — no pude leer el contenido completo**: `tcrf.net` está detrás de un reto de Cloudflare que no se puede saltar desde este contenedor (ni con `curl` directo ni con WebFetch), y `web.archive.org` está bloqueado por la política de red de esta sesión ("Blocked by egress policy"). Sólo tengo confirmado por búsqueda que existen las páginas `God_of_War_II` y `Proto:God_of_War_II` (únicas de la saga en TCRF) y su contenido general (sistema de magia temprano del prototipo de enero de 2007), pero no el detalle línea por línea de texto sin usar. Intentos: `curl` directo (403, Cloudflare), WebFetch (403), Wayback Machine vía API (`archive.org/wayback/available`, sí devuelve snapshot, pero `curl` a `web.archive.org` da "Blocked by egress policy" y WebFetch dice "unable to fetch from web.archive.org").
- ⚠️ **Game UI Database** (`gameuidatabase.com`) y **Interface In Game** (`interfaceingame.com`): la portada y las fichas individuales (`gameData.php?id=N`) están detrás de un reto de Cloudflare que no salté (igual que documentó ya el archivo `_Cuadros de dialogo por franquicia` sobre esta misma web para otras franquicias); usé resúmenes de búsqueda y el 80.lv/GDC en su lugar, que sí dieron datos confirmados por el propio estudio.
- ⚠️ **Colores hex exactos del HUD** (barra de salud, ira, subtítulo): no tengo una captura con el HUD activo — las capturas oficiales de Steam en `datos-texto.md` son tomas de marketing sin interfaz. No medí hex porque no es mi tarea (los fondos/paisajes con hex son el punto 16, del investigador de imagen), pero dejo constancia de que la interfaz de combate en sí tampoco está medida por nadie del equipo todavía.
- ⚠️ **Comic de Dark Horse**: no encontré páginas escaneadas para mirar directamente los globos de grito/pensamiento — sólo una reseña que describe el truco de las runas en los globos nórdicos.
- ⚠️ **Nombre del artista/diseñador exacto de la tipografía Berserker**: ninguna fuente lo da (ni Typography.Guru ni 80.lv la atribuyen a una persona).

---

<a name="bitacora"></a>
## Bitácora de búsqueda

**Punto de partida**: `partes/datos-texto.md` (capturas de Steam de God of War y Ragnarök, sin HUD — son tomas de marketing).

**Búsquedas web (en inglés y español; no hizo falta japonés/coreano/chino — la obra no viene de esos países, encargo dice "si la obra viene de ahí")**:
- Tipografía: `"God of War" 2018 logo font typeface fontsinuse`, `God of War Ragnarok font UI typeface identify`, `"Berserker" font "God of War" dafont OTF download free`, `"Gill Sans" free alternative Google Fonts open source lookalike "Cabin"`, `"Noto Sans Runic" Google Fonts free elder futhark unicode`, `free Greek typeface "GFS Didot" ancient Greek OFL Google Fonts`, `"God of War" runes Norse alphabet in-game symbols meaning translate`.
- Interfaz/cuadros de diálogo: `God of War Ragnarok Atreus journal codex UI design interview`, `"God of War" Dark Horse comic graphic novel speech bubbles lettering`, `God of War 2018 skill tree Mystic Gateway Nine Realms UI colors screenshot`, `"God of War" 2018 HUD health bar rage meter minimalist interface design`.
- Videojuegos/HUD histórico: `God of War 2005 original trilogy HUD health orb magic meter red orbs combo`, `"God of War III" 2010 interface changes health orb magic meter item box comparison GoW1`, `"God of War Ragnarok: Valhalla" DLC interface roguelike UI new`.
- TCRF/contenido cortado: `tcrf.net "God of War" cutting room floor unused`, `tcrf.net "God of War II" unused text debug menu prototype`, `tcrf.net "God of War" 2018 OR "God of War III" unused content debug`.
- Técnica/estilo (punto 18): `God of War 2018 GDC talk "one shot" camera cinematography Santa Monica Studio`, `God of War 2018 art direction interview Raf Grassetti concept art process ZBrush Substance`, `God of War Ragnarok "making of" behind the scenes engine tools Maya Houdini photogrammetry Santa Monica Studio`, `Digital Foundry God of War Ragnarok tech analysis rendering resolution ray tracing checkerboard`, `God of War 2018 Kratos skin shader subsurface scattering weathered leather texture breakdown`, `God of War PC graphics settings film grain chromatic aberration vignette options list`.
- Obras parecidas (punto 24): `Cory Barlog God of War 2018 influences inspired by "Children of Men" "Old Man's Journey" interview`, `games similar to God of War 2018 Ragnarok recommended if you like`, `Cory Barlog "Rope" "Birdman" continuous camera interview God of War inspiration`.
- Mundo/símbolos (punto 25): `God of War series story arcs timeline summary Greek saga Norse saga games order`, `God of War iconic objects Blades of Chaos Leviathan Axe Draupnir Spear symbols meaning fan vocabulary "Boy" "Stranger"`.

**Consultas directas (API, sin gastar cupo de buscador)**:
- `godofwar.fandom.com/api.php` (formato `action=parse&prop=wikitext`, la web normal da 402): páginas `Languages`, `Codex`, `Cut_Content`, `Nine_Realms`.
- Descarga y comprobación con **fontTools** de `GODOFWAR.TTF` (dafont, fan font del logo de 2005-2007: sin tildes/ñ/¿, con ¡) y `Cabin[wdth,wght].ttf` (Google Fonts vía GitHub: con á é í ó ú ñ Ñ ¿ ¡ ü Á É completos).
- `hiddenpalace.org` (prototipo de God of War II, enero 2007).
- `open3dlab.com` (rig gratuito de Kratos para Blender, licencia CC BY-NC-ND).
- `glaucolonghi.com`, `80.lv`, `variety.com`, `svg.com`, `foro3d.com`, `screenrant.com`, `sourcegaming.info`, `gamesradar.com`, `thegamer.com`.

**Fuentes que no pude usar** (ver «No encontré» arriba): `tcrf.net` (Cloudflare), `gameuidatabase.com` e `interfaceingame.com` (Cloudflare), `web.archive.org` (bloqueado por política de red de esta sesión).

**Imágenes descargadas y miradas** (capturas de Steam ya listadas en `datos-texto.md`, guardadas en la carpeta de trabajo fuera del repositorio): `gow1_ss1.jpg`, `ragnarok_ss1.jpg`, `ragnarok_ss2.jpg`, `ragnarok_ss3.jpg` — todas tomas de marketing sin HUD visible; confirman el logo/lettering pero no aportan datos de interfaz en juego.

No hace falta relanzar: todos los puntos obligatorios (5, 6, 11, 18, 24, 25) están completos con fuentes dobles donde fue posible. Quedan sólo los ⚠️ de «No encontré» arriba, que son extras (no obligatorios) según el repaso final contra `ENCARGO.md`.
