# Imagen · Your Name: cielos y ciudades (Kimi no Na wa. / 君の名は。)

Investigador de imagen. Puntos 1, 3, 15, 16, 19 y 23 de `ENCARGO.md`.
Parte de `partes/datos-imagen.md` (no repite esas consultas). Formato: libreta de datos, un dato por línea.

**Aviso importante de identidad de la obra (comprobado 25-sep-2026):** el AniList ID 97962 usado por
`recolectar.py` en `datos-imagen.md` (portada, sinopsis) **NO es la película**: es
«Suntory Minami Alps no Tennen Mizu» (サントリー 南アルプスの天然水), un SPECIAL de 3 anuncios comerciales
de Suntory que usan a Taki y Mitsuha con fines publicitarios (confirmado con la API GraphQL de AniList:
`{Media(id:97962){title{romaji} format episodes}}` → `Suntory Minami Alps no Tennen Mizu`, formato
SPECIAL, 3 episodios). ✅ La portada `97962-3rBcawJt63sG.jpg` de `datos-imagen.md` **no se usa** en esta
parte por ese motivo. El AniList real de la película es **id 21519** («Kimi no Na wa.» / «Your Name.»,
MOVIE, 2016, 716942 popularidad, 43331 favoritos) — confirmado con
`{Media(id:21519){title{romaji english} format startDate{year}}}`. Esto coincide con la comprobación que
ya hizo el investigador de voz en `partes/voz.md` sobre Doblaje Wiki (misma película, sin mezcla con
«El jardín de las palabras» ni «Suzume»). Los datos de personajes (favoritos Mitsuha 4560 / Taki 2865,
IDs de personaje 121514/121516/121518/121520/121522/121524) sí coinciden entre `datos-imagen.md` y el
AniList 21519 correcto, así que esa parte de `datos-imagen.md` es reutilizable.

## Hallazgos

### Punto 1 — Arte oficial, en cantidad y variado

**Key visual / póster oficial** (el arte más repetido de la franquicia) — ✅ dos fuentes:
- Póster internacional: Mitsuha y Taki de espaldas, sentados en el cráter del lago Itomori al
  atardecer, mirando el cometa Tiamat partirse en dos sobre un Tokio en miniatura abajo. Cielo en
  degradado estrellado azul-violeta-naranja, la marca de composición de Makoto Shinkai (cielo real y
  ciudad diminuta en el mismo encuadre).
  - AniList (cover del ID correcto 21519): `https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx21519-SUo3ZQuCbYhJ.png`
    (460×690, medido) ✅
  - Póster oficial latino en Doblaje Wiki (mismo key visual, edición para México/LatAm):
    `https://static.wikia.nocookie.net/doblaje/images/3/3b/Your_Name.jpg` (2000×3000, medido, vía API
    `imageinfo`) ✅ — visto en detalle: logo «Your Name.» en tipografía manuscrita fina blanca sobre el
    cielo, créditos abajo en español latino.
  - Banner ancho (mismo arte, recorte panorámico): AniList
    `https://s4.anilist.co/file/anilistcdn/media/anime/banner/21519-1ayMXgNlmByb.jpg` (1900×400, medido) ✅
- **Paleta medida con `estilo.py`** sobre el key visual (`ref/anilist_cover.png`, 460×690):
  `#059BDB` 21% · `#074D9A` 21% · `#0472B7` 13% · `#E1E4E7` 10% · `#99C0DD` 8% (azul cielo degradado,
  predominante) y en el recorte panorámico (`anilist_banner.jpg`, 1900×400) tonos de atardecer:
  `#EDD9BF` · `#96808E` · `#392830` (naranja-rosado-violeta del horizonte). ✅ (medido, no de memoria).

**Hoja de contacto propia** (`herramientas/investigar_serie.py`, wiki `kiminonawa`, páginas Taki y
Mitsuha, 39 imágenes ≥500 000 px, guardada en `hojas/personajes_01.jpg`, 2400×1420, 560 KB):
- Nº 1 Mitsuha Miyamizu 2013 (retrato limpio, pelo largo, uniforme urbano) · Nº 2-3 grupo (Shinta,
  Taki, Tsukasa / Taki y Okudera en su cita) · Nº 4 Mitsuha gritando (shock del intercambio de cuerpos)
  · Nº 10 Mitsuha y Taki en Kataware-doki (atardecer, escena cumbre) · Nº 18 «Writing» (Taki escribiendo
  en su propia mano) · Nº 24-25 retratos cuadrados estilo icono (2022) · Nº 35 «Mitsuha comet» (ella
  mirando el cometa) · Nº 38 «Futaba Death» (madre de Mitsuha) · Nº 39 reencuentro final en la
  escalinata. ✅ (mirada en Read, 2400×1420, hoja completa).
- Fuente de cada imagen: `https://kiminonawa.fandom.com/wiki/Taki_Tachibana` y
  `.../wiki/Mitsuha_Miyamizu` (API `imageinfo`, anchos y altos medidos por la propia API, ya en
  `datos-imagen.md`). ✅

**Hojas de modelo (character design) encontradas fuera de lo que trajo el recolector** (búsqueda manual
en `allimages` de la wiki, prefijos `Itomori`, `Miyamizu`, `Suit`) — ✅ (API `imageinfo`, tamaño medido):
- `Itomori_High_MaleUni.png` (1432×2160) y `Itomori_High_FemaleUni.png` (1150×1990): hoja de modelo del
  **uniforme escolar de Itomori High** (chico y chica, frente y espalda), la referencia técnica más
  limpia de vestuario que hay en la wiki.
- `Itomori_High_SweaterUni.png` (1150×1990): variante de invierno con jersey.
- `Miyamizu_Attire.jpg` (1280×686), `Miyamizu_Gohei.jpg` (1280×697), `Miyamizu_Headdress.jpg`
  (1280×720): fotogramas del ritual sintoísta familiar (kimono blanco de miko, gohei ceremonial,
  tocado), vistos en Read — escena nocturna con luz de fuego/luna, tonos morados y ocres por la
  iluminación de la escena (no son los colores planos de la tela; ver punto 15 para el hex real de la
  tela con luz neutra).
- `Suit.png` (564×1800): Taki adulto de traje (epílogo, Tokio, años después).

**Portadas de productos físicos** — ✅:
- Póster/carátula de Blu-ray latino: el mismo key visual, en Doblaje Wiki (arriba). ⚠️ no encontré la
  carátula japonesa original de CoMix Wave/Toho en alta resolución medida desde aquí (ver «No encontré»).

**Aviso para el redactor**: la única portada de `datos-imagen.md` (AniList 97962) es del especial de
Suntory, no de la película — no usarla como «portada oficial de la serie», sólo como colaboración
comercial si aplica (ver punto 23).

### Punto 3 — Fan art y 3D como referencia (nunca para pegar)

**Fan art mejor valorado** (Safebooru, ya en `datos-imagen.md`, con autor/origen citado) — ✅:
- Taki y Mitsuha (post con ambas etiquetas), 1920×1080, 4 puntos:
  `https://safebooru.org/images/2646/ccd0c12e610fb75a070eb0391296fd19e6973414.jpg` · origen Pixiv
  `pixiv.net/artworks/63465513`. Visto en Read (`ref/fanart1.jpg`): ilustración genérica de los dos
  personajes, no es una pose «viva» específica de la película — sirve sólo como referencia de estilo de
  color de fans, no de pose.
- 3050×1617, origen Pixiv `86363633_p0`:
  `https://safebooru.org/images/3175/53a8b2b82888da86cebb3d6c408715423207402e.jpg` ⚠️ (no verifiqué
  autor exacto de Pixiv, sólo el ID de imagen).
- ⚠️ Aviso: el propio `datos-imagen.md` trae también fan art de Hatsune Miku, Cirno, Konpaku Youmu y
  Kancolle bajo la búsqueda de Danbooru `related_tag`/Safebooru — **no son de esta película**, es ruido
  del recolector automático (etiquetas compartidas o búsqueda mal acotada). No los uso.

**Modelos 3D con licencia libre** (Sketchfab, búsqueda directa por API, licencia en la respuesta) — ✅
no hay modelos del personaje o de objetos con marca de la película en sí (nombre «Kimi no Na wa» o
«Your Name» no da resultados en `search?type=models`), pero sí objetos genéricos del mismo tipo que los
del mundo de la película, todos con licencia CC declarada por el propio autor en Sketchfab:
- **Torii gate**, CC Attribution-NonCommercial-ShareAlike: `https://sketchfab.com/3d-models/none-c64d94871bc541a0a5b11d98b787b82e`
  — sirve para el santuario de Itomori/Suga Shrine.
- **Japanese Torii gate Game Asset**, CC Attribution: `https://sketchfab.com/3d-models/none-e12d2fa1b2b94928b8b87cb7787e2462`
- **Torii Gate** (otro autor), CC Attribution: `https://sketchfab.com/3d-models/none-9ae0d9df1ea44f2b922fa2f810e097ca`
- **Japanese Toro** (farol de piedra de santuario), CC Attribution: `https://sketchfab.com/3d-models/none-afe883adeab045348b7dc9a038975feb`
- **2020.215 Pair of Guardian Figures (Zuishin)**, CC0 Public Domain (licencia más permisiva, del Museo
  de Bellas Artes): `https://sketchfab.com/3d-models/none-cb74e1c1c6a64e7491e4e94ddb9acbbc`
- **太鼓橋 (Taikobashi, puente arqueado de santuario)**, CC Attribution: `https://sketchfab.com/3d-models/none-4d26f93c87174cc2ab9040faf949d605`
- **Nazo no eki (Mystery Station)**, estación de tren estilo japonés, CC Attribution:
  `https://sketchfab.com/3d-models/none-6cbd6ce6354f44a4b6517e8176d8741b`
- **Animated Ticket Gate** (torniquete de estación japonesa), CC Attribution:
  `https://sketchfab.com/3d-models/none-19a605237de941edbd9fe829ca0cfedf`
- ⚠️ No encontré un modelo 3D específico del **cometa Tiamat** con licencia libre (las búsquedas «comet»
  devuelven modelos genéricos no relacionados); para el cometa, mejor referencia = el propio key visual
  (punto 1) más un HDRI/skybox de estrellas genérico si se modela en Blender.

### Punto 15 — Vestuario, colores medidos, accesorios, «icónico»

**Uniforme de Itomori High School** (hoja de modelo de la wiki, `Itomori_High_MaleUni.png` 1432×2160 y
`Itomori_High_FemaleUni.png` 1150×1980, celdas 1 y 2 de `hojas/vestuario_fondos_01.jpg`, vistas en Read)
— ✅ (imagen oficial de la wiki + medido con Pillow, filtrando el fondo crema de la hoja):
- Chaqueta/blazer y detalle de corbata: **azul acero apagado `#40728B`** (color dominante no-fondo en
  ambas hojas de modelo, masculina y femenina — es el mismo tono en las dos, confirma que es el color
  corporativo del uniforme, no un error de medición). Detalle secundario verde grisáceo `#8CA39B`
  (corbata o vivo de cuello).
- Piel (referencia de tono, no ropa): `#F0B475` / `#F4B276` (medido en ambas hojas).
- Negro casi puro `#363533` / `#463D3E`: zapatos y líneas de contorno del uniforme, no la tela principal.
- Esto es **la ropa icónica que todos reconocen**: Mitsuha y Taki pasan casi toda la película en este
  uniforme (ella en Itomori, él en Tokio con un uniforme de corte similar); es la referencia obligatoria
  para no dibujarlos «de pie con ropa cualquiera», tal como pide `reglas_del_dueno.md`.
- Texto de la wiki (`datos-imagen.md`, ya citado): uniforme medio de Taki = camisa blanca + corbata
  verde + blazer amarillo pálido con cuello en V (versión de los 14 años); de adulto pasa a un traje de
  oficina (`Suit.png`, 564×1800, visto en el índice de hojas).

**Traje ceremonial de las sacerdotisas Miyamizu** (`Miyamizu_Attire.jpg`, `Miyamizu_Gohei.jpg` celda 3,
`Miyamizu_Headdress.jpg` celda 4 de `hojas/vestuario_fondos_01.jpg`, vistos en Read) — ✅ imagen oficial + ⚠️ color exacto de la tela (las 3
imágenes son de una escena nocturna con luz de fuego/luna, así que el hex medido es el de la escena
iluminada, no el de la tela en luz neutra de día — lo digo explícito para que el redactor no lo use como
«el color plano de la tela»):
- Es el **kimono blanco de miko (hakui) con hakama/detalles bermellón**, la vestimenta tradicional de
  sacerdotisa sintoísta japonesa (identificación visual directa en las 3 imágenes: tela blanca suelta,
  tocado ceremonial, gohei de papel blanco en zigzag). Bajo la luz nocturna de la escena, el blanco se
  ve `#F7F2C6` (crema cálido por la luz de fuego) y hay tonos morados `#9D7FA0` de la iluminación
  ambiental, no de la tela.
- **El cordón kumihimo rojo** (el accesorio-ancla del punto 12 de `voz.md` y del punto 1 de
  `reglas_del_dueno.md`): medido en `Mitsuha_Miyamizu_2013.png` (2640×2160, luz de día neutra, la
  imagen con mejor iluminación de las disponibles) → **`#A55849`**, un rojo terracota apagado (no rojo
  saturado de caricatura), coherente con la paleta general de Shinkai (colores de atardecer, nunca
  colores planos puros). ✅ (medido con Pillow, filtrando los tonos de piel que dominan la imagen).
- Peinado de Mitsuha con el cordón: media coleta alta con dos mechones trenzados (descrito en
  `datos-imagen.md`, texto de «Appearance» de la wiki, ya citado ahí) — el cordón atado en forma de lazo.
- Vestuario secundario confirmado por texto de la wiki (`datos-imagen.md`): Mitsuha pasa a un corte de
  pelo corto y ropa urbana moderna en la Tokio de después del cambio (`Mitsuha_with_short_hair.jpg`,
  1040×1040) — el «antes / después» es un cambio de vestuario reconocible para la lámina si se quiere
  mostrar su arco.

### Punto 16 — Fondos, ciudades, luz y hora del día

**Lugares reales que inspiraron la película** (Tofugu, artículo de peregrinación anime, y Snow Monkey
Resorts) — ✅ dos fuentes:
- **Escalinata de Suga Shrine** (Yotsuya, Tokio): la escena más icónica y más peregrinada por los fans
  (Taki y Mitsuha casi se cruzan y reconocen al final). Es EL fondo real más reconocible de la película.
  Fuentes: `https://www.tofugu.com/japan/your-name-locations/` y
  `https://animetrivia.app/articles/guide/anime-pilgrimage-in-japan-a-guide-to-seichi-junrei` (ambas lo
  nombran como el ejemplo más citado de «seichi junrei», peregrinación a lugares de anime). ✅
- **National Art Center, Roppongi** (interior con paredes de madera y mapas de cristal) y **Tokyo City
  View / Roppongi Hills**: escenario de la cita de Taki y Okudera-senpai. ✅ (Tofugu).
- **Yotsuya Station** (salida Akasaka) y el cruce con el Lawson 100 camino al santuario: fondos urbanos
  cotidianos de Tokio que aparecen en el clímax. ✅ (Tofugu).
- **Shinjuku**: pantalla gigante Yunika Vision (donde se ve la cobertura del cometa cayendo) y el cruce
  tras la comisaría con la Cocoon Tower de fondo. Es el Tokio más «de postal» de la película (luces de
  neón, multitud). ✅ (Tofugu).
- **Cafe La Bohème (Shinjuku Gyoen)**: inspiró el restaurante ficticio «Il Giardino delle Parole» donde
  trabajan Taki y Okudera. ✅ (Tofugu).
- **Itomori-chō es un pueblo ficticio**, inspirado en **Hida (Gifu)** y el **lago Suwa (Nagano)** —
  confirmado explícitamente por Tofugu; no existe como lugar real, así que no hay «fondo de pantalla
  real» de Itomori, sólo de sus referencias (Hida, lago Suwa). ✅
- Nota para el redactor: esto encaja con el punto 23 (turismo/peregrinación) y con «en qué fijarse
  especialmente: Tokio» que pide `encargos/101-your-name-cielos-y-ciudades.md`.

**Luz de Shinkai, medida en key visual y fondos** — ✅ (medido con `estilo.py`, no de memoria):
- Cielo diurno/atardecer del póster oficial (celda 5 de `hojas/vestuario_fondos_01.jpg`): `#059BDB` `#074D9A` `#0472B7`
  (azules de cielo en degradado) + `#E1E4E7` `#99C0DD` (nubes/luz alta). Saturación 74%, brillo 71% —
  colores intensos pero SIN negro puro en las sombras (marca de Shinkai: sombra con color, nunca gris
  neutro).
- Recorte panorámico del mismo arte (`anilist_banner.jpg`): tonos de atardecer `#EDD9BF` `#96808E`
  `#392830` (crema-rosado-violeta oscuro del horizonte).
- Cielo nocturno estrellado sobre Itomori (fondo de fans, Wallhaven `8oy372`, 3840×2160, celda 7 de
  `hojas/vestuario_fondos_01.jpg`, con las etiquetas propias `Kimi no Na Wa / night / night sky`, sin
  autor declarado — usar sólo como referencia, no como fuente oficial): `#283B50` `#4C6C92` `#19232A`
  `#3E5B7B` (azules de noche
  profundos, con un azul más claro `#4C6C92` que simula la Vía Láctea, la firma visual de las escenas
  nocturnas de pueblo de esta película). ✅ medido / ⚠️ fan art, no arte oficial de estudio.
- **Regla de estilo para la guía de IA** (observación directa de las imágenes, no de memoria): Shinkai
  nunca usa un cielo plano de un solo azul; siempre hay un degradado de al menos 3 tonos y nubes con
  volumen pintado (ver «sombreado degradado / pintado» que devuelve `estilo.py` en las 4 imágenes de
  cielo analizadas arriba, ninguna dio «plano»).

**Fondos de pantalla oficiales vs. de fans** — ⚠️: en `datos-imagen.md` la sección de Wallhaven quedó
vacía (el recolector no encontró resultados con su consulta); yo sí encontré resultados consultando la
API directa (arriba, `8oy372`). No encontré un banco de **fondos de pantalla oficiales** (los que
reparte CoMix Wave o Toho en su web) accesibles desde aquí — ver «No encontré».

### Punto 19 — Texturas 2D (tramas, grano, pinceles) y su licencia

- **Screentones/tramas de manga libres**: Clip Studio Assets tiene un pack gratuito oficial, «[FREE]
  Manga Screentone Pack 1» (`https://assets.clip-studio.com/en-us/detail?id=2142037`), gratis con cuenta
  de Clip Studio (no requiere pago). ✅
- **Colección libre alternativa** (uso declarado libre por el autor, fuera de Clip Studio): «Free Screen
  Tone Collection 1», usable en Krita/Procreate/Photoshop: `https://manga-with-stef.com/free-screen-tone-collection-1` ✅
- **Grano/degradados en punto** (DeviantArt, licencia de uso libre declarada por la autora en la
  descripción de la pieza): `https://www.deviantart.com/botanycameos/art/Free-resource-300dpi-Screentones-DOT-pack-398507125` ⚠️ (verificar los términos exactos de la licencia en la página antes de usar comercialmente).
- **Texturas reales equivalentes** (papel, madera — para el punto 4/19 combinados), todas CC0 en
  ambientCG (licencia estándar del sitio, sin atribución necesaria): `Paper001`, `Paper005`, `Paper006`
  (papel), `Wood051`, `Wood092`, `Wood094`, `Wood095` (madera de interiores tipo casa de campo de
  Itomori o el apartamento de Taki en Tokio), consultado en
  `https://ambientcg.com/api/v2/full_json?type=Material&q=Paper` y `...&q=Wood`. ✅
- Nota: no until encontré un banco de texturas pintadas a mano específicas del estilo CoMix Wave (su
  técnica real es render digital con post-proceso de grano de cámara, ver `partes/texto.md` para el
  punto 18 técnico completo); las texturas de arriba son la mejor aproximación libre.

### Punto 23 — Colaboraciones y cruces; figuras oficiales y cosplay

- **Colaboración comercial oficial confirmada**: Suntory (Minami Alps no Tennen Mizu), 3 anuncios
  animados cortos con Taki y Mitsuha bebiendo agua mineral Suntory, producidos también por CoMix Wave
  (AniList SPECIAL id 97962, confirmado arriba). Es la colaboración de marca más clara y documentada
  desde aquí. ✅ (dos fuentes: AniList y el propio catálogo de CoMix Wave que la lista como obra
  relacionada de la franquicia en `datos-texto.md`).
- **Turismo/peregrinación oficial**: «Anime Tourism Association», en colaboración con Kadokawa ASCII
  Research Lab, organizó un concurso para llevar 30 fans a las localizaciones reales de la película
  (Fandom Entertainment News). ✅ Es el fenómeno de «colaboración con el mundo real» más grande de esta
  película en concreto (a diferencia de otras series del encargo, no hay gacha ni Fortnite conocidos
  desde aquí). ⚠️ No until encontré colaboraciones tipo videojuego gacha, cafés temáticos oficiales o
  eventos tipo USJ para esta película — ver «No encontré».
- **Cosplay y fan art expuesto** (Openverse, licencia CC BY-NC-ND declarada por el fotógrafo en Flickr):
  varias fotos de arte de fans de «Kimi no Na wa.» expuesto en una convención (impresiones/pósters de
  fans en un panel de exhibición, no cosplay de persona real vistiendo el traje) —
  `https://live.staticflickr.com/5795/31429921955_847ef8c692_b.jpg` (727×1024, medido) y 7 fotos más de
  la misma serie de Flickr. ✅ (vista en Read, confirmado que es arte de fans expuesto, no cosplay).
  ⚠️ No until encontré fotos de **cosplay real** (persona vistiendo a Taki/Mitsuha) con licencia libre
  verificable desde Openverse — ver «No encontré».
- **Figuras oficiales**: no until encontré (desde las fuentes abiertas de este entorno) una ficha de
  figura oficial con foto y licencia clara; ver «No encontré».

## Lo mejor para la lámina

1. **El cordón kumihimo rojo** (`#A55849`, terracota apagado, medido) es el objeto-ancla perfecto: real,
   modelable en Blender (una trenza), y es el accesorio que el fandom reconoce al instante (coincide con
   `partes/voz.md`, punto 12).
2. **La escalinata de Suga Shrine** es el fondo real más reconocido de toda la película — si la lámina
   quiere «un sitio real de la serie», éste es el que un fan de verdad identifica al instante, más que
   cualquier interior genérico de Itomori (que ni siquiera es un lugar real).
3. **El uniforme de Itomori High** (azul acero `#40728B` + corbata verde grisácea `#8CA39B`) es la ropa
   icónica de ambos personajes casi toda la película — evita el error de «ropa genérica de calle» que
   señala `reglas_del_dueno.md`.
4. **El cielo degradado de 3+ tonos, nunca plano** (azul `#074D9A`→`#059BDB`→crema `#E1E4E7`, o de noche
   `#19232A`→`#283B50`→`#4C6C92`) es la marca visual más repetible de Shinkai para cualquier fondo de la
   lámina, con o sin personajes.
5. El **key visual del cometa Tiamat partiéndose sobre Tokio** (póster oficial) es la imagen más
   reconocible de la franquicia entera; sirve de referencia directa de composición (personajes pequeños
   de espaldas + cielo protagonista + ciudad diminuta abajo).

## No encontré

- **Carátula japonesa original** (CoMix Wave/Toho) del Blu-ray en alta resolución medida: sólo confirmé
  la edición latina (Doblaje Wiki, 2000×3000). Búsquedas: no repetí consultas de imagen fuera de las
  fuentes ya abiertas (Fandom, AniList, Doblaje Wiki, Wallhaven, Sketchfab, Openverse, ambientCG) para
  no gastar cupo de buscador en algo de bajo impacto para la lámina.
- **Modelo 3D con licencia libre del cometa Tiamat** específico, o de la casa/pueblo de Itomori: las
  búsquedas en Sketchfab (`comet`, `Itomori shrine`) no dieron nada específico de la obra: sólo genéricos
  de cometas/cráteres sin relación, o vacío. Alternativa anotada arriba (HDRI de estrellas + key visual
  como referencia).
- **Colaboraciones tipo gacha/videojuego, cafés temáticos oficiales o evento tipo USJ**: búsquedas en
  japonés («君の名は コラボ 2024 2025 グッズ 展覧会») y en inglés («Your Name collaboration merchandise
  JR East») no dieron una colaboración comercial reciente más allá de Suntory (2016) y el fenómeno de
  turismo/peregrinación. Puede que exista y no la haya encontrado con las fuentes abiertas desde aquí;
  no afirmo que no exista, sólo que no la hallé.
- **Fotos de cosplay real** (persona, no arte impreso) con licencia libre verificable: Openverse sólo
  devolvió fan art expuesto en convención, no cosplay.
- **Ficha de figura oficial** (Good Smile Company u otro fabricante) con foto y licencia: no busqué en
  MyFigureCollection ni en la tienda directa por no tener acceso confirmado desde aquí en esta tanda;
  si el redactor lo necesita, se puede pedir como ampliación.
- **Wallhaven con fondos "sólo aptos" filtrados por resolución exacta ≥1920×1080 de la consulta original
  de `datos-imagen.md`**: esa sección quedó vacía en el recolector automático (fallo de consulta, no de
  la API); yo sí conseguí resultados con una consulta distinta (`q=kimi no na wa`, arriba).

## Bitácora

- Español: «Kimi no Na wa coraboración góza tenrankai» (sin resultado útil, ver búsqueda en japonés
  abajo, mejor resultado).
- Japonés: `君の名は コラボ 2024 2025 グッズ 展覧会` (sin colaboración reciente encontrada).
- Inglés: «Your Name Kimi no Na wa official collaboration merchandise Suica JR East real locations
  tourism pilgrimage» (dio el hallazgo clave de Suga Shrine y el Anime Tourism Project) y «Kimi no Na wa
  Your Name collaboration JR East station stamp rally official art» (sin resultado, no hay stamp rally
  de esta película).
- Consultas directas a API (no buscador, no gastan cupo):
  - AniList GraphQL (`graphql.anilist.co`): `Media(id:97962)` para confirmar que es el especial de
    Suntory, `Media(search:"Kimi no Na wa", type:ANIME, format:MOVIE)` para hallar el ID real (21519),
    y `Media(id:21519){bannerImage coverImage characters studios}` para portada, banner y personajes.
  - Fandom API `kiminonawa.fandom.com/api.php`: `list=allimages` con varios prefijos (`Mitsuha`,
    `Shrine`, `Itomori`, `Uniform`, `Suit`, `Miyamizu`, `Kumihimo`) para hallar las hojas de modelo de
    vestuario que el recolector automático no trajo; `list=search&srwhat=text` para «collaboration»,
    «exhibition», «merchandise» (sin resultado).
  - Doblaje Wiki API: `list=allimages&aiprefix=Your` para hallar el póster latino oficial
    (`Your_Name.jpg`), y `prop=imageinfo` para medir su tamaño real (2000×3000).
  - Wallhaven API (`wallhaven.cc/api/v1/search`): `q=kimi no na wa` para fondos de pantalla, y
    `/api/v1/w/<id>` para confirmar licencia/tags de uno de ellos.
  - Sketchfab API (`api.sketchfab.com/v3/search`): `q=<término>&downloadable=true` con «your name kimi
    no na wa» (vacío), «comet», «torii gate», «japanese train station», «shinto shrine», «kumihimo
    braid cord» (vacío) para modelos 3D con licencia.
  - Openverse API (`api.openverse.org/v1/images`): `q=Kimi no Na wa cosplay` para fotos con licencia
    libre.
  - ambientCG API (`ambientcg.com/api/v2/full_json`): `type=Material&q=Wood|Paper|Fabric` para
    texturas CC0.
  - `herramientas/investigar_serie.py --serie "Your Name: cielos y ciudades" --wiki kiminonawa --paginas
    "Taki Tachibana" "Mitsuha Miyamizu"`: hoja de contacto de 39 imágenes (guardada en `hojas/`).
  - `herramientas/estilo.py` sobre 8 imágenes (key visual, banner, wallpaper, hojas de modelo de
    vestuario) para paletas y tipo de sombreado.
  - Pillow directo (Python) para medir hex de zonas específicas de vestuario, filtrando el color de
    fondo de las hojas de modelo, cuando `estilo.py` (que promedia toda la imagen) no aislaba bien la
    tela del fondo crema de la hoja.

Sigue: falta completar `imagen.json` con las referencias medidas (portada real AniList 21519, póster
latino, hojas de modelo de vestuario, wallpaper, modelos Sketchfab, texturas ambientCG, fan art
Safebooru/Openverse ya citados arriba) y la tabla de «Cumplimiento del encargo» de esta parte contra los
puntos 1, 3, 15, 16, 19 y 23 (las 2 hojas de contacto, `personajes_01.jpg` y `vestuario_fondos_01.jpg`,
ya están listas en `hojas/`, ambas <3 MB).

