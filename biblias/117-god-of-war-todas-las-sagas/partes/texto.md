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

(pendiente)

---

<a name="punto-11"></a>
## Punto 11 — Videojuegos de la franquicia: interfaz, menús, cajas de diálogo

(pendiente)

---

<a name="punto-18"></a>
## Punto 18 — Estilo de dibujo y técnica, y cómo replicarlo

(pendiente)

---

<a name="punto-24"></a>
## Punto 24 — Obras parecidas

(pendiente)

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
