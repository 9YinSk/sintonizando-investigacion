# Parte de TEXTO, JUEGOS Y TÉCNICA · Hollow Knight (encargo 67)

Investigador de texto. Puntos 5, 6, 11, 18, 24 y 25 de ENCARGO.md. Libreta de datos, no prosa.
Wiki de Fandom confirmada: `hollowknight.fandom.com`. Sin serie hermana en este encargo.

## Hallazgos

### 5 · Tipografía y su letra libre

Hollow Knight (y Silksong) usan sólo dos tipos reales, sin letra propia diseñada: son tipografías comerciales reutilizadas.

- Interfaz, título, nombres de zona y créditos: **Trajan Pro** (mayúsculas romanas grabadas en piedra) · https://en.wikipedia.org/wiki/Trajan_(typeface) y confirmado en el hilo de datamining de ZenHAX (fuente del archivo del juego) https://zenhax.com/viewtopic.php@t=17838.html · ✅ (dos fuentes)
- Diálogo de los personajes (los cuadros de texto en juego): **Perpetua** (serif inglesa de Eric Gill, 1929-32) · archivo extraído `Perpetua.TTF` en la wiki técnica del juego https://hollowknight.wiki/w/File:Perpetua.TTF y https://en.wikipedia.org/wiki/Perpetua_(typeface) · ✅ (dos fuentes)
- Ninguna de las dos es gratis para descargar tal cual (son de Monotype/Linotype, de pago); por eso hace falta letra libre parecida.
- **Letra libre para Trajan Pro (logo, títulos, nombres de zona)**: Google Fonts **Cinzel**, todo mayúsculas ornamentales grabadas en piedra romana, la sustituta más citada de Trajan · https://fonts.google.com/specimen/Cinzel · comprobada con fontTools (`TTFont(f).getBestCmap()` sobre el TTF bajado de `fonts.gstatic.com`): trae á é í ó ú ñ Ñ ¿ ¡ ü · ✅ (uso extendido + comprobación propia)
- **Letra libre para Perpetua (diálogo)**: Google Fonts **EB Garamond** (serif clásica próxima en proporción y peso) o **Spectral** (serif contemporánea, más legible en pantalla pequeña) · https://fonts.google.com/specimen/EB+Garamond y https://fonts.google.com/specimen/Spectral · las dos comprobadas con fontTools: tildes, ñ, ¿ y ¡ presentes · ✅
- **Letra libre para logo o rótulo tallado/gótico** (si se quiere un toque más «grabado en madera de iglesia», como las cartelas y el logo con ornamentos góticos, ver punto 6): **MedievalSharp** o **Metamorphous** (Google Fonts), ambas con trazo irregular a pluma/gubia · https://fonts.google.com/specimen/MedievalSharp y https://fonts.google.com/specimen/Metamorphous · comprobadas con fontTools: sí traen tildes, ñ, ¿, ¡ · ✅
- Alternativa serif más ornamental para citas largas o cartelas de personaje (Seer, Confesor): **Cardo** (Google Fonts, hecha para textos académicos con muchos diacríticos) · https://fonts.google.com/specimen/Cardo · comprobada con fontTools: sí · ✅
- No hay onomatopeyas dibujadas en pantalla (el juego casi no tiene SFX de texto en pantalla, a diferencia de un manga); los «gritos» del Caballero no llevan letra especial, sólo signos de exclamación dentro del mismo cuadro de diálogo con Perpetua. ⚠️ (una fuente: revisión propia de capturas de Steam en `datos-texto.md`, no hay artículo que lo documente aparte)
- Comprobación técnica hecha con fontTools sobre los TTF reales descargados de `fonts.gstatic.com` (no de memoria), guardados en `/tmp/claude-0/trabajo/67-hollow-knight-texto/`.

### 6 · Cuadros de diálogo, cartelas e interfaz (lo más importante para la lámina)

No hay manga oficial de Hollow Knight; **el «cuadro de diálogo» de esta obra es el del propio videojuego**: un panel de piedra/hueso rectangular, nunca una burbuja redonda. Analizado en detalle en champicky.com (blog de diseño de interfaces) y en el catálogo de capturas de interfaceingame.com.

- El cuadro de diálogo es un **rectángulo con esquinas curvas, borde fino claro sobre fondo casi negro semitransparente**, sin cola ni pico como una burbuja de cómic: se apoya siempre en la parte baja de la pantalla, encima del personaje que habla · https://champicky.com/2022/03/23/hollow-knight-interface-design-analysis/ y capturas propias de Steam (`datos-texto.md`) · ✅ (dos fuentes)
- Arriba y abajo del cuadro hay una **cenefa dibujada a mano**: espirales que terminan en voluta, inspiradas en los remates de los gabletes (frontones) góticos de iglesias francesas e inglesas; la misma cenefa (girada y escalada) decora también el logo, los menús, las instrucciones y los carteles con el nombre de cada zona · https://champicky.com/2022/03/23/hollow-knight-interface-design-analysis/ (cita fuentes: A. C. Pugin, *Pugin's Gothic Ornament*) · ✅
- El icono que marca «sigue hablando / hay más texto» es una **flecha estrecha y alargada**, sacada por abstracción de los remates de piedra (finiales) de las catedrales góticas; el mismo tipo de flecha señala objetos interactivos · misma fuente champicky.com · ✅
- Motivo recurrente en toda la interfaz: **caparazones de insecto** (con y sin alas) usados como adorno, coherente con que los personajes son bichos; en las tiendas, el marco de la ventana usa la silueta de la cabeza del tendero (p. ej. Iselda, Salubra) como decoración · misma fuente, con capturas propias · ✅
- Nombres de zona (cartelas de «bienvenida a…») usan la misma cenefa espiral pero girada en ángulos distintos según el sitio, nunca un marco genérico · champicky.com · ⚠️ (una fuente, sin segunda referencia que lo detalle)
- No hay pensamientos en globo con nube (no es un personaje que «piense en voz alta» en pantalla): toda la narrativa pasa por el mismo cuadro rectangular, sea diálogo de un NPC, texto de un ítem (Hunter's Journal) o un cartel del mundo · revisión propia de capturas Steam + página de la wiki `Hunter's Journal` https://hollowknight.fandom.com/wiki/Hunter%27s_Journal · ⚠️ (una fuente detallada, coincide con lo visto en capturas)
- La taxonomía de pantallas de interfaz (catálogo con capturas) distingue: Diálogo, Menú principal, Menú de partida, Inventario, Mapa, Créditos, Pantalla de derrota, Ajustes de mando/audio/brillo, Logros, Tienda, Tutorial · https://interfaceingame.com/games/hollow-knight/ · ✅ (catálogo curado, cruzado con capturas de Steam)

### 11 · Videojuegos de la franquicia: interfaz, menús y cajas de diálogo

Hay dos juegos: *Hollow Knight* (2017) y *Hollow Knight: Silksong* (2025), ambos de Team Cherry, con la misma familia visual de interfaz (cenefas góticas + insecto), documentados con capturas 1920×1080 en `datos-texto.md`.

- *Hollow Knight* tiene **10 «estilos de menú» distintos** que cambian el fondo, color y sonido ambiente del menú principal (se eligen en la pestaña Extras): Classic (hierba), Hidden Dreams (brillo), The Grimm Troupe (fuego crepitando), Lifeblood (hierba), Infected (latido bajo, se desbloquea al completar el final «Hollow Knight» o «Sealed Siblings»), Void (desatura color + ambiente del Abismo, final «Dream No More»), Steel Soul (desatura color + ambiente de Crystal Peak, modo Alma de Acero), y más · wikitext de `Menu Styles (Hollow Knight)` https://hollowknight.fandom.com/wiki/Menu_Styles_(Hollow_Knight) · ✅ (fuente primaria de la wiki, contrastable en capturas de Steam)
- *Silksong* tiene **7 estilos de menú**, 6 con condición de desbloqueo; al completar «Sister of the Void» y desbloquear el estilo Surface se añade el pin de Lace junto a la Aguja de Hornet en todos los estilos (refleja que ahora ella es la protagonista) · https://hollowknight.wiki/w/Menu_Styles_(Silksong) y confirmado por resumen cruzado de búsqueda · ✅
- El **Hunter's Journal** (bestiario) usa el mismo cuadro rectangular con cenefa gótica que el diálogo, pero con una entrada de texto más larga y un dibujo del bicho a la izquierda; se abre y completa cazando enemigos · https://hollowknight.fandom.com/wiki/Hunter%27s_Journal · ⚠️ (una fuente citada, comprobado además en capturas propias de Steam)
- El **Hall of Gods** (galería de jefes en el DLC Godmaster) usa tarjetas con marco ornamental, similar a una vitrina de trofeos, distinta del resto de menús (más recargada, con el sello de cada jefe) · https://hollowknight.fandom.com/wiki/Hall_of_Gods · ⚠️ (una fuente)
- Ambos juegos están localizados a Español de España, coreano, chino simplificado y tradicional, japonés, entre otros (11 idiomas de texto), lo que confirma que la interfaz soporta tildes, ñ y signos de apertura ¿¡ en su propia fuente (Perpetua) de forma oficial · ficha de Steam en `datos-texto.md` (capturas 1920×1080, 367520 y 1030300) · ✅
- No hay «letra según emoción» dentro del juego (no grita en tipografía distinta ni cambia de fuente para pensar): toda variación es de puntuación (signos de exclamación, puntos suspensivos) dentro del mismo cuadro Perpetua · revisión propia de capturas · ⚠️ (una fuente)


