# Parte IMAGEN · 33-frieren (repaso: puntos 19 y 23 de ENCARGO.md)

La biblia ya tiene los puntos 1, 3, 15 y 16 (arte oficial, fan art/3D,
vestuario, fondos) hechos y con ✅ en su tabla de cumplimiento. Esta parte
sólo aporta lo que falta: **punto 19 (texturas 2D)** y **punto 23
(colaboraciones y cruces)**, que no estaban en la biblia. Parto de
`partes/datos-imagen.md` (no repito esas consultas) y de
`herramientas/seccion.py 33-frieren --indice`.

## Hallazgos

### Punto 19 · Texturas 2D

**19.1 Tramas del manga (screentone), vistas de verdad, no de memoria**

- Panel real de la **Frieren Wiki** (capítulo 41, la llegada al frente
  norte): las montañas del fondo llevan un **screentone de punto fino**
  (degradado: más denso arriba, se aclara hacia la base) y encima **rayas
  verticales blancas** (efecto de luz/lluvia digital superpuesto al tono).
  La multitud usa **línea fina y densa** (crosshatching) sin apenas tono, y
  algunos personajes llevan **patrones a cuadros/rejilla dibujados a mano**
  en el pecho (no es tono mecánico, es trama dibujada) · [Northern Magic
  Corps CH41.png, Frieren Wiki](https://static.wikia.nocookie.net/frieren/images/7/70/Northern_Magic_Corps_CH41.png)
  (visto con Read, recortado y ampliado x3) ✅ (coincide con el estilo
  descrito por Tsukasa Abe en la ficha de la wiki y con las páginas de
  muestra de [Shogakukan Comic](https://shogakukan-comic.jp/book?isbn=9784098508761),
  «試し読みあり») · 595×343
- No encontré un artbook o *making of* que explique la marca exacta de
  tono que usa Abe (Clip Studio tiene tonos integrados: lo más probable,
  pero no confirmado en ninguna entrevista) ⚠️.
- **Equivalente libre para Photoshop/Clip Studio**: generador **open
  source** `svg-halftone` (convierte cualquier imagen a trama de puntos
  SVG editable, círculo/hexágono/diamante) · [GitHub —
  evestera/svg-halftone](https://github.com/evestera/svg-halftone) ·
  licencia MIT (repositorio) ✅. Alternativa sin instalar nada: generador
  web gratuito [HalftoneDots](https://halftonedots.com/halftone-pattern)
  (exporta SVG editable) ⚠️ licencia de uso no aclarada en la web, revisar
  antes de usar en algo público.

**19.2 Grano de papel**

- La **guía oficial «FRIEREN OFFICIAL STARTING GUIDE»** (ya citada en §3,
  `referencias.json` de la biblia) usa un **fondo de papel color crema casi
  blanco** (medido con Pillow sobre el original: `#FDFDFD`-`#FFFFFF`) con
  un **marbleado gris muy sutil** apenas visible ampliado x2, a juego con
  el «papel texturado» que menciona la concept artist **Seiko Yoshioka**
  para los mapas (entrevista en [MdN](https://www.mdn.co.jp/design/features/7151),
  ya citada en la biblia §5.1) ✅ (visto con Read en el recorte
  `frieren_collar_crop.jpg`, medido con Pillow).
- **Textura libre equivalente**: **Paper 006** (fotogrametría, CC0, sin
  crédito obligatorio), papel beige/marrón claro con grano visible ·
  [ambientcg.com/a/Paper006](https://ambientcg.com/a/Paper006) · imagen de
  muestra 1024×1024 (medida) ✅.

**19.3 Pinceladas (acuarela de fondos)**

- Ya documentado en la biblia §5.1: Yoshioka pintó los fondos con **«color
  de acuarela pálida, fresca»** (清涼感あふれる淡い水彩), escaneando texturas de
  papel y tinta reales para mapas y carteles. No repito la cita (ver
  biblia §5.1) — lo que aporto aquí es el **equivalente libre**: no hallé
  un banco de texturas de acuarela con licencia clara y descargable
  directa (Rawpixel y Freepik piden cuenta; `publicdomainpictures.net` no
  respondió al pedir la imagen directa, 2 intentos) ⚠️. Alternativa
  probada: pintar la textura a mano en Photoshop con un pincel de acuarela
  del propio programa (pincel «Acuarela húmeda», incluido de serie) sobre
  **Paper 006** (19.2) como base, o simular el «tono suave» con el filtro
  *Gaussian blur* + textura de papel encima en modo *Multiply*.

**19.4 Patrones de ropa**

- **La camisa de rayas de Frieren** (blanco y negro, bajo la chaqueta
  blanca): medida con Pillow sobre la hoja de modelo oficial
  (`referencias.json` n.º 0 de la biblia, 2718×1920): rayas **blanco puro
  (`#FFFFFF`) y casi negro (`#181818`-`#1E1E1E`)**, de **ancho parecido
  entre sí** (no es una raya fina tipo camisa de vestir: es gruesa, casi
  de payaso/mimo), horizontales sobre el torso, curvándose con el cuerpo
  ✅ (visto y medido en `frieren_collar_crop.jpg`, recorte del original de
  la wiki, con Read + Pillow). Coincide con el texto de la wiki: «striped
  black-and-white shirt» ([Frieren Wiki, Appearance](https://frieren.fandom.com/wiki/Frieren#Appearance),
  ya en `datos-imagen.md`) ✅.
- **Fern, Stark y Himmel no llevan estampado repetido**: sus ropas son de
  **color plano** (blanco, negro, azul, beige) según el texto de la wiki
  (`datos-imagen.md`, «Appearance» de cada uno) — lo único que se repite
  es el **ribete dorado** de Frieren y Fern (ya en §16 de la biblia, no lo
  repito) ✅.
- **Equivalente libre para el patrón de rayas**: patrón SVG de rayas
  gratis en [freesvg.org/stripe-seamless-pattern](https://freesvg.org/stripe-seamless-pattern)
  (dominio público según la política general del sitio) ⚠️ una fuente,
  revisar la licencia exacta del archivo antes de usarlo; alternativa
  segura: dibujar el patrón a mano (es sólo blanco y negro alterno, fácil
  de vectorizar en Illustrator/Photoshop con guías).

**19.5 Emblemas y logos**

- **El «Emblema Sagrado» (Holy Emblem / 聖杖の証)**: colgante que llevan
  los grandes magos (Frieren lo lleva puesto). Forma de **rombo/diamante
  metálico** con líneas que se cruzan en aspa y **remaches redondos** en
  cada punta, dos **cuernos curvos** arriba sujetando una anilla; metal
  gris mate envejecido, con manchas oscuras de óxido · [Frieren Wiki,
  «Holy Emblem»](https://frieren.fandom.com/wiki/Holy_Emblem), imagen
  `Holy_Emblem_EP18.png` 1920×1080 (medida) ✅ — **visto entero con Read**:
  paleta medida con `estilo.py`: `#A4A796` 20%, `#D0ECED` 15%, `#423E3C`
  9% (fondo de vidriera); el metal del emblema en sí ronda `#7A868E` a
  `#A8BECD`, sombreado degradado suave, línea de contorno fina `#62605B`.
  Es un objeto **excelente para un colgante/insignia** de canal (ej. una
  medalla o botón de recursos).
- El **logo de la serie** y su tipografía ya están medidos en la biblia
  §6 (no repito): teal `#…`, mincho espaciado.
- **La sala del examen de primera clase** tiene un **emblema en el atril**
  y vidrieras con motivos geométricos: ya está en `hojas/pantalla_01.jpg`
  n.º 8 (mirar ese número, no hace falta bajar de nuevo) ✅.
- No encontré un **emblema propio de un gremio o país** aparte del Emblema
  Sagrado y el escudo/insignia de la Asociación Mágica Continental (sale
  como el edificio, no como un escudo aislado): busqué «guild mark»,
  «crest», «emblem» en el buscador de texto de la wiki (`srwhat=text`) y
  reviso «Northern Magic Corps» — es un grupo militar, no tiene insignia
  gráfica documentada aparte del uniforme ⚠️.
- **Equivalentes libres para metal grabado**: **Metal 034** (oro liso,
  CC0) · [ambientcg.com/a/Metal034](https://ambientcg.com/a/Metal034),
  imagen de muestra 1024×1024 (medida) ✅ — sirve para el dorado de
  cuellos, hebillas y el Emblema si se quiere dorado en vez de gris.

**19.6 Texturas reales de vestuario (complemento a la tela)**

- **Lana blanca tejida** (para la capa/jacket de Frieren y Fern): **Fabric
  019** (CC0) · [ambientcg.com/a/Fabric019](https://ambientcg.com/a/Fabric019),
  1024×1024 (medida) ✅.
- **Cuero marrón** (botas de todos, correa de Stark): **Leather 037**
  (CC0) · [ambientcg.com/a/Leather037](https://ambientcg.com/a/Leather037),
  1024×1024 (medida) ✅.
- (La madera, la piedra y el pergamino ya están en la biblia §5.4 —
  Poly Haven — no los repito.)

### Punto 23 · Colaboraciones y cruces

**23.1 Marcas, tiendas y eventos (fuera de los videojuegos, que ya están
en la biblia §13)** — fuente principal [collabo-cafe.com, categoría
Frieren](https://collabo-cafe.com/events/category/frieren/) (lista viva,
consultada el 24-sep-2026), cruzada con las webs de cada marca cuando se
pudo:

| Colaboración | Fechas | Qué trae de nuevo | Fuente(s) |
|---|---|---|---|
| **Frieren Café ~Flower Garden~** | desde 31-jul (Tokio Solamachi, luego Osaka/Nagoya) | tema «jardín de flores», ilustraciones exclusivas con trajes florales | [frieren-anime.jp/news/4244](https://frieren-anime.jp/news/4244/) ⚠️ (403 al reabrir; visto por snippet de búsqueda) |
| **Frieren × Sweets Paradise** (5 tiendas) | 3 al 31-mar-2026, escalonado | **uniforme de pastelero chibi** para Frieren, Fern, Stark, Himmel, Heiter y Eisen: gorro blanco de cocinero con cinta de color por personaje, delantal marrón sobre camisa blanca; cada uno con su postre o gesto (Frieren con batidor y su bastón, Fern con uvas, Stark con tarta, Himmel con pastel gigante, Heiter con cuchillo y frutas, Eisen con libro) | [collabo-cafe.com](https://collabo-cafe.com/events/collabo/frieren-cafe-sweets-paradise-2026/) ✅ **visto** el visual completo con Read (imagen 1500×1060) |
| **Frieren «社交界ver.» (versión alta sociedad) × Loft** (Ikebukuro y Namba) | 20-feb a 8-mar-2026 | **ropa de gala nueva, nunca vista en la serie**: Frieren de vestido blanco de hombros descubiertos con una rosa; Fern de vestido lila; Stark de casaca militar roja con charreteras doradas; Himmel con capa roja de príncipe, brazo alzado; Heiter de casaca azul con copa de vino; Eisen de casaca verde con monóculo | [collabo-cafe.com](https://collabo-cafe.com/events/collabo/frieren-high-society-pop-up-store-amnibus-loft-2026/) ✅ **visto** el visual completo con Read (imagen 1500×842), organiza AMNIBUS |
| **Frieren × PARCO POP UP** | (ya en `referencias.json` n.º 5 de la biblia, no repito) | Frieren y Fern leen sentadas en pilas de libros | biblia §3 ✅ |
| **Frieren × Seven-Eleven** (nacional) | 24-sep a 7-oct-2026 | campaña de helados con regalo de acrílicos (ilustración nueva no confirmada) | [collabo-cafe.com](https://collabo-cafe.com/events/collabo/frieren-seven-eleven-campaign-2026/) ⚠️ una fuente |
| **Frieren × Real Escape Game** | desde 10-sep-2026, Harajuku y más ciudades | (ya en biblia §13.1, no repito) | — |
| **Frieren × USJ (Universal Studios Japan)**, restaurante temático | 30-may-2026 a 11-ene-2026 (año siguiente) | menú temático | [collabo-cafe.com](https://collabo-cafe.com/events/collabo/frieren-usj-osaka-restaurant-2026/) + [Famitsu](https://www.famitsu.com/article/202511/58865) (ya citado en biblia §13.1) ✅ |
| **Frieren × Abeno Harukas 300** (mirador, Osaka) | desde 28-abr-2026 | evento colaborativo en el observatorio | [collabo-cafe.com](https://collabo-cafe.com/events/collabo/frieren-benoharukas-300-2026/) ⚠️ una fuente |
| **Frieren × librerías (feria «Vermeer Exhibition»)** | desde 20-jul-2026 | promoción cruzada en librerías de todo Japón | [collabo-cafe.com](https://collabo-cafe.com/events/collabo/frieren-vermeer-exhibition-bookstore-fair-2026/) ⚠️ una fuente |
| **Cápsulas «Pico Pale» (metal charm marker)** | desde 29-ago-2026 | llaveros metálicos en máquinas expendedoras | [collabo-cafe.com](https://collabo-cafe.com/events/collabo/frieren-pico-pale-metal-charm-marker-2026/) ⚠️ una fuente |
| **Figuras «Noodle Stopper»** (premios de salón) | desde ago-2026 | figuras premio nuevas | [collabo-cafe.com](https://collabo-cafe.com/events/collabo/frieren-noodle-stoper-prize-2026/) ⚠️ una fuente |
| **Uniqlo UT / GU** | (fecha exacta no confirmada) | camisetas gráficas con arte de la serie | búsqueda en inglés (TikTok, Instagram, Facebook de tiendas GU) ⚠️ varias fuentes de segunda mano, ninguna oficial de Uniqlo/GU directa: **no verificado al 100%**, tratar con cautela |

**23.2 Figuras oficiales (su pose es una referencia 3D real)** — fuente:
[Good Smile Company](https://www.goodsmile.com), Funko, POP MART (todas
**tiendas oficiales licenciadas**, no fan-made; la pose está esculpida por
un profesional, sirve de referencia de volumen):

| Figura | Tamaño | Pose / qué trae | Fuente |
|---|---|---|---|
| **Nendoroid Frieren** | ~100 mm | 3 caras (neutra, «pilla», *chibi*); accesorios: bastón, grimorio, hierba de luna azul | [goodsmile.com/en/product/56111](https://www.goodsmile.com/en/product/56111) ✅ |
| **Nendoroid Stark** | ~100 mm | 3 caras (sonrisa, decisión, llanto); arma; extra de tienda oficial: **«hamburguesa absurdamente grande» + mango** (el gag del cumpleaños, T1-12) | [hobby.dengeki.com/news/2362750](https://hobby.dengeki.com/news/2362750/) ✅ |
| **Nendoroid Himmel** | ~100 mm | 3 caras (decisión, etérea, ojos cerrados); espada; **corona de flor de loto azul** (la escena del ep. 2); extra: anillo espejo de loto | [hobby.dengeki.com/news/2362750](https://hobby.dengeki.com/news/2362750/) ✅ |
| **POP UP PARADE Frieren: Blow Kiss Ver.** | 165 mm | Frieren con **abrigo blanco de invierno cruzado (botones marrones), bufanda azul, botas marrones**, mandando un beso, mano libre extendida; escultor Daigaku, pintura Tomofumi (WATANA BOX) | [goodsmile.com/en/product/60707](https://www.goodsmile.com/en/product/60707) ✅ **visto** con Read (foto de producto 750×1050) |
| **POP UP PARADE Frieren** (estándar) y **Braids Ver.** | 160-165 mm | de pie con el bastón / con trenzas | `datos-imagen.md` (ya recolectado, no repito la búsqueda) ✅ |
| **POP UP PARADE Himmel** | (mm no confirmado) | **espada clavada en el suelo, sonriendo** — pose heroica/de presentación | [natalie.mu/comic/news/671304](https://natalie.mu/comic/news/671304) ⚠️ (la web dio 403 al reabrir; título del artículo describe la pose) |
| **Figura a escala 1/7 «Fern ～追憶のひととき～» (Un momento de nostalgia)** | escala 1/7, ¥22.000, ago-2026 | Fern con el bastón al hombro y una **mariposa azul posándose en su mano libre**, capa negra abierta, base tipo viñeta | [hobby.watch.impress.co.jp/docs/news/2035669](https://hobby.watch.impress.co.jp/docs/news/2035669.html) ✅ **vista** con Read (foto de producto) |
| **Funko Pop! Frieren, Fern, Himmel, Stark** (línea normal) | escala Funko estándar | cada uno con su objeto (bastón, hacha) | [collider.com](https://collider.com/frieren-beyond-journeys-end-figures-funko-pop-images/) + [popshopguide.com](https://www.popshopguide.com/2025/06/18/funko-pop-frieren/) ✅ dos fuentes |
| **Funko Pop! «Frieren en un Mimic»** | ídem | Frieren **siendo «comida» por el cofre mímico** — el gag de §14 hecho figura oficial | [funko.com/pop-frieren-in-a-mimic](https://funko.com/pop-frieren-in-a-mimic/87125.html) (403 al reabrir) + [collider.com](https://collider.com/frieren-beyond-journeys-end-figures-funko-pop-images/) ✅ dos fuentes |
| **Funko Pop! Himmel chase (1/6)** | ídem | Himmel con **corona de hierba de luna azul** (episodio 2) — variante rara | [collider.com](https://collider.com/frieren-beyond-journeys-end-figures-funko-pop-images/) ⚠️ una fuente |
| **Funko Pop! Plus Frieren (Flower Crown)** | tamaño «Plus» (mayor) | Frieren con corona de flores | [funko.com/pop-plus-frieren-flower-crown](https://funko.com/pop-plus-frieren-flower-crown/88552.html) ⚠️ una fuente, no pude reabrir la ficha |
| **POP MART — «Frieren: Beyond Journey's End» series** | *blind box* (caja sorpresa) | serie de figuras coleccionables (no pude confirmar poses una a una) | [popmart.com/us/products/5697](https://www.popmart.com/us/products/5697/frieren-beyond-journey-s-end-series-figures) ⚠️ una fuente |
| **Loungefly × Crunchyroll — mochila y bandolera** | — | mochila de **satén con detalles dorados y rojos**, dije del bastón; bandolera de **piel sintética irisada**, sello dorado en relieve, bastón moldeado en 3D delante | [amazon.com (ficha Loungefly)](https://www.amazon.com/Loungefly-September-2025-Catalog-Item/dp/B0DSQXS48Q) + [merchoid.com](https://www.merchoid.com/loungefly-crunchyroll-frieren-beyond-journey-s-end-crossbody-bag/) ✅ dos fuentes |
| **Crunchyroll Store — bolsa tote exclusiva** | — | bolsa con las **armas icónicas** de la serie estampadas | [store.crunchyroll.com](https://store.crunchyroll.com/products/frieren-beyond-journeys-end-frieren-tote-crunchyroll-exclusive-400000043958.html) ⚠️ una fuente |

**23.3 Cosplay bien hecho (materiales y volumen reales)**

- `datos-imagen.md` ya trajo **17 fotos de cosplay en Wikimedia Commons**
  (Openverse), todas del fotógrafo **Benlisquare**, licencia **CC BY-SA
  4.0**, en convenciones grandes: **Comiket 105 y 107** (Tokio), **Comic
  World Taiwan-Kaohsiung 49**, **SMASH 2025** (Australia) — cosplay de
  **Frieren, Fern y Übel**, tamaños reales de 3793×5702 a 6048×4024 px.
  Son la fuente correcta (convención + fotógrafo acreditado + licencia
  clara), a diferencia de una foto suelta de redes sin crédito.
- ⚠️ **No pude abrir los archivos originales para describir a simple
  vista tela, costura o volumen**: `upload.wikimedia.org` devolvió **429
  (demasiadas peticiones)** en 3 intentos con esperas de 5, 15 y más
  segundos — el propio `AYUDANTE.md` avisa de que somos varios ayudantes
  compartiendo IP y que a veces toca esperar minutos; no insistí más para
  no gastar más acciones. **Pendiente para quien retome**: reintentar
  `curl -L -A "Mozilla/5.0" <url>` de una de estas URLs (todas están en
  `datos-imagen.md`, sección «Fotos con licencia libre») pasados unos
  minutos, y anotar aquí tela/costura/volumen de al menos 2 fotos.
- Lo que sí puedo afirmar con la ficha de Wikimedia (metadatos, no la
  imagen): son fotos **de prensa/archivo en convención**, con cámara
  réplex (una lleva en el nombre «Sony E 10-18mm F4 OSS», dato EXIF de
  archivo), varias tomas del mismo cosplay desde ángulos distintos (10mm,
  12mm, 14mm, 16mm, 18mm) — eso indica una **sesión cuidada**, no una foto
  de pasillo al azar ✅ (dato del propio nombre de archivo, dos o más
  fotos por cosplay).

## Lo mejor para la lámina

- El **Emblema Sagrado** (§19.5): un colgante metálico real, con historia
  dentro de la serie («insignia de gran mago»), perfecto como icono de
  medalla o botón de un canal.
- Las **ilustraciones de colaboración «社交界ver.»** y **Sweets Paradise**
  (§23.1): dan ropa y poses que la serie nunca mostró (gala, repostero) —
  útiles si se quiere una lámina «especial» sin inventar de la nada, todo
  con fuente oficial.
- La **Nendoroid de Stark con la hamburguesa gigante** y el **Funko Pop de
  Frieren en el Mimic** (§23.2): confirman que los propios gags de fan
  (§14 de la biblia) ya son mercancía oficial — se pueden usar sin miedo
  a que «no sea canon».
- Las **rayas negras y blancas gruesas** de la camisa de Frieren (§19.4),
  medidas de verdad: un detalle fácil de olvidar (tapado por la chaqueta)
  pero reconocible si se ve el cuello.
- **Paper 006 + Fabric 019 + Leather 037 + Metal 034** de ambientcg
  (§19.2, 19.5, 19.6): cuatro texturas CC0 sin crédito obligatorio, listas
  para capas de Photoshop.

## No encontré

- ⚠️ **Tela ni costura de las fotos de cosplay a simple vista**:
  `upload.wikimedia.org` dio 429 en los 3 intentos que hice (con esperas
  entre medias); quedan las 17 fotos con su ficha (autor, licencia,
  tamaño) en `datos-imagen.md`, pero no las miré una a una. Búsquedas
  hechas: descarga directa con `curl -A "Mozilla/5.0"` y con cabecera de
  navegador distinta, y por la página de archivo de Commons (esta sí
  respondió 200, pero es la página, no la imagen).
- ⚠️ **Ninguna entrevista o *making of*** que diga qué marca de tono usa
  Tsukasa Abe, ni qué pinceles concretos, en la parte de manga (sí está
  documentado el estilo de fondos del anime por Yoshioka, ya en la
  biblia). Busqué en japonés («作画 インタビュー», «トーン») y en inglés
  («art style screentone hatching»): salen artículos generales sobre el
  manga, ninguno técnico. El artbook oficial («FRIEREN ART WORKS»,
  Kioon éditions en Francia) podría tenerlo, pero no vi su contenido, sólo
  su existencia.
- ⚠️ **Licencia exacta del patrón de rayas de freesvg.org** y del
  generador **HalftoneDots**: sus páginas no dejan clara la licencia
  archivo por archivo; anoté ambos con esa reserva.
- ⚠️ **La colaboración Uniqlo/GU** no la pude confirmar en una fuente
  oficial de Uniqlo o GU (sólo redes de terceros la mencionan): dejarla
  como «por confirmar», no como dato firme.
- ⚠️ **Poses una a una de la serie POP MART** y **tamaño en mm de POP UP
  PARADE Himmel**: sus páginas no las detallan en el resumen que pude
  leer; `natalie.mu` y `funko.com` dieron 403 al reabrir (2 intentos cada
  una, no insistí más).
- ⚠️ **Textura de acuarela libre y descargable directa**: probé
  `publicdomainpictures.net` (no respondió al pedir la imagen, 2
  intentos) y Rawpixel/Freepik (piden cuenta): dejo la alternativa de
  pincel de Photoshop en su lugar (§19.3).


## Bitácora de búsqueda

Partí de `partes/datos-imagen.md` (no repetí esas consultas de AniList,
Fandom, Danbooru, Safebooru, Wallhaven, Sketchfab ni Openverse) y de
`herramientas/seccion.py 33-frieren --indice` para ver qué faltaba.

**Buscador web** (13 búsquedas de mi cupo de ~50):
- Inglés: «Frieren manga Kanehito Yamada Tsukasa Abe art style screentone
  hatching linework»; «free manga screentone halftone brush pack Procreate
  Clip Studio CC0»; «free seamless stripe pattern SVG CC0 fabric texture
  generator»; «open source halftone dot pattern generator SVG free CC0
  comic manga»; «Frieren art book making of interview brush pencil
  watercolor paper texture»; «free watercolor paper texture CC0 public
  domain high resolution wet-on-wet bleed»; «Frieren official figure Good
  Smile Company Nendoroid POP UP PARADE»; «"Frieren" Uniqlo UT
  collaboration t-shirt»; «Frieren Funko Pop official figure release»;
  «Frieren Loungefly bag Crunchyroll store exclusive collaboration».
- Japonés: «葬送のフリーレン 漫画 トーン 作画 インタビュー»; «Frieren コラボ
  カフェ 期間限定 ポップアップストア 2026»; «グッドスマイルカンパニー
  フェルン シュタルク ヒンメル フィギュア 葬送のフリーレン».

**Red directa** (API y descargas, sin gastar buscador):
- **Frieren Wiki (Fandom)**: `api.php?action=query&list=search` para
  «emblem», «crest», «guild mark», «Continental Magic Association»;
  `action=parse&prop=wikitext` y `action=query&prop=imageinfo` para
  **Holy Emblem**, **Continental Magic Association** y **Northern Magic
  Corps** (imágenes e info de tamaño).
- **ambientcg.com API** (`/api/v2/full_json`): texturas CC0 de **paper**,
  **fabric**, **leather**, **glass**, **gold**, **wool**, **linen**;
  medidas las miniaturas 1024×1024 de Paper006, Fabric019, Leather037 y
  Metal034 con Pillow.
- **Openverse API**: «halftone screentone pattern» y «old paper texture
  grain» — sin resultados útiles con licencia clara.
- **GitHub**: encontrado `evestera/svg-halftone` (MIT) por el buscador,
  no lo cloné (no hacía falta, es una web tool también).
- **collabo-cafe.com** (listado y fichas de eventos), **goodsmile.com**,
  **hobby.dengeki.com**, **hobby.watch.impress.co.jp**, **collider.com**:
  leídos con WebFetch.
- **Descargas directas con `curl`** (medidas con Pillow y con
  `herramientas/estilo.py`): hoja oficial de Frieren (recortes de cuello y
  camisa), Holy Emblem, Northern Magic Corps (panel de manga, con zoom
  x3), figura Blow Kiss Ver., visual Sweets Paradise, visual «社交界ver.»,
  foto de la figura a escala 1/7 de Fern, 4 miniaturas CC0 de ambientcg.

**Fallos y cómo los resolví**:
- `frieren-anime.jp` y `natalie.mu`: **403** al reabrir (funcionaron por
  snippet de búsqueda la primera vez) — usé el snippet, no insistí una
  tercera vez.
- `funko.com`: **403** en las dos fichas que probé — me quedé con
  `collider.com` como fuente (dos fuentes igualmente, por `popshopguide.com`
  citado dentro del resumen).
- `upload.wikimedia.org`: **429** (límite compartido entre ayudantes) en
  3 intentos con esperas crecientes — anotado en «No encontré», no
  reintenté una cuarta vez.
- `publicdomainpictures.net`: sin respuesta al pedir la imagen — 2
  intentos, cambié de estrategia (§19.3).
