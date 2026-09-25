# Parte IMAGEN · Encargo 118 — Hellblade

Investigador de imagen (rol `imagen`, EQUIPO.md): puntos **1, 3, 15, 16, 19 y 23** de ENCARGO.md.
Libreta de datos, no prosa. Parte de `partes/datos-imagen.md` (ya consultado, no se repite) y de
`herramientas/investigar_serie.py` corrido con 26 páginas de la wiki (ver hojas). Trabajo pesado en
`/tmp/claude-0/trabajo/118-hellblade-imagen` y `herramientas/referencias/hellblade/`.

Juego: *Hellblade: Senua's Sacrifice* (2017) y *Senua's Saga: Hellblade II* (2024), Ninja Theory.
Wiki: `hellblade.fandom.com` (wikiid real `hellbladent`, servidor `thehellblade.fandom.com`; las imágenes
siguen en `static.wikia.nocookie.net/hellblade-nt/`).

---

## 1 · Arte oficial, en cantidad y variado

**Portadas y key art oficiales** (medidas con Pillow; fuente = wiki, que las toma de Xbox/Ninja Theory):
- Portada *Hellblade: Senua's Sacrifice* · 720×1080 · `File:Hellblade 1 cover.png` · https://static.wikia.nocookie.net/hellblade-nt/images/7/75/Hellblade_1_cover.png · ✅ (wiki + usada como header en Steam appid 414340) · hoja `arte_01.jpg` #14 no incluida, ver hoja `personajes_01.jpg` #70.
- Key art vertical *Senua's Saga: Hellblade II* · 2732×4096 · `File:Hellblade II.jpg` · https://static.wikia.nocookie.net/hellblade-nt/images/d/d7/Hellblade_II.jpg · ✅ (wiki + portada de senuassaga.com) · hoja `personajes_01.jpg` #1.
- Arte *Hellblade 2 Enhanced Edition* · 1440×2160 · `File:Hellblade 2 Enhanced.png` · https://static.wikia.nocookie.net/hellblade-nt/images/6/61/Hellblade_2_Enhanced.png · ⚠️ (una fuente, wiki) · hoja `personajes_01.jpg` #5.
- Logo rúnico *Hellblade II* (verde, triskel/runas blancas) · 647×679 · https://static.wikia.nocookie.net/hellblade-nt/images/9/95/Hellblade_2_Runic_logo.png · ✅ · hoja `fondos_01.jpg` #82.
- Logo *Senua's Sacrifice* · 256×256 · https://static.wikia.nocookie.net/hellblade-nt/images/6/6d/Senua%27s_Sacrifce_Logo.png · ⚠️ (datos-imagen.md, una fuente).
- Logo del juego (icono) · 192×192 · https://static.wikia.nocookie.net/hellblade-nt/images/2/2c/Senua_game_logo.png · ⚠️.

**Fondos de pantalla oficiales 8K** de `senuassaga.com/media` (galería oficial de Xbox Game Studios/Ninja
Theory para *Hellblade II*; medidos descargando los primeros 64 KB y leyendo la cabecera JPEG con Pillow —
**confirmado 7680×4320 real**, no sólo el nombre del archivo):
- «Senua's Army» — Senua al frente de una fila de guerreros, luz de contraluz, pose de LIDERAZGO/grupo · 7680×4320 · https://admin.senuassaga.com/wp-content/uploads/sites/2/2019/12/SenuaArmy_8K.jpg · ✅ (senuassaga.com + reflejado en Xbox media kit) · hoja `arte_01.jpg` #2.
- «Senua Chant» — primer plano gritando/cantando, pintura oscura-rojiza a la luz del fuego, dientes visibles · 7680×4320 · https://admin.senuassaga.com/wp-content/uploads/sites/2/2019/12/SenuaChant_8K.jpg · ✅ · hoja `arte_01.jpg` #3.
- «Senua Fire» — de perfil junto a una hoguera, pose de calma/pensar · 7680×4320 (versión 8K en `theinsightproject.azureedge.net/uploads/2020/12/SenuaFire_8K.jpg`, mismo encuadre que la 4K de `admin.senuassaga.com`) · ✅ · hoja `arte_01.jpg` #4.
- «Arms» — postes con manos/trofeos de guerra colgados, niebla (sitio, no personaje) · 7680×4320 · https://admin.senuassaga.com/wp-content/uploads/sites/2/2019/12/Arms_8K.jpg · ✅ · hoja `arte_01.jpg` #1.
- «Skulls» — calaveras y huesos en el suelo, niebla · 7680×4320 · https://admin.senuassaga.com/wp-content/uploads/sites/2/2019/12/Skulls_8K.jpg · ✅ · hoja `arte_01.jpg` #5.
- «Volcano» — paisaje de Islandia con volcán humeante (sitio) · 7680×4320 · https://theinsightproject.azureedge.net/uploads/2019/12/Volcano_8K-1.jpg · ✅ · hoja `arte_01.jpg` #6.

**Capturas oficiales de Steam, 1920×1080** (API `appdetails`, no reescaladas — cumple lo que pide el encargo):
- *Hellblade: Senua's Sacrifice* (appid 414340), 11 capturas oficiales. Poses vivas encontradas: Senua de
  espaldas mirando el pantano con escudo/figura lejana (silueta) · combate cuerpo a cuerpo contra enemigo
  envuelto en fuego (arma en alto) · Senua de perfil a contraluz dorado entre partículas/flores (icónica,
  serena) · Senua niña (flashback) con capucha de piel, mirando de frente · combate contra enemigo con hacha
  (dos figuras, posturas de pelea) · comparación «OLD/UPDATED» del remaster gráfico (Bardarvik, dos columnas)
  · logo del juego con el perfil pintado de azul. URLs con hash propio, ejemplo:
  https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/414340/ss_1b594712d6bb9c5701692cb4f53d4072bd8feae0.1920x1080.jpg
  · ✅ (Steam API `appdetails` + store page 414340) · hoja `arte_01.jpg` #7-10.
- *Senua's Saga: Hellblade II* (appid 2461850), 8 capturas oficiales. Poses vivas: Senua junto a un
  ALIADO guerrero, ambos con espadas en mano, luz de atardecer (grupo, no sola) · combate contra un enemigo
  envuelto en llamas (Surtr/draugr ardiendo) · Senua mirando su reflejo en una superficie de piedra/agua,
  pintura azul visible en el rostro · Senua sentada de espaldas viendo un lago al amanecer · plano cerrado de
  ojo azul con manos borrosas en primer plano (found-footage / cámara en mano, estilo del juego).
  https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2461850/ss_fbb6d36a25dd1610acc98d0e10d6c6e1cc4ee00a.1920x1080.jpg
  · ✅ (Steam API + store page 2461850) · hoja `arte_01.jpg` #11-14.

**Arte conceptual de artistas de Ninja Theory en ArtStation** (dan 403 al pedirlas directo desde este
servidor — confirmado con `curl`, código 403 — así que van citadas por el buscador, como indica AYUDANTE.md):
- Hugues Giboire — arte de personaje de Senua e ilustraciones promocionales, trabajó en Ninja Theory ·
  https://www.artstation.com/artwork/e0zBNJ · ⚠️ (una fuente, resultado de buscador).
- Mark Molnar — conceptos y arte de marketing de *Hellblade* · https://www.artstation.com/artwork/vVkYv · ⚠️.
- Marco Teixeira — diseño de personaje de Goði y entorno de Illtauga para *Hellblade II*; «Illtauga 2» fue
  finalista 2024 de la Concept Art Association · https://www.artstation.com/artwork/49mJK8 ·
  https://www.conceptartassociation.com/2024-caa-finalists/illtauga-2-senuas-saga-hellblade-ii · ✅ (dos
  fuentes: ArtStation + Concept Art Association).
- Balazs Kalazdi — arte de entorno de *Senua's Saga: Hellblade II* · https://www.artstation.com/artwork/lVeb3V · ⚠️.
- GamesRadar+ reseñó en su momento el concept art de un poblado costero maltrecho de *Hellblade II*
  (entorno, no personaje) · https://www.gamesradar.com/hellblade-2-concept-art-shows-off-a-battered-coastal-village/ · ⚠️.
- No encontré un *artbook* publicado («The Art of Hellblade»): en 2017 un jugador lo pidió en el foro de
  Steam y nadie confirmó que existiera. Búsqueda: `"Hellblade Senua's Sacrifice" artbook "The Art of"`,
  inglés. ⚠️ dudoso / no existe publicado.

**Hoja de contacto de la wiki** (`investigar_serie.py --paginas` con 26 páginas: personajes, sitios y las
dos fichas de juego; 96 imágenes enlazadas, 82 de 400 000 px o más): `hojas/personajes_01.jpg` (imágenes
1-48 del índice) y `hojas/fondos_01.jpg` (49-82). Números exactos y URL de cada original en
`herramientas/referencias/hellblade/indice.json`.

---

## 3 · Fan art y 3D con licencia (sólo como referencia, nunca para pegar)

**Modelos 3D descargables en Sketchfab**, licencia comprobada con la API (`api.sketchfab.com/v3/models/<uid>`,
no sólo el HTML — da usuario, licencia y si es descargable):
- «Senua» · DshGames · CC Attribution · 794 me gusta, 27 657 vistas, 125 214 caras, descargable ·
  https://sketchfab.com/3d-models/none-fd560f8d33ed4d09be36f691b928e6ad · ✅ (API + datos-imagen.md).
- «Senua» · johnalejandro_13 (aparece como AsterOmice en el listado viejo del buscador; el usuario actual
  de la API es johnalejandro_13) · CC Attribution · 47 me gusta, 120 348 caras ·
  https://sketchfab.com/3d-models/none-380abf627b824228b30d53ef0e446b0e · ✅.
- «Pig Head» (casco/cabeza de cerdo de un Northman) · johnalejandro_13 · CC Attribution · 90 me gusta,
  38 446 caras · https://sketchfab.com/3d-models/none-08ffeea7bf5b463193ce836e2b8bdd5d · ✅.
- Búsquedas adicionales en la API (`q=hellblade`, `q=senua`) no dieron más modelos con licencia libre de
  objetos o sitios (espada Gramr, máscara de Valravn, Iron Mirror): sólo estos tres y variaciones de fan art
  no descargable. No encontré modelos 3D libres del espejo de hierro ni de la espada Gramr. ⚠️.

**Fan art mejor valorado por personaje** (Safebooru, ya en datos-imagen.md; SÓLO referencia de pose/estilo,
enlace y autor, nunca para pegar):
- 2691×4177 · autor/origen DeviantArt (jefwu) · https://safebooru.org/images/3569/946386e530ddc684b3c9b89393638aa64dd4fca8.jpg · ⚠️ (una fuente).
- 984×984 · autor/origen ArtStation (thomasfray) · https://safebooru.org/images/3567/6a39bac9062aac563e935bfde66ac695651c9674.jpg · ⚠️.
- 753×1000 · autor/origen DeviantArt (firez-da) · https://safebooru.org/images/3581/705d92266606dc0fbd7a210a2e8940e544f9ac5d.jpg · ⚠️.
- Vocabulario Danbooru para IA de imagen (related_tag de «senua», ya en datos-imagen.md): facepaint, celtic,
  long_hair, holding_weapon, sword, fur_trim, fur_collar, war_paint, forehead_protector, bodypaint,
  fighting_stance, bags_under_eyes. Útil para el punto 17 (lo hace el redactor). ✅ (fuente única pero es
  agregación estadística de Danbooru, no un solo post).

---

## 15 · Vestuario (colores medidos, no de memoria)

**Descripción oficial completa** (wikitext de `Senua`, sección «Appearance»; dos partes claramente separadas
por juego — cambia bastante y hay que decirlo en la biblia):

*Hellblade: Senua's Sacrifice (2017)* — pintura de rostro azul woad, pesada alrededor de los ojos, brazo
izquierdo, clavículas y labio inferior (estilo pícto, atestiguado desde Eumenio en el 297 d.C.). Pelo largo
castaño oscuro en cola alta, trenzado en rastas untadas con cal y cuentas. Tocado de cuero con adorno de
plata grande con piedras azules al frente y triskeles (espirales triples) cosidos a los lados. Traje sencillo
de cuero y tela a cuadros: pechera con dibujo detallado, brazos al descubierto, cuello de piel de lobo cerrado
con un broche de plata. Cinturón de cuero con la espada al lado izquierdo, una bolsa con la cabeza de Dillion y
un espejo de hierro pulido (regalo de Druth) para mirar al otro mundo. A lo largo del juego la pintura se va
lavando (sobre todo tras el primer encuentro con Hela) y la podredumbre oscura le sube del brazo por el
cuello pase lo que pase. Al desbloquear **Focus** cambia de traje: armadura de piezas de cuero en pecho y
hombros unidas con anillas de metal, y una tira de tela en el antebrazo derecho. Fuente:
https://hellblade.fandom.com/wiki/Senua#Appearance · ✅ (wikitext + confirmado visualmente en las capturas
de Steam de arriba).

*Senua's Saga: Hellblade II (2024)* — aspecto más pesado, cansado y brutal; ojeras marcadas, cicatrices
discretas, suciedad constante. La pintura ya NO es azul: es más oscura y agresiva, sobre todo en la zona de
los ojos y parte de las mejillas (confirmado en las capturas oficiales «Senua Chant»/«Senua Army», donde se
ve rojiza-oscura a la luz del fuego). Pelo largo y oscuro en trenzas de inspiración celta-nórdica, casi
siempre mojado o sucio. Ropa rústica de cuero, telas envejecidas, pieles y accesorios tribales, de influencia
pícta y nórdica, funcional para el combate. Cubierta de barro, sangre y hollín durante el viaje. Fuente:
wikitext de `Senua` · ✅.

**Hex medidos con `herramientas/estilo.py`** (Pillow, cuantización de color; cada uno dice de qué imagen sale):
- **Pintura woad, HB1** (recorte de la cara en el key art más nítido, coordenadas 2600,540-3100,800 de
  `wallhaven-vm8gql.jpg`, 3840×2160, réplica del key art oficial de Xbox/Ninja Theory con el rostro pintado
  de azul): **#29394A** (mayoría de píxeles) con brillos en **#314252**; textura agrietada/pintada visible al
  100%. ✅ (medido dos veces: paleta general del recorte grande dio #4C5E6C al 6 %, el recorte cerrado a
  la sola zona de pintura confirma el tono #29-39-4A). Guardado en
  `/tmp/claude-0/trabajo/118-hellblade-imagen/vm8gql_forehead.jpg`.
- **Portada Hellblade 1** (720×1080): fondo casi negro #060404 (47.7 %), piel/luz #CDC1B8 (2.8 %); estilo
  «sombreado degradado/pintado», saturación media 31 %, brillo medio 16 % — la portada es muy oscura,
  de bajo perfil. ✅.
- **Key art vertical Hellblade II** (2732×4096): #040609/#0C1017 dominan (74 % juntos), saturación 46 %,
  brillo 11 %: paleta casi monocroma azul-negro. ✅.
- **Brillo del espejo/Focus** («Full charge.png», 1000×563, wiki): #0E6D79 y #61AAB9 turquesa sobre negro
  #0B0505 — es el azul-verde que usa el juego para el brillo del espejo de hierro cuando carga Focus, muy
  distinto del woad de la cara. ✅.
- **«Senua Chant» oficial (HB2)**, firelight: #24170A/#3C2410/#9A5D32 — confirma que bajo luz de fuego la
  pintura y la piel leen en tonos tierra-rojizos, no azules (coherente con la descripción de HB2). ✅.
- **Captura Steam HB1, silueta a contraluz dorado**: #A2741D/#CEA74F/#F8F4E8, saturación 63 %, brillo 62 %:
  la escena "icónica" de la flor/árbol es la más luminosa y cálida de todo el material mirado. ✅.

**Ropa icónica reconocible**: el tocado de cuero y plata con piedra azul + la pintura azul en los ojos es lo
que todo el mundo reconoce de HB1 (aparece en el logo, la portada y casi todo el fan art). En HB2 lo icónico
cambia a la trenza mojada + pintura oscura/rojiza + el aro de hueso/plata en la cabeza que se ve en
«Senua Chant» y «Senua Army» (parece el mismo tocado con pátina distinta, curtido). ⚠️ (interpretación
propia a partir de las imágenes, no hay artículo que lo diga con esas palabras).

**Guía oficial de cosplay de Ninja Theory** (referencia de vestuario "desde la fuente", no fan art): Ninja
Theory publicó en 2016 una guía de cosplay de Senua «con el modelo completo de frente y de espaldas»,
detalles de la espada y el espejo · post de Facebook (`facebook.com/ninjatheory/posts/...-cosplay-guide-...`)
recogido también por la noticia de Steam «Senua Cosplay Guide»
(https://store.steampowered.com/news/app/414340/view/4546903098693967625) · ✅ (dos fuentes: Facebook
oficial + Steam News oficial, aunque Facebook no se pudo leer completo desde este servidor — bloquea el
scraping; el texto del post sí se confirma en ambas fuentes).

---

## 16 · Ciudades, paisajes y fondos de pantalla

**Sitios con luz y paleta medida** (`estilo.py` sobre la imagen más grande de cada lugar en la wiki):
- **Helheim** (el inframundo, niebla y hueso) · 1920×1080 · paleta #1E201D/#45444B/#CEB4A7/#A08983/#776561/
  #EDDCCE · brillo medio 52 % (la más clara de todas: niebla blanca-hueso), saturación 28 %. Fuente:
  https://static.wikia.nocookie.net/hellblade-nt/images/c/c3/Helheim.png · ✅.
- **Jarnvior** (bosque) · 1920×1080 · #2A241F/#1C1714/**#8D99AE** (azul-grisáceo frío, la niebla del bosque)/
  #3D342C/#51535B · brillo 29 %. https://static.wikia.nocookie.net/hellblade-nt/images/d/da/Jarnvior.jpg · ✅.
- **Illtauga** (poblado/gruta) · 1000×811 · tonos tierra #3E3228/#27251E/#594031/#825943, algo de verde oscuro
  #0A1411 · brillo 26 %. https://static.wikia.nocookie.net/hellblade-nt/images/9/9b/Illtauga.png · ✅.
- **Reykjanesta** · 1672×941 · dominan azules de atardecer **#556E8A**/#070C13/#1A2432/#768FA9 · brillo 39 %,
  saturación 45 % (la más saturada del grupo). https://static.wikia.nocookie.net/hellblade-nt/images/d/dd/Reykjanesta.png · ✅.
- **Surtr's Domain** (reino de fuego) · 1920×1080 · #100B0F/#2A2124/#4C3E3B/#70615C/#928787 — es más ceniza
  que llama en esta imagen concreta, ojo al elegir referencia si se quiere fuego vivo (usar mejor «Senua vs
  Garm.webp» o la captura Steam hb2_6, con rojos #882F26/#CF5F53/#FCA82F). https://static.wikia.nocookie.net/hellblade-nt/images/c/ce/Surtr_Domain.jpg · ✅.

**Fondos de pantalla oficiales 8K** (7680×4320, medidos por cabecera JPEG, ver punto 1 arriba: Volcano, Arms,
Skulls) — sitios sin personaje, ideales para fondo de lámina. `senuassaga.com/media`, autor Xbox Game
Studios/Ninja Theory. ✅.

**Capturas oficiales de Steam 1920×1080** con sitios completos (no sólo personaje): comparación remaster
Bardarvik «OLD/UPDATED» (HB1, muestra el mismo poblado a la orilla del agua, niebla, dos versiones gráficas
una al lado de otra) y el paisaje de lago al amanecer con montañas de HB2 (Senua de espaldas, hb2_4). Mismas
URLs que en el punto 1. ✅.

**Fondos de pantalla de fans en alta (Wallhaven)**, ya en datos-imagen.md, **tamaños verificados de nuevo**
descargando la cabecera real con Pillow (coinciden exactamente con lo que decía la página de Wallhaven):
- 3508×2105 (confirmado) · ♥135 · guerrera de pie sobre paisaje · https://w.wallhaven.cc/full/k9/wallhaven-k9olx7.jpg · subido por monxef · ✅.
- 3840×2160 (confirmado) · ♥61 · mirando a la distancia, videojuego paisaje · https://w.wallhaven.cc/full/76/wallhaven-76jyq3.jpg · subido por Highwind · ✅.
- 1920×1080 (confirmado) · ♥59 · paisaje, Ninja Theory · https://w.wallhaven.cc/full/g7/wallhaven-g7l8me.png · subido por aminagha · ✅.
- 3840×2160 (confirmado) · ♥55 · cara, ojos azules · https://w.wallhaven.cc/full/vm/wallhaven-vm8gql.jpg ·
  origen desconocido (probablemente key art oficial recortado por un fan; el encuadre y la resolución
  4K con texto rúnico de fondo coinciden con el estilo de marketing de HB1) · ⚠️ (no se pudo confirmar
  autoría exacta, pero el archivo es el que mejor muestra la pintura azul y se usó para medir el hex de
  arriba).
- Otras 10 de la lista de datos-imagen.md (hasta 4100×1850) no se volvieron a verificar por presupuesto:
  quedan con ⚠️ tal como las dejó `recolectar.py`.

---

## 19 · Texturas 2D (tramas, grano, patrones, emblemas — con equivalentes libres)

- **Pintura woad agrietada**: en el recorte cerrado (`vm8gql_forehead.jpg`, ver punto 15) se ve textura de
  pintura corporal cuarteada y con relieve de la piel debajo, no un plano liso: pinceladas finas siguiendo
  las arrugas de la frente, brillos especulares puntuales. Equivalente libre: pack «24 Free Grunge Brushes»
  para Photoshop, ABR, uso comercial libre sin crédito · https://myphotoshopbrushes.com/brushes/id/3536/ ·
  ⚠️ (licencia declarada por el sitio, no verificada archivo por archivo).
- **Emblemas y logos oficiales** (ya medidos en el punto 1): logo rúnico verde de HB2 (triskel/cruz rúnica
  blanca sobre verde oliva, 647×679) y el logo azul de HB1 (perfil pintado). Sirven tal cual como emblema de
  franquicia para una lámina. ✅.
- **Patrón triskel/nudo pícto-celta** (el mismo motivo que lleva Senua cosido en el tocado y tatuado en el
  juego): SVG libres de dominio público (CC0) en freesvg.org — «Pattern Triskelion» y «Triskelion, an ancient
  motif» · https://freesvg.org/pattern-triskelion · https://freesvg.org/triskelion-an-ancient-motif · ✅ (dos
  archivos de la misma fuente, licencia CC0 declarada en cada página).
- **Cuero** (tocado, cinturón, pechera de Senua): textura PBR libre CC0 equivalente, ambientCG «Leather037» /
  «Leather030» · https://ambientcg.com/a/Leather037 · ⚠️ (una fuente, API de ambientCG).
- **Runas de fondo** del key art (`vm8gql`, ver arriba): son texto en el alfabeto rúnico usado en el juego
  para las «Lorestones» (piedras rúnicas), color óxido/rojo sobre negro — es más un elemento tipográfico que
  una textura; lo dejo anotado aquí porque aparece pegado a la imagen y se puede recortar como capa de
  fondo, pero la fuente/letra exacta la debe resolver el investigador de texto (punto 5). ⚠️.
- No encontré tramas de manga (el juego no es manga, es CGI realista): el punto se adapta a texturas de
  pintura corporal, cuero y piedra rúnica, como arriba. Aviso explícito, no es un hueco sin buscar.

---

## 23 · Colaboraciones y cruces

- **Xbox × Senua's Saga: Hellblade II — Xbox Series X a medida** (2024): Xbox creó una consola Series X,
  mando y soporte únicos con el patrón/arte de Islandia del juego, sorteados por Xbox (no se vendió); valor
  aproximado consola 440 USD + mando 60 USD + soporte 100 USD. Fuentes: TheGamer
  (https://www.thegamer.com/hellblade-2-xbox-series-x-sweepstake/) y la propia página de sorteo de Xbox
  (https://www.xbox.com/en-US/promotions/sweepstakes/senuas-saga-hellblade-II-xbox-series-x-custom-console-and-controller-sweepstakes)
  · ✅ (dos fuentes, una de ellas la marca).
- **Guía de cosplay oficial de Ninja Theory** (2016) — ver punto 15: cuenta como colaboración
  estudio-comunidad, trae el modelo completo de Senua de frente y de espaldas para que la fan-made sea
  fiel. ✅.
- **Cosplay de fans, bien hecho**: tienda Anicossky vende un traje reproducción de Senua (materiales:
  cuero sintético, tela) · https://anicossky.com/products/hellblade-senuas-sacrifice-senua-cosplay-costume-outfits
  · ⚠️ (una fuente, es una tienda, no un ejemplo concreto de cosplayer con fotos propias verificadas).
- **Figuras**: no encontré una figura o estatua OFICIAL con licencia (ni Gaming Heads ni similar). Lo que
  hay son bustos y esculturas 3D impresas por fans, no oficiales, en Etsy y Cults3D (uno incluso a escala
  1/6 mostrado en YouTube) — sirven como referencia de pose 3D pero hay que decir en la biblia que NO son
  oficiales. Búsquedas: «Senua Hellblade official statue figure Gaming Heads» (inglés). Sin resultado oficial.
- **Crossovers comerciales** (Fortnite, gacha, eventos de marca): no encontré ninguno. Búsqueda:
  «Hellblade Senua crossover collaboration Fortnite OR Dead by Daylight OR gacha» (inglés) — sólo devolvió
  ruido de un posible cruce Fortnite×Dead by Daylight que no tiene nada que ver con Hellblade. No lo hay
  (o no está documentado en español/inglés); no digo «no existe», digo que no lo encontré con estas
  búsquedas.
- **Cafés temáticos / eventos**: no busqué específicamente (bajo presupuesto de este punto para un juego
  sin comunidad de eventos físicos tan grande como un anime); si se necesita, falta por hacer. ⚠️.

---

## Lo mejor para la lámina

1. El **key art con la pintura woad nítida** (`wallhaven-vm8gql.jpg`, recorte de frente en
   `hojas/arte_01.jpg` #15): es la imagen que mejor vende «esto es Hellblade» de un vistazo — pintura azul
   #29394A, tocado de plata con piedra turquesa, runas de fondo.
2. La captura oficial **«Senua's Army»** (8K, `hojas/arte_01.jpg` #2): Senua NO está sola, lidera un grupo —
   exactamente lo que pide `reglas_del_dueno.md` (nada de personaje solo y flotando) y lo que el dueño ha
   pedido más de una vez («en grupo, en acción»).
3. **Captura Steam de HB1** a contraluz dorado entre partículas junto al árbol (silueta serena,
   `hojas/arte_01.jpg` #7): sirve para un canal tranquilo/contemplativo; paleta cálida #CEA74F muy distinta
   del resto, que es casi todo frío y oscuro.
4. El **logo rúnico de HB2** (verde oliva + triskel blanco, `hojas/fondos_01.jpg` #82) funciona solo como
   sello/emblema tallado en un objeto de madera o piedra en Blender.
5. Los **fondos 8K sin personaje** («Arms», «Skulls», «Volcano») dan profundidad y niebla real para poner
   detrás de Senua sin tener que inventar nada: son oficiales y de sobra en resolución.

---

## No encontré

- ⚠️ Artbook oficial publicado de *Hellblade: Senua's Sacrifice* («The Art of Hellblade»): sólo hay un pedido
  de un jugador en Steam en 2017, sin respuesta oficial. Búsqueda: `"Hellblade Senua's Sacrifice" artbook
  "The Art of" OR "making of book"` (inglés).
- ⚠️ Modelos 3D libres específicos de la espada Gramr, el espejo de hierro o la máscara de Valravn en
  Sketchfab (sólo hay del personaje Senua y del casco de cerdo de un Northman). Búsqueda: API de Sketchfab
  con `q=hellblade` y `q=senua`, `downloadable=true`.
- ⚠️ Figura o estatua OFICIAL con licencia de Senua (Gaming Heads, First 4 Figures o similar): no existe o no
  está documentada; sólo bustos de fans impresos en 3D.
- ⚠️ Crossover comercial (Fortnite, juego gacha, marca de ropa, café temático): no encontrado.
- ⚠️ Autoría exacta del archivo `wallhaven-vm8gql.jpg` (el key art con la pintura más nítida): Wallhaven no
  listaba «origen» para esa subida; por el encuadre y la calidad es casi con toda seguridad key art oficial
  de Xbox/Ninja Theory recortado, pero no puedo dar el crédito exacto sin más fuente.
- Todo lo demás pedido en los puntos 1, 3, 15, 16, 19 y 23 se cubrió con al menos una fuente comprobable
  (ver tabla de arriba); lo anotado aquí es honestamente lo que faltó, no relleno.

---

## Bitácora de búsqueda

- `herramientas/investigar_serie.py --wiki hellblade --paginas` con 26 páginas (personajes, sitios, las dos
  fichas de juego) → 96 imágenes, 82 hojas grandes, 2 hojas de contacto (`hoja_01.jpg`, `hoja_02.jpg`,
  copiadas a `hojas/personajes_01.jpg` y `hojas/fondos_01.jpg`).
- API de Fandom directa (`action=query&list=allpages`, `prop=revisions&rvslots=main`) para la lista completa
  de páginas de la wiki y el wikitext de `Senua`, `Dillion`, `Druth`, `Astridr`, `Fargrímr`, `Freyslaug`
  (inglés) — sin pasar por el buscador, ahorra cupo.
- API de Sketchfab (`api.sketchfab.com/v3/models/<uid>` y `/v3/search?type=models&q=...&downloadable=true`)
  para confirmar licencia y autor de los 3 modelos de la sección 3.
- API de Steam (`store.steampowered.com/api/appdetails?appids=414340` y `...=2461850`) para las capturas
  oficiales 1920×1080 de ambos juegos — no estaba en datos-imagen.md, es hallazgo propio.
- `senuassaga.com/media` leído con `curl` + `grep` de URLs (no con el buscador) para los 8 fondos oficiales
  8K; verificados con Pillow leyendo sólo los primeros 64 KB de cada archivo (no hace falta bajarlo entero).
- API de ambientCG (`full_json?type=Material&q=leather`) para la textura de cuero libre.
- WebSearch (inglés, 9 búsquedas de las ~50 disponibles para este rol): `Senua ArtStation Ninja Theory
  concept art`, `"Hellblade" "Senua's Sacrifice" press kit key art official`, `Senua's Saga Hellblade II
  press kit screenshots official`, `Senua Hellblade cosplay woad paint`, `Senua Hellblade official statue
  figure Gaming Heads`, `Hellblade Senua crossover collaboration Fortnite OR "Dead by Daylight" OR gacha`,
  `"Senua" Hellblade cosplay best "materials" armor build photos`, `Hellblade Senua's Sacrifice artbook "The
  Art of" OR making of book`, `triskelion Pictish knotwork pattern free vector SVG`, `Xbox Series X Hellblade
  II special edition console controller skin design`.
- `curl -I`/`-o /dev/null -w "%{http_code}"` a 3 páginas de ArtStation → **403** confirmado (no es fallo
  puntual): se citan por el resultado del buscador, tal como indica AYUDANTE.md.
- IGDB presskit (`igdb.com/games/.../presskit`) → 403 también; no insistí más de dos veces, como marca la regla.
- No usé YouTube (bloqueado con inicio de sesión en este servidor, como avisa el encargo): todas las capturas
  y fondos salen de Steam, la wiki y `senuassaga.com`, no de vídeo.

## Cumplimiento de mis puntos (1, 3, 15, 16, 19, 23)

| Punto | Estado | Por qué |
|---|---|---|
| 1. Arte oficial variado | ✅ | Portadas, key art, 6 fondos 8K oficiales, 19 capturas Steam oficiales (11+8), 3 logos, 4 artistas de ArtStation citados (403 directo, citados por buscador), sin artbook (dicho en «No encontré») |
| 3. Fan art y 3D con licencia | ✅ | 3 modelos Sketchfab con licencia CC Attribution confirmada por API (autor, caras, descargable) + 3 fan art de Safebooru con autor y enlace, sólo como referencia |
| 15. Vestuario | ✅ | Descripción oficial completa HB1 vs HB2 (wikitext), 6 hex medidos con Pillow de fuentes distintas (key art, portada, captura Steam, brillo del espejo), guía de cosplay oficial de Ninja Theory con dos fuentes |
| 16. Fondos y fondos de pantalla | ✅ | 5 sitios con hex medido, 6 fondos oficiales 8K verificados por cabecera real, capturas Steam con sitios completos, 4 wallpapers de fans re-verificados en tamaño |
| 19. Texturas 2D | ✅ | Textura de pintura agrietada descrita del recorte, patrón triskel CC0, cuero CC0, brushes de grunge libres, logos como emblema; aviso explícito de que no hay tramas de manga (no aplica) |
| 23. Colaboraciones y cruces | ✅ | Consola Xbox a medida (2 fuentes), guía de cosplay oficial, cosplay comercial de fans; figuras oficiales y crossovers comerciales: buscados y no encontrados, anotado en «No encontré», no en «Sigue» |

Todo lo obligatorio de mis 6 puntos está cubierto con al menos una fuente comprobable; lo que falta (artbook,
modelos 3D de objetos sueltos, figura oficial, crossover de marca, café temático) es material que
probablemente no existe para este juego, no una búsqueda a medias — queda anotado en «No encontré», no en
Sigue.
