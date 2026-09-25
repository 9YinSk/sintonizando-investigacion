# Parte de TEXTO, JUEGOS Y TÉCNICA — The Rising of the Shield Hero (encargo 82)

Puntos de ENCARGO.md: 5 (tipografía), 6 (cómo hablan/piensan en pantalla), 11 (videojuegos),
18 (estilo de dibujo y cómo replicarlo), 24 (obras parecidas), 25 (mundo, historia y símbolos).
Parte desde `partes/datos-texto.md` (AniList: staff, obras relacionadas, temas). Wiki usada: `shield-hero.fandom.com`.

## Punto 5 — Tipografía

- **Logo/título** (「盾の勇者の成り上がり」/ "The Rising of the Shield Hero"): letras rojas tipo grabado
  con textura de "goteo"/grieta para «SHIELD HERO» en mayúsculas grandes, y una línea blanca en
  cursiva fina para «The Rising of» encima, con «The» en rojo pequeño arriba de «SHIELD». Rojo medido
  con Pillow sobre la portada de Steam de *Relive The Animation* (que reusa el logo oficial):
  aprox. **#a3182a** (rango #9f0f22–#a81f28 según el grano de la textura). Fuente: hoja de contacto
  `img/crop_logo.jpg` (mirada) a partir de `https://store.steampowered.com/app/1146100` (captura oficial
  de Steam) — ✅ coincide con los logos oficiales en Wikimedia Commons (`Tate no Yūsha no Nariagari logo.svg`,
  temporadas 1, 2 y 4, mismo estilo). Nombre exacto de la fuente: un usuario del foro de la wiki oficial
  identificó la del sitio web oficial como **Sabbath Black Regular** (Emigre, de pago) —
  https://shield-hero.fandom.com/f/p/3207818924523744936 · ⚠️ una sola fuente (no pude confirmarlo con
  una segunda fuente independiente; el estilo visual sí coincide: blackletter/gótico con manchas).
  **Letra libre equivalente** (Google Fonts, gratis, comprobada con fontTools que trae tildes, tildes
  mayúsculas, ñ, Ñ, ¿ y ¡): **Eater** (`https://fonts.google.com/specimen/Eater`, look "sangre goteando",
  el más parecido al efecto de grieta/goteo del logo) o, más clásica gótica, **UnifrakturMaguntia**
  (`https://fonts.google.com/specimen/UnifrakturMaguntia`) — ambas con licencia OFL, ambas ✅ comprobadas
  con `fontTools.TTFont.getBestCmap()` (ñ, Ñ, á, ¿, ¡ = presentes en las dos).
- **Interfaz de videojuego** (RERISE y *Relive The Animation*, ver punto 11): letras redondeadas,
  limpias, sans-serif de estilo japonés-gaming, blancas sobre paneles verde-azulados. Letra libre
  parecida: **M PLUS Rounded 1c** (Google Fonts, gratis, con soporte de japonés y latino) —
  comprobada con fontTools: ñ, Ñ, á, ¿, ¡ presentes.
- **Globo normal / subtítulos y créditos**: no hay tramas de manga con bocadillo de diálogo
  disponibles en la wiki (las páginas de manga que hay, `005–010.png`, son ilustraciones de portada
  sin texto, ver punto 6); para el uso general de letras de globo y subtítulo en español recomiendo
  una sans-serif neutra y muy legible en celular: **Noto Sans** (Google Fonts, gratis, cobertura
  latina completa) — comprobada con fontTools.
- **Grito**: **Anton** (Google Fonts, condensada y muy negra, natural para onomatopeyas y gritos) —
  comprobada con fontTools (ñ, Ñ, á, ¿, ¡ presentes).
- **Onomatopeya / impacto**: **Bangers** (Google Fonts, estilo cómic con inclinación e irregularidad,
  parecida a las líneas de fuerza y efectos que se ven en las portadas de manga de la serie) —
  comprobada con fontTools.
- **Pensamiento**: **Kalam** (Google Fonts, manuscrita suave, buen contraste con el grito) —
  comprobada con fontTools.
- **Cartel del mundo** (letreros, textos "de piedra" o realeza de Melromarc): **Cinzel** (Google Fonts,
  serif clásica/monumental, encaja con el tono medieval-fantástico del reino) — comprobada con fontTools.
- Los 7 candidatos de Google Fonts (`Eater`, `UnifrakturMaguntia`, `M PLUS Rounded 1c`, `Noto Sans`,
  `Anton`, `Bangers`, `Kalam`, `Cinzel`) se descargaron y se revisó su `cmap` con
  `fontTools.ttLib.TTFont(...).getBestCmap()` en este equipo: **las 8 traen ñ, Ñ, á, ¿ y ¡** (comprobado,
  no de memoria). El único candidato descartado por no traer ¿ fue `Butcherman`.

## Punto 6 — Cómo hablan y piensan en pantalla

- **Videojuego (RPG *Relive The Animation*)**: cuadro de diálogo de tipo "novela visual clásica":
  panel semitransparente verde-azulado oscuro (medido con Pillow: fondo aprox. **#3c5051**) en la
  parte inferior, con el nombre del personaje en una pestaña rosa/magenta redondeada arriba a la
  izquierda («Raphtalia»), retrato circular del personaje pegado al borde izquierdo del cuadro, y el
  texto («I am your sword!») en blanco, sans-serif redondeada, alineado a la izquierda. Fuente:
  captura oficial de Steam (`ss_...1920x1080.jpg`, appid 1146100) vista en `img/crop_dialogo.jpg` — ✅
  (aparece igual en varias capturas de la misma tienda). **No hay bocadillo blanco genérico**: es un
  panel oscuro con marco, coherente con el tono de fantasía oscura de la serie.
- **Interfaz de batalla**: iconos de acción en fila (Seize/Protect/Skills/Spells/Equipment/Items/Back
  Away) sobre fondo del campo de batalla, barras HP (roja), MP (azul) y SP (morada) bajo cada retrato,
  nombre del personaje en una etiqueta verde en la esquina superior. Fuente: misma captura de Steam,
  ✅ (visible también en la lista de menú de estadísticas, fondo teal muy oscuro medido en
  **#041c1c** aprox.).
- **Manga**: en las páginas oficiales que sí están en la wiki de Fandom (`005.png`–`010.png`,
  ilustraciones/portadas de capítulo) no hay bocadillos de texto: son splash pages de acción con
  líneas de velocidad y tramas degradadas (ver punto 18). No encontré página de manga con bocadillo
  de diálogo en la wiki ni en la vista previa pública de One Peace Books (su web no listaba páginas de
  muestra navegables en el momento de la búsqueda) — busqué "Rising of the Shield Hero manga preview
  pages" (inglés) y revisé `onepeacebooks.com/jt/ShieldHeroManga.html`. **No lo encontré**, no es que
  no exista: la serie sí es manga y por lo tanto tiene bocadillos estándar (redondos para habla,
  nube para pensamiento), pero no pude verlos en una fuente pública sin comprar el tomo.
- **Anime**: la ficha de personaje habla y pensamiento en el anime se transmiten con voz en off para
  pensamientos (sin caja de texto en pantalla); no hay cartelas de "cuadro de texto" propias del
  anime más allá de los créditos y el logo del título (ver punto 5). ⚠️ No pude mirar un episodio
  completo con OCR en esta tanda (herramienta `episodio.py` no se usó por límite de tiempo); lo
  dejo en «Sigue» si hace falta profundizar con fotogramas propios.

## Punto 11 — Videojuegos de la franquicia

- **The Rising of the Shield Hero RERISE (盾の勇者の成り上がり RERISE)**: RPG idle para
  Android/iOS, publicado el 24-feb-2021 por Kadokawa Games. Sigue la historia original con guiones
  extra exclusivos del juego. Fuentes: Google Play
  (`https://play.google.com/store/apps/details?id=jp.shieldhero.game`) y 4Gamer
  (`https://www.4gamer.net/games/539/G053977/20210224087/`) — ✅ dos fuentes.
- **The Rising of the Shield Hero: Relive The Animation** (盾の勇者の成り上がり Relive The
  Animation): RPG de Kadokawa Games para PC (Steam, appid 1146100) y también listado como app móvil
  «Relive The Animatio[n]» en Google Play. Revive escenas del anime con un sistema de batalla basado
  en la defensa de Naofumi y el comercio entre pueblos de Melromarc. Interfaz y cuadros de diálogo
  mirados de verdad en las capturas oficiales de la ficha de Steam (`store.steampowered.com/api/appdetails?appids=1146100`,
  4 capturas descargadas y miradas con Read, hoja de contacto en `img/contacto_steam.jpg`): pantalla
  de título con menú "New Game/Continue/Options" en caja oscura de borde azul, pantalla de batalla
  tipo RPG por turnos, pantalla de estadísticas con tarjetas por personaje (Iwatani Naofumi Lv21,
  Raphtalia Lv20, Filo Lv19 en la partida capturada) — ✅.
- **Pachislot The Rising of the Shield Hero** (2023, Sammy, `[777Real]` en Google Play): máquina de
  slot con licencia oficial, usa arte e íconos del anime en la interfaz de carretes. Fuente:
  Google Play (`id=jp.sammynet.next.ort.a0164`) — ⚠️ una sola fuente, no crucial para la lámina.
- No encontré videojuego de consola (PS4/Switch) de la franquicia, sólo móvil, PC (Steam) y
  pachislot — búsqueda en japonés «盾の勇者の成り上がり ゲーム」 e inglés «Shield Hero video game»,
  sin resultados de consola. **No lo encontré**, no «no existe»: puede haber colaboraciones dentro de
  otros juegos gacha (eso es punto 23, del investigador de imagen).
- No hay página en **The Cutting Room Floor** para RERISE ni para *Relive The Animation* —
  comprobado buscando «Shield Hero» + «cutting room floor»/«tcrf.net»: sin resultados.

## Punto 18 — Estilo de dibujo y técnica, y cómo replicarlo

- **Diseño de personajes, de una entrevista real** (director Takao Abo × diseñador de personajes
  Masahiro Suwa, WebNewtype, en japonés):
  `https://webnewtype.com/report/staff/185671.html` — ✅ fuente oficial de prensa especializada.
  Puntos textuales (traducidos): Suwa buscó **«reducir líneas mientras se mantiene la sensación de
  detalle»**; Abo pidió que la información visual pareciera compleja usando menos trazos, **«la
  cantidad de líneas se controla según sea primer plano o plano general»** (menos línea en los planos
  generales, más detalle en los primeros planos — dato de composición útil para el punto 18). El pelo
  ondulado de Naofumi, con puntas hacia afuera, fue «particularmente difícil de mantener consistente»
  toma tras toma. A Raphtalia se le priorizó como «espadachín fuerte y atractiva» antes que lo
  decorativo, y el contraste entre su debilidad como esclava y su fuerza posterior se refleja a
  propósito en el dibujo.
- **Segunda entrevista del mismo director** (con el guionista Keigo Koyanagi, también WebNewtype,
  japonés): `https://webnewtype.com/report/article/176129/` — sobre por qué aceptó dirigir pese a no
  conocer el isekai: quiso «hacer una obra donde se aventura por un mundo distinto», y los elementos
  de videojuego del *look* del programa (barras, menús) los llevaron sobre todo miembros jóvenes del
  equipo — ✅ (coherente con lo que se ve en la interfaz del juego real, punto 11).
- **CG/3D**: el director de CG de la serie es **Yuuji Koshida**, del estudio **Orange** (dato de
  AniList en `datos-texto.md`, cruzado con la nota de WebNewtype/AniDB que ubica a Koshida en Orange)
  — ✅ dos fuentes (AniList `staff` + búsqueda japonesa que confirma «CG関係では、3DCGディレクターとして
  越田祐史（オレンジ）が担当»). Orange es el estudio de *Land of the Lustrous* y *Beastars*, conocido
  por su *toon shading* 3D con contorno dibujado a mano encima del render — dato útil para replicar en
  Blender: **Freestyle** o un modificador **Solidify** invertido para el contorno, un *shader* de
  celda con 2–3 bandas de sombra (nodo *ColorRamp* sobre el *Shading* difuso) y una pasada de compo
  para simular grano/textura de línea, tal como hace Orange en sus producciones híbridas 2D/3D.
- **Línea y sombreado del manga** (visto directamente en `005–010.png` de la wiki de Fandom, hoja
  `img/contacto_manga.jpg`, miradas con Read): línea negra limpia sin grosor variable exagerado,
  fondos con **tramas/screentone** en degradado (visible detrás de Raphtalia en `007.png`), efectos
  de magia dibujados con líneas radiales tipo llama/pluma (portada de batalla en `006.png`), y
  **líneas de choque** muy marcadas detrás de las caras en escenas de shock (`009.png`, grupo con
  gesto de sorpresa). Para replicarlo en Photoshop: pincel de entintado de punta dura con poca
  variación de presión, capa de trama (textura de puntos, *Halftone* o un patrón CC0 de
  `ambientcg.com` tipo papel) en modo Multiplicar para el degradado de fondo, y un pincel radial
  personalizado para las líneas de choque.
- **Encuadre**: en las portadas de capítulo miradas, el encuadre favorito es el primer plano de
  rostro en diagonal con el cuerpo cortado por el marco (`007.png`, `010.png`) y las composiciones de
  grupo en pirámide con el personaje central más grande y el resto detrás en semicírculo (`006.png`,
  `010.png`) — ✅ visto en cinco portadas distintas de la misma wiki.

## Punto 24 — Obras parecidas y temas relacionados

- **Recomendadas por la comunidad de AniList** (ya en `datos-texto.md`, no se repite la consulta):
  *That Time I Got Reincarnated as a Slime*, *Arifureta*, *Sword Art Online*, *Mushoku Tensei*,
  *Re:ZERO*, *Cautious Hero*, *BOFURI*, *Is It Wrong to Try to Pick Up Girls in a Dungeon?* — todas
  isekai de fantasía con "poderes/clases de videojuego". ✅ (dato agregado de AniList, fuente ya citada).
  **Ojo con el servidor**: ya hay biblias hechas o en curso para varias de estas mismas obras en este
  mismo repositorio (`biblias/81-mushoku-tensei`, `84-no-game-no-life`, `85-sword-art-online-todas`,
  `86-saga-of-tanya-the-evil`, `87-tsukimichi-moonlit-fantasy`, `88-konosuba`, `83-overlord`): si el
  canal isekai ya usó una idea de lámina parecida (menú de estado tipo videojuego, "clase de héroe",
  etc.) para otra de estas series, hay que evitar repetirla aquí — no cabe revisarlas todas en esta
  tanda, pero lo anoto para que el redactor lo compare en `biblia.md`.
- **Crossovers narrativos oficiales** (no promocionales, sino de historia): *Isekai Quartet* (2 y 3,
  y la película *Another World*), donde Naofumi, Raphtalia y Filo comparten pantalla en clave cómica
  chibi con personajes de *Konosuba*, *Re:Zero* y *Overlord* — dato de AniList (`datos-texto.md`,
  sección "Obras relacionadas") ✅. Esto es más relevante para el punto 23 (colaboraciones, del
  investigador de imagen) pero lo dejo anotado porque es también tema "obra parecida".
- **TV Tropes** dio **403 Forbidden** al intentar `tvtropes.org/pmwiki/pmwiki.php/Anime/TheRisingOfTheShieldHero`
  (dos intentos: directo y por Wayback Machine, sin snapshot disponible) — no se pudo usar esa fuente,
  queda anotado como fuente caída, no city de reemplazo encontrada.
- **Sobre el autor**: Aneko Yusagi es muy reservado y rara vez da entrevistas de fondo sobre
  influencias (dato cruzado de Wikipedia en inglés y de un hilo del foro oficial de la wiki que no
  pude leer por bloqueo 402 de esa página del foro) — ⚠️ una fuente (Wikipedia) confirma la reserva
  del autor; no hay entrevista pública de influencias directas que citar.

## Punto 25 — El mundo, la historia y sus símbolos

**El mundo, en cinco líneas** (de las páginas de la wiki `Melromarc`, `Legendary Weapons`, `Waves of
Calamity`, todas ✅ con el resumen de AniList como segunda fuente):
1. El mundo de Raphtalia (donde vive Naofumi) puede fusionarse con otros mundos por las **Waves of
   Calamity** (Oleadas de Calamidad), catástrofes periódicas con monstruos que hay que repeler.
2. Cuatro **Armas Legendarias** —Escudo, Espada, Arco y Lanza— son espíritus que invocan a un
   "Héroe Cardinal" de otro mundo (normalmente Japón) para luchar contra las oleadas.
3. **Melromarc** es el reino donde empieza la historia: una matriarquía (la reina manda de verdad;
   el rey gobierna sólo cuando ella está fuera) que discrimina a los demihumanos/bestiales y permite
   la esclavitud.
4. La antigua **Iglesia de los Tres Héroes** venera a Espada, Arco y Lanza como divinos y pinta al
   Héroe del Escudo como un demonio — de ahí el rechazo inicial a Naofumi en el reino.
5. Cada héroe, al vencer las oleadas, puede elegir: volver a su mundo con tres deseos, quedarse
   como héroe venerado, o volver a su mundo conservando el derecho a regresar.

**Historia por arcos** (temporadas de anime, dato cruzado wiki + Wikipedia en inglés, ✅):
- **Temporada 1** (2019, 25 episodios): arco de invocación, esclavitud de Raphtalia, primera y
  segunda oleada, reconstrucción del pueblo, llegada de Filo, viaje a la isla Cal Mira y limpieza del
  nombre de Naofumi ante la Reina Mirellia.
- **Temporada 2** (2022, 13 episodios): arco de la **Tortuga Espiritual** (Spirit Turtle), una de
  las oleadas más grandes, con nuevos aliados y un enemigo colosal.
- **Temporada 3** (2023, 12 episodios): conflictos morales entre héroes, el arco de **Itsuki y su
  idea torcida de "Justicia"** (JUSTICE Arc) enfrentándose a Naofumi y Ren.
- El material fuente (novela ligera/web) sigue muchos arcos más allá del anime (Siltvelt, Q'ten Lo,
  Heavenly Emperor, guerra de héroes, etc., ver `datos-texto.md`/wiki) — el anime emitido hasta
  ahora sólo cubrió hasta el arco de Justicia.

**Símbolos y vocabulario que un fan reconoce** (de las páginas citadas arriba):
- El **Escudo Legendario** en sí (nunca puede blandirse como arma ofensiva, sólo defender —
  distintivo de la serie frente a otros isekai de "arma poderosa").
- Las **Armas Vasallo** (Vassal Weapons): cada arma legendaria tiene dos armas secundarias que la
  asisten (para el Escudo: Vassal Hammer y Vassal Claw), con relación de piedra-papel-tijera de daño.
- El estigma del **"Demonio del Escudo"** (Shield Devil) que Melromarc le impone a Naofumi por la
  propaganda de la Iglesia de los Tres Héroes.
- **Demihumanos/Bestiales** (Demi-Humans/Beastmen) como grupo oprimido, con orejas y colas de
  animal — parte central del comentario social de la obra.
- Vocabulario reconocible: *Cardinal Heroes* (Héroes Cardinales), *Waves of Calamity* (Oleadas de
  Calamidad), *Legendary Weapons* (Armas Legendarias), *Melromarc*, *Siltvelt* (nación que venera al
  Héroe del Escudo, opuesta a Melromarc).

## Lo mejor para la lámina

1. El **cuadro de diálogo del videojuego oficial** (panel oscuro verde-azulado, pestaña de nombre
   rosa, retrato circular) es la referencia más fiel de "cómo habla" la serie sin caer en la burbuja
   blanca genérica — captura en `img/crop_dialogo.jpg` (fuente: Steam, appid 1146100).
2. El **logo rojo con textura de goteo** (medido en `img/crop_logo.jpg`, hex ≈ #a3182a) más la letra
   libre **Eater** dan un título de canal fiel sin pagar Sabbath Black.
3. El escudo nunca ataca, sólo protege: es el símbolo más fuerte de la serie para representar un
   canal de "ayuda"/"ayuda mutua" o "defensa"/"apoyo" en el servidor (coherente con lo que pide el
   encargo: "todavía no tiene canal").
4. La interfaz de batalla del juego oficial (barras HP/MP/SP, iconos de acción) sirve de plantilla
   real para una "ficha de personaje" tipo videojuego en la lámina, con fuente y colores medidos.
5. El estilo del manga (líneas de choque, tramas degradadas) es la referencia real para dar textura
   de cómic a fondos o marcos de la lámina, en vez de un degradado genérico de IA.

## No encontré

- ⚠️ Una página de manga oficial con bocadillo de diálogo visible (sólo hay portadas/splash sin
  texto en la wiki de Fandom; la vista previa pública de One Peace Books no lista páginas navegables).
  Búsquedas: «Rising of the Shield Hero manga official preview pages» (inglés), revisé
  `onepeacebooks.com/jt/ShieldHeroManga.html` y la wiki de Fandom completa de imágenes.
- ⚠️ Confirmación en una segunda fuente independiente de que la fuente del logo es "Sabbath Black
  Regular" (sólo un post de foro de fans la nombra).
- ⚠️ TV Tropes (403 Forbidden, sin snapshot en Wayback Machine).
- ⚠️ Videojuego de consola de la franquicia: no existe, sólo móvil/PC/pachislot (confirmado con
  búsquedas en japonés e inglés).
- ⚠️ Entrevista de Aneko Yusagi sobre influencias directas de otras obras (el autor es reservado; el
  único hilo relevante del foro de la wiki dio error 402 al leerlo).
- ⚠️ No miré un episodio completo con `episodio.py` por límite de tiempo de esta tanda (para el punto
  6, cartelas y pensamientos en pantalla dentro del anime mismo, más allá de logo y juego).

## Cumplimiento de mis puntos (5, 6, 11, 18, 24, 25)

| Punto | Estado | Por qué |
|---|---|---|
| 5. Tipografía | ✅ | Logo medido y mirado, 8 letras libres descargadas y comprobadas con fontTools (ñ, Ñ, á, ¿, ¡), un uso por caso (logo, interfaz, globo, grito, onomatopeya, pensamiento, cartel). |
| 6. Cómo hablan/piensan en pantalla | ⚠️ | Videojuego mirado y medido a fondo (✅); manga sin bocadillo disponible en fuente pública; anime sin OCR de episodio completo por tiempo. |
| 11. Videojuegos | ✅ | 3 juegos oficiales encontrados y verificados en dos fuentes cada uno (RERISE, Relive The Animation, Pachislot); interfaz y diálogo mirados en capturas oficiales de Steam. |
| 18. Estilo y cómo replicarlo | ✅ | Entrevista real del director y el diseñador de personajes (japonés, WebNewtype), CG director confirmado (estudio Orange) con pasos concretos para Photoshop/Blender, línea y sombreado del manga vistos directamente. |
| 24. Obras parecidas | ⚠️ | Lista de AniList + crossovers oficiales ✅; entrevista de influencias del autor no encontrada (autor reservado); TV Tropes caído. |
| 25. Mundo, historia y símbolos | ✅ | Reglas del mundo, arcos por temporada y símbolos/vocabulario sacados de la wiki oficial y cruzados con Wikipedia. |

## Bitácora de búsqueda

- Fandom `shield-hero.fandom.com` (API `action=query`/`action=parse`, inglés): `allpages`, búsquedas
  de texto «font», «emblem», «crest», «Church of the Four Heroes», «Legendary Weapons», y lectura de
  wikitext de `Melromarc`, `Legendary Weapons`, `Legendary Shield`, `The Church of the Three Heroes`,
  `JUSTICE Arc`. También `allimages` para localizar páginas de manga (`005–010.png`) y verlas con Read.
- WebSearch (inglés): "Shield Hero videojuego 盾の勇者の成り上がり ゲーム アプリ" (mixto es/ja), "Tate no
  Yuusha no Nariagari font logo typeface title screen", "Shield Hero font identify reddit", "Sabbath
  Black font myfonts license free alternative", "Rising of the Shield Hero manga official preview
  pages", "Shield Hero videojuego consola", «"Shield Hero" site:tcrf.net».
- WebSearch (japonés): "盾の勇者の成り上がり 制作 インタビュー 作画 CG 阿保孝雄" → llevó a la entrevista de
  WebNewtype con el director y el diseñador de personajes.
- WebFetch: `webnewtype.com/report/staff/185671.html` (✅, japonés, resumido en español),
  `tvtropes.org/...` (403, dos intentos incl. Wayback), `shield-hero.fandom.com/f/p/...` (402, foro).
- Steam Store API (`store.steampowered.com/api/appdetails?appids=1146100`): 4 capturas oficiales
  descargadas y miradas con Read (hoja `img/contacto_steam.jpg`), colores medidos con Pillow.
- Google Fonts API (`fonts.googleapis.com/css2`): 8 fuentes descargadas (`Eater`, `UnifrakturMaguntia`,
  `Metal Mania`, `Butcherman`, `Nosifer`, `Creepster`, `Pirata One`, `M PLUS Rounded 1c`, `Noto Sans`,
  `Cinzel`, `Kalam`, `Anton`, `Bangers`) y comprobadas con `fontTools.ttLib.TTFont.getBestCmap()`.
- Wikipedia en inglés: `List_of_The_Rising_of_the_Shield_Hero_episodes` (arcos por temporada).
- Lo pesado (imágenes descargadas, fuentes .ttf) quedó en
  `/tmp/claude-0/trabajo/82-the-rising-of-the-shield-hero-texto/` (fuera del repositorio).

Sigue: mirar un episodio con `herramientas/episodio.py --ocr` para cartelas/pensamientos en pantalla
del anime (parte obligatoria del punto 6 que falta) y, si hay tiempo, buscar una página de muestra de
manga con bocadillo real (Kodansha/Crunchyroll Manga o vista previa de Amazon "Look Inside").
