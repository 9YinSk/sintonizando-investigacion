# Investigador de TEXTO — Konosuba
_Puntos 5, 6, 11, 18, 24 y 25 de ENCARGO.md_
_Escrito el 2026-09-26_

---

## Hallazgos

### Punto 5 — Tipografía

**Logo**
- Logo del manga (「この素晴らしい世界に祝福を」): los kanji van en **まーと太角ゴシック** (Māto Futokaku Gothic, CFONT/Design Pocket — gótica japonesa gruesa de esquinas cuadradas) y el hiragana en **やさしいキモチつながるココロ** · ⚠️ una sola fuente (tuit de [@designpocket_jp](https://x.com/designpocket_jp/status/1261653378486071296), cuenta especializada en identificar tipografía de diseño japonés)
- Diseñador de logo/título acreditado en el equipo del anime: **Ushio Funayama** (舩山潮), "Title Logo Design" · ⚠️ una sola fuente ([AniList staff](https://anilist.co/anime/21202/staff), ya en `datos-texto.md`); no encontré una segunda fuente que lo confirme
- Letra libre equivalente para el logo en español: **Archivo Black** (Google Fonts, OFL) — gótica gruesa de remates cuadrados, mismo peso visual · ✅ comprobada la cobertura de ñ/¿/¡/tildes vía [API de Fontsource](https://api.fontsource.org/v1/fonts/archivo-black) (subset `latin`, rango Unicode U+0000-00FF incluye ñ=00F1, ¿=00BF, ¡=00A1, á/é/í/ó/ú)

**Cartelas de título de episodio (dentro del anime)**
- Cada episodio abre con una cartela propia: fondo oscuro estrellado/acuático, un **cubo de cristal cian flotante**, Aqua flotando arriba, y el texto "第◯話" + el título en una **gótica redondeada muy gruesa, relleno cian y borde claro**, con efecto de brillo/glitch pixelado en los bordes · ✅ medido directamente en `File:Episode 1 Title.png` y `File:Episode 4 Title.png` (Fandom, 1920×1080 cada una): relleno cian **#0CA9F8**, fondo casi negro
- Letra libre equivalente: **Baloo 2 ExtraBold** o **Fredoka Bold** (Google Fonts, OFL, redondeadas y gruesas) · ✅ subset `latin` confirmado vía Fontsource (ñ/¿/¡/tildes cubiertos)

**El alfabeto ficticio del mundo (cartel del mundo)**
- En pergaminos, carteles y la ficha de aventurero del anime aparece un **alfabeto latino inventado** (no es inglés real). Un fan (`u/-Alexor-` en Reddit) lo transcribió por primera vez sólo con mayúsculas; otro fan (HarJIT) lo amplió a minúsculas, números y signos, y lo convirtió en fuente TTF descargable (`Konosuba2/3/4-Regular.ttf`) — trabajo de fans, sin aval oficial · ✅ [harjit.moe/konosubanomoji.html](https://harjit.moe/konosubanomoji.html), [hilo original de Reddit](https://www.reddit.com/r/Konosuba/comments/6288ap/konosuba_font/)
- **Comprobado con fontTools** (`Konosuba4-Regular.ttf`, 141 glifos): tiene **¿ y ¡** ✅, pero **NO tiene ñ ni vocales con tilde** (á, é, í, ó, ú todas ausentes) ❌ — si se usa para un cartel en español hay que evitar palabras con tilde o ñ, o sustituir esas letras a mano
- Incluye además símbolos propios: el sigilo de Aqua/Axis (una especie de @) y el de Eris (parecido a $/€) en las versiones 3 y 4 de la fuente

**Cuadros de diálogo del videojuego oficial** (ver también punto 6)
- *Love For These Clothes Of Desire!* (Steam, 2024): el texto va en una **serif redondeada gruesa, blanca, con sombra/contorno gris azulado** sobre el pergamino · ⚠️ no identifiqué el nombre exacto de la fuente
- Letra libre equivalente propuesta: **Alegreya Bold** o **Bitter Bold** (Google Fonts, serif con personalidad de libro antiguo) · ✅ subset `latin` confirmado (ñ/¿/¡/tildes)

**Interfaz de *Fantastic Days*** (gacha móvil)
- Texto de los globos de tutorial: **sans blanca gruesa y redondeada**, sin serifa · ⚠️ fuente no identificada
- Libre equivalente: **Baloo 2** (ya recomendada arriba) o **Varela Round** · ✅ subset `latin` confirmado

**Subtítulos oficiales**
- No conseguí una captura propia de subtítulos oficiales en español (Crunchyroll) esta sesión para medir la fuente — YouTube pide iniciar sesión desde este servidor y no encontré el tráiler doblado en Dailymotion/Internet Archive a tiempo. Queda en "No encontré".

---

### Punto 6 — Cómo hablan y piensan en pantalla

**Videojuego *Love For These Clothes Of Desire!*** (Steam, MAGES./PQube, 2024) — medido directamente en 4 capturas oficiales 1920×1080 de la tienda de Steam:
- El cuadro de diálogo es un **pergamino desenrollado horizontal**, con los **extremos enrollados en cilindro** visibles a los lados (sobre todo a la derecha).
- El nombre de quien habla va en una **cinta/banderín en forma de pergamino pequeño** arriba a la izquierda, con esquinas en cola de golondrina y un filete fino con una voluta decorativa.
- Borde superior e inferior del pergamino con un **patrón de triángulos/dientes en marrón anaranjado**, como una greca cosida.
- Abajo a la derecha, un pequeño **rombo/gema cian** hace de indicador de "seguir".
- Colores medidos: pergamino de fondo **#D6C57C**, cinta del nombre **#D1A461**, filete/borde naranja **#B36F1A**, barra de créditos inferior (marrón muy oscuro) **#481312**.
- Las **elecciones de diálogo** usan el mismo pergamino pero más claro, en lista vertical, con flechas «‹ ›» a los lados para desplazar.
- El **menú de planificación semanal** (fuera del diálogo) usa la misma paleta pergamino/marrón oscuro con iconos circulares por tarea.
- ✅ fuente: [Steam Store — appid 2349140](https://store.steampowered.com/app/2349140/), capturas oficiales descargadas y medidas con Pillow

**Videojuego *Konosuba: Fantastic Days*** (Sumzap, gacha móvil, 2020-2025) — medido en 4 capturas oficiales del tutorial de batalla en `konofan.fandom.com` (2232×1080):
- Los tutoriales/avisos de combate van en una **burbuja redondeada rosa magenta con pico apuntando** hacia lo que señala (sin retrato de personaje).
- Texto blanco, grueso, centrado.
- Los iconos de habilidad van en **cuadrados redondeados oscuros** en la parte baja de la pantalla; arriba de cada personaje hay una barra de espera/vida pequeña con iconos.
- Color medido del magenta: **#DC3478** aprox. (rango #D0276F–#E73178 según la zona) — coincide con el color de marca oficial **#E3026B** que la propia wiki usa como fondo de las pestañas de este juego en su plantilla.
- ✅ fuente: [konofan.fandom.com — Battle tutorial](https://konofan.fandom.com/wiki/Battle_tutorial), imágenes descargadas y medidas

**Manga** (Masahito Watari, en *Gekkan Dragon Age* desde sept. 2014)
- Dos reseñas (FandomPost, Taykobon) señalan una técnica propia de Watari: **los apartes y chistes pequeños van en texto más chico dentro del MISMO globo** que la frase principal, dando un efecto de "dicho entre dientes" · ⚠️ una sola fuente (no pude abrir ninguna de las dos páginas directamente — FandomPost dio 403 y Taykobon dio error 521; el dato viene de los fragmentos que devolvió la búsqueda)
- No encontré una página de manga real para medir la forma exacta de los globos (ver «No encontré»): Danbooru/Safebooru no devolvieron páginas de manga etiquetadas para esta serie con los límites de 1-2 etiquetas que aceptan sin cuenta.

**Cartelas de título de episodio** (anime): ver punto 5 — cubo cian + Aqua + texto cian sobre fondo estrellado, en cada episodio de las temporadas principales.

**Objeto-interfaz del propio mundo: la Máquina de Fichas del Gremio de Aventureros**
- En vez de un menú de pantalla, el Gremio de Axel usa un **aparato físico**: una esfera de cristal **cian brillante** rodeada de un aro dorado con piñones y púas, sobre patas retorcidas de bronce oscuro tipo raíz/tentáculo, con acentos cian que gotean del pedestal.
- Es el objeto más parecido a una "interfaz" que tiene la serie fuera de los videojuegos: convierte el típico panel de estadísticas de un RPG en un objeto real dentro del mundo — ideal para el punto 17 y para "un objeto real en un sitio real" de `reglas_del_dueno.md`.
- Colores medidos: esfera cian **#30EEDE**, aro dorado **#DBCE90**, patas oscuras **#282425**.
- ✅ fuente: [Fandom — File:Card Machine.JPG](https://konosuba.fandom.com/wiki/File:Card_Machine.JPG), 848×480, medida directamente

---

### Punto 11 — Videojuegos de la franquicia

Konosuba tiene **seis** videojuegos oficiales (ninguno tiene versión en español); resumen con lo que pude verificar de su interfaz:

| Juego | Año | Plataforma | Desarrollador/editor | Qué es | Interfaz/diálogo |
|---|---|---|---|---|---|
| **KonoSuba: in the life** | 2016 | PC (RPG Maker VX) | fan-made con reconocimiento oficial, repartido con el BD/DVD vol. 1 | RPG estilo años 90, cubre las primeras novelas | No conseguí captura del cuadro de diálogo; por ser RPG Maker VX es casi seguro el cuadro por defecto del motor (caja rectangular translúcida abajo) ⚠️ sin confirmar |
| **KonoSuba: Judgment on this Greedy Game!** | 2017 | PS Vita / PS4 | 5pb. (des.) / Capcom (ed.) | Novela visual: Kazuma debe devolver ropa interior robada por una maldición | ⚠️ no conseguí capturas de su caja de diálogo propia |
| **KonoSuba: Labyrinth of Hope and the Gathering Adventurers (+ Plus)** | 2019 / Plus 2020 | PS Vita/PS4/Switch/Xbox | Entergram (des.) / Capcom y SNK (ed.) | RPG de mazmorras tras la temporada 2 | Tiene página propia en **The Cutting Room Floor** (contenido descartado): un archivo `ADV\test.txa` dentro de `FILES.psarc` guarda una pantalla de título temprana/maqueta sin usar · ⚠️ una sola fuente (la página de TCRF da 403 por Cloudflare al abrirla directo; el dato viene del fragmento de búsqueda) — [tcrf.net/Kono_Subarashii_Sekai_ni_Shukufuku_wo!...(PlayStation_Vita)](https://tcrf.net/Kono_Subarashii_Sekai_ni_Shukufuku_wo!_~Kibou_no_Meikyuu_to_Tsudoishi_Boukensha-tachi~_(PlayStation_Vita)) |
| **KonoSuba: Fantastic Days** | 2020–2025 (cerrado; versión offline hasta ene. 2027) | Android/iOS/PC | Sumzap | Gacha RPG por turnos con diseños SD, historia original, doblaje completo | Ver punto 6: burbujas de tutorial rosa magenta, iconos redondeados ✅ medido |
| **Kono Yokubou no Ishou ni Chouai wo!** ("Love For These Clothes Of Desire!" en Occidente) | 2019 JP / 2024 internacional | PS4/Vita (JP) · PC Steam (internacional, MAGES./PQube) | MAGES. | Novela visual: una "Losa Negra" maldita cambia la personalidad de las chicas | Ver punto 6: caja de pergamino ✅ medido a fondo |
| **KonoSuba: in the life** (ver arriba) también cuenta como aparición en videojuego "cameo": el crossover **Isekai Quartet** (2019, no es un videojuego, es un anime crossover — lo dejo fuera de esta tabla) | — | — | — | — | — |

- No hay ningún juego de consola con demo/interfaz jugable en Steam más allá del ya cubierto; no encontré ninguno con capturas propias en **Game UI Database** (`gameuidatabase.com`) — busqué "Konosuba" y no aparece listado ⚠️.

---

### Punto 18 — Estilo de dibujo y técnica, y cómo replicarlo

**Estudios y equipo, por temporada** ✅ (dos fuentes: [Fandom — Anime](https://konosuba.fandom.com/wiki/Anime) tabla de staff, y [ONE Esports](https://www.oneesports.gg/anime/konosuba-season-3-studio-animation/) / [Anime News Network](https://www.animenewsnetwork.com/news/2023-06-21/konosuba-god-blessing-on-this-wonderful-world-3-anime-to-air-in-2024/.199473) para S3):
- Temporadas 1-2 (2016-2017): **Studio DEEN**, director Takaomi Kanasaki
- Película *Legend of Crimson* (2019): **J.C.Staff**, mismo director/reparto/compositor
- Spin-off *An Explosion on this Wonderful World!* (2023) y Temporada 3 (2024): **Studio Drive**, Kanasaki pasa a director en jefe y **Yujiro Abe** dirige episodio a episodio; el diseñador de personajes **Koichi Kikuta** se mantiene en las cuatro etapas

**Entrevista al diseñador de personajes Koichi Kikuta** (revista *Anime Style* 009, julio 2016; traducida por Wave Motion Cannon) ✅ — [wavemotioncannon.com](https://wavemotioncannon.com/2017/02/07/konosuba-interview-with-koichi-kikuta-anime-style-009-july-2016/):
- Su filosofía: *"la calidad de un anime está en los layouts, no en los personajes"* — prioriza composiciones "tipo cámara/foto" por encima del pulido de animación de personajes.
- No copió el estilo "mono" de las ilustraciones de la novela ligera: diseñó a los personajes para que mostraran **sus lados menos favorecedores** (caras raras, gestos poco favorecedores) en vez de la ternura del original, inspirado en el trazo simplificado y fácil de animar de **Takahiro Kishida**.
- Línea **mínima y económica**; su ideal es el dibujo tipo "sakuga".
- **Colores de pupila muy saturados** junto a tonos oscuros para dar degradado pintado sin retocar digitalmente; **sombra marcada bajo la nariz** como sello personal, influido por el animador de GoHands **Shingo Suzuki**.
- Aceptó caras "graciosas" fuera de modelo para la comedia, en vez de mantener siempre la consistencia del diseño.

**El hechizo Explosión, medido directamente** — descargué el clip oficial `File:Explosion.gif` de la wiki (35 fotogramas, 800×450) y lo analicé con `herramientas/estilo.py`:
- Fotograma inicial (Megumin apuntando, círculo mágico formándose): paleta dominante **#1D1409** (oscuro), **#E38A2B** (naranja medio), **#CE350A** (rojo); saturación 76%, brillo 46%; sombreado "degradado/pintado".
- Fotograma intermedio: paleta casi igual, saturación 75%, brillo 47%.
- Fotograma del estallido total (pantalla casi blanca): paleta vira a **#F8D170 / #FCECB1** (crema/amarillo claro), brillo sube a 76%, y la línea se adelgaza hasta "poca línea" — el contorno desaparece dentro de la propia luz.
- Animador acreditado por el fandom de sakuga como responsable de prácticamente todas las explosiones de Megumin: **Kazunori Ozawa** ⚠️ una sola fuente (síntesis de búsqueda, no verifiqué directamente un crédito de episodio)

**Ficha de personaje oficial (Megumin, corte transparente)** — `File:Megumin-anime.png` (300×600), medida con `estilo.py` sobre fondo blanco:
- Confirma **sombreado plano (cel)**, sin degradados en el cuerpo del personaje.
- Color de línea medido: **#85563E** (un marrón oscuro cálido, no negro puro) — coincide con la técnica habitual de anime de usar línea coloreada en vez de negro puro en zonas de piel/pelo.

**Cómo replicarlo en Photoshop**
- Rellenos planos por celda (selección + cubo, 2-3 tonos por color, sin degradado) para el cuerpo de los personajes.
- Una sola capa de sombra dura (modo Multiplicar, sin pincel suave) colocada bajo la nariz/mentón, siguiendo el sello de Kikuta.
- Línea en **marrón oscuro cálido** (no negro puro) de 2-3 px.
- Para el hechizo Explosión: una capa de degradado/resplandor (modo Trama o Aclarar, radial) que va de **#1D1409** en el borde a **#F8D170/#FCECB1** en el centro, imitando la escalada de brillo medida arriba; encima, un anillo de "círculo mágico" rojo con opacidad y algo de desenfoque de movimiento radial.

**Cómo replicarlo en Blender**
- *Shader to RGB* + *Color Ramp* posterizada a 2-3 escalones para el sombreado plano del cuerpo.
- Contorno con **Freestyle** o un modificador **Solidify** en marrón oscuro cálido (no negro).
- Para la Explosión: sistema de partículas/volumétrico de fuego (o una esfera con *Emission* + textura de ruido) controlado por un *Color Ramp* que barra oscuro→naranja→crema siguiendo los hex medidos arriba; un plano emisivo con textura del círculo mágico rojo, rotando, delante del personaje que lanza el hechizo.

**Encuadres y composición**
- No encontré un desglose plano a plano oficial más allá de la filosofía general de Kikuta citada arriba ("layouts tipo cámara"). Queda anotado en «No encontré» para no inventar reglas de encuadre por emoción que no pude verificar.

---

### Punto 24 — Obras parecidas y temas relacionados

**Influencias que el propio autor (Natsume Akatsuki) ha citado**, confirmadas en dos entrevistas distintas:
- *Record of Lodoss War* (ロードス島戦記), de **Ryo Mizuno**: la primera novela fantástica que leyó; dice que le "enganchó" al género y que construyó desde ahí el tipo de historias que escribe · ✅✅ dos fuentes: [ln-news.com, entrevista "Ranobe no Moto"](https://ln-news.com/articles/35149/1) y [sneakerbunko.jp, coloquio Lodoss×Konosuba con Mizuno](https://sneakerbunko.jp/lodoss30th/news/20190731_01.html)
- Manga favoritos citados: **Drifters** y **Hunter × Hunter** (dice preferir revistas seinen sobre shonen); otras novelas ligeras que marcaron su base: **Slayers** y **Sorcerous Stabber Orphen** · ✅ (ln-news.com)
- Videojuegos que menciona como influencia de su sensibilidad: **Dragon Quest Builders**, **Monster Hunter Frontier** y **Kantai Collection** — de este último sale su propio seudónimo "Akatsuki" (nombre de un barco del juego) · ✅ (ln-news.com)
- Su propia descripción de la fórmula de Konosuba: *"una comedia disfrazada de fantasía harem isekai"* (異世界ハーレムファンタジーの皮をかぶったコメディ作品); considera que el anime es casi "la versión real" y que la novela original funciona casi como su novelización · ✅ (ln-news.com)

**Lista curada de obras similares** (no algorítmica, con razones concretas) ✅ [GameRant](https://gamerant.com/best-isekai-anime-like-konosuba/):
- *Ixion Saga DT* — comedia cruda y autoconsciente de su propio absurdo
- *Outbreak Company* — sátira de la cultura otaku
- *Combatants Will Be Dispatched!* — **mismo autor**, mismo estilo de slapstick y personajes disfuncionales
- *Problem Children Are Coming From Another World* — grupo de personalidades chocantes
- *Magical Shopping Arcade Abenobashi* — parodia y juego con las expectativas del espectador
- *Cautious Hero* — protagonista que invierte el cliché isekai
- *My Next Life As A Villainess* — sátira del isekai/otome
- *The Devil Is a Part-Timer!* — comedia de "pez fuera del agua"
- *That Time I Got Reincarnated As a Slime* — isekai desenfadado

(Las recomendaciones algorítmicas de AniList ya están en `datos-texto.md`; no las repito.)

**TV Tropes**: existe una página (`Anime/KonoSubarashiiSekaiNiShukufukuWo` y `LightNovel/...`) pero **no pude abrirla**: da 403 tanto por `curl` directo como por la herramienta de lectura web, y no encontré una copia en Wayback Machine (`archive.org/wayback/available` no devolvió ningún snapshot) ⚠️ — queda en «No encontré».

---

### Punto 25 — El mundo, la historia y sus símbolos

**Las reglas del mundo, en cinco líneas** ✅ ([Terminology](https://konosuba.fandom.com/wiki/Terminology), [Magic](https://konosuba.fandom.com/wiki/Magic), Fandom):
1. El "Mundo Paralelo" es una fantasía tipo videojuego amenazada por el Rey Demonio, bajo la jurisdicción de la diosa Eris.
2. Todos tienen estadísticas de RPG (Fuerza, Vitalidad, Inteligencia, Poder Mágico, Destreza, Agilidad, Suerte) registradas en una **Ficha de Aventurero**.
3. La moneda es el **eris** (cobre/plata/oro/mithril; 1 mithril = 1.000.000 eris; 1 eris ≈ 1 yen, según Aqua).
4. Japón (moderno y pacífico) está bajo la jurisdicción de Aqua; morir allí y renacer en el Mundo Paralelo con un poder "tramposo" (Cheat) es la premisa de la serie.
5. Entre ambos mundos hay un Más Allá y un Cielo con tiempo distinto: una hora en el Más Allá equivale a un mes en Japón y a varios meses en el Mundo Paralelo.

**La historia por arcos** (temporada ↔ volumen de novela, confirmado cruzando la [tabla de staff/episodios de Fandom](https://konosuba.fandom.com/wiki/Anime) con la ficha de cada volumen) ✅:
- **T1** (2016, DEEN) — vol. 1 (sin título propio) + vol. 2 *"Love, Witches & Other Delusions!"*: llegada a Axel, se forma el grupo, primera Explosión de Megumin, el Destructor/Beldia.
- **T2** (2017, DEEN) — vol. 3 *"You're Being Summoned, Darkness"* + vol. 4 *"You Good-for-Nothing Quartet"*: Wiz y Vanir, el arco del casino de Baccarat.
- **Película "Legend of Crimson"** (2019, J.C.Staff) — vol. 5 *"Crimson Magic Clan, Let's & Go!!"*: la Aldea de los Demonios Carmesí, Sylvia/Hans.
- **Spin-off "Explosion"** (2023, Drive): precuela centrada en el pasado de Megumin (novela ligera propia, *Bakuen*, 2014-2019, mismo autor/ilustradora).
- **T3** (2024, Drive) — vol. 6 *"Princess of the Six Flowers"* + vol. 7 *"110-Million Bride"*.
- **T4**: anunciada para 2027, sin emitir todavía.

**Facciones y símbolos**
- **Demonios Carmesí (紅魔族, Crimson Demons)**: clan de magos de pelo oscuro y **ojos rojos que brillan cuando se emocionan**; todos nacen con un **tatuaje de código de barras** en un lugar aleatorio del cuerpo (son humanos modificados artificialmente por el mismo "Doctor" que creó al Destructor); personalidad chūnibyō, obsesión por poses y frases de presentación dramáticas, muchos son NEET · ✅ [Fandom — Crimson Demons](https://konosuba.fandom.com/wiki/Crimson_Demons)
- **Culto/Orden Axis (アクシズ教, culto de Aqua)**: emblema = **rombo celeste con borde blanco y un glifo de ola/rayo estilizado dentro** — medido directamente en la imagen oficial de la wiki (`File:AxisCult.png`, 480×480): azul ~**#8ABDCE**. Minoría fanática (unos pocos cientos de seguidores en todo el mundo), sede en los baños termales de Arcanletia, fama de captar gente de forma agresiva · ✅ [Fandom — Axis Order](https://konosuba.fandom.com/wiki/Axis_Order)
- **Orden de Eris (エリス教)**: fe nacional del Reino de Belzerg, más numerosa pero menos fanática que Axis; celebra el Festival de Apreciación de Eris cada verano · ✅ [Fandom — Eris Order](https://konosuba.fandom.com/wiki/Eris_Order)
- **Gremio de Aventureros**: su "Máquina de Fichas" (ver punto 6) es el objeto icónico más parecido a una interfaz física del mundo.
- **"Misión Durián" (Durian Quest)**: jerga de Axel para una misión cuya paga no compensa lo tediosa/peligrosa/desagradable que es — la comparan con la fruta durián, apreciada por pocos · ✅ [Fandom — Terminology](https://konosuba.fandom.com/wiki/Terminology)

---

## Lo mejor para la lámina

1. La **Máquina de Fichas del Gremio** (esfera cian + aro dorado + patas de bronce retorcido): objeto físico, hecho a mano para Blender, y es literalmente la "interfaz" del mundo convertida en objeto real — exactamente lo que pide `reglas_del_dueno.md`.
2. La **cartela de título de episodio** (cubo cian flotante + Aqua + texto cian grueso sobre fondo estrellado): plantilla lista para anunciar "capítulos" o secciones de un canal.
3. El **pergamino del videojuego oficial** (extremos enrollados, cinta con el nombre, gema cian): ya es el "objeto real en un sitio real" perfecto para un cuadro de diálogo con temática de fantasía/aventura, sin caer en la burbuja blanca genérica.
4. El **rombo celeste del culto Axis** (Aqua): pequeño, reconocible, fácil de repetir como sello o insignia.
5. La **paleta medida de la Explosión** (#1D1409 → #E38A2B → #CE350A → #F8D170): lista para un fondo "boom" cómico sin caer en colores planos ni en un naranja genérico de IA.

---

## No encontré

- **Nombre exacto de la fuente** del cuadro de diálogo del videojuego *Love For These Clothes Of Desire!* y de *Fantastic Days*: comprobado visualmente y medido en color, pero no identificado por nombre · ⚠️ buscado en dafont.com (el hilo "Konosuba this font" existe pero nadie respondió) y por comparación visual
- **Subtítulos oficiales en español** (Crunchyroll): no conseguí una captura propia esta sesión para medir la fuente — YouTube pidió iniciar sesión desde este servidor, y no encontré a tiempo el mismo tráiler en Dailymotion/Internet Archive con subtítulos quemados
- **Página real de manga** (para medir la forma exacta de los globos): Danbooru y Safebooru no devolvieron resultados con las combinaciones de 1-2 etiquetas permitidas sin cuenta; me quedé con lo que dicen dos reseñas (FandomPost, Taykobon) sobre el texto pequeño dentro del globo, pero no pude abrir ninguna de las dos páginas directamente (403 y error 521)
- **TV Tropes** (`Anime/KonoSubarashiiSekaiNiShukufukuWo`): da 403 por Cloudflare tanto por `curl` como por la herramienta de lectura web; no hay copia en Wayback Machine
- **The Cutting Room Floor**, página completa: existe y la confirmé por búsqueda (juego *Labyrinth of Hope*, PS Vita, con una pantalla de título temprana sin usar en `ADV\test.txa`), pero la página en sí da 403 por Cloudflare al intentar abrirla directamente
- **Interfaz de *KonoSuba: in the life*** (RPG Maker VX): no encontré capturas propias del juego, sólo confirmé que existe y su motor
- **Game UI Database** (`gameuidatabase.com`): no tiene ninguna entrada para juegos de Konosuba
- **Coreano/chino**: la obra es japonesa y su público de doblaje/localización relevante para el servidor es hispanohablante, así que prioricé japonés/inglés/español; sí hice una búsqueda en coreano sobre la interfaz de *Fantastic Days* (que tuvo lanzamiento en Corea vía Nexon) y sólo salieron reseñas generales, sin detalle de tipografía

---

## Bitácora de búsqueda

| Búsqueda | Idioma | Fuente | Resultado |
|---|---|---|---|
| Konosuba logo font identification | JA/EN | WebSearch | まーと太角ゴシック + やさしいキモチ (una fuente, tuit de diseño) |
| Kurone Mishima interview character design | EN | WebSearch | Llevó a la entrevista de Kikuta (Wave Motion Cannon), más útil |
| Koichi Kikuta interview (Anime Style 009) | EN | WebFetch | Traducción completa leída y citada |
| 暁なつめ インタビュー 影響を受けた作品 | JA | WebSearch | Lodoss War como influencia fundacional |
| ln-news.com entrevista Akatsuki | JA→ES | WebFetch | Influencias (Drifters, HxH, Slayers, Orphen, Lodoss, videojuegos) |
| gamerant best isekai anime like konosuba | EN | WebFetch | Lista curada con razones |
| Konosuba season 3 studio Drive | EN | WebSearch | Confirmado Drive, Kanasaki/Abe, Kikuta se mantiene |
| Konosuba sakuga explosion effects | EN | WebSearch | Animador Kazunori Ozawa (una fuente) |
| Konosuba manga review speech bubbles Masahito Watari | EN | WebSearch + WebFetch | FandomPost 403, Taykobon error 521; quedó el dato del snippet |
| harjit.moe konosubanomoji | EN | WebFetch + fontTools | Alfabeto ficticio del mundo; comprobado ñ/tildes ausentes, ¿/¡ presentes |
| dafont Konosuba this font | EN | WebFetch | Hilo sin respuesta |
| site:tcrf.net Konosuba | EN | WebSearch | Labyrinth of Hope (PS Vita) tiene página; la página en sí da 403 |
| TV Tropes Anime/KonoSubarashii... | EN | curl + WebFetch + Wayback | 403 en todos los intentos; sin snapshot en Wayback |
| 코노스바 폰트 대사창 게임 인터페이스 | KO | WebSearch | Confirma lanzamiento coreano (Nexon) de Fantastic Days; sin detalle tipográfico |
| Fandom API: Magic, Terminology, Axel, Crimson Demons, Axis Order, Eris Order, Anime, Kono Subarashii Sekai ni Shukufuku wo!, Kono Subarashii Sekai ni Bakuen wo! | EN | Fandom API (`action=parse`, wikitext) | Consultadas directamente, citadas arriba |
| Fandom: Konosuba: Fantastic Days, Judgment on this Greedy Game, in the life, Labyrinth of Hope, Love for these Clothes of Desire | EN | Fandom API | Las 5 fichas de videojuego leídas |
| Danbooru konosuba comic / 4koma | EN | API | Sin resultados con el límite de 2 etiquetas |
| Steam store search konosuba | — | curl | 4 productos; appid 2349140 identificado como el juego principal |
| Steam appdetails 2349140 | — | curl | Ficha completa + 13 capturas 1920×1080 |
| Descarga y medición de 4 capturas de Steam | — | Pillow / `estilo.py` | Colores del pergamino medidos |
| konofan.fandom.com Battle tutorial | — | Fandom API | 8 imágenes; 4 descargadas y medidas |
| File:Explosion.gif (konosuba.fandom.com) | — | Fandom API + Pillow + `estilo.py` | 35 fotogramas; 3 analizados con color y sombreado |
| File:Megumin-anime.png | — | Fandom API + Pillow + `estilo.py` | Línea y sombreado plano medidos sobre fondo blanco |
| File:Episode 1/4 Title.png | — | Fandom API + Pillow | Cartela de episodio medida (cian #0CA9F8) |
| File:AxisCult.png | — | Fandom API + Pillow | Emblema Axis medido |
| File:Card Machine.JPG | — | Fandom API + Pillow | Máquina de fichas del Gremio medida |
| Google Fonts / Fontsource: Archivo Black, Baloo 2, Fredoka, Alegreya, Varela Round | — | API de Fontsource | Cobertura de ñ/¿/¡/tildes confirmada por `unicodeRange` del subset `latin` |
| Konosuba4-Regular.ttf | — | fontTools | ¿/¡ presentes; ñ y vocales con tilde ausentes |

---

Sigue: subtítulos oficiales en español (medir fuente con un clip real cuando YouTube deje de pedir sesión, o probar Dailymotion/Internet Archive de nuevo), y confirmar por una segunda fuente el crédito de "Ushio Funayama" como diseñador del logo si aparece en algún artbook o making-of.
