# Parte de IMAGEN · Generator Rex (105)

Investigador de imagen. Puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md. Libreta de datos, no prosa.
`datos-imagen.md` de recolectar.py salió casi todo inútil: mezcló a Rex con personajes de Teen Titans,
Adventure Time y Powerpuff Girls (búsqueda genérica «rex» sin wiki fijada) y el Sketchfab/Openverse
salió por coincidencia de la palabra «rex» (T-Rex, OSIRIS-REx, Stephen King). Sólo se aprovecha lo de
`rex_salazar` en Danbooru/Safebooru; el resto se descarta y se repite bien en esta parte.

Wiki real: `generatorrex.fandom.com` (imágenes alojadas en `static.wikia.nocookie.net/generatorrexpedia/`).

## 1 · Arte oficial, en cantidad y variado

Hojas de contacto con `investigar_serie.py --wiki generatorrex --min-px 90000` sobre Rex Salazar, Agent Six,
Bobo Haha, Providence, Van Kleiss, Breach, White Knight, Rex Salazar's machines, Nanites, Circe, Noah Nixon
y Rebecca Holiday: 121 imágenes enlazadas, 113 grandes, 3 hojas (en `hojas/`). Miradas fotograma a fotograma.

- Retrato oficial de infobox de Rex Salazar (chaqueta roja, camiseta verde oscuro, goggles naranjas en la cabeza) · https://static.wikia.nocookie.net/generatorrexpedia/images/e/e5/Rex_Salazar.png · ✅ (wiki + usado en cientos de fan pages) · 333×250
- Arte de personaje de Agent Six (traje verde oscuro, gafas de sol, katanas a la espalda) · https://static.wikia.nocookie.net/generatorrexpedia/images/9/94/Agent_Six.png · ✅ · 333×250
- Arte de personaje de Bobo Haha (mono con chaleco caqui y arnés, cresta roja) · https://static.wikia.nocookie.net/generatorrexpedia/images/9/97/Bobo.png · ✅ · 333×250
- Arte de personaje de Van Kleiss (abrigo/capa negra con hombreras y cuello oliva) · https://static.wikia.nocookie.net/generatorrexpedia/images/d/d6/Van_Kleiss.png · ✅ · 333×250
- Arte de personaje de White Knight (abrigo blanco largo, cuello de tortuga negro) · https://static.wikia.nocookie.net/generatorrexpedia/images/9/92/White_Knight.png · ✅ · 333×250
- Arte de personaje de Circe (peto rojo sobre top gris, botas y guantes tostados) · https://static.wikia.nocookie.net/generatorrexpedia/images/7/75/Circe.png · ✅ · 333×250
- Certificado/diploma de Providence con sello institucional (prop oficial, útil para tipografía de mundo) · https://static.wikia.nocookie.net/generatorrexpedia/images/7/7a/Providence_Certificate.jpg · ✅ (hoja 1 nº3) · 1208×920
- «Rex Build Omnitrix.webp», arte promocional del crossover Ben 10/Generator Rex: Heroes United (Rex con un Omnitrix) · https://static.wikia.nocookie.net/generatorrexpedia/images/e/e4/Rex_Build_Omnitrix.webp · ✅ (hoja 1 nº2, se ve el hilo de Twitter de Duncan Rouleau -co-creador- confirmando que era técnicamente posible) · 1125×1377
- Fotograma de Rex en su forma EVO completa/Omega-1 (transformación de cuerpo entero, textura dorada-armadura) · https://static.wikia.nocookie.net/generatorrexpedia/images/...(320-Full_Omega-1_form.png, hoja 1 nº30) · ⚠️ (una sola fuente, wiki) · 511×288

- Portada oficial del DVD «Generator Rex, Volume 1» (primer lanzamiento en DVD, 19-oct-2010, EE.UU.), arte de
  key visual con Rex en pose de acción y logo del show · Generator Rex Wiki · https://static.wikia.nocookie.net/generatorrexpedia/images/8/8a/Generator_Rex_volume_1.jpg · ✅ (wiki + 90sdvds.com y cinematerial.com listan la
  misma caja) · 455×500
- Índice con ~17 variantes de pósters/carátulas de TV de distintos países (incluida una portada de DVD rusa) ·
  CinemaMaterial · https://www.cinematerial.com/tv/generator-rex-i1636691 · ⚠️ (índice, no se abrió cada variante
  una por una; el redactor puede elegir la que más sirva)
- Anuncio impreso promocional de Cartoon Network en formato página de cómic (2010), estilo de línea y color
  oficial fuera de la wiki · eBay (venta de coleccionismo, la imagen del anuncio es la fuente) ·
  https://www.ebay.com/itm/156490284583 · ⚠️ (una sola fuente, listado comercial)

Sigue en «Bitácora» las búsquedas de arte fuera de wiki (portadas DVD/Blu-ray, artbook) que no dieron nada verificable en la red abierta de este contenedor.

## 15 · Vestuario, colores medidos

Hex medidos con Pillow (recorte de zona de tela, sin bordes de línea) sobre el arte oficial de personaje de la wiki citado en el punto 1. Método en la Bitácora.

Personaje | Prenda | Hex medido | De qué imagen
---|---|---|---
Rex Salazar | Chaqueta/chamarra (roja, su prenda icónica) | #A04D47 | Rex_Salazar.png (retrato infobox, wiki)
Rex Salazar | Camiseta interior (verde oscuro grisáceo) | #394B45 | Rex_Salazar.png (retrato infobox, wiki)
Agent Six | Traje (verde botella oscuro) | #3F4C43 | Agent_Six.png (dominante, estilo.py)
Agent Six | Corbata (negra) | #3F3F3F | Agent_Six.png
Bobo Haha | Chaleco/arnés (caqui claro) | #838370 | Bobo.png (retrato infobox)
Bobo Haha | Franja central del arnés (turquesa apagado) | #495D68 | Bobo.png
Van Kleiss | Capa/abrigo (negro) | #140D07 | Van_Kleiss.png
Van Kleiss | Cuello y hombreras (oliva-mostaza) | #736B58 | Van_Kleiss.png
White Knight | Abrigo largo (blanco roto) | #E5E5E4 | White_Knight.png
White Knight | Cuello alto/corbata (negro puro) | #050504 | White_Knight.png (medido en píxel de la sombra del cuello, no en zona con luz)
Circe | Peto/overol (rojo oscuro, en sombra de calle) | #56262A | Circe.png
Circe | Top interior (gris azulado) | #838694 | Circe.png
Circe | Guantes/botas (tostado) | #554E43 | Circe.png

Nota: son capturas de wiki en baja resolución (333×250), colores «planos» del cel-shading de la serie sin degradado
fuerte; el hex es representativo del tono base de cada prenda, no un Pantone exacto.

**Descripción oficial completa de Rex** (ficha «Physical appearance» de la wiki, en inglés, traducida): piel
morena, pelo negro liso hacia atrás y levemente puntiagudo, ojos cafés. Chamarra roja-naranja con estampado.
Camiseta de dos colores: mitad de arriba azul-verdoso (coincide con el hex medido #394B45, la wiki la llama
«blue»), mitad de abajo **blanca** (visible bajo la chamarra en varios fotogramas, p. ej. hoja 1 nº8 y nº24).
Pantalón negro con patrones geométricos azules que brillan cuando usa sus poderes. Guantes azules con puños
naranjas. Zapatos azul-negro. Goggles de lente naranja, normalmente sobre la cabeza, no puestos · Generator Rex
Wiki (texto de la ficha) + medición propia con Pillow (coincide en el tono de la mitad de arriba) · ✅ · —

**Peinado y accesorios de los demás** (de las mismas fichas, en inglés): Agent Six, pelo castaño oscuro corto,
katanas a la espalda (su arma, no accesorio de moda) · Bobo Haha es un chimpancé EVO (no un mono cualquiera:
ficha oficial dice «Chimpanzee EVO»), pelo/pelaje castaño, cresta roja en la cabeza, pistolas láser gemelas ·
Circe tiene el pelo negro con mechas rojas (antes fue negro con morado, cambia tras un arco de la temporada 2) ·
✅ (fichas de infobox de la wiki, dato estructurado, no prosa de fan) · —

**Por temporada**: la chamarra roja de Rex es su «uniforme» icónico y se repite igual en capturas numeradas de
las 3 temporadas (101, 115, 201, 209, 219, 316, 319, 320 en los nombres de archivo de la wiki); no cambia de
color entre arcos. Sí tiene trajes especiales puntuales para misiones (traje sigiloso oscuro en «Rex in a
stealth suit.png», hoja 1 nº45) y White Knight tiene un «White Knight Battle Suit» distinto a su abrigo normal
(hoja 3 nº108-109) · ✅ (visto en las hojas de contacto, capturas de episodios repartidos en toda la serie) · —

## 3 · Fan art (referencia) y modelos 3D con licencia libre

Fan art real de `rex_salazar` en Safebooru (tag `generator_rex`), 15 resultados; se descartan los de personajes
que no son de esta serie que trajo `datos-imagen.md` (Raven, Robin, Starfire, Marceline, Bonnibel, Buttercup:
ruido del recolector, no son Generator Rex).

- Rex con alas mecánicas y espada, pose de acción, alta resolución · x.com/LuisGangMD · https://safebooru.org/images/75/788570e88ab6810e442e2f7e6a71c283bcac954a.jpg · ✅ (Safebooru + fuente original en X) · 1603×2048
- Crossover fan art Rex + Ben Tennyson (animification, varios estilos) · x.com/Zero_zoner · https://safebooru.org/images/1344/15544a796f788687b55a99aad28ba1e1bcbe809f.jpg · ⚠️ · 850×1100
- Rex con cañón de brazo (Slam Cannon), estilo fiel al show · Pixiv (id 23327...) · https://safebooru.org/images/1053/7eaae138d28344ab973a773993184864a7d53cfc.jpg · ⚠️ · 1143×1210
- Rex EVO/lucha (gyosone), muy detallado, estilo semirrealista · Pixiv, 2022 · https://safebooru.org/images/4619/a1c1bd448c9d0def94e3c9a2596cc5c92223e453.png · ✅ (en datos-imagen.md y Safebooru) · 3050×1951
- Rex ojos brillantes/glow, fan art oscuro y dramático · twitter.com/_obarii · https://safebooru.org/images/4619/bd90c8a4f95681f298f48854efb05c4c7cd6b0bb.jpg · ⚠️ · 2753×3540 (candidato a fondo de pantalla por tamaño)
- Rex de espaldas, chamarra verde alterna, fan art de pose dinámica · timothypan (DeviantArt) · https://safebooru.org/images/2372/c993e153e4d5bf99019db3ea71071f0707e14ca9.png · ⚠️ · 600×900
- Crossover Ben 10/Generator Rex «Heroes United», Rex y Ben espalda con espalda · timothypan (DeviantArt) · https://safebooru.org/images/2372/8982f9bccc8c518a40b1b8bf6cf53a71b58a9036.png · ⚠️ · 1200×900
- Crossover Ben 10 Omniverse + Generator Rex, ambos personajes juntos · steveahn (DeviantArt) · https://safebooru.org/images/2107/ac9ab22fec18b551b7ccbe851f5993751bdd9389.jpg · ⚠️ · 1024×576
- Vocabulario de tags que más se repite al dibujar a Rex solo (Danbooru related_tag): shirt, black_hair, jacket, white_shirt (fan-error: en el show es verde, no blanco), full_body, open_clothes, spiked_hair, red_jacket, goggles, blue_pants, orange_goggles, mechanical_arms, huge_weapon, dark_skin · https://danbooru.donmai.us/related_tag?query=rex_salazar · ✅ (recolectado y comprobado contra el arte oficial) · —

**Modelos 3D con licencia libre (Sketchfab, todos CC Attribution y descargables), centrados en nanitos y máquinas de Rex:**

- «The Meta-Nanites | Generator Rex» (FBX) · GeneratedSentience · CC Attribution · 29 164 caras · https://sketchfab.com/3d-models/the-meta-nanites-generator-rex-fbx-96c7ebeae4984f1795bfc03566b0c994 · ✅ (aparece también en búsqueda web) · miniatura 64×36
- «The Meta-Nanites | Generator Rex» (STL, para imprimir) · GeneratedSentience · CC Attribution · https://sketchfab.com/3d-models/none-27fcb1daca6248fd8e880e211405ad3b · ✅
- «Standard Nanite | Generator Rex» · GeneratedSentience · CC Attribution · 2 882 caras · https://sketchfab.com/3d-models/standard-nanite-generator-rex-dfce4adcfab3413dad270e0ec6b54cd9 · ✅
- «The Omega-1 Nanite from Generator Rex» · GeneratedSentience · CC Attribution · https://sketchfab.com/3d-models/none-e113a940c5a9445e8364145f8202dc13 · ⚠️
- «Rex's Nanites» · DigiWiz · CC Attribution · 4 752 caras · https://sketchfab.com/3d-models/rexs-nanites-fcb18f29fade4093a12220f65d71e361 · ⚠️
- «Rex Salazarpunkbusters» (el build Punk Busters de Rex) · StevenS1 · CC Attribution · 17 574 caras · https://sketchfab.com/3d-models/rex-salazarpunkbusters-2ced5b0c57a84131b1ad20fca7999e38 · ✅ · miniatura 1024×576
- «Generator Rex Flying jetpack high quality» (su Boogie Pack) · K_I_R_A · CC Attribution · 8 450 caras · https://sketchfab.com/3d-models/generator-rex-flying-jetpack-high-quality-c0a4918e586b440f830153665bc7d7f2 · ✅
- «No Machines Rex Salazar» (Rex sin sus builds, sólo el personaje) · Mateusz.Krupa · CC Attribution · 5 900 caras · https://sketchfab.com/3d-models/no-machines-rex-salazar-7e85161474cd40c293c2e8264d6338ac · ✅
- «Biowulf (generator rex)» (EVO villano, forma de lobo) · luh842011 · a comprobar licencia exacta en la ficha (aparece en búsqueda como descargable) · https://sketchfab.com/3d-models/biowulf-generator-rex-c07d5bc8bfa64fd6bc8ab8cd2fed4d8f · ⚠️
- Colección «Generator Rex» de Natsu (@gochusuper), varios modelos agrupados · https://sketchfab.com/gochusuper/collections/generator-rex-14e4f576759440d7b446874f1771501e · ⚠️ (no se abrió cada modelo suelto)

No se encontró nada específico de Generator Rex en Poly Haven (es un banco genérico de HDRIs/materiales
fotorrealistas, sin contenido de fan de series); sus texturas metálicas sirven para el punto 19 (más abajo), no
como «modelo con licencia de la serie».

## 16 · Fondos de pantalla (ciudades, paisajes; oficiales y de fans en alta)

Wallhaven no tiene nada con «Generator Rex» (0 resultados, `wallhaven.cc/api/v1/search?q=Generator Rex`): es una
serie de 2010-2013 con poco fandom de wallpapers ahí. Se encontró en su lugar:

- Imagen promocional oficial 1920×1080 del especial crossover «Ben 10/Generator Rex: Heroes United» (Rex y Ben
  Tennyson juntos, fondo de acción) · Generator Rex Wiki · https://static.wikia.nocookie.net/generatorrexpedia/images/4/4a/GenRexBen10.jpeg · ✅ (usada como imagen de la ficha del episodio) · 1920×1080 — sirve directo como wallpaper o fondo de lámina
- Fan art de Rex a toda plantilla, 2753×3540, fondo oscuro dramático (candidato a wallpaper vertical/story) ·
  twitter.com/_obarii · https://safebooru.org/images/4619/bd90c8a4f95681f298f48854efb05c4c7cd6b0bb.jpg · ⚠️ · 2753×3540
- Fan art de Rex en pelea, 3050×1951, buena resolución horizontal · Pixiv 2022 · https://safebooru.org/images/4619/a1c1bd448c9d0def94e3c9a2596cc5c92223e453.png · ✅ · 3050×1951
- Bancos de wallpapers de terceros con colecciones dedicadas a la serie (no medidos uno a uno, hay que elegir
  dentro): Alpha Coders («Generator Rex» ~1113 fondos) https://alphacoders.com/generator-rex ; WallpaperAccess
  https://wallpaperaccess.com/generator-rex ; Wallpaper Flare https://www.wallpaperflare.com/search?wallpaper=generator+rex
  · ⚠️ (páginas índice, no una imagen concreta medida; el redactor o quien monte la lámina debería abrir la que
  más le sirva y medirla)

No encontré fondos de pantalla **oficiales** de estudio (Cartoon Network nunca publicó un pack de wallpapers
dedicado, a diferencia de series más recientes); lo mejor es el fotograma 1920×1080 del crossover y el fan art
grande de Pixiv/X.

## 19 · Texturas 2D (tramas, grano, patrones, emblemas; con licencia)

Generator Rex es cel-shading plano occidental, sin tramas de manga; el punto se adapta a lo que sí tiene: patrón
de nanites (puntitos azules brillantes), textura metálica de los builds, tela caqui del equipo de Providence, y
el logo/emblema de Providence. Texturas equivalentes libres (todas CC0, ambientcg):

- Metal cepillado (para los builds mecánicos de Rex y los EVOs metálicos) · «Metal055A» · CC0 · https://ambientcg.com/view?id=Metal055A · ✅ (catálogo verificado) · hasta 8K, aquí citado a 2048×2048 (tamaño estándar de descarga)
- Acero corrugado (para la arquitectura industrial de Providence/laboratorios) · «CorrugatedSteel009» · CC0 · https://ambientcg.com/view?id=CorrugatedSteel009 · ✅ · 2048×2048
- Tela de lona/algodón caqui (para el chaleco de Bobo Haha y los uniformes de Providence) · «Fabric066» · CC0 · https://ambientcg.com/view?id=Fabric066 · ✅ · 2048×2048
- Grano de papel (para viñetas del cómic digital tie-in) · «Paper006» · CC0 · https://ambientcg.com/view?id=Paper006 · ✅ · 2048×2048
- Pinceles de trama/halftone gratis para Photoshop (puntos de cómic, útiles para las viñetas de Cartoon Network
  Action Pack) · Brusheezy, «Mabecman's Screentones» (34 pinceles, gratis, licencia de uso libre con crédito) ·
  https://www.brusheezy.com/brushes/50379-mabecman-s-screentones-halftone-brushes · ⚠️ (verificar la licencia
  exacta del autor al bajar, Brusheezy mezcla free/premium) · —

**Cómics oficiales tie-in** (existen, y traen su propio estilo de línea plana con relleno digital, no trama de
imprenta): la revista digital *Cartoon Network Action Pack* publicó episodios cortos de Generator Rex, p. ej.
«Wood for the Trees» (№67), «Extra baggage» (№51), «A Blank Canvas» (№56), «Heart of Stone» (№54) · Generator
Rex Wiki, listado de cómics · ⚠️ (confirmado que existen por la wiki; no se abrió cada número para ver el arte
interior, sólo los títulos)

## 23 · Colaboraciones y cruces

- **Crossover oficial de TV**: «Ben 10/Generator Rex: Heroes United» (estrenado en NYCC el 16-oct-2011, emisión
  en Cartoon Network el 25-nov-2011), episodio doble (T3, ep. 11-12), Rex se junta con Ben Tennyson de *Ben 10:
  Ultimate Alien* · Generator Rex Wiki (wikitext del episodio) · ✅ (ficha del episodio + imagen promocional
  1920×1080) · imagen: https://static.wikia.nocookie.net/generatorrexpedia/images/4/4a/GenRexBen10.jpeg
- **Crossover en videojuego navegador**: Rex es un «Battler» jugable en el juego de Cartoon Network «Titanic
  Kungfubot Offensive» (TKO), con sus movimientos Smack Hands, Slam Cannon y su super Big Fat Sword (B.F.S.) ·
  Generator Rex Wiki (ficha del personaje en el juego) · ✅ · imagen 174×252: https://static.wikia.nocookie.net/generatorrexpedia/images/7/7f/Tko_charrex_174x252.png
- **Figuras oficiales**: línea de juguetes Mattel 2010, figuras básicas de 4" (Rex, Agent Six, Van Kleiss,
  Providence Agent, Punk Busters, Battle Saw, Twin Blaster Boogie Pack), venían con un «mini-EVO» · Generator
  Rex Wiki «Generator Rex toy line» + amoktime.com (fichas individuales por figura) · ✅ (dos fuentes
  independientes) · foto de la línea: https://static.wikia.nocookie.net/generatorrexpedia/images/1/12/Generator_rex_toy_line.jpg (200×160, baja resolución, es foto de producto de catálogo)
- Hubo también **juguetes cancelados** nunca puestos a la venta (galería «Canceled Generator Rex Toys» en la
  wiki, 8 imágenes) · Generator Rex Wiki · ⚠️ (una sola fuente, no se abrió cada imagen)
- **Cosplay**: guía de construcción del disfraz de Rex Salazar (chamarra roja con detalle dorado tipo moto,
  pantalón negro con líneas geométricas azules que en el show brillan al usar sus poderes; sugiere pintura que
  brilla en la oscuridad para replicar el efecto) · Carbon Costume · https://carboncostume.com/rex-salazar-from-generator-rex/ · ✅ (coincide con el hex medido en el punto 15) · —; también listados de cosplay en Cosplay.com (https://cosplay.com/character/rex-salazar) y disfraces/pelucas a la venta en CosplayFU · ⚠️ (páginas de catálogo, no fotos concretas de cosplay verificadas)
- No encontré colaboraciones con marcas externas (cafés temáticos, eventos, gachas, Fortnite): es una serie de
  2010-2013 sin ese tipo de merchandising posterior; búsquedas «Generator Rex x Fortnite», «Generator Rex café»,
  «Generator Rex gacha collab» sin resultados relevantes.


## Lo mejor para la lámina

- El retrato oficial de Rex Salazar (chaqueta roja #A04D47 + camiseta verde #394B45 + goggles naranjas) es la
  referencia de vestuario más segura: aparece igual en episodios, en el DVD y en el toy line.
- La imagen promocional 1920×1080 del crossover «Heroes United» ya viene en resolución de lámina (1200×800 cabe
  de sobra) y muestra a Rex en pose de acción, no de pie estático.
- Los modelos 3D CC Attribution de los nanites (Meta-Nanites, Standard Nanite) son el material más fiel al
  «fijarse especialmente en nanitos» que pide el encargo: se pueden renderizar en Blender con textura metálica
  de ambientcg encima.
- El build Punk Busters (guantes-cañón de Rex) en 3D descargable sirve para una pose «con su arma/objeto», la
  queja explícita del dueño sobre láminas «de pie con una ropa».
- El certificado de Providence (1208×920) da tipografía y grafismo institucional real para cualquier prop de
  fondo (diploma, carné, pantalla de interfaz) sin inventar nada.

## No encontré

- Wallpapers oficiales dedicados (pack de fondos de pantalla del estudio): no existen para esta serie de
  2010-2013; búsqueda `wallhaven.cc/api/v1/search?q=Generator Rex` → 0 resultados. Lo más parecido son fan arts
  grandes de Pixiv/X y la imagen promo del crossover.
- Colaboraciones con marcas externas o eventos (cafés temáticos, Fortnite, gachas): búsquedas web «Generator Rex
  x Fortnite», «Generator Rex café temático», «Generator Rex gacha collab» sin resultados relevantes; es
  esperable en una serie sin esa clase de merchandising posterior.
- Poly Haven no tiene nada específico de la serie (es un banco genérico); se cubrió el hueco con ambientcg (CC0)
  para las texturas del punto 19.
- No se abrió cada número de los cómics digitales «Cartoon Network Action Pack» para ver su arte interior línea
  por línea (⚠️ sólo se confirmaron los títulos existentes en la wiki); quien monte la lámina puede profundizar
  ahí si necesita más referencias de cómic.
- Licencia exacta del modelo «Biowulf (generator rex)» de Sketchfab: aparece como descargable en la búsqueda
  pero no se abrió su ficha individual para confirmar el tipo de CC.

## Bitácora

- Wiki de Fandom: `generatorrex.fandom.com` (imágenes en `static.wikia.nocookie.net/generatorrexpedia/`),
  confirmada por búsqueda en `api.php?action=query&list=search`. `datos-imagen.md` no traía wiki (el encargo no
  la fijó); se buscó a mano.
- `investigar_serie.py --wiki generatorrex --min-px 90000 --paginas "Rex Salazar" "Agent Six" "Bobo Haha"
  "Providence" "Van Kleiss" "Breach" "White Knight" "Rex Salazar's machines" "Nanites" "Circe" "Noah Nixon"
  "Rebecca Holiday"` → 121 imágenes enlazadas, 113 grandes, 3 hojas de contacto (en español: se subieron a
  `hojas/` como `personajes_01.jpg`, `personajes_02.jpg`, `maquinas_01.jpg`).
- Colores: recorte con Pillow de zonas de tela limpias (sin borde de línea) sobre el retrato oficial de cada
  personaje en la wiki; verificado visualmente con recortes ampliados antes de medir (ver método en el punto 15).
- Danbooru `related_tag` y Safebooru API (`tags=generator_rex`) en inglés, para fan art y vocabulario de tags.
- Sketchfab API (`api.sketchfab.com/v3/search?type=models&q=...&downloadable=true`) en inglés, varias consultas:
  «generator rex», «generator rex nanite», «generator rex jetpack», «rex salazar», «biowulf generator rex»,
  «Meta-Nanites». Se comprobó licencia y nº de caras de cada modelo elegido con `api.sketchfab.com/v3/models/<id>`.
- ambientcg API (`ambientcg.com/api/v2/full_json`) para texturas CC0: Metal, Fabric, Paper.
- Búsquedas web (WebSearch, en inglés): «Generator Rex wallpaper 1920x1080», «Generator Rex Sketchfab 3D model
  download», «Generator Rex action figure Mattel 2010», «Generator Rex cosplay Rex Salazar costume», «Generator
  Rex DVD cover complete series poster key art», «circuit board pattern seamless texture CC0», «free halftone
  dot pattern brushes Photoshop CC0 comic screentone». 7 búsquedas usadas del cupo de ~50.
- `datos-imagen.md` (recolectar.py) revisado primero: casi todo su contenido (Danbooru/Safebooru de Raven,
  Robin, Starfire, Marceline, Bonnibel, Buttercup; Sketchfab de terrenos/SciFi genérico; Openverse de dinosaurios
  y NASA OSIRIS-REx) es ruido de una búsqueda genérica por la palabra «rex» sin wiki fijada; se descartó y se
  investigó todo de nuevo con la wiki correcta. Sólo se aprovechó el bloque de `rex_salazar` en Danbooru y
  Safebooru, que sí es de esta serie.
