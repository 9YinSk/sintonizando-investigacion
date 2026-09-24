# Parte · Investigador de TEXTO, JUEGOS Y TÉCNICA · Lilo & Stitch (23-lilo-stitch)

Puntos de `ENCARGO.md`: **5** (tipografía), **6** (cuadros de diálogo), **11**
(videojuegos), **18** (estilo de dibujo y técnica, cómo replicarlo), **24**
(obras parecidas) y **25** (mundo y símbolos).

Parto de `partes/datos-texto.md` (casi vacío: la película no es serie de
AniList ni tiene etiqueta en Danbooru, así que `recolectar.py` no trajo casi
nada) y de `biblia.md` ya existente (hecha con la red cerrada, sin ver
ninguna imagen ni vídeo — lo dice su propio recuadro «Cómo se hizo»). Mi
trabajo de hoy es con la **red abierta**: miré cómics reales, capturas de
videojuego, modelos 3D y letras, cosa que la pasada anterior no pudo hacer.
No repito lo que la biblia ya tiene confirmado (§6 tipografía, §7 diálogo,
§13 videojuegos); lo amplío, lo verifico con imágenes y **añado los puntos
18, 24 y 25, que en la biblia actual no existen todavía** (se saltó, porque
esta biblia es de antes del 24-sep-2026, cuando se añadieron esos 3 puntos
al encargo).

Formato: un dato por línea, fuente enlazada, ✅ (dos fuentes) o ⚠️ (una).

---

## Punto 5 · Tipografía

### 5.1 El logo oficial (confirmado con imagen)

- Logo oficial «Lilo & Stitch»: rótulo a mano, letras redondas muy gruesas,
  algo infladas, bailando sobre la línea, en rojo con contorno blanco ✅
  (imagen oficial medida por su API: **800×620 → en realidad 800×310 px**,
  [Fandom disney, `File:Lilo & Stitch Logo.png`](https://static.wikia.nocookie.net/disney/images/9/9d/Lilo_%26_Stitch_Logo.png/revision/latest?cb=20160630120430),
  necesita `Referer: https://www.fandom.com/`). La vi directamente.
- La copia que circula en internet con ese look se llama **«Buka Bird»**, de
  Steve Ferrera, **gratis sólo para uso personal** ✅ (ya confirmado en
  `biblia.md` §6 con 3 fuentes: FontMeme, FontBolt, Fontspace.io). No pude
  bajarla hoy tampoco (no está en Google Fonts ni GitHub) para comprobar
  tildes con fontTools ⚠️: si el dueño la quiere, hay que comprar la
  licencia comercial o pedir permiso a Ferrera.
- **Variante del logo en el videojuego de Game Boy Advance** (2002,
  Digital Eclipse): el mismo rótulo rojo-con-blanco pero **metido dentro de
  una tabla de surf**, con un borde verde de florecitas blancas alrededor
  («Disney's» arriba en letra fina). La vi yo mismo en la pantalla de
  título ✅ (captura propia, ver `gba/s12.png` en la carpeta de trabajo;
  fuente [archive.org/details/stitch_gba](https://archive.org/details/stitch_gba),
  480×320 px, el tamaño real del hardware). Es una **variante de logo lista
  para usar en un objeto físico** (una tabla de surf, un cartel de playa):
  útil si la lámina quiere un guiño al merchandising sin copiar el logo
  principal 1:1.
- **Variante del logo en el manga japonés** *Tono-sama to Stitch* / *Stitch
  & the Samurai* (2020-2021, ver §24): la portada usa un título distinto,
  en trazo de pincel más anguloso y con sangre/tinta roja, estilo cartel de
  samurái — nada que ver con el redondeado de Disney. La vi yo mismo
  (portada, 432×648 px, [TOKYOPOP](https://tokyopop.com/collections/disneymanga/products/9781427868961_disney-manga-stitch-and-the-samurai-volume-1))
  ✅. Sirve para mostrar que la franquicia **cambia de letra según el
  contexto cultural**; no la recomiendo para #fotos (es demasiado alejada
  del tono Disney/Hawái del canal).

### 5.2 Ocho letras libres, una por uso (comprobadas hoy con fontTools)

Bajé cada letra directa de `fonts.gstatic.com` (la URL real que da la API
`css2` de Google Fonts) y comprobé con `fontTools.ttLib` si el cmap trae
**á é í ó ú ñ Ñ ¿ ¡**. Las 8 están completas ✅ (verificación propia, hoy).
Las 4 primeras ya estaban en la biblia (las revalidé); las 4 últimas son
**nuevas**, para los usos que la biblia todavía no cubría (globo de cómic,
grito, cartel del mundo, interfaz):

| Uso (punto 5 del encargo) | Letra | Diseñador/fundición | Licencia | Tildes ñ ¿¡ |
|---|---|---|---|---|
| **Logo o título** | Lilita One | Juan Montoreano | OFL | ✅ completa |
| **Pensamiento** (burbuja de nube, blanda) | Baloo 2 | Ek Type | OFL | ✅ completa |
| **Onomatopeya** (fuerte, de cómic clásico) | Luckiest Guy | Astigmatic | OFL | ✅ completa |
| **Créditos / pie de foto a mano** | Gochi Hand | HT Fonts | OFL | ✅ completa (ya en biblia) |
| **Globo normal de cómic** ⭐ nuevo | **Comic Neue** (Bold) | Craig Rozynski | OFL | ✅ completa |
| **Grito / exclamación** ⭐ nuevo | **Bangers** | Vernon Adams | OFL | ✅ completa |
| **Cartel del mundo** (tiki, surf, luau) ⭐ nuevo | **Trade Winds** | Sideshow | OFL | ✅ completa |
| **Interfaz de juego / HUD** ⭐ nuevo | **Actor** | Sorkin Type Co. | OFL | ✅ completa |
| **Subtítulos o créditos de vídeo** ⭐ nuevo | **Quicksand** | Andrew Paglinawan | OFL | ✅ completa |

- **Comic Neue** está diseñada explícitamente como «un Comic Sans mejor
  para cómics»: encaja perfecto con el globo normal que vi en el cómic real
  (§6.1) ✅ [Google Fonts](https://fonts.google.com/specimen/Comic+Neue).
- **Trade Winds** tiene look de cartel de tiki-bar / luau de los años 50:
  la recomiendo para un letrero dentro del mundo (un cartel de tienda de
  surf, no para el título del canal) ✅ [Google Fonts](https://fonts.google.com/specimen/Trade+Winds).
- **Actor** es una sans condensada de aire «pantalla de nave espacial»,
  coherente con la tecnología de Jumba y la Federación Galáctica (§25) ✅
  [Google Fonts](https://fonts.google.com/specimen/Actor).
- Recomendación final para #fotos: **Lilita One** para «Fotos» (el título
  del canal), **Gochi Hand** para los pies de foto a mano de Lilo, y si se
  usa un bocadillo de cómic, **Comic Neue Bold**.

---

## Punto 6 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

**Esto es lo más importante del encargo** («la lámina NO lleva una burbuja
blanca genérica»). La biblia ya tiene bien cubierta la película (no hay
globos, todo es voz en off, con la lista de escenas y minutos en su §7). Lo
que yo aporto hoy es lo que la red cerrada no pudo dar: **cómics reales de
la franquicia, vistos con mis propios ojos**, que sí tienen bocadillo.

### 6.1 El bocadillo real de la franquicia (visto directamente)

Miré 3 páginas del cómic **Dynamite Entertainment, *Disney's Lilo & Stitch*
#1** (2024, guion Greg Pak, dibujo Giulia Giacomino), bajadas de la
[preview de DuckTalks](https://ducktalks.com/2024/01/03/dynamite-comics-lilo-stitch-1-preview/)
(1988×3057 px cada página, medidas por mí) ✅:

- **Bocadillo normal**: óvalo blanco, borde negro de 3-4 px, cola recta
  hacia quien habla. Letra en **mayúsculas, sans-serif redondeada y
  gruesa** (muy parecida a Comic Neue Bold), con palabras clave en
  **cursiva y más gruesas** para dar énfasis («*BLOW* up», «*responsible*
  older sister», «*'OHANA*»). No hay línea fina de cómic clásico
  americano: es una letra más suave, a juego con lo redondeado de los
  personajes.
- **Cartela de flashback/aparte**: rectángulo con esquinas redondeadas,
  fondo **azul pálido** (no blanco), mismo tipo de letra, para el «Look,
  you can't... you can't just blow things up!» de Nani en modo recuerdo.
- **No hay bocadillo de pensamiento ni onomatopeyas** en las páginas que vi
  (⚠️ dato de sólo 3 páginas de 1 cómic; puede haber en otros números).
- **Frase encontrada, en el propio cómic**: «**'OHANA MEANS FAMILY. AND
  FAMILY MEANS NO ONE GETS LEFT BEHIND OR FORGOTTEN, RIGHT?**» — «**RIGHT.**»
  (David a Nani, cómic #1, 2024) ✅. Es la **misma frase icónica** de la
  película (ahí sale de Lilo a Stitch), reescrita en el cómic: **doble
  fuente independiente** para la frase más citada de toda la franquicia.
- **Vocabulario hawaiano metido tal cual en el globo, en cursiva**:
  «**'Ohana**», «**Kuleana**» (responsabilidad — cuidar de los demás y del
  entorno) y «**Mālama 'āina**» (cuidar la tierra) ✅ (vistas en la página;
  significado confirmado en 2 fuentes: [Ko Olina](https://koolina.com/destination/kuleana/),
  [NOAA Sanctuaries](https://sanctuaries.noaa.gov/magazine/6/kuleana.html)).
  Es vocabulario real del mundo (ver también §25): útil para un texto corto
  tipo «Kuleana: sube lo que hiciste tú» en el canal.
- **Conclusión para la lámina**: si hace falta un bocadillo, que sea **el
  óvalo blanco de borde grueso con letra Comic Neue Bold en mayúsculas**,
  nunca la burbuja plana estilo chat/messenger. Esto confirma y afina lo
  que ya decía la biblia en su §7.5 («qué NO hacer»).

### 6.2 Cómics de la franquicia (mapa completo)

- **Disney Adventures *Comic Zone*** (2002-2007): tiras cortas en la
  revista infantil; compiladas en *Comic Zone Volume 1: Disney's Lilo &
  Stitch* (2006) ✅ ([Disney Wiki](https://disney.fandom.com/wiki/Comic_Zone_Volume_1:_Disney%27s_Lilo_%26_Stitch),
  [Lilo & Stitch Wiki](https://liloandstitch.fandom.com/wiki/Comic_Zone_Volume_1:_Disney%27s_Lilo_%26_Stitch)).
- Dato curioso de participación: en mayo de 2006 Disney Adventures publicó
  **«Stitch's Movie Mix-Up»**, una versión de la tira **con los bocadillos
  vacíos** para que los niños escribieran su propio diálogo y lo mandaran a
  la revista ✅ (2 fuentes: [Lilo & Stitch Wiki](https://liloandstitch.fandom.com/wiki/Comic_Zone_Volume_1:_Disney%27s_Lilo_%26_Stitch),
  reflejado también en [TV Tropes, *Comic Zone: Lilo & Stitch*](https://tvtropes.org/pmwiki/pmwiki.php/ComicStrip/ComicZoneLiloAndStitch)
  vía buscador, la web en sí me dio 403 hoy). Es la prueba de que el
  bocadillo vacío **ya se usó de verdad** con esta franquicia como juego
  participativo — una idea reutilizable para el foro de #fotos («escribe
  tú el pie de foto»).
- **Dynamite Entertainment, *Lilo & Stitch*** (2024-en curso), guion Greg
  Pak: la serie activa ahora mismo, la que vi en 6.1 ✅.
- **Manga *Tono-sama to Stitch* / *Stitch & the Samurai*** (2020-2021,
  Japón): ver §24, no pude ver páginas interiores (sólo la portada) ⚠️.

### 6.3 En los videojuegos

Ningún juego de la franquicia tiene una caja de diálogo tan icónica como la
de Pokémon o Undertale (confirmado en biblia §7.4 y ampliado en mi §11): no
la uses como referencia central.

---
