# Parte de TEXTO, JUEGOS Y TÉCNICA · Digimon Adventure (1999)

Investigador de texto: puntos 5, 6, 11, 18, 24 y 25 de ENCARGO.md. Formato libreta
(un dato por línea, fuente, ✅/⚠️). Parte de `partes/datos-texto.md` (AniList,
staff, obras relacionadas — ya comprobado ahí, no se repite aquí salvo que se
amplíe).

## Punto 5 · Tipografía

**Logo (título)** ✅ medido con `herramientas/estilo.py` sobre el logo japonés
oficial (`static.wikia.nocookie.net/digimon/…/Digimon_Adventure_Logo.png`,
512×195, vía API de Fandom con `Referer: https://www.fandom.com/`):
- Relleno en degradado amarillo→naranja: `#FAD30A` (amarillo, 13.9% del área) a
  `#EA6F0B` (naranja, 9.0%). Contorno grueso azul `#1164A7` (7.0%) y línea oscura
  `#392903`/`#211510`. El logo japonés «デジモンアドベンチャー» tiene el borde
  recortado en zigzag, como una descarga de energía o un destello digital (no
  es un rectángulo limpio).
- El logo internacional de la franquicia («DIGIMON DIGITAL MONSTERS», el que
  usó Fox Kids en 1999) es un parche circular: «DIGIMON» en letras gruesas,
  condensadas y ligeramente inclinadas (itálica agresiva, look de placa
  deportiva/parche de los 90), en naranja con contorno azul/negro, con
  «DIGITAL MONSTERS» arriba y abajo en un anillo. Fuente: imagen
  `LOGODIGIMON.jpg` de digimon.fandom.com (269×143, medida con Pillow).
- **Letra libre recomendada**: **Anton** (Google Fonts/Fontsource, licencia
  OFL, condensada, muy gruesa) para el peso; si se quiere el ángulo itálico
  del parche real, inclinarla manualmente unos 8-10°. Comprobado con
  fontTools (`getBestCmap()` sobre el archivo `latin` de Fontsource): trae
  á/é/í/ó/ú/ñ/Ñ/¿/¡. ✅
- Alternativa más redondeada (si se prefiere el aire «juguete de los 90»):
  **Titan One** (Google Fonts, OFL) — también comprobada con fontTools, trae
  todos los caracteres. ✅
- Hay una fuente hecha por fans que imita el logo pixelado de **Digimon World
  DS** («Digimon World Ds» de UnderAnAquarianRock, dafont.com, 100% gratis
  para uso personal): **falla** — comprobado con fontTools, NO tiene tildes,
  ñ, ¿ ni ¡ (sólo ASCII). ⚠️ No usar para texto en español; sólo serviría para
  el propio wordmark «DIGIMON» que no lleva esos caracteres.

**Globo normal (diálogo tranquilo)**: no hay manga con globos propios de
*Adventure* (ver punto 6: la serie es anime, casi sin cartelas de globo). Para
una lámina con globo redondeado, recomendado **Baloo 2** (Google Fonts, OFL,
peso 700), trazo redondeado y amigable, encaja con el tono infantil/90 de la
serie. Comprobado con fontTools: trae todos los caracteres españoles. ✅

**Grito**: **Bangers** (Google Fonts, OFL) — letra de cómic en itálica
dinámica, gruesa, ideal para «¡Agumon, digivoluciona!» gritado. Comprobada con
fontTools: completa. ✅

**Pensamiento**: **Patrick Hand** (Google Fonts, OFL) — trazo de rotulador a
mano, más suave que el grito, para el texto pensado (la serie no usa nube de
pensamiento clásica: casi todo el monólogo interno es narrado en voz en off,
ver punto 6). Comprobada, completa. ✅

**Onomatopeya**: **Luckiest Guy** (Google Fonts, OFL) — letra de cómic muy
gruesa con borde, para *impactos* y golpes de las peleas. Comprobada, completa.
✅ (Alternativa: Bangers también sirve doblada).

**Cartel del mundo** (rótulos de File City, carteles de madera del Digital
World): **Permanent Marker** (Google Fonts, OFL) — imita un marcador grueso a
mano, coincide con el aspecto artesanal/reciclado de los carteles de File City
(chatarra y madera, ver punto 25). Comprobada, completa. ✅

**Interfaz de videojuego**: **Press Start 2P** (Google Fonts, OFL) — pixel
font de 8-16 bit, coincide con la letra pixelada real del menú y las cajas de
diálogo de *Digimon World* (PS1, 1999, ver punto 11: fotograma medido). Trae
todos los caracteres españoles (comprobado con fontTools) aunque el juego
original sólo usaba mayúsculas ASCII en inglés. ✅ Alternativa para pantallas
tipo «terminal/Digivice»: **VT323** (Google Fonts, OFL, imita un monitor CRT
verde), también comprobada y completa. ✅

**Subtítulos o créditos**: **Nunito** (Google Fonts, OFL) — sans-serif
redondeada, limpia, legible en celular; comprobada, completa. ✅

_Cómo se comprobó cada letra_: se bajó el archivo `.ttf` real (subset "latin"
de Fontsource, que en Google Fonts SÍ incluye á/é/í/ó/ú/ñ/Ñ/¿/¡ pese al
nombre — el subset "latin-ext" en cambio trae otras letras latinas
[checo/polaco/etc.] y NO estos acentos: se comprobó primero con "latin-ext" y
falló en las 13 fuentes probadas, luego con "latin" y las 14 funcionaron) y se
abrió con `fontTools.ttLib.TTFont(...).getBestCmap()`, comprobando que
`ord(c) in cmap` para cada carácter. Script en
`/tmp/claude-0/trabajo/40-digimon-texto/fuentes/`. Captura comparativa
(`muestra_fuentes.png`, renderizada con Pillow) confirma visualmente que
todas las letras muestran bien «¡BANGERS! ñoño áéíóú ¿Qué?».

## Punto 6 · Cómo hablan y piensan en pantalla

- **Es un anime, no manga**: *Digimon Adventure* (1999) no tiene manga propio
  con globos — el manga de la franquicia es *V-Tamer 01* (Hiroshi Izawa,
  V-Jump, 1998-2003), un Tai **alternativo** al de la serie, no una
  adaptación con los mismos globos. Fuente: wikitext de
  `digimon.fandom.com/wiki/Digimon_Adventure_V-Tamer_01`. ✅ Por eso, para la
  lámina, el «cuadro de diálogo propio de la serie» tiene que salir del
  **Digimon Analyzer** (la ficha en pantalla que aparece cuando un Digimon
  nuevo entra en escena) y de los videojuegos (punto 11), no de un globo de
  manga.
- **El Digimon Analyzer, primera versión** (usada desde la llegada al Digital
  World hasta la derrota de Etemon): fondo negro y blanco a cuadros (rejilla),
  la imagen del Digimon en un recuadro negro, el nombre en **letras azules
  sobre una caja verde** encima de la imagen, la romanización en letras
  latinas al lado, y una caja rosa/dorada y otra azul verdosa con los datos.
  Fuente: wikitext de `digimon.fandom.com/wiki/Digimon_Analyzer`. ✅ Fotograma
  propio (`TanemonAnalyzer.jpg`, 300×240, vía API de Fandom): confirma la
  rejilla negra, la etiqueta verde redondeada con «TANEMON», y a la derecha
  una caja rosa con «幼年期» (In-Training) y una tabla de datos en japonés
  (レッサーデジモン / タイプ / データ / 必殺技). Paleta medida con
  `estilo.py`: negro `#030302` (51%), gris verdoso `#324632`, turquesa
  `#42B9AC`, verde `#319F41`. Línea marcada, sombreado mixto, brillo bajo
  (25%): la pantalla es oscura, casi toda negra con la ficha iluminada. ✅
- **El Analyzer, segunda versión** (se lo da Gennai a Izzy, luego se
  actualiza para ver los datos de los Digivices de los demás): fondo negro con
  un texto rojo en bucle «ANALYZER DIGIMON ANALYZER DIGIMON…» arriba y abajo
  (como un ticker), nombre en **letras verdes sobre cápsula negra/verde**, una
  etiqueta rosa con el nivel (p. ej. «完全体» Ultimate) y tres cajas
  (negra/naranja/plata) con los datos. Fotograma propio
  (`Magnaangemon.jpg`, 300×240): confirma el ticker rojo y la cápsula verde
  del nombre. Paleta medida: marrón oscuro `#362E1E` (17%), casi negro
  `#1B0A02`, beige `#A69584`/`#817060`, rojo apagado `#79231F`. ✅
- **Lo importante para la lámina**: NUNCA una burbuja blanca de cómic
  genérica. La «voz visual» propia de Digimon es esta **ficha técnica en
  pantalla, oscura, con rejilla o textura digital de fondo y una cápsula de
  color con el nombre** — más parecida a una interfaz de ordenador o a un
  visor de Digivice que a un globo. Es lo que hay que traducir a los cuadros
  de texto del canal: caja oscura semitransparente, borde fino de color, el
  «nombre del que habla» en una cápsula redondeada de color vivo arriba, texto
  claro debajo.
- **Cómo narra la serie**: no hay voz en off de pensamiento con nube; en el
  doblaje japonés e inglés, el propio Digimon o un narrador dan los datos del
  Analyzer en voz alta mientras aparece en pantalla (confirmado en el
  wikitext: «con este analizador, normalmente son los propios Digimon los que
  dan la información»). ✅
- Los cuadros de diálogo de **Digimon Survive** (videojuego, ver punto 11) SÍ
  son el mejor referente «sin burbuja blanca»: texto blanco superpuesto a la
  escena 3D, sin caja, con el nombre del personaje arriba en blanco grueso y
  una línea fina debajo que separa nombre de texto, y una flechita ▽ en la
  esquina para avanzar. Fotograma propio (`survive_1.jpg`, 1920×1080, captura
  oficial de Steam). ✅ Las decisiones de diálogo (el «medidor de carácter» de
  Survive) se muestran como **pastillas alargadas** con un icono de flecha de
  dirección (arriba/izquierda/derecha) al lado: pastilla oscura para las
  opciones neutras y una **pastilla verde clara resaltada** para la opción de
  más «Empatía» en ese momento. Fotograma propio (`survive_2.jpg`). ✅

## Bitácora (parcial, sigue)

- Wiki `digimon.fandom.com` vía `action=parse&prop=wikitext`: Crests, Digivice,
  Digivolution, Digimon Adventure (página principal), Digimon Analyzer,
  Digimon World, Digimon Adventure V-Tamer 01. Todas con éxito.
- `tcrf.net` (The Cutting Room Floor): **bloqueado con 403 (Cloudflare)** en
  dos intentos (API y página directa). Wayback Machine de tcrf.net también
  falló (egress policy / conexión cortada — proxy compartido con otros
  ayudantes). Pendiente reintentar más tarde si hay tiempo.
- Steam API (`storesearch`, `appdetails`) para los videojuegos actuales:
  funcionó bien (ver punto 11).
- Internet Archive: vídeo de `Digimon World PlayStation PAL Gameplay (Full
  Demostration)` usado con `fotogramas.py --cortes` y `--fotograma` para sacar
  las cajas de diálogo reales del juego de 1999.
- Fontsource API (`api.fontsource.org`) + CDN de jsDelivr para bajar `.ttf`
  reales y comprobarlos con fontTools.
- dafont.com: búsqueda `search.php?q=digimon` funcionó por curl directo (sin
  JS).
- WebSearch usadas hasta ahora (2 de ~50): «Digimon Adventure logo font
  identification typeface» (inglés), «Digimon Adventure animation production
  Toei cel digital paint interview character designer» (inglés).

Sigue: puntos 11 (ampliar con más juegos: Cyber Sleuth, Next Order, Time
Stranger — interfaz ya vista en capturas de Steam, falta describir en texto y
medir colores; buscar TCRF por otra vía o dar por ⚠️), 18 (estilo de dibujo y
técnica de animación 1999, cómo replicar en Photoshop/Blender — falta
profundizar con entrevistas), 24 (obras parecidas más allá de AniList: TV
Tropes, influencias declaradas del autor), 25 (mundo/historia por arcos,
vocabulario, símbolos — falta completar arcos y vocabulario), y la tabla de
cumplimiento + "Lo mejor para la lámina" + "No encontré" finales.
