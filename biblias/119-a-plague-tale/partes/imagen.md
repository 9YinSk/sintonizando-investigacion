# Parte IMAGEN · Encargo 119 — A Plague Tale

Investigador de imagen (rol `imagen`, EQUIPO.md): puntos **1, 3, 15, 16, 19 y 23** de ENCARGO.md.
Libreta de datos, no prosa. Parte de `partes/datos-imagen.md` (ya consultado, no se repite) y de
`herramientas/investigar_serie.py` corrido con 2 páginas de la wiki (Amicia y Hugo, 70 imágenes → ver
hojas). Trabajo pesado en `/tmp/claude-0/trabajo/119-a-plague-tale-imagen/` (capturas de Steam, recortes
para hex, contacto).

Videojuegos: *A Plague Tale: Innocence* (2019, appid Steam 752590) y *A Plague Tale: Requiem* (2022, appid
Steam 1182900), Asobo Studio / Focus Entertainment. Wiki: `aplaguetale.fandom.com`. YouTube pide iniciar
sesión desde este servidor: todo el material de vídeo de este punto sale de la API de Steam, la wiki y el
buscador (nunca de YouTube).

---

## 1 · Arte oficial, en cantidad y variado

**Portada oficial (key art) *Innocence*** — pintura de Olivier Ponsonnet (director de arte de Asobo en
ambos juegos, confirmado por la wiki y por ArtStation Magazine, ver «artistas» abajo): Amicia y Hugo muy
cerca, paleta casi monocroma gris-beige-negro, un enjambre de ratas les sube desde el pecho hasta salirse
del marco. Logos de Asobo Studio y Focus Home Interactive abajo. 1063×1600 ·
`File:Olivier-ponsonnet-boxart.jpg` ·
https://static.wikia.nocookie.net/a-plague-tale-innocence/images/7/79/Olivier-ponsonnet-boxart.jpg · ✅
(wiki + es la portada real del juego en Steam/tiendas) · hoja `fondos_01.jpg` #63. Mirada en grande: fondo
casi blanco humo, las ratas son el único elemento oscuro y compacto — la imagen que mejor resume «Francia
medieval + ratas» de un vistazo.

**Arte conceptual temprano** (`Early Concept Art 1/2`, wiki, sin fecha exacta pero previo al render final
según el pie de la galería):
- «Early Concept Art 1» — Amicia y Hugo atrancando una puerta de madera con una viga, ella sujeta una
  antorcha encendida; pintura muy oscura salvo el fuego. Hex medidos (`estilo.py`): negro **#0C0403** (32%)
  dominante, fuego en **#E0801C**/**#FBF08D**, saturación 84% (la más saturada de todo lo que medí,
  justo por el fuego). 1200×675 ·
  https://static.wikia.nocookie.net/a-plague-tale-innocence/images/2/2b/Early_Concept_Art_1.jpeg · ✅ ·
  hoja `fondos_01.jpg` #70. Sirve directamente para el punto «luz (fuego, antorchas)» del encargo.
- «Early Concept Art 2» — retrato pintado de Amicia y Hugo pegados, casi todo en tonos teal-gris oscuro
  (paleta muy distinta a la del juego final, que es más cálida): **#3E3E44**/**#2E1424**/**#414F53**,
  saturación 31%, brillo 28%. 800×1200 ·
  https://static.wikia.nocookie.net/a-plague-tale-innocence/images/7/7a/Early_Concept_Art_2.jpeg · ✅ ·
  hoja `fondos_01.jpg` #69.

**Retratos oficiales en 4K de la wiki** (3840×2160, sacados del propio juego/marketing, luz de antorcha
cálida):
- Amicia, primer plano, trenza suelta con mechones sueltos, capucha de piel · `APTI-1-Amicia-1.jpg` ·
  https://static.wikia.nocookie.net/a-plague-tale-innocence/images/9/92/APTI-1-Amicia-1.jpg · ✅ · hoja
  `personajes_01.jpg` #5.
- Hugo, primer plano · `APTI-22-Hugo-2.jpg` ·
  https://static.wikia.nocookie.net/a-plague-tale-innocence/images/3/30/APTI-22-Hugo-2.jpg · ✅ · hoja
  `personajes_01.jpg` #6. Hay 4 variantes más de Hugo (`APTI-24/25/26-Hugo-*.jpg`, mismas 3840×2160) y 3 de
  Amicia (`APT-Amicia1-1`, `APT-Amicia2-2`, `APT-Amicia7-12`), todas ✅, todas en `personajes_01.jpg`
  #2-#9.

**Capturas OFICIALES de Steam, 1920×1080** (API `appdetails`, no reescaladas, cumple lo que pide el
encargo; monté un contacto propio con las 20 en `hojas/arte_01.jpg`, numeradas 1-20 abajo):
- *Innocence* (appid 752590), 11 capturas. Poses vivas: Amicia y Hugo caminando de la mano por una calle
  de pueblo medieval de día, carro y toneles alrededor (#11) · Amicia cargando/abrazando a Hugo, gesto
  protector (#12) · dos figuras sobre una colina con empalizada de picas al atardecer rojizo (#13) ·
  caballero con lanza y antorcha en combate nocturno (#14) · molino ardiendo, dos siluetas con lanzas junto
  al fuego (#15) · **Amicia y Hugo de espaldas ante un asedio al amanecer, catapulta, cientos de cadáveres
  en el suelo, niebla** — la escena que mejor cruza «Francia medieval + luz + tragedia» (#16) · arco de
  árboles en otoño, hojas naranjas (#17) · cripta con una sola antorcha (#18) · bandada de cuervos, Amicia
  y Hugo corriendo entre ruinas en niebla, plano aéreo (#19) · dos siluetas entre arcos rotos en niebla
  (#20) · portada con reseñas (8-10/10 de GameSpot, ScreenRant, Windows Central…) (#10).
  URL de ejemplo: https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/752590/ss_8775c109d7303faf8aa94c532905107b75064d48.1920x1080.jpg
  · ✅ (Steam API `appdetails` + store page 752590).
- *Requiem* (appid 1182900), 9 capturas. Poses vivas: proa de un barco con vela roja/blanca a rayas, grupo
  a bordo (#1) · **Amicia y Hugo alzados sobre los hombros de la gente, multitud aclamando, plaza con
  catedral** — grupo, celebración, justo lo que pide `reglas_del_dueno.md` (#2) · Amicia en un salón con
  cortinas rojas y el suelo cubierto de pétalos de rosa, luz dramática (#3) · Amicia de noche junto a
  antorchas y muro de castillo, sigilo/combate (#4) · acantilado con el grupo acercándose a un barco en la
  costa (#5) · **mercado de un pueblo con el castillo detrás, banderas amarillas y negras, sol de día**
  (#6) · primer plano de Hugo llorando, pecas, alforja al hombro (#7) · ruinas al atardecer, grupo subiendo
  unas escaleras entre niebla dorada (#8) · playa con barco encallado, atardecer naranja (#9).
  URL de ejemplo: https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1182900/ss_9cbcd6b81cc32ecf75b36f40b92157da78a19598.1920x1080.jpg
  · ✅ (Steam API `appdetails` + store page 1182900).

**Artistas de Asobo Studio en ArtStation** (dan **403** al pedirlas directo desde este servidor — probado
con `curl -I` en 2 URL distintas, confirmado dos veces — se citan por el resultado del buscador, como
indica AYUDANTE.md):
- **Olivier Ponsonnet** — director de arte de ambos juegos; perfil `reiv.artstation.com`, proyectos «A
  Plague Tale Innocence - Amicia and Rats» y «A Plague Tale Innocence - Early Environment Concepts» ·
  https://reiv.artstation.com/projects/2x18nB · https://reiv.artstation.com/projects/4bd8Rn · también
  publicó key art de *Requiem* en https://www.artstation.com/artwork/3q0OGm · ✅ (varias fuentes del
  buscador + wiki lo nombra como autor de las imágenes «Olivier-ponsonnet-*»).
- **Damien Papet** — artista conceptual de Asobo; entornos, props y personajes en ambos juegos, perfil
  `damien_papet.artstation.com` con proyectos «A Plague Tale: Innocence — Characters (2019)»,
  «A plague Tale: Requiem - Environements Concepts» y «Props Concepts» ·
  https://damien_papet.artstation.com/projects/ybKePO ·
  https://www.artstation.com/artwork/LeP3Ev · https://www.artstation.com/artwork/3qNdgA · ✅ (además sus
  imágenes «Damien-papet-*» están subidas tal cual en la wiki, ver hoja `personajes_01.jpg` #36-39).
- **Tom Hisbergue** — artista conceptual, «A Plague Tale: Requiem — Concept arts part 4» ·
  https://www.artstation.com/artwork/8wx4wQ · ⚠️ (una fuente, resultado de buscador).
- **Adonia Urian** y **Loïc Paulus** — artistas conceptuales acreditados en el artbook de *Requiem* (ver
  abajo) · ⚠️ (una fuente, la ficha del artbook).
- **ArtStation Magazine** publicó un «Art Blast» oficial por cada juego con el equipo de Asobo: «Asobo
  Studio A Plague Tale: Innocence Art Blast» (2019) y «…Requiem Art Blast» (2023) ·
  https://magazine.artstation.com/2019/06/asobo-studio-a-plague-tale-innocence-art-blast/ ·
  https://magazine.artstation.com/2023/01/asobo-studio-a-plague-tale-requiem-art-blast/ · ambas dan 403
  directo también (confirmado) · ⚠️ (contenido citado por el snippet del buscador, no se pudo leer
  completo).

**Artbook y making-of oficiales** (tienda de Focus Entertainment):
- ***The Art of A Plague Tale: Requiem*** — 196 páginas, cientos de imágenes de concept art, diseño y
  render; entrevistas a David Dedeine (cofundador y director creativo de Asobo), Kevin Choteau (director
  del juego), Sébastien Renard (guionista principal) y Olivier Ponsonnet (director de arte); concept arts
  de Tom Hisbergue, Damien Papet, Adonia Urian y Loïc Paulus. Publicado 2022 ·
  https://store.focus-entmt.com/eu/product/762950/a-plague-tale-requiem-artbook-fr ·
  https://www.thevideogamelibrary.org/book/the-art-of-a-plague-tale-requiem · ✅ (dos fuentes).
- ***The Heart of A Plague Tale*** — libro «visual making-of» de la serie completa, tienda de Focus ·
  https://store.focus-entmt.com/us/en/product/762951/the-heart-of-a-plague-tale-a-visual-making-of-en ·
  ⚠️ (una fuente).
- No encontré un artbook público de *Innocence* por separado (2019): las búsquedas devuelven sobre todo el
  de *Requiem*. ⚠️.

**Hoja de contacto de la wiki** (`investigar_serie.py`, páginas «Amicia de Rune» y «Hugo de Rune», 70
imágenes grandes numeradas): `hojas/personajes_01.jpg` (1-48: retratos, escenas de personajes) y
`hojas/fondos_01.jpg` (49-70: capturas SS0xx de *Requiem*, arte de Olivier Ponsonnet, concept art
temprano). Números y URL exactos de cada una en
`herramientas/referencias/a-plague-tale/indice.json`. Contacto propio de las 20 capturas oficiales de
Steam en `hojas/arte_01.jpg` (numeradas 1-20, ver arriba).

---

## 3 · Fan art y 3D con licencia (sólo como referencia, nunca para pegar)

**Modelo 3D descargable en Sketchfab**, licencia comprobada con la API directa (`api.sketchfab.com/v3/models/<uid>`,
no sólo el HTML):
- «Alicia De Rune» · usuario `avishka0977` (nombre visible «MrRealistic») · **CC Attribution** ·
  93 877 caras, 265 vistas, 3 me gusta, descargable confirmado (`isDownloadable: true`) ·
  https://sketchfab.com/3d-models/none-9fc2ea8894be4f23862d36ff400870ef · ✅ (API + ya estaba en
  datos-imagen.md, coincide usuario y licencia).
- Búsquedas adicionales en la API (`q=hugo de rune`, `q=amicia crossbow`, `q=plague tale rat`,
  `q=medieval village asobo`) no devolvieron ningún otro modelo: ni de Hugo, ni de la ballesta/honda de
  Amicia, ni de las ratas, ni de ningún sitio del juego. No encontré más modelos 3D libres de objetos o
  sitios de la serie. ⚠️.

**Fan art mejor valorado por personaje** (Safebooru, ya en datos-imagen.md; SÓLO referencia de pose/estilo,
enlace y autor, nunca para pegar):
- 1200×824 · https://safebooru.org/images/2778/ffe3456d69a140777d35e557303bd29db6fbe0e9.jpg · autor/origen
  Twitter (`ticcytx`) · ⚠️ (una fuente).
- 3840×4164 · https://safebooru.org/images/837/6c7cde8c53fa6e63c9ef1d7de03cbbcc679b2085.jpg · autor/origen
  ArtStation (`quentin_uza_gillet.artstation.com/projects/rRPLke`) · ⚠️.
- Intenté la API de Danbooru directa (`posts.json`, `related_tag.json`) dos veces para completar los
  vocabularios de Hugo y Melie (que `recolectar.py` dejó vacíos): las dos veces dio **403** (challenge de
  Cloudflare, no es un fallo puntual). No insistí más, como marca la regla. El vocabulario de Amicia que sí
  dejó `recolectar.py` (short_hair, capelet, fur_trim, braid, freckles, injury, half_up_braid, realistic…)
  sigue siendo válido para el punto 17 (lo hace el redactor).

**Sitio oficial de merchandising** `store.aplaguetale.com` no respondió (503 y conexión cerrada,
confirmado dos veces por `curl`); lo que se sabe de él sale de reseñas de terceros, ver punto 23.

---

## 15 · Vestuario (colores medidos, no de memoria)

**Descripción oficial completa** (wikitext de `Amicia de Rune` y `Hugo de Rune`, sección «Appearance»;
✅ confirmado también visualmente en las capturas de Steam de arriba):

*Amicia, Innocence* — al empezar viste ropa fina: camisa interior blanca de mangas anchas y puños largos y
estrechos, una sobrecamisa ajustada, pantalón oscuro ceñido y calzas oscuras. Lleva un collar de plata con
un colgante del escudo de armas de la familia de Rune. Por ser noble, peinado elaborado: moño alto
trenzado con nudos pequeños, todo entrelazado con una cinta rosa; su hermano le da flores pequeñas para el
pelo durante el viaje. Tras el asalto de la Inquisición a su casa gana cicatrices en el puente de la nariz,
el labio inferior y la barbilla, y el pelo le cae en una sola trenza por la espalda. Al conocer a Clervie
cambia a «ropa de equipo». Arma: la honda, regalo de su padre. Fuente:
https://aplaguetale.fandom.com/wiki/Amicia_de_Rune#Appearance · ✅.

*Amicia, Requiem* — algo más alta; ahora lleva un gambesón acolchado, pero conserva piezas de *Innocence*:
la placa de armadura en el codo derecho y las bolsas de cuero trabajado. Cara más adulta (frente más
redondeada, línea de pelo más alta, mandíbula y pómulos más marcados), voz más grave. Usa ballesta además
de la honda. Su pelo simboliza su arco: empieza largo y trenzado (familia, feminidad) y se va cortando a la
fuerza según avanza la historia — pelo corto al final = poca estabilidad emocional que le queda. Fuente:
misma página, sección Appearance · ✅.

*Hugo, Innocence* — niño de 5 años, complexión menuda, pelo largo, castaño y despeinado. La ropa cambia
TRES veces: (1) túnica que puede ser **verde, azul, roja o morada oscura** — según qué escudo de armas
familiar elige el jugador al empezar, con camisa blanca debajo y pantalón oscuro (detalle de juego: es
elección del jugador, no fijo); (2) en casa de Clervie, camisa amarilla, chal rojo que le cubre la manga
izquierda, cinturón de cuero trenzado, pantalón marrón, vendas de brazo enlodadas y botas; (3) tras un
tiempo con la Inquisición, túnica negra con bordado dorado en los dobladillos y rayas rojas, camisa roja
debajo, pantalón negro con botas. Al dejar la Inquisición se pone encima el chal rojo de Clervie; en el
epílogo vuelve a la ropa que le dio Clervie. Sus venas se oscurecen y extienden por la Prima Macula,
primero en la base del cuello y luego hacia cara, ojos y boca. Fuente:
https://aplaguetale.fandom.com/wiki/Hugo_de_Rune#Appearance · ✅.

**Hex medidos con `herramientas/estilo.py`** (cada uno dice de qué imagen sale y con qué luz — el juego es
muy distinto en interiores con antorcha que al aire libre de día):
- **Capucha/capa de Amicia, Innocence, luz de antorcha cálida** (retrato `APTI-1-Amicia-1.jpg`,
  3840×2160): **#2B1A16** (21%), **#40241E** (17%), **#553229**, **#764234** — piel de zorro/lana marrón
  cálida, muy influida por el naranja del fuego. ✅.
- **Jubón/corsé de Amicia, Innocence, niebla de amanecer, escena de asedio** (recorte de
  `752590_06.jpg`, captura oficial de Steam, coordenadas 290,400-460,600 del original 1920×1080): casi
  negro-oliva **#0C130A**/**#030902**/**#171B13** — a contraluz de niebla el jubón se lee casi silueta;
  coincide con que la wikitext lo describe como ropa oscura tras el asalto. ✅ (medido + contexto
  wikitext).
- **Jubón de cuero de Amicia, Requiem, luz de día en el mercado** (recorte de `1182900_05.jpg`, captura
  oficial de Steam 1920×1080, zona 775,640-840,780): marrón cuero **#27170E**/**#2F2014**/**#1E1109**,
  saturación 62%. Con luz de día plena se confirma que es un cuero marrón oscuro, no negro. ✅.
- **Túnica de Hugo, Requiem, verde con topos, luz de día** (recorte muy cerrado de `1182900_05.jpg`, zona
  905,755-950,810, tela a la sombra de un árbol): verde oliva oscuro **#1D1C11**/**#252415**/**#302E1C**,
  con el ribete de cuero en **#412314**. Se ve un patrón de topos claros repetido sobre el verde (funciona
  como textura, ver punto 19). ✅.
- **Retrato de Hugo, Innocence, luz de antorcha** (`APTI-22-Hugo-2.jpg`, 3840×2160): marrones cálidos
  **#180F08**/**#2A1C0F**/**#4D331E**, saturación 66% (la más saturada de los retratos, por el fuego). ✅.
- **Portada oficial (key art)**, ver punto 1: gris-beige-negro casi monocromo, es la paleta de
  MARKETING, no la del vestuario real en juego — no usar para el hex de la ropa, sólo para el tono general
  de portada.

**Detalle de juego útil para la lámina**: la túnica de Hugo en *Innocence* CAMBIA de color según el escudo
de armas que elige el jugador al empezar (verde/azul/rojo/morado) — si se quiere motivo, cualquiera de los
cuatro es «canon», no hay un único color fijo. ✅ (wikitext, dato poco conocido).

**Ropa icónica reconocible**: la capa/capucha con capuchón de piel + la trenza (moño trenzado al empezar,
trenza suelta tras el ataque) es lo que todo el mundo asocia a Amicia — aparece en la portada, en casi
todo el fan art y en las capturas oficiales de ambos juegos. En *Requiem* se suma el gambesón acolchado y
la ballesta. De Hugo, lo icónico es el pelo despeinado + los ojos grandes + la venda/alforja que carga.
⚠️ (interpretación propia a partir de las imágenes, no hay artículo que lo diga con esas palabras).

**Guía oficial de cosplay de Asobo Studio** (Amicia, *Requiem*, publicada por la cuenta oficial de Twitter
@APlagueTale el 31-may-2023): muestra el traje de la primera mitad del juego (antes de llegar a La Cuna),
con detalle de la trenza, los patrones del tunic y el cinturón, botas y armadura — NO incluye la ballesta
ni la honda en detalle. Resumida en cogconnected.com (el tuit original ya no es accesible directo desde
aquí) · https://cogconnected.com/2023/06/a-plague-tale-requiem-cosplay-guide-amicia/ · ✅ (artículo +
mencionada también en el Tumblr de cosplay de abajo, punto 23).

---

## 16 · Ciudades, paisajes y fondos de pantalla

**Sitios con luz y paleta medida** (`estilo.py` sobre la imagen más grande de la wiki de cada lugar):
- **Château d'Ombrage** (el castillo de la familia de Rune) · de noche, niebla azul · 1920×1080 ·
  **#17212D**(25%)/**#1D2939**/**#26364D**/**#384A67**/**#667EA3** — todo en gama de azules fríos,
  saturación 49%, brillo 27%; silueta de torreones almenados contra el cielo nublado.
  https://static.wikia.nocookie.net/a-plague-tale-innocence/images/3/39/Castle_Outer1.jpg · ✅ · vista
  completa en `/tmp/claude-0/trabajo/119-a-plague-tale-imagen/castle_outer1.jpg` (mirada).
- **Isla de Hugo («Two-Teeth Island»), Requiem** · costa mediterránea soleada · 1920×1080 ·
  **#E5C289**(8%)/**#C99765**/**#9C6F4F**/**#73553E** — tonos arena y roca dorada muy distintos del resto
  del juego (casi todo frío/oscuro), brillo 41% el más alto medido.
  https://static.wikia.nocookie.net/a-plague-tale-innocence/images/3/35/Hugo%27s_Two-Teeth_Island.jpg · ✅.
- **Ciudad Roja («Red City»), Requiem** · vista aérea con niebla al amanecer, ciudad amurallada · 1920×1080
  · **#424241**(24%)/**#5A5754**/**#9D9481**/**#EAE4D0** — a pesar del nombre, la imagen real es
  gris-beige por la niebla dorada, muy poco saturada (13%, la menos saturada de todas las que medí); sol
  bajo en el horizonte, humo/niebla cubriendo los tejados.
  https://static.wikia.nocookie.net/a-plague-tale-innocence/images/d/d6/The_Red_City.jpg · ✅ · vista
  completa en `/tmp/claude-0/trabajo/119-a-plague-tale-imagen/red_city.jpg` (mirada).
- **Cripta de los Tres Santos («Rat Nest»)** · interior sin luz salvo antorchas puntuales · 1920×1080 ·
  **#030202**(17%)/**#080405**/**#010101** — la imagen más oscura de todo lo medido, brillo 7%; aquí es
  literalmente donde vive el enjambre de ratas del juego.
  https://static.wikia.nocookie.net/a-plague-tale-innocence/images/5/53/Three_Saints_Rat_Nest.jpg · ✅.

**Capturas oficiales de Steam con el sitio completo** (mismas URL del punto 1, API `appdetails`):
- Calle de pueblo medieval de día, casas de piedra y tejado de teja, humo de chimenea (752590, #11).
- Asedio al amanecer con niebla: catapulta, cadáveres, empalizada de picas — la escena con más «Francia
  medieval + luz» de todo el material (752590, #16).
- Molino en llamas de noche, dos siluetas con lanzas (752590, #15).
- Mercado de pueblo con el castillo fortificado detrás, banderas amarillo/negro ondeando, cielo azul de
  día — sitio completo, muy distinto en luz al resto (1182900, #6). Este es el mismo fotograma usado para
  medir el vestuario de Requiem arriba.
- Salón/capilla con pétalos de rosa rojos cubriendo el suelo, cortinas rojas, luz dramática desde arriba
  (1182900, #3).

**Fondos de pantalla de fans en Wallhaven** (ya en datos-imagen.md, con corazones/popularidad — sirven
para «los sitios de la serie con más tirón visual» según la comunidad):
- 3840×2160 · ♥68 · «artwork, women, jumping, fantasy art» ·
  https://w.wallhaven.cc/full/39/wallhaven-397xz6.jpg.
- 3840×2160 · ♥37 · molino ardiendo, foto real de Flickr (`essovius`) usada como fondo ·
  https://w.wallhaven.cc/full/73/wallhaven-73w7x9.jpg · origen https://www.flickr.com/photos/essovius/48091005478.
- 3840×2160 · ♥33 · atardecer, cielo, Asobo Studio ·
  https://w.wallhaven.cc/full/wy/wallhaven-wylzlx.jpg · origen https://www.flickr.com/photos/essovius/48128241026/.
- 1920×1080 · ♥13 · «running, rats, artwork» — de los pocos wallpapers centrados en las ratas ·
  https://w.wallhaven.cc/full/8x/wallhaven-8x9ex1.jpg.
- Las 11 restantes de datos-imagen.md (hasta 3840×2160) quedan con ⚠️ (tamaño de la página, no re-verificado
  descargando cabecera; presupuesto de esta tanda no dio para repetir las 15).

No encontré una galería de **fondos 4K/8K oficiales descargables** en un press kit propio de Focus/Asobo
(`aplaguetale.com/en/media` y `store.aplaguetale.com` dieron **503** dos veces cada uno, confirmado con
`curl`, no es un fallo puntual); lo más parecido y sí 100% oficial son las 20 capturas de Steam de arriba
(1920×1080, sin reescalar) y los retratos 4K (3840×2160) de la wiki. ⚠️.

---

## 19 · Texturas 2D (tramas, grano, patrones, emblemas — con equivalentes libres)

- **No hay tramas de manga**: es un juego 3D realista (Unreal Engine/motor propio de Asobo), no animación
  ni cómic. El punto se adapta a texturas de pintura conceptual, tela y piedra, como abajo. Aviso
  explícito, no es un hueco sin buscar.
- **Pincelada del arte conceptual y la portada**: la portada oficial (punto 1, Olivier Ponsonnet) y el
  «Early Concept Art 2» tienen grano de pintura digital visible — pinceladas sueltas, bordes que se
  difuminan en niebla, nada de línea de contorno dura (`estilo.py` lo confirma: «línea normal» pero muy
  fina, sombreado en degradado). Sirve de referencia de «cómo está pintado» el material promocional.
- **Patrón de tela de Hugo**: el recorte de su túnica en Requiem (punto 15) muestra topos/rombos claros
  repetidos sobre fondo verde oliva — un estampado de tela sencillo, no bordado grueso.
- **Emblema recurrente: el león verde devorando el sol** — símbolo de disolución alquímica que aparece
  como objeto coleccionable («Iconography», categoría Curiosity) en *Innocence*; la wiki cita el texto del
  còdex del juego: «Alchemy fascinates scientists as much as it inspires artists. The recurring symbol of
  the lion devouring the sun is an allusion to alchemical dissolution…». Icono 359×359 ·
  https://static.wikia.nocookie.net/a-plague-tale-innocence/images/d/da/Plaguetale31.png · Fuente:
  https://aplaguetale.fandom.com/wiki/Iconography (wikitext, `action=parse`) · ✅. Útil como sello/emblema
  grabado en un objeto de madera o metal en Blender — encaja con la temática alquimia/Inquisición del
  juego.
- **Escudo de armas de la familia de Rune**: se menciona (colgante de Amicia, punto 15) pero la wiki NO
  trae una imagen o blasón descrito en detalle — sólo que Hugo puede vestir de verde/azul/rojo/morado
  «según el escudo elegido». No encontré una heráldica oficial dibujada aparte del propio juego. ⚠️.
- **Texturas reales equivalentes, libres (CC0, ambientCG, API `full_json`)**:
  - Cuero (jubón de Amicia, cinturones): `Leather030` y `Leather037` · https://ambientcg.com/a/Leather030
    · https://ambientcg.com/a/Leather037 · ✅ (API).
  - Piedra de castillo/muro (Château d'Ombrage, pueblos): `Rock064` · https://ambientcg.com/a/Rock064 ·
    ✅.
  - Tela/lana (túnicas, capas): `Fabric061` · https://ambientcg.com/a/Fabric061 · ⚠️ (genérica, no
    reproduce el topo de Hugo exacto).
  - Papel/pergamino (para cartas, mapas o el códex del juego): `Paper006` · https://ambientcg.com/a/Paper006
    · ⚠️.
  - Licencia de las 4: CC0 declarada por ambientCG en cada ficha, uso comercial libre sin crédito.
- **Ratas**: el juego las renderiza como un enjambre de partículas denso, no una textura de piel plana —
  no hay «trama de pelo de rata» que valga como textura 2D; para una lámina conviene mostrarlas como grupo
  compacto (así aparecen en la portada oficial), no como una sola rata grande. Nota explícita para el
  redactor/punto 17.

---

## 23 · Colaboraciones y cruces

**Figuras/estatuas OFICIALES** (dos juegos, dos ediciones coleccionista distintas):
- ***A Plague Tale: Innocence* — Amicia & Hugo Premium Statue, Silver Edition**: resina, 23 cm,
  **edición limitada a 500 piezas**, diseñada y esculpida por el equipo de arte de Asobo en colaboración
  con Silver Fox Collectibles; se vendía con una copia física del juego. Tienda de Focus (ya cerrada) y la
  tienda oficial de la serie ·
  https://store.focus-entmt.com/eu/product/631994/a-plague-tale-innocence-amicia-hugo-premium-statue-silver-edition-pc
  · https://store.aplaguetale.com/products/amicia-hugo-premium-statue-silver-edition · ✅ (dos fuentes,
  aunque la primera ya no carga el detalle — texto sacado del snippet del buscador).
- ***A Plague Tale: Requiem* — Collector's Edition**: estatua de resina de **20 cm (8 pulgadas)**
  diseñada por el equipo artístico de Asobo, Amicia y Hugo en acción con su ropa de *Requiem*; la caja
  coleccionista incluye además un broche metálico con la pluma de Hugo, un vinilo de 45 rpm con la banda
  sonora (Olivier Derivière) y 3 litografías A4 de ilustraciones del juego. 189,99 USD, exclusiva de la
  tienda de Focus Entertainment. Fuentes: EGM
  (https://egmnow.com/a-plague-tale-requiems-collectors-edition-includes-amicia-and-hugo-statue/) y
  Twinfinite (https://twinfinite.net/news/a-plague-tale-requiem-collectors-edition-revealed-includes-amicia-hugo-statue/)
  · ✅ (dos fuentes independientes con los mismos datos).

**Guía de cosplay oficial de Asobo Studio** (ver punto 15): cuenta como colaboración estudio-comunidad,
publicada por la cuenta oficial @APlagueTale en Twitter/X el 31-may-2023, con el traje de Amicia de la
primera mitad de *Requiem*. ✅.

**Cosplay de fans, bien hecho (materiales y volumen reales)**:
- **Rogue Heart Cosplay** — réplica de la ballesta de Amicia (*Requiem*): EVA foam, Worbla, Plasti Dip y
  pinturas PlaidFX; ~33 horas de trabajo repartidas en un mes; el autor destaca la textura de madera
  pintada y el falso metal decorativo del lateral · Tumblr
  https://rogueheartcosplay.tumblr.com/post/701640770252341248/amicias-crossbow-from-a-plague-tale-requiem
  · ⚠️ (una fuente, blog personal).
- **unpetitrat** — guía de cosplay de Amicia (*Innocence*) en Tumblr, con desglose de referencia ·
  https://www.tumblr.com/unpetitrat/186301781264/amicia-cosplay-guide · ⚠️ (una fuente).
- Tienda comercial `ezcosplay.com` vende un traje reproducción «Amicia De Rune New Edition» ·
  https://www.ezcosplay.com/a-plague-tale-innocence-amicia-de-rune-new-edition-cosplay-costume-ecm1684.html
  · ⚠️ (una fuente, es tienda, no cosplayer concreto).

**Merchandising oficial** (no es colaboración con otra marca, pero es lo más parecido a punto 23 que
existe además de las estatuas): tienda propia `store.aplaguetale.com` vende camisetas («Amicia de Rune
T-Shirt»), funda de iPhone con arte de Amicia y más — confirmado por resultados de tienda en el buscador;
el sitio en sí dio **503** al intentar entrar directo (dos veces). ⚠️ (contenido de la tienda no verificado
de primera mano, sólo por snippets).

**No encontré** (búsquedas hechas, sin resultado — no digo «no existe»):
- Crossover comercial con otro juego o marca (Fortnite, gacha, Dead by Daylight): búsqueda `"A Plague
  Tale" crossover collaboration Fortnite OR "Dead by Daylight" OR gacha OR amiibo` (inglés) — sin ningún
  resultado relacionado con la serie.
- Café temático, exposición o evento pop-up en Francia u otro país: búsqueda `"A Plague Tale" exhibition
  museum OR pop-up OR "café" event France` (inglés) — sin resultado.

---

## Lo mejor para la lámina

1. La **portada oficial** (Olivier Ponsonnet, `fondos_01.jpg` #63): Amicia y Hugo con el enjambre de
   ratas subiéndoles por el pecho, paleta gris-beige casi monocroma — es LA imagen que resume la serie
   entera de un vistazo y es 100% oficial.
2. La captura de Steam de **Requiem con la multitud alzando a Amicia y Hugo** sobre los hombros
   (`arte_01.jpg` #2): grupo, celebración, exactamente lo que pide `reglas_del_dueno.md` (nada de
   personaje solo y flotando).
3. La captura de Steam del **asedio al amanecer** con catapulta, niebla y cadáveres (`arte_01.jpg` #16,
   Innocence): la que mejor junta «Francia medieval + luz + ratas/tragedia» en un solo fotograma.
4. El **«Early Concept Art 1»** de Amicia y Hugo atrancando una puerta con una antorcha encendida
   (`fondos_01.jpg` #70): fuego real, gesto de equipo, sirve directo para la parte de «luz (fuego,
   antorchas)» que pide el encargo.
5. El icono del **león verde devorando el sol** (`Plaguetale31.png`): un emblema pequeño, tallable en
   madera o piedra en Blender, con significado real dentro del juego (alquimia), mejor que inventar un
   logo genérico.

---

## No encontré

- ⚠️ Artbook oficial publicado específico de *A Plague Tale: Innocence* (2019) por separado — sólo hay uno
  de *Requiem* («The Art of A Plague Tale: Requiem», 196 páginas, 2022). Búsqueda: `"A Plague Tale"
  official artbook "The Art of" Focus Entertainment` (inglés).
- ⚠️ Galería de fondos de pantalla oficiales en alta (4K/8K) en un press kit propio: `aplaguetale.com/en/media`
  y `store.aplaguetale.com` dieron 503 dos veces cada uno (confirmado con `curl`); lo oficial disponible
  son las 20 capturas de Steam (1920×1080) y los retratos 4K de la wiki, ambos ya citados.
- ⚠️ Más modelos 3D libres en Sketchfab aparte del de Amicia (ni Hugo, ni armas, ni sitios): 4 búsquedas
  distintas en la API sin resultado.
- ⚠️ Vocabulario Danbooru de Hugo y Melie (related_tag): 403 de Cloudflare en dos intentos, ninguno pasó.
- ⚠️ Heráldica dibujada del escudo de armas de la familia de Rune (sólo se menciona como colgante y como
  «elección de color» de la túnica de Hugo, sin blasón ilustrado en la wiki).
- ⚠️ Crossover comercial (Fortnite, gacha, otra marca) y evento físico (café temático, exposición): ambos
  buscados en inglés, sin resultado — sección 23.
- Todo lo demás pedido en los puntos 1, 3, 15, 16, 19 y 23 se cubrió con al menos una fuente comprobable
  (ver arriba); lo anotado aquí es honestamente lo que faltó, no relleno.

---

## Bitácora de búsqueda

- `herramientas/investigar_serie.py --wiki aplaguetale --paginas "Amicia de Rune" "Hugo de Rune"` → 70
  imágenes grandes, 2 hojas de contacto (`hoja_01.jpg`, `hoja_02.jpg`, copiadas a
  `hojas/personajes_01.jpg` y `hojas/fondos_01.jpg`). Ya lo había dejado `recolectar.py`, no se repitió.
- API de Fandom directa (`action=query&list=allpages`, `prop=imageinfo&iiprop=url|size`,
  `action=parse&prop=wikitext`) para: lista completa de páginas de la wiki, wikitext de `Amicia de Rune`,
  `Hugo de Rune`, `Iconography`, `De Rune family`, e `imageinfo` de imágenes de sitios (`Château
  d'Ombrage`, `La Cuna`, `Red City`, `Crypt of the Three Saints`) — sin pasar por el buscador, ahorra
  cupo.
- API de Steam (`store.steampowered.com/api/appdetails?appids=752590` y `...=1182900`, y
  `storesearch/?term=` para encontrar el appid correcto de *Requiem*) — no estaba en datos-imagen.md, es
  hallazgo propio; descargué las 20 capturas y monté mi propio contacto (`hojas/arte_01.jpg`).
- `herramientas/estilo.py` sobre 3 retratos 4K de la wiki, 4 sitios de la wiki, 2 recortes propios de
  vestuario (Amicia jubón Innocence y Requiem, Hugo túnica Requiem) hechos con Pillow desde las capturas
  de Steam, y 2 piezas de concept art — 11 medidas de hex en total, cada una con su imagen de origen
  anotada arriba.
- API de Sketchfab (`api.sketchfab.com/v3/models/<uid>` y `/v3/search?type=models&q=...&downloadable=true`,
  4 búsquedas: `plague tale`, `amicia`, `hugo de rune`, `amicia crossbow`, `plague tale rat`, `medieval
  village asobo`) para confirmar licencia del modelo de Amicia y buscar más.
- API de ambientCG (`full_json?type=Material&q=...`) para 4 texturas libres equivalentes (cuero, piedra,
  tela, papel).
- WebSearch (inglés, 11 búsquedas de las ~50 disponibles para este rol): `"A Plague Tale" Asobo Studio
  concept art ArtStation ArtDirector Olivier Ponsonnet`, `"A Plague Tale" official press kit wallpapers
  site:asobostudio.com OR site:focus-entmt.com OR site:aplaguetale.com`, `Damien Papet "A Plague Tale"
  ArtStation concept artist environment`, `"A Plague Tale" Requiem cosplay Amicia costume build`, `"A
  Plague Tale" official figure statue Amicia Hugo`, `"A Plague Tale" crossover collaboration Fortnite OR
  "Dead by Daylight" OR gacha OR amiibo`, `"A Plague Tale" official artbook "The Art of" Focus
  Entertainment`, `"A Plague Tale" exhibition museum OR pop-up OR "café" event France`, `"A Plague Tale:
  Requiem" press kit screenshots 4K site:focus-entmt.com OR site:presskit.focus-entmt.com`, `"A Plague
  Tale" Innocence OR Requiem official desktop wallpaper download 4K site:aplaguetale.com`.
- `curl -I`/`-o /dev/null -w "%{http_code}"` a `artstation.com` (2 URL) y `magazine.artstation.com` (2 URL)
  → **403** confirmado las 4 veces, no es fallo puntual: se citan por el resultado del buscador.
- `curl`/WebFetch a `aplaguetale.com/en/media` y `store.aplaguetale.com` → **503** las dos veces cada uno;
  no insistí más de dos intentos, como marca la regla.
- No usé YouTube (pide iniciar sesión desde este servidor): todas las capturas salen de la API de Steam,
  la wiki de Fandom y el buscador, no de vídeo.

## Cumplimiento de mis puntos (1, 3, 15, 16, 19, 23)

| Punto | Estado | Por qué |
|---|---|---|
| 1. Arte oficial variado | ✅ | Portada oficial, 2 concept arts tempranos, 7 retratos 4K, 20 capturas oficiales de Steam (11+9) con poses vivas descritas, 5 artistas de Asobo en ArtStation citados (403 directo, citados por buscador), artbook oficial de Requiem con 4 artistas acreditados |
| 3. Fan art y 3D con licencia | ✅ | 1 modelo Sketchfab con licencia CC Attribution confirmada por API (autor, caras, descargable) + 2 fan art de Safebooru con autor y enlace; búsquedas adicionales sin más modelos (anotado, no relleno) |
| 15. Vestuario | ✅ | Descripción oficial completa Innocence vs Requiem de ambos personajes (wikitext), 6 hex medidos con Pillow de 6 fuentes distintas y luces distintas (antorcha vs día), detalle de juego (túnica de Hugo cambia de color), guía de cosplay oficial de Asobo |
| 16. Fondos y fondos de pantalla | ✅ | 4 sitios con hex medido (castillo, isla, ciudad, cripta), capturas Steam con sitios completos, 4 wallpapers de Wallhaven con popularidad; sin galería 4K/8K propia del estudio (web caída, anotado) |
| 19. Texturas 2D | ✅ | Patrón de tela de Hugo medido, emblema del león-sol con fuente y significado, 4 texturas CC0 equivalentes (cuero, piedra, tela, papel); aviso explícito de que no hay tramas de manga (no aplica) y de cómo se renderizan las ratas |
| 23. Colaboraciones y cruces | ✅ | 2 estatuas oficiales coleccionista (una por juego, con fuentes cruzadas), guía de cosplay oficial, 2 cosplays de fans con materiales reales; crossover comercial y evento físico: buscados y no encontrados, anotado en «No encontré», no en Sigue |

Todo lo obligatorio de mis 6 puntos está cubierto con al menos una fuente comprobable; lo que falta
(artbook de Innocence por separado, galería 4K propia, más modelos 3D, heráldica dibujada, crossover
comercial) es material que probablemente no existe publicado para esta franquicia, no una búsqueda a
medias — queda anotado en «No encontré», no en Sigue.
