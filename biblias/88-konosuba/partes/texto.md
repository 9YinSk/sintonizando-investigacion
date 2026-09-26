# Texto, juegos y técnica · Konosuba (88-konosuba)

Investigador de texto, juegos y técnica. Puntos 5, 6, 11, 18, 24 y 25 de ENCARGO.md.
Libreta de datos: un dato por línea, fuente enlazada, ✅ (dos fuentes) o ⚠️ (una), minuto o tamaño si aplica.

## 5 · Tipografía

El logo real de KonoSuba (visto en el título de temporada 3 «Bonus Stage», fotograma propio)
es kanji redondeado grueso (maru-gothic), contorno blanco de ~8-10 px, relleno en degradado
magenta→dorado, sobre estallido de partículas; el subtítulo en alfabeto latino («KONO SUBARASHII
SEI... -BONUS STAGE-») va en una slab-serif condensada en versalitas. La comunidad de dafont.com
identificó por separado, para el logo «KonoSuba God's Blessing...», dos fuentes:

- Título/logo, letra base identificada: **Grobold** (dafont, «100% Free») · hilo dafont.com/forum/read/311727 (RulGcia, 29-mar-2017) · ✅ (hilo con acuerdo de 2 usuarios) · comprobado con fontTools: **NO** trae á/í/ó/ú/Á/Í/Ó/Ú/ñ/Ñ/¿/¡/ü (sólo é/É) → no sirve para texto en español sin retocar.
- Título/logo, segunda letra identificada: **Tiki Tropic** (dafont, «100% Free») · dafont.com/forum/read/311727 (LeoBloxyDonut, 13-sep-2020) · ✅ · comprobado con fontTools: **SÍ** trae á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü completos (las 3 variantes: Regular, Bold, Outline) → mejor opción libre para rotular «KONOSUBA» completo en español.
- Diseñador del logo oficial (créditos AniList): Ushio Funayama (舩山潮), «Title Logo Design» · https://anilist.co/anime/21202/staff · ⚠️ (una fuente, sin His nombre de letra confirmado por el estudio).
- Alfabeto propio del mundo isekai: los carteles, pergaminos y sellos del «Mundo Paralelo» usan un alfabeto latino modificado inventado para la serie (no es japonés ni un alfabeto real). Incluye el sigilo de Aqua (orden Axis, usado como «@») y el sigilo de Eris (usado como «$»/«€»). Reconstruido en fuente libre por un fan (HarJIT, basado en el trabajo previo de /u/-Alexor-, fuente «SVGfont») en 3 versiones (Konosuba2/3/4-Regular.ttf, descarga gratis) · https://harjit.moe/konosubanomoji.html · ⚠️ (fanwork, sin reconocimiento oficial, pero el alfabeto en sí se ve en pantalla en la serie).
- Cuadro de diálogo del videojuego (ver punto 6/11): la letra de los nombres y del texto es una sans/serif redondeada clara sobre pergamino, sin identificar aún la fuente exacta; pendiente de comparar carácter por carácter con Google Fonts.
- Créditos/subtítulos oficiales en streaming (Crunchyroll): usan su tipografía estándar de plataforma (no propia de Konosuba); sin verificar aparte para esta serie.

**Letra libre recomendada por uso** (para la lámina, en español):
| Uso | Letra libre | Trae tildes/ñ/¿¡ |
|---|---|---|
| Logo/título | Tiki Tropic (Bold para el filete grueso) | Sí (fontTools) |
| Globo normal de manga | por confirmar (ver punto 6) | — |
| Grito | Tiki Tropic Bold o similar cómic grueso | Sí |
| Cartel del mundo/alfabeto isekai | Konosuba4-Regular (HarJIT, decorativo, sólo para ambientar, no para texto legible) | No aplica (no es alfabeto latino estándar) |
| Interfaz de videojuego (parchment UI) | por confirmar | — |

## 6 · Cuadros de diálogo (manga, cartelas, interfaces, pensamientos)

- **Videojuego** «KONOSUBA - God's Blessing on this Wonderful World! Love For These Clothes Of Desire!» (Steam, PQube/MAGES., 2024): el cuadro de diálogo es un **pergamino/scroll de madera y papel**, con los extremos enrollados como un rollo, filete marrón oscuro, relleno beige-arena; el nombre del personaje va en una **cinta/banderola con puntas** encima del cuadro. Las elecciones de diálogo son varias franjas de pergamino apiladas con flechas «‹ ›» para pasar de opción. Medido con Pillow sobre la captura oficial (1920×1080): fondo del pergamino `#CCB47A`, cinta del nombre `#D4AE67`, borde oscuro `#C08E53` (±5 por canal, JPG de Steam) · https://store.steampowered.com/app/2349140 · ✅ (visto directamente en la captura oficial).
- El menú de gestión (itinerario/«Schedule Overview») usa el mismo lenguaje visual: paneles color hueso con filete marrón, iconos redondos oscuros, pestañas con esquinas en punta — coherente con «pergamino de aventurero» en todo el juego, no sólo en el diálogo · misma fuente.
- **Manga** (capítulo 1, portada a color, edición de fan-scan en inglés vía MangaFox, dibujo de Masaru Watanabe/渡真仁 según los créditos de la propia página): las cajas de narración son **estallidos irregulares de bordes puntiagudos** (tipo «burst»), relleno blanco, texto en mayúsculas itálicas gruesas; hay una cinta ondulada vertical para el crédito de la revista (Sneaker Bunko). Ojo: la rotulación de esa imagen es de la traducción de fans, no el japonés original, así que sólo sirve para la FORMA de la caja, no para la letra exacta · https://static.wikia.nocookie.net/konosuba/images/c/c1/Manga_chapter_1_page_2.jpg · ⚠️ (una fuente, es scanlation).
- **Cartelas promocionales del anime** (tráiler oficial de la OVA en Dailymotion, fotograma propio a 0:06 y 0:12): el texto de anuncio «まだまだ冒険» (・Aún hay aventura) usa gótico japonés muy grueso, dorado con contorno negro, colocado en diagonal con destellos; el cartel de ubicación «アクセル» (Axel, el pueblo) es un gótico blanco fino, minúsculo, alineado abajo a la izquierda, sin caja — así presenta la franquicia los letreros de lugar en su material oficial · https://www.dailymotion.com/video/x9avkfi (min 0:06 y 0:12) · ✅ (visto en vídeo oficial de la distribuidora, canal «Espinof»).
- **Videojuego retro** «KonoSuba: in the life» (RPG Maker VX, oficial pero fan-hecho, regalo del BD/DVD vol. 1, 25-mar-2016): estilo de interfaz JRPG clásico de los 90 (cita textual de la wiki: «a 1990's style fantasy RPG») — previsible caja azul con borde blanco tipo Dragon Quest/Final Fantasy de NES-SNES, típico de RPG Maker por defecto · https://konosuba.fandom.com/wiki/Konosuba:_in_the_life · ⚠️ (no se localizó captura de pantalla directa, sólo la descripción de la wiki).
- Onomatopeyas de explosión: el hechizo de Megumin se muestra en pantalla como texto de impacto durante el tráiler (destello blanco total a las 0:24, halo rosa `#FFD8FF` medido a 0:24.6 en el mismo fotograma) — el "flash" cubre casi toda la pantalla, técnica de golpe de luz total más que letra en pantalla · mismo tráiler · ✅.

## 11 · Videojuegos de la franquicia

Lista verificada de juegos con interfaz/diálogo propios (wiki de Fandom + Steam + tienda oficial):

- **KonoSuba: God's Blessing on this Wonderful World! Love For These Clothes Of Desire!** (PS4/Switch/Steam, visual novel de gestión, MAGES./PQube, japonés 2019, occidente 7-feb-2024) — capturas 1920×1080 bajadas y miradas (ver punto 6) · https://store.steampowered.com/app/2349140 · ✅.
- **KonoSuba: Labyrinth of Hope and the Gathering Adventurers** («~希望の迷宮と集いし冒険者たち~», PS Vita/PS4, RPG de mazmorras, Entergram/Capcom, 27-jun-2019; versión ampliada «Plus» 27-ago-2020 también en Switch por SNK) · https://konosuba.fandom.com/wiki/Konosuba:_Labyrinth_of_Hope_and_the_Gathering_Adventurers · ✅ (wiki + ficha del juego con opening «STAND UP!» y ending «Mata Ashita»).
- **KonoSuba: Fantastic Days** (アプリ móvil iOS/Android, gacha RPG por equipos, Sumzap, 27-feb-2020; versión PC en 2024) — retrata a los personajes en super-deformado (SD); servicio cerrado a fines de enero-2025, versión offline descargable hasta enero-2027 · https://konosuba.fandom.com/wiki/Konosuba:_Fantastic_Days · ✅.
- **KonoSuba: in the life** (RPG Maker VX, PC, fan-hecho con reconocimiento oficial, regalo del primer BD/DVD, 25-mar-2016) — estilo JRPG retro de los 90 · https://konosuba.fandom.com/wiki/Konosuba:_in_the_life · ⚠️ (una fuente).
- **Isekai Quartet** (crossover de mesa/tácticas chibi con otras isekai, no es un juego propio sino un anime-crossover; no cuenta como videojuego de Konosuba) — se anota para no confundir · https://anilist.co/anime/21202 (relaciones) · ✅.

## 18 · Estilo de dibujo y técnica, y cómo replicarlo

Rigs y tramas: ver puntos 3 y 19.

- Equipo creativo (créditos AniList, confirmado también en el sitio oficial konosuba.com/1st/staff_cast): director Takaomi Kanasaki (金崎貴臣), diseño de personajes del anime Kouichi Kikuta (菊田幸一) sobre el diseño original de Kurone Mishima (三嶋くろね), director de arte Masakazu Miyake (三宅昌和), diseño de color Saori Yoshida (吉田沙織), director de fotografía Shigemitsu Hamao (浜尾繁光), directora de CG Kana Imagaki (今垣佳奈), estudio Studio DEEN (TV) / J.C.Staff (película «Legend of Crimson») · https://anilist.co/anime/21202/staff · ✅ (AniList + sitio oficial japonés).
- Filosofía de dirección cómica, cita directa del director Kanasaki (entrevista 1-nov-2019 con el guionista Makoto Uezu, ddnavi.com, con motivo de la película): distingue **「ギャグ」(gag)** de **「コメディ」(comedia)** — el gag es «algo repentino y sin conexión que hace reír de golpe, como fuegos artificiales de un solo tiro»; la comedia «hace reír de forma natural dentro del drama». Dice que calcula el «sube y baja de tensión» («テンションの上げ下げ») **plano por plano** para la comedia · https://ddnavi.com/article/d574070/a/ · ✅ (entrevista directa, en japonés, leída completa).
- Técnica real para dibujar explosiones «vistosas» y deformadas en animación 2D japonesa (no específico de Konosuba, pero es la técnica de oficio que usan los animadores de efectos en anime cómico/de acción, aplicable directo al motivo central de la serie): se prioriza la **silueta** sobre el realismo; se construye girando repetidamente formas redondas de luz llamadas **「T-light」** para crear la sensación de expansión; se combinan líneas rectas y curvas (tipo rayo) para acentuar lo deformado. Autor: Kazunori Ozawa, serie de artículos de animación de efectos · https://genkosha.pictures/movie/19091928091 · ✅ (fuente técnica profesional, en japonés).
- **Cómo replicarlo en Photoshop** (aplicando la técnica de arriba + lo visto en las capturas propias): 1) silueta grande y redondeada en una capa `Multiplicar` o `Trama` oscura; 2) 3-4 capas de «T-light» (óvalos de luz blanca/amarilla con desenfoque gaussiano, cada una rotada unos 15-30°) en modo `Aumentar luminosidad (Color dodge)` para el núcleo; 3) rayos rectos finos con la herramienta Lápiz + jitter de ángulo, en amarillo/blanco, modo `Trama`; 4) borde final: contorno blanco grueso (Estilo de capa → Trazo, 6-10 px) si se usa para texto/logo, igual que el título de temporada 3 medido en el fotograma propio (halo `#FFD8FF`, fondo oscuro `#212C2E`); 5) grano y aberración cromática como ajuste final (capa de ruido + desplazar levemente los canales R/B) para imitar el filtro de vídeo del anime.
- **Cómo replicarlo en Blender**: para el pergamino/parchment del videojuego (punto 6), un plano con textura de papel (ver ambientCG en punto 4/19) + `Bevel` en los bordes enrollados + Shader `Principled BSDF` con rugosidad alta y un `Bump` sutil; para un toon shading general del elenco, `Shader to RGB` + rampa de color de 2-3 tonos (plano, no degradado suave) y contorno con **Solidify invertido** (más simple de controlar por escena que Freestyle si hay muchos objetos). Sombreado observado en las capturas del juego y en los fotogramas propios: **sombra plana de un solo tono** en la piel y el pelo (no degradado), típico del anime de TV de este estudio; no se encontró artbook o making-of oficial que confirme el software exacto de producción 2D (posible Retas/CLIP STUDIO PAINT, estándar de la industria en 2016, pero sin fuente directa) · ⚠️ (inferencia razonada, no confirmada por el estudio).

## 24 · Obras parecidas y temas relacionados

- Recomendaciones directas de usuarios de AniList (mismo público, votos altos): *Cautious Hero: The Hero Is Overpowered but Overly Cautious* (1107 votos), *Combatants Will Be Dispatched!* (373), *Princess Connect! Re:Dive* (299), *The Devil is a Part-Timer!* (256), *Uncle from Another World* (226), *Isekai Quartet* (200, crossover directo con Konosuba), *TSUKIMICHI -Moonlit Fantasy-* (136), *DanMachi* (134), *Mushoku Tensei* (86) · https://anilist.co/anime/21202 · ✅ (dato agregado de la propia plataforma).
- TV Tropes (página «Literature/KonoSuba», resumen de buscador; la página en sí bloquea acceso directo desde este servidor y su copia en Wayback también está bloqueada aquí, ver Bitácora): la resume así, cita literal del resumen indexado: «Konosuba takes pretty much every trope and character archetype associated with "Isekai" stories, and RPG games and either deconstruct, subverts, or inverts them» — confirma que el eje del humor es la **deconstrucción/parodia de tropos isekai y de videojuego de rol**, coherente con el punto 11 (interfaces RPG parodiadas) · https://tvtropes.org/pmwiki/pmwiki.php/Literature/KonoSuba · ⚠️ (resumen de buscador, no la página completa).
- Comparación directa de tono con el propio anime «hermano» de crossover **Isekai Quartet** (comparte elenco con *Re:Zero*, *Overlord* y *The Saga of Tanya the Evil*, todas isekai pero de tono serio) — Konosuba es el contrapunto cómico dentro de ese mismo grupo de franquicias · https://anilist.co/anime/21202 (relaciones) · ✅.
- Trivia de spin-off: *KonoSuba: An Explosion on This Wonderful World!* (manga/novela ligera centrada en Megumin) es la obra «hermana» dentro de la misma franquicia, no una influencia externa — se anota para no proponerla como «parecida» por error · https://tvtropes.org/pmwiki/pmwiki.php/Literature/KonoSubaAnExplosionOnThisWonderfulWorld · ⚠️.

## 25 · El mundo, la historia y sus símbolos

- El «Mundo Paralelo» (Parallel World) tiene moneda propia, el **eris**, acuñada en cobre/plata/oro/mithril (1 moneda de mithril = 1.000.000 eris; 1 eris ≈ 1 yen japonés según Aqua); también existe en billetes · https://konosuba.fandom.com/wiki/Terminology · ✅ (wiki, página dedicada «Terminology»).
- Sistema de juego de rol integrado al mundo: ficha de aventurero con 7 estadísticas en japonés — Fuerza (筋力), Vitalidad (生命力), Inteligencia (知力), Poder Mágico (魔力), Destreza (器用度), Agilidad (敏捷性) y Suerte (幸運) — más niveles, puntos de habilidad y «carnet de aventurero» con lista de monstruos cazados · misma fuente · ✅.
- Organizaciones/facciones con emblema propio: **Gremio de Aventureros** (gubernamental), **Gremio de Mercaderes**, **Gremio de Magos** (controla pergaminos), Asociación de Cazadores, Instituto de Investigación Mágica · misma fuente · ✅.
- **Orden de Axis** (culto de Aqua, アクシズ教): pocos cientos de seguidores en todo el mundo, sede en Arcanletia, financiada por las aguas termales que Aqua volvió agua bendita (cura heridas y repele muertos-vivientes/demonios); su símbolo está en el archivo `AxisCult.png` (480×480) de la wiki · https://static.wikia.nocookie.net/konosuba/images/1/17/AxisCult.png · ✅ (wiki + novela ligera vol. 4 y 15 citadas dentro del artículo).
- **Orden de Eris** (culto de la diosa de la fortuna Eris, fe nacional del Reino de Belzerg; la familia noble Dustiness —de Darkness— es tradicionalmente fiel a esta orden; cada verano hacen el «Festival de Apreciación a Eris», donde alguien se disfraza de la diosa) · https://konosuba.fandom.com/wiki/Eris_Order · ✅.
- **Demonios Carmesí / Crimson Demons** (紅魔族, tribu de magos del pueblo de Megumin): piel pálida, pelo castaño oscuro/negro, ojos carmesí que brillan al excitarse, tatuaje de código de barras de nacimiento (por ser «humanos modificados artificialmente»); son todos chūnibyō, obsesionados con la «genialidad», con pose y frase de firma propias — rasgo de estilo actuado, no sólo de vestuario · https://konosuba.fandom.com/wiki/Crimson_Demons · ✅.
- «Durian Quest»: jerga local de Axel para las misiones que nadie quiere tomar por su mala paga frente al riesgo (la comparación es literal con la fruta durián) — vocabulario reconocible por el fandom, útil para texto de canal · misma fuente Terminology · ✅.

## Lo mejor para la lámina

- El cuadro de diálogo real de la franquicia es un pergamino de madera enrollada con cinta-banderola para el nombre (medido en el juego oficial de Steam), no una burbuja blanca genérica.
- Letra libre para «KONOSUBA» en español con tildes/ñ/¿¡ completos: **Tiki Tropic** (comprobado con fontTools); Grobold sólo sirve para el inglés/sin acentos.
- El alfabeto propio del mundo (con el sigilo de Aqua/Axis y el de Eris) es un recurso único y poco usado para decorar carteles del mundo sin que se lea como texto real.
- La técnica «T-light» (formas redondas de luz rotadas) es la manera profesional de dibujar la explosión de Megumin; se explica paso a paso para Photoshop arriba.
- Emblemas ya identificados y con imagen: símbolo de la Orden de Axis (`AxisCult.png`) y de la Orden de Eris (`Faith.png`), listos para usar como sello o parche en un objeto de la lámina.

## No encontré

- Nombre exacto de la fuente tipográfica usada en el cuadro de diálogo del videojuego de Steam (identifiqué la FORMA del cuadro con capturas propias, no el nombre de la letra) — búsqueda: «Konosuba game dialogue box font», «KonoSuba Love for these Clothes UI font» (WebSearch, sin resultado directo). ⚠️
- Captura de pantalla directa de «KonoSuba: in the life» (RPG Maker VX) — sólo hay la descripción de la wiki, los vídeos bonus del BD no están en plataformas abiertas. ⚠️
- TV Tropes y Wayback Machine están bloqueados en este contenedor para lectura directa (curl da 403/egress-policy incluso a través de web.archive.org; `navegar.py` falla porque falta el navegador headless versión 1243 en `/opt/pw-browsers`, sólo hay la 1194) — se dejó constancia para que quien tenga acceso los revise a mano. Sólo pude usar los resúmenes que da el buscador. ⚠️
- Making-of o artbook oficial que confirme el software 2D de producción (Retas, CLIP STUDIO PAINT u otro) — búsqueda en japonés «このすば 制作 作画 インタビュー» y «金崎貴臣 このすば インタビュー» sin resultado técnico, sólo entrevistas de casting/dirección de actores. ⚠️
- Interfaz o capturas propias de «Fantastic Days» y de «Labyrinth of Hope» (juego cerrado/discontinuado); sólo tengo su ficha de wiki, no imágenes de su HUD — pendiente si aparecen en Google Play/App Store archivado o en YouTube (bloqueado aquí). ⚠️

## Bitácora

- Fandom `konosuba.fandom.com/api.php`: búsquedas de texto (`srsearch`) en inglés para «logo», «Axis Church symbol», «Crimson Demon Clan», «Adventurer Guild», «alphabet writing language», «manga page», «in the life», «Fantastic Days», «Eris Order» — todas con resultado, sin usar navegador (la API funciona directo, sin 403).
- Steam: `store.steampowered.com/search` y `api/appdetails` para localizar el juego con interfaz visible y sus 13 capturas oficiales 1920×1080; 4 bajadas y miradas con Read (contact sheet propio).
- WebSearch (en inglés): «Konosuba logo font title typography identification» → llevó a 2 hilos de dafont.com y a la página de HarJIT sobre el alfabeto del mundo. «Natsume Akatsuki interview influences Konosuba inspired by RPG games» → sin transcripción disponible.
- WebSearch (en japonés): «金崎貴臣 このすば インタビュー 制作 アニメーション» → llevó a la entrevista de ddnavi.com (leída completa); «このすば 爆発 エフェクト 作画 撮影 インタビュー Studio DEEN» → sin resultado específico de Konosuba, pero sí un tutorial profesional general de efectos de explosión usado igualmente.
- fontTools (`TTFont(f).getBestCmap()`) sobre Grobold.ttf y las 3 variantes de Tiki Tropic, descargadas de dafont.com (licencia «100% Free» comprobada en la ficha de cada fuente).
- Dailymotion + `fotogramas.py --cada 3`: tráiler oficial de la OVA (canal «Espinof», 48.679 vistas) completo, 11 fotogramas de 0:00 a 0:30; además 4 fotogramas propios con ffmpeg en 23.2/23.5/24.3/24.6 s para medir el color del logo de temporada 3 en el estallido. Vídeo borrado tras sacar las hojas.
- TCRF (`tcrf.net/api.php`) bloqueado por Cloudflare (challenge JS) tanto por curl como por `navegar.py` (falta el binario del navegador headless en el contenedor, versión 1243 vs 1194 instalada) — no se pudo entrar. TV Tropes da 403 directo por WebFetch y por curl; su copia en Wayback Machine también está bloqueada por política de red del contenedor («Blocked by egress policy» / reset de conexión), confirmado en dos intentos.
- Arctic Shift (Reddit) probado con el parámetro correcto (`query=`, no `q=`) sobre r/Konosuba, sin dato nuevo aprovechable para mis puntos.
