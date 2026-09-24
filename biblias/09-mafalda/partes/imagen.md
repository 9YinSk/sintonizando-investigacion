# Parte del investigador de IMAGEN · Mafalda (09-mafalda)

Puntos de `ENCARGO.md`: **1** (arte oficial), **3** (fan art y 3D con licencia),
**15** (vestuario), **16** (fondos y paisajes) — ya estaban en `biblia.md` y aquí
confirmo lo dudoso con una segunda fuente y añado lo nuevo — y **19** (texturas
2D) y **23** (colaboraciones y cruces), que son puntos nuevos y no existían.

Parto de `partes/datos-imagen.md` (no repito esas consultas: Danbooru/Safebooru
dieron sobre todo ruido de otros personajes porque Mafalda no es un personaje
de anime; lo único que usé de ahí fueron los Sketchfab y los Openverse, abajo
verificados) y de `python3 herramientas/seccion.py 09-mafalda --rol imagen`.

Trabajo pesado (imágenes bajadas, hojas de trabajo) en
`/tmp/claude-0/trabajo/09-imagen/`. Las 3 hojas finales están en `hojas/`.

---

## 1 · Arte oficial (punto 1) — confirmo lo dudoso y añado

### Confirmado / corregido de lo que ya estaba en la biblia (sección 3)
- **Manolito y Susanita se sumaron a la estatua de Mafalda en San Telmo el 29
  de septiembre de 2014** (por los 50 años, mismo escultor Pablo Irrgang,
  supervisado por Quino) ✅ — antes sólo tenía una fuente (Asturias.com) con
  el mes aproximado; confirmado con fecha exacta en dos fuentes nuevas:
  [iProfesional](https://www.iprofesional.com/notas/197131-Para-los-50-aos-de-Mafalda-este-lunes-se-le-sumarn-Susanita-y-Manolito-en-San-Telmo),
  [La Capital de Rosario](https://www.lacapital.com.ar/informacion-general/susanita-y-manolito-acompanan-mafalda-n440946.html).
- **El vestido de Netflix SÍ lleva lunares negros** (no era una nota suelta):
  aparece igual en varios medios ✅
  ([Emol](https://www.emol.com/noticias/Espectaculos/2026/04/08/1196675/revelan-primera-imagen-serie-mafalda.html),
  y coincide con [El Diario NY](https://eldiariony.com/2026/04/08/netflix-muestra-primera-foto-de-la-serie-animada-de-mafalda/)).
  Sube de ⚠️ a ✅. Además: **un dibujo oficial distinto** (ver más abajo, el de
  la Mafalda Wiki) también tiene lunares negros sobre rojo — confirma que es
  un patrón que Quino/los herederos repiten, no una invención de Netflix.
- **CORRECCIÓN — el Paseo de la Historieta NO tiene 15 paradas**: la biblia
  llevaba ese número con una sola fuente (Welcome Argentina). Con fuentes
  mejores: se inauguró el **20 de julio de 2012** con Mafalda, Susanita y
  Manolito, y hoy tiene **más de 20 estatuas y 7 murales** (otra fuente da 19
  esculturas) ✅
  ([La Nación, jul-2025](https://www.lanacion.com.ar/que-sale/de-el-eternauta-a-mafalda-el-mapa-de-esculturas-del-paseo-de-la-historieta-de-san-telmo-nid22072025/),
  [Infobae, jul-2025](https://www.infobae.com/sociedad/2025/07/24/de-patoruzito-a-el-eternauta-todas-las-esculturas-del-paseo-de-la-historieta-en-san-telmo-para-conocer/),
  [Buenos Aires Ciudad, oficial](https://buenosaires.gob.ar/noticias/paseo-de-la-historieta-0)).
  Va desde Chile y Defensa (Mafalda) hasta el Museo del Humor (La Jirafa de
  Mordillo), cruzando San Telmo, Monserrat y Puerto Madero.

### Nuevo: una CUARTA estatua oficial de Mafalda (Barranco, Lima, Perú)
No estaba en la biblia. Muy bien documentada (6+ fuentes) ✅:
- **8ª escultura de Mafalda en el mundo**, en una banca del **Boulevard Sáenz
  Peña, cuadra 2, Barranco (Lima)**. Escultor: **Pablo Irrgang** (el mismo de
  San Telmo y Oviedo). Comisionada por la **Embajada Argentina en Perú**, con
  aporte de **Pluspetrol y Haug S.A.** Instalada de forma permanente el **21
  de septiembre de 2023**
  ([El Comercio](https://elcomercio.pe/luces/arte/escultura-de-mafalda-sera-instalada-en-lima-el-proximo-21-de-setiembre-conoce-el-lugar-exacto-aqui-mafalda-quino-argentina-barranco-lima-peru-arte-ultimas-noticia/),
  [La República](https://larepublica.pe/sociedad/2023/09/22/mafalda-en-lima-conoce-como-llegar-a-la-escultura-de-la-famosa-caricatura-y-mas-detalles-barranco-embajada-de-argentina-saenz-pena-778360),
  [El Peruano](https://www.elperuano.pe/noticia/223637-paren-el-mundo-mafalda-se-instalo-en-boulevar-de-barranco-fotos),
  [Andina](https://andina.pe/agencia/noticia-paren-mundo-mafalda-se-instalo-boulevar-barranco-fotos-955230.aspx),
  [Embajada Argentina en Perú, oficial](https://eperu.cancilleria.gob.ar/es/inauguramos-una-escultura-de-mafalda-en-barranco-para-celebrar-la-amistad-argentino-peruana)).
- **Vestido y moño color AMARILLO ORO**, el color de la bandera del distrito
  de Barranco (elegido a propósito, no es el verde de San Telmo ni el rojo de
  Oviedo) ✅. Fotos en Wikimedia Commons, autor **Omar Vega Ramos**, **CC
  BY-SA 4.0** (marzo 2025)
  ([archivo](https://commons.wikimedia.org/wiki/File:Estatua_de_Mafalda_en_Lima,_Per%C3%BA_02.jpg)).
  → hoja `arte_01.jpg` #6.

### Otros sitios reales con Mafalda (Wikimedia Commons; búsqueda directa a su
API, `generator=search&gsrsearch=Mafalda Quino`, namespace 6)
- **Plaza Mafalda, barrio de Colegiales, Buenos Aires** — sitio real
  DISTINTO de San Telmo, con el nombre de Mafalda. Foto de **Roberto
  Fiadone**, **CC BY-SA 4.0**, 2015, 4595×3361 (medida)
  ([archivo](https://commons.wikimedia.org/wiki/File:Plaza_Mafalda_Colegiales_Quino.JPG))
  ⚠️ (una sola fuente: la ficha de la foto; no encontré nota de prensa que
  describa esta plaza en particular, sólo que existe con ese nombre).
  → hoja `arte_01.jpg` #8.
- **Puerta rotulada "Quino/Mafalda"** — puerta verde de vidrio con una
  calcomanía de Mafalda y una placa. Foto de Roberto Fiadone, **CC BY-SA
  3.0**, 2013, 2848×2134
  ([archivo](https://commons.wikimedia.org/wiki/File:Puertas_Quino_Mafalda.jpg))
  ⚠️ (no pude leer el texto exacto de la placa en la miniatura).
  → hoja `arte_01.jpg` #12. Sirve de referencia de "objeto real con rótulo"
  para el concepto de lámina.
- **Merchandising oficial del 60º aniversario** (2024): lata/estuche con
  Mafalda soplando una vela y el texto **"¡Feliz aniversario, Mafalda!"**
  sobre fondo crema con lunares dorados. Foto de **Emilio Gómez Fernández**,
  **CC BY-SA 4.0**, dic-2024, 4624×3472
  ([archivo](https://commons.wikimedia.org/wiki/File:Mafalda_Merchandising_-_60th_anniversary.jpg)).
  Ver también punto 23. → hoja `arte_01.jpg` #5.

### Arte a color oficial nuevo (Mafalda Wiki, es.fandom — API directa,
`prop=imageinfo`, 48 imágenes bajadas con `Referer: https://www.fandom.com/`
y medidas con Pillow; no las tenía la biblia)
- **"Mafaldapensativa"**: dibujo a color de Mafalda sentada en un banco
  verde, pensativa, **vestido rojo con lunares negros y moño rojo**, medias
  blancas. 1800×1600 (medida) ✅. Colores medidos con Pillow (promedio de los
  píxeles más comunes de la imagen):
  **rojo `#E00025`**, **negro `#000000`** (lunares, pelo, contorno), **piel
  `#F7BA98`**, **verde del banco `#9ACF15`**, blanco `#FFFFFF`.
  → hoja `arte_01.jpg` #3. Es la mejor referencia de color medida de toda la
  biblia (las demás eran "propuesta, sin medir").
- Portadas: **Mafaldalibross.png** (1280×1485, montaje de tapas Lumen),
  **Todamafalda.jpg** (477×684, tapa naranja de "Todo Mafalda"),
  **Netflixalda.png** (1200×675, el logo/imagen de la revelación Netflix),
  **Mafaldamundo.JPG** (574×332, Mafalda con el globo terráqueo — ver
  punto 19), **Almacensantelmo.jpg** (600×600, foto real del mural del
  almacén Don Manolo en San Telmo).

### Las hojas de contacto (con Pillow, API de la wiki en español)
`investigar_serie.py` no sabe usar `mafalda.fandom.com/es/`, así que consulté
la API a mano (`list=allimages`, `iiprop=url|size`) y monté las hojas yo mismo
con Pillow:
1. **`hojas/personajes_01.jpg`**: los 18 personajes con imagen en la wiki
   (Mafalda, Felipe, Manolito, Susanita, Libertad, Miguelito, Raquel, Guille,
   Muriel, Tía Paca, los padres, Don Basilio la tortuga, etc.). Sirve para
   silueta y proporciones de cada uno (punto 15).
2. **`hojas/objetos_01.jpg`**: el almacén Don Manolo (dibujo y foto real), la
   plaza, gags icónicos (la pelota, la burocracia-tortuga, los
   extraterrestres), Quino dibujando. Sirve para fondos y objetos (puntos 1,
   4, 16 — de otros roles, pero la imagen ya está lista).
3. **`hojas/arte_01.jpg`**: la más completa — portadas, el dibujo a color
   oficial, la revelación de Netflix, la lata del 60º aniversario, **3
   estatuas distintas** (San Telmo, Lima, y de fondo la de Oviedo se ve en la
   sección 3 de la biblia), la Plaza Mafalda de Colegiales, los peluches
   oficiales de la Feria de San Telmo, la tira del globo terráqueo y un
   crossover fan ("Mafaltrix"). Cubre los puntos 1, 15, 16, 19 y 23 a la vez.

---

## 2 · Fan art y 3D con licencia (punto 3) — confirmo licencias por API

La biblia (sección 5) tenía varios modelos de Sketchfab marcados ⚠️ "no pude
ver la licencia". Los comprobé **uno por uno con la API de Sketchfab**
(`api.sketchfab.com/v3/models/<uid>`, el campo `license` viene en la
respuesta) — ahora son ✅:

| Modelo | Autor | Licencia (API) | Enlace |
|---|---|---|---|
| Mafalda | andresspa79 | **CC Attribution (CC BY)** ✅ | [ver](https://sketchfab.com/3d-models/mafalda-9a5f14636a254068b71dddd58fcc3d46) |
| Mafalda | Aleshi2002 | **CC Attribution (CC BY)** ✅ | [ver](https://sketchfab.com/3d-models/mafalda-662e483a459b4b878beb1b53a2bbf26e) |
| Mafalda's hair | KirbyDreamFan | **CC Attribution (CC BY)** ✅ | [ver](https://sketchfab.com/3d-models/mafaldas-hair-c508c8e203e54d6d950d53f7483ca08b) |
| Mafalda | larafabiano | **CC Attribution (CC BY)** ✅ | [ver](https://sketchfab.com/3d-models/mafalda-926ebd1e829f41a1a5e20a632cd6f594) — ojo: es un `uid` distinto al que trae la biblia para el mismo autor; hay dos modelos de larafabiano, ambos CC BY |
| **Royal Mail postbox** (el buzón, punto 3/objetos) | Karolisbutenas | **CC Attribution-NonCommercial-ShareAlike (CC BY-NC-SA)** ✅ | [ver](https://sketchfab.com/3d-models/royal-mail-postbox-bcfb6e6252bb4934899f92bb6f4a8870) — confirma lo que la biblia sólo suponía |
| Mailbox | PagDev | **CC Attribution (CC BY)** ✅ | [ver](https://sketchfab.com/3d-models/mailbox-edcf56d8772a47868a6da8dfc1a42694) — confirma la suposición de la biblia |
| Old Mailbox | yoyavova | **CC Attribution (CC BY)**, descargable ✅ | [ver](https://sketchfab.com/3d-models/old-mailbox-496244e610f340179abd8360ee185763) — confirma la suposición de la biblia |

**Conclusión para el buzón (objeto del plan de este canal)**: el modelo de
PagDev o el de yoyavova (ambos CC BY, sólo piden crédito) son más seguros de
usar que el de Karolisbutenas (CC BY-NC-SA, más restrictivo aunque el
servidor no vende nada).

### Fan art nuevo con licencia real (mejor que Pixiv/DeviantArt sin licencia)
- **"Mafaltrix Recargada"**: cartel/mural que parodia a Mafalda y sus amigos
  vestidos como en *Matrix Reloaded* (gabardinas, lentes oscuros), fotografiado
  en un local. Foto de **huguito**, Flickr vía Openverse, **CC BY-NC-SA 2.0**,
  1024×768 (medida)
  ([foto](https://live.staticflickr.com/225/488129852_970e25aba5_b.jpg)).
  Es un crossover **fan**, no oficial — sólo referencia de pose de grupo "en
  acción", nunca para pegar. ⚠️ no identifiqué al autor original del dibujo,
  sólo a quien tomó la foto (la licencia es de la FOTO).
- Peluches oficiales de la Feria de San Telmo (ver punto 23): vestido de
  lunares **blancos** sobre rojo — variante de color distinta a la del dibujo
  de la wiki (lunares negros). Útil para ver que el color exacto del lunar
  varía según el producto, no la forma del patrón.

---

## 3 · Vestuario, con hex medidos (punto 15)

### Colores medidos con Pillow (antes la biblia decía "propuesta, sin medir")
- **Vestido y moño de Mafalda, dibujo oficial de la wiki**: rojo `#E00025`,
  lunares negros `#000000` ✅ (medido directo, ver punto 1).
- **Estatua de San Telmo** (verde): medí el promedio de píxeles verdes en
  **dos fotos distintas** con licencia CC BY —
  [blmurch](https://live.staticflickr.com/3516/3924482936_a2e9ffd019_b.jpg):
  promedio **`#4B6736`** (verde oliva);
  [Nico Kaiser](https://live.staticflickr.com/8108/8638774678_6893e0887b_b.jpg):
  zona en sombra **`#29311A`** (más oscuro). ✅ **Corrijo** la ficha de la
  biblia: es un **verde oliva/musgo**, no un "verde claro" o menta.
- **Estatua de Lima (Barranco)**: **amarillo oro**, según la prensa (el color
  de la bandera de Barranco) — se ve claramente dorado/mostaza en la foto de
  Wikimedia Commons, pero **no medí el hex exacto** porque sólo tengo una
  miniatura de 500 px; si hace falta el hex exacto, bajar el original
  (4032×3024) del [archivo de Commons](https://commons.wikimedia.org/wiki/File:Estatua_de_Mafalda_en_Lima,_Per%C3%BA_02.jpg). ⚠️ color confirmado, hex no medido.

### Vestuario de personajes secundarios (la tabla de la biblia los tenía "sin
dato"; lo saqué del wikitext de la Mafalda Wiki vía su API,
`action=parse&prop=wikitext`, y crucé cada uno con una segunda fuente)
- **Susanita**: vestido **negro** + remera o sudadera de manga larga debajo;
  su ropa "suele variar" ✅ dos fuentes independientes
  ([Mafalda Wiki](https://mafalda.fandom.com/es/wiki/Susanita),
  [historietamania.com](https://www.historietamania.com/susanita/) — coincide
  casi palabra por palabra, así que probablemente una copió de la otra, pero
  son dos publicaciones distintas).
- **Miguelito**: **overol** (mameluco) + sudadera o suéter **a rayas** debajo;
  su rasgo más marcado es el pelo tipo "lechuga" ✅ dos fuentes
  ([Mafalda Wiki](https://mafalda.fandom.com/es/wiki/Miguelito),
  [historietamania.com](https://www.historietamania.com/) vía el mismo
  resumen). No estaba nada de Miguelito en la tabla de vestuario de la
  biblia: **falta añadirlo**.
- **Manolito**: saco/chaqueta + camisa + pantalón corto, siempre con lápiz y
  libreta. El dato nuevo: **"a diferencia de los demás personajes, casi nunca
  se le ha visto con ropa diferente"** (su ropa NO cambia, al revés que
  Susanita) ⚠️ una sola fuente (Mafalda Wiki); no crucé esta frase exacta con
  una segunda, aunque el saco+libreta ya estaba confirmado en la biblia con
  otra fuente.
- **Felipe**: sigue **sin color de ropa documentado** en ninguna fuente que
  encontré (ni la wiki, ni historietamania, ni las webs oficiales lo dicen).
  Dejo esto en «No encontré», no invento un color.

---

## 4 · Ciudades, paisajes y fondos de pantalla (punto 16)

- **Plaza Mafalda, Colegiales** (Buenos Aires): sitio real nuevo, ver punto 1.
  ⚠️ una sola fuente (la ficha de la foto de Commons).
- **Fondos de pantalla oficiales**: seguí sin encontrar. Repetí la búsqueda
  con la red abierta ("Mafalda wallpaper oficial", "fondo de pantalla Mafalda
  4k site:quino.com.ar") y sólo aparecen tableros de Pinterest con tiras
  coloreadas por fans (nunca la fuente original) y fondos de fans sueltos sin
  autor claro. Confirmo el hallazgo de la biblia: no hay fondos de pantalla
  oficiales publicados. ⚠️

---

## 5 · Texturas 2D (punto 19 — NUEVO, no existía en la biblia)

- **Mafalda no usa trama de manga** (screentone): es una tira de prensa
  entintada a mano, en blanco y negro sólido, sin puntos de trama dibujados.
  Lo confirmo mirando las hojas de contacto (líneas sólidas, negros planos,
  sin semitonos). El "grano" que se ve en libros viejos es del **papel y la
  impresión**, no un recurso de dibujo — eso ya está cubierto por las
  texturas de papel del punto 4/6 de la biblia (ambientcg Paper001/003/005,
  CC0); no repito esa búsqueda.
- **El patrón de tela que sí hay que replicar: los lunares (polka dots) del
  vestido de Mafalda.** Los vi en tres soportes oficiales distintos, cada uno
  con un color de lunar diferente:
  - Negros sobre rojo → dibujo oficial de la wiki (punto 1).
  - Blancos sobre rojo → peluches oficiales, Feria de San Telmo (punto 23).
  - Dorados sobre crema → lata del 60º aniversario (punto 1/23).
  Es el elemento más simple y reconocible para decorar cualquier objeto de la
  lámina sin tener que dibujar la cara del personaje.
- **Texturas y pinceles libres equivalentes** (con licencia comprobada en la
  propia web, no de memoria):
  - **Trama tipo cómic (halftone), gratis**: paquete de 12 texturas de trama
    distorsionada, Spoon Graphics
    ([enlace](https://blog.spoongraphics.co.uk/freebies/free-pack-of-12-distressed-halftone-pattern-textures))
    ⚠️ dice "gratis para descargar"; revisar el término exacto (uso comercial)
    antes de usarla fuera del servidor.
  - **Puntos de trama (halftone), 10 SVG + 10 PNG**, Unblast
    ([enlace](https://unblast.com/free-halftone-dot-textures-svg-png/)) ⚠️ el
    sitio dice "uso personal y comercial", no leí el texto legal completo.
  - **Pinceles de tinta gratis para Procreate** ("FREE Comic Ink Set", +20
    pinceles de entintado y efectos), de georgvw
    ([Gumroad](https://georgvw.gumroad.com/l/free_procreate_ink_brushes)) ✅
    declarado gratis por el propio autor.
  - **Patrón de lunares**: es una geometría simple, sin derechos de autor
    propios; lo más seguro es generarlo directo en Photoshop/Procreate (un
    pincel redondo con espaciado regular) en vez de bajar un asset con
    licencia dudosa. Si se quiere un overlay ya hecho, Vecteezy tiene varios,
    pero piden cuenta gratuita o dan atribución obligatoria ⚠️.
- **Emblemas y logos**: la tira no tiene un "logo de facción" como una
  franquicia de juegos. Lo más parecido a un emblema es **el globo
  terráqueo** que Mafalda mira y toca (aparece en la tira "Mafalda y el
  mundo", en portadas, y es su gesto más citado — ver hoja `arte_01.jpg`
  #10), y el rótulo **"mafalda"** en minúsculas y redondeado usado en libros y
  en la revelación de Netflix. El análisis de esa letra (si trae tildes, ñ,
  etc.) es del punto 5, que hace el investigador de texto; aquí sólo dejo las
  imágenes fuente (`Mafaldamundo.JPG`, `Netflixalda.png`, `Todamafalda.jpg`).

---

## 6 · Colaboraciones y cruces (punto 23 — NUEVO, no existía en la biblia)

### El 60º aniversario (2024) fue la colaboración más grande
- **Mafalda visitó la sede de la ONU en Nueva York**: una estatua (escultora
  la misma persona que las de San Telmo/Oviedo/Lima, **Pablo Irrgang**)
  recorrió la sala de intérpretes de español y la sala donde sesiona el
  Consejo Económico y Social (ECOSOC). Lo organizó el **Gobierno de la Ciudad
  de Buenos Aires** ✅ fuente oficial de Naciones Unidas:
  [Noticias ONU](https://news.un.org/es/story/2024/11/1534621),
  [ONU Argentina, oficial](https://argentina.un.org/es/284639-sus-60-a%C3%B1os-mafalda-cumpli%C3%B3-el-sue%C3%B1o-de-ser-int%C3%A9rprete-en-la-onu),
  [Infobae](https://www.infobae.com/cultura/2024/11/26/mafalda-conquista-nueva-york-llego-a-la-onu-y-participo-de-los-emmy/).
- **Mafalda fue la primera figura latinoamericana en subir al escenario de
  los Emmy Internacionales** (52ª edición), entregando 3 premios (Animación,
  Factual & Entertainment, Live-Action) ✅ mismas fuentes.
- **Nestlé + El Ocho Licencias**: colección conmemorativa de tabletas de
  chocolate Extrafino con **tazas y latas de colección con frases icónicas**
  de la tira ✅ ([sweetpress.com](https://www.sweetpress.com/actualidad/el-ocho-balance-positivo-de-la-colaboracion-entre-mafalda-y-nestle-MC17269063)).
  Foto real de una de esas latas (¡feliz aniversario, Mafalda!) en Wikimedia
  Commons — ver punto 1.
- **Chocolate Jack (México)**: colección de **24 figuras sorpresa** con
  Mafalda, Felipe, Susanita, Miguelito, Libertad, Guille y los padres ⚠️ una
  sola fuente, un blog no oficial
  ([TVLaint](https://www.tvlaint.com/2026/03/chocolate-jack-lanza-una-coleccion-de.html));
  no crucé con un anuncio oficial de la marca.

### Otras colaboraciones oficiales
- **Ecovidrio** (España, 2022): campaña de concienciación sobre reciclaje de
  vidrio, con tiras temáticas de Mafalda y **contenedores decorados** en
  Alcalá de Henares, Fuenlabrada, San Sebastián de los Reyes y Talavera de la
  Reina ✅ dos fuentes:
  [sweetpress/DARetail](https://distribucionactualidad.com/mafalda-se-une-a-ecovidrio-para-concienciar-sobre-el-reciclaje-de-envases/),
  [Ecovidrio, sitio oficial de la marca](https://www.ecovidrio.es/mafalda).
- **UNICEF**: Quino ilustró a Mafalda y sus amigos para la **Declaración de
  los Derechos del Niño** en 1976-77, y de nuevo en **2018** para los 30 años
  de la Convención sobre los Derechos del Niño, a pedido de UNICEF ✅ tres
  fuentes: [Campus FAD](https://www.campusfad.org/blog/accion-magistral/los-derechos-del-nino-mafalda-y-la-integracion/),
  cuenta oficial [@MafaldaDigital en X](https://x.com/MafaldaDigital/status/1464625147340595206),
  [UNICEF Argentina en Facebook](https://www.facebook.com/UNICEFargentina/videos/mafalda-10-derechos-fundamentales-de-los-ni%C3%B1os-ni%C3%B1as-y-adolescentes/450039782172277/).
- **Estampillas postales**: Argentina emitió su primer sello de Mafalda hacia
  1991, y en 2018 Correo Argentino sacó un **cuadernillo con 3 estampillas**
  ($32, $53 y $85) más 2 hojitas — la pieza filatélica más vendida de ese año
  ✅ ([La Nación](https://www.lanacion.com.ar/cultura/mafalda-cerati-sandro-estrellas-estampillas-mas-vendidas-nid2204025/)).
  Italia también sacó un sello propio (Istituto Poligrafico e Zecca dello
  Stato, tarifa B, con Mafalda en tres expresiones típicas) ⚠️ una fuente de
  resumen, no verifiqué el año exacto.
- **Concurso Internacional de Ilustración Mafalda**: cartel de 53×84 cm,
  abierto a mayores de 18 años de cualquier país, máximo 3 obras por
  participante (bases de la edición 2026 en PDF) ⚠️ alojado por una fundación
  española (fundacioncinemascomics.com); no confirmé si tiene aval directo de
  los herederos de Quino.

### Estatuas internacionales (además de San Telmo y Oviedo, ya en la biblia)
- **Barranco, Lima, Perú** (2023) — ver punto 1, muy bien confirmada.
- **Madrid** (nov-2024) — la biblia ya la menciona con una sola fuente
  (Infobae); no encontré una segunda. Sigue ⚠️.

### Figuras oficiales y cosplay
- **Peluches oficiales**, vistos a la venta en la Feria de San Telmo: vestido
  de lunares **blancos** sobre rojo, mangas y pies amarillos, zapatos negros
  ✅ foto real
  ([wallyg, Flickr/Openverse, CC BY-NC-ND 2.0](https://live.staticflickr.com/8300/8004984465_fa8d4d0556_b.jpg)).
- **Cosplay bien hecho, con materiales y volumen reales: no encontré**. Sólo
  hay disfraces caseros simples (peluca negra alborotada + vestido rojo) en
  DeviantArt y Flickr, sin trabajo de tela o volumen elaborado como pide el
  encargo. Lo dejo en «No encontré» en vez de inventar que existe.
- **Crossover fan** "Mafaltrix Recargada" (Matrix) — ver punto 2/3.

---

## Lo mejor para la lámina

1. La estatua de San Telmo (verde oliva **medido**, `#4B6736`), sentada en un
   banco blanco real, es el objeto+pose más fácil de llevar a Blender: banco,
   volumen, luz de tarde (hoja `arte_01.jpg` #7).
2. El patrón de **lunares** del vestido (negro, blanco o dorado según el
   soporte oficial) hace reconocible a Mafalda sin dibujar la cara: sirve para
   decorar el buzón o cualquier objeto del canal #sugerencias.
3. La pose de Mafalda con el **globo terráqueo** (`Mafaldamundo.JPG`, hoja
   `arte_01.jpg` #10) es la que mejor encaja con un foro de "propuestas para
   mejorar el mundo/servidor".
4. Tres estatuas oficiales, tres colores distintos (verde San Telmo, rojo
   Oviedo, dorado Lima) prueban que **no hay un color único**: lo más seguro
   es dejar el vestido en blanco y negro, como la tira, y reservar el color al
   entorno (buzón, papel, luz).
5. La lata oficial del 60º aniversario (`Mafalda_Merchandising_-_60th_a.jpg`,
   hoja `arte_01.jpg` #5) muestra cómo el propio equipo de Mafalda combina
   tipografía redondeada + lunares dorados + frase icónica en un objeto: es
   la referencia más directa de "estilo de merchandising oficial" para
   diseñar el buzón.

---

## No encontré (con las búsquedas hechas)

- ⚠️ **Fondos de pantalla oficiales en alta**: repetí la búsqueda con la red
  abierta ("Mafalda wallpaper oficial", "fondo de pantalla Mafalda 4k
  site:quino.com.ar"); sólo tableros de fans en Pinterest. Sigue sin haber.
- ⚠️ **Cosplay "bien hecho"** (materiales y volumen reales, punto 23): sólo
  disfraces caseros simples.
- ⚠️ **Segunda fuente para la estatua de Madrid** (nov-2024): sólo Infobae.
- ⚠️ **Autor original del cartel "Mafaltrix Recargada"**: sólo tengo la
  licencia de quien lo fotografió, no de quien lo dibujó.
- ⚠️ **Color de ropa de Felipe**: ninguna fuente lo da (ni oficial ni de fans).
- ⚠️ **Hex exacto del amarillo de la estatua de Lima**: sólo vi una
  miniatura; el original está en Wikimedia Commons a 4032×3024 para quien
  quiera medirlo.
- ⚠️ **Aval oficial del Concurso Internacional de Ilustración Mafalda** por
  los herederos de Quino: no lo confirmé, sólo vi las bases de la fundación
  organizadora.
- ⚠️ **Colaboración con videojuegos** (Fortnite, gachas u otros): busqué
  específicamente ("Mafalda Fortnite OR videojuego colaboración skin gacha")
  y no hay nada — ni skin, ni evento, ni filtración. Mafalda no tiene
  colaboraciones de videojuego conocidas.
- ⚠️ **Café temático o tienda pop-up oficial**: busqué ("Mafalda café
  temático tienda pop-up") y sólo aparecen tazas y productos de merchandising
  sueltos (Amazon, Cafebrería El Péndulo) y menciones vagas a "una tienda
  icónica de Mafalda en Buenos Aires", sin nombre ni dirección verificable.
  No es lo mismo que un café temático real como los hay de otras franquicias.

---

## Bitácora de búsqueda (imagen)

**Búsquedas web (español), 16 en total** — cupo usado: 16/50:
"Mafalda colaboración marca campaña oficial 2020 2021 2022" ·
"Mafalda UNICEF embajadora derechos del niño" ·
"Mafalda estampilla sello postal Argentina" ·
"Mafalda café temático tienda pop-up" ·
"Mafalda Naciones Unidas ONU ilustre visitante ceremonia ONU ilustración ODS" ·
"Mafalda cosplay concurso" ·
"\"Mafalda\" figuras coleccion Comansi OR Fanattik OR muñeco oficial licencia" ·
"halftone dot pattern texture free CC0 png overlay comic" ·
"polka dot seamless pattern free CC0 vector fabric texture" ·
"free ink brush pack Procreate Photoshop comic linework CC0 OR free license" ·
"estatuas Manolito Susanita San Telmo 2014 sumaron esquina Chile Defensa" ·
"Mafalda serie Netflix primera imagen vestido lunares diseño personaje 2026" ·
"\"Paseo de la Historieta\" Buenos Aires cuántas estatuas esculturas recorrido" ·
"Susanita vestido negro Manolito Miguelito overol descripción personajes Mafalda" ·
"estatua Mafalda Lima Perú parque ubicación" ·
"Mafalda Fortnite OR videojuego colaboración skin gacha".

**APIs usadas directamente (sin gastar cupo de buscador)**:
- **Mafalda Wiki** (`mafalda.fandom.com/es/api.php`): `list=allpages` (41
  páginas), `list=allimages&iiprop=url|size|mime` (48 imágenes, todas bajadas
  con `Referer: https://www.fandom.com/` y medidas con Pillow),
  `action=parse&prop=wikitext` para Susanita, Manolito, Felipe, Libertad y
  Miguelito (vestuario y rasgos).
- **Sketchfab** (`api.sketchfab.com/v3/models/<uid>`): 7 modelos comprobados
  uno por uno (licencia real de la API, no adivinada del buscador).
- **Wikimedia Commons** (`commons.wikimedia.org/w/api.php`):
  `generator=search&gsrsearch=Mafalda Quino&gsrnamespace=6` (30 resultados
  con `imageinfo`/`extmetadata`), más consultas puntuales por título para
  autor/licencia/fecha exacta de 4 fotos.
- **GitHub API**: intenté buscar repositorios de texturas de trama
  (screentone); este contenedor la tiene limitada a repos ya configurados
  ("sessions are bound to their configured repositories"), así que resolví
  las texturas por buscador web en su lugar.
- No usé YouTube (pide iniciar sesión desde este servidor); no hacía falta
  para mis puntos, que no llevan vídeo.

**Fotos descargadas y medidas con Pillow** (ancho/alto reales, no de
catálogo): 48 de la Mafalda Wiki + 4 de Openverse/Flickr + 4 de Wikimedia
Commons. **Colores medidos con Pillow**: 5 tonos exactos del dibujo oficial a
color de la wiki, y el verde de la estatua de San Telmo en dos fotos CC BY
distintas (una da un verde más oscuro por estar en sombra: es la misma
estatua, no dos colores).
