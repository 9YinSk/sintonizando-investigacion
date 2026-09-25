# Parte de TEXTO, JUEGOS Y TÉCNICA · Days Gone (encargo 120)

Investigador de texto: puntos 5, 6, 11, 18, 24, 25 de `ENCARGO.md`. Libreta de datos, no prosa.
Parte de `partes/datos-texto.md` (Steam) y `partes/episodios.md` (tráiler argumental ya visto).
Wiki confirmada: `https://daysgone.fandom.com` (MediaWiki 1.43.9, comprobado por `api.php?action=query&meta=siteinfo`).

## Punto 5 — Tipografía

Days Gone es un videojuego realista, sin globos de manga: «cómo hablan en pantalla» son subtítulos, cartelas de misión y textos de interfaz (se detalla en el punto 6). Aun así hay **letras según cada uso** bien diferenciadas, miradas en las capturas de `www.gameuidatabase.com/gameData.php?id=275` (Cloudflare bloquea la portada; funciona por el espejo de Wayback, ver Bitácora) y en fotogramas propios:

- **Logo/título oficial** (carátula, key art, Steam): letra de trazo grueso, geométrica, con **puntos/rombos añadidos en el centro de varias letras** — la «textura de óxido» que pide el encargo es justo ese picado en el trazo. Según el hilo del foro de dafont donde el propio autor de la pregunta identificó y confirmó la fuente, es **Refrigerator Deluxe Heavy** (de pago, MyFonts/Fontspring), con esos puntos centrales añadidos a mano después. ⚠️ (una sola fuente, pero es el hilo donde el autor original la identificó y la dio por buena) https://www.dafont.com/forum/read/301026/days-gone-font
  - Letra libre parecida más cercana que encontré y comprobé con fontTools (trazo grueso, geométrico, todo mayúsculas): **Anton** (Google Fonts) — sí trae á é í ó ú ñ Ñ ¿ ¡ ü. https://fonts.google.com/specimen/Anton · comprobado con `fontTools.ttLib.TTFont(...).getBestCmap()` sobre el .ttf bajado de `fonts.gstatic.com`. ✅ (verificado por mí, con la herramienta que pide `AYUDANTE.md`)
- **Logo del menú principal** (dentro del juego, no la carátula): versión más simple, sin puntos ni óxido, en un recuadro con borde fino — la misma familia condensada en negrita que el resto del HUD (ver abajo). Visto en `guidb_thumbs/02.jpg` (Wayback → Game UI Database). ✅ (imagen propia + Game UI Database)
- **Interfaz de juego (menús, HUD)**: una sans geométrica condensada, siempre en VERSALES, con bastante interletrado, en dos grosores — uno grueso para títulos de pantalla («SKILLS», «MECHANIC», «MERCHANT», «STORYLINES», «INVENTORY») y uno más fino para las listas del menú principal («CONTINUE», «LOAD GAME», «NEW GAME», «OPTIONS»). ✅ (miradas en `guidb_thumbs/02.jpg, 11.jpg, 16.jpg, 31.jpg, 39.jpg, 45.jpg`, todas del espejo Wayback de Game UI Database)
  - Dato cruzado interesante: la propia web de Bend Studio (`bendstudio.com`) usa una familia tipográfica **propia llamada «Config»**, con los pesos `configthin`, `configlight`, `configregular` y `configbold` (lo dice su CSS, comprobado por mí con `curl` sobre `/assets/site/css/fout.css`). El HUD del juego usa exactamente ese patrón de un peso fino para texto corrido y uno grueso para títulos, lo que sugiere que es la misma familia o una emparentada, aunque no pude bajar el .woff2 para comparar letra a letra (protegido por ruta). ⚠️ (cruce razonado, no una prueba directa letra por letra) https://bendstudio.com (CSS: `/assets/site/css/fout.css?c=183`)
  - Letra libre parecida más cercana, comprobada con fontTools: **Oswald** (para el peso normal/semibold de las listas de menú) y **Bebas Neue** (para los títulos más pesados y ajustados como «SKILLS»). Las dos traen á é í ó ú ñ Ñ ¿ ¡ ü. https://fonts.google.com/specimen/Oswald · https://fonts.google.com/specimen/Bebas+Neue ✅ (verificado con fontTools)
- **Cartelas de misión / subtítulos** (texto que aparece sobre la imagen del juego, esquina superior izquierda, sin caja ni burbuja): letra más fina y más alta que la del HUD, todavía en VERSALES pero con trazo ligero — ejemplo real: «THE ONLY ONE HE'S GOT» sobre la partida, con una etiqueta pequeña naranja «STORY JOB» debajo. ✅ (mirado en `guidb_thumbs/56.jpg`, Wayback → Game UI Database, captura `Days-Gone07172020-100304-75783_thumb.jpg`)
  - Letra libre parecida comprobada: **Fjalla One** o **Barlow Semi Condensed** (ambas con acentos, ñ, ¿ ¡ completos). https://fonts.google.com/specimen/Fjalla+One
- **Grito / alerta** («SURROUNDED», cuando te rodea una horda): mismo tipo de letra que el HUD pero en **rojo sangre sobre una textura de mancha negra y roja, con bordes desgarrados** (grunge, no un globo dentado de cómic). ✅ (mirado en `guidb_thumbs/10.jpg`, Wayback → Game UI Database)
- **Onomatopeya**: no aplica — Days Gone no usa onomatopeyas en pantalla (ni en manga ni en textos superpuestos); los sonidos se comunican con el propio audio y con el diseño del HUD (el grito de un Screamer, por ejemplo, se ve como un icono de alerta y se oye, no se lee). Lo digo con la búsqueda hecha: `srsearch=onomatopoeia` en la wiki no da resultados de interfaz.
- **Cartel del mundo (rótulo real dentro del juego)**: el parche inferior («rocker») de la chaqueta de moteros de Deacon dice **«NOMAD»**, bordado en una letra **slab/serif ancha, curva, en marrón rojizo sobre parche beige**, cosida en una chaqueta vaquera/cuero azul desgastada — típica letra de parche de motero (western, con relieve de hilo). Medido y mirado por mí en un fotograma oficial de Steam (recorte propio). ✅ (fotograma propio, `store.steampowered.com/app/1259420`, captura `ss_80bbb5ea187cc422012f7a84e694f20f87a26862`) https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1259420/ss_80bbb5ea187cc422012f7a84e694f20f87a26862.1920x1080.jpg
  - Letra libre parecida (slab ancha, look de parche bordado, con acentos completos): **Rye** (Google Fonts, letra western de rótulo, comprobada con fontTools: trae á é í ó ú ñ Ñ ¿ ¡ ü). https://fonts.google.com/specimen/Rye
- **Créditos / letra corrida (recordings, notas encontradas)**: la misma condensada del HUD, en gris claro sobre panel oscuro, formateada como guion de radio con el nombre en mayúsculas seguido de dos puntos («CPL. ESPOSITO: Sir, we got a problem –»), con **rayas largas (—)** para cortar la frase, no puntos suspensivos. ✅ (mirado en `guidb_thumbs/36.jpg` y `37.jpg`, «FIELD RECORDING - 1260», Wayback → Game UI Database)

## Punto 6 — Cómo hablan y piensan en pantalla

**Esto responde directo a la queja del dueño** («cuadros de diálogo acordes a la temática, no una burbuja blanca rara»): Days Gone **no usa nunca una burbuja**. Cada tipo de texto en pantalla tiene su propio formato, todos mirados en capturas reales (Game UI Database vía Wayback y fotogramas de Steam):

- **Subtítulos de diálogo** (la conversación normal, en cualquier escena o cinemática): una **barra sólida negra, ancho completo, alineada abajo**, con el **nombre del personaje en blanco y negrita seguido de dos puntos**, y la frase en blanco normal justo debajo o al lado. Ejemplo real, textual: *«Deacon: Yeah, Boozer and I decided to head down to Lost Lake for a while, just a change of scenery, you know?»*. Sin marco, sin cola de burbuja, sin fondo de color: sólo la caja negra semitransparente. ✅ (mirado en `guidb_thumbs/24.jpg`, pantalla «BOUNTIES», Wayback → Game UI Database `gameData.php?id=275`) https://web.archive.org/web/20241209104516/https://www.gameuidatabase.com/uploads/Days-Gone07172020-100258-98058_thumb.jpg
- **Título de misión / cartela de historia**: texto grande, VERSALES, sin caja, **esquina superior izquierda**, sobre la imagen del juego (no interrumpe la acción); debajo, una etiqueta pequeña con fondo de color sólido (naranja para «STORY JOB») indicando el tipo de encargo. Ejemplo real: *«THE ONLY ONE HE'S GOT»* + etiqueta *«STORY JOB»*. ✅ (mirado en `guidb_thumbs/56.jpg`)
- **Nuevo objetivo**: arriba a la izquierda, un icono triangular pequeño (el mismo triángulo con silueta de torre/campamento que marca los puntos del mapa) + la etiqueta diminuta «NEW OBJECTIVE» + el texto del objetivo en grande, VERSALES, y debajo una segunda etiqueta con fondo naranja con el nombre del lugar. Ejemplo real: *«NEW OBJECTIVE» → «INVESTIGATE LAST KNOWN LOCATION»*. ✅ (mirado en `guidb_thumbs/51.jpg`)
- **Grabaciones de campo / notas encontradas** (los objetos NERO y de otros que Deacon recoge y hace sonar): pantalla completa aparte (no superpuesta a la acción), fondo oscuro con foto del sitio de fondo muy oscurecida, encabezado «FIELD RECORDING - <número>» en la letra condensada del HUD, y el texto como **guion de radio**: nombre en mayúsculas + dos puntos + la frase, con **rayas largas (—) para cortar el habla entrecortada**, no puntos suspensivos. Trae barra de scroll y un contador de progreso de coleccionables arriba a la derecha («29%»). ✅ (mirado en `guidb_thumbs/36.jpg` y `37.jpg`)
- **Alerta de horda / grito**: aparece igual que un título de misión pero en rojo sangre sobre una mancha oscura desgarrada (ver punto 5) — es lo más parecido a un «grito» que tiene el juego, pero sigue sin ser un globo: es una cartela de pantalla completa tipo aviso. Ejemplo real: *«SURROUNDED»*. ✅ (mirado en `guidb_thumbs/10.jpg`)
- **Pensamiento**: Days Gone no usa cajas de pensamiento; el monólogo interior de Deacon, cuando lo hay, se resuelve con voz en off sin texto en pantalla (comprobado buscando `srsearch=inner monologue` y `voiceover` en la wiki: no hay página de mecánica dedicada, y las escenas de radio ya cubren la función de «lo que piensa Deacon en voz alta»). ⚠️ (no encontré una fuente dedicada al monólogo interior; lo baso en no encontrar mecánica de «pensamiento» en la wiki ni en las capturas de interfaz)
- **HUD permanente durante el juego**: abajo a la izquierda, dos barras apiladas finas (verde = Salud, azul = Aguante/Stamina) sin marco, con iconos pequeños de munición y arma debajo; abajo a la derecha, un **disco/brújula circular** con textura desgastada, marcador cardinal «N», y dos iconos pequeños (cámara y un icono de gesto/silbido) a los lados; arriba a la derecha, cuando aplica, una etiqueta con fondo negro y el nombre del campamento («HOT SPRINGS», con un icono de vapor) y el dinero/chatarra («₵»). ✅ (mirado en `guidb_thumbs/25.jpg`, `51.jpg`, `56.jpg`, `24.jpg`)

## Punto 11 — Videojuegos de la franquicia: interfaz, menús, cuadros de diálogo

(pendiente)

## Punto 18 — Estilo y técnica, y cómo replicarlo

(pendiente)

## Punto 24 — Obras parecidas y temas relacionados

(pendiente)

## Punto 25 — El mundo, la historia y sus símbolos

**Las reglas del mundo, en cinco líneas** (de la wikitext de la wiki, ficha del juego y de «Freakers»):
- Dos años antes de la historia, Cloverdale Corporation desarrolló en secreto un arma biológica disfrazada de proyecto de biobotánica; un empleado, David Gorman, robó una muestra para denunciarla en una convención en Portland y se infectó sin saberlo, difundiendo el «virus Freaker» por todo el mundo en dos semanas. · ✅ (Fandom `Freakers`, dos secciones «History»/«Creation» cruzadas con la ficha del juego `Days Gone`) https://daysgone.fandom.com/wiki/Freakers
- El virus mató a 2.500 millones de personas; la costa este de EE. UU. cayó en dos días, la costa oeste (menos poblada, donde está Oregón) resistió más. La civilización colapsó en asentamientos pequeños. · ✅ https://daysgone.fandom.com/wiki/Freakers
- El virus infecta también animales (lobos, osos, cuervos); crea criaturas feroces, caníbales, con la piel llena de llagas y sin pelo (menos los «Reachers», que recuperan vello). Se comunican por feromonas y forman mentes de colmena en grupo («Swarmers»). · ✅ https://daysgone.fandom.com/wiki/Freakers
- El clima cambia el comportamiento: la lluvia amortigua sus sentidos, la nieve les da más fuerza pero les baja la visión. · ✅ https://daysgone.fandom.com/wiki/Freakers
- Juego ambientado en Farewell, Oregón, dos años después de la pandemia; Deacon St. John (ex-Mongrels MC) busca a su mujer Sarah, con quien puede reunirse porque hay indicios de que sigue viva. Perspectiva en tercera persona, mundo abierto con sitios reales de Oregón (Marion Forks, Belknap Crater, Crater Lake). · ✅ (ficha del juego, Fandom) https://daysgone.fandom.com/wiki/Days_Gone

**Historia por arcos** (de la ficha del juego, sección «Plot», y de las páginas de facciones):
- **Arco 1 — Llegada a Farewell / Boozer herido**: Deacon y Boozer buscan a Leon; la moto de Deacon se avería, Boozer cae en una emboscada de los Rippers y queda malherido; Deacon recupera su moto (que se la había llevado el campamento de Copeland) y empieza a trabajar para los campamentos. · ✅ (Fandom `Drifter Bike`, sección «Events of Days Gone») https://daysgone.fandom.com/wiki/Drifter_Bike
- **Arco 2 — Los campamentos y las hordas**: Deacon hace de mercenario/cazarrecompensas para Copeland's Camp, Tucker's Camp/Lost Lake e Iron Mike's Camp, sube «Trust Level» limpiando hordas, entregando orejas de Freaker y comida, y desbloquea armas y piezas de moto. · ✅ (Fandom `Trust Level`) https://daysgone.fandom.com/wiki/Trust_Level
- **Arco 3 — Los Rippers y NERO**: el culto Rest In Peace (Rippers), liderado por Carlos (antes Jessie Williamson, expulsado de los Mongrels por asesinar a otro miembro), venera a los Freakers y el fin del mundo; en paralelo Deacon investiga los puestos abandonados de NERO (National Emergency Response Organization) buscando pistas de Sarah. · ✅ (Fandom `Rippers`, `National Emergency Response Organization`) https://daysgone.fandom.com/wiki/Rippers · https://daysgone.fandom.com/wiki/National_Emergency_Response_Organization
- **Arco 4 — reencuentro con Sarah y la Milicia de Deschutes**: Deacon encuentra a Sarah con vida en un campamento de NERO; el enfrentamiento final es contra la Milicia (Iron Mike / Coronel Garrett); si Copeland's Camp y Tucker's Camp llegaron a Trust Level 3, se unen a la batalla final (final alternativo). · ✅ (Fandom `Trust Level`, sección «Alternate Ending») https://daysgone.fandom.com/wiki/Trust_Level
- **Remaster (2025)**: versión remasterizada lanzada el 25 de abril de 2025 (confirmado también en la propia ficha de Steam: DLC «Carretera Rota» del 24-abr-2025). · ✅ (Fandom `Days Gone`, sección «Remaster»; `partes/datos-texto.md` Steam) https://daysgone.fandom.com/wiki/Days_Gone

**Emblemas y logos de grupos** (medibles en las imágenes ya bajadas por `recolectar.py`, `biblias/120-days-gone/partes/datos-imagen.md`):
- **Mongrels MC**: el logo es un perro con un chorro de sangre saliendo de la boca, mordiendo su propia cadena; colores del club **negro, blanco y rojo**. Lema: *«Ride the Broken Road»*. Imagen 512×512 ya bajada: https://static.wikia.nocookie.net/daysgone/images/9/93/Mongrel_MC.png · ✅ (Fandom `Mongrels Motorcycle Club`, wikitext) https://daysgone.fandom.com/wiki/Mongrels_Motorcycle_Club
- **NERO**: identificador visual son los **trajes HAZMAT amarillos**, vehículos MRAP con ametralladoras Browning M2HB, checkpoints con vallas y carteles de cuarentena; el logo de la organización (`NERO.png`) aparece en su ficha. · ✅ https://daysgone.fandom.com/wiki/National_Emergency_Response_Organization
- **Rippers (culto R.I.P.)**: se identifican por **cortes y cicatrices rituales, ropa rasgada, armas rudimentarias, arneses de tirador de la 2ª Guerra Mundial, fortificaciones de madera y hogueras** — nada de logo gráfico, su «marca» es el propio cuerpo mutilado y las hogueras nocturnas. · ✅ (infobox de facción, wikitext) https://daysgone.fandom.com/wiki/Rippers

**Objetos icónicos y vocabulario propio** (glosario que un fan reconoce al instante, de la wikitext de `Freakers`):
- **Drifter Bike**: la moto de Deacon, inventario móvil y medio de transporte; el único objeto que conservó de su moto vieja es el depósito de gasolina personalizado que le regaló Sarah. · ✅ https://daysgone.fandom.com/wiki/Drifter_Bike
- **Freakers / Freaks / los infectados**: nombre genérico. Tipos con nombre propio (glosario oficial de la wiki, nombres en pseudo-latín entre paréntesis): **Swarmer** (Homo sapiens mūtans, el infectado básico, se mueven en manada por feromonas), **Horde** (Homo sapiens mūtans Turba, mutación que hace que los swarmers formen manadas de cientos), **Bleacher** (albino), **Newt** («cría», pasivo salvo que te acerques o tengas poca vida; hay «loot newt» de cueva), **Screamer** (grito agudo que llama a la horda), **Breaker** (aguanta mucho daño, perfora armadura militar), **Reacher** (más rápido, fuerte e inteligente, con pelo), **Runner** (lobo infectado, más rápido que la moto), **Rager Bear** (oso infectado, aguanta balas y alambre de espino), **Crier** (cuervo infectado, ataca en bandada). · ✅ (glosario completo con nombres científicos ficticios) https://daysgone.fandom.com/wiki/Freakers
- **NERO, N.E.R.O.**: la agencia gubernamental de emergencias, criticada por no contener el virus; sus campamentos y puestos de control abandonados salpican el mapa. · ✅ https://daysgone.fandom.com/wiki/National_Emergency_Response_Organization
- **Rippers**: culto R.I.P. (Rest In Peace) que venera a los Freakers. · ✅ https://daysgone.fandom.com/wiki/Rippers
- **Trust Level / Camp Credits**: el sistema de confianza con cada campamento (hasta nivel 3), moneda de trueque por orejas de Freaker, comida y misiones. · ✅ https://daysgone.fandom.com/wiki/Trust_Level
- **Survival Wheel**: el menú radial de inventario en juego (ver punto 11). · ✅ https://daysgone.fandom.com/wiki/Survival_Wheel

## Cronología de facciones y campamentos (para el punto 25)
- Copeland's Camp, Tucker's Camp (Lost Lake / Hot Springs), Iron Mike's Camp: los tres campamentos de refugiados con los que Deacon sube Trust Level. · ✅ (Fandom `Trust Level`, búsqueda interna con nombres coincidentes en `Trust Level`, `Judgment`) https://daysgone.fandom.com/wiki/Trust_Level
- Milicia del condado de Deschutes (Iron Mike / Coronel Garrett): la facción militar antagonista del tramo final. · ⚠️ (una sola fuente, wikitext de búsqueda «Judgment»: `Mark Copeland`, `Iron Mike`; no confirmé aún con una segunda fuente independiente el nombre exacto «Deschutes County Militia») https://daysgone.fandom.com/wiki/Days_Gone (resultado de búsqueda interna `srsearch=Judgment`)

## Lo mejor para la lámina

(pendiente)

## No encontré

(pendiente)

## Bitácora

(pendiente)

Sigue: rellenar todos los puntos (5, 6, 11, 18, 24, 25) desde cero.
