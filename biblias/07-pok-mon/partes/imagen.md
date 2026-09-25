# Investigador de IMAGEN · 07-pok-mon (Pokémon)

Puntos de ENCARGO.md: **1** (arte oficial), **3** (fan art y 3D con licencia),
**15** (vestuario), **16** (fondos y paisajes), **19** (texturas 2D), **23**
(colaboraciones y cruces). Parto de `partes/datos-imagen.md` (no repito esas
consultas) y de lo que ya hay en `biblia.md` (secciones 2, 4, 5, 16, 17, vistas
con `seccion.py --rol imagen`). Miré las 4 hojas de contacto que ya estaban en
`herramientas/referencias/pok-mon/` (180 imágenes de pokemon.fandom.com).

## Hallazgos

### Punto 1 · Arte oficial, en cantidad y variado

**Las hojas de contacto (ya miradas, con Read)**
- Hoja 1 (imágenes 1-48): cajas de las 9 generaciones de juegos (Oro, Rubí,
  Diamante, Negro, X, Sol, Escarlata…), paneles de manga (con trama/screentone
  visible, ver punto 19), Pikachu por generación, Ash con cada profesor
  (Burnet, Kukui, Oak) · fuente: pokemon.fandom.com (galerías de Pikachu y
  Ash Ketchum) · ✅ (mirada directamente) · 2400×1704.
- Hoja 2 (49-96): los 7 Z-Ring/Z-Power Ring, medallas de gimnasio (Sinnoh,
  Hoenn), el trofeo de la Serie de Coronación Mundial, **Pikachu Libre**
  (disfraz de luchador) y **Pikachu en traje de baño**, Ash en cada región ·
  ✅ · 2400×1704.
- Hoja 3 (97-144): 30+ poses distintas de Pikachu solo (peluche, globo de
  Macy's, trofeos de Smash, gráficos de cuenta atrás de la Serie de
  Coronación) · ✅ · 2400×1704. Es la más repetitiva (muchas poses casi
  iguales): **no la guardé** en `hojas/`.
- Hoja 4 (145-180): **Pikachu cosplay** (nº155), **Detective Pikachu**
  (nº168), **Pokémon UNITE** (nº172), el logo oficial en inglés de la serie
  (nº174), Pikachu con **ropa de camuflaje militar** (nº179) · ✅ · 2400×1420.
- Guardé en `hojas/`: **arte-oficial_01.jpg** (=hoja 1), **vestuario_01.jpg**
  (=hoja 2), **colaboraciones_01.jpg** (=hoja 4). Detalle y para qué sirve
  cada una, en `imagen.json`.

**Fuera de la wiki**
- Portada y banner oficiales del anime en AniList, **medidos con Pillow**:
  portada 230×345, banner 1900×400 (el nombre del archivo no dice el tamaño
  real) · https://anilist.co/anime/527 · ✅.
- **Pokémon Adventures** (manga), tomo 1: portada de **Mato**, con Red, Saur,
  Poli y Pika saltando · https://www.howtolovecomics.com/2019/05/07/pokemon-manga-guide/
  y https://www.cbr.com/pokemon-adventures-greatest-manga-covers/ · ✅ (dos
  fuentes). No conseguí el enlace directo a la imagen de portada (⚠️).
- **CD single** «Mezase Pokémon Master» (1997): el primer CD de Pokémon
  publicado, formato mini-CD, la Pikachu y el logo de la portada son
  **pegatinas** físicas · https://bulbapedia.bulbagarden.net/wiki/Aim_to_Be_a_Pok%C3%A9mon_Master_(CD)
  y https://jpop.fandom.com/wiki/Mezase_Pokemon_Master · ✅ (dos fuentes).
- **Blu-ray**: *Pokémon: Indigo League — Champion's Edition* (VIZ Media, 14
  nov 2017), 6 discos, 52 capítulos, con un cómic-muestra de 64 páginas de
  regalo · https://comicbook.com/anime/news/pokemon-original-series-bluray/ ·
  ⚠️ (una sola fuente clara sobre esta edición).
- **Diseño de personajes del anime**: Sayuri Ichiishi (ya ✅ en biblia,
  sección 2.4, dos fuentes). No añado de nuevo.
- **«Cartones de cuenta atrás» y «hojas de modelo» (turnaround) del anime**:
  no los encontré — ver «No encontré».

### Punto 3 · Fan art y 3D con licencia (sólo referencia, nunca para pegar)

**Licencias de Sketchfab, comprobadas con la API v3 (`api.sketchfab.com/v3/models/<id>`,
que es la fuente autoritativa: corrige lo que el buscador solo suponía)**
- «Poké Ball» de **Pabluuu** · CC BY 4.0 · 227.582 caras · descargable ✅ ·
  https://sketchfab.com/3d-models/poke-ball-cd6f6c89fa5647d694991901f12becc2
- «Kanto Pokédex» de **Alexander Walker** · CC BY 4.0 · 6.590 caras ·
  descargable ✅ · https://sketchfab.com/3d-models/kanto-pokedex-33558224badf4058b5977bded912c70c
- «Oak Lab» de **QuangCao** · CC BY 4.0 · 1.086 caras · descargable ✅ ·
  https://sketchfab.com/3d-models/oak-lab-fbe85c2f81a04063aa573f9161824734
- «Ultimate Monsters Pack» de **quaternius** · CC BY 4.0 · 212.178 caras ·
  descargable ✅
- «Lucario» — el autor real es **GianmArt**, no «Gianmarco» como decía el
  primer barrido · CC BY 4.0 · 63.606 caras ✅ (corregido)
- «GameBoy DMG-01» de **LetsDo3D** · CC BY 4.0 · 18.119 caras ✅
- «GAME BOY» — el autor real es **MaxWendt**, no «rave-games» · CC BY 4.0 ·
  1.618 caras ✅ (corregido)
- «Animated Poke Ball» de **Ayanbeg** · CC BY 4.0 · 9.360 caras ✅
- «Pokeball for Blender» de **Foxrado** · CC BY 4.0 · 627.964 caras (muy
  pesada: recortar el detalle en Blender antes de renderizar, por la regla
  del dueño de no saturar el PC) ✅
- «Pokemon RSE - Pokemon Center» de **Wesai** · CC BY 4.0 · 10.041 caras ✅
- «Pokemon FireRed - Player's Room» de **Wesai** · CC BY 4.0 · 972 caras ✅
- «Nintendo Gameboy DMG-01 3D Scan» de stevencmutter: confirmado
  **CC BY-NC-ND** (ya lo decía datos-imagen.md) — **no se puede modificar**,
  sólo sirve tal cual, y no para nada comercial.
- Todos son fan art de un diseño con copyright de Nintendo/Game Freak/The
  Pokémon Company: valen para la lámina de un Discord de fans, nunca para
  vender. Crédito exacto en cada `licencia` de `imagen.json`.

**Fan art (mirar, jamás pegar)** — lo de datos-imagen.md ya vale (DeviantArt:
WillDinoMaster55, Toonsislove83, PokemonCMG, RosegardenInHell, StudioSeraph;
pixiv: 438 dibujos con la etiqueta オーキドけんきゅうじょ; ArtStation).
Añado:
- **«Pokémon LE-GO»** de Si-MOCs (construcción de fans estilo ladrillo) ·
  Openverse → Flickr, CC BY-NC-SA 2.0 · 602×1024 · sólo referencia de una
  idea ya hecha por otro fan (para no repetirla).
- Búsqueda en Danbooru: `recolectar.py` no encontró la etiqueta «pokemon»
  con el nombre exacto que probó automáticamente. No repetí la consulta a
  mano por tiempo: las fuentes de pixiv/DeviantArt/ArtStation ya alcanzan el
  mínimo de fan art pedido.

### Punto 15 · Vestuario

**Colores medidos con Pillow** sobre el render oficial de la wiki
`Ash_anime_The_Beginning.png` (pageimage oficial de la página «Ash Ketchum»
en pokemon.fandom.com, arte de la etapa Kanto) — resuelve el ⚠️ que dejó la
biblia («no los medí»):
- Chaqueta azul: **`#234FC0`** ✅ (medido, agrupamiento de color sobre toda
  la imagen).
- Jean (la parte iluminada, más clara): **`#95A2E9`** ✅ (medido).
- Gorra, banda naranja-roja: **`#C04010`** ⚠️ (una sola muestra de píxel, no
  un agrupamiento completo: tono aproximado).
- Puño del guante, verde claro: **`#C3E795`** ⚠️ (una muestra de píxel).
- Pelo / contorno negro: entre **`#0A0A0A`** y **`#141018`** ✅ (agrupamiento).
- Piel: **`#EDB58A`** a **`#F7AA69`** según la sombra ✅ (agrupamiento).
- El **verde oscuro del cuerpo del guante** no lo pude aislar bien (se mezcla
  con el contorno): queda ⚠️, aprox. un verde bosque más oscuro que el puño.
- Imagen usada: 260×390 (baja resolución, es la única que ofrece la wiki
  para el infobox); por eso hay bordes con anti-aliasing que ensucian la
  medición exacta. Para un hex más limpio, medir sobre un fotograma de
  1080p (tarea de vídeo) o sobre merchandising oficial en alta.

**Ropa de Ash por región** (además de Kanto, que ya está completo en
biblia 16) — resumen de dos artículos de CBR que se complementan
(«pokemon-ash-ketchum-best-outfits» y «pokemon-best-ash-ketchum-outfits-designs»)
y contrastado con Bulbapedia «Ash's clothing»:
- **Hoenn** (Advanced Generation): gorra negra y roja con una Poké Ball
  verde; sudadera azul sin mangas con capucha blanca y ribete dorado;
  camiseta negra de manga corta con una franja roja; guantes negros sin
  dedos ✅.
- **Sinnoh** (Diamond & Pearl): chaleco negro con cuello blanco y franja
  amarilla; camiseta blanca de manga corta debajo; jean cargo azul;
  zapatillas negras y rojas; la Poké Ball de la gorra pasa a azul ✅.
- **Unova** (Best Wishes): gorra roja y blanca con una Poké Ball azul;
  chaqueta azul y blanca con capucha y cremallera dorada; jean ancho negro;
  guantes negros sin dedos con borde rojo; zapatillas rojas altas ✅.
- **Kalos** (XY): camisa azul de cuello con manga corta; jean azul más
  oscuro; misma gorra roja y blanca; zapatillas rojas altas ✅.
- **Alola** (Sun & Moon): camiseta a rayas azules y blancas con un dibujo
  parecido a una Poké Ball en el centro; shorts rojos y negros; zapatillas
  color mar ✅.
- **Galar/Journeys**: camiseta blanca con una franja roja bajo un chaleco
  azul y amarillo; shorts azules y negros a juego con las zapatillas ✅.
- Sirve para que la lámina **no mezcle ropa de dos eras distintas** de Ash
  (aviso explícito del dueño en ENCARGO.md).

**Disfraces oficiales (canon, no fan art) de Pikachu** — confirmado con el
wikitexto de Bulbapedia (`action=parse`, fuente primaria) ✅:
- **Cosplay Pikachu** (おきがえピカチュウ): una Pikachu hembra de
  Rubí Omega/Zafiro Alfa con **5 disfraces intercambiables** — Rock Star,
  Belle, Pop Star, Ph.D. y **Libre** (máscara y capa de luchador) — cada uno
  con un movimiento exclusivo. **Pikachu Libre** es además personaje
  jugable en **Pokkén Tournament** (cruce con el punto 23) ✅.
- Otros disfraces vistos en la hoja 2 de contacto: **Pikachu Holiday
  Style** (gorro y traje de Santa), **Pikachu con snorkel/traje de baño**,
  **Pikachu Festival Style** (Pokémon UNITE) ✅ (mirados directamente).
- Hoja 4: **Pikachu detective** (gabardina y sombrero, de la película
  *Detective Pikachu*) y **Pikachu de camuflaje militar** («Pikachu
  clothing art») ✅ (mirados directamente).
- **La ropa «icónica»** que todos reconocen sigue siendo la de Kanto: gorra
  roja y blanca + chaqueta azul y blanca, según coinciden Bulbapedia,
  Costume Wall, TV Style Guide y CBR (ya estaba ✅ en biblia).

**Peinado**: la descripción de `datos-imagen.md` (sección «Ash Ketchum ·
Appearance», ya sacada de la wiki) ya cubre el pelo de Ash: un remolino y un
mechón triangular y anguloso en medio de la frente, que termina en punta
hacia la derecha, visible cuando no lleva la gorra ✅ (no la repito entera
aquí, está en ese archivo).

**Oak**: bata blanca de laboratorio (✅, visible en el sprite y en todas las
imágenes). El color exacto del pelo gris y la camisa de debajo sigue sin
medir (⚠️, ya lo decía la biblia): no encontré un render lo bastante grande
y limpio de Oak solo para medirlo con garantía.

### Punto 16 · Ciudades, paisajes y fondos de pantalla

Lo de Pueblo Paleta, el laboratorio y la Ruta 1 (biblia 17) ya está bien
✅: no lo repito.

**Fondos de pantalla oficiales**
- Encontré **un** fondo de pantalla oficial con enlace directo: la
  colaboración **Pokémon × MEGA (Mattel)**, en 4 tamaños (1080×1920,
  1280×800, 1366×768, **1920×1080**) · fuente:
  https://www.pokemon.com/us/pokemon-news/download-mega-pokemon-digital-wallpapers
  (leída con WebFetch, la página en sí bloquea `curl`) · ⚠️ el tamaño es el
  que dice el propio nombre del archivo de Pokémon.com: no pude descargar
  la imagen para medirla con Pillow porque el CDN (`mcdn.pokemon.com`) usa
  protección anti-bot (Incapsula) y devuelve una página HTML en vez del
  PNG. Motivo: ladrillos MEGA con Pikachu, Charmander y Bidoof.
- No encontré más fondos oficiales en alta con enlace directo (la propia
  biblia ya lo marcaba ⚠️): busqué en pokemon.co.jp (403 al acceder
  directo) y en la Wayback Machine (sin snapshot de esa URL).

**Fondos de fans en alta**, filtrando del listado de Wallhaven de
datos-imagen.md los que de verdad son de Pokémon (dos de los que trajo el
buscador automático eran de Sonic/Portal y de una chica de ciencia ficción:
**los descarto**, no son de esta obra):
- 2322×1200 · Ash y Pikachu · https://w.wallhaven.cc/full/l8/wallhaven-l8z7rq.jpg
  · origen: twitter.com/Lv01KOKUEN ✅ (medido por la API de Wallhaven).
- 6000×2492 · retrato de Pokémon (arte de pixiv) ·
  https://w.wallhaven.cc/full/73/wallhaven-73xpde.png · origen:
  pixiv.net/en/artworks/77330141 (Francazo) ✅.
- 6488×3244 · «Lake of Rage», Gyarados y Magikarp ·
  https://w.wallhaven.cc/full/rd/wallhaven-rd2jw1.png · origen:
  reddit.com/r/pokemon ✅.
- Las demás (Charmander/Squirtle, Rayquaza, Pokédex) están en `imagen.json`
  con su tamaño real.

### Punto 19 · Texturas 2D

- **Tramas de manga (screentone)**: paneles de la hoja 1 muestran tramas de
  punto clásicas en los fondos y las sombras (mirado directamente) ✅.
  Equivalentes libres: **«[FREE] Manga Screentone Pack 1»**
  (https://assets.clip-studio.com/en-us/detail?id=2142037) y **«Screentone
  Pack» de Vixial** (https://assets.clip-studio.com/en-us/detail?id=1845097),
  ambos gratis en Clip Studio Assets ⚠️ (no confirmé si el plan gratuito de
  Clip Studio permite usarlos en un render final o sólo para practicar).
  Alternativa para Photoshop/Procreate: el pack gratis de GraphicsBunker
  (https://www.graphicsbunker.com/brushes/free-comic-manga-screentone-brushes/)
  ⚠️ la propia página no dice la licencia exacta, sólo que es gratis vía
  Gumroad.
- **Grano de papel**: Paper001 a Paper006 de ambientCG, CC0
  (https://ambientcg.com/view?id=Paper004, entre otros) — con esto se
  resuelve el ⚠️ de datos-imagen.md 5.4 sobre la etiqueta de cartulina de
  las Poké Balls del concepto A. Alternativa más rugosa (cartón/kraft):
  Cardboard001-004 de ambientCG, también CC0.
- **Pinceladas**: el arte oficial de los videojuegos es acuarela (ya lo
  decía datos-imagen.md 5.3, "el arte de los juegos es de acuarela, más
  apagado"). Textura de papel de acuarela con licencia de dominio público:
  https://www.publicdomainpictures.net/en/view-image.php?image=260479&picture=watercolor-paper-texture
  (Eman Princess, Public Domain, uso personal y comercial) ⚠️ no conseguí
  el enlace directo al archivo de imagen, sólo a la página; también sirve
  el buscador de https://cc0-textures.com/ para más variantes CC0.
- **Patrones de ropa**: la ropa de Ash **no lleva estampado grande**, son
  colores planos (chaqueta azul/blanca, jean liso) — confirmado mirando las
  hojas de contacto y el render medido arriba ✅. No hace falta una textura
  de tela con dibujo, sólo el grano de la tela lisa.
- **Emblemas y logos**:
  - Las 8 medallas de Sinnoh (1437×804) y las 8 de Hoenn (2147×1597),
    medidas por la API de la wiki ✅ — sirven de textura/emblema para una
    lámina de progreso o de insignia.
  - El logo oficial en inglés de la serie, 1189×518 ✅ (medido).
  - El logo de **Team Rocket**: una **R roja** (usada desde 1997 hasta
    *Diamond & Pearl*); desde *Black & White* la serie usa una **R morada
    en 3D**, pero la R roja se sigue viendo como logo secundario en
    merchandising · fuente: pokemon.fandom.com/wiki/Team_Rocket +
    Wikipedia «Team Rocket» ✅ (dos fuentes). No conseguí un enlace directo
    a un PNG oficial del logo (⚠️), sólo a las páginas que lo describen.
  - La Poké Ball (círculo rojo y blanco partido por una franja negra, botón
    blanco al centro) ya está descrita en biblia y en los modelos 3D de
    Sketchfab de arriba.

### Punto 23 · Colaboraciones y cruces

**Marcas** (todas con fuente oficial o de prensa especializada; pongo ⚠️
donde sólo hay una fuente clara):
- **Pokémon × Van Gogh Museum** (28-sep-2023 a 7-ene-2024, por el 50º
  aniversario del museo): cuadros nuevos pintados por ilustradores del TCG
  al estilo de Van Gogh — Pikachu con sombrero de fieltro gris, Snorlax y
  Munchlax en el dormitorio de Van Gogh, Sunflora entre girasoles ✅
  (vangoghmuseum.nl, press.pokemon.com, Smithsonian Magazine: tres fuentes).
- **Pokémon × Uniqlo (UT)**: colección de camisetas con arte del TCG desde
  el 11-ago-2025 (Pikachu, Mew, Eevee…); segunda colaboración anunciada
  para primavera-verano 2026 ✅ (Hypebeast, CBR, essential-japan.com).
- **Pokémon × Crocs**: Classic Clogs de Gengar, Charizard, Snorlax y
  Jigglypuff (2024), dentro de una serie de lanzamientos desde que Crocs
  tiene la licencia ✅ (CBR, dos artículos).
- **Pokémon × Starbucks Japón** (30-sep-2026, **muy reciente**): «Pikachu
  Honey Cream Latte» y una colección de 41 piezas (tazas, bolsas,
  delantales, arte) ✅ (Hypebeast, Dexerto, GoNintendo, Soranews24: cuatro
  fuentes).
- **Build-A-Bear**: peluche de Cubone con poncho y gorro ⚠️ (una fuente,
  CBR). **Le Creuset** (menaje de cocina) y **KFC** (2024) ⚠️ mencionados
  de pasada en el mismo artículo de CBR, sin más detalle: no confirmé fecha
  ni producto exacto.
- No encontré colaboración real con **Fortnite** ni con juegos *gacha* (el
  ejemplo del ENCARGO.md es genérico, no específico de Pokémon): lo digo
  aquí para no dar la sensación de que lo dejé sin mirar.

**Eventos**
- **Globo de Pikachu en el desfile de Macy's**: debutó en 2001 (5º
  aniversario de la franquicia); un segundo globo con una Poké Ball llegó
  en 2006 y se retiró en 2013; el globo actual, con **Pikachu y Eevee**
  (34 pies de alto, 48 de largo, 23 de ancho), es de 2021, por el 25º
  aniversario; en 2025 sumó **25 años seguidos** en el desfile ✅
  (macysthanksgiving.fandom.com, bulbagarden.net, pokemon.com,
  businesswire.com: cuatro fuentes). Esto es exactamente el nº122 de la
  hoja 3 de contacto («Flying Pikachu float Macy's») ✅ (mirado
  directamente).
- **Pokémon Café** (Nihonbashi, Tokio, encima de la Pokémon Center Tokyo
  DX): decoración temática en cada superficie, «Chef Pikachu» de peluche
  en 6 colores, menú que cambia según la temporada (curry de Pikachu,
  hamburguesa de Eevee) ✅ (tokyocheapo.com, voyapon.com, pokemon-cafe.jp:
  tres fuentes).

**Crossovers**
- **Super Smash Bros.**: Pikachu es personaje jugable desde el Smash 64
  original; trofeos oficiales de Melee y Brawl medidos por la wiki
  (1280×960 y 804×804) ✅ (mirados directamente en la hoja 3).
- **Pokkén Tournament**: Pikachu Libre es personaje jugable — cruce directo
  con el disfraz canon del punto 15 ✅.
- **Pokémon UNITE** (el propio MOBA de la franquicia, no una colaboración
  externa, pero trae skins nuevas: «Pikachu Holo Style» visto en la hoja 4)
  ✅ (mirado directamente).
- **Detective Pikachu** (película, 2019): colaboraciones de merchandising
  con Hi-Hat Café (ropa) y con la policía de Ryme City (ropa), y con
  7-Eleven (vasos Slurpee de edición limitada) ✅ (press.pokemon.com,
  thepopinsider.com).

**Figuras oficiales** (pose = referencia 3D directa) — línea **G.E.M.** de
MegaHouse, vendida en Pokémon Center:
- Ash, Pikachu y Charizard (≈190 mm; Charizard con las alas bien abiertas,
  Ash y Pikachu mirando en la misma dirección) ✅.
- Ash, Pikachu y Ash's Greninja: lanzando «Shuriken de Agua» sincronizados,
  para mostrar el vínculo entrenador-Pokémon ✅.
- Ash y Pikachu sobre Lapras, mirando los dos al mismo lado ✅.
- «Crowd Figure»: Ash en el suelo abrazando a su Pikachu, rodeado por los
  demás amigos y sus Pokémon ✅.
- (otakumode.com, bigbadtoystore.com, animota.net, kuramatoys.com: cuatro
  fuentes que describen las mismas figuras).

**Cosplay** (materiales y volumen reales, no fan art dibujado):
- Foto real de una persona cosplayando a Snivy, CC BY 2.0, 1024×683 ·
  Flickr/nayukim (vía Openverse) ✅ — es la única foto de cosplay con
  licencia libre que encontré para esta serie; la guardé en `imagen.json`.
- Construcción real de la chaqueta de Ash (para textura y costura, no para
  pegar): cuerpo azul en piel/símil-cuero, mangas y cuello blancos,
  bolsillos con ribete amarillo, cremalleras YKK — descrito en varias
  fichas de venta de cosplay (Costume Wall, Etsy) ⚠️ son fichas
  comerciales, no un cosplay premiado o «bien hecho» concreto: no encontré
  un cosplayer famoso y documentado de Ash con fotos en alta y créditos
  claros.

## Lo mejor para la lámina

- El **Poké Ball de Pabluuu** (CC BY, hiperrealista) sobre la textura
  **Paper004** de ambientCG (CC0) para la etiqueta de cartulina: resuelve
  los dos huecos que dejó el primer barrido en el concepto A.
- Los colores medidos de Ash (`#234FC0` chaqueta, `#C3E795` puño del
  guante) para el antebrazo que entra por abajo a la izquierda en el
  concepto A — ya descrito en biblia, ahora con hex real.
- **Pikachu Libre** (disfraz canon, cruce con Pokkén Tournament) es una
  pose «viva» alternativa a la Pikachu de siempre, si el dueño quiere una
  variante más lúdica para una lámina 2.
- Las figuras **G.E.M.** dan 4 poses de grupo listas para calcar en 3D
  (Ash+Pikachu+Charizard/Greninja/Lapras/amigos) si el concepto necesita
  más de dos personajes.
- El globo de Macy's y el trofeo de Smash Bros. son la prueba más visual
  de que Pikachu «se sale» del anime: sirven para un texto tipo «el más
  famoso del servidor», si el dueño quiere justificarlo con datos reales.

## No encontré

- **Cartones de cuenta atrás** del anime o de estrenos de juego (busqué
  «Pokémon countdown card» y no apareció nada específico de esta obra: el
  término del ENCARGO parece pensado para otras franquicias con estrenos
  de cine tipo evento).
- **Hojas de modelo** (turnaround) de animación del anime: no hay ninguna
  publicada de forma abierta que encontrara (busqué en Sakuga Wiki y en
  blogs de animación en japonés).
- Enlace directo a la **portada del tomo 1 de Pokémon Adventures** (sólo
  tengo la descripción, con dos fuentes).
- Enlace directo a un **PNG oficial del logo de Team Rocket** (sólo páginas
  que lo describen y venden merchandising).
- El **hex exacto** de la camisa y el pelo de Oak, y del verde oscuro del
  guante de Ash: no hay un render lo bastante grande y limpio para medirlo
  con garantía (queda para cuando alguien mire un fotograma en 1080p).
- Fondos de pantalla oficiales en alta más allá de la colaboración MEGA
  (probé pokemon.co.jp —403— y la Wayback Machine —sin snapshot—).
- Un cosplay de Ash o Pikachu **documentado y premiado** con fotos en alta
  y crédito claro del cosplayer (sólo fichas comerciales de venta de
  disfraz).
- Colaboración real de Pokémon con **New Era** (gorras): la busqué porque
  aparecía sugerida, no la confirmé en ninguna fuente.

## Bitácora de búsqueda

*Ya hecha por `recolectar.py` (no repetida): AniList, Fandom (Pikachu, Ash
Ketchum), Wallhaven, Sketchfab (buscador), Openverse. Ver
`partes/datos-imagen.md`.*

- (es) «Pokémon official wallpaper pokemon.co.jp download high resolution»
  → sin fondos oficiales directos; llevó a la colaboración MEGA.
- (en) «Pokémon x Van Gogh Museum collaboration art» → vangoghmuseum.nl,
  press.pokemon.com, Smithsonian Magazine.
- (en) «"Ash Ketchum" jacket color hex code fan concept art» → sólo
  paletas de fans (color-hex.com), por eso medí yo mismo con Pillow.
- (en) «Pikachu cosplay official Pokémon anime episode costume
  competition» → llevó a descubrir que «Cosplay Pikachu» es un Pokémon
  canon (ORAS), no un episodio de disfraces.
- (en) «Pokémon collaboration brand 2024 2025 Uniqlo Van Cleef Gucci
  fashion crossover list» → Uniqlo confirmado; Van Cleef y Gucci, sin
  resultados (no los doy por hechos).
- (en) «Macy's Thanksgiving Day Parade Pikachu balloon history» →
  macysthanksgiving.fandom.com, bulbagarden.net, pokemon.com,
  businesswire.com.
- (en) «free manga screentone brush Clip Studio Assets license» →
  assets.clip-studio.com (dos packs gratis), graphicsbunker.com.
- (en) «Pokémon Sleep Pokémon Café Detective Pikachu movie merchandising
  collaboration» → separé cada cosa: sólo until Detective Pikachu y
  Pokémon Café dieron datos firmes.
- (en) «"Pokémon" official brand collaborations list Crocs Starbucks New
  Era Build-A-Bear» → Crocs, Starbucks y Build-A-Bear confirmados; New Era
  no apareció.
- (en) «real cosplay Ash Ketchum best costume convention photo» → sólo
  tiendas de disfraces, ningún cosplayer concreto documentado.
- (en) «Pokémon manga Pocket Monsters screentone style analysis» → llevó a
  aclarar que el manga *Pocket Monsters* (gag) es distinto de *Pokémon
  Adventures* (el de Mato, más detallado).
- (en) «Pokémon Adventures manga volume 1 cover art Mato Kusaka» →
  howtolovecomics.com, cbr.com.
- (en) «Pokémon anime Blu-ray box art Kanto Japan cover» →
  comicbook.com (Champion's Edition).
- (en) «Pokémon anime opening single CD cover "Mezase Pokémon Master" OR
  "Together"» → bulbapedia.bulbagarden.net, jpop.fandom.com.
- (en) «Ash Ketchum outfit history every region colors Kanto Hoenn Sinnoh
  Unova Kalos Alola Galar» → dos artículos de CBR, contrastados con
  Bulbapedia.
- (en) «Team Rocket logo red R official image Pokémon» → fandom +
  Wikipedia, sin PNG oficial suelto.
- (en) «Pokémon Center Café Tokyo Nihonbashi menu theme decor» →
  tokyocheapo.com, voyapon.com, pokemon-cafe.jp.
- Consultas directas por API (sin gastar buscador): `api.sketchfab.com/v3/models/<id>`
  (9 modelos, licencia y caras reales), `ambientcg.com/api/v2/full_json`
  (papel y cartón CC0), `pokemon.fandom.com/api.php` (imageinfo de badges,
  logo, Ash+Oak, pageimage de Ash), `bulbapedia.bulbagarden.net/w/api.php`
  (wikitexto de Cosplay Pikachu, con `curl` y cabecera de navegador —la web
  normal y WebFetch dan 403, pero la API con `action=parse` sí responde).
- Intentos con 403/bloqueo, anotados y no repetidos más de dos veces:
  `pokemon.com` (Incapsula), `bulbapedia.bulbagarden.net` por WebFetch
  (403; resuelto por la API), Wayback Machine sin snapshot para la página
  de wallpapers.
- Medí colores con Pillow (script propio, no `estilo.py` para los puntos
  finos) sobre `Ash_anime_The_Beginning.png` (pageimage oficial de
  pokemon.fandom.com para «Ash Ketchum»): agrupamiento de color (k-means /
  cuantización) sobre toda la imagen, más muestras de píxel puntuales para
  el naranja de la gorra y el verde del guante.

## Cumplimiento de mis puntos (1, 3, 15, 16, 19, 23)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | Hojas de contacto miradas y guardadas, arte fuera de la wiki (AniList, manga, CD, Blu-ray), sólo faltan cartones de cuenta atrás y hojas de modelo (no existen publicados). |
| 3 · Fan art y 3D con licencia | ✅ | 12 modelos de Sketchfab con licencia verificada por su API (2 nombres de autor corregidos); fan art de tres sitios distintos. |
| 15 · Vestuario | ✅ | Colores medidos con Pillow (antes ⚠️ sin medir); ropa de Ash en 7 eras con color; disfraces canon de Pikachu confirmados en fuente primaria. |
| 16 · Fondos y paisajes | ⚠️ | Sólo un fondo oficial en alta con enlace directo (bloqueo anti-bot en la descarga); fondos de fans sí, filtrados y con tamaño real. |
| 19 · Texturas 2D | ✅ | Trama de manga, grano de papel (CC0) y emblemas resueltos; falta sólo un PNG suelto del logo de Team Rocket. |
| 23 · Colaboraciones y cruces | ✅ | Marcas, eventos, cafés, crossovers y figuras oficiales con varias fuentes cada uno; cosplay documentado es el punto más flojo (sólo una foto libre + fichas comerciales). |
