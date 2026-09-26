# Parte de TEXTO, JUEGOS Y TÉCNICA · The Legend of Zelda (encargo 65)

Investigador de texto. Puntos 5, 6, 11, 18, 24 y 25 de ENCARGO.md. Libreta de datos: un dato por línea, con fuente y ✅/⚠️.
No hay serie hermana. `datos-texto.md` venía casi vacío (AniList lo trató como el manga de A Link to the Past, no como el videojuego): la investigación real está abajo.

## Hallazgos

## 5 · Tipografía

Nintendo nunca vende sus letras: todo lo de abajo es la aproximación libre más cercana, hecha por fans. Comprobé tildes, ñ, ¿ y ¡ descargando cada `.ttf` y mirando su `cmap` con fontTools (no de memoria).

**Letra libre por uso, con la comprobación de fontTools:**

Uso | Letra libre | Tildes/ñ | ¿ ¡ | Fuente
---|---|---|---|---
Logo/título (BOTW, TOTK) | **Hylia Serif** (Omni Jacala/Artsy Omni, gratis no comercial) | ✅ sí | ❌ no | descargada de wfonts.com, comprobada con fontTools
Logo «THE LEGEND OF» (ALttP, Link's Awakening, OoT, MM) | **Charlemagne** (de pago; no hay gemela libre exacta) | ⚠️ no comprobado (de pago) | ⚠️ | [Zelda Wiki: lista de fuentes de logos](https://zelda.fandom.com/wiki/List_of_fonts_used_in_The_Legend_of_Zelda_logos) ✅ (recogido también en [Zelda Universe](https://zeldauniverse.net/media/fonts/))
Diálogo en pantalla, BOTW/TOTK | oficial: **FOT-Rodin** (de pago, Fontworks); libre más cercana: **Hylia Serif** | ✅ sí | ❌ no | ✅ dos fuentes (búsqueda web + Zelda Universe)
Diálogo pixelado, A Link to the Past (SNES) | **Return of Ganon** (codeman38, gratis, TrueType del original de Zelda 3) | ✅ sí | ✅ sí | descargada y comprobada con fontTools; ✅ dos fuentes (dafont + 1001fonts)
Diálogo pixelado, GBA (Minish Cap / Four Swords / reedición ALttP) | **TLOZ Minish Cap/ALttP/Four Sword** (FontStruct, gratis) | ✅ sí | ❌ no | descargada de dafont y comprobada con fontTools
Interfaz de juego (menús, nombres de objeto), Wind Waker y posteriores | **RocknRoll One** (Google Fonts, japonés+latín, licencia OFL libre total) | ✅ sí | ✅ sí | comprobada con fontTools; ⚠️ el uso «para interfaces Zelda» sólo en Zelda Universe (una fuente)
Onomatopeya / cartel del mundo, estilo rotulado grueso | **Reggae One** (Google Fonts, OFL) | ✅ sí | ✅ sí | comprobada con fontTools; ⚠️ recomendación de Zelda Universe (una fuente)
Subtítulos/créditos (uso genérico, no específico de Zelda) | cualquier sans neutra tipo Noto Sans; no hay una «oficial» reconocible fuera del juego | — | — | ⚠️ no encontré una fuente de créditos propia de la franquicia

**Idiomas (Hylian, Sheikah, Gerudo, Zonai):** no son alfabetos latinos, son conlangs simbólicos (cada glifo sustituye una letra latina o representa un fonema propio); fontTools no aplica «tildes» del mismo modo, pero si se mapean sobre el teclado latino sí llevan las 26 letras. Libres, por juego: **Hylian 64** (OoT/MM), **Ancient Hylian** (Wind Waker y Four Swords Adventures), **TP Hylian** (Twilight Princess), **SS Ancient Hylian** (Skyward Sword), **ALBW/BOTW Hylian**, **BOTW Sheikah**, **Gerudo Typography** (OoT/BOTW) — ✅ listados igual en [Zelda Universe](https://zeldauniverse.net/media/fonts/) y [Zelda Central](https://zeldacentral.com/media/fonts/).
- El **Zonai** de Tears of the Kingdom (glifos verde menta de los templos) tiene una fuente de fans en Cogspace ✅ ([Cogspace: Zonai Font](https://www.cogspace.com/2023/05/29/zonai-font-from-the-legend-of-zelda-tears-of-the-kingdom/)), gratis.
- El logo de TOTK usa una serif customizada que imita piedra agrietada/hueso viejo, con «of the» a tamaño reducido apilado bajo «TEARS»/«KINGDOM»; no hay una réplica libre identificada ⚠️.

## 6 · Cuadros de diálogo (juegos y manga)

Zelda es sobre todo un videojuego: su «cuadro de diálogo» real es la caja de texto en pantalla, no un globo de manga. Cada juego cambia la caja.

- **A Link to the Past (SNES, 1991)**: texto blanco pixelado, sin caja visible, directo sobre la escena ✅ (medido en `zelda/` del equipo, [Game UI Database ALttP](https://www.gameuidatabase.com/gameData.php?id=1820)).
- **Ocarina of Time (N64, 1998)**: 5 tipos de caja de texto identificados en el motor: tipo 0 «black box» (negra estándar), tipo 1 «wooden box» (marco de madera, cambia el color del texto), tipo 2 «blue box», tipo 3 «ocarina input box» (para tocar canciones), tipos 4-5 sin marco (tipo 5 sin sombra de texto) ✅ ([CloudModding OoT Wiki: Text Format](https://wiki.cloudmodding.com/oot/Text_Format)). La fuente del texto es **FOT-Chiaro** (Fontworks, de pago) ⚠️ una fuente (foro GameFAQs).
- **The Wind Waker (GameCube, 2003)**: caja de diálogo estándar sobre fondo negro translúcido; caja azul translúcida con el icono del objeto a la izquierda al recoger un ítem ✅ ([Winditor/WindWakerTextEditor, herramienta de modding](https://github.com/Sage-of-Mirrors/WindWakerTextEditor)).
- **Breath of the Wild (2017)** ✅ (medido por el equipo en `zelda/`): cápsula negra translúcida (≈80%, sobre hierba mide `#1F2315`), extremos redondos con un adorno fino en cada punta; el nombre del hablante pequeño en blanco arriba a la izquierda, fuera del texto; el texto en blanco, negrita, cursiva, centrado, con una ▽ que parpadea abajo para continuar.
- **Tears of the Kingdom (2023)**: las voces de los sabios/templos flotan en el aire, en **verde menta `#7FF1D7`**, rodeadas de glifos Zonai del mismo color, sin caja ✅ (medido por el equipo).
- **Cartelas de mundo**: postes indicadores y letreros de tienda en madera tallada (Kakariko, Hyrule Field) son parte del atrezzo 3D, no overlay 2D; su letra sigue la familia del logo del juego (Hylia Serif de referencia).

**Manga (Akira Himekawa, dúo de autoras)**: adapta Ocarina of Time, Majora's Mask, Four Swords, Twilight Princess, A Link to the Past y más, publicado por Shogakukan/VIZ ✅ ([Zelda Wiki: Akira Himekawa](https://zelda.fandom.com/wiki/Akira_Himekawa), [Wikipedia](https://en.wikipedia.org/wiki/Akira_Himekawa)). Sigue las convenciones estándar del shonen: globo ovalado de trazo fino para diálogo normal, globo dentado para grito, nube de círculos pequeños para pensamiento y onomatopeya en katakana grande fuera del globo — **por comparación con el propio dossier del equipo sobre Dragon Ball, mismo bloque editorial de Shogakukan/Shueisha en la era 1990-2000** ⚠️ (no verifiqué mirando una página concreta; el diseño visual de personajes y páginas lo cubre el investigador de imagen).

**Qué NO hacer**: un rectángulo gris opaco en una lámina de BOTW (es cápsula translúcida con esquinas redondas); en TOTK, el sabio habla sin caja de ningún tipo; en ALttP no hay caja, sólo texto sobre la escena.

**Capturas de referencia**: `zelda/` (3, del equipo) · [Game UI Database: BOTW id=35](https://www.gameuidatabase.com/gameData.php?id=35) (⚠️ Cloudflare bloquea curl y no hay navegador headless instalado en el contenedor; probé Wayback también sin éxito, así que no repetí la captura) · [TOTK id=1781](https://gameuidatabase.com/gameData.php?id=1781) · [ALttP id=1820](https://www.gameuidatabase.com/gameData.php?id=1820).

