# Texto, juegos y técnica · Sailor Moon (investigador de texto — puntos 5, 6, 11, 18, 24, 25 de ENCARGO.md)

Parte de `partes/datos-texto.md` (AniList, staff, obras parecidas de usuarios, IDs de arcos).
Es libreta de datos: un dato por línea, con fuente, ✅ (dos fuentes) o ⚠️ (una fuente o de memoria).

---

## Punto 5 · Tipografía (logo, globos, juegos — una letra por uso)

Fuente base: gráfico **"Fonts and Typefaces Used in Sailor Moon"** de la usuaria de DeviantArt `the-sweet` (2013), recopilado con la comunidad de SailorMoonForums/GenVid y enlazado desde "Sailor Moon Font List" de KinnoHitsuji · imagen vista y medida (1280×498) en `sm_fonts.jpg` (guardada en mi carpeta de trabajo). Es la única fuente que identifica letra por letra las tipografías **reales** usadas en las ediciones en inglés (Kodansha USA actual, Mixx/Tokyopop años 90-2000, y el logo del anime en inglés). Para el original japonés no encontré quién diseñó el logotipo a mano (ver «No encontré»).

- **Logo/título** (letras reales del logo del anime en inglés): **Birch**, **Matrix Slant** y **Matrix Tall** (de pago) ✅ — coincide con una búsqueda independiente que identifica "Matrix II" y "Birch" para el mismo logo (dafont forum + textstudio) → dos fuentes.
  - Libre equivalente: **Luckiest Guy** (Google Fonts, OFL) — display redondeada con panza, parecida a Birch/Occidental. Verificada con fontTools (`fontTools.ttLib`, `getBestCmap()`): trae á é í ó ú ñ Ñ ¿ ¡ ü.
- **Logo "Pretty Guardian"** (portada de la reedición y del live action), y créditos de "Naoko Takeuchi" en la reedición: **Occidental** (de pago) ✅ (mismo gráfico).
- **"Sailor Moon" en la página de contenidos** de la edición Kodansha actual: **Harrington** (de pago) ✅.
- **Título del logo del manga** (letras del rótulo "Sailor Moon" de Kodansha): **Shardee** y **Calfon no.540 Swash Alternative** (de pago) ✅.
- **Globo normal** (diálogo del manga, edición Kodansha USA actual — la que se vende hoy): **CC Comicrazy Roman** (Comicraft, de pago) ✅.
  - Libre equivalente 1 (recomendada): **Coming Soon** (Google Fonts, OFL) — lettering casual de cómic. Verificada con fontTools: trae **todas** las tildes/ñ/¿/¡.
  - Libre equivalente 2, más parecida a simple vista pero con un problema real: **Anime Ace 2.0 BB** (Blambot, vía FontSpace) — la usan casi todas las demás biblias de este proyecto para manga. **La descargué y la comprobé yo misma con fontTools** (`AnimeAce20Bb-K97.ttf`, `AnimeAce20BbBold-2Av.ttf`, `AnimeAce20BbItalic-vlA.ttf`): **sí trae** á é í ó ú ñ Ñ ü, pero **no trae ¿ ni ¡** (no hay glyphs `questiondown`/`exclamdown` en ninguno de los tres archivos, comprobado con `getGlyphOrder()`). Además su licencia es «Freeware, Non-Commercial» (no es de uso libre comercial). ⚠️ **Esto matiza lo que dice la guía general `_Cuadros de dialogo por franquicia`**, que la da como «con tildes» sin comprobar los signos de apertura — en español hacen falta los dos. Para Sailor Moon recomiendo **Coming Soon** como opción principal por esto.
- **Diálogo del manga, edición Mixx/Tokyopop** (primera edición en inglés, años 90-2000): **Cassia** y **Mercurius Script MT** (de pago) ✅.
- **Títulos de acto/capítulo** (edición Kodansha): **Kabel** (de pago, geométrica tipo Bauhaus) ✅.
  - Libre aproximada: no hay clon exacto de Kabel; la más cercana que verifiqué es **Montserrat** ExtraBold (Google Fonts, OFL) — geométrica, con tildes/ñ/¿/¡ verificadas.
- **"Contents" de la reedición del manga**: **Courier New** (de pago pero muy extendida) ✅.
  - Libre: **Special Elite** (Google Fonts, máquina de escribir) ya verificada con tildes/ñ/¿/¡ completas (uso también recomendado abajo para subtítulos/interfaz retro).
- **Los artbooks** (Materials Collection y siguientes): **Eddacaps** (de pago, mayúsculas gruesas) ✅.
  - Libre aproximada: **Fredoka** Bold (Google Fonts, redondeada gruesa), verificada con fontTools.
- **Cartelas de episodio del doblaje en inglés** (temporadas 1-2, Cloverway): **"Heatwave"** (de pago/donationware) ✅.
  - Alternativa libre encontrada pero **sin verificar con fontTools** (no la descargué: es de baja prioridad) ⚠️: "Heat Wave" de Xerographer Fonts, dafont, donationware. Recomiendo en su lugar **Yellowtail** (Google Fonts, script fluido), ya verificada con todas las tildes/ñ/¿/¡, como aproximación seguramente libre al aire "de pincel ochentero".
- **Grito**: no encontré una fuente identificada para el grito específicamente (en manga occidentalizado el grito suele ir en el mismo lettering pero más grande/negrita, convención estándar de "Manga iconography", Wikipedia) ⚠️.
  - Libre propuesta: **Bangers** (Google Fonts, OFL, mayúsculas de impacto), verificada con fontTools: tildes/ñ/¿/¡ completas.
- **Pensamiento**: un comentario recogido en la búsqueda (no pude verificar el archivo de fuente ni una segunda fuente) dice que el diálogo de pensamiento en Sailor Moon usó la tipografía **"OH-no.2"** ⚠️ (una sola fuente, sin poder comprobarla yo misma).
  - Libre propuesta, visualmente cercana a la cursiva caligráfica real "Apple Chancery" (la del "Pretty Guardian" de contenidos): **Mrs Saint Delafield** (Google Fonts), verificada con fontTools: tildes/ñ/¿/¡ completas.
- **Onomatopeya** (japonés original, dibujada a mano en katakana, no es "una fuente" — convención estándar del manga japonés) ✅ (Wikipedia: Manga iconography).
  - Libre para imitar el trazo a pincel japonés: **Yuji Syuku** (Google Fonts, OFL), verificada con fontTools: tildes/ñ/¿/¡ completas (además cubre japonés).
- **Cartel del mundo** (letreros dentro de la ficción): visto directamente en un panel del manga (`gamecentercrown_manga.png`, 379×480, de sailormoon.fandom.com) el rótulo vertical **「クラウンゲームセンター」** (Crown Game Center) en katakana grueso, sobre la fachada del edificio con textura de screentone de puntos ✅ (imagen propia).
  - Libre para letreros con texto japonés: **DotGothic16** (Google Fonts, gótica de píxel), verificada con fontTools: tildes/ñ/¿/¡ completas.
- **Interfaz de videojuego**: visto directamente en el HUD del «juego de Sailor V» ficticio dentro de la propia serie (`sailorvgame.jpg`, 225×169, de sailormoon.fandom.com): arriba a la izquierda **"NEXT 00"**, arriba a la derecha **"SCORE: 25080"**, en una tipografía blanca de trazo simple con contorno oscuro, sobre fondo morado de sala arcade ✅ (imagen propia).
  - Libre para ese HUD retro: **Press Start 2P** (Google Fonts, OFL) — **la descargué y verifiqué con fontTools**: sí trae tildes/ñ/¿/¡ completas. ⚠️ Esto corrige a la guía general del proyecto, que la daba «probablemente con acentos, por comprobar» sin comprobarlo.
- **Subtítulos/créditos** (streaming actual de Sailor Moon Crystal en Crunchyroll/Netflix Latinoamérica): tipografía sans estándar de cada plataforma, no propia de la serie; no la medí en un fotograma esta tanda ⚠️.
  - Libre neutra recomendada: **Montserrat**, ya verificada.

---

## Punto 6 · Cómo hablan y piensan en pantalla (el más importante — nada de burbuja blanca genérica)

- Convención general de globo de manga: arco sólido desde la cabeza para el habla; fila de círculos pequeños en vez del arco para el pensamiento (o para susurrar) ✅ (Wikipedia: *Speech balloon*, *Manga iconography*).
- El manga original de Takeuchi es en blanco y negro, con mucho **screentone de puntos** para sombrear fachadas, cielo y pelo — visto directamente: la fachada del Game Center Crown lleva screentone punteado uniforme y las barandas llevan trama de rayas finas (`gamecentercrown_manga.png`) ✅ (imagen propia).
- El «brillo» de Takeuchi: ella misma cuenta que **rociaba corrector líquido sobre el manga para que pareciera que brilla** («Spray correction fluid on to make the manga look sparkly») ✅ (entrevista larga de 50 preguntas + comentarios sobre 20 piezas de una exposición, recopilada en inglés en brickme.tumblr.com). Se ve aplicado como rayitas finas que irradian de un objeto brillante: la supercomputadora de Mercury al abrirse lleva justo ese efecto alrededor (`mercury_supercomputer.gif`, 280×226) ✅ (imagen propia, coincide con la técnica descrita → dos fuentes).
- **Objeto-interfaz más icónico de la franquicia — la Supercomputadora de Mercury** (Super Computer / Mini-Data Computer, スーパー・コンピューター): aparato plegable turquesa tipo agenda/teléfono con teclado completo, que analiza el entorno y busca puntos débiles del enemigo; se la dio Luna ✅ (sailormoon.fandom.com, wikitext del ítem). Dato con fuente oficial citada por la wiki: en el **Materials Collection** (artbook oficial) la propia Naoko Takeuchi dice que la pantalla muestra información «al estilo de The Terminator»; y en un episodio del anime la pantalla mostró, de broma, las tres Directivas Primarias de RoboCop ⚠️ (un solo sitio —la wiki— aunque cita directamente el artbook oficial; no pude ver la página del artbook yo misma).
- **Mercury Visor** (マーキュリー・ゴーグル): visera transparente azul, pantalla tipo *head-mounted display* que le muestra información directamente en el campo de visión; aparece al tocarse el pendiente; sale en manga, anime 90s, Crystal y los musicales (Sera Myu) ✅ (sailormoon.fandom.com, wikitext).
- **El «juego de Sailor V»**, un elemento narrativo dentro de la propia historia (un arcade de pelea lateral que Artemis programó para entrenar a Minako sin que ella lo supiera): su HUD real dentro de la ficción muestra "NEXT 00" y "SCORE: ####" arriba, en blanco simple sobre fondo oscuro morado de discoteca (`sailorvgame.jpg`) ✅ (imagen propia). La frase **«GAME ENDLESS»** aparece en pantalla cuando se abre la puerta secreta hacia el Centro de Mando Lunar escondido bajo la máquina ✅ (sailormoon.fandom.com, sección Trivia de *Sailor V (video game)*).
- **Eyecatch** (cartela de corte a publicidad): en la primera temporada, un foco recorre un fondo estrellado, ilumina a Luna y luego a Sailor Moon de espaldas mientras una voz dice «Sailor Moon!» y aparece el logo de temporada al girar ella; la voz suena «masculina» antes del corte y «femenina» después. En Sailor Moon R cambia: las Guerreras Interiores en versión chibi saltan una a una a la pantalla y posan mientras se oye «Sailor Moon R!» ⚠️ (un solo resultado de búsqueda; no pude leer WikiMoon.org directamente —dio 403/Cloudflare tanto por WebFetch como por curl directo, dos intentos cada vez—).
- **Videojuego con la caja de diálogo más "clásica"**: *Bishōjo Senshi Sailor Moon* (PC Engine/TurboGrafx-CD, Banpresto, 1994) es una **novela visual** — el formato con caja de texto más parecido a un videojuego de diálogo de toda la franquicia (texto abajo, retrato del personaje) ✅ (Wikipedia: *List of Sailor Moon video games*), pero no vi una captura real de esa caja (⚠️ diseño exacto sin confirmar).
- **No pude entrar a Game UI Database** (`gameuidatabase.com`, capturas reales de HUD de videojuego que sí usa la guía general del proyecto para otras franquicias) ni a **The Cutting Room Floor** (`tcrf.net`): ambas dan reto de Cloudflare («Just a moment...») tanto por WebFetch como por curl con distintos user-agents, y lo intenté dos veces cada una antes de desistir, como marca AYUDANTE.md.

---

## Punto 11 · Videojuegos de la franquicia (interfaz, menús, cajas de diálogo)

Fuente principal: Wikipedia *List of Sailor Moon video games* + páginas individuales de sailormoon.fandom.com (dos fuentes que coinciden en fechas/plataformas) ✅ salvo donde se marca lo contrario.

| Juego | Plataforma / año | Género · nota de interfaz |
|---|---|---|
| Bishōjo Senshi Sailor Moon | Super Famicom, Angel, 27-ago-1993 | Beat 'em up de scroll lateral: golpes, patadas y especiales |
| Bishōjo Senshi Sailor Moon R | Super Famicom, Angel, 29-dic-1993 | Secuela directa, mismo género |
| Bishōjo Senshi Sailor Moon S: Jōgai Rantō!? Shuyaku Sōdatsusen | Super Famicom, 1994 | Pelea 1 vs 1, con modo historia, torneo y versus |
| Bishōjo Senshi Sailor Moon: Another Story | Super Famicom, Angel, 1995 | **El único RPG por turnos «clásico»** de la franquicia; traducción de fans al inglés actualizada en 2019 (sailormoonnews.com) |
| Bishōjo Senshi Sailor Moon S | Game Gear, Bandai, 27-ene-1995 | Pelea 2D; traducción de fans al inglés en 2019 (sailormoonnews.com). TCRF documenta texto y gráficos sin usar, pero no pude leer la página (403 Cloudflare) ⚠️ |
| Bishōjo Senshi Sailor Moon | PC Engine/TurboGrafx-CD, Banpresto, 1994 | **Novela visual**: caja de texto abajo + retrato — el formato de diálogo más «de videojuego clásico» de la saga ⚠️ (diseño exacto sin captura propia) |
| Pretty Soldier Sailor Moon | Arcade, Banpresto, 1995 | Beat 'em up a 4 jugadores. TCRF lo describe (en el resumen del buscador) como «un juego apresurado, mina de oro de contenido sin usar» ⚠️ (no pude leer la página completa, 403) |
| Bishōjo Senshi Sailor Moon SuperS: Shin Shuyaku Sōdatsusen | PlayStation, 1996 | Pelea, con reparto de hasta 20 puntos para subir atributos de cada personaje |
| Quiz Bishōjo Senshi Sailor Moon | Arcade, 1997 | Trivia con diálogo |
| Sailor Moon Drops | Móvil iOS/Android, Beeline Interactive/Bandai Namco | Puzzle de combinar-3; cerrado a nivel internacional el 28-mar-2019 |
| Sailor Moon: La Luna Splende / La Luna Brilla | Nintendo DS, 2011 | El único juego de la franquicia con **localización europea** (italiano) |
| 3D Adventures of Sailor Moon | Sin publicar/cancelado | Documentado por TCRF con texturas sin usar y un modelo 3D inacabado de Sailor Moon — dato de interés para el punto 18/23, pero **una sola fuente** (resumen de buscador, TCRF no se pudo leer directo) ⚠️ |

- **El «juego de Sailor V» dentro de la ficción** no es un producto real (ver punto 6): es la excusa narrativa de por qué Minako/Sailor V ya sabía pelear. El arcade real más cercano en nombre y época es *Pretty Soldier Sailor Moon* (Banpresto, 1995).
- No encontré videojuego oficial «activo» hoy (2026) más allá de relanzamientos retro y traducciones de fans; *Sailor Moon Drops* está cerrado desde 2019 ⚠️ (no es obligatorio del punto, lo dejo como dato de contexto).

---

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Materiales reales de Naoko Takeuchi**, declarados por ella misma (entrevista larga de 50 preguntas + comentarios sobre 20 piezas de una exposición, recopilada en inglés en brickme.tumblr.com) ✅:
- Lápiz mecánico de 0.5 mm, dureza H; papel de manga de marca propia para el trazo.
- Para las ilustraciones a color combina, según la pieza: tinta de color, marcadores, rotulador, color poster, aerógrafo/spray de color y **screentone** (tramas adhesivas), sobre distintos papeles: Kent fino, Canson, papel japonés con estampado **«Unsai»** (motivo de porcelana china) y papel Classico Fabriano.
- Truco de brillo: **rocía corrector líquido** sobre el dibujo para que parezca que brilla (ver ejemplo real en punto 6).
- Siempre piensa de dónde viene la luz antes de dibujar.
- Trabajó como asistente aplicando **screentone** en el primer tomo de *Hunter × Hunter*, de su esposo **Yoshihiro Togashi** — la misma técnica de trama que usa en su propio manga ✅ (Wikipedia: *Naoko Takeuchi*) → dos fuentes con lo anterior.
- Formación: química farmacéutica (Kyoritsu College of Pharmacy), como plan por si el manga no funcionaba ✅ (Wikipedia).

**Estilo general** (CBR, «Why Does The Art in the Sailor Moon Franchise Hold Up So Well?») ✅:
- Cuerpos larguiruchos, pelo larguísimo, ojos grandes y expresivos, ropa «de pasarela»; inspirado en alta costura (Dior, Mugler), cuentos de hadas y mitología. Los trajes sailor están basados en el propio uniforme escolar de Takeuchi.
- El anime de los 90 (Toei) usa **animación en cel de plástico tradicional**, con las ilustraciones a color de Takeuchi como referencia directa de paleta. Paleta de Tokio: «azul pálido brumoso, verde azulado (teal) y lila», que conecta visualmente la ciudad moderna con el Reino Lunar celestial.
- El estilo cambia por arco: el arco del Reino Oscuro mete horror cósmico («eldritch») con youmas grotescos; el arco SuperS (Dream/Circo de la Luna Muerta) adopta una estética de cuento de hadas más suave, trazo delicado y tonos pastel.

**Equipo creativo** (AniList, ya en `datos-texto.md`, cruzado con Wikipedia) ✅:
- Dirección de arte: Tadao Kubota (eps. 1-26) → Takamura Mukuo (eps. 27-46).
- Diseño de personajes: Kazuko Tadano (serie original) → **Ikuko Itoh**, desde Sailor Moon S (1994) hasta el final de SuperS (1995) (Wikipedia: *Ikuko Itoh*).
- Animador clave recurrente 1992-1996: **Katsumi Tamegai** (Wikipedia).

**Sailor Moon Crystal (2014-)**: reboot fiel al manga, animación **digital/CGI**, mantiene diseños y paletas de Takeuchi ✅ (CBR). Las primeras temporadas usaron mucho CGI 3D en las transformaciones y generaron rechazo de fans acostumbrados al dibujo a mano (se describieron como «muñecas de goma estiradas para que les quede el traje») ⚠️ (una fuente escrita —screenrant.com— aunque es un hecho muy repetido en reseñas de MyAnimeList que aparecieron en la misma búsqueda). Desde la 3ª temporada se quitó el CGI de las transformaciones y volvió la animación tradicional. Para las películas *Eternal* y *Cosmos* se suma **Studio DEEN** junto a Toei; **Kazuko Tadano** retoma el diseño de personajes, relevando a Akira Takahashi (que lo llevó en la 3ª temporada) ✅ (comicbook.com + Wikipedia: *Sailor Moon Eternal*).

**Cómo replicarlo en Photoshop** (traducción práctica de lo anterior, no es cita textual de ninguna fuente):
- Línea: entintado manga clásico, fino y limpio (no de grosor muy variable); pincel tipo «G-Pen» en Photoshop/Clip Studio.
- Sombreado: capa con patrón de medios tonos (Filtro → Píxelado → Color Halftone, o una trama de puntos importada) en modo Multiplicar sobre el color plano, para imitar el screentone.
- Brillo: rayitas finas blancas radiales alrededor de un objeto u ojo, a mano o con un pincel de «destello», imitando el corrector líquido de Takeuchi.
- Paleta: azul pálido/teal/lila para Tokio; blanco y dorado con destellos para el Reino de la Luna.
- Para el estilo Crystal (actual, digital): línea vectorial limpia y color plano con degradados sutiles, casi sin textura de papel.

**En Blender**: contorno con el modificador **Solidify** invertido (grosor uniforme tipo cel) o **Freestyle**, más un *shader* Toon (nodo Shader to RGB + Color Ramp de 2-3 bandas) para las sombras — la misma receta que usan otras biblias de este proyecto para series de cel-shading. No encontré esta tanda modelos o *rigs* 3D con licencia libre verificada de Sailor Moon en Sketchfab (⚠️ no es mi punto directo —eso es del investigador de imagen, punto 3— pero lo anoto porque toca el 18).

**Encuadres y composición**: no encontré una fuente dedicada (entrevista de storyboard, making of) sobre planos y ángulos típicos de la serie ⚠️ — es lo más flojo de este punto; lo dejo pendiente.

---

## Punto 24 · Obras parecidas y temas relacionados

- Recomendaciones de usuarios de AniList (ya listadas en `datos-texto.md`, no repetidas aquí: Cardcaptor Sakura, Revolutionary Girl Utena, Princess Tutu, Magical DoReMi, Tokyo Mew Mew, Kamikaze Kaitou Jeanne, InuYasha, Magic Knight Rayearth, Yu Yu Hakusho, Puella Magi Madoka Magica, Heartcatch Precure!, Shugo Chara!, Precure, Fushigi Yugi).
- **Influencias que la propia Takeuchi reconoció** (página *«Influences that inspired Codename Wa Sailor V/Sailor Moon»* en sailormoon.fandom.com, la wiki oficial que recomienda el encargo) ✅:
  - **Bishoujo Kamen Poitrine** (tokusatsu de acción real, finales 80-90): heroína enmascarada con una hermana chibi que se une después con varita-espada muy parecida al Moon Kaleidoscope de Sailor Moon/Chibi Moon.
  - **Sailor Suit Rebel Alliance** (セーラー服反逆同盟, 80s): colegialas de uniforme marinero con poderes espirituales (lanzar rosas como dardos, cadenas de oro) contra profesores corruptos, con grandes batallas grupales.
  - **Himitsu no Akko-chan** (1969-70): niña con espejo mágico que la transforma en lo que quiera.
  - **Warrior of Love Rainbowman** (1972): el mismo canal japonés que después emitiría Sailor Moon; el traje del héroe se parece al de Moonlight Knight/Mamoru.
  - **Cutie Honey** (1973-74): las frases iniciales de Sailor V se parecen a la coletilla de Cutie Honey.
  - **Majokko Megu-chan** (1974-75): maga pelirroja altiva que compite contra su rival de pelo azul por el trono de la Reina Mágica.
  - **The Rose of Versailles** (1979-80): Lady Oscar inspira a las princesas guerreras que protegen la galaxia en nombre del Milenio de Plata; su amor prohibido es paralelo al de Endymion y Serenity; **Sailor Uranus está inspirada directamente en Lady Oscar** (mujer que viste y pelea como hombre) — confirmado también en un artículo dedicado, CBR *«Rose of Versailles Sailor Moon similarities»* ✅ → dos fuentes.
  - **Wonder Woman** (serie de TV, 1975) inspiró que casi todas las guerreras luchen en tacón de aguja ⚠️ (una sola fuente, la misma wiki).
- **Inspiración de estilo de dibujo**: **Leiji Matsumoto** (creador de *Galaxy Express 999*), según la propia Takeuchi en una entrevista de 1996 para la revista *Animerica* — aunque ella misma se distancia porque «las mujeres de Matsumoto son todas adultas y sexis» ✅ (recogido en Wikipedia, con cita directa a Animerica 1996).
- **Origen editorial**: tras publicar el manga *Maria*, Takeuchi quería un manga de «chicas peleadoras del espacio»; su editor **Fumio Osano** sugirió vestir a la protagonista con uniforme marinero → nace *Codename: Sailor V*, luego ampliado a 5 guerreras para la adaptación a anime de Toei ✅ (Wikipedia: *Naoko Takeuchi*).
- **Qué otras láminas del servidor se le parecen** (revisé las 41 carpetas de `biblias/` ya creadas, encargos 01 a 42 menos el propio 38): **ninguna es una serie mahou shoujo/shoujo clásica de los 90** — no hay Cardcaptor Sakura, Precure ni nada similar entre los encargos activos. Lo más cercano en tono es Oshi no Ko, pero es idol/drama, no mágico ✅ (comprobación interna, listado de carpetas, no es fuente externa). Es una buena noticia: la lámina de Sailor Moon no repetiría estética con ninguna otra ya encargada.
- **Cruce real con otra serie de este mismo proyecto**: Takeuchi fue asistente de screentone de su esposo **Yoshihiro Togashi** en el primer tomo de *Hunter × Hunter* (biblias/36-hunter-x-hunter) ✅ (Wikipedia) — dato de sabor, no de parecido de tono, pero verificable y curioso para un post cruzado.

---

## Punto 25 · El mundo, la historia y sus símbolos

Fuente principal: sailormoon.fandom.com (wiki oficial recomendada por el encargo), leída por su API (`action=query&prop=revisions&rvslots=main`, wikitext crudo) — cada ítem cruzado con Wikipedia o con AniList donde se pudo, marcado abajo.

**Reglas del mundo en cinco líneas** ✅ (wikitext de *Silver Millennium*, cruzado con la sinopsis general de AniList/Wikipedia):
1. Hace milenios existió el **Milenio de Plata** (Silver Millennium), un reino en la Luna que vivía en armonía con el resto de planetas del sistema solar (menos la Tierra).
2. La familia real lunar lleva una **marca de luna creciente** en la frente (Reina/Princesa/Neo-Reina Serenity, Chibiusa, y los gatos lunares Luna/Artemis/Diana).
3. Su deber es proteger el **Cristal de Plata Legendario** (Ginzuishou) y vigilar que la Tierra evolucione sin influencias negativas.
4. Los habitantes del Milenio de Plata envejecen igual que los humanos, pero dejan de envejecer al llegar a la adultez.
5. Ese reino renacerá en la Tierra entre los siglos XX y XXX, centrado en **Cristal Tokio** (Crystal Tokyo), donde gobierna Neo-Reina Serenity.

**La historia por arcos**, cada uno con su grupo villano ✅ (wikitext de cada `EvilGroups Infobox`, cruzado con el listado de temporadas de AniList):
1. **Dark Kingdom** (Reino Oscuro) — temporada 1: comandante **Reina Beryl**, líder verdadera **Reina Metalia**; monstruos Youma.
2. **Black Moon Clan** (Clan de la Luna Negra) — Sailor Moon R: líder **Wiseman**, escondite en Nemesis, monstruos Droids.
3. **Death Busters** — Sailor Moon S: líder **Master Pharaoh 90**, comandantes Kaolinite/Mistress 9, sub-grupo las Witches 5, escondite Academia Mugen.
4. **Dead Moon Circus** — Sailor Moon SuperS (arco «Dream»): reina **Nehelenia**, comandante Zirconia, sub-grupos Amazon Trio y Amazoness Quartet, monstruos Lemures.
5. **Shadow Galactica** — Sailor Stars: líder **Chaos**, comandante **Sailor Galaxia**, sub-grupo Sailor Animamates, escondite Sagittarius Zero Star / Ginga TV.

**Símbolos y objetos icónicos**, con romanización oficial ✅ (wikitext de cada `Item Infobox`):
- **Cristal de Plata Legendario** (幻の銀水晶, *Maboroshi no Ginsuishou*).
- **Broche de transformación** (変身・ブローチ, *Henshin Buroochi*) — frase «Moon Prism Power, Make Up».
- **Moon Stick** (ムーン・スティック) — primera arma de Sailor Moon; cura y destruye.
- **Cutie Moon Rod** (キューティ・ムーン・ロッド) y **Spiral Heart Moon Rod** (スパイラルハートムーンロッド) — evoluciones del báculo, ligadas a los ataques «Moon Princess Halation» y «Moon Spiral Heart Attack»/«Rainbow Moon Heartache».
- Otros ítems por personaje, sólo listados por nombre (índice de moonkitty.net, sin descripción visual propia) ⚠️: Tiara (4 versiones), Pluma de disfraz (Disguise Pen), Medallón estelar (Star Locket), Comunicador, Lápiz de transformación (una por guerrera), Llave del Tiempo y Luna P (de Chibiusa).
- **Sailor V** es a la vez el alter ego de Minako (antes de unirse al grupo) y el nombre del videojuego arcade ficticio dentro de la propia historia (ver punto 6) — guiño metanarrativo directo.

**Vocabulario propio que un fan reconoce al instante** ✅ (sailormoon.fandom.com + Doblaje Wiki, ya citado en `datos-texto.md`):
- «Moon Prism Power, Make Up!» — la frase de transformación de Usagi (la redacción exacta del doblaje latino es del punto 8, del equipo de voz) ⚠️.
- **Youma / Droid / Daimon / Lemures**: el nombre del monstruo de turno cambia según el arco (ver tabla arriba) — vocabulario que ubica en qué temporada estás.
- **«Game Center Crown»**, el arcade donde se esconde el Centro de Mando Lunar.
- **«Ginzuishou»** (Cristal de Plata) y **«Crystal Tokyo»**, los dos términos que resumen el objetivo final de la serie.

**Sin verificar esta tanda** (detalle extra, no obligatorio del punto) ⚠️: la lista completa de símbolos planetarios por guerrera con imagen propia medida — se sabe que cada una lleva el símbolo astronómico de su planeta (el tag «Henshin» 91% de AniList lo confirma indirectamente), pero no medí cada símbolo con una imagen propia esta tanda; es un dato que roza más el punto de vestuario (imagen).

---

## Lo mejor para la lámina

1. El **«juego de Sailor V»** ficticio (arcade con HUD propio «NEXT/SCORE») es un objeto real-en-un-sitio-real perfecto: una máquina arcade con esa pantalla exacta, para un canal de videojuegos o retro.
2. La **Supercomputadora + Visor de Mercury** es el objeto-interfaz más icónico de la franquicia — cabe perfecto como «pantalla» con fotograma real en un canal de tecnología o edición.
3. El screentone punteado + las rayitas de «brillo» (corrector líquido) que Takeuchi usaba a mano son la textura 2D más fácil y auténtica de replicar en Photoshop.
4. Ningún otro canal del servidor usa la estética *mahou shoujo* de los 90 — hueco libre para diferenciarse.
5. Para diálogo normal, usar **Coming Soon** (gratis, con toda la puntuación en español) en vez de Anime Ace 2.0 BB, a la que le faltan ¿ y ¡.

## No encontré (extra, no obligatorio — con las búsquedas hechas)

- La tipografía exacta del **logo japonés original** (hand-lettered): busqué «Sailor Moon logo font identify», «Sailor Moon logotype font» — sólo salieron identificaciones del logo **inglés** (Birch/Matrix/Occidental). No hay un nombre de fuente ni de diseñador para el logotipo katakana original. ⚠️
- **Capturas reales** de las cajas de diálogo de los juegos de pelea de SNES/Game Gear: Game UI Database y The Cutting Room Floor dieron 403 (reto de Cloudflare) en los dos intentos permitidos cada uno, por WebFetch y por curl directo con distintos user-agents. ⚠️
- La fuente **«OH-no.2»** para el pensamiento en la edición Kodansha: sólo un resultado de búsqueda la menciona, sin poder descargarla ni verificarla con fontTools. ⚠️
- Una entrevista o *making of* específico sobre **encuadres y composición de cámara** del anime: no encontré ninguno dedicado a esto en el tiempo de esta tanda. ⚠️
- **WikiMoon.org** (la wiki en inglés más detallada, con la página de Eyecatch) dio 403/Cloudflare tanto por WebFetch como por curl directo, dos intentos cada vez — usé sailormoon.fandom.com (la sugerida por el encargo) y moonkitty.net como alternativas. ⚠️
- Modelos o *rigs* 3D con licencia libre verificada de Sailor Moon en Sketchfab (toca el punto 18, pero es del investigador de imagen — punto 3). ⚠️

## Bitácora de búsqueda

- **Datos de partida**: `partes/datos-texto.md` (AniList: ficha, staff, obras relacionadas/recomendadas) — no repetido, sólo cruzado.
- **Wiki oficial** (sailormoon.fandom.com), API `action=query&prop=revisions&rvslots=main` (wikitext crudo, sin gastar cupo de buscador): *Silver Crystal*, *Moon Stick*, *Crescent Moon Wand* (sin contenido), *Cutie Moon Rod*, *Spiral Heart Moon Rod*, *Moon Kaleidoscope* (sin contenido), *Dark Kingdom*, *Black Moon Clan*, *Death Busters*, *Dead Moon Circus*, *Shadow Galactica*, *Silver Millennium* (+ sección Crystal Tokyo), *Sailor V* (redirección), *Transformation Brooch*, *Super Computer*, *Mercury Visor*, *Sailor V (video game)*, *Game Center Crown*, *Influences that inspired Codename Wa Sailor V/Sailor Moon*.
- **Imágenes propias** vistas y medidas (API `prop=imageinfo&iiprop=url|size` + descarga + `Read`): `File:Sailorvgame.jpg` (225×169), `File:Sm.gamecentercrown.manga.png` (379×480), `File:M minisupercomputer.gif` (280×226), más imageinfo sin descargar de `File:A mercurygoggles.jpg` (234×220) y `File:Crystal Brooch.png` (386×468).
- **WebSearch** (inglés salvo que se diga lo contrario): «Sailor Moon manga speech bubble thought bubble typography shoujo conventions» · «"Sailor Moon" logo font identify Birch Matrix» · «"Anime Ace 2.0 BB" font download free Blambot» · «"Heatwave" font dafont free script 80s» · «Sailor Moon anime eyecatch attack name card on screen transformation text» · «Sailor Moon video games list SNES Game Gear Famicom Another Story Sailor Moon Drops» · «Sailor Moon Mercury mini super computer visor screen text interface» · «"Sailor V" arcade game within Sailor Moon anime manga Minako plays» · «Naoko Takeuchi Sailor Moon art style influences Codename Sailor V interview» · «Naoko Takeuchi manga drawing technique pen ink screentone materials interview» · «Sailor Moon Crystal 3D CGI transformation backlash DoGA animation fans reaction» · «Sailor Moon Crystal studio DEEN Production IG digital animation art style change season» · «"Sailor Moon" Toei Animation 1992 cel animation technique douga sakuga production notes» · «"Sailor Moon" "The Cutting Room Floor" TCRF beta unused text».
- **WebFetch**: DeviantArt (KinnoHitsuji, literatura con el link a la imagen de the-sweet — descargada aparte), TV Tropes (403, dos intentos con curl y WebFetch), WikiMoon.org ×2 páginas (403 ambas), moonkitty.net (2 páginas, una sin datos útiles), CBR (2 artículos, útiles), Wikipedia (*Naoko Takeuchi*, *List of Sailor Moon video games*), brickme.tumblr.com (entrevista/comentario de arte, muy útil), TCRF (403 ×2).
- **fontTools** (`TTFont(...).getBestCmap()` y `getGlyphOrder()`, comprobando á é í ó ú ñ Ñ ¿ ¡ ü): 14 fuentes de Google Fonts descargadas de `cdn.jsdelivr.net/fontsource` (Bangers, Luckiest Guy, Zeyada, Yuji Syuku, Klee One, DotGothic16, Press Start 2P, Special Elite, Caveat, Mrs Saint Delafield, Yellowtail, Permanent Marker, Montserrat, Noto Sans JP) + 6 más (Coming Soon, Patrick Hand, Short Stack, Gochi Hand, Architects Daughter, Fredoka) → **todas con las 10 letras/signos completos**. Anime Ace 2.0 BB (Blambot, vía fontspace.com/get/family/pwjm, 3 estilos) → **le faltan ¿ y ¡** en los tres estilos.
- **Webs bloqueadas** (403/Cloudflare, dos intentos cada una, no reintentadas): `wikimoon.org` (directo y vía API), `tcrf.net` (directo y vía API), `gameuidatabase.com` (búsqueda y ficha directa).

**Sigue:** nada obligatorio pendiente de los puntos 5, 6, 11, 18, 24 y 25 — lo que falta (fuente exacta del logo japonés, capturas de HUD de los juegos de SNES/Game Gear, making-of de encuadres) queda en «No encontré» porque son extras, no lo mínimo que pide ENCARGO.md. Si se abre otra tanda: reintentar TCRF/Game UI Database/WikiMoon por un canal distinto (por ejemplo pidiendo al jefe una IP o user-agent distintos), y medir los símbolos planetarios por guerrera con imagen propia si el redactor lo pide.
