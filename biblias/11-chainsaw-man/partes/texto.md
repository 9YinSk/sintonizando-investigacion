# Parte de TEXTO · Chainsaw Man (encargo 11)

Repaso corto (biblia ya tiene los puntos 1-17 y 19-21; faltan 18-25). Este
investigador cubre **18 (estilo y técnica), 24 (obras parecidas) y 25 (mundo,
historia y símbolos)**, según la tabla de «Repaso corto» de `EQUIPO.md`. Parto
de `partes/datos-texto.md` (AniList: staff, recomendaciones, obras
relacionadas) y no repito esas consultas.

## Hallazgos

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Manga (Tatsuki Fujimoto, a mano/digital):**
- Línea **gruesa, suelta y «sketchy»**, no la línea limpia y uniforme de
  manga contemporáneo (compara con Naruto o We Never Learn); la línea se
  vuelve más nerviosa en el movimiento ✅ ([Anime News Network: «The
  Chainsaw Man Anime's Style Feels Off»](https://www.animenewsnetwork.com/feature/2022-11-18/the-chainsaw-man-anime-style-feels-off/.191720),
  análisis de estilo en [FandomWire](https://fandomwire.com/chainsaw-mans-6-ugliest-manga-panels-prove-tatsuki-fujimotos-artstyle-can-never-beat-gege-akutamis-jjk/)).
- **Sombreado**: tramas grises (screentone) + tramado cruzado a pluma para
  dramatismo, **sin fórmula fija** de un capítulo a otro (a veces casi sin
  trama) ✅ (mismas dos fuentes).
- **Composición**: escenas de diálogo con fondos vacíos y viñetas
  «casi mudas» tipo plano de cine (ya en §6 de la biblia); las peleas
  cambian a sombras muy cargadas y fondos llenos de detalle y caos ✅
  (ANN; [CBR sobre las viñetas](https://www.cbr.com/greatest-chainsaw-man-manga-panels/),
  ya citado en §6).
- No se confirmó con qué programa dibuja Fujimoto: un hilo de Yahoo
  Chiebukuro dice que él sí es digital pero sus ayudantes hacen acabados a
  mano ⚠️ (una fuente, sin nombrar el programa)
  ([Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14222070749)).

**Anime (MAPPA, dirección Ryū Nakayama, 2022) — filosofía y pipeline 3D:**
- El estudio persiguió un **«3DCG orientado al dibujo»** (作画に寄せた3DCG):
  el director pidió que el 3D se integrara con la animación a mano, no que
  buscara el fotorrealismo ✅ ([CGWORLD parte 1, modelado](https://cgworld.jp/article/202303-chainsawman1.html)).
- **Software confirmado por CGWORLD** (revista técnica, entrevista al
  equipo): **3ds Max 2022** (modelado), **ZBrush 2021** (escultura de los
  demonios), **Substance 3D Painter 2021** (materiales), **Photoshop 2021**
  (retoque de texturas a mano encima del material), **Pencil+ 4 (v4.2.0)**
  (plugin de sombreado tipo cel/toon), **KM-3D Cloth Deform 1.0** (tela sin
  simulación física completa) ✅ (mismo artículo, dos veces: texto y
  metadatos del propio CGWORLD).
- Chainsaw Man y Samurai Sword llevan **3 niveles de detalle (LOD)**: plano
  general, plano medio y primer plano con pupilas visibles ✅ (misma
  fuente).
- El **rig** de Chainsaw Man controla cada diente y cada eslabón de cadena
  por separado, y el cuello gira automáticamente para que la corbata no
  atraviese el cuerpo ✅ (misma fuente).
- **Fotografía/compositing** (撮影): **After Effects** + el plugin de
  gradación **Magic Bullet Looks** + **PSOFT CelFX**; el director de
  fotografía **Teppei Itō** aplica un color complementario a cada plano
  (naranja sobre escenas azules) para bajar contraste y saturación y dar
  «aire de acción real», con seguimiento fotograma a fotograma para igualar
  los materiales 2D con los modelos 3D en movimiento ✅ ([CGWORLD parte 3,
  fotografía](https://cgworld.jp/article/202303-chainsawman3.html)). El
  mismo artículo describe **«envolturas» de luz ambiental y cambios de
  color atmosférico** (brillo/*glow* alrededor de las fuentes de luz) y
  capas de humo, sangre y agua compradas como stock, con desenfoque de
  profundidad de campo incluso en detalles pequeños (la espuma de una
  cerveza) ✅ (misma fuente) — es el «brillo» que pide el punto 18, además
  del grano.
- **Encuadre y cámara**: paleta apagada de tono naturalista + luz de tipo
  cinematográfico, con homenajes directos: plano-secuencia con primer plano
  extremo al estilo Tarantino en el paseo de Power hacia el despacho de
  Makima; «plano tatami» al estilo Ozu en el primer viaje en coche de Denji
  y Makima; punto de vista en primera persona en el callejón del ep. 12;
  planos generales extremos tras las peleas para mostrar el destrozo ✅
  ([Anime Herald, con cita de Kevin Cirugeda/Sakuga Blog](https://www.animeherald.com/2023/06/03/how-the-chainsaw-man-anime-adaptation-grounded-itself-in-filmic-realism/)).
- En el ep. 8 (pelea en la azotea) la cámara sube en primer plano sobre
  Katana Man, pasa a plano general y vuelve a primeros planos antes de la
  carga final: composición en capas, no un solo encuadre ✅ (misma fuente).
- El *opening* de la T1 («KICK BACK») recrea, plano a plano, escenas de
  películas reales como homenaje directo (ya apuntado en §1/§11 de la
  biblia con la lista de películas; aquí se confirma que es **plano a
  plano**, no sólo temático) ✅ (misma fuente Anime Herald).

**Cómo reproducirlo en Photoshop y Blender** (guía propia, a partir de lo
anterior — no es cita, es traducción a herramientas de escritorio):
- **Blender**: escultura en *Sculpt Mode* para los demonios (equivalente a
  ZBrush); contorno grueso con **Solidify + normales invertidas** o con
  **Freestyle** (línea propia de Blender, ajustando grosor por distancia a
  cámara como hacían con sus 3 LOD); *Cloth Simulation* nativa para la ropa
  suelta (equivalente al KM-3D Cloth Deform); un nodo *Shader to RGB* +
  *Color Ramp* de 2-3 tonos sobre el difuso para el sombreado plano tipo
  cel; luz de tres puntos suave, sin especular dura, para el aire «real».
- **Photoshop**: capa de ajuste **Balance de color/Curvas** con tinte
  complementario (naranja sobre azul o al revés) para imitar el grading de
  Itō; capa de **grano de película** (Filtro > Ruido, o una textura de
  grano en modo Superponer al 8-15 %) y una viñeta suave; para el contorno
  de línea gruesa del manga, pincel de tinta con presión variable y una
  capa de trama (Screen Tone) al 20-30 % en vez de degradado limpio.
- **Rigs y modelos 3D libres del personaje** (para no partir de cero en
  Blender): en Sketchfab hay varios modelos de Denji/Chainsaw Man con
  licencia **CC Attribution** (CC-BY), algunos ya con huesos («Denji
  (Chainsaw-Man) (Yes Rigged bone)», [sketchfab.com/3d-models/none-bdd7c53adfc54033b47fb8e3f60545b1](https://sketchfab.com/3d-models/none-bdd7c53adfc54033b47fb8e3f60545b1);
  también «Denji (Chainsaw Man)», [...55234e1109bc40819168fadbf5869fca](https://sketchfab.com/3d-models/none-55234e1109bc40819168fadbf5869fca),
  y «Denji and Pochita», [...aa07c407793d48dca02f8b27ba79d397](https://sketchfab.com/3d-models/none-aa07c407793d48dca02f8b27ba79d397))
  ✅ (API de Sketchfab, `search?q=chainsaw+man+denji&downloadable=true`);
  ⚠️ **verificar cada uno al descargar**: son fan art no oficial, la
  licencia la pone quien sube el modelo, no Shueisha/MAPPA — usarlos sólo
  como base de pose/proporciones, citando autor y enlace.
- **Sobre «filtros» tipo aberración cromática/halación**: el plugin que usó
  MAPPA (**Magic Bullet Looks**) sí trae herramientas de aberración
  cromática y halación de fábrica, pero el artículo de CGWORLD **no dice
  explícitamente** que Chainsaw Man las use ⚠️ (no lo encontré confirmado;
  lo que sí confirma es el grano y el tinte de color complementario,
  arriba). Si se quiere ese efecto extra en Photoshop, un filtro de
  aberración cromática sutil (desplazar 1-2 px los canales rojo y azul) es
  coherente con «cámara real», pero no está documentado como parte del
  estilo oficial de la serie.

### Punto 24 · Obras parecidas y temas relacionados

- Recomendaciones automáticas de AniList (ya en `datos-texto.md`, no
  repetido aquí): *Jujutsu Kaisen*, *Dorohedoro*, *Devilman Crybaby*,
  *Dandadan*, *Parasyte*, *Hell's Paradise*, *Kaiju No. 8*, *Tokyo Ghoul*,
  *Zom 100*, *Undead Unluck*, *Attack on Titan*, *FLCL*.
- **El propio Fujimoto** describió su serie como **«una copia de Dorohedoro
  y Jujutsu Kaisen»**, un **«FLCL malvado»** y un **«Abara pop»** (Abara es
  un manga de Tsutomu Nihei, el de *Blame!*) ✅ ([Wikipedia
  EN](https://en.wikipedia.org/wiki/Chainsaw_Man), sección de producción;
  ⚠️ cita indirecta, no vi la entrevista original en japonés).
- Comparó el tono de la **2.ª parte** con ***El gran Lebowski*** (por su
  final ambiguo) ✅ (misma fuente).
- **Influencias directas** citadas por Fujimoto: ***La matanza de Texas***
  (1974) — «el motosierra molaba», origen literal del nombre — ✅
  ([FandomWire](https://fandomwire.com/tatsuki-fujimoto-took-inspiration-from-iconic-30-9-million-movie-texas-chainsaw-massacre/),
  [Wikipedia EN](https://en.wikipedia.org/wiki/Chainsaw_Man)); el clímax de
  la 1.ª parte se inspiró en la **pelea final de *Kizumonogatari Parte 3:
  Reiketsu*** (2016) ✅ (Wikipedia EN); el arco de Reze (manga y película)
  se inspiró en ***Jin-Roh: La Brigada del Lobo*** (tono y alegoría de
  Caperucita Roja) y en ***Before Sunrise*** de Linklater (estructura de
  cita romántica) ✅ ([SlashFilm](https://www.slashfilm.com/2020861/chainsaw-man-the-movie-reze-arc-romance-before-sunrise-inspiration/)).
- En el folleto de la película *Arco de Reze* Fujimoto mezcla referencias
  «serias» con disparatadas: cita además ***FLCL***, ***Sharknado***,
  ***Interstellar***, ***El club de la tifón*** (台風クラブ) y ***Hereditary***,
  y hasta *Winnie the Pooh*, como cosas que le gustan (comentarios de tomo,
  costumbre suya) ✅ ([búsqueda en japonés: realsound.jp](https://realsound.jp/book/2023/01/post-1229201.html),
  [shachikudayo.com](https://www.shachikudayo.com/entry/2022/07/27/190025),
  [EpicStream en inglés](https://epicstream.com/article/things-that-inspired-chainsaw-man-creator-tatsuki-fujimoto)).
- **Comparación crítica recurrente con *Devilman* de Go Nagai**: sexo y
  violencia crudos, protagonista que muere y resucita fusionado con un
  demonio; varios medios llaman a Chainsaw Man heredero directo de Devilman
  ✅ (dos fuentes independientes: [CBR](https://www.cbr.com/devliman-chainsaw-man-anime/),
  [artículo en Seize the Press](https://www.seizethepress.com/2024/02/10/rip-and-tear-stp9/)).
- **Qué otras láminas del servidor se le parecen** (para no repetir idea):
  comprobé todos los `encargos/*.md` y **ningún otro encargo apunta al
  canal #que-estas-viendo** ✅ (grep sobre 130+ encargos). En tono (sangre,
  violencia, tema adulto) las biblias ya escritas más cercanas son
  `18-death-note` (objeto: el cuaderno sobre la mesa) y
  `02-attack-on-titan` (objeto: la estela de piedra), pero usan canal y
  objeto distintos («textos», «reglas») — el concepto de «cine y entradas»
  de este encargo no se repite en ningún otro sitio del servidor ✅.

### Punto 25 · El mundo, la historia y sus símbolos

**Reglas del mundo, en 5 líneas** (✅ confirmado en Chainsaw Man Wiki y
cruzado con Wikipedia EN):
1. Los **Demonios** nacen en el **Infierno** del miedo colectivo humano a un
   concepto; cuanto más se teme ese concepto en el mundo, más fuerte es el
   demonio (por eso el Demonio Arma es casi invencible) ✅
   ([Fandom: Devil](https://chainsaw-man.fandom.com/wiki/Devil)).
2. Un demonio puede firmar un **Contrato** con un humano: a cambio de poder
   entrega algo (años de vida, un órgano, obediencia); el trato no se puede
   romper sin morir, salvo que el propio contrato incluya una cláusula de
   salida ✅ ([Fandom: Contract](https://chainsaw-man.fandom.com/wiki/Contract)).
3. Un **Endemoniado** (*Fiend*, 魔人) es un demonio que ocupa un cadáver
   humano y pierde poder al hacerlo; un **Híbrido** es un humano fusionado
   con un demonio vivo, como Denji con Pochita ✅ ([Fandom: Fiend](https://chainsaw-man.fandom.com/wiki/Fiend)).
4. La **Seguridad Pública** (gobierno) y el **Sector Privado** (mercenarios)
   cazan demonios en Japón; sólo los Cazadores de Demonios certificados
   pueden firmar contratos y llevar armas contra ellos ✅
   ([Fandom: Devil Hunter](https://chainsaw-man.fandom.com/wiki/Devil_Hunter)).
5. Los **Cuatro Jinetes** — Control (Makima, luego Nayuta), Guerra (Yoru),
   Hambruna (Fami) y Muerte — son los demonios más poderosos, eco directo de
   los Cuatro Jinetes del Apocalipsis bíblico (en japonés se usa 騎士,
   «caballero», la palabra normal para ese concepto) ✅
   ([Fandom: Four Horsemen](https://chainsaw-man.fandom.com/wiki/Four_Horsemen)).
- Cruce con **Wikipedia EN** (misma definición de demonios/contratos/
  híbridos, con otras palabras): ✅ doble fuente confirmada.

**La historia por arcos**, con capítulos (fuente: Chainsaw Man Wiki,
páginas *Public Safety Saga* y *Academy Saga*, ✅ en las dos):

*Parte 1 — Saga de Seguridad Pública* (cap. 1-97, dic-2018 a dic-2020):
- **Arco de introducción** (1-4): Denji conoce a Pochita, muere y nace
  Chainsaw Man.
- **Arco del Demonio Murciélago** (5-13): rescata al gato de Power.
- **Arco del Demonio Eternidad** (14-22): misión por un fragmento del
  Demonio Arma.
- **Arco de Katana Man** (23-38): venganza tras un ataque a la División
  Especial 4.
- **Arco de la Chica Bomba** (39-52): romance con Reze, que resulta ser una
  bomba humana — **aquí está la escena del cine del canal** (cap. 39, ya
  en §2 de la biblia).
- **Arco de los Asesinos Internacionales** (53-70): Denji, ya famoso, es
  objetivo mundial.
- **Arco del Demonio Arma** (71-79): batalla final contra el Demonio Arma.
- **Arco del Demonio Control** (80-97, final de la parte 1): Makima se
  revela como el Demonio Control; Denji la mata.

*Parte 2 — Saga de la Academia* (cap. 98-232, jul-2022 a **25-mar-2026**,
fin de la serialización) ⚠️ (la fecha de fin la da la propia wiki; no la
crucé con una segunda fuente porque cae fuera del backup habitual de
noticias que consulté):
- **Arco del Demonio Justicia** (98-111): Asa Mitaka se fusiona con Yoru,
  el Demonio Guerra.
- **Arco de las citas con Denji** (112-120): acuario y casa de Denji.
- **Arco del Demonio Caída** (121-131): Chainsaw Man salva a Asa y Yoru.
- **Arco de la Iglesia de Chainsaw Man** (132-155): una iglesia que idolatra
  a Chainsaw Man mueve sus hilos en la sombra.
- **Arco del Demonio Vejez** (156-190): Denji toca fondo (pierde casa y
  mascotas) mientras buscan a Nayuta.
- **Arco del Demonio Muerte** (191-232, final de la serie): el Demonio
  Muerte llega a la Tierra; desenlace de toda la obra.

**Emblemas, logos y objetos icónicos:**
- El **cordón/cremallera en el pecho de Denji**: al tirar de él le salen
  motosierras de la cabeza y los brazos. Es el gesto y objeto que define
  visualmente a «Chainsaw Man» ✅ en dos páginas de la misma wiki (Denji,
  Pochita), coherentes entre sí; ⚠️ no encontré una fuente fuera de Fandom
  que lo llame explícitamente «objeto icónico», aunque es un hecho de trama
  muy conocido y se ve en toda la mercancía oficial.
- El **traje negro con corbata** de los Cazadores de Demonios de Seguridad
  Pública (resiste el fuego) es el uniforme reconocible de la organización
  ✅ ([CBR: «The Public Safety Commission, Explained»](https://www.cbr.com/chainsaw-man-public-safety-commission-explained/));
  **no existe un escudo o emblema oficial documentado** para la División
  Especial 4 más allá del propio traje ⚠️ (lo busqué en el wikitexto de la
  wiki, en VS Battles Wiki y en CBR; no aparece ningún emblema, sólo el
  nombre completo **Tokyo Special Division 4**).
- El logo de la franquicia (letra a mano, bordes dentados) ya está descrito
  en la §6 de la biblia: no lo repito aquí.

**Vocabulario propio** (para IA de imagen y de texto, complementa la §17 de
la biblia que hace el redactor):
Demonio (*Devil*), Endemoniado (*Fiend*), Híbrido (*Hybrid*), Contrato
(*Contract*), Cazador de Demonios (*Devil Hunter*), Seguridad Pública /
Sector Privado, Infierno (*Hell*), Cuatro Jinetes (*Four Horsemen*), Nayuta
(reencarnación-niña del Demonio Control), miedo primigenio/colectivo (lo
que da fuerza a un demonio, útil para explicar «amenaza» sin ser gráfico).

---

## Lo mejor para la lámina

1. El grading real de Itō (naranja sobre azul, grano fino, contraste bajo)
   es la clave para que el fondo de cine de la lámina no parezca «plano»:
   aplicarlo con una capa de ajuste, no dejarlo saturado.
2. La línea gruesa y las tramas cruzadas de Fujimoto (sin limpieza tipo
   JJK) dan la textura «sucia» de 1997 que ya pide la biblia: coherente con
   la sala de cine, no con un dibujo pulido.
3. El propio Fujimoto ama el cine tanto como Makima: usar carteles de
   películas reales que él mismo cita (*El gran Lebowski*, *Jin-Roh*,
   *Kizumonogatari*) como pósters de fondo en la sala, mejor que carteles
   inventados.
4. El cordón del pecho de Denji es el objeto-símbolo más reconocible de
   toda la franquicia: sirve como detalle pequeño y no explícito (un
   llavero, un tirador) sin tener que dibujar sangre ni pelea.
5. No hace falta más lore de terror para un canal tranquilo: los Cuatro
   Jinetes y el resto del mundo quedan mejor como dato de fondo (por si se
   hace una lámina 2) que como texto visible aquí.

## No encontré

- ⚠️ Un **emblema oficial** (escudo/logo) de la División Especial 4 o de
  Seguridad Pública, distinto del traje negro: lo busqué en el wikitexto de
  Chainsaw Man Wiki, en VS Battles Wiki y en CBR.
- ⚠️ Un artículo (fuera de Fandom) que llame explícitamente «objeto
  icónico» al cordón del pecho de Denji; el hecho de trama está clarísimo
  en dos páginas de la propia wiki, pero es una única fuente de origen.
- ⚠️ El programa de dibujo exacto de Fujimoto para el manga (¿Clip Studio
  Paint?): sólo un hilo de Yahoo Chiebukuro dice que es digital, sin
  nombrar el programa; no hay entrevista oficial que lo confirme.
- ⚠️ Una entrevista en **coreano** sobre las influencias de estilo de
  Fujimoto: sólo encontré fichas de personajes en NamuWiki, no artículos de
  análisis de estilo o técnica en coreano o chino.
- La cita original en japonés de «una copia de Dorohedoro y Jujutsu
  Kaisen»: la tomé de Wikipedia en inglés (que sí cita su fuente), no vi el
  original.

## Bitácora

- Fandom API (`chainsaw-man.fandom.com/api.php`, texto e imágenes no
  necesarias aquí): `allpages` (para listar los arcos), `Public Safety
  Saga`, `Academy Saga`, `Devil`, `Contract`, `Fiend`, `Devil Hunter`,
  `Four Horsemen`, `Pochita`, `Denji`; búsquedas de texto `story arc`,
  `Four Horsemen`, `ripcord OR pull cord`, `Public Safety emblem OR
  symbol`.
- WebSearch (inglés): «Tatsuki Fujimoto influences movies interview
  Chainsaw Man inspiration»; «Chainsaw Man anime CGWORLD 3DCG making of
  interview MAPPA»; «Chainsaw Man anime color grading film grain
  cinematography Ryu Nakayama director interview»; «Chainsaw Man manga art
  style thick lines screentone rough sketchy Fujimoto analysis»; «Chainsaw
  Man compared to Devilman Go Nagai influence critics»; «Chainsaw Man
  Special Division 4 armband emblem Public Safety uniform devil hunter».
- WebSearch (japonés): «チェンソーマン 藤本タツキ 影響 映画 インタビュー»;
  «cgworld.jp チェンソーマン CG 制作 record»; «藤本タツキ 作画 使用ソフト
  クリップスタジオ デジタル 原稿».
- WebFetch: `animeherald.com` (realismo fílmico, cita a Kevin
  Cirugeda/Sakuga Blog); `cgworld.jp/article/202303-chainsawman1.html`
  (modelado 3D); `cgworld.jp/article/202303-chainsawman3.html`
  (fotografía/compositing); `en.wikipedia.org/wiki/Chainsaw_Man` (mundo e
  influencias); `medium.com/making-comics/...` — **403, no sirvió**.
- Comprobé `encargos/*.md` (130+ archivos) con `grep` para confirmar que
  ningún otro encargo usa el canal #que-estas-viendo, y miré los objetos de
  las biblias ya escritas con tono parecido (`18-death-note`,
  `02-attack-on-titan`) para el punto 24.
- No usé el buscador de imágenes ni `investigar_serie.py`: mis tres puntos
  (18, 24, 25) son de técnica, comparación y lore, no de arte nuevo; eso lo
  cubre el investigador de imagen.

Sigue: nada pendiente de lo obligatorio en los puntos 18, 24 y 25. Si hay
tiempo extra: buscar una fuente en coreano o chino sobre estilo/técnica (⚠️
en «No encontré», no es obligatorio para estos tres puntos) y confirmar con
una segunda fuente la fecha de fin de serialización (25-mar-2026).
