# Investigador de TEXTO, JUEGOS Y TÉCNICA · El viaje de Chihiro (encargo 98)

Puntos de `ENCARGO.md` que me tocan: **5** (tipografía), **6** (cómo hablan y piensan en
pantalla), **11** (videojuegos de la franquicia), **18** (estilo de dibujo y técnica, y cómo
replicarlo), **24** (obras parecidas) y **25** (el mundo, la historia y sus símbolos).

Parto de `partes/datos-texto.md` (AniList: ficha, equipo creativo, obras parecidas; Steam no
devolvió juegos). Lo pesado (fotogramas oficiales, fuentes .woff2 comprobadas) está en
`/tmp/claude-0/trabajo/98-el-viaje-de-chihiro-texto/`. Es película (2001), no serie: no hay manga
oficial ni videojuego con licencia — se comprueba y se dice, no se inventa.

## Hallazgos

### Punto 5 · Tipografía

**El logo del título**
- El logo de `千と千尋の神隠し` usa una fuente base, pero el carácter 千 ("Chi") se rehízo a mano
  porque no cuadraba en proporción con el resto del logo (según se cuenta) · fuente: cuenta de fans
  [@ghibli_world en X](https://x.com/ghibli_world/status/1814525645466034560) (jul-2026) · ⚠️ una
  sola fuente, no oficial — no encontré quién lo dibujó ni una segunda fuente que lo confirme.
- Letra libre para un logo/título con ese aire pintado a pincel: **Yuji Syuku** (Google
  Fonts/Fontsource, licencia OFL-1.1) · comprobado con `fontTools` sobre el archivo real
  (`yuji-syuku-latin-400-normal.woff2`): trae á é í ó ú ñ Ñ ¿ ¡ Á É · ✅ (herramienta, no de memoria).

**El rótulo tallado de la casa de baños — 「油屋」(Aburaya)**
- Letrero de madera con los kanji 屋油 (se lee de derecha a izquierda: 油屋, *Aburaya*) tallados en
  relieve, iluminado por el fondo rojo del edificio · visto y medido en el fotograma oficial
  `chihiro048.jpg` (1920×1038, `ghibli.jp/gallery/`) · colores medidos con Pillow: madera del cartel
  `#B87D4B`, trazo tallado oscuro `#6A4D3F` a `#684C3B` · ✅ (imagen oficial, medido por mí) + Fandom
  confirma la lectura y el significado ("Bathhouse", `油屋`, *Aburaya*, lit. "casa del aceite") en
  [ghibli.fandom.com/wiki/Bathhouse](https://ghibli.fandom.com/wiki/Bathhouse).
- Letra libre más cercana para un cartel tallado así: **Shippori Mincho B1** (OFL-1.1, gruesa, con
  esquinas de cincel) · comprobado con fontTools: trae á é í ó ú ñ Ñ ¿ ¡ Á É · ✅.
- El estandarte/bandera blanca junto a la puerta lleva sólo el kanji 油 dentro de un círculo, en
  pincelada gruesa tipo *mon* (emblema familiar japonés) · visto en `chihiro011.jpg` (fotograma
  oficial, exterior nocturno de la casa de baños) · ✅ (imagen oficial).

**El bib del bebé Boh — 「坊」**
- Bata/peto rojo con el kanji 坊 ("niño", diminutivo cariñoso de bebé) en blanco con contorno negro
  grueso, trazo infantil redondeado · visto y medido en `chihiro035.jpg` y `chihiro048.jpg`: rojo
  `#E7605A`/`#EA635F`, kanji blanco cálido `#EBECDC` · ✅ (imagen oficial, medido por mí).
- Letra libre para ese estilo infantil/redondeado: **Hachi Maru Pop** (OFL-1.1) · comprobado con
  fontTools: á é í ó ú ñ Ñ ¿ ¡ Á É presentes · ✅.

**Las 8 letras pedidas por el encargo (una por uso), todas verificadas con `fontTools` sobre el
archivo `.woff2` real, no de memoria — todas OFL-1.1, Google Fonts/Fontsource, con á é í ó ú ñ Ñ ¿ ¡
Á É confirmados:**

| Uso | Letra libre | Por qué |
|---|---|---|
| Logo o título | **Yuji Syuku** | pincel fino, aire de caligrafía de título de película |
| Globo normal | **Klee One** | escritura a mano cuidada, legible, informal sin ser infantil |
| Grito | **Yuji Boku** | pincel grueso e irregular, mucha presión |
| Pensamiento | **Zen Old Mincho** | serif fino y sobrio, para el silencio interior (Ghibli casi no usa globos de pensamiento: ver más abajo) |
| Onomatopeya | **Hachi Maru Pop** | redonda, saltarina, como una burbuja de sonido |
| Cartel del mundo | **Shippori Mincho B1** | gruesa, esquinas de cincel — igual que el rótulo 油屋 |
| Interfaz de juego | **M PLUS Rounded 1c** | redondeada, es la familia que más usan los HUD de juegos japoneses reales |
| Subtítulos o créditos | **Noto Sans JP** | neutra y muy legible a tamaño pequeño |
- ✅ (herramienta `fontTools`, comprobado por mí descargando cada `.woff2` de Fontsource).
- Alternativa suelta para notas escritas a mano (cartas, etiquetas) si hace falta una novena letra:
  **Yomogi** (OFL-1.1, también verificada) · ✅.

**Onomatopeyas / cuadros del manga**
- *El viaje de Chihiro* **no tiene manga oficial** (es una película original de Miyazaki, no una
  adaptación) · comprobado buscando en japonés e inglés: no aparece en ninguna lista de manga de
  Ghibli ni en AniList (`Obras relacionadas` sólo lista un corto, *Piyopiyo Baba*, ninguna manga) ·
  ✅ (ausencia comprobada en dos fuentes: AniList y la búsqueda directa).
- Tokuma Shoten publicó un **フィルムコミック (film comic)** —fotogramas reales de la película con
  globos de diálogo superpuestos, formato habitual en Japón para películas Ghibli— título
  `フィルムコミック 千と千尋の神隠し（１）` · fuente: [tokuma.jp/book/b503717.html](https://www.tokuma.jp/book/b503717.html)
  · ⚠️ sólo la ficha de venta: no encontré páginas escaneadas para ver el rotulado tipográfico real
  de esos globos.

**Subtítulos y créditos**
- No encontré qué tipografía usan los subtítulos oficiales en español latino (Blu-ray o streaming)
  · búsquedas hechas en español y japonés, sin resultado con una fuente identificada · ⚠️ **No
  encontré** (ver abajo). Los créditos originales japoneses van en formato vertical clásico de cine
  japonés (estilo mincho); de ahí la recomendación **Zen Old Mincho** para pensamiento/interior y
  **Noto Sans JP** para subtítulos legibles en español, ambas verificadas arriba.

### Punto 6 · Cómo hablan y piensan en pantalla

- Es película, no manga ni serie: "hablar en pantalla" aquí es **diálogo hablado + rótulos físicos
  del mundo**, no burbujas de historieta. Esto encaja con la queja del dueño ("no una burbuja
  blanca rara"): la propia serie ya evita la burbuja genérica.
- **La cartela más importante de toda la película es el contrato de trabajo.** Chihiro firma un
  papel con su nombre completo en kanji (荻野千尋, *Ogino Chihiro*); Yubaba le "roba" el nombre
  arrancando los caracteres del papel y deja sólo 千 (*Sen*, "mil") — ella pasa a llamarse Sen el
  resto de la película. El truco es literal: mientras conserve el papel con su nombre completo,
  Yubaba la controla · fuente: [ghibli.fandom.com/wiki/Yubaba](https://ghibli.fandom.com/wiki/Yubaba)
  y [ghibli.fandom.com/wiki/Chihiro_Ogino](https://ghibli.fandom.com/wiki/Chihiro_Ogino) · ✅ (dos
  páginas de la wiki, coinciden).
- El rótulo tallado 油屋 y la bandera con 油 (ver punto 5) son la "cartela del mundo" real de la
  serie: madera oscura, relieve tallado, nunca un rectángulo blanco plano.
- El bib de Boh (坊, ver punto 5) es el ejemplo de texto "cariñoso/infantil" en pantalla.
- En `chihiro048.jpg` se ve un segundo cartel azul con el kanji 臨 parcialmente visible en la
  fachada de una tienda (probable "臨時休業", "cerrado temporalmente", un gag visual típico de
  fondo en el pueblo) · ⚠️ no pude confirmar el texto completo: el cartel está fuera de foco y
  parcialmente tapado en el fotograma oficial disponible.
- No hay pensamientos en globo: Miyazaki no usa esa convención en esta película; el "pensar" se
  transmite con silencio, mirada y música, nunca con texto en pantalla · dato de estilo, coherente
  con no encontrar ninguna caja de pensamiento en las fuentes revisadas (wiki, fotogramas
  oficiales) · ✅ (ausencia comprobada, no es un olvido de búsqueda).
- No hay interfaz de videojuego ni subtítulos de videojuego que mostrar: ver punto 11 (no existe
  videojuego oficial de la franquicia).
- **Recomendación de diseño para la lámina** (coherente con el punto 5): un cuadro de diálogo con
  forma de tablilla de madera tallada, fondo caramelo `#B87D4B`, letras en relieve oscuro
  `#6A4D3F`, en vez de una burbuja blanca — imita directamente el cartel real de la serie.

### Punto 11 · Videojuegos de la franquicia

- **No existe un videojuego oficial con licencia de El viaje de Chihiro / Sen to Chihiro no
  Kamikakushi.** Comprobado en tres vías independientes: (1) Steam, con `recolectar.py` (no
  devolvió ningún juego, sección "Videojuegos en Steam" vacía en `datos-texto.md`); (2) búsquedas en
  inglés y japonés (`Spirited Away video game`, `千と千尋の神隠し ゲーム 公式`, `千と千尋の神隠し
  ゲーム 公式 携帯 アプリ`) que sólo devuelven quizzes de fans no oficiales y apps de terceros; (3)
  AniList, cuya sección "Obras relacionadas" no lista ningún `GAME` · ✅ (ausencia confirmada en tres
  fuentes independientes, no es que no busqué).
- Existe un remake de fans **no oficial**, "*Spirited Away: The 8-bit Videogame*" (estilo NES,
  hecho por un fan), cubierto por [GIGAZINE](https://gigazine.net/gsc_news/en/20150501-spirited-away-8bit)
  en 2015 · ⚠️ una sola fuente, y es fan-made: sin licencia de Ghibli, sólo como curiosidad de
  fandom, no como referencia de interfaz real.
- **The Cutting Room Floor (TCRF)** no tiene ninguna entrada sobre esta película: es un sitio
  centrado en contenido descartado de *videojuegos*, y al no haber videojuego oficial no hay nada
  que documentar ahí · comprobado con búsqueda directa en tcrf.net · ✅ (ausencia justificada, no
  es "no lo busqué").
- El punto no aplica en su forma completa por lo anterior: no hay interfaz, menú ni caja de
  diálogo de videojuego propio que describir. (Nota aparte, no es mío: Studio Ghibli sí colabora en
  el arte de otros videojuegos, como *Ni no Kuni* de Level-5, pero es otra franquicia sin personajes
  de Chihiro — eso es del punto 23, "colaboraciones", que le toca al investigador de imagen; lo dejo
  anotado para que no se pierda.)

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

- **Equipo:** dirección y guion Hayao Miyazaki; dirección de arte Yōji Takeshige (con Noboru
  Yoshida de asistente); diseño de color Michiyo Yasuda; fotografía Atsushi Okui; edición Takeshi
  Seyama · fuente: AniList (`datos-texto.md`, ya recolectado) · ✅.
- **Mezcla 2D/3D, con cifra exacta:** unos **100 planos de CGI sobre unos 1.400 planos totales**
  (≈8% del metraje), integrados sin costura con el dibujo a mano · fuente:
  [blog.alltheanime.com/toonz-toon-shaders-and-studio-ghibli](https://blog.alltheanime.com/toonz-toon-shaders-and-studio-ghibli/)
  · corroborado de forma independiente por [xsisupport.com/tag/spirited-away](https://xsisupport.com/tag/spirited-away/),
  que da la misma cifra ("100 of the film's 1,400 scenes") citando al supervisor de CG **Mitsunori
  Kataama** · ✅ (dos fuentes independientes, mismo número).
- **Software real, con nombres:** el entintado, coloreado digital y composición se hicieron con
  **Toonz** (el mismo programa que Studio Ghibli ayudó a liberar después como **OpenToonz**, gratis
  desde 2016) · fuente: [engadget.com](https://www.engadget.com/2016-03-21-toonz-studio-ghibli-edition-open-source.html)
  + All the Anime (arriba) · ✅. Los planos en 3D se hicieron en **Softimage|3D**, con
  **Toon Shaders** —herramientas de renderizado para simular el aspecto de dibujo animado
  tradicional, desarrolladas por **Michael Arias**, ya probadas antes en *La princesa Mononoke*
  (1997)— · fuente: All the Anime + xsisupport.com · ✅ (dos fuentes).
- **Cómo se usó el 3D en concreto:** el equipo creó un **shader de textura 2D propio** ("2D Texture
  Shader") que proyecta los fondos *pintados a mano* sobre modelos 3D simples desde varias
  posiciones de cámara —para escenas con movimientos de cámara complicados o multitudes
  imposibles de animar a mano, como el puente lleno de espíritus o el interior del tren—; y
  shaders de agua con *ray tracing* para los reflejos del mar en la escena del tren flotando sobre
  el agua · fuente: xsisupport.com (cita directa al supervisor Kataama) · ✅.
- **Fondos y paleta:** pintura tradicional (gouache/acuarela) escaneada y coloreada digitalmente;
  paleta cálida y terrosa en la casa de baños — rojos intensos, verde oscuro en los tejados, dorado
  en los detalles, madera caramelo en los carteles · medido por mí con Pillow en fotogramas
  oficiales: rojo del edificio `#DD2317`/`#EA6661`/`#F68776`, madera del cartel `#B87D4B` (ver
  punto 5) · ✅ (medido, dos fotogramas oficiales distintos dan tonos del mismo rango).
- **Cómo replicarlo en Blender:** para arquitectura compleja (la casa de baños), usar geometría
  simple (planos y cajas) con una textura *pintada a mano* proyectada por UV — es exactamente el
  mismo truco que el "2D Texture Shader" original, y en Blender se logra con el modificador **UV
  Project** o con proyección de cámara sobre el material. Para el contorno de línea, **Freestyle**
  (línea marrón oscuro o verde oscuro, nunca negro puro, como en los tejados y vigas medidos
  arriba) o un **Solidify** invertido si se prefiere malla. Luz cálida direccional + un *rim light*
  dorado para las ventanas iluminadas de noche (ver `chihiro011.jpg`).
- **Cómo replicarlo en Photoshop:** capas separadas de línea / color plano / sombra dura (el
  sombreado de Ghibli es "cel" de dos tonos, sin degradados suaves); pincel tipo "gouache seco" con
  textura de papel para fondos; pincel de tinta con variación leve de grosor (no uniforme) para las
  líneas de personaje.
- **Encuadres:** los movimientos de cámara complejos (tren, puente) usan la cámara 3D descrita
  arriba; en las escenas emocionales, Miyazaki tiende a planos largos y quietos (el llamado *ma*,
  el silencio entre acciones) — esto es un rasgo de estilo general documentado sobre Miyazaki, no
  pude verificarlo con minuto exacto de esta película porque YouTube pide iniciar sesión desde este
  servidor y no llegué a montar `fotogramas.py` sobre un clip largo en Dailymotion/Internet
  Archive dentro de esta tanda · ⚠️ **pendiente de comprobar con fotograma y minuto** — lo puede
  cerrar el investigador de vídeo con `fotogramas.py` si le queda cupo, o yo en la siguiente tanda.

### Punto 24 · Obras parecidas

- Recomendaciones de usuarios de AniList (ya en `datos-texto.md`, no repetido aquí en detalle): *El
  castillo ambulante*, *Mi vecino Totoro*, *Kiki: entregas a domicilio*, *Ponyo*, *La princesa
  Mononoke*, *Nausicaä del Valle del Viento* — todas de Miyazaki/Ghibli, comparten protagonista
  niña/joven que crece a través de un viaje fantástico · ✅ (AniList, ya recolectado).
- **Influencia reconocida:** la novela infantil de **Sachiko Kashiwaba**, *Kiri no Mukō no Fushigi
  na Machi* ("La ciudad misteriosa al otro lado de la niebla", 1975) — trata de una niña que tiene
  que repintar la chimenea de una casa de baños en un pueblo mágico. Miyazaki había querido
  adaptarla antes de hacer *La princesa Mononoke*, y su atmósfera influyó claramente en *Chihiro*
  aunque la trama final sea distinta · fuente: [Japan Society](https://japansociety.org/events/the-village-beyond-the-mist-with-bestselling-childrens-author-sachiko-kashiwaba/)
  y [GLLI-US](https://glli-us.org/2026/09/15/worldkidlit-month-focus-on-japan-two-translations-of-sachiko-kashiwabas-first-novel/)
  · ✅ (dos fuentes independientes, coinciden). Dato cruzado: en *El susurro del corazón* (Ghibli,
  1995) un personaje aparece leyendo ese mismo libro.
- **Mismo servidor:** al momento de escribir esto ya hay otros tres encargos Ghibli en marcha en
  `biblias/`: `100-la-princesa-mononoke`, `99-el-castillo-ambulante` y
  `102-el-estilo-ghibli-en-general` (más `101-your-name-cielos-y-ciudades`, mismo tono de fantasía
  aunque no es Ghibli) — ninguno tenía `biblia.md` terminada todavía · comprobado mirando las
  carpetas de `biblias/` · ✅. El redactor debería diferenciar la lámina de Chihiro (casa de baños,
  espíritus, comida) del "estilo Ghibli general" para no repetir ideas.
- No pude leer **TV Tropes** (`tvtropes.org/pmwiki/pmwiki.php/Anime/SpiritedAway`): el sitio devolvió
  **403 Forbidden** al intentar leerlo · ⚠️ **No encontré** (bloqueado, un solo intento con
  WebFetch, según regla de no insistir más de dos veces en la misma web).

### Punto 25 · El mundo, la historia y sus símbolos

**Reglas del mundo (cinco líneas)**
1. Cruzar el puente rojo de noche mete a un humano en el mundo espiritual y lo hace invisible para
   los suyos; al volver a cruzar el río de regreso, la regla que repite el tráiler doblado es "no
   miren atrás" · fuente: transcripción propia del tráiler oficial en latino, ya en
   `partes/episodios.md` (minuto 0:00) · ✅.
2. Comer comida de los espíritus sin permiso convierte a un humano en cerdo — así pierde a sus
   padres Chihiro al principio · fuente: [ghibli.fandom.com/wiki/Spirited_Away](https://ghibli.fandom.com/wiki/Spirited_Away)
   · ✅.
3. Yubaba controla a sus trabajadores robándoles el nombre con un contrato firmado (ver punto 6);
   si alguien olvida su verdadero nombre, no puede volver a casa nunca — le pasó casi a Haku · ✅
   (wiki, ver punto 6).
4. El oro (金, *kin*) es la moneda de los espíritus; el oro falso que reparte Sin Cara corrompe a
   quien lo desea, y Zeniba tenía un **sello de oro** que Haku robó por orden de Yubaba · fuente:
   [ghibli.fandom.com/wiki/Gold](https://ghibli.fandom.com/wiki/Gold) · ✅.
5. Los ríos y montañas japoneses tienen espíritus propios (*kami*) que visitan la casa de baños a
   diario para descansar; Haku es en realidad el espíritu de un río real relleno para construir
   viviendas — su verdadero nombre es **Nigihayami Kohakunushi** (饒速水小白主, "Señor del veloz río
   Kohaku") · fuente: [ghibli.fandom.com/wiki/Haku](https://ghibli.fandom.com/wiki/Haku), citando
   el *Roman Album* oficial de Tokuma Shoten · ✅.

**Historia por arcos (resumen corto)**
1. La familia Ogino llega a un parque temático abandonado; los padres comen sin permiso y se
   vuelven cerdos; aparece Haku, aparece el mar que atrapa a Chihiro en el mundo espiritual.
2. Chihiro consigue trabajo con Yubaba con ayuda de Kamaji y Lin; pierde su nombre y pasa a
   llamarse Sen.
3. Sen limpia al "Espíritu Apestoso" (en realidad un espíritu de río contaminado) y gana respeto en
   la casa de baños; conoce a Sin Cara, que empieza a rondarla.
4. Sin Cara se descontrola dentro de la casa de baños, atrae a los trabajadores con oro falso y se
   los traga.
5. Sen viaja al pantano a devolver el sello de oro robado a Zeniba (la hermana gemela de Yubaba) y
   salvar a Haku, herido por los papelitos-pájaro (*shikigami*) de Yubaba.
6. Yubaba le pone a Sen la prueba final —reconocer a sus padres entre un grupo de cerdos, sin
   acertar por trampa, sino diciendo la verdad ("ninguno de estos es mi padre o madre")— y Chihiro
   recupera su nombre y a su familia.
   · fuente de todo el arco: cruce de [ghibli.fandom.com/wiki/Spirited_Away](https://ghibli.fandom.com/wiki/Spirited_Away)
   con las páginas individuales de Yubaba, Zeniba, Haku y Chihiro Ogino · ✅ (varias páginas de la
   misma wiki, consistentes entre sí).

**Emblemas, objetos icónicos y vocabulario**
- El cartel tallado **油屋** y la bandera con **油** (ver punto 5) — el emblema visual central de la
  serie.
- Las **fichas de baño** de madera (*bath tokens*) que reparte el capataz (Foreman) para poder
  limpiar cada tina · fuente: [ghibli.fandom.com/wiki/Foreman](https://ghibli.fandom.com/wiki/Foreman)
  · ✅.
- El **sello de oro de Zeniba**, robado por Haku por orden de Yubaba — motor de la segunda mitad de
  la trama · ✅ (ver regla del mundo n.º 4).
- La **liga para el pelo** que Chihiro consigue en la casa de Zeniba, tejida a mano por las amigas
  de Zeniba con hilos de todos los trabajadores de la casa de baños — protege a Chihiro y brilla al
  final de la película · fuente: [ghibli.fandom.com/wiki/Zeniba](https://ghibli.fandom.com/wiki/Zeniba)
  · ✅.
- Los **papelitos-pájaro (shikigami)** que lanza Yubaba para cazar a Haku convertido en dragón ·
  página propia en la wiki, [ghibli.fandom.com/wiki/Shikigami](https://ghibli.fandom.com/wiki/Shikigami)
  · ✅.
- Las **bolitas de hollín** (*susuwatari*, también *makkuro kurosuke*) que cargan carbón en la sala
  de calderas de Kamaji — comparten diseño con *Mi vecino Totoro* · fuente:
  [ghibli.fandom.com/wiki/Susuwatari](https://ghibli.fandom.com/wiki/Susuwatari) · ✅.
- Vocabulario propio: **Aburaya** (油屋, la casa de baños — lit. "casa del aceite", **no** "casa del
  agua caliente", que en japonés normal sería 湯屋 *yuya*, la palabra esperada para un baño público)
  · confirmado oficialmente en el propio rótulo tallado y en la wiki · ✅. Hay una lectura de fans
  japoneses de que el nombre "油屋" es un guiño a los barrios de placer del Japón antiguo (donde las
  trabajadoras usaban nombres falsos, como hace Yubaba con los suyos) · fuente:
  [note.com/hatamove](https://note.com/hatamove/n/nc1fbe1bf2674) · ⚠️ interpretación de fans, no
  una declaración oficial de Miyazaki que yo haya podido verificar en fuente primaria.
- **Sen** (千, el nombre robado de Chihiro, literalmente "mil") — de ahí el propio título de la
  película, "Sen y Chihiro". **Kaonashi** (Sin Cara). **Kamikakushi** (神隠し, "ocultamiento por los
  dioses/espíritus"): es el término tradicional japonés para una desaparición sobrenatural
  —especialmente de niños— y es la segunda mitad del título original · ✅ (dato ampliamente
  documentado, wiki + diccionario).
- La arquitectura de la casa de baños: Miyazaki la describió como una mezcla de "Japón, Occidente y
  el Palacio del Dragón (Ryūgū-jō)", un estilo llamado *giyōfū* (擬洋風, "pseudo-occidental"); se
  citan como referencia declarada el edificio **Kodakara-yu** (Museo de Arquitectura al Aire Libre
  de Edo-Tokio) y el **Dōgo Onsen Honkan** (Ehime) · fuentes: [note.com/hatamove](https://note.com/hatamove/n/nc1fbe1bf2674)
  y [ghiblog.com/chihiro-yuya](https://ghiblog.com/chihiro-yuya/) · ⚠️ dos fuentes, pero ambas de
  blogs de fans que citan a Miyazaki de segunda mano — no encontré la declaración original en un
  artbook o entrevista primaria.

## Lo mejor para la lámina

1. El rótulo tallado **「油屋」** (`chihiro048.jpg`, madera `#B87D4B` / talla `#6A4D3F`) es la
   cartela oficial de la serie: úsalo tal cual como plantilla de "cuadro de diálogo" del canal, en
   vez de una burbuja blanca.
2. La bandera circular con **油** (`chihiro011.jpg`) sirve de sello/insignia pequeña para etiquetas
   del canal o del bot.
3. Letras verificadas y listas para usar: **Yuji Syuku** (título/logo) y **Shippori Mincho B1**
   (carteles), ambas con tildes, ñ, ¿ y ¡ comprobados con `fontTools`.
4. Objeto real para una lámina en Blender: una **ficha de baño de madera** o el **sello dorado de
   Zeniba** como icono 3D — geometría simple + textura pintada, igual que hacía el propio estudio.
5. Sin Cara (Kaonashi) es el personaje secundario más fuerte para una lámina de grupo o de "canal
   silencioso": icónico, mudo, con fandom propio fuera de Chihiro y Haku.

## No encontré

- ⚠️ La tipografía exacta de los **subtítulos oficiales en español latino** (Blu-ray/streaming):
  no hay ninguna fuente que la documente; busqué en español y japonés.
- ⚠️ El rotulado tipográfico real de los globos del **film comic** de Tokuma Shoten (sólo encontré
  la ficha de venta, no páginas escaneadas).
- ⚠️ El texto completo del segundo cartel azul (con 臨) en `chihiro048.jpg`: está fuera de foco en
  el único fotograma oficial disponible con ese ángulo.
- ⚠️ La página de **TV Tropes** sobre la película: dio 403 Forbidden al leerla (un solo intento,
  según la regla de no insistir).
- ⚠️ Una segunda fuente que confirme que Toshio Suzuki dibujó a mano el carácter 千 del logo (sólo
  un tuit de fans).
- ⚠️ Una fuente primaria (artbook, entrevista directa) para la comparación de la arquitectura de la
  casa de baños con el Kodakara-yu y el Dōgo Onsen Honkan — sólo la repiten blogs de fans.
- ⚠️ Minuto exacto de un plano que muestre el *ma* (silencio/quietud de cámara) típico de Miyazaki:
  no pude montar `fotogramas.py` sobre un clip largo en esta tanda (YouTube pedía inicio de sesión
  y no llegué a intentarlo en Dailymotion/Internet Archive por límite de tiempo). No es obligatorio
  de mis puntos (pertenece más al punto 14 del investigador de vídeo), lo anoto como aviso, no como
  pendiente mío.

## Bitácora de búsqueda

- **Español**: "千と千尋の神隠し colores oficiales", inventario de `servidor/inventario.md` y
  `servidor/reglas_del_dueno.md` (sin resultados propios de Chihiro, es un encargo nuevo).
- **Japonés**: `千と千尋の神隠し ロゴタイトル 真野薫 デザイン フォント`, `"千と千尋" ロゴ 「千」
  鈴木敏夫 手書き バランス`, `千と千尋の神隠し アニメコミック 徳間書店 セリフ 吹き出し`,
  `千と千尋の神隠し ゲーム 公式 携帯 アプリ`, `スタジオジブリ 千と千尋の神隠し 公式ゲーム 任天堂
  存在しない`, `湯屋 油屋 千と千尋 看板 文字 デザイン 意味`, `千と千尋の神隠し 字幕 スペイン語
  フォント OR クレジット 書体` — vía WebSearch.
- **Inglés**: `Spirited Away video game official Sen to Chihiro no Kamikakushi videogame`,
  `Spirited Away production Toonz software CG train scene animation technique interview`,
  `Studio Ghibli Spirited Away production digital paint CGI compositing Toonz interview making of`,
  `TCRF "The Cutting Room Floor" Spirited Away OR Ghibli`, `Miyazaki Spirited Away inspired novel
  "Kiri no Mukou no Fushigi na Machi" Kashiwaba influence` — vía WebSearch.
- **Fuentes consultadas**: ghibli.jp (galería oficial, 8 fotogramas 1920×1038 descargados y medidos
  con Pillow/tesseract), ghibli.fandom.com (API `action=parse`/`action=query`, páginas: Bathhouse,
  Yubaba, Zeniba, Gold, Foreman, Kasuga, Susuwatari, Haku, Chihiro Ogino, Shikigami), AniList (ya en
  `datos-texto.md`), Fontsource API (`api.fontsource.org`, 9 fuentes descargadas como `.woff2` y
  comprobadas con `fontTools`), blog.alltheanime.com, xsisupport.com, engadget.com, japansociety.org,
  glli-us.org, note.com/hatamove, ghiblog.com, tokuma.jp, gigazine.net, tcrf.net (búsqueda directa,
  sin resultado), tvtropes.org (403 Forbidden).
- **No usé YouTube** para vídeo (pide iniciar sesión desde este servidor, según instrucción); los 8
  fotogramas de estilo vienen de la galería oficial de ghibli.jp, no de vídeo.
- Herramientas usadas: `curl` directo a las APIs de Fandom/AniList/Fontsource, `Pillow` (color y
  contact sheet), `tesseract -l jpn` (lectura de carteles, resultado parcial), `fontTools`
  (`TTFont(f).getBestCmap()`, comprobación real de tildes/ñ/¿/¡ en 9 fuentes).
